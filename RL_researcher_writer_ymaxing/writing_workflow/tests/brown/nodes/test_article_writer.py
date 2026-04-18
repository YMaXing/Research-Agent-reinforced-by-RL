"""Tests for brown.nodes.article_writer module."""

import pytest

from brown.builders import build_model
from brown.config_app import get_app_config
from brown.entities.articles import Article, ArticleExamples, SelectedText
from brown.entities.guidelines import ArticleGuideline
from brown.entities.media_items import MediaItems
from brown.entities.profiles import ArticleProfiles
from brown.entities.research import Research
from brown.entities.reviews import ArticleReviews, Review, SelectedTextReviews
from brown.nodes.article_writer import ArticleWriter


class TestArticleWriter:
    """Test the ArticleWriter class."""

    def test_article_writer_initialization(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test creating writer with fake model."""
        mock_response = {
            "content": """
# Mock Title
### Mock Subtitle

Mock intro.

## Section 1
Mock section 1.

## Section 2
Mock section 2.

## Section 3
Mock section 3.

## Conclusion
Mock conclusion.

## References
Mock references.
"""
        }

        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        assert writer.model == model

    @pytest.mark.asyncio
    async def test_article_writer_ainvoke_success(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test article generation with mocked response."""
        mock_response = '{"content": "# Generated Article\\n### Mock Subtitle\\n\\nThis is a generated article about AI.\\n\\n## Section 1\\nMock section 1.\\n\\n## Section 2\\nMock section 2.\\n\\n## Section 3\\nMock section 3.\\n\\n## Conclusion\\nMock conclusion.\\n\\n## References\\nMock references.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, Article)
        assert "# Generated Article" in result.content

    @pytest.mark.asyncio
    async def test_article_writer_with_media_items(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test article generation with media items."""
        mock_response = '{"content": "# Article with Media\\n### Mock Subtitle\\n\\nThis article includes diagrams.\\n\\n## Section 1\\nMock section 1.\\n\\n## Section 2\\nMock section 2.\\n\\n## Section 3\\nMock section 3.\\n\\n## Conclusion\\nMock conclusion.\\n\\n## References\\nMock references.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        from brown.entities.media_items import MermaidDiagram

        media_items = MediaItems(
            media_items=[MermaidDiagram(location="Introduction", content="graph TD\n    A --> B", caption="Test diagram")]
        )

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, Article)
        assert "Article with Media" in result.content

    @pytest.mark.asyncio
    async def test_article_writer_with_reviews(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test article generation with reviews (editing mode)."""
        mock_response = '{"content": "# Revised Article\\n### Mock Subtitle\\n\\nThis is a revised article based on reviews.\\n\\n## Section 1\\nMock section 1.\\n\\n## Section 2\\nMock section 2.\\n\\n## Section 3\\nMock section 3.\\n\\n## Conclusion\\nMock conclusion.\\n\\n## References\\nMock references.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        reviews = ArticleReviews(
            article=Article(content="Test article"),
            reviews=[Review(profile="test_profile", location="test_location", comment="Needs improvement")],
        )

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=reviews,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, Article)
        assert "Revised Article" in result.content

    @pytest.mark.asyncio
    async def test_article_writer_empty_input(
        self,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test article writer with empty input."""
        mock_response = '{"content": "# Mock Title\\n### Mock Subtitle\\n\\nEmpty article\\n\\n## Section 1\\nMock section 1.\\n\\n## Section 2\\nMock section 2.\\n\\n## Section 3\\nMock section 3.\\n\\n## Conclusion\\nMock conclusion.\\n\\n## References\\nMock references.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        article_guideline = ArticleGuideline(content="")
        research = Research(content="")

        writer = ArticleWriter(
            article_guideline=article_guideline,
            research=research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, Article)
        # The mocked response will return the default mocked article content
        # The exact content depends on the mocked responses in the ArticleWriter node

    def test_article_writer_requires_mocked_response_for_fake_model(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test that fake model requires mocked response."""
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        # Don't set responses - should use default

        # The mocked response will return the default mocked article content
        # The exact content depends on the mocked responses in the ArticleWriter node
        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        assert writer.model == model

    def test_article_writer_prompt_contains_word_count_exclusion_rule(self) -> None:
        """Prompt specifies that only prose text counts toward section word limits."""
        assert "count **only prose text**" in ArticleWriter.system_prompt_template
        assert "Mermaid diagram code blocks" in ArticleWriter.system_prompt_template
        assert "code blocks" in ArticleWriter.system_prompt_template
        assert "Captions for diagrams" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_enforces_word_count_per_section(self) -> None:
        """Prompt enforces word-count constraints at the individual section level, not as an
        article-wide total, and the Verification step requires a per-section prose count check
        before the article is returned. A ±50-word tolerance applies on both ends.
        """
        assert "individual section level" in ArticleWriter.system_prompt_template
        assert "A section that is too short may not borrow words from adjacent sections" in ArticleWriter.system_prompt_template
        # Verification checklist must name per-section check explicitly
        assert "independently tally the prose-only word count of that section" in ArticleWriter._verification_checklist
        assert "Sections are checked one by one" in ArticleWriter._verification_checklist
        # Tolerance is now ±10% with minimum ±25 words
        assert "\u00b110%" in ArticleWriter._verification_checklist  # ± symbol
        assert "minimum" in ArticleWriter._verification_checklist
        assert "\u00b125 words" in ArticleWriter._verification_checklist

    def test_article_writer_prompt_item_zero_is_h3_subsection(self) -> None:
        """Prompt clarifies that item '0' in a numbered guideline list is the first peer H3
        subsection, not an introductory paragraph, so setup/config code is never omitted.
        """
        assert 'Item "0" is not a preamble' in ArticleWriter.system_prompt_template
        assert "first peer content entry" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_contains_inline_table_fallback_rule(self) -> None:
        """Prompt instructs writer to produce a Markdown table inline for comparison content
        when no pre-generated media item covers that section."""
        assert "produce a Markdown table" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_no_mermaid_for_comparison_data(self) -> None:
        """Prompt explicitly forbids Mermaid diagrams for structured 2D comparison data."""
        assert "Do **not** produce a Mermaid diagram for structured" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_contains_citation_rule(self) -> None:
        """Writing Requirements section includes a mandatory citation rule."""
        assert "**Citations:**" in ArticleWriter.system_prompt_template
        assert "[[N]](url)" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_first_person_anecdote_requires_citation(self) -> None:
        """First-person anecdotes adapted from research into 'we' voice must still be cited;
        rewriting content into the course voice does not make it uncitable.
        """
        assert "First-person anecdotes are not exempt" in ArticleWriter.system_prompt_template
        assert "indistinguishable from a hallucination" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_verification_scans_for_labeled_bullet_artifacts(self) -> None:
        """Verification step must explicitly instruct the writer to scan every paragraph opener
        for bold-label patterns from guideline structural artifacts and rewrite them as flowing
        prose before returning — closing the self-correction loop for format-copying issues.
        """
        assert "Scan every paragraph opener for bold-label patterns" in ArticleWriter._verification_checklist
        assert "rewrite those paragraphs as flowing prose" in ArticleWriter._verification_checklist

    def test_article_writer_prompt_kind1_kind2_classification(self) -> None:
        """Prompt defines Kind 1 (outline directives to expand) and Kind 2 (verbatim artifacts
        to reproduce) so the writer knows which guideline content to rewrite vs. preserve.
        """
        assert "Kind 1 — Outline directives" in ArticleWriter.system_prompt_template
        assert "Kind 2 — Verbatim artifacts" in ArticleWriter.system_prompt_template
        assert "Important exclusion" in ArticleWriter.system_prompt_template

    def test_article_writer_verification_strips_h3_number_prefixes(self) -> None:
        """Verification checklist instructs the writer to remove leading number prefixes
        from H3 headings (e.g., `### 1.` becomes `###`).
        """
        assert "Scan all H3 headings for leading number prefixes" in ArticleWriter._verification_checklist
        assert "remove the number and period" in ArticleWriter._verification_checklist

    def test_article_writer_verification_rewrites_intro_standalone_list(self) -> None:
        """Verification checklist instructs the writer to rewrite any standalone bulleted or
        numbered list in the introduction's closing paragraph as an inline enumeration.
        """
        assert "introduction's closing paragraph for a standalone bulleted or numbered list" in ArticleWriter._verification_checklist
        assert "inline sentence-level enumeration" in ArticleWriter._verification_checklist

    def test_article_writer_verification_fixes_references_format(self) -> None:
        """Verification checklist and Writing Requirements both enforce bulleted reference format."""
        assert "References section format" in ArticleWriter.system_prompt_template
        assert "Do NOT use a numbered list" in ArticleWriter.system_prompt_template
        assert "bulleted list item following" in ArticleWriter._verification_checklist

    def test_article_writer_prompt_shared_setup_subsection(self) -> None:
        """Article Outline rules instruct the writer to create a dedicated `### Setup` subsection
        for shared setup code from golden-source notebooks.
        """
        assert "Shared setup code (notebook-sourced)" in ArticleWriter.system_prompt_template
        assert "### Setup" in ArticleWriter.system_prompt_template

    def test_article_writer_prompt_guideline_priority_exception(self) -> None:
        """The 'never deviate' rule acknowledges that the article_guideline takes priority
        when it explicitly conflicts with other rules.
        """
        assert "article_guideline> explicitly provides a conflicting instruction" in ArticleWriter.system_prompt_template
        assert "article_guideline> takes priority" in ArticleWriter.system_prompt_template

    def test_article_writer_verification_shared_between_core_and_exploration(self) -> None:
        """The same _verification_checklist is injected into both the core system prompt
        and the exploration integration prompt so both passes run identical quality gates.
        """
        assert "{_verification_checklist}" in ArticleWriter.system_prompt_template
        assert "{_verification_checklist}" in ArticleWriter.exploration_integration_prompt_template

    def test_article_writer_review_prompt_preserves_verification(self) -> None:
        """Review prompts replace the writing workflow but explicitly preserve the Verification
        checklist from the system prompt.
        """
        assert "continue to apply the **Verification** checklist" in ArticleWriter.article_reviews_prompt_template
        assert "continue to apply the **Verification** checklist" in ArticleWriter.selected_text_reviews_prompt_template

    def test_article_writer_exploration_prompt_contains_mandatory_citation_rule(self) -> None:
        """Exploration integration prompt contains the mandatory citation rule for exploration sources."""
        assert "Citations (mandatory)" in ArticleWriter.exploration_integration_prompt_template
        assert "[[N]](url)" in ArticleWriter.exploration_integration_prompt_template

    @pytest.mark.asyncio
    async def test_article_writer_with_selected_text_reviews(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test article writer with selected text reviews returns SelectedText."""
        mock_response = '{"content": "## Mock Section Title\\n\\nMock selected text content that has been edited based on the human feedback and reviews.\\n\\nThis is the edited version of the selected text that addresses the specific issues identified in the reviews while\\nincorporating the human feedback.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        article = Article(content="Test article")
        selected_text = SelectedText(article=article, content="Original selected text", first_line_number=10, last_line_number=15)
        reviews = SelectedTextReviews(
            article=article,
            selected_text=selected_text,
            reviews=[Review(profile="test_profile", location="test_location", comment="Needs improvement")],
        )

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=reviews,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, SelectedText)
        assert result.article == article
        assert result.first_line_number == 10
        assert result.last_line_number == 15
        assert "Mock selected text content" in result.content

    @pytest.mark.asyncio
    async def test_article_writer_selected_text_preserves_line_numbers(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test that line numbers are preserved in selected text output."""
        mock_response = '{"content": "## Mock Section Title\\n\\nCompletely rewritten content that has been edited based on the human feedback and reviews.\\n\\nThis is the edited version of the selected text that addresses the specific issues identified in the reviews while\\nincorporating the human feedback.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        article = Article(content="Test article")
        selected_text = SelectedText(article=article, content="Original selected text", first_line_number=25, last_line_number=40)
        reviews = SelectedTextReviews(
            article=article,
            selected_text=selected_text,
            reviews=[Review(profile="test_profile", location="test_location", comment="Rewrite completely")],
        )

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=reviews,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, SelectedText)
        assert result.article == article
        assert result.first_line_number == 25
        assert result.last_line_number == 40
        assert "Completely rewritten content" in result.content

    @pytest.mark.asyncio
    async def test_article_writer_selected_text_vs_article_output(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test that ArticleWriter returns correct type based on review type."""
        mock_response = '{"content": "# Mock Title\\n### Mock Subtitle\\n\\nMock content based on review type.\\n"}'
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        article = Article(content="Test article")
        selected_text = SelectedText(article=article, content="Original selected text", first_line_number=10, last_line_number=15)

        # Test with ArticleReviews - should return Article
        article_reviews = ArticleReviews(
            article=article,
            reviews=[Review(profile="test_profile", location="test_location", comment="Article needs improvement")],
        )

        article_writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=article_reviews,
            model=model,
        )

        article_result = await article_writer.ainvoke()
        assert isinstance(article_result, Article)
        assert "Mock Title" in article_result.content

        # Test with SelectedTextReviews - should return SelectedText
        selected_text_reviews = SelectedTextReviews(
            article=article,
            selected_text=selected_text,
            reviews=[Review(profile="test_profile", location="test_location", comment="Selected text needs improvement")],
        )

        selected_text_writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=selected_text_reviews,
            model=model,
        )

        selected_text_result = await selected_text_writer.ainvoke()
        assert isinstance(selected_text_result, SelectedText)
        assert selected_text_result.article == article
        assert selected_text_result.first_line_number == 10
        assert selected_text_result.last_line_number == 15

    @pytest.mark.asyncio
    async def test_article_writer_selected_text_content(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_research: Research,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Test that selected text content is properly extracted and returned."""
        mock_response = '{"content": "## Enhanced Section\\n\\nThis is the enhanced selected text content with more technical details and examples.\\n\\nThe content has been significantly improved based on the feedback provided.\\n"}'  # noqa: E501
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        article = Article(content="Test article")
        selected_text = SelectedText(article=article, content="Original selected text", first_line_number=5, last_line_number=12)
        reviews = SelectedTextReviews(
            article=article,
            selected_text=selected_text,
            reviews=[Review(profile="test_profile", location="test_location", comment="Add technical details")],
        )

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=mock_research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=reviews,
            model=model,
        )

        result = await writer.ainvoke()

        assert isinstance(result, SelectedText)
        assert result.article == article
        assert "Enhanced Section" in result.content
        assert "technical details and examples" in result.content
        assert "significantly improved" in result.content

    # ------------------------------------------------------------------ #
    # Verification checklist — word-count & trim order tests              #
    # ------------------------------------------------------------------ #

    def test_verification_checklist_word_count_exclusion_list_complete(self) -> None:
        """The verification checklist excludes all five non-prose categories from word counts."""
        checklist = ArticleWriter._verification_checklist
        assert "code blocks" in checklist
        assert "Mermaid" in checklist
        assert "table cell text" in checklist
        assert "captions" in checklist
        assert "citation markers" in checklist or "[[N]](url)" in checklist

    def test_verification_checklist_tolerance_is_percentage_based(self) -> None:
        """Tolerance uses ±10% (min ±25 words), not a fixed ±50 words."""
        checklist = ArticleWriter._verification_checklist
        assert "±10%" in checklist
        assert "±25 words" in checklist
        # Old ±50 must not appear
        assert "50 words below" not in checklist
        assert "50 words above" not in checklist

    def test_verification_checklist_trim_priority_order(self) -> None:
        """5-step trim priority order: exploration-only → over-explained → transitions → wordy → weakest."""
        checklist = ArticleWriter._verification_checklist
        # All five steps must be present, in numbered order
        assert "1. **Remove exploration-only sentences first.**" in checklist
        assert "2. **Shorten over-explained examples.**" in checklist
        assert "3. **Collapse redundant transitions.**" in checklist
        assert "4. **Tighten wordy phrasing.**" in checklist
        assert "5. **Remove the weakest supporting detail.**" in checklist

    def test_verification_checklist_never_cut_guard(self) -> None:
        """Never-cut guard protects five content categories from trimming."""
        checklist = ArticleWriter._verification_checklist
        assert "guideline-required points" in checklist
        assert "golden-source facts" in checklist
        assert "Kind 2 artifacts" in checklist
        assert "exploitation-source facts" in checklist
        assert "citations" in checklist

    def test_verification_checklist_core_draft_landing_check(self) -> None:
        """Core-draft landing check distinguishes lower-half from upper-half tolerance."""
        checklist = ArticleWriter._verification_checklist
        assert "Core-draft landing check" in checklist
        assert "lower half of the window" in checklist
        assert "upper half" in checklist
        assert "do not trim required content just to reclaim exploration headroom" in checklist

    def test_verification_checklist_exploration_citation_skip_during_core_pass(self) -> None:
        """Exploration citation completeness check is skipped during the core article draft pass."""
        checklist = ArticleWriter._verification_checklist
        assert "skip this check during the core article draft pass" in checklist

    def test_verification_checklist_caption_limit_30_words(self) -> None:
        """Caption conciseness check enforces ≤30 words consistently."""
        checklist = ArticleWriter._verification_checklist
        assert "no more than 30 words" in checklist

    def test_verification_checklist_bold_label_check_no_first_priority(self) -> None:
        """Bold-label check has no **First:** label — it runs in document order like other checks."""
        checklist = ArticleWriter._verification_checklist
        assert "**First:**" not in checklist
        assert "before proceeding to any other verification step" not in checklist

    # ------------------------------------------------------------------ #
    # System prompt — core-draft word-count rules                         #
    # ------------------------------------------------------------------ #

    def test_system_prompt_core_draft_lower_half_target(self) -> None:
        """Core draft targets the lower half of the tolerance window to reserve exploration headroom."""
        prompt = ArticleWriter.system_prompt_template
        assert "lower half of the tolerance window" in prompt
        assert "target minus 10% and the target itself" in prompt
        assert "packing priority" in prompt

    def test_system_prompt_word_count_exclusion_matches_checklist(self) -> None:
        """The word-count exclusion list in the Article Guideline section matches the verification checklist."""
        prompt = ArticleWriter.system_prompt_template
        checklist = ArticleWriter._verification_checklist
        # Both must mention the same exclusion categories with consistent wording
        for category in ["code blocks", "Mermaid", "table cell text", "Captions"]:
            assert category.lower() in prompt.lower(), f"Missing '{category}' in system_prompt_template"
            assert category.lower() in checklist.lower(), f"Missing '{category}' in _verification_checklist"

    # ------------------------------------------------------------------ #
    # Exploration integration prompt — three-phase integration process    #
    # ------------------------------------------------------------------ #

    def test_exploration_prompt_three_phases_present(self) -> None:
        """Integration process has exactly three phases plus a final step."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "### Phase 1" in prompt
        assert "### Phase 2" in prompt
        assert "### Phase 3" in prompt
        assert "### Final Step" in prompt

    def test_exploration_prompt_phase1_source_registry(self) -> None:
        """Phase 1 produces a Source Registry with explicit format."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Source Registry" in prompt
        assert "DISMISSED" in prompt
        assert "excluding the References section" in prompt

    def test_exploration_prompt_phase2_references_exclusion(self) -> None:
        """Phase 2 skips the References section."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Skip the References section" in prompt

    def test_exploration_prompt_phase2_step5_is_single_loop(self) -> None:
        """Step 5 explicitly states that sub-steps 5a–5g execute as one loop iteration per source."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Execute sub-steps 5a through 5g as a single loop iteration" in prompt
        assert "before moving to the next source" in prompt

    def test_exploration_prompt_phase2_step5a_baseline_recorded(self) -> None:
        """Step 5a records the baseline word count before the insertion text is written."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Note the section's current prose word count as the **baseline**" in prompt
        assert "for step 5g" in prompt

    def test_exploration_prompt_phase2_step5e_completes_5f_5g(self) -> None:
        """Step 5e allows stopping new sources but mandates finishing 5f and 5g for the current one."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        # The source uses a typographic apostrophe (\u2019)
        assert "do not" in prompt and "next source" in prompt and "iteration" in prompt
        assert "still complete steps 5f and 5g for the current source" in prompt

    def test_exploration_prompt_phase2_step5f_is_rule_check(self) -> None:
        """Step 5f is the per-integration rule check (formerly standalone step 6)."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "**Per-integration rule check.**" in prompt
        # All four rules must be present inside step 5f
        assert "Narrative primacy" in prompt
        assert "Placement" in prompt
        assert "Self-contained integration" in prompt

    def test_exploration_prompt_phase2_step5f_remediation_paths(self) -> None:
        """Step 5f specifies per-rule remediation actions."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        # Narrative primacy → trim → remove
        assert "trim the insertion to its minimum viable form" in prompt
        # Placement → relocate → remove
        assert "relocate the insertion" in prompt
        # Self-contained → remove only (text wraps across lines)
        assert "Trimming cannot fix a structural" in prompt
        # Citations → add → remove
        assert "uncited exploration content must never be retained" in prompt

    def test_exploration_prompt_phase2_step5g_records_word_count(self) -> None:
        """Step 5g records the insertion's prose word count using the step 5a baseline."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Record the insertion's prose word count" in prompt
        assert "subtract the baseline noted at the start of step 5a" in prompt
        # Must reference the new sub-step names (5d, 5f), not the old step 6
        assert "step 5d overflow resolution or step 5f remediation" in prompt

    def test_exploration_prompt_phase2_cumulative_weight_is_step6(self) -> None:
        """Cumulative weight check is now step 6 (not step 7)."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "6. **Cumulative weight check.**" in prompt
        # Old step 7 must not exist
        assert "7. **Cumulative weight check.**" not in prompt

    def test_exploration_prompt_phase2_headroom_skip_targets_step6(self) -> None:
        """Step 2's zero-headroom shortcut skips to step 6 (cumulative weight), not step 7."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "skip to step 6" in prompt
        assert "skip to step 7" not in prompt

    def test_exploration_prompt_phase2_four_ranking_criteria(self) -> None:
        """Step 3 ranks sources by 4 criteria in priority order."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Criterion 1" in prompt
        assert "Specificity" in prompt
        assert "Criterion 2" in prompt
        assert "Depth over breadth under headroom pressure" in prompt
        assert "Criterion 3" in prompt
        assert "Novelty" in prompt
        assert "Criterion 4" in prompt
        assert "Alignment" in prompt

    def test_exploration_prompt_phase2_word_count_exclusion_matches(self) -> None:
        """Phase 2 step 2 headroom estimation excludes the same categories as the verification checklist."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        # Step 2 exclusion list
        assert "excluding code blocks, Mermaid" in prompt
        assert "table cells" in prompt
        assert "captions" in prompt
        assert "citation markers" in prompt

    # ------------------------------------------------------------------ #
    # Exploration integration prompt — Phase 3 cross-section checks       #
    # ------------------------------------------------------------------ #

    def test_exploration_prompt_phase3_ratio_check_references_step5g(self) -> None:
        """Phase 3 check 3 references step 5g for recorded word counts (not old step 6)."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "recorded in\n   Phase 2 step 5g" in prompt or "recorded in Phase 2 step 5g" in prompt.replace("\n   ", " ")

    def test_exploration_prompt_phase3_ratio_upper_bound_note(self) -> None:
        """Phase 3 check 3 notes counts are upper-bound approximations and references step 6."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "upper-bound approximations" in prompt
        assert "step 6 or Phase 3 checks 1-2" in prompt
        # Old "step 7" reference must not appear here
        assert "step 7 or Phase 3" not in prompt

    def test_exploration_prompt_phase3_ratio_cap_20_percent(self) -> None:
        """Exploration-to-core ratio is capped at approximately 20%."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "approximately 20%" in prompt

    def test_exploration_prompt_phase3_duplication_and_saturation_checks(self) -> None:
        """Phase 3 includes same-content duplication and citation saturation checks."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Same-content duplication check" in prompt
        assert "Citation saturation check" in prompt

    # ------------------------------------------------------------------ #
    # Exploration integration prompt — integration rules                  #
    # ------------------------------------------------------------------ #

    def test_exploration_prompt_integration_rules_complete(self) -> None:
        """All six integration rules are present."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Narrative primacy" in prompt
        assert "Placement" in prompt
        assert "Multi-section use" in prompt
        assert "Multiple sources per section" in prompt
        assert "Self-contained integration" in prompt
        assert "Citations (mandatory)" in prompt

    def test_exploration_prompt_multi_source_cross_ref_to_phase2(self) -> None:
        """Multiple sources per section rule cross-references Phase 2 steps 3-5."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Phase 2 steps 3-5" in prompt

    def test_exploration_prompt_examples_scope_note(self) -> None:
        """Examples section has the scope note clarifying they show content quality, not the process."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "do not model\nthe three-phase process" in prompt or "do not model the three-phase process" in prompt.replace("\n", " ")

    def test_exploration_prompt_word_count_ceiling_defers_to_phase2(self) -> None:
        """Word-count ceiling block defers all sizing decisions to Phase 2."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        assert "Phase 1 (qualification) does not check word counts" in prompt
        assert "handled in Phase 2" in prompt

    # ------------------------------------------------------------------ #
    # Review templates — exploration scoping                              #
    # ------------------------------------------------------------------ #

    def test_review_template_no_three_phase_rerun(self) -> None:
        """Both review templates instruct not to re-run the three-phase integration process."""
        assert "do not re-run the three-phase integration process" in ArticleWriter.article_reviews_prompt_template
        # In the selected-text template the phrase wraps across lines
        assert "do not re-run the three-phase" in ArticleWriter.selected_text_reviews_prompt_template
        assert "integration process" in ArticleWriter.selected_text_reviews_prompt_template

    def test_review_templates_prefer_golden_exploitation_sources(self) -> None:
        """Review templates prefer golden or exploitation sources over exploration content."""
        assert "prefer golden or exploitation sources" in ArticleWriter.article_reviews_prompt_template
        assert "prefer golden or exploitation sources" in ArticleWriter.selected_text_reviews_prompt_template

    # ------------------------------------------------------------------ #
    # Python code — research context routing                              #
    # ------------------------------------------------------------------ #

    @pytest.mark.asyncio
    async def test_core_draft_uses_to_core_context(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Core draft (no reviews) uses to_core_context() which strips exploration sources."""
        format_b_content = (
            '<research_source phase="exploitation" url="https://example.com/exploit">exploit content</research_source>\n'
            '<research_source phase="exploration" url="https://example.com/explore">explore content</research_source>'
        )
        research = Research(content=format_b_content)

        mock_response = '{"content": "# Title\\n\\nContent"}'
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        # Verify the core context strips exploration
        core_ctx = research.to_core_context()
        assert "exploit content" in core_ctx
        assert "explore content" not in core_ctx

        result = await writer.ainvoke()
        assert isinstance(result, Article)

    @pytest.mark.asyncio
    async def test_review_pass_uses_full_context(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """Review pass (with reviews) uses to_context() which includes exploration sources."""
        format_b_content = (
            '<research_source phase="exploitation" url="https://example.com/exploit">exploit content</research_source>\n'
            '<research_source phase="exploration" url="https://example.com/explore">explore content</research_source>'
        )
        research = Research(content=format_b_content)

        mock_response = '{"content": "# Revised\\n\\nContent"}'
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        reviews = ArticleReviews(
            article=Article(content="Original"),
            reviews=[Review(profile="p", location="l", comment="c")],
        )

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            reviews=reviews,
            model=model,
        )

        # Verify full context includes exploration
        full_ctx = research.to_context()
        assert "exploit content" in full_ctx
        assert "explore content" in full_ctx

        result = await writer.ainvoke()
        assert isinstance(result, Article)

    @pytest.mark.asyncio
    async def test_exploration_integration_uses_exploration_sources_directly(
        self,
        mock_article_guideline: ArticleGuideline,
        mock_article_profiles: ArticleProfiles,
        mock_media_items: MediaItems,
        mock_article_examples: ArticleExamples,
    ) -> None:
        """ainvoke_exploration_integration uses _exploration_sources for the exploration_sources slot."""
        format_b_content = (
            '<research_source phase="exploitation" url="https://example.com/exploit">exploit content</research_source>\n'
            '<research_source phase="exploration" url="https://example.com/explore">explore content</research_source>'
        )
        research = Research(content=format_b_content)

        mock_response = '{"content": "# Integrated\\n\\nContent with exploration"}'
        app_config = get_app_config()
        model, _ = build_model(app_config, node="write_article")
        model.responses = [mock_response]

        writer = ArticleWriter(
            article_guideline=mock_article_guideline,
            research=research,
            article_profiles=mock_article_profiles,
            media_items=mock_media_items,
            article_examples=mock_article_examples,
            model=model,
        )

        core_article = Article(content="# Core Article\n\nCore content.")

        # Verify _exploration_sources extracts only exploration blocks
        assert "explore content" in research._exploration_sources
        assert "exploit content" not in research._exploration_sources

        result = await writer.ainvoke_exploration_integration(core_article)
        assert isinstance(result, Article)

    # ------------------------------------------------------------------ #
    # Cross-template consistency checks                                   #
    # ------------------------------------------------------------------ #

    def test_no_stale_step_references(self) -> None:
        """No stale step-number references remain in the exploration integration prompt."""
        prompt = ArticleWriter.exploration_integration_prompt_template
        # Old standalone step 6 (now 5f) and step 7 (now 6) must not appear as top-level steps
        assert "7. **Cumulative weight check.**" not in prompt
        assert "6. **Per-integration rule check.**" not in prompt
        # Old cross-references must be gone
        assert "step 6 remediation" not in prompt
        assert "skip to step 7" not in prompt
        assert "step 7 or Phase 3" not in prompt

    def test_caption_limit_consistent_across_all_locations(self) -> None:
        """Caption word limit is 30 words in both the system prompt media section and verification checklist."""
        system = ArticleWriter.system_prompt_template
        checklist = ArticleWriter._verification_checklist
        assert "30 words" in system
        assert "30 words" in checklist
        # Old 20-word limit must not appear
        assert "20 words" not in system
        assert "20 words" not in checklist
