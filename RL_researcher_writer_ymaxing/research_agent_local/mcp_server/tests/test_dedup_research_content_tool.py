"""Unit tests for src/tools/dedup_research_content_tool.py.

These tests patch the handler call to ensure deterministic logic-only checks,
without any real LLM invocation.
"""

from pathlib import Path
from unittest.mock import patch

from src.config.constants import DEDUPLICATED_RESEARCH_FILE, RESEARCH_OUTPUT_FOLDER
from src.tools.dedup_research_content_tool import deduplicate_research_content_tool

_PATCH_HANDLER = "src.tools.dedup_research_content_tool.deduplicate_research_content"


class TestDeduplicateResearchContentTool:
    async def test_success_writes_deduplicated_file_and_returns_metadata(self, tmp_research_dir):
        with patch(
            _PATCH_HANDLER,
            return_value=("# Final Research\n\nMerged content", {"golden/guideline": 2}, 3),
        ):
            result = await deduplicate_research_content_tool(str(tmp_research_dir))

        assert result["status"] == "success"
        assert result["source_counts"] == {"golden/guideline": 2}
        assert result["total_parts_collected"] == 3

        dedup_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER / DEDUPLICATED_RESEARCH_FILE
        assert dedup_path.exists()
        assert dedup_path.read_text(encoding="utf-8") == "# Final Research\n\nMerged content"
        assert str(dedup_path.resolve()) == result["deduplicated_path"]

    async def test_returns_error_on_directory_validation_failure(self, tmp_path):
        missing_dir = tmp_path / "does_not_exist"
        result = await deduplicate_research_content_tool(str(missing_dir))

        assert result["status"] == "error"
        assert "Directory validation failed" in result["message"]

    async def test_returns_error_when_handler_raises(self, tmp_research_dir):
        with patch(_PATCH_HANDLER, side_effect=RuntimeError("handler exploded")):
            result = await deduplicate_research_content_tool(str(tmp_research_dir))

        assert result["status"] == "error"
        assert "Content deduplication failed" in result["message"]

    async def test_returns_error_when_file_write_fails(self, tmp_research_dir):
        with patch(_PATCH_HANDLER, return_value=("# Dedup", {"research_urls": 1}, 1)):
            with patch.object(Path, "write_text", side_effect=OSError("disk full")):
                result = await deduplicate_research_content_tool(str(tmp_research_dir))

        assert result["status"] == "error"
        assert "Failed to save deduplicated file" in result["message"]