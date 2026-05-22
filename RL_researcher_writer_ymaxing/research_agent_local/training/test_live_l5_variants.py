"""
Live verification of section_oracle.json and guideline_features.json
across the three lesson-5 variants (minimal / standard / demanding).

Run AFTER generate_digests.py has been executed with --force on all three:

    uv run python training/generate_digests.py \\
        --articles 05_workflow_patterns__var_minimal \\
                   05_workflow_patterns__var_standard \\
                   05_workflow_patterns__var_demanding \\
        --force

Then:

    uv run python training/test_live_l5_variants.py
"""

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
TRAINING_DIR = Path(__file__).parent
REPO_ROOT    = TRAINING_DIR.parent
BASES_DIR    = REPO_ROOT.parent / "rl_training_data" / "bases"

VARIANTS = [
    "05_workflow_patterns__var_minimal",
    "05_workflow_patterns__var_standard",
    "05_workflow_patterns__var_demanding",
]
VARIANT_LABELS = {"minimal": "minimal", "standard": "standard", "demanding": "demanding"}

PRESET_ORDER = {"skip": 0, "light": 1, "standard": 2, "deep": 3}
VALID_PRESETS = set(PRESET_ORDER)

FEATURE_KEYS = ["target_words", "mandatory_bullets", "must_cover_depth", "must_stay_brief"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _short(variant: str) -> str:
    return variant.split("__var_")[-1]


def _load(variant: str, filename: str) -> dict:
    path = BASES_DIR / variant / filename
    if not path.exists():
        print(f"  [MISSING] {path}")
        return {}
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _check_file_exists(variant: str, filename: str) -> bool:
    path = BASES_DIR / variant / filename
    if not path.exists():
        print(f"FAIL  {variant}/{filename} — file not found. Did you run the pipeline with --force?")
        return False
    print(f"OK    {variant}/{filename}")
    return True


# ---------------------------------------------------------------------------
# Check 1 — all output files exist
# ---------------------------------------------------------------------------

def check_files_exist() -> bool:
    print("\n=== CHECK 1: Output files exist ===")
    ok = True
    for v in VARIANTS:
        for fn in ("research_digest.md", "section_oracle.json", "guideline_features.json"):
            ok &= _check_file_exists(v, fn)
    return ok


# ---------------------------------------------------------------------------
# Check 2 — oracle preset tokens are all valid
# ---------------------------------------------------------------------------

def check_oracle_tokens() -> bool:
    print("\n=== CHECK 2: Oracle presets are valid tokens ===")
    ok = True
    for v in VARIANTS:
        oracle = _load(v, "section_oracle.json")
        presets: dict[str, str] = oracle.get("presets", {})
        bad = {k: p for k, p in presets.items() if p not in VALID_PRESETS}
        if bad:
            print(f"FAIL  {_short(v)}: invalid presets {bad}")
            ok = False
        else:
            print(f"OK    {_short(v)}: {len(presets)} sections, "
                  f"presets={sorted(set(presets.values()))}")
    return ok


# ---------------------------------------------------------------------------
# Check 3 — feature keys are present and non-negative integers
# ---------------------------------------------------------------------------

def check_feature_schema() -> bool:
    print("\n=== CHECK 3: Feature schema is correct ===")
    ok = True
    for v in VARIANTS:
        feats = _load(v, "guideline_features.json")
        policy = feats.get("external_evidence_policy", "")
        if policy not in ("forbidden", "allowed", "required"):
            print(f"FAIL  {_short(v)}: bad external_evidence_policy={policy!r}")
            ok = False
        sections: dict = feats.get("sections", {})
        if not sections:
            print(f"FAIL  {_short(v)}: no sections in guideline_features.json")
            ok = False
            continue
        for sec_id, sec in sections.items():
            for k in FEATURE_KEYS:
                v_ = sec.get(k)
                if not isinstance(v_, int) or v_ < 0:
                    print(f"FAIL  {_short(v)}: {sec_id}.{k} = {v_!r} (expected non-negative int)")
                    ok = False
        if ok:
            print(f"OK    {_short(v)}: policy={policy!r}, {len(sections)} sections")
    return ok


# ---------------------------------------------------------------------------
# Check 4 — variants show monotone feature ordering (minimal ≤ standard ≤ demanding)
# for target_words and mandatory_bullets (the two headline dims)
# ---------------------------------------------------------------------------

def check_feature_ordering() -> bool:
    print("\n=== CHECK 4: Feature ordering — demanding ≥ standard ≥ minimal ===")

    all_feats = {v: _load(v, "guideline_features.json") for v in VARIANTS}

    # Collect all section ids that appear in all three
    section_sets = [set(all_feats[v].get("sections", {}).keys()) for v in VARIANTS]
    common = section_sets[0] & section_sets[1] & section_sets[2]
    if not common:
        print("FAIL  No section ids are shared across all three variants — "
              "check that section IDs are deterministically generated.")
        return False

    print(f"  Shared section ids ({len(common)}): {sorted(common)}")
    print()

    ok = True
    col_w = 12
    header = f"  {'section':<35} {'key':<20}" + "".join(
        f" {_short(v):>{col_w}}" for v in VARIANTS
    )
    print(header)
    print("  " + "-" * (len(header) - 2))

    for sec_id in sorted(common):
        for key in ("target_words", "mandatory_bullets"):
            vals = [all_feats[v]["sections"][sec_id].get(key, 0) for v in VARIANTS]
            # Check monotone (minimal ≤ standard ≤ demanding)
            mono = vals[0] <= vals[1] <= vals[2]
            flag = "   " if mono else "!!!"
            print(f"  {flag}{sec_id:<33} {key:<20}" +
                  "".join(f" {v:>{col_w}}" for v in vals))
            if not mono:
                ok = False

    if ok:
        print("\n  All features are monotonically non-decreasing across variants.")
    else:
        print("\n  Some features violate monotone ordering — see !!! rows above.")
    return ok


# ---------------------------------------------------------------------------
# Check 5 — oracle presets show ordering (minimal ≤ standard ≤ demanding)
# ---------------------------------------------------------------------------

def check_preset_ordering() -> bool:
    print("\n=== CHECK 5: Oracle preset ordering — demanding ≥ standard ≥ minimal ===")

    all_oracles = {v: _load(v, "section_oracle.json").get("presets", {}) for v in VARIANTS}
    common = (
        set(all_oracles[VARIANTS[0]]) &
        set(all_oracles[VARIANTS[1]]) &
        set(all_oracles[VARIANTS[2]])
    )
    if not common:
        print("FAIL  No common section ids across oracle files.")
        return False

    ok = True
    col_w = 10
    header = f"  {'section':<35}" + "".join(
        f" {_short(v):>{col_w}}" for v in VARIANTS
    ) + "  ordering"
    print(header)
    print("  " + "-" * (len(header) - 2))

    violations = 0
    for sec_id in sorted(common):
        presets = [all_oracles[v].get(sec_id, "skip") for v in VARIANTS]
        ranks   = [PRESET_ORDER.get(p, -1) for p in presets]
        mono    = ranks[0] <= ranks[1] <= ranks[2]
        flag    = "   " if mono else "!!!"
        order_str = "≤".join(f"r{r}" for r in ranks)
        print(f"  {flag}{sec_id:<33}" +
              "".join(f" {p:>{col_w}}" for p in presets) +
              f"  {order_str}")
        if not mono:
            violations += 1
            ok = False

    # Summary
    n = len(common)
    print(f"\n  Shared sections checked: {n}")
    if ok:
        print(f"  All {n} sections satisfy ordering.")
    else:
        print(f"  {violations}/{n} sections violate ordering — "
              "some are expected if sections are short/self-contained in all variants.")

    # Warn if any variant's oracle is missing sections relative to its features
    for v in VARIANTS:
        feats = _load(v, "guideline_features.json")
        oracle_keys = set(all_oracles[v].keys())
        feat_keys   = set(feats.get("sections", {}).keys())
        missing = feat_keys - oracle_keys
        if missing:
            print(f"  WARN  {_short(v)}: {len(missing)} section(s) in features but missing from oracle: {sorted(missing)}")

    return ok


# ---------------------------------------------------------------------------
# Check 6 — build_rl_input produces valid {system, user} for each section
# ---------------------------------------------------------------------------

def check_build_rl_input() -> bool:
    print("\n=== CHECK 6: build_rl_input produces valid dicts ===")

    # Import from the training package
    sys.path.insert(0, str(TRAINING_DIR.parent))
    try:
        from training.generate_digests import build_rl_input, _RL_INPUT_SYSTEM
    except ImportError as e:
        print(f"FAIL  Could not import generate_digests: {e}")
        return False

    ok = True
    for v in VARIANTS:
        digest_path = BASES_DIR / v / "research_digest.md"
        if not digest_path.exists():
            print(f"SKIP  {_short(v)}: no digest")
            continue

        digest = digest_path.read_text(encoding="utf-8")

        # Extract section ids from gap_profile
        sec_ids = re.findall(r'<section\s+id="([^"]+)"', digest)
        if not sec_ids:
            print(f"FAIL  {_short(v)}: no sections in digest gap_profile")
            ok = False
            continue

        errs = []
        for sec_id in sec_ids:
            result = build_rl_input(digest, sec_id)
            if not isinstance(result, dict):
                errs.append(f"{sec_id}: not a dict")
                continue
            if result.get("system") is not _RL_INPUT_SYSTEM:
                errs.append(f"{sec_id}: system prompt is not _RL_INPUT_SYSTEM")
            user = result.get("user", "")
            if "skip, light, standard, or deep" not in user:
                errs.append(f"{sec_id}: task token list missing from user message")
            if sec_id not in user:
                errs.append(f"{sec_id}: section id not in user message")
            # Check that 4 feature attrs appear in user message (injected into gap_profile)
            for attr in ("target_words", "mandatory_bullets", "must_cover_depth", "must_stay_brief"):
                if attr not in user:
                    errs.append(f"{sec_id}: '{attr}' missing from user gap_profile")

        if errs:
            print(f"FAIL  {_short(v)}: {len(errs)} error(s)")
            for e in errs[:5]:
                print(f"        {e}")
            ok = False
        else:
            print(f"OK    {_short(v)}: {len(sec_ids)} sections, "
                  f"all build_rl_input calls valid, "
                  f"user msg ~{sum(len(build_rl_input(digest,s)['user']) for s in sec_ids) // len(sec_ids):,} chars avg")
    return ok


# ---------------------------------------------------------------------------
# Check 7 — gap_profile in digest has feature attrs injected
# ---------------------------------------------------------------------------

def check_digest_feature_injection() -> bool:
    print("\n=== CHECK 7: Feature attrs injected into digest <gap_profile> ===")
    ok = True
    for v in VARIANTS:
        digest_path = BASES_DIR / v / "research_digest.md"
        if not digest_path.exists():
            print(f"SKIP  {_short(v)}: no digest")
            continue
        digest = digest_path.read_text(encoding="utf-8")
        # Find all <section .../> rows in gap_profile
        rows = re.findall(r'<section\s+id="[^"]+"\s+need_depth="\d+"[^/]*/>', digest)
        missing_attrs = []
        for row in rows:
            for attr in ("target_words", "mandatory_bullets", "must_cover_depth", "must_stay_brief"):
                if attr not in row:
                    missing_attrs.append(f"{row[:60]}... missing {attr}")
        if missing_attrs:
            print(f"FAIL  {_short(v)}: {len(missing_attrs)} row(s) missing attrs")
            for m in missing_attrs[:3]:
                print(f"        {m}")
            ok = False
        else:
            print(f"OK    {_short(v)}: {len(rows)} gap_profile rows all have 4 feature attrs")
    return ok


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 65)
    print("LIVE TEST: lesson-5 variant trio (minimal / standard / demanding)")
    print("=" * 65)

    results: dict[str, bool] = {}

    results["files_exist"]      = check_files_exist()
    if not results["files_exist"]:
        print("\nPipeline output missing — run generate_digests.py with --force first.")
        return 1

    results["oracle_tokens"]    = check_oracle_tokens()
    results["feature_schema"]   = check_feature_schema()
    results["feature_ordering"] = check_feature_ordering()
    results["preset_ordering"]  = check_preset_ordering()
    results["build_rl_input"]   = check_build_rl_input()
    results["digest_injection"] = check_digest_feature_injection()

    print("\n" + "=" * 65)
    print("SUMMARY")
    print("=" * 65)
    all_ok = True
    for name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {status}  {name}")
        all_ok &= passed

    if all_ok:
        print("\nAll checks passed.")
    else:
        print("\nSome checks failed — see details above.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
