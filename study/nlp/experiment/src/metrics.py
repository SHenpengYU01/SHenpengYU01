"""Evaluation metrics for translator and evaluator."""
from __future__ import annotations

import math
from typing import Sequence


def pearson(x: Sequence[float], y: Sequence[float]) -> float:
    n = len(x)
    if n == 0:
        return 0.0
    mx, my = sum(x) / n, sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = math.sqrt(sum((xi - mx) ** 2 for xi in x) * sum((yi - my) ** 2 for yi in y))
    return num / den if den > 1e-9 else 0.0


def spearman(x: Sequence[float], y: Sequence[float]) -> float:
    def rank(a: Sequence[float]) -> list[float]:
        sorted_vals = sorted((v, i) for i, v in enumerate(a))
        ranks = [0.0] * len(a)
        i = 0
        while i < len(sorted_vals):
            j = i
            while j + 1 < len(sorted_vals) and sorted_vals[j + 1][0] == sorted_vals[i][0]:
                j += 1
            r = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[sorted_vals[k][1]] = r
            i = j + 1
        return ranks
    return pearson(rank(x), rank(y))


def quadratic_weighted_kappa(x: Sequence[float], y: Sequence[float], min_rating: int = 1, max_rating: int = 5) -> float:
    """QWK for integer ratings in [min_rating, max_rating]."""
    def hist(a: Sequence[float]) -> list[float]:
        h = [0.0] * (max_rating - min_rating + 1)
        for v in a:
            idx = int(round(v)) - min_rating
            idx = max(0, min(idx, max_rating - min_rating))
            h[idx] += 1.0
        return [c / len(a) for c in h]

    n = len(x)
    if n == 0:
        return 0.0
    o = [[0.0] * (max_rating - min_rating + 1) for _ in range(max_rating - min_rating + 1)]
    for xi, yi in zip(x, y):
        i = max(0, min(int(round(xi)) - min_rating, max_rating - min_rating))
        j = max(0, min(int(round(yi)) - min_rating, max_rating - min_rating))
        o[i][j] += 1.0 / n

    hx, hy = hist(x), hist(y)
    e = [[hx[i] * hy[j] for j in range(len(hy))] for i in range(len(hx))]

    num = sum((o[i][j] - e[i][j]) * (i - j) ** 2 for i in range(len(hx)) for j in range(len(hy)))
    den = sum(e[i][j] * (i - j) ** 2 for i in range(len(hx)) for j in range(len(hy)))
    return 1.0 - num / den if den > 1e-9 else 1.0


def accuracy_same_bucket(x: Sequence[float], y: Sequence[float], buckets: Sequence[float] | None = None) -> float:
    """Accuracy where ratings are binned by bucket thresholds."""
    if buckets is None:
        buckets = [2, 3, 4, 5]

    def bucket(v: float) -> int:
        for i, b in enumerate(buckets):
            if v <= b:
                return i
        return len(buckets)

    correct = sum(bucket(xi) == bucket(yi) for xi, yi in zip(x, y))
    return correct / len(x) if x else 0.0


def solve_rate_laplacian(pred_correct: int, total: int) -> float:
    return (pred_correct + 1) / (total + 2)
