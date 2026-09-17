"""Check whether real exploration-effort data (actual query/scrape counts per
arm's real episode) supports replacing the flat ordinal `nr` (0/1/2/3) cost
driver with an empirically-measured one, BEFORE picking any new cost_coef by
a normative/global sweep.

Motivation: `cost = cost_coef * nr` currently assumes light/standard/deep cost
exactly 1x/2x/3x a fixed unit. But each arm maps to a REAL, separately-run
episode directory (see generate_episode_oracles.py's _ARM_PRESETS /
_TEST_ARM_PRESETS) with its own recorded `.research/full_queries.md` and
`url_phases.json` -- i.e. we already have the ACTUAL exploration-phase query
and scrape counts the agent used for every arm of every one of the 42
articles. If actual effort scales roughly linearly with nr, the flat
assumption is fine and any cost_coef fix is unavoidably a normative choice of
scale. If actual effort deviates substantially (e.g. "deep" barely explores
more than "standard" for some topics, or explores far more for others), that
is real per-article signal we can fold into the cost term directly, instead
of a single global constant.

Exploitation phases are constant across arms (see rl_training_data's
_count_tool_calls.py docstring/note) -- only EXPLORATION query/scrape counts
can differ between skip/light/standard/deep, so this script focuses on those.

Usage (from research_agent_local/training/):
  python3 analyze_empirical_cost.py
"""

from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))

import generate_episode_oracles as geo

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent.parent
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"

_TRAIN_TOPICS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access", "11_multimodal",
]
_TRAIN_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
_TEST_ARTICLES = [
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI", "Bird_Eye_Extreme",
    "Dark_Dimension", "Distinct_AI_Models", "Earth_Oceans_Origin", "Gravity_Entropy",
    "HNSW", "Insects_Consciousness", "Space-Time_QECC", "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
]
_MIXEDDEPTH = ["Distinct_AI_Models__mixeddepth", "Insects_Consciousness__mixeddepth"]
_ALL_42 = [f"{t}__{v}" for t in _TRAIN_TOPICS for v in _TRAIN_VARIANTS] + _TEST_ARTICLES + _MIXEDDEPTH

_ARM_ORDER = geo._ARM_ORDER  # ["skip", "light", "standard", "deep"]
_ARM_ROUNDS = geo._ARM_ROUNDS  # {"skip":0,"light":1,"standard":2,"deep":3}

# 9 genuinely reward-determined "cost-suppressed" articles found in the prior
# diagnostic (analyze_cost_imbalance.py + hard-constraint filtering).
_ACTIONABLE_9 = [
    "05_workflow_patterns__var_standard", "06_tools__var_standard", "06_tools__var_demanding",
    "09_RAG__var_standard", "10_memory_knowledge_access__var_demanding",
    "11_multimodal__var_standard", "04_structured_outputs", "07_reasoning_planning",
    "Earth_Oceans_Origin",
]


def _count_episode(ep_dir: Path) -> dict:
    research = ep_dir / ".research"
    explore_rounds = len(list(research.glob("_explore_round_*.done")))
    exploit_rounds = len(list(research.glob("_exploit_round_*.done")))

    fq = research / "full_queries.md"
    explore_queries = exploit_queries = 0
    if fq.exists():
        text = fq.read_text(encoding="utf-8", errors="replace")
        explore_queries = len(re.findall(r"\[Exploration\]", text))
        exploit_queries = len(re.findall(r"\[Exploitation\]", text))

    up = research / "url_phases.json"
    explore_scrapes = exploit_scrapes = 0
    if up.exists():
        try:
            phases = json.loads(up.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            phases = {}
        for tag in phases.values():
            s = str(tag)
            if "[EXPLORATION]" in s:
                explore_scrapes += 1
            elif "[EXPLOITATION]" in s:
                exploit_scrapes += 1

    return {
        "explore_rounds": explore_rounds, "exploit_rounds": exploit_rounds,
        "explore_queries": explore_queries, "exploit_queries": exploit_queries,
        "explore_scrapes": explore_scrapes, "exploit_scrapes": exploit_scrapes,
        "explore_effort": explore_queries + explore_scrapes,
    }


def _ep_dir_for(article: str, arm: str) -> Path | None:
    is_var = "__var_" in article
    if is_var:
        preset = geo._ARM_PRESETS[arm][0]
        d = _EPISODES_DIR / f"{article}__preset{preset}"
    else:
        preset = geo._TEST_ARM_PRESETS[arm][0]
        d = _TEST_EPISODES_DIR / f"{article}__preset{preset}"
    return d if d.is_dir() else None


def main() -> None:
    per_arm: dict[str, list[dict]] = {a: [] for a in _ARM_ORDER}
    per_article: dict[str, dict[str, dict]] = {}

    missing = []
    for article in _ALL_42:
        per_article[article] = {}
        for arm in _ARM_ORDER:
            ep_dir = _ep_dir_for(article, arm)
            if ep_dir is None:
                missing.append(f"{article}/{arm}")
                continue
            m = _count_episode(ep_dir)
            per_arm[arm].append(m)
            per_article[article][arm] = m

    if missing:
        print(f"WARNING: {len(missing)} missing episode dirs: {missing[:10]}{' ...' if len(missing) > 10 else ''}\n")

    # ---- Part 1: exploit phase really constant? (sanity check) ------------
    print("=" * 100)
    print("PART 1: Is the EXPLOITATION phase really constant across arms? (sanity check)")
    print("=" * 100)
    for arm in _ARM_ORDER:
        rows = per_arm[arm]
        eq = [r["exploit_queries"] for r in rows]
        es = [r["exploit_scrapes"] for r in rows]
        er = [r["exploit_rounds"] for r in rows]
        print(f"  {arm:<10} exploit_rounds mean={statistics.mean(er):.2f} (std={statistics.pstdev(er):.2f})  "
              f"exploit_queries mean={statistics.mean(eq):.2f} (std={statistics.pstdev(eq):.2f})  "
              f"exploit_scrapes mean={statistics.mean(es):.2f} (std={statistics.pstdev(es):.2f})  n={len(rows)}")
    print()

    # ---- Part 2: actual EXPLORATION effort per arm, corpus-wide ------------
    print("=" * 100)
    print("PART 2: Actual EXPLORATION effort per arm (queries+scrapes), corpus-wide (n=42 each)")
    print("=" * 100)
    means = {}
    qmeans = {}
    smeans = {}
    for arm in _ARM_ORDER:
        rows = per_arm[arm]
        eff = [r["explore_effort"] for r in rows]
        eq = [r["explore_queries"] for r in rows]
        es = [r["explore_scrapes"] for r in rows]
        er = [r["explore_rounds"] for r in rows]
        mu = statistics.mean(eff)
        sd = statistics.pstdev(eff)
        means[arm] = mu
        qmeans[arm] = statistics.mean(eq)
        smeans[arm] = statistics.mean(es)
        print(f"  {arm:<10} assumed_nr={_ARM_ROUNDS[arm]}  actual_explore_rounds mean={statistics.mean(er):.2f}  "
              f"actual_explore_effort mean={mu:6.2f} (std={sd:5.2f}, min={min(eff)}, max={max(eff)})  "
              f"[queries={qmeans[arm]:.2f}  scrapes={smeans[arm]:.2f}]")
    print()
    print("  Per-round INCREMENTAL breakdown (queries vs scrapes added per additional round):")
    prev_q, prev_s, prev_r = 0.0, 0.0, 0
    for arm in _ARM_ORDER:
        r = _ARM_ROUNDS[arm]
        dq = qmeans[arm] - prev_q
        ds = smeans[arm] - prev_s
        dr = r - prev_r
        if dr > 0:
            print(f"  {arm:<10} +{dr} round(s): +{dq:.2f} queries ({dq/dr:.2f}/round), "
                  f"+{ds:.2f} scrapes ({ds/dr:.2f}/round)")
        prev_q, prev_s, prev_r = qmeans[arm], smeans[arm], r
    print()
    print("  Ratio check (actual_effort[arm] / actual_effort[light]) vs (assumed nr[arm] / nr[light]):")
    light_mu = means["light"] if means["light"] else 1.0
    for arm in _ARM_ORDER:
        assumed_ratio = _ARM_ROUNDS[arm] / _ARM_ROUNDS["light"] if _ARM_ROUNDS["light"] else float("nan")
        actual_ratio = means[arm] / light_mu if light_mu else float("nan")
        print(f"  {arm:<10} assumed={assumed_ratio:5.2f}x   actual={actual_ratio:5.2f}x")
    print()

    # ---- Part 3: per-article variability -- does actual effort track nr? --
    print("=" * 100)
    print("PART 3: Per-article actual exploration effort (all 42 articles)")
    print("=" * 100)
    header = f"{'article':<45} {'skip':>6} {'light':>6} {'std':>6} {'deep':>6}  deep/std_actual  deep/std_assumed"
    print(header)
    print("-" * len(header))
    deep_std_actual_ratios = []
    for article in _ALL_42:
        row = per_article[article]
        if len(row) < 4:
            continue
        eff = {a: row[a]["explore_effort"] for a in _ARM_ORDER}
        deep_std_actual = eff["deep"] / eff["standard"] if eff["standard"] else float("nan")
        deep_std_actual_ratios.append(deep_std_actual)
        print(f"{article:<45} {eff['skip']:>6} {eff['light']:>6} {eff['standard']:>6} {eff['deep']:>6}  "
              f"{deep_std_actual:>14.2f}x  {1.5:>15.2f}x")
    print()
    valid = [r for r in deep_std_actual_ratios if r == r]  # drop NaNs
    print(f"  mean(deep/standard actual effort ratio) = {statistics.mean(valid):.2f}x  "
          f"(assumed nr ratio = 3/2 = 1.50x)  n={len(valid)}")
    print()

    # ---- Part 4: focus on the 9 actionable articles ------------------------
    print("=" * 100)
    print("PART 4: Focus on the 9 cost-suppressed-but-actionable articles")
    print("=" * 100)
    header2 = f"{'article':<40} {'skip':>6} {'light':>6} {'std':>6} {'deep':>6}  deep_vs_std_actual"
    print(header2)
    print("-" * len(header2))
    for article in _ACTIONABLE_9:
        row = per_article.get(article, {})
        if len(row) < 4:
            print(f"{article:<40}  (missing episode data)")
            continue
        eff = {a: row[a]["explore_effort"] for a in _ARM_ORDER}
        ratio = eff["deep"] / eff["standard"] if eff["standard"] else float("nan")
        print(f"{article:<40} {eff['skip']:>6} {eff['light']:>6} {eff['standard']:>6} {eff['deep']:>6}  {ratio:>16.2f}x")


if __name__ == "__main__":
    main()
