"""
Meta-reasoner tool: RL-guided exploration preset prediction (PRODUCTION pipeline).

Uses a GRPO-trained Qwen3-4B + LoRA adapter to analyse the research digest and produce
structured section-level signals, then applies a deterministic policy guard (external-evidence
policy: forbidden/required/capped). This is the production pipeline: RL model + deterministic
guard only — no LLM-planner stage, no grok_only/rl_only ablation switches. The only sanctioned
way to deviate from its recommendation is an explicit user-directed override (see
research_instructions_prompt.py step 3.4) or the guard's own policy clamp.

For the evaluation/ablation variant (grok_only, rl_only, the disabled-by-default LLM-planner
stage) used by evaluation/test_grok_planner.py to measure the RL model's marginal
contribution, see evaluation/predict_exploration_preset_eval.py. That variant is intentionally
NOT part of this production pipeline and is not exposed on the production MCP server.

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
    • <0.40 → uncertain.

entropy (bits, base-2)
    Spread of the probability distribution over presets 0–3.
    Computed as H = −∑ p·log₂(p+ε) over the aggregated preset probs.
    • H < 0.5 → very confident (nearly all mass on one preset).
    • 0.5–1.5 → moderate confidence.
    • H > 1.5 → model is uncertain. This is informational only, not a basis for the client LLM to
      self-override; only an explicit user-directed override or a policy guard may change the plan.

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

import logging
from pathlib import Path
from typing import Any, Dict

from ..app.preset_planner_handler import (
    assemble_result,
    extract_gap_profile,
    fallback_aggregator,
    load_or_generate_digest,
    run_rl_stage,
)

logger = logging.getLogger(__name__)


async def predict_exploration_preset_tool(research_directory: str) -> Dict[str, Any]:
    """
    Predict the exploration preset for an article: RL model + deterministic policy guard only.

    Reads (or auto-generates) research_digest.md from the research directory,
    runs per-section inference through the GRPO-trained Qwen3-4B + LoRA model,
    and returns a structured two-stage planning decision.

    If research_digest.md does not yet exist in the research directory, the tool
    generates it on-the-fly via the v2 digest pipeline (generate_digests.py, run
    in the training venv) and writes research_digest.md, digest_section_placeholder.json, and
    guideline_features.json before running inference. This requires the training
    venv and XAI_API_KEY (in mcp_client/.env) and the .research/ subfolder to
    contain the exploitation sources collected during step 3.

    The tool performs two-stage inference:
      Stage 1 (RL model): per-section preset prediction via word-count-weighted
                          probability vote → aggregate recommendation (P0–P3).
      Stage 2 (deterministic policy guard, no LLM call): clamps the RL pick to the
                          article's external-evidence policy (forbidden → P0,
                          required → ≥ P1, capped → ≤ P1). The RL pick is
                          authoritative except where this guard fires — there is no
                          LLM-planner stage in this tool at all (see module docstring).

    Args:
        research_directory: Path to the research directory. Must contain either:
          - research_digest.md (pre-existing, used directly), or
          - article_guideline.md + .research/ subfolder (digest auto-generated).

    Returns:
        Dict with keys:
          status               – "success" or "error"
          digest_generated     – True if the digest was generated on-the-fly
          rl_recommendation    – aggregate preset (0–3), name, confidence, entropy_bits,
                                 floor_correction_applied, agg_probs (the full 4-vector
                                 [P0,P1,P2,P3] aggregate probability distribution, for
                                 offline decision-rule analysis), raw_argmax_preset (the
                                 preset before the cost-sensitive rule adjustment),
                                 cost_rule_adjusted (True if the rule moved the pick
                                 away from raw argmax).
          section_signals      – per-section list of preset, name, top2 probs.
          guidance             – one-sentence synthesis from the RL stage.
          article_guideline    – full text of article_guideline.md
          digest_gap_profile   – gap profile section from the digest
          llm_recommendation   – the FINAL authoritative decision (the field name is a
                                 historical artifact; no LLM is involved) — the RL pick
                                 clamped only by the deterministic policy guard: preset
                                 (0–3), name, reasoning, override, override_reason,
                                 decision_drivers, risk_flags.
          message              – human-readable summary
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

    try:
        rl = await run_rl_stage(digest)
    except Exception as exc:
        logger.exception("RL inference failed")
        return {"status": "error", "message": f"RL inference failed: {exc}"}

    llm_recommendation = fallback_aggregator(rl["evidence"])

    return assemble_result(digest_generated, rl, llm_recommendation, article_guideline, digest_gap_profile)
