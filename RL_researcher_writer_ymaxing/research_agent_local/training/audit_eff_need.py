"""Reconstruct eff_need distribution from existing digest XML + guideline features.

Run from research_agent_local/:
  python3 training/audit_eff_need.py
"""
import re, json, pathlib, collections, sys

_THIS_DIR = pathlib.Path(__file__).resolve().parent
BASE = _THIS_DIR.parent.parent / "rl_training_data" / "bases"


def _preset_2d(need, target_words, mandatory_bullets, must_cover_depth, must_stay_brief, policy):
    if policy == "forbidden":
        return "skip", -999
    headroom = 0
    if target_words >= 400: headroom += 1
    elif 0 < target_words < 200: headroom -= 1
    if mandatory_bullets >= 5: headroom += 1
    elif 0 < mandatory_bullets <= 2: headroom -= 1
    if must_cover_depth >= 3: headroom += 1
    if must_stay_brief >= 2: headroom -= 1
    if policy == "required": headroom += 1
    eff_need = need + 2 * headroom
    if eff_need <= 2: return "skip", eff_need
    if eff_need <= 5: return "light", eff_need
    if eff_need <= 9: return "standard", eff_need
    return "deep", eff_need


data_points = []

for d in sorted(BASE.iterdir()):
    if d.name.endswith("_OLD"): continue
    digest_f = d / "research_digest.md"
    oracle_f = d / "section_oracle.json"
    features_f = d / "guideline_features.json"
    if not (digest_f.exists() and oracle_f.exists() and features_f.exists()):
        continue
    features = json.loads(features_f.read_text(encoding="utf-8"))
    policy = features.get("external_evidence_policy", "allowed")
    oracle = json.loads(oracle_f.read_text(encoding="utf-8")).get("presets", {})
    text = digest_f.read_text(encoding="utf-8")
    gp_match = re.search(r"<gap_profile>(.*?)</gap_profile>", text, re.DOTALL)
    if not gp_match:
        print(f"WARN: no gap_profile in {d.name}", file=sys.stderr)
        continue
    for sm in re.finditer(
        r'<section\s+id="([^"]+)"\s+need_depth="(\d+)"\s+need_breadth="(\d+)"'
        r'\s+target_words="(\d+)"\s+mandatory_bullets="(\d+)"'
        r'\s+must_cover_depth="(\d+)"\s+must_stay_brief="(\d+)"',
        gp_match.group(1),
    ):
        sec_id = sm.group(1)
        need = int(sm.group(2)) + int(sm.group(3))
        tw = int(sm.group(4))
        mb = int(sm.group(5))
        mcd = int(sm.group(6))
        msb = int(sm.group(7))
        label, eff = _preset_2d(need, tw, mb, mcd, msb, policy)
        oracle_label = oracle.get(sec_id, "?")
        vtype = d.name.split("__var_")[1] if "__var_" in d.name else "base"
        data_points.append((need, eff, label, oracle_label, policy, vtype, d.name, sec_id))

print(f"Total data points: {len(data_points)}")
print()

# 1. Raw need distribution (all policies)
print("=== Raw `need` distribution (all, including forbidden) ===")
raw_needs = [p[0] for p in data_points]
cnt = collections.Counter(raw_needs)
total = len(raw_needs)
cumulative = 0
for i in sorted(cnt):
    n = cnt[i]
    cumulative += n
    band = "skip" if i<=2 else ("light" if i<=5 else ("standard" if i<=9 else "deep"))
    print(f"  need={i:3d}: {n:3d} ({100*n/total:.1f}%)  cum={100*cumulative/total:.0f}%  [{band}]")
print()

# 2. eff_need distribution (non-forbidden)
nonforbidden = [p for p in data_points if p[4] != "forbidden"]
print(f"=== eff_need distribution (non-forbidden, n={len(nonforbidden)}) ===")
eff_needs = [p[1] for p in nonforbidden]
cnt2 = collections.Counter(eff_needs)
total2 = len(eff_needs)
cumulative = 0
for i in sorted(cnt2):
    n = cnt2[i]
    cumulative += n
    band = "skip" if i<=2 else ("light" if i<=5 else ("standard" if i<=9 else "deep"))
    print(f"  eff={i:3d}: {n:3d} ({100*n/total2:.1f}%)  cum={100*cumulative/total2:.0f}%  [{band}]")
print()

# 3. Oracle vs computed agreement
print("=== Oracle vs recomputed label agreement ===")
agree = sum(1 for p in data_points if p[2] == p[3])
print(f"  {agree}/{len(data_points)} agree ({100*agree/len(data_points):.1f}%)")
mismatches = [(p[6], p[7], p[2], p[3]) for p in data_points if p[2] != p[3]]
if mismatches:
    print("  Mismatches:")
    for art, sec, comp, ora in mismatches[:20]:
        print(f"    {art}/{sec}: computed={comp} oracle={ora}")
print()

# 4. What thresholds would give ~25% per non-forbidden class?
print("=== Threshold sensitivity for non-forbidden sections ===")
eff_sorted = sorted(eff_needs)
n = len(eff_sorted)
targets = [0.25, 0.50, 0.75]
for t in targets:
    idx = int(t * n)
    print(f"  {int(t*100)}th percentile of eff_need: {eff_sorted[min(idx, n-1)]}")
print()
print("  Quartile suggestion (to equalize non-forbidden classes into 4 equal groups):")
for q, label in [(0.25, "skip"), (0.50, "light"), (0.75, "standard")]:
    idx = int(q * n)
    print(f"    eff_need <= {eff_sorted[min(idx, n-1)]:2d} -> {label}")
print(f"    eff_need >  {eff_sorted[min(int(0.75*n), n-1)]:2d} -> deep")
