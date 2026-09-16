"""
Evaluation/ablation variant of the exploration-preset predictor.

NOT part of the production MCP server — lives outside mcp_server/ so production and
evaluation code stay in strictly separate directories, and is used exclusively by
evaluation/test_planner.py to measure the RL model's marginal contribution and to
regression-test the (disabled-by-default) LLM-planner stage against the deterministic policy
guard. Adds the grok_only/rl_only ablation switches and the LLM-planner call that
mcp_server/src/tools/predict_exploration_preset_tool.py (the production tool) intentionally
does not have.

Real clients — including this repo's own interactive mcp_client and any third-party MCP host
(Claude Code, Cursor, etc.) — must use the production predict_exploration_preset MCP tool
instead: RL model + deterministic policy guard only, or an explicit user-directed override.
See mcp_server/src/prompts/research_instructions_prompt.py.

This module imports the production mcp_server's ``src.app`` handlers directly (via a
sys.path insertion of the mcp_server/ directory, mirroring how those handlers themselves
cross-import rl_inference_service/_digest_parse.py) rather than duplicating their logic, so evaluation
always tracks the exact production Stage-1 pipeline. Run with the mcp_server venv, e.g.:

    uv run --project mcp_server python evaluation/test_planner.py
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Cross-import the production mcp_server handlers (mcp_server/ on sys.path so
# ``src`` resolves the same way it does when the server itself runs via
# `uv run --directory mcp_server run python -m src.server`).
# ---------------------------------------------------------------------------
_EVAL_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _EVAL_DIR.parent  # research_agent_local/
_MCP_SERVER_DIR = _AGENT_DIR / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from src.app.preset_planner_handler import (  # noqa: E402
    assemble_result,
    build_article_evidence,
    extract_gap_profile,
    fallback_aggregator,
    load_or_generate_digest,
    run_rl_stage,
)
from preset_planner_handler_eval import (
    _INCLUDE_GUIDELINE_IN_PLANNER,
    call_grok_planner,
    call_grok_planner_standalone,
)

# ---------------------------------------------------------------------------
# XAI API key (same mcp_client/.env the rest of the pipeline reads it from —
# see training/audit_semantic_signals.py for the same convention).
# ---------------------------------------------------------------------------
_MCP_CLIENT_ENV = _AGENT_DIR / "mcp_client" / ".env"


def _read_api_key_from_env_file(var_name: str, env_path: Path) -> str | None:
    """Minimal .env parser (no python-dotenv dependency) -- extracts one
    variable's value and never logs/echoes it."""
    if not env_path.exists():
        return None
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        if key.strip() == var_name:
            return value.strip().strip('"').strip("'")
    return None


def _resolve_xai_api_key() -> str | None:
    return os.environ.get("XAI_API_KEY") or _read_api_key_from_env_file("XAI_API_KEY", _MCP_CLIENT_ENV)


# Skip the LLM-planner call by default (measured evidence in
# grok_planner_test_results/run13_rl_grok_pipeline_analysis.md A.17-A.17.9 shows it adds no
# value over RL+guards on the current checkpoint). Set PRESET_PLANNER_SKIP_LLM=false to
# re-enable it for a future re-evaluation.
_SKIP_LLM_DEFAULT = os.environ.get("PRESET_PLANNER_SKIP_LLM", "true").strip().lower() not in (
    "false", "0", "no",
)


async def predict_exploration_preset_eval(
    research_directory: str,
    grok_only: bool = False,
    rl_only: bool = False,
    skip_llm: bool = _SKIP_LLM_DEFAULT,
) -> Dict[str, Any]:
    """
    Predict the exploration preset for an article, with evaluation/ablation switches.

    Same Stage 1 (RL model) as the production predict_exploration_preset tool, but
    additionally supports:
      - grok_only=True: skip RL inference entirely and call the LLM planner (currently Grok 4.2)
        from the article guideline + coverage gap profile alone, to measure the RL model's
        marginal contribution.
      - rl_only=True: run RL inference but skip the LLM-planner/guard stage entirely, returning
        the raw RL recommendation with llm_recommendation=None, for the caller to apply its own
        guard logic (as test_grok_planner.py's rl_guards_only mode does).
      - Otherwise (both False): mirrors the historical combined RL+LLM-planner pipeline, gated by
        ``skip_llm`` (default True — deterministic fallback_aggregator; pass False, or set
        PRESET_PLANNER_SKIP_LLM=false, to re-enable the LLM-planner call for a future
        re-evaluation).

    Args:
        research_directory: Path to the research directory (see predict_exploration_preset_tool.py).
        grok_only: When True, skip RL inference; LLM-alone baseline. rl_recommendation is None.
        rl_only: When True, skip the LLM-planner/guard stage; llm_recommendation is None.
        skip_llm: When True (default), use the deterministic fallback_aggregator instead of a
                  real LLM-planner call. Ignored when grok_only or rl_only is True.

    Returns:
        Same shape as the production predict_exploration_preset tool's return dict.
    """
    research_path = Path(research_directory)
    if not research_path.exists():
        return {
            "status": "error",
            "message": f"Research directory not found: {research_directory}",
        }

    try:
        digest, digest_generated = await load_or_generate_digest(research_path)
    except Exception as exc:
        logger.exception("Digest load/generation failed")
        return {"status": "error", "message": f"Digest generation failed: {exc}"}

    guideline_path = research_path / "article_guideline.md"
    article_guideline = (
        guideline_path.read_text(encoding="utf-8", errors="replace")
        if guideline_path.exists()
        else ""
    )
    digest_gap_profile = extract_gap_profile(digest)

    xai_api_key = _resolve_xai_api_key()

    # -----------------------------------------------------------------------
    # Branch: LLM-alone baseline (no RL inference; currently Grok 4.2)
    # -----------------------------------------------------------------------
    if grok_only:
        # Digest-only evidence packet: same per-section gaps + economics the full
        # pipeline sees, but with no trained-scorer signal (rl_aggregate=None and
        # empty per-section RL fields). Isolates the section model's contribution.
        evidence = build_article_evidence(digest)
        llm_recommendation: dict | None = None
        if xai_api_key is not None:
            try:
                llm_recommendation = await call_grok_planner_standalone(
                    api_key=xai_api_key,
                    base_url="https://api.x.ai/v1",
                    evidence=evidence,
                    article_guideline=(
                        article_guideline if _INCLUDE_GUIDELINE_IN_PLANNER else ""
                    ),
                )
                if llm_recommendation:
                    logger.info("LLM standalone chose P%d", llm_recommendation["preset"])
            except Exception:
                logger.warning("LLM standalone planner call failed.")
        else:
            logger.warning("XAI_API_KEY not set; cannot run LLM standalone planner.")

        llm_preset = llm_recommendation["preset"] if llm_recommendation else "?"
        return {
            "status": "success",
            "digest_generated": digest_generated,
            "rl_recommendation": None,
            "section_signals": [],
            "guidance": "",
            "llm_recommendation": llm_recommendation,
            "article_evidence": evidence,
            "article_guideline": article_guideline,
            "digest_gap_profile": digest_gap_profile,
            "message": (
                f"LLM standalone (no RL) chose preset P{llm_preset}."
                if llm_recommendation
                else "LLM standalone call failed or XAI_API_KEY not set."
            ),
        }

    try:
        rl = await run_rl_stage(digest)
    except Exception as exc:
        logger.exception("RL inference failed")
        return {"status": "error", "message": f"RL inference failed: {exc}"}

    if rl_only:
        # RL-only baseline / policy-guard ablation: skip the LLM planner stage entirely.
        llm_recommendation = None
        logger.info("rl_only=True; skipping LLM planner stage.")
    elif skip_llm:
        logger.info("skip_llm=True; using deterministic fallback aggregator.")
        llm_recommendation = fallback_aggregator(rl["evidence"])
    elif xai_api_key is not None:
        try:
            llm_recommendation = await call_grok_planner(
                api_key=xai_api_key,
                base_url="https://api.x.ai/v1",
                evidence=rl["evidence"],
                article_guideline=(
                    article_guideline if _INCLUDE_GUIDELINE_IN_PLANNER else ""
                ),
            )
            logger.info(
                "LLM planner chose P%d (override=%s)",
                llm_recommendation["preset"],
                llm_recommendation["override"],
            )
        except Exception:
            logger.warning("LLM planner call failed; using deterministic fallback.")
            llm_recommendation = fallback_aggregator(rl["evidence"])
    else:
        logger.warning("XAI_API_KEY not set; using deterministic fallback aggregator.")
        llm_recommendation = fallback_aggregator(rl["evidence"])

    return assemble_result(digest_generated, rl, llm_recommendation, article_guideline, digest_gap_profile)
