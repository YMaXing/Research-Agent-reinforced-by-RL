"""Single source of truth for infer.py's default adapter checkpoint.

Deliberately has NO heavy dependencies (stdlib only) so
preset_infer_handler.py -- running in the mcp_server's own venv, not the
training venv -- can import it cheaply to find out what the "current
default" checkpoint is, without needing torch/transformers/peft installed.

infer.py imports DEFAULT_ADAPTER_DIR from here instead of defining its own
copy, so there is exactly one place to edit when shipping a new checkpoint.
"""
from __future__ import annotations

from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent  # RL_researcher_writer_ymaxing/

# Update this line when shipping a new checkpoint -- both infer.py's CLI
# default and preset_infer_handler.py's stale-server detection read it.
DEFAULT_ADAPTER_DIR: Path = (
    _REPO_ROOT / "rl_training_data" / "checkpoints" / "tasks"
    / "run33_averaged_confidence" / "epochs" / "epoch_0081"
)
