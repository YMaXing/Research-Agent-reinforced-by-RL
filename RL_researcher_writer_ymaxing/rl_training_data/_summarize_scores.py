import json, pathlib, statistics
from collections import defaultdict

ep_dir = pathlib.Path(__file__).parent / "episodes"
files = sorted(ep_dir.glob("*/scores.json"))

by_article = defaultdict(list)
for f in files:
    ep = f.parent.name
    if "_Old" in ep:
        continue
    article = ep.rsplit("__preset", 1)[0]
    scores = json.loads(f.read_text())
    by_article[article].append(scores)

keys = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_structure",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
    "user_intent_golden_source_priority",
]
short = {
    "ground_truth_core_content": "core_content",
    "ground_truth_flow": "flow",
    "ground_truth_structure": "structure",
    "ground_truth_depth_enhancement": "depth_enh",
    "ground_truth_breadth_enhancement": "breadth_enh",
    "ground_truth_core_preservation": "core_pres",
    "user_intent_guideline_adherence": "guideline",
    "user_intent_research_anchoring": "research_anc",
    "user_intent_golden_source_priority": "golden_src",
}

all_scores = defaultdict(list)
for article in sorted(by_article):
    group = by_article[article]
    print(f"--- {article} (n={len(group)}) ---")
    for k in keys:
        vals = [s[k] for s in group if k in s]
        all_scores[k].extend(vals)
        print(f"  {short[k]:20s}  mean={statistics.mean(vals):.3f}  min={min(vals):.3f}  max={max(vals):.3f}")
    print()

total_eps = sum(len(v) for v in by_article.values())
print(f"=== OVERALL (n={total_eps} episodes, {len(files)} scores.json files total) ===")
for k in keys:
    vals = all_scores[k]
    print(f"  {short[k]:20s}  mean={statistics.mean(vals):.3f}  min={min(vals):.3f}  max={max(vals):.3f}")
