import json, re, math, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASES = ROOT.parent / "rl_training_data" / "bases"
MD = ROOT / "grok_planner_test_results" / "rl_guards_only_train_and_test_results_run33_averaged_confidence_epoch81.md"
TEST_SUM = ROOT / "grok_planner_test_results" / "semantic_signals_results" / "test_summary.json"
TRAIN_SUM = ROOT / "grok_planner_test_results" / "semantic_signals_results" / "train_summary.json"

# ---- Parse RL+guards eval report ----
text = MD.read_text(encoding="utf-8")
blocks = re.split(r"(?=  Variant : )", text)
eval_data = {}
for b in blocks:
    m = re.search(r"Variant : (\S+)\s+\[(TRAIN|TEST)\]", b)
    if not m:
        continue
    name, split = m.group(1), m.group(2)
    policy_m = re.search(r"Policy\s*:\s*(\w+)", b)
    rl_m = re.search(r"RL model\s*:\s*P(\d)\s+(\w+)\s+conf=(\d+)%\s+H=([\d.]+)bits", b)
    oracle_m = re.search(r"Oracle\s*:\s*P(\d)\s+(\w+)", b)
    regret_m = re.search(r"Regret\s*:\s*([\d.]+)", b)
    verdict_m = re.search(r"Verdict\s*:\s*(\S+)\s+([A-Z ]+?)\s*(?:\(|$)", b)
    if not (policy_m and rl_m and oracle_m and regret_m):
        continue
    eval_data[name] = {
        "split": split,
        "policy": policy_m.group(1),
        "conf": int(rl_m.group(3)) / 100.0,
        "H": float(rl_m.group(4)),
        "oracle_idx": int(oracle_m.group(1)),
        "regret": float(regret_m.group(1)),
        "verdict": verdict_m.group(2).strip() if verdict_m else "?",
    }

print(f"Parsed {len(eval_data)} articles from eval report")

# ---- Semantic signal + word-weighting ----
def load_summary(path):
    return {d["article"]: d for d in json.loads(path.read_text(encoding="utf-8"))}

test_sig = load_summary(TEST_SUM)
train_sig = load_summary(TRAIN_SUM)
all_sig = {**test_sig, **train_sig}

def weighted_signals(article, parsed):
    feat_path = BASES / article / "guideline_features.json"
    feats = json.loads(feat_path.read_text(encoding="utf-8"))["sections"]
    num_s = num_r = denom = 0.0
    max_r = 0.0
    for sec in parsed["sections"]:
        sid = sec["sec_id"]
        w = feats.get(sid, {}).get("target_words")
        if w is None:
            key = sid.split("::")[0]
            match = next((k for k in feats if k.startswith(key + "::")), None)
            w = feats[match]["target_words"] if match else 0
        num_s += w * sec["scripted_example_fraction"]
        num_r += w * sec["argumentative_risk"]
        denom += w
        max_r = max(max_r, sec["argumentative_risk"])
    return num_s/denom, num_r/denom, max_r

rows = []
for name, ev in eval_data.items():
    if ev["policy"] == "forbidden":
        continue
    sig = all_sig.get(name)
    if not sig or not sig.get("parse_ok"):
        print(f"MISSING SIGNAL: {name}")
        continue
    parsed = sig["parsed"]
    w_scripted, w_risk, max_risk = weighted_signals(name, parsed)
    rows.append({
        "article": name,
        "split": ev["split"],
        "verdict": ev["verdict"],
        "regret": ev["regret"],
        "conf": ev["conf"],
        "H": ev["H"],
        "si": parsed["source_independence"],
        "tc": parsed["topic_canonicity"],
        "w_scripted": w_scripted,
        "w_risk": w_risk,
        "max_risk": max_risk,
    })

print(f"Joined {len(rows)} non-forbidden articles with valid semantic signals\n")

# ---- Standardize (z-score) each of 5 signal dims across the full corpus ----
dims = ["si", "tc", "w_scripted", "w_risk", "conf"]
means = {d: statistics.mean(r[d] for r in rows) for d in dims}
stdevs = {d: statistics.pstdev(r[d] for r in rows) for d in dims}

for r in rows:
    z = {d: (r[d] - means[d]) / stdevs[d] if stdevs[d] > 0 else 0.0 for d in dims}
    r["z"] = z
    r["combined_l2"] = math.sqrt(sum(v*v for v in z.values()))
    r["combined_l1"] = sum(abs(v) for v in z.values())

rows.sort(key=lambda r: -r["combined_l2"])
header = f"{'rank':<5}{'article':<45}{'split':<6}{'verdict':<10}{'L2':<7}{'L1':<7}" + "".join(f"z_{d:<8}" for d in dims)
print(header)
for i, r in enumerate(rows, 1):
    zs = "".join(f"{r['z'][d]:>+9.2f} " for d in dims)
    marker = "  <<<" if r["article"] == "07_reasoning_planning" else ""
    print(f"{i:<5}{r['article']:<45}{r['split']:<6}{r['verdict']:<10}{r['combined_l2']:<7.2f}{r['combined_l1']:<7.2f}{zs}{marker}")

print(f"\nn = {len(rows)} articles total")

print("\n--- Univariate percentile rank of 07_reasoning_planning on each dim ---")
target = next(r for r in rows if r["article"] == "07_reasoning_planning")
for d in dims:
    vals = sorted(r[d] for r in rows)
    rank = vals.index(target[d]) + 1
    n = len(vals)
    print(f"{d:<12} value={target[d]:.3f}  rank={rank}/{n}  (z={target['z'][d]:+.2f})  mean={means[d]:.3f} sd={stdevs[d]:.3f}")
