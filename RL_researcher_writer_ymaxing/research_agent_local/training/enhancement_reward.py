"""Tunable count x quality -> credit mapping for depth/breadth enhancement scoring.

Background: section-level depth_enhancement/breadth_enhancement grading used to be
binary (0/1), capping reward credit at the FIRST qualifying instance regardless of
how many additional valid, source-attributed instances a section actually contained.
This under-rewarded standard/deep exploration (which tends to produce more qualifying
instances per section) relative to light, a plausible structural contributor to the
persistent light/P1 oracle majority. See run13_rl_grok_pipeline_analysis.md, Part 5
(sections 25-27) for the full investigation and worked examples from real graded
articles.

The grader (writing_workflow/src/brown/evals/metrics/new_follows_gt/) now reports,
for depth_enhancement/breadth_enhancement only, a structured tag embedded in the
`reason` text: ``[instances=N; quality=tier1,tier2,...]`` where N is the true total
count of qualifying instances and each tier is "strong" or "standard". The binary
0/1 `score` field is UNCHANGED (still feeds article-level scores.json aggregation),
so the richer (count, qualities) signal lives entirely in the free-text reason,
parsed downstream by generate_episode_oracles.py::_parse_sections_ordered.

HOW TO TUNE: edit the constants below and re-run, in order:
    python3 training/generate_episode_oracles.py
    python3 training/compute_article_oracle.py
NO re-grading is needed to retune these constants -- (count, qualities) are parsed
fresh from the already-graded reasoning.json on every run. Re-grading is only
required if the grader's tag itself needs to change (e.g. adding a third quality
tier), since that is baked into the graded text.

This module has zero dependencies beyond the stdlib so it can be imported freely
from both generate_episode_oracles.py and compute_article_oracle.py without risk
of circular imports or heavy side effects.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Tunable parameters
# ---------------------------------------------------------------------------

#: Maximum number of qualifying instances that earn credit (anti-stuffing: any
#: instances beyond this many, in the WEIGHTED sense below, no longer add credit).
#: The grader itself reports the true, uncapped count -- capping happens here,
#: downstream, so raising this later does not require re-grading.
INSTANCE_CAP: int = 3

#: Per-instance weight by quality tier, used to compute a single "weighted count"
#: from a list of per-instance tiers before applying the saturation curve below.
#: "strong" instances count fully; "standard" instances count partially, so e.g.
#: 2 strong instances (weight 2.0) sit between 2 and 3 standard instances
#: (weight 1.3-1.95) in the saturation curve -- quantity can partially substitute
#: for quality and vice versa, both folded into one dimension before saturating.
QUALITY_WEIGHT: dict[str, float] = {
    "strong": 1.00,
    "standard": 0.65,
}

#: Fallback weight for an unrecognized quality tier (defensive; should not normally
#: be hit if the grader follows the mandated "strong"/"standard" vocabulary).
_DEFAULT_QUALITY_WEIGHT = QUALITY_WEIGHT["standard"]

#: Saturating credit curve, keyed by integer weighted-instance-count from 0 to
#: INSTANCE_CAP inclusive. Concave / diminishing-returns by design: a single
#: instance is deliberately credited LESS than the old binary scheme's implicit
#: 1.0, so that multi-instance sections have real headroom to score higher above
#: it -- this reshaping (not raising the ceiling) is the actual fix for the
#: "enhancement ceiling" bias while preserving the existing anti-stuffing cap on
#: the `explore` term in _section_reward (still capped at 0.5 * core_preservation).
CREDIT_AT_WEIGHTED_COUNT: dict[int, float] = {
    0: 0.00,
    1: 0.55,
    2: 0.80,
    3: 1.00,
}


def enhancement_credit(qualities: list[str]) -> float:
    """Map a list of per-instance quality tiers to a single credit value in [0, 1].

    Substitutes for the old binary depth_enhancement/breadth_enhancement score in
    _section_reward's ``explore`` term. ``qualities`` should be the list of
    "strong"/"standard" tags parsed from the grader's ``[instances=N; quality=...]``
    tag (already capped to at most 5 entries by the grader itself, ideally in
    strongest-first order -- see prompts.py); an empty list means 0 qualifying
    instances (score was 0).

    When there are more than INSTANCE_CAP qualifying instances, only the
    STRONGEST INSTANCE_CAP of them are counted -- qualities are sorted by weight
    (descending) before taking the cap, regardless of the order they arrived in.
    This matters because the grader's own vocabulary is "in the order discussed"
    (not necessarily strength order), so relying on plain list order would let a
    weak instance edge out a genuinely stronger one just by being reported first.

    The curve is a smooth interpolation of CREDIT_AT_WEIGHTED_COUNT driven by the
    quality-weighted instance count, capped at INSTANCE_CAP:
        0 instances            -> 0.00
        1 standard instance    -> ~0.36  (0.65 weighted, interpolated 0.00->0.55)
        1 strong instance      -> 0.55
        2 standard instances   -> ~0.63  (1.30 weighted, interpolated 0.55->0.80)
        2 strong instances     -> 0.80
        3 standard instances   -> ~0.79  (1.95 weighted, interpolated 0.55->0.80)
        3+ strong instances    -> 1.00
    """
    if not qualities:
        return 0.00

    weights = sorted(
        (QUALITY_WEIGHT.get(q, _DEFAULT_QUALITY_WEIGHT) for q in qualities),
        reverse=True,
    )
    weighted = sum(weights[:INSTANCE_CAP])
    weighted = min(weighted, float(INSTANCE_CAP))

    lo = int(weighted)
    hi = min(lo + 1, INSTANCE_CAP)
    frac = weighted - lo

    lo_credit = CREDIT_AT_WEIGHTED_COUNT[lo]
    hi_credit = CREDIT_AT_WEIGHTED_COUNT[hi]
    return round(lo_credit + frac * (hi_credit - lo_credit), 6)
