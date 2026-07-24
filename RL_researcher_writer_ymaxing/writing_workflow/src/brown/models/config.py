from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field, PrivateAttr


class SupportedModels(StrEnum):
    GOOGLE_GEMINI_25_PRO = "google_genai:gemini-2.5-pro"
    GOOGLE_GEMINI_25_FLASH = "google_genai:gemini-2.5-flash"
    GOOGLE_GEMINI_25_FLASH_LITE = "google_genai:gemini-2.5-flash-lite"
    XAI_GROK_430 = "xai:grok-4.3"
    XAI_GROK_420 = "xai:grok-4.20-0309-reasoning"
    XAI_GROK_41_FAST = "xai:grok-4-1-fast-reasoning"
    # Claude Sonnet 5 has a 1M-token context window by default (vs. 200k on Sonnet 4.5),
    # which is required for grading large presets whose combined prompt can exceed 200k tokens.
    ANTHROPIC_CLAUDE_SONNET = "anthropic:claude-sonnet-5"
    FAKE_MODEL = "fake"


class ModelConfig(BaseModel):
    temperature: float = 0.7
    top_k: int | None = None
    n: int = 1
    response_modalities: list[str] | None = None
    include_thoughts: bool = False
    thinking_budget: int | None = Field(
        default=None,
        ge=0,
        description="If reasoning is available, the maximum number of tokens the model can use for thinking.",
    )
    max_output_tokens: int | None = None
    max_retries: int = 1

    mocked_response: Any | list[Any] | None = None

    # Tracks which item in a list mocked_response to use on the next get_model call.
    _response_index: int = PrivateAttr(default=0)

    def model_dump(self, *args, **kwargs) -> dict[str, Any]:
        return super().model_dump(
            include={
                "temperature",
                "top_k",
                "n",
                "response_modalities",
                "thinking_budget",
                "max_output_tokens",
                "max_retries",
            },
            mode=kwargs.pop("mode", "json"),
            *args,
            **kwargs,
        )


# Parameters that are Google-specific and should not be passed to non-Google providers.
GOOGLE_ONLY_PARAMS = {"thinking_budget", "top_k", "response_modalities"}

# Parameters unsupported by the Anthropic Messages API (e.g. `n` for multiple
# completions has no Anthropic equivalent and raises a TypeError if passed).
ANTHROPIC_UNSUPPORTED_PARAMS = {"n"}

# Anthropic models with adaptive thinking always on (Claude Sonnet 5, Opus 4.8, Fable 5,
# Mythos 5) manage sampling internally and reject an explicit `temperature`, raising
# `invalid_request_error: 'temperature' is deprecated for this model`.
ANTHROPIC_NO_TEMPERATURE_MODELS = {
    "anthropic:claude-sonnet-5",
    "anthropic:claude-opus-4-8",
    "anthropic:claude-fable-5",
    "anthropic:claude-mythos-5",
}

DEFAULT_MODEL_CONFIGS = {
    "google_genai:gemini-2.5-pro": ModelConfig(
        temperature=0.7,
        include_thoughts=False,
        thinking_budget=1000,
        max_retries=1,
    ),
    "google_genai:gemini-2.5-flash": ModelConfig(
        temperature=1,
        thinking_budget=1000,
        include_thoughts=False,
        max_retries=1,
    ),
    "xai:grok-4.20-0309-reasoning": ModelConfig(
        temperature=0.7,
        max_retries=1,
    ),
    "xai:grok-4-1-fast-reasoning": ModelConfig(
        temperature=0.0,
        max_retries=1,
    ),
    "anthropic:claude-sonnet-5": ModelConfig(
        temperature=0.0,
        max_retries=1,
        # The installed langchain-anthropic version doesn't yet recognise "claude-sonnet-5"
        # in its model-profile table, so it silently falls back to a 4096-token max_tokens
        # default -- far too small for multi-section structured-output grading and causes
        # truncated/unparseable tool calls (`stop_reason: max_tokens`). Set explicitly
        # (Sonnet 5 supports up to 128k output tokens).
        max_output_tokens=64000,
    ),
}
