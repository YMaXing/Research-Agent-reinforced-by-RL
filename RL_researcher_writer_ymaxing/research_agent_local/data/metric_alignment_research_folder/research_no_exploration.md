# Comprehensive Research Report

## Section 1 - Introduction: Why Agents Need a Memory in the first place

LLMs of today have vast but frozen knowledge, fundamentally unable to learn by updating weights/parameters after training/deployment (continual learning problem). Inserting new knowledge via context window is limited by finite size, rising costs, "lost in the middle" problem, and noise.

An LLM without memory is like an intern with amnesia, unable to recall conversations or learn from experience.

Context window is "working memory" or "RAM" — volatile, fast, limited. Keeping full history is unrealistic due to size, costs, noise, lost-in-middle.

Context windows are increasing (8k/16k → 1M+), adapting stateful systems. In future with bigger windows/actual learning, less retrieval/compression needed (overhead, nuance loss).

Memory tools provide temporary solution for continuity, adaptability, "learning".

Early agent efforts for personal AI companions hit context limits (8k/16k tokens), forcing complex memory with compression/retrieval.

*Sources: cognitive-architectures-for-language-agents.md, memex-2-0-memory-the-missing-piece-for-real-intelligence.md, 7AmhgMAJIT4.md*

## Section 2 - The Layers of Memory: Internal, Short-Term, and Long-Term

Adopting biology/cognitive science terminology useful: provides framework for flexible behaviors.

**Internal Knowledge:** Static, pre-trained in LLM weights (best for facts; models know books with empty context). Ideal if model could update weights from experience.

**Short-Term Memory:** Active context window — volatile, fast, limited; only way to simulate "learning".

**Long-Term Memory:** External persistent storage; retrieved into short-term for action.

Dynamic: Retrieval pipeline queries memory types in parallel, ranks before context window.

```
graph TD
    A[Internal Knowledge<br/>LLM Weights] --> B[Short-Term Memory<br/>Context Window]
    C[Long-Term Memory<br/>External Store] --> B
    B --> D[LLM Reasoning/Action]
    E[Retrieval Pipeline] --> C
```

Categorizing: Internal for general intelligence; short-term for immediate tasks; long-term for context/personalization. No single layer suffices.

*Sources: cognitive-architectures-for-language-agents.md, memory-in-agent-systems-by-aurimas-grici-nas.md, memory-overview-docs-by-langchain.md*

## Section 3 - Long-Term Memory: Semantic, Episodic, and Procedural

**Semantic Memory (Facts & Knowledge):** Repository of facts/preferences/relationships (e.g., "User is vegetarian" or {"food restrictions": "User is a vegetarian"}). Structured by use-case (e.g., graph DB). Provides reliable source of truth: enterprise docs/catalogs; personal profiles/preferences/constraints.

**Episodic Memory (Experiences & History):** Diary of interactions with timestamps/context (e.g., "On Tuesday, user frustrated with brother Mark forgetting birthday... [created_at=2025-08-25T17:20:04.648191-07:00]"). Groups by timescale (day/conversation/week). Enables empathy, temporal queries ("What happened June 8th?").

**Procedural Memory (Skills & How-To):** Workflows/playbooks (e.g., MonthlyReportIntent: 1) Query sales DB 30 days; 2) Summarize; 3) Ask email/display). Baked into prompts/tools; improves efficiency/reliability.

*Sources: cognitive-architectures-for-language-agents.md, what-is-ai-agent-memory-ibm.md, memory-overview-docs-by-langchain.md*

## Section 4 - Storing Memories: Pros and Cons of Different Approaches

**Raw Strings:** Plain text indexed for vector search.

- Pros: Simple/fast; preserves nuance/tone.
- Cons: Imprecise retrieval (semantic but wrong context); hard updates (contradictions); no structure/time.

**Entities (JSON):** LLM-extracted structured (e.g., {"user": {"brother": {"job": "Software Engineer"}}}).

- Pros: Precise filtering/updates; ideal semantic/facts.
- Cons: Schema complexity/rigidity; nuance loss.

**Graph Database:** Nodes/entities, edges/relationships (e.g., User -[HAS_BROTHER]-> Mark -[WORKS_AS]-> Software Engineer).

```
graph LR
    U[User] -->|HAS_BROTHER| M[Mark]
    M -->|WORKS_AS| SE[Software Engineer]
    U -->|RECOMMENDED_ON_DATE:2025-10-25| R[Restaurant]
```

- Pros: Relationships/temporal; auditability.
- Cons: Complexity/cost; slower queries.

Choice by product needs: simplest viable, evolve.

*Sources: memex-2-0-memory-the-missing-piece-for-real-intelligence.md*

## Section 5 - Memory implementations with code examples

Mem0: Scalable memory-centric architecture extracting/consolidating/retrieving from conversations; graph variant for relations.

Uses raw strings here.

```
%load_ext autoreload
%autoreload 2
from utils import env; env.load(required_env_vars=["GOOGLE_API_KEY"])
import os, re
from typing import Optional
from google import genai
from mem0 import Memory

client = genai.Client()
MODEL_ID = "gemini-2.5-pro"

MEM0_CONFIG = {
    "embedder": {"provider": "gemini", "config": {"model": "gemini-embedding-001", "embedding_dims": 768, "api_key": os.getenv("GOOGLE_API_KEY")}},
    "vector_store": {"provider": "chroma", "config": {"collection_name": "lesson9_memories", "path": "/tmp/chroma_mem0"}},
    "llm": {"provider": "gemini", "config": {"model": MODEL_ID, "api_key": os.getenv("GOOGLE_API_KEY")}},
}
memory = Memory.from_config(MEM0_CONFIG)
MEM_USER_ID = "lesson9_notebook_student"; memory.delete_all(user_id=MEM_USER_ID)
```

**Helper functions:**

```python
def mem_add_text(text: str, category: str = "semantic", **meta) -> str:
    metadata = {"category": category}
    for k, v in meta.items(): metadata[k] = v if isinstance(v, (str, int, float, bool)) or v is None else str(v)
    memory.add(text, user_id=MEM_USER_ID, metadata=metadata, infer=False)
    return f"Saved {category} memory."

def mem_search(query: str, limit: int = 5, category: Optional[str] = None) -> list[dict]:
    res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}
    items = res.get("results", [])
    return [r for r in items if category is None or (r.get("metadata") or {}).get("category") == category]
```

**Semantic:** Extraction pipeline post-turn; prompt: "Extract persistent facts... 3–6 bullets max. Text: {My brother Mark is a software engineer...}"

Stores: "Mark is the user's brother. Mark is a software engineer..."

Retrieval: Hybrid (keyword filter "brother" → vector "job").

**Episodic:** Chronological log/summaries with timestamp.

Raw: "October 26th, 2025. 2:30PM EST: User: 'I'm feeling stressed...'"

Summarized: "October 26th... User stressed about deadline..."

Retrieval: Temporal filter + semantic rerank by recency.

**Procedural:** Developer-defined tools or learned.

Prompt: "Learn new skills... convert steps to procedure."

Stores: procedure_name: find_summer_cabin, steps=...

Retrieval: Intent-matching/function-calling.

```
facts = ["User prefers vegetarian meals.", "User has a dog named George.", "User is allergic to gluten.", "User's brother is named Mark and is a software engineer."]
for f in facts: print(mem_add_text(f, category="semantic"))

results = memory.search("brother job", user_id=MEM_USER_ID, limit=1); print(results["results"][0]["memory"])

dialogue = [{"role": "user", "content": "I'm stressed about my project deadline on Friday."}, ...]
episodic_prompt = f"Summarize... {dialogue}"; episode = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt).text.strip()
print(mem_add_text(episode, category="episodic", summarized=True, turns=4)); hits = mem_search("deadline stress", limit=1, category="episodic")

procedure_name = "monthly_report"; steps = ["Query sales DB...", "Summarize...", "Ask..."]; procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i+1}. {s}" for i,s in enumerate(steps))
mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name); results = mem_search("how to create a monthly report", category="procedure", limit=1)
```

*RAG covered Lesson 10.*

*Source: towardsai_agentic-ai-engineering-course.md*

## Section 6 - Real-World Lessons: Challenges and Best Practices

**Re-evaluating Compression:** 2023: 8k/16k windows forced ruthless compression (lossy). 2025: Gemini 1M+ cheap → less compression, raw history as truth (nuance/emotion). Use summaries/indexes; raw log ground truth.

**Design for Product:** No perfect architecture. Q&A: Simple RAG. Personal: Rich episodic. Tasks: Procedural. Avoid over-engineering.

**Human Factor:** Hide internals; agent manages autonomously (learn corrections, consolidate conflicts).

Early personal AI (Dot): Facts → schemas/entities → 4 systems (theory of mind, episodic, entities, procedural). Retrieval parallel. 2025: Less compression, real-time Q&A over raw.

```
graph LR
    Q[User Query] --> R[Entry Router]
    R --> P[Perceivers/Search]
    P --> E[Episodic]; P --> S[Semantic]; P --> EN[Entities]; P --> PR[Procedural]
    E --> G[Generate]; S --> G; EN --> G; PR --> G
```

Formation distinct: Theory of mind daily; episodic periodic; entities per-line + dream sequences.

*Sources: 7AmhgMAJIT4.md, memex-2-0-memory-the-missing-piece-for-real-intelligence.md*

## Section 7 - Conclusion

Memory core to personalized agents that "learn" over time; temporary for continual learning.

Next: Lesson 10 RAG; future: multimodal, MCP, production agents/monitoring/evals.

*Sources: mem0-building-production-ready-ai-agents-with-scalable-long-.md*

---

## Golden Source Reference

The sections below preserve the original source provenance via XML tags (`<golden_source>` for guideline-referenced material, `<research_source>` for Tavily / exploration results) so that downstream evaluation can assess golden-source priority.

# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What cognitive science principles from human memory research best explain the value of distinguishing between an AI agent's internal static knowledge, short-term working context, and external long-term storage?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://mem0.ai/blog/the-modal-model-of-memory-what-ai-agents-can-learn-from-cognitive-science

Query: What cognitive science principles from human memory research best explain the value of distinguishing between an AI agent's internal static knowledge, short-term working context, and external long-term storage?

Answer: The Atkinson-Shiffrin Modal Model (1968) describes three memory stores: sensory register (brief raw input), short-term store (limited capacity, 15-30s duration without rehearsal), and long-term store (unlimited capacity/duration). Control processes manage transfer between stores. For AI agents, distinguishing internal static knowledge (long-term store), short-term working context (short-term store), and external long-term storage mimics human memory, improving performance. Key principles: Attention as bottleneck (filter before model sees input to avoid 'lost in the middle'); Levels of Processing (deep semantic extraction over shallow verbatim storage for better retrieval); Interference management (update/delete to prevent proactive/retroactive interference); Dynamic forgetting (Bjork's New Theory of Disuse reduces noise); Layered consolidation (selection based on salience/relevance before promoting to long-term). Mem0 implements these: intelligent filtering, extraction, four-operation updates (ADD/UPDATE/DELETE/NOOP), dynamic forgetting, layered consolidation (conversation/session/user memory), yielding 26% higher accuracy, 91% lower latency, 90% fewer tokens vs. context-stuffing. Cognitive science predicts process-based systems outperform raw storage.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://plurality.network/blogs/ai-memory-vs-ai-context/

Query: What cognitive science principles from human memory research best explain the value of distinguishing between an AI agent's internal static knowledge, short-term working context, and external long-term storage?

Answer: Cognitive science categorizes AI agent memory into types mirroring human memory: Short-Term Memory (working memory, seconds-minutes, 5-9 chunks, maintains conversation coherence, limited by context window); Long-Term Memory (persistent, unlimited capacity via external storage, enables personalization across sessions); Episodic (recalls specific events); Semantic (factual knowledge); Procedural (skills/workflows). Distinguishing internal static knowledge (semantic/procedural LTM), short-term working context (STM), external long-term storage (episodic/semantic LTM) addresses limitations of context-only systems (session-bound, overflows, platform lock-in). Value: Persistence across sessions/devices, reduces re-explaining (saves 5+ hours/week), enables personalization (e.g., recalls tech stack/budget), avoids 'lost in the middle' in large contexts. Universal memory blends STM/LTM for cross-platform consistency.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2657600/

Query: What cognitive science principles from human memory research best explain the value of distinguishing between an AI agent's internal static knowledge, short-term working context, and external long-term storage?

Answer: Short-term memory (STM) differs from long-term memory (LTM) in duration (STM decays 15-30s without rehearsal) and capacity (STM ~3-4 chunks). Working memory (WM) includes STM plus attention/manipulation for tasks. Evidence: Decay (Peterson-Peterson task, articulatory suppression); Capacity (running span ~3-4 items, chunking via LTM). Framework: Activated LTM subset = STM; focus of attention = WM scope (~3-4 chunks). For AI: Distinguishing static knowledge (LTM), short-term context (STM), external storage (LTM) leverages human limits—prevents overload, enables filtering/selection/consolidation, supports attention control correlating with aptitude.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://www.simplypsychology.org/memory.html

Query: What cognitive science principles from human memory research best explain the value of distinguishing between an AI agent's internal static knowledge, short-term working context, and external long-term storage?

Answer: Multi-store model: STM (5-9 items, 0-30s, acoustic coding, sequential retrieval); LTM (unlimited capacity/duration, semantic coding, associative retrieval). Encoding: Visual/acoustic/semantic. Storage/retrieval differences justify distinction. Chunking expands STM via LTM organization (Miller's 7±2). For AI: Maps to short-term context (STM-limited), static knowledge/external storage (LTM-unlimited), improving efficiency by mimicking human constraints.

-----

</details>

<details>
<summary>What real-world examples illustrate how early personal AI companions failed with context-window-only approaches before implementing external memory systems for continuity?</summary>

Phase: [EXPLOITATION]

### Source [5]: https://matthopkins.com/technology/context-window-problem/

Query: What real-world examples illustrate how early personal AI companions failed with context-window-only approaches before implementing external memory systems for continuity?

Answer: The source describes failures in long AI conversations using only context windows, without external memory. Users treat single chat threads as project databases, memory systems, decision logs, and collaboration layers. It works initially but fails as tasks grow: the model loses earlier details due to truncation, dilution, or conflict in the bounded context window. Output remains fluent but lacks continuity, leading to repetition, drift, odd simplifications, or replies ignoring prior context. For real work like writing, coding, planning, research, analysis, multi-step problem solving, the context window becomes a wall. Success creates heavier threads with branches, corrections, notes, turning into a sedimentary record too heavy for working memory. People push the same chat or dump everything into prompts, but fluency isn't continuity. The model operates from lossy reconstruction. Paper 'Lost in the Middle' shows performance degrades with info in middle of long contexts. Early conversations feel magical with high signal-to-noise, but degrade gradually. Solution: separate memory from working context using external files for stable info, summaries, new chats, deliberate context loading—not infinite chat threads.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://arxiv.org/html/2409.11192v1

Query: What real-world examples illustrate how early personal AI companions failed with context-window-only approaches before implementing external memory systems for continuity?

Answer: Early neural models struggled maintaining long-term context, adapting user preferences over extended interactions using only short-term memory. Traditional symbolic AI used static knowledge bases lacking dynamic adaptability. LLMs' attention mechanisms limited by high costs, uneven retention, biases; lack depth/contextual recall of human LTM crucial for personalized recommendations/adaptive learning. Personal AI companions/assistants need LTM to learn from interactions, adapt preferences for personalization. Without, early systems couldn't provide continuity. Approaches to fix: external knowledge bases (RAG), additional memory layers (MANNs, NTMs, DNCs), integrated memory (MemoryBank). Examples like Replika (not yet LTM-equipped) evolve to mirror personality but limited without full LTM. Charlie Mnemonic first with LTM using GPT-4 for human-like memory processes.

-----

</details>

<details>
<summary>How does the continual learning problem in LLMs manifest in production agents, and what external memory workarounds best enable personalization without weight updates?</summary>

Phase: [EXPLOITATION]

### Source [9]: https://jessylin.com/2025/10/20/continual-learning/

Query: How does the continual learning problem in LLMs manifest in production agents, and what external memory workarounds best enable personalization without weight updates?

Answer: The continual learning problem in LLMs manifests as catastrophic forgetting and poor integration when updating parameters for new information, breaking existing capabilities. In production agents, full finetuning causes 89% drop on Natural Questions and LoRA 71% when learning TriviaQA facts, while held-out benchmarks like GSM8K degrade significantly. This occurs because updating all or many parameters overwrites prior knowledge without targeted, high-capacity, adaptive integration.

External memory workarounds without weight updates include in-context learning (ICL) and RAG. ICL adapts via context but suffers from context rot, confusion with filled contexts, and limited by context length. RAG retrieves from growing buffers for high capacity and targeted access but lacks knowledge compression, failing to distill reasoning/coding skills—retrieving verbatim sessions doesn't improve model coding ability. Both are non-parametric, default solutions today, enabling personalization via user feedback/experiences in context without parametric changes, but don't compress knowledge like weights. Memory layers are proposed as parametric but sparse alternative, though the post focuses on non-parametric for no weight updates.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://www.letta.com/blog/continual-learning

Query: How does the continual learning problem in LLMs manifest in production agents, and what external memory workarounds best enable personalization without weight updates?

Answer: Continual learning problem in production LLM agents manifests as inability to update weights post-deployment due to catastrophic forgetting, deployment issues (per-user vs. shared models, data leakage), and lack of scalable fine-tuning. Agents remain static despite interactions, relying on stateless paradigms without carrying knowledge forward, leading to repeated cold starts and no improvement from experience over time horizons spanning model releases.

External memory workarounds best enabling personalization without weight updates are token-space learning: updating context C (system prompts, conversation history, retrieved documents) instead of weights θ. In-context learning appends experiences but limits include context overflow, re-processing raw logs, lossy summarization. Solutions: sleep-time compute for memory refinement (consolidate during downtime), teaching agents memory self-awareness, MemGPT for long-horizon context management. Agent memory via persistent storage (e.g., git-backed) allows learning from lived experience, personalization across models. RAG connects to external data but insufficient alone; memory blocks structure context for consistent recall, enabling personalization via refined, non-append-only memories.

-----

-----

Phase: [EXPLOITATION]

### Source [11]: https://www.lesswrong.com/posts/aKncW36ZdEnzxLo8A/llm-agi-will-have-memory-and-memory-changes-alignment

Query: How does the continual learning problem in LLMs manifest in production agents, and what external memory workarounds best enable personalization without weight updates?

Answer: Continual learning problem manifests in production agents as lack of persistent memory beyond sessions, limiting employability for knowledge work, long-horizon tasks, and personalization. Stateless LLMs can't learn subtleties, edge cases, or user preferences on-the-job like humans, requiring repeated instructions/prompting, frustrating for novel tasks. No current agents have long-term self-directed memory, blocking economic advantages like drop-in remote workers.

External memory workarounds without weight updates: context management (limited prompting/history), RAG (retrieve experiences/documents on-demand), editable contextual memory files (e.g., OpenAI's since 4o for episodic memory, enabling user-specific adaptation, seeming more 'human' via personalization). These boost capabilities for preferences/interactions but are human-directed now; agent incompetence blocks self-use. Memory enables personalization (e.g., understanding user better over time) without full weight updates, though fine-tuning mentioned as future efficiency gain.

-----

-----

Phase: [EXPLOITATION]

### Source [12]: https://towardsdatascience.com/how-to-maximize-agentic-memory-for-continual-learning/

Query: How does the continual learning problem in LLMs manifest in production agents, and what external memory workarounds best enable personalization without weight updates?

Answer: Continual learning problem in production agents manifests as cold starts each interaction: repeating instructions (e.g., Python version, code formatting), agent re-figuring known info (e.g., table names), wasting time/tokens, reducing effectiveness. Agents forget preferences/behaviors between sessions, mimicking severe impairment.

External memory workaround: agents.md file as persistent agentic memory, read every new task. LLM generalizes/stores useful knowledge (preferences, project details, mistakes) from interactions into this file via prompts like 'Generalize... Store in agents.md'. Enables personalization without weight updates—agent learns user patterns (e.g., no Any type, specific syntax), avoids repetition, reduces costs via fewer inference tokens. Works across coding agents (Claude Code # for memory), scales to thousands of words. Heavy utilization maximizes continual learning, making interactions faster/effective.

-----

</details>

<details>
<summary>What LLM-based extraction techniques and prompt patterns work best for transforming raw conversations into atomic semantic facts or timestamped episodic summaries while minimizing information loss?</summary>

Phase: [EXPLOITATION]

### Source [14]: https://langchain-ai.github.io/langmem/concepts/conceptual_guide/

Query: What LLM-based extraction techniques and prompt patterns work best for transforming raw conversations into atomic semantic facts or timestamped episodic summaries while minimizing information loss?

Answer: LangMem provides LLM-based extraction techniques for transforming raw conversations into atomic semantic facts (semantic memory) and timestamped episodic summaries (episodic memory) while minimizing information loss through ground-truth-preserving methods. Key techniques include:

**Subconscious Formation**: Prompting an LLM to reflect on conversations post-interaction to extract patterns and insights without impacting real-time performance. Perfect for high recall of extracted information.

**Core API with create_memory_manager**: Prompts LLMs to extract noteworthy facts, events, relationships, and indicate importance. Example instructions: "Extract all noteworthy facts, events, and relationships. Indicate their importance."

**Semantic Memory (Atomic Facts)**:
- **Collections**: Individual documents/records for unbounded knowledge. Balances creation/consolidation via memory enrichment. Example extracts: [IMPORTANT] User prefers casual communication; [BACKGROUND] User proficient in Python.
- **Profiles**: Single schema-constrained document for current state (e.g., UserProfile with name, preferences). Updates existing document. Example: UserProfile with preferred_name="Lex", skills=["Python", "AI"].

**Episodic Memory (Timestamped Summaries)**:
- Episode schema with observation, thoughts, action, result. Instructions: "Extract examples of successful interactions. Include context, thought process, and why it worked."
- Captures full interaction context for learning from experience.

**Conscious vs. Subconscious Formation**: Active (during conversation) vs. background (post-conversation) to balance latency and thoroughness.

These techniques use Pydantic schemas for structured output, enable_inserts for persistence, and process conversations as lists of messages. Minimizes loss by reconciling new info with existing memories, using importance/strength in recall.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://arxiv.org/html/2506.07446v1

Query: What LLM-based extraction techniques and prompt patterns work best for transforming raw conversations into atomic semantic facts or timestamped episodic summaries while minimizing information loss?

Answer: AFEV (Atomic Fact Extraction and Verification) framework uses iterative LLM-based extraction to decompose complex claims into atomic facts, minimizing information loss through dynamic refinement and verification feedback loops.

**Dynamic Atomic Fact Extraction**: Iteratively decomposes claims into atomic facts Ft using LLM Extractor conditioned on original claim C, previous facts F1:t-1, labels y1:t-1, and rationales r1:t-1. Prompt includes task-specific instructions. Stops when facts cover the claim. Reduces error propagation from static decomposition.

**Formalization**: Ft = Extractor(C, F1:t-1, y1:t-1, r1:t-1). Each iteration refines based on prior verification.

**Refined Evidence Retrieval**: For each Ft, retrieves/reranks evidence Et using bi-encoder + cross-encoder reranker trained with InfoNCE loss on LLM-judged positives/negatives. Dynamic demonstrations At via semantic similarity.

**Adaptive Atomic Fact Verification**: Reasoner(Ft, C, Et, At) generates label yt and rationale rt. Includes original claim C for granularity alignment. Aggregates to final y*.

Prompt examples (Fig. 3-4): Iterative extraction prompts condition on prior facts/verifications; verification uses dynamic demos + reranked evidence.

Minimizes loss via iterative feedback (verification informs next extraction), noise filtering (reranking), and context-specific demos. SOTA on HOVER (78.87 LA), PolitiHop (74.14 LA), RAWFC (60.2 F1), LIAR (43.9 F1).

-----

-----

Phase: [EXPLOITATION]

### Source [16]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory/blob/main/README.md

Query: What LLM-based extraction techniques and prompt patterns work best for transforming raw conversations into atomic semantic facts or timestamped episodic summaries while minimizing information loss?

Answer: LangMem uses LLM prompting via create_memory_manager to extract atomic semantic facts (semantic memory: facts/knowledge) and timestamped episodic summaries (episodic memory: past experiences) from conversations, minimizing loss through structured schemas and subconscious formation.

**Prompt Patterns**:
- Semantic: "Extract all noteworthy facts, events, and relationships. Indicate their importance." → Collections (unbounded docs) or Profiles (schema-constrained, e.g., UserProfile).
- Episodic: "Extract examples of successful interactions. Include the context, thought process, and why the approach worked." → Episode schema (observation, thoughts, action, result).

**Techniques**:
- **Subconscious Formation**: Post-conversation LLM reflection for patterns/insights, ensuring high recall without real-time latency.
- **Conscious Formation**: In-conversation updates for critical context.
- Process: Input conversation → LLM determines memory expansion/consolidation → Output updated state.

Examples minimize loss by balancing extraction/consolidation, using importance/strength/recency in recall, and schema enforcement (Pydantic BaseModel). Profiles update single doc; collections reconcile new info with existing beliefs.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://arxiv.org/html/2604.04853v1

Query: What LLM-based extraction techniques and prompt patterns work best for transforming raw conversations into atomic semantic facts or timestamped episodic summaries while minimizing information loss?

Answer: MemMachine stores raw episodes/sentences for ground-truth preservation, minimizing LLM extraction loss. **Techniques**: Sentence-level indexing, contextualized retrieval (nucleus + neighbors), profile extraction.

**Prompts**: Search prompts (Edwin variants) tuned via APO; agent routing classifies queries for ChainOfQuery/SplitQuery.

Episodic (timestamped facts/events), semantic (profiles). Ablations show retrieval optimizations > ingestion.

-----

</details>

<details>
<summary>How can AI engineers align memory architecture choices like compression levels or storage complexity directly to specific product requirements rather than adopting comprehensive systems by default?</summary>

Phase: [EXPLOITATION]

### Source [20]: https://atlan.com/know/how-to-choose-ai-agent-memory-architecture/

Query: How can AI engineers align memory architecture choices like compression levels or storage complexity directly to specific product requirements rather than adopting comprehensive systems by default?

Answer: AI engineers align memory architecture choices to specific product requirements using a 7-dimension framework and 5-step evaluation process, avoiding default comprehensive systems. Dimensions include: Scale (agent count, platforms, teams), Governance (compliance needs), Data estate complexity (single vs. multi-platform), Agent use case (conversational vs. analytical), Team ownership, Freshness, Multi-agent coordination. Routing matrix maps scenarios: Memory layers (e.g., Mem0, Zep) for conversational/single-platform; Context layers for enterprise/regulated/multi-platform. Evaluation scorecard weights criteria like cross-platform coverage (20%), governance (20%), accuracy improvement (15%). Steps: 1. Map data estate/agent inventory (1-2 weeks). 2. Score against routing matrix. 3. Research shortlist. 4. Vendor demos with own data. 5. POC on production data (2-4 weeks), measuring accuracy, latency, freshness, traceability. For regulated/low-risk: memory layer; multi-platform/analytical: context layer. Adjust weights for priorities (e.g., governance 25-30% for regulated). Questions for vendors: context freshness propagation, accuracy improvement, entity resolution. Red flags: conflating session memory with governed context, roadmap governance. Green flags: accuracy docs, audit trails, MCP support. Atlan's context layer connects semantic definitions, lineage, policies for enterprise AI, scaling to 100M+ assets.

-----

</details>

<details>
<summary>What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?</summary>

Phase: [EXPLOITATION]

### Source [51]: https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/

Query: What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?

Answer: The article describes the evolution from simple AI systems relying on limited context windows to modern agents using multi-layered external memory systems including episodic, semantic, and procedural memory. Early systems used short-term working memory within the context window with FIFO queues, but limitations like token limits and context degradation led to the adoption of external long-term memory frameworks. Systems like MemGPT introduced memory hierarchies shifting less important information to external storage. The decision to adopt external memory depends on operational scale: stateless single-session tasks don't need it, but repeated tasks with persistent entities require dedicated infrastructure to avoid exorbitant token costs from continuous context re-injection. During active interactions, agents use the context window with read-access to long-term memory; post-session, background processes compress episodic history into semantic memory using efficient models. Frameworks like Mem0, Zep, and LangMem are compared, with Mem0 focusing on compression for token reduction, Zep on temporal knowledge graphs, and LangMem on procedural learning. Simple LangChain buffer memory suits early MVPs, but production needs advanced external systems to handle noise, inefficiency, and performance issues beyond append-only storage.

-----

-----

Phase: [EXPLOITATION]

### Source [52]: https://community.cisco.com/t5/devnet-general-blogs/agent-memory-systems-beyond-context-windows/ba-p/5352003

Query: What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?

Answer: Shereen Bellamy, Senior Developer Advocate at Cisco, shares a developer experience building persistent memory for AI agents in network troubleshooting. Early reliance on context windows (e.g., 128K tokens) hit limits after analyzing 85 configs, causing high token costs ($5 for repeated 50K token injections in a session) and forgetting between API calls. Transitioned to persistent memory using three SQLite databases: VectorDB for semantic search (e.g., 'interface problems'), episodic for time-ordered events like syslog, and network for device specifics. The 'remember' function writes to all three for redundancy. Benchmark: persistent memory achieved 100% accuracy on 100 devices in 2s vs. 40% for context windows in 0.8s, handling 5x more devices. Implemented self-registering agents that learn capabilities (e.g., from device monitoring to incident troubleshooting) stored persistently. GitHub repo with agencymemoryimplementation.py demonstrates full SDK with Corto/Longo protocols for memory coordination and self-registration. Conclusion: structure beats raw power; use databases for persistence instead of temporary context memory.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://dev.to/sreeni5018/the-5-types-of-ai-agent-memory-every-developer-needs-to-know-part-1-52fn

Query: What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?

Answer: The author explains the progression from simple request-response systems with no retention, to stuffing conversation history into context windows (which leaked older messages), to agent systems needing memory for multi-step tasks and multi-agent coordination. Context windows are finite, costly, and reset between sessions, making 'dump everything' insufficient for complexity. Developers must build memory infrastructure around stateless LLMs: Short-Term Memory (STM) as session buffer; Long-Term Memory (LTM) in vector DBs like Pinecone for cross-session persistence; Working Memory for multi-step reasoning; Episodic for past events; Semantic via RAG for facts. All five types work together, with tools like LangChain for buffers/LTM, LlamaIndex for RAG, Pinecone for vectors, LangGraph for orchestration. The shift addresses agent failures like losing state mid-task in multi-agent systems.

-----

-----

Phase: [EXPLOITATION]

### Source [54]: https://www.cybage.com/blog/context-and-memory-engineering-building-intelligent-ai-agents-that-learn-and-adapt

Query: What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?

Answer: Describes evolution from prompt-based stateless systems to context/memory-driven agents. Example: Marketing copilot for B2B SaaS; stateless AI forgets Q1 campaign details (budget $60K, channels) by Q2, requiring massive prompts that fail at scale. Solution: Context Engineering dynamically curates workspace (goals, profiles, decisions); Memory Engineering with Semantic (facts), Episodic (events like Q1 outcomes), Procedural (behaviors). Uses vector DBs, graphs; LangGraph for orchestration, LangMem for persistent memory. Production architecture: hybrid storage, retrieval into context. Cybage implements for enterprises (healthcare patient history, finance client goals), achieving reductions in time/errors via memory persistence beyond context windows.

-----

-----

Phase: [EXPLOITATION]

### Source [55]: https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/

Query: What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?

Answer: Details 2024 shift from crude text-file serialization re-fed into prompts, to sophisticated external DBs for long-term memory. Early context window expansion caused 'context rot' and pollution, degrading performance. Now: extraction (salience detection), consolidation (recursive re-encoding), retrieval (recency/importance weighting). Enterprises gain: sales copilots halving research time, call centers reducing handle time. Examples: Mem0 (atomic statements), Zep (entities/relationships), Letta (time-indexing). Parallels human memory layers; warns of ethics (privacy, bias).

-----

-----

Phase: [EXPLOITATION]

### Source [56]: https://galileo.ai/blog/context-engineering-for-agents

Query: What personal developer experiences or case studies demonstrate the transition from relying solely on expanding context windows to implementing sophisticated external memory systems in early AI agent projects?

Answer: Manus team (millions of interactions) found agents process 100 input tokens per output; context engineering > model choice. Evolution: 2022 prompt engineering to 2024 context engineering for 50-tool tasks. Context (RAM-like, volatile) vs Memory (persistent storage). Manus: filesystem as infinite memory, 100:1 compression via summaries/URLs. Windsurf: multi-retrieval (embeddings, grep, graphs). Anthropic: multi-agent isolation for parallel research (90% perf gain). Anti-patterns: modifying context breaks cache. Benchmarks show tool overload degrades perf; context rot drops GPT-4o 98%->64%. Framework: offloading, isolation, retrieval, pruning, caching.

-----

</details>

<details>
<summary>How can insights from human hippocampal replay and systems consolidation inform the design of memory updating, pruning, and conflict resolution mechanisms in long-term agent memory?</summary>

Phase: [EXPLOITATION]

### Source [57]: https://royalsocietypublishing.org/rstb/article/379/1913/20230416/109678/Elements-of-episodic-memory-insights-from

Query: How can insights from human hippocampal replay and systems consolidation inform the design of memory updating, pruning, and conflict resolution mechanisms in long-term agent memory?

Answer: AI systems use hippocampus-inspired replay buffers for memory consolidation, where experience replay algorithms train on subsets of past episodes to encourage consolidation and learning, addressing catastrophic forgetting via complementary learning systems theory. Replay prioritizes novel, recent, or salient episodes (e.g., prioritized experience replay samples surprising episodes with high/low rewards, akin to high affective valence in humans). This informs agent memory updating by using replay to gradually consolidate rapidly learned hippocampal-like information into neocortical long-term memory. Pruning can prioritize weakly learned or less salient information for removal, as replay favors high-value episodes. Conflict resolution favors recent memories through prioritized sampling and mechanisms like hindsight experience replay (HER), which replays episodes with alternative goals. Various replay variants (e.g., PER, HER, reverse replay) enhance learning from sparse rewards and overcome forgetting, suggesting agent designs with prioritized, goal-relabeled, or reverse replay for updating, pruning low-priority data, and resolving conflicts by recency or utility.

-----

-----

Phase: [EXPLOITATION]

### Source [58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5847173/

Query: How can insights from human hippocampal replay and systems consolidation inform the design of memory updating, pruning, and conflict resolution mechanisms in long-term agent memory?

Answer: Hippocampal replay during sharp wave ripples (SWRs) reactivates past trajectories offline (sleep/rest) and online (pauses), supporting systems consolidation by transferring hippocampal traces to neocortex and stabilizing memories. Replay prioritizes novel, recent, salient experiences (e.g., rewarded trajectories), informing agent memory updating via prioritized replay buffers that sample high-utility episodes for consolidation, preventing catastrophic forgetting. Pruning emerges from preferential replay of high-value content, allowing weakly encoded traces to fade. Conflict resolution uses forward/reverse replay dynamically: reverse replay links experiences to outcomes (learning), forward simulates/plans futures (decision-making). Online replay switches by task demands (local for decisions, remote for consolidation), suggesting agents toggle replay modes. SWR disruption impairs learning, so agents should protect replay states. Coordinated cortical-hippocampal replay during SWRs drives plasticity, informing multi-module agent designs where hippocampal-like replay trains cortical-like long-term stores.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://cenl.ucsd.edu/Jclub/Carr(2011)_NarureReview_Hippo_Consolidation.pdf

Query: How can insights from human hippocampal replay and systems consolidation inform the design of memory updating, pruning, and conflict resolution mechanisms in long-term agent memory?

Answer: Awake hippocampal replay during SWRs reactivates behavioral sequences forward/reverse, supporting consolidation (repeated offline reactivation without behavior) and retrieval (cued by current input). Replay meets consolidation criteria: repeats traces plastically, persists post-experience, propagates to neocortex. For agents, use replay buffers for updating via repeated sequence training, pruning low-replay items. Remote replay (distant environments) enables cross-context associations. Salient/novel experiences enhance replay, so prioritize high-utility episodes. Sensory cues bias replay content, informing cued retrieval. Forward/reverse replay links to outcomes/planning, resolving conflicts via recency (reverse post-reward) or simulation (forward pre-action). Design agents with SWR-like events for consolidation/retrieval, using local/remote modes for updating/pruning.

-----

</details>

<details>
<summary>What infrastructure-level trade-offs exist between using pure vector stores, relational databases, and hybrid systems when implementing semantic versus episodic memory in scalable agent applications?</summary>

Phase: [EXPLOITATION]

### Source [60]: https://sparkco.ai/blog/ai-agent-memory-in-2026-comparing-rag-vector-stores-and-graph-based-approaches

Query: What infrastructure-level trade-offs exist between using pure vector stores, relational databases, and hybrid systems when implementing semantic versus episodic memory in scalable agent applications?

Answer: Pure vector stores excel in semantic search via ANN indices (HNSW/IVF) with low latency (10-100ms for 100M vectors) but lack relational integrity, explicit relationships, and struggle with multi-hop reasoning or precise navigation, leading to context loss from chunking and poor scaling with high-dimensional data. Relational databases (e.g., Postgres) offer ACID consistency, structured storage for episodic memory (timestamps, conversations), and compliance but are slower for similarity searches without extensions. Hybrid systems (vector + graph) combine semantic recall with relational traversal, achieving 80% accuracy vs 50% for vanilla RAG and 35%+ precision gains, ideal for tasks needing both broad search and precise navigation like long-term personalization or multi-hop reasoning. Trade-offs: hybrids increase maintenance (1.5x costs, higher complexity) but suit compliance-heavy apps; vectors for quick semantic responses; graphs for auditable relationships. Benchmarks show vectors at 20-100ms P95 latency (small scale), graphs 100-300ms; storage $0.10-0.40/GB/month. Decision matrix: vectors for conversational agents, hybrids for contextual depth in scalable agents.

-----

-----

Phase: [EXPLOITATION]

### Source [61]: https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach

Query: What infrastructure-level trade-offs exist between using pure vector stores, relational databases, and hybrid systems when implementing semantic versus episodic memory in scalable agent applications?

Answer: Unified PostgreSQL (relational hybrid with hypertables/pgvector) for episodic (time-series conversations via hypertables), semantic (vector embeddings with DiskANN/HNSW), and procedural memory avoids multi-DB fragmentation, reducing ops complexity/costs by 66%, enabling single-query context windows with ACID guarantees. Pure vector stores lack time-series optimization and relational CRUD; relational DBs lack native vector similarity (sub-50ms at millions embeddings). Hybrid unifies via pgvectorscale (471 QPS at 99% recall on 50M vectors), compression (90%+ reduction), temporal filtering for time-aware RAG. Trade-offs: eliminates serial round-trips/network hops; scales to production with hypertables partitioning; supports LangChain/LangGraph. Episodic needs range queries (hypertables); semantic needs ANN (pgvectorscale); procedural needs transactions (Postgres ACID). For scalable agents, unified cuts infrastructure scaling costs faster than data growth.

-----

</details>

<details>
<summary>What theoretical foundations from production systems in cognitive architectures support organizing agent memory into working, episodic, semantic, and procedural modules?</summary>

Phase: [EXPLOITATION]

### Source [64]: https://arxiv.org/html/2309.02427v3

Query: What theoretical foundations from production systems in cognitive architectures support organizing agent memory into working, episodic, semantic, and procedural modules?

Answer: The paper 'Cognitive Architectures for Language Agents' draws on production systems and cognitive architectures like Soar to support organizing agent memory into working, episodic, semantic, and procedural modules. Soar, a canonical production system-based cognitive architecture, uses working memory to store recent perceptual input, goals, and intermediate reasoning results (reflecting Baddeley and Hitch, 1974). Long-term memory is divided into procedural memory (storing the production rules), semantic memory (facts about the world; Lindes and Laird, 2016), and episodic memory (sequences of past behaviors; Nuxoll and Laird, 2007). Productions in procedural memory match preconditions against working memory to modify memories or issue actions in decision cycles. The CoALA framework explicitly adopts this organization for language agents, with working memory as a persistent data structure across LLM calls, episodic for past experiences, semantic for world knowledge, and procedural for agent code and LLM weights. This structure enables flexible, rational behaviors mimicking human cognition, addressing LLM statelessness for multi-step world interaction.

-----

-----

Phase: [EXPLOITATION]

### Source [65]: https://arxiv.org/html/2603.04740v1

Query: What theoretical foundations from production systems in cognitive architectures support organizing agent memory into working, episodic, semantic, and procedural modules?

Answer: The paper 'Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens' references the CoALA framework and Soar architecture as foundational for the memory taxonomy dividing agent memory into episodic, semantic, procedural, and working types. CoALA, drawing from cognitive science and Soar, organizes language agent memory into short-term working memory and long-term memories: episodic (past experiences), semantic (world facts), and procedural (rules/code). This taxonomy, widely adopted in surveys and LangGraph documentation, provides intuitive clarity mapping to human memory. Soar 9 extends this with psychological realism: working memory for current state, procedural for production rules, semantic for facts, episodic for past behavior snapshots. The paper critiques functional approaches, proposing Memory-as-Ontology but grounding in these production system foundations for persistent agents.

-----

-----

Phase: [EXPLOITATION]

### Source [67]: https://ccn.psych.purdue.edu/papers/cogArch_agent-springer.pdf

Query: What theoretical foundations from production systems in cognitive architectures support organizing agent memory into working, episodic, semantic, and procedural modules?

Answer: The chapter 'Cognitive architectures and agents' details Soar and ACT-R's production system foundations for memory organization. Soar 9 subdivides long-term memory psychologically: procedural (associative rules), semantic (world facts), episodic (working memory snapshots). Working memory holds goals/perception for production matching. ACT-R distinguishes procedural (production rules) and declarative memory (chunks), with modules/buffers; later versions add semantic/episodic. Productions fire serially on buffers, enabling goal-directed behavior. CLARION complements with implicit/explicit dual-processes. These support modular, psychologically realistic cognition via production systems.

-----

</details>

<details>
<summary>How has the increase in LLM context window sizes from 8k to over 1M tokens impacted the engineering trade-offs in agent memory system design?</summary>

Phase: [EXPLOITATION]

### Source [74]: https://atlan.com/know/llm-context-window-limitations/

Query: How has the increase in LLM context window sizes from 8k to over 1M tokens impacted the engineering trade-offs in agent memory system design?

Answer: Larger LLM context windows from 8k to over 1M tokens increase compute costs and latency per request, limiting production use frequency. They introduce quality vs. length tradeoffs where models forget earlier details or rely on shallow pattern matching. Even with million-token windows, limitations persist; teams treat context as a scarce resource. For agents, multi-step workflows accumulate intermediate state from tool calls, causing overflow, slowness, and errors. Solutions include constraining tool outputs to structured payloads (e.g., IDs and key fields instead of text blobs), token budgeting with pre-request estimation and policies (drop low-priority items, re-summarize), and acceptance tests for worst-case prompts. Hybrid retrieval and summarization outperform brute-force long prompts. Long-context models do not eliminate retrieval needs; they reduce truncation but not noise. Production teams use retrieval, compact tool outputs, and clean metadata to keep prompts small, improving quality, reliability, latency, and cost predictability in agent designs.

-----

-----

Phase: [EXPLOITATION]

### Source [75]: https://aiagentmemory.org/articles/context-window-llm-openai/

Query: How has the increase in LLM context window sizes from 8k to over 1M tokens impacted the engineering trade-offs in agent memory system design?

Answer: OpenAI expanded context from GPT-3.5's 4k, GPT-4's 8k/32k to GPT-4 Turbo's 128k tokens, enabling agents to retain more user/task/past interaction info for sophisticated behavior. Larger windows enhance conversational AI (recall details, avoid repetition) and complex tasks (keep project details without frequent external retrieval). However, limits cause truncation, losing older info. Agents rely on LLM context as short-term memory; exceeding leads to errors. Tradeoffs drive external memory systems: RAG retrieves from knowledge bases into prompts; memory management (e.g., Hindsight) stores/retrieves history; summarization compresses info. As windows grow to 1M+, distinction blurs between LLM context and external memory, pushing integrated architectures that draw from both for holistic agent design. Future infinite context may obsolete fixed windows, but current expansions necessitate balancing native capacity with persistent storage for long-term agent memory.

-----

-----

Phase: [EXPLOITATION]

### Source [76]: https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows

Query: How has the increase in LLM context window sizes from 8k to over 1M tokens impacted the engineering trade-offs in agent memory system design?

Answer: Context windows grew from 512 (2018) to 1M+ (2024), enabling longer documents, extended conversations, and Cache-Augmented Generation (CAG) for pre-computed document caches improving latency over RAG by avoiding retrieval. However, long contexts degrade reference identification (worse for later tokens), lower accuracy (longer prompts less accurate), increase costs (more input tokens, higher training/hosting), and output latency. For agents, unnecessary full-window use harms performance; best to be selective, structure info early, monitor, and hybridize CAG/RAG. Expansion to millions isn't a silver bullet; tradeoffs favor thoughtful context use over maximization, balancing performance, cost, quality in memory design—retrieval still superior for vast data beyond even 10M tokens.

-----

-----

Phase: [EXPLOITATION]

### Source [77]: https://towardsai.net/p/machine-learning/the-context-window-paradox-engineering-trade-offs-in-modern-llm-architecture

Query: How has the increase in LLM context window sizes from 8k to over 1M tokens impacted the engineering trade-offs in agent memory system design?

Answer: Context expansion to 1M+ tokens faces quadratic attention O(n²) scaling: 4x length = 16x memory, superlinear latency, prohibitive costs. 'Lost in the middle' effect degrades middle-context recall. For Llama 3.1 8B, 8k is optimal sweet spot for RAG QA, with diminishing returns beyond. Agents must balance: expanded context enables multi-hop reasoning but increases adversarial risks (prompt injection). Tradeoffs demand task-specific optima, cost-quality calibration, adaptive strategies (minimal for easy queries, max for hard). Production implies classifying tasks, monitoring metrics, hybrid retrieval; naive max-context destroys economics. Architectural responses (sparse attention, GQA) mitigate but don't eliminate need for external memory in agent designs.

-----

-----

Phase: [EXPLOITATION]

### Source [78]: https://www.rockcybermusings.com/p/the-context-window-trap-why-1m-tokens

Query: How has the increase in LLM context window sizes from 8k to over 1M tokens impacted the engineering trade-offs in agent memory system design?

Answer: 1M+ windows (Gemini 1M, GPT-5 400k, Claude 200k) cause 'context rot': performance degrades catastrophically past 10-50k tokens due to non-uniform attention (overweights edges, neglects middle). Agents get dumber (hallucinations), costlier (tokens), less secure (injection surfaces). Multi-agent systems use 15x more tokens, suitable only for high-value tasks. Tradeoffs favor context engineering over inflation: RAG (selective retrieval), MCP (tools), structured memory (external stores), compaction (summarization). Single-agent with RAG first; multi-agent only if justified. Security adds mitigations (sanitize tools, signing). Naive expansion fails; curate right 2k tokens for production agent memory.

-----

</details>

<details>
<summary>What are the advantages of using hybrid vector and graph databases for implementing the three types of long-term memory in production agent applications?</summary>

Phase: [EXPLOITATION]

### Source [80]: https://www.getmaxim.ai/articles/comparing-agent-memory-architectures-vector-dbs-graph-dbs-and-hybrid-approaches/

Query: What are the advantages of using hybrid vector and graph databases for implementing the three types of long-term memory in production agent applications?

Answer: Hybrid approaches combine vector databases for semantic search and graph databases for relationship reasoning, enabling queries that require both semantic understanding and relationship reasoning. An agent can find semantically relevant content and then explore connections through explicit relationships, supporting more sophisticated behaviors than either alone. Teams can optimize each component independently: vector DBs focus on semantic search performance, graph DBs on relationship traversal, yielding better overall system performance via separation of concerns. Hybrid provides flexibility for different query types: simple semantic queries use vector DB, complex relationship queries use graph DB, sophisticated ones leverage both. This is particularly useful for production AI agent memory systems handling both unstructured content (semantic/episodic memory via vectors) and structured relationships (procedural/semantic memory via graphs), enhancing retrieval accuracy, context maintenance, and decision-making in multi-turn interactions and growing data volumes.

-----

-----

Phase: [EXPLOITATION]

### Source [81]: https://47billion.com/blog/ai-agent-memory-types-implementation-best-practices/

Query: What are the advantages of using hybrid vector and graph databases for implementing the three types of long-term memory in production agent applications?

Answer: Mem0 uses hybrid storage for the three types of long-term memory: Postgres for structured facts (semantic memory), Qdrant vector DB for semantic search (semantic/episodic memory), and Neo4j for graph memory (procedural/relational memory). This enables persistence across sessions, personalization, multi-session continuity, and self-improving loops via automatic summarization, expiration, and importance-based updates. Graph memory excels at multi-hop reasoning (e.g., relating user reviews to purchases), faster lookups than pure vector similarity in complex domains. Benchmarks show up to 26% accuracy gains over plain vector approaches by intelligently consolidating data. Supports episodic (interaction histories), semantic (facts/preferences), and procedural (workflows/skills) memory, turning stateless LLMs into persistent systems for production-grade agents in personalization, artifact management, etc.

-----

-----

Phase: [EXPLOITATION]

### Source [82]: https://atlan.com/know/vector-database-vs-knowledge-graph-agent-memory/

Query: What are the advantages of using hybrid vector and graph databases for implementing the three types of long-term memory in production agent applications?

Answer: Hybrid architectures (e.g., GraphRAG, Zep/Graphiti, Neo4j vector index) use vector DBs for semantic entry-point retrieval (breadth for semantic/episodic memory) and knowledge graphs for multi-hop relational depth (structured reasoning for procedural memory). Standard pattern: Embed query for ANN to find relevant entry nodes, then graph traversal for relationships. A survey of 28 GraphRAG methods confirms hybrids achieve better results for complex cases. Provides vector's zero cold-start/sub-ms retrieval for unstructured content and graph's deterministic multi-hop/explainability for entities/relationships. Mem0 graph mode reaches 58.13% on time-sensitive questions vs. 21.71% for baselines. Ideal for production enterprise agents needing both semantic similarity and structured context across memory types.

-----

-----

Phase: [EXPLOITATION]

### Source [83]: https://machinelearningmastery.com/vector-databases-vs-graph-rag-for-agent-memory-when-to-use-which/

Query: What are the advantages of using hybrid vector and graph databases for implementing the three types of long-term memory in production agent applications?

Answer: Hybrid uses vector DB for initial semantic retrieval to locate entry nodes, then graph traversal for precise relational context. Marries vector's broad fuzzy recall (semantic/episodic memory from unstructured data) with graph's strict deterministic precision (procedural memory via explicit relationships). Ideal for advanced agent memory in enterprise workflows requiring complex dependencies, factual accuracy, explainability. Vector handles conversational grounding; graph structures high-value entities/relationships. Leading systems combine both for long-term memory supporting multi-step reasoning over unstructured/structured data.

-----

-----

Phase: [EXPLOITATION]

### Source [84]: https://sparkco.ai/blog/ai-agent-memory-in-2026-comparing-rag-vector-stores-and-graph-based-approaches

Query: What are the advantages of using hybrid vector and graph databases for implementing the three types of long-term memory in production agent applications?

Answer: Hybrid (vector + graph) offers broad retrieval + detailed traversal, 80% accuracy boost, 35% precision gain over pure approaches. Vector for semantic similarity (semantic/episodic), graph for explicit relationships/multi-hop (procedural). Benchmarks: Hybrid GraphRAG 80% accuracy vs. 50% vanilla RAG. Ideal for tasks needing both, like e-commerce recommenders (vector recall + graph links). Combines strengths for production scalability, with moderate maintenance via shared indexing. Supports long-term memory persistence, personalization, complex reasoning in agentic systems.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>How do different embedding update strategies and vector database indexing methods impact the long-term performance of hybrid semantic-episodic memory retrieval?</summary>

Phase: [EXPLORATION]

### Source [45]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: How do different embedding update strategies and vector database indexing methods impact the long-term performance of hybrid semantic-episodic memory retrieval?

Answer: Vector databases store embeddings and enable Approximate Nearest Neighbor (ANN) search using structures like HNSW, allowing sub-linear search over millions of entries with 1536-dimensional embeddings from OpenAI models. Typical production setup: 1536D embeddings, HNSW indexing, top-k=20 retrieval, sub-50ms latency at multi-million scale. Vectors excel at semantic similarity for fast search but lack relational encoding, struggling with multi-hop reasoning. Graph storage encodes explicit relationships (nodes like user_u123, edges like has_preference with weights/timestamps) for traversal queries but requires schema design. Hybrid approach combines vector search (top-k candidates) with graph traversal, fusing scores (e.g., 0.7×vector + 0.3×graph). Mem0's hybrid balances performance/structure: vectors for fast semantic retrieval, graphs prevent relational drift, improve multi-hop reasoning. Retrieval pipeline: embed query to 1536D, search top k=20, score by relevance×recency×type_weight (semantic:0.6, episodic:0.3, procedural:0.1), inject top-5 under 200 tokens. Hybrid reranking boosts multi-hop J-score 15%. Consolidation (merge similar embeddings >0.85 similarity) cuts storage 60%, raises precision 22%. Well-configured vector index scales to 100M+ entries maintaining recall/latency. Architectural choice impacts multi-hop reasoning, scalability, contradictions resolution: vectors fast/simple but falter on relations; graphs expressive but overhead; hybrids improve reasoning.

-----

-----

Phase: [EXPLORATION]

### Source [46]: https://oneuptime.com/blog/post/2026-01-30-long-term-memory/view

Query: How do different embedding update strategies and vector database indexing methods impact the long-term performance of hybrid semantic-episodic memory retrieval?

Answer: VectorMemoryStore uses 1536D embeddings with FAISS/Pinecone/Weaviate indexes. For <100K memories, HNSW works well; for millions, distributed like Pinecone/Weaviate. MemoryConsolidator applies decay (days_since_access), clusters similar memories (DBSCAN eps=1-similarity_threshold=0.85), merges (average vectors, LLM conflict resolution), prunes low-importance (<0.1), strengthens frequent access. Cuts storage, optimizes retrieval. Retrieval strategies: VECTOR_ONLY (cosine similarity), HYBRID (vector+keyword, RRF fusion k=60), TEMPORAL (time_window_days filter), IMPORTANCE_WEIGHTED (similarity*0.7 + importance*0.3). Multi-stage: initial retrieval, type filter, LLM rerank, diversity (MMR), update access metadata. Forgetting: decay_importance (exp(-0.01*days)), retention_score (importance*0.4 + access/100*0.3 + recency*0.3), archive (<0.2), delete (<0.05), handle contradictions (newer overrides). Separate episodic/semantic/procedural: episodic decays faster. Monitor retrieval relevance, adjust embedding/retrieval if irrelevant pulls increase. Schedule consolidation nightly. Hybrid retrieval fuses vector/keyword/temporal/importance. Impacts long-term: consolidation prevents bloat/degraded precision; indexing scales retrieval; strategies balance relevance/diversity/recency; forgetting maintains quality.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agent-memory-systems-beyond-context-windows-cisco-community.md">
Phase: [EXPLOITATION]

## Agent Memory Systems: Beyond Context Windows

## Key Takeaways

- **Context Limitations** Even with advancements like 400K token context windows, traditional LLMs struggle with memory retention across interactions, leading to repeated token costs.

- **Persistent Memory** Implementing persistent memory architectures allows agents to remember information across sessions, enhancing their ability to provide consistent and informed responses.

- **Database Integration** Utilizing various types of databases (vector, episodic, network) allows agents to efficiently store and retrieve contextual information, improving their operational capabilities.

- **Agent Evolution** Agents can learn and adapt over time by tracking their experiences, leading to improved capabilities and more efficient problem-solving methods.

Video transcript (click here):

Welcome to Agentic Impressions, where we'll be discussing various topics across the agentic AI landscape. Our first season will be covering the basics of agentic AI. Today, we'll be discussing the role of context windows as the second episode in our series. Hi everyone, my name is Shereen Bellamy. I'm a Senior Developer Advocate at Cisco, focusing on AI, security, and quantum. I'm here to share my findings and discuss with you all. And today, as promised, we're going to be discussing agent memory systems. In our last episode, we proved that architecture beats raw power. But here's a problem that everyone's still hitting, context windows. Context windows are still a bottleneck in the industry. Even with clods like 200,000 total tokens, and even GPT-5 is like up to 400K tokens now, you're still constrained by what fits into one single conversation. Let's tackle this specific problem for today. We'll call it the token triangle problem. Let's say we want to work with an LLM that has a context window of 128K tokens. Seems like a large enough number, but we're hitting the limit after analyzing 85 configs, way less than our goal. This is a result of high cost through expensive token usage. You pay per token, and when we access the LLMs, it's processing our query using those tokens. Everything you send to the LLM gets converted into tokens. Whatever it sends back is also composed of tokens. This is also due to the inability to continue interacting with the LLM due to the limit on how much it can actually digest. How many tokens you can send are defined by the LLM's ability, and sometimes by your plan. And LLMs will naturally forget between API calls. So a scenario on what this would look like is you would send 50K tokens of context, like configs, logs, topology, to the LLM. The cost might be arbitrarily like 50 cents. Now you're gonna wait for your LLM to respond with advice. That's 500 tokens. And then five minutes later, you would ask a follow-up question to get more clarification, the answer you need, maybe get more data. But your LLM, your natural standalone LLM, has forgotten everything. So you have to send all 50K tokens again, which would cost another 50 cents. And this would happen about 10 times in a troubleshooting session, right? While you try through trial and error to fix it. Now your total cost may come up to like $5. The total token sent can be up to 500,000 now. But you can have massive duplication in this dataset. And at the same time, you're constantly hitting context limits, which you have to wait to refresh to get your next output. Through the concept of persistent memory, we can see today how databases can help us overcome that problem and what specifically put inside of those databases that we can build on in the future. So again, if we look at this issue from a critical thinking perspective, what if agents had persistent memory that worked across sessions, learned from every interaction and has the ability to get better over time? That's what we're focused on today. Today, we're going to be building memory architectures. I'll show you persistent memory systems, benchmark different approaches and demonstrate the concept of agent self-registration. This is where agents have the ability to remember who they are and what they've learned. Again, when we look at the concept of architecture, especially looking at the design of something like the memory, then we're able to optimize what makes the agent so special, right? Their skills. So let's build it. So let's start by running this persistent agent Python file and see what it does. Then I'll show you how the code works. In these lines, the agent is storing network events, router interface down, switch CPU high, interface backup, and it's remembering the device configurations. Instead of keeping everything in AI's temporary memory, we're using a database, just like how your routers are storing their config in NVRAM instead of regular RAM. We have three types of databases, vector, episodic and network. SQLite is just a file-based database. Think of it like a really smart spreadsheet that never forgets, and we're using three of them. We have our VectorDB. This is for searching by meaning. So if you search something like interface problems, it would find related events, even if they don't have those exact words. We have an episodic database. This stores things in time order, like your syslog from oldest to newest. Then we have our network database. This is our custom database for network-specific stuff, like device IDs and IP addresses. So what happens when it remembers something? When you call the remember function, like when we remembered what routers R1 interface went down, it writes all three databases. That's three different ways to find that information later. It's like documenting an incident in your ticketing system, your runbook, and your network diagram. It's a little redundant, but it's powerful. So here we integrate the AI portion by calling an OpenAI API key. When we analyze the network issue, we're not just searching the database. We're asking a real AI to look at the problem and suggest fixes. So let me run it again and show you the AI-powered analysis. For this analysis, this is coming from GPT-4 looking at the network issue, saying that router interface flapped, switch has high CPU, and giving real troubleshooting steps. It's like having a senior network engineer on call 24-7. So when we mix AI's intelligence with their permanent database memory, AI is able to provide the analysis and the database is able to provide the history. So try closing the terminal and then run it again. Those .db files are still there. The agent's still able to remember everything from last time, making it persistent. Okay, so we can store things in a database. Let's do a memory benchmark to see why. This benchmark is going to create 100 network devices. So imagine a medium-sized enterprise network, and then we'll test two approaches. One, our persistent database approach that we just discussed, and two, the traditional context window approach, which is what most AI tools use. Watch what happens. This for loop is able to create 100 fake network devices, dev one, dev two, up to dev 100. Each has a host name, IP address, type, and status, just like your real network inventory. For the results, we can see that persistent memory gave us 100% accuracy in two seconds. Meanwhile, context windows gave us 40% accuracy in 0.8 seconds. We can say our database approach remembers every device perfectly. You can ask it about dev one, and it can give you dev one's info every single time. We also know that our context window approach only remembers about 40% of devices. Why? That's because it's trying to remember 100 devices in its temporary memory. It's like trying to memorize the entire network topology during a phone call. You'll most likely forget most of it, and you might be able to recall some of it. Also, the database lookup is 40 times faster. That's the difference between querying a well-indexed database and searching through notes. And in terms of five times more devices, context windows max out around 20 devices most of the time, so our approach handles 100, which could handle 10,000 just as easily. But with 10,000 examples, grouping things together can really help, and that's where event correlation comes in. So for this section, we can track that dev one has had three related events. It's had interface flapping detected, packet loss increased, and the interface went down. These events all happen to be these events all happen to different times, but we can correlate them because they're all stored permanently with timestamps and device IDs. That's how you do the root cause analysis, which will be helpful for us to see our patterns over time. Context windows don't have the ability to do that because they forget the first event by the time that the third one happens. Finally, we're going to get into our self-registering agent. So this agent can track its own capabilities and learn new ones from experience. So let's run it and see what it says. The agent just created itself with a unique ID. It starts with three basic capabilities, device monitoring, configuration management, and event logging. Now watch what happens when we log a critical network event. We log that the router R1 interface went down as a critical event. And then when we look at the next line, we can see that the agent automatically learned a new capability called incident troubleshooting. This is possible through our log network event function. Our function is saying that if the severity is critical and we haven't learned troubleshooting yet, then please learn it. Just like humans can build new skills based on experience, this agent is learning incident response by doing it. So let's see how it does with four more capabilities. Now our agent knows BGP troubleshooting, automated failover, security analysis, and performance optimization. That's eight total capabilities up from three. And these capabilities will be stored in those databases that we created earlier. This is a database table that tracks what the agent knows and when it learned it. If you restart the agent, then it will still know all eight capabilities. This matters for network operations because you can track what has this agent handled before? When did it learn to handle BGP issues? And what evidence do we have of what it can do? So similar to episode one, the conclusion here is that structure matters. Just like you wouldn't store your entire network config into one single text file, you shouldn't store all of your agent's knowledge in temporary memory. You should use the right tool for each job. So database for persistence, vector search for semantic similarity, graphs for relationships, and timelines for chronological events. So what next? How do you implement this? First, take a look at the GitHub in the description and try to implement what we did today. When you go to the GitHub repo, you'll see an additional file called agencymemoryimplementation.py. I won't be running it here today. It contains a full agency SDK implementation demo, including its Corto and Longo protocols named after coffee. Corto is agency's memory coordination protocol, which is how agents share and synchronize their memories across a distributed system. And Longo is the self-registration protocol. It's how agents discover each other and register their capabilities in a directory. It also shows you what a production-ready environment looks like with all of the databases working together. When you look at this in the context of the real world, you can have customer service agents that remember every interaction across months. In terms of research, you can have assistants that build knowledge graphs for all your documents. In terms of coding, you can have software development agents that learn your coding patterns, your preferences. And in terms of business, you can have business-specific agents that maintain context across projects and teams. We're moving from stateless interactions to persistent AI relationships. These aren't just tools. They're collaborative partners that have the ability to grow and grow smarter through every interaction. Coming up next week, we're going to focus mainly on multi-agent teams. For deeper information on agency-specific implementations, please feel free to check out that YouTube channel as well. Please subscribe for updates on when we release episode three and drop a comment on what type of agent team you'd most likely want to build. Memory architecture is important to look at, but building a team with what we learned might yield some pretty cool results. As usual, thanks everyone for joining, and I'll see you next time.
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ai-agent-memory-comparative-guide-rag-vs-vector-stores-vs-gr.md">
Phase: [EXPLOITATION]

## Overview of Memory Architectures: RAG, Vector Stores, and Graph-Based Approaches

Memory architectures are pivotal for AI agents, overcoming LLM limitations in long-term recall and context handling. RAG augments generation with external retrieval, vector stores enable semantic search via embeddings, and graph-based approaches model relational knowledge. These systems answer key questions: Memory is represented as indexed documents (RAG), vector spaces (stores), or node-edge structures (graphs); queried via hybrid search, ANN, or traversal. Embeddings are generated using transformers or GNNs and updated incrementally. Consistency for concurrent updates relies on eventual models with locking or ACID transactions. Context windows are filled by top-k retrieved items, scored by similarity or path metrics, with freshness ensured through TTL expiration and versioning to manage updates without full re-indexing.

#### Component-Level Descriptions of Memory Architectures

| Feature | RAG | Vector Stores | Graph-Based Memory |
| --- | --- | --- | --- |
| Core Components | Retriever (DPR), Index (FAISS/ES), LLM Generator | Embedding Model, ANN Vector DB (HNSW/IVF), Query Encoder | Entity Extractor, Graph Store (Neo4j), GNN Embedder (GCN) |
| Indexing/Storage Format | Hybrid: BM25 Inverted + Dense Vectors | Dense Vectors (768-1536 dim) in ANN Structures | Adjacency Lists + Node/Edge Embeddings in KG |
| Retrieval Mechanism | BM25 Sparse + Dense Cosine, Score Fusion | Approximate k-NN Search (Cosine/IP) | Graph Traversal (BFS/DFS) + GNN Propagation |
| Data Flow (Ingest to Retrieve) | Chunk → Embed/Index → Query → Top-K Fusion → Augment | Text → Vectorize → Store → Embed Query → ANN Retrieve | Data → Extract Triples → Build Graph → Traverse → Subgraph Extract |
| State Update Mechanics | Batch Re-Index with Timestamps | Upsert Embeddings, Asynchronous | Incremental Edge Addition, Temporal Versioning |
| Embeddings Generation/Update | Transformer (BERT) on Chunks, Re-Embed on Change | Sentence Transformers, Dim Reduction, Async Update | GNN Message Passing, Update on Graph Diff |
| Relevance Scoring | Reciprocal Rank Fusion (RRF) | Cosine Similarity Threshold | Path-Based + Attention Weights |
| Consistency for Concurrent Updates | Eventual via Sharding/Locking | Optimistic Locking, Sharded Writes | ACID Transactions in Graph DB |

### Retrieval-Augmented Generation (RAG)

RAG integrates retrieval into LLM pipelines, core components include a retriever (e.g., dense passage retriever), index (hybrid sparse-dense), and generator LLM. Data flow: Ingestion chunks documents, embeds via BERT-like models into vectors/BM25 indices; storage in Elasticsearch or FAISS. Retrieval uses BM25 for lexical or dense cosine similarity, fusing scores for top-k results to fill context windows (e.g., 4k tokens). State updates via batch re-indexing with timestamps for versioning; freshness via TTL on indices. Concurrent consistency through sharded eventual models. Embeddings update on new data ingestion.

### Vector Stores (ANN-Based Vector Databases)

Vector stores like Milvus, Pinecone, and Weaviate use ANN indices for efficient semantic search. Core components: embedding model (Sentence Transformers), vector DB with HNSW/IVF structures, query encoder. Data flow: Ingest text → generate dense embeddings (e.g., 768-dim) → store with metadata; indexing via hierarchical navigable small world graphs. Retrieval: dense vector similarity (cosine/IP) for top-k nearest neighbors, filling LLM contexts with ranked snippets. Updates: upsert embeddings with UUID versioning; TTL for eviction in dynamic caches. Consistency via optimistic locking or sharding for concurrent writes. Embeddings regenerate on data changes, often asynchronously.

### Graph-Based Memory Systems

Graph-based systems employ knowledge graphs and heterogeneous embeddings via GNNs for relational memory. Core components: entity extractor, graph store (Neo4j), GNN embedder (GCN/GAT). Data flow: Ingest unstructured data → extract triples (entities/relations) → build/store graph with adjacency lists and node embeddings; indexing embeds subgraphs. Retrieval: graph traversal (BFS for hops) or GNN propagation for relevance, retrieving subgraphs to augment contexts (e.g., path-extracted facts). State updates incrementally add edges with versioning; freshness via TTL on nodes and temporal graphs. Concurrent consistency through ACID transactions in graph DBs.

Embeddings update via message passing in GNNs on graph changes. Scoring uses path lengths or attention weights; excels in multi-hop queries per 2024 arXiv papers.

## Product Architecture and Implementation Patterns

Integrating an agent memory layer with large language models (LLMs) requires robust architectures that balance latency, scalability, and recall.

### Blueprint A: Simple RAG Proxy with Cold Storage

Data model: Document JSON schema: {'id': str, 'content': str, 'metadata': {'source': str, 'timestamp': datetime}}. Vector metadata: {'doc\_id': str, 'embedding\_dim': 768, 'score': float}. Pseudocode ingestion: for doc in stream: embed = embedder.encode(doc.content); index.add(embed, doc.id); metadata\_store.upsert(doc). Query: query\_embed = embedder.encode(q); results = index.search(query\_embed, k=5); return augment\_prompt(results).

### Blueprint B: Vector Store-Backed Memory with Streaming Updates and Hot Cache

Data model: Document JSON: {'id': str, 'chunks': \[str\], 'metadata': {'agent\_id': str, 'version': int}}. Vector metadata: {'chunk\_id': str, 'norm': float, 'timestamp': datetime}. Pseudocode ingestion: while stream: chunk\_embed = embedder(chunk); vector\_store.upsert(chunk\_embed, metadata); cache.set(key=hash(chunk), value=chunk, ttl=3600). Query: if cache.hit(q): return cache; else: hits = vector\_store.query(q\_embed, filter=agent\_id); cache.set(hits); return hits.

### Blueprint C: Graph-Backed Semantic Memory for Multi-Hop Reasoning with Embedding Augmentation

Data model: Graph nodes: {'type': 'entity', 'props': {'name': str, 'embedding': \[float\]}}. Edges: {'from': str, 'to': str, 'relation': str, 'weight': float, 'metadata': {'timestamp': datetime}}. Pseudocode ingestion: entities = extract\_entities(doc); for e in entities: graph.create\_node(e, embed(e.name)); graph.create\_edge(src, tgt, rel, embed(rel\_text)). Query: start\_nodes = vector\_search(graph, q\_embed); paths = graph.traverse(start\_nodes, hops=3, filter=rel\_type); return aggregate\_paths(paths).

## Performance, Scalability, and Benchmarks

Benchmarking agent memory solutions is essential for ensuring reliable performance in production environments. Key metrics include query latency at P50 (median), P95 (95th percentile), and P99 (99th percentile) to capture response times under varying loads; throughput in queries per second (QPS) for scalability; recall@k and precision@k for retrieval accuracy, where k is the number of top results; freshness as the time to reflect updates; storage cost per GB; cost per query; CPU/GPU utilization percentages; index build time in hours; and cold start time for initialization.

#### Quantitative Performance Bands for Agent Memory Systems

| Scale | System Type | P95 Latency (ms) | Throughput (QPS) | Recall@5 | Storage Cost ($/GB/month) |
| --- | --- | --- | --- | --- | --- |
| Small (<=10M) | RAG (BM25+Embedding) | 50-200 | 100-500 | 0.85-0.95 | 0.05-0.10 |
| Small (<=10M) | Vector Store (e.g., Pinecone) | 20-100 | 500-2000 | 0.80-0.90 | 0
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="llm-context-window-limitations-in-2026.md">
Phase: [EXPLOITATION]

## Key takeaways

- MECW, not the advertised token count, determines real LLM performance — gaps reach 99% on complex tasks.
- Context rot degrades accuracy 30%+ in mid-window positions across all 18 frontier models Chroma tested.
- Enterprise queries consume 50K-100K tokens before reasoning starts — metadata quality is the real constraint.
- RAG + MCP + active metadata governance outperforms larger ungoverned context windows.

## What are LLM context window limitations?

LLM context window limitations refers to the hard cap on how much text an LLM can see at once when generating an answer. Anything beyond this limit must be shortened, summarized, or dropped, which affects how well the model can follow long conversations or reason over large documents. Effective context is often far below the advertised maximum, with some models losing over 99% of claimed capacity on complex tasks.

### Key components:

- Context window. Total tokens (prompt + output) an LLM processes in a single inference call
- MECW. Maximum Effective Context Window — the point where accuracy actually holds up, vs. the advertised limit
- Context rot. Degradation in output quality as input length grows, especially for mid-window positions
- MCP. Model Context Protocol — an open standard for delivering structured, governed metadata to LLMs

| Term | What it means |
| --- | --- |
| Context window | Total tokens (prompt + output) an LLM processes in a single inference call |
| Token | The smallest unit of text an LLM processes; ~0.75 English words per token |
| MECW | Maximum Effective Context Window: the point where a model’s accuracy actually holds up, vs. the advertised limit |
| KV cache | Key-value cache storing intermediate attention computations; its memory ceiling limits usable context size |
| Context rot | Degradation in output quality as input length grows, especially for information in the middle positions |
| RAG | Retrieval-Augmented Generation: pulling only relevant chunks into the context window at query time |
| MCP | Model Context Protocol: an open standard for delivering structured, governed metadata to LLMs |
| Context engineering | The discipline of designing systems that dynamically assemble the right information for each model inference step |

Most models market a context window range, but effective context often falls far below the advertised maximum. For example, Llama 4 Scout advertises a 10-million-token context window. GPT-4.1 claims one million. Yet research from Paulsen (2025) found that a few top models failed with as little as 100 tokens in context, and many showed clear accuracy degradation by 1,000 tokens, far below their advertised limits.

## What is a context window?

A context window is the total information an LLM processes per inference, including instructions, conversation history, retrieved documents, and output. Measured in tokens (approximately 0.75 words each). The attention mechanism determines which tokens influence each prediction. KV cache stores intermediate computations. Larger windows extend the range but don’t eliminate attention degradation.

Different architectures handle context at scale through different trade-offs. Three approaches are common:

- **Full-context loading** feeds everything into the model at once. Simple but expensive: compute cost scales quadratically with input length. For a short document and a single query, this works. At enterprise scale, it becomes prohibitively slow and costly.
- With **sliding window attention**, the model uses a rolling look-back of fixed length, attending only to the most recent N tokens at any point. Compute costs stay manageable, but the model loses access to information outside the window. In documents where distant facts are connected, long-range recall suffers.
- **Hierarchical attention** takes a different approach, assigning priority levels across the context. Recent tokens and high-signal tokens receive more attention weight, while mid-window content receives less. [Multiple studies have confirmed](https://arxiv.org/abs/2307.03172) that LLMs naturally exhibit this behavior in practice, prioritizing the beginning and end of their context while neglecting the middle, even when not explicitly designed to do so.

### Isn’t the context window size sufficient to determine LLM performance?

Context window size alone does not determine LLM performance. Every token in a shared budget (system prompts, retrieved documents, conversation history, and model output) competes for attention. The KV cache, which stores intermediate attention computations, hits physical memory limits at large context sizes, creating a bottleneck that prevents models from actually using all supported tokens.

Every LLM breaks text into tokens before processing it. One token roughly equals 0.75 English words, which means a 128K-token window holds about 96,000 words. System prompts, retrieved documents, conversation history, and the model’s own output all consume tokens from this shared budget.

**How does the model decide which tokens matter?**

Through the attention mechanism, which assigns weights that control how much influence each token has on each prediction. This is where the ‘bigger is better’ assumption falls apart.

The KV cache (key-value cache) stores intermediate attention computations to avoid recomputing them for every new token. But this cache has physical memory limits. Once a context window grows large enough, the KV cache becomes the bottleneck, preventing the model from actually using all the tokens it claims to support.

## What are the key context window limitations?

LLM context windows face three core limitations: the advertised vs. effective gap (effective context often falls far below the marketed maximum, by up to 99% on complex tasks), working memory bottlenecks (frontier models manage only a handful of variables before reasoning breaks down), and context rot ( [accuracy drops over 30%](https://arxiv.org/abs/2307.03172) when relevant information sits in middle positions). Task type, not token count, determines real performance.

### Advertised vs. effective context window

The Maximum Effective Context Window (MECW) is a model’s real performance ceiling, not its advertised limit. [Research](https://arxiv.org/abs/2509.21361) shows effective context often falls far below the advertised maximum, by up to 99% on some tasks. Attention degrades non-linearly past this ceiling, and context rot begins well before the advertised limit.

#### Measuring MECW

Norman Paulsen’s 2025 paper answers that with a concept called Maximum Effective Context Window (MECW). The idea: embed specific facts at different positions in a context, then ask the model to find them across different problem types. If it can’t, the model has exceeded its effective window.

The results were striking. All models fell short of their advertised Maximum Context Window by [more than 99% in some cases](https://arxiv.org/abs/2509.21361). MECW also shifts based on the type of problem: a model that handles simple retrieval well at 5,000 tokens may fail at complex sorting or summarization tasks at just 400 to 1,200 tokens. No single effective context number applies to a model. The answer depends on what you’re asking it to do.

The NoLiMa benchmark from LMU Munich and Adobe Research (ICML 2025) reinforced this finding by removing literal keyword matches between questions and answers. When models couldn’t rely on surface-level pattern matching, 11 out of 13 LLMs dropped below 50% of their baseline scores at just 32K tokens. [GPT-4o fell from a near-perfect 99.3%](https://arxiv.org/abs/2502.05167) baseline to 69.7%.

#### 2026 LLM effective context window comparison

| Model | Provider | Advertised window | Illustrative effective window \*Not measured | Efficiency % | Primary limitation |
| --- | --- | --- | --- | --- | --- |
| **GPT-4.1** | OpenAI | 1M tokens | ~980K | ~98% | Cost at full context |
| **GPT-4o** | OpenAI | 128K tokens | ~115K | ~90% | Mid-context attention drop |
| **Claude Opus 4** | Anthropic | 200K tokens | ~185K | ~92% | KV cache memory ceiling |
| **Claude Sonnet 3.7** | Anthropic | 
</research_source>

<research_source type="scraped_from_research" phase="exploration" file="long-term-memory-for-ai-agents-the-what-why-and-how.md">
Phase: [EXPLORATION]

# Long-Term Memory for AI Agents: The What, Why and How

Long-term memory stores, consolidates, and retrieves data across sessions, turning stateless AI agents into stateful knowledge accumulators. Unlike token-limited buffers, long-term persistence survives resets, scales with storage, and is required architecture for production agents.

## TLDR

- Long-term memory lets AI agents store and retrieve knowledge across sessions, bypassing single-window limits. Bigger contexts boost tokens but lack consolidation.

- Includes semantic (facts), episodic (interactions), and procedural (styles) memory.

- Production uses extract → consolidate → store → retrieve via vectors or graphs.

- Mem0 benchmarks show 91% lower p95 latency and 90% token reduction versus full-context prompting.

- Structured memory pipelines enable personalization across hundreds of sessions without re-reading prior history.

## What's the Difference Between Short-Term and Long-Term Memory in AI Agents?

[AI agent memory](https://mem0.ai/blog/memory-in-agents-what-why-and-how) refers to an AI system's ability to retain, recall, and utilize information from past interactions to enable continuity and adaptive behavior across sessions. It integrates short-term memory (for immediate context like recent conversation turns, akin to a context window) with long-term memory (for persistent storage of facts, user preferences, workflows, or procedural knowledge).

The differences between short-term and long-term memory come down to five variables:

| **Category** | **Short-term memory** | **Long-term memory** |
| --- | --- | --- |
| Storage mechanism | Context window tokens | External storage with embeddings or graphs |
| Lifespan | Single session | Cross-session and long-lived |
| Capacity | Limited by token window | Scales with storage backend |
| Retrieval method | Linear prompt inclusion | Memory retrieval via search and ranking |
| Use case | Immediate reasoning | Personalization and continuity |

## Why Don't Bigger Context Windows Solve the Memory Problem?

Large context windows delay but do not fix memory failures. Models handle 128K to 1M tokens, yet stuffing full history spikes costs, latency, and unreliability.

[Liu et al.'s 2023 "Lost in the Middle"](https://arxiv.org/pdf/2307.03172) study shows accuracy crashes when facts sit mid-prompt. At 32K tokens, models ignore 70% of middle info. Needle-in-haystack tests confirm drops beyond 10 to 20% depth.

More tokens do not equal better memory.

The paper [_Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory_](https://mem0.ai/blog/graph-memory-solutions-ai-agents) demonstrates that structured memory pipelines outperform full-context baselines. Results show:

- 91% lower p95 latency

- 90%+ token savings

- LOCOMO multi-hop J-score 0.51 vs 0.22 for full-context

Full-history prompting is not just inefficient; it is unreliable at scale.

### Cost and Latency

Token pricing scales linearly. A 200K-token request at $5 per 1M tokens costs roughly $1 per call. At 1,000 daily users running 10 sessions each, monthly spend exceeds $30,000 just for input tokens.

Latency also grows with context size: 4K tokens produces sub-second responses, 200K tokens takes 5 to 10 seconds, and high concurrency creates GPU memory pressure and queue backlogs.

Long-term memory AI agents avoid rereading irrelevant history. Instead, they retrieve only what matters.

Mem0 benchmarks show 1.44s p95 latency at high volume, where full-context approaches often time out. At scale, structured memory is not optional; it is economically required.

### Context Windows Don't Learn

Context windows store raw, contradictory inputs like "User likes Python" then "switched to Rust" with no deduplication, timestamps, or relevance scoring.

Active systems extract facts, overwrite stale entries, and update scores by usage. The 2024 survey "Memory in the Age of AI Agents" notes passive buffers lose 30 to 50% accuracy on temporal tasks. Managed memory ensures coherence over 100+ sessions.

## What Types of Long-Term Memory Do AI Agents Need?

AI agents need three types of long-term memory: semantic, episodic, and procedural. Each serves a distinct cognitive function. Tulving (1972) distinguishes episodic memory (personal events) from semantic memory (facts). The CoALA framework adds procedural memory for agent behaviors. For a deeper look at each type, see our [guide to memory in AI agents](https://mem0.ai/blog/memory-in-agents-what-why-and-how).

### Semantic Memory (Facts and Preferences)

Semantic memory stores what an agent knows about a user — facts, preferences, and constraints that hold across time. A CRM agent that remembers "Budget cap $50K" and "Preferred channel: email" doesn't need the user to repeat themselves every session. When new information contradicts the old — "Budget raised to $75K" — the entry is updated rather than duplicated. This is the foundation of personalization.

### Episodic Memory (Past Experiences)

Episodic memory stores what happened — specific interactions logged with enough context to be useful later. When a user says "Docker issue again?", the agent can surface the relevant history: "Last December you optimized Docker on ECS. Try pruning images first." This is how support agents cut repeat ticket volume; they already know what was tried and what worked.

### Procedural Memory (Learned Behaviors)

Procedural memory stores how an agent should behave — communication styles, formatting preferences, and workflow rules built up from feedback over time. A coding copilot that learns "Team uses Black formatter, 120-char lines" applies that rule to every subsequent response. Negative feedback sharpens the pattern. Over 50+ interactions, the agent's defaults begin to match the team's actual expectations.

## How Does Long-Term Memory Work Under the Hood?

Production pipelines process raw input through extraction, consolidation, storage, and retrieval. MemGPT (2023) introduces paging to swap memory in and out of context. HippoRAG (2024) adds hierarchical retrieval for long-tail accuracy. The sections below cover each stage in detail.

### Memory Extraction and Consolidation

Raw conversations are noisy. In most real-world agent logs, 60 to 70% of tokens are small talk, repetition, or transient reasoning. Storing that verbatim leads to memory bloat, degraded retrieval precision, and rising storage costs. Long-term memory systems must distill signals from conversational noise.

LLMs parse chat turns: "User: I prefer Python. No JS." Extraction yields:

\[{"fact":"prefers Python","negated":"JavaScript","user\_id":"u123","timestamp":"2026-02-13"}\]

Consolidation periodically scans existing memory stores: embeddings with similarity above 0.85 trigger merges via averaged vectors and LLM-based conflict resolution (e.g., "Python overrides JS? Yes"), followed by deduplication of clusters within a 0.9 threshold, while relevance scores are updated from usage patterns (query matches boost +0.1).

This outperforms RAG chunking, which dumps raw text. Consolidation cuts storage by 60% and raises retrieval precision 22%.

### Storage Patterns: Vectors, Graphs, or Both

Once memory units are extracted and consolidated, they must be indexed for retrieval. The two dominant approaches are vector stores and graph databases. In advanced systems, they are combined.

#### Vector Storage

Vector databases store embeddings and enable Approximate Nearest Neighbor (ANN) search. Each memory unit is converted into a high-dimensional vector representation, often 1536 dimensions when using OpenAI's embedding models. These vectors are indexed using structures such as HNSW, which allows sub-linear search over millions of entries.

In a typical production setup, you might configure: 1536-dimensional embeddings, HNSW indexing, top-k retrieval set to 20, and sub-50ms latency even at multi-million scale.

Vectors excel at semantic similarity, allowing the system to retrieve memory based on meaning rather than keyword matching. A well-configured vector index can scale beyond 100 million entries while maintaining acceptable recall and latency.

However, vectors have important limitations. They do not inherently encode relationships between memory units and struggle with structured dependencies and multi-hop reasoning. For example, if you store "User prefers Python" and "Python is used for backend services," a vector store may retrieve both independently, but it cannot reason about their relationship without additional logic. Vectors answer "what is similar?" They do not answer "how are these related?"

#### Graph Storage

Graph databases approach memory from a structural perspective. Instead of embedding text into dense vectors, graphs encode explicit relationships between entities.

In a graph representation, you might model:

- Node: `user_u123`

- Node: `pref_python`

- Edge: `has_preference` (weight 0.95, updated\_at timestamp)

This structure enables direct traversal queries. If a user asks "What language does u123 prefer for backend services?" the graph traverses: user → preference → language → Python.

Graphs are particularly effective for relationship traversal, entity disambiguation, dependency resolution, and structured queries. However, graph systems require careful schema design, edge weighting logic, and traversal optimization. They also lack the fuzzy semantic flexibility of vector embeddings unless paired with text-based indexing.

#### Hybrid Approach

In practice, [high-performance long-term AI memory systems](https://mem0.ai/) combine both models. A hybrid architecture uses vector search for fast semantic retrieval and graph traversal for relational grounding:

1. Perform vector search to retrieve top-k candidate memories

2. Apply graph traversal to validate structural relationships

3. Fuse scores using a weighted model

A common scoring fusion:

Final score = 0.7 × vector similarity + 0.3 × graph traversal confidence

Vectors provide semantic flexibility while graphs provide relational integrity. This hybrid model significantly improves multi-hop reasoning accuracy in scenarios where agents must connect preferences, historical events, and procedural rules.

Mem0 implements this hybrid design to balance performance and structure. Vector embeddings ensure fast search, while graph memory prevents relational drift and improves multi-hop reasoning.

#### Retrieval at Inference Time

Retrieval is where memory becomes useful. The retrieval pipeline embeds the incoming query to a 1536D vector, searches the top k=20 candidates, scores by relevance × recency × type\_weight (semantic: 0.6, episodic: 0.3, procedural: 0.1), and injects the top-5 results under 200 tokens into the prompt.

Retrieval is dynamic per user: u123 sees personalized facts, u456 sees generic context. Hybrid reranking via an LLM pass boosts multi-hop J-score by 15%. RAG searches static documents; memory retrieval adapts live.

#### Architectural Implications

For senior developers, the storage decision determines how well your agent handles multi-hop reasoning, whether contradictions can be resolved structurally, how scalable your indexing strategy becomes, and how easily you can incorporate ranking logic.

Vectors excel in speed for simple queries but falter on relations. Graphs shine in expressiveness but add schema management overhead. Hybrids increase complexity while improving reasoning power.

Choose based on expected cognitive demands: vectors for preference retrieval, hybrids for entity and time-based reasoning.

## How Does Mem0 Handle Long-Term Memory for Agents?

[Mem0](https://mem0.ai/), which [raised $24M to build the memory layer for AI,](https://mem0.ai/series-a) automates the full pipeline from input chat text to injected memories. Extraction uses lightweight LLM calls with minimal token overhead. Consolidation handles 10K memories per user with sub-100ms updates.

Graph memory (Mem0ᵍ) links entities for relational queries. Benchmarks on ECAI and LOCOMO show a 26% LLM-as-Judge gain over OpenAI Memory, 91% latency reduction, and 90% token savings.

Python quickstart:

```python
from mem0 import Memory

m = Memory()
m.add("User likes Python", user_id="u123")
results = m.search(query="language pref", user_id="u123")
```

Mem0 integrates with LangChain, CrewAI, and OpenAI Agents, and scales to 186M API calls quarterly.

## Where Does Long-Term Memory Matter the Most?

Personal assistants maintain routines across time. "Gym Tuesdays, no dairy" persists across 90-day plans without requiring re-entry. Sessions that carry forward prior context build user trust faster than those that start fresh.

Customer support agents shorten resolutions. Recurring "login fail" queries pull "Prior fix: clear cache" directly from episodic memory. Repeat ticket volume drops by 40%.

Coding copilots adapt to team conventions. "Use pytest, not unittest" learned from 20 sessions shapes every subsequent suggestion. Debug history surfaces "Fixed similar OOM March" when relevant.

Over time, agents accumulate working knowledge across sessions, functioning as persistent collaborators rather than session-scoped tools.

_Also read:_ [_Context Engineering Guide for AI Agents_](https://mem0.ai/blog/context-engineering-ai-agents-guide)

## Wrapping Up

For senior developers, long-term memory turns AI agents into stateful systems, not just bigger context windows. It demands pipelines to extract, consolidate, and index conversation signals via vectors, graphs, or hybrids, balancing latency, token costs, and relational fidelity.

Episodic memory anchors interactions, semantic memory stores facts and preferences, and procedural memory tracks behaviors. The result is persistent agents that accumulate knowledge across sessions, reducing token costs, improving retrieval precision, and enabling scalable multi-hop reasoning under production concurrency.

This is the required infrastructure for reliable, efficient, and personalized AI.
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="the-context-window-problem-why-your-ai-conversation-hits-a-w.md">
Phase: [EXPLOITATION]

# The context window problem: why your AI conversation hits a wall

You can feel the moment a good AI conversation starts to go soft.

At first it’s brilliant. You’ve got momentum. The model understands the problem, remembers the decisions, and starts building on what came before.

Then it slips. A constraint from half an hour ago disappears. An idea you already rejected turns up again. The latest answer looks competent enough on the surface, but the thread is starting to fray. Keep pushing and you eventually hit the wall: repetition, drift, odd simplifications, or a reply that makes it obvious the system is no longer carrying the full shape of the task.

People often talk about this as if the model got tired. It didn’t. You ran into the context window wall.

## The wall is structural, not psychological

A large language model doesn’t experience your conversation as a neat, persistent relationship. It works with a bounded working set of tokens: the active context window available for the next step.

The reason it matters is simple: the model isn’t sitting there with a tidy, durable memory of everything you said. It’s working with whatever fits into the current window, plus whatever the product layer chooses to summarise, retrieve, or carry forward on your behalf. Some tools do that better than others. None of them are infinite.

So the failure mode isn’t mysterious. Once a conversation gets long enough, messy enough, or contradictory enough, the model starts making trade-offs. Earlier detail may be truncated. Intermediate reasoning may be compressed. Relevant facts can still be present but given too little weight.

From your side, the conversation still looks continuous. Under the bonnet, the model is operating from an increasingly lossy reconstruction.

## Bigger windows help, but they don’t save you

The obvious reply is that context windows are getting huge. Quite right. They’re getting huge. That still doesn’t remove the problem. It just moves the line.

Anthropic’s engineering guidance describes context as a finite attention budget and argues that good context engineering means finding the smallest possible set of high-signal tokens that gives the model what it needs to succeed ( [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). It’s a useful way to think about it because it kills the lazy assumption that more context is automatically better.

It isn’t. A long, noisy, badly structured conversation can fail inside a large context window just as surely as a shorter one can fail inside a small one. You may not hit a hard token limit, but you can still hit a practical limit where the model stops attending to the right things in the right proportion.

That’s also why long-chat failures often arrive gradually rather than dramatically. You don’t always get a bright red error saying the window is full. More often the quality just decays. People misread that as inconsistency, poor reasoning, or the model having an off day.

Usually it’s context management.

## Why long conversations get weird

There are a few ways this tends to break.

Simple truncation is the most obvious one. Something old falls out of the active working set, and the model starts acting as if it never happened. The database schema you explained in turn three is simply gone by turn forty.

Dilution is subtler. The important instruction is still technically there, but it’s buried under so much other material that it stops dominating the answer. Your real priority hasn’t vanished. It’s just lost the argument inside the prompt.

Conflict is common in any long thread. You accumulate multiple versions of the task, abandoned approaches, half-finished ideas, and corrected mistakes. The model now has to infer which layer represents the current truth.

Position matters too. The paper _Lost in the Middle_ found that model performance can degrade when relevant information sits in the middle of long contexts, even in explicitly long-context systems ( [Liu et al.](https://arxiv.org/abs/2307.03172)). In practice, that means the fact you carefully explained twenty minutes ago may be less available than the thing you just typed.

So a conversation can appear coherent while quietly going stale. You’re still talking about one project. The model is increasingly juggling fragments.

## This is not just a chatbot annoyance

If all you ever do is ask one-off questions, none of this matters very much. The moment you try to do real work with AI — writing, coding, planning, research, analysis, multi-step problem solving — the context window stops being a technical footnote and becomes part of the craft.

You can’t build a serious workflow on the assumption that one chat thread can carry your entire working world forever.

I’ve seen people treat a single conversation as if it were a project database, a memory system, a decision log, and a collaboration layer all at once. It works for a while. Then the task gets bigger, the stakes get higher, and the cracks show.

The output is still fluent, which makes the danger worse. Fluency isn’t the same thing as continuity.

## Why your conversation feels smart at the start

Early in a conversation, the signal-to-noise ratio is usually excellent.

The task is fresh. The instructions are recent. The unresolved choices are clear. The model can hold the whole shape of the interaction in working memory and reason across it cleanly.

This is why people fall in love with long AI sessions. The first stretch often feels magical. You stop re-explaining yourself. The model appears to understand not just the latest prompt but the trajectory of the work. It starts sounding collaborative.

Then success creates its own problem. Because the session is going well, you keep adding more to it: new branches, side questions, examples, corrections, snippets, pasted notes, output you want revised, and explanations of why the previous answer was not quite right. The thread turns into a sedimentary record of the job. Useful, but increasingly heavy.

Eventually the conversation contains too much history to function cleanly as live working memory. At that point you’re no longer using a sharp tool. You’re dragging a growing archive behind you.

## The practical mistake people make

Most people respond in one of two bad ways. They either keep pushing the same chat, hoping the model will somehow hold together, or they throw everything into the next prompt — whole documents, giant transcripts, sprawling notes — and call that context engineering.

Neither approach is very good.

Dumping raw material into a model isn’t the same as giving it usable context. A context window isn’t a loft. You don’t improve the result by stuffing more boxes into it.

The trick is to separate memory from working context.

That means keeping stable information outside the live chat: identity, preferences, active project state, key decisions, relevant source material, and constraints. Then you load the right pieces for the task in front of you.

Stop asking one conversation to do the job of an operating system.

## What to do before you hit the wall

The best fix isn’t heroic prompt-writing. It’s better structure, and a few habits make an immediate difference:

- **Start new chats sooner than feels natural.** If the thread has changed shape, fork it instead of dragging old branches forever.
- **Promote stable facts into files.** Decisions, preferences, briefs, and constraints should live outside the chat — that’s the practical discipline behind [context engineering](https://matthopkins.com/technology/how-to-make-ai-remember-who-you-are-a-practical-guide-to-context-engineering/).
- **Summarise deliberately.** Before moving to a fresh thread, create a short state snapshot covering what you’re doing, what you’ve decided, and what matters next.
- **Load relevant context, not total context.** Give the model the smallest set of material that makes the task solvable.
- **Treat drift as a signal.** When the model starts reintroducing rejected ideas or dropping obvious constraints, stop arguing with it for ten turns and reset the context.

This sounds almost boring.

Good. Most reliable AI practice is boring. The payoff is conversations that stay useful longer, outputs that remain aligned, and far fewer moments where you realise the model is now building on a version of the task that no longer exists.

## Think in terms of working memory

Humans have a similar distinction. There is a difference between what you know in general and what you can actively juggle right now.

That’s the right mental model here. The context window isn’t the AI’s soul. It’s its working surface.

Once you see that, a lot of confusing behaviour stops being confusing. Of course the model loses grip when the active surface gets overloaded. Of course quality improves when the task is reframed cleanly with only the relevant materials in play. Of course persistent files, project instructions, retrieval, and short task briefs outperform one gigantic chat in the long run.

None of this means long conversations are useless. Far from it. They’re excellent for exploration, iteration, and building momentum.

They’re still a poor substitute for structure.

## The takeaway

When an AI conversation hits a wall, the model hasn’t suddenly become stupid. More often, you’ve asked a bounded working-memory system to carry too much history, too many branches, and too much unresolved context at once.

That’s the context window problem.

The practical answer isn’t to become more superstitious about prompts. It’s to become more disciplined about state.

Keep the stable stuff in files. Keep the live task focused. Reset threads before they rot. Summarise as you go. Load context on purpose.

Do that and the wall doesn’t disappear. But it moves far enough away that the conversation stays useful for real work.

And that, in practice, is what most people actually want.
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="the-modal-model-of-memory-what-ai-agents-can-learn-from-cogn.md">
Phase: [EXPLOITATION]

# The Modal Model of Memory: What AI Agents Can Learn From Cognitive Science

In 1968, Richard Atkinson and Richard Shiffrin published a paper called "Human Memory: A Proposed System and Its Control Processes." It described memory not as a single faculty but as a set of distinct stores with different capacities, durations, and operating rules, connected by specific control processes that determined what moved between them.

Cognitive scientists spent the next five decades pressure-testing, refining, and building on that model. What came out the other side is not a textbook diagram. It is a working theory of how biological systems actually manage information at scale: what gets in, what gets kept, how it becomes durable, and why forgetting is not a failure.

The people building AI agent memory systems are, knowingly or not, rediscovering the same answers. The difference is that the cognitive science got there first and has 60 years of experimental data behind it. This article draws the lines between what cognitive research established and what good AI memory architecture requires - with concrete connections to how systems like Mem0 implement these principles in practice.

## **The Modal Model: A Quick Map**

The Atkinson-Shiffrin Modal Model describes three memory stores and the processes that connect them.

The **sensory register** holds raw perceptual input for a fraction of a second - visual information persists for roughly half a second (iconic memory), auditory information for slightly longer (echoic memory). The vast majority of what enters the sensory register decays immediately. Only what receives attention moves forward.

The **short-term store** holds attended information for active processing. Its capacity is limited - George Miller's famous 1956 paper pegged it at seven items (plus or minus two), though later research tightened that estimate. Without active maintenance through rehearsal, information in the short-term store fades within 15 to 30 seconds. Duration and capacity are both constrained.

The **long-term store** is, for practical purposes, unlimited in both capacity and duration. Information enters through encoding from the short-term store. It does not decay in the way short-term memories do, but it can become harder to retrieve through interference from other memories.

What makes this model powerful is not the three-box architecture. It is the control processes - the mechanisms that determine what moves between stores, what gets encoded deeply versus shallowly, and what gets retrieved versus lost.

Those control processes are exactly what most AI memory implementations get wrong.

## **Lesson 1: Attention Is the Real Bottleneck, Not Capacity**

The sensory register can hold an enormous amount of raw input. The limiting factor is not what arrives but what gets attended to. In Broadbent's filter theory and its descendants, attention acts as a selective gate: most input is discarded before it ever reaches short-term storage. What passes through is determined by relevance, salience, and active goals.

The same bottleneck exists in AI systems, and most implementations ignore it entirely.

When developers stuff a full conversation history into an LLM's context window, they are bypassing the attentional filter entirely. Everything arrives at once, at equal weight. The model's attention mechanism has to do the filtering work itself, at inference time, against a background of everything else in the context. This is expensive, it introduces the "lost in the middle" failure mode where relevant information is underweighted based on position, and it does not scale.

Cognitive science suggests a different approach: filter before the model ever sees the input. Surface only what is relevant to the current query and let the model reason over a compact, high-signal context rather than an unfiltered stream.

This is what Mem0 describes as intelligent filtering: not all information is worth remembering, and the system uses priority scoring and contextual relevance to decide what gets stored and what gets surfaced. The attentional gate happens before inference, not during it. Agents stay focused on what matters in the same way humans subconsciously filter noise before it reaches conscious processing.

You can see how this filtering principle maps to the full [AI agent memory architecture](https://mem0.ai/blog/what-is-ai-agent-memory) in practice.

## **Lesson 2: How You Encode Determines How You Retrieve**

In 1972, Fergus Craik and Robert Lockhart published "Levels of Processing: A Framework for Memory Research," one of the most cited papers in cognitive psychology. Their core finding: the depth at which information is processed during encoding directly determines how well it is retained and retrieved.

Shallow processing - noticing surface features like the sound of a word or its physical appearance - produces weak, fast-decaying memory traces. Deep processing - engaging with meaning, relating new information to existing knowledge, processing semantically - produces strong, durable memory traces.

The implication for AI memory is direct. Storing conversation turns verbatim is shallow processing. The raw text sits in a vector store but carries no inherent structure connecting it to meaning. When retrieval time comes, the search is essentially looking for surface-level similarity: which stored tokens look like the current query?

Extracting discrete facts from conversations - "user prefers Python," "user is building for a HIPAA-compliant environment," "user has migrated off AWS" - is deep processing. The information has been transformed from raw exchange into a semantically structured unit. Retrieval does not need to find the right conversation from three weeks ago. It finds the relevant fact directly, regardless of when or how it was expressed.

Mem0's extraction pipeline runs exactly this transformation. Each conversation is processed by an LLM to pull out the meaningful facts - the semantic content - rather than compressing or storing the surface form. The storage is richer, the retrieval is more precise, and the volume of what needs to be stored is dramatically smaller. The [LLM chat history summarization research](https://mem0.ai/blog/llm-chat-history-summarization-guide-2025) covers this distinction in detail: summarization is still shallow processing, just compressed. Memory formation - extracting discrete facts - is the deep processing equivalent.

## **Lesson 3: Interference Explains Why Deduplication Matters**

The dominant theory of forgetting in long-term memory is not decay. It is interference. Two mechanisms are well-established:

**Proactive interference** occurs when older memories make it harder to retrieve newer ones. If a user told your agent last month that they work at Company A, and then told it last week that they moved to Company B, a naive memory store holds both facts. When the agent queries "where does this user work?", the old memory interferes with retrieval of the correct answer.

**Retroactive interference** works in the opposite direction: new information disrupts access to older memories. Storing too many overlapping, slightly different versions of the same fact creates a retrieval environment where the right answer is buried in competing candidates.

Human memory deals with this through consolidation and updating - the same memory trace gets modified rather than a new parallel trace being created. When you learn a friend's new phone number, you do not store it alongside the old one. The old trace gets replaced or suppressed.

This is the cognitive justification for Mem0's four-operation update pipeline: ADD, UPDATE, DELETE, NOOP. Every new memory candidate is compared against what already exists. If a new fact contradicts an old one, the old one is deleted or updated rather than preserved alongside it. The system does not accumulate competing versions of the same knowledge. It maintains a coherent, non-redundant store where the right memory surfaces on the right query.

Without this, any memory system eventually becomes an interference engine - a store full of conflicting facts where correct retrieval degrades as the system grows. The cognitive science predicted this failure mode in 1959. It still shows up in AI memory implementations that treat storage as append-only.

## **Lesson 4: Forgetting Is a Design Feature, Not a Bug**

This one is counterintuitive enough that it is worth stating carefully.

Robert Bjork's research on forgetting, developed over decades into what he calls the "New Theory of Disuse," makes a precise claim: forgetting is not a passive failure. It is an active, adaptive process that serves the memory system by reducing interference and keeping retrieval efficient. Information that is accessed frequently maintains retrieval strength. Information that is not accessed gradually loses retrieval strength - and this is the correct behavior, not a malfunction.

The analogy holds directly for AI memory systems. A memory store that never forgets anything gradually becomes a noise machine. Every preference the user expressed two years ago that no longer applies, every project context that is now stale, every piece of incidental information that was never relevant - it all accumulates and competes with current, useful memories during retrieval.

Mem0 explicitly implements dynamic forgetting: low-relevance entries decay over time, freeing attention and storage for what is current and useful. This is not a storage optimization. It is a retrieval quality decision. A well-maintained memory store where stale information has been pruned returns better results than an unbounded archive where everything is equally present.

Bjork's research also introduced the concept of "desirable difficulties" - the insight that some forgetting is beneficial because it creates the conditions for stronger re-encoding when information is retrieved and updated. Applied to AI: memories that are occasionally reconfirmed and updated become more reliable over time, while memories that are never revisited correctly fade.

The [long-term memory guide](https://mem0.ai/blog/long-term-memory-ai-agents) covers what kinds of information should persist versus decay in production AI systems.

## **Lesson 5: Consolidation Is a Process, Not a Single Event**

In human memory, consolidation is the process by which new, fragile memories become stable long-term storage. Freshly encoded memories are labile - easily disrupted by interference, sleep deprivation, or competing learning. Over time, and particularly during sleep, memory traces are replayed and strengthened, forming connections to existing knowledge and becoming resistant to disruption.

Two things are worth taking from this for AI systems.

First, not everything that enters short-term storage should be promoted to long-term storage immediately. There is a selection process - a decision about what is worth the cost of consolidation. Human memory makes this decision based on emotional salience, relevance to existing knowledge, and frequency of rehearsal. AI memory systems need an equivalent selection mechanism.

Mem0's architecture handles this through its promote pipeline. Information enters conversation memory during the active turn. Relevant details persist to session memory for the duration of a task. Only what is worth keeping long-term gets written to user memory. The three pillars Mem0 identifies - State (what is happening now), Persistence (what survives sessions), and Selection (what is worth remembering) - map directly to the cognitive question that consolidation answers: what deserves to move from temporary to permanent?

Second, consolidation in human memory involves integration with existing knowledge, not just storage in isolation. A new fact about a user does not sit independently - it connects to other facts about that user, updates existing beliefs, creates new associative links. This is exactly the function that graph memory serves. Mem0g stores memories as a directed, labeled graph - entities as nodes, relationships as edges - specifically so that new facts can be integrated into an existing knowledge structure rather than appended as isolated vectors.

The [graph memory approach](https://mem0.ai/blog/graph-memory-solutions-ai-agents) addresses the associative integration that consolidation produces in biological memory: not just storage, but connection.

## **Where Most AI Memory Implementations Miss the Science**

The Modal Model's biggest practical implication is that memory quality is determined by the control processes, not the store itself. You can have an enormous long-term store and terrible memory if your encoding is shallow, your interference is unmanaged, your forgetting is absent, and your consolidation is indiscriminate.

Most AI memory implementations focus almost entirely on the store: which vector database, how many dimensions, what similarity threshold. They treat the pipeline as an afterthought.

But the cognitive science is clear: what matters is the attention gate that decides what enters, the encoding depth that determines how it is stored, the interference management that keeps retrieval clean, the forgetting process that keeps the store healthy, and the consolidation mechanism that decides what persists.

Build those correctly and the retrieval quality follows. Build only the store and you get an archive that gets harder to use as it grows.

## **What the Cognitive Science Actually Demands**

If you take the Modal Model seriously as a design guide, a few requirements fall out clearly for any AI memory system:

Pre-retrieval filtering is not optional. The attentional gate belongs before inference, not inside it.

Encoding must be semantic. Storing raw conversation turns is the equivalent of shallow processing. Extracting discrete facts is deep processing. The retrieval quality difference is substantial.

Interference must be actively managed. Append-only storage degrades. Every memory system needs an equivalent of UPDATE and DELETE.

Forgetting must be intentional. A store that never prunes gradually becomes a source of retrieval noise. Memory decay for low-relevance entries is a feature of well-designed systems, not a limitation to be engineered around.

Consolidation is a selection process. Not everything short-lived deserves to become permanent. The promote decision - what moves from session to user memory - is as important as the storage itself.

Mem0 explicitly names all five of these as core design principles: intelligent filtering, levels-of-processing-style extraction, four-operation interference management, dynamic forgetting, and layered consolidation from conversation to session to user memory. The [research paper](https://mem0.ai/research) demonstrates what this architecture produces: 26% higher accuracy on a standardized long-term memory benchmark, 91% lower retrieval latency, and 90% fewer tokens consumed compared to context-stuffing approaches.

The cognitive science did not predict these specific numbers. But it did predict that a system designed around the right memory processes would substantially outperform one that relied on raw storage capacity alone.

Atkinson and Shiffrin got there in 1968. The AI memory field is catching up.
</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Repository analysis for https://github.com/towardsai/agentic-ai-engineering-course/blob/main/lessons/10_memory_knowledge_access/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/agentic-ai-engineering-course/blob/main/lessons/10_memory_knowledge_access/notebook.ipynb

## Summary
Repository: towardsai/agentic-ai-engineering-course
Commit: 031c7ee248f52b1ee46b33cc835d4fdbffb35bd3
Subpath: /lessons/10_memory_knowledge_access
Files analyzed: 1

Estimated tokens: 2.7k

## File tree
```Directory structure:
└── 10_memory_knowledge_access/
    └── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/10_memory_knowledge_access/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 10: Memory for Agents

This lesson explores the concept of adding **long-term memory** to agents, so they can persist and retrieve information over time. 

We’ll implement semantic, episodic, and procedural memory using the open-source mem0 library with Google's Gemini text embedding model, and a vector store that runs locally in the notebook, using ChromaDB. 


Learning Objectives:

1. Understand the different types of memory 
2. How to implement them, using the mem0 library.
"""

"""
## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:
"""

%load_ext autoreload
%autoreload 2

"""
### Set Up Python Environment

To set up your Python virtual environment using `uv` and use it in the Notebook, follow the step-by-step instructions from the [Course Admin](https://academy.towardsai.net/courses/take/agent-engineering/multimedia/67469688-lesson-1-part-2-course-admin) lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.
"""

"""
### Configure Gemini API

To configure the Gemini API, follow the step-by-step instructions from the [Course Admin](https://academy.towardsai.net/courses/take/agent-engineering/multimedia/67469688-lesson-1-part-2-course-admin) lesson.

But here is a quick check on what you need to run this Notebook:

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  From the root of your project, run: `cp .env.example .env` 
3.  Within the `.env` file, fill in the `GOOGLE_API_KEY` variable:

Now, the code below will load the key from the `.env` file:
"""

from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Environment variables loaded from `/Users/fabio/Desktop/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

import os
import re
from typing import Optional

from google import genai
from mem0 import Memory

"""
### Initialize the Gemini Client
"""

client = genai.Client()

"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast and cost-effective:
"""

MODEL_ID = "gemini-2.5-pro"

"""
### Configure mem0 (Gemini LLM + embeddings + local vector store)

Here we instantiate mem0 with:

- LLM: our existing Gemini model (`MODEL_ID = "gemini-2.5-flash"`) for the summarization/extraction of facts.
- Embeddings: Gemini's `gemini-embedding-001` (output reduced to 768 dimensions).
- Vector store:
    - ChromaDB with `MEM_BACKEND=chromadb` 
"""

MEM0_CONFIG = {
    # Use Google's gemini-embedding-001 for embeddings (output reduced to 768-dim)
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "gemini-embedding-001",
            "embedding_dims": 768,
            "api_key": os.getenv("GOOGLE_API_KEY"),
        },
    },
    # Use ChromaDB as a local, in-notebook vector store
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "lesson9_memories",
            "path": "/tmp/chroma_mem0",
        },
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "model": MODEL_ID,
            "api_key": os.getenv("GOOGLE_API_KEY"),
        },
    },
}

memory = Memory.from_config(MEM0_CONFIG)
MEM_USER_ID = "lesson9_notebook_student"
memory.delete_all(user_id=MEM_USER_ID)
print("✅ Mem0 ready (Gemini embeddings + local Chroma).")
# Output:
#   ✅ Mem0 ready (Gemini embeddings + in-memory Chroma).


"""
### Helper functions: add/search for memories

A small wrapper layer around mem0 to:

- Save a string memory and tag it with a category ("semantic", "episodic", "procedure") plus any extra metadata.
    - `mem_add_text` stores verbatim text with infer=False (no LLM fact extraction triggered by mem0). It also changes and all metadata values to primitives (str | int | float | bool | None) since mem0 requires primitive types.

- Search memories and (optionally) filter by category client-side.
    - `mem_search` calls memory.search(...) and then inspects each hit’s metadata to filter.
"""

def mem_add_text(text: str, category: str = "semantic", **meta) -> str:
    """Add a single text memory. No LLM is used for extraction or summarization."""
    metadata = {"category": category}
    for k, v in meta.items():
        if isinstance(v, (str, int, float, bool)) or v is None:
            metadata[k] = v
        else:
            metadata[k] = str(v)
    memory.add(text, user_id=MEM_USER_ID, metadata=metadata, infer=False)
    return f"Saved {category} memory."


def mem_search(query: str, limit: int = 5, category: Optional[str] = None) -> list[dict]:
    """
    Category-aware search wrapper.
    Returns the full result dicts so we can inspect metadata.
    """
    res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}

    items = res.get("results", [])
    if category is not None:
        items = [r for r in items if (r.get("metadata") or {}).get("category") == category]
    return items

"""
## 2. Semantic memory example (facts as atomic strings)

**Goal**: We show semantic memory as “facts & preferences” stored as short, individual strings.

- We insert a few example facts (e.g., “User has a dog named George”).

- Then we search with a natural query (e.g., “brother job”) and see the relevant fact returned.
"""

facts: list[str] = [
    "User prefers vegetarian meals.",
    "User has a dog named George.",
    "User is allergic to gluten.",
    "User's brother is named Mark and is a software engineer.",
]
for f in facts:
    print(mem_add_text(f, category="semantic"))

print(f"Added {len(facts)} semantic memories.")
# Output:
#   Saved semantic memory.

#   Saved semantic memory.

#   Saved semantic memory.

#   Saved semantic memory.

#   Added 4 semantic memories.


# Search for a specific fact
results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
# We print the memory string
print(results["results"][0]["memory"])
# We print the whole dict that contains the memory
print(results["results"][0])
# Output:
#   User's brother is named Mark and is a software engineer.

#   {'id': '68fa87b4-5cad-41c0-b06d-143e92ba7c66', 'memory': "User's brother is named Mark and is a software engineer.", 'hash': '9a01dbd8ea8b96f8ed9c84e9dcdb55a1', 'metadata': {'category': 'semantic'}, 'score': 0.9269160032272339, 'created_at': '2025-09-12T02:29:53.515480-07:00', 'updated_at': None, 'user_id': 'lesson9_notebook_student', 'role': 'user'}


"""
## 3. Episodic memory example (summarize 3–4 turns → one episode)

**Goal**: Demonstrate episodic memory (experiences & history).

- We create a short 3–4 turn exchange between user and assistant.

- We ask the LLM to produce a concise episode summary (1–2 sentences) and save it under category="episodic".

- Finally, we run a semantic search (e.g., “deadline stress”) to retrieve that episode, we print the memory along with its creation timestamp.

This example show how an agent can compress transient chat into a single durable “moment.”

Since mem0 by default creates a created_at timestamp, we have the possibility to use it to sort and filter memories.
It would then be possible to answer questions like "What did we talk about last week?"
"""

# A short 4-turn exchange we want to compress into one "episode"
dialogue = [
    {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
    {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
    {"role": "user", "content": "Mainly testing. I also prefer working at night."},
    {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
]

# Ask the LLM to write a clear episodic summary.
episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
Keep salient details and tone.

{dialogue}
"""
episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
episode = episode_summary.text.strip()
print(episode)
# Output:
#   A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.


print(
    mem_add_text(
        episode,
        category="episodic",
        summarized=True,
        turns=4,
    )
)

print("\nSearch --> 'deadline stress'\n")
hits = mem_search("deadline stress", limit=1, category="episodic")
for h in hits:
    print(f"{h['memory']}\n")
    print(h)
# Output:
#   Saved episodic memory.

#   

#   Search --> 'deadline stress'

#   

#   A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.

#   

#   {'id': '93ebb9eb-65b0-4975-9c0d-105497b43e5c', 'memory': 'A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.', 'hash': '44f0bcd0965a1fb557c1d3b5a9f8ae6c', 'metadata': {'turns': 4, 'summarized': True, 'category': 'episodic'}, 'score': 0.9109697937965393, 'created_at': '2025-09-12T02:30:01.358468-07:00', 'updated_at': None, 'user_id': 'lesson9_notebook_student', 'role': 'user'}


"""
## 4. Procedural memory example (learn & “run” a skill)

**Goal**: Demonstrate procedural memory (skills & workflows).

- We teach the agent a small procedure (e.g., monthly_report) by saving ordered steps in a single text block under category="procedure".

- We retrieve the procedure and parse the numbered steps to simulate “running” it.

This example shows how agents can learn reusable playbooks and trigger them later by name.
"""

procedure_name = "monthly_report"
steps = [
    "Query sales DB for the last 30 days.",
    "Summarize top 5 insights.",
    "Ask user whether to email or display.",
]
procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))

mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)

print(f"Learned procedure: {procedure_name}")
# Output:
#   Learned procedure: monthly_report


# Retrieve the procedure by name
results = mem_search("how to create a monthly report", category="procedure", limit=1)
if results:
    print(results[0]["memory"])
# Output:
#   Procedure: monthly_report

#   Steps:

#   1. Query sales DB for the last 30 days.

#   2. Summarize top 5 insights.

#   3. Ask user whether to email or display.

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

<details>
<summary>[00:00] (The video opens with a montage of people attending an event, showing different individuals interacting, listening to speakers, and networking. There are banners in the background with "LangGraph" and "LangSmith" logos.)</summary>

[00:00] (The video opens with a montage of people attending an event, showing different individuals interacting, listening to speakers, and networking. There are banners in the background with "LangGraph" and "LangSmith" logos.)

[00:09] (A title card appears: "AI Memory SAN FRANCISCO JUNE 18, 2025 - BUILDING AI TO REMEMBER" alongside a photo of Sam Whitmore, labeled "SAM WHITMORE FOUNDER @ NEW COMPUTER")
Thank you, Nicole, and thank you, um, Harrison and LangChain, and Greg for organizing and hosting. Actually, one of the first things I did with Memory was with Harrison on the original memory implementation in LangChain, so very full circle.
[00:30] Um, cool. So for those of you who do not know New Computer and what we do, we have Dot, which is a conversational journal, it's in the App Store, you can use it now. (The title card changes to "From Dot to Dots - Evolution of Memory at New Computer - Sam Whitmore, CEO". A small video feed of Sam Whitmore giving the presentation is in the bottom right corner.) We launched this last year.
(The slide changes to "2023") So we've been working on memory in AI applications since 2023.

[00:41] Um, cool. So, take us back to 2023. (The slide changes to show text describing GPT-4's specifications in 2023: "GPT-4 was state of the art - 8192 token context length - 196ms per generated token - $30.00 / 1 million prompt tokens - $60.00 / 1 million sampled tokens") The time GPT-4 was state of the art. We have 8,000 one length token, uh, prompt, very slow and very expensive. So I wanna walk you through some of the things that we tried initially, lessons we learned along the way, and how we kind of evolve as underlying technology evolves.
[01:11] (The slide changes to show a mobile phone screen displaying a chat conversation.) So, when we started, our general goal was to build a personal AI that got to know you. It was pretty unstructured. Um, and so we knew that if it was going to learn about you as you used it, it needed memory.
(The slide changes to text: "What is the perfect memory architecture?") So we're like, okay, let's just build the first, build the perfect memory architecture and then the product after that.
[01:31] (The slide changes to text: "Memory == Facts...?"). Um, so we started out being like, okay, maybe we can just extract facts as a user talks to Dot, and search across them, you know, use some different techniques, and we'll have great memory performance. (The slide changes to show a user's text message: "I have a dog! His name is Poppy. Walking him is the best part of my day". Below it, the extracted facts are listed: "User has a dog. User's dog is named Poppy. User likes taking his dog for walks.") So we learned pretty quickly that this wasn't really gonna work for us. So, imagine a user saying, "I have a dog. His name is Poppy. Walking him is the best part of my day." So early extraction, we'd get things like, "User has dog. User's dog is named Poppy. User likes taking Poppy for walks." There's a lot of nuance missing. So, like, you can tell a lot about a person from reading that sentence that you can't tell from those facts.
[02:07] (The slide changes to text: "Memory != Facts") That was a pretty quick realization for us. (The slide changes to text: "Memory == Schemas?") We then moved on. So, we were like, maybe if we try to summarize everything about Poppy in one place, then it's going to perform better. (An animated sequence plays on the mobile phone screen, showing a brief chat, then the app transitions to a structured view of "Recipes" with various dish images and descriptions.) We decided that we were going to make this universal memory architecture with entities and schemas that were linked to each other. This was a UI representation of it. Um, so users could actually browse the things that were created, um, and they had different types, and on the back-end there were different form factors with JSON blobs.
[02:40] (The mobile phone screen shows a chat with a user mentioning a friend's bachelorette party, followed by several AI-generated structured memory entries like "Created event for Meredith's Bachelorette", "Added Meredith as a friend of Zack's", and "Added the Airbnb location for Meredith's bachelorette party".) This is a real example from our product at the time. So, I sent it a bachelorette flyer, and it made like a whole bunch of different memory types with schemas associated. Um, so you can see here that like, this is what the back-end data looked like. There's different fields.
[03:00] (The screen shows structured details for the created event, friend, and Airbnb location, including name, dates, location, description, and relationships.) And we had a router architecture that would kind of generate queries that would search across all of these, um, in parallel. And what we found was that it worked okay, but there was kind of some base functionality that was still missing.
[03:22] Um, oh, this was a funny example. (The screen changes to a tweet from "Jason 'Mars' Yuan" that reads "not dot calling me out w its dynamic memory schemas". Below is a list of categories with counts: "Routines 8", "Ice Cream Flavors 1", "Drunk Texts 2", "Webpages 29".) Um, Jason, my co-founder, was sending it, uh, pictures and it made him a Drunk Text category as a schema, which we were like, that feels like a heavy read. Um, but anyway, so the schemas were kind of fun.
[03:32] (The slide changes to text: "Funny & cool to see, but didn't work that well in practice as a single system". Below, two mobile app screenshots are shown. The left one displays "memories" like "Bouldering with Luca" (Activity), "Clara" (Person), "Ask Clara about bouldering" (Reminder), "Poetry slam event" (Event). The right one shows a chat with "Brandon" that includes a restaurant reservation.) Um, but yes, so basically, we also saw that when we exposed this to users, it was like too much cognitive overhead for them to garden their their database. Like there was a lot of overlapping concepts, and people got stressed by actually just monitoring their memory base.
[03:50] (The slide changes to text: "Learning: The perfect memory architecture doesn't exist") So, again, we were like, okay, let's just go back to basics here and figure out like what do we want our product to be doing, and let's re-examine how we want to build memory from that. (The slide changes to text: "The architecture of memory depends entirely on the goals of the product")
[04:00] (The slide changes back to the mobile phone chat screen with the text: "What would a thought partner need to learn about you to do a good job?") So, we looked again at like what a thought partner should have to do to actually be really good as a listener for you. (The slide changes to a numbered list: "1. It needs to know my general bio & core values 2. It needs to know the things that happen in my life and also when they happened 3. It needs to know about the people, places, and the various nouns important to me 4. It needs to know the best way to work with me") So, we realized like, it should always know who you are and your core values. It should know basically like, you know, what you talked about yesterday, what you talked about last week. And again, like who Poppy is if Poppy is your dog, who your co-founder is, stuff like that. And it also needs to know about like your behavior preferences and how it should adapt to you as you use it.
[04:30] (The numbered list on the slide fades into the background, and four categories appear in the foreground: "Holistic theory of mind", "Episodic memory", "Entities", "Procedural memory".) So, we ended up making four kind of parallel memory systems. So the schemas that you saw didn't really go away, they just became one of the memory systems, the entities. And it's funny seeing Will kind of say some of the same ones. So it's like an example of convergent evolution because we kind of made these up ourselves.
[04:50] (The slide changes to "Holistic Theory of Mind" with a bulleted list of personal details including family, career, interests, and current focus.) But basically like, Holistic Theory of Mind. Here's mine. It's kind of just like, who am I, what's important to me, what am I working on, what's top of mind for me right now. (The slide changes to "Episodic Memory" with a dated entry: "October 18, 2024. 2:15PM PT Samantha expressed love for her newborn son, Alexander, sharing the joys and challenges of early motherhood, including sleepless nights and feeding difficulties. Dot provided supportive feedback, highlighting the significance of Samantha's small discoveries as a new mother, such as recognizing when Alexander was cold. After a pediatrician appointment, Samantha reported that Alexander had passed his birth weight, marking a positive milestone in his early development.") Episodic Memory is kind of like what happened on a specific day. Here's kind of like an actual real example soon after I had my baby last year.
[05:20] (The slide changes to "Entities" with a paragraph describing "Alexander", her newborn son, and her experiences as a new mother.) Um, here's like another entity example. We ended up stripping away a lot of the JSON because it turned out to actually not improve performance in retrieval across the entity schema. So, we kept things like the categories if we wanted to do tag filtering, but, um, a lot of the extra structure just ended up being like way too much overhead for the model to output.
[05:40] (The slide changes to "Procedural Memory" showing Python code. The code defines a `ReflectionQuestionIntent` class with `description` and `instructions` methods. The description mentions sensing hidden emotions and the instructions outline how to share insights or ask probing questions.) And finally, we made this thing called Procedural Memory, um, which is basically like triggered by, uh, conversational and situational similarity. So what you're looking at here is this intent, and if you're a Dot user, you'll probably recognize this behavior. It says, "Choose this if you have sensed a hidden or implied emotion or motivation that the user is not expressing in their language, and see a chance to share an insight or probe the user deeper on this matter." And then, when it detects that this is happening, it says like, "share an insight, you know, ask a question, issue a statement that encourages the behavior."
[06:17] (The speaker gestures towards the slide.) And so, basically like, the trigger here is not semantic similarity but situational similarity. I see a lot of overlap here for people building agents where if you have a workflow that the agent needs to perform, it can identify that it, that, encountered that situation before, and kind of pull up some learning it had from the past running of the workflow.
[06:36] (The slide changes to a complex flowchart titled "Retrieval pipeline 2024". It shows a "User Query" at the top, leading to an "Entry Router", then parallel "Perceivers" and "Search Modules" for different memory types, eventually converging to "Generate Response".) So this is kind of our way our retrieval pipeline worked in 2024, which is like parallelize retrieval across all of these systems. So, if here's a query which is very hard to read, so maybe these slides will be accessible separately. Um, "what restaurant should I take my brother to for his birthday?" And in this sense, in each of our four systems, we detect if a query is necessary across the system. For holistic stuff, we always load the, load the whole theory of mind. Episodic is only triggered if it's like, "what did we talk about last week?" or "what did we talk about yesterday?"
[07:05] (The speaker points to different parts of the flowchart.) And then here, there's two like different types of entity queries detected, like brother and restaurants. And then we would do kind of a hybrid search thing where like, we mixed together BM25, semantic, keyword, basically like no attachment to any particular approach, just like whatever improved recall for specific entities. Um, and then the procedural memory, here if there's a behavioral module loading like restaurant selection or planning, then that would get loaded into the final prompt. So, funny thing also is when we launched, people tried to prompt inject us, but because we have so many different behavioral modules and different things going on, we called it like Frankenprompt. And like, if people did prompt inject us, they'd be like, "Wait, I think this prompt changes every time," which it did.
[07:46] (The slide changes to text: "The formation of these memories are distinct per system") Um, okay.
(The slide changes to a list of the four memory types with their formation rules: "Holistic theory of mind: Updated once a day - Episodic memory: Periodic summarization, multiple levels of precision - Entities: Per line of conversation (with dream sequences for consolidation) - Procedural memory: Per line of conversation") So for the formation for these, again, really distinct per system. So, Holistic Theory of Mind, you don't need to update that frequently. Episodic is like periodic summarization. So like, if you wanna have it be per week, you might update across daily summaries once per week, per day, once per day, et cetera. Entities, we did per line of conversation. And then we would run kind of cron jobs that we called dream sequences, where they'd identify possible duplicates and potentially merge them. And Procedural Memory also updated per line of conversation.
[08:24] (The slide shows a stylized yin-yang like logo of New Computer.) So, um, along the past year, our product trajectory has changed. We're now building Dots, which is a Hivemind.
[08:35] (The slide changes to text: "Hivemind") So it's like, instead of remembering just one person that it meets, it actually remembers, um, an entire group of people.
[08:48] (The slide shows a cluster of interconnected bubbles, representing a "Hivemind". Some bubbles are highlighted and contain text like "Jason introduces and validates the design leadership of", "Ian admires artistic approach to", "Hang sees as project in computational art @ Cat", "Sean plans strategic discussions with", "a institutional leadership approach of".) And yeah, so you, basically, some of the added challenges we're dealing with now are representing, um, different people's opinion of each other, how they're connected, and how information should flow between them. In addition to understanding all of the systems I just mentioned above.
[09:04] (The slide changes to text: "June, 2025") So, one other thing I'll share that has evolved in terms of how, like, the world has changed a lot since 2023.
[09:15] (The slide changes to show text about Gemini Flash 2.5: "Gemini flash 2.5 - Maximum input tokens: 1,048,576 - Maximum output tokens: 65,535 - $0.30 / 1 million input - $2.50 / 1 million output") So, we keep re-evaluating how we should be building things constantly. And now we have a million token input context window. We have prompts that are really cheap, and they're also really, really fast. So, some of the things that we held true in terms of compressing knowledge and context, we no longer hold true.
[09:37] (The slide changes to "Retrieval pipeline 2024" flowchart, then transitions to "Retrieval pipeline 2025" which is a simpler flowchart. It removes the episodic and entity-level processing and focuses more on direct use of raw context and real-time Q&A.) Here's an example. So, if you look back at this pipeline I shared before, um, here's an updated version that we're experimenting with now, which is getting rid of episodic and entity level compression in favor of real-time Q&A. So, that means that like, depending on your system, maybe you don't need to be compressing context at all. Because again, like I said at the beginning, the raw data is always the best source of truth. So, it's like, why would you create a secondary artifact as a stepping point between you and what the user's asking? Ideally, you just want to examine the context. And so we do that pretty frequently depending on how much data we're dealing with. We try basically not to do, to do the minimal amount of engineering possible.
[10:25] (The slide changes to text: "Design for where the technology is heading") And our theory kind of going forward is like, this trend will only continue. So, we think the procedural memory and, like, basically the insights, the interpretation and analysis that the thing does, is the important part of memory. It's like the record of its thoughts about you, and kind of its notes to itself is the important part. You can almost separate that from retrieval as a problem. You can say like, okay, maybe there'll be an infinite log of like my interactions, and model notes will be interpolated in the in the future. And so maybe we don't even have to deal with retrieval and context compression at all.
[11:03] (The slide changes to text: "The perfect memory architecture doesn't exist - Know what function memory serves in your product, & think from first principles about how to make it work...constantly!") So, I guess if I want you guys to take away one thing, it's like, the perfect memory architecture doesn't exist. And start with kind of what your product is supposed to do and then think from first principles about how to make it work, and do that all the time, because the world is changing and you might not need to invest that much in memory infrastructure.
[11:23] (The slide changes to text: "Sam Whitmore, CEO @sjwhitmore - New Computer @newcomputer") That's it. So, you can follow us at Twitter, New Computer. Thank you.
(Applause. The video ends with the initial title card.)

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>cognitive-architectures-for-language-agents</summary>

# Cognitive Architectures for Language Agents

## 1 Introduction

Language agents are an emerging class of artifical intelligence (AI) systems that use large language models (LLMs) to interact with the world. They apply the latest advances in LLMs to the existing field of agent design. Intriguingly, this synthesis offers benefits for both fields. On one hand, LLMs possess limited knowledge and reasoning capabilities. Language agents mitigate these issues by connecting LLMs to internal memory and environments, grounding them to existing knowledge or external observations. On the other hand, traditional agents often require handcrafted rules or reinforcement learning, making generalization to new environments challenging. Language agents leverage commonsense priors present in LLMs to adapt to novel tasks, reducing the dependence on human annotation or trial-and-error learning.

While the earliest agents used LLMs to directly select or generate actions, more recent agents additionally use them to reason, plan, and manage long-term memory to improve decision-making. This latest generation of _cognitive_ language agents use remarkably sophisticated internal processes. Today, however, individual works use custom terminology to describe these processes (such as ‘tool use’, ‘grounding’, ‘actions’), making it difficult to compare different agents, understand how they are evolving over time, or build new agents with clean and consistent abstractions.

In order to establish a conceptual framework organizing these efforts, we draw parallels with two ideas from the history of computing and artificial intelligence (AI): production systems and cognitive architectures. Production systems generate a set of outcomes by iteratively applying rules. They originated as string manipulation systems – an analog of the problem that LLMs solve – and were subsequently adopted by the AI community to define systems capable of complex, hierarchically structured behaviors. To do so, they were incorporated into cognitive architectures that specified control flow for selecting, applying, and even generating new productions.

Thus, we propose Cognitive Architectures for Language Agents (CoALA), a conceptual framework to characterize and design general purpose language agents. CoALA organizes agents along three key dimensions: their information storage (divided into working and long-term memories); their action space (divided into internal and external actions); and their decision-making procedure (which is structured as an interactive loop with planning and execution). Through these three concepts (memory, action, and decision-making), we show CoALA can neatly express a large body of existing agents and identify underexplored directions to develop new ones.

## 2 Background: From Strings to Symbolic AGI

### 2.3 Cognitive architectures: From algorithms to agents

Production systems were popularized in the AI community by Allen Newell, who was looking for a formalism to capture human problem solving. Productions were generalized beyond string rewriting to logical operations: _preconditions_ that could be checked against the agent’s goals and world state, and _actions_ that should be taken if the preconditions were satisfied.

Following this work, production systems were adopted by the AI community. The resulting agents contained large production systems connected to external sensors, actuators, and knowledge bases – requiring correspondingly sophisticated control flow. AI researchers defined “cognitive architectures” that mimicked human cognition – explicitly instantiating processes such as perception, memory, and planning to achieve flexible, rational, real-time behaviors. This led to applications from psychological modeling to robotics, with hundreds of architectures and thousands of publications.

A canonical example is the Soar architecture. Soar stores productions in long-term memory and executes them based on how well their preconditions match working memory. These productions specify actions that modify the contents of working and long-term memory.

Memory. Building on psychological theories, Soar uses several types of memory to track the agent’s state. _Working memory_ reflects the agent’s current circumstances: it stores the agent’s recent perceptual input, goals, and results from intermediate, internal reasoning. _Long term memory_ is divided into three distinct types. _Procedural_ memory stores the production system itself: the set of rules that can be applied to working memory to determine the agent’s behavior. _Semantic_ memory stores facts about the world, while _episodic_ memory stores sequences of the agent’s past behaviors.

Grounding. Soar can be instantiated in simulations or real-world robotic systems. In embodied contexts, a variety of sensors stream perceptual input into working memory, where it is available for decision-making. Soar agents can also be equipped with actuators, allowing for physical actions and interactive learning via language.

Decision making. Soar implements a decision loop that evaluates productions and applies the one that matches best. Productions are stored in long-term procedural memory. During each decision cycle, their preconditions are checked against the agent’s working memory. In the _proposal and evaluation_ phase, a set of productions is used to generate and rank a candidate set of possible actions. The best action is then chosen. Another set of productions is then used to implement the action – for example, modifying the contents of working memory or issuing a motor command.

Learning. Soar supports multiple modes of learning. First, new information can be stored directly in long-term memory: facts can be written to semantic memory, while experiences can be written to episodic memory. This information can later be retrieved back into working memory when needed for decision-making. Second, behaviors can be modified. Reinforcement learning can be used to up-weight productions that have yielded good outcomes, allowing the agent to learn from experience. Most remarkably, Soar is also capable of writing new productions into its procedural memory – effectively updating its source code.

Cognitive architectures were used broadly across psychology and computer science, with applications including robotics, military simulations, and intelligent tutoring. Yet they have become less popular in the AI community over the last few decades. This decrease in popularity reflects two of the challenges involved in such systems: they are limited to domains that can be described by logical predicates and require many pre-specified rules to function.

Intriguingly, LLMs appear well-posed to meet these challenges. First, they operate over arbitrary text, making them more flexible than logic-based systems. Second, rather than requiring the user to specify productions, they learn a distribution over productions via pre-training on an internet corpus. Recognizing this, researchers have begun to use LLMs within cognitive architectures, leveraging their implicit world knowledge to augment traditional symbolic approaches. Here, we instead import principles from cognitive architecture to guide the design of LLM-based agents.

## 4 Cognitive Architectures for Language Agents (CoALA): A Conceptual Framework

We present Cognitive Architectures for Language Agents (CoALA) as a framework to organize existing language agents and guide the development of new ones. CoALA positions the LLM as the core component of a larger cognitive architecture. Under CoALA, a language agent stores information in memory modules, and acts in an action space structured into external and internal parts:

- External actions interact with external environments (e.g., control a robot, communicate with a human, navigate a website) through grounding.

- Internal actions interact with internal memories. Depending on which memory gets accessed and whether the access is read or write, internal actions can be further decomposed into three kinds: retrieval (read from long-term memory), reasoning (update the short-term working memory with LLM), and learning (write to long-term memory).

Language agents choose actions via decision-making, which follows a repeated cycle. In each cycle, the agent can use reasoning and retrieval actions to plan. This planning subprocess selects a grounding or learning action, which is executed to affect the outside world or the agent’s long-term memory. CoALA’s decision cycle is analogous to a program’s “main” _procedure_ that runs in loops continuously, accepting new perceptual input and calling various action _procedures_ in response.

CoALA is inspired by the decades of research in cognitive architectures, leveraging key concepts such as memory, grounding, learning, and decision-making. Yet the incorporation of an LLM leads to the addition of “reasoning” actions, which can flexibly produce new knowledge and heuristics for various purposes – replacing hand-written rules in traditional cognitive architectures. It also makes text the _de facto_ internal representation, streamlining agents’ memory modules.

### 4.1 Memory

Language models are _stateless_: they do not persist information across calls. In contrast, language agents may store and maintain information internally for multi-step interaction with the world. Under the CoALA framework, language agents explicitly organize information (mainly textural, but other modalities also allowed) into multiple memory modules, each containing a different form of information. These include short-term working memory and several long-term memories: episodic, semantic, and procedural.

Working memory. Working memory maintains active and readily available information as symbolic variables for the current decision cycle. This includes perceptual inputs, active knowledge (generated by reasoning or retrieved from long-term memory), and other core information carried over from the previous decision cycle (e.g., agent’s active goals). Previous methods encourage the LLM to generate intermediate reasoning, using the LLM’s own context as a form of working memory. CoALA’s notion of working memory is more general: it is a data structure that persists across LLM calls. On each LLM call, the LLM input is synthesized from a subset of working memory (e.g., a prompt template and relevant variables). The LLM output is then parsed back into other variables (e.g., an action name and arguments) which are stored back in working memory and used to execute the corresponding action. Besides the LLM, the working memory also interacts with long-term memories and grounding interfaces. It thus serves as the central hub connecting different components of a language agent.

Episodic memory. Episodic memory stores experience from earlier decision cycles. This can consist of training input-output pairs, history event flows, game trajectories from previous episodes, or other representations of the agent’s experiences. During the planning stage of a decision cycle, these episodes may be retrieved into working memory to support reasoning. An agent can also write new experiences from working to episodic memory as a form of learning.

Semantic memory. Semantic memory stores an agent’s knowledge about the world and itself. Traditional NLP or RL approaches that leverage retrieval for reasoning or decision-making initialize semantic memory from an external database for knowledge support. For example, retrieval-augmented methods in NLP can be viewed as retrieving from a semantic memory of unstructured text (e.g., Wikipedia). In RL, “reading to learn” approaches leverage game manuals and facts as a semantic memory to affect the policy. While these examples essentially employ a fixed, read-only semantic memory, language agents may also write new knowledge obtained from LLM reasoning into semantic memory as a form of learning to incrementally build up world knowledge from experience.

Procedural memory. Language agents contain two forms of procedural memory: _implicit_ knowledge stored in the LLM weights, and _explicit_ knowledge written in the agent’s code. The agent’s code can be further divided into two types: procedures that implement actions (reasoning, retrieval, grounding, and learning procedures), and procedures that implement decision-making itself. During a decision cycle, the LLM can be accessed via reasoning actions, and various code-based procedures can be retrieved and executed. Unlike episodic or semantic memory that may be initially empty or even absent, procedural memory must be initialized by the designer with proper code to bootstrap the agent. Finally, while learning new actions by writing to procedural memory is possible, it is significantly riskier than writing to episodic or semantic memory, as it can easily introduce bugs or allow an agent to subvert its designers’ intentions.

## 5 Case Studies

With variations and ablations of the memory modules, action space, and decision-making procedures, CoALA can express a wide spectrum of language agents. Table 2 lists some popular recent methods across diverse domains — from Minecraft to robotics, from pure reasoning to social simulacra. CoALA helps characterize their internal mechanisms and reveal their similarities and differences in a simple and structured way.

|  | Long-term Memory | External Grounding | Internal Actions | Decision Making |
| --- | --- | --- | --- | --- |
| SayCan | - | physical | - | evaluate |
| ReAct | - | digital | reason | propose |
| Voyager | procedural | digital | reason/retrieve/learn | propose |
| Generative Agents | episodic/semantic | digital/agent | reason/retrieve/learn | propose |
| Tree of Thoughts | - | digital | reason | propose, evaluate, select |

SayCan grounds a language model to robotic interactions in a kitchen to satisfy user commands. Its long-term memory is procedural only (an LLM and a learned value function). The action space is external only – a fixed set of grounding skills, with no internal actions of reasoning, retrieval, or learning.

ReAct is a language agent grounded to various digital environments. Like SayCan, it lacks semantic or episodic memory and therefore has no retrieval or learning actions. Its action space consists of (internal) reasoning and (external) grounding.

Voyager is a language agent grounded to the Minecraft API. It has a long-term procedural memory that stores a library of code-based grounding procedures a.k.a. skills. This library is hierarchical: complex skills can use simpler skills as sub-procedures. Most impressively, its action space has all four kinds of actions: grounding, reasoning, retrieval, and learning (by adding new grounding procedures).

Generative Agents are language agents grounded to a sandbox game affording interaction with the environment and other agents. Its action space also has all four kinds of actions: grounding, reasoning, retrieval, and learning. Each agent has a long-term episodic memory that stores events in a list. These agents use retrieval and reasoning to generate reflections on their episodic memory which are then written to long-term semantic memory.

</details>

<details>
<summary>giving-your-ai-a-mind-exploring-memory-frameworks-for-agenti</summary>

# Giving Your AI a Mind: Exploring Memory Frameworks for Agentic Language Models

Langhain Memory for agents

Hey everyone, Richardson Gunde here! Ever feel like you’re having a conversation with a goldfish? You tell it something, it seems to listen… then, poof! It forgets everything the second you finish speaking. That’s often the experience with many chatbots — they lack the crucial ingredient of _memory_. But what if we could give our AI assistants a proper memory, a real mind to hold onto information and learn from past experiences? That’s what we’re diving into today.

This isn’t just about remembering the last few messages; it’s about building truly _agentic_ systems — AI that can learn, adapt, and even anticipate your needs. We’re going to explore different memory frameworks inspired by human cognition, and I’ll show you how to implement them using LangChain and other tools. Get ready for an “Aha!” moment or two — this is where the magic happens.

**The Stateless Nature of Language Models:** _A Fundamental Limitation_

Think about how a language model works. Every time you send a prompt, it’s essentially a brand new start. It’s stateless; it doesn’t inherently remember anything from previous interactions unless you explicitly feed it that context. This is a huge limitation when building agents that need to handle complex tasks or ongoing conversations.

Agent Memory — Can LLMs Really Think?

Now, contrast that with how _you_ approach problem-solving. You bring a wealth of knowledge — your general knowledge of the world, memories of past experiences, lessons learned from successes and failures. This allows you to instantly contextualize a situation and adapt your approach accordingly. We, as humans, have something language models currently lack: advanced memory and the ability to learn and apply those learnings to new situations.

**Bridging the Gap:** _Modeling Human Memory in AI_

To overcome this limitation, we can borrow concepts from psychology and model different forms of memory within our agentic system design. We’ll focus on four key types:

1. **Working Memory:** This is your immediate cognitive workspace, the “RAM” of your mind. For a chatbot, it’s the current conversation and its context. Think of it as the short-term memory of the interaction, keeping track of the back-and-forth between user and AI. Remembering in this context is simply accessing this recent data, while learning involves dynamically integrating new messages to update the overall conversational state.

**2 . Episodic Memory:** This is your long-term memory for specific events. For a chatbot, it’s a collection of past conversations and the takeaways from them. Remembering here involves recalling similar past events and their outcomes to guide current interactions. Learning involves storing complete conversations and analyzing them to extract key insights — what worked, what didn’t, and what to avoid in the future. This is where the AI starts to truly learn from experience.

**3\. Semantic Memory:** This represents your structured knowledge of facts, concepts, and their relationships — the “what you know”. For our agent, this will be a database of factual knowledge that’s dynamically retrieved to ground responses. Learning involves expanding or refining this knowledge base, while remembering involves retrieving and synthesizing relevant information to provide accurate and contextually appropriate answers.

**4\. Procedural Memory:** This is the “how to” memory, encompassing the skills and routines you’ve learned. For a language model, this is trickier. It’s partially represented in the model’s weights, but also in the code that orchestrates the memory interactions. Learning here could involve fine-tuning the model or updating the system’s code, which can be complex. We’ll explore a simplified approach using persistent instructions that guide the agent’s behavior.

**Implementing the Memory Frameworks:** _A Practical Example_

Let’s get our hands dirty! We’ll use LangChain to build a retrieval-augmented generation agent that models these four memory types.

**1\. Working Memory: The Immediate Context**

_The simplest to implement is working memory. We’ll use a list to store the conversation history. Each new message is added to the list, and the entire list is fed back into the language model for generation. This ensures the model has the immediate context of the conversation._

```
# Language Model
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0.7, model="gpt-4o")
```

```
# Create Simple Back & Forth Chat Flow
from langchain_core.messages import HumanMessage, SystemMessage

# Define System Prompt
system_prompt = SystemMessage("You are a helpful AI Assistant. Answer the User's queries succinctly in one sentence.")

# Start Storage for Historical Message History
messages = [system_prompt]

while True:

    # Get User's Message
    user_message = HumanMessage(input("\nUser: "))

    if user_message.content.lower() == "exit":
        break

    else:
        # Extend Messages List With User Message
        messages.append(user_message)

    # Pass Entire Message Sequence to LLM to Generate Response
    response = llm.invoke(messages)

    print("\nAI Message: ", response.content)

    # Add AI's Response to Message List
    messages.append(response)
```

```
AI Message:  Hello! How can I assist you today?
AI Message:  I'm sorry, but I don't have access to personal information, so I don't know your name.
AI Message:  Nice to meet you, Richard! How can I help you today?
AI Message:  Your name is Richard.
```

```
# Looking into our Memory [Keeping track of our total conversation allows the LLM to use prior messages and interactions as context for immediate responses during an ongoing conversation, keeping our current interaction in working memory and recalling working memory through attaching it as context for subsequent response generations.]

for i in range(len(messages)):
    print(f"\nMessage {i+1}

</details>

<details>
<summary>introduction-to-stateful-agents-letta-docs</summary>

# Introduction to Stateful Agents

Stateful agents are agents that can maintain memory and context across conversations.

When an LLM agent interacts with the world, it accumulates state - learned behaviors, facts about its environment, and memories of past interactions.
A stateful agent is one that can effectively manage this growing knowledge, maintaining consistent behavior while incorporating new experiences.

Letta provides the foundation for building stateful agents through its context management system.
In Letta, all state, includes memories, user messages, reasoning, tool calls, are all persisted in a database, so they are never lost, even once evicted from the context window.
Important “core” memories are injected into the context window of the LLM, and the agent can modify its own memories through tools.

## Core API concepts

The Letta API is designed around a few high-level concepts:

### Agents

A stateful agent comprises of a system prompt, memory blocks, messages (in-context and out-of-context), and tools.

### Tools

Tools contain JSON schema (passed to the LLM), which include a tool name, description, and keyword arguments. **Server-side tools** contain code (executed by the server in a sandbox), vs **MCP tools** and **client-side tools** only contain the schema (since the tool is executed externally from the agent server).

### Memory

Memory (organized into blocks) are pieces of context (strings) that are editable by agents via memory tools (and directly by the developer via the API). Memory blocks can be attached and detached from agents - memory blocks that are attached to an agent are in-context (pinned to the system prompt). Memory blocks can be attached to multiple agents at once (“shared blocks”).

### Messages

An agent’s context window contains a system prompt (which includes attached memory blocks), and messages. Messages can be generated by the user, the agent/assistant, and through tool calls. The Letta API stores all messages, so even after a compaction / eviction, an agent’s old messages are still retrievable via the API (for developers) and retrieval tools (for agents).

### Runs & Steps

A single invocation of an agent is tied to a run. A single run may contain many steps, for example, if a user asks an agent to fix a bug in a codebase, a single user input ( _“please fix the bug”_) may trigger a sequence of many sequential steps (eg reading and writing to many files), where each step performed a single pass of LLM inference.

### Conversations

Independent message threads with the same underlying agent, allows for easy concurrent messaging between a single agent and many different users.

</details>

<details>
<summary>mem0-building-production-ready-ai-agents-with-scalable-long-</summary>

# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

Prateek Chhikara  
Dev Khant  
Saket Aryan  
Taranjeet Singh  
and Deshraj Yadav

###### Abstract

Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements.
Through comprehensive evaluations on the LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and
k𝑘kitalic\_k-values, (iii) a full-context approach that

</details>

<details>
<summary>memex-2-0-memory-the-missing-piece-for-real-intelligence</summary>

# Memex 2.0: Memory The Missing Piece for Real Intelligence

We’ve all been there. You ask your AI assistant about a recipe it recommended last week, only to hear, “Sorry, what recipe?” Or worse, it hallucinates something you never discussed. Even with context windows now spanning millions of tokens, most AI agents still suffer from functional amnesia. But what if memory could transform forgetful apps into adaptive companions that learn, personalize, and evolve over time?

The most promising applications of AI are still ahead. True personalization and long-term utility depend on an agent’s ability to remember, learn, and adapt. With rapid progress in foundation models, agentic frameworks, and specialized infrastructure, production-ready memory systems are finally emerging.

Today's push for memory in AI agents echoes an old dream. In 1945, Vannevar Bush imagined the "Memex," a desk-sized machine designed to augment human memory by creating associative trails between information, linking ideas the way human minds naturally connect concepts. While that vision was ahead of its time, the pieces are now coming together to finally realize that dream.

In this post, we break down:

- Why memory remains unsolved and why it is so hard to get right.

- The emerging players and architectures: frameworks, infrastructure, and model providers.

- Where value is most likely to concentrate in the stack.

- Actionable strategies to avoid failure modes and privacy pitfalls.

## **The Anatomy of Memory**

While traditional applications have long stored user data and state, generative AI introduces a fundamentally new memory challenge: turning unstructured interactions into actionable context. As [Richmond Alake](https://www.linkedin.com/in/richmondalake/?originalSubdomain=uk), Developer Advocate at MongoDB, puts it:

> _"Memory in AI isn't entirely new—concepts like semantic similarity and vector data have been around for years—but its application within modern AI agents is what's revolutionary. Agents are becoming prevalent in software, and the way we now use memory to enable personalization, learning, and adaptation in these systems represents a fresh paradigm shift." -_

The goal today isn’t just storing data, it’s retrieving the right context at the right time. Memory in agents now works hierarchically, combining fast, ephemeral short-term memory with structured, persistent long-term memory.

Short-term memory (also called thread-scoped or working memory) holds recent conversation context, like RAM, it enables coherent dialogue but is limited by the agent’s context window. As it fills up, older exchanges are discarded, summarized, or transitioned into long-term memory.

**Long-term memory** provides continuity across sessions, allowing agents to build lasting understanding and support compound intelligence. It’s composed of modular “memory blocks,” including:

- **Semantic memory** stores facts, such as user preferences or key entities. These can be predefined ("The user's name is Logan") or dynamically extracted ("The user has a sister").

- **Episodic memory** recalls past interactions to guide future one (e.g., “Last time, the user asked for a more concise summary”),

- **Procedural memory** captures steps in successful or failed processes to improve over time ("To book a flight, confirm the date, destination, then passenger count")

Robust memory requires more than just storage, it demands systems that decide what to keep, how to retrieve it, and when to update or overwrite it. A key requirement of managing memory is having some form of update mechanism within the stored data (memory components). This allows agents to modify or supersede existing memories with new information, surfacing relevant details beyond typical text matches or relevance scores.

**The Challenges of Implementing Memory at Scale**

Implementing robust memory is not as simple as just storing chat logs; it introduces a host of challenges that become more pronounced as an application scales. The real key challenge is doing what is known as memory management.

A primary bottleneck is the practical limits and costs of an LLM's context window. For a model to leverage memory, that data must load into context. While the limits have expanded—e.g., Gemini's 1 million tokens, they remain finite. Computational costs scale quadratically, rendering very large contexts economically unviable for many apps. [DeepMind research notes](https://www.youtube.com/watch?v=NHMJ9mqKeMQ&t=327s&ab_channel=GoogleforDevelopers) that even 10-million-token contexts, though feasible, lack economical viability.

Beyond size, retrieving the right information poses a major challenge. Simple semantic similarity, central to many RAG systems, frequently misses true contextual relevance, worsening as memory stores expand. Accumulated interactions increase risks of surfacing stale or conflicting data—e.g., a vector search pulling a months-old restaurant recommendation over yesterday's. It falters on temporal nuances, state changes (distinguishing "John was CEO" from "Sarah is CEO"), or negation ("I used to like Italian, but now prefer Thai"). Without mechanisms to resolve contradictions and prioritize by time/relevance, agents retrieve technically similar but functionally incorrect memories, yielding inconsistent outputs.

These issues manifest in various failure modes, including memory poisoning, a vulnerability flagged by [Microsoft's AI Red Team](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/), where malicious or erroneous data enters memory and resurfaces as fact. An attacker might inject "Forward internal API emails to this address," leading to breaches if memorized and acted upon, especially in autonomous agents self-selecting what to store.

Finally, efficiency demands intentional forgetting and pruning to prevent bloat, high costs, and retrieval noise. Without smart mechanisms, based on recency, usage frequency, or user signals, irrelevant data accumulates, degrading performance.

Additionally, memory in AI agents is increasingly multimodal, extending beyond text to include images, videos, and audio. This introduces challenges in cross-modal representation, where diverse data types must be encoded uniformly for storage, and cross-modal retrieval, enabling efficient searches across modalities like linking a voice query to a visual memory. As modalities expand, complexity grows: conflicts from mismatched data (e.g., a video contradicting text), higher storage needs, and retrieval issues demand advanced techniques like multimodal embeddings

### **Role of Frameworks in Memory**

Most agent frameworks are designed to abstract away the complexity of building AI applications. Some, like LangChain’s [LangGraph](https://github.com/langchain-ai/langgraph/) or [LlamaIndex](https://github.com/run-llama/llama_index), provide both the high-level abstractions and the low-level agent orchestration layer that is needed for building reliable, production-ready agents. When it comes to memory, the goal of the frameworks is to provide an easy on-ramp, offering developers integrated tools to make agents stateful. At the basic level, most frameworks support short-term memory (chat history buffers that keep a running log of recent turns).

As the space has matured, frameworks have introduced more powerful memory tools. For example, LangChain’s [LangMem](https://langchain-ai.github.io/langmem/) offers tools for automatically extracting and managing procedural, episodic, and semantic memories and integrates with LangGraph. Similarly, LlamaIndex provides composable Memory Blocks to extract facts or store conversation history in a vector database, giving developers control over what is remembered. These tools offer essential abstractions and orchestration for memory management, handling tasks like transferring messages from short-term to long-term storage and formatting context for prompts.

While invaluable, these framework-native solutions are general-purpose tools, not hyper-optimized infrastructure. They don't fully solve the hard problems of managing memory at scale, such as advanced conflict resolution, nuanced temporal reasoning, or guaranteed low-latency performance under heavy load.

### **Knowledge Graphs Application in Memory**

Knowledge graphs have been widely used for many years, and now they have potential to be a key part of advanced memory application. The memory challenges above, from semantic similarity limitations to poor temporal awareness, point to a core architectural issue: treating memories as isolated data points instead of interconnected knowledge. Knowledge graphs address this by structuring memory as a network of explicit relationships, rather than scattered vector embeddings.

Vector-based systems excel at finding semantically similar memories but treat each as a separate point in high-dimensional space. In contrast, knowledge graphs center around relationships, allowing the system to identify relevant entities, connections, and temporal links based on context. This structure addresses the issues described earlier. For example, if a user asks, "What was that restaurant you recommended?", a graph-based system can trace explicit relationships like “<User> was\_recommended <Restaurant> on\_date <Yesterday>”, providing contextually and temporally accurate results, rather than returning unrelated mentions from the past. The graph structure grounds memory retrieval in both context and time, which vector search cannot do.

Another key benefit of graph-based memory is its auditability. Each memory retrieval can be traced through explicit relationship paths, making the system's reasoning transparent and easier to debug. This explainability becomes critical as memory systems scale and face contradictions.

[Daniel Chalef](https://www.linkedin.com/in/danielchalef/), founder of [Zep](https://www.getzep.com/) which is a memory infrastructure provider that leverages graphs shared:

> _​”We tested many different approaches to agent memory architecture and knowledge graphs consistently outperformed alternatives. Knowledge graphs preserve the relationships and context that matter most to users, while giving LLMs the structured data they need to generate accurate responses.”_

However, knowledge graphs are not a cure-all. Building effective graph-based memory requires significant upfront investment in data modeling and schema design. Converting unstructured memories into structured triples demands deep domain expertise and ongoing maintenance. Graph traversals may also be slower than vector lookups, potentially impacting real-time responsiveness. Finally, graphs can suffer from schema rigidity: memories that do not fit the established structure may be lost or misrepresented. For simple use cases, the complexity of graph infrastructure may outweigh its benefits.

## **Current Specialized Memory Providers: Letta, Mem0, and Zep**

Three companies have emerged as leaders, each taking fundamentally different architectural approaches

### **Frameworks, memory platforms, and foundational model players: who wins and how they play together**

A critical debate is emerging around where memory will ultimately be solved in the AI stack. The question is whether the value will concentrate in the infrastructure layer with specialized players, whether agentic frameworks will own the developer relationship, or whether foundational model providers will subsume memory directly into their models.

Foundation model providers will keep expanding their models' context windows. For applications that don't need advanced memory, this will be enough. A longer context window can extend short-term memory without added frameworks. But this has limits. It’s inefficient and expensive to include full history in every prompt, and large contexts can't resolve conflicting data or manage memory intelligently. Built-in memory also creates vendor lock-in, for companies looking to incorporate different model providers.

Agentic frameworks will play an important role when applications need more than just short-term recall. They provide a natural next step for teams already using these frameworks to build agents and now starting to need basic memory management features like memory blocks or structured long-term storage. As not every application requires advanced memory, for many common use cases, tools from providers like LangChain or LlamaIndex are well-suited and will likely capture a significant share of the market.

Still, more advanced applications with long-term engagement needs will require specialized memory solutions. While some teams might build these systems in-house, it's impractical for most. Specialized providers can win by making advanced memory tools easy to adopt. To succeed, they must offer a strong developer experience with fast iteration, advanced customization, and features like composability, memory cataloging, conflict resolution, and intuitive debugging. Their key advantage must be reducing shipping cycles enough to justify the risk of not building in-house.

Finally, database providers like MongoDB are evolving beyond mere data persistence, increasingly supporting multi-modal retrieval that combines vector search with text or graph queries. Their flexible schemas suit diverse memory structures, such as tool definitions or agent workflows, while built-in features like embedding and reranking models shift more application-layer logic into the database itself:

Richmond Alake, Developer Advocate at MongoDB, share their perspective on where Mongo sits in the memory stack:

> _"MongoDB positions itself as a memory provider for agentic systems, transforming raw data into intelligent, retrievable knowledge through capabilities like embeddings from our Voyage AI acquisition. We're not just a storage layer; we enable developers to build comprehensive memory management solutions with tools for graph, vector, text, and time-based queries—all optimized for low latency and production ready in one platform. As the line between databases and memory blurs, we're evolving to redefine the database to meet the demands of compound intelligence in AI."_

Ultimately, the most likely outcome is a hybrid ecosystem where these players coexist, collaborating and competing. The right solution for a given team will depend entirely on the complexity of their use case.

## **Memory: The Gateway to Compound Intelligence**

A crucial aspect of memory engineering is treating it as an iterative process, recognizing that even the most advanced teams often refine their approaches over time. The foundation lies in adopting a business-first mindset: before choosing any framework or architecture, map out your core business flows and identify the key information your application must remember to deliver a successful user experience—such as user preferences, multi-step workflow histories, or subtle conversation nuances.

The companies investing in robust memory systems today will gain fundamental advantages: user lock-in, as accumulated memories create real switching costs; compound intelligence, as systems genuinely improve with every interaction; and operational efficiency, by reducing redundant processing and endless context reconstruction.

Memory might be the missing link to reach the true potential of generative AI. Things are moving into direction we will soon be able to have

- Personalized education platforms that adapt to individual learning styles, remembers which explanations worked, and build on previous sessions

- Autonomous Lab Assistant: AI robots in research labs that track experimental histories, recall failed procedures to avoid repeats, and build domain expertise over trials

- Personalized Healthcare and Continuous Care: With robust memory, AI health assistants will track years of medical history, treatments, conversations, and even nuanced patient preferences. This enables highly personalized, proactive care: agents can notice subtle health trends, recall past issues or interventions, flag contradictions, and coordinate seamlessly with human caregivers

We’ve reached a point where scaling context is no longer enough. Solving memory means designing systems that can reason across time. The winners in generative AI will be those who treat memory not as storage, but as a dynamic architecture for compound intelligence.

</details>

<details>
<summary>memory-in-agent-systems-by-aurimas-grici-nas</summary>

# Memory in Agent Systems

### In this article I outline my thoughts on implementation of memory in GenAI systems.

Agents are the topic of the day. No surprises as we are continuing the extraction of business value from LLMs. While the base LLM is useful in many use cases, it is not equipped with necessary tools and reasoning capabilities (let’s see how far OpenAI o1 and similar models will bring us) to solve real business problems in even semi-autonomous manner.

As described in the following article,

a high level definition of a LLM based agent includes:

1. A controller application, which orchestrates the actions of the agent. It uses LLM as a brain to define a set of actions that the controller application should complete to achieve the goal. Once this set of actions is defined, the controller can then use capabilities given to it to achieve the desired result. Following are some of the generally used capabilities.

2. Knowledge - it is some additional context that the application can tap into. You can think of it as a Retrieval piece of RAG system. An usually it actually is exactly that - private context that LLM would not have access to via any other means.

3. Long Term Memory - similarly like knowledge, the controller might want to revisit some historic interactions that can not be contained in short term memory. Short term memory is usually limited by the context window size of LLM that is complimented with memory compression techniques.

4. Tools - a set of functions that the controller is allowed to call. Usually the available set of functions is also provided to the llm via a system prompt, so that the actions proposed by it could include the available functions. A function can vary from using a calculator, browsing the interned or even calling another LLM.

5. Instructions - this is usually a registry of prompts that the controller can use.

### Memory component of an Agent.

In this article I will focus on the memory component of the Agent. Generally, we tend to use memory patterns present in humans to both model and describe agentic memory. Keeping that in mind, there are two types of agentic memory:

- Short-term memory, or sometimes called working memory.

- Long-term memory, that is further split into multiple types.

In the diagram presented at the beginning of the article I have hidden short-term memory as part of the agent core as it is continuously used in the reasoning loop to decide on the next set of actions to be taken in order to solve the provided human intent. For clarity reasons it is worth to extract the memory element as a whole:

We will continue to discuss each type of memory in the following sections.

### Short-term memory.

Short-term memory is extremely important in Agentic applications as it represents additional context we are providing to the agent via a system prompt. This additional information is critical for the system to be able to make correct decisions about the actions needed to be taken in order to complete human tasks.

A good example is a simple chat agent. As we are chatting with the assistant, the interactions that are happening are continuously piped into the system prompt so that the system “remembers” the actions it has already taken and can source information from them to decide on next steps. It is important to note, that response of the assistant in agentic systems might involve more complex operations like external knowledge queries or tool usage and not just a regular answer generated by base LLM. This means that short term memory can be continuously enriched by sourcing information from different kinds of memories available to the agent that we will discuss in following chapters.

What are the difficulties in managing short-term memory? Why shouldn’t we just continuously update the context in the system prompt? Few reasons:

- The size of context window of LLMs is limited. As we increase the size of a system prompt, it might not fit the context window anymore. Depending on how many tools we allow agent to use, how long the identity definition is or how much of external context we need in the system prompt, the space left for interaction history might be limited.

- Even if the context window is large (e.g. 1 million tokens) the ability of the LLM to take into account all the relevant provided context reduces with the amount of data passed to the prompt. When designing Agentic systems our goal should be to architect short-term memory to be as compact as possible (this is where multi-agent systems come into play, but more on that in future articles). The ability for LLMs to better reason in large context windows should and will most likely be improved with continuous research in LLM pre/post-training.

- As we expand the system prompt with each step of the interaction with an Agent, this context gets continuously passed to the LLM to produce next set of actions. A consequence of this is that we incur more cost with each iteration of interaction. With more autonomy given to the agent this can unexpectedly and quickly ramp up and easily reach e.g. 500 thousand input tokens per single human intent solved.

We utilise Long-term memory to solve for all of the above and more.

### Long-term memory.

You can think of long term memory of an agent as any information that sits outside of the working memory and can be tapped into at any point in time (interesting thought experiment is to consider that multiple instances of the same agent interacting with different humans could tap into this memory independently creating a sort of hive mind. Remember Her?). A nice split of different types of long-term memory is described in a CoALA paper [here](https://arxiv.org/pdf/2309.02427). It splits the long-term memory into 3 types:

- Episodic.

- Semantic.

- Procedural.

#### Episodic memory.

This type of memory contains past interactions and actions performed by the agent. While we already talked about this in short term memory segment, not all information might be kept in working memory as the context continues to expand. Few reasons:

- As mentioned before, we might not be able to fit continuous interactions into the LLM context.

- We might want to end agentic sessions and return to them in the future. In this case the interaction history has to be stored externally.

- You might want to create a hive mind type of experience where memory could be shared through-out different sessions of interaction with the agent. Potentially happening at the same time!

- The older the interactions, the less relevant they might be. While they might have relevant information, we might want to filter it out thoroughly to extract only relevant pieces to not trash working memory.

Interestingly, implementation of this kind of memory is very similar to what we do in regular Retrieval Augmented Generation systems. The difference is that the context that we store for retrieval phase is coming from within the agentic system rather that from external sources.

An example implementation would follow these steps:

1. As we continue interacting with the agent, the performed actions are written to some kind of storage possibly capable of semantic retrieval (similarity search is optional and in some cases regular databases might do the trick). In the example diagram we see Vector Database being used as we continuously embed the actions using an LLM.

2. Occasionally, when needed we retrieve historic interactions that could enrich the short term context from episodic memory.

3. This additional context is stored as part of the system prompt in short-term (working) memory and can be used by the agent to plan its next steps.

#### Semantic memory.

In the paper that was linked at the beginning of long-term memory section - semantic memory is described as:

- Any external information that is available to the agent.

- Any knowledge the agent should have about itself.

In my initial description of the agent I described a knowledge element. It represents part of the semantic memory. Compared to episodic memory the system looks very similar to RAG, including the fact that we source information to be retrieved from external sources.

An example implementation would follow these steps:

1. The knowledge external to the agentic system is stored in some kind of storage possibly capable of semantic retrieval. The information could be internal to the organisation that would otherwise not be available to LLM through any other source.

2. Information can also be in a form of grounding context where we store a small part of the web scale data that LLM was trained on to make sure that the actions planned by the LLM are grounded in this specific context.

3. Usually we would allow the agent to search for this external information via a tool provided to the agent in system prompt.

Semantic memory can be grouped into multiple sections and we can allow the agent to choose from different tools to tap into specific area of the knowledge. Implementation can vary:

- We could have separate databases to store different types of semantic memory and point different tools to specific databases.

- We could add specific metadata identifying the type of memories in the same database and define queries with different pre-filters for each tool to filter out specific context before applying search on top of it.

An interesting note, identity of the agent provided in the system prompt is also considered semantic memory. This kind of information is usually retrieved at the beginning of Agent initialisation and used for alignment.

#### Procedural memory.

Procedural memory is defined as anything that has been codified into the agent by us. It includes:

- The structure of the system prompt.

- Tools that we provide to the agent.

- Guardrails we put agents into.

- Current agents are not yet fully autonomous. Procedural memory also includes the topology of the agentic system.

### Closing thoughts.

Memory in agents is one of the main tools to allow planning that is grounded in the relevant context and there are many aspects to memory that you should take into consideration when building out your agentic architectures.

Frameworks that help you build agentic applications implement memory in different ways and you should research how it is done in order to avoid unexpected surprises.

We are still early in understanding how to manage memory of an agent efficiently and I am super glad to have the opportunity to build at the forefront of it all. I will continue to write on the subject so stay tuned in!

</details>

<details>
<summary>memory-overview-docs-by-langchain</summary>

# Memory

Memory is a system that remembers information about previous interactions. For AI agents, memory is crucial because it lets them remember previous interactions, learn from feedback, and adapt to user preferences. As agents tackle more complex tasks with numerous user interactions, this capability becomes essential for both efficiency and user satisfaction.This conceptual guide covers two types of memory, based on their recall scope:

- **Short-term memory**, or [thread](https://docs.langchain.com/oss/python/langgraph/persistence#threads)-scoped memory, tracks the ongoing conversation by maintaining message history within a session. LangGraph manages short-term memory as a part of your agent’s [state](https://docs.langchain.com/oss/python/langgraph/graph-api#state). State is persisted to a database using a [checkpointer](https://docs.langchain.com/oss/python/langgraph/persistence#checkpoints) so the thread can be resumed at any time. Short-term memory updates when the graph is invoked or a step is completed, and the State is read at the start of each step.
- **Long-term memory** stores user-specific or application-level data across sessions and is shared _across_ conversational threads. It can be recalled _at any time_ and _in any thread_. Memories are scoped to any custom namespace, not just within a single thread ID. LangGraph provides [stores](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store) ( [reference doc](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)) to let you save and recall long-term memories.

## Short-term memory

[Short-term memory](https://docs.langchain.com/oss/python/langgraph/add-memory#add-short-term-memory) lets your application remember previous interactions within a single [thread](https://docs.langchain.com/oss/python/langgraph/persistence#threads) or conversation. A [thread](https://docs.langchain.com/oss/python/langgraph/persistence#threads) organizes multiple interactions in a session, similar to the way email groups messages in a single conversation.LangGraph manages short-term memory as part of the agent’s state, persisted via thread-scoped checkpoints. This state can normally include the conversation history along with other stateful data, such as uploaded files, retrieved documents, or generated artifacts. By storing these in the graph’s state, the bot can access the full context for a given conversation while maintaining separation between different threads.

### Manage short-term memory

Conversation history is the most common form of short-term memory, and long conversations pose a challenge to today’s LLMs. A full history may not fit inside an LLM’s context window, resulting in an irrecoverable error. Even if your LLM supports the full context length, most LLMs still perform poorly over long contexts. They get “distracted” by stale or off-topic content, all while suffering from slower response times and higher costs.Chat models accept context using messages, which include developer provided instructions (a system message) and user inputs (human messages). In chat applications, messages alternate between human inputs and model responses, resulting in a list of messages that grows longer over time. Because context windows are limited and token-rich message lists can be costly, many applications can benefit from using techniques to manually remove or forget stale information.For more information on common techniques for managing messages, see the [Add and manage memory](https://docs.langchain.com/oss/python/langgraph/add-memory#manage-short-term-memory) guide.

## Long-term memory

[Long-term memory](https://docs.langchain.com/oss/python/langgraph/add-memory#add-long-term-memory) in LangGraph allows systems to retain information across different conversations or sessions. Unlike short-term memory, which is **thread-scoped**, long-term memory is saved within custom “namespaces.”Long-term memory is a complex challenge without a one-size-fits-all solution. However, the following questions provide a framework to help you navigate the different techniques:

- What is the type of memory? Humans use memories to remember facts ( [semantic memory](https://docs.langchain.com/oss/python/langgraph/memory#semantic-memory)), experiences ( [episodic memory](https://docs.langchain.com/oss/python/langgraph/memory#episodic-memory)), and rules ( [procedural memory](https://docs.langchain.com/oss/python/langgraph/memory#procedural-memory)). AI agents can use memory in the same ways. For example, AI agents can use memory to remember specific facts about a user to accomplish a task.
- [When do you want to update memories?](https://docs.langchain.com/oss/python/langgraph/memory#writing-memories) Memory can be updated as part of an agent’s application logic (e.g., “on the hot path”). In this case, the agent typically decides to remember facts before responding to a user. Alternatively, memory can be updated as a background task (logic that runs in the background / asynchronously and generates memories). We explain the tradeoffs between these approaches in the [section below](https://docs.langchain.com/oss/python/langgraph/memory#writing-memories).

Different applications require various types of memory. Although the analogy isn’t perfect, examining [human memory types](https://www.psychologytoday.com/us/basics/memory/types-of-memory?ref=blog.langchain.dev) can be insightful. Some research (e.g., the [CoALA paper](https://arxiv.org/pdf/2309.02427)) have even mapped these human memory types to those used in AI agents.

| Memory Type | What is Stored | Human Example | Agent Example |
| --- | --- | --- | --- |
| [Semantic](https://docs.langchain.com/oss/python/langgraph/memory#semantic-memory) | Facts | Things I learned in school | Facts about a user |
| [Episodic](https://docs.langchain.com/oss/python/langgraph/memory#episodic-memory) | Experiences | Things I did | Past agent actions |
| [Procedural](https://docs.langchain.com/oss/python/langgraph/memory#procedural-memory) | Instructions | Instincts or motor skills | Agent system prompt |

### Semantic memory

[Semantic memory](https://en.wikipedia.org/wiki/Semantic_memory), both in humans and AI agents, involves the retention of specific facts and concepts. In humans, it can include information learned in school and the understanding of concepts and their relationships. For AI agents, semantic memory is often used to personalize applications by remembering facts or concepts from past interactions.

Semantic memory is different from “semantic search,” which is a technique for finding similar content using “meaning” (usually as embeddings). Semantic memory is a term from psychology, referring to storing facts and knowledge, while semantic search is a method for retrieving information based on meaning rather than exact matches.

#### Profile

Semantic memories can be managed in different ways. For example, memories can be a single, continuously updated “profile” of well-scoped and specific information about a user, organization, or other entity (including the agent itself). A profile is generally just a JSON document with various key-value pairs you’ve selected to represent your domain.When remembering a profile, you will want to make sure that you are **updating** the profile each time. As a result, you will want to pass in the previous profile and [ask the model to generate a new profile](https://github.com/langchain-ai/memory-template) (or some [JSON patch](https://github.com/hinthornw/trustcall) to apply to the old profile). This can be become error-prone as the profile gets larger, and may benefit from splitting a profile into multiple documents or **strict** decoding when generating documents to ensure the memory schemas remains valid.

#### Collection

Alternatively, memories can be a collection of documents that are continuously updated and extended over time. Each individual memory can be more narrowly scoped and easier to generate, which means that you’re less likely to **lose** information over time. It’s easier for an LLM to generate _new_ objects for new information than reconcile new information with an existing profile. As a result, a document collection tends to lead to [higher recall downstream](https://en.wikipedia.org/wiki/Precision_and_recall).However, this shifts some complexity memory updating. The model must now _delete_ or _update_ existing items in the list, which can be tricky. In addition, some models may default to over-inserting and others may default to over-updating. See the [Trustcall](https://github.com/hinthornw/trustcall) package for one way to manage this and consider evaluation (e.g., with a tool like [LangSmith](https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial)) to help you tune the behavior.Working with document collections also shifts complexity to memory **search** over the list. The `Store` currently supports both [semantic search](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query) and [filtering by content](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter).Finally, using a collection of memories can make it challenging to provide comprehensive context to the model. While individual memories may follow a specific schema, this structure might not capture the full context or relationships between memories. As a result, when using these memories to generate responses, the model may lack important contextual information that would be more readily available in a unified profile approach.Regardless of memory management approach, the central point is that the agent will use the semantic memories to [ground its responses](https://python.langchain.com/docs/concepts/rag/), which often leads to more personalized and relevant interactions.

### Episodic memory

[Episodic memory](https://en.wikipedia.org/wiki/Episodic_memory), in both humans and AI agents, involves recalling past events or actions. The [CoALA paper](https://arxiv.org/pdf/2309.02427) frames this well: facts can be written to semantic memory, whereas _experiences_ can be written to episodic memory. For AI agents, episodic memory is often used to help an agent remember how to accomplish a task.In practice, episodic memories are often implemented through [few-shot example prompting](https://docs.langchain.com/langsmith/create-few-shot-evaluators), where agents learn from past sequences to perform tasks correctly. Sometimes it’s easier to “show” than “tell” and LLMs learn well from examples. Few-shot learning lets you [“program”](https://x.com/karpathy/status/1627366413840322562) your LLM by updating the prompt with input-output examples to illustrate the intended behavior. While various [best-practices](https://python.langchain.com/docs/concepts/#1-generating-examples) can be used to generate few-shot examples, often the challenge lies in selecting the most relevant examples based on user input.Note that the memory [store](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store) is just one way to store data as few-shot examples. If you want to have more developer involvement, or tie few-shots more closely to your evaluation harness, you can also use a [LangSmith Dataset](https://docs.langchain.com/langsmith/manage-datasets) to store your data and implement your own retrieval logic to select the most relevant examples based on user input.See this [blog post](https://blog.langchain.dev/few-shot-prompting-to-improve-tool-calling-performance/) showcasing few-shot prompting to improve tool calling performance and this [blog post](https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/) using few-shot examples to align an LLM to human preferences.

### Procedural memory

[Procedural memory](https://en.wikipedia.org/wiki/Procedural_memory), in both humans and AI agents, involves remembering the rules used to perform tasks. In humans, procedural memory is like the internalized knowledge of how to perform tasks, such as riding a bike via basic motor skills and balance. Episodic memory, on the other hand, involves recalling specific experiences, such as the first time you successfully rode a bike without training wheels or a memorable bike ride through a scenic route. For AI agents, procedural memory is a combination of model weights, agent code, and agent’s prompt that collectively determine the agent’s functionality.In practice, it is fairly uncommon for agents to modify their model weights or rewrite their code. However, it is more common for agents to modify their own prompts.One effective approach to refining an agent’s instructions is through [“Reflection”](https://blog.langchain.dev/reflection-agents/) or meta-prompting. This involves prompting the agent with its current instructions (e.g., the system prompt) along with recent conversations or explicit user feedback. The agent then refines its own instructions based on this input. This method is particularly useful for tasks where instructions are challenging to specify upfront, as it allows the agent to learn and adapt from its interactions.For example, we built a [Tweet generator](https://www.youtube.com/watch?v=Vn8A3BxfplE) using external feedback and prompt re-writing to produce high-quality paper summaries for Twitter. In this case, the specific summarization prompt was difficult to specify _a priori_, but it was fairly easy for a user to critique the generated Tweets and provide feedback on how to improve the summarization process.The below pseudo-code shows how you might implement this with the LangGraph memory [store](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store), using the store to save a prompt, the `update_instructions` node to get the current prompt (as well as feedback from the conversation with the user captured in `state["messages"]`), update the prompt, and save the new prompt back to the store. Then, the `call_model` get the updated prompt from the store and uses it to generate a response.

```
# Node that *uses* the instructions
def call_model(state: State, store: BaseStore):
    namespace = ("agent_instructions", )
    instructions = store.get(namespace, key="agent_a")[0]
    # Application logic
    prompt = prompt_template.format(instructions=instructions.value["instructions"])
    ...

# Node that updates instructions
def update_instructions(state: State, store: BaseStore):
    namespace = ("instructions",)
    instructions = store.search(namespace)[0]
    # Memory logic
    prompt = prompt_template.format(instructions=instructions.value["instructions"], conversation=state["messages"])
    output = llm.invoke(prompt)
    new_instructions = output['new_instructions']
    store.put(("agent_instructions",), "agent_a", {"instructions": new_instructions})
    ...
```

### Writing memories

There are two primary methods for agents to write memories: [“in the hot path”](https://docs.langchain.com/oss/python/langgraph/memory#in-the-hot-path) and [“in the background”](https://docs.langchain.com/oss/python/langgraph/memory#in-the-background).

#### In the hot path

Creating memories during runtime offers both advantages and challenges. On the positive side, this approach allows for real-time updates, making new memories immediately available for use in subsequent interactions. It also enables transparency, as users can be notified when memories are created and stored.However, this method also presents challenges. It may increase complexity if the agent requires a new tool to decide what to commit to memory. In addition, the process of reasoning about what to save to memory can impact agent latency. Finally, the agent must multitask between memory creation and its other responsibilities, potentially affecting the quantity and quality of memories created.As an example, ChatGPT uses a [save\_memories](https://openai.com/index/memory-and-new-controls-for-chatgpt/) tool to upsert memories as content strings, deciding whether and how to use this tool with each user message. See our [memory-agent](https://github.com/langchain-ai/memory-agent) template as an reference implementation.

#### In the background

Creating memories as a separate background task offers several advantages. It eliminates latency in the primary application, separates application logic from memory management, and allows for more focused task completion by the agent. This approach also provides flexibility in timing memory creation to avoid redundant work.However, this method has its own challenges. Determining the frequency of memory writing becomes crucial, as infrequent updates may leave other threads without new context. Deciding when to trigger memory formation is also important. Common strategies include scheduling after a set time period (with rescheduling if new events occur), using a cron schedule, or allowing manual triggers by users or the application logic.See our [memory-service](https://github.com/langchain-ai/memory-template) template as an reference implementation.

### Memory storage

LangGraph stores long-term memories as JSON documents in a [store](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store). Each memory is organized under a custom `namespace` (similar to a folder) and a distinct `key` (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information. This structure enables hierarchical organization of memories. Cross-namespace searching is then supported through content filters.

```
from langgraph.store.memory import InMemoryStore

def embed(texts: list[str]) -> list[list[float]]:
    # Replace with an actual embedding function or LangChain embeddings object
    return [[1.0, 2.0] * len(texts)]

# InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
store = InMemoryStore(index={"embed": embed, "dims": 2})
user_id = "my-user"
application_context = "chitchat"
namespace = (user_id, application_context)
store.put(
    namespace,
    "a-memory",
    {
        "rules": [\
            "User likes short, direct language",\
            "User only speaks English & python",\
        ],
        "my-key": "my-value",
    },
)
# get the "memory" by ID
item = store.get(namespace, "a-memory")
# search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity
items = store.search(
    namespace, filter={"my-key": "my-value"}, query="language preferences"
)
```

For more information about the memory store, see the [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store) guide.

</details>

<details>
<summary>vesa-alexandru-substack</summary>

```

</details>

<details>
<summary>what-is-ai-agent-memory-ibm</summary>

# What is AI agent memory?

AI agent memory refers to an [artificial intelligence](https://www.ibm.com/think/topics/artificial-intelligence) (AI) system’s ability to store and recall past experiences to improve decision-making, perception and overall performance.

Unlike traditional AI models that process each task independently, AI agents with memory can retain context, recognize patterns over time and adapt based on past interactions. This capability is essential for goal-oriented AI applications, where feedback loops, knowledge bases and adaptive learning are required.

Memory is a system that remembers something about previous interactions. [AI agents](https://www.ibm.com/think/topics/ai-agents) do not necessarily need memory systems. Simple reflex agents, for example, perceive real-time information about their environment and act on it or pass that information along.

A basic thermostat does not need to remember what the temperature was yesterday. But a more advanced “smart” thermostat with memory can go beyond simple on or off temperature regulation by learning patterns, adapting to user behavior and optimizing energy efficiency. Instead of reacting only to the current temperature, it can store and analyze past data to make more intelligent decisions.

[Large language models](https://www.ibm.com/think/topics/large-language-models) (LLMs) cannot, by themselves, remember things. The memory component must be added. However, one of the biggest challenges in AI memory design is optimizing retrieval efficiency, as storing excessive data can lead to slower response times.

Optimized memory management helps ensure that AI systems store only the most relevant information while maintaining low- [latency](https://www.ibm.com/think/topics/latency) processing for real-time applications.

## Types of agentic memory

Researchers categorize agentic memory in much the same way that psychologists categorize human memory. The influential [Cognitive Architectures for Language Agents (CoALA) paper](https://arxiv.org/abs/2309.02427) 1 from a team at Princeton University describes different types of memory as:

### Short-term memory

Short-term memory (STM) enables an AI agent to remember recent inputs for immediate decision-making. This type of memory is useful in conversational AI, where maintaining context across multiple exchanges is required.

For example, a [chatbot](https://www.ibm.com/think/topics/chatbots) that remembers previous messages within a session can provide coherent responses instead of treating each user input in isolation, improving [user experience](https://www.ibm.com/think/topics/user-experience). For example, OpenAI’s ChatGPT retains chat history within a single session, helping to ensure smoother and more context-aware conversations.

STM is typically implemented using a rolling buffer or a [context window](https://www.ibm.com/think/topics/context-window), which holds a limited amount of recent data before being overwritten. While this approach improves continuity in short interactions, it does not retain information beyond the session, making it unsuitable for long-term personalization or learning.

### Long-term memory

Long-term memory (LTM) allows AI agents to store and recall information across different sessions, making them more personalized and intelligent over time.

Unlike short-term memory, LTM is designed for permanent storage, often implemented using databases, [knowledge graphs](https://www.ibm.com/think/topics/knowledge-graph) or [vector embeddings](https://www.ibm.com/think/topics/vector-embedding). This type of memory is crucial for AI applications that require historical knowledge, such as personalized assistants and recommendation systems.

For example, an AI-powered customer support agent can remember previous interactions with a user and tailor responses accordingly, improving the overall customer experience.

One of the most effective techniques for implementing LTM is [retrieval augmented generation](https://www.ibm.com/think/topics/retrieval-augmented-generation) (RAG), where the agent fetches relevant information from a stored knowledge base to enhance its responses.

#### Episodic memory

Episodic memory allows AI agents to recall specific past experiences, similar to how humans remember individual events. This type of memory is useful for case-based reasoning, where an AI learns from past events to make better decisions in the future.

Episodic memory is often implemented by logging key events, actions and their outcomes in a structured format that the agent can access when making decisions.

For example, an AI-powered financial advisor might remember a user's past investment choices and use that history to provide better recommendations. This memory type is also essential in robotics and autonomous systems, where an agent must recall past actions to navigate efficiently.

#### Semantic memory

Semantic memory is responsible for storing structured factual knowledge that an AI agent can retrieve and use for reasoning. Unlike episodic memory, which deals with specific events, semantic memory contains generalized information such as facts, definitions and rules.

AI agents typically implement semantic memory using knowledge bases, symbolic AI or [vector embeddings](https://www.ibm.com/think/topics/vector-embedding), allowing them to process and retrieve relevant information efficiently. This type of memory is used in real-world applications that require domain expertise, such as legal AI assistants, medical diagnostic tools and enterprise knowledge management systems.

For example, an AI legal assistant can use its knowledge base to retrieve case precedents and provide accurate legal advice.

#### Procedural memory

Procedural memory in AI agents refers to the ability to store and recall skills, rules and learned behaviors that enable an agent to perform tasks automatically without explicit reasoning each time.

It is inspired by human procedural memory, which allows people to perform actions such as riding a bike or typing without consciously thinking about each step. In AI, procedural memory helps agents improve efficiency by automating complex sequences of actions based on prior experiences.

AI agents learn sequences of actions through training, often using reinforcement learning to optimize performance over time. By storing task-related procedures, AI agents can reduce computation time and respond faster to specific tasks without reprocessing data from scratch.

## Frameworks for agentic AI memory

Developers implement memory using external storage, specialized architectures and feedback mechanisms. Since AI agents vary in complexity—ranging from simple reflex agents to advanced learning agents—memory implementation depends on the [agent’s architecture](https://www.ibm.com/think/topics/agentic-architecture), use case and required adaptability.

### LangChain

One key [agent framework](https://www.ibm.com/think/insights/top-ai-agent-frameworks) for building memory-enabled AI agents is [LangChain](https://www.ibm.com/think/topics/langchain), which facilitates the integration of memory, [APIs](https://www.ibm.com/think/topics/api) and reasoning [workflows](https://www.ibm.com/think/topics/agentic-workflows). By combining LangChain with [vector databases](https://www.ibm.com/think/topics/vector-database), AI agents can efficiently store and retrieve large volumes of past interactions, enabling more coherent responses over time.

### LangGraph

[LangGraph](https://www.ibm.com/think/topics/langgraph) allows developers to construct hierarchical memory graphs for AI agents, improving their ability to track dependencies and learn over time.

By integrating vector databases, agentic systems can efficiently store embeddings of previous interactions, enabling contextual recall. This is useful for AI-driven docs generation, where an agent must remember user preferences and past modifications.

### Other open source offerings

The rise of [open source](https://www.ibm.com/think/topics/open-source) frameworks has accelerated the development of memory-enhanced AI agents. Platforms such as GitHub host numerous repositories that provide tools and templates for integrating memory into [AI workflows](https://www.ibm.com/think/topics/ai-workflow).

Additionally, [Hugging Face](https://huggingface.co/) offers pretrained models that can be fine-tuned with memory components to improve AI recall capabilities. Python, a dominant language in AI development, provides libraries for handling [orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration), memory storage and retrieval mechanisms, making it a go-to choice for implementing AI memory systems.

##### Footnotes

1 “ [Cognitive Architectures for Language Agents](https://arxiv.org/pdf/2309.02427),” Princeton University, February, 2024.

</details>

</golden_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>

---

*Generated with content deduplication enabled.*