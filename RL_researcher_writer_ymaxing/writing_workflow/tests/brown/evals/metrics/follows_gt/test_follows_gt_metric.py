import pytest

from brown.evals.metrics.base import CriterionScore, SectionCriteriaScores
from brown.evals.metrics.new_follows_gt import prompts as follows_gt_prompts
from brown.evals.metrics.new_follows_gt.metric import FollowsGTMetric
from brown.evals.metrics.new_follows_gt.types import (
    FollowsGTArticleScores,
    FollowsGTCriteriaScores,
)
from brown.models import ModelConfig, SupportedModels


@pytest.fixture
def mock_article_scores_perfect() -> FollowsGTArticleScores:
    """
    Fixture for a perfect FollowsGTArticleScores response.
    """
    return FollowsGTArticleScores(
        sections=[
            SectionCriteriaScores(
                title="Introduction",
                scores=FollowsGTCriteriaScores(
                    core_content=CriterionScore(score=1, reason="Perfect core content."),
                    flow=CriterionScore(score=1, reason="Perfect flow."),
                    structure=CriterionScore(score=1, reason="Perfect structure."),
                    depth_enhancement=CriterionScore(score=1, reason="Perfect depth enhancement."),
                    breadth_enhancement=CriterionScore(score=1, reason="Perfect breadth enhancement."),
                    core_preservation=CriterionScore(score=1, reason="Perfect core preservation."),
                ),
            ),
            SectionCriteriaScores(
                title="Body",
                scores=FollowsGTCriteriaScores(
                    core_content=CriterionScore(score=1, reason="Perfect core content."),
                    flow=CriterionScore(score=1, reason="Perfect flow."),
                    structure=CriterionScore(score=1, reason="Perfect structure."),
                    depth_enhancement=CriterionScore(score=1, reason="Perfect depth enhancement."),
                    breadth_enhancement=CriterionScore(score=1, reason="Perfect breadth enhancement."),
                    core_preservation=CriterionScore(score=1, reason="Perfect core preservation."),
                ),
            ),
        ]
    )


@pytest.fixture
def mock_article_scores_mixed() -> FollowsGTArticleScores:
    """
    Fixture for a mixed FollowsGTArticleScores response.
    """
    return FollowsGTArticleScores(
        sections=[
            SectionCriteriaScores(
                title="Introduction",
                scores=FollowsGTCriteriaScores(
                    core_content=CriterionScore(score=0, reason="Bad core content."),
                    flow=CriterionScore(score=1, reason="Good flow."),
                    structure=CriterionScore(score=0, reason="Bad structure."),
                    depth_enhancement=CriterionScore(score=1, reason="Good depth enhancement."),
                    breadth_enhancement=CriterionScore(score=0, reason="Bad breadth enhancement."),
                    core_preservation=CriterionScore(score=1, reason="Good core preservation."),
                ),
            ),
            SectionCriteriaScores(
                title="Body",
                scores=FollowsGTCriteriaScores(
                    core_content=CriterionScore(score=1, reason="Good core content."),
                    flow=CriterionScore(score=0, reason="Bad flow."),
                    structure=CriterionScore(score=1, reason="Good structure."),
                    depth_enhancement=CriterionScore(score=0, reason="Bad depth enhancement."),
                    breadth_enhancement=CriterionScore(score=1, reason="Good breadth enhancement."),
                    core_preservation=CriterionScore(score=0, reason="Bad core preservation."),
                ),
            ),
        ]
    )


@pytest.fixture
def mock_article_scores_empty_sections() -> FollowsGTArticleScores:
    """
    Fixture for a FollowsGTArticleScores response with empty sections.
    """
    return FollowsGTArticleScores(sections=[])


@pytest.fixture
def mock_article_metric(mock_article_scores_perfect: FollowsGTArticleScores) -> FollowsGTMetric:
    """
    Fixture for a FollowsGTMetric instance with a mocked perfect response.
    """
    model_config = ModelConfig(mocked_response=mock_article_scores_perfect)
    return FollowsGTMetric(model=SupportedModels.FAKE_MODEL, model_config=model_config)


@pytest.fixture
def mock_article_metric_mixed(mock_article_scores_mixed: FollowsGTArticleScores) -> FollowsGTMetric:
    """
    Fixture for a FollowsGTMetric instance with a mocked mixed response.
    """
    model_config = ModelConfig(mocked_response=mock_article_scores_mixed)
    return FollowsGTMetric(model=SupportedModels.FAKE_MODEL, model_config=model_config)


@pytest.fixture
def mock_article_metric_empty_sections(mock_article_scores_empty_sections: FollowsGTArticleScores) -> FollowsGTMetric:
    """
    Fixture for a FollowsGTMetric instance with a mocked empty sections response.
    """
    model_config = ModelConfig(mocked_response=mock_article_scores_empty_sections)
    return FollowsGTMetric(model=SupportedModels.FAKE_MODEL, model_config=model_config)


def test_article_metric_perfect_score(mock_article_metric: FollowsGTMetric) -> None:
    """
    Test that FollowsGTMetric returns perfect scores when mocked with a perfect response.
    """
    output = "This is a well-written article."
    expected_output = "This is the ideal article."

    results = mock_article_metric.score(output=output, expected_output=expected_output)

    assert isinstance(results, list) and len(results) == 6
    for result in results:
        assert result.value == 1.0
        assert result.name.startswith("ground_truth_")


def test_article_metric_mixed_scores(mock_article_metric_mixed: FollowsGTMetric) -> None:
    """
    Test that FollowsGTMetric returns mixed scores when mocked with a mixed response.
    """
    output = "This article has some issues."
    expected_output = "This is the ideal article."

    results = mock_article_metric_mixed.score(output=output, expected_output=expected_output)

    assert isinstance(results, list) and len(results) == 6

    # Expected averages for mixed scores across 2 sections — each criterion averages to (0+1)/2 = 0.5
    for result in results:
        assert result.value == 0.5
        assert result.name.startswith("ground_truth_")


def test_article_metric_empty_sections(mock_article_metric_empty_sections: FollowsGTMetric) -> None:
    """
    Test that FollowsGTMetric handles empty sections gracefully (should return empty list).
    """
    output = ""
    expected_output = ""

    results = mock_article_metric_empty_sections.score(output=output, expected_output=expected_output)
    assert isinstance(results, list) and len(results) == 0  # Empty sections return empty list


def test_article_metric_init_requires_mocked_response_for_fake_model() -> None:
    """
    Test that FollowsGTMetric raises an AssertionError if FAKE_MODEL is used without a mocked_response.
    """
    with pytest.raises(AssertionError, match="Mocked response is required for fake model"):
        model_config = ModelConfig(mocked_response=None)
        FollowsGTMetric(model=SupportedModels.FAKE_MODEL, model_config=model_config)


def test_article_metric_init_default_model() -> None:
    """
    Test that FollowsGTMetric initializes with the default model if not specified.
    """
    metric = FollowsGTMetric()
    assert metric.model == SupportedModels.GOOGLE_GEMINI_25_FLASH


def test_article_metric_init_custom_name() -> None:
    """
    Test that FollowsGTMetric initializes with a custom name.
    """
    custom_name = "my_custom_follows_gt_metric"
    metric = FollowsGTMetric(name=custom_name)
    assert metric.name == custom_name


# ---------------------------------------------------------------------------
# Prompt-content tests
# Verify that key rules introduced during prompt engineering are present in
# SYSTEM_PROMPT so regressions are caught if the prompt is edited carelessly.
# ---------------------------------------------------------------------------


def test_system_prompt_contains_h1_exclusion() -> None:
    """
    The Structure criterion must exclude the article-level H1 title from the
    headers-formatting check.
    """
    assert "H1" in follows_gt_prompts.SYSTEM_PROMPT
    assert "article title" in follows_gt_prompts.SYSTEM_PROMPT


def test_system_prompt_contains_structure_filtering_procedure() -> None:
    """
    The Structure criterion must document the paragraph-length filtering
    procedure: step over accepted additions before evaluating GT paragraph
    patterns.
    """
    assert "stepping over the additions" in follows_gt_prompts.SYSTEM_PROMPT
    assert "not a structure failure" in follows_gt_prompts.SYSTEM_PROMPT


def test_system_prompt_contains_flow_filtering_procedure() -> None:
    """
    The Flow criterion must document the filtering procedure for sections
    that contain complementary additions interspersed with GT ideas.
    """
    assert "filtering procedure" in follows_gt_prompts.SYSTEM_PROMPT
    assert "stepping over" in follows_gt_prompts.SYSTEM_PROMPT


def test_system_prompt_contains_bridgeless_gap_caveat() -> None:
    """
    The Flow criterion must include the bridgeless-gap exception: an absent
    idea that leaves an abrupt transition between surrounding ideas is a
    legitimate Flow=0 reason.
    """
    assert "bridgeless gap" in follows_gt_prompts.SYSTEM_PROMPT


def test_system_prompt_contains_non_qualifying_addition_flow_rule() -> None:
    """
    The Flow accepted-differences bullet must state that non-qualifying
    additions (depth=0 AND breadth=0) are not covered by the accepted-
    difference rule, and that a disproportionately long non-qualifying
    addition constitutes a Flow=0 failure.
    """
    assert "non-qualifying addition" in follows_gt_prompts.SYSTEM_PROMPT
    assert "Flow=0" in follows_gt_prompts.SYSTEM_PROMPT


def test_system_prompt_contains_non_qualifying_addition_core_preservation_rule() -> None:
    """
    The WHAT TO AVOID section must state that non-qualifying additions must
    not trigger CorePreservation=0 and that their penalty belongs to Flow.
    """
    assert "CorePreservation=0" in follows_gt_prompts.SYSTEM_PROMPT
    assert "belongs exclusively to Flow" in follows_gt_prompts.SYSTEM_PROMPT


def test_system_prompt_flow_does_not_own_missing_topics() -> None:
    """
    The Flow criterion must explicitly state that missing topics are handled
    by CoreContent, not Flow.
    """
    assert "Do not score Flow=0 for missing topics or ideas" in follows_gt_prompts.SYSTEM_PROMPT


# ---------------------------------------------------------------------------
# get_eval_prompt rendering tests
# ---------------------------------------------------------------------------


def test_get_eval_prompt_injects_output_and_expected_output() -> None:
    """
    get_eval_prompt must embed the output and expected_output strings verbatim
    in the rendered prompt.
    """
    output = "GENERATED_ARTICLE_CONTENT"
    expected_output = "EXPECTED_ARTICLE_CONTENT"
    rendered = follows_gt_prompts.get_eval_prompt(
        output=output,
        expected_output=expected_output,
        few_shot_examples=follows_gt_prompts.DEFAULT_FEW_SHOT_EXAMPLES,
    )
    assert output in rendered
    assert expected_output in rendered


def test_get_eval_prompt_injects_few_shot_examples() -> None:
    """
    get_eval_prompt must embed the serialised few-shot examples in the
    rendered prompt (i.e. the {examples} placeholder is substituted).
    """
    rendered = follows_gt_prompts.get_eval_prompt(
        output="output",
        expected_output="expected",
        few_shot_examples=follows_gt_prompts.DEFAULT_FEW_SHOT_EXAMPLES,
    )
    # The examples context should not leave the raw placeholder behind.
    assert "{examples}" not in rendered
    # At least one of the known example section titles must appear.
    assert "Why Structured Outputs Are Critical" in rendered


def test_get_eval_prompt_no_unfilled_placeholders() -> None:
    """
    The rendered prompt must contain none of the three known template
    placeholders ({examples}, {output}, {expected_output}) in their
    raw, unsubstituted form.
    """
    rendered = follows_gt_prompts.get_eval_prompt(
        output="output",
        expected_output="expected",
        few_shot_examples=follows_gt_prompts.DEFAULT_FEW_SHOT_EXAMPLES,
    )
    for placeholder in ("{examples}", "{output}", "{expected_output}"):
        assert placeholder not in rendered, f"Unfilled placeholder found: {placeholder}"


# ---------------------------------------------------------------------------
# Scoring behaviour: core_preservation default-1 path
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_article_scores_no_enhancements() -> FollowsGTArticleScores:
    """
    Fixture where both enhancement scores are 0 and core_preservation is 1
    (the default path when there are no qualifying depth/breadth additions).
    """
    return FollowsGTArticleScores(
        sections=[
            SectionCriteriaScores(
                title="Introduction",
                scores=FollowsGTCriteriaScores(
                    core_content=CriterionScore(score=1, reason="All GT ideas present."),
                    flow=CriterionScore(score=1, reason="Correct order and transitions."),
                    structure=CriterionScore(score=1, reason="Matching structure."),
                    depth_enhancement=CriterionScore(score=0, reason="No depth additions."),
                    breadth_enhancement=CriterionScore(score=0, reason="No breadth additions."),
                    core_preservation=CriterionScore(score=1, reason="Default 1: no qualifying additions to evaluate."),
                ),
            ),
        ]
    )


def test_core_preservation_default_one_scores_correctly(
    mock_article_scores_no_enhancements: FollowsGTArticleScores,
) -> None:
    """
    When both depth_enhancement and breadth_enhancement are 0, core_preservation
    defaults to 1. The metric must return 1.0 for core_preservation in that case.
    """
    model_config = ModelConfig(mocked_response=mock_article_scores_no_enhancements)
    metric = FollowsGTMetric(model=SupportedModels.FAKE_MODEL, model_config=model_config)

    results = metric.score(output="output", expected_output="expected")

    core_preservation_result = next(r for r in results if "core_preservation" in r.name)
    assert core_preservation_result.value == 1.0
