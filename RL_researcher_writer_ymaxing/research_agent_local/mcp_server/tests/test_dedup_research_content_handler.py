"""Unit tests for src/app/dedup_research_content_handler.py.

All tests replace get_chat_model with a fake deterministic model to avoid
any real LLM API calls.
"""

from pathlib import Path
from unittest.mock import patch

import pytest

from src.app.dedup_research_content_handler import deduplicate_research_content
from src.config.constants import (
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_FOLDER,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    URLS_FROM_RESEARCH_FOLDER,
)

_PATCH_TARGET = "src.app.dedup_research_content_handler.get_chat_model"


def _write_source_files(output_path: Path) -> None:
    golden = output_path / URLS_FROM_GUIDELINES_FOLDER
    code = output_path / URLS_FROM_GUIDELINES_CODE_FOLDER
    youtube = output_path / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER

    golden.mkdir(parents=True, exist_ok=True)
    code.mkdir(parents=True, exist_ok=True)
    youtube.mkdir(parents=True, exist_ok=True)

    (golden / "g1.md").write_text("Guideline content A", encoding="utf-8")
    (golden / "g2.md").write_text("Guideline content B", encoding="utf-8")
    (code / "c1.md").write_text("Code summary content", encoding="utf-8")
    (youtube / "y1.md").write_text("Transcript content", encoding="utf-8")
    research_urls = output_path / URLS_FROM_RESEARCH_FOLDER
    research_urls.mkdir(parents=True, exist_ok=True)
    (research_urls / "r1.md").write_text("Research URL extraction content", encoding="utf-8")


class TestDeduplicateResearchContent:
    async def test_collects_sources_and_returns_counts(self, fake_plain_model_factory, tmp_research_dir):
        output_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        _write_source_files(output_path)

        model = fake_plain_model_factory("# Deduplicated\n\nCleaned output")
        with patch(_PATCH_TARGET, return_value=model):
            deduplicated_md, source_counts, total_parts = await deduplicate_research_content(
                tmp_research_dir, output_path
            )

        assert deduplicated_md == "# Deduplicated\n\nCleaned output"
        assert source_counts["golden/guideline"] == 2
        assert source_counts["research_urls"] == 1
        assert source_counts["code summaries"] == 1
        assert source_counts["YouTube transcripts"] == 1
        assert total_parts == 5

    async def test_prompt_contains_guidelines_and_collected_content(
        self, fake_plain_model_factory, tmp_research_dir
    ):
        output_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        _write_source_files(output_path)

        prompts_seen = []
        model = fake_plain_model_factory("# dedup")
        original = model.ainvoke

        async def spy(prompt, **kw):
            prompts_seen.append(str(prompt))
            return await original(prompt, **kw)

        model.ainvoke = spy

        with patch(_PATCH_TARGET, return_value=model):
            await deduplicate_research_content(tmp_research_dir, output_path)

        assert prompts_seen, "ainvoke was not called"
        prompt_text = prompts_seen[0]
        assert "RAG Systems" in prompt_text
        assert "Guideline content A" in prompt_text
        assert "Code summary content" in prompt_text
        assert "Transcript content" in prompt_text
        assert "Research URL extraction content" in prompt_text

    async def test_uses_none_when_guidelines_file_missing(self, fake_plain_model_factory, tmp_path):
        research_path = tmp_path
        output_path = research_path / RESEARCH_OUTPUT_FOLDER
        output_path.mkdir(parents=True, exist_ok=True)
        research_urls_dir = output_path / URLS_FROM_RESEARCH_FOLDER
        research_urls_dir.mkdir(parents=True, exist_ok=True)
        (research_urls_dir / "r1.md").write_text("Only content", encoding="utf-8")

        prompts_seen = []
        model = fake_plain_model_factory("# dedup")
        original = model.ainvoke

        async def spy(prompt, **kw):
            prompts_seen.append(str(prompt))
            return await original(prompt, **kw)

        model.ainvoke = spy

        with patch(_PATCH_TARGET, return_value=model):
            await deduplicate_research_content(research_path, output_path)

        assert "<none>" in prompts_seen[0]

    async def test_raises_when_no_sources_found(self, fake_plain_model_factory, tmp_research_dir):
        output_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        output_path.mkdir(parents=True, exist_ok=True)

        model = fake_plain_model_factory("# dedup")
        with patch(_PATCH_TARGET, return_value=model):
            with pytest.raises(ValueError, match="No valid content found"):
                await deduplicate_research_content(tmp_research_dir, output_path)

    async def test_raises_runtime_error_when_llm_call_fails(self, tmp_research_dir):
        output_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        output_path.mkdir(parents=True, exist_ok=True)
        research_urls_dir = output_path / URLS_FROM_RESEARCH_FOLDER
        research_urls_dir.mkdir(parents=True, exist_ok=True)
        (research_urls_dir / "r1.md").write_text("Only content", encoding="utf-8")

        class FailingModel:
            async def ainvoke(self, prompt, **kwargs):
                raise RuntimeError("synthetic llm failure")

        with patch(_PATCH_TARGET, return_value=FailingModel()):
            with pytest.raises(RuntimeError, match="Content deduplication LLM call failed"):
                await deduplicate_research_content(tmp_research_dir, output_path)

    async def test_raises_runtime_error_when_llm_returns_empty_content(
        self, fake_plain_model_factory, tmp_research_dir
    ):
        output_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        output_path.mkdir(parents=True, exist_ok=True)
        research_urls_dir = output_path / URLS_FROM_RESEARCH_FOLDER
        research_urls_dir.mkdir(parents=True, exist_ok=True)
        (research_urls_dir / "r1.md").write_text("Only content", encoding="utf-8")

        model = fake_plain_model_factory("   ")
        with patch(_PATCH_TARGET, return_value=model):
            with pytest.raises(RuntimeError, match="Content deduplication LLM call failed"):
                await deduplicate_research_content(tmp_research_dir, output_path)