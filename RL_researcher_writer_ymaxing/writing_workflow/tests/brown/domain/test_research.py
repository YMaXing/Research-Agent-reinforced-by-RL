"""Tests for brown.entities.research module."""

from brown.entities.research import Research


class TestResearch:
    """Test the Research class."""

    def test_research_creation(self) -> None:
        """Test creating a research object."""
        content = "# Research\n\nThis is research content."
        research = Research(content=content)
        assert research.content == content

    def test_research_to_context(self) -> None:
        """Test research context generation."""
        research = Research(content="# Research\n\nAI research findings")
        context = research.to_context()

        assert "<research>" in context
        assert "</research>" in context
        assert "# Research\n\nAI research findings" in context

    def test_research_empty_content(self) -> None:
        """Test research with empty content."""
        research = Research(content="")
        assert research.content == ""

        context = research.to_context()
        assert "<research>" in context
        assert "</research>" in context

    def test_research_complex_content(self) -> None:
        """Test research with complex content."""
        content = """# Research: Machine Learning

## Overview
Machine learning is a subset of AI.

## Key Concepts
- Supervised learning
- Unsupervised learning
- Reinforcement learning

## Applications
- Image recognition
- Natural language processing
- Recommendation systems

## References
- [Deep Learning Book](https://example.com/book)
- [ML Course](https://example.com/course)
"""
        research = Research(content=content)
        assert research.content == content

        context = research.to_context()
        assert "Machine Learning" in context
        assert "Key Concepts" in context
        assert "Applications" in context
        assert "References" in context

    # --- is_format_a ---

    def test_research_is_format_a_true(self) -> None:
        """Test is_format_a returns True for Format A content."""
        research = Research(content="# Comprehensive Research Report\n\nSome content.")
        assert research.is_format_a is True

    def test_research_is_format_a_leading_whitespace(self) -> None:
        """Test is_format_a handles leading whitespace before the heading."""
        research = Research(content="  \n\n# Comprehensive Research Report\n\nSome content.")
        assert research.is_format_a is True

    def test_research_is_format_a_false(self) -> None:
        """Test is_format_a returns False for Format B content."""
        research = Research(content="<golden_source>Some source content</golden_source>")
        assert research.is_format_a is False

    # --- _exploration_sources ---

    def test_research_exploration_sources_format_a_empty(self) -> None:
        """Test _exploration_sources returns empty string for Format A regardless of XML tags present."""
        content = '# Comprehensive Research Report\n\n<research_source phase="exploration">Source</research_source>'
        research = Research(content=content)
        assert research._exploration_sources == ""

    def test_research_exploration_sources_no_exploration_blocks(self) -> None:
        """Test _exploration_sources returns empty string when no exploration blocks are present."""
        content = '<golden_source>Content</golden_source>\n<research_source phase="exploitation">Exploit</research_source>'
        research = Research(content=content)
        assert research._exploration_sources == ""

    def test_research_exploration_sources_extracts_blocks(self) -> None:
        """Test _exploration_sources extracts only exploration blocks from Format B."""
        content = (
            "<golden_source>Core content</golden_source>\n\n"
            '<research_source phase="exploitation">Exploit source</research_source>\n\n'
            '<research_source phase="exploration">Explore source 1</research_source>\n\n'
            '<research_source phase="exploration">Explore source 2</research_source>'
        )
        research = Research(content=content)
        sources = research._exploration_sources
        assert "Explore source 1" in sources
        assert "Explore source 2" in sources
        assert "Exploit source" not in sources
        assert "Core content" not in sources

    # --- to_reviewer_context ---

    def test_research_to_reviewer_context_format_a(self) -> None:
        """Test to_reviewer_context returns Format A skip message."""
        research = Research(content="# Comprehensive Research Report\n\nSome content.")
        context = research.to_reviewer_context()
        assert "Format A" in context
        assert "Skip all exploration integration checks" in context
        assert "<exploration_sources>" not in context

    def test_research_to_reviewer_context_format_b_no_sources(self) -> None:
        """Test to_reviewer_context returns Format B no-sources skip message."""
        research = Research(content="<golden_source>Content</golden_source>")
        context = research.to_reviewer_context()
        assert "Format B" in context
        assert "Skip all exploration integration checks" in context
        assert "<exploration_sources>" not in context

    def test_research_to_reviewer_context_format_b_with_sources(self) -> None:
        """Test to_reviewer_context returns Format B block with exploration sources."""
        content = (
            '<golden_source>Core content</golden_source>\n\n<research_source phase="exploration">Exploration insight</research_source>'
        )
        research = Research(content=content)
        context = research.to_reviewer_context()
        assert "Format B" in context
        assert "<exploration_sources>" in context
        assert "Exploration insight" in context
        assert "</exploration_sources>" in context
        assert "Skip all exploration integration checks" not in context

    def test_research_str_representation(self) -> None:
        """Test string representation."""
        research = Research(content="Test research content")
        str_repr = str(research)

        assert "Research(len_content=21, len_image_urls=0)" in str_repr
