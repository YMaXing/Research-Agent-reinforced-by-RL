"""PROTOTYPE (read-only, small-sample): test embedding-distance novelty as a
candidate section-level reward dimension.

Motivation: run13_rl_grok_pipeline_analysis.md Part 5 -- every deterministic
surface-marker candidate tried so far (raw citations, marginal citations,
numeric-claim counts, analytical-connector density) either fails at the
standard/deep boundary or fails outright at section granularity (marginal
citations: 42%/33% positive at light->standard/standard->deep, i.e. worse than
a coin flip). This tests a semantic alternative: embed each arm's rendering of
a section and the skip-arm's rendering of the SAME section, and measure cosine
distance. Unlike citation-position matching, this doesn't depend on WHICH
section a source got cited in -- it directly measures whether the section's
CONTENT differs, which should be robust to the "source landed in the wrong
section" misattribution problem that broke the citation-count candidate.

Scope: originally piloted on 4 articles (~140 embedding calls); the 4-article
pilot showed 100% positive at skip->light, a clean null at light->standard
(45%), and a preliminary, borderline-significant positive signal at
standard->deep (66%, n=29 sections) -- the first candidate of any kind (citations,
numeric claims, connector density) to show a non-reversed signal at that
specific boundary. This run SCALES UP to the full original 40-article corpus
(24 TRAIN variants + 16 TEST no-variant articles -- explicitly excludes the 2
__mixeddepth augmented pilots, which are not part of the original corpus) to
check whether that boundary-specific signal survives a much larger sample
(~2300 embedding calls total, ~578 sections x 4 arms). Embedding calls are ~2
orders of magnitude cheaper than LLM grading calls, but this is still real API
cost at this scale -- run only with explicit go-ahead.

Requires GOOGLE_API_KEY (reads from writing_workflow/.env). Uses the
top-level .venv (numpy/sklearn/google-genai already installed there).

Usage (from research_agent_local/, using the top-level .venv's python):
  ../../.venv/bin/python3 training/_proto_embedding_novelty.py
"""

from __future__ import annotations

import os
import re
import statistics
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import generate_episode_oracles as geo  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent
_ENV_PATH = _REPO_ROOT / "writing_workflow" / ".env"

ARMS = geo._ARM_ORDER

# The original 40 production articles (24 TRAIN variants + 16 TEST no-variant) --
# explicitly excludes the 2 __mixeddepth augmented pilots (Insects_Consciousness__mixeddepth,
# Distinct_AI_Models__mixeddepth), which are NOT part of the original corpus.
_TRAIN_BASE_ARTICLES = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "10_memory_knowledge_access",
    "11_multimodal",
]
_TRAIN_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
_TEST_ARTICLES = [
    "04_structured_outputs",
    "07_reasoning_planning",
    "13_agent_framework",
    "14_agent_system_design",
    "29_evaluation_metrics",
    "31_CI",
    "Bird_Eye_Extreme",
    "Dark_Dimension",
    "Distinct_AI_Models",
    "Earth_Oceans_Origin",
    "Gravity_Entropy",
    "HNSW",
    "Insects_Consciousness",
    "Space-Time_QECC",
    "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
]
_ARTICLES = [f"{base}__{v}" for base in _TRAIN_BASE_ARTICLES for v in _TRAIN_VARIANTS] + _TEST_ARTICLES
assert len(_ARTICLES) == 40, f"expected 40 articles, got {len(_ARTICLES)}"

_HEADER_RE = re.compile(r"^## (.+)$", re.MULTILINE)
_REFERENCES_RE = re.compile(r"^## References\b", re.MULTILINE)


def _load_google_api_key() -> str:
    """Read GOOGLE_API_KEY from writing_workflow/.env without executing the file."""
    if os.environ.get("GOOGLE_API_KEY"):
        return os.environ["GOOGLE_API_KEY"]
    text = _ENV_PATH.read_text(encoding="utf-8")
    m = re.search(r"^GOOGLE_API_KEY=(.+)$", text, re.MULTILINE)
    if not m:
        raise RuntimeError(f"GOOGLE_API_KEY not found in {_ENV_PATH}")
    return m.group(1).strip().strip('"').strip("'")


def _split_sections(text: str) -> list[tuple[str, str]]:
    """Split article.md by level-2 '## ' headers, excluding References onward."""
    text = _REFERENCES_RE.split(text, maxsplit=1)[0]
    parts = _HEADER_RE.split(text)
    out: list[tuple[str, str]] = []
    for i in range(1, len(parts), 2):
        body = parts[i + 1] if i + 1 < len(parts) else ""
        out.append((parts[i].strip(), body.strip()))
    return out


def _article_dir_and_presets(article: str) -> tuple[Path, dict[str, list[int]]]:
    no_variant = "__var_" not in article
    root = geo._TEST_EPISODES_DIR if no_variant else geo._EPISODES_DIR
    presets = geo._TEST_ARM_PRESETS if no_variant else geo._ARM_PRESETS
    return root, presets


def main() -> None:
    api_key = _load_google_api_key()
    from google import genai  # noqa: PLC0415 -- deferred import, only needed if key load succeeds

    client = genai.Client(api_key=api_key)

    # --- Collect all (article, section_idx, arm) -> body text pairs needing embeddings ---
    all_bodies: dict[tuple[str, int, str], str] = {}
    section_titles: dict[tuple[str, int], str] = {}
    for article in _ARTICLES:
        root, presets = _article_dir_and_presets(article)
        texts: dict[str, str] = {}
        ok = True
        for arm in ARMS:
            p = presets[arm][0]
            f = root / f"{article}__preset{p}" / "article.md"
            if not f.exists():
                print(f"  MISSING: {f}")
                ok = False
                break
            texts[arm] = f.read_text(encoding="utf-8", errors="replace")
        if not ok:
            continue
        skip_secs = _split_sections(texts["skip"])
        skip_by_norm = {geo._normalize(t): b for t, b in skip_secs}
        for si, (title, _body) in enumerate(skip_secs):
            norm = geo._normalize(title)
            section_titles[(article, si)] = title
            for arm in ARMS:
                arm_secs = _split_sections(texts[arm])
                arm_by_norm = {geo._normalize(t): b for t, b in arm_secs}
                body = arm_by_norm.get(norm)
                if body is None and si < len(arm_secs):
                    body = arm_secs[si][1]
                all_bodies[(article, si, arm)] = body or ""

    print(f"Collected {len(all_bodies)} (article, section, arm) bodies needing embeddings.")

    # --- Embed everything (batched, one call per text -- gemini-embedding-001 has no
    # batch endpoint in the basic client API, so this is len(all_bodies) calls) ---
    embeddings: dict[tuple[str, int, str], list[float]] = {}
    keys = sorted(all_bodies.keys())
    for i, key in enumerate(keys):
        text = all_bodies[key][:8000]  # safety truncation, well within embedding model limits
        if not text.strip():
            embeddings[key] = None
            continue
        try:
            result = client.models.embed_content(model="gemini-embedding-001", contents=[text])
            embeddings[key] = list(result.embeddings[0].values)
        except Exception as exc:  # noqa: BLE001
            print(f"  EMBED FAILED for {key}: {exc}")
            embeddings[key] = None
        if (i + 1) % 100 == 0:
            print(f"  ...{i + 1}/{len(keys)} embedded", flush=True)

    print(f"Done embedding. {sum(1 for v in embeddings.values() if v is not None)}/{len(keys)} succeeded.")

    # --- Cosine distance vs skip's embedding, per (article, section, arm) ---
    def cosine_sim(a: list[float], b: list[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        na = sum(x * x for x in a) ** 0.5
        nb = sum(y * y for y in b) ** 0.5
        if na == 0 or nb == 0:
            return 1.0
        return dot / (na * nb)

    novelty: dict[tuple[str, int, str], float] = {}
    for article in _ARTICLES:
        for (a2, si, arm), emb in embeddings.items():
            if a2 != article:
                continue
            skip_emb = embeddings.get((article, si, "skip"))
            if emb is None or skip_emb is None:
                continue
            novelty[(article, si, arm)] = 1.0 - cosine_sim(skip_emb, emb)

    print()
    print("=" * 100)
    print("EMBEDDING-DISTANCE NOVELTY (1 - cosine_sim vs matched skip section)")
    print("=" * 100)
    for arm in ARMS:
        vals = [v for (a2, si, a3), v in novelty.items() if a3 == arm]
        if not vals:
            continue
        print(f"  {arm:<10} n={len(vals):<4} mean={statistics.mean(vals):.4f}  median={statistics.median(vals):.4f}")

    print()
    print("Adjacent-arm per-section gaps (SAME section, matched):")
    rows = []
    for article in _ARTICLES:
        n_secs = len({si for (a2, si, _a3) in novelty if a2 == article})
        for si in range(n_secs):
            row = {arm: novelty.get((article, si, arm)) for arm in ARMS}
            if all(v is not None for v in row.values()):
                rows.append(row)
    for i in range(3):
        a, b = ARMS[i], ARMS[i + 1]
        d = [r[b] - r[a] for r in rows]
        if not d:
            continue
        n_pos = sum(1 for v in d if v > 0)
        print(f"  {a}->{b}: mean=+{statistics.mean(d):.4f}  median=+{statistics.median(d):.4f}  "
              f"n_pos={n_pos}/{len(d)} ({100 * n_pos / len(d):.0f}%)")

    print()
    print(f"(n={len(rows)} fully-matched sections across {len(_ARTICLES)} articles)")


if __name__ == "__main__":
    main()
