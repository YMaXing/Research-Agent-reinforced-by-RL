"""
Meta-reasoner tool: RL-guided exploration preset prediction.

Uses a GRPO-trained Qwen3-4B + LoRA adapter to analyse the research
digest and produce structured section-level signals that help the client
LLM (Grok) decide how many rounds of exploration to run and in what order.

If research_digest.md does not yet exist in the research directory, the
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
import json as _json
import logging
import math
import re
import subprocess
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict

from ..config.settings import settings

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Subprocess inference server — infer.py --serve via training venv (has torch)
# ---------------------------------------------------------------------------
# parents[3] = research_agent_local/  (tools is 3 levels below: mcp_server/src/tools/)
_TRAINING_DIR = Path(__file__).resolve().parents[3] / "training"
_TRAINING_PYTHON = _TRAINING_DIR / ".venv" / "bin" / "python"
_INFER_SCRIPT = _TRAINING_DIR / "infer.py"
_INFER_PORT = 8787
_INFER_STARTUP_TIMEOUT = 1800  # seconds — Qwen3-4B NF4 over /mnt/f/ can take >5 min

_infer_proc: subprocess.Popen | None = None
_infer_lock = threading.Lock()

# ---------------------------------------------------------------------------
# Digest generation constants (mirrors generate_digests.py)
# ---------------------------------------------------------------------------
_DIGEST_MODEL = "grok-4-1-fast-reasoning"
_PLANNER_MODEL = "grok-4.20-0309-reasoning"  # Grok 4.2 reasoning — final planning decision
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


# Collects stderr lines from the infer subprocess so the pipe never blocks.
_infer_stderr_lines: list[str] = []
_infer_stderr_lock = threading.Lock()


def _drain_stderr(proc: subprocess.Popen) -> None:
    """Background thread: read stderr line-by-line, log each line, keep last 200."""
    if proc.stderr is None:
        return
    for raw in proc.stderr:
        line = raw.decode(errors="replace").rstrip()
        logger.debug("[infer-server] %s", line)
        with _infer_stderr_lock:
            _infer_stderr_lines.append(line)
            if len(_infer_stderr_lines) > 200:
                _infer_stderr_lines.pop(0)


def _ensure_infer_server() -> str:
    """Start the infer.py HTTP server subprocess if not already running.

    Uses the training venv's Python (which has torch/transformers installed).
    Blocks until the /health endpoint responds or the timeout is reached.
    Returns the server base URL.

    stderr is drained by a background thread to prevent pipe-buffer stalls
    (bitsandbytes / transformers can emit hundreds of KB during model load).
    """
    global _infer_proc
    base_url = f"http://127.0.0.1:{_INFER_PORT}"
    health_url = f"{base_url}/health"

    # Fast path — already running
    if _infer_proc is not None and _infer_proc.poll() is None:
        return base_url

    with _infer_lock:
        # Re-check after acquiring lock
        if _infer_proc is not None and _infer_proc.poll() is None:
            return base_url

        logger.info(
            "Starting infer.py HTTP server (this will load the model — "
            "~5-10 min on first call over /mnt/f/)…"
        )
        with _infer_stderr_lock:
            _infer_stderr_lines.clear()

        _infer_proc = subprocess.Popen(
            [
                str(_TRAINING_PYTHON),
                str(_INFER_SCRIPT),
                "--serve",
                "--port", str(_INFER_PORT),
            ],
            cwd=str(_TRAINING_DIR),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )

        # Drain stderr in a background thread so the pipe buffer never fills.
        _stderr_thread = threading.Thread(
            target=_drain_stderr, args=(_infer_proc,), daemon=True
        )
        _stderr_thread.start()

        # Poll /health until ready or timeout
        deadline = time.monotonic() + _INFER_STARTUP_TIMEOUT
        last_exc: Exception | None = None
        while time.monotonic() < deadline:
            if _infer_proc.poll() is not None:
                with _infer_stderr_lock:
                    stderr = "\n".join(_infer_stderr_lines)
                raise RuntimeError(
                    f"Infer server process exited unexpectedly during startup.\n{stderr}"
                )
            try:
                with urllib.request.urlopen(health_url, timeout=2) as resp:
                    if resp.status == 200:
                        logger.info("Infer server is ready.")
                        return base_url
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
            time.sleep(2)

        with _infer_stderr_lock:
            stderr_tail = "\n".join(_infer_stderr_lines[-40:])
        raise RuntimeError(
            f"Infer server did not become ready within {_INFER_STARTUP_TIMEOUT}s. "
            f"Last error: {last_exc}\n"
            f"Last stderr output:\n{stderr_tail}"
        )


def _call_infer_server(digest: str) -> tuple[int, list[float], list[dict], dict]:
    """Send the digest to the running infer server and return structured results."""
    base_url = _ensure_infer_server()
    payload = _json.dumps({"digest": digest, "verbose": True}).encode()
    req = urllib.request.Request(
        f"{base_url}/predict",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    # Inference can take several minutes for large digests
    with urllib.request.urlopen(req, timeout=600) as resp:
        data = _json.loads(resp.read())
    if "error" in data:
        raise RuntimeError(f"Infer server returned error: {data['error']}")
    preset: int = data["preset"]
    probs: list[float] = data["probs"]
    sections: list[dict] = data.get("sections", [])
    corrections: dict = data.get("corrections", {})
    return preset, probs, sections, corrections


def _entropy(probs: list[float]) -> float:
    """Shannon entropy in bits: H = -∑ p·log₂(p+ε)."""
    eps = 1e-12
    return -sum(p * math.log2(p + eps) for p in probs)


def _extract_gap_profile(digest: str) -> str:
    """
    Extract the '## 3. Overall Gap Profile' section from the exploitation digest.

    Returns the section text, or an empty string if the section is absent
    (e.g. the digest was malformed or not yet generated).
    """
    marker = "## 3. Overall Gap Profile"
    idx = digest.find(marker)
    if idx == -1:
        return ""
    # Take everything from the marker to the next top-level ## heading (if any)
    rest = digest[idx:]
    # Find the next ## heading after the marker itself
    next_heading = rest.find("\n## ", len(marker))
    if next_heading != -1:
        return rest[:next_heading].strip()
    return rest.strip()


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


# ---------------------------------------------------------------------------
# Grok 4.2 final planning call
# ---------------------------------------------------------------------------
_PLANNER_SYSTEM = """\
You are an expert research strategist deciding how many rounds of autonomous web \
exploration to run before writing an article. You will be shown the RL model's \
output, the article guideline, and a coverage gap profile from the exploitation digest.

Your job: make the final exploration-preset decision.

Preset meanings (P0–P5):
  P0 – No exploration   (coverage is already complete)
  P1 – 1 round, balanced
  P2 – 2 rounds: balanced → depth
  P3 – 2 rounds: depth → breadth
  P4 – 3 rounds: balanced → depth → breadth
  P5 – 3 rounds: depth → breadth → depth

Rules:
  1. Begin by explicitly restating the RL model's recommendation and your \
agreement or disagreement.
  2. Use the article guideline to understand topic complexity and intended depth.
  3. Use the gap profile to quantify which sections need more coverage.
  4. Only override the RL model if the article guideline or gap profile provides \
a concrete reason.
  5. Your final output MUST be valid JSON (no prose after the JSON block)."""

_PLANNER_STANDALONE_SYSTEM = """\
You are an expert research strategist deciding how many rounds of autonomous web \
exploration to run before writing an article. You will be shown the article \
guideline and a coverage gap profile from the exploitation digest.

Your job: choose the best exploration preset entirely on your own judgment.

Preset meanings (P0–P5):
  P0 – No exploration   (coverage is already complete)
  P1 – 1 round, balanced
  P2 – 2 rounds: balanced → depth
  P3 – 2 rounds: depth → breadth
  P4 – 3 rounds: balanced → depth → breadth
  P5 – 3 rounds: depth → breadth → depth

Rules:
  1. Use the article guideline to understand topic complexity and intended depth.
  2. Use the gap profile to quantify which sections need more coverage.
  3. Prefer fewer rounds unless the gap profile clearly justifies more.
  4. Your final output MUST be valid JSON (no prose after the JSON block)."""

_PLANNER_STANDALONE_USER_TEMPLATE = """\
## Article Guideline

<article_guideline>
{article_guideline}
</article_guideline>

---

## Coverage Gap Profile (from Exploitation Digest)

<gap_profile>
{digest_gap_profile}
</gap_profile>

---

## Task

Based solely on the article guideline and the coverage gap profile above, \
choose the best exploration preset. Output ONLY the following JSON block \
(no additional prose after it):

```json
{{
  "preset": <integer 0-5>,
  "name": "<preset_name>",
  "reasoning": "<2-4 sentences: which evidence drove your final decision>"
}}
```"""

_PLANNER_USER_TEMPLATE = """\
## RL Model Output

Aggregate recommendation: P{preset} — {name}
Confidence: {confidence:.0%} | Entropy: {entropy:.2f} bits
Floor correction applied: {floor_applied}
RL guidance: {guidance}

### Per-Section Signals
{section_table}

---

## Article Guideline

<article_guideline>
{article_guideline}
</article_guideline>

---

## Coverage Gap Profile (from Exploitation Digest)

<gap_profile>
{digest_gap_profile}
</gap_profile>

---

## Task

First, explicitly state whether you agree with the RL model's recommendation \
of P{preset} and why (1-2 sentences). Then output ONLY the following JSON block \
(no additional prose after it):

```json
{{
  "preset": <integer 0-5>,
  "name": "<preset_name>",
  "reasoning": "<2-4 sentences: which evidence drove your final decision>",
  "override": <true|false>,
  "override_reason": "<why you deviated from the RL model, or null if you agree>"
}}
```"""


async def _call_grok_planner(
    api_key: str,
    base_url: str,
    rl_preset: int,
    rl_confidence: float,
    rl_entropy: float,
    floor_applied: bool,
    guidance: str,
    section_signals: list[dict],
    article_guideline: str,
    digest_gap_profile: str,
) -> dict:
    """Call Grok 4.2 to produce the final exploration-preset decision.

    Grok sees the RL model's full output (aggregate recommendation, per-section
    signals, confidence, entropy) together with the article guideline and the
    structured gap profile extracted from the exploitation digest.

    Returns a dict with keys: preset, name, reasoning, override, override_reason.
    Falls back to the RL recommendation on any parsing failure.
    """
    from openai import AsyncOpenAI  # noqa: PLC0415

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    section_table = "\n".join(
        f"  {i + 1}. [{s['title']}]  P{s['preset']} ({s['name']})  top2={s['top2']}"
        for i, s in enumerate(section_signals)
    ) or "  (no section signals)"

    user_msg = _PLANNER_USER_TEMPLATE.format(
        preset=rl_preset,
        name=_PRESET_NAMES[rl_preset].replace("_", " "),
        confidence=rl_confidence,
        entropy=rl_entropy,
        floor_applied=floor_applied,
        guidance=guidance,
        section_table=section_table,
        article_guideline=article_guideline or "(not available)",
        digest_gap_profile=digest_gap_profile or "(not available)",
    )

    response = await client.chat.completions.create(
        model=_PLANNER_MODEL,
        messages=[
            {"role": "system", "content": _PLANNER_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        max_tokens=4096,
    )
    raw = (response.choices[0].message.content or "").strip()

    # Extract JSON — fenced code block first, then bare object
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    json_str = m.group(1) if m else ""
    if not json_str:
        m = re.search(r"\{[^{}]*\}", raw, re.DOTALL)
        json_str = m.group(0) if m else ""

    try:
        parsed = _json.loads(json_str)
        parsed_preset = int(parsed["preset"])
        if parsed_preset not in range(_NUM_PRESETS):
            raise ValueError(f"preset {parsed_preset} out of range 0-{_NUM_PRESETS - 1}")
        return {
            "preset": parsed_preset,
            "name": _PRESET_NAMES[parsed_preset].replace("_", " "),
            "reasoning": parsed.get("reasoning", ""),
            "override": bool(parsed.get("override", parsed_preset != rl_preset)),
            "override_reason": parsed.get("override_reason"),
        }
    except Exception:
        logger.warning(
            "Grok planner response could not be parsed as JSON; "
            "defaulting to RL recommendation. raw=%s", raw[:300]
        )
        return {
            "preset": rl_preset,
            "name": _PRESET_NAMES[rl_preset].replace("_", " "),
            "reasoning": "JSON parsing failed; using RL model recommendation.",
            "override": False,
            "override_reason": None,
        }


async def _call_grok_planner_standalone(
    api_key: str,
    base_url: str,
    article_guideline: str,
    digest_gap_profile: str,
) -> dict:
    """Call Grok 4.2 to make an exploration-preset decision with NO RL signals.

    Used for the Grok-alone baseline: Grok sees only the article guideline and
    the structured gap profile, making its decision independently of any
    Qwen3-4B output. Comparing this result to the full RL+Grok pipeline shows
    how much value the RL section-level signals add.

    Returns a dict with keys: preset, name, reasoning.
    """
    from openai import AsyncOpenAI  # noqa: PLC0415

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    user_msg = _PLANNER_STANDALONE_USER_TEMPLATE.format(
        article_guideline=article_guideline or "(not available)",
        digest_gap_profile=digest_gap_profile or "(not available)",
    )

    response = await client.chat.completions.create(
        model=_PLANNER_MODEL,
        messages=[
            {"role": "system", "content": _PLANNER_STANDALONE_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        max_tokens=4096,
    )
    raw = (response.choices[0].message.content or "").strip()

    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    json_str = m.group(1) if m else ""
    if not json_str:
        m = re.search(r"\{[^{}]*\}", raw, re.DOTALL)
        json_str = m.group(0) if m else ""

    try:
        parsed = _json.loads(json_str)
        parsed_preset = int(parsed["preset"])
        if parsed_preset not in range(_NUM_PRESETS):
            raise ValueError(f"preset {parsed_preset} out of range 0-{_NUM_PRESETS - 1}")
        return {
            "preset": parsed_preset,
            "name": _PRESET_NAMES[parsed_preset].replace("_", " "),
            "reasoning": parsed.get("reasoning", ""),
        }
    except Exception:
        logger.warning(
            "Grok standalone planner response could not be parsed as JSON. raw=%s", raw[:300]
        )
        return None


async def predict_exploration_preset_tool(research_directory: str, grok_only: bool = False) -> Dict[str, Any]:
    """
    Predict the optimal exploration preset for an article using the trained RL model.

    Reads (or auto-generates) research_digest.md from the research directory,
    runs per-section inference through the GRPO-trained Qwen3-4B + LoRA model,
    and returns structured signals to help the client LLM decide how many rounds
    of exploration to run and in what order.

    If research_digest.md does not yet exist in the research directory, the tool
    generates it on-the-fly via a 4-stage pipeline (COLLECT→COMPRESS→ASSEMBLE→GENERATE)
    using the XAI API and writes it to research_digest.md before running inference.
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
          - research_digest.md (pre-existing, used directly), or
          - article_guideline.md + .research/ subfolder (digest auto-generated).
        grok_only: When True, skip the RL inference stage entirely and call Grok 4.2
          with only the article guideline + coverage gap profile (no section-level
          RL signals). Use this for the Grok-alone baseline to measure the RL
          model's marginal contribution. rl_recommendation will be None in the result.

    Returns:
        Dict with keys:
          status               – "success" or "error"
          digest_generated     – True if the digest was generated on-the-fly
          rl_recommendation    – aggregate preset, name, confidence, entropy,
                                 floor_correction_applied. None when grok_only=True.
          section_signals      – per-section list of preset, name, top2 probs.
                                 Empty list when grok_only=True.
          guidance             – one-sentence synthesis for the client LLM.
                                 Empty string when grok_only=True.
          article_guideline    – full text of article_guideline.md
          digest_gap_profile   – "## 3. Overall Gap Profile" section from the digest
          grok_recommendation  – Grok 4.2's planning decision. When grok_only=False:
                                 preset, name, reasoning, override, override_reason.
                                 When grok_only=True: preset, name, reasoning (no
                                 override fields — RL had no input to override).
                                 None if XAI_API_KEY is unset or the call fails.
          message              – human-readable summary
    """
    research_path = Path(research_directory)
    digest_path = research_path / "research_digest.md"

    if not research_path.exists():
        return {
            "status": "error",
            "message": f"Research directory not found: {research_directory}",
        }

    digest_generated = False

    if not digest_path.exists():
        logger.info(f"research_digest.md not found — generating on-the-fly for {research_directory}")
        if settings.xai_api_key is None:
            return {
                "status": "error",
                "message": (
                    "research_digest.md not found and XAI_API_KEY is not configured. "
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

    guideline_path = research_path / "article_guideline.md"
    article_guideline = (
        guideline_path.read_text(encoding="utf-8", errors="replace")
        if guideline_path.exists()
        else ""
    )
    digest_gap_profile = _extract_gap_profile(digest)

    # -----------------------------------------------------------------------
    # Branch: Grok-alone baseline (no RL inference)
    # -----------------------------------------------------------------------
    if grok_only:
        grok_recommendation: dict | None = None
        if settings.xai_api_key is not None:
            try:
                grok_recommendation = await _call_grok_planner_standalone(
                    api_key=settings.xai_api_key.get_secret_value(),
                    base_url="https://api.x.ai/v1",
                    article_guideline=article_guideline,
                    digest_gap_profile=digest_gap_profile,
                )
                if grok_recommendation:
                    logger.info("Grok standalone chose P%d", grok_recommendation["preset"])
            except Exception:
                logger.warning("Grok standalone planner call failed.")
        else:
            logger.warning("XAI_API_KEY not set; cannot run Grok standalone planner.")

        grok_preset = grok_recommendation["preset"] if grok_recommendation else "?"
        return {
            "status": "success",
            "digest_generated": digest_generated,
            "rl_recommendation": None,
            "section_signals": [],
            "guidance": "",
            "grok_recommendation": grok_recommendation,
            "article_guideline": article_guideline,
            "digest_gap_profile": digest_gap_profile,
            "message": (
                f"Grok standalone (no RL) chose preset P{grok_preset}."
                if grok_recommendation
                else "Grok standalone call failed or XAI_API_KEY not set."
            ),
        }

    # -----------------------------------------------------------------------
    # Standard pipeline: RL inference → Grok 4.2
    # -----------------------------------------------------------------------
    try:
        loop = asyncio.get_running_loop()
        preset, agg_probs, section_details, meta = await loop.run_in_executor(
            None, _call_infer_server, digest
        )
    except Exception as exc:
        logger.exception("RL inference failed")
        return {"status": "error", "message": f"RL inference failed: {exc}"}

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

    grok_recommendation = None
    if settings.xai_api_key is not None:
        try:
            grok_recommendation = await _call_grok_planner(
                api_key=settings.xai_api_key.get_secret_value(),
                base_url="https://api.x.ai/v1",
                rl_preset=preset,
                rl_confidence=confidence,
                rl_entropy=h,
                floor_applied=floor_applied,
                guidance=guidance_str,
                section_signals=section_signals,
                article_guideline=article_guideline,
                digest_gap_profile=digest_gap_profile,
            )
            logger.info(
                "Grok planner chose P%d (override=%s)",
                grok_recommendation["preset"],
                grok_recommendation["override"],
            )
        except Exception:
            logger.warning("Grok planner call failed; falling back to RL recommendation.")
    else:
        logger.warning("XAI_API_KEY not set; skipping Grok 4.2 planner call.")

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
        "grok_recommendation": grok_recommendation,
        "article_guideline": article_guideline,
        "digest_gap_profile": digest_gap_profile,
        "message": (
            f"RL model recommends preset P{preset} "
            f"({_PRESET_NAMES[preset].replace('_', ' ')}) "
            f"with {confidence:.0%} confidence across {len(section_signals)} sections. "
            f"Entropy: {h:.2f} bits."
        ),
    }
    return result
