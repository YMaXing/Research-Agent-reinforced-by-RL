"""Comprehensive dataset analysis across all 126 variant episodes (7 articles x 3 variants x 6 presets)."""
import json
from pathlib import Path
from collections import Counter, defaultdict
import statistics

EP_BASE = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes")
PRESET_ROUNDS = {0:0, 1:1, 2:2, 3:2, 4:3, 5:3}
ARTICLES = ["02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
            "06_tools", "08_react_practice", "09_RAG", "11_multimodal"]
VARIANTS = ["var_minimal", "var_standard", "var_demanding"]


def compute_reward(s, p, vl):
    cc, fl = s["ground_truth_core_content"], s["ground_truth_flow"]
    de, be = s["ground_truth_depth_enhancement"], s["ground_truth_breadth_enhancement"]
    cp = s["ground_truth_core_preservation"]
    ga, ra = s["user_intent_guideline_adherence"], s["user_intent_research_anchoring"]
    nr = PRESET_ROUNDS[p]
    if vl == "minimal":
        return 0.05*cc + 0.05*fl + 0.80*ga + 0.10*ra - 0.02*nr
    elif vl == "demanding":
        return 0.12*cc + 0.08*fl + cp*(0.55*de + 0.35*be)*0.50 + (0.60*ga + 0.40*ra)*0.25 - 0.01*nr
    else:
        return 0.20*cc + 0.20*fl + cp*(0.60*de + 0.40*be)*0.30 + (0.50*ga + 0.50*ra)*0.30 - 0.02*nr


# Load all data
data = {}  # data[art][var][p] = {scores, reward}
for art in ARTICLES:
    data[art] = {}
    for var in VARIANTS:
        data[art][var] = {}
        for p in range(6):
            sf = EP_BASE / f"{art}__{var}__preset{p}" / "scores.json"
            s = json.loads(sf.read_text())
            data[art][var][p] = {"s": s, "r": compute_reward(s, p, var.replace("var_", ""))}


def line(c="="): print(c * 90)


# ============================================================
# 1. REWARD TABLE — full 126 episodes
# ============================================================
line()
print("  SECTION 1 — REWARD TABLE  (all 126 variant episodes)")
line()
for art in ARTICLES:
    print(f"\n  {art}")
    print(f"  {'Variant':<16} {'P0':>7} {'P1':>7} {'P2':>7} {'P3':>7} {'P4':>7} {'P5':>7}  │  {'Oracle':>10}")
    for var in VARIANTS:
        rs = [data[art][var][p]["r"] for p in range(6)]
        op = rs.index(max(rs))
        print(f"  {var:<16} " + "  ".join(f"{r:7.4f}" for r in rs) + f"  │  P{op} ({max(rs):.3f})")


# ============================================================
# 2. SIGNAL QUALITY — regret per group
# ============================================================
line()
print("  SECTION 2 — GRPO SIGNAL QUALITY  (regret = max - mean per group)")
line()
print(f"  {'Group':<46} {'max':>7} {'mean':>7} {'min':>7} {'regret':>8} {'spread':>8}  quality")
strong = ok = weak = 0
all_regrets = []
group_quality = {}
for art in ARTICLES:
    for var in VARIANTS:
        rs = [data[art][var][p]["r"] for p in range(6)]
        mx, mn, mu = max(rs), min(rs), sum(rs)/6
        regret = mx - mu
        spread = mx - mn
        all_regrets.append(regret)
        if regret >= 0.12:
            q = "STRONG"; strong += 1
        elif regret >= 0.06:
            q = "ok    "; ok += 1
        else:
            q = "weak  "; weak += 1
        group_quality[(art, var)] = q.strip()
        label = f"{art}__{var}"
        print(f"  {label:<46} {mx:7.4f} {mu:7.4f} {mn:7.4f} {regret:8.4f} {spread:8.4f}  {q}")

print(f"\n  Summary: STRONG={strong}/21  ok={ok}/21  weak={weak}/21  | mean regret={sum(all_regrets)/len(all_regrets):.4f}")


# ============================================================
# 3. ORACLE PRESET DISTRIBUTION
# ============================================================
line()
print("  SECTION 3 — ORACLE PRESET DISTRIBUTION  (which preset wins, per variant level)")
line()
oracle_counts = {var: Counter() for var in VARIANTS}
oracle_grid = {var: {} for var in VARIANTS}
for art in ARTICLES:
    for var in VARIANTS:
        rs = [data[art][var][p]["r"] for p in range(6)]
        op = rs.index(max(rs))
        oracle_counts[var][op] += 1
        oracle_grid[var][art] = (op, max(rs))

print(f"  {'Article':<25} {'var_minimal':>20} {'var_standard':>20} {'var_demanding':>20}")
for art in ARTICLES:
    cells = [f"P{oracle_grid[v][art][0]} ({oracle_grid[v][art][1]:.3f})" for v in VARIANTS]
    print(f"  {art:<25} " + " ".join(f"{c:>20}" for c in cells))

print()
print(f"  Oracle preset frequency by variant level (out of 7 articles):")
for var in VARIANTS:
    counts = " ".join(f"P{p}={oracle_counts[var][p]}" for p in range(6))
    print(f"    {var:<16} {counts}")

print()
all_oracle = Counter()
for var in VARIANTS:
    all_oracle.update(oracle_counts[var])
print(f"  TOTAL oracle frequency (21 groups): " + " ".join(f"P{p}={all_oracle[p]}" for p in range(6)))


# ============================================================
# 4. PER-METRIC DISTRIBUTION
# ============================================================
line()
print("  SECTION 4 — PER-METRIC DISTRIBUTION  (mean / std across all 126)")
line()
metrics = ["ground_truth_core_content", "ground_truth_flow", "ground_truth_structure",
           "ground_truth_depth_enhancement", "ground_truth_breadth_enhancement",
           "ground_truth_core_preservation", "user_intent_guideline_adherence",
           "user_intent_research_anchoring", "user_intent_golden_source_priority"]

# overall
print(f"  {'Metric':<38} {'mean':>7} {'std':>7} {'min':>7} {'max':>7}")
print(f"  {'─'*38} {'─'*7} {'─'*7} {'─'*7} {'─'*7}")
for m in metrics:
    vals = [data[a][v][p]["s"].get(m, 0) for a in ARTICLES for v in VARIANTS for p in range(6)]
    print(f"  {m:<38} {statistics.mean(vals):7.3f} {statistics.stdev(vals):7.3f} {min(vals):7.3f} {max(vals):7.3f}")

# Per variant breakdown
print()
print(f"  By variant level — mean of key metrics:")
print(f"  {'Variant':<16} {'cc':>7} {'fl':>7} {'de':>7} {'be':>7} {'cp':>7} {'ga':>7} {'ra':>7}")
for var in VARIANTS:
    means = {}
    for short, full in [("cc","ground_truth_core_content"), ("fl","ground_truth_flow"),
                         ("de","ground_truth_depth_enhancement"), ("be","ground_truth_breadth_enhancement"),
                         ("cp","ground_truth_core_preservation"), ("ga","user_intent_guideline_adherence"),
                         ("ra","user_intent_research_anchoring")]:
        vals = [data[a][var][p]["s"][full] for a in ARTICLES for p in range(6)]
        means[short] = statistics.mean(vals)
    print(f"  {var:<16} " + "  ".join(f"{means[k]:5.3f}" for k in ["cc","fl","de","be","cp","ga","ra"]))


# ============================================================
# 5. ANOMALY INVENTORY
# ============================================================
line()
print("  SECTION 5 — ANOMALY INVENTORY")
line()

# 5a. Low ga
print("\n  5a. Low ga episodes (ga <= 0.5):")
low_ga = []
for art in ARTICLES:
    for var in VARIANTS:
        for p in range(6):
            ga = data[art][var][p]["s"]["user_intent_guideline_adherence"]
            if ga <= 0.5:
                r = data[art][var][p]["r"]
                low_ga.append((art, var, p, ga, r))
low_ga.sort(key=lambda x: x[3])
for a, v, p, ga, r in low_ga:
    print(f"    ga={ga:.3f}  reward={r:.4f}  {a}__{v}__preset{p}")
print(f"    ── {len(low_ga)} episodes total")

# 5b. Low rewards (bottom 10)
print("\n  5b. Lowest 10 rewards across all 126 episodes:")
all_eps = []
for art in ARTICLES:
    for var in VARIANTS:
        for p in range(6):
            all_eps.append((data[art][var][p]["r"], art, var, p))
all_eps.sort()
for r, a, v, p in all_eps[:10]:
    ga = data[a][v][p]["s"]["user_intent_guideline_adherence"]
    print(f"    reward={r:.4f}  ga={ga:.3f}  {a}__{v}__preset{p}")

# 5c. Highest 10 rewards
print("\n  5c. Highest 10 rewards across all 126 episodes:")
for r, a, v, p in all_eps[-10:][::-1]:
    ga = data[a][v][p]["s"]["user_intent_guideline_adherence"]
    print(f"    reward={r:.4f}  ga={ga:.3f}  {a}__{v}__preset{p}")

# 5d. Perfect ga episodes
perfect = [(a,v,p,data[a][v][p]["r"]) for a in ARTICLES for v in VARIANTS for p in range(6)
           if data[a][v][p]["s"]["user_intent_guideline_adherence"] >= 0.999]
print(f"\n  5d. Perfect ga=1.0 episodes: {len(perfect)}/126 ({100*len(perfect)/126:.1f}%)")


# ============================================================
# 6. PRESET COST/BENEFIT (research rounds vs reward)
# ============================================================
line()
print("  SECTION 6 — PRESET COST/BENEFIT  (does more research help?)")
line()
print(f"  Mean reward per preset across all 21 (article,variant) groups:")
print(f"  {'Preset':<10} {'rounds':>7} {'mean R':>10} {'std':>7} {'oracle wins':>14}")
for p in range(6):
    rs = [data[a][v][p]["r"] for a in ARTICLES for v in VARIANTS]
    nr = PRESET_ROUNDS[p]
    wins = sum(oracle_counts[v][p] for v in VARIANTS)
    print(f"  P{p:<8} {nr:>7} {statistics.mean(rs):10.4f} {statistics.stdev(rs):7.4f} {wins:>14}/21")


# ============================================================
# 7. GRPO READINESS
# ============================================================
line()
print("  SECTION 7 — GRPO READINESS SUMMARY")
line()

# Group-level reward variance (for advantage normalization)
print("  Reward distribution check (need spread > ~0.05 for meaningful advantages):")
near_zero = sum(1 for a in ARTICLES for v in VARIANTS
                if (max(data[a][v][p]["r"] for p in range(6)) - min(data[a][v][p]["r"] for p in range(6))) < 0.05)
print(f"    Groups with spread < 0.05 (near-zero advantage): {near_zero}/21")

# Reward range overall
all_r = [data[a][v][p]["r"] for a in ARTICLES for v in VARIANTS for p in range(6)]
print(f"\n  Reward statistics (all 126):")
print(f"    min={min(all_r):.4f}  max={max(all_r):.4f}  mean={statistics.mean(all_r):.4f}  std={statistics.stdev(all_r):.4f}")

# Per-variant reward ranges (formulas produce different scales)
print(f"\n  Reward range per variant level (formulas have different scales):")
for var in VARIANTS:
    vs = [data[a][var][p]["r"] for a in ARTICLES for p in range(6)]
    print(f"    {var:<16} min={min(vs):.4f}  max={max(vs):.4f}  mean={statistics.mean(vs):.4f}")

# Recommendation
print()
print("  Final assessment:")
print(f"    - Total episodes: 126/126 graded")
print(f"    - Strong signal groups: {strong}/21 ({100*strong/21:.0f}%)")
print(f"    - Usable signal groups (ok+strong): {strong+ok}/21 ({100*(strong+ok)/21:.0f}%)")
print(f"    - Weak signal groups: {weak}/21 ({100*weak/21:.0f}%)")
print(f"    - Mean regret: {sum(all_regrets)/len(all_regrets):.4f} (regret-hybrid weighting will up-weight strong groups)")
