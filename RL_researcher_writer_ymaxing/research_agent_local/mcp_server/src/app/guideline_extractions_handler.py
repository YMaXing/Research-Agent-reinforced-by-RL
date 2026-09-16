"""Text processing utilities for URL and file extraction."""

import json
import re
from pathlib import Path

from ..config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)
from ..utils.url_utils import normalize_url_for_match


# ---------------------------------------------------------------------------
# Section-aware classification helpers
# ---------------------------------------------------------------------------

_GOLDEN_SECTION_KEYWORDS = ("golden sources", "code", "notebook")


def _classify_section(header_lower: str) -> str:
    """Return 'golden' for a stripped, lower-cased H2 header text.

    Only the "Golden Sources" section and an independent code/notebook block (any
    header containing "code" or "notebook", e.g. "Lesson Code", "Article Code",
    "Notebooks") are golden. Every other section — "Other Sources", "Documentation",
    any other named section, or text before the first H2 heading — is exploitation.
    """
    for kw in _GOLDEN_SECTION_KEYWORDS:
        if kw in header_lower:
            return "golden"
    return "exploitation"


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    """Return items with duplicates removed, keeping first-seen order."""
    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def extract_urls_by_section(text: str) -> dict[str, list[str]]:
    """
    Extract URLs and classify them as 'golden' or 'exploitation' based on their H2 section.

    Section rules (matched by lower-cased header text):
    - ``## Golden Sources``, or any independent code/notebook block (header containing
      "code" or "notebook", e.g. ``## Lesson Code``, ``## Article Code``, ``## Notebooks``)
      → golden.
    - Everything else — ``## Other Sources``, ``## Documentation``, any other named
      section, or text before the first H2 heading → exploitation.
    - If a URL is found under a golden section anywhere in the document, that URL is
      always reported as golden even if it also appears elsewhere (e.g. quoted inline
      within a lesson section) — golden classification takes precedence.

    Args:
        text: The full article guideline text.

    Returns:
        A dict with keys ``"golden"`` and ``"exploitation"``, each mapping to a
        de-duplicated, order-preserving list of URLs found in that section type.
    """
    golden_urls: list[str] = []
    exploitation_urls: list[str] = []

    # Split on H2 headings, keeping each part together with its heading
    parts = re.split(r"(?m)^(?=## )", text)

    for part in parts:
        if not part.strip():
            continue
        first_line = part.split("\n", 1)[0]
        header_lower = first_line.lstrip("#").strip().lower() if re.match(r"^## ", first_line) else ""
        section_type = _classify_section(header_lower)

        for url in extract_urls(part):
            if section_type == "exploitation":
                exploitation_urls.append(url)
            else:
                golden_urls.append(url)

    golden = _dedupe_preserve_order(golden_urls)
    golden_set = set(golden)
    exploitation = [u for u in _dedupe_preserve_order(exploitation_urls) if u not in golden_set]
    return {"golden": golden, "exploitation": exploitation}


def extract_urls(text: str) -> list[str]:
    """Extract all HTTP/HTTPS URLs from the given text, skipping image files.

    Image URLs (ending in .webp, .jpg, .jpeg, .png, .gif, .svg, .bmp, .ico,
    .tiff, .avif) are excluded because they are writing directives ("Insert an
    image with the URL …"), not research sources to scrape.
    """
    _IMAGE_EXTS = re.compile(
        r"\.(webp|jpe?g|png|gif|svg|bmp|ico|tiff?|avif)(\?[^\s)>\"',]*)?$",
        re.IGNORECASE,
    )
    # Strip HTML comments first so URLs inside <!-- ... --> are not extracted.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Backtick excluded so a URL wrapped in `...` (inline code span) doesn't swallow the
    # closing backtick, which would otherwise defeat the image-extension check below.
    url_pattern = re.compile(r"https?://[^\s)>\"',`]+")
    return [u for u in url_pattern.findall(text) if not _IMAGE_EXTS.search(u)]


def extract_url_titles(text: str) -> dict[str, str]:
    """Extract {url: title} mapping from markdown links [title](url) in text.

    HTML comments (<!-- ... -->) are stripped first so that paywalled-URL
    comments of the form <!-- [Title](URL) --> do not leak into the mapping.
    """
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
    return {url: title.strip() for title, url in pattern.findall(text)}


def extract_local_paths(text: str) -> list[str]:
    """Extract local file paths referenced on their own line inside double quotes.

    Matches lines whose *entire content* (ignoring surrounding whitespace) is a
    quoted filename, e.g.:

        "Evolution and tinkering.md"
        "src/main.py"

    A line-anchored pattern is used deliberately so that inline prose quotes like
        ``"The bird retina is one of the most metabolically active tissues..."``
    are never mistaken for local-file references, even when the opening quote uses
    ASCII U+0022 while the closing quote uses a curly character (U+201D).

    Accepted extensions: .py  .ipynb  .md
    """
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Match a line whose only content (after optional whitespace) is a quoted
    # filename with one of the accepted extensions.  Both straight (U+0022) and
    # curly (U+201C / U+201D) opening/closing quote variants are accepted.
    _OPEN_Q  = r'["\u201c]'
    _CLOSE_Q = r'["\u201d]'
    line_pattern = re.compile(
        rf'^\s*{_OPEN_Q}([^"\u201c\u201d\n]+\.(?:py|ipynb|md)){_CLOSE_Q}\s*$',
        re.MULTILINE | re.IGNORECASE,
    )

    local_files: list[str] = []
    for m in line_pattern.finditer(text):
        filename = m.group(1).strip()
        if not re.match(r"https?://", filename, re.IGNORECASE) and filename not in local_files:
            local_files.append(filename)
    return local_files


def extract_local_paths_by_section(text: str) -> dict[str, list[str]]:
    """Extract local file references and classify them as 'golden' or 'exploitation'.

    Uses the same section-classification rules as :func:`extract_urls_by_section`:
    "Golden Sources" and independent code/notebook blocks → golden; everything else →
    exploitation. Golden classification takes precedence for a path found in both.

    Returns:
        ``{"golden": [...], "exploitation": [...]}``, each de-duplicated and
        order-preserving.
    """
    golden_paths: list[str] = []
    exploitation_paths: list[str] = []

    parts = re.split(r"(?m)^(?=## )", text)
    for part in parts:
        if not part.strip():
            continue
        first_line = part.split("\n", 1)[0]
        header_lower = first_line.lstrip("#").strip().lower() if re.match(r"^## ", first_line) else ""
        section_type = _classify_section(header_lower)

        for path in extract_local_paths(part):
            if section_type == "exploitation":
                exploitation_paths.append(path)
            else:
                golden_paths.append(path)

    golden = _dedupe_preserve_order(golden_paths)
    golden_set = set(golden)
    exploitation = [p for p in _dedupe_preserve_order(exploitation_paths) if p not in golden_set]
    return {"golden": golden, "exploitation": exploitation}


# ---------------------------------------------------------------------------
# Reference-only URL handling
# ---------------------------------------------------------------------------
#
# Article guidelines list a locally-supplied source using the convention:
#
#     <!-- [Title](https://arxiv.org/abs/2205.12293) -->
#     "Evolving Dark Sector and the Dark Dimension Scenario.md"
#
# The file content is provided locally, so the commented-out URL is *reference
# only* and must never be scraped or picked up as a research source. Without
# this guard, Tavily can rediscover the same URL during the exploitation /
# exploration phases and it gets fully scraped again in step 6 — wasting API
# credits and duplicating content in the downstream writer context.


def extract_local_file_reference_urls(text: str) -> list[str]:
    """Extract reference-only URLs commented out directly above a local-file line.

    A URL qualifies when it appears inside one or more HTML comments that are
    immediately followed (ignoring blank lines) by a line whose sole content is a
    quoted local-file reference (``.py`` / ``.ipynb`` / ``.md``). Any other
    intervening content breaks the pairing so unrelated commented URLs elsewhere
    in the guideline are not captured.

    Returns an order-preserving, de-duplicated list of the raw URLs.
    """
    _open_q = r'["\u201c]'
    _close_q = r'["\u201d]'
    local_file_line = re.compile(
        rf'^\s*{_open_q}[^"\u201c\u201d\n]+\.(?:py|ipynb|md){_close_q}\s*$',
        re.IGNORECASE,
    )
    comment_line = re.compile(r"^\s*<!--.*?-->\s*$")
    url_re = re.compile(r"https?://[^\s)>\"'\]]+")

    result: list[str] = []
    pending: list[str] = []
    for line in text.splitlines():
        if comment_line.match(line):
            pending.extend(url_re.findall(line))
        elif not line.strip():
            continue  # blank line — keep any pending URLs
        elif local_file_line.match(line):
            result.extend(pending)
            pending = []
        else:
            pending = []  # any other content breaks the comment→file pairing

    seen: set[str] = set()
    deduped: list[str] = []
    for u in result:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def load_reference_url_blocklist(research_directory: str) -> set[str]:
    """Return the set of normalised reference-only URLs to exclude from research.

    Reads ``local_file_reference_urls`` from GUIDELINES_FILENAMES_FILE. For
    research directories built before that key existed, it falls back to
    re-deriving the URLs directly from the article guideline so already-generated
    bases are protected without re-running the extraction step. URLs are returned
    normalised via :func:`normalize_url_for_match` so callers can match
    rediscovered URL variants (e.g. ``/abs/`` vs ``/pdf/`` arXiv links).
    """
    research_path = Path(research_directory)
    gf_path = research_path / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE

    urls: list[str] = []
    if gf_path.exists():
        try:
            data = json.loads(gf_path.read_text(encoding="utf-8"))
            urls = list(data.get("local_file_reference_urls", []) or [])
        except (ValueError, OSError):
            urls = []

    if not urls:
        guideline_path = research_path / ARTICLE_GUIDELINE_FILE
        if guideline_path.exists():
            try:
                urls = extract_local_file_reference_urls(
                    guideline_path.read_text(encoding="utf-8")
                )
            except OSError:
                urls = []

    return {norm for u in urls if (norm := normalize_url_for_match(u))}

