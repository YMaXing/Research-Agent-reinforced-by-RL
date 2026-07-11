"""PROTOTYPE (Phase 1) — corpus-answer-coverage feature.

Standalone, does NOT touch the digest pipeline. For each article it:
  1. collect_sources()  -> all 5 scraped buckets (golden_web/youtube/code/local + exploitation)
  2. _extract_all_anchors() -> the guideline's specific demand anchors (with the
     structural-anchor filter already applied)
  3. For EACH source (full text, temperature=0) asks which anchors that source
     *substantively answers* (not merely mentions).
  4. Aggregates via OR across all sources: an anchor is "answered" if >=1 source
     answers it. answer_coverage = n_answered / n_anchors (per section + article).

Emits a per-article JSON to /tmp/answer_cov/<article>.json and prints a summary
line. Also records the current need_depth/need_breadth from the on-disk digest so
Phase-2 can test augment-vs-replace (marginal information of need over coverage).

Usage:
  python _proto_answer_coverage.py <article1> <article2> ...
  python _proto_answer_coverage.py --repeat 3 <article>   # noise check
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_digests as gd  # noqa: E402
import _digest_parse  # noqa: E402

_OUT_DIR = Path("/tmp/answer_cov")
_OUT_DIR.mkdir(parents=True, exist_ok=True)

# Only these full-text scraped buckets are judged (Tavily snippets excluded on
# purpose — prospective/low-fidelity; a "mention" in a snippet must not count as
# "answered"). This is exactly the set of golden + exploitation-guideline sources
# available on disk at workflow step 3.4 (digest/preset decision time).
_SOURCE_BUCKETS = ("golden_web", "golden_youtube", "golden_code", "golden_local", "exploitation")

_ANSWER_SYSTEM = (
    "You judge whether a single research source substantively answers specific "
    "content demands of an article. Output only JSON."
)

_ANSWER_USER_TEMPLATE = """\
Article: "{article_title}"

Below is ONE research source, followed by a numbered list of specific CONTENT DEMANDS
(anchors) taken verbatim from the article's writing guideline.

Decide, for each demand, whether THIS source *substantively answers* it.

"Substantively answers" means: the source contains the specific facts, explanation,
data, quote, or evidence that a writer would need to satisfy this demand WITHOUT any
further web research — either fully, or enough that only trivial confirmation remains.

Do NOT count a demand as answered if the source merely mentions the topic in passing,
is tangentially related, or would still require the writer to go find the actual
content elsewhere. Be strict: when in doubt, mark it NOT answered.

<source filename="{filename}" type="{source_type}">
{content}
</source>

CONTENT DEMANDS:
{anchor_list}

Return ONLY this JSON (no prose):
{{"answered_anchor_ids": ["a3", "a7", ...]}}
Include an id ONLY if this source substantively answers that demand.
"""


async def _judge_source(
    client, semaphore, article_title, filename, source_type, content, anchors
):
    """Return the set of anchor ids this source substantively answers."""
    if len(content) > gd._MAX_SOURCE_CHARS:
        content = content[: gd._MAX_SOURCE_CHARS] + "\n\n[...content truncated...]"
    anchor_list = "\n".join(f'  {a["id"]}: {a["anchor"]}' for a in anchors)
    async with semaphore:
        try:
            resp = await client.chat.completions.create(
                model=gd.MODEL,
                messages=[
                    {"role": "system", "content": _ANSWER_SYSTEM},
                    {
                        "role": "user",
                        "content": _ANSWER_USER_TEMPLATE.format(
                            article_title=article_title,
                            filename=filename,
                            source_type=source_type,
                            content=content,
                            anchor_list=anchor_list,
                        ),
                    },
                ],
                max_tokens=2048,
                temperature=0,
                response_format={"type": "json_object"},
            )
            raw = (resp.choices[0].message.content or "").strip()
            parsed = json.loads(raw)
            ids = parsed.get("answered_anchor_ids", []) or []
            valid = {a["id"] for a in anchors}
            return {i for i in ids if i in valid}
        except Exception as e:  # noqa: BLE001
            print(f"    [warn] judge failed for {filename}: {e}", flush=True)
            return set()


async def compute_article(client, article: str) -> dict:
    base_dir = gd._BASES_DIR / article
    title = gd.ARTICLES.get(article) or gd._derive_article_title(base_dir)
    sources = gd.collect_sources(base_dir)

    # Anchors (structural-anchor filter already applied inside _extract_all_anchors)
    raw_anchors = gd._extract_all_anchors(sources["guideline"])
    anchors = []
    for idx, a in enumerate(raw_anchors, 1):
        anchors.append({"id": f"a{idx}", "anchor": a["anchor"], "section_id": a["section_id"]})
    if not anchors:
        return {"article": article, "error": "no anchors"}

    # All full-text sources across the 5 buckets
    src_items: list[tuple[str, str, str]] = []  # (source_type, filename, content)
    for st in _SOURCE_BUCKETS:
        for fname, content in sources.get(st, {}).items():
            src_items.append((st, fname, content))

    semaphore = asyncio.Semaphore(5)
    tasks = [
        _judge_source(client, semaphore, title, fname, st, content, anchors)
        for (st, fname, content) in src_items
    ]
    results = await asyncio.gather(*tasks) if tasks else []

    answered: set[str] = set()
    for r in results:
        answered |= r

    # Per-section + per-article coverage
    by_sec: dict[str, list[str]] = {}
    for a in anchors:
        by_sec.setdefault(a["section_id"], []).append(a["id"])
    sec_cov = {}
    for sid, ids in by_sec.items():
        n_ans = sum(1 for i in ids if i in answered)
        sec_cov[sid] = {"n_anchors": len(ids), "n_answered": n_ans,
                        "coverage": round(n_ans / len(ids), 3)}

    n_anchors = len(anchors)
    n_answered = len(answered)
    coverage = round(n_answered / n_anchors, 3)

    # Record current on-disk need_depth/need_breadth + oracle for Phase-2 analysis
    need_d = need_b = None
    digest_path = base_dir / "research_digest.md"
    if digest_path.exists():
        try:
            d = _digest_parse.parse_digest(digest_path.read_text(encoding="utf-8"))
            need_d = sum(g.get("need_depth", 0) for g in d["gap_rows"].values())
            need_b = sum(g.get("need_breadth", 0) for g in d["gap_rows"].values())
        except Exception:
            pass
    oracle = None
    orc_path = base_dir / "article_oracle.json"
    if orc_path.exists():
        try:
            o = json.load(open(orc_path, encoding="utf-8"))
            oracle = {"arm": o.get("oracle_arm"), "arm_idx": o.get("oracle_arm_idx")}
        except Exception:
            pass

    out = {
        "article": article,
        "n_sources": len(src_items),
        "n_anchors": n_anchors,
        "n_answered": n_answered,
        "answer_coverage": coverage,
        "need_depth": need_d,
        "need_breadth": need_b,
        "oracle": oracle,
        "section_coverage": sec_cov,
    }
    (_OUT_DIR / f"{article}.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    orc_s = f"{oracle['arm']}({oracle['arm_idx']})" if oracle else "?"
    print(
        f"{article:32s} n_src={len(src_items):2d} n_anchors={n_anchors:3d} "
        f"answered={n_answered:3d} coverage={coverage:.2f}  "
        f"need_d={need_d} need_b={need_b}  oracle={orc_s}",
        flush=True,
    )
    return out


async def main(articles: list[str], repeat: int):
    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=gd._XAI_API_KEY, base_url=gd._XAI_BASE_URL)
    if repeat > 1:
        art = articles[0]
        print(f"NOISE CHECK: {art} x{repeat}")
        covs = []
        for r in range(repeat):
            out = await compute_article(client, art)
            covs.append(out.get("answer_coverage"))
        print(f"  coverage across {repeat} runs: {covs}  range={max(covs)-min(covs):.3f}")
    else:
        for art in articles:
            await compute_article(client, art)
    await client.close()
    print("PROTO_DONE")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("articles", nargs="+")
    ap.add_argument("--repeat", type=int, default=1)
    args = ap.parse_args()
    asyncio.run(main(args.articles, args.repeat))
