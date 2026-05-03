# RL_researcher_writer_ymaxing — package map

This directory hosts all the code for the **Research-Agent-reinforced-by-RL**
project. It is structured as several independent `uv` projects that talk to
each other over MCP.

For project context, the three-phase pipeline, and credits, see the top-level
[../README.md](../README.md), [../Plan_of_attack.md](../Plan_of_attack.md), and
[../presentation.md](../presentation.md).

## Subprojects

| Folder | Purpose | README |
|---|---|---|
| [research_agent_local/](research_agent_local) | Nova research agent: FastMCP server, terminal client, RL data generator (`rl_data_generator.py`), digest builder (`generate_digests.py`), and the GRPO + QLoRA trainer under `training/`. | [research_agent_local/README.md](research_agent_local/README.md) |
| [writing_workflow/](writing_workflow) | Brown writing agent: LangGraph workflows for article generation / editing, MCP server, and the RL writing (`rl_writing_generator.py`) and grading (`rl_grading_generator.py`) generators that produce Phase 2 training data. | [writing_workflow/README.md](writing_workflow/README.md) |
| [agents_integration_local/](agents_integration_local) | Composed MCP server that fronts the research and writing agents over HTTP, plus a launcher that boots both backends, the composed server, and the client. | [agents_integration_local/mcp_client/README.md](agents_integration_local/mcp_client/README.md) |

## Other directories

| Folder | Purpose |
|---|---|
| `models/Qwen3-4B/` | Local copy of the Qwen3-4B base weights used by the GRPO trainer and the inference wrapper. Falls back to `Qwen/Qwen3-4B` on the Hugging Face Hub if missing. |
| `rl_training_data/` | Offline RL artifacts: `bases/<article>/research_digest.md`, `episodes/<article>__preset<N>/{research.md,article.md,scores.json}`, and `checkpoints/tasks/task_<timestamp>/{best,epoch_*,final}/`. |
| `utils/` | Tiny shared helpers (`utils.env.load`, `utils.pretty_print.wrapped` / `function_call`) consumed by the notebooks and CLI scripts. |
| `evak_offline_metrics.ipynb`, `eval_offline_dataset.ipynb` | Notebooks for inspecting the offline reward dataset and metric calibration. |

## Where to start

- **Just want to run the agents end to end?** See the top-level
  [../README.md](../README.md#quickstart-use-the-agentic-system).
- **Want to reproduce the held-out test results?** See
  [../README.md](../README.md#reproduce-the-held-out-test-results-l2-l6-l9).
- **Want to dive into a single subsystem?** Open the corresponding README
  above.

## License

Apache-2.0 — see [LICENSE](LICENSE). Originates from the
[Towards AI Agentic AI Engineering course](https://academy.towardsai.net/courses/agent-engineering)
package; significantly extended in this fork.
