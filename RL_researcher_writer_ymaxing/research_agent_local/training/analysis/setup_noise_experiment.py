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

For the 16 no-variant TEST articles (production episodes live under
rl_training_data/test_episodes/, not episodes/, and use presets 0-3 directly --
see generate_episode_oracles.py::_TEST_ARM_PRESETS), pass --test to source from
test_episodes/ instead; --presets then defaults to 0 1 2 3 automatically.

EXPANDING an already-replicated set of articles (e.g. analysis md A.15.3's N=3->N=5
targeted expansion): re-run with the SAME --articles list and a HIGHER --target-n
(total draws including the production one) or --replicates (additional draws only,
--target-n minus 1). Already-created replicate dirs are detected and skipped
(existing per-preset inputs are never touched), so only the new replicate indices are
created -- and the printed NEXT STEPS commands list only those new episode names, so
re-running write/grade doesn't needlessly re-touch already-graded replicate1/replicate2.

Usage (from research_agent_local/):
  python3 training/setup_noise_experiment.py
  python3 training/setup_noise_experiment.py --articles 09_RAG__var_standard --replicates 5
  python3 training/setup_noise_experiment.py --test --articles HNSW Dark_Dimension --replicates 2
  python3 training/setup_noise_experiment.py --articles 03_context_engineering__var_standard \
      08_react_practice__var_standard 09_RAG__var_standard --target-n 5   # N=3 -> N=5 expansion
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
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"
_NOISE_EXPERIMENT_DIR = _REPO_ROOT / "rl_training_data" / "noise_experiment"

# The two narrowest-margin (non-policy-forced) articles per audit_oracle_margins.py.
_DEFAULT_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]

# Active arm-presets for TRAIN *variant* articles (skip=0, light=1, standard=3, deep=5).
# Mirrors generate_episode_oracles.py::_ARM_PRESETS / _EPISODE_ROUNDS.
_DEFAULT_PRESETS = [0, 1, 3, 5]

# No-variant TEST articles map arms directly to presets 0-3, see
# generate_episode_oracles.py::_TEST_ARM_PRESETS.
_DEFAULT_TEST_PRESETS = [0, 1, 2, 3]

_DEFAULT_REPLICATES = 3

_COPY_ITEMS = ["article_guideline.md", "research.md", ".research"]

# Status values returned by _copy_episode_inputs -- "created"/"would_create" mean this
# replicate is genuinely new work; "skipped_exists" means a prior run already set it up.
_MISSING_SOURCE, _SKIPPED_EXISTS, _WOULD_CREATE, _CREATED = (
    "missing_source", "skipped_exists", "would_create", "created",
)


def _copy_episode_inputs(src: Path, dst: Path, dry_run: bool) -> str:
    if not src.exists():
        print(f"  SKIP (source missing): {src}", file=sys.stderr)
        return _MISSING_SOURCE
    if dst.exists():
        print(f"  SKIP (already set up): {dst}")
        return _SKIPPED_EXISTS

    if dry_run:
        print(f"  WOULD CREATE: {dst}  (from {src.name})")
        return _WOULD_CREATE

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
    return _CREATED


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--presets", nargs="+", type=int, default=None)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES,
                         help="Number of replicate dirs to ensure exist (ADDITIONAL to the "
                              "production draw). Already-existing replicate dirs are left alone, "
                              "so raising this on a previously-run --articles list only adds the "
                              "missing higher-numbered replicates (an N-expansion, e.g. N=3->N=5 "
                              "is --replicates 2 -> --replicates 4). See --target-n for the "
                              "total-draws-including-production framing used in the analysis doc.")
    parser.add_argument("--target-n", type=int, default=None,
                         help="Total draws INCLUDING the production one (matches the analysis "
                              "doc's 'N=3'/'N=5' vocabulary). Overrides --replicates as "
                              "target_n - 1 when set.")
    parser.add_argument("--test", action="store_true",
                         help="Source from test_episodes/ (no-variant TEST articles, presets 0-3) "
                              "instead of episodes/ (TRAIN variant articles, presets 0,1,3,5).")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    replicates = args.replicates
    if args.target_n is not None:
        if args.target_n < 2:
            sys.exit(f"--target-n must be >= 2 (1 production draw + at least 1 replicate), got {args.target_n}")
        replicates = args.target_n - 1

    episodes_dir = _TEST_EPISODES_DIR if args.test else _EPISODES_DIR
    presets = args.presets if args.presets is not None else (_DEFAULT_TEST_PRESETS if args.test else _DEFAULT_PRESETS)

    print("=" * 80)
    print("NOISE-MEASUREMENT REPLICATE SETUP")
    print(f"Articles:   {args.articles}")
    print(f"Presets:    {presets}  ({'TEST 0-3' if args.test else 'TRAIN active arm-presets, not 0-3'})")
    print(f"Replicates: {replicates}  (target N={replicates + 1} total draws incl. production)")
    print(f"Source:     {episodes_dir}")
    print(f"Dest:       {_NOISE_EXPERIMENT_DIR}")
    print("=" * 80)

    all_article_names: list[str] = []
    new_article_names: list[str] = []
    for article in args.articles:
        for r in range(1, replicates + 1):
            rep_name = f"{article}__replicate{r}"
            all_article_names.append(rep_name)
            rep_statuses = [
                _copy_episode_inputs(episodes_dir / f"{article}__preset{p}",
                                      _NOISE_EXPERIMENT_DIR / f"{rep_name}__preset{p}", args.dry_run)
                for p in presets
            ]
            if any(s in (_CREATED, _WOULD_CREATE) for s in rep_statuses):
                new_article_names.append(rep_name)

    print()
    if len(new_article_names) < len(all_article_names):
        print(f"{len(all_article_names) - len(new_article_names)} replicate dir(s) already existed "
              f"(from a prior run) and were left untouched -- an N-expansion, not a fresh setup.")
    print("-" * 80)
    print("NEXT STEPS (from writing_workflow/, real LLM API cost -- confirm before running):")
    print("-" * 80)
    if not new_article_names:
        print("Nothing new to write/grade -- all requested replicate dirs already existed.\n")
        return
    articles_arg = " ".join(new_article_names)
    presets_arg = " ".join(str(p) for p in presets)
    print(
        "1) Write (temperature 0.7 -- course.yaml, NO CONFIG_FILE override; matches GT/production,\n"
        "   per §A.7.1: rl_generation.yaml's temp=0.25 is a confirmed systematic bias vs standard/deep):\n"
        f'   uv run python rl_writing_generator.py '
        f'--articles {articles_arg} --presets {presets_arg} '
        f'--episodes-dir ../rl_training_data/noise_experiment\n'
    )
    print(
        "2) Grade (Claude judge, ground truth auto-resolved back to the base article, see\n"
        "   rl_grading_generator.py::_strip_replicate_suffix):\n"
        f"   uv run python rl_grading_generator.py --grading-model claude --articles {articles_arg} "
        f"--presets {presets_arg} --episodes-dir ../rl_training_data/noise_experiment\n"
    )
    print(
        "3) Measure noise across ALL replicates incl. any set up by a prior run (from research_agent_local/):\n"
        f"   python3 training/measure_replicate_noise.py --articles {' '.join(args.articles)} --replicates {replicates}\n"
    )


if __name__ == "__main__":
    main()
