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
    LOCAL_FILES_FROM_RESEARCH_FOLDER,
    NEXT_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
    URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
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

    async def test_does_not_create_full_queries_file(self, fake_structured_model, tmp_research_dir):
        """generate_next_queries_tool only writes next_queries.md; full_queries.md is handled by deduplicate_new_queries_tool."""
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert not (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).exists()

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

    async def test_local_files_context_collected(self, tmp_research_dir):
        """If local_files_from_research folder contains .md files, content is included in context."""
        local_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / LOCAL_FILES_FROM_RESEARCH_FOLDER
        local_dir.mkdir(parents=True, exist_ok=True)
        (local_dir / "notebook.md").write_text(
            "# Local Notebook\nImportant local content.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert "Important local content." in recording.last_prompt


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

    async def test_does_not_create_full_queries_file(self, fake_structured_model, tmp_research_dir):
        """generate_next_complementary_queries_tool only writes next_queries.md; full_queries.md is handled by deduplicate_new_queries_tool."""
        with patch(_LLM_PATCH, return_value=fake_structured_model):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert not (tmp_research_dir / RESEARCH_OUTPUT_FOLDER / FULL_QUERIES_FILE).exists()

    async def test_focus_depth_sends_80_percent_to_prompt(self, tmp_research_dir):
        """focus='depth' overrides ratio to 1.0 → prompt must contain '100'."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=0.1,  # should be ignored
                focus="depth",
            )

        assert "100" in recording.last_prompt

    async def test_focus_breadth_sends_20_percent_depth_to_prompt(self, tmp_research_dir):
        """focus='breadth' overrides ratio to 0.0 → depth_pct=0 in prompt."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(
                str(tmp_research_dir),
                depth_vs_breadth_ratio=0.9,  # should be ignored
                focus="breadth",
            )

        assert "0" in recording.last_prompt

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

    async def test_local_files_context_collected(self, tmp_research_dir):
        """If local_files_from_research folder contains .md files, content is included in context."""
        local_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / LOCAL_FILES_FROM_RESEARCH_FOLDER
        local_dir.mkdir(parents=True, exist_ok=True)
        (local_dir / "local_doc.md").write_text(
            "# Local Doc\nCritical local information.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert "Critical local information." in recording.last_prompt


# ---------------------------------------------------------------------------
# Scraped-context completeness: all five guideline-source folders are read
# by BOTH tools (regression tests for the "exploitation sources missing" bug)
# ---------------------------------------------------------------------------

class TestScrapedContextIncludesAllFolders:
    """
    Verify that generate_next_queries_tool and generate_next_complementary_queries_tool
    include content from every folder that is populated in step 2 of the workflow:
      - urls_from_guidelines          (golden other-URLs, step 2.2)
      - urls_from_guidelines_code     (golden GitHub, step 2.3)
      - urls_from_guidelines_youtube  (golden YouTube, step 2.4)
      - urls_from_guidelines_exploitation  ("Other Sources", step 2.5)
      - local_files_from_research     (local files, step 2.1)
    """

    # ---- exploitation tool --------------------------------------------------

    async def test_exploitation_tool_reads_code_folder(self, tmp_research_dir):
        code_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_CODE_FOLDER
        code_dir.mkdir(parents=True, exist_ok=True)
        (code_dir / "repo.md").write_text(
            "# GitHub Repo\nGolden code context.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert "Golden code context." in recording.last_prompt

    async def test_exploitation_tool_reads_youtube_folder(self, tmp_research_dir):
        yt_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER
        yt_dir.mkdir(parents=True, exist_ok=True)
        (yt_dir / "video.md").write_text(
            "# YouTube Transcript\nGolden video content.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert "Golden video content." in recording.last_prompt

    async def test_exploitation_tool_reads_exploitation_folder(self, tmp_research_dir):
        """Regression: 'Other Sources' exploitation URLs must be visible in scraped_ctx."""
        exploit_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER
        exploit_dir.mkdir(parents=True, exist_ok=True)
        (exploit_dir / "other_source.md").write_text(
            "# Other Source\nExploitation source content.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_queries_tool(str(tmp_research_dir))

        assert "Exploitation source content." in recording.last_prompt

    async def test_exploitation_tool_reads_all_five_folders_together(self, tmp_research_dir):
        """All five folders contribute content simultaneously."""
        base = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        sentinel_map = {
            "urls_from_guidelines": "GOLDEN_OTHER_SENTINEL",
            URLS_FROM_GUIDELINES_CODE_FOLDER: "GOLDEN_CODE_SENTINEL",
            URLS_FROM_GUIDELINES_YOUTUBE_FOLDER: "GOLDEN_YOUTUBE_SENTINEL",
            URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER: "EXPLOITATION_SENTINEL",
            LOCAL_FILES_FROM_RESEARCH_FOLDER: "LOCAL_FILES_SENTINEL",
        }
        for folder_name, sentinel in sentinel_map.items():
            folder = base / folder_name
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "content.md").write_text(sentinel, encoding="utf-8")

        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_queries_tool(str(tmp_research_dir))

        for sentinel in sentinel_map.values():
            assert sentinel in recording.last_prompt

    # ---- complementary tool -------------------------------------------------

    async def test_complementary_tool_reads_code_folder(self, tmp_research_dir):
        code_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_CODE_FOLDER
        code_dir.mkdir(parents=True, exist_ok=True)
        (code_dir / "repo.md").write_text(
            "# GitHub Repo\nComplementary code context.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert "Complementary code context." in recording.last_prompt

    async def test_complementary_tool_reads_youtube_folder(self, tmp_research_dir):
        yt_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER
        yt_dir.mkdir(parents=True, exist_ok=True)
        (yt_dir / "video.md").write_text(
            "# YouTube Transcript\nComplementary video content.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert "Complementary video content." in recording.last_prompt

    async def test_complementary_tool_reads_exploitation_folder(self, tmp_research_dir):
        """Regression: 'Other Sources' exploitation URLs must be visible in scraped_ctx."""
        exploit_dir = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER
        exploit_dir.mkdir(parents=True, exist_ok=True)
        (exploit_dir / "other_source.md").write_text(
            "# Other Source\nComplementary exploitation content.", encoding="utf-8"
        )
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        assert "Complementary exploitation content." in recording.last_prompt

    async def test_complementary_tool_reads_all_five_folders_together(self, tmp_research_dir):
        """All five folders contribute content simultaneously."""
        base = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        sentinel_map = {
            "urls_from_guidelines": "COMP_GOLDEN_OTHER_SENTINEL",
            URLS_FROM_GUIDELINES_CODE_FOLDER: "COMP_GOLDEN_CODE_SENTINEL",
            URLS_FROM_GUIDELINES_YOUTUBE_FOLDER: "COMP_GOLDEN_YOUTUBE_SENTINEL",
            URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER: "COMP_EXPLOITATION_SENTINEL",
            LOCAL_FILES_FROM_RESEARCH_FOLDER: "COMP_LOCAL_FILES_SENTINEL",
        }
        for folder_name, sentinel in sentinel_map.items():
            folder = base / folder_name
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "content.md").write_text(sentinel, encoding="utf-8")

        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_LLM_PATCH, return_value=recording):
            await generate_next_complementary_queries_tool(str(tmp_research_dir))

        for sentinel in sentinel_map.values():
            assert sentinel in recording.last_prompt
