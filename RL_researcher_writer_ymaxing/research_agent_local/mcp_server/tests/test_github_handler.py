"""Unit tests for src/app/github_handler.py.

``process_github_url`` is async and calls ``gitingest.ingest_async`` which we
mock to avoid network I/O.  We test:
  - filename derivation from URL
  - markdown report structure on success
  - base64 image stripping
  - truncation of oversized content
  - error handling when ingestion fails
"""

from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from src.app.github_handler import process_github_url

_PATCH_INGEST = "src.app.github_handler.ingest_async"


@pytest.fixture
def dest_folder(tmp_path: Path) -> Path:
    folder = tmp_path / "code_sources"
    folder.mkdir()
    return folder


class TestProcessGithubUrl:
    async def test_success_writes_markdown_and_returns_true(self, dest_folder):
        fake_summary = "10 files, 500 lines"
        fake_tree = "src/\n  main.py"
        fake_content = "def main(): pass"
        with patch(_PATCH_INGEST, new_callable=AsyncMock, return_value=(fake_summary, fake_tree, fake_content)):
            result = await process_github_url("https://github.com/owner/repo", dest_folder, "tok")

        assert result is True
        output = dest_folder / "owner_repo.md"
        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert "## Summary" in content
        assert fake_summary in content
        assert "## File tree" in content
        assert "## Extracted content" in content

    async def test_filename_for_short_url(self, dest_folder):
        with patch(_PATCH_INGEST, new_callable=AsyncMock, return_value=("s", "t", "c")):
            await process_github_url("https://github.com/single", dest_folder, None)

        # Fallback naming when fewer than 2 path parts
        files = list(dest_folder.iterdir())
        assert len(files) == 1
        assert files[0].suffix == ".md"

    async def test_base64_images_stripped(self, dest_folder):
        fake_content = '![img](data:image/png;base64,iVBORw0KGgoAAAA) rest'
        with patch(_PATCH_INGEST, new_callable=AsyncMock, return_value=("s", "t", fake_content)):
            await process_github_url("https://github.com/a/b", dest_folder, None)
        md = (dest_folder / "a_b.md").read_text(encoding="utf-8")
        assert "data:image/png;base64" not in md
        assert "[... base64 image removed ...]" in md

    async def test_truncation_when_content_too_long(self, dest_folder):
        huge_content = "x" * 200_000
        with patch(_PATCH_INGEST, new_callable=AsyncMock, return_value=("s", "t", huge_content)):
            await process_github_url("https://github.com/a/b", dest_folder, None)
        md = (dest_folder / "a_b.md").read_text(encoding="utf-8")
        assert len(md) <= 65_000 + 200  # header + truncation message overhead
        assert "[... Content truncated due to length ...]" in md

    async def test_ingestion_failure_returns_false_and_writes_error(self, dest_folder):
        with patch(_PATCH_INGEST, new_callable=AsyncMock, side_effect=RuntimeError("network down")):
            result = await process_github_url("https://github.com/a/b", dest_folder, None)

        assert result is False
        md = (dest_folder / "a_b.md").read_text(encoding="utf-8")
        assert "Error processing" in md
