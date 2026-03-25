"""Unit tests for src/app/youtube_handler.py.

``get_video_id`` is a pure function — no mocking needed.
``process_youtube_url`` and ``transcribe_youtube`` are async and call the
Google GenAI client; we mock the client to avoid real API calls.
"""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.app.youtube_handler import get_video_id, process_youtube_url


# ---------------------------------------------------------------------------
# get_video_id (pure function)
# ---------------------------------------------------------------------------


class TestGetVideoId:
    def test_standard_youtube_url(self):
        assert get_video_id("https://www.youtube.com/watch?v=abc123") == "abc123"

    def test_short_youtu_be_url(self):
        assert get_video_id("https://youtu.be/xyz789") == "xyz789"

    def test_youtube_url_with_extra_params(self):
        vid = get_video_id("https://www.youtube.com/watch?v=abc&t=120")
        assert vid == "abc"

    def test_non_youtube_url_returns_none(self):
        assert get_video_id("https://example.com/page") is None

    def test_empty_string(self):
        assert get_video_id("") is None

    def test_youtube_no_v_param(self):
        assert get_video_id("https://www.youtube.com/channel/UCxyz") is None


# ---------------------------------------------------------------------------
# process_youtube_url
# ---------------------------------------------------------------------------


class TestProcessYoutubeUrl:
    async def test_creates_output_file_with_video_id_name(self, tmp_path):
        """Verifies the output filename is derived from the video id."""
        with patch("src.app.youtube_handler.transcribe_youtube", new_callable=AsyncMock) as mock_transcribe:
            semaphore = asyncio.Semaphore(2)
            await process_youtube_url("https://www.youtube.com/watch?v=test_vid", tmp_path, semaphore)

        mock_transcribe.assert_awaited_once()
        call_kwargs = mock_transcribe.call_args
        output_path = call_kwargs.kwargs.get("output_path") or call_kwargs.args[1]
        assert output_path.name == "test_vid.md"

    async def test_fallback_filename_for_unparseable_url(self, tmp_path):
        with patch("src.app.youtube_handler.transcribe_youtube", new_callable=AsyncMock) as mock_transcribe:
            semaphore = asyncio.Semaphore(2)
            await process_youtube_url("https://example.com/no-video-id", tmp_path, semaphore)

        call_kwargs = mock_transcribe.call_args
        output_path = call_kwargs.kwargs.get("output_path") or call_kwargs.args[1]
        assert output_path.suffix == ".md"
        # Fallback name should be sanitized URL
        assert "example.com" in output_path.stem
