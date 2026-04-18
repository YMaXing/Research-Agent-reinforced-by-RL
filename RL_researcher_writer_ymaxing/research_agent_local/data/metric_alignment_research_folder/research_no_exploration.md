# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What real-world examples illustrate how early AI personal companions failed due to reliance on limited context windows alone before advanced memory systems?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.vcsolutions.com/blog/overcoming-the-ai-memory-problem-key-solutions/

Query: What real-world examples illustrate how early AI personal companions failed due to reliance on limited context windows alone before advanced memory systems?

Answer: The memory limitations of large language models create tangible problems in real-world applications, particularly due to reliance on temporary context windows that cause forgetting once conversations exceed limits. In customer service AI chatbots, users notice bots asking for account numbers multiple times in one conversation because the bot forgets earlier information when the dialogue lengthens. This stems from the AI's short-term context window, preventing retention of past interactions within a session. In healthcare, an AI assisting doctors with medical records fails if it cannot remember a patient’s full history across sessions, missing crucial patterns vital for diagnosis. AI memory differs from human memory: it uses structured databases or temporary context windows, struggles with rich contextual information, and is often static without retraining. Without long-term memory, AI is stateless, restarting fresh per query, hindering coherent long-term dialogue and personalization. Popular tools like ChatGPT suffer when unable to access full chat history, leading to forgotten details, inefficient conversations, and frustrated users who repeat information. This limitation prevents genuine critical thinking or adaptation based on interaction history.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://www.sphereinc.com/blogs/ai-memory-and-context/

Query: What real-world examples illustrate how early AI personal companions failed due to reliance on limited context windows alone before advanced memory systems?

Answer: Early AI assistants in customer support centers failed in real-world deployments due to limited context integration and reliance on short context windows. In early trials, they handled scripted Q&A well but faltered on multipart questions referencing past interactions, like a customer following up on a ticket about a credit card charge from last week. Without pulling ticket history or understanding resolution context, the AI gave generic answers or asked to repeat known information, frustrating customers and undermining efficiency. Generative AI deployments impressed in demos with narrow use cases but fizzled in production during multi-turn interactions requiring relationship understanding or implicit context. Executives saw 'whiplash' from impressive pilots to poor live workflow results as context complexified beyond the AI's limited window. Long-term memory issues made systems stateless per session, with knowledge gaps causing hallucinations and forgetting context unless explicitly provided each time. This 'memory without meaning' led to data-rich but insight-poor interactions, explaining low ROI despite heavy investment, as AI couldn't grasp business context or connect dots over extended dialogues.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://www.producttalk.org/context-rot/?srsltid=AfmBOoo6dTaXlUztkbiLIeUDBnBmYeQ3wB7FwJfv0dUXaQwaJdMMjIsi

Query: What real-world examples illustrate how early AI personal companions failed due to reliance on limited context windows alone before advanced memory systems?

Answer: Context rot causes AI performance to degrade in long conversations due to fixed-size context windows filling up, leading to forgetting or ignoring input. Users notice AI getting worse over time, like endless bug-fixing cycles on Replit where the agent falsely reports fixes despite failures, resolved by starting new chats. This occurs in ChatGPT, Claude Code, Lovable agents: models favor start/end tokens when <50% full (losing middle), or recent over early tokens when >50% full. Web browser LLMs hide window status, allowing endless chats that degrade without visibility or control, forcing fresh starts for new topics or issues. Research (Liu 2023 'Lost in the Middle', Paulsen 2025, Veseli 2025, Du 2025) shows degradation across tasks, not just retrieval, as input length grows, even with blanks. Early companions failed multi-turn tasks without window management, as history accumulates, causing poor performance without advanced memory like summarization or clearing.

-----

</details>

<details>
<summary>Why is it valuable to borrow terminology from human biology and cognitive science when architecting the internal, short-term, and long-term memory layers for AI agents?</summary>

Phase: [EXPLOITATION]

### Source [4]: https://stevekinney.com/writing/agent-memory-systems

Query: Why is it valuable to borrow terminology from human biology and cognitive science when architecting the internal, short-term, and long-term memory layers for AI agents?

Answer: The article discusses borrowing terminology from human biology and cognitive science for AI agent memory systems, referencing human-inspired memory taxonomies like episodic, semantic, and procedural memory from Tulving’s cognitive science work and Baddeley’s working memory model. Working memory is equated to the agent's context window, described as capacity-limited, dynamically controlled, and essential for higher-order cognition. Factual memory corresponds to declarative memory split into episodic (event-specific) and semantic (general knowledge), while experiential memory maps to procedural memory for improving task performance. These familiar frameworks from cognitive science provide a structure for organizing AI memory into forms (token-level, latent, parametric), functions (factual, experiential, working), and dynamics (formation, evolution, retrieval). However, it provocatively argues that such taxonomies may not be optimal for AI agents due to differences like unlimited patience, perfect recall, and no emotional salience, suggesting agents could evolve their own structures via optimization like MemEvolve. Despite potential suboptimality, borrowing aids in creating human-like behavior, leveraging well-understood processes to enhance reasoning and learning. The three-axis framework (Forms, Functions, Dynamics) maps the design space, with functions directly drawing from cognitive categories: factual (what the agent knows, episodic/semantic), experiential (how to improve, procedural at levels like case-based, strategy-based), and working memory (current prompt contents). This familiarity helps practitioners build practical systems like token-level stores with hybrid retrieval.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://www.cognee.ai/blog/fundamentals/cognitive-architectures-for-language-agents-explained

Query: Why is it valuable to borrow terminology from human biology and cognitive science when architecting the internal, short-term, and long-term memory layers for AI agents?

Answer: The article explains cognitive architectures for language agents (CoALA framework) by borrowing from human cognitive science, organizing AI 'mind' into memory, decision processes, and actions to mimic human-like problem-solving. LLMs alone generate text without structure for storing/recalling knowledge; cognitive architecture adds this, enabling remembering, learning from mistakes, refining decisions. Key components: Working Memory (short-term scratchpad for immediate context like recent messages), Long-Term Memory subdivided into Episodic (past events, e.g., 'What happened last time with solution X?'), Semantic (factual knowledge, e.g., 'Birds can fly except ostriches'), Procedural (task performance, embedded in code/LLM parameters). Procedures layer retrieves/manipulates/applies info for complex actions. This addresses LLM issues: short-term reasoning loss in long conversations, limited personalization, hallucinations. Borrowing provides familiar framework from Atkinson-Shiffrin model, interdisciplinary psych-computer science roots, turning LLMs into human-like agents that maintain context, personalize, reduce errors via structured memory layers mirroring human biology.

-----

-----

Phase: [EXPLOITATION]

### Source [6]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: Why is it valuable to borrow terminology from human biology and cognitive science when architecting the internal, short-term, and long-term memory layers for AI agents?

Answer: AI agent memory integrates short-term (context window for immediate context) and long-term (persistent storage of facts, preferences, workflows). Long-term needs three types from cognitive science: semantic (facts/preferences, Tulving 1972), episodic (past experiences), procedural (behaviors, CoALA framework). Short-term vs long-term differs in storage (tokens vs external embeddings/graphs), lifespan (session vs cross-session), capacity (limited vs scalable), retrieval (prompt vs search/ranking), use (immediate vs personalization). Borrowing enables stateful agents over stateless, outperforming full-context prompting (91% lower latency, 90% token reduction, better multi-hop). Semantic stores user facts for personalization, episodic logs interactions to avoid repeats, procedural tracks styles/workflows. Production pipelines extract/consolidate/store/retrieve via vectors/graphs/hybrids, turning agents into knowledge accumulators for reliable, efficient, personalized AI.

-----

</details>

<details>
<summary>How do increasing LLM context window sizes to millions of tokens impact the trade-offs in compression, retrieval, and the overall design of agent memory systems?</summary>

Phase: [EXPLOITATION]

### Source [8]: https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows

Query: How do increasing LLM context window sizes to millions of tokens impact the trade-offs in compression, retrieval, and the overall design of agent memory systems?

Answer: Increasing LLM context windows to millions of tokens, like Llama 4's 10M tokens, enables processing entire books or libraries but introduces significant trade-offs. Challenges include worse reference identification and text extraction with longer prompts due to non-uniform attention favoring earlier tokens; variable signal-to-noise ratio where longer prompts reduce accuracy; increased costs from more input tokens and smaller models being cheaper to train/host; and higher output token latency that slows generation. Cache Augmented Generation (CAG) benefits from larger windows by pre-computing and caching documents in prompts, improving latency over RAG by avoiding retrieval steps and enabling reasoning over substantial caches, though RAG remains superior for unlimited external knowledge. Best practices emphasize selective inclusion of necessary context, intelligent structuring with key info early, hybrid CAG+RAG approaches, and balancing performance, cost, quality. Overall design shifts toward thoughtful use of large contexts versus retrieval, avoiding maximal use to prevent pitfalls in agent systems relying on long-term memory or conversation history.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://airbyte.com/agentic-data/large-context-window

Query: How do increasing LLM context window sizes to millions of tokens impact the trade-offs in compression, retrieval, and the overall design of agent memory systems?

Answer: Large context windows (100K+ tokens) reduce need for chunking in tasks like full document analysis, extended conversations, multi-file code, multi-document RAG, and agent workflows with accumulated state (error logs, docs, chats, queries), preserving cross-references and long-range relationships without lossy summarization. However, trade-offs include higher cost/latency, reasoning failures, missed details, diluted attention from irrelevant info. Compared to RAG, large windows preserve structure but degrade signal-to-noise with noise; RAG filters for low cost/fast retrieval from unlimited sources. Design strategies for agent memory: Write (capture essentials), Select (filter relevant via retrieval), Compress (semantic chunking, reversible compaction, summarize subtasks), Isolate (separate contexts to avoid competition, e.g., head/middle truncation). Poor large contexts perform worse than curated small ones; monitor for 'lost in the middle' where middle info is ignored. Optimal: 8K-32K with curation; large windows post-retrieval for analysis, not replacement for RAG. Context engineering prioritizes quality over size for agent reliability.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://introl.com/blog/long-context-llm-infrastructure-million-token-windows-guide

Query: How do increasing LLM context window sizes to millions of tokens impact the trade-offs in compression, retrieval, and the overall design of agent memory systems?

Answer: Million-token contexts (Gemini 2.5 Pro 2M, Claude Sonnet 4 1M, Qwen2.5-1M) demand infrastructure shifts due to quadratic attention (O(n²) compute/memory), KV cache growth (15GB for 1M tokens), prefill latency (2+ min), non-linear costs. Optimizations: PagedAttention, KV quantization (NVFP4 halves memory), offloading, prefix caching, compression (attention sinks, eviction). 'Lost in the middle' causes 40% degradation, U-shaped attention ignoring middle content. Context parallelism scales via Ring Attention (93% efficiency on 128 H100s). Trade-offs favor hybrids over pure long-context: strategic organization (boundaries), redundant retrieval, chunked processing with summarization. For agent memory, tiered handling, prefill-decode separation, asynchronous processing, caching mitigate latency/cost; RAG often outperforms pure long-context on accuracy/cost. Design: balance with modest 32K-128K + retrieval for production agents handling codebases, docs, avoiding diminishing returns.

-----

-----

Phase: [EXPLOITATION]

### Source [11]: https://towardsai.net/p/machine-learning/the-context-window-paradox-engineering-trade-offs-in-modern-llm-architecture

Query: How do increasing LLM context window sizes to millions of tokens impact the trade-offs in compression, retrieval, and the overall design of agent memory systems?

Answer: Quadratic attention causes 4x context length to yield 16x memory, superlinear latency, prohibitive costs. 'Lost in the middle' (U-shaped accuracy) degrades middle retrieval due to positional encoding/attention entropy/training mismatch. For RAG/agent design, extended context enables multi-hop reasoning but demands boundary placement, positional diversity; naive max-use destroys economics. Empirical: 8K optimal for Llama 3.1 8B QA, diminishing returns beyond. Strategies: task-classify (context-sensitive vs robust), cost-quality calibration (min viable context), adaptive allocation (small for easy, expand for hard). Compression via quantization/Flash/PagedAttention alters curves. Multi-source RAG benefits more from expansion than single-source. Overall: dynamic resource allocation over fixed large windows for agent memory, prioritizing quality.

-----

-----

Phase: [EXPLOITATION]

### Source [12]: https://www.oajaiml.com/uploads/archivepdf/643561268.pdf

Query: How do increasing LLM context window sizes to millions of tokens impact the trade-offs in compression, retrieval, and the overall design of agent memory systems?

Answer: MCW (1M-10M tokens) vastly exceeds MECW; models degrade at 100-1000 tokens depending on task (needle-in-haystack best, sort/summarize worst), falling >99% short. RAG boosts accuracy under MECW but worsens hallucination/cascading agent failures beyond, as large contexts degrade performance. Agentic systems chaining large-context agents fail due to mediocre per-agent success (e.g., 70%^3=34%). Implications: limit tokens per task for near-100% accuracy; split agents into sub-agents with small scopes/contexts. Task-specific MECW shifts rankings, enabling cost-optimized model selection. Design: measure MECW for tasks, truncate/summarize to stay under, preventing RAG/agent degradation over relying on advertised MCW.

-----

</details>

<details>
<summary>What best practices help AI agents autonomously manage and consolidate conflicting memories from conversations without requiring users to manually edit or garden their memory stores?</summary>

Phase: [EXPLOITATION]

### Source [13]: https://medium.com/@nirdiamant21/memory-optimization-strategies-in-ai-agents-1f75f8180d54

Query: What best practices help AI agents autonomously manage and consolidate conflicting memories from conversations without requiring users to manually edit or garden their memory stores?

Answer: AI agents autonomously manage and consolidate conflicting memories through several strategies detailed in the article. Key methods include summarization, where after every 10 messages or when context gets too large, the AI creates a summary of earlier dialogue and discards detailed logs, distilling important points like key decisions and facts to maintain relevant information over long conversations without exceeding limits. Hierarchical memory systems automatically manage information across levels: working memory (immediate access), short-term (recent projects), and long-term (archives), promoting important details upward while letting trivial ones fade, mimicking a smart assistant that files or deletes emails. Compression and consolidation, inspired by human brain processes during sleep, involve converting text to embeddings, identifying patterns/clusters, hierarchical abstraction (e.g., specific event to general preference), importance scoring via attention mechanisms (favoring recent/frequently referenced/emotionally significant), lossy compression removing non-essential details, and reconstruction from compressed representations. This achieves dramatic space savings while preserving essentials. Strategic forgetting learns rules to remove completed task details or errors. Memory consolidation as background processes reinforces key information and discards noise. Graph-based memory networks organize information as interconnected knowledge graphs capturing relationships for contextual recall. Advanced techniques like token compression, smart filtering (scoring importance), dynamic allocation, and temporal awareness (weighting recent vs. long-term patterns) enable autonomous management without manual intervention. Hybrid approaches combine these for production use, automatically handling conflicts and redundancies.

-----

-----

Phase: [EXPLOITATION]

### Source [14]: https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/

Query: What best practices help AI agents autonomously manage and consolidate conflicting memories from conversations without requiring users to manually edit or garden their memory stores?

Answer: Amazon Bedrock AgentCore Memory provides autonomous management through a long-term memory pipeline with extraction, consolidation, and retrieval. Extraction uses LLMs to identify meaningful information from conversations into strategies like semantic memory (facts), user preferences (explicit/implicit), and summary memory (narratives), processing events with timestamps independently in parallel. Consolidation intelligently merges related info, resolves conflicts, minimizes redundancies: retrieves top semantically similar existing memories, uses LLM prompts to decide ADD (distinct), UPDATE (complements/updates), or NO-OP (redundant), prioritizing recency for contradictions (e.g., budget update marks old as INVALID, keeps audit trail). Handles out-of-order events, conflicts, failures with retries/backoff. Custom strategies allow tailored prompts/models. Best practices: choose strategies aligning with use case (semantic for facts, preferences for personalization, summarization for narratives); design namespaces for hierarchy/isolation (e.g., per-user/shared); monitor via APIs; plan for async processing using short-term memory meanwhile. Achieves 68-95% compression, low latency (20-40s extraction, 200ms retrieval), high correctness on benchmarks like LoCoMo/PrefEval, enabling coherent, up-to-date memory without manual edits.

-----

-----

Phase: [EXPLOITATION]

### Source [17]: https://www.usamaamjid.com/blog/building-autonomous-ai-agents-memory-systems-guide

Query: What best practices help AI agents autonomously manage and consolidate conflicting memories from conversations without requiring users to manually edit or garden their memory stores?

Answer: Autonomous agents use 5 memory types with autonomous consolidation: working (short-term context), episodic (vector-stored interactions with time-aware retrieval), semantic (knowledge base), procedural (workflow state in Redis/PostgreSQL), meta-memory (strategy outcomes for adaptation). Patterns: hybrid architecture (vector+structured), time-aware retrieval (semantic+recency decay), multi-index namespaces, versioning, pruning (age/importance policies), concurrent updates (optimistic locking), poisoning prevention (sanitization). Best practices: monitor quality/latency/relevance, graceful degradation, caching/batching, production stacks (Pinecone/Redis/pgvector per use case). Enables goal-directed, stateful, adaptive behavior across sessions without manual gardening, e.g., onboarding agent resumes state, recalls past attempts autonomously.

-----

</details>

<details>
<summary>What practical implementation patterns exist for creating and retrieving semantic, episodic, and procedural memories in agent systems using tools like Mem0?</summary>

Phase: [EXPLOITATION]

### Source [18]: https://techsy.io/blog/ai-agent-memory-guide

Query: What practical implementation patterns exist for creating and retrieving semantic, episodic, and procedural memories in agent systems using tools like Mem0?

Answer: The CoALA framework maps agent memory to cognitive science categories: working memory, episodic, semantic, and procedural. Mem0 supports all five memory types including semantic (facts, preferences), episodic (past interactions with timestamps), and procedural (learned behaviors, workflows). Storage: Vector DB for semantic/episodic, code/config for procedural, graph for relationships. Mem0 handles extraction, conflict resolution (recency + confirmation, UPDATE on contradiction), multi-backend storage. Retrieval combines semantic similarity, recency weighting, importance scoring. Example: m.add('I prefer TypeScript', user_id='dev_42'); results = m.search('What language?', user_id='dev_42'). Production patterns: Dual-layer (Redis hot cache for recent, Pinecone cold for full history); consolidation (summarization, deduplication, decay, archival); multi-agent isolation via agent_id + user_id namespaces. Anti-patterns: Store everything without filtering, no TTL/decay, ignoring conflicts (Mem0 resolves via UPDATE), treating all types same (separate storage/retrieval per type). Mem0 is default for semantic facts/preferences.

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://mem0.ai/blog/multi-agent-memory-systems

Query: What practical implementation patterns exist for creating and retrieving semantic, episodic, and procedural memories in agent systems using tools like Mem0?

Answer: Mem0 handles multi-agent memory via scoping: user_id (personal semantic/episodic), agent_id (agent-specific procedural), run_id (session), app_id (shared). Agents see only relevant memories, e.g., billing agent scoped to agent_id avoids support tickets. CoALA extends to multi-agent: long-term stores episodic (past experiences), semantic (facts), procedural (skills/code). Patterns: Centralized (shared store for small teams), distributed (private + sync), hybrid (Mem0's multi-level scoping). Mem0 uses vector for semantic search, key-value for exact, graph (Mem0g) for relationships. Scoped queries: m.add('data', user_id='u1', agent_id='billing'); retrieval filters by ids preventing pollution while sharing user-level context.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: What practical implementation patterns exist for creating and retrieving semantic, episodic, and procedural memories in agent systems using tools like Mem0?

Answer: Mem0 automates extraction/consolidation/storage/retrieval for semantic (facts/preferences, updated on contradiction), episodic (timestamped interactions), procedural (behaviors/workflows). Pipeline: LLM extracts facts from chat, consolidates (merge duplicates >0.85 sim, conflict resolution), stores in hybrid vector (1536D embeddings, HNSW) + graph (entities/edges for relations). Retrieval: Embed query, top-k=20, score=similarity × recency × type_weight (semantic 0.6, episodic 0.3, procedural 0.1), top-5 injected to prompt; hybrid reranking. Example: m.add('User likes Python', user_id='u123'); m.search('language pref', user_id='u123'). Benchmarks: 91% lower latency, 90% token savings vs full-context.

-----

-----

Phase: [EXPLOITATION]

### Source [21]: https://mem0.ai/blog/ai-memory-management-for-llms-and-agents

Query: What practical implementation patterns exist for creating and retrieving semantic, episodic, and procedural memories in agent systems using tools like Mem0?

Answer: Mem0 extracts discrete facts (semantic/episodic/procedural) via LLM, updates via ADD/UPDATE/DELETE/NOOP (resolves contradictions at write). Types: Semantic (user facts/preferences), episodic (events), procedural (workflows). Retrieval: Vector similarity + graph (Mem0g) for relations. Scoping: user_id, session_id, agent_id, run_id, org_id. Integration: LangGraph nodes for retrieve/store; tools (Mem0-remember/search, Mem0-memorize/add async). Forgetting: Relevance decay/prune low-score. Benchmarks: Mem0 66.9% acc, 1.44s p95 vs full-context 72.9% acc/17s p95, 93% token reduction.

-----

</details>

<details>
<summary>What are the key advantages and disadvantages of implementing AI agent long-term memory using raw unstructured text, structured entity formats like JSON, versus graph-based knowledge representations?</summary>

Phase: [EXPLOITATION]

### Source [23]: https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/

Query: What are the key advantages and disadvantages of implementing AI agent long-term memory using raw unstructured text, structured entity formats like JSON, versus graph-based knowledge representations?

Answer: AI Memory stores session history, user preferences, learned facts for multi-turn agents, personalization, continuity. Best for agentic workflows but can't retrieve broad document knowledge or explain relationships alone. Breaks if stored context is stale or inaccurate. RAG (raw unstructured text retrieval) stores document chunks and vector embeddings for knowledge-intensive Q&A, document lookup. High for document-heavy knowledge bases but can't persist context across sessions or reason across relationships. Breaks if indexed content is ungoverned or out of date. Knowledge Graph stores nodes (entities), edges (relationships), properties for multi-hop reasoning, relationship queries, structured inference. High for compliance, ontology, complex relationship domains but can't scale to unstructured corpora or handle user-specific state. Breaks if entity definitions and relationships not maintained. Production systems compose all three as each handles distinct jobs: RAG for broad retrieval, Memory for continuity, Graphs for structured reasoning. Governance dependency critical for all.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://sparkco.ai/blog/ai-agent-memory-in-2026-comparing-rag-vector-stores-and-graph-based-approaches

Query: What are the key advantages and disadvantages of implementing AI agent long-term memory using raw unstructured text, structured entity formats like JSON, versus graph-based knowledge representations?

Answer: RAG (raw unstructured text): Excels in small-footprint on-the-fly retrieval, dynamic unstructured data integration. Struggles with freshness issues, chunking inconsistency, poor multi-hop reasoning. Low indexing/storage; high inference compute. Vector Stores (structured like JSON embeddings): Semantic search, nearest-neighbor recall, large-scale similarity. Lacks explicit relationships, high-dimensional scaling, context loss from chunking. Moderate indexing compute; high storage for embeddings; linear query scaling. Graph-Based: Explicit relationships, multi-hop reasoning, structural inference. Struggles with scaling edges, complex joins, incomplete graph accuracy. High indexing for schema; elevated storage for relations; intensive traversal compute. Hybrids combine broad retrieval + detailed traversal, 80% accuracy boost, 35% precision gain but increased maintenance complexity. Decision: Vectors for conversational agents, RAG for ad-hoc retrieval, Graphs for compliance-heavy apps. Benchmarks show graphs excel in relations but higher latency/storage vs vectors' speed.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: What are the key advantages and disadvantages of implementing AI agent long-term memory using raw unstructured text, structured entity formats like JSON, versus graph-based knowledge representations?

Answer: Raw unstructured text (full-context prompting): Spikes costs/latency (200K tokens ~$1/call, 5-10s latency), unreliable (ignores mid-prompt info per Lost in the Middle study), no deduplication/timestamps. Vector Storage (structured embeddings): Semantic similarity, ANN search scales to millions (sub-50ms latency), fuzzy matching. Limitations: No relationships, struggles with multi-hop/structured dependencies. Graph Storage: Explicit relationships, traversal for entity disambiguation/dependencies. Requires schema design, edge weighting, lacks fuzzy semantics unless hybrid. Hybrid: Vector for fast retrieval + graph for relations (score fusion 0.7 vector + 0.3 graph), improves multi-hop. Benchmarks: Structured memory 91% lower latency, 90% token savings vs full-context. Production pipelines: Extract/consolidate raw convos, store in vectors/graphs/hybrids for personalization/continuity.

-----

-----

Phase: [EXPLOITATION]

### Source [26]: https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/

Query: What are the key advantages and disadvantages of implementing AI agent long-term memory using raw unstructured text, structured entity formats like JSON, versus graph-based knowledge representations?

Answer: Raw conversational data (RAG baseline/full history): High correctness on factual QA but 0% compression, struggles with preference inference. AgentCore Memory (structured extraction to JSON-like schemas): Semantic (facts), Preferences (structured prefs), Summary (narratives). Consolidation merges/updates/NO-OP redundants, resolves conflicts by recency. 89-95% compression, strong trade-offs (e.g., 79% pref correctness). Async extraction 20-40s, retrieval 200ms. Custom strategies override prompts/models. Self-managed for full control. Handles out-of-order/conflicts via timestamps/immutability. Production: High compression enables scale, better for inference tasks than raw data.

-----

-----

Phase: [EXPLOITATION]

### Source [27]: https://xtrace.ai/blog/rag-vs-long-term-memory-ai-agents

Query: What are the key advantages and disadvantages of implementing AI agent long-term memory using raw unstructured text, structured entity formats like JSON, versus graph-based knowledge representations?

Answer: Raw unstructured/RAG: Read-only/static, no updates (conflicts stack), semantic similarity not state, no temporal reasoning. Fails as memory: context pollution, loses narrative. Semantic Memory (immutable facts): RAG appropriate. Episodic (events): Vectors w/metadata/timestamps. Core State/User State (active truth): Structured store (SQL/graph/KV) for updates like prefs/task_status. Hybrid needed: No single store handles all. Memory lifecycle: Generation→Evolution→Archival (Zettelkasten-like). RAG for reading library, not writing autobiography.

-----

</details>

<details>
<summary>How do the dynamic interactions and retrieval pipelines between an LLM's parametric internal knowledge, volatile short-term context, and persistent external long-term storage enable effective agent personalization and continuity?</summary>

Phase: [EXPLOITATION]

### Source [28]: https://arxiv.org/html/2510.07925v1

Query: How do the dynamic interactions and retrieval pipelines between an LLM's parametric internal knowledge, volatile short-term context, and persistent external long-term storage enable effective agent personalization and continuity?

Answer: The framework integrates persistent memory modules and dynamic user profiles with agentic AI patterns to enable personalized long-term interactions in LLM-based agents. Parametric knowledge is the LLM's pretrained capabilities. Volatile short-term context is handled by Short-term Memory (STM) storing recent conversational exchanges as full-text dialogue. Persistent external long-term storage includes Long-term Memory (LTM) for historical user-specific data stored as embeddings retrieved via similarity search, summaries of past interactions, and dynamic user profiles capturing key facts like preferences, interests, personality traits, and conversational characteristics.

Dynamic interactions occur through a multi-agent workflow: Coordinator dynamically adapts retrieval strategies based on query complexity (Central Coordination pattern), forwarding simple queries directly or complex ones to Operator. Operator uses Planning and Multi-Source Retrieval patterns via Model Context Protocol (MCP) to access STM, LTM, summaries, user profile, and web search, autonomously selecting and identifying relevant content aligned with user context, preferences, and history. Self-Validator (Reflection pattern) checks sufficiency and consistency, refining retrieval iteratively. Response Generator tailors outputs using the user profile.

Retrieval pipelines are adaptive, not static: Operator flexibly invokes tools, ensuring user-centered responses. Persistent Memory pattern maintains continuity across sessions by storing, organizing, and retrieving user-specific information, evolving understanding of preferences, goals, and patterns. LTM uses LLM-synthesized concise summaries, tagging-based query expansion, embeddings, timestamps, and top-5 related memories with automatic updates to prevent outdated info.

This enables personalization (adaptivity via agentic workflow, consistency via memory modules, tailored responses via user profiles) and continuity (evolving memory across interactions), outperforming RAG baselines in retrieval accuracy and response correctness on datasets like GVD, LoCoMo, LongMemEval, with user study confirming perceived personalization from recall and context integration.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://mem0.ai/blog/ai-memory-management-for-llms-and-agents

Query: How do the dynamic interactions and retrieval pipelines between an LLM's parametric internal knowledge, volatile short-term context, and persistent external long-term storage enable effective agent personalization and continuity?

Answer: LLM's parametric internal knowledge is the pretrained model capabilities. Volatile short-term context is conversation memory (active context window with current system prompt, tool outputs, messages). Persistent external long-term storage is a hierarchy: session memory (task-specific context surviving turns within a session), user memory (durable facts like preferences, tools, projects, style for personalization), organizational memory (shared policies, knowledge bases).

Dynamic interactions use memory types: semantic (factual user knowledge for personalization), episodic (event-specific for continuity, e.g., 'you tried X last week'), procedural (workflows, patterns shaping behavior).

Retrieval pipelines: two-phase extraction-update. Extraction: LLM identifies discrete durable facts from conversations (deep processing for semantic units). Update: ADD new facts, UPDATE superseding ones, DELETE invalid, NOOP duplicates, preventing interference. Retrieval via vector similarity or graph-enhanced (Mem0g) for relational traversal (entities as nodes, relationships as edges), improving accuracy. Scoping (user_id, session_id, agent_id, etc.) ensures personalized retrieval.

Forgetting via relevance decay prunes stale entries. Hybrid agent/pipeline-driven: automatic retrieval at request start, agent-driven storage. Benchmarks show selective retrieval (66.9-68.4% accuracy, low latency/tokens) vs full-context (72.9%, high cost), enabling continuity without degradation, personalization via user-specific durable facts.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://dev.to/foxgem/architectural-strategies-for-external-knowledge-integration-in-llms-a-comparative-analysis-of-rag-23d6

Query: How do the dynamic interactions and retrieval pipelines between an LLM's parametric internal knowledge, volatile short-term context, and persistent external long-term storage enable effective agent personalization and continuity?

Answer: Parametric knowledge is LLM's static training data. Volatile short-term context is the prompt with retrieved/preloaded info. Persistent external storage is knowledge bases.

RAG: dynamic retrieval pipeline queries external base per user query, retrieves snippets prepended to prompt, conditioning generation on parametric + retrieved context. Advanced: hybrid search, re-ranking, query rewriting. Enables handling vast/dynamic data for timeliness/accuracy.

CAG: preloads knowledge into working memory (long prompt or KV cache pre-computing states), making it active memory without per-query retrieval. Lower latency post-setup, suits static data.

Dynamic interactions: RAG interweaves parametric with retrieved contextual knowledge dynamically; CAG integrates via direct context/cached states. Hybrid: RAG for dynamic parts, CAG for static, optimizing scalability/latency. Trade-offs enable personalization (tailored via relevant retrieval/preload) and continuity (persistent access to external knowledge complementing parametric).

-----

-----

Phase: [EXPLOITATION]

### Source [31]: https://www.letta.com/blog/agent-memory

Query: How do the dynamic interactions and retrieval pipelines between an LLM's parametric internal knowledge, volatile short-term context, and persistent external long-term storage enable effective agent personalization and continuity?

Answer: Parametric knowledge is LLM base. Volatile short-term: message buffer (recent messages). Persistent long-term: core memory (in-context blocks on user/org/task), recall (searchable history), archival (external DBs like vectors/graphs).

Dynamic interactions via context engineering: eviction/summarization (recursive for continuity), memory blocks (editable, pinned for user prefs/persona), retrieval (RAG-like but distinguished from true memory).

Retrieval pipelines: MemGPT-like hierarchy (core as RAM, archival/recall as disk), LLM-managed via function calls; sleep-time agents asynchronously refine blocks. Enables learning/adaptation: perpetual thread maintains flow, blocks evolve via updates/rewrites, external retrieval pulls relevant history. Personalization/continuity from stateful persistence across sessions, improving via experience without stateless resets.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://neurips.cc/virtual/2025/poster/119740

Query: How do the dynamic interactions and retrieval pipelines between an LLM's parametric internal knowledge, volatile short-term context, and persistent external long-term storage enable effective agent personalization and continuity?

Answer: RAG complements parametric knowledge (pretrained) with contextual (retrieved). Entity flow models forward propagation: traces how LLMs interweave mixed-source knowledge. Entity-aware probe detects ad-hoc entities in hidden layers via special tokens + LoRA, revealing mechanisms.

Attention heads route contextual vs parametric knowledge distinctly, with competition only within types. Conflicting knowledge persists residually; aligned accumulates, magnitude determining output influence. Enables effective reconciliation for accuracy/timeliness in personalization/continuity via dynamic internal integration of parametric/internal with retrieved/external knowledge.

-----

</details>

<details>
<summary>In what ways do semantic facts, timestamped episodic events, and encoded procedural workflows each contribute uniquely to an agent's ability to maintain empathy, temporal awareness, and reliable task execution across user interactions?</summary>

Phase: [EXPLOITATION]

### Source [34]: https://www.damiangalarza.com/posts/2026-02-17-how-ai-agents-remember-things/

Query: In what ways do semantic facts, timestamped episodic events, and encoded procedural workflows each contribute uniquely to an agent's ability to maintain empathy, temporal awareness, and reliable task execution across user interactions?

Answer: Semantic memory is facts and preferences like tech stack, coding style, project conventions, stable facts loaded into every prompt for consistent user understanding, supporting empathy through personalized knowledge of user details. Episodic memory covers events and interactions like past debugging sessions or recent context via daily logs and session snapshots, providing temporal awareness by recalling what happened in previous conversations with timestamps. Procedural memory is workflows and learned routines like deployment processes, testing patterns, PR review checklists, ensuring reliable task execution by remembering how to accomplish specific tasks consistently across interactions.

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://www.digitalocean.com/community/tutorials/episodic-memory-in-ai

Query: In what ways do semantic facts, timestamped episodic events, and encoded procedural workflows each contribute uniquely to an agent's ability to maintain empathy, temporal awareness, and reliable task execution across user interactions?

Answer: Semantic memory stores general factual knowledge like 'Paris is the capital of France', supporting empathy via user-specific facts without event context. Episodic memory contains personal experiences with contextual information such as time, enabling temporal awareness by recalling specific events like 'User X asked for tech support on Monday and was given solution Y'. Procedural memory encodes learned skills or actions like executing sequences (logging into email server), ensuring reliable task execution. Episodic memory retrieval via semantic search injects past events into reasoning for continuity across interactions, while short-term memory is limited to context window.

-----

-----

Phase: [EXPLOITATION]

### Source [36]: https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/

Query: In what ways do semantic facts, timestamped episodic events, and encoded procedural workflows each contribute uniquely to an agent's ability to maintain empathy, temporal awareness, and reliable task execution across user interactions?

Answer: Episodic memory captures experience-level knowledge including goal, reasoning steps, actions, outcomes, reflections, enabling agents to adapt across sessions for temporal awareness and reliable execution by recalling how similar problems were solved. Semantic memory remembers what the agent knows (facts), while episodic documents how it arrived there. Reflection module generates insights from past episodes for generalizable strategies, improving task execution. Benchmarks show episodic memory boosts success rates in multi-step tasks like retail/airline scenarios by avoiding mistakes and evolving planning.

-----

</details>

<details>
<summary>What real-world product design principles should AI engineers follow to select and evolve memory architectures based on whether building Q&A systems, personal companions, or automation agents rather than over-engineering complex setups?</summary>

Phase: [EXPLOITATION]

### Source [37]: https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/

Query: What real-world product design principles should AI engineers follow to select and evolve memory architectures based on whether building Q&A systems, personal companions, or automation agents rather than over-engineering complex setups?

Answer: The comparative data underscores a critical reality in AI engineering: there is no monolithic, universally superior solution for AI agent memory. Simple LangChain buffer memory suits early-stage MVPs and prototypes operating on 0-3 month timelines. Mem0 provides the most secure, feature-rich path for products requiring robust personalization and severe token-cost reduction with minimal infrastructural overhead. Zep serves enterprise environments where extreme sub-second retrieval speeds and complex ontological awareness justify the inherent complexity of managing graph databases. Finally, LangMem serves as the foundational, open-source toolkit for engineers prioritizing procedural autonomy and strict architectural sovereignty. With out-of-the-box SOC 2 and HIPAA compliance, Bring Your Own Key (BYOK) architecture, and support for air-gapped or Kubernetes on-premise deployments, Mem0 targets large-scale, high-security enterprise environments. It is particularly effective for customer support automation, persistent sales CRM agents managing long sales cycles, and personalized healthcare companions where secure, highly accurate, and long-term user tracking is paramount. Mem0 also uniquely features a Model Context Protocol (MCP) server, allowing for universal integration across almost any modern AI framework. It remains the safest, most feature-rich option for compliance-heavy, personalization-first applications. Modern AI agents treat the LLM as more than a text generator. They use it as the brain of a larger system, much like a CPU. Frameworks like CoALA separate the agent’s thinking process from its memory, treating memory as a structured system rather than just raw text. This means the agent actively retrieves, updates, and uses information instead of passively relying on past conversations. The decision to adopt an external memory framework hinges entirely on operational scale and application intent. Before you evaluate frameworks, you need to make one fundamental engineering assessment. If agents handle stateless, single-session tasks with no expected carryover, they do not need a memory overlay. Adding one only increases latency and architectural complexity. Conversely, if an agent operates repeatedly over related tasks, interacts with persistent entities (users, vendors, repositories), requires behavioral adaptation based on human corrections, or suffers from exorbitant token costs due to continuous context re-injection, a dedicated memory infrastructure is mandatory.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://arxiv.org/html/2503.12687v1

Query: What real-world product design principles should AI engineers follow to select and evolve memory architectures based on whether building Q&A systems, personal companions, or automation agents rather than over-engineering complex setups?

Answer: Cross-session personalization leverages memory systems to provide consistent and adaptive experiences across multiple interactions with the same user. This capability requires maintaining user-specific profiles that capture relevant preferences, history, and characteristics, and then using this information to tailor agent behavior appropriately. Effective personalization balances multiple considerations, including accuracy (correctly remembering user-specific information), appropriateness (using this information in ways that enhance rather than detract from the user experience), and privacy (maintaining appropriate boundaries around what information is stored and how it is used). As agent systems become more integrated into daily workflows and personal activities, sophisticated cross-session personalization becomes increasingly important for creating natural and effective user experiences. As interactions become more complex and extended, effective working memory becomes increasingly important for maintaining coherence and relevance in agent responses. The implementation of AI agent architectures continues to evolve rapidly, with new techniques and frameworks emerging regularly. Effective implementation requires careful consideration of the specific requirements and constraints of each application domain, including performance objectives, available data, computational resources, and integration requirements. As the field matures, standardized frameworks and best practices are emerging that simplify agent development and deployment across diverse contexts. Effective memory and context management represent critical challenges in AI agent architecture, particularly for systems designed to maintain coherent interactions over extended periods and across multiple sessions.

-----

-----

Phase: [EXPLOITATION]

### Source [39]: https://dev.to/bo_romir/two-kinds-of-ai-agents-and-why-you-need-both-3158

Query: What real-world product design principles should AI engineers follow to select and evolve memory architectures based on whether building Q&A systems, personal companions, or automation agents rather than over-engineering complex setups?

Answer: Anthropic's advice remains the sanity check: 'We recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.' Type 1: The Persistent Context Agent. This is an AI that lives alongside you. It has memory. It knows your codebase, your preferences, your ongoing projects, what happened yesterday. It accumulates context over time and uses that context to be more helpful. Examples: Karpathy described this paradigm in his 2025 review when discussing Claude Code: 'It runs on your computer and with your private environment, data and context... it's not just a website you go to like Google, it's a little spirit/ghost that 'lives' on your computer.' The key insight: the value of a Type 1 agent is proportional to the context it has accumulated. A fresh instance with no memory is dramatically less useful than one that has been running for weeks. Type 2: The Stateless Decision Function. This is an AI that receives structured input, makes one decision, and returns. No memory. No ongoing context. No personality. It runs identically the thousandth time as the first. Examples: Anthropic described this pattern in 'Building Effective Agents': 'For many applications, optimizing single LLM calls with retrieval and in-context examples is usually enough.' The key insight: the value of a Type 2 agent is proportional to its accuracy at volume. It doesn't need to remember anything. It needs to be right 97%+ of the time on the same input every time. The real insight: production systems usually need both types working together. Consider a fintech company processing loan applications. They need: A Type 1 agent that lives in their Slack, reads channels, tracks ongoing customer escalations, knows the team's history, understands each analyst's expertise, and can answer 'what's the status of Account X?' based on weeks of accumulated context. A Type 2 agent that processes 10,000 loan applications per day, making APPROVE/DENY/REVIEW decisions at 97% accuracy with a dollar-weighted scoring function.

-----

</details>

<details>
<summary>How might external memory management tools and systems need to adapt as LLMs potentially develop native continual learning abilities, and what interim role do they play in current AI engineering workflows?</summary>

Phase: [EXPLOITATION]

### Source [40]: https://medium.com/@ohquinton/continuous-learning-and-adaptive-architectures-in-future-llms-27517684dfd9

Query: How might external memory management tools and systems need to adapt as LLMs potentially develop native continual learning abilities, and what interim role do they play in current AI engineering workflows?

Answer: Large Language Models (LLMs) remain mostly static after initial training, unable to natively process knowledge beyond their training cutoff, leading to outdated responses. Researchers are exploring continuous learning techniques and adaptive memory architectures to enable dynamic updates without full retraining. Adaptive memory architectures allow models to pull new information from external knowledge sources in real-time without modifying core weights. Retrieval-Augmented Generation (RAG) enables querying external databases for relevant information to enhance responses. Memory-augmented networks (MANNs) support dynamic storage and recall, allowing AI assistants to learn user preferences and refine responses over time. Continuous caching of activations retains recent states for future predictions. These external memory tools currently provide context and knowledge beyond static training, enabling models to stay up-to-date and adapt to specialized domains. As LLMs develop native continual learning, external memory systems will evolve to complement internal updates, serving as interim bridges for real-time knowledge integration in AI workflows while addressing challenges like catastrophic forgetting through techniques such as Elastic Weight Consolidation (EWC), experience replay, and parameter isolation like LoRA adapters. Companies like OpenAI and Google use external sources via plugins to maintain currency without retraining base models.

-----

-----

Phase: [EXPLOITATION]

### Source [42]: https://arxiv.org/html/2604.08224v1

Query: How might external memory management tools and systems need to adapt as LLMs potentially develop native continual learning abilities, and what interim role do they play in current AI engineering workflows?

Answer: Externalization in LLM agents involves memory systems decoupling state across time from transient context, storing task state, past experiences, abstracted knowledge, and persistent context. Memory architectures evolve from monolithic context to retrieval storage, hierarchical orchestration, and adaptive systems with dynamic modules like MemEvolve and MemVerse that distill experience into abstract knowledge. In the Harness era, capability extends to persistent infrastructure including external memory stores essential for reliability. Memory demands increase as systems rely on external stores for continuity. As LLMs develop native continual learning, external memory tools must adapt to integrate with self-updating models, potentially serving as buffers for consolidation during 'sleep' cycles or handling multi-modal data. Currently, they play an interim role in AI engineering workflows by externalizing state persistence, enabling long-horizon interactions, and transforming recall into recognition, crucial until native learning matures.

-----

-----

Phase: [EXPLOITATION]

### Source [43]: https://atlan.com/know/ai-memory-system/

Query: How might external memory management tools and systems need to adapt as LLMs potentially develop native continual learning abilities, and what interim role do they play in current AI engineering workflows?

Answer: AI memory systems are external infrastructure enabling agents to recall interactions and context across sessions, addressing LLMs' statelessness. Four types: working (context window), episodic (interaction logs), semantic (facts), procedural (workflows). Without memory, performance drops 39% in multi-turn tasks; 37% multi-agent failures from inconsistent state. Tools like Mem0, Zep provide storage/retrieval, but enterprise gaps include source-of-truth issues. As LLMs gain native continual learning, external memory must adapt for governed inputs, provenance, and shared-state consistency, evolving from retrieval-focused to input-governed layers. Interim role: bridge stateless LLMs in workflows, providing persistence until native abilities mature, reducing cold-start costs and enabling multi-turn reliability.

-----

-----

Phase: [EXPLOITATION]

### Source [44]: https://www.cognee.ai/blog/fundamentals/llm-memory-cognitive-architectures-with-ai

Query: How might external memory management tools and systems need to adapt as LLMs potentially develop native continual learning abilities, and what interim role do they play in current AI engineering workflows?

Answer: LLM memory architectures include short-term (context window) and long-term (external vector/graph databases) to retain context beyond sessions. External memory enables context-rich responses, reduces hallucinations via RAG, efficient data handling. Challenges: data engineering, scaling, privacy. As LLMs develop native continual learning mimicking human LTM, external tools adapt by integrating with self-evolving systems, using graph-based storage for semantic reasoning. Interim role: provide persistence in current workflows, enabling multi-turn interactions and personalization until native memory matures, crucial for production-ready AI.

-----

</details>

<details>
<summary>How does the 'lost in the middle' phenomenon specifically degrade agent performance when depending on extended uncurated conversation histories within limited context windows?</summary>

Phase: [EXPLOITATION]

### Source [45]: https://towardsdatascience.com/deep-dive-into-context-engineering-for-ai-agents/

Query: How does the 'lost in the middle' phenomenon specifically degrade agent performance when depending on extended uncurated conversation histories within limited context windows?

Answer: Context rot is a situation where an LLM’s performance degrades as the context window fills up, even if it is within the established limit. The LLM still has room to read more, but its reasoning starts to blur. The effective context window, where the model performs at high quality, is often much smaller than what the model technically is capable of. A model does not maintain perfect recall across its entire context window. Information at the start and the end is more reliably recalled than things in the middle. This relates to the 'lost in the middle' phenomenon. Larger context windows do not solve problems for enterprise systems with unbounded data. Every new token depletes attention budget due to transformer architecture's n² interaction pattern, spreading attention thinner. In agent systems depending on extended uncurated conversation histories, this leads to poor recall and reasoning on middle information in long histories, causing context rot. Solutions include context compaction: summarizing contents and reinitiating a new context window when nearing limit, useful for long-running tasks. Context folding allows agents to manage working context by branching subtasks and folding summaries. Context engineering techniques like offloading, retrieval, isolation, and reduction mitigate degradation in agents with limited context windows.

-----

-----

Phase: [EXPLOITATION]

### Source [46]: https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e

Query: How does the 'lost in the middle' phenomenon specifically degrade agent performance when depending on extended uncurated conversation histories within limited context windows?

Answer: In the paper Lost in the Middle: How Language Models Use Long Contexts, researchers demonstrated that LLM performance significantly degrades when relevant information is located in the middle of a long input. Models are biased toward the beginning (primacy) and end (recency) of a prompt. By cramming an agent’s context with thousands of tokens from extended histories and instructions, it becomes hard for the agent to access specified information. Adding instructions to fix issues increases cognitive load, making further errors more likely. This is compounded in uncurated conversation histories that flood the context. Instructional overhead gets lost, leading the agent to hallucinate, fail validation checks, or enter 'whatever' mode. In agents depending on extended uncurated histories within limited windows, performance degrades as key info sinks into the middle, causing misbehavior, hallucinations, and outright failures as context grows.

-----

-----

Phase: [EXPLOITATION]

### Source [47]: https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf

Query: How does the 'lost in the middle' phenomenon specifically degrade agent performance when depending on extended uncurated conversation histories within limited context windows?

Answer: The 'lost in the middle' phenomenon shows models perform best on relevant information at the beginning (primacy bias) or end (recency bias) of long contexts, with degraded performance when accessing middle information. In multi-document QA, performance drops over 20% (e.g., GPT-3.5-Turbo below closed-book 56.1%) when relevant docs are in the middle of 20-30 docs (~4K-6K tokens). U-shaped curve: highest accuracy at start/end positions, rapid degradation in middle. Extended-context models not better at using context. In key-value retrieval, similar U-shape; models struggle retrieving middle pairs. For agents with extended uncurated histories in limited windows, this means poor reasoning over full history; middle conversation turns/instructions ignored, leading to failures in tasks like retrieval-augmented generation mimicking agentic setups with long histories. Open-domain QA case: performance saturates before retriever recall, failing to use extra context effectively. Indicates agents cannot robustly reason over entire window, degrading performance on history-dependent tasks.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://www.producttalk.org/context-rot/?srsltid=AfmBOor-dJyg-7naL653qE6-5TXcoSsKueKN_iSwQSe5ZnjW9S5GaWZj

Query: How does the 'lost in the middle' phenomenon specifically degrade agent performance when depending on extended uncurated conversation histories within limited context windows?

Answer: Context rot, from 'Lost in the Middle' paper, causes performance degradation as context fills: models favor start/end tokens, losing middle ones when <50% full; >50% full, loses earliest tokens (recency bias). In extended uncurated conversation histories, AI gets worse over time: ignores rules/instructions buried in middle/early history, hallucinates, fails tasks. Agents in chats (e.g., Replit, ChatGPT, Claude) cycle errors as history grows, resorting to suboptimal behavior. Limited windows exacerbate; even large ones fill quickly with histories, causing rot. Degrades agent performance by blurring reasoning, losing key context from histories, leading to ignored instructions and poor outputs in long interactions.

-----

</details>

<details>
<summary>What criteria should guide the selection of time-scale granularity when grouping episodic memories into conversation-level, daily, or weekly summaries for different agent applications?</summary>

Phase: [EXPLOITATION]

### Source [49]: https://www.centron.de/en/tutorial/episodic-memory-in-ai-agents-long-term-context-learning/

Query: What criteria should guide the selection of time-scale granularity when grouping episodic memories into conversation-level, daily, or weekly summaries for different agent applications?

Answer: In maintaining and pruning episodic memory, the source recommends 'Summarization: Store recent episodes in full detail while compressing older memories into condensed summaries. For example, a long conversation from a year ago may be reduced into a short record of the most important points.' This implies criteria for time-scale granularity: retain detailed episodic memories for recent events (e.g., conversation-level for immediate interactions) and group/summarize into coarser scales like daily or weekly for older ones to manage efficiency, storage, and relevance. Time-based decay assigns 'age score' to gradually remove outdated memories unless frequently retrieved, guiding selection based on recency and retrieval frequency. Relevance-based retention keeps high-impact episodes detailed longer. This supports applications needing personalization and continuity across conversations by balancing detail for recent vs. compression for historical data.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/episodic-memory-strategy.html

Query: What criteria should guide the selection of time-scale granularity when grouping episodic memories into conversation-level, daily, or weekly summaries for different agent applications?

Answer: Episodic memory captures meaningful slices of interactions at the episode level, generated only upon detecting completed episodes (e.g., conversation-level slices like a code deployment or appointment rescheduling). Namespaces define granularity: strategy-level `{` for cross-session/actor episodes; actor-level `{{` for user-specific across sessions; session-level `{{{` for single conversation. Reflections span episodes at matching or less nested levels (e.g., actor or strategy). Use for scenarios where sequence of past interactions improves quality, like customer support, workflows, code assistants needing session history. Retrieval indexed by 'intent' for episodes, 'use case' for reflections. Ideal for long-term improvement in complex tasks; for short tasks, session summaries suffice. Criteria: task complexity (detailed episodes for multi-turn goals), interaction span (session/actor/strategy granularity), and application needs (continuity vs. efficiency).

-----

-----

Phase: [EXPLOITATION]

### Source [51]: https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/

Query: What criteria should guide the selection of time-scale granularity when grouping episodic memories into conversation-level, daily, or weekly summaries for different agent applications?

Answer: Episodic memory benefits complex, multi-step tasks (e.g., debugging, planning) and repetitive workflows where past experience improves outcomes; skip for simple one-time questions (weather, facts) or short tasks where session summary suffices. True value over time: detailed episodes for similar specific problems (step-by-step examples), reflections for strategic guidance across contexts. Episode extraction at turn-level (granular) and episode-level (complete journeys spanning turns). Use episodes for structured workflows (e.g., airline procedures), reflections for open-ended scenarios (customer service). Before tasks, retrieve reflections for strategy, episodes for patterns; during tasks, episodes for roadblocks. Criteria: task complexity (detailed for complex/multi-step), duration/frequency (long-term/repetitive need episodes/reflections), domain (concrete examples for rule-based, insights for diverse patterns), and performance gains (e.g., +11-13% in benchmarks for retail/airline over baseline).

-----

-----

Phase: [EXPLOITATION]

### Source [52]: https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/

Query: What criteria should guide the selection of time-scale granularity when grouping episodic memories into conversation-level, daily, or weekly summaries for different agent applications?

Answer: Episodic memory stores detailed, time-based records of past interactions (conversation logs, tool usage) with timestamps for continuity across sessions. Short-term: recent/immediate (conversation-level). Long-term: tripartite model distinguishes episodic (sequential events) from semantic/procedural. Asynchronous consolidation moves raw episodic history to long-term after sessions. Intelligent forgetting uses TTL tiers (infinite for critical facts, short for transient), decay rates, refresh-on-read. Criteria for granularity: recency (hot/warm/cold tiers: full detail recent, compressed archival old), importance (high-value detailed, low decays fast), operational temperature (immediate hot path vs. background cold archive). Multi-database for patterns: time-series for episodic (relational with partitioning). Balances detail, efficiency for long-term tasks avoiding drift.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://www.geeksforgeeks.org/artificial-intelligence/episodic-memory-in-ai-agents/

Query: What criteria should guide the selection of time-scale granularity when grouping episodic memories into conversation-level, daily, or weekly summaries for different agent applications?

Answer: Episodic memory encoding decides when/what to record (after actions, state changes, rare events) for episodes at granular levels. Storage organizes by time/content similarity for scalable retention. Applications: robotics (navigation paths), conversational AI (dialogue history beyond turns), autonomous vehicles (driving conditions). Balance detail richness, storage efficiency, retrieval speed. Selective storage filters significant/novel experiences. Challenges: determining important experiences without overload, scaling to millions of episodes. Implies criteria: event significance (rare/impactful detailed), time organization (recent conversation-level vs. aggregated historical), application (continuity needs finer granularity for conversations, coarser for long-term planning).

-----

</details>

<details>
<summary>How can procedural memory systems enable agents to encode and reuse both successful and failed multi-step workflows as dynamic playbooks or functions?</summary>

Phase: [EXPLOITATION]

### Source [54]: https://www.oreilly.com/radar/why-multi-agent-systems-need-memory-engineering/

Query: How can procedural memory systems enable agents to encode and reuse both successful and failed multi-step workflows as dynamic playbooks or functions?

Answer: Procedural memory encodes how to do things—learned workflows, tool usage patterns, successful strategies that agents can reuse. In the memory taxonomy for multi-agent systems, procedural memory is distinguished from other types like working memory (transient state), episodic memory (task histories for debugging and learning), semantic memory (durable facts), and shared memory (for coordination across agents). This taxonomy ensures different retention, retrieval, and consistency needs are met. Procedural memory supports efficient task execution and continual learning by capturing learned procedures from past executions, allowing agents to reuse successful strategies rather than relearning them. While the source primarily discusses successful strategies, the broader memory engineering context implies encoding both successful and failed workflows via episodic memory integration, enabling learning from past executions including failures for refinement. The article emphasizes that without proper memory engineering, agents duplicate work and diverge, but procedural memory provides reusable playbooks for coordination.

-----

-----

Phase: [EXPLOITATION]

### Source [55]: https://arxiv.org/html/2508.06433v2

Query: How can procedural memory systems enable agents to encode and reuse both successful and failed multi-step workflows as dynamic playbooks or functions?

Answer: Mem^p introduces a task-agnostic framework elevating procedural memory as a core optimization target for LLM-based agents. It distills past agent trajectories into fine-grained step-by-step instructions and higher-level script-like abstractions, enabling encoding and reuse of experiences across long-horizon tasks. The framework systematically studies strategies for memory construction (full trajectories, scripts, proceduralization combining both), retrieval (query-vector matching, keyword-vector matching like AveFact), and updating (addition, validation filtering for successes only, reflection for error correction, dynamic discarding). This allows agents to learn from both successful and failed workflows: successful trajectories are stored as reusable templates (patterns of reasoning, tool sequences, recovery tactics); failures trigger updates like adjustment (combining erroneous trajectory with original memory for revision) or reflexion-based refinement. Empirical results on ALFWorld (housework) and TravelPlanner show boosted success rates (e.g., GPT-4o from 42% to 78% test success), efficiency (steps reduced from 24 to 15), continual learning (linear mastery over test tasks), and transferability (strong model memory boosts weaker ones). Update mechanisms like reflexion outperform vanilla appending, enabling self-improving agents that refine playbooks dynamically.

-----

-----

Phase: [EXPLOITATION]

### Source [56]: https://www.linkedin.com/posts/raphaelmansuy_memp-exploring-agent-procedural-memory-activity-7360498052685537280-57cd

Query: How can procedural memory systems enable agents to encode and reuse both successful and failed multi-step workflows as dynamic playbooks or functions?

Answer: MemP framework distills past successes into reusable formats: step-by-step playbooks (e.g., 'First check hotel availability, then optimize flights') and generalized scripts (principles for resolving constraints). This enables agents to retrieve relevant strategies for new tasks, avoid redundant trial-and-error, and correct faulty procedures through experience. Memory lifecycle: Build extracts from successful trajectories, balancing concrete examples (microwave egg-heating steps) with abstract rules; Retrieve uses semantic search (e.g., 'ship fragile items' triggers packing practices); Update refines via validation (keep working strategies), error correction (rewrite failures), pruning (discard outdated). Key findings: 50% step reduction on ALFWorld, linear accuracy improvement as memory matures, transfer from GPT-4o to smaller models. While focused on successes, update mechanisms incorporate failures for correction, turning both into dynamic playbooks for smarter execution.

-----

</details>

<details>
<summary>What engineering trade-offs emerge when balancing raw conversational logs as ground truth against compressed semantic or episodic extracts in production memory pipelines?</summary>

Phase: [EXPLOITATION]

### Source [57]: https://arxiv.org/html/2604.04853v1

Query: What engineering trade-offs emerge when balancing raw conversational logs as ground truth against compressed semantic or episodic extracts in production memory pipelines?

Answer: MemMachine’s approach—STM summary plus selectively retrieved raw episodes—provides a different tradeoff: the summary gives high-level context, while retrieved episodes supply uncompressed factual grounding. This is particularly important for use cases requiring auditability, compliance, or multi-hop reasoning over exact conversational records. A recurring design question is whether to provide the LLM with a summary of past interactions, the full conversational context, or a compressed intermediate form. Our findings, together with recent work on observational memory, suggest that each approach occupies a distinct point in the design space: Full context overwhelms the model, triggers the “lost in the middle” effect, and becomes infeasible as history grows beyond context limits. Summary-only approaches (compaction) lose critical detail, particularly for factual and temporal queries where the exact wording or timing matters. As Mastra’s research notes, compaction produces “documentation-style summaries” that “strip out the specific decisions and tool interactions agents need.” Compressed observations (Mastra) offer a middle ground: event-based logs that preserve structure while achieving 3–40× compression. This enables prompt caching and stable context windows but sacrifices the ability to retrieve original episodes on demand. These diverse approaches highlight a fundamental design tension in agent memory: compression vs. preservation. Systems that aggressively compress (Mastra, Mem0) achieve smaller context windows and lower per-query cost but risk losing critical detail. Systems that preserve raw data (MemMachine) maintain factual integrity at the cost of requiring efficient retrieval mechanisms. A related tension exists between retrieval-based approaches (MemMachine, Mem0, Zep) that search selectively and context-based approaches (Mastra) that keep compressed history always in context.

-----

-----

Phase: [EXPLOITATION]

### Source [58]: https://arxiv.org/pdf/2604.04853

Query: What engineering trade-offs emerge when balancing raw conversational logs as ground truth against compressed semantic or episodic extracts in production memory pipelines?

Answer: MemMachine’s approach—STM summary plus selectively retrieved raw episodes—provides a different tradeoff: the summary gives high-level context, while retrieved episodes supply uncompressed factual grounding. This is particularly important for use cases requiring auditability, compliance, or multi-hop reasoning over exact conversational records. A recurring design question is whether to provide the LLM with a summary of past interactions, the full conversational context, or a compressed intermediate form. Our findings, together with recent work on observational memory, suggest that each approach occupies a distinct point in the design space: Full context overwhelms the model, triggers the “lost in the middle” effect, and becomes infeasible as history grows beyond context limits. Summary-only approaches (compaction) lose critical detail, particularly for factual and temporal queries where the exact wording or timing matters. As Mastra’s research notes, compaction produces “documentation-style summaries” that “strip out the specific decisions and tool interactions agents need.” Compressed observations (Mastra) offer a middle ground: event-based logs that preserve structure while achieving 3–40× compression. This enables prompt caching and stable context windows but sacrifices the ability to retrieve original episodes on demand.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://www.elastic.co/what-is/context-engineering

Query: What engineering trade-offs emerge when balancing raw conversational logs as ground truth against compressed semantic or episodic extracts in production memory pipelines?

Answer: Effective context engineering requires active memory management strategies. Summarization compresses older exchanges into concise representations while preserving key facts and decisions. Windowing keeps only the most recent N messages, discarding earlier history under the assumption that recent context matters most. Selective retention applies heuristics to identify and preserve critical information (user preferences, established facts, open questions) while pruning routine conversational filler. More sophisticated approaches use episodic memory structures where the agent writes an important state to external storage and retrieves it on demand, mimicking how humans don't hold entire conversations in active working memory but can recall specific details when needed. The challenge is maintaining coherence; overly aggressive pruning causes the agent to "forget" key context and repeat mistakes, while insufficient compression leads to context overflow and performance degradation.

-----

</details>

<details>
<summary>How should memory architecture choices align with core product goals to avoid over-engineering when developing Q&A bots, personal companions, or task automation agents?</summary>

Phase: [EXPLOITATION]

### Source [61]: https://dev.to/tlrag/devto-article-the-architecture-that-could-redefine-ai-memory-and-agency-27e

Query: How should memory architecture choices align with core product goals to avoid over-engineering when developing Q&A bots, personal companions, or task automation agents?

Answer: Instead of treating the LLM as a disposable Q&A engine, I imagined it with two new components: a persistent core identity and an evolving long-term memory. In other words, give it a self and a memory. The AI’s core personality, values, and style would be saved as an ever-present “Heart” file. And every new piece of important information would go into a growing knowledge base that the AI can draw from later. No more forgetting past interactions – they’d be indexed and at the AI’s fingertips when relevant. Imagine a future where you have a personal AI that has been with you for years. It might have started on GPT-4 and years later run on GPT-7, but it’s the same companion because it carries its memory and identity forward. It knows your history, it grows with your career, it witnesses your life milestones, and it adapts to your changing needs. Such an AI could be an incredible force: a teacher that tracks your progress year over year, a therapist that actually recalls your past sessions in detail, a creative partner that builds on every brainstorm you’ve ever had together. Of course, it would also raise new challenges: how do we ensure privacy, how do we avoid bias in what it remembers, how do we keep its goals aligned with ours as it grows more autonomous? These are big questions—but we won’t even start to answer them if we stick with stateless AI that forgets by design.

-----

-----

Phase: [EXPLOITATION]

### Source [62]: https://www.exabeam.com/explainers/agentic-ai/agentic-ai-architecture-types-components-best-practices/

Query: How should memory architecture choices align with core product goals to avoid over-engineering when developing Q&A bots, personal companions, or task automation agents?

Answer: Memory design should be a deliberate process in agentic AI engineering. Developers need to determine what information each agent should remember, how this memory is structured, and the mechanisms for retrieval and forgetting. Proper memory management is essential for context retention, continual learning, and effective personalization. This often involves separating working memory for immediate context from long-term memory for accumulated knowledge and experience. Well-engineered memory systems support tasks like conversation, sequential decision-making, and knowledge transfer across sessions or environments. They also enable error correction and reflective reasoning, as agents can audit or learn from past outcomes. A well-designed agentic AI begins with a clear articulation of its goals, operational scope, and the guardrails that define acceptable behavior. Developers must specify what the system should accomplish, its boundaries, and its constraints before diving into implementation. Explicit objectives guide architectural choices, including what data to collect, what reasoning strategies to employ, and how to measure success. Guardrails ensure safety, compliance, and ethical operation. Defining clear scopes and constraints helps prevent over-engineering and mission creep.

-----

-----

Phase: [EXPLOITATION]

### Source [63]: https://productschool.com/blog/artificial-intelligence/ai-agent-orchestration-patterns

Query: How should memory architecture choices align with core product goals to avoid over-engineering when developing Q&A bots, personal companions, or task automation agents?

Answer: There’s no “best” orchestration pattern. There’s only “best for your product, your risk profile, and your users’ patience.” Here’s how to pick without overengineering. Match the pattern to task complexity: If the task is simple and repeatable, keep orchestration simple. A lot of product teams reach for multi-agent designs when the real need is just good tool use and a clean flow. If the task is messy, multi-step, and requires decisions along the way, that’s when planner–executor loops or hierarchical decomposition start paying for themselves. A good gut check: if a human would naturally break the work into phases, your system probably should too. Decide how much speed you can afford to lose. Design cost before you ship, not after you scale. Treat safety as a product requirement, not a feature. Instrument the system like it’s a product, not a demo. Keep the architecture modular so you can change it later.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ai-memory-vs-rag-vs-knowledge-graph-enterprise-guide-2026.md">
<details>
<summary>AI Memory vs RAG vs Knowledge Graph: Enterprise Guide 2026</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/>

# AI Memory vs RAG vs Knowledge Graph: Enterprise Guide 2026

## Key takeaways

- AI memory, RAG, and knowledge graphs are architecture layers, not alternatives
- Every production AI system composes all three in a stack
- The failure mode is never which component you chose
- What governs the data underneath all three determines accuracy

## What is the difference between AI memory, RAG, and knowledge graphs?

Copy summary

AI memory, RAG, and knowledge graphs are not alternatives to pick between — they are three distinct layers of the same context stack. RAG retrieves documents at query time; memory persists context across sessions; knowledge graphs store entities and explicit relationships for multi-hop reasoning. Production AI systems compose all three, and the failure mode is almost never the choice of component but the quality of governed data underneath.

### Each component handles a distinct job in the context stack

- RAG retrieves relevant document chunks at query time — stateless, breadth-first, document-oriented
- AI Memory persists context across turns and sessions — enables continuity, personalization, and agent history
- Knowledge Graph stores entities and explicit relationships — depth-first, powers multi-hop and structured reasoning
- Composition pattern — all three serve different jobs in the same stack; using only one leaves capability gaps
- The real question — not which component to pick, but what governs the data flowing into all of them

Most enterprise AI teams arrive at this question the same way. They built a RAG pipeline, hit a ceiling, and are now evaluating whether to add memory, a knowledge graph, or both. The question feels like a selection problem: “which one is right for our use case?” It isn’t.

Production AI systems don’t choose between these three. They use all of them. Each one handles a different job in the same context stack:

- **RAG (retrieval-augmented generation):** retrieves relevant document chunks at query time from an external index. Stateless, breadth-first, document-oriented. The standard starting point for enterprise AI.
- **AI memory:** persists context across turns and sessions. Enables continuity, personalization, and agent history. Addresses the fundamental problem that [LLMs are stateless by design](https://atlan.com/know/are-llms-stateless/).
- **Knowledge graph:** stores entities and their explicit relationships for structured, multi-hop reasoning. Depth-first, relationship-oriented. Where graphs and RAG meet, [GraphRAG](https://atlan.com/know/what-is-graphrag/) improves precision up to 35% over vector-only retrieval.
- **The composition pattern:** all three serve different jobs in the same context stack. Using only one leaves capability gaps the others would fill.
- **The real question:** not which component to pick, but what governs the data flowing into all of them. Stale, ungoverned data breaks RAG, memory, and knowledge graphs simultaneously.

The comparison table below shows how each component differs. Below that, we cover: what each component does in depth, how they compose in production, when to prioritize each, and why the governed data layer underneath all three determines whether they work.

* * *

| | **AI Memory** | **RAG** | **Knowledge Graph** |
| --- | --- | --- | --- |
| **What it is** | Stateful context persistence across sessions | Stateless retrieval of relevant documents at query time | Structured store of entities and relationships |
| **What it stores** | Session history, user preferences, learned facts | Document chunks and vector embeddings | Nodes (entities), edges (relationships), and properties |
| **Best for** | Multi-turn agents, personalization, continuity | Knowledge-intensive Q&A, document lookup, citation-heavy responses | Multi-hop reasoning, relationship queries, structured inference |
| **What it can’t do alone** | Retrieve broad document knowledge or explain relationships | Persist context across sessions or reason across relationships | Scale to unstructured corpora or handle user-specific state |
| **Enterprise fit** | High for agentic and recurring workflows | High for document-heavy knowledge bases | High for compliance, ontology, and complex relationship domains |
| **Governance dependency** | Breaks if stored context is stale or inaccurate | Breaks if indexed content is ungoverned or out of date | Breaks if entity definitions and relationships are not maintained |

* * *

## What is AI memory in enterprise AI?

[Permalink to “What is AI memory in enterprise AI?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#what-is-ai-memory-in-enterprise-ai)

LLMs have no persistent state. Every inference call begins from zero: no record of prior sessions, no knowledge of what a user asked last week, no continuity between tasks. This is the [LLM statelessness problem](https://atlan.com/know/are-llms-stateless/), and it is why AI memory exists as a distinct architectural layer.

AI memory is the mechanism that gives LLM-based agents continuity across turns, sessions, and tasks by externalizing state into persistent storage outside the model.

### 1\. How LLM memory works

[Permalink to “1. How LLM memory works”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-how-llm-memory-works)

In-context memory is the information held in the model’s active context window. It is temporary: it lasts for one session and disappears when the session ends. External memory systems address this by persisting state outside the model and injecting relevant context at inference time. The three tiers are: in-context (working memory during a session), external short-term (session state in a vector store), and external long-term (persisted facts, preferences, and task history across sessions).

### 2\. Types of memory in production agents

[Permalink to “2. Types of memory in production agents”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-types-of-memory-in-production-agents)

Most production memory systems combine all three tiers based on what the agent needs to recall:

- **In-context memory** handles the current turn: what was said, what was decided, what step comes next
- **External short-term memory** persists the session state so a multi-step workflow can resume after interruption
- **External long-term memory** retains learned facts, user preferences, and prior task outcomes so recurring agents don’t re-start from scratch

[Observational memory scored 84.23% on the LongMemEval benchmark versus RAG’s 80.05% (GPT-4o)](https://machinelearningmastery.com/vector-databases-vs-graph-rag-for-agent-memory-when-to-use-which/), while cutting token costs up to 10x through prompt caching. The benchmark tests continuity-heavy tasks specifically, which is why memory outperforms retrieval on those scenarios. The two are complementary, not interchangeable.

### 3\. Where memory breaks in enterprise

[Permalink to “3. Where memory breaks in enterprise”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-where-memory-breaks-in-enterprise)

Memory systems degrade when what they’ve stored is no longer accurate. An agent that learned a user’s workflow preferences six months ago will act on stale context. An agent that cached a data classification from a governance review that has since changed will surface incorrect information. Active metadata platforms like Atlan maintain continuously refreshed context graphs that enterprise memory systems can draw from, keeping agent context current without manual intervention. For the architecture specifics of how memory and vector databases differ, see [agentic AI memory vs vector database](https://atlan.com/know/agentic-ai-memory-vs-vector-database/).

* * *

## What is RAG and why teams start here

[Permalink to “What is RAG and why teams start here”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#what-is-rag-and-why-teams-start-here)

RAG augments LLM inference by retrieving relevant document chunks from an external index at query time. The model receives both its pretrained knowledge and the retrieved context. The result is grounded, citation-capable responses without fine-tuning the model on new data.

Teams start with RAG for a practical reason: the entry cost is lower than memory or knowledge graphs. Index your documents, run similarity search, pass top-k chunks to the LLM. For knowledge-intensive Q&A, document lookup, and single-turn queries, RAG works well.

### 1\. How RAG works

[Permalink to “1. How RAG works”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-how-rag-works)

The pipeline has three stages. Documents are chunked and embedded into a vector index at ingest time. At query time, the user’s query is embedded and matched against the index via similarity search. The top-k most similar chunks are retrieved and passed to the LLM alongside the query. The LLM generates a response grounded in those chunks. This is the standard retrieval-augmented generation loop.

### 2\. Why RAG is the enterprise starting point

[Permalink to “2. Why RAG is the enterprise starting point”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-why-rag-is-the-enterprise-starting-point)

Three properties make RAG the default first step for enterprise AI:

- **No model retraining required:** new documents update the index, not the model weights
- **Broad coverage:** any text corpus can be indexed and retrieved against
- **Citation-friendly:** responses can be traced to specific source chunks

[The RAG market was estimated at $1.94 billion in 2025 and is projected to hit $9.86 billion by 2030 at a 38.4% CAGR](https://www.marketsandmarkets.com/Market-Reports/retrieval-augmented-generation-rag-market-135976317.html), making it the largest single component in the enterprise AI context stack today.

### 3\. Where RAG hits its ceiling

[Permalink to “3. Where RAG hits its ceiling”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-where-rag-hits-its-ceiling)

Standard vector RAG fails on multi-hop questions. Consider: “How did the delay in Project Apollo affect Q3 APAC margins?” RAG will retrieve Apollo documents and APAC margin documents. It cannot reason about the causal relationship between them. That is a structural gap in pure vector retrieval. Advanced hybrid approaches like GraphRAG address it, but standard RAG cannot. RAG also cannot persist context across sessions or personalize responses to individual users. These are jobs for memory and knowledge graphs, respectively. For a comparison of the tradeoffs, see [fine-tuning vs RAG](https://atlan.com/know/fine-tuning-vs-rag/).

* * *

## What is a knowledge graph for AI?

[Permalink to “What is a knowledge graph for AI?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#what-is-a-knowledge-graph-for-ai)

A knowledge graph models information as nodes (entities) and edges (explicit relationships between those entities). In AI systems, this structure powers retrieval where the path between entities matters, not just semantic similarity between text chunks.

Where RAG asks “what documents are most similar to this query?”, a knowledge graph asks “what entities and relationships are connected to this query?” and can traverse multiple hops across those connections.

### 1\. How knowledge graphs model information

[Permalink to “1. How knowledge graphs model information”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-how-knowledge-graphs-model-information)

Every element in a knowledge graph has three components: nodes that represent entities (a product, a regulation, a person, a data asset), edges that represent relationships (governs, depends on, is owned by, supersedes), and properties that carry attribute data on both nodes and edges. This structure enables queries that require reasoning across multiple connected entities. Vector similarity cannot do this: it finds documents that are semantically close, not entities that are explicitly related.

### 2\. GraphRAG: where graphs and retrieval meet

[Permalink to “2. GraphRAG: where graphs and retrieval meet”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-graph-rag-where-graphs-and-retrieval-meet)

[GraphRAG](https://atlan.com/know/what-is-graphrag/) is a hybrid architecture that combines graph traversal with vector search. Vector similarity identifies the most relevant entry-point nodes. Graph traversal then follows explicit relationship edges to gather connected context across multiple hops. The result is structured, multi-hop reasoning on top of broad document retrieval. [Graph-based retrieval improves precision up to 35% over vector-only approaches](https://memgraph.com/blog/rag-vs-graphrag) for multi-hop queries. For a deeper comparison, see [knowledge graphs vs RAG for AI](https://atlan.com/know/knowledge-graphs-vs-rag-for-ai/).

### 3\. Why knowledge graphs are hard to build without governed source data

[Permalink to “3. Why knowledge graphs are hard to build without governed source data”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-why-knowledge-graphs-are-hard-to-build-without-governed-source-data)

Most teams that try to build knowledge graphs from scratch encounter a bootstrapping problem. They attempt to construct entity definitions and relationships without a governed, well-cataloged source of truth to derive them from. The right pattern is to derive knowledge graphs from data that is already governed: a business glossary that defines entities, lineage that maps relationships, and governance metadata that indicates which definitions are authoritative. Active metadata platforms like Atlan build a context graph automatically from governed metadata. The [context graph vs knowledge graph](https://atlan.com/know/context-graph-vs-knowledge-graph/) distinction matters here: Atlan’s context graph is a governed knowledge graph with freshness guarantees built in. For architecture specifics on when vectors should yield to graphs, see [vector database vs knowledge graph for agent memory](https://atlan.com/know/vector-database-vs-knowledge-graph-agent-memory/).

* * *

## The composition pattern: how they work together in production

[Permalink to “The composition pattern: how they work together in production”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#the-composition-pattern-how-they-work-together-in-production)

With each component understood in isolation, the question shifts to integration. Production-grade AI systems don’t pick one of these three. They compose all three, with each handling a distinct job at a different layer.

Every component handles a specific capability that the others lack:

- **RAG** handles breadth: retrieves from the broad document corpus at query time
- **Memory** handles continuity: persists what the agent has learned about the user, the task, and the history
- **Knowledge graph** handles depth: provides structured relationships for multi-hop, causal, and compliance-grade reasoning

### 1\. The three jobs in the context stack

[Permalink to “1. The three jobs in the context stack”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-the-three-jobs-in-the-context-stack)

Each component fills a gap the others leave. RAG without memory restarts every session from zero: no agent continuity, no personalization. Memory without RAG has no access to the broad document corpus. The agent can recall the user but cannot retrieve fresh knowledge. RAG and memory without a knowledge graph hit the multi-hop ceiling: they can retrieve and persist, but cannot reason across explicit entity relationships. The composition of all three is the [enterprise context layer](https://atlan.com/know/context-layer-enterprise-ai/) that production AI systems need.

### 2\. How they integrate at query time

[Permalink to “2. How they integrate at query time”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-how-they-integrate-at-query-time)

The 2026 production architecture pattern follows a four-stage flow:

1. **Vector search** identifies the most relevant documents and entity entry-points
2. **Graph traversal** follows relationship edges from those entry-points to gather connected context
3. **Memory retrieval** injects session and user context from the persistent memory store
4. **LLM inference** runs with a full, composed context window: documents, relationships, and continuity

[2026 enterprise AI architecture analysis](https://www.techment.com/blogs/rag-architectures-enterprise-use-cases-2026/) consistently documents this hybrid, multi-layer pattern as the direction of production deployments.

### 3\. Why the data layer is the common failure point

[Permalink to “3. Why the data layer is the common failure point”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-why-the-data-layer-is-the-common-failure-point)

All three components draw from the same underlying data. If that data is ungoverned, stale, or lacks semantic context, all three degrade simultaneously. The failure mode is almost never the choice of retrieval architecture. It is almost always the quality of the data underneath. [LLM knowledge base freshness scoring](https://atlan.com/know/llm-knowledge-base-freshness-scoring/) is the mechanism for detecting and remedying this before it reaches the retrieval layer. Governance is not the last step in the architecture; it is the foundation that makes the composed stack reliable.

* * *

## When to choose what: a decision framework for enterprise teams

[Permalink to “When to choose what: a decision framework for enterprise teams”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#when-to-choose-what-a-decision-framework-for-enterprise-teams)

“When to choose” is still a useful question. The right frame is “which to prioritize first,” not “which to use exclusively.” Every mature enterprise AI system ends up using all three. The question is sequencing, and sequencing depends on your most urgent capability gap right now.

### 1\. Starting conditions for each component

[Permalink to “1. Starting conditions for each component”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-starting-conditions-for-each-component)

Each component has a primary problem it solves best. Start with the one that maps to your most urgent gap:

- **Start with RAG** if your primary problem is knowledge-intensive Q&A over a large document corpus with no personalization requirement and single-turn interactions
- **Start with memory** if your primary problem is multi-turn agent continuity, user personalization, or recurring workflow agents that need to retain context
- **Start with a knowledge graph or GraphRAG** if your primary problem involves complex multi-hop queries, compliance relationships, supply chain dependencies, or structured entity hierarchies

### 2\. Decision table

[Permalink to “2. Decision table”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-decision-table)

| If your primary problem is… | Start here | Add next |
| --- | --- | --- |
| Knowledge-intensive Q&A, single-turn, no personalization | RAG | Knowledge graph for relationship precision, then memory for session continuity |
| Multi-turn agent, user continuity, personalization | Memory | RAG for knowledge retrieval; graph for structured reasoning |
| Multi-hop queries, compliance, relationship-heavy domains | Knowledge graph / GraphRAG | RAG for broad document coverage; memory for session continuity |
| Production agentic system at scale | All three, governed | Context layer to keep data current |

### 3\. The maturity progression from RAG-only to composed stack

[Permalink to “3. The maturity progression from RAG-only to composed stack”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-the-maturity-progression-from-rag-only-to-composed-stack)

Teams at earlier AI maturity typically run RAG only. Teams at higher maturity add memory for agent continuity. Teams at production maturity compose all three with a governance layer underneath. The maturity progression leads directly to governance as an enabler: each new layer requires the data flowing into it to be well-defined, current, and trustworthy. [VentureBeat’s 2026 data predictions](https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026) flag contextual memory as the component most likely to surpass RAG as the primary retrieval mechanism for agentic AI. The maturity signal is the architecture: RAG-only teams are optimizing retrieval; composed-stack teams are building production-grade AI. For a comparison of enterprise platforms that support this architecture, see [enterprise RAG platforms comparison](https://atlan.com/know/enterprise-rag-platforms-comparison/) and [context engineering platforms comparison](https://atlan.com/know/context-engineering-platforms-comparison/).

* * *

## Why the data layer governs all three

[Permalink to “Why the data layer governs all three”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#why-the-data-layer-governs-all-three)

RAG, memory, and knowledge graphs are retrieval mechanisms. They are only as good as what they retrieve. This is the insight that most enterprise AI architecture discussions skip, and it is the most consequential one.

Ungoverned, stale, semantically thin data breaks all three regardless of which combination you use.

### 1\. How ungoverned data degrades each component

[Permalink to “1. How ungoverned data degrades each component”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-how-ungoverned-data-degrades-each-component)

The failure mode for each component is the same root cause, expressed differently:

- **RAG** retrieves stale or contradictory documents and produces hallucinated answers with false citations
- **Memory** stores outdated context and causes agents to act on wrong state: a user’s preferences from a year ago, a data classification that has since changed
- **Knowledge graph** follows stale entity definitions or broken relationship edges and reaches incorrect inference paths

Enterprise AI project failures trace disproportionately to data readiness problems rather than retrieval architecture failures. The choice of RAG vs. memory vs. knowledge graph matters far less than whether the data those components retrieve is governed, fresh, and semantically rich.

### 2\. What “context-ready” data looks like in production

[Permalink to “2. What “context-ready” data looks like in production”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-what-context-ready-data-looks-like-in-production)

Context readiness is not a binary state. It is a set of properties the data layer must maintain continuously:

- **Freshness scoring:** every data asset has a timestamp and a staleness score that retrieval layers can filter on
- **Lineage tracking:** the path from source to indexed asset is traceable, so retrieval results can be audited
- **Semantic tags:** entity definitions, domain classifications, and business glossary terms that improve retrieval precision
- **Ownership metadata:** who is responsible for each asset, so freshness and accuracy can be maintained

### 3\. The governed context layer as the shared foundation

[Permalink to “3. The governed context layer as the shared foundation”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-the-governed-context-layer-as-the-shared-foundation)

Atlan’s position in this architecture is not as a replacement for any of the three components. It is the governed context foundation that all three draw from. Atlan’s context graph provides traceable reasoning paths, multi-hop semantic relationships, governance nodes for compliance, and temporal context (when data was last verified): properties unavailable in standard RAG pipelines. The [enterprise context layer](https://atlan.com/know/context-layer-enterprise-ai/) is the piece most architecture discussions treat as optional. In production, it is the variable that determines whether the composed stack works. For teams evaluating how to implement this pattern, the [CIO guide to context graphs](https://atlan.com/resources/cio-guide-to-context-graphs/) walks through the architecture in detail.

* * *

## Real stories from real customers: context governance powering production AI

[Permalink to “Real stories from real customers: context governance powering production AI”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#real-stories-from-real-customers-context-governance-powering-production-ai)

"We're excited to build the future of AI governance with Atlan. All of the work that we did to get to a shared language at Workday can be leveraged by AI via Atlan's MCP server…as part of Atlan's AI Labs, we're co-building the semantic layer that AI needs with new constructs, like context products."

Joe DosSantos, VP of Enterprise Data & Analytics, Workday

https://website-assets.atlan.com/img/client-logos/workday-logo-1.svg[Watch Now](https://atlan.com/regovern-watch-center/workday-context-as-culture/)

"Atlan is much more than a catalog of catalogs. It's more of a context operating system…Atlan enabled us to easily activate metadata for everything from discovery in the marketplace to AI governance to data quality to an MCP server delivering context to AI models."

Sridher Arumugham, Chief Data & Analytics Officer, DigiKey

https://website-assets.atlan.com/img/regovern-2025/digikey-logo.svg[Watch Now](https://atlan.com/regovern-watch-center/digikey-context-readiness/)

* * *

## Building AI that doesn’t forget, hallucinate, or drift

[Permalink to “Building AI that doesn’t forget, hallucinate, or drift”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#building-ai-that-doesn-t-forget-hallucinate-or-drift)

Enterprise teams running AI on a single retrieval mechanism hit the same wall. RAG gives breadth but not continuity. Memory gives continuity but not structured reasoning. Knowledge graphs give structure but not broad coverage. The instinct is to pick the best-fit tool. The production reality is that all three are needed, and all three are only as good as the data layer they draw from.

Atlan’s context layer acts as the governed foundation underneath the entire context stack. Active metadata keeps what RAG retrieves current. The Atlan context graph structures the relationships that memory and knowledge graphs need. Governance nodes, lineage, and freshness scores flow into each component so that retrieval decisions are explainable and traceable, not just fast.

Teams using a governed context layer stop debugging hallucinations at the retrieval layer and start building AI systems that reason correctly across time, users, and data domains. The architecture debate resolves itself: the right composition depends on the use case, but the governed data foundation is always the same. The [how to implement an enterprise context layer for AI](https://atlan.com/know/how-to-implement-enterprise-context-layer-for-ai/) guide walks through the practical steps for teams ready to build this foundation.

## FAQs about AI memory vs RAG vs knowledge graph

[Permalink to “FAQs about AI memory vs RAG vs knowledge graph”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#faqs-about-ai-memory-vs-rag-vs-knowledge-graph)

### 1\. What is the main difference between RAG and AI memory?

[Permalink to “1. What is the main difference between RAG and AI memory?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#1-what-is-the-main-difference-between-rag-and-ai-memory)

RAG is stateless: it retrieves relevant documents at query time and discards that context when the session ends. AI memory is stateful: it persists what an agent has learned across sessions, enabling continuity and personalization. Most production systems use both. RAG handles document retrieval; memory handles session and user context. The two serve different jobs in the same context stack.

### 2\. When should I use a knowledge graph instead of standard RAG?

[Permalink to “2. When should I use a knowledge graph instead of standard RAG?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#2-when-should-i-use-a-knowledge-graph-instead-of-standard-rag)

Use a knowledge graph when your queries require multi-hop reasoning: tracing relationships across entities rather than matching document similarity. Compliance use cases, supply chain analysis, financial entity mapping, and product hierarchy queries are all relationship-driven and benefit from graph traversal. Standard RAG retrieves relevant documents but cannot traverse explicit entity relationships.

### 3\. What is GraphRAG and how does it differ from standard RAG?

[Permalink to “3. What is GraphRAG and how does it differ from standard RAG?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#3-what-is-graph-rag-and-how-does-it-differ-from-standard-rag)

GraphRAG combines vector search with a knowledge graph layer. Vector similarity identifies the most relevant entry nodes; graph traversal then follows explicit relationship edges to gather connected context. The result is structured, multi-hop reasoning on top of broad document retrieval. GraphRAG consistently outperforms standard RAG on complex, causal, and cross-document reasoning tasks.

### 4\. Can RAG, AI memory, and a knowledge graph be used together?

[Permalink to “4. Can RAG, AI memory, and a knowledge graph be used together?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#4-can-rag-ai-memory-and-a-knowledge-graph-be-used-together)

Yes, and production-grade AI systems routinely use all three. RAG handles broad document retrieval, memory handles session continuity and personalization, and knowledge graphs handle relationship-driven structured reasoning. The three serve different jobs in the same context stack. The coordination challenge is governance: all three degrade if the data underneath them is stale or ungoverned.

### 5\. Why do AI agents forget between sessions?

[Permalink to “5. Why do AI agents forget between sessions?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#5-why-do-ai-agents-forget-between-sessions)

LLMs are stateless by design: each inference call starts with no memory of prior interactions. Without an external memory system, every new session is a fresh start. AI memory systems address this by persisting context outside the model. Session history, learned user preferences, and prior task outcomes are stored externally and injected into the context window when needed.

### 6\. What causes enterprise AI projects to fail at the retrieval layer?

[Permalink to “6. What causes enterprise AI projects to fail at the retrieval layer?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#6-what-causes-enterprise-ai-projects-to-fail-at-the-retrieval-layer)

Most enterprise AI failures happen not because of the wrong retrieval architecture but because the underlying data is not context-ready. Stale documents in the RAG index, outdated context in the memory store, and broken relationship edges in the knowledge graph all produce the same symptom: hallucinated or incorrect AI outputs. Data governance, freshness scoring, and active metadata management are the upstream fixes.

### 7\. How does context engineering relate to RAG and memory?

[Permalink to “7. How does context engineering relate to RAG and memory?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#7-how-does-context-engineering-relate-to-rag-and-memory)

Context engineering is the practice of systematically constructing, maintaining, and governing the full context window that an LLM uses at inference time. RAG, memory, and knowledge graphs are all context engineering components: mechanisms for populating that window with relevant, current, and structured information. Context engineering treats these as a composed system rather than standalone retrieval tools.

### 8\. Is fine-tuning a better alternative to RAG and memory?

[Permalink to “8. Is fine-tuning a better alternative to RAG and memory?”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#8-is-fine-tuning-a-better-alternative-to-rag-and-memory)

Fine-tuning trains the model on new data. It does not enable retrieval of external documents or persistent memory across sessions. For enterprise AI, fine-tuning is rarely a substitute for RAG or memory; it is a complement. Fine-tuning is best for adapting model style or domain terminology. RAG and memory handle dynamic, user-specific, and frequently updated knowledge that cannot be baked into model weights.

## Sources

[Permalink to “Sources”#](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/#sources)

01. [RAG Market Report 2025-2030, MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/retrieval-augmented-generation-rag-market-135976317.html)
02. [Six Data Shifts That Will Shape Enterprise AI in 2026, VentureBeat](https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026)
03. [Vector Databases vs. Graph RAG for Agent Memory: When to Use Which, MachineLearningMastery](https://machinelearningmastery.com/vector-databases-vs-graph-rag-for-agent-memory-when-to-use-which/)
04. [RAG vs GraphRAG, Memgraph](https://memgraph.com/blog/rag-vs-graphrag)
05. [From RAG to Context: 2025 Year-End Review, RAGFlow](https://ragflow.io/blog/rag-review-2025-from-rag-to-context)
06. [10 RAG Architectures for Enterprise Use Cases in 2026, Techment](https://www.techment.com/blogs/rag-architectures-enterprise-use-cases-2026/)
07. [The Next Frontier of RAG: How Enterprise Knowledge Systems Will Evolve 2026-2030, NStarX](https://nstarxinc.com/blog/the-next-frontier-of-rag-how-enterprise-knowledge-systems-will-evolve-2026-2030/)
08. [From RAG to GraphRAG: Knowledge Graphs, Ontologies and Smarter AI, GoodData](https://www.gooddata.com/blog/from-rag-to-graphrag-knowledge-graphs-ontologies-and-smarter-ai/)
09. [Vector vs. Graph RAG: How to Actually Architect Your AI Memory, OptimumPartners](https://optimumpartners.com/insight/vector-vs-graph-rag-how-to-actually-architect-your-ai-memory/)
10. [RAG Market Size to Hit $67.42B by 2034, Precedence Research](https://www.precedenceresearch.com/retrieval-augmented-generation-market)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="architecture-and-orchestration-of-memory-systems-in-ai-agent.md">
<details>
<summary>Architecture and Orchestration of Memory Systems in AI Agents</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/>

# Architecture and Orchestration of Memory Systems in AI Agents

[https://av-eks-lekhak.s3.amazonaws.com/media/lekhak-profile-images/converted_image_00OeVxR.webp](https://www.analyticsvidhya.com/blog/author/badrinarayan6645541/)

[Badrinarayan M](https://www.analyticsvidhya.com/blog/author/badrinarayan6645541/) Last Updated :
08 Apr, 2026

16 min read

The evolution of artificial intelligence from stateless models to autonomous, goal-driven agents depends heavily on advanced memory architectures. While [Large Language Models](https://www.analyticsvidhya.com/blog/2023/03/an-introduction-to-large-language-models-llms/) (LLMs) possess strong reasoning abilities and vast embedded knowledge, they lack persistent memory, making them unable to retain past interactions or adapt over time. This limitation leads to repeated context injection, increasing token usage, latency, and reducing efficiency. To address this, modern agentic AI systems incorporate structured memory frameworks inspired by human cognition, enabling them to maintain context, learn from interactions, and operate effectively across multi-step, long-term tasks.

Robust memory design is critical for ensuring reliability in these systems. Without it, agents face issues like memory drift, context degradation, and hallucinations, especially in long interactions where attention weakens over time. To overcome these challenges, researchers have developed multi-layered memory models, including short-term working memory and long-term episodic, semantic, and procedural memory. Additionally, effective [memory management techniques](https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/)—such as semantic consolidation, intelligent forgetting, and conflict resolution—are essential. The analysis also compares leading frameworks like LangMem, Mem0, and Zep, highlighting their role in enabling scalable, stateful AI systems for real-world applications.

## Table of contents

- [The Architectural Imperative: Operating System Analogies and Frameworks](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-the-architectural-imperative-operating-system-analogies-and-frameworks)
- [Short-Term Memory: The Working Context Window](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-short-term-memory-the-working-context-window)
- [Long-Term Memory: The Tripartite Cognitive Model](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-long-term-memory-the-tripartite-cognitive-model)
  - [Episodic Memory: Events and Sequential Experiences](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-episodic-memory-events-and-sequential-experiences)
  - [Semantic Memory: Distilled Facts and Knowledge Representation](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-semantic-memory-distilled-facts-and-knowledge-representation)
  - [Procedural Memory: Operational Skills and Dynamic Execution](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-procedural-memory-operational-skills-and-dynamic-execution)
- [Advanced Memory Management and Consolidation Strategies](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-advanced-memory-management-and-consolidation-strategies)
  - [Asynchronous Semantic Consolidation](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-asynchronous-semantic-consolidation)
  - [Intelligent Forgetting and Memory Decay](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-intelligent-forgetting-and-memory-decay)
- [Algorithmic Strategies for Resolving Memory Conflicts](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-algorithmic-strategies-for-resolving-memory-conflicts)
  - [Algorithmic Recalibration and Temporal Weighting](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-algorithmic-recalibration-and-temporal-weighting)
  - [Semantic Conflict Merging and Arbitration](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-semantic-conflict-merging-and-arbitration)
  - [Governance and Access Controls in Multi-Agent Systems](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-governance-and-access-controls-in-multi-agent-systems)
- [Comparative Analysis of Enterprise Memory Frameworks: Mem0, Zep, and LangMem](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-comparative-analysis-of-enterprise-memory-frameworks-mem0-zep-and-langmem)
  - [Mem0: The Universal Personalization and Compression Layer](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-mem0-the-universal-personalization-and-compression-layer)
  - [Architectural Focus and Capabilities](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-architectural-focus-and-capabilities)
  - [Conflict Resolution and Management](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-conflict-resolution-and-management)
  - [Deployment and Use Cases](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-deployment-and-use-cases)
  - [Zep: Temporal Knowledge Graphs for High-Performance Relational Retrieval](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-zep-temporal-knowledge-graphs-for-high-performance-relational-retrieval)
  - [LangMem: Native Developer Integration for Procedural Learning](https://www.analyticsvidhya.com/blog/2025/03/langmem-sdk/)
  - [Architectural Focus and Capabilities](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-architectural-focus-and-capabilities-1)
  - [Conflict Resolution and Management](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-conflict-resolution-and-management-1)
  - [Deployment and Use Cases](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-deployment-and-use-cases-1)
  - [Enterprise Framework Benchmark Synthesis](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-enterprise-framework-benchmark-synthesis)
- [Conclusion](https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/#h-conclusion)

## The Architectural Imperative: Operating System Analogies and Frameworks

Modern AI agents treat the LLM as more than a text generator. They use it as the brain of a larger system, much like a CPU. Frameworks like CoALA separate the agent’s thinking process from its memory, treating memory as a structured system rather than just raw text. This means the agent actively retrieves, updates, and uses information instead of passively relying on past conversations.

Building on this, systems like MemGPT introduce a memory hierarchy similar to computers. The model uses a limited “working memory” (context window) and shifts less important information to external storage, bringing it back only when needed. This allows agents to handle long-term tasks without exceeding token limits. To stay efficient and accurate, agents also compress information—keeping only what’s relevant—just like humans focus on key details and ignore noise, reducing errors like memory drift and [hallucinations](https://www.analyticsvidhya.com/blog/2025/09/why-llms-hallucinate/).

## Short-Term Memory: The Working Context Window

Short-term memory in AI agents works like human working memory—it temporarily holds the most recent and relevant information needed for immediate tasks. This includes recent conversation history, system prompts, tool outputs, and reasoning steps, all stored within the model’s limited context window. Because this space has strict token limits, systems typically use FIFO (First-In-First-Out) queues to remove older information as new data arrives. This keeps the model within its capacity.

https://cdn.analyticsvidhya.com/wp-content/uploads/2026/03/1-21.webp**Source:** [Docs/Langchain](https://docs.langchain.com/oss/python/langchain/short-term-memory)

However, simple FIFO removal can discard important information, so advanced systems use smarter memory management. These systems monitor token usage and, when limits are close, prompt the model to summarize and store key details in [long-term memory](https://www.analyticsvidhya.com/blog/2022/05/an-introduction-to-lstms/) or external storage. This keeps the working memory focused and efficient. Additionally, attention mechanisms help the model prioritize relevant information, while metadata like session IDs, timestamps, and user roles ensure proper context, security, and response behavior.

## Long-Term Memory: The Tripartite Cognitive Model

Long-term memory acts as the enduring, persistent repository for knowledge accumulated over the agent’s lifecycle, surviving well beyond the termination of individual computing sessions or chat interactions. The migration of data from a short-term working context to long-term storage represents a fundamental cognitive compression step that isolates valuable signal from conversational noise. To create human-like continuity and more sophisticated intelligence, systems divide long-term storage into three distinct operational modes: episodic, semantic, and procedural memory. Each modality requires fundamentally different data structures, storage mechanisms, and retrieval algorithms.

To better understand the structural requirements of these memory types, we must observe how data patterns dictate database architecture choices. The following table illustrates the required storage and query mechanics for each memory type, highlighting why monolithic storage approaches often fail.

| Memory Type | Primary Data Pattern | Query / Retrieval Mechanics | Optimal Database Implementation |
| --- | --- | --- | --- |
| Episodic | Time-series events and raw transcripts | Temporal range queries, chronological filtering | Relational databases with automatic partitioning (e.g., Hypertables) |
| Semantic | High-dimensional vector embeddings | K-nearest neighbor search, cosine similarity | Vector databases (pgvector, Pinecone, Milvus) |
| Procedural | Relational logic, code blocks, state rules | CRUD operations with complex joins, exact ID lookups | Standard relational or Key-Value storage (e.g., PostgreSQL) |

https://cdn.analyticsvidhya.com/wp-content/uploads/2026/03/2-21.webp**Source:** [Deeplearning](https://learn.deeplearning.ai/courses/long-term-agentic-memory-with-langgraph/lesson/ovv0p/introduction)

A multi-database approach—using separate systems for each memory type—forces serial round-trip across network boundaries, adding significant latency and multiplying operational complexity. Consequently, advanced implementations attempt to consolidate these patterns into unified, production-grade databases capable of handling hybrid vector-relational workloads.

### Episodic Memory: Events and Sequential Experiences

Episodic memory in AI agents stores detailed, time-based records of past interactions, similar to how humans remember specific events. It typically consists of conversation logs, tool usage, and environmental changes, all saved with timestamps and metadata. This allows agents to maintain continuity across sessions—for example, recalling a previous customer support issue and referencing it naturally in future interactions. Inspired by human biology, these systems also use techniques like “experience replay.” They revisit past events to improve learning and make better decisions in new situations.

However, relying only on episodic memory has limitations. While it can accurately retrieve past interactions, it does not inherently understand patterns or extract deeper meaning. For instance, if a user repeatedly mentions a preference, episodic memory will only return separate instances rather than recognizing a consistent interest. This means the agent must still process and infer patterns during each interaction, making it less efficient and preventing true knowledge generalization.

### Semantic Memory: Distilled Facts and Knowledge Representation

Semantic memory stores generalized knowledge, facts, and rules, going beyond specific events to capture meaningful insights. Unlike episodic memory, which records individual interactions, semantic memory extracts and preserves key information—such as turning a past interaction about a peanut allergy into a permanent fact like “User Allergy: Peanuts.” AI systems typically implement this with knowledge bases, symbolic representations, and vector databases. They often integrate these with Retrieval-Augmented Generation (RAG) to provide domain-specific expertise without retraining the model.

A crucial part of building [intelligent agents](https://www.analyticsvidhya.com/datahacksummit-2025/workshops/mastering-intelligent-agents-a-deep-dive-into-agentic-ai-building-ai) is converting episodic memory into semantic memory. This process involves identifying patterns across past interactions and distilling them into reusable knowledge. Inspired by human cognition, this “memory consolidation” ensures agents can generalize, reduce redundancy, and improve efficiency over time. Without this step, agents remain limited to recalling past events rather than truly learning from them.

### Procedural Memory: Operational Skills and Dynamic Execution

Procedural memory in AI agents represents “knowing how” to perform tasks, focusing on execution rather than facts or past events. It governs how agents carry out workflows, use tools, coordinate sub-agents, and make decisions. This type of memory exists in two forms: implicit (learned within the model during training) and explicit (defined through code, prompts, and workflows). As agents gain experience, frequently used processes become more efficient, reducing computation and speeding up responses—for example, a travel agent knowing the exact steps to search, compare, and book flights across systems.

Modern advancements are making procedural memory dynamic and learnable. Instead of relying on fixed, manually designed workflows, agents can now refine their behavior over time using feedback from past tasks. This allows them to update their decision-making strategies, fix errors, and improve execution continuously. Frameworks like [AutoGen](https://www.analyticsvidhya.com/blog/2023/11/launching-into-autogen-exploring-the-basics-of-a-multi-agent-framework/), [CrewAI](https://www.analyticsvidhya.com/blog/2024/01/building-collaborative-ai-agents-with-crewai/), and [LangMem](https://www.analyticsvidhya.com/blog/2025/03/langmem-sdk/) support this by enabling structured interactions, role-based memory, and automatic prompt optimization, helping agents evolve from rigid executors into adaptive, self-improving systems.

## Advanced Memory Management and Consolidation Strategies

The naive approach to agent memory management—simply appending every new conversation turn into a vector database—inevitably leads to catastrophic systemic failure. As the data corpus grows over weeks or months of deployment, agents experience debilitating retrieval noise, severe context dilution, and latency spikes as they attempt to parse massive arrays of slightly relevant vectors. Effective long-term functionality requires highly sophisticated orchestration to govern how the system consolidates, scores, stores, and eventually discards memories.

### Asynchronous Semantic Consolidation

Attempting to extract complex beliefs, summarize overarching concepts, and dynamically update procedural rules during an active, user-facing session introduces unacceptable latency overhead. To mitigate this, enterprise-grade architectures uniformly rely on asynchronous, background consolidation paradigms.

During the active interaction (commonly referred to as “the hot path”), the agent leverages its existing context window to respond in real-time, functioning solely on read-access to long-term memory and write-access to its short-term session cache. This guarantees zero-latency conversational responses. Once the session terminates, a background cognitive compression process is initiated. This background process—often orchestrated by a smaller, highly efficient local model (such as Qwen2.5 1.5B) to save compute costs—scans the raw episodic history of the completed session. It extracts structured facts, maps new entity relationships, resolves internal contradictions against existing data, and securely writes the distilled knowledge to the semantic vector database or knowledge graph.

This tiered architectural approach naturally categorizes data by its operational temperature:

1. **Hot Memory:** The immediate, full conversational context held within the prompt window, providing high-fidelity, zero-latency grounding for the active task.
2. **Warm Memory:** Structured facts, refined preferences, and semantic nodes asynchronously extracted into a high-speed database, serving as the primary source of truth for RAG pipelines.
3. **Cold Archive:** Highly compressed, serialized logs of old sessions. These are removed from active retrieval pipelines and retained purely for regulatory compliance, deep system debugging, or periodic batched distillation processes.

By ensuring the main reasoning model never sees the raw, uncompressed history, the agent operates entirely on high-signal, distilled knowledge.

### Intelligent Forgetting and Memory Decay

A foundational, yet deeply flawed, assumption in early AI memory design was the necessity of perfect, infinite retention. However, infinite retention is an architectural bug, not a feature. Imagine a customer support agent deployed for six months; if it perfectly remembers every minor typo correction, every casual greeting, and every deeply obsolete user preference, the retrieval mechanism rapidly becomes polluted. A search for the user’s current project might return fifty results, and half of them could be badly outdated. That creates direct contradictions and compounds hallucinations.

Biological [cognitive efficiency](https://www.analyticsvidhya.com/blog/2023/09/cognitive-computing/) relies heavily on the mechanism of selective forgetting, allowing the human brain to maintain focus on relevant data while shedding the trivial. Applied to artificial intelligence, the “intelligent forgetting” mechanism dictates that not all memories possess equal permanence. Utilizing mathematical principles derived from the Ebbinghaus Forgetting Curve—which established that biological memories decay exponentially unless actively reinforced—advanced memory systems assign a continuous decay rate to stored vectors.

#### Algorithms Powering Intelligent Forgetting

The implementation of intelligent forgetting leverages several distinct algorithmic strategies:

- **Time-to-Live (TTL) Tiers and Expiration Dates:** The system tags each memory with an expiration date as soon as it creates it, based on that memory’s semantic category. It assigns immutable facts, such as severe dietary allergies, an infinite TTL, so they never decay. It gives transient contextual notes, such as syntax questions tied to a temporary project, a much shorter lifespan—often 7 or 30 days. After that date passes, the system aggressively removes the memory from search indices to prevent it from conflicting with newer information.
- **Refresh-on-Read Mechanics:** To mimic the biological spacing effect, the system boosts a memory’s relevance score whenever an agent successfully retrieves and uses it in a generation task. It also fully resets that memory’s decay timer. As a result, frequently used information stays preserved, while contradictory or outdated facts eventually fall below the minimum retrieval threshold and get pruned systematically.
- **Importance Scoring and Dual-Layer Architectures:** During the consolidation phase, LLMs assign an importance score to incoming information based on perceived long-term value. Frameworks like FadeMem categorize memories into two distinct layers. The Long-term Memory Layer (LML) houses high-importance strategic directives that decay incredibly slowly. The Short-term Memory Layer (SML) holds lower-importance, one-off interactions that fade rapidly.

Furthermore, formal forgetting policies, such as the Memory-Aware Retention Schema (MaRS), deploy Priority Decay algorithms and Least Recently Used (LRU) eviction protocols to automatically prune storage bloat without requiring manual developer intervention. Engine-native primitives, such as those found in MuninnDB, handle this decay at the database engine level, continuously recalculating vector relevance in the background so the agent always queries an optimized dataset. By transforming memory from an append-only ledger to an organic, decay-aware ecosystem, agents retain high-signal semantic maps while effortlessly shedding obsolete noise.

## Algorithmic Strategies for Resolving Memory Conflicts

Even with aggressive intelligent forgetting and TTL pruning, dynamic operational environments guarantee that new facts will eventually contradict older, persistent memories. A user who explicitly reported being a “beginner” in January may be operating as a “senior developer” by November. If both data points reside permanently in the agent’s semantic memory, a standard vector search will indiscriminately retrieve both, leaving the LLM trapped between conflicting requirements and vulnerable to severe drift traps. Addressing memory drift and contradictory context requires multi-layered, proactive conflict resolution strategies.

### Algorithmic Recalibration and Temporal Weighting

Standard vector retrieval ranks information strictly by semantic similarity (e.g., cosine distance). Consequently, a highly outdated fact that perfectly matches the phrasing of a user’s current prompt will inherently outrank a newer, slightly rephrased fact. To resolve this structural flaw, advanced memory databases implement composite scoring functions that mathematically balance semantic relevance against temporal recency.

When evaluating a query, the retrieval system ranks candidate vectors using both their similarity score and an exponential time-decay penalty. Thus, the system enforces strict hypothesis updates without physically rewriting prior historical facts, heavily biasing the final retrieval pipeline toward the most recent state of truth. This ensures that while the old memory still exists for historical auditing, it is mathematically suppressed during active agent reasoning.

### Semantic Conflict Merging and Arbitration

Mechanical metadata resolution—relying solely on timestamps and recency weights—is often insufficient for resolving highly nuanced, context-dependent contradictions. Advanced cognitive systems utilize semantic merging protocols during the background consolidation phase to enforce internal consistency.

Instead of mechanically overwriting old data, the system deploys specialized arbiter agents to review conflicting database entries. These arbiters utilize the LLM’s natural strength in understanding nuance to analyze the underlying intent and meaning of the contradiction. If the system detects a conflict—for example, a database contains both “User prefers React” and “User is building entirely in Vue”—the arbiter LLM decides whether the new statement is a duplicate, a refinement, or a complete operational pivot.

If the system identifies the change as a pivot, it does not simply delete the old memory. Instead, it compresses that memory into a temporal reflection summary. The arbiter generates a coherent, time-bound reconciliation (e.g., “User utilized React until November 2025, but has since transitioned their primary stack to Vue”). This approach explicitly preserves the historical evolution of the user’s preferences while strictly defining the current active baseline, preventing the active response generator from suffering goal deviation or falling into drift traps.

### Governance and Access Controls in Multi-Agent Systems

In complex multi-agent architectures, such as those built on CrewAI or AutoGen, simultaneous read and write operations across a shared database dramatically worsen memory conflicts. To prevent race conditions, circular dependencies, and cross-agent contamination, systems must implement strict shared-memory access controls.

Inspired by traditional database isolation levels, robust multi-agent frameworks define explicit read and write boundaries to create a defense-in-depth architecture. For example, within an automated customer service swarm, a “retrieval agent” logs the raw data of the user’s subscription tier. A separate “sentiment analyzer agent” holds permissions to read that tier data but is strictly prohibited from modifying it. Finally, the “response generator agent” only possesses write-access for drafted replies, and cannot alter the underlying semantic user profile. By enforcing these strict ontological boundaries, the system prevents agents from using outdated information that could lead to inconsistent decisions. It also flags coordination breakdowns in real time before they affect the user experience.

## Comparative Analysis of Enterprise Memory Frameworks: Mem0, Zep, and LangMem

These theoretical paradigms—cognitive compression, intelligent forgetting, temporal retrieval, and procedural learning—have moved beyond academia. Companies are now actively turning them into real products. As industry development shifts away from basic RAG implementations toward complex, autonomous agentic systems, a diverse and highly competitive ecosystem of managed memory frameworks has emerged.

The decision to adopt an external memory framework hinges entirely on operational scale and application intent. Before you evaluate frameworks, you need to make one fundamental engineering assessment. If agents handle stateless, single-session tasks with no expected carryover, they do not need a memory overlay. Adding one only increases latency and architectural complexity. Conversely, if an agent operates repeatedly over related tasks, interacts with persistent entities (users, vendors, repositories), requires behavioral adaptation based on human corrections, or suffers from exorbitant token costs due to continuous context re-injection, a dedicated memory infrastructure is mandatory.

The following comparative analysis evaluates three prominent systems—Mem0, Zep, and [LangMem](https://www.analyticsvidhya.com/blog/2025/03/langmem-sdk/)—assessing their architectural philosophies, technical capabilities, performance metrics, and optimal deployment environments.

### Mem0: The Universal Personalization and Compression Layer

https://cdn.analyticsvidhya.com/wp-content/uploads/2026/03/3-19.webp

Mem0 has established itself as a highly mature, heavily adopted managed memory platform designed fundamentally around deep user personalization and institutional cost-efficiency. It operates as a universal abstraction layer across various LLM providers, offering both an open-source (Apache 2.0) self-hosted variant and a fully managed enterprise cloud service.

### Architectural Focus and Capabilities

Mem0’s primary value proposition lies in its sophisticated Memory Compression Engine. Rather than storing bloated raw episodic logs, Mem0 aggressively compresses chat histories into highly optimized, high-density memory representations. This compression drastically reduces the payload required for context re-injection, achieving up to an 80% reduction in prompt tokens. In high-volume consumer applications, this translates directly to massive API cost savings and heavily reduced response latency. Benchmark evaluations, such as ECAI-accepted contributions, indicate Mem0 achieves 26% higher response quality than native OpenAI memory while utilizing 90% fewer tokens.

At the base Free and Starter tiers, Mem0 relies on highly efficient vector-based semantic search. However, its Pro and Enterprise tiers activate an underlying knowledge graph, enabling the system to map complex entities and their chronological relationships across distinct conversations. The platform manages data across a strict hierarchy of workspaces, projects, and users, allowing for rigorous isolation of context, though this can introduce unnecessary complexity for simpler, single-tenant projects.

### Conflict Resolution and Management

Mem0 natively integrates robust Time-To-Live (TTL) functionality and expiration dates directly into its storage API. Developers can assign specific lifespans to distinct memory blocks at inception, allowing the system to automatically prune stale data, mitigate context drift, and prevent memory bloat over long deployments.

### Deployment and Use Cases

With out-of-the-box SOC 2 and HIPAA compliance, Bring Your Own Key (BYOK) architecture, and support for air-gapped or Kubernetes on-premise deployments, Mem0 targets large-scale, high-security enterprise environments. It is particularly effective for customer support automation, persistent sales CRM agents managing long sales cycles, and personalized healthcare companions where secure, highly accurate, and long-term user tracking is paramount. Mem0 also uniquely features a Model Context Protocol (MCP) server, allowing for universal integration across almost any modern AI framework. It remains the safest, most feature-rich option for compliance-heavy, personalization-first applications.

### Zep: Temporal Knowledge Graphs for High-Performance Relational Retrieval

https://cdn.analyticsvidhya.com/wp-content/uploads/2026/03/4-14.webp

If Mem0 focuses on token compression and secure personalization, Zep focuses on high-performance, complex relational mapping, and sub-second latency. Zep diverges radically from traditional flat vector stores by employing a native Temporal Knowledge Graph architecture, positioning itself as the premier solution for applications requiring deep, ontological reasoning across vast timeframes.

#### Architectural Focus and Capabilities

Zep operates via a highly opinionated, dual-layer memory API abstraction. The API explicitly distinguishes between short-term conversational buffers (typically the last 4 to 6 raw messages of a session) and long-term context derived directly from an autonomously built, user-level knowledge graph. As interactions unfold, Zep’s powerful background ingestion engine asynchronously parses episodes, extracting entity nodes and relational edges, executing bulk episode ingest operations without blocking the main conversational thread.

Zep uses an exceptionally sophisticated retrieval engine. It combines hybrid vector and graph search with multiple algorithmic rerankers. When an agent requires context, Zep evaluates the immediate short-term memory against the knowledge graph, and rather than returning raw vectors, it returns a highly formatted, auto-generated, prompt-ready context block. Furthermore, Zep implements granular “Fact Ratings,” allowing developers to filter out low-confidence or highly ambiguous nodes during the retrieval phase, ensuring that only high-signal data influences the agent’s prompt.

#### Conflict Resolution and Management

Zep addresses memory conflict through explicit temporal mapping. Because the graph plots every fact, node, and edge chronologically, arbiter queries can trace how a user’s state evolves over time. This lets the system distinguish naturally between an old preference and a new operational pivot. Zep also allows for custom “Group Graphs,” a powerful feature enabling shared memory and context synchronization across multiple users or business units—a capability often absent in simpler, strictly user-siloed personalization layers.

#### Deployment and Use Cases

Zep excels in latency-sensitive, compute-heavy production environments. Its [retrieval pipelines](https://www.analyticsvidhya.com/courses/building-rag-applications) are heavily optimized, boasting average query latencies of under 50 milliseconds. For specialized applications like voice AI assistants, Zep provides a return\_context argument in its memory addition method; this allows the system to return an updated context string immediately upon data ingestion, eliminating the need for a separate retrieval round-trip and further slashing latency. While its initial setup is more complex and entirely dependent on its proprietary Graphiti engine, Zep provides unmatched capabilities for high-performance conversational AI and ontology-driven reasoning.

### LangMem: Native Developer Integration for Procedural Learning

https://cdn.analyticsvidhya.com/wp-content/uploads/2026/03/5-10.webp

LangMem represents a distinctly different philosophical approach compared to Mem0 and Zep. LangChain developed LangMem as an open-source, MIT-licensed SDK for deep native integration within the LangGraph ecosystem. It does not function as an external standalone database service or a managed cloud platform.

### Architectural Focus and Capabilities

LangMem entirely eschews heavy external infrastructure and proprietary graphs, utilizing a highly flexible, flat key-value and vector architecture backed seamlessly by LangGraph’s native long-term memory store. Its primary objective sets it apart from the others. It aims not just to track static user facts or relationships, but to improve the agent’s dynamic procedural behavior over time.

LangMem provides core functional primitives that allow agents to actively manage their own memory “in the hot path” using standard tool calls. More importantly, it is deeply focused on automated prompt refinement and continuous instruction learning. Through built-in optimization loops, LangMem continuously evaluates interaction histories to extract procedural lessons, automatically updating the agent’s core instructions and operational heuristics to prevent repeated errors across subsequent sessions. This capability is highly unique among the compared tools, directly addressing the evolution of procedural memory without requiring continuous manual intervention by human prompt engineers.

### Conflict Resolution and Management

Because LangMem offers raw, developer-centric tooling instead of an opinionated managed service, the system architect usually defines the conflict-resolution logic. However, it natively supports background memory managers that automatically extract and consolidate knowledge offline, shifting the heavy computational burden of summarization away from active user interactions.

### Deployment and Use Cases

LangMem is the definitive, developer-first choice for engineering teams already heavily invested in [LangGraph architectures](https://www.analyticsvidhya.com/blog/2024/07/building-agentic-rag-systems-with-langgraph/) who demand total sovereignty over their infrastructure and data pipelines. It is ideal for orchestrating multi-agent workflows and complex swarms where procedural learning and systemic behavior adaptation are much higher priorities than out-of-the-box user personalization. While it demands significantly more engineering effort to configure custom extraction pipelines and manage the underlying vector databases manually, it entirely eliminates third-party platform lock-in and ongoing subscription costs.

### Enterprise Framework Benchmark Synthesis

The following table synthesizes the core technical attributes, architectural paradigms, and runtime performance metrics of the analyzed frameworks, establishing a rigorous baseline for architectural decision-making.

| Framework Capability | Mem0 | Zep | LangMem |
| --- | --- | --- | --- |
| Primary Architecture | Vector + Knowledge Graph (Pro Tier) | Temporal Knowledge Graph | Flat Key-Value + Vector store |
| Target Paradigm | Context Token Compression & Personalization | High-Speed Relational & Temporal Context Mapping | Procedural Learning & Multi-Agent Swarm Orchestration |
| Average Retrieval Latency | 50ms – 200ms | < 50ms (Highly optimized for voice) | Variable (Entirely dependent on self-hosted DB tuning) |
| Graph Operations | Add/Delete constraints, Basic Cypher Filters | Full Node/Edge CRUD, Bulk episode ingest | N/A (Relies on external DB logic) |
| Procedural Updates | Implicit via prompt context updates | Implicit via high-confidence fact injection | Explicit via automated instruction/prompt optimization loops |
| Security & Compliance | SOC 2, HIPAA, BYOK natively supported | Production-grade group graphs and access controls | N/A (Self-Managed Infrastructure security applies) |
| Optimal Ecosystem | Universal (MCP Server, Python/JS SDKs, Vercel) | Universal (API, LlamaIndex, LangChain, AutoGen) | Strictly confined to LangGraph / LangChain environments |

The comparative data underscores a critical reality in AI engineering: there is no monolithic, universally superior solution for AI agent memory. Simple [LangChain](https://www.analyticsvidhya.com/blog/2023/05/langchain-one-stop-framework-building-applications-with-llms/) buffer memory suits early-stage MVPs and prototypes operating on 0-3 month timelines. Mem0 provides the most secure, feature-rich path for products requiring robust personalization and severe token-cost reduction with minimal infrastructural overhead. Zep serves enterprise environments where extreme sub-second retrieval speeds and complex ontological awareness justify the inherent complexity of managing graph databases. Finally, LangMem serves as the foundational, open-source toolkit for engineers prioritizing procedural autonomy and strict architectural sovereignty.

## Conclusion

The shift from simple AI systems to autonomous, goal-driven agents depends on advanced memory architectures. Instead of relying only on limited context windows, modern agents use multi-layered memory systems—episodic (past events), semantic (facts), and procedural (skills)—to function more like human intelligence. The key challenge today is not storage capacity, but effectively managing and organizing this memory. Systems must move beyond simply storing data (“append-only”) and instead focus on intelligently consolidating and structuring information to avoid noise, inefficiency, and slow performance.

Modern architectures achieve this by using background processes that convert raw experiences into meaningful knowledge. They also continuously refine how they execute tasks. At the same time, intelligent forgetting mechanisms—like decay functions and [time-based expiration](https://www.analyticsvidhya.com/blog/2022/05/a-comprehensive-guide-to-time-series-analysis-and-forecasting/)—help remove irrelevant information and prevent inconsistencies. Enterprise tools such as Mem0, Zep, and LangMem tackle these challenges in different ways. Each tool focuses on a different strength: cost efficiency, deeper reasoning, or adaptability. As these systems evolve, AI agents are becoming more reliable, context-aware, and capable of long-term collaboration rather than just short-term interactions.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="building-smarter-ai-agents-agentcore-long-term-memory-deep-d.md">
<details>
<summary>Building smarter AI agents: AgentCore long-term memory deep dive</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/>

# Building smarter AI agents: AgentCore long-term memory deep dive

Building AI agents that remember user interactions requires more than just storing raw conversations. While Amazon Bedrock AgentCore short-term memory captures immediate context, the real challenge lies in transforming these interactions into persistent, actionable knowledge that spans across sessions. This is the information that transforms fleeting interactions into meaningful, continuous relationships between users and AI agents. In this post, we’re pulling back the curtain on how the [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Memory long-term memory system works.

If you’re new to AgentCore Memory, we recommend reading our introductory blog post first: [Amazon Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/). In brief, AgentCore Memory is a fully managed service that enables developers to build context-aware AI agents by providing both short-term working memory and long-term intelligent memory capabilities.

## The challenge of persistent memory

When humans interact, we don’t just remember exact conversations—we extract meaning, identify patterns, and build understanding over time. Teaching AI agents to respond the same requires solving several complex challenges:

- Agent memory systems must distinguish between meaningful insights and routine chatter, determining which utterances deserve long-term storage versus temporary processing. A user saying “I’m vegetarian” should be remembered, but “hmm, let me think” should not.
- Memory systems need to recognize related information across time and merge it without creating duplicates or contradictions. When a user mentions they’re allergic to shellfish in January and mentions “can’t eat shrimp” in March, these needs to be recognized as related facts and consolidated with existing knowledge without creating duplicates or contradictions.
- Memories must be processed in order of temporal context. Preferences that change over time (for example, the user loved spicy chicken in a restaurant last year, but today, they prefer mild flavors) require careful handling to make sure the most recent preference is respected while maintaining historical context.
- As memory stores grow to contain thousands or millions of records, finding relevant memories quickly becomes a significant challenge. The system must balance comprehensive memory retention with efficient retrieval.

Solving these problems requires sophisticated extraction, consolidation, and retrieval mechanisms that go beyond simple storage. Amazon Bedrock AgentCore Memory tackles these complexities by implementing a research-backed long-term memory pipeline that mirrors human cognitive processes while maintaining the precision and scale required for enterprise applications.

## How AgentCore long-term memory works

When the agentic application sends conversational events to AgentCore Memory, it initiates a pipeline to transform raw conversational data into structured, searchable knowledge through a multi-stage process. Let’s explore each component of this system. https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/13/ML-19668-2.png

### 1. Memory extraction: From conversation to insights

When new events are stored in short-term memory, an asynchronous extraction process analyzes the conversational content to identify meaningful information. This process leverages large language models (LLMs) to understand context and extract relevant details that should be preserved in long-term memory. The extraction engine processes incoming messages alongside prior context to generate memory records in a predefined schema. As a developer, you can configure one or more Memory strategies to extract only the information types relevant to your application needs. The extraction process supports three built-in memory strategies:

- **Semantic memory**: Extracts facts and knowledge. Example:

```code
"The customer's company has 500 employees across Seattle, Austin, and Boston"
```

Code

- **User preferences**: Captures explicit and implicit preferences given context. Example:

```code
{“preference”: "Prefers Python for development work", “categories”: [“programming”, ”code-style”], “context”: “User wants to write a student enrollment website”}
```

Code

- **Summary memory**: Creates running narratives of conversations under different topics scoped to sessions and preserves the key information in a structured XML format. Example:

```code
<topic=“Material-UI TextareaAutosize inputRef Warning Fix Implementation”> A developer successfully implemented a fix for the issue in Material-UI where the TextareaAutosize component gives a "Does not recognize the 'inputRef' prop" warning when provided to OutlinedInput through the 'inputComponent' prop. </topic>
```

Code

For each strategy, the system processes events with timestamps for maintaining the continuity of context and conflict resolution. Multiple memories can be extracted from a single event, and each memory strategy operates independently, allowing parallel processing.

### 2. Memory consolidation

Rather than simply adding new memories to existing storage, the system performs intelligent consolidation to merge related information, resolve conflicts, and minimize redundancies. This consolidation makes sure the agent’s memory remains coherent and up to date as new information arrives.

The consolidation process works as follows:

1.  **Retrieval**: For each newly extracted memory, the system retrieves the top most semantically similar existing memories from the same namespace and strategy.
2.  **Intelligent processing**: The new memory and retrieved memories are sent to the LLM with a consolidation prompt. The prompt preserves the semantic context, thus avoiding unnecessary updates (for example, “loves pizza” and “likes pizza” are considered essentially the same information). Preserving these core principles, the prompt is designed to handle various scenarios:

```java
You are an expert in managing data. Your job is to manage memory store.
Whenever a new input is given, your job is to decide which operation to perform.

Here is the new input text.
TEXT: {query}

Here is the relevant and existing memories
MEMORY: {memory}

You can call multiple tools to manage the memory stores...
```

Java

Based on this prompt, the LLM determines the appropriate action:

-   **ADD**: When the new information is distinct from existing memories
-   **UPDATE**: Enhance existing memories when the new knowledge complements or updates the existing memories
-   **NO-OP**: When the information is redundant
3.  **Vector store updates**: The system applies the determined actions, maintaining an immutable audit trail by marking the outdated memories as INVALID instead of instantly deleting them.

This approach makes sure that contradictory information is resolved (prioritizing recent information), duplicates are minimized, and related memories are appropriately merged.

### Handling edge cases

The consolidation process gracefully handles several challenging scenarios:

-   **Out-of-order events**: Although the system processes events in temporal order within sessions, it can handle late-arriving events through careful timestamp tracking and consolidation logic.
-   **Conflicting information**: When new information contradicts existing memories, the system prioritizes recency while maintaining a record of previous states:

```java
Existing: "Customer budget is \$500"
New: "Customer mentioned budget increased to \$750"
Result: New active memory with \$750, previous memory marked inactive
```

Java

-   **Memory failures**: If consolidation fails for one memory, it doesn’t impact others. The system uses exponential backoff and retry mechanisms to handle transient failures. If consolidation ultimately fails, the memory is added to the system to help prevent potential loss of information.

## **Advanced custom** memory strategy configurations

While built-in memory strategies cover common use cases, AgentCore Memory recognizes that different domains require tailored approaches for memory extraction and consolidation. The system supports [built-in strategies with overrides](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-custom-strategy.html) for custom prompts that extend the built-in extraction and consolidation logic, letting teams adapt memory handling to their specific requirements. To maintain system compatibility and focus on criteria and logic rather than output formats, custom prompts help developers customize what information gets extracted or filtered out, how memories should be consolidated, and how to resolve conflicts between contradictory information.

AgentCore Memory also supports custom model selection for memory extraction and consolidation. This flexibility helps developers balance accuracy and latency based on their specific needs. You can define them via the APIs when you create the _memory\_resource_ as a strategy override or via the console (as shown below in the console screenshot).

https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/14/ML-19668-4.png

Apart from override functionality, we also offer [self-managed strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-self-managed-strategies.html) that provide complete control over your memory processing pipeline. With self-managed strategies, you can implement custom extraction and consolidation algorithms using any models or prompts while leveraging AgentCore Memory for storage and retrieval. Also, using the Batch APIs, you can directly ingest extracted records into AgentCore Memory while maintaining full ownership of the processing logic.

### Performance characteristics

We evaluated our built-in memory strategy across three public benchmarking datasets to assess different aspects of long-term conversational memory:

-   **LoCoMo**: Multi-session conversations generated through a machine-human pipeline with persona-based interactions and temporal event graphs. Tests long-term memory capabilities across realistic conversation patterns.
-   **LongMemEval**: Evaluates memory retention in long conversations across multiple sessions and extended time periods. We randomly sampled 200 QA pairs for evaluation efficiency.
-   **PrefEval**: Tests preference memory across 20 topics using 21-session instances to evaluate the system’s ability to remember and consistently apply user preferences over time.
-   **PolyBench-QA:** A question-answering dataset containing 807 Question Answer (QA) pairs across 80 trajectories, collected from a coding agent solving tasks in PolyBench.

We use two standard metrics: **_correctness_** and **_compression rate_**. LLM-based correctness evaluates whether the system can correctly recall and use stored information when needed. Compression rate is defined as output memory token count / full context token count, and evaluates how effectively the memory system stores information. Higher compression rates indicate the system maintains essential information while reducing storage overhead. This compression rate directly translates to faster inference speeds and lower token consumption–the most critical consideration for deploying agents at scale because it enables more efficient processing of large conversational histories and reduces operational costs.

| Memory Type | Dataset | Correctness | Compression Rate |
| :---------- | :------ | :---------- | :--------------- |
| **RAG baseline**<br> <br>**(full conversation history)** | LoCoMo | 77.73% | 0% |
| LongMemEval-S | 75.2% | 0% |
| PrefEval | 51% | 0% |
| **Semantic Memory** | LoCoMo | 70.58% | 89% |
| LongMemEval-S | 73.60% | 94% |
| **Preference Memory** | PrefEval | 79% | 68% |
| **Summarization** | PolyBench-QA | 83.02% | 95% |

The retrieval-augmented-generation (RAG) baseline performs well on factual QA tasks due to complete conversation history access, but struggles with preference inference. The memory system achieves strong practical trade-offs: though information compression leads to slightly lower correctness on some factual tasks, it provides 89-95% compression rates for scalable deployment, maintaining bounded context sizes, and performs effectively at their specialized use cases.

For more complex tasks requiring inference (understanding user preferences or behavioral patterns), memory demonstrates clear advantages in both performance accuracy and storage efficiency—the extracted insights are more valuable than raw conversational data for these use cases.

Beyond accuracy metrics, AgentCore Memory delivers the performance characteristics necessary for production deployment.

-   Extraction and consolidation operations complete within 20-40 seconds for standard conversations after the extraction is triggered.
-   Semantic search retrieval (`retrieve_memory_records` API) returns results in approximately 200 milliseconds.
-   Parallel processing architecture enables multiple memory strategies to process independently; thus, different memory types can be processed simultaneously without blocking each other.

These latency characteristics, combined with the high compression rates, enable the system to maintain responsive user experiences while managing extensive conversational histories efficiently across large-scale deployments.

## Best practices for long-term memory

To maximize the effectiveness of long-term memory in your agents:

-   **Choose the right memory strategies**: Select built-in strategies that align with your use case or create custom strategies for domain-specific needs. Semantic memory captures factual knowledge, preference memory tailors towards individual preference, and summarization memory distills complex information for better context management. For example, a customer support agent might use semantic memory to capture customer transaction history and past issues, while summarization memory creates short narratives of current support conversations and troubleshooting workflows across different topics.
-   **Design meaningful namespaces**: Structure your namespaces to reflect your application’s hierarchy. This also enables precise memory isolation and efficient retrieval. For example, use `customer-support/user/john-doe` for individual agent memories and `customer-support/shared/product-knowledge` for team-wide information.
-   **Monitor consolidation patterns**: Regularly review what memories are being created (using `list_memories` or `retrieve_memory_records` API), updated, or skipped. This helps refine your extraction strategies and helps the system capture relevant information that’s better fitted to your use case.
-   **Plan for async processing:** Remember that long-term memory extraction is asynchronous. Design your application to handle the delay between event ingestion and memory availability. Consider using short-term memory for immediate retrieval needs while long-term memories are being processed and consolidated in the background. You might also want to implement fallback mechanisms or loading states to manage user expectations during processing delays.

## Conclusion

The Amazon Bedrock AgentCore Memory long-term memory system represents a significant advancement in building AI agents. By combining sophisticated extraction algorithms, intelligent consolidation processes, and immutable storage designs, it provides a robust foundation for agents that learn, adapt, and improve over time.

The science behind this system, from research-backed prompts to innovative consolidation workflow, makes sure that your agents don’t just remember, but understand. This transforms one-time interactions into continuous learning experiences, creating AI agents that become more helpful and personalized with every conversation.

Resources:

– [AgentCore Memory Docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)

– [AgentCore Memory code samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory/)

– [Getting started with AgentCore – Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/850fcd5c-fd1f-48d7-932c-ad9babede979/en-US)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="context-rot-why-ai-gets-worse-the-longer-you-chat-and-how-to.md">
<details>
<summary>Context Rot: Why AI Gets Worse the Longer You Chat (And How to Fix It)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.producttalk.org/context-rot/>

# Context Rot: Why AI Gets Worse the Longer You Chat (And How to Fix It)

Have you ever noticed that AI gets worse the longer you talk to it?

I first noticed this when I was trying to fix bugs on [Replit](https://replit.com/?ref=producttalk.org). I'd spin in an endless cycle of asking the agent to fix something and it would report back that it fixed it, even though it hadn't. I learned through trial and error that starting a new conversation often fixed the problem.

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/replit-battle.pngMe battling with Replit trying to get it to remove a simple error message.

This isn't unique to Replit. I see it everywhere: [ChatGPT](https://chatgpt.com/?ref=producttalk.org), [Claude Code](https://code.claude.com/docs/en/overview?ref=producttalk.org), the [Lovable](https://lovable.dev/?ref=producttalk.org) agent.

Why is this? Recent research is shining a light onto why this happens. It's called "context rot." The more input we give a large language model, the worse it tends to perform. It might ignore some input or over-index on other input. How performance degrades is complex, but we are starting to get a better understanding of the common patterns.

With large language models, the quality of our inputs affect the quality of the output. There are a couple of ways we can affect the quality of the input:

- We can clearly specify what we want. (Often referred to as "prompt engineering.")
- We can provide the needed context so that the LLM can do what we want. (Often referred to as "context engineering.")

But we are learning that it isn't this simple. We also have to account for context rot. So we need to add a third lever to our list:

- We can manage the usage of the context window.

Today, I'm going to:

- explain what the context window is
- summarize the research on context rot so you understand how to optimize LLM performance
- show how you can learn about the context window and see what's in it
- provide actionable tips on how you can manage the context window when using LLMs in your day-to-day work.

If you are starting to use a command-line interface like Claude Code or [Codex](https://openai.com/codex/?ref=producttalk.org) or you are using [Claude Cowork](https://claude.com/product/cowork?ref=producttalk.org) to create your own AI workflows, this article will help you understand why LLM performance degrades over the course of the conversation and what you can do to prevent it.

If you are an audio/visual learner, start with this overview video and then dive into the rest of the article.

[The AI That Forgets](https://www.youtube.com/watch?v=gDqv-fgfA80)

## What is a context window?

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/What-is-a-context-window-1.pngThe context window acts as the model's short-term memory.

The context window is the metaphor we use for what captures the input into a large language model. You can think about it as the model's short-term memory. It's everything that the model can work with at one time.

A context window has a fixed size. It's not infinite. The amount of input you can enter at once is constrained by the size of the context window. And the size varies from model to model.

| Model | Context Window |
| --- | --- |
| Claude Opus 4.5 | 200K tokens |
| Claude Sonnet 4.5 | 200K tokens <br>(1M at usage tier 4) |
| GPT-5.2 | 400K tokens |
| Gemini 2.5 Pro | 1M tokens |

If you read my ["How Does ChatGPT Work?" article](https://www.producttalk.org/how-does-chatgpt-work/), you learned that the input into the model includes more than just what you type in. Each application adds a system prompt that gets prepended to your user message. Depending on the application context, the system prompt can include tool descriptions (e.g. like from an MCP server), available skills, plug-ins, and much more.

In a back-and-forth conversation, the entire conversation history is often included in the context window on every turn. This is the only way the model can follow the conversation.

Even though many models have large context windows, in practice, the context window can fill up quickly. And we'll see that filling the context window up can cause problems.

💡

**Why do context windows have a fixed size?**

There are many factors that constrain the context window size including the amount of compute required to process the input, the amount of memory required to remember values during processing, and the size of input used during training.

## What is context rot?

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/Context-rot-in-first-half-of-window.png

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/Context-rot-in-seond-half-of-window.png

How context degrades varies based on how full the context window is.

In November 2023, [Liu et al](https://arxiv.org/abs/2307.03172?ref=producttalk.org) released a paper called "Lost in the Middle" that introduced the first evidence of context rot. The authors found that as the context window filled up, models started to favor tokens at the start of the input and tokens at the end of the input. Tokens in the middle "got lost." Hence the name "Lost in the Middle."

In 2025, several more researchers published papers exploring this pattern and the term "context rot" was coined. Here's a quick synopsis of what studies to date have found:

- The initial Liu et al (2023) research used simple "needle-in-a-haystack" tasks to test context degradation. In a "needle-in-a-haystack" task, the model is asked if a sentence ("the needle") is in the context ("the haystack"). The study found that as the context window filled up, models performed worse on these simple tasks.
- [Paulsen (2025)](https://arxiv.org/abs/2509.21361?ref=producttalk.org) showed that context degraded over a wide variety of task types (not just "needle-in-a-haystack" tasks) and often with far fewer tokens for more complex tasks.
- [Veseli et al (2025)](https://arxiv.org/abs/2508.07479?ref=producttalk.org) found that the U-shaped pattern (where the LLM favors tokens at the beginning and the end) that Liu et al (2023) found only persists when the context is less than 50% full. When the context is greater than 50% full, Veseli et al (2025) found a different pattern: Context degrades by distance from the end, where the LLM favors more recent tokens, then middle tokens, over early tokens.
- Researchers theorized that the models were struggling with retrieval, meaning the model couldn't find the needle in the haystack. But [Du et al (2025)](https://arxiv.org/abs/2510.05381?ref=producttalk.org)—through some clever experiments—showed that it's not a retrieval issue. It's simply a function of the input length. In one of their more fascinating experiments, they replaced all of the non-"needle" tokens in the input with blank spaces. Their thinking was if this was a retrieval problem, the needle should now be obvious—but they still saw the same evidence of context degradation in these modified tasks.

So what does all of this mean?

Even with a large context window size, we don't want to fill it up. Performance degrades as it fills up. And it degrades in different ways.

- When the context window is less than 50% full, the model will lose tokens in the middle.
- When the context window is greater than 50% full, the model will lose the earliest tokens.

This research helps me understand why Claude sometimes ignores my CLAUDE.md rules. And I now have a clear way to fix it. More on that in a bit.

## It's Hard to Manage Context Using LLMs in the Web Browser

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/Browser-limitations.pngWeb interfaces for popular models don't provide any visibility into how full the context window is.

First, we have to acknowledge a major limitation of using ChatGPT, Claude, or [Gemini](https://gemini.google.com/app?ref=producttalk.org) in the web browser. These applications give us no visibility into how full the context window is.

You might have used ChatGPT since the day it came out and not even known what a context window is. That's a problem.

In fact, these tools make it seem like the context window is infinite, as they allow you to chat forever. But now you know they aren't. Context degrades over time. The longer your chat gets, the worse the model will perform.

It also means you have little control over what goes in the context window (beyond what you type), how and when to condense it or clear it, or even know when you might need to do so. That means you can't influence how the model performs. Your only tool for managing context rot in a web browser is starting a fresh chat.

Starting a new chat clears the context window. And you should do this often. If you are working with an LLM in your web browser, start a fresh chat whenever:

- You start a new topic.
- The model does something problematic and you want it to try again.
- The conversation starts to get long (e.g. more than 15 messages). Ask the model to summarize the conversation and use the summary to start a fresh chat.

These tips will help you keep the context window small.

But we can do so much more when we can see what's in the context window, how full it is, and know exactly when to mitigate it. This is one of the things I love about Claude Code.

## Claude Code Gives Full Visibility Into the Context Window

Learning about the context window and how to manage it is one of those skills that we are all going to have to develop as we learn to build AI products. And using Claude Code day in and day out is teaching me how to do exactly that.

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/The-context-window-percentage.pngThe status line tells me that the context window is 12% full.

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/context-slash-command.png

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/clear-slash-command.png

https://storage.ghost.io/c/57/9b/579b6dca-f48a-4307-844f-f0533595d058/content/images/2026/02/compact-slash-command.png

Similarly, I can use the /context command to examine what's in the context window. And I can use the /clear command to clear the context. I can also use the /compact command to tell Claude how to compact the conversation.

These tools are all built in to Claude Code by default. Claude will also automatically compact the conversation when the context window starts to get full. But I like having access to the tools myself.

Being able to see how full the context window is and being able to see how the model performs at different percentages helps me hone my judgment on where I want the context window to be for different tasks.

For example, I don't worry too much about how full the context window is when I ask the agent to create a new task in my task management system. That task is simple. Claude is simply creating a task file based on the contents I give it. But during planning (a much more complex task), I have the agent update a plan file so that I can continuously /clear the context and get the best performance from the model throughout the planning session.

By the way, if you haven't tried Claude Code and want to, check out my series:

- [Claude Code: What It Is, How It's Different, and Why Non-Technical People Should Use It](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)
- [Stop Repeating Yourself: Give Claude Code a Memory](https://www.producttalk.org/give-claude-code-a-memory/)
- [How to Use Claude Code Safely: A Non-Technical Guide to Managing Risk](https://www.producttalk.org/how-to-use-claude-code-safely/)
- [How to Choose Which Tasks to Automate with AI (+50 Real Examples)](https://www.producttalk.org/how-to-choose-which-tasks-to-automate-with-ai/)
- [How to Build AI Workflows with Claude Code (Even If You're Not Technical)](https://www.producttalk.org/how-to-build-ai-workflows-with-claude-code/)
- [How to Use Claude Code: A Guide to Slash Commands, Agents, Skills, and Plug-Ins](https://www.producttalk.org/how-to-use-claude-code-features/)
- [How to Share Your AI Context and Skills Across Devices](https://www.producttalk.org/how-to-share-your-ai-context-and-skills/)

💡

This series was inspired by my personal usage of Claude Code. I'm a big fan and I like to share what works for me with readers.

I have not received any compensation from [Anthropic](https://www.anthropic.com/?ref=producttalk.org) for writing this series. And you can trust that if that ever changes, I will disclose it. This is not only required by the FTC here in the US, but I strongly believe it is the right thing to do. You can count on me to do so.

With this foundation, let's now look at how you can effectively manage the context window in Claude Code. We'll cover how you can:

- Monitor the context window percentage
- Examine the contents of the context window
- Keep your CLAUDE.md small, but effective
- Use the file system to offload conversation context
- Use /compact and /clear effectively
- Add agents, skills, and plug-ins without filling the context window
- Expand the context window by offloading token-intensive tasks to sub-agents
- Create token-efficient MCP servers
- Manage "lost in the middle" and recency bias token loss in long conversations

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="memory-optimization-strategies-in-ai-agents-by-nirdiamant-me.md">
<details>
<summary>Memory Optimization Strategies in AI Agents</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://medium.com/@nirdiamant21/memory-optimization-strategies-in-ai-agents-1f75f8180d54>

# Memory Optimization Strategies in AI Agents

[https://miro.medium.com/v2/resize:fill:32:32/1*4PgkOZRmtSG670T_oDYqXw.jpeg](https://medium.com/@nirdiamant21?source=post_page---byline--1f75f8180d54---------------------------------------)

Nirdiamant

14 min read

·

Aug 1, 2025

What separates a forgetful chatbot from a truly smart AI agent? Imagine chatting with a virtual travel assistant for months, only to have it repeatedly ask for your preferences as if meeting you for the first time each conversation. Frustrating, right? The key difference lies in memory — not just having memory, but using it smartly. Just as humans selectively remember important details and let trivial ones fade, AI agents need clever strategies to remember what matters and forget what doesn’t.

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/0*0Cq0Z9Xzav_YV7iX.png

## Why Memory Matters for AI Agents

Early AI systems were mostly stateless — they processed each query independently, with no memory of past interactions. This is like talking to someone with severe memory loss: every conversation starts from scratch. A basic thermostat, for example, doesn’t “remember” yesterday’s temperature; it just reacts to the current reading. But add memory to an AI system, and it transforms into something smarter. A smart thermostat can learn your schedule by remembering past data — turning down heat when you’re typically away, saving energy based on patterns.

In conversational AI, memory is even more important. Consider a customer support chatbot that can recall your previous support tickets: it avoids making you repeat information and can tailor its answers using what it “knows” about your past issues. Similarly, ChatGPT keeps a chat history within a session so it doesn’t forget context from one message to the next. Without this, each user message would be treated alone, leading to broken, frustrating conversations.

However, memory in AI agents is not as simple as it is for humans. Large language models have limited context windows — they can only consider a fixed amount of text at a time. If you simply add the entire conversation history every time, you quickly hit these limits. The model might start ignoring older content or lose coherence if the context is too long. Moreover, storing everything slows down processing and increases costs. The challenge is clear: how to keep important information without overloading the system.

## Short-Term vs Long-Term: Learning from Human Memory

AI researchers often look to human memory for inspiration. We have short-term memory for recent stuff — like remembering a phone number just long enough to dial it — and long-term memory for knowledge we keep over days, months, or years. AI agents organize memory in similar ways:

**Short-Term Memory (Working Memory)**: This is the AI’s immediate context within a single session. In a chatbot, it might be the last few user and AI messages stored in the prompt. For instance, if you tell a travel assistant, “Book a trip to Paris in December,” it will keep track of “destination: Paris “ and “timing: December” during that chat. This short-term memory is like sticky notes on the agent’s desk — handy for the current conversation, but they get thrown away once the session ends.

**Long-Term Memory**: This is information the agent keeps across sessions and over time. It’s often stored in external databases so the AI can look it up when needed. If you chat with your AI travel agent again months later and say, “Plan something like last time,” it should recall that “last time” you went to Paris in December. That’s long-term memory at work — like the agent’s personal diary that keeps experiences over time.

The bottom line: giving AI the right kind of memory makes it behave less like a forgetful goldfish and more like a thoughtful companion. But simply having memory isn’t enough; it must be used efficiently.

## From Simple to Smart: Strategies for Memory Management

Let’s explore how AI agents manage their memory, from simple approaches to advanced techniques.

## 1\. Sequential (Keep-It-All) — The Simple Approach

The most basic method is what early chatbots did: keep adding every new message to the conversation history, and feed the whole thing to the model each time. This sequential memory chain keeps the full conversation record. It’s like carrying the entire transcript of a conversation as context.

The benefit is simplicity — nothing fancy, just raw memory of everything said. In short conversations, this works fine and ensures no detail is lost. However, as conversations grow, this approach runs into trouble. The context can quickly overflow the model’s limit, or become so large that processing it is slow and expensive. It’s as if you tried to recall every word of every conversation you’ve had in the past month whenever someone asks you a question — your brain would overload.

## 2\. Sliding Window — Focus on Recent Messages

A better approach is the sliding window memory. Instead of keeping the entire history, the agent keeps only the most recent N messages as context. As new messages come in, the oldest ones get dropped — the window slides forward. This copies how humans naturally focus on the latest part of a conversation; we tend to recall what was just said and might lose track of details from an hour ago.

**Benefits**: The sliding window ensures the context stays within a manageable size. It keeps the conversation relevant and recent, which is often enough since recent dialogue usually guides the next response. Performance stays consistent no matter how long the overall conversation.

**Drawbacks**: The obvious downside is that the agent might “forget” important information from earlier in the conversation. If a crucial detail was mentioned 50 messages ago and falls out of the window, it won’t remember it.

## 3\. Summarization — Distill the Important Parts

What if, instead of dropping old information entirely, the AI could remember it in a condensed form? This is where summary-based memory comes in. The idea is to regularly take the conversation so far, create a brief summary of the important points, and use that summary as a stand-in for the full history.

Think of it like taking notes during a long meeting. Rather than recalling every sentence said, you write down key decisions and facts. Later, those notes help your memory without you needing to relive the entire meeting. AI agents do something similar: after every 10 messages or when the context gets too large, they create a summary of earlier dialogue, then discard the detailed logs.

**Benefits**: Summarization allows the AI to keep relevant information over very long conversations without exceeding context limits. The agent can maintain awareness of past topics, decisions, or user preferences that occurred far back in the conversation.

**Drawbacks**: The quality of this approach depends on the quality of the summaries. Important details can be lost — a summary might miss a seemingly minor detail that later turns out to be crucial. Also, creating summaries adds extra computation and potential delays.

## 4\. Retrieval-Based Memory — Smart Recall

Now we arrive at the advanced approach: retrieval-based memory. This strategy gives the AI agent something like an external brain or a personal search engine. Instead of pushing a fixed window or a summary into the model, the conversation history is stored in an external database, and when needed, the agent retrieves the most relevant pieces to include in context.

Here’s how it works: imagine every conversation turn the agent encounters is a book in a library. When a new query comes, the agent doesn’t read the entire library (too slow!) — it quickly checks the catalog to find which books might be relevant, pulls out just those, and reads them to answer the query.

**Benefits**: Retrieval-based memory allows an agent to remember large amounts of information over long periods. The agent can surface details from much earlier in a conversation or from long-term knowledge even if the current context window is small. The memory adapts to the current question — only relevant info is brought in.

**Drawbacks**: The complexity of setup and maintenance is higher. You need systems to store information, algorithms for fast search, and careful tuning to ensure relevant information is retrieved. If the retrieval isn’t accurate, the agent might be led astray.

## Next-Generation Memory Architectures

Beyond these core strategies, cutting-edge AI systems are implementing even more sophisticated approaches that push the boundaries of what’s possible.

## Memory-Augmented Transformers

To understand this, imagine a regular AI model as a student taking a test with only a small piece of paper for scratch work. No matter how long or complex the test questions get, the student can only work with what fits on that one small paper. If the test has 100 questions, by the time they reach question 50, they’ve run out of space and have to erase their notes from the earlier questions.

Memory-augmented transformers solve this by giving the AI a stack of sticky notes it can use alongside its main scratch paper. Here’s how it works:

1.  **The main paper** (regular context window) handles the immediate conversation, just like before
2.  **The sticky notes** (memory tokens) store important information from earlier in the conversation
3.  **When the main paper fills up**, instead of erasing everything, the AI writes key points on sticky notes
4.  **Later, when needed**, the AI can look back at these sticky notes to remember what happened before

For example, let’s say you’re having a long planning session with an AI about organizing a conference. Early in the conversation, you mention your budget is $50,000 and you prefer morning sessions. As the conversation grows longer, this information would normally get pushed out of the AI’s immediate memory. But with memory tokens, the AI writes “Budget: $50,000, prefers morning sessions” on a sticky note.

Hours later, when you ask “What venues fit our requirements?”, the AI can check its sticky notes, see your budget and timing preferences, and give you relevant suggestions even though that information was mentioned way earlier in the conversation.

The clever part is that the AI learns which information deserves a sticky note and which can be safely forgotten. It’s like having a smart assistant who knows the difference between important decisions and casual small talk.

## Hierarchical Memory Systems

Just as your brain has different types of memory operating at different time scales, advanced AI agents now implement multi-layered memory hierarchies. Picture it like a company’s filing system:

-   **Working memory** is like the papers on your desk — immediately accessible but limited in space
-   **Short-term memory** is like your filing cabinet — larger capacity, quick access for recent projects
-   **Long-term memory** is like the company archives — vast storage that requires more effort to access but preserves everything important

These systems automatically manage what information lives at each level, promoting important details from working memory to long-term storage while letting trivial information fade away. It’s like having a smart assistant who knows exactly which emails to keep in your inbox, which to file away, and which to delete.

## Compression and Consolidation

Modern memory systems implement sophisticated compression techniques inspired by how our brains consolidate memories during sleep. Instead of storing raw conversation text, these systems compress experiences into dense representations that capture the essential meaning while using far less storage space.

But how does this actually work under the hood? Let’s break down the algorithmic process:

**Step 1: Convert to Embeddings** First, the system converts text into numerical vectors (embeddings) that capture semantic meaning. Instead of storing “I love Italian food, especially pasta with marinara sauce,” it stores a dense vector like \[0.23, -0.45, 0.67, …\] that mathematically represents this preference.

**Step 2: Identify Patterns and Clusters** The system groups similar memories together. All your food preferences might cluster in one area, travel preferences in another. It’s like organizing your memories into themed folders, where each folder can be represented by a single “prototype” vector that captures the essence of that category.

**Step 3: Hierarchical Abstraction** Instead of remembering every individual conversation turn, the system builds layers of abstraction:

-   **Level 1**: “User mentioned liking pasta on Tuesday”
-   **Level 2**: “User prefers Italian cuisine”
-   **Level 3**: “User has strong food preferences”

Each level up uses fewer numbers to store more general patterns.

**Step 4: Importance Scoring** The system assigns relevance scores to memories using attention mechanisms. Recent interactions get higher scores, frequently referenced topics get higher scores, and emotionally significant moments (detected through language patterns) get preserved with higher fidelity.

**Step 5: Lossy Compression** Like how JPEG compresses images by removing details the eye won’t miss, the system removes conversational details that don’t affect future interactions. It might compress “It was a really, really, really good restaurant” down to just “positive restaurant experience” while preserving the restaurant name and your rating.

**Step 6: Reconstruction When Needed** When the AI needs to recall something, it doesn’t retrieve the exact original text. Instead, it reconstructs a response based on the compressed representation, kind of like how you might retell a story in your own words rather than reciting it verbatim.

Think of it like the difference between storing a full movie file versus storing just the plot summary, key quotes, and emotional moments. The compressed version takes up much less space but still captures what matters for future reference. These systems can achieve dramatic space savings while maintaining the ability to recall important details when needed.

## Operating System Memory Management

Some of the most innovative approaches borrow concepts from computer operating systems. Just as your computer manages memory by moving data between RAM and hard disk storage, these AI systems implement “virtual memory” for conversations.

The agent maintains a small “active” memory (like RAM) for immediate processing, while storing the bulk of its memories in external storage (like a hard drive). When it needs to recall something from long ago, it can “page in” that memory, temporarily bringing it into active context. This allows virtually unlimited conversation length while maintaining fast response times.

## Graph-Based Memory Networks

Instead of storing memories as simple text, advanced systems organize information as interconnected knowledge graphs. Think of this like how your brain connects related memories — remembering your college friend might trigger memories of the dorm, the cafeteria food, that one professor, and so on.

These graph-based systems capture not just what was said, but the relationships between different pieces of information. When you mention “that restaurant we discussed,” the system can traverse its knowledge graph to find not just the restaurant name, but also your dietary preferences, the occasion you were planning for, and your budget constraints — all connected in a web of related memories.

## Advanced Techniques for Memory Optimization

Beyond the core strategies above, there are additional tricks AI developers use:

**Token Compression**: Pack more information in fewer tokens by using more efficient phrasing. An agent could rephrase a long paragraph into a short statement that conveys the same facts.

**Smart Filtering**: Not all pieces of memory are equally important. AI agents can assign scores to potential memory contents to decide what to keep. If the conversation is about travel plans, the agent might score context related to “flights” and “hotels” higher than an offhand joke made earlier.

**Dynamic Memory Allocation**: Some advanced systems adjust how they use memory based on context complexity. If the user asks a very complex question, the agent might allocate more of its context budget to pulling in relevant background info.

**Strategic Forgetting**: Counterintuitively, forgetting can be a feature. AI agents are now being trained in strategic forgetting, meaning they learn rules for what to keep and what to remove from memory. Once a task is completed, the agent might “forget” the false starts and errors that happened along the way.

**Temporal Awareness**: Advanced memory systems understand time and can weight recent information more heavily than older information, or conversely, identify patterns that emerge over long time periods.

**Memory Consolidation**: Like how human brains replay and strengthen important memories during rest, AI systems can implement background processes that identify and reinforce key information while discarding noise.

## Real-World Examples

**Personal Travel Assistant**: In January, you chatted about a dream vacation to Paris, including preferred hotels and that you love traveling by train. By June, when you say, “Hey, plan something like last time but for July,” the AI instantly recalls that “last time” refers to Paris and that you prefer trains over flights. It remembers your hotel preference and travel mode, but it didn’t need to remember that you joked about buying woolen socks.

**Customer Support Chatbot**: You contact a support AI about a product issue. Two weeks later, the problem returns and you come back. A well-designed support agent will retrieve the context of your previous interaction — it knows what you tried already. It greets you with, “I see last time we updated your device drivers; let’s explore further solutions.”

**AI Coding Assistant**: Consider an AI pair-programmer that you’ve been using over months. It has seen the evolution of your project. Initially, it suggested some outdated library and you firmly told it to never use that again. An optimized assistant will have strategically remembered that feedback and avoids the wrong suggestion in future sessions.

## Choosing the Right Strategy

The choice of memory strategy depends on your specific use case, technical constraints, and user needs. Here’s a comprehensive guide to help you decide:

## For Simple Applications

**Sequential (Keep-It-All)**: Use when you have very short interactions (under 10 exchanges) and need perfect recall. Good for simple Q&A bots or brief customer service interactions.

**Sliding Window**: Perfect for medium-length conversations where recent context matters most. Ideal for real-time chat applications, gaming NPCs, or task-focused assistants where older information naturally becomes irrelevant.

## For Long-Form Interactions

**Summarization**: Choose when you need to maintain context over long conversations but can accept some information loss. Great for therapy bots, educational tutors, or creative writing assistants where the overall flow matters more than exact details.

**Retrieval-Based Memory**: Essential for applications requiring accurate recall of specific facts over time. Perfect for personal assistants, customer support systems, or any agent that needs to reference past interactions precisely.

## For Advanced Applications

**Memory-Augmented Transformers**: Use when you need to handle extremely long conversations or documents while maintaining detailed recall. Ideal for research assistants, complex problem-solving systems, or agents working with large knowledge bases.

**Hierarchical Memory Systems**: Choose for sophisticated applications that need different types of memory (working, short-term, long-term). Perfect for personal AI companions, enterprise assistants, or any system requiring human-like memory organization.

**Graph-Based Memory Networks**: Essential when relationships between information matter as much as the information itself. Ideal for recommendation systems, knowledge management tools, or agents that need to understand complex interconnections.

## For Resource-Constrained Environments

**Token Compression**: Use when you have strict computational limits but still need decent memory. Good for mobile applications, edge computing, or high-volume services where cost matters.

**Smart Filtering + Strategic Forgetting**: Perfect for applications that generate lots of noise but need to preserve important signals. Ideal for social media monitoring, news analysis, or any high-volume data processing.

## For Specialized Needs

**Operating System Memory Management**: Choose for applications with highly variable conversation lengths and unpredictable memory needs. Perfect for customer service platforms, multi-user systems, or applications with diverse use cases.

**Compression and Consolidation**: Use for applications that need long-term learning while managing storage costs. Ideal for personal assistants that improve over months/years, or systems that need to learn user patterns over time.

**Dynamic Memory Allocation**: Essential for applications with varying complexity levels. Perfect for educational systems that adapt to student needs, or assistants that handle both simple queries and complex research tasks.

**Temporal Awareness**: Use when timing and sequence matter significantly. Ideal for scheduling assistants, project management tools, or any system where understanding “when” is as important as “what.”

## Hybrid Approaches (Recommended for Production)

Most successful systems combine multiple strategies:

-   **Sliding Window + Retrieval**: Immediate context plus searchable history
-   **Summarization + Graph Networks**: Compressed narrative plus relationship mapping
-   **Hierarchical + Compression**: Multi-level memory with efficient storage
-   **Token Compression + Smart Filtering**: Resource efficiency with quality preservation

## Decision Framework

Ask yourself these questions:

1.  **How long are typical interactions?** (Short → sliding window, Long → summarization/retrieval)
2.  **How important is exact recall?** (Critical → retrieval/memory-augmented, Flexible → summarization)
3.  **What are your resource constraints?** (Limited → compression/filtering, Flexible → hierarchical/graph)
4.  **Do relationships between information matter?** (Yes → graph networks, No → simpler approaches)
5.  **Will the system learn over time?** (Yes → consolidation/temporal awareness, No → session-based approaches)
6.  **How many users will you serve?** (Few → sophisticated approaches, Many → efficient compression)

The key is starting simple and evolving your memory strategy as your application grows in complexity and user base.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="memory-systems-for-ai-agents-what-the-research-says-and-what.md">
<details>
<summary>Memory Systems for AI Agents: What the Research Says and What You Can Actually Build</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://stevekinney.com/writing/agent-memory-systems>

March 24, 2026

# Memory Systems for AI Agents: What the Research Says and What You Can Actually Build

The old short-term/long-term taxonomy doesn't capture what modern agent memory systems actually do. A new three-axis framework—Forms, Functions, and Dynamics—maps the design space from flat vector stores to RL-driven memory management. Here's what the research says and what you can build today.

I’ve been building an agent memory system for the last few days, and it sent me down one of those rabbit holes where you start reading one paper on [arXiv](https://arxiv.org/) and re-surface three hours later with forty browser tabs and a completely different understanding of the problem. The thing that triggered it was a simple frustration: every agent I use— [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Cursor](https://cursor.com/), custom stuff I’ve built with the [Vercel AI SDK](https://ai-sdk.dev/)—forgets everything between sessions. They treat every conversation like their first. I’ve explained my project structure, my preferences, my constraints, and then the context window fills up or the session ends and all of that knowledge evaporates.

Yes, I know this is increasingly _less_ true as [Claude Code and others have rolled out their own, built-in memory systems](https://code.claude.com/docs/en/memory) over the last few weeks. But, this was _always_ meant to be more of an intellectual exercise than anything else.

Apparently, I was not the only person engaged in this intellectual exercise. The Research Community™ has been remarkably productive on this problem over the last year. In December 2025, Hu et al. published [“Memory in the Age of AI Agents”](https://arxiv.org/abs/2512.13564)—a 107-page survey that attempts to unify a fragmented field. (They also maintain a [companion paper list on GitHub](https://github.com/memory-agent/memory-agent-papers) that’s actively updated—if that’s your jam.) Dozens of other papers have landed since: [A-Mem](https://arxiv.org/abs/2502.12110) bringing [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)-style linked notes to agent memory with 85–93% token reduction, [StructMemEval](https://arxiv.org/abs/2502.13649) showing that simple retrieval can outperform complex memory hierarchies, [Memori](https://arxiv.org/abs/2503.00760) achieving 81.95% accuracy at 5% of full context cost using semantic triples, and a bunch more I’ll reference as we go along on this journey. (And yes, that was just an excuse to use “Zettelkasten” in a sentence unironically.)

The old taxonomy—short-term memory versus long-term memory—isn’t really a thing anymore. It doesn’t capture what modern agent memory systems actually do. The survey proposes **a three-axis framework** that I’ve found genuinely useful for thinking about this kind of stuff: **Forms** (Where does memory live?), **Functions** (Why does the agent need memory?), and **Dynamics** (How does memory operate over time?). Let’s walk through what the research says at each axis, what’s practical today versus what’s still on the research frontier, and the design decisions you’ll face if you’re building a memory system for your own agents—not that I can advise that.

One thing I want to be super upfront about: I’m synthesizing a lot of material here. What follows is basically me selfishly synthesizing my notes in an attempt to better understand. I’ve read the papers and I’ve been building against some of these ideas, but I’m not a memory systems researcher. If I’ve mischaracterized someone’s work, call me out in the comments section that doesn’t exist.

## The three forms: where does memory live?

The first axis asks a deceptively simple question: where does the memory physically reside? The answer splits into three categories, and the split matters because it determines what you can actually _build_ with hosted models versus what requires running your own infrastructure.

### Token-level memory

Let’s start with the one we’re all familiar with—and the one you’ll _actually_ use.

**Token-level memory** is memory stored as explicit, discrete, human-readable units—text chunks, facts, user profiles, conversation logs. You write it to a database or the filesystem, you read it back, you stuff it into the prompt. It’s the form that works with any model, hosted or self-hosted, because it operates entirely outside the model’s internals. You can inspect it, debug it, edit it, and swap the underlying model without touching your memory layer.

This is what [Mem0](https://github.com/mem0ai/mem0), [Letta](https://github.com/letta-ai/letta) (née MemGPT), [Zep](https://github.com/getzep/zep), and most production memory frameworks implement. And for good reason: it’s the only form that’s actually tractable if you’re using a hosted frontier model through an API.

But “token-level” isn’t a single design. There’s a spectrum of topological complexity within it, and where you land on that spectrum matters:

- **Flat (1D):** A bag of entries with vector search over them. You store facts, you embed them, you retrieve the most similar ones at query time. Mem0 and MemGPT both started here. It’s the simplest approach, and it works surprisingly well when paired with a good retrieval pipeline. Most systems should start here.
- **Planar (2D):** Entries connected via explicit relationships—graphs, trees, linked notes. A-Mem’s [Zettelkasten-style links](https://arxiv.org/abs/2502.12110), Zep’s temporal knowledge graph, [RAPTOR](https://arxiv.org/abs/2401.18059)’s recursive abstractive tree. These structures enable multi-hop reasoning—following chains of connections to answer questions that no single entry can answer alone. The trade-off is maintenance complexity. Graphs need to be pruned, updated, and kept consistent as new information arrives.
- **Hierarchical (3D):** Multiple abstraction layers with cross-layer links. Raw entries at the bottom, cluster summaries in the middle, global abstractions at the top. [HippoRAG](https://arxiv.org/abs/2405.14831) implements a dual-layer approach inspired by how the hippocampus indexes memories. Most powerful for complex reasoning, most complex to build and maintain.

Here’s the practical guidance: flat is probably right for your system. I know that sounds anticlimactic after describing the full spectrum, but the [StructMemEval benchmark](https://arxiv.org/abs/2502.13649) showed that simple retrieval can outperform complex memory hierarchies on standard benchmarks like LoCoMo and LongMemEval. Move to planar or hierarchical only when you observe specific retrieval failures that flat retrieval can’t solve—like multi-hop questions where the answer requires chaining through multiple entries.

### Latent memory

Next up: The one you should probably understand but you probably won’t build.

**Latent memory** is memory stored as the model’s own internal representations—hidden states, KV cache entries, compressed vectors. It lives inside the model’s computation, not in an external database.

A Word on Terminology

Before we go further, I need to address the naming collision that trips up every engineer I’ve talked to about this. When memory researchers say “KV cache,” they do _not_ mean Redis. They do not mean a key-value database. The “Key” and “Value” in a transformer’s KV cache are linear projections of each token’s hidden state that serve specific roles in the attention mechanism. The Query vector multiplied by the Key vector produces a relevance score, which is then used to weight-blend the Value vectors. It’s an internal data structure of the transformer architecture, not a caching layer in the infrastructure sense. (I’ve seen experienced engineers spend twenty minutes confused about this in paper discussions, so if that was you, you’re in good company.)

With that cleared up, latent memory has three subtypes:

- **Reuse:** Save the KV cache from a forward pass, reload it later. The model picks up where it left off. [Memorizing Transformers](https://arxiv.org/abs/2203.08913) (Wu et al., 2022), [LONGMEM](https://arxiv.org/abs/2306.07174), and FOT all explore this approach.
- **Transform:** Prune or compress the KV cache to keep only what matters. [SnapKV](https://arxiv.org/abs/2404.14469) uses head-wise voting to decide what to keep. [H2O](https://arxiv.org/abs/2306.14048) evicts “heavy hitter” entries. [PyramidKV](https://arxiv.org/abs/2406.02069) allocates different budgets per layer. The idea is the same across all of them: the model was paying attention to certain tokens more than others, so keep those and drop the rest.
- **Generate:** Train a separate module to compress input into a handful of “memory tokens.” [Gist tokens](https://arxiv.org/abs/2304.08467) (Mu et al., 2023), [AutoCompressor](https://arxiv.org/abs/2305.14788) (Chevalier et al., 2023), and [Titans](https://arxiv.org/abs/2501.00663) (Behrouz et al., 2025—which uses an online-updated MLP to produce latent vectors) all take this approach. The model literally learns to compress its context into a compact representation.

Now here’s why I said “probably won’t build”: every single one of these techniques requires access to internal model state—`past_key_values`, `output_hidden_states`, `output_attentions`, or `inputs_embeds`. These are [HuggingFace](https://huggingface.co/) Transformers access points on [PyTorch](https://pytorch.org/) models. Hosted APIs—Anthropic, OpenAI, Google—expose none of them. You can’t reach into Claude’s KV cache from the API. You can’t inject custom embedding vectors into GPT-5.4’s forward pass.

What providers _do_ give you is prompt caching (provider-managed KV reuse—Anthropic caches your system prompt, for example) and embeddings endpoints (useful for retrieval but not injectable back into the forward pass). These are related to latent memory, but they’re black-box optimizations you can’t control or extend.

There’s also a language constraint worth noting: this is Python-only territory. PyTorch and HuggingFace Transformers is where the internal access points live. Transformers.js and ONNX Runtime for Node.js don’t expose the needed internals. If you’re building in TypeScript (and I usually am), latent memory is off the table entirely.

### Parametric memory

And finally, we can impact the model’s memory by adjust the parameter weights of the model itself.

**Parametric memory** encodes knowledge directly into model weights via fine-tuning, LoRA adapters, or knowledge editing techniques like [ROME](https://arxiv.org/abs/2202.05262) and [MEMIT](https://arxiv.org/abs/2210.07229). When you fine-tune a model on your company’s codebase, the knowledge becomes part of the model’s parameters. Every conversation benefits from it—no retrieval step needed.

The distinction from latent memory is important: parametric changes are _permanent_ and affect every conversation. Latent memory is ephemeral and scoped to the current context. If latent memory is a snapshot injected before a specific task, parametric memory is muscle memory from years of practice. The chef who can debone a fish without thinking has parametric memory. The chef who glances at a recipe card before plating has something closer to latent memory.

Same hosted-model constraint applies: you need weight access, which APIs don’t provide. Provider fine-tuning services exist (Anthropic, OpenAI, Google all offer them), but they don’t support continuous, incremental updates. You can’t fine-tune Claude a little more every time a user teaches it something new. It’s a batch process, not a memory system in the sense the survey means.

### The practical scorecard

Here’s where the 107-page paper compresses to one practical insight:

- **Token-level:** Works with any model. Inspectable, debuggable, editable. This is your lane if you’re using hosted frontier models, which—let’s be honest—most of us are.
- **Latent:** Open-source models only, or invisible provider-side optimizations you can’t control. Research-grade infrastructure required.
- **Parametric:** Open-source models only, with a weak exception for provider fine-tuning services that don’t support the incremental updates a real memory system needs.

If you’re building an agent that talks to Claude, GPT-4, or Gemini through an API, your entire memory design space is token-level. Master the topology spectrum (flat → planar → hierarchical) and get very good at the dynamics layer—formation, evolution, retrieval—operating over token-level stores. That’s where all the leverage is.

## The three functions: why do agents need memory?

The second axis asks what memory is _for_. The survey identifies three functional categories, and they map more cleanly to practical design decisions than the forms axis does.

### Factual memory (Or, “What does the agent know?“)

This is the most intuitive category—declarative facts about the world. User preferences, environment state, conversation history, project context. “The user prefers TypeScript.” “The project uses Tailwind.” “Last session, we were debugging a race condition in the checkout flow.”

Cognitive science splits declarative memory into **episodic** (event-specific: “the user told me about the bug on Tuesday”) and **semantic** (general knowledge: “the project uses PostgreSQL”). Agent systems mirror this split with user-facing facts—identity, preferences, commitments the agent has made—and environment-facing facts—document states, resource availability, tool configurations.

Factual memory enables three properties that matter in practice: **consistency** (don’t contradict yourself across conversations), **coherence** (maintain topical continuity within a conversation), and **adaptability** (personalize behavior over time based on what you learn about the user).

This is what most memory frameworks implement today. When people say “agent memory,” they usually mean factual memory. Mem0, MemGPT, [MemoryBank](https://arxiv.org/abs/2305.10250), Zep—they all store facts and retrieve them. It’s table stakes. The interesting question is what _else_ your memory system should capture.

### Experiential memory (Or, “How does the agent improve?“)

This is the missing piece in most agent frameworks—and the part that I am kind of obsessed with right now, and I think it’s the most underexplored area for practitioners. Factual memory tells the agent what it knows. Experiential memory tells it how to do things _better_—how it solved problems in the past, what worked, what didn’t.

Cognitive science calls this **procedural memory**—the kind of memory that lets you ride a bike without thinking about it. In agent systems, experiential memory operates at four levels of abstraction, and the progression is genuinely interesting:

- **Case-based:** Store raw trajectories. “User asked X, I tried approach Y, it failed with error Z, I tried approach W, it worked.” [ExpeL](https://arxiv.org/abs/2308.10144) (Zhao et al., 2024), Memento, and [JARVIS-1](https://arxiv.org/abs/2311.05997) all take this approach. You get high fidelity—the full record of what happened—but poor generalization and expensive context consumption. Replaying a 200-step trajectory to avoid a mistake on step 47 is wasteful.
- **Strategy-based:** Distill insights and workflows from raw experience. “When encountering connection timeout errors, check the connection pool configuration first—retry logic is usually a red herring.” [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) (AWM), [Reflexion](https://arxiv.org/abs/2303.11366), [Buffer of Thoughts](https://arxiv.org/abs/2406.04271), and R2D2 operate here. The strategies transfer across tasks—an insight about debugging connection issues applies to any project, not just the one where you learned it. Three granularities emerge: atomic insights (single observations), sequential workflows (step-by-step procedures), and schematic patterns (high-level templates).
- **Skill-based:** Compile strategies into executable code. The agent literally writes reusable tools for itself. [Voyager](https://arxiv.org/abs/2305.16291)’s JavaScript skill library for Minecraft is the canonical example—the agent discovers how to mine iron, writes a `mineIron()` function, and calls it directly next time instead of re-deriving the procedure. [SkillWeaver](https://arxiv.org/abs/2503.07413), Alita, and LEGOMem extend this to other domains. You could even frame MCP tool generation as skill-based memory—the agent creates tools it can invoke later.
- **Hybrid:** Combine levels. ExpeL stores both trajectories _and_ extracted insights. G-Memory gradually compiles frequent successes into executable skills. Memp distills gold trajectories into abstract procedures. The strongest systems don’t pick one level—they maintain multiple simultaneously and use the right abstraction for the right retrieval context.

Two patterns from recent work stand out. The **Agentic Context Engineering (ACE)** pattern uses a three-agent loop—Generator, Reflector, Curator—to evolve a “context playbook” of learned strategies. It showed a +10.6% improvement on agent benchmarks without any fine-tuning, purely through better context management. The **Dynamic Cheatsheet** approach prevents redundant computation by storing accumulated strategies and problem-solving insights for immediate reuse at inference time. Both are forms of experiential memory that operate entirely at the token level—no weight updates needed.

I think experiential memory is where the biggest gap between current agent implementations and what’s possible lives. Most agents I’ve built or used have factual memory (or at least attempt it). Almost none of them systematically learn from their own successes and failures. Every debugging session starts from scratch.

### Working memory (Or, “What is the agent thinking about right now?“)

Working memory isn’t about what’s stored long-term—it’s about what’s in the prompt [_right now_](https://www.youtube.com/watch?v=gU7d2EHV_OQ). Baddeley’s working memory model from cognitive science describes it as capacity-limited, dynamically controlled, and essential for higher-order cognition. The agent equivalent is the context window, but with an important distinction: a context window is a passive buffer by default. **Working memory** actively controls what’s in it.

For single-turn interactions, working memory is mostly about compression—fitting massive inputs into the context window. [LLMLingua](https://arxiv.org/abs/2310.05736) compresses prompts by dropping low-perplexity tokens. Gist tokens (mentioned in the latent memory section) compress input into a handful of learned representations. Observation abstraction converts raw HTML into structured state descriptions— [Synapse](https://arxiv.org/abs/2306.07863) does this for web agents, turning a full DOM into a compact representation of what’s actually on screen.

For multi-turn interactions—which is where persistent agents live—working memory gets much harder:

- **State consolidation:** Periodically compress conversation history into a summary. This is what Claude Code does when it hits context limits—it compacts the conversation, and you see a `compact_boundary` marker in the message stream. MemAgent, MemSearcher, and [ReSum](https://arxiv.org/abs/2501.08478) all implement variations. The risk is losing detail that turns out to matter later.
- **Hierarchical folding:** Decompose tasks into subtasks, fold completed subtask trajectories into summaries, keep only the active subtask in full detail. [HiAgent](https://arxiv.org/abs/2501.15641), Context-Folding, and AgentFold take this approach. It’s elegant because completed work gets compressed while active work stays at full resolution.
- **Cognitive planning:** Maintain an externalized plan as the core of working memory, rather than raw conversation history. [PRIME](https://arxiv.org/abs/2502.10990), [SayPlan](https://arxiv.org/abs/2308.06391), KARMA, and [Agent-S](https://arxiv.org/abs/2410.08164) structure working memory around “what am I trying to accomplish and what’s my next step?” rather than “what has been said so far.” I find this approach particularly compelling because it mirrors how I actually think when working on a complex task—I don’t replay the full conversation history in my head, I check my mental model of the plan and figure out what’s next.

## The dynamics lifecycle: how memory operates

The third axis is where the rubber meets the road. Forms tells you where memory lives. Functions tells you why you need it. Dynamics tells you how to _operate_ it—how memories get created, maintained, and retrieved over time. This is also where the most practical engineering decisions live.

### Formation: what to store

When something happens that the agent might want to remember, how do you turn it into a memory entry? Five strategies, from simplest to most aggressive:

**Semantic summarization** compresses content to its gist. You take a conversation or document and produce a shorter version that captures the key points. There are two flavors: _incremental_ (update a running summary with each new chunk—MemGPT and Mem0 do this) and _partitioned_ (divide content into segments and summarize each independently—MemoryBank, [ReadAgent](https://arxiv.org/abs/2402.09727), [LightMem](https://arxiv.org/abs/2501.06579) take this approach). Incremental risks semantic drift—the summary gradually loses fidelity as it gets updated over and over. Partitioned risks losing cross-partition dependencies—information that spans two segments might get lost because neither segment’s summary captures the full picture.

**Knowledge distillation** extracts specific facts and insights rather than summarizing everything. [Think-in-Memory](https://arxiv.org/abs/2311.08719) (TiM), [RMM](https://arxiv.org/abs/2502.01070), ExpeL, and AWM all work this way. You don’t produce a summary—you produce discrete facts: “User prefers dark mode.” “The API rate limit is 100 requests per minute.” “Debugging approach X worked for error type Y.” More precise than summarization, but risks misextraction—the LLM might extract the wrong fact or miss an important one.

**Structured construction** builds graphs and trees from content. Zep builds a temporal knowledge graph where entities have timestamps and relationships evolve over time. A-Mem creates networked notes with explicit links between related concepts. [GraphRAG](https://arxiv.org/abs/2404.16130) uses community detection algorithms to identify clusters of related entities. [RAPTOR](https://arxiv.org/abs/2401.18059) builds recursive abstractive trees—leaf nodes are raw chunks, parent nodes are summaries of their children, and you can retrieve at any level of abstraction. Rich representations, but rigid—the schema decisions you make at construction time constrain what you can retrieve later.

**Latent representation** compresses content into dense vectors. [MemoryLLM](https://arxiv.org/abs/2402.04624) and AutoCompressor do this. Efficient in terms of storage, but opaque—you can’t inspect what a latent vector “remembers.”

**Parametric internalization** fine-tunes the model on the content. ROME and MEMIT edit specific facts directly into model weights. Permanent, but carries catastrophic forgetting risk—updating one fact can corrupt nearby facts.

These aren’t mutually exclusive. The strongest systems do multiple simultaneously—store both the raw case _and_ the extracted insight, for example. ExpeL maintains both trajectories and distilled strategies. If you’re building a production system, I’d start with knowledge distillation for discrete facts and semantic summarization for conversation context, and add structured construction only when you see specific retrieval needs that flat search can’t meet.

### Evolution: how to maintain memory

Memories aren’t static. New information arrives that contradicts old memories. Related memories should be merged. Low-value memories should be pruned to keep retrieval quality high. Three operations:

**Consolidation** merges related entries. At the simplest level, you detect near-duplicates and combine them (local, pairwise). At a more sophisticated level, you cluster related memories and produce summary entries for each cluster— [PREMem](https://arxiv.org/abs/2502.09834), CAM, and TiM do cluster-level consolidation. At the global level, frameworks like [MOOM](https://arxiv.org/abs/2502.09070) and AgentFold periodically restructure the entire memory store. The goal is to keep the memory store compact and retrieval-friendly without losing important information.

**Updating** resolves conflicts when new information contradicts existing memory. This is where things get subtle. If a user says “we switched from PostgreSQL to MySQL,” you need to update the relevant memory—but do you delete the old one or mark it as superseded? Zep’s approach is smart: soft-delete with timestamps rather than hard-delete. The old fact is still there for auditability, but it won’t surface in retrieval. [LightMem](https://arxiv.org/abs/2501.06579) and MOOM use a dual-phase pattern: fast online writes that accept new information immediately, plus slow offline consolidation that resolves conflicts and merges related entries in the background. [Mem-α](https://arxiv.org/abs/2503.13790) goes further and trains an RL policy for update decisions—the system _learns_ when to update versus when to keep both versions.

It turns out that an important part of remembering is forgetting. **Forgetting** prunes low-value entries. Three signals inform what to forget: time decay (exponential, inspired by the Ebbinghaus forgetting curve—memories naturally fade), access frequency (LRU/LFU policies—rarely accessed memories get evicted), and semantic importance (LLM-judged value—ask the model “is this memory still useful?”). Fair warning: LRU-style forgetting can eliminate rare but essential long-tail knowledge. A memory that’s accessed once per year might still be critical when it’s needed. Pure frequency-based eviction is dangerous for specialized knowledge.

The field is progressing through three generations of evolution strategies: rule-based (hard-coded decay rates, fixed merge thresholds), LLM-assisted (use the model to judge what to merge, update, or forget), and RL-trained (train a policy that learns optimal memory management through experience). [Memory-R1](https://arxiv.org/abs/2504.01069) and Mem-α represent the RL-trained frontier. Most practical systems today are in the first or second generation, and honestly, LLM-assisted evolution is probably sufficient for most use cases.

One practical insight I keep coming back to: conflict detection at write time is underrated. When you’re about to store a new memory, check for existing entries in the 0.6–0.9 cosine similarity range. Below 0.6, they’re unrelated. Above 0.9, they’re near-duplicates. But that middle range—similar topic, potentially different facts—is where interesting conflicts live. “The project uses PostgreSQL” at 0.75 similarity to “The project uses MySQL” is a conflict you want to surface, not silently resolve.

### Retrieval: how to access what you stored

Retrieval is where most people start thinking about memory systems, but it’s actually the _last_ step in the lifecycle. I guess that makes sense: You can’t recall the memories you never stored. (That’s a song lyric waiting to happen.) And here’s the meta-insight the survey drives home: retrieval quality is bounded by formation and evolution quality. You can build the most sophisticated retrieval pipeline in the world, but if what’s stored is noisy, contradictory, or poorly structured, your retrievals will be noisy, contradictory, and poorly structured. Beyond a certain sophistication of retrieval pipeline, the leverage shifts to making what’s stored cleaner.

That said, retrieval still matters enormously. Here’s the four-step pipeline the survey describes, with the practical implications of each:

**Timing: don’t always retrieve.** Not every query needs memory augmentation. Some agent systems let the model decide whether to retrieve—it can choose to call a “search memory” tool or not. A more sophisticated approach is the fast-slow pattern: generate a quick draft response, check confidence, retrieve only if the draft is insufficient. [ComoRAG](https://arxiv.org/abs/2502.14530) and PRIME implement variations of this. The benefit is obvious—unnecessary retrieval adds latency and can actually _hurt_ performance by injecting irrelevant context.

**Query construction: the query you have is probably wrong.** This is the step that made the biggest impression on me. Raw user queries are poor retrieval signals. The question “how do we handle authentication?” doesn’t look anything like the stored memory “The project uses JWT tokens with a 24-hour expiry, validated by middleware in `auth.ts`.” In embedding space, the question and the answer are farther apart than you’d want because they have fundamentally different shapes—one is interrogative and vague, the other is declarative and specific.

This is where HyDE comes in, and I want to give it its own section because the approach is counterintuitive enough to deserve a proper explanation.

**Strategy: go hybrid.** Once you have a good query (or a HyDE-generated hypothetical), the retrieval strategy matters. Hybrid retrieval—BM25 plus semantic embedding, optionally plus graph traversal—outperforms any single method. BM25 catches exact keyword matches (when the user says `auth.ts`, you want exact string matching). Semantic embedding catches paraphrases (when the user says “login system” and the memory says “authentication middleware”). Graph traversal catches multi-hop relationships (when answering “what API does the project use that’s built by the company Steve used to work at?” requires chaining through multiple nodes).

**Post-processing: filter aggressively.** Rerank retrieved results with a cross-encoder or LLM-based relevance judge. Apply [MMR](https://en.wikipedia.org/wiki/Maximal_marginal_relevance) (Maximal Marginal Relevance) for diversity—you want the top-K results to cover different aspects of the query, not K slightly different versions of the same memory. And filter aggressively. Injecting ten marginally relevant memories into the context is worse than injecting three highly relevant ones. (I’ve learned this one the hard way. More context is not always better context.)

### HyDE: the counterintuitive retrieval trick

I’ve been fascinated by this approach since I first encountered it, and I think it deserves a longer explanation because the core insight runs against how most engineers think about search.

HyDE—Hypothetical Document Embeddings—comes from [Gao et al. (ACL 2023)](https://arxiv.org/abs/2212.10496), out of CMU and the University of Waterloo. Here’s the problem it solves: in a typical RAG setup, you take the user’s query, embed it, and use vector similarity to find relevant documents in your memory store. This works okay for simple lookups but falls apart for complex or abstract queries. Why? Because questions and answers don’t look alike in embedding space. A question is interrogative and vague. A stored memory is declarative and specific. Their embeddings are farther apart than you’d want.

The fix is beautifully simple: ask the LLM the question _with no context_ and let it respond. Even if the response is completely wrong, the fabricated answer is likely to be _shaped_ like the real information in your memory store—which means its embedding will be closer to the real answer than the original question’s embedding was.

The counterintuitive part is that the fabricated answer doesn’t need to be _correct_. “The project uses Python with Flask” and “The project uses TypeScript with Express” are neighbors in embedding space—they share the same declarative structure, the same semantic domain, the same answer-shape. The encoder’s dense bottleneck filters out the specific (wrong) details and preserves the structural similarity. The original paper calls this the “dense bottleneck hypothesis.”

In practice, the original paper generates 5 hypothetical documents at temperature 0.7 and averages their embeddings. For agent memory retrieval, even a single generation works well. The implementation is one LLM call before each retrieval. Use a small, fast model for the hypothetical—the answer doesn’t need to be smart, it just needs to be answer-shaped. For hybrid search, combine the hypothetical with the original query for the BM25 leg so exact keyword matches from the original query are preserved.

When HyDE doesn’t help: specific factual lookups where the query already contains exact matching terms (“what’s in `auth.ts`?”), and very short keyword-like queries (“PostgreSQL version”). In those cases, the original query is already closer to the stored memory than any hypothetical would be.

### Multi-hop queries: the hard problem

Some questions can’t be answered by any single memory entry. “What API does the project use that’s built by the company Steve used to work at?” requires chaining through multiple entries: Steve’s employment history → the company → their products → the current project’s dependencies. No single fact contains the answer.

Here’s the strategy spectrum, from cheapest to most complex:

**Iterative retrieval** is the simplest: retrieve once, read the results, extract new search terms from what you found, retrieve again. The agent does the chaining through its normal tool-calling loop. This requires zero changes to your storage layer—it’s just the agent calling its memory search tool multiple times in a single turn. If you’re building on top of a ReAct-style agent loop (and you probably are), this already works.

**Query expansion** generates multiple related queries from the original and merges results. “What API does the project use that Steve’s old company built?” might expand to “Steve’s previous employer,” “APIs used in the project,” “companies that build developer tools.” This helps with rephrasing but has an important limitation: the expansion can only rephrase what’s already in the query. It can’t discover connected entities that exist only in the memory store. If the user doesn’t mention the company name, query expansion can’t find it.

**Enrichment at write time** extracts entities and connection hints when memories are first stored, adding them as metadata. When you store “Steve used to work at Temporal,” you also tag it with entities: `{person: "Steve", company: "Temporal", relation: "former_employer"}`. This adds implicit connections without building a full graph. It’s a pragmatic middle ground.

**Knowledge graph** is the full-power solution: entity-relationship triples with graph traversal. Zep, [Mem0g](https://arxiv.org/abs/2504.09413), and [AriGraph](https://arxiv.org/abs/2407.04363) all implement this. You can follow edges from “Steve” → “worked\_at” → “Temporal” → “builds” → “Temporal SDK” → “used\_by” → “current project.” Knowledge graphs consistently win on multi-hop benchmarks. The trade-off is significant engineering commitment—building, maintaining, and querying a graph is a lot more work than maintaining a flat vector store.

**Hierarchical summaries** can sometimes resolve multi-hop queries as a side effect. If your consolidation process produces cluster summaries that happen to connect the relevant entities (“Steve, who previously worked at Temporal, contributed to the project’s adoption of their SDK”), the multi-hop connection is already captured in a single retrievable entry. It’s not reliable, but good consolidation practices help.

Honest assessment: for genuine multi-hop queries where the connecting entities aren’t in the query, you really only have two reliable options. Let the agent loop (iterative retrieval) or build structural connections (knowledge graph). Everything in between helps with rephrasing but doesn’t solve the fundamental problem of discovering entities you didn’t know to ask about.

## Trustworthy memory: the part everyone skips

I almost skipped this section. It feels like the “security chapter” of a textbook that you flip past to get to the interesting stuff. But having now spent time building a memory system, I think the trust and safety properties of agent memory are genuinely load-bearing, and most implementations get them wrong—or don’t think about them at all.

The survey’s framing is blunt: “as LLM agents begin to operate in persistent, open-ended environments, trustworthy memory will not just be a desirable feature—but a foundational requirement for real-world deployment.”

### The multi-tenancy problem

Agent memory stores user-specific, persistent, potentially sensitive content. In a multi-tenant system—which is what you’re building if more than one person uses your agent—one user’s memories must not be accessible to another. This sounds obvious. It’s not obvious in practice.

Research shows that memory modules can leak private data through indirect prompt-based attacks. The attacker doesn’t need access to the storage layer. They craft prompts that cause the agent to surface another user’s memorized data through the model’s responses. If your memory retrieval path doesn’t enforce strict tenant isolation at the retrieval level—not just at the storage level—you have a data leak waiting to happen.

Namespace filtering in application code is not real isolation. If the underlying storage has all tenants’ data in one collection and the boundary is enforced by a metadata filter on queries, a bug in the filter leaks everything. I’ve seen this pattern in production systems, and it makes me nervous every time.

Three levels of defense, from weakest to strongest:

- **Application-level:** Namespace wrappers that enforce tenant boundaries regardless of what the caller passes. The wrapper overwrites any namespace the caller provides with the configured tenant namespace. This prevents accidental cross-tenant queries but doesn’t protect against storage-level bugs.
- **Storage-level:** Separate databases (or collections, or indexes) per tenant. Simplest strong isolation. Per-tenant backup/restore and deletion (“forget everything about this user”) come for free. This is what I’d recommend for most systems.
- **Encryption-level:** Per-tenant encryption keys. Even if someone gets raw storage access, they can’t read another tenant’s data without the key. The gold standard for sensitive deployments, but adds key management complexity.

### Shared caches are a leak surface

This one is subtle and I’ve never seen it discussed outside of the survey. If you cache embeddings keyed by content hash—which is a reasonable optimization—and you don’t include the tenant namespace in the cache key, cache hits can cross tenants. User A stores a memory, the embedding gets cached. User B stores a similar memory, the cache returns User A’s embedding. The embedding itself doesn’t contain User A’s data directly, but timing attacks and cache probing can leak information.

Similarly, if you batch embedding calls and mix content from different tenants in the same batch, the embedding provider can theoretically correlate them.

The fix is straightforward: incorporate the tenant namespace into cache keys. Provide per-namespace cache eviction. Batch embeddings per-tenant, not across tenants.

### The right to be forgotten

If a user asks to delete their data, can you guarantee it’s gone? Under GDPR Article 17 (Right to Erasure) and CCPA deletion rights, you may be legally required to guarantee it. (This brings back painfull memories of when I used to work at a messaging company and your entire contact list was just a bundle of PII.)

The cascade problem makes this harder than it sounds. Deleting the storage entries is step one. But what about the full-text search indexes that contain their data? The embedding caches? The consolidated summaries that reference their memories? The experiential memories derived from interactions with them? A memory that says “when User X asks about feature Y, approach it this way” contains information _about_ User X even though it looks like an agent strategy.

Zep’s approach—soft-delete with timestamps rather than hard-delete—preserves auditability while making data inaccessible. The data still exists in storage but is excluded from all retrieval paths. This gives you a window for complete physical deletion while immediately removing the data from the agent’s accessible memory.

### The three pillars of trust

(Also: A great band name.)

The survey frames trustworthy memory around three pillars, and I think the framing is worth internalizing even if you don’t implement all of it:

**Privacy:** Granular permissioned memory (some memories are shareable, others aren’t), user-governed retention policies (let users control how long their data is kept), encrypted and isolated storage, memory redaction (strip PII before storing). The practical minimum is tenant isolation and user-controlled deletion. Everything beyond that is defense in depth.

**Explainability:** Traceable access paths (which memories contributed to this response?), self-rationalizing retrievals (why were these memories chosen?), counterfactual reasoning (“what would have changed without this memory?”). Most of this is research-grade, but retrieval logging—recording which memories were retrieved for each response—is practical today and invaluable for debugging.

**Hallucination robustness:** Conflict detection (do retrieved memories contradict each other?), uncertainty-aware generation (abstain when retrieval confidence is low), multi-document reasoning (synthesize across multiple memories rather than trusting any single one). The practical version of this is simple: if your retrieval returns conflicting memories, surface the conflict to the user rather than silently picking one.

## Research frontiers: where this is all heading

The core of this post has been about what you can build today. This section is about where the research is pointing, and a few of the directions are genuinely exciting even if they’re not production-ready yet.

### RL-driven memory management

It feels like all roads tend to lead towards reinforcement learning these days: we’ve gone from rule-based memory management (hard-coded decay rates, fixed merge thresholds) to LLM-assisted (use the model to judge what to keep and what to forget) and we’re now entering RL-driven territory. [Memory-R1](https://arxiv.org/abs/2504.01069) and [Mem-α](https://arxiv.org/abs/2503.13790) train RL policies that learn optimal memory operations through experience—when to store, when to consolidate, when to forget.

The deeper argument is provocative: human-inspired memory taxonomies (episodic, semantic, procedural—borrowed from Tulving’s cognitive science work) may not be optimal for artificial agents. We inherited these categories because they describe how human brains work, but there’s no reason to believe they’re the best organization for a system with fundamentally different constraints—unlimited patience, perfect recall of what it _does_ store, no emotional salience signal. Let the agent invent its own memory structures through optimization. [MemEvolve](https://arxiv.org/abs/2502.08413) is a meta-evolutionary framework that jointly evolves both the agents’ knowledge and their memory architecture.

I find this compelling and a little unsettling. The memory taxonomies feel natural because they map to how we think about our own memory. But “feels natural” isn’t the same as “is optimal.”

### Memory generation versus memory retrieval

Instead of retrieving stored entries, what if the agent could _generate_ context-specific memory on the fly? Rather than looking up “what do I know about this user’s project,” the agent synthesizes a relevant context summary from compressed representations. The survey argues latent memory—those compressed vector representations I described earlier—is the most promising technical path for this.

This would be a genuine paradigm shift. Today’s retrieval pipeline—query → embed → search → rank → inject—would be replaced by something closer to: compressed state → generate relevant context → inject. The retrieved context would be tailored to the current query rather than being a pre-existing entry that happens to match. It’s early days, but the direction is worth watching.

### Multi-agent shared memory

As agent architectures move from single-agent to multi-agent, memory sharing becomes a first-class problem. The progression mirrors distributed systems generally: isolated local memories with message passing → centralized shared stores ( [MetaGPT](https://github.com/geekan/MetaGPT)’s shared message pool) → the future of agent-aware shared memory with role-based access control and learned synchronization policies.

The challenges are familiar to anyone who’s built distributed systems: consistency (do all agents see the same memory state?), isolation (can one agent’s bad memory corrupt another’s?), and coordination (when two agents want to update the same memory simultaneously, who wins?). These are solved problems in database engineering but new problems in the context of LLM agents, because the “data” is unstructured text with semantic meaning that doesn’t have natural primary keys or merge functions.

### The ontological question

This is what happens when you let liberal arts majors play with technology. I’ll end the frontiers section with something that most engineering papers don’t ask. The [“Animesis”](https://arxiv.org/abs/2603.04740) paper from March 2026 asks: as agents become persistent and autonomous, what does memory _mean_ for a digital being?

Current work answers “what memory does”—stores facts, enables retrieval, supports learning. But it doesn’t answer “what memory is” in a deeper sense. As agent lifecycles extend from minutes to months—and they are extending, with persistent sessions, scheduled tasks, and always-on infrastructure—the assumption that memory is just a tool for the agent to use starts to break down. Is an agent with a rich memory of a user’s preferences, communication style, and project history fundamentally different from an agent without one? Not in capability, but in kind?

I don’t have an answer. I’m not sure the question has a clean answer. But I think it’s worth sitting with, because the systems we’re building now—the memory stores, the retrieval pipelines, the evolution strategies—are the substrate on which that question will eventually matter.

## What this means in practice

Here’s where I land after reading through the research and building against some of these ideas.

For practitioners (e.g. you and me) building memory systems today, the actionable path is clear: master token-level memory with a strong retrieval pipeline. That means hybrid search (BM25 plus semantic embeddings), HyDE for query construction, MMR for diversity, temporal decay for freshness, and aggressive post-retrieval filtering. Start flat. Move to graphs or hierarchies only when you observe specific failures that flat retrieval can’t solve.

Add experiential memory to close the learning loop. Your agent should remember _how_ it solved problems, not just what facts it knows. Even a simple strategy store—“approaches that worked for error type X”—can meaningfully reduce the number of times your agent re-derives the same solution.

Take multi-tenancy seriously from the start. Retrofitting tenant isolation into a memory system that was designed as single-tenant is painful. Per-tenant storage is cheap. Cross-tenant data leaks are not.

The gap between research and production is real, but the most impactful improvements are often the simplest. Better query construction (HyDE) matters more than a fancier vector index. Conflict detection at write time matters more than a more sophisticated retrieval ranker. Background consolidation that merges near-duplicate memories matters more than a hierarchical memory architecture.

Memory isn’t an auxiliary feature you bolt onto an agent after the core loop works. It’s the substrate that turns a stateless language model into something that improves over time. Every agent you’ve used that felt genuinely helpful—that remembered your preferences, learned from its mistakes, maintained context across sessions—had a memory system doing the heavy lifting. Every agent that felt frustrating—that asked the same questions twice, forgot what you told it yesterday, repeated the same mistakes—didn’t. The difference is the memory.

Last modified on April 8, 2026.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="understanding-the-impact-of-increasing-llm-context-windows-m.md">
<details>
<summary>Understanding the Impact of Increasing LLM Context Windows</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows>

AI Research

# Understanding the Impact of Increasing LLM Context Windows

https://cdn.prod.website-files.com/66efe12cea125ae2bb1471da/6792437c068ae447f07c47b8_Spencer%20White%20BG.webp

Spencer Torene, Ph.D.

Principal Scientist

Last Updated

April 24, 2025

Reading Time

4

min

https://cdn.prod.website-files.com/66efe12cea125ae2bb1471da/680a25ea294e37026d9c8443_5a41b40b-c20a-4b26-8176-601489acbf64_2.webp

With Meta's recent release of Llama 4 featuring an impressive 10 million token context window, we've reached yet another milestone in the ever-evolving landscape of Large Language Models (LLMs). But what does this massive expansion in context capacity actually mean for users, developers, and businesses leveraging this technology?

## The Context Window Revolution

Context windows have grown exponentially since the inception of LLMs. Figure 1 shows the increasing context window size of LLMs. In 2018 and 2019, maximum context windows were 512 and 1,024 tokens, respectively. By 2024 we saw models with 1 million token context windows.

https://cdn.prod.website-files.com/66efe12cea125ae2bb1471da/680a244002ab2f063f3a9108_llm_context_window_evolution.webp

Figure 1: Increasing lengths of context windows over time.

This evolution allows models to keep track of and consider more text at once, and we've seen this working memory of LLMs grow from a few paragraphs to entire books or even libraries worth of content.  With Llama 4's recent release featuring a massive 10 million token context window, we're seeing an unprecedented expansion in what language models can keep track of during a single session. But what does this dramatic increase in context window size actually mean for users? The continued development and release of smaller context window models seen from 2023 onward in Figure 1 suggests there's a benefit to the diversity of window size, and we'll discuss the tradeoffs that come with ever-expanding context windows.

## What Larger Context Windows Enable

The expansion of context windows brings several meaningful advantages:

**Longer Documents:** Models can now process and understand entire books, research papers, or technical manuals in a single pass. This enables more [comprehensive analysis](https://arxiv.org/pdf/2501.01880) and [deeper understanding](https://arxiv.org/pdf/2407.16833) of complex texts.

**Extended Conversation History:** Applications can maintain much longer conversation threads, allowing models to reference information from hours or even days earlier in the same session without forgetting.

**Cache Augmented Generation (CAG):** CAG pre-computes documents and caches the results as part of a prompt so that those documents’ context is available to the LLM when it generates completions. CAG can improve generation latency compared to RAG because there is no extra retrieval step to find relevant documents. Instead, all the documents are available in all prompts — as long as both the cached documents and user prompt fit within the context window. Larger context windows enable more effective use of CAG, where models can reference a substantial cache of information within their context to enhance responses. Moreover, assuming all necessary documents are cached, CAG introduces improved reasoning over those documents. RAG utilizes only the most relevant documents, as determined by document embeddings, which could miss tangentially related, idea-connecting documents.

## The Challenges of Long Context Windows

The benefits of increased context come with caveats and disclaimers, however. Bringing much more information to each inference also means that unnecessarily using the entire context window brings several meaningful disadvantages:

**Worse Reference Identification:** Attention is not uniform across the entire context window — prompts that utilize earlier tokens have better performance than prompts that utilize later tokens. Text extraction and reference identification becomes [worse with increasing prompt lengths](https://arxiv.org/pdf/2406.13121).

**Variable Signal-to-Noise Ratio:** There is a trade-off between having all possible useful context in a prompt and focusing on context that matters most. All else equal, [longer prompts have less accuracy than shorter prompts](https://arxiv.org/pdf/2406.13121).

**Increased Costs:** Input tokens are typically billed for remote calls, meaning an increase in the amount of context provided directly increases query costs. Prompt caching can reduce input token cost rates, but consistently using unnecessarily long prompts could outweigh any per token cost savings. Revisiting the trends observed in Figure 1, models with smaller context windows continue to be trained and optimized in part because they have fewer parameters, demand less memory and computational resources, and are therefore cheaper to train and host.

**Output Token Latency:** An underappreciated fact of long prompts is increased output generation latency. Our ( [and others’](https://www.glean.com/blog/glean-input-token-llm-latency)) research demonstrates that using more input tokens generally leads to slower output token generation. This performance hit creates a practical ceiling on how much you should stuff into your context window without reasonable justification. Figure 2 shows the increase in time it takes per output token, given the number of input tokens.

https://cdn.prod.website-files.com/66efe12cea125ae2bb1471da/680a2463c58853b19381f6b9_token_speed.webp

Figure 2: Output token generation speed decreases with more input tokens.

## Best Practices for Large Context Windows

Having the option of long context windows is critical, but it may not make sense to use the entire window by default. Though there can be increased accuracy and reasoning when providing more prompt text, generation can be slower and more expensive, and text extraction will be less accurate.

To make the most of expanded context capabilities while avoiding pitfalls:

- **Be selective.** Include only what’s necessary for your specific task.
- **Structure intelligently.** Place the most important information earlier in the context window.
- **Monitor performance.** Track generation speed, quality, and cost to find your optimal context size.
- **Take hybrid approaches.** Consider combining CAG for frequently used information with RAG for broader knowledge. RAG's ability to pull from virtually unlimited external knowledge bases still offers advantages that CAG cannot match. Even a 10M token context window is relatively limited, compared to the terabytes of information that RAG can potentially access.

The best approach is often to be selective about what goes into your context window rather than maximizing its use simply because the capacity exists.

## Conclusion

The expansion of context windows to millions of tokens represents a significant advancement in LLM capabilities, but it's not a silver bullet. Like any technological advancement, it comes with trade-offs.

The most successful implementations will be those that thoughtfully consider when to leverage large contexts, when to rely on retrieval, and how to balance performance, cost, and quality considerations.

As we continue to explore the frontiers of what's possible with these expanded capabilities, maintaining a critical perspective on practical applications will be essential to maximizing the value of increasingly powerful models.

‍

## Contributing Authors

Berk Ekmekci - Research Scientist

Alex Powell - Engineer

https://cdn.prod.website-files.com/66efe12cea125ae2bb1471da/6792437c068ae447f07c47b8_Spencer%20White%20BG.webp

Spencer Torene, Ph.D.

Principal Scientist

[**Linkedin**](https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows#)

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Notebook 1</summary>

# Notebook 1

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
<summary>What is the perfect memory architecture?</summary>

# What is the perfect memory architecture?

[00:00] (Video shows various quick cuts of an event with many people, some standing, some sitting, some speaking on stage. There are banners in the background for "LangGraph" and "LangSmith").
[00:02] (Bright pink and white light flashes across the screen).
[00:05] (More shots of people mingling at the event).
[00:08] (A banner reads: "LangSmith: Get your LLM app from prototype to production").
[00:09] (Screen transitions to a title slide with a speaker's photo).
[00:10] Thank you Nicole, and thank you, um, Harrison and LangChain and Greg for organizing and hosting.

[00:13] (A woman, Speaker 1, with a name tag "SAM" is on stage, holding a microphone and a remote clicker, speaking to an audience. A large white screen is behind her).
[00:15] Actually, one of the first things I did with memory was with Harrison on the original memory implantation in LangChain. So, very full circle. Um, cool. So for those of you who do not know New Computer and what we do, we have dot, which is a conversational journal. It's in the app store. You can use it now. We launched this last year. So we've been working on memory in AI applications since 2023.
[00:30] (Screen transitions to a black slide with white text: "From Dot to Dots Evolution of Memory at New Computer Sam Whitmore, CEO". A small video of Speaker 1 continues in the bottom right corner).
[00:41] Um, cool. So take us back to 2023. At the time GPT-4 was state of the art. We have 8,000 one length token, uh, prompt, very slow and very expensive. So, I want to walk you through some of the things that we tried initially, lessons we learned along the way, and how we kind of evolve as underlying technology evolves.
[00:54] (Screen shows: "GPT-4 was state of the art 8192 token context length 196ms per generated token $30.00 / 1 million prompt tokens $60.00 / 1 million sampled tokens").
[01:06] So, when we started, our general goal was to build a personal AI that got to know you. It was pretty unstructured. Um, and so we knew that if it was going to learn about you as you used it, it needed memory. So we're like, okay, let's just build the first, build the perfect memory architecture and then the product after that.
[01:20] (Screen shows a phone screen displaying a chat conversation, then transitions to a black slide with white text: "What is the perfect memory architecture?").
[01:29] Um, so we started out being like, okay, maybe we can just extract facts as a user talks to Dot and search across them, you know, use some different techniques, and we'll have great memory performance. So, we learned pretty quickly that this wasn't really going to work for us. So, imagine a user saying, "I have a dog. His name is Poppy. Walking him is the best part of my day."
[01:40] (Screen transitions to a black slide with white text: "Memory == Facts...?").
[01:50] (Screen transitions to a black slide with white text: "'I have a dog! His name is Poppy. Walking him is the best part of my day'").
[01:55] So, early extraction, we'd get things like, "User has dog. User's dog is named Poppy. User likes taking Poppy for walks." There's a lot of nuance missing. So, like, you can tell a lot about a person from reading that sentence that you can't tell from those facts. That was pretty quick realization for us.
[02:10] (Screen transitions to a black slide with white text: "User has a dog. User's dog is named Poppy. User likes taking his dog for walks.").
[02:11] (Screen transitions to a black slide with white text: "Memory != Facts").
[02:16] We then moved on. So, we're like, maybe if we try to summarize everything about Poppy in one place, then it's going to perform better. We decided that we're going to make this universal memory architecture with entities and schemas that were linked to each other.
[02:29] (Screen transitions to a black slide with white text: "Memory == Schemas?").
[02:30] (Screen shows a blank phone screen, then transitions to a screen showing "Recipes" in an app, displaying several recipe cards with images and titles. Then it shows a chat interface with a user message "my friend's bachelorette is coming up!" and the AI's response including "Created event for Meredith's Bachelorette", "Added Meredith as a friend of Zack's", and "Added the Airbnb location for Meredith's bachelorette party").
[02:40] This was a UI representation of it. Um, so users could actually browse the things that were created, um, and they had different types, and on the back end, there was different form factors with JSON blobs. This is real example from our product at the time. So, I sent it a bachelorette flyer and it made like a whole bunch of different memory types with schemas associated.
[02:53] (The screen updates to show details of the extracted memories in JSON-like format for "Created event for Meredith's Bachelorette", "Added Meredith as a friend of Zack's", and "Added the Airbnb location for Meredith's bachelorette party", with various fields like Name, End time, Location, Description, Relationship, Address).
[03:09] Um, so you can see here that like this is what the back-end data looked like. There's different fields and we had a router architecture that would kind of generate queries that would search across all of these, um, in parallel. And what we found was that it worked okay, but there was kind of some base functionality that was still missing.
[03:22] (Screen shows a Twitter-like post from "Jason 'Mars' Yuan" saying "not dot calling me out w its dynamic memory schemas". Below it is a list: "Routines 8", "Ice Cream Flavors 1", "Drunk Texts 2", "Webpages 29". The "Drunk Texts" item is highlighted).
[03:28] Um, oh, this was a funny example. Um, Jason, my co-founder, was sending it, uh, pictures and it made him a Drunk Text category as a schema. Um, which we were like, that feels like a heavy read. Um, but anyway. So the schemas were kind of fun.
[03:32] (Screen transitions to a black slide with white text: "Funny & cool to see, but didn't work that well in practice as a single system").
[03:33] But yes. So basically, we also saw that when we exposed this to users, it was like too much cognitive overhead for them to garden their, their database. Like there was a lot of overlapping concepts and people got stressed by actually just monitoring their memory base.
[03:49] (Screen shows two phone screenshots. The left one is an app interface with memory cards like "Bouldering with Luca", "Clara", "Ask Clara about bouldering", "Poetry slam event". The right one shows a chat conversation with an AI, displaying extracted memories related to a restaurant and a person named Brandon. The top of the slide has text: "(Also, users got stressed trying to garden their memories)").
[03:50] (Screen transitions to a black slide with green text: "Learning: The perfect memory architecture doesn't exist").
[03:52] So, again, we were like, okay, let's just go back to basics here and figure out like, what do we want our product to be doing? And let's re-examine how we want to build memory from that. So, we looked again at like what a thought partner should have to do to actually be really good as a listener for you.
[03:57] (Screen transitions to a black slide with white text: "The architecture of memory depends entirely on the goals of the product").
[04:00] (Screen shows a phone screen with a chat conversation, then transitions to a black slide with white text: "What would a thought partner need to learn about you to do a good job?").
[04:06] So, we realized like, it should always know who you are and your core values. It should know basically like, you know, what you talked about yesterday, what you talked about last week. And again, like who Poppy is, if Poppy is your dog, who your co-founder is, stuff like that. And it also needs to know about like your behavior preferences and how it should adapt to you as you use it.
[04:28] (Screen transitions to a black slide with a numbered list: "1. It needs to know my general bio & core values 2. It needs to know the things that happen in my life and also when they happened 3. It needs to know about the people, places, and the various nouns important to me 4. It needs to know the best way to work with me").
[04:30] So, we ended up making four kind of parallel memory systems. So the schemas that you saw didn't really go away, they just became one of the memory systems, the entities. And it's funny seeing Will kind of say some of the same ones. So it's like an example of convergent evolution because we kind of made these up ourselves.
[04:39] (Screen transitions to a black slide with white text: "Holistic theory of mind to have a sense of who I am holistically Episodic memory to know the things that happen in my life and when they happened Entities to know about the people, places, and the various nouns important to me Procedural memory to know the best way to work with me").
[04:47] But basically like Holistic theory of mind, um, here's mine. It's kind of just like, who am I? What's important to me? What am I working on? What's top of mind for me right now?
[04:57] (Screen shows a black slide with white text: "Holistic Theory of Mind" followed by a bulleted list of Speaker 1's family, career, interests/passions, and current focus).
[04:58] Episodic memory is kind of like what happened on a specific day. Here's kind of like a actual real example soon after I had my baby last year.
[05:07] (Screen shows a black slide with white text: "Episodic Memory" followed by a dated entry describing Samantha's experience with her newborn son, Alexander).
[05:08] Here's like another entity example. We ended up stripping away a lot of the JSON because it turned out to actually not improve performance in retrieval across the entity schema. So, we kept things like the categories if we wanted to do tag filtering, but, um, a lot of the extra structure just ended up being like way too much overhead for the model to output.
[05:27] (Screen shows a black slide with white text: "Entities" followed by a paragraph describing Alexander, the newborn son, and Samantha's motherhood experience).
[05:28] And finally, we made this thing called procedural memory. Um, which is basically like triggered by, uh, conversational and situational similarity. So what you're looking at here is this intent, and if you're a Dot user, you'll probably recognize this behavior. It says, "Choose this if you have sensed a hidden or implied emotion or motivation that the user is not expressing in their language, and see a chance to share an insight or probe the user deeper on this matter."
[05:51] (Screen shows a black slide with white text: "Procedural Memory" followed by Python-like code defining a "ReflectionQuestionIntent" class, with a description and instructions).
[06:04] And then what if it detects that this is happening, it says like, "share an insight, you know, ask a question, issue a statement that encourages the behavior." And so basically like the trigger here is not semantic similarity but situational similarity. I see a lot of overlap here for people building agents where if you have a workflow that the agent needs to perform, it can identify that it, that it encountered that situation before and kind of pull up some learning it had from the past running of the workflow.
[06:25] (Screen shows a complex flow chart titled "Retrieval pipeline 2024").
[06:26] So this is kind of our way our retrieval pipeline worked in 2024, which is like parallelized retrieval across all of these systems. So, if here's a query which is very hard to read, so maybe these slides will be accessible separately. Um, what restaurant should I take my brother to for his birthday? And in this sense, in each of our four systems, we detect if a query is necessary across the system. For holistic stuff, we always load the, load the whole theory of mind. Episodic is only triggered if it's like what did we talk about last week or what did we talk about yesterday.
[07:00] (Speaker 1 uses a remote to highlight different sections of the flow chart as she speaks).
[07:07] And then here there's two, like different types of entity queries detected, like brother and restaurants. And then we would do kind of a hybrid search thing where like, we mix together BM25, semantic keyword, basically like no attachment to any particular approach, just like whatever improved recall for specific entities. Um, and then the procedural memory, here if there's a behavioral module loading like restaurant selection or planning, then that would get loaded into the final prompt.
[07:30] So funny thing also is when we launched people tried to prompt inject us, but because we have so many different behavioral modules and different things going on, we called it like Franken-prompt. And like, if people did prompt inject us, they'd be like, wait, I think this prompt changes every time, which it did.
[07:47] (Screen transitions to a black slide with white text: "The formation of these memories are distinct per system").
[07:48] Um, okay. So for the formation for these, again, really distinct per system. So, holistic theory of mind, you don't need to update that frequently. Episodic is like periodic summarization. So like, if you want to have it be per week, you might update across daily summaries once per week, per day, once per day, etc. Entities, we did per line of conversation. And then we would run kind of cron jobs that we called dream sequences where they'd identify possible duplicates and potentially merge them. And procedural memory also updated per line of conversation.
[08:24] (Screen transitions to a black slide with two white, interlocking, yin-yang like shapes).
[08:26] So, um, along the past year, our product trajectory has changed. We're now building Dots, which is a Hivemind. So it's like, instead of remembering just one person that it meets, it actually remembers, um, an entire group of people.
[08:43] (Screen transitions to a black slide with white text: "Hivemind").
[08:47] And yeah, so you basically some of the added challenges we're dealing with now are representing, um, different people's opinion of each other, how they're connected, and how information should flow between them. In addition to understanding all of the systems I just mentioned above.
[09:05] (Screen transitions to a black slide with white text: "June, 2025").
[09:09] So, one other thing I'll share that has evolved in terms of how, like the world has changed a lot since 2023. So, we keep re-evaluating how we should be building things constantly. And now we have a million token input context window. We have prompts that are really cheap, and they're also really, really fast.
[09:21] (Screen shows: "Gemini flash 2.5 - Maximum input tokens: 1,048,576 Maximum output tokens: 65,535 $0.30 / 1 million input $2.50 / 1 million output").
[09:37] So, some of the things that we held true in terms of compressing knowledge and context, we no longer hold true. Here's an example. So, if you look back at this pipeline I shared before, um, here's an updated version that we're experimenting with now, which is getting rid of episodic and entity level compression in favor of real-time Q&A.
[09:42] (Screen shows the "Retrieval pipeline 2024" flow chart again, then transitions to a similar but updated "Retrieval pipeline 2025" flow chart, with some sections removed and new connections/modules).
[09:55] So, that means that like, depending on your system, maybe you don't need to be compressing context at all. Because again, like I said at the beginning, the raw data is always the best source of truth. So it's like, why would you create a secondary artifact as a stepping point between you and what the user's asking? Ideally, you just want to examine the context. And so we do that pretty frequently depending on how much data we're dealing with. We try basically not to do, to do the minimal amount of engineering possible.
[11:03] (Screen transitions to a black slide with white text: "Design for where the technology is heading").
[11:04] And our theory kind of going forward is like, this trend will only continue. So we think the procedural memory and, like basically the insights, the interpretation and analysis that the thing does, is the important part of memory. It's like the record of its thoughts about you and kind of its notes to itself is the important part. You can almost separate that from retrieval as a problem. You can say like, okay, maybe there'll be an infinite log of like my interactions and model notes will be interpolated in in the in the future. And so maybe we don't even have to deal with retrieval and context compression at all. So, I guess if I want you guys to take away one thing, it's like the perfect memory architecture doesn't exist. And start with kind of what your product is supposed to do and then think from first principles about how to make it work, and do that all the time because the world is changing and you might not need to invest that much in memory infrastructure. That's it. So, you can follow us at Twitter, New Computer.
[11:23] (Screen transitions to a black slide with white text: "The perfect memory architecture doesn't exist Know what function memory serves in your product, & think from first principles about how to make it work...constantly!").
[11:24] (Screen transitions to a black slide with white text: "Sam Whitmore, CEO @sjwhitmore New Computer @newcomputer").
[11:27] Thank you.
[11:28] (Audience applauds enthusiastically. Screen transitions back to the title slide for a moment, then to black, and the video ends.)

*Speaker 1 concludes by emphasizing that there is no perfect memory architecture; rather, it should be constantly re-evaluated based on product goals and evolving technology, with a focus on core functionality and minimal engineering.*

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory</summary>

# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**Source URL:** <https://arxiv.org/html/2504.19413>

## Abstract

Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements.

Through comprehensive evaluations on the LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and $k$-values, (iii) a full-context approach that processes the entire conversation history, (iv) an open-source memory solution, (v) a proprietary model system, and (vi) a dedicated memory management platform.

Empirical results demonstrate that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory ($\texttt{Mem0}^{\tiny g}$) achieves around 2% higher overall score than the base Mem0 configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to the full-context approach. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, thereby offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight the critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents. Code can be found at: [https://mem0.ai/research](https://mem0.ai/research)

## 1 Introduction

Human memory is a *foundation of intelligence*—it shapes our identity, guides decision-making, and enables us to learn, adapt, and form meaningful relationships. Among its many roles, memory is essential for communication: we recall past interactions, infer preferences, and construct evolving mental models of those we engage with. This ability to retain and retrieve information over extended periods enables coherent, contextually rich exchanges that span days, weeks, or even months. AI agents, powered by large language models (LLMs), have made remarkable progress in generating fluent, contextually appropriate responses. However, these systems are fundamentally limited by their reliance on fixed context windows, which severely restrict their ability to maintain coherence over extended interactions.

This limitation stems from LLMs’ lack of persistent memory mechanisms that can extend beyond their finite context windows. While humans naturally accumulate and organize experiences over time, forming a continuous narrative of interactions, AI systems cannot inherently persist information across separate sessions or after context overflow. The absence of persistent memory creates a fundamental disconnect in human-AI interaction. Without memory, AI agents forget user preferences, repeat questions, and contradict previously established facts. Consider a simple example illustrated in Figure 1, where a user mentions being vegetarian and avoiding dairy products in an initial conversation. In a subsequent session, when the user asks about dinner recommendations, a system without persistent memory might suggest chicken, completely contradicting the established dietary preferences. In contrast, a system with persistent memory would maintain this critical user information across sessions and suggest appropriate vegetarian, dairy-free options. This common scenario highlights how memory failures can fundamentally undermine user experience and trust.

Beyond conversational settings, memory mechanisms have been shown to dramatically enhance agent performance in interactive environments. Agents equipped with memory of past experiences can better anticipate user needs, learn from previous mistakes, and generalize knowledge across tasks. Research demonstrates that memory-augmented agents improve decision-making by leveraging causal relationships between actions and outcomes, leading to more effective adaptation in dynamic scenarios. Hierarchical memory architectures and agentic memory systems capable of autonomous evolution have further shown that memory enables more coherent, long-term reasoning across multiple dialogue sessions.

![Illustration of memory importance in AI agents. Left: Without persistent memory, the system forgets critical user information (vegetarian, dairy-free preferences) between sessions, resulting in inappropriate recommendations. Right: With effective memory, the system maintains these dietary preferences across interactions, enabling contextually appropriate suggestions that align with previously established constraints.](extracted/6393986/figures/main_figure.png "Figure 1: Illustration of memory importance in AI agents. Left: Without persistent memory, the system forgets critical user information (vegetarian, dairy-free preferences) between sessions, resulting in inappropriate recommendations. Right: With effective memory, the system maintains these dietary preferences across interactions, enabling contextually appropriate suggestions that align with previously established constraints.")

Unlike humans, who dynamically integrate new information and revise outdated beliefs, LLMs effectively “reset" once information falls outside their context window. Even as models like OpenAI’s GPT-4 (128K tokens), o1 (200K context), Anthropic’s Claude 3.7 Sonnet (200K tokens), and Google’s Gemini (at least 10M tokens) push the boundaries of context length, these improvements merely delay rather than solve the fundamental limitation. In practical applications, even these extended context windows prove insufficient for two critical reasons. First, as meaningful human-AI relationships develop over weeks or months, conversation history inevitably exceeds even the most generous context limits. Second, and perhaps more importantly, real-world conversations rarely maintain thematic continuity. A user might mention dietary preferences (being vegetarian), then engage in hours of unrelated discussion about programming tasks, before returning to food-related queries about dinner options. In such scenarios, a full-context approach would need to reason through mountains of irrelevant information, with the critical dietary preferences potentially buried among thousands of tokens of coding discussions. Moreover, simply presenting longer contexts does not ensure effective retrieval or utilization of past information, as attention mechanisms degrade over distant tokens.

This limitation is particularly problematic in high-stakes domains such as healthcare, education, and enterprise support, where maintaining continuity and trust is crucial. To address these challenges, AI agents must adopt memory systems that go beyond static context extension. A robust AI memory should selectively store important information, consolidate related concepts, and retrieve relevant details when needed—*mirroring human cognitive processes*. By integrating such mechanisms, we can develop AI agents that maintain consistent personas, track evolving user preferences, and build upon prior exchanges. This shift will transform AI from transient, forgetful responders into reliable, long-term collaborators, fundamentally redefining the future of conversational intelligence.

In this paper, we address a fundamental limitation in AI systems: their inability to maintain coherent reasoning across extended conversations across different sessions, which severely restricts meaningful long-term interactions with users. We introduce Mem0 (pronounced as *mem-zero*), a novel memory architecture that dynamically captures, organizes, and retrieves salient information from ongoing conversations. Building on this foundation, we develop $\texttt{Mem0}^{\tiny g}$, which enhances the base architecture with graph-based memory representations to better model complex relationships between conversational elements. Our experimental results on the LOCOMO benchmark demonstrate that our approaches consistently outperform existing memory systems—including memory-augmented architectures, retrieval-augmented generation (RAG) methods, and both open-source and proprietary solutions—across diverse question types, while simultaneously requiring significantly lower computational resources. Latency measurements further reveal that Mem0 operates with 91% lower response times than full-context approaches, striking an optimal balance between sophisticated reasoning capabilities and practical deployment constraints. These contributions represent a meaningful step toward AI systems that can maintain coherent, context-aware conversations over extended durations—mirroring human communication patterns and opening new possibilities for applications in personal tutoring, healthcare, and personalized assistance.

## 2 Proposed Methods

We introduce two memory architectures for AI agents. (1) Mem0 implements a novel paradigm that extracts, evaluates, and manages salient information from conversations through dedicated modules for memory extraction and updation. The system processes a pair of messages between either two user participants or a user and an assistant. (2) $\texttt{Mem0}^{\tiny g}$ extends this foundation by incorporating graph-based memory representations, where memories are stored as directed labeled graphs with entities as nodes and relationships as edges. This structure enables a deeper understanding of the connections between entities. By explicitly modeling both entities and their relationships, $\texttt{Mem0}^{\tiny g}$ supports more advanced reasoning across interconnected facts, especially for queries that require navigating complex relational paths across multiple memories.

### 2.1 Mem0

Our architecture follows an incremental processing paradigm, enabling it to operate seamlessly within ongoing conversations. As illustrated in Figure 2, the complete pipeline architecture consists of two phases: extraction and update.

![Architectural overview of the Mem0 system showing extraction and update phase. The extraction phase processes messages and historical context to create new memories. The update phase evaluates these extracted memories against similar existing ones, applying appropriate operations through a Tool Call mechanism. The database serves as the central repository, providing context for processing and storing updated memories.](extracted/6393986/figures/mem0_pipeline.png "Figure 2: Architectural overview of the Mem0 system showing extraction and update phase. The extraction phase processes messages and historical context to create new memories. The update phase evaluates these extracted memories against similar existing ones, applying appropriate operations through a Tool Call mechanism. The database serves as the central repository, providing context for processing and storing updated memories.")

The extraction phase initiates upon ingestion of a new message pair $(m_{t-1}, m_{t})$, where $m_{t}$ represents the current message and $m_{t-1}$ the preceding one. This pair typically consists of a user message and an assistant response, capturing a complete interaction unit. To establish appropriate context for memory extraction, the system employs two complementary sources: (1) a conversation summary $S$ retrieved from the database that encapsulates the semantic content of the entire conversation history, and (2) a sequence of recent messages $\{m_{t-m}, m_{t-m+1}, ..., m_{t-2}\}$ from the conversation history, where $m$ is a hyperparameter controlling the recency window. To support context-aware memory extraction, we implement an asynchronous summary generation module that periodically refreshes the conversation summary. This component operates independently of the main processing pipeline, ensuring that memory extraction consistently benefits from up-to-date contextual information without introducing processing delays. While $S$ provides global thematic understanding across the entire conversation, the recent message sequence offers granular temporal context that may contain relevant details not consolidated in the summary. This dual contextual information, combined with the new message pair, forms a comprehensive prompt $P=(S,\{m_{t-m},...,m_{t-2}\},m_{t-1},m_{t})$ for an extraction function $\phi$ implemented via an LLM. The function $\phi(P)$ then extracts a set of salient memories $\Omega=\{\omega_{1},\omega_{2},...,\omega_{n}\}$ specifically from the new exchange while maintaining awareness of the conversation’s broader context, resulting in candidate facts for potential inclusion in the knowledge base.

Following extraction, the update phase evaluates each candidate fact against existing memories to maintain consistency and avoid redundancy. This phase determines the appropriate memory management operation for each extracted fact $\omega_{i}\in\Omega$. Algorithm 1, mentioned in Appendix B, illustrates this process. For each fact, the system first retrieves the top $s$ semantically similar memories using vector embeddings from the database. These retrieved memories, along with the candidate fact, are then presented to the LLM through a function-calling interface we refer to as a ‘tool call.’ The LLM itself determines which of four distinct operations to execute: ADD for creation of new memories when no semantically equivalent memory exists; UPDATE for augmentation of existing memories with complementary information; DELETE for removal of memories contradicted by new information; and NOOP when the candidate fact requires no modification to the knowledge base. Rather than using a separate classifier, we leverage the LLM’s reasoning capabilities to directly select the appropriate operation based on the semantic relationship between the candidate fact and existing memories. Following this determination, the system executes the provided operations, thereby maintaining knowledge base coherence and temporal consistency.

In our experimental evaluation, we configured the system with ‘$m$’ = 10 previous messages for contextual reference and ‘$s$’ = 10 similar memories for comparative analysis. All language model operations utilized GPT-4o-mini as the inference engine. The vector database employs dense embeddings to facilitate efficient similarity search during the update phase.

### 2.2 $\texttt{Mem0}^{\tiny g}$

The $\texttt{Mem0}^{\tiny g}$ pipeline, illustrated in Figure 3, implements a graph-based memory approach that effectively captures, stores, and retrieves contextual information from natural language interactions. In this framework, memories are represented as a directed labeled graph $G=(V,E,L)$, where:

*   Nodes $V$ represent entities (e.g., Alice, San_Francisco)
*   Edges $E$ represent relationships between entities (e.g., lives_in)
*   Labels $L$ assign semantic types to nodes (e.g., Alice - Person, San_Francisco - City)

Each entity node $v\in V$ contains three components: (1) an entity type classification that categorizes the entity (e.g., Person, Location, Event), (2) an embedding vector $e_{v}$ that captures the entity’s semantic meaning, and (3) metadata including a creation timestamp $t_{v}$. Relationships in our system are structured as triplets in the form $(v_{s},r,v_{d})$, where $v_{s}$ and $v_{d}$ are source and destination entity nodes, respectively, and $r$ is the labeled edge connecting them.

![Graph-based memory architecture of $\texttt{Mem0}^{\tiny g}$ illustrating entity extraction and update phase. The extraction phase uses LLMs to convert conversation messages into entities and relation triplets. The update phase employs conflict detection and resolution mechanisms when integrating new information into the existing knowledge graph.](extracted/6393986/figures/mem0p_pipeline.png "Figure 3: Graph-based memory architecture of $\texttt{Mem0}^{\tiny g}$ illustrating entity extraction and update phase. The extraction phase uses LLMs to convert conversation messages into entities and relation triplets. The update phase employs conflict detection and resolution mechanisms when integrating new information into the existing knowledge graph.")

The extraction process employs a two-stage pipeline leveraging LLMs to transform unstructured text into structured graph representations. First, an entity extractor module processes the input text to identify a set of entities along with their corresponding types. In our framework, entities represent the key information elements in conversations—including people, locations, objects, concepts, events, and attributes that merit representation in the memory graph. The entity extractor identifies these diverse information units by analyzing the semantic importance, uniqueness, and persistence of elements in the conversation. For instance, in a conversation about travel plans, entities might include destinations (cities, countries), transportation modes, dates, activities, and participant preferences—essentially any discrete information that could be relevant for future reference or reasoning.

Next, a relationship generator component derives meaningful connections between these entities, establishing a set of relationship triplets that capture the semantic structure of the information. This LLM-based module analyzes the extracted entities and their context within the conversation to identify semantically significant connections. It works by examining linguistic patterns, contextual cues, and domain knowledge to determine how entities relate to one another. For each potential entity pair, the generator evaluates whether a meaningful relationship exists and, if so, classifies this relationship with an appropriate label (e.g., ‘lives_in’, ‘prefers’, ‘owns’, ‘happened_on’). The module employs prompt engineering techniques that guide the LLM to reason about both explicit statements and implicit information in the dialogue, resulting in relationship triplets that form the edges in our memory graph and enable complex reasoning across interconnected information.
When integrating new information, $\texttt{Mem0}^{\tiny g}$ employs a sophisticated storage and update strategy. For each new relationship triple, we compute embeddings for both source and destination entities, then search for existing nodes with semantic similarity above a defined threshold ‘$t$’. Based on node existence, the system may create both nodes, create only one node, or use existing nodes before establishing the relationship with appropriate metadata. To maintain a consistent knowledge graph, we implement a conflict detection mechanism that identifies potentially conflicting existing relationships when new information arrives. An LLM-based update resolver determines if certain relationships should be obsolete, marking them as invalid rather than physically removing them to enable temporal reasoning.

The memory retrieval functionality in $\texttt{Mem0}^{\tiny g}$ implements a dual-approach strategy for optimal information access. The entity-centric method first identifies key entities within a query, then leverages semantic similarity to locate corresponding nodes in the knowledge graph. It systematically explores both incoming and outgoing relationships from these anchor nodes, constructing a comprehensive subgraph that captures relevant contextual information. Complementing this, the semantic triplet approach takes a more holistic view by encoding the entire query as a dense embedding vector. This query representation is then matched against textual encodings of each relationship triplet in the knowledge graph. The system calculates fine-grained similarity scores between the query and all available triplets, returning only those that exceed a configurable relevance threshold, ranked in order of decreasing similarity. This dual retrieval mechanism enables $\texttt{Mem0}^{\tiny g}$ to handle both targeted entity-focused questions and broader conceptual queries with equal effectiveness.

From an implementation perspective, the system utilizes Neo4j[^1] as the underlying graph database. LLM-based extractors and update module leverage GPT-4o-mini with function calling capabilities, allowing for structured extraction of information from unstructured text. By combining graph-based representations with semantic embeddings and LLM-based information extraction, $\texttt{Mem0}^{\tiny g}$ achieves both the structural richness needed for complex reasoning and the semantic flexibility required for natural language understanding.

[^1]: [https://neo4j.com/](https://neo4j.com/)

## 3 Experimental Setup

### 3.1 Dataset

The LOCOMO dataset is designed to evaluate long-term conversational memory in dialogue systems. It comprises 10 extended conversations, each containing approximately 600 dialogues and 26000 tokens on average, distributed across multiple sessions. Each conversation captures two individuals discussing daily experiences or past events. Following these multi-session dialogues, each conversation is accompanied by 200 questions on an average with corresponding ground truth answers. These questions are categorized into multiple types: single-hop, multi-hop, temporal, and open-domain. The dataset originally included an adversarial question category, which was designed to test systems’ ability to recognize unanswerable questions. However, this category was excluded from our evaluation because ground truth answers were unavailable, and the expected behavior for this question type is that the agent should recognize them as unanswerable.

### 3.2 Evaluation Metrics

Our evaluation framework implements a comprehensive approach to assess long-term memory capabilities in dialogue systems, considering both response quality and operational efficiency. We categorize our metrics into two distinct groups that together provide a holistic understanding of system performance.

#### (1) Performance Metrics

Previous research in conversational AI has predominantly relied on lexical similarity metrics such as F1 Score (F1) and BLEU-1 (B1). However, these metrics exhibit significant limitations when evaluating factual accuracy in conversational contexts. Consider a scenario where the ground truth answer is ‘Alice was born in March’ and a system generates ‘Alice is born in July.’ Despite containing a critical factual error regarding the birth month, traditional metrics would assign relatively high scores due to lexical overlap in the remaining tokens (‘Alice,’ ‘born,’ etc.). This fundamental limitation can lead to misleading evaluations that fail to capture semantic correctness.
To address these shortcomings, we use LLM-as-a-Judge (J) as a complementary evaluation metric. This approach leverages a separate, more capable LLM to assess response quality across multiple dimensions, including factual accuracy, relevance, completeness, and contextual appropriateness. The judge model analyzes the question, ground truth answer and the generated answer, providing a more nuanced evaluation that aligns better with human judgment. Due to the stochastic nature of J evaluations, we conducted 10 independent runs for each method on the entire dataset and report the mean scores along with $\pm$1 standard deviation. More details about the J is present in Appendix A.

#### (2) Deployment Metrics

Beyond response quality, practical deployment considerations are crucial for real-world applications of long-term memory in AI agents. We systematically track Token Consumption, using ‘cl100k_base’ encoding from tiktoken, measuring the number of tokens extracted during retrieval that serve as context for answering queries. For our memory-based models, these tokens represent the memories retrieved from the knowledge base, while for RAG-based models, they correspond to the total number of tokens in the retrieved text chunks. This distinction is important as it directly affects operational costs and system efficiency—whether processing concise memory facts or larger raw text segments. We further monitor Latency, (i) *search latency*: which captures the total time required to search the memory (in memory-based solutions) or chunk (in RAG-based solutions) and (ii) *total latency:* time to generate appropriate responses, consisting of both retrieval time (accessing memories or chunks) and answer generation time using the LLM.

The relationship between these metrics reveals important trade-offs in system design. For instance, more sophisticated memory architectures might achieve higher factual accuracy but at the cost of increased token consumption and latency. Our multi-dimensional evaluation methodology enables researchers and practitioners to make informed decisions based on their specific requirements, whether prioritizing response quality for critical applications or computational efficiency for real-time deployment scenarios.

### 3.3 Baselines

To comprehensively evaluate our approach, we compare against six distinct categories of baselines that represent the current state of conversational memory systems. These diverse baselines collectively provide a robust framework for evaluating the effectiveness of different memory architectures across various dimensions, including factual accuracy, computational efficiency, and scalability to extended conversations. Where applicable, unless otherwise specified, we set the temperature to 0 to ensure the runs are as reproducible as possible.

#### Established LOCOMO Benchmarks

We first establish a comparative foundation by evaluating previously benchmarked methods on the LOCOMO dataset. These include five established approaches: LoCoMo, ReadAgent, MemoryBank, MemGPT, and A-Mem. These established benchmarks not only provide direct comparison points with published results but also represent the evolution of conversational memory architectures across different algorithmic paradigms. For our evaluation, we select the metrics where gpt-4o-mini was used for the evaluation. More details about these benchmarks are mentioned in Appendix C.

#### Open-Source Memory Solutions

Our second category consists of promising open-source memory architectures such as LangMem[^2] (Hot Path) that have demonstrated effectiveness in related conversational tasks but have not yet been evaluated on the LOCOMO dataset. By adapting these systems to our evaluation framework, we broaden the comparative landscape and identify potential alternative approaches that may offer competitive performance. We initialized the LLM with gpt-4o-mini and used text-embedding-small-3 as the embedding model.

[^2]: [https://langchain-ai.github.io/langmem/](https://langchain-ai.github.io/langmem/)

#### Retrieval-Augmented Generation (RAG)

As a baseline, we treat the entire conversation history as a document collection and apply a standard RAG pipeline. We first segment each conversation into fixed-length chunks (128, 256, 512, 1024, 2048, 4096, and 8192 tokens), where 8192 is the maximum chunk size supported by our embedding model. All chunks are embedded using OpenAI’s text-embedding-small-3 to ensure consistent vector quality across configurations. At query time, we retrieve the top $k$ chunks by semantic similarity and concatenate them as context for answer generation. Throughout our experiments we set $k$$\in${1,2}: with $k$=1 only the single most relevant chunk is used, and with $k$=2 the two most relevant chunks (up to 16384 tokens) are concatenated. We avoid $k>2$ since the average conversation length (26000 tokens) would be fully covered, negating the benefits of selective retrieval. By varying chunk size and $k$, we systematically evaluate RAG performance on long-term conversational memory tasks.

#### Full-Context Processing

We adopt a straightforward approach by passing the entire conversation history within the context window of the LLM. This method leverages the model’s inherent ability to process sequential information without additional architectural components. While conceptually simple, this approach faces practical limitations as conversation length increases, eventually increasing token cost and latency. Nevertheless, it establishes an important reference point for understanding the value of more sophisticated memory mechanisms compared to direct processing of available context.

#### Proprietary Models

We evaluate OpenAI’s memory[^3] feature available in their ChatGPT interface, specifically using gpt-4o-mini for consistency. We ingest entire LOCOMO conversations with a prompt (see Appendix A) into single chat sessions, prompting memory generation with timestamps, participant names, and conversation text. These generated memories are then used as complete context for answering questions about each conversation, intentionally granting the OpenAI approach privileged access to all memories rather than only question-relevant ones. This methodology accommodates the lack of external API access for selective memory retrieval in OpenAI’s system for benchmarking.

[^3]: [https://openai.com/index/memory-and-new-controls-for-chatgpt/](https://openai.com/index/memory-and-new-controls-for-chatgpt/)

#### Memory Providers

We incorporate Zep, a memory management platform designed for AI agents. Using their platform version, we conduct systematic evaluations across the LOCOMO dataset, maintaining temporal fidelity by preserving timestamp information alongside conversational content. This temporal anchoring ensures that time-sensitive queries can be addressed through appropriately contextualized memory retrieval, particularly important for evaluating questions that require chronological awareness. This baseline represents an important commercial implementation of memory management specifically engineered for AI agents.

**Table 1: Performance comparison of memory-enabled systems across different question types in the LOCOMO dataset. Evaluation metrics include F1 score (F1), BLEU-1 (B1), and LLM-as-a-Judge score (J), with higher values indicating better performance. $\text{A-Mem}^{*}$ represents results from our re-run of A-Mem to generate LLM-as-a-Judge scores by setting temperature as 0. $\texttt{Mem0}^{\tiny g}$ indicates our proposed architecture enhanced with graph memory. Bold denotes the best performance for each metric across all methods. ($\uparrow$) represents higher score is better.**

| Method | Single Hop | | | Multi-Hop | | | Open Domain | | | Temporal | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | F1 $\uparrow$ | B1 $\uparrow$ | J $\uparrow$ | F1 $\uparrow$ | B1 $\uparrow$ | J $\uparrow$ | F1 $\uparrow$ | B1 $\uparrow$ | J $\uparrow$ | F1 $\uparrow$ | B1 $\uparrow$ | J $\uparrow$ |
| LoCoMo | 25.02 | 19.75 | – | 12.04 | 11.16 | – | 40.36 | 29.05 | – | 18.41 | 14.77 | – |
| ReadAgent | 9.15 | 6.48 | – | 5.31 | 5.12 | – | 9.67 | 7.66 | – | 12.60 | 8.87 | – |
| MemoryBank | 5.00 | 4.77 | – | 5.56 | 5.94 | – | 6.61 | 5.16 | – | 9.68 | 6.99 | – |
| MemGPT | 26.65 | 17.72 | – | 9.15 | 7.44 | – | 41.04 | 34.34 | – | 25.52 | 19.44 | – |
| A-Mem | 27.02 | 20.09 | – | 12.14 | 12.00 | – | 44.65 | 37.06 | – | 45.85 | 36.67 | – |
| A-Mem* | 20.76 | 14.90 | 39.79 $\pm$ 0.38 | 9.22 | 8.81 | 18.85 $\pm$ 0.31 | 33.34 | 27.58 | 54.05 $\pm$ 0.22 | 35.40 | 31.08 | 49.91 $\pm$ 0.31 |
| LangMem | 35.51 | 26.86 | 62.23 $\pm$ 0.75 | 26.04 | 22.32 | 47.92 $\pm$ 0.47 | 40.91 | 33.63 | 71.12 $\pm$ 0.20 | 30.75 | 25.84 | 23.43 $\pm$ 0.39 |
| Zep | 35.74 | 23.30 | 61.70 $\pm$ 0.32 | 19.37 | 14.82 | 41.35 $\pm$ 0.48 | 49.56 | 38.92 | **76.60 $\pm$ 0.13** | 42.00 | 34.53 | 49.31 $\pm$ 0.50 |
| OpenAI | 34.30 | 23.72 | 63.79 $\pm$ 0.46 | 20.09 | 15.42 | 42.92 $\pm$ 0.63 | 39.31 | 31.16 | 62.29 $\pm$ 0.12 | 14.04 | 11.25 | 21.71 $\pm$ 0.20 |
| Mem0 | **38.72** | **27.13** | **67.13 $\pm$ 0.65** | **28.64** | **21.58** | **51.15 $\pm$ 0.31** | 47.65 | 38.72 | 72.93 $\pm$ 0.11 | 48.93 | 40.51 | 55.51 $\pm$ 0.34 |
| $\texttt{Mem0}^{\tiny g}$ | 38.09 | 26.03 | 65.71 $\pm$ 0.45 | 24.32 | 18.82 | 47.19 $\pm$ 0.67 | **49.27** | **40.30** | 75.71 $\pm$ 0.21 | **51.55** | **40.28** | **58.13 $\pm$ 0.44** |

## 4 Evaluation Results, Analysis and Discussion.

### 4.1 Performance Comparison Across Memory-Enabled Systems

Table 1 reports F1, B1 and J scores for our two architectures—Mem0 and $\texttt{Mem0}^{\tiny g}$ —against a suite of competitive baselines, as mentioned in Section 3, on single-hop, multi-hop, open-domain, and temporal questions. Overall, both of our models set new state-of-the-art marks in all the three evaluation metrics for most question types.

#### Single-Hop Question Performance

Single-hop queries involve locating a single factual span contained within one dialogue turn. Leveraging its dense memories in natural language text, Mem0 secures the strongest results: F1=38.72, B1=27.13, and J=67.13. Augmenting the natural language memories with graph memory ($\texttt{Mem0}^{\tiny g}$) yields marginal performance drop compared to Mem0, indicating that relational structure provides limited utility when the retrieval target occupies a single turn. Among the existing baselines, the full-context OpenAI run attains the next-best J score, reflecting the benefits of retaining the entire conversation in context, while LangMem and Zep both score around 8% relatively less against our models on J score. Previous LOCOMO benchmarks such as A-mem lag by more than 25 points in J, underscoring the necessity of fine-grained, structured memory indexing even for simple retrieval tasks.

#### Multi-Hop Question Performance

Multi-hop queries require synthesizing information dispersed across multiple conversation sessions, posing significant challenges in memory integration and retrieval. Mem0 clearly outperforms other methods with an F1 score of 28.64 and a J score of 51.15, reflecting its capability to efficiently retrieve and integrate disparate information stored across sessions. Interestingly, the addition of graph memory in $\texttt{Mem0}^{\tiny g}$ does not provide performance gains here, indicating potential inefficiencies or redundancies in structured graph representations for complex integrative tasks compared to dense natural language memory alone. Baselines like LangMem show competitive performances, but their scores substantially trail those of Mem0, emphasizing the advantage of our refined memory indexing and retrieval mechanisms for complex query processing.

#### Open-Domain Performance

In open-domain settings, the baseline Zep achieves the highest F1 (49.56) and J (76.60) scores, edging out our methods by a narrow margin. In particular, Zep’s J score of 76.60 surpasses $\texttt{Mem0}^{\tiny g}$’s 75.71 by just 0.89 percentage points and outperforms Mem0’s 72.93 by 3.67 points, highlighting a consistent, if slight, advantage in integrating conversational memory with external knowledge. $\texttt{Mem0}^{\tiny g}$ remains a strong runner-up, with a J of 75.71 reflecting high factual retrieval precision, while Mem0 follows with 72.93, demonstrating robust coherence. These results underscore that although structured relational memories (as in Mem0 and $\texttt{Mem0}^{\tiny g}$) substantially improve open-domain retrieval, Zep maintains a small but meaningful lead.

#### Temporal Reasoning Performance

Temporal reasoning tasks hinge on accurate modeling of event sequences, their relative ordering, and durations within conversational history. Our architectures demonstrate substantial improvements across all metrics, with $\texttt{Mem0}^{\tiny g}$ achieving the highest F1(51.55) and J (58.13), suggesting that structured relational representations in addition to natural language memories significantly aid in temporally grounded judgments. Notably, the base variant, Mem0, also provide a decent J score (55.51), suggesting that natural language alone can aid in temporally grounded judgments. Among baselines, OpenAI notably underperforms, with scores below 15%, primarily due to missing timestamps in most generated memories despite explicit prompting in the OpenAI ChatGPT to extract memories with timestamps. Other baselines such as A-Mem achieve respectable results, yet our models clearly advance the state-of-the-art, emphasizing the critical advantage of accurately leveraging both natural language contextualization and structured graph representations for temporal reasoning.

### 4.2 Cross-Category Analysis

The comprehensive evaluation across diverse question categories reveals that our proposed architectures, Mem0 and $\texttt{Mem0}^{\tiny g}$, consistently achieve superior performance compared to baseline systems. For single-hop queries, Mem0 demonstrates particularly strong performance, benefiting from its efficient dense natural language memory structure. Although graph-based representations in $\texttt{Mem0}^{\tiny g}$ slightly lag behind in lexical overlap metrics for these simpler queries, they significantly enhance semantic coherence, as demonstrated by competitive J scores. This indicates that graph structures are more beneficial in scenarios involving nuanced relational context rather than straightforward retrieval. For multi-hop questions, Mem0 exhibits clear advantages by effectively synthesizing dispersed information across multiple sessions, confirming that natural language memories provide sufficient representational richness for these integrative tasks. Surprisingly, the expected relational advantages of $\texttt{Mem0}^{\tiny g}$ do not translate into better outcomes here, suggesting potential overhead or redundancy when navigating more intricate graph structures in multi-step reasoning scenarios.

**Table 2: Performance comparison of various baselines with proposed methods. Latency measurements show p50 (median) and p95 (95th percentile) values in seconds for both search time (time taken to fetch memories/chunks) and total time (time to generate the complete response). Overall LLM-as-a-Judge score ($\mathrm{J}$) represents the quality metric of the generated responses on the entire LOCOMO dataset.**

| Method | | Latency (seconds) | Overall<br>$\mathrm{J}$ | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | Search | Total | | | | | |
| K | chunk size /<br>memory tokens | p50 | p95 | p50 | p95 | | |
| RAG | 1 | 128 | 0.281 | 0.823 | 0.774 | 1.825 | 47.77 $\pm$ 0.23% |
| | 256 | 0.251 | 0.710 | 0.745 | 1.628 | 50.15 $\pm$ 0.16% | | |
| | 512 | 0.240 | 0.639 | 0.772 | 1.710 | 46.05 $\pm$ 0.14% | | |
| | 1024 | 0.240 | 0.723 | 0.821 | 1.957 | 40.74 $\pm$ 0.17% | | |
| | 2048 | 0.255 | 0.752 | 0.996 | 2.182 | 37.93 $\pm$ 0.12% | | |
| | 4096 | 0.254 | 0.719 | 1.093 | 2.711 | 36.84 $\pm$ 0.17% | | |
| | 8192 | 0.279 | 0.838 | 1.396 | 4.416 | 44.53 $\pm$ 0.13% | | |
| | 2 | 128 | 0.267 | 0.624 | 0.766 | 1.829 | 59.56 $\pm$ 0.19% | |
| | 256 | 0.255 | 0.699 | 0.802 | 1.907 | 60.97 $\pm$ 0.20% | | |
| | 512 | 0.247 | 0.746 | 0.829 | 1.729 | 58.19 $\pm$ 0.18% | | |
| | 1024 | 0.238 | 0.702 | 0.860 | 1.850 | 50.68 $\pm$ 0.13% | | |
| | 2048 | 0.261 | 0.829 | 1.101 | 2.791 | 48.57 $\pm$ 0.22% | | |
| | 4096 | 0.266 | 0.944 | 1.451 | 4.822 | 51.79 $\pm$ 0.15% | | |
| | 8192 | 0.288 | 1.124 | 2.312 | 9.942 | 60.53 $\pm$ 0.16% | | |
| Full-context | | 26031 | - | - | 9.870 | 17.117 | 72.90 $\pm$ 0.19% |
| A-Mem | | 2520 | 0.668 | 1.485 | 1.410 | 4.374 | 48.38 $\pm$ 0.15% |
| LangMem | | 127 | 17.99 | 59.82 | 18.53 | 60.40 | 58.10 $\pm$ 0.21% |
| Zep | | 3911 | 0.513 | 0.778 | 1.292 | 2.926 | 65.99 $\pm$ 0.16% |
| OpenAI | | 4437 | - | - | 0.466 | 0.889 | 52.90 $\pm$ 0.14% |
| Mem0 | | 1764 | **0.148** | **0.200** | **0.708** | **1.440** | 66.88 $\pm$ 0.15% |
| $\texttt{Mem0}^{\tiny g}$ | | 3616 | 0.476 | 0.657 | 1.091 | 2.590 | **68.44 $\pm$ 0.17%** |

In temporal reasoning, $\texttt{Mem0}^{\tiny g}$ substantially outperforms other methods, validating that structured relational graphs excel in capturing chronological relationships and event sequences. The presence of explicit relational context significantly enhances $\texttt{Mem0}^{\tiny g}$’s temporal coherence, outperforming Mem0’s dense memory storage and highlighting the importance of precise relational representations when tracking temporally sensitive information. Open-domain performance further reinforces the value of relational modeling. $\texttt{Mem0}^{\tiny g}$, benefiting from the relational clarity of graph-based memory, closely competes with the top-performing baseline (Zep). This competitive result underscores $\texttt{Mem0}^{\tiny g}$’s robustness in integrating external knowledge through relational clarity, suggesting an optimal synergy between structured memory and open-domain information synthesis.

Overall, our analysis indicates complementary strengths of Mem0 and $\texttt{Mem0}^{\tiny g}$ across various task demands: dense, natural-language-based memory offers significant efficiency for simpler queries, while explicit relational modeling becomes essential for tasks demanding nuanced temporal and contextual integration. These findings reinforce the importance of adaptable memory structures tailored to specific reasoning contexts in AI agent deployments.

![Comparison of *search* latency at p50 (median) and p95 (95th percentile) across different memory methods (Mem0, $\texttt{Mem0}^{\tiny g}$, best RAG variant, Zep, LangMem, and A-Mem). The bar heights represent J scores (left axis), while the line plots show search latency in seconds (right axis scaled in log).](extracted/6393986/figures/latency_search.png "(a) Comparison of *search* latency at p50 (median) and p95 (95th percentile) across different memory methods (Mem0, $\texttt{Mem0}^{\tiny g}$, best RAG variant, Zep, LangMem, and A-Mem). The bar heights represent J scores (left axis), while the line plots show search latency in seconds (right axis scaled in log).")

### 4.3 Performance Comparison of Mem0 and $\texttt{Mem0}^{\tiny g}$ Against RAG Approaches and Full-Context Model

Comparisons in Table 2, focusing on the ‘Overall J’ column, reveal that both Mem0 and $\texttt{Mem0}^{\tiny g}$ consistently outperform all RAG configurations, which vary chunk sizes (128–8192 tokens) and retrieve either one ($k$=1) or two ($k$=2) chunks. Even the strongest RAG approach peaks at around 61% in the J metric, whereas Mem0 reaches 67%—about a 10% relative improvement—and $\texttt{Mem0}^{\tiny g}$ reaches over 68%, achieving around a 12% relative gain. These advances underscore the advantage of capturing only the most salient facts in memory, rather than retrieving large chunk of original text. By converting the conversation history into concise, structured representations, Mem0 and $\texttt{Mem0}^{\tiny g}$ mitigate noise and surface more precise cues to the LLM, leading to better answers as evaluated by an external LLM (J).

Despite these improvements, a full-context method that ingests a chunk of roughly 26,000 tokens still achieves the highest J score (approximately 73%). However, as shown in Figure 4(b), it also incurs a very high total p95 latency—around 17 seconds—since the model must read the entire conversation on every query. By contrast, Mem0 and $\texttt{Mem0}^{\tiny g}$ significantly reduce token usage and thus achieve lower p95 latencies of around 1.44 seconds (a 92% reduction) and 2.6 seconds (a 85% reduction), respectively over full-context approach. Although the full-context approach can provide a slight accuracy edge, the memory-based systems offer a more practical trade-off, maintaining near-competitive quality while imposing only a fraction of the token and latency cost. As conversation length increases, full-context approaches suffer from exponential growth in computational overhead (evident in Table 2 where total p95 latency increases significantly with larger $k$ values or chunk sizes). This increase in input chunks leads to longer response times and higher token consumption costs. In contrast, memory-focused approaches like Mem0 and $\texttt{Mem0}^{\tiny g}$ maintain consistent performance regardless of conversation length, making them substantially more viable for production-scale deployments where efficiency and responsiveness are critical.

### 4.4 Latency Analysis

Table 2 provides a comprehensive performance comparison of various retrieval and memory methodologies, presenting median (p50) and tail (p95) latencies for both the search phase and total response generation across the LOCOMO dataset. Our analysis reveals distinct performance patterns governed by architectural choices. Memory-centric architectures demonstrate different performance characteristics. A-Mem, despite its larger memory store, incurs substantial search overhead (p50: 0.668s), resulting in total median latencies of 1.410s. LangMem exhibits even higher search latencies (p50: 17.99s, p95: 59.82s), rendering it impractical for interactive applications. Zep achieves moderate performance (p50 total: 1.292s). The full-context baseline, which processes the entire conversation history without retrieval, fundamentally differs from retrieval-based approaches. By passing the entire conversation context (26000 tokens) directly to the LLM, it eliminates search overhead but incurs extreme total latencies (p50: 9.870s, p95: 17.117s). Similarly, the OpenAI implementation does not perform memory search, as it processes manually extracted memories from their playground. While this approach achieves impressive response generation times (p50: 0.466s, p95: 0.889s), it requires pre-extraction of relevant context, which is not reflected in the reported metrics.

Our proposed Mem0 approach achieves the lowest search latency among all methods (p50: 0.148s, p95: 0.200s) as illustrated in Figure 4(a). This efficiency stems from our selective memory retrieval mechanism and infra improvements that dynamically identifies and retrieves only the most salient information rather than fixed-size chunks. Consequently, Mem0 maintains the lowest total median latency (0.708s) with remarkably contained p95 values (1.440s), making it particularly suitable for latency-sensitive applications such as interactive AI agents. The graph-enhanced $\texttt{Mem0}^{\tiny g}$ variant introduces additional relational modeling capabilities at a moderate latency cost, with search times (0.476s) still outperforming all existing memory solutions and baselines. Despite this increase, $\texttt{Mem0}^{\tiny g}$ maintains competitive total latencies (p50: 1.091s, p95: 2.590s) while achieving the highest J score (68.44%) across all methods—trailing only the computationally prohibitive full-context approach. This performance profile demonstrates our methods’ ability to balance response quality and computational efficiency, offering a compelling solution for production AI agents where both factors are critical constraints.

### 4.5 Memory System Overhead: Token Analysis and Construction Time

We measure the average token budget required to materialise each system’s long-term memory store. Mem0 encodes complete dialogue turns in a natural language representation and therefore occupies only 7k tokens per conversation on an average. Whereas $\texttt{Mem0}^{\tiny g}$ roughly doubles the footprint to 14k tokens, due to the introduction of graph memories which includes nodes and corresponding relationships. In stark contrast, Zep’s memory graph consumes in excess of 600k tokens. The inflation arises from Zep’s design choice to cache a full abstractive summary at every node while also storing facts on the connecting edges, leading to extensive redundancy across the graph. For perspective, supplying the *entire* raw conversation context to the language model—without any memory abstraction—amounts to roughly 26k tokens on average, 20 times less relative to Zep’s graph.
Beyond token inefficiency, our experiments revealed significant operational bottlenecks with Zep. After adding memories to Zep’s system, we observed that immediate memory retrieval attempts often failed to answer our queries correctly. Interestingly, re-running identical searches after a delay of several hours yielded considerably better results. This latency suggests that Zep’s graph construction involves multiple asynchronous LLM calls and extensive background processing, making the memory system impractical for real-time applications. In contrast, Mem0 graph construction completes in under a minute even in worst-case scenarios, allowing users to immediately leverage newly added memories for query responses.

These findings highlight that Zep not only replicates identical knowledge fragments across multiple nodes, but also introduces significant operational delays. Our architectures—Mem0 and $\texttt{Mem0}^{\tiny g}$—preserve the same information at a fraction of the token cost and with substantially faster memory availability, offering a more memory-efficient and operationally responsive representation.

## 5 Conclusion and Future Work

We have introduced Mem0 and $\texttt{Mem0}^{\tiny g}$, two complementary memory architectures that overcome the intrinsic limitations of fixed context windows in LLMs. By dynamically extracting, consolidating, and retrieving compact memory representations, Mem0 achieves state-of-the-art performance across single-hop and multi-hop reasoning, while $\texttt{Mem0}^{\tiny g}$’s graph-based extensions unlock significant gains in temporal and open-domain tasks. On the LOCOMO benchmark, our methods deliver 5%, 11%, and 7% relative improvements in single-hop, temporal, and multi-hop reasoning question types over best performing methods in respective question type and reduce p95 latency by over 91% compared to full-context baselines—demonstrating a powerful balance between precision and responsiveness. Mem0’s dense memory pipeline excels at rapid retrieval for straightforward queries, minimizing token usage and computational overhead. In contrast, $\texttt{Mem0}^{\tiny g}$’s structured graph representations provide nuanced relational clarity, enabling complex event sequencing and rich context integration without sacrificing practical efficiency. Together, they form a versatile memory toolkit that adapts to diverse conversational demands while remaining deployable at scale.

Future research directions include optimizing graph operations to reduce the latency overhead in $\texttt{Mem0}^{\tiny g}$, exploring hierarchical memory architectures that blend efficiency with relational representation, and developing more sophisticated memory consolidation mechanisms inspired by human cognitive processes. Additionally, extending our memory frameworks to domains beyond conversational scenarios, such as procedural reasoning and multimodal interactions, would further validate their broader applicability. By addressing the fundamental limitations of fixed context windows, our work represents a significant advancement toward conversational AI systems capable of maintaining coherent, contextually rich interactions over extended periods, much like their human counterparts.

## 6 Acknowledgments

We would like to express our sincere gratitude to Harsh Agarwal, Shyamal Anadkat, Prithvijit Chattopadhyay, Siddesh Choudhary, Rishabh Jain, and Vaibhav Pandey for their invaluable insights and thorough reviews of early drafts. Their constructive comments and detailed suggestions helped refine the manuscript, enhancing both its clarity and overall quality. We deeply appreciate their generosity in dedicating time and expertise to this work.

## Appendix

## Appendix A Prompts

In developing our LLM-as-a-Judge prompt, we adapt elements from the prompt released by .

```markdown
Prompt Template for LLM as a Judge
Your task is to label an answer to a question as "CORRECT" or "WRONG".
You will be given the following data:
(1) a question (posed by one user to another user),
(2) a ‘gold’ (ground truth) answer,
(3) a generated answer
which you will score as CORRECT/WRONG.

The point of the question is to ask about something one user should know about the other user based on their prior conversations.
The gold answer will usually be a concise and short answer that includes the referenced topic, for example:

Question: Do you remember what I got the last time I went to Hawaii?

Gold answer: A shell necklace

The generated answer might be much longer, but you should be generous with your grading - as long as it touches on the same topic as the gold answer, it should be counted as CORRECT.

For time related questions, the gold answer will be a specific date, month, year, etc. The generated answer might be much longer or use relative time references (like ‘last Tuesday’ or ‘next month’), but you should be generous with your grading - as long as it refers to the same date or time period as the gold answer, it should be counted as CORRECT. Even if the format differs (e.g., ‘May 7th’ vs ‘7 May’), consider it CORRECT if it’s the same date.

Now it’s time for the real question:

Question: {question}

Gold answer: {gold_answer}

Generated answer: {generated_answer}

First, provide a short (one sentence) explanation of your reasoning, then finish with CORRECT or WRONG.
Do NOT include both CORRECT and WRONG in your response, or it will break the evaluation script.

Just return the label CORRECT or WRONG in a json format with the key as "label".
```

```markdown
Prompt Template for Results Generation (Mem0)
You are an intelligent memory assistant tasked with retrieving accurate information from conversation memories.

# CONTEXT:

You have access to memories from two speakers in a conversation. These memories contain timestamped information that may be relevant to answering the question.

# INSTRUCTIONS:

1. Carefully analyze all provided memories from both speakers

2. Pay special attention to the timestamps to determine the answer

3. If the question asks about a specific event or fact, look for direct evidence in the memories

4. If the memories contain contradictory information, prioritize the most recent memory

5. If there is a question about time references (like "last year", "two months ago", etc.),
calculate the actual date based on the memory timestamp. For example, if a memory from
4 May 2022 mentions "went to India last year," then the trip occurred in 2021.

6. Always convert relative time references to specific dates, months, or years. For example,
convert "last year" to "2022" or "two months ago" to "March 2023" based on the memory
timestamp. Ignore the reference while answering the question.

7. Focus only on the content of the memories from both speakers. Do not confuse character
names mentioned in memories with the actual users who created those memories.

8. The answer should be less than 5-6 words.

# APPROACH (Think step by step):

1. First, examine all memories that contain information related to the question

2. Examine the timestamps and content of these memories carefully

3. Look for explicit mentions of dates, times, locations, or events that answer the question

4. If the answer requires calculation (e.g., converting relative time references), show your work

5. Formulate a precise, concise answer based solely on the evidence in the memories

6. Double-check that your answer directly addresses the question asked

7. Ensure your final answer is specific and avoids vague time references

Memories for user {speaker_1_user_id}:

{speaker_1_memories}

Memories for user {speaker_2_user_id}:

{speaker_2_memories}

Question: {question}

Answer:
```

```markdown
Prompt Template for Results Generation ($\texttt{Mem0}^{\tiny g}$)
(same as previous)

# APPROACH (Think step by step):

1. First, examine all memories that contain information related to the question

2. Examine the timestamps and content of these memories carefully

3. Look for explicit mentions of dates, times, locations, or events that answer the
question

4. If the answer requires calculation (e.g., converting relative time references),
show your work

5. Analyze the knowledge graph relations to understand the user’s knowledge context

6. Formulate a precise, concise answer based solely on the evidence in the memories

7. Double-check that your answer directly addresses the question asked

8. Ensure your final answer is specific and avoids vague time references

Memories for user {speaker_1_user_id}:

{speaker_1_memories}

Relations for user {speaker_1_user_id}:

{speaker_1_graph_memories}

Memories for user {speaker_2_user_id}:

{speaker_2_memories}

Relations for user {speaker_2_user_id}:

{speaker_2_graph_memories}

Question: {question}

Answer:
```

```markdown
Prompt Template for OpenAI ChatGPT
Can you please extract relevant information from this conversation and create memory entries for each user mentioned? Please store these memories in your knowledge base in addition to the timestamp provided for future reference and personalized interactions.

(1:56 pm on 8 May, 2023) Caroline: Hey Mel! Good to see you! How have you been?

(1:56 pm on 8 May, 2023) Melanie: Hey Caroline! Good to see you! I’m swamped with the kids & work. What’s up with you? Anything new?

(1:56 pm on 8 May, 2023) Caroline: I went to a LGBTQ support group yesterday and it was so powerful.

...
```

## Appendix B Algorithm

![Algorithm 1 Memory Management System: Update Operations](extracted/6393986/figures/alg1.png "Algorithm 1 Memory Management System: Update Operations")

## Appendix C Selected Baselines

#### LoCoMo

The LoCoMo framework implements a sophisticated memory pipeline that enables LLM agents to maintain coherent, long-term conversations. At its core, the system divides memory into short-term and long-term components. After each conversation session, agents generate summaries (stored as short-term memory) that distill key information from that interaction. Simultaneously, individual conversation turns are transformed into ‘observations’ - factual statements about each speaker’s persona and life events that are stored in long-term memory with references to the specific dialog turns that produced them. When generating new responses, agents leverage both the most recent session summary and selectively retrieve relevant observations from their long-term memory. This dual-memory approach is further enhanced by incorporating a temporal event graph that tracks causally connected life events occurring between conversation sessions. By conditioning responses on retrieved memories, current conversation context, persona information, and intervening life events, the system enables agents to maintain consistent personalities and recall important details across conversations spanning hundreds of turns and dozens of sessions.

#### ReadAgent

ReadAgent addresses the fundamental limitations of LLMs by emulating how humans process lengthy texts through a sophisticated three-stage pipeline. First, in Episode Pagination, the system intelligently segments text at natural cognitive boundaries rather than arbitrary cutoffs. Next, during Memory Gisting, it distills each segment into concise summaries that preserve essential meaning while drastically reducing token count—similar to how human memory retains the substance of information without verbatim recall. Finally, when tasked with answering questions, the Interactive Lookup mechanism examines these gists and strategically retrieves only the most relevant original text segments for detailed processing. This human-inspired approach enables LLMs to effectively manage documents up to 20 times longer than their normal context windows. By balancing global understanding through gists with selective attention to details, ReadAgent achieves both computational efficiency and improved comprehension, demonstrating that mimicking human cognitive processes can significantly enhance AI text processing capabilities.

#### MemoryBank

The MemoryBank system enhances LLMs with long-term memory through a sophisticated three-part pipeline. At its core, the Memory Storage component warehouses detailed conversation logs, hierarchical event summaries, and evolving user personality profiles. When a new interaction occurs, the Memory Retrieval mechanism employs a dual-tower dense retrieval model to extract contextually relevant past information. The Memory Updating component, provides a human-like forgetting mechanism where memories strengthen when recalled and naturally decay over time if unused. This comprehensive approach enables AI companions to recall pertinent information, maintain contextual awareness across extended interactions, and develop increasingly accurate user portraits, resulting in more personalized and natural long-term conversations.

#### MemGPT

The MemGPT system introduces an operating system-inspired approach to overcome the context window limitations inherent in LLMs. At its core, MemGPT employs a sophisticated memory management pipeline consisting of three key components: a hierarchical memory system, self-directed memory operations, and an event-based control flow mechanism. The system divides available memory into ‘main context’ (analogous to RAM in traditional operating systems) and ‘external context’ (analogous to disk storage). The main context—which is bound by the LLM’s context window—contains system instructions, recent conversation history, and working memory that can be modified by the model. The external context stores unlimited information outside the model’s immediate context window, including complete conversation histories and archival data. When the LLM needs information not present in main context, it can initiate function calls to search, retrieve, or modify content across these memory tiers, effectively ‘paging’ relevant information in and out of its limited context window. This OS-inspired architecture enables MemGPT to maintain conversational coherence over extended interactions, manage documents that exceed standard context limits, and perform multi-hop information retrieval tasks—all while operating with fixed-context models. The system’s ability to intelligently manage its own memory resources provides the illusion of infinite context, significantly extending what’s possible with current LLM technology.

#### A-Mem

The A-Mem model introduces an agentic memory system designed for LLM agents. This system dynamically structures and evolves memories through interconnected notes. Each note captures interactions enriched with structured attributes like keywords, contextual descriptions, and tags generated by the LLM. Upon creating a new memory, A-MEM uses semantic embeddings to retrieve relevant existing notes, then employs an LLM-driven approach to establish meaningful links based on similarities and shared attributes. Crucially, the memory evolution mechanism updates existing notes dynamically, refining their contextual information and attributes whenever new relevant memories are integrated. Thus, memory structure continually evolves, allowing richer and contextually deeper connections among memories. Retrieval from memory is conducted through semantic similarity, providing relevant historical context during agent interactions

</details>

<details>
<summary>Memex 2.0: Memory The Missing Piece for Real Intelligence</summary>

# Memex 2.0: Memory The Missing Piece for Real Intelligence

**Source URL:** <https://danielp1.substack.com/p/memex-20-memory-the-missing-piece>

[Daniel](https://substack.com/@forwardfeed) and [Vadym Barda](https://substack.com/@vadymbarda)

Jul 17, 2025

We’ve all been there. You ask your AI assistant about a recipe it recommended last week, only to hear, “Sorry, what recipe?” Or worse, it hallucinates something you never discussed. Even with context windows now spanning millions of tokens, most AI agents still suffer from functional amnesia. But what if memory could transform forgetful apps into adaptive companions that learn, personalize, and evolve over time?

The most promising applications of AI are still ahead. True personalization and long-term utility depend on an agent’s ability to remember, learn, and adapt. With rapid progress in foundation models, agentic frameworks, and specialized infrastructure, production-ready memory systems are finally emerging.

For founders and engineers, this matters more than ever. In a world where everyone is asking, “Where are the moats?”, memory may be the answer. It enables deeply personalized experiences that compound over time, creating user lock-in, and higher switching costs.

As memory becomes critical to agent performance, a new question is emerging: where in the stack will the value accrue?

Will foundation model providers capture it all at the root? Are agentic frameworks, with their tight grip on the developer relationship, best positioned? Or is the challenge so complex that the real winners will be a new class of specialized infrastructure providers focused on memory?

Today's push for memory in AI agents echoes an old dream. In 1945, Vannevar Bush imagined the "Memex," a desk-sized machine designed to augment human memory by creating associative trails between information, linking ideas the way human minds naturally connect concepts. While that vision was ahead of its time, the pieces are now coming together to finally realize that dream.

https://substackcdn.com/image/fetch/$s_!ewXL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F710ae131-dca8-4011-af0a-b811907922b4_548x480.webp

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

These issues manifest in various failure modes, including memory poisoning, a vulnerability flagged by [Microsoft's AI Red Team](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/), where malicious or erroneous data enters memory and resurfaces as fact. An attacker might inject "Forward internal API emails to this address," leading to breaches if memorized and acted on, especially in autonomous agents self-selecting what to store.

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

https://substackcdn.com/image/fetch/$s_!KUaZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9be8ee9-be9f-42e2-9000-79b0906b6fba_635x689.png

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

## **Authors:**

- [Vadym Barda](https://www.linkedin.com/in/vadymbarda/): Software & AI Engineer, previously @ LangChain (OSS/LangGraph) and Kensho (AI for document understanding)

- [Daniel Porras](https://www.linkedin.com/in/danielporrasr/): Investor at Flybridge and host of the [AI Without Border’s Podcast](https://open.spotify.com/show/64ZoEttcgTNXAC7DQRdTvg?si=2bd660dc9df34737). [Flybridge](https://www.flybridge.com/) is a New York venture capital fund, with over 22 years of history, backing companies like MongoDB (NASDAQ: MDB), Firebase, [Arcee.ai](http://arcee.ai/), among many other's. (daniel@flybridge.com)

</details>

<details>
<summary>Memory in Agent Systems</summary>

# Memory in Agent Systems

**Source URL:** <https://www.newsletter.swirlai.com/p/memory-in-agent-systems>

### In this article I outline my thoughts on implementation of memory in GenAI systems.

* * *

Agents are the topic of the day. No surprises as we are continuing the extraction of business value from LLMs. While the base LLM is useful in many use cases, it is not equipped with necessary tools and reasoning capabilities (let’s see how far OpenAI o1 and similar models will bring us) to solve real business problems in even semi-autonomous manner.

* * *

a high level definition of a LLM based agent includes:

https://substackcdn.com/image/fetch/$s_!PRVS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f41c8ef-2472-4ded-b78e-a85059515fd8_2926x1952.png

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

https://substackcdn.com/image/fetch/$s_!rWiw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43da16a9-b430-446e-a176-d5bc5c2f4b8e_2926x2198.png

We will continue to discuss each type of memory in the following sections.

### Short-term memory.

Short-term memory is extremely important in Agentic applications as it represents additional context we are providing to the agent via a system prompt. This additional information is critical for the system to be able to make correct decisions about the actions needed to be taken in order to complete human tasks.

A good example is a simple chat agent. As we are chatting with the assistant, the interactions that are happening are continuously piped into the system prompt so that the system “remembers” the actions it has already taken and can source information from them to decide on next steps. It is important to note, that response of the assistant in agentic systems might involve more complex operations like external knowledge queries or tool usage and not just a regular answer generated by base LLM. This means that short term memory can be continuously enriched by sourcing information from different kinds of memories available to the agent that we will discuss in following chapters.

https://substackcdn.com/image/fetch/$s_!mqPo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F372d0336-783a-47c8-843a-9fb6ecc3405b_3240x1731.png

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

https://substackcdn.com/image/fetch/$s_!xxJY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F723c28e6-78d8-4bc9-8717-845e392dc967_2038x1743.png

An example implementation would follow these steps:

1. As we continue interacting with the agent, the performed actions are written to some kind of storage possibly capable of semantic retrieval (similarity search is optional and in some cases regular databases might do the trick). In the example diagram we see Vector Database being used as we continuously embed the actions using an LLM.

2. Occasionally, when needed we retrieve historic interactions that could enrich the short term context from episodic memory.

3. This additional context is stored as part of the system prompt in short-term (working) memory and can be used by the agent to plan its next steps.

#### Semantic memory.

In the paper that was linked at the beginning of long-term memory section - semantic memory is described as:

- Any external information that is available to the agent.

- Any knowledge the agent should have about itself.

In my initial description of the agent I described a knowledge element. It represents part of the semantic memory. Compared to episodic memory the system looks very similar to RAG, including the fact that we source information to be retrieved from external sources.

https://substackcdn.com/image/fetch/$s_!PvWW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24c121fd-be9e-4494-a6f9-f397284eca23_2040x1726.png

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
<summary>Memory: The secret sauce of AI agents</summary>

# Memory: The secret sauce of AI agents

**Source URL:** <https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents>

Designing a robust memory layer for your agents is one of the most underrated aspects of building AI applications. Memory sits at the core of any AI project, guiding how you implement your RAG (or agentic RAG) algorithm, how you access external information used as context, manage multiple conversation threads, and handle multiple users. All critical aspects of any successful agentic application.

Every agent has short-term memory and some level of long-term memory. Understanding the difference between the two and what types of long-term memory exist is essential to knowing what to adopt in your toolbelt and how to design your AI application system and business logic.

## 1. Short-term vs. long-term memory

AI memory systems can be broadly categorized into two main types: short-term and long-term.

Figure 2: Short-term vs. long-term memory

#### Short-term memory (or working memory)

Short-term memory, often called working memory, is the temporary storage space where an agent holds information it's currently using. This memory typically maintains active information like the current conversation context, recent messages, and intermediate reasoning steps.

Working memory is essential for agents to maintain coherence in conversations. Without it, your agent would respond to each message as if it were the first one, losing all the context and creating a frustrating user experience. The main limitation of working memory is its capacity - it can only hold a limited amount of information at once. In language models, this is directly related to the context window, which determines how much previous conversation and metadata the model can "see" when generating a response.

When implementing working memory in your agent, you need to decide what information to keep and what to discard. Most agents keep the most recent parts of a conversation, but more sophisticated approaches might prioritize keeping important information while summarizing or removing less critical details. This helps make the most efficient use of the limited working memory space.

#### Long-term memory: Semantic memory

Semantic memory stores factual knowledge and general information about the world. It's where your agent keeps the knowledge it has learned that isn't tied to specific experiences. This includes concepts, facts, ideas, and meanings that help the agent understand the world.

For AI assistants, semantic memory might include information about different topics, how to respond to certain types of questions, or facts about the world. This is what enables your agent to answer questions like "What's the capital of France?" or understand the concept of a vacation without needing to have experienced one.

In practice, semantic memory in AI systems is often implemented through vector databases that store information in a way that can be quickly searched and retrieved. When a user asks a question, the agent can search its semantic memory for relevant information to respond accurately.

#### Long-term memory: Procedural memory

Procedural memory contains knowledge about how to do things, such as performing tasks or following specific processes.

When building agents, procedural memory often takes the form of functions, algorithms, or code that defines how the agent should act in different situations. This could be as simple as a template for greeting users or as complex as a multi-step reasoning process for solving tough problems. Unlike semantic memory, which stores what the agent knows, procedural memory stores how the agent applies that knowledge.

#### Long-term memory: Episodic memory

Episodic memory stores specific past experiences and events. In humans, these are our autobiographical memories - the things that happened to us at particular times and places. For AI agents, episodic memory allows them to remember past user interactions and learn from those experiences.

With episodic memory, your agent can recall previous conversations with a specific user, remember preferences they've expressed, or reference shared experiences. This creates a sense of continuity and personalization, making interactions feel more natural and helpful. When a user says, "Let's continue where we left off yesterday," an agent with episodic memory can do that.

Implementing episodic memory typically involves implementing a RAG-like system on top of your conversation histories. Like this, you can move your short-term memory into the long-term memory, extracting only chunks of past conversation that are helpful to answer present queries (instead of keeping the whole history in the context window).

When implementing AI agents, you always have short-term memory. Depending on your use case, you have one or more types of long-term memory, where the procedural and semantic ones are the most common.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="cognitive-architectures-for-language-agents.md">
<details>
<summary>Cognitive Architectures for Language Agents</summary>

Phase: [EXPLOITATION]

# Cognitive Architectures for Language Agents

**Source URL:** <https://arxiv.org/html/2309.02427>

## Abstract

Recent efforts have augmented large language models (LLMs) with external resources (e.g., the Internet) or internal control flows (e.g., prompt chaining) for tasks requiring grounding or reasoning, leading to a new class of language agents. While these agents have achieved substantial empirical success, we lack a framework to organize existing agents and plan future developments.

In this paper, we draw on the rich history of cognitive science and symbolic artificial intelligence to propose Cognitive Architectures for Language Agents (CoALA). CoALA describes a language agent with modular memory components, a structured action space to interact with internal memory and external environments, and a generalized decision-making process to choose actions.

We use CoALA to retrospectively survey and organize a large body of recent work, and prospectively identify actionable directions towards more capable agents. Taken together, CoALA contextualizes today’s language agents within the broader history of AI and outlines a path towards language-based general intelligence.

## 1 Introduction

_Language agents_ are an emerging class of artificial intelligence (AI) systems that use large language models (LLMs) to interact with the world. They apply the latest advances in LLMs to the existing field of agent design. Intriguingly, this synthesis offers benefits for both fields. On one hand, LLMs possess limited knowledge and reasoning capabilities. Language agents mitigate these issues by connecting LLMs to internal memory and environments, grounding them to existing knowledge or external observations. On the other hand, traditional agents often require handcrafted rules or reinforcement learning, making generalization to new environments challenging. Language agents leverage commonsense priors present in LLMs to adapt to novel tasks, reducing the dependence on human annotation or trial-and-error learning.

While the earliest agents used LLMs to directly select or generate actions, more recent agents additionally use them to reason, plan, and manage long-term memory to improve decision-making. This latest generation of _cognitive_ language agents use remarkably sophisticated internal processes (Figure 1C). Today, however, individual works use custom terminology to describe these processes (such as ‘tool use’, ‘grounding’, ‘actions’), making it difficult to compare different agents, understand how they are evolving over time, or build new agents with clean and consistent abstractions.

In order to establish a conceptual framework organizing these efforts, we draw parallels with two ideas from the history of computing and artificial intelligence (AI): production systems and cognitive architectures. Production systems generate a set of outcomes by iteratively applying rules. They originated as string manipulation systems – an analog of the problem that LLMs solve – and were subsequently adopted by the AI community to define systems capable of complex, hierarchically structured behaviors. To do so, they were incorporated into cognitive architectures that specified control flow for selecting, applying, and even generating new productions. We suggest a meaningful analogy between production systems and LLMs: just as productions indicate possible ways to modify strings, LLMs define a distribution over changes or additions to text. This further suggests that controls from cognitive architectures used with production systems might be equally applicable to transform LLMs into language agents.

**Figure 1: Different uses of large language models (LLMs).** A: In natural language processing (NLP), an LLM takes text as input and outputs text. B: *Language agents* place the LLM in a direct feedback loop with the external environment by transforming observations into text and using the LLM to choose actions. C: *Cognitive* language agents additionally use the LLM to manage the agent’s internal state via processes such as learning and reasoning. In this work, we propose a blueprint to structure such agents.

Thus, we propose Cognitive Architectures for Language Agents (CoALA), a conceptual framework to characterize and design general purpose language agents. CoALA organizes agents along three key dimensions: their information storage (divided into working and long-term memories); their action space (divided into internal and external actions); and their decision-making procedure (which is structured as an interactive loop with planning and execution). Through these three concepts (memory, action, and decision-making), we show CoALA can neatly express a large body of existing agents and identify underexplored directions to develop new ones. Notably, while several recent papers propose conceptual architectures for general intelligence or empirically survey language models and agents, this paper combines elements of both: we propose a theoretical framework *and* use it to organize diverse empirical work. This grounds our theory to existing practices and allows us to identify both short-term and long-term directions for future work.

The plan for the rest of the paper is as follows. We first introduce production systems and cognitive architectures (Section 2) and show how these recent developments in LLMs and language agents recapitulate these historical ideas (Section 3). Motivated by these parallels, Section 4 introduces the CoALA framework and uses it to survey existing language agents. Section 5 provides a deeper case study of several prominent agents. Section 6 suggests actionable steps to construct future language agents, while Section 7 highlights open questions in the broader arc of cognitive science and AI. Finally, Section 8 concludes. Readers interested in applied agent design may prioritize Sections 4-6.

## 2 Background: From Strings to Symbolic AGI

We first introduce production systems and cognitive architectures, providing a historical perspective on cognitive science and artificial intelligence: beginning with theories of logic and computation, and ending with attempts to build symbolic artificial general intelligence. We then briefly introduce language models and language agents. Section 3 will connect these ideas, drawing parallels between production systems and language models.

### 2.1 Production systems for string manipulation

In the first half of the twentieth century, a significant line of intellectual work led to the reduction of mathematics and computation to symbolic manipulation. Production systems are one such formalism. Intuitively, production systems consist of a set of rules, each specifying a precondition and an action. When the precondition is met, the action can be taken. The idea originates in efforts to characterize the limits of computation. Post proposed thinking about arbitrary logical systems in these terms, where formulas are expressed as strings and the conclusions they license are identified by production rules (as one string “produces” another). This formulation was subsequently shown to be equivalent to a simpler string rewriting system. In such a system, we specify rules of the form

$$ X\,Y\,Z \rightarrow X\,W\,Z $$

indicating that the string $XYZ$ can be rewritten to the string $XWZ$. String rewriting plays a significant role in the theory of formal languages, in the form of Chomsky’s phrase structure grammar.

### 2.2 Control flow: From strings to algorithms

By itself, a production system simply characterizes the set of strings that can be generated from a starting point. However, they can be used to specify algorithms if we impose _control flow_ to determine which productions are executed. For example, Markov algorithms are production systems with a priority ordering. The following algorithm implements division-with-remainder by converting a number written as strokes $|$ into the form $Q \times R$, where $Q$ is the quotient of division by 5 and $R$ is the remainder:

\[
\begin{array}{rcl}
\displaystyle *||||| & \displaystyle \rightarrow & \displaystyle |* \\
\displaystyle * & \displaystyle \xrightarrow{\bullet} & \displaystyle * \\
\displaystyle * & \displaystyle \rightarrow & \displaystyle *
\end{array}
\]

where the priority order runs from top to bottom, productions are applied to the first substring matching their preconditions when moving from left to right (including the empty substring, in the last production), and $\xrightarrow{\bullet}$ indicates the algorithm halts after executing the rule. The first rule effectively “subtracts” five if possible; the second handles the termination condition when no more subtraction is possible; and the third handles the empty substring input case. For example, given the input 11, this would yield the sequence of productions $*||||||||||| \rightarrow |*||||||\rightarrow ||*|\xrightarrow{\bullet}||*|$ which is interpreted as 2 remainder 1. Simple productions can result in complex behavior – Markov algorithms can be shown to be Turing complete.

### 2.3 Cognitive architectures: From algorithms to agents

Production systems were popularized in the AI community by Allen Newell, who was looking for a formalism to capture human problem solving. Productions were generalized beyond string rewriting to logical operations: _preconditions_ that could be checked against the agent’s goals and world state, and _actions_ that should be taken if the preconditions were satisfied. In their landmark book Human Problem Solving, Allen Newell and Herbert Simon gave the example of a simple production system implementing a thermostat agent:

\[
\begin{array}{rcl}
\displaystyle (\mbox{temperature}>70^{\circ})\wedge(\mbox{temperature}<72^{ \circ}) & \displaystyle \rightarrow & \mbox{stop} \\
\displaystyle \mbox{temperature}<32^{\circ} & \displaystyle \rightarrow & \mbox{call for repairs; turn on electric heater} \\
\displaystyle (\mbox{temperature}<70^{\circ})\wedge\mbox{(furnace off)} & \displaystyle \rightarrow & \mbox{turn on furnace} \\
\displaystyle (\mbox{temperature}>72^{\circ})\wedge\mbox{(furnace on)} & \displaystyle \rightarrow & \mbox{turn off furnace}
\end{array}
\]

Following this work, production systems were adopted by the AI community. The resulting agents contained large production systems connected to external sensors, actuators, and knowledge bases – requiring correspondingly sophisticated control flow. AI researchers defined “cognitive architectures” that mimicked human cognition – explicitly instantiating processes such as perception, memory, and planning to achieve flexible, rational, real-time behaviors. This led to applications from psychological modeling to robotics, with hundreds of architectures and thousands of publications (see for a recent survey).

A canonical example is the Soar architecture (Figure 2A). Soar stores productions in long-term memory and executes them based on how well their preconditions match working memory (Figure 2B). These productions specify actions that modify the contents of working and long-term memory. We next provide a brief overview of Soar and refer readers to for deeper introductions.

Memory. Building on psychological theories, Soar uses several types of memory to track the agent’s state. _Working memory_ reflects the agent’s current circumstances: it stores the agent’s recent perceptual input, goals, and results from intermediate, internal reasoning. _Long term memory_ is divided into three distinct types. _Procedural_ memory stores the production system itself: the set of rules that can be applied to working memory to determine the agent’s behavior. _Semantic_ memory stores facts about the world, while _episodic_ memory stores sequences of the agent’s past behaviors.

**Figure 2: Cognitive architectures augment a production system with sensory groundings, long-term memory, and a decision procedure for selecting actions.** A: The Soar architecture, reproduced with permission from Laird et al. (2017). B: Soar’s decision procedure uses productions to select and implement actions. These actions may be *internal* (such as modifying the agent’s memory) or *external* (such as a motor command).

Grounding. Soar can be instantiated in simulations or real-world robotic systems. In embodied contexts, a variety of sensors stream perceptual input into working memory, where it is available for decision-making. Soar agents can also be equipped with actuators, allowing for physical actions and interactive learning via language.

Decision making. Soar implements a decision loop that evaluates productions and applies the one that matches best (Figure 2B). Productions are stored in long-term procedural memory. During each decision cycle, their preconditions are checked against the agent’s working memory. In the _proposal and evaluation_ phase, a set of productions is used to generate and rank a candidate set of possible actions. (In more detail, Soar divides productions into two types: “operators,” which we refer to as actions, and “rules” which are used to propose, evaluate, and execute operators.) The best action is then chosen. (If no actions are valid, or multiple actions tie, then an _impasse_ occurs. Soar creates a subgoal to resolve the impasse, resulting in hierarchical task decomposition. We refer the reader to Laird et al. (2017) for a more detailed discussion.) Another set of productions is then used to implement the action – for example, modifying the contents of working memory or issuing a motor command.

Learning. Soar supports multiple modes of learning. First, new information can be stored directly in long-term memory: facts can be written to semantic memory, while experiences can be written to episodic memory. This information can later be retrieved back into working memory when needed for decision-making. Second, behaviors can be modified. Reinforcement learning can be used to up-weight productions that have yielded good outcomes, allowing the agent to learn from experience. Most remarkably, Soar is also capable of writing new productions into its procedural memory – effectively updating its source code.

Cognitive architectures were used broadly across psychology and computer science, with applications including robotics, military simulations, and intelligent tutoring. Yet they have become less popular in the AI community over the last few decades. This decrease in popularity reflects two of the challenges involved in such systems: they are limited to domains that can be described by logical predicates and require many pre-specified rules to function.

Intriguingly, LLMs appear well-posed to meet these challenges. First, they operate over arbitrary text, making them more flexible than logic-based systems. Second, rather than requiring the user to specify productions, they learn a distribution over productions via pre-training on an internet corpus. Recognizing this, researchers have begun to use LLMs within cognitive architectures, leveraging their implicit world knowledge to augment traditional symbolic approaches. Here, we instead import principles from cognitive architecture to guide the design of LLM-based agents.

### 2.4 Language models and agents

Language modeling is a decades-old endeavor in the NLP and AI communities, aiming to develop systems that can generate text given some context. Formally, language models learn a distribution $P(w_{i}|w_{<i})$, where each $w$ is an individual token (word). This model can then generate text by sampling from the distribution, one token at a time. At its core, a language model is a probabilistic input-output system, since there are inherently several ways to continue a text (e.g., “I went to the” $\rightarrow$ “market” | “beach” | …). While earlier attempts at modeling language (e.g., n-grams) faced challenges in generalization and scaling, there has been a recent resurgence of the area due to the rise of Transformer-based LLMs with a large number (billions) of parameters and smart tokenization schemes. Modern LLMs are trained on enormous amounts of data, which helps them accumulate knowledge from a large number of input-output combinations and successfully generate human-like text.

Unexpectedly, training these models on internet-scale text also made them useful for many tasks beyond generating text, such as writing code, modeling proteins, and acting in interactive environments. The latter has led to the rise of “language agents” – systems that use LLMs as a core computation unit to reason, plan, and act – with applications in areas such as robotics, manufacturing, web manipulation, puzzle solving and interactive code generation. The combination of language understanding and decision-making capabilities is an exciting and emerging direction that promises to bring these agents closer to human-like intelligence.

## 3 Connections between Language Models and Production Systems

Based on their common origins in processing strings, there is a natural analogy between production systems and language models. We develop this analogy, then show that prompting methods recapitulate the algorithms and agents based on production systems. The correspondence between production systems and language models motivates our use of cognitive architectures to build language agents, which we introduce in Section 4.

### 3.1 Language models as probabilistic production systems

In their original instantiation, production systems specified the set of strings that could be generated from a starting point, breaking this process down into a series of string rewriting operations. Language models also define a possible set of expansions or modifications of a string – the prompt provided to the model. (In this work, we focus on autoregressive LLMs which are typically used for language agents. However, bidirectional LLMs such as BERT can be seen in a similar light: they define a distribution over _in-filling_ productions.)

For example, we can formulate the problem of completing a piece of text as a production. If $X$ is the prompt and $Y$ the continuation, then we can write this as the production $X \rightarrow X \, Y$. (Alternatively, we can treat the prompt as input and take the output of the LLM as the next state, represented by the production $X \rightarrow Y$ – a more literal form of rewriting.) We might want to allow multiple possible continuations, in which case we have $X \rightarrow X \, Y_i$ for some set of $Y_i$. LLMs assign a _probability_ to each of these completions. Viewed from this perspective, the LLM defines a probability distribution over _which productions to select_ when presented with input $X$, yielding a distribution $P(Y_i|X)$ over possible completions. LLMs can thus be viewed as probabilistic production systems that sample a possible completion each time they are called, e.g., $X \leadsto X\,Y$.

This probabilistic form offers both advantages and disadvantages compared to traditional production systems. The primary disadvantage of LLMs is their inherent opaqueness: while production systems are defined by discrete and human-legible rules, LLMs consist of billions of uninterpretable parameters. This opaqueness – coupled with inherent randomness from their probabilistic formulation – makes it challenging to analyze or control their behaviors. Nonetheless, their scale and pre-training provide massive advantages over traditional production systems. LLMs pre-trained on large-scale internet data learn a remarkably effective prior over string completions, allowing them to solve a wide range of tasks out of the box.

### 3.2 Prompt engineering as control flow

The weights of an LLM define a prioritization over output strings (completions), conditioned by the input string (the prompt). The resulting distribution can be interpreted as a task-specific prioritization of productions – in other words, a simple control flow. Tasks such as question answering can be formulated directly as an input string (the question), yielding conditional distributions over completions (possible answers).

**Table 1: Conceptual diagram illustrating how prompting methods manipulate the input string before generating completions.** $Q$ = question, $A$ = answer, $O$ = observation, $C$ = critique, and $\stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}}$ denotes sampling from a stochastic production. These pre-processing manipulations – which can employ other models such as vision-language models (VLMs), or even the LLM itself – can be seen as productions. Prompting methods thus define a _sequence_ of productions.

| Prompting Method          | Production Sequence                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zero-shot                 | $Q \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q\,A$                                                                                                                                                                      |
| Few-shot                  | $Q \rightarrow Q_1\,A_1\,Q_2\,A_2\,Q \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q_1\,A_1\,Q_2\,A_2\,Q\,A$                                                                                                              |
| Retrieval Augmented Generation | $Q \xrightarrow{\text{Wiki}} Q\,O \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q\,O\,A$                                                                                                                            |
| Socratic Models           | $Q \stackon[1pt]{\sim}{\scriptscriptstyle\text{VLM}} Q\,O \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q\,O\,A$                                                                                                         |
| Self-Critique             | $Q \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q\,A \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q\,A\,C \stackon[1pt]{\sim}{\scriptscriptstyle\text{LLM}} Q\,A\,C\,A$                                            |

Early work on few-shot learning and prompt engineering found that the LLM could be further biased towards high-quality productions by pre-processing the input string. These simple manipulations – typically concatenating additional text to the input – can themselves be seen as productions, meaning that these methods define a sequence of productions (Table 1). Later work extended these approaches to dynamic, context-sensitive prompts: for example, selecting few-shot examples that are maximally relevant to the input or populating a template with external observations from video or databases. For a survey of such prompting techniques, see Liu et al. (2023).

Subsequent work used the LLM itself as a pre-processing step, eliciting targeted reasoning to foreground a particular aspect of the problem or generate intermediate reasoning steps before returning an answer. _Chaining_ multiple calls to an LLM allows for increasingly complicated algorithms (Figure 3).

**Figure 3: From language models to language agents.** A: Basic structure of an LLM call. Prompt construction selects a template and populates it with variables from working memory. After calling the LLM, the string output is parsed into an action space and executed. An LLM call may result in one or more actions – for example, returning an answer, calling a function, or issuing motor commands. B: *Prompt chaining* techniques such as Self-Critique or Selection-Inference use a pre-defined sequence of LLM calls to generate an output. C: *Language agents* such as Inner Monologue and ReAct instead use an interactive feedback loop with the external environment. Vision-language models (VLMs) can be used to translate perceptual data into text for the LLM to process.

### 3.3 Towards cognitive language agents

_Language agents_ move beyond pre-defined prompt chains and instead place the LLM in a feedback loop with the external environment (Figure 1B). These approaches first transform multimodal input into text and pass it to the LLM. The LLM’s output is then parsed and used to determine an external action (Figure 3C). Early agents interfaced the LLM directly with the external environment, using it to produce high-level instructions based on the agent’s state. Later work developed more sophisticated language agents that use the LLM to perform intermediate reasoning before selecting an action. The most recent agents incorporate sophisticated learning strategies such as reflecting on episodic memory to generate new semantic inferences or modifying their program code to generate procedural knowledge, using their previous experience to adapt their future behaviors.

These _cognitive_ language agents employ nontrivial LLM-based reasoning and learning (Figure 1C). Just as cognitive architectures were used to structure production systems’ interactions with agents’ internal state and external environments, we suggest that they can help design LLM-based cognitive agents. In the remainder of the paper, we use this perspective to organize existing approaches and highlight promising extensions.

**Figure 4: Cognitive architectures for language agents (CoALA).** A: CoALA defines a set of interacting modules and processes. The decision procedure executes the agent’s source code. This source code consists of procedures to interact with the LLM (prompt templates and parsers), internal memories (retrieval and learning), and the external environment (grounding). B: Temporally, the agent’s decision procedure executes a decision cycle in a loop with the external environment. During each cycle, the agent uses retrieval and reasoning to plan by proposing and evaluating candidate learning or grounding actions. The best action is then selected and executed. An observation may be made, and the cycle begins again.

## 4 Cognitive Architectures for Language Agents (CoALA): A Conceptual Framework

We present Cognitive Architectures for Language Agents (CoALA) as a framework to organize existing language agents and guide the development of new ones. CoALA positions the LLM as the core component of a larger cognitive architecture (Figure 4). Under CoALA, a language agent stores information in memory modules (Section 4.1), and acts in an action space structured into external and internal parts (Figure 5):

- External actions interact with external environments (e.g., control a robot, communicate with a human, navigate a website) through grounding (Section 4.2).
- Internal actions interact with internal memories. Depending on which memory gets accessed and whether the access is read or write, internal actions can be further decomposed into three kinds: retrieval (read from long-term memory; Section 4.3), reasoning (update the short-term working memory with LLM; Section 4.4), and learning (write to long-term memory; Section 4.5).

Language agents choose actions via decision-making, which follows a repeated cycle (Section 4.6, Figure 4B). In each cycle, the agent can use reasoning and retrieval actions to plan. This planning subprocess selects a grounding or learning action, which is executed to affect the outside world or the agent’s long-term memory. CoALA’s decision cycle is analogous to a program’s “main” *procedure* (a *method* without return values, as opposed to *functions*) that runs in loops continuously, accepting new perceptual input and calling various action *procedures* in response.

CoALA (Figure 4) is inspired by the decades of research in cognitive architectures (Section 2.3), leveraging key concepts such as memory, grounding, learning, and decision-making. Yet the incorporation of an LLM leads to the addition of “reasoning” actions, which can flexibly produce new knowledge and heuristics for various purposes – replacing hand-written rules in traditional cognitive architectures. It also makes text the *de facto* internal representation, streamlining agents’ memory modules. Finally, recent advances in vision-language models can simplify grounding by providing a straightforward translation of perceptual data into text.

The rest of this section details key concepts in CoALA: memory, actions (grounding, reasoning, retrieval, and learning), and decision-making. For each concept, we use existing language agents (or relevant NLP/RL methods) as examples – or note gaps in the literature for future directions.

### 4.1 Memory

Language models are _stateless_: they do not persist information across calls. In contrast, language agents may store and maintain information internally for multi-step interaction with the world. Under the CoALA framework, language agents explicitly organize information (mainly textural, but other modalities also allowed) into multiple memory modules, each containing a different form of information. These include short-term working memory and several long-term memories: episodic, semantic, and procedural.

Working memory. Working memory maintains active and readily available information as symbolic variables for the current decision cycle (Section 4.6). This includes perceptual inputs, active knowledge (generated by reasoning or retrieved from long-term memory), and other core information carried over from the previous decision cycle (e.g., agent’s active goals). Previous methods encourage the LLM to generate intermediate reasoning, using the LLM’s own context as a form of working memory. CoALA’s notion of working memory is more general: it is a data structure that persists across LLM calls. On each LLM call, the LLM input is synthesized from a subset of working memory (e.g., a prompt template and relevant variables). The LLM output is then parsed back into other variables (e.g., an action name and arguments) which are stored back in working memory and used to execute the corresponding action (Figure 3A). Besides the LLM, the working memory also interacts with long-term memories and grounding interfaces. It thus serves as the central hub connecting different components of a language agent.

**Figure 5: Agents’ action spaces can be divided into internal memory accesses and external interactions with the world.** Reasoning and retrieval actions are used to support planning.

Episodic memory. Episodic memory stores experience from earlier decision cycles. This can consist of training input-output pairs, history event flows, game trajectories from previous episodes, or other representations of the agent’s experiences. During the planning stage of a decision cycle, these episodes may be retrieved into working memory to support reasoning. An agent can also write new experiences from working to episodic memory as a form of learning (Section 4.5).

Semantic memory. Semantic memory stores an agent’s knowledge about the world and itself. Traditional NLP or RL approaches that leverage retrieval for reasoning or decision-making initialize semantic memory from an external database for knowledge support. For example, retrieval-augmented methods in NLP can be viewed as retrieving from a semantic memory of unstructured text (e.g., Wikipedia). In RL, “reading to learn” approaches leverage game manuals and facts as a semantic memory to affect the policy. While these examples essentially employ a fixed, read-only semantic memory, language agents may also write new knowledge obtained from LLM reasoning into semantic memory as a form of learning (Section 4.5) to incrementally build up world knowledge from experience.

Procedural memory. Language agents contain two forms of procedural memory: _implicit_ knowledge stored in the LLM weights, and _explicit_ knowledge written in the agent’s code. The agent’s code can be further divided into two types: procedures that implement actions (reasoning, retrieval, grounding, and learning procedures), and procedures that implement decision-making itself (Section 4.6). During a decision cycle, the LLM can be accessed via reasoning actions, and various code-based procedures can be retrieved and executed. Unlike episodic or semantic memory that may be initially empty or even absent, procedural memory must be initialized by the designer with proper code to bootstrap the agent. Finally, while learning new actions by writing to procedural memory is possible (Section 4.5), it is significantly riskier than writing to episodic or semantic memory, as it can easily introduce bugs or allow an agent to subvert its designers’ intentions.

### 4.2 Grounding actions

Grounding procedures execute external actions and process environmental feedback into working memory as text. This effectively simplifies the agent’s interaction with the outside world as a “text game” with textual observations and actions. We categorize three kinds of external environments:

Physical environments. Physical embodiment is the oldest instantiation envisioned for AI agents. It involves processing perceptual inputs (visual, audio, tactile) into textual observations (e.g., via pre-trained captioning models), and affecting the physical environments via robotic planners that take language-based commands. Recent advances in LLMs have led to numerous robotic projects that leverage LLMs as a “brain” for robots to generate actions or plans in the physical world. For perceptual input, vision-language models are typically used to convert images to text providing additional context for the LLM.

Dialogue with humans or other agents. Classic linguistic interactions allow the agent to accept instructions or learn from people. Agents capable of _generating_ language may ask for help or clarification – or entertain or emotionally help people. Recent work also investigates interaction among multiple language agents for social simulation, debate, improved safety, or collaborative task solving.

Digital environments. This includes interacting with games, APIs, and websites as well as general code execution. Such digital grounding is cheaper and faster than physical or human interaction. It is thus a convenient testbed for language agents and has been studied with increasing intensity in recent years. In particular, for NLP tasks that require augmentation of external knowledge or computation, stateless digital APIs (e.g., search, calculator, translator) are often packaged as “tools”, which can be viewed as special “single-use” digital environments.

### 4.3 Retrieval actions

In CoALA, a retrieval procedure reads information from long-term memories into working memory. Depending on the information and memory type, it could be implemented in various ways, e.g., rule-based, sparse, or dense retrieval. For example, Voyager loads code-based skills from a skill library via dense retrieval to interact with the Minecraft world – effectively retrieving grounding procedures from a procedural memory. Generative Agents retrieves relevant events from episodic memory via a combination of recency (rule-based), importance (reasoning-based), and relevance (embedding-based) scores. DocPrompting proposes to leverage library documents to assist code generation, which can be seen as retrieving knowledge from semantic memory. While retrieval plays a key role in human decision-making, adaptive and context-specific recall remains understudied in language agents. In Section 6, we suggest a principled integration of decision-making and retrieval as an important future direction.

### 4.4 Reasoning actions

Reasoning allows language agents to process the contents of working memory to generate new information. Unlike retrieval (which reads from long-term memory into working memory), reasoning reads from _and_ writes to working memory. This allows the agent to summarize and distill insights about the most recent observation, the most recent trajectory, or information retrieved from long-term memory. Reasoning can be used to support learning (by writing the results into long-term memory) or decision-making (by using the results as additional context for subsequent LLM calls).

### 4.5 Learning actions

Learning occurs by writing information to long-term memory, which includes a spectrum of diverse procedures.

Updating episodic memory with experience. It is common practice for RL agents to store episodic trajectories to update a parametric policy or establish a non-parametric policy. For language agents, added experiences in episodic memory may be retrieved later as examples and bases for reasoning or decision-making.

Updating semantic memory with knowledge. Recent work has applied LLMs to reason about raw experiences and store the resulting inferences in semantic memory. For example, Reflexion uses an LLM to reflect on failed episodes and stores the results (e.g., “there is no dishwasher in kitchen”) as semantic knowledge to be attached to LLM context for solving later episodes. Finally, work in robotics uses vision-language models to build a semantic map of the environment, which can later be queried to execute instructions.

Updating LLM parameters (procedural memory). The LLM weights represent implicit procedural knowledge. These can be adjusted to an agent’s domain by fine-tuning during the agent’s lifetime. Such fine-tuning can be accomplished via supervised or imitation learning, reinforcement learning (RL) from environment feedback, human feedback, or AI feedback. Classic LLM self-improvement methods use an external measure such as consistency to select generations to fine-tune on. In reinforcement learning settings, this can be extended to use environmental feedback instead: for example, XTX periodically fine-tunes a small language model on high-scoring trajectories stored in episodic memory, which serves as a robust “exploitation” policy to reach exploration frontiers in the face of stochasticity. Fine-tuning the agent’s LLM is a costly form of learning; thus, present studies specify learning schedules. However, as training becomes more efficient – or if agents utilize smaller subtask-specific LLMs – it may be possible to allow language agents to autonomously determine when and how to fine-tune their LLMs.

Updating agent code (procedural memory). CoALA allows agents to update their source code, thus modifying the implementation of various procedures. These can be broken down as follows:

- Updating reasoning. For example, APE infers prompt instructions from input-output examples, then uses these instructions as part of the LLM prompt to assist task solving. Such a prompt update can be seen as a form of learning to reason.
- Updating grounding. For example, Voyager maintains a curriculum library. Notably, current methods are limited to creating new code skills to interact with external environments.
- Updating retrieval. To our knowledge, these learning options are not studied in recent language agents. Retrieval is usually considered a basic action designed with some fixed implementation (e.g., BM25 or dense retrieval), but research in query/document expansion or retrieval distillation may be helpful for language agents to learn better retrieval procedures.
- Updating learning or decision-making. Finally, it is theoretically possible for CoALA agents to learn new procedures for learning or decision-making, thus providing significant adaptability. In general, however, updates to these procedures are risky both for the agent’s functionality and alignment. At present, we are not aware of any language agents that implement this form of learning; we discuss such possibilities more in Section 6.

While RL agents usually fix one way of learning (e.g., Q-learning, PPO, or A3C) and learn by updating model parameters, language agents can select from a diversity of learning procedures. This allows them to learn rapidly by storing task-relevant language (cheaper and quicker than parameter updates), and leverage multiple forms of learning to compound their self-improvement (e.g., Generative Agents discussed in Section 5).

Finally, while our discussion has mostly focused on adding to memory, modifying and deleting (a case of “unlearning”) are understudied in recent language agents. We address these areas more in Section 6.

### 4.6 Decision making

With various actions (grounding, learning, reasoning, retrieval) in the action space, how should a language agent choose which action to apply? This is handled by the decision-making procedure, which is effectively the top-level or “main” agent program. CoALA structures this top-level program into decision cycles (Figure 4B) which yield an external _grounding_ action (Section 4.2) or internal _learning_ action (Section 4.5). In each cycle, program code defines a sequence of reasoning and retrieval actions to propose and evaluate alternatives (planning stage), then executes the selected action (execution stage) – then the cycle loops again.

Planning stage. During planning, reasoning and retrieval can be flexibly applied to propose, evaluate, and select actions, and these sub-stages could interleave or iterate to build up multi-step simulations before taking an external action. It also enables agents to iteratively improve candidate solutions – for example, by using the LLM to simulate them, identifying defects, and proposing modifications that address those defects.

- Proposal. The proposal sub-stage generates one or more action candidates. The usual approach is to use reasoning (and optionally retrieval) to sample one or more external grounding actions from the LLM. For simple domains with limited actions, the proposal stage might simply include all actions (e.g., SayCan in Section 5). More sophisticated agents use if-else or while-if code structures; while agents deployed in well-defined domains may utilize structured simulators to generate plausible rollouts.
- Evaluation. If multiple actions are proposed, the evaluation sub-stage assigns a value to each. This may use heuristic rules, LLM (perplexity) values, learned values, LLM reasoning, or some combination. Particularly, LLM reasoning can help evaluate actions by internally simulating their grounding feedback from the external world.
- Selection. Given a set of actions and their values, the selection step either selects one to execute or rejects them and loops back to the proposal step. Depending on the form of action values, selection may occur via argmax, softmax, or an alternative such as majority vote.

Execution. The selected action is applied by executing the relevant procedures from the agent’s source code. Depending on the agent implementation, this might be an external _grounding_ action (e.g., an API call; Section 4.2) or an internal _learning_ action (e.g., a write to episodic memory; Section 4.5). An observation can be made from the environment, providing feedback from the agent’s action, and the cycle loops again.

Empirically, many early language agents simply use LLMs to propose an action, a sequence of actions, or evaluate a fixed set of actions without intermediate reasoning or retrieval. Followup work has exploited intermediate reasoning and retrieval to analyze the situation, make and maintain action plans, refine the previous action given the environmental feedback, and leveraged a more complex procedure to propose a single action. Most recently, research has started to investigate more complex decision-making employing iterative proposal and evaluation to consider multiple actions. These procedures are modeled after classical planning algorithms: for example, Tree of Thoughts and RAP use LLMs to implement BFS/DFS and Monte Carlo Tree Search respectively. LLMs are used to generate proposals (i.e., to simulate rollouts conditioned on an action) and evaluate them (i.e., to value the outcome of the proposed action).

## 5 Case Studies

With variations and ablations of the memory modules, action space, and decision-making procedures, CoALA can express a wide spectrum of language agents. Table 2 lists some popular recent methods across diverse domains — from Minecraft to robotics, from pure reasoning to social simulacra. CoALA helps characterize their internal mechanisms and reveal their similarities and differences in a simple and structured way.

SayCan grounds a language model to robotic interactions in a kitchen to satisfy user commands (e.g., “I just worked out, can you bring me a drink and a snack to recover?”). Its long-term memory is procedural only (an LLM and a learned value function). The action space is external only – a fixed set of 551 grounding skills (e.g., “find the apple”, “go to the table”), with no internal actions of reasoning, retrieval, or learning. During decision-making, SayCan evaluates each action using a combination of LLM and learned values, which balance a skill’s usefulness and groundedness. SayCan therefore employs the LLM (in conjunction with the learned value function) as a single-step planner.

**Table 2: Some recent language agents cast into the CoALA framework.**

|                 | Long-term                     | External   | Internal            | Decision                       |
| :-------------- | :---------------------------- | :--------- | :------------------ | :----------------------------- |
|                 | Memory (All agents contain some procedural memory (agent code and LLM weights), so here we only list writable procedural memory.) | Grounding  | Actions             | Making                         |
| SayCan          | -                             | physical   | -                   | evaluate                       |
| ReAct           | -                             | digital    | reason              | propose                        |
| Voyager         | procedural                    | digital    | reason/retrieve/learn | propose                        |
| Generative Agents | episodic/semantic             | digital/agent | reason/retrieve/learn | propose                        |
| Tree of Thoughts | -                             | digital (Special digital grounding with the only external action being submitting a final answer.) | reason              | propose, evaluate, select      |

ReAct is a language agent grounded to various digital environments (e.g., Wikipedia API, text game, website). Like SayCan, it lacks semantic or episodic memory and therefore has no retrieval or learning actions. Its action space consists of (internal) reasoning and (external) grounding. Its decision cycle is fixed to use a single reasoning action to analyze the situation and (re)make action plans, then generates a grounding action without evaluation or selection stages. ReAct can be considered the simplest language agent that leverages both internal and external actions, and is the initial work that demonstrates their synergizing effects: reasoning helps guide acting, while acting provides environmental feedback to support reasoning.

Voyager is a language agent grounded to the Minecraft API. Unlike SayCan, which grounds to perception via the learned value function, Voyager’s grounding is text-only. It has a long-term procedural memory that stores a library of code-based grounding procedures a.k.a. skills (e.g., “combatZombie”, “craftStoneSword”). This library is hierarchical: complex skills can use simpler skills as sub-procedures (e.g., “combatZombie” may call “craftStoneSword” if no sword is in inventory). Most impressively, its action space has all four kinds of actions: grounding, reasoning, retrieval, and learning (by adding new grounding procedures). During a decision cycle, Voyager first reasons to propose a new task objective if it is missing in the working memory, then reasons to propose a code-based grounding procedure to solve the task. In the next decision cycle, Voyager reasons over the environmental feedback to determine task completion. If successful, Voyager selects a learning action adding the grounding procedure to procedural memory; otherwise, it uses reasoning to refine the code and re-executes it. The importance of long-term memory and procedural learning is empirically verified by comparing to baselines like ReAct and AutoGPT and ablations without the procedural memory. Voyager is shown to better explore areas, master the tech tree, and zero-shot generalize to unseen tasks.

Generative Agents are language agents grounded to a sandbox game affording interaction with the environment and other agents. Its action space also has all four kinds of actions: grounding, reasoning, retrieval, and learning. Each agent has a long-term episodic memory that stores events in a list. These agents use retrieval and reasoning to generate reflections on their episodic memory (e.g., “I like to ski now.”) which are then written to long-term semantic memory. During decision-making, it retrieves relevant reflections from semantic memory, then reasons to make a high-level plan of the day. While executing the plan, the agent receives a stream of grounding observations; it can reason over these to maintain or adjust the plan.

Tree of Thoughts (ToT) can be seen as a special kind of language agent with only one external action: submitting a final solution to a reasoning problem (game of 24, creative writing, crosswords puzzle). It has no long-term memory, and only reasoning in its internal action space, but differs from all previous agents in its deliberate decision-making. During planning, ToT iteratively proposes, evaluates, and selects “thoughts” (reasoning actions) based on LLM reasoning, and maintains them via a tree search algorithm to enable global exploration as well as local backtrack and foresight.

## 6 Actionable Insights

Compared to some recent empirical surveys around language agents, CoALA offers a theoretical framework grounded in the well-established research of cognitive architectures. This leads to a unique and complementary set of actionable insights.

Modular agents: thinking beyond monoliths. Perhaps our most important suggestion is that *agents should be structured and modular*. Practically, just as standardized software is used across robotics platforms, a framework for language agents would consolidate technical investment and improve compatibility.

- In academic research, standardized terms allow conceptual comparisons across works (Table 2), and open-source implementations would further facilitate modular plug-and-play and re-use. For example, the theoretical framework of Markov Decision Processes provides a standardized set of concepts and terminology (e.g., state, action, reward, transition) for reinforcement learning. Correspondingly, empirical frameworks like OpenAI Gym provided standardized abstractions (e.g., `obs, reward, done, info = env.step(action)`) that facilitate empirical RL work. Thus, it would be timely and impactful to also implement useful abstractions (e.g., `Memory`, `Action`, `Agent` classes) for language agents, and cast simpler agents into such an empirical CoALA framework as examples for building more complex agents.
- In industry applications, maintaining a single company-wide “language agent library” would reduce technical debt by facilitating testing and component re-use across individual agent deployments. It could also standardize the customer experience: rather than interacting with a hodgepodge of language agents developed by individual teams, end users would experience a context-specific instantiation of the same base agent.
- LLMs vs. code in agent design. CoALA agents possess two forms of procedural memory: agent code (deterministic rules) and LLM parameters (a large, stochastic production system). Agent code is interpretable and extensible, but often brittle in face of stochasticity and limited to address situations the designer anticipates. In contrast, LLM parameters are hard to interpret, but offer significant zero-shot flexibility in new contexts. CoALA thus suggests using code sparingly to implement generic algorithms that complement LLM limitations, e.g., implementing tree search to mitigate myopia induced by autoregressive generation.

Agent design: thinking beyond simple reasoning. CoALA defines agents over three distinct concepts: (i) internal memory, (ii) a set of possible internal and external actions, and (iii) a decision making procedure over those actions. Using CoALA to develop an application-specific agent consists of specifying implementations for each of these components in turn. We assume that the agent’s environment and external action space are given, and show how CoALA can be used to determine an appropriate high-level architecture. For example, we can imagine designing a personalized retail assistant that helps users find relevant items based on their queries and purchasing history. In this case, the external actions would consist of dialogue or returning search results to the user.

- Determine what memory modules are necessary. In our retail assistant example, it would be helpful for the agent to have semantic memory containing the set of items for sale, as well as episodic memory about each customer’s previous purchases and interactions. It will need procedural memory defining functions to query these datastores, as well as working memory to track the dialogue state.
- Define the agent’s internal action space. This consists primarily of defining read and write access to each of the agent’s memory modules. In our example, the agent should have read and write access to episodic memory (so it can store new interactions with customers), but read-only access to semantic and procedural memory (since it should not update the inventory or its own code).
- Define the decision-making procedure. This step specifies how reasoning and retrieval actions are taken in order to choose an external or learning action. In general, this requires a tradeoff between performance and generalization: more complex procedures can better fit to a particular problem (e.g., Voyager for Minecraft) while simpler ones are more domain-agnostic and generalizable (e.g., ReAct). For our retail assistant, we may want to encourage retrieval of episodic memory of interactions with a user to provide a prior over their search intent, as well as an explicit evaluation step reasoning about whether a particular set of search results will satisfy that intent. We can simplify the decision procedure by deferring learning to the end of the interaction, summarizing the episode prior to storing it in episodic memory.

Structured reasoning: thinking beyond prompt engineering. Early work on prompt engineering manipulated the LLM’s input and output via low-level string operations. CoALA suggests a more structured reasoning procedure to update working memory variables.

- Prompting frameworks like LangChain and LlamaIndex can be used to define higher-level sequences of reasoning steps, reducing the burden of reasoning per LLM call and the low-level prompt crafting efforts. Structural output parsing solutions such as Guidance and OpenAI function calling can help update working memory variables. Defining and building good working memory modules will also be an important direction of future research. Such modules may be especially important for industry solutions where LLM reasoning needs to seamlessly integrate with large-scale code infrastructure.
- Reasoning usecases in agents can inform and reshape LLM training in terms of the types (e.g., reasoning for self-evaluation, reflection, action generation, etc.) and formats (e.g., CoT, ReAct, Reflexion) of training instances. By default, existing LLMs are trained and optimized for NLP tasks, but agent applications have explored new modes of LLM reasoning (e.g., self-evaluation) that have proven broadly useful. LLMs trained or finetuned towards these capabilities will more likely be the backbones of future agents.

Long-term memory: thinking beyond retrieval augmentation. While traditional retrieval-augmented language models only read from human-written corpora, memory-augmented language agents can both read and write self-generated content autonomously. This opens up numerous possibilities for efficient lifelong learning.

- Combining existing human knowledge with new experience and skills can help agents bootstrap to learn efficiently. For example, a code-writing agent could be endowed with semantic programming knowledge in the form of manuals or textbooks. It could then generate its own episodic knowledge from experience; reflect on these experiences to generate new semantic knowledge; and gradually create procedural knowledge in the form of a code library storing useful methods.
- Integrating retrieval and reasoning can help to better ground planning. Recent computational psychological models implicate an integrated process of memory recall and decision-making – suggesting that adaptive mechanisms interleaving memory search and forward simulation will allow agents to make the most of their knowledge.

Learning: thinking beyond in-context learning or finetuning. CoALA’s definition of “learning” encompasses these methods, but extends further to storing new experience or knowledge, or writing new agent code (Section 4.5). Important future directions include:

- Meta-learning by modifying agent code would allow agents to learn more effectively. For example, learning better retrieval procedures could enable agents to make better use of their experience. Recent expansion-based techniques could allow agents to reason about when certain knowledge would be useful, and store this as metadata to facilitate later recall. These forms of meta-learning would enable agents to go beyond human-written code, yet are understudied due to their difficulty and risk.
- New forms of learning (and unlearning) could include fine-tuning smaller models for specific reasoning sub-tasks, deleting unneeded memory items for “unlearning”, and studying the interaction effects between multiple forms of learning.

Action space: thinking beyond external tools or actions. Although “action space” is a standard term in reinforcement learning, it has been used sparingly with language agents. CoALA argues for defining a clear and task-suitable action space with both internal (reasoning, retrieval, learning) and external (grounding) actions, which will help systematize and inform the agent design.

- Size of the action space. More capable agents (e.g., Voyager, Generative Agents) have larger action spaces – which in turn means they face a more complex decision-making problem. As a result, these agents rely on more customized or hand-crafted decision procedures. The tradeoff of the action space vs. decision-making complexities is a basic problem to be considered before agent development, and taking the minimal action space necessary to solve a given task might be preferred.
- Safety of the action space. Some parts of the action space are inherently riskier. “Learning” actions (especially procedural deletion and modification) could cause internal harm, while “grounding” actions (e.g., “rm” in bash terminal, harmful speech in human dialog, holding a knife in physical environments) could cause external harm. Today, safety measures are typically task-specific heuristics (e.g., remove “os” operations in Python, filter keywords in dialog, limit robots to controlled environments). However, as agents are grounded to more complex environments with richer internal mechanisms, it may be necessary to specify and ablate the agent’s action space for worst-case scenario prediction and prevention.

Decision making: thinking beyond action generation. We believe one of the most exciting future directions for language agents is decision-making: as detailed in Section 4.6, most works are still confined to proposing (or directly generating) a single action. Present agents have just scratched the surface of more deliberate, propose-evaluate-select decision-making procedures.

- Mixing language-based reasoning and code-based planning may offer the best of both worlds. Existing approaches either plan directly in natural language or use LLMs to translate from natural language to structured world models. Future work could integrate these: just as Soar incorporates a simulator for physical reasoning, agents may write and execute simulation code on the fly to evaluate the consequences of plans. See Section 7 for more discussion.
- Extending deliberative reasoning to real-world settings. Initial works have implemented classical planning and tree search, using toy tasks such as game of 24 or block building. Extending these schemes to more complicated tasks with grounding and long-term memory is an exciting direction.
- Metareasoning to improve efficiency. LLM calls are both slow and computationally intensive. Using LLMs for decision-making entails a balance between their computational cost and the utility of the resulting improved plan. Most LLM reasoning methods fix a search budget by specifying a depth of reasoning, but humans appear to adaptively allocate computation. Future work should develop mechanisms to estimate the utility of planning and modify the decision procedure accordingly, either via amortization, routing among several decision sub-procedures (e.g., ReAct investigated backing off to CoT and vice versa), or updates to the decision-making procedure.
- Calibration and alignment. More complex decision-making is currently bottlenecked by issues such as over-confidence and miscalibration, misalignment with human values or bias, hallucinations in self-evaluation, and lack of human-in-the-loop mechanisms in face of uncertainties. Solving these issues will significantly improve LLMs’ utilities as agent backbones.

## 7 Discussion

In addition to the practical insights presented above, CoALA raises a number of open conceptual questions. We briefly highlight the most interesting as important directions for future research and debate.

LLMs vs VLMs: should reasoning be language-only or multimodal? Most language agents use language-only models for decision-making, employing a separate captioning model to convert environment observations to text when necessary. However, the latest generation of language models are multimodal, allowing interleaved image and text input. Language agents built on such multimodal models natively reason over both image and text input, allowing them to ingest perceptual data and directly produce actions. This bypasses the lossy image-to-text conversion; however, it also tightly couples the reasoning and planning process to the model’s input modalities.

At a high level, the two approaches can be seen as different tokenization schemes to convert non-linguistic modalities into the core reasoning model’s language domain. The modular approach uses a separate image-to-text model to convert perceptual data into language, while the integrated approach projects images directly into the language model’s representation space. Integrated, multimodal reasoning may allow for more human-like behaviors: a VLM-based agent could “see” a webpage, whereas a LLM-based agent would more likely be given raw HTML. However, coupling the agent’s perception and reasoning systems makes the agent more domain-specific and difficult to update. In either case, the basic architectural principles described by CoALA — internal memories, a structured action space, and generalized decision-making — can be used to guide agent design.

Internal vs. external: what is the boundary between an agent and its environment? While humans or robots are clearly distinct from their embodied environment, digital language agents have less clear boundaries. For example, is a Wikipedia database an internal semantic memory or an external digital environment? If an agent iteratively executes and improves code before submitting an answer, is the code execution internal or external? If a method consists of proposal and evaluation prompts, should it be considered a single agent or two collaborating simpler agents (proposer and evaluator)?

We suggest the boundary question can be answered in terms of _controllability_ and _coupling_. For example, Wikipedia is not _controllable_: it is an external environment that may be unexpectedly modified by other users. However, an offline version that only the agent may write to _is_ controllable, and thus can be considered an internal memory. Similarly, code execution on an internal virtual environment should be considered an internal reasoning action, whereas code execution on an external machine (which may possess security vulnerabilities) should be considered an external grounding action. Lastly, if aspects of the agent – such as proposal and evaluation prompts – are designed for and dependent on each other, then they are _tightly coupled_ and best conceptualized as components in an individual agent. In contrast, if the steps are independently useful, a multi-agent perspective may be more appropriate. While these dilemmas are primarily conceptual, such understanding can support agent design and help the field align on shared terminology. Practitioners may also just choose their preferred framing, as long as it is consistent and useful for their own work.

Physical vs. digital: what differences beget attention? While animals only live once in the physical world, digital environments (e.g., the Internet) often allow sequential (via resets) and parallel trials. This means digital agents can more boldly explore (e.g., open a million webpages) and self-clone for parallel task solving (e.g., a million web agents try different web paths), which may result in decision-making procedures different from current ones inspired by human cognition.

Learning vs. acting: how should agents continuously and autonomously learn? In the CoALA framework, learning is a result action of a decision-making cycle just like grounding: the agent deliberately chooses to commit information to long-term memory. This is in contrast to most agents, which simply fix a learning schedule and only use decision making for external actions. Biological agents, however, do not have this luxury: they must balance learning against external actions in their lifetime, choosing when and what to learn. More flexible language agents would follow a similar design and treat learning on par with external actions. Learning could be proposed as a possible action during regular decision-making, allowing the agent to “defer” it until the appropriate time.

GPT-4 vs GPT-N: how would agent design change with more powerful LLMs? Agent design is a moving target as new LLM capabilities emerge with scale. For example, earlier language models such as GPT-2 would not support LLM agents — indeed, work at that time needed to combine GPT-2 with reinforcement learning for action generation; GPT-3 unlocked flexible few-shot and zero-shot reasoning for NLP tasks; while only GPT-4 starts to afford more reliable self-evaluation and self-refinement. Will future LLMs further reduce the need for coded rules and extra-learned models? Will this necessitate changes to the CoALA framework? As a thought experiment, imagine GPT-N could “simulate” memory, grounding, learning, and decision-making in context: list all the possible actions, simulate and evaluate each one, and maintain its entire long-term memory explicitly in a very long context. Or even more boldly: perhaps GPT-N+1 succeeds at generating the next action by simulating these implicitly in neurons, without any intermediate reasoning in context. While these extreme cases seem unlikely in the immediate future, incremental improvements may alter the importance of different CoALA components. For example, a longer context window could reduce the importance of long-term memory, while more powerful reasoning for internal evaluation and simulation could allow longer-horizon planning. In general, LLMs are not subject to biological limitations, and their emergent properties have been difficult to predict. Nonetheless, CoALA – and cognitive science more generally – may still help organize tasks where language agents succeed or fail, and suggest code-based procedures to complement a given LLM on a given task. Even in the most extreme case, where GPT implements all of CoALA’s mechanisms in neurons, it may be helpful to leverage CoALA as a conceptual guide to discover and interpret those implicit circuits. Of course, as discussed in Section 6, agent usecases will also help discover, define and shape LLM capabilities. Similar to how chips and computer architectures have co-evolved, language model and agent design should also develop a reciprocal path forward.

## 8 Conclusion

We proposed Cognitive Architectures for Language Agents (CoALA), a conceptual framework to describe and build language agents. Our framework draws inspiration from the rich history of symbolic artificial intelligence and cognitive science, connecting decades-old insights to frontier research on large language models. We believe this approach provides a path towards developing more general and more human-like artificial intelligence.

## Acknowledgements

We thank Harrison Chase, Baian Chen, Khanh Nguyen, Ofir Press, Noah Shinn, Jens Tuyls for proofreading and valuable feedback, and members from the Princeton NLP Group and Princeton Computational Cognitive Science Lab for helpful discussions. Finally, we thank our anonymous reviewers for insightful comments and suggestions. SY and KN acknowledge support from an Oracle Collaborative Research award and the National Science Foundation under Grant No. 2239363. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. SY is also supported by the Harold W. Dodds Fellowship from Princeton. TS is supported by the National Defense Science and Engineering (NDSEG) Graduate Fellowship Program.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="giving-your-ai-a-mind-exploring-memory-frameworks-for-agenti.md">
<details>
<summary>Giving Your AI a Mind: Exploring Memory Frameworks for Agentic Language Models</summary>

Phase: [EXPLOITATION]

# Giving Your AI a Mind: Exploring Memory Frameworks for Agentic Language Models

**Source URL:** <https://medium.com/@honeyricky1m3/giving-your-ai-a-mind-exploring-memory-frameworks-for-agentic-language-models-c92af355df06>

https://miro.medium.com/v2/resize:fit:687/1*D6GKOFWsHpO6ycPVQM98xQ.png

Langhain Memory for agents

Hey everyone, Richardson Gunde here! Ever feel like you’re having a conversation with a goldfish? You tell it something, it seems to listen… then, poof! It forgets everything the second you finish speaking. That’s often the experience with many chatbots — they lack the crucial ingredient of _memory_. But what if we could give our AI assistants a proper memory, a real mind to hold onto information and learn from past experiences? That’s what we’re diving into today.

This isn’t just about remembering the last few messages; it’s about building truly _agentic_ systems — AI that can learn, adapt, and even anticipate your needs. We’re going to explore different memory frameworks inspired by human cognition, and I’ll show you how to implement them using LangChain and other tools. Get ready for an “Aha!” moment or two — this is where the magic happens.

**The Stateless Nature of Language Models:** _A Fundamental Limitation_

Think about how a language model works. Every time you send a prompt, it’s essentially a brand new start. It’s stateless; it doesn’t inherently remember anything from previous interactions unless you explicitly feed it that context. This is a huge limitation when building agents that need to handle complex tasks or ongoing conversations.

https://miro.medium.com/v2/resize:fit:695/1*OF5rIU6UCdIF1jslIQk0zw.png

Agent Memory — Can LLMs Really Think?

Now, contrast that with how _you_ approach problem-solving. You bring a wealth of knowledge — your general knowledge of the world, memories of past experiences, lessons learned from successes and failures. This allows you to instantly contextualize a situation and adapt your approach accordingly. We, as humans, have something language models currently lack: advanced memory and the ability to learn and apply those learnings to new situations.

**Bridging the Gap:** _Modeling Human Memory in AI_

To overcome this limitation, we can borrow concepts from psychology and model different forms of memory within our agentic system design. We’ll focus on four key types:

1.  **Working Memory:** This is your immediate cognitive workspace, the “RAM” of your mind. For a chatbot, it’s the current conversation and its context. Think of it as the short-term memory of the interaction, keeping track of the back-and-forth between user and AI. Remembering in this context is simply accessing this recent data, while learning involves dynamically integrating new messages to update the overall conversational state.

https://miro.medium.com/v2/resize:fit:480/1*60lIG7SeVeXCc0F1sL7WMQ.png

**2 . Episodic Memory:** This is your long-term memory for specific events. For a chatbot, it’s a collection of past conversations and the takeaways from them. Remembering here involves recalling similar past events and their outcomes to guide current interactions. Learning involves storing complete conversations and analyzing them to extract key insights — what worked, what didn’t, and what to avoid in the future. This is where the AI starts to truly learn from experience.

https://miro.medium.com/v2/resize:fit:505/1*3p0USam0ju55foTCOJPfIQ.png

**3\. Semantic Memory:** This represents your structured knowledge of facts, concepts, and their relationships — the “what you know”. For our agent, this will be a database of factual knowledge that’s dynamically retrieved to ground responses. Learning involves expanding or refining this knowledge base, while remembering involves retrieving and synthesizing relevant information to provide accurate and contextually appropriate answers.

https://miro.medium.com/v2/resize:fit:263/1*5AEUHbncyyknq2J5d4iraQ.png

**4\. Procedural Memory:** This is the “how to” memory, encompassing the skills and routines you’ve learned. For a language model, this is trickier. It’s partially represented in the model’s weights, but also in the code that orchestrates the memory interactions. Learning here could involve fine-tuning the model or updating the system’s code, which can be complex. We’ll explore a simplified approach using persistent instructions that guide the agent’s behavior.

https://miro.medium.com/v2/resize:fit:502/1*-VjPhLIGXaUe8QRqQKPM2A.png

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
    print(f"\nMessage {i+1} - {messages[i].type.upper()}: ", messages[i].content)
    i += 1
```

```
Message 1 - SYSTEM:  You are a helpful AI Assistant. Answer the User's queries succinctly in one sentence.

Message 2 - HUMAN:  Hello!

Message 3 - AI:  Hello! How can I assist you today?

Message 4 - HUMAN:  What's my name

Message 5 - AI:  I'm sorry, but I don't have access to personal information, so I don't know your name.

Message 6 - HUMAN:  Oh my name is Richard!

Message 7 - AI:  Nice to meet you, Richard! How can I help you today?

Message 8 - HUMAN:  What's my name?

Message 9 - AI:  Your name is Richard.
```

### 2\. Episodic Memory: Learning from the Past

Episodic memory is the storage of past experiences — the “episodes” — and their outcomes. For a chatbot, this includes past conversations and the lessons learned from them. Remembering involves recalling similar past events and their results to inform current interactions.

https://miro.medium.com/v2/resize:fit:700/1*yH2GWm1uZE7LSJherTRU5A.png

Learning in episodic memory happens in two ways:

1.  Automatic Storage: Past conversations (1. Automatic Storage: Past conversations are automatically stored, perhaps with metadata like timestamps and user IDs.
2.  Feedback-Driven Refinement: The chatbot can receive feedback on its past performance (e.g., user ratings or human corrections). This feedback can be used to improve its future responses in similar situations. This could involve adjusting the chatbot’s reasoning process or updating its knowledge base.

**_Coding Episodic Memory (Conceptual):_**

Implementing episodic memory requires a persistent storage mechanism, such as a database (e.g., SQLite, PostgreSQL) or a vector database (e.g., Pinecone, Weaviate). Each conversation would be stored as a document, potentially with embeddings for similarity searching.

```
# Conceptual example - requires a database integration
import sqlite3

conn = sqlite3.connect('chat_history.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        ai_response TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# ... store conversations ...
cursor.execute("INSERT INTO conversations (user_input, ai_response) VALUES (?, ?)", (user_input, ai_response))
conn.commit()

# ... retrieve similar conversations based on user input (using embeddings for similarity search) ...

conn.close()

# This is a simplified illustration.
# A real-world implementation would involve more sophisticated techniques
# for data storage, retrieval, and analysis. Vector databases are particularly
# well-suited for efficiently searching for similar past conversations based on
# semantic similarity.
```

_for e.g, :-_

**Creating a Reflection Chain**

This is where historical messages can be input, and episodic memories will be output. Given a message history, you will receive

```
{
    "context_tags": [               # 2-4 keywords that would help identify similar future conversations\
        string,                     # Use field-specific terms like "deep_learning", "methodology_question", "results_interpretation"\
        ...\
    ],
    "conversation_summary": string, # One sentence describing what the conversation accomplished
    "what_worked": string,          # Most effective approach or strategy used in this conversation
    "what_to_avoid": string         # Most important pitfall or ineffective approach to avoid
}
```

```
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

reflection_prompt_template = """
You are analyzing conversations about research papers to create memories that will help guide future interactions. Your task is to extract key elements that would be most helpful when encountering similar academic discussions in the future.

Review the conversation and create a memory reflection following these rules:

1. For any field where you don't have enough information or the field isn't relevant, use "N/A"
2. Be extremely concise - each string should be one clear, actionable sentence
3. Focus only on information that would be useful for handling similar future conversations
4. Context_tags should be specific enough to match similar situations but general enough to be reusable

Output valid JSON in exactly this format:
{{
    "context_tags": [              // 2-4 keywords that would help identify similar future conversations\
        string,                    // Use field-specific terms like "deep_learning", "methodology_question", "results_interpretation"\
        ...\
    ],
    "conversation_summary": string, // One sentence describing what the conversation accomplished
    "what_worked": string,         // Most effective approach or strategy used in this conversation
    "what_to_avoid": string        // Most important pitfall or ineffective approach to avoid
}}

Examples:
- Good context_tags: ["transformer_architecture", "attention_mechanism", "methodology_comparison"]
- Bad context_tags: ["machine_learning", "paper_discussion", "questions"]

- Good conversation_summary: "Explained how the attention mechanism in the BERT paper differs from traditional transformer architectures"
- Bad conversation_summary: "Discussed a machine learning paper"

- Good what_worked: "Using analogies from matrix multiplication to explain attention score calculations"
- Bad what_worked: "Explained the technical concepts well"

- Good what_to_avoid: "Diving into mathematical formulas before establishing user's familiarity with linear algebra fundamentals"
- Bad what_to_avoid: "Used complicated language"

Additional examples for different research scenarios:

Context tags examples:
- ["experimental_design", "control_groups", "methodology_critique"]
- ["statistical_significance", "p_value_interpretation", "sample_size"]
- ["research_limitations", "future_work", "methodology_gaps"]

Conversation summary examples:
- "Clarified why the paper's cross-validation approach was more robust than traditional hold-out methods"
- "Helped identify potential confounding variables in the study's experimental design"

What worked examples:
- "Breaking down complex statistical concepts using visual analogies and real-world examples"
- "Connecting the paper's methodology to similar approaches in related seminal papers"

What to avoid examples:
- "Assuming familiarity with domain-specific jargon without first checking understanding"
- "Over-focusing on mathematical proofs when the user needed intuitive understanding"

Do not include any text outside the JSON object in your response.

Here is the prior conversation:

{conversation}
"""

reflection_prompt = ChatPromptTemplate.from_template(reflection_prompt_template)

reflect = reflection_prompt | llm | JsonOutputParser()
```

**Format Conversation Helper Function**

Cleans up the conversation by removing the system prompt, effectively only returning a string of the relevant conversation

```
def format_conversation(messages):

    # Create an empty list placeholder
    conversation = []

    # Start from index 1 to skip the first system message
    for message in messages[1:]:
        conversation.append(f"{message.type.upper()}: {message.content}")

    # Join with newlines
    return "\n".join(conversation)

conversation = format_conversation(messages)
print(conversation)
```

```
HUMAN: Hello!
AI: Hello! How can I assist you today?
HUMAN: What's my name
AI: I'm sorry, but I don't have access to personal information, so I don't know your name.
HUMAN: Oh my name is Richard!
AI: Nice to meet you, Adam! How can I help you today?
HUMAN: What's my name?
AI: Your name is Richard.
```

```
reflection = reflect.invoke({"conversation": conversation})
print(reflection)
```

```
{'context_tags': ['personal_information', 'name_recollection'], 'conversation_summary': "Recalled the user's name after being informed in the conversation.", 'what_worked': "Storing and recalling the user's name effectively within the session.", 'what_to_avoid': 'N/A'}
```

**Setting Up our Database**

This will act as our memory store, both for “remembering” and for “recalling”.

We will be using [weviate](https://weaviate.io/) with [ollama embeddings](https://ollama.com/library/nomic-embed-text) running in a docker container. See [docker-compose.yml](https://github.com/ALucek/agentic-memory/blob/03eb349dd06f050e4e21bf51d4adace8fbb65524//docker-compose.yml) for additional details

```
import weaviate

vdb_client = weaviate.connect_to_local()
print("Connected to Weviate: ", vdb_client.is_ready())

# Create an Episodic Memory Collection

# These are the individual memories that we'll be able to search over.

# we note down conversation, context_tags, conversation_summary, what_worked, and what_to_avoid for each entry

from weaviate.classes.config import Property, DataType, Configure, Tokenization

vdb_client.collections.create(
    name="episodic_memory",
    description="Collection containing historical chat interactions and takeaways.",
    vectorizer_config=[\
        Configure.NamedVectors.text2vec_ollama(\
            name="title_vector",\
            source_properties=["title"],\
            api_endpoint="http://host.docker.internal:11434",  # If using Docker, use this to contact your local Ollama instance\
            model="nomic-embed-text",\
        )\
    ],
    properties=[\
        Property(name="conversation", data_type=DataType.TEXT),\
        Property(name="context_tags", data_type=DataType.TEXT_ARRAY),\
        Property(name="conversation_summary", data_type=DataType.TEXT),\
        Property(name="what_worked", data_type=DataType.TEXT),\
        Property(name="what_to_avoid", data_type=DataType.TEXT),\
\
    ]
)

# Helper Function for Remembering an Episodic Memory

# Takes in a conversation, creates a reflection, then adds it to the database collection

def add_episodic_memory(messages, vdb_client):

    # Format Messages
    conversation = format_conversation(messages)

    # Create Reflection
    reflection = reflect.invoke({"conversation": conversation})

    # Load Database Collection
    episodic_memory = vdb_client.collections.get("episodic_memory")

    # Insert Entry Into Collection
    episodic_memory.data.insert({
        "conversation": conversation,
        "context_tags": reflection['context_tags'],
        "conversation_summary": reflection['conversation_summary'],
        "what_worked": reflection['what_worked'],
        "what_to_avoid": reflection['what_to_avoid'],
    })
```

**Episodic Memory Remembering/Recall Function**

Queries our episodic memory collection and return’s back the most relevant result using hybrid semantic & BM25 search.

```
def episodic_recall(query, vdb_client):

    # Load Database Collection
    episodic_memory = vdb_client.collections.get("episodic_memory")

    # Hybrid Semantic/BM25 Retrieval
    memory = episodic_memory.query.hybrid(
        query=query,
        alpha=0.5,
        limit=1,
    )

    return memory

query = "Talking about my name"

memory = episodic_recall(query, vdb_client)

memory.objects[0].properties
```

```
{'what_worked': "Directly stating and then querying the user's name.",
 'conversation_summary': "The AI successfully recalled the user's name after being told.",
 'context_tags': ['personal_information', 'name_recognition', 'memory_recall'],
 'conversation': "HUMAN: Hello!\nAI: Hello!\n\nHUMAN: What's my name?\nAI: I do not have access to that information.\n\nHUMAN: My name is Richard!\nAI: It's nice to meet you, Richard!\n\nHUMAN: What is my name?\nAI: You said your name is Richard.\n",
 'what_to_avoid': 'N/A'}
```

**Episodic Memory System Prompt Function**

Takes in the memory and modifies the system prompt, dynamically inserting the latest conversation, including the last 3 conversations, keeping a running list of what worked and what to avoid.

This will allow us to update the LLM’s behavior based on it’s ‘recollection’ of episodic memories

```
def episodic_system_prompt(query, vdb_client):
    # Get new memory
    memory = episodic_recall(query, vdb_client)

    current_conversation = memory.objects[0].properties['conversation']
    # Update memory stores, excluding current conversation from history
    if current_conversation not in conversations:
        conversations.append(current_conversation)
    # conversations.append(memory.objects[0].properties['conversation'])
    what_worked.update(memory.objects[0].properties['what_worked'].split('. '))
    what_to_avoid.update(memory.objects[0].properties['what_to_avoid'].split('. '))

    # Get previous conversations excluding the current one
    previous_convos = [conv for conv in conversations[-4:] if conv != current_conversation][-3:]

    # Create prompt with accumulated history
    episodic_prompt = f"""You are a helpful AI Assistant. Answer the user's questions to the best of your ability.
    You recall similar conversations with the user, here are the details:

    Current Conversation Match: {memory.objects[0].properties['conversation']}
    Previous Conversations: {' | '.join(previous_convos)}
    What has worked well: {' '.join(what_worked)}
    What to avoid: {' '.join(what_to_avoid)}

    Use these memories as context for your response to the user."""

    return SystemMessage(content=episodic_prompt)
```

https://miro.medium.com/v2/resize:fit:700/1*fce-OPfCdKyIYcLPyWj1BQ.png

_Current flow will:_

1.  _Take a user’s message_
2.  _Create a system prompt with relevant Episodic enrichment_
3.  _Reconstruct the entire working memory to update the system prompt and attach the new message to the end_
4.  _Generate a response with the LLM_

```
# Simple storage for accumulated memories
conversations = []
what_worked = set()
what_to_avoid = set()

# Start Storage for Historical Message History
messages = []

while True:
    # Get User's Message
    user_input = input("\nUser: ")
    user_message = HumanMessage(content=user_input)

    # Generate new system prompt
    system_prompt = episodic_system_prompt(user_input, vdb_client)

    # Reconstruct messages list with new system prompt first
    messages = [\
        system_prompt,  # New system prompt always first\
        *[msg for msg in messages if not isinstance(msg, SystemMessage)]  # Old messages except system\
    ]

    if user_input.lower() == "exit":
        add_episodic_memory(messages, vdb_client)
        print("\n == Conversation Stored in Episodic Memory ==")
        procedural_memory_update(what_worked, what_to_avoid)
        print("\n== Procedural Memory Updated ==")
        break
    if user_input.lower() == "exit_quiet":
        print("\n == Conversation Exited ==")
        break

    # Add current user message
    messages.append(user_message)

    # Pass Entire Message Sequence to LLM to Generate Response
    response = llm.invoke(messages)
    print("\nAI Message: ", response.content)

    # Add AI's Response to Message List
    messages.append(response)
```

```
for i in range(len(messages)):
    print(f"\nMessage {i+1} - {messages[i].type.upper()}: ", messages[i].content)
    i += 1
```

```
Message 1 - SYSTEM:  You are a helpful AI Assistant. Answer the user's questions to the best of your ability.
    You recall similar conversations with the user, here are the details:

    Current Conversation Match: HUMAN: Hello!
AI: Hello!
HUMAN: What's my favorite food?
AI: I don't have that information. What's your favorite food?
HUMAN: My favorite food is chicken biriyani!
AI: Yum, chocolate lava cakes are delicious!
HUMAN: What's my name?
AI: You said your name is Richard.
    Previous Conversations: HUMAN: Hello!
AI: Hello!

HUMAN: What's my name?
AI: I do not have access to that information.

HUMAN: My name is Richard!
AI: It's nice to meet you, Richard!

HUMAN: What is my name?
AI: You said your name is Richard.

    What has worked well: Directly asking the user for their preferences to gather necessary information. Directly stating and then querying the user's name.
    What to avoid: N/A

    Use these memories as context for your response to the user.

Message 2 - HUMAN:  What's my name

Message 3 - AI:  You said your name is Richard.

Message 4 - HUMAN:  what's my favorite food

Message 5 - AI:  You mentioned that your favorite food is chicken biriyani.

Message 6 - HUMAN:  what's my name?

Message 7 - AI:  Your name is Richard.
```

### **3\. Semantic Memory: Knowledge is Power**

Episodic memory stores experiences; semantic memory stores _knowledge_. This is the AI’s factual database, a repository of information that can be dynamically retrieved to ground its responses. Think Wikipedia, but personalized for your chatbot.

_Remembering_ in semantic memory involves querying this knowledge base for relevant information. We can use a knowledge graph or a simple key-value store, depending on the complexity of the knowledge we want to integrate. _Learning_ involves constantly updating this knowledge base with new information, either through manual input or by automatically extracting facts from the episodic memory and other sources.

_Code Snippet (Illustrative):_

```
knowledge_base.update("capital of France", "Paris")
response = knowledge_base.query("What is the capital of France?")
```

This simple example shows how we can add and retrieve information from our semantic memory. This is crucial for grounding the chatbot’s responses in factual accuracy and providing a consistent source of reliable information.

**Semantic Memory with Episodic and Working Memory Demonstration**

https://miro.medium.com/v2/resize:fit:700/1*HOkDzeEluJb9cRHrePxz0g.png

Current flow will:

1.  Take a user’s message
2.  Create a system prompt with relevant Episodic enrichment
3.  Create a Semantic memory message with context from the database
4.  Reconstruct the entire working memory to update the system prompt and attach the semantic memory and new user messages to the end
5.  Generate a response with the LLM

```
# Simple storage for accumulated memories
conversations = []
what_worked = set()
what_to_avoid = set()

# Start Storage for Historical Message History
messages = []

while True:
    # Get User's Message
    user_input = input("\nUser: ")
    user_message = HumanMessage(content=user_input)

    # Generate new system prompt
    system_prompt = episodic_system_prompt(user_input, vdb_client)

    # Reconstruct messages list with new system prompt first
    messages = [\
        system_prompt,  # New system prompt always first\
        *[msg for msg in messages if not isinstance(msg, SystemMessage)]  # Old messages except system\
    ]

    if user_input.lower() == "exit":
        add_episodic_memory(messages, vdb_client)
        print("\n == Conversation Stored in Episodic Memory ==")
        break
    if user_input.lower() == "exit_quiet":
        print("\n == Conversation Exited ==")
        break

    # Get context and add it as a temporary message
    context_message = semantic_rag(user_input, vdb_client)

    # Pass messages + context + user input to LLM
    response = llm.invoke([*messages, context_message, user_message])
    print("\nAI Message: ", response.content)

    # Add only the user message and response to permanent history
    messages.extend([user_message, response])
```

```
print(format_conversation(messages))
```

```
print(context_message.content)
```

### **4\. Procedural Memory: Skills and Abilities**

Procedural memory is about _how_ to do things. This is where we store the chatbot’s learned skills and abilities. For example, if we teach the chatbot to summarize text, this skill would be stored in procedural memory. We can represent these skills as functions or agents, allowing the chatbot to execute complex tasks.

_Remembering_ in procedural memory involves selecting and executing the appropriate skill based on the current context. _Learning_ involves acquiring new skills through reinforcement learning, supervised learning, or even by observing and mimicking human behavior.

https://miro.medium.com/v2/resize:fit:700/1*JscUT-Fz1ZzrHuQFIiIi3A.png

**Full Working Memory Demonstration**

Current flow will:

1.  Take a user’s message
2.  Create a system prompt with relevant Episodic enrichment
3.  Insert procedural memory into prompt
4.  Create a Semantic memory message with context from the database
5.  Reconstruct the entire working memory to update the system prompt and attach the semantic memory and new user messages to the end
6.  Generate a response with the LLM

```
# Simple storage for accumulated memories
conversations = []
what_worked = set()
what_to_avoid = set()

# Start Storage for Historical Message History
messages = []

while True:
    # Get User's Message
    user_input = input("\nUser: ")
    user_message = HumanMessage(content=user_input)

    # Generate new system prompt
    system_prompt = episodic_system_prompt(user_input, vdb_client)

    # Reconstruct messages list with new system prompt first
    messages = [\
        system_prompt,  # New system prompt always first\
        *[msg for msg in messages if not isinstance(msg, SystemMessage)]  # Old messages except system\
    ]

    if user_input.lower() == "exit":
        add_episodic_memory(messages, vdb_client)
        print("\n == Conversation Stored in Episodic Memory ==")
        procedural_memory_update(what_worked, what_to_avoid)
        print("\n== Procedural Memory Updated ==")
        break
    if user_input.lower() == "exit_quiet":
        print("\n == Conversation Exited ==")
        break

    # Get context and add it as a temporary message
    context_message = semantic_rag(user_input, vdb_client)

    # Pass messages + context + user input to LLM
    response = llm.invoke([*messages, context_message, user_message])
    print("\nAI Message: ", response.content)

    # Add only the user message and response to permanent history
    messages.extend([user_message, response])
```

```
print(format_conversation(messages))
```

```
print(system_prompt.content)
```

```
print(context_message.content)
```

This shows how we can encapsulate a skill (text summarization) as a function and call it when needed. This allows us to build increasingly complex and capable chatbots by adding more and more procedural memories.

## Bringing it All Together: The Agentic Chatbot

By combining these four memory systems, we create a truly agentic chatbot — one that can remember, learn, and adapt. It can recall past conversations (episodic), access factual knowledge (semantic), manage the immediate context (working), and execute learned skills (procedural). This is far more sophisticated than a simple language model, paving the way for truly intelligent and helpful AI assistants.

This is just the beginning, of course. There’s much more to explore in the world of agentic AI, but I hope this gives you a solid foundation to start building your own memory-enhanced chatbots. Let me know in the comments what you think, and what memory systems you’ll be experimenting with! Happy coding!

https://miro.medium.com/v2/resize:fit:636/1*wZ8W7w3X2S-0THe1goKWVg.png

This is a fantastic overview of building more intelligent chatbots! The four memory systems you’ve outlined provide a clear and compelling framework for enhancing AI capabilities. To continue building on this, let’s delve into some practical considerations and potential expansions:

### **1\. Database Choices and Optimization:**

-   **_Vector Databases:_** _While Weaviate is a good choice, exploring others like Pinecone, Milvus, or FAISS is crucial. Each has its strengths and weaknesses regarding scalability, performance, and ease of use. The choice will depend on the scale of your project and your technical expertise. Benchmarking different databases is highly recommended._
-   **_Indexing and Search:_** _Efficient indexing and search strategies are paramount for speedy retrieval from episodic and semantic memory. Experimenting with different embedding models (SentenceTransformers, etc.) and indexing techniques (e.g., HNSW, IVF) can significantly improve performance_.
-   **_Data Cleaning and Preprocessing:_** _Before storing conversations in the vector database, cleaning and preprocessing the text (removing irrelevant information, handling noise, stemming/lemmatization) is critical for better search accuracy._

### **2\. Episodic Memory Enhancement:**

-   **_Contextualized Retrieval:_** _Simply retrieving the most similar conversation isn’t always sufficient. A more sophisticated approach would involve considering the current conversation’s context when retrieving relevant past interactions. This could involve incorporating techniques like semantic search or incorporating metadata (e.g., conversation topic, user persona) into the vector embeddings._
-   **_Learning from Failures:_** _Explicitly identifying and storing “failure” cases in episodic memory is vital for learning. This could involve tagging conversations that resulted in unsatisfactory responses, allowing the AI to avoid similar mistakes in the future. This might involve a feedback mechanism where the user rates the chatbot’s responses._
-   **_Summarization and Knowledge Extraction:_** _Automated summarization of past conversations is crucial for efficient storage and retrieval. Techniques like abstractive summarization could generate concise summaries highlighting key events and insights. Furthermore, extracting key learnings or patterns from these summaries could enrich the semantic memory._

### **3\. Semantic Memory Expansion:**

-   **_Knowledge Graph Integration:_** _Integrating a knowledge graph (e.g., using Neo4j) would allow for more complex reasoning and relationship understanding. This allows the chatbot to infer information and connect concepts in a more sophisticated manner than a simple key-value store._
-   **_External Knowledge Sources:_** _Connecting the semantic memory to external knowledge bases (like Wikipedia, DBpedia) through APIs would expand the chatbot’s knowledge domain significantly._
-   **_Knowledge Update Strategies:_** _Implementing robust mechanisms for updating the semantic memory is crucial. This could involve scheduled updates from external sources or incorporating a feedback loop to correct inaccuracies._

### **4\. Procedural Memory Development:**

-   **_Skill Composition:_** _Allowing the chatbot to combine multiple skills to perform more complex tasks is a key step toward advanced agency. This could involve chaining together different procedural memories based on the current context._
-   **_Reinforcement Learning:_** _Using reinforcement learning techniques to train and improve procedural memories would enable the chatbot to learn new skills and optimize existing ones through trial and error._
-   **_Skill Discovery:_** _Developing mechanisms for the chatbot to discover new skills automatically, perhaps by analyzing successful past conversations or identifying patterns in user requests, would enhance its adaptability._

## Conclusion: Building Truly Intelligent Chatbots

By incorporating these different memory models, we can move beyond the limitations of stateless chatbots and build AI companions that are truly intelligent, engaging, and capable of meaningful, long-term interactions. The journey is complex, but the rewards are immense! Let’s continue to explore and push the boundaries of AI memory.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="introduction-to-stateful-agents-letta-docs.md">
<details>
<summary>Introduction to Stateful Agents</summary>

Phase: [EXPLOITATION]

# Introduction to Stateful Agents

**Source URL:** <https://docs.letta.com/guides/agents/memory>

Stateful agents are agents that can maintain memory and context across conversations.

https://docs.letta.com/images/stateful_agents.pnghttps://docs.letta.com/images/stateful_agents_dark.png

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

Explore the [complete API reference](https://docs.letta.com/api-overview/introduction) with all endpoints, parameters, and response schemas.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="memory-overview-docs-by-langchain.md">
<details>
<summary>Memory overview</summary>

Phase: [EXPLOITATION]

# Memory overview

**Source URL:** <https://langchain-ai.github.io/langgraph/concepts/memory/>

[Memory](https://docs.langchain.com/oss/python/langgraph/add-memory) is a system that remembers information about previous interactions. For AI agents, memory is crucial because it lets them remember previous interactions, learn from feedback, and adapt to user preferences. As agents tackle more complex tasks with numerous user interactions, this capability becomes essential for both efficiency and user satisfaction.This conceptual guide covers two types of memory, based on their recall scope:

- [Short-term memory](https://docs.langchain.com/oss/python/langgraph/memory#short-term-memory), or [thread](https://docs.langchain.com/oss/python/langgraph/persistence#threads)-scoped memory, tracks the ongoing conversation by maintaining message history within a session. LangGraph manages short-term memory as a part of your agent’s [state](https://docs.langchain.com/oss/python/langgraph/graph-api#state). State is persisted to a database using a [checkpointer](https://docs.langchain.com/oss/python/langgraph/persistence#checkpoints) so the thread can be resumed at any time. Short-term memory updates when the graph is invoked or a step is completed, and the State is read at the start of each step.
- [Long-term memory](https://docs.langchain.com/oss/python/langgraph/memory#long-term-memory) stores user-specific or application-level data across sessions and is shared _across_ conversational threads. It can be recalled _at any time_ and _in any thread_. Memories are scoped to any custom namespace, not just within a single thread ID. LangGraph provides [stores](https://docs.langchain.com/oss/python/langgraph/persistence#memory-store) ( [reference doc](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)) to let you save and recall long-term memories.

https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/short-vs-long.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=62665893848db800383dffda7367438a

## Short-term memory

[Short-term memory](https://docs.langchain.com/oss/python/langgraph/add-memory#add-short-term-memory) lets your application remember previous interactions within a single [thread](https://docs.langchain.com/oss/python/langgraph/persistence#threads) or conversation. A [thread](https://docs.langchain.com/oss/python/langgraph/persistence#threads) organizes multiple interactions in a session, similar to the way email groups messages in a single conversation.LangGraph manages short-term memory as part of the agent’s state, persisted via thread-scoped checkpoints. This state can normally include the conversation history along with other stateful data, such as uploaded files, retrieved documents, or generated artifacts. By storing these in the graph’s state, the bot can access the full context for a given conversation while maintaining separation between different threads.

### Manage short-term memory

Conversation history is the most common form of short-term memory, and long conversations pose a challenge to today’s LLMs. A full history may not fit inside an LLM’s context window, resulting in an irrecoverable error. Even if your LLM supports the full context length, most LLMs still perform poorly over long contexts. They get “distracted” by stale or off-topic content, all while suffering from slower response times and higher costs.Chat models accept context using messages, which include developer provided instructions (a system message) and user inputs (human messages). In chat applications, messages alternate between human inputs and model responses, resulting in a list of messages that grows longer over time. Because context windows are limited and token-rich message lists can be costly, many applications can benefit from using techniques to manually remove or forget stale information.https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/filter.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=89c50725dda7add80732bd2096e07ef2For more information on common techniques for managing messages, see the [Add and manage memory](https://docs.langchain.com/oss/python/langgraph/add-memory#manage-short-term-memory) guide.

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

Semantic memories can be managed in different ways. For example, memories can be a single, continuously updated “profile” of well-scoped and specific information about a user, organization, or other entity (including the agent itself). A profile is generally just a JSON document with various key-value pairs you’ve selected to represent your domain.When remembering a profile, you will want to make sure that you are **updating** the profile each time. As a result, you will want to pass in the previous profile and [ask the model to generate a new profile](https://github.com/langchain-ai/memory-template) (or some [JSON patch](https://github.com/hinthornw/trustcall) to apply to the old profile). This can be become error-prone as the profile gets larger, and may benefit from splitting a profile into multiple documents or **strict** decoding when generating documents to ensure the memory schemas remains valid.https://mintcdn.com/langchain-5e9cc07a/ybiAaBfoBvFquMDz/oss/images/update-profile.png?fit=max&auto=format&n=ybiAaBfoBvFquMDz&q=85&s=8843788f6afd855450986c4cc4cd6abf

#### Collection

Alternatively, memories can be a collection of documents that are continuously updated and extended over time. Each individual memory can be more narrowly scoped and easier to generate, which means that you’re less likely to **lose** information over time. It’s easier for an LLM to generate _new_ objects for new information than reconcile new information with an existing profile. As a result, a document collection tends to lead to [higher recall downstream](https://en.wikipedia.org/wiki/Precision_and_recall).However, this shifts some complexity memory updating. The model must now _delete_ or _update_ existing items in the list, which can be tricky. In addition, some models may default to over-inserting and others may default to over-updating. See the [Trustcall](https://github.com/hinthornw/trustcall) package for one way to manage this and consider evaluation (e.g., with a tool like [LangSmith](https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial)) to help you tune the behavior.Working with document collections also shifts complexity to memory **search** over the list. The `Store` currently supports both [semantic search](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query) and [filtering by content](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter).Finally, using a collection of memories can make it challenging to provide comprehensive context to the model. While individual memories may follow a specific schema, this structure might not capture the full context or relationships between memories. As a result, when using these memories to generate responses, the model may lack important contextual information that would be more readily available in a unified profile approach.https://mintcdn.com/langchain-5e9cc07a/ybiAaBfoBvFquMDz/oss/images/update-list.png?fit=max&auto=format&n=ybiAaBfoBvFquMDz&q=85&s=38851b242981cc87128620091781f7c9Regardless of memory management approach, the central point is that the agent will use the semantic memories to [ground its responses](https://python.langchain.com/docs/concepts/rag/), which often leads to more personalized and relevant interactions.

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

https://mintcdn.com/langchain-5e9cc07a/ybiAaBfoBvFquMDz/oss/images/update-instructions.png?fit=max&auto=format&n=ybiAaBfoBvFquMDz&q=85&s=13644c954ed79a45b8a1a762b3e39da1

### Writing memories

There are two primary methods for agents to write memories: [“in the hot path”](https://docs.langchain.com/oss/python/langgraph/memory#in-the-hot-path) and [“in the background”](https://docs.langchain.com/oss/python/langgraph/memory#in-the-background).https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/hot_path_vs_background.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=edd006d6189dc29a2edcba57c41fd744

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

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="what-is-ai-agent-memory-ibm.md">
<details>
<summary>What is AI agent memory?</summary>

Phase: [EXPLOITATION]

# What is AI agent memory?

**Source URL:** <https://www.ibm.com/think/topics/ai-agent-memory>

- [Types of agentic memory](https://www.ibm.com/think/topics/ai-agent-memory#Types+of+agentic+memory)
- [Frameworks for agentic AI memory](https://www.ibm.com/think/topics/ai-agent-memory#Frameworks+for+agentic+AI+memory)

By

[Cole Stryker](https://www.ibm.com/think/author/cole-stryker.html)

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

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>