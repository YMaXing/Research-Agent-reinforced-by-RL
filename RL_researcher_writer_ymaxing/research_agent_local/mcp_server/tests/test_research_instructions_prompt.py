"""Unit tests for src/prompts/research_instructions_prompt.py.

Covers the conditional branching introduced by ``enable_content_dedup``:
- When dedup is enabled (default): step 7 block is present, final write step is numbered 8.
- When dedup is disabled: step 7 block is absent, final write step is numbered 7.
"""

from unittest.mock import patch

import pytest

_PATCH_SETTINGS = "src.prompts.research_instructions_prompt.settings"


def _make_settings(enable_content_dedup: bool):
    """Return a minimal settings stub with the fields the prompt reads."""
    return type(
        "Settings",
        (),
        {
            "enable_content_dedup": enable_content_dedup,
            "maximum_exploration_rounds": 4,
            "maximum_sources_to_scrape": 6,
        },
    )()


class TestResearchInstructionsPromptDeduEnabled:
    async def test_returns_string(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=True)):
            result = await full_research_instructions_prompt()

        assert isinstance(result, str)
        assert len(result) > 0

    async def test_contains_dedup_step_7(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=True)):
            result = await full_research_instructions_prompt()

        assert "7. Content-level deduplication:" in result
        assert "deduplicate_research_content" in result

    async def test_write_step_is_numbered_8(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=True)):
            result = await full_research_instructions_prompt()

        assert "8. Write final research file:" in result
        assert "8.1 Run the" in result

    async def test_write_step_not_numbered_7(self):
        """Step 7 must be dedup, not the write step, when dedup is enabled."""
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=True)):
            result = await full_research_instructions_prompt()

        assert "7. Write final research file:" not in result

    async def test_exploration_rounds_substituted(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=True)):
            result = await full_research_instructions_prompt()

        assert "{settings.maximum_exploration_rounds}" not in result
        assert "{n_max_round}" not in result
        assert "maximum number of 4 rounds" in result

    async def test_sources_to_scrape_substituted(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=True)):
            result = await full_research_instructions_prompt()

        assert "{settings.maximum_sources_to_scrape}" not in result
        assert "{n_max_sources_to_scrape}" not in result
        assert "chooses up to 6 diverse" in result


class TestResearchInstructionsPromptDeduDisabled:
    async def test_returns_string(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=False)):
            result = await full_research_instructions_prompt()

        assert isinstance(result, str)
        assert len(result) > 0

    async def test_dedup_step_7_absent(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=False)):
            result = await full_research_instructions_prompt()

        assert "7. Content-level deduplication:" not in result
        # The tool description should also be absent
        assert "deduplicate_research_content" not in result

    async def test_write_step_is_numbered_7(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=False)):
            result = await full_research_instructions_prompt()

        assert "7. Write final research file:" in result
        assert "7.1 Run the" in result

    async def test_write_step_not_numbered_8(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=False)):
            result = await full_research_instructions_prompt()

        assert "8. Write final research file:" not in result

    async def test_exploration_rounds_substituted(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=False)):
            result = await full_research_instructions_prompt()

        assert "{n_max_round}" not in result
        assert "maximum number of 4 rounds" in result

    async def test_sources_to_scrape_substituted(self):
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=False)):
            result = await full_research_instructions_prompt()

        assert "{n_max_sources_to_scrape}" not in result
        assert "chooses up to 6 diverse" in result


class TestResearchInstructionsPromptStepNumberConsistency:
    @pytest.mark.parametrize("dedup_enabled", [True, False])
    async def test_no_unresolved_format_placeholders(self, dedup_enabled: bool):
        """Ensure no leftover .format()-style placeholders remain in the output."""
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=dedup_enabled)):
            result = await full_research_instructions_prompt()

        assert "{n_max_round}" not in result
        assert "{n_max_sources_to_scrape}" not in result

    @pytest.mark.parametrize("dedup_enabled", [True, False])
    async def test_create_research_file_tool_always_mentioned(self, dedup_enabled: bool):
        """The create_research_file tool must appear in the prompt regardless of dedup setting."""
        from src.prompts.research_instructions_prompt import full_research_instructions_prompt

        with patch(_PATCH_SETTINGS, _make_settings(enable_content_dedup=dedup_enabled)):
            result = await full_research_instructions_prompt()

        assert "create_research_file" in result
