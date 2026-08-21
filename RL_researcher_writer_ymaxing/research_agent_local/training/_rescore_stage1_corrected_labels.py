"""Re-score the historical Stage 1 TEST results under the CORRECTED TEST oracle
labels from A.15.4, to test whether the label corrections change the model ranking.

sec61's Stage 1 comparisons (run26/27/28/29 + the zero-retrain baseline) were all
scored against production TEST oracle labels. A.15.4's N=3 replication found 4 of
the 12 CRITICAL/HIGH TEST labels to be wrong. This script re-scores each run's
saved per-article predictions under the corrected labels and reports how the
headline metrics and the run ranking move.

Parses the saved `rl_only_train_and_test_results_*.md` TEST tables (the same
tables sec61 quoted), so no re-inference and no GPU are needed.

Read-only, zero LLM calls, zero writes.
Usage (from research_agent_local/):  python3 training/_rescore_stage1_corrected_labels.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
_RESULTS = _TRAINING.parent / "grok_planner_test_results"

PRESET_IDX = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
ARM_OF = {0: "skip", 1: "light", 2: "standard", 3: "deep"}

# A.15.4 (2026-08-20), post explore-split-fix: 4 corrections, 1 unresolved.
CORRECTIONS = {
    "Earth_Oceans_Origin":   ("standard", "deep"),
    "Gravity_Entropy":       ("standard", "light"),
    "13_agent_framework":    ("deep",     "light"),
    "Insects_Consciousness": ("light",    "deep"),
}
UNRESOLVED = {"07_reasoning_planning"}
ARM_TO_IDX = {v: k for k, v in ARM_OF.items()}

RUN_FILES = {
    "run26_costcoef_only @ep146": "rl_only_train_and_test_results_run26_epoch146.md",
    "run27_debecurve_only @ep110": "rl_only_train_and_test_result_run27_epoch110.md",
    "run28_garatreat_only":        "rl_only_train_and_test_results_run28_garatreat_only.md",
    "run29_costcoef05 @ep94":      "rl_only_train_and_test_results_run29_costcoef05.md",
}

_ROW = re.compile(
    r"^\s{2}(\S.*?)\s{2,}TEST\s+(P\d|—)\s+(\S+)\s+(P\d|—)\s*→\s*(P\d|—)\s+.*$"
)


def parse_test_rows(path: Path):
    """Return {article: (chosen_idx, oracle_idx)} from the TEST table."""
    rows = {}
    in_test = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if "TEST  (held-out" in line:
            in_test = True
            continue
        if in_test and line.strip().startswith("n=") and "exact=" in line:
            break
        if not in_test:
            continue
        m = _ROW.match(line.rstrip())
        if m:
            art, _rl, _grok, chosen, oracle = m.groups()
            if chosen in PRESET_IDX and oracle in PRESET_IDX:
                rows[art.strip()] = (PRESET_IDX[chosen], PRESET_IDX[oracle])
    return rows


def score(rows, corrected: bool, exclude_unresolved: bool = False):
    n = exact = near = miss = 0
    abs_err = 0
    changed = []
    for art, (chosen, oracle) in rows.items():
        if exclude_unresolved and art in UNRESOLVED:
            continue
        new_oracle = oracle
        if corrected and art in CORRECTIONS:
            new_oracle = ARM_TO_IDX[CORRECTIONS[art][1]]
        n += 1
        d = abs(chosen - new_oracle)
        abs_err += d
        if d == 0:
            exact += 1
        elif d == 1:
            near += 1
        else:
            miss += 1
        if corrected and art in CORRECTIONS:
            old_d = abs(chosen - oracle)
            verdict = lambda x: "EXACT" if x == 0 else ("NEAR" if x == 1 else "MISS")
            if verdict(old_d) != verdict(d):
                changed.append(f"{art}: {verdict(old_d)}->{verdict(d)}")
    return {"n": n, "exact": exact, "near": near, "miss": miss,
            "mae": abs_err / n if n else 0.0, "changed": changed}


def main():
    print("=" * 112)
    print("Stage 1 TEST results re-scored under A.15.4's CORRECTED TEST oracle labels")
    print("=" * 112)
    print("Corrections applied:")
    for a, (old, new) in CORRECTIONS.items():
        print(f"  {a:<28} {old:>9} -> {new}")
    print(f"Left unchanged (unresolved 3-way split): {', '.join(UNRESOLVED)}\n")

    hdr = (f"  {'run':<30} | {'ORIGINAL labels':^30} | {'CORRECTED labels':^30} | {'delta':>12}")
    print(hdr)
    print(f"  {'':<30} | {'exact':>6} {'near':>5} {'miss':>5} {'MAE':>6} | "
          f"{'exact':>6} {'near':>5} {'miss':>5} {'MAE':>6} | {'exact':>12}")
    print("  " + "-" * (len(hdr) - 2))

    all_changes = {}
    for label, fname in RUN_FILES.items():
        p = _RESULTS / fname
        if not p.exists():
            print(f"  {label:<30} | (file not found: {fname})")
            continue
        rows = parse_test_rows(p)
        if not rows:
            print(f"  {label:<30} | (no TEST rows parsed from {fname})")
            continue
        o = score(rows, corrected=False)
        c = score(rows, corrected=True)
        all_changes[label] = c["changed"]
        d_exact = c["exact"] - o["exact"]
        print(f"  {label:<30} | {o['exact']:>4}/{o['n']:<2} {o['near']:>5} {o['miss']:>5} {o['mae']:>6.3f} | "
              f"{c['exact']:>4}/{c['n']:<2} {c['near']:>5} {c['miss']:>5} {c['mae']:>6.3f} | {d_exact:>+12}")

    print("\n  Per-run verdict changes on the 4 corrected articles:")
    for label, changes in all_changes.items():
        print(f"    {label:<30} {'; '.join(changes) if changes else '(none)'}")

    print("\n" + "=" * 112)
    print("Same, EXCLUDING the unresolved article (07_reasoning_planning) — the honest n=15 view")
    print("=" * 112)
    print(f"  {'run':<30} | {'orig exact':>11} | {'corrected exact':>16} | {'corrected MAE':>14}")
    print("  " + "-" * 80)
    for label, fname in RUN_FILES.items():
        p = _RESULTS / fname
        if not p.exists():
            continue
        rows = parse_test_rows(p)
        if not rows:
            continue
        o = score(rows, corrected=False, exclude_unresolved=True)
        c = score(rows, corrected=True, exclude_unresolved=True)
        print(f"  {label:<30} | {o['exact']:>3}/{o['n']:<2} ({o['exact']/o['n']:>5.1%}) | "
              f"{c['exact']:>3}/{c['n']:<2} ({c['exact']/c['n']:>5.1%})    | {c['mae']:>14.3f}")

    # ---- sec60.12 discipline: everything must be scored RELATIVE to the trivial
    # constant predictor on the SAME label set, or a label change masquerades as a
    # model improvement.
    ref = parse_test_rows(_RESULTS / RUN_FILES["run26_costcoef_only @ep146"])
    for corrected in (False, True):
        oracles = []
        for art, (_ch, orc) in ref.items():
            if corrected and art in CORRECTIONS:
                orc = ARM_TO_IDX[CORRECTIONS[art][1]]
            oracles.append(orc)
        dist = [oracles.count(i) for i in range(4)]
        best = max(range(4), key=lambda i: dist[i])
        near = [sum(1 for o in oracles if abs(o - i) <= 1) for i in range(4)]
        tag = "CORRECTED" if corrected else "ORIGINAL "
        print(f"\n  TEST oracle dist ({tag}) sk/li/st/dp = {dist}   "
              f"best constant predictor = '{ARM_OF[best]}' -> {dist[best]}/{len(oracles)} "
              f"= {dist[best]/len(oracles):.1%} strict, {max(near)/len(oracles):.1%} near-tie")

    print("\n" + "=" * 112)
    print("BASELINE-RELATIVE view (sec60.12 discipline): articles gained over the trivial predictor")
    print("=" * 112)
    print(f"  {'run':<30} | {'ORIGINAL (base 6/16)':>22} | {'CORRECTED (base 7/16)':>23}")
    print("  " + "-" * 80)
    for label, fname in RUN_FILES.items():
        p = _RESULTS / fname
        if not p.exists():
            continue
        rows = parse_test_rows(p)
        if not rows:
            continue
        o, c = score(rows, corrected=False), score(rows, corrected=True)
        # recompute each label set's own trivial baseline from that run's oracle column
        def base(corr):
            orcs = [ARM_TO_IDX[CORRECTIONS[a][1]] if (corr and a in CORRECTIONS) else v
                    for a, (_ch, v) in rows.items()]
            return max(orcs.count(i) for i in range(4))
        bo, bc = base(False), base(True)
        print(f"  {label:<30} | {o['exact']:>3} vs {bo:<3} = {o['exact']-bo:>+3} articles | "
              f"{c['exact']:>3} vs {bc:<3} = {c['exact']-bc:>+3} articles")
    print("\n  ^ THIS is the metric that matters: a label correction that raises BOTH the model's")
    print("    score and the trivial baseline by the same amount is not a real model improvement.")


if __name__ == "__main__":
    main()
