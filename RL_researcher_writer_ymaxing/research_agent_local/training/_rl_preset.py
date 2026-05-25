"""Shared RL preset constants and per-section input builder.

This module is intentionally minimal — no heavy imports, no API calls — so it
can be safely imported by any script in the training pipeline without triggering
LLM client initialisation.

Used by:
  generate_digests.py   — defines _RL_INPUT_SYSTEM and build_rl_input
  train_grpo.py         — loads section_oracle.json, tokenizes training groups
  infer.py              — runs the trained model for preset prediction
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Preset vocabulary
# ---------------------------------------------------------------------------

#: Mapping from ordinal index to preset name (skip < light < standard < deep).
PRESET_NAMES: dict[int, str] = {0: "skip", 1: "light", 2: "standard", 3: "deep"}

#: Reverse mapping: preset name → ordinal index.
PRESET_ORDER: dict[str, int] = {v: k for k, v in PRESET_NAMES.items()}

#: Number of exploration rounds per preset name.
PRESET_ROUNDS: dict[str, int] = {"skip": 0, "light": 1, "standard": 2, "deep": 3}

#: Total number of presets (action-space size for the RL model).
NUM_PRESETS: int = 4


# ---------------------------------------------------------------------------
# System prompt (KV-cache friendly — constant across all sections / articles)
# ---------------------------------------------------------------------------

_RL_INPUT_SYSTEM = """\
You are an exploration-preset selector for a research-writing pipeline.
For ONE section of an article you receive a structured digest of available
sources, coverage gaps, and writer constraints, and you output a single
preset choice.

OUTPUT
  Reply with EXACTLY one token: skip, light, standard, or deep.
  No explanation, no quotes, no surrounding text.

PRESET MEANINGS
  skip      No exploration. The exploration phase is skipped entirely;
            only already-collected sources are available to the writer.

  light     1 exploration round with balanced focus:
              · round 1 — balanced (50% depth queries / 50% breadth queries)
            Effective cumulative mix: 50% depth / 50% breadth.

  standard  2 exploration rounds, depth-first then breadth:
              · round 1 — depth-focused  (100% depth queries)
              · round 2 — breadth-focused (100% breadth queries)
            Effective cumulative mix: 50% depth / 50% breadth, but sequenced
            so that the most specific technical gaps are filled before wider
            context is gathered.

  deep      3 exploration rounds, depth-breadth-depth pattern:
              · round 1 — depth-focused  (100% depth queries)
              · round 2 — breadth-focused (100% breadth queries)
              · round 3 — depth-focused  (100% depth queries)
            Effective cumulative mix: ~67% depth / 33% breadth.
            Use when the section has both significant technical gaps and a
            large enough writing budget to absorb the extra material.

<preset_semantics>
IMPORTANT — "skip" means the research pipeline is bypassed; the writer uses
only sources already present in the digest. It does NOT mean the section is
unimportant or should be written briefly.
  - If <research_already_gathered> shows high depth_score and breadth_score,
    "skip" produces the richest possible output: the writer already has
    everything needed, and extra rounds add nothing.
  - Section importance, target_words, and must_cover_depth govern how much
    the WRITER produces; the preset only controls whether more research runs
    first.
  - Choose "skip" when existing coverage is sufficient for the writing budget.
    Choose higher presets only to close genuine, explorable gaps.
</preset_semantics>

INPUT SCHEMA (what each tag means)

<digest_meta>
  Article-level summary. Notable fields:
    <tavily_saturation>           value in [0, 1]. Higher means new web-search
                                  rounds keep finding the same URLs (low
                                  marginal value); lower means new rounds keep
                                  surfacing fresh URLs (high marginal value).

<artefact_registry>
  Code, mermaid, tables, and quotes that have already been extracted from
  sources. Anything listed here can be dropped into the article without
  further research.

<sources>
  Compressed summaries of the source files relevant to this section.

<tavily_yield_per_section>
  Per-section table.
    helping_rounds   how many exploration rounds already contributed to this
                     section. Higher means more research has been done.
    unique_facts     distinct URLs / facts pulled in across rounds.
    duplicate_facts  repeats. High duplicates + many helping_rounds = saturated.

<target_section>
  Two sub-blocks describing what has been gathered and what is still needed.

  <research_already_gathered>
    depth_checklist (8 items): motivation, theoretical_foundations,
      technical_nuances, latest_advancements, limitations_failure_modes,
      implementation_tradeoffs, case_studies_metrics, artefact_available.
      depth_score = count of items with present="yes".
    breadth_checklist (6 items): adjacent_concepts, cross_domain_analogies,
      historical_context, enabling_technologies, industry_applications,
      adjacent_trends. breadth_score = count of items with present="yes".
    orphan_anchors — writing-guideline bullets not yet backed by any source.
      route="depth" | "breadth": exploration can plausibly close these gaps.
      route="unreachable": no web search can supply what is missing.
    HIGH scores + few depth/breadth orphans  →  research is already sufficient.
    LOW scores + orphans routed depth/breadth →  extra rounds can close gaps.

  <research_needed_for_writing .../>  (self-closing; derived from writing
                                       guideline + coverage gap counts)
    need_depth        (8 − depth_score) + 3 × depth-routed orphan count.
                      Higher = more technical gaps to fill before writing.
    need_breadth      (6 − breadth_score) + 3 × breadth-routed orphan count.
    target_words      prose-word budget for this section.
    mandatory_bullets number of bullets the writer must address.
    must_cover_depth  bullets demanding named tools, numbers, benchmarks,
                      or code. Higher = writer needs more specific evidence.
    must_stay_brief   bullets explicitly capped to brief treatment. Higher =
                      less room for new material even when gaps exist.

DECISION DIRECTIONS (qualitative; do NOT apply fixed thresholds)
  - Higher need_depth and / or need_breadth (from <research_needed_for_writing>)
    strengthen the case for more exploration. Cross-check with the scores in
    <research_already_gathered>: low scores confirm the gaps are real.
  - Orphans in <research_already_gathered> routed "depth" or "breadth" point
    at gaps exploration can close. Route "unreachable" cannot be helped.
  - Saturation near 1 or high helping_rounds with diminishing new facts
    weaken the case for additional rounds.
  - Larger target_words, larger mandatory_bullets, and higher must_cover_depth
    (all from <research_needed_for_writing>) raise the writing budget, so a
    higher preset is justified for the same nominal need.
  - Smaller target_words or must_stay_brief > 0 cap how much new material the
    section can absorb, so a lower preset is appropriate even with gaps.
  - "standard" and "deep" differ in their third round: "deep" adds one more
    depth pass, so prefer "deep" only when must_cover_depth is high and the
    word budget is large enough to use the extra technical material.

Use these signals to pick the smallest preset that meaningfully closes the
section's coverage gaps within its writing budget."""


# ---------------------------------------------------------------------------
# Per-section RL input builder
# ---------------------------------------------------------------------------

def build_rl_input(digest: str, target_section_id: str) -> dict[str, str]:
    """Construct the per-section RL input for the preset selector model.

    Returns a dict {"system": ..., "user": ...} suitable for use as a chat
    message pair.  The system message is constant across all sections /
    articles (KV-cache friendly) and contains the schema note + decision
    directions.  The user message is per-section: it contains the digest
    fragments and the target section, with <sources> filtered to only the
    slugs referenced by the target section.
    """
    def _extract_tag(text: str, tag: str) -> str:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(0) if m else f"<{tag}>(not found)</{tag}>"

    digest_meta = _extract_tag(digest, "digest_meta")
    # external_evidence_policy is article-level: "forbidden" short-circuits the
    # entire exploration phase upstream (before the section-level model is called);
    # "allowed"/"required" are passed to the downstream article-level aggregator.
    # Strip it here so the section-level model sees only per-section signals.
    digest_meta = re.sub(
        r"\s*<external_evidence_policy>[^<]*</external_evidence_policy>", "", digest_meta
    )
    artefact_registry = _extract_tag(digest, "artefact_registry")

    tavily_yield = _extract_tag(digest, "tavily_yield_per_section")
    # Filter tavily_yield to the target section's row only — other rows carry no
    # signal for the current selection decision, and saturation is already in
    # digest_meta.  Keep the table header so the model sees column names.
    _ty_inner = re.search(
        r"<tavily_yield_per_section>(.*?)</tavily_yield_per_section>",
        tavily_yield,
        re.DOTALL,
    )
    if _ty_inner:
        _inner = _ty_inner.group(1)
        _hdr = re.search(r"(\| section_id \|[^\n]+\n\|[-|]+\|\n)", _inner)
        _row = re.search(
            rf"(\|\s*{re.escape(target_section_id)}\s*\|[^\n]+)", _inner
        )
        _parts: list[str] = []
        if _hdr:
            _parts.append(_hdr.group(1).rstrip())
        if _row:
            _parts.append(_row.group(1).rstrip())
        if _parts:
            tavily_yield = (
                "<tavily_yield_per_section>\n"
                + "\n".join(_parts)
                + "\n</tavily_yield_per_section>"
            )

    gap_profile_raw = _extract_tag(digest, "gap_profile")
    # Strip the stub placeholder that generate_digests.py leaves unfilled —
    # it is literal noise and provides no signal to the model.
    gap_profile = re.sub(
        r"\s*<exploration_insight>[^<]*</exploration_insight>", "", gap_profile_raw
    )
    # Filter gap_profile to the target section's <section/> row only — other
    # sections' rows add ~400 tokens of irrelevant noise per training group.
    # Extract the target section's gap attributes for <research_needed_for_writing>.
    _rnw_attrs = ""
    _gp_inner = re.search(r"<gap_profile>(.*?)</gap_profile>", gap_profile, re.DOTALL)
    if _gp_inner:
        _rnw_sec = re.search(
            rf'<section\s+id="{re.escape(target_section_id)}"([^/]*)/>',
            _gp_inner.group(1),
        )
        if _rnw_sec:
            _rnw_attrs = _rnw_sec.group(1).strip()

    sec_m = re.search(
        r'(<section\s+id="' + re.escape(target_section_id) + r'"[^>]*>.*?</section>)',
        digest,
        re.DOTALL,
    )
    if not sec_m:
        target_section_block = f'<section id="{target_section_id}">(not found)</section>'
        source_slugs: list[str] = []
    else:
        target_section_block = sec_m.group(1)
        attr_m = re.search(r'sources="([^"]*)"', target_section_block)
        source_slugs = [s.strip() for s in (attr_m.group(1).split(",") if attr_m else [])]
        source_slugs = [s for s in source_slugs if s]

        # Wrap depth_checklist + breadth_checklist + orphan_anchors in
        # <research_already_gathered>, and inject <research_needed_for_writing>
        # before </section> so the model sees gathered vs. needed side-by-side.
        _chk_m = re.search(r'(\n[ \t]*)<depth_checklist', target_section_block)
        _end_m = (
            re.search(r'</orphan_anchors>', target_section_block)
            or re.search(r'<orphan_anchors[^>]*/>', target_section_block)
            or re.search(r'</breadth_checklist>', target_section_block)
        )
        if _chk_m and _end_m and _end_m.start() > _chk_m.start():
            _indent = _chk_m.group(1)  # e.g. "\n  "
            _gathered = target_section_block[_chk_m.start() : _end_m.end()]
            target_section_block = (
                target_section_block[: _chk_m.start()]
                + f"{_indent}<research_already_gathered>"
                + _gathered
                + f"{_indent}</research_already_gathered>"
                + target_section_block[_end_m.end() :]
            )
        if _rnw_attrs:
            # Determine child indentation from the first child element.
            _ci_m = re.search(
                r'\n([ \t]+)<(?:depth_checklist|research_already_gathered)',
                target_section_block,
            )
            _child_indent = _ci_m.group(1) if _ci_m else "  "
            target_section_block = re.sub(
                r'(\n?[ \t]*</section>)\s*$',
                f'\n{_child_indent}<research_needed_for_writing {_rnw_attrs}/>'
                + r'\1',
                target_section_block,
                count=1,
            )

    # Filter artefact_registry to rows whose Source column is in source_slugs.
    # Sections that cite none of their sources' artefacts get an explicit "(none)".
    _ar_inner = re.search(r"<artefact_registry>(.*?)</artefact_registry>", artefact_registry, re.DOTALL)
    if _ar_inner:
        _ar_lines = _ar_inner.group(1).splitlines()
        _hdr_lines = [l for l in _ar_lines if l.startswith("| ID |") or l.startswith("|---")]
        _data_lines = [
            l for l in _ar_lines
            if l.startswith("| A") and any(f"| {slug} |" in l for slug in source_slugs)
        ]
        _body = "\n".join(_hdr_lines + (_data_lines if _data_lines else ["(none)"]))
        artefact_registry = f"<artefact_registry>\n{_body}\n</artefact_registry>"

    all_sources_m = re.search(r"<sources>(.*?)</sources>", digest, re.DOTALL)
    if all_sources_m and source_slugs:
        filtered_parts: list[str] = []
        for slug in source_slugs:
            sm = re.search(
                r'<s slug="' + re.escape(slug) + r'"[^>]*>.*?</s>',
                all_sources_m.group(1),
                re.DOTALL,
            )
            if sm:
                filtered_parts.append(sm.group(0))
        filtered_sources = "<sources>\n" + "\n\n".join(filtered_parts) + "\n</sources>"
    else:
        filtered_sources = "<sources>(no matching sources)</sources>"

    user_message = "\n\n".join([
        digest_meta,
        artefact_registry,
        filtered_sources,
        tavily_yield,
        f"<target_section>\n{target_section_block}\n</target_section>",
        f"<task>\nSelect the exploration preset for section "
        f'"{target_section_id}". Output exactly one token: skip, light, standard, or deep.\n</task>',
    ])

    return {"system": _RL_INPUT_SYSTEM, "user": user_message}
