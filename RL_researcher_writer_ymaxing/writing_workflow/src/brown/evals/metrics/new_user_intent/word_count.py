"""Deterministic prose word-count utilities for the guideline_adherence length check.

LLMs are unreliable at precisely counting words in long text. Since the word-count
methodology (see word_count_methodology_memo.md) is a fully mechanical algorithm, it is
implemented here in code and the resulting exact counts are injected into the grading
prompt as ground truth -- the grading LLM looks the count up instead of recounting it.

The section-splitting rules mirror SYSTEM_PROMPT point 8 in prompts.py (H2-delimited
sections, with the Introduction allowed to appear before the first H2 and merged with an
explicit "## Introduction" H2 if both are present). The "References" section is always
excluded, matching the memo.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_H2_LINE_RE = re.compile(r"^##[ \t]+(.+?)[ \t]*$", re.MULTILINE)
_H1_LINE_RE = re.compile(r"^#[ \t]+.*$", re.MULTILINE)
_FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_TABLE_ROW_RE = re.compile(r"^[ \t]*\|.*\|[ \t]*$")
_CAPTION_LINE_RE = re.compile(r"^[ \t]*Image[ \t]+\d+[ \t]*:", re.IGNORECASE)
_BARE_URL_LINE_RE = re.compile(r"^[ \t]*<?https?://\S+>?[ \t]*$")
_IMAGE_EMBED_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
# Citation markers: the spec'd `[[N]](url)` plus, defensively, single-bracket `[N](url)`.
_CITATION_RE = re.compile(r"\[\[\d+\]\]\([^)]*\)|\[\d+\]\([^)]*\)")
_MD_FORMAT_CHARS_RE = re.compile(r"[#*_`>]")
# Em/en-dash joining two words with no surrounding whitespace (e.g. "mindset—questioning")
# is a word separator, not part of a compound word -- unlike a real hyphen ("well-known").
_DASH_JOIN_RE = re.compile(r"(?<=[A-Za-z])[\u2013\u2014](?=[A-Za-z])")
_HAS_ALNUM_RE = re.compile(r"[A-Za-z0-9]")


@dataclass(frozen=True)
class SectionWordCount:
    """The exact prose-only word count for one H2-delimited section of an article."""

    title: str
    prose_word_count: int


def split_into_sections(article_markdown: str) -> list[tuple[str, str]]:
    """Split article markdown into (title, body) pairs using H2 boundaries.

    Any content before the first H2 belongs to the Introduction. If the first H2 is
    itself titled "Introduction", pre-H2 content (e.g. a lead image) is merged into it
    rather than kept as a separate, orphaned section. "References" is always dropped.
    """
    matches = list(_H2_LINE_RE.finditer(article_markdown))
    if not matches:
        return [("Introduction", _H1_LINE_RE.sub("", article_markdown).strip())]

    pre_h2_content = _H1_LINE_RE.sub("", article_markdown[: matches[0].start()]).strip()
    first_title = matches[0].group(1).strip()

    sections: list[tuple[str, str]] = []
    start_idx = 0

    if first_title.lower() == "introduction":
        body_start = matches[0].end()
        body_end = matches[1].start() if len(matches) > 1 else len(article_markdown)
        body = article_markdown[body_start:body_end].strip()
        merged = f"{pre_h2_content}\n\n{body}".strip() if pre_h2_content else body
        sections.append(("Introduction", merged))
        start_idx = 1
    elif pre_h2_content:
        sections.append(("Introduction", pre_h2_content))

    for i in range(start_idx, len(matches)):
        title = matches[i].group(1).strip()
        if title.lower() == "references":
            continue
        body_start = matches[i].end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(article_markdown)
        sections.append((title, article_markdown[body_start:body_end].strip()))

    return sections


def compute_prose_word_count(section_text: str) -> int:
    """Compute the exact prose-only word count of one section's markdown text.

    Excludes fenced code blocks (including Mermaid), table rows, image/diagram caption
    lines, bare image-placeholder URL lines, image embeds, and inline citation markers.
    Strips markdown formatting characters without removing the words they wrap, splits
    em/en-dash-joined words, and discards any stray punctuation-only tokens left behind
    (e.g. a lone "." after a citation marker right before a period is removed).
    """
    text = _FENCED_CODE_RE.sub(" ", section_text)

    kept_lines = [
        line
        for line in text.splitlines()
        if not (_TABLE_ROW_RE.match(line) or _CAPTION_LINE_RE.match(line) or _BARE_URL_LINE_RE.match(line))
    ]
    text = "\n".join(kept_lines)

    text = _IMAGE_EMBED_RE.sub(" ", text)
    text = _CITATION_RE.sub(" ", text)
    text = _DASH_JOIN_RE.sub(" ", text)
    text = _MD_FORMAT_CHARS_RE.sub(" ", text)

    return sum(1 for token in text.split() if _HAS_ALNUM_RE.search(token))


def compute_section_word_counts(article_markdown: str) -> list[SectionWordCount]:
    """Compute the exact prose-only word count for every section of the article."""
    return [
        SectionWordCount(title=title, prose_word_count=compute_prose_word_count(body))
        for title, body in split_into_sections(article_markdown)
    ]


def to_prompt_block(section_counts: list[SectionWordCount]) -> str:
    """Render pre-computed section word counts as a plain-text block for prompt injection."""
    if not section_counts:
        return "(no H2-delimited sections detected in the generated article)"
    return "\n".join(f'- "{sc.title}": {sc.prose_word_count} words' for sc in section_counts)
