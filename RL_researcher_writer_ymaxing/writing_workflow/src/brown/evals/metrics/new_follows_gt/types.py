"""Type definitions for the ground_truth evaluation metric.

This module contains Pydantic models and types used for evaluating articles
against ground truth content across six dimensions (core_content, flow,
structure, depth_enhancement, breadth_enhancement, core_preservation).
"""

from pathlib import Path

from brown.evals.metrics.base import (
    ArticleScores,
    BaseExample,
    BaseFewShotExamples,
    CriteriaScores,
    CriterionScore,
)


class FollowsGTCriteriaScores(CriteriaScores):
    """Represents scores for all six evaluation dimensions of a section.

    This model contains binary scores for a single section across the six
    dimensions used in ground-truth assessment (no mechanics dimension).

    Attributes:
        core_content: Score for substance match to GT.
        flow: Score for logical progression (adaptive to single-paragraph).
        structure: Score for internal formatting (adaptive to single-paragraph).
        depth_enhancement: Score for valuable depth additions from exploration.
        breadth_enhancement: Score for valuable breadth additions from exploration.
        core_preservation: Score for preserving GT core without dilution.
    """

    core_content: CriterionScore
    flow: CriterionScore
    structure: CriterionScore
    depth_enhancement: CriterionScore
    breadth_enhancement: CriterionScore
    core_preservation: CriterionScore


class FollowsGTArticleScores(ArticleScores[FollowsGTCriteriaScores]):
    """Article-level scores for the FollowsGT evaluation metric.

    This class represents the complete evaluation results for an article,
    containing scores for all sections across the six FollowsGT dimensions.
    """

    pass


class FollowsGTMetricExample(BaseExample):
    """Represents a single example for the ground_truth evaluation.

    Attributes:
        output: The generated article content.
        expected_output: The expected (ground-truth) article content.
        scores: The FollowsGTArticleScores associated with this example.
    """

    output: str
    expected_output: str
    scores: FollowsGTArticleScores

    @classmethod
    def from_markdown(cls, output_file: Path, expected_output_file: Path, scores: FollowsGTArticleScores) -> "FollowsGTMetricExample":
        """Create a FollowsGTMetricExample instance from markdown files.

        Args:
            output_file: Path to the generated article content.
            expected_output_file: Path to the expected article content.
            scores: The FollowsGTArticleScores associated with this example.

        Returns:
            An instance of FollowsGTMetricExample populated with content from files and scores.
        """
        output = output_file.read_text()
        expected_output = expected_output_file.read_text()

        return cls(output=output, expected_output=expected_output, scores=scores)

    def to_context(self) -> str:
        """Convert the example to a formatted string for use as context in prompts.

        Returns:
            A string representation of the example, including output, expected output, and scores.
        """
        return f"""
<output>
{self.output}
</output>
<expected_output>
{self.expected_output}
</expected_output>
{self.scores.to_context()}
"""


class FollowsGTMetricFewShotExamples(BaseFewShotExamples[FollowsGTMetricExample]):
    """Collection of few-shot examples for the FollowsGT evaluation metric.

    This class contains examples used for prompt engineering to guide the
    language model in evaluating articles against ground truth content.
    """

    pass
