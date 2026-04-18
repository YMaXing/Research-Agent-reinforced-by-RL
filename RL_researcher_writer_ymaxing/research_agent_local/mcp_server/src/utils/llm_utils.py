"""LLM utilities for creating and managing chat models."""

import logging
from typing import Optional, Type

from langchain.chat_models import init_chat_model
from langchain.chat_models.base import BaseChatModel
from langchain_tavily import TavilySearch
from pydantic import BaseModel

from ..config.settings import settings
from .opik_utils import TrackedLangChainModel, TrackedTavilyTool, is_opik_enabled, track_langchain_model

logger = logging.getLogger(__name__)


def get_chat_model(model_id: str, schema: Optional[Type[BaseModel]] = None) -> BaseChatModel | TrackedLangChainModel:
    """
    Initializes and returns a chat model from the centralized configuration.

    Args:
        model_id: The model identifier to use from llm_configs

    Returns:
        An instance of a LangChain chat model.
    """
    selected_model_config = settings.llm_configs[model_id]
    model_identifier = selected_model_config["identifier"]
    model_params = selected_model_config.get("params", {})
    api_key_env_var = selected_model_config.get("api_key_env_var")

    init_kwargs = model_params.copy()

    if api_key_env_var:
        # Get the appropriate API key based on the environment variable name
        api_key = None
        if api_key_env_var == "GOOGLE_API_KEY" and settings.google_api_key:
            api_key = settings.google_api_key.get_secret_value()
        elif api_key_env_var == "XAI_API_KEY" and settings.xai_api_key:
            api_key = settings.xai_api_key.get_secret_value()
        elif api_key_env_var == "TAVILY_API_KEY" and settings.tavily_api_key:
            if settings.search_enhancement_model.startswith("grok"):
                api_key = settings.xai_api_key.get_secret_value()
            elif settings.search_enhancement_model.startswith("gemini"):
                api_key = settings.google_api_key.get_secret_value()
            else:
                raise RuntimeError(f"Unsupported structure enhancement model for Tavily tool: {settings.search_enhancement_model}")
        if not api_key:
            msg = f"{api_key_env_var} environment variable not set."
            logger.error(msg)
            raise RuntimeError(msg)
        init_kwargs["api_key"] = api_key

    model = init_chat_model(model_identifier, **init_kwargs)

    if schema is not None:
        model = model.with_structured_output(schema)



    # Apply Opik tracking if configured
    if is_opik_enabled():
        return track_langchain_model(model, model_id)

    return model

def get_tavily_tool(model_id: str = "tavily") -> TavilySearch | TrackedTavilyTool:
    """
    Initializes and returns a Tavily search tool from the centralized configuration.
    Works exactly like get_chat_model() and includes Opik tracking when enabled.
    """
    selected_model_config = settings.llm_configs[model_id]
    tool_params = selected_model_config.get("params", {})
    api_key_env_var = selected_model_config.get("api_key_env_var")

    init_kwargs = tool_params.copy()

    # Reuse your existing API key logic (exactly as in get_chat_model)
    if api_key_env_var == "TAVILY_API_KEY" and settings.tavily_api_key:
        init_kwargs["api_key"] = settings.tavily_api_key.get_secret_value()
    elif api_key_env_var and not init_kwargs.get("api_key"):
        msg = f"{api_key_env_var} environment variable not set."
        logger.error(msg)
        raise RuntimeError(msg)

    tool = TavilySearch(**init_kwargs)

    # Apply Opik tracking if configured (identical pattern to your LLMs)
    if is_opik_enabled():
        return TrackedTavilyTool(tool, model_id, settings.opik_project_name)

    return tool