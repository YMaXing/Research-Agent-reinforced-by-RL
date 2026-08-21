import re
from functools import cached_property

from loguru import logger
from pydantic import BaseModel

from brown.entities.mixins import ContextMixin
from brown.utils.a import asyncio_run, run_jobs
from brown.utils.network import is_image_url_valid


class Research(BaseModel, ContextMixin):
    content: str
    max_image_urls: int = 30

    @cached_property
    def image_urls(self) -> list[str]:
        # TODO: Add support for SVG images (now Gemini fails to process them).
        image_urls = re.findall(
            r"(?!data:image/)https?://[^\s]+\.(?:jpg|jpeg|png|bmp|webp)",
            self.content,
            re.IGNORECASE,
        )
        jobs = [is_image_url_valid(url) for url in image_urls]
        results = asyncio_run(run_jobs(jobs))

        urls = [url for url, valid in zip(image_urls, results) if valid]
        if len(urls) > self.max_image_urls:
            logger.warning(f"Found `{len(urls)} > {self.max_image_urls}` image URLs in research. Trimming to first {self.max_image_urls}.")
            urls = urls[: self.max_image_urls]

        return urls

    @property
    def is_format_a(self) -> bool:
        return self.content.lstrip().startswith("# Comprehensive Research Report")

    @property
    def _exploration_sources(self) -> str:
        """Extract all <research_source phase="exploration"> blocks from Format B content."""
        if self.is_format_a:
            return ""
        matches = re.findall(
            r'<research_source[^>]*phase=["\']exploration["\'][^>]*>.*?</research_source>',
            self.content,
            re.DOTALL | re.IGNORECASE,
        )
        return "\n\n".join(matches)

    @property
    def has_exploration_sources(self) -> bool:
        """Check if Format B research contains exploration-phase sources."""
        return not self.is_format_a and bool(self._exploration_sources)

    def to_core_context(self) -> str:
        """Return research context without exploration-phase sources (for core draft pass)."""
        if self.is_format_a:
            return self.to_context()
        stripped = re.sub(
            r'<research_source[^>]*phase=["\']exploration["\'][^>]*>.*?</research_source>',
            "",
            self.content,
            flags=re.DOTALL | re.IGNORECASE,
        )
        return f"\n<{self.xml_tag}>\n    {stripped}\n</{self.xml_tag}>\n"

    def to_reviewer_context(self) -> str:
        """Return the research context for the article reviewer.

        Previously this returned only a format summary (plus, for Format B, the extracted
        exploration-phase blocks) — the reviewer never actually saw the golden/exploitation
        source material, so it had no way to verify whether a claim in the article was really
        traceable to research and therefore required a citation. This now always includes the
        full research content so the golden/exploitation citation completeness check (which
        applies to every format) can be cross-referenced against real source text, in addition
        to the exploration integration checks (Format B only).
        """
        if self.is_format_a:
            banner = (
                "Research format: **Format A** (deduplicated). "
                "Exploration-phase content was pre-filtered upstream before the writer received the research. "
                "Skip all exploration integration checks — they do not apply to Format A articles.\n\n"
                "The deduplicated body below (everything before the `## Golden Source Reference` heading) is "
                "the authoritative factual reference for the golden/exploitation citation completeness check: "
                "treat every fact, claim, or example traceable to it with the same citation strictness as a "
                "golden source. The `## Golden Source Reference` appendix that follows maps facts back to "
                "their original `<golden_source>`/`<research_source>` provenance tags — use it to identify the "
                "correct citation URL when flagging a missing citation, but do not use it as a source of "
                "additional facts beyond what the deduplicated body already covers."
            )
            return f"{banner}\n\n{self.content}"

        sources = self._exploration_sources
        if not sources:
            banner = (
                "Research format: **Format B** (raw XML-tagged). "
                'No `<research_source phase="exploration">` blocks were found in the research. '
                "Skip all exploration integration checks — no exploration sources were available to the writer.\n\n"
                "The full research content below includes `<golden_source>` and "
                '`<research_source phase="exploitation">` tags — use them for the golden/exploitation citation '
                "completeness check."
            )
            return f"{banner}\n\n{self.content}"

        banner = (
            "Research format: **Format B** (raw XML-tagged). "
            "The full research content below includes `<golden_source>` and "
            '`<research_source phase="exploitation">` tags — use them for the golden/exploitation citation '
            "completeness check.\n\n"
            "It also contains the exploration-phase sources that were available to the writer during the "
            "integration pass, repeated separately below for convenience. Use them for two sequential checks:\n\n"
            "1. **Coverage check (missing integration):** For each source, assess whether it contains "
            "content that meets the depth/breadth integration bar — e.g. theoretical foundations, technical "
            "nuances, alternative perspectives, limitations, real-world case studies, adjacent concepts, "
            "historical context, or emerging trends. If a source qualifies and its content does not appear "
            "anywhere in the article, flag a review citing the specific section(s) where integration would "
            "have been appropriate and briefly describe what the source would have added.\n\n"
            "2. **Quality check (present integration):** For any exploration content that does appear in "
            "the article, verify it satisfies all integration rules: follows the core point it enriches "
            "(never leads), does not dominate any section's narrative, does not introduce concepts the "
            "article then structurally depends on elsewhere, and has not shifted the section's focus away "
            "from what the article guideline specifies for that section.\n\n"
            "<exploration_sources>\n"
            f"{sources}\n"
            "</exploration_sources>"
        )
        return f"{banner}\n\n{self.content}"

    def to_context(self) -> str:
        return f"""
<{self.xml_tag}>
    {self.content}
</{self.xml_tag}>
"""

    def __str__(self) -> str:
        return f"Research(len_content={len(self.content)}, len_image_urls={len(self.image_urls)})"
