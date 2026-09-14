"""Re-backtest the cost-sensitive decision rule (preset_infer_handler._COST_MATRIX)
against the POST-Phase-0 digest distributions.

Loads every per-article JSON saved in this directory (produced by
`test_grok_planner.py --save-json`, which reflects the NEW Phase-0 digests), and:

  1. Refits the empirical class-conditional cost matrix
     Cost[c][a] = E[R_w(true=c) - R_w(action=a)] from the TRAIN split
     (excluding forbidden-policy articles, same methodology as the original
     2026-07-10 backtest documented in run13_rl_grok_pipeline_analysis.md §9/§13).
  2. Backtests three RL-only (pre-Grok) decision policies against the RAW
     `rl_agg_probs` saved in each JSON, on both splits:
       - plain argmax (no cost rule)
       - the CURRENTLY SHIPPED cost matrix (constrained, max_step=1)
       - the REFIT cost matrix (constrained, max_step=1)
  3. Prints a comparison table (exact/near/miss/MAE/regret) so a ship/no-ship
     decision can be made without touching production code first.

Read-only: does not modify preset_infer_handler.py. If the refit matrix wins
per the doc's own bar (>=+2 test exacts, 0 new misses), apply it by hand.
"""
from __future__ import annotations

import json
import statistics
from pathlib import Path

NUM_PRESETS = 4
PRESET_NAMES = ["skip", "light", "standard", "deep"]

# The matrix currently shipped in preset_infer_handler.py (copied verbatim for
# side-by-side comparison; keep in sync if that file changes).
# Refit 2026-08-25 against N=3-replication-corrected oracle data -- see
# preset_infer_handler.py::_COST_MATRIX and run13_rl_grok_pipeline_analysis.md A.25.
SHIPPED_COST_MATRIX: list[list[float]] = [
    [0.0000, 0.0356, 0.1384, 0.0179],
    [0.1096, 0.0000, 0.0616, 0.0499],
    [0.0810, 0.0233, 0.0000, 0.0539],
    [0.1067, 0.0369, 0.0436, 0.0000],
]
MAX_STEP = 1


def load_articles(directory: Path) -> list[dict]:
    articles = []
    for path in sorted(directory.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("rl_agg_probs") is None or data.get("oracle_preset") is None:
            continue
        articles.append(data)
    return articles


def refit_cost_matrix(train_articles: list[dict]) -> tuple[list[list[float]], dict]:
    """Cost[c][a] = mean over train articles with oracle==c of (r_w[c] - r_w[a])."""
    buckets: dict[int, list[list[float]]] = {c: [] for c in range(NUM_PRESETS)}
    for art in train_articles:
        if art.get("policy") == "forbidden":
            continue
        c = art["oracle_preset"]
        r_w = art["r_w_rewards"]
        if len(r_w) != NUM_PRESETS:
            continue
        buckets[c].append(r_w)

    matrix = [[0.0] * NUM_PRESETS for _ in range(NUM_PRESETS)]
    counts = {}
    for c in range(NUM_PRESETS):
        rows = buckets[c]
        counts[c] = len(rows)
        if not rows:
            continue
        for a in range(NUM_PRESETS):
            diffs = [r_w[c] - r_w[a] for r_w in rows]
            matrix[c][a] = round(statistics.mean(diffs), 4)
    return matrix, counts


def apply_cost_rule(
    raw_preset: int, probs: list[float], matrix: list[list[float]], max_step: int = MAX_STEP
) -> int:
    lo = max(0, raw_preset - max_step)
    hi = min(NUM_PRESETS - 1, raw_preset + max_step)
    candidates = range(lo, hi + 1)
    exp_costs = {
        a: sum(probs[c] * matrix[c][a] for c in range(NUM_PRESETS))
        for a in candidates
    }
    return min(candidates, key=lambda a: exp_costs[a])


def evaluate(
    articles: list[dict], matrix: list[list[float]] | None
) -> dict:
    exact = near = miss = 0
    abs_errs: list[int] = []
    regrets: list[float] = []
    per_article = []
    for art in articles:
        probs = art["rl_agg_probs"]
        r_w = art["r_w_rewards"]
        oracle = art["oracle_preset"]
        raw_argmax = max(range(NUM_PRESETS), key=lambda i: probs[i])
        if matrix is None:
            chosen = raw_argmax
        else:
            chosen = apply_cost_rule(raw_argmax, probs, matrix)

        diff = abs(chosen - oracle)
        abs_errs.append(diff)
        if diff == 0:
            exact += 1
            verdict = "EXACT"
        elif diff == 1:
            near += 1
            verdict = "NEAR"
        else:
            miss += 1
            verdict = "MISS"

        if art.get("policy") != "forbidden" and len(r_w) > max(oracle, chosen):
            regret = round(r_w[oracle] - r_w[chosen], 4)
            regrets.append(regret)
        else:
            regret = None

        per_article.append(
            {
                "variant": art["variant"],
                "raw_argmax": raw_argmax,
                "chosen": chosen,
                "oracle": oracle,
                "verdict": verdict,
                "regret": regret,
            }
        )

    n = len(articles)
    return {
        "n": n,
        "exact": exact,
        "near": near,
        "miss": miss,
        "mae": round(statistics.mean(abs_errs), 4) if abs_errs else None,
        "regret_mean": round(statistics.mean(regrets), 4) if regrets else None,
        "regret_max": round(max(regrets), 4) if regrets else None,
        "per_article": per_article,
    }


def print_summary(label: str, res: dict) -> None:
    n, exact, near, miss = res["n"], res["exact"], res["near"], res["miss"]
    print(
        f"{label:38s} n={n:2d}  exact={exact:2d} ({exact/n:.0%})  "
        f"near={near:2d}  miss={miss:2d}  MAE={res['mae']}  "
        f"regret_mean={res['regret_mean']}  regret_max={res['regret_max']}"
    )


def print_diff(label: str, base: dict, other: dict) -> None:
    base_map = {a["variant"]: a for a in base["per_article"]}
    for art in other["per_article"]:
        b = base_map.get(art["variant"])
        if b and b["chosen"] != art["chosen"]:
            print(
                f"    [{label}] {art['variant']:45s} "
                f"{PRESET_NAMES[b['chosen']]:8s}({b['verdict']}) -> "
                f"{PRESET_NAMES[art['chosen']]:8s}({art['verdict']})  "
                f"oracle={PRESET_NAMES[art['oracle']]}"
            )


def main() -> None:
    here = Path(__file__).parent
    all_articles = load_articles(here)
    train = [a for a in all_articles if a.get("split") == "TRAIN"]
    test = [a for a in all_articles if a.get("split") == "TEST"]
    print(f"Loaded {len(all_articles)} articles ({len(train)} TRAIN, {len(test)} TEST)\n")

    refit_matrix, counts = refit_cost_matrix(train)
    print(f"Refit sample sizes per oracle class (non-forbidden TRAIN): {counts}\n")

    print("--- Refit cost matrix (rows=true oracle, cols=action) ---")
    header = "        " + "".join(f"{n:>10s}" for n in PRESET_NAMES)
    print(header)
    for c in range(NUM_PRESETS):
        print(f"{PRESET_NAMES[c]:8s}" + "".join(f"{refit_matrix[c][a]:10.4f}" for a in range(NUM_PRESETS)))
    print()

    print("--- Shipped cost matrix (for reference) ---")
    print(header)
    for c in range(NUM_PRESETS):
        print(f"{PRESET_NAMES[c]:8s}" + "".join(f"{SHIPPED_COST_MATRIX[c][a]:10.4f}" for a in range(NUM_PRESETS)))
    print()

    for split_name, articles in (("TEST", test), ("TRAIN", train)):
        print(f"=== {split_name} (n={len(articles)}) ===")
        base = evaluate(articles, matrix=None)
        shipped = evaluate(articles, matrix=SHIPPED_COST_MATRIX)
        refit = evaluate(articles, matrix=refit_matrix)
        print_summary("  argmax (no rule)", base)
        print_summary("  shipped cost matrix", shipped)
        print_summary("  refit cost matrix (new digests)", refit)
        print()
        print("  Differences: argmax -> shipped:")
        print_diff("shipped", base, shipped)
        print("  Differences: shipped -> refit:")
        print_diff("refit", shipped, refit)
        print()


if __name__ == "__main__":
    main()
