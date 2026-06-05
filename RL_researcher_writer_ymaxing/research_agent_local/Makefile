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

# --------------------------------------------------------------------------- #
# RL data generator (Phase 1)
# Usage examples:
#   make run-rl-gen-dry                                    # show plan, no execution
#   make run-rl-gen                                        # full pipeline (all articles × all presets)
#   make run-rl-gen ARTICLES="02_workflows_vs_agents" PRESETS="0 1"
# --------------------------------------------------------------------------- #

ARTICLES ?=
PRESETS  ?=

_ARTICLES_FLAG = $(if $(ARTICLES),--articles $(ARTICLES),)
_PRESETS_FLAG  = $(if $(PRESETS),--presets $(PRESETS),)
_RL_FLAGS      = $(_ARTICLES_FLAG) $(_PRESETS_FLAG)

run-rl-gen-dry:
	uv run --project mcp_server python training/rl_data_generator.py --dry-run $(_RL_FLAGS)

run-rl-gen:
	uv run --project mcp_server python training/rl_data_generator.py $(_RL_FLAGS)

# --------------------------------------------------------------------------- #
# GRPO training  (Phase 2)
# PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True prevents OOM on tight-VRAM
# GPUs by letting the CUDA caching allocator grow segments incrementally
# instead of failing on fragmented free blocks.
#
# Usage examples:
#   make train-grpo                                        # default settings
#   make train-grpo TASK_ID=run02 EPOCHS=300 LR=5e-5
#   make train-grpo-section TASK_ID=run02_section
#   make train-grpo TRAIN_FLAGS="--resume"
#   make train-grpo-dry                                    # verify setup, no training
# --------------------------------------------------------------------------- #

TASK_ID     ?= run02_section_rh_r8
EPOCHS      ?= 300
LR          ?= 5e-5
LORA_R      ?= 8
LORA_ALPHA  ?= 8
TRAIN_FLAGS ?=

# NOTE: PYTORCH_CUDA_ALLOC_CONF must be placed immediately before the command
# that spawns the Python process (uv run), NOT before `cd`.  In bash,
# VAR=value cmd only sets VAR for that single command; subsequent commands
# joined by && run in the original environment.
_TRAIN_CMD = cd training && PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True uv run python train_grpo.py \
	--task-id $(TASK_ID) \
	--epochs $(EPOCHS) \
	--lr $(LR) \
	--lora-r $(LORA_R) \
	--lora-alpha $(LORA_ALPHA) \
	$(TRAIN_FLAGS)

train-grpo:
	$(_TRAIN_CMD)

train-grpo-section:
	$(_TRAIN_CMD) --granularity section

train-grpo-resume:
	$(_TRAIN_CMD) --resume

train-grpo-section-resume:
	$(_TRAIN_CMD) --granularity section --resume

train-grpo-dry:
	$(_TRAIN_CMD) --dry-run

