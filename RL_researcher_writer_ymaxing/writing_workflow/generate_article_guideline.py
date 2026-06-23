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

  # Extract a planning brief from a finished article (saves to inputs/briefs/)
  uv run python generate_article_guideline.py --from-article 03_context_engineering
  uv run python generate_article_guideline.py --from-article 03_context_engineering 06_tools

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
# External (non-course) article mode
# ---------------------------------------------------------------------------
# Required headings for standalone articles — no Anchoring or Narrative Flow.
_REQUIRED_H2_EXTERNAL = [
    "Context of the Article",
    "Article Outline",
    "Golden Sources",
]

_EXTERNAL_SYSTEM_PROMPT = """\
You are an expert science and technical writer.

Your task: generate a complete, detailed article guideline from a structured brief.

The guideline is used by a writing team to produce a full, standalone article
(not part of a course). It must contain enough per-section bullet-point detail
that a writer can produce the complete article without any additional instructions.

REQUIRED OUTPUT STRUCTURE (produce in this exact order):

  ## Context of the Article
      ### What We Are Planning to Share
      ### Why We Think It's Valuable
      ### Expected Length of the Article
      ### Theory / Practice Ratio

  ## Article Outline
  (numbered list: 1. Section 1 Title, 2. Section 2 Title, …)

  ## Section 1 - <Title>
  ## Section 2 - <Title>
  … (one block per section listed in the brief)

  ## Golden Sources
  ## Other Sources     (omit if the brief has none)

ABSOLUTE FORMATTING RULES (violating any of these is a hard failure):
  1. Every H2 heading MUST start with exactly `## ` at column 0. NEVER wrap an
     H2 in bold. The very first line of your output MUST be exactly:
     `## Context of the Article`
  2. Every section's length annotation MUST be on its own line, formatted
     EXACTLY as: `-  **Section length:** N words`
     This is the LAST line of each `## Section N` block.
  3. The `### Theory / Practice Ratio` value MUST be reproduced VERBATIM from
     the brief.
  4. The `### Expected Length of the Article` MUST use the brief's
     `Target Length` value verbatim, formatted as: `**N,NNN words**`.
  5. Each `## Section N` block MUST use the section's `target_words` from the
     brief verbatim in its `**Section length:**` line. Do NOT re-estimate.
  6. The `## Golden Sources` and `## Other Sources` lists MUST contain ONLY
     the sources listed in the brief, formatted as a Markdown list with
     `[Title](URL)` link syntax. NEVER invent, substitute, or add sources.
  7. Do NOT name specific papers, researchers, organisms, or tools UNLESS they
     are explicitly listed in the brief. Stay generic otherwise.
  8. For the FINAL `## Section N` block, simply omit the `Transition to
     Section N+1:` line.
  9. The brief's key_points define the CONTENT BUDGET for each section.
     Cover every key_point. Do NOT introduce additional top-level concepts
     beyond what the brief names. You may expand each key_point with a concrete
     illustrative example, a failure mode, or a contrast with an adjacent
     concept already named in the brief.
 10. DIAGRAM REQUIREMENTS ARE MANDATORY. For every `- [diagram] …` entry in
     the brief, emit an explicit instruction bullet in that section describing
     exactly what the diagram must show. NEVER drop or omit a diagram entry.

PER-SECTION REQUIREMENTS — each ## Section N block must contain:
  • Detailed bullet points expanding every key_point from the brief
  • For every `- [diagram]` entry: an explicit "Include a Mermaid diagram …" bullet
  • Named researchers/experiments/findings ONLY when present in the brief
  • A `Transition to Section N+1:` line (omit for the final section)
  • The `-  **Section length:** N words` line as the very last line

STYLE:
  • Bullet-heavy and detail-dense (not prose paragraphs)
  • Name the exact findings, methods, and evidence from the brief
  • Never use vague instructions like "explain X" — always specify the angle,
    the depth, and the concrete evidence to use
  • Use "we" / "our" for the writing team, "the reader" for the audience

Return ONLY the guideline text.  No preamble, no explanation, no code fences.\
"""

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
 10. The brief's key_points for each section define the CONTENT BUDGET for that
     section. Every key_point listed must be covered. Do NOT invent additional
     top-level concepts, sub-taxonomies, or technique categories beyond what the
     key_points explicitly name. You may expand each key_point with:
       - a concrete illustrative example
       - a failure mode or edge case
       - a contrast with an adjacent concept already named in the brief
     but you may NOT introduce a new concept that has no anchor in the brief.
     PRESERVE THE BRIEF'S FRAMING: do NOT re-organize a section under a new
     organizing scheme of your own (e.g. regrouping named techniques into
     "pre-retrieval / indexing / post-retrieval" buckets, lifecycle phases, or
     any taxonomy not present in the brief). Cover the key_points in the order
     and under the framing the brief gives them.
     If a section's key_points list is empty, derive content ONLY from:
       - the section title
       - the lesson's topic_summary and why_valuable fields
       - concepts named in the Concepts from Previous / Future Lessons fields
     and keep the expansion MINIMAL and CONSERVATIVE — mirror the section
     title's framing, do NOT impose a new structure, and do NOT fill empty
     key_points by freely inventing technique lists from your general
     knowledge of the topic.
 11. DIAGRAM REQUIREMENTS ARE MANDATORY DELIVERABLES. For every entry in a
     section's `diagrams` list (rendered as `- [diagram] …` in the brief),
     emit an explicit instruction bullet in that section telling the writer to
     produce that diagram. Name it as a Mermaid diagram and describe exactly
     what it must show (nodes, flow, comparison). NEVER drop, merge, or
     silently omit a diagram entry. Do NOT invent diagrams that are not listed
     in the brief.

PER-SECTION REQUIREMENTS — each ## Section N block must contain:
  • One bullet cluster per key_point in the brief; sub-bullets expand that
    specific point with examples, failure modes, or named contrasts (rule 10)
  • For every `- [diagram]` entry in the section's brief, an explicit
    "Include a Mermaid diagram that shows …" bullet (rule 11)
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
# Brief-extraction system prompt (used by --from-article mode)
# ---------------------------------------------------------------------------

_BRIEF_EXTRACTION_SYSTEM_PROMPT = """\
You are a senior curriculum designer for the "Agentic AI Engineering" course.

Your task: read a FINISHED lesson article and reconstruct the planning brief
that a course author would have written BEFORE drafting the article.

The brief is a PLANNING DOCUMENT, not a summary.  Key points must be
conceptual anchors — the ideas a course author would jot down when deciding
what to cover — NOT verbatim sentences or condensed excerpts from the article.

CALIBRATION — right level of detail for key_points:
  ✓ GOOD: "Contrast RAG vs fine-tuning: when each is the right tool (cost, latency, specificity)"
  ✓ GOOD: "Vector embeddings: how semantic similarity search works vs. keyword search"
  ✗ TOO THIN: "RAG components"  (no angle, no contrast, no question to answer)
  ✗ TOO DENSE: "RAG has three components: Retrieval uses FAISS to do ANN search over
     embedded chunks, Augmentation injects top-k results into the context, Generation..."
     (this is article text, not a planning note)

Output ONLY a valid YAML document matching this schema exactly (no markdown
fences, no preamble, no explanation — raw YAML only):

  lesson_number: <int>
  title: "<lesson title WITHOUT 'Lesson N:' prefix>"
  topic_summary: |
    <2-4 sentence description of what the lesson covers, at planning level>
  why_valuable: |
    <1-2 sentences on why this topic matters to AI Engineers>
  target_length_words: <int, approximate word count of article body>
  theory_practice_ratio: "<X% theory - Y% practice>"
  lesson_scope: >
    <one sentence: lesson position + what comes before/after>
  audience: >
    <one sentence: who the reader is and what they already know>
  concepts_from_previous_lessons:
    - <concept 1 — infer from article cross-references such as "as we saw in lesson N">
  concepts_for_future_lessons:
    - <concept 1 — infer from forward-references in the article>
  sections:
    - title: "<section title WITHOUT 'Section N -' prefix>"
      target_words: <int, approximate word count of this section>
      key_points:
        - "<conceptual anchor — name concept + angle/contrast/question; 3–6 per section>"
      diagrams:
        - ("<planning-level description of a Mermaid/conceptual diagram "
           "this section must contain; OMIT this key entirely if the "
           "section has no author-created diagram>")
  golden_sources:
    - title: "<source title>"
      url: "<URL>"
  other_sources:
    - title: "<source title>"
      url: "<URL>"

RULES:
  1. key_points are planning notes, not article excerpts.  Each names a
     concept and an angle (contrast, failure mode, question, diagram idea).
  2. target_words per section: use the EXACT prose word count from the
     SECTION PROSE WORD COUNTS block in the user message — those numbers
     were computed programmatically (all code fences, table rows, and HTML
     comments already stripped).  Copy each number verbatim; do NOT
     re-estimate.
  3. For fields that require course context not present in the article
     (lesson_scope, concepts_from/for_future_lessons), make a reasonable
     inference.
  4. theory_practice_ratio: estimate from proportion of explanatory text
     vs. code / hands-on walkthroughs.  IMPORTANT — inline illustrative
     examples (short customer scenarios, toy queries, single-step
     demonstrations) embedded within an explanatory paragraph count as
     THEORY.  Only dedicated hands-on walkthroughs where the reader is
     expected to run code, execute commands, or follow step-by-step tasks
     count as PRACTICE.  If the article has no such hands-on section, use
     "100% theory - 0% practice".
  5. golden_sources: look FIRST for a dedicated "Golden Sources", "References",
     "Sources", or "Further Reading" section at the END of the article.
     Extract URLs from there.  Fall back to inline URLs in the article body
     only if no dedicated section exists.  Never invent or guess URLs.
  6. other_sources: same lookup logic as Rule 5 — extract from a dedicated
     "Other Sources" or secondary further-reading section if present;
     otherwise write: other_sources: []
  7. Always include the Introduction as the FIRST section.  Course articles
     always open with a short intro (100–250 words) that callbacks to
     previous lessons and previews the current lesson.  Include it even if
     the intro is brief; set target_words to the actual prose count.
  8. Do NOT name specific Python class names, method names, or implementation
     details from code (e.g. "inspect.signature()", "5-step loop", exact
     parameter names).  Stay at the concept level: name the pattern or
     mechanism, not the code detail.
  9. target_length_words (top-level): sum of all section target_words values
     ONLY — do NOT include words from code blocks, diagrams, or the source
     list at the end of the article.
 10. Output raw YAML only.  No markdown code fences, no preamble.
 11. sections list: each numbered entry in the SECTION PROSE WORD COUNTS
     block must become its own section entry.  Do NOT merge two entries into
     one.  Sub-headings that are already combined in that block (because they
     are subsections of a parent section) should NOT be split back out.
 12. diagrams: scan each section for Mermaid code blocks and author-created
     conceptual diagrams (flowcharts, block/architecture diagrams, sequence
     diagrams).  For each, add ONE planning-level entry to that section's
     `diagrams` list describing what the diagram must convey (e.g.
     "Mermaid flowchart: user query → retriever → augmentation → generator").
     These are required visual deliverables, so capture every one you find.
     Do NOT include external screenshots, photos, or decorative images, and
     do NOT invent diagrams that are not in the article.  If a section has no
     such diagram, OMIT the `diagrams` key for that section.
 13. YAML quoting — always double-quote any string value that contains a
     colon character (`:`), e.g. ``title: "The RAG System: Core Components"``.
     Failure to quote will cause a parse error.
 14. YAML quoting — every item in a sequence (key_points, diagrams, etc.)
     must be a fully-quoted string if it contains any double-quote, colon,
     or other YAML special character.  Wrap the entire value in double-quotes
     and escape internal double-quotes as ``\"``.  Never start a list item
     with a partial quoted segment such as ``- "foo" bar baz``.\
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _repair_yaml(text: str) -> str:
    """Fix common LLM YAML-generation errors before parsing.

    Handles two patterns:
    1. Sequence items with a partially-quoted leading segment followed by
       plain text, e.g. ``- "Lost in the middle" degradation …``
       → ``- "Lost in the middle degradation …"``
    2. Mapping values that contain an unquoted colon, e.g.
       ``- title: The RAG System: Core Components``
       → ``- title: "The RAG System: Core Components"``
    """
    lines = text.splitlines()
    result = []
    for line in lines:
        # Fix 1: sequence items of the form:  - "quoted part" trailing text
        m1 = re.match(r'^(\s*-\s+)"(.*?"?.*?)"(\s+\S.*)$', line)
        if m1:
            prefix, first, rest = m1.group(1), m1.group(2), m1.group(3).strip()
            combined = (first + " " + rest).replace("\\", "\\\\").replace('"', '\\"')
            line = f'{prefix}"{combined}"'
        else:
            # Fix 2: mapping values with an unquoted colon
            m2 = re.match(r"^(\s*(?:-\s+)?)(\w[\w_]*):\s+(.+)$", line)
            if m2:
                prefix, key, value = m2.group(1), m2.group(2), m2.group(3)
                # Skip already-quoted or block-scalar values, numbers, booleans
                if not (
                    value.startswith('"')
                    or value.startswith("'")
                    or value.startswith("|")
                    or value.startswith(">")
                    or value.startswith("[")
                    or value.startswith("{")
                    or re.match(r"^[\d.]+$", value)
                    or value in ("true", "false", "null", "~")
                ):
                    if ": " in value or value.endswith(":"):
                        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
                        line = f'{prefix}{key}: "{escaped}"'
        result.append(line)
    return "\n".join(result)


def _read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _load_brief(brief_path: Path, external: bool = False) -> dict[str, Any]:
    """Load and validate a brief YAML file.

    When ``external=True`` (standalone article, not a course lesson), the
    course-specific keys (lesson_number, lesson_scope, audience, concepts_*)
    are not required.
    """
    with brief_path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if external:
        required = [
            "title",
            "topic_summary",
            "why_valuable",
            "target_length_words",
            "theory_practice_ratio",
            "sections",
            "golden_sources",
        ]
    else:
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
    """Render a brief dict into a compact, human-readable text for the LLM prompt.

    Course-specific fields (lesson_number, lesson_scope, audience, concepts_*)
    are included only when present, so this function works for both course and
    external (standalone) briefs.
    """
    lesson_num = brief.get("lesson_number", 0)
    title = brief.get("title", "Untitled")
    if lesson_num:
        lines: list[str] = [f"# Lesson {lesson_num}: {title}", ""]
    else:
        lines = [f"# {title}", ""]

    lines += [
        "## Topic Summary",
        brief["topic_summary"].strip(),
        "",
        "## Why Valuable",
        brief["why_valuable"].strip(),
        "",
        f"## Target Length: {brief['target_length_words']:,} words",
        f"## Theory / Practice Ratio: {brief['theory_practice_ratio']}",
    ]
    if brief.get("lesson_scope"):
        lines += ["", f"## Lesson Scope: {brief['lesson_scope']}"]
    if brief.get("audience"):
        lines.append(f"## Audience: {brief['audience']}")

    prev = brief.get("concepts_from_previous_lessons") or []
    if prev:
        lines += ["", "## Concepts from Previous Lessons"]
        for c in prev:
            lines.append(f"- {c}")

    fut = brief.get("concepts_for_future_lessons") or []
    if fut:
        lines += ["", "## Concepts for Future Lessons"]
        for c in fut:
            lines.append(f"- {c}")

    lines += ["", "## Sections"]
    for s in brief["sections"]:
        lines.append(f"  ### {s['title']} (~{s['target_words']} words)")
        for kp in s.get("key_points", []):
            lines.append(f"    - {kp}")
        for ce in s.get("code_examples", []):
            lines.append(f"    - [code example] {ce}")
        for dg in s.get("diagrams", []):
            lines.append(f"    - [diagram] {dg}")

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

    # Section bodies (text after each `## Section N` heading) so we can detect
    # diagram requirements that the section author must reproduce.
    section_bodies = re.split(r"(?m)^## Section \d+\s*[-:].*$", guideline)[1:]

    def _diagrams_from_body(body: str) -> list[str]:
        out: list[str] = []
        for line in body.splitlines():
            stripped = line.strip().lstrip("-*•").strip()
            if re.search(r"\b(mermaid|diagram)\b", stripped, re.IGNORECASE):
                out.append(stripped)
        return out

    sections_payload = []
    for i, (t, w) in enumerate(zip(section_titles, section_lens)):
        body = section_bodies[i] if i < len(section_bodies) else ""
        sec: dict[str, Any] = {"title": t.strip(), "target_words": w, "key_points": []}
        diagrams = _diagrams_from_body(body)
        if diagrams:
            sec["diagrams"] = diagrams
        sections_payload.append(sec)

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


# Heading patterns that indicate a sources/references appendix, not a content section.
_NON_CONTENT_HEADING_RE = re.compile(
    r"^(?:\*+)?(?:References?|Golden Sources?|Other Sources?|Further Reading|Sources?)(?:\*+)?$",
    re.IGNORECASE,
)


def _count_section_prose_words(article_text: str) -> list[tuple[str, int]]:
    """Parse an article by ## headings and count prose-only words in each section.

    Strips fenced code blocks FIRST (to avoid false ## splits inside code),
    then splits on ## headings, and excludes known non-content sections
    (References, Golden Sources, etc.).

    Also includes the pre-heading introduction prose (content before the first
    ## heading, after stripping the H1 title line) as the first entry.

    Returns an ordered list of (section_title, word_count) pairs covering
    only real content sections of the article.
    """

    def _prose_wc(text: str) -> int:
        text = re.sub(r"(?m)^\|.*\|$", "", text)  # table rows
        text = re.sub(r"<!--[\s\S]*?-->", "", text)  # HTML comments
        return len(text.split())

    # Strip code fences before splitting so ## inside code doesn't create
    # phantom sections.
    stripped = re.sub(r"```[\s\S]*?```", "", article_text)

    parts = re.split(r"(?m)^## ", stripped)
    results: list[tuple[str, int]] = []

    # parts[0] is the H1 title + intro prose (before the first ## heading).
    # Strip the H1 line, then count remaining prose as the Introduction.
    intro_body = re.sub(r"(?m)^#[^#][^\n]*\n", "", parts[0])
    intro_wc = _prose_wc(intro_body)
    if intro_wc > 50:  # only add if there is real intro content
        results.append(("Introduction", intro_wc))

    for part in parts[1:]:
        first_nl = part.find("\n")
        if first_nl == -1:
            continue
        title = part[:first_nl].strip()
        # Remove bold markers so '## **Conclusion**' matches normally
        plain_title = re.sub(r"\*+", "", title).strip()
        # Skip sources/references appendix sections
        if _NON_CONTENT_HEADING_RE.match(plain_title):
            continue
        results.append((plain_title, _prose_wc(part[first_nl:])))
    return results


async def _extract_brief_from_article(
    llm,
    article_text: str,
    article_slug: str,
) -> dict[str, Any]:
    """Call the LLM to extract a planning-level brief from a finished article.

    Returns a dict with the same schema as ``_load_brief`` output.
    The caller is responsible for writing the result to a YAML file for
    human review before it is used for guideline generation.
    """
    # Pre-compute lesson number from the slug so the LLM doesn't have to guess.
    lesson_num = 0
    num_m = re.match(r"(\d+)", article_slug)
    if num_m:
        lesson_num = int(num_m.group(1))

    section_prose = _count_section_prose_words(article_text)
    prose_lines = "\n".join(f"  {i}. {title}: {wc} words" for i, (title, wc) in enumerate(section_prose, 1))
    word_count = len(article_text.split())
    user_message = (
        f"Article slug: {article_slug}\n"
        f"Approximate total word count: {word_count:,}\n\n"
        f"SECTION PROSE WORD COUNTS (code fences stripped; sub-headings\n"
        f"inside code blocks are excluded; References/Sources appendix excluded):\n"
        f"{prose_lines}\n\n"
        f"This list is the AUTHORITATIVE section structure for the brief.\n"
        f"Use each word count verbatim as target_words for that section.\n"
        f"Do NOT create sections for any ## headings in the article text that\n"
        f"do not appear in this list — they are sub-headings within their parent\n"
        f"section or appendix material.  Do NOT merge any two listed entries.\n\n"
        f"ARTICLE TEXT:\n{'=' * 60}\n"
        f"{article_text.strip()}\n"
        f"{'=' * 60}\n\n"
        f"Generate the planning brief YAML for this article."
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            messages = [
                SystemMessage(content=_BRIEF_EXTRACTION_SYSTEM_PROMPT),
                HumanMessage(content=user_message),
            ]
            response = await llm.ainvoke(messages)
            text = response.content.strip()

            # Strip markdown code fences if the model wrapped the output
            text = re.sub(r"^```(?:yaml)?\s*\n", "", text)
            text = re.sub(r"\n```\s*$", "", text)
            text = text.strip()

            # Repair common LLM YAML issues before parsing
            text = _repair_yaml(text)

            data = yaml.safe_load(text)
            if not isinstance(data, dict):
                raise ValueError(f"LLM output did not parse to a dict: {type(data)}")

            # Patch lesson_number if the LLM omitted or zeroed it
            if lesson_num and not data.get("lesson_number"):
                data["lesson_number"] = lesson_num

            # Ensure required list fields exist
            for key in ("sections", "golden_sources", "concepts_from_previous_lessons", "concepts_for_future_lessons"):
                if key not in data:
                    data[key] = []

            return data

        except Exception as exc:
            logger.warning("Brief extraction attempt %d/%d failed: %s", attempt, MAX_RETRIES, exc)
            if attempt < MAX_RETRIES:
                wait = attempt * RETRY_BACKOFF_BASE
                logger.info("  retrying in %ds …", wait)
                await asyncio.sleep(wait)

    raise RuntimeError(f"Failed to extract brief from article '{article_slug}' after {MAX_RETRIES} attempts")


def _validate_output(
    guideline: str,
    expected_sections: int,
    brief: dict[str, Any] | None = None,
    external: bool = False,
) -> list[str]:
    """Return a list of validation error strings (empty list = valid)."""
    errors: list[str] = []

    required_h2 = _REQUIRED_H2_EXTERNAL if external else _REQUIRED_H2
    for heading in required_h2:
        if f"## {heading}" not in guideline:
            errors.append(f"Missing required section: ## {heading}")

    if not external and not any(f"## {v}" in guideline for v in _ANCHORING_VARIANTS):
        errors.append("Missing required section: ## Anchoring the Lesson in the Course")

    # Rule 1: no bolded H2 headings, and the first non-empty line must be the
    # correct opening heading for the article type.
    bold_h2 = re.findall(r"^\*+\s*##\s", guideline, re.MULTILINE)
    if bold_h2:
        errors.append(f"Found {len(bold_h2)} bolded/asterisk-wrapped H2 heading(s); H2s must start with exactly '## ' at column 0")
    expected_first = "## Context of the Article" if external else "## Global Context of the Lesson"
    first_nonempty = next((ln for ln in guideline.splitlines() if ln.strip()), "")
    if first_nonempty.strip() != expected_first:
        errors.append(f"First non-empty line must be '{expected_first}' (got: {first_nonempty[:80]!r})")

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
    external: bool = False,
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
        # Prefer the real hand-verified YAML brief when it exists; fall back
        # to re-deriving from the guideline only when no YAML is available.
        brief_yaml_path = _BRIEFS_DIR / f"{article}.yaml"
        if brief_yaml_path.exists():
            compact_brief = _brief_to_text(_load_brief(brief_yaml_path))
            logger.debug("  Few-shot %s: using real brief YAML", article)
        else:
            compact_brief = _derive_compact_brief_from_guideline(full_guideline, article)
            logger.debug("  Few-shot %s: no brief YAML — deriving from guideline", article)
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
                SystemMessage(content=_EXTERNAL_SYSTEM_PROMPT if external else _SYSTEM_PROMPT),
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
            # Post-process: strip Rule 9 meta-commentary the LLM sometimes emits
            # on the last section (e.g. "- Transition is not needed as this is
            # the last section."). Rule 9 forbids it but the LLM still produces it.
            text = re.sub(
                r"\n- Transition is not needed[^\n]*\n",
                "\n",
                text,
            )
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
    external: bool = False,
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

    brief = _load_brief(brief_path, external=external)
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

    guideline_text = await _generate_guideline(llm, brief, few_shot_articles, external=external)

    errors = _validate_output(guideline_text, expected_sections, brief, external=external)
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


async def _build_eval_brief(llm, article: str) -> dict[str, Any]:
    """Build the task brief for an eval-split article.

    Mirrors the real authoring flow:
      1. If a curated ``inputs/briefs/{article}.yaml`` exists, use it.
      2. Otherwise extract a planning brief from the held-out ground-truth
         article via the LLM (rich key_points + diagram requirements) and
         save the result next to the synthesized guideline for inspection.

    The pipeline never reads the original article_guideline.md for this
    article — all information must come from article_ground_truth.md or be
    left for human-in-the-loop editing of the saved brief YAML.
    """
    curated = _BRIEFS_DIR / f"{article}.yaml"
    if curated.exists():
        logger.info("[EVAL] %s: using curated brief %s", article, curated.name)
        return _load_brief(curated)

    # Locate the held-out ground-truth article to extract the brief from.
    gt_path = _EVAL_DATA_DIR / article / "article_ground_truth.md"
    if not gt_path.exists():
        gt_path = _EVAL_DATA_DIR / article / "article.md"
    if not gt_path.exists():
        raise FileNotFoundError(
            f"No ground-truth article for {article!r}: tried article_ground_truth.md and article.md in {_EVAL_DATA_DIR / article}"
        )

    logger.info("[EVAL] %s: extracting brief from %s …", article, gt_path.name)
    brief = await _extract_brief_from_article(llm, _read_file(gt_path), article)

    # Persist the extracted brief for inspection (NOT in inputs/briefs/, to keep
    # the few-shot brief pool clean of held-out test articles).
    inspect_path = _EVAL_DATA_DIR / article / "article_brief_extracted.yaml"
    header = (
        f"# Auto-extracted EVAL brief for: {article}\n"
        f"# Source: {gt_path.name}\n"
        f"# Generated by --eval-mode for inspection only. Edit and copy to\n"
        f"# inputs/briefs/{article}.yaml to pin a curated brief for this article.\n\n"
    )
    _write_file(
        inspect_path,
        header + yaml.dump(brief, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120),
    )
    logger.info("[EVAL] %s: saved extracted brief → %s", article, inspect_path.name)
    return brief


async def eval_mode(few_shot_articles: list[str], llm) -> None:
    """Run synthesizer on test split; save as article_guideline_synthesized.md."""
    logger.info("=" * 70)
    logger.info("EVAL MODE — generating guidelines for test split: %s", TEST_ARTICLES)
    logger.info("Few-shot pool: %s", few_shot_articles)
    logger.info("=" * 70)

    # Source the course-wide boilerplate from the FIRST training article so we
    # never touch any held-out test content.
    boilerplate_source_article = TRAINING_ARTICLES[0]
    boilerplate_path = _EVAL_DATA_DIR / boilerplate_source_article / "article_guideline.md"
    boilerplate_text = _read_file(boilerplate_path) if boilerplate_path.exists() else ""
    if not boilerplate_text:
        logger.warning(
            "[EVAL] Could not load boilerplate source from %s — boilerplate blocks will be LLM-generated",
            boilerplate_path,
        )

    for article in TEST_ARTICLES:
        gt_path_check = (
            _EVAL_DATA_DIR / article / "article_ground_truth.md"
            if (_EVAL_DATA_DIR / article / "article_ground_truth.md").exists()
            else _EVAL_DATA_DIR / article / "article.md"
        )
        if not gt_path_check.exists():
            logger.warning("[SKIP] %s — ground-truth article not found", article)
            continue

        brief = await _build_eval_brief(llm, article)

        logger.info("[EVAL] Generating %s …", article)
        guideline_text = await _generate_guideline(llm, brief, few_shot_articles)

        # Inject verbatim boilerplate from a TRAINING article (never from the
        # held-out original) so the diff reflects only variable section content.
        if boilerplate_text:
            guideline_text = _inject_boilerplate_from_source(guideline_text, boilerplate_text)

        output_path = _EVAL_DATA_DIR / article / "article_guideline_synthesized.md"
        _write_file(output_path, guideline_text)
        word_count = len(guideline_text.split())

        orig_path = _EVAL_DATA_DIR / article / "article_guideline.md"
        orig_sec = len(re.findall(r"^## Section \d+", _read_file(orig_path), re.MULTILINE)) if orig_path.exists() else "?"
        synth_sec = len(re.findall(r"^## Section \d+", guideline_text, re.MULTILINE))
        logger.info(
            "  %-40s orig=%s secs  →  synth=%d secs/%d words",
            article,
            orig_sec,
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


async def from_article_mode(
    articles: list[str],
    force: bool,
    dry_run: bool,
    llm,
) -> None:
    """Extract planning briefs from finished articles; save as YAML for review.

    For each article slug, looks for:
      1. ``{_EVAL_DATA_DIR}/{article}/article_ground_truth.md``  (preferred)
      2. ``{_EVAL_DATA_DIR}/{article}/article.md``               (fallback)
      3. The value itself as a direct file path.

    Output is written to ``inputs/briefs/{article}.yaml`` with a header comment
    reminding the reviewer to check TODO fields before running guideline generation.
    """
    logger.info("=" * 70)
    logger.info("FROM-ARTICLE MODE — extracting briefs for: %s", articles)
    logger.info("Model: %s", _GENERATION_MODEL)
    logger.info("=" * 70)

    _BRIEFS_DIR.mkdir(parents=True, exist_ok=True)

    for raw in articles:
        # Resolve article file path
        article_slug = raw
        article_path = _EVAL_DATA_DIR / raw / "article_ground_truth.md"
        if not article_path.exists():
            article_path = _EVAL_DATA_DIR / raw / "article.md"
        if not article_path.exists():
            # Try as a direct file path
            article_path = Path(raw)
            article_slug = article_path.stem
        if not article_path.exists():
            logger.error(
                "[MISSING] No article file found for %r — tried article_ground_truth.md, article.md, and as a direct path.",
                raw,
            )
            continue

        output_path = _BRIEFS_DIR / f"{article_slug}.yaml"
        if output_path.exists() and not force:
            logger.info(
                "[SKIP] %s — brief already exists at %s (use --force to overwrite)",
                article_slug,
                output_path,
            )
            continue

        word_count = len(_read_file(article_path).split())
        logger.info(
            "[FROM-ARTICLE] %s  (%s, ~%d words) …",
            article_slug,
            article_path.name,
            word_count,
        )

        if dry_run:
            logger.info(
                "  [DRY-RUN] would extract brief from %s via %s → %s",
                article_path.name,
                _GENERATION_MODEL,
                output_path,
            )
            continue

        try:
            article_text = _read_file(article_path)
            brief = await _extract_brief_from_article(llm, article_text, article_slug)
        except Exception:
            logger.exception("FAILED to extract brief for %s", article_slug)
            continue

        # Post-inject sources from the planning guideline when available.
        # The article body only contains inline citations; the curated source
        # list lives in article_guideline.md, which the LLM cannot access.
        guideline_path = _EVAL_DATA_DIR / article_slug / "article_guideline.md"
        if guideline_path.exists():
            try:
                guideline_brief = _extract_brief_dict_from_guideline(_read_file(guideline_path), article_slug)
                injected_golden = guideline_brief.get("golden_sources") or []
                injected_other = guideline_brief.get("other_sources") or []
                if injected_golden:
                    brief["golden_sources"] = injected_golden
                    brief["other_sources"] = injected_other
                    logger.info(
                        "  Sources injected from article_guideline.md: %d golden, %d other",
                        len(injected_golden),
                        len(injected_other),
                    )
            except Exception as exc:
                logger.warning("  Could not inject sources from guideline: %s", exc)

        # Serialise to YAML with a review header
        header = (
            f"# Auto-extracted brief for: {article_slug}\n"
            f"# Source: {article_path.name}\n"
            f"# REVIEW BEFORE USE — check all fields, especially those marked\n"
            f"# '# TODO: review' which require course-context knowledge.\n"
            f"# Then run:\n"
            f"#   uv run python generate_article_guideline.py --article {article_slug}\n\n"
        )
        yaml_text = header + yaml.dump(
            brief,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=120,
        )

        _write_file(output_path, yaml_text)
        n_sections = len(brief.get("sections", []))
        logger.info("  Saved: %s  (%d sections)", output_path, n_sections)
        logger.info(
            "  Next: review %s, then run:\n    uv run python generate_article_guideline.py --article %s",
            output_path.name,
            article_slug,
        )

    logger.info("=" * 70)
    logger.info("Done.")


# ---------------------------------------------------------------------------
# Pipeline entry
# ---------------------------------------------------------------------------


async def run_pipeline(args: argparse.Namespace) -> None:
    # External articles don't use course-based few-shot examples by default;
    # the external system prompt is self-contained. Pass --few-shot explicitly
    # to provide an external article few-shot example (e.g. --few-shot Bird_Eye_Extreme).
    if args.few_shot:
        few_shot = list(args.few_shot)
    elif getattr(args, "external", False):
        few_shot = []
    else:
        few_shot = list(_DEFAULT_FEW_SHOT)

    # Remove the target article(s) from the few-shot pool to prevent leakage
    if args.article:
        few_shot = [a for a in few_shot if a not in args.article]

    if args.eval_mode:
        llm = get_model(_GENERATION_MODEL, _GENERATION_CONFIG)
        await eval_mode(few_shot, llm)
        return

    if args.from_article:
        llm = get_model(_GENERATION_MODEL, _GENERATION_CONFIG)
        await from_article_mode(list(args.from_article), args.force, args.dry_run, llm)
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
    logger.info("  Mode      : %s", "external" if getattr(args, "external", False) else "course")
    logger.info("  Few-shot  : %s", few_shot)
    logger.info("  Model     : %s", _GENERATION_MODEL)
    logger.info("  Dry-run   : %s", args.dry_run)
    logger.info("  Force     : %s", args.force)
    logger.info("=" * 70)

    for article in articles:
        logger.info("─" * 60)
        try:
            await generate_for_brief(article, few_shot, args.force, args.dry_run, llm, external=getattr(args, "external", False))
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
        "--from-article",
        nargs="+",
        metavar="ARTICLE",
        dest="from_article",
        help=(
            "Extract a planning brief from a finished article and save as a YAML file for review. "
            "Accepts article slugs (looks for article_ground_truth.md in the eval dataset) "
            "or direct file paths. Output: inputs/briefs/{article}.yaml"
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
    parser.add_argument(
        "--external",
        action="store_true",
        help=(
            "Generate a standalone (non-course) article guideline using the external "
            "template (## Context of the Article / ## Article Outline; no Anchoring "
            "or Narrative Flow sections). Brief YAML only requires: title, "
            "topic_summary, why_valuable, target_length_words, theory_practice_ratio, "
            "sections, golden_sources."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    asyncio.run(run_pipeline(args))


if __name__ == "__main__":
    main()
