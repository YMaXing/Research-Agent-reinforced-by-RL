"""Re-generate research.md for episodes whose scraped files were replaced."""
import sys
from pathlib import Path

_TRAINING_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _TRAINING_DIR.parent / "mcp_server"
sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv
load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

from src.tools.create_research_file_tool import create_research_file_tool

EPISODES_DIR = _TRAINING_DIR.parent.parent / "rl_training_data" / "episodes"

TARGETS = [
    "10_memory_knowledge_access__preset2",
    "10_memory_knowledge_access__preset4",
]

for ep_name in TARGETS:
    ep_dir = EPISODES_DIR / ep_name
    print(f"Regenerating {ep_name} ...", flush=True)
    result = create_research_file_tool(str(ep_dir))
    status = result.get("status", "?")
    msg = result.get("message", str(result))
    print(f"  {status}: {msg}", flush=True)

print("Done.")
