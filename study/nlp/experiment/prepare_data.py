#!/usr/bin/env python3
"""Download CULTURE-MT and split into train/dev/test stratified by score/domain/type."""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

import yaml


def stratified_split(records: list[dict], ratios: list[float], seed: int) -> tuple[list[dict], list[dict], list[dict]]:
    random.seed(seed)
    # group by (domain, type, score_bucket)
    groups = defaultdict(list)
    for r in records:
        score = r.get("score", 3)
        bucket = int(score)  # 1-5
        key = (r.get("domain", "unknown"), r.get("type", "unknown"), bucket)
        groups[key].append(r)

    train, dev, test = [], [], []
    for key, items in groups.items():
        random.shuffle(items)
        n = len(items)
        n_train = int(n * ratios[0])
        n_dev = int(n * ratios[1])
        train.extend(items[:n_train])
        dev.extend(items[n_train : n_train + n_dev])
        test.extend(items[n_train + n_dev :])

    random.shuffle(train)
    random.shuffle(dev)
    random.shuffle(test)
    return train, dev, test


def normalize_record(raw: dict) -> dict:
    """Normalize a CULTURE-MT row to the schema expected by run_pilot."""
    return {
        "source": raw.get("source", raw.get("chinese", "")),
        "reference": raw.get("translation", raw.get("english", "")),
        "score": int(raw.get("score", 3)),
        "domain": raw.get("domain", "unknown"),
        "type": raw.get("type", "unknown"),
    }


def main() -> None:
    cfg_path = Path(__file__).resolve().parent / "config.yaml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))

    data_cfg = cfg["data"]
    total = data_cfg["total_samples"]
    ratios = [data_cfg["train_ratio"], data_cfg["dev_ratio"], data_cfg["test_ratio"]]
    seed = data_cfg["seed"]

    out_dir = Path(cfg["paths"]["data"])
    out_dir.mkdir(parents=True, exist_ok=True)

    local_path = data_cfg.get("local_path")
    if local_path and Path(local_path).exists():
        print(f"Loading from local path: {local_path}")
        with open(local_path, "r", encoding="utf-8") as f:
            records = [json.loads(line) for line in f if line.strip()]
    else:
        print(f"Downloading CULTURE-MT from HuggingFace ({data_cfg['hf_dataset']})...")
        try:
            from datasets import load_dataset
        except ImportError as exc:
            raise ImportError("pip install datasets") from exc
        ds = load_dataset(data_cfg["hf_dataset"], split="train")
        records = [normalize_record(dict(row)) for row in ds]

    # filter valid records
    records = [r for r in records if r["source"] and r["reference"] and 1 <= r["score"] <= 5]
    if len(records) > total:
        random.seed(seed)
        records = random.sample(records, total)

    train, dev, test = stratified_split(records, ratios, seed)

    def _write(recs: list[dict], path: Path) -> None:
        path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in recs),
            encoding="utf-8",
        )

    _write(train, out_dir / "train.jsonl")
    _write(dev, out_dir / "dev.jsonl")
    _write(test, out_dir / "test.jsonl")

    print(f"Wrote {len(train)} train, {len(dev)} dev, {len(test)} test records to {out_dir}")


if __name__ == "__main__":
    main()
