import itertools
import json
import logging
import threading

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

_log = logging.getLogger(__name__)

MODEL_TO_REQUIRED_API_KEY = {
    SupportedModels.GOOGLE_GEMINI_25_PRO: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_FLASH: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_FLASH_LITE: "GOOGLE_API_KEY",
    SupportedModels.XAI_GROK_420: "XAI_API_KEY",
    SupportedModels.XAI_GROK_41_FAST: "XAI_API_KEY",
}


# ---------------------------------------------------------------------------
# Google API key rotator — round-robin across GOOGLE_API_KEYS
# ---------------------------------------------------------------------------


class _GoogleKeyRotator:
    """Thread-safe round-robin rotator for multiple Google API keys.

    Initialised lazily from GOOGLE_API_KEYS (comma-separated) with fallback
    to GOOGLE_API_KEY.  Each call to next_key() returns the next key in the
    cycle, spreading TPM quota across N independent keys.
    """

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._cycle: itertools.cycle | None = None
        self._keys: list[str] = []
        self._initialised = False

    def _init(self) -> None:
        settings = get_settings()
        keys: list[str] = []

        # Prefer GOOGLE_API_KEYS (comma-separated, multiplied quota)
        if settings.GOOGLE_API_KEYS:
            keys = [k.strip() for k in settings.GOOGLE_API_KEYS.split(",") if k.strip()]

        # Fall back to single GOOGLE_API_KEY
        if not keys and settings.GOOGLE_API_KEY:
            keys = [settings.GOOGLE_API_KEY.get_secret_value()]

        if not keys:
            self._keys = []
            self._cycle = None
        else:
            self._keys = keys
            self._cycle = itertools.cycle(keys)
            if len(keys) > 1:
                _log.info("Google API key rotator initialised with %d keys (%.0f× TPM quota)", len(keys), len(keys))

        self._initialised = True

    def next_key(self) -> str | None:
        """Return the next API key, or None if no keys are configured."""
        with self._lock:
            if not self._initialised:
                self._init()
            if self._cycle is None:
                return None
            return next(self._cycle)

    @property
    def num_keys(self) -> int:
        with self._lock:
            if not self._initialised:
                self._init()
            return len(self._keys)


_google_key_rotator = _GoogleKeyRotator()


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
        if required_api_key == "GOOGLE_API_KEY":
            # Use round-robin key rotation for Google models to multiply TPM quota.
            api_key = _google_key_rotator.next_key()
            if not api_key:
                raise ValueError("No Google API key configured. Set GOOGLE_API_KEYS (comma-separated) or GOOGLE_API_KEY in your .env file.")
            model_kwargs["api_key"] = api_key
        else:
            if not getattr(settings, required_api_key):
                raise ValueError(f"Required environment variable `{required_api_key}` is not set")
            else:
                model_kwargs["api_key"] = getattr(settings, required_api_key)

    return init_chat_model(**model_kwargs)
