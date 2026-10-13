"""Generate skill patches from recent success/failure cases."""
from __future__ import annotations

import random
from pathlib import Path

from src.client import LLMClient
from src.skill_manager import Skill


def _load_prompt(name: str) -> str:
    path = Path(__file__).resolve().parents[1] / "prompts" / f"{name}.txt"
    return path.read_text(encoding="utf-8")


def _sample_cases(records: list[dict], n: int, success_ratio: float) -> tuple[list[dict], list[dict]]:
    """Sample success and failure cases evenly across error modes."""
    successes = [r for r in records if r["aligned"] and r["gold_score"] >= 4]
    failures = [r for r in records if not r["aligned"] or r["gold_score"] <= 3]

    n_success = int(n * success_ratio)
    n_failure = n - n_success

    sampled_success = random.sample(successes, min(len(successes), n_success))
    sampled_failure = random.sample(failures, min(len(failures), n_failure))

    # if one side is short, compensate from the other
    if len(sampled_success) < n_success and failures:
        sampled_failure += random.sample(failures, min(len(failures), n_success - len(sampled_success)))
    if len(sampled_failure) < n_failure and successes:
        sampled_success += random.sample(successes, min(len(successes), n_failure - len(sampled_failure)))

    return sampled_success, sampled_failure


def _format_translator_case(r: dict, label: str) -> str:
    lines = [
        f"### {label} case",
        f"Source: {r['source']}",
        f"Reference: {r['reference']}",
        f"Candidate: {r['translation']}",
        f"Evaluator overall: {r['eval_overall']}",
        f"Gold score: {r['gold_score']}",
        f"Evaluator diagnosis: {r['eval'].get('diagnosis', '')}",
        f"Evaluator suggestions: {r['eval'].get('suggestions', '')}",
    ]
    return "\n".join(lines)


def _format_evaluator_case(r: dict, label: str) -> str:
    lines = [
        f"### {label} case",
        f"Source: {r['source']}",
        f"Candidate: {r['translation']}",
        f"Evaluator overall: {r['eval_overall']}",
        f"Gold score: {r['gold_score']}",
        f"Evaluator dimensions: {r['eval'].get('dimensions', {})}",
        f"Evaluator diagnosis: {r['eval'].get('diagnosis', '')}",
    ]
    return "\n".join(lines)


def propose_translator_patch(skill: Skill, records: list[dict], n_cases: int, success_ratio: float, client: LLMClient) -> str:
    successes, failures = _sample_cases(records, n_cases, success_ratio)
    cases_text = "\n\n".join(
        [_format_translator_case(r, "Success") for r in successes]
        + [_format_translator_case(r, "Failure") for r in failures]
    )
    system = _load_prompt("gen_translator_patch").format(skill_body=skill.render())
    user = f"## Cases\n\n{cases_text}\n\nNow propose the patch."
    return client.quick_chat(system, user, temperature=client.model_cfg["temperature_generate"])


def propose_evaluator_patch(skill: Skill, records: list[dict], n_cases: int, success_ratio: float, client: LLMClient) -> str:
    # evaluator cares most about misaligned cases
    misaligned = [r for r in records if not r["aligned"]]
    aligned = [r for r in records if r["aligned"]]

    sampled_mis = random.sample(misaligned, min(len(misaligned), int(n_cases * 0.7)))
    sampled_ok = random.sample(aligned, min(len(aligned), n_cases - len(sampled_mis)))
    cases_text = "\n\n".join(
        [_format_evaluator_case(r, "Misaligned") for r in sampled_mis]
        + [_format_evaluator_case(r, "Aligned") for r in sampled_ok]
    )
    system = _load_prompt("gen_evaluator_patch").format(skill_body=skill.render())
    user = f"## Cases\n\n{cases_text}\n\nNow propose the patch."
    return client.quick_chat(system, user, temperature=client.model_cfg["temperature_generate"])
