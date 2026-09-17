"""Analyze the pairwise-grading judge's repeat-draws noise floor.

Consumes:
  - pairwise_repeat_targets.json (10 strong-disagreement + 5 strong-agreement
    targets, each with its original single-draw preference + a_arm/b_arm)
  - rl_training_data/pairwise/pilot/<article>/pairwise_repeats.json (N extra
    draws per target, written by writing_workflow/rl_pipeline/rl_pairwise_repeat_check.py)

For each target, combines the ORIGINAL draw + the N repeat draws into one
distribution of standard-vs-deep deltas (converted to a fixed (standard,deep)
frame using each target's fixed a_arm/b_arm -- never re-randomized, so this is
a clean isolation of judge-call noise). Reports:
  - the raw preference-label distribution across all draws (does the SAME
    input ever produce a DIFFERENT label?)
  - the denoised (mean-of-all-draws) margin, vs. the original single-draw margin
  - whether denoising flips the tag-vs-pairwise classification (strong_disagree
    -> agrees, or strong_agree -> disagrees)
  - the overall correlation between denoised pairwise margin and tag margin,
    compared to the single-draw correlation on the SAME 15 targets (apples to
    apples -- the pilot's r=0.223 was computed over all 92 observations, most
    of which are NOT in this repeat set, so don't compare against that number
    directly).

Does NOT call any LLM -- pure post-hoc analysis of already-collected data.

Usage (from research_agent_local/training/):
  python3 analyze_repeat_noise.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from pairwise_reward import PREFERENCE_TO_DELTA, _PAIRWISE_DIR

_THIS_DIR = Path(__file__).resolve().parent
_TARGETS_PATH = _THIS_DIR / "pairwise_repeat_targets.json"

_STRONG_MARGIN = 0.05


def _classify(tag_margin: float, pw_margin: float) -> str:
    if abs(tag_margin) < 0.02 and abs(pw_margin) < 0.02:
        return "trivial"
    if abs(tag_margin) >= _STRONG_MARGIN and abs(pw_margin) >= _STRONG_MARGIN:
        return "strong_agree" if (tag_margin > 0) == (pw_margin > 0) else "strong_disagree"
    return "weak"


def _delta_in_std_deep_frame(preference: str, a_arm: str, b_arm: str) -> float | None:
    """Convert one preference label to a signed (standard - deep) delta, given
    the target's FIXED a_arm/b_arm (same for every draw of this target).
    """
    if preference not in PREFERENCE_TO_DELTA:
        return None
    raw = PREFERENCE_TO_DELTA[preference]  # positive means B > A
    if a_arm == "standard" and b_arm == "deep":
        return -raw  # B(deep)-A(standard) = raw  =>  standard-deep = -raw
    if a_arm == "deep" and b_arm == "standard":
        return raw  # B(standard)-A(deep) = raw  =>  standard-deep = raw
    raise ValueError(f"Unexpected arm pair for a std-vs-deep repeat target: {a_arm}/{b_arm}")


def analyze() -> None:
    targets = json.loads(_TARGETS_PATH.read_text(encoding="utf-8"))

    repeats_cache: dict[str, dict] = {}
    rows = []  # (target, all_deltas, denoised_margin, new_classification)

    for target in targets:
        article = target["article"]
        if article not in repeats_cache:
            repeats_path = _PAIRWISE_DIR / article / "pairwise_repeats.json"
            if not repeats_path.exists():
                print(f"SKIP {article}: no pairwise_repeats.json found at {repeats_path}")
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
        all_deltas = [d for p in all_preferences if (d := _delta_in_std_deep_frame(p, a_arm, b_arm)) is not None]

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

    # Aggregate: correlation on this 15-target subset, single-draw vs denoised.
    n = len(rows)
    if n >= 2:
        tag_vals = [row["target"]["tag_margin"] for row in rows]
        single_vals = [row["target"]["pairwise_margin_single_draw"] for row in rows]
        denoised_vals = [row["denoised_margin"] for row in rows]

        def _pearson(xs: list[float], ys: list[float]) -> float:
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
        print(f"On this {n}-target subset (NOT comparable to the pilot's overall r=0.223, that was over all 92 obs):")
        print(f"  tag vs SINGLE-draw pairwise margin:   r={r_single:+.3f}")
        print(f"  tag vs DENOISED (mean-of-draws) margin: r={r_denoised:+.3f}")
        print(f"  strong_disagree targets that FLIPPED to agreement after denoising: {n_disagree_flipped}/{n_disagree_total}")
        print(f"  strong_agree (control) targets that FLIPPED to disagreement after denoising: {n_agree_flipped}/{n_agree_total}")


if __name__ == "__main__":
    analyze()
