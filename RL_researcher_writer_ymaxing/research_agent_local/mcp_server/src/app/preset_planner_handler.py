"""
Article-evidence builder and production-pipeline glue for the exploration-preset
tool (predict_exploration_preset_tool.py): RL model + deterministic policy guard
only, no LLM call anywhere in this module.

The eval-only LLM-planner path (render_evidence_brief, the policy/escalation guards,
the planner prompts, and call_grok_planner/call_grok_planner_standalone) lives
entirely in evaluation/preset_planner_handler_eval.py, used by
evaluation/predict_exploration_preset_eval.py and evaluation/test_grok_planner.py.
That eval module cross-imports build_article_evidence/fallback_aggregator FROM this
file, but nothing in this file imports or calls anything eval-only.
"""

from __future__ import annotations

import asyncio
import logging
import re
import subprocess
import sys
from pathlib import Path

from .preset_infer_handler import (
    PRESET_NAMES,
    NUM_PRESETS,
    apply_cost_sensitive_rule,
    call_infer_server,
    entropy,
    guidance,
    top2,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# _digest_parse — stdlib-only, lives in training/ (single source of truth).
# parents[3] = research_agent_local/ for files in mcp_server/src/app/
# ---------------------------------------------------------------------------
_TRAINING_DIR = Path(__file__).resolve().parents[3] / "training"
if str(_TRAINING_DIR) not in sys.path:
    sys.path.insert(0, str(_TRAINING_DIR))
import _digest_parse  # noqa: E402  # type: ignore[import-not-found]

_GENERATE_DIGESTS_SCRIPT = _TRAINING_DIR / "generate_digests.py"
_TRAINING_PYTHON = _TRAINING_DIR / ".venv" / "bin" / "python"
_DIGEST_GEN_TIMEOUT = 1800  # seconds — COMPRESS+GENERATE over many sources


def _generate_digest_via_subprocess(research_dir: Path) -> None:
    """Generate research_digest.md for a live research dir via generate_digests.py.

    Runs the full v2 pipeline in the training venv, which has the pipeline deps
    and reads XAI_API_KEY from mcp_client/.env. Writes research_digest.md,
    digest_section_placeholder.json, and guideline_features.json into ``research_dir``.

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


async def load_or_generate_digest(research_path: Path) -> tuple[str, bool]:
    """Read research_digest.md, generating it on-the-fly via the v2 pipeline if absent.

    Returns (digest_text, digest_generated). Raises on any failure (generation or read).
    Used by the production predict_exploration_preset_tool.py.
    """
    digest_path = research_path / "research_digest.md"
    if not digest_path.exists():
        logger.info(f"research_digest.md not found — generating on-the-fly for {research_path}")
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, _generate_digest_via_subprocess, research_path)
        digest = digest_path.read_text(encoding="utf-8")
        logger.info(f"Digest written to {digest_path}")
        return digest, True
    return digest_path.read_text(encoding="utf-8"), False


def extract_gap_profile(digest: str) -> str:
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


# ---------------------------------------------------------------------------
# Article evidence packet  (Stage 1 → Stage 2 contract)
# ---------------------------------------------------------------------------

def build_article_evidence(
    digest: str,
    preset: int | None = None,
    agg_probs: list[float] | None = None,
    section_details: list[dict] | None = None,
) -> dict:
    """Join the section-scorer output with parsed digest signals into one packet.

    The section list is taken from the digest (gap_profile rows), so this works
    with OR without the trained scorer: when ``section_details`` / ``agg_probs``
    are omitted (the LLM-standalone baseline) the per-section RL fields are left
    empty and ``rl_aggregate`` is None. When provided, RL detail is overlaid by
    sec_id.

    Args:
        digest:          Full v2 XML digest text.
        preset:          Section-scorer aggregate argmax (0–3), or None.
        agg_probs:       Aggregate distribution [skip, light, standard, deep], or None.
        section_details: Per-section infer output (title=sec_id, probs, chosen,
                         target_words, margin, confidence, weight), or None.

    Returns the ``article_evidence`` dict described in article_level_aggregator_plan.md §3.
    """
    parsed = _digest_parse.parse_digest(digest)
    meta = parsed["meta"]
    gap_rows = parsed["gap_rows"]
    gap_overall = parsed["gap_overall"]
    coverage = parsed["coverage"]

    total_tw = sum(r["target_words"] for r in gap_rows.values())
    rl_by_id = {d.get("title", ""): d for d in (section_details or [])}

    section_signals: list[dict] = []
    for sec_id, gap in gap_rows.items():
        cov = coverage.get(sec_id, {})
        d = rl_by_id.get(sec_id, {})
        tw = int(gap.get("target_words") or d.get("target_words") or 0)
        weight = (tw / total_tw) if total_tw > 0 else 0.0
        probs = d.get("probs", [])
        s_top2_margin = 0.0
        if len(probs) >= 2:
            s_ranked = sorted(probs, reverse=True)
            s_top2_margin = s_ranked[0] - s_ranked[1]
        section_signals.append({
            "sec_id": sec_id,
            "label": _digest_parse.short_label(sec_id),
            "title": _digest_parse.readable_title(sec_id),
            "target_words": tw,
            "weight": round(weight, 4),
            # RL per-section detail (empty when no scorer output)
            "chosen_preset": int(d["chosen"]) if "chosen" in d else None,
            "distribution": [round(p, 4) for p in probs],
            "top2": top2(probs) if probs else [],
            "top2_margin": round(s_top2_margin, 4),
            "model_confidence": round(float(d.get("confidence", 0.0)), 4),
            # digest-derived coverage / demand signals
            "need_depth": gap.get("need_depth", 0),
            "need_breadth": gap.get("need_breadth", 0),
            "depth_score": cov.get("depth_score", 0),
            "breadth_score": cov.get("breadth_score", 0),
            # Residual demand = raw need MINUS what's already covered. Raw need_depth
            # is universally large across articles and preset levels (see "DO NOT
            # ESCALATE ON RAW GAP COUNTS" in the planner system prompt) so it must
            # never drive escalation; residual is the more honest "how much is
            # actually still missing" figure and is context for the GENERAL DOWNWARD
            # OVERRIDE (a section can show need_depth=14 yet be fully served by
            # existing coverage, e.g. depth_score=6/8 already close to sufficient for
            # a science-explainer article backed by golden sources). The P1/P2
            # boundary itself is handled upstream by the deterministic cost-sensitive
            # rule (preset_infer_handler.apply_cost_sensitive_rule), not by this signal.
            "residual_depth": max(0, gap.get("need_depth", 0) - cov.get("depth_score", 0)),
            "residual_breadth": max(0, gap.get("need_breadth", 0) - cov.get("breadth_score", 0)),
            "mandatory_bullets": gap.get("mandatory_bullets", 0),
            "must_cover_depth": gap.get("must_cover_depth", 0),
            "must_stay_brief": gap.get("must_stay_brief", 0),
            "orphans": cov.get("orphans", {"depth": 0, "breadth": 0, "unreachable": 0}),
            "self_contained": cov.get("self_contained", False),
            "intent": cov.get("intent", ""),
        })

    rl_aggregate: dict | None = None
    if agg_probs is not None and preset is not None:
        ranked = sorted(agg_probs, reverse=True)
        top2_margin = ranked[0] - ranked[1] if len(ranked) >= 2 else 0.0
        # Budget-weighted HARD section-vote mass: for each preset, the fraction of
        # the article's writing budget whose own section argmax-voted for it. This is
        # the calibrated escalation signal — a large intro section voting skip would
        # otherwise blur out small-but-heavy technical sections that vote deep in the
        # soft aggregate distribution above.
        vote_mass = [0.0] * NUM_PRESETS
        for s in section_signals:
            cp = s.get("chosen_preset")
            if cp is not None and 0 <= cp < NUM_PRESETS:
                vote_mass[cp] += s["weight"]
        mass_total = sum(vote_mass)
        if mass_total > 0:
            vote_mass = [m / mass_total for m in vote_mass]
        rl_aggregate = {
            "preset": int(preset),
            "preset_name": PRESET_NAMES.get(int(preset), str(preset)),
            "distribution": [round(p, 4) for p in agg_probs],
            "confidence": round(agg_probs[preset], 4),
            "entropy_bits": round(entropy(agg_probs), 4),
            "top2_margin": round(top2_margin, 4),
            "section_vote_mass": [round(m, 4) for m in vote_mass],
            "escalation_mass": round(vote_mass[2] + vote_mass[3], 4),
            "standard_mass": round(vote_mass[2], 4),
            "deep_mass": round(vote_mass[3], 4),
        }

    return {
        "guideline_context": {
            "article_title": meta["article_title"],
            "external_evidence_policy": meta["external_evidence_policy"],
            "n_content_sections": meta["n_content_sections"] or len(section_signals),
            "expected_total_words": total_tw,
        },
        "rl_aggregate": rl_aggregate,
        "section_signals": section_signals,
        "digest_global": {
            "n_orphan_anchors": meta["n_orphan_anchors"],
            "total_sources": meta["total_sources"],
            "total_artefacts": meta["total_artefacts"],
            "dominant_gap_type": gap_overall["dominant_gap_type"],
            "weakest_sections": [
                _digest_parse.short_label(s) for s in gap_overall["weakest_sections"]
            ],
            "strongest_sections": [
                _digest_parse.short_label(s) for s in gap_overall["strongest_sections"]
            ],
        },
    }


# ---------------------------------------------------------------------------
# Production-pipeline glue (used by predict_exploration_preset_tool.py)
# ---------------------------------------------------------------------------

async def run_rl_stage(digest: str) -> dict:
    """Stage 1: RL inference + cost-sensitive rule + evidence packet + section signals."""
    loop = asyncio.get_running_loop()
    preset, agg_probs, section_details = await loop.run_in_executor(None, call_infer_server, digest)

    # Cost-sensitive decision rule: adjusts the raw argmax using the empirical
    # reward-asymmetry cost matrix (fit from train-set oracles), restricted to
    # a 1-level move. Supersedes plain argmax as the pipeline's RL recommendation
    # — see preset_infer_handler.apply_cost_sensitive_rule docstring for the
    # backtest that validated this (TEST exact 7->10, regret -51%, 0 new misses).
    raw_argmax_preset = preset
    preset = apply_cost_sensitive_rule(preset, agg_probs)
    cost_rule_adjusted = preset != raw_argmax_preset

    confidence = round(agg_probs[preset], 4)
    h = round(entropy(agg_probs), 4)
    section_floor = max((d["chosen"] for d in section_details), default=preset)
    floor_applied = preset <= 1 and section_floor >= 2 and h <= 1.5
    guidance_str = guidance(preset, confidence, h, floor_applied)
    if cost_rule_adjusted:
        guidance_str += (
            f" Cost-sensitive rule adjusted the raw vote P{raw_argmax_preset} -> "
            f"P{preset} (reward asymmetry: a miss in this direction is costlier "
            f"than the alternative at this boundary)."
        )

    # Build the structured, leakage-free evidence packet.
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

    return {
        "preset": preset,
        "raw_argmax_preset": raw_argmax_preset,
        "cost_rule_adjusted": cost_rule_adjusted,
        "confidence": confidence,
        "entropy_bits": h,
        "floor_applied": floor_applied,
        "guidance_str": guidance_str,
        "evidence": evidence,
        "section_signals": section_signals,
        "agg_probs": agg_probs,
    }


def assemble_result(
    digest_generated: bool,
    rl: dict,
    llm_recommendation: dict | None,
    article_guideline: str,
    digest_gap_profile: str,
) -> dict:
    """Assemble predict_exploration_preset_tool.py's return dict from a completed RL stage."""
    return {
        "status": "success",
        "digest_generated": digest_generated,
        "rl_recommendation": {
            "preset": rl["preset"],
            "name": PRESET_NAMES[rl["preset"]],
            "confidence": rl["confidence"],
            "entropy_bits": rl["entropy_bits"],
            "floor_correction_applied": rl["floor_applied"],
            "agg_probs": [round(float(p), 4) for p in rl["agg_probs"]],
            "raw_argmax_preset": rl["raw_argmax_preset"],
            "cost_rule_adjusted": rl["cost_rule_adjusted"],
        },
        "section_signals": rl["section_signals"],
        "guidance": rl["guidance_str"],
        "llm_recommendation": llm_recommendation,
        "article_evidence": rl["evidence"],
        "article_guideline": article_guideline,
        "digest_gap_profile": digest_gap_profile,
        "message": (
            f"RL model recommends preset P{rl['preset']} ({PRESET_NAMES[rl['preset']]}) "
            f"with {rl['confidence']:.0%} confidence across {len(rl['section_signals'])} sections. "
            f"Entropy: {rl['entropy_bits']:.2f} bits."
        ),
    }


# ---------------------------------------------------------------------------
# Deterministic fallback aggregator
# ---------------------------------------------------------------------------

def fallback_aggregator(evidence: dict) -> dict:
    """Deterministic article preset from the evidence packet (no LLM call).

    Used when XAI_API_KEY is unset or when the planner LLM returns unparseable
    output. Applies the RL aggregate vote and hard policy guards.
    """
    rl = evidence["rl_aggregate"]
    policy = evidence["guideline_context"]["external_evidence_policy"]
    rl_preset = int(rl["preset"])

    if policy == "forbidden":
        return {
            "preset": 0,
            "name": "skip",
            "reasoning": "external_evidence_policy=forbidden — exploration output is unusable.",
            "override": rl_preset != 0,
            "override_reason": "policy forbids external evidence" if rl_preset != 0 else None,
            "decision_drivers": ["policy:forbidden"],
            "risk_flags": [],
        }

    preset = rl_preset
    drivers = ["rl_aggregate"]
    risk_flags: list[str] = []
    if policy == "required" and preset < 1:
        preset = 1
        drivers.append("policy:required")
    if policy == "capped":
        dist = rl["distribution"]
        if preset > 1:
            # A.20.14: a corpus-wide check (13/14 oracle-standard/deep articles,
            # plus every one of 6 cross-referenced real RL-distribution cases)
            # found ZERO confirmed cases of skip beating light in this
            # population -- not even the cases where the residual itself
            # favored skip. The residual therefore carries no demonstrated
            # skip-favoring signal, so every standard/deep vote capped to light
            # is flagged AMBIGUOUS for review, regardless of the residual split.
            preset = 1
            drivers.append("policy:capped")
            risk_flags.append(
                f"policy=capped AMBIGUOUS: standard/deep vote capped to light "
                f"(residual P(skip)={dist[0]:.3f} vs P(light)={dist[1]:.3f}) -- no "
                f"data-confirmed case of skip beating light in this population "
                f"(A.20.14); flagged for review"
            )
        else:
            resolved = 1 if dist[1] >= dist[0] else 0
            if resolved != preset:
                preset = resolved
                drivers.append("policy:capped")

    return {
        "preset": preset,
        "name": PRESET_NAMES.get(preset, str(preset)),
        "reasoning": (
            f"Deterministic fallback: section-scorer vote ({rl['preset_name']}) "
            f"adjusted for policy={policy}."
        ),
        "override": preset != rl_preset,
        "override_reason": None,
        "decision_drivers": drivers,
        "risk_flags": ["deterministic fallback — no LLM reasoning applied", *risk_flags],
    }


