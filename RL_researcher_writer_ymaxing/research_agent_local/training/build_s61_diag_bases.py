"""Build 3 diagnostic bases/ directories for the §61 Stage 1 single-variable
reward-formula ablation (analysis md §61): today's `research_digest.md`/
`guideline_features.json` (unchanged model inputs) + a freshly-COMPUTED
`section_oracle.json` under one of the 3 isolated candidate formulas from
`model_gate_candidates.py`'s S61_* factorial (§61 Stage 0) -- zero new
generation, reuses already-graded episode data via model_gate_candidates.py's
own corpus loader/candidate functions.

Each candidate changes exactly ONE of the 3 real differences between C2
(shipped) and true Formula B, holding the other two at C2's production values:
  S61_cost_only  -- cost_coef=-0.06 * ordinal round-count units only
  S61_debe_only  -- raw (pre-enhancement_credit()) de/be only
  S61_gara_only  -- additive (0.50*ga+0.50*ra)*0.30, no gate, only

Writes to 3 NEW, separate roots (never touches `rl_training_data/bases/` or
any existing backup): `bases_S61_COSTONLY_DIAG/`, `bases_S61_DEBEONLY_DIAG/`,
`bases_S61_GARAONLY_DIAG/`. Point `train_grpo.py` at one via its existing
`--bases-dir` override.

Usage (from research_agent_local/):
  python3 training/build_s61_diag_bases.py
  python3 training/build_s61_diag_bases.py --candidates S61_cost_only --dry-run
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import model_gate_candidates as mgc  # noqa: E402
import generate_episode_oracles as geo  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent
_TODAY_BASES = _REPO_ROOT / "rl_training_data" / "bases"

_TRAIN_ARTICLES = [
    "02_workflows_vs_agents__var_minimal", "02_workflows_vs_agents__var_standard", "02_workflows_vs_agents__var_demanding",
    "03_context_engineering__var_minimal", "03_context_engineering__var_standard", "03_context_engineering__var_demanding",
    "05_workflow_patterns__var_minimal", "05_workflow_patterns__var_standard", "05_workflow_patterns__var_demanding",
    "06_tools__var_minimal", "06_tools__var_standard", "06_tools__var_demanding",
    "08_react_practice__var_minimal", "08_react_practice__var_standard", "08_react_practice__var_demanding",
    "09_RAG__var_minimal", "09_RAG__var_standard", "09_RAG__var_demanding",
    "10_memory_knowledge_access__var_minimal", "10_memory_knowledge_access__var_standard", "10_memory_knowledge_access__var_demanding",
    "11_multimodal__var_minimal", "11_multimodal__var_standard", "11_multimodal__var_demanding",
]

_CANDIDATE_OUT_DIRS = {
    "S61_cost_only": _REPO_ROOT / "rl_training_data" / "bases_S61_COSTONLY_DIAG",
    "S61_debe_only": _REPO_ROOT / "rl_training_data" / "bases_S61_DEBEONLY_DIAG",
    "S61_gara_only": _REPO_ROOT / "rl_training_data" / "bases_S61_GARAONLY_DIAG",
    # Stage 2 preview (2026-08-06): cost_coef=-0.05 with H0 units (production's
    # own unit shape, only the coefficient scaled) -- recommended over -0.045
    # after the magnitude-sweep preview showed a sharpness cliff between -0.045
    # and -0.05, with -0.045 landing in a worse spot on both floor% and deep-count.
    "S61_cost05_H0": _REPO_ROOT / "rl_training_data" / "bases_S61_COST05_DIAG",
}

_FROM_TODAY = ["research_digest.md", "guideline_features.json"]


def build_candidate(candidate_name: str, articles: list[str], dry_run: bool) -> int:
    out_root = _CANDIDATE_OUT_DIRS[candidate_name]
    fn = mgc.CANDIDATES[candidate_name]
    cost_units = fn._cost_units or geo._ARM_COST_UNITS

    corpus = {art_var: secs for art_var, split, secs, no_variant in mgc.load_corpus() if art_var in articles}

    print(f"\n--- {candidate_name} -> {out_root} ---")
    ok = 0
    for article in articles:
        today_dir = _TODAY_BASES / article
        out_dir = out_root / article
        missing = [f for f in _FROM_TODAY if not (today_dir / f).exists()]
        if article not in corpus:
            missing.append("(episode data)")
        if missing:
            print(f"  SKIP {article}: missing {missing}")
            continue

        sections_out: dict[str, dict] = {}
        for sid, tw, per_arm in corpus[article]:
            rewards = {}
            for arm in mgc.ARMS:
                nr = cost_units[arm]
                rest, expl = fn(per_arm[arm], nr)
                rewards[arm] = round(rest + expl, 4)
            oracle_arm = max(mgc.ARMS, key=rewards.__getitem__)
            sections_out[sid] = {"oracle": oracle_arm, "rewards": rewards}

        if dry_run:
            print(f"  WOULD BUILD: {out_dir}  ({len(sections_out)} sections)")
            ok += 1
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        for f in _FROM_TODAY:
            shutil.copy2(today_dir / f, out_dir / f)
        payload = {
            "version": 5,
            "article": article.split("__var_")[0],
            "variant": article.split("__var_")[1] if "__var_" in article else None,
            "merge_source": f"model_gate_candidates.py::{candidate_name}",
            "sections": sections_out,
        }
        (out_dir / "section_oracle.json").write_text(
            json.dumps(payload, indent=2), encoding="utf-8"
        )
        print(f"  BUILT: {out_dir}  ({len(sections_out)} sections)")
        ok += 1
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_TRAIN_ARTICLES)
    parser.add_argument(
        "--candidates", nargs="+", default=list(_CANDIDATE_OUT_DIRS.keys()),
        choices=list(_CANDIDATE_OUT_DIRS.keys()),
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("=" * 80)
    print("BUILD S61 STAGE-1 SINGLE-VARIABLE DIAGNOSTIC BASES")
    print(f"Today's bases (digests, unchanged): {_TODAY_BASES}")
    print("=" * 80)

    total_ok = 0
    total_expected = 0
    for name in args.candidates:
        total_ok += build_candidate(name, args.articles, args.dry_run)
        total_expected += len(args.articles)

    print(f"\nDone: {total_ok}/{total_expected} article-candidate combination(s) built.")
    return 0 if total_ok == total_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
