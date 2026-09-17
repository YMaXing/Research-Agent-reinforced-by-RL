"""URL normalisation helpers for reference-URL blocklist matching."""

from __future__ import annotations

import re
from urllib.parse import urlsplit

# arXiv identifier, e.g. ``2205.12293`` optionally followed by a version (``v2``).
_ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")


def normalize_url_for_match(url: str) -> str:
    """Return a canonical form of *url* suitable for equality comparison.

    The goal is to treat URLs that point at the *same underlying resource* as
    equal, so a reference-only URL listed in an article guideline can be matched
    against the (often slightly different) URL that Tavily later rediscovers.

    Normalisation rules:
    - strip surrounding whitespace and angle brackets ``<>``;
    - lower-case the host and drop a leading ``www.``;
    - drop the scheme (so ``http``/``https`` variants match) and the URL
      fragment (``#…``);
    - strip a trailing ``.pdf`` suffix and any trailing slash from the path;
    - arXiv URLs collapse to ``arxiv.org/abs/<id>`` regardless of ``/abs/`` vs
      ``/pdf/``, a ``.pdf`` suffix, or a version suffix (``v1``/``v2``/…).

    Returns an empty string for falsy / unparseable input.
    """
    if not url:
        return ""
    cleaned = url.strip().strip("<>").strip()
    if not cleaned:
        return ""

    try:
        parts = urlsplit(cleaned)
    except ValueError:
        return cleaned.lower()

    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path

    # arXiv canonicalisation — match abs/pdf, versions, and a .pdf suffix.
    if "arxiv.org" in host:
        m = _ARXIV_ID_RE.search(path)
        if m:
            return f"arxiv.org/abs/{m.group(1)}"

    if path.lower().endswith(".pdf"):
        path = path[:-4]
    path = path.rstrip("/")

    key = f"{host}{path}"
    if parts.query:
        key = f"{key}?{parts.query}"
    return key
