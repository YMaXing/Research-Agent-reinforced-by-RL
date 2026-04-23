# Nova Research MCP Client

Interactive terminal client and batch runner for the Nova research MCP
server. Used both for hands-on research sessions and for producing the
offline RL training episodes consumed by GRPO.

## Install

```bash
uv sync
```

## Run

### Interactive REPL (in-memory transport)

The simplest mode — the MCP server is imported and runs in the same
process as the client.

```bash
uv run python -m src.client
```

### Interactive REPL (stdio against a separate server)

```bash
# Terminal A — start the server
cd ../mcp_server && uv run mcp-server --transport stdio

# Terminal B — start the client
uv run python -m src.client --transport stdio
```

### Batch runner

The batch runner keeps the MCP server alive across multiple research samples
(no per-sample startup cost) and supports a **two-variant mode** that emits
both an exploitation-only `research_no_exploration.md` and a full
`research.md` per sample.

Other features:

- Fresh conversation history per sample (no context bleed)
- Interactive REPL for queueing multiple batches without restarting
- Non-interactive mode for CI / scripts, plus a dry-run mode

See `src/batch_runner.py` for CLI flags. Most RL Phase-1 runs go through
[`../rl_data_generator.py`](../rl_data_generator.py), which wraps the batch
runner with sentinel-based resumability.

## Configure

Copy `.env.example` → `.env` and mirror the keys from `mcp_server/.env`
(see [../mcp_server/README.md](../mcp_server/README.md)).

## Where this fits

- Workflow + RL data generation: [../README.md](../README.md).
- Project pipeline overview: [../../../README.md](../../../README.md).
