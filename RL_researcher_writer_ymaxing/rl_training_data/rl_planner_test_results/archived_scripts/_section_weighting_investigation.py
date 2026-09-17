"""Investigates whether an alternative section->article reward-weighting
scheme (replacing target_words) would improve the article-level oracle
argmax, as proposed by the user: "train a lightweight model to determine
sectional weights, decoupled from section-level GRPO training."

Recomputes R_w for all 40 corpus articles under 6 weighting schemes using
already-collected section_oracle(_averaged).json + guideline_features.json
data (no new inference), and checks agreement against the final (possibly
manually-corrected) oracle_arm label -- both overall and specifically on the
10 `_MANUAL_OVERRIDES` articles where the current scheme is documented to
have needed correction.

Usage:
    python3 _section_weighting_investigation.py
"""

from __future__ import annotations

import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BASES_DIR = _HERE.parent.parent / "rl_training_data" / "bases"
_ARMS = ["skip", "light", "standard", "deep"]

# Mirrors compute_article_oracle.py::_MANUAL_OVERRIDES (see that file for the
# provenance of each correction -- A.15.2/A.15.4 majority-vote-of-replicates).
_MANUAL_OVERRIDES = {
    "06_tools__var_minimal": "skip",
    "11_multimodal__var_demanding": "standard",
    "09_RAG__var_demanding": "deep",
    "08_react_practice__var_demanding": "light",
    "11_multimodal__var_standard": "skip",
    "06_tools__var_demanding": "light",
    "Earth_Oceans_Origin": "deep",
    "Gravity_Entropy": "light",
    "13_agent_framework": "light",
    "Insects_Consciousness": "deep",
}


def _load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _compute_r_w(oracle_sections: dict, features_sections: dict, weight_fn) -> dict[str, float]:
    """Faithful reimplementation of compute_article_oracle.py::_compute_r_w,
    generalized to accept any per-section weight_fn(sec_id, feat, info) -> float
    in place of the hardcoded target_words weight."""
    acc_rest = {a: 0.0 for a in _ARMS}
    acc_explore = {a: 0.0 for a in _ARMS}
    total_w = 0.0
    n_sections = 0
    has_explore = False
    for sec_id, info in oracle_sections.items():
        rewards = info["rewards"]
        explore = info.get("explore")
        feat = features_sections.get(sec_id, {})
        w = weight_fn(sec_id, feat, info)
        total_w += w
        n_sections += 1
        for arm in _ARMS:
            total_reward = float(rewards.get(arm, 0.0))
            if explore is not None:
                has_explore = True
                explore_val = float(explore.get(arm, 0.0))
                acc_rest[arm] += w * (total_reward - explore_val)
                acc_explore[arm] += explore_val
            else:
                acc_rest[arm] += w * total_reward
    if total_w == 0:
        return {a: 0.0 for a in _ARMS}
    if has_explore:
        return {a: (acc_rest[a] / total_w) + (acc_explore[a] / n_sections) for a in _ARMS}
    return {a: acc_rest[a] / total_w for a in _ARMS}


def _w_target_words(sec_id, feat, info):
    tw = feat.get("target_words")
    return float(tw) if tw is not None else 100.0


def _w_uniform(sec_id, feat, info):
    return 1.0


def _w_must_cover_depth(sec_id, feat, info):
    return float(feat.get("must_cover_depth", 0)) + 1.0


def _w_mandatory_bullets(sec_id, feat, info):
    return float(feat.get("mandatory_bullets", 0)) + 1.0


def _w_margin(sec_id, feat, info):
    """Weight a section by how decisive its OWN top-vs-runner-up reward gap
    is -- an analog of the training-side confidence weighting (A.16.7's
    --section-weight confidence), applied at the aggregation step instead."""
    vals = sorted(info["rewards"].values(), reverse=True)
    margin = vals[0] - vals[1] if len(vals) > 1 else 0.0
    return max(margin, 0.001)


def _w_tw_times_margin(sec_id, feat, info):
    return _w_target_words(sec_id, feat, info) * _w_margin(sec_id, feat, info)


SCHEMES = {
    "target_words (current)": _w_target_words,
    "uniform": _w_uniform,
    "must_cover_depth": _w_must_cover_depth,
    "mandatory_bullets": _w_mandatory_bullets,
    "margin (confidence)": _w_margin,
    "target_words x margin": _w_tw_times_margin,
}


def run(corpus: list[str]) -> None:
    results = {name: {"agree": 0, "n": 0, "override_hits": []} for name in SCHEMES}

    for variant in corpus:
        vdir = _BASES_DIR / variant
        oracle_data = _load_json(vdir / "section_oracle_averaged.json") or _load_json(vdir / "section_oracle.json")
        if oracle_data is None:
            continue
        oracle_sections = oracle_data["sections"]
        gf = _load_json(vdir / "guideline_features.json") or {}
        features_sections = gf.get("sections", {})
        ao = _load_json(vdir / "article_oracle_averaged.json") or _load_json(vdir / "article_oracle.json")
        final_label = ao.get("oracle_arm") if ao else None

        for name, fn in SCHEMES.items():
            r_w = _compute_r_w(oracle_sections, features_sections, fn)
            argmax = max(r_w, key=r_w.get)
            results[name]["n"] += 1
            if argmax == final_label:
                results[name]["agree"] += 1
            if variant in _MANUAL_OVERRIDES:
                correct = _MANUAL_OVERRIDES[variant]
                results[name]["override_hits"].append((variant, argmax, correct, argmax == correct))

    print(f"{'scheme':25s} {'agree w/ final label':>22s}")
    for name, res in results.items():
        print(f"{name:25s} {res['agree']}/{res['n']} = {100 * res['agree'] / res['n']:.1f}%")

    print("\n=== raw argmax vs corrected truth on the 10 known override cases ===")
    for name, res in results.items():
        hits = sum(1 for *_, ok in res["override_hits"] if ok)
        print(f"{name}: {hits}/{len(res['override_hits'])} correct without needing an override")


if __name__ == "__main__":
    import sys
    stage0_table = Path("/tmp/stage0_table.json")
    if stage0_table.exists():
        corpus = [r["variant"] for r in json.loads(stage0_table.read_text())]
    else:
        print("Run _stage0_residual_error_feature_audit.py first to build the corpus list.", file=sys.stderr)
        sys.exit(1)
    run(corpus)
