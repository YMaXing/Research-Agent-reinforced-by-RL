"""Metric differentiation analysis across the 4 exploration arms.

Read-only diagnostic. Reuses generate_episode_oracles' parsing/lookup helpers so
the numbers reflect exactly what the reward formula sees -- but loads ALL graded
dims (not just _REWARD_DIMS, which _load_episode filters to).

Question: which graded metrics actually DIFFERENTIATE the 4 arms
(skip/light/standard/deep), and which are effectively constant (satisficing)?
"""
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402

ARMS = geo._ARM_ORDER

ALL_DIMS = {
    "cc": "ground_truth_core_content",
    "fl": "ground_truth_flow",
    "st": "ground_truth_structure",
    "de": "ground_truth_depth_enhancement",
    "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation",
    "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring",
    "gsp": "user_intent_golden_source_priority",
}
ENH_DIMS = {"de", "be"}

# Effective additive weight of each metric in the CURRENT reward formula:
# gt_base = .20cc + .20fl ; explore = cp*(.60de+.40be)*.50 ; ui = (.50ga+.50ra)*.30
CURRENT_WEIGHT = {
    "cc": 0.20, "fl": 0.20, "st": 0.0,
    "de": 0.30, "be": 0.20,   # cp*(.6*.5) and cp*(.4*.5), with cp ~= 1
    "cp": 0.0,                # multiplicative gate, not additive
    "ga": 0.15, "ra": 0.15, "gsp": 0.0,
}

TEST_ARTICLES = [
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI",
    "Bird_Eye_Extreme", "Dark_Dimension", "Distinct_AI_Models",
    "Earth_Oceans_Origin", "Gravity_Entropy", "HNSW",
    "Insects_Consciousness", "Space-Time_QECC", "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
]


def load_episode_all_dims(episode_dir: Path):
    """Like geo._load_episode but WITHOUT the _REWARD_DIMS filter."""
    path = episode_dir / "reasoning.json"
    if not path.exists():
        path = episode_dir / "reasons.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {d: geo._parse_sections_ordered(data[d]) for d in data if isinstance(data.get(d), str)}


def build_targets():
    targets = []
    for topic in geo._ALL_ARTICLES:
        for var in geo._VARIANTS:
            targets.append((f"{topic}__{var}", topic, False))
    for art in TEST_ARTICLES:
        targets.append((art, art, True))
    return targets


def collect():
    rows = []
    missing = {}
    for art_var, article, no_variant in build_targets():
        p = geo._BASES_DIR / art_var / "section_oracle.json"
        if not p.exists():
            continue
        sec_ids = list(json.loads(p.read_text(encoding="utf-8")).get("sections", {}).keys())
        if not sec_ids:
            continue
        sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]

        arm_presets = geo._TEST_ARM_PRESETS if no_variant else geo._ARM_PRESETS
        ep_root = geo._TEST_EPISODES_DIR if no_variant else geo._EPISODES_DIR

        arm_eps = {}
        for arm, pids in arm_presets.items():
            name = f"{article}__preset{pids[0]}" if no_variant else f"{art_var}__preset{pids[0]}"
            ep_dir = ep_root / name
            if not ep_dir.exists():
                alt = geo._EPISODES_DIR / name
                ep_dir = alt if alt.exists() else ep_dir
            arm_eps[arm] = load_episode_all_dims(ep_dir) if ep_dir.exists() else {}

        for arm, ep in arm_eps.items():
            for short, dim in ALL_DIMS.items():
                if dim not in ep:
                    missing.setdefault(short, set()).add(art_var)

        for idx, (sid, snorm) in enumerate(zip(sec_ids, sec_norms)):
            rec = {"article": art_var, "split": "TEST" if no_variant else "TRAIN", "vals": {}}
            for short, dim in ALL_DIMS.items():
                per_arm = {}
                for arm in ARMS:
                    entries = arm_eps[arm].get(dim, [])
                    if short in ENH_DIMS:
                        enh = geo._get_enhancement(entries, snorm, idx)
                        v = geo._get_score(entries, snorm, idx) if enh is None else enhancement_credit(enh[1])
                    else:
                        v = geo._get_score(entries, snorm, idx)
                    per_arm[arm] = float(v)
                rec["vals"][short] = per_arm
            rows.append(rec)

    if missing:
        print("NOTE - dims absent from some episodes' reasoning.json:", file=sys.stderr)
        for k, v in sorted(missing.items()):
            print(f"   {k}: missing in {len(v)} article(s)", file=sys.stderr)
    return rows


def report(rows, split=None):
    sub = [r for r in rows if split is None or r["split"] == split]
    n = len(sub)
    if not n:
        return
    print(f"\n{'='*112}")
    print(f"  {split or 'ALL'}  (n = {n} sections)")
    print(f"{'='*112}")
    print(f"{'metric':5s} {'w':>5s} {'mean':>6s} | {'skip':>6s} {'light':>6s} {'std':>6s} {'deep':>6s} | "
          f"{'armSprd':>7s} {'%const':>7s} {'meanRng':>7s} {'monoUp':>6s} | {'w*Rng':>7s} {'w*Sprd':>7s}")
    print("-" * 112)

    for short in ALL_DIMS:
        w = CURRENT_WEIGHT[short]
        am = {a: sum(r["vals"][short][a] for r in sub) / n for a in ARMS}
        overall = sum(am.values()) / 4
        spread = max(am.values()) - min(am.values())
        ranges, n_const, n_mono, n_var = [], 0, 0, 0
        for r in sub:
            v = r["vals"][short]
            rng = max(v.values()) - min(v.values())
            ranges.append(rng)
            if rng < 1e-9:
                n_const += 1
            else:
                n_var += 1
                seq = [v[a] for a in ARMS]
                if all(seq[i] <= seq[i + 1] for i in range(3)):
                    n_mono += 1
        mean_rng = sum(ranges) / n
        mono = (n_mono / n_var) if n_var else 0.0
        print(f"{short:5s} {w:5.2f} {overall:6.3f} | {am['skip']:6.3f} {am['light']:6.3f} "
              f"{am['standard']:6.3f} {am['deep']:6.3f} | {spread:7.4f} {n_const/n:7.1%} "
              f"{mean_rng:7.4f} {mono:6.1%} | {w*mean_rng:7.4f} {w*spread:7.4f}")

    print()
    print("  w        = effective additive weight in the CURRENT reward formula")
    print("  armSprd  = max-min of the 4 ARM MEANS  <-- systematic (signal) differentiation")
    print("  %const   = share of sections identical across all 4 arms (zero differentiation)")
    print("  meanRng  = mean per-section (max-min) across arms  <-- total variation incl. noise")
    print("  monoUp   = of varying sections, share monotonically increasing skip->deep")
    print("  w*Rng    = weighted TOTAL variation injected into the reward (signal + noise)")
    print("  w*Sprd   = weighted SYSTEMATIC signal contributed to arm separation")


if __name__ == "__main__":
    rows = collect()
    report(rows, "TRAIN")
    report(rows, "TEST")
    report(rows, None)
