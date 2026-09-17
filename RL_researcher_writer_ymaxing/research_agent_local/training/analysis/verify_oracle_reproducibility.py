"""Phase 0 data-integrity check (A.16.7): recompute every production
``section_oracle.json`` cell-for-cell via ``generate_episode_oracles.py``'s
REAL code path (``process_article_variant(..., dry_run=True, return_data=True)``)
and assert 100% agreement against the stored file.

Why this exists: three silent bugs were found in this investigation (TRAIN-only
preset mapping applied to TEST articles, a missing v4+ "explore" split in
merge_replicate_oracles.py, and an ordinal-index misalignment from duplicated
digest section ids) -- each produced plausible-looking numbers and survived
multiple manual review passes. All three would have been caught INSTANTLY by
this check, because it reuses production's own function rather than a parallel
re-implementation (which is exactly how bug #3 was introduced elsewhere).
See run13_rl_grok_pipeline_analysis.md A.16.0/A.16.7.

Run this BEFORE trusting any tool that reads section_oracle.json for a
label-consuming job (merge_replicate_oracles.py, a retrain, etc.) and in CI.

Read-only: dry_run=True means generate_episode_oracles.py never writes.

Usage (from research_agent_local/):
  python3 training/verify_oracle_reproducibility.py
  python3 training/verify_oracle_reproducibility.py --articles 13_agent_framework 06_tools
  python3 training/verify_oracle_reproducibility.py --verbose

Exit code: 0 if every article matches, 1 if any mismatch or article failed to recompute.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import generate_episode_oracles as geo  # noqa: E402

_TOL = 1e-6


def _split_art_var(dir_name: str) -> tuple[str, str | None]:
    """(article, variant) from a bases/ dir name, mirroring process_article_variant's
    own convention: '{article}__var_X' -> (article, 'var_X'); anything else -> (dir_name, None)."""
    for v in geo._VARIANTS:
        suffix = f"__{v}"
        if dir_name.endswith(suffix):
            return dir_name[: -len(suffix)], v
    return dir_name, None


def _diff_sections(stored: dict, recomputed: dict, art_var: str, verbose: bool) -> list[str]:
    problems = []
    stored_ids = set(stored.keys())
    recomputed_ids = set(recomputed.keys())
    if stored_ids != recomputed_ids:
        only_stored = stored_ids - recomputed_ids
        only_recomp = recomputed_ids - stored_ids
        problems.append(
            f"{art_var}: section-id set mismatch (only in stored: {sorted(only_stored)}, "
            f"only in recompute: {sorted(only_recomp)})"
        )

    for sid in sorted(stored_ids & recomputed_ids):
        s, r = stored[sid], recomputed[sid]
        if s.get("oracle") != r.get("oracle"):
            problems.append(f"{art_var}/{sid}: oracle arm differs stored={s.get('oracle')} recomputed={r.get('oracle')}")
        for field in ("rewards", "explore"):
            s_vals, r_vals = s.get(field, {}), r.get(field, {})
            for arm in geo._ARM_ORDER:
                sv, rv = float(s_vals.get(arm, 0.0)), float(r_vals.get(arm, 0.0))
                if abs(sv - rv) > _TOL:
                    problems.append(
                        f"{art_var}/{sid}/{arm}/{field}: stored={sv:.6f} recomputed={rv:.6f} "
                        f"diff={rv - sv:+.6f}"
                    )
        if verbose and not any(sid in p for p in problems):
            print(f"    OK  {art_var}/{sid}")
    return problems


def verify_article(dir_name: str, bases_dir: Path, verbose: bool) -> tuple[bool, list[str]]:
    oracle_path = bases_dir / dir_name / "section_oracle.json"
    if not oracle_path.exists():
        return True, []  # nothing to verify, not a failure

    stored = json.loads(oracle_path.read_text(encoding="utf-8")).get("sections", {})
    if not stored:
        return True, []

    article, variant = _split_art_var(dir_name)
    ok, recomputed = geo.process_article_variant(article, variant, dry_run=True, return_data=True)
    if not ok or recomputed is None:
        return False, [f"{dir_name}: process_article_variant() failed to recompute (see warnings above)"]

    problems = _diff_sections(stored, recomputed, dir_name, verbose)
    return (len(problems) == 0), problems


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=None,
                         help="Only verify these bases/ directory names (default: every dir with a section_oracle.json).")
    parser.add_argument("--verbose", action="store_true", help="Print every section checked, not just mismatches.")
    args = parser.parse_args()

    bases_dir = geo._BASES_DIR
    if args.articles:
        dir_names = args.articles
    else:
        dir_names = sorted(
            d.name for d in bases_dir.iterdir()
            if d.is_dir() and (d / "section_oracle.json").exists()
        )

    print(f"Verifying {len(dir_names)} article(s) under {bases_dir}\n")

    n_ok = n_fail = n_cells_total = 0
    all_problems: list[str] = []
    for dir_name in dir_names:
        ok, problems = verify_article(dir_name, bases_dir, args.verbose)
        n_cells_total += 1
        if ok:
            n_ok += 1
            print(f"  PASS  {dir_name}")
        else:
            n_fail += 1
            print(f"  FAIL  {dir_name}  ({len(problems)} problem(s))")
            all_problems.extend(problems)

    print(f"\n{'=' * 90}")
    print(f"{n_ok}/{n_cells_total} articles fully reproducible, {n_fail} with mismatches")
    print(f"{'=' * 90}")

    if all_problems:
        print("\nDetail:")
        for p in all_problems:
            print(f"  - {p}")
        print(f"\nRESULT: FAIL -- section_oracle.json is NOT reproducible from raw reasoning.json "
              f"for {n_fail} article(s). Do not trust merge/replicate/retrain output until fixed.")
        sys.exit(1)

    print("\nRESULT: PASS -- every section_oracle.json cell reproduces exactly from raw reasoning.json.")
    sys.exit(0)


if __name__ == "__main__":
    main()
