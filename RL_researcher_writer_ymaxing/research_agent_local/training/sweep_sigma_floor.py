"""Sweep sigma_floor against the corpus to expose the drop-rate / confidence trade-off.

Context: estimate_noise_floor.py measures the REAL run-to-run reward noise of a
(section, arm) cell at mean sd ~= 0.099 (median 0.087) -- i.e. the difference
between two arms carries a noise sd of roughly 0.099*sqrt(2) ~= 0.14. The shipped
sigma_floor = 0.04 is ~0.4x a single cell's noise sd, so it is far too permissive
to be doing the job its own help-text claims ("groups with max-min < sigma_floor
are dropped as noise").

This sweep shows what each candidate floor costs (groups dropped = training data
lost) and buys (share of surviving groups whose top-1-vs-top-2 margin actually
exceeds the measured noise).
"""
import sys
from pathlib import Path

_TRAINING = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training")
sys.path.insert(0, str(_TRAINING))
import generate_episode_oracles as geo  # noqa: E402
import model_gate_candidates as m  # noqa: E402

ARMS = geo._ARM_ORDER

# From estimate_noise_floor.py (n=60 cells, 2 articles, 3 replicates each)
CELL_NOISE_SD = 0.0991
DIFF_NOISE_SD = CELL_NOISE_SD * (2 ** 0.5)   # noise on a DIFFERENCE between two arms

CANDIDATE_NAME = "C2_soft_ga_pen010"


def main():
    corpus = m.load_corpus()
    fn = m.CANDIDATES[CANDIDATE_NAME]

    cells = []
    for art_var, split, secs, no_variant in corpus:
        for sid, tw, per_arm in secs:
            rs = []
            for arm in ARMS:
                rest, expl = fn(per_arm[arm], geo._ARM_COST_UNITS[arm])
                rs.append(rest + expl)
            mean_r = sum(rs) / 4
            std = (sum((r - mean_r) ** 2 for r in rs) / 4) ** 0.5
            srt = sorted(rs, reverse=True)
            cells.append({"split": split, "spread": max(rs) - min(rs), "std": std,
                          "margin": srt[0] - srt[1], "regret": max(rs) - mean_r})

    print(f"formula = {CANDIDATE_NAME} (cost_coef -0.03), n = {len(cells)} sections\n")
    print(f"MEASURED noise: per-cell sd = {CELL_NOISE_SD:.4f}; "
          f"noise on an arm-DIFFERENCE = {DIFF_NOISE_SD:.4f}\n")

    hdr = (f"{'sigma_floor':>11s} | {'dropped':>8s} {'kept':>6s} | {'floored':>8s} | "
           f"{'meanAdv':>8s} | {'margin>noiseSD':>14s} {'margin>2xSD':>12s}")
    print(hdr)
    print("-" * len(hdr))

    for sf in (0.04, 0.06, 0.08, 0.10, 0.12, 0.14):
        kept = [c for c in cells if c["spread"] >= sf]
        dropped = len(cells) - len(kept)
        floored = sum(1 for c in kept if c["std"] < sf)
        advs = [c["regret"] / max(c["std"], sf) for c in kept]
        mean_adv = sum(advs) / len(advs) if advs else 0.0
        gt1 = sum(1 for c in kept if c["margin"] > DIFF_NOISE_SD)
        gt2 = sum(1 for c in kept if c["margin"] > 2 * DIFF_NOISE_SD)
        mark = "  <-- current" if abs(sf - 0.04) < 1e-9 else ""
        print(f"{sf:11.2f} | {dropped:4d} ({dropped/len(cells):3.0%}) {len(kept):6d} | "
              f"{floored/len(kept):7.1%} | {mean_adv:8.3f} | "
              f"{gt1:5d} ({gt1/len(kept):4.0%}) {gt2:5d} ({gt2/len(kept):4.0%}){mark}")

    print()
    print("  dropped        = groups train_grpo discards as flat (spread < sigma_floor)")
    print("  floored        = of kept groups, share whose raw_std < sigma_floor")
    print("                   (advantage denominator artificially clamped)")
    print("  meanAdv        = mean normalized GRPO advantage over kept groups")
    print("  margin>noiseSD = kept groups whose top1-top2 margin exceeds ONE sd of")
    print("                   arm-difference noise (~68% confidence the winner is real)")
    print("  margin>2xSD    = ... exceeds two sd (~95% confidence)")


if __name__ == "__main__":
    main()
