"""Re-run Part 7's diagnostic analyses (§53/§54/§58) on the N=3-averaged TRAIN corpus.

Read-only, zero LLM calls, zero writes. Part 7 (analysis md) built its metric-
differentiation and gate-candidate findings entirely from single-draw (N=1)
production `reasoning.json` data, via `model_gate_candidates.load_corpus()`.
The 24 TRAIN articles now each have N=3 draws (1 production + 2 real
temperature=0.7 replicates, per Appendix A.13). This script re-derives the same
raw per-dimension values `load_corpus()` extracts, but AVERAGES each
(section, arm, dimension) scalar across all available draws before handing the
corpus to `model_gate_candidates.evaluate()` -- so every candidate formula in
Part 7 (A1/B/C1/C2/C3/D/E/F, the H-series cost_coef sweep) can be re-scored on
averaged data using the EXACT SAME formula code, no duplication.

TEST articles are NOT averaged here (their replication was a separate, later
decision and may still be in progress) -- they pass through as single-draw,
identical to `model_gate_candidates.load_corpus()`'s existing behavior. This
script's comparisons are therefore TRAIN-only; Part 7's own tables already
report TRAIN and ALL(40) splits separately for this reason.

Averaging happens at the per-draw SCALAR level (post-`enhancement_credit()` for
de/be, post-`_get_score()` for everything else) -- i.e. exactly what
`load_corpus()` would extract from each draw individually, simple-averaged
across draws. This mirrors the granularity `merge_replicate_oracles.py` uses for
final section rewards, one level less aggregated (per-dimension, not
per-formula-combined-reward), which is what a formula-comparison tool needs.

Does NOT touch anything about actual GRPO training runs (entropy, checkpoints,
TEST eval accuracy) -- purely a re-derivation of Part 7's zero-cost reward-
signal-quality diagnostics on the replicated data.

Usage (from research_agent_local/):
  python3 training/reanalyze_part7_averaged.py
"""
import json
import statistics
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402
import model_gate_candidates as mgc  # noqa: E402

_REPO_ROOT = _TRAINING.parent.parent
_NOISE_DIR = _REPO_ROOT / "rl_training_data" / "noise_experiment"

DIMS = mgc.DIMS
ENH = mgc.ENH
ARMS = mgc.ARMS


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
    """One draw's per-dimension scalar values for one (section, arm)."""
    vals = {}
    for short, dim in DIMS.items():
        entries = entries_by_dim.get(dim, [])
        if short in ENH:
            enh = geo._get_enhancement(entries, snorm, idx)
            vals[short] = geo._get_score(entries, snorm, idx) if enh is None \
                else enhancement_credit(enh[1])
            vals[f"{short}_raw"] = geo._get_score(entries, snorm, idx)
        else:
            vals[short] = geo._get_score(entries, snorm, idx)
    return vals


def load_corpus_averaged(n_replicates=2):
    """Same shape as model_gate_candidates.load_corpus(), TRAIN articles averaged
    over (1 production + n_replicates) draws; TEST articles single-draw (unchanged)."""
    out = []
    n_averaged = 0
    for t in geo._ALL_ARTICLES:
        for v in geo._VARIANTS:
            art_var = f"{t}__{v}"
            so = geo._BASES_DIR / art_var / "section_oracle.json"
            gf = geo._BASES_DIR / art_var / "guideline_features.json"
            if not so.exists():
                continue
            sec_ids = list(json.loads(so.read_text(encoding="utf-8")).get("sections", {}).keys())
            if not sec_ids:
                continue
            feats = {}
            if gf.exists():
                feats = json.loads(gf.read_text(encoding="utf-8")).get("sections", {})
            sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]

            arm_presets = geo._ARM_PRESETS
            preset_to_arm = {pid: arm for arm, ids in arm_presets.items() for pid in ids}
            arm_draws = {}  # arm -> [entries_by_dim, ...] across draws
            for arm, pids in arm_presets.items():
                pid = pids[0]
                draws = []
                prod_dir = geo._EPISODES_DIR / f"{art_var}__preset{pid}"
                prod = _load_reasoning(prod_dir)
                if prod is not None:
                    draws.append(prod)
                for r in range(1, n_replicates + 1):
                    rep_dir = _NOISE_DIR / f"{art_var}__replicate{r}__preset{pid}"
                    rep = _load_reasoning(rep_dir)
                    if rep is not None:
                        draws.append(rep)
                arm_draws[arm] = draws

            secs = []
            for idx, (sid, snorm) in enumerate(zip(sec_ids, sec_norms)):
                tw = feats.get(sid, {}).get("target_words")
                tw = int(tw) if tw is not None else 100
                per_arm = {}
                for arm in ARMS:
                    draws = arm_draws[arm]
                    per_draw_vals = [_draw_vals(d, snorm, idx) for d in draws]
                    if len(per_draw_vals) > 1:
                        n_averaged += 1
                    avg = {}
                    keys = per_draw_vals[0].keys() if per_draw_vals else {}
                    for k in keys:
                        avg[k] = sum(pv[k] for pv in per_draw_vals) / len(per_draw_vals)
                    per_arm[arm] = avg
                secs.append((sid, tw, per_arm))
            out.append((art_var, "TRAIN", secs, False))

    # TEST articles: reuse load_corpus()'s own single-draw extraction unchanged
    single_draw_corpus = mgc.load_corpus()
    test_names = set(mgc.TEST_ARTICLES)
    for art_var, split, secs, no_variant in single_draw_corpus:
        if art_var in test_names:
            out.append((art_var, split, secs, no_variant))

    return out, n_averaged


if __name__ == "__main__":
    corpus, n_cells = load_corpus_averaged()
    n_train_secs = sum(len(s) for a, sp, s, _ in corpus if sp == "TRAIN")
    n_test_secs = sum(len(s) for a, sp, s, _ in corpus if sp == "TEST")
    print(f"loaded {len(corpus)} articles -- TRAIN sections: {n_train_secs}, "
          f"TEST sections: {n_test_secs} (single-draw, unaveraged)")
    print(f"TRAIN (section,arm) cells averaged across >1 draw: {n_cells}\n")

    hdr = (f"{'candidate':24s} | {'drop%':>6s} {'floor%':>6s} {'mMargin':>7s} {'medMrg':>7s} "
           f"{'advNorm':>6s} {'nearTie':>6s} | {'sec sk/li/st/dp':15s} | {'art dist':11s} thin"
           f" || {'ALLdrop':>6s} {'flr%':>6s} {'medMrg':>7s} {'adv':>6s} | {'art dist':11s} thin")
    print(hdr)
    print("-" * len(hdr))
    names = ["A1_current_cost003", "B_drop_ra", "C1_soft_ga_pen005", "C2_soft_ga_pen010",
             "C3_soft_ga_pen015", "G_pure_drop_ga", "D_hard_ga", "E_hard_trio_drop_ga",
             "F_hard_trio_drop_ga_cc",
             "H_C2_cost-0.06", "H_C2_cost-0.045", "H_C2_cost-0.03", "H_C2_cost-0.02",
             "A0_current_cost002"]
    for name in names:
        fn = mgc.CANDIDATES[name]
        ss, aa = mgc.evaluate(corpus, fn)
        mgc.report(name, ss, aa)
    print()

    # ---------------------------------------------------------------------
    # §53-style metric-differentiation indices (armSprd/%const/meanRng/monoUp),
    # TRAIN only, on the SAME averaged per-arm values already extracted above.
    # ("st" / ground_truth_structure omitted -- not part of model_gate_candidates'
    # DIMS dict since it carries zero weight in every shipped/candidate formula;
    # §53.6/F5 already confirmed its exclusion on single-draw data, not re-derived here.)
    # ---------------------------------------------------------------------
    print(f"\n{'='*100}")
    print("  TRAIN metric-differentiation indices (averaged N=3) -- compare against §53.4's TRAIN table")
    print(f"{'='*100}")
    print(f"{'metric':5s} {'mean':>6s} | {'skip':>6s} {'light':>6s} {'std':>6s} {'deep':>6s} | "
          f"{'armSprd':>7s} {'%const':>7s} {'meanRng':>7s} {'monoUp':>6s} {'SNR':>5s}")
    print("-" * 100)
    train_secs = [(sid, tw, per_arm) for a, sp, secs, _ in corpus if sp == "TRAIN" for sid, tw, per_arm in secs]
    n = len(train_secs)
    for short in ("de", "be", "fl", "cc", "ga", "ra", "cp", "gsp"):
        am = {a: sum(per_arm[a][short] for _, _, per_arm in train_secs) / n for a in ARMS}
        overall = sum(am.values()) / 4
        spread = max(am.values()) - min(am.values())
        ranges, n_const, n_mono, n_var = [], 0, 0, 0
        for _, _, per_arm in train_secs:
            vals = {a: per_arm[a][short] for a in ARMS}
            rng = max(vals.values()) - min(vals.values())
            ranges.append(rng)
            if rng < 1e-9:
                n_const += 1
            else:
                n_var += 1
                seq = [vals[a] for a in ARMS]
                if all(seq[i] <= seq[i + 1] for i in range(3)):
                    n_mono += 1
        mean_rng = sum(ranges) / n
        mono = (n_mono / n_var) if n_var else 0.0
        snr = (spread / mean_rng) if mean_rng > 1e-9 else float("nan")
        print(f"{short:5s} {overall:6.3f} | {am['skip']:6.3f} {am['light']:6.3f} "
              f"{am['standard']:6.3f} {am['deep']:6.3f} | {spread:7.4f} {n_const/n:7.1%} "
              f"{mean_rng:7.4f} {mono:6.1%} {snr:5.2f}")
