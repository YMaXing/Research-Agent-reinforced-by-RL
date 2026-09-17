"""Select repeat-draw targets for the light_vs_standard noise-floor check.

Companion to select_repeat_targets.py (which did this for standard_vs_deep).
Re-derives the classification from analyze_light_boundary.py's already-computed
rows (re-run here, zero LLM cost) for the light_vs_standard pair specifically
-- light_vs_deep showed no directional signal in the free first look and is
not targeted here.

Outputs a target list in the EXACT SAME schema as pairwise_repeat_targets.json
(article, section_title, dimension, classification, a_arm, b_arm,
original_preference, tag_margin, pairwise_margin_single_draw) so it is directly
consumable by the EXISTING writing_workflow/rl_pipeline/rl_pairwise_repeat_check.py driver
with no code changes there -- only --targets and --output-name need to point
at this round's files (see that script's --output-name flag, added specifically
so this second round does not overwrite the first round's pairwise_repeats.json).

Does NOT call any LLM -- pure re-derivation from already-collected pilot data.

Usage (from research_agent_local/training/):
  python3 select_light_repeat_targets.py --out pairwise_repeat_targets_light_vs_standard.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))

from analyze_light_boundary import _ARTICLES, _classify, _delta_in_frame, _lookup_tag_credit, _DIMENSIONS
from pairwise_reward import _PAIRWISE_DIR, _tag_credits_for_arm
import generate_episode_oracles as geo

_THIS_DIR = Path(__file__).resolve().parent
_PAIR_KEY = "light_vs_standard"
_ARM_X, _ARM_Y = "light", "standard"


def select_targets(n_agree_controls: int) -> list[dict]:
    disagree_targets: list[dict] = []
    agree_targets: list[dict] = []

    for article in _ARTICLES:
        path = _PAIRWISE_DIR / article / "pairwise_judgments.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        tag_x = _tag_credits_for_arm(article, _ARM_X)
        tag_y = _tag_credits_for_arm(article, _ARM_Y)

        for title, sec in data["sections"].items():
            entry = sec.get(_PAIR_KEY)
            if not entry or "error" in entry:
                continue
            a_arm, b_arm = entry["a_arm"], entry["b_arm"]
            norm_title = geo._normalize(title)
            for dim in _DIMENSIONS:
                dim_judgment = entry.get(dim)
                if not dim_judgment:
                    continue
                delta = _delta_in_frame(dim_judgment["preference"], a_arm, b_arm, _ARM_X, _ARM_Y)
                if delta is None:
                    continue
                tag_margin = _lookup_tag_credit(tag_y, norm_title, dim) - _lookup_tag_credit(tag_x, norm_title, dim)
                kind = _classify(tag_margin, delta)
                if kind not in ("strong_agree", "strong_disagree"):
                    continue

                target = {
                    "article": article,
                    "section_title": title,
                    "dimension": dim,
                    "classification": kind,
                    "a_arm": a_arm,
                    "b_arm": b_arm,
                    "original_preference": dim_judgment["preference"],
                    "tag_margin": round(tag_margin, 4),
                    "pairwise_margin_single_draw": round(delta, 4),
                }
                (disagree_targets if kind == "strong_disagree" else agree_targets).append(target)

    if n_agree_controls and len(agree_targets) > n_agree_controls:
        step = len(agree_targets) / n_agree_controls
        agree_sample = [agree_targets[int(i * step)] for i in range(n_agree_controls)]
    else:
        agree_sample = agree_targets

    return disagree_targets + agree_sample


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--n-agree-controls", type=int, default=4)
    parser.add_argument("--out", type=Path, default=_THIS_DIR / "pairwise_repeat_targets_light_vs_standard.json")
    args = parser.parse_args()

    targets = select_targets(args.n_agree_controls)
    n_disagree = sum(1 for t in targets if t["classification"] == "strong_disagree")
    n_agree = sum(1 for t in targets if t["classification"] == "strong_agree")
    args.out.write_text(json.dumps(targets, indent=2), encoding="utf-8")
    print(f"Selected {len(targets)} targets ({n_disagree} strong_disagree + {n_agree} strong_agree controls)")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
