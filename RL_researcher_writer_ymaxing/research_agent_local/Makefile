# run the client in different modes for a single episode

run-stdio:
	uv run --project mcp_client python -m mcp_client.src.client 

test-server:
	uv run --project mcp_server pytest mcp_server/tests/

# --------------------------------------------------------------------------- #
# Batch runner
# Usage examples:
#   make run-batch                              # interactive mode, no initial batch
#   make run-batch SAMPLES_DIR=data/batch       # initial batch from a parent dir, then interactive
#   make run-batch SAMPLES=data/s1 data/s2      # explicit sample dirs, then interactive
#   make run-batch-ci SAMPLES_DIR=data/batch    # non-interactive (CI/script)
#   make run-batch-two-variants SAMPLES_DIR=data/batch
#   make run-batch-dry-run SAMPLES_DIR=data/batch
# --------------------------------------------------------------------------- #

# Optional inputs (may be overridden on the command line)
SAMPLES_DIR ?=
SAMPLES     ?=

# Build --samples-dir and --sample flags from the provided variables
_SAMPLES_DIR_FLAG = $(if $(SAMPLES_DIR),--samples-dir $(SAMPLES_DIR),)
_SAMPLES_FLAG     = $(foreach s,$(SAMPLES),--sample $(s))
_BATCH_FLAGS      = $(_SAMPLES_DIR_FLAG) $(_SAMPLES_FLAG)

# Interactive batch runner (default: no initial batch, stays alive for more)
run-batch:
	uv run --project mcp_client python -m mcp_client.src.batch_runner $(_BATCH_FLAGS)

# Non-interactive (CI/script): process the batch and exit
run-batch-ci:
	uv run --project mcp_client python -m mcp_client.src.batch_runner $(_BATCH_FLAGS) --non-interactive

# Two-variant mode: generates research_no_exploration.md + research.md per sample
run-batch-two-variants:
	uv run --project mcp_client python -m mcp_client.src.batch_runner $(_BATCH_FLAGS) --two-variants

# Two-variant mode, non-interactive
run-batch-two-variants-ci:
	uv run --project mcp_client python -m mcp_client.src.batch_runner $(_BATCH_FLAGS) --two-variants --non-interactive

# Dry-run: list samples that would be processed without running anything
run-batch-dry-run:
	uv run --project mcp_client python -m mcp_client.src.batch_runner $(_BATCH_FLAGS) --dry-run