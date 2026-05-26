"""Phase 2c — Exploitation Digest Generator (v2)

Generates structured exploitation digests for each training article.
These digests serve as compact context (~4.7K tokens) for the RL policy model
(Qwen3-4B) to select exploration presets from.

Pipeline (8 stages):
  0. EXTRACT   — Deterministic artefact extraction + placeholder injection
  1. COLLECT   — Read all source files from rl_training_data/bases/<article>/.research/
  2. COMPRESS  — Summarize each source to ~250-700 tokens (parallel async, semaphore-limited)
  2b. INDEX    — Build section→source TF-IDF index + detect orphan anchors
  2c. FEATURES — LLM-extract variant-agnostic guideline features (target_words,
                 mandatory_bullets, must_cover_depth, must_stay_brief per section
                 + external_evidence_policy per article). Variant names are
                 never passed to the LLM.
  3. ASSEMBLE  — Build XML-tagged context for Stage 4
  4. GENERATE  — Single API call → XML digest with per-section checklist coverage
  5. VALIDATE  — Deterministic post-processing: recount scores, build gap_profile
                 (with feature attrs injected), compute 2D preset oracle,
                 insert external_evidence_policy into digest_meta
  6. STORE     — Write research_digest.md, section_oracle.json,
                 guideline_features.json under rl_training_data/bases/<article>/

Usage (from research_agent_local/):
  uv run --project mcp_client python training/generate_digests.py
  uv run --project mcp_client python training/generate_digests.py --articles 02_workflows_vs_agents
  uv run --project mcp_client python training/generate_digests.py --dry-run
  uv run --project mcp_client python training/generate_digests.py --force

Depth checklist items (from PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS):
  motivation, theoretical_foundations, technical_nuances, latest_advancements,
  limitations_failure_modes, implementation_tradeoffs, case_studies_metrics, artefact_available

Breadth checklist items:
  adjacent_concepts, cross_domain_analogies, historical_context,
  enabling_technologies, industry_applications, adjacent_trends
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import html
import json
import logging
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Paths and env loading
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent          # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent         # RL_researcher_writer_ymaxing/
_ENV_FILE = _AGENT_DIR / "mcp_client" / ".env"
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

load_dotenv(_ENV_FILE, override=False)

import os  # noqa: E402 (must come after dotenv)

_XAI_API_KEY = os.environ.get("XAI_API_KEY")
_XAI_BASE_URL = os.environ.get("XAI_BASE_URL", "https://api.x.ai/v1")
_ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")  # optional; used for Layer-3 fallback

if not _XAI_API_KEY:
    sys.exit(
        "ERROR: XAI_API_KEY not found. "
        f"Add it to {_ENV_FILE} or set it as an environment variable."
    )

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
MODEL = "grok-4-1-fast-reasoning"
_ANTHROPIC_MODEL = "claude-opus-4-5"  # Layer-3 fallback model

_COMPRESS_CONCURRENCY = 5
_MAX_SOURCE_CHARS = 80_000

_DEPTH_ITEMS = [
    "motivation",
    "theoretical_foundations",
    "technical_nuances",
    "latest_advancements",
    "limitations_failure_modes",
    "implementation_tradeoffs",
    "case_studies_metrics",
    "artefact_available",
]

_BREADTH_ITEMS = [
    "adjacent_concepts",
    "cross_domain_analogies",
    "historical_context",
    "enabling_technologies",
    "industry_applications",
    "adjacent_trends",
]

_SKIP_SECTION_KEYWORDS = {
    "global context",
    "anchoring",
    "achoring",  # typo present in some guidelines
    "narrative flow",
    "lesson outline",
    "outline",
    "golden sources",
    "other sources",
    "article code",
    "brevity requirements",
    "additional requirements",
}

# Recognized code language tags — only fenced blocks with these langs are extracted as artefacts.
_CODE_LANGS = frozenset({
    "python", "py", "javascript", "js", "typescript", "ts", "bash", "sh",
    "json", "yaml", "yml", "html", "css", "java", "go", "rust", "c", "cpp",
    "sql", "r", "ruby", "php", "swift", "kotlin", "scala", "perl", "lua",
    "dockerfile", "makefile", "toml", "ini", "xml", "markdown", "md",
    "text", "txt", "plain", "console", "terminal", "output", "pseudocode",
})

_BASE_ARTICLES: dict[str, str] = {
    "02_workflows_vs_agents": "Workflows vs. Agents",
    "03_context_engineering": "Context Engineering",
    "05_workflow_patterns": "Workflow Patterns",
    "06_tools": "Tools",
    "08_react_practice": "ReAct in Practice",
    "09_RAG": "Retrieval-Augmented Generation",
    "10_memory_knowledge_access": "Memory and Knowledge Access",
    "11_multimodal": "Multimodal AI",
}

# Auto-register variant directories (__var_minimal, __var_standard, __var_demanding)
# so the CLI can target any variant present under rl_training_data/bases/.
ARTICLES: dict[str, str] = {}
for _slug, _title in _BASE_ARTICLES.items():
    ARTICLES[_slug] = _title
    for _v in ("minimal", "standard", "demanding"):
        ARTICLES[f"{_slug}__var_{_v}"] = f"{_title} ({_v} variant)"

# ---------------------------------------------------------------------------
# Text normalization helpers
# ---------------------------------------------------------------------------

def _normalize_text(text: str) -> str:
    """Unescape HTML entities and normalize Unicode quotes to ASCII."""
    text = html.unescape(text)
    return (
        text.replace('\u201c', '"').replace('\u201d', '"')
            .replace('\u2018', "'").replace('\u2019', "'")
    )


# ---------------------------------------------------------------------------
# Helpers: section ID + slug
# ---------------------------------------------------------------------------

def _make_section_id(n: int, title: str) -> str:
    """Return canonical section ID like S3::context-engineering-overview."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"S{n}::{slug}"


def _extract_content_sections(guideline: str) -> list[tuple[int, str]]:
    """Return (1-indexed-n, title) for all content sections (skip preamble/meta)."""
    sections: list[tuple[int, str]] = []
    n = 0
    for line in guideline.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            if not any(kw in title.lower() for kw in _SKIP_SECTION_KEYWORDS):
                n += 1
                sections.append((n, title))
    return sections


def _extract_all_anchors(guideline: str) -> list[dict[str, str]]:
    """
    Extract all bullet-point anchors from content sections.
    Returns list of {anchor, section_id, section_title}.
    An anchor is any non-empty bullet (- or *) in a content section,
    up to 120 chars, trimmed of markdown bold markers.
    """
    content_sections = _extract_content_sections(guideline)
    if not content_sections:
        return []

    lines = guideline.splitlines()
    cs_set = {t for _, t in content_sections}
    cs_n_map = {t: n for n, t in content_sections}

    anchors: list[dict[str, str]] = []
    current_sec: tuple[int, str] | None = None

    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip()
            if title in cs_set:
                current_sec = (cs_n_map[title], title)
            else:
                current_sec = None
            continue

        if current_sec is None:
            continue

        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = stripped[2:].strip()
            text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
            text = _normalize_text(text)
            text = text[:120].strip()
            if len(text) >= 10:
                n, title = current_sec
                anchors.append({
                    "anchor": text,
                    "section_id": _make_section_id(n, title),
                    "section_title": title,
                })

    return anchors


# ---------------------------------------------------------------------------
# Stage 0: EXTRACT ARTEFACTS (deterministic)
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(
    r"(?P<indent>[ \t]*)(?P<fence>```|~~~)(?P<lang>[^\n]*)\n(?P<body>.*?)(?P=fence)",
    re.DOTALL,
)
_MERMAID_RE = re.compile(
    r"(?P<indent>[ \t]*)```mermaid\n(?P<body>.*?)```",
    re.DOTALL,
)
_TABLE_RE = re.compile(
    r"(?:^\|.+\|\n){3,}",
    re.MULTILINE,
)
_BLOCKQUOTE_RE = re.compile(
    r"(?:^>[ \t]?.+\n){2,}",
    re.MULTILINE,
)


def _topic_keywords(body: str, surrounding: str = "") -> str:
    """Extract 3-5 lowercase topic keywords, preferring artefact body over surrounding prose."""
    source = body if body.strip() else surrounding
    words = re.findall(r"[a-zA-Z]{4,}", source.lower())
    stopwords = {
        "this", "that", "with", "from", "have", "been", "will", "which",
        "they", "their", "there", "when", "also", "some", "more", "into",
        "about", "each", "such", "what", "your", "code", "example",
        "then", "often", "just", "like", "than", "here", "where", "would",
        "could", "should", "think", "happen", "make", "want", "need",
        "give", "take", "know", "look", "come", "does", "dont", "using",
        "used", "uses", "many", "much", "very", "being", "other", "while",
        "after", "before", "these", "those", "above", "below", "first",
        "second", "third", "note", "type", "name", "value", "data",
        "list", "item", "line", "file", "function", "class", "object",
        "string", "number", "array", "output", "input", "result",
        "return", "error", "test", "true", "false",
    }
    seen: set[str] = set()
    keywords: list[str] = []
    for w in words:
        if w not in stopwords and w not in seen:
            seen.add(w)
            keywords.append(w)
            if len(keywords) == 5:
                break
    return ",".join(keywords) if keywords else "general"


def extract_artefacts(
    source_slug: str,
    content: str,
    global_registry: list[dict[str, Any]],
    seen_hashes: dict[str, str],
    per_source_cap: int = 10,
) -> str:
    """
    Extract fenced code, mermaid, tables, and long blockquotes from content.
    Mutates global_registry and seen_hashes in-place.
    Returns modified_content_with_placeholders.

    Deduplication: artefacts whose first 120 chars hash matches an already-seen
    artefact are replaced with a reference to the existing ID (no new row added).
    Per-source cap: at most per_source_cap new artefacts are added per source file.
    Only fenced blocks with a recognized language tag (_CODE_LANGS) are extracted.
    """
    source_count = 0
    modified = content

    def _add(body: str, artefact_type: str, surrounding: str) -> str:
        nonlocal source_count
        h = hashlib.md5(body[:120].encode(), usedforsecurity=False).hexdigest()[:16]
        if h in seen_hashes:
            existing_id = seen_hashes[h]
            return f"[ARTEFACT_{existing_id}: {artefact_type}, dup]"
        if source_count >= per_source_cap:
            return body  # leave in place, don't extract
        source_count += 1
        idx = len(global_registry) + 1
        art_id = f"A{idx:02d}"
        seen_hashes[h] = art_id
        lines = body.splitlines()
        first_line = body.strip().splitlines()[0] if body.strip() else ""
        preview = first_line[:40] if first_line else (lines[0][:40] if lines else "")
        kw = _topic_keywords(first_line, surrounding)
        global_registry.append({
            "id": art_id,
            "source_slug": source_slug,
            "type": artefact_type,
            "topic_keywords": kw,
            "line_count": len(lines),
            "preview": preview,
        })
        return f"[ARTEFACT_{art_id}: {artefact_type}, {len(lines)} lines, topic={kw}]"

    # Process mermaid first (subset of fenced, so catch before generic fence)
    def _replace_mermaid(m: re.Match) -> str:
        body = m.group("body")
        surrounding = modified[max(0, m.start() - 200): m.start()]
        return _add(body, "mermaid", surrounding)

    modified = _MERMAID_RE.sub(_replace_mermaid, modified)

    # Generic fenced code blocks — only extract blocks with a recognized language tag
    def _replace_fence(m: re.Match) -> str:
        lang = m.group("lang").strip().lower()
        if lang == "mermaid":
            return m.group(0)  # already handled above
        if not lang or lang not in _CODE_LANGS:
            return m.group(0)  # skip: empty or unrecognized lang (e.g. XML prose blocks)
        body = m.group("body")
        surrounding = modified[max(0, m.start() - 200): m.start()]
        return _add(body, f"code:{lang}", surrounding)

    modified = _FENCE_RE.sub(_replace_fence, modified)

    # Markdown tables (>=3 rows)
    def _replace_table(m: re.Match) -> str:
        surrounding = modified[max(0, m.start() - 200): m.start()]
        return _add(m.group(0), "table", surrounding) + "\n"

    modified = _TABLE_RE.sub(_replace_table, modified)

    # Long blockquotes (>=2 consecutive lines)
    def _replace_quote(m: re.Match) -> str:
        surrounding = modified[max(0, m.start() - 200): m.start()]
        return _add(m.group(0), "quote", surrounding) + "\n"

    modified = _BLOCKQUOTE_RE.sub(_replace_quote, modified)

    return modified


def extract_all_artefacts(
    sources: dict,
) -> tuple[dict, list[dict[str, Any]]]:
    """
    Run Stage 0 on every source file.
    Returns (sources_with_placeholders, global_artefact_registry).
    Deduplication and per-source caps are applied globally across all source files.
    """
    global_registry: list[dict[str, Any]] = []
    seen_hashes: dict[str, str] = {}  # content_hash[:16] → first artefact_id
    sources_stripped: dict = {
        "guideline": sources["guideline"],
        "tavily_results": sources["tavily_results"],
        "full_queries": sources["full_queries"],
    }

    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        stripped_bucket: dict[str, str] = {}
        for fname, content in sources[source_type].items():
            slug = fname[:-3] if fname.endswith(".md") else fname
            modified = extract_artefacts(slug, content, global_registry, seen_hashes)
            stripped_bucket[fname] = modified
        sources_stripped[source_type] = stripped_bucket

    return sources_stripped, global_registry


def _format_artefact_registry_md(registry: list[dict[str, Any]]) -> str:
    if not registry:
        return "| ID | Source | Type | Topic | Lines | Preview |\n|----|----|----|----|----|----|\\n(none)"
    rows = ["| ID | Source | Type | Topic | Lines | Preview |", "|----|----|----|----|----|----|"]
    for e in registry:
        preview = e["preview"].replace("|", "\\|")
        rows.append(
            f"| {e['id']} | {e['source_slug']} | {e['type']} "
            f"| {e['topic_keywords']} | {e['line_count']} | {preview} |"
        )
    return "\n".join(rows)


def _drop_unreferenced_artefacts(digest: str) -> str:
    """Remove artefact registry rows for artefacts not referenced elsewhere in the digest."""
    registry_re = re.compile(r'(<artefact_registry>)(.*?)(</artefact_registry>)', re.DOTALL)
    m = registry_re.search(digest)
    if not m:
        return digest
    # Collect all A## IDs referenced OUTSIDE the registry block
    outside = digest[:m.start()] + digest[m.end():]
    referenced_ids = set(re.findall(r'\bA\d{2}\b', outside))
    # Filter registry table rows, keeping headers/separators and referenced rows
    registry_content = m.group(2)
    lines = registry_content.split('\n')
    kept = []
    for line in lines:
        id_m = re.match(r'\|\s*(A\d+)', line.strip())
        if id_m:
            if id_m.group(1) in referenced_ids:
                kept.append(line)
            # else: silently drop unreferenced artefact row
        else:
            kept.append(line)  # keep header and separator rows
    new_registry = m.group(1) + '\n'.join(kept) + m.group(3)
    return digest[:m.start()] + new_registry + digest[m.end():]


# ---------------------------------------------------------------------------
# Guideline feature extraction (variant-agnostic numeric signals)
#
# The hard constraint for this stage is that variant names
# (minimal / standard / demanding) must NEVER appear in the prompt or the
# returned features. The LLM only sees the guideline text; it infers all
# signals purely from directive language, word-count cues, and bullet
# structure. Differences across the three variants of the same article come
# from the underlying guideline text itself, not from any variant label.
# ---------------------------------------------------------------------------

_FEATURES_SYSTEM = """\
You parse article-writing guidelines into structured numeric constraints.
Read ONLY the guideline text. Infer all signals from directive language,
explicit word-count requirements, bullet structure, and brevity / depth
modifiers (e.g., "briefly", "in-depth", "with concrete numbers", "skim").
Output strict JSON exactly matching the requested shape. No preamble, no
markdown wrapper, no commentary."""

_FEATURES_USER_TEMPLATE = """\
Article: {article_title}

The content sections (1-indexed) are:
{section_listing}

Below is the FULL guideline. Read it carefully and extract numeric features
for every listed content section, plus one article-wide policy flag.

PER-SECTION FEATURES (all non-negative integers; use 0 when no signal)

  target_words         Estimated target word count for the section's prose.
                       - If the guideline states an explicit count (e.g.
                         "Target: ~250 words" or "300-400 words"), use it
                         (midpoint for a range).
                       - Otherwise translate qualitative cues:
                           "briefly" / "one sentence"   -> 80
                           "concise paragraph"           -> 150
                           "moderate" / unmarked         -> 250
                           "in-depth" / "detailed"       -> 500
                           "extensive" / "comprehensive" -> 800
                       - 0 only if there is truly no length signal at all.

  mandatory_bullets    Number of bullets / checklist items under the section
                       header that the writer MUST address. Skip bullets
                       explicitly marked optional / nice-to-have.

  must_cover_depth     Of those mandatory bullets, how many demand SPECIFIC
                       depth: named tools, named papers / authors, numbers,
                       benchmarks, code, reproducible parameters, concrete
                       failure modes. Bullets that say things like "with
                       examples", "name the algorithm", "cite a benchmark",
                       "include code", "list the trade-offs" count here.

  must_stay_brief      Of those mandatory bullets, how many are explicitly
                       capped (modifiers: "briefly", "succinctly", "one
                       sentence", "high-level only", "skim", "do not
                       elaborate", "summary only").

ARTICLE-WIDE FEATURE

  external_evidence_policy
    "forbidden"  guideline tells the writer to stick to supplied / golden
                 sources and NOT to bring in outside research.
    "allowed"    guideline neither forbids nor requires outside evidence
                 (this is the default for most guidelines).
    "required"   guideline explicitly demands the writer cite external
                 sources, fresh benchmarks, or recent papers beyond the
                 supplied set.

OUTPUT — exactly this JSON shape (use the section IDs from the listing above):

{{
  "external_evidence_policy": "forbidden|allowed|required",
  "sections": {{
    "S1::...": {{"target_words": 0, "mandatory_bullets": 0, "must_cover_depth": 0, "must_stay_brief": 0}},
    "S2::...": {{"target_words": 0, "mandatory_bullets": 0, "must_cover_depth": 0, "must_stay_brief": 0}}
  }}
}}

<guideline>
{guideline}
</guideline>"""


def _clamp_int(v: Any, lo: int, hi: int) -> int:
    """Coerce a JSON value to int and clamp into [lo, hi]; return 0 on failure."""
    try:
        x = int(v)
    except (TypeError, ValueError):
        return 0
    return max(lo, min(hi, x))


def _empty_features(content_sections: list[tuple[int, str]]) -> dict[str, Any]:
    return {
        "external_evidence_policy": "allowed",
        "sections": {
            _make_section_id(n, t): {
                "target_words": 0,
                "mandatory_bullets": 0,
                "must_cover_depth": 0,
                "must_stay_brief": 0,
            }
            for n, t in content_sections
        },
    }


async def extract_guideline_features(
    client,
    article_title: str,
    guideline: str,
    content_sections: list[tuple[int, str]],
    dry_run: bool,
) -> dict[str, Any]:
    """
    Single LLM call that parses the guideline into variant-agnostic numeric
    signals. The LLM does not know which variant this is; differentiation
    between minimal / standard / demanding arises solely from the guideline
    text. Returns a sanitized dict; falls back to all-zeros on any error.
    """
    fallback = _empty_features(content_sections)
    if dry_run or not content_sections:
        return fallback

    section_listing = "\n".join(
        f"  {_make_section_id(n, t)}: {t}" for n, t in content_sections
    )

    try:
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": _FEATURES_SYSTEM},
                {
                    "role": "user",
                    "content": _FEATURES_USER_TEMPLATE.format(
                        article_title=article_title,
                        section_listing=section_listing,
                        guideline=guideline,
                    ),
                },
            ],
            max_tokens=2048,
            response_format={"type": "json_object"},
        )
        raw = response.choices[0].message.content.strip()
        parsed = json.loads(raw)
    except Exception as e:
        log.warning(f"    extract_guideline_features failed ({e}); using fallback.")
        return fallback

    policy = parsed.get("external_evidence_policy", "allowed")
    if policy not in ("forbidden", "allowed", "required"):
        policy = "allowed"

    raw_secs = parsed.get("sections", {})
    if not isinstance(raw_secs, dict):
        raw_secs = {}

    sections_out: dict[str, dict[str, int]] = {}
    for n, t in content_sections:
        sid = _make_section_id(n, t)
        row = raw_secs.get(sid)
        if not isinstance(row, dict):
            row = {}
        sections_out[sid] = {
            "target_words": _clamp_int(row.get("target_words", 0), 0, 5000),
            "mandatory_bullets": _clamp_int(row.get("mandatory_bullets", 0), 0, 50),
            "must_cover_depth": _clamp_int(row.get("must_cover_depth", 0), 0, 50),
            "must_stay_brief": _clamp_int(row.get("must_stay_brief", 0), 0, 50),
        }

    return {"external_evidence_policy": policy, "sections": sections_out}


# ---------------------------------------------------------------------------
# Stage 1: COLLECT
# ---------------------------------------------------------------------------

def _read_md_dir(directory: Path) -> dict[str, str]:
    """Read all .md files in a directory. Returns {filename: content}."""
    if not directory.exists():
        return {}
    return {
        f.name: f.read_text(encoding="utf-8", errors="replace")
        for f in sorted(directory.glob("*.md"))
    }


def collect_sources(base_dir: Path) -> dict:
    """Read all source files for an article. Returns a structured dict."""
    research_dir = base_dir / ".research"

    def _read_optional(path: Path) -> str:
        return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

    return {
        "guideline": (base_dir / "article_guideline.md").read_text(
            encoding="utf-8", errors="replace"
        ),
        "golden_web": _read_md_dir(research_dir / "urls_from_guidelines"),
        "golden_youtube": _read_md_dir(research_dir / "urls_from_guidelines_youtube_videos"),
        "golden_code": _read_md_dir(research_dir / "urls_from_guidelines_code"),
        "exploitation": _read_md_dir(research_dir / "urls_from_guidelines_exploitation"),
        "tavily_results": _read_optional(research_dir / "tavily_results.md"),
        "full_queries": _read_optional(research_dir / "full_queries.md"),
    }



# ---------------------------------------------------------------------------
# Stage 2: COMPRESS (artefact-aware, variable token budget)
# ---------------------------------------------------------------------------

_COMPRESS_SYSTEM = (
    "You are a precise research summarizer. Output only the summary, no preamble."
)

_COMPRESS_USER_TEMPLATE = """\
Summarize the following research source for an article titled "{article_title}".

Source filename: {filename}
Source type: {source_type}
Target length: {max_tokens} tokens

Produce a factual summary covering:
- Main topic and key concepts explained
- Concrete examples, tools, frameworks, APIs, or techniques mentioned (use exact names)
- Specific data points, benchmarks, or claims that could support article sections
- Notable limitations or gaps in coverage

IMPORTANT: Artefacts referenced as `[ARTEFACT_Xxx: type, N lines, topic=...]` exist in the
source. Do NOT reproduce them. Do NOT list them as gaps. Mention their existence and topic
naturally in your summary (e.g., "includes a 23-line Python tool-loop example").

Be specific. Name exact tools and concepts. Do not editorialize.

<source>
{content}
</source>"""


async def _compress_one(
    client,
    semaphore: asyncio.Semaphore,
    article_title: str,
    filename: str,
    source_type: str,
    content: str,
    max_tokens: int,
    dry_run: bool,
) -> str:
    if dry_run:
        return f"[DRY-RUN summary of {filename} ({source_type})]"

    if len(content) > _MAX_SOURCE_CHARS:
        content = content[:_MAX_SOURCE_CHARS] + "\n\n[...content truncated...]"

    async with semaphore:
        log.info(f"    COMPRESS  [{source_type}] {filename}")
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": _COMPRESS_SYSTEM},
                {
                    "role": "user",
                    "content": _COMPRESS_USER_TEMPLATE.format(
                        article_title=article_title,
                        filename=filename,
                        source_type=source_type,
                        max_tokens=max_tokens,
                        content=content,
                    ),
                },
            ],
            max_tokens=max_tokens + 64,
        )
        return response.choices[0].message.content.strip()


async def compress_all_sources(
    client,
    article_title: str,
    sources: dict,
    dry_run: bool,
) -> dict[str, dict[str, str]]:
    semaphore = asyncio.Semaphore(_COMPRESS_CONCURRENCY)

    _MAX_TOKENS = {
        "golden_web": 700,
        "exploitation": 700,
        "golden_youtube": 350,
        "golden_code": 350,
    }

    keys: list[tuple[str, str]] = []
    tasks = []

    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        mt = _MAX_TOKENS[source_type]
        for filename, content in sources[source_type].items():
            keys.append((source_type, filename))
            tasks.append(
                _compress_one(
                    client, semaphore, article_title,
                    filename, source_type, content, mt, dry_run,
                )
            )

    results = await asyncio.gather(*tasks)

    summaries: dict[str, dict[str, str]] = {
        "golden_web": {},
        "golden_youtube": {},
        "golden_code": {},
        "exploitation": {},
    }
    for (source_type, filename), summary in zip(keys, results):
        summaries[source_type][filename] = summary

    return summaries


# ---------------------------------------------------------------------------
# Stage 2b: INDEX — TF-IDF section→source mapping + orphan detection
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z]{3,}", text.lower())


def _tfidf_overlap(query_tokens: list[str], doc_tokens: list[str]) -> float:
    if not query_tokens or not doc_tokens:
        return 0.0
    doc_tf: dict[str, float] = defaultdict(float)
    for t in doc_tokens:
        doc_tf[t] += 1
    total = len(doc_tokens)
    score = 0.0
    for t in set(query_tokens):
        if t in doc_tf:
            score += math.log(1 + doc_tf[t] / total)
    return score / (math.log(1 + len(set(query_tokens))) + 1e-9)


def build_section_source_index(
    guideline: str,
    sources: dict,
) -> dict[str, list[str]]:
    """
    For each content section, find top-3 source files by TF-IDF overlap.
    Returns {section_id: [slug1, slug2, slug3]}.
    """
    content_sections = _extract_content_sections(guideline)

    sec_lines: dict[str, list[str]] = {}
    current_id: str | None = None
    sec_n_map = {title: n for n, title in content_sections}
    cs_set = {title for _, title in content_sections}

    for line in guideline.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            if title in cs_set:
                n = sec_n_map[title]
                current_id = _make_section_id(n, title)
                sec_lines[current_id] = [title]
            else:
                current_id = None
        elif current_id and line.strip():
            sec_lines[current_id].append(line)

    all_sources: list[tuple[str, str]] = []
    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        for fname, content in sources[source_type].items():
            slug = fname[:-3] if fname.endswith(".md") else fname
            all_sources.append((slug, content))

    result: dict[str, list[str]] = {}
    source_selection_counts: dict[str, int] = defaultdict(int)
    for sec_id, lines in sec_lines.items():
        q_tokens = _tokenize(" ".join(lines))
        scores: list[tuple[float, str]] = []
        for slug, content in all_sources:
            d_tokens = _tokenize(content[:20000])
            s = _tfidf_overlap(q_tokens, d_tokens)
            # Diversity penalty: discourage sources already assigned to many sections
            penalty = 1.0 / (1.0 + 0.4 * source_selection_counts[slug])
            scores.append((s * penalty, slug))
        scores.sort(reverse=True)
        top3 = [slug for _, slug in scores[:3]]
        for slug in top3:
            source_selection_counts[slug] += 1
        result[sec_id] = top3

    return result


def classify_orphan_anchors(
    guideline: str,
    sources: dict,
) -> list[dict[str, str]]:
    """
    Find guideline anchors not well-covered by any source.
    Returns list of {anchor, section_id, section_title} for orphan anchors.
    An anchor is orphan if max TF-IDF overlap across all sources < 0.15.
    """
    all_anchors = _extract_all_anchors(guideline)

    all_source_tokens: list[tuple[str, list[str]]] = []
    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        for fname, content in sources[source_type].items():
            slug = fname[:-3] if fname.endswith(".md") else fname
            all_source_tokens.append((slug, _tokenize(content[:20000])))
    if sources.get("tavily_results"):
        all_source_tokens.append(("tavily", _tokenize(sources["tavily_results"][:20000])))

    orphans: list[dict[str, str]] = []
    for anchor_info in all_anchors:
        q_tokens = _tokenize(anchor_info["anchor"])
        max_score = 0.0
        for _slug, d_tokens in all_source_tokens:
            s = _tfidf_overlap(q_tokens, d_tokens)
            if s > max_score:
                max_score = s
        if max_score < 0.15:
            orphans.append(anchor_info)

    return orphans


def compute_tavily_yield(
    sources: dict,
    content_sections: list[tuple[int, str]],
    base_dir: Path | None = None,
) -> tuple[str, float]:
    """
    Parse full_queries.md to compute per-section Tavily yield.
    Returns (tavily_yield_table_str, saturation_float).

    total_rounds is detected from _exploit_round_N.done sentinel files when
    base_dir is provided (most accurate), falling back to text-pattern detection.
    Per-section helping_rounds are attributed by parsing "Reason:" text in
    full_queries.md for "Section N" / "Sections N and M" references.
    """
    full_queries = sources.get("full_queries", "")
    tavily_raw = sources.get("tavily_results", "")

    empty_rows = [
        "| section_id | helping_rounds | unique_facts | duplicate_facts |",
        "|----|----|----|-----|",
    ]
    for n, title in content_sections:
        sec_id = _make_section_id(n, title)
        empty_rows.append(f"| {sec_id} | 0 | 0 | 0 |")

    if not full_queries:
        return "\n".join(empty_rows), 0.5

    # --- Detect total rounds ---
    total_rounds = 0
    if base_dir is not None:
        done_files = list((base_dir / ".research").glob("_exploit_round_*.done"))
        total_rounds = len(done_files)
    if total_rounds == 0:
        # Fallback: scan for explicit "Round N" markers in text
        round_markers = re.findall(r"(?:^|\n)(?:##\s+)?[Rr]ound\s+(\d+)", full_queries)
        total_rounds = max((int(r) for r in round_markers), default=0)
    if total_rounds == 0:
        # Last fallback: estimate from query count (typically ~3-4 queries per round)
        n_queries = len(re.findall(r"Query \[\d+\]", full_queries))
        total_rounds = max(1, (n_queries + 2) // 3) if n_queries else 0

    # --- Compute Tavily saturation ---
    all_urls = re.findall(r"https?://[^\s\)]+", tavily_raw)
    unique_urls = list(dict.fromkeys(all_urls))
    n_unique = len(unique_urls)
    n_dup = len(all_urls) - n_unique

    if total_rounds < 3:
        saturation = 0.5
    else:
        first_half = tavily_raw[: len(tavily_raw) // 2]
        last_half = tavily_raw[len(tavily_raw) // 2 :]
        first_urls = len(set(re.findall(r"https?://[^\s\)]+", first_half)))
        last_urls = len(set(re.findall(r"https?://[^\s\)]+", last_half)))
        saturation = last_urls / (first_urls + 1e-9)
        saturation = min(1.0, saturation)

    # --- Attribute helping_rounds per section from query reasons ---
    # Split on "Query [N]" boundaries; parse each block's "Reason:" for section refs
    query_blocks = re.split(r"Query \[\d+\]\s*\[?[^\]]*\]?", full_queries)
    sec_query_counts: dict[str, int] = defaultdict(int)
    for block in query_blocks[1:]:  # skip text before the first Query block
        reason_m = re.search(r"Reason\s*:", block, re.IGNORECASE)
        if not reason_m:
            continue
        reason_text = block[reason_m.start(): reason_m.start() + 600]
        for n, title in content_sections:
            sec_id = _make_section_id(n, title)
            # Match "Section N" or "Sections N" (with optional "and M" / "M and N")
            if re.search(rf"\bSections?\s+(?:\d+\s*(?:,|and)\s*)*{n}\b", reason_text, re.IGNORECASE):
                sec_query_counts[sec_id] += 1

    # --- Build yield table ---
    n_secs = len(content_sections)
    per_sec_unique = max(1, n_unique // n_secs) if n_secs else 0
    per_sec_dup = max(0, n_dup // n_secs) if n_secs else 0

    rows = [
        "| section_id | helping_rounds | unique_facts | duplicate_facts |",
        "|---|---|---|---|",
    ]
    for idx, (n, title) in enumerate(content_sections):
        sec_id = _make_section_id(n, title)
        weight = 1.0 - 0.3 * (idx / max(1, n_secs - 1))
        # helping_rounds: use attributed query count if available, else distribute proportionally
        hr = sec_query_counts.get(sec_id, 0)
        if hr == 0:
            hr = max(0, round(total_rounds * weight))
        u = max(0, round(per_sec_unique * weight))
        d = max(0, round(per_sec_dup * weight))
        rows.append(f"| {sec_id} | {hr} | {u} | {d} |")

    return "\n".join(rows), round(saturation, 3)


# ---------------------------------------------------------------------------
# Stage 3: ASSEMBLE
# ---------------------------------------------------------------------------

def assemble_context(
    sources: dict,
    summaries: dict[str, dict[str, str]],
    artefact_registry: list[dict[str, Any]],
    section_to_sources: dict[str, list[str]],
    orphan_anchors: list[dict[str, str]],
    tavily_yield_table: str,
    tavily_saturation: float,
    article_title: str,
) -> str:
    artefact_md = _format_artefact_registry_md(artefact_registry)

    source_parts: list[str] = []
    for source_type, label in [
        ("golden_web", "golden_web"),
        ("golden_youtube", "golden_youtube"),
        ("golden_code", "golden_code"),
        ("exploitation", "exploitation"),
    ]:
        for fname, summary in summaries[source_type].items():
            slug = fname[:-3] if fname.endswith(".md") else fname
            source_parts.append(
                f'<s slug="{slug}" type="{label}">\n{summary}\n</s>'
            )
    sources_xml = "<sources>\n" + "\n\n".join(source_parts) + "\n</sources>"

    sec_map_lines = ["| section_id | top_sources |", "|---|---|"]
    for sec_id, slugs in section_to_sources.items():
        sec_map_lines.append(f"| {sec_id} | {', '.join(slugs)} |")
    sec_map = "\n".join(sec_map_lines)

    if orphan_anchors:
        orphan_lines = ["| anchor | section_id |", "|---|---|"]
        for oa in orphan_anchors[:40]:
            safe = oa["anchor"].replace("|", "\\|")
            orphan_lines.append(f"| {safe} | {oa['section_id']} |")
        orphan_block = "\n".join(orphan_lines)
    else:
        orphan_block = "(none)"

    content_sections = _extract_content_sections(sources["guideline"])
    sec_list = "\n".join(
        f"  {_make_section_id(n, t)}: {t}" for n, t in content_sections
    )

    return f"""<article_guideline>
{sources['guideline']}
</article_guideline>

<artefact_registry>
{artefact_md}
</artefact_registry>

{sources_xml}

<section_to_sources>
{sec_map}
</section_to_sources>

<orphan_anchors_raw>
{orphan_block}
</orphan_anchors_raw>

<tavily_yield_per_section>
{tavily_yield_table}
tavily_saturation={tavily_saturation}
</tavily_yield_per_section>

<content_sections>
{sec_list}
</content_sections>"""


# ---------------------------------------------------------------------------
# Stage 4: GENERATE
# ---------------------------------------------------------------------------

_DIGEST_SYSTEM = """\
You are generating a structured exploitation digest for RL training data.
Your output will be parsed by a deterministic validator. Follow the XML schema exactly.
Be factual. Use only information present in the provided sources.

IMPORTANT RULES:
1. For every section block, populate ALL 8 depth items and ALL 6 breadth items.
2. For present="yes" items, the evidence= attribute MUST reference a real source slug
   (e.g., "building-effective-agents-anthropic#L12" or "tavily_r3").
3. For orphan anchors, assign route="depth", route="breadth", or route="unreachable".
   "unreachable" = pure-lookup question (a fact that simply doesn't exist in any web source).
   "depth" or "breadth" = coverage gap that CAN be addressed with more exploration.
4. depth_score and breadth_score in attributes are placeholders — the validator will
   overwrite them with deterministic counts. You may write any integer there.
5. The artefact_available depth item: present="yes" iff the section's artefacts= attribute
   is non-empty.
6. Do NOT reproduce artefact content. Reference them only by ID in evidence= attributes.
7. Output ONLY the XML digest. No preamble, no markdown wrapper.
8. For these commonly under-detected checklist items, apply the definitions below strictly —
   mark present="yes" if ANY of the following conditions is met by any source:
   - "latest_advancements": the source mentions recent (< 3 years) updates, new library
     versions, revised best practices, new benchmarks, or emerging patterns for this topic.
   - "historical_context": the source references where this concept originated, its
     predecessors, earlier implementations, or how it evolved over time.
   - "cross_domain_analogies": the source draws ANY explicit comparison to a concept from
     a different field (e.g., manufacturing pipelines, biological systems, supply chains).
     Mark "no" only if zero such analogies appear anywhere in the source.
   - "adjacent_trends": the source mentions nearby emerging practices or movements that
     relate to but are not the central topic (e.g., LLM-native CI/CD adjacent to workflow
     patterns, or serverless adjacent to API design).
9. <section_coverage> MUST contain EXACTLY one <section> block for EACH section_id in the
   <tavily_yield_per_section> table — do NOT merge, skip, or omit any. If your per-section
   analysis is very long, finish the current section and continue to the next; stopping
   early is a validation failure. Completeness comes first."""

_DIGEST_USER_TEMPLATE = """\
Generate a structured exploitation digest for the article "{article_title}".

Context:
{context}

---

{section_ids_note}Output EXACTLY this XML structure. Replace {{PLACEHOLDERS}} with real values.

<digest_meta>
  <article_title>{article_title}</article_title>
  <total_sources>{{N}}</total_sources>
  <total_artefacts>{{N}}</total_artefacts>
  <tavily_saturation>{{float 0-1}}</tavily_saturation>
  <n_orphan_anchors>{{N}}</n_orphan_anchors>
  <n_content_sections>{{N}}</n_content_sections>
  <external_evidence_policy>{{will be overwritten by the validator}}</external_evidence_policy>
</digest_meta>

<artefact_registry>
{{copy the artefact_registry table from context, verbatim}}
</artefact_registry>

<sources>
{{one <s slug="..." type="..."> block per source file, containing the compressed summary}}
</sources>

<tavily_yield_per_section>
{{copy the tavily_yield_per_section table from context, verbatim, including tavily_saturation= line}}
</tavily_yield_per_section>

<section_coverage>
{{For EACH content section listed in <content_sections>, output a <section> block:}}

<section id="{{section_id}}" self_contained="yes|no" sources="{{comma-sep slugs}}" artefacts="{{comma-sep artefact IDs or empty}}">
  <intent>One sentence: what this section aims to cover and why it matters for the article.</intent>
  <depth_checklist depth_score="0">
    <item name="motivation" present="yes|no" evidence="{{slug#Lline or tavily_rN or empty}}"/>
    <item name="theoretical_foundations" present="yes|no" evidence=""/>
    <item name="technical_nuances" present="yes|no" evidence=""/>
    <item name="latest_advancements" present="yes|no" evidence=""/>
    <item name="limitations_failure_modes" present="yes|no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes|no" evidence=""/>
    <item name="case_studies_metrics" present="yes|no" evidence=""/>
    <item name="artefact_available" present="yes|no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="yes|no" evidence=""/>
    <item name="cross_domain_analogies" present="yes|no" evidence=""/>
    <item name="historical_context" present="yes|no" evidence=""/>
    <item name="enabling_technologies" present="yes|no" evidence=""/>
    <item name="industry_applications" present="yes|no" evidence=""/>
    <item name="adjacent_trends" present="yes|no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
    {{For each orphan anchor that belongs to THIS section, output:}}
    <orphan route="depth|breadth|unreachable" anchor="{{exact anchor text}}" bullet="{{closest depth/breadth item name}}">
      One-sentence justification for this routing decision.
    </orphan>
  </orphan_anchors>
</section>

</section_coverage>

<gap_profile>
  <section id="{{section_id}}" need_depth="{{int}}" need_breadth="{{int}}"/>
  {{repeat for all sections; the validator will overwrite need_depth /}}
  {{need_breadth and add target_words, mandatory_bullets, must_cover_depth,}}
  {{must_stay_brief attributes deterministically -- you do not compute them}}
  <overall>
    <weakest_sections>{{comma-sep section IDs}}</weakest_sections>
    <strongest_sections>{{comma-sep section IDs}}</strongest_sections>
    <dominant_gap_type>depth|breadth|balanced</dominant_gap_type>
    <exploration_insight>One actionable sentence on what additional exploration would most improve article quality.</exploration_insight>
  </overall>
</gap_profile>
"""

_MISSING_SECTIONS_USER_TEMPLATE = """\
For the article "{article_title}", the <section_coverage> block was missing sections for \
these section IDs:
{missing_ids_list}

Generate ONLY those missing <section> blocks (one per ID above, in order) using the exact \
XML schema below.
Each block MUST include ALL 8 depth_checklist items and ALL 6 breadth_checklist items.
Output ONLY the bare <section>...</section> elements — no preamble, no wrapper tags.

XML schema for each section:
<section id="{{section_id}}" self_contained="yes|no" sources="{{comma-sep slugs}}" artefacts="{{IDs or empty}}">
  <intent>One sentence: what this section aims to cover and why it matters.</intent>
  <depth_checklist depth_score="0">
    <item name="motivation" present="yes|no" evidence="{{slug#Lline or tavily_rN or empty}}"/>
    <item name="theoretical_foundations" present="yes|no" evidence=""/>
    <item name="technical_nuances" present="yes|no" evidence=""/>
    <item name="latest_advancements" present="yes|no" evidence=""/>
    <item name="limitations_failure_modes" present="yes|no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes|no" evidence=""/>
    <item name="case_studies_metrics" present="yes|no" evidence=""/>
    <item name="artefact_available" present="yes|no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="yes|no" evidence=""/>
    <item name="cross_domain_analogies" present="yes|no" evidence=""/>
    <item name="historical_context" present="yes|no" evidence=""/>
    <item name="enabling_technologies" present="yes|no" evidence=""/>
    <item name="industry_applications" present="yes|no" evidence=""/>
    <item name="adjacent_trends" present="yes|no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
    {{For orphan anchors belonging to THIS section only:}}
    <orphan route="depth|breadth|unreachable" anchor="{{exact anchor text}}" bullet="{{closest item name}}">
      One-sentence justification.
    </orphan>
  </orphan_anchors>
</section>

Context:
{context}
"""


async def generate_digest(
    client,
    article_title: str,
    context: str,
    dry_run: bool,
    content_sections: list[tuple[int, str]] | None = None,
) -> str:
    if dry_run:
        return _make_dry_run_digest(article_title)

    if content_sections:
        n = len(content_sections)
        ids = [_make_section_id(n_i, t) for n_i, t in content_sections]
        section_ids_note = (
            f"COMPLETENESS REQUIREMENT: Your <section_coverage> block MUST contain "
            f"exactly {n} <section> blocks, one for each ID listed below in order:\n"
            + "\n".join(f"  {sid}" for sid in ids)
            + "\n\n---\n\n"
        )
    else:
        section_ids_note = ""

    log.info(f"  Stage 4: GENERATE digest (model={MODEL})")
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": _DIGEST_SYSTEM},
            {
                "role": "user",
                "content": _DIGEST_USER_TEMPLATE.format(
                    article_title=article_title,
                    context=context,
                    section_ids_note=section_ids_note,
                ),
            },
        ],
        max_tokens=32768,
    )
    return response.choices[0].message.content.strip()


async def _generate_missing_sections(
    client,
    article_title: str,
    context: str,
    missing_ids: list[str],
) -> str:
    """Generate ONLY the missing <section> blocks and return them as raw XML."""
    missing_ids_list = "\n".join(f"  - {sid}" for sid in missing_ids)
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": _DIGEST_SYSTEM},
            {
                "role": "user",
                "content": _MISSING_SECTIONS_USER_TEMPLATE.format(
                    article_title=article_title,
                    missing_ids_list=missing_ids_list,
                    context=context,
                ),
            },
        ],
        max_tokens=32768,
    )
    return response.choices[0].message.content.strip()


def _splice_sections_into_coverage(digest: str, new_sections_xml: str) -> str:
    """Insert new <section> blocks just before </section_coverage>."""
    # Strip any accidental <section_coverage> wrapper the model may echo
    inner = re.sub(
        r"</?section_coverage\b[^>]*>", "", new_sections_xml, flags=re.IGNORECASE
    ).strip()
    if not inner:
        return digest
    return digest.replace("</section_coverage>", inner + "\n</section_coverage>", 1)


async def _generate_missing_sections_opus(
    article_title: str,
    context: str,
    missing_ids: list[str],
) -> str:
    """Layer-3 fallback: generate missing <section> blocks via Claude Opus."""
    try:
        from anthropic import AsyncAnthropic  # soft import
    except ModuleNotFoundError:
        raise RuntimeError(
            "anthropic package not installed. "
            "Add 'anthropic>=0.40.0' to mcp_server/pyproject.toml and run uv sync."
        )
    missing_ids_list = "\n".join(f"  - {sid}" for sid in missing_ids)
    opus_client = AsyncAnthropic(api_key=_ANTHROPIC_API_KEY)
    try:
        message = await opus_client.messages.create(
            model=_ANTHROPIC_MODEL,
            max_tokens=16384,
            system=_DIGEST_SYSTEM,
            messages=[
                {
                    "role": "user",
                    "content": _MISSING_SECTIONS_USER_TEMPLATE.format(
                        article_title=article_title,
                        missing_ids_list=missing_ids_list,
                        context=context,
                    ),
                }
            ],
        )
        return message.content[0].text.strip()
    finally:
        await opus_client.close()


def _make_dry_run_digest(article_title: str) -> str:
    return f"""<digest_meta>
  <article_title>{article_title}</article_title>
  <total_sources>0</total_sources>
  <total_artefacts>0</total_artefacts>
  <tavily_saturation>0.5</tavily_saturation>
  <n_orphan_anchors>0</n_orphan_anchors>
  <n_content_sections>1</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|--------|------|-------|-------|---------|
(none)
</artefact_registry>

<sources>
<s slug="dry-run" type="golden_web">
[DRY-RUN summary]
</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::dry-run | 0 | 0 | 0 |
tavily_saturation=0.5
</tavily_yield_per_section>

<section_coverage>
<section id="S1::dry-run" self_contained="yes" sources="" artefacts="">
  <intent>[DRY-RUN]</intent>
  <depth_checklist depth_score="0">
    <item name="motivation" present="no" evidence=""/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::dry-run" need_depth="8" need_breadth="6" target_words="0" mandatory_bullets="0" must_cover_depth="0" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S1::dry-run</weakest_sections>
    <strongest_sections></strongest_sections>
    <dominant_gap_type>balanced</dominant_gap_type>
    <exploration_insight>[DRY-RUN]</exploration_insight>
  </overall>
</gap_profile>"""


# ---------------------------------------------------------------------------
# Stage 5: VALIDATE + deterministic post-processing
# ---------------------------------------------------------------------------

_SECTION_BLOCK_RE = re.compile(
    r'<section\s+id="([^"]+)"[^>]*>(.*?)</section>',
    re.DOTALL,
)
_ITEM_PRESENT_RE = re.compile(
    r'<item\s+name="([^"]+)"\s+present="(yes|no)"(?:\s+evidence="([^"]*)")?'
)
_ORPHAN_RE = re.compile(
    r'<orphan\s+route="(depth|breadth|unreachable)"\s+anchor="([^"]+)"\s+bullet="([^"]*)"'
)


def _count_checklist(section_body: str, items: list[str]) -> int:
    count = 0
    for m in _ITEM_PRESENT_RE.finditer(section_body):
        if m.group(1) in items and m.group(2) == "yes":
            count += 1
    return count


def _count_orphans_by_route(section_body: str) -> tuple[int, int, int]:
    nd = nb = nu = 0
    for m in _ORPHAN_RE.finditer(section_body):
        route = m.group(1)
        if route == "depth":
            nd += 1
        elif route == "breadth":
            nb += 1
        else:
            nu += 1
    return nd, nb, nu


def _rewrite_score_attr(text: str, section_id: str, attr: str, new_val: int) -> str:
    """Overwrite depth_score or breadth_score for a specific section."""
    pattern = re.compile(
        r'(<(?:depth|breadth)_checklist\s+(?:depth|breadth)_score=")(\d+)(")',
    )
    sec_pattern = re.compile(
        r'(<section\s+id="' + re.escape(section_id) + r'"[^>]*>)(.*?)(</section>)',
        re.DOTALL,
    )

    def _replace_section(m: re.Match) -> str:
        body = m.group(2)
        count = [0]

        def _replace_attr(am: re.Match) -> str:
            tag = am.group(0)
            if attr in tag and count[0] == 0:
                count[0] += 1
                return am.group(1) + str(new_val) + am.group(3)
            return am.group(0)

        new_body = pattern.sub(_replace_attr, body)
        return m.group(1) + new_body + m.group(3)

    return sec_pattern.sub(_replace_section, text)


def _rewrite_orphan_counts(text: str, section_id: str, nd: int, nb: int, nu: int) -> str:
    sec_pattern = re.compile(
        r'(<section\s+id="' + re.escape(section_id) + r'"[^>]*>)(.*?)(</section>)',
        re.DOTALL,
    )
    orphan_tag_re = re.compile(
        r'<orphan_anchors\s+n_depth="\d+"\s+n_breadth="\d+"\s+n_unreachable="\d+"'
    )

    def _replace_section(m: re.Match) -> str:
        body = m.group(2)
        new_body = orphan_tag_re.sub(
            f'<orphan_anchors n_depth="{nd}" n_breadth="{nb}" n_unreachable="{nu}"',
            body,
        )
        return m.group(1) + new_body + m.group(3)

    return sec_pattern.sub(_replace_section, text)


def _preset_2d(
    need: int,
    target_words: int,
    must_cover_depth: int,
    must_stay_brief: int,
    policy: str,
) -> str:
    """
    2D preset rule: combine raw coverage need with variant-agnostic writing
    headroom and the article-wide external_evidence_policy.

    Intuition: even with high coverage need, a section that is supposed to
    be brief cannot absorb the fruits of extra exploration. Conversely, a
    section with explicit depth demands and a large word budget should run
    more rounds for the same nominal need.

    Preset names (exploration intensity):
        skip     — no exploration; skip the phase entirely
        light    — 1 round, balanced focus (50% depth / 50% breadth)
        standard — 2 rounds: round 1 depth-focused (100% depth),
                             round 2 breadth-focused (100% breadth)
        deep     — 3 rounds: round 1 depth-focused, round 2 breadth-focused,
                             round 3 depth-focused (~67% depth / 33% breadth)

    forbidden policy short-circuits to "skip" (no exploration is usable).
    required policy bumps headroom by +1 (external evidence is mandatory).
    """
    if policy == "forbidden":
        return "skip"

    headroom = 0
    if target_words >= 400:
        headroom += 1
    elif 0 < target_words < 200:
        headroom -= 1
    if must_cover_depth >= 3:
        headroom += 1
    if must_stay_brief >= 2:
        headroom -= 1
    if policy == "required":
        headroom += 1

    # Larger headroom => more room to absorb new research => higher preset.
    # Negative headroom (brief / sparse / explicitly-capped section) shrinks the
    # effective need so a short section doesn't trigger heavy exploration.
    eff_need = need + 2 * headroom

    if eff_need <= 2:
        return "skip"
    if eff_need <= 5:
        return "light"
    if eff_need <= 9:
        return "standard"
    return "deep"


def _compute_gap_profile_deterministic(
    digest: str,
    content_sections: list[tuple[int, str]],
    known_slugs: set[str],
    features: dict[str, Any],
) -> tuple[str, dict[str, str]]:
    """
    Build a fully deterministic <gap_profile> block from the parsed section
    coverage AND inject variant-agnostic per-section features into each
    <section> row:
        target_words, mandatory_bullets, must_cover_depth, must_stay_brief

    need_depth   = (8 - depth_score) + 3 * n_depth_orphans
    need_breadth = (6 - breadth_score) + 3 * n_breadth_orphans
    preset       = 2D function of (need_depth + need_breadth, headroom_proxy,
                                   external_evidence_policy)

    Returns (gap_profile_xml_str, oracle_dict).
    oracle_dict maps section_id -> recommended_preset and is kept SEPARATE
    from the digest (written to section_oracle.json).
    """
    policy = features.get("external_evidence_policy", "allowed")
    feat_sections: dict[str, dict[str, int]] = features.get("sections", {})

    sections_data: list[tuple[str, int, int, dict[str, int]]] = []

    for m in _SECTION_BLOCK_RE.finditer(digest):
        sec_id = m.group(1)
        body = m.group(2)

        depth_score = _count_checklist(body, _DEPTH_ITEMS)
        breadth_score = _count_checklist(body, _BREADTH_ITEMS)
        nd, nb, nu = _count_orphans_by_route(body)

        need_depth = max(0, (8 - depth_score) + 3 * nd)
        need_breadth = max(0, (6 - breadth_score) + 3 * nb)
        sec_feat = feat_sections.get(sec_id, {
            "target_words": 0, "mandatory_bullets": 0,
            "must_cover_depth": 0, "must_stay_brief": 0,
        })
        sections_data.append((sec_id, need_depth, need_breadth, sec_feat))

    # Build oracle dict (kept out of digest)
    oracle: dict[str, str] = {
        sec_id: _preset_2d(
            nd + nb,
            sf["target_words"],
            sf["must_cover_depth"], sf["must_stay_brief"],
            policy,
        )
        for sec_id, nd, nb, sf in sections_data
    }

    # Backfill "skip" for sections that have features but no coverage block in
    # the digest.  No coverage block means the LLM found no depth/breadth gap
    # for that section, which is semantically equivalent to skip.
    covered_ids = {sec_id for sec_id, *_ in sections_data}
    for sec_id in feat_sections:
        if sec_id not in covered_ids:
            oracle[sec_id] = "skip"

    # Build gap_profile XML WITHOUT recommended_preset, WITH feature attrs
    lines = ["<gap_profile>"]
    for sec_id, nd, nb, sf in sections_data:
        lines.append(
            f'  <section id="{sec_id}" need_depth="{nd}" need_breadth="{nb}"'
            f' target_words="{sf["target_words"]}"'
            f' mandatory_bullets="{sf["mandatory_bullets"]}"'
            f' must_cover_depth="{sf["must_cover_depth"]}"'
            f' must_stay_brief="{sf["must_stay_brief"]}"/>'
        )

    if sections_data:
        sorted_by_total = sorted(sections_data, key=lambda x: x[1] + x[2])
        strongest = [s[0] for s in sorted_by_total[:2]]
        weakest = [s[0] for s in sorted_by_total[-2:]]
        total_d = sum(s[1] for s in sections_data)
        total_b = sum(s[2] for s in sections_data)
        gap_type = (
            "depth" if total_d > total_b * 1.5
            else "breadth" if total_b > total_d * 1.5
            else "balanced"
        )
    else:
        strongest = weakest = []
        gap_type = "balanced"

    lines.append("  <overall>")
    lines.append(f"    <weakest_sections>{', '.join(weakest)}</weakest_sections>")
    lines.append(f"    <strongest_sections>{', '.join(strongest)}</strongest_sections>")
    lines.append(f"    <dominant_gap_type>{gap_type}</dominant_gap_type>")
    lines.append("    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>")
    lines.append("  </overall>")
    lines.append("</gap_profile>")
    return "\n".join(lines), oracle


def _inject_external_evidence_policy(digest: str, policy: str) -> str:
    """
    Ensure <digest_meta> contains exactly one <external_evidence_policy> tag
    with the given value. Replaces any prior tag, or inserts before </digest_meta>
    if absent. Returns the digest unchanged if no <digest_meta> block exists.
    """
    meta_re = re.compile(r"(<digest_meta>)(.*?)(</digest_meta>)", re.DOTALL)
    m = meta_re.search(digest)
    if not m:
        return digest
    body = m.group(2)
    tag_re = re.compile(r"\s*<external_evidence_policy>[^<]*</external_evidence_policy>")
    body = tag_re.sub("", body)
    body = body.rstrip() + (
        f"\n  <external_evidence_policy>{policy}</external_evidence_policy>\n"
    )
    return digest[:m.start()] + m.group(1) + body + m.group(3) + digest[m.end():]


def validate_and_postprocess(
    digest: str,
    guideline: str,
    known_slugs: set[str],
    artefact_registry: list[dict[str, Any]],
    features: dict[str, Any],
) -> tuple[str, bool, list[str], dict[str, str]]:
    """
    Validate + deterministic post-processing.
    Returns (postprocessed_digest, passed, issues, oracle_dict).
    oracle_dict maps section_id -> recommended_preset (NOT written into the digest).
    Variant-agnostic features are injected into <gap_profile> rows and into
    <digest_meta><external_evidence_policy>.
    """
    issues: list[str] = []

    for tag in ["<digest_meta>", "<artefact_registry>", "<sources>",
                "<section_coverage>", "<gap_profile>"]:
        if tag not in digest:
            issues.append(f"Missing required tag: {tag}")

    content_sections = _extract_content_sections(guideline)
    for n, title in content_sections:
        sec_id = _make_section_id(n, title)
        if sec_id not in digest:
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            if slug not in digest:
                issues.append(f"Section missing from coverage: {sec_id}")

    modified = digest
    known_artefact_ids = {e["id"] for e in artefact_registry}
    norm_guideline = _normalize_text(guideline)

    for m in _SECTION_BLOCK_RE.finditer(digest):
        sec_id = m.group(1)
        body = m.group(2)

        depth_score = _count_checklist(body, _DEPTH_ITEMS)
        breadth_score = _count_checklist(body, _BREADTH_ITEMS)
        nd, nb, nu = _count_orphans_by_route(body)

        modified = _rewrite_score_attr(modified, sec_id, "depth_score", depth_score)
        modified = _rewrite_score_attr(modified, sec_id, "breadth_score", breadth_score)
        modified = _rewrite_orphan_counts(modified, sec_id, nd, nb, nu)

        for item_m in _ITEM_PRESENT_RE.finditer(body):
            if item_m.group(2) == "yes":
                evidence = item_m.group(3) or ""
                if evidence:
                    slug_part = evidence.split("#")[0].split("_r")[0]
                    if (slug_part not in known_slugs
                            and slug_part != "tavily"
                            and slug_part not in known_artefact_ids):
                        issues.append(
                            f"Section {sec_id}: unknown evidence slug '{slug_part}'"
                        )

        for orphan_m in _ORPHAN_RE.finditer(body):
            anchor_text = _normalize_text(orphan_m.group(2))
            route = orphan_m.group(1)
            if route in ("depth", "breadth"):
                if anchor_text.lower() not in norm_guideline.lower():
                    issues.append(
                        f"Section {sec_id}: orphan anchor not in guideline: "
                        f"'{anchor_text[:60]}'"
                    )

    gap_block, oracle = _compute_gap_profile_deterministic(
        modified, content_sections, known_slugs, features
    )
    gap_re = re.compile(r"<gap_profile>.*?</gap_profile>", re.DOTALL)
    if gap_re.search(modified):
        modified = gap_re.sub(gap_block, modified)
    else:
        modified = modified + "\n\n" + gap_block

    # Inject article-wide external_evidence_policy into <digest_meta>
    modified = _inject_external_evidence_policy(
        modified, features.get("external_evidence_policy", "allowed")
    )

    # Drop artefact registry rows for artefacts not referenced anywhere in the digest
    modified = _drop_unreferenced_artefacts(modified)

    passed = len(issues) == 0
    return modified, passed, issues, oracle


# ---------------------------------------------------------------------------
# Build RL input (per-section, ~4.7K tokens)
# ---------------------------------------------------------------------------
# _RL_INPUT_SYSTEM and build_rl_input are defined once in _rl_preset.py and
# re-imported here so other training scripts can use them without triggering
# this module's API-key guard.
from _rl_preset import _RL_INPUT_SYSTEM, build_rl_input  # noqa: E402, F401


# ---------------------------------------------------------------------------
# Per-article orchestration
# ---------------------------------------------------------------------------

async def process_article(
    client,
    article_dir: str,
    dry_run: bool,
    force: bool,
) -> bool:
    base_dir = _BASES_DIR / article_dir
    output_path = base_dir / "research_digest.md"
    article_title = ARTICLES[article_dir]

    log.info("=" * 65)
    log.info(f"Article: {article_dir}  ({article_title})")

    if output_path.exists() and not force:
        log.info("  SKIP — research_digest.md already exists (use --force to overwrite)")
        return True

    # Stage 1: COLLECT
    log.info("  Stage 1: COLLECT")
    sources = collect_sources(base_dir)
    counts = {k: len(v) for k, v in sources.items() if isinstance(v, dict)}
    log.info(f"    {counts}")

    # Stage 0: EXTRACT ARTEFACTS (deterministic)
    log.info("  Stage 0: EXTRACT ARTEFACTS")
    sources_stripped, artefact_registry = extract_all_artefacts(sources)
    log.info(f"    Extracted {len(artefact_registry)} artefacts")

    known_slugs: set[str] = set()
    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        for fname in sources[source_type]:
            slug = fname[:-3] if fname.endswith(".md") else fname
            known_slugs.add(slug)

    # Stage 2b: INDEX
    log.info("  Stage 2b: INDEX")
    section_to_sources = build_section_source_index(sources["guideline"], sources)
    orphan_anchors = classify_orphan_anchors(sources["guideline"], sources)
    log.info(f"    {len(orphan_anchors)} orphan anchors detected")

    content_sections = _extract_content_sections(sources["guideline"])
    tavily_yield_table, tavily_saturation = compute_tavily_yield(
        sources, content_sections, base_dir=base_dir
    )

    # Stage 2c: GUIDELINE FEATURES (variant-agnostic numeric signals)
    log.info("  Stage 2c: EXTRACT GUIDELINE FEATURES")
    features = await extract_guideline_features(
        client, article_title, sources["guideline"], content_sections, dry_run
    )
    log.info(
        f"    external_evidence_policy={features['external_evidence_policy']}, "
        f"sections_with_features={len(features['sections'])}"
    )

    # Stage 2: COMPRESS (uses artefact-stripped sources)
    total_sources = sum(counts.values())
    log.info(f"  Stage 2: COMPRESS ({total_sources} sources, concurrency={_COMPRESS_CONCURRENCY})")
    summaries = await compress_all_sources(client, article_title, sources_stripped, dry_run)

    # Stage 3: ASSEMBLE
    log.info("  Stage 3: ASSEMBLE")
    context = assemble_context(
        sources, summaries, artefact_registry,
        section_to_sources, orphan_anchors,
        tavily_yield_table, tavily_saturation,
        article_title,
    )
    log.info(f"    Assembled context: ~{len(context) // 4:,} tokens")

    # Stage 4+5 with retries
    digest: str | None = None
    oracle: dict[str, str] = {}
    issues: list[str] = []
    if dry_run:
        digest = await generate_digest(client, article_title, context, dry_run)
        log.info("  Stage 5: VALIDATE — skipped (dry-run)")
    else:
        last_processed: str | None = None
        for attempt in range(1, 4):
            if attempt == 1 or last_processed is None:
                # Layer 1: full digest generation with explicit section-IDs requirement
                candidate = await generate_digest(
                    client, article_title, context, dry_run, content_sections
                )
            else:
                # Layer 2: targeted completion — generate only missing sections and splice
                missing_ids = [
                    iss.split("Section missing from coverage: ")[1]
                    for iss in issues
                    if iss.startswith("Section missing from coverage: ")
                ]
                if missing_ids:
                    log.info(
                        f"  Stage 4b: TARGETED COMPLETION for "
                        f"{len(missing_ids)} missing section(s): {missing_ids}"
                    )
                    new_xml = await _generate_missing_sections(
                        client, article_title, context, missing_ids
                    )
                    candidate = _splice_sections_into_coverage(last_processed, new_xml)
                else:
                    # No missing sections but other validation issue — regenerate whole digest
                    candidate = await generate_digest(
                        client, article_title, context, dry_run, content_sections
                    )

            log.info(f"  Stage 5: VALIDATE + POSTPROCESS (attempt {attempt})")
            processed, ok, issues, attempt_oracle = validate_and_postprocess(
                candidate, sources["guideline"], known_slugs, artefact_registry, features
            )
            last_processed = processed

            if ok:
                digest = processed
                oracle = attempt_oracle
                log.info("    Validation PASSED")
                break
            else:
                log.warning("    Validation issues:")
                for issue in issues:
                    log.warning(f"      * {issue}")
                digest = processed
                oracle = attempt_oracle
                if attempt == 3:
                    log.error("    All 3 attempts failed — saving last processed candidate.")

        # Layer 3: Claude Opus fallback for any remaining missing sections
        if issues and not dry_run:
            still_missing = [
                iss.split("Section missing from coverage: ")[1]
                for iss in issues
                if iss.startswith("Section missing from coverage: ")
            ]
            if still_missing:
                if _ANTHROPIC_API_KEY:
                    log.warning(
                        f"  Stage 4c: OPUS FALLBACK ({_ANTHROPIC_MODEL}) for "
                        f"{len(still_missing)} section(s): {still_missing}"
                    )
                    try:
                        new_xml = await _generate_missing_sections_opus(
                            article_title, context, still_missing
                        )
                        candidate = _splice_sections_into_coverage(digest, new_xml)
                        processed, ok, issues, attempt_oracle = validate_and_postprocess(
                            candidate, sources["guideline"], known_slugs,
                            artefact_registry, features,
                        )
                        if ok:
                            digest = processed
                            oracle = attempt_oracle
                            log.info("    Opus fallback PASSED")
                        else:
                            log.error("    Opus fallback also failed — saving best candidate.")
                            digest = processed
                            oracle = attempt_oracle
                    except Exception as exc:
                        log.error(f"    Opus fallback error: {exc}")
                else:
                    log.warning(
                        "  Layer-3 fallback skipped — ANTHROPIC_API_KEY not set in "
                        f"{_ENV_FILE}"
                    )

    # Stage 6: STORE
    log.info("  Stage 6: STORE")
    if not dry_run and digest:
        output_path.write_text(digest, encoding="utf-8")
        log.info(f"    Written: {output_path}")
        oracle_path = base_dir / "section_oracle.json"
        oracle_path.write_text(json.dumps({"presets": oracle}, indent=2), encoding="utf-8")
        log.info(f"    Oracle written: {oracle_path}")
        features_path = base_dir / "guideline_features.json"
        features_path.write_text(json.dumps(features, indent=2), encoding="utf-8")
        log.info(f"    Features written: {features_path}")
        log.info(f"    Digest size: ~{len(digest) // 4:,} tokens ({len(digest):,} chars)")
    else:
        log.info(f"    [DRY-RUN] Would write to: {output_path}")

    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main(articles: list[str], dry_run: bool, force: bool) -> None:
    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=_XAI_API_KEY, base_url=_XAI_BASE_URL)

    log.info(f"Digest pipeline v2 — model={MODEL}, dry_run={dry_run}, force={force}")
    log.info(f"Bases dir: {_BASES_DIR}")

    results: list[tuple[str, bool]] = []
    for article_dir in articles:
        ok = await process_article(client, article_dir, dry_run, force)
        results.append((article_dir, ok))

    await client.close()

    log.info("=" * 65)
    log.info("SUMMARY")
    for article_dir, ok in results:
        log.info(f"  {'OK    ' if ok else 'FAILED'} {article_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate exploitation digests (v2) for RL training articles."
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        choices=list(ARTICLES.keys()),
        default=list(ARTICLES.keys()),
        metavar="ARTICLE",
        help=(
            "Articles to process (default: all). "
            f"Choices: {', '.join(ARTICLES.keys())}"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan only — no API calls, no files written.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing research_digest.md files.",
    )
    args = parser.parse_args()

    asyncio.run(main(args.articles, args.dry_run, args.force))
