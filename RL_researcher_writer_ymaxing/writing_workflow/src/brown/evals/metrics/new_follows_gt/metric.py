"""Implementation of the FollowsGT evaluation metric.

This module implements a metric that evaluates how well generated articles
match ground-truth articles across six binary dimensions:
core_content, flow, structure, depth_enhancement, breadth_enhancement, core_preservation.
"""

from typing import Any, cast

from opik.evaluation.metrics import score_result

from brown.evals.metrics.base import BrownBaseMetric
from brown.models import ModelConfig, SupportedModels, get_model

from . import prompts
from .types import (
    CorePreservationArticleScores,
    FollowsGTArticleScores,
)


class FollowsGTMetric(BrownBaseMetric):
    """A metric that evaluates generated articles against ground-truth articles across six dimensions.

    This metric uses a language model to assess how well the generated article matches the GT
    (CoreContent, Flow, Structure) and how well the exploration phase added value
    (DepthEnhancement, BreadthEnhancement, CorePreservation). It automatically handles
    both single-paragraph (such as in the LFRQA) and multi-section articles, and computes average scores per dimension,
    providing detailed breakdowns for comprehensive analysis.

    Returns separate ScoreResult objects for each of the six dimensions with per-section reasoning.

    Args:
        model: The language model to use for evaluation. Defaults to GOOGLE_GEMINI_25_FLASH.
        name: The name of the metric. Defaults to "article".
        model_config: Configuration for the model including temperature, thinking budget,
            and retry settings. If None, uses default configuration with temperature=0.0,
            thinking_budget=4096, include_thoughts=False, and max_retries=3.
        track: Whether to track the metric in observability tools. Defaults to True.
        project_name: Optional project name to track the metric in for cases when there are
            no parent span/trace to inherit project name from.

    Attributes:
        few_shot_examples: Default few-shot examples used for prompt engineering.
        structured_output_type: The ArticleScores type used for structured output parsing.

    Example:
        >>> from brown.evals.metrics.article.metric import ArticleMetric
        >>> article_metric = ArticleMetric()
        >>> results = await article_metric.ascore(
        ...     output="Generated article content...",
        ...     expected_output="Expected article content..."
        ... )
        >>> # results is a list of ScoreResult objects, one per dimension
        >>> for result in results:
        ...     print(f"{result.name}: {result.value}")  # e.g., "article_flow: 0.85"
        ...     print(f"Reason: {result.reason}")

    """

    def __init__(
        self,
        model: SupportedModels = SupportedModels.GOOGLE_GEMINI_25_FLASH,
        name: str = "ground_truth",
        model_config: ModelConfig | None = None,
        track: bool = True,
        project_name: str | None = None,
    ) -> None:
        """Initialize the FollowsGTMetric instance."""
        model_config = model_config or ModelConfig(temperature=0.0, thinking_budget=1024 * 4, include_thoughts=False, max_retries=3)
        super().__init__(
            model=model,
            name=name,
            structured_output_type=FollowsGTArticleScores,
            few_shot_examples=prompts.DEFAULT_FEW_SHOT_EXAMPLES,
            model_config=model_config,
            track=track,
            project_name=project_name,
        )

    async def ascore(
        self,
        output: str,
        expected_output: str,
        exploration_sources: str | None = None,
        **ignored_kwargs: Any,
    ) -> list[score_result.ScoreResult]:
        """Asynchronously calculate the ground-truth evaluation scores across six dimensions.

        Returns a list of six ScoreResult objects (one per the six dimensions: core_content, flow, structure,
        depth_enhancement, breadth_enhancement, core_preservation)
        with aggregated scores (0.0-1.0) and detailed per-section reasoning.


        The evaluation process involves:
        1. Initializing a fresh model client to avoid coroutine reuse issues
        2. Constructing an evaluation prompt with few-shot examples
        3. Getting structured output from the LLM with ArticleScores format
        4. Converting the response to ScoreResult objects for each dimension

        Args:
            output: The generated article content to be evaluated.
            expected_output: The expected article content to compare against.
            exploration_sources: Optional formatted string listing the exploration-phase
                sources for this episode. When provided, DepthEnhancement and
                BreadthEnhancement scores only credit additions traceable to these
                sources. When None, falls back to standard criteria (backward compatible).
            **ignored_kwargs: Additional keyword arguments that are ignored to maintain
                compatibility with the base metric interface.

        Returns:
            list[score_result.ScoreResult]: A list of ScoreResult objects, one for each
                dimension (core_content, flow, structure, depth_enhancement, breadth_enhancement, core_preservation), containing the
                aggregated score (between 0.0 and 1.0) and detailed reasons broken
                down by sections.

        Raises:
            ValueError: If the model fails to return a structured response or if the
                response cannot be parsed into the expected ArticleScores format.

        Note:
            A new model client is initialized for each call to avoid coroutine reuse
            issues when running in multiple threads due to sharing the same model
            instance across threads.

        """
        # Pass 1: evaluate the five independent criteria. The SYSTEM_PROMPT does not include the
        # CorePreservation criterion definition, so the LLM's core_preservation output here is a
        # placeholder that will be overwritten by pass 2.
        pass1_client = get_model(self.model, self.model_config).with_structured_output(FollowsGTArticleScores)
        pass1_query = prompts.get_eval_prompt(
            output=output,
            expected_output=expected_output,
            few_shot_examples=self.few_shot_examples,
            exploration_sources=exploration_sources,
        )
        pass1_response = cast(
            FollowsGTArticleScores,
            await pass1_client.ainvoke(
                [
                    {
                        "role": "user",
                        "content": pass1_query,
                    }
                ]
            ),
        )

        if not pass1_response:
            raise ValueError("Model failed to return a structured response for pass 1.")

        # Pass 2: evaluate core_preservation with the finalised depth/breadth scores as context.
        # Sequential execution guarantees the judge builds on the actual pass-1 enhancement scores
        # regardless of whether they are 0 or 1.
        core_pres_client = get_model(self.model, self.model_config).with_structured_output(CorePreservationArticleScores)
        core_pres_query = prompts.get_core_preservation_prompt(
            output=output,
            expected_output=expected_output,
            article_scores=pass1_response,
            few_shot_examples=self.few_shot_examples,
        )
        core_pres_response = cast(
            CorePreservationArticleScores,
            await core_pres_client.ainvoke(
                [
                    {
                        "role": "user",
                        "content": core_pres_query,
                    }
                ]
            ),
        )

        # Overwrite the pass-1 core_preservation placeholders with the pass-2 scores.
        # Matching by index is robust against minor title paraphrasing by the LLM.
        if core_pres_response and len(core_pres_response.sections) == len(pass1_response.sections):
            for section, core_pres_section in zip(pass1_response.sections, core_pres_response.sections):
                section.scores.core_preservation = core_pres_section.core_preservation

        return pass1_response.to_score_result(self.name)
