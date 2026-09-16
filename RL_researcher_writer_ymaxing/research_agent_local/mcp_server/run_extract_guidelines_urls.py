"""Standalone runner for workflow step 1.3 (extract_guidelines_urls_tool).

Usage:
    python run_extract_guidelines_urls.py [research_directory]

Defaults to the 26_end_to_end_demo base if no directory is given.
"""

import json
import sys

from src.tools.extract_guidelines_urls_tool import extract_guidelines_urls_tool

DEFAULT_RESEARCH_DIR = (
    "/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/"
    "rl_training_data/bases/26_end_to_end_demo"
)


def main() -> None:
    research_dir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_RESEARCH_DIR
    result = extract_guidelines_urls_tool(research_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
