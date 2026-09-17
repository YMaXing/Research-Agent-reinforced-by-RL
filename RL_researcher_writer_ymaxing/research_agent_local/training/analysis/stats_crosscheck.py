"""Wilcoxon signed-rank + sign-flip permutation cross-checks, and a paired
bootstrap CI, for RL+guards (run33/ep81) vs. the guarded-`light` constant
baseline on TEST (n=16, regret n=15 excluding the one forbidden-policy
article). Reuses guarded_constant_baseline.py's data loaders directly (no
reward-formula/guard-logic duplication).

All three tests operate on the SAME paired per-article quantities:
  - dist_reduction  = baseline_ordinal_dist - model_ordinal_dist   (n=16)
  - regret_reduction = baseline_regret - model_regret              (n=15, forbidden excluded)

Usage (from research_agent_local/training/):
    python stats_crosscheck.py
"""

from __future__ import annotations

import random
import statistics
from itertools import product

import guarded_constant_baseline as gcb

ARMS = gcb.ARMS
LIGHT_IDX = ARMS.index("light")


def paired_data() -> tuple[list[float], list[float]]:
    """Returns (dist_reductions[n=16], regret_reductions[n=15])."""
    baseline = gcb.score_constant_baseline(gcb.TEST_ARTICLES, LIGHT_IDX)["per_article"]
    dist_reductions = []
    regret_reductions = []
    for article in gcb.TEST_ARTICLES:
        b = baseline[article]
        model_idx = gcb._RL_GUARDS_CHOSEN_TEST[article]
        oracle_idx = b["oracle_idx"]
        accepted = {oracle_idx, *b["tied_idx"]}
        model_dist = 0 if model_idx in accepted else min(abs(model_idx - a) for a in accepted)
        dist_reductions.append(b["dist"] - model_dist)
        if b["policy"] != "forbidden":
            _, r_w, _ = gcb._read_oracle(article)
            model_regret = r_w[oracle_idx] - r_w[model_idx]
            regret_reductions.append(b["regret"] - model_regret)
    return dist_reductions, regret_reductions


def wilcoxon_signed_rank_exact(diffs: list[float]) -> dict:
    """Exact one-sided Wilcoxon signed-rank test (H1: median diff > 0).
    Drops exact zeros per convention; enumerates all 2^m sign assignments
    over the m ranks (m small enough here, <=16, for brute enumeration)."""
    nonzero = [d for d in diffs if d != 0]
    m = len(nonzero)
    ranked = sorted(range(m), key=lambda i: abs(nonzero[i]))
    ranks = [0.0] * m
    # average-rank ties
    i = 0
    while i < m:
        j = i
        while j + 1 < m and abs(nonzero[ranked[j + 1]]) == abs(nonzero[ranked[i]]):
            j += 1
        avg_rank = sum(range(i + 1, j + 2)) / (j - i + 1)
        for k in range(i, j + 1):
            ranks[ranked[k]] = avg_rank
        i = j + 1
    signs = [1 if d > 0 else -1 for d in nonzero]
    w_plus = sum(r for r, s in zip(ranks, signs) if s > 0)
    # exact null: enumerate all 2^m sign flips of `ranks`
    count_ge = 0
    total = 2 ** m
    for bits in product([1, -1], repeat=m):
        s = sum(r for r, b in zip(ranks, bits) if b > 0)
        if s >= w_plus - 1e-9:
            count_ge += 1
    p_one_sided = count_ge / total
    return {"n": m, "w_plus": w_plus, "p_one_sided": p_one_sided}


def sign_flip_permutation_exact(diffs: list[float]) -> dict:
    """Exact one-sided sign-flip permutation test on the RAW differences
    (not ranked) -- tests H1: mean diff > 0."""
    nonzero = [d for d in diffs if d != 0]
    m = len(nonzero)
    observed = sum(nonzero)
    count_ge = 0
    total = 2 ** m
    for bits in product([1, -1], repeat=m):
        s = sum(d * b for d, b in zip(nonzero, bits))
        if s >= observed - 1e-9:
            count_ge += 1
    p_one_sided = count_ge / total
    return {"n": m, "observed_sum": observed, "p_one_sided": p_one_sided}


def paired_bootstrap(diffs: list[float], b_draws: int = 100_000, seed: int = 20260828) -> dict:
    rng = random.Random(seed)
    n = len(diffs)
    means = []
    for _ in range(b_draws):
        sample = [diffs[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    lo = means[int(0.025 * b_draws)]
    hi = means[int(0.975 * b_draws)]
    p_le_zero = sum(1 for m in means if m <= 0) / b_draws
    return {
        "n": n, "observed_mean": statistics.mean(diffs),
        "boot_mean": statistics.mean(means),
        "ci95": (lo, hi), "p_one_sided_le_zero": p_le_zero,
    }


def main() -> None:
    dist_reductions, regret_reductions = paired_data()
    print(f"dist_reductions  (n={len(dist_reductions)}): {dist_reductions}")
    print(f"regret_reductions (n={len(regret_reductions)}): {[round(r, 4) for r in regret_reductions]}")

    print("\n=== Wilcoxon signed-rank (exact, one-sided H1: reduction > 0) ===")
    for name, diffs in (("MAE/dist reduction", dist_reductions), ("regret reduction", regret_reductions)):
        r = wilcoxon_signed_rank_exact(diffs)
        print(f"  {name:20s} n={r['n']:2d}  W+={r['w_plus']:.1f}  p={r['p_one_sided']:.4f}")

    print("\n=== Sign-flip permutation test (exact, one-sided H1: mean reduction > 0) ===")
    for name, diffs in (("MAE/dist reduction", dist_reductions), ("regret reduction", regret_reductions)):
        r = sign_flip_permutation_exact(diffs)
        print(f"  {name:20s} n={r['n']:2d}  sum={r['observed_sum']:.4f}  p={r['p_one_sided']:.4f}")

    print("\n=== Paired bootstrap (B=100,000, one-sided H1: mean reduction > 0) ===")
    for name, diffs in (("MAE/dist reduction", dist_reductions), ("regret reduction", regret_reductions)):
        r = paired_bootstrap(diffs)
        print(
            f"  {name:20s} n={r['n']:2d}  mean={r['observed_mean']:.4f}  "
            f"95% CI=[{r['ci95'][0]:.4f}, {r['ci95'][1]:.4f}]  p(<=0)={r['p_one_sided_le_zero']:.4f}"
        )


if __name__ == "__main__":
    main()
