"""Select repeat-draw targets for the pairwise-grading noise-floor check.

Reads pairwise_pilot_report.json (produced by pairwise_reward.py) and the raw
pairwise_judgments.json files, recomputes the same tag-vs-pairwise margin
classification used in the pilot analysis, and selects a small, cheap target
set for the repeated-draws noise check:
  - ALL "strong disagreement" (article, section, dimension) triples (both
    methods confident, opposite sign) -- the cases we actually need to explain.
  - A deterministic sample of "strong agreement" triples as a control group
    (if repeats are just as noisy here, that tells us something about the
    method in general, not something specific to the disagreement cases).

For each target, also pulls the standard_vs_deep pair's ORIGINAL a_arm/b_arm
assignment (so the repeat-draws driver reuses the exact same A/B slot instead
of re-randomizing -- isolating judge-call noise from position-bias noise).

Does NOT call any LLM -- pure re-derivation from already-collected data.

Usage (from research_agent_local/training/):
  python3 select_repeat_targets.py --out pairwise_repeat_targets.json
  python3 select_repeat_targets.py --n-agree-controls 5 --out pairwise_repeat_targets.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent.parent
_PAIRWISE_DIR = _REPO_ROOT / "rl_training_data" / "pairwise" / "pilot"

_STRONG_MARGIN = 0.05
_DIMENSIONS = ("depth", "breadth")


def _classify(tag_margin: float, pw_margin: float) -> str:
    if abs(tag_margin) < 0.02 and abs(pw_margin) < 0.02:
        return "trivial"
    if abs(tag_margin) >= _STRONG_MARGIN and abs(pw_margin) >= _STRONG_MARGIN:
        return "strong_agree" if (tag_margin > 0) == (pw_margin > 0) else "strong_disagree"
    return "weak"


def select_targets(report_path: Path, n_agree_controls: int) -> list[dict]:
    reports = json.loads(report_path.read_text(encoding="utf-8"))

    disagree_targets: list[dict] = []
    agree_targets: list[dict] = []

    for report in reports:
        article = report["article"]
        judgments_path = _PAIRWISE_DIR / article / "pairwise_judgments.json"
        raw = json.loads(judgments_path.read_text(encoding="utf-8"))

        for title, entry in report["sections"].items():
            std_vs_deep = raw["sections"].get(title, {}).get("standard_vs_deep")
            if not std_vs_deep or "error" in std_vs_deep:
                continue
            for dim in _DIMENSIONS:
                tag = entry["tag"]
                pw = entry["pairwise"][dim]
                tag_margin = tag["standard"][dim] - tag["deep"][dim]
                pw_margin = pw["standard"] - pw["deep"]
                kind = _classify(tag_margin, pw_margin)
                if kind not in ("strong_agree", "strong_disagree"):
                    continue

                target = {
                    "article": article,
                    "section_title": title,
                    "dimension": dim,
                    "classification": kind,
                    "a_arm": std_vs_deep["a_arm"],
                    "b_arm": std_vs_deep["b_arm"],
                    "original_preference": std_vs_deep[dim]["preference"],
                    "tag_margin": round(tag_margin, 4),
                    "pairwise_margin_single_draw": round(pw_margin, 4),
                }
                (disagree_targets if kind == "strong_disagree" else agree_targets).append(target)

    # Deterministic sample of agreement controls: evenly spaced through the list
    # (not random) so the selection is reproducible without needing a fixed seed.
    if n_agree_controls and len(agree_targets) > n_agree_controls:
        step = len(agree_targets) / n_agree_controls
        agree_sample = [agree_targets[int(i * step)] for i in range(n_agree_controls)]
    else:
        agree_sample = agree_targets

    return disagree_targets + agree_sample


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", type=Path, default=_THIS_DIR / "pairwise_pilot_report.json")
    parser.add_argument("--n-agree-controls", type=int, default=5)
    parser.add_argument("--out", type=Path, default=_THIS_DIR / "pairwise_repeat_targets.json")
    args = parser.parse_args()

    targets = select_targets(args.report, args.n_agree_controls)
    n_disagree = sum(1 for t in targets if t["classification"] == "strong_disagree")
    n_agree = sum(1 for t in targets if t["classification"] == "strong_agree")
    args.out.write_text(json.dumps(targets, indent=2), encoding="utf-8")
    print(f"Selected {len(targets)} targets ({n_disagree} strong_disagree + {n_agree} strong_agree controls)")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
