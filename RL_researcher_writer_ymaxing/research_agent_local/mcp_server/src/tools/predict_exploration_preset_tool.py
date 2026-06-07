"""
Meta-reasoner tool: RL-guided exploration preset prediction.

Uses a GRPO-trained Qwen3-4B + LoRA adapter to analyse the research
digest and produce structured section-level signals that help the client
LLM (Grok) decide how many rounds of exploration to run and in what order.

If research_digest.md does not yet exist in the research directory, the
tool generates it on-the-fly via the v2 digest pipeline (generate_digests.py,
run in the training venv) before running RL inference.

Signal semantics
----------------
preset (0–3)
    The RL model's recommended exploration strategy:
      0 – skip     No exploration (existing coverage is sufficient)
      1 – light    1 round, balanced (50% depth / 50% breadth)
      2 – standard 2 rounds: depth → breadth
      3 – deep     3 rounds: depth → breadth → depth

confidence
    Probability mass on the chosen preset (0.0–1.0).
    • ≥0.70 → strong signal, model is decisive.
    • 0.40–0.70 → moderate; consider section breakdown.
    • <0.40 → uncertain; apply your own judgement.

entropy (bits, base-2)
    Spread of the probability distribution over presets 0–3.
    Computed as H = −∑ p·log₂(p+ε) over the aggregated preset probs.
    • H < 0.5 → very confident (nearly all mass on one preset).
    • 0.5–1.5 → moderate confidence.
    • H > 1.5 → model is uncertain; override freely.

floor_correction_applied
    True when the max-preset floor heuristic fired: the aggregate vote was
    P0 or P1 (skip/light), but at least one individual section predicted
    standard (P2) or deep (P3). The floor prevents intro-section dominance
    from masking technical sections that need more exploration.

top2 (per section)
    The two highest-probability presets for each section and their probabilities.
    A large gap between rank-1 and rank-2 (e.g. [P3, 0.81], [P2, 0.11]) means
    the model is highly confident for that section.
    A small gap (e.g. [P2, 0.45], [P3, 0.40]) means the section is ambiguous.

guidance
    One-sentence synthesis for the client LLM to use as a reasoning seed.
    When entropy is high (>1.5) the guidance explicitly says so.

Model architecture note
-----------------------
The RL model was trained with GRPO (Group Relative Policy Optimisation) on
section-level inference tasks across 4 AI-course articles. It predicts the
per-section preset using a section-level system prompt, then aggregates by
word-count-weighted confidence-gated probability vote. A max-preset floor is
applied when the aggregate vote is skip or light but at least one section
predicts standard or deep, preventing short intro sections from masking
technical depth requirements.
"""

from __future__ import annotations

import asyncio
import logging
import re
import subprocess
from pathlib import Path
from typing import Any, Dict

from ..config.settings import settings
from ..app.preset_infer_handler import (
    PRESET_NAMES,
    call_infer_server,
    entropy,
    guidance,
)
from ..app.preset_planner_handler import (
    _INCLUDE_GUIDELINE_IN_PLANNER,
    build_article_evidence,
    call_grok_planner,
    call_grok_planner_standalone,
    fallback_aggregator,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths (tools/ is 3 levels below research_agent_local/, same as app/)
# ---------------------------------------------------------------------------
_TRAINING_DIR = Path(__file__).resolve().parents[3] / "training"
_TRAINING_PYTHON = _TRAINING_DIR / ".venv" / "bin" / "python"
_GENERATE_DIGESTS_SCRIPT = _TRAINING_DIR / "generate_digests.py"
_DIGEST_GEN_TIMEOUT = 1800  # seconds — COMPRESS+GENERATE over many sources


# ---------------------------------------------------------------------------
# On-the-fly digest generation (delegates to generate_digests.py v2 pipeline)
# ---------------------------------------------------------------------------

def _generate_digest_via_subprocess(research_dir: Path) -> None:
    """Generate research_digest.md for a live research dir via generate_digests.py.

    Runs the full v2 pipeline in the training venv, which has the pipeline deps
    and reads XAI_API_KEY from mcp_client/.env. Writes research_digest.md,
    section_oracle.json, and guideline_features.json into ``research_dir``.

    Raises RuntimeError on non-zero exit.
    """
    proc = subprocess.run(
        [
            str(_TRAINING_PYTHON),
            str(_GENERATE_DIGESTS_SCRIPT),
            "--research-dir", str(research_dir),
        ],
        cwd=str(_TRAINING_DIR),
        capture_output=True,
        text=True,
        timeout=_DIGEST_GEN_TIMEOUT,
    )
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip()[-2000:]
        raise RuntimeError(
            f"Digest generation failed (exit {proc.returncode}):\n{tail}"
        )



# ---------------------------------------------------------------------------
# Gap-profile extraction
# ---------------------------------------------------------------------------

def _extract_gap_profile(digest: str) -> str:
    """Extract the coverage gap profile section from the exploitation digest.

    Prefers the v2 XML <gap_profile> block. Falls back to the legacy markdown
    "## 3. Overall Gap Profile" section. Returns "" if neither is present.
    """
    m = re.search(r"<gap_profile>.*?</gap_profile>", digest, re.DOTALL)
    if m:
        return m.group(0).strip()

    marker = "## 3. Overall Gap Profile"
    idx = digest.find(marker)
    if idx == -1:
        return ""
    rest = digest[idx:]
    next_heading = rest.find("\n## ", len(marker))
    if next_heading != -1:
        return rest[:next_heading].strip()
    return rest.strip()



async def predict_exploration_preset_tool(research_directory: str, grok_only: bool = False, rl_only: bool = False) -> Dict[str, Any]:
    """
    Predict the optimal exploration preset for an article using the trained RL model.

    Reads (or auto-generates) research_digest.md from the research directory,
    runs per-section inference through the GRPO-trained Qwen3-4B + LoRA model,
    and returns structured signals to help the client LLM decide how many rounds
    of exploration to run and in what order.

    If research_digest.md does not yet exist in the research directory, the tool
    generates it on-the-fly via the v2 digest pipeline (generate_digests.py, run
    in the training venv) and writes research_digest.md, section_oracle.json, and
    guideline_features.json before running inference. This requires the training
    venv and XAI_API_KEY (in mcp_client/.env) and the .research/ subfolder to
    contain the exploitation sources collected during step 3.

    The tool performs two-stage inference:
      Stage 1 (RL model): per-section preset prediction via word-count-weighted
                          probability vote → aggregate recommendation.
      Stage 2 (client):   the client uses the returned signals to make the final
                          decision, overriding the RL model when entropy is high
                          or section signals are contradictory.

    Args:
        research_directory: Path to the research directory. Must contain either:
          - research_digest.md (pre-existing, used directly), or
          - article_guideline.md + .research/ subfolder (digest auto-generated).
        grok_only: When True, skip the RL inference stage entirely and call Grok 4.2
          with only the article guideline + coverage gap profile (no section-level
          RL signals). Use this for the Grok-alone baseline to measure the RL
          model's marginal contribution. rl_recommendation will be None in the result.
        rl_only: When True, run the RL inference stage but SKIP the Grok 4.2 planner
          entirely. grok_recommendation will be None in the result. Use this for the
          RL-only baseline and the RL + deterministic-policy-guard ablation (the
          caller applies the forbidden->skip / required->>=light guards itself).

    Returns:
        Dict with keys:
          status               – "success" or "error"
          digest_generated     – True if the digest was generated on-the-fly
          rl_recommendation    – aggregate preset, name, confidence, entropy,
                                 floor_correction_applied. None when grok_only=True.
          section_signals      – per-section list of preset, name, top2 probs.
                                 Empty list when grok_only=True.
          guidance             – one-sentence synthesis for the client LLM.
                                 Empty string when grok_only=True.
          article_guideline    – full text of article_guideline.md
          digest_gap_profile   – "## 3. Overall Gap Profile" section from the digest
          grok_recommendation  – Grok 4.2's planning decision. When grok_only=False:
                                 preset, name, reasoning, override, override_reason.
                                 When grok_only=True: preset, name, reasoning (no
                                 override fields — RL had no input to override).
                                 None if XAI_API_KEY is unset or the call fails.
          message              – human-readable summary
    """
    research_path = Path(research_directory)
    digest_path = research_path / "research_digest.md"

    if not research_path.exists():
        return {
            "status": "error",
            "message": f"Research directory not found: {research_directory}",
        }

    digest_generated = False

    if not digest_path.exists():
        logger.info(f"research_digest.md not found — generating on-the-fly for {research_directory}")
        try:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(
                None, _generate_digest_via_subprocess, research_path
            )
            digest = digest_path.read_text(encoding="utf-8")
            digest_generated = True
            logger.info(f"Digest written to {digest_path}")
        except Exception as exc:
            logger.exception("On-the-fly digest generation failed")
            return {"status": "error", "message": f"Digest generation failed: {exc}"}
    else:
        try:
            digest = digest_path.read_text(encoding="utf-8")
        except Exception as exc:
            return {"status": "error", "message": f"Failed to read digest: {exc}"}

    guideline_path = research_path / "article_guideline.md"
    article_guideline = (
        guideline_path.read_text(encoding="utf-8", errors="replace")
        if guideline_path.exists()
        else ""
    )
    digest_gap_profile = _extract_gap_profile(digest)

    # -----------------------------------------------------------------------
    # Branch: Grok-alone baseline (no RL inference)
    # -----------------------------------------------------------------------
    if grok_only:
        # Digest-only evidence packet: same per-section gaps + economics the full
        # pipeline sees, but with no trained-scorer signal (rl_aggregate=None and
        # empty per-section RL fields). Isolates the section model's contribution.
        evidence = build_article_evidence(digest)
        grok_recommendation: dict | None = None
        if settings.xai_api_key is not None:
            try:
                grok_recommendation = await call_grok_planner_standalone(
                    api_key=settings.xai_api_key.get_secret_value(),
                    base_url="https://api.x.ai/v1",
                    evidence=evidence,
                    article_guideline=(
                        article_guideline if _INCLUDE_GUIDELINE_IN_PLANNER else ""
                    ),
                )
                if grok_recommendation:
                    logger.info("Grok standalone chose P%d", grok_recommendation["preset"])
            except Exception:
                logger.warning("Grok standalone planner call failed.")
        else:
            logger.warning("XAI_API_KEY not set; cannot run Grok standalone planner.")

        grok_preset = grok_recommendation["preset"] if grok_recommendation else "?"
        return {
            "status": "success",
            "digest_generated": digest_generated,
            "rl_recommendation": None,
            "section_signals": [],
            "guidance": "",
            "grok_recommendation": grok_recommendation,
            "article_evidence": evidence,
            "article_guideline": article_guideline,
            "digest_gap_profile": digest_gap_profile,
            "message": (
                f"Grok standalone (no RL) chose preset P{grok_preset}."
                if grok_recommendation
                else "Grok standalone call failed or XAI_API_KEY not set."
            ),
        }

    # -----------------------------------------------------------------------
    # Standard pipeline: RL inference → article evidence packet → Grok 4.2
    # -----------------------------------------------------------------------
    try:
        loop = asyncio.get_running_loop()
        preset, agg_probs, section_details = await loop.run_in_executor(
            None, call_infer_server, digest
        )
    except Exception as exc:
        logger.exception("RL inference failed")
        return {"status": "error", "message": f"RL inference failed: {exc}"}

    confidence = round(agg_probs[preset], 4)
    h = round(entropy(agg_probs), 4)
    section_floor = max((d["chosen"] for d in section_details), default=preset)
    floor_applied = preset <= 1 and section_floor >= 2 and h <= 1.5
    guidance_str = guidance(preset, confidence, h, floor_applied)

    # Build the structured, leakage-free evidence packet (Stage 1 → Stage 2).
    evidence = build_article_evidence(digest, preset, agg_probs, section_details)

    # Compact per-section view for the result payload (backward-compatible shape).
    section_signals = [
        {
            "title": s["title"],
            "label": s["label"],
            "preset": s["chosen_preset"],
            "name": PRESET_NAMES.get(s["chosen_preset"], "?"),
            "top2": s["top2"],
        }
        for s in evidence["section_signals"]
    ]

    # Stage 2: Grok 4.2 planner. Always produce an article-level decision —
    # fall back to the deterministic aggregator if Grok is unavailable/errors.
    if rl_only:
        # RL-only baseline / policy-guard ablation: skip the Grok stage entirely.
        grok_recommendation = None
        logger.info("rl_only=True; skipping Grok planner stage.")
    elif settings.xai_api_key is not None:
        try:
            grok_recommendation = await call_grok_planner(
                api_key=settings.xai_api_key.get_secret_value(),
                base_url="https://api.x.ai/v1",
                evidence=evidence,
                article_guideline=(
                    article_guideline if _INCLUDE_GUIDELINE_IN_PLANNER else ""
                ),
            )
            logger.info(
                "Grok planner chose P%d (override=%s)",
                grok_recommendation["preset"],
                grok_recommendation["override"],
            )
        except Exception:
            logger.warning("Grok planner call failed; using deterministic fallback.")
            grok_recommendation = fallback_aggregator(evidence)
    else:
        logger.warning("XAI_API_KEY not set; using deterministic fallback aggregator.")
        grok_recommendation = fallback_aggregator(evidence)

    return {
        "status": "success",
        "digest_generated": digest_generated,
        "rl_recommendation": {
            "preset": preset,
            "name": PRESET_NAMES[preset],
            "confidence": confidence,
            "entropy_bits": h,
            "floor_correction_applied": floor_applied,
        },
        "section_signals": section_signals,
        "guidance": guidance_str,
        "grok_recommendation": grok_recommendation,
        "article_evidence": evidence,
        "article_guideline": article_guideline,
        "digest_gap_profile": digest_gap_profile,
        "message": (
            f"RL model recommends preset P{preset} "
            f"({PRESET_NAMES[preset]}) "
            f"with {confidence:.0%} confidence across {len(section_signals)} sections. "
            f"Entropy: {h:.2f} bits."
        ),
    }
