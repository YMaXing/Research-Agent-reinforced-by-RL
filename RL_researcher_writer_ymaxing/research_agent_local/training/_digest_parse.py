"""Stdlib-only parsers for the v2 XML research digest.

This module is the **single source of truth** for reading article-level and
per-section signals out of ``research_digest.md`` (the v2 XML format produced by
``generate_digests.py``).  It is imported by:

* ``mcp_server`` — ``predict_exploration_preset_tool.py`` builds the article
  evidence packet for the Grok aggregator from these parsers.
* ``training`` — eval / diagnostics scripts that need the same signals.

Design constraints
------------------
* **Stdlib only** (``re``) so it imports cleanly in *either* venv (the
  mcp_server venv has no torch; the training venv does).  Do not add heavy deps.
* **Read-only.**  These functions never run the model and never touch reward
  files (``section_oracle.json``) or per-arm articles.  Everything returned here
  is derivable from a single exploitation pass, which is exactly what is
  available at inference on a brand-new article.  Keeping the parsers reward-free
  is what makes the evidence packet leakage-safe (see the aggregator plan §0.5).

The v2 digest layout these parsers target::

    <digest_meta>
      <article_title>…</article_title>
      <total_sources>13</total_sources>
      <total_artefacts>18</total_artefacts>
      <tavily_saturation>1.0</tavily_saturation>
      <n_orphan_anchors>48</n_orphan_anchors>
      <n_content_sections>6</n_content_sections>
      <external_evidence_policy>allowed</external_evidence_policy>
    </digest_meta>

    <section_coverage>
      <section id="S1::…" self_contained="yes" sources="a,b,c" artefacts="A01,A02">
        <intent>…</intent>
        <depth_checklist depth_score="8"> … </depth_checklist>
        <breadth_checklist breadth_score="6"> … </breadth_checklist>
        <orphan_anchors n_depth="2" n_breadth="1" n_unreachable="0"> … </orphan_anchors>
      </section>
      …
    </section_coverage>

    <gap_profile>
      <section id="S1::…" need_depth="6" need_breadth="3" target_words="450"
               mandatory_bullets="5" must_cover_depth="0" must_stay_brief="0"/>
      …
      <overall>
        <weakest_sections>S4::…, S6::…</weakest_sections>
        <strongest_sections>S1::…, S3::…</strongest_sections>
        <dominant_gap_type>depth</dominant_gap_type>
        <exploration_insight>…</exploration_insight>
      </overall>
    </gap_profile>
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Low-level helpers
# ---------------------------------------------------------------------------


def _block(text: str, tag: str) -> str:
    """Return the inner text of the first ``<tag>…</tag>`` block, or ``""``."""
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
    return m.group(1) if m else ""


def _child_text(block: str, tag: str) -> str:
    """Return the trimmed inner text of a simple ``<tag>…</tag>`` child."""
    m = re.search(rf"<{tag}>(.*?)</{tag}>", block, re.DOTALL)
    return m.group(1).strip() if m else ""


def _to_int(value: str, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _to_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _attr(attrs: str, name: str) -> str:
    """Pull a single ``name="value"`` attribute out of an attribute string."""
    m = re.search(rf'{name}="([^"]*)"', attrs)
    return m.group(1) if m else ""


def _split_csv(value: str) -> list[str]:
    """Split a comma-separated attribute into a clean list (drops empties)."""
    return [s.strip() for s in value.split(",") if s.strip()]


# ---------------------------------------------------------------------------
# sec_id helpers
# ---------------------------------------------------------------------------

_SEC_ID_RE = re.compile(r"^S(\d+)::section-\d+-(.+)$")


def short_label(sec_id: str) -> str:
    """``S6::section-6-key-strategies`` -> ``S6``."""
    m = re.match(r"^(S\d+)::", sec_id)
    return m.group(1) if m else sec_id


def readable_title(sec_id: str) -> str:
    """``S6::section-6-key-strategies-and-tradeoffs`` -> ``key strategies and tradeoffs``.

    Falls back to the raw ``sec_id`` when it does not match the expected shape.
    """
    m = _SEC_ID_RE.match(sec_id)
    if not m:
        return sec_id
    return m.group(2).replace("-", " ").strip()


# ---------------------------------------------------------------------------
# <digest_meta>
# ---------------------------------------------------------------------------


def parse_digest_meta(digest: str) -> dict:
    """Parse the article-level ``<digest_meta>`` block.

    Returns a dict with keys: ``article_title``, ``total_sources``,
    ``total_artefacts``, ``tavily_saturation``, ``n_orphan_anchors``,
    ``n_content_sections``, ``external_evidence_policy``.  Missing fields get
    safe defaults (``external_evidence_policy`` defaults to ``"allowed"``).
    """
    meta = _block(digest, "digest_meta")
    return {
        "article_title": _child_text(meta, "article_title"),
        "total_sources": _to_int(_child_text(meta, "total_sources")),
        "total_artefacts": _to_int(_child_text(meta, "total_artefacts")),
        "tavily_saturation": _to_float(_child_text(meta, "tavily_saturation")),
        "n_orphan_anchors": _to_int(_child_text(meta, "n_orphan_anchors")),
        "n_content_sections": _to_int(_child_text(meta, "n_content_sections")),
        "external_evidence_policy": (
            _child_text(meta, "external_evidence_policy") or "allowed"
        ),
    }


# ---------------------------------------------------------------------------
# <gap_profile>
# ---------------------------------------------------------------------------

#: Per-section self-closing row inside <gap_profile>.
_GAP_SECTION_RE = re.compile(r'<section\s+id="([^"]+)"([^/]*)/>')


def parse_gap_profile_rows(digest: str) -> dict[str, dict]:
    """Parse the per-section rows of ``<gap_profile>``.

    Returns ``{sec_id: {need_depth, need_breadth, target_words,
    mandatory_bullets, must_cover_depth, must_stay_brief}}`` (all ints).
    The ``<overall>`` summary is parsed separately by ``parse_gap_overall``.
    """
    gp = _block(digest, "gap_profile")
    rows: dict[str, dict] = {}
    for sec_id, attrs in _GAP_SECTION_RE.findall(gp):
        rows[sec_id] = {
            "need_depth": _to_int(_attr(attrs, "need_depth")),
            "need_breadth": _to_int(_attr(attrs, "need_breadth")),
            "target_words": _to_int(_attr(attrs, "target_words")),
            "mandatory_bullets": _to_int(_attr(attrs, "mandatory_bullets")),
            "must_cover_depth": _to_int(_attr(attrs, "must_cover_depth")),
            "must_stay_brief": _to_int(_attr(attrs, "must_stay_brief")),
        }
    return rows


def parse_gap_overall(digest: str) -> dict:
    """Parse the ``<overall>`` summary inside ``<gap_profile>``.

    Returns ``{weakest_sections: [sec_id…], strongest_sections: [sec_id…],
    dominant_gap_type: str}``.  Section lists are returned as full sec_ids.
    """
    gp = _block(digest, "gap_profile")
    overall = _block(gp, "overall")
    return {
        "weakest_sections": _split_csv(_child_text(overall, "weakest_sections")),
        "strongest_sections": _split_csv(_child_text(overall, "strongest_sections")),
        "dominant_gap_type": _child_text(overall, "dominant_gap_type"),
    }


# ---------------------------------------------------------------------------
# <section_coverage>
# ---------------------------------------------------------------------------

#: A full <section …> … </section> block inside <section_coverage>.
_COV_SECTION_RE = re.compile(
    r'<section\s+id="([^"]+)"([^>]*)>(.*?)</section>', re.DOTALL
)


def parse_section_coverage(digest: str) -> dict[str, dict]:
    """Parse the per-section coverage state from ``<section_coverage>``.

    Returns ``{sec_id: {self_contained: bool, sources: [...], artefacts: [...],
    intent: str, depth_score: int, breadth_score: int,
    orphans: {depth, breadth, unreachable}}}``.

    ``depth_score`` is out of 8 and ``breadth_score`` is out of 6 (the checklist
    sizes used during digest generation).
    """
    cov_block = _block(digest, "section_coverage")
    out: dict[str, dict] = {}
    for sec_id, attrs, inner in _COV_SECTION_RE.findall(cov_block):
        depth_m = re.search(r'<depth_checklist\s+depth_score="(\d+)"', inner)
        breadth_m = re.search(r'<breadth_checklist\s+breadth_score="(\d+)"', inner)
        orphan_m = re.search(
            r'<orphan_anchors([^>]*)(?:/>|>)', inner
        )
        orphan_attrs = orphan_m.group(1) if orphan_m else ""
        out[sec_id] = {
            "self_contained": _attr(attrs, "self_contained") == "yes",
            "sources": _split_csv(_attr(attrs, "sources")),
            "artefacts": _split_csv(_attr(attrs, "artefacts")),
            "intent": _child_text(inner, "intent"),
            "depth_score": _to_int(depth_m.group(1)) if depth_m else 0,
            "breadth_score": _to_int(breadth_m.group(1)) if breadth_m else 0,
            "orphans": {
                "depth": _to_int(_attr(orphan_attrs, "n_depth")),
                "breadth": _to_int(_attr(orphan_attrs, "n_breadth")),
                "unreachable": _to_int(_attr(orphan_attrs, "n_unreachable")),
            },
        }
    return out


# ---------------------------------------------------------------------------
# Convenience: parse everything in one pass
# ---------------------------------------------------------------------------


def parse_digest(digest: str) -> dict:
    """Parse all article-level + per-section signals from a v2 digest.

    Returns ``{meta, gap_rows, gap_overall, coverage}``.  Convenience wrapper so
    callers do a single call instead of four.
    """
    return {
        "meta": parse_digest_meta(digest),
        "gap_rows": parse_gap_profile_rows(digest),
        "gap_overall": parse_gap_overall(digest),
        "coverage": parse_section_coverage(digest),
    }
