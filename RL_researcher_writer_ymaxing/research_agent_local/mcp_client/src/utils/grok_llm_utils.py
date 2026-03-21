"""LLM and Grok (xAI) utilities for configuration and response processing."""

from typing import Any, Dict, List, Optional

import openai

from ..settings import settings
from .opik_handler import track_openai_client


def build_llm_config_with_tools(mcp_tools: List, thinking_enabled: bool = True) -> Dict[str, Any]:
    """Build Grok config with all MCP tools converted to OpenAI-compatible format.

    Args:
        mcp_tools: List of MCP tool objects with name, description, and inputSchema.
        thinking_enabled: Whether to enable extended reasoning (Grok-3+ only).

    Returns:
        A dict of kwargs to spread into chat.completions.create().
    """
    grok_tools = [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema,
            },
        }
        for tool in mcp_tools
    ]

    config: Dict[str, Any] = {
        "tools": grok_tools,
        "tool_choice": "auto",
    }

    # reasoning_effort is supported on Grok-3 models when thinking is enabled
    if thinking_enabled:
        config["reasoning_effort"] = "high"

    return config


def extract_thought_summary(response: openai.types.chat.ChatCompletion) -> Optional[str]:
    """Collect reasoning content if present (Grok extended thinking)."""
    chunks = [
        choice.message.reasoning_content
        for choice in response.choices
        if getattr(choice.message, "reasoning_content", None)
    ]
    return "\n".join(chunks).strip() if chunks else None


def extract_final_answer(response: openai.types.chat.ChatCompletion) -> Optional[str]:
    """Extract the final text answer from the response."""
    chunks = [
        choice.message.content
        for choice in response.choices
        if choice.message.content and choice.finish_reason != "tool_calls"
    ]
    return "\n".join(chunks).strip() if chunks else None


def extract_first_function_call(response: openai.types.chat.ChatCompletion):
    """Return (name, args) for the first tool call, or None if the model produced a final answer."""
    import json

    for choice in response.choices:
        tool_calls = getattr(choice.message, "tool_calls", None) or []
        if tool_calls:
            tc = tool_calls[0]
            return tc.function.name, json.loads(tc.function.arguments or "{}")
    return None


class LLMClient:
    """Grok (xAI) LLM client using the OpenAI-compatible API."""

    def __init__(self, model_id: str, llm_config: Dict[str, Any]):
        """Initialize the Grok client.

        Args:
            model_id: The Grok model identifier (e.g., 'grok-3-beta').
            llm_config: Tool/config kwargs from build_llm_config_with_tools().

        Raises:
            ValueError: If the model is not a supported Grok model.
        """
        if not model_id.startswith("grok"):
            raise ValueError(f"Model '{model_id}' is not supported. Only Grok models are currently implemented.")

        if not settings.xai_api_key:
            raise ValueError("XAI_API_KEY is not configured.")

        self.model_id = model_id
        self.llm_config = llm_config

        base_client = openai.AsyncOpenAI(
            api_key=settings.xai_api_key.get_secret_value(),
            base_url=settings.xai_base_url,
        )
        self.client = track_openai_client(base_client)

    async def generate_content(
        self, contents: List[Dict[str, Any]]
    ) -> openai.types.chat.ChatCompletion:
        """Generate content using the Grok model.

        Args:
            contents: List of message dicts in OpenAI chat format
                      (e.g., [{"role": "user", "content": "..."}]).

        Returns:
            The ChatCompletion response.
        """
        return await self.client.chat.completions.create(
            model=self.model_id,
            messages=contents,
            **self.llm_config,
        )
