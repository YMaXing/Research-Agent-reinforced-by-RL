"""
Composed MCP Server - Combines research and writing servers into a single endpoint.

This server uses FastMCP's composition features to mount both the research agent
and writing workflow servers, exposing all their capabilities through a single
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
        config_path: Optional path to config file. If None, uses the default
            mcp_servers_config_http.json shipped alongside this package.
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent.parent / "mcp_servers_config_http.json"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)


def create_composed_server(config_path: Path | None = None) -> FastMCP:
    """
    Create a composed MCP server by mounting research and writing servers.

    Args:
        config_path: Optional path to config file. If None, uses default mcp_servers_to_compose.json

    Returns:
        FastMCP: The composed server instance with both servers mounted
    """
    # Create the main composed server
    mcp = FastMCP(
        name="Research+Writing Composed Server",
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

        This prompt combines the research agent workflow with the writing workflow,
        providing end-to-end instructions for conducting comprehensive research
        and generating an article from that research.

        Args:
            dir_path: Path to the directory that will contain research resources
                     and the final article.

        Returns:
            A formatted prompt string with complete workflow instructions.
        """
        return f"""
# Complete Research and Article Generation Workflow

This workflow combines two phases: research and article generation, both operating on
the directory `{dir_path}`.

---

## PHASE 1: Research

Fetch the "full_research_instructions_prompt" MCP prompt (mounted from the research agent
server) and follow its instructions exactly, using `{dir_path}` as the research directory
for every tool call. That prompt is the single source of truth for the research workflow
and is kept up to date independently of this combined prompt, so do not substitute,
summarize, or duplicate its steps here.

---

## PHASE 2: Article Generation

Once Phase 1 is complete, `{dir_path}` will contain `article_guideline.md` and `research.md`,
which provide all the context needed for article generation.

Don't check whether any expected files are missing, just call the "generate_article" tool of
the writing MCP server with `{dir_path}` - it takes care of everything.

Once the article has been generated, let the user know that the "edit_article" and
"edit_selected_text" tools of the writing MCP server (along with their matching prompts) are
available afterward if they want to revise the article.
""".strip()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Composed MCP Server (Research + Writing)")
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
        help="Path to MCP servers configuration file (overrides default mcp_servers_config_http.json)",
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
