"""
Integration tests for the two public tool functions in
``src/tools/generate_next_queries_tool.py``:

    generate_next_queries_tool
    generate_next_complementary_queries_tool

Both functions orchestrate file I/O + an LLM call.  The LLM is replaced by a
fake model so only the deterministic orchestration logic is exercised.

File-I/O layer
--------------
``tmp_research_dir`` (from conftest) provides an isolated directory containing
``article_guideline.md``.  After each tool call we inspect the files that were
written, asserting structure rather than exact content.

LLM layer
---------
``get_chat_model`` is patched inside ``src.app.generate_queries_handler``
(where it is actually called) at ``src.app.generate_queries_handler.get_chat_model``.
"""

import pytest
from pathlib import Path
from unittest.mock import patch

from tests.conftest import FAKE_QUERIES_5, FakeStructuredModel, RecordingModel
from src.tools.generate_next_queries_tool import (
    generate_next_complementary_queries_tool,
    generate_next_queries_tool,
)
from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    FULL_QUERIES_FILE,
    NEXT_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)

_LLM_PATCH = "src.app.generate_queries_handler.get_chat_model"


# ---------------------------------------------------------------------------
# generate_next_queries_tool  (exploitation / round queries)
# ---------------------------------------------------------------------------

class TestGenerateNextQueriesTool:
    async def test_returns_success_status(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_queries_tool(str(tmp_research_dir))

        assert result["status"] == "success"

    async def test_returns_correct_query_count(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_queries_tool(str(tmp_research_dir))

        assert result["queries_count"] == 5

    async def test_result_queries_list_has_five_items(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_queries_tool(str(tmp_research_dir))

        assert len(result["queries"]) == 5

    async def test_result_contains_output_path_key(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_queries_tool(str(tmp_research_dir))

        assert "output_path" in result

    async def test_creates_research_output_folder(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert (tmp_research_dir / RESEARCH_OUTPUT_FOLDER).is_dir()

    async def test_creates_next_queries_file(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / NEXT_QUERIES_FILE).exists()

    async def test_next_queries_file_contains_query_text(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        content = (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / NEXT_QUERIES_FILE).read_text(
            encoding="utf-8"
        )
        assert "What is RAG?" in content

    async def test_creates_full_queries_file(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).exists()

    async def test_full_queries_file_uses_exploitation_tag(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        content = (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).read_text(
            encoding="utf-8"
        )
        assert "[Exploitation]" in content

    async def test_full_queries_ids_start_at_1_for_new_directory(
        self, fake_structured_model, tmp_research_dir
    ):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        content = (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).read_text(
            encoding="utf-8"
        )
        assert "Query [1]" in content

    async def test_second_call_increments_ids(self, fake_structured_model, tmp_research_dir):
        """Running the tool twice on the same directory should assign ids 1-5, then 6-10."""
        model = FakeStructuredModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=model):
            await generate_next_queries_tool(str(tmp_research_dir))
        with patch(_LLM_PATCH, return_value=model):
            await generate_next_queries_tool(str(tmp_research_dir))

        content = (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).read_text(
            encoding="utf-8"
        )
        assert "Query [6]" in content

    async def test_next_queries_file_is_overwritten_on_second_call(
        self, fake_structured_model, tmp_research_dir
    ):
        """next_queries.md is always fresh (not appended)."""
        model = FakeStructuredModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=model):
            await generate_next_queries_tool(str(tmp_research_dir))

        # Modify the file manually
        nq = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / NEXT_QUERIES_FILE
        nq.write_text("stale content", encoding="utf-8")

        with patch(_LLM_PATCH, return_value=model):
            await generate_next_queries_tool(str(tmp_research_dir))

        content = nq.read_text(encoding="utf-8")
        assert "stale content" not in content

    async def test_raises_value_error_for_nonexistent_directory(self):
        with pytest.raises(ValueError):
            await generate_next_queries_tool("/this/path/does/not/exist")

    async def test_result_message_is_string(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_queries_tool(str(tmp_research_dir))

        assert isinstance(result["message"], str)

    async def test_scraped_context_collected_when_urls_folder_exists(
        self, fake_structured_model, tmp_research_dir
    ):
        """If the urls_from_guidelines folder contains .md files, content is read and forwarded."""
        urls_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / "urls_from_guidelines"
        urls_dir.mkdir(parents=True, exist_ok=True)
        (urls_dir / "scraped_page.md").write_text(
            "# Scraped\nContent from the web.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert "Content from the web." in recording.last_prompt


# ---------------------------------------------------------------------------
# generate_next_complementary_queries_tool  (exploration / RL rounds)
# ---------------------------------------------------------------------------

class TestGenerateNextComplementaryQueriesTool:
    async def test_returns_success_status(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert result["status"] == "success"

    async def test_returns_correct_query_count(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            result = await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert result["queries_count"] == 5

    async def test_full_queries_uses_exploration_tag(self, fake_structured_model, tmp_research_dir):
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        content = (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).read_text(
            encoding="utf-8"
        )
        assert "[Exploration]" in content

    async def test_focus_depth_sends_80_percent_to_prompt(self, tmp_research_dir):
        """focus='depth' overrides ratio to 0.80 → prompt must contain '80'."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=0.1,  # should be ignored
                focus="depth",
            )

        assert "80" in recording.last_prompt

    async def test_focus_breadth_sends_20_percent_depth_to_prompt(self, tmp_research_dir):
        """focus='breadth' overrides ratio to 0.20 → depth_pct=20 in prompt."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=0.9,  # should be ignored
                focus="breadth",
            )

        assert "20" in recording.last_prompt

    async def test_focus_balanced_honours_provided_ratio(self, tmp_research_dir):
        """focus='balanced' clamps the user-supplied ratio to [0, 1] and uses it."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=0.6,
                focus="balanced",
            )

        assert "60" in recording.last_prompt

    async def test_focus_balanced_clamps_ratio_above_1(self, tmp_research_dir):
        """ratio > 1.0 is clamped to 1.0 → depth_pct=100."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=1.5,
                focus="balanced",
            )

        assert "100" in recording.last_prompt

    async def test_focus_balanced_clamps_ratio_below_0(self, tmp_research_dir):
        """ratio < 0.0 is clamped to 0.0 → depth_pct=0."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=-0.5,
                focus="balanced",
            )

        assert "0" in recording.last_prompt

    async def test_next_queries_file_is_overwritten(self, fake_structured_model, tmp_research_dir):
        nq = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / NEXT_QUERIES_FILE
        nq.parent.mkdir(parents=True, exist_ok=True)
        nq.write_text("old complementary content", encoding="utf-8")

        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        content = nq.read_text(encoding="utf-8")
        assert "old complementary content" not in content

    async def test_raises_value_error_for_nonexistent_directory(self):
        with pytest.raises(ValueError):
            await generate_next_complementary_queries_tool("/nonexistent/path")

    async def test_default_focus_is_balanced(self, tmp_research_dir):
        """Calling without explicit focus should default to balanced (ratio=0.5)."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir)
                # no focus argument → defaults to "balanced", ratio=0.5
            )

        assert "50" in recording.last_prompt
