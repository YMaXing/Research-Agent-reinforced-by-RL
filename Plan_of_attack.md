# Plan of Attack

## Researcher Agent 
## Models

- switch to grok 4 families for similar performance but cheaper prices **done for the researcher, pending the writer**

## Tools

replace the fixed number of calling tools with a maximum limit

- expand searching scopes 

- Tavily replacing Perplexity as the chosen search-RAG tool for queries **done**

- LaTeX source scraping for full arXiv papers 

- (Optional) immediate fact-checking for quotes and claimed facts 

- (Optional) semantic deduplication 

- (Optional) cost reporting 

- (Optional) add PDF parsing to local file processing

## End-to-end Metrics for Content and Guideline Adherence

- completeness

- relevance

- accuracy

- novelty

- process reward, e.g. +1 for useful info gain per call, –1 for redundant calls, –2 for errors

- cost penalty

## Data

- length of section

1. AIRS-Bench

2. LFRQA

3. others

## RL Environment

### MCP client Layer

more advanced: mcp-agent, purpose-built for deep-research agents **baseline done**

### RL Training Layer

lightweight Gym-like env with

- Policy: fine-tuned LLM models using LORA
- State: research context + message history (summarized to avoid token explosion).
- Action: LLM-generated tool call JSON (or “research_complete” to terminate).
- Observation: tool result (fed straight back to LLM context).
- Episode: one full research session (max 10–20 steps or until “finalize”).
