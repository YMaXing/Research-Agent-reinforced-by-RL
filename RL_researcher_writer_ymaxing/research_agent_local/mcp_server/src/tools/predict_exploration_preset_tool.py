"""
Meta-reasoner tool: RL-guided exploration preset prediction.

Uses a GRPO-trained Qwen3-4B + LoRA adapter to analyse the exploitation
digest and produce structured section-level signals that help the client
LLM (Grok) decide how many rounds of exploration to run and in what order.

If exploitation_digest.md does not yet exist in the research directory, the
tool generates it on-the-fly via a 4-stage pipeline (COLLECT → COMPRESS →
ASSEMBLE → GENERATE) before running RL inference.

Signal semantics
----------------
preset (0–5)
    The RL model's recommended exploration strategy:
      0 – No exploration (baseline)
      1 – 1 round, balanced
      2 – 2 rounds, balanced then depth
      3 – 2 rounds, depth then breadth
      4 – 3 rounds, balanced then depth then breadth
      5 – 3 rounds, depth then breadth then depth

confidence
    Probability mass on the chosen preset (0.0–1.0).
    • ≥0.70 → strong signal, model is decisive.
    • 0.40–0.70 → moderate; consider section breakdown.
    • <0.40 → uncertain; apply your own judgement.

entropy (bits, base-2)
    Spread of the probability distribution over presets 0–5.
    Computed as H = −∑ p·log₂(p+ε) over the aggregated preset probs.
    • H < 0.5 → very confident (nearly all mass on one preset).
    • 0.5–1.5 → moderate confidence.
    • H > 1.5 → model is uncertain; override freely.

floor_correction_applied
    True when the max-preset floor heuristic fired: the aggregate vote was
    P0–P2, but at least one individual section predicted a higher preset.
    The floor prevents intro-section dominance from masking deep technical
    sections that need more exploration.

top2 (per section)
    The two highest-probability presets for each section and their probabilities.
    A large gap between rank-1 and rank-2 (e.g. [P3, 0.81], [P2, 0.11]) means
    the model is highly confident for that section.
    A small gap (e.g. [P3, 0.35], [P4, 0.32]) means the section is ambiguous.

guidance
    One-sentence synthesis for the client LLM to use as a reasoning seed.
    When entropy is high (>1.5) the guidance explicitly says so.

Model architecture note
-----------------------
The RL model was trained with GRPO (Group Relative Policy Optimisation) on
section-level inference tasks across 4 AI-course articles. It predicts the
per-section preset using a section-level system prompt, then aggregates by
word-count-weighted probability vote. A max-preset floor is applied when the
aggregate vote is ≤P2 to prevent under-exploration caused by short intro sections
dominating the vote.
"""

from __future__ import annotations

import asyncio
import logging
import math
import threading
from pathlib import Path
from typing import Any, Dict

from ..config.settings import settings

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Lazy singleton — model loads once on first tool call (~3 min on GPU)
# ---------------------------------------------------------------------------
_selector = None
_selector_lock = threading.Lock()

# parents[3] = research_agent_local/  (tools is 3 levels below: mcp_server/src/tools/)
_TRAINING_DIR = Path(__file__).resolve().parents[3] / "training"

# ---------------------------------------------------------------------------
# Digest generation constants (mirrors generate_digests.py)
# ---------------------------------------------------------------------------
_DIGEST_MODEL = "grok-4-1-fast-reasoning"
_COMPRESS_CONCURRENCY = 5
_MAX_SOURCE_CHARS = 80_000
_SKIP_SECTION_KEYWORDS = {
    "global context", "anchoring", "achoring", "narrative flow",
    "lesson outline", "outline", "golden sources", "other sources", "article code",
}

_COMPRESS_SYSTEM = "You are a precise research summarizer. Output only the summary, no preamble."
_COMPRESS_USER_TEMPLATE = """\
Summarize the following research source.
Source filename: {filename}
Source type: {source_type}

Produce a factual 200-300 token summary covering:
- Main topic and key concepts explained
- Concrete examples, tools, frameworks, APIs, or techniques mentioned (use exact names)
- Specific data points, benchmarks, or claims that could support article sections
- Notable limitations or gaps in coverage

Be specific. Do not editorialize.

<source>
{content}
</source>"""

_DIGEST_SYSTEM = """\
You are generating a structured exploitation digest for an RL policy model.
Your output will be used as compact context for a small RL policy model to select
research exploration strategies. Be specific, factual, and follow the format exactly.
Target 5,000-8,000 tokens total. Do NOT summarize briefly."""

_DIGEST_USER_TEMPLATE = """\
Generate a structured exploitation digest.

{context}

---

Generate the exploitation digest in EXACTLY this format:

# Exploitation Digest

## 1. Source Inventory

### Golden Sources
| Source | Type | Key Contributions |
|--------|------|------------------|

### Exploitation Sources
| Source | Type | Key Contributions |
|--------|------|------------------|

### Tavily Exploitation Results
- Total exploitation rounds: N
- Total queries run: N
- Per-query yield quality: [brief assessment]

## 2. Per-Section Coverage Analysis

For EACH content section in the article guideline (skip preamble sections like
Global Context, Anchoring, Narrative Flow, Outline, Golden Sources, Other Sources):

### S{{N}} — {{exact section title}}
**Coverage: STRONG|PARTIAL|WEAK**
**What we have:** [3-5 sentences. Name specific source files. Cite concrete facts, tools, benchmarks.]
**Remaining depth gaps:** [2-4 specific sub-topics lacking coverage]
**Remaining breadth gaps:** [1-3 adjacent topics not covered]

## 3. Overall Gap Profile
- **Gap counts:** depth_gaps=N, breadth_gaps=N
- **Weakest sections:** [comma-separated]
- **Strongest sections:** [comma-separated]
- **Gap character:** [one sentence]
- **Query saturation:** [assessment]
- **Key insight for exploration strategy:** [one actionable sentence]
"""

_REQUIRED_DIGEST_HEADERS = [
    "## 1. Source Inventory",
    "### Golden Sources",
    "### Exploitation Sources",
    "## 2. Per-Section Coverage Analysis",
    "## 3. Overall Gap Profile",
]


def _read_md_dir(directory: Path) -> dict[str, str]:
    if not directory.exists():
        return {}
    return {
        f.name: f.read_text(encoding="utf-8", errors="replace")
        for f in sorted(directory.glob("*.md"))
    }


def _collect_sources(research_dir: Path) -> dict:
    """Read all source files for a research directory."""
    dot_research = research_dir / ".research"

    def _optional(path: Path) -> str:
        return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

    return {
        "guideline": _optional(research_dir / "article_guideline.md"),
        "golden_web": _read_md_dir(dot_research / "urls_from_guidelines"),
        "golden_youtube": _read_md_dir(dot_research / "urls_from_guidelines_youtube_videos"),
        "golden_code": _read_md_dir(dot_research / "urls_from_guidelines_code"),
        "exploitation": _read_md_dir(dot_research / "urls_from_guidelines_exploitation"),
        "tavily_results": _optional(dot_research / "tavily_results.md"),
        "full_queries": _optional(dot_research / "full_queries.md"),
    }


async def _compress_one(
    client,
    semaphore: asyncio.Semaphore,
    filename: str,
    source_type: str,
    content: str,
) -> str:
    if len(content) > _MAX_SOURCE_CHARS:
        content = content[:_MAX_SOURCE_CHARS] + "\n\n[...content truncated...]"
    async with semaphore:
        response = await client.chat.completions.create(
            model=_DIGEST_MODEL,
            messages=[
                {"role": "system", "content": _COMPRESS_SYSTEM},
                {"role": "user", "content": _COMPRESS_USER_TEMPLATE.format(
                    filename=filename, source_type=source_type, content=content,
                )},
            ],
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()


async def _compress_all(client, sources: dict) -> dict[str, dict[str, str]]:
    semaphore = asyncio.Semaphore(_COMPRESS_CONCURRENCY)
    keys: list[tuple[str, str]] = []
    tasks = []
    for source_type in ("golden_web", "golden_youtube", "golden_code", "exploitation"):
        for filename, content in sources[source_type].items():
            keys.append((source_type, filename))
            tasks.append(_compress_one(client, semaphore, filename, source_type, content))
    results = await asyncio.gather(*tasks)
    summaries: dict[str, dict[str, str]] = {
        "golden_web": {}, "golden_youtube": {}, "golden_code": {}, "exploitation": {},
    }
    for (source_type, filename), summary in zip(keys, results):
        summaries[source_type][filename] = summary
    return summaries


def _format_source_block(tag: str, summaries: dict[str, str]) -> str:
    if not summaries:
        return f"<{tag}>\n(none)\n</{tag}>"
    parts = [f"### {fname}\n{summary}" for fname, summary in summaries.items()]
    return f"<{tag}>\n" + "\n\n".join(parts) + f"\n</{tag}>"


def _assemble_context(sources: dict, summaries: dict) -> str:
    blocks = [
        f"<article_guideline>\n{sources['guideline']}\n</article_guideline>",
        _format_source_block("golden_web_summaries", summaries["golden_web"]),
        _format_source_block("golden_youtube_summaries", summaries["golden_youtube"]),
        _format_source_block("golden_code_summaries", summaries["golden_code"]),
        _format_source_block("exploitation_source_summaries", summaries["exploitation"]),
        f"<tavily_exploitation_results>\n{sources['tavily_results']}\n</tavily_exploitation_results>",
        f"<exploitation_query_history>\n{sources['full_queries']}\n</exploitation_query_history>",
    ]
    return "\n\n".join(blocks)


async def _generate_digest_text(client, context: str) -> str:
    response = await client.chat.completions.create(
        model=_DIGEST_MODEL,
        messages=[
            {"role": "system", "content": _DIGEST_SYSTEM},
            {"role": "user", "content": _DIGEST_USER_TEMPLATE.format(context=context)},
        ],
        max_tokens=16384,
    )
    return response.choices[0].message.content.strip()


async def _generate_digest(research_dir: Path, api_key: str, base_url: str) -> str:
    """Run COLLECT→COMPRESS→ASSEMBLE→GENERATE and return the digest text."""
    from openai import AsyncOpenAI  # noqa: PLC0415
    client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    logger.info("Digest generation: COLLECT stage")
    sources = _collect_sources(research_dir)

    total = sum(len(v) for v in sources.values() if isinstance(v, dict))
    logger.info(f"Digest generation: COMPRESS stage ({total} sources)")
    summaries = await _compress_all(client, sources)

    logger.info("Digest generation: ASSEMBLE stage")
    context = _assemble_context(sources, summaries)

    logger.info("Digest generation: GENERATE stage")
    digest = ""
    for attempt in range(1, 4):
        digest = await _generate_digest_text(client, context)
        if all(h in digest for h in _REQUIRED_DIGEST_HEADERS):
            logger.info(f"Digest generation: validation passed (attempt {attempt})")
            return digest
        logger.warning(f"Digest generation: validation failed (attempt {attempt}), retrying")
    logger.warning("Digest generation: all 3 attempts failed — using last candidate")
    return digest


_PRESET_NAMES = {
    0: "no_exploration",
    1: "1_round_balanced",
    2: "2_rounds_balanced_then_depth",
    3: "2_rounds_depth_then_breadth",
    4: "3_rounds_balanced_depth_breadth",
    5: "3_rounds_depth_breadth_depth",
}
_NUM_PRESETS = 6
_ENTROPY_THRESHOLD_HIGH = 1.5
_ENTROPY_THRESHOLD_LOW = 0.5
_CONFIDENCE_STRONG = 0.70
_CONFIDENCE_MODERATE = 0.40


def _get_selector():
    global _selector
    if _selector is None:
        with _selector_lock:
            if _selector is None:
                import sys
                sys.path.insert(0, str(_TRAINING_DIR))
                from infer import ExplorationStrategySelector  # type: ignore[import]  # noqa: PLC0415
                logger.info("Loading RL model (first call — ~3 min on GPU)…")
                _selector = ExplorationStrategySelector()
                logger.info("RL model loaded and cached.")
    return _selector


def _entropy(probs: list[float]) -> float:
    """Shannon entropy in bits: H = -∑ p·log₂(p+ε)."""
    eps = 1e-12
    return -sum(p * math.log2(p + eps) for p in probs)


def _top2(probs: list[float]) -> list[list]:
    """Return [[preset_str, prob], [preset_str, prob]] for the top-2 presets."""
    ranked = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
    return [[f"P{ranked[i][0]}", round(ranked[i][1], 4)] for i in range(2)]


def _guidance(preset: int, confidence: float, entropy: float, floor_applied: bool) -> str:
    parts: list[str] = []

    if entropy > _ENTROPY_THRESHOLD_HIGH:
        parts.append(
            f"RL model is uncertain (H={entropy:.2f} bits > 1.5) — apply your own judgement."
        )
    elif confidence >= _CONFIDENCE_STRONG:
        parts.append(
            f"RL model strongly recommends P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}, confidence {confidence:.0%})."
        )
    else:
        parts.append(
            f"RL model recommends P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}, confidence {confidence:.0%})."
        )

    if floor_applied:
        parts.append(
            "Floor correction fired: a technical section needed more exploration "
            "than the aggregate vote suggested."
        )

    return " ".join(parts)


async def predict_exploration_preset_tool(research_directory: str) -> Dict[str, Any]:
    """
    Predict the optimal exploration preset for an article using the trained RL model.

    Reads (or auto-generates) exploitation_digest.md from the research directory,
    runs per-section inference through the GRPO-trained Qwen3-4B + LoRA model,
    and returns structured signals to help the client LLM decide how many rounds
    of exploration to run and in what order.

    If exploitation_digest.md does not yet exist in the research directory, the tool
    generates it on-the-fly via a 4-stage pipeline (COLLECT→COMPRESS→ASSEMBLE→GENERATE)
    using the XAI API and writes it to exploitation_digest.md before running inference.
    This requires the XAI_API_KEY environment variable to be set and the .research/
    subfolder to contain the exploitation sources collected during step 3.

    The tool performs two-stage inference:
      Stage 1 (RL model): per-section preset prediction via word-count-weighted
                          probability vote → aggregate recommendation.
      Stage 2 (client):   the client uses the returned signals to make the final
                          decision, overriding the RL model when entropy is high
                          or section signals are contradictory.

    Args:
        research_directory: Path to the research directory. Must contain either:
          - exploitation_digest.md (pre-existing, used directly), or
          - article_guideline.md + .research/ subfolder (digest auto-generated).

    Returns:
        Dict with keys:
          status               – "success" or "error"
          digest_generated     – True if the digest was generated on-the-fly
          rl_recommendation    – aggregate preset, name, confidence, entropy,
                                 floor_correction_applied
          section_signals      – per-section list of preset, name, top2 probs
          guidance             – one-sentence synthesis for the client LLM
          message              – human-readable summary
    """
    research_path = Path(research_directory)
    digest_path = research_path / "exploitation_digest.md"

    if not research_path.exists():
        return {
            "status": "error",
            "message": f"Research directory not found: {research_directory}",
        }

    digest_generated = False

    if not digest_path.exists():
        # Auto-generate the digest on-the-fly
        logger.info(f"exploitation_digest.md not found — generating on-the-fly for {research_directory}")
        if settings.xai_api_key is None:
            return {
                "status": "error",
                "message": (
                    "exploitation_digest.md not found and XAI_API_KEY is not configured. "
                    "Either run the exploitation phase first or provide an XAI API key."
                ),
            }
        try:
            digest = await _generate_digest(
                research_path,
                api_key=settings.xai_api_key.get_secret_value(),
                base_url="https://api.x.ai/v1",
            )
            digest_path.write_text(digest, encoding="utf-8")
            digest_generated = True
            logger.info(f"Digest written to {digest_path}")
        except Exception as exc:
            logger.exception("On-the-fly digest generation failed")
            return {"status": "error", "message": f"Digest generation failed: {exc}"}
    else:
        try:
            digest = digest_path.read_text(encoding="utf-8")
        except Exception as exc:
            return {"status": "error", "message": f"Failed to read digest: {exc}"}

    try:
        selector = _get_selector()
    except Exception as exc:
        logger.exception("Failed to load RL model")
        return {"status": "error", "message": f"RL model failed to load: {exc}"}

    try:
        preset, agg_probs, section_details, meta = selector.predict_article_verbose(digest)
    except Exception as exc:
        logger.exception("Inference error")
        return {"status": "error", "message": f"Inference failed: {exc}"}

    # --- Derived signals ---
    confidence = round(agg_probs[preset], 4)
    h = round(_entropy(agg_probs), 4)
    section_vote = meta.get("section_vote", preset)
    section_floor = meta.get("section_floor", 0)
    floor_applied = section_vote <= 2 and section_floor > section_vote and h <= 1.5

    section_signals = []
    for d in section_details:
        section_signals.append({
            "title": d["title"],
            "preset": d["chosen"],
            "name": _PRESET_NAMES[d["chosen"]].replace("_", " "),
            "top2": _top2(d["probs"]),
        })

    guidance_str = _guidance(preset, confidence, h, floor_applied)

    result = {
        "status": "success",
        "digest_generated": digest_generated,
        "rl_recommendation": {
            "preset": preset,
            "name": _PRESET_NAMES[preset].replace("_", " "),
            "confidence": confidence,
            "entropy_bits": h,
            "floor_correction_applied": floor_applied,
        },
        "section_signals": section_signals,
        "guidance": guidance_str,
        "message": (
            f"RL model recommends preset P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}) "
            f"with {confidence:.0%} confidence across {len(section_signals)} sections. "
            f"Entropy: {h:.2f} bits."
        ),
    }
    return result
