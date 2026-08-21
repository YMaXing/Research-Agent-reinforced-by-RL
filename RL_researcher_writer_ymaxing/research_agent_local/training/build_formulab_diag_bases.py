"""Build a diagnostic bases/ directory for the Formula-B reward-swap experiment
(analysis md §60.9/§60.12): today's `research_digest.md`/`guideline_features.json`
(current digest pipeline, unchanged model inputs) + the TRUE original Formula-B
`section_oracle.json` (from `bases_ORACLE_BACKUP_20260708_231117/`, zero new
generation). Section IDs were verified identical across all 24 TRAIN articles
before building this (0 mismatches) -- see §60.9.

Writes to a NEW, separate root (`rl_training_data/bases_FORMULAB_DIAG/`) --
neither `rl_training_data/bases/` (current production) nor the Formula-B backup
is ever modified. Point `train_grpo.py` at the result via its new `--bases-dir`
override.

Usage (from research_agent_local/):
  python3 training/build_formulab_diag_bases.py
  python3 training/build_formulab_diag_bases.py --dry-run
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_TODAY_BASES = _REPO_ROOT / "rl_training_data" / "bases"
_FORMULAB_BACKUP = _REPO_ROOT / "rl_training_data" / "bases_ORACLE_BACKUP_20260708_231117"
_OUT_DIR = _REPO_ROOT / "rl_training_data" / "bases_FORMULAB_DIAG"

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

# Files needed by train_grpo.py::load_section_groups() -- today's model-input
# side (unchanged pipeline) vs. the reward-label side (Formula-B backup).
_FROM_TODAY = ["research_digest.md", "guideline_features.json"]
_FROM_FORMULAB = ["section_oracle.json"]


def build_article(article: str, dry_run: bool) -> bool:
    today_dir = _TODAY_BASES / article
    fb_dir = _FORMULAB_BACKUP / article
    out_dir = _OUT_DIR / article

    missing = [f for f in _FROM_TODAY if not (today_dir / f).exists()]
    missing += [f for f in _FROM_FORMULAB if not (fb_dir / f).exists()]
    if missing:
        print(f"  SKIP {article}: missing {missing}")
        return False

    if dry_run:
        print(f"  WOULD BUILD: {out_dir}  "
              f"(digest+features from bases/, section_oracle.json from Formula-B backup)")
        return True

    out_dir.mkdir(parents=True, exist_ok=True)
    for f in _FROM_TODAY:
        shutil.copy2(today_dir / f, out_dir / f)
    for f in _FROM_FORMULAB:
        shutil.copy2(fb_dir / f, out_dir / f)
    print(f"  BUILT: {out_dir}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_TRAIN_ARTICLES)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("=" * 80)
    print("BUILD FORMULA-B DIAGNOSTIC BASES (today's digests + Formula-B reward labels)")
    print(f"Today's bases:     {_TODAY_BASES}")
    print(f"Formula-B backup:  {_FORMULAB_BACKUP}")
    print(f"Output:            {_OUT_DIR}")
    print("=" * 80)

    ok = sum(build_article(a, args.dry_run) for a in args.articles)
    print()
    print(f"Done: {ok}/{len(args.articles)} article(s) built.")
    return 0 if ok == len(args.articles) else 1


if __name__ == "__main__":
    raise SystemExit(main())
