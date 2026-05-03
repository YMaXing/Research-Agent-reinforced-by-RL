"""Phase 2c — Exploitation Digest Generator

Generates structured exploitation digests for each of the 5 training articles.
These digests serve as compact context (~3.5–4.7K tokens) for the RL policy
model (Qwen3-4B) to select exploration presets from.

Pipeline (6 stages):
  1. COLLECT  — Read all source files from rl_training_data/bases/<article>/.research/
  2. COMPRESS — Summarize each source to ~250 tokens (parallel async, semaphore-limited)
  3. ASSEMBLE — Build XML-tagged context from all summaries + tavily + query history
  4. GENERATE — Single API call → structured 3-section digest (grok-4-1-fast-reasoning)
  5. VALIDATE — Check section completeness; retry up to 2 times on failure
  6. STORE    — Write to rl_training_data/bases/<article>/research_digest.md

Usage (from research_agent_local/):
  uv run --project mcp_client python generate_digests.py
  uv run --project mcp_client python generate_digests.py --articles 02_workflows_vs_agents
  uv run --project mcp_client python generate_digests.py --dry-run
  uv run --project mcp_client python generate_digests.py --force
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import re
import sys
from pathlib import Path

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

# Max concurrent compression calls (to stay within rate limits)
_COMPRESS_CONCURRENCY = 5

# Max chars per source before truncation (~20K tokens at 4 chars/tok)
_MAX_SOURCE_CHARS = 80_000

# Preamble/metadata section keywords — skipped in coverage analysis
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
}

# Articles: dir name → display title
ARTICLES: dict[str, str] = {
    "02_workflows_vs_agents": "Workflows vs. Agents",
    "03_context_engineering": "Context Engineering",
    "05_workflow_patterns": "Workflow Patterns",
    "06_tools": "Tools",
    "08_react_practice": "ReAct in Practice",
    "09_RAG": "Retrieval-Augmented Generation",
    "11_multimodal": "Multimodal AI",
}

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
# Stage 2: COMPRESS
# ---------------------------------------------------------------------------

_COMPRESS_SYSTEM = (
    "You are a precise research summarizer. Output only the summary, no preamble."
)

_COMPRESS_USER_TEMPLATE = """\
Summarize the following research source for an article titled "{article_title}".

Source filename: {filename}
Source type: {source_type}

Produce a factual 200-300 token summary covering:
- Main topic and key concepts explained
- Concrete examples, tools, frameworks, APIs, or techniques mentioned (use exact names)
- Specific data points, benchmarks, or claims that could support article sections
- Notable limitations or gaps in coverage

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
    dry_run: bool,
) -> str:
    """Compress a single source file to ~250 tokens."""
    if dry_run:
        return f"[DRY-RUN summary of {filename} ({source_type})]"

    # Truncate very large sources so each call stays within the model's context
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
                        content=content,
                    ),
                },
            ],
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()


async def compress_all_sources(
    client,
    article_title: str,
    sources: dict,
    dry_run: bool,
) -> dict[str, dict[str, str]]:
    """Run all compression tasks concurrently. Returns {source_type: {filename: summary}}."""
    semaphore = asyncio.Semaphore(_COMPRESS_CONCURRENCY)

    keys: list[tuple[str, str]] = []
    tasks = []

    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        for filename, content in sources[source_type].items():
            keys.append((source_type, filename))
            tasks.append(
                _compress_one(
                    client, semaphore, article_title,
                    filename, source_type, content, dry_run,
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
# Stage 3: ASSEMBLE
# ---------------------------------------------------------------------------

def _format_source_block(tag: str, summaries: dict[str, str]) -> str:
    if not summaries:
        return f"<{tag}>\n(none)\n</{tag}>"
    parts = [f"### {fname}\n{summary}" for fname, summary in summaries.items()]
    return f"<{tag}>\n" + "\n\n".join(parts) + f"\n</{tag}>"


def assemble_context(
    sources: dict,
    summaries: dict[str, dict[str, str]],
) -> str:
    """Build the full XML-tagged context for Stage 4."""
    blocks = [
        f"<article_guideline>\n{sources['guideline']}\n</article_guideline>",
        _format_source_block("golden_web_summaries", summaries["golden_web"]),
        _format_source_block("golden_youtube_summaries", summaries["golden_youtube"]),
        _format_source_block("golden_code_summaries", summaries["golden_code"]),
        _format_source_block("exploitation_source_summaries", summaries["exploitation"]),
        f"<tavily_exploitation_results>\n{sources['tavily_results']}\n</tavily_exploitation_results>",
        f"<exploitation_query_history>\n{sources['full_queries']}\n</exploitation_query_history>",
    ]
    return "\n\n".join(blocks)


# ---------------------------------------------------------------------------
# Stage 4: GENERATE
# ---------------------------------------------------------------------------

_DIGEST_SYSTEM = """\
You are generating a structured exploitation digest for RL training data preparation.
Your output will be used as compact context for a small RL policy model to select
research exploration strategies. Be specific, factual, and follow the format exactly.

IMPORTANT: The digest must be detailed and thorough. Target 5,000-8,000 tokens total.
Do NOT summarize briefly — provide rich, specific detail in every field."""

_DIGEST_USER_TEMPLATE = """\
Generate a structured exploitation digest for the article titled "{article_title}".

The context below includes the article guideline, summaries of all research sources
(golden and exploitation), Tavily search results, and the query history used during
the exploitation phase.

{context}

---

Generate the exploitation digest in EXACTLY this format. Do not add extra sections.

# Exploitation Digest — {article_title}

## 1. Source Inventory

### Golden Sources
| Source | Type | Key Contributions |
|--------|------|------------------|
(one row per golden source across golden_web, golden_youtube, golden_code)

### Exploitation Sources
| Source | Type | Key Contributions |
|--------|------|------------------|
(one row per exploitation source)

### Tavily Exploitation Results
- Total exploitation rounds: N
- Total queries run: N
- Per-query yield quality: [brief assessment]

## 2. Per-Section Coverage Analysis

For EACH content section in the article guideline, skip preamble/metadata sections
(e.g., "Global Context", "Anchoring", "Narrative Flow", "Outline", "Golden Sources",
"Other Sources", "Article Code"). Cover only the numbered content sections.

### S{{N}} — {{exact section title from guideline}}
**Coverage: STRONG|PARTIAL|WEAK**
**What we have:** [Write 3-5 detailed sentences. Name specific source files that
contribute. Cite concrete facts, numbers, benchmarks, tools, frameworks, or API
names found in the sources. Explain how the sources map to this section's needs.
For example: "building-effective-agents-anthropic.md provides the 5-pattern taxonomy
(chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) with
code examples for each. Tavily rounds 3-5 surfaced 12 additional case studies..."]
**Remaining depth gaps:** [List 2-4 specific sub-topics that lack detailed coverage.
Be precise — name the exact concept or technique missing, not vague categories.]
**Remaining breadth gaps:** [List 1-3 specific adjacent topics not covered at all.
Name the exact topic, tool, or framework that would complement this section.]

(Repeat for every content section)

## 3. Overall Gap Profile
- **Gap counts:** depth_gaps=N, breadth_gaps=N (summed across all sections)
- **Weakest sections:** [comma-separated]
- **Strongest sections:** [comma-separated]
- **Gap character:** [one sentence on dominant gap type and pattern]
- **Query saturation:** [assessment of whether existing queries cover the search space well]
- **Key insight for exploration strategy:** [one actionable sentence on what additional exploration would most improve article quality]
"""


async def generate_digest(
    client,
    article_title: str,
    context: str,
    dry_run: bool,
) -> str:
    """Generate the full structured digest (Stage 4)."""
    if dry_run:
        return (
            f"# Exploitation Digest — {article_title}\n\n"
            "## 1. Source Inventory\n\n### Golden Sources\n[DRY-RUN]\n\n"
            "### Exploitation Sources\n[DRY-RUN]\n\n### Tavily Exploitation Results\n[DRY-RUN]\n\n"
            "## 2. Per-Section Coverage Analysis\n\n### S1 — Introduction\n"
            "**Coverage: PARTIAL**\n**What we have:** [DRY-RUN]\n"
            "**Remaining depth gaps:** [DRY-RUN]\n**Remaining breadth gaps:** [DRY-RUN]\n\n"
            "## 3. Overall Gap Profile\n- **Gap counts:** depth_gaps=0, breadth_gaps=0\n"
            "- **Weakest sections:** [DRY-RUN]\n- **Strongest sections:** [DRY-RUN]\n"
            "- **Gap character:** [DRY-RUN]\n- **Query saturation:** [DRY-RUN]\n"
            "- **Key insight for exploration strategy:** [DRY-RUN]\n"
        )

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
                ),
            },
        ],
        max_tokens=16384,
    )
    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------------
# Stage 5: VALIDATE
# ---------------------------------------------------------------------------

_REQUIRED_HEADERS = [
    "## 1. Source Inventory",
    "### Golden Sources",
    "### Exploitation Sources",
    "### Tavily Exploitation Results",
    "## 2. Per-Section Coverage Analysis",
    "## 3. Overall Gap Profile",
]

_COVERAGE_PATTERN = re.compile(r"\*\*Coverage:\s*(STRONG|PARTIAL|WEAK)\*\*")

# Strips "Section N - " / "Section N: " / "Section - " prefixes from guideline titles.
# The model generates "S{N} — {description}" so we match on the description part only.
_SECTION_PREFIX_RE = re.compile(r'^Section\s+\w*\s*[-:]\s*', re.IGNORECASE)


def _strip_section_prefix(title: str) -> str:
    """Return the descriptive part of a section title, stripping the 'Section N -' prefix."""
    stripped = _SECTION_PREFIX_RE.sub('', title).strip()
    return stripped if stripped else title


def _extract_content_sections(guideline: str) -> list[str]:
    """Return article content section titles, excluding preamble/metadata sections."""
    sections = []
    for line in guideline.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            if not any(kw in title.lower() for kw in _SKIP_SECTION_KEYWORDS):
                sections.append(title)
    return sections


def validate_digest(digest: str, guideline: str) -> tuple[bool, list[str]]:
    """Validate digest structure. Returns (passed, list_of_issues)."""
    issues = []

    for header in _REQUIRED_HEADERS:
        if header not in digest:
            issues.append(f"Missing required header: {header!r}")

    content_sections = _extract_content_sections(guideline)
    for title in content_sections:
        # Match on the description part only (after "Section N - ").
        # The model generates "S{N} — {description}" so the prefix differs.
        description = _strip_section_prefix(title)
        if description.lower() not in digest.lower():
            issues.append(f"Content section not found in coverage analysis: {title!r}")

    if not _COVERAGE_PATTERN.search(digest):
        issues.append("No STRONG|PARTIAL|WEAK coverage ratings found")

    token_est = len(digest) // 4
    if token_est < 1_000:
        issues.append(f"Digest too short (~{token_est} tokens; minimum 1,000)")
    if token_est > 24_000:
        issues.append(f"Digest too long (~{token_est} tokens; maximum 24,000)")

    return len(issues) == 0, issues


# ---------------------------------------------------------------------------
# Per-article orchestration
# ---------------------------------------------------------------------------

async def process_article(
    client,
    article_dir: str,
    dry_run: bool,
    force: bool,
) -> bool:
    """Run the full 6-stage pipeline for one article. Returns True on success."""
    base_dir = _BASES_DIR / article_dir
    output_path = base_dir / "research_digest.md"
    article_title = ARTICLES[article_dir]

    log.info("=" * 65)
    log.info(f"Article: {article_dir}  ({article_title})")

    if output_path.exists() and not force:
        log.info(f"  SKIP — research_digest.md already exists (use --force to overwrite)")
        return True

    # Stage 1
    log.info("  Stage 1: COLLECT")
    sources = collect_sources(base_dir)
    counts = {k: len(v) for k, v in sources.items() if isinstance(v, dict)}
    log.info(f"    {counts}")

    total_sources = sum(counts.values())
    log.info(f"  Stage 2: COMPRESS ({total_sources} sources, concurrency={_COMPRESS_CONCURRENCY})")
    summaries = await compress_all_sources(client, article_title, sources, dry_run)

    # Stage 3
    log.info("  Stage 3: ASSEMBLE")
    context = assemble_context(sources, summaries)
    log.info(f"    Assembled context: ~{len(context) // 4:,} tokens")

    # Stage 4+5 with retries
    digest: str | None = None
    if dry_run:
        # In dry-run mode the stub output is not a real digest; skip validation.
        digest = await generate_digest(client, article_title, context, dry_run)
        log.info("  Stage 5: VALIDATE — skipped (dry-run)")
    else:
        for attempt in range(1, 4):
            candidate = await generate_digest(client, article_title, context, dry_run)

            log.info(f"  Stage 5: VALIDATE (attempt {attempt})")
            ok, issues = validate_digest(candidate, sources["guideline"])

            if ok:
                digest = candidate
                log.info("    Validation PASSED")
                break
            else:
                log.warning(f"    Validation FAILED:")
                for issue in issues:
                    log.warning(f"      • {issue}")
                if attempt == 3:
                    log.error("    All 3 attempts failed — saving last candidate anyway.")
                    digest = candidate

    # Stage 6
    log.info("  Stage 6: STORE")
    if not dry_run:
        output_path.write_text(digest, encoding="utf-8")
        log.info(f"    Written: {output_path}")
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

    log.info(f"Digest pipeline — model={MODEL}, dry_run={dry_run}, force={force}")
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
        description="Generate exploitation digests for RL training articles."
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        choices=list(ARTICLES.keys()),
        default=list(ARTICLES.keys()),
        metavar="ARTICLE",
        help=(
            "Articles to process (default: all 5). "
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
