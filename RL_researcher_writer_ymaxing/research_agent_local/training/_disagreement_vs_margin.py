"""Does cross-draw label disagreement concentrate where it doesn't matter?

_replication_retrain_analysis.py found only 45.0% agreement between two
independent replicate draws on which arm is best. That number is alarming ONLY
if the disagreement lands on sections where the arm choice actually carries
reward consequences. This buckets sections by their N=3-averaged margin and
reports (a) draw-agreement rate and (b) the mean REGRET of picking the
minority arm instead of the majority arm, per bucket.

Read-only, zero LLM calls, zero writes.
Usage (from research_agent_local/):  python3 training/_disagreement_vs_margin.py
"""
from __future__ import annotations

import statistics
import sys
from collections import Counter
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import _replication_retrain_analysis as rra  # noqa: E402

ARMS = rra.ARMS
_BUCKETS = [(0.00, 0.02), (0.02, 0.04), (0.04, 0.08), (0.08, 0.15), (0.15, 9.99)]


def main():
    corpus = rra.load_train_draws()
    fn = rra.CANDIDATES["C2_shipped"]

    rows = []
    for _key, per_arm in corpus:
        avg = {a: statistics.mean(fn(per_arm[a][d], rra._nr(a, fn)) for d in range(3)) for a in ARMS}
        ranked = sorted(ARMS, key=lambda a: avg[a], reverse=True)
        margin = avg[ranked[0]] - avg[ranked[1]]

        winners = []
        for d in range(3):
            r = {a: fn(per_arm[a][d], rra._nr(a, fn)) for a in ARMS}
            winners.append(max(ARMS, key=r.__getitem__))
        counts = Counter(winners)
        top_n = counts.most_common(1)[0][1]
        rep_agree = winners[1] == winners[2]      # unbiased pair (both un-corrected)

        # regret of the WORST arm any draw nominated, measured on the averaged reward
        worst_nominated = min(avg[w] for w in set(winners))
        regret = avg[ranked[0]] - worst_nominated

        rows.append({"margin": margin, "rep_agree": rep_agree, "top_n": top_n, "regret": regret})

    print("=" * 100)
    print("Cross-draw disagreement vs. how much the decision actually matters (TRAIN, shipped C2)")
    print("=" * 100)
    hdr = (f"  {'averaged margin':<18} {'n':>4} {'rep1=rep2':>10} {'unanimous':>10} "
           f"{'3-way split':>12} {'mean regret of':>16}")
    print(hdr)
    print(f"  {'':<18} {'':>4} {'':>10} {'(3/3)':>10} {'(1/1/1)':>12} {'worst nominee':>16}")
    print("  " + "-" * (len(hdr) - 2))
    for lo, hi in _BUCKETS:
        sel = [r for r in rows if lo <= r["margin"] < hi]
        if not sel:
            continue
        n = len(sel)
        label = f"{lo:.2f} - {hi:.2f}" if hi < 9 else f">= {lo:.2f}"
        print(f"  {label:<18} {n:>4} {sum(r['rep_agree'] for r in sel)/n:>9.1%} "
              f"{sum(1 for r in sel if r['top_n']==3)/n:>9.1%} "
              f"{sum(1 for r in sel if r['top_n']==1)/n:>11.1%} "
              f"{statistics.mean(r['regret'] for r in sel):>16.4f}")

    n = len(rows)
    print("  " + "-" * (len(hdr) - 2))
    print(f"  {'ALL':<18} {n:>4} {sum(r['rep_agree'] for r in rows)/n:>9.1%} "
          f"{sum(1 for r in rows if r['top_n']==3)/n:>9.1%} "
          f"{sum(1 for r in rows if r['top_n']==1)/n:>11.1%} "
          f"{statistics.mean(r['regret'] for r in rows):>16.4f}")

    below = [r for r in rows if r["margin"] < 0.04]
    above = [r for r in rows if r["margin"] >= 0.04]
    print(f"\n  Sections BELOW sigma_floor margin (0.04), i.e. GRPO drops or clamps them: "
          f"{len(below)}/{n} = {len(below)/n:.1%}")
    print(f"    ...their draw-agreement: {sum(r['rep_agree'] for r in below)/len(below):.1%}   "
          f"mean regret: {statistics.mean(r['regret'] for r in below):.4f}")
    print(f"  Sections ABOVE it (the ones that actually drive the gradient): {len(above)}/{n} = {len(above)/n:.1%}")
    print(f"    ...their draw-agreement: {sum(r['rep_agree'] for r in above)/len(above):.1%}   "
          f"mean regret: {statistics.mean(r['regret'] for r in above):.4f}")


if __name__ == "__main__":
    main()
