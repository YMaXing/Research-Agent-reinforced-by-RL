"""
Batch ground-truth scraper for the eval dataset.

Scrapes a list of URLs and saves each result as
  writing_workflow/inputs/evals/dataset/data/<slug>/article_ground_truth.md

URL routing (automatic, based on URL pattern):
  arXiv   → arxiv2markdown (highest quality) + LLM cleanup; falls back to Jina.ai
  YouTube → youtube-transcript-api transcript
  GitHub  → gitingest repository summary
  PDF     → Jina.ai Reader (avoids Firecrawl 2-column artifacts)
  Web     → Firecrawl + LLM cleanup; falls back to Jina.ai on boilerplate

Resumability:
  article_ground_truth.md already exists → skip (use --force to overwrite).

Usage (from research_agent_local/):
  uv run --project mcp_server python scrape_ground_truth.py
  uv run --project mcp_server python scrape_ground_truth.py --dry-run
  uv run --project mcp_server python scrape_ground_truth.py --slugs 04_structured_outputs 07_reasoning_planning
  uv run --project mcp_server python scrape_ground_truth.py --config path/to/articles.json
  uv run --project mcp_server python scrape_ground_truth.py --force
  uv run --project mcp_server python scrape_ground_truth.py --concurrency 2

Edit ARTICLES below to define your slug → URL mapping, or supply --config with a
JSON file of the same shape: {"<slug>": "<url>", ...}.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# Load the project .env before pydantic-settings instantiates Settings.
# pydantic-settings resolves env_file=".env" relative to CWD, but the actual
# .env lives at mcp_server/.env — so we load it explicitly here.
try:
    from dotenv import load_dotenv as _load_dotenv
    _load_dotenv(Path(__file__).parent / "mcp_server" / ".env", override=False)
except ImportError:
    pass  # python-dotenv not available; rely on env vars already being set

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("scrape_ground_truth")

# ---------------------------------------------------------------------------
# Article map — edit this dict to add/remove articles.
# Keys   : slug that becomes the subfolder name under dataset/data/
# Values : URL to scrape
# ---------------------------------------------------------------------------
ARTICLES: dict[str, str] = {
    # "04_structured_outputs": "https://example.com/structured-outputs",
    # "07_reasoning_planning": "https://example.com/reasoning-planning",
    # "13_agent_framework":    "https://example.com/agent-frameworks",
}

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent          # research_agent_local/
_REPO_ROOT = _THIS_DIR.parent                        # RL_researcher_writer_ymaxing/
OUTPUT_ROOT = (
    _REPO_ROOT
    / "writing_workflow"
    / "inputs"
    / "evals"
    / "dataset"
    / "data"
)

# ---------------------------------------------------------------------------
# URL-type detection helpers
# ---------------------------------------------------------------------------
_GITHUB_RE = re.compile(r"https?://(?:www\.)?github\.com/", re.IGNORECASE)
_YOUTUBE_RE = re.compile(
    r"https?://(?:www\.)?(?:youtube\.com/watch|youtu\.be/)", re.IGNORECASE
)
_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/", re.IGNORECASE)


def _url_type(url: str) -> str:
    """Return 'arxiv' | 'youtube' | 'github' | 'pdf' | 'web'."""
    if _ARXIV_RE.search(url):
        return "arxiv"
    if _YOUTUBE_RE.search(url):
        return "youtube"
    if _GITHUB_RE.search(url):
        return "github"
    parsed = urlparse(url)
    if parsed.path.lower().endswith(".pdf"):
        return "pdf"
    return "web"


# ---------------------------------------------------------------------------
# Per-URL scraper — dispatches to the right handler
# ---------------------------------------------------------------------------

_MATH_CONVERSION_PROMPT = """\
You are processing a markdown document scraped from the web.
The mathematical formulas were captured as unicode text instead of LaTeX
(e.g. "attn(Q,K,V)=softmax(QK⊤dk)V" instead of proper LaTeX).

Rewrite the ENTIRE document, converting every mathematical expression to
proper LaTeX that renders correctly in Markdown (KaTeX/MathJax).

RULES
-----
1.  Standalone equation lines (a line that is purely a formula)  →  $$ ... $$ (display math, blank line before and after).
2.  Short math embedded in a sentence  →  $ ... $ (inline math).
3.  Convert unicode math to LaTeX commands, for example:
      ⊤ → \\top       ∈ → \\in        ∑ → \\sum      ∏ → \\prod
      √ → \\sqrt{}    ⊙ → \\odot      ⊗ → \\otimes   ⊕ → \\oplus
      ∞ → \\infty     ≤ → \\leq       ≥ → \\geq      ≠ → \\neq
      ≈ → \\approx    ∝ → \\propto    ∣ → \\mid      ‖ → \\|
      αβγδεηθκλμνξπρστφχψω → \\alpha \\beta \\gamma \\delta \\epsilon \\eta \\theta \\kappa \\lambda \\mu \\nu \\xi \\pi \\rho \\sigma \\tau \\phi \\chi \\psi \\omega
      ΓΔΛΣΦΩ → \\Gamma \\Delta \\Lambda \\Sigma \\Phi \\Omega
4.  Reconstruct implicit fractions from context
      (e.g. "softmax(QK⊤dk)" → "\\text{{softmax}}\\left(\\frac{{QK^\\top}}{{\\sqrt{{d_k}}}}\\right)").
5.  Subscripts / superscripts that appear as concatenated letters
      (e.g. "RL×d" → "\\mathbb{{R}}^{{L\\times d}}", "hτ+1(n)" → "h_{{\\tau+1}}^{{(n)}}").
6.  Keep ALL non-mathematical text, markdown links, headers, lists, code
      blocks, and image lines EXACTLY as-is — do NOT alter them.
7.  Output the COMPLETE rewritten document with NO extra wrapper or commentary.

DOCUMENT TO CONVERT:
"""


async def fix_math_to_latex(markdown: str, chat_model) -> str:
    """Post-process scraped markdown: convert unicode math to LaTeX via LLM.

    Long documents are processed in section-level chunks so the model never
    hits its output-token ceiling.  Each chunk is converted independently and
    the results are reassembled in order.
    """
    from langchain_core.messages import HumanMessage

    # Split on H1/H2 headers so each chunk is a coherent section.
    # We keep the header line as the first line of its chunk.
    header_re = re.compile(r"^#{1,2} ", re.MULTILINE)
    splits = list(header_re.finditer(markdown))

    if not splits:
        # No headers — treat as a single chunk.
        chunks = [markdown]
    else:
        chunks = []
        positions = [m.start() for m in splits]
        # Text before first header (e.g. front-matter / table-of-contents)
        if positions[0] > 0:
            chunks.append(markdown[: positions[0]])
        for i, pos in enumerate(positions):
            end = positions[i + 1] if i + 1 < len(positions) else len(markdown)
            chunks.append(markdown[pos:end])

    converted_chunks: list[str] = []
    for i, chunk in enumerate(chunks):
        logger.debug(f"[fix-math] chunk {i + 1}/{len(chunks)}  ({len(chunk)} chars)")
        response = await chat_model.ainvoke(
            [HumanMessage(content=_MATH_CONVERSION_PROMPT + chunk)]
        )
        raw: str = response.content or ""
        result = raw.strip()

        # Strip accidental markdown fences the model may add.
        if result.startswith("```"):
            lines = result.splitlines()
            # Drop the opening fence line (e.g. ```markdown).
            result = "\n".join(lines[1:])
            # Drop the closing fence.
            if result.rstrip().endswith("```"):
                result = result.rstrip()[:-3].rstrip()

        result = result.strip()
        if not result:
            # Model returned empty/fence-only response — keep the original chunk.
            logger.warning(
                f"[fix-math] chunk {i + 1}/{len(chunks)} returned empty after "
                f"stripping — keeping original chunk unchanged."
            )
            result = chunk.strip()

        converted_chunks.append(result)

    converted = "\n\n".join(converted_chunks)
    # Collapse runs of 3+ blank lines to 2.
    converted = re.sub(r"\n{3,}", "\n\n", converted)
    return converted


async def run_fix_math(
    slugs: list[str] | None,
    chat_model,
    force: bool = False,
) -> None:
    """Standalone mode: convert unicode math to LaTeX in already-scraped files."""
    candidates: list[Path] = []
    if slugs:
        for s in slugs:
            p = OUTPUT_ROOT / s / "article_ground_truth.md"
            if p.exists():
                candidates.append(p)
            else:
                logger.warning(f"[fix-math] No file found for slug '{s}' at {p}")
    else:
        candidates = sorted(OUTPUT_ROOT.rglob("article_ground_truth.md"))

    logger.info(f"[fix-math] {len(candidates)} file(s) to convert.")
    for path in candidates:
        md = path.read_text(encoding="utf-8")
        # Skip if already contains LaTeX delimiters (unless --force).
        if not force and ("$$" in md or "$ " in md or " $" in md):
            logger.info(f"[fix-math]  SKIP (already has LaTeX)  {path}")
            continue
        logger.info(f"[fix-math]  Converting  {path}")
        converted = await fix_math_to_latex(md, chat_model)
        path.write_text(converted, encoding="utf-8")
        logger.info(
            f"[fix-math]  DONE  {path}  "
            f"({len(converted.splitlines())} lines)"
        )


async def scrape_one(
    slug: str,
    url: str,
    chat_model,
    firecrawl_app,
    katex: bool = False,
) -> dict:
    """Scrape a single URL and return {slug, url, title, markdown, success}."""
    from mcp_server.src.app.scraping_handler import (
        scrape_and_clean,
        scrape_arxiv_url,
        scrape_katex_article,
        scrape_with_jina,
    )
    from mcp_server.src.app.github_handler import process_github_url
    from mcp_server.src.app.youtube_handler import process_youtube_url

    kind = _url_type(url)
    logger.info(f"[{slug}]  type={kind}  url={url}")

    try:
        if kind == "arxiv":
            result = await scrape_arxiv_url(url, article_guidelines="", chat_model=chat_model)

        elif kind == "youtube":
            # process_youtube_url writes to a file; we need the markdown directly.
            # Use a temp directory and read the output back.
            import tempfile
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                success = await process_youtube_url(url, dest_folder=tmp_path)
                md_files = list(tmp_path.glob("*.md"))
                if success and md_files:
                    markdown = md_files[0].read_text(encoding="utf-8")
                    result = {"url": url, "title": slug, "markdown": markdown, "success": True}
                else:
                    result = {
                        "url": url, "title": slug,
                        "markdown": f"YouTube transcription failed for {url}.",
                        "success": False,
                    }

        elif kind == "github":
            import tempfile
            from mcp_server.src.config.settings import settings
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                token = settings.github_token.get_secret_value() if settings.github_token else None
                success = await process_github_url(
                    url, dest_folder=tmp_path, token=token, title=slug
                )
                md_files = list(tmp_path.glob("*.md"))
                if success and md_files:
                    markdown = md_files[0].read_text(encoding="utf-8")
                    result = {"url": url, "title": slug, "markdown": markdown, "success": True}
                else:
                    result = {
                        "url": url, "title": slug,
                        "markdown": f"GitHub ingestion failed for {url}.",
                        "success": False,
                    }

        elif kind == "pdf":
            result = await scrape_with_jina(url)

        else:  # web
            if firecrawl_app is not None and katex:
                # KaTeX-aware path: get rawHtml from Firecrawl, extract LaTeX annotations.
                result = await scrape_katex_article(url, firecrawl_app)
            elif firecrawl_app is not None:
                result = await scrape_and_clean(
                    url,
                    article_guidelines="",   # no guideline context for ground-truth scraping
                    firecrawl_app=firecrawl_app,
                    chat_model=chat_model,
                )
            else:
                # Firecrawl key not set — fall back to Jina.ai (no API key required).
                result = await scrape_with_jina(url)

    except Exception as exc:
        logger.error(f"[{slug}]  unexpected error: {exc}", exc_info=True)
        result = {
            "url": url, "title": slug,
            "markdown": f"Error scraping {url}:\n\n{exc}",
            "success": False,
        }

    result["slug"] = slug
    return result


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------
async def run_pipeline(
    articles: dict[str, str],
    force: bool = False,
    dry_run: bool = False,
    concurrency: int = 3,
    katex_slugs: set[str] | None = None,
    fix_math: bool = False,
) -> None:
    """``katex_slugs``: slugs that should use the KaTeX-preserving scraper.
    ``fix_math``: run LLM math-to-LaTeX conversion after each successful save."""
    from mcp_server.src.config.settings import settings
    from mcp_server.src.utils.llm_utils import get_chat_model
    from firecrawl import AsyncFirecrawl

    # Categorise
    to_scrape: list[tuple[str, str]] = []
    skipped: list[str] = []
    for slug, url in articles.items():
        out_path = OUTPUT_ROOT / slug / "article_ground_truth.md"
        if out_path.exists() and not force:
            skipped.append(slug)
        else:
            to_scrape.append((slug, url))

    logger.info("=" * 70)
    logger.info("Ground-truth batch scraper")
    logger.info(f"  Output root : {OUTPUT_ROOT}")
    logger.info(f"  Total       : {len(articles)}")
    logger.info(f"  To scrape   : {len(to_scrape)}")
    logger.info(f"  Already done: {len(skipped)}  (use --force to overwrite)")
    logger.info(f"  Concurrency : {concurrency}")
    logger.info("=" * 70)

    if dry_run:
        logger.info("DRY RUN — no scraping performed.")
        for slug, url in to_scrape:
            logger.info(f"  WOULD SCRAPE  {slug:<40}  {url}")
        for slug in skipped:
            logger.info(f"  SKIP (exists) {slug}")
        return

    if not to_scrape:
        logger.info("Nothing to do.")
        return

    # Determine which URL types are in the batch.
    url_types = {_url_type(url) for _, url in to_scrape}
    needs_firecrawl = "web" in url_types and bool(settings.firecrawl_api_key)
    needs_llm = bool(url_types & {"web", "arxiv"}) and bool(settings.firecrawl_api_key)

    if "web" in url_types and not settings.firecrawl_api_key:
        logger.warning(
            "FIRECRAWL_API_KEY is not set — web URLs will be scraped via Jina.ai "
            "(no LLM cleanup). Set FIRECRAWL_API_KEY in mcp_server/.env for full quality."
        )

    firecrawl_app = (
        AsyncFirecrawl(api_key=settings.firecrawl_api_key.get_secret_value())
        if needs_firecrawl
        else None
    )
    chat_model = get_chat_model(settings.scraping_model) if needs_llm else None

    # Scrape concurrently (bounded)
    semaphore = asyncio.Semaphore(concurrency)

    async def _bounded(slug: str, url: str) -> dict:
        async with semaphore:
            use_katex = bool(katex_slugs and slug in katex_slugs)
            return await scrape_one(slug, url, chat_model, firecrawl_app, katex=use_katex)

    tasks = [_bounded(slug, url) for slug, url in to_scrape]
    results: list[dict] = await asyncio.gather(*tasks)

    # Write results
    succeeded = 0
    failed = 0
    for res in results:
        slug = res["slug"]
        out_dir = OUTPUT_ROOT / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "article_ground_truth.md"

        if res["success"] and res.get("markdown", "").strip():
            out_path.write_text(res["markdown"], encoding="utf-8")
            if fix_math and chat_model is not None:
                logger.info(f"  [fix-math] Converting math in {slug} ...")
                converted = await fix_math_to_latex(res["markdown"], chat_model)
                out_path.write_text(converted, encoding="utf-8")
                logger.info(
                    f"  SAVED  {slug}  →  {out_path}  "
                    f"({len(converted.splitlines())} lines, math converted)"
                )
            else:
                logger.info(
                    f"  SAVED  {slug}  →  {out_path}  "
                    f"({len(res['markdown'].splitlines())} lines)"
                )
            succeeded += 1
        else:
            # Write a failure marker so the user can inspect why it failed
            fail_path = out_dir / "article_ground_truth.FAILED.md"
            fail_path.write_text(res.get("markdown", "unknown error"), encoding="utf-8")
            logger.warning(
                f"  FAILED {slug}  →  failure details written to {fail_path}"
            )
            failed += 1

    logger.info("=" * 70)
    logger.info(
        f"Done — {succeeded} saved, {failed} failed, {len(skipped)} skipped."
    )
    logger.info("=" * 70)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Scrape a batch of article URLs and save each as "
            "article_ground_truth.md in the eval dataset directory."
        )
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        metavar="PATH",
        help=(
            "Path to a JSON file mapping slug → URL. "
            'Format: {"<slug>": "<url>", ...}. '
            "When provided, overrides the ARTICLES dict embedded in this script."
        ),
    )
    parser.add_argument(
        "--slugs",
        nargs="+",
        default=None,
        metavar="SLUG",
        help="Restrict scraping to these slugs (must be present in ARTICLES or --config).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite article_ground_truth.md even if it already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the plan without scraping anything.",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=3,
        metavar="N",
        help="Max concurrent scraping tasks (default: 3).",
    )
    parser.add_argument(
        "--katex",
        nargs="*",
        default=None,
        metavar="SLUG",
        help=(
            "Use the KaTeX-preserving scraper (Firecrawl rawHtml + BeautifulSoup LaTeX "
            "extraction) for web URLs. Does NOT filter which slugs are scraped — use "
            "--slugs for that. "
            "Without slug arguments (--katex) applies to all web URLs being scraped. "
            "With slug arguments (--katex A B) applies only to those slugs. "
            "Example: --slugs Transformer_Family_V2 --katex"
        ),
    )
    parser.add_argument(
        "--fix-math",
        action="store_true",
        dest="fix_math",
        help=(
            "Post-process article_ground_truth.md files with an LLM to convert "
            "unicode math symbols to proper LaTeX ($...$ / $$...$$). "
            "Can be used standalone (re-processes already-saved files, no re-scraping) "
            "or combined with --slugs to target specific articles. "
            "Files that already contain $$ are skipped unless --force is also set. "
            "Example (standalone): --slugs Transformer_Family_V2 --fix-math"
        ),
    )
    args = parser.parse_args()

    # Resolve article map
    if args.config:
        raw = args.config.read_text(encoding="utf-8")
        articles: dict[str, str] = json.loads(raw)
        logger.info(f"Loaded {len(articles)} articles from {args.config}")
    else:
        articles = dict(ARTICLES)

    if not articles:
        # --fix-math standalone needs no article map — it processes existing files.
        if args.fix_math:
            fix_slugs = args.slugs or None
            from mcp_server.src.config.settings import settings
            from mcp_server.src.utils.llm_utils import get_chat_model
            chat_model = get_chat_model(settings.scraping_model)
            asyncio.run(run_fix_math(slugs=fix_slugs, chat_model=chat_model, force=args.force))
            return
        logger.error(
            "No articles defined. Either populate the ARTICLES dict in this script "
            "or pass --config path/to/articles.json."
        )
        sys.exit(1)

    # Apply --slugs filter
    if args.slugs:
        unknown = [s for s in args.slugs if s not in articles]
        if unknown:
            logger.error(f"Unknown slug(s): {unknown}. Available: {sorted(articles)}")
            sys.exit(1)
        articles = {s: articles[s] for s in args.slugs}

    # Resolve --katex: None → not set, [] → all slugs, [slug, ...] → specific slugs.
    if args.katex is None:
        katex_slugs: set[str] | None = None
    elif len(args.katex) == 0:
        katex_slugs = set(articles.keys())
    else:
        katex_slugs = set(args.katex)

    asyncio.run(
        run_pipeline(
            articles=articles,
            force=args.force,
            dry_run=args.dry_run,
            concurrency=args.concurrency,
            katex_slugs=katex_slugs,
            fix_math=args.fix_math,
        )
    )


if __name__ == "__main__":
    main()
