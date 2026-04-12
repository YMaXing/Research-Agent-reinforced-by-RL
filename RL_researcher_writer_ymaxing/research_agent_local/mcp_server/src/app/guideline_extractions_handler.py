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
    """Extract all HTTP/HTTPS URLs from the given text."""
    url_pattern = re.compile(r"https?://[^\s)>\"',]+")
    return url_pattern.findall(text)


def extract_local_paths(text: str) -> list[str]:
    """Extract local file paths that are referenced inside double quotes or as standalone filenames.

    We treat a reference as a local file path if it:
      • is wrapped in double quotes e.g. "code.py" or "src/main.py", OR
      • appears as a standalone filename with valid extension (e.g., at the start of a line or after whitespace)
      • does NOT start with an URL scheme such as http:// or https://
      • has a file extension that is one of: .py, .ipynb, .md
    """
    local_files = []

    # First, find anything inside double quotes
    candidate_pattern = re.compile(r'"([^"]+)"')
    quoted_candidates = candidate_pattern.findall(text)

    for c in quoted_candidates:
        c = c.strip()
        # Skip if it looks like a URL
        if re.match(r"https?://", c, re.IGNORECASE):
            continue
        # Must have one of the allowed file extensions
        if re.search(r"\.(py|ipynb|md)$", c, re.IGNORECASE):
            if c not in local_files:
                local_files.append(c)

    # Second, find standalone filenames (not wrapped in quotes)
    # Look for files that appear after whitespace or at start of line and have valid extensions
    standalone_pattern = re.compile(r'(?:^|\s)([^\s"]+\.(py|ipynb|md))(?:\s|$)', re.MULTILINE | re.IGNORECASE)
    standalone_matches = standalone_pattern.findall(text)

    for match in standalone_matches:
        filename = match[0].strip()

        # Skip if it looks like a URL
        if re.match(r"https?://", filename, re.IGNORECASE):
            continue

        # Skip if it contains URL-like patterns (has protocol or domain-like structure)
        if "://" in filename or filename.count(".") > 2:
            continue

        if filename not in local_files:
            local_files.append(filename)

    return local_files
