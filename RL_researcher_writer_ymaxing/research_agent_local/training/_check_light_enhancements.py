import json, re
from pathlib import Path

ROOT = Path("../../rl_training_data").resolve()
DRAWS = {
    "production": ROOT / "test_episodes" / "State_of_LLM_Reasoning__preset1" / "reasoning.json",
    "replicate1": ROOT / "noise_experiment" / "State_of_LLM_Reasoning__replicate1__preset1" / "reasoning.json",
    "replicate2": ROOT / "noise_experiment" / "State_of_LLM_Reasoning__replicate2__preset1" / "reasoning.json",
}

# Each metric's text is a sequence of "<section title>:\n**<score>:** <reasoning...>" blocks
# separated by blank lines, in section order.
BLOCK_RE = re.compile(r"^(.*?):\n\*\*(\d+):\*\*\s*(.*)$", re.DOTALL)


def split_sections(text: str) -> list[tuple[str, int, str]]:
    # Sections are separated by "\n\n" at top level; titles never contain "\n\n".
    parts = re.split(r"\n\n(?=[^\n]+:\n\*\*\d+:\*\*)", text.strip())
    out = []
    for p in parts:
        m = re.match(r"^(.*?):\n\*\*(\d+):\*\*\s*(.*)$", p.strip(), re.DOTALL)
        if m:
            title, score, rest = m.group(1).strip(), int(m.group(2)), m.group(3)
            inst_m = re.search(r"\[instances=(\d+)", rest)
            instances = int(inst_m.group(1)) if inst_m else None
            out.append((title, score, instances))
    return out


for draw_name, path in DRAWS.items():
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"\n=== {draw_name} ===")
    for metric in ("ground_truth_depth_enhancement", "ground_truth_breadth_enhancement"):
        text = data.get(metric, "")
        sections = split_sections(text)
        hits = [(t, s, i) for t, s, i in sections if s == 1 and (i or 0) > 0]
        print(f"  {metric}: {len(sections)} sections parsed, {len(hits)} with score=1 & instances>0")
        for t, s, i in hits:
            print(f"    -> {t}  (instances={i})")
