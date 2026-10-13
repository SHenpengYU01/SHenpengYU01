"""Translator: generate candidate translations given a source post and skill."""
from __future__ import annotations

from pathlib import Path

from src.client import LLMClient
from src.skill_manager import Skill


def _load_prompt(name: str) -> str:
    path = Path(__file__).resolve().parents[1] / "prompts" / f"{name}.txt"
    return path.read_text(encoding="utf-8")


def translate(source: str, domain: str, post_type: str, skill: Skill, client: LLMClient) -> dict:
    system = _load_prompt("translate").format(skill_body=skill.render())
    user = f"Source: {source}\nDomain: {domain}\nType: {post_type}\n\nPlease provide the translation and a short reflection."
    raw = client.quick_chat(system, user, temperature=client.model_cfg["temperature_translate"])

    # Simple parsing: first non-empty line as translation, rest as reflection
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    translation = lines[0] if lines else raw.strip()
    reflection = "\n".join(lines[1:]) if len(lines) > 1 else ""
    return {"translation": translation, "reflection": reflection, "raw": raw}
