"""Tests for the comparison-matrix filter helpers in brown.workflows.generate_article.

Covers:
  - _is_comparison_matrix_section  (original Pros/Cons + broadened attribute detection)
  - _is_comparison_matrix_description
  - _extract_section_text
  - _filter_comparison_matrix_tool_calls
  - _filter_comparison_matrix_media_items
"""

from brown.workflows.generate_article import (
    _extract_section_text,
    _filter_comparison_matrix_media_items,
    _filter_comparison_matrix_tool_calls,
    _is_comparison_matrix_description,
    _is_comparison_matrix_section,
)

# ---------------------------------------------------------------------------
# _is_comparison_matrix_section
# ---------------------------------------------------------------------------


class TestIsComparisonMatrixSection:
    """Original Pros/Cons detection and broadened per-item attribute detection."""

    # --- original Pros/Cons behaviour ---

    def test_pros_and_cons_each_at_least_twice_returns_true(self) -> None:
        """Classic Pros/Cons labelling with >=2 of each is a comparison matrix."""
        section = "Approach A\nPros: fast, cheap\nCons: fragile, limited\nApproach B\nPros: reliable, flexible\nCons: slow, expensive\n"
        assert _is_comparison_matrix_section(section) is True

    def test_pro_cons_singular_forms_detected(self) -> None:
        """Singular 'Pro:' / 'Con:' forms also match."""
        section = "Option 1\nPro: easy\nCon: limited\nOption 2\nPro: powerful\nCon: complex\n"
        assert _is_comparison_matrix_section(section) is True

    def test_pros_count_below_threshold_returns_false(self) -> None:
        """Only one 'Pros:' and one 'Cons:' is NOT enough to flag a comparison matrix."""
        section = "Approach A\nPros: fast\nCons: fragile\n"
        assert _is_comparison_matrix_section(section) is False

    def test_flow_description_not_detected_as_comparison(self) -> None:
        """A plain architecture flow description is not a comparison matrix."""
        section = (
            "Data flows from the user through the API gateway into the database.\n"
            "The processing pipeline consists of ingestion, transformation, and storage.\n"
        )
        assert _is_comparison_matrix_section(section) is False

    # --- broadened attribute detection ---

    def test_trade_offs_appearing_twice_contributes_one_marker_hit(self) -> None:
        """'Trade-offs:' appearing >=2 times counts as one marker hit (needs 2 types)."""
        section = "Approach A\nTrade-offs: some trade-offs here\nApproach B\nTrade-offs: different trade-offs\n"
        # Only 1 attribute type (trade-offs) >= 2 times → marker_hits = 1 → False
        assert _is_comparison_matrix_section(section) is False

    def test_two_different_attribute_types_each_at_least_twice_returns_true(self) -> None:
        """Two distinct attribute types each appearing >=2 times → comparison matrix."""
        section = (
            "Approach A\nTrade-offs: high latency\nUse cases: batch processing\n"
            "Approach B\nTrade-offs: limited throughput\nUse cases: real-time streaming\n"
        )
        assert _is_comparison_matrix_section(section) is True

    def test_complexity_and_performance_each_twice_returns_true(self) -> None:
        """'Complexity:' and 'Performance:' each >= 2 times is a comparison matrix."""
        section = "Option A\nComplexity: low\nPerformance: fast\nOption B\nComplexity: high\nPerformance: optimal\n"
        assert _is_comparison_matrix_section(section) is True

    def test_advantages_and_disadvantages_each_twice_returns_true(self) -> None:
        """'Advantages:' and 'Disadvantages:' each >= 2 times is a comparison matrix."""
        section = "Method 1\nAdvantages: simple\nDisadvantages: slow\nMethod 2\nAdvantages: fast\nDisadvantages: complex\n"
        assert _is_comparison_matrix_section(section) is True

    def test_limitations_appearing_twice_alone_not_enough(self) -> None:
        """'Limitations:' appearing twice but no second attribute type → not a matrix."""
        section = "Approach A\nLimitations: cannot scale\nApproach B\nLimitations: high memory usage\n"
        # Only 1 type → marker_hits = 1 → False
        assert _is_comparison_matrix_section(section) is False

    def test_when_to_use_and_complexity_each_twice_returns_true(self) -> None:
        """'When to use:' and 'Complexity:' each >=2 times is a comparison matrix."""
        section = (
            "Strategy 1\nWhen to use: small datasets\nComplexity: O(n)\nStrategy 2\nWhen to use: large datasets\nComplexity: O(n log n)\n"
        )
        assert _is_comparison_matrix_section(section) is True

    def test_use_case_hyphenated_form_detected(self) -> None:
        """'Use-case:' hyphenated form is also detected."""
        section = "Option A\nUse-case: streaming\nComplexity: medium\nOption B\nUse-case: batch\nComplexity: low\n"
        assert _is_comparison_matrix_section(section) is True

    def test_case_insensitive_matching(self) -> None:
        """Attribute markers are matched case-insensitively."""
        section = (
            "Approach A\nTRADE-OFFS: some issues\nLIMITATIONS: bounded scope\n"
            "Approach B\nTrade-Offs: other issues\nLimitations: narrow use\n"
        )
        assert _is_comparison_matrix_section(section) is True


# ---------------------------------------------------------------------------
# _is_comparison_matrix_description
# ---------------------------------------------------------------------------


class TestIsComparisonMatrixDescription:
    """Tool-call description heuristic: pros+cons synonym co-occurrence."""

    def test_pros_and_cons_present_returns_true(self) -> None:
        assert _is_comparison_matrix_description("show the pros and cons of each approach") is True

    def test_advantages_and_disadvantages_returns_true(self) -> None:
        assert _is_comparison_matrix_description("compare advantages and disadvantages") is True

    def test_benefits_and_drawbacks_returns_true(self) -> None:
        assert _is_comparison_matrix_description("list benefits and drawbacks of the three methods") is True

    def test_strengths_and_limitations_returns_true(self) -> None:
        assert _is_comparison_matrix_description("strengths and limitations side by side") is True

    def test_only_pros_no_cons_returns_false(self) -> None:
        assert _is_comparison_matrix_description("highlight the benefits of each approach") is False

    def test_only_cons_no_pros_returns_false(self) -> None:
        assert _is_comparison_matrix_description("show the drawbacks of each method") is False

    def test_flow_description_returns_false(self) -> None:
        assert _is_comparison_matrix_description("flowchart showing data flowing from ingestion through transformation to storage") is False


# ---------------------------------------------------------------------------
# _extract_section_text
# ---------------------------------------------------------------------------


class TestExtractSectionText:
    """Guideline section extraction by heading match."""

    GUIDELINE = (
        "# Article\n"
        "\n"
        "## Section 1: Introduction\n"
        "Intro content here.\n"
        "\n"
        "## Section 2: Memory Types\n"
        "Memory content here.\n"
        "\n"
        "### Section 2.1: Short-Term Memory\n"
        "Short-term content.\n"
        "\n"
        "## Section 3: Conclusion\n"
        "Conclusion content.\n"
    )

    def test_extracts_exact_heading_match(self) -> None:
        text = _extract_section_text(self.GUIDELINE, "Section 2: Memory Types")
        assert text is not None
        assert "Memory content here." in text

    def test_substring_match_works(self) -> None:
        """Fuzzy: if section_title is a substring of the heading."""
        text = _extract_section_text(self.GUIDELINE, "Memory Types")
        assert text is not None
        assert "Memory content here." in text

    def test_heading_substring_of_title_works(self) -> None:
        """Fuzzy: if heading is a substring of the provided title."""
        text = _extract_section_text(self.GUIDELINE, "Full Title Including Section 1: Introduction")
        assert text is not None
        assert "Intro content here." in text

    def test_body_ends_before_next_heading(self) -> None:
        """Extracted text must not bleed into the next section."""
        text = _extract_section_text(self.GUIDELINE, "Memory Types")
        assert text is not None
        assert "Conclusion content" not in text

    def test_non_matching_title_returns_none(self) -> None:
        text = _extract_section_text(self.GUIDELINE, "Nonexistent Section XYZ")
        assert text is None

    def test_last_section_has_no_end_boundary(self) -> None:
        """The last section in the guideline runs to the end of the string."""
        text = _extract_section_text(self.GUIDELINE, "Conclusion")
        assert text is not None
        assert "Conclusion content." in text


# ---------------------------------------------------------------------------
# _filter_comparison_matrix_tool_calls
# ---------------------------------------------------------------------------


class TestFilterComparisonMatrixToolCalls:
    """Pre-generation filter: drop mermaid tool calls for comparison matrix sections."""

    def _make_job(self, description: str, section_title: str = "Test Section") -> dict:
        return {
            "name": "mermaid_diagram_generator_tool",
            "args": {
                "description_of_the_diagram": description,
                "section_title": section_title,
            },
        }

    def test_description_with_pros_and_cons_is_filtered(self) -> None:
        jobs = [self._make_job("compare the pros and cons of all three approaches")]
        messages: list[str] = []
        result = _filter_comparison_matrix_tool_calls(jobs, "", messages.append)
        assert result == []

    def test_description_without_pros_cons_is_kept(self) -> None:
        jobs = [self._make_job("flowchart showing the memory retrieval pipeline")]
        messages: list[str] = []
        result = _filter_comparison_matrix_tool_calls(jobs, "", messages.append)
        assert len(result) == 1

    def test_secondary_guideline_check_filters_pros_cons_section(self) -> None:
        """Secondary check: section content with Pros:/Cons: triggers filtering."""
        guideline = "## Retrieval Strategies\nOption A\nPros: fast\nCons: limited\nOption B\nPros: flexible\nCons: slow\n"
        jobs = [self._make_job("visualize the three strategies", "Retrieval Strategies")]
        messages: list[str] = []
        result = _filter_comparison_matrix_tool_calls(jobs, guideline, messages.append)
        assert result == []

    def test_secondary_check_keeps_non_comparison_section(self) -> None:
        """Secondary check: flow-only section content is kept."""
        guideline = "## Memory Pipeline\nData flows from long-term memory through retrieval into the context window.\n"
        jobs = [self._make_job("flowchart of the memory pipeline", "Memory Pipeline")]
        messages: list[str] = []
        result = _filter_comparison_matrix_tool_calls(jobs, guideline, messages.append)
        assert len(result) == 1

    def test_mixed_jobs_partial_filtering(self) -> None:
        """Only jobs that match comparison matrix criteria are removed."""
        jobs = [
            self._make_job("flowchart of memory architecture", "Memory Architecture"),
            self._make_job("compare pros and cons of three approaches", "Comparison"),
        ]
        messages: list[str] = []
        result = _filter_comparison_matrix_tool_calls(jobs, "", messages.append)
        assert len(result) == 1
        assert result[0]["args"]["section_title"] == "Memory Architecture"

    def test_filtered_job_logs_message(self) -> None:
        """A filtered job must produce a log message explaining why it was dropped."""
        jobs = [self._make_job("show pros and cons of methods")]
        messages: list[str] = []
        _filter_comparison_matrix_tool_calls(jobs, "", messages.append)
        assert len(messages) == 1
        assert "comparison matrix" in messages[0].lower() or "filtered" in messages[0].lower()


# ---------------------------------------------------------------------------
# _filter_comparison_matrix_media_items
# ---------------------------------------------------------------------------


class TestFilterComparisonMatrixMediaItems:
    """Post-generation safety net: drop MermaidDiagram items with comparison-matrix content.

    A diagram is dropped when two or more distinct comparison attributes
    (Pros/Cons, trade-offs, limitations, use cases, complexity, etc.) appear.
    """

    def _make_mermaid_diagram(self, content: str) -> object:
        from brown.entities.media_items import MermaidDiagram

        return MermaidDiagram(location="Test", content=content, caption="caption")

    def test_mermaid_with_pros_and_cons_is_dropped(self) -> None:
        diagram = self._make_mermaid_diagram('```mermaid\ngraph TD\n  A["Pros: fast"]\n  B["Cons: slow"]\n```')
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert result == []

    def test_mermaid_with_advantages_and_disadvantages_is_dropped(self) -> None:
        diagram = self._make_mermaid_diagram('```mermaid\ngraph TD\n  A["Advantages: flexible"]\n  B["Disadvantages: complex"]\n```')
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert result == []

    def test_mermaid_with_tradeoffs_and_limitations_is_dropped(self) -> None:
        """Trade-offs + limitations counts as two distinct comparison attributes."""
        diagram = self._make_mermaid_diagram(
            '```mermaid\ngraph TD\n  A["Trade-offs: higher latency"]\n  B["Limitations: memory bound"]\n```'
        )
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert result == []

    def test_mermaid_with_use_cases_and_complexity_is_dropped(self) -> None:
        """Use cases + complexity counts as two distinct comparison attributes."""
        diagram = self._make_mermaid_diagram('```mermaid\ngraph TD\n  A["Use cases: real-time"]\n  B["Complexity: O(n log n)"]\n```')
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert result == []

    def test_mermaid_with_strengths_and_weaknesses_is_dropped(self) -> None:
        """Strengths + weaknesses counts as two distinct comparison attributes."""
        diagram = self._make_mermaid_diagram('```mermaid\ngraph TD\n  A["Strengths: parallelisable"]\n  B["Weaknesses: brittle"]\n```')
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert result == []

    def test_single_attribute_alone_is_kept(self) -> None:
        """A diagram that only mentions one comparison attribute word is kept (no pair)."""
        diagram = self._make_mermaid_diagram('```mermaid\ngraph TD\n  A["Performance: O(1) lookup"]\n  B["Cache hit"]\n```')
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert len(result) == 1

    def test_flow_diagram_without_comparison_content_is_kept(self) -> None:
        diagram = self._make_mermaid_diagram('```mermaid\nflowchart LR\n  A["Input"] -- "process" --> B["Output"]\n```')
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert len(result) == 1

    def test_non_mermaid_items_always_kept(self) -> None:
        """Non-MermaidDiagram media items must pass through untouched."""
        from brown.entities.media_items import MediaItem

        class OtherItem(MediaItem):
            xml_tag: str = "other"

        item = OtherItem(location="Test", content="pros: x\ncons: y", caption="caption")
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([item], messages.append)  # type: ignore[arg-type]
        assert len(result) == 1

    def test_mixed_items_partial_filtering(self) -> None:
        """Only MermaidDiagram items with comparison-matrix content are dropped."""
        from brown.entities.media_items import MermaidDiagram

        good = MermaidDiagram(
            location="Architecture",
            content='```mermaid\nflowchart LR\n  A["Ingestion"] --> B["Storage"]\n```',
            caption="Memory flow",
        )
        bad = MermaidDiagram(
            location="Comparison",
            content='```mermaid\ngraph TD\n  A["Pros: fast"]\n  B["Cons: slow"]\n```',
            caption="Comparison table",
        )
        messages: list[str] = []
        result = _filter_comparison_matrix_media_items([good, bad], messages.append)  # type: ignore[arg-type]
        assert len(result) == 1
        assert result[0].location == "Architecture"

    def test_dropped_item_logs_message(self) -> None:
        """A dropped item must produce a log message."""
        diagram = self._make_mermaid_diagram('```mermaid\ngraph TD\n  A["Pros: x"]\n  B["Cons: y"]\n```')
        messages: list[str] = []
        _filter_comparison_matrix_media_items([diagram], messages.append)  # type: ignore[arg-type]
        assert len(messages) == 1
