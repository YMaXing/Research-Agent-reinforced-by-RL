"""Scraping cache utilities — reuse already-scraped content from sibling episodes.

When multiple episodes are generated for the same article (e.g.
``02_workflows_vs_agents__preset0``, ``preset1``, ``preset2``…), they often
select many of the same URLs to scrape.  This module lets each tool look up
whether a sibling episode has already produced a scraped file for a given URL,
and copy that file rather than making a duplicate API call.

Supported URL types
-------------------
- **web / arXiv** : matched by the ``**Source URL:** <url>`` marker embedded in
  every file written by ``write_scraped_results_to_files``.
- **GitHub**      : matched by the deterministic filename ``{owner}_{repo}.md``
  that ``process_github_url`` always produces.
- **YouTube**     : matched by the deterministic filename ``{video_id}.md`` that
  ``transcribe_youtube`` always produces.

Public API
----------
- ``find_cached_web_files(urls, sample_dir)``      → (cached, uncached)
- ``find_cached_github_files(urls, sample_dir)``   → (cached, uncached)
- ``find_cached_youtube_files(urls, sample_dir)``  → (cached, uncached)
- ``copy_cached_files(cached, target_dir, url_to_phase=None)``  → list[filename]
"""

import logging
import re
import shutil
from pathlib import Path
from urllib.parse import parse_qs, urlparse

logger = logging.getLogger(__name__)

# Regex to extract the URL from the "**Source URL:** <url>" marker.
_SOURCE_URL_RE = re.compile(r"\*\*Source URL:\*\*\s*<([^>]+)>")

# All scraping output sub-folders that live under <episode>/.research/.
# Keep this list in sync with constants.py whenever a new folder is added.
_SCRAPE_SUBFOLDERS = (
    "urls_from_guidelines",
    "urls_from_guidelines_exploitation",
    "urls_from_guidelines_youtube_videos",
    "urls_from_guidelines_code",
    "urls_from_research",
    # batch_runner renames urls_from_research → this after the no-exploration variant
    "urls_from_research_no_exploration",
)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _get_article_base_name(sample_dir: Path) -> str:
    """Return the article base name by stripping the variant/preset suffix.

    Examples
    --------
    ``02_workflows_vs_agents__preset0``        → ``02_workflows_vs_agents``
    ``02_workflows_vs_agents__var_minimal__preset2`` → ``02_workflows_vs_agents``
    """
    name = sample_dir.name
    for sep in ("__var_", "__preset"):
        idx = name.find(sep)
        if idx != -1:
            return name[:idx]
    return name


def _get_sibling_episode_dirs(sample_dir: Path) -> list[Path]:
    """Return sibling episode directories that share the same article base name."""
    parent = sample_dir.parent
    if not parent.is_dir():
        return []
    base = _get_article_base_name(sample_dir)
    return sorted(
        d
        for d in parent.iterdir()
        if d.is_dir() and d != sample_dir and _get_article_base_name(d) == base
    )


def _build_web_url_index(sibling_dir: Path) -> dict[str, Path]:
    """Return a ``{url: file_path}`` mapping for all web/arXiv scraped files in *sibling_dir*.

    Only the first 15 lines of each ``.md`` file are read to locate the
    ``**Source URL:**`` marker — this keeps the scan fast even for large files.
    """
    index: dict[str, Path] = {}
    research_dir = sibling_dir / ".research"
    if not research_dir.is_dir():
        return index
    for subfolder in _SCRAPE_SUBFOLDERS:
        folder = research_dir / subfolder
        if not folder.is_dir():
            continue
        for md_file in folder.glob("*.md"):
            try:
                head = md_file.read_text(encoding="utf-8", errors="replace")
                for line in head.splitlines()[:15]:
                    m = _SOURCE_URL_RE.search(line)
                    if m:
                        url = m.group(1).strip()
                        index.setdefault(url, md_file)
                        break
            except OSError:
                pass
    return index


def _find_file_by_name_in_siblings(filename: str, siblings: list[Path]) -> Path | None:
    """Search all known scrape sub-folders in *siblings* for a file with *filename*."""
    for sibling in siblings:
        for subfolder in _SCRAPE_SUBFOLDERS:
            candidate = sibling / ".research" / subfolder / filename
            if candidate.is_file():
                return candidate
    return None


def _github_expected_filename(url: str) -> str | None:
    """Derive the deterministic filename that ``process_github_url`` would produce."""
    parts = [p for p in urlparse(url).path.strip("/").split("/") if p]
    return f"{parts[0]}_{parts[1]}.md" if len(parts) >= 2 else None


def _youtube_expected_filename(url: str) -> str | None:
    """Derive the deterministic filename that ``transcribe_youtube`` would produce."""
    parsed = urlparse(url)
    if "youtube.com" in parsed.netloc:
        video_id = parse_qs(parsed.query).get("v", [None])[0]
    elif "youtu.be" in parsed.netloc:
        video_id = parsed.path.lstrip("/") or None
    else:
        video_id = None
    return f"{video_id}.md" if video_id else None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def find_cached_web_files(
    urls: list[str],
    sample_dir: Path,
) -> tuple[dict[str, Path], list[str]]:
    """Look up cached web / arXiv files from sibling episodes.

    Parameters
    ----------
    urls:
        URLs to look up.
    sample_dir:
        The current episode directory (used to locate siblings).

    Returns
    -------
    cached:
        Mapping ``{url: path_to_cached_file}`` for every URL that was found in
        a sibling episode.
    uncached:
        Subset of *urls* that were **not** found in any sibling.
    """
    if not urls:
        return {}, []
    siblings = _get_sibling_episode_dirs(sample_dir)
    if not siblings:
        return {}, list(urls)

    # Build a combined URL → file index from all siblings (first occurrence wins).
    url_index: dict[str, Path] = {}
    for sibling in siblings:
        for url, path in _build_web_url_index(sibling).items():
            url_index.setdefault(url, path)

    cached: dict[str, Path] = {}
    uncached: list[str] = []
    for url in urls:
        if url in url_index:
            cached[url] = url_index[url]
        else:
            uncached.append(url)
    return cached, uncached


def find_cached_github_files(
    urls: list[str],
    sample_dir: Path,
) -> tuple[dict[str, Path], list[str]]:
    """Look up cached GitHub repository files from sibling episodes."""
    if not urls:
        return {}, []
    siblings = _get_sibling_episode_dirs(sample_dir)
    if not siblings:
        return {}, list(urls)

    cached: dict[str, Path] = {}
    uncached: list[str] = []
    for url in urls:
        name = _github_expected_filename(url)
        found = _find_file_by_name_in_siblings(name, siblings) if name else None
        if found:
            cached[url] = found
        else:
            uncached.append(url)
    return cached, uncached


def find_cached_youtube_files(
    urls: list[str],
    sample_dir: Path,
) -> tuple[dict[str, Path], list[str]]:
    """Look up cached YouTube transcription files from sibling episodes."""
    if not urls:
        return {}, []
    siblings = _get_sibling_episode_dirs(sample_dir)
    if not siblings:
        return {}, list(urls)

    cached: dict[str, Path] = {}
    uncached: list[str] = []
    for url in urls:
        name = _youtube_expected_filename(url)
        found = _find_file_by_name_in_siblings(name, siblings) if name else None
        if found:
            cached[url] = found
        else:
            uncached.append(url)
    return cached, uncached


def copy_cached_files(
    cached: dict[str, Path],
    target_dir: Path,
    url_to_phase: dict[str, str] | None = None,
) -> list[str]:
    """Copy cached scraped files into *target_dir*.

    If *url_to_phase* is provided and contains the URL, the ``Phase:`` header
    line in the destination file is updated so that phase-based provenance
    tagging remains correct for the current episode.

    Parameters
    ----------
    cached:
        ``{url: source_file_path}`` mapping returned by one of the
        ``find_cached_*`` helpers.
    target_dir:
        Directory to copy files into (created if it does not exist).
    url_to_phase:
        Optional ``{url: phase_label}`` mapping (e.g. ``"[EXPLOITATION]"``).
        When supplied, the destination file's first ``Phase:`` line is
        rewritten to match the current episode's phase assignment.

    Returns
    -------
    list[str]
        Filenames (not full paths) of files that were successfully copied or
        were already present in *target_dir*.
    """
    if not cached:
        return []
    target_dir.mkdir(parents=True, exist_ok=True)
    copied_names: list[str] = []

    for url, src_path in cached.items():
        dest = target_dir / src_path.name
        if not dest.exists():
            try:
                shutil.copy2(src_path, dest)
                # Use the grandparent of .research/<subfolder>/<file> as the
                # episode name for the log message.
                try:
                    origin = src_path.parent.parent.parent.name
                except AttributeError:
                    origin = "sibling"
                logger.info("Cache hit [%s]: copied %s", origin, src_path.name)
            except OSError as e:
                logger.warning("Cache: failed to copy %s → %s: %s", src_path, dest, e)
                continue
        else:
            logger.debug("Cache: destination already exists, skipping copy: %s", dest.name)

        # Optionally correct the Phase header so downstream provenance tagging
        # reflects this episode's phase assignment, not the sibling's.
        if url_to_phase and url in url_to_phase:
            _update_phase_header(dest, url_to_phase[url])

        copied_names.append(src_path.name)

    return copied_names


def _update_phase_header(file_path: Path, new_phase: str) -> None:
    """Rewrite the ``Phase:`` header line in *file_path* to *new_phase*."""
    try:
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines(keepends=True)
        new_header = f"Phase: {new_phase}\n"
        if lines and lines[0].strip().startswith("Phase:"):
            if lines[0] == new_header:
                return  # already correct — no write needed
            lines[0] = new_header
            file_path.write_text("".join(lines), encoding="utf-8")
        elif not content.startswith("Phase:"):
            # File has no Phase header yet — prepend one.
            file_path.write_text(new_header + "\n" + content, encoding="utf-8")
    except OSError as e:
        logger.warning("Cache: failed to update phase header in %s: %s", file_path, e)
