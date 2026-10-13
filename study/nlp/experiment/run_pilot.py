#!/usr/bin/env python3
"""Main pilot loop for translator-evaluator skill co-evolution."""
from __future__ import annotations

import json
import random
from pathlib import Path

import yaml

from src.client import LLMClient
from src.evaluate import evaluate
from src.metrics import accuracy_same_bucket, quadratic_weighted_kappa, spearman
from src.patch_generator import propose_evaluator_patch, propose_translator_patch
from src.replay import select_best_versions
from src.skill_manager import SkillManager
from src.translate import translate


def load_config(path: str | None = None) -> dict:
    if path is None:
        path = Path(__file__).resolve().parent / "config.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_data(cfg: dict) -> tuple[list[dict], list[dict], list[dict]]:
    data_dir = Path(cfg["paths"]["data"])
    train_path = data_dir / "train.jsonl"
    dev_path = data_dir / "dev.jsonl"
    test_path = data_dir / "test.jsonl"

    def _read(path: Path) -> list[dict]:
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    return _read(train_path), _read(dev_path), _read(test_path)


def run_iteration(
    t: int,
    trans_skill,
    eval_skill,
    trans_history: list,
    eval_history: list,
    train: list[dict],
    dev: list[dict],
    client: LLMClient,
    cfg: dict,
    sm: SkillManager,
) -> tuple:
    """Run one co-evolution iteration and return new skills plus metrics."""
    buckets = cfg["experiment"]["buckets"]
    n_cases = cfg["experiment"]["cases_for_patch"]
    success_ratio = cfg["experiment"]["success_ratio"]

    print(f"\n=== Iteration {t} ===")

    # 1. translate train
    print("[1/5] Translating train set...")
    train_records = []
    for r in train:
        pred = translate(r["source"], r.get("domain", ""), r.get("type", ""), trans_skill, client)
        ev = evaluate(r["source"], pred["translation"], r["reference"], eval_skill, client)
        rec = {
            "source": r["source"],
            "reference": r["reference"],
            "translation": pred["translation"],
            "reflection": pred["reflection"],
            "eval": ev,
            "eval_overall": ev["overall"],
            "gold_score": r["score"],
            "domain": r.get("domain", ""),
            "type": r.get("type", ""),
            "aligned": accuracy_same_bucket([ev["overall"]], [r["score"]], buckets) == 1.0,
        }
        train_records.append(rec)

    # 2. compute train metrics
    eval_scores = [r["eval_overall"] for r in train_records]
    gold_scores = [r["gold_score"] for r in train_records]
    train_kappa = quadratic_weighted_kappa(eval_scores, gold_scores)
    train_acc = accuracy_same_bucket(eval_scores, gold_scores, buckets)
    train_spear = spearman(eval_scores, gold_scores)
    print(f"  Train evaluator kappa={train_kappa:.3f} acc={train_acc:.3f} spearman={train_spear:.3f}")

    # 3. generate patches
    print("[2/5] Generating translator skill patches...")
    trans_patch = propose_translator_patch(trans_skill, train_records, n_cases, success_ratio, client)
    print("[3/5] Generating evaluator skill patches...")
    eval_patch = propose_evaluator_patch(eval_skill, train_records, n_cases, success_ratio, client)

    # 4. candidate versions
    print("[4/5] Building candidate skill versions...")
    trans_candidate = sm.apply_patch(trans_skill, trans_patch, f"v{t}-candidate")
    eval_candidate = sm.apply_patch(eval_skill, eval_patch, f"v{t}-candidate")

    # 5. cross-time replay
    print("[5/5] Cross-time replay on dev probe set...")
    window = cfg["experiment"].get("replay_window")
    new_trans, new_eval, replay_meta = select_best_versions(
        trans_history + [trans_candidate],
        eval_history + [eval_candidate],
        dev,
        client,
        buckets,
        window=window,
    )
    new_trans.version = f"v{t}"
    new_eval.version = f"v{t}"
    print(
        f"  Selected trans={new_trans.version} eval={new_eval.version} "
        f"product={replay_meta['product']:.3f} "
        f"easy={replay_meta['easy_correct']}/{replay_meta['easy_total']} "
        f"hard={replay_meta['hard_correct']}/{replay_meta['hard_total']}"
    )

    return new_trans, new_eval, train_records, replay_meta


def evaluate_on_set(records: list[dict], trans_skill, eval_skill, client: LLMClient, cfg: dict, name: str) -> dict:
    buckets = cfg["experiment"]["buckets"]
    preds = []
    evals = []
    golds = []
    print(f"\nEvaluating on {name}...")
    for r in records:
        pred = translate(r["source"], r.get("domain", ""), r.get("type", ""), trans_skill, client)
        ev = evaluate(r["source"], pred["translation"], r["reference"], eval_skill, client)
        preds.append(pred)
        evals.append(ev["overall"])
        golds.append(r["score"])

    return {
        "set": name,
        "n": len(records),
        "evaluator_kappa": quadratic_weighted_kappa(evals, golds),
        "evaluator_accuracy": accuracy_same_bucket(evals, golds, buckets),
        "evaluator_spearman": spearman(evals, golds),
        "avg_eval_score": sum(evals) / len(evals) if evals else 0.0,
        "avg_gold_score": sum(golds) / len(golds) if golds else 0.0,
    }


if __name__ == "__main__":
    cfg = load_config()
    random.seed(cfg["experiment"].get("seed", 42))

    out_dir = Path(cfg["paths"]["outputs"])
    out_dir.mkdir(parents=True, exist_ok=True)

    client = LLMClient(cfg)
    sm = SkillManager(cfg["paths"]["skills"])

    trans_skill = sm.load("translator_skill_v0")
    eval_skill = sm.load("evaluator_skill_v0")

    train, dev, test = load_data(cfg)
    print(f"Loaded train={len(train)} dev={len(dev)} test={len(test)}")

    trans_history = [trans_skill]
    eval_history = [eval_skill]

    results = []
    for t in range(1, cfg["experiment"]["iterations"] + 1):
        new_trans, new_eval, train_records, replay_meta = run_iteration(
            t, trans_skill, eval_skill, trans_history, eval_history, train, dev, client, cfg, sm
        )
        trans_skill, eval_skill = new_trans, new_eval
        trans_history.append(trans_skill)
        eval_history.append(eval_skill)

        # save versions
        sm.save(trans_skill, trans_skill.version)
        sm.save(eval_skill, eval_skill.version)

        # evaluate on test
        test_metrics = evaluate_on_set(test, trans_skill, eval_skill, client, cfg, f"test-v{t}")
        print(
            f"  Test kappa={test_metrics['evaluator_kappa']:.3f} "
            f"acc={test_metrics['evaluator_accuracy']:.3f} "
            f"avg_gold={test_metrics['avg_gold_score']:.2f} avg_eval={test_metrics['avg_eval_score']:.2f}"
        )

        results.append({"iteration": t, "replay": replay_meta, "test": test_metrics})

    # final summary
    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSummary saved to {summary_path}")
