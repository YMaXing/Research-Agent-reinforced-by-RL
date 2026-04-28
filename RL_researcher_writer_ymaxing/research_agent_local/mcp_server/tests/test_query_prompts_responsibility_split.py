"""Static-content tests for the step-3 / step-4 responsibility split.

These tests pin the structural invariants of three LLM prompt templates that
together enforce the boundary between the exploitation phase (step 3,
lookup-only) and the exploration phase (step 4, gap-driven depth/breadth):

    PROMPT_GENERATE_QUERIES_AND_REASONS
    PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
    PROMPT_DEDUPLICATE_QUERIES

Plus the master ``research_instructions_prompt`` that wires those prompts into
the agent workflow.

All tests are content assertions on string templates - no LLM is invoked.
"""

from __future__ import annotations

from unittest.mock import patch

import pytest

from src.config.prompts import (
    PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS,
    PROMPT_GENERATE_QUERIES_AND_REASONS,
    PROMPT_DEDUPLICATE_QUERIES,
)


_PATCH_SETTINGS = "src.prompts.research_instructions_prompt.settings"


def _make_settings(enable_content_dedup: bool = True):
    return type(
        "Settings",
        (),
        {
            "enable_content_dedup": enable_content_dedup,
            "maximum_exploration_rounds": 4,
            "maximum_sources_to_scrape": 6,
        },
    )()


# ---------------------------------------------------------------------------
# Step 3 prompt: PROMPT_GENERATE_QUERIES_AND_REASONS
# ---------------------------------------------------------------------------


class TestStep3ExploitationPromptContent:
    """The exploitation prompt must be unambiguously lookup-only."""

    def test_declares_exploitation_lookup_scope(self):
        assert "EXPLOITATION" in PROMPT_GENERATE_QUERIES_AND_REASONS
        assert "LOOKUP ONLY" in PROMPT_GENERATE_QUERIES_AND_REASONS

    def test_requires_anchor_in_reason_field(self):
        # Mandatory `Anchor: "..."` prefix on every reason field
        assert 'Anchor: "<verbatim quote from the guideline>"' in PROMPT_GENERATE_QUERIES_AND_REASONS
        assert "Mandatory anchoring rule" in PROMPT_GENERATE_QUERIES_AND_REASONS

    def test_lists_three_anchor_types(self):
        # H2/H3 heading, bullet point, named entity
        assert "H2 or H3 section heading" in PROMPT_GENERATE_QUERIES_AND_REASONS
        assert "bullet point" in PROMPT_GENERATE_QUERIES_AND_REASONS.lower()
        assert "named entity" in PROMPT_GENERATE_QUERIES_AND_REASONS.lower()

    @pytest.mark.parametrize(
        "forbidden_phrase",
        [
            "Limitations",
            "failure modes",
            "Latest advancements",
            "Real-world case studies",
            "History",
            "Future implications",
            "Cross-domain analogies",
            "Enabling, disrupting, or adjacent technologies",
            "Theoretical foundations",
        ],
    )
    def test_forbidden_categories_explicitly_listed(self, forbidden_phrase):
        # The forbidden-categories list is the teeth of the lookup-only rule
        assert forbidden_phrase in PROMPT_GENERATE_QUERIES_AND_REASONS

    def test_few_shot_examples_use_anchor_prefix(self):
        # All four few-shot reasons must demonstrate the `Anchor: "..."` format
        # so the LLM imitates it. Count occurrences of the literal token.
        anchor_count = PROMPT_GENERATE_QUERIES_AND_REASONS.count('Anchor: "')
        # 1 in the rule statement + 4 in the few-shot examples = at least 5
        assert anchor_count >= 5, (
            f"Expected at least 5 Anchor: prefixes (1 rule + 4 examples), got {anchor_count}"
        )

    def test_allows_dropping_below_n_queries_to_avoid_leakage(self):
        # Quality-over-quantity escape hatch
        assert "generate fewer queries" in PROMPT_GENERATE_QUERIES_AND_REASONS

    def test_format_placeholders_preserved(self):
        for placeholder in (
            "{n_queries}",
            "{article_guidelines}",
            "{full_queries}",
            "{past_research}",
            "{scraped_ctx}",
        ):
            assert placeholder in PROMPT_GENERATE_QUERIES_AND_REASONS


# ---------------------------------------------------------------------------
# Step 4 prompt: PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
# ---------------------------------------------------------------------------


class TestStep4ExplorationPromptContent:
    """The exploration prompt must be gap-driven only \u2014 no pure coverage."""

    def test_declares_exploration_gap_driven_scope(self):
        assert "EXPLORATION" in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
        assert "GAP-DRIVEN" in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS

    def test_requires_category_label_in_reason(self):
        assert "Category: Depth\u2014" in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
        assert "Category: Breadth\u2014" in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
        assert "Mandatory category labelling" in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS

    def test_requires_anchor_citation_in_reason(self):
        # Step-4 reasons must also cite the anchor they deepen/expand around
        assert 'Anchor: "<guideline anchor this query deepens or expands around>"' in (
            PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
        )

    def test_explicitly_forbids_pure_coverage(self):
        # Pure-coverage queries are step-3 territory and forbidden here
        assert "Pure-coverage questions" in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
        assert '"What is X?"' in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
        assert '"How does X work?"' in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS

    def test_few_shot_examples_use_category_and_anchor_prefixes(self):
        # 2 depth + 2 breadth few-shot reasons + at least 1 mention in the rule
        depth_count = PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS.count("Category: Depth\u2014")
        breadth_count = PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS.count(
            "Category: Breadth\u2014"
        )
        assert depth_count >= 3, f"Expected \u2265 3 'Category: Depth\u2014' tokens, got {depth_count}"
        assert breadth_count >= 3, (
            f"Expected \u2265 3 'Category: Breadth\u2014' tokens, got {breadth_count}"
        )

    def test_format_placeholders_preserved(self):
        for placeholder in (
            "{n_queries}",
            "{article_guidelines}",
            "{full_queries}",
            "{past_research}",
            "{scraped_ctx}",
            "{depth_percentage}",
            "{breadth_percentage}",
        ):
            assert placeholder in PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS


# ---------------------------------------------------------------------------
# Dedup prompt: PROMPT_DEDUPLICATE_QUERIES (backstop rules)
# ---------------------------------------------------------------------------


class TestDeduplicationPromptBackstopRules:
    """Dedup prompt must reject exploration-flavored exploitation queries and
    coverage-flavored exploration queries as a safety net."""

    def test_exploitation_round_has_exploration_leakage_backstop(self):
        assert "Backstop rule (exploration leakage)" in PROMPT_DEDUPLICATE_QUERIES

    def test_complementary_round_has_exploitation_leakage_backstop(self):
        assert "Backstop rule (exploitation leakage)" in PROMPT_DEDUPLICATE_QUERIES

    @pytest.mark.parametrize(
        "leakage_category",
        [
            "limitations",
            "failure modes",
            "latest advancements",
            "real-world case studies",
            "future implications",
            "cross-domain analogies",
            "history",
        ],
    )
    def test_backstop_lists_forbidden_exploitation_categories(self, leakage_category):
        # The exploration-leakage backstop must enumerate the categories so the
        # LLM can recognize them on sight
        assert leakage_category in PROMPT_DEDUPLICATE_QUERIES.lower()

    def test_format_placeholders_preserved(self):
        for placeholder in ("{full_queries_history}", "{new_queries_list}", "{query_source}"):
            assert placeholder in PROMPT_DEDUPLICATE_QUERIES


# ---------------------------------------------------------------------------
# Master research instructions prompt: scope headers in step 3 and step 4
# ---------------------------------------------------------------------------


class TestResearchInstructionsScopeHeaders:
    """The master agent prompt must echo the responsibility split at the
    workflow level, so the orchestrator enforces it across rounds."""

    async def test_step_3_has_lookup_only_scope_header(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings()):
            result = await full_research_instructions_prompt()

        assert "Scope of step 3 (lookup-only)" in result
        # Must remind the agent that depth/breadth categories are forbidden here
        assert "*forbidden* in this phase" in result
        # Must reference the dedup tool as the backstop
        assert "dedup tool will reject any exploitation query that drifts" in result

    async def test_step_4_has_gap_driven_scope_header(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings()):
            result = await full_research_instructions_prompt()

        assert "Scope of step 4 (gap-driven exploration only)" in result
        # Must explicitly forbid pure-coverage queries here
        assert "Pure-coverage" in result and "are *forbidden* here" in result
        # Must reference the dedup tool as the backstop (collapse whitespace so the
        # assertion is robust to line wrapping in the prompt source).
        collapsed = " ".join(result.split())
        assert "dedup tool will reject any exploration query that is pure coverage" in collapsed

    async def test_scope_headers_appear_before_sub_steps(self):
        """The scope header must appear before the 3.1 / 4.1 sub-step bullets so
        the agent sees the constraint before reading the loop body."""
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings()):
            result = await full_research_instructions_prompt()

        step3_scope_idx = result.index("Scope of step 3 (lookup-only)")
        step3_substep_idx = result.index("3.1.")
        assert step3_scope_idx < step3_substep_idx

        step4_scope_idx = result.index("Scope of step 4 (gap-driven exploration only)")
        step4_substep_idx = result.index("4.1.")
        assert step4_scope_idx < step4_substep_idx
