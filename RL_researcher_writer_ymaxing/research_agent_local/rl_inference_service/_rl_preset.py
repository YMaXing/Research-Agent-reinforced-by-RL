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
IMPORTANT — 
1. "skip" does NOT mean the section is unimportant or should be
written briefly, it means the exploration phase is skipped because the existing
coverage is sufficient for the writing budget. 
2. "target_words", "must_cover_depth" and "must_stay_brief" govern how much the WRITER produces; 
the preset only controls whether more research runs before writing begins.
</preset_semantics>

INPUT SCHEMA (what each tag means)

<digest_meta>
  Article-level summary.

<artefact_registry>
  Code, mermaid, tables, and quotes already extracted from sources. Anything
  listed here is immediately usable by the writer without further research.
  A populated registry reduces the need for depth exploration on
  evidence-heavy sections (must_cover_depth > 0).

<sources>
  Compressed summaries of the source files relevant to this section.

<target_section>
  Two sub-blocks describing the section's coverage state and writing requirements.

  <coverage_status>
    depth_checklist — single-line: depth="N/8" gaps="comma-list of uncovered
      items". Items: motivation, theoretical_foundations, technical_nuances,
      latest_advancements, limitations_failure_modes, implementation_tradeoffs,
      case_studies_metrics, artefact_available.
    breadth_checklist — single-line: breadth="N/6" gaps="comma-list of uncovered
      items". Items: adjacent_concepts, cross_domain_analogies,
      historical_context, enabling_technologies, industry_applications,
      adjacent_trends.
    writing_gaps — guideline bullets not yet backed by any source.
      Each <gap route="depth"|"breadth" item="..."/> is a writing bullet
      that exploration can provide evidence for.
    HIGH scores + empty checklist gaps + no writing_gaps  →  research is already sufficient.
    LOW scores / non-empty checklist gaps / writing_gaps present  →  extra rounds can help.

  <section_profile .../>  (self-closing; derived from coverage gaps and writing
                           guideline constraints)
    need_depth        (8 − depth_score) + 3 × depth-routed writing_gaps count.
                      Higher = more technical gaps to fill before writing.
    need_breadth      (6 − breadth_score) + 3 × breadth-routed writing_gaps count.
    target_words      prose-word budget for this section.
    must_cover_depth  bullets demanding named tools, numbers, benchmarks,
                      or code. Higher = writer needs more specific evidence.
    must_stay_brief   bullets explicitly capped to brief treatment. Higher =
                      less room for new material even when gaps exist.
    <evidence_required count="N"> (only present when must_cover_depth > 0)
      N bullets require specific named evidence. Signals that depth research
      has direct, concrete payoff.

<preset_signals>
  Compact one-liner derived from <target_section> (present when available).
    gathered="depth:N/8 breadth:N/6"   — current checklist scores.
    needed="depth:N breadth:N"         — gaps to fill (= need_depth / need_breadth).
    budget="words:N must_cover_depth:N must_stay_brief:N" — writing constraints.
  Use as a quick cross-check against the detail in <target_section>.

DECISION DIRECTIONS (signals indicate direction — do not apply fixed thresholds)
  Primary signals: need_depth and need_breadth (from <preset_signals> or
  <section_profile>). Secondary confirmation: non-empty checklist gaps= lists
  and <gap> count in <writing_gaps>.

  Coverage level — how much research is already in place:
    · High gathered scores (depth N/8 and breadth N/6 near their ceilings),
      empty checklist gaps= lists, and no <writing_gaps> entries → push toward lower
      presets. Well-covered sections gain little from further exploration.
    · Low gathered scores, non-empty checklist gaps=, or <writing_gaps> entries present →
      push toward higher presets. Each <gap> in <writing_gaps> is a writing
      bullet with no source backing that exploration can provide.

  Gap shape — what kind of exploration fits best:
    · need_depth >> need_breadth → favour presets that front-load depth queries;
      the depth-first round structures fit better than a balanced single round.
    · need_depth and need_breadth both significant and roughly equal → a balanced
      or depth-first structure both work; total gap size governs the level.
    · need_breadth >> need_depth → a balanced or breadth-oriented approach
      suffices; extra depth passes add less value.

  Writing budget — how much new material the section can absorb:
    · Large target_words → push toward higher presets; the section has room
      to incorporate extra findings.
    · Small target_words or must_stay_brief > 0 → push toward lower presets;
      extra rounds yield material the section cannot use.
    · High must_cover_depth → named tools, benchmarks, or numbers are required;
      depth exploration has direct payoff; push toward higher, depth-heavy presets.
      Even when need_depth is low, high must_cover_depth is a signal that current
      sources may be too general to supply the specific named evidence some bullets
      demand — treat it as independent pressure toward deeper exploration.

  Combining signals:
    Signals compound — large gaps, high must_cover_depth, and a large budget
    together create strong upward pressure; near-complete coverage and a small
    budget create strong downward pressure. When signals conflict, the budget acts
    as a ceiling: exploration rounds that produce material the section cannot
    absorb offer no benefit regardless of gap size.

  Choose the lowest preset the combined signal pressure genuinely justifies."""


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
    digest_meta = re.sub(r"\s*<tavily_saturation>[^<]*</tavily_saturation>", "", digest_meta)
    digest_meta = re.sub(r"\s*<n_orphan_anchors>[^<]*</n_orphan_anchors>", "", digest_meta)
    artefact_registry = _extract_tag(digest, "artefact_registry")

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
            # Strip mandatory_bullets — not an exploration-relevant signal.
            _rnw_attrs = re.sub(r'\s*mandatory_bullets="\d+"', '', _rnw_attrs)

    depth_score = 0
    breadth_score = 0
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

        # Wrap depth_checklist + breadth_checklist + writing_gaps in
        # <coverage_status>, and inject <section_profile>
        # before </section> so the model sees coverage state and requirements together.
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
                + f"{_indent}<coverage_status>"
                + _gathered
                + f"{_indent}</coverage_status>"
                + target_section_block[_end_m.end() :]
            )
        if _rnw_attrs:
            # Determine child indentation from the first child element.
            _ci_m = re.search(
                r'\n([ \t]+)<(?:depth_checklist|coverage_status)',
                target_section_block,
            )
            _child_indent = _ci_m.group(1) if _ci_m else "  "
            target_section_block = re.sub(
                r'(\n?[ \t]*</section>)\s*$',
                f'\n{_child_indent}<section_profile {_rnw_attrs}/>'
                + r'\1',
                target_section_block,
                count=1,
            )
            # P4: inject <evidence_required> after <section_profile> when mcd > 0
            _mcd_m = re.search(r'must_cover_depth="(\d+)"', _rnw_attrs)
            _mcd = int(_mcd_m.group(1)) if _mcd_m else 0
            if _mcd > 0:
                target_section_block = target_section_block.replace(
                    f'<section_profile {_rnw_attrs}/>',
                    f'<section_profile {_rnw_attrs}/>'
                    f'\n{_child_indent}<evidence_required count="{_mcd}">'
                    f'{_mcd} mandatory bullet{"s" if _mcd != 1 else ""} require'
                    f' specific named evidence (tools, papers, benchmarks, or numbers).'
                    f'</evidence_required>',
                )
        # P1: Compress depth_checklist to single-line tag
        _dc_m = re.search(r'<depth_checklist[^>]*>(.*?)</depth_checklist>', target_section_block, re.DOTALL)
        if _dc_m:
            _dc_score_m = re.search(r'depth_score="(\d+)"', _dc_m.group(0))
            depth_score = int(_dc_score_m.group(1)) if _dc_score_m else 0
            _dc_gaps = re.findall(r'<item name="([^"]+)" present="no"', _dc_m.group(1))
            target_section_block = target_section_block.replace(
                _dc_m.group(0),
                f'<depth_checklist depth="{depth_score}/8" gaps="{",".join(_dc_gaps)}"/>',
                1,
            )
        # P1: Compress breadth_checklist to single-line tag
        _bc_m = re.search(r'<breadth_checklist[^>]*>(.*?)</breadth_checklist>', target_section_block, re.DOTALL)
        if _bc_m:
            _bc_score_m = re.search(r'breadth_score="(\d+)"', _bc_m.group(0))
            breadth_score = int(_bc_score_m.group(1)) if _bc_score_m else 0
            _bc_gaps = re.findall(r'<item name="([^"]+)" present="no"', _bc_m.group(1))
            target_section_block = target_section_block.replace(
                _bc_m.group(0),
                f'<breadth_checklist breadth="{breadth_score}/6" gaps="{",".join(_bc_gaps)}"/>',
                1,
            )
        # P2: Strip n_unreachable from orphan_anchors and condense <orphan> children to <gap> tags
        target_section_block = re.sub(
            r'(<orphan_anchors[^>]*?)\s*n_unreachable="\d+"',
            r'\1',
            target_section_block,
        )
        _oa_m = re.search(r'<orphan_anchors([^>]*)>(.*?)</orphan_anchors>', target_section_block, re.DOTALL)
        if _oa_m:
            _oa_gaps = re.findall(r'<orphan route="([^"]+)"[^>]*bullet="([^"]+)"', _oa_m.group(2))
            _oa_lines = ''.join(f'\n    <gap route="{r}" item="{b}"/>' for r, b in _oa_gaps)
            target_section_block = target_section_block.replace(
                _oa_m.group(0),
                f'<writing_gaps{_oa_m.group(1)}>{_oa_lines}\n  </writing_gaps>',
                1,
            )
        # Rename any remaining self-closing <orphan_anchors/> → <writing_gaps/>
        target_section_block = target_section_block.replace(
            '<orphan_anchors', '<writing_gaps'
        ).replace('</orphan_anchors>', '</writing_gaps>')

    # P3: Build <preset_signals> from gathered scores + writing budget
    _ps = ""
    if _rnw_attrs:
        _rv: dict[str, str] = {}
        for _n in ("need_depth", "need_breadth", "target_words",
                   "must_cover_depth", "must_stay_brief"):
            _m2 = re.search(rf'{_n}="(\d+)"', _rnw_attrs)
            _rv[_n] = _m2.group(1) if _m2 else "0"
        _ps = (
            f'<preset_signals'
            f' gathered="depth:{depth_score}/8 breadth:{breadth_score}/6"'
            f' needed="depth:{_rv["need_depth"]} breadth:{_rv["need_breadth"]}"'
            f' budget="words:{_rv["target_words"]}'
            f' must_cover_depth:{_rv["must_cover_depth"]}'
            f' must_stay_brief:{_rv["must_stay_brief"]}"/>'
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
        if _data_lines:
            _body = "\n".join(_hdr_lines + _data_lines)
            artefact_registry = f"<artefact_registry>\n{_body}\n</artefact_registry>"
        else:
            artefact_registry = '<artefact_registry n="0"/>'

    # Build compact sources_summary (slug + type only) — full source text is
    # not needed for preset selection and creates a length confounder across
    # variants (standard digests have much longer per-source summaries than
    # minimal/demanding variants of the same article).  The downstream writer
    # LLM receives the full digest with all <sources> content.
    all_sources_m = re.search(r"<sources>(.*?)</sources>", digest, re.DOTALL)
    if all_sources_m and source_slugs:
        _sm_parts: list[str] = []
        for slug in source_slugs:
            sm = re.search(
                r'<s slug="' + re.escape(slug) + r'"([^>]*)>',
                all_sources_m.group(1),
            )
            if sm:
                _sm_parts.append(f'  <s slug="{slug}"{sm.group(1)}/>')
        sources_summary = (
            f'<sources_summary n="{len(_sm_parts)}">\n'
            + "\n".join(_sm_parts)
            + "\n</sources_summary>"
        ) if _sm_parts else '<sources_summary n="0"/>'
    else:
        sources_summary = f'<sources_summary n="{len(source_slugs)}"/>'

    user_message = "\n\n".join(filter(None, [
        digest_meta,
        artefact_registry,
        sources_summary,
        f"<target_section>\n{target_section_block}\n</target_section>",
        _ps,
        f"<task>\nSelect the exploration preset for section "
        f'"{target_section_id}". Output exactly one token: skip, light, standard, or deep.\n</task>',
    ]))

    return {"system": _RL_INPUT_SYSTEM, "user": user_message}
