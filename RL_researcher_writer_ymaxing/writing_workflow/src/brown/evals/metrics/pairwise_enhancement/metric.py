"""Async grading function for the pairwise depth/breadth-enhancement comparison metric."""

from typing import cast

from brown.models import ModelConfig, SupportedModels, get_model, structured_output_kwargs

from . import prompts
from .types import PairwiseEnhancementJudgment


async def grade_pairwise(
    doc_a: str,
    doc_b: str,
    section_guideline: str,
    model: SupportedModels = SupportedModels.GOOGLE_GEMINI_25_FLASH,
    model_config: ModelConfig | None = None,
) -> PairwiseEnhancementJudgment:
    """Grade one pairwise comparison (one section, BOTH depth and breadth in one call).

    A new model client is created per call (matches FollowsGTMetric's pattern,
    avoids coroutine-reuse issues when running many calls concurrently).

    Args:
        doc_a: Document A's rendering of this section.
        doc_b: Document B's rendering of this section.
        section_guideline: The guideline's demand text for this section.
        model: The judge model. Defaults to Gemini 2.5 Flash; pass
            SupportedModels.ANTHROPIC_CLAUDE_SONNET for the more reliable judge
            used elsewhere in this investigation's re-grades (§24/§28).
        model_config: Defaults to temperature=0.0, matching the deterministic
            grading convention used throughout this pipeline.

    Returns:
        The parsed PairwiseEnhancementJudgment (depth + breadth).

    Raises:
        ValueError: If the model fails to return a structured response.
    """
    model_config = model_config or ModelConfig(temperature=0.0, thinking_budget=1024 * 4, include_thoughts=False, max_retries=3)
    client = get_model(model, model_config).with_structured_output(PairwiseEnhancementJudgment, **structured_output_kwargs(model))
    query = prompts.get_pairwise_prompt(
        section_guideline=section_guideline,
        doc_a=doc_a,
        doc_b=doc_b,
    )
    response = cast(
        PairwiseEnhancementJudgment,
        await client.ainvoke([{"role": "user", "content": query}]),
    )
    if not response:
        raise ValueError("Model failed to return a structured pairwise judgment.")
    return response
