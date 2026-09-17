"""LLM and Gemini utilities for configuration and response processing."""

from typing import Any, Dict, List, Optional

from google import genai
from google.genai import types

from ..settings import settings
from .opik_handler import track_genai_client


def build_llm_config_with_tools(
    mcp_tools: List, thinking_enabled: bool = True, params: Optional[Dict[str, Any]] = None
) -> types.GenerateContentConfig:
    """Build Gemini config with all MCP tools converted to Gemini format."""
    params = params or {}
    gemini_tools = []

    for tool in mcp_tools:
        gemini_tool = types.Tool(
            function_declarations=[
                types.FunctionDeclaration(
                    name=tool.name,
                    description=tool.description,
                    parameters=tool.inputSchema,
                )
            ]
        )
        gemini_tools.append(gemini_tool)

    # Create thinking config dynamically based on current state
    thinking_config = types.ThinkingConfig(
        include_thoughts=thinking_enabled,
        thinking_budget=params.get("thinking_budget", settings.thinking_budget),
    )

    return types.GenerateContentConfig(
        tools=gemini_tools,
        thinking_config=thinking_config,
        temperature=params.get("temperature"),
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )


def extract_thought_summary(response: types.GenerateContentResponse) -> str | None:
    """Collect human-readable thought summaries if present."""
    parts = getattr(response.candidates[0].content, "parts", []) or []
    chunks = [p.text for p in parts if getattr(p, "thought", False) and getattr(p, "text", None)]
    return "\n".join(chunks).strip() if chunks else None


def extract_final_answer(response: types.GenerateContentResponse) -> str | None:
    """Extract the final answer from the response."""
    parts = getattr(response.candidates[0].content, "parts", []) or []
    chunks = [p.text for p in parts if not getattr(p, "thought", False) and getattr(p, "text", None)]
    return "\n".join(chunks).strip() if chunks else None


def extract_first_function_call(response: types.GenerateContentResponse):
    """Return (name, args) for the first function call, or None if the model produced a final answer."""
    if getattr(response, "function_calls", None):
        fc = response.function_calls[0]
        return fc.name, dict(fc.args or {})
    parts = getattr(response.candidates[0].content, "parts", []) or []
    for p in parts:
        if getattr(p, "function_call", None):
            return p.function_call.name, dict(p.function_call.args or {})
    return None


class LLMClient:
    """Model-agnostic LLM client for generating content."""

    def __init__(self, model_id: str, llm_config: types.GenerateContentConfig, params: Optional[Dict[str, Any]] = None):
        """Initialize LLM client with specified model and configuration.

        Args:
            model_id: The model identifier (e.g., 'gemini-2.5-flash')
            llm_config: The configuration for content generation
            params: Per-model params from orchestrator_configs (max_retries).

        Raises:
            ValueError: If the model is not supported
        """
        if not model_id.startswith("gemini"):
            raise ValueError(f"Model '{model_id}' is not supported. Only Gemini models are currently implemented.")

        self.model_id = model_id
        self.llm_config = llm_config
        params = params or {}

        # Initialize Gemini client with Opik tracking if configured
        http_options = types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=params.get("max_retries", 3))
        )
        base_client = genai.Client(api_key=settings.google_api_key.get_secret_value(), http_options=http_options)
        self.client = track_genai_client(base_client)

    async def generate_content(self, contents: List[types.Content]) -> types.GenerateContentResponse:
        """Generate content using the configured LLM model.

        Args:
            contents: The conversation contents

        Returns:
            The generated content response
        """
        return await self.client.aio.models.generate_content(
            model=self.model_id,
            contents=contents,
            config=self.llm_config,
        )
