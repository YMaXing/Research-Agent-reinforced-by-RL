import os
from functools import lru_cache
from typing import Annotated

from loguru import logger
from pydantic import Field, FilePath, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_PATH = os.getenv("ENV_FILE_PATH", ".env")
logger.info(f"Loading environment file from `{ENV_FILE_PATH}`")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="ignore", env_file_encoding="utf-8")

    # --- Gemini ---

    GOOGLE_API_KEY: SecretStr | None = Field(default=None, alias="GOOGLE_API_KEY", description="The API key for the Gemini API.")

    # Multiple comma-separated Gemini keys for round-robin rotation to multiply TPM quota.
    # Example: GOOGLE_API_KEYS=AIza...key1,AIza...key2,AIza...key3
    # Falls back to GOOGLE_API_KEY if not set.
    GOOGLE_API_KEYS: str | None = Field(
        default=None, alias="GOOGLE_API_KEYS", description="Comma-separated Google API keys for round-robin rotation."
    )

    # --- xAI ---

    XAI_API_KEY: SecretStr | None = Field(default=None, alias="XAI_API_KEY", description="The API key for the xAI API.")

    # --- Opik ---

    OPIK_ENABLED: bool = Field(default=False, alias="OPIK_ENABLED", description="Whether to use Opik for monitoring and logging.")
    OPIK_WORKSPACE: str | None = Field(
        default=None, alias="OPIK_WORKSPACE", description="Name of the Opik workspace containing the project."
    )
    OPIK_PROJECT_NAME: str = Field(default="brown", alias="OPIK_PROJECT_NAME", description="Name of the Opik project.")
    OPIK_API_KEY: SecretStr | None = Field(default=None, alias="OPIK_API_KEY", description="The API key for the Opik API.")

    # --- App Config ---

    CONFIG_FILE: Annotated[
        FilePath, Field(default="configs/course.yaml", alias="CONFIG_FILE", description="Path to the application configuration YAML file.")
    ]


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
