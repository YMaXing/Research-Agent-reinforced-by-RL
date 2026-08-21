"""Decision-support for "does N=3 replication better prepare the next retrain?"

Applies train_grpo.py::load_section_groups()'s EXACT flat-filter / near-tie /
advantage logic to both label sets (single-draw section_oracle.json vs N=3
section_oracle_averaged.json) and reports the quantities that actually decide
whether a retrain can demonstrate learning:

  1. constant-predictor baselines (sec59/60.12's success criterion -- the bar
     any run must beat to have demonstrated ANY learning), strict + near-tie
  2. label-distribution balance (entropy / max-class share)
  3. how many groups survive the sigma_floor flat-filter (= actual trainable set)
  4. sigma_floor_fraction (the denominator-clamped share, logged every epoch)
  5. mean |advantage| (raw gradient magnitude the policy actually sees)

Read-only, zero LLM calls, zero writes, no torch import (re-implements the
arithmetic inline rather than importing train_grpo, which pulls in transformers).
Every formula below is copied line-for-line from load_section_groups().

Usage (from research_agent_local/):
  python3 training/_compare_label_sets_for_training.py
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import generate_episode_oracles as geo  # noqa: E402

_BASES = _TRAINING.parent.parent / "rl_training_data" / "bases"
PRESET_NAMES = ["skip", "light", "standard", "deep"]

_SIGMA_FLOOR = 0.04      # train_grpo.py default
_NEAR_TIE_MARGIN = 0.06  # train_grpo.py default

_TRAIN_ARTICLES = [f"{t}__{v}" for t in geo._ALL_ARTICLES for v in geo._VARIANTS]


def load_groups(oracle_filename: str):
    """Mirror of train_grpo.py::load_section_groups()'s per-section logic."""
    kept, dropped = [], 0
    for article in _TRAIN_ARTICLES:
        p = _BASES / article / oracle_filename
        if not p.exists():
            continue
        sections = json.loads(p.read_text(encoding="utf-8")).get("sections", {})
        for sec_id, info in sorted(sections.items()):
            rewards = [float(info["rewards"].get(PRESET_NAMES[i], 0.0)) for i in range(4)]
            max_r = max(rewards)
            if max_r - min(rewards) < _SIGMA_FLOOR:   # flat-group filter
                dropped += 1
                continue
            mean_r = sum(rewards) / 4
            raw_std = (sum((r - mean_r) ** 2 for r in rewards) / 4) ** 0.5
            std_r = max(raw_std, _SIGMA_FLOOR)
            kept.append({
                "name": f"{article}__{sec_id}",
                "rewards": rewards,
                "best_idx": rewards.index(max_r),
                "acceptable_idxs": [i for i, r in enumerate(rewards) if r >= max_r - _NEAR_TIE_MARGIN],
                "hit_sigma_floor": raw_std < _SIGMA_FLOOR,
                "raw_std": raw_std,
                "margin": max_r - sorted(rewards, reverse=True)[1],
                "advantages": [(r - mean_r) / std_r for r in rewards],
            })
    return kept, dropped


def analyze(label, groups, dropped):
    n = len(groups)
    dist = {p: 0 for p in PRESET_NAMES}
    for g in groups:
        dist[PRESET_NAMES[g["best_idx"]]] += 1

    # constant-predictor baselines: best single arm played always (sec60.12's criterion)
    strict_by_arm = {p: dist[p] / n for p in PRESET_NAMES}
    near_by_arm = {
        p: sum(1 for g in groups if i in g["acceptable_idxs"]) / n
        for i, p in enumerate(PRESET_NAMES)
    }
    best_strict_arm = max(strict_by_arm, key=strict_by_arm.get)
    best_near_arm = max(near_by_arm, key=near_by_arm.get)

    probs = [dist[p] / n for p in PRESET_NAMES if dist[p]]
    entropy_bits = -sum(q * math.log2(q) for q in probs)

    n_floored = sum(1 for g in groups if g["hit_sigma_floor"])
    mean_abs_adv = statistics.mean(abs(a) for g in groups for a in g["advantages"])
    mean_regret_adv = statistics.mean(
        max(g["advantages"]) - statistics.mean(g["advantages"]) for g in groups
    )
    n_multi_accept = sum(1 for g in groups if len(g["acceptable_idxs"]) > 1)

    print(f"\n{'='*100}")
    print(f"  {label}")
    print(f"{'='*100}")
    print(f"  trainable groups (survived sigma_floor flat-filter): {n}   (dropped flat: {dropped})")
    print(f"  oracle-arm distribution (sk/li/st/dp): {[dist[p] for p in PRESET_NAMES]}")
    print(f"  label-distribution entropy: {entropy_bits:.3f} bits (max 2.000 = perfectly balanced)")
    print(f"  *** best constant predictor, STRICT:   '{best_strict_arm}' -> {strict_by_arm[best_strict_arm]:.1%}")
    print(f"  *** best constant predictor, NEAR-TIE: '{best_near_arm}' -> {near_by_arm[best_near_arm]:.1%}")
    print(f"      (all arms strict: {', '.join(f'{p}={strict_by_arm[p]:.1%}' for p in PRESET_NAMES)})")
    print(f"      (all arms near:   {', '.join(f'{p}={near_by_arm[p]:.1%}' for p in PRESET_NAMES)})")
    print(f"  sigma_floor_fraction (raw_std < {_SIGMA_FLOOR}, denominator-clamped): {n_floored/n:.1%}")
    print(f"  groups with >1 acceptable arm (near_tie_margin={_NEAR_TIE_MARGIN}): {n_multi_accept/n:.1%}")
    print(f"  mean |advantage| (gradient magnitude seen by policy): {mean_abs_adv:.4f}")
    print(f"  mean top-advantage-above-mean (regret signal): {mean_regret_adv:.4f}")
    print(f"  median section margin: {statistics.median(g['margin'] for g in groups):.4f}")
    return {
        "n": n, "dist": dist, "strict_base": strict_by_arm[best_strict_arm],
        "near_base": near_by_arm[best_near_arm], "entropy": entropy_bits,
        "floored": n_floored / n, "mean_abs_adv": mean_abs_adv,
        "groups": {g["name"]: g for g in groups},
    }


def main():
    single, sdrop = load_groups("section_oracle.json")
    avg, adrop = load_groups("section_oracle_averaged.json")
    s = analyze("SINGLE-DRAW labels (section_oracle.json) — what every run to date trained on", single, sdrop)
    a = analyze("N=3-AVERAGED labels (section_oracle_averaged.json) — what a replication retrain would use", avg, adrop)

    print(f"\n{'='*100}")
    print("  HEAD-TO-HEAD: what changes for the next retrain")
    print(f"{'='*100}")
    print(f"  {'quantity':<52} {'single-draw':>12} {'averaged':>12} {'delta':>10}")
    print("  " + "-" * 88)
    rows = [
        ("trainable groups", s["n"], a["n"], "higher=more data"),
        ("STRICT constant-predictor bar to beat", f"{s['strict_base']:.1%}", f"{a['strict_base']:.1%}", "lower=easier"),
        ("NEAR-TIE constant-predictor bar to beat", f"{s['near_base']:.1%}", f"{a['near_base']:.1%}", "lower=easier"),
        ("label entropy (bits, 2.0=balanced)", f"{s['entropy']:.3f}", f"{a['entropy']:.3f}", "higher=balanced"),
        ("sigma_floor_fraction", f"{s['floored']:.1%}", f"{a['floored']:.1%}", "lower=better"),
        ("mean |advantage|", f"{s['mean_abs_adv']:.4f}", f"{a['mean_abs_adv']:.4f}", "higher=stronger"),
    ]
    for name, sv, av, note in rows:
        print(f"  {name:<52} {str(sv):>12} {str(av):>12}   ({note})")

    # label agreement between the two sets, on sections present in both
    common = set(s["groups"]) & set(a["groups"])
    agree = sum(1 for k in common if s["groups"][k]["best_idx"] == a["groups"][k]["best_idx"])
    print(f"\n  Sections present in BOTH trainable sets: {len(common)}")
    print(f"  ...of which the oracle arm AGREES: {agree}/{len(common)} = {agree/len(common):.1%}")
    print(f"  ...i.e. the retrain would train on a DIFFERENT target for {len(common)-agree} "
          f"({1-agree/len(common):.1%}) of shared sections")

    only_single = set(s["groups"]) - set(a["groups"])
    only_avg = set(a["groups"]) - set(s["groups"])
    print(f"\n  Sections trainable ONLY under single-draw (averaging flattened them): {len(only_single)}")
    print(f"  Sections trainable ONLY under averaged (averaging separated them):     {len(only_avg)}")


if __name__ == "__main__":
    main()
