"""A.15.4 follow-up: does TEST show the same ga (guideline_adherence) cross-
draft mean-drop found for TRAIN (Sec59.5: 0.740->0.412 under N=3 averaging),
and if so, does lowering the ga gate threshold (shipped default 0.5, see
generate_episode_oracles.py::_ga_gate_penalty) stabilize the 12 CRITICAL/HIGH
TEST articles' label landscape from A.15.4 (5 confirmed / 4 corrected / 3
unresolved 3-way splits under the shipped threshold)?

Read-only, zero LLM calls, zero writes. Inline-copies _section_reward's
formula terms (matching sweep_reward_formula.py's established "inline
copy, parameterised by cfg" pattern for formula experiments) rather than
modifying generate_episode_oracles.py; only the ga gate threshold varies
across candidates, everything else (gt_base/explore/cost) is the shipped
C2 formula.

Usage (from research_agent_local/):
  python3 training/_test_ga_gate_threshold_sweep.py
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import compute_article_oracle as cao  # noqa: E402
import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402

_TEST_ARTICLES = [
    "Earth_Oceans_Origin", "Gravity_Entropy", "Dark_Dimension",
    "14_agent_system_design", "07_reasoning_planning", "Distinct_AI_Models",
    "04_structured_outputs", "Space-Time_QECC", "13_agent_framework",
    "Bird_Eye_Extreme", "Understanding_Reasoning_LLMs", "Insects_Consciousness",
]

DIMS = {
    "cc": "ground_truth_core_content", "fl": "ground_truth_flow",
    "de": "ground_truth_depth_enhancement", "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation", "ga": "user_intent_guideline_adherence",
}
ENH = {"de", "be"}
ARM_ORDER = mrn._ARM_ORDER

# shipped C2 constants (see generate_episode_oracles.py::_section_reward) --
# only ga_gate_threshold is varied by this script.
_COST_COEF = -0.03
_DE_WEIGHT = 0.45
_BE_WEIGHT = 0.30
_GA_GATE_PENALTY = -0.10


def _load_reasoning(d: Path):
    p = d / "reasoning.json"
    if not p.exists():
        p = d / "reasons.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return {k: geo._parse_sections_ordered(data[k]) for k in data if isinstance(data.get(k), str)}


def _draw_vals(entries_by_dim, snorm, idx):
    vals = {}
    for short, dim in DIMS.items():
        entries = entries_by_dim.get(dim, [])
        if short in ENH:
            enh = geo._get_enhancement(entries, snorm, idx)
            vals[short] = geo._get_score(entries, snorm, idx) if enh is None else enhancement_credit(enh[1])
        else:
            vals[short] = geo._get_score(entries, snorm, idx)
    return vals


def _load_article_draws(article: str):
    """Return (sec_ids, {draw_label: {sec_id: {arm: vals_dict or None}}}).

    Iterates production's own digest-ordered sec_id list (duplicates INCLUDED) so
    _get_score's ordinal fallback matches production; a deduped list diverges on
    ~9% of cells (analysis md A.15.4, 2026-08-20).
    """
    so = json.loads((mrn._BASES_DIR / article / "section_oracle.json").read_text(encoding="utf-8"))
    oracle_keys = list(so["sections"].keys())
    digest_path = mrn._BASES_DIR / article / "research_digest.md"
    sec_ids = geo._extract_sec_ids_ordered(digest_path.read_text(encoding="utf-8")) \
        if digest_path.exists() else []
    if not sec_ids or not set(oracle_keys).issubset(set(sec_ids)):
        sec_ids = oracle_keys
    sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]
    arm_presets = mrn._arm_presets_for(article)
    nr_units = geo._ARM_COST_UNITS

    def _one_draw(episode_by_arm: dict):
        out = {}
        for idx, (sid, snorm) in enumerate(zip(sec_ids, sec_norms)):
            out[sid] = {}
            for arm in ARM_ORDER:
                ep = episode_by_arm.get(arm)
                out[sid][arm] = _draw_vals(ep, snorm, idx) if ep is not None else None
        return out

    draws = {}
    prod_by_arm = {}
    for arm, pids in arm_presets.items():
        ep_dir = geo._TEST_EPISODES_DIR / f"{article}__preset{pids[0]}"
        if not ep_dir.exists():
            ep_dir = geo._EPISODES_DIR / f"{article}__preset{pids[0]}"
        prod_by_arm[arm] = _load_reasoning(ep_dir)
    draws["production"] = _one_draw(prod_by_arm)

    for r in (1, 2):
        prefix = mrn._NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}"
        rep_by_arm = {}
        found = False
        for arm, pids in arm_presets.items():
            ep_dir = Path(f"{prefix}__preset{pids[0]}")
            rep = _load_reasoning(ep_dir) if ep_dir.exists() else None
            if rep is not None:
                found = True
            rep_by_arm[arm] = rep
        if found:
            draws[f"replicate{r}"] = _one_draw(rep_by_arm)

    return sec_ids, draws, nr_units


def _section_reward_at(vals: dict, nr: float, ga_threshold: float) -> tuple[float, float]:
    """Returns (total, explore) -- total == gt_base + explore + gate + cost,
    explore stored separately so cao._compute_r_w() can apply Candidate E's
    simple-mean-explore aggregation identically to production section_oracle.json."""
    gt_base = 0.20 * vals["cc"] + 0.20 * vals["fl"]
    explore = vals["cp"] * (_DE_WEIGHT * vals["de"] + _BE_WEIGHT * vals["be"])
    cost = _COST_COEF * nr
    gate = _GA_GATE_PENALTY if vals["ga"] < ga_threshold else 0.0
    return gt_base + explore + gate + cost, explore


def _article_oracle_at(sec_ids, draw_sections, nr_units, ga_threshold, features):
    """One draw -> (oracle_arm, margin, r_w)."""
    sections_output = {}
    for sid in sec_ids:
        rewards = {}
        explores = {}
        for arm in ARM_ORDER:
            vals = draw_sections[sid][arm]
            if vals:
                rewards[arm], explores[arm] = _section_reward_at(vals, nr_units[arm], ga_threshold)
            else:
                rewards[arm], explores[arm] = float("-inf"), 0.0
        sections_output[sid] = {
            "oracle": max(ARM_ORDER, key=rewards.__getitem__),
            "rewards": rewards,
            "explore": explores,
        }
    r_w, *_ = cao._compute_r_w(sections_output, features)
    ranked = sorted(ARM_ORDER, key=lambda a: r_w[a], reverse=True)
    return ranked[0], r_w[ranked[0]] - r_w[ranked[1]], r_w


def part1_ga_mean_drop():
    print("=" * 100)
    print("PART 1: TEST ga (guideline_adherence) mean, production (single-draw) vs N=3-averaged")
    print("=" * 100)
    prod_vals, avg_vals = [], []
    for art in _TEST_ARTICLES:
        sec_ids, draws, _ = _load_article_draws(art)
        seen = set()
        for sid in sec_ids:
            if sid in seen:
                continue
            seen.add(sid)
            for arm in ARM_ORDER:
                prod_cell = draws["production"][sid][arm]
                if prod_cell is not None:
                    prod_vals.append(prod_cell["ga"])
                cells = [draws[k][sid][arm]["ga"] for k in draws if draws[k][sid][arm] is not None]
                if cells:
                    avg_vals.append(sum(cells) / len(cells))
    print(f"  production (single-draw) ga: n={len(prod_vals)}  mean={statistics.mean(prod_vals):.4f}  "
          f"pass-rate(>=0.5)={sum(1 for v in prod_vals if v >= 0.5) / len(prod_vals):.1%}")
    print(f"  N=3-averaged ga:             n={len(avg_vals)}  mean={statistics.mean(avg_vals):.4f}  "
          f"pass-rate(>=0.5)={sum(1 for v in avg_vals if v >= 0.5) / len(avg_vals):.1%}")
    print(f"  (compare to TRAIN Sec59.5 finding: production mean=0.740 -> N=3-averaged mean=0.412)")
    print()


def part2_threshold_sweep(thresholds: list[float]):
    print("=" * 100)
    print("PART 2: ga gate threshold sweep -- per-article production/averaged/votes at each threshold")
    print("=" * 100)

    cache = {art: _load_article_draws(art) for art in _TEST_ARTICLES}
    features_cache = {
        art: json.loads((mrn._BASES_DIR / art / "guideline_features.json").read_text(encoding="utf-8"))
        .get("sections", {})
        for art in _TEST_ARTICLES
    }

    for thr in thresholds:
        n_confirmed = n_corrected = n_unresolved = 0
        detail = []
        for art in _TEST_ARTICLES:
            sec_ids, draws, nr_units = cache[art]
            feats = features_cache[art]

            per_draw_oracle = {}
            per_draw_rw = {}
            for label, sections in draws.items():
                arm, margin, r_w = _article_oracle_at(sec_ids, sections, nr_units, thr, feats)
                per_draw_oracle[label] = arm
                per_draw_rw[label] = r_w

            # averaged-argmax: average each draw's r_w vector, then argmax (matches
            # merge_replicate_oracles.py's per-draw-gate-then-average-final-reward order)
            avg_rw = {a: sum(per_draw_rw[lbl][a] for lbl in draws) / len(draws) for a in ARM_ORDER}
            avg_ranked = sorted(ARM_ORDER, key=lambda a: avg_rw[a], reverse=True)
            avg_arm = avg_ranked[0]

            votes = [per_draw_oracle["production"]] + [per_draw_oracle[k] for k in draws if k != "production"]
            vote_counts = {a: votes.count(a) for a in set(votes)}
            top_count = max(vote_counts.values())
            tied = [a for a, c in vote_counts.items() if c == top_count]
            majority_arm = tied[0] if len(tied) == 1 else None

            prod_arm = per_draw_oracle["production"]
            if majority_arm is None:
                n_unresolved += 1
                disp = "UNRESOLVED"
            elif majority_arm == prod_arm:
                n_confirmed += 1
                disp = "CONFIRMED"
            else:
                n_corrected += 1
                disp = "CORRECTED"
            detail.append((art, prod_arm, avg_arm, votes, majority_arm, disp))

        print(f"\n  ga_gate_threshold={thr:.2f}  ->  confirmed={n_confirmed}  corrected={n_corrected}  "
              f"unresolved(3-way split)={n_unresolved}   (n=12)")
        for art, prod_arm, avg_arm, votes, majority_arm, disp in detail:
            mv = majority_arm if majority_arm is not None else "NO-MAJ"
            print(f"      {art:<32} prod={prod_arm:<9} avg-argmax={avg_arm:<9} "
                  f"votes={votes}  majority={mv:<9} {disp}")


if __name__ == "__main__":
    part1_ga_mean_drop()
    part2_threshold_sweep([0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2])
