"""
RL inference server management for the predict_exploration_preset tool.

Manages the lifecycle of the infer.py HTTP subprocess (Qwen3-4B + LoRA, NF4
quantised, training venv) and exposes the three lightweight signal helpers that
are shared between the infer handler and the planner handler.
"""

from __future__ import annotations

import json as _json
import logging
import math
import subprocess
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths  (parents[3] = research_agent_local/  for files in mcp_server/src/app/)
# ---------------------------------------------------------------------------
_TRAINING_DIR = Path(__file__).resolve().parents[3] / "training"
_TRAINING_PYTHON = _TRAINING_DIR / ".venv" / "bin" / "python"
_INFER_SCRIPT = _TRAINING_DIR / "infer.py"

# ---------------------------------------------------------------------------
# 4-preset vocabulary (mirrors _rl_preset.py)
# ---------------------------------------------------------------------------
PRESET_NAMES: dict[int, str] = {0: "skip", 1: "light", 2: "standard", 3: "deep"}
NUM_PRESETS: int = 4
ENTROPY_THRESHOLD_HIGH: float = 1.5
ENTROPY_THRESHOLD_LOW: float = 0.5
CONFIDENCE_STRONG: float = 0.70
CONFIDENCE_MODERATE: float = 0.40

# ---------------------------------------------------------------------------
# Infer server process management
# ---------------------------------------------------------------------------
_INFER_PORT = 8787
_INFER_STARTUP_TIMEOUT = 1800  # seconds — Qwen3-4B NF4 over /mnt/f/ can take >5 min

_infer_proc: subprocess.Popen | None = None
_infer_lock = threading.Lock()

# Collects stderr from the infer subprocess so the OS pipe never blocks.
_infer_stderr_lines: list[str] = []
_infer_stderr_lock = threading.Lock()


def _drain_stderr(proc: subprocess.Popen) -> None:
    """Background thread: read stderr line-by-line, log each line, keep last 200."""
    if proc.stderr is None:
        return
    for raw in proc.stderr:
        line = raw.decode(errors="replace").rstrip()
        logger.debug("[infer-server] %s", line)
        with _infer_stderr_lock:
            _infer_stderr_lines.append(line)
            if len(_infer_stderr_lines) > 200:
                _infer_stderr_lines.pop(0)


def ensure_infer_server() -> str:
    """Start the infer.py HTTP server subprocess if not already running.

    Uses the training venv's Python (which has torch/transformers installed).
    Blocks until the /health endpoint responds or the startup timeout is reached.
    Returns the server base URL (``http://127.0.0.1:<port>``).

    stderr is drained by a background thread to prevent pipe-buffer stalls
    (bitsandbytes / transformers can emit hundreds of KB during model load).
    """
    global _infer_proc
    base_url = f"http://127.0.0.1:{_INFER_PORT}"
    health_url = f"{base_url}/health"

    # Fast path — already running
    if _infer_proc is not None and _infer_proc.poll() is None:
        return base_url

    with _infer_lock:
        # Re-check after acquiring lock
        if _infer_proc is not None and _infer_proc.poll() is None:
            return base_url

        logger.info(
            "Starting infer.py HTTP server (this will load the model — "
            "~5-10 min on first call over /mnt/f/)…"
        )
        with _infer_stderr_lock:
            _infer_stderr_lines.clear()

        _infer_proc = subprocess.Popen(
            [
                str(_TRAINING_PYTHON),
                str(_INFER_SCRIPT),
                "--serve",
                "--port", str(_INFER_PORT),
            ],
            cwd=str(_TRAINING_DIR),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )

        _stderr_thread = threading.Thread(
            target=_drain_stderr, args=(_infer_proc,), daemon=True
        )
        _stderr_thread.start()

        deadline = time.monotonic() + _INFER_STARTUP_TIMEOUT
        last_exc: Exception | None = None
        while time.monotonic() < deadline:
            if _infer_proc.poll() is not None:
                with _infer_stderr_lock:
                    stderr = "\n".join(_infer_stderr_lines)
                raise RuntimeError(
                    f"Infer server process exited unexpectedly during startup.\n{stderr}"
                )
            try:
                with urllib.request.urlopen(health_url, timeout=2) as resp:
                    if resp.status == 200:
                        logger.info("Infer server is ready.")
                        return base_url
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
            time.sleep(2)

        with _infer_stderr_lock:
            stderr_tail = "\n".join(_infer_stderr_lines[-40:])
        raise RuntimeError(
            f"Infer server did not become ready within {_INFER_STARTUP_TIMEOUT}s. "
            f"Last error: {last_exc}\n"
            f"Last stderr output:\n{stderr_tail}"
        )


def call_infer_server(digest: str) -> tuple[int, list[float], list[dict]]:
    """Send the digest to the running infer server and return structured results.

    Returns ``(preset, aggregate_probs, section_details)``.
    Each ``section_details`` entry carries: title (=sec_id), probs, chosen,
    target_words, word_count, margin, confidence, weight.
    """
    base_url = ensure_infer_server()
    payload = _json.dumps({"digest": digest, "verbose": True}).encode()
    req = urllib.request.Request(
        f"{base_url}/predict",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    # Inference can take several minutes for large digests.
    with urllib.request.urlopen(req, timeout=600) as resp:
        data = _json.loads(resp.read())
    if "error" in data:
        raise RuntimeError(f"Infer server returned error: {data['error']}")
    preset: int = data["preset"]
    probs: list[float] = data["probs"]
    sections: list[dict] = data.get("sections", [])
    return preset, probs, sections


# ---------------------------------------------------------------------------
# Signal helpers (used by both infer and planner handlers)
# ---------------------------------------------------------------------------

def entropy(probs: list[float]) -> float:
    """Shannon entropy in bits: H = −∑ p·log₂(p+ε)."""
    eps = 1e-12
    return -sum(p * math.log2(p + eps) for p in probs)


def top2(probs: list[float]) -> list[list]:
    """Return [[preset_str, prob], [preset_str, prob]] for the top-2 presets."""
    ranked = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
    return [[f"P{ranked[i][0]}", round(ranked[i][1], 4)] for i in range(2)]


def guidance(preset: int, confidence: float, h: float, floor_applied: bool) -> str:
    """One-sentence synthesis for the client LLM to use as a reasoning seed."""
    parts: list[str] = []

    if h > ENTROPY_THRESHOLD_HIGH:
        parts.append(
            f"RL model is uncertain (H={h:.2f} bits > 1.5) — apply your own judgement."
        )
    elif confidence >= CONFIDENCE_STRONG:
        parts.append(
            f"RL model strongly recommends P{preset} "
            f"({PRESET_NAMES[preset].replace('_', ' ')}, confidence {confidence:.0%})."
        )
    else:
        parts.append(
            f"RL model recommends P{preset} "
            f"({PRESET_NAMES[preset].replace('_', ' ')}, confidence {confidence:.0%})."
        )

    if floor_applied:
        parts.append(
            "Floor correction fired: a technical section needed more exploration "
            "than the aggregate vote suggested."
        )

    return " ".join(parts)
