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
        """Return a compact research context for the article reviewer.

        Tells the reviewer the detected format and — for Format B — provides the
        exploration-phase source blocks so it can cross-reference article content
        against the actual source material when checking exploration integration rules.
        """
        if self.is_format_a:
            return (
                "Research format: **Format A** (deduplicated). "
                "Exploration-phase content was pre-filtered upstream before the writer received the research. "
                "Skip all exploration integration checks — they do not apply to Format A articles."
            )
        sources = self._exploration_sources
        if not sources:
            return (
                "Research format: **Format B** (raw XML-tagged). "
                'No `<research_source phase="exploration">` blocks were found in the research. '
                "Skip all exploration integration checks — no exploration sources were available to the writer."
            )
        return (
            "Research format: **Format B** (raw XML-tagged). "
            "The following exploration-phase sources were available to the writer during the integration pass. "
            "Use them for two sequential checks:\n\n"
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

    def to_context(self) -> str:
        return f"""
<{self.xml_tag}>
    {self.content}
</{self.xml_tag}>
"""

    def __str__(self) -> str:
        return f"Research(len_content={len(self.content)}, len_image_urls={len(self.image_urls)})"
