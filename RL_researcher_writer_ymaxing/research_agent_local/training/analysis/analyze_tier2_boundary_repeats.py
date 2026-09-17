"""Analyze the tier-2 credit-boundary repeat-draws noise-floor check.

Consumes:
  - pairwise_tier2_boundary_targets.json (the 7 clean tier0-vs-tier2 targets,
    including the ORIGINAL 3 draws already collected by the scaled
    standard-vs-deep run -- see select_tier2_boundary_targets.py)
  - rl_training_data/pairwise/pilot/<article>/pairwise_repeats_tier2_boundary.json
    (the NEW repeat draws, written by writing_workflow/rl_pipeline/rl_pairwise_repeat_check.py)

Pools the ORIGINAL 3 draws + the NEW repeat draws into one combined sample per
target (same A/B slot throughout, so this isolates judge-call noise, not
position-bias noise -- same convention as the tier-1 repeat-draws check), then
recomputes the per-target and aggregate "clean 0-vs-2 magnitude" estimate with
the larger pooled N, to see whether the N=7/N=3-draws-each estimate (+0.169,
implying a 4.73x overstatement vs the tag's flat +0.800 jump) holds up.

Does NOT call any LLM -- pure post-hoc analysis.

Usage (from research_agent_local/training/):
  python3 analyze_tier2_boundary_repeats.py
  python3 analyze_tier2_boundary_repeats.py --targets pairwise_tier2_boundary_targets.json \\
      --repeats-name pairwise_repeats_tier2_boundary.json
"""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

from pairwise_reward import PREFERENCE_TO_DELTA

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_PAIRWISE_PILOT_DIR = _REPO_ROOT / "rl_training_data" / "pairwise" / "pilot"

_DEFAULT_TARGETS = _THIS_DIR / "pairwise_tier2_boundary_targets.json"
_DEFAULT_REPEATS_NAME = "pairwise_repeats_tier2_boundary.json"


def _delta_std_deep(preference: str, a_arm: str, b_arm: str) -> float | None:
    if preference not in PREFERENCE_TO_DELTA:
        return None
    raw = PREFERENCE_TO_DELTA[preference]
    if a_arm == "standard" and b_arm == "deep":
        return -raw
    if a_arm == "deep" and b_arm == "standard":
        return raw
    return None


def analyze(targets_path: Path, repeats_name: str) -> None:
    targets = json.loads(targets_path.read_text(encoding="utf-8"))

    all_magnitudes: list[float] = []
    print("=" * 100)
    for t in targets:
        article, title, dim = t["article"], t["section_title"], t["dimension"]
        a_arm, b_arm = t["a_arm"], t["b_arm"]
        side_with_2_is_std = t["side_with_2_is_std"]

        # Original 3 draws (already collected, from stddeep_judgments.json)
        orig_prefs = t.get("original_preferences_all_3", [])
        pooled_deltas = [dd for p in orig_prefs if (dd := _delta_std_deep(p, a_arm, b_arm)) is not None]
        n_orig = len(pooled_deltas)

        # New repeat draws, if collected yet
        repeats_path = _PAIRWISE_PILOT_DIR / article / repeats_name
        n_new = 0
        if repeats_path.exists():
            data = json.loads(repeats_path.read_text(encoding="utf-8"))
            entry = data.get("sections", {}).get(title, {}).get(dim)
            if entry:
                for r in entry.get("repeats", []):
                    if "error" in r:
                        continue
                    dd = _delta_std_deep(r["preference"], entry["a_arm"], entry["b_arm"])
                    if dd is not None:
                        pooled_deltas.append(dd)
                        n_new += 1

        if not pooled_deltas:
            print(f"  [{article} / {title} / {dim}] NO DATA")
            continue

        # Normalize sign: positive = the 2-instance side winning
        pooled_signed = [d if side_with_2_is_std else -d for d in pooled_deltas]
        mean_signed = statistics.mean(pooled_signed)
        std_signed = statistics.pstdev(pooled_signed) if len(pooled_signed) > 1 else 0.0
        all_magnitudes.append(mean_signed)

        status = "REPEATS COLLECTED" if n_new else "original 3-draws only (repeats not yet run)"
        print(
            f"  [{article:<32}] {title[:32]:32s} {dim:8s} n_orig={n_orig} n_new={n_new}  "
            f"pooled_mean={mean_signed:+.4f}  pooled_std={std_signed:.4f}  ({status})"
        )

    print("=" * 100)
    if all_magnitudes:
        overall_mean = statistics.mean(all_magnitudes)
        print(f"N targets: {len(all_magnitudes)}")
        print(f"Mean pooled magnitude (2-instance side advantage): {overall_mean:+.4f}")
        print(f"Current tag jump (tier2 - tier0): +0.8000")
        if overall_mean > 0:
            print(f"Implied overstatement ratio: {0.8 / overall_mean:.2f}x")
        print()
        print("Compare to the pre-repeat estimate (3 draws/target only): +0.1690 (4.73x overstatement)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--targets", type=Path, default=_DEFAULT_TARGETS)
    parser.add_argument("--repeats-name", default=_DEFAULT_REPEATS_NAME)
    args = parser.parse_args()
    analyze(args.targets, args.repeats_name)


if __name__ == "__main__":
    main()
