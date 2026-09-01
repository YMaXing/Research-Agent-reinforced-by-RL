"""Re-classify external_evidence_policy ONLY (Stage 2c), skipping the
expensive COMPRESS/GENERATE stages -- for the A.20 Scenario-C redesign.

Updates BOTH copies of the field so they can't drift apart:
  - bases/<article>/guideline_features.json          (read by compute_article_oracle.py)
  - bases/<article>/research_digest.md <digest_meta>  (read by preset_planner_handler.py
    via _digest_parse.parse_digest_meta() -- the real inference path)

Per-section numeric features (target_words/mandatory_bullets/...) are also
refreshed as a side effect of the same Stage-2c call, but those aren't what
this pass is about; only external_evidence_policy is diffed/printed.

Usage (from research_agent_local/):
    uv run --project training python training/regen_policy_features.py --articles 02_workflows_vs_agents__var_minimal
    uv run --project training python training/regen_policy_features.py --all
    uv run --project training python training/regen_policy_features.py --all --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

_INFER_SERVICE_DIR = Path(__file__).resolve().parent.parent / "rl_inference_service"
if str(_INFER_SERVICE_DIR) not in sys.path:
    sys.path.insert(0, str(_INFER_SERVICE_DIR))
import generate_digests as gd  # noqa: E402
import guarded_constant_baseline as gcb

ALL_ARTICLES: list[str] = gcb.TRAIN_ARTICLES + gcb.TEST_ARTICLES


async def _regen_one(client, article: str, dry_run: bool) -> tuple[str, str, str]:
    base_dir = gd._BASES_DIR / article
    guideline_path = base_dir / "article_guideline.md"
    digest_path = base_dir / "research_digest.md"
    features_path = base_dir / "guideline_features.json"

    guideline = guideline_path.read_text(encoding="utf-8", errors="replace")
    content_sections = gd._extract_content_sections(guideline)
    article_title = gd.ARTICLES.get(article) or gd._derive_article_title(base_dir)

    old_policy = "N/A"
    if features_path.exists():
        old_policy = json.loads(features_path.read_text(encoding="utf-8")).get(
            "external_evidence_policy", "N/A"
        )

    features = await gd.extract_guideline_features(
        client, article_title, guideline, content_sections, dry_run=False
    )
    new_policy = features["external_evidence_policy"]

    if not dry_run:
        features_path.write_text(json.dumps(features, indent=2), encoding="utf-8")
        if digest_path.exists():
            digest = digest_path.read_text(encoding="utf-8")
            digest = gd._inject_external_evidence_policy(digest, new_policy)
            digest_path.write_text(digest, encoding="utf-8")

    return article, old_policy, new_policy


async def main(articles: list[str], dry_run: bool) -> None:
    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=gd._XAI_API_KEY, base_url=gd._XAI_BASE_URL)
    try:
        changed = []
        for article in articles:
            old, new = (await _regen_one(client, article, dry_run))[1:]
            flag = "  <<< CHANGED" if old != new else ""
            print(f"{article:45s} {old:10s} -> {new:10s}{flag}")
            if old != new:
                changed.append((article, old, new))
    finally:
        await client.close()

    print(f"\n{len(changed)} article(s) changed policy:")
    for article, old, new in changed:
        print(f"  {article}: {old} -> {new}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--articles", nargs="+", metavar="ARTICLE")
    parser.add_argument("--all", action="store_true", help="all 40 official TRAIN+TEST articles")
    parser.add_argument("--dry-run", action="store_true", help="classify only, write nothing")
    args = parser.parse_args()

    if args.all:
        targets = ALL_ARTICLES
    elif args.articles:
        targets = args.articles
    else:
        parser.error("pass --articles ART1 ART2 ... or --all")

    asyncio.run(main(targets, args.dry_run))
