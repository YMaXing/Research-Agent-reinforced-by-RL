"""
Repair script — re-scrape URLs that failed due to Firecrawl PaymentRequired errors.

The pipeline writes a ``scraping-failed*.md`` placeholder file when a URL cannot
be scraped (e.g. insufficient Firecrawl credits).  This script finds those
placeholders, re-scrapes the URLs using Jina.ai reader (free alternative to
Firecrawl), replaces the placeholders with the real content, and regenerates
research.md for each affected episode.

Special handling:
  - arXiv URLs:   uses arxiv2markdown (high-quality, already in the project).
  - PDF links:    routed to Jina.ai which handles PDFs natively.
  - All others:   Jina.ai markdown reader (https://r.jina.ai/<url>).

Usage (from research_agent_local/):
  uv run --project mcp_server python training/repair_failed_scrapes.py
  uv run --project mcp_server python training/repair_failed_scrapes.py --dry-run
  uv run --project mcp_server python training/repair_failed_scrapes.py \\
      --episodes 09_RAG__var_demanding__preset0 09_RAG__var_demanding__preset1
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import httpx

# ---------------------------------------------------------------------------
# Ensure the mcp_server package is importable
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _THIS_DIR.parent / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv  # noqa: E402
load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

# Heavy imports are deferred to avoid slow startup on Windows/WSL filesystem.
# They are loaded lazily inside functions that actually need them.
def _lazy_imports():
    """Return (scrape_arxiv_url, extract_arxiv_id, RESEARCH_OUTPUT_FOLDER,
    create_research_file_tool, get_chat_model, settings) on first call."""
    from src.app.scraping_handler import scrape_arxiv_url, extract_arxiv_id  # noqa: E402
    from src.config.constants import RESEARCH_OUTPUT_FOLDER  # noqa: E402
    from src.tools.create_research_file_tool import create_research_file_tool  # noqa: E402
    from src.utils.llm_utils import get_chat_model  # noqa: E402
    from src.config.settings import settings  # noqa: E402
    return scrape_arxiv_url, extract_arxiv_id, RESEARCH_OUTPUT_FOLDER, create_research_file_tool, get_chat_model, settings

# Eagerly import only the tiny constant we need at module level
from src.config.constants import RESEARCH_OUTPUT_FOLDER  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("repair_failed_scrapes")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_TRAINING_DATA_DIR = _THIS_DIR.parent.parent / "rl_training_data"
_EPISODES_DIR = _TRAINING_DATA_DIR / "episodes"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
JINA_BASE_URL = "https://r.jina.ai/"
JINA_TIMEOUT_SECONDS = 60
JINA_HEADERS = {
    "Accept": "text/plain",
    "X-Return-Format": "markdown",
}

# Filename pattern for placeholder files written by the pipeline
FAILED_GLOB = "scraping-failed*.md"

# Regex to extract URL and phase from placeholder file content
_URL_RE = re.compile(r'\*\*Source URL:\*\*\s*<?(\S+?)>?\s*\n')
_PHASE_RE = re.compile(r'Phase:\s*(\[.*?\])')

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class FailedScrape:
    placeholder_path: Path   # absolute path to scraping-failed*.md
    url: str
    phase: str               # e.g. "[EXPLOITATION]"
    episode_dir: Path        # episode root (not .research/)


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def parse_placeholder(path: Path) -> tuple[str, str] | None:
    """Return (url, phase) from a scraping-failed*.md file, or None if unparseable."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    url_m = _URL_RE.search(content)
    phase_m = _PHASE_RE.search(content)
    if not url_m:
        return None
    url = url_m.group(1).rstrip(">")
    phase = phase_m.group(1) if phase_m else "[EXPLOITATION]"
    return url, phase


def find_failed_scrapes(
    episodes_dir: Path,
    filter_episodes: list[str] | None = None,
) -> list[FailedScrape]:
    """Find all scraping-failed*.md files in urls_from_research/ subdirectories."""
    results: list[FailedScrape] = []
    for ep_dir in sorted(episodes_dir.iterdir()):
        if not ep_dir.is_dir():
            continue
        if filter_episodes and ep_dir.name not in filter_episodes:
            continue

        research_urls_dir = ep_dir / RESEARCH_OUTPUT_FOLDER / "urls_from_research"
        if not research_urls_dir.exists():
            continue

        for placeholder in sorted(research_urls_dir.glob(FAILED_GLOB)):
            parsed = parse_placeholder(placeholder)
            if parsed is None:
                logger.warning(f"Could not parse {placeholder}; skipping.")
                continue
            url, phase = parsed
            results.append(FailedScrape(
                placeholder_path=placeholder,
                url=url,
                phase=phase,
                episode_dir=ep_dir,
            ))

    return results


# ---------------------------------------------------------------------------
# Jina.ai scraping
# ---------------------------------------------------------------------------

async def scrape_with_jina(url: str, client: httpx.AsyncClient) -> dict:
    """
    Scrape a URL using Jina.ai reader and return {url, title, markdown, success}.

    Returns a failure dict (success=False) on any error rather than raising.
    """
    jina_url = JINA_BASE_URL + url
    try:
        response = await client.get(
            jina_url,
            headers=JINA_HEADERS,
            timeout=JINA_TIMEOUT_SECONDS,
            follow_redirects=True,
        )
        response.raise_for_status()
        markdown = response.text.strip()

        # Jina.ai may return the title in a header; fall back to first H1
        title = response.headers.get("x-title", "").strip()
        if not title:
            for line in markdown.splitlines():
                stripped = line.strip()
                if stripped.startswith("# "):
                    title = stripped[2:].strip()
                    break
        title = title or "N/A"

        return {"url": url, "title": title, "markdown": markdown, "success": bool(markdown)}
    except Exception as exc:
        logger.error(f"Jina.ai failed for {url}: {exc}")
        return {"url": url, "title": "Scraping Failed", "markdown": str(exc), "success": False}


# ---------------------------------------------------------------------------
# Core repair
# ---------------------------------------------------------------------------

def _build_file_content(url: str, phase: str, title: str, markdown_body: str) -> str:
    """Produce the canonical file format used by the pipeline."""
    # Inject title as H1 if missing from body (mirrors scrape_research_urls_tool logic)
    if (
        title
        and title.lower() not in {"n/a", "scraping failed", "scraping timeout", ""}
        and not any(ln.strip().startswith("# ") for ln in markdown_body.splitlines())
    ):
        markdown_body = f"# {title}\n\n{markdown_body}"

    url_header = f"**Source URL:** <{url}>\n\n"
    return f"Phase: {phase}\n\n{url_header}{markdown_body}"


async def repair_one(fs: FailedScrape, dry_run: bool, jina_client: httpx.AsyncClient) -> bool:
    """
    Re-scrape a single failed URL and overwrite its placeholder file.

    Returns True on success (real content written), False otherwise.
    """
    url = fs.url
    logger.info(f"[{fs.episode_dir.name}] Re-scraping {fs.phase} → {url}")

    if dry_run:
        logger.info("  [DRY-RUN] Would scrape and overwrite placeholder.")
        return False

    # ── 1. Scrape ────────────────────────────────────────────────────────────
    scrape_arxiv_url, extract_arxiv_id, _, _, get_chat_model, settings = _lazy_imports()
    arxiv_id = extract_arxiv_id(url)
    if arxiv_id:
        logger.info(f"  → arXiv detected ({arxiv_id}), using arxiv2markdown …")
        article_guidelines = _read_article_guidelines(fs.episode_dir)
        chat_model = get_chat_model(settings.scraping_model)
        result = await scrape_arxiv_url(url, article_guidelines, chat_model)
    elif url.endswith(".pdf") or "arxiv.org/pdf/" in url:
        # Non-arXiv PDF: stanford, aclanthology, etc. — try Jina.ai which can
        # extract text from PDFs.  Fall back to a plain arxiv2markdown attempt
        # if the URL contains an arXiv ID anyway.
        logger.info("  → PDF detected, using Jina.ai …")
        result = await scrape_with_jina(url, jina_client)
    else:
        logger.info("  → Using Jina.ai reader …")
        result = await scrape_with_jina(url, jina_client)

    if not result.get("success") or not result.get("markdown", "").strip():
        logger.warning(f"  ⚠️  Re-scraping returned no content for {url}. Placeholder unchanged.")
        return False

    # ── 2. Write back to placeholder file (same path, overwrite) ─────────────
    new_content = _build_file_content(
        url=url,
        phase=fs.phase,
        title=result.get("title", "N/A"),
        markdown_body=result["markdown"],
    )
    try:
        fs.placeholder_path.write_text(new_content, encoding="utf-8")
        # Rename away from scraping-failed*.md so it won't be re-detected on reruns
        stem = fs.placeholder_path.stem.replace("scraping-failed", "jina-scraped", 1)
        new_name = fs.placeholder_path.with_name(stem + ".md")
        fs.placeholder_path.rename(new_name)
        char_count = len(new_content)
        logger.info(f"  ✅ Wrote {char_count:,} chars → {new_name.name}")
        return True
    except OSError as exc:
        logger.error(f"  ❌ Could not write/rename {fs.placeholder_path}: {exc}")
        return False


def _read_article_guidelines(episode_dir: Path) -> str:
    """Read article_guideline.md from episode directory (needed for arXiv cleanup LLM)."""
    guideline_path = episode_dir / "article_guideline.md"
    if guideline_path.exists():
        return guideline_path.read_text(encoding="utf-8", errors="replace")
    return ""


async def repair_episode(
    ep_dir: Path,
    failed_in_ep: list[FailedScrape],
    dry_run: bool,
    jina_client: httpx.AsyncClient,
) -> None:
    """Repair all failed scrapes for one episode, then regenerate research.md."""
    any_repaired = False
    for fs in failed_in_ep:
        repaired = await repair_one(fs, dry_run, jina_client)
        any_repaired = any_repaired or repaired

    if not any_repaired:
        if not dry_run:
            logger.info(f"[{ep_dir.name}] No URLs successfully re-scraped; research.md unchanged.")
        return

    # Delete existing research.md so create_research_file_tool regenerates it
    research_md = ep_dir / "research.md"
    if research_md.exists() and not dry_run:
        research_md.unlink()
        logger.info(f"[{ep_dir.name}] Deleted stale research.md.")

    if dry_run:
        logger.info(f"[{ep_dir.name}] [DRY-RUN] Would regenerate research.md.")
        return

    logger.info(f"[{ep_dir.name}] Regenerating research.md …")
    _, _, _, create_research_file_tool, _, _ = _lazy_imports()
    result = create_research_file_tool(str(ep_dir))
    if result.get("status") == "success":
        logger.info(f"[{ep_dir.name}] ✅ research.md regenerated.")
    else:
        logger.error(f"[{ep_dir.name}] ❌ research.md regeneration failed: {result}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main(dry_run: bool, filter_episodes: list[str] | None) -> None:
    all_failed = find_failed_scrapes(_EPISODES_DIR, filter_episodes)

    if not all_failed:
        logger.info("✅ No failed scrape placeholders found.")
        return

    # Group by episode
    by_episode: dict[Path, list[FailedScrape]] = {}
    for fs in all_failed:
        by_episode.setdefault(fs.episode_dir, []).append(fs)

    # Summary
    unique_urls = {fs.url for fs in all_failed}
    logger.info(
        f"Found {len(all_failed)} failed placeholder(s) across "
        f"{len(by_episode)} episode(s) ({len(unique_urls)} unique URL(s)):"
    )
    for ep_dir, items in by_episode.items():
        for fs in items:
            logger.info(f"  [{ep_dir.name}] {fs.phase}  {fs.url}")

    if dry_run:
        logger.info("\n[DRY-RUN] No files will be modified.")
        return

    # Re-scrape with a shared httpx client (connection pooling)
    async with httpx.AsyncClient() as jina_client:
        for ep_dir, items in by_episode.items():
            await repair_episode(ep_dir, items, dry_run=False, jina_client=jina_client)

    logger.info("\n✅ Repair run complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Re-scrape failed Firecrawl URLs via Jina.ai")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report what would be done; do not modify any files.",
    )
    parser.add_argument(
        "--episodes",
        nargs="+",
        metavar="EPISODE",
        help="Limit repair to specific episode directory names.",
    )
    args = parser.parse_args()
    asyncio.run(main(dry_run=args.dry_run, filter_episodes=args.episodes))
