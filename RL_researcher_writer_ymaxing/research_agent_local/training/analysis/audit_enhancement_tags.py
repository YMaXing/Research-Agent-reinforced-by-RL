"""Corpus-wide audit of the enhancement [instances=N; quality=...] tags
actually present in reasoning.json, across every arm (skip/light/standard/deep).

Motivation: after the full-corpus regen (see run13_rl_grok_pipeline_analysis.md
Part 5 / diff_oracle_regen.py), the arm distribution moved OPPOSITE to the
fix's motivating hypothesis -- light grew (19->22), deep shrank (5->2), not
the reverse. The fix's whole premise assumes `deep` typically has MORE
qualifying enhancement instances per section than `light` (so the new
count-aware credit curve should reward it more once the old binary ceiling
stops masking that difference). This script tests that assumption directly
against the REAL, now fully-tagged corpus instead of continuing to reason
from the 2-article pilot sample.

For every (article, arm) pair, loads the depth_enhancement + breadth_enhancement
dimension entries from that arm's actual episode reasoning.json, parses the
[instances=N; quality=...] tag per section, and reports:
  - mean/median instance count per arm, corpus-wide
  - the count histogram (0,1,2,3,4,5,6+) per arm
  - mean enhancement_credit() per arm (the actual number _section_reward sees)

Read-only, zero cost -- pure aggregation over already-graded data.

Usage (from research_agent_local/):
  python3 training/audit_enhancement_tags.py
  python3 training/audit_enhancement_tags.py --articles 13_agent_framework Dark_Dimension
"""

from __future__ import annotations

import argparse
import statistics
import sys
from collections import Counter
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"

_ARM_ORDER = ["skip", "light", "standard", "deep"]
_DIMS = ["ground_truth_depth_enhancement", "ground_truth_breadth_enhancement"]


def _iter_article_dirs() -> list[str]:
    return sorted(
        d.name for d in _BASES_DIR.iterdir()
        if d.is_dir() and (d / "article_oracle.json").exists()
    )


def _episode_dir_for_arm(article_dir_name: str, arm: str) -> Path:
    no_variant = "__var_" not in article_dir_name
    if no_variant:
        preset = geo._TEST_ARM_PRESETS[arm][0]
        return _TEST_EPISODES_DIR / f"{article_dir_name}__preset{preset}"
    preset = geo._ARM_PRESETS[arm][0]
    return _EPISODES_DIR / f"{article_dir_name}__preset{preset}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=None, help="Restrict to these bases/ dir names (default: all)")
    args = parser.parse_args()

    article_dirs = args.articles if args.articles else _iter_article_dirs()

    # Per-arm accumulators
    counts_by_arm: dict[str, list[int]] = {a: [] for a in _ARM_ORDER}
    credits_by_arm: dict[str, list[float]] = {a: [] for a in _ARM_ORDER}
    quality_counter_by_arm: dict[str, Counter] = {a: Counter() for a in _ARM_ORDER}
    n_tagged_by_arm: dict[str, int] = {a: 0 for a in _ARM_ORDER}
    n_untagged_by_arm: dict[str, int] = {a: 0 for a in _ARM_ORDER}

    for article_dir in article_dirs:
        for arm in _ARM_ORDER:
            ep_dir = _episode_dir_for_arm(article_dir, arm)
            episode = geo._load_episode(ep_dir)
            for dim in _DIMS:
                for _raw, _norm, _score, enh in episode.get(dim, []):
                    if enh is None:
                        n_untagged_by_arm[arm] += 1
                        continue
                    n_tagged_by_arm[arm] += 1
                    count, qualities = enh
                    counts_by_arm[arm].append(count)
                    credits_by_arm[arm].append(enhancement_credit(qualities))
                    quality_counter_by_arm[arm].update(qualities)

    print("=" * 100)
    print(f"ENHANCEMENT TAG AUDIT: {len(article_dirs)} article(s), dims={_DIMS}")
    print("=" * 100)
    for arm in _ARM_ORDER:
        counts = counts_by_arm[arm]
        credits = credits_by_arm[arm]
        n_tagged = n_tagged_by_arm[arm]
        n_untagged = n_untagged_by_arm[arm]
        print(f"\n  ARM: {arm}")
        print(f"    tagged entries: {n_tagged}   untagged (legacy) entries: {n_untagged}")
        if not counts:
            print("    (no tagged data)")
            continue
        hist = Counter(min(c, 6) for c in counts)
        hist_str = "  ".join(f"{k}{'+' if k == 6 else ''}:{hist.get(k, 0)}" for k in range(0, 7))
        print(f"    instance-count histogram: [{hist_str}]")
        print(f"    mean count={statistics.mean(counts):.3f}  median={statistics.median(counts):.1f}  "
              f"max={max(counts)}")
        print(f"    mean enhancement_credit()={statistics.mean(credits):.4f}  "
              f"(old-binary-equivalent would be ~1.0 for any count>=1, 0.0 for count=0)")
        zero_frac = sum(1 for c in counts if c == 0) / len(counts)
        one_frac = sum(1 for c in counts if c == 1) / len(counts)
        multi_frac = sum(1 for c in counts if c >= 2) / len(counts)
        print(f"    fraction: 0-instance={zero_frac:.2%}  1-instance={one_frac:.2%}  2+instance={multi_frac:.2%}")
        qc = quality_counter_by_arm[arm]
        total_q = sum(qc.values())
        if total_q:
            print(f"    quality mix (of {total_q} instances): " +
                  "  ".join(f"{q}={n} ({n/total_q:.1%})" for q, n in qc.most_common()))

    print()
    print("=" * 100)
    print("CROSS-ARM COMPARISON (the decisive check: does deep > standard > light on mean count/credit?)")
    print("=" * 100)
    for label, acc in (("mean instance count", counts_by_arm), ("mean enhancement_credit", credits_by_arm)):
        vals = {a: (statistics.mean(acc[a]) if acc[a] else float("nan")) for a in _ARM_ORDER}
        print(f"  {label}: " + "  ".join(f"{a}={vals[a]:.3f}" for a in _ARM_ORDER))


if __name__ == "__main__":
    main()
