# Nova Research Agent (`research_agent_local`)

The research half of the **Research-Agent-reinforced-by-RL** pipeline.

This subproject contains:

- A FastMCP **research server** ([`mcp_server/`](mcp_server)) exposing 14
  research tools, 1 prompt, and 2 resources.
- An interactive **terminal client** ([`mcp_client/`](mcp_client)) plus a
  batch runner.
- The **RL data generator** ([`rl_data_generator.py`](rl_data_generator.py))
  that produces `research.md` for every `(article × preset)` episode used in
  GRPO training.
- The **digest builder** ([`generate_digests.py`](generate_digests.py)) that
  turns an exploitation run into the structured
  `exploitation_digest.md` consumed by the RL policy at inference time.
- The **GRPO + QLoRA trainer** and inference / eval scripts under
  [`training/`](training).

For project-level context, see the top-level
[../../README.md](../../README.md), [../../Plan_of_attack.md](../../Plan_of_attack.md),
and [../../presentation.md](../../presentation.md).

---

## Contents

- [Layout](#layout)
- [Prerequisites](#prerequisites)
- [Install](#install)
- [Configure environment variables](#configure-environment-variables)
- [Workflow overview](#workflow-overview)
- [Run the research agent interactively](#run-the-research-agent-interactively)
- [Generate RL training data (Phase 1)](#generate-rl-training-data-phase-1)
- [Build exploitation digests for the RL policy](#build-exploitation-digests-for-the-rl-policy)
- [Outputs under `.research/`](#outputs-under-research)
- [Training and evaluation](#training-and-evaluation)
- [Use the server from other MCP clients](#use-the-server-from-other-mcp-clients)

---

## Layout

```
research_agent_local/
├── mcp_server/                   # FastMCP server (tools, prompts, resources)
├── mcp_client/                   # Interactive REPL + batch runner
├── rl_data_generator.py          # Phase 1: research.md per (article × preset)
├── generate_digests.py           # Build exploitation_digest.md per article
├── repair_missing_tavily_queries.py  # One-shot maintenance for stale episodes
├── training/                     # GRPO + QLoRA trainer, inference, eval
│   ├── train_grpo.py
│   ├── infer.py
│   ├── eval_accuracy.py
│   ├── test_meta_reasoner.py
│   └── pyproject.toml
├── data/
│   └── metric_alignment_research_folder/  # L10 metric-calibration corpus
├── meta_reasoner_test_results/   # Persisted JSON signals from past test runs
└── Makefile
```

---

## Prerequisites

- **Python 3.12** (subprojects pin `3.12.11`).
- **[uv](https://github.com/astral-sh/uv)** package manager.
- POSIX shell (use **WSL** on Windows).
- For training and local LoRA inference: an NVIDIA GPU with 4-bit (NF4)
  bitsandbytes support, ≥ 16 GB VRAM recommended.

---

## Install

Each component is its own `uv` project. Install once per component you plan to
use:

```bash
# Research MCP server
cd mcp_server   && uv sync && cd -

# Interactive client / batch runner
cd mcp_client   && uv sync && cd -

# GRPO trainer + inference / eval
cd training     && uv sync && cd -
```

`uv sync` creates a `.venv` inside each folder and installs all dependencies
declared in that folder's `pyproject.toml`.

---

## Configure environment variables

Both server and client read configuration from real environment variables and
from a project-local `.env` (see `.env.example` in each folder). For a smooth
setup create a `.env` in **both** `mcp_server/` and `mcp_client/`.

Minimum required:

```bash
GOOGLE_API_KEY=your-google-api-key            # Gemini, used by tools and prompts
TAVILY_API_KEY=your-tavily-api-key            # Web search (replaces Perplexity)
FIRECRAWL_API_KEY=your-firecrawl-api-key      # Page scraping
# Optional second key for round-robin to dodge Firecrawl rate limits:
FIRECRAWL_API_KEY_2=your-second-firecrawl-key
```

Optional:

```bash
GITHUB_TOKEN=your-github-pat                  # GitHub repo analysis
OPIK_API_KEY=your-opik-key                    # Observability
OPIK_PROJECT_NAME=research-agent              # Defaults if unset
```

If something fails with "missing API key" errors, verify the variables are
visible in the shell where you run `uv`.

---

## Workflow overview

The research agent runs an **8-step workflow**, with parameters configurable
per call:

| Parameter | Default | Meaning |
|---|---|---|
| `maximum_exploration_rounds` | 3 | Max exploration iterations after exploitation |
| `n_exploration_queries_per_round` | 4 | Queries generated per exploration round |
| `maximum_sources_to_scrape` | 6 | Cap on sources fully scraped per round |
| `enable_content_dedup` | false | Optional semantic dedup of scraped content |

1. **Setup** — ask the user for the research directory, explain the workflow.
2. **Extract & process golden sources** (parallel) — extract URLs from
   `article_guideline.md`, process local files, scrape golden sources.
3. **Exploitation phase** (3 rounds by default) — generate queries, dedup,
   run Tavily searches, scrape top results.
4. **Exploration phase** (up to 3 rounds, schedule chosen by preset) —
   generate complementary queries (depth / breadth / balanced), dedup, run
   Tavily searches.
5–6. *Reserved for future phases.*
7. **Content deduplication** (optional) — semantic dedup while preserving
   phase hierarchy.
8. **Write final research** — emit `research.md` with an XML-tagged source
   structure.

The six **exploration presets** (P0–P5) used by the RL policy differ only in
how step 4 is scheduled. See [../../Plan_of_attack.md](../../Plan_of_attack.md#exploration-presets-bandit-arms).

---

## Run the research agent interactively

The recommended local mode is the **in-memory transport** — the client imports
the server inside the same process.

```bash
cd mcp_client
uv run python -m src.client
```

This will print the available tools / resources / prompts and drop you into:

```text
👤 You:
```

Typical first commands inside the REPL:

```text
/prompt/full_research_instructions_prompt
The research folder is /absolute/path/to/your/article. Run the complete workflow.
```

For a separate-process layout:

```bash
# Terminal A
cd mcp_server && uv run mcp-server --transport stdio

# Terminal B
cd mcp_client && uv run python -m src.client --transport stdio
```

---

## Generate RL training data (Phase 1)

[`rl_data_generator.py`](rl_data_generator.py) runs the full research workflow
across the cartesian product of `articles × presets` and produces a
`research.md` per episode. It is **idempotent** and resumable — sentinels like
`.research/_stepN.done`, `_exploit_round_N.done`, and `_explore_round_N.done`
let you safely re-run after a crash.

```bash
# From research_agent_local/
uv run --project mcp_server python rl_data_generator.py
```

Notable behaviour:

- **Pre-seeded content** for sources Firecrawl cannot scrape
  (`decodingml.substack.com`, `x.com`).
- **Dual Firecrawl keys** rotated round-robin to avoid rate limits.
- Outputs land under
  `../rl_training_data/episodes/<article>__preset<N>/.research/`.

If a previous run left `next_queries.md` files missing the original Tavily
queries, you can repair them with:

```bash
uv run python repair_missing_tavily_queries.py
```

---

## Build exploitation digests for the RL policy

The RL policy is conditioned on a structured **exploitation digest** —
gap profile + per-section coverage analysis — extracted from each article's
exploitation run. To (re)generate them:

```bash
uv run python generate_digests.py
```

Digests land at `../rl_training_data/bases/<article>/exploitation_digest.md`.

---

## Outputs under `.research/`

Each episode directory ends up with the following files (depending on the
preset and whether dedup is enabled):

| File | Contents |
|---|---|
| `research.md` | Final research deliverable, full workflow |
| `research_no_exploration.md` | Exploitation-only baseline (when produced via two-variant batch mode) |
| `deduplicated_research.md` | Optional dedup output |
| `tavily_results.md` | All Tavily search results across rounds |
| `next_queries.md` | Per-round generated queries |
| `full_queries.md` | Cumulative query history |
| `guidelines_filenames.json` | URLs extracted from the guideline, classified by type |
| `urls_from_guidelines/`, `urls_from_research/`, … | Scraped page contents |
| `_step*.done`, `_exploit_round_*.done`, `_explore_round_*.done` | Sentinels for resumability |

---

## Training and evaluation

The GRPO + QLoRA trainer, inference wrapper, and held-out test scripts live
in [`training/`](training):

```bash
cd training
uv sync

# Train (4-article train set, simple-average GRPO)
uv run python train_grpo.py --dry-run        # sanity check
uv run python train_grpo.py                  # full training

# Inference on a single digest
uv run python infer.py \
    --digest ../../rl_training_data/bases/02_workflows_vs_agents/exploitation_digest.md \
    --verbose

# Section + article accuracy on train and test splits
# (run from research_agent_local/)
cd ..
uv run python training/eval_accuracy.py \
    --checkpoint ../rl_training_data/checkpoints/tasks/task_20260422_114127/best

# Held-out meta-reasoner test (L2, L6, L9): produces the per-article RL signal
# JSON and the EXACT / NEAR / MISS verdict
uv run python training/test_meta_reasoner.py \
    --checkpoint ../rl_training_data/checkpoints/tasks/task_20260422_114127/best
```

Checkpoints are written to
`../rl_training_data/checkpoints/tasks/task_<timestamp>/{best,epoch_*,final}/`
with TensorBoard logs under `runs/run_<timestamp>/`. The reproducible
simple-average GRPO checkpoint referenced in `presentation.md` is
`task_20260422_114127/best`.

For the full GRPO loss, hyperparameter history, and reward formula, see
[../../presentation.md](../../presentation.md).

---

## Use the server from other MCP clients

The MCP server is standalone and can be wired into any MCP-aware client
(Cursor, Claude Desktop, Zed, …). Adjust the absolute path to
`research_agent_local/mcp_server` for your machine:

```json
{
  "mcpServers": {
    "nova-research": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/RL_researcher_writer_ymaxing/research_agent_local/mcp_server",
        "run", "mcp-server", "--transport", "stdio"
      ],
      "env": {
        "ENV_FILE_PATH": "/absolute/path/to/RL_researcher_writer_ymaxing/research_agent_local/mcp_server/.env"
      }
    }
  }
}
```

For HTTP transport, replace `stdio` with `streamable-http` and add `--port 8001`.

### Available tools and resources

- **Content discovery & processing**:
  `create_research_file_tool`, `extract_guidelines_urls_tool`,
  `process_github_urls_tool`, `process_local_files_tool`,
  `scrape_research_urls_tool`, `scrape_and_clean_other_urls_tool`,
  `transcribe_youtube_videos_tool`
- **AI-powered analysis**: `run_perplexity_research_tool`,
  `generate_next_queries_tool`
- **Content curation**: `select_research_sources_to_scrape_tool`,
  `select_research_sources_to_keep_tool`
- **Resources**: `get_available_tools_resource`,
  `get_memory_usage_resource`, `get_server_config_resource`,
  `get_system_status_resource`

For a more compact component-level summary see the per-folder READMEs:
[mcp_server/README.md](mcp_server/README.md),
[mcp_client/README.md](mcp_client/README.md).
