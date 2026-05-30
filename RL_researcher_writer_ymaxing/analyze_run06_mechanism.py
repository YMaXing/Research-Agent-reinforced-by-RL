"""Quantify the TRUE mechanism behind deep-collapse in run06.

The GRPO loss here is analytic advantage-weighted cross-entropy:
    loss_grpo = -(1/4) Σ_a A_a · log π_a
With mean-centred advantages (Σ_a A_a = 0), the gradient on logit z_k is:
    ∂loss/∂z_k = -(1/4) A_k        (CONSTANT in π_k — does NOT vanish)
So gradient descent raises z_deep by (lr/4)·A_deep every step for a
deep-oracle section, regardless of how small π_deep is.

This script measures, per oracle class:
  - count, total normalized word_weight (the loss weight actually applied)
  - the NET aggregate pull on each logit: Σ_s w_s · A_s,k
    (positive = sections collectively push that logit UP)
  - effective class weights under current scheme vs sqrt-inverse-frequency
to show whether the deep logit is out-pulled by the majority classes.
"""
from __future__ import annotations
import json, glob, math
from pathlib import Path
from collections import defaultdict

ROOT = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing")
BASES = ROOT / "rl_training_data/bases"
PRESET_NAMES = ["skip", "light", "standard", "deep"]
SIGMA_FLOOR = 0.04   # train_grpo default --sigma-floor
N_ARTICLES_GUESS = None  # computed below


def variant_level(variant_field: str) -> str:
    v = variant_field.replace("var_", "")
    return v


def load_groups():
    """Replicate load_section_groups advantage + weight logic (hybrid default)."""
    articles = defaultdict(list)  # article -> list of group dicts
    for f in glob.glob(str(BASES / "*__var_*" / "section_oracle.json")):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        article_dir = Path(f).parent.name
        variant = variant_level(d.get("variant", ""))
        for sid, sec in d.get("sections", {}).items():
            rwd = sec.get("rewards", {})
            rewards = [float(rwd.get(n, 0.0)) for n in PRESET_NAMES]
            wcount = sec.get("word_count", sec.get("words", 100))
            mx, mn = max(rewards), min(rewards)
            if mx - mn < SIGMA_FLOOR:
                continue  # dropped flat group
            mean_r = sum(rewards) / 4
            raw_std = math.sqrt(sum((r - mean_r) ** 2 for r in rewards) / 4)
            std_r = max(raw_std, SIGMA_FLOOR)
            adv = [(r - mean_r) / std_r for r in rewards]
            best = rewards.index(mx)
            articles[article_dir].append({
                "variant": variant,
                "oracle": PRESET_NAMES[best],
                "best_idx": best,
                "adv": adv,
                "raw_std": raw_std,
                "regret": mx - mean_r,
                "wcount": float(wcount),
            })
    return articles


def apply_weights(articles, mode="hybrid", use_variant_3x=True, class_w=None):
    """Return flat list of (group, normalized_weight) replicating train logic."""
    n_articles = len(articles)
    flat = []
    for article, groups in articles.items():
        if mode == "hybrid":
            raw = [g["wcount"] * g["raw_std"] for g in groups]
        elif mode == "regret-hybrid":
            raw = [g["wcount"] * g["regret"] for g in groups]
        elif mode == "wordcount":
            raw = [g["wcount"] for g in groups]
        else:
            raw = [1.0] * len(groups)

        if use_variant_3x:
            new = []
            for g, rw in zip(groups, raw):
                v = g["variant"]
                anti = ({"standard", "deep"} if v == "minimal"
                        else {"skip", "light"} if v == "demanding" else set())
                new.append(rw * (3.0 if g["oracle"] in anti else 1.0))
            raw = new
        if class_w is not None:
            raw = [rw * class_w[g["oracle"]] for g, rw in zip(groups, raw)]

        tot = sum(raw) or len(groups)
        if sum(raw) == 0:
            raw = [1.0] * len(groups)
            tot = len(groups)
        for g, rw in zip(groups, raw):
            flat.append((g, rw / tot / n_articles))
    return flat


def analyze(flat, label):
    cls_w = defaultdict(float)
    cls_n = defaultdict(int)
    pull = [0.0, 0.0, 0.0, 0.0]  # Σ_s w_s · A_s,k
    deep_pull_pos = 0.0
    deep_pull_neg = 0.0
    for g, w in flat:
        cls_w[g["oracle"]] += w
        cls_n[g["oracle"]] += 1
        for k in range(4):
            pull[k] += w * g["adv"][k]
        a_deep = w * g["adv"][3]
        if a_deep >= 0:
            deep_pull_pos += a_deep
        else:
            deep_pull_neg += a_deep
    print(f"\n=== {label} ===")
    print(f"  class counts:  " + "  ".join(f"{n}:{cls_n[n]}" for n in PRESET_NAMES))
    tw = sum(cls_w.values())
    print(f"  class weight%: " + "  ".join(f"{n}:{100*cls_w[n]/tw:.1f}%" for n in PRESET_NAMES))
    print(f"  NET logit pull (Σ w·A): " +
          "  ".join(f"{n}:{pull[k]:+.4f}" for k, n in enumerate(PRESET_NAMES)))
    print(f"  deep logit: +pull(deep-good secs)={deep_pull_pos:+.4f}  "
          f"-pull(deep-bad secs)={deep_pull_neg:+.4f}  net={pull[3]:+.4f}")


def main():
    articles = load_groups()
    n_groups = sum(len(v) for v in articles.values())
    print(f"Articles: {len(articles)}  groups (after flat-drop): {n_groups}")

    # Verify Σ_a A_a = 0
    bad = 0
    for groups in articles.values():
        for g in groups:
            if abs(sum(g["adv"])) > 1e-6:
                bad += 1
    print(f"Advantage zero-sum check: {bad} groups violate Σ_a A_a=0 (expect 0)")

    # class counts (pre-weight)
    cc = defaultdict(int)
    for groups in articles.values():
        for g in groups:
            cc[g["oracle"]] += 1
    total = sum(cc.values())
    print(f"Oracle class balance: " + "  ".join(f"{n}:{cc[n]}({100*cc[n]/total:.0f}%)" for n in PRESET_NAMES))

    # 1) Current run06 scheme: hybrid + variant 3x
    flat_cur = apply_weights(articles, "hybrid", use_variant_3x=True)
    analyze(flat_cur, "CURRENT run06: hybrid × variant-3x")

    # 2) regret-hybrid + variant 3x
    flat_reg = apply_weights(articles, "regret-hybrid", use_variant_3x=True)
    analyze(flat_reg, "ALT: regret-hybrid × variant-3x")

    # 3) sqrt inverse-frequency class weights (replace variant-3x)
    inv_sqrt = {n: math.sqrt(total / (4 * cc[n])) if cc[n] else 0 for n in PRESET_NAMES}
    print("\n  sqrt-inv-freq class multipliers:", {n: round(inv_sqrt[n], 2) for n in PRESET_NAMES})
    flat_invs = apply_weights(articles, "hybrid", use_variant_3x=False, class_w=inv_sqrt)
    analyze(flat_invs, "ALT: hybrid × sqrt-inverse-frequency (no variant-3x)")

    # 4) full inverse-frequency
    inv = {n: (total / (4 * cc[n])) if cc[n] else 0 for n in PRESET_NAMES}
    print("\n  full-inv-freq class multipliers:", {n: round(inv[n], 2) for n in PRESET_NAMES})
    flat_inv = apply_weights(articles, "hybrid", use_variant_3x=False, class_w=inv)
    analyze(flat_inv, "ALT: hybrid × full-inverse-frequency")

    # 5) combined: regret-hybrid × variant-3x × sqrt-inv-freq
    flat_combo = apply_weights(articles, "regret-hybrid", use_variant_3x=True, class_w=inv_sqrt)
    analyze(flat_combo, "ALT: regret-hybrid × variant-3x × sqrt-inv-freq")

    # 6) RECOMMENDED: hybrid × variant-3x × full-inv-freq
    flat_rec = apply_weights(articles, "hybrid", use_variant_3x=True, class_w=inv)
    analyze(flat_rec, "RECOMMENDED: hybrid × variant-3x × full-inverse-frequency")


if __name__ == "__main__":
    main()
