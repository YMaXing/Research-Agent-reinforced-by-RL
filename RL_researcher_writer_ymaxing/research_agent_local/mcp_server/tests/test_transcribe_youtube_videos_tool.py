"""Unit tests for src/tools/transcribe_youtube_videos_tool.py.

``process_youtube_url`` is mocked so no real transcription or GenAI calls
are made.  Only file I/O and control-flow logic is tested.
"""

import json
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
)
from src.tools.transcribe_youtube_videos_tool import transcribe_youtube_videos_tool

_PATCH_PROCESS = "src.tools.transcribe_youtube_videos_tool.process_youtube_url"


def _setup_dir(tmp_path: Path, youtube_urls: list[str] | None = None) -> Path:
    """Create a valid research directory with guidelines_filenames.json."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# Topic", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()

    data = {"youtube_videos_urls": youtube_urls or []}
    (output / GUIDELINES_FILENAMES_FILE).write_text(
        json.dumps(data), encoding="utf-8"
    )
    return tmp_path


class TestTranscribeYoutubeVideosTool:
    async def test_success_processes_urls(self, tmp_path):
        urls = ["https://youtube.com/watch?v=abc", "https://youtube.com/watch?v=xyz"]
        research_dir = _setup_dir(tmp_path, urls)

        with patch(_PATCH_PROCESS, new_callable=AsyncMock) as mock_proc:
            result = await transcribe_youtube_videos_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["videos_processed"] == 2
        assert result["videos_total"] == 2
        assert mock_proc.await_count == 2

        # Output folder was created
        yt_folder = research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER
        assert yt_folder.is_dir()

    async def test_empty_urls(self, tmp_path):
        research_dir = _setup_dir(tmp_path, [])

        result = await transcribe_youtube_videos_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["videos_processed"] == 0

    async def test_no_youtube_key_in_json(self, tmp_path):
        """JSON exists but has no youtube_videos_urls key."""
        (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# T", encoding="utf-8")
        output = tmp_path / RESEARCH_OUTPUT_FOLDER
        output.mkdir()
        (output / GUIDELINES_FILENAMES_FILE).write_text("{}", encoding="utf-8")

        result = await transcribe_youtube_videos_tool(str(tmp_path))

        assert result["videos_processed"] == 0

    async def test_raises_for_missing_json(self, tmp_path):
        """Should raise when guidelines_filenames.json is absent."""
        (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# T", encoding="utf-8")
        (tmp_path / RESEARCH_OUTPUT_FOLDER).mkdir()

        with pytest.raises(ValueError):
            await transcribe_youtube_videos_tool(str(tmp_path))

    async def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            await transcribe_youtube_videos_tool("/nonexistent/path")

    async def test_passes_semaphore_and_dest_folder(self, tmp_path):
        """Verify correct positional args forwarded to process_youtube_url."""
        urls = ["https://youtube.com/watch?v=abc"]
        research_dir = _setup_dir(tmp_path, urls)

        with patch(_PATCH_PROCESS, new_callable=AsyncMock) as mock_proc:
            await transcribe_youtube_videos_tool(str(research_dir))

        call_args = mock_proc.call_args
        # First arg: url, second: dest_folder (Path), third: semaphore
        assert call_args.args[0] == urls[0]
        dest = call_args.args[1]
        assert dest == research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER
