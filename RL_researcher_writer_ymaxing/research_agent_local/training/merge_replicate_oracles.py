"""Merge replicate write+grade draws back into an averaged per-section reward
label -- A.5's documented "one genuine gap" in the noise-measurement
infrastructure: replicates were only ever MEASURED (measure_replicate_noise.py),
never became a production label.

For each ``(section, arm)`` cell, averages the reward across ALL available
draws for that cell -- the original single production draw already in
``section_oracle.json``, plus every graded replicate found under
``rl_training_data/noise_experiment/<article>__replicateN__preset{p}/`` -- and
writes the result to a NEW, separate file:

    rl_training_data/bases/<article>/section_oracle_averaged.json

The production ``section_oracle.json`` (single draw) is NEVER modified by this
script -- per A.5's design decision, the single-draw path must stay
reproducible (this investigation has relied on diffing against it repeatedly,
e.g. run13_rl_grok_pipeline_analysis.md §60.6). Also written per section: the
per-arm reward sd across draws and the draw count actually used -- this is
exactly the per-label confidence signal A.8's proposed
``--section-weight confidence`` mode needs, computed here for free since the
draws are already loaded.

IMPORTANT -- temperature must match production (2026-07-30 finding, analysis md
§A.7.1): replicate draws MUST be generated at temperature 0.7 (``course.yaml``),
the same profile that generated GT and every original production episode. The
lower-temperature profile (``rl_generation.yaml``, 0.25) was found to be a
CONFIRMED SYSTEMATIC BIAS against `standard`/`deep` (not just lower noise) --
averaging 0.25 draws into a production label would silently corrupt the
deep-vs-standard decision GRPO is trained to make. This script does not (cannot)
verify a replicate directory's generation temperature -- that is the caller's
responsibility. The 2 currently-existing ``noise_experiment/`` datasets
(09_RAG__var_standard, 06_tools__var_standard) are known to be 0.25 and should
be treated as a code-path validation fixture only, NOT a production merge,
until they are regenerated at 0.7.

Usage (from research_agent_local/):
  python3 training/merge_replicate_oracles.py
  python3 training/merge_replicate_oracles.py --articles 09_RAG__var_standard --replicates 3
  python3 training/merge_replicate_oracles.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import measure_replicate_noise as mrn  # noqa: E402

_BASES_DIR = mrn._BASES_DIR
_NOISE_EXPERIMENT_DIR = mrn._NOISE_EXPERIMENT_DIR
_ARM_ORDER = mrn._ARM_ORDER
_ARM_PRESETS_FLAT = mrn._ARM_PRESETS_FLAT
_arm_presets_flat_for = mrn._arm_presets_flat_for  # TRAIN {0,1,3,5} vs TEST {0,1,2,3}

_DEFAULT_ARTICLES = mrn._DEFAULT_ARTICLES
_DEFAULT_REPLICATES = mrn._DEFAULT_REPLICATES


def _discover_replicates(article: str, max_replicates: int) -> list[int]:
    """Return the 1-based replicate indices that actually have graded data on disk."""
    found = []
    presets = _arm_presets_flat_for(article)
    for r in range(1, max_replicates + 1):
        if any((_NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}__preset{p}" / "reasoning.json").exists()
               for p in presets):
            found.append(r)
    return found


def merge_article(article: str, max_replicates: int, dry_run: bool, cost_formula: str = "c2") -> bool:
    section_oracle_path = _BASES_DIR / article / "section_oracle.json"
    if not section_oracle_path.exists():
        print(f"  SKIP {article}: no production section_oracle.json", file=sys.stderr)
        return False

    orig_oracle = json.loads(section_oracle_path.read_text(encoding="utf-8"))
    sec_ids = list(orig_oracle["sections"].keys())

    # Replicate rewards MUST be computed over production's own digest-ordered id list
    # (duplicates included) or the ordinal fallback in _get_score lands on a different
    # entry than production used -- silently averaging apples with oranges for ~9% of
    # cells. See measure_replicate_noise._production_sec_ids / analysis md A.15.4.
    prod_sec_ids = mrn._production_sec_ids(article)
    if not prod_sec_ids or not set(sec_ids).issubset(set(prod_sec_ids)):
        print(f"  WARN {article}: digest sec_ids missing/incomplete, falling back to "
              f"oracle key order (ordinal fallback may diverge from production)", file=sys.stderr)
        prod_sec_ids = sec_ids

    replicate_ids = _discover_replicates(article, max_replicates)
    if not replicate_ids:
        print(f"  SKIP {article}: no graded replicates found under {_NOISE_EXPERIMENT_DIR}", file=sys.stderr)
        return False

    # draws[sec_id][arm] = [production_draw, replicate_draw_1, replicate_draw_2, ...]
    draws: dict[str, dict[str, list[float]]] = {
        sid: {a: [float(orig_oracle["sections"][sid]["rewards"][a])] for a in _ARM_ORDER}
        for sid in sec_ids
    }
    # explore_draws mirrors draws but for the v4+ "explore" sub-component (needed so
    # compute_article_oracle.py::_compute_r_w() applies Candidate E's simple-mean-explore
    # aggregation to the averaged output identically to production section_oracle.json --
    # see run13_rl_grok_pipeline_analysis.md A.15.4 follow-up, 2026-08-20).
    explore_draws: dict[str, dict[str, list[float]]] = {
        sid: {a: [float(orig_oracle["sections"][sid]["explore"][a])] for a in _ARM_ORDER}
        for sid in sec_ids
    }
    for r in replicate_ids:
        prefix = _NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}"
        sections = mrn._compute_replicate_sections(article, prefix, prod_sec_ids, cost_formula=cost_formula)
        for sid in sec_ids:
            for a in _ARM_ORDER:
                draws[sid][a].append(float(sections[sid]["rewards"][a]))
                explore_draws[sid][a].append(float(sections[sid]["explore"][a]))

    merged_sections: dict[str, dict] = {}
    for sid in sec_ids:
        arm_mean: dict[str, float] = {}
        arm_sd: dict[str, float] = {}
        arm_n: dict[str, int] = {}
        arm_explore_mean: dict[str, float] = {}
        for a in _ARM_ORDER:
            vals = draws[sid][a]
            arm_mean[a] = statistics.mean(vals)
            arm_sd[a] = statistics.stdev(vals) if len(set(vals)) > 1 else 0.0
            arm_n[a] = len(vals)
            arm_explore_mean[a] = statistics.mean(explore_draws[sid][a])
        oracle = max(_ARM_ORDER, key=arm_mean.__getitem__)
        merged_sections[sid] = {
            "oracle": oracle,
            "rewards": {a: round(arm_mean[a], 6) for a in _ARM_ORDER},
            "reward_sd": {a: round(arm_sd[a], 6) for a in _ARM_ORDER},
            "n_draws": arm_n,
            "explore": {a: round(arm_explore_mean[a], 6) for a in _ARM_ORDER},
        }

    dist: dict[str, int] = {}
    for info in merged_sections.values():
        dist[info["oracle"]] = dist.get(info["oracle"], 0) + 1
    flips = sum(
        1 for sid in sec_ids
        if merged_sections[sid]["oracle"] != orig_oracle["sections"][sid]["oracle"]
    )
    print(f"  {article}: {len(sec_ids)} sections, {1 + len(replicate_ids)} draws/arm "
          f"(1 production + {len(replicate_ids)} replicate(s) {replicate_ids})  "
          f"oracle dist: {dist}  section-oracle flips vs single-draw: {flips}/{len(sec_ids)}")

    if dry_run:
        return True

    output = {
        "version": 1,
        "merge_source": "single-draw section_oracle.json (production) + "
                         "noise_experiment replicates via measure_replicate_noise.py's recompute path",
        "article": orig_oracle["article"],
        "variant": orig_oracle["variant"],
        "n_draws_per_arm": 1 + len(replicate_ids),
        "replicate_ids_used": replicate_ids,
        "sections": merged_sections,
        # Legacy 'presets' field, mirrors generate_episode_oracles.py's convention.
        "presets": {sid: info["oracle"] for sid, info in merged_sections.items()},
    }
    out_path = _BASES_DIR / article / "section_oracle_averaged.json"
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"    -> wrote {out_path}  (production section_oracle.json untouched)")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES,
                         help="Max replicate index to look for; missing ones are skipped, not required.")
    parser.add_argument("--target-n", type=int, default=None,
                         help="Total draws INCLUDING the production one; overrides --replicates as target_n - 1.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--cost-formula", choices=["c2", "design_c"], default="c2",
                         help="Reward cost mechanism -- see generate_episode_oracles.py::_DESIGN_C_COST.")
    parser.add_argument("--bases-dir", type=Path, default=None,
                         help="Override the bases root (default: production rl_training_data/bases/). "
                              "Must match generate_episode_oracles.py's --bases-dir for the same experiment.")
    args = parser.parse_args()
    if args.target_n is not None:
        args.replicates = args.target_n - 1

    if args.bases_dir is not None:
        global _BASES_DIR
        _BASES_DIR = args.bases_dir
        mrn._BASES_DIR = args.bases_dir  # _compute_replicate_sections/_production_sec_ids read mrn's own copy

    print("=" * 80)
    print("MERGE-BACK: averaging replicate draws into section_oracle_averaged.json")
    print(f"Articles:   {args.articles}")
    print(f"Max replicates checked per article: {args.replicates}")
    print("Output:     bases/<article>/section_oracle_averaged.json "
          "(single-draw section_oracle.json is never modified)")
    print("WARNING: this script does not verify replicate generation temperature.")
    print("Per analysis md §A.7.1, replicates MUST be temperature 0.7 (course.yaml), matching")
    print("production/GT -- NOT 0.25 (rl_generation.yaml), a confirmed systematic bias against")
    print("standard/deep. The 2 default articles' existing noise_experiment/ data is 0.25 and is")
    print("a known-confounded fixture -- treat any merge of it as a code-path check, not production.")
    print("=" * 80)

    ok = 0
    for article in args.articles:
        if merge_article(article, args.replicates, args.dry_run, cost_formula=args.cost_formula):
            ok += 1
    print()
    print(f"Done: {ok}/{len(args.articles)} article(s) merged.")
    return 0 if ok == len(args.articles) else 1


if __name__ == "__main__":
    raise SystemExit(main())
