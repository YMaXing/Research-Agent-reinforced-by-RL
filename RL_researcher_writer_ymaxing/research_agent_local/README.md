# Nova Research Agent (`research_agent_local`)

The research half of the **Research-Agent-reinforced-by-RL** pipeline. Given
an `article_guideline.md` (plus any golden sources it names), it gathers
golden + exploitation-phase sources unconditionally, then an RL policy
decides how many *additional* exploration-phase rounds to run before the
final `research.md` is written. See the top-level
[../../README.md](../../README.md) for the full picture (source tiers,
pipeline diagram, results).

This subproject is split into **5 independent `uv` projects**:

| Sub-project | Role |
|---|---|
| [`mcp_server/`](mcp_server) | FastMCP server exposing 16 research tools, 1 prompt, and 2 resources — the actual research workflow. |
| [`mcp_client/`](mcp_client) | Interactive terminal REPL + batch runner (drives RL Phase-1 data generation). |
| [`rl_inference_service/`](rl_inference_service) | **Production** RL inference: `infer.py` (Qwen3-4B + LoRA), `generate_digests.py`, and the production checkpoint. No LLM call. |
| [`evaluation/`](evaluation) | **Eval-only** harness: benchmarks RL(+guards) against an LLM planner (any `--planner-model`) on the held-out TRAIN/TEST split. Not part of production. |
| [`training/`](training) | GRPO + QLoRA trainer, plus the offline reward-calibration / data-quality research toolchain. |

Also present: [`rl_data_generator.py`](rl_data_generator.py) (a thin root
shim for Phase-1 data generation) and [`test_planner.py`](test_planner.py)
(a thin root shim for the eval harness — see
[evaluation/README.md](evaluation/README.md)).

---

## Contents

- [Layout](#layout)
- [Prerequisites](#prerequisites)
- [Install](#install)
- [Configure environment variables](#configure-environment-variables)
- [Workflow overview](#workflow-overview)
- [Run the research agent interactively](#run-the-research-agent-interactively)
- [Generate RL training data (Phase 1)](#generate-rl-training-data-phase-1)
- [Production RL inference](#production-rl-inference)
- [Evaluate against baselines and LLM planners](#evaluate-against-baselines-and-llm-planners)
- [Train your own GRPO policy](#train-your-own-grpo-policy)
- [Outputs under `.research/`](#outputs-under-research)
- [Use the server from other MCP clients](#use-the-server-from-other-mcp-clients)

---

## Layout

```
research_agent_local/
├── mcp_server/                   # FastMCP server (tools, prompts, resources)
├── mcp_client/                   # Interactive REPL + batch runner
├── rl_inference_service/         # Production RL inference: infer.py, generate_digests.py,
│                                 #   checkpoints/production/ (the shipped LoRA adapter)
├── evaluation/                   # Eval-only harness: test_planner.py, --planner-model for any LLM
├── training/                     # GRPO + QLoRA trainer + offline analysis scripts
│   ├── pipeline/                 # train_grpo.py, generate_episode_oracles.py, compute_article_oracle.py, …
│   ├── maintenance/               # reusable data-repair scripts
│   ├── analysis/                  # 40+ reward-formula / noise / calibration research scripts (kept flat)
│   └── docs/                      # test_set_build_plan.md
├── rl_data_generator.py          # Root shim: Phase 1, produce research.md per (article × preset)
├── test_planner.py               # Root shim: delegates to evaluation/test_planner.py
└── Makefile
```

---

## Prerequisites

- **Python 3.12** (subprojects pin `3.12.11`).
- **[uv](https://github.com/astral-sh/uv)** package manager.
- POSIX shell (use **WSL** on Windows).
- For `rl_inference_service`/`training` (local LoRA inference + GRPO training):
  an NVIDIA GPU with 4-bit (NF4) bitsandbytes support, ≥ 16 GB VRAM recommended.

---

## Install

Each sub-project is its own `uv` project. Install only the ones you plan to use:

```bash
cd mcp_server            && uv sync && cd -   # research MCP server (always needed)
cd mcp_client             && uv sync && cd -   # interactive client / Phase-1 batch runner
cd rl_inference_service   && uv sync && cd -   # production RL inference (loads Qwen3-4B + LoRA)
cd training               && uv sync && cd -   # GRPO trainer + offline analysis scripts
```

`evaluation/` has no `pyproject.toml` of its own — it's driven via
`uv run --project mcp_server python evaluation/test_planner.py ...` (see
[evaluation/README.md](evaluation/README.md)).

`uv sync` creates a `.venv` inside each folder and installs all dependencies
declared in that folder's `pyproject.toml`.

---

## Configure environment variables

Server and client read configuration from real environment variables and
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
ANTHROPIC_API_KEY=your-anthropic-key          # Optional Layer-3 fallback in generate_digests.py
XAI_API_KEY=your-xai-key                      # Only used by evaluation/'s LLM-planner baseline
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
3. **Exploitation phase** (3 rounds, always runs) — generate queries, dedup,
   run Tavily searches, scrape top results. Step 3.4 runs the RL preset
   selector (`predict_exploration_preset`) right after this phase.
4. **Exploration phase** (0-3 rounds, schedule set by the chosen preset) —
   generate complementary queries (depth / breadth / balanced), dedup, run
   Tavily searches. Entirely skipped when the preset is `skip`.
5–6. *Reserved for future phases.*
7. **Content deduplication** (optional, SKIP by default and in development) — 
semantic dedup while preservin  phase hierarchy.
8. **Write final research** — emit `research.md` with an XML-tagged source
   structure (golden / exploitation / exploration).

The **4 exploration presets** (`skip`/`light`/`standard`/`deep`, P0–P3) used
by the RL policy differ only in how step 4 is scheduled — see the preset
table in [../../README.md](../../README.md#pipeline-at-a-glance).

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
  `../rl_training_data/episodes/<article>__preset<N>/.research/` (or
  `test_episodes/` for the held-out corpus).

If a previous run left `next_queries.md` files missing the original Tavily
queries, `training/maintenance/repair_missing_tavily_queries.py` can repair
them.

---

## Production RL inference

Production inference (RL policy + a deterministic policy guard, no LLM call)
lives in [`rl_inference_service/`](rl_inference_service) — this is what
`predict_exploration_preset` (the MCP tool step 3.4 calls) spawns as an HTTP
subprocess, and what builds each article's `research_digest.md`. See
[rl_inference_service/README.md](rl_inference_service/README.md).

---

## Evaluate against baselines and LLM planners

The eval-only harness under [`evaluation/`](evaluation) reproduces every
number in the top-level README's
[Results](../../README.md#results-rlguards-vs-baselines) section, and can
additionally benchmark the RL policy against an LLM planner (Grok, Claude, or
any other model via `--planner-model`). See
[evaluation/README.md](evaluation/README.md) for the full command reference.

Quick start (no API keys needed for the default RL-only/RL+guards modes):

```bash
cd mcp_server && uv sync && cd -
cd rl_inference_service && uv sync && cd -
uv run --project mcp_server python evaluation/test_planner.py --rl-guards-only --test-only
```

---

## Train your own GRPO policy

The GRPO + QLoRA trainer, reward-formula pipeline, and 40+ offline
research/calibration scripts live in [`training/`](training). See
[training/README.md](training/README.md) for the full breakdown of
`pipeline/` vs `maintenance/` vs `analysis/`.

```bash
cd training
uv run python pipeline/train_grpo.py --dry-run                  # sanity-check setup
uv run python pipeline/train_grpo.py --task-id my_run            # full training
```

Checkpoints land under
`../rl_training_data/checkpoints/tasks/<task-id>/{best,epoch_*,latest}/`.
Evaluate a new checkpoint via
`evaluation/test_planner.py --adapter-dir tasks/<task-id>/best --rl-guards-only --test-only`,
or copy it to `rl_inference_service/checkpoints/production/` to make it the
default for production inference.

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

### Available tools and resources (16 tools, 1 prompt, 2 resources)

- **Golden-source ingestion**: `extract_guidelines_urls_tool`,
  `process_local_files_tool`, `process_github_urls_tool`,
  `scrape_and_clean_other_urls_tool`, `transcribe_youtube_videos_tool`
- **Exploitation phase**: `scrape_exploitation_guideline_urls_tool`,
  `generate_next_queries_tool`, `deduplicate_new_queries_tool`,
  `run_tavily_research_tool`, `select_research_sources_to_scrape_tool`,
  `scrape_research_urls_tool`
- **RL preset decision**: `predict_exploration_preset_tool` (production;
  RL policy + deterministic guard only, no LLM — see
  [rl_inference_service/README.md](rl_inference_service/README.md))
- **Exploration phase**: `generate_next_complementary_queries_tool` (reuses
  several of the exploitation-phase tools above for dedup/search/scrape)
- **Final assembly**: `select_research_sources_to_keep_tool`,
  `deduplicate_research_content_tool`, `create_research_file_tool`
- **Resources**: `system://status`, `system://memory`

For a more compact component-level summary see the per-folder READMEs:
[mcp_server/README.md](mcp_server/README.md),
[mcp_client/README.md](mcp_client/README.md).
