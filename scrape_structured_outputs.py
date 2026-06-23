#!/usr/bin/env python3
"""
Manual scraper for https://developers.openai.com/api/docs/guides/structured-outputs

This script fetches the page and converts the main content to Markdown
while trying to preserve text and code blocks as faithfully as possible.

Usage:
    python scrape_structured_outputs.py

Requirements:
    pip install requests beautifulsoup4 markdownify lxml
"""

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import markdownify as md
import re
from pathlib import Path


def clean_markdown(text: str) -> str:
    """Light cleanup: collapse excessive blank lines, fix some common artifacts."""
    # Collapse 3+ newlines into 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove trailing whitespace on lines
    text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)
    return text.strip()


def get_main_content(soup: BeautifulSoup) -> Tag | None:
    """
    Try to locate the main documentation content container.
    You may need to adjust the selectors below after inspecting the page
    with your browser's DevTools (Elements tab).
    """
    # Common patterns for documentation sites
    candidates = [
        soup.find("main"),
        soup.find("article"),
        soup.find("div", {"class": re.compile(r"content|docs-content|main-content|prose", re.I)}),
        soup.find("div", {"id": re.compile(r"content|main|article", re.I)}),
    ]

    for candidate in candidates:
        if candidate:
            # Remove obvious navigation / sidebar / footer elements
            for unwanted in candidate.find_all(
                ["nav", "header", "footer", "aside"],
                class_=re.compile(r"nav|sidebar|menu|toc|breadcrumb|footer", re.I)
            ):
                unwanted.decompose()

            # Also remove elements that are clearly not content
            for tag in candidate.find_all(class_=re.compile(r"sidebar|nav|toc|menu|header|footer", re.I)):
                tag.decompose()

            return candidate

    # Fallback: return the whole body if nothing better is found
    return soup.find("body")


def scrape_page(url: str, output_path: str | Path = "structured-outputs-full.md") -> None:
    print(f"Fetching: {url}")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch page: {e}")
        return

    soup = BeautifulSoup(resp.text, "lxml")

    main = get_main_content(soup)
    if not main:
        print("Could not locate main content. The page structure may have changed.")
        print("Please open the page in a browser, inspect the HTML, and update the selectors in get_main_content().")
        return

    # Convert HTML → Markdown
    # heading_style="ATX" gives nice # ## ### headings
    # code_language=True tries to preserve language hints on code blocks
    markdown = md(
        str(main),
        heading_style="ATX",
        bullets="-",
        code_language=True,
        strip=["script", "style", "noscript"],
    )

    markdown = clean_markdown(markdown)

    # Write output
    output_path = Path(output_path)
    output_path.write_text(markdown, encoding="utf-8")

    print(f"Successfully saved full Markdown to: {output_path.resolve()}")
    print(f"File size: {output_path.stat().st_size:,} bytes")


if __name__ == "__main__":
    URL = "https://developers.openai.com/api/docs/guides/structured-outputs"
    OUTPUT = "structured-outputs-full.md"

    scrape_page(URL, OUTPUT)
