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

INPUT SCHEMA (what each tag means)

<digest_meta>
  Article-level summary. Notable fields:
    <tavily_saturation>           value in [0, 1]. Higher means new web-search
                                  rounds keep finding the same URLs (low
                                  marginal value); lower means new rounds keep
                                  surfacing fresh URLs (high marginal value).
    <external_evidence_policy>
        forbidden  the writer is told NOT to bring in outside research.
                   Extra exploration is wasted no matter the gaps.
        allowed    no restriction (default).
        required   the writer is expected to add external evidence, so
                   exploration carries more weight than its gaps alone imply.

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

<gap_profile>
  Deterministic per-section signals. For each <section/> row:
    need_depth         unmet depth checklist items + 3 * depth-routed orphans
                       (higher = more gaps in technical specifics).
    need_breadth       unmet breadth checklist items + 3 * breadth-routed
                       orphans (higher = more gaps in surrounding concepts).
    target_words       approximate prose budget for the section. Larger budget
                       = more room to absorb new research.
    mandatory_bullets  number of checklist items the writer must address.
                       More bullets = denser section = more research can fit.
    must_cover_depth   bullets that demand concrete examples, numbers, or
                       named tools. Higher = more specific facts needed.
    must_stay_brief    bullets explicitly capped (briefly / one sentence /
                       high-level). Higher = less room for new material.

<target_section>
  The section's full coverage block: depth_checklist (8 items), breadth_checklist
  (6 items), and orphan_anchors with route="depth" | "breadth" | "unreachable".

DECISION DIRECTIONS (qualitative; do NOT apply fixed thresholds)
  - Higher need_depth and / or need_breadth strengthen the case for more
    exploration.
  - Orphans routed "depth" or "breadth" point at gaps that exploration can
    plausibly close. Orphans routed "unreachable" cannot be helped by more
    rounds.
  - Saturation near 1 or high helping_rounds with diminishing new facts
    weaken the case for additional rounds.
  - Larger target_words, larger mandatory_bullets, and higher must_cover_depth
    raise the writing budget, so a higher preset is justified for the same
    nominal need.
  - Smaller target_words or must_stay_brief > 0 cap how much new material the
    section can absorb, so a lower preset is appropriate even with gaps.
  - external_evidence_policy = "forbidden" overrides everything else: choose
    "skip" because no external evidence can be used regardless of gaps.
  - external_evidence_policy = "required" biases toward a higher preset
    because outside evidence is mandatory.
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
    artefact_registry = _extract_tag(digest, "artefact_registry")
    tavily_yield = _extract_tag(digest, "tavily_yield_per_section")
    gap_profile_raw = _extract_tag(digest, "gap_profile")
    # Strip the stub placeholder that generate_digests.py leaves unfilled —
    # it is literal noise and provides no signal to the model.
    gap_profile = re.sub(
        r"\s*<exploration_insight>[^<]*</exploration_insight>", "", gap_profile_raw
    )

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
        gap_profile,
        f"<target_section>\n{target_section_block}\n</target_section>",
        f"<task>\nSelect the exploration preset for section "
        f'"{target_section_id}". Output exactly one token: skip, light, standard, or deep.\n</task>',
    ])

    return {"system": _RL_INPUT_SYSTEM, "user": user_message}
