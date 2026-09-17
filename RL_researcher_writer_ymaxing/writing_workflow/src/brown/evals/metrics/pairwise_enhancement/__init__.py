"""Pairwise depth/breadth-enhancement comparison metric.

Compares two arms' renderings of the SAME article section directly against
each other, instead of scoring each in isolation against a fixed rubric.
Built to test whether judge-side ceiling saturation/absolute-scale imprecision
(not just written-content noise) is limiting the standard-vs-deep separation
in the section-level reward -- see run13_rl_grok_pipeline_analysis.md Part 5
for the background and design rationale.
"""

from .metric import grade_pairwise
from .types import PairwiseEnhancementJudgment, PreferenceLabel

__all__ = ["grade_pairwise", "PairwiseEnhancementJudgment", "PreferenceLabel"]
