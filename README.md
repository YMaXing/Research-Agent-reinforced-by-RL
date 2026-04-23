# Research-Agent-reinforced-by-RL

An end-to-end **Research → Writing** agentic system whose research-planning step
is fine-tuned with **offline GRPO**. A small Qwen3-4B + LoRA policy reads a
structured *exploitation digest* of an article topic and selects one of six
**exploration presets** that drives how the research agent explores the web
before the writing agent drafts the article.

The repository is a fork of the [Towards AI](https://academy.towardsai.net/courses/agent-engineering)
*Agentic AI Engineering* course materials, extended with:

- a full RL data-generation pipeline (research + writing + grading),
- offline GRPO + QLoRA training of an exploration-preset selector,
- a two-stage inference pipeline (RL policy + Grok 4.2 planner),
- a composed MCP server that fronts the research and writing agents over HTTP.

> Architecture, reward design, training math, and held-out test results are
> documented in [Plan_of_attack.md](Plan_of_attack.md) and [presentation.md](presentation.md).

---

## Contents

- [Pipeline at a glance](#pipeline-at-a-glance)
- [Repository layout](#repository-layout)
- [Prerequisites](#prerequisites)
- [Quickstart: use the agentic system](#quickstart-use-the-agentic-system)
- [Reproduce the held-out test results (L2, L6, L9)](#reproduce-the-held-out-test-results-l2-l6-l9)
- [Train your own GRPO policy](#train-your-own-grpo-policy)
- [Credits](#credits)

---

## Pipeline at a glance

```
┌────────────────────────┐    ┌───────────────────────────┐    ┌───────────────────────┐
│ article_guideline.md   │ →  │ Research MCP (Nova)       │ →  │ exploitation_digest   │
│ (topic, outline, style)│    │  • Tavily search          │    │ (gap profile + per-   │
└────────────────────────┘    │  • Firecrawl scraping     │    │  section coverage)    │
                              │  • arXiv LaTeX, GitHub    │    └──────────┬────────────┘
                              └───────────────────────────┘               │
                                                                          ▼
                              ┌───────────────────────────┐    ┌───────────────────────┐
                              │ Writing MCP (Brown)       │ ← │ RL preset selector    │
                              │  • LangGraph generate /   │    │  Qwen3-4B + LoRA      │
                              │    review / edit          │    │  + Grok 4.2 planner   │
                              │  • Mermaid media tools    │    │  → preset 0..5        │
                              └──────────┬────────────────┘    └───────────────────────┘
                                         │
                                         ▼
                                   article.md
```

The RL policy is trained **offline** on 24 pre-rolled episodes
(4 train articles × 6 presets). At inference time the policy emits a per-section
preset distribution; a Grok 4.2 reasoning call inside the same MCP tool is
allowed to override the policy when the article guideline gives a concrete
reason.

---

## Repository layout

```
Reinsearch_agent/
├── Plan_of_attack.md                  # Project plan, dataset, reward, training phases
├── presentation.md                    # GRPO math, results, ablations
├── README.md                          # ← you are here
└── RL_researcher_writer_ymaxing/      # All code lives here
    ├── README_PACKAGE.md              # Subpackage map
    ├── research_agent_local/          # Research MCP server + client + RL data gen + training
    │   ├── mcp_server/                # FastMCP research tools (Tavily, Firecrawl, arXiv, …)
    │   ├── mcp_client/                # Interactive REPL + batch runner
    │   ├── rl_data_generator.py       # Phase 1: produce research.md per (article × preset)
    │   ├── generate_digests.py        # Build exploitation_digest.md inputs for the RL policy
    │   └── training/                  # GRPO + QLoRA trainer, inference, eval scripts
    ├── writing_workflow/              # Brown writing agent + RL writing/grading generators
    ├── agents_integration_local/      # Composed MCP server (research + writing over HTTP)
    │   ├── composed_server_script.py  # Launcher: starts both backends + composed server + client
    │   ├── mcp_server/                # Composed server implementation
    │   └── mcp_client/                # Client that talks to the composed server
    ├── models/Qwen3-4B/               # Local base-model weights (downloaded separately)
    ├── rl_training_data/              # bases/, episodes/, checkpoints/  (offline RL artifacts)
    └── utils/                         # env loader + pretty-print helpers
```

---

## Prerequisites

- **Python 3.12** (subprojects pin `3.12.11` via `pyproject.toml`).
- **[uv](https://github.com/astral-sh/uv)** package manager — each subproject
  has its own `uv` environment; nothing is installed at the repo root.
- **GNU Make** (used by the writing workflow Makefile).
- A POSIX shell. On Windows, use **WSL**.
- For training and local inference: an **NVIDIA GPU** with bitsandbytes-NF4
  support (≥ 16 GB VRAM recommended for Qwen3-4B in 4-bit).
- API keys for the providers used by each agent (see the per-subproject
  READMEs):
  - `GOOGLE_API_KEY` — Gemini, used by the writing agent and graders
  - `TAVILY_API_KEY` — web search for the research agent
  - `FIRECRAWL_API_KEY` (and optionally a second one for round-robin) — scraping
  - `OPIK_API_KEY` — optional, observability
  - `XAI_API_KEY` — optional, Grok 4.2 planner stage at inference time

---

## Quickstart: use the agentic system

The fastest end-to-end path is the **composed MCP server**, which boots the
research and writing agents as HTTP services and exposes them through one
client.

```bash
# 1. Install dependencies for each subproject (one-time).
cd RL_researcher_writer_ymaxing/research_agent_local/mcp_server && uv sync && cd -
cd RL_researcher_writer_ymaxing/research_agent_local/mcp_client && uv sync && cd -
cd RL_researcher_writer_ymaxing/writing_workflow                   && uv sync && cd -
cd RL_researcher_writer_ymaxing/agents_integration_local/mcp_server && uv sync && cd -
cd RL_researcher_writer_ymaxing/agents_integration_local/mcp_client && uv sync && cd -

# 2. Configure API keys in each .env (copy from .env.example, then edit).
#    At minimum: GOOGLE_API_KEY, TAVILY_API_KEY, FIRECRAWL_API_KEY.

# 3. Launch the composed server + client.
cd RL_researcher_writer_ymaxing/agents_integration_local
uv run python composed_server_script.py
```

The launcher starts the research server on `:8001`, the writing server on
`:8002`, the composed server on `:8003`, and drops you into the client REPL.
From there you can drive a full *research → write* run end to end.

If you only want one half of the system, see:

- [research_agent_local/README.md](RL_researcher_writer_ymaxing/research_agent_local/README.md)
  — run the research agent standalone and produce a `research.md`.
- [writing_workflow/README.md](RL_researcher_writer_ymaxing/writing_workflow/README.md)
  — run the writing agent on an existing `research.md` + guideline.

---

## Reproduce the held-out test results (L2, L6, L9)

The `presentation.md` table (Section 7) reports test-set behaviour for the
**simple-average GRPO** policy on the three held-out articles
`02_workflows_vs_agents`, `06_tools`, `09_RAG`. You can reproduce those numbers
locally without any API calls — the exploitation digests and offline grading
scores are checked into `rl_training_data/`.

> The reproducible checkpoint is `task_20260422_114127/best`
> (Run 2 in `presentation.md`: $\beta = 0.05$, $\alpha = 0.15$,
> per-section simple-average weighting).

### 1. Install training-side dependencies

```bash
cd RL_researcher_writer_ymaxing/research_agent_local/training
uv sync
```

This pulls in `transformers`, `peft`, `bitsandbytes`, `torch` (CUDA), and
`tensorboard`.

### 2. Make sure the base model is present

`infer.py` looks first at `RL_researcher_writer_ymaxing/models/Qwen3-4B/` and
falls back to downloading `Qwen/Qwen3-4B` from the Hugging Face Hub. To use
local weights, place them under that directory (the `models/Qwen3-4B/` folder
already lists the expected files).

### 3. Run the meta-reasoner test on the held-out articles

From `RL_researcher_writer_ymaxing/research_agent_local/`:

```bash
# Default: tests {02_workflows_vs_agents, 06_tools, 09_RAG} with the
# checkpoint hard-coded in eval_accuracy.py / test_meta_reasoner.py.
uv run python training/test_meta_reasoner.py \
    --checkpoint ../rl_training_data/checkpoints/tasks/task_20260422_114127/best
```

For each article this:

1. Reads `rl_training_data/bases/<article>/exploitation_digest.md`.
2. Runs section-level inference with the LoRA policy, prints the structured
   RL signal JSON (per-section distributions, aggregated preset, confidence,
   entropy, floor flag) — exactly what the Grok planner would receive.
3. Computes the **oracle preset** from the offline reward data in
   `rl_training_data/episodes/<article>__preset*/scores.json`.
4. Tags each article as `EXACT`, `NEAR` (`|chosen − oracle| = 1`), or `MISS`.

Useful flags:

```bash
uv run python training/test_meta_reasoner.py --articles 09_RAG       # subset
uv run python training/test_meta_reasoner.py --save-json              # persist signals
```

### 4. Reproduce the section-level / article-level accuracy table

```bash
# From research_agent_local/
uv run python training/eval_accuracy.py \
    --checkpoint ../rl_training_data/checkpoints/tasks/task_20260422_114127/best
```

This reports top-1 section-level and article-level accuracy on both the train
split (`{03, 05, 08, 11}`) and the test split (`{02, 06, 09}`) using the same
reward formula encoded in [`Plan_of_attack.md`](Plan_of_attack.md).

### 5. (Optional) See what the policy says about a single digest

```bash
uv run python training/infer.py \
    --digest ../rl_training_data/bases/02_workflows_vs_agents/exploitation_digest.md \
    --verbose
```

---

## Train your own GRPO policy

To re-run training (4-article train set, simple-average per-section weighting):

```bash
cd RL_researcher_writer_ymaxing/research_agent_local/training
uv run python train_grpo.py --dry-run        # sanity-check setup
uv run python train_grpo.py                  # full training
uv run python train_grpo.py --epochs 200 --lr 5e-5 --beta 0.05
```

Outputs land under `RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/task_<timestamp>/`,
with `best/`, `epoch_*/`, `final/`, and a TensorBoard log under
`runs/run_<timestamp>/`. Point `eval_accuracy.py` and `test_meta_reasoner.py`
at the new `best/` directory with `--checkpoint`.

The full data-generation pipeline (Phase 1 research → Phase 2a writing →
Phase 2b grading) is documented in [Plan_of_attack.md](Plan_of_attack.md) and
in the per-subproject READMEs.

---

## Credits

Built on top of the [Agentic AI Engineering course](https://academy.towardsai.net/courses/agent-engineering)
by **Towards AI** and **Decoding AI**. The Nova research agent and Brown
writing agent originated in that course; the RL policy, training pipeline,
composed MCP server, and held-out evaluation are extensions in this fork.

Licensed under Apache-2.0 — see [LICENSE](RL_researcher_writer_ymaxing/LICENSE).
