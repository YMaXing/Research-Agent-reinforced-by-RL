"""Research tools package - Business logic for MCP server."""

# URL and file extraction tools
# Final research compilation tools
from .create_research_file_tool import create_research_file_tool
from .extract_guidelines_urls_tool import extract_guidelines_urls_tool
from .predict_exploration_preset_tool import predict_exploration_preset_tool

# Research query and analysis tools
from .generate_next_queries_tool import generate_next_queries_tool, generate_next_complementary_queries_tool
from .process_github_urls_tool import process_github_urls_tool
from .process_local_files_tool import process_local_files_tool
from .run_tavily_research_tool import run_tavily_research_tool
from .dedup_new_queries_tool import deduplicate_new_queries_tool
from .dedup_research_content_tool import deduplicate_research_content_tool

# Web scraping and content processing tools
from .scrape_and_clean_other_urls_tool import scrape_and_clean_other_urls_tool
from .scrape_exploitation_guideline_urls_tool import scrape_exploitation_guideline_urls_tool
from .scrape_research_urls_tool import scrape_research_urls_tool

# Source selection and curation tools
from .select_research_sources_to_keep_tool import select_research_sources_to_keep_tool
from .select_research_sources_to_scrape_tool import select_research_sources_to_scrape_tool
from .transcribe_youtube_videos_tool import transcribe_youtube_videos_tool

# Export all functions for easy importing
__all__ = [
    # URL and file extraction
    "extract_guidelines_urls_tool",
    "process_local_files_tool",
    # Web scraping and content processing
    "scrape_and_clean_other_urls_tool",
    "scrape_exploitation_guideline_urls_tool",
    "scrape_research_urls_tool",
    "process_github_urls_tool",
    "transcribe_youtube_videos_tool",
    # Research query and analysis
    "generate_next_queries_tool",
    "generate_next_complementary_queries_tool",
    "run_tavily_research_tool",
    "deduplicate_new_queries_tool",
    # Source selection and curation
    "select_research_sources_to_keep_tool",
    "select_research_sources_to_scrape_tool",
    "deduplicate_research_content_tool",
    # Final research compilation
    "create_research_file_tool",
    # RL meta-reasoner
    "predict_exploration_preset_tool",
]
