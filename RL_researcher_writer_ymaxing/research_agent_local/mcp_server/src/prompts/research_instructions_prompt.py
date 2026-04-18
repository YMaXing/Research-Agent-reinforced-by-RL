"""Full research instructions prompt implementation."""

import logging

from ..config.settings import settings

logger = logging.getLogger(__name__)


async def full_research_instructions_prompt() -> str:
    """
    Return the complete research agent instructions as a string.

    Returns:
        The complete research instructions as a string
    """
    dedup_enabled = settings.enable_content_dedup

    dedup_step_number = 7   # step number assigned to dedup when enabled
    # Paragraph shown inside the write step describing how DEDUPLICATED_RESEARCH_FILE is used
    dedup_available_block = f"""
    When DEDUPLICATED_RESEARCH_FILE is available (i.e. step {dedup_step_number}.1 was run), the tool produces a RESEARCH_MD_FILE
    that contains:
      (a) A primary body section with the clean deduplicated content.
      (b) A "Golden Source Reference" appendix containing the full XML-tagged section assembly described above.
          This appendix exists so that downstream LLM metric judges evaluating the generated article can
          identify which parts of the research came from golden sources versus Tavily research, supporting
          the GoldenSourcePriority evaluation criterion.
    
    If DEDUPLICATED_RESEARCH_FILE is not available (step {dedup_step_number}.1 was skipped), the tool falls back to writing
    the XML-tagged section assembly directly as the RESEARCH_MD_FILE.
""" if dedup_enabled else """
    Since content deduplication is disabled, DEDUPLICATED_RESEARCH_FILE will not be present.
    The "create_research_file" tool will write the RESEARCH_MD_FILE with
    the full XML-tagged section assembly directly, without a separate deduplicated content section.
"""

    dedup_step_block = """
7. Content-level deduplication:

    7.1 Run the "deduplicate_research_content" tool. The tool reads all research content available in the scraped guideline sources 
    from URLS_FROM_GUIDELINES_FOLDER, URLS_FROM_RESEARCH_FOLDER, URLS_FROM_GUIDELINES_CODE_FOLDER, URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    and URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER.
    The tool takes a large collection of research sources (from golden sources provided by the article guideline file to both exploitation and exploration phases) 
    and produce the cleanest, most authoritative, non-repetitive knowledge base possible following phase-aware protection rules and hierarchical deduplication goals.
    The tool will automatically remove redundant information while preserving important unique insights, and cluster similar concepts together even if they come from different sources.
    You will be able to see the hierarchy of the sources in the content structure, with clear XML-like tags indicating the source of each content block. 
    Overall, the tool prefers golden > exploitation > high-authority exploration > other exploration sources, but it also applies more complex rules to protect unique insights 
    from lower-tier sources and to ensure that the final content is comprehensive and non-repetitive. The deduplicated content is saved to the DEDUPLICATED_RESEARCH_FILE within RESEARCH_OUTPUT_DIRECTORY.

""" if dedup_enabled else ""

    write_step_number = 8 if dedup_enabled else 7

    instructions_content = f"""
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
    ARTICLE_GUIDELINE_FILE and categorises all references by the H2 section they appear in:

    **Golden sources** (from "Golden Sources", "Article Code", "Lesson Code", or any other section):
    • "github_urls" - GitHub links that are golden sources;
    • "youtube_videos_urls" - YouTube video links that are golden sources;
    • "other_urls" - all other HTTP/HTTPS links (including arXiv papers) that are golden sources;
    • "local_files" - relative paths to local files mentioned in the guidelines.

    **Exploitation sources** (from "Other Sources" section only):
    • "exploitation_github_urls" - GitHub links listed under "Other Sources";
    • "exploitation_youtube_videos_urls" - YouTube links listed under "Other Sources";
    • "exploitation_other_urls" - all other HTTP/HTTPS links (including arXiv papers) listed under "Other Sources".

    Only extensions allowed for local files are: ".py", ".ipynb", and ".md".
    The extracted data is saved to the GUIDELINES_FILENAMES_FILE within the RESEARCH_OUTPUT_DIRECTORY directory.

2. Process the extracted resources in parallel:

    You can run the following sub-steps (2.1 to 2.5) in parallel. In a single turn, you can call all the
    necessary tools for these steps.

    2.1 Local files - run the "process_local_files" tool to read every file path listed under "local_files" in the
    GUIDELINES_FILENAMES_FILE and copy its content into the LOCAL_FILES_FROM_RESEARCH_FOLDER subfolder within
    RESEARCH_OUTPUT_DIRECTORY, giving each copy an appropriate filename (path separators are replaced with underscores).

    2.2 Golden other URL links (including arXiv papers) - run the "scrape_and_clean_other_urls" tool to read the
    `other_urls` list (golden sources from "Golden Sources", "Article Code", and "Lesson Code" sections) from
    GUIDELINES_FILENAMES_FILE and scrape/clean them. ArXiv papers are automatically scraped with arxiv2markdown
    for higher-quality extraction. The tool writes the cleaned markdown files inside the
    URLS_FROM_GUIDELINES_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY.

    2.3 Golden GitHub URLs - run the "process_github_urls" tool to process the `github_urls` list (golden sources)
    from the GUIDELINES_FILENAMES_FILE with gitingest and save a Markdown summary for each URL inside the
    URLS_FROM_GUIDELINES_CODE_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY.

    2.4 Golden YouTube URLs - run the "transcribe_youtube_urls" tool to process the `youtube_videos_urls` list
    (golden sources) from the GUIDELINES_FILENAMES_FILE, transcribe each video, and save the transcript as a
    Markdown file inside the URLS_FROM_GUIDELINES_YOUTUBE_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY.
        Note: Please be aware that video transcription can be a time-consuming process. For reference,
        transcribing a 39-minute video can take approximately 4.5 minutes.

    2.5 Exploitation guideline URLs ("Other Sources") - run the "scrape_exploitation_guideline_urls" tool to
    process all URLs listed under the `exploitation_github_urls`, `exploitation_youtube_videos_urls`, and
    `exploitation_other_urls` keys. Each URL type is routed to its dedicated handler:
    - GitHub URLs → gitingest repository summary (same as step 2.3 but non-golden)
    - YouTube URLs → video transcript (same as step 2.4 but non-golden)
    - ArXiv URLs → arxiv2markdown scrape (same high-quality extraction as step 2.2 but non-golden)
    - Other web URLs → firecrawl scrape + LLM clean (same as step 2.2 but non-golden)
    All output files are saved to the URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER subfolder. In the final
    research file these sources are tagged <research_source type="guideline_exploitation">, not <golden_source>.

3. Exploitation Phase, repeat the following research loop for 3 rounds:

    For each of the 3 exploitation rounds:

    3.1. Run the "generate_next_queries" tool to analyze the ARTICLE_GUIDELINE_FILE, the already-scraped guideline
    URLs, and the existing TAVILY_RESULTS_FILE. The tool identifies knowledge gaps, proposes new web-search
    questions, and writes them - together with a short justification for each - to the NEXT_QUERIES_FILE within
    RESEARCH_OUTPUT_DIRECTORY.

    3.2. Run "deduplicate_new_queries_tool" with query_source="exploitation" to remove any semantic duplicates among the queries generated in this round and against the full query history.
    The deduplicated queries are saved back to NEXT_QUERIES_FILE and also appended to FULL_QUERIES_FILE.

    3.3. Run the "run_tavily_research" tool with the new queries in NEXT_QUERIES_FILE. This tool executes the queries with
    Tavily and appends the results to the TAVILY_RESULTS_FILE within RESEARCH_OUTPUT_DIRECTORY.

4. Exploration Phase, repeat the following research loop for an indefinite number of rounds with a configurable maximum number of {settings.maximum_exploration_rounds} rounds:

    For each of the {settings.maximum_exploration_rounds} exploitation rounds:

    4.1. Run "generate_next_complementary_queries_tool" (where you should choose the value for the arguments "focus" and/or "depth_vs_breadth_ratio") 
        to analyzes the article guidelines, already-scraped content, and existing Tavily results. The tool dives deeper into the content already covered 
        in past research, and/or explores other uncovered aspects that are closely related to past research and may expand the research scope, 
        then propose new web-search questions, and writes them - together with a rationale explaining why it's important and what additional value 
        it brings for the article for each - to NEXT_QUERIES_FILE within RESEARCH_OUTPUT_DIRECTORY.
    
    4.2. Run "deduplicate_new_queries_tool" with query_source="complementary" to remove semantic duplicates among the queries generated in this round and against the full query history.
    The deduplicated queries are saved back to NEXT_QUERIES_FILE and also appended to FULL_QUERIES_FILE.

    4.3 Run the "run_tavily_research" tool with the new complementary queries in NEXT_QUERIES_FILE. This tool executes the queries with
    Tavily and appends the results to the TAVILY_RESULTS_FILE within RESEARCH_OUTPUT_DIRECTORY.

5. Filter Tavily results by quality:

    5.1 Run the "select_research_sources_to_keep" tool. The tool reads the ARTICLE_GUIDELINE_FILE and the
    TAVILY_RESULTS_FILE and applies a two-stage evaluation process:
    - **Stage 1 — Exploitation sources**: Each [EXPLOITATION] source is evaluated on domain authority &
      trustworthiness, relevance to the article guidelines, and content quality. Exploitation sources are
      strongly protected and only rejected if clearly low-quality, unreliable, or irrelevant.
    - **Stage 2 — Exploration sources**: Each [EXPLORATION] source is evaluated on the same three dimensions,
      but with a higher bar. The tool scans through the article guidelines section by section and only accepts
      an exploration source if it can identify at least one specific section where the source adds genuine new
      value in depth or breadth:
      - **Depth** (inward — intensify understanding of the core topic): motivation for the topic (why it exists,
        what problem it solves), theoretical foundations or mathematical underpinnings, technical nuances or
        alternative implementation perspectives, latest advancements or recent developments,
        limitations/criticisms/failure modes, implementation challenges or latency/scale trade-offs,
        real-world case studies or concrete metrics, future implications or open research directions.
      - **Breadth** (outward — connect to adjacent areas outside the core topic): adjacent or related concepts
        that expand the scope, cross-domain analogies or lessons from other fields, historical context or
        evolution of the topic, enabling/disrupting technologies that intersect with the core topic, practical
        applications of the core topic in other industries or domains, emerging trends in adjacent fields or
        the broader ecosystem.
      Sources that cannot satisfy this criterion are rejected.
    The tool writes the comma-separated IDs of the accepted sources to the TAVILY_SOURCES_SELECTED_FILE **and**
    saves a filtered markdown file TAVILY_RESULTS_SELECTED_FILE that contains only the full content blocks of
    the accepted sources. Both files are saved within RESEARCH_OUTPUT_DIRECTORY.

6. Identify which of the accepted sources deserve a *full* scrape:

    6.1 Run the "select_research_sources_to_scrape" tool. It analyses the TAVILY_RESULTS_SELECTED_FILE together
    with the ARTICLE_GUIDELINE_FILE and the material already scraped from guideline URLs, then chooses up to {settings.maximum_sources_to_scrape} diverse,
    authoritative sources whose full content will add most value. The chosen URLs are written (one per line) to the
    URLS_TO_SCRAPE_FROM_RESEARCH_FILE within RESEARCH_OUTPUT_DIRECTORY.

    6.2 Run the "scrape_research_urls" tool. The tool reads the URLs from URLS_TO_SCRAPE_FROM_RESEARCH_FILE and
    scrapes/cleans each URL's full content, including special high-quality handling for arXiv papers. The cleaned markdown files are saved to the
    URLS_FROM_RESEARCH_FOLDER subfolder within RESEARCH_OUTPUT_DIRECTORY with appropriate filenames.
{dedup_step_block}
{write_step_number}. Write final research file:

    {write_step_number}.1 Run the "create_research_file" tool. The tool always assembles all source content into XML-tagged sections
    that clearly distinguish golden sources (material referenced in the article guideline) from research sources
    (material discovered through Tavily exploitation and exploration rounds):
    
    • Golden sources are wrapped in <golden_source type="..."> tags, where the type attribute identifies the
      specific guideline-referenced category:
        - type="guideline_urls"   — web pages scraped from golden URLs listed in the article guideline
        - type="guideline_code"   — GitHub repositories referenced in the golden sources of the article guideline
        - type="guideline_youtube" — YouTube videos referenced in the golden sources of the article guideline
        - type="local_files"      — local files referenced in the article guideline
    
    • Exploitation sources from the article guideline ("Other Sources" section) are wrapped in
      <research_source type="guideline_exploitation"> tags. These sources were explicitly listed
      in the guidelines but are treated as exploitation (not golden) because they are supplementary
      references rather than primary authoritative sources.

    • Research sources (Tavily results and URLs scraped from Tavily-discovered links) are wrapped in
      <research_source type="..."> tags. Importantly, even if a Tavily-discovered URL is a GitHub repo
      or YouTube video, it is still a research source (not golden) because it was not referenced in the
      article guideline.
    
{dedup_available_block}
    The final RESEARCH_MD_FILE is saved in the root of the research directory.

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
│   ├── URLS_FROM_GUIDELINES_FOLDER/                    # Step 2.2 — Scraped content from golden other URLs in guidelines
│   │   └── [scraped_web_pages...]
│   ├── URLS_FROM_GUIDELINES_CODE_FOLDER/               # Step 2.3 — GitHub repository summaries (golden sources)
│   │   └── [github_repo_summaries...]
│   ├── URLS_FROM_GUIDELINES_YOUTUBE_FOLDER/            # Step 2.4 — YouTube video transcripts (golden sources)
│   │   └── [youtube_transcripts...]
│   ├── URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER/       # Step 2.5 — Scraped "Other Sources" (exploitation, non-golden)
│   │   └── [exploitation_sources...]
│   ├── FULL_QUERIES_FILE                               # Steps 3.2 / 4.2 — Cumulative history of all deduplicated queries
│   ├── NEXT_QUERIES_FILE                               # Steps 3.1 / 4.1 — Proposed queries for the current round
│   ├── TAVILY_RESULTS_FILE                             # Steps 3.3 / 4.3 — Complete results from all Tavily rounds
│   ├── TAVILY_SOURCES_SELECTED_FILE                    # Step 5.1 — Accepted source IDs after quality filtering
│   ├── TAVILY_RESULTS_SELECTED_FILE                    # Step 5.1 — Filtered Tavily results (accepted sources only)
│   ├── URLS_TO_SCRAPE_FROM_RESEARCH_FILE               # Step 6.1 — URLs chosen for full content scraping
│   ├── URL_PHASES_FILE                                 # Step 6.1 — URL → phase mapping (exploitation / exploration)
│   ├── URLS_FROM_RESEARCH_FOLDER/                      # Step 6.2 — Fully scraped content from selected research URLs
│   │   └── [full_research_sources...]
    │   └── DEDUPLICATED_RESEARCH_FILE                      # Step 7.1 — Phase-aware deduplicated knowledge base (omitted when dedup disabled)
└── RESEARCH_MD_FILE                                    # Step {write_step_number}.1 — Final comprehensive research compilation
```

This organized structure ensures all research artifacts are systematically collected, processed, and made easily
accessible for article writing and future reference.
    """.strip()

    return instructions_content
