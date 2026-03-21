"""Opik configuration and tracking utilities."""

import opik
import openai
from google import genai
from opik.integrations.genai import track_genai
from opik.integrations.openai import track_openai

from ..settings import settings


def configure_opik():
    """Configure Opik monitoring if all required settings are provided.

    Returns:
        bool: True if Opik was configured, False otherwise
    """
    if settings.opik_api_key and settings.opik_workspace and settings.opik_project_name:
        opik.configure(
            api_key=settings.opik_api_key.get_secret_value(),
            workspace=settings.opik_workspace,
            use_local=False,
            force=True,
        )
        return True
    return False


def track_genai_client(client: genai.Client) -> genai.Client:
    """Track a Gemini client with Opik if configured.

    Args:
        client: The Gemini client to track

    Returns:
        The tracked client if Opik is configured, otherwise the original client
    """
    # Apply Opik tracking if all required settings are configured
    if settings.opik_api_key and settings.opik_workspace and settings.opik_project_name:
        return track_genai(client, project_name=settings.opik_project_name)
    else:
        return client


def track_openai_client(client: openai.AsyncOpenAI) -> openai.AsyncOpenAI:
    """Track an OpenAI-compatible client (e.g. Grok/xAI) with Opik if configured.

    Args:
        client: The AsyncOpenAI client to track

    Returns:
        The tracked client if Opik is configured, otherwise the original client
    """
    if settings.opik_api_key and settings.opik_workspace and settings.opik_project_name:
        return track_openai(client, project_name=settings.opik_project_name)
    else:
        return client
    

