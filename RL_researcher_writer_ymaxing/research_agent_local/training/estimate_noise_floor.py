"""Empirically estimate the reward noise floor from the replicate experiment.

`sigma_floor` (train_grpo, default 0.04) has two jobs:
  1. flat-group filter  -- drop groups whose max-min reward spread is "just noise"
  2. advantage-normalisation floor -- stop dividing by a near-zero std

Both are noise-threshold decisions, but the 0.04 default has no recorded
derivation anywhere in the repo (it is an unexplained argparse default; the one
nearby code comment references a *different* value, 0.05, in the since-replaced
variant-conditional formula).

This tool derives the number the way it should be derived: from the measured
run-to-run reward noise of the SAME (article, section, arm) across independent
write+grade replicates (rl_training_data/noise_experiment/).

Reward is recomputed with the CURRENT production formula via
generate_episode_oracles._section_reward_components, so the noise estimate is on
the same scale as the rewards sigma_floor is compared against.

CLI (added 2026-08-04 to point this at the new temperature=0.7 replicate set,
instead of only the original 2 temperature=0.25-confounded articles, per
analysis md A.7.1/A.10 step 3):
  python3 estimate_noise_floor.py
  python3 estimate_noise_floor.py --articles 06_tools__var_standard 09_RAG__var_standard --replicates 2
"""
import argparse
import json
import statistics
import sys
from pathlib import Path

_TRAINING = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training")
sys.path.insert(0, str(_TRAINING))
import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402

NOISE_ROOT = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment")
_DEFAULT_ARTICLES = ["09_RAG__var_standard", "06_tools__var_standard"]
_DEFAULT_REPLICATES = 3
PRESET_TO_ARM = {0: "skip", 1: "light", 3: "standard", 5: "deep"}


def load_all(d: Path):
    p = d / "reasoning.json"
    if not p.exists():
        p = d / "reasons.json"
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {k: geo._parse_sections_ordered(data[k]) for k in data if isinstance(data.get(k), str)}


def section_reward(ep, snorm, idx, arm):
    def sc(dim):
        return geo._get_score(ep.get(dim, []), snorm, idx)

    def enh(dim):
        e = geo._get_enhancement(ep.get(dim, []), snorm, idx)
        return sc(dim) if e is None else enhancement_credit(e[1])

    rest, expl = geo._section_reward_components(
        cc=sc("ground_truth_core_content"),
        fl=sc("ground_truth_flow"),
        de=enh("ground_truth_depth_enhancement"),
        be=enh("ground_truth_breadth_enhancement"),
        cp=sc("ground_truth_core_preservation"),
        ga=sc("user_intent_guideline_adherence"),
        ra=sc("user_intent_research_anchoring"),
        nr=geo._ARM_COST_UNITS[arm],
        variant="standard",
    )
    return rest + expl


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES,
                         help="Max replicate index to look for (additional to the production draw).")
    parser.add_argument("--target-n", type=int, default=None,
                         help="Total draws INCLUDING the production one; overrides --replicates as target_n - 1.")
    args = parser.parse_args()
    replicates = args.replicates if args.target_n is None else args.target_n - 1
    run(args.articles, list(range(1, replicates + 1)))


def run(ARTICLES, REPLICATES):
    """Returns a stats dict (mean/median/p90 sd, diff-sd, per_cell_sd/rows) for reuse by
    other analysis scripts, in addition to printing the same report as before."""
    per_cell_sd = []      # noise sd of one (section, arm) across replicates
    per_cell_range = []
    rows = []

    for art in ARTICLES:
        so = geo._BASES_DIR / art / "section_oracle.json"
        sec_ids = list(json.loads(so.read_text(encoding="utf-8")).get("sections", {}).keys())
        sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]

        # replicate -> preset -> parsed episode
        eps = {}
        for rep in REPLICATES:
            eps[rep] = {}
            for p in PRESET_TO_ARM:
                d = NOISE_ROOT / f"{art}__replicate{rep}__preset{p}"
                eps[rep][p] = load_all(d) if d.exists() else {}

        for idx, (sid, snorm) in enumerate(zip(sec_ids, sec_norms)):
            for p, arm in PRESET_TO_ARM.items():
                vals = []
                for rep in REPLICATES:
                    ep = eps[rep].get(p, {})
                    if not ep:
                        continue
                    vals.append(section_reward(ep, snorm, idx, arm))
                if len(vals) >= 2:
                    sd = statistics.stdev(vals)
                    per_cell_sd.append(sd)
                    per_cell_range.append(max(vals) - min(vals))
                    rows.append((art, sid[:40], arm, len(vals), round(sd, 4),
                                 round(max(vals) - min(vals), 4)))

    print(f"Measured {len(per_cell_sd)} (section, arm) cells across replicates {REPLICATES}")
    print(f"  articles: {ARTICLES}\n")

    stats = {"per_cell_sd": per_cell_sd, "rows": rows}

    if per_cell_sd:
        s = sorted(per_cell_sd)
        r = sorted(per_cell_range)

        def pct(xs, q):
            i = int(q * (len(xs) - 1))
            return xs[i]

        mean_sd = statistics.mean(per_cell_sd)
        median_sd = statistics.median(per_cell_sd)
        diff_sd = mean_sd * (2 ** 0.5)
        stats.update({
            "mean_sd": mean_sd, "median_sd": median_sd,
            "p75_sd": pct(s, 0.75), "p90_sd": pct(s, 0.90), "max_sd": max(per_cell_sd),
            "diff_sd_1x": diff_sd, "diff_sd_2x": 2 * diff_sd,
        })
        print("REWARD NOISE (sd of the same section+arm across independent replicates):")
        print(f"  mean sd     = {mean_sd:.4f}")
        print(f"  median sd   = {median_sd:.4f}")
        print(f"  p75 sd      = {pct(s, 0.75):.4f}")
        print(f"  p90 sd      = {pct(s, 0.90):.4f}")
        print(f"  max sd      = {max(per_cell_sd):.4f}")
        print(f"  share of cells with sd == 0 (perfectly stable): "
              f"{sum(1 for x in per_cell_sd if x < 1e-9)/len(per_cell_sd):.1%}")
        print()
        print("REWARD NOISE (max-min range across replicates, same cell):")
        print(f"  mean range  = {statistics.mean(per_cell_range):.4f}")
        print(f"  median range= {statistics.median(per_cell_range):.4f}")
        print(f"  p90 range   = {pct(r, 0.90):.4f}")
        print()
        print("ARM-DIFFERENCE noise (sd*sqrt(2), what a top1-vs-top2 margin is compared against):")
        print(f"  1x diff-sd  = {diff_sd:.4f}")
        print(f"  2x diff-sd  = {2 * diff_sd:.4f}")
        print()
        print("INTERPRETATION vs the current sigma_floor = 0.04:")
        below = sum(1 for x in per_cell_sd if x < 0.04) / len(per_cell_sd)
        print(f"  {below:.1%} of cells have replicate-noise sd BELOW 0.04")
        print(f"  => a spread of 0.04 between two arms is {0.04/max(mean_sd,1e-9):.2f}x "
              f"the mean per-cell noise sd")
        print()
        print("Worst 12 cells by noise sd:")
        for row in sorted(rows, key=lambda x: -x[4])[:12]:
            print(f"  {row[0]:26s} {row[2]:9s} n={row[3]} sd={row[4]:.4f} range={row[5]:.4f}  {row[1]}")

    return stats


if __name__ == "__main__":
    main()
