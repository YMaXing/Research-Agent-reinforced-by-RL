"""Thorough analysis of run06 GRPO training time series + failure modes.

Reads training_log.jsonl (per-epoch + per-group) and section_oracle.json
ground-truth labels, then reports:
  1. Best checkpoints (strict top1, near-tie top1, mean reward) + epochs.
  2. Temporal evolution of key scalars.
  3. Confusion matrices (overall + per variant) at the best strict epoch.
  4. Failure/miss breakdown correlated with variant.
  5. Actionable recommendations.
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing")
RUN_DIR = ROOT / "rl_training_data/checkpoints/tasks/run06"
LOG = RUN_DIR / "training_log.jsonl"
BASES = ROOT / "rl_training_data/bases"

PRESET_NAMES = ["skip", "light", "standard", "deep"]


def load_log() -> list[dict]:
    rows = []
    with open(LOG, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def variant_of(group_name: str) -> str:
    # e.g. "02_workflows_vs_agents__var_minimal__S1::..."
    if "__var_minimal" in group_name:
        return "minimal"
    if "__var_standard" in group_name:
        return "standard"
    if "__var_demanding" in group_name:
        return "demanding"
    return "unknown"


def build_oracle_map() -> dict[str, int]:
    """Map full log group key (article__var_X__S#::slug) -> oracle preset idx.

    section_oracle.json 'sections' is a dict keyed by 'S#::slug' with each
    value carrying an 'oracle' label; the log group key prepends the
    article__var_variant directory name.
    """
    name_to_idx = {n: i for i, n in enumerate(PRESET_NAMES)}
    oracle: dict[str, int] = {}
    for d in sorted(BASES.glob("*__var_*")):
        f = d / "section_oracle.json"
        if not f.exists():
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        article_var = d.name  # e.g. 02_workflows_vs_agents__var_minimal
        sections = data.get("sections", {})
        for sid, sec in sections.items():
            lab = sec.get("oracle") if isinstance(sec, dict) else sec
            idx = name_to_idx.get(lab)
            if idx is not None:
                oracle[f"{article_var}__{sid}"] = idx
    return oracle


def group_base_key(full_name: str) -> str:
    # strip the "::section-slug" suffix
    return full_name.split("::", 1)[0]


def main() -> None:
    rows = load_log()
    print(f"Loaded {len(rows)} epochs from {LOG.name}\n")

    # ---- 1. Best checkpoints ----
    best_strict = max(rows, key=lambda r: r["strict_top1_accuracy"])
    best_neartie = max(rows, key=lambda r: r["top1_accuracy"])
    best_reward = max(rows, key=lambda r: r["mean_expected_reward"])

    print("=" * 70)
    print("1. BEST CHECKPOINTS")
    print("=" * 70)
    for label, r, key in [
        ("strict top-1 acc", best_strict, "strict_top1_accuracy"),
        ("near-tie top-1 acc", best_neartie, "top1_accuracy"),
        ("mean reward E[R]", best_reward, "mean_expected_reward"),
    ]:
        print(f"  {label:22s}: epoch {r['epoch']:>4d}  value={r[key]:.4f}  "
              f"(E[R]={r['mean_expected_reward']:.4f}, "
              f"strict={r['strict_top1_accuracy']:.4f}, "
              f"near-tie={r['top1_accuracy']:.4f}, H={r['mean_entropy']:.3f})")

    # ---- 2. Temporal evolution ----
    print("\n" + "=" * 70)
    print("2. TEMPORAL EVOLUTION (sampled every ~15 epochs)")
    print("=" * 70)
    cols = ["epoch", "loss_total", "loss_grpo", "loss_kl", "mean_kl",
            "grad_norm", "mean_expected_reward", "top1_accuracy",
            "strict_top1_accuracy", "mean_entropy", "sigma_floor_fraction"]
    hdr = ["ep", "loss", "grpo", "kl", "mKL", "‖g‖", "E[R]", "near", "strict", "H", "σflr"]
    print("  " + " ".join(f"{h:>7s}" for h in hdr))
    step = max(1, len(rows) // 12)
    for r in rows[::step] + [rows[-1]]:
        vals = [r["epoch"], r["loss_total"], r["loss_grpo"], r["loss_kl"],
                r["mean_kl"], r["grad_norm"], r["mean_expected_reward"],
                r["top1_accuracy"], r["strict_top1_accuracy"],
                r["mean_entropy"], r["sigma_floor_fraction"]]
        print("  " + " ".join(f"{v:>7.3f}" if isinstance(v, float) else f"{v:>7d}" for v in vals))

    # entropy collapse detection
    h0, hlast = rows[0]["mean_entropy"], rows[-1]["mean_entropy"]
    print(f"\n  Entropy: {h0:.3f} (ep0) -> {hlast:.3f} (ep{rows[-1]['epoch']})  "
          f"Δ={hlast-h0:+.3f}")
    print(f"  Peak strict acc {best_strict['strict_top1_accuracy']:.4f} at epoch {best_strict['epoch']}; "
          f"final {rows[-1]['strict_top1_accuracy']:.4f}")

    # ---- 3 & 4. Confusion + failure analysis at best strict epoch ----
    oracle = build_oracle_map()
    print(f"\n  (oracle map covers {len(oracle)} sections)")

    target_epoch = best_strict
    pg = target_epoch["per_group"]

    # overall + per-variant confusion: rows=oracle(true), cols=pred(top1)
    def fresh_cm():
        return [[0] * 4 for _ in range(4)]

    cm_all = fresh_cm()
    cm_var = {v: fresh_cm() for v in ("minimal", "standard", "demanding")}
    matched = 0
    unmatched = []
    for gname, gm in pg.items():
        base = gname
        if base not in oracle:
            unmatched.append(base)
            continue
        true_i = oracle[base]
        pred_i = gm["top1_preset"]
        cm_all[true_i][pred_i] += 1
        cm_var[variant_of(gname)][true_i][pred_i] += 1
        matched += 1

    print("\n" + "=" * 70)
    print(f"3. CONFUSION MATRIX @ best-strict epoch {target_epoch['epoch']} "
          f"({matched} sections matched to oracle)")
    print("=" * 70)
    if unmatched:
        print(f"  WARNING: {len(unmatched)} groups unmatched to oracle, e.g. {unmatched[:3]}")

    def print_cm(cm, title):
        print(f"\n  --- {title} ---")
        print("  true\\pred  " + " ".join(f"{n:>9s}" for n in PRESET_NAMES) + "   recall")
        total = sum(sum(r) for r in cm)
        diag = sum(cm[i][i] for i in range(4))
        for i in range(4):
            rsum = sum(cm[i])
            rec = cm[i][i] / rsum if rsum else float("nan")
            print(f"  {PRESET_NAMES[i]:>9s}  " +
                  " ".join(f"{cm[i][j]:>9d}" for j in range(4)) +
                  f"   {rec:.2f} ({cm[i][i]}/{rsum})")
        # precision row
        prec = []
        for j in range(4):
            csum = sum(cm[i][j] for i in range(4))
            prec.append(cm[j][j] / csum if csum else float("nan"))
        print("  precision  " + " ".join(f"{p:>9.2f}" for p in prec))
        acc = diag / total if total else float("nan")
        print(f"  accuracy = {acc:.3f} ({diag}/{total})")

    print_cm(cm_all, "OVERALL")
    for v in ("minimal", "standard", "demanding"):
        print_cm(cm_var[v], f"VARIANT = {v}")

    # ---- 4. Failure mode breakdown ----
    print("\n" + "=" * 70)
    print("4. FAILURE MODES (oracle != top1) @ best-strict epoch, by variant")
    print("=" * 70)
    miss_by_var = defaultdict(lambda: defaultdict(int))
    miss_examples = defaultdict(list)
    for gname, gm in pg.items():
        base = gname
        if base not in oracle:
            continue
        true_i = oracle[base]
        pred_i = gm["top1_preset"]
        if true_i != pred_i:
            v = variant_of(gname)
            key = f"{PRESET_NAMES[true_i]}->{PRESET_NAMES[pred_i]}"
            miss_by_var[v][key] += 1
            if len(miss_examples[v + "|" + key]) < 3:
                miss_examples[v + "|" + key].append(
                    (base.split("__")[0], gm["expected_reward"],
                     [round(p, 2) for p in gm["action_probs"]]))
    for v in ("minimal", "standard", "demanding"):
        total_miss = sum(miss_by_var[v].values())
        print(f"\n  {v}: {total_miss} misses")
        for key, c in sorted(miss_by_var[v].items(), key=lambda x: -x[1]):
            print(f"    {key:24s} x{c}")
            for art, er, ap in miss_examples[v + '|' + key]:
                print(f"        e.g. {art:32s} E[R]={er:.2f} probs={ap}")

    # ---- skip-specific tracking across time ----
    print("\n" + "=" * 70)
    print("5. SKIP RECALL OVER TIME (oracle=skip sections only)")
    print("=" * 70)
    skip_bases = {b for b, i in oracle.items() if i == 0}
    print(f"  {len(skip_bases)} oracle=skip sections total")
    step2 = max(1, len(rows) // 12)
    print("  epoch  skip_recall  pred_skip_count  (of oracle-skip)")
    for r in rows[::step2] + [rows[-1]]:
        pg2 = r["per_group"]
        hit = tot = 0
        for gname, gm in pg2.items():
            base = gname
            if base in skip_bases:
                tot += 1
                if gm["top1_preset"] == 0:
                    hit += 1
        rec = hit / tot if tot else float("nan")
        print(f"  {r['epoch']:>5d}     {rec:.3f}        {hit}/{tot}")


if __name__ == "__main__":
    main()
