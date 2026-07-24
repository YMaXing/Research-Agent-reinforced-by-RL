"""Sweep candidate reward-formula variants across already-graded articles, at
ZERO re-grading cost.

Purpose: answer "what would article X's oracle/margin look like under a
different cost_coef / explore_mult / quality-weight / credit-curve?" by
recomputing purely from already-parsed reasoning.json data (same source
generate_episode_oracles.py reads). Never writes section_oracle.json or
article_oracle.json -- this is a read-only exploration tool, not a
replacement for the real pipeline. See run13_rl_grok_pipeline_analysis.md
Part 5 (sections 25-33) for the background this tool exists to support.

Each variant overrides zero or more of:
  cost_coef      float  -- per-round cost, default -0.06 (current production)
  explore_mult   float  -- overall explore-term scale, default 0.50
  quality_weight dict   -- {"strong": w, "standard": w}, default {1.0, 0.65}
  instance_cap   int    -- max instances credited, default 3
  credit_curve   dict   -- {int: float} tiered ladder OR
  exp_k          float  -- if set, use smooth credit(n)=1-(1-exp_k)**n instead
                           of credit_curve (mutually exclusive with credit_curve)

Usage (from research_agent_local/):
  python3 training/sweep_reward_formula.py
  python3 training/sweep_reward_formula.py --articles 09_RAG__var_standard
  python3 training/sweep_reward_formula.py --variants baseline explore_065

Output is both printed to stdout AND written to a timestamped .txt file under
_OUTPUT_DIR (research_agent_local/training/reward_grid_test_results/) by
default -- override with --output-dir, or suppress the file with --no-file.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import compute_article_oracle as cao  # noqa: E402
import generate_episode_oracles as geo  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent
_OUTPUT_DIR = _THIS_DIR / "reward_grid_test_results"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

_DEFAULT_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]

# Current production defaults (must mirror enhancement_reward.py / generate_episode_oracles.py
# exactly, so "baseline" reproduces the real pipeline's numbers as a sanity check).
_PROD_COST_COEF = -0.06
_PROD_EXPLORE_MULT = 0.50
_PROD_QUALITY_WEIGHT = {"strong": 1.00, "standard": 0.65}
_PROD_INSTANCE_CAP = 3
_PROD_CREDIT_CURVE = {0: 0.00, 1: 0.55, 2: 0.80, 3: 1.00}

# ---------------------------------------------------------------------------
# Named candidate variants -- edit/add freely, nothing here requires re-grading
# ---------------------------------------------------------------------------
VARIANTS: dict[str, dict] = {
    "baseline": {},
    # --- Controls: candidates A/B (cap/ladder extension), already shown in
    # run13_rl_grok_pipeline_analysis.md Part 5 §34 to BACKFIRE on both
    # re-graded articles (lowers `deep`'s reward instead of raising it). Kept
    # here purely as a regression check -- if a future re-graded article
    # reverses this finding (many sections genuinely exceeding 3 instances),
    # that would be a signal worth revisiting; otherwise expect these to keep
    # underperforming baseline.
    "control_A_extended_ladder_cap5": {
        "instance_cap": 5,
        "credit_curve": {0: 0.00, 1: 0.55, 2: 0.80, 3: 0.93, 4: 0.98, 5: 1.00},
    },
    "control_B_smooth_exp_k055_cap8": {
        "instance_cap": 8,
        "exp_k": 0.55,
    },
}

# ---------------------------------------------------------------------------
# Systematic grid: candidate C (standard-tier quality weight) x candidate D
# (explore multiplier) -- the two levers that did NOT backfire in §34, cross
# producted since their interaction hasn't been tested and §34 already found
# these two kinds of levers do NOT combine additively (see cap5_plus_explore_065
# below). 5 x 4 = 20 combinations, run on every requested article at zero
# re-grading cost. (0.50, 0.65) reproduces baseline exactly -- a built-in
# sanity check that the grid-generation code is correct.
# ---------------------------------------------------------------------------
_EXPLORE_MULT_GRID = [0.50, 0.60, 0.70, 0.80, 0.90]
_STANDARD_WEIGHT_GRID = [0.65, 0.75, 0.85, 0.95]


def _build_grid_variants() -> dict[str, dict]:
    grid: dict[str, dict] = {}
    for em in _EXPLORE_MULT_GRID:
        for sw in _STANDARD_WEIGHT_GRID:
            name = f"grid_explore{em:.2f}_stdw{sw:.2f}"
            cfg: dict = {}
            if em != _PROD_EXPLORE_MULT:
                cfg["explore_mult"] = em
            if sw != _PROD_QUALITY_WEIGHT["standard"]:
                cfg["quality_weight"] = {"strong": 1.00, "standard": sw}
            grid[name] = cfg
    return grid


VARIANTS.update(_build_grid_variants())

# --- Single-lever reference points at the EXACT values used in §32/§34's
# earlier writeup (0.65, 0.80, 0.80) -- intentionally standalone entries, NOT
# aliased to grid cells, since the grid's spacing (0.60/0.70/0.80/0.90) does
# not include 0.65 and would silently mismatch the documented prior results.
VARIANTS["D_only_explore_065"] = {"explore_mult": 0.65}
VARIANTS["D_only_explore_080"] = {"explore_mult": 0.80}
VARIANTS["C_only_stdw_080"] = {"quality_weight": {"strong": 1.00, "standard": 0.80}}

# Reference: A (backfiring control) combined with D, already shown in §34 to
# partially cancel D's benefit -- kept for contrast against the C x D grid
# above, which does not exhibit this cancellation.
VARIANTS["control_A_plus_explore_065"] = {
    "instance_cap": 5,
    "credit_curve": {0: 0.00, 1: 0.55, 2: 0.80, 3: 0.93, 4: 0.98, 5: 1.00},
    "explore_mult": 0.65,
}


def _credit(qualities: list[str], cfg: dict) -> float:
    """Compute enhancement credit for one section under a variant config.

    Mirrors enhancement_reward.enhancement_credit()'s sort-then-cap logic, but
    parameterised so every constant is swappable per variant, and supports an
    optional smooth exponential curve (exp_k) as an alternative to the tiered
    credit_curve dict.
    """
    if not qualities:
        return 0.0
    quality_weight = cfg.get("quality_weight", _PROD_QUALITY_WEIGHT)
    instance_cap = cfg.get("instance_cap", _PROD_INSTANCE_CAP)
    default_w = quality_weight.get("standard", 0.65)

    weights = sorted((quality_weight.get(q, default_w) for q in qualities), reverse=True)
    weighted = sum(weights[:instance_cap])
    weighted = min(weighted, float(instance_cap))

    exp_k = cfg.get("exp_k")
    if exp_k is not None:
        return round(1.0 - (1.0 - exp_k) ** weighted, 6)

    credit_curve = cfg.get("credit_curve", _PROD_CREDIT_CURVE)
    lo = int(weighted)
    hi = min(lo + 1, instance_cap)
    frac = weighted - lo
    lo_credit = credit_curve.get(lo, credit_curve[max(credit_curve)])
    hi_credit = credit_curve.get(hi, credit_curve[max(credit_curve)])
    return round(lo_credit + frac * (hi_credit - lo_credit), 6)


def _recompute_from_episode_dims(
    episode_dims: dict[int, dict],
    sec_ids: list[str],
    sec_norms: list[str],
    features: dict,
    cfg: dict,
) -> tuple[str, float, dict[str, float]]:
    """Core per-section/per-arm recompute, parameterised over cfg, shared by
    both the ORIGINAL production episode path and the replicate (noise_experiment)
    path -- so both sides of any majority-vote comparison use the identical
    formula for a given cfg. See _recompute() (production episodes) and
    _recompute_replicate() (temp=0.25 replicates) for the two callers.
    """
    cost_coef = cfg.get("cost_coef", _PROD_COST_COEF)
    explore_mult = cfg.get("explore_mult", _PROD_EXPLORE_MULT)

    sections_output: dict[str, dict] = {}
    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        preset_rewards: dict[int, float] = {}
        for p, nr in geo._EPISODE_ROUNDS.items():
            ep = episode_dims.get(p, {})

            def _score(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                return geo._get_score(_ep.get(dim, []), _sn, _si)

            def _enh(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                e = geo._get_enhancement(_ep.get(dim, []), _sn, _si)
                if e is None:
                    return _score(dim)  # legacy fallback, same as production
                return _credit(e[1], cfg)

            cc = _score("ground_truth_core_content")
            fl = _score("ground_truth_flow")
            de = _enh("ground_truth_depth_enhancement")
            be = _enh("ground_truth_breadth_enhancement")
            cp = _score("ground_truth_core_preservation")
            ga = _score("user_intent_guideline_adherence")
            ra = _score("user_intent_research_anchoring")

            gt_base = 0.20 * cc + 0.20 * fl
            explore = cp * (0.60 * de + 0.40 * be) * explore_mult
            user_intent = (0.50 * ga + 0.50 * ra) * 0.30
            cost = cost_coef * nr
            preset_rewards[p] = gt_base + explore + user_intent + cost

        arm_rewards = {arm: preset_rewards[geo._ARM_PRESETS[arm][0]] for arm in geo._ARM_ORDER}
        sections_output[sec_id] = {
            "oracle": max(geo._ARM_ORDER, key=arm_rewards.__getitem__),
            "rewards": arm_rewards,
        }

    r_w, _total_w, _n, _n_with_target = cao._compute_r_w(sections_output, features)
    ranked = sorted(cao.ARMS, key=lambda a: r_w[a], reverse=True)
    margin = r_w[ranked[0]] - r_w[ranked[1]]
    return ranked[0], margin, r_w


def _load_article_context(article_var: str) -> tuple[list[str], list[str], dict]:
    bases_dir = _BASES_DIR / article_var
    digest = (bases_dir / "research_digest.md").read_text(encoding="utf-8")
    sec_ids = geo._extract_sec_ids_ordered(digest)
    sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]
    features = json.loads((bases_dir / "guideline_features.json").read_text(encoding="utf-8"))["sections"]
    return sec_ids, sec_norms, features


def _recompute(article_var: str, cfg: dict) -> tuple[str, float, dict[str, float]]:
    """Recompute an article's R_w/oracle/margin under a variant config.

    Reads the SAME already-graded reasoning.json files generate_episode_oracles.py
    reads; writes nothing. Uses raw argmax for the oracle pick (does not
    replicate compute_article_oracle.py's secondary near-tie signals S3/S4/S5,
    which need actual article-text analysis) -- fine for sensitivity sweeps,
    since the goal is comparing R_w/margin shifts across variants, not
    reproducing the exact production near-tie tie-break.
    """
    sec_ids, sec_norms, features = _load_article_context(article_var)
    episode_dims = {p: geo._load_episode(_EPISODES_DIR / f"{article_var}__preset{p}") for p in geo._EPISODE_ROUNDS}
    return _recompute_from_episode_dims(episode_dims, sec_ids, sec_norms, features, cfg)


_NOISE_EXPERIMENT_DIR = _REPO_ROOT / "rl_training_data" / "noise_experiment"


def _recompute_replicate(article_var: str, replicate_n: int, cfg: dict) -> tuple[str, float, dict[str, float]] | None:
    """Same as _recompute(), but for one temp=0.25 noise-experiment replicate.

    Returns None if the replicate's episodes aren't graded yet. Uses the SAME
    _recompute_from_episode_dims() core as the production-episode path, so a
    given cfg is applied identically to both -- required for a valid
    majority-vote comparison across (original + replicates) at any explore_mult/
    quality_weight/etc. setting, not just the production default.
    """
    prefix = _NOISE_EXPERIMENT_DIR / f"{article_var}__replicate{replicate_n}"
    if not any((_NOISE_EXPERIMENT_DIR / f"{article_var}__replicate{replicate_n}__preset{p}" / "reasoning.json").exists()
               for p in geo._EPISODE_ROUNDS):
        return None
    sec_ids, sec_norms, features = _load_article_context(article_var)
    episode_dims = {p: geo._load_episode(Path(f"{prefix}__preset{p}")) for p in geo._EPISODE_ROUNDS}
    return _recompute_from_episode_dims(episode_dims, sec_ids, sec_norms, features, cfg)


_MAJORITY_VOTE_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]
_MAJORITY_VOTE_EXPLORE_GRID = [0.50, 0.60, 0.65, 0.70, 0.80, 0.90]


def majority_vote_sweep(article_var: str, explore_mults: list[float], emit) -> None:
    """For each explore_mult value, recompute the ORIGINAL production episode
    AND all 3 temp=0.25 replicates under the IDENTICAL cfg, then take a
    majority vote across the 4 independent draws.

    This is the non-circular way to test whether raising explore_mult
    overturns a replicate-confirmed label: instead of asking "does grid cell X
    disagree with the single baseline-formula label" (which begs the question
    of whether the baseline formula's own label is correct), this asks "does
    the MAJORITY of independent draws (different temp=0.25 writing samples)
    still support the same arm once every draw is recomputed under the SAME
    candidate cfg". If the majority stays stable across the explore_mult
    range, that's real evidence the label is robust to this lever. If the
    majority itself shifts, that's evidence the lever reveals something the
    single-draw comparison couldn't -- not just an artifact of trusting one
    formula's label as ground truth for judging changes to that formula.
    """
    for explore_mult in explore_mults:
        cfg = {} if explore_mult == _PROD_EXPLORE_MULT else {"explore_mult": explore_mult}
        draws: list[tuple[str, float]] = []
        orig_arm, orig_margin, _ = _recompute(article_var, cfg)
        draws.append((orig_arm, orig_margin))
        for r in (1, 2, 3):
            result = _recompute_replicate(article_var, r, cfg)
            if result is not None:
                arm, margin, _ = result
                draws.append((arm, margin))
        votes: dict[str, int] = {}
        for arm, _m in draws:
            votes[arm] = votes.get(arm, 0) + 1
        majority_arm = max(votes, key=votes.__getitem__)
        n_majority = votes[majority_arm]
        tie = sum(1 for v in votes.values() if v == n_majority) > 1
        votes_str = ", ".join(f"{a}={n}" for a, n in sorted(votes.items(), key=lambda kv: -kv[1]))
        draws_str = "  ".join(f"{a}({m:+.3f})" for a, m in draws)
        tie_flag = " [TIE]" if tie else ""
        emit(f"  explore_mult={explore_mult:.2f}  majority={majority_arm:<8}{tie_flag}  votes=[{votes_str}]  draws=[{draws_str}]")


def _recompute_any(article_dir_name: str, cfg: dict) -> tuple[str, float, dict[str, float]] | None:
    """Same as _recompute(), but works for ANY already-graded bases/ directory,
    not just the 2 hardcoded default (re-graded, tagged) articles -- TRAIN
    variant articles (dir name contains "__var_", uses episodes/ +
    _EPISODE_ROUNDS/_ARM_PRESETS) AND TEST/no-variant/augmented articles (no
    "__var_" in the name, e.g. "13_agent_framework" or "Insects_Consciousness__mixeddepth",
    uses test_episodes/ + _TEST_EPISODE_ROUNDS/_TEST_ARM_PRESETS, sequential
    preset ids 0-3, per generate_episode_oracles.py's own no_variant branch).

    NOTE on what this can and cannot test for un-tagged (not-yet-re-graded)
    articles: quality_weight/instance_cap/credit_curve/exp_k have ZERO effect
    on them (legacy reasoning.json has no [instances=N;...] tag, so _enh()
    bypasses _credit() entirely and returns the raw binary score, same as
    production). Only cost_coef/explore_mult have any effect on untagged
    articles, since those multiply the whole term regardless of tag presence.
    This is exactly why a corpus-wide sweep can meaningfully test explore_mult
    sensitivity today, but cannot meaningfully test quality_weight/instance_cap
    beyond the 2 already re-graded articles.

    Returns None if the bases dir or its research_digest.md is missing.
    """
    bases_dir = _BASES_DIR / article_dir_name
    digest_path = bases_dir / "research_digest.md"
    features_path = bases_dir / "guideline_features.json"
    if not (digest_path.exists() and features_path.exists()):
        return None
    digest = digest_path.read_text(encoding="utf-8")
    sec_ids = geo._extract_sec_ids_ordered(digest)
    sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]
    features = json.loads(features_path.read_text(encoding="utf-8"))["sections"]

    no_variant = "__var_" not in article_dir_name
    if no_variant:
        ep_rounds = geo._TEST_EPISODE_ROUNDS
        episodes_dir = _TEST_EPISODES_DIR
        # no_variant episodes are named "<base_article>__preset<N>" (plain base
        # name, matching generate_episode_oracles.py's own no_variant branch) --
        # article_dir_name itself may already carry a "__mixeddepth"-style
        # augmentation suffix, which IS part of the episode dir name too (the
        # pilots' episodes were generated under that exact augmented name).
        episode_prefix = article_dir_name
    else:
        ep_rounds = geo._EPISODE_ROUNDS
        episodes_dir = _EPISODES_DIR
        episode_prefix = article_dir_name

    episode_dims = {p: geo._load_episode(episodes_dir / f"{episode_prefix}__preset{p}") for p in ep_rounds}
    arm_presets = geo._TEST_ARM_PRESETS if no_variant else geo._ARM_PRESETS
    return _recompute_core(episode_dims, ep_rounds, arm_presets, sec_ids, sec_norms, features, cfg)


def _recompute_core(
    episode_dims: dict[int, dict],
    ep_rounds: dict[int, int],
    arm_presets: dict[str, list[int]],
    sec_ids: list[str],
    sec_norms: list[str],
    features: dict,
    cfg: dict,
) -> tuple[str, float, dict[str, float]]:
    """Fully generic version of _recompute_from_episode_dims, parameterised
    over the preset/round/arm mapping too (not just hardcoded to the TRAIN
    variant convention) -- needed because TEST/no-variant articles use a
    DIFFERENT preset-id space (0-3, sequential) than TRAIN variants (0/1/3/5,
    presets 2/4 archived). See generate_episode_oracles.py's own no_variant
    branch for the source of truth this mirrors.
    """
    cost_coef = cfg.get("cost_coef", _PROD_COST_COEF)
    explore_mult = cfg.get("explore_mult", _PROD_EXPLORE_MULT)

    sections_output: dict[str, dict] = {}
    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        preset_rewards: dict[int, float] = {}
        for p, nr in ep_rounds.items():
            ep = episode_dims.get(p, {})

            def _score(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                return geo._get_score(_ep.get(dim, []), _sn, _si)

            def _enh(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                e = geo._get_enhancement(_ep.get(dim, []), _sn, _si)
                if e is None:
                    return _score(dim)
                return _credit(e[1], cfg)

            cc = _score("ground_truth_core_content")
            fl = _score("ground_truth_flow")
            de = _enh("ground_truth_depth_enhancement")
            be = _enh("ground_truth_breadth_enhancement")
            cp = _score("ground_truth_core_preservation")
            ga = _score("user_intent_guideline_adherence")
            ra = _score("user_intent_research_anchoring")

            gt_base = 0.20 * cc + 0.20 * fl
            explore = cp * (0.60 * de + 0.40 * be) * explore_mult
            user_intent = (0.50 * ga + 0.50 * ra) * 0.30
            cost = cost_coef * nr
            preset_rewards[p] = gt_base + explore + user_intent + cost

        arm_rewards = {arm: preset_rewards[preset_ids[0]] for arm, preset_ids in arm_presets.items()}
        sections_output[sec_id] = {
            "oracle": max(geo._ARM_ORDER, key=arm_rewards.__getitem__),
            "rewards": arm_rewards,
        }

    r_w, _total_w, _n, _n_with_target = cao._compute_r_w(sections_output, features)
    ranked = sorted(cao.ARMS, key=lambda a: r_w[a], reverse=True)
    margin = r_w[ranked[0]] - r_w[ranked[1]]
    return ranked[0], margin, r_w


def corpus_explore_mult_sweep(explore_mults: list[float], emit) -> None:
    """Corpus-wide, zero-re-grading-cost explore_mult sensitivity sweep across
    EVERY already-graded article-variant dir under _BASES_DIR (TRAIN + TEST +
    augmented pilots) -- addresses "test more articles" directly, for the one
    lever (explore_mult) that has an effect on un-tagged/legacy data too.

    Purely DESCRIPTIVE: reports how many raw-argmax picks flip vs baseline at
    each explore_mult value, and which specific articles flip. This is NOT a
    correctness judgment (we don't have ground truth for most of these
    articles) -- it answers "how big a lever is this, in aggregate, across the
    corpus" (blast-radius), a different and non-circular question from
    "does the flip match a formula-dependent label".
    """
    article_dirs = sorted(
        d.name for d in _BASES_DIR.iterdir()
        if d.is_dir() and (d / "article_oracle.json").exists()
    )
    baseline_results: dict[str, tuple[str, float]] = {}
    baseline_orig_margin: dict[str, float] = {}
    for name in article_dirs:
        result = _recompute_any(name, {})
        if result is None:
            continue
        arm, margin, _ = result
        baseline_results[name] = (arm, margin)
        try:
            orig = json.loads((_BASES_DIR / name / "article_oracle.json").read_text(encoding="utf-8"))
            baseline_orig_margin[name] = orig.get("margin", margin)
        except (OSError, json.JSONDecodeError):
            baseline_orig_margin[name] = margin

    emit(f"  Corpus size (already-graded, recomputable): {len(baseline_results)} article-variant dirs")
    emit()
    for explore_mult in explore_mults:
        cfg = {} if explore_mult == _PROD_EXPLORE_MULT else {"explore_mult": explore_mult}
        flips = []
        for name, (base_arm, _base_margin) in baseline_results.items():
            result = _recompute_any(name, cfg)
            if result is None:
                continue
            new_arm, new_margin, _ = result
            if new_arm != base_arm:
                flips.append((name, base_arm, new_arm, baseline_orig_margin[name]))
        thin = [f for f in flips if abs(f[3]) < 0.06]
        comfortable = [f for f in flips if abs(f[3]) >= 0.06]
        emit(f"  explore_mult={explore_mult:.2f}  flips={len(flips)}/{len(baseline_results)}  "
             f"(thin-margin<0.06: {len(thin)}, comfortable-margin>=0.06: {len(comfortable)})")
        for name, old_arm, new_arm, orig_margin in flips:
            tag = "COMFORTABLE" if abs(orig_margin) >= 0.06 else "thin"
            emit(f"      {name:<45} {old_arm:<8} -> {new_arm:<8} (orig_margin={orig_margin:+.4f}, {tag})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--variants", nargs="+", default=list(VARIANTS.keys()), choices=list(VARIANTS.keys()))
    parser.add_argument(
        "--output-dir",
        default=str(_OUTPUT_DIR),
        help=f"Directory to write a timestamped results .txt file into (default: {_OUTPUT_DIR})",
    )
    parser.add_argument("--no-file", action="store_true", help="Only print to stdout, skip writing a results file")
    parser.add_argument(
        "--majority-vote-sweep",
        action="store_true",
        help="Instead of the per-variant table, sweep explore_mult and recompute the "
             "(original + 3 replicates) majority vote at each value, for the "
             "articles with noise-experiment replicate data (09_RAG/06_tools __var_standard).",
    )
    parser.add_argument(
        "--corpus-sweep",
        action="store_true",
        help="Corpus-wide explore_mult sensitivity sweep across EVERY already-graded "
             "bases/ dir (TRAIN+TEST+augmented) -- reports raw-argmax flip counts vs "
             "baseline at each explore_mult value. Zero re-grading cost.",
    )
    parser.add_argument(
        "--corpus-explore-grid",
        nargs="+",
        type=float,
        default=_EXPLORE_MULT_GRID,
        help="explore_mult values to test in --corpus-sweep mode.",
    )
    args = parser.parse_args()

    lines: list[str] = []

    def emit(line: str = "") -> None:
        print(line)
        lines.append(line)

    if args.corpus_sweep:
        emit("=" * 100)
        emit("CORPUS-WIDE EXPLORE_MULT SENSITIVITY SWEEP (all already-graded articles)")
        emit("=" * 100)
        corpus_explore_mult_sweep(args.corpus_explore_grid, emit)
        if not args.no_file:
            out_dir = Path(args.output_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_path = out_dir / f"corpus_sweep_{timestamp}.txt"
            out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"\n[written to {out_path}]")
        return

    if args.majority_vote_sweep:
        mv_articles = args.articles if args.articles != _DEFAULT_ARTICLES else _MAJORITY_VOTE_ARTICLES
        for article in mv_articles:
            emit("=" * 100)
            emit(f"MAJORITY-VOTE SWEEP: {article}  (original + 3 replicates, per explore_mult)")
            emit("=" * 100)
            majority_vote_sweep(article, _MAJORITY_VOTE_EXPLORE_GRID, emit)
            emit()
        if not args.no_file:
            out_dir = Path(args.output_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_path = out_dir / f"majority_vote_sweep_{timestamp}.txt"
            out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"\n[written to {out_path}]")
        return

    per_article_results: dict[str, dict[str, tuple[str, float, dict[str, float]]]] = {}

    for article in args.articles:
        emit("=" * 100)
        emit(f"ARTICLE: {article}")
        emit("=" * 100)
        results: dict[str, tuple[str, float, dict[str, float]]] = {}
        for variant_name in args.variants:
            cfg = VARIANTS[variant_name]
            arm, margin, r_w = _recompute(article, cfg)
            results[variant_name] = (arm, margin, r_w)
            r_w_str = "  ".join(f"{a}:{r_w[a]:.4f}" for a in cao.ARMS)
            emit(f"  {variant_name:<28} raw_argmax={arm:<8} margin={margin:+.4f}  R_w=[{r_w_str}]")
        per_article_results[article] = results
        emit()

    # --- Summary: winner change vs baseline, per article ---
    if "baseline" in args.variants:
        emit("=" * 100)
        emit("SUMMARY: winner/margin change vs baseline")
        emit("=" * 100)
        for article, results in per_article_results.items():
            base_arm, base_margin, _ = results["baseline"]
            emit(f"  {article}  (baseline: {base_arm}, margin={base_margin:+.4f})")
            for variant_name, (arm, margin, _r_w) in results.items():
                if variant_name == "baseline":
                    continue
                changed = " <-- WINNER CHANGED" if arm != base_arm else ""
                emit(f"    {variant_name:<28} {arm:<8} margin={margin:+.4f}  Delta_margin={margin - base_margin:+.4f}{changed}")
        emit()

    # --- Cross-article agreement view: which grid cells favor the SAME arm
    # in every requested article? A formula change that helps one article but
    # not another is much weaker evidence than one that generalizes. ---
    grid_names = [v for v in args.variants if v.startswith("grid_")]
    if len(grid_names) >= 2 and len(per_article_results) >= 2:
        emit("=" * 100)
        emit("CROSS-ARTICLE AGREEMENT (grid_* variants only)")
        emit("=" * 100)
        for variant_name in grid_names:
            winners = {article: results[variant_name][0] for article, results in per_article_results.items()}
            distinct = set(winners.values())
            agree = "AGREE" if len(distinct) == 1 else "disagree"
            winners_str = "  ".join(f"{a}={w}" for a, w in winners.items())
            emit(f"  {variant_name:<28} [{agree}]  {winners_str}")
        emit()

    if not args.no_file:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = out_dir / f"sweep_{timestamp}.txt"
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\n[written to {out_path}]")


if __name__ == "__main__":
    main()
