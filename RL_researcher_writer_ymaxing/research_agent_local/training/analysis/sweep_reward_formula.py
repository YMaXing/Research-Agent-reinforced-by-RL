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
  cost_units     dict   -- {arm_name: float} overrides the per-arm unit count
                           the cost term multiplies cost_coef by (production
                           uses the ordinal round count nr=0/1/2/3). When set,
                           cost = cost_coef * cost_units[arm] instead of
                           cost_coef * nr, for every preset mapped to that arm.
                           See analyze_empirical_cost.py / H0_empirical_cost_units
                           below for the data-derived motivation.

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
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import compute_article_oracle as cao  # noqa: E402
import generate_episode_oracles as geo  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent.parent
_OUTPUT_DIR = _THIS_DIR / "reward_grid_test_results"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

_DEFAULT_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]

# Current production defaults (must mirror enhancement_reward.py / generate_episode_oracles.py
# exactly, so "baseline" reproduces the real pipeline's numbers as a sanity check).
# tier1 updated 0.55->0.35 on 2026-07-25 (G0 shipped to production, see
# run13_rl_grok_pipeline_analysis.md Part 6 §47/§51) -- keep this in sync with
# enhancement_reward.py's CREDIT_AT_WEIGHTED_COUNT whenever that changes again.
# cost_coef staged recalibration: -0.06 -> -0.045 -> -0.03 (2026-07-25) -> -0.02
# (2026-07-26, later found to overcorrect deep-prediction on TEST, see run17-19)
# -> -0.03 (2026-07-29, C2 ship, reverted alongside the ga/ra redesign below).
# Keep this in sync with generate_episode_oracles.py's hardcoded `cost = -0.03 * nr`.
_PROD_COST_COEF = -0.03
# RETIRED by C2 (2026-07-29): explore no longer has a separate scalar
# multiplier -- its old *0.50 is folded into _PROD_DE_WEIGHT/_PROD_BE_WEIGHT
# below. Kept defined (unused in the formula body) only so majority_vote_sweep()/
# corpus_explore_mult_sweep()'s pre-C2 explore_mult grid still has a name to
# compare against; those two functions' whole premise (a single explore scalar)
# no longer maps onto C2's shape -- treat their sweep results as archived/pre-C2.
_PROD_EXPLORE_MULT = 0.50
# C2 (2026-07-29, Part 7 S53-57): explore = cp*(de_weight*de + be_weight*be),
# ra removed entirely from the formula, ga demoted from an additive weight to
# a flat gate penalty below the threshold. Keep in sync with
# generate_episode_oracles.py's _section_reward/_ga_gate_penalty.
_PROD_DE_WEIGHT = 0.45
_PROD_BE_WEIGHT = 0.30
_PROD_GA_GATE_THRESHOLD = 0.5
_PROD_GA_GATE_PENALTY = -0.10
_PROD_QUALITY_WEIGHT = {"strong": 1.00, "standard": 0.65}
_PROD_INSTANCE_CAP = 3
# tier2 updated 0.80->0.45 on 2026-07-25 (J0 shipped to production, see
# run13_rl_grok_pipeline_analysis.md Part 7) -- keep this in sync with
# enhancement_reward.py's CREDIT_AT_WEIGHTED_COUNT whenever that changes again.
_PROD_CREDIT_CURVE = {0: 0.00, 1: 0.35, 2: 0.45, 3: 1.00}
# Candidate E (simple, unweighted mean of the explore term across sections,
# instead of target-words-weighted) was shipped to production earlier (§39) --
# compute_article_oracle.py._compute_r_w auto-detects this via the "explore"
# field's presence in section_oracle.json v4+, unconditionally, not via a
# toggle. "baseline" here must default to True too, or it silently
# reproduces PRE-candidate-E behavior and disagrees with real production
# (caught 2026-07-25: 06_tools__var_standard's baseline margin was off by
# 0.014 -- 0.0227 vs the real 0.0370 -- until this default was fixed).
_PROD_SIMPLE_AVG_EXPLORE = True

# Candidate H0 (empirical cost-unit recalibration) was shipped to production on
# 2026-07-25, see run13_rl_grok_pipeline_analysis.md Part 7 -- cost is now
# cost_coef * _PROD_ARM_COST_UNITS[arm] instead of cost_coef * nr (ordinal round
# count). "baseline" here must default to the empirical units too, or it
# silently reproduces PRE-H0 behavior (same staleness class of bug as
# _PROD_SIMPLE_AVG_EXPLORE above -- keep this in sync with
# generate_episode_oracles.py's _ARM_COST_UNITS whenever that changes again).
_PROD_ARM_COST_UNITS: dict[str, float] = {"skip": 0.0, "light": 1.00, "standard": 1.88, "deep": 2.31}

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

# --- Scale-compensation candidate: audit_enhancement_tags.py found the new
# curve reduces mean enhancement_credit ~40% UNIFORMLY across skip/light/
# standard/deep (since ~90-97% of entries are 0-or-1-instance for EVERY arm,
# and the 1-instance credit was intentionally cut from the old implicit 1.0
# to 0.55) rather than selectively cutting light's credit as hypothesized.
# explore_mult=0.50/0.60 ~= 0.83 is the value that restores the OLD overall
# scale of the explore differentiator while keeping the new curve's (real,
# data-confirmed) deep>standard>light ordering intact.
VARIANTS["D_scale_compensate_083"] = {"explore_mult": 0.83}

# --- Candidate E: simple (unweighted) mean of the explore term across
# sections, instead of target-words-weighted -- user's proposal (2026-07-24):
# an enhancement instance shouldn't count for more just because it landed in
# a long section. See _section_reward_components() in generate_episode_oracles.py
# and _compute_r_w() in compute_article_oracle.py (both updated to support
# this) for the real implementation this cfg flag exercises here for testing.
VARIANTS["E_simple_avg_explore"] = {"simple_avg_explore": True}
VARIANTS["E_plus_D_explore_083"] = {"simple_avg_explore": True, "explore_mult": 0.83}

# Reference: A (backfiring control) combined with D, already shown in §34 to
# partially cancel D's benefit -- kept for contrast against the C x D grid
# above, which does not exhibit this cancellation.
VARIANTS["control_A_plus_explore_065"] = {
    "instance_cap": 5,
    "credit_curve": {0: 0.00, 1: 0.55, 2: 0.80, 3: 0.93, 4: 0.98, 5: 1.00},
    "explore_mult": 0.65,
}

# ---------------------------------------------------------------------------
# Candidate F: curve-SCALE recalibration (run13_rl_grok_pipeline_analysis.md
# §40) -- distinct from D (explore_mult, a blunt external multiplier touching
# every arm/section uniformly) and distinct from the backfiring A/B cap-
# extension family. These only raise the credit for the DOMINANT 0/1-instance
# case (INSTANCE_CAP stays at 3, tier-3 stays anchored at 1.00 -- no cap
# extension, no re-introduction of the A/B dilution mechanism), since §38
# found the fix's ORDERING is real/data-confirmed but its SCALE (specifically
# the 1-instance credit, cut from the old implicit 1.0 to 0.55) was tuned
# against an n=1-pilot recount, not the real ~90%-of-entries-are-0-or-1
# corpus-wide distribution.
# ---------------------------------------------------------------------------
VARIANTS["F1_tier1_070"] = {
    "credit_curve": {0: 0.00, 1: 0.70, 2: 0.85, 3: 1.00},
}
VARIANTS["F2_tier1_080"] = {
    "credit_curve": {0: 0.00, 1: 0.80, 2: 0.90, 3: 1.00},
}
VARIANTS["F3_tier1_065_gentle"] = {
    "credit_curve": {0: 0.00, 1: 0.65, 2: 0.83, 3: 1.00},
}
# F + C combined: raise both the count-ladder's tier-1 floor AND the
# standard-quality weight together -- tests whether the two "safe" (non
# cap-extending) levers compound usefully or interact non-additively, the
# same kind of check §34 did for A+D.
VARIANTS["F1_plus_C_stdw080"] = {
    "credit_curve": {0: 0.00, 1: 0.70, 2: 0.85, 3: 1.00},
    "quality_weight": {"strong": 1.00, "standard": 0.80},
}

# G-series: LOWER (not raise) tier-1, the OPPOSITE direction from F1/F2/F3.
# Motivated by the pairwise-LLM-comparison investigation (see
# run13_rl_grok_pipeline_analysis.md Part 5, pairwise grading sections): a
# statistically significant (binomial two-tailed p=0.031, pooled across 18
# disjoint disagreement sections spanning 16 topics), independently-replicated
# finding that tag-based grading systematically OVER-credits `deep` relative
# to `standard` specifically when deep has found exactly 1 more qualifying
# instance than standard (the clearest cases: standard=0 instances/credit=0.00,
# deep=1 strong instance/credit=0.55 under production -- i.e. EXACTLY the
# tier-1 step). Majority-voted (3-draw) direct pairwise comparison on 5 such
# sections put the TRUE standard-vs-deep gap at a mean of ~+0.207 (range
# +0.067 to +0.367), not +0.55 -- i.e. tier-1's current value is roughly
# 2.5x too steep relative to this direct measurement.
# NOTE: this directly conflicts with F3's (already-recommended, not yet
# shipped) tier1=0.65 -- F3 was validated via corpus-flip-count + one
# replicate-majority label, a coarser test that cannot detect a
# small-in-aggregate-but-wrong-in-direction per-section miscalibration like
# this one. Presented as a genuine, unresolved tension for the final
# ship decision, not silently overridden.
# G0 = conservative half-measure (splits the gap between current 0.55 and the
# ~0.20 point estimate); G1 = aggressive, directly calibrated to the point
# estimate. Both leave tier-2/tier-3 unchanged (weaker, smaller-magnitude
# evidence there -- Earth_Oceans_Origin/Understanding_Reasoning_LLMs showed
# disagreement margins of only -0.147/-0.25 at those higher counts, versus
# the clean -0.55 at tier-1).
VARIANTS["G0_tier1_035"] = {
    "credit_curve": {0: 0.00, 1: 0.35, 2: 0.80, 3: 1.00},
}
VARIANTS["G1_tier1_020"] = {
    "credit_curve": {0: 0.00, 1: 0.20, 2: 0.80, 3: 1.00},
}

# ---------------------------------------------------------------------------
# Candidate J0: tier-2 recalibration (2026-07-25) -- distinct from G-series
# (tier-1). Scaled standard-vs-deep pairwise data (16 articles, N=218 section-
# dim observations) plus a dedicated repeat-draws check on 7 clean tier0-vs-
# tier2 boundary cases (pooled N=8 draws/target, 56 total) found the real
# pairwise-judged magnitude of a full 0-to-2-weighted-instance jump is only
# ~+0.165, vs the current tag's flat +0.800 -- a robust, twice-measured (n=3
# then n=8 draws/target, barely moved: 0.169->0.165) ~4.8x overstatement.
# NOTE: this raw point estimate (~0.165) is actually BELOW tier1's own
# established estimate (~0.207, behind G0) -- taken at face value this would
# violate the curve's required monotonicity (tier2 must stay >= tier1=0.35).
# Rather than set tier2 to the raw estimate, J0 uses the SAME "conservative
# compromise between old assumption and point estimate" logic as G0 itself:
# roughly the midpoint of (0.80, ~0.17) ~= 0.485, chosen as 0.45 to keep
# comfortable headroom above tier1. Tier-3 (1.00) is UNCHANGED -- the one
# tier0-vs-tier3 data point collected was flagged unreliable (title-matching
# bug in the cross-referencing script), so there is no trustworthy evidence
# to recalibrate it yet.
# ---------------------------------------------------------------------------
VARIANTS["J0_tier2_045"] = {
    "credit_curve": {0: 0.00, 1: 0.35, 2: 0.45, 3: 1.00},
}

# ---------------------------------------------------------------------------
# Candidate K-series: TRAIN-ONLY, SELECTION-BIAS-CORRECTED re-derivation
# (2026-07-25) -- prompted by the user flagging that G0/H0/J0's evidence
# mixed TRAIN and TEST articles (train/test leakage risk for any future
# retrain+eval). Re-scanning restricted to TRAIN-only articles found:
#   - H0: negligible change (units 1.90/2.35 vs shipped 1.88/2.31) -- NOT
#     re-shipped, see PRE_H0_ordinal_nr/H0_empirical_cost_units above.
#   - tier1/tier2: a SEPARATE, more significant issue surfaced while doing
#     this -- G0's original +0.207 point estimate was computed from only the
#     "clearest tag-vs-pairwise DISAGREEMENT" cases (sections cherry-picked
#     because they showed the largest gap from the OLD 0.55 assumption), not
#     a representative sample of all clean tier0-vs-tier1 cases. That is a
#     selection-bias/regression-to-the-mean problem, independent of and in
#     addition to the train/test question. Re-scanning ALL currently-
#     collected clean 0-vs-1 cases (unfiltered by disagreement), TRAIN-only:
#     mean=+0.098 (n=38) -- much lower than +0.207. Same fix applied to J0's
#     tier2 evidence (which was NOT disagreement-pre-filtered to begin with,
#     so this is a pure TRAIN-only comparison there): mean=+0.210 (n=5),
#     vs the shipped-from-all-42 +0.165.
#   - Applying the SAME "conservative compromise between old assumption and
#     point estimate" convention already used for G0/J0 themselves:
#       tier1: midpoint(0.55, 0.098) ~= 0.32
#       tier2: midpoint(0.80, 0.210) ~= 0.50
#     Both are modest deltas from what's shipped (0.35, 0.45) -- this
#     corpus-grid-sweep gate checks whether either delta actually flips any
#     already-graded article's decision before investing in full
#     re-validation (backup/regen-42/replicate-vote).
# ---------------------------------------------------------------------------
VARIANTS["K0_tier1_032_only"] = {
    "credit_curve": {0: 0.00, 1: 0.32, 2: 0.45, 3: 1.00},
}
VARIANTS["K1_tier2_050_only"] = {
    "credit_curve": {0: 0.00, 1: 0.35, 2: 0.50, 3: 1.00},
}
VARIANTS["K2_tier1_032_tier2_050"] = {
    "credit_curve": {0: 0.00, 1: 0.32, 2: 0.50, 3: 1.00},
}

# ---------------------------------------------------------------------------
# Candidate H0: EMPIRICAL cost-unit recalibration (2026-07-25) -- distinct in
# kind from G-series (which retunes the CONTENT credit curve). This retunes
# the COST side using measured data instead of a normative cost_coef sweep.
#
# analyze_cost_imbalance.py found `cost` is 93% of deep's average shortfall
# vs the winning arm (deep's content is actually slightly FAVORED on average
# by gt_base+explore combined). Before treating cost_coef itself as the lever,
# analyze_empirical_cost.py measured each arm's REAL exploration-phase
# activity (actual query+scrape counts from each arm's own separately-run
# episode's .research/full_queries.md + url_phases.json, corpus-wide n=42):
#   light=4.83, standard=9.07, deep=11.14 (mean explore_effort, skip=0)
# i.e. deep's real activity is only 2.31x light's, not the 3.00x its flat
# nr=3 assumption charges it for (standard: 1.88x actual vs 2.00x assumed).
# Per-round incrementals confirm the mechanism (real diminishing returns, not
# noise): round1 +3.60 queries/+1.24 scrapes, round2 +3.88q/+0.36 scrapes
# (scrape saturation), round3(deep) only +1.81q/+0.26 scrapes (both query
# generation and scraping have saturated by round 3).
#
# This variant swaps the per-arm unit count the cost term multiplies
# cost_coef by -- {0,1,2,3} (assumed) -> {0, 1.00, 1.88, 2.31} (measured) --
# while leaving cost_coef=-0.06 itself untouched. A data-derived recalibration
# of what "rounds" means for cost, not an arbitrary new constant.
# ---------------------------------------------------------------------------
VARIANTS["H0_empirical_cost_units"] = {
    "cost_units": {"skip": 0.0, "light": 1.00, "standard": 1.88, "deep": 2.31},
}
# Kept for regression/backward comparison now that H0 IS the production
# baseline (2026-07-25) -- reproduces the OLD (pre-H0) ordinal-round-count
# cost model exactly, the mirror image of how G0_tier1_035 was kept after G0 shipped.
VARIANTS["PRE_H0_ordinal_nr"] = {
    "cost_units": {"skip": 0.0, "light": 1.0, "standard": 2.0, "deep": 3.0},
}

# ---------------------------------------------------------------------------
# Candidate I-series: cost_coef ABSOLUTE SCALE (2026-07-25) -- distinct from H0
# (which only fixed the per-arm UNIT shape, {0,1,2,3}->{0,1.00,1.88,2.31}).
# Even after H0, analyze_cost_imbalance.py still shows cost = ~85% of deep's
# average shortfall vs the winning arm (down from ~93% pre-H0, but still
# overwhelmingly dominant) -- evidence that -0.06 itself, not just the units it
# multiplies, may be too large. These candidates scale cost_coef down while
# keeping H0's empirical unit shape ({0,1.00,1.88,2.31}) intact, to isolate the
# SCALE question from the (already-fixed) shape question. Untested/unshipped --
# see run13_rl_grok_pipeline_analysis.md Part 7 for validation results.
# ---------------------------------------------------------------------------
_H0_UNITS = {"skip": 0.0, "light": 1.00, "standard": 1.88, "deep": 2.31}
VARIANTS["I0_cost_coef_050"] = {"cost_coef": -0.050, "cost_units": _H0_UNITS}
VARIANTS["I1_cost_coef_045"] = {"cost_coef": -0.045, "cost_units": _H0_UNITS}
VARIANTS["I2_cost_coef_040"] = {"cost_coef": -0.040, "cost_units": _H0_UNITS}
VARIANTS["I3_cost_coef_035"] = {"cost_coef": -0.035, "cost_units": _H0_UNITS}
VARIANTS["I4_cost_coef_030"] = {"cost_coef": -0.030, "cost_units": _H0_UNITS}

# I-series continued (2026-07-26): -0.03 is current production. Testing
# further reductions below production to check whether deep's structural
# cost-disadvantage (highest cost_units=2.31 of any arm) can be eased further
# without disturbing the corpus, motivated by the goldremoved pilot's
# razor-thin (+0.0074) article-level margin and the deep-scarcity roadmap.
VARIANTS["I5_cost_coef_025"] = {"cost_coef": -0.025, "cost_units": _H0_UNITS}
VARIANTS["I6_cost_coef_020"] = {"cost_coef": -0.020, "cost_units": _H0_UNITS}
VARIANTS["I7_cost_coef_015"] = {"cost_coef": -0.015, "cost_units": _H0_UNITS}


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
    simple_avg_explore = cfg.get("simple_avg_explore", _PROD_SIMPLE_AVG_EXPLORE)
    cost_units = cfg.get("cost_units", _PROD_ARM_COST_UNITS)
    preset_to_arm = {pid: arm for arm, ids in geo._ARM_PRESETS.items() for pid in ids}

    sections_output: dict[str, dict] = {}
    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        preset_rewards: dict[int, float] = {}
        preset_explore: dict[int, float] = {}
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

            de_weight = cfg.get("de_weight", _PROD_DE_WEIGHT)
            be_weight = cfg.get("be_weight", _PROD_BE_WEIGHT)
            ga_threshold = cfg.get("ga_gate_threshold", _PROD_GA_GATE_THRESHOLD)
            ga_penalty = cfg.get("ga_gate_penalty", _PROD_GA_GATE_PENALTY)

            gt_base = 0.20 * cc + 0.20 * fl
            explore = cp * (de_weight * de + be_weight * be)
            ga_gate = ga_penalty if ga < ga_threshold else 0.0
            units = cost_units[preset_to_arm[p]]
            cost = cost_coef * units
            preset_rewards[p] = gt_base + explore + ga_gate + cost
            preset_explore[p] = explore

        arm_rewards = {arm: preset_rewards[geo._ARM_PRESETS[arm][0]] for arm in geo._ARM_ORDER}
        arm_explore = {arm: preset_explore[geo._ARM_PRESETS[arm][0]] for arm in geo._ARM_ORDER}
        sections_output[sec_id] = {
            "oracle": max(geo._ARM_ORDER, key=arm_rewards.__getitem__),
            "rewards": arm_rewards,
        }
        if simple_avg_explore:
            sections_output[sec_id]["explore"] = arm_explore

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


def majority_vote_sweep_named(article_var: str, named_cfgs: list[tuple[str, dict]], emit) -> None:
    """Generalized version of majority_vote_sweep(): takes arbitrary named cfgs
    (not just explore_mult values), so ANY candidate -- curve-scale (F-series),
    quality_weight (C), or explore_mult (D) -- can be checked the same
    non-circular way: recompute the ORIGINAL + all 3 replicates under the
    IDENTICAL cfg, then take a majority vote across the 4 independent draws,
    instead of comparing a swept cfg against a single formula-dependent label.
    """
    for name, cfg in named_cfgs:
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
        emit(f"  {name:<28}  majority={majority_arm:<8}{tie_flag}  votes=[{votes_str}]  draws=[{draws_str}]")


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
    named_cfgs = [
        (f"explore_mult={em:.2f}", {} if em == _PROD_EXPLORE_MULT else {"explore_mult": em})
        for em in explore_mults
    ]
    majority_vote_sweep_named(article_var, named_cfgs, emit)


def _recompute_any(article_dir_name: str, cfg: dict) -> tuple[str, float, dict[str, float]] | None:
    """Same as _recompute(), but works for ANY already-graded bases/ directory,
    not just the 2 hardcoded default (re-graded, tagged) articles -- TRAIN
    variant articles (dir name ends with the canonical "__var_minimal"/
    "__var_standard"/"__var_demanding" suffix, uses episodes/ +
    _EPISODE_ROUNDS/_ARM_PRESETS) AND TEST/no-variant/augmented articles (any
    other name, e.g. "13_agent_framework", "Insects_Consciousness__mixeddepth",
    or an ablation-pilot name like "<topic>__var_goldremoved" that happens to
    contain the substring "__var_" without being a real training variant,
    uses test_episodes/ + _TEST_EPISODE_ROUNDS/_TEST_ARM_PRESETS, sequential
    preset ids 0-3, per generate_episode_oracles.py's own no_variant branch).

    IMPORTANT: the no-variant check below matches the exact canonical suffix,
    NOT a loose ``"__var_" in article_dir_name`` substring check -- the latter
    previously misrouted ablation-pilot articles (whose name contains "__var_"
    without being a real training variant) to the wrong preset-ID scheme
    (ARM_EPISODE/_EPISODE_ROUNDS instead of _TEST_ARM_PRESETS/_TEST_EPISODE_ROUNDS),
    silently reading a non-existent or unrelated episode directory for
    "standard"/"deep" (found via 10_memory_knowledge_access__var_goldremoved:
    this bug made "deep" read a non-existent preset5 dir, returning garbage
    negative R_w, while "standard" silently read preset3's real content --
    actually deep's episode -- same bug class as compute_article_oracle.py's
    _episode_dir(), fixed there on 2026-07-26; fixed here the same day).

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

    no_variant = not any(
        article_dir_name.endswith(f"__{v}") for v in ("var_minimal", "var_standard", "var_demanding")
    )
    if no_variant:
        ep_rounds = geo._TEST_EPISODE_ROUNDS
        # no_variant episodes are named "<base_article>__preset<N>" (plain base
        # name, matching generate_episode_oracles.py's own no_variant branch) --
        # article_dir_name itself may already carry a "__mixeddepth"-style
        # augmentation suffix, which IS part of the episode dir name too (the
        # pilots' episodes were generated under that exact augmented name).
        episode_prefix = article_dir_name
        # Directory ROOT and preset-numbering SCHEME are independent decisions
        # (mirrors compute_article_oracle.py's _episode_dir() fix): most
        # no-variant articles live under test_episodes/, but some ablation
        # pilots (e.g. "<topic>__var_goldremoved") have their episodes placed
        # under episodes/ instead by rl_data_generator.py. Detect which root
        # actually holds preset0 rather than assuming test_episodes/.
        if (_EPISODES_DIR / f"{episode_prefix}__preset0").exists() and not (
            _TEST_EPISODES_DIR / f"{episode_prefix}__preset0"
        ).exists():
            episodes_dir = _EPISODES_DIR
        else:
            episodes_dir = _TEST_EPISODES_DIR
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
    simple_avg_explore = cfg.get("simple_avg_explore", _PROD_SIMPLE_AVG_EXPLORE)
    cost_units = cfg.get("cost_units", _PROD_ARM_COST_UNITS)
    preset_to_arm = {pid: arm for arm, ids in arm_presets.items() for pid in ids}

    sections_output: dict[str, dict] = {}
    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        preset_rewards: dict[int, float] = {}
        preset_explore: dict[int, float] = {}
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

            de_weight = cfg.get("de_weight", _PROD_DE_WEIGHT)
            be_weight = cfg.get("be_weight", _PROD_BE_WEIGHT)
            ga_threshold = cfg.get("ga_gate_threshold", _PROD_GA_GATE_THRESHOLD)
            ga_penalty = cfg.get("ga_gate_penalty", _PROD_GA_GATE_PENALTY)

            gt_base = 0.20 * cc + 0.20 * fl
            explore = cp * (de_weight * de + be_weight * be)
            ga_gate = ga_penalty if ga < ga_threshold else 0.0
            units = cost_units[preset_to_arm[p]]
            cost = cost_coef * units
            preset_rewards[p] = gt_base + explore + ga_gate + cost
            preset_explore[p] = explore

        arm_rewards = {arm: preset_rewards[preset_ids[0]] for arm, preset_ids in arm_presets.items()}
        arm_explore = {arm: preset_explore[preset_ids[0]] for arm, preset_ids in arm_presets.items()}
        sections_output[sec_id] = {
            "oracle": max(geo._ARM_ORDER, key=arm_rewards.__getitem__),
            "rewards": arm_rewards,
        }
        if simple_avg_explore:
            sections_output[sec_id]["explore"] = arm_explore

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


def corpus_grid_sweep(variant_names: list[str], emit) -> None:
    """Corpus-wide C x D (quality_weight x explore_mult) grid sweep across
    EVERY already-graded article-variant dir under _BASES_DIR.

    Unlike corpus_explore_mult_sweep(), this ALSO exercises quality_weight/
    instance_cap/credit_curve -- meaningful corpus-wide now that all 40
    production articles carry the [instances=N; quality=...] tag (see
    run13_rl_grok_pipeline_analysis.md Part 5 for when/why this became true).
    Before this, quality_weight sweeps were a no-op on 38/40 articles since
    untagged reasoning.json bypasses enhancement_credit() entirely.

    Purely DESCRIPTIVE, same caveat as corpus_explore_mult_sweep(): reports
    flip counts/which articles flip vs baseline, split by original margin
    tier. Not a correctness judgment -- most of these 40 articles have no
    independent re-grade/replicate confirmation of their own, so a flip here
    is evidence the lever is doing something, not evidence it's right.
    """
    article_dirs = sorted(
        d.name for d in _BASES_DIR.iterdir()
        if d.is_dir() and (d / "article_oracle.json").exists()
    )
    baseline_results: dict[str, str] = {}
    baseline_orig_margin: dict[str, float] = {}
    for name in article_dirs:
        result = _recompute_any(name, {})
        if result is None:
            continue
        arm, _margin, _ = result
        baseline_results[name] = arm
        try:
            orig = json.loads((_BASES_DIR / name / "article_oracle.json").read_text(encoding="utf-8"))
            baseline_orig_margin[name] = orig.get("margin", 0.0)
        except (OSError, json.JSONDecodeError):
            baseline_orig_margin[name] = 0.0

    emit(f"  Corpus size (already-graded, recomputable): {len(baseline_results)} article-variant dirs")
    base_dist = {a: sum(1 for arm in baseline_results.values() if arm == a) for a in geo._ARM_ORDER}
    emit(f"  Baseline arm distribution: {base_dist}")
    emit()
    for variant_name in variant_names:
        cfg = VARIANTS[variant_name]
        flips = []
        new_dist = {a: 0 for a in geo._ARM_ORDER}
        for name, base_arm in baseline_results.items():
            result = _recompute_any(name, cfg)
            if result is None:
                continue
            new_arm, _new_margin, _ = result
            new_dist[new_arm] = new_dist.get(new_arm, 0) + 1
            if new_arm != base_arm:
                flips.append((name, base_arm, new_arm, baseline_orig_margin[name]))
        thin = [f for f in flips if abs(f[3]) < 0.06]
        comfortable = [f for f in flips if abs(f[3]) >= 0.06]
        emit(f"  {variant_name:<28} flips={len(flips)}/{len(baseline_results)}  "
             f"(thin-margin<0.06: {len(thin)}, comfortable-margin>=0.06: {len(comfortable)})  "
             f"new_dist={new_dist}")
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
    parser.add_argument(
        "--corpus-grid-sweep",
        action="store_true",
        help="Corpus-wide C x D grid sweep (quality_weight x explore_mult) across EVERY "
             "already-graded bases/ dir -- meaningful now that all 40 production articles "
             "carry the enhancement count/quality tag. Uses the same VARIANTS grid cells "
             "as the per-article table (--corpus-grid-variants to restrict).",
    )
    parser.add_argument(
        "--corpus-grid-variants",
        nargs="+",
        default=[v for v in VARIANTS if v.startswith("grid_")],
        choices=list(VARIANTS.keys()),
        help="Which VARIANTS entries to test in --corpus-grid-sweep mode (default: all grid_* cells).",
    )
    args = parser.parse_args()

    lines: list[str] = []

    def emit(line: str = "") -> None:
        print(line)
        lines.append(line)

    if args.corpus_grid_sweep:
        emit("=" * 100)
        emit("CORPUS-WIDE C x D GRID SWEEP (all already-graded articles)")
        emit("=" * 100)
        corpus_grid_sweep(args.corpus_grid_variants, emit)
        if not args.no_file:
            out_dir = Path(args.output_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_path = out_dir / f"corpus_grid_sweep_{timestamp}.txt"
            out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"\n[written to {out_path}]")
        return

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
            result = _recompute_any(article, cfg)
            if result is None:
                emit(f"  {variant_name:<28} SKIPPED (bases dir or research_digest.md/guideline_features.json missing)")
                continue
            arm, margin, r_w = result
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
