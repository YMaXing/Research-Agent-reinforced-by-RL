"""Agent loop handling utilities."""

import json
from typing import Any, Dict, List, Tuple

from fastmcp import Client

from ..settings import settings
from . import gemini_llm_utils as gemini
from . import grok_llm_utils as grok
from .print_utils import Color, Style, print_colored


# ---------------------------------------------------------------------------
# Provider dispatch
# ---------------------------------------------------------------------------

# Keyed by the provider prefix used in orchestrator_configs' "identifier" field
# (e.g. "xai:grok-4.6"), not by the orchestrator_configs key itself.
_PROVIDERS = {
    "google_genai": gemini,
    "xai": grok,
}


def _resolve_orchestrator(orchestrator_key: str) -> Tuple[Any, str, Dict[str, Any]]:
    """Resolve an orchestrator_configs key to (provider module, raw model id, params)."""
    config = settings.orchestrator_configs.get(orchestrator_key)
    if config is None:
        raise ValueError(
            f"Unknown orchestrator key '{orchestrator_key}'. Must be one of: "
            f"{', '.join(settings.orchestrator_configs)}"
        )
    identifier = config["identifier"]
    prefix, _, raw_model_id = identifier.partition(":")
    provider = _PROVIDERS.get(prefix)
    if provider is None:
        raise ValueError(f"Unsupported provider prefix '{prefix}' in identifier '{identifier}'.")
    return provider, raw_model_id, config.get("params", {})


# ---------------------------------------------------------------------------
# Message-format helpers (Gemini uses types.Content, Grok uses OpenAI dicts)
# ---------------------------------------------------------------------------


def make_user_message(text: str) -> Any:
    """Create a user message in the format expected by the active provider."""
    if settings.model_id.startswith("gemini"):
        from google.genai import types

        return types.Content(role="user", parts=[types.Part(text=text)])
    return {"role": "user", "content": text}


def _append_assistant_response(history: List, response: Any, model_id: str) -> None:
    """Append the model's own response object to conversation history."""
    if model_id.startswith("gemini"):
        history.append(response.candidates[0].content)
    else:
        history.append(response.choices[0].message.model_dump())


async def execute_tool(name: str, args: dict, client: Client):
    """Execute a tool and return the result."""
    print()
    print_colored(f"⚡ Executing tool '{name}' via MCP server...", Color.CYAN)
    try:
        tool_result = await client.call_tool(name, args)
        if getattr(tool_result, "isError", False):
            error_msg = f"Tool '{name}' returned an error: {tool_result}"
            print_colored(f"❌ {error_msg}", Color.BRIGHT_RED)
            raise Exception(error_msg)
        print_colored("✅ Tool execution successful!", Color.CYAN)
        return tool_result
    except Exception as e:
        error_msg = f"Tool '{name}' execution failed: {e}"
        print_colored(f"❌ {error_msg}", Color.BRIGHT_RED)
        raise Exception(error_msg)


async def handle_agent_loop(
    conversation_history: List,
    tools: List,
    client: Client,
    thinking_enabled: bool,
):
    """Handle the agent loop for tool execution."""
    provider, model_id, params = _resolve_orchestrator(settings.model_id)

    # Initialize LLM client using the resolved provider
    llm_config = provider.build_llm_config_with_tools(tools, thinking_enabled, params)
    llm_client = provider.LLMClient(model_id, llm_config, params)

    while True:
        print()
        # Call LLM with current conversation history
        response = await llm_client.generate_content(conversation_history)

        # Extract and display thoughts as separate message (only if enabled)
        if thinking_enabled:
            thoughts = provider.extract_thought_summary(response)
            if thoughts:
                print_colored("🤔 LLM's Thoughts:", Color.BRIGHT_MAGENTA, Style.BOLD)
                print_colored(thoughts, Color.MAGENTA)
                print()

        # Check for function calls
        function_call_info = provider.extract_first_function_call(response)
        if function_call_info:
            name, args = function_call_info

            # Check if this is a tool call
            is_tool = any(tool.name == name for tool in tools)

            if is_tool:
                print()
                print_colored("🔧 Function Call (Tool):", Color.CYAN, Style.BOLD)
                print_colored("  Tool: ", Color.CYAN, end="")
                print_colored(name, Color.CYAN, Style.BOLD)
                print_colored("  Arguments: ", Color.CYAN, end="")
                print_colored(json.dumps(args, indent=2), Color.CYAN)

                # Execute the tool via MCP server
                try:
                    tool_result = await execute_tool(name, args, client)
                    # Add tool result to conversation history
                    tool_response = f"Tool '{name}' executed successfully. Result: {tool_result}"
                    conversation_history.append(make_user_message(tool_response))
                except Exception as e:
                    # Error already printed by execute_tool; surface it clearly to the LLM
                    error_response = f"Tool '{name}' returned an error: {e}"
                    conversation_history.append(make_user_message(error_response))

            else:
                error_msg = f"Unknown function call: '{name}'. Not found in tools."
                print_colored(f"❌ {error_msg}", Color.BRIGHT_RED)
                conversation_history.append(make_user_message(error_msg))

        else:
            # Extract final text response - this ends the ReAct loop
            final_text = provider.extract_final_answer(response)
            if final_text:
                print_colored("💬 LLM Response: ", Color.WHITE, end="")
                print(final_text)

                # Add LLM's final response to conversation history
                _append_assistant_response(conversation_history, response, model_id)
            else:
                print_colored("💬 No response generated", Color.BRIGHT_RED)

            print()
            break  # Exit the agent loop
