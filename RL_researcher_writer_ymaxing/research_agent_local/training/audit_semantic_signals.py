"""Standalone, offline extractor for three qualitative signals a numeric
coverage-gap scorer cannot see: scripted/self-contained example content,
evidentiary saturation (source redundancy + topic canonicity), and
per-section argumentative risk (interpretive/normative weight vs. its own
source support).

This is a DIAGNOSTIC tool only -- it does not call, modify, or influence the
shipped RL+guards / Grok planner decision path in preset_planner_handler.py.
It exists so the three signals identified from a manual close-reading of
Insects_Consciousness and 07_reasoning_planning (both high-regret TEST misses)
can be extracted for the whole corpus and correlated against known oracle
labels / regret figures BEFORE anyone decides whether to wire them into a
live decision. See run13_rl_grok_pipeline_analysis.md Appendix A for that
close-reading writeup.

Usage (from research_agent_local/training/, requires XAI_API_KEY):
    uv run python audit_semantic_signals.py --articles Insects_Consciousness,07_reasoning_planning
    uv run python audit_semantic_signals.py --test-only
    uv run python audit_semantic_signals.py --all
    uv run python audit_semantic_signals.py --articles HNSW --dry-run   # print prompt only, no API call

Do NOT invoke with a bare `python`/`python3` (system interpreter) -- it lacks the
`openai` package. `uv run` resolves this project's own .venv (openai is a
declared dependency here, see pyproject.toml), so no explicit venv path is needed.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent
_REPO_ROOT = _AGENT_DIR.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_OUT_DIR = _AGENT_DIR / "grok_planner_test_results" / "semantic_signals_results"

# Same .env the rest of the pipeline reads XAI_API_KEY from (predict_exploration_preset_tool.py).
_MCP_CLIENT_ENV = _AGENT_DIR / "mcp_client" / ".env"

# Same model as the production planner (preset_planner_handler.py::_PLANNER_MODEL)
# for a like-for-like comparison; override with --model if desired.
_DEFAULT_MODEL = "grok-4.20-0309-reasoning"

_TRAIN_LESSONS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access",
    "11_multimodal",
]
_VARIANTS = ("var_minimal", "var_standard", "var_demanding")
TRAIN_ARTICLES: list[str] = [
    f"{lesson}__{var}" for lesson in sorted(_TRAIN_LESSONS) for var in _VARIANTS
]
TEST_ARTICLES: list[str] = sorted([
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI",
    "Bird_Eye_Extreme", "Dark_Dimension", "Distinct_AI_Models",
    "Earth_Oceans_Origin", "Gravity_Entropy", "HNSW", "Insects_Consciousness",
    "Space-Time_QECC", "State_of_LLM_Reasoning", "Understanding_Reasoning_LLMs",
])

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

_SEMANTIC_SIGNAL_SYSTEM = """\
You are a research-methodology auditor for an autonomous article-writing system. \
You do NOT choose an exploration preset. Your only job is to extract three specific \
qualitative judgments from an article's guideline and research digest that a numeric \
coverage-gap scorer cannot see, so they can be tested offline against known outcomes.

CONTEXT
Before an article is written, the system can run extra rounds of autonomous web \
exploration (0-3 rounds: skip / light / standard / deep) to close coverage gaps. A \
separate, already-shipped pipeline scores per-section coverage gaps numerically \
(need_depth, need_breadth, orphan anchors, self-contained flags) and picks a preset \
from that. That numeric scorer cannot read prose for genre, redundancy, or \
argumentative risk -- your job is to supply exactly those three qualitative signals, \
per section where noted, so they can be correlated with the numeric scorer's actual \
errors before anyone decides whether to wire them into a live decision.

INPUT
You will receive the full author-written article guideline (verbatim, all sections) \
and the research digest (source previews and per-section coverage-gap checklists).

THE THREE SIGNALS

1. SCRIPTED-EXAMPLE FRACTION (per section, 0.0-1.0)
   Some sections are NOT open topics needing evidence -- they are fully pre-scripted, \
   invented illustrative narratives or dialogues (e.g. a step-by-step worked example \
   with specific fictional inputs/outputs dictated verbatim by the guideline). No \
   amount of exploration can improve such content because it is not sourced from the \
   world at all -- it is authored. Score how much of THIS section's content is this \
   kind of self-contained, invented narrative, as opposed to claims that describe or \
   interpret real-world facts, findings, or sources.
     0.0 = the section is entirely open, evidence-seeking content.
     1.0 = the section is entirely a pre-scripted worked example with no room for, or \
           need of, external material.
   Distinguish this from a section merely being SHORT or already well-covered -- a \
   short section about a real, external fact can still score low here; a long section \
   can score high here if its content is invented illustration throughout.

2. EVIDENTIARY SATURATION (article-level, two separate 0.0-1.0 scores)
   a. source_independence: are the found sources actually independent, distinct \
      documents, or mostly restatements/mirrors of the same one or two primary \
      documents (e.g. a declaration's homepage and its own "background" subpage, or \
      two blog posts summarizing the same paper)?
        0.0 = sources are almost entirely redundant restatements of 1-2 documents.
        1.0 = every source is an independent primary document or study.
   b. topic_canonicity: independent of what was actually found, how likely is it that \
      further exploration on THIS topic would mostly re-surface material that is \
      already extremely well-documented across the general literature/internet \
      (canonical, widely-explained patterns or concepts), as opposed to a niche or \
      fast-moving topic where genuinely new, non-redundant material is still findable?
        0.0 = niche/novel topic, more searching would likely surface real new material.
        1.0 = extremely canonical/oversaturated topic, more searching mostly finds \
              restatements of what a competent writer already knows.
   Both scores push toward LESS exploration being valuable when high, but for \
   different reasons (low source_independence = "what we found overlaps itself"; \
   high topic_canonicity = "there is little new to find even if we looked harder").

3. ARGUMENTATIVE RISK (per section, 0.0-1.0)
   Independent of raw coverage-gap counts, does this section carry unusually HIGH \
   interpretive, normative, evaluative, or cross-domain-analogy weight RELATIVE TO \
   how well its own cited sources actually support that reasoning? A section that \
   draws policy conclusions, ethical claims, or analogies to a different field, while \
   citing thin, generic, or tangential support for that specific leap, should score \
   high here even if its raw coverage-gap numbers look unremarkable. A section that \
   is purely descriptive/summarizing well-matched sources should score low, even if \
   it is long or technical.
     0.0 = purely descriptive, low argumentative weight, or well-supported by its own \
           cited sources.
     1.0 = section makes a high-stakes original argument, normative claim, or \
           cross-domain analogy that is thinly supported by what has actually been \
           found so far.

CALIBRATION EXAMPLE (illustrative only, not from the corpus)
A lesson that spells out an entire fictional dialogue between a user and an agent, \
turn by turn, should score scripted_example_fraction near 1.0 for that section \
regardless of how technical the surrounding topic is. An article built entirely \
around interpreting one named policy document, whose only other sources are \
different pages of that same document's own website, should score \
source_independence near 0.0 even if total_sources looks adequate. A section that \
pivots from summarizing a scientific finding to asserting what it implies for an \
unrelated field (e.g. "this also tells us X about AI systems"), backed only by the \
same narrow sources used for the original finding, should score argumentative_risk \
high for that pivot.

OUTPUT
Reason briefly first, then output ONLY this JSON block, with nothing after it:

```json
{{
  "sections": [
    {{
      "sec_id": "<matches the section id from the digest>",
      "scripted_example_fraction": <float 0.0-1.0>,
      "argumentative_risk": <float 0.0-1.0>,
      "risk_rationale": "<1 sentence citing the specific guideline text and/or source gap>"
    }}
  ],
  "source_independence": <float 0.0-1.0>,
  "topic_canonicity": <float 0.0-1.0>,
  "overall_notes": "<2-3 sentences summarizing the dominant signal, if any>"
}}
```"""

_SEMANTIC_SIGNAL_USER_TEMPLATE = """\
## Article guideline (verbatim)
{guideline_text}

---

## Research digest -- sources and section coverage
{digest_text}

---

## Your task
Score all three signals for every content section listed in the digest's \
section_coverage block. Then output ONLY the JSON block specified in your \
instructions (nothing after it)."""


# ---------------------------------------------------------------------------
# Input loading
# ---------------------------------------------------------------------------

def _load_input(article: str) -> tuple[str, str]:
    """Return (guideline_text, digest_text) exactly as found on disk."""
    art_dir = _BASES_DIR / article
    guideline_path = art_dir / "article_guideline.md"
    digest_path = art_dir / "research_digest.md"
    guideline_text = guideline_path.read_text(encoding="utf-8") if guideline_path.exists() else "(no article_guideline.md found)"
    digest_text = digest_path.read_text(encoding="utf-8") if digest_path.exists() else "(no research_digest.md found)"
    return guideline_text, digest_text


# ---------------------------------------------------------------------------
# JSON extraction (mirrors preset_planner_handler.py::_extract_json_block)
# ---------------------------------------------------------------------------

def _extract_json_block(raw: str) -> dict:
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    json_str = m.group(1) if m else ""
    if not json_str:
        matches = re.findall(r"\{.*\}", raw, re.DOTALL)
        json_str = matches[-1] if matches else ""
    if not json_str:
        return {}
    try:
        return json.loads(json_str)
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Model call
# ---------------------------------------------------------------------------

async def score_article(article: str, model: str, api_key: str) -> dict:
    """Call the LLM once for `article` and return the parsed signal dict
    (plus the raw response text, for auditing parse failures)."""
    from openai import AsyncOpenAI  # noqa: PLC0415

    guideline_text, digest_text = _load_input(article)
    user_msg = _SEMANTIC_SIGNAL_USER_TEMPLATE.format(
        guideline_text=guideline_text, digest_text=digest_text
    )

    client = AsyncOpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": _SEMANTIC_SIGNAL_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        max_tokens=4096,
    )
    raw = (response.choices[0].message.content or "").strip()
    parsed = _extract_json_block(raw)
    return {"article": article, "parsed": parsed, "raw": raw, "parse_ok": bool(parsed)}


def build_prompt_preview(article: str) -> str:
    """Render the exact system+user prompt for --dry-run inspection, no API call."""
    guideline_text, digest_text = _load_input(article)
    user_msg = _SEMANTIC_SIGNAL_USER_TEMPLATE.format(
        guideline_text=guideline_text, digest_text=digest_text
    )
    return (
        f"=== SYSTEM ===\n{_SEMANTIC_SIGNAL_SYSTEM}\n\n"
        f"=== USER ===\n{user_msg}"
    )


# ---------------------------------------------------------------------------
# API key
# ---------------------------------------------------------------------------

def _read_api_key_from_env_file(var_name: str, env_path: Path) -> str | None:
    """Minimal .env parser (no python-dotenv dependency) -- extracts one
    variable's value and never logs/echoes it."""
    if not env_path.exists():
        return None
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        if key.strip() == var_name:
            return value.strip().strip('"').strip("'")
    return None


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

async def _main_async(articles: list[str], model: str, dry_run: bool, out_dir: Path) -> None:
    if dry_run:
        for a in articles:
            print(build_prompt_preview(a))
            print("\n" + "=" * 100 + "\n")
        return

    api_key = os.environ.get("XAI_API_KEY") or _read_api_key_from_env_file("XAI_API_KEY", _MCP_CLIENT_ENV)
    if not api_key:
        print(f"ERROR: XAI_API_KEY not set in environment or found in {_MCP_CLIENT_ENV}.")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for a in articles:
        print(f"  {a} ...", end=" ", flush=True)
        try:
            result = await score_article(a, model, api_key)
        except Exception as exc:
            print(f"ERROR: {exc}")
            results.append({"article": a, "error": str(exc)})
            continue
        if not result["parse_ok"]:
            print("PARSE FAILED (see saved raw response)")
        else:
            p = result["parsed"]
            print(
                f"source_independence={p.get('source_independence')}  "
                f"topic_canonicity={p.get('topic_canonicity')}  "
                f"n_sections_scored={len(p.get('sections', []))}"
            )
        (out_dir / f"{a}.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        results.append(result)

    (out_dir / "_summary.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nSaved {len(results)} result(s) to {out_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract scripted-example / evidentiary-saturation / "
        "argumentative-risk signals per article, for offline backtesting."
    )
    parser.add_argument("--articles", type=str, help="Comma-separated exact bases/ directory names.")
    parser.add_argument("--all", action="store_true", help="Run all 24 TRAIN + 16 TEST articles.")
    parser.add_argument("--train-only", action="store_true")
    parser.add_argument("--test-only", action="store_true")
    parser.add_argument("--model", type=str, default=_DEFAULT_MODEL)
    parser.add_argument("--out-dir", type=Path, default=_OUT_DIR)
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print the exact rendered prompt(s) and exit; no API call, no XAI_API_KEY needed.",
    )
    args = parser.parse_args()

    if args.articles:
        articles = [a.strip() for a in args.articles.split(",")]
    elif args.test_only:
        articles = list(TEST_ARTICLES)
    elif args.train_only:
        articles = list(TRAIN_ARTICLES)
    elif args.all:
        articles = TRAIN_ARTICLES + TEST_ARTICLES
    else:
        parser.error("Specify one of --articles, --all, --train-only, --test-only.")
        return

    missing = [a for a in articles if not (_BASES_DIR / a).is_dir()]
    if missing:
        print(f"ERROR: no bases/ directory for: {missing}")
        return

    asyncio.run(_main_async(articles, args.model, args.dry_run, args.out_dir))


if __name__ == "__main__":
    main()
