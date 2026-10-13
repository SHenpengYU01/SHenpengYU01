"""Evaluator: score a candidate translation on cultural effectiveness."""
from __future__ import annotations

import json
import re
from pathlib import Path

from src.client import LLMClient
from src.skill_manager import Skill


def _load_prompt(name: str) -> str:
    path = Path(__file__).resolve().parents[1] / "prompts" / f"{name}.txt"
    return path.read_text(encoding="utf-8")


def _extract_json(text: str) -> dict:
    # try fenced code block first
    m = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
    if m:
        text = m.group(1)
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # fallback: try to extract the first JSON object
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return {"overall": 3, "dimensions": {}, "diagnosis": "", "suggestions": "", "raw": text}


def evaluate(source: str, candidate: str, reference: str, skill: Skill, client: LLMClient) -> dict:
    system = _load_prompt("evaluate").format(skill_body=skill.render())
    user = f"Source: {source}\nCandidate Translation: {candidate}\nReference Translation: {reference}\n\nOutput JSON only."
    raw = client.quick_chat(system, user, temperature=client.model_cfg["temperature_evaluate"])
    parsed = _extract_json(raw)
    parsed["raw"] = raw
    # ensure overall score exists and is numeric
    if "overall" not in parsed or not isinstance(parsed["overall"], (int, float)):
        parsed["overall"] = 3
    parsed["overall"] = max(1, min(5, int(round(parsed["overall"]))))
    return parsed
