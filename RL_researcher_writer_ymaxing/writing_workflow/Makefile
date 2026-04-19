ifeq (,$(wildcard .env))
$(error .env file is missing. Please create one based on .env.example. Run: "cp .env.example .env" and fill in the missing values.)
endif

include .env
export

export UV_PROJECT_ENVIRONMENT=.venv
export PYTHONPATH = ./src/

.PHONY: tests

# --- Default Values ---

QA_FOLDERS := src/ tests/ scripts/
DIR_PATH ?= inputs/tests/00_debug
HUMAN_FEEDBACK ?=
TRANSPORT_ARG := $(if $(TRANSPORT),--transport $(TRANSPORT),)

# --- Utilities ---DIR_PATH

help: # Display this help message with a list of available commands.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

build: # Build the project.
	uv sync

# --- Agents ---

brown-generate-article: # Run the Brown MCP client to generate an article.
	uv run python scripts/brown_mcp_cli.py generate-article --dir-path $(DIR_PATH)

brown-edit-article: # Run the Brown MCP client to edit an article.
	uv run python scripts/brown_mcp_cli.py edit-article --dir-path $(DIR_PATH) --human-feedback $(HUMAN_FEEDBACK)

brown-edit-selected-text: # Run the Brown MCP client to a selected text section of an article.
	uv run python scripts/brown_mcp_cli.py edit-text --dir-path $(DIR_PATH) --human-feedback $(HUMAN_FEEDBACK) --first-line $(FIRST_LINE) --last-line $(LAST_LINE)

# --- RL Training Data ---

rl-writing-generate: # Phase 2a: Generate article.md for all RL training episodes.
	uv run python rl_writing_generator.py

rl-writing-dry-run: # Phase 2a dry run: Show plan without executing.
	uv run python rl_writing_generator.py --dry-run

rl-grading-generate: # Phase 2b: Grade article.md episodes and write scores.json.
	uv run python rl_grading_generator.py

rl-grading-dry-run: # Phase 2b dry run: Show grading plan without LLM calls.
	uv run python rl_grading_generator.py --dry-run

# --- Evals ---

brown-create-eval-dataset: # Create the evaluation dataset for Brown.
	uv run python -m scripts.brown_create_eval_dataset \
		--input-dir inputs/evals/dataset \
		--name brown-course-lessons \
		--description "Evaluation dataset on course lessons format."

brown-run-eval: # Run the evaluation for Brown.
	uv run python -m scripts.brown_run_eval \
		--dataset-name brown-course-lessons \
		--metrics follows_gt \
		--cache-dir outputs/evals
		--workers 1 \
		# --read-from-cache


# --- Tests & QA ---

tests: # Run tests.
	CONFIG_FILE=configs/debug.yaml uv run pytest

pre-commit: # Run pre-commit hooks.
	uv run pre-commit run 

format-fix: # Auto-format Python code using ruff formatter.
	uv run ruff format $(QA_FOLDERS)

lint-fix: # Auto-fix linting issues using ruff linter.
	uv run ruff check --fix $(QA_FOLDERS)

format-check: # Check code formatting without making changes using ruff formatter.
	uv run ruff format --check $(QA_FOLDERS) 

lint-check: # Check code for linting issues without fixing them using ruff linter.
	uv run ruff check $(QA_FOLDERS)
