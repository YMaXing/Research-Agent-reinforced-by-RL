"""Type definitions for the ground_truth evaluation metric.

This module contains Pydantic models and types used for evaluating articles
against ground truth content across five dimensions (core_content, flow,
structure, depth_enhancement, breadth_enhancement, core_preservation).
"""

from pathlib import Path

import pydantic

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
        depth_enhancement: Score for valuable depth additions from exploration (inward).
        breadth_enhancement: Score for valuable breadth additions from exploration (outward).
        core_preservation: Score for preserving GT core without dilution.
    """

    core_content: CriterionScore
    flow: CriterionScore
    structure: CriterionScore
    depth_enhancement: CriterionScore
    breadth_enhancement: CriterionScore
    core_preservation: CriterionScore

    def to_context(self) -> str:
        """Serialize the five pass-1 criteria only.

        core_preservation is excluded because it is evaluated in a dedicated
        second pass and must not appear in the pass-1 few-shot examples
        (SYSTEM_PROMPT no longer defines that criterion).
        """
        _PASS1_FIELDS = ("core_content", "flow", "structure", "depth_enhancement", "breadth_enhancement")
        scores_xml = ""
        for field_name in _PASS1_FIELDS:
            field_score = getattr(self, field_name)
            scores_xml += f"""    <{field_name}>
        <reason>{field_score.reason}</reason>
        <score>{field_score.score}</score>
    </{field_name}>
"""
        return scores_xml


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
        exploration_sources: Optional formatted string listing the exploration-phase
            sources available when the example was generated. When provided, the judge
            is expected to verify depth/breadth additions against these sources.
        scores: The FollowsGTArticleScores associated with this example.
    """

    output: str
    expected_output: str
    exploration_sources: str | None = None
    scores: FollowsGTArticleScores

    @classmethod
    def from_markdown(
        cls,
        output_file: Path,
        expected_output_file: Path,
        scores: FollowsGTArticleScores,
        exploration_sources: str | None = None,
    ) -> "FollowsGTMetricExample":
        """Create a FollowsGTMetricExample instance from markdown files.

        Args:
            output_file: Path to the generated article content.
            expected_output_file: Path to the expected article content.
            scores: The FollowsGTArticleScores associated with this example.
            exploration_sources: Optional formatted string of exploration-phase sources
                used to calibrate depth/breadth scoring in this example.

        Returns:
            An instance of FollowsGTMetricExample populated with content from files and scores.
        """
        output = output_file.read_text()
        expected_output = expected_output_file.read_text()

        return cls(
            output=output,
            expected_output=expected_output,
            exploration_sources=exploration_sources,
            scores=scores,
        )

    def to_context(self) -> str:
        """Convert the example to a formatted string for use as context in prompts.

        Returns:
            A string representation of the example, including output, expected output,
            optional exploration sources, and scores.
        """
        sources_block = f"\n<exploration_sources>\n{self.exploration_sources}\n</exploration_sources>" if self.exploration_sources else ""
        return f"""
<output>
{self.output}
</output>
<expected_output>
{self.expected_output}
</expected_output>{sources_block}
{self.scores.to_context()}
"""

    def to_core_preservation_context(self) -> str:
        """Convert the example to a formatted string for use in the pass-2 core preservation prompt.

        The format mirrors the CORE_PRESERVATION_PROMPT structure: enhancement scores first,
        then the articles, then the expected core_preservation judgments. This teaches the LLM
        how to evaluate CorePreservation given the already-determined depth/breadth scores.

        Returns:
            A string representation suitable for embedding as a few-shot example in
            get_core_preservation_prompt.
        """
        # Build enhancement scores block (same format as _build_section_scores_context)
        score_lines: list[str] = []
        for section in self.scores.sections:
            d = section.scores.depth_enhancement
            b = section.scores.breadth_enhancement
            score_lines.append(f'Section: "{section.title}"')
            score_lines.append(f'  depth_enhancement:   score={d.score}, reason="{d.reason}"')
            score_lines.append(f'  breadth_enhancement: score={b.score}, reason="{b.reason}"')
            score_lines.append("")
        enhancement_scores_text = "\n".join(score_lines)

        # Build expected core_preservation output XML
        cp_xml_parts: list[str] = []
        for section in self.scores.sections:
            cp = section.scores.core_preservation
            cp_xml_parts.append(
                f"    <section>\n"
                f"        <section_title>{section.title}</section_title>\n"
                f"        <core_preservation>\n"
                f"            <score>{cp.score}</score>\n"
                f"            <reason>{cp.reason}</reason>\n"
                f"        </core_preservation>\n"
                f"    </section>"
            )
        cp_xml = "\n".join(cp_xml_parts)

        return f"""<enhancement_scores>
{enhancement_scores_text}</enhancement_scores>
<output>
{self.output}
</output>
<expected_output>
{self.expected_output}
</expected_output>
<core_preservation_scores>
{cp_xml}
</core_preservation_scores>
"""


class FollowsGTMetricFewShotExamples(BaseFewShotExamples[FollowsGTMetricExample]):
    """Collection of few-shot examples for the FollowsGT evaluation metric.

    This class contains examples used for prompt engineering to guide the
    language model in evaluating articles against ground truth content.
    """

    def to_core_preservation_context(self) -> str:
        """Convert examples to a formatted string for the pass-2 core preservation prompt.

        Serializes each example using to_core_preservation_context(), which exposes the
        depth/breadth scores alongside the articles and expected core_preservation judgments.

        Returns:
            A string containing all examples formatted for insertion into CORE_PRESERVATION_PROMPT.
        """
        examples = "\n\n".join(
            [
                f"<example_{i + 1}>\n{example.to_core_preservation_context()}\n</example_{i + 1}>\n"
                for i, example in enumerate(self.examples)
            ]
        )
        return examples


class CorePreservationSectionScore(pydantic.BaseModel):
    """Core preservation score for a single section.

    Used as the response type for the second-pass core_preservation evaluation,
    where depth_enhancement and breadth_enhancement scores are provided explicitly
    as context so the LLM can build on them when grading core_preservation.

    Attributes:
        title: The title of the section, matching the title from the first pass.
        core_preservation: The core preservation score and reason for this section.
    """

    title: str = pydantic.Field(description="The title of the section being evaluated.")
    core_preservation: CriterionScore = pydantic.Field(description="The core preservation score for this section.")


class CorePreservationArticleScores(pydantic.BaseModel):
    """Article-level core preservation scores for all sections.

    Used as the structured-output response type for the second LLM call in the
    two-pass FollowsGT evaluation. Sections must be returned in the same order
    as they were listed in the prompt.

    Attributes:
        sections: One CorePreservationSectionScore per article section, in order.
    """

    sections: list[CorePreservationSectionScore] = pydantic.Field(
        description="Core preservation scores for each section, in the same order as the input."
    )
