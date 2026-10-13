"""Thin wrapper around OpenAI-compatible chat completions with caching and retry."""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any

import yaml


def _load_config(path: str | None = None) -> dict:
    if path is None:
        path = Path(__file__).resolve().parents[1] / "config.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class LLMClient:
    def __init__(self, config: dict | None = None):
        self.cfg = config or _load_config()
        self.model_cfg = self.cfg["model"]
        self.provider = self.model_cfg["provider"]
        self.model_name = self.model_cfg["model_name"]
        self.api_base = self.model_cfg.get("api_base")
        self.temperature = self.model_cfg["temperature_translate"]
        self.max_tokens = self.model_cfg["max_tokens"]

        self.cache_dir = Path(self.cfg["paths"]["outputs"]) / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        if self.provider == "openai":
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise ImportError("pip install openai") from exc
            kwargs = {}
            if self.api_base:
                kwargs["base_url"] = self.api_base
            key = os.environ.get(self.model_cfg.get("api_key_env", "OPENAI_API_KEY"))
            if key:
                kwargs["api_key"] = key
            self.client = OpenAI(**kwargs)
        else:
            raise NotImplementedError(f"provider {self.provider} not supported yet")

    def _cache_key(self, messages: list[dict], temperature: float, max_tokens: int) -> str:
        payload = json.dumps({"m": messages, "t": temperature, "n": max_tokens}, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def chat(self, messages: list[dict], temperature: float | None = None, max_tokens: int | None = None) -> str:
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens

        key = self._cache_key(messages, temperature, max_tokens)
        cache_file = self.cache_dir / f"{key}.json"
        if self.cfg["logging"].get("cache_calls", True) and cache_file.exists():
            return json.loads(cache_file.read_text(encoding="utf-8"))["content"]

        for attempt in range(5):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                content = resp.choices[0].message.content
                if self.cfg["logging"].get("cache_calls", True):
                    cache_file.write_text(json.dumps({"content": content}, ensure_ascii=False), encoding="utf-8")
                return content
            except Exception as exc:
                wait = 2 ** attempt
                print(f"[LLM error] {exc}; retry in {wait}s")
                time.sleep(wait)
        raise RuntimeError("LLM call failed after retries")

    def quick_chat(self, system: str, user: str, temperature: float | None = None) -> str:
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        return self.chat(messages, temperature=temperature)
