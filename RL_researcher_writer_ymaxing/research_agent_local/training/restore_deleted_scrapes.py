"""
Restore two deleted scraped files:

Problem 1 (preset2): Medium article was LLM-cleaned to empty.
  → Re-scrape WITHOUT LLM cleaning (save raw Firecrawl content).
  → Regenerate research.md for preset2.

Problem 2 (preset4): Hippocampal PDF file was deleted.
  → Re-scrape and restore the file.
  → Do NOT regenerate research.md (it's already correct without the reference).
"""
import asyncio
import sys
from pathlib import Path

_TRAINING_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _TRAINING_DIR.parent / "mcp_server"
sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv
load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

from firecrawl import AsyncFirecrawl
from src.app.scraping_handler import scrape_url
from src.config.settings import settings
from src.tools.create_research_file_tool import create_research_file_tool

EPISODES_DIR = _TRAINING_DIR.parent.parent / "rl_training_data" / "episodes"

MEDIUM_URL = "https://medium.com/@richardhightower/agent-memory-the-key-to-salient-episodic-memory-for-ai-agents-70b0f8e296db"
MEDIUM_FILENAME = "agent-memory-the-key-to-salient-episodic-memory-for-ai-agents.md"
MEDIUM_PHASE = "[EXPLORATION]"
PRESET2_DIR = EPISODES_DIR / "10_memory_knowledge_access__preset2"
PRESET2_SCRAPES = PRESET2_DIR / ".research" / "urls_from_research"

HIPPO_URL = "http://people.whitman.edu/~herbrawt/hippocampus.pdf"
HIPPO_FILENAME = "the-hippocampal-indexing-theory-and-episodic-memory-updating.md"
HIPPO_PHASE = "[EXPLORATION]"
PRESET4_DIR = EPISODES_DIR / "10_memory_knowledge_access__preset4"
PRESET4_SCRAPES = PRESET4_DIR / ".research" / "urls_from_research"


async def restore_file(url: str, phase: str, out_path: Path, label: str) -> None:
    """Scrape url with raw Firecrawl (no LLM cleaning) and save to out_path."""
    key = settings.firecrawl_api_key
    firecrawl_app = AsyncFirecrawl(api_key=key.get_secret_value())

    print(f"[{label}] Scraping {url} ...", flush=True)
    result = await scrape_url(url, firecrawl_app, use_cache=False)

    if not result.get("success"):
        print(f"[{label}] ⚠️  Scrape failed: {result.get('markdown', '')[:200]}", flush=True)
        return

    title = result.get("title", "")
    raw_md = result.get("markdown", "")
    tokens_approx = len(raw_md.split())
    print(f"[{label}] ✓ Got {tokens_approx} approx-words. Title: {title!r}", flush=True)

    # Build header matching the existing scraped-file format
    url_header = f"# Title: {title}\n# URL: {url}\n\n"
    phase_header = f"Phase: {phase}\n\n"
    content = f"{phase_header}{url_header}{raw_md}"

    out_path.write_text(content, encoding="utf-8")
    print(f"[{label}] ✅ Saved → {out_path}", flush=True)


async def main() -> None:
    # --- Problem 1: Medium article (preset2) ---
    medium_out = PRESET2_SCRAPES / MEDIUM_FILENAME
    await restore_file(MEDIUM_URL, MEDIUM_PHASE, medium_out, "preset2/medium")

    # Regenerate research.md for preset2 to include the restored content
    print("\n[preset2] Regenerating research.md ...", flush=True)
    res = create_research_file_tool(str(PRESET2_DIR))
    print(f"  {res.get('status')}: {res.get('message')}", flush=True)

    # --- Problem 2: Hippocampal PDF (preset4) ---
    hippo_out = PRESET4_SCRAPES / HIPPO_FILENAME
    await restore_file(HIPPO_URL, HIPPO_PHASE, hippo_out, "preset4/hippocampal")
    print("\n[preset4] research.md NOT regenerated (reference already removed).", flush=True)

    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
