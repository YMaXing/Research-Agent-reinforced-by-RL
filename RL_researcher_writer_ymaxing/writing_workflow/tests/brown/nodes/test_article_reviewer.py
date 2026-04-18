"""Tests for brown.nodes.article_reviewer module."""

import pytest

from brown.builders import build_model
from brown.config_app import get_app_config
from brown.entities.articles import Article, SelectedText
from brown.entities.guidelines import ArticleGuideline
from brown.entities.profiles import (
    ArticleProfile,
    ArticleProfiles,
    CharacterProfile,
    MechanicsProfile,
    StructureProfile,
    TerminologyProfile,
    TonalityProfile,
)
from brown.entities.research import Research
from brown.entities.reviews import ArticleReviews, HumanFeedback, Review, SelectedTextReviews
from brown.nodes.article_reviewer import ArticleReviewer


class TestArticleReviewer:
    """Test the ArticleReviewer class."""

    def test_article_reviewer_initialization(self) -> None:
        """Test creating reviewer."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(reviews=[Review(profile="test_profile", location="test_location", comment="This is a good article.")])

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        assert reviewer.model == model

    @pytest.mark.asyncio
    async def test_article_reviewer_ainvoke_success(self) -> None:
        """Test review generation with mocked response."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[
                Review(profile="test_profile", location="test_location", comment="This article is well-written and informative."),
                Review(profile="test_profile", location="test_location", comment="Could use more examples in section 2."),
            ]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        # Test input data
        article = Article(content="# Test Article\n\nThis is test content.")

        result = await reviewer.ainvoke()

        assert isinstance(result, ArticleReviews)
        assert len(result.reviews) == 2
        assert result.reviews[0].comment == "This article is well-written and informative."
        assert result.reviews[0].profile == "test_profile"
        assert result.reviews[1].comment == "Could use more examples in section 2."
        assert result.reviews[1].profile == "test_profile"

    @pytest.mark.asyncio
    async def test_article_reviewer_structured_output(self) -> None:
        """Test that reviewer returns structured output."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[Review(profile="test_profile", location="test_location", comment="Excellent article with clear structure.")]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        article = Article(content="# Test Article\n\nContent here.")

        result = await reviewer.ainvoke()

        # Verify structure
        assert isinstance(result, ArticleReviews)
        assert len(result.reviews) == 1

        review = result.reviews[0]
        assert hasattr(review, "comment")
        assert hasattr(review, "profile")
        assert hasattr(review, "location")
        assert isinstance(review.comment, str)
        assert isinstance(review.profile, str)
        assert isinstance(review.location, str)

    @pytest.mark.asyncio
    async def test_article_reviewer_empty_article(self) -> None:
        """Test reviewer with empty article."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[Review(profile="test_profile", location="test_location", comment="Article is too short and lacks content.")]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        result = await reviewer.ainvoke()

        assert isinstance(result, ArticleReviews)
        assert len(result.reviews) == 1
        assert "too short" in result.reviews[0].comment

    @pytest.mark.asyncio
    async def test_article_reviewer_multiple_reviews(self) -> None:
        """Test reviewer generating multiple reviews."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[
                Review(profile="test_profile", location="test_location", comment="Good introduction section."),
                Review(profile="test_profile", location="test_location", comment="Body section needs more detail."),
                Review(profile="test_profile", location="test_location", comment="Conclusion is well-written."),
            ]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        result = await reviewer.ainvoke()

        assert isinstance(result, ArticleReviews)
        assert len(result.reviews) == 3

        # Check that all reviews have valid structure
        for review in result.reviews:
            assert isinstance(review.comment, str)
            assert isinstance(review.profile, str)
            assert isinstance(review.location, str)
            assert len(review.comment) > 0

    def test_article_reviewer_requires_mocked_response_for_fake_model(self) -> None:
        """Test that fake model requires mocked response."""
        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        # Don't set responses - should use default

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        # Should not raise an error - fake model uses default response when mocked_response is None
        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        # Verify it was created successfully
        assert reviewer.model == model

    def test_article_reviewer_selected_text_initialization(self) -> None:
        """Test creating reviewer with selected text."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[Review(profile="test_profile", location="test_location", comment="This is a good selected text.")]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_selected_text")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        selected_text = SelectedText(article=article, content="Selected text content", first_line_number=10, last_line_number=15)
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=selected_text,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        assert reviewer.model == model
        assert reviewer.is_selected_text is True
        assert reviewer.is_article is False

    @pytest.mark.asyncio
    async def test_article_reviewer_selected_text_ainvoke(self) -> None:
        """Test review generation for selected text with mocked response."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[
                Review(profile="test_profile", location="test_location", comment="This selected text is well-written and informative."),
                Review(profile="test_profile", location="test_location", comment="Could use more examples in this section."),
            ]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_selected_text")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        selected_text = SelectedText(article=article, content="Selected text content", first_line_number=10, last_line_number=15)
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=selected_text,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )

        result = await reviewer.ainvoke()

        assert isinstance(result, SelectedTextReviews)
        assert result.article == article
        assert result.selected_text == selected_text
        assert len(result.reviews) == 2
        assert result.reviews[0].comment == "This selected text is well-written and informative."
        assert result.reviews[1].comment == "Could use more examples in this section."

    @pytest.mark.asyncio
    async def test_article_reviewer_selected_text_with_human_feedback(self) -> None:
        """Test selected text reviewer with human feedback."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[
                Review(profile="human_feedback", location="Selected text level", comment="Add more technical details to this section."),
                Review(profile="test_profile", location="test_location", comment="Good structure but needs more depth."),
            ]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_selected_text")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        selected_text = SelectedText(article=article, content="Selected text content", first_line_number=10, last_line_number=15)
        human_feedback = HumanFeedback(content="This section needs more technical depth")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        reviewer = ArticleReviewer(
            to_review=selected_text,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            human_feedback=human_feedback,
            model=model,
        )

        result = await reviewer.ainvoke()

        assert isinstance(result, SelectedTextReviews)
        assert result.article == article
        assert result.selected_text == selected_text
        assert len(result.reviews) == 2
        # Check that human feedback was processed
        human_feedback_reviews = [r for r in result.reviews if r.profile == "human_feedback"]
        assert len(human_feedback_reviews) == 1
        assert "technical details" in human_feedback_reviews[0].comment

    def test_article_reviewer_initialization_with_research(self) -> None:
        """Test that reviewer stores research when provided."""
        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )
        research = Research(content='<golden_source>Core</golden_source>\n\n<research_source phase="exploration">Insight</research_source>')

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            research=research,
            model=model,
        )

        assert reviewer.research == research

    @pytest.mark.asyncio
    async def test_article_reviewer_ainvoke_with_research(self) -> None:
        """Test that ainvoke completes successfully when research is provided with Format B exploration sources."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(
            reviews=[Review(profile="test_profile", location="test_location", comment="Exploration sources are well-integrated.")]
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )
        research = Research(content='<golden_source>Core</golden_source>\n\n<research_source phase="exploration">Insight</research_source>')

        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            research=research,
            model=model,
        )

        result = await reviewer.ainvoke()

        assert isinstance(result, ArticleReviews)
        assert len(result.reviews) == 1
        assert result.reviews[0].comment == "Exploration sources are well-integrated."

    def test_article_reviewer_article_property(self) -> None:
        """Test that article property returns correct article for both Article and SelectedText inputs."""
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(reviews=[Review(profile="test_profile", location="test_location", comment="Test comment")])

        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Test Article\n\nContent here.")
        selected_text = SelectedText(article=article, content="Selected text content", first_line_number=10, last_line_number=15)
        article_guideline = ArticleGuideline(content="Write a test article.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )

        # Test with Article input
        article_reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )
        assert article_reviewer.article == article

        # Test with SelectedText input
        selected_text_reviewer = ArticleReviewer(
            to_review=selected_text,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
        )
        assert selected_text_reviewer.article == article

    def test_article_reviewer_prompt_contains_word_count_exclusion_rule(self) -> None:
        """Reviewer prompt specifies that only prose text counts toward section word limits."""
        assert "count **only prose text**" in ArticleReviewer.system_prompt_template
        assert "Mermaid diagram code blocks" in ArticleReviewer.system_prompt_template
        assert "code blocks" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_enforces_word_count_per_section(self) -> None:
        """Reviewer prompt enforces word-count constraints at the individual section level and
        the Chain of Thoughts contains a dedicated per-section prose-count pass.
        """
        assert "individual section level" in ArticleReviewer.system_prompt_template
        assert "A section that is too short may not borrow words from adjacent sections" in ArticleReviewer.system_prompt_template
        # Chain of Thoughts must name per-section check step
        assert "Per-section word-count check" in ArticleReviewer.system_prompt_template
        assert "Each section is evaluated independently" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_no_length_violation_for_code_heavy_sections(self) -> None:
        """Reviewer prompt instructs not to flag length violations caused by code, media, or captions."""
        assert "Do not raise a length-violation review" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_prose_below_minimum(self) -> None:
        """Reviewer prompt must flag prose shortfalls; a ±10% tolerance is used,
        so prose falling more than that tolerance below the target is flagged.
        """
        assert "never compensate for" in ArticleReviewer.system_prompt_template
        assert "below the stated target" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_prose_above_maximum(self) -> None:
        """Reviewer prompt must also flag sections exceeding the stated target by more than
        the ±10% tolerance — both over-length and under-length are enforced.
        """
        assert "exceeds the stated" in ArticleReviewer.system_prompt_template
        assert "trimmed" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_labeled_bullet_artifacts(self) -> None:
        """Reviewer must detect and flag sections where the writer reproduced the guideline's
        labeled bullet-point structural artifacts instead of expanding them into narrative prose.
        """
        assert "content-expansion" in ArticleReviewer.system_prompt_template
        assert "content expansion compliance" in ArticleReviewer.system_prompt_template
        assert "flowing prose that integrates the content naturally" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_uncited_first_person_anecdotes(self) -> None:
        """Reviewer must flag first-person anecdotes written in 'we' voice that are traceable
        to a research source but lack a citation — they are indistinguishable from hallucinations.
        """
        assert "First-person anecdotes require citations" in ArticleReviewer.system_prompt_template
        assert "uncited first-person narrative drawn from research is indistinguishable" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_contains_enumeration_completeness_check(self) -> None:
        """Reviewer prompt must instruct the reviewer to verify that every numbered item
        (0, 1, 2, 3…) in the guideline produced a corresponding H3 subsection, including
        item '0' which must not be treated as an introductory paragraph.
        """
        assert "Enumeration completeness" in ArticleReviewer.system_prompt_template
        assert 'Item "0" is the first peer content' in ArticleReviewer.system_prompt_template
        assert "missing its own H3 subsection" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_kind1_kind2_classification(self) -> None:
        """Reviewer prompt defines Kind 1 (outline directives — flag) and Kind 2 (verbatim
        artifacts — do not flag) to prevent false-positive content-expansion reviews on
        code blocks, labeled example prompts, and labeled example outputs.
        """
        assert "Kind 1 — Outline directives" in ArticleReviewer.system_prompt_template
        assert "Kind 2 — Verbatim artifacts" in ArticleReviewer.system_prompt_template
        assert "must NOT be flagged as content-expansion violations" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_h3_number_prefixes(self) -> None:
        """Reviewer prompt instructs flagging H3 headings that include a leading number
        prefix derived from the guideline's list numbering.
        """
        assert "H3 heading number prefixes" in ArticleReviewer.system_prompt_template
        assert "position marker only" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_shared_setup_subsection(self) -> None:
        """Reviewer prompt instructs checking for a dedicated `### Setup` subsection
        when golden-source research contains shared setup code.
        """
        assert "Shared setup subsection" in ArticleReviewer.system_prompt_template
        assert "### Setup" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_intro_standalone_list(self) -> None:
        """Reviewer prompt instructs flagging a standalone bulleted or numbered list
        at the end of the introduction that previews what will be covered.
        """
        assert "Introduction standalone list" in ArticleReviewer.system_prompt_template
        assert "sentence-level enumeration" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_flags_references_numbered_format(self) -> None:
        """Reviewer prompt instructs flagging the References section if it uses a
        numbered list format instead of the correct bulleted format.
        """
        assert "References section format" in ArticleReviewer.system_prompt_template
        assert "- [N] [Title or short description](url)" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_cot_word_count_excludes_citation_markers(self) -> None:
        """Reviewer Chain of Thoughts step 5b must list inline citation markers as an
        exclusion from the prose word count, consistent with the writer's definition.
        """
        assert "[[N]](url)" in ArticleReviewer.system_prompt_template
        assert "inline citation markers" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_prompt_includes_media_items_section(self) -> None:
        """Reviewer system prompt must include a {media_items} placeholder so the reviewer
        can verify that pre-generated media items were placed in their declared sections.
        """
        assert "{media_items}" in ArticleReviewer.system_prompt_template
        assert "pre-generated media items" in ArticleReviewer.system_prompt_template

    def test_article_reviewer_accepts_media_items_kwarg(self) -> None:
        """ArticleReviewer.__init__ must accept an optional media_items parameter."""
        from brown.entities.media_items import MediaItems
        from brown.nodes.article_reviewer import ReviewsOutput

        mock_response = ReviewsOutput(reviews=[])
        app_config = get_app_config()
        model, _ = build_model(app_config, node="review_article")
        model.responses = [mock_response.model_dump_json()]

        article = Article(content="# Title\n\n## Section\n\nContent.")
        article_guideline = ArticleGuideline(content="Write about topic X.")
        article_profiles = ArticleProfiles(
            character=CharacterProfile(name="test", content="Test character"),
            article=ArticleProfile(name="test", content="Test article"),
            structure=StructureProfile(name="test", content="Test structure"),
            mechanics=MechanicsProfile(name="test", content="Test mechanics"),
            terminology=TerminologyProfile(name="test", content="Test terminology"),
            tonality=TonalityProfile(name="test", content="Test tonality"),
        )
        reviewer = ArticleReviewer(
            to_review=article,
            article_guideline=article_guideline,
            article_profiles=article_profiles,
            model=model,
            media_items=MediaItems.build(),
        )
        assert reviewer.media_items is not None

    def test_article_reviewer_selected_text_preserves_reviewing_rules(self) -> None:
        """Selected-text chain of thoughts replaces the reviewing workflow but explicitly
        preserves all Reviewing Rules from the system prompt.
        """
        assert "continue to apply all Reviewing Rules" in ArticleReviewer.selected_text_system_prompt_template
