"""GitHub-specific utilities."""

import logging
import re
from pathlib import Path
from urllib.parse import urlparse

from gitingest import ingest_async

logger = logging.getLogger(__name__)


def _normalize_github_url(url: str) -> str:
    """Normalise a GitHub URL before passing it to gitingest.

    ``gitingest`` pins the branch to the commit that is current *at clone time*
    and then performs a sparse checkout of the requested subpath.  When the URL
    points to a single file via ``/blob/<branch>/path/to/file``, the file may
    not exist at that pinned commit (e.g. it was added later), causing a
    ``ValueError: <repo> cannot be found``.

    To avoid this, single-file blob URLs are converted to their parent-directory
    tree URL (``/tree/<branch>/path/to/``), so gitingest ingests the whole
    directory instead of failing on a missing file.

    All other GitHub URLs are returned unchanged.
    """
    parsed = urlparse(url)
    if "github.com" not in parsed.netloc:
        return url

    # Match /blob/<ref>/path/to/file  (at least owner/repo/blob/ref/something)
    parts = [p for p in parsed.path.split("/") if p]
    # parts: [owner, repo, "blob", ref, ...path_parts...]
    try:
        blob_idx = parts.index("blob")
    except ValueError:
        return url  # not a blob URL — leave as-is

    path_parts = parts[blob_idx + 2 :]  # everything after blob/<ref>
    if not path_parts:
        return url  # no subpath — leave as-is

    # If the last segment looks like a file (has an extension), convert to the
    # parent directory tree URL; otherwise leave as-is (already a directory).
    last = path_parts[-1]
    if "." not in last:
        return url  # already a directory path

    ref = parts[blob_idx + 1]
    owner_repo = "/".join(parts[:blob_idx])
    parent_dir = "/".join(path_parts[:-1])

    # Build the tree URL for the parent directory
    if parent_dir:
        new_path = f"/{owner_repo}/tree/{ref}/{parent_dir}"
    else:
        # File is at repo root — fall back to ingesting the whole repo
        new_path = f"/{owner_repo}"

    normalized = parsed._replace(path=new_path).geturl()
    logger.info(f"Normalised GitHub URL: {url!r} → {normalized!r}")
    return normalized


async def process_github_url(url: str, dest_folder: Path, token: str | None) -> bool:
    """Fetch a GitHub repository (or file) with gitingest and write a Markdown report."""
    ingestion_succeeded = False
    ingest_url = _normalize_github_url(url)
    try:
        summary, tree, content = await ingest_async(ingest_url, exclude_patterns="*.lock", token=token)
        ingestion_succeeded = True
        md = (
            f"# Repository analysis for {url}\n\n"
            f"## Summary\n{summary}\n\n"
            f"## File tree\n```{tree}\n```\n\n"
            f"## Extracted content\n{content}"
        )
    except Exception as e:
        md = f"# Error processing {url}\n\n{e}"
        logger.error(f"Error processing repository {url}: {e}", exc_info=True)

    # Regex for markdown-style base64 images: ![...](data:image/...)
    md = re.sub(r"!\[[^\]]*\]\(data:image/[^;]+;base64,[^\)]+\)", "[... base64 image removed ...]", md)
    # Regex for HTML-style base64 images: <img src="data:image/...">
    md = re.sub(r'<img[^>]+src="data:image/[^;]+;base64,[^"]+"[^>]*>', "[... base64 image removed ...]", md)
    # Regex for naked base64 image data starting with common magic numbers.
    md = re.sub(
        r"(?:iVBOR|/9j/|R0lGOD|UklGR)[A-Za-z0-9+/=\s]{100,}", "[... base64 image removed ...]", md, flags=re.IGNORECASE
    )

    # Check if content is too long and truncate if necessary
    MAX_CHARS = 65_000
    if len(md) > MAX_CHARS:
        logger.warning(f"⚠️ Warning: Content for {url} is {len(md)} characters, truncating to {MAX_CHARS} characters")
        md = md[:MAX_CHARS] + "\n\n[... Content truncated due to length ...]"

    # Construct a filename that reflects the repo (owner_repo.md) or fallback to sanitized URL
    parsed = urlparse(url)
    parts = [p for p in parsed.path.strip("/").split("/") if p]
    if len(parts) >= 2:
        dest_name = f"{parts[0]}_{parts[1]}.md"
    else:
        dest_name = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".md"

    dest_path = dest_folder / dest_name
    dest_path.write_text(md, encoding="utf-8")
    if ingestion_succeeded:
        logger.info(f"Successfully processed repository {url} and wrote  {dest_path}")

    return ingestion_succeeded
