"""MCP startup utilities."""

from typing import List

from mcp_agent.agents.agent import Agent


async def get_capabilities_from_mcp_client(client: Agent) -> tuple[List, List, List]:
    """Get available capabilities. Must be called inside an active agent context."""
    tools = await client.list_tools()
    resources = await client.list_resources()
    prompts = await client.list_prompts()
    return tools.tools, resources.resources, prompts.prompts


def print_startup_info(tools: List, resources: List, prompts: List):
    """Print startup information about available capabilities."""
    print(f"🛠️  Available tools: {len(tools)}")
    print(f"📚 Available resources: {len(resources)}")
    print(f"💬 Available prompts: {len(prompts)}")
    print()
    print(
        "Available Commands: /tools, /resources, /prompts, /prompt/<name>, "
        "/resource/<uri>, /model-thinking-switch, /quit"
    )
    print()
