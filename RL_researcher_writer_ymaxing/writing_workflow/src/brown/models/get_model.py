import json

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from brown.config import get_settings

from .config import (
    DEFAULT_MODEL_CONFIGS,
    GOOGLE_ONLY_PARAMS,
    ModelConfig,
    SupportedModels,
)
from .fake_model import FakeModel

MODEL_TO_REQUIRED_API_KEY = {
    SupportedModels.GOOGLE_GEMINI_25_PRO: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_FLASH: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_FLASH_LITE: "GOOGLE_API_KEY",
    SupportedModels.XAI_GROK_420: "XAI_API_KEY",
    SupportedModels.XAI_GROK_41_FAST: "XAI_API_KEY",
}


def get_model(model: SupportedModels, config: ModelConfig | None = None) -> BaseChatModel:
    if model == SupportedModels.FAKE_MODEL:
        if config and config.mocked_response is not None:
            if hasattr(config.mocked_response, "model_dump"):
                mocked_response_json = config.mocked_response.model_dump(mode="json")
            else:
                mocked_response_json = json.dumps(config.mocked_response)
            return FakeModel(responses=[mocked_response_json])
        else:
            return FakeModel(responses=[])

    config = config or DEFAULT_MODEL_CONFIGS.get(model) or ModelConfig()
    model_kwargs = {
        "model": model.value,
        **config.model_dump(),
    }

    # Remove Google-specific params for non-Google providers.
    if not model.value.startswith("google_genai:"):
        for key in GOOGLE_ONLY_PARAMS:
            model_kwargs.pop(key, None)
        # ChatXAI (OpenAI-compatible) uses 'max_tokens' instead of 'max_output_tokens'.
        max_out = model_kwargs.pop("max_output_tokens", None)
        if max_out is not None:
            model_kwargs["max_tokens"] = max_out

    required_api_key = MODEL_TO_REQUIRED_API_KEY.get(model)
    if required_api_key:
        settings = get_settings()
        if not getattr(settings, required_api_key):
            raise ValueError(f"Required environment variable `{required_api_key}` is not set")
        else:
            model_kwargs["api_key"] = getattr(settings, required_api_key)

    return init_chat_model(**model_kwargs)
