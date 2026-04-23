# Composed MCP Client

Client for the **composed MCP server** in
[`agents_integration_local/`](..). The composed server fronts the Nova
research agent and the Brown writing agent as a single HTTP endpoint, so a
single client session can drive a full *research → write* run.

> For most users the easiest entry point is the launcher
> [`composed_server_script.py`](../composed_server_script.py) one level up,
> which boots the research server (`:8001`), the writing server (`:8002`),
> the composed server (`:8003`), and this client.

## Install

```bash
uv sync
```

You'll also want `uv sync` in the sibling directories whose servers this
client talks to:

- [`../mcp_server/`](../mcp_server) — the composed server
- [`../../research_agent_local/mcp_server/`](../../research_agent_local/mcp_server) — research backend
- [`../../writing_workflow/`](../../writing_workflow) — writing backend

## Configure

Each backend reads its own `.env` (see their READMEs). The launcher loads:

- `agents_integration_local/.env` (optional shared overrides)
- `agents_integration_local/mcp_client/.env` (this folder)
- `research_agent_local/mcp_server/.env`
- `writing_workflow/.env`

Minimum keys required across the system:

```bash
GOOGLE_API_KEY=...
TAVILY_API_KEY=...
FIRECRAWL_API_KEY=...
# Optional: FIRECRAWL_API_KEY_2, GITHUB_TOKEN, OPIK_API_KEY, OPIK_WORKSPACE
```

## Run (recommended: via the launcher)

From `agents_integration_local/`:

```bash
uv run python composed_server_script.py
```

This starts:

| Service | Port | Source |
|---|---|---|
| Research MCP server | 8001 | [`research_agent_local/mcp_server/`](../../research_agent_local/mcp_server) |
| Writing MCP server  | 8002 | [`writing_workflow/`](../../writing_workflow) |
| Composed MCP server | 8003 | [`mcp_server/`](../mcp_server) (this folder's sibling) |
| Composed client     | —    | this client, configured via [`../mcp_composed_server_config_http.json`](../mcp_composed_server_config_http.json) |

Startup is gated on each upstream port becoming reachable
(`MCP_STARTUP_TIMEOUT_SECONDS`, default 300). Shutdown of the launcher
terminates all four processes cleanly.

## Run (manual, advanced)

If you want to run pieces by hand — e.g. point the client at an already-
running composed server:

```bash
uv run python -m src.client \
    --config ../mcp_composed_server_config_http.json
```

The two HTTP configs in the parent directory:

- [`../mcp_servers_config_http.json`](../mcp_servers_config_http.json) —
  used by the **composed server** to reach the two backends on
  `localhost:8001` and `localhost:8002`.
- [`../mcp_composed_server_config_http.json`](../mcp_composed_server_config_http.json) —
  used by **this client** to reach the composed server on `localhost:8003`.

## Where this fits

- Project pipeline overview and quickstart:
  [../../../README.md](../../../README.md).
- Research agent details: [`../../research_agent_local/README.md`](../../research_agent_local/README.md).
- Writing agent details: [`../../writing_workflow/README.md`](../../writing_workflow/README.md).
