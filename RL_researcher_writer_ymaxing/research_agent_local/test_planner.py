"""Shim — delegates to evaluation/test_grok_planner.py.

Allows invoking the eval harness from the research_agent_local/ root:

    uv run --project mcp_server python test_grok_planner.py [args...]

without having to remember the evaluation/ subdirectory.
"""
import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "evaluation"))
runpy.run_path(
    str(Path(__file__).parent / "evaluation" / "test_planner.py"),
    run_name="__main__",
)
