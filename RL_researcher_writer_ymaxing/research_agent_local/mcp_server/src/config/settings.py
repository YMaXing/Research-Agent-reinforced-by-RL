"""Server configuration settings."""

import logging
from typing import Any, Dict, Union

from numpy import maximum
from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Application settings for the Research MCP Server."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    # Server settings
    server_name: str = Field(default="Research MCP Server", description="The name of the server")
    version: str = Field(default="0.1.0", description="The version of the server")
    log_level: Union[int, str] = Field(default=logging.INFO, alias="LOG_LEVEL", description="The log level")
    log_level_dependencies: Union[int, str] = Field(
        default=logging.WARNING, alias="LOG_LEVEL_DEPENDENCIES", description="The log level for dependencies"
    )

    @field_validator("log_level", "log_level_dependencies", mode="before")
    @classmethod
    def _parse_log_level(cls, v: Any) -> int:
        if isinstance(v, str):
            level = logging.getLevelName(v.upper())
            if not isinstance(level, int):
                raise ValueError(f"Invalid log level: {v!r}")
            return level
        return v

    # Research settings
    maximum_exploration_rounds: int = Field(default=3, alias="MAXIMUM_EXPLORATION_ROUNDS", description="Maximum number of exploration rounds in the research loop")
    n_exploration_queries_per_round: int = Field(default=4, alias="N_EXPLORATION_QUERIES_PER_ROUND", description="Number of exploration queries to generate per exploration round. Only applicable if maximum_exploration_rounds > 0.")
    maximum_sources_to_scrape: int = Field(default=6, alias="MAXIMUM_SOURCES_TO_SCRAPE", description="Maximum number of sources to scrape fully during research")
    enable_content_dedup: bool = Field(default=False, alias="ENABLE_CONTENT_DEDUP", description="Whether to run the content deduplication step (step 7). Set to false to feed the full raw research into the final file.")
    user_plan_override_allowed: bool = Field(
        default=True,
        alias="USER_PLAN_OVERRIDE_ALLOWED",
        description=(
            "Whether the workflow always stops after predict_exploration_preset (step 3.4) to present "
            "the RL+guards pipeline's recommended exploration plan and let the user confirm or override "
            "it before step 4 runs. Defaults to True: the client always presents the recommendation and "
            "waits for the user's decision, looping on natural-language overrides until the user says "
            "the plan is final. Set False to skip this and proceed straight from the recommendation to "
            "step 4 automatically — the only remaining stop in that mode is the narrower "
            "'AMBIGUOUS'-tagged policy-guard question (see research_instructions_prompt.py step 3.4). "
            "An unprompted user override is always honoured regardless of this setting."
        ),
    )
    
    # LLM Configuration
    youtube_transcription_model: str = Field(default="gemini-3.7-flash", description="Model for YouTube transcription, only supported Gemini models")
    scraping_model: str = Field(default="gemini-3.7-flash", description="Model for web scraping")
    query_generation_model: str = Field(default="grok-4.6", description="Model for query generation")
    search_enhancement_model: str = Field(default="grok-4.6-non-reasoning", description="Model for search enhancement")
    source_selection_model: str = Field(default="grok-4.6", description="Model for source selection")
    content_dedup_model: str = Field(default="grok-4.6-reasoning", description="Model for content deduplication")
    
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
    anthropic_api_key: SecretStr | None = Field(
        default=None,
        alias="ANTHROPIC_API_KEY",
        description=(
            "The API key for the Anthropic (Claude) API. Passed through to the "
            "rl_inference_service/generate_digests.py subprocess for its optional "
            "Layer-3 fallback; not otherwise used by the server itself."
        ),
    )
    tavily_api_key: SecretStr | None = Field(
        default=None, alias="TAVILY_API_KEY", description="The API key for the Tavily API"
    )
    jina_api_key: SecretStr | None = Field(
        default=None, alias="JINA_API_KEY", description="The API key for the Jina.ai Reader API"
    )

    # RL exploration-preset inference service (rl_inference_service/)
    rl_infer_adapter_dir: str | None = Field(
        default=None,
        alias="RL_INFER_ADAPTER_DIR",
        description=(
            "Optional override for which LoRA checkpoint the RL inference server (infer.py) "
            "loads, as an absolute path. Defaults to rl_inference_service/_infer_config.py's "
            "own DEFAULT_ADAPTER_DIR when unset."
        ),
    )
    rl_infer_port: int = Field(
        default=8787,
        alias="RL_INFER_PORT",
        description="Localhost port the RL inference server (infer.py --serve) listens on.",
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
            "gemini-3.1-pro-preview": {
                # NOTE: previously named "gemini-3-pro" with identifier "google_genai:gemini-3-pro",
                # which is not a real Gemini model id (was never usable). Fixed to a valid identifier.
                "identifier": "google_genai:gemini-3.1-pro-preview",
                "api_key_env_var": "GOOGLE_API_KEY",
                "params": {
                    "temperature": 0.8,
                    "thinking_budget": 1000,
                    "include_thoughts": False,
                    "max_retries": 3,
                },
            },
            "gemini-3.7-flash": {
                "identifier": "google_genai:gemini-3.7-flash",
                "api_key_env_var": "GOOGLE_API_KEY",
                "params": {
                    "temperature": 1,
                    "thinking_budget": 1000,
                    "include_thoughts": False,
                    "max_retries": 3,
                },
            },
            "gemini-2.5-flash": {
                # Kept for backward compatibility; no longer the default for any role.
                "identifier": "google_genai:gemini-2.5-flash",
                "api_key_env_var": "GOOGLE_API_KEY",
                "params": {
                    "temperature": 1,
                    "thinking_budget": 1000,
                    "include_thoughts": False,
                    "max_retries": 3,
                },
            },
            "grok-4.6": {
                "identifier": "xai:grok-4.6",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.8,
                    # supports low/medium/high/xhigh; high is xAI's own default. grok-4.6 is a single
                    # unified model (no separate reasoning/non-reasoning SKU like the 4.20 generation).
                    "reasoning_effort": "high",
                    "max_retries": 3,
                },
            },
            "grok-4.6-reasoning": {
                "identifier": "xai:grok-4.6",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.8,
                    "max_retries": 3,
                },
            },
            "grok-4.6-non-reasoning": {
                "identifier": "xai:grok-4.6",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.0,
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
                # Kept for backward compatibility; deprecated by xAI in favor of grok-4.20-non-reasoning.
                "identifier": "xai:grok-4-1-fast-non-reasoning",
                "api_key_env_var": "XAI_API_KEY",
                "params": {
                    "temperature": 0.0,
                },
            },
            "grok-4-1-fast-reasoning": {
                # Kept for backward compatibility; deprecated by xAI in favor of grok-4.20-reasoning.
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
                    "include_raw_content": False,  # raw page HTML is fetched separately by scrape_research_urls_tool; enabling this bloats the LLM prompt 20-50x with no quality gain
                    "include_answer": True,
                    # add any other Tavily params you like (time_range, include_images, etc.)
                },
            }
        }


# Global settings instance
settings = Settings()
