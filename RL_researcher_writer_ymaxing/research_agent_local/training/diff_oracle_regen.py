"""Diff article_oracle.json across a before/after pair of bases/ directories.

Purpose: the single most important sanity check for a full-corpus oracle
regeneration (e.g. after re-grading all 40 articles with the enhancement
count/quality tag, see run13_rl_grok_pipeline_analysis.md Part 5 §25-36) --
before touching any reward-formula lever, first confirm what the ALREADY-
DESIGNED, ALREADY-VALIDATED fix (current production defaults: INSTANCE_CAP=3,
QUALITY_WEIGHT strong=1.00/standard=0.65, credit curve, explore_mult=0.50
baked into generate_episode_oracles.py::_section_reward) actually does at full
scale, versus the n=2 sample this was piloted on.

Reports, per article:
  - oracle_arm flip (old -> new), if any
  - margin delta
Reports in aggregate:
  - arm distribution before vs after (does light's over-representation shrink,
    per the original §25 motivating hypothesis?)
  - flip count, split by whether the OLD margin was thin (<0.06) or
    comfortable (>=0.06) -- flips concentrated in thin-margin articles are
    expected/lower-risk; flips in comfortable-margin articles are the ones
    worth manually inspecting first.

Does NOT recompute anything itself -- purely reads two already-computed sets
of article_oracle.json files. Read-only, zero cost.

Usage (from research_agent_local/):
  python3 training/diff_oracle_regen.py --before rl_training_data/bases_PRETAG_BACKUP_20260723 --after rl_training_data/bases
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_DEFAULT_AFTER = _THIS_DIR.parent.parent / "rl_training_data" / "bases"

_ARM_ORDER = ["skip", "light", "standard", "deep"]


def _load_oracle(bases_dir: Path, name: str) -> dict | None:
    p = bases_dir / name / "article_oracle.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--before", required=True, type=Path, help="Path to the pre-regen backup bases/ dir")
    parser.add_argument("--after", type=Path, default=_DEFAULT_AFTER, help="Path to the post-regen bases/ dir (default: production)")
    parser.add_argument("--thin-threshold", type=float, default=0.06, help="Old margin below this = 'thin' (default 0.06, matches audit_oracle_margins.py's HIGH tier)")
    args = parser.parse_args()

    names = sorted(
        d.name for d in args.before.iterdir()
        if d.is_dir() and (d / "article_oracle.json").exists()
    )

    flips: list[tuple[str, str, str, float, float]] = []  # name, old_arm, new_arm, old_margin, new_margin
    unchanged = 0
    missing_after = []
    old_dist = {a: 0 for a in _ARM_ORDER}
    new_dist = {a: 0 for a in _ARM_ORDER}

    for name in names:
        old = _load_oracle(args.before, name)
        new = _load_oracle(args.after, name)
        if old is None:
            continue
        old_arm = old.get("oracle_arm")
        old_margin = old.get("margin", 0.0)
        if old_arm in old_dist:
            old_dist[old_arm] += 1
        if new is None:
            missing_after.append(name)
            continue
        new_arm = new.get("oracle_arm")
        new_margin = new.get("margin", 0.0)
        if new_arm in new_dist:
            new_dist[new_arm] += 1
        if new_arm != old_arm:
            flips.append((name, old_arm, new_arm, old_margin, new_margin))
        else:
            unchanged += 1

    print("=" * 100)
    print(f"ORACLE REGEN DIFF: {args.before} -> {args.after}")
    print("=" * 100)
    print(f"  {len(names)} article(s) in 'before'; {len(missing_after)} missing in 'after'")
    print(f"  {unchanged} unchanged, {len(flips)} flipped\n")

    print("  Arm distribution BEFORE:", {a: old_dist[a] for a in _ARM_ORDER})
    print("  Arm distribution AFTER: ", {a: new_dist[a] for a in _ARM_ORDER})
    print()

    if flips:
        thin_flips = [f for f in flips if abs(f[3]) < args.thin_threshold]
        comfortable_flips = [f for f in flips if abs(f[3]) >= args.thin_threshold]
        print(f"  FLIPS split by old margin (thin < {args.thin_threshold}):")
        print(f"    thin-margin flips: {len(thin_flips)}  (expected/lower-risk)")
        print(f"    comfortable-margin flips: {len(comfortable_flips)}  (inspect these first)")
        print()
        print("  All flips:")
        for name, old_arm, new_arm, old_margin, new_margin in flips:
            tag = "COMFORTABLE" if abs(old_margin) >= args.thin_threshold else "thin"
            print(f"    {name:<45} {old_arm:<8} -> {new_arm:<8}  old_margin={old_margin:+.4f}  new_margin={new_margin:+.4f}  ({tag})")

    if missing_after:
        print(f"\n  MISSING in 'after' (not yet regenerated): {', '.join(missing_after)}")


if __name__ == "__main__":
    main()
