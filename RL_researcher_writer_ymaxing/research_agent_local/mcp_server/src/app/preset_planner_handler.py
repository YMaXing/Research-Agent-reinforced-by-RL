"""
Grok 4.2 planner handler for the predict_exploration_preset tool.

Builds the leakage-free article evidence packet from a v2 digest and optional
RL section-scorer output, renders it as a guided markdown brief, and calls the
Grok 4.2 reasoning model (or a deterministic fallback) for the final
exploration-preset decision.
"""

from __future__ import annotations

import json as _json
import logging
import re
import sys
from pathlib import Path
from typing import Any

from .preset_infer_handler import (
    PRESET_NAMES,
    NUM_PRESETS,
    entropy,
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

# ---------------------------------------------------------------------------
# Grok planner model
# ---------------------------------------------------------------------------
_PLANNER_MODEL = "grok-4.20-0309-reasoning"

# ---------------------------------------------------------------------------
# Calibrated escalation thresholds
# ---------------------------------------------------------------------------
# When the RL aggregate vote is UNCERTAIN (confidence < _DECISIVE_CONFIDENCE or
# entropy > 1.5 bits), Grok may escalate above the RL pick, but only when the
# budget-weighted section-vote mass clears _ESCALATION_MASS_THRESHOLD. These MUST
# stay in sync with the numeric thresholds written into _PLANNER_SYSTEM.
_DECISIVE_CONFIDENCE = 0.70
_ESCALATION_MASS_THRESHOLD = 0.30

# ---------------------------------------------------------------------------
# Article evidence packet constants
# ---------------------------------------------------------------------------
_POLICY_MEANING: dict[str, str] = {
    "forbidden": (
        "external evidence is NOT allowed for this article — exploration output "
        "cannot be used, so the only valid choice is skip"
    ),
    "allowed": (
        "external web evidence is permitted but not mandatory — explore only if "
        "the gaps justify it"
    ),
    "required": (
        "external web evidence is mandatory — at least light exploration must run"
    ),
}

# ---------------------------------------------------------------------------
# Guideline appendix
# ---------------------------------------------------------------------------
# Real guidelines top out around ~34k chars (~8.5k tokens); the 80k ceiling
# (~20k tokens) never truncates legitimate content.
_INCLUDE_GUIDELINE_IN_PLANNER = True
_GUIDELINE_APPENDIX_MAX_CHARS = 80_000


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
    are omitted (the Grok-standalone baseline) the per-section RL fields are left
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
# Evidence rendering helpers
# ---------------------------------------------------------------------------

def _interpret_rl(conf: float, h: float) -> str:
    if h > 1.5:
        return (
            f"UNCERTAIN (entropy {h:.2f} bits > 1.5) — the scorer is spread across "
            "presets and NOT decisive; let the budget-weighted section votes set the level."
        )
    if conf >= 0.70:
        return (
            f"DECISIVE ({conf:.0%} of the vote on its top pick) — a strong learned "
            "signal; trust it and do not escalate above it without a hard constraint."
        )
    if conf >= 0.40:
        return (
            f"MODERATE ({conf:.0%} on its top pick) — a real lean but NOT decisive; "
            "weigh the budget-weighted section votes below to set the level."
        )
    return (
        f"WEAK ({conf:.0%} on its top pick) — NOT decisive; let the budget-weighted "
        "section votes set the level."
    )


def _pct_row(dist: list[float]) -> str:
    names = ["skip", "light", "standard", "deep"]
    return "  ·  ".join(
        f"{names[i]} {dist[i]*100:.0f}%" for i in range(min(len(dist), 4))
    )


def render_guideline_appendix(article_guideline: str) -> str:
    """Render the raw article guideline as a clearly-delimited primary source.

    Returns ``""`` when no guideline text is given.
    """
    text = (article_guideline or "").strip()
    if not text:
        return ""
    if len(text) > _GUIDELINE_APPENDIX_MAX_CHARS:
        text = text[:_GUIDELINE_APPENDIX_MAX_CHARS] + "\n\n[... guideline truncated ...]"
    return (
        "---\n\n"
        "## Appendix — Article guideline (primary source)\n"
        "The full author-written guideline is reproduced verbatim below. The "
        "structured brief above is your PRIMARY decision basis; consult this only "
        "for qualitative scope cues the numbers miss — intended depth, audience, "
        "tone, and any explicit \"keep this brief\" / \"go deep here\" instructions. "
        "Do NOT let the guideline's sheer length or detail inflate the preset: "
        "exploration buys missing *evidence*, not matching prose volume.\n\n"
        "<article_guideline>\n"
        f"{text}\n"
        "</article_guideline>\n"
    )


def render_evidence_brief(
    evidence: dict,
    *,
    include_rl: bool = True,
    article_guideline: str = "",
) -> str:
    """Render the evidence packet as a guided markdown decision brief.

    When ``include_rl`` is False the trained-scorer sections are omitted (used
    for the Grok-standalone baseline so it decides from the guideline + gaps
    alone, isolating the RL signal's marginal value).

    When ``article_guideline`` is non-empty it is appended verbatim as a
    primary-source appendix after the structured brief.
    """
    gc = evidence["guideline_context"]
    glob = evidence["digest_global"]
    secs = evidence["section_signals"]
    policy = gc["external_evidence_policy"]

    out: list[str] = []

    # --- 1. Article ---
    out.append("# Exploration Decision Brief\n")
    out.append("## 1. Article")
    out.append(f"- Title: {gc['article_title'] or '(untitled)'}")
    out.append(f"- Content sections: {gc['n_content_sections']}")
    out.append(f"- Total writing budget: {gc['expected_total_words']} words")
    out.append(
        f"- External-evidence policy: **{policy.upper()}** — "
        f"{_POLICY_MEANING.get(policy, 'unknown policy')}"
    )
    out.append("")

    # --- 2. Trained section-scorer aggregate (primary signal) ---
    if include_rl:
        rl = evidence["rl_aggregate"]
        out.append("## 2. Trained section-scorer — aggregate recommendation  (primary signal)")
        out.append(
            "A GRPO-trained model read every section and voted for an exploration "
            "preset, weighting each section by its writing budget. This learned, "
            "budget-weighted vote is the best single predictor of the reward-optimal "
            "preset — treat it as your prior and move off it only for a concrete reason."
        )
        out.append("")
        out.append(f"- Recommendation: **P{rl['preset']} {rl['preset_name']}**")
        out.append(f"- Soft vote distribution:  {_pct_row(rl['distribution'])}")
        out.append(f"- Read: {_interpret_rl(rl['confidence'], rl['entropy_bits'])}")
        if "section_vote_mass" in rl:
            std_m = rl.get("standard_mass", 0.0)
            deep_m = rl.get("deep_mass", 0.0)
            out.append(
                f"- Budget-weighted section votes:  {_pct_row(rl['section_vote_mass'])}"
            )
            bar = f"{_ESCALATION_MASS_THRESHOLD*100:.0f}%"
            out.append(
                f"- Vote-mass gates: standard-vote mass = {std_m*100:.0f}%  \u00b7  "
                f"deep-vote mass = {deep_m*100:.0f}%  (bar {bar}). These masses ONLY "
                f"gate a P2->P3 escalation (deep-vote mass \u2265 {bar} from a P2 pick) "
                f"and the deep-or-nothing guard. They do NOT sanction escalating a P0/P1 "
                f"pick up to P2 \u2014 see OVERRIDE POLICY."
            )
            self_contained_wt = sum(s["weight"] for s in secs if s.get("self_contained"))
            out.append(
                f"- Residual/self-containment context: {self_contained_wt*100:.0f}% of the "
                f"writing budget sits in sections flagged self-contained (see \u00a73 table). "
                f"This is descriptive context only \u2014 it is NOT a sanctioned mechanism for "
                f"moving off the RL pick; the RL pick already incorporates a reward-calibrated "
                f"cost-sensitive adjustment before you see it."
            )
        out.append("")

    # --- 3. Per-section breakdown ---
    out.append("## 3. Per-section breakdown")
    out.append(
        "Each row is one section. **Budget** is its share of the article (larger "
        "sections dominate the article-level choice). The gap columns contrast what "
        "the exploitation pass already covered against what the guideline demands."
    )
    out.append("")

    if include_rl:
        header = (
            "| # | Section | Budget | RL pick | need d/b | cov d·b | resid d/b | self-cont | must-ev | orphans d/b | brief |"
        )
        sep = "|---|---------|-------:|---------|:-------:|:------:|:--------:|:--------:|:------:|:----------:|:----:|"
    else:
        header = (
            "| # | Section | Budget | need d/b | cov d·b | resid d/b | self-cont | must-ev | orphans d/b | brief |"
        )
        sep = "|---|---------|-------:|:-------:|:------:|:--------:|:--------:|:------:|:----------:|:----:|"
    out.append(header)
    out.append(sep)

    for i, s in enumerate(secs, 1):
        budget = f"{s['weight']*100:.0f}%"
        need = f"{s['need_depth']}/{s['need_breadth']}"
        cov = f"{s['depth_score']}·{s['breadth_score']}"
        resid = f"{s.get('residual_depth', 0)}/{s.get('residual_breadth', 0)}"
        self_cont = "yes" if s.get("self_contained") else "—"
        must_ev = str(s["must_cover_depth"])
        orph = f"{s['orphans']['depth']}/{s['orphans']['breadth']}"
        brief = "yes" if s["must_stay_brief"] else "—"
        sec_label = f"{s['label']} {s['title']}"[:40]
        if include_rl:
            rl_pick = (
                f"{PRESET_NAMES.get(s['chosen_preset'], '?')} "
                f"·{s['top2_margin']:.2f}"
            )
            out.append(
                f"| {i} | {sec_label} | {budget} | {rl_pick} | {need} | {cov} | "
                f"{resid} | {self_cont} | {must_ev} | {orph} | {brief} |"
            )
        else:
            out.append(
                f"| {i} | {sec_label} | {budget} | {need} | {cov} | "
                f"{resid} | {self_cont} | {must_ev} | {orph} | {brief} |"
            )

    out.append("")
    out.append("Legend:")
    out.append(
        "- **need d/b** — unmet depth / breadth gap pressure (higher = more "
        "missing; includes orphaned guideline anchors). Universally large across "
        "articles and presets — do NOT use this raw number to escalate."
    )
    out.append(
        "- **cov d·b** — coverage already achieved (depth out of 8, breadth out of 6)."
    )
    out.append(
        "- **resid d/b** — RESIDUAL need = need MINUS coverage already achieved. This "
        "is the honest \"how much is actually still missing\" figure \u2014 context for "
        "the GENERAL DOWNWARD OVERRIDE only, not a standalone trigger."
    )
    out.append(
        "- **self-cont** — \"yes\" means the digest judged this section's already-scraped "
        "sources well-matched to its topic. Supporting context, but NOT sufficient alone "
        "\u2014 some genuinely-P2 articles have every section self-contained yet still need "
        "real new depth/breadth; check resid d/b too."
    )
    out.append(
        "- **must-ev** — # mandatory bullets that REQUIRE named evidence (tools, "
        "benchmarks, numbers). High = section cannot be written well without sourced facts."
    )
    out.append(
        "- **orphans d/b** — guideline anchors with no backing source yet "
        "(depth / breadth)."
    )
    out.append(
        "- **brief** — \"yes\" means the section must stay short and cannot absorb "
        "extra research."
    )
    if include_rl:
        out.append(
            "- **RL pick** — that section's own scorer choice and its top-2 margin "
            "(bigger margin = more confident)."
        )
    out.append("")

    # Section intents (semantic context, one line each)
    if any(s["intent"] for s in secs):
        out.append("Section intents:")
        for s in secs:
            if s["intent"]:
                out.append(f"- {s['label']} — {s['intent']}")
        out.append("")

    # --- 4. Exploration economics ---
    out.append("## 4. Exploration economics (article-wide)")
    out.append(
        f"- Unbacked anchors (article-wide): {glob['n_orphan_anchors']} — guideline "
        "claims still lacking a source."
    )
    out.append(
        f"- Dominant gap type: {glob['dominant_gap_type'] or 'n/a'} — where the "
        "missing coverage mostly lies."
    )
    weak = ", ".join(glob["weakest_sections"]) or "n/a"
    strong = ", ".join(glob["strongest_sections"]) or "n/a"
    out.append(f"- Weakest sections: {weak}   ·   Strongest: {strong}")
    out.append("")

    # --- 5. Primary-source appendix: raw article guideline (optional) ---
    appendix = render_guideline_appendix(article_guideline)
    if appendix:
        out.append(appendix)

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Deterministic fallback aggregator
# ---------------------------------------------------------------------------

def fallback_aggregator(evidence: dict) -> dict:
    """Deterministic article preset from the evidence packet (no LLM call).

    Used when XAI_API_KEY is unset or when Grok returns unparseable output.
    Applies the RL aggregate vote and hard policy guards.
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
    if policy == "required" and preset < 1:
        preset = 1
        drivers.append("policy:required")

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
        "risk_flags": ["deterministic fallback — no LLM reasoning applied"],
    }


# ---------------------------------------------------------------------------
# Deterministic policy guard (hard constraint clamp)
# ---------------------------------------------------------------------------
# Never trust the LLM to honour the external-evidence policy. After Grok returns
# a preset, clamp it deterministically so a policy violation is impossible:
#   forbidden -> P0 skip   (exploration output is unusable in the final article)
#   required  -> >= P1 light (external evidence is mandatory)
# These are the only two policy directions that have a hard, non-negotiable
# constraint; "allowed" imposes nothing.

def _apply_policy_guards(preset: int, policy: str) -> tuple[int, str | None]:
    """Clamp a chosen preset to satisfy the external-evidence policy.

    Returns ``(clamped_preset, note)`` where ``note`` is a short human-readable
    string when a clamp fired, else None.
    """
    if policy == "forbidden" and preset != 0:
        return 0, f"policy=forbidden: clamped P{preset}->P0 skip"
    if policy == "required" and preset < 1:
        return 1, f"policy=required: clamped P{preset}->P1 light"
    return preset, None


# ---------------------------------------------------------------------------
# Deterministic escalation guard (hard constraint clamp)
# ---------------------------------------------------------------------------
# The planner prompt explicitly states "NEVER escalate a P0 or P1 pick up to P2
# or higher, regardless of vote mass or gap counts" (in both the system prompt
# and the user template) — but a 2026-07-10 held-out backtest showed Grok
# violating this anyway, using the budget-weighted vote-mass number to
# functionally reconstruct a retired P1->P2 escalation (override_reason:
# "departed from uncertain P1 aggregate to P2 because budget-weighted standard
# mass (68%)..."), undoing a correct cost-rule-adjusted RL pick. A prompt-level
# instruction alone is not reliable enough for this hard boundary; enforce it
# in code, matching the existing forbidden/required policy-guard pattern. The
# still-sanctioned P0->P1 nudge (one level up) is unaffected.

def _apply_escalation_guard(preset: int, rl_preset: int) -> tuple[int, str | None]:
    """Hard block: never let Grok escalate a P0/P1 RL pick all the way to P2+.

    Returns ``(clamped_preset, note)`` where ``note`` is a short human-readable
    string when a clamp fired, else None.
    """
    if rl_preset <= 1 and preset >= 2:
        return (
            1,
            f"escalation_guard: clamped P{preset}->P1 (RL pick was P{rl_preset}; "
            f"escalating a P0/P1 RL vote to P2+ is not permitted)",
        )
    return preset, None


# ---------------------------------------------------------------------------
# Grok 4.2 system prompts and user templates
# ---------------------------------------------------------------------------

_PLANNER_SYSTEM = """\
You are the article-level exploration planner for an autonomous research-and-writing \
system. Your decisions are scored against an offline oracle, so accuracy matters.

THE DECISION
Before an article is written, the system can run extra rounds of autonomous web \
exploration to close coverage gaps. Exploration costs time and money and, past a \
point, returns mostly duplicate material. Choose ONE exploration preset for the \
whole article that buys the most useful new coverage for the least waste.

THE FOUR PRESETS (ordered by cost)
  P0 skip     - no exploration. Existing coverage is already sufficient.
  P1 light    - 1 round, balanced (~50% depth / 50% breadth). Cheap touch-up.
  P2 standard - 2 rounds: depth -> breadth. Meaningful gap-filling.
  P3 deep     - 3 rounds: depth -> breadth -> depth. Expensive; only when large,
                evidence-heavy gaps clearly justify it.

WHERE THE EVIDENCE COMES FROM (so you weigh it correctly)
A single exploitation pass has already run. From it you receive a guided brief with:
  1. A trained section-scorer's budget-weighted vote over the four presets. The
     scorer was trained (GRPO) to predict, per section, which preset maximises the
     article's reward — it already weighed every per-section gap (must-ev, unbacked
     anchors, need_depth, coverage scores) against the reward trade-off. Its
     aggregate vote is the reward-trained estimate of the optimal preset. Treat it
     as your primary signal and the approximate location of the reward peak.
  2. A per-section table of coverage already achieved vs. what the guideline demands,
     including a RESIDUAL-need column (need minus coverage) and a self-contained flag.
     Use this to understand DIRECTION (which sections need depth-first vs.
     breadth-first rounds) and, per the OVERRIDE POLICY below, as the basis for the
     sanctioned downward step — NOT to re-derive escalation from raw need_depth.
  3. Article-wide gap economics (unbacked anchors, dominant gap type).

THE REWARD CURVE IS SINGLE-PEAKED
Article reward as a function of preset is unimodal: one optimum, declining on both
sides. Over-escalating past the peak dilutes the article's guideline-adherence, flow
and structure while buying diminishing returns; under-escalating leaves evidence gaps
unfilled. BOTH directions lose reward — aim for the peak, and do NOT reflexively round
toward the cheapest arm.

TRUST THE SCORER WHEN IT IS CONFIDENT; READ THE VOTES WHEN IT IS NOT
The section-scorer's aggregate vote is the reward-trained estimate of the peak, but it
is only as trustworthy as it is confident, and it can be mis-calibrated on articles
unlike those it was trained on:
  - DECISIVE (confidence >= 70% and low entropy): a strong learned signal. Do NOT pick
    a preset above it — upward escalation is almost never correct here.
  - UNCERTAIN (confidence < 70% OR entropy > 1.5 bits): the learned signal is weak. The
    budget-weighted per-section votes carry real information the aggregate has blurred
    away; use them together with the OVERRIDE POLICY below, which may point up OR down.

DO NOT ESCALATE ON RAW GAP COUNTS
Coverage gaps (must-ev, unbacked anchors, need_depth) are universally present across
every article and preset level and carry little information about whether escalation
helps. Do NOT escalate just because these counts look large. The single calibrated
escalation signal is the BUDGET-WEIGHTED SECTION-VOTE MASS in the brief: the share of
the article's writing budget whose own section voted skip / light / standard / deep. A
large intro section voting skip can hide small-but-heavy technical sections that need
deep exploration — the vote mass exposes exactly that.

RESIDUAL NEED IS CONTEXT, NOT A DECISION TRIGGER
The brief's "resid d/b" column (need MINUS coverage already achieved) is NOT a raw gap
count — it is the honest measure of what is actually still missing. It is useful context
for the GENERAL DOWNWARD OVERRIDE below, but it is NOT a standalone trigger: the RL pick
you are shown has ALREADY been adjusted by a reward-calibrated cost-sensitive rule before
you see it (see PIPELINE NOTE below), so do not re-derive a P1/P2 boundary correction from
residual need yourself — that correction is already baked into the pick.

PIPELINE NOTE — THE RL PICK IS ALREADY COST-ADJUSTED
The RL pick shown above is not a raw model argmax. It has already been passed through a
deterministic, empirically-fit cost-sensitive rule that corrects for known reward
asymmetries (under-shooting the true preset is usually costlier than a 1-level
over-shoot). Do not attempt to re-derive that correction yourself from confidence,
residual need, or self-containment — you would likely be duplicating or fighting a
correction that was already made more reliably than a prompt-level judgement call can.
Your job is to catch what a numeric rule CANNOT see (policy compliance, and genuinely
qualitative red flags), not to re-second-guess the P0-P3 level itself.

OVERRIDE POLICY
  - SANCTIONED UPWARD ESCALATION — P2 -> P3 ONLY, and ONLY when the scorer vote is
    UNCERTAIN:
      * To P3 deep: if the RL pick is P2 AND the budget-weighted mass of sections
        voting DEEP specifically is >= 30% — choose P3.
      * NEVER escalate a P0 or P1 pick up to P2 or higher, regardless of vote mass or
        gap counts. This is enforced as a HARD, NON-NEGOTIABLE CODE-LEVEL GUARD after
        your response — any P2+ you return when the RL pick was P0/P1 will be silently
        clamped back down, so there is no benefit to attempting it. (An earlier policy
        revision sanctioned this escalation; it was retired after held-out evaluation
        showed it fired twice and was wrong both times, and a later revision found the
        LLM was still reaching this outcome via vote-mass reasoning despite an explicit
        textual prohibition — hence the hard code-level guard now, not just a prompt rule.)
      * NEVER escalate when the vote is DECISIVE.
  - DEEP-OR-NOTHING GUARD: if the RL pick is P1 and the deep-vote mass is high while
    the standard-vote mass is low (a depth-or-nothing pattern), do NOT infer that P2 is
    worth trying — the standard middle sits in a reward valley for such articles. P3 is
    reachable only from a P2 pick, never a two-level jump from P1.
  - GENERAL DOWNWARD OVERRIDE: you MAY choose one level BELOW the scorer's pick when
    most high-budget sections are brief-flagged or already well-covered (depth_score
    >= 6, or residual need near zero), or the vote is highly uncertain with no
    dominant arm AND neither standard-vote nor deep-vote mass reaches 30% (no real
    escalation signal).
  - SANCTIONED P0 -> P1 NUDGE: if the scorer votes P0 skip, its runner-up is P1 light
    with substantial mass (>= 25%), AND neither standard-vote nor deep-vote mass
    reaches 30% — you MAY choose P1 light as cheap insurance.

USE need_depth / need_breadth FOR ROUND COMPOSITION, NOT LEVEL
Once you have chosen a preset, need_depth / need_breadth tell you which sections need
depth-first vs. breadth-first rounds — let them shape the composition of the rounds
(depth -> breadth vs. balanced). The escalation/down-step LEVEL, by contrast, comes
from the budget-weighted section-vote mass and residual-need/self-contained signals,
not from these raw gap columns.

PRIMARY-SOURCE APPENDIX (may follow the brief)
You may also receive the full author-written article guideline reproduced verbatim.
The structured brief is your PRIMARY basis; use the guideline only to catch
qualitative scope cues the numbers cannot express (intended depth, audience, tone,
explicit "keep brief"/"go deep" instructions). Never let its length, ambition, or
detail push the preset up — exploration buys missing evidence, not matching prose
volume.

HARD CONSTRAINTS (these override everything above)
  - external-evidence policy = forbidden -> you MUST choose P0 skip.
  - external-evidence policy = required  -> you MUST choose at least P1 light.

OUTPUT
Reason briefly first (a few sentences citing the SPECIFIC evidence that drove you),
then output ONLY this JSON block, with nothing after it:

```json
{{
  "preset": <integer 0-3>,
  "name": "<skip|light|standard|deep>",
  "reasoning": "<2-4 sentences naming the decisive evidence>",
  "override": <true|false>,
  "override_reason": "<why you departed from the section-scorer's aggregate, or null>",
  "decision_drivers": ["<short names of the signals that drove the choice>"],
  "risk_flags": ["<short notes on what could make this decision wrong>"]
}}
```"""

_PLANNER_STANDALONE_SYSTEM = """\
You are the article-level exploration planner for an autonomous research-and-writing \
system. You will be shown a guided brief built from a single exploitation pass: the \
article overview, a per-section table of coverage vs. guideline demand, and \
article-wide exploration economics. There is NO trained-model recommendation in this \
mode — decide entirely on your own reading of the evidence.

THE DECISION
Choose ONE exploration preset for the whole article that buys the most useful new \
coverage for the least waste.

THE FOUR PRESETS (ordered by cost)
  P0 skip     - no exploration. Existing coverage is already sufficient.
  P1 light    - 1 round, balanced (~50% depth / 50% breadth). Cheap touch-up.
  P2 standard - 2 rounds: depth -> breadth. Meaningful gap-filling.
  P3 deep     - 3 rounds: depth -> breadth -> depth. Expensive; only when large,
                evidence-heavy gaps clearly justify it.

HOW TO WEIGH THE SIGNALS
  - Default toward the CHEAPER arm; escalate only on concrete, sizeable, evidence-driven
    gaps (large need_depth AND a depth mandate).
  - Weight sections by writing budget; gaps in tiny or "must stay brief" sections barely
    matter.
  - must-ev (must_cover_depth) is depth pressure even when need_depth looks modest.
  - The table's "resid d/b" column is need MINUS existing coverage — a small residual
    means the gap is mostly already filled; weigh this more heavily than the raw need
    column when judging whether escalation is really warranted.
  - "self-cont" flags a section whose already-gathered sources are well-matched to its
    topic — supporting (not sufficient) evidence that little new exploration is needed
    there; check it alongside resid d/b, not in isolation.

PRIMARY-SOURCE APPENDIX (may follow the brief)
You may also receive the full author-written article guideline reproduced verbatim.
The structured brief is your PRIMARY basis; use the guideline only to catch
qualitative scope cues the numbers cannot express (intended depth, audience, tone,
explicit "keep brief"/"go deep" instructions). Never let its length, ambition, or
detail push the preset up — exploration buys missing evidence, not matching prose
volume.

HARD CONSTRAINTS (these override everything above)
  - external-evidence policy = forbidden -> you MUST choose P0 skip.
  - external-evidence policy = required  -> you MUST choose at least P1 light.

OUTPUT
Reason briefly first (a few sentences citing the specific evidence), then output ONLY
this JSON block, with nothing after it:

```json
{{
  "preset": <integer 0-3>,
  "name": "<skip|light|standard|deep>",
  "reasoning": "<2-4 sentences naming the decisive evidence>",
  "decision_drivers": ["<short names of the signals that drove the choice>"],
  "risk_flags": ["<short notes on what could make this decision wrong>"]
}}
```"""

_PLANNER_USER_TEMPLATE = """\
{evidence_brief}
---

## Your task
Decide the single exploration preset for THIS article. Work through the brief above
step by step:
  1. State the section-scorer's aggregate vote (already cost-adjusted upstream) and
     whether it is DECISIVE or UNCERTAIN.
  2. If UNCERTAIN, check whether a sanctioned P2->P3 escalation, a general downward
     override, or a P0->P1 nudge applies (see OVERRIDE POLICY in your instructions).
     Use the preset-SPECIFIC deep-vote mass for the P2->P3 escalation. NEVER escalate
     a P0/P1 pick up to P2 or higher under any circumstance \u2014 this is enforced as a
     hard code-level guard regardless of what you return, so do not spend reasoning
     trying to justify it.
  3. State your final choice and the single most decisive reason.

Then output ONLY the JSON block specified in your instructions (nothing after it)."""

_PLANNER_STANDALONE_USER_TEMPLATE = """\
{evidence_brief}
---

## Your task
Decide the single exploration preset for THIS article based solely on the brief above.
Work through it step by step - weigh the per-section gaps against the writing budgets
and the exploration economics - then output ONLY the JSON block specified in your
instructions (nothing after it)."""


# ---------------------------------------------------------------------------
# JSON extraction helper
# ---------------------------------------------------------------------------

def _extract_json_block(raw: str) -> dict:
    """Pull the JSON decision object out of a model reply.

    Tries a fenced ```json block first, then the last bare {...} object.
    Returns ``{}`` on any parse failure.
    """
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    json_str = m.group(1) if m else ""
    if not json_str:
        matches = re.findall(r"\{[^{}]*\}", raw, re.DOTALL)
        json_str = matches[-1] if matches else ""
    if not json_str:
        return {}
    try:
        return _json.loads(json_str)
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Grok 4.2 planner calls
# ---------------------------------------------------------------------------

async def call_grok_planner(
    api_key: str,
    base_url: str,
    evidence: dict,
    article_guideline: str = "",
) -> dict:
    """Call Grok 4.2 for the final exploration-preset decision.

    Grok receives the guided evidence brief rendered from ``evidence``.
    When ``article_guideline`` is provided it is appended verbatim as a
    primary-source appendix.

    Returns a dict with keys: preset, name, reasoning, override, override_reason,
    decision_drivers, risk_flags.  Falls back to ``fallback_aggregator`` on any
    parsing failure.
    """
    from openai import AsyncOpenAI  # noqa: PLC0415

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    rl_preset = int(evidence["rl_aggregate"]["preset"])
    policy = evidence["guideline_context"]["external_evidence_policy"]
    user_msg = _PLANNER_USER_TEMPLATE.format(
        evidence_brief=render_evidence_brief(
            evidence, include_rl=True, article_guideline=article_guideline
        )
    )

    response = await client.chat.completions.create(
        model=_PLANNER_MODEL,
        messages=[
            {"role": "system", "content": _PLANNER_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        max_tokens=4096,
    )
    raw = (response.choices[0].message.content or "").strip()

    parsed = _extract_json_block(raw)
    try:
        parsed_preset = int(parsed["preset"])
        if parsed_preset not in range(NUM_PRESETS):
            raise ValueError(f"preset {parsed_preset} out of range 0-{NUM_PRESETS - 1}")
        # Deterministic hard-constraint guards, applied in order:
        # (1) never let Grok escalate a P0/P1 RL pick to P2+ (see
        #     _apply_escalation_guard docstring — a prompt instruction alone was
        #     shown to be insufficient); (2) forbidden->skip, required->>=light.
        escalated_preset, escalation_note = _apply_escalation_guard(parsed_preset, rl_preset)
        final_preset, guard_note = _apply_policy_guards(escalated_preset, policy)
        drivers = parsed.get("decision_drivers", [])
        risk_flags = parsed.get("risk_flags", [])
        override_reason = parsed.get("override_reason")
        notes = [n for n in (escalation_note, guard_note) if n]
        if notes:
            drivers = [*drivers, "policy_guard"]
            risk_flags = [*risk_flags, *notes]
            joined_notes = "; ".join(notes)
            override_reason = (
                joined_notes if not override_reason else f"{override_reason}; {joined_notes}"
            )
        return {
            "preset": final_preset,
            "name": PRESET_NAMES[final_preset],
            "reasoning": parsed.get("reasoning", ""),
            "override": final_preset != rl_preset,
            "override_reason": override_reason,
            "decision_drivers": drivers,
            "risk_flags": risk_flags,
        }
    except Exception:
        logger.warning(
            "Grok planner response could not be parsed as JSON; "
            "using deterministic fallback. raw=%s", raw[:300]
        )
        fb = fallback_aggregator(evidence)
        fb["reasoning"] = "Grok JSON parse failed; " + fb["reasoning"]
        return fb


async def call_grok_planner_standalone(
    api_key: str,
    base_url: str,
    evidence: dict,
    article_guideline: str = "",
) -> dict | None:
    """Call Grok 4.2 with NO trained-scorer signal (the Grok-alone baseline).

    The primary-source guideline appendix (when provided) is included identically
    to the full call so the only difference between the two modes is the RL signal.

    Returns a dict with keys: preset, name, reasoning, decision_drivers,
    risk_flags.  Returns None on parsing failure.
    """
    from openai import AsyncOpenAI  # noqa: PLC0415

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    policy = evidence["guideline_context"]["external_evidence_policy"]
    user_msg = _PLANNER_STANDALONE_USER_TEMPLATE.format(
        evidence_brief=render_evidence_brief(
            evidence, include_rl=False, article_guideline=article_guideline
        )
    )

    response = await client.chat.completions.create(
        model=_PLANNER_MODEL,
        messages=[
            {"role": "system", "content": _PLANNER_STANDALONE_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        max_tokens=4096,
    )
    raw = (response.choices[0].message.content or "").strip()

    parsed = _extract_json_block(raw)
    try:
        parsed_preset = int(parsed["preset"])
        if parsed_preset not in range(NUM_PRESETS):
            raise ValueError(f"preset {parsed_preset} out of range 0-{NUM_PRESETS - 1}")
        # Deterministic hard-constraint guard (forbidden->skip, required->>=light).
        final_preset, guard_note = _apply_policy_guards(parsed_preset, policy)
        drivers = parsed.get("decision_drivers", [])
        risk_flags = parsed.get("risk_flags", [])
        if guard_note:
            drivers = [*drivers, "policy_guard"]
            risk_flags = [*risk_flags, guard_note]
        return {
            "preset": final_preset,
            "name": PRESET_NAMES[final_preset],
            "reasoning": parsed.get("reasoning", ""),
            "decision_drivers": drivers,
            "risk_flags": risk_flags,
        }
    except Exception:
        logger.warning(
            "Grok standalone planner response could not be parsed as JSON. raw=%s", raw[:300]
        )
        return None
