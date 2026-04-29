"""Tests for _build_exploration_sources in rl_grading_generator.py."""

from pathlib import Path

from rl_grading_generator import _build_exploration_sources

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_BLOCK_SEP = "-----"

_EXPLORATION_BLOCK = """\

Phase: [EXPLORATION]

### Source [1]: https://example.com/explore-a

Query: What are the theoretical tradeoffs in LLM autonomy?

Answer: First sentence about autonomy. Second sentence expanding on it.
"""

_EXPLOITATION_BLOCK = """\

Phase: [EXPLOITATION]

### Source [2]: https://example.com/exploit-b

Query: What is the basic definition of agents?

Answer: Agents are systems that perceive their environment and take actions.
"""

_EXPLORATION_BLOCK_2 = """\

Phase: [EXPLORATION]

### Source [3]: https://example.com/explore-c

Query: How do multi-agent systems scale?

Answer: Multi-agent systems scale horizontally. Each agent handles a sub-task.
"""


def _write_tavily(research_dir: Path, content: str) -> None:
    research_dir.mkdir(parents=True, exist_ok=True)
    (research_dir / "tavily_results_selected.md").write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestBuildExplorationSources:
    def test_returns_none_when_tavily_file_missing(self, tmp_path: Path) -> None:
        """Returns None when tavily_results_selected.md does not exist."""
        result = _build_exploration_sources(tmp_path)
        assert result is None

    def test_returns_none_when_no_exploration_blocks(self, tmp_path: Path) -> None:
        """Returns None when all blocks are EXPLOITATION-phase."""
        content = _EXPLOITATION_BLOCK
        _write_tavily(tmp_path, content)
        result = _build_exploration_sources(tmp_path)
        assert result is None

    def test_returns_exploration_blocks_without_url_phases(self, tmp_path: Path) -> None:
        """All EXPLORATION blocks are returned even when url_phases.json is absent."""
        content = _BLOCK_SEP.join(["", _EXPLORATION_BLOCK, _EXPLORATION_BLOCK_2])
        _write_tavily(tmp_path, content)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "https://example.com/explore-a" in result
        assert "https://example.com/explore-c" in result

    def test_excludes_exploitation_blocks(self, tmp_path: Path) -> None:
        """EXPLOITATION blocks are excluded; only EXPLORATION blocks appear."""
        content = _BLOCK_SEP.join(["", _EXPLOITATION_BLOCK, _EXPLORATION_BLOCK])
        _write_tavily(tmp_path, content)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "https://example.com/explore-a" in result
        assert "https://example.com/exploit-b" not in result

    def test_all_exploration_entries_returned_regardless_of_url_phases(self, tmp_path: Path) -> None:
        """All EXPLORATION entries from tavily_results_selected.md are included,
        even if url_phases.json only lists a subset of those URLs.
        This verifies that url_phases.json is not used as a filter."""
        # url_phases.json only references explore-a, not explore-c
        url_phases = {"https://example.com/explore-a": "[EXPLORATION]"}
        (tmp_path / "url_phases.json").write_text(__import__("json").dumps(url_phases), encoding="utf-8")
        content = _BLOCK_SEP.join(["", _EXPLORATION_BLOCK, _EXPLORATION_BLOCK_2])
        _write_tavily(tmp_path, content)

        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "https://example.com/explore-a" in result
        # explore-c must also appear despite not being in url_phases.json
        assert "https://example.com/explore-c" in result

    def test_snippet_only_entries_included(self, tmp_path: Path) -> None:
        """Snippet-only entries (tagged [EXPLORATION] but never selected for scraping)
        are included — this is the primary use-case the fallback was introduced for."""
        # 3 exploration blocks, none of their URLs in url_phases.json
        content = _BLOCK_SEP.join(["", _EXPLORATION_BLOCK, _EXPLOITATION_BLOCK, _EXPLORATION_BLOCK_2])
        _write_tavily(tmp_path, content)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "https://example.com/explore-a" in result
        assert "https://example.com/explore-c" in result
        assert "https://example.com/exploit-b" not in result

    def test_query_included_in_entry(self, tmp_path: Path) -> None:
        """Each entry contains its Query line."""
        _write_tavily(tmp_path, _EXPLORATION_BLOCK)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "What are the theoretical tradeoffs in LLM autonomy?" in result

    def test_answer_summary_included_in_entry(self, tmp_path: Path) -> None:
        """Each entry contains a summary (first 2 sentences) of the Answer."""
        _write_tavily(tmp_path, _EXPLORATION_BLOCK)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "First sentence about autonomy." in result

    def test_answer_truncated_at_300_chars(self, tmp_path: Path) -> None:
        """Answers longer than 300 chars are truncated with '...'."""
        long_answer = "X" * 400 + "."
        block = f"""
Phase: [EXPLORATION]

### Source [1]: https://example.com/long

Query: Long answer query.

Answer: {long_answer}
"""
        _write_tavily(tmp_path, block)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "..." in result
        # Summary portion must not exceed 300 + len("...") chars
        lines = result.splitlines()
        summary_line = next((line for line in lines if line.strip().startswith("Summary:")), None)
        assert summary_line is not None
        summary_value = summary_line.split("Summary:", 1)[1].strip()
        assert len(summary_value) <= 303  # 300 + "..."

    def test_header_present_in_output(self, tmp_path: Path) -> None:
        """The standard exploration-sources header is included."""
        _write_tavily(tmp_path, _EXPLORATION_BLOCK)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "exploration phase" in result
        assert "Depth and breadth additions score 1" in result

    def test_entry_format(self, tmp_path: Path) -> None:
        """Each entry follows the '- url\\n  Query: ...\\n  Summary: ...' format."""
        _write_tavily(tmp_path, _EXPLORATION_BLOCK)
        result = _build_exploration_sources(tmp_path)
        assert result is not None
        assert "- https://example.com/explore-a" in result
        assert "  Query:" in result
        assert "  Summary:" in result
