"""Select repeat-draw targets for the tier-2 credit-boundary noise-floor check.

Scans rl_training_data/pairwise_stddeep_scale/<article>/stddeep_judgments.json
(already-collected, N=3-draws-per-section standard-vs-deep data) for the
CLEANEST possible tier-2 boundary comparisons: sections where one arm has
EXACTLY 0 weighted qualifying instances (tier0, credit=0.00) and the other has
EXACTLY 2.0 weighted instances (tier2, credit=0.80) -- the same style of
"clean tier-boundary isolation" that produced G0's ~0.207 point estimate for
tier1, applied here to tier2.

Motivation: analyze_stddeep_scale.py's tier-2+ filter (N=36, mixed comparison
types) found a 1.67x tag-vs-pairwise overstatement on average, but the isolated
N=7 clean 0-vs-2 cases showed a much sharper 4.73x overstatement (mean
pairwise-judged magnitude +0.169 vs the tag's flat +0.800 jump) -- see
run13_rl_grok_pipeline_analysis.md Part 7. N=7 is too small to trust directly
(this investigation's own standard: never ship off a small sample without a
repeat-draws noise check, per the tier-1 precedent). This script selects
those exact N=7 targets (plus any others matching the same clean-boundary
criterion the scaled run may have produced) for that check.

Preserves the ORIGINAL a_arm/b_arm slot assignment recorded in
stddeep_judgments.json (does NOT re-randomize) so rl_pairwise_repeat_check.py
can add MORE draws in the same frame, isolating judge-call noise from
position-bias noise -- exactly the tier-1 repeat-check convention.

Does NOT call any LLM -- pure re-derivation from already-collected data.

Usage (from research_agent_local/training/):
  python3 select_tier2_boundary_targets.py --out pairwise_tier2_boundary_targets.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import generate_episode_oracles as geo
from enhancement_reward import QUALITY_WEIGHT, INSTANCE_CAP
from pairwise_reward import PREFERENCE_TO_DELTA

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_SCALE_DIR = _REPO_ROOT / "rl_training_data" / "pairwise_stddeep_scale"


def _weighted_count(qualities: list[str]) -> float:
    weights = sorted((QUALITY_WEIGHT.get(q, 0.65) for q in qualities), reverse=True)
    return min(sum(weights[:INSTANCE_CAP]), float(INSTANCE_CAP))


def _get_enh(article: str, arm: str, dim: str, norm_title: str, idx: int) -> tuple[int, list[str]]:
    is_var = "__var_" in article
    if is_var:
        ep_dir = geo._EPISODES_DIR / f"{article}__preset{geo._ARM_PRESETS[arm][0]}"
    else:
        ep_dir = geo._TEST_EPISODES_DIR / f"{article}__preset{geo._TEST_ARM_PRESETS[arm][0]}"
    dims = geo._load_episode(ep_dir)
    key = "ground_truth_depth_enhancement" if dim == "depth" else "ground_truth_breadth_enhancement"
    entries = dims.get(key, [])
    enh = geo._get_enhancement(entries, norm_title, idx)
    return (0, []) if enh is None else enh


def _delta_std_deep(preference: str, a_arm: str, b_arm: str) -> float | None:
    if preference not in PREFERENCE_TO_DELTA:
        return None
    raw = PREFERENCE_TO_DELTA[preference]
    if a_arm == "standard" and b_arm == "deep":
        return -raw
    if a_arm == "deep" and b_arm == "standard":
        return raw
    return None


def select_targets() -> list[dict]:
    targets: list[dict] = []
    if not _SCALE_DIR.exists():
        return targets

    for article in sorted(p.name for p in _SCALE_DIR.iterdir() if p.is_dir()):
        path = _SCALE_DIR / article / "stddeep_judgments.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))

        for idx, (title, entry) in enumerate(data["sections"].items()):
            a_arm, b_arm = entry["a_arm"], entry["b_arm"]
            norm_title = geo._normalize(title)

            for dim in ("depth", "breadth"):
                cnt_std, q_std = _get_enh(article, "standard", dim, norm_title, idx)
                cnt_deep, q_deep = _get_enh(article, "deep", dim, norm_title, idx)
                wc_std, wc_deep = round(_weighted_count(q_std), 2), round(_weighted_count(q_deep), 2)

                is_clean_02 = (wc_std == 0.0 and wc_deep == 2.0) or (wc_std == 2.0 and wc_deep == 0.0)
                if not is_clean_02:
                    continue

                prefs = [d[dim]["preference"] for d in entry["draws"] if "error" not in d]
                deltas = [dd for p in prefs if (dd := _delta_std_deep(p, a_arm, b_arm)) is not None]
                if not deltas:
                    continue
                pw_margin_3draw = round(sum(deltas) / len(deltas), 4)
                side_with_2_is_std = wc_std == 2.0
                tag_margin = (0.80 if side_with_2_is_std else 0.0) - (0.0 if side_with_2_is_std else 0.80)

                targets.append(
                    {
                        "article": article,
                        "section_title": title,
                        "dimension": dim,
                        "classification": "tier2_boundary_0v2",
                        "a_arm": a_arm,
                        "b_arm": b_arm,
                        "original_preference": prefs[0] if prefs else None,
                        "original_preferences_all_3": prefs,
                        "tag_margin": round(tag_margin, 4),
                        "pw_margin_3draw_mean": pw_margin_3draw,
                        "cnt_std": cnt_std,
                        "cnt_deep": cnt_deep,
                        "side_with_2_is_std": side_with_2_is_std,
                    }
                )
    return targets


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=_THIS_DIR / "pairwise_tier2_boundary_targets.json")
    args = parser.parse_args()

    targets = select_targets()
    args.out.write_text(json.dumps(targets, indent=2), encoding="utf-8")

    print(f"Selected {len(targets)} clean tier0-vs-tier2 boundary targets -> {args.out}")
    for t in targets:
        print(
            f"  [{t['article']:<32}] {t['section_title'][:35]:35s} {t['dimension']:8s} "
            f"cnt(std={t['cnt_std']},deep={t['cnt_deep']})  a={t['a_arm']} b={t['b_arm']}  "
            f"pw_3draw_mean={t['pw_margin_3draw_mean']:+.3f}"
        )


if __name__ == "__main__":
    main()
