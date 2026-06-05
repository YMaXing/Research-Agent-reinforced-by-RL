"""
Fix two issues with L10 episodes:

Problem 1 (preset2 — Medium article behind paywall):
  - Delete the scraped file.
  - Remove the <research_source> block AND the Source [50] entry from research.md.

Problem 2 (preset4 — hippocampal PDF):
  - Strip the REFERENCES section (line 867 onward) from the scraped file.
  - Append the article (without references) to research.md as a new <research_source> block.
"""
import sys
from pathlib import Path

_TRAINING_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _TRAINING_DIR.parent / "mcp_server"
sys.path.insert(0, str(_MCP_SERVER_DIR))

EPISODES_DIR = _TRAINING_DIR.parent.parent / "rl_training_data" / "episodes"

# ─── Paths ────────────────────────────────────────────────────────────────────
P2_DIR   = EPISODES_DIR / "10_memory_knowledge_access__preset2"
P2_FILE  = P2_DIR / ".research" / "urls_from_research" / "agent-memory-the-key-to-salient-episodic-memory-for-ai-agents.md"
P2_RESEARCH = P2_DIR / "research.md"

P4_DIR   = EPISODES_DIR / "10_memory_knowledge_access__preset4"
P4_FILE  = P4_DIR / ".research" / "urls_from_research" / "the-hippocampal-indexing-theory-and-episodic-memory-updating.md"
P4_RESEARCH = P4_DIR / "research.md"

# ─── Problem 1: preset2 Medium article ────────────────────────────────────────
print("=== Problem 1: preset2 Medium article ===")

# 1a. Delete the scraped file
if P2_FILE.exists():
    P2_FILE.unlink()
    print(f"  Deleted: {P2_FILE.name}")
else:
    print(f"  Already absent: {P2_FILE.name}")

# 1b. Remove from research.md
text = P2_RESEARCH.read_text(encoding="utf-8")

# Remove the <research_source> block for the Medium article
MEDIUM_BLOCK_START = '<research_source type="scraped_from_research" phase="exploration" file="agent-memory-the-key-to-salient-episodic-memory-for-ai-agents.md">'
MEDIUM_BLOCK_END   = "</research_source>"

start_idx = text.find(MEDIUM_BLOCK_START)
if start_idx == -1:
    print("  ⚠️  Could not find <research_source> block for Medium article in research.md")
else:
    # Find the closing tag after the start
    end_idx = text.find(MEDIUM_BLOCK_END, start_idx)
    if end_idx == -1:
        print("  ⚠️  Could not find closing </research_source> for Medium article")
    else:
        end_idx += len(MEDIUM_BLOCK_END)
        # Also consume the trailing newline(s) so we don't leave a blank gap
        while end_idx < len(text) and text[end_idx] in "\n":
            end_idx += 1
        text = text[:start_idx] + text[end_idx:]
        print("  Removed <research_source> block from research.md")

# Remove the "Source [50]" entry in the Tavily/source-list section
# Pattern: "-----\n\nPhase: ...\n\n### Source [50]: https://medium.com/...\n\n...\n\n-----"
MEDIUM_URL = "https://medium.com/@richardhightower/agent-memory-the-key-to-salient-episodic-memory-for-ai-agents-70b0f8e296db"
MARKER = f"### Source [50]: {MEDIUM_URL}"
src50_idx = text.find(MARKER)
if src50_idx == -1:
    print("  ⚠️  Could not find 'Source [50]' entry in research.md")
else:
    # Walk backward to consume the preceding "-----\n\nPhase: [EXPLORATION]\n\n"
    # We want to remove from the \n\n after the previous "-----" up to and including
    # the "-----" that follows this source entry.
    # Find the start of the block (go back to find the separator line "-----")
    block_start = text.rfind("\n-----\n", 0, src50_idx)
    if block_start == -1:
        print("  ⚠️  Could not find preceding separator for Source [50]")
    else:
        # block_start points to \n-----\n — include the \n before -----
        # Find the closing separator "-----" after the source entry
        block_end = text.find("\n-----\n", src50_idx)
        if block_end == -1:
            print("  ⚠️  Could not find trailing separator for Source [50]")
        else:
            block_end += len("\n-----\n")
            text = text[:block_start] + "\n-----\n" + text[block_end:]
            print("  Removed 'Source [50]' entry from research.md")

P2_RESEARCH.write_text(text, encoding="utf-8")
print("  Saved research.md for preset2")

# ─── Problem 2: preset4 hippocampal article ────────────────────────────────────
print("\n=== Problem 2: preset4 hippocampal article ===")

# 2a. Strip REFERENCES section from the scraped file
hippo_text = P4_FILE.read_text(encoding="utf-8")
hippo_lines = hippo_text.splitlines(keepends=True)

# Find the REFERENCES line
ref_line_idx = None
for i, line in enumerate(hippo_lines):
    if line.strip() == "REFERENCES":
        ref_line_idx = i
        break

if ref_line_idx is None:
    print("  ⚠️  Could not find REFERENCES line in hippocampal file")
else:
    # Keep lines before (and not including) REFERENCES; also strip the preceding separator
    # Lines before ref_line_idx typically end with "* * *\n\n" — keep that separator
    # but remove from "REFERENCES" onward.
    kept_lines = hippo_lines[:ref_line_idx]
    # Trim trailing blank lines after the last separator
    while kept_lines and kept_lines[-1].strip() == "":
        kept_lines.pop()
    hippo_stripped = "".join(kept_lines) + "\n"
    P4_FILE.write_text(hippo_stripped, encoding="utf-8")
    removed = len(hippo_lines) - ref_line_idx
    print(f"  Stripped REFERENCES section ({removed} lines removed). New length: {len(kept_lines)} lines.")

# 2b. Build the <research_source> block and insert into research.md before <golden_source>
hippo_content = P4_FILE.read_text(encoding="utf-8")

# Extract title from the first "# Title:" line in the file
title = "The hippocampal indexing theory and episodic memory: Updating the index"
for line in hippo_content.splitlines():
    if line.startswith("# Title:"):
        title = line[len("# Title:"):].strip()
        break

new_block = (
    f'<research_source type="scraped_from_research" phase="exploration" file="the-hippocampal-indexing-theory-and-episodic-memory-updating.md">\n'
    f"<details>\n"
    f"<summary>{title}</summary>\n"
    f"\n"
    f"{hippo_content}\n"
    f"</details>\n"
    f"\n"
    f"</research_source>\n"
    f"\n"
)

# Insert before <golden_source ...>
p4_text = P4_RESEARCH.read_text(encoding="utf-8")
GOLDEN_MARKER = "<golden_source "
golden_idx = p4_text.find(GOLDEN_MARKER)
if golden_idx == -1:
    print("  ⚠️  Could not find <golden_source> in preset4 research.md — appending at end")
    p4_text = p4_text + new_block
else:
    p4_text = p4_text[:golden_idx] + new_block + p4_text[golden_idx:]
    print("  Inserted hippocampal <research_source> block before <golden_source>")

P4_RESEARCH.write_text(p4_text, encoding="utf-8")
print("  Saved research.md for preset4")

print("\nDone.")
