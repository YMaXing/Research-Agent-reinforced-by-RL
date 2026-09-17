import itertools
import json
import logging
import threading

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from brown.config import get_settings

from .config import (
    ANTHROPIC_NO_TEMPERATURE_MODELS,
    ANTHROPIC_UNSUPPORTED_PARAMS,
    DEFAULT_MODEL_CONFIGS,
    GOOGLE_ONLY_PARAMS,
    ModelConfig,
    SupportedModels,
)
from .fake_model import FakeModel

_log = logging.getLogger(__name__)

MODEL_TO_REQUIRED_API_KEY = {
    SupportedModels.GOOGLE_GEMINI_37_FLASH: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_31_FLASH_LITE: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_31_PRO_PREVIEW: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_PRO: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_FLASH: "GOOGLE_API_KEY",
    SupportedModels.GOOGLE_GEMINI_25_FLASH_LITE: "GOOGLE_API_KEY",
    SupportedModels.XAI_GROK_430: "XAI_API_KEY",
    SupportedModels.XAI_GROK_420: "XAI_API_KEY",
    SupportedModels.XAI_GROK_41_FAST: "XAI_API_KEY",
    SupportedModels.ANTHROPIC_CLAUDE_SONNET: "ANTHROPIC_API_KEY",
}


def extract_text_content(content: object) -> str:
    """Return the plain text from a chat model response's ``.content``.

    Most models return ``.content`` as a plain string. Some (e.g. gemini-3.7-flash)
    return a list of content-block dicts instead (e.g. ``{"type": "text", "text": "..."}``).
    This extracts the actual text from each block, dropping non-text blocks (e.g.
    "thinking", tool-call signatures), so callers get a consistent string regardless
    of which underlying model produced the response. Only needed for raw (non
    structured-output) ``ainvoke`` calls — ``with_structured_output`` results are
    already parsed and unaffected by this.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        text_parts = []
        for part in content:
            if isinstance(part, dict):
                block_type = part.get("type")
                if block_type is not None and block_type != "text":
                    continue
                text_parts.append(part.get("text", ""))
            else:
                text_parts.append(str(part))
        return "".join(text_parts)
    return str(content)


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
            responses = config.mocked_response if isinstance(config.mocked_response, list) else [config.mocked_response]
            idx = config._response_index % len(responses)
            config._response_index += 1
            chosen = responses[idx]
            if hasattr(chosen, "model_dump"):
                mocked_response_json = chosen.model_dump(mode="json")
            else:
                mocked_response_json = json.dumps(chosen)
            return FakeModel(responses=[mocked_response_json])
        else:
            return FakeModel(responses=[])

    config = config or DEFAULT_MODEL_CONFIGS.get(model) or ModelConfig()

    # If the caller passed an explicit config that doesn't set max_output_tokens, fall back
    # to the model's registered default rather than leaving it unset. This matters for
    # Anthropic models: langchain-anthropic derives its own max_tokens default from a local
    # model-profile table that may not yet know about newer model IDs, silently falling back
    # to a small 4096-token cap that truncates large structured-output responses.
    if config.max_output_tokens is None:
        default_for_model = DEFAULT_MODEL_CONFIGS.get(model)
        if default_for_model and default_for_model.max_output_tokens is not None:
            config = config.model_copy(update={"max_output_tokens": default_for_model.max_output_tokens})

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

    # Anthropic's Messages API has no equivalent for `n` (multiple completions);
    # passing it raises `AsyncMessages.create() got an unexpected keyword argument 'n'`.
    if model.value.startswith("anthropic:"):
        for key in ANTHROPIC_UNSUPPORTED_PARAMS:
            model_kwargs.pop(key, None)
        # Models with adaptive thinking always on manage sampling internally and reject
        # an explicit `temperature` (400 invalid_request_error: deprecated for this model).
        if model.value in ANTHROPIC_NO_TEMPERATURE_MODELS:
            model_kwargs.pop("temperature", None)

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


def structured_output_kwargs(model: SupportedModels) -> dict[str, str]:
    """Return the extra kwargs `with_structured_output()` should be called with for *model*.

    Anthropic's default `with_structured_output` method ("function_calling") forces a tool
    call and has been observed to unreliably encode nested `list[...]` fields for schemas
    like ours (stringified JSON, double-wrapped objects, JSON with trailing prose -- see
    `SectionsCoercionMixin`). Anthropic's dedicated `"json_schema"` structured-output method
    uses native constrained decoding instead of tool-call argument encoding and avoids this
    whole class of bug, so use it for all Anthropic models. Other providers keep their
    default method.
    """
    if model.value.startswith("anthropic:"):
        return {"method": "json_schema"}
    return {}
