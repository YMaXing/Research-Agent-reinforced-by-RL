# Plan of Attack

## Overview

Train **Qwen3-4B-Instruct-2507** with **GRPO** (Group Relative Policy Optimization, G=4)
to produce higher-quality AI research articles by reinforcing exploration strategy choices
during the research phase.

Training uses **QLoRA NF4 (r=8)** to keep the fine-tune memory-efficient.

---

## Dataset: Decoding AI Course Articles

| Split | Lessons | Notes |
|-------|---------|-------|
| **Train** | L2, L3, L5, L8, L11 | 5 articles x 6 presets = 30 episodes |
| **Test** | L6, L9 | Held out for generalization check |
| **Few-shot eval examples** | L4, L7 | Used as few-shot examples inside grading prompts |
| **Metric alignment** | L10 | Used for metric calibration only |

Word count targets (updated to match ground-truth article lengths):

| Lesson | Target Words |
|--------|-------------|
| L2 (02_workflows_vs_agents) | 3,900 |
| L3 (03_context_engineering) | 3,300 |
| L5 (05_workflow_patterns) | 5,500 |
| L6 (06_tools) | 3,700 |
| L8 (08_react_practice) | 3,000 |
| L9 (09_RAG) | 2,800 |
| L11 (11_multimodal) | 5,200 |

---

## Exploration Presets (Bandit Arms)

6 ExplorationPreset variants define the research strategy per episode:

| ID | Name | Rounds | Focus Sequence |
|----|------|--------|----------------|
| 0 | baseline | 0 | (pure exploitation only) |
| 1 | single_balanced | 1 | balanced |
| 2 | balanced_then_depth | 2 | balanced -> depth |
| 3 | depth_then_breadth | 2 | depth -> breadth |
| 4 | balanced_depth_breadth | 3 | balanced -> depth -> breadth |
| 5 | depth_breadth_depth | 3 | depth -> breadth -> depth |

Each episode directory is `rl_training_data/episodes/<article>__preset<N>/`.

---

## Three-Phase Pipeline

### Phase 1 - Research Generation (rl_data_generator.py) - RUNNING

**Script**: `research_agent_local/rl_data_generator.py`
**Runner**: `uv run --project mcp_server python rl_data_generator.py` (from `research_agent_local/`)

Generates `research.md` for each episode via the MCP research agent.

- Steps 1-3: exploitation (query gen + scraping + synthesis)
- Steps 4-7: exploration rounds per preset's focus_sequence, then final synthesis
- Pre-seeded content for sources Firecrawl cannot scrape (decodingml.substack.com, x.com)
- Dual Firecrawl API keys (round-robin) to avoid rate limits
- Sentinel-based resumability: `.research/_stepN.done`, `_exploit_round_N.done`, `_explore_round_N.done`
- Idempotent: skips completed sentinels; safe to re-run after crash

**Status**: 24/30 done (L2x6, L3x6, L5x6, L8x5 done -- L8p5 + L11x6 pending)

---

### Phase 2a - Article Generation (rl_writing_generator.py) - IMPLEMENTED

**Script**: `writing_workflow/rl_writing_generator.py`
**Runner**: `uv run python rl_writing_generator.py` (from `writing_workflow/`)
**Model**: Gemini 2.5 Pro

Generates `article.md` for each episode with `research.md`.

- Calls `build_generate_article_workflow(checkpointer)` -> `workflow.ainvoke({...})`
- 2 review iterations per article
- 3-layer resumability:
  1. `article.md` exists -> skip (zero cost)
  2. Per-episode SQLite checkpointer + deterministic thread_id for LangGraph task memoization
  3. Per-episode retry with exponential backoff (3 attempts, 30s base)
- CLI: `--articles`, `--presets`, `--dry-run`

---

### Phase 2b - Grading (rl_grading_generator.py) - NEXT

**Script**: `writing_workflow/rl_grading_generator.py`
**Runner**: `uv run python rl_grading_generator.py` (from `writing_workflow/`)
**Model**: Gemini 2.5 Flash (LLM-as-judge)

Grades each `article.md` on 9 dimensions and saves raw scores to `scores.json`.

**Option 4 -- Store all 9 scores, defer reward formula to Phase 3:**

```
scores.json
{
  "ground_truth_core_content":          0.0-1.0,   # FollowsGTMetric
  "ground_truth_flow":                  0.0-1.0,
  "ground_truth_structure":             0.0-1.0,
  "ground_truth_depth_enhancement":     0.0-1.0,
  "ground_truth_breadth_enhancement":   0.0-1.0,
  "ground_truth_core_preservation":     0.0-1.0,
  "user_intent_guideline_adherence":    0.0-1.0,   # UserIntentMetric
  "user_intent_research_anchoring":     0.0-1.0,
  "user_intent_golden_source_priority": 0.0-1.0
}
```

Inputs per episode:
- `output` = `episode_dir/article.md`
- `expected_output` = `inputs/evals/dataset/data/<lesson>/article_ground_truth.md`
- `input` (guideline) = `inputs/evals/dataset/data/<lesson>/article_guideline.md`
- `context["research"]` = `episode_dir/research.md`

Sentinel: `scores.json` existence -> skip.
CLI: `--articles`, `--presets`, `--dry-run`.

---

### Phase 3 - GRPO Training - NOT YET DESIGNED

**Algorithm**: GRPO (Group Relative Policy Optimization), G=4
**Model**: Qwen3-4B-Instruct-2507
**Fine-tuning**: QLoRA NF4, r=8

Reward formula to be decided in Phase 3 using the 9 stored dimension scores.
Candidate design: weighted combination of the 9 scores, with exploration-specific
bonuses for `depth_enhancement` and `breadth_enhancement` in non-baseline presets.

---

## Infrastructure

### MCP Research Agent

- **Server**: `research_agent_local/mcp_server/` (FastMCP)
- **Client**: `research_agent_local/mcp_client/` (LangGraph agent)
- Tools: Tavily search, Firecrawl scraping (dual-key), arXiv LaTeX, semantic dedup

### Writing Workflow

- **Package**: `writing_workflow/src/brown/`
- **Eval metrics** (LLM-as-judge, Gemini 2.5 Flash):
  - `FollowsGTMetric`: 6 dimensions (binary 0/1 per section -> avg 0.0-1.0)
  - `UserIntentMetric`: 3 dimensions (same approach)
- **Observability**: Opik for score tracking
