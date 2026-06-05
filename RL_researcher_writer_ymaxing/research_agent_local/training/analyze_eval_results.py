"""Analyze training-set eval results by parsing _eval_run2_v2.log + article_oracle.json.

Produces per-variant breakdowns, confusion matrices, near-miss reward analysis,
and article-level aggregation diagnostics.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent
_REPO_ROOT = _AGENT_DIR.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_LOG_PATH = _THIS_DIR / "_eval_run2_v2.log"

PRESET_NAMES = {
    0: "P0 baseline",
    1: "P1 single_balanced",
    2: "P2 balanced_depth",
    3: "P3 depth_breadth",
    4: "P4 bal_depth_breadth",
    5: "P5 depth_breadth_depth",
}
NUM_PRESETS = 6


def parse_log(path: Path) -> dict[str, dict]:
    """Parse the eval log into {article: {sections: [(title, oracle, pred)],
    article_oracle, article_pred, article_rewards}}."""
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"^--- ([^ ]+) ---$", text, flags=re.MULTILINE)
    # blocks: [pre, name1, body1, name2, body2, ...]
    out: dict[str, dict] = {}
    for i in range(1, len(blocks), 2):
        name = blocks[i].strip()
        body = blocks[i + 1]
        sections: list[tuple[str, int, int]] = []
        for m in re.finditer(
            r"^  (.{50}) P\s*(\d)  P\s*(\d)\s+([✓✗])$", body, re.MULTILINE
        ):
            title = m.group(1).strip()
            oracle = int(m.group(2))
            pred = int(m.group(3))
            sections.append((title, oracle, pred))
        m_oracle = re.search(r"Article oracle: P(\d)", body)
        m_pred = re.search(r"Article predicted: P(\d)", body)
        m_rew = re.search(r"Article rewards: \[([^\]]+)\]", body)
        rewards = []
        if m_rew:
            rewards = [float(x.strip().strip("'\"")) for x in m_rew.group(1).split(",")]
        if m_oracle and m_pred:
            out[name] = {
                "sections": sections,
                "article_oracle": int(m_oracle.group(1)),
                "article_pred": int(m_pred.group(1)),
                "article_rewards": rewards,
            }
    return out


def variant_of(article: str) -> str:
    if "__var_minimal" in article:
        return "minimal"
    if "__var_demanding" in article:
        return "demanding"
    return "standard"


def main() -> None:
    parsed = parse_log(_LOG_PATH)
    if not parsed:
        sys.exit("Failed to parse log")

    # Load oracle JSONs for section reward data (to compute reward-gap at miss)
    oracles: dict[str, dict] = {}
    for art in parsed:
        p = _BASES_DIR / art / "article_oracle.json"
        oracles[art] = json.loads(p.read_text(encoding="utf-8"))

    # ----------------------------------------------------------------------
    # 1. Per-variant section accuracy
    # ----------------------------------------------------------------------
    variant_sec: dict[str, list[int]] = defaultdict(list)  # variant -> [0/1]
    variant_art: dict[str, list[int]] = defaultdict(list)
    for art, d in parsed.items():
        v = variant_of(art)
        for _, o, p in d["sections"]:
            variant_sec[v].append(int(o == p))
        variant_art[v].append(int(d["article_oracle"] == d["article_pred"]))

    print("=" * 78)
    print(" 1. Per-variant accuracy")
    print("=" * 78)
    print(f"  {'Variant':<12}  {'Section acc':<18}  {'Article acc':<14}")
    for v in ("minimal", "standard", "demanding"):
        s = variant_sec[v]
        a = variant_art[v]
        print(
            f"  {v:<12}  {sum(s)}/{len(s)} = {sum(s) / len(s):>5.1%}      "
            f"{sum(a)}/{len(a)} = {sum(a) / len(a):>5.1%}"
        )

    # ----------------------------------------------------------------------
    # 2. Section-level confusion matrix
    # ----------------------------------------------------------------------
    cm = [[0] * NUM_PRESETS for _ in range(NUM_PRESETS)]
    oracle_count = Counter()
    pred_count = Counter()
    for d in parsed.values():
        for _, o, p in d["sections"]:
            cm[o][p] += 1
            oracle_count[o] += 1
            pred_count[p] += 1

    print()
    print("=" * 78)
    print(" 2. Section-level confusion matrix  (rows=oracle, cols=predicted)")
    print("=" * 78)
    print(f"  {'oracle\\pred':<12}" + "".join(f"  P{i:<3}" for i in range(NUM_PRESETS)) + f"  {'total':>5}  {'recall':>7}")
    for o in range(NUM_PRESETS):
        row = "  ".join(f"{cm[o][p]:>3}" for p in range(NUM_PRESETS))
        tot = oracle_count[o]
        rec = cm[o][o] / tot if tot else 0.0
        print(f"  P{o:<10}  {row}  {tot:>5}  {rec:>6.1%}")
    print(f"  {'pred total':<12}" + "".join(f"  {pred_count[p]:>3}" for p in range(NUM_PRESETS)))

    # ----------------------------------------------------------------------
    # 3. Reward-gap on section misses ("near-miss" analysis)
    # ----------------------------------------------------------------------
    # For each section miss, compute (oracle_reward - predicted_reward).
    miss_gaps: list[float] = []
    miss_gap_by_variant: dict[str, list[float]] = defaultdict(list)
    nearmiss_buckets = [0, 0, 0, 0]  # <=0.01, <=0.05, <=0.10, >0.10
    for art, d in parsed.items():
        v = variant_of(art)
        sec_data = oracles[art]["sections"]
        # Match section by title
        title_to_rewards = {s["title"]: s["rewards_by_preset"] for s in sec_data}
        for title, o, p in d["sections"]:
            # Try exact match first; fall back to startswith
            rewards = title_to_rewards.get(title)
            if rewards is None:
                for k, v_r in title_to_rewards.items():
                    if k.startswith(title) or title.startswith(k):
                        rewards = v_r
                        break
            if rewards is None or o == p:
                continue
            gap = rewards[o] - rewards[p]
            miss_gaps.append(gap)
            miss_gap_by_variant[v].append(gap)
            if gap <= 0.01:
                nearmiss_buckets[0] += 1
            elif gap <= 0.05:
                nearmiss_buckets[1] += 1
            elif gap <= 0.10:
                nearmiss_buckets[2] += 1
            else:
                nearmiss_buckets[3] += 1

    print()
    print("=" * 78)
    print(" 3. Reward-gap analysis on section misses  (n=%d)" % len(miss_gaps))
    print("=" * 78)
    if miss_gaps:
        miss_gaps_s = sorted(miss_gaps)
        mean_gap = sum(miss_gaps) / len(miss_gaps)
        median = miss_gaps_s[len(miss_gaps_s) // 2]
        print(f"  Mean reward gap on misses : {mean_gap:.4f}")
        print(f"  Median reward gap on misses: {median:.4f}")
        print(f"  Max  reward gap on misses : {max(miss_gaps):.4f}")
        print()
        print(f"  Near-miss bucket  (gap):    count   pct")
        labels = ["<=0.01 (tie)", "<=0.05 (close)", "<=0.10 (moderate)", ">0.10 (real)"]
        total = sum(nearmiss_buckets)
        for lab, c in zip(labels, nearmiss_buckets):
            print(f"    {lab:<22}  {c:>5}   {c / total:>5.1%}")
        print()
        for v in ("minimal", "standard", "demanding"):
            g = miss_gap_by_variant[v]
            if g:
                print(f"  {v:<10} mean miss-gap = {sum(g) / len(g):.4f}  (n={len(g)})")

    # ----------------------------------------------------------------------
    # 4. Section reward achieved vs oracle ceiling
    # ----------------------------------------------------------------------
    sec_realised = 0.0
    sec_oracle_total = 0.0
    sec_uniform_total = 0.0
    for art, d in parsed.items():
        sec_data = oracles[art]["sections"]
        title_to_rewards = {s["title"]: s["rewards_by_preset"] for s in sec_data}
        for title, o, p in d["sections"]:
            rewards = title_to_rewards.get(title)
            if rewards is None:
                for k, v_r in title_to_rewards.items():
                    if k.startswith(title) or title.startswith(k):
                        rewards = v_r
                        break
            if rewards is None:
                continue
            sec_realised += rewards[p]
            sec_oracle_total += rewards[o]
            sec_uniform_total += sum(rewards) / NUM_PRESETS
    n = sum(len(d["sections"]) for d in parsed.values())
    print()
    print("=" * 78)
    print(" 4. E[R] check (section-level)")
    print("=" * 78)
    print(f"  Sections             : {n}")
    print(f"  E[R] uniform         : {sec_uniform_total / n:.4f}")
    print(f"  E[R] model           : {sec_realised / n:.4f}")
    print(f"  E[R] oracle ceiling  : {sec_oracle_total / n:.4f}")
    gap_closed = (sec_realised - sec_uniform_total) / (sec_oracle_total - sec_uniform_total)
    print(f"  Gap closed           : {gap_closed:.1%}")

    # ----------------------------------------------------------------------
    # 5. Article-level: predicted preset rank in true ranking
    # ----------------------------------------------------------------------
    print()
    print("=" * 78)
    print(" 5. Article-level diagnostics")
    print("=" * 78)
    rank_dist = Counter()
    art_realised = 0.0
    art_oracle_total = 0.0
    art_uniform_total = 0.0
    art_realised_minus_runnerup = []
    print(f"  {'article':<40}  oracle pred  rank  ΔR(oracle-pred)  ΔR(uniform-pred)")
    print(f"  {'-' * 40}  ------ ----  ----  ---------------  ----------------")
    for art, d in sorted(parsed.items()):
        rew = d["article_rewards"]
        ranking = sorted(range(NUM_PRESETS), key=lambda i: rew[i], reverse=True)
        rank = ranking.index(d["article_pred"])  # 0 = best
        rank_dist[rank] += 1
        gap_oracle = rew[d["article_oracle"]] - rew[d["article_pred"]]
        uniform = sum(rew) / NUM_PRESETS
        gap_uniform = uniform - rew[d["article_pred"]]  # negative if pred>uniform
        art_realised += rew[d["article_pred"]]
        art_oracle_total += rew[d["article_oracle"]]
        art_uniform_total += uniform
        art_realised_minus_runnerup.append(gap_oracle)
        flag = "✓" if rank == 0 else f"#{rank + 1}"
        print(
            f"  {art:<40}   P{d['article_oracle']}    P{d['article_pred']}   {flag:<4}"
            f"     {gap_oracle:+.4f}        {gap_uniform:+.4f}"
        )
    print()
    print(f"  Predicted preset rank distribution (rank in true ranking, lower=better):")
    for r in range(NUM_PRESETS):
        c = rank_dist.get(r, 0)
        print(f"    rank #{r + 1}:  {c:>3}  ({c / 21:>5.1%})")
    print()
    n_art = len(parsed)
    print(f"  E[R] article uniform : {art_uniform_total / n_art:.4f}")
    print(f"  E[R] article model   : {art_realised / n_art:.4f}")
    print(f"  E[R] article oracle  : {art_oracle_total / n_art:.4f}")
    if art_oracle_total > art_uniform_total:
        gc = (art_realised - art_uniform_total) / (art_oracle_total - art_uniform_total)
        print(f"  Article gap closed   : {gc:.1%}")

    # ----------------------------------------------------------------------
    # 6. Article-level miss diagnostics: were these "tight" or "decisive" cases?
    # ----------------------------------------------------------------------
    print()
    print("=" * 78)
    print(" 6. Article-level miss diagnostics  (oracle margin vs miss)")
    print("=" * 78)
    print(f"  {'article':<40}  hit?   oracle_margin   miss_gap")
    print(f"  {'-' * 40}  ----   -------------   --------")
    margin_hits = []
    margin_miss = []
    for art, d in sorted(parsed.items()):
        oracle_margin = oracles[art]["margin"]
        miss_gap = d["article_rewards"][d["article_oracle"]] - d["article_rewards"][d["article_pred"]]
        hit = d["article_oracle"] == d["article_pred"]
        flag = "✓" if hit else "✗"
        print(f"  {art:<40}  {flag:<4}   {oracle_margin:.4f}          {miss_gap:.4f}")
        if hit:
            margin_hits.append(oracle_margin)
        else:
            margin_miss.append(oracle_margin)
    if margin_hits:
        print(f"\n  Mean oracle margin on HITS : {sum(margin_hits) / len(margin_hits):.4f}  (n={len(margin_hits)})")
    if margin_miss:
        print(f"  Mean oracle margin on MISS : {sum(margin_miss) / len(margin_miss):.4f}  (n={len(margin_miss)})")

    # ----------------------------------------------------------------------
    # 7. Per-article section accuracy ranking (best/worst articles)
    # ----------------------------------------------------------------------
    per_art = []
    for art, d in parsed.items():
        c = sum(1 for _, o, p in d["sections"] if o == p)
        t = len(d["sections"])
        per_art.append((art, c, t, c / t if t else 0))
    per_art.sort(key=lambda x: x[3])
    print()
    print("=" * 78)
    print(" 7. Per-article section accuracy ranking (worst → best)")
    print("=" * 78)
    for art, c, t, acc in per_art:
        print(f"  {art:<40}  {c}/{t} = {acc:>5.1%}")


if __name__ == "__main__":
    main()
