"""Set up replicate episode directories for the write+grade noise-measurement
experiment (Part 4 §20 fix #3, targeting the narrowest-margin articles flagged
by training/audit_oracle_margins.py, §22).

WHY THESE TWO ARTICLES: `audit_oracle_margins.py` flagged 09_RAG__var_standard
(margin=-0.0148) and 06_tools__var_standard (margin=-0.0046) as the two
narrowest NON-policy-forced margins in the whole corpus -- genuine near-tie
decisions where compute_article_oracle.py's secondary S3/S4/S5 signals had to
break the tie, exactly the kind of low-confidence label this experiment exists
to interrogate.

WHAT THIS SCRIPT DOES (cheap, read/copy only -- no LLM calls, no cost):
for each target article, copies each ACTIVE arm-preset's inputs
(article_guideline.md, research.md, .research/) from the real production
episode dir into N replicate directories under a SEPARATE root
(rl_training_data/noise_experiment/), so the (expensive) write+grade steps can
be re-run N times per arm WITHOUT ever touching the real
rl_training_data/episodes/ directories used for actual GRPO training.

Both target articles are TRAIN variant articles, so the 4 arms map to presets
{0,1,3,5} (NOT 0-3 -- presets 2 and 4 are archived, see
generate_episode_oracles.py::_ARM_PRESETS). This script hardcodes that mapping
for variant articles; pass --presets to override for no-variant articles.

Usage (from research_agent_local/):
  python3 training/setup_noise_experiment.py
  python3 training/setup_noise_experiment.py --articles 09_RAG__var_standard --replicates 5
  python3 training/setup_noise_experiment.py --dry-run
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_NOISE_EXPERIMENT_DIR = _REPO_ROOT / "rl_training_data" / "noise_experiment"

# The two narrowest-margin (non-policy-forced) articles per audit_oracle_margins.py.
_DEFAULT_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]

# Active arm-presets for TRAIN *variant* articles (skip=0, light=1, standard=3, deep=5).
# Mirrors generate_episode_oracles.py::_ARM_PRESETS / _EPISODE_ROUNDS.
_DEFAULT_PRESETS = [0, 1, 3, 5]

_DEFAULT_REPLICATES = 3

_COPY_ITEMS = ["article_guideline.md", "research.md", ".research"]


def _copy_episode_inputs(src: Path, dst: Path, dry_run: bool) -> bool:
    if not src.exists():
        print(f"  SKIP (source missing): {src}", file=sys.stderr)
        return False
    if dst.exists():
        print(f"  SKIP (already set up): {dst}")
        return True

    if dry_run:
        print(f"  WOULD CREATE: {dst}  (from {src.name})")
        return True

    dst.mkdir(parents=True)
    for item in _COPY_ITEMS:
        s = src / item
        if not s.exists():
            print(f"  WARN: {s} missing, skipping this item", file=sys.stderr)
            continue
        d = dst / item
        if s.is_dir():
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    print(f"  CREATED: {dst}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--presets", nargs="+", type=int, default=_DEFAULT_PRESETS)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("=" * 80)
    print("NOISE-MEASUREMENT REPLICATE SETUP")
    print(f"Articles:   {args.articles}")
    print(f"Presets:    {args.presets}  (active arm-presets, not 0-3)")
    print(f"Replicates: {args.replicates}")
    print(f"Source:     {_EPISODES_DIR}")
    print(f"Dest:       {_NOISE_EXPERIMENT_DIR}")
    print("=" * 80)

    replicate_article_names: list[str] = []
    for article in args.articles:
        for r in range(1, args.replicates + 1):
            rep_name = f"{article}__replicate{r}"
            replicate_article_names.append(rep_name)
            for p in args.presets:
                src = _EPISODES_DIR / f"{article}__preset{p}"
                dst = _NOISE_EXPERIMENT_DIR / f"{rep_name}__preset{p}"
                _copy_episode_inputs(src, dst, args.dry_run)

    print()
    print("-" * 80)
    print("NEXT STEPS (from writing_workflow/, real LLM API cost -- confirm before running):")
    print("-" * 80)
    articles_arg = " ".join(replicate_article_names)
    presets_arg = " ".join(str(p) for p in args.presets)
    print(
        "1) Write (temperature 0.25 profile, NOT course.yaml):\n"
        f'   CONFIG_FILE=configs/rl_generation.yaml uv run python rl_writing_generator.py '
        f'--articles {articles_arg} --presets {presets_arg} '
        f'--episodes-dir ../rl_training_data/noise_experiment\n'
    )
    print(
        "2) Grade (ground truth auto-resolved back to the base article, see\n"
        "   rl_grading_generator.py::_strip_replicate_suffix):\n"
        f"   uv run python rl_grading_generator.py --articles {articles_arg} --presets {presets_arg} "
        f"--episodes-dir ../rl_training_data/noise_experiment\n"
    )
    print(
        "3) Measure noise (from research_agent_local/):\n"
        f"   python3 training/measure_replicate_noise.py --articles {' '.join(args.articles)}\n"
    )


if __name__ == "__main__":
    main()
