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
import os
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

# _infer_config.py has zero heavy deps (stdlib only), so it can be imported
# directly into the mcp_server's own venv -- this is how ensure_infer_server()
# knows what infer.py's CURRENT default checkpoint is without needing torch.
import sys as _sys  # noqa: E402
if str(_TRAINING_DIR) not in _sys.path:
    _sys.path.insert(0, str(_TRAINING_DIR))
from _infer_config import DEFAULT_ADAPTER_DIR as _INFER_DEFAULT_ADAPTER_DIR  # noqa: E402

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

# Override which checkpoint the infer server loads without editing infer.py's
# hardcoded _DEFAULT_ADAPTER_DIR -- e.g.
#   RL_INFER_ADAPTER_DIR=/path/to/checkpoints/tasks/run30_.../best uv run ...
_ADAPTER_ENV_VAR = "RL_INFER_ADAPTER_DIR"

_infer_proc: subprocess.Popen | None = None
_infer_lock = threading.Lock()
# Adapter path the CURRENTLY RUNNING subprocess reported via /health at startup
# -- the source of truth ensure_infer_server() compares future requests against
# so a checkpoint change (new --adapter-dir, new RL_INFER_ADAPTER_DIR, or an
# edited _DEFAULT_ADAPTER_DIR) triggers a restart instead of silently reusing
# stale weights (see run13_rl_grok_pipeline_analysis.md A.17 -- this exact bug
# made two "different checkpoint" evals return byte-identical predictions).
_infer_adapter_dir: str | None = None

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


def _query_health(base_url: str, timeout: float = 2.0) -> dict | None:
    try:
        with urllib.request.urlopen(f"{base_url}/health", timeout=timeout) as resp:
            if resp.status == 200:
                return _json.loads(resp.read())
    except Exception:  # noqa: BLE001
        pass
    return None


def _terminate_infer_proc() -> None:
    global _infer_proc, _infer_adapter_dir
    if _infer_proc is not None and _infer_proc.poll() is None:
        logger.info("Stopping stale infer server (adapter changed)…")
        _infer_proc.terminate()
        try:
            _infer_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            _infer_proc.kill()
            _infer_proc.wait(timeout=10)
    _infer_proc = None
    _infer_adapter_dir = None


def ensure_infer_server(adapter_dir: str | None = None) -> str:
    """Start the infer.py HTTP server subprocess if not already running with
    the requested adapter checkpoint.

    ``adapter_dir`` (optional): resolves in this order: the argument, then the
    ``RL_INFER_ADAPTER_DIR`` env var, then ``None`` (infer.py's own hardcoded
    default). If a server is already running with a DIFFERENT adapter than
    requested, it is terminated and restarted -- this is the fix for the bug
    where a long-lived server silently kept serving a stale checkpoint across
    unrelated eval runs (A.17).

    Uses the training venv's Python (which has torch/transformers installed).
    Blocks until the /health endpoint responds or the startup timeout is reached.
    Returns the server base URL (``http://127.0.0.1:<port>``).

    stderr is drained by a background thread to prevent pipe-buffer stalls
    (bitsandbytes / transformers can emit hundreds of KB during model load).
    """
    global _infer_proc, _infer_adapter_dir
    base_url = f"http://127.0.0.1:{_INFER_PORT}"

    # Resolve what SHOULD be running: an explicit override (arg or env var) if
    # given, otherwise infer.py's own current default -- NOT "don't care".
    # Falling back to None here was the bug (2026-08-21): it made "no override
    # given" skip the stale-checkpoint check entirely, so editing infer.py's
    # _DEFAULT_ADAPTER_DIR and restarting a caller that never passes an
    # explicit adapter_dir (e.g. test_grok_planner.py) kept reusing whatever
    # checkpoint the server happened to load first.
    requested = adapter_dir or os.environ.get(_ADAPTER_ENV_VAR) or str(_INFER_DEFAULT_ADAPTER_DIR)
    requested_resolved = str(Path(requested).resolve())

    # Fast path — already running with the requested adapter.
    if _infer_proc is not None and _infer_proc.poll() is None:
        if requested_resolved == _infer_adapter_dir:
            return base_url

    with _infer_lock:
        # Re-check after acquiring lock
        if _infer_proc is not None and _infer_proc.poll() is None:
            if requested_resolved == _infer_adapter_dir:
                return base_url
            logger.warning(
                "Infer server is running adapter '%s' but '%s' was requested -- restarting.",
                _infer_adapter_dir, requested_resolved,
            )
            _terminate_infer_proc()

        logger.info(
            "Starting infer.py HTTP server (this will load the model — "
            "~5-10 min on first call over /mnt/f/)…"
        )
        with _infer_stderr_lock:
            _infer_stderr_lines.clear()

        cmd = [str(_TRAINING_PYTHON), str(_INFER_SCRIPT), "--serve", "--port", str(_INFER_PORT),
               "--adapter-dir", requested]
        _infer_proc = subprocess.Popen(
            cmd,
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
            health = _query_health(base_url)
            if health is not None:
                _infer_adapter_dir = health.get("adapter_dir")
                logger.info("Infer server is ready. Serving adapter: %s", _infer_adapter_dir)
                if _infer_adapter_dir != requested_resolved:
                    logger.warning(
                        "Requested adapter '%s' but server reports '%s' -- "
                        "check infer.py's --adapter-dir handling.",
                        requested_resolved, _infer_adapter_dir,
                    )
                return base_url
            time.sleep(2)

        with _infer_stderr_lock:
            stderr_tail = "\n".join(_infer_stderr_lines[-40:])
        raise RuntimeError(
            f"Infer server did not become ready within {_INFER_STARTUP_TIMEOUT}s. "
            f"Last error: {last_exc}\n"
            f"Last stderr output:\n{stderr_tail}"
        )


def call_infer_server(digest: str, adapter_dir: str | None = None) -> tuple[int, list[float], list[dict]]:
    """Send the digest to the running infer server and return structured results.

    ``adapter_dir``: optional override, see ensure_infer_server(). Most callers
    should leave this None and control the checkpoint via RL_INFER_ADAPTER_DIR.

    Returns ``(preset, aggregate_probs, section_details)``.
    Each ``section_details`` entry carries: title (=sec_id), probs, chosen,
    target_words, word_count, margin, confidence, weight.
    """
    base_url = ensure_infer_server(adapter_dir)
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


# ---------------------------------------------------------------------------
# Cost-sensitive decision rule (empirical, fit from train-set oracle rewards)
# ---------------------------------------------------------------------------
# Cost[c][a] = E[R_w(true class c) - R_w(action a)], fit from the 16 non-forbidden
# train-set article oracles (2026-07-10 backtest — see
# grok_planner_test_results/run13_rl_grok_pipeline_analysis.md Part 2 §9/§13).
# Encodes the reward asymmetry the raw argmax ignores: under-shooting (picking
# too cheap) costs far more than a 1-level over-shoot at the P0/P1 boundary
# (0.147 vs 0.015); the reverse but smaller asymmetry favors P1 over P2 unless
# the vote is fairly confident (P1/P2: over-cost 0.132 vs under-cost 0.077);
# P2/P3 is roughly symmetric (0.080 vs 0.079) so plain argmax is fine there.
_COST_MATRIX: list[list[float]] = [
    # action:    skip     light  standard    deep
    [0.0000, 0.0148, 0.0551, 0.1223],  # true = skip
    [0.1467, 0.0000, 0.1317, 0.1730],  # true = light
    [0.1693, 0.0768, 0.0000, 0.0797],  # true = standard
    [0.0666, 0.0578, 0.0794, 0.0000],  # true = deep
]

#: Never let the rule move more than this many preset levels from the raw
#: argmax. An unconstrained argmin over the full cost matrix can jump 2+
#: levels purely because a cheap preset has uniformly low cost as an action
#: across all true classes — validated on the 2026-07-10 backtest to misfire
#: on a high-entropy, high-preset vote (a 51%-confidence P3 vote was overridden
#: all the way to P1). Restricting to adjacent presets preserved every
#: validated fix while eliminating that failure mode.
_COST_RULE_MAX_STEP: int = 1


def apply_cost_sensitive_rule(raw_preset: int, probs: list[float]) -> int:
    """Adjust the raw argmax preset using the empirical reward-asymmetry cost matrix.

    Computes the minimum-expected-cost action
    ``E[cost | a] = sum_c probs[c] * _COST_MATRIX[c][a]``, restricted to
    candidates within `_COST_RULE_MAX_STEP` of ``raw_preset``.

    Backtest result (2026-07-10, against saved run13_formulaB aggregate
    distributions): TEST exact 7->10 (44%->62%), near 9->6, miss 0->0 (stays
    zero), ordinal MAE 0.562->0.375, reward-regret mean 0.0779->0.0384 (-51%),
    regret max 0.3192->0.1700 (-47%). TRAIN exact 19->20, miss unchanged at 2
    (both pre-existing label-near-tie artifacts, not affected by this rule).
    """
    lo = max(0, raw_preset - _COST_RULE_MAX_STEP)
    hi = min(NUM_PRESETS - 1, raw_preset + _COST_RULE_MAX_STEP)
    candidates = range(lo, hi + 1)
    exp_costs = {
        a: sum(probs[c] * _COST_MATRIX[c][a] for c in range(NUM_PRESETS))
        for a in candidates
    }
    return min(candidates, key=lambda a: exp_costs[a])
