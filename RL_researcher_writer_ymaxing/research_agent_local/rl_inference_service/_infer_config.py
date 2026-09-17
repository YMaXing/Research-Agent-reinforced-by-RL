"""Single source of truth for infer.py's default adapter checkpoint.

Deliberately has NO heavy dependencies (stdlib only) so
preset_infer_handler.py -- running in the mcp_server's own venv, not this
service's venv -- can import it cheaply to find out what the "current
default" checkpoint is, without needing torch/transformers/peft installed.

infer.py imports DEFAULT_ADAPTER_DIR from here instead of defining its own
copy, so there is exactly one place to edit when shipping a new checkpoint.
"""
from __future__ import annotations

from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent

# The pinned production checkpoint lives IN this package (checkpoints/production/),
# copied from rl_training_data/checkpoints/tasks/<run>/epochs/<epoch>/ once a run
# is chosen for production -- decoupled from the full experiment archive there
# (which keeps every checkpoint from every run and is not a stable pointer).
# Update this line when shipping a new checkpoint -- both infer.py's CLI
# default and preset_infer_handler.py's stale-server detection read it.
DEFAULT_ADAPTER_DIR: Path = _THIS_DIR / "checkpoints" / "production"
