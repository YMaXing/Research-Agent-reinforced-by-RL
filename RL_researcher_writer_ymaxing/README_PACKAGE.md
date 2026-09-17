# RL_researcher_writer_ymaxing — package map

This directory hosts all the code for the **Research-Agent-reinforced-by-RL**
project. It is structured as several independent `uv` projects (each with its
own `.venv` + `pyproject.toml`) that talk to each other over MCP, or — for the
offline RL half — via plain filesystem artifacts under `rl_training_data/`.

For project vision, the pipeline diagram, and the RL+guards results, see the
top-level [../README.md](../README.md).

## Subprojects

| Folder | Purpose | README |
|---|---|---|
| [research_agent_local/](research_agent_local) | Nova research agent: FastMCP server + client, production RL inference, the eval-only LLM-planner harness, and the full GRPO training/analysis toolchain (5 sub-projects, see below). | [research_agent_local/README.md](research_agent_local/README.md) |
| [writing_workflow/](writing_workflow) | Brown writing agent: LangGraph workflows for article generation/editing, MCP server, evals (FollowsGT / UserIntent), and the RL writing + grading generators under `rl_pipeline/` that produce Phase 2 training data. | [writing_workflow/README.md](writing_workflow/README.md) |
| [agents_integration_local/](agents_integration_local) | Composed MCP server that fronts the research and writing agents over HTTP, plus a launcher that boots both backends, the composed server, and the client. | [agents_integration_local/README.md](agents_integration_local/README.md) |

### `research_agent_local/`'s 5 sub-projects

Each is its own independent `uv` project:

| Folder | Purpose | README |
|---|---|---|
| [mcp_server/](research_agent_local/mcp_server) | FastMCP research tools (Tavily, Firecrawl, arXiv, GitHub, YouTube) + the production `predict_exploration_preset` tool. | [README](research_agent_local/mcp_server/README.md) |
| [mcp_client/](research_agent_local/mcp_client) | Interactive REPL + batch runner (also drives RL Phase-1 data generation). | [README](research_agent_local/mcp_client/README.md) |
| [rl_inference_service/](research_agent_local/rl_inference_service) | Production RL inference: `infer.py` (Qwen3-4B + LoRA HTTP server), `generate_digests.py`, and the production checkpoint (also on [HF](https://huggingface.co/xintelligence/qwen3-4b-research-planner-lora)). No LLM call. | [README](research_agent_local/rl_inference_service/README.md) |
| [evaluation/](research_agent_local/evaluation) | Eval-only harness: benchmarks RL / RL+guards against an LLM planner (`--planner-model`, Grok/Claude/etc.) on the held-out TRAIN/TEST split. | [README](research_agent_local/evaluation/README.md) |
| [training/](research_agent_local/training) | GRPO + QLoRA trainer (`pipeline/`), reusable data-repair scripts (`maintenance/`), and 40+ offline research/calibration scripts (`analysis/`). | [README](research_agent_local/training/README.md) |

## Other directories

| Folder | Purpose |
|---|---|
| `models/Qwen3-4B/` | Local copy of the Qwen3-4B base weights used by the GRPO trainer and `rl_inference_service`. Falls back to `Qwen/Qwen3-4B` on the Hugging Face Hub if missing. |
| `rl_training_data/` | Offline RL artifacts: `bases/`, `episodes/` + `test_episodes/`, `oracle_review/`, `pairwise/`, `rl_planner_test_results/` (results + the master `analysis_document.md` research log). `bases/`, `episodes/`/`test_episodes/`, and `checkpoints/` are gitignored — see [rl_training_data/README.md](rl_training_data/README.md) (large artifacts also mirrored on [HF Datasets](https://huggingface.co/datasets/xintelligence/research-agent-rl-episodes)). |
| `utils/` | Tiny shared helpers (`utils.env.load`, `utils.pretty_print.wrapped` / `function_call`). |

## Where to start

- **Just want to run the agents end to end?** See the top-level
  [../README.md](../README.md#quickstart-use-the-agentic-system).
- **Want to reproduce the held-out test results?** See
  [../README.md](../README.md#how-the-rlguards-policy-is-evaluated).
- **Want to dive into a single subsystem?** Open the corresponding README
  above.

## License

Apache-2.0 — see [LICENSE](LICENSE). Originates from the
[Towards AI Agentic AI Engineering course](https://academy.towardsai.net/courses/agent-engineering)
package; significantly extended in this fork.
