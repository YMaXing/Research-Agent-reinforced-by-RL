# Composed MCP Server

A **composition-only** MCP server: it mounts the Nova research server and
the Brown writing server as unprefixed proxies onto one `FastMCP` instance,
so a single client sees one merged tool/prompt namespace instead of two
separate servers. It defines no research or writing tools of its own — only
one extra prompt that chains the two backends together.

For the client that talks to this server, see
[`../mcp_client/README.md`](../mcp_client/README.md). For the recommended
way to run everything together, see
[`../README.md`](../README.md#quickstart-the-launcher).

## How composition works

`src/main.py::create_composed_server()`:

1. Loads `mcp_servers_config_http.json` (one directory up) — a plain
   `{"mcpServers": {name: {"url": ...}}}` map, the same shape FastMCP/MCP
   clients use everywhere else in this repo.
2. For each entry, creates a `fastmcp.Client` pointed at that URL, wraps it
   in a `FastMCP.as_proxy(...)`, and `mcp.mount(proxy)`s it **without a
   prefix** — so `predict_exploration_preset` (research) and
   `generate_article` (writing) both appear as top-level tools on the
   composed server, not `local-research-agent.predict_exploration_preset`.
3. Registers one additional prompt,
   `full_research_and_writing_workflow(dir_path)`, that instructs the
   calling LLM to run the research prompt first, then call the writing
   server's `generate_article` tool on the same directory — the only thing
   this package adds beyond pure proxying.

This means the composed server is only useful once its two upstreams are
already running and reachable at the URLs in
[`mcp_servers_config_http.json`](../mcp_servers_config_http.json) — it does
not start them itself (that's what
[`composed_server_script.py`](../composed_server_script.py) is for).

## Install

```bash
uv sync
```

## Run standalone

```bash
# stdio (default)
uv run python -m src.main

# HTTP, port 8003 (what the launcher actually uses)
uv run python -m src.main --transport streamable-http --port 8003

# Point at a different upstream config
uv run python -m src.main --config /path/to/alternate_servers_config.json
```

Requires the research server (`research_agent_local/mcp_server`) and writing
server (`writing_workflow`) to already be reachable at the URLs configured
in `mcp_servers_config_http.json` (defaults: `localhost:8001`/`:8002`).
Normally you don't run this by hand — see the launcher below.

## Where this fits

- [`composed_server_script.py`](../composed_server_script.py) boots both
  backends, this server, and the client together — the recommended entry
  point, documented in
  [`../README.md`](../README.md#quickstart-the-launcher).
- [`../mcp_client/README.md`](../mcp_client/README.md) — the client that
  talks to this server.
- [`../../research_agent_local/mcp_server/README.md`](../../research_agent_local/mcp_server/README.md) —
  the research backend this server proxies.
- [`../../writing_workflow/README.md`](../../writing_workflow/README.md) —
  the writing backend this server proxies.
