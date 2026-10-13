"""Cross-time replay: select best (translator, evaluator) skill versions."""
from __future__ import annotations

from itertools import product

from src.client import LLMClient
from src.evaluate import evaluate
from src.metrics import solve_rate_laplacian
from src.skill_manager import Skill
from src.translate import translate


def _is_solved(pred_score: float, gold_score: float, buckets: list[float]) -> bool:
    def bucket(v: float) -> int:
        for i, b in enumerate(buckets):
            if v <= b:
                return i
        return len(buckets)
    return bucket(pred_score) == bucket(gold_score)


def score_version_pair(
    trans_skill: Skill,
    eval_skill: Skill,
    probe_records: list[dict],
    client: LLMClient,
    buckets: list[float],
) -> dict:
    """Return solve rates for easy/hard subsets and product score."""
    easy_records = [r for r in probe_records if r["gold_score"] >= 4]
    hard_records = [r for r in probe_records if r["gold_score"] <= 3]

    def eval_subset(subset: list[dict]) -> tuple[int, int]:
        correct = 0
        for r in subset:
            pred = translate(r["source"], r["domain"], r["type"], trans_skill, client)
            ev = evaluate(r["source"], pred["translation"], r["reference"], eval_skill, client)
            if _is_solved(ev["overall"], r["gold_score"], buckets):
                correct += 1
        return correct, len(subset)

    easy_correct, easy_total = eval_subset(easy_records)
    hard_correct, hard_total = eval_subset(hard_records)

    return {
        "easy_correct": easy_correct,
        "easy_total": easy_total,
        "hard_correct": hard_correct,
        "hard_total": hard_total,
        "solve_easy": solve_rate_laplacian(easy_correct, easy_total),
        "solve_hard": solve_rate_laplacian(hard_correct, hard_total),
        "product": solve_rate_laplacian(easy_correct, easy_total) * solve_rate_laplacian(hard_correct, hard_total),
    }


def select_best_versions(
    trans_candidates: list[Skill],
    eval_candidates: list[Skill],
    probe_records: list[dict],
    client: LLMClient,
    buckets: list[float],
    window: int | None = None,
) -> tuple[Skill, Skill, dict]:
    """Grid search over recent candidate pairs, pick max product solve rate."""
    if window:
        trans_candidates = trans_candidates[-window:]
        eval_candidates = eval_candidates[-window:]

    best_pair = (trans_candidates[-1], eval_candidates[-1])
    best_meta = {"product": -1.0}

    for ts, es in product(trans_candidates, eval_candidates):
        meta = score_version_pair(ts, es, probe_records, client, buckets)
        if meta["product"] > best_meta["product"]:
            best_meta = meta
            best_pair = (ts, es)

    return best_pair[0], best_pair[1], best_meta
