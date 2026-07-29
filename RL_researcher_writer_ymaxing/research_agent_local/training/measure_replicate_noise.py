"""Measure write+grade noise for the narrowest-margin articles via replicate reruns.

Consumes the output of ``setup_noise_experiment.py`` + the writing/grading
generators run against ``rl_training_data/noise_experiment/`` (Part 4 §20 fix #3,
§22's audit-flagged targets). Reuses the SAME reward formula and article-level
weighting as production (imported, not duplicated, per repo convention) from
``generate_episode_oracles.py`` and ``compute_article_oracle.py``.

For each target article:
  - Loads N replicate reasoning.json sets (temperature 0.25, this experiment)
    from rl_training_data/noise_experiment/<article>__replicateR__preset{P}.
  - Computes per-section per-arm rewards for each replicate (same formula as
    production section_oracle.json).
  - Computes the target-words-weighted article-level R_w and margin for each
    replicate (same weighting as production article_oracle.json).
  - Reports: per-section reward std/range across replicates, article-level
    margin std/range across replicates, oracle_arm flip-rate across replicates,
    and a comparison against the ORIGINAL single-draw production run (temperature
    0.7) already on disk in rl_training_data/bases/<article>/section_oracle.json
    + article_oracle.json.

This does NOT write/modify any production file — read-only analysis.

Usage (from research_agent_local/):
  python3 training/measure_replicate_noise.py
  python3 training/measure_replicate_noise.py --articles 09_RAG__var_standard
  python3 training/measure_replicate_noise.py --replicates 3
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import compute_article_oracle as cao  # noqa: E402
import generate_episode_oracles as geo  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_NOISE_EXPERIMENT_DIR = _REPO_ROOT / "rl_training_data" / "noise_experiment"

_DEFAULT_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]
_DEFAULT_REPLICATES = 3

# Active arm-presets for TRAIN variant articles (skip=0, light=1, standard=3, deep=5).
_ARM_PRESETS = geo._ARM_PRESETS
_ARM_ORDER = geo._ARM_ORDER


def _variant_short(article: str) -> str:
    return article.rsplit("__", 1)[-1].replace("var_", "")


def _compute_replicate_sections(article: str, replicate_dir_prefix: Path, sec_ids: list[str]) -> dict[str, dict]:
    """Compute {sec_id: {"oracle": arm, "rewards": {...}}} for one replicate,
    mirroring generate_episode_oracles.py::process_article_variant's inner loop
    -- INCLUDING its enhancement-credit routing (de/be go through
    _get_enhancement()/enhancement_credit() when the [instances=N; quality=...]
    tag is present, falling back to the raw binary score only for untagged/
    legacy reasoning.json). Both the ORIGINAL production episode and these
    replicates were re-graded with the new tag-emitting grader, so both sides
    of the majority-vote comparison must use the identical formula -- this was
    NOT the case before this fix (see run13_rl_grok_pipeline_analysis.md §36).
    """
    variant_short = _variant_short(article)
    sec_norms = [geo._sec_id_to_norm(sid) for sid in sec_ids]
    # preset id -> arm name, so cost uses geo._ARM_COST_UNITS (empirical, H0,
    # shipped 2026-07-25) instead of the stale ordinal _EPISODE_ROUNDS_FLAT --
    # keeps this replicate computation in sync with real production.
    preset_to_arm = {pid: arm for arm, ids in _ARM_PRESETS.items() for pid in ids}

    episode_dims: dict[int, dict] = {}
    for p in _ARM_PRESETS_FLAT:
        ep_dir = Path(f"{replicate_dir_prefix}__preset{p}")
        episode_dims[p] = geo._load_episode(ep_dir) if ep_dir.exists() else {}

    sections_output: dict[str, dict] = {}
    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        preset_rewards: dict[int, float] = {}
        for p in _ARM_PRESETS_FLAT:
            ep = episode_dims[p]
            nr = geo._ARM_COST_UNITS[preset_to_arm[p]]

            def _score(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                return geo._get_score(_ep.get(dim, []), _sn, _si)

            def _enh_credit(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                enh = geo._get_enhancement(_ep.get(dim, []), _sn, _si)
                if enh is None:
                    return geo._get_score(_ep.get(dim, []), _sn, _si)
                _count, qualities = enh
                return geo.enhancement_credit(qualities)

            preset_rewards[p] = geo._section_reward(
                cc=_score("ground_truth_core_content"),
                fl=_score("ground_truth_flow"),
                de=_enh_credit("ground_truth_depth_enhancement"),
                be=_enh_credit("ground_truth_breadth_enhancement"),
                cp=_score("ground_truth_core_preservation"),
                ga=_score("user_intent_guideline_adherence"),
                ra=_score("user_intent_research_anchoring"),
                nr=nr,
                variant=variant_short,
            )

        arm_rewards = {arm: preset_rewards[_ARM_PRESETS[arm][0]] for arm in _ARM_ORDER}
        oracle = max(_ARM_ORDER, key=arm_rewards.__getitem__)
        sections_output[sec_id] = {
            "oracle": oracle,
            "rewards": {k: round(arm_rewards[k], 6) for k in _ARM_ORDER},
        }
    return sections_output


_ARM_PRESETS_FLAT = sorted({p for ps in geo._ARM_PRESETS.values() for p in ps})
_EPISODE_ROUNDS_FLAT = geo._EPISODE_ROUNDS


def _stats(values: list[float]) -> str:
    if len(values) < 2:
        return f"n={len(values)} (need >=2 for std)"
    mu = statistics.mean(values)
    sd = statistics.stdev(values)
    return f"mean={mu:+.4f}  std={sd:.4f}  range=[{min(values):+.4f}, {max(values):+.4f}]"


def measure_article(article: str, n_replicates: int) -> None:
    print("=" * 100)
    print(f"ARTICLE: {article}")
    print("=" * 100)

    section_oracle_path = _BASES_DIR / article / "section_oracle.json"
    features_path = _BASES_DIR / article / "guideline_features.json"
    article_oracle_path = _BASES_DIR / article / "article_oracle.json"
    if not (section_oracle_path.exists() and features_path.exists()):
        print(f"  MISSING production section_oracle.json/guideline_features.json for {article}, skipping.")
        return

    orig_oracle = json.loads(section_oracle_path.read_text(encoding="utf-8"))
    features = json.loads(features_path.read_text(encoding="utf-8"))
    features_sections = features.get("sections", {})
    sec_ids = list(orig_oracle["sections"].keys())

    orig_r_w, total_w, n_sections, _ = cao._compute_r_w(orig_oracle["sections"], features_sections)
    orig_margin = None
    orig_arm = None
    if article_oracle_path.exists():
        orig_article_oracle = json.loads(article_oracle_path.read_text(encoding="utf-8"))
        orig_margin = orig_article_oracle.get("margin")
        orig_arm = orig_article_oracle.get("oracle_arm")

    print(f"  ORIGINAL (temp=0.7, single draw): oracle_arm={orig_arm}  margin={orig_margin}")
    print(f"  ORIGINAL r_w_rewards: {{{', '.join(f'{a}:{orig_r_w[a]:.4f}' for a in _ARM_ORDER)}}}")
    print()

    replicate_r_w: list[dict[str, float]] = []
    replicate_sections: list[dict[str, dict]] = []
    missing = 0
    for r in range(1, n_replicates + 1):
        prefix = _NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}"
        if not any((_NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}__preset{p}" / "reasoning.json").exists()
                   for p in _ARM_PRESETS_FLAT):
            missing += 1
            continue
        sections = _compute_replicate_sections(article, prefix, sec_ids)
        replicate_sections.append(sections)
        r_w, *_ = cao._compute_r_w(sections, features_sections)
        replicate_r_w.append(r_w)

    if not replicate_r_w:
        print(f"  No replicate data found yet under {_NOISE_EXPERIMENT_DIR} "
              f"(run setup_noise_experiment.py + the writing/grading generators first).")
        return
    if missing:
        print(f"  ({missing}/{n_replicates} replicate(s) not yet graded)")

    print(f"  --- {len(replicate_r_w)} replicate(s) (temp=0.25) ---")
    for i, r_w in enumerate(replicate_r_w, start=1):
        ranked = sorted(_ARM_ORDER, key=lambda a: r_w[a], reverse=True)
        margin = r_w[ranked[0]] - r_w[ranked[1]]
        print(f"  replicate {i}: oracle_arm={ranked[0]:<8} margin={margin:+.4f}  "
              f"r_w={{{', '.join(f'{a}:{r_w[a]:.4f}' for a in _ARM_ORDER)}}}")

    print()
    print("  --- Article-level margin across replicates ---")
    margins = []
    arms_picked = []
    for r_w in replicate_r_w:
        ranked = sorted(_ARM_ORDER, key=lambda a: r_w[a], reverse=True)
        margins.append(r_w[ranked[0]] - r_w[ranked[1]])
        arms_picked.append(ranked[0])
    print(f"  margin {_stats(margins)}")
    print(f"  oracle_arm votes: {dict((a, arms_picked.count(a)) for a in set(arms_picked))}")
    if orig_margin is not None:
        print(f"  vs original (temp=0.7) margin={orig_margin:+.4f}, oracle_arm={orig_arm}")

    print()
    print("  --- Per-section reward std across replicates (per arm) ---")
    for sec_id in sec_ids:
        for arm in _ARM_ORDER:
            vals = [s[sec_id]["rewards"][arm] for s in replicate_sections]
            if len(vals) >= 2:
                sd = statistics.stdev(vals)
                if sd > 0.02:  # only print sections/arms with non-trivial spread
                    orig_val = orig_oracle["sections"].get(sec_id, {}).get("rewards", {}).get(arm)
                    print(f"    {sec_id:<45} {arm:<9} {_stats(vals)}  (orig temp=0.7: {orig_val})")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES)
    args = parser.parse_args()

    for article in args.articles:
        measure_article(article, args.replicates)


if __name__ == "__main__":
    main()
