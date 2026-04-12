"""Tavily research handler - exact drop-in compatibility with your existing pipeline."""

import asyncio
import logging
import re
from pathlib import Path
from typing import Dict, List, Tuple

from openai import InternalServerError, RateLimitError
from pydantic import BaseModel, Field

from ..config.constants import TAVILY_RESULTS_FILE
from ..config.prompts import PROMPT_WEB_SEARCH
from ..utils.llm_utils import get_chat_model, get_tavily_tool

from ..config.settings import settings

logger = logging.getLogger(__name__)


class SourceAnswer(BaseModel):
    """A single source answer with URL and content."""
    url: str = Field(description="The URL of the source")
    queries: List[str] = Field(description="The queries that led to this source")
    phase: str = Field(description="The research phase this source originated from (Exploitation or Exploration)")
    answer: str = Field(description="The detailed answer extracted from that source")


class SearchResponse(BaseModel):
    """Structured response from search containing multiple sources."""
    sources: List[SourceAnswer] = Field(description="List of sources with their answers")


async def run_tavily_search(query: str) -> Tuple[str, Dict[int, str], Dict[int, str]]:
    """Run Tavily + strong LLM structuring"""
    
    # 1. Tavily retrieval (rich raw_content + advanced depth)
    tavily_tool = get_tavily_tool("tavily")
    logger.info(f"🔍 Running Tavily search for: {query}")
    tavily_results = await tavily_tool.ainvoke({"query": query})   # returns List[dict] with raw_content

    # Truncate raw_content per result to stay well within the model's context window.
    # 5 results × 8 000 chars ≈ 40 000 chars (~10 K tokens) — generous but bounded.
    _RAW_CONTENT_CHAR_LIMIT = 8_000
    if isinstance(tavily_results, list):
        for result in tavily_results:
            if isinstance(result, dict) and isinstance(result.get("raw_content"), str):
                result["raw_content"] = result["raw_content"][:_RAW_CONTENT_CHAR_LIMIT]

    # 2. Strong LLM synthesis (better than Sonar for technical content)
    # Use include_raw=True so we can inspect what the model actually returned if parsing fails.
    # PydanticToolsParser (used internally by with_structured_output) returns parsed=None when the
    # model emits plain text instead of a tool call — this is guarded against by the raw_content
    # truncation above, which keeps the total prompt within the model's context window.
    base_llm = get_chat_model(settings.search_enhancement_model)
    struct_llm = base_llm.with_structured_output(SearchResponse, include_raw=True)

    # Optional: enhance the prompt with Tavily results
    enhanced_prompt = (
        PROMPT_WEB_SEARCH.format(query=query)
        + f"\n\nUse the following high-quality search results as source material:\n{tavily_results}"
    )

    # Retry with exponential back-off on transient 503 / rate-limit errors.
    _MAX_RETRIES = 4
    _BASE_DELAY = 5.0  # seconds
    last_exc: Exception | None = None
    for attempt in range(_MAX_RETRIES):
        try:
            raw_result = await struct_llm.ainvoke(enhanced_prompt)
            break
        except (InternalServerError, RateLimitError) as exc:
            last_exc = exc
            status = getattr(exc, "status_code", None)
            if status not in (429, 503) and not isinstance(exc, RateLimitError):
                raise
            delay = _BASE_DELAY * (2 ** attempt)
            logger.warning(
                f"⚠️ LLM returned {status} for query {query!r} "
                f"(attempt {attempt + 1}/{_MAX_RETRIES}). "
                f"Retrying in {delay:.0f}s…"
            )
            await asyncio.sleep(delay)
    else:
        raise last_exc  # all retries exhausted

    response = raw_result.get("parsed") if isinstance(raw_result, dict) else raw_result

    if response is None or not hasattr(response, "sources") or response.sources is None:
        parsing_error = raw_result.get("parsing_error") if isinstance(raw_result, dict) else None
        raw_output = raw_result.get("raw") if isinstance(raw_result, dict) else None
        # Extract the actual text the model emitted instead of a tool call
        raw_text = getattr(raw_output, "content", None) if raw_output is not None else None
        tool_calls = getattr(raw_output, "tool_calls", None) if raw_output is not None else None
        logger.warning(
            f"⚠️ LLM returned no structured response for query: {query!r}.\n"
            f"  parsing_error : {parsing_error!r}\n"
            f"  prompt_length : {len(enhanced_prompt)}\n"
            f"  tool_calls    : {tool_calls!r}\n"
            f"  raw_content   : {raw_text!r}"
        )
        return "", {}, {}

    # 3. Convert to the exact format your append function expects
    answer_by_source: Dict[int, str] = {}
    citations: Dict[int, str] = {}
    for i, source in enumerate(response.sources, 1):
        answer_by_source[i] = source.answer
        citations[i] = source.url

    # Build full_answer for backward compatibility
    full_answer_lines = []
    for i, source in enumerate(response.sources, 1):
        full_answer_lines.append(f"### [{i}]: {source.url}")
        full_answer_lines.append(source.answer)
        full_answer_lines.append("")
    full_answer = "\n".join(full_answer_lines)

    return full_answer, answer_by_source, citations

def compute_next_source_id(results_path: Path) -> int:
    """Compute the next available source ID by finding the highest existing ID."""
    if not results_path.exists():
        return 1
    pattern = re.compile(r"### Source \[(\d+)\]:")
    max_id = 0
    for line in results_path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1


def append_tavily_results(
    results_path: Path,
    query: str,
    answer_by_source: Dict[int, str],
    citations: Dict[int, str],
    starting_id: int,
    phase: str = "[EXPLOITATION]",
) -> int:
    """Append results for a single query. Returns next available global id."""
    with results_path.open("a", encoding="utf-8") as f:
        last_id = starting_id
        for local_id, url in citations.items():
            content = answer_by_source.get(local_id, "").strip()
            if not content:
                continue
            f.write(f"Phase: {phase}\n\n")
            f.write(f"### Source [{last_id}]: {url}\n\n")
            f.write(f"Query: {query}\n\n")
            f.write(f"Answer: {content}\n\n")
            f.write("-----\n\n")
            last_id += 1
    return last_id


async def run_queries(article_id: str, queries: List[str]) -> None:
    if not queries:
        logger.warning("⚠️  No queries supplied - nothing to do.")
        return

    base_dir = Path("articles") / article_id
    results_path = base_dir / TAVILY_RESULTS_FILE

    # Ensure output directory and file exist
    results_path.parent.mkdir(parents=True, exist_ok=True)
    results_path.touch(exist_ok=True)

    next_global_id = compute_next_source_id(results_path)

    logger.info(f"Executing {len(queries)} Tavily queries concurrently...")
    tasks = [run_tavily_search(query) for query in queries]
    search_results = await asyncio.gather(*tasks)
    logger.info("...all Tavily queries finished. Appending results.")

    for query, (_, answer_by_source, citations) in zip(queries, search_results):
        if citations:
            next_global_id = append_tavily_results(
                results_path,
                query,
                answer_by_source,
                citations,
                next_global_id,
            )
            logger.info(f"Appended results for query: '{query}' (added {len(citations)} source section(s)).")

    logger.info(f"\n✅ Completed Tavily research round. Results saved to {results_path}.")


def extract_tavily_chunks(markdown: str) -> Dict[int, str]:
    """Return a map {source_id: markdown_block} for each source block in the file.

    Each block starts with an optional ``Phase: [...]`` line followed by
    ``### Source [<id>]: <url>`` and ends before the next block or EOF.
    Backward compatible with the old format where Phase appeared after Query.
    """
    # Match the optional Phase line that precedes ### Source, or ### Source alone
    # (backward compat for old format where Phase was not at the top of each block).
    # The optional group is non-capturing so group(1) is always the source ID.
    pattern = re.compile(r"^(?:Phase: [^\n]+\n\n)?### Source \[(\d+)]\:", re.MULTILINE)
    chunks: Dict[int, str] = {}

    matches = list(pattern.finditer(markdown))
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        source_id = int(match.group(1))
        chunks[source_id] = markdown[start:end].strip()
    return chunks


def group_tavily_by_query(chunks: Dict[int, str], selected_ids: List[int]) -> Dict[str, List[str]]:
    """
    Group source blocks by their query string. Returns {query: [block, ...]}.
    Only includes blocks whose source_id is in selected_ids.
    """
    query_to_blocks = {}
    for src_id in selected_ids:
        block = chunks.get(src_id)
        if not block:
            continue
        query_match = re.search(r"^Query:\s*(.+)$", block, re.MULTILINE)
        query = query_match.group(1).strip() if query_match else f"Query for Source [{src_id}]"
        query_to_blocks.setdefault(query, []).append(block)
    return query_to_blocks
