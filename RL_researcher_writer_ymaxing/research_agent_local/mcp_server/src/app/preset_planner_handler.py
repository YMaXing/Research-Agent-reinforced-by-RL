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
        rl_aggregate = {
            "preset": int(preset),
            "preset_name": PRESET_NAMES.get(int(preset), str(preset)),
            "distribution": [round(p, 4) for p in agg_probs],
            "confidence": round(agg_probs[preset], 4),
            "entropy_bits": round(entropy(agg_probs), 4),
            "top2_margin": round(top2_margin, 4),
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
            f"UNCERTAIN (entropy {h:.2f} bits > 1.5) — the scorer is spread "
            "across presets, so your own reading of the gaps carries more weight."
        )
    if conf >= 0.70:
        return (
            f"DECISIVE ({conf:.0%} of the vote on its top pick) — a strong learned "
            "signal; depart from it only with a concrete reason."
        )
    if conf >= 0.40:
        return (
            f"MODERATE ({conf:.0%} on its top pick) — a real lean, but confirm it "
            "against the per-section gaps below."
        )
    return f"WEAK ({conf:.0%} on its top pick) — treat it only as a soft prior."


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
        out.append(f"- Vote distribution:  {_pct_row(rl['distribution'])}")
        out.append(f"- Read: {_interpret_rl(rl['confidence'], rl['entropy_bits'])}")
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
            "| # | Section | Budget | RL pick | need d/b | cov d·b | must-ev | orphans d/b | brief |"
        )
        sep = "|---|---------|-------:|---------|:-------:|:------:|:------:|:----------:|:----:|"
    else:
        header = (
            "| # | Section | Budget | need d/b | cov d·b | must-ev | orphans d/b | brief |"
        )
        sep = "|---|---------|-------:|:-------:|:------:|:------:|:----------:|:----:|"
    out.append(header)
    out.append(sep)

    for i, s in enumerate(secs, 1):
        budget = f"{s['weight']*100:.0f}%"
        need = f"{s['need_depth']}/{s['need_breadth']}"
        cov = f"{s['depth_score']}·{s['breadth_score']}"
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
                f"{must_ev} | {orph} | {brief} |"
            )
        else:
            out.append(
                f"| {i} | {sec_label} | {budget} | {need} | {cov} | "
                f"{must_ev} | {orph} | {brief} |"
            )

    out.append("")
    out.append("Legend:")
    out.append(
        "- **need d/b** — unmet depth / breadth gap pressure (higher = more "
        "missing; includes orphaned guideline anchors)."
    )
    out.append(
        "- **cov d·b** — coverage already achieved (depth out of 8, breadth out of 6)."
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
  2. A per-section table of coverage already achieved vs. what the guideline demands.
     Use this to understand DIRECTION (which sections need depth-first vs.
     breadth-first rounds) — NOT to re-derive whether to escalate.
  3. Article-wide gap economics (unbacked anchors, dominant gap type).

THE REWARD CURVE IS SINGLE-PEAKED
Article reward as a function of preset is unimodal: one optimum, declining on both
sides. The section-scorer's aggregate vote is the reward-trained estimate of that
peak. Stepping above its pick almost always steps down the far side of the curve.
The asymmetry is severe: a correct escalation from the optimum typically gains ~0.03
reward; an over-escalation costs up to 0.7 (past the peak, extra exploration dilutes
the article's guideline-adherence, flow, and structure while buying diminishing
returns on depth and breadth enhancement). The downside is large and sometimes
catastrophic; the upside of an escalation override is almost always small.

DO NOT DERIVE ESCALATION FROM THE GAP TABLE
Coverage gaps (must-ev, unbacked anchors, need_depth) describe what is missing, but
they carry NO information about the reward trade-off. Every article shows dozens of
unbacked anchors and non-zero must-ev — these signals are universally present across
all preset levels and are not predictive of whether escalation actually helps. The
scorer already priced them in against the reward. Re-deriving escalation from the gap
table double-counts signals the scorer already weighed and has a strong systematic
bias toward over-escalation.

ASYMMETRIC OVERRIDE POLICY
  - NEVER choose a preset ABOVE the section-scorer's pick when it votes P1 or higher.
    The scorer already independently catches every genuinely demanding article at the
    correct level (P2/P3) — if it votes P1, standard or deep is almost never correct.
    An upward override of a P1+ vote is almost always wrong.
  - You MAY choose one level BELOW the scorer's pick when the gap table shows most
    high-budget sections are brief-flagged, already well-covered (depth_score >= 6),
    or the vote is highly uncertain (entropy > 1.5 bits, no dominant arm).
  - SINGLE SANCTIONED UPWARD NUDGE (P0 -> P1 only): if the scorer votes P0 skip AND
    its runner-up is P1 light with substantial mass (>= 25% of the vote) AND no
    section individually votes standard or deep — you MAY choose P1 light as cheap
    insurance. If multiple sections individually vote standard/deep (a
    depth-or-nothing pattern), keep P0 — the light middle arm sits in a reward valley
    and will lose reward, not gain it.
  - There is NO valid upward override from P1 to P2, or P2 to P3, regardless of
    what the gap table shows.

USE THE PER-SECTION TABLE FOR DIRECTION, NOT LEVEL
If you choose to run exploration, need_depth / need_breadth tell you which sections
need depth-first vs. breadth-first rounds. Let them inform the composition of the
exploration rounds (depth -> breadth vs. balanced), not the decision to escalate.

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
  1. State what the section-scorer's aggregate vote is and how confident it is.
  2. Check whether any sanctioned override condition is met (see ASYMMETRIC OVERRIDE
     POLICY in your instructions). Remember: never override a P1+ vote upward.
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
        # Deterministic hard-constraint guard (forbidden->skip, required->>=light).
        final_preset, guard_note = _apply_policy_guards(parsed_preset, policy)
        drivers = parsed.get("decision_drivers", [])
        risk_flags = parsed.get("risk_flags", [])
        override_reason = parsed.get("override_reason")
        if guard_note:
            drivers = [*drivers, "policy_guard"]
            risk_flags = [*risk_flags, guard_note]
            override_reason = (
                guard_note if not override_reason else f"{override_reason}; {guard_note}"
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
