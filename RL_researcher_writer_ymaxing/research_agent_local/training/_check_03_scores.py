"""
Audit all section-level scores for article 03 (context engineering) across
all variants (base, minimal, standard, demanding) and all 6 presets.
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent.parent / "rl_training_data" / "episodes"
VARIANTS = ["", "__var_minimal", "__var_standard", "__var_demanding"]
ALL_DIMS = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
]
DIM_ABBR = {
    "ground_truth_core_content":        "cc",
    "ground_truth_flow":                "fl",
    "ground_truth_depth_enhancement":   "de",
    "ground_truth_breadth_enhancement": "be",
    "ground_truth_core_preservation":   "cp",
    "user_intent_guideline_adherence":  "ga",
    "user_intent_research_anchoring":   "ra",
}
VAR_LABELS = {
    "": "BASE",
    "__var_minimal": "MINIMAL",
    "__var_standard": "STANDARD",
    "__var_demanding": "DEMANDING",
}

# Format: "Section Title:\n**score:** reasoning..."
# \n is a REAL newline (code 10). We split on \n\n to get paragraphs,
# then find lines ending with ":" followed by "**0**" or "**1**" on the next line.
def parse_sections(text: str) -> dict[str, int]:
    result: dict[str, int] = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        # Check if next non-empty line starts with **0** or **1**
        if line.endswith(":"):
            # Look ahead for the score
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines):
                next_line = lines[j].lstrip()
                m = re.match(r'^\*\*([01]):\*\*', next_line)
                if m:
                    title = line[:-1].strip()  # remove trailing colon
                    result[title] = int(m.group(1))
                    i = j + 1
                    continue
        i += 1
    return result


def main() -> None:
    issues: list[dict] = []

    for var in VARIANTS:
        vlabel = VAR_LABELS[var]
        for preset in range(6):
            ep_name = f"03_context_engineering{var}__preset{preset}"
            rjson = BASE / ep_name / "reasoning.json"
            if not rjson.exists():
                print(f"MISSING: {ep_name}/reasoning.json")
                continue

            data: dict = json.loads(rjson.read_text(encoding="utf-8"))

            sec_scores: dict[str, dict[str, int]] = {}
            sec_order: list[str] = []

            for dim in ALL_DIMS:
                abbr = DIM_ABBR[dim]
                val = data.get(dim, "")
                if not isinstance(val, str):
                    continue
                parsed = parse_sections(val)
                for sec, score in parsed.items():
                    sec_scores.setdefault(sec, {})[abbr] = score
                    if sec not in sec_order:
                        sec_order.append(sec)

            if not sec_scores:
                print(f"PARSE FAIL: {ep_name}")
                # Debug: show first 200 chars of cc dim
                print(f"  cc dim preview: {repr(data.get('ground_truth_core_content','')[:200])}")
                continue

            print(f"\n=== [{vlabel}] P{preset} — {len(sec_order)} sections ===")
            hdr = f"  {'idx':>3}  {'Section':<48}  cc fl de be cp | ga ra  flags"
            print(hdr)
            print("  " + "-" * (len(hdr) - 2))

            for idx, sec in enumerate(sec_order):
                s = sec_scores[sec]
                gt_zero = all(s.get(a, "?") == 0 for a in ["cc", "fl", "de", "be", "cp"])
                flags = []
                if s.get("cc", "?") == 0:
                    flags.append("cc=0")
                if gt_zero:
                    flags.append("ALL-GT-0")
                flag_str = "  << " + " ".join(flags) if flags else ""
                vals = " ".join(str(s.get(a, "?")) for a in ["cc", "fl", "de", "be", "cp"])
                ui_vals = " ".join(str(s.get(a, "?")) for a in ["ga", "ra"])
                row = f"  {idx:>3}  {sec:<48}  {vals} | {ui_vals}{flag_str}"
                print(row)
                if flags:
                    issues.append({
                        "var": vlabel, "p": preset, "idx": idx,
                        "sec": sec, "s": dict(s), "flags": flags,
                    })

    print("\n\n" + "=" * 70)
    print("ISSUE SUMMARY")
    print("=" * 70)
    if not issues:
        print("  No anomalous sections found.")
    else:
        prev = None
        for iss in issues:
            if iss["var"] != prev:
                print(f"\n  [{iss['var']}]")
                prev = iss["var"]
            sc = iss["s"]
            sc_str = " ".join(f"{a}={sc.get(a, '?')}" for a in ["cc", "fl", "de", "be", "cp", "ga", "ra"])
            print(f"    P{iss['p']} idx{iss['idx']:>2}  {iss['sec']:<48}  {sc_str}  [{', '.join(iss['flags'])}]")
    print(f"\nTotal anomalous section×preset pairs: {len(issues)}")


if __name__ == "__main__":
    main()
