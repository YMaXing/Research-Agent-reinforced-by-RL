"""
Composed MCP Server - Combines Nova and Brown servers into a single endpoint.

This server uses FastMCP's composition features to mount both the Nova research agent
and Brown writing workflow servers, exposing all their capabilities through a single
MCP server without prefixes.

Usage:
    python -m src.main
"""

import json
import logging
from pathlib import Path

from fastmcp import Client, FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_server_config(config_path: Path | None = None) -> dict:
    """Load the MCP servers configuration from JSON file.

    Args:
        config_path: Optional path to config file. If None, uses default mcp_servers_to_compose.json
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent / "mcp_servers_to_compose.json"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)


def create_composed_server(config_path: Path | None = None) -> FastMCP:
    """
    Create a composed MCP server by mounting Nova and Brown servers.

    Args:
        config_path: Optional path to config file. If None, uses default mcp_servers_to_compose.json

    Returns:
        FastMCP: The composed server instance with both servers mounted
    """
    # Create the main composed server
    mcp = FastMCP(
        name="Nova+Brown Composed Server",
        version="0.1.0",
    )

    logger.info("Loading server configuration...")
    config = load_server_config(config_path)

    servers_config = config.get("mcpServers", {})

    if not servers_config:
        raise ValueError("No servers found in configuration")

    logger.info(f"Found {len(servers_config)} servers to compose: {list(servers_config.keys())}")

    # Create proxies and mount each server
    for server_name, server_config in servers_config.items():
        logger.info(f"Creating proxy for {server_name}...")

        # Wrap the server config in the mcpServers structure expected by Client
        client_config = {"mcpServers": {server_name: server_config}}

        # Create a client for this server
        client = Client(client_config)

        # Create a proxy from the client
        proxy = FastMCP.as_proxy(client)

        logger.info(f"Mounting {server_name} without prefix...")
        mcp.mount(proxy)

    # Register the combined workflow prompt
    register_combined_prompt(mcp)

    logger.info("Composed server created successfully!")
    return mcp


def register_combined_prompt(mcp: FastMCP) -> None:
    """Register the combined research and writing workflow prompt."""

    @mcp.prompt()
    def full_research_and_writing_workflow(dir_path: Path) -> str:
        """Complete workflow for research and article generation.

        This prompt combines the Nova research agent workflow with the Brown
        article generation workflow, providing end-to-end instructions for
        conducting comprehensive research and generating an article from that research.

        Args:
            dir_path: Path to the directory that will contain research resources
                     and the final article.

        Returns:
            A formatted prompt string with complete workflow instructions.
        """
        return f"""
# Complete Research and Article Generation Workflow

This workflow combines two phases: research (Nova) and article generation (Brown).

---

## PHASE 1: Research (Nova)

Your job is to execute the workflow below.

All the tools require a research directory as input.
If the user doesn't provide a research directory, you should ask for it before executing any tool.

**Workflow:**

1. Setup:

    1.1. Explain to the user the numbered steps of the workflow. Be concise. Keep them numbered so that the user
    can easily refer to them later.

    1.2. Ask the user for the research directory, if not provided. Ask the user if any modification is needed for the
    workflow (e.g. running from a specific step, adding user feedback to specific steps, or changing parameters such as the number of exploration rounds).

    1.3 Extract the URLs from the ARTICLE_GUIDELINE_FILE with the "extract_guidelines_urls" tool. This tool reads the
    ARTICLE_GUIDELINE_FILE and extracts three groups of references from the guidelines:
    • "github_urls" - all GitHub links;
    • "youtube_videos_urls" - all YouTube video links;
    • "other_urls" - all remaining HTTP/HTTPS links, including arxiv papers;
    • "local_files" - relative paths to local files mentioned in the guidelines (e.g. "code.py", "src/main.py").
    Only extensions allowed are: ".py", ".ipynb", and ".md".
    The extracted data is saved to the GUIDELINES_FILENAMES_FILE within the RESEARCH_OUTPUT_DIRECTORY directory.

2. Process the extracted resources in parallel:

    You can run the following sub-steps (2.1 to 2.4) in parallel. In a single turn, you can call all the
    necessary tools for these steps.

    2.1 Local files - run the "process_local_files" tool to read every file path listed under "local_files" in the
    GUIDELINES_FILENAMES_FILE and copy its content into the LOCAL_FILES_FROM_RESEARCH_FOLDER subfolder within
    RESEARCH_OUTPUT_DIRECTORY, giving each copy an appropriate filename (path separators are replaced with underscores).

    2.2 Other URL links (including arXiv papers) - run the "scrape_and_clean_other_urls" tool to read the `other_urls` list from the
    GUIDELINES_FILENAMES_FILE and scrape/clean them. The tool writes the cleaned markdown files inside the
    URLS_FROM_GUIDELINES_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY.

    2.3 GitHub URLs - run the "process_github_urls" tool to process the `github_urls` list from the
    GUIDELINES_FILENAMES_FILE with gitingest and save a Markdown summary for each URL inside the
    URLS_FROM_GUIDELINES_CODE_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY.

    2.4 YouTube URLs - run the "transcribe_youtube_urls" tool to process the `youtube_videos_urls` list from the
    GUIDELINES_FILENAMES_FILE, transcribe each video, and save the transcript as a Markdown file inside the
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY.
        Note: Please be aware that video transcription can be a time-consuming process. For reference,
        transcribing a 39-minute video can take approximately 4.5 minutes.

3. Exploitation Phase, repeat the following research loop for 3 rounds:

    For each of the 3 exploitation rounds:

    3.1. Run the "generate_next_queries" tool to analyze the ARTICLE_GUIDELINE_FILE, the already-scraped guideline
    URLs, and the existing TAVILY_RESULTS_FILE. The tool identifies knowledge gaps, proposes new web-search
    questions, and writes them - together with a short justification for each - to the NEXT_QUERIES_FILE within
    RESEARCH_OUTPUT_DIRECTORY.

    3.2. Run "deduplicate_new_queries" with query_source="exploitation" to remove any semantic duplicates among the queries generated in this round and against the full query history.
    The deduplicated queries are saved back to NEXT_QUERIES_FILE and also appended to FULL_QUERIES_FILE.

    3.3. Run the "run_tavily_research" tool with the new queries in NEXT_QUERIES_FILE. This tool executes the queries with
    Tavily and appends the results to the TAVILY_RESULTS_FILE within RESEARCH_OUTPUT_DIRECTORY.

4. Exploration Phase, repeat the following research loop for a configurable maximum number of 3 rounds:

    For each of the 3 exploration rounds:

    4.1. Run "generate_next_complementary_queries" (where you should choose the value for the arguments "focus" and/or "depth_vs_breadth_ratio")
        to analyze the article guidelines, already-scraped content, and existing Tavily results. The tool dives deeper into the content already covered
        in past research, and/or explores other uncovered aspects that are closely related to past research and may expand the research scope,
        then proposes new web-search questions, and writes them - together with a rationale explaining why it's important and what additional value
        it brings for the article for each - to NEXT_QUERIES_FILE within RESEARCH_OUTPUT_DIRECTORY.

    4.2. Run "deduplicate_new_queries" with query_source="complementary" to remove semantic duplicates among the queries generated in this round and against the full query history.
    The deduplicated queries are saved back to NEXT_QUERIES_FILE and also appended to FULL_QUERIES_FILE.

    4.3 Run the "run_tavily_research" tool with the new complementary queries in NEXT_QUERIES_FILE. This tool executes the queries with
    Tavily and appends the results to the TAVILY_RESULTS_FILE within RESEARCH_OUTPUT_DIRECTORY.

5. Filter Tavily results by quality:

    5.1 Run the "select_research_sources_to_keep" tool. The tool reads the ARTICLE_GUIDELINE_FILE and the
    TAVILY_RESULTS_FILE (including queries in both exploitation and exploration phases), automatically evaluates
    each source for trustworthiness, authority and relevance, writes the comma-separated IDs of the accepted sources
    to the TAVILY_SOURCES_SELECTED_FILE **and** saves a filtered markdown file TAVILY_RESULTS_SELECTED_FILE that contains
    only the full content blocks of the accepted sources. Both files are saved within RESEARCH_OUTPUT_DIRECTORY.

6. Identify which of the accepted sources deserve a *full* scrape:

    6.1 Run the "select_research_sources_to_scrape" tool. It analyses the TAVILY_RESULTS_SELECTED_FILE together
    with the ARTICLE_GUIDELINE_FILE and the material already scraped from guideline URLs, then chooses up to 5 diverse,
    authoritative sources whose full content will add most value. The chosen URLs are written (one per line) to the
    URLS_TO_SCRAPE_FROM_RESEARCH_FILE within RESEARCH_OUTPUT_DIRECTORY.

    6.2 Run the "scrape_research_urls" tool. The tool reads the URLs from URLS_TO_SCRAPE_FROM_RESEARCH_FILE and
    scrapes/cleans each URL's full content, including special high-quality handling for arXiv papers. The cleaned markdown files are saved to the
    URLS_FROM_RESEARCH_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY with appropriate filenames.

7. Content-level deduplication:

    7.1 Run the "deduplicate_research_content" tool. The tool reads all research content available in the scraped guideline sources
    from URLS_FROM_GUIDELINES_FOLDER, URLS_FROM_RESEARCH_FOLDER, URLS_FROM_GUIDELINES_CODE_FOLDER, and URLS_FROM_GUIDELINES_YOUTUBE_FOLDER.
    The tool takes a large collection of research sources (from golden sources provided by the article guideline file to both exploitation and exploration phases)
    and produces the cleanest, most authoritative, non-repetitive knowledge base possible following phase-aware protection rules and hierarchical deduplication goals.
    The tool will automatically remove redundant information while preserving important unique insights, and cluster similar concepts together even if they come from different sources.
    Overall, the tool prefers golden > exploitation > high-authority exploration > other exploration sources, but it also applies more complex rules to protect unique insights
    from lower-tier sources and to ensure that the final content is comprehensive and non-repetitive. The deduplicated content is saved to the DEDUPLICATED_RESEARCH_FILE within RESEARCH_OUTPUT_DIRECTORY.

8. Write final research file:

    8.1 Run the "create_research_file" tool. The tool assembles all source content into XML-tagged sections
    that clearly distinguish golden sources (material referenced in the article guideline) from research sources
    (material discovered through Tavily exploitation and exploration rounds):

    • Golden sources are wrapped in <golden_source type="..."> tags, where the type attribute identifies the
      specific guideline-referenced category:
        - type="guideline_urls"    — web pages scraped from URLs listed in the article guideline
        - type="guideline_code"    — GitHub repositories referenced in the article guideline
        - type="guideline_youtube" — YouTube videos referenced in the article guideline
        - type="local_files"       — local files referenced in the article guideline

    • Research sources (Tavily results and URLs scraped from Tavily-discovered links) are wrapped in
      <research_source type="..."> tags. Importantly, even if a Tavily-discovered URL is a GitHub repo
      or YouTube video, it is still a research source (not golden) because it was not referenced in the
      article guideline.

    When DEDUPLICATED_RESEARCH_FILE is available (i.e. step 7.1 was run), the tool produces a RESEARCH_MD_FILE
    that contains:
      (a) A primary body section with the clean deduplicated content.
      (b) A "Golden Source Reference" appendix containing the full XML-tagged section assembly described above.

    If DEDUPLICATED_RESEARCH_FILE is not available (step 7.1 was skipped), the tool falls back to writing
    the XML-tagged section assembly directly as the RESEARCH_MD_FILE.

    In both cases, the final RESEARCH_MD_FILE is saved in the root of the research directory.

Depending on the results of previous steps, you may want to skip running a tool if not necessary.

**Critical Failure Policy:**

If a tool reports a complete failure, you are required to halt the entire workflow immediately. A complete failure
is defined as processing zero items successfully (e.g., scraped 0/7 URLs, processed 0 files).

If this occurs, your immediate and only action is to:
    1. State the exact tool that failed and quote the output message.
    2. Announce that you are stopping the workflow as per your instructions.
    3. Ask the user for guidance on how to proceed.

**File and Folder Structure:**

After running the complete workflow, the research directory will contain the following structure:

```
research_directory/
├── ARTICLE_GUIDELINE_FILE                              # Input: Article guidelines and requirements
├── RESEARCH_OUTPUT_FOLDER/                             # Hidden directory containing all research data
│   ├── GUIDELINES_FILENAMES_FILE                       # Step 1.3 — Extracted URLs and local files from guidelines
│   ├── LOCAL_FILES_FROM_RESEARCH_FOLDER/               # Step 2.1 — Copied local files referenced in guidelines
│   │   └── [processed_local_files...]
│   ├── URLS_FROM_GUIDELINES_FOLDER/                    # Step 2.2 — Scraped content from other URLs in guidelines
│   │   └── [scraped_web_pages...]
│   ├── URLS_FROM_GUIDELINES_CODE_FOLDER/               # Step 2.3 — GitHub repository summaries and code analysis
│   │   └── [github_repo_summaries...]
│   ├── URLS_FROM_GUIDELINES_YOUTUBE_FOLDER/            # Step 2.4 — YouTube video transcripts
│   │   └── [youtube_transcripts...]
│   ├── FULL_QUERIES_FILE                               # Steps 3.2 / 4.2 — Cumulative history of all deduplicated queries
│   ├── NEXT_QUERIES_FILE                               # Steps 3.1 / 4.1 — Proposed queries for the current round
│   ├── TAVILY_RESULTS_FILE                             # Steps 3.3 / 4.3 — Complete results from all Tavily rounds
│   ├── TAVILY_SOURCES_SELECTED_FILE                    # Step 5.1 — Accepted source IDs after quality filtering
│   ├── TAVILY_RESULTS_SELECTED_FILE                    # Step 5.1 — Filtered Tavily results (accepted sources only)
│   ├── URLS_TO_SCRAPE_FROM_RESEARCH_FILE               # Step 6.1 — URLs chosen for full content scraping
│   ├── URL_PHASES_FILE                                 # Step 6.1 — URL → phase mapping (exploitation / exploration)
│   ├── URLS_FROM_RESEARCH_FOLDER/                      # Step 6.2 — Fully scraped content from selected research URLs
│   │   └── [full_research_sources...]
│   └── DEDUPLICATED_RESEARCH_FILE                      # Step 7.1 — Phase-aware deduplicated knowledge base
└── RESEARCH_MD_FILE                                    # Step 8.1 — Final comprehensive research compilation
```

This organized structure ensures all research artifacts are systematically collected, processed, and made easily
accessible for article writing and future reference.

---

## PHASE 2: Article Generation (Brown)

Once the research phase is complete, the research directory (specified as `{dir_path}`) will contain:
- `article_guideline.md` - The original article guidelines and requirements
- `research.md` - The comprehensive research compilation from Phase 1

These files provide all the necessary context and information for article generation.

**Next Step:**

Using Brown hosted as an MCP server, generate an article using all the necessary resources from 
the following directory: `{dir_path}`. Don't check if any expected files are missing, just trigger 
the "generate_article" tool of the Brown MCP Server, which will take care of everything.
""".strip()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Composed MCP Server (Nova + Brown)")
    parser.add_argument(
        "--transport",
        "-t",
        type=str,
        choices=["stdio", "streamable-http"],
        default="stdio",
        help="Transport protocol to use (stdio or streamable-http)",
    )
    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=8003,
        help="Port number for HTTP transport (default: 8003)",
    )
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        default=None,
        help="Path to MCP servers configuration file (overrides default mcp_servers_to_compose.json)",
    )
    args = parser.parse_args()

    logger.info("Starting composed MCP server...")

    try:
        composed_server = create_composed_server(config_path=args.config)
        logger.info("Running composed server...")

        # Run the server with the specified transport
        if args.transport == "streamable-http":
            composed_server.run(transport=args.transport, port=args.port)
        else:
            composed_server.run(transport=args.transport)
    except Exception as e:
        logger.error(f"Failed to start composed server: {e}")
        raise
