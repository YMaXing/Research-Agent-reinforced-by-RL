# Nova Research MCP Server

FastMCP server that exposes research tools (Tavily search, Firecrawl scraping,
arXiv LaTeX, GitHub analysis, YouTube transcription, …) used by the rest of
the **Research-Agent-reinforced-by-RL** pipeline.

## Install

```bash
uv sync
```

## Run

```bash
# stdio transport (used by the local mcp_client and Cursor/Claude Desktop)
uv run mcp-server --transport stdio

# HTTP transport (used by the composed server in agents_integration_local/)
uv run python -m src.server --transport streamable-http --port 8001
```

## Configure

Copy `.env.example` → `.env` and set at least:

```bash
GOOGLE_API_KEY=...
TAVILY_API_KEY=...
FIRECRAWL_API_KEY=...
```

Optional: `FIRECRAWL_API_KEY_2` (round-robin), `GITHUB_TOKEN`,
`OPIK_API_KEY`.

## Tools, prompts, and resources

16 tools / 1 prompt / 2 resources, covering golden-source ingestion,
exploitation-phase research, the production RL preset decision
(`predict_exploration_preset_tool` — RL policy + deterministic guard, no LLM
call), the exploration phase, and final research-file assembly. Full list
and per-tool semantics: see
[../README.md](../README.md#available-tools-and-resources-16-tools-1-prompt-2-resources).

## Where this fits

- Workflow, env vars, and end-to-end usage: [../README.md](../README.md).
- Project-level context and pipeline diagram: [../../../README.md](../../../README.md).
- Composed HTTP deployment fronting this server + the writing server:
  [../../agents_integration_local/README.md](../../agents_integration_local/README.md).
