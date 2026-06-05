"""Thorough analysis of a GRPO training run (run11 by default).

Reads training_log.jsonl and reports:
  1. Epoch-level trajectory of the headline metrics
  2. Best epochs by strict / near-tie / E[R]
  3. KL / grad-norm / entropy dynamics + phase transition
  4. Per-class confusion at the best strict epoch
  5. Chronically-wrong sections (wrong in >=80% of epochs)
  6. Near-tie vs strict gap (impact of --near-tie-margin relaxation)
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev

RUN = sys.argv[1] if len(sys.argv) > 1 else "run11"
BASE = Path(__file__).resolve().parent / "checkpoints" / "tasks" / RUN
LOG = BASE / "training_log.jsonl"

PRESET_NAMES = {0: "skip", 1: "light", 2: "standard", 3: "deep"}

rows = [json.loads(l) for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()]
print(f"Run: {RUN}   epochs logged: {len(rows)}  (epoch {rows[0]['epoch']}..{rows[-1]['epoch']})")

# ---------------------------------------------------------------------------
# 1. Headline trajectory
# ---------------------------------------------------------------------------
def g(r, k, d=0.0):
    return r.get(k, d)

best_strict = max(rows, key=lambda r: g(r, "strict_top1_accuracy"))
best_near   = max(rows, key=lambda r: g(r, "top1_accuracy"))
best_er     = max(rows, key=lambda r: g(r, "mean_expected_reward"))

print("\n" + "=" * 78)
print("1. BEST EPOCHS")
print("=" * 78)
for label, r in [("strict_top1", best_strict), ("near_tie_top1", best_near), ("E[R]", best_er)]:
    print(f"  best {label:<14} @ ep{r['epoch']:>3}: "
          f"strict={g(r,'strict_top1_accuracy'):.4f}  near={g(r,'top1_accuracy'):.4f}  "
          f"E[R]={g(r,'mean_expected_reward'):.4f}  KL={g(r,'mean_kl'):.3f}  "
          f"gnorm={g(r,'grad_norm'):.3f}  H={g(r,'mean_entropy'):.3f}")

# epochs where strict > 0.80
over80 = [r for r in rows if g(r, "strict_top1_accuracy") > 0.80]
print(f"\n  epochs with strict_top1 > 0.80: {len(over80)}")
for r in over80:
    print(f"    ep{r['epoch']:>3}: strict={g(r,'strict_top1_accuracy'):.4f}  "
          f"near={g(r,'top1_accuracy'):.4f}  E[R]={g(r,'mean_expected_reward'):.4f}  "
          f"KL={g(r,'mean_kl'):.3f}  H={g(r,'mean_entropy'):.3f}")

# ---------------------------------------------------------------------------
# 2. Trajectory sampling
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("2. TRAJECTORY (every ~10 epochs)")
print("=" * 78)
print(f"  {'ep':>3} {'strict':>7} {'near':>7} {'E[R]':>7} {'KL':>7} {'gnorm':>7} {'H':>7} {'floor%':>7} {'lr':>9}")
step = max(1, len(rows) // 20)
for r in rows[::step] + [rows[-1]]:
    print(f"  {r['epoch']:>3} {g(r,'strict_top1_accuracy'):>7.4f} {g(r,'top1_accuracy'):>7.4f} "
          f"{g(r,'mean_expected_reward'):>7.4f} {g(r,'mean_kl'):>7.3f} {g(r,'grad_norm'):>7.3f} "
          f"{g(r,'mean_entropy'):>7.3f} {g(r,'sigma_floor_fraction'):>7.3f} {g(r,'lr'):>9.2e}")

# ---------------------------------------------------------------------------
# 3. KL / entropy phase transition + late-run stability
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("3. DYNAMICS")
print("=" * 78)
kls = [g(r, "mean_kl") for r in rows]
gns = [g(r, "grad_norm") for r in rows]
hs  = [g(r, "mean_entropy") for r in rows]
strict = [g(r, "strict_top1_accuracy") for r in rows]
print(f"  KL:      min={min(kls):.3f}  max={max(kls):.3f}  final={kls[-1]:.3f}  "
      f"argmax=ep{rows[kls.index(max(kls))]['epoch']}")
print(f"  gnorm:   min={min(gns):.3f}  max={max(gns):.3f}  final={gns[-1]:.3f}  "
      f"argmax=ep{rows[gns.index(max(gns))]['epoch']}")
print(f"  entropy: min={min(hs):.3f}  max={max(hs):.3f}  final={hs[-1]:.3f}")

# Phase transition: first epoch strict crosses 0.50, 0.70, 0.78
for thr in (0.50, 0.60, 0.70, 0.75, 0.78, 0.80):
    hit = next((r for r in rows if g(r, "strict_top1_accuracy") >= thr), None)
    if hit:
        print(f"  first strict>={thr:.2f}: ep{hit['epoch']}")

# Late-run regression: best strict epoch vs final
print(f"\n  best strict ep{best_strict['epoch']} = {g(best_strict,'strict_top1_accuracy'):.4f}  "
      f"vs final ep{rows[-1]['epoch']} = {strict[-1]:.4f}  "
      f"(delta={strict[-1]-g(best_strict,'strict_top1_accuracy'):+.4f})")

# Stability after best: std of strict over last 20 epochs
tail = strict[-20:]
print(f"  last-20-epoch strict: mean={mean(tail):.4f}  std={pstdev(tail):.4f}  "
      f"min={min(tail):.4f}  max={max(tail):.4f}")

# ---------------------------------------------------------------------------
# 4. Per-class confusion at best strict epoch
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"4. CONFUSION @ best strict epoch (ep{best_strict['epoch']})")
print("=" * 78)
pg = best_strict.get("per_group", {})
# oracle preset is unknown directly; infer from acceptable via top1_correct + strict.
# Instead, build confusion from the section_oracle files? We only have predictions here.
# We DO have per-group top1_preset and whether it was correct/strict.
# Build a prediction histogram and a "correct vs wrong" tally.
pred_hist = defaultdict(int)
strict_correct = 0
near_correct = 0
total = 0
for name, m in pg.items():
    total += 1
    pred_hist[m["top1_preset"]] += 1
    if m.get("strict_top1"):
        strict_correct += 1
    if m.get("top1_correct"):
        near_correct += 1
print(f"  groups={total}  strict_correct={strict_correct} ({strict_correct/total:.3f})  "
      f"near_correct={near_correct} ({near_correct/total:.3f})")
print(f"  prediction histogram: "
      + "  ".join(f"{PRESET_NAMES[k]}={pred_hist.get(k,0)}" for k in range(4)))

# near-tie-only wins (correct under near but NOT strict): the relaxation payoff
near_only = [name for name, m in pg.items()
             if m.get("top1_correct") and not m.get("strict_top1")]
print(f"  near-tie-only wins (relaxation payoff): {len(near_only)}")

# ---------------------------------------------------------------------------
# 5. Chronically-wrong sections across all epochs
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("5. CHRONICALLY-WRONG SECTIONS (strict-wrong in >=80% of epochs)")
print("=" * 78)
wrong_count = defaultdict(int)
near_wrong_count = defaultdict(int)
seen = defaultdict(int)
pred_by_sec = defaultdict(lambda: defaultdict(int))
# Only consider epochs in the converged region (after phase transition)
conv_start = next((r["epoch"] for r in rows if g(r, "strict_top1_accuracy") >= 0.70), rows[len(rows)//2]["epoch"])
conv_rows = [r for r in rows if r["epoch"] >= conv_start]
for r in conv_rows:
    for name, m in r.get("per_group", {}).items():
        seen[name] += 1
        if not m.get("strict_top1"):
            wrong_count[name] += 1
        if not m.get("top1_correct"):
            near_wrong_count[name] += 1
        pred_by_sec[name][m["top1_preset"]] += 1

print(f"  (over {len(conv_rows)} converged epochs, ep>={conv_start})")
chronic = sorted(
    [(n, wrong_count[n] / seen[n], near_wrong_count[n] / seen[n]) for n in seen if seen[n]],
    key=lambda x: -x[1],
)
n_strict_chronic = sum(1 for _, w, _ in chronic if w >= 0.80)
n_near_chronic   = sum(1 for _, _, nw in chronic if nw >= 0.80)
print(f"  strict-chronic (>=80% wrong): {n_strict_chronic}")
print(f"  near-chronic   (>=80% wrong): {n_near_chronic}  <- these survive even after relaxation")
print()
print(f"  {'strict%wrong':>11} {'near%wrong':>10}  {'mode-pred':>10}  section")
for name, w, nw in chronic[:25]:
    modep = max(pred_by_sec[name].items(), key=lambda x: x[1])[0]
    short = name.split("__")[0][:14] + "/" + name.split("::")[-1][:34]
    print(f"  {w:>11.2f} {nw:>10.2f}  {PRESET_NAMES[modep]:>10}  {short}")

# ---------------------------------------------------------------------------
# 6. Near-tie vs strict gap over time (did relaxation help?)
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("6. NEAR-TIE vs STRICT GAP (relaxation effect)")
print("=" * 78)
gaps = [(r["epoch"], g(r, "top1_accuracy") - g(r, "strict_top1_accuracy")) for r in conv_rows]
gv = [x[1] for x in gaps]
print(f"  converged near-strict gap: mean={mean(gv):.4f}  min={min(gv):.4f}  max={max(gv):.4f}")
print(f"  at best strict ep{best_strict['epoch']}: "
      f"near={g(best_strict,'top1_accuracy'):.4f} - strict={g(best_strict,'strict_top1_accuracy'):.4f} "
      f"= {g(best_strict,'top1_accuracy')-g(best_strict,'strict_top1_accuracy'):.4f}")
