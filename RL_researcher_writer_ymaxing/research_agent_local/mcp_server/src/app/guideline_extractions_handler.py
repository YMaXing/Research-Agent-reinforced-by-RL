"""Text processing utilities for URL and file extraction."""

import re


# ---------------------------------------------------------------------------
# Section-aware classification helpers
# ---------------------------------------------------------------------------

_EXPLOITATION_SECTION_KEYWORDS = ("other sources",)
_GOLDEN_SECTION_KEYWORDS = ("golden sources", "article code", "lesson code")


def _classify_section(header_lower: str) -> str:
    """Return 'exploitation' or 'golden' for a stripped, lower-cased H2 header text."""
    for kw in _EXPLOITATION_SECTION_KEYWORDS:
        if kw in header_lower:
            return "exploitation"
    return "golden"


def extract_urls_by_section(text: str) -> dict[str, list[str]]:
    """
    Extract URLs and classify them as 'golden' or 'exploitation' based on their H2 section.

    Section rules (matched by lower-cased header text):
    - ``## Other Sources``  → exploitation
    - ``## Golden Sources``, ``## Article Code``, ``## Lesson Code``, or any other
      section (including text before the first H2 heading) → golden

    Args:
        text: The full article guideline text.

    Returns:
        A dict with keys ``"golden"`` and ``"exploitation"``, each mapping to a list
        of URLs found in that section type.
    """
    golden_urls: list[str] = []
    exploitation_urls: list[str] = []

    # Split on H2 headings, keeping each part together with its heading
    parts = re.split(r"(?m)^(?=## )", text)

    for part in parts:
        if not part.strip():
            continue
        first_line = part.split("\n", 1)[0]
        if re.match(r"^## ", first_line):
            header_lower = first_line.lstrip("#").strip().lower()
            section_type = _classify_section(header_lower)
        else:
            # Text before any H2 heading defaults to golden
            section_type = "golden"

        for url in extract_urls(part):
            if section_type == "exploitation":
                exploitation_urls.append(url)
            else:
                golden_urls.append(url)

    return {"golden": golden_urls, "exploitation": exploitation_urls}


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
    url_pattern = re.compile(r"https?://[^\s)>\"',]+")
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
    ``## Other Sources`` → exploitation; everything else → golden.

    Returns:
        ``{"golden": [...], "exploitation": [...]}``
    """
    golden: list[str] = []
    exploitation: list[str] = []

    parts = re.split(r"(?m)^(?=## )", text)
    for part in parts:
        if not part.strip():
            continue
        first_line = part.split("\n", 1)[0]
        if re.match(r"^## ", first_line):
            header_lower = first_line.lstrip("#").strip().lower()
            section_type = _classify_section(header_lower)
        else:
            section_type = "golden"

        for path in extract_local_paths(part):
            if section_type == "exploitation":
                exploitation.append(path)
            else:
                golden.append(path)

    return {"golden": golden, "exploitation": exploitation}

