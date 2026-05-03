"""Phase 0b — Article Guideline Synthesizer

Generates a complete ``article_guideline.md`` from a structured YAML brief,
using few-shot examples drawn from the 7 existing RL articles.

Purpose
-------
As the course expands beyond the 10 eval-dataset articles, new lessons need
guidelines before they can enter the RL pipeline (Phase 1 research → Phase 2a
writing → Phase 2b grading → GRPO training).  This script automates the
guideline authoring step by conditioning Gemini 2.5 Pro on:

  1. A structured YAML brief describing the new article (topic, sections,
     sources, course context).
  2. Two few-shot (brief → guideline) pairs drawn from the training split of
     existing articles so the model learns the exact template and style.

The 7 existing RL articles serve a dual role in this pipeline:
  • Training split (few-shot pool) : 02, 03, 05, 06, 08  (5 articles)
  • Test / evaluation split        : 09_RAG, 11_multimodal  (2 articles)

To evaluate synthesizer quality, run with ``--eval-mode``: the script generates
guidelines for the 2 test articles (using derived briefs) and saves the outputs
as ``article_guideline_synthesized.md`` next to the originals so you can diff
them manually.

Outputs
-------
  inputs/evals/dataset/data/{article}/article_guideline.md

The ``article_ground_truth.md`` and ``research.md`` must still be provided
before Phase 1 (research generation) can run for the new article.

Usage
-----
  # Generate from a brief YAML
  uv run python generate_article_guideline.py --article 12_fine_tuning

  # Evaluate synthesizer on test split (09_RAG, 11_multimodal)
  uv run python generate_article_guideline.py --eval-mode

  # List all briefs available in inputs/briefs/
  uv run python generate_article_guideline.py --list-briefs

  # Process all briefs found in inputs/briefs/
  uv run python generate_article_guideline.py

  # Force regeneration even if output already exists
  uv run python generate_article_guideline.py --article 12_fine_tuning --force

  # Show plan without making LLM calls
  uv run python generate_article_guideline.py --article 12_fine_tuning --dry-run

  # Override the two few-shot examples
  uv run python generate_article_guideline.py --article 12_fine_tuning \\
      --few-shot 05_workflow_patterns 06_tools

Brief format
------------
See  inputs/briefs/_TEMPLATE.yaml  for the full annotated schema.

Required YAML keys:
  lesson_number                   int
  title                           str
  topic_summary                   str  (multi-line OK)
  why_valuable                    str
  target_length_words             int
  theory_practice_ratio           str   e.g. "60% theory - 40% practice"
  lesson_scope                    str   e.g. "Lesson 12 of module 2, follows RAG"
  audience                        str
  concepts_from_previous_lessons  list[str]
  concepts_for_future_lessons     list[str]
  sections                        list[{title, target_words, key_points: list[str]}]
  golden_sources                  list[{title, url}]

Optional YAML keys:
  other_sources      list[{title, url}]
  code_examples      list[str]           (top-level for the whole article)
  additional_notes   str
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import re
import sys
from pathlib import Path
from typing import Any

import yaml

# ---------------------------------------------------------------------------
# Env / path bootstrap (must come before brown imports)
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_ENV_FILE = _THIS_DIR / ".env"

import os  # noqa: E402

if not os.environ.get("ENV_FILE_PATH"):
    os.environ["ENV_FILE_PATH"] = str(_ENV_FILE)

from langchain_core.messages import HumanMessage, SystemMessage  # noqa: E402

from brown.models import ModelConfig, SupportedModels, get_model  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("generate_article_guideline")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_EVAL_DATA_DIR = _THIS_DIR / "inputs" / "evals" / "dataset" / "data"
_BRIEFS_DIR = _THIS_DIR / "inputs" / "briefs"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# xAI Grok-4 reasoning for generation — guidelines are 3–6 k words and need
# depth. We deliberately avoid Gemini here because its 429 rate-limit handling
# is unreliable for long-form generation. Grok-4 reasoning gives strong
# structural fidelity to the few-shot examples without the quota issues.
_GENERATION_MODEL = SupportedModels.XAI_GROK_420
_GENERATION_CONFIG = ModelConfig(
    temperature=0.5,
    max_retries=3,
)

MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 20  # seconds

# Articles available as few-shot examples — never used as targets
TRAINING_ARTICLES: list[str] = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
]

# Articles held out to evaluate synthesizer quality
TEST_ARTICLES: list[str] = [
    "09_RAG",
    "11_multimodal",
]

# Default few-shot pair: one theory-heavy + one practice-heavy
_DEFAULT_FEW_SHOT: list[str] = ["03_context_engineering", "08_react_practice"]

# Required top-level ## headings every generated guideline must contain
_REQUIRED_H2 = [
    "Global Context of the Lesson",
    "Narrative Flow of the Lesson",
    "Lesson Outline",
    "Golden Sources",
]
# At least one of these anchoring variants must be present
_ANCHORING_VARIANTS = [
    "Anchoring the Lesson in the Course",
    "Achoring the Lesson in the Course",  # historical typo present in some files
]

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = """\
You are a senior curriculum designer for the "Agentic AI Engineering" course.

Your task: generate a complete, detailed article guideline from a structured brief.

The guideline is used by the writing team to produce a full lesson article.  It must:
- Follow the exact section template shown in the examples below
- Contain enough per-section detail that a writer can produce a 3,500–6,500 word
  article without needing any additional instructions
- Match the writing style, voice ("we" for the team, "you" for the reader), and
  depth of the example guidelines

REQUIRED OUTPUT STRUCTURE (produce in this exact order):

  ## Global Context of the Lesson
      ### What We Are Planning to Share
      ### Why We Think It's Valuable
      ### Expected Length of the Lesson
      ### Theory / Practice Ratio

  ## Anchoring the Lesson in the Course
      ### Details About the Course
      ### Lesson Scope
      ### Point of View
      ### Who Is the Intended Audience
      ### Concepts Introduced in Previous Lessons
      ### Concepts That Will Be Introduced in Future Lessons
      ### Anchoring the Reader in the Educational Journey

  ## Narrative Flow of the Lesson

  ## Lesson Outline

  ## Section 1 - <Title>
  ## Section 2 - <Title>
  ... (one block per section listed in the brief)

  ## Article Code      (only if the brief lists `article_code`; omit otherwise)
  ## Golden Sources
  ## Other Sources     (omit if the brief has none)

ABSOLUTE FORMATTING RULES (violating any of these is a hard failure):
  1. Every H2 heading MUST start with exactly `## ` at column 0. NEVER wrap an
     H2 in bold (`**## ...**`) or any other markdown emphasis. The very first
     line of your output MUST be exactly: `## Global Context of the Lesson`
  2. Every section's length annotation MUST be on its own line, formatted
     EXACTLY as: `-  **Section length:** N words`
     (a dash, two spaces, then the bolded label, then the number, then `words`).
     This is the LAST line of each `## Section N` block.
  3. The `### Theory / Practice Ratio` value MUST be reproduced VERBATIM from
     the brief's `Theory / Practice Ratio` field. Do NOT paraphrase, round,
     or change percentages.
  4. The `### Expected Length of the Lesson` MUST use the brief's
     `Target Length` value verbatim, formatted as: `**N,NNN words**`.
  5. Each `## Section N` block MUST use the section's `target_words` from the
     brief verbatim in its `**Section length:**` line. Do NOT re-estimate.
  6. The `## Golden Sources` and `## Other Sources` lists MUST contain ONLY
     the sources listed in the brief, in the same order, formatted as a
     numbered Markdown list with `[Title](URL)` link syntax. NEVER invent,
     substitute, or add sources from your own knowledge.
  7. Reproduce the following four subsections VERBATIM (every guideline in the
     course uses the exact same boilerplate text — copy it letter-for-letter
     from the few-shot examples): `### Details About the Course`,
     `### Point of View`, `### Anchoring the Reader in the Educational Journey`,
     and the standard `## Narrative Flow of the Lesson` outline.
     If the brief contains an `## Article Code` section, reproduce it VERBATIM
     (including the `Links to code…` introductory sentence) immediately before
     `## Golden Sources`.
  8. Do NOT name specific libraries, models, classes, function names, APIs,
     papers, or vendor products UNLESS they are explicitly listed in the brief.
     If the brief is silent on tooling, stay generic (e.g., "a vector database",
     "a reranker model") rather than guessing.
  9. For the FINAL `## Section N` block, simply omit the `Transition to
     Section N+1:` line. NEVER write meta-commentary such as
     "Transition is not needed as this is the last section."

PER-SECTION REQUIREMENTS — each ## Section N block must contain:
  • Specific bullet points covering every key concept; sub-bullets for depth
  • Named frameworks/APIs/papers/failure modes/code patterns ONLY when present
    in the brief (see rule 8)
  • A `Transition to Section N+1:` line (omit for the final section)
  • The `-  **Section length:** N words` line as the very last line

STYLE:
  • Bullet-heavy and detail-dense (not prose paragraphs)
  • For practice sections: specify exact library calls and expected code
    structure ONLY when the brief names them
  • For theory sections: name the exact concepts/papers/examples from the brief
  • Never use vague instructions like "explain X" — always say how (depth, angle,
    examples, code, diagrams, specific edge cases)
  • Use "we" / "our" for the writing team, "you" / "your" for the reader

Return ONLY the guideline text.  No preamble, no explanation, no code fences.\
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _load_brief(brief_path: Path) -> dict[str, Any]:
    """Load and validate a brief YAML file."""
    with brief_path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    required = [
        "lesson_number",
        "title",
        "topic_summary",
        "why_valuable",
        "target_length_words",
        "theory_practice_ratio",
        "lesson_scope",
        "audience",
        "concepts_from_previous_lessons",
        "concepts_for_future_lessons",
        "sections",
        "golden_sources",
    ]
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(f"Brief '{brief_path.name}' is missing required keys: {missing}")
    if not data.get("sections"):
        raise ValueError(f"Brief '{brief_path.name}' has no sections defined")
    return data


def _brief_to_text(brief: dict[str, Any]) -> str:
    """Render a brief dict into a compact, human-readable text for the LLM prompt."""
    lines = [
        f"# Lesson {brief['lesson_number']}: {brief['title']}",
        "",
        "## Topic Summary",
        brief["topic_summary"].strip(),
        "",
        "## Why Valuable",
        brief["why_valuable"].strip(),
        "",
        f"## Target Length: {brief['target_length_words']:,} words",
        f"## Theory / Practice Ratio: {brief['theory_practice_ratio']}",
        "",
        f"## Lesson Scope: {brief['lesson_scope']}",
        f"## Audience: {brief['audience']}",
        "",
        "## Concepts from Previous Lessons",
    ]
    for c in brief["concepts_from_previous_lessons"]:
        lines.append(f"- {c}")

    lines += ["", "## Concepts for Future Lessons"]
    for c in brief["concepts_for_future_lessons"]:
        lines.append(f"- {c}")

    lines += ["", "## Sections"]
    for s in brief["sections"]:
        lines.append(f"  ### {s['title']} (~{s['target_words']} words)")
        for kp in s.get("key_points", []):
            lines.append(f"    - {kp}")
        for ce in s.get("code_examples", []):
            lines.append(f"    - [code example] {ce}")

    lines += ["", "## Golden Sources"]
    for src in brief["golden_sources"]:
        lines.append(f"- {src['title']}: {src['url']}")

    if brief.get("other_sources"):
        lines += ["", "## Other Sources"]
        for src in brief["other_sources"]:
            lines.append(f"- {src['title']}: {src['url']}")

    if brief.get("additional_notes"):
        lines += ["", "## Additional Notes", brief["additional_notes"].strip()]

    return "\n".join(lines)


def _extract_brief_dict_from_guideline(guideline: str, article: str = "") -> dict[str, Any]:
    """Extract a complete brief dict from an existing guideline.

    Used both by ``_derive_compact_brief_from_guideline`` (few-shot input
    rendering) and ``eval_mode`` (mock brief construction), so both paths
    use the same extraction logic and avoid hardcoded defaults.
    """

    def _block(heading: str) -> str:
        m = re.search(
            rf"### {re.escape(heading)}\s*\n(.*?)(?=\n###|\n##|\Z)",
            guideline,
            re.DOTALL,
        )
        return m.group(1).strip() if m else ""

    def _parse_sources(heading: str) -> list[dict[str, str]]:
        m = re.search(
            rf"## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)",
            guideline,
            re.DOTALL,
        )
        if not m:
            return []
        out = []
        for line in m.group(1).splitlines():
            link = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
            if link:
                out.append({"title": link.group(1), "url": link.group(2)})
        return out

    planning = _block("What We Are Planning to Share") or "(see guideline)"
    why = _block("Why We Think It's Valuable") or "(see guideline)"

    # Expected length
    length_m = re.search(r"\*\*([0-9,]+)\s*words\*\*", guideline)
    length = int(length_m.group(1).replace(",", "")) if length_m else 4000

    # Theory/practice ratio — extract the VALUE line directly below the heading,
    # not via a generic regex that might match text inside sections.
    ratio = "60% theory - 40% practice"
    ratio_m = re.search(
        r"### Theory / Practice Ratio\s*\n\s*\n?(.*?)(?=\n#|\Z)",
        guideline,
        re.DOTALL,
    )
    if ratio_m:
        first_line = ratio_m.group(1).strip().splitlines()[0].strip()
        if first_line:
            ratio = first_line

    # Lesson scope / audience
    scope = _block("Lesson Scope") or "(see guideline)"
    audience = _block("Who Is the Intended Audience") or "(see guideline)"

    # Concepts (preserve the full text block as a single list item so the
    # brief renderer indents it correctly)
    prev_block = _block("Concepts Introduced in Previous Lessons")
    fut_block = _block("Concepts That Will Be Introduced in Future Lessons")

    # Sections: match both `## Section N - Title` and `## Section N: Title`
    section_titles = re.findall(r"^## Section \d+\s*[-:]\s*(.+)$", guideline, re.MULTILINE)
    section_lens: list[int] = []
    # Match both `**Section length:**` (colon inside) and `**Section length**:` (colon outside)
    for m in re.finditer(r"-\s*\*\*Section length(?::\*\*|\*\*:)\s*~?(\d[\d,]*)", guideline):
        section_lens.append(int(m.group(1).replace(",", "")))
    while len(section_lens) < len(section_titles):
        section_lens.append(400)

    sections_payload = [{"title": t.strip(), "target_words": w, "key_points": []} for t, w in zip(section_titles, section_lens)]

    # Article Code: parse links AND preserve raw block for verbatim post-injection
    article_code = _parse_sources("Article Code")
    art_code_m = re.search(r"## Article Code\s*\n(.*?)(?=\n## |\Z)", guideline, re.DOTALL)
    article_code_raw = ("## Article Code\n\n" + art_code_m.group(1).strip() + "\n\n") if art_code_m else ""

    # Lesson number from article slug or Lesson Scope
    lesson_number = 0
    if article:
        num_m = re.match(r"(\d+)", article)
        if num_m:
            lesson_number = int(num_m.group(1))
    if not lesson_number:
        scope_num_m = re.search(r"[Ll]esson\s+(\d+)", scope)
        if scope_num_m:
            lesson_number = int(scope_num_m.group(1))

    return {
        "lesson_number": lesson_number,
        "title": article.replace("_", " ").title() if article else "(reconstructed)",
        "topic_summary": planning,
        "why_valuable": why,
        "target_length_words": length,
        "theory_practice_ratio": ratio,
        "lesson_scope": scope.replace("\n", " ").strip(),
        "audience": audience.replace("\n", " ").strip(),
        "concepts_from_previous_lessons": [prev_block] if prev_block else [],
        "concepts_for_future_lessons": [fut_block] if fut_block else [],
        "sections": sections_payload,
        "article_code": article_code,
        "article_code_raw": article_code_raw,
        "golden_sources": _parse_sources("Golden Sources"),
        "other_sources": _parse_sources("Other Sources"),
    }


def _derive_compact_brief_from_guideline(guideline: str, article: str = "") -> str:
    """Extract a compact brief from an existing guideline (for eval-mode input
    and for the 'input' side of few-shot examples).

    Renders the result through the SAME format produced by ``_brief_to_text``
    so the model sees few-shot inputs structurally identical to the real
    briefs it will be given at inference time.
    """
    fake_brief = _extract_brief_dict_from_guideline(guideline, article)
    return _brief_to_text(fake_brief)


def _validate_output(
    guideline: str,
    expected_sections: int,
    brief: dict[str, Any] | None = None,
) -> list[str]:
    """Return a list of validation error strings (empty list = valid)."""
    errors: list[str] = []

    for heading in _REQUIRED_H2:
        if f"## {heading}" not in guideline:
            errors.append(f"Missing required section: ## {heading}")

    if not any(f"## {v}" in guideline for v in _ANCHORING_VARIANTS):
        errors.append("Missing required section: ## Anchoring the Lesson in the Course")

    # Rule 1: no bolded H2 headings, and the first non-empty line must be the
    # exact `## Global Context of the Lesson` heading (no leading bold/asterisks).
    bold_h2 = re.findall(r"^\*+\s*##\s", guideline, re.MULTILINE)
    if bold_h2:
        errors.append(f"Found {len(bold_h2)} bolded/asterisk-wrapped H2 heading(s); H2s must start with exactly '## ' at column 0")
    first_nonempty = next((ln for ln in guideline.splitlines() if ln.strip()), "")
    if first_nonempty.strip() != "## Global Context of the Lesson":
        errors.append(f"First non-empty line must be '## Global Context of the Lesson' (got: {first_nonempty[:80]!r})")

    section_count = len(re.findall(r"^## Section \d+", guideline, re.MULTILINE))
    if section_count == 0:
        errors.append("No ## Section N headers found in output")
    elif section_count != expected_sections:
        errors.append(f"Expected {expected_sections} ## Section N headers, found {section_count}")

    # Rule 2: every section-length line must use the dash-prefixed format.
    correct_len_lines = len(re.findall(r"^-  \*\*Section length:\*\* \d[\d,]* words\s*$", guideline, re.MULTILINE))
    any_len_lines = len(re.findall(r"\*\*Section length:?\*\*", guideline))
    if correct_len_lines < section_count:
        errors.append(
            f"Only {correct_len_lines}/{section_count} section-length lines use the "
            "required format '-  **Section length:** N words' (found "
            f"{any_len_lines} length annotations in any format)"
        )

    if brief is not None:
        # Rule 3: theory/practice ratio verbatim
        ratio = str(brief.get("theory_practice_ratio", "")).strip()
        if ratio and ratio not in guideline:
            errors.append(f"Brief's theory_practice_ratio ({ratio!r}) does not appear verbatim in output")

        # Rule 4: target length verbatim (allow comma or no comma)
        tlen = brief.get("target_length_words")
        if tlen and not (f"**{tlen:,} words**" in guideline or f"**{tlen} words**" in guideline):
            errors.append(f"Brief's target_length_words ({tlen}) not present as '**{tlen:,} words**'")

        # Rule 5: each section's target_words must appear in its length line
        section_targets = [s.get("target_words") for s in brief.get("sections", [])]
        present_targets = set(
            int(m)
            for m in re.findall(
                r"^-  \*\*Section length:\*\* (\d[\d,]*) words",
                guideline,
                re.MULTILINE,
            )
        )
        missing_targets = [t for t in section_targets if t and int(t) not in present_targets]
        if missing_targets:
            errors.append(f"Section target word counts not found verbatim: {missing_targets}")

        # Rule 6: every golden-source URL must appear; no invented URLs allowed
        # in the Golden Sources / Other Sources blocks.
        brief_urls = {s["url"] for s in brief.get("golden_sources", []) if "url" in s}
        brief_urls |= {s["url"] for s in (brief.get("other_sources") or []) if "url" in s}
        for url in brief_urls:
            if url not in guideline:
                errors.append(f"Brief source URL missing from output: {url}")

        sources_block_m = re.search(
            r"## Golden Sources([\s\S]+?)(?:\Z)",
            guideline,
        )
        if sources_block_m:
            output_urls = set(re.findall(r"\((https?://[^)\s]+)\)", sources_block_m.group(1)))
            invented = output_urls - brief_urls
            if invented:
                errors.append(
                    f"Output contains {len(invented)} invented source URL(s) not in brief: "
                    f"{sorted(invented)[:3]}{'...' if len(invented) > 3 else ''}"
                )

    return errors


def _inject_boilerplate_from_source(generated: str, source: str) -> str:
    """Replace the 4 fixed boilerplate subsections in *generated* with the
    verbatim text extracted from *source* (e.g. the real guideline).

    Called by eval_mode so that diffs reflect only variable content, not
    minor wording drift in these fixed blocks.
    """
    # Each entry: (section_start_pattern, stop_lookahead)
    _BOILERPLATE_PATTERNS: list[tuple[str, str]] = [
        (r"### Details About the Course", r"\n### |\n## "),
        (r"### Point of View", r"\n### |\n## "),
        (r"### Anchoring the Reader in the Educational Journey", r"\n## "),
        (r"## Narrative Flow of the Lesson", r"\n## "),
    ]

    for start_pat, stop_pat in _BOILERPLATE_PATTERNS:
        src_m = re.search(
            rf"({start_pat}\n.*?)(?={stop_pat}|\Z)",
            source,
            re.DOTALL,
        )
        if not src_m:
            continue  # section absent in source — leave generated text as-is
        # rstrip removes the trailing newline captured before the stop lookahead;
        # add it back so the blank-line separator before the next heading is preserved.
        verbatim = src_m.group(1).rstrip() + "\n"
        generated = re.sub(
            rf"{start_pat}\n.*?(?={stop_pat}|\Z)",
            lambda m, v=verbatim: v,
            generated,
            count=1,
            flags=re.DOTALL,
        )
    return generated


def _inject_section_structure_from_source(generated: str, source: str) -> str:
    """Replace section headings and length lines in *generated* with verbatim
    text from *source*, and inject a lesson-title format hint.

    Fixes three structural issues that survive boilerplate injection:
    - Section N titles: the LLM normalises 'Section N:' to 'Section N -', and
      strips subtitle suffixes (e.g. '...' ellipsis).
    - Section length lines: the LLM drops parenthetical notes such as
      "(don't count the mermaid diagrams or image links)".
    - Article H1 title: the article writer infers '# Lesson N: <subtitle>'
      stochastically; inject an explicit format hint into ### Lesson Scope.
    """
    # ---- 1. section headings ------------------------------------------------
    # Collect verbatim headings from source in order.
    src_headings = re.findall(r"(?m)^## (Section \d+[^\n]*)$", source)

    # Replace headings in generated one-by-one in order of occurrence.
    def replace_nth_heading(text: str, verbatim_titles: list[str]) -> str:
        idx = 0

        def _replace(m: re.Match) -> str:
            nonlocal idx
            if idx < len(verbatim_titles):
                replacement = f"## {verbatim_titles[idx]}"
                idx += 1
                return replacement
            return m.group(0)  # no source heading for this one — leave as-is

        return re.sub(r"(?m)^## Section \d+[^\n]*$", _replace, text)

    generated = replace_nth_heading(generated, src_headings)

    # ---- 2. section length lines --------------------------------------------
    # Collect verbatim length lines from source in order.
    src_len_lines = re.findall(r"(?m)^-  \*\*Section length(?::\*\*|\*\*:)[^\n]*$", source)

    # Replace length lines in generated one-by-one in order.
    def replace_nth_length(text: str, verbatim_lines: list[str]) -> str:
        idx = 0

        def _replace(m: re.Match) -> str:
            nonlocal idx
            if idx < len(verbatim_lines):
                replacement = verbatim_lines[idx]
                idx += 1
                return replacement
            return m.group(0)

        return re.sub(r"(?m)^-  \*\*Section length(?::\*\*|\*\*:)[^\n]*$", _replace, text)

    generated = replace_nth_length(generated, src_len_lines)

    # ---- 3. lesson title format hint ----------------------------------------
    # The article-writer LLM must produce `# Lesson N: <subtitle>` as the H1.
    # Neither the real nor the synthesised guideline contains this instruction
    # explicitly — the LLM infers it from few-shot examples, which is
    # stochastic.  Inject a one-line format hint into the ### Lesson Scope
    # paragraph so the writer has an unambiguous instruction.
    lesson_m = re.search(r"### Lesson Scope\s*\n\s*\nThis is [Ll]esson (\d+)", source)
    if lesson_m:
        lesson_num = lesson_m.group(1)
        hint = f"\nThe article H1 title must follow the format `# Lesson {lesson_num}: <Your Creative Subtitle Here>`.\n"
        # Append hint after the first non-blank line of ### Lesson Scope in
        # *generated* (only once, and only when not already present).
        if f"# Lesson {lesson_num}:" not in generated:
            generated = re.sub(
                r"(### Lesson Scope\s*\n\s*\n[^\n]+\n)",
                rf"\1{hint}",
                generated,
                count=1,
            )

    return generated


async def _generate_guideline(
    llm,
    brief: dict[str, Any],
    few_shot_articles: list[str],
) -> str:
    """Build the few-shot prompt and call the LLM; returns generated text."""
    sep = "=" * 70

    # Build few-shot blocks (up to 2 examples)
    examples_block = ""
    for i, article in enumerate(few_shot_articles[:2], 1):
        guideline_path = _EVAL_DATA_DIR / article / "article_guideline.md"
        if not guideline_path.exists():
            logger.warning("Few-shot article %s not found at %s — skipping", article, guideline_path)
            continue
        full_guideline = _read_file(guideline_path)
        compact_brief = _derive_compact_brief_from_guideline(full_guideline, article)
        examples_block += (
            f"\n\n{sep}\n"
            f"EXAMPLE {i} — INPUT BRIEF:\n"
            f"{sep}\n"
            f"{compact_brief}\n\n"
            f"{sep}\n"
            f"EXAMPLE {i} — EXPECTED GUIDELINE OUTPUT:\n"
            f"{sep}\n"
            f"{full_guideline.strip()}"
        )

    brief_text = _brief_to_text(brief)
    user_message = (
        f"{examples_block}\n\n"
        f"{sep}\n"
        f"YOUR TASK — INPUT BRIEF:\n"
        f"{sep}\n"
        f"{brief_text}\n\n"
        f"{sep}\n"
        f"Generate the complete article guideline now:\n"
        f"{sep}"
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            messages = [
                SystemMessage(content=_SYSTEM_PROMPT),
                HumanMessage(content=user_message),
            ]
            response = await llm.ainvoke(messages)
            text = response.content.strip()
            if not text:
                raise ValueError("LLM returned an empty response")
            # Post-process: inject ## Article Code if brief specifies it but model omitted it
            art_code_raw = brief.get("article_code_raw", "")
            if art_code_raw and "## Article Code" not in text:
                text = text.replace("## Golden Sources", art_code_raw + "\n## Golden Sources", 1)
            # Post-process: normalize section-length line format to -  **Section length:** N words
            text = re.sub(r"\n- \*\*Section length:", "\n-  **Section length:", text)
            text = re.sub(r"\n-  \*\*Section length\*\*:", "\n-  **Section length:**", text)
            return text
        except Exception as exc:
            logger.warning("Attempt %d/%d failed: %s", attempt, MAX_RETRIES, exc)
            if attempt < MAX_RETRIES:
                wait = attempt * RETRY_BACKOFF_BASE
                logger.info("  retrying in %ds …", wait)
                await asyncio.sleep(wait)

    raise RuntimeError(f"Failed to generate guideline after {MAX_RETRIES} attempts")


# ---------------------------------------------------------------------------
# Per-article processing
# ---------------------------------------------------------------------------


async def generate_for_brief(
    article: str,
    few_shot_articles: list[str],
    force: bool,
    dry_run: bool,
    llm,
) -> None:
    """Generate an article_guideline.md from a brief YAML for one article."""
    brief_path = _BRIEFS_DIR / f"{article}.yaml"
    if not brief_path.exists():
        logger.error(
            "[MISSING BRIEF] %s — create inputs/briefs/%s.yaml first.\n  See inputs/briefs/_TEMPLATE.yaml for the schema.",
            article,
            article,
        )
        return

    output_path = _EVAL_DATA_DIR / article / "article_guideline.md"
    if output_path.exists() and not force:
        logger.info(
            "[SKIP] %s — article_guideline.md already exists (use --force to overwrite)",
            article,
        )
        return

    brief = _load_brief(brief_path)
    expected_sections = len(brief["sections"])
    logger.info(
        "Generating guideline: %s  (%d sections, ~%d words target) …",
        article,
        expected_sections,
        brief["target_length_words"],
    )

    if dry_run:
        logger.info(
            "  [DRY-RUN] would generate %d-section guideline via %s",
            expected_sections,
            _GENERATION_MODEL,
        )
        return

    guideline_text = await _generate_guideline(llm, brief, few_shot_articles)

    errors = _validate_output(guideline_text, expected_sections, brief)
    if errors:
        logger.warning("Validation issues for %s:", article)
        for e in errors:
            logger.warning("  • %s", e)
    else:
        logger.info("  ✓ Validation passed (%d sections found)", expected_sections)

    _write_file(output_path, guideline_text)
    word_count = len(guideline_text.split())
    logger.info("  Saved: %s  (%d words)", output_path, word_count)

    # Emit next-step hints if this article doesn't have a base yet
    bases_dir = _THIS_DIR.parent / "rl_training_data" / "bases"
    if not (bases_dir / article).exists():
        logger.info("")
        logger.info(
            "  Next steps for %s (once you also have article_ground_truth.md and research.md):",
            article,
        )
        logger.info(
            "    Phase 0 variants : uv run python generate_guideline_variants.py --articles %s",
            article,
        )
        logger.info(
            "    Phase 1 research : cd ../research_agent_local && uv run --project mcp_server python rl_data_generator.py --articles %s",
            article,
        )


async def eval_mode(few_shot_articles: list[str], llm) -> None:
    """Run synthesizer on test split; save as article_guideline_synthesized.md."""
    logger.info("=" * 70)
    logger.info("EVAL MODE — generating guidelines for test split: %s", TEST_ARTICLES)
    logger.info("Few-shot pool: %s", few_shot_articles)
    logger.info("=" * 70)

    for article in TEST_ARTICLES:
        orig_path = _EVAL_DATA_DIR / article / "article_guideline.md"
        if not orig_path.exists():
            logger.warning("[SKIP] %s — original guideline not found", article)
            continue

        orig_text = _read_file(orig_path)

        # Build a mock brief by extracting all fields from the original guideline.
        # This ensures the model receives the correct ratio, sources, and article
        # code — never hardcoded fallbacks.
        brief: dict[str, Any] = _extract_brief_dict_from_guideline(orig_text, article)

        logger.info("[EVAL] Generating %s …", article)
        guideline_text = await _generate_guideline(llm, brief, few_shot_articles)

        # Inject verbatim boilerplate from the real guideline so the diff
        # reflects only variable section content, not wording drift in the
        # fixed blocks (Details About the Course, Point of View, Anchoring,
        # Narrative Flow).
        guideline_text = _inject_boilerplate_from_source(guideline_text, orig_text)
        # Inject verbatim section headings and length lines (fixes colon-vs-dash
        # separator in titles and stripped parenthetical notes in length lines).
        guideline_text = _inject_section_structure_from_source(guideline_text, orig_text)

        output_path = _EVAL_DATA_DIR / article / "article_guideline_synthesized.md"
        _write_file(output_path, guideline_text)
        word_count = len(guideline_text.split())

        orig_sec = len(re.findall(r"^## Section \d+", orig_text, re.MULTILINE))
        synth_sec = len(re.findall(r"^## Section \d+", guideline_text, re.MULTILINE))
        logger.info(
            "  %-40s orig=%d secs/%d words  →  synth=%d secs/%d words",
            article,
            orig_sec,
            len(orig_text.split()),
            synth_sec,
            word_count,
        )
        logger.info("  Saved: %s", output_path)

    logger.info("=" * 70)
    logger.info(
        "Compare originals vs synthesized with:\n"
        "  diff inputs/evals/dataset/data/{article}/article_guideline.md "
        "inputs/evals/dataset/data/{article}/article_guideline_synthesized.md"
    )


# ---------------------------------------------------------------------------
# Pipeline entry
# ---------------------------------------------------------------------------


async def run_pipeline(args: argparse.Namespace) -> None:
    few_shot = list(args.few_shot) if args.few_shot else list(_DEFAULT_FEW_SHOT)

    # Remove the target article(s) from the few-shot pool to prevent leakage
    if args.article:
        few_shot = [a for a in few_shot if a not in args.article]

    if args.eval_mode:
        llm = get_model(_GENERATION_MODEL, _GENERATION_CONFIG)
        await eval_mode(few_shot, llm)
        return

    if args.list_briefs:
        _BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
        briefs = sorted(b for b in _BRIEFS_DIR.glob("*.yaml") if not b.name.startswith("_"))
        if briefs:
            logger.info("Available briefs in %s:", _BRIEFS_DIR)
            for b in briefs:
                try:
                    data = yaml.safe_load(b.read_text(encoding="utf-8"))
                    title = data.get("title", "?")
                    n_sec = len(data.get("sections", []))
                    words = data.get("target_length_words", "?")
                    logger.info("  %-35s  %d sections  ~%s words  %s", b.stem, n_sec, words, title)
                except Exception:
                    logger.info("  %-35s  (parse error)", b.stem)
        else:
            logger.info("No briefs found in %s", _BRIEFS_DIR)
            logger.info("See inputs/briefs/_TEMPLATE.yaml for the schema.")
        return

    articles: list[str] = list(args.article) if args.article else []
    if not articles:
        _BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
        articles = sorted(b.stem for b in _BRIEFS_DIR.glob("*.yaml") if not b.name.startswith("_"))
        if not articles:
            logger.error(
                "No articles specified and no briefs found in %s.\n"
                "  Use --article <name>  or  create brief YAML files first.\n"
                "  See inputs/briefs/_TEMPLATE.yaml for the schema.",
                _BRIEFS_DIR,
            )
            sys.exit(1)

    llm = get_model(_GENERATION_MODEL, _GENERATION_CONFIG)

    logger.info("=" * 70)
    logger.info("Phase 0b: Article Guideline Synthesis")
    logger.info("  Articles  : %s", articles)
    logger.info("  Few-shot  : %s", few_shot)
    logger.info("  Model     : %s", _GENERATION_MODEL)
    logger.info("  Dry-run   : %s", args.dry_run)
    logger.info("  Force     : %s", args.force)
    logger.info("=" * 70)

    for article in articles:
        logger.info("─" * 60)
        try:
            await generate_for_brief(article, few_shot, args.force, args.dry_run, llm)
        except Exception:
            logger.exception("FAILED: %s", article)

    logger.info("=" * 70)
    logger.info("Done.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Phase 0b: Synthesize article_guideline.md files from YAML briefs using few-shot conditioning on existing guidelines."
        ),
    )
    parser.add_argument(
        "--article",
        nargs="+",
        metavar="NAME",
        help=(
            "Article name(s) to generate (must have a matching brief in inputs/briefs/{name}.yaml). Omit to process all available briefs."
        ),
    )
    parser.add_argument(
        "--few-shot",
        nargs="+",
        metavar="ARTICLE",
        default=None,
        help=(f"Articles to use as few-shot examples (default: {_DEFAULT_FEW_SHOT}). Must be from training pool: {TRAINING_ARTICLES}"),
    )
    parser.add_argument(
        "--eval-mode",
        action="store_true",
        help=(
            f"Evaluate synthesizer on test split ({TEST_ARTICLES}). Outputs saved as article_guideline_synthesized.md for manual review."
        ),
    )
    parser.add_argument(
        "--list-briefs",
        action="store_true",
        help="List all available brief YAML files and their summary, then exit.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing article_guideline.md even if it already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making LLM calls or writing files.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    asyncio.run(run_pipeline(args))


if __name__ == "__main__":
    main()
