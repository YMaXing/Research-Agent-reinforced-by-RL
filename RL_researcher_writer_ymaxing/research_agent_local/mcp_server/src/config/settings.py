"""Server configuration settings."""

import logging
from typing import Any, Dict

from numpy import maximum
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Application settings for the Research MCP Server."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    # Server settings
    server_name: str = Field(default="Research MCP Server", description="The name of the server")
    version: str = Field(default="0.1.0", description="The version of the server")
    log_level: int = Field(default=logging.INFO, alias="LOG_LEVEL", description="The log level")
    log_level_dependencies: int = Field(
        default=logging.WARNING, alias="LOG_LEVEL_DEPENDENCIES", description="The log level for dependencies"
    )

    # Research settings
    maximum_exploration_rounds: int = Field(default=3, alias="MAXIMUM_EXPLORATION_ROUNDS", description="Maximum number of exploration rounds in the research loop")
    n_exploration_queries_per_round: int = Field(default=4, alias="N_EXPLORATION_QUERIES_PER_ROUND", description="Number of exploration queries to generate per exploration round. Only applicable if maximum_exploration_rounds > 0.")
    maximum_sources_to_scrape: int = Field(default=6, alias="MAXIMUM_SOURCES_TO_SCRAPE", description="Maximum number of sources to scrape fully during research")
    enable_content_dedup: bool = Field(default=False, alias="ENABLE_CONTENT_DEDUP", description="Whether to run the content deduplication step (step 7). Set to false to feed the full raw research into the final file.")
    
    # LLM Configuration
    youtube_transcription_model: str = Field(default="gemini-2.5-flash", description="Model for YouTube transcription, only supported Gemini models")
    scraping_model: str = Field(default="grok-4-1-fast-reasoning", description="Model for web scraping")
    query_generation_model: str = Field(default="grok-4.20-reasoning", description="Model for query generation")
    search_enhancement_model: str = Field(default="grok-4-1-fast-non-reasoning", description="Model for search enhancement")
    source_selection_model: str = Field(default="grok-4-1-fast-reasoning", description="Model for source selection")
    content_dedup_model: str = Field(default="grok-4-1-fast-reasoning", description="Model for content deduplication")

    # API Keys
    google_api_key: SecretStr | None = Field(
        default=None, alias="GOOGLE_API_KEY", description="The API key for the Google API"
    )
    firecrawl_api_key: SecretStr | None = Field(
        default=None, alias="FIRECRAWL_API_KEY", description="The API key for the Firecrawl API"
    )
    github_token: SecretStr | None = Field(default=None, alias="GITHUB_TOKEN", description="The GitHub token")
    xai_api_key: SecretStr | None = Field(
        default=None, alias="XAI_API_KEY", description="The API key for the xAI (Grok) API"
    )
    tavily_api_key: SecretStr | None = Field(
        default=None, alias="TAVILY_API_KEY", description="The API key for the Tavily API"
    )

    # Opik Monitoring Configuration
    opik_api_key: SecretStr | None = Field(
        default=None, alias="OPIK_API_KEY", description="The API key to authenticate with Opik"
    )
    opik_workspace: str | None = Field(
        default=None,
        alias="OPIK_WORKSPACE",
        description="The Opik workspace name. If not set, the default workspace will be used.",
    )
    opik_project_name: str = Field(default="nova", alias="OPIK_PROJECT_NAME", description="Opik's project name")

    @property
    def llm_configs(self) -> Dict[str, Dict[str, Any]]:
        """Get the LLM configurations."""
        return {
            "gemini-3-pro": {
                "identifier": "google_genai:gemini-3-pro",
                "api_key_env_var": "GOOGLE_API_KEY",
                "params": {
                    "temperature": 0.8,
                    "thinking_budget": 1000,
                    "include_thoughts": False,
                    "max_retries": 3,
                },
            },
            "gemini-2.5-flash": {
                "identifier": "google_genai:gemini-2.5-flash",
                "api_key_env_var": "GOOGLE_API_KEY",
                "params": {
                    "temperature": 1,
                    "thinking_budget": 1000,
                    "include_thoughts": False,
                    "max_retries": 3,
                },
            },
            "grok-4.20-reasoning": {
                "identifier": "xai:grok-4.20-0309-reasoning",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.8,
                    "max_retries": 3,
                },
            },
            "grok-4.20-multi-agent": {
                "identifier": "xai:grok-4.20-multi-agent-0309",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.8,
                    "max_retries": 3,
                },
            },
            "grok-4-1-fast-non-reasoning": {
                "identifier": "xai:grok-4-1-fast-non-reasoning",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.0,
                },
            },
            "grok-4-1-fast-reasoning": {
                "identifier": "xai:grok-4-1-fast-reasoning",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 1,
                },
            },
            "tavily": {
                "identifier": "tavily",    
                "api_key_env_var": "TAVILY_API_KEY",       # ignored for tools, kept for config consistency
                "params": {
                    "max_results": 5,
                    "search_depth": "advanced",
                    "include_raw_content": True,
                    "include_answer": True,
                    # add any other Tavily params you like (time_range, include_images, etc.)
                },
            }
        }


# Global settings instance
settings = Settings()
