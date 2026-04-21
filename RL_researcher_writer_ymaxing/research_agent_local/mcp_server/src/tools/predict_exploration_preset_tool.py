"""
Meta-reasoner tool: RL-guided exploration preset prediction.

Uses a GRPO-trained Qwen3-4B + LoRA adapter to analyse the exploitation
digest and produce structured section-level signals that help the client
LLM (Grok) decide how many rounds of exploration to run and in what order.

If exploitation_digest.md does not yet exist in the research directory, the
tool generates it on-the-fly via a 4-stage pipeline (COLLECT → COMPRESS →
ASSEMBLE → GENERATE) before running RL inference.

Signal semantics
----------------
preset (0–5)
    The RL model's recommended exploration strategy:
      0 – No exploration (baseline)
      1 – 1 round, balanced
      2 – 2 rounds, balanced then depth
      3 – 2 rounds, depth then breadth
      4 – 3 rounds, balanced then depth then breadth
      5 – 3 rounds, depth then breadth then depth

confidence
    Probability mass on the chosen preset (0.0–1.0).
    • ≥0.70 → strong signal, model is decisive.
    • 0.40–0.70 → moderate; consider section breakdown.
    • <0.40 → uncertain; apply your own judgement.

entropy (bits, base-2)
    Spread of the probability distribution over presets 0–5.
    Computed as H = −∑ p·log₂(p+ε) over the aggregated preset probs.
    • H < 0.5 → very confident (nearly all mass on one preset).
    • 0.5–1.5 → moderate confidence.
    • H > 1.5 → model is uncertain; override freely.

floor_correction_applied
    True when the max-preset floor heuristic fired: the aggregate vote was
    P0–P2, but at least one individual section predicted a higher preset.
    The floor prevents intro-section dominance from masking deep technical
    sections that need more exploration.

top2 (per section)
    The two highest-probability presets for each section and their probabilities.
    A large gap between rank-1 and rank-2 (e.g. [P3, 0.81], [P2, 0.11]) means
    the model is highly confident for that section.
    A small gap (e.g. [P3, 0.35], [P4, 0.32]) means the section is ambiguous.

guidance
    One-sentence synthesis for the client LLM to use as a reasoning seed.
    When entropy is high (>1.5) the guidance explicitly says so.

Model architecture note
-----------------------
The RL model was trained with GRPO (Group Relative Policy Optimisation) on
section-level inference tasks across 4 AI-course articles. It predicts the
per-section preset using a section-level system prompt, then aggregates by
word-count-weighted probability vote. A max-preset floor is applied when the
aggregate vote is ≤P2 to prevent under-exploration caused by short intro sections
dominating the vote.
"""

from __future__ import annotations

import asyncio
import logging
import math
import threading
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Lazy singleton — model loads once on first tool call (~3 min on GPU)
# ---------------------------------------------------------------------------
_selector = None
_selector_lock = threading.Lock()

# parents[3] = research_agent_local/  (tools is 3 levels below: mcp_server/src/tools/)
_TRAINING_DIR = Path(__file__).resolve().parents[3] / "training"
_PRESET_NAMES = {
    0: "no_exploration",
    1: "1_round_balanced",
    2: "2_rounds_balanced_then_depth",
    3: "2_rounds_depth_then_breadth",
    4: "3_rounds_balanced_depth_breadth",
    5: "3_rounds_depth_breadth_depth",
}
_NUM_PRESETS = 6
_ENTROPY_THRESHOLD_HIGH = 1.5
_ENTROPY_THRESHOLD_LOW = 0.5
_CONFIDENCE_STRONG = 0.70
_CONFIDENCE_MODERATE = 0.40


def _get_selector():
    global _selector
    if _selector is None:
        with _selector_lock:
            if _selector is None:
                import sys
                sys.path.insert(0, str(_TRAINING_DIR))
                from infer import ExplorationStrategySelector  # noqa: PLC0415
                logger.info("Loading RL model (first call — ~3 min on GPU)…")
                _selector = ExplorationStrategySelector()
                logger.info("RL model loaded and cached.")
    return _selector


def _entropy(probs: list[float]) -> float:
    """Shannon entropy in bits: H = -∑ p·log₂(p+ε)."""
    eps = 1e-12
    return -sum(p * math.log2(p + eps) for p in probs)


def _top2(probs: list[float]) -> list[list]:
    """Return [[preset_str, prob], [preset_str, prob]] for the top-2 presets."""
    ranked = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
    return [[f"P{ranked[i][0]}", round(ranked[i][1], 4)] for i in range(2)]


def _guidance(preset: int, confidence: float, entropy: float, floor_applied: bool) -> str:
    parts: list[str] = []

    if entropy > _ENTROPY_THRESHOLD_HIGH:
        parts.append(
            f"RL model is uncertain (H={entropy:.2f} bits > 1.5) — apply your own judgement."
        )
    elif confidence >= _CONFIDENCE_STRONG:
        parts.append(
            f"RL model strongly recommends P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}, confidence {confidence:.0%})."
        )
    else:
        parts.append(
            f"RL model recommends P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}, confidence {confidence:.0%})."
        )

    if floor_applied:
        parts.append(
            "Floor correction fired: a technical section needed more exploration "
            "than the aggregate vote suggested."
        )

    return " ".join(parts)


async def predict_exploration_preset_tool(research_directory: str) -> Dict[str, Any]:
    """
    Predict the optimal exploration preset for an article using the trained RL model.

    Reads the exploitation_digest.md from the research directory, runs per-section
    inference through the GRPO-trained Qwen3-4B + LoRA model, and returns structured
    signals to help the client LLM decide how many rounds of exploration to run.

    The tool performs two-stage inference:
      Stage 1 (RL model): per-section preset prediction via word-count-weighted
                          probability vote → aggregate recommendation.
      Stage 2 (client):   the client uses the returned signals to make the final
                          decision, overriding the RL model when entropy is high
                          or section signals are contradictory.

    Args:
        research_directory: Path to the research directory containing
                            exploitation_digest.md at its root.

    Returns:
        Dict with keys:
          status          – "success" or "error"
          rl_recommendation – aggregate preset, name, confidence, entropy,
                              floor_correction_applied
          section_signals – per-section list of preset, name, top2 probs
          guidance        – one-sentence synthesis for the client LLM
          message         – human-readable summary
    """
    research_path = Path(research_directory)
    digest_path = research_path / "exploitation_digest.md"

    if not research_path.exists():
        return {
            "status": "error",
            "message": f"Research directory not found: {research_directory}",
        }
    if not digest_path.exists():
        return {
            "status": "error",
            "message": (
                f"exploitation_digest.md not found in {research_directory}. "
                "Run the exploitation digest generation step first."
            ),
        }

    try:
        digest = digest_path.read_text(encoding="utf-8")
    except Exception as exc:
        return {"status": "error", "message": f"Failed to read digest: {exc}"}

    try:
        selector = _get_selector()
    except Exception as exc:
        logger.exception("Failed to load RL model")
        return {"status": "error", "message": f"RL model failed to load: {exc}"}

    try:
        preset, agg_probs, section_details, meta = selector.predict_article_verbose(digest)
    except Exception as exc:
        logger.exception("Inference error")
        return {"status": "error", "message": f"Inference failed: {exc}"}

    # --- Derived signals ---
    confidence = round(agg_probs[preset], 4)
    h = round(_entropy(agg_probs), 4)
    section_vote = meta.get("section_vote", preset)
    section_floor = meta.get("section_floor", 0)
    floor_applied = section_vote <= 2 and section_floor > section_vote

    section_signals = []
    for d in section_details:
        section_signals.append({
            "title": d["title"],
            "preset": d["chosen"],
            "name": _PRESET_NAMES[d["chosen"]].replace("_", " "),
            "top2": _top2(d["probs"]),
        })

    guidance_str = _guidance(preset, confidence, h, floor_applied)

    result = {
        "status": "success",
        "rl_recommendation": {
            "preset": preset,
            "name": _PRESET_NAMES[preset].replace("_", " "),
            "confidence": confidence,
            "entropy_bits": h,
            "floor_correction_applied": floor_applied,
        },
        "section_signals": section_signals,
        "guidance": guidance_str,
        "message": (
            f"RL model recommends preset P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}) "
            f"with {confidence:.0%} confidence across {len(section_signals)} sections. "
            f"Entropy: {h:.2f} bits."
        ),
    }
    return result
