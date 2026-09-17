"""Type definitions for the pairwise depth/breadth-enhancement comparison metric.

Both dimensions (depth and breadth) are judged in ONE call per pairwise
comparison, so the total call count matches the ~180-call estimate (3 pairs x
~60 sections), not double it.
"""

from typing import Literal

import pydantic

PreferenceLabel = Literal["a_much_more", "a_more", "tie", "b_more", "b_much_more"]


class _DimensionJudgment(pydantic.BaseModel):
    """One dimension's (depth or breadth) relative judgment for a single pairwise comparison."""

    preference: PreferenceLabel = pydantic.Field(
        description=(
            "Does document B contain MORE distinct, source-attributed enhancement content than "
            "document A, for this ONE dimension? 'tie' means A and B are equivalent (including "
            "both being empty)."
        )
    )
    a_instances: list[str] = pydantic.Field(
        default_factory=list,
        description="Distinct enhancement instances present in A but NOT in B (brief phrase each).",
    )
    b_instances: list[str] = pydantic.Field(
        default_factory=list,
        description="Distinct enhancement instances present in B but NOT in A (brief phrase each).",
    )


class PairwiseEnhancementJudgment(pydantic.BaseModel):
    """A single pairwise comparison of two article sections, covering BOTH enhancement
    dimensions (depth and breadth) in one structured-output call.

    Compares document A against document B -- both are one arm's rendering of the
    SAME article section.
    """

    depth: _DimensionJudgment = pydantic.Field(description="Depth-enhancement comparison.")
    breadth: _DimensionJudgment = pydantic.Field(description="Breadth-enhancement comparison.")
    reasoning: str = pydantic.Field(description="Brief overall justification referencing the specific instances found for both dimensions.")
