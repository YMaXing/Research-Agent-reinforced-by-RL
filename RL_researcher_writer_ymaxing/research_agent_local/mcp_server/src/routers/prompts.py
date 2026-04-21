"""MCP Prompts registration for adaptive conversation starters."""

import opik
from fastmcp import FastMCP

# Import prompts with a different name to avoid naming collision
from ..prompts.research_instructions_prompt import full_research_instructions_prompt as _get_research_instructions
from ..utils.opik_utils import opik_context
from ..config.settings import settings


def register_mcp_prompts(mcp: FastMCP) -> None:
    """Register all MCP prompts with the server instance."""

    @mcp.prompt()
    @opik.track(type="general", project_name=settings.opik_project_name)
    async def full_research_instructions_prompt() -> str:
        """Complete research agent workflow instructions."""

        opik_context.initialize_thread_id()

        return await _get_research_instructions()
