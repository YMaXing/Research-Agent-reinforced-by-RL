"""Client configuration settings."""

import logging
from pathlib import Path
from typing import Any, Dict

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Application settings for the MCP Client."""

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        extra="ignore",
        env_file_encoding="utf-8",
    )

    # Server settings and paths
    project_root: Path = Field(
        default_factory=lambda: Path(__file__).parent.parent, description="The root directory of the mcp_client project"
    )
    server_main_path: Path = Field(
        default_factory=lambda: Path(__file__).parent.parent.parent / "mcp_server",
        description="The path to the server's main.py file",
    )
    log_level: int = Field(default=logging.INFO, alias="LOG_LEVEL", description="The log level")
    log_level_dependencies: int = Field(
        default=logging.WARNING, alias="LOG_LEVEL_DEPENDENCIES", description="The log level for dependencies"
    )

    # LLM Configuration
    google_api_key: SecretStr | None = Field(default=None, alias="GOOGLE_API_KEY", description="The Google API key for Gemini models")
    xai_api_key: SecretStr | None = Field(default=None, alias="XAI_API_KEY", description="The xAI API key for Grok models")
    xai_base_url: str = Field(default="https://api.x.ai/v1", alias="XAI_BASE_URL", description="The xAI API base URL")
    orchestrator_key: str = Field(default="grok-4.1-fast-reasoning", description="Default orchestrator model key")
    model_id: str = Field(default="grok-4.1-fast-reasoning", description="Default model ID for LLM operations")
    thinking_budget: int = Field(default=1024, alias="THINKING_BUDGET", description="Thinking budget for latency vs. depth tradeoff")

    # Agent configuration
    max_iterations: int = Field(default=15, description="Maximum number of iterations for the agent loop") 

    # Opik Configuration
    opik_api_key: SecretStr | None = Field(default=None, alias="OPIK_API_KEY", description="The API key for Opik")
    opik_workspace: str | None = Field(default=None, alias="OPIK_WORKSPACE", description="The Opik workspace name")
    opik_project_name: str | None = Field(default=None, alias="OPIK_PROJECT_NAME", description="The Opik project name")

    @property
    def orchestrator_configs(self) -> Dict[str, Dict[str, Any]]:
        """Get the orchestrator configurations."""
        return {
            "gemini-2.5-flash": {
                "identifier": "google_genai:gemini-2.5-flash",
                "params": {
                    "temperature": 1,
                    "thinking_budget": -1,
                    "include_thoughts": True,
                    "max_retries": 3,
                },
            },
            "grok-4.1-fast-reasoning": {
                "identifier": "xai:grok-4.1-fast-reasoning",
                "params": {
                    "temperature": 1,
                    "thinking_budget": self.thinking_budget,
                    "max_retries": 3,
                },
            },
        }


# Global settings instance
settings = Settings()
