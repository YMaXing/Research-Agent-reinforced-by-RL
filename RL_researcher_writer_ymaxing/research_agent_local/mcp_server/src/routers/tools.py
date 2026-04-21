"""MCP Tools registration for research operations."""

from typing import Any, Dict, Literal

import opik
from fastmcp import FastMCP


from ..tools import (
    create_research_file_tool,
    extract_guidelines_urls_tool,
    predict_exploration_preset_tool,
    generate_next_queries_tool,
    generate_next_complementary_queries_tool,
    run_tavily_research_tool,
    process_github_urls_tool,
    process_local_files_tool,
    scrape_and_clean_other_urls_tool,
    scrape_exploitation_guideline_urls_tool,
    scrape_research_urls_tool,
    select_research_sources_to_keep_tool,
    select_research_sources_to_scrape_tool,
    transcribe_youtube_videos_tool,
    deduplicate_new_queries_tool,
    deduplicate_research_content_tool,
)
from ..utils.opik_utils import opik_context
from ..config.settings import settings


def register_mcp_tools(mcp: FastMCP) -> None:
    """Register all MCP tools with the server instance."""

    # ============================================================================
    # URL AND FILE EXTRACTION TOOLS
    # ============================================================================

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def extract_guidelines_urls(research_directory: str) -> Dict[str, Any]:
        """
        Extract URLs and local file references from article guidelines.

        Reads the ARTICLE_GUIDELINE_FILE file in the research directory and extracts:
        - GitHub URLs
        - Other HTTP/HTTPS URLs
        - Local file references (files mentioned in quotes with extensions)

        Results are saved to GUIDELINES_FILENAMES_FILE in the research directory.

        Args:
            research_directory: Path to the research directory containing ARTICLE_GUIDELINE_FILE

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - github_sources_count: Number of GitHub URLs found
                - youtube_sources_count: Number of YouTube URLs found
                - web_sources_count: Number of other web URLs found
                - local_files_count: Number of local file references found
                - output_path: Path to the generated GUIDELINES_FILENAMES_FILE
                - message: Human-readable success message
        """

        opik_context.update_thread_id()

        result = extract_guidelines_urls_tool(research_directory)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def process_local_files(research_directory: str) -> Dict[str, Any]:
        """
        Process local files referenced in the article guidelines.

        Reads the GUIDELINES_FILENAMES_FILE file and copies each referenced local file
        to the LOCAL_FILES_FROM_RESEARCH_FOLDER subfolder. Path separators in filenames are
        replaced with underscores to avoid creating nested folders.

        Args:
            research_directory: Path to the research directory containing GUIDELINES_FILENAMES_FILE

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - files_processed: List of successfully processed files
                - files_failed: List of files that failed to process
                - total_files: Total number of files processed
                - files_copied_count: Number of files successfully copied
                - files_failed_count: Number of files that failed to copy
                - output_directory: Path to the output directory
                - message: Human-readable success message with processing results
        """

        opik_context.update_thread_id()

        result = process_local_files_tool(research_directory)
        return result

    # ============================================================================
    # WEB SCRAPING AND CONTENT PROCESSING TOOLS
    # ============================================================================

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def scrape_and_clean_other_urls(research_directory: str, concurrency_limit: int = 4) -> Dict[str, Any]:
        """
        Scrape and clean other URLs (including arxiv URLs) from GUIDELINES_FILENAMES_FILE.

        Reads the GUIDELINES_FILENAMES_FILE file and scrapes/cleans each URL listed
        under 'other_urls'. The cleaned markdown content is saved to the
        URLS_FROM_GUIDELINES_FOLDER subfolder with appropriate filenames.

        Args:
            research_directory: Path to the research directory containing GUIDELINES_FILENAMES_FILE
            concurrency_limit: Maximum number of concurrent tasks for scraping (default: 4)

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - urls_processed: List of successfully processed URLs
                - urls_failed: List of URLs that failed to process
                - total_urls: Total number of URLs processed
                - successful_urls_count: Number of URLs successfully scraped
                - failed_urls_count: Number of URLs that failed to scrape
                - output_directory: Path to the output directory
                - message: Human-readable success message with processing results
        """

        opik_context.update_thread_id()

        result = await scrape_and_clean_other_urls_tool(research_directory, concurrency_limit)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def scrape_exploitation_guideline_urls(
        research_directory: str, concurrency_limit: int = 4
    ) -> Dict[str, Any]:
        """
        Scrape URLs from the "Other Sources" section of the article guidelines (exploitation sources).

        Reads ``exploitation_github_urls``, ``exploitation_youtube_videos_urls``, and
        ``exploitation_other_urls`` from GUIDELINES_FILENAMES_FILE and processes each with
        its dedicated handler:
        - GitHub URLs → gitingest summary (process_github_urls)
        - YouTube URLs → transcript (transcribe_youtube_urls)
        - arXiv URLs → arxiv2markdown scrape
        - Other web URLs → firecrawl scrape + LLM clean

        All output is saved to URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER and tagged as
        ``<research_source type="guideline_exploitation">`` in the final research file.

        Args:
            research_directory: Path to the research directory containing GUIDELINES_FILENAMES_FILE.
            concurrency_limit: Maximum number of concurrent web scraping tasks (default: 4).

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success" or "warning")
                - github_processed: Number of GitHub URLs processed
                - youtube_processed: Number of YouTube URLs processed
                - arxiv_processed: Number of arXiv papers processed
                - web_processed: Number of web URLs processed
                - urls_total: Total number of exploitation URLs attempted
                - output_directory: Path to URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER
                - message: Human-readable summary
        """
        opik_context.update_thread_id()
        result = await scrape_exploitation_guideline_urls_tool(research_directory, concurrency_limit)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def process_github_urls(research_directory: str) -> Dict[str, Any]:
        """
        Process GitHub URLs from GUIDELINES_FILENAMES_FILE using gitingest.

        Reads the GUIDELINES_FILENAMES_FILE file and processes each URL listed
        under 'github_urls' using gitingest to extract repository summaries, file trees,
        and content. The results are saved as markdown files in the
        URLS_FROM_GUIDELINES_CODE_FOLDER subfolder.

        Args:
            research_directory: Path to the research directory containing GUIDELINES_FILENAMES_FILE

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - urls_processed: List of successfully processed GitHub URLs
                - urls_failed: List of GitHub URLs that failed to process
                - total_urls: Total number of GitHub URLs processed
                - successful_urls_count: Number of GitHub URLs successfully processed
                - failed_urls_count: Number of GitHub URLs that failed to process
                - output_directory: Path to the output directory
                - message: Human-readable success message with processing results
        """

        opik_context.update_thread_id()

        result = await process_github_urls_tool(research_directory)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def transcribe_youtube_urls(research_directory: str) -> Dict[str, Any]:
        """
        Transcribe YouTube video URLs from GUIDELINES_FILENAMES_FILE using an LLM.

        Reads the GUIDELINES_FILENAMES_FILE file and processes each URL listed
        under 'youtube_videos_urls'. Each video is transcribed, and the results are
        saved as markdown files in the URLS_FROM_GUIDELINES_YOUTUBE_FOLDER subfolder.

        Args:
            research_directory: Path to the research directory containing GUIDELINES_FILENAMES_FILE

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - urls_processed: List of successfully transcribed YouTube URLs
                - urls_failed: List of YouTube URLs that failed to transcribe
                - total_urls: Total number of YouTube URLs processed
                - successful_urls_count: Number of YouTube URLs successfully transcribed
                - failed_urls_count: Number of YouTube URLs that failed to transcribe
                - output_directory: Path to the output directory
                - message: Human-readable success message with processing results
        """

        opik_context.update_thread_id()

        result = await transcribe_youtube_videos_tool(research_directory)
        return result

    # ============================================================================
    # RESEARCH QUERY AND ANALYSIS TOOLS
    # ============================================================================

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def generate_next_queries(research_directory: str, n_queries: int = 5) -> Dict[str, Any]:
        """
        Generate candidate web-search queries for the next research round.

        Analyzes the article guidelines, already-scraped content, and existing Tavily
        results to identify knowledge gaps and propose new web-search questions.
        Each query includes a rationale explaining why it's important for the article.
        Results are saved to next_queries.md in the research directory.

        Args:
            research_directory: Path to the research directory containing article data
            n_queries: Number of queries to generate (default: 5)

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - queries_generated: List of generated query dictionaries with 'query' and 'rationale' keys
                - queries_count: Number of queries generated
                - output_path: Path to the generated next_queries.md file
                - message: Human-readable success message with generation results
        """

        opik_context.update_thread_id()

        result = await generate_next_queries_tool(research_directory, n_queries)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def run_tavily_research(
        research_directory: str,
        queries: list[str],
        query_source: Literal["exploitation", "complementary"] = "exploitation",
    ) -> Dict[str, Any]:
        """
        Run selected web-search queries with Tavily and store the results.

        Executes the provided queries using Tavily Search enhanced with strong LLM structuring and appends
        the results to tavily_results.md in the research directory. Each query
        result includes the answer and source citations, tagged with the research phase
        ("[EXPLOITATION]" for core queries, "[EXPLORATION]" for complementary queries).

        Args:
            research_directory: Path to the research directory where results will be saved
            queries: List of web-search queries to execute
            query_source: Origin of the current query batch – "exploitation" (default) for
                core exploitation rounds, or "complementary" for exploration rounds.
                Controls the Phase tag written to tavily_results.md.

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - queries_executed: List of queries that were successfully executed
                - queries_failed: List of queries that failed to execute
                - total_queries: Total number of queries processed
                - successful_queries_count: Number of queries successfully executed
                - failed_queries_count: Number of queries that failed to execute
                - total_sources: Total number of sources collected across all queries
                - output_path: Path to the updated tavily_results.md file
                - message: Human-readable success message with processing results
        """

        opik_context.update_thread_id()

        result = await run_tavily_research_tool(research_directory, queries, query_source=query_source)
        return result
    
    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def generate_next_complementary_queries(research_directory: str, 
                                                    n_queries: int = settings.n_exploration_queries_per_round, 
                                                    focus: Literal["balanced", "depth", "breadth"] = "balanced") -> Dict[str, Any]:
        """
        Generate complementary candidate web-search queries to explore uncovered but closely relevant aspects.

        Analyzes the article guidelines, already-scraped content, and existing Tavily results 
        to dive deeper into the content already covered in past research, and/or explore other uncovered aspects 
        that are closely related to past research and may expand the research scope, then propose new web-search questions.
        Each query includes a rationale explaining why it's important and what additional value it brings for the article.
        Results are saved to next_queries.md in the research directory.

        Args:
            research_directory: Path to the research directory containing article data
            n_queries: Number of queries to generate (default: settings.n_exploration_queries_per_round)
            focus: Focus of query generation, one of "balanced", "depth", or "breadth" (default: "balanced")

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - queries_generated: List of generated query dictionaries with 'query' and 'rationale' keys
                - queries_count: Number of queries generated
                - output_path: Path to the generated next_queries.md file
                - message: Human-readable success message with generation results
        """

        opik_context.update_thread_id()

        result = await generate_next_complementary_queries_tool(research_directory, n_queries, focus=focus)
        return result
    
    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def deduplicate_new_queries(
            research_directory: str,
            query_source: Literal["exploitation", "complementary"] = "exploitation",
        ) -> Dict[str, Any]:
        """
        Runs after every query generation round (exploitation or complementary).
        Deduplicates the new batch among themselves and against FULL_QUERIES_FILE history.
        Writes clean next_queries.md for run_tavily_research.

        Args:
            research_directory: Path to the research directory containing the output subdirectory with next_queries.md and full_queries.md
            query_source: Origin of the current query batch, one of "exploitation" or "complementary" (default: "exploitation")

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success" or "skipped")
                - new_queries_count: Total number of queries in the incoming batch
                - kept_count: Number of queries retained after deduplication
                - removed_duplicates: Number of queries dropped as duplicates
                - output_path: Path to the rewritten next_queries.md file
                - message: Human-readable summary of the operation
        """
        opik_context.update_thread_id()

        result = await deduplicate_new_queries_tool(research_directory, query_source=query_source)
        return result
    
    # ============================================================================
    # SOURCE SELECTION AND CURATION TOOLS
    # ============================================================================

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def select_research_sources_to_keep(research_directory: str) -> Dict[str, Any]:
        """
        Automatically select high-quality sources from Tavily results.

        Uses LLM to evaluate each source in tavily_results.md for trustworthiness,
        authority, and relevance based on the article guidelines and explorative research. 
        Writes the comma-separated IDs of accepted sources to tavily_sources_selected.md 
        and saves a filtered markdown file tavily_results_selected.md containing only the accepted sources.

        Args:
            research_directory: Path to the research directory (e.g., "articles/1")

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - sources_selected_count: Number of sources selected
                - selected_source_ids: List of IDs of selected sources
                - sources_selected_path: Path to the tavily_sources_selected.md file
                - results_selected_path: Path to the tavily_results_selected.md file
                - message: Human-readable success message with selection results
        """

        opik_context.update_thread_id()

        result = await select_research_sources_to_keep_tool(research_directory)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def select_research_sources_to_scrape(research_directory: str, max_sources: int = settings.maximum_sources_to_scrape) -> Dict[str, Any]:
        """
        Select up to max_sources priority research sources to scrape in full.

        Analyzes the filtered Tavily results together with the article guidelines and
        the material already scraped from guideline URLs, then chooses up to max_sources diverse,
        authoritative sources whose full content will add most value. The chosen URLs are
        written (one per line) to urls_to_scrape_from_research.md.

        Args:
            research_directory: Path to the research directory (e.g., "articles/1")
            max_sources: Maximum number of sources to select (default: settings.maximum_sources_to_scrape)

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - sources_selected: List of selected source URLs
                - sources_selected_count: Number of sources selected
                - output_path: Path to the urls_to_scrape_from_research.md file
                - reasoning: AI reasoning for why these sources were selected
                - message: Human-readable success message with selection results and reasoning
        """

        opik_context.update_thread_id()

        result = await select_research_sources_to_scrape_tool(research_directory, max_sources)
        return result

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def scrape_research_urls(research_directory: str, concurrency_limit: int = 4) -> Dict[str, Any]:
        """
        Scrape the selected research URLs for full content.

        Reads the URLs from urls_to_scrape_from_research.md and scrapes/cleans each URL's
        full content. The cleaned markdown files are saved to the urls_from_research
        subfolder with appropriate filenames.

        Args:
            research_directory: Path to the research directory containing urls_to_scrape_from_research.md
            concurrency_limit: Maximum number of concurrent tasks for scraping (default: 4)

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - urls_processed: List of successfully processed URLs
                - urls_failed: List of URLs that failed to process
                - total_urls: Total number of URLs processed
                - successful_urls_count: Number of URLs successfully scraped
                - failed_urls_count: Number of URLs that failed to scrape
                - output_directory: Path to the output directory
                - message: Human-readable success message with processing results
        """

        opik_context.update_thread_id()

        result = await scrape_research_urls_tool(research_directory, concurrency_limit)
        return result

    # ============================================================================
    # FINAL RESEARCH COMPILATION TOOLS
    # ============================================================================

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def deduplicate_research_content(research_directory: str) -> Dict[str, Any]:
        """
        Deduplicates ALL research sources as a whole (Tavily + Guidelines + Research URLs + Code + YouTube).
        Produces a single clean, concise deduplicated_research.md file.

        Args:
            research_directory: Path to the research directory containing all source subfolders and the output directory

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success" or "error")
                - deduplicated_path: Absolute path to the generated deduplicated_research.md file
                - source_counts: Dictionary mapping each source category to the number of files collected
                - total_parts_collected: Total number of content parts fed into deduplication
                - message: Human-readable summary of the operation
        """

        opik_context.update_thread_id()
        result = await deduplicate_research_content_tool(research_directory)
        return result
    
    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def create_research_file(research_directory: str) -> Dict[str, Any]:
        """
        Generate the final comprehensive research.md file.

        Combines all research data including filtered Tavily results, scraped guideline
        sources, and full research sources into a comprehensive research.md file. The file
        is organized into sections with collapsible blocks for easy navigation.

        Args:
            research_directory: Path to the research directory containing all research data

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - markdown_file: Path to the generated research.md file
                - research_results_count: Number of research result sections
                - scraped_sources_count: Number of scraped sources sections
                - code_sources_count: Number of code source sections
                - youtube_transcripts_count: Number of YouTube transcript sections
                - additional_sources_count: Number of additional source sections
                - message: Human-readable success message with file generation results
        """

        opik_context.update_thread_id()

        result = create_research_file_tool(research_directory)
        return result

    # ============================================================================
    # RL META-REASONER TOOLS
    # ============================================================================

    @mcp.tool()
    @opik.track(type="tool", project_name=settings.opik_project_name)
    async def predict_exploration_preset(research_directory: str) -> Dict[str, Any]:
        """
        Predict the optimal exploration preset using the GRPO-trained RL model.

        Reads exploitation_digest.md from the research directory and runs two-stage
        inference:

        Stage 1 — RL model (Qwen3-4B + LoRA, NF4 quantised):
          Splits the digest into per-section excerpts and runs a word-count-weighted
          probability vote to produce an aggregate preset recommendation.
          A max-preset floor heuristic fires when the aggregate vote is P0–P2 and at
          least one section individually predicts a higher preset, preventing short
          intro sections from masking deep technical sections.

        Stage 2 — client LLM (you):
          Use the returned signals to make the final decision.  The RL model closes
          ~91% of the uniform-random → oracle E[R] gap, but top-1 accuracy on
          unseen articles is low (~5–17%); treat it as calibrated evidence, not ground
          truth.  Override freely when entropy_bits > 1.5 or confidence < 0.40.

        Signal semantics:
          preset (int 0–5):
            0 – no exploration
            1 – 1 round, balanced
            2 – 2 rounds, balanced then depth
            3 – 2 rounds, depth then breadth
            4 – 3 rounds, balanced then depth then breadth
            5 – 3 rounds, depth then breadth then depth

          confidence (float 0–1):
            Probability mass on the chosen preset.
            ≥0.70 → decisive.  0.40–0.70 → check section signals.  <0.40 → uncertain.

          entropy_bits (float):
            H = −∑ p·log₂(p+ε) over the 6-preset distribution.
            <0.5 → very confident.  0.5–1.5 → moderate.  >1.5 → uncertain, override.

          floor_correction_applied (bool):
            True when the floor heuristic raised the aggregate vote.

          section_signals[i].top2:
            [["P3", 0.81], ["P2", 0.11]] — large gap means high section confidence.
            [["P3", 0.35], ["P4", 0.32]] — small gap means ambiguous section.

          guidance (str):
            One-sentence synthesis.  Use this as your reasoning seed.

        Note: the RL model loads on the first call (~3 min on GPU) and is then cached
        for the lifetime of the server process.

        Args:
            research_directory: Path to the research directory containing
                                exploitation_digest.md at its root.

        Returns:
            Dict[str, Any]:
                - status: "success" or "error"
                - rl_recommendation: dict with preset, name, confidence,
                                     entropy_bits, floor_correction_applied
                - section_signals: list of per-section dicts with title, preset,
                                   name, top2
                - guidance: one-sentence synthesis for the client LLM
                - message: human-readable summary
        """
        opik_context.update_thread_id()
        result = await predict_exploration_preset_tool(research_directory)
        return result

    # ============================================================================
    # TRACKING TOOLS
    # ============================================================================