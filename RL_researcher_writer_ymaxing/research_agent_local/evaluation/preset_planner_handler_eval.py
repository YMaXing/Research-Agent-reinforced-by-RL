"""
Eval-only LLM planner (currently Grok 4.2) for the exploration-preset pipeline.

Lives outside mcp_server/ entirely — nothing here is reachable from the production
predict_exploration_preset tool, which only ever uses the deterministic RL pick +
policy guard (mcp_server/src/app/preset_planner_handler.py::fallback_aggregator).
Used exclusively by evaluation/predict_exploration_preset_eval.py to measure the RL
model's marginal contribution and to regression-test this LLM-planner stage against
the deterministic policy guard.

Cross-imports the production mcp_server handlers (``build_article_evidence``,
``fallback_aggregator``, ``PRESET_NAMES``, ``NUM_PRESETS``) via a sys.path insertion of
the mcp_server/ directory, mirroring how those handlers themselves cross-import
training/_digest_parse.py.
"""

from __future__ import annotations

import json as _json
import logging
import re
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

_EVAL_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _EVAL_DIR.parent  # research_agent_local/
_MCP_SERVER_DIR = _AGENT_DIR / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from src.app.preset_infer_handler import PRESET_NAMES, NUM_PRESETS  # noqa: E402
from src.app.preset_planner_handler import (  # noqa: E402
    build_article_evidence,
    fallback_aggregator,
)

from preset_planner_prompt_eval import (
    PROMPT_PRESET_PLANNER_STANDALONE_SYSTEM,
    PROMPT_PRESET_PLANNER_STANDALONE_USER_TEMPLATE,
    PROMPT_PRESET_PLANNER_SYSTEM,
    PROMPT_PRESET_PLANNER_USER_TEMPLATE,
)

# ---------------------------------------------------------------------------
# Planner LLM model (currently Grok 4.2; swap to change the pipeline's LLM)
# ---------------------------------------------------------------------------
_PLANNER_MODEL = "grok-4.20-0309-reasoning"

# ---------------------------------------------------------------------------
# Calibrated escalation thresholds
# ---------------------------------------------------------------------------
# When the RL aggregate vote is UNCERTAIN (confidence < _DECISIVE_CONFIDENCE or
# entropy > 1.5 bits), the LLM planner may escalate above the RL pick, but only
# when the budget-weighted section-vote mass clears _ESCALATION_MASS_THRESHOLD.
# These MUST stay in sync with the numeric thresholds written into PROMPT_PRESET_PLANNER_SYSTEM.
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
    "capped": (
        "the article's scope is a survey of fixed/named sources — exploration is capped "
        "at light: only skip or light are valid, never standard or deep"
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
    for the LLM-standalone baseline so it decides from the guideline + gaps
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
# Deterministic policy guard (hard constraint clamp)
# ---------------------------------------------------------------------------
# Never trust the LLM to honour the external-evidence policy. After the LLM
# returns a preset, clamp it deterministically so a policy violation is impossible:
#   forbidden -> P0 skip     (exploration output is unusable in the final article)
#   required  -> >= P1 light (external evidence is mandatory)
#   capped    -> <= P1 light (article scope is a survey of fixed/named sources;
#                             the {skip,light} ceiling is a design decision, not a
#                             data-driven one — see A.20 discussion). WITHIN that
#                             ceiling, the skip-vs-light choice is NOT "leave preset
#                             alone if already <= 1" — it always defers to the RL
#                             distribution's own P(skip) vs P(light) preference,
#                             since an in-bounds preset can still disagree with the
#                             distribution (e.g. after the cost-sensitive rule's
#                             adjustment). No distribution available -> leave as-is.
# These are the only three policy directions that have a hard, non-negotiable
# constraint; "allowed" imposes nothing.

def _apply_policy_guards(
    preset: int, policy: str, distribution: list[float] | None = None
) -> tuple[int, str | None]:
    """Clamp a chosen preset to satisfy the external-evidence policy.

    ``distribution`` is the RL aggregate's raw 4-arm probability vector
    ([skip, light, standard, deep]). For "capped" it is the SOLE arbiter of
    the skip-vs-light choice whenever preset is already in {0, 1} -- not just
    a fallback for out-of-bounds presets -- since the incoming preset can
    disagree with the distribution's own ranking. No distribution -> leave
    an in-bounds preset unchanged.

    A standard/deep vote is ALWAYS capped to light regardless of distribution
    (A.20.11: the residual P(skip) vs P(light) split is unreliable there and is
    never used to pick the arm). Every such clamp is marked AMBIGUOUS and
    flagged for review, not just cases where the residual disagrees with light:
    a corpus-wide check (A.20.14) found zero confirmed cases of skip beating
    light in this population, including every case where the residual itself
    favored skip -- so the residual's direction carries no demonstrated signal
    in either direction and is not a basis for trusting light only selectively.

    A skip vote under "required" is likewise ALWAYS elevated to light and marked
    AMBIGUOUS: a corpus-wide check (A.20.15) found no consistent winner among
    light/standard/deep once skip is excluded -- light was clearly best in some
    cases, but in others standard or deep won by a wide margin, and in one case
    light was even the WORST of the three eligible arms (worse than skip itself).

    Returns ``(clamped_preset, note)`` where ``note`` is a short human-readable
    string when a clamp fired, else None.
    """
    if policy == "forbidden" and preset != 0:
        return 0, f"policy=forbidden: clamped P{preset}->P0 skip"
    if policy == "required" and preset < 1:
        if distribution:
            return 1, (
                f"policy=required: clamped P{preset}->P1 light — AMBIGUOUS: no "
                f"data-confirmed default among light/standard/deep for a skip vote "
                f"in this population (A.20.15); RL distribution "
                f"P(light)={distribution[1]:.3f}, P(standard)={distribution[2]:.3f}, "
                f"P(deep)={distribution[3]:.3f}; flagged for review"
            )
        return 1, (
            f"policy=required: clamped P{preset}->P1 light — AMBIGUOUS: no "
            f"data-confirmed default among light/standard/deep for a skip vote "
            f"in this population (A.20.15); flagged for review"
        )
    if policy == "capped":
        if preset > 1:
            if distribution:
                return 1, (
                    f"policy=capped: clamped P{preset}->P1 light — AMBIGUOUS: no "
                    f"data-confirmed case of skip beating light for a standard/deep "
                    f"vote in this population (A.20.14); residual "
                    f"P(skip)={distribution[0]:.3f} vs P(light)={distribution[1]:.3f}, "
                    f"flagged for review"
                )
            return 1, (
                f"policy=capped: clamped P{preset}->P1 light — AMBIGUOUS: no "
                f"data-confirmed case of skip beating light for a standard/deep "
                f"vote in this population (A.20.14); flagged for review"
            )
        if distribution:
            resolved = 1 if distribution[1] >= distribution[0] else 0
            if resolved != preset:
                return resolved, (
                    f"policy=capped: distribution favors P{resolved} "
                    f"{PRESET_NAMES[resolved]} over P{preset} {PRESET_NAMES[preset]} "
                    f"(P(skip)={distribution[0]:.3f} vs P(light)={distribution[1]:.3f})"
                )
    return preset, None


# ---------------------------------------------------------------------------
# Deterministic escalation guard (hard constraint clamp)
# ---------------------------------------------------------------------------
# The planner prompt explicitly states "NEVER escalate a P0 or P1 pick up to P2
# or higher, regardless of vote mass or gap counts" (in both the system prompt
# and the user template) — but a 2026-07-10 held-out backtest showed the LLM
# violating this anyway, using the budget-weighted vote-mass number to
# functionally reconstruct a retired P1->P2 escalation (override_reason:
# "departed from uncertain P1 aggregate to P2 because budget-weighted standard
# mass (68%)..."), undoing a correct cost-rule-adjusted RL pick. A prompt-level
# instruction alone is not reliable enough for this hard boundary; enforce it
# in code, matching the existing forbidden/required policy-guard pattern. The
# still-sanctioned P0->P1 nudge (one level up) is unaffected.

def _apply_escalation_guard(preset: int, rl_preset: int) -> tuple[int, str | None]:
    """Hard block: never let the LLM planner escalate a P0/P1 RL pick all the way to P2+.

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
# LLM planner calls (currently Grok 4.2)
# ---------------------------------------------------------------------------

async def call_grok_planner(
    api_key: str,
    base_url: str,
    evidence: dict,
    article_guideline: str = "",
) -> dict:
    """Call the planner LLM (currently Grok 4.2) for the final exploration-preset decision.

    The LLM receives the guided evidence brief rendered from ``evidence``.
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
    user_msg = PROMPT_PRESET_PLANNER_USER_TEMPLATE.format(
        evidence_brief=render_evidence_brief(
            evidence, include_rl=True, article_guideline=article_guideline
        )
    )

    response = await client.chat.completions.create(
        model=_PLANNER_MODEL,
        messages=[
            {"role": "system", "content": PROMPT_PRESET_PLANNER_SYSTEM},
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
        # (1) never let the LLM escalate a P0/P1 RL pick to P2+ (see
        #     _apply_escalation_guard docstring — a prompt instruction alone was
        #     shown to be insufficient); (2) forbidden->skip, required->>=light,
        #     capped->skip-or-light (distribution-arbitrated, A.20.11).
        escalated_preset, escalation_note = _apply_escalation_guard(parsed_preset, rl_preset)
        final_preset, guard_note = _apply_policy_guards(
            escalated_preset, policy, evidence["rl_aggregate"]["distribution"]
        )
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
            "LLM planner response could not be parsed as JSON; "
            "using deterministic fallback. raw=%s", raw[:300]
        )
        fb = fallback_aggregator(evidence)
        fb["reasoning"] = "LLM JSON parse failed; " + fb["reasoning"]
        return fb


async def call_grok_planner_standalone(
    api_key: str,
    base_url: str,
    evidence: dict,
    article_guideline: str = "",
) -> dict | None:
    """Call the planner LLM (currently Grok 4.2) with NO trained-scorer signal (the LLM-alone baseline).

    The primary-source guideline appendix (when provided) is included identically
    to the full call so the only difference between the two modes is the RL signal.

    Returns a dict with keys: preset, name, reasoning, decision_drivers,
    risk_flags.  Returns None on parsing failure.
    """
    from openai import AsyncOpenAI  # noqa: PLC0415

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    policy = evidence["guideline_context"]["external_evidence_policy"]
    user_msg = PROMPT_PRESET_PLANNER_STANDALONE_USER_TEMPLATE.format(
        evidence_brief=render_evidence_brief(
            evidence, include_rl=False, article_guideline=article_guideline
        )
    )

    response = await client.chat.completions.create(
        model=_PLANNER_MODEL,
        messages=[
            {"role": "system", "content": PROMPT_PRESET_PLANNER_STANDALONE_SYSTEM},
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
        # Deterministic hard-constraint guard (forbidden->skip, required->>=light,
        # capped->[skip,light]). No RL distribution exists in standalone mode
        # (rl_aggregate is None), so a capped clamp here always defaults to light.
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
            "LLM standalone planner response could not be parsed as JSON. raw=%s", raw[:300]
        )
        return None
