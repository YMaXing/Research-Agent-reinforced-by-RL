"""Shim — delegates to training/rl_data_generator.py.

Allows invoking the data generator from the research_agent_local/ root:

    uv run --project mcp_server python rl_data_generator.py [args...]

without having to remember the training/ subdirectory.
"""
import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "training"))
runpy.run_path(
    str(Path(__file__).parent / "training" / "rl_data_generator.py"),
    run_name="__main__",
)
