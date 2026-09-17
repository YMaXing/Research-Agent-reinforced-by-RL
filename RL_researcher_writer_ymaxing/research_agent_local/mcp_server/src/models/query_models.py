"""Pydantic models for query generation and research operations."""

from typing import List

from pydantic import BaseModel, Field
from typing_extensions import Literal

# Shared constant so the handler's shorten loop uses the same limit as the schema hint.
_MAX_QUERY_CHARS = 200


class QueryAndReason(BaseModel):
    """A single web-search query and the reason for it."""

    question: str = Field(
        description=(
            "A concise web-search question (≤ 15 words). "
            "Must address a single, specific concept. "
            "Do NOT combine multiple sub-questions or paste guideline text verbatim."
        ),
        max_length=_MAX_QUERY_CHARS,
    )
    reason: str = Field(description="The reason why this question is important for the research.")


class GeneratedQueries(BaseModel):
    """A list of generated web-search queries and their reasons."""

    queries: List[QueryAndReason] = Field(description="A list of web-search queries and their reasons.")


class SourceSelection(BaseModel):
    """Structured response expected from the LLM."""

    selection_type: Literal["none", "all", "specific"] = Field(
        description=(
            "Type of selection made: 'none' for no sources, 'all' for all sources, "
            "or 'specific' for specific source IDs"
        )
    )
    source_ids: List[int] = Field(
        description="List of selected source IDs. Empty for 'none', all IDs for 'all', or specific IDs for 'specific'"
    )


class TopSourceSelection(BaseModel):
    """Expected structure from the LLM when choosing the top sources."""

    selected_urls: List[str] = Field(description="List of URLs to scrape in full, ordered by priority.")
    reasoning: str = Field(description="Short explanation summarising why these URLs were chosen.")
