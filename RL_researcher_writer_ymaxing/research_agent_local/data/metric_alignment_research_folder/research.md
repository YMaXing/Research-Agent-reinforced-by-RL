# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What key concepts from human cognitive science and neuroscience on different memory types, such as semantic, episodic, and procedural, provide useful frameworks for designing persistent memory in AI agents?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://bluetickconsultants.medium.com/building-ai-agents-with-memory-systems-cognitive-architectures-for-llms-176d17e642e7

Query: What key concepts from human cognitive science and neuroscience on different memory types, such as semantic, episodic, and procedural, provide useful frameworks for designing persistent memory in AI agents?

Answer: The article draws from human cognitive architectures to design memory systems for LLM-based AI agents, identifying four key types inspired by human cognition: Working Memory (temporary holding and processing of active information for real-time interaction), Episodic Memory (recall of specific past events for learning from experiences, implemented via FAISS vector search for similarity-based retrieval of past conversations), Semantic Memory (foundational factual knowledge, concepts, and world relationships for reasoning, using RAG and FAISS for dynamic querying), and Procedural Memory (rules, processes, and task execution strategies, updated via fine-tuning or code changes for automating behaviors). These integrate for persistent learning: Working for immediate context, Episodic for adaptation, Semantic for accuracy, Procedural for execution. Combining them enables human-like persistent reasoning beyond stateless LLMs. References cognitive architectures like ACT-R implicitly through human analogies.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/

Query: What key concepts from human cognitive science and neuroscience on different memory types, such as semantic, episodic, and procedural, provide useful frameworks for designing persistent memory in AI agents?

Answer: Long-term memory follows a tripartite cognitive model from human neuroscience: Episodic (time-series events, sequential experiences like conversation logs with timestamps for continuity and experience replay), Semantic (distilled facts, knowledge representation via vector databases or knowledge graphs for generalization and RAG), Procedural (operational skills, dynamic execution of workflows and decision rules, refined via feedback for efficiency). Short-term working memory uses FIFO queues within context windows. Data migrates via cognitive compression from short-term to long-term, using separate storage (relational for episodic, vector for semantic, key-value for procedural). This enables human-like persistence, preventing drift and enabling adaptation across sessions. Advanced management includes asynchronous consolidation and intelligent forgetting mimicking Ebbinghaus curve.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://www.ibm.com/think/topics/ai-agent-memory

Query: What key concepts from human cognitive science and neuroscience on different memory types, such as semantic, episodic, and procedural, provide useful frameworks for designing persistent memory in AI agents?

Answer: AI agent memory mirrors human types: Short-term (recent inputs via context windows for immediate decisions), Long-term subdivided into Episodic (specific past experiences for case-based reasoning, logged events/outcomes e.g., financial choices), Semantic (factual knowledge, facts/rules via knowledge bases/vector embeddings for domain expertise e.g., legal precedents), Procedural (skills/behaviors for automatic task performance, via reinforcement learning). LTM uses RAG for retrieval. Frameworks like LangChain/LangGraph enable persistent storage/retrieval, improving adaptation over stateless models. Cites CoALA paper on cognitive architectures.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-should-try-in-2026/

Query: What key concepts from human cognitive science and neuroscience on different memory types, such as semantic, episodic, and procedural, provide useful frameworks for designing persistent memory in AI agents?

Answer: Frameworks implement human-inspired memory for persistent AI agents: Mem0 (personalized long-term memory across sessions), Zep (conversational episodic/semantic extraction), LangChain (various memory types/strategies), LlamaIndex (short/long-term for knowledge reasoning), Letta (OS-like context management), Cognee (knowledge graphs for interconnected episodic/semantic recall). Enables learning from interactions, context maintenance, personalization beyond stateless tools. Focuses on storage/retrieval/summarization for facts, experiences, preferences.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://www.digitalocean.com/community/tutorials/episodic-memory-in-ai

Query: What key concepts from human cognitive science and neuroscience on different memory types, such as semantic, episodic, and procedural, provide useful frameworks for designing persistent memory in AI agents?

Answer: Episodic memory (event-based personal experiences with context, e.g., user instructions) contrasts semantic (general facts), short-term (context window), procedural (skills). Stores/retrieves via vector databases/semantic search for lifelong learning, adaptation. Organized hierarchically or graphs; pruned by relevance/decay. Enables personalization, continuous learning, RL enhancement, task automation. Fits cognitive architecture for human-like persistence.

-----

</details>

<details>
<summary>How have expanding LLM context windows from 8k-16k to over 1 million tokens shifted engineering practices around memory compression, summarization, and raw history retention in agent systems?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://arxiv.org/pdf/2509.21361

Query: How have expanding LLM context windows from 8k-16k to over 1 million tokens shifted engineering practices around memory compression, summarization, and raw history retention in agent systems?

Answer: The expansion of context windows from hundreds to tens of thousands and recently to millions of tokens enables longer contexts for seamless retrieval-augmented generation (RAG), more nuanced chat histories, and document-centric agents reasoning over sprawling datasets. However, empirical evidence shows a divergence between maximum context window (MCW) and maximum effective context window (MECW), where performance degrades beyond certain token counts depending on task type. Models fail with as little as 100 tokens in some cases and show severe degradation by 1000 tokens, falling far short of MCW by >99%. This necessitates strategies to optimize RAG pipelines, truncate or summarize distant context, and use realistic MECW estimates rather than MCW for design. In agentic frameworks, understanding MECW per task and model improves accuracy to near flawless levels without modifications like temperature adjustments. Large contexts lead to increased hallucination rates, context rot, and cascading failures in chained agents. Recommendations include limiting token counts, using RAG under MECW to improve accuracy, and avoiding large context windows which degrade performance. For summarization tasks, models performed worse than needle-in-a-haystack, indicating large contexts are ineffective even for aggregation. Real-world RAG using provided facts improves accuracy under MECW but worsens it beyond, emphasizing careful raw history retention and compression.

-----

-----

Phase: [EXPLOITATION]

### Source [7]: https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows

Query: How have expanding LLM context windows from 8k-16k to over 1 million tokens shifted engineering practices around memory compression, summarization, and raw history retention in agent systems?

Answer: Context windows have expanded exponentially from 512 tokens in 2018 to 1 million by 2024 and 10 million with Llama 4, enabling processing of entire books, extended conversation history, and Cache Augmented Generation (CAG) for pre-computed documents. However, challenges include worse reference identification in longer prompts, variable signal-to-noise ratio where longer prompts reduce accuracy, increased costs from more input tokens, and output token latency rising with input size. Best practices emphasize selectivity: include only necessary context, structure important information earlier, monitor performance, and use hybrid CAG with RAG. Rather than maximizing capacity, be selective about context to avoid pitfalls, shifting practices toward compression and summarization of non-essential history while retaining raw key elements at the front. This balances performance, cost, and quality, avoiding over-reliance on raw history retention.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://www.linkedin.com/posts/bijit-ghosh-48281a78_optimizing-any-ai-agent-framework-with-context-activity-7357760656386760705-KI8a

Query: How have expanding LLM context windows from 8k-16k to over 1 million tokens shifted engineering practices around memory compression, summarization, and raw history retention in agent systems?

Answer: Expanding context windows leads to context rot where token count increases cause models to lose focus due to n² attention patterns, and dense context causes collapse into useless summaries. Engineering shifts to context engineering: Hierarchical Context Layering (meta, operational, domain, historical, environmental) loaded conditionally; Semantic Context Compression distilling documents and clustering embeddings; Dynamic context windowing pruning low-impact tokens and decaying stale info; Progressive summarization compressing older layers with boundaries; Async summarization to prevent drift; Context budgets pinning latest N turns verbatim while summarizing history; Structured summaries (environment, steps, blockers, decisions) flagging contradictions. Practices emphasize trimming entire turns, metadata hygiene stripping noise, idempotent summaries, and evaluation via LLM-as-judge for coherence. For agent systems, this enables task-specific memory, reducing hallucinations and token waste over raw retention.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://galileo.ai/blog/context-engineering-for-agents

Query: How have expanding LLM context windows from 8k-16k to over 1 million tokens shifted engineering practices around memory compression, summarization, and raw history retention in agent systems?

Answer: Larger windows enable multi-step tasks but cause context rot (performance drops after 30k tokens), distraction, poisoning, confusion, and clash. Practices shift to Five Buckets: Offloading heavy data externally (e.g., file system as memory, 100:1 compression); Context Isolation via multi-agents for parallel tasks; Retrieval with multi-techniques (semantic, keyword, graphs); Reducing via pruning/compaction at 95% usage preserving objectives; Caching for 10x cost reduction. Distinguish context (working memory: immediate, expensive, volatile) from memory (long-term: vast, persistent, retrieved). Keep recent tools/errors in context, historical in memory. Anti-patterns: modifying prior context (breaks cache), loading all tools. For agents, reversible compression, dynamic retrieval, auto-summarization prevent bloat while retaining raw access via paths/URLs, emphasizing structured retention over full history.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://towardsdatascience.com/deep-dive-into-context-engineering-for-ai-agents/

Query: How have expanding LLM context windows from 8k-16k to over 1 million tokens shifted engineering practices around memory compression, summarization, and raw history retention in agent systems?

Answer: Larger windows exacerbate context rot from attention scarcity (n² patterns) and don't solve unbounded enterprise data issues. Shifts to context engineering: Offloading to external systems; Dynamic retrieval over front-loading; Isolation to prevent contamination; Reduction via compaction (summarizing and restarting windows, preserving constraints like failed approaches). Context folding collapses subtasks. Harness manages assembly deterministically. Multi-agent communication via structured state transfer/artifacts, not shared transcripts, to avoid pollution and KV-cache penalties. Keep small, distinct tools. Agentic memory persists notes selectively (persistent preferences constraining reasoning), with revision. Compaction preserves what constrains future actions, avoiding useless summaries. Practices prioritize precise shaping over volume for coherence in long tasks.

-----

</details>

<details>
<summary>What real-world examples exist of early personal AI companion projects encountering context window limitations and subsequently building custom memory architectures with retrieval components?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://www.emotionmachine.com/blog/how-memory-works

Query: What real-world examples exist of early personal AI companion projects encountering context window limitations and subsequently building custom memory architectures with retrieval components?

Answer: Emotion Machine's AI companion project evolved through three memory architectures to address context window limitations. V1 used pgvector with semantic search and importance scoring for selective retrieval, but had limitations: selective retrieval missed important memories not matching query embeddings well, leading to injecting marginal memories into the context window; importance scoring added latency and cost. V2 introduced a scratchpad (inspired by ChatGPT and MemGPT paper), a small curated list of semantic entries injected fully into the system prompt every turn for full visibility, trading scalability for simplicity, with LLM-managed add/update/delete operations. V3 used a filesystem with hot_context.md (agent-curated summary ~500 words) for agentic workflows, where agents navigate files with bash tools like ls/grep outperforming specialized retrieval, synced to DB cache for fast chat reads. These iterations directly responded to context window constraints by building external memory with retrieval (V1), full injection (V2), and filesystem retrieval (V3). Mental models drew from MemGPT (LLM context as RAM, external as disk with paging via tools like core_memory_append, archival_memory_search).

-----

</details>

<details>
<summary>In production AI agents, what are the trade-offs and implementation lessons when using structured entity-based storage like JSON for semantic memories versus more advanced graph databases?</summary>

Phase: [EXPLOITATION]

### Source [12]: https://tianpan.co/blog/long-term-memory-types-ai-agents

Query: In production AI agents, what are the trade-offs and implementation lessons when using structured entity-based storage like JSON for semantic memories versus more advanced graph databases?

Answer: Semantic memory in agent systems is typically implemented as structured records in a graph database or key-value store. The graph approach is particularly powerful because it captures relationships: "user A works at company B, which uses tool C, which has known incompatibility with integration D." A flat key-value store can't represent that relational structure. Semantic memory contains facts and knowledge extracted from experience, no longer tied to specific episodes, answering "what do I know about this user/domain/entity." Implementation challenges include facts going stale over time, requiring confidence decay mechanisms where memories become less authoritative unless reinforced, downweighted or flagged for re-verification if untouched for months. Production implementations combine vector stores for semantic retrieval with temporal metadata filters, weighting toward recent memories and excluding older ones beyond relevance thresholds. Separate stores by type (episodic, semantic, procedural) with different retrieval strategies; mixing into a single vector database complicates retrieval. Write time quality is crucial: invest in extraction pipelines for semantic facts, importance scores, and temporal context. Build measurement baselines before sophistication due to 'Memory Trilemma' where retrieval initially drops accuracy.

-----

-----

Phase: [EXPLOITATION]

### Source [13]: https://www.techtarget.com/searchenterpriseai/tip/What-is-AI-agent-memory-Types-tradeoffs-and-implementation

Query: In production AI agents, what are the trade-offs and implementation lessons when using structured entity-based storage like JSON for semantic memories versus more advanced graph databases?

Answer: AI agent memory tradeoffs include reliability vs. autonomy: smaller, simpler memory (like JSON/document stores) improves predictability but limits context and creativity; larger sophisticated ones enable deeper autonomy but risk hallucinations. Cost vs. performance: MongoDB provides more space/reliability at less cost; DynamoDB has high storage costs and item size limits leading to complex situations. Semantic LTM stores facts, definitions, rules for domain expertise, implemented with databases and knowledge graphs. LTM uses databases, knowledge graphs, vector embeddings, RAG for context, understanding, reasoning. Short-term memory (STM) is simple rolling buffer but volatile; LTM slower but enables learning. Implementation often uses disk-based databases like MongoDB with RAG; frameworks like LangChain support vector databases, LangGraph hierarchical memory. Separate STM/LTM access via state client/retriever.

-----

-----

Phase: [EXPLOITATION]

### Source [14]: https://47billion.com/blog/ai-agent-memory-types-implementation-best-practices/

Query: In production AI agents, what are the trade-offs and implementation lessons when using structured entity-based storage like JSON for semantic memories versus more advanced graph databases?

Answer: Vector vs Graph vs SQL trade-offs: Vector DBs excellent for semantic similarity but poor multi-hop; Graph DBs fast relationship traversal ideal for episodic/procedural; SQL/Postgres reliable, auditable, ACID-compliant for long-term facts. Storage vs inference trade-off: full history explodes costs; use hierarchical memory, importance scoring, dynamic forgetting. Long-term memory in databases (Postgres for structured facts, vector stores for embeddings); sub-types episodic (interaction history), semantic (facts/preferences), procedural (workflows). Graph memory (Neo4j) excels at multi-hop reasoning. Mem0 uses hybrid: Postgres facts/episodic, Qdrant vectors, Neo4j graphs; automatic summarization, expiration. Forgetting mechanisms: temporal decay, relevance scoring. Multi-agent: shared organizational + private spaces via IDs prevent bloat. Production: Mem0/LangGraph for scale; add graph + self-improving loops.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://blogs.oracle.com/developers/comparing-file-systems-and-databases-for-effective-ai-agent-memory-management

Query: In production AI agents, what are the trade-offs and implementation lessons when using structured entity-based storage like JSON for semantic memories versus more advanced graph databases?

Answer: Avoid polyglot persistence: vector DB for embeddings, NoSQL for JSON, graph for relationships, relational for transactions leads to four databases, security models, backups, scaling, failure points; coordination tax with glue code. Filesystems for prototypes (simple, debuggable) but lack concurrency, ACID, semantic retrieval; databases essential for shared state. Converged databases handle operational history, artifacts, metadata, semantics unified. JSON/NoSQL as flat lacks relations; graphs/databases provide guarantees for production concurrency, auditability, queryability.

-----

-----

Phase: [EXPLOITATION]

### Source [16]: https://sparkco.ai/blog/ai-agent-memory-in-2026-comparing-rag-vector-stores-and-graph-based-approaches

Query: In production AI agents, what are the trade-offs and implementation lessons when using structured entity-based storage like JSON for semantic memories versus more advanced graph databases?

Answer: Graph-based memories excel in explicit relationships, multi-hop reasoning, structural integrity for complex inference but struggle scaling edges in dense graphs, complex joins, high relational storage, elevated indexing costs, compute-intensive traversals. Vector stores for semantic search but lack explicit relationships. RAG simple but poor multi-hop. Hybrids combine for precision gains. Graphs for knowledge-intensive tasks; trade precision vs speed.

-----

</details>

<details>
<summary>What are proven best practices for designing agent memory systems that handle conflict resolution, updates, and maintenance autonomously to avoid imposing cognitive overhead on end users?</summary>

Phase: [EXPLOITATION]

### Source [17]: https://www.usamaamjid.com/blog/building-autonomous-ai-agents-memory-systems-guide

Query: What are proven best practices for designing agent memory systems that handle conflict resolution, updates, and maintenance autonomously to avoid imposing cognitive overhead on end users?

Answer: Proven best practices for designing agent memory systems include implementing five types of agentic memory: working (short-term context), episodic (interaction history), semantic (knowledge base), procedural (workflow state), and meta-memory (learning/adaptation). Use hybrid memory architecture combining vector stores like Pinecone for semantic/episodic memory with structured storage like Redis for procedural memory. Key practices: Memory Versioning to track changes with immutable audit trails for multi-step processes; optimistic locking for concurrent updates to handle conflicts; memory pruning with policies for age, importance, and storage size to maintain efficiency; sanitization to prevent poisoning by redacting PII and validating content before storage. Time-aware retrieval with recency decay and semantic similarity scoring. Meta-memory enables autonomous adaptation by learning effective strategies. Monitor quality with metrics like retrieval latency and relevance; graceful degradation with fallbacks. Batch processing and caching for performance. These ensure autonomous conflict resolution (prioritize recent info, mark outdated as invalid), updates (versioning, consolidation), and maintenance (pruning, monitoring) without user overhead.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/

Query: What are proven best practices for designing agent memory systems that handle conflict resolution, updates, and maintenance autonomously to avoid imposing cognitive overhead on end users?

Answer: Amazon Bedrock AgentCore Memory provides best practices for long-term memory: Use memory extraction strategies (semantic for facts, user preferences, summary for narratives) processing events with timestamps for context continuity. Intelligent consolidation: Retrieve similar memories, use LLM prompts to decide ADD (distinct info), UPDATE (complement/enhance), or NO-OP (redundant), prioritizing recency for conflicts; mark outdated as INVALID for audit trails. Handles edge cases like out-of-order events, contradictions (update with recency), failures (retry/backoff, fallback add). Custom strategies for domain-specific extraction/consolidation. Namespaces for isolation (e.g., per-user/team). Monitor patterns via APIs. Async processing with short-term fallback. Parallel strategy processing. Best practices: Choose strategies per use case; design hierarchical namespaces; monitor creation/updates/skips; plan for async delays. Achieves 89-95% compression, low latency (20-40s extraction, 200ms retrieval). Enables autonomous resolution, updates, maintenance.

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://stevekinney.com/writing/agent-memory-systems

Query: What are proven best practices for designing agent memory systems that handle conflict resolution, updates, and maintenance autonomously to avoid imposing cognitive overhead on end users?

Answer: Best practices from research: Token-level memory (flat vector stores start simple, upgrade to planar graphs/hierarchical for multi-hop). Dynamics: Formation via knowledge distillation (extract facts) or semantic summarization; Evolution with consolidation (merge duplicates via clustering), updating (soft-delete superseded with timestamps, conflict detection at 0.6-0.9 similarity), forgetting (time decay, frequency, LLM-judged importance). Retrieval: Timing (agent decides/ confidence-based), HyDE (generate hypothetical for better query embedding), hybrid (BM25+semantic+graph), post-process (rerank, MMR diversity, filter). Trustworthy: Tenant isolation (per-tenant storage), shared cache keys include namespace, soft-delete for GDPR. Experiential memory for improvement (store trajectories/strategies). Multi-tenancy prevents leaks. Conflict surfacing over silent resolution. Hierarchical folding for context limits. Autonomous via agent-controlled retrieval as tool, background consolidation.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://machinelearningmastery.com/7-steps-to-mastering-memory-in-agentic-ai-systems/

Query: What are proven best practices for designing agent memory systems that handle conflict resolution, updates, and maintenance autonomously to avoid imposing cognitive overhead on end users?

Answer: 7 steps: 1. Treat as systems problem (write/read paths, eviction). 2. Taxonomy: short-term (context window), episodic (events), semantic (facts), procedural (workflows). 3. RAG for shared knowledge, memory for user-specific. 4. Decisions: distill to structured objects; store as embeddings/profiles/graphs; hybrid retrieval; decay/TTL for forgetting. 5. Context as constrained: prioritize/compress/filter to avoid poisoning/distraction; agent-controlled paging. 6. Retrieval as tool in loop for targeted access; versioning/ownership for multi-agent. 7. Evaluate: retrieval metrics (latency/precision/recall), unit tests, monitor growth, use corrections as signals. Frameworks like MemGPT/Letta handle infra. Intentional writes/removals ensure autonomous handling without user overhead.

-----

</details>

<details>
<summary>What specific limitations does the 'lost in the middle' effect impose on LLM performance when using extended conversation histories for short-term memory in agent systems?</summary>

Phase: [EXPLOITATION]

### Source [21]: https://mem0docs.xyz/task/blog/lost-in-the-middle-problem-ai-agent-memory/

Query: What specific limitations does the 'lost in the middle' effect impose on LLM performance when using extended conversation histories for short-term memory in agent systems?

Answer: The 'lost in the middle' problem is an empirically documented failure mode of large language models: when a long context window contains relevant information, models reliably attend to content near the beginning and end, and systematically overlook content in the middle. This has direct implications for any agent that relies on passing full conversation history to the model. A 2023 study from Stanford ('Lost in the Middle: How Language Models Use Long Contexts') demonstrated that LLM performance on multi-document question answering degrades when the relevant passage is placed in the middle of a long context. Models with 20 documents performed best when the answer was in the first or last document, and worst when it was at position 10-11. The effect held across GPT-3.5, Claude, and other major models. If your memory strategy is to concatenate conversation history and prepend it to the system prompt, you are creating exactly this failure condition at scale. A user who mentioned their security requirements 40 messages ago — now buried in the middle of a 60,000-token context — is less likely to have those requirements honored than if they had been mentioned in the last two messages. The most important context, established early in a relationship, ends up furthest from the model's attention.

-----

-----

Phase: [EXPLOITATION]

### Source [22]: https://www.linkedin.com/posts/philipp-schmid-a6a2bb196_do-llms-struggle-in-long-multi-turn-conversations-activity-7329049107690381312-aRJL

Query: What specific limitations does the 'lost in the middle' effect impose on LLM performance when using extended conversation histories for short-term memory in agent systems?

Answer: "loss-in-the-middle", LLMs pay less attention to information provided in intermediate turns compared to the first and last turns. LLMs show a significant performance drop (average 39%) in multi-turn conversations compared to single-turn, fully-specified ones. Degradation is primarily due to a large increase in unreliability (+112%) rather than a major loss in aptitude (-15%). This affects multi-turn conversations where important information from intermediate turns gets less attention.

-----

-----

Phase: [EXPLOITATION]

### Source [23]: https://substack.com/home/post/p-163369565

Query: What specific limitations does the 'lost in the middle' effect impose on LLM performance when using extended conversation histories for short-term memory in agent systems?

Answer: A 2023 paper from Stanford and UNC titled 'Lost in the Middle: How Language Models Use Long Contexts' showed that LLMs tend to latch onto the beginning and end of a document, leaving the midsection to fade into the fog. Give an LLM a document with thousands of tokens and bury a key fact in the middle. The model fumbles again and again. Transformers promise attention across all tokens, but attention is not memory. Scaling the context window is not the same as teaching a model how to use it. A 2024 study by MIT and Google Cloud AI showed a U-shaped attention bias: LLMs consistently favor the start and end of input sequences, neglecting the middle even when it contains the most relevant content.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2

Query: What specific limitations does the 'lost in the middle' effect impose on LLM performance when using extended conversation histories for short-term memory in agent systems?

Answer: In 2023, researchers from Stanford, UC Berkeley, and Samaya AI published 'Lost in the Middle' showing a U-shaped performance curve: high accuracy when relevant document at beginning or end, dramatic drop in middle. Affects multi-turn conversations where important information was mentioned 20 messages ago. Bigger context windows mean more middle, more room for information to get lost. It affects any task that puts multiple pieces of information into the context — summarization, question answering over multiple documents, multi-turn conversations.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/

Query: What specific limitations does the 'lost in the middle' effect impose on LLM performance when using extended conversation histories for short-term memory in agent systems?

Answer: Current LLM agents’ short-term memories are often constrained by token limits. Full Conversation Buffer stores entire history but increases token usage, latency, and cost as conversations lengthen; not scalable for very long dialogues. Windowed Buffer retains recent messages but risks losing older context. This relates to limitations in handling extended histories due to context window constraints, implying lost in the middle issues in long contexts.

-----

</details>

<details>
<summary>How can procedural memory be implemented in AI agents to store and retrieve reusable multi-step workflows for improved reliability on common tasks?</summary>

Phase: [EXPLOITATION]

### Source [26]: https://www.decodingai.com/p/how-does-memory-for-ai-agents-work

Query: How can procedural memory be implemented in AI agents to store and retrieve reusable multi-step workflows for improved reliability on common tasks?

Answer: Procedural memory is the agent’s muscle memory, consisting of skills, learned workflows, and 'how-to' knowledge that dictates the ability to perform multi-step tasks. It is often baked into the agent’s system prompt as reusable tools or defined sequences. For example, an agent stores a 'MonthlyReportIntent' procedure: 1) Query sales DB, 2) Summarize findings, 3) Email user. This makes behavior reliable and predictable by encoding successful workflows, avoiding reasoning from scratch each time. Implementation: Define a procedure as a text block with steps, e.g., procedure_name = 'monthly_report'; steps = ['Query sales DB for the last 30 days.', 'Summarize top 5 insights.', 'Ask user whether to email or display.']; Save using mem_add_text(procedure_text, category='procedure', procedure_name=procedure_name). Retrieve by intent: results = mem_search('how to create a monthly report', category='procedure', limit=1), outputting the procedure steps. This enhances reliability on common tasks by reusing multi-step workflows.

-----

-----

Phase: [EXPLOITATION]

### Source [27]: https://arxiv.org/html/2511.22074v1

Query: How can procedural memory be implemented in AI agents to store and retrieve reusable multi-step workflows for improved reliability on common tasks?

Answer: PRAXIS (Procedural Recall for Agents with eXperiences Indexed by State) implements procedural memory as a lightweight post-training mechanism storing consequences of actions and retrieving by matching environmental and internal states of past episodes to the current state. Each memory entry includes: M_env-pre (environmental state before action), M_int (agent's internal state including directive), a_i (action taken), M_env-post (state after action). Retrieval uses Alg. 1 to fetch informative memories augmenting action selection with state-action-result exemplars generated in real-time. Evaluated on REAL web browsing benchmark, it improves task completion accuracy (40.3% to 44.1% mean over five reps), best-of-5 accuracy (53.7% to 55.7%), reliability (74.5% to 79.0%), and efficiency (steps from 25.2 to 20.2 avg). Retrieved traces provide reusable priors, suppress stochastic variance, bias towards successful trajectories, generalize to unseen tasks/interfaces, essential for fast-evolving stateful environments like web automation.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://arxiv.org/html/2508.06433v2

Query: How can procedural memory be implemented in AI agents to store and retrieve reusable multi-step workflows for improved reliability on common tasks?

Answer: Mem^p framework endows agents with learnable, updatable procedural memory by distilling past trajectories into fine-grained step-by-step instructions and higher-level script-like abstractions. Strategies for Build (full trajectory, script abstraction, proceduralization combining both), Retrieval (query-vector, keyword-vector like AveFact), Update (vanilla append, validation filter successes, adjustment/reflection on failures). Stored as Mem = sum m^p_t where m^p_t = B(tau_t, r_t); retrieved via cosine similarity argmax S(t_new, t_i). On TravelPlanner/ALFWorld, boosts success (e.g., GPT-4o Proceduralization: TravelPlanner #CS 79.94, ALFWorld Test 77.86; steps reduced), eliminates fruitless exploration, continual linear mastery via updates. Scales with retrieval breadth/k, transfers from strong (GPT-4o) to weak models (Qwen2.5-14B +5% success). Update via reflection most effective, enabling reuse of reasoning/tool sequences/recovery tactics across similar long-horizon tasks in same environment.

-----

</details>

<details>
<summary>What are the practical trade-offs of storing agent memories as raw unstructured strings versus more processed formats in scalable production environments?</summary>

Phase: [EXPLOITATION]

### Source [29]: https://blogs.oracle.com/developers/comparing-file-systems-and-databases-for-effective-ai-agent-memory-management

Query: What are the practical trade-offs of storing agent memories as raw unstructured strings versus more processed formats in scalable production environments?

Answer: The article compares file systems (raw unstructured strings like markdown files, logs, transcripts) versus databases (processed formats with structure, vectors, SQL tables) for AI agent memory in scalable production. Raw unstructured strings in file systems excel for prototypes: simple, transparent, debuggable, token-efficient via progressive disclosure (tail, grep, range reads), pretraining-native interface, low overhead, natural for artifacts. However, in production they fail on concurrency (silent corruption, no ACID), brittle search (keyword/grep misses semantics), scaling (directory bloat, expensive scans), DIY indexing, schema drift, poor multi-user coordination, coarse security. Databases win for production: concurrency/integrity guarantees, semantic retrieval (vectors beat grep on paraphrases), indexed scalability, ACID transactions, fine-grained access control, auditability. Benchmarks show database-backed MemAgent faster/qualitatively better on large corpora (87.1% vs 29.7% LLM judge score) due to relevant chunks vs scanning/paging files; concurrency tests reveal filesystem locking reinventing databases with fewer guarantees. Hybrid recommended: file ergonomics for dev, database for durable shared memory. Polyglot persistence warned against—unified database simplifies. For multi-user/scale, databases enforce correctness/coordination essential.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://www.databricks.com/blog/memory-scaling-ai-agents

Query: What are the practical trade-offs of storing agent memories as raw unstructured strings versus more processed formats in scalable production environments?

Answer: File systems store raw unstructured strings (markdown/logs) well for small-scale/individual users but degrade at scale: lacks indexing/structured queries/semantic search, retrieval degrades with growth, hard governance. Processed formats in dedicated stores (e.g., PostgreSQL/pgvector) enable scalable storage with structured queries, full-text, vector similarity in unified engine; serverless separates storage/compute for cost/durability. Episodic (raw interactions) vs semantic (distilled facts/skills) require different processing/retrieval; personal vs organizational needs scoped access. Memory management essential: consolidation (quality control), evolution (updates/pruning), governance (identity-aware ACLs, lineage). Raw piles become insufficient when shared/multi-process; databases coordinate/correct under concurrency like Apollo-era IMS. Production needs converged systems avoiding polyglot persistence failure modes.

-----

-----

Phase: [EXPLOITATION]

### Source [31]: https://vectorize.io/articles/best-ai-agent-memory-systems

Query: What are the practical trade-offs of storing agent memories as raw unstructured strings versus more processed formats in scalable production environments?

Answer: Raw unstructured strings (chat logs) are noise; processed formats extract facts/entities/embeddings/graphs for structured knowledge. Ingestion pipelines (not dumping text) identify facts, resolve entities, add timestamps/embeddings—output structured, not blobs. Storage layers: vector (semantic), graph (relations), keyword (exact), temporal (time-aware). Well-designed systems do heavy processing at write (extraction/resolution/graph) for fast reads; memories written once (background), read many times (latency-sensitive). Raw fails vector-only on terminology mismatch; multi-strategy (semantic+keyword+graph+temporal) robust. Benchmarks like LoCoMo/LongMemEval test conversational recall, but institutional knowledge (lessons/domain models) needs extraction/compounding. Production optimizes reads over writes; raw chat buffers handle personalization, but institutional needs processed structures (vectors+graphs).

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://dev.to/dohkoai/8-ai-agent-memory-patterns-for-production-systems-beyond-basic-rag-5795

Query: What are the practical trade-offs of storing agent memories as raw unstructured strings versus more processed formats in scalable production environments?

Answer: Raw strings (sliding window of messages) baseline but need smart summarization; semantic memory processes into embeddings/categories/importance/recency for meaning-based retrieval vs recency. Episodic stores sequences/events/outcomes/lessons (structured from raw). Working memory structures current task (goal/plan/findings/hypotheses). Persistent SQLite persists all with categories/indexes/gc. Consolidation processes raw into merged/strengthened memories (merge duplicates, extract patterns, decay/promote). Contextual retrieval factors task/emotion/trajectory beyond raw query. Raw lacks structure/scalability; processed enables importance/duplicate detection/gc/consolidation. SQLite embedded/zero-config/concurrent for production persistence vs raw files.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://stevekinney.com/writing/agent-memory-systems

Query: What are the practical trade-offs of storing agent memories as raw unstructured strings versus more processed formats in scalable production environments?

Answer: Raw unstructured (token-level flat: bag of text chunks) simple/inspectable/debuggable for hosted models; processed (planar: graphs/trees; hierarchical: abstraction layers) enables multi-hop but maintenance complex. Benchmarks show simple retrieval beats hierarchies often. Knowledge distillation extracts facts from raw; structured construction builds graphs/trees. Consolidation merges/updates/prunes raw entries. Evolution resolves conflicts (soft-delete timestamps), forgetting (decay/access/importance). Retrieval: hybrid (BM25+semantic+graph) over raw; HyDE generates answer-shaped queries. Multi-tenancy needs tenant-isolated storage vs shared raw. Production: token-level with strong dynamics (formation/evolution/retrieval); raw risks noise/contradictions, processed adds precision/scalability but complexity. Start flat, add structure on failures.

-----

</details>

<details>
<summary>How should memory architectures be tailored to specific agent product goals, such as factual accuracy in enterprise Q&A versus narrative continuity in personal companions?</summary>

Phase: [EXPLOITATION]

### Source [34]: https://towardsai.net/p/machine-learning/how-to-design-efficient-memory-architectures-for-agentic-ai-systems

Query: How should memory architectures be tailored to specific agent product goals, such as factual accuracy in enterprise Q&A versus narrative continuity in personal companions?

Answer: Tailor memory architectures based on agent workload and goals. For factual accuracy in enterprise Q&A like medical assistants, legal research, financial advisors, use knowledge graphs (GraphRAG) for precise, explainable reasoning and high-fidelity facts, avoiding hallucination risks from fuzzy vector similarity. Hybrid vector retrieval for speed plus GraphRAG for precision. Semantic memory suffices for simple Q&A. For long conversations requiring narrative continuity, add episodic memory for past experiences/conversation history and working memory management. Hierarchical memory (H-MEM, MemGPT) essential for long-running sessions spanning 100+ turns or multiple days/weeks to prevent context distraction and control costs. The right architecture combines memory types: simple Q&A uses semantic memory; long conversations add episodic/working; complex reasoning needs procedural and knowledge graphs. Start simple with vector RAG, add complexity for scale, factual errors, or high costs: hierarchical for conversations, graphs for fidelity.

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/

Query: How should memory architectures be tailored to specific agent product goals, such as factual accuracy in enterprise Q&A versus narrative continuity in personal companions?

Answer: Design memory architecture intentionally for agent objectives using structured short-term (immediate conversational context) and long-term memory (persistent knowledge/preferences). Use hierarchical namespaces (e.g., /org_id/user_id/preferences) for isolation/retrieval, TTL based on needs (e.g., 30 days chat histories vs. longer preferences). Memory strategies: Semantic for facts/knowledge (enterprise Q&A accuracy), Summary for conversation points/decisions (narrative continuity), User Preferences for styles/choices (personalization). Optimization works backwards from core objectives: short-term for immediate context, long-term for insights across sessions. For enterprise, focus on persistent facts/preferences; for companions, summaries and preferences maintain continuity. Custom strategies for domain-specific extraction.

-----

-----

Phase: [EXPLOITATION]

### Source [36]: https://medium.com/@upadhya.saumya/architecting-intelligent-agents-a-comprehensive-guide-to-memory-context-a2868a3cfd43

Query: How should memory architectures be tailored to specific agent product goals, such as factual accuracy in enterprise Q&A versus narrative continuity in personal companions?

Answer: Tailor hybrid memory systems to use case: Factual grounding in enterprise Q&A requires RAG with factual long-term/semantic memory (vector DB/knowledge graph for proprietary docs). Narrative continuity in personal companions needs episodic memory (past interactions in structured DBs/vector stores with temporal filtering) and long-term personalization (persistent user profiles). Short-term/in-context for simple chatbots; complex workflows need structured state tracking. Architectural decision points: factual grounding uses RAG/semantic; personalization/episodic for continuity. Hybrid combines types: semantic for knowledge, episodic for experiences, working for immediate.

-----

-----

Phase: [EXPLOITATION]

### Source [37]: https://www.thenirvanalab.com/blog/architecting-ai-agents/

Query: How should memory architectures be tailored to specific agent product goals, such as factual accuracy in enterprise Q&A versus narrative continuity in personal companions?

Answer: Choose memory layer per business objective: short-term for current session, long-term for personalization/continuity (customer engagement/companions), episodic for traceability (regulatory/enterprise Q&A). Memory provides context/continuity; tailor to outcomes like reducing support costs (recall complaints) vs. loyalty (personalization). Not every case needs long-term; regulatory favors episodic over personalization.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://dev.to/oblivionlabz/building-an-ai-agent-with-memory-architecture-for-power-users-2kpl

Query: How should memory architectures be tailored to specific agent product goals, such as factual accuracy in enterprise Q&A versus narrative continuity in personal companions?

Answer: Three-layer memory for context retention: Short-term (immediate window for focus/continuity), Long-term (vector DB for profiles/decisions, semantic search), Working (buffer retrieves/processes LTM for STM). Enables learning from past, consistency across sessions for power users. Prompting prioritizes long-term context for relevant continuity.

-----

</details>

<details>
<summary>What cognitive science principles best explain the distinctions and interactions between an LLM's pre-trained parametric knowledge, its working context as short-term memory, and external persistent long-term storage in agent design?</summary>

Phase: [EXPLOITATION]

### Source [39]: https://aiagentmemory.org/articles/persistent-memory-for-llm/

Query: What cognitive science principles best explain the distinctions and interactions between an LLM's pre-trained parametric knowledge, its working context as short-term memory, and external persistent long-term storage in agent design?

Answer: The source distinguishes persistent memory for LLMs (long-term memory) from the model’s internal working memory or context window. Working Memory (Context Window): This is the temporary, immediate information the LLM is actively processing. It’s fast but limited in size and duration. Information here is lost once the window slides or the session ends. Long-Term Memory (Persistent Memory): This is the external, durable storage for information that the LLM can access across sessions. It’s slower to access but can hold vast amounts of data indefinitely. The goal of persistent memory for LLMs is to bridge the gap between the transient nature of working memory and the need for lasting knowledge. Types of persistent memory mimic human memory: Episodic memory stores specific past events or interactions; Semantic memory stores general knowledge, facts, concepts, and relationships. An LLM uses semantic memory to answer factual questions, understand abstract concepts, and make logical deductions, distinct from personal experiences in episodic memory. Pre-trained parametric knowledge is implied as internal semantic memory encoded in model weights, while external persistent storage handles episodic and additional semantic memory across sessions. Persistent memory overcomes LLM statelessness, enabling maintenance of conversational context, building long-term knowledge, personalization, and complex tasks.

-----

-----

Phase: [EXPLOITATION]

### Source [40]: https://www.emergentmind.com/topics/persistent-memory-for-llm-agents

Query: What cognitive science principles best explain the distinctions and interactions between an LLM's pre-trained parametric knowledge, its working context as short-term memory, and external persistent long-term storage in agent design?

Answer: Persistent memory in LLM agents draws on cognitive science, distinguishing transient short-term/working memory from persistent long-term cross-session stores. Human cognitive models like Baddeley’s working memory and Atkinson-Shiffrin model inspire centralized working memory hubs, episodic buffers, and mechanisms for encoding, prioritization, layered retrieval. Architectural innovations include multi-level memory hierarchies (e.g., Core/Episodic/Semantic/Procedural in MIRIX; STM/MTM/LPM in MemoryOS). Key principle: Separation of transient (short-term/working memory, token-limited context) from persistent (long-term, external evolving table/buffer/hierarchical store separate from static model weights/parametric knowledge). Persistent memory enables long-term retention, structured organization, dynamic updates for sequential decision-making, personalization, lifelong learning. Nemori uses graph-structured/event-based segmentation from cognitive science (Two-Step Alignment, Predict-Calibrate principles). MIRIX employs six memory types (Core, Episodic, Semantic, Procedural, Resource, Knowledge Vault) managed by dedicated agents. Pre-trained parametric knowledge is static internal weights; working context is transient STM; external persistent LTM is dynamic, updatable via RL, hierarchical structures.

-----

-----

Phase: [EXPLOITATION]

### Source [41]: https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/

Query: What cognitive science principles best explain the distinctions and interactions between an LLM's pre-trained parametric knowledge, its working context as short-term memory, and external persistent long-term storage in agent design?

Answer: Cognitive science categorizes memory into procedural, semantic, episodic. Procedural memory: LLM weights/chain-of-thought examples/agent codes (pre-trained parametric knowledge). Semantic memory: facts/concepts/general knowledge; internal (pre-training encoded in weights), external (knowledge base like graph/vector DB). Episodic memory: past experiences/interactions, intertwined with short-term memory via few-shot prompting/summarizing. Short-Term Memory (STM): working memory in context window for current task/conversation, temporary (lost post-session unless transferred). Long-Term Memory (LTM): external storage (DBs/vector DBs) for info beyond window/across sessions, retrieved into STM. STM ensures current state awareness; LTM stores acquired info for future. Hybrid: parametric (fine-tuned LLM/internal) + non-parametric (external DB); symbolic (structured) + neural (vector); summarization + vector. Pre-trained parametric = internal semantic/procedural; working context = STM/episodic; external persistent = LTM semantic/episodic.

-----

-----

Phase: [EXPLOITATION]

### Source [42]: https://arxiv.org/html/2504.02441v1

Query: What cognitive science principles best explain the distinctions and interactions between an LLM's pre-trained parametric knowledge, its working context as short-term memory, and external persistent long-term storage in agent design?

Answer: Cognitive architecture categorizes memory: Sensory (prompt input), Short-Term/Working Memory (STM: context window for immediate processing, lost post-session), Long-Term Memory (LTM: explicit-episodic/semantic via external DBs/vector/graph stores; implicit-procedural). LLMs encode linguistic patterns into parameters (pre-trained parametric knowledge/static after training, no real-time updates unlike dynamic human memory). Parallels: pattern recognition, context influence, primacy/recency effects. Differences: LLMs static (no real-time adaptation/emotional influence/selective forgetting); human dynamic/malleable/selective. Text-based LTM: acquisition (selection/summarization), management (update/storage/access), utilization (retrieval: semantic/full-text/etc.). LTM bridges STM transience. Parametric knowledge is static weights; working context=STM; external persistent=external LTM stores.

-----

-----

Phase: [EXPLOITATION]

### Source [43]: https://www.cognee.ai/blog/fundamentals/llm-memory-cognitive-architectures-with-ai

Query: What cognitive science principles best explain the distinctions and interactions between an LLM's pre-trained parametric knowledge, its working context as short-term memory, and external persistent long-term storage in agent design?

Answer: Cognitive architectures: Sensory Memory (SM: prompt input), Short-Term Memory (STM/working: context window, ephemeral), Long-Term Memory (LTM: external DBs/vector/graph for persistent knowledge/experiences). LTM explicit (episodic events/semantic facts), implicit (procedural skills). Pre-trained parametric knowledge akin to internal semantic/procedural in weights. STM: immediate context, lost post-response. LTM: vector/graph DBs for cross-session recall. Memory enables context-rich responses, reduces hallucinations (RAG), efficient data processing, self-evolution. Challenges: data engineering, scaling, privacy.

-----

</details>

<details>
<summary>How can LLM prompts be designed to extract episodic memories that effectively capture temporal sequences, emotional context, and nuanced relationship dynamics from raw conversations?</summary>

Phase: [EXPLOITATION]

### Source [44]: https://aclanthology.org/2023.emnlp-main.838.pdf

Query: How can LLM prompts be designed to extract episodic memories that effectively capture temporal sequences, emotional context, and nuanced relationship dynamics from raw conversations?

Answer: The paper describes designing sophisticated LLM prompts using ChatGPT to generate multi-session dialogues that capture temporal sequences (time intervals like 'a few hours later' to 'a couple of years later'), emotional context through coherent interactions across sessions, and nuanced relationship dynamics (pre-defined 10 relationships like co-workers, husband-wife, assigned via prompts). Prompts include: event, time interval, speaker relationship, and full prior context. Example prompt: 'The following is a next conversation between {Relationship}. The {Relationship} took turns talking about the below topics: {Session N-1 Event Description} {Time Intervals Between Session N-1 and N} the last topic, this is the topic {Relationship} are talking about today: {Session N Event Description} {Speaker A}’s statements start with [Speaker A] and {Speaker B}’s statements start with [Speaker B]. {Speaker A} and {Speaker B} talk about today’s topic, and if necessary, continue the conversation by linking it to the conversation topic of the past. Complete the conversation in exactly that format.' Relationships assigned by prompting ChatGPT with events and list of 10 options. Prompts ensure chronological dynamics, consistency, and relational nuances, enabling extraction of episodic memories from generated conversations. Human evaluation confirms high coherence (4.04/5), consistency (4.41/5), time interval awareness (4.46/5), and relationship reflection (4.40/5).

-----

</details>

<details>
<summary>What hybrid retrieval techniques combining entity filtering, vector similarity, temporal decay, and re-ranking are most effective for pulling relevant items from different long-term memory stores into an agent's context?</summary>

Phase: [EXPLOITATION]

### Source [45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12092450/

Query: What hybrid retrieval techniques combining entity filtering, vector similarity, temporal decay, and re-ranking are most effective for pulling relevant items from different long-term memory stores into an agent's context?

Answer: The paper 'Enhancing memory retrieval in generative agents through LLM-trained cross attention networks' discusses common memory retrieval methods for generative agents including temporal decay ranking, evaluation of memory importance, vector similarity matching, and combinations of these techniques. It proposes Weighted Memory Retrieval (WMR) as baseline: score = Recency × Importance × Relevance, where Recency decays hourly by 0.995 factor, Importance from LLM, Relevance as cosine similarity between memory and query embeddings. Top-k memories selected. Limitations noted in matching complex correlations. Introduces Auxiliary Cross Attention Network (ACAN) using cross-attention to compute attention weights between agent state (query) and memory bank (key-value pairs), ranking and retrieving most relevant memories. Trained with LLM assistance comparing against WMR baseline via custom loss function. Experiments show ACAN outperforms WMR (avg score 5.94 vs 5.05, p<0.0001) and improves agent behavior consistency (attendance 32.6% vs 24.6%). No explicit entity filtering or re-ranking beyond attention ranking, but combines temporal decay, vector similarity, and LLM importance in baseline.

-----

-----

Phase: [EXPLOITATION]

### Source [46]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory

Query: What hybrid retrieval techniques combining entity filtering, vector similarity, temporal decay, and re-ranking are most effective for pulling relevant items from different long-term memory stores into an agent's context?

Answer: Curated repository on AI memory for LLMs/agents. Describes hybrid retrieval: Semantic Pre-filtering (vector similarity Top-100), Contextual Reranking (query context), Temporal Filtering (recent info). Memory Compression: Content/Representation/Organization-level, Knowledge Distillation. Memory Retrieval: complex process with semantic pre-filtering, contextual reranking, temporal filtering. Lists papers/systems on memory operations (write/retrieve/update/delete/compress), management (lifecycle/conflict/resource/security), classification (access frequency/structure/sharing/temporal), mechanisms (RAG/reflection/routing). Mentions tool-driven memory exploration with multi-indexed DB (string matching/vector similarity). Clinical docs organized as tree with manifests for progressive disclosure navigation. No specific entity filtering but graph/tree structures imply relational filtering.

-----

-----

Phase: [EXPLOITATION]

### Source [47]: https://medium.com/graph-praxis/hybrid-vector-graph-retrieval-patterns-11fdbd800e3e

Query: What hybrid retrieval techniques combining entity filtering, vector similarity, temporal decay, and re-ranking are most effective for pulling relevant items from different long-term memory stores into an agent's context?

Answer: Discusses hybrid vector-graph retrieval for RAG: vector for initial candidates, graph traversal for context expansion. Optimal: vector search + graph (15-30% faithfulness/relevancy gains). Pure vector misses relationships; pure graph misses semantics. Recommends traversal depth limits, re-ranking, caching. Empirical evidence for hybrid superiority. Architecture: FalkorDB with OLAP vector stores. Mentions temporal graphs (T-GRAG) for time-sensitive retrieval addressing temporal ambiguity. No explicit entity filtering but graphs enable relational filtering. Re-ranking post-hybrid crucial.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://aiamastery.substack.com/p/lesson-23-hybrid-search-and-filtering

Query: What hybrid retrieval techniques combining entity filtering, vector similarity, temporal decay, and re-ranking are most effective for pulling relevant items from different long-term memory stores into an agent's context?

Answer: Lesson on hybrid search: vector similarity + keyword/BM25 + metadata filtering + RRF fusion + reranking. Builds production hybrid retriever combining semantic (embeddings), lexical (BM25), structured (SQL-like filters). Reranker (from prior lesson) on diverse candidates. For enterprise VAIA: API Gateway → Query Router → Hybrid Retrieval → Reranker → Context → LLM. Addresses vector missing exact terms/acronyms. No temporal decay but metadata filtering could include time. Re-ranking final stage.

-----

</details>

<details>
<summary>How do importance scoring, memory decay functions, and autonomous consolidation mechanisms help manage scale and relevance in production long-term memory systems for agents?</summary>

Phase: [EXPLOITATION]

### Source [49]: https://tianpan.co/blog/long-term-memory-types-ai-agents

Query: How do importance scoring, memory decay functions, and autonomous consolidation mechanisms help manage scale and relevance in production long-term memory systems for agents?

Answer: Effective retrieval in production AI agent memory systems combines three signals: Relevance (semantic similarity via embedding cosine similarity), Recency (exponential decay based on how recently a memory was created or accessed, with decay factor ~0.995 per hour prioritizing recent memories over older semantically similar ones), and Importance (LLM-scored at write time or inferred from user behavior, e.g., repeated messages indicate higher importance). These are weighted into a retrieval score outperforming similarity-only approaches. Decay downweights memories in retrieval until below threshold (effectively invisible but recoverable), preventing stale info pollution without deletion, preserving correctness. Mirrors Ebbinghaus curve: unaccessed info decays, retrieved info strengthens. Manages scale by keeping stores manageable (e.g., 40% token cost reduction via tiered decay/hot storage), ensures relevance by prioritizing recent/significant memories. Autonomous consolidation implied in separate episodic/semantic/procedural stores with extraction at write time, promoting facts (e.g., episodic 'migrating AWS to GCP' to semantic 'GCP-based infra') for lighter retrieval. Principled forgetting prevents log-like accumulation.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://arxiv.org/html/2603.07670v1

Query: How do importance scoring, memory decay functions, and autonomous consolidation mechanisms help manage scale and relevance in production long-term memory systems for agents?

Answer: Retrieval scores memories by weighted mix of recency (exponential decay), relevance (embedding similarity), and importance (self-assessed integer), improving over cosine similarity. Dual-buffer consolidation: new memories in 'hot' buffer during probation, promoted to long-term after quality checks (re-verification, deduplication, importance scoring), mirroring hippocampal-to-neocortical transfer. Manages scale by probation preventing overflow, ensures relevance via checks. Decay/forgetting needed for scale; unaccessed info decays. At production scale, incorrect reflections persist dangerously; consolidation manages this. Generative Agents pipeline clusters observations into reflections autonomously. Manages scale/relevance by prioritizing significant/recent memories, fading less relevant via decay/consolidation.

-----

-----

Phase: [EXPLOITATION]

### Source [51]: https://dev.to/sudarshangouda/ai-agent-memory-part-2-the-case-for-intelligent-forgetting-4i48

Query: How do importance scoring, memory decay functions, and autonomous consolidation mechanisms help manage scale and relevance in production long-term memory systems for agents?

Answer: Importance scoring initializes memory strength (high=long-term layer slow decay, low=short-term fast decay). Decay via Ebbinghaus curve from last_accessed (retrieval resets clock, spacing effect); rate inversely proportional to importance (critical slow, low fast). Prunes below threshold at search time (time-based, not add-based). FadeMem dual-layer: importance from relevance/access/age; retains critical facts better (82% vs 78%) at 55% storage. Manages scale by natural dropout of unimportant/old memories, prevents bloat/stale noise. Relevance via strength-ranked retrieval (overlap × strength). Autonomous via continuous background decay/prune. Addresses production issues: stale context, retrieval noise, conflicts, storage bloat.

-----

-----

Phase: [EXPLOITATION]

### Source [52]: https://arxiv.org/html/2504.19413v1

Query: How do importance scoring, memory decay functions, and autonomous consolidation mechanisms help manage scale and relevance in production long-term memory systems for agents?

Answer: Mem0 extracts salient memories incrementally, updates via LLM deciding ADD/UPDATE/DELETE/NOOP against similar memories (retrieves top-10 similar), maintaining consistency/relevance without redundancy. Autonomous consolidation: LLM classifies operations based on semantic relations. Graph Mem0 adds entity/relation extraction for relational structure. Manages scale via concise memories (vs full context), low token use. No explicit decay, but update/NOOP prunes irrelevance. Prioritizes important info, outperforming baselines on LOCOMO (e.g., 67% LLM-Judge vs 61% Zep). Handles contradictions (prioritize recent), scale via vector DB similarity search.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/

Query: How do importance scoring, memory decay functions, and autonomous consolidation mechanisms help manage scale and relevance in production long-term memory systems for agents?

Answer: AgentCore Memory extracts via strategies (semantic, preferences, summary), consolidates autonomously: retrieves top similar, LLM decides ADD/UPDATE/NOOP (prioritizes recent for conflicts). No explicit decay mentioned, but consolidation merges/resolves redundancies. Manages scale via compression (89-95%), namespaces for isolation. Retrieval semantic search (~200ms). Production latencies: extraction 20-40s async, parallel strategies. Best practices: monitor consolidation, design namespaces. Ensures relevance by extracting salient facts/preferences, consolidation prevents duplicates/conflicts.

-----

</details>

<details>
<summary>What strategies should AI engineers use to begin with simple memory implementations and iteratively evolve storage and retrieval based on observed agent performance and specific application needs?</summary>

Phase: [EXPLOITATION]

### Source [54]: https://medium.com/@nirdiamant21/memory-optimization-strategies-in-ai-agents-1f75f8180d54

Query: What strategies should AI engineers use to begin with simple memory implementations and iteratively evolve storage and retrieval based on observed agent performance and specific application needs?

Answer: AI engineers should start with simple memory implementations like Sequential (Keep-It-All) for very short interactions (under 10 exchanges) needing perfect recall, such as simple Q&A bots, and Sliding Window for medium-length conversations where recent context matters most, ideal for real-time chat applications or task-focused assistants. For long-form interactions, evolve to Summarization when maintaining context over long conversations with acceptable information loss is needed, like therapy bots, and Retrieval-Based Memory for accurate recall of specific facts over time, perfect for personal assistants. For advanced applications, add Memory-Augmented Transformers for extremely long conversations, Hierarchical Memory Systems for different memory types, and Graph-Based Memory Networks when relationships matter. The decision framework asks: How long are typical interactions? (Short → sliding window, Long → summarization/retrieval); How important is exact recall? (Critical → retrieval/memory-augmented, Flexible → summarization); Resource constraints? (Limited → compression/filtering, Flexible → hierarchical/graph); Do relationships matter? (Yes → graph networks, No → simpler); Will the system learn over time? (Yes → consolidation/temporal awareness); How many users? (Few → sophisticated, Many → efficient compression). The key is starting simple and evolving the memory strategy as the application grows in complexity and user base, using hybrid approaches like Sliding Window + Retrieval for production.

-----

-----

Phase: [EXPLOITATION]

### Source [55]: https://stevekinney.com/writing/agent-memory-systems

Query: What strategies should AI engineers use to begin with simple memory implementations and iteratively evolve storage and retrieval based on observed agent performance and specific application needs?

Answer: For practitioners building memory systems, start with token-level memory using flat (1D) vector stores with a strong retrieval pipeline including hybrid search (BM25 plus semantic embeddings), HyDE for query construction, MMR for diversity, temporal decay for freshness, and aggressive post-retrieval filtering. The StructMemEval benchmark shows simple retrieval outperforms complex hierarchies on standard benchmarks. Move to planar (2D) graphs or hierarchical (3D) structures only when observing specific retrieval failures like multi-hop questions that flat retrieval can't solve. Add experiential memory for learning how problems were solved, starting simple like a strategy store for approaches that worked for error types. Begin flat and evolve based on observed failures. For formation, start with knowledge distillation for facts and semantic summarization for context. For evolution, implement consolidation, updating with conflict detection, and forgetting via time decay or frequency. Retrieval should use timing (retrieve only when needed), query construction (HyDE), hybrid strategy, and post-processing filtering. Iterative retrieval or query expansion for multi-hop, enriching at write time before full graphs.

-----

-----

Phase: [EXPLOITATION]

### Source [56]: https://newsletter.owainlewis.com/p/4-context-engineering-strategies

Query: What strategies should AI engineers use to begin with simple memory implementations and iteratively evolve storage and retrieval based on observed agent performance and specific application needs?

Answer: Start with simple external memory by having the agent write important state to external files like plans or todos (e.g., Claude Code writes plans to disk, TodoWrite for task state), avoiding keeping everything in context. Use just-in-time retrieval: keep references (file paths) and load content only when needed, dynamically loading tool definitions based on task. Compress and prune by summarizing history and deleting stale tool outputs. For complex tasks, isolate with sub-agents each in their own context. These strategies manage context window as RAM, evolving from writing external memory and selective loading for simple agents to compression and multi-agent isolation as performance degrades in long-running tasks.

-----

-----

Phase: [EXPLOITATION]

### Source [57]: https://machinelearningmastery.com/7-steps-to-mastering-memory-in-agentic-ai-systems/

Query: What strategies should AI engineers use to begin with simple memory implementations and iteratively evolve storage and retrieval based on observed agent performance and specific application needs?

Answer: Begin with a conversation buffer and basic vector store as short-term/working memory. Add explicit reasoning scratchpads for multi-step planning when needed. Implement episodic memory for past events via timestamped vector records, semantic for facts/profiles, procedural for rules/workflows. Use hybrid retrieval matching type (semantic for episodic, key lookup for structured). Design around what/where/how/when to store/retrieve/forget, treating context window as constrained resource with prioritization and filtering. Implement agent-controlled retrieval as a tool inside the loop. Evolve by evaluating memory metrics (retrieval accuracy, relevance, latency) and production feedback; add graph-based long-term memory only when relationships bottleneck retrieval. Monitor growth, prune with decay/TTL, use frameworks like Mem0, Letta. Premature complexity slows teams—start simple, iterate based on observed failures.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What recent advances in continual learning for neural networks offer potential pathways beyond current external memory workarounds for agent personalization and adaptation?</summary>

Phase: [EXPLORATION]

### Source [58]: https://arxiv.org/html/2603.01761v1

Query: What recent advances in continual learning for neural networks offer potential pathways beyond current external memory workarounds for agent personalization and adaptation?

Answer: The paper 'Modular Memory is the Key to Continual Learning Agents' proposes a modular memory framework combining In-Weight Learning (IWL) and In-Context Learning (ICL) to enable continual adaptation without external memory workarounds. It argues that foundation models make modular continual learning feasible, leveraging ICL for rapid adaptation via working and long-term memory modules, and IWL for stable core model updates. The framework includes a core model for perception/reasoning, working memory for current context, and long-term memory for facts/experiences with retrieval, updating, forgetting, and consolidation. Advances in ICL (Yin et al., 2024; Lampinen et al., 2025) and reasoning with external knowledge (Luo et al., 2025) enable this. Memory representations include slot-based (raw data, embeddings like KV caches) and distributed neural memories, with desiderata like per-item storage efficiency, capacity, modality, update speed, selective forgetting, retrieval, transferability, and generalization. Operations cover addition, forgetting, retrieval, and core consolidation. This addresses limitations of external memory (unbounded growth, compression loss) and frozen models, enabling personalization, adaptation to shifts, and efficiency in domains like embodied agents where learnable memory updates object relations. Opportunities include faster adaptation, hallucination reduction, explainability, personalization, and world modeling.

-----

-----

Phase: [EXPLORATION]

### Source [59]: https://arxiv.org/abs/2511.01093

Query: What recent advances in continual learning for neural networks offer potential pathways beyond current external memory workarounds for agent personalization and adaptation?

Answer: The paper introduces ATLAS, an Adaptive Teaching and Learning System achieving gradient-free continual learning for agents by decoupling reasoning (Teacher) from execution (Student) with persistent learning memory storing distilled guidance. This shifts adaptation from model parameters to system-level orchestration, maximizing task success while minimizing compute via inference-time strategies like supervision adjustment. On ExCyTIn-Bench (cyberthreat investigation), ATLAS with GPT-5-mini achieves 54.1% success, outperforming GPT-5 (High) by 13% at 86% less cost. Cross-incident validation shows generalization: frozen pamphlets from one incident boost accuracy 28%→41% without retraining, shifting verbose exploration to structured reasoning. This provides pathways beyond external memory by internalizing experience via dual-agent architecture and orchestration, enabling real-time adaptation for deployable agents.

-----

-----

Phase: [EXPLORATION]

### Source [60]: https://arxiv.org/html/2109.11369v4

Query: What recent advances in continual learning for neural networks offer potential pathways beyond current external memory workarounds for agent personalization and adaptation?

Answer: The survey 'Recent Advances of Continual Learning in Computer Vision' categorizes methods beyond external memory workarounds: regularization (EWC, SI, MAS constraining updates), knowledge distillation (LwF distilling prior knowledge), generative replay (DGR generating past data), parameter isolation (PackNet, PathNet task-specific subnetworks), and hybrids. Recent advances include orthogonal gradient projection (Gradient Projection Memory projecting new gradients orthogonal to prior task spaces), prompt tuning with orthogonal gradients, Hebbian projections for spiking networks, and utility-based perturbed gradient descent. These enable internal adaptation without replay buffers, addressing agent personalization via stable plasticity balance. Performance comparisons show strong results in image classification, semantic segmentation, object detection, person re-ID without external storage reliance.

-----

-----

Phase: [EXPLORATION]

### Source [61]: https://cameronrwolfe.substack.com/p/rl-continual-learning

Query: What recent advances in continual learning for neural networks offer potential pathways beyond current external memory workarounds for agent personalization and adaptation?

Answer: Recent RLHF/RLVR advances show on-policy RL naturally mitigates catastrophic forgetting better than SFT in continual post-training, via low-KL distributional shift bias (RL's Razor). Papers like 'Reinforcement Finetuning Naturally Mitigates Forgetting' demonstrate RL (GRPO) achieves near multi-task performance without replay, unlike SFT causing severe forgetting. 'Retaining by Doing' confirms on-policy data key, equating RL to reverse KL (mode-seeking) vs SFT forward KL (mode-covering). 'RL's Razor' proves KL divergence on target data predicts forgetting, RL biases low-shift solutions. Architectural extensions like LoRA modules or MoE aid without external memory. Pathways for agent adaptation: RL enables personalization via conservative updates preserving general capabilities while adapting to new tasks/domains.

-----

</details>

<details>
<summary>What are the nuanced trade-offs in using LLM-based extraction pipelines for creating structured semantic and episodic memories, particularly regarding information loss, extraction accuracy, and drift over extended interactions?</summary>

Phase: [EXPLORATION]

### Source [62]: https://arxiv.org/html/2601.04170v1

Query: What are the nuanced trade-offs in using LLM-based extraction pipelines for creating structured semantic and episodic memories, particularly regarding information loss, extraction accuracy, and drift over extended interactions?

Answer: LLM-based extraction pipelines for agent memories face significant trade-offs in multi-agent systems over extended interactions. Key issues include behavioral drift, where decision-making deviates from initial specifications without parameter changes, manifesting as semantic drift (deviation from intent), coordination drift (consensus breakdown), and behavioral drift (unintended strategies). Context window pollution occurs as histories grow with irrelevant early information, diluting relevant context and degrading quality; episodic memory consolidation mitigates by pruning stale data. Distributional shift arises from deployment in narrow domains diverging from training data, accelerating drift in specialized areas like financial analysis. Reinforcement through autoregression creates feedback loops amplifying errors. Agent Stability Index (ASI) quantifies drift across 12 dimensions, showing early onset (median 73 interactions), compounding effects, and domain variation. Performance degrades: task success -42%, accuracy -25%, interventions +216%. Mitigation via episodic consolidation, drift-aware routing, and anchoring reduces drift 51-81%, but increases overhead 9-23%. Trade-offs: higher reliability vs. throughput cost; drift monitoring requires instrumentation; short testing misses 75% cases. Information loss from pollution and shift; accuracy declines progressively; drift accumulates over interactions without intervention.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://arxiv.org/html/2603.11768v1

Query: What are the nuanced trade-offs in using LLM-based extraction pipelines for creating structured semantic and episodic memories, particularly regarding information loss, extraction accuracy, and drift over extended interactions?

Answer: LLM-based extraction pipelines for evolving agent memories incur nuanced trade-offs in stability, validity, efficiency, and safety. Semantic drift from lossy iterative summarization distorts ground truth, e.g., mild preferences intensify via re-encoding, measured as embedding divergence δ(M_T, K_true)=1-sim(E(M_T),E(K_true)). Procedural drift reinforces suboptimal workflows; goal drift shifts alignment via bias accumulation. Validity failures: hallucinations store fabrications; obsolescence from stale data. Efficiency: latency scales with history; bloat from redundant logs. Safety: poisoning via injections; leakage in multi-agent. Trade-offs: latency-safety (verification slows writes); stability-plasticity (filtering ossifies knowledge); graph scalability. SSGM framework decouples evolution from governance via validation gates, temporal decay w(Δτ)=exp(-(Δτ/η)^κ), access controls, dual mutable/immutable tracks. Bounded drift theorem: O(N⋅ε_step) vs. naive O(T⋅ε_step). Information loss via compression; accuracy via drift/hallucination; drift over interactions from unchecked updates.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://arxiv.org/html/2512.19537v1

Query: What are the nuanced trade-offs in using LLM-based extraction pipelines for creating structured semantic and episodic memories, particularly regarding information loss, extraction accuracy, and drift over extended interactions?

Answer: LLM-based extraction pipelines using event extraction (EE) for structured semantic/episodic memories address LLM limitations: hallucinations without constraints, fragile long-context linking, context window bounds. EE provides cognitive scaffold: schemas/slots for grounding/verification (reduces loss/accuracy issues); chains for stepwise reasoning (reproducibility); links for graph-RAG (beyond similarity); updatable stores for episodic memory (long-horizon planning). Trade-offs: generative probabilistic outputs risk accumulation; dispersed evidence causes linking failures; similarity retrieval misses relations. EE evolves from prediction to system interface: explicit/constrained/computable outputs as intermediates/external memories. In LLM era, EE mitigates cognitive gaps but requires structured complements for reliability over end-to-end generation. Information loss minimized by schemas; accuracy via verification; drift countered by event graphs.

-----

</details>

<details>
<summary>How have memory architectures from autonomous robotics and embodied AI systems influenced the design of procedural and episodic memory in modern LLM-based conversational agents?</summary>

Phase: [EXPLORATION]

### Source [65]: https://arxiv.org/pdf/2603.07670

Query: How have memory architectures from autonomous robotics and embodied AI systems influenced the design of procedural and episodic memory in modern LLM-based conversational agents?

Answer: The paper 'Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers' discusses memory architectures in LLM agents, drawing from cognitive science models like Baddeley’s working memory model. It defines episodic memory as records of concrete experiences (tool calls, observations) and procedural memory as reusable skills and plans, exemplified by Voyager’s skill library in Minecraft, an embodied game agent. Game agents require tight integration of episodic (what happened) and procedural memory (what to do). JARVIS-1 extends hierarchical memory to multimodal settings with stores for visual observations (embodied), textual plans, and executable skills. Cognitive Architectures for Language Agents proposes working, episodic, semantic, and procedural stores interacting via LLM executive, echoing Baddeley. Hierarchical virtual context like MemGPT pages data between tiers. Open challenges include multimodal embodied memory for robotics fusing text, vision, proprioception. Autonomous robotics influences via embodied agents like Voyager and JARVIS-1, inspiring episodic-procedural integration and multimodal hierarchies in LLM conversational agents for adaptability and skill reuse.

-----

-----

Phase: [EXPLORATION]

### Source [66]: https://arxiv.org/html/2603.07670v1

Query: How have memory architectures from autonomous robotics and embodied AI systems influenced the design of procedural and episodic memory in modern LLM-based conversational agents?

Answer: Similar to the PDF, this HTML version covers the same content. Voyager in Minecraft (embodied agent) uses procedural skill library for executable plans. Game agents integrate episodic and procedural memory. JARVIS-1 for multimodal embodied settings with visual, textual, skills stores. Cognitive architectures mirror human memory types. Influences from embodied AI like robotics-inspired hierarchies and multimodal memory for LLM agents' procedural/episodic designs.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/

Query: How have memory architectures from autonomous robotics and embodied AI systems influenced the design of procedural and episodic memory in modern LLM-based conversational agents?

Answer: Article on memory systems: episodic (events, sequential experiences), procedural (operational skills, execution). Frameworks like LangMem for procedural learning. Mentions Voyager (Minecraft embodied agent) implicitly via skill libraries. Discusses embodied settings but no explicit robotics influence on LLM conversational agents. Focuses on tripartite model (episodic, semantic, procedural) for long-term memory in agents.

-----

</details>

<details>
<summary>What design principles from personal knowledge management tools such as Roam Research, Obsidian, or Memex-inspired systems can inform effective semantic, episodic, and procedural memory architectures for AI personal companions?</summary>

Phase: [EXPLORATION]

### Source [70]: https://www.emotionmachine.com/blog/how-memory-works

Query: What design principles from personal knowledge management tools such as Roam Research, Obsidian, or Memex-inspired systems can inform effective semantic, episodic, and procedural memory architectures for AI personal companions?

Answer: The Emotion Machine blog post discusses three memory architectures for AI companions: pgvector-backed semantic memory (V1), ChatGPT-style scratchpad (V2), and filesystem-based context (V3). It frames memory through cognitive science: working memory (context window), semantic memory (facts), episodic memory (experiences), procedural memory (instructions/skills). These map to systems built, with pragmatic naming like 'scratchpad' or 'hot context'. Key principles include asynchronous ingestion via Modal workers (invisible to conversation), layered context assembly (core prompt, memory, knowledge, tools in parallel), and separation of personal memory from knowledge base (OpenAI vector store for documents). V1 uses importance scoring and two-stage retrieval; V2 maintains curated semantic entries injected every turn; V3 materializes context as files in /em/ for agent navigation. No direct mention of Roam Research, Obsidian, or Memex, but filesystem approach echoes file-based PKM tools. Influences effective architectures via cognitive abstractions, async processing, and pluggable layers for semantic (facts), episodic (scratchpad), procedural (behaviors/tools). (198 words)

-----

-----

Phase: [EXPLORATION]

### Source [71]: https://arxiv.org/html/2604.04853v1

Query: What design principles from personal knowledge management tools such as Roam Research, Obsidian, or Memex-inspired systems can inform effective semantic, episodic, and procedural memory architectures for AI personal companions?

Answer: MemMachine is a ground-truth-preserving memory system for personalized AI agents with short-term memory (STM: current context), long-term episodic memory (specific experiences), semantic/profile memory (high-level facts/preferences), and extensible procedural memory (skills/strategies). Architecture: REST API/SDK/MCP interfaces; storage via PostgreSQL/pgvector/SQLite/Neo4j. Episodic memory preserves raw records for factual accuracy; semantic distills patterns like 'user prefers vegetarian'. Data ingestion segments episodes into sentences for fine-grained indexing. Retrieval uses contextualized nucleus expansion (neighboring episodes) and reranking. Profile memory extracts structured attributes. No explicit PKM tool mentions, but sentence-level chunking and graph storage parallel Obsidian's atomic notes/links. Informs AI memory via multi-tier (STM/LTM), ground-truth preservation (episodic), distillation (semantic), and procedural extensibility, emphasizing when to use each for personalization without LLM extraction errors. (187 words)

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://www.analyticsvidhya.com/blog/2026/04/memory-systems-in-ai-agents/

Query: What design principles from personal knowledge management tools such as Roam Research, Obsidian, or Memex-inspired systems can inform effective semantic, episodic, and procedural memory architectures for AI personal companions?

Answer: Article on memory architectures for AI agents: short-term (working context), long-term tripartite (episodic: events; semantic: facts via RAG/vector DBs; procedural: skills/workflows). Asynchronous consolidation extracts structured facts from episodic history. Intelligent forgetting uses TTL tiers, refresh-on-read, importance scoring. Conflict resolution via temporal weighting, semantic merging. Compares frameworks: Mem0 (compression/personalization), Zep (temporal KG), LangMem (procedural). No Roam/Obsidian/Memex mentions, but multi-DB approach (relational for episodic, vector for semantic, KV for procedural) echoes PKM hybrid storage. Principles: cognitive compression, decay-aware ecosystems, layered access controls inform AI memory via separate stores, async processing, forgetting policies for semantic (facts), episodic (experiences), procedural (skills) scalability. (162 words)

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://medium.com/@zmarandos/where-ai-ends-and-i-begin-0d6e8be4e00f

Query: What design principles from personal knowledge management tools such as Roam Research, Obsidian, or Memex-inspired systems can inform effective semantic, episodic, and procedural memory architectures for AI personal companions?

Answer: Personal PKM system using Obsidian (local markdown, linked notes) with Claude Code. Vault structure: Fleeting (raw), Reference (annotations), Permanent (atomic insights, human-only). AI assists organization/search/triage but cannot create permanent notes. Principles: minimal folders (links structure), no hoarding, leverage LLM strengths (backlinking, surfacing connections). Separate operational (Notion) from knowledge hub. Exploratory vaults for AI-generated research maps. Echoes Zettelkasten. Informs AI via human-AI boundaries (permanent human-written), link-based structure over folders (graph memory), pragmatic AI use (search/suggest), curation over collection for semantic (facts/insights), episodic (fleeting/reference). (148 words)

-----

-----

Phase: [EXPLORATION]

### Source [74]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory

Query: What design principles from personal knowledge management tools such as Roam Research, Obsidian, or Memex-inspired systems can inform effective semantic, episodic, and procedural memory architectures for AI personal companions?

Answer: Curated repo on AI/LLM memory: surveys, papers, benchmarks, systems. Core concepts: explicit (vector/graph DBs), parametric (weights), short/long-term, episodic/semantic/procedural. Operations: write/retrieve/update/delete/compress. No direct Roam/Obsidian/Memex, but graph DBs/KG parallel Obsidian links; Zettelkasten-inspired systems noted. Systems like Mem0/Zep/LangMem/MemGPT emphasize layered (STM/LTM), cognitive-inspired (episodic facts/skills). Benchmarks: LoCoMo/LongMemEval for long-term. Informs via multi-type separation, lifecycle mgmt, PKM-like curation (forgetting/decay). (112 words)

-----

</details>

<details>
<summary>What empirical evidence exists on how different memory consolidation schedules (e.g., immediate vs. batched offline processing) impact the accuracy of semantic and episodic recall in long-running agent deployments exceeding 1000 interactions?</summary>

Phase: [EXPLORATION]

### Source [75]: https://dr.lib.iastate.edu/bitstreams/a6058084-7b84-48dc-88e4-42813c785d8c/download

Query: What empirical evidence exists on how different memory consolidation schedules (e.g., immediate vs. batched offline processing) impact the accuracy of semantic and episodic recall in long-running agent deployments exceeding 1000 interactions?

Answer: CRAM (Consolidation-based Routing for Adaptive Memory) implements biologically inspired memory consolidation that gradually distills episodic retrievals (attention-based) into parametric semantic memory. Empirical results show a sharp phase transition at ~3K training steps where attention usage drops 37.8× from moderate levels to 1.6% while achieving 100% retrieval accuracy on SRCD benchmark (vs. 68% for baselines like Transformer, SeqBoat). This demonstrates immediate consolidation during training outperforms static/batched approaches, as proven by Theorem 1 showing static routing requires Ω(f·n) attention for recurring patterns. Learned dynamics quantitatively match human episodic-to-semantic transition (power law exponent γ=0.43 vs. human 0.4–0.5). Transfer tests show 48–52% attention reduction on unseen tasks without retraining. Training exceeds 10K steps (>1000 interactions equivalent). No direct immediate vs. batched comparison, but phase transition implies online consolidation critical for long-term retention. Semantic memory quality qt triggers routing shift when crossing ~0.83 threshold.

-----

-----

Phase: [EXPLORATION]

### Source [76]: https://arxiv.org/html/2404.00573v1

Query: What empirical evidence exists on how different memory consolidation schedules (e.g., immediate vs. batched offline processing) impact the accuracy of semantic and episodic recall in long-running agent deployments exceeding 1000 interactions?

Answer: No direct empirical evidence on immediate vs. batched consolidation schedules. Paper focuses on human-like memory architecture with mathematical model for dynamic consolidation considering contextual relevance, elapsed time, and recall frequency. Model replicates spaced repetition effect: memories recalled repeatedly over long periods retained more strongly than frequent short-term recalls (citing Roediger & Karpicke 2006). Quantitative evaluation on 10 tasks shows statistically significant lower loss (t=-5.687, p=0.000299) vs. Generative Agents, indicating superior recall accuracy. Qualitative evaluation over 1 week to 3 months conversations with 6 participants shows accurate recall of personal habits/preferences. Memory stored/recalled autonomously via cued recall trigger when p(t) exceeds threshold 0.86. No interaction counts >1000 or schedule comparison. Batched processing absent; consolidation continuous via recall frequency updating decay constant a=1/gn where gn increases with spaced recalls.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory

Query: What empirical evidence exists on how different memory consolidation schedules (e.g., immediate vs. batched offline processing) impact the accuracy of semantic and episodic recall in long-running agent deployments exceeding 1000 interactions?

Answer: No direct comparison of immediate vs. batched schedules. Curated list of 300+ papers/systems on AI/LLM memory. Relevant: CRAM (immediate consolidation during training, 37.8× attention reduction post-3K steps, 100% accuracy SRCD benchmark >10K steps). OBLIVION (decay-driven activation, hierarchical L1-L3, balances learning/forgetting long-horizon). MemFactory (unified inference/training, GRPO fine-tuning). MemVerse (parametric + hierarchical retrieval, multimodal lifelong). MemInsight (autonomous augmentation). MemSifter (proxy reasoning offload). No explicit >1000 interaction deployments or schedule ablation studies. Benchmarks like LoCoMo (long-horizon), MemoryArena (multi-session), LifeBench (multi-source) evaluate long-term but not schedules.

-----

</details>

<details>
<summary>How do variations in entity resolution accuracy during JSON-structured memory creation affect downstream personalization quality and error propagation in production personal assistant agents?</summary>

Phase: [EXPLORATION]

### Source [80]: https://www.mdpi.com/2306-5729/11/4/66

Query: How do variations in entity resolution accuracy during JSON-structured memory creation affect downstream personalization quality and error propagation in production personal assistant agents?

Answer: The provenance graph representation in AgentSec enables reconstruction of causal chains across reasoning and action steps, supporting downstream analyses of faithfulness, error propagation, and decision reversibility. This structured entity-relation model connects user interactions, decision traces, tool calls, memory updates, and assistant responses with explicit causal relations like 'triggered', 'caused', 'derived from', and 'used by'. Such provenance supports auditing tasks including detecting unsupported reasoning steps, identifying missing dependencies, or analyzing propagation of faulty tool responses through the decision trace. All interaction components are recorded as structured traces forming a sequential log that mirrors temporal execution, ensuring intermediate reasoning steps, side effects, and final responses remain observable and auditable. The dataset captures scenarios with memory conflicts, overwrites, and provenance branching, enabling study of error propagation in agent memory updates. Validation tools and schema ensure structural consistency for reliable downstream analyses of agent behavior, reasoning fidelity, and causal accountability.

-----

-----

Phase: [EXPLORATION]

### Source [81]: https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter8/Chapter8-Memory-and-Retrieval.md

Query: How do variations in entity resolution accuracy during JSON-structured memory creation affect downstream personalization quality and error propagation in production personal assistant agents?

Answer: Current large language models are stateless, leading to context loss, lack of personalization, limited learning ability, and consistency issues in multi-turn conversations. The memory system addresses this with a four-layer architecture: WorkingMemory (temporary, TTL-managed), EpisodicMemory (events, SQLite+Qdrant), SemanticMemory (knowledge graphs, Qdrant+Neo4j), and PerceptualMemory (multimodal). Semantic memory addition extracts entities and relationships to build structured knowledge representations, where entity resolution accuracy directly impacts knowledge graph quality and downstream personalization. Retrieval uses hybrid strategies combining vector similarity, graph reasoning, and importance weighting, with scoring formulas like (vector × 0.7 + graph × 0.3) × (0.8 + importance × 0.4). Errors in entity resolution propagate through memory types, affecting consolidation (working → episodic → semantic) and forgetting strategies, ultimately degrading agent personalization quality and response consistency.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://arxiv.org/pdf/2506.13839

Query: How do variations in entity resolution accuracy during JSON-structured memory creation affect downstream personalization quality and error propagation in production personal assistant agents?

Answer: Entity resolution accuracy critically impacts data quality for AI applications, particularly when linking heterogeneous sources without unique identifiers. Poor resolution leads to incorrect entity matches, propagating errors through AI systems and causing harms like biased outcomes or privacy breaches. In production, variations in accuracy affect downstream personalization by creating inconsistent entity profiles, while error propagation occurs through causal chains in provenance graphs. Standards for entity resolution should address preprocessing (cleaning, standardization), model evaluation (precision/recall tradeoffs), and secure linkage to mitigate risks. Key AI actors (data scientists, domain experts) must inform standards for data preparation and bias mitigation, ensuring high-quality linked data for reliable personalization in personal assistant agents. Failure to resolve entities correctly results in poor-quality learning/employment records, disproportionately affecting marginalized groups.

-----

-----

Phase: [EXPLORATION]

### Source [83]: https://link.springer.com/article/10.1007/s44206-025-00232-4

Query: How do variations in entity resolution accuracy during JSON-structured memory creation affect downstream personalization quality and error propagation in production personal assistant agents?

Answer: Personalized Privacy Assistants (PPAs) require high entity resolution accuracy for accurate inferences about user preferences, directly affecting personalization quality. Variations in accuracy during memory creation (e.g., JSON-structured user data) propagate errors, leading to incorrect privacy decisions and reduced agency. Hybrid PPAs (manual-automated) are preferred, but accuracy concerns arise from implicit data use, risking biased profiles. Experts emphasize human-in-the-loop validation, explicit user preferences over inferred data, and oversight to prevent error propagation. Accountability requires transparency in entity resolution processes, with multistakeholder involvement (regulators, developers) to ensure compliance. Poor resolution undermines GDPR principles of accuracy and accountability, impacting downstream personalization in agents.

-----

-----

Phase: [EXPLORATION]

### Source [84]: https://developers.openai.com/cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents

Query: How do variations in entity resolution accuracy during JSON-structured memory creation affect downstream personalization quality and error propagation in production personal assistant agents?

Answer: Temporal agents build knowledge graphs from JSON-structured memory, where entity resolution accuracy ensures correct triplet extraction (subject-predicate-object). Poor accuracy propagates errors through invalidation agents, affecting temporal validity and downstream retrieval quality. Multi-hop retrieval over graphs requires precise entity linking; variations lead to missed relationships and degraded personalization. Production safeguards include output validation, structured logging, and monitoring for data drift. Relevance scoring and pruning prevent error accumulation in large graphs. Hybrid tools balance fixed (rigid queries) and free-form (flexible) retrieval, with model selection (o3 → o4-mini → GPT-4.1) optimizing accuracy vs. latency. Evaluation uses golden answers and synthetic evals to measure propagation impact on agent performance.

-----

</details>

<details>
<summary>What are the measurable effects of combining procedural memory with ReAct reasoning loops on reducing planning iterations and tool misuse rates in agentic workflows?</summary>

Phase: [EXPLORATION]

### Source [85]: https://arxiv.org/html/2602.20867v1

Query: What are the measurable effects of combining procedural memory with ReAct reasoning loops on reducing planning iterations and tool misuse rates in agentic workflows?

Answer: Skills are a form of procedural memory that encode how to act, compressing learned procedures into reusable modules that reduce cognitive load on the model’s context window. Without a skill layer, every task requires reasoning from first principles, consuming tokens to re-derive procedures. Curated skills raise agent pass rates by 16.2 percentage points on average in SkillsBench, while self-generated skills degrade performance by 1.3 pp. A smaller model with curated skills outperforms a larger model without them. Procedural memory serves as an efficiency multiplier. Plans are one-time and not executable; skills persist across sessions with executable policies. ReAct is referenced in hybrid skills and execution patterns, but combining procedural memory with ReAct loops is implied in reducing reasoning tax and improving efficiency in agentic workflows by reusing procedures instead of iterative reasoning from scratch.

-----

-----

Phase: [EXPLORATION]

### Source [86]: https://arxiv.org/html/2508.06433v2

Query: What are the measurable effects of combining procedural memory with ReAct reasoning loops on reducing planning iterations and tool misuse rates in agentic workflows?

Answer: MempMem^p explores agent procedural memory, distilling trajectories into instructions and abstractions. On ALFWorld and TravelPlanner, procedural memory reduces steps and boosts success rates. Proceduralization (trajectories + scripts) yields optimal performance, e.g., GPT-4o: 87.14% dev, 77.86% test on ALFWorld vs. no memory 42.14%. Memory update strategies like reflexion improve performance linearly over tasks, reducing steps by 14. Agents with procedural memory cut fruitless exploration, directly addressing planning iterations and tool misuse by reusing verified procedures instead of ReAct-style trial-and-error. Transfer from strong to weak models boosts weaker agents substantially.

-----

</details>

<details>
<summary>How have memory management techniques from distributed systems consensus protocols been adapted to ensure consistency in multi-session AI agent memory stores?</summary>

Phase: [EXPLORATION]

### Source [89]: https://arxiv.org/pdf/2601.05569

Query: How have memory management techniques from distributed systems consensus protocols been adapted to ensure consistency in multi-session AI agent memory stores?

Answer: The paper introduces SEDMA (Self-Evolving Distributed Memory Architecture), a framework for coordinated memory management across computation, communication, and deployment layers in distributed AI systems. It features a dual memory system with long-term episodic memory tracking performance patterns and short-term working memory for workload statistics. Memory-guided matrix processing dynamically partitions RRAM computations using historical strategies from long-term memory and current statistics from short-term memory. Adaptive distributed communication uses memory-aware peer selection, storing peer performance profiles in long-term memory and current loads in short-term memory for optimal routing. Dynamic deployment optimization recompiles configurations based on runtime memory patterns. While not explicitly from consensus protocols, it employs distributed hash tables (DHTs) and peer-to-peer mechanisms akin to distributed systems, with memory ensuring consistency across heterogeneous environments. Experiments show 87.3% memory utilization efficiency. No direct mention of consensus protocols like Paxos or Raft, but coordinated optimization across layers maintains consistency in multi-session distributed AI agent deployments.

-----

-----

Phase: [EXPLORATION]

### Source [90]: https://medium.com/@cauri/memory-in-multi-agent-systems-technical-implementations-770494c0eca7

Query: How have memory management techniques from distributed systems consensus protocols been adapted to ensure consistency in multi-session AI agent memory stores?

Answer: The article discusses technical implementations for memory in multi-agent systems, directly adapting distributed systems techniques for consistency. CRDTs (Conflict-free Replicated Data Types) from distributed systems consensus ensure eventual consistency without locking, allowing multiple agents to write independently to shared memory stores. Different memory types use tailored CRDT implementations. CQRS (Command Query Responsibility Segregation) separates write and read models, optimizing for multi-agent operations with intent-based commands and multiple projections for query patterns, integrating with event sourcing. These handle conflicts in multi-session scenarios where agents share persistent memory. Event sourcing captures reasoning behind writes for retrospective analysis. Semantic conflict resolution uses arbiter agents for coherent reconciliations considering intent. Model Context Protocol (MCP) enables natural language database operations across agents. RAG for episodic/semantic memory with pgvector. Distillation compresses conversations into high-signal representations stored appropriately. These ensure consistency in multi-session AI agent memory stores via distributed consensus-inspired techniques.

-----

-----

Phase: [EXPLORATION]

### Source [91]: https://link.springer.com/article/10.1007/s44163-026-00992-z

Query: How have memory management techniques from distributed systems consensus protocols been adapted to ensure consistency in multi-session AI agent memory stores?

Answer: The paper proposes 'memory fabric' for shared, persistent multiuser memory in conversational AI agents. Provenance and consistency mechanisms maintain reliability using CRDTs (Conflict-free Replicated Data Types) for eventual consistency in distributed memory, reconciling writes order-agnostically even for concurrent multi-agent updates. CRDT principles guide shared conversational memory design. Graph-structured memory with provenance tracks origins, modifications, and confidence via knowledge graphs for merging, conflict detection, and reasoning in multi-user contexts. Privacy via differential privacy, encryption, role-based access, and lifecycle management. Benchmarks like LoCoMo and MADial-Bench evaluate long-term multi-session memory. Reviews architectures like NTMs, DNCs, Key-Value Memory Networks, AutoGen, AgentVerse, SRMT for multi-agent shared memory. Dynamic allocation, pruning, and indexing prevent overload. Ensures consistency across multi-session AI agent stores adapting distributed consensus techniques.

-----

</details>

<details>
<summary>What evaluation benchmarks and metrics beyond LOCOMO are used to assess the long-term coherence and personalization effectiveness of agent memory systems in real-world multi-month deployments?</summary>

Phase: [EXPLORATION]

### Source [92]: https://www.emergentmind.com/topics/locomo-and-perltqa

Query: What evaluation benchmarks and metrics beyond LOCOMO are used to assess the long-term coherence and personalization effectiveness of agent memory systems in real-world multi-month deployments?

Answer: LoCoMo and PerLTQA are benchmarks for evaluating long-term memory, retrieval, and reasoning in agent systems. Beyond LOCOMO, PerLTQA evaluates QA grounded in lifelong personal memory, distinguishing semantic (profiles, relationships) and episodic memory (events, dialogues). Metrics include: Memory Classification (F1, accuracy); Memory Retrieval (BM25, DPR, Contriever, MAP); Memory Synthesis (BLEU, ROUGE-L, coherency, correctness). LoCoMo uses QA (F1, Recall@k), Event Summarization (FactScore, ROUGE), Multimodal Generation (BLEU, ROUGE-L, MM-Relevance). These assess multi-session dialogues (avg. 19.3 sessions, 304 turns) for coherence and personalization via hierarchical retrieval efficiency and multi-hop reasoning.

-----

-----

Phase: [EXPLORATION]

### Source [93]: https://vectorize.io/articles/best-ai-agent-memory-systems

Query: What evaluation benchmarks and metrics beyond LOCOMO are used to assess the long-term coherence and personalization effectiveness of agent memory systems in real-world multi-month deployments?

Answer: LongMemEval is a benchmark beyond LOCOMO for assessing long-term coherence and personalization in agent memory systems, evaluating retrieval from long conversational histories. It tests single/multi-session user/assistant info, preferences, knowledge updates, temporal reasoning. Used by frameworks like Hindsight (91.4%), SuperMemory (81.6%), Mem0 (49%). Notes limitations: focuses on conversational data, lacks task execution evaluation for real-world multi-month deployments. Calls for new benchmarks measuring task performance improvement over time (fewer errors, faster ramp-up).

-----

-----

Phase: [EXPLORATION]

### Source [94]: https://supermemory.ai/research/

Query: What evaluation benchmarks and metrics beyond LOCOMO are used to assess the long-term coherence and personalization effectiveness of agent memory systems in real-world multi-month deployments?

Answer: LongMemEval is used beyond LOCOMO to evaluate agent memory, spanning 500 questions in 6 categories: single-session-user/assistant/preference, knowledge-update, temporal-reasoning, multi-session. Assesses information extraction, multi-session reasoning, knowledge updates, temporal reasoning. Supermemory achieves SOTA (81.6% gpt-4o, 85.2% gemini-3-pro) vs Zep (71.2%), full-context (60.2%). LLM-as-Judge evaluation. LongMemEval_s tests human-assistant interactions approximating real-world chat history, challenging retrieval, reasoning over time, noise filtering.

-----

-----

Phase: [EXPLORATION]

### Source [95]: https://openreview.net/pdf/0b178c4aed95d526dfbfd9b52a535f4dc2bbc4bd.pdf

Query: What evaluation benchmarks and metrics beyond LOCOMO are used to assess the long-term coherence and personalization effectiveness of agent memory systems in real-world multi-month deployments?

Answer: LoCoMo-Plus extends beyond factual LOCOMO for cognitive memory evaluation in long-term conversational settings. Assesses beyond-factual cognitive memory (causal, state, goal, value constraints) under cue-trigger semantic disconnect. Uses constraint-consistency framework: unified conversational queries (no task disclosure), LLM-as-judge for valid response space membership. Metrics critique: rejects BLEU/ROUGE/F1/EM due to length/style bias; favors judge reliability (high human/LLM agreement). Reveals performance drops (e.g., GPT-4o 62% factual to 42% cognitive), length sensitivity in cognitive tasks.

-----

-----

Phase: [EXPLORATION]

### Source [96]: https://openreview.net/pdf/e5155034533dbd9688b6b90fb4c0a60980fcfa4c.pdf

Query: What evaluation benchmarks and metrics beyond LOCOMO are used to assess the long-term coherence and personalization effectiveness of agent memory systems in real-world multi-month deployments?

Answer: Memora benchmark evaluates long-term memory for personalized agents over weeks/months/quarters (up to 1991 sessions). Tasks: remembering, reasoning, recommending grounded in evolving memory (preferences, activities, goals). Metrics: Forgetting-Aware Memory Accuracy (FAMA) = MPA - λ(1-FAA), penalizes obsolete memory use; memory presence/forgetting absence via multi-LLM judges. Stresses consolidation (avg 17+ sessions), mutation (up to 14.8 updates). Exposes failures in LLMs/agents (e.g., reasoning FAMA ~5-30%), reuse of invalid memories, partial retrieval.

-----

</details>

<details>
<summary>What LLM-driven techniques for autonomous memory auditing, contradiction flagging, and self-correction have proven effective in maintaining semantic and episodic store integrity over thousands of interactions?</summary>

Phase: [EXPLORATION]

### Source [97]: https://openreview.net/pdf?id=0xfDgpPaNJ

Query: What LLM-driven techniques for autonomous memory auditing, contradiction flagging, and self-correction have proven effective in maintaining semantic and episodic store integrity over thousands of interactions?

Answer: HiMem proposes a hierarchical long-term memory framework with Episode Memory (immutable episodic records via Topic-Aware Event–Surprise Dual-Channel Segmentation) and Note Memory (stable knowledge via multi-stage extraction). Key LLM-driven technique: conflict-aware Memory Reconsolidation. Triggered by retrieval failure from Note Memory when Episode Memory provides evidence, it performs query-conditioned knowledge extraction from episodes, classifies new info vs. existing notes as independent (ADD), extendable (UPDATE), or contradictory (DELETE), applying typed operations to revise Note Memory. This enables self-correction and evolution, echoing belief revision (Gärdenfors, 1988). Episodic memory remains immutable for temporal integrity. Conservative feedback loop: retrieval failure → episodic inspection → targeted supplementation. Ablations show self-evolution improves Note Memory by 5.85% GPT-Score. Essential for semantic consistency over long-term interactions (LoCoMo benchmark: up to 32 stages, 600 turns/session). Outperforms baselines in accuracy/consistency (80.71% overall GPT-Score). Hierarchical retrieval (Note-first, fallback to Episode) balances efficiency/accuracy.

-----

-----

Phase: [EXPLORATION]

### Source [98]: https://arxiv.org/html/2603.07670v1

Query: What LLM-driven techniques for autonomous memory auditing, contradiction flagging, and self-correction have proven effective in maintaining semantic and episodic store integrity over thousands of interactions?

Answer: Survey formalizes agent memory as write–manage–read loop. Effective techniques: conflict-aware reconsolidation (HiMem-like), introspective reflection (Reflexion: verbal self-critiques post-failure stored as episodic memory; Generative Agents: clusters observations into reflections). Self-improving: ExpeL extracts success/failure rules from trajectory contrasts. Risks: self-reinforcing errors (mitigate via evidence citation). Benchmarks (LoCoMo, MemBench, MemoryAgentBench, MemoryArena) test over thousands interactions, showing gaps in contradiction handling/selective forgetting. Hierarchical (MemGPT: OS paging), reflective evolution maintain integrity.

-----

-----

Phase: [EXPLORATION]

### Source [99]: https://www.preprints.org/manuscript/202601.0618

Query: What LLM-driven techniques for autonomous memory auditing, contradiction flagging, and self-correction have proven effective in maintaining semantic and episodic store integrity over thousands of interactions?

Answer: Evolutionary framework: Storage (trajectories), Reflection (refinement), Experience (abstraction). Reflection stage: Introspection (self-critique verifies/repairs trajectories; Reflexion distills feedback; detects contradictions via consistency checks). Error rectification targets hallucinations/multi-step errors. Environment/Coordination feedback. Proven over long interactions via benchmarks assessing consistency (LoCoMo: 35 sessions, 16K tokens). Experience abstracts for generalization, but Reflection flags contradictions.

-----

-----

Phase: [EXPLORATION]

### Source [100]: https://arxiv.org/html/2604.04853v1

Query: What LLM-driven techniques for autonomous memory auditing, contradiction flagging, and self-correction have proven effective in maintaining semantic and episodic store integrity over thousands of interactions?

Answer: MemMachine: ground-truth-preserving episodic/semantic memory. Contextualized retrieval expands nucleus episodes with neighbors for integrity. Profile memory extracts/updates user facts, handling contradictions via latest state. Benchmarks (LoCoMo: 91.69%; LongMemEval S: 93%) over thousands interactions. Ablations: retrieval depth/prompts key for self-correction-like accuracy.

-----

-----

Phase: [EXPLORATION]

### Source [101]: https://openreview.net/pdf/efa7518ae97c78d6fa2dcbdb06e9a6bf5e799c97.pdf

Query: What LLM-driven techniques for autonomous memory auditing, contradiction flagging, and self-correction have proven effective in maintaining semantic and episodic store integrity over thousands of interactions?

Answer: Taxonomy: episodic/semantic/procedural. Techniques: reflection (Reflexion: self-critiques), conflict resolution in updates. Benchmarks (LoCoMo, LongMemEval) test integrity over long interactions.

-----

</details>

<details>
<summary>How have state persistence and memory recall patterns from NPC design in open-world video games influenced episodic and procedural memory architectures in contemporary LLM-based conversational agents?</summary>

Phase: [EXPLORATION]

### Source [103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11449156/

Query: How have state persistence and memory recall patterns from NPC design in open-world video games influenced episodic and procedural memory architectures in contemporary LLM-based conversational agents?

Answer: The paper reviews episodic-inspired AI systems, particularly in reinforcement learning agents for games like Atari and navigation tasks, using hippocampus-inspired replay buffers for episodic memory. Early architectures like Soar include procedural memory (if-then rules), working memory (current state), and episodic memory (past states). These enable strategic decision-making, fast learning, navigation, exploration, and acting over temporal distance in game environments. Event memory in AI agents supports one-shot learning in sparse-reward settings like Atari Labyrinth, novel strategies in TankSoar, and cognitive map construction for navigation. The paper proposes AI event memory informs biological episodic memory functions, such as planning independent of simulation and fast learning in novel environments. Direct influence from open-world NPC design is not explicit, but game agent architectures draw from biological episodic memory, paralleling NPC state persistence and recall.

-----

-----

Phase: [EXPLORATION]

### Source [104]: https://antoniosliapis.com/articles/llm_and_games.php

Query: How have state persistence and memory recall patterns from NPC design in open-world video games influenced episodic and procedural memory architectures in contemporary LLM-based conversational agents?

Answer: The survey on LLMs in games discusses NPCs using LLMs for dialogue and behavior, with persistent memory via language-based storage of environment state and actions, summarized for prompting to retain knowledge. Generative Agents project populates virtual village with LLM agents recalling past events during social interactions in sandbox environments. Background NPCs maintain agency illusion through goal-following and planning. No explicit link to open-world game NPC design influencing LLM memory architectures, but highlights LLMs enabling state persistence and recall patterns in conversational agents simulating NPC-like behavior.

-----

-----

Phase: [EXPLORATION]

### Source [105]: https://www.daydreamsoft.com/blog/generative-npc-behavior-using-llms-transforming-ai-characters-into-adaptive-intelligent-entities

Query: How have state persistence and memory recall patterns from NPC design in open-world video games influenced episodic and procedural memory architectures in contemporary LLM-based conversational agents?

Answer: The blog describes LLM-based NPCs with persistent memory remembering player choices, alliances, betrayals, or conversations for personal gameplay. Dynamic decision-making evaluates scenarios considering consequences. Hybrid with traditional AI for pathfinding and behavior trees. Challenges include guardrails for lore accuracy. No direct discussion of influence from open-world game NPC design on LLM architectures, but emphasizes state persistence enabling organic, memory-driven interactions in open-world-like games.

-----

-----

Phase: [EXPLORATION]

### Source [106]: https://www.diva-portal.org/smash/get/diva2:2013165/FULLTEXT01.pdf

Query: How have state persistence and memory recall patterns from NPC design in open-world video games influenced episodic and procedural memory architectures in contemporary LLM-based conversational agents?

Answer: The thesis implements Dax NPC with episodic memory in JSON logging past exchanges, sentiments, timestamps for recall and consistency. Uses Mistral LLM with prompts incorporating memory and sentiment. Related work includes memory-augmented NPCs inspired by human memory. No explicit influence from open-world NPC design, but framework enables context-aware, emotion-based persistence in game conversations.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ai-agent-memory-explained-types-implementation-best-practice.md">
<details>
<summary>AI Agent Memory: Types, Implementation, Challenges & Best Practices 2026</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://47billion.com/blog/ai-agent-memory-types-implementation-best-practices/>

# AI Agent Memory: Types, Implementation, Challenges & Best Practices 2026

https://47billion.com/wp-content/uploads/2026/03/AI-Agent-Memory-2026-1-3-1024x536.webp

**AI agent memory** enables AI systems to store, retrieve, and update information across interactions. Unlike LLM context windows, it provides persistent knowledge through short-term memory, long-term memory, and retrieval systems like vector databases and graph databases. This allows AI agents to personalize responses, maintain multi-session context, and continuously improve.

Memory is the core of truly intelligent **AI agent memory systems**. Without it, even the most powerful LLMs remain stateless — forgetting everything after each interaction. In 2026, production-grade **agent memory** turns one-shot chatbots into persistent, personalized, self-improving systems capable of long horizon reasoning, personalization, and multi-session continuity.

This guide dives deep into **AI agent memory** — from short-term vs long-term memory in AI agents to advanced implementations like Mem0, graph memory, and Agentic Context Engineering. Whether you’re building with LangChain, exploring Mem0, or deploying enterprise agents, you’ll find actionable insights, code-ready concepts, and real-world examples.

https://47billion.com/wp-content/uploads/2026/03/image-6.png

Source: [mem0.ai](https://mem0.ai/blog/memory-in-agents-what-why-and-how)

**What Is AI Agent Memory?**

**AI agent memory** refers to a system’s ability to store, retrieve, and update information across interactions, enabling continuity, learning, and personalization. Unlike a simple LLM context window (which is limited and resets), true agent memory combines:

- **Short-term memory** (working memory for the current session)

- **Long-term memory** (persistent across sessions)

- **Retrieval mechanisms** (semantic search, graph traversal, or SQL queries)

It goes beyond basic RAG (Retrieval-Augmented Generation). RAG fetches external documents once; agent memory maintains evolving state, user preferences, past decisions, and learned procedures.

According to cognitive architectures like CoALA and production frameworks such as Mem0, agent memory mirrors human cognition: episodic (what happened), semantic (what I know), and procedural (how to do it).

**Types of Memory in AI Agents (Cognitive + Scope-Based)**

Memory in AI agents falls into two broad categories: **cognitive** (what it remembers) and **scope-based** (who it remembers for).

Here’s a clear comparison:

https://47billion.com/wp-content/uploads/2026/03/image-10.png

[Source:](https://www.riskinfo.ai/post/agentic-memory-unleashing-the-potential-of-ai-with-a-digital-brain) [riskinfo.ai](https://www.riskinfo.ai/post/agentic-memory-unleashing-the-potential-of-ai-with-a-digital-brain)

**_1\. Short-Term / Working Memory_**

- Holds recent conversation turns, intermediate reasoning, and session context.

- Supports expiration timestamps (filter by current time).

- Implementation: Conversation buffers or in-memory caches.

- Use case: Live chatbot session where the agent remembers the last 5–10 exchanges.

**_2\. Long-Term Memory (Persistent)_**

- Survives session resets and powers continuity.

- Stored in databases (Postgres for structured facts, vector stores for embeddings).

- Sub-types (standard in Mem0, LangGraph, and CoALA):

- **Episodic Memory**: Summarized history of specific interactions (“Last session the user updated Artifact X and preferred Y approach”).

- **Semantic Memory**: Facts and preferences (“User like pizza, prefers dark mode, works in fintech”).

- **Procedural Memory**: Workflows and skills (“Step-by-step process for invoice approval: validate → route → notify”).

**_3\. Graph Memory (Advanced Relational)_**

- Uses Neo4j or similar to create entity-relationship graphs.

- Excels at multi-hop reasoning (“What products did this user review that are related to their previous purchase?”).

- Faster lookups than pure vector similarity in complex domains.

**_4\. Scope-Based Isolation_**

- User ID, Agent ID, Session ID, or Organizational (shared across team agents).

- Enables personalization while maintaining privacy and separation.

https://47billion.com/wp-content/uploads/2026/03/image-9.png

[Source:](https://ai.gopubby.com/long-term-memory-for-agentic-ai-systems-4ae9b37c6c0f) [ai.gopubby.com](https://ai.gopubby.com/long-term-memory-for-agentic-ai-systems-4ae9b37c6c0f)

**Mem0: The Production-Grade Memory Layer for Agents**

Among frameworks (LangChain, LlamaIndex, Zep), **Mem0** stands out as the most mature long-term memory solution in 2026. It supports all the types above in just a few lines of code and uses hybrid storage:

- Postgres for long-term facts and episodic summaries

- Qdrant (or similar vector DB) for semantic search

- Neo4j integration for graph memory

- Automatic summarization, expiration, and importance-based updates

Mem0 also powers self-improving loops by continuously updating memories from interactions. Benchmarks show up to 26% accuracy gains over plain vector approaches because it intelligently consolidates and forgets irrelevant data.

**Real-World Use Cases & Implementation Examples**

**Personalization Engine** (e.g., customer support chatbot):

- Short-term: Current chat session.

- Episodic: Summarize previous tickets.

- Semantic: User preferences (“prefers email updates”).

- Result: Agent greets returning users by name and references past issues instantly.

**Artifact Management Chatbot** (internal enterprise tool):

- Graph memory traverses relationships between documents.

- Procedural memory stores approval workflows.

- Long-term memory persists complete artifact history.

https://47billion.com/wp-content/uploads/2026/03/image-7.png

[mem0.ai](https://mem0.ai/research)

**Agentic Context Engineering: The Self-Improving Agent Revolution**

Traditional agents suffer from two major flaws:

- **Brevity bias** — LLMs favor short answers and drop nuance.

- **Context collapse** — Iterative summarization erodes details over time.

The 2025 arXiv paper _Agentic Context Engineering_ (ACE) solves this with a three-agent loop:

1. **Generator** → Produces initial response/trajectory.

2. **Reflector** → Evaluates and refines (detects errors, adds missing context).

3. **Curator** → Extracts learnings and updates a “context playbook” (skills.md or memory store).

Next time the agent runs, the playbook is injected automatically. Result: +10.6% on agent benchmarks and +8.6% in domain tasks — all without fine-tuning the LLM.

https://47billion.com/wp-content/uploads/2026/03/image-8.png

[Source: altexsoft.com](https://www.altexsoft.com/blog/agentic-context-engineering/)

LangGraph’s /remember attribute and Mem0’s update mechanisms make this easy to implement today.

**Challenges & Optimization Strategies (2026 Best Practices)**

- **Storage vs Inference Trade-off**: Full history explodes costs. Solution: Hierarchical memory + importance scoring + dynamic forgetting.

- **Vector vs Graph vs SQL**:

- Vector DBs → Excellent semantic similarity but poor multi-hop.

- Graph DBs → Fast relationship traversal (ideal for episodic + procedural).

- SQL/Postgres → Reliable, auditable, ACID-compliant for long-term facts.

- **Forgetting Mechanisms**: Not remembering everything is a feature. Use temporal decay, relevance scoring, or user-defined policies (e.g., forget after one semester in education agents).

- **Multi-Agent Memory**: Shared organizational memory + private agent-specific spaces (via agent\_id/user\_id) prevent context bloat.

**How to Get Started & Choose the Right Framework**

- Quick prototype: Mem0 + LangGraph (3 lines for memory).

- Production: Mem0 or 47billion.com’s  for enterprise scale.

- Advanced: Add graph memory + ACE loops for self-improving agents.

**Key Takeaways for 2026**

- Context window ≠ memory.

- RAG alone is not enough.

- Persistent, multi-type memory + self-improvement loops = the new standard for agentic AI.

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

### 1\. Memory extraction: From conversation to insights

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

### 2\. Memory consolidation

Rather than simply adding new memories to existing storage, the system performs intelligent consolidation to merge related information, resolve conflicts, and minimize redundancies. This consolidation makes sure the agent’s memory remains coherent and up to date as new information arrives.

The consolidation process works as follows:

1. **Retrieval**: For each newly extracted memory, the system retrieves the top most semantically similar existing memories from the same namespace and strategy.
2. **Intelligent processing**: The new memory and retrieved memories are sent to the LLM with a consolidation prompt. The prompt preserves the semantic context, thus avoiding unnecessary updates (for example, “loves pizza” and “likes pizza” are considered essentially the same information). Preserving these core principles, the prompt is designed to handle various scenarios:





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

   - **ADD**: When the new information is distinct from existing memories
   - **UPDATE**: Enhance existing memories when the new knowledge complements or updates the existing memories
   - **NO-OP**: When the information is redundant
3. **Vector store updates**: The system applies the determined actions, maintaining an immutable audit trail by marking the outdated memories as INVALID instead of instantly deleting them.

This approach makes sure that contradictory information is resolved (prioritizing recent information), duplicates are minimized, and related memories are appropriately merged.

### Handling edge cases

The consolidation process gracefully handles several challenging scenarios:

- **Out-of-order events**: Although the system processes events in temporal order within sessions, it can handle late-arriving events through careful timestamp tracking and consolidation logic.
- **Conflicting information**: When new information contradicts existing memories, the system prioritizes recency while maintaining a record of previous states:





```java
Existing: "Customer budget is \$500"
New: "Customer mentioned budget increased to \$750"
Result: New active memory with \$750, previous memory marked inactive
```





Java

- **Memory failures**: If consolidation fails for one memory, it doesn’t impact others. The system uses exponential backoff and retry mechanisms to handle transient failures. If consolidation ultimately fails, the memory is added to the system to help prevent potential loss of information.

## **Advanced custom** memory strategy configurations

While built-in memory strategies cover common use cases, AgentCore Memory recognizes that different domains require tailored approaches for memory extraction and consolidation. The system supports [built-in strategies with overrides](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-custom-strategy.html) for custom prompts that extend the built-in extraction and consolidation logic, letting teams adapt memory handling to their specific requirements. To maintain system compatibility and focus on criteria and logic rather than output formats, custom prompts help developers customize what information gets extracted or filtered out, how memories should be consolidated, and how to resolve conflicts between contradictory information.

AgentCore Memory also supports custom model selection for memory extraction and consolidation. This flexibility helps developers balance accuracy and latency based on their specific needs. You can define them via the APIs when you create the _memory\_resource_ as a strategy override or via the console (as shown below in the console screenshot).

https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/14/ML-19668-4.png

Apart from override functionality, we also offer [self-managed strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-self-managed-strategies.html) that provide complete control over your memory processing pipeline. With self-managed strategies, you can implement custom extraction and consolidation algorithms using any models or prompts while leveraging AgentCore Memory for storage and retrieval. Also, using the Batch APIs, you can directly ingest extracted records into AgentCore Memory while maintaining full ownership of the processing logic.

### Performance characteristics

We evaluated our built-in memory strategy across three public benchmarking datasets to assess different aspects of long-term conversational memory:

- **LoCoMo**: Multi-session conversations generated through a machine-human pipeline with persona-based interactions and temporal event graphs. Tests long-term memory capabilities across realistic conversation patterns.
- **LongMemEval**: Evaluates memory retention in long conversations across multiple sessions and extended time periods. We randomly sampled 200 QA pairs for evaluation efficiency.
- **PrefEval**: Tests preference memory across 20 topics using 21-session instances to evaluate the system’s ability to remember and consistently apply user preferences over time.
- **PolyBench-QA:** A question-answering dataset containing 807 Question Answer (QA) pairs across 80 trajectories, collected from a coding agent solving tasks in PolyBench.

We use two standard metrics: **_correctness_** and **_compression rate_**. LLM-based correctness evaluates whether the system can correctly recall and use stored information when needed. Compression rate is defined as output memory token count / full context token count, and evaluates how effectively the memory system stores information. Higher compression rates indicate the system maintains essential information while reducing storage overhead. This compression rate directly translates to faster inference speeds and lower token consumption–the most critical consideration for deploying agents at scale because it enables more efficient processing of large conversational histories and reduces operational costs.

|     |     |     |     |
| --- | --- | --- | --- |
| **Memory Type** | **Dataset** | **Correctness** | **Compression Rate** |
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

- Extraction and consolidation operations complete within 20-40 seconds for standard conversations after the extraction is triggered.
- Semantic search retrieval (`retrieve_memory_records` API) returns results in approximately 200 milliseconds.
- Parallel processing architecture enables multiple memory strategies to process independently; thus, different memory types can be processed simultaneously without blocking each other.

These latency characteristics, combined with the high compression rates, enable the system to maintain responsive user experiences while managing extensive conversational histories efficiently across large-scale deployments.

## Best practices for long-term memory

To maximize the effectiveness of long-term memory in your agents:

- **Choose the right memory strategies**: Select built-in strategies that align with your use case or create custom strategies for domain-specific needs. Semantic memory captures factual knowledge, preference memory tailors towards individual preference, and summarization memory distills complex information for better context management. For example, a customer support agent might use semantic memory to capture customer transaction history and past issues, while summarization memory creates short narratives of current support conversations and troubleshooting workflows across different topics.
- **Design meaningful namespaces**: Structure your namespaces to reflect your application’s hierarchy. This also enables precise memory isolation and efficient retrieval. For example, use `customer-support/user/john-doe` for individual agent memories and `customer-support/shared/product-knowledge` for team-wide information.
- **Monitor consolidation patterns**: Regularly review what memories are being created (using `list_memories` or `retrieve_memory_records` API), updated, or skipped. This helps refine your extraction strategies and helps the system capture relevant information that’s better fitted to your use case.
- **Plan for async processing:** Remember that long-term memory extraction is asynchronous. Design your application to handle the delay between event ingestion and memory availability. Consider using short-term memory for immediate retrieval needs while long-term memories are being processed and consolidated in the background. You might also want to implement fallback mechanisms or loading states to manage user expectations during processing delays.

## Conclusion

The Amazon Bedrock AgentCore Memory long-term memory system represents a significant advancement in building AI agents. By combining sophisticated extraction algorithms, intelligent consolidation processes, and immutable storage designs, it provides a robust foundation for agents that learn, adapt, and improve over time.

The science behind this system, from research-backed prompts to innovative consolidation workflow, makes sure that your agents don’t just remember, but understand. This transforms one-time interactions into continuous learning experiences, creating AI agents that become more helpful and personalized with every conversation.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-does-memory-for-ai-agents-work-by-paul-iusztin.md">
<details>
<summary>How Does Memory for AI Agents Work?</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.decodingai.com/p/how-does-memory-for-ai-agents-work>

# How Does Memory for AI Agents Work?

[https://substackcdn.com/image/fetch/$s_!k2ig!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00bc74e0-3601-49ce-8ab9-4c7b499ce597_1280x1280.png](https://www.decodingai.com/)

# [https://substackcdn.com/image/fetch/$s_!XBIw!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85e4cd45-ca39-48d4-941c-86dc67ba9848_1344x325.png](https://www.decodingai.com/)

SubscribeSign in

https://substackcdn.com/image/fetch/$s_!pQz0!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0714d360-396c-4b41-a676-1b58dc1dc5f3_1470x1470.jpeg

Discover more from Decoding AI Magazine

Join for content on designing, building, and shipping AI software. Learn AI engineering, end-to-end, from idea to production. Every Tuesday.

Over 40,000 subscribers

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# How Does Memory for AI Agents Work?

### The 4 memory types every AI agent needs

[https://substackcdn.com/image/fetch/$s_!pQz0!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0714d360-396c-4b41-a676-1b58dc1dc5f3_1470x1470.jpeg](https://substack.com/@pauliusztin)

[Paul Iusztin](https://substack.com/@pauliusztin)

Dec 02, 2025

80

7

14

Share

_**Welcome to the AI Agents Foundations series**: A 9-part journey from Python developer to AI Engineer. Made by busy people. For busy people._

Everyone’s talking about AI agents. But what actually is an agent? When do we need them? How do they plan and use tools? How do we pick the correct AI tools and agentic architecture? …and most importantly, where do we even start?

To answer all these questions (and more!), We’ve started a 9-article straight-to-the-point series to build the skills and mental models to ship real AI agents in production.

We will write everything from scratch, jumping directly into the building blocks that will teach you _“how to fish”_.

**What’s ahead**:

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. _**AI Agent’s Memory** ← You are here_

9. [Multimodal Agents](https://www.decodingai.com/p/stop-converting-documents-to-text)


By the end, you’ll have a deep understanding of how to design agents that think, plan, and execute—and most importantly, how to integrate them in your AI apps without being overly reliant on any AI framework.

**Let’s get started.**

* * *

## [Opik: Open-Source LLMOps Platform (Sponsored)](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul)

This **AI Agents Foundations** series is brought to you by [Opik](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul) (created by Comet), the LLMOps open-source platform used by Uber, Etsy, Netflix, and more.

Comet, through its free events, is dedicated to helping the AI community keep up on the state-of-the-art LLMOps topics, such as:

- AI observability: evaluating and monitoring of LLM apps

- Detecting hallucinations

- Defining custom AI evals for your business use case


These are old problems… But applying them in production isn’t! There is constant progress in all these dimensions.

[https://substackcdn.com/image/fetch/$s_!yeD8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeaa636a-b1a6-429b-83d8-080bc218e596_1200x400.png](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul) [Try Opik for free here](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul) (25k spans/month free)

That’s why **Comet** constantlyoffers **free events** on **how to solve LLMOps problems** **in production**, hands-on, with tools and strategies for LLM evaluation, experiment tracking, and trace monitoring, so you can properly move from theory to shipping AI apps.

_You can check out their free events on LLMOps here:_

[LLMOps Events](https://luma.com/cometml?k=c)

The next ones are on the 7th of December on AI observability and on the 17th of December on hallucinations. Both are looking over state-of-the-art papers on how to solve these problems. Enjoy!

* * *

## AI Agent’s Memory

One year ago at ZTRON, we faced a challenge that many AI builders encounter: how do we give our agent access to the right information at the right time? Like most teams, we jumped straight into building a complex multimodal Retrieval-Augmented Generation (RAG) system. We built the whole suite: embeddings for text, embeddings for images, OCR, summarization, chunking, and multiple indexes.

Our ingestion pipeline became incredibly heavy. It introduced unnecessary complexity around scaling, monitoring, and maintenance. At query time, instead of a straight line from question to answer, our agent would zigzag through 10 to 20 retrieval steps, trying to gather the right context. The latency was terrible, costs were high, and debugging was a nightmare.

Then we realized something essential. Because we were building a vertical AI agent for a specific use case, our data wasn’t actually that big. Through virtual multi-tenancy and smart data siloing, we could retrieve relevant data with simple SQL queries and fit everything comfortably within modern context windows—around 65,000 tokens maximum, well within Gemini’s 1 million token input capacity.

We dropped the entire RAG layer in favor of Context-Augmented Generation (CAG) with smart context window engineering. Everything became faster, cheaper, and more reliable. This experience taught me that the fundamental challenge in building AI agents isn’t just about retrieval. It is about understanding how to architect memory systems that match your actual use case.

The core problem we are solving is the fundamental limitation of LLMs: their knowledge is vast but frozen in time. They are unable to learn by updating their weights after training, a problem known as “continual learning” [\[1\]](https://arxiv.org/html/2510.17281v2). An LLM without memory is like an intern with amnesia. They might be brilliant, but they cannot recall previous conversations or learn from experience.

To overcome this, we use the context window as a form of “working memory.” However, keeping an entire conversation thread plus additional information in the context window is often unrealistic. Rising costs per turn and the “lost in the middle” problem—where models struggle to use information buried in the center of a long prompt limit this approach. While context windows are increasing, relying solely on them introduces noise and overhead [\[2\]](https://arxiv.org/abs/2307.03172).

Memory tools act as the solution. They provide agents with continuity, adaptability, and the ability to “learn” without retraining. When we first started building agents, working with 8k or 16k token limits forced us to engineer complex compression systems. Today, we have more breathing room, but the principles of organizing memory remain essential for performance.

In this article, we will explore:

1. The four fundamental types of memory for AI agents.

2. A detailed look at long-term memory: Semantic, Episodic, and Procedural.

3. The trade-offs between storing memories as strings, entities, or knowledge graphs.

4. The complete memory cycle, from ingestion to inference.


## The 4 Memory Types for AI Agents

To build effective agents, we must distinguish between the different places information lives. We can borrow terms from biology and cognitive science to categorize these layers useful for engineering.

There are four distinct memory types based on their persistence and proximity to the model’s reasoning core.

**1\. Internal Knowledge:** This is the static, pre-trained knowledge baked into the LLM’s weights. It is the best place to store general world knowledge—models know about whole books without needing them in the context window. However, this memory is frozen at the time of training.

**2\. Context Window:** This is the slice of information we pass to the LLM during a specific call. It acts as the RAM of the LLM. It is the only “reality” the model sees during inference.

**3\. Short-Term Memory:** This is the RAM of the entire agentic system. It contains the active context window plus recent interactions, conversation history, and details retrieved from long-term memory. We slice this short-term memory to create the context window for a single inference step. It is volatile and fast, simulating the feeling of “learning” during a session [\[3\]](https://www.ibm.com/think/topics/ai-agent-memory).

**4\. Long-Term Memory:** This is the external, persistent storage system (disk) where an agent saves and retrieves information. This layer provides the personalization and context that internal knowledge lacks and short-term memory cannot retain [\[4\]](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents).

The dynamic between these layers creates the agent’s intelligence. First, part of the long-term memory is “retrieved” and brought into short-term memory. This retrieval pipeline queries different memory types in parallel. Next, we slice the short-term memory into an active context window through context engineering. Finally, during inference, the LLM uses its internal weights plus the active context window to generate output.

https://substackcdn.com/image/fetch/$s_!G5CM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c6f2d58-f21f-4b49-b4f0-fb553fc28e36_1200x1200.png Image 1: A flowchart illustrating the four memory types for AI agents and their dynamic data flow.

Another useful way to visualize this is by proximity to the LLM. Internal memory is intrinsic, while long-term memory is the furthest away, requiring specific retrieval mechanisms to become useful.

https://substackcdn.com/image/fetch/$s_!X4Ty!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff28bf45c-5354-4c96-879a-fad379a7f675_1200x1200.png Image 2: A hierarchical diagram showing the four memory types for AI agents and their information flow.

Categorizing memory this way is critical for engineering. Internal knowledge handles general reasoning. Short-term memory manages the immediate task. Long-term memory handles personalization and continuity. No single layer can perform all three functions effectively. To better understand long-term memory, we can further apply cognitive science definitions to specific data types.

## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a single bucket of text. It consists of three distinct types, each serving a different role in making an agent “intelligent” [\[5\]](https://arxiv.org/html/2309.02427), [\[6\]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems).

### Semantic Memory (Facts & Knowledge)

Semantic memory is the agent’s encyclopedia. It stores individual pieces of knowledge or “facts.” These can be independent strings, such as _“The user is a vegetarian,”_ or structured attributes attached to an entity, like `{”food restrictions”: “User is a vegetarian”}`. This is where the agent stores concepts and relationships regarding specific domains, people, or places.

The primary role of semantic memory is to provide a reliable source of truth. For an enterprise agent, this might involve storing internal company documents or technical manuals. For a personal assistant, semantic memory builds a persistent user profile. It recalls specific preferences like `{”music”: “User likes rock music”}` or constraints like `{”dog”: “User has a dog named George”}`. This allows the agent to retrieve relevant facts without searching through a noisy conversation history.

Let’s look at how we can implement semantic memory using `mem0`, an open-source memory library.

1. We define a helper function to add text to memory and categorize it.


```
def mem_add_text(text: str, category: str = “semantic”, **meta) -> str:
    “”“Add a single text memory. No LLM is used for extraction or summarization.”“”
    metadata = {”category”: category}
    for k, v in meta.items():
        if isinstance(v, (str, int, float, bool)) or v is None:
            metadata[k] = v
        else:
            metadata[k] = str(v)
    memory.add(text, user_id=MEM_USER_ID, metadata=metadata, infer=False)
    return f”Saved {category} memory.”
```

2. We insert specific facts about the user.


```
facts: list[str] = [\
    “User prefers vegetarian meals.”,\
    “User has a dog named George.”,\
    “User is allergic to gluten.”,\
    “User’s brother is named Mark and is a software engineer.”,\
]
for f in facts:
    print(mem_add_text(f, category=”semantic”))
```

3. We can now search for this specific semantic information.


```
results = memory.search(”brother job”, user_id=MEM_USER_ID, limit=1)
print(results[”results”][0][”memory”])
```

4. It outputs:


```
User’s brother is named Mark and is a software engineer.
```

### Episodic Memory (Experiences & History)

Episodic memory is the agent’s personal diary. It records past interactions, but unlike timeless facts, these memories have a timestamp. It captures _“what happened and when.”_

This memory type is essential for maintaining conversational context and understanding relationship dynamics. A semantic fact might be _“User is frustrated with his brother.”_ An episodic memory would be: _“On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I provided an empathetic response. \[created\_at=2025-08-25\].”_

This “episode” provides nuanced context. If the topic comes up again, the agent can say, “I know the topic of your brother’s birthday can be sensitive,” rather than just stating a fact. It also allows the agent to answer questions like _“What happened last week?”_ [\[7\]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Here is how we can implement episodic memory by compressing a conversation into a summary.

1. We define a dialogue and ask the LLM to summarize it into an episode.


```
dialogue = [\
    {”role”: “user”, “content”: “I’m stressed about my project deadline on Friday.”},\
    {”role”: “assistant”, “content”: “I’m here to help—what’s the blocker?”},\
    {”role”: “user”, “content”: “Mainly testing. I also prefer working at night.”},\
    {”role”: “assistant”, “content”: “Okay, we can split testing into two sessions.”},\
]

episodic_prompt = f”“”Summarize the following 3–4 turns as one concise ‘episode’ (1–2 sentences).
Keep salient details and tone.

{dialogue}
“”“
episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
episode = episode_summary.text.strip()
```

2. We save this summary as an episodic memory.


```
print(
    mem_add_text(
        episode,
        category=”episodic”,
        summarized=True,
        turns=4,
    )
)
```

3. We can search for the “experience” later.


```
hits = mem_search(”deadline stress”, limit=1, category=”episodic”)
for h in hits:
    print(f”{h[’memory’]}\n”)
```

4. It outputs:


```
A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
```

### Procedural Memory (Skills & How-To)

Procedural memory is the agent’s muscle memory. It consists of skills, learned workflows, and “how-to” knowledge. It dictates the agent’s ability to perform multi-step tasks.

This memory is often baked into the agent’s system prompt as reusable tools or defined sequences. For example, an agent might store a `MonthlyReportIntent` procedure. When a user asks for a report, the agent retrieves this procedure: 1) Query sales DB, 2) Summarize findings, 3) Email user. This makes behavior reliable and predictable. It encodes successful workflows so the agent doesn’t have to reason from scratch every time [\[8\]](https://arxiv.org/html/2508.06433v2).

1. We define a procedure as a text block containing steps.


```
procedure_name = “monthly_report”
steps = [\
    “Query sales DB for the last 30 days.”,\
    “Summarize top 5 insights.”,\
    “Ask user whether to email or display.”,\
]
procedure_text = f”Procedure: {procedure_name}\nSteps:\n” + “\n”.join(f”{i + 1}. {s}” for i, s in enumerate(steps))

mem_add_text(procedure_text, category=”procedure”, procedure_name=procedure_name)
```

2. We retrieve the procedure by intent.


```
results = mem_search(”how to create a monthly report”, category=”procedure”, limit=1)
if results:
    print(results[0][”memory”])
```

3. It outputs:


```
Procedure: monthly_report
Steps:
1. Query sales DB for the last 30 days.
2. Summarize top 5 insights.
3. Ask user whether to email or display.
```

https://substackcdn.com/image/fetch/$s_!vH8x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9d07e03-3d66-41bc-b839-c6f8dc510c00_1109x508.png Image 3: A flowchart illustrating an AI Agent interacting with Semantic, Episodic, and Procedural long-term memory systems.

Now that we know what to save, we must decide _how_ to store it.

## Storing Memories: Pros and Cons of Different Approaches

The way an agent’s memories are stored is an architectural decision that impacts performance, complexity, and scalability. There is no one-size-fits-all solution. Let’s explore the three primary methods we experiment with as AI Engineers.

### 1\. Storing Memories as Raw Strings

This is the simplest method. Conversational turns or documents are stored as plain text and indexed for vector search.

**Pros:** It is simple and fast to set up, requiring minimal engineering. It preserves nuance, capturing emotional tone and linguistic cues without loss in translation.

**Cons:** Retrieval is often imprecise. A query like “What is my brother’s job?” might retrieve every conversation mentioning “brother” and “job” without pinpointing the current fact. Updating is difficult; if a user corrects a fact (“My brother is now a doctor”), the new string just adds to the log, creating potential contradictions. It also lacks structure, making it hard to distinguish state changes over time (e.g., “Barry _was_ CEO” vs. “Claude _is_ CEO”).

### 2\. Storing Memories as Entities (JSON-like Structures)

Here, we use an LLM to transform messy interactions into structured memories, stored in formats like JSON within document databases (MongoDB) or SQL databases (PostgreSQL).

**Pros:** It allows for precise, field-level filtering (e.g., `“user”: {”brother”: {”job”: “Software Engineer”}}`). The agent can retrieve specific facts without ambiguity. Updates are easier. You simply overwrite the relevant field. This is ideal for semantic memory like user profiles or preferences.

**Cons:** It requires upfront schema design complexity. Still, tt can be rigid. If the agent encounters information that doesn’t fit the schema, that data might be lost unless the schema is updated [\[9\]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece).

### 3\. Storing Memories in a Knowledge Graph

This is the most advanced approach. Memories are stored as a network of nodes (entities) and edges (relationships) using databases such as Neo4j or PostgreSQL.

**Pros:** It excels at representing complex relationships (e.g., `(User) -> [HAS_BROTHER] -> (Mark)`). It offers superior contextual and temporal awareness by modeling time as a property of a relationship (e.g., `[RECOMMENDED_ON_DATE]`). Retrieval is auditable. You can trace the path of reasoning, which builds trust.

**Cons:** It has the highest complexity and cost. Converting unstructured text into graph triples is difficult. Graph traversals can be slower than vector lookups, potentially impacting real-time performance. For simple use cases, it is often overkill [\[10\]](https://arxiv.org/html/2504.19413).

https://substackcdn.com/image/fetch/$s_!9Nxk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fcaddfe-f8c5-49c7-9c26-9620fb343c7b_832x1052.jpeg Image 4: A knowledge graph illustrating memory as interconnected entities and relationships. We took the image from this [LinkedIn post](https://www.linkedin.com/posts/tonyseale_this-week-anthropic-dropped-claude-sonnet-activity-7379787334398926848-iVOE?utm_source=share&utm_medium=member_desktop&rcm=ACoAACQFQWgBqowPZBqBQgSC3ATmuatVfZkf6fE). If the source is different, let us know, and we will update the article.

> **💡 Note:** Vector databases are typically document databases with vector indexes. They are excellent for retrieval but, in terms of storage structure, they usually fall into the “raw strings” or “entities” bucket (2nd option).

The choice should be guided by your product’s needs. Start simple and evolve as complexity grows.

## Memory cycles: From Long-Term to Internal Memory

How do these memory types work together? They operate as a single clockwork system.

01. **User Input:** We start with the user input, which triggers the entire system.

02. **Ingestion:** Long-term memory is populated by data pipelines or RAG ingestion. External data is accessed via APIs or Model Context Protocol (MCP) servers.

03. **Retrieval:** Data is pulled from long-term memory into short-term memory using search tools.

04. **Short-Term Assembly:** Short-term memory is populated with facts from long-term memory, user input, LLM’s internal chatter and output, and the current tool schemas.

05. **Context Engineering:** We slice the short-term memory to fit the context window. If a user asks about Nvidia, we trim facts about other companies. This projection from the short-term memory to the context window is part of the art of context engineering.

06. **Inference:** We pass this context window to the LLM. The answer is generated based on this window plus the LLM’s internal knowledge. This is their reality.

07. **Loop:** The output of the LLM is added back to the short-term memory.

08. **Update - From Short-Term Memory:** Based on any new facts about the user and problem at hand, we can further update the long-term memory with user preferences and facts, such as what companies they like.

09. **Update - From External World:** Meanwhile, the long-term memory can constantly be updated with other facts from the data pipelines.

10. **Persistence:** Finally, the short-term memory can be saved to a database to remember context between multiple user sessions.


https://substackcdn.com/image/fetch/$s_!sJOC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8451b9a-061a-480f-9989-659960bd51c6_1200x1200.png Image 5: A comprehensive flowchart illustrating the Memory Cycles for an AI agent, showing the continuous interaction between Long-Term Memory, Short-Term Memory, Context Window, and Internal LLM Memory.

## Conclusion

Memory is the component that transforms a stateless chat application into a personalized agent. It is the current engineering solution to the problem of continual learning. By constantly engineering the context window (the LLM’s reality) we allow agents to “learn” and adapt over time.

_Remember that this article is part of a longer series of 9 pieces on the AI Agents Foundations that will give you the tools to morph from a Python developer to an AI Engineer._

**Here’s our roadmap:**

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. _**AI Agent’s Memory** ← You just finished this one._

9. [Multimodal Data](https://www.decodingai.com/p/stop-converting-documents-to-text) _← Move to this one_


See you next Tuesday.

[Paul Iusztin](https://www.pauliusztin.ai/)

* * *

_What’s your take on today’s topic? Do you agree, disagree, or is there something I missed?_

[Leave a comment](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work/comments)

* * *

If you enjoyed this article, the ultimate compliment is to share our work.

[Share](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work?utm_source=substack&utm_medium=email&utm_content=share&action=share)

* * *

## Go Deeper

Everything you learned in this article, from building evals datasets to evaluators, comes from the AI Evals & Observability module of our [Agentic AI Engineering self-paced course](https://academy.towardsai.net/courses/agent-engineering?ref=b3ab31).

**Your path to agentic AI for production.** Built in partnership with [Towards AI](https://academy.towardsai.net/courses/agent-engineering?ref=b3ab31).

Across **34 lessons** (articles, videos, and a lot of code), you’ll design, build, evaluate, and deploy production-grade AI agents end to end. By the final lesson, you’ll have built a multi-agent system that orchestrates **Nova** (a deep research agent) and **Brown** (a full writing workflow), plus a **capstone project** where you apply everything on your own.

_Three portfolio projects and a certificate to show off in interviews. Plus a Discord community where you have direct access to other industry experts and me._

Rated 4.9/5 ⭐️ by 190+ early students — “Every AI Engineer needs a course like this.”

[Learn more](https://academy.towardsai.net/courses/agent-engineering?ref=b3ab31)

_Not ready to commit?_ We also prepared a free 6-day email course to reveal the _**6 critical mistakes that silently destroy agentic systems.** [Get the free email course.](https://email-course.towardsai.net/?ref=b3ab31)_

* * *

_Thanks again to [Opik](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul) for sponsoring the series and keeping it free!_

[https://substackcdn.com/image/fetch/$s_!oSDm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26c21863-4ee6-4026-91c7-74650eb16dac_3168x792.png](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul)

**If you want to monitor, evaluate and optimize your AI workflows and agents:**

[Try Opik for free](https://www.comet.com/signup?utm_source=newsletter&utm_medium=partner&utm_campaign=paul)

* * *

## References

01. Wang, L., Zhang, X., Su, H., & Zhu, J. (2025). A Comprehensive Survey of Continual Learning. arXiv preprint arXiv:2302.00487. [https://arxiv.org/html/2510.17281v2](https://arxiv.org/html/2510.17281v2)

02. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv preprint arXiv:2307.03172. [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)

03. What is AI agent memory?. (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-memory](https://www.ibm.com/think/topics/ai-agent-memory)

04. Iusztin, P. (2024, May 21). Memory: The secret sauce of AI agents. Decoding AI Magazine. [article](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agent)

05. Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2023). Cognitive Architectures for Language Agents. arXiv. [https://arxiv.org/html/2309.02427](https://arxiv.org/html/2309.02427)

06. Griciūnas, A. (2024, October 30). Memory in Agent Systems. SwirlAI Newsletter. article. [article](https://www.newsletter.swirlai.com/p/memory-in-agent-systems)

07. Whitmore, S. (2025, June 18). What is the perfect memory architecture?. YouTube. [video](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112)

08. Mem^p: A Framework for Procedural Memory in Agents. (n.d.). arXiv. [https://arxiv.org/html/2508.06433v2](https://arxiv.org/html/2508.06433v2)

09. Chalef, D. (2024, June 25). Memex 2.0: Memory The Missing Piece for Real Intelligence. Substack. [article](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece)

10. Chhikara, P. (2025). Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. arXiv. [https://arxiv.org/html/2504.19413](https://arxiv.org/html/2504.19413)


* * *

## Images

If not otherwise stated, all images are created by the author.

* * *

#### Subscribe to Decoding AI Magazine

Hundreds of paid subscribers

Join for content on designing, building, and shipping AI software. Learn AI engineering, end-to-end, from idea to production. Every Tuesday.

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[https://substackcdn.com/image/fetch/$s_!1FeB!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc82d9b0e-b22a-473c-873b-c182dfc665e3_384x512.png](https://substack.com/profile/49225893-greg-motyl)[https://substackcdn.com/image/fetch/$s_!V-BF!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c02878f-ce7a-465c-95cf-55185238262e_96x96.jpeg](https://substack.com/profile/134913575-rahul)[https://substackcdn.com/image/fetch/$s_!h9m0!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb1a29f0-0d43-4956-bdb9-539312737259_1167x832.jpeg](https://substack.com/profile/86944266-vishal-vatsalya)[https://substackcdn.com/image/fetch/$s_!Gp4v!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43e712b6-c344-452f-8a3e-6aa67810417e_1176x1177.png](https://substack.com/profile/328344890-nikki-swango)[https://substackcdn.com/image/fetch/$s_!emRR!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d21f0ca-db1a-4da0-a8ed-0089aa75fe52_1167x879.jpeg](https://substack.com/profile/100547866-duong-bui)

80 Likes∙

[14 Restacks](https://substack.com/note/p-180239220/restacks?utm_source=substack&utm_content=facepile-restacks)

80

7

14

Share

PreviousNext

#### Discussion about this post

CommentsRestacks

https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png

[https://substackcdn.com/image/fetch/$s_!J0tu!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcc231af-becb-46d7-a503-8314a6b5e870_3840x3840.png](https://substack.com/profile/8759131-toxsec?utm_source=comment)

[ToxSec](https://substack.com/profile/8759131-toxsec?utm_source=substack-feed-item)

[Dec 2](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work/comment/183420139 "Dec 2, 2025, 11:57 AM")

Liked by Paul Iusztin

“Pros: It allows for precise, field-level filtering (e.g., “user”: {”brother”: {”job”: “Software Engineer”}}). The agent can retrieve specific facts without ambiguity. Updates are easier. You simply overwrite the relevant field. This is ideal for semantic memory like user profiles or preferences.”

Agree. I think the pros outweigh the cons, because it’s mostly just a little upfront work to get it going. This is how I stored data for my rag. Great post thanks.

Like (2)

Reply

Share

[1 reply by Paul Iusztin](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work/comment/183420139)

[https://substackcdn.com/image/fetch/$s_!7YXY!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4df7cd9-864a-4f5d-ac19-cd996d715f0a_5184x3880.jpeg](https://substack.com/profile/257807890-meenakshi-navamaniavadaiappan?utm_source=comment)

[Meenakshi NavamaniAvadaiappan](https://substack.com/profile/257807890-meenakshi-navamaniavadaiappan?utm_source=substack-feed-item)

[Dec 2](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work/comment/183349082 "Dec 2, 2025, 8:47 AM")

Liked by Paul Iusztin

Thanks for memory management planning on the same for the good 😊

Like (2)

Reply

Share

[1 reply](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work/comment/183349082)

[5 more comments...](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work/comments)

TopLatestDiscussions

[Build your Second Brain AI assistant](https://www.decodingai.com/p/build-your-second-brain-ai-assistant)

[Using agents, RAG, LLMOps and LLM systems](https://www.decodingai.com/p/build-your-second-brain-ai-assistant)

Feb 6, 2025•[Paul Iusztin](https://substack.com/@pauliusztin)

942

37

159

https://substackcdn.com/image/fetch/$s_!YzRk!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8ba5fa8-00aa-42fa-a187-62cb80fa7301_1166x1090.png

[Stop Building AI Agents](https://www.decodingai.com/p/stop-building-ai-agents)

[Here’s what you should build instead](https://www.decodingai.com/p/stop-building-ai-agents)

Jun 26, 2025•[Hugo Bowne-Anderson](https://substack.com/@hugobowne)

191

13

25

https://substackcdn.com/image/fetch/$s_!hKEL!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43169d77-56ed-4b9d-8a58-891a5a1039f8_847x480.png

[Context Engineering: 2025’s #1 Skill in AI](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

[Everything you must know about context engineering to ship successful AI apps](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

Jul 22, 2025•[Paul Iusztin](https://substack.com/@pauliusztin)

302

16

35

https://substackcdn.com/image/fetch/$s_!l6XV!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa822500b-aa82-4114-9ec4-e4bc48638b24_1150x1040.png

See all

### Ready for more?

Subscribe

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-to-design-efficient-memory-architectures-for-agentic-ai-.md">
<details>
<summary>How to Design Efficient Memory Architectures for Agentic AI Systems</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsai.net/p/machine-learning/how-to-design-efficient-memory-architectures-for-agentic-ai-systems>

# How to Design Efficient Memory Architectures for Agentic AI Systems

Name: Towards AI
Legal Name: Towards AI, Inc.
Description: Towards AI is the world's leading artificial intelligence (AI) and technology publication. Read by thought-leaders and decision-makers around the world.
Phone Number: +1-650-246-9381
Email: pub@towardsai.net

228 Park Avenue SouthNew York,
NY10003United States

Website: [https://towardsai.net/](https://towardsai.net/)
Publisher: [https://towardsai.net/#publisher](https://towardsai.net/#publisher)
Diversity Policy: [https://towardsai.net/about](https://towardsai.net/about)
Ethics Policy: [https://towardsai.net/about](https://towardsai.net/about)
Masthead: [https://towardsai.net/about](https://towardsai.net/about)

Name: Towards AI
Legal Name: Towards AI, Inc.
Description: Towards AI is the world's leading artificial intelligence (AI) and technology publication.
Founders:
Roberto Iriondo,
[Website](https://www.robertoiriondo.com/),
Job Title: Co-founder and Advisor
Works for: Towards AI, Inc.
Follow Roberto:
[X](https://x.com/@robiriondo),
[LinkedIn](https://www.linkedin.com/in/robiriondo),
[GitHub](https://github.com/robiriondo),
[Google Scholar](https://scholar.google.com/citations?user=dTn7NEcAAAAJ),
[Towards AI Profile](https://towardsai.net/p/author/robiriondo),
[Medium](https://medium.com/@robiriondo),
[ML@CMU](https://www.ml.cmu.edu/robiriondo),
[FreeCodeCamp](https://www.freecodecamp.org/news/author/robiriondo/),
[Crunchbase](https://www.crunchbase.com/person/roberto-iriondo),
[Bloomberg](https://www.bloomberg.com/profile/person/22994840),
[Roberto Iriondo, Generative AI Lab](https://roberto.generativeailab.org/),
[Generative AI Lab](https://generativeailab.org/) [VeloxTrend](https://veloxtrend.com/) [Ultrarix Capital Partners](https://ultrarix.com/)Denis Piffaretti,
Job Title: Co-founder
Works for: Towards AI, Inc.Louie Peters,
Job Title: Co-founder
Works for: Towards AI, Inc.Louis-François Bouchard,
Job Title: Co-founder
Works for: Towards AI, Inc.

Cover:


https://b3688296.smushcdn.com/3688296/wp-content/uploads/2024/09/towards-ai-og-graph.jpg?lossy=0&strip=1&webp=1

Logo:


https://b3688296.smushcdn.com/3688296/wp-content/uploads/2019/05/towards-ai-square-circle-png.png?lossy=0&strip=1&webp=1

Areas Served: Worldwide
Alternate Name: Towards AI, Inc.
Alternate Name: Towards AI Co.
Alternate Name: towards ai
Alternate Name: towardsai
Alternate Name: towards.ai
Alternate Name: tai
Alternate Name: toward ai
Alternate Name: toward.ai
Alternate Name: Towards AI, Inc.
Alternate Name: towardsai.net
Alternate Name: pub.towardsai.net

Follow us on:
[Facebook](https://www.facebook.com/towardsAl/ "Facebook") [X](https://x.com/towards_ai "X") [LinkedIn](https://www.linkedin.com/company/towards-artificial-intelligence "LinkedIn") [Instagram](https://www.instagram.com/towards_ai/ "Instagram") [Youtube](https://www.youtube.com/channel/UCQNjFuhOJM1YqFTPY1Q_kYQ "Youtube") [Github](https://github.com/towardsai "Github") [Google My Business](https://local.google.com/place?id=4955254490173856159&use=srp&ved=1t%3A65428&_ga=2.191706990.559569912.1635283323-985655235.1633987376#fpstate=lie "Google my Business") [Google Search](https://www.google.com/search?ved=1t:65428&_ga=2.191706990.559569912.1635283323-985655235.1633987376&q=Towards+AI&ludocid=4955254490173856159&lsig=AB86z5Ur3DZsSmdOFFUwd-bMHTIe#fpstate=lie "Google Search") [Google News](https://news.google.com/publications/CAAqBwgKMNiLmgswgpayAw?oc=3&ceid=US:en "Google News") [Google Maps](https://g.page/TowardsAI?gm "Google Maps") [Discord](https://discord.com/invite/V7RGX9XKAW "Discord") [Shop](https://gumroad.com/towardsai "Shop") [Towards AI, Medium Editorial](https://towardsai.medium.com/ "Towards AI, Medium Editorial") [Medium](https://medium.com/towards-artificial-intelligence "Medium") [Flipboard](https://flipboard.com/@Towards_AI "Flipboard") [Publication](https://pub.towardsai.net/ "Publication") [Feed](https://feed.towardsai.net/ "AI Feed") [Sponsors](https://sponsors.towardsai.net/ "Sponsors") [Sponsors](https://members.towardsai.net/ "Members") [Contribute](https://contribute.towardsai.net/ "Contribute")

5 stars – based on
497 reviews




#### Frequently Used, Contextual References

TODO: Remember to copy unique IDs whenever it needs used. i.e., URL: 304b2e42315e

## Resources

**Free: 6-day [Agentic AI Engineering Email Guide](https://email-course.towardsai.net/?utm_source=towardsai.net&utm_medium=header_bar)**.

_Learnings from Towards AI's hands-on work with real clients._

<Base64-Image-Removed>

[Artificial Intelligence](https://towardsai.net/ai/artificial-intelligence) [Latest](https://towardsai.net/ai/l) [Machine Learning](https://towardsai.net/ai/machine-learning)

# How to Design Efficient Memory Architectures for Agentic AI Systems

[Suchitra Malimbada](https://towardsai.net/p/author/suchitramalimbada)

[31 likes](https://towardsai.net/wp-admin/admin-ajax.php?action=process_simple_like&post_id=48231&nonce=192ee09830&is_comment=0&disabled=true "Like")

November 4, 2025

Last Updated on November 6, 2025 by [Editorial Team](https://towardsai.net/p/author/editorial-team)

#### Author(s): [Suchitra Malimbada](https://blog.suchitra.me/)

Originally published on [Towards AI](https://towardsai.net/).


_A practical guide to building [agentic](https://academy.towardsai.net/courses/agent-engineering/?utm_source=towardsai.net "Agentic AI Engineer Course") AI systems that manage memory efficiently using hierarchical memory architectures, knowledge graphs, and forgetting machanisms, covering everything needed to know before designing memory architecture._

<Base64-Image-Removed>A gif showing how AI [agents](https://academy.towardsai.net/courses/agent-engineering/?utm_source=towardsai.net "Agentic AI Engineer Course") tend to get costly and context overflow if memory not being managed properly

As you can see in the above simulation, the agent confidently handled the first four messages — retrieving the order number, confirming the user’s name, and updating shipping details. But by message five, when the user asks a simple question, the agent has completely lost context and the cost is high.

This is a fundamental architecture problem. Basic vector storage fails at scale because memory isn’t just about retrieval — it’s about state management, quality control, and strategic forgetting. Here’s what actually works: hierarchical memory systems that route information efficiently, knowledge graphs that maintain factual coherence, self-reflection loops that filter hallucinations, and forgetting curves that prune noise. Each architecture solves specific failure modes. The key is knowing when to use what.

**Contents:**

- Why Basic Memory Fails
- The Four Memory Types (And When to Use Each)
- Hierarchical Memory (H-MEM, MemGPT)
- Knowledge Graphs (GraphRAG)
- Selective Forgetting
- Choosing Your Architecture
- Production Tradeoffs

## Why Basic Memory Fails

Vector databases work brilliantly for one-shot queries. Search for “machine learning papers,” get semantically similar documents, done. But production agents aren’t one-shot systems. They maintain conversations across hundreds of turns, coordinate with other agents, and accumulate context that spans weeks.

Flat vector storage, which is storing everything in an undifferentiated vector database and retrieving via cosine similarity introduces four catastrophic failure modes when you scale past examples.

**Context Poisoning** happens when your agent stores hallucinations or errors. In an autonomous feedback loop, contaminated memory compounds. The agent retrieves its own mistakes, reinforces them in new responses, and creates increasingly inaccurate outputs. A customer service bot that incorrectly logs a refund policy will confidently cite that false policy in future interactions, generating a cascade of wrong answers. Without quality control mechanisms, errors become self-reinforcing.

**Context Distraction** buries critical information under noise. Your vector database returns the top 10 most semantically similar entries. But semantic similarity doesn’t equal relevance. When a user asks about their order status, the agent might retrieve nine unrelated order discussions and one relevant entry. The [LLM](https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev "LLM Dev")’s attention gets diluted across irrelevant context. It makes suboptimal decisions because it can’t identify the signal through the noise.

**Context Clash** loads contradictory information into the same context window. A user changed their shipping address two weeks ago, but your vector search retrieves both the old and new addresses with similar relevance scores. The [LLM](https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev "LLM Dev") sees conflicting facts simultaneously, produces inconsistent behavior, and loses coherence. Which address is current? The agent guesses — and often guesses wrong.

**Work Duplication** emerges in multi-agent systems when agents lack shared memory. Agent A fetches a user’s transaction history. Agent B, moments later, fetches the same data because it has no awareness of Agent A’s work. Computational waste multiplies. State diverges across agents. Your system burns tokens on redundant operations while agents maintain inconsistent views of reality.

## The Four Memory Types (And When to Use Each)

Production agents need memory systems that mirror human cognition. Psychological research identifies four functional memory types, and mapping these to agent architectures solves specific problems.

**Working memory** is your agent’s active workspace. It holds the current conversation, recent tool outputs, and symbolic variables needed for immediate decisions. This maps directly to the LLM’s context window. For a customer service agent, working memory contains the last five user messages and the retrieved account status. It’s fast, limited by token constraints, and temporary. Information here must be actively maintained or it vanishes after the interaction completes.

**Episodic memory** stores specific past experiences. This includes conversation history from previous sessions, task outcomes, and tool execution results. When a user says “remember when we discussed shipping options last week,” episodic memory enables that recall. It is possible to implement this with vector databases that index historical interactions. It preserves temporal sequences and supports retrieval across sessions. Episodic memory is what allows the agent to maintain continuity to understand that the user its talking to today is the same user from yesterday’s conversation.

**Semantic memory** is agents knowledge base, consist with persistent facts about the world, the domain, or the agent itself. A medical assistant’s semantic memory contains disease information, treatment protocols, and drug interactions. It’s usually stored in vector databases or knowledge graphs, augmented from external sources like documentation, wikis, or databases. Semantic memory persists indefinitely and updates as knowledge changes. Unlike episodic memory which tracks “what happened,” semantic memory tracks “what is true.”

**Procedural memory** encodes learned skills and action sequences. This is the automation engine. A code generation agent doesn’t just retrieve examples of API calls ,it stores validated procedures for authentication, error handling, and testing workflows. Procedural memory lets agents perform complex tasks without reasoning through every step. It can be implemented using structured formats like PDDL (Planning Domain Definition Language) or Pydantic schemas, ensuring skills are auditable and transferable between models.

The right architecture combines these types based on your agent’s workload. Simple Q&A? Semantic memory alone suffices. Long conversations? Add episodic and working memory management. Complex multi-step reasoning? You need procedural memory and knowledge graphs.

**Critical insight:** Treating all memory identically is the root cause of most production failures. Information has different persistence requirements, access patterns, and quality thresholds. Your architecture must reflect these distinctions.

But understanding memory types is not enough for developing AI agents. The real challenge emerges when episodic and semantic memory repositories scale to millions of entries. At this scale, even categorizing information correctly doesn’t solve the retrieval problem — the agent still drowns in semantically similar but contextually irrelevant results.

This is where flat storage architectures break down completely. A vector database might correctly identify that 10,000 memories relate to “customer shipping inquiries,” but the agent needs the _one specific conversation_ from three weeks ago where this particular user discussed address changes. Semantic similarity alone cannot make this distinction. The solution requires structural organization where broad categories progressively narrow to specific instances.

## Hierarchical Memory: Routing Information Efficiently

### The Problem It Solves

Flat vector databases perform broad similarity searches across millions of entries. While modern vector databases use approximate nearest neighbor algorithms (HNSW, IVF) to avoid truly exhaustive O(n) searches, they still lack contextual awareness. They can’t distinguish between “this embedding is similar” and “this information is relevant to the current task.” As memory scales, retrieval becomes increasingly noisy, retrieving semantically similar results that are contextually irrelevant.

### How It Works

Hierarchical memory organizes information into layers of increasing abstraction, enabling targeted retrieval without scanning the entire database. Think of it as a filing system where you check the drawer label before searching individual folders.

**H-MEM** (Hierarchical Memory) implements four layers: Domain, Category, Memory Trace, and Episode. When an agent needs context, it doesn’t compute similarity against every stored memory. Instead, it uses self-position index encoding to route queries layer by layer. The Domain layer identifies the broad area (customer support vs product recommendations). The Category layer narrows to specific topics (shipping issues vs payment problems). The Memory Trace layer surfaces relevant conversation threads. Finally, the Episode layer retrieves individual interactions.

This index-based routing avoids exhaustive searches by eliminating irrelevant branches early. The system maintains efficiency even as the memory footprint scales substantially. Instead of comparing your query against millions of memories, you compare it against dozens of domain categories, then dozens of subcategories within the relevant domain, and so on.

**MemGPT** takes a different approach inspired by operating system memory management. It maintains a small Core Memory , essential facts and identity compressed into the always-accessible context window and a massive External Context stored in archival memory. The agent orchestrates data movement between these tiers via self-generated function calls, implementing a paging mechanism.

When context is needed, MemGPT dynamically loads relevant chunks from the archive into the core context, then evicts them when no longer needed. This mirrors how operating systems manage RAM and disk storage. The result is token cost savings exceeding 90% compared to naive approaches that cram entire conversation histories into the context window. MemGPT deployments achieve high token cost savings through virtual context management while significantly reducing p95 latency compared to standard long-context models.

### When to Use This

Hierarchical memory becomes essential in long-running conversational agents. If your agent maintains sessions spanning 100+ turns, or if you’re building systems where users return across multiple days or weeks, hierarchical architectures prevent context distraction and control token costs.

Avoid this for simple, isolated tasks. One-shot document summarization doesn’t justify the engineering complexity. The setup overhead only pays dividends at scale.

### Implementation Notes

For H-MEM, you’ll need to implement index generation during memory encoding. Each stored interaction requires metadata tags for routing — domain classification, category labels, and temporal markers. Use sentence transformers to generate embeddings, then train a small classifier to predict routing indices.

For MemGPT, integrate with frameworks like LangChain or build custom function calling interfaces. Your LLM needs explicit commands to `load_context()`, `update_core_memory()`, and `archive_memory()`. Monitor your token consumption before and after—MemGPT deployments typically show 85-95% reductions in context-related token usage.

**Common Pitfall:** Over-indexing. Adding too many hierarchical layers introduces routing errors where relevant memories get misclassified and missed. Start with three layers maximum, expand only if retrieval precision degrades. Monitor your recall metrics closely during the first month of deployment.

Cost implications favor hierarchical systems for high-volume deployments. The upfront engineering investment is 2–3x higher than flat vector storage, but operational token savings compound dramatically. For agents handling 10,000+ conversations per day, hierarchical memory typically pays for itself within 2–3 months through reduced token consumption.

## Knowledge Graphs: When Facts Must Be Exact

Vector similarity is inherently fuzzy. When the agent needs precise factual grounding — medical diagnoses, legal reasoning, financial calculations , semantic similarity produces dangerous approximations. A vector search might return “Drug X treats hypertension” but miss the critical fact that Drug X interacts lethally with another medication the patient is taking. Knowledge graphs enforce structural relationships and enable multi-hop reasoning that vector systems fundamentally cannot achieve.

### How It Works

Vector RAG retrieves based on semantic proximity. If you search for “treatment options for hypertension,” it returns documents containing similar language. GraphRAG retrieves based on explicit relationships stored as nodes and edges in a graph structure.

Consider this scenario: A doctor’s assistant needs to recommend hypertension medication. Vector search finds the most semantically similar content and returns: “Drug X treats hypertension.” Seems helpful.

<Base64-Image-Removed>A graph database showing how an agent will use multi-hop reasoning.

The agent reasons: “Patient A has hypertension. Drug X would be effective, but Patient A is currently taking Drug Z. Drug X and Drug Z have dangerous interactions. I should recommend Drug W instead, which treats hypertension without interacting with Drug Z.”

This is verifiable, multi-hop reasoning that vector similarity cannot achieve. The graph provides an explainable path from query to conclusion, drastically increasing reliability and trustworthiness in high-stakes domains.

The technical mechanism involves entity extraction, relationship mapping, and graph traversal. When ingesting documents, you parse entities (people, places, drugs, diseases) and relationships (treats, causes, contraindicated\_with). These populate a graph database like Neo4j. Queries use Cypher to traverse nodes and edges, following relationship paths.

GraphRAG excels at multi-hop reasoning that vector systems miss entirely. Consider: “Which customers in Chicago ordered products affected by the recent supply chain delay?” A vector search struggles — there’s no single document containing this answer. GraphRAG traverses: Customer nodes → located\_in → Chicago. Customer nodes → ordered → Product nodes. Product nodes → affected\_by → Supply Chain Event. The intersection yields the answer.

Building production GraphRAG requires a robust ETL (Extract-Transform-Load) pipeline. Unstructured text must be transformed into structured entities and relationships. Modern implementations use LLMs for entity extraction, then validate outputs against schema definitions.

[https://miro.medium.com/v2/da:true/39309aa989a0b10efa2291d777f51465d571981b6b92231e51a0846a592cb403https://miro.medium.com/v2/da:true/d3cd1505b3697d277993a9b714cca5440eef772de587a18a64e4a3c58fd8ef49](https://medium.com/plans?source=upgrade_membership---post_li_non_moc_upsell--81ed456bb74f---------------------------------------)

**Critically important:** Use predefined Cypher queries rather than LLM-generated database queries. Hallucinated queries corrupt your graph. Define a fixed query library for common patterns, expanding as needed based on actual usage. This ensures consistent schema formats and substantially reduces the potential for hallucinations in your critical data ingestion pipeline.

Knowledge graphs become essential when factual accuracy and explainability are critical requirements. Medical assistants, legal research tools, and financial advisors need verifiable reasoning paths. If the agent must justify its conclusions by citing a chain of facts, GraphRAG provides that transparency. The ability to show “I recommended X because of facts A, B, and C, which are connected by relationships 1, 2, and 3” is invaluable in regulated industries.

Avoid knowledge graphs for simple Q&A or when latency is paramount. Graph traversal introduces query overhead — multi-hop queries requiring three or more edge traversals can add significant latency compared to vector retrieval. If your use case tolerates occasional imprecision and demands sub-100ms response times, stick with vectors.

### Implementation Notes

Start with a hybrid architecture. Use vector search for fast semantic retrieval, fall back to GraphRAG for complex queries requiring multi-hop reasoning. An orchestration layer decides which backend to query based on query complexity signals such as question length, presence of compound clauses, or explicit relationship indicators like “because,” “related to,” or “connected to.”

For the ETL pipeline, use spaCy or LLM-based extractors to identify entities. Pass extractions through a validation layer checking against your predefined schema before committing to the graph. Implement edge deduplication to prevent erroneous combinations of similar edges between unrelated entities.

**Common Pitfall:** Graph explosion, Unrestricted entity extraction generates millions of low-value nodes that degrade query performance without adding value. Apply relevance filtering and only store entities mentioned multiple times or tagged as high-importance. Monitor graph size and prune aggressively. A well-maintained graph database should have high edge density relative to node count.

Cost-wise, graph databases scale differently than vector stores. Neo4j’s Infinigraph architecture enables horizontal scaling for 100TB+ workloads using property sharding . But hosting graph infrastructure is more expensive than managed vector services like Pinecone. Budget 1.5–2x the infrastructure cost of vector-only approaches, though this is offset by reduced hallucination-related support costs in high-stakes applications.

## Selective Forgetting: Memory as a Strategic Resource

Unbounded memory leads to context distraction and unsustainable costs. Long-lived agents accumulate millions of low-value entries that dilute retrieval quality and inflate storage expenses. Without pruning, your vector database becomes a landfill where finding relevant information becomes progressively harder.

### How It Works

Selective forgetting applies utility scoring to determine which memories to retain and which to prune. The RIF (Recency-Relevance-Frequency) formula combines three factors:

**Recency –** A memory from five minutes ago is more valuable than one from five months ago. It can be implemented using exponential decay:

```
R_i = e^(-λ * t)
```

where `t` is the time since last access and `λ` is a decay constant you tune based on your domain. Fast-moving contexts like customer support need aggressive decay (λ = 0.1). Slower domains like legal research use gentler curves (λ = 0.01).

**Relevance** means semantic similarity, it’s usually the cosine similarity between the memory’s vector embedding and the current query vector.

**Frequency/Utility** tracks how often a memory has been accessed or reflects a manually assigned importance score. For example, a validated procedural memory teaching your agent to handle authentication errors might have high utility regardless of access frequency. This component prevents premature deletion of critical but infrequently-used knowledge.

Combine these into a weighted score:

```
RIF_score = α*R_i + β*E_i + γ*U_i
```

where α, β, γ are tunable weights you adjust based on your domain requirements.

The **Ebbinghaus Forgetting Curve** informs this approach. Human memory loss is steepest shortly after learning, then plateaus. This can be replicated in the agent by applying steep initial decay, then reducing the decay rate for memories that survive the first pruning cycle. Memories accessed multiple times get “reinforced” with lower decay rates ,just like human learning strengthens frequently-recalled information.

<Base64-Image-Removed>Ebbinghaus Forgetting Curve for AI

A critical technical challenge is **temporal vector encoding**. Traditional RAG produces “homogeneous recall” ,retrieving multiple memories that are semantically identical but temporally distinct. Your agent retrieves three instances of “customer asked about shipping” from different dates without distinguishing which is most recent or most relevant.

SynapticRAG solves this by encoding temporal information directly into the vector representation. Each memory vector includes both semantic content and a timestamp component, ensuring retrieval considers both _what_ and _when_. This prevents your agent from confidently citing outdated information simply because it’s semantically similar to the current query.

### When to Use This

Implement forgetting for any long-lived agent expected to operate continuously for weeks or months. Without pruning, memory databases grow unbounded and retrieval degrades. The longer your agent runs, the more critical forgetting becomes. In production deployments, aggressive forgetting typically reduces vector database size by 40–60% after 30 days of operation, cutting hosting costs proportionally.

**Critical caveat:** Some domains legally require perfect recall. Healthcare records, financial transactions, and legal discovery cannot use aggressive forgetting. In these cases, implement tiered archival storage rather than deletion — moving cold data to cheaper storage while maintaining retrievability for compliance purposes.

### Implementation Notes

Start with conservative decay rates and monitor retrieval quality metrics. Track precision (are retrieved memories relevant?) and recall (are you missing critical information?). If precision drops, you’re forgetting too aggressively. If context distraction increases, you’re not forgetting enough. Tune λ iteratively using validation sets.

Run pruning operations during off-peak hours. Recalculating RIF scores and deleting entries is computationally expensive. Schedule nightly batch [jobs](https://jobs.towardsai.net/ "AI Jobs") to evaluate the entire memory database and remove low-scoring entries. Monitor the operation’s impact on query latency the next day.

Track cost savings explicitly. Each pruned memory reduces storage costs and speeds up future retrievals. Create dashboards showing memory database size over time, average RIF scores, and retrieval performance metrics.

**Common Pitfall:** Premature deletion of useful memories. Implement a soft-delete mechanism first. Flag memories for deletion but retain them in an archive. Monitor which archived memories get requested. If access patterns show you’re frequently needing archived data, your decay parameters are too aggressive. Adjust and retest before implementing hard deletes.

## Choosing Your Architecture

The right memory architecture depends on your constraints, not abstract preferences. Here’s how to decide.

**Start with your agent’s task complexity.** If you’re building a simple one-shot document summarizer, stick with basic vector RAG. The engineering overhead of hierarchical memory or knowledge graphs isn’t justified. Your agent processes isolated requests with no continuity between interactions. Standard semantic search handles this perfectly.

**If your agent maintains conversational state across 100+ turns,** hierarchical memory becomes essential. MemGPT’s OS-paging approach dramatically reduces token costs while maintaining coherence. Without hierarchical organization, context distraction will degrade response quality and inflate bills. Implement H-MEM or MemGPT as your baseline architecture for any long-running conversational system.

**If your agent needs factual accuracy and explainable reasoning** — medical assistants, legal research, financial advisors — knowledge graphs become essential. The latency cost of graph traversal is justified by the fidelity gain and regulatory requirements for explainability. You cannot afford the hallucination risk inherent in fuzzy vector similarity. Hybrid architectures combining vector retrieval for speed and GraphRAG for precision offer the best balance.

**For multi-agent systems where coordination matters,** implement shared memory spaces with procedural memory transfer. Without this, agents duplicate work and maintain inconsistent state. Shared memory in multi-agent systems introduces distributed systems challenges: race conditions, consistency guarantees, and coordination overhead. Simple shared databases create bottlenecks. Production systems need conflict-free replicated data types (CRDTs) or event-sourcing patterns to maintain coherence across agents without introducing single points of failure.

**Consider your operational constraints.** Latency-sensitive applications favor vector-only architectures despite lower fidelity. If you must respond within 200ms, multi-hop graph traversal isn’t viable. Use vectors for retrieval and post-process results to detect contradictions.

**Budget conscious?** Start simple and scale up. Begin with basic vector RAG. Add hierarchical memory when token costs exceed your threshold. Introduce knowledge graphs only when factual errors create measurable user impact. Each architectural addition increases maintenance burden. Optimize for your current pain points, not hypothetical future needs.

## Production Tradeoffs

Three dimensions dominate production memory architecture decisions: latency, cost, and operational complexity.

### Latency vs Fidelity

Vector search delivers p95 latencies under 50ms but produces fuzzy, sometimes hallucinated results. Knowledge graph traversal provides precise, explainable answers but introduces query overhead. Multi-hop graph queries requiring three or more edge traversals can add substantial latency compared to vector-only retrieval.

**When is the overhead worth it?** High-stakes decisions justify latency. A medical diagnosis tool should spend extra milliseconds traversing a knowledge graph to ensure drug interaction safety. A chatbot answering “What’s your return policy?” should use fast vector retrieval.

Hybrid architectures split the difference. Simple queries route to vector search. Complex queries trigger graph traversal. The orchestration layer adds 10–20ms overhead but optimizes the overall latency-fidelity tradeoff. Expect 30–40% of queries to use graphs, 60–70% to use vectors in typical deployments.

### Cost Analysis

Token consumption drives LLM costs. Reflection loops consume tokens but enable smaller base models. MemGPT-style paging saves 90% compared to stuffing entire conversation histories into context. A conversation using 10,000 tokens with naive context management drops to 1,000 tokens with hierarchical memory.

Memory storage costs scale differently across architectures. Vector databases like Pinecone charge per indexed vector and per query. Knowledge graphs like Neo4j cost more for managed instances handling moderate query volumes. However, integrated systems that leverage both graph structures and vector indexes within a single platform (like Weaviate) often simplify capacity planning and reduce infrastructure overhead compared to managing disparate backends.

**The hidden calculation:** If graph integration prevents even a single critical error in a medical or financial application, the ROI justifies the infrastructure expense. Calculate the cost of errors in your domain, not just the cost of infrastructure.

### Operational Complexity

ETL pipelines for knowledge graphs require ongoing maintenance. Entity schemas evolve as your domain expands. Extraction logic must adapt to new document formats. Budget 20–30% of your engineering time for graph maintenance once deployed.

Horizontal scaling presents challenges. Modern graph databases like Neo4j’s Infinigraph use property sharding to distribute graph data across clusters while preserving logical consistency. But coordinating distributed graph queries introduces complexity. Vector databases scale more easily — add shards independently with minimal coordination overhead.

Managing disparate backends compounds complexity. Your system needs vector databases for semantic memory, graph databases for factual memory, and code repositories for procedural memory. Each requires separate backup strategies, monitoring, and security policies.

Simple vector RAG lets engineers iterate fast. Hierarchical memory and knowledge graphs require architectural planning, schema design, and performance tuning. Velocity drops 30–50% during initial implementation. The complexity pays dividends in production reliability and user satisfaction, but only after the learning curve.

## Conclusion

Memory isn’t peripheral storage anymore. It’s the reasoning engine that determines whether your agent maintains coherence across thousands of interactions or collapses into incoherent noise.

Start simple. Use vector RAG until you hit its limits, context distraction at scale, factual errors that matter, or token costs that exceed your budget. Then add complexity deliberately. Hierarchical memory for long-running conversations. Knowledge graphs for high-fidelity reasoning. Reflection loops for quality control. Forgetting curves for operational sustainability.

The future of agent memory draws from neuroscience and embodied cognition. Multimodal sensing such as integrating visual, auditory, and tactile inputs requires memory systems that unify diverse modalities. Spatio-temporal memory lets agents operating in physical environments track object locations and movements over time, supporting low-level skills like object manipulation and navigation over extended periods. These advances will push agents from linguistic reasoning toward genuine environmental understanding.

But those capabilities build on the foundations covered here. By Mastering hierarchical routing, knowledge graph integration, and selective forgetting first, it’s possible to absorb what comes next easily.

[Join thousands of data leaders](https://towardsai.net/subscribe "Artificial Intelligence Newsletter") on the [AI newsletter](https://towardsai.net/subscribe "AI Newsletter"). Join over 80,000 subscribers and keep up to date with the latest developments in AI. From research to projects and ideas. If you are building an [AI startup](https://sponsors.towardsai.net/ "AI Startups"), an AI-related product, or a service, we invite you to consider becoming a [sponsor](https://sponsors.towardsai.net/ "Helping Scale AI and Technology Startups").

Published via [Towards AI](https://towardsai.net/)

[Towards AI - Medium](https://towardsai.net/p/tag/towards-ai-medium)

* * *

# Towards AI Academy

### We Build Enterprise-Grade AI. We'll Teach You to Master It Too.

15 engineers. 100,000+ students. Towards AI Academy teaches what actually survives production.

**Start free — no commitment:**

→ [6-Day Agentic AI Engineering Email Guide](https://email-course.towardsai.net/?utm_source=towardsai.net&utm_medium=footer_cta) — one practical lesson per day

→ [Agents Architecture Cheatsheet](https://academy.towardsai.net/products/digital_downloads/agents-cheatsheet/?utm_source=towardsai.net&utm_medium=footer_cta) — 3 years of architecture decisions in 6 pages

**Our courses:**

→ [AI Engineering Certification](https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev?utm_source=towardsai.net&utm_medium=footer_cta) — 90+ lessons from project selection to deployed product. The most comprehensive practical LLM course out there.

→ [Agent Engineering Course](https://academy.towardsai.net/courses/agent-engineering?utm_source=towardsai.net&utm_medium=footer_cta) — Hands on with production agent architectures, memory, routing, and eval frameworks — built from real enterprise engagements.

→ [AI for Work](https://academy.towardsai.net/courses/ai-business-professionals?utm_source=towardsai.net&utm_medium=footer_cta) — Understand, evaluate, and apply AI for complex work tasks.

_**Note:** Article content contains the views of the contributing authors and not Towards AI._

* * *

### Related posts

[<Base64-Image-Removed>](https://towardsai.net/p/machine-learning/the-l1-loss-gradient-explained-from-scratch "The L1 Loss Gradient, Explained From Scratch")

[Artificial Intelligence](https://towardsai.net/ai/artificial-intelligence), [Latest](https://towardsai.net/ai/l), [Machine Learning](https://towardsai.net/ai/machine-learning)

### [The L1 Loss Gradient, Explained From Scratch](https://towardsai.net/p/machine-learning/the-l1-loss-gradient-explained-from-scratch)

[Utkarsh Mittal](https://towardsai.net/p/author/utkarshmittal)

[17 likes](https://towardsai.net/wp-admin/admin-ajax.php?action=process_simple_like&post_id=50639&nonce=192ee09830&is_comment=0&disabled=true "Like")

[<Base64-Image-Removed>](https://towardsai.net/p/machine-learning/your-postcode-is-deciding-your-care-i-built-a-pipeline-to-prove-it "Your Postcode Is Deciding Your Care. I Built a Pipeline to Prove It.")

[Data Engineering](https://towardsai.net/ai/data-engineering), [Data Science](https://towardsai.net/ai/data-science), [Latest](https://towardsai.net/ai/l), [Machine Learning](https://towardsai.net/ai/machine-learning)

### [Your Postcode Is Deciding Your Care. I Built a Pipeline to Prove It.](https://towardsai.net/p/machine-learning/your-postcode-is-deciding-your-care-i-built-a-pipeline-to-prove-it)

[Yusuf Ismail](https://towardsai.net/p/author/yusufismail)

[13 likes](https://towardsai.net/wp-admin/admin-ajax.php?action=process_simple_like&post_id=50641&nonce=192ee09830&is_comment=0&disabled=true "Like")

[<Base64-Image-Removed>](https://towardsai.net/p/machine-learning/i-directed-ai-agents-to-build-a-tool-that-stress-tests-incentive-designs-heres-what-it-found "I Directed AI Agents to Build a Tool That Stress-Tests Incentive Designs. Here’s What It Found.")

[Artificial Intelligence](https://towardsai.net/ai/artificial-intelligence), [Latest](https://towardsai.net/ai/l), [Machine Learning](https://towardsai.net/ai/machine-learning)

### [I Directed AI Agents to Build a Tool That Stress-Tests Incentive Designs. Here’s What It Found.](https://towardsai.net/p/machine-learning/i-directed-ai-agents-to-build-a-tool-that-stress-tests-incentive-designs-heres-what-it-found)

[Selfradiance](https://towardsai.net/p/author/selfradiance)

[16 likes](https://towardsai.net/wp-admin/admin-ajax.php?action=process_simple_like&post_id=50643&nonce=192ee09830&is_comment=0&disabled=true "Like")

[https://miro.medium.com/v2/resize:fit:700/0*HlWi3rYCiRXBiYIR](https://towardsai.net/p/machine-learning/long-term-vs-short-term-memory-for-ai-agents-a-practical-guide-without-the-hype "Long-Term vs Short-Term Memory for AI Agents: A Practical Guide Without the Hype")

[Artificial Intelligence](https://towardsai.net/ai/artificial-intelligence), [Latest](https://towardsai.net/ai/l), [Machine Learning](https://towardsai.net/ai/machine-learning)

### [Long-Term vs Short-Term Memory for AI Agents: A Practical Guide Without the Hype](https://towardsai.net/p/machine-learning/long-term-vs-short-term-memory-for-ai-agents-a-practical-guide-without-the-hype)

[Andrii Tkachuk](https://towardsai.net/p/author/andriitkachuk)

[19 likes](https://towardsai.net/wp-admin/admin-ajax.php?action=process_simple_like&post_id=50645&nonce=192ee09830&is_comment=0&disabled=true "Like")

### GDPR CCPA Statement

In order for Towards AI to work properly, we log user data. By using Towards AI, you agree to our [Privacy Policy](https://towardsai.net/privacy), including our cookie policy.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="memory-systems-for-ai-agents-what-the-research-says-and-what.md">
<details>
<summary>Memory Systems for AI Agents: What the Research Says and What You Can Actually Build</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://stevekinney.com/writing/agent-memory-systems>

# Memory Systems for AI Agents: What the Research Says and What You Can Actually Build

[siGithub](https://github.com/stevekinney) [siInstagram](https://instagram.com/stevekinney) [siX](https://twitter.com/stevekinney) [Visit LinkedIn profile](https://linkedin.com/in/stevekinney) [siYoutube](https://www.youtube.com/channel/UChXe-1_Jh91Z_CM3ppH39Xg)

## Further Reading

- April 6, 2026 [Claude Ultraplan: Planning in the Cloud, Executing Wherever](https://stevekinney.com/writing/claude-ultraplan)
- April 5, 2026 [Playwright vs. Chrome DevTools MCP: Driving vs. Debugging](https://stevekinney.com/writing/driving-vs-debugging-the-browser)
- March 30, 2026 [Entering the Mind of Ralph Wiggum](https://stevekinney.com/writing/the-ralph-loop)
- March 24, 2026 [Memory Systems for AI Agents: What the Research Says and What You Can Actually Build](https://stevekinney.com/writing/agent-memory-systems)
- March 23, 2026 [Temporal's Developer Skill Is a Promising First Draft](https://stevekinney.com/writing/temporal-developer-skill)
- March 18, 2026 [The Anatomy of an Agent Loop](https://stevekinney.com/writing/agent-loops)
- March 16, 2026 [Agent Skills, Stripped of Hype](https://stevekinney.com/writing/agent-skills)
- March 15, 2026 [Designing a Build System That Runs Untrusted Code](https://stevekinney.com/writing/designing-a-system-to-run-untrusted-code)
- March 12, 2026 [Designing an AI Gateway and Durable Workflow System](https://stevekinney.com/writing/ai-gateway-durable-workflows)
- March 11, 2026 [MCP Apps and the Missing Middle of AI Tooling](https://stevekinney.com/writing/mcp-apps)
- March 10, 2026 [My Ridiculous AI-Assisted Development Workflow](https://stevekinney.com/writing/ai-assisted-development-workflow)
- March 8, 2026 [build-temporal-workflow: Faster Temporal Workflow Bundling with esbuild](https://stevekinney.com/writing/build-temporal-workflow)
- March 5, 2026 [Prompt Engineering Across the OpenAI, Anthropic, and Gemini APIs](https://stevekinney.com/writing/prompt-engineering-frontier-llms)
- January 11, 2026 [Introducing Prose Writer](https://stevekinney.com/writing/introducing-prose-writer)
- May 13, 2025 [Cursor Rules for Writing Temporal Workflows with TypeScript](https://stevekinney.com/writing/cursor-rules-temporal-typescript)

[RSS Feed](https://stevekinney.com/writing/rss)

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

<research_source type="scraped_from_research" phase="exploitation" file="the-three-memory-systems-every-production-ai-agent-needs.md">
<details>
<summary>The Three Memory Systems Every Production AI Agent Needs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://tianpan.co/blog/long-term-memory-types-ai-agents>

# The Three Memory Systems Every Production AI Agent Needs

```markdown
Most AI agents fail the same way: they work perfectly in demos and fall apart after the tenth real conversation. The agent that helped a user configure a billing integration last Tuesday has no idea who that user is today. It asks for their company name again. Then their plan tier. Then re-explains concepts the user already knows. The experience degrades from "useful assistant" to "chatbot with amnesia."

https://opengraph-image.blockeden.xyz/api/og-tianpan-co?title=The%20Three%20Memory%20Systems%20Every%20Production%20AI%20Agent%20Needs

The instinct is to throw more context at the problem — stuff the conversation history into the prompt and call it solved. That works until it doesn't. At scale, full-context approaches become prohibitively expensive, and more troublingly, performance degrades as input grows. Research shows LLM accuracy drops measurably as context length increases, even within a model's advertised limits. A 1M-token context window is not a memory system.

The agents that work in production treat memory as a first-class architectural concern, not an afterthought. And the ones that get it right distinguish between three fundamentally different types of information that need to persist — each with different storage patterns, retrieval strategies, and decay characteristics.

## Why the Three-Way Distinction Matters

Cognitive science has long recognized that human memory is not monolithic. Episodic memory handles autobiographical events ("I had that meeting Tuesday"). Semantic memory handles general knowledge ("Paris is the capital of France"). Procedural memory handles skills ("how to ride a bike"). These systems operate differently, decay differently, and fail differently.

AI agents benefit from the same taxonomy — not as a philosophical exercise, but because each memory type maps directly to a different engineering problem.

Treating all persistent information the same way is a common mistake. If you store everything as semantic facts in a knowledge graph, you lose the temporal context that makes past interactions meaningful. If you store everything as episodic conversation logs, retrieval becomes expensive and noisy at scale. If you have no procedural layer, your agent never learns to stop making the same mistakes.

## Episodic Memory: The Log of What Happened

Episodic memory stores specific interactions with their context intact: what was asked, what was answered, what tools were called, what the outcome was, and when it all happened.

This is the memory type that makes agents feel like they know you. When a customer support agent recalls that a user called about a billing discrepancy six weeks ago and already received a credit, that's episodic memory. When a coding assistant remembers that you specifically prefer async/await over promise chains and you mentioned this during a session three weeks back, that's episodic memory.

The implementation challenge is threefold. First, episodic memories need timestamps — the temporal dimension is load-bearing. "The user said they were evaluating our product" means something different if it was said yesterday versus eight months ago. Second, episodic stores grow without bound. Without deliberate pruning or summarization, retrieval degrades over time as the signal-to-noise ratio falls. Third, individual episodes need to be accessible by both semantic similarity (what topics were discussed) and temporal proximity (what happened recently).

Production implementations typically combine vector stores for semantic retrieval with temporal metadata filters. The retrieval query isn't just "find memories similar to this" — it's "find memories similar to this, weighted toward recent ones, excluding anything older than a relevance threshold."

## Semantic Memory: The Knowledge That Outlasts Any Single Conversation

Semantic memory contains facts and knowledge that have been extracted from experience but are no longer tied to the specific episode that produced them. It answers "what do I know about this user/domain/entity" rather than "what happened."

Consider how this consolidation works in practice. A user mentions in passing during a session that they're migrating from AWS to GCP. That's an episodic event. But the fact "this user's infrastructure is GCP-based" becomes a semantic fact that should inform every future response — it doesn't need the episode around it to be useful. Keeping it episodic means every retrieval has to drag along unnecessary context. Promoting it to semantic memory makes it lighter and more durable.

Semantic memory in agent systems is typically implemented as structured records in a graph database or key-value store. The graph approach is particularly powerful because it captures relationships: "user A works at company B, which uses tool C, which has known incompatibility with integration D." A flat key-value store can't represent that relational structure.

The wrinkle is that semantic "facts" can go stale. Users change jobs, companies change tech stacks, preferences evolve. A fact that was true eight months ago may now be actively misleading. This is where many production implementations add a confidence decay mechanism: semantic memories become less authoritative over time unless they're reinforced by new episodic evidence. If no interaction has touched a fact in six months, it gets downweighted in retrieval or flagged for re-verification.

## Procedural Memory: Learning What Works

Procedural memory is the most underused of the three in current agent architectures, and arguably the most valuable for systems that need to improve over time.

Procedural memory stores _how to do things_ — specifically, patterns that have proven effective in this context with this user or domain. Not general knowledge about how to write code, but specific learned preferences: this user always wants unit tests included with any function they request; this organization's API gateway rejects payloads above 4KB so always paginate; this customer's data schema uses snake\_case everywhere.

The distinction from semantic memory is subtle but important. "The user prefers Python" is semantic — it's a fact about the user. "When writing data pipeline code for this user, use Polars instead of Pandas because past responses using Pandas were flagged as unhelpful" is procedural — it's a learned heuristic about _what to do_.

In human cognition, procedural memory is implicit and automatic. For AI agents, it has to be made explicit and retrievable. Some implementations achieve this through reinforcement signals: when a user rates a response positively, the approach that generated it gets encoded as a procedure. Others use self-critique loops where the agent periodically reviews its interaction history and extracts generalizable patterns.

The payoff is compounding: an agent with well-maintained procedural memory gets measurably better with use. This is the difference between a tool and an assistant that learns your workflow.

## The Retrieval Problem: Balancing Three Competing Signals

Having three memory stores doesn't help if you can't retrieve from them accurately under load. The retrieval layer is where most production systems fail.

Naive vector similarity search — embed the current query, find the nearest stored memories — works acceptably for small stores. As the store grows into thousands or millions of records, it produces increasingly noisy results. Relevant memories get crowded out by topically-similar-but-contextually-irrelevant ones.

Effective retrieval combines three independent signals:

**Relevance** — semantic similarity between the current context and stored memories, measured via embedding cosine similarity. This is the baseline.

**Recency** — how recently a memory was created or last accessed. Implemented as exponential decay: a memory from yesterday is far more likely to matter than one from a year ago, even if the year-old memory is more semantically similar. A decay factor around 0.995 per hour is a reasonable starting point.

**Importance** — how significant the memory was when it was formed. Some implementations use an LLM to score importance at write time; others infer importance from user behavior (a message the user sent three times is more important than one they sent once).

Combining these three signals into a weighted retrieval score consistently outperforms similarity-only approaches. The challenge is calibrating the weights: too much recency bias and the agent forgets important long-term context; too little and it gets distracted by stale information.

Research on the "Memory Trilemma" adds a sobering data point: for the first 30-150 conversations, simply dumping all history into the context window achieves 70-82% accuracy. Switching to retrieval-based approaches can initially drop this to 30-45%. The sophisticated retrieval system needs time to be worth the complexity. Build the full context baseline first, measure it, then replace specific failure modes with targeted memory retrieval rather than adopting a complex architecture from day one.

## The Forgetting Question

A memory system that only accumulates is not a memory system — it's a log. Production agents need principled forgetting.

The Ebbinghaus forgetting curve, which models how humans forget information over time without reinforcement, has a practical analog in agent memory. Information that isn't accessed decays. Information that is regularly retrieved gets strengthened. This mirrors how useful information in practice stays relevant: a user's active preferences keep getting reinforced through interactions, while preferences from a project they finished a year ago naturally fade.

Implementing decay doesn't mean deleting memories. It means downweighting them in retrieval scoring until they fall below a threshold where they're effectively invisible — but can be recovered if specifically requested. This preserves correctness (you can always look up the full history) while preventing stale information from polluting active reasoning.

The operational benefit extends to cost. Memory stores that decay intelligently stay manageable. One education platform reduced token costs by 40% by implementing tiered memory with decay, routing recent and high-importance memories to hot storage while archiving older ones.

## Practical Architecture Advice

Three practical decisions that matter more than the specific tools:

**Separate your stores by type.** Keep episodic logs, semantic facts, and procedural patterns in different stores with different retrieval strategies. Mixing them into a single vector database makes retrieval harder and obscures what kind of information you actually have.

**Write time is as important as read time.** Most teams design memory systems read-first. The quality of retrieval depends entirely on the quality of what was stored. Invest in extraction pipelines that pull semantic facts from raw conversation logs, assign importance scores, and tag temporal context at write time.

**Build measurement before you build sophistication.** Before implementing multi-store architectures with weighted retrieval and decay functions, establish a baseline accuracy metric on representative conversations. The Memory Trilemma effect is real — complexity doesn't automatically mean better results. Measure each component's contribution before adding the next one.

## What This Unlocks

The business case for long-term agent memory isn't abstract. Agents with all three memory types working correctly exhibit genuinely different behavior: they remember past conversations, they accumulate knowledge about users and domains, and they get better at their job over time.

This is what separates an agent that runs a useful demo from one that users actually want to use every day. The former impresses in a 20-minute walkthrough; the latter compounds value over weeks and months because it retains what it learns.

The three-memory framework is not the only way to think about this problem, but it provides a practical vocabulary for discussing what kind of persistence a system needs and why. Episodic for continuity, semantic for knowledge, procedural for improvement. Each requires different engineering, different retrieval strategies, and different decay logic. Get all three right and the agent starts feeling less like a tool and more like someone who's been paying attention.

**References:**

- [https://www.tribe.ai/applied-ai/beyond-the-bubble-how-context-aware-memory-systems-are-changing-the-game-in-2025](https://www.tribe.ai/applied-ai/beyond-the-bubble-how-context-aware-memory-systems-are-changing-the-game-in-2025)
- [https://arxiv.org/abs/2512.13564](https://arxiv.org/abs/2512.13564)
- [https://arxiv.org/pdf/2502.06975](https://arxiv.org/pdf/2502.06975)
- [https://redis.io/blog/ai-agent-memory-stateful-systems/](https://redis.io/blog/ai-agent-memory-stateful-systems/)
- [https://www.salesforce.com/blog/agentic-memory-agents/](https://www.salesforce.com/blog/agentic-memory-agents/)
- [https://mem0.ai/blog/state-of-ai-agent-memory-2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [https://arxiv.org/abs/2502.12110](https://arxiv.org/abs/2502.12110)
- [https://www.letta.com/blog/agent-memory](https://www.letta.com/blog/agent-memory)
- [https://serokell.io/blog/design-patterns-for-long-term-memory-in-llm-powered-architectures](https://serokell.io/blog/design-patterns-for-long-term-memory-in-llm-powered-architectures)
- [https://research.trychroma.com/context-rot](https://research.trychroma.com/context-rot)
- [https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [https://arxiv.org/html/2508.15294v1](https://arxiv.org/html/2508.15294v1)
```

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="three-memory-architectures-for-ai-companions-pgvector-scratc.md">
<details>
<summary>Three Memory Architectures for AI Companions (pgvector, Scratchpad, Filesystem)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.emotionmachine.com/blog/how-memory-works>

# Three Memory Architectures for AI Companions (pgvector, Scratchpad, Filesystem)

This is a walkthrough of how we built memory at Emotion Machine, from our first pgvector-backed semantic memory through a ChatGPT-style scratchpad to a full filesystem-based context system for agentic workflows. Three versions, each one a response to the limitations of the last, each one shaped by a different mental model of what "memory" should mean for an AI companion.

I'm writing this partly to document what we've built and partly because the broader field is moving fast and I want to have our own reference point for where we stand relative to it. The memory problem in AI companions is, in my view, the single hardest product problem in this space. The question that matters most is what to remember, when to remember it, and how to surface it without making the companion feel like it's reading from a dossier.

* * *

## The landscape

Before getting into our own systems, it's worth noting where the field is right now, because it influenced every design choice we made.

The MemGPT paper (Packer et al., 2023) was probably the most useful framing for us early on. The core idea: treat the LLM's context window like RAM and external storage like disk, then let the agent manage its own paging. Two tiers: main context (always visible, fixed-size, writable via tool calls) and external context (needs explicit retrieval). The agent uses function calls like `core_memory_append`, `archival_memory_search`, `conversation_search` to move things in and out. Simple, elegant, maps cleanly onto operating system concepts most engineers already understand.

We've found it useful to think about memory through a cognitive science lens: working memory (what's in the context window right now), semantic memory (facts), episodic memory (experiences), procedural memory (instructions/skills). These map naturally onto the systems we've built, and they're useful abstractions for companion developers. But we've been pragmatic about naming. Sometimes "scratchpad" or "hot context" communicates intent better than "episodic memory" does. If calling something an "agenda" makes more sense for the workflow you're building on top, call it an agenda.

Anthropic's context engineering post points to the meta-problem: context is a finite resource with diminishing marginal returns. Every token competes for attention. Context rot is real. As you stuff more into the window, recall degrades. Their techniques (compaction, structured note-taking, sub-agent architectures) directly influenced V3's design. Claude Code's approach of keeping lightweight identifiers (file paths, grep patterns) and loading data just-in-time rather than pre-loading everything is basically what we converged on independently.

There's also an active debate right now between the "file interfaces are all you need" camp (Anthropic, Letta, LlamaIndex, where benchmarks show `grep` and `ls` outperforming specialized retrieval tools) and the "filesystems are just bad databases" camp (Dax from OpenCode, swyx, and others who rightly point out you'll accidentally reinvent search indexes, transaction logs, and locking mechanisms). We've landed on a pragmatic middle ground: real files for agent-mode navigation, but backed by a database cache for fast chat reads. More on this below.

The "Everything is Context" paper (Xu et al.) formalized what we'd been feeling intuitively: that context engineering needs a persistent, governed infrastructure with clear lifecycle management: history (immutable logs) → memory (structured, indexed views) → scratchpad (temporary workspace). Their file-system abstraction is the academic version of what we built in V3.

One thing worth calling out: most of the recent discourse skews toward agentic, filesystem-heavy, long-horizon memory architectures. That's exciting, but for the majority of companion-like interactions (chat, voice, real-time back-and-forth) a simpler scratchpad model like V2 covers most of what you need. A curated list of facts about the user, injected into every turn, with an LLM managing what gets added and removed. It's fast, transparent, and easy for developers to customize. We think V2 is the right starting point for most companion use cases, and V3 is for when your companion needs to do real work autonomously.

* * *

## V1: pgvector and importance scoring

V1 was our first real attempt at companion memory. The mental model was classic RAG with a twist: instead of treating all retrieved information equally, we added an importance scoring system that lets the companion weigh what matters.

Here, every piece of information that might be worth remembering gets scored by a small LLM (gpt-4o-mini) on a 1-10 importance scale. Identity facts, commitments, deadlines score 9-10. Strong preferences, goals score 7-9. Mild interests, medium-term tasks land at 5-7. Chit-chat and transient details get 1-4. If the score clears a threshold (0.55 by default), the content gets embedded via `text-embedding-3-small` and stored in a pgvector column alongside the importance score, a user weight, modality tag, and timestamp metadata.

We also built heuristic floors to guard against the LLM under-scoring things that are clearly important. If someone says "my name is" something, that gets a floor of 0.85 regardless of what the LLM thinks. Goals ("my goal is", "remind me") get 0.75. Constraints ("I can't", "I never") get 0.65. Preferences ("my favorite", "I love") get 0.60. These floors are conservative and based on pattern matching, but they catch the cases where the LLM just doesn't see what a human companion developer would obviously want remembered.

Retrieval uses a two-stage algorithm. Stage one: pgvector's HNSW approximate nearest neighbor search pulls ~300 candidates. Stage two: re-rank using a composite score: `similarity * importance * weight_user * lambda_recency^(hours_since_access)`. The recency decay (lambda=0.995 by default) means older memories gradually fade unless they keep getting accessed. Results above a minimum saliency threshold get returned, top-k (default 15).

Retrieval doesn't fire on every turn. There's a gating heuristic: keyword triggers ("remember", "my name", "do you know") or periodic cadence (every ~2 turns or 30-second gaps). This was important for latency: you don't want to do a vector search on "haha yeah" or "ok sounds good."

All ingestion runs asynchronously through Modal workers. The user never waits for memory processing. This was a hard requirement from the beginning: memory ingestion should be invisible to the conversation flow.

The knowledge base (document retrieval for PDFs, FAQs, reference material) runs on a separate system: OpenAI's vector store API. Files get uploaded, automatically chunked (800 tokens, 400 overlap), embedded, and indexed for hybrid search (keyword + semantic, combined via Reciprocal Rank Fusion). This is conceptually separate from personal memory. It's the companion's reference library, not its memory of the user.

```
                              V1: pgvector memory

  Conversation Turn
        │
        ▼
  ┌─────────────┐    no     ┌──────────────────┐
  │ Gate check: │───────────│  Skip retrieval,  │
  │ should we   │           │  respond directly │
  │ retrieve?   │           └──────────────────┘
  └─────┬───────┘
        │ yes
        ▼
  ┌─────────────┐           ┌──────────────────┐
  │  Embed      │──────────▶│  pgvector HNSW   │
  │  query      │           │  ~300 candidates  │
  └─────────────┘           └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │  Re-rank:        │
                            │  sim × importance │
                            │  × weight × decay│
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │  Top-k memories  │
                            │  → system prompt │
                            └──────────────────┘

  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  Async Ingestion (background, never blocks user)

  User/Assistant message
        │
        ▼
  ┌─────────────┐           ┌──────────────────┐
  │ LLM scores  │──────────▶│  Heuristic floor  │
  │ importance  │           │  (identity: 0.85  │
  │ (1-10)      │           │   goals: 0.75...) │
  └─────────────┘           └────────┬─────────┘
                                     │ above threshold?
                                     ▼
                            ┌──────────────────┐
                            │  Embed + store   │
                            │  in pgvector     │
                            └──────────────────┘
```

V1 works. It's been in production, it handles the basics of "remember what the user told you" competently. But it has real limitations:

1. Selective retrieval means the companion can miss things that are important but don't match the current query embedding well. You can crank up top\_k, but then you're injecting a lot of marginal memories into the context window.
2. The importance scoring adds latency and cost to ingestion, and the rubric doesn't always map to what matters for a specific companion use case, it needs to be adjusted.

* * *

## V2: the scratchpad

V2 was inspired by ChatGPT's memory. The core insight: instead of selectively retrieving from a large pool via vector search, just maintain a small, curated list of semantic entries and inject the entire thing into the system prompt every turn.

V2's bigger shift was moving from "companions and conversations" to "relationships." A Relationship is the unit of persistent state: one user paired with one companion, surviving across sessions, devices, and time. Each relationship carries three buckets of state: a developer-owned Profile (structured data that persists forever), Memory (the scratchpad, semantic entries, also forever), and Session State (temporary, cleared when session ends).

The scratchpad itself is a flat list of typed entries. Each entry has content, a type (identity, preference, goal, event, relationship, other), and timestamps. After every conversation turn, an async Modal worker runs: it fetches the current entries, feeds them along with the latest user/assistant messages to an LLM (default: gemini-2.0-flash), and the LLM returns a JSON blob of operations: add new entries, update existing ones, delete stale ones. The whole thing runs in the background, never blocking the user response.

Retrieval is simple: load all entries, format as a bulleted list, inject into the system prompt. No gating, no vector search, no relevance scoring. The entire scratchpad is always visible to the companion. This trades off scalability (you can't have 10,000 entries in the scratchpad) for simplicity and full context visibility.

Developer customization is straightforward. You can override the ingestion prompt to control what gets stored, when, and how. You can specify entry types with examples: "Memory type: personal relation → Mark has a happy friendship with his sister, Ana." "Memory type: major event → Mark got into college at MIT." Users can also directly ADD, UPDATE, DELETE entries through the API or UI.

Context assembly in V2 became a layered system. Bottom up: core system prompt, priority behavior injections, memory context (V1 retrieved or V2 full scratchpad), knowledge context (if relevant), profile, session state, recent messages, current user message. Each layer is independently pluggable. The orchestrator runs them in parallel and composes the final prompt.

V2 also introduced the behavior system (priority behaviors that inject into prompt before LLM runs, async behaviors that fire after), auto-summarization (incremental summaries at 200/400/600 messages), and a config cascade (turn > relationship > companion). These aren't memory per se, but they're part of the same context engineering problem.

```
                            V2: scratchpad memory

  Every Conversation Turn
        │
        ├───────────────────────────────────────┐
        │                                       │
        ▼                                       ▼
  ┌─────────────┐                     ┌──────────────────┐
  │ Load full   │                     │ Async worker     │
  │ scratchpad  │                     │ (background)     │
  │ (cached 30s)│                     │                  │
  └──────┬──────┘                     │ Feeds turn to LLM│
         │                            │        │         │
         ▼                            │        ▼         │
  ┌──────────────┐                    │ ┌──────────────┐ │
  │ Format as    │                    │ │ LLM returns  │ │
  │ bullet list  │                    │ │ operations:  │ │
  │              │                    │ │  ADD / UPDATE│ │
  │ Inject into  │                    │ │  / DELETE    │ │
  │ system prompt│                    │ └──────┬───────┘ │
  │ (all entries)│                    │        │         │
  └──────┬──────┘                     │        ▼         │
         │                            │ ┌──────────────┐ │
         ▼                            │ │ Apply ops    │ │
  ┌──────────────┐                    │ │ to DB        │ │
  │ LLM responds │                    │ └──────────────┘ │
  │ with full    │                    └──────────────────┘
  │ memory       │
  │ visibility   │
  └──────────────┘

  Scratchpad entries: [ identity | preference | goal | event | relationship | other ]
  Sorted by: last modified (newest first)
```

The trade-offs of V2 vs V1:

- V2 is simpler, gives full visibility, and makes it easy to reason about what the companion "knows" at any given moment. V1 is better for large memory stores where you can't inject everything.
- V2's LLM-managed ADD/UPDATE/DELETE is more intuitive than V1's importance scoring. The LLM decides what's worth keeping, not a rubric.
- V2 is per-relationship (correct abstraction). V1 was per-companion (wrong abstraction, fixed later).
- V2's weakness is scale. If a relationship generates hundreds of entries, you're burning tokens on the full list every turn. But given how much context is fed to agents context window already, this might not be an issue. V1 only scales better here because it's selective but it will be noisy.

* * *

## V3: the filesystem

V3 is a different animal. It emerged from the shift to agent mode, where the companion autonomously performs complex tasks (research, tool use, multi-step workflows) inside a sandboxed environment. The memory system had to change because the interaction model changed. Agents need to navigate information on demand.

The core idea: materialize all context as real files in a Modal Volume mounted at `/em/`. Actual files on disk that the agent browses with bash. `ls /em/memory/`, `grep "preference" /em/profile/user.yaml`, `cat /em/tools/weather_api/spec.yaml`. This works because LLMs are post-trained extensively on code and CLI operations. They know how to navigate filesystems. Letta's benchmarks confirmed this: `grep` and `ls` outperform specialized memory/retrieval tools.

The filesystem structure:

```
/em/
├── memory/
│   ├── hot_context.md      # agent-curated relationship summary
│   └── scratchpad.md       # session working notes
├── knowledge/documents/    # uploaded PDFs, docs
├── profile/user.yaml       # user profile
├── workspace/
│   ├── AGENTS.md           # developer-defined guidelines
│   └── outputs/            # agent-generated files
├── tools/                  # em-provided, developer, agent-created
├── .claude/skills/         # Claude Code SDK skills
├── .git/                   # version control
└── .locks/                 # concurrency control
```

The most important file in this structure is `hot_context.md`. It's an agent-curated summary of the relationship state (user profile, recent context, key preferences, active tasks, important facts) kept to around 500 words. After each agent session, a curation step runs: the agent reads the current hot\_context, looks at what just happened in the session, and updates the file with new learnings. This gets synced to a database cache (`relationship_context_cache` table), so chat mode can read it in ~1ms without touching the volume.

```
                     V3: hot_context lifecycle

  ┌──────────────────────────────────────────────────────────┐
  │                    Modal Volume /em/                      │
  │                                                          │
  │  memory/hot_context.md    profile/user.yaml   tools/     │
  │  memory/scratchpad.md     workspace/AGENTS.md  .claude/  │
  └────────────┬──────────────────────┬──────────────────────┘
               │                      │
       ┌───────┴───────┐      ┌───────┴───────┐
       │  Agent Mode   │      │  Chat Mode    │
       │               │      │               │
       │  Agent reads  │      │  Reads from   │
       │  /em/ with    │      │  DB cache     │
       │  bash (ls,    │      │  (~1ms)       │
       │  grep, cat)   │      │               │
       │       │       │      └───────────────┘
       │       ▼       │              ▲
       │  Does work,   │              │
       │  updates files│              │
       │       │       │              │
       │       ▼       │              │
       │ ┌───────────┐ │     ┌────────┴────────┐
       │ │ Curation  │ │     │  DB cache:      │
       │ │ step:     │─┼────▶│  relationship_  │
       │ │ update    │ │     │  context_cache  │
       │ │ hot_ctx   │ │     │  (sync on end)  │
       │ └───────────┘ │     └─────────────────┘
       └───────────────┘

  Pre-hydrate:  DB → Volume (before sandbox)
  Sandbox exec: Agent in /em/, tools via Gateway
  Post-sync:    Volume → DB (after sandbox, conflict detection)
```

The curation pattern is the key innovation of V3's memory approach. Instead of a scoring rubric (V1) or an LLM-managed entry list (V2), the agent itself decides what's important enough to surface in the global context. This is the "structured note-taking" pattern.

The lifecycle of an agent session follows this pattern: pre-hydrate (DB → Volume, load hot\_context, profile, AGENTS.md, track start versions), execute in sandboxes (agent operates in dedicated directory, no DB calls inside, tools via em-tool CLI → Gateway HTTPS) and finally sync with databases.

Concurrency was a real concern. What happens when multiple agent sessions run for the same relationship? Git worktrees. Each session gets its own branch and worktree under `/em/.worktrees/session-{'{id}'}/`. On completion, the branch merges back to main with conflict resolution. File-based locks prevent race conditions. It works and it's well-understood.

Conflict resolution between chat updates and agent sessions is handled by the curation step. If the DB version of hot\_context is newer than the start version (meaning chat updated it while the agent was running), the curation prompt includes both versions and the LLM naturally merges them.

* * *

## What coexists

These systems don't replace each other cleanly. They serve different purposes and coexist:

- **Memory V1/V2**: personal memory about the user. Facts, preferences, goals, life events. V1 for large stores with selective retrieval, V2 for simpler full-visibility scratchpads.
- **Knowledge Base** (OpenAI Vector Store): document retrieval. PDFs, FAQs, reference material. Classic RAG, separate from personal memory.
- **Hot Context** (V3): agent-curated relationship summary for fast chat reads. The "working memory" of the relationship.
- **Conversation Summaries**: incremental summarization at message count thresholds (200, 400, 600). Compaction for long-running relationships.

All memory ingestion is async and never blocks the user response. Context assembly is layered and pluggable. Each source of context (core prompt, memory, knowledge, tools, behaviors) is an independently enabling layer that runs in parallel.

* * *

## What's still open

1. **Consolidation and forgetting**: scratchpad entries accumulate over time. We don't have a great mechanism for merging related entries into higher-level summaries, and forgetting is arguably the hardest unsolved challenge in agent memory right now. That said, we intentionally kept the scratchpad open and extensible so developers can implement their own summarization and forgetting strategies on top of it. The primitives are there. The right policies will vary by use case.
2. **Fuzzy retrieval and temporal reasoning**: two ideas we think are promising but haven't implemented yet. Fuzzy retrieval would let the companion simulate imperfect memory ("Hmm, that rings a bell but I can't quite remember the details..."). Temporal reasoning would let the companion say things like "I know we talked about this previously and you might not have had the time to reflect on it" or "don't fret, we can come back to it another time." Both require reasoning about time intervals at different resolutions, from seconds to days.
3. **Cross-relationship search**: V3 is per-relationship, which is correct for privacy. But there are use cases where patterns across relationships (at the companion level) would be valuable. This might need pgvector at the V3 level.
4. **Checkpoint restore**: Modal's `snapshot_filesystem()` doesn't capture mounted volumes, so we can't restore agent sessions to previous checkpoints. Git-based checkpoints or S3 tarballs are options, but neither is great.

* * *

## Where I think this is going

I see the filesystem approach as the right abstraction for agent-mode memory. Models understand files natively, the developer experience is intuitive (just put an AGENTS.md in the right place), and the approach scales naturally. The agent loads what it needs rather than everything getting injected upfront.

For most companion use cases, V2 is probably what you want. A scratchpad that the LLM manages, injected fully into every turn, with developer-customizable ingestion prompts to shape what gets stored. It's simple, it's fast, and it gives full visibility into what the companion knows. If you're building a coaching bot, a customer support companion, a language tutor, or any conversational product where the user comes back regularly, V2 handles it well. You don't need a filesystem or an agent sandbox for that.

V3 and the hot\_context pattern become relevant when the companion needs to do real work: research tasks, multi-step tool use, file manipulation, things that require a sandboxed execution environment. In that world, hot\_context.md is the bridge. The agent curates it after each session, and chat mode reads it from a database cache in ~1ms. So you get the rich filesystem world of agent mode and the low-latency requirement of real-time chat working together.

The hardest remaining problem is taste. What should a companion remember? What should it surface, and when? These are product questions that require deep understanding of the relationship between user and companion, and getting the "what to remember" question right matters more than any retrieval algorithm. I think the ingestion prompt customization in V2 and the AGENTS.md in V3 are our best current answers, giving companion developers the tools to shape memory behavior for their specific use case. But there's a lot more to figure out here.

* * *

## References

1. Packer, C., Fang, V., Patil, S., Lin, K., Wooders, S., & Gonzalez, J. (2023). _MemGPT: Towards LLMs as Operating Systems_. [https://arxiv.org/pdf/2310.08560](https://arxiv.org/pdf/2310.08560)
2. Xu, X., Gu, X., Mao, R., Li, Y., Bai, Q., & Zhu, L. _Everything is Context: Agentic File System Abstraction for Context Engineering_. [https://ar5iv.labs.arxiv.org/html/2512.05470](https://ar5iv.labs.arxiv.org/html/2512.05470)
3. Anthropic. _Effective Context Engineering for AI Agents_. [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025)
4. Letta (formerly MemGPT): [https://www.letta.com/](https://www.letta.com/)
5. OpenAI Vector Stores API: [https://platform.openai.com/docs/assistants/tools/file-search](https://platform.openai.com/docs/assistants/tools/file-search)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="what-is-the-lost-in-the-middle-problem-and-how-does-it-affec.md">
<details>
<summary>What is the 'lost in the middle' problem and how does it affect AI agent memory?</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://mem0docs.xyz/task/blog/lost-in-the-middle-problem-ai-agent-memory/>

# What is the 'lost in the middle' problem and how does it affect AI agent memory?

The 'lost in the middle' problem is an empirically documented failure mode of large language models: when a long context window contains relevant information, models reliably attend to content near the beginning and end, and systematically overlook content in the middle. This has direct implications for any agent that relies on passing full conversation history to the model.

## The research finding

A 2023 study from Stanford ('Lost in the Middle: How Language Models Use Long Contexts') demonstrated that LLM performance on multi-document question answering degrades when the relevant passage is placed in the middle of a long context. Models with 20 documents performed best when the answer was in the first or last document, and worst when it was at position 10-11. The effect held across GPT-3.5, Claude, and other major models.

## Why this matters for agent memory

If your memory strategy is to concatenate conversation history and prepend it to the system prompt, you are creating exactly this failure condition at scale. A user who mentioned their security requirements 40 messages ago — now buried in the middle of a 60,000-token context — is less likely to have those requirements honored than if they had been mentioned in the last two messages. The most important context, established early in a relationship, ends up furthest from the model's attention.

## How targeted memory retrieval solves it

Memory retrieval replaces the 'dump everything in context' approach with selective injection. Instead of passing 60,000 tokens of history, you retrieve the 5-10 most relevant memory entries for the current query and inject them at the beginning of the prompt — the position with the highest model attention. Total memory context: 300-500 tokens, all in the high-attention zone.

```
# BAD: Full history — critical facts buried in the middle
messages = [\
    {"role": "system", "content": system_prompt},\
    *all_50_previous_turns,  # Critical fact is at turn 12\
    {"role": "user", "content": current_query},\
]

# GOOD: Retrieved memories injected at high-attention position
memories = memory.search(current_query, user_id=user_id, limit=5)
memory_text = "\n".join([m["memory"] for m in memories["results"]])

messages = [\
    {"role": "system", "content": f"{system_prompt}\n\nKnown facts:\n{memory_text}"},\
    *recent_session_turns,  # Only last few turns\
    {"role": "user", "content": current_query},\
]
```

## The compound benefit

Targeted retrieval solves both the lost-in-the-middle problem and the token cost problem simultaneously. You send fewer tokens (lower cost) in the right positions (higher reliability). Mem0's retrieval pipeline ranks memories by a combination of semantic similarity and recency, so the most contextually relevant facts occupy the high-attention positions in your prompt.

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