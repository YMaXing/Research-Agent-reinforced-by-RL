"""Margin analysis of misses at best-strict epoch (epoch 129) for run06.

For every section where top1_preset != oracle:
  reward_margin     = R[oracle] - R[predicted]   (how much reward was left on table)
  prob_margin       = P[oracle] - P[predicted]   (model confidence displacement)
  oracle_gap        = R[oracle] - second_best_R  (how clear the oracle label is)
  rewards_std       = std(R[all 4])              (group difficulty / separability)

Reports:
  A) Distribution of reward_margin by miss type and variant
  B) Scatter: hard misses (large reward_margin) vs soft misses (near-tie)
  C) Deep-specific miss anatomy
  D) Per-article deep-oracle sections with full reward arrays
"""
from __future__ import annotations

import json
import math
import glob
from collections import defaultdict
from pathlib import Path

ROOT = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing")
RUN_DIR = ROOT / "rl_training_data/checkpoints/tasks/run06"
LOG = RUN_DIR / "training_log.jsonl"
BASES = ROOT / "rl_training_data/bases"
PRESET_NAMES = ["skip", "light", "standard", "deep"]
BEST_EPOCH = 129


def load_epoch(target: int) -> dict:
    with open(LOG, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if r["epoch"] == target:
                return r
    raise ValueError(f"epoch {target} not found")


def build_oracle_data() -> dict[str, dict]:
    """Full oracle data: group_key -> {oracle_idx, rewards:[4 floats]}"""
    name_to_idx = {n: i for i, n in enumerate(PRESET_NAMES)}
    out: dict[str, dict] = {}
    for f in glob.glob(str(BASES / "*__var_*" / "section_oracle.json")):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        article_var = Path(f).parent.name
        for sid, sec in d.get("sections", {}).items():
            key = f"{article_var}__{sid}"
            rewards_raw = sec.get("rewards", {})
            rewards_list = [float(rewards_raw.get(n, 0.0)) for n in PRESET_NAMES]
            oracle_idx = name_to_idx.get(sec.get("oracle"), -1)
            out[key] = {
                "oracle_idx": oracle_idx,
                "rewards": rewards_list,
                "variant": d.get("variant", "?"),
                "article": d.get("article", "?"),
                "sid": sid,
            }
    return out


def std4(vals):
    mu = sum(vals) / 4
    return math.sqrt(sum((v - mu) ** 2 for v in vals) / 4)


def fmt_probs(p):
    return "[" + ", ".join(f"{x:.2f}" for x in p) + "]"


def fmt_rewards(r):
    return "[" + ", ".join(f"{x:.2f}" for x in r) + "]"


def main():
    epoch_data = load_epoch(BEST_EPOCH)
    pg = epoch_data["per_group"]
    oracle_data = build_oracle_data()

    print(f"Margin analysis @ epoch {BEST_EPOCH}  ({len(pg)} groups, {len(oracle_data)} in oracle)\n")

    # ── collect all misses ──────────────────────────────────────────────
    misses = []
    hits = []
    for gname, gm in pg.items():
        if gname not in oracle_data:
            continue
        od = oracle_data[gname]
        true_i = od["oracle_idx"]
        pred_i = gm["top1_preset"]
        probs = gm["action_probs"]
        rewards = od["rewards"]
        r_oracle = rewards[true_i]
        r_pred = rewards[pred_i]
        reward_margin = r_oracle - r_pred        # >0 means we left reward on table
        prob_margin = probs[true_i] - probs[pred_i]  # <0 means model strongly prefers wrong
        oracle_gap = r_oracle - sorted(rewards, reverse=True)[1]  # gap to 2nd best
        g_std = std4(rewards)
        rec = {
            "name": gname,
            "article": od["article"],
            "variant": od["variant"],
            "sid": od["sid"],
            "true_i": true_i,
            "pred_i": pred_i,
            "true_name": PRESET_NAMES[true_i],
            "pred_name": PRESET_NAMES[pred_i],
            "miss_type": f"{PRESET_NAMES[true_i]}->{PRESET_NAMES[pred_i]}",
            "rewards": rewards,
            "r_oracle": r_oracle,
            "r_pred": r_pred,
            "reward_margin": reward_margin,
            "prob_margin": prob_margin,
            "oracle_gap": oracle_gap,
            "g_std": g_std,
            "probs": probs,
            "expected_reward": gm["expected_reward"],
        }
        if true_i != pred_i:
            misses.append(rec)
        else:
            hits.append(rec)

    n_total = len(misses) + len(hits)
    print(f"Correct: {len(hits)}/{n_total}  |  Misses: {len(misses)}/{n_total}\n")

    # ── A) Margin distribution summary ─────────────────────────────────
    SIGMA = 0.05   # near-tie threshold
    hard = [m for m in misses if m["reward_margin"] > SIGMA]
    soft = [m for m in misses if 0 < m["reward_margin"] <= SIGMA]
    gain = [m for m in misses if m["reward_margin"] <= 0]  # pred >= oracle (near-tie wins)

    print("=" * 70)
    print("A) MISS SEVERITY BREAKDOWN  (σ_floor = 0.05)")
    print("=" * 70)
    print(f"  Hard misses (margin > 0.05) : {len(hard):>3d}  ({len(hard)/len(misses):.0%})")
    print(f"  Soft misses (0 < margin ≤0.05): {len(soft):>3d}  ({len(soft)/len(misses):.0%})")
    print(f"  Gain / near-tie (margin ≤ 0): {len(gain):>3d}  ({len(gain)/len(misses):.0%})")

    def margin_stats(lst, label):
        if not lst:
            print(f"  {label}: (none)")
            return
        margins = [m["reward_margin"] for m in lst]
        print(f"  {label}: n={len(lst)}  "
              f"mean={sum(margins)/len(margins):.3f}  "
              f"min={min(margins):.3f}  max={max(margins):.3f}")

    margin_stats(hard, "hard ")
    margin_stats(soft, "soft ")
    margin_stats(gain, "gain ")

    # ── B) Breakdown by miss type + variant ────────────────────────────
    print("\n" + "=" * 70)
    print("B) MISS TYPE × SEVERITY × VARIANT")
    print("=" * 70)
    by_type: dict[str, list] = defaultdict(list)
    for m in misses:
        by_type[m["miss_type"]].append(m)

    for mtype, lst in sorted(by_type.items(), key=lambda x: -len(x[1])):
        margins = [m["reward_margin"] for m in lst]
        h = sum(1 for m in margins if m > SIGMA)
        s = sum(1 for m in margins if 0 < m <= SIGMA)
        g = sum(1 for m in margins if m <= 0)
        var_counts = defaultdict(int)
        for m in lst:
            var_counts[m["variant"]] += 1
        var_str = "  ".join(f"{k}:{v}" for k, v in sorted(var_counts.items()))
        print(f"\n  {mtype:22s}  n={len(lst):>2d}  "
              f"hard={h} soft={s} gain={g}  "
              f"mean_margin={sum(margins)/len(margins):.3f}  [{var_str}]")
        # Print each instance
        for m in sorted(lst, key=lambda x: -x["reward_margin"]):
            print(f"    {m['article']:35s} {m['sid'].split('::')[0]}  "
                  f"R={fmt_rewards(m['rewards'])}  "
                  f"margin={m['reward_margin']:+.3f}  "
                  f"P={fmt_probs(m['probs'])}  "
                  f"var={m['variant']}")

    # ── C) Deep-oracle miss anatomy ─────────────────────────────────────
    print("\n" + "=" * 70)
    print("C) DEEP-ORACLE SECTIONS — FULL ANATOMY (all 18, sorted by margin)")
    print("=" * 70)
    deep_all = [v for v in oracle_data.values() if v["oracle_idx"] == 3]
    # get their epoch-129 prediction
    art_var_to_pred: dict[str, dict] = {}
    for gname, gm in pg.items():
        art_var_to_pred[gname] = gm

    print(f"  {'article':35s} {'var':10s} {'sid':4s}  {'rewards (s,l,st,dp)':28s}  "
          f"{'oracle_gap':>11s}  {'g_std':>6s}  {'pred':>8s}  {'margin':>7s}  probs")
    for od in sorted(deep_all, key=lambda x: (x["variant"], x["article"])):
        base = f"{Path(od['article']).name if '/' not in od['article'] else od['article']}"
        # reconstruct oracle key prefix
        found_key = None
        for gname in pg:
            if od["article"] in gname and od["sid"] in gname:
                found_key = gname
                break
        if found_key is None:
            continue
        gm = pg[found_key]
        pred_i = gm["top1_preset"]
        r = od["rewards"]
        margin = r[3] - r[pred_i]
        oracle_gap = r[3] - sorted(r, reverse=True)[1]
        g_std = std4(r)
        print(f"  {od['article']:35s} {od['variant']:10s} {od['sid'].split('::')[0]:4s}  "
              f"R={fmt_rewards(r)}  "
              f"gap={oracle_gap:+.3f}  "
              f"std={g_std:.3f}  "
              f"pred={PRESET_NAMES[pred_i]:8s}  "
              f"margin={margin:+.3f}  "
              f"P={fmt_probs(gm['action_probs'])}")

    # ── D) Hit margin distribution — are correct answers also confident? ──
    print("\n" + "=" * 70)
    print("D) HIT CONFIDENCE CHECK (correct predictions)")
    print("=" * 70)
    hit_probs = [h["probs"][h["true_i"]] for h in hits]
    low_conf = [h for h in hits if h["probs"][h["true_i"]] < 0.5]
    print(f"  Correct preds: {len(hits)}  mean P[oracle]={sum(hit_probs)/len(hit_probs):.3f}")
    print(f"  Low-confidence correct (P[oracle]<0.5): {len(low_conf)}")
    for h in sorted(low_conf, key=lambda x: x["probs"][x["true_i"]]):
        print(f"    {h['article']:35s} {h['sid'].split('::')[0]:4s}  "
              f"oracle={h['true_name']:8s}  P[oracle]={h['probs'][h['true_i']]:.3f}  "
              f"R={fmt_rewards(h['rewards'])}  var={h['variant']}")

    # ── E) Reward margin histogram (text) ──────────────────────────────
    print("\n" + "=" * 70)
    print("E) REWARD MARGIN HISTOGRAM (all misses)")
    print("=" * 70)
    buckets = [(-1.0, -0.1), (-0.1, 0.0), (0.0, 0.05), (0.05, 0.1),
               (0.1, 0.2), (0.2, 0.3), (0.3, 0.5), (0.5, 1.01)]
    for lo, hi in buckets:
        cnt = sum(1 for m in misses if lo <= m["reward_margin"] < hi)
        bar = "█" * cnt
        label = f"[{lo:+.2f},{hi:+.2f})"
        print(f"  {label:16s}  {cnt:>3d}  {bar}")

    # ── F) Deep-oracle margin histogram across training epochs ──────────
    print("\n" + "=" * 70)
    print("F) DEEP-ORACLE SECTION EXPECTED_REWARD ACROSS EPOCHS (sampled)")
    print("=" * 70)
    rows = [json.loads(l) for l in open(LOG, encoding="utf-8") if l.strip()]
    deep_keys = [gname for gname in rows[0]["per_group"] if oracle_data.get(gname, {}).get("oracle_idx") == 3]
    print(f"  {len(deep_keys)} deep-oracle sections tracked")
    step = max(1, len(rows) // 10)
    header = "  epoch  " + "  ".join(f"{k.split('__')[1][:3]}{k.split('__')[2][:3]}" for k in deep_keys[:8])
    print(header)
    for r in rows[::step] + [rows[-1]]:
        vals = []
        for k in deep_keys[:8]:
            gm = r["per_group"].get(k, {})
            pred_i = gm.get("top1_preset", -1)
            er = gm.get("expected_reward", 0.0)
            marker = "D" if pred_i == 3 else PRESET_NAMES[pred_i][0].upper() if pred_i >= 0 else "?"
            vals.append(f"{marker}({er:.2f})")
        print(f"  {r['epoch']:>5d}  " + "  ".join(f"{v:>8s}" for v in vals))

    print("\nLegend: D=deep(correct) S=skip L=light T=standard  value=expected_reward at that epoch")


if __name__ == "__main__":
    main()
