"""Analyze the pairwise-grading judge's repeat-draws noise floor for light_vs_standard.

Companion to analyze_repeat_noise.py (which did this for standard_vs_deep).
Consumes:
  - pairwise_repeat_targets_light_vs_standard.json (4 strong-disagreement +
    4 strong-agreement targets, from select_light_repeat_targets.py)
  - rl_training_data/pairwise_pilot/<article>/pairwise_repeats_light_vs_standard.json
    (N extra draws per target, written by
    writing_workflow/rl_pairwise_repeat_check.py --output-name pairwise_repeats_light_vs_standard.json)

Same method as analyze_repeat_noise.py: combine ORIGINAL + repeat draws into
one distribution of (standard - light) deltas per target (fixed a_arm/b_arm
frame, never re-randomized), report label distribution/spread, whether
denoising flips the tag-vs-pairwise classification, and the denoised vs
single-draw correlation on this specific target subset.

Does NOT call any LLM -- pure post-hoc analysis of already-collected data.

Usage (from research_agent_local/training/):
  python3 analyze_light_repeat_noise.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from analyze_light_boundary import _delta_in_frame, _classify
from pairwise_reward import _PAIRWISE_DIR

_THIS_DIR = Path(__file__).resolve().parent
_TARGETS_PATH = _THIS_DIR / "pairwise_repeat_targets_light_vs_standard.json"
_REPEATS_FILENAME = "pairwise_repeats_light_vs_standard.json"
_ARM_X, _ARM_Y = "light", "standard"


def analyze() -> None:
    targets = json.loads(_TARGETS_PATH.read_text(encoding="utf-8"))

    repeats_cache: dict[str, dict] = {}
    rows = []

    for target in targets:
        article = target["article"]
        if article not in repeats_cache:
            repeats_path = _PAIRWISE_DIR / article / _REPEATS_FILENAME
            if not repeats_path.exists():
                print(f"SKIP {article}: no {_REPEATS_FILENAME} found at {repeats_path}")
                repeats_cache[article] = None
                continue
            repeats_cache[article] = json.loads(repeats_path.read_text(encoding="utf-8"))
        data = repeats_cache[article]
        if data is None:
            continue

        entry = data.get("sections", {}).get(target["section_title"], {}).get(target["dimension"])
        if entry is None:
            print(f"SKIP {article} / {target['section_title']} / {target['dimension']}: no repeat data found")
            continue

        a_arm, b_arm = target["a_arm"], target["b_arm"]
        all_preferences = [target["original_preference"]] + [
            r["preference"] for r in entry["repeats"] if "error" not in r
        ]
        all_deltas = [
            d for p in all_preferences if (d := _delta_in_frame(p, a_arm, b_arm, _ARM_X, _ARM_Y)) is not None
        ]

        denoised_margin = sum(all_deltas) / len(all_deltas) if all_deltas else 0.0
        new_class = _classify(target["tag_margin"], denoised_margin)

        rows.append(
            {
                "target": target,
                "all_preferences": all_preferences,
                "all_deltas": all_deltas,
                "denoised_margin": denoised_margin,
                "original_classification": target["classification"],
                "new_classification": new_class,
            }
        )

    print("=" * 100)
    for row in rows:
        t = row["target"]
        label_counts = Counter(row["all_preferences"])
        spread = (max(row["all_deltas"]) - min(row["all_deltas"])) if row["all_deltas"] else 0.0
        flipped = row["new_classification"] != row["original_classification"]
        flip_note = "  <-- FLIPPED after denoising" if flipped else ""
        print(f"{t['article']} | {t['section_title']} | {t['dimension']}  [{t['classification']}]")
        print(f"  labels across {len(row['all_preferences'])} draws: {dict(label_counts)}  (spread={spread:.3f})")
        print(
            f"  tag_margin={t['tag_margin']:+.3f}  single_draw_pw_margin={t['pairwise_margin_single_draw']:+.3f}  "
            f"denoised_pw_margin={row['denoised_margin']:+.3f}  -> {row['new_classification']}{flip_note}"
        )

    n = len(rows)
    if n >= 2:
        tag_vals = [row["target"]["tag_margin"] for row in rows]
        single_vals = [row["target"]["pairwise_margin_single_draw"] for row in rows]
        denoised_vals = [row["denoised_margin"] for row in rows]

        def _pearson(xs, ys):
            mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
            cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
            vx = sum((x - mx) ** 2 for x in xs)
            vy = sum((y - my) ** 2 for y in ys)
            return cov / (vx * vy) ** 0.5 if vx > 0 and vy > 0 else 0.0

        r_single = _pearson(tag_vals, single_vals)
        r_denoised = _pearson(tag_vals, denoised_vals)
        n_disagree_flipped = sum(
            1 for row in rows if row["original_classification"] == "strong_disagree" and row["new_classification"] != "strong_disagree"
        )
        n_disagree_total = sum(1 for row in rows if row["original_classification"] == "strong_disagree")
        n_agree_flipped = sum(
            1 for row in rows if row["original_classification"] == "strong_agree" and row["new_classification"] != "strong_agree"
        )
        n_agree_total = sum(1 for row in rows if row["original_classification"] == "strong_agree")

        print("=" * 100)
        print(f"On this {n}-target subset:")
        print(f"  tag vs SINGLE-draw pairwise margin:   r={r_single:+.3f}")
        print(f"  tag vs DENOISED (mean-of-draws) margin: r={r_denoised:+.3f}")
        print(f"  strong_disagree targets that FLIPPED to agreement after denoising: {n_disagree_flipped}/{n_disagree_total}")
        print(f"  strong_agree (control) targets that FLIPPED to disagreement after denoising: {n_agree_flipped}/{n_agree_total}")


if __name__ == "__main__":
    analyze()
