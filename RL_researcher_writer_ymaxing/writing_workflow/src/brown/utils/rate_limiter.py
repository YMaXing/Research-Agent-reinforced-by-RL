"""Global async rate-limiter for LLM API calls.

Usage (in workflow nodes):

    from brown.utils.rate_limiter import llm_throttle

    async with llm_throttle():
        output = await self.model.ainvoke(inputs)

Configuration (call once at process startup, e.g. in rl_writing_generator.py):

    from brown.utils.rate_limiter import set_llm_concurrency
    set_llm_concurrency(2)  # allow at most 2 concurrent LLM calls
"""

from __future__ import annotations

import asyncio
import logging
import time
from contextlib import asynccontextmanager
from typing import AsyncIterator

_log = logging.getLogger(__name__)

# Default: 3 concurrent LLM API calls across the entire process.
# Gemini 2.5 Pro supports ~150 RPM and 2M TPM on the paid tier.
# 3 concurrent calls is a safe default; raise via --llm-concurrency if you
# have higher quota headroom.
_DEFAULT_CONCURRENCY = 3

# After a 429 failure escapes (after tenacity gives up), we hold the semaphore
# for this many extra seconds before releasing it to the next caller.
# Both xAI and Gemini enforce per-minute windows; with large-context article
# calls (100K-500K tokens), the TPM window often needs a full 90s to clear.
_QUOTA_COOLDOWN_SECS: int = 90

# Minimum seconds between successive LLM calls.
# Gemini 2.5 Pro has a 150 RPM ceiling (~0.4 s/call theoretically), but each
# article call consumes 100K-500K tokens so TPM is the binding constraint.
# An 8 s gap keeps burst RPM well below 60 and spaces out token consumption
# across the per-minute TPM window more evenly.
_INTER_CALL_DELAY_SECS: float = 8.0

# Module-level semaphore — lazily created the first time llm_throttle() is
# entered so it is always bound to the running event loop.
_semaphore: asyncio.Semaphore | None = None
_max_concurrency: int = _DEFAULT_CONCURRENCY

# Monotonic timestamp of the most recent LLM call completion (success or fail).
_last_call_finished: float = 0.0


def set_llm_concurrency(n: int) -> None:
    """Set the maximum number of concurrent LLM calls for this process.

    Must be called *before* any LLM call is made (i.e. before the workflow
    starts).  Calling it after the semaphore has been initialised has no
    effect and logs a warning.
    """
    global _max_concurrency, _semaphore
    if _semaphore is not None:
        _log.warning(
            "set_llm_concurrency(%d) called after semaphore was already initialised — ignoring.  Call before starting any workflow.", n
        )
        return
    _max_concurrency = n


def _get_semaphore() -> asyncio.Semaphore:
    """Return (and lazily create) the process-level LLM semaphore."""
    global _semaphore
    if _semaphore is None:
        _semaphore = asyncio.Semaphore(_max_concurrency)
    return _semaphore


def _is_quota_error(exc: BaseException) -> bool:
    """Return True if *exc* looks like a Gemini 429 / quota-exhausted error."""
    try:
        from google.api_core.exceptions import ResourceExhausted  # type: ignore[import-untyped]

        if isinstance(exc, ResourceExhausted):
            return True
    except ImportError:
        pass
    # Fall back to string matching for when the exception is wrapped by LangChain.
    msg = str(exc).lower()
    return "resourceexhausted" in msg or "429" in msg or "quota" in msg


@asynccontextmanager
async def llm_throttle() -> AsyncIterator[None]:
    """Async context manager that gates entry to at most *max_concurrency*
    concurrent LLM API calls across the entire process.

    Before yielding, enforces a minimum gap of *_INTER_CALL_DELAY_SECS*
    since the last call finished to prevent burst-rate TPM violations.

    When a quota-exhausted (429) error escapes after tenacity has given up,
    the semaphore slot is held for an extra *_QUOTA_COOLDOWN_SECS* seconds
    before being released.  This lets the Gemini per-minute token window reset
    so the next caller doesn't immediately hit the same limit.

    Example::

        async with llm_throttle():
            output = await self.model.ainvoke(inputs)
    """
    global _last_call_finished
    async with _get_semaphore():
        # Enforce minimum gap between successive calls to spread token usage
        # across the 60-second TPM window and avoid burst-rate violations.
        since_last = time.monotonic() - _last_call_finished
        if _last_call_finished > 0 and since_last < _INTER_CALL_DELAY_SECS:
            gap = _INTER_CALL_DELAY_SECS - since_last
            _log.info("Rate-limiter: waiting %.1fs before next LLM call", gap)
            await asyncio.sleep(gap)
        try:
            yield
        except Exception as exc:
            if _is_quota_error(exc):
                _log.warning(
                    "Quota exhausted (429) — holding rate-limiter slot for %ds to let the per-minute window reset.",
                    _QUOTA_COOLDOWN_SECS,
                )
                await asyncio.sleep(_QUOTA_COOLDOWN_SECS)
            raise
        finally:
            _last_call_finished = time.monotonic()
