"""
New MCP Client based on mcp-agent - Interactive MCP client with configurable transport options.

Usage:
    # In-memory transport (default - MCP server runs in same process)
    uv run python -m src.client

    # Stdio transport (MCP server runs as external process)
    uv run python -m src.client --transport stdio

Transport Options:
    - in-memory: MCP server runs in the same process (faster, easier debugging)
    - stdio: MCP server runs as external process with explicit configuration:
        * Transport: stdio
        * Command: uv --directory <server_path> run mcp-server --transport stdio
        * Better isolation and process separation
"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.config import get_settings as get_mcp_settings

from .settings import settings
from .utils.handle_message_utils import handle_user_message
from .utils.logging_utils import configure_logging
from .utils.mcp_startup_utils import get_capabilities_from_mcp_client, print_startup_info
from .utils.opik_handler import configure_opik  
from .utils.parse_message_utils import parse_user_input

# Configure logging
configure_logging()

# Load mcp-agent config from YAML, then inject the computed server path
_mcp_settings = get_mcp_settings()
_mcp_settings.mcp.servers["research-agent"].args = [
    "--directory",
    str(settings.server_main_path),
    "run",
    "-m",
    "src.server",
    "--transport",
    "stdio",
]

# Create the main application object
app = MCPApp(name="ResearchClient", settings=_mcp_settings)

async def main():
    """Main function to demonstrate FastMCP client with configurable transport."""
    parser = argparse.ArgumentParser(description="Nova MCP Client")
    parser.add_argument(
        "--transport",
        "-t",
        type=str,
        choices=["in-memory", "stdio"],
        default="in-memory",
        help="Transport method: 'in-memory' (default) or 'stdio' for external MCP server",
    )
    args = parser.parse_args()

    async with app.run():
        try:
            # Initialize Opik if configured
            if configure_opik():
                logging.info("📊 Opik monitoring enabled")
            else:
                logging.info("📊 Opik monitoring disabled (missing configuration)")

            # Initialize MCP client based on transport mode
            if args.transport == "in-memory":
                # Add the project root to Python path to enable importing mcp_server
                project_root = Path(__file__).parent.parent.parent
                sys.path.insert(0, str(project_root))
                from mcp_server.src.server import create_mcp_server

                logging.info("🚀 Starting MCP client with in-memory transport...")
                mcp_server = create_mcp_server()
                await app.context.mcp_registry.register_server(
                    name="research-agent",
                    server=mcp_server,                  # ← pass the FastMCP instance directly
                    # transport="memory" is implicit when passing server object
                )

            elif args.transport == "stdio":
                logging.info("🚀 Starting MCP client with stdio transport...")
                
            agent = Agent(
                name="research_agent",
                instruction="You are a research agent. Use the provided tools, resources, and prompts to solve complex queries.",
                server_names=["research_agent"],   # Must match the key in config.yaml
            )
           
            # Print startup information about MCP server
            tools, resources, prompts = await get_capabilities_from_mcp_client(agent)
            print_startup_info(tools, resources, prompts)

            # Initialize conversation history
            conversation_history = []

            # Initialize thinking state (enabled by default)
            thinking_enabled = True

            # Main conversation loop
            async with agent:
                while True:
                    try:
                        # Get user input
                        user_input = input("👤 You: ").strip()
                        if not user_input:
                            continue

                        # Parse the user input to determine what type it is
                        parsed_input = parse_user_input(user_input)

                        # Handle the user message and determine if we should continue
                        should_continue, thinking_enabled = await handle_user_message(
                            parsed_input=parsed_input,
                            tools=tools,
                            resources=resources,
                            prompts=prompts,
                            conversation_history=conversation_history,
                            mcp_client=agent,
                            thinking_enabled=thinking_enabled,
                        )

                        if not should_continue:
                            break

                    except KeyboardInterrupt:
                        print()
                        logging.info("👋 Interrupted by user. Goodbye!")
                        break
                    except Exception as e:
                        print()
                        logging.error(f"Error: {e}")
                        logging.info("Continuing conversation...\n")

        except Exception as e:
            logging.error(f"Failed to initialize MCP client: {e}")
            return


if __name__ == "__main__":
    asyncio.run(main())
