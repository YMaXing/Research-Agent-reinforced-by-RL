"""
Count tool calls per preset from episode data (Option C analysis).

Metrics per episode:
  - explore_queries:  lines matching "[Exploration]" in full_queries.md
  - explore_scrapes:  "[EXPLORATION]" entries in url_phases.json
  - explore_rounds:   count of _explore_round_N.done files

Exploitation phases are constant across presets (3 fixed rounds), so only
the exploration metrics can show a P2-vs-P3 / P4-vs-P5 difference.
"""
from __future__ import annotations
import json
import re
from collections import defaultdict
from pathlib import Path

EPISODES_DIR = Path(__file__).parent / "episodes"
VARIANTS = ("var_minimal", "var_standard", "var_demanding")
ARTICLES = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "10_memory_knowledge_access",
    "11_multimodal",
]


def count_episode(ep_dir: Path) -> dict:
    research = ep_dir / ".research"

    # ── exploration rounds (done-file count) ────────────────────────────────
    explore_rounds = len(list(research.glob("_explore_round_*.done")))

    # ── full_queries.md → count [Exploration] vs [Exploitation] queries ────
    fq = research / "full_queries.md"
    explore_queries = 0
    exploit_queries = 0
    if fq.exists():
        text = fq.read_text(encoding="utf-8", errors="replace")
        explore_queries = len(re.findall(r"\[Exploration\]", text))
        exploit_queries = len(re.findall(r"\[Exploitation\]", text))

    # ── url_phases.json → scrape counts ────────────────────────────────────
    up = research / "url_phases.json"
    explore_scrapes = 0
    exploit_scrapes = 0
    if up.exists():
        phases = json.loads(up.read_text(encoding="utf-8", errors="replace"))
        for tag in phases.values():
            if "[EXPLORATION]" in str(tag):
                explore_scrapes += 1
            elif "[EXPLOITATION]" in str(tag):
                exploit_scrapes += 1

    return {
        "explore_rounds":  explore_rounds,
        "explore_queries": explore_queries,
        "explore_scrapes": explore_scrapes,
        "exploit_queries": exploit_queries,
        "exploit_scrapes": exploit_scrapes,
    }


def main() -> None:
    # Accumulate per (variant, preset)
    data: dict[tuple[str, int], list[dict]] = defaultdict(list)

    for article in ARTICLES:
        for variant in VARIANTS:
            for preset in range(6):
                ep_dir = EPISODES_DIR / f"{article}__{variant}__preset{preset}"
                if not ep_dir.is_dir():
                    continue
                metrics = count_episode(ep_dir)
                metrics["article"] = article
                data[(variant, preset)].append(metrics)

    # ── Per-episode detail table ────────────────────────────────────────────
    print("=" * 110)
    print("PART 1: Per-episode detail  (exploration metrics only)")
    print("=" * 110)

    header = f"{'Episode':<55} {'P':>2} {'ExRnd':>5} {'ExQry':>5} {'ExScr':>5}"
    print(header)
    print("-" * 75)

    for article in ARTICLES:
        for variant in VARIANTS:
            for preset in range(6):
                ep_dir = EPISODES_DIR / f"{article}__{variant}__preset{preset}"
                if not ep_dir.is_dir():
                    continue
                m = count_episode(ep_dir)
                label = f"{article}__{variant}"
                print(
                    f"{label:<55} {preset:>2}  "
                    f"{m['explore_rounds']:>4}  "
                    f"{m['explore_queries']:>4}  "
                    f"{m['explore_scrapes']:>4}"
                )

    # ── Aggregate by (variant, preset) ─────────────────────────────────────
    print()
    print("=" * 110)
    print("PART 2: Mean ± std by (variant, preset)  — 8 episodes each")
    print("=" * 110)

    import statistics

    def fmt(vals: list[float]) -> str:
        if not vals:
            return "  n/a"
        mu = statistics.mean(vals)
        if len(vals) > 1:
            sd = statistics.stdev(vals)
            return f"{mu:5.2f} ±{sd:4.2f}"
        return f"{mu:5.2f}"

    print(f"\n{'Variant':<15} {'P':>2}  "
          f"{'ExRnd':>14}  {'ExQry':>14}  {'ExScr':>14}  n")
    print("-" * 70)

    for variant in VARIANTS:
        for preset in range(6):
            rows = data[(variant, preset)]
            if not rows:
                continue
            rnd = [r["explore_rounds"] for r in rows]
            qry = [r["explore_queries"] for r in rows]
            scr = [r["explore_scrapes"] for r in rows]
            print(
                f"{variant:<15} P{preset}  "
                f"{fmt(rnd):>14}  "
                f"{fmt(qry):>14}  "
                f"{fmt(scr):>14}  {len(rows)}"
            )
        print()

    # ── Key comparison: P2 vs P3, P4 vs P5 ─────────────────────────────────
    print("=" * 110)
    print("PART 3: P2 vs P3 and P4 vs P5 gap (exploration queries and scrapes)")
    print("=" * 110)
    print()

    for variant in VARIANTS:
        print(f"[{variant}]")
        for lo, hi in [(2, 3), (4, 5)]:
            rows_lo = data[(variant, lo)]
            rows_hi = data[(variant, hi)]
            if not rows_lo or not rows_hi:
                continue
            qlo = statistics.mean(r["explore_queries"] for r in rows_lo)
            qhi = statistics.mean(r["explore_queries"] for r in rows_hi)
            slo = statistics.mean(r["explore_scrapes"] for r in rows_lo)
            shi = statistics.mean(r["explore_scrapes"] for r in rows_hi)
            print(
                f"  P{lo} vs P{hi}:  "
                f"queries  P{lo}={qlo:.2f}  P{hi}={qhi:.2f}  Δ={qhi-qlo:+.2f}  |  "
                f"scrapes  P{lo}={slo:.2f}  P{hi}={shi:.2f}  Δ={shi-slo:+.2f}"
            )
        print()

    # ── Proposed cost weights ───────────────────────────────────────────────
    print("=" * 110)
    print("PART 4: Proposed empirical cost weights (normalised to P1=1.0)")
    print("  cost_weight[p] = mean(total_queries[p]) / mean(total_queries[P1])")
    print("  where total_queries = exploit_queries + explore_queries")
    print("=" * 110)
    print()

    # Pool all variants to get a single cost estimate
    pooled: dict[int, list[float]] = defaultdict(list)
    for variant in VARIANTS:
        for preset in range(6):
            rows = data[(variant, preset)]
            for r in rows:
                total = r["exploit_queries"] + r["explore_queries"]
                pooled[preset].append(float(total))

    p1_mean = statistics.mean(pooled[1]) if pooled[1] else 1.0
    print(f"{'Preset':<8} {'Mean total queries':>20}  {'Normalised weight':>18}")
    print("-" * 50)
    for p in range(6):
        vals = pooled[p]
        mu = statistics.mean(vals) if vals else 0.0
        w = mu / p1_mean if p1_mean else 0.0
        print(f"P{p}      {mu:>20.2f}  {w:>18.4f}")

    print()
    print("NOTE: If Δ(P2,P3) ≈ 0 and Δ(P4,P5) ≈ 0, empirical cost cannot break")
    print("      the symmetry and Option A (ordinal index) is the only recourse.")


if __name__ == "__main__":
    main()
