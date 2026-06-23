"""Quick test for the fixed extraction functions."""
import sys, os
os.chdir(os.path.dirname(__file__))
sys.path.insert(0, "mcp_server/src")

import json
from app.guideline_extractions_handler import extract_local_paths, extract_local_paths_by_section

guideline = open(
    "rl_training_data/bases/Bird_Eye_Extreme/article_guideline.md", encoding="utf-8"
).read()

by_section = extract_local_paths_by_section(guideline)
flat       = extract_local_paths(guideline)

print("=== extract_local_paths_by_section ===")
print("golden      :", by_section["golden"])
print("exploitation:", by_section["exploitation"])
print()
print("=== extract_local_paths (flat) ===")
print(flat)
