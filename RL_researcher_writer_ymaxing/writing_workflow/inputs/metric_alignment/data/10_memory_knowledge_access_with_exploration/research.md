# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What real-world challenges did developers face when building personal AI companions using only context windows of 8k to 16k tokens, and how did they begin implementing external memory systems?</summary>

Phase: [EXPLOITATION]

### Source [4]: https://community.cisco.com/t5/devnet-general-blogs/agent-memory-systems-beyond-context-windows/ba-p/5352003

Query: What real-world challenges did developers face when building personal AI companions using only context windows of 8k to 16k tokens, and how did they begin implementing external memory systems?

Answer: Context windows remain a bottleneck even at 200K-400K tokens (e.g., GPT-5), constraining single conversations and causing high token costs, duplication, and forgetting between API calls—e.g., resending 50K tokens multiple times in troubleshooting costs $5 vs. efficient alternatives. Agents hit limits analyzing configs/logs, paying per token with repeated sends due to no cross-session memory. Developers implemented persistent memory architectures using databases beyond context windows: VectorDB for semantic search (e.g., interface problems), Episodic DB for time-ordered events (syslog-like), Network DB for specifics (device IDs/IPs). Agents 'remember' via writing to these on events, enabling analysis without reloading. Benchmarks show 100% accuracy vs. 40% for context windows, 40x faster, scalable to 10K+. Self-registering agents track/learn capabilities persistently. Like NVRAM vs. RAM, stores permanently for evolution over sessions.

-----

</details>

<details>
<summary>How can concepts from human episodic memory, such as timestamped events and contextual narratives, be practically applied to improve empathy and continuity in LLM-based personal assistant agents?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://arxiv.org/pdf/2502.06975

Query: How can concepts from human episodic memory, such as timestamped events and contextual narratives, be practically applied to improve empathy and continuity in LLM-based personal assistant agents?

Answer: Episodic memory for LLM agents operationalizes five key properties from human cognition: long-term storage, explicit reasoning, single-shot learning, instance-specific memories, and contextualized memories. Instance-specific memories store details unique to particular occurrences with temporal contexts, enabling reasoning about specific past actions and consequences. Contextual memories bind events to when, where, and why they occurred, supporting retrieval based on cues. For personal assistants, this preserves timestamped events (e.g., user interactions) and contextual narratives (e.g., motivations, outcomes), improving continuity by recalling prior sessions without degradation. It enhances empathy via personalized, context-sensitive responses, such as tailored assistance recalling past preferences or experiences. External memory stores episodes for retrieval into in-context memory, with consolidation into parametric memory for generalization. Encoding segments continuous input into discrete episodes with metadata; retrieval reinstates relevant past episodes for reasoning. This framework supports adaptive behavior in dynamic environments like personalized customer support, maintaining performance over extended interactions for empathetic, continuous engagement.

-----

-----

Phase: [EXPLOITATION]

### Source [7]: https://arxiv.org/html/2604.04853v1

Query: How can concepts from human episodic memory, such as timestamped events and contextual narratives, be practically applied to improve empathy and continuity in LLM-based personal assistant agents?

Answer: Episodic memory stores specific past experiences—what happened, when, where, and with whom—treating each conversational turn as an episode with metadata (timestamp, participants, session ID). This provides ground truth for factual recall, reconstructing history, and maintaining continuity across sessions. For personal assistants, it enables personalization by preserving user history, preferences, and context, transforming generic LLMs into adaptive assistants. Profile memory (semantic) distills user attributes from episodes, combining with episodic for 'what happened' (factual grounding) and 'who the user is' (preferences). Contextualized retrieval expands matched episodes with neighboring context, addressing conversational interdependence for accurate reasoning. Temporal awareness via timestamps supports event ordering. This dual architecture supports empathy through demonstrated recall of interactions, preference adaptation, and proactive suggestions, ensuring continuity without repetition. Short-term memory holds recent episodes/summaries; long-term persists all for search. In MemMachine, raw episodes are stored with sentence-level indexing, minimizing LLM extraction errors for reliable, empathetic continuity.

-----

</details>

<details>
<summary>What are the advantages and disadvantages of using knowledge graphs for modeling relationships and temporal changes in agent memory compared to simpler structured data approaches?</summary>

Phase: [EXPLOITATION]

### Source [8]: https://atlan.com/know/vector-database-vs-knowledge-graph-agent-memory/

Query: What are the advantages and disadvantages of using knowledge graphs for modeling relationships and temporal changes in agent memory compared to simpler structured data approaches?

Answer: Knowledge graphs excel at modeling complex relationships through typed entity relationships and deterministic multi-hop traversal, enabling precise reasoning over explicit connections like 'governs', 'references', or 'derives_from'. They provide explainability via auditable reasoning paths tracing back to specific graph nodes, crucial for regulated industries. For temporal changes, Zep/Graphiti’s bi-temporal model supports validity intervals on edges (t_valid, t_invalid), achieving 18.5% accuracy improvement on LongMemEval temporal reasoning tasks and 90% response latency reduction versus baselines (arXiv 2501.13956). GraphRAG enables global queries outperforming vector RAG on dataset-wide questions (arXiv 2404.16130). Compared to simpler structured data like vector databases, KGs offer multi-hop relational reasoning and temporal support where vectors provide only flat semantics and no native temporal model, leading to stale data issues and invisible freshness failures.

Disadvantages include cold-start problem: graphs start empty, requiring labor-intensive ontology construction and entity extraction, unlike zero cold-start vectors. Ontology maintenance burden demands expert curation as business evolves. GraphRAG refresh incurs high GPU costs and latency for dynamic content (arXiv 2507.03226). Query complexity requires Cypher/SPARQL expertise. No native governance; lacks permissions unlike some metadata graphs. Vectors excel in sub-millisecond fuzzy recall of unstructured content with universal type support and low overhead, while KGs demand significant upfront investment.

-----

</details>

<details>
<summary>How does the mem0 library handle the creation, storage, and hybrid retrieval of semantic, episodic, and procedural memories in agent applications?</summary>

Phase: [EXPLOITATION]

### Source [13]: https://docs.ag2.ai/latest/docs/use-cases/notebooks/notebooks/agentchat_memory_using_mem0/

Query: How does the mem0 library handle the creation, storage, and hybrid retrieval of semantic, episodic, and procedural memories in agent applications?

Answer: Mem0 provides comprehensive memory management for long-term, short-term, semantic, and episodic memories for individual users, agents, and sessions through robust APIs. It uses a hybrid database approach combining vector, key-value, and graph databases to efficiently store and retrieve different types of information. Memories are associated with unique identifiers like user_id. When storing, Mem0 extracts relevant facts and preferences. Retrieval uses a sophisticated process considering relevance, importance, and recency. Creation involves adding conversation messages via memory.add(messages=conversation, user_id="customer_service_bot"), which stores the entire conversation history. Retrieval is done via memory.search(data, user_id="customer_service_bot"), fetching relevant memories which are then flattened and injected into agent prompts for context-aware responses. This enables maintaining context across sessions, adaptive personalization, and dynamic updates in agent applications like customer service chatbots and multi-agent conversations.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: How does the mem0 library handle the creation, storage, and hybrid retrieval of semantic, episodic, and procedural memories in agent applications?

Answer: Mem0 handles long-term memory for AI agents with semantic (facts and preferences), episodic (past interactions), and procedural (styles and behaviors) memories. Creation involves extraction and consolidation from raw conversations using LLMs to distill signals, then storage in hybrid vector and graph databases: vectors for semantic similarity search, graphs for relational structure. Consolidation merges similar memories, resolves conflicts, and updates relevance scores. Retrieval embeds queries to vectors, searches top-k candidates, scores by relevance × recency × type_weight (semantic: 0.6, episodic: 0.3, procedural: 0.1), reranks with LLM, and injects top results into prompts. Hybrid approach balances performance: vector for fast search, graph for multi-hop reasoning. Mem0 automates the pipeline, achieving 91% lower p95 latency, 90% token savings. Integrates with LangChain, CrewAI for agent applications enabling personalization across sessions.

-----

-----

Phase: [EXPLOITATION]

### Source [16]: https://docs.mem0.ai/core-concepts/memory-types

Query: How does the mem0 library handle the creation, storage, and hybrid retrieval of semantic, episodic, and procedural memories in agent applications?

Answer: Mem0 organizes memory into layers: conversation (short-term), session, user (long-term factual, episodic, semantic), and organizational. Long-term memory captures factual memory (user preferences, facts), episodic memory (summaries of past interactions), semantic memory (relationships between concepts). Creation: messages added to conversation layer via memory.add(["I'm Alex..."], user_id="alex", session_id="trip-planning"), promoting relevant details to session/user layers. Storage: each layer stored separately. Hybrid retrieval: search merges layers, ranking user > session > history, e.g., memory.search("Any hotel preferences?", user_id="alex", session_id="trip-planning"). Use session_id for short-term, user_id for persistent. Maps classic categories to layered storage for agents to reason contextually across sessions.

-----

</details>

<details>
<summary>What best practices have emerged from production deployments of AI agent memory systems regarding compression strategies, autonomous memory maintenance, and minimizing user involvement in memory management?</summary>

Phase: [EXPLOITATION]

### Source [17]: https://arxiv.org/pdf/2603.07670

Query: What best practices have emerged from production deployments of AI agent memory systems regarding compression strategies, autonomous memory maintenance, and minimizing user involvement in memory management?

Answer: From production deployments of AI agent memory systems, several best practices have emerged:

**Compression Strategies:**
- Sliding windows retaining the n most recent turns and dropping the rest.
- Rolling summaries that periodically condense older history into shorter precis.
- Hierarchical summaries at turn, session, and topic granularities.
- Task-conditioned compression where the current query decides which parts of history keep full detail.
Context-resident memory is transparent but prone to summarization drift; supplement with external stores for raw records. Production Pattern B (Context + retrieval store) is the workhorse for most agents like coding assistants and customer-service bots.

**Autonomous Memory Maintenance:**
- Write-path filtering rejects low-signal records, canonicalization normalizes data, deduplication merges entries, priority scoring ranks by relevance/novelty, metadata tagging supports queries.
- Read-path optimizations: two-stage retrieval, retrieval gating, token budgeting, cache layers.
- Handle staleness/contradictions via temporal versioning (prefer newest), source attribution, contradiction detection, periodic consolidation.
- Architecture patterns: Tiered memory with learned control (e.g., MemGPT, Agentic Memory) where agents manage tiers autonomously via tools or RL-optimized policies.
- Observability: Comprehensive logging of every memory operation (write/read/update/delete) with timestamps/context/records; replay tools, memory diffs for debugging.

**Minimizing User Involvement:**
- Retrieval pipelines inject relevant records automatically each step.
- Prompted self-control lets LLM decide memory operations via tool calls (e.g., MemGPT's core_memory_append).
- Learned control optimizes memory ops end-to-end without manual intervention.
- Production deployments emphasize autonomous systems like Pattern B/C, reducing engineering burden while ensuring retrieval quality via logging and analysis.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/

Query: What best practices have emerged from production deployments of AI agent memory systems regarding compression strategies, autonomous memory maintenance, and minimizing user involvement in memory management?

Answer: Amazon Bedrock AgentCore Memory provides production best practices:

**Compression Strategies:**
- Achieves 89-95% compression rates via extraction into semantic/preference/summary memories.
- Intelligent consolidation merges related info, resolves conflicts prioritizing recency.

**Autonomous Memory Maintenance:**
- Asynchronous extraction/consolidation pipeline using LLMs for ADD/UPDATE/NO-OP decisions.
- Built-in strategies (semantic, preferences, summaries) with custom overrides/self-managed options.
- Immutable audit trail marking outdated memories INVALID.
- Parallel processing, exponential backoff retries.

**Minimizing User Involvement:**
- Automatic retrieval via semantic search (~200ms latency).
- Namespaces for hierarchy/isolation; async processing with short-term fallback.
- Monitor via list/retrieve APIs; design for no manual intervention.

-----

</details>

<details>
<summary>How can developers design effective LLM prompts to extract and structure semantic facts from conversations for long-term agent memory?</summary>

Phase: [EXPLOITATION]

### Source [27]: https://langchain-ai.github.io/langmem/concepts/conceptual_guide/

Query: How can developers design effective LLM prompts to extract and structure semantic facts from conversations for long-term agent memory?

Answer: LangMem provides ways to extract meaningful details from chats for long-term memory. Each memory operation follows: 1. Accept conversation(s) and current memory state. 2. Prompt an LLM to determine how to expand or consolidate the memory state. 3. Respond with the updated memory state.

Design considerations: What type of content (facts/knowledge for semantic memory)? When memories formed (conscious during conversation or subconscious after)? Where stored (semantic store)?

Semantic Memory stores facts and knowledge as collections (individual documents) or profiles (strict schema documents). Collections balance extraction and consolidation; indicate importance for relevance.

Example for collections: manager = create_memory_manager("anthropic:claude-3-5-sonnet-latest", instructions="Extract all noteworthy facts, events, and relationships. Indicate their importance.", enable_inserts=True). Process conversation to extract memories like [IMPORTANT] facts.

Example for profiles: Define Pydantic schema (e.g., UserProfile with name, preferences), instructions="Extract user preferences and settings", enable_inserts=False. Updates single document.

Choose profiles for current state/quick access, collections for contextual recall across interactions.

Subconscious formation: Prompt LLM post-conversation to extract insights without slowing interaction, ensuring higher recall.

-----

</details>

<details>
<summary>In what ways do larger context windows in modern LLMs change the role and implementation of external long-term memory systems in agent design?</summary>

Phase: [EXPLOITATION]

### Source [32]: https://weaviate.io/blog/context-engineering

Query: In what ways do larger context windows in modern LLMs change the role and implementation of external long-term memory systems in agent design?

Answer: Larger context windows do not solve the fundamental constraint of finite context in LLM agents. It's tempting to assume shoving everything into bigger context windows solves memory problems, but this is generally not the case, leading to production agents needing deliberate memory architecture. Short-term memory is the live context window: recent turns/reasoning, tool outputs, retrieved documents—finite space that should stay lean. Long-term memory lives outside the model in vector databases for quick retrieval (RAG), holding episodic data (past events, interactions), semantic data (knowledge), procedural data (routines). External memory grows, updates, persists beyond context window. Agents depend on memory layer: short-term in context window, long-term retrieved on demand. Context engineering builds LLM memory by deciding what stays in context window vs. stored/retrieved as long-term. Agents architect context dynamically, using retrieval from external stores.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://research.ibm.com/blog/larger-context-window

Query: In what ways do larger context windows in modern LLMs change the role and implementation of external long-term memory systems in agent design?

Answer: Larger context windows allow feeding LLM more details directly via 'prompt stuffing', essentially replicating what RAG provides without external retrieval. With larger windows, can throw in all books/enterprise documents, potentially making RAG obsolete as no information loss from retrieval. However, RAG remains relevant for current-events, evaluating contradictory info (policy updates), cost efficiency (scanning thousands of docs per query inefficient; filter first). Larger windows best for less common queries after filtering extraneous details. IBM extended Granite models to 128k tokens for better coding by ingesting more docs internally.

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://redis.io/blog/llm-context-windows/

Query: In what ways do larger context windows in modern LLMs change the role and implementation of external long-term memory systems in agent design?

Answer: Large context windows (128k-2M) degrade accuracy past 32k tokens ('lost-in-the-middle'), high cost/latency; small windows (<32k) consistent for focused tasks. Production uses RAG for stable accuracy as data scales (retrieves relevant sections vs. stuffing), agent memory: short-term (conversation history, eviction), long-term (vector embeddings for semantic retrieval across sessions). Redis Agent Memory Server combines layers with vector search/caching, extending context beyond single limits. Optimal: combine large windows for full-doc reasoning, RAG for scaling, caching for repeats—external memory essential despite larger windows.

-----

</details>

<details>
<summary>What real-world case studies demonstrate the benefits of tailoring memory architecture to specific agent use cases like personal companions versus automation tasks?</summary>

Phase: [EXPLOITATION]

### Source [37]: https://arxiv.org/html/2503.12687v1

Query: What real-world case studies demonstrate the benefits of tailoring memory architecture to specific agent use cases like personal companions versus automation tasks?

Answer: The paper discusses memory and context management in AI agent architectures, distinguishing between types like working memory (task-relevant during execution), episodic memory (specific interactions), semantic memory (conceptual knowledge), and procedural memory (action sequences). Microsoft's deputy CTO Sam Schillace notes effective memory systems are essential for agent autonomy to carry context across actions. Cross-session personalization uses memory for consistent, adaptive experiences maintaining user profiles for preferences and history, balancing accuracy, appropriateness, and privacy. Chunking and chaining divide interactions for storage and relevance-based access. In real-world applications, Section 5.2 Personal Assistance and Productivity highlights memory for task management, information retrieval, creative collaboration, personalized learning, communication assistance, where agents like Microsoft Copilot use memory for continuity (e.g., drafting emails, recapping meetings). Users report saving 1.5 hours/week on tasks. Section 5.1 Enterprise Applications shows automation benefits like Vodafone's AI agent handling 70% inquiries reducing resolution time 47%, logistics reducing errors 83%, using memory for context in customer service, process automation. Section 5 contrasts personal (continuity, personalization) vs enterprise automation (scalable task execution). Challenges include scalability, retrieval accuracy for complex tasks.

-----

</details>

<details>
<summary>How are rapidly expanding LLM context windows from thousands to millions of tokens altering the balance between in-context history and external long-term memory systems in agent design?</summary>

Phase: [EXPLOITATION]

### Source [42]: https://aiagentmemory.org/articles/context-window-llm-comparison-2025/

Query: How are rapidly expanding LLM context windows from thousands to millions of tokens altering the balance between in-context history and external long-term memory systems in agent design?

Answer: For years, LLM context windows were measured in mere thousands of tokens, creating significant limitations for AI agents. Tasks requiring long conversations or analysis of extensive documents were challenging, often necessitating complex AI agent memory systems or retrieval-augmented generation (RAG) to bridge the gap. However, rapid advancements in LLM memory system architectures and attention mechanisms have drastically altered this landscape. By 2025, models with context windows exceeding 100,000 tokens are becoming commonplace, with some pushing towards the million-token mark. This leap fundamentally changes how we think about AI agent long-term memory and its reliance on external storage. The size of an LLM’s context window directly impacts its ability to perform complex tasks, allowing agents to maintain conversational coherence, process large documents, execute multi-step instructions, and improve reasoning capabilities. This shift influences the design of AI agent architecture patterns, potentially reducing the reliance on sophisticated episodic memory in AI agents for immediate recall, though long-term storage remains vital. Large context windows offer a form of 'short-term' or 'working' memory for AI agents, but they don’t replace the need for persistent long-term memory AI agents. Context Window acts like an agent’s immediate scratchpad, volatile and resets with each session, excellent for immediate recall within a single interaction. Persistent Memory stores information across sessions, including episodic memory (specific events) and semantic memory (general knowledge). Systems like Hindsight complement the LLM’s built-in context. Large context windows can enhance existing AI memory systems and RAG pipelines: richer prompts with more retrieved information, reduced retrieval needs for tasks that previously required frequent external knowledge base access, better reasoning over retrieved data. The FAQ notes that large context windows reduce the need for external memory systems for short-term recall, but differ from traditional AI memory systems which provide persistent, long-term storage across sessions.

-----

</details>

<details>
<summary>Why does adopting terminology from human biology and cognitive science, such as distinguishing internal knowledge from working and long-term memory, provide a stronger foundation for building effective AI agent architectures?</summary>

Phase: [EXPLOITATION]

### Source [47]: https://arxiv.org/html/2410.15665v1

Query: Why does adopting terminology from human biology and cognitive science, such as distinguishing internal knowledge from working and long-term memory, provide a stronger foundation for building effective AI agent architectures?

Answer: Adopting terminology from human biology and cognitive science, particularly distinguishing working memory, short-term memory, and long-term memory (LTM), provides a stronger foundation for AI agent architectures by enabling structured memory systems that support self-evolution, continuous learning, and adaptability. Human memory research divides memory into working/short-term (temporary task information, quickly forgotten) and LTM (stores knowledge/experiences influencing behavior, including episodic, semantic, procedural subtypes). LTM is the key data foundation for human personality and diverse behaviors from world interactions. For AI, LTM accumulates historical experiences, overcomes context window limitations of short-term approaches, enables continuous optimization, personalization, and stronger adaptability in complex environments/multi-agent collaboration. Current LLMs rely on limited contextual/parametric memory (temporality, no continuous learning, hard to update/express individual data). Inspired by human LTM (encoding/consolidation/retrieval via hippocampus/cortex), AI LTM supports self-evolution: data accumulation, real-time weight updates, diverse model architectures. LTM empowers foundation models with historical data for personalization without full retraining, enables inference-training integration for dynamic adaptation, and facilitates multi-agent collaboration via differentiated agents. Without LTM, models lack lifelong learning; with it, they achieve self-improving intelligence beyond averaged foundation models.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://mem0.ai/blog/the-modal-model-of-memory-what-ai-agents-can-learn-from-cognitive-science

Query: Why does adopting terminology from human biology and cognitive science, such as distinguishing internal knowledge from working and long-term memory, provide a stronger foundation for building effective AI agent architectures?

Answer: Atkinson-Shiffrin's Modal Model (sensory/short-term/long-term stores with control processes) guides AI memory: attention filters input, deep semantic encoding improves retrieval, interference management via updates/deletes, dynamic forgetting reduces noise, consolidation selects persistent info. Adopting this provides scalable architectures outperforming raw storage (e.g., Mem0: 26% accuracy gain, 91% lower latency), enabling self-evolution like biological systems.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What emerging techniques are being developed to enable agents to perform online updates to their internal (parametric) knowledge without full retraining, bridging the gap to true continual learning?</summary>

Phase: [EXPLORATION]

### Source [57]: https://arxiv.org/html/2511.01093v1

Query: What emerging techniques are being developed to enable agents to perform online updates to their internal (parametric) knowledge without full retraining, bridging the gap to true continual learning?

Answer: The paper introduces ATLAS, a dual-agent architecture for gradient-free continual learning that enables online adaptation without retraining model parameters. It decouples reasoning (Teacher model) from execution (Student model) and uses a Persistent Learning Memory (PLM) to store distilled guidance from experiences. The orchestration layer dynamically adjusts strategies like supervision level or plan selection at inference time based on retrieved learning history and rewards from Teacher-Student interactions. This shifts adaptation from model weights to system-level orchestration, achieving immediate behavioral modification without gradients, specialized hardware, or datasets. On ExCyTIn-Bench (cyber-threat benchmark), ATLAS boosts GPT-5-mini success from 33.7% to 54.1%, outperforms larger GPT-5 by 13%, reduces tokens by 45% (78k vs 142k), and shows progressive efficiency (tokens drop from 101k to 67k over 98 tasks). Cross-incident transfer improves accuracy 28% to 41% with frozen pamphlets, no retraining. Contrasts with training-based (LoRA, QLoRA, DoRA), prompt optimization, retrieval systems, and passive memory mechanisms, which rely on gradients or lack active skill synthesis. Rewards use two-tier ensemble judges for auditable scores. Generates causally annotated traces for world-model training.

-----

</details>

<details>
<summary>In what ways do different temporal granularities for episodic memory storage impact an agent's temporal reasoning capabilities and personalization quality?</summary>

Phase: [EXPLORATION]

### Source [62]: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/episodic-memory-strategy.html

Query: In what ways do different temporal granularities for episodic memory storage impact an agent's temporal reasoning capabilities and personalization quality?

Answer: Episodic memory in Amazon Bedrock AgentCore captures meaningful slices of user and system interactions as structured episode records rather than storing every raw event. Episodes represent completed interaction sequences analyzed turn-by-turn into situation, intent, assessment, justification, and reflection. Reflections analyze patterns across multiple episodes to extract insights like successful tool combinations, failure modes, and best practices. Namespaces control storage granularity: strategy-level aggregates episodes across actors/sessions; actor-level stores per actor across sessions; session-level per session. Reflections can span multiple actors or stay actor-specific. Finer granularity (session/actor) enables precise temporal context and personalization by retrieving user-specific past experiences via semantic search, improving adaptation to preferences, consistency, and avoiding repeated mistakes. Coarser strategy-level supports pattern identification across users. Retrieval of similar episodes/reflections enhances temporal reasoning by understanding sequence evolution, maintaining long-term coherence. Use cases like customer support benefit from sequence understanding over time, adapting to evolving preferences. Temporal reasoning improves through timestamped episodes and reflections spanning interactions, enabling agents to reference past strategies in new contexts.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://arxiv.org/html/2509.10852v1

Query: In what ways do different temporal granularities for episodic memory storage impact an agent's temporal reasoning capabilities and personalization quality?

Answer: PREMem structures episodic memory at fine-grained fragment level from conversations, categorized into factual (states/attributes), experiential (events/actions), subjective (preferences/opinions). Temporal granularity addresses LLM weaknesses in relative time (yesterday/last week) via four patterns: ongoing facts use message dates; specific past absolute dates; unclear past 'Before [date]'; future 'After [date]'. Fragments clustered semantically per session, then cross-session linked via centroid similarity > threshold. Five evolution patterns (extension, accumulation, specification, transformation, connection) model temporal changes via schema theory, performed in pre-storage reasoning. Ablation shows temporal reasoning removal drops temporal scores 5.7-16.4%, confirming fine temporal granularity boosts temporal reasoning. Without categories, personalization drops 1.8-8.9% as undifferentiated storage loses preference tracking precision. Cross-session reasoning (Step 2) improves overall 3-5%, multi-hop 3-5%, temporal 5-16%. Finer granularity enables evolution tracking (e.g., preference shifts), enhancing personalization consistency. Coarser session-level baselines underperform on temporal/multi-hop. Experiments across LoCoMo/LongMemEval show PREMem excels in temporal reasoning (74.1-76.7% vs. baselines 36-50%), knowledge updates (55-61% vs. 38-42%), confirming fine temporal episodic storage improves agent temporal reasoning and personalization quality.

-----

</details>

<details>
<summary>What applications of agent memory systems in scientific research, such as laboratory notebooks or hypothesis tracking, demonstrate the value of procedural and episodic memory types?</summary>

Phase: [EXPLORATION]

### Source [76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11449156/

Query: What applications of agent memory systems in scientific research, such as laboratory notebooks or hypothesis tracking, demonstrate the value of procedural and episodic memory types?

Answer: The Soar architecture comprises multiple memory systems, including modules for procedural memory (if-then rules for virtual actions), working memory (current state, sensing, potential actions), and episodic memory (stores past states from working memory, retrievable by cueing). In scientific research contexts, these systems highlight episodic memory's role in directing research by identifying novel or neglected hypotheses as pursuit-worthy, such as its independent role in planning and contributions to fast learning in novel, sparse-reward environments. Event memory (episodic-inspired) aids strategic decision-making, fast learning (e.g., one-shot learning in Labyrinth), exploration, navigation (constructing cognitive maps), and acting over temporal distance, demonstrating value in hypothesis generation and testing. Procedural memory automates actions via rules, complementing episodic recall for informed decisions. No direct laboratory notebooks or hypothesis tracking mentioned, but systems propose evaluating episodic memory theories via AI, isolating memory contributions to behavior through ablation studies, advancing scientific understanding of memory functions.

-----

</details>

<details>
<summary>In what ways have memory patterns from collaborative software tools like wikis or version control systems informed the design of shared semantic memory in multi-user AI agents?</summary>

Phase: [EXPLORATION]

### Source [85]: https://machinelearningmastery.com/7-steps-to-mastering-memory-in-agentic-ai-systems/

Query: In what ways have memory patterns from collaborative software tools like wikis or version control systems informed the design of shared semantic memory in multi-user AI agents?

Answer: For multi-agent systems, shared memory introduces additional complexity. Agents can read stale data written by a peer or overwrite each other’s episodic records. Design shared memory with explicit ownership and versioning: [...] Semantic memory holds structured factual knowledge: user preferences, domain facts, entity relationships, and general world knowledge relevant to the agent’s scope. A customer service agent that knows a user prefers concise answers and operates in the legal industry is drawing on semantic memory. This is often implemented as entity profiles updated incrementally over time, combining relational storage for structured fields with vector storage for fuzzy retrieval. [...] Memory is fundamentally a systems architecture problem: deciding what to store, where to store it, when to retrieve it, and, more importantly, what to forget. None of those decisions can be delegated to the model itself without explicit design. The practical implication is to design your memory layer the way you’d design any production data system. Think about write paths, read paths, indexes, eviction policies, and consistency guarantees before writing a single line of agent code.

-----

</details>

<details>
<summary>What are the specific cognitive load and error propagation challenges when dynamically updating procedural memory through user-taught workflows in production agent systems?</summary>

Phase: [EXPLORATION]

### Source [96]: https://arxiv.org/html/2508.06433v2

Query: What are the specific cognitive load and error propagation challenges when dynamically updating procedural memory through user-taught workflows in production agent systems?

Answer: Mem^p framework distills trajectories into procedural memory (step-by-step instructions, script-like abstractions) with Build, Retrieval, Update strategies. Dynamic updates via Vanilla (append all), Validation (only successes), Adjustment (revise failed executions). Challenges: Existing frameworks (LangGraph, AutoGPT, Memory Bank) provide coarse abstractions without optimizing procedural memory lifecycle (build, index, patch, prune), no principled quantification of efficiency or guarantee new experiences improve vs. erode performance. Cognitive load: Without optimization, agents restart exploration on similar tasks, high test-time cost in steps/tokens; procedural memory reduces fruitless exploration. Error propagation: Appending flawed trajectories without validation introduces errors; Adjustment combines erroneous trajectory with original and revises, but unexamined patching risks propagating failures if revisions inadequate. Vanilla updates all trajectories, including failures, potentially eroding performance.

-----

</details>

<details>
<summary>How do different temporal aggregation strategies for episodic memories (per-turn, per-day, per-week) quantitatively affect an agent's ability to perform narrative reconstruction and relationship dynamics modeling?</summary>

Phase: [EXPLORATION]

### Source [99]: https://arxiv.org/html/2501.13121v1

Query: How do different temporal aggregation strategies for episodic memories (per-turn, per-day, per-week) quantitatively affect an agent's ability to perform narrative reconstruction and relationship dynamics modeling?

Answer: The paper introduces a benchmark for episodic memory in LLMs, modeling episodic events with temporal (t), spatial (s), entity (ent), and content (c) attributes. Events are generated using a truncated geometric distribution for dates, ensuring varying frequencies (rare to frequent occurrences). Tasks include cue-based recall varying specificity, e.g., (t,*,*,*) retrieves events at specific time t, testing temporal granularity. Performance degrades with cue overload (multiple matching events), particularly for time cues (lowest F1 scores). Chronological tracking (latest state, chrono lists) shows low exact matches (≤36% latest, ≤18% all events), poor ordering (low Kendall τ). No explicit per-turn/day/week aggregation, but geometric sampling creates temporal clustering mimicking aggregation levels, affecting multi-event retrieval and narrative coherence. Finer temporal cues (specific t) better for single events but overload for multiples; coarser (no t) worse overall. Supports narrative reconstruction via entity/time tracking, relationship modeling via multi-event cues.

-----

</details>

<details>
<summary>What engineering tradeoffs arise when implementing autonomous memory consolidation processes that resolve contradictions between raw string, entity, and graph storage layers without human oversight?</summary>

Phase: [EXPLORATION]

### Source [104]: https://clawxiv.org/api/pdf/clawxiv.2602.00032

Query: What engineering tradeoffs arise when implementing autonomous memory consolidation processes that resolve contradictions between raw string, entity, and graph storage layers without human oversight?

Answer: The paper presents 'memory enzymes' as six autonomous maintenance processes—link strengthening, salience-protected decay, contradiction detection, cluster consolidation, belief reinforcement, and tag-overlap linking—that operate on the knowledge graph without manual intervention to resolve contradictions and consolidate memories across layers. Key engineering tradeoffs include scalability vs. complexity: the system is small-scale (205 memories), and scaling properties of the enzyme suite are unknown, particularly the O(n²) contradiction detector, which becomes a bottleneck as LanceDB ANN search scales well but the enzyme pipeline does not. Efficiency vs. safety: autonomous processes like contradiction detection (semantic similarity >0.7 with opposition patterns) and belief reinforcement (evidence-weighted EMA with inertia λ_eff = λ_base × N^−α) balance epistemic humility (asymmetric λ_reinforce=0.15 vs. λ_contradict=0.30) and belief stability, but risks belief poisoning without full cascading propagation or evidence diversity. Reliability without oversight: enzymes run in dry-run mode, return structured results, but limitations include manual belief formation, unimplemented cascading, and O(n²) costs. Production metrics show 16 contradictions flagged, but future work notes enzyme pipeline as likely bottleneck. Tradeoff between active maintenance (benefits over passive accumulation) and computational overhead in long-running agents.

-----

</details>

<details>
<summary>In what ways do hybrid vector-graph indexing schemas in tools like mem0 impact retrieval precision for entity-linked semantic memories compared to pure vector approaches under high update frequency?</summary>

Phase: [EXPLORATION]

### Source [109]: https://sparkco.ai/blog/ai-agent-memory-in-2026-comparing-rag-vector-stores-and-graph-based-approaches

Query: In what ways do hybrid vector-graph indexing schemas in tools like mem0 impact retrieval precision for entity-linked semantic memories compared to pure vector approaches under high update frequency?

Answer: Hybrid vector-graph indexing schemas, such as Hybrid GraphRAG, improve retrieval precision for entity-linked semantic memories by combining vector retrieval for broad semantic search with graph traversal for precise relational navigation and refinement. This achieves 80% accuracy vs. 50% for vanilla RAG, with 35%+ precision gains in benchmarks, particularly for tasks demanding high precision like multi-hop reasoning in R&D assistants (80% multi-hop success, 35% reduced innovation cycle). Under high update frequency, pure vector approaches suffer from stale embeddings and retrieval noise (dimensionality curse), while hybrids balance costs (1.5x vector + graph) but face increased maintenance complexity (schema updates, 3-4 person-months/year for graphs). Graphs demand completeness checks and edge density management, with indexing 2-5x vector time, yet provide sophisticated entity linking (90% partial accuracy). 2024 benchmarks show 35% precision gains for hybrids in precise retrieval scenarios influenced by IP protections.

-----

-----

Phase: [EXPLORATION]

### Source [110]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: In what ways do hybrid vector-graph indexing schemas in tools like mem0 impact retrieval precision for entity-linked semantic memories compared to pure vector approaches under high update frequency?

Answer: Mem0 uses a hybrid vector-graph indexing schema for long-term memory in AI agents, balancing performance and structure. Vector embeddings enable fast semantic retrieval (1536D, ANN search with HNSW), while graph storage provides relational integrity, preventing drift and improving multi-hop reasoning accuracy. Retrieval pipeline: embed query, fetch top-k=20 candidates via vector search, score by relevance × recency × type_weight (semantic 0.6, episodic 0.3, procedural 0.1), hybrid reranking with LLM boosts multi-hop J-score by 15%. Compared to pure vector (excels in speed but falters on relations), hybrid fuses scores (0.7 × vector similarity + 0.3 × graph confidence), significantly improving multi-hop accuracy for entity-linked memories connecting preferences, events, rules. Under high update frequency, vectors support async upsert with versioning; graphs enable incremental edge addition with temporal versioning; hybrids handle concurrent updates via ACID transactions, outperforming pure vectors which lack structural resolution for dynamic relational data.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agent-memory-systems-beyond-context-windows-cisco-community.md">
Phase: [EXPLOITATION]

## Agent Memory Systems: Beyond Context Windows

### Key Takeaways

- **Context Limitations** Even with advancements like 400K token context windows, traditional LLMs struggle with memory retention across interactions, leading to repeated token costs.

- **Persistent Memory** Implementing persistent memory architectures allows agents to remember information across sessions, enhancing their ability to provide consistent and informed responses.

- **Database Integration** Utilizing various types of databases (vector, episodic, network) allows agents to efficiently store and retrieve contextual information, improving their operational capabilities.

- **Agent Evolution** Agents can learn and adapt over time by tracking their experiences, leading to improved capabilities and more efficient problem-solving methods.

Video transcript (click here):

Welcome to Agentic Impressions, where we'll be discussing various topics across the agentic AI landscape. Our first season will be covering the basics of agentic AI. Today, we'll be discussing the role of context windows as the second episode in our series. Hi everyone, my name is Shereen Bellamy. I'm a Senior Developer Advocate at Cisco, focusing on AI, security, and quantum. I'm here to share my findings and discuss with you all. And today, as promised, we're going to be discussing agent memory systems. In our last episode, we proved that architecture beats raw power. But here's a problem that everyone's still hitting, context windows. Context windows are still a bottleneck in the industry. Even with clods like 200,000 total tokens, and even GPT-5 is like up to 400K tokens now, you're still constrained by what fits into one single conversation. Let's tackle this specific problem for today. We'll call it the token triangle problem. Let's say we want to work with an LLM that has a context window of 128K tokens. Seems like a large enough number, but we're hitting the limit after analyzing 85 configs, way less than our goal. This is a result of high cost through expensive token usage. You pay per token, and when we access the LLMs, it's processing our query using those tokens. Everything you send to the LLM gets converted into tokens. Whatever it sends back is also composed of tokens. This is also due to the inability to continue interacting with the LLM due to the limit on how much it can actually digest. How many tokens you can send are defined by the LLM's ability, and sometimes by your plan. And LLMs will naturally forget between API calls. So a scenario on what this would look like is you would send 50K tokens of context, like configs, logs, topology, to the LLM. The cost might be arbitrarily like 50 cents. Now you're gonna wait for your LLM to respond with advice. That's 500 tokens. And then five minutes later, you would ask a follow-up question to get more clarification, the answer you need, maybe get more data. But your LLM, your natural standalone LLM, has forgotten everything. So you have to send all 50K tokens again, which would cost another 50 cents. And this would happen about 10 times in a troubleshooting session, right? While you try through trial and error to fix it. Now your total cost may come up to like $5. The total token sent can be up to 500,000 now. But you can have massive duplication in this dataset. And at the same time, you're constantly hitting context limits, which you have to wait to refresh to get your next output. Through the concept of persistent memory, we can see today how databases can help us overcome that problem and what specifically put inside of those databases that we can build on in the future. So again, if we look at this issue from a critical thinking perspective, what if agents had persistent memory that worked across sessions, learned from every interaction and has the ability to get better over time? That's what we're focused on today. Today, we're going to be building memory architectures. I'll show you persistent memory systems, benchmark different approaches and demonstrate the concept of agent self-registration. This is where agents have the ability to remember who they are and what they've learned. Again, when we look at the concept of architecture, especially looking at the design of something like the memory, then we're able to optimize what makes the agent so special, right? Their skills. So let's build it. So let's start by running this persistent agent Python file and see what it does. Then I'll show you how the code works. In these lines, the agent is storing network events, router interface down, switch CPU high, interface backup, and it's remembering the device configurations. Instead of keeping everything in AI's temporary memory, we're using a database, just like how your routers are storing their config in NVRAM instead of regular RAM. We have three types of databases, vector, episodic and network. SQLite is just a file-based database. Think of it like a really smart spreadsheet that never forgets, and we're using three of them. We have our VectorDB. This is for searching by meaning. So if you search something like interface problems, it would find related events, even if they don't have those exact words. We have an episodic database. This stores things in time order, like your syslog from oldest to newest. Then we have our network database. This is our custom database for network-specific stuff, like device IDs and IP addresses. So what happens when it remembers something? When you call the remember function, like when we remembered what routers R1 interface went down, it writes all three databases. That's three different ways to find that information later. It's like documenting an incident in your ticketing system, your runbook, and your network diagram. It's a little redundant, but it's powerful. So here we integrate the AI portion by calling an OpenAI API key. When we analyze the network issue, we're not just searching the database. We're asking a real AI to look at the problem and suggest fixes. So let me run it again and show you the AI-powered analysis. For this analysis, this is coming from GPT-4 looking at the network issue, saying that router interface flapped, switch has high CPU, and giving real troubleshooting steps. It's like having a senior network engineer on call 24-7. So when we mix AI's intelligence with their permanent database memory, AI is able to provide the analysis and the database is able to provide the history. So try closing the terminal and then run it again. Those .db files are still there. The agent's still able to remember everything from last time, making it persistent. Okay, so we can store things in a database. Let's do a memory benchmark to see why. This benchmark is going to create 100 network devices. So imagine a medium-sized enterprise network, and then we'll test two approaches. One, our persistent database approach that we just discussed, and two, the traditional context window approach, which is what most AI tools use. Watch what happens. This for loop is able to create 100 fake network devices, dev one, dev two, up to dev 100. Each has a host name, IP address, type, and status, just like your real network inventory. For the results, we can see that persistent memory gave us 100% accuracy in two seconds. Meanwhile, context windows gave us 40% accuracy in 0.8 seconds. We can say our database approach remembers every device perfectly. You can ask it about dev one, and it can give you dev one's info every single time. We also know that our context window approach only remembers about 40% of devices. Why? That's because it's trying to remember 100 devices in its temporary memory. It's like trying to memorize the entire network topology during a phone call. You'll most likely forget most of it, and you might be able to recall some of it. Also, the database lookup is 40 times faster. That's the difference between querying a well-indexed database and searching through notes. And in terms of five times more devices, context windows max out around 20 devices most of the time, so our approach handles 100, which could handle 10,000 just as easily. But with 10,000 examples, grouping things together can really help, and that's where event correlation comes in. So for this section, we can track that dev one has had three related events. It's had interface flapping detected, packet loss increased, and the interface went down. These events all happen to be these events all happen to different times, but we can correlate them because they're all stored permanently with timestamps and device IDs. That's how you do the root cause analysis, which will be helpful for us to see our patterns over time. Context windows don't have the ability to do that because they forget the first event by the time that the third one happens. Finally, we're going to get into our self-registering agent. So this agent can track its own capabilities and learn new ones from experience. So let's run it and see what it says. The agent just created itself with a unique ID. It starts with three basic capabilities, device monitoring, configuration management, and event logging. Now watch what happens when we log a critical network event. We log that the router R1 interface went down as a critical event. And then when we look at the next line, we can see that the agent automatically learned a new capability called incident troubleshooting. This is possible through our log network event function. Our function is saying that if the severity is critical and we haven't learned troubleshooting yet, then please learn it. Just like humans can build new skills based on experience, this agent is learning incident response by doing it. So let's see how it does with four more capabilities. Now our agent knows BGP troubleshooting, automated failover, security analysis, and performance optimization. That's eight total capabilities up from three. And these capabilities will be stored in those databases that we created earlier. This is a database table that tracks what the agent knows and when it learned it. If you restart the agent, then it will still know all eight capabilities. This matters for network operations because you can track what has this agent handled before? When did it learn to handle BGP issues? And what evidence do we have of what it can do? So similar to episode one, the conclusion here is that structure matters. Just like you wouldn't store your entire network config into one single text file, you shouldn't store all of your agent's knowledge in temporary memory. You should use the right tool for each job. So database for persistence, vector search for semantic similarity, graphs for relationships, and timelines for chronological events. So what next? How do you implement this? First, take a look at the GitHub in the description and try to implement what we did today. When you go to the GitHub repo, you'll see an additional file called agencymemoryimplementation.py. I won't be running it here today. It contains a full agency SDK implementation demo, including its Corto and Longo protocols named after coffee. Corto is agency's memory coordination protocol, which is how agents share and synchronize their memories across a distributed system. And Longo is the self-registration protocol. It's how agents discover each other and register their capabilities in a directory. It also shows you what a production-ready environment looks like with all of the databases working together. When you look at this in the context of the real world, you can have customer service agents that remember every interaction across months. In terms of research, you can have assistants that build knowledge graphs for all your documents. In terms of coding, you can have software development agents that learn your coding patterns, your preferences. And in terms of business, you can have business-specific agents that maintain context across projects and teams. We're moving from stateless interactions to persistent AI relationships. These aren't just tools. They're collaborative partners that have the ability to grow and grow smarter through every interaction. Coming up next week, we're going to focus mainly on multi-agent teams. For deeper information on agency-specific implementations, please feel free to check out that YouTube channel as well. Please subscribe for updates on when we release episode three and drop a comment on what type of agent team you'd most likely want to build. Memory architecture is important to look at, but building a team with what we learned might yield some pretty cool results. As usual, thanks everyone for joining, and I'll see you next time.
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="building-smarter-ai-agents-agentcore-long-term-memory-deep-d.md">
Phase: [EXPLOITATION]

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

When the agentic application sends conversational events to AgentCore Memory, it initiates a pipeline to transform raw conversational data into structured, searchable knowledge through a multi-stage process. Let’s explore each component of this system.

### 1\. Memory extraction: From conversation to insights

When new events are stored in short-term memory, an asynchronous extraction process analyzes the conversational content to identify meaningful information. This process leverages large language models (LLMs) to understand context and extract relevant details that should be preserved in long-term memory. The extraction engine processes incoming messages alongside prior context to generate memory records in a predefined schema. As a developer, you can configure one or more Memory strategies to extract only the information types relevant to your application needs. The extraction process supports three built-in memory strategies:

- **Semantic memory**: Extracts facts and knowledge. Example:

```code
"The customer's company has 500 employees across Seattle, Austin, and Boston"
```

- **User preferences**: Captures explicit and implicit preferences given context. Example:

```code
{“preference”: "Prefers Python for development work", “categories”: [“programming”, ”code-style”], “context”: “User wants to write a student enrollment website”}
```

- **Summary memory**: Creates running narratives of conversations under different topics scoped to sessions and preserves the key information in a structured XML format. Example:

```code
<topic=“Material-UI TextareaAutosize inputRef Warning Fix Implementation”> A developer successfully implemented a fix for the issue in Material-UI where the TextareaAutosize component gives a "Does not recognize the 'inputRef' prop" warning when provided to OutlinedInput through the 'inputComponent' prop. </topic>
```

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

- **Memory failures**: If consolidation fails for one memory, it doesn’t impact others. The system uses exponential backoff and retry mechanisms to handle transient failures. If consolidation ultimately fails, the memory is added to the system to help prevent potential loss of information.

## **Advanced custom** memory strategy configurations

While built-in memory strategies cover common use cases, AgentCore Memory recognizes that different domains require tailored approaches for memory extraction and consolidation. The system supports [built-in strategies with overrides](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-custom-strategy.html) for custom prompts that extend the built-in extraction and consolidation logic, letting teams adapt memory handling to their specific requirements. To maintain system compatibility and focus on criteria and logic rather than output formats, custom prompts help developers customize what information gets extracted or filtered out, how memories should be consolidated, and how to resolve conflicts between contradictory information.

AgentCore Memory also supports custom model selection for memory extraction and consolidation. This flexibility helps developers balance accuracy and latency based on their specific needs. You can define them via the APIs when you create the _memory\_resource_ as a strategy override or via the console (as shown below in the console screenshot).

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
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="context-engineering-llm-memory-and-retrieval-for-ai-agents-w.md">
Phase: [EXPLOITATION]

## But What Is a Context Window?

The context window is the model's active workspace, where it holds instructions and information for a current task. Every word, number, and piece of punctuation consumes space in this window. Think of it like a whiteboard: once it fills up, older information must be erased to make room for the new, causing important past details to be lost.
In more technical terms, a context window refers to the maximum amount of input data a language model can consider at one time when generating responses, measured in [tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them). This window includes all your inputs, model's outputs, tool calls, and retrieved documents, acting as the model’s short-term memory. Every token placed in the context window directly influences what the model can "see" and how it responds.

## Context Engineering vs. Prompt Engineering

Prompt engineering focuses on how you phrase and structure instructions for the LLM to generate the best results, such as writing clear/clever prompts, adding examples, or asking the model to "think step-by-step.” While important, prompt engineering alone cannot fix the fundamental limitation of a disconnected model.

Context engineering, on the other hand, is the discipline of designing the architecture that feeds an LLM the right information at the right time. It's about building the bridges that connect a disconnected model to the outside world, retrieving external data, using tools, and giving it a memory to ground its responses in facts, not just training data.

In practice, context engineering is how you build LLM memory: deciding what stays in the context window, what gets stored as long-term memory, and what gets retrieved later.

## The Context Window Challenge

The LLM context window can only hold so much information at once. This fundamental constraint shapes what agents and agentic systems are currently capable of. Every time an agent processes information, it must decide what remains active, what can be summarized/compressed/deleted, what should be stored externally, and how much space to reserve for reasoning. It's tempting to assume that shoving everything into bigger context windows solves this problem, but this is generally not the case. This is why production agents need deliberate memory architecture—not just bigger windows.

Here are the critical failure modes that emerge as context grows:

- **Context Poisoning**: Incorrect or hallucinated information enters the context. Because agents reuse and build upon that context, these errors continue and compound.
- **Context Distraction**: The agent becomes burdened by too much past information; history, tool outputs, summaries, and over-relies on repeating past behavior rather than reasoning fresh.
- **Context Confusion**: Irrelevant tools or documents crowd the context, distracting the model and causing it to use the wrong tool or instructions.
- **Context Clash**: Contradictory information within the context misleads the agent, leaving it stuck between conflicting assumptions.

These aren't just technical limitations, these are core design challenges of any modern AI app. You can't fix this fundamental limitation by simply writing better prompts or increasing the maximum size of the context window. You have to build a system around the model.

That is what Context Engineering is all about!

## Memory

This is what most people mean when they search for LLM memory or agent memory: a system that combines the context window with retrieval and long-term storage so the agent can stay consistent over time.

A stateless LLM can answer a single question well, but it has no idea what happened five minutes ago or why that matters for the next decision. Memory transforms the model into something that feels more dynamic and, dare we say, more ‘human’, that’s capable of holding onto context, learning from the past, and adapting on the fly. For context engineering, the core challenge is not “how much can we store?” but “what deserves a spot in front of the model right now, and what can safely live elsewhere?

**The Architecture of Agent Memory**

Memory in an AI agent is all about retaining information to navigate changing tasks, remember what worked (or didn't), and think ahead. To build robust agents, we need to think in layers, often blending different types of memory for the best results.

**Short‑term memory** is the live context window: recent turns/reasoning, tool outputs, and retrieved documents that the model needs to reason about the current step. This space is brutally finite, so it should stay lean, just enough conversation history to keep the thread coherent and decisions grounded.

**Long-term memory**, by contrast, lives outside the model, usually in vector databases for quick retrieval ( [RAG](https://weaviate.io/blog/introduction-to-rag)). These stores keep information permanently, and can hold:

- Episodic Data: past events, user interactions, preferences
- Semantic Data: general and domain knowledge
- Procedural Data: routines, workflows, decision steps

Because it’s external, this memory can grow, update, and persist beyond the model’s context window.

Most modern systems usually implement a hybrid memory setup, i.e., blending short-term memory with long-term for depth. Some architectures also add a _working memory_: a temporary space for information needed during a multi-step task. For example, while booking a trip, an agent might keep the destination, dates, and budget in working memory until the task is done, without storing it permanently. This is often called persistent memory or agent long-term memory.

**Designing Memory That Doesn’t Pollute Context**

The worst memory system is the one that faithfully stores everything. Old, low‑quality, or noisy entries eventually come back through retrieval and start to contaminate the context with stale assumptions or irrelevant details. Effective agents are selective: they filter which interactions get promoted into long‑term storage, often by letting the model “reflect” on an event and assign an importance or usefulness score before saving it.

Once in storage, memories need maintenance. Periodic pruning, merging duplicates, deleting outdated facts, and replacing long transcripts with compact summaries keep retrieval sharp and prevent the context window from being filled with historical clutter. Criteria like recency and retrieval frequency are simple but powerful signals for what to keep and what to retire.

Our eBook’s memory section goes deeper into more of these memory management strategies, including mastering the art of retrieval, being selective about what you store, and pruning and refining memories. It also highlights the key principle: always tailor the memory architecture to the task because there’s no one-size-fits-all solution (at least not yet).

Terminology

If you're searching for **LLM memory** or **agent memory**, you're usually looking for the systems behind context engineering: **retrieval**, **long-term memory storage**, and **rules for what enters the context window** at each step.
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="core-concepts.md">
Phase: [EXPLOITATION]

# Long-term Memory in LLM Applications

Long-term memory allows agents to remember important information across conversations. LangMem provides ways to extract meaningful details from chats, store them, and use them to improve future interactions. At its core, each memory operation in LangMem follows the same pattern:

1. Accept conversation(s) and current memory state
2. Prompt an LLM to determine how to expand or consolidate the memory state
3. Respond with the updated memory state

The best memory systems are often application-specific. In designing yours, the following questions can serve as a useful guide:

1. **What** type of content should your agent learn: facts/knowledge? summary of past events? Rules and style?
2. **When** should the memories be formed (and **who** should form the memories)
3. **Where** should memories be stored? (in the prompt? Semantic store?). This largely determines how they will be recalled.

## Types of Memory

Memory in LLM applications can reflect some of the structure of human memory, with each type serving a distinct purpose in building adaptive, context-aware systems:

| Memory Type | Purpose | Agent Example | Human Example | Typical Storage Pattern |
| --- | --- | --- | --- | --- |
| Semantic | Facts & Knowledge | User preferences; knowledge triplets | Knowing Python is a programming language | Profile or Collection |
| Episodic | Past Experiences | Few-shot examples; Summaries of past conversations | Remembering your first day at work | Collection |
| Procedural | System Behavior | Core personality and response patterns | Knowing how to ride a bicycle | Prompt rules or Collection |

### Semantic Memory: Facts and Knowledge

Semantic memory stores the essential facts and other information that ground an agent's responses. Two common representations of semantic memory are collections (to record an unbounded amount of knowledge to be searched at runtime) and profiles (to record task-specific information that follows a strict schema that is easily looked up by user or agent).

#### Collection

Collections are what most people think of when they imagine agent long-term memory. In this type, memories are stored as individual documents or records. For each new conversation, the memory system can decide to insert new memories to the store.

Using a collection-type memory adds some complexity to the process of updating your memory state. The system must reconcile new information with previous beliefs, either _deleting_/ _invalidating_ or _updating_/ _consolidating_ existing memories. If the system over-extracts, this could lead to reduced precision of memories when your agent needs to search the store. If it under-extracts, this could lead to low recall. LangMem uses a memory enrichment process that strives to balance memory creation and consolidation, while letting you, the developer, customize the instructions to further shift the strength of each.

Finally, memory relevance is more than just semantic similarity. Recall should combine similarity with "importance" of the memory, as well as the memory's "strength", which is a function of how recently/frequently it was used.

Extracting semantic memories as collectionsSetup

```
from langmem import create_memory_manager

manager = create_memory_manager(
    "anthropic:claude-3-5-sonnet-latest",
    instructions="Extract all noteworthy facts, events, and relationships. Indicate their importance.",
    enable_inserts=True,
)

# Process a conversation to extract semantic memories
conversation = [\
    {"role": "user", "content": "I work at Acme Corp in the ML team"},\
    {"role": "assistant", "content": "I'll remember that. What kind of ML work do you do?"},\
    {"role": "user", "content": "Mostly NLP and large language models"}\
]
```

```
memories = manager.invoke({"messages": conversation})
```

#### Profiles

**Profiles** on the other hand are well-scoped for a particular task. Profiles are a single document that represents the current state, like a user's main goals with using an app, their preferred name and response style, etc. When new information arrives, it updates the existing document rather than creating a new one. This approach is ideal when you only care about the latest state and want to avoid remembering extraneous information.

Managing user preferences with profilesSetup

```
from langmem import create_memory_manager
from pydantic import BaseModel

class UserProfile(BaseModel):
    """Save the user's preferences."""
    name: str
    preferred_name: str
    response_style_preference: str
    special_skills: list[str]
    other_preferences: list[str]

manager = create_memory_manager(
    "anthropic:claude-3-5-sonnet-latest",
    schemas=[UserProfile],
    instructions="Extract user preferences and settings",
    enable_inserts=False,
)

# Extract user preferences from a conversation
conversation = [\
    {"role": "user", "content": "Hi! I'm Alex but please call me Lex. I'm a wizard at Python and love making AI systems that don't sound like boring corporate robots 🤖"},\
    {"role": "assistant", "content": "Nice to meet you, Lex! Love the anti-corporate-robot stance. How would you like me to communicate with you?"},\
    {"role": "user", "content": "Keep it casual and witty - and maybe throw in some relevant emojis when it feels right ✨ Also, besides AI, I do competitive speedcubing!"},\
]
```

```
profile = manager.invoke({"messages": conversation})[0]
```

Choose between profiles and collections based on how you'll use the data: profiles excel when you need quick access to current state and when you have data requirements about what type of information you can store. They are also easy to present to a user for manual editing. Collections are useful when you want to track knowledge across many interactions without loss of information, and when you want to recall certain information contextually rather than every time.

### Episodic Memory: Past Experiences

Episodic memory preserves successful interactions as learning examples that guide future behavior. Unlike semantic memory which stores facts, episodic memory captures the full context of an interaction—the situation, the thought process that led to success, and why that approach worked. These memories help the agent learn from experience, adapting its responses based on what has worked before.

Defining and extracting episodesSetup

```
from pydantic import BaseModel, Field
from langmem import create_memory_manager

class Episode(BaseModel):
    """An episode captures how to handle a specific situation, including the reasoning process
    and what made it successful."""

    observation: str = Field(
        ...,
        description="The situation and relevant context"
    )
    thoughts: str = Field(
        ...,
        description="Key considerations and reasoning process"
    )
    action: str = Field(
        ...,
        description="What was done in response"
    )
    result: str = Field(
        ...,
        description="What happened and why it worked"
    )

manager = create_memory_manager(
    "anthropic:claude-3-5-sonnet-latest",
    schemas=[Episode],
    instructions="Extract examples of successful interactions. Include the context, thought process, and why the approach worked.",
    enable_inserts=True,
)

# Example conversation
conversation = [\
    {"role": "user", "content": "What's a binary tree? I work with family trees if that helps"},\
    {"role": "assistant", "content": "A binary tree is like a family tree, but each parent has at most 2 children. Here's a simple example:\n   Bob\n  /  \\\nAmy  Carl\n\nJust like in family trees, we call Bob the 'parent' and Amy and Carl the 'children'."},\
    {"role": "user", "content": "Oh that makes sense! So in a binary search tree, would it be like organizing a family by age?"},\
]
```

```
# Extract episode(s)
episodes = manager.invoke({"messages": conversation})
```

### Procedural Memory: System Instructions

Procedural memory encodes how an agent should behave and respond. It starts with system prompts that define core behavior, then evolves through feedback and experience. As the agent interacts with users, it refines these instructions, learning which approaches work best for different situations.

Optimizing prompts based on feedbackSetup

```
from langmem import create_prompt_optimizer

optimizer = create_prompt_optimizer(
    "anthropic:claude-3-5-sonnet-latest",
    kind="metaprompt",
    config={"max_reflection_steps": 3}
)
```

```
prompt = "You are a helpful assistant."
trajectory = [\
    {"role": "user", "content": "Explain inheritance in Python"},\
    {"role": "assistant", "content": "Here's a detailed theoretical explanation..."},\
    {"role": "user", "content": "Show me a practical example instead"},\
]
optimized = optimizer.invoke({
    "trajectories": [(trajectory, {"user_score": 0})],
    "prompt": prompt
})
```

## Writing memories

Memories can form in two ways, each suited for different needs. Active formation happens during conversations, enabling immediate updates when critical context emerges. Background formation occurs between interactions, allowing deeper pattern analysis without impacting response time. This dual approach lets you balance responsiveness with thorough learning.

| Formation Type | Latency Impact | Update Speed | Processing Load | Use Case |
| --- | --- | --- | --- | --- |
| Active | Higher | Immediate | During Response | Critical Context Updates |
| Background | None | Delayed | Between/After Calls | Pattern Analysis, Summaries |

### Conscious Formation

You may want your agent to save memories "in the hot path". This active memory formation happens during the conversation, enabling immediate updates when critical context emerges. This approach is easy to implement and lets the agent itself choose how to store and update its memory. However, it adds perceptible latency to user interactions, and it adds one more obstacle to the agent's ability to satisfy the user's needs.

### Subconscious Formation

"Subconscious" memory formation refers to the technique of prompting an LLM to reflect on a conversation after it occurs (or after it has been inactive for some period), finding patterns and extracting insights without slowing down the immediate interaction or adding complexity to the agent's tool choice decisions. This approach is perfect for ensuring higher recall of extracted information.

## Integration Patterns

LangMem's memory utilities are organized in two layers of integration patterns:

### 1. Core API

At its heart, LangMem provides functions that transform memory state without side effects. These primitives are the building blocks for memory operations:

- **Memory Managers**: Extract new memories, update or remove outdated memories, and consolidate and generalize from existing memories based on new conversation information
- **Prompt Optimizers**: Update prompt rules and core behavior based on conversation information (with optional feedback)

These core functions do not depend on any particular database or storage system. You can use them in any application.

### 2. Stateful Integration

The next layer up depends on LangGraph's long-term memory store. These components use the core API above to transform memories that exist in the store and upsert/delete them as needed when new conversation information comes in:

- **Store Managers**: Automatically persist extracted memories
- **Memory Management Tools**: Give agents direct access to memory operations

Use these if you're using LangGraph Platform or LangGraph OSS, since it's an easy way to add memory capabilities to your agents.

## Storage System

Storage is optional

Remember that LangMem's core functionality is built around that don't require any specific storage layer. The storage features described here are part of LangMem's higher-level integration with LangGraph, useful when you want built-in persistence.

When using LangMem's stateful operators or platform services, the storage system is built on LangGraph's storage primitives, providing a flexible and powerful way to organize and access memories. The storage system is designed around two concepts:

### Memory Namespaces

Memories are organized into namespaces that allow for natural segmentation of data:

- **Multi-Level Namespaces**: Group memories by organization, user, application, or any other hierarchical structure
- **Contextual Keys**: Identify memories uniquely within their namespace
- **Structured Content**: Store rich, structured data with metadata for better organization

Organizing memories hierarchically

```
# Organize memories by organization -> configurable user -> context
namespace = ("acme_corp", "{user_id}", "code_assistant")
```

Namespaces can include template variables (such as `"{user_id}"`) to be populated at runtime from `configurable` fields in the `RunnableConfig`.

### Flexible Retrieval

If you use one of the managed APIs, LangMem will integrate directly with LangGraph's BaseStore interface for memory storage and retrieval. The storage system supports multiple ways to retrieve memories:

- **Direct Access**: Get a specific memory by key
- **Semantic Search**: Find memories by semantic similarity
- **Metadata Filtering**: Filter memories by their attributes
</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="memory-for-autonomous-llm-agents-mechanisms-evaluation-and-e.md">
Phase: [EXPLOITATION]

## Abstract

Abstract Large language model (LLM) agents increasingly operate in settings where a single context window is far too small to capture what has happened, what was learned, and what should not be repeated.
Memory—the ability to persist, organize, and selectively recall information across interactions—is what turns a stateless text generator into a genuinely adaptive agent.
This survey offers a structured account of how memory is designed, implemented, and evaluated in modern LLM-based agents, covering work from 2022 through early 2026.
We formalize agent memory as a write–manage–read loop tightly coupled with perception and action, then introduce a three-dimensional taxonomy spanning temporal scope, representational substrate, and control policy.
Five mechanism families are examined in depth: context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, and policy-learned management.
On the evaluation side, we trace the shift from static recall benchmarks to multi-session agentic tests that interleave memory with decision-making, analyzing four recent benchmarks that expose stubborn gaps in current systems.
We also survey applications where memory is the differentiating factor—personal assistants, coding agents, open-world games, scientific reasoning, and multi-agent teamwork—and address the engineering realities of write-path filtering, contradiction handling, latency budgets, and privacy governance.
The paper closes with open challenges: continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, and multimodal embodied memory.

## 1 Introduction

Scaling large language models has unlocked a new class of autonomous software agents—systems that perceive environments, reason about goals, wield tools, and take action over extended time horizons .
What separates these agents from a vanilla chatbot is not merely bigger models; it is the expectation that they *learn from experience*.
A coding assistant should remember that a particular API is flaky, a game-playing agent should recall which crafting recipes it already mastered, and a personal scheduler should never ask a user’s birthday twice.
All of this demands memory.

### 1.1 What goes wrong without it

Picture a debugging assistant that works on a large codebase across a week of sessions.
Without memory, every Monday morning it rediscovers the directory layout, re-reads the same README, and—worst of all—retries the exact fix that crashed the build on Friday.
Equip the same agent with even a modest memory module and the dynamic shifts: it arrives already knowing the hotspots, skips the dead ends, and gradually distills project-specific heuristics.

This is not a marginal improvement; it is a qualitative change.
Memory transforms a stateless LLM into a *self-evolving* agent  that can (i) accumulate factual knowledge and user preferences, (ii) develop behavioral patterns grounded in prior experience, (iii) avoid repeating costly mistakes, and (iv) continuously improve through interaction.

### 1.2 A brief history of neural memory

The ambition to give neural networks external storage dates back over a decade.
Memory Networks  and their end-to-end variant  introduced differentiable read-write access to external slots for question answering.
Neural Turing Machines  and Differentiable Neural Computers  pushed further, supporting both content-based and location-based addressing over a memory matrix.
Memorizing Transformers  and Recurrent Memory Transformers  later integrated explicit memory layers directly into the Transformer backbone.

A parallel thread focused on retrieval.
RAG  married a pre-trained generator with a dense document retriever, and RETRO  showed that pulling from a *trillion*-token corpus at inference time could match much larger models at a fraction of the parameter count.
These systems proved a crucial point: external knowledge stores can be queried dynamically during generation without retraining.

The leap from retrieval-augmented *models* to memory-augmented *agents* happened quickly.
ReAct  interleaved reasoning traces with environment actions, producing an interpretable trajectory that doubles as short-horizon memory.
Reflexion  took this further by storing verbal self-critiques after task attempts—essentially giving the agent a post-mortem journal.
Then came the Generative Agents paper , whose simulated town of 25 characters demonstrated that a simple observation–reflection–planning loop could produce months of coherent social behavior.
Since 2023, the design space has exploded: hierarchical virtual memory inspired by operating systems , ever-growing skill libraries in Minecraft , SQL databases as symbolic memory , and—most recently—end-to-end learned memory management via reinforcement learning .

### 1.3 Why another survey?

Several broad agent surveys already exist , and Zhang et al.  published a memory-focused review in 2024.
However, the landscape has shifted considerably since then.
A wave of 2025–2026 contributions—Agentic Memory , MemBench , MemoryAgentBench , MemoryArena —has introduced learned memory control, richer evaluation dimensions, and agentic benchmarks that tightly couple memory with action.

This survey zooms in on the *memory module* and asks three questions:

- RQ1
How should memory in LLM agents be decomposed and formalized?
- RQ2
What mechanisms exist, and what trade-offs do they impose?
- RQ3
How should memory be evaluated when the ultimate test is downstream agent performance?

Contributions.
We formalize agent memory as a write–manage–read loop within a POMDP-style agent cycle (Section [2](#S2)), propose a three-dimensional taxonomy that unifies disparate designs (Section [3](#S3)), provide deep mechanism reviews with concrete system comparisons (Section [4](#S4)), survey benchmarks alongside a practical metric stack (Section [5](#S5)), map applications where memory is the differentiating factor (Section [6](#S6)), discuss engineering realities and architecture patterns (Section [7](#S7)), position relative to prior surveys (Section [8](#S8)), and chart open research directions (Section [9](#S9)).

## 2 Problem Formulation and Design Objectives

### 2.1 The agent loop, seen through memory

At each discrete step $t$, an agent receives input $x_{t}$—a user message, a sensor reading, or a tool return value—and must produce an action $a_{t}$.
Between these two events, it consults its accumulated memory.
We write:

$$a_{t}=\pi_{\theta}\!\bigl(x_{t},\;\mathcal{R}(M_{t},x_{t}),\;g_{t}\bigr),\quad\text{(1)}$$

$$M_{t+1}=\mathcal{U}\!\bigl(M_{t},x_{t},a_{t},o_{t},r_{t}\bigr),\quad\text{(2)}$$

where $\pi_{\theta}$ is the policy (typically a prompted or partially fine-tuned LLM), $\mathcal{R}$ reads from memory, $\mathcal{U}$ writes to and manages memory, $g_{t}$ encodes active goals, $o_{t}$ is environment feedback, and $r_{t}$ is any reward-like signal.

Two aspects deserve emphasis.
First, $\mathcal{U}$ is *not* a simple append operation.
In a well-designed system it summarizes, deduplicates, scores priority, resolves contradictions, and—when appropriate—deletes.
Second, $\pi_{\theta}$ and $(\mathcal{R},\mathcal{U})$ form a feedback loop: the agent’s decisions determine what gets written, and what is written shapes future decisions.
This recursive dependence is what makes memory both powerful and brittle—one bad write can pollute the store for many steps downstream.

### 2.2 Connection to POMDPs

Cast formally, the setup above is a partially observable Markov decision process.
Memory $M_{t}$ plays the role of the agent’s *belief state*: an internal summary of history that stands in for the unobservable true state of the world.
Classical POMDP solvers update beliefs via Bayesian filtering; LLM agents do something analogous—albeit messier—through natural language compression, vector indexing, or structured storage.

The analogy clarifies an important point: agent memory is not merely a database lookup problem.
It is about maintaining a *sufficient statistic* of the interaction history for good action selection, subject to hard computational and storage budgets.

### 2.3 Five design objectives and their tensions

Across the systems we review, memory mechanisms are pulled along five axes:

- •
Utility – Does memory actually improve task outcomes?
- •
Efficiency – What is the token, latency, and storage cost per unit of utility gained?
- •
Adaptivity – Can the system update incrementally from interaction feedback without a full retrain?
- •
Faithfulness – Is recalled information accurate and current? Stale or hallucinated recall can be worse than no recall at all.
- •
Governance – Does the system respect privacy, support deletion requests, and comply with organizational policy?

These objectives tug in opposite directions.
Maximizing utility tempts you to store everything, which bloats storage and creates governance headaches.
Aggressive compression improves efficiency but silently discards the one rare fact that turns out to be critical three weeks later.
Any real deployment must navigate these trade-offs deliberately, and the “right” balance point shifts with the application.
A medical triage agent, where a missed allergy record could be life-threatening, operates under a very different faithfulness–efficiency frontier than a casual recipe recommender.
Understanding these tensions is not merely academic—it directly shapes architectural choices, as we discuss in subsequent sections.

### 2.4 Memory as a differentiator: an empirical perspective

The practical importance of memory design is perhaps best illustrated by ablation results reported across recent systems.
In the Generative Agents experiment , removing the reflection component caused agent behavior to degenerate from coherent multi-day planning to repetitive, context-free responses within 48 simulated hours.
Voyager  without its skill library lost 15.3$\times$ in tech-tree milestone speed—the skill library *was* the performance.
And in MemoryArena , swapping an active memory agent for a long-context-only baseline dropped task completion from over 80% to roughly 45% on interdependent multi-session tasks.

These numbers underscore a recurring theme: the gap between “has memory” and “does not have memory” is often larger than the gap between different LLM backbones.
Investing in memory architecture can yield returns that rival—or exceed—model scaling.

## 3 A Unified Taxonomy of Agent Memory

Cognitive scientists have long distinguished multiple memory systems in the human brain .
Agent designers—often unconsciously—mirror that structure.
We organize the space along three orthogonal dimensions.

### 3.1 Temporal scope

Working memory.
Whatever fits inside the current context window constitutes the agent’s working memory.
Baddeley’s central executive plus buffer model  maps neatly: the LLM is the executive, the context window is the buffer, and both share the same bottleneck—limited capacity.

Episodic memory.
Records of concrete experiences: individual tool calls, conversation turns, environment observations.
In the Generative Agents world , every observation—“Isabella saw Klaus painting in the park at 3pm”—lands in the episodic stream with a timestamp, an importance score, and an embedding for later retrieval.

Semantic memory.
Abstracted, de-contextualized knowledge.
An episodic fact like “the user corrected the date format on Jan 5, Jan 12, and Feb 1” may consolidate into the semantic record “user prefers DD/MM/YYYY.”
This consolidation is rarely automatic; most current systems require explicit prompting or heuristic triggers.

Procedural memory.
Reusable skills and executable plans.
Voyager’s skill library  is the clearest example: every verified Minecraft routine is stored as runnable JavaScript, indexed by a natural language description, and composed on the fly for novel tasks.

In practice, most agents blend at least two of these.
The hard question is the *transition policy*: when does an episodic record graduate to semantic status, and when does a semantic fact get instantiated back into working memory for a specific task?

To illustrate the interplay, consider a customer-support agent handling returns.
Each return request constitutes an episodic record.
After processing hundreds of similar requests, the agent might consolidate the pattern into a semantic rule: “customers who received damaged items within 7 days are eligible for express replacement.”
When a new request arrives, this semantic rule is loaded into working memory alongside the specific episodic details of the current case.
If the agent also has stored scripts for processing returns (procedural memory), the four memory types form a complete reasoning stack: the procedure says *how*, semantic memory says *what the policy is*, episodic memory says *what happened*, and working memory holds the live reasoning context.

This four-layer integration is the aspiration; most current systems implement only two layers well and handle the transitions between layers via crude heuristics.
The consolidation step—where episodes become semantic knowledge—is particularly underserved: it typically requires either explicit developer rules or periodic LLM-driven summarization, both of which are fragile and hard to validate.

### 3.2 Representational substrate

How memory is physically stored constrains what the agent can efficiently do with it.

Context-resident text—summaries, scratchpads, chain-of-thought traces —is the simplest substrate.
Fully transparent, zero infrastructure, but ruthlessly capacity-limited.

Vector-indexed stores encode records as dense embeddings and support approximate nearest-neighbor search .
They scale gracefully to millions of records but lose structured relationships: you can ask “what’s most similar?” but not “what caused what?”

Structured stores—SQL databases , key–value maps, knowledge graphs —preserve relational structure and support complex queries (“all API failures involving service X in the last 7 days”), at the cost of upfront schema design.

Executable repositories—code libraries, tool definitions, plan templates —let the agent invoke stored skills directly, sidestepping regeneration and the errors it introduces.

Hybrid stores are the norm in production.
MemGPT , for instance, layers a context-window “main memory” over a searchable recall database and a vector-indexed archive—each tier with different access patterns and eviction rules.

### 3.3 Control policy

Perhaps the most consequential—and least discussed—dimension is *who decides* what to store, what to retrieve, and what to discard.

Heuristic control hard-codes rules: top-$k$ retrieval, summarize every $n$ turns, expire records older than $d$ days.
Predictable, easy to debug, but blind to context.

Prompted self-control exposes memory operations as tool calls and lets the LLM decide when to invoke them.
MemGPT’s core_memory_append and archival_memory_search are canonical examples .
Quality here hinges on the LLM’s instruction-following ability and on how well the memory API is documented in the system prompt.

Learned control treats memory operations as policy actions optimized end-to-end.
Agentic Memory  trains store, retrieve, update, summarize, and discard as callable tools via a three-stage RL pipeline with step-wise GRPO.
The payoff is substantial—learned policies discover non-obvious strategies such as preemptive summarization before the context is full—but so is the training cost.

### 3.4 Representative systems at a glance

Table [1](#S3.T1) plots key systems and benchmarks on a timeline.

**Table 1: Representative memory systems and benchmarks for LLM agents (2020–2026).**
| System | Year | Memory Category | Distinguishing Feature |
| --- | --- | --- | --- |
| RAG | 2020 | Non-parametric retrieval | First to couple a seq2seq generator with a dense document retriever at NeurIPS 2020. |
| RETRO | 2022 | Retrieval at scale | Chunks retrieved from a 2-trillion-token corpus; 7.5B-parameter model rivals 175B Jurassic-1 on 10/16 benchmarks. |
| ReAct | 2022 | Trajectory traces | Reasoning-and-acting traces double as short-horizon working memory; 34% absolute gain on ALFWorld. |
| Reflexion | 2023 | Reflective episodic | Verbal self-critiques stored as episodic memory; 91% pass@1 on HumanEval (vs. 80% GPT-4 baseline). |
| Generative Agents | 2023 | Episodic + reflective | 25 simulated characters autonomously organize a Valentine’s party via observation–reflection–planning cycles. |
| Voyager | 2023 | Procedural skill library | 3.3$\times$ more unique items and 15.3$\times$ faster tech-tree progression than prior Minecraft agents. |
| LongMem | 2023 | Long-form external | Frozen backbone + residual side-network; memory bank scales to 65k tokens. |
| ChatDB | 2023 | Structured symbolic | SQL databases as agent memory; supports precise INSERT/SELECT queries over interaction records. |
| ExpeL | 2024 | Experiential learning | Systematically extracts success/failure “rules of thumb” from trajectory comparisons. |
| MemGPT | 2024 | Hierarchical virtual | OS-inspired paging across main context, recall DB, and archival vector store. |
| MemoryBank | 2024 | Long-term with forgetting | Ebbinghaus-curve decay applied to chatbot memory; published at AAAI 2024. |
| LoCoMo | 2024 | Benchmark | Up to 35 sessions, 300+ turns, 9k–16k tokens per conversation; humans still far ahead. |
| MemBench | 2025 | Benchmark | Separates factual vs. reflective memory; participation vs. observation modes; ACL 2025 Findings. |
| MemoryAgentBench | 2025 | Benchmark | Tests four cognitive competencies; no current system masters all four. |
| Agentic Memory | 2026 | Unified STM/LTM policy | Memory ops trained as RL actions via step-wise GRPO; outperforms all memory-augmented baselines on five benchmarks. |
| MemoryArena | 2026 | Benchmark | Multi-session interdependent tasks in four domains; near-saturated LoCoMo models drop to 40–60% here. |

## 4 Core Memory Mechanisms

We now examine each mechanism family in detail, grounding the discussion in concrete system designs and their empirical trade-offs.

### 4.1 Context-resident memory and compression

The most straightforward way to give an agent memory is to keep relevant information in the prompt.
System messages, recent conversation turns, scratchpad notes—everything the LLM “sees” on every call functions as working memory with perfect in-window recall.

The trouble starts when history outgrows the window.
Several compression strategies have emerged:
(i) *sliding windows* that retain the $n$ most recent turns and drop the rest;
(ii) *rolling summaries* that periodically condense older history into a shorter precis;
(iii) *hierarchical summaries* operating at turn, session, and topic granularities;
(iv) *task-conditioned compression*, where the current query decides which parts of history keep full detail.
The Self-Controlled Memory system  hands this decision to the agent itself, letting it choose which segments deserve verbatim retention versus aggressive condensation.

Context-resident memory is transparent and infrastructure-free, but it carries a well-known pathology: *summarization drift*.
Each compression pass silently discards low-frequency details.
After enough passes, the agent “remembers” a sanitized, generic version of history—precisely the kind of memory that fails on edge cases.
Extending context windows to 100k+ tokens  delays the problem but cannot eliminate it, and longer contexts incur quadratic cost increases in attention.

To make this concrete: consider an agent that processes 50 user interactions per day.
After one week of rolling summarization, the raw 350-turn history has been compressed through at least three summary cycles.
A rare but critical instruction from day one—say, “never call the production database directly”—may survive the first compression but is exactly the kind of low-frequency, high-importance detail that tends to vanish by the third pass.
The agent then proceeds to call the production database, with predictable consequences.

This is not a hypothetical failure mode; it mirrors reported issues in deployed long-running chatbots and coding assistants.
The implication is clear: for any agent expected to run for more than a handful of sessions, context-resident memory should be supplemented—not replaced, but supplemented—with an external store that preserves raw records at full fidelity.

A less obvious but equally important limitation of context-resident memory is *attentional dilution*.
Even within a sufficiently large window, the LLM’s attention mechanism must distribute capacity across all tokens.
As more memory content is injected, the model’s ability to focus on any single piece degrades—a phenomenon empirically documented in the “lost in the middle” literature, where information placed in the center of a long context is recalled less reliably than information at the beginning or end.
This suggests that simply making the window bigger is not a complete solution; the agent must also *curate* what enters the window, which brings us back to the fundamental need for retrieval and filtering mechanisms.

### 4.2 Retrieval-augmented memory stores

RAG  demonstrated that pairing a generator with a non-parametric retrieval index produces strong results on knowledge-intensive tasks.
In agent settings, the store is populated not with encyclopedia articles but with *living interaction records*: tool call logs, environment observations, user corrections, partial plans, and verbal reflections.

Indexing granularity.
Fine-grained indexing (individual tool calls or single sentences) gives precise recall but can fragment multi-step reasoning into meaningless shards.
Coarse-grained indexing (full sessions or long passages) preserves context but drowns the signal in noise.
The practical sweet spot is multi-granularity indexing, where the retriever adaptively selects the right resolution.
Dense passage retrieval  via learned encoders, typically backed by FAISS-style approximate nearest-neighbor search , remains the default implementation, often augmented with sparse BM25 and metadata filters (timestamps, tool types, task tags).

Query formulation.
A subtlety that many systems gloss over: the agent’s immediate input $x_{t}$ is often a poor retrieval query.
A user asking “Why did that crash?” needs the agent to retrieve the crash log from two sessions ago, not the most semantically similar sentence.
Strategies include LLM-reformulated queries, multi-query fan-out with result fusion, and using the current subgoal as an additional retrieval signal.
Self-RAG  goes one step further and teaches the model to decide *whether* retrieval is warranted at all—a simple gate that substantially cuts unnecessary latency.

Scale.
RETRO  and follow-up work on trillion-token datastores  suggest that retrieval memory can scale to years of interaction history without architectural changes.
The bottleneck shifts decisively from storage to *relevance*: ensuring that the most *useful*—not merely the most *similar*—records are returned.

Read-write memory.
RET-LLM  bridges free-form retrieval and structured storage by letting the agent write structured triplets at storage time while querying them via natural language.
This is a pragmatic compromise: schema at write time, flexibility at read time.

### 4.3 Reflective and self-improving memory

Reflexion  introduced a deceptively simple idea: after failing a task, have the agent write a natural language post-mortem, then prepend it to the prompt on the next attempt.
No gradient updates, no reward model—just a text file of self-critiques.
The results were striking: 91% pass@1 on HumanEval, versus 80% for GPT-4 without reflection.

Generative Agents  built a richer pipeline.
Raw observations accumulate in an episodic stream.
Periodically, the agent clusters related observations and synthesizes higher-order *reflections*—e.g., “Klaus has been eating alone and seems withdrawn.”
Retrieval scores memories by a weighted mix of recency (exponential decay), relevance (embedding similarity), and importance (a self-assessed integer).
This multi-signal scoring is a substantial improvement over pure cosine similarity and remains influential in later designs.

ExpeL  pushes the paradigm further by systematically contrasting successful and failed trajectories, extracting discriminative “rules of thumb,” and storing them as reusable heuristics.
Think-in-Memory  separates retrieval from reasoning: the agent first recalls, then performs a dedicated thinking step over the recalled content before generating a response.

The central risk of reflective memory is *self-reinforcing error*.
If the agent incorrectly concludes “API X always returns errors with parameter Y,” it will avoid that call path forever, never collecting evidence to overturn the false belief.
Over-generalization is the sibling risk: a lesson learned in one context applied blindly in another.
Quality gates—confidence scores, contradiction checking against other memories, periodic expiration—are necessary but still underdeveloped.

The problem becomes more acute at scale.
A single incorrect reflection in a short-lived agent causes limited damage; the same incorrect reflection persisting in a long-running production agent—potentially influencing thousands of downstream decisions over weeks—can be catastrophic.
The severity of the reflective memory failure mode scales with agent lifetime, making it particularly dangerous in exactly the settings where memory is most needed.

One mitigation strategy explored in recent work is *reflection grounding*: requiring the agent to cite specific episodic evidence for each reflection it generates.
If the reflection “API X is unreliable” must point to three concrete failure instances, the agent is less likely to generate baseless generalizations.
This does not fully solve the problem—the cited evidence may itself be unrepresentative—but it provides an auditable trail that can be reviewed by human operators.

### 4.4 Hierarchical memory and virtual context management

MemGPT  borrows an idea that operating system designers perfected decades ago: virtual memory.
An OS gives each process the illusion of vast, contiguous memory by transparently paging data between RAM and disk.
MemGPT does the same for the LLM’s context window:

- •
Main context (RAM): the active window holding system prompt, recent messages, and currently relevant records.
- •
Recall storage (disk): a searchable database of all past messages.
- •
Archival storage (cold storage): a vector-indexed store for documents and long-term knowledge.

The agent moves data between tiers by calling memory management “functions”—archival_memory_search, core_memory_append, and so on.
An interrupt mechanism passes control to the agent on each user message or timer event, letting it perform multiple internal memory operations before responding.

JARVIS-1  extends the hierarchical principle to multimodal settings, with separate stores for visual observations, textual plans, and executable skills.
Cognitive Architectures for Language Agents  propose a generalized blueprint where working, episodic, semantic, and procedural stores interact through a central executive (the LLM), directly echoing Baddeley’s model .

The Achilles’ heel of hierarchical memory is *orchestration*.
Page the wrong things in and you waste precious context tokens; archive too aggressively and you create “memory blindness”—the agent simply does not know that the critical fact exists somewhere in cold storage.
This tension motivates the next mechanism family.

It is worth noting that orchestration failures in hierarchical memory tend to be *silent*.
Unlike a crashed API call, which produces an error message, a paging decision that evicts the wrong record simply results in a slightly worse response—no exception, no log entry, no obvious signal that something went wrong.
Over time, these silent failures compound.
Diagnosing them requires detailed memory operation logs and retrospective analysis—an engineering investment that few current systems make but that is essential for production-grade deployments.

### 4.5 Policy-learned memory management

Heuristics and prompted self-control are not optimized for the agent’s end task.
A $k$-nearest-neighbor retriever does not know whether the retrieved record will actually help; a fixed summarization schedule does not care whether the material being compressed is important.

Agentic Memory (AgeMem)  addresses this by treating five memory operations—store, retrieve, update, summarize, discard—as callable tools within the agent’s policy, then optimizing the entire pipeline with reinforcement learning.
Training proceeds in three stages: supervised warm-up on memory demonstrations, task-level RL with outcome rewards, and finally step-level GRPO that provides denser credit assignment for individual memory actions.
Across five long-horizon benchmarks, AgeMem consistently outperforms strong baselines, and the learned policy surfaces non-obvious tactics: proactively summarizing intermediate results *before* the context fills up, and selectively discarding records that are semantically similar to existing ones but add no new information.

Open concerns remain.
RL training over long horizons is expensive.
Learned forgetting could delete safety-critical information.
Policies trained on one task distribution may fail to transfer.
And it is hard to explain *why* the agent chose a particular memory action—interpretability lags behind capability.

### 4.6 Parametric memory and weight-based adaptation

All of the above treat memory as external to the model’s weights.
An alternative family embeds memory *inside* the parameters through fine-tuning or adapter modules.
MemLLM  fine-tunes the LLM to interact with an explicit read-write memory module, tightly coupling parametric and non-parametric knowledge.
Joint training of retrieval and generation  yields better memory utilization than frozen-retriever baselines.

Parametric memory offers seamless integration—the model just “knows” things.
But it is hard to audit (where exactly in the weights is the user’s birthday stored?), hard to delete from (machine unlearning is still immature), and expensive to update (each new fact requires fine-tuning).
For these reasons, most deployed agents favor non-parametric, inspectable stores.

## 5 Evaluation: From Recall to Agentic Utility

### 5.1 Why classical retrieval metrics fall short

Precision@$k$ and nDCG tell you whether the right document was retrieved.
They say nothing about whether the agent *used* that document correctly—or whether retrieving it was even worth the latency.
Agent memory evaluation must jointly assess *memory quality* and *decision quality*, along with concerns that classical IR ignores entirely: staleness, contradiction, forgetting quality, and governance compliance.

### 5.2 The new benchmark landscape

Four recent benchmarks push evaluation in complementary directions.

LoCoMo  tests very long-term conversational memory: up to 35 sessions, 300+ turns, and 9k–16k tokens per conversation.
Three evaluation tasks—factual QA, event summarization, and dialogue generation—probe different memory demands.
The headline result: even RAG-augmented LLMs lag far behind humans, especially on temporal and causal dynamics.

MemBench  distinguishes *factual* from *reflective* memory and tests each in both *participation* and *observation* modes.
Metrics span three dimensions: effectiveness (accuracy), efficiency (number of memory operations), and capacity (performance degradation as the memory store grows).

MemoryAgentBench  grounds evaluation in cognitive science, probing four competencies: accurate retrieval, test-time learning, long-range understanding, and selective forgetting.
Long-context datasets are reformatted into incremental multi-turn interactions to simulate realistic accumulation.
No current system masters all four competencies; most fail conspicuously on selective forgetting.

MemoryArena  embeds memory evaluation inside complete agentic tasks—web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning—where later subtasks depend on what the agent learned from earlier ones.
The most striking finding: models that score near-perfectly on LoCoMo plummet to 40–60% in MemoryArena, exposing a deep gap between passive recall and active, decision-relevant memory use.

### 5.3 Benchmark comparison

Table [2](#S5.T2) summarizes design differences across these four benchmarks.

**Table 2: Feature comparison of recent agent memory benchmarks.**
| Benchmark | Year | Multi-session | Multi-turn | Agentic tasks | Forgetting | Multimodal |
| --- | --- | --- | --- | --- | --- | --- |
| LoCoMo | 2024 | ✓ | ✓ | – | – | ✓ |
| MemBench | 2025 | – | ✓ | – | – | – |
| MemoryAgentBench | 2025 | – | ✓ | – | ✓ | – |
| MemoryArena | 2026 | ✓ | ✓ | ✓ | – | – |

### 5.4 A practical metric stack

Deployment demands more nuance than any single benchmark provides.
We propose a four-layer evaluation stack:

Layer 1—Task effectiveness:
success rate, factual correctness, plan completion rate.

Layer 2—Memory quality:
retrieved-record precision/recall, contradiction rate, staleness distribution, coverage of task-relevant facts.

Layer 3—Efficiency:
latency per memory operation, prompt tokens consumed by memory content, retrieval calls per step, storage growth over time.

Layer 4—Governance:
privacy leakage rate, deletion compliance, access-scope violations.

Ablation studies should isolate the write policy, the retrieval strategy, and the compression module to attribute gains to specific components rather than the overall pipeline.

### 5.5 Cross-cutting lessons from the benchmarks

Aggregating results across these four evaluations, several patterns stand out.

Long context is not memory.
Despite context windows stretching to 200k tokens , long-context models consistently underperform purpose-built memory systems on tasks requiring selective retrieval and active management.
MemoryArena makes this starkest: passive recall aces are poor memory agents.

RAG helps, but the gap to humans is wide.
RAG-based agents beat pure long-context baselines across the board, yet the primary bottleneck is no longer storage—it is *retrieval quality*.
Agents routinely surface plausible but stale or off-topic records .

Nobody evaluates forgetting well.
Only MemoryAgentBench tests selective forgetting explicitly.
Yet in any long-running deployment, the inability to discard outdated information gradually poisons retrieval precision.

Cross-session coherence is underexplored.
Most benchmarks measure within-session performance.
MemoryArena’s multi-session design reveals that maintaining consistent knowledge and behavior across sessions separated by hours or days is a distinct—and largely unsolved—challenge.

The parametric–non-parametric gap is real.
Systems with parametric memory (fine-tuned weights) and non-parametric memory (external stores) show different failure profiles.
Parametric memory excels at seamless knowledge integration but fails at targeted deletion and auditing.
Non-parametric memory supports inspection and governance but can feel “bolted on”—the agent sometimes ignores retrieved records or uses them inconsistently.
The optimal balance between these two approaches, and how to combine them effectively, remains an open empirical question.

Evaluation must include cost.
A memory system that achieves 5% higher accuracy but triples latency and storage cost may not be an improvement in practice.
None of the current benchmarks systematically report efficiency metrics alongside effectiveness, making it difficult to assess whether reported gains are “free” or come at significant operational expense.
Future evaluations should mandate reporting of at least token consumption and latency overhead alongside accuracy numbers.

## 6 Where Memory Makes or Breaks the Agent

Memory is not uniformly important.
A one-shot translation tool barely needs it; a month-long project collaborator cannot function without it.
Below we examine domains where memory is the differentiating factor.

### 6.1 Personal assistants and conversational agents

A personal assistant that forgets your dietary restrictions or re-asks your timezone every session is, at best, annoying.
MemoryBank  models memory decay via Ebbinghaus forgetting curves : frequently accessed, high-importance memories are reinforced, while neglected ones fade.
MemGPT  demonstrates multi-session chat with evolving user models.
The core tension in this domain is *personalization without overstepping*—the agent must remember enough to be genuinely helpful without surfacing information the user considers private or forgotten.

### 6.2 Software engineering agents

Coding agents assist with generation, debugging, review, and project management across codebases that may contain millions of lines .
Memory requirements are steep: retain architecture decisions, track bug report histories, remember code-style preferences, and maintain a library of verified solutions.
ChatDev  equips role-playing agents (CEO, CTO, programmer, tester) with shared memory to keep a project coherent across development phases.
MetaGPT  structures this shared memory as standardized documents—PRDs, design specs, code modules—that persist and evolve.

The distinguishing challenge here is *structural scale*: the memory system must index and retrieve relevant portions of a codebase that may span thousands of files, not just conversations.

### 6.3 Open-world game agents

Minecraft and similar sandboxes are popular testbeds precisely because they demand long-horizon planning and compositional skill reuse.
Voyager  showed that an ever-growing skill library enables lifelong learning: 3.3$\times$ more unique items and 15.3$\times$ faster milestone progression than prior agents.
JARVIS-1  extends this with multimodal memory spanning visual observations and textual plans.
Ghost in the Minecraft  uses text-based knowledge and memory for generally capable open-world agents.

The key challenge is *compositional skill reuse*: the agent must not only recall individual skills but chain them creatively to solve novel problems.

### 6.4 Scientific reasoning and discovery

Scientific agents must track hypotheses, record experimental outcomes, digest literature, and revise beliefs as evidence accumulates.
Memory here acts as a hypothesis ledger and evidence accumulator.
The distinctive challenge is *uncertainty-aware memory*: the agent must maintain not just facts but confidence levels, and update them correctly as new data arrives—something most current memory systems handle poorly or not at all.

### 6.5 Multi-agent collaboration

When multiple agents work together, memory becomes a coordination mechanism.
AutoGen  lets agents build on each other’s contributions through shared context.
CAMEL  explores role-aware communicative agents that must remember prior agreements and collaborative history.
ProAgent  builds proactive teammates that anticipate needs based on memory of past interactions.

Two challenges dominate: *shared vs. private memory boundaries*—what should be visible to whom?—and *consistency under concurrent writes*—what happens when two agents update shared memory simultaneously?
Current multi-agent frameworks handle shared memory in one of two ways: either all memory is shared (simple but leaks private information) or each agent maintains its own store with no cross-agent access (isolated but prevents knowledge transfer).
Neither extreme is satisfactory.
A principled middle ground would define role-based access controls over a shared memory substrate, allowing a project manager agent to see high-level summaries from a developer agent without accessing the raw code diffs.
Database-style access control lists, adapted for natural language records, are a natural but unexplored solution.

### 6.6 Tool use and API orchestration

Tool-using agents  interact with APIs, databases, and web services.
Memory must track which tools exist, how to call them, what parameters worked last time, and which sequences of calls have been verified.
AgentBench  evaluates agents across eight environments; agents that lose track of their command history show sharp performance drops in multi-step tasks.
DERA  uses dialog-turn memory to refine tool-use strategies iteratively.

A practical hazard unique to this setting is *schema drift*: when an API updates its interface, stored usage patterns become invalid.
Version tracking and schema validation on stored tool-use records are essential but rarely implemented.
In fast-moving API ecosystems, a tool-use memory system that does not handle schema drift will accumulate an increasing fraction of invalid records, progressively degrading the agent’s ability to reuse past experience.

The broader point here is that tool-use memory is not just about storing “what worked”; it is about maintaining a living, versioned catalog of tool capabilities that degrades gracefully as the external world changes.
This connects to the software engineering concept of dependency management: just as a build system must track library versions, a tool-using agent must track API versions in its memory store.

### 6.7 Cross-domain memory transfer

An emerging direction is transferring memory *across* domains—e.g., debugging heuristics learned in Python reused for Java, or time-management strategies from one user applied to another.
Tree of Thoughts  provides a framework for deliberate problem-solving that could benefit from cross-domain procedural memory.
The open question is how to identify which memories generalize and which are hopelessly context-specific.

### 6.8 Summary: where different memory types matter most

The application survey reveals a clear pattern: different domains stress different memory types.
Personal assistants depend most on semantic memory (user preferences and profiles).
Software engineering agents lean heavily on procedural memory (verified code patterns and architecture decisions).
Game agents need tight integration of episodic and procedural memory (what happened $+$ what to do about it).
Scientific agents require semantic memory with explicit uncertainty tracking.
Multi-agent systems add a coordination layer that no single-agent memory design currently handles well.

No existing system provides strong support across all these profiles simultaneously, which suggests that the next leap in agent memory may come from more modular, pluggable architectures where memory components can be composed and configured per deployment rather than baked into a monolithic design.

## 7 Engineering Realities

### 7.1 The write path

Storing every interaction verbatim is tempting and almost always wrong.
Noise—small talk, redundant confirmations, repeated greetings—degrades retrieval precision.
A well-designed write path includes:
*filtering* to reject low-signal records,
*canonicalization* to normalize dates, names, and quantities,
*deduplication* to merge overlapping entries,
*priority scoring* to rank records by task relevance and novelty,
and *metadata tagging* (timestamp, source, task label, confidence) to support structured queries downstream.

The optimal filtering threshold is application-specific.
A medical agent cannot afford false negatives (missing a drug allergy mention); a casual chat assistant can tolerate them.
Between these extremes lies a spectrum: enterprise customer-support bots typically prioritize high recall for contractual commitments but accept lower recall for casual preferences, while financial advisory agents demand near-perfect recall for regulatory disclosures but can afford to forget informal chit-chat.
The write-path design should be informed by a risk analysis that maps memory failure modes to their downstream consequences in the target domain.

### 7.2 The read path

Not every step needs retrieval, and not every retrieval needs the full pipeline.
Practical read-path optimizations include:
two-stage retrieval (fast BM25 or metadata filter $\rightarrow$ slower cross-encoder reranker),
retrieval-or-not gating ,
token budgeting that dynamically allocates context space between memory and current task,
and cache layers for high-frequency records like user preferences.

### 7.3 Staleness, contradictions, and drift

A personal assistant that sends a birthday card to a user’s ex-partner at the old address is not just unhelpful—it is harmful.
Long-lived memory stores accumulate stale records, and without explicit mechanisms the agent has no way to distinguish the 2024 address from the 2022 one.

Robust systems need *temporal versioning* (prefer the newest record), *source attribution* (user statement $>$ agent inference), *contradiction detection* (flag conflicts for resolution), and *periodic consolidation* (scheduled sweeps that merge duplicates and retire stale entries).

### 7.4 Latency and cost

Users expect sub-second responses for simple queries.
Retrieval pipelines can easily add 200–500ms.
Common mitigations: asynchronous writes (defer storage until after the response), progressive retrieval (start generating while retrieval runs in parallel), and dynamic routing (skip retrieval for straightforward requests, engage the full pipeline only when ambiguity is high).

Xu et al.  show that retrieving a handful of highly relevant passages into a moderate-length context often beats both pure long-context and pure retrieval approaches—a useful guideline for tuning the latency–quality tradeoff.

### 7.5 Privacy, compliance, and deletion

Agent memory can harbor sensitive data: health details, financial records, private conversations.
Deployments must provide encryption at rest and in transit, per-user access scoping, automated PII redaction, configurable retention policies, and auditable deletion that removes data from every tier—including vector index entries and backup snapshots.

When memories have leaked into fine-tuned weights, external deletion is insufficient.
Machine unlearning  is the only path, and it remains far from production-ready.
The intersection of agent memory governance and machine unlearning is an urgent open problem.

### 7.6 Three architecture patterns

In practice, agent memory systems cluster into three recurring patterns:

Pattern A: Monolithic context.
All memory lives inside the prompt.
Zero infrastructure, fully transparent, but capacity-capped and prone to summarization drift.
Suitable for short-lived agents or rapid prototyping.

Pattern B: Context + retrieval store.
Working memory in the context window; long-term records in an external vector or structured store.
A retrieval pipeline injects relevant records each step.
This is the workhorse pattern behind most production agents today: coding assistants, customer-service bots, enterprise copilots.
The engineering burden is manageable; the main challenge is retrieval quality.

Pattern C: Tiered memory with learned control.
Multiple tiers—context, structured DB, vector store, cold archive—managed by a learned or prompted controller.
MemGPT  and AgeMem  are exemplars.
This pattern offers the most headroom but demands the most sophisticated engineering and training.

Our recommendation: start with Pattern B, instrument it thoroughly, and graduate to Pattern C only when empirical data shows that learned control meaningfully improves your target workload.

### 7.7 Observability and debugging

Memory systems are notoriously difficult to debug.
When an agent gives a wrong answer, was the problem in retrieval (wrong records surfaced), in the write path (relevant information never stored), in compression (detail lost during summarization), or in the LLM’s reasoning over correctly retrieved content?

Production deployments benefit from comprehensive memory operation logging: every write, read, update, and delete should be recorded with timestamps, triggering context, and the records involved.
Replay tools that let developers re-run a failed interaction with modified memory content are invaluable for root-cause analysis.
Some teams have found that a simple “memory diff”—showing what changed in the memory store between two conversation turns—provides more diagnostic value than traditional log analysis.

This observability infrastructure is rarely discussed in research papers, but its absence is one of the primary reasons that impressive demo-stage memory systems fail to make the transition to reliable production deployments.

Beyond debugging, memory observability also supports *continuous improvement*.
By analyzing patterns in memory operations—which types of records are retrieved most often, which are written but never read, which retrieval queries consistently return empty results—teams can identify bottlenecks and calibrate their memory systems over time.
This feedback loop is standard in database engineering (query performance monitoring, index optimization) but is almost entirely absent in agent memory practice.
Borrowing these techniques, even in simplified form, would significantly improve the reliability of deployed memory-augmented agents.

A related concern is *regression testing for memory behavior*.
When a memory system is updated—say, a new embedding model is deployed for the vector store—the effects on retrieval quality are unpredictable and potentially subtle.
Without a suite of regression tests that verify expected memory behavior on representative scenarios, changes to the memory subsystem become a source of untracked risk.
Building such test suites requires ground-truth annotations of “which memories should be retrieved for which queries,” an investment that pays dividends in system stability.

## 8 Positioning Relative to Prior Surveys

Xi et al.  and Wang et al.  offer broad agent surveys in which memory is one module among many.
Zhang et al.  focus specifically on memory and organize their review around write–manage–read operations; our work updates their coverage with 2025–2026 systems (AgeMem, MemBench, MemoryAgentBench, MemoryArena), adds a POMDP-grounded formulation, and extends the discussion to applications, engineering patterns, and governance.

Gao et al.  survey RAG comprehensively, but their scope is the retrieval–generation pipeline, not agent-specific memory needs.
Sumers et al.  propose a cognitive architecture blueprint for language agents; our taxonomy is complementary, sharing the cognitive science terminology but extending the analysis to representational substrates and control policies.

A question often raised is whether expanding context windows—from 4k in early GPT models to 200k+ today —makes external memory obsolete.
The evidence says no.
Longer context enlarges working memory but does not provide persistent cross-session storage, structured knowledge organization, selective retrieval from months of history, or governance mechanisms like deletion and access control.
Moreover, inference cost scales quadratically with context length, and Xu et al.  show empirically that a modest context augmented with targeted retrieval outperforms brute-force long context on many tasks.

## 9 Open Challenges

### 9.1 Principled consolidation

Current systems oscillate between hoarding (store everything, drown in noise) and amnesia (compress aggressively, lose rare but vital facts).
Neuroscience offers a suggestive model: during sleep, the hippocampus replays recent experiences, strengthening important traces and pruning the rest .
An analogous “offline consolidation” process—scheduled during idle periods—could provide a principled balance.
Open questions: how to estimate memory importance without future-sight, how to detect when consolidation is needed, and how to guarantee that safety-critical records survive the process.

One concrete approach worth exploring is *dual-buffer consolidation*, where newly formed memories reside in a “hot” buffer during a probation period and are promoted to long-term storage only after passing quality checks—re-verification, deduplication, and importance scoring.
This mirrors the hippocampal-to-neocortical transfer observed in biological memory , where new memories are initially hippocampus-dependent and gradually become independent through repeated reactivation.
Implementing this in an agent system would require defining the probation period, the promotion criteria, and the fallback behavior when the hot buffer overflows before promotion occurs.

### 9.2 Causally grounded retrieval

Semantic similarity answers “what looks like this?” but not “what caused this?”
When an agent debugs a system failure, the relevant memory may be temporally distant and semantically dissimilar to the current error message yet causally upstream.
Hybrid retrievers blending semantic similarity, temporal ordering, causal graph traversal, and counterfactual relevance remain largely unexplored.
Building them will require integrating causal discovery techniques with memory indexing—technically challenging but potentially transformative for complex reasoning tasks.

A concrete starting point would be to augment the standard vector index with a lightweight causal metadata layer.
When storing a memory record, the agent could annotate it with an estimated *causal parent*—the earlier record or event that precipitated it.
At retrieval time, the system would traverse these causal links alongside the standard similarity search, surfacing records that are semantically distant but causally relevant.
Such a system need not perform full causal inference; even approximate causal annotations, generated by the LLM at write time, could substantially improve retrieval for reasoning-heavy tasks like root cause analysis, counterfactual planning, and multi-step debugging.

### 9.3 Trustworthy reflection

Self-reflection is a powerful adaptation mechanism that can also entrench mistakes.
If the agent falsely concludes that “approach $A$ always fails,” it will never test approach $A$ again—a classic confirmation bias.
Future systems need external validation (check reflections against ground truth when available), uncertainty quantification (decay confidence over time without confirming evidence), adversarial probing (periodically challenge stored beliefs with counterexamples), and expiration policies (retire unvalidated reflections after a set period).

### 9.4 Learning to forget

Forgetting is not a bug; it is a feature—essential for robustness, privacy, and efficiency.
Yet current systems handle it crudely: hard time-based expiration, storage-limit eviction, or nothing at all.
The research problem is to learn *selective* forgetting policies that maximize long-term utility under safety and compliance constraints.
Connections to machine unlearning  are critical when memories have influenced model behavior through in-context learning or fine-tuning.

### 9.5 Multimodal and embodied memory

As agents move into robotics and mixed-reality, memory must fuse text, vision, audio, proprioception, and tool state.
JARVIS-1  provides an early example in Minecraft, but real-world embodied settings add spatial memory, real-time latency constraints, and the thorny problem of cross-modal retrieval—finding a visual memory via a textual query, or vice versa.

### 9.6 Multi-agent memory governance

Multi-agent systems raise questions that single-agent memory never encounters: access control over shared stores, consensus protocols for concurrent writes, and knowledge transfer mechanisms between agents with different specializations.
Current approaches rely on shared conversation logs or document stores; more sophisticated designs—distributed memory with merge semantics, hierarchical shared memory with per-agent caches—remain wide open.

### 9.7 Toward memory-efficient architectures

Memory-augmented agents are expensive: large context windows, multiple retrieval calls per step, ever-growing stores.
Sparse retrieval (activating a tiny fraction of the store per step), compressed session vectors, memory-native architectures like Recurrent Memory Transformers , and retrieval-free injection via adapters  all point toward cheaper alternatives, though none has yet demonstrated strong agent-level performance.

### 9.8 Deeper neuroscience integration

Current agent memory borrows cognitive science labels; deeper engagement could yield better mechanisms.
Spreading activation —where accessing one memory primes related ones—could improve retrieval beyond direct similarity.
Memory reconsolidation theory—retrieval renders a memory labile and subject to revision—could inform update mechanisms.
Ebbinghaus curves , already used in MemoryBank , could be extended with spaced repetition to optimize reinforcement timing.

### 9.9 Foundation models for memory management

A longer-term vision: a *foundation model for memory control*, trained across diverse agent tasks to perform write, retrieve, summarize, forget, and consolidate operations with general competence—much as instruction-tuned LLMs  provide general language capabilities.
AgeMem  takes a first step by learning memory management as a policy, but the vision of a truly task-agnostic memory controller remains unrealized.

Such a foundation model would need to handle a diverse distribution of memory challenges: short-term conversational tracking, long-term user profiling, high-frequency tool-use logging, rare but safety-critical information retention, and graceful degradation when storage budgets are exhausted.
The training data requirements are daunting—the model would need exposure to thousands of agent trajectories across dozens of domains, with ground-truth labels for memory operation quality.
Generating this training data synthetically, perhaps by having advanced LLMs retrospectively annotate which memory operations in historical traces were helpful or harmful, could bootstrap the process.

### 9.10 Standardized evaluation

The field still lacks a community-standard evaluation harness.
Each benchmark uses its own datasets, metrics, and protocols, making cross-paper comparison unreliable.
A GLUE-style shared leaderboard for agent memory—spanning conversational, agentic, and multi-session tracks, with standardized metrics from our four-layer stack—would substantially accelerate progress and reduce duplicated effort.

## 10 Conclusion

Memory has moved from a peripheral add-on to the central engineering and research challenge for LLM-based agents.
The field has traversed three generations in rapid succession: prompt-level compression, retrieval-augmented external stores, and end-to-end learned memory policies.
Evaluation has evolved in tandem—from static recall tests to multi-session agentic benchmarks that expose the gap between remembering a fact and actually using it.

This survey has offered a POMDP-grounded formalization, a three-axis taxonomy, a deep dive into five mechanism families, a structured benchmark comparison, an application-level analysis, and a practical engineering playbook.
But the hardest problems remain ahead: how to consolidate without catastrophic loss, how to retrieve by cause rather than similarity, how to reflect without entrenching errors, and how to forget safely.
Solving these will determine whether the next generation of agents is merely impressive or genuinely reliable.

If there is one takeaway from this survey, it is that memory deserves the same level of engineering investment as the LLM itself.
Model selection gets months of careful benchmarking; memory architecture often gets an afternoon.
The evidence reviewed here suggests that flipping this priority—treating memory as a first-class system component worthy of dedicated design, testing, and optimization—may be the single highest-leverage intervention available to agent builders today.

## Acknowledgments

This manuscript targets *Advanced Intelligent Systems*.
Author, funding, and ethics metadata should be finalized before submission.

## Conflict of Interest

The authors declare no conflict of interest.

## Data Availability Statement

No primary data were generated in this study.
All referenced works are publicly available as cited.

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="position-episodic-memory-is-the-missing-piece-for-long-term-.md">
Phase: [EXPLOITATION]

## Abstract

Abstract As Large Language Models (LLMs) evolve from text-completion tools into fully fledged agents operating in dynamic environments, they must address the challenge of continuous learning and long-term knowledge retention. Many biological systems solve these challenges with episodic memory, which supports single-shot learning of instance-specific contexts. Inspired by this, we present a framework for LLM agents, centered around five key properties of episodic memory that underlie adaptive and context-sensitive behavior. With various research efforts already covering portions of these properties, this position paper argues that now is the right time for an explicit, integrated focus on episodic memory to catalyze the development of long-term agents. To this end, we outline a roadmap that unites several research directions under the goal to support all five properties of episodic memory for more efficient long-term LLM agents.

## 1 Introduction

Large Language Models (LLMs) are rapidly expanding beyond their origins as text-completion engines. Instead, they are evolving into agentic systems capable of taking meaningful actions in complex environments . This transformation can enable a range of real-world applications, including autonomous research assistance , aiding in literature reviews, data analysis, and hypothesis generation; personalized customer support , where they can recall prior interactions to provide consistent and tailored assistance; and interactive tutoring systems , which track learning progress, and revisit challenging concepts to ensure effective and personalized education.
These diverse applications hint at a vast potential of LLMs to enable intelligent agents capable of meaningful and context-sensitive interaction.

Operating and reasoning over extended timescales in dynamic interactive contexts demands that an agent not only recalls what happened, but also when, how, why, and involving whom. Such rich traces of past events, motivations, and outcomes form the basis of context-sensitive behavior—especially crucial in large-scale projects involving human stakeholders and multiple actors. For example, a future long-term LLM agent that is supposed to assist in the ongoing development of a massive software project such as Linux—which has spanned decades, encompasses over 40 million lines of code, and additionally involves countless past contributions, issues, comments, notes, and feature requests—would need to continuously integrate and reason about a vast, evolving historical context while adapting to new requirements.
Core necessities for this kind of system are constant computational cost per new token and a stable or improving performance over time.

Ongoing research directions attack the problem of long-term retention and adaptation from different angles and have made impressive progress.
However, we are still lacking approaches that maintain relevant contextualized information over long time frames at a constant cost without degrading performance—necessities for a widespread adoption of LLM agents in many long-term settings.

Meanwhile, many biological systems solve the demands for acting in a continually evolving environment with a dedicated memory system that allows for both fast and slow learning: episodic memory . In this position paper, we argue that the growing demand for LLM agents to operate effectively over extended timescales, alongside ongoing advances in long-context models, external memory systems, and efficient fine-tuning methods, makes episodic memory a timely framework to unify efforts for enabling truly long-term LLM agents.

Figure: Figure 1: LLM-Agents with an Episodic Memory system. The LLM agent acts on and gets feedback from an environment. Feedback can come in the form of outputs from programs (E1), from other agents (E2), humans (E3), as well as external real-world data (E4). Actions can modify parts of the environment, and provide feedback for humans or other agents in the environment. Within the agent, an external memory system acts as a bridge between parametric and in-context memory while allowing for fast *encoding* of and *retrieval* into in-context memory (the LLM’s context window). (a) *Consolidation*: Episodes in the external memory are consolidated into a model’s broader parametric memory to avoid capacity limitations and allow for generalization to new semantic knowledge and procedural skills based on specific instances. (b) *Encoding*: Limited in-context memory can offload its content into external memory. (c) *Retrieval*: Stored episodes can later be retrieved and used to reinstate representations into in-context memory.
Refer to caption: x1.png

To lay out the argument for this position, we proceed as follows: In Section 2, we operationalize the concept of episodic memory for LLM agents by highlighting five key properties that distinguish it from other biological types of memory that are also desirable for LLM agents. We proceed to argue in Section 3 for episodic memory as a unifying goal by showing how various existing approaches to improve LLM memory target different properties that are united in episodic memory. In Section 4, we highlight how unifying these threads under a common goal can spur more holistic progress and outline a roadmap toward implementing episodic memory. Lastly, in Section 5, we discuss alternative views under which episodic memory would not be necessary for long-term LLM agents.

## 2 Operationalizing EM for LLMs

To transfer the concept of episodic memory from cognitive science to the context of LLM agents, we highlight five properties of episodic memory that are useful for LLM agents, and that distinguish episodic memory from other memory types in animals and humans. These five properties naturally cluster into two categories: properties that concern the way that the system operates with the memory—namely, long-term storage, explicit reasoning, and single-shot learning, and properties that concern the content of the stored memory—namely, instance-specific and contextualized memories. We first discuss how the combination of these five properties distinguishes episodic memory from other types of memories in animals and humans, and then detail each property and its utility for LLM agents.

### 2.1 Unique Combination of EM Properties

Episodic memory is one of multiple memory systems that exist in animals and humans, distinguished by its unique combination of properties (Table 1). Other biological memory systems that share some, but not all, properties of episodic memory are 1) procedural memory , which allows for long-term storage of memories for implicit operations or task behaviors, such as producing a sequence of a particular type, rather than reasoning about the sequence; 2) semantic memory , which allows for long-term storage of factual knowledge and explicit reasoning with these stored memories, but lacks specificity to single instances of acquired information and its context; and 3) working memory , which can share many of the highlighted properties of episodic memory except for the important fact that it does not allow for long-term storage. The unique combination of important properties in episodic memory makes it a promising candidate for translation to AI systems.

### 2.2 Importance of EM Properties for LLM Agents

**Table 1: Properties of episodic memory in comparison to other relevant forms of memory in animals and humans.**
| Memory Type | Long-term | Explicit | Single-shot | Instance-specific | Contextual  relations |
| --- | --- | --- | --- | --- | --- |
| Episodic | ✓ | ✓ | ✓ | ✓ | ✓ |
| Procedural | ✓ | $\times$ | $\times$ | $\times$ | $\times$ |
| Semantic | ✓ | ✓ | $\times$ | $\times$ | $\times$ |
| Working | $\times$ | ✓ | ✓ | ✓ | ✓ |

#### 2.2.1 Episodic Memory Operations

Long-term storage.
In humans and other animals, episodic memory functions as a form of long-term memory, capable of storing knowledge throughout an individual’s lifetime . This distinguishes it from working memory, which is transient. For LLM agents, an effective episodic memory system must similarly support memory retrieval across any number of tokens. This requires mechanisms for long-term memory that maintain an agent’s performance throughout a continual interaction with an environment. An adaptive long-term agent should not only prevent a degradation in performance over time-it should also be able to improve by learning new general knowledge and skills.

Explicit reasoning.
In classical theories of human memory, episodic memory is described as a subset of declarative or explicit memory . A defining feature of explicit memory is the ability to reflect and reason about the memory content. In the context of LLM agents, the explicitness of memory is necessary as agents need to be able to answer direct queries about stored information or use this information in explicit internal reasoning processes.

Single-shot learning.
A key characteristic of episodic memory, as emphasized in complementary learning systems theory, is its ability to be acquired based on a single exposure . This fast learning enables the rapid encoding of unique experiences or events. For LLM agents, this capability is particularly crucial in environments where continual deployment may not provide multiple variations or repetitions of specific events. Certain occurrences in an environment may happen only once, necessitating an episodic memory system that is capable of effectively capturing and utilizing information from single exposures.

#### 2.2.2 Episodic Memory Content

Instance-specific memories.
Episodic memory stores information specific to an individual sequence of events along with their distinct temporal contexts . This specificity allows episodic memory to capture details unique to a particular occurrence, enabling its application in agentic environments where reasoning about specific past actions and their consequences matters. This can include past lines of reasoning that were associated with a decision to be made by an LLM agent.

Contextual memories. Episodic memory binds context to its memory content, such as when, where, and why an event was encountered . The ability to store many contextual relations associated with a specific event enables retrieval based on contextual cues as well as explicit recall of context. For LLM agents, this property is important to not only remember that a specific event happened in the past, but also when, why, and in which broader context it happened.

## 3 Current Approaches

While many methods currently exist to modify and augment LLM memory, we argue that they fall short of the memory properties that would enable effective, long-term LLM agents. We group existing methods that seek to improve the memory of LLMs into three categories that are relevant to episodic memory:

- 1.
In-Context Memory methods extend the effective context length by optimizing computational efficiency and length generalization;
- 2.
External Memory methods augment a model’s in-context memory capacity with a separate module, often with reduced GPU memory requirements and/or computational cost;
- 3.
Parametric Memory methods modify the LLM parameters that encode memories (primarily learned from the language modeling training data).

In this section, we discuss examples in each category that capture different properties of episodic memory (Table 2). More importantly, we highlight their shortcomings in supporting episodic memory for LLM agents in isolation.

**Table 2: Methods for in-context, external, and parametric memory do not cover all features of episodic memory. $\sim$ is used for cases where it is unclear whether an aspect of episodic memory is properly satisfied by a method.**
| Memory Approach | Long-term | Explicit | Single-shot | Inst.-specific | Contextual rel. |  |
| --- | --- | --- | --- | --- | --- | --- |
| In-Context | KV-Compression | $\times$ | ✓ | ✓ | ✓ | ✓ |
| State-space-model | $\times$ | ✓ | ✓ | ✓ | ✓ |  |
| External | RAG | ✓ | ✓ | $\sim$ | $\sim$ | $\times$ |
| GraphRAG | ✓ | ✓ | $\sim$ | $\sim$ | $\sim$ |  |
| Parametric | Efficient Fine-tuning | ✓ | ✓ | $\times$ | $\times$ | $\times$ |
| Knowledge Editing | ✓ | $\sim$ | $\times$ | $\sim$ | $\times$ |  |
| Context Distillation | ✓ | ✓ | $\times$ | ✓ | $\times$ |  |

### 3.1 In-Context Memory

In-context memory (ICM) allows LLMs to perform single-shot, instance-specific, and contextualized learning by enabling them to directly attend to representations of encountered sequences (Table 2). ICM capacity is either tightly limited or extensible but expensive to scale, often requiring sequence parallelization. Recent works seek to extend it by increasing the context window, but models struggle with length generalization beyond training exposures. We review existing methods and their limitations in addressing these challenges.

One active research direction focuses on extending the in-context window to handle significantly longer sequences, enabling LLMs to perform reasoning over extended contexts. This advancement brings LLMs closer to mimicking episodic memory, as it allows models to retain and utilize information across longer contexts. However, transformer-based LLMs face significant challenges, including the high computational cost of processing long sequences and limitations in length generalization.
Recent research has sought to address these challenges by reducing memory usage, optimizing inference time, and improving long-sequence generation. Despite these advancements, current methods have yet to achieve robust, persistent memory capabilities necessary for long-term, open-ended, and context-aware reasoning. Below, we briefly review existing methods and their limitations.

Memory reduction.
For transformer-based LLMs, several methods aim to reduce memory and computation costs.

Sparsification and compression methods selectively retain relevant information to optimize memory usage. Sparsification strategies optimize memory by restricting attention computations to the most relevant parts of the sequence , reducing both storage and computational overhead. Similarly, forgetting mechanisms remove less useful tokens to maintain efficiency . Other compression-based approaches dynamically reduce KV cache size by storing only the most important tokens and key-value pairs . Adaptive strategies further refine compression across layers  or merge similar states to minimize redundancy .

Quantization methods reduce memory footprints by lowering precision or selectively storing information. Quantization techniques store key-value pairs at reduced precision , allowing for larger context windows with a relatively minimal performance degradation.

Inference time reduction.
Efficiency improvements during inference focus on optimizing KV cache management and parallelization. Techniques such as paged caching  dynamically allocate memory to accommodate longer sequences without excessive overhead. Other methods leverage GPU memory pooling and adaptive chunking  to process extended contexts efficiently while maintaining fast retrieval and computation speeds.
Other strategies improve efficiency by reusing KV tensors across layers

Recent work has aimed to introduce episodic memory in LLMs by structuring token sequences into retrievable events , enhancing long-context reasoning and outperforming retrieval-based models. However, a fundamental challenge remain the increasing memory and retrieval costs: maintaining the full KV-Cache for an entire interaction history can quickly become impractical, especially in large-scale, long-duration, and multimodal applications. This limitation is inherent to KV-Cache management systems, which must retain the entire cache, leading to significant storage and computational overhead.

Transformer alternatives to reduce both memory and inference time.
In addition to optimizing KV cache storage and management, alternative architectures have been proposed to address the limitations of standard transformers in both memory and inference time.

Linear attention  approximates full self-attention using kernel-based or low-rank transformations, significantly reducing computational complexity and improving efficiency for long-sequence processing.
State-space models (SSMs)  further achieve linear scaling for sequence handling by maintaining a fixed-size representation, making them inherently memory-efficient. Hybrid architectures  combine these techniques with transformers to compress KV-cache sizes while preserving strong performance.
Other alternatives restructure the transformer architecture itself to enhance efficiency. Some models  modify the decoder structure to reduce memory usage and latency, while others  compress sequence information into compact representations to improve inference speed and scalability.

These methods enhance ICM efficiency, but their reliance on compression, approximation, and selective retention comes with limited support for long-term reasoning with episodic memory. This limitation highlights the need for an external memory structure that retains past information. Methods of KV-cache optimization can also discard older context, leading to irreversible information loss and different model behavior .
Generally, methods with a constant cost, like SSMs, struggle to handle a continually expanding interaction history in dynamic environments, while methods with an increasing state representation increase in both inference time and GPU memory requirements.

Length Generalization.
Length generalization refers to a model’s ability to maintain understanding over long sequences, preventing degradation of performance such as forgetting or losing context midway through processing . In essence, humans avoid SSMs’ trade-offs by storing compressed representations and retrieving knowledge adaptively, allowing us to manage expanding information effortlessly.

To address this, lightweight solutions  create adapters to process and retrieve long inputs before passing the content to the LLM.
Other approaches  refine attention patterns and positional encodings to enhance long-context comprehension.
Alternative architectures  improve long-context learning through mechanisms like differential attention and segment-level recurrence.
Another promising approach embeds test-time information into the model’s parameters, creating a form of long-term memory , combining attention with neural memory modules, enabling adaptability for long contexts but at the cost of increased inference overhead. These approaches have limited capacity and still face eventual forgetting over very long sequences.

### 3.2 External Memory

Many methods propose a separate memory module that stores information when it exceeds the effective operating span of the model. These augmented memory models are usually evaluated on tasks which require using that stored information. As such, these methods typically have long-term and explicit memory (Table 2). However, they often lack information that relates the stored memories to one another—especially contextual details on how the model acquired the memory, or details to help differentiate specific instances. They are typically not evaluated for single-shot learning, especially for specific instances. And finally, there is a lack of proposals to generalize information from these instances and update parametric memory (Figure 1a). Below we review some relevant external memory methods and elaborate on key examples to illustrate these shortcomings.

Slot-based memory with recurrent controllers. A key advance in memory augmentation in the pre-transformer era was the formulation of learnable memory modules external to the main neural network . External memories were stored in individual slots and updated via a recurrent memory controller. These models were shown to retain longer-term information than vanilla long-short term memory (LSTM) networks. Similar memory augmentation methods have been adapted for transformers . However, these methods lack a way to store contextual details that LLM agents would need in an episodic memory, as they strongly depend on the details available in the input data. One exception devised a method to record temporal relationships between memories , but this has yet to be seen in augmented LLMs.

Distributed vs. slot memory. An issue with slot-based memory modules is that they are capacity-limited, both by the number of slots and the dimensionality of each slot representation. While these models adopt forgetting mechanisms to mitigate this, the capacity limit still affects how long memories can be stored. Another approach addresses this downside by storing external memories in a sparse, distributed fashion instead of in slots. Recent work integrated distributed memory in an LLM, and showed that the model can recall a greater number of facts over longer contexts, compared to baseline LLMs. While they demonstrate how they can perform one-shot memory updates (fact-editing), they do not evaluate single-shot learning of novel facts.

RAG and GraphRAG methods. Retrieval Augmented Generation (RAG) methods maintain an external database of information that is added to the input data to augment LLM generation. Naive RAG implementations encode chunks of text using embedding models , typically without much metadata or contextual detail about the original text. (One exception is work that preserves the order of retrieved text from the database .) And while text embedding models can capture some similarity relationships between embeddings, they do not encompass the rich set of relationships that LLM agents will likely need for most applications. GraphRAG models replace the vector embedding database with a structured graph that explicitly encodes relationships as connections between nodes . Still, these graphs encode a limited number of relationship types, even when researchers branch out beyond pre-existing datasets and learn to build the graphs directly from the input text . As such, they also lack rich contextual detail.

External storage of past LLM inputs and outputs. Another type of approach maintains a database of pasts LLM inputs to avoid recomputing predictions to similar future inputs . Here, contextual information (e.g. details that differentiate specific instances) will only be stored when explicitly given in the LLM input text. That is, the memory is much more dependent on input data, limiting test-time generalization. One proposal to mitigate this formulates a long-term memory module for context that is updated with LLM activations based on the current inputs . Other approaches additionally store LLM outputs, such as generated text , summarizations , chain-of-thought steps , and extracted relation triples . One approach specialized for chat interactions stores timestamps and user personality profiles as context . These modifications enable storage of contextual details useful for LLM agents. However, specifying the type of contextual detail is restrictive, so it is preferable to combine this with a more learnable and flexible mechanism for storing context.

Learning to interact with external memory. The approaches described above may fine-tune or instruct the LLM to interact with and update external memory. That is, the LLM learns the functions of a memory controller. For example, several RAG approaches fine-tune the LLM to make better use of the retrieved content . Other approaches define how LLMs should interact with memory, requiring them to learn specific API calls or memory hierarchies . These provide possible mechanisms to add information to external memory, such as contextual details and specific instances. However, most current work does not consider how to modify the LLM to generalize across specific instances to store new knowledge in LLM parameters (Figure 1a). propose one way to generalize across instances by adding a data-independent memory system (a.k.a. meta-memory, persistent memory) in addition to a more data-dependent memory module. However, the data-independent memory is considered to be closer to task memory than knowledge distillation, and the meta-memory parameters are kept separate from the LLM itself.

### 3.3 Parametric Memory

This type of memory allows LLMs to process the information in the input to obtain well-suited output. Parametric memory values are initially learned through back-propagation with a pretraining dataset.
During this process, the parametric memory tends to capture general knowledge and rules ranging from syntax to common sense and factual knowledge.
Due to the sheer size of the parametric memory, the amount of data needed for pre-training is usually very large, following power laws .
Generally, parametric memory is fixed after training, i.e., does not change with the input at inference time.

A relevant research direction in parametric memory focuses on adapting LLM parameters to specific domains, tasks, or applications when given limited resources. Efficient fine-tuning methods have been developed in recent years to tackle the runtime and memory consumption of this process. Alternatively, distillation techniques have been proposed to update knowledge and propagate it through a model. A key challenge is the need for updating specific factual knowledge without interfering with other knowledge. Some facts may change over time, requiring surgical precision to update the parameters of a model. The line of work that proposes these updates is known as knowledge editing.

Efficient Fine-tuning. Various works have been proposed to reduce the computational needs (hardware memory) of updating a model to a specific domain. Among these, Low-Rank Adaptation (LoRA) applies additive low-rank approximation updates to shift the model parameters.
Several methods proposed other ways to further improve efficiency by reducing and localizing updates . Other work learned modifications on representations instead of parameters .
In all cases, fine-tuning methods require a dataset to adapt a model for a specific task or domain, i.e. they are not capable of single-shot learning or capturing instance-specific and contextually rich information.
On the other hand, additional fine-tuned adapter parameters are often frozen after the fine-tuning process, supporting the long term storage of information. Moreover, these methods tend to preserve the reasoning capabilities while updating the model with newly captured information .

Knowledge Editing. As the environment evolves over time, some factual knowledge becomes outdated (e.g., the president of a country may change after the elections). Knowledge editing methods aim to make modifications to the factual knowledge in parametric memory with targeted updates while avoiding interference with other facts. In ROME and MEM-IT , the first step is to find relevant parameters (in MLPs) that influence the specific fact through causal interventions and then update the related parameters with low-rank model edits. An alternative research direction proposes to train a hyper-network that predicts the amount of change for each parameter given the knowledge to be edited. A different method, SERAC, stores the set of edits in an external memory, combined with a scope detector and a counter-factual model to decide when and how to apply the edits. All knowledge editing methods work on facts which are inherently context-free, making it impossible to contextualize the edited knowledge in the history of the agent-environment interaction. However, they mimic the episodic memory traits of learning from a single instance, while enabling long-term retention.

The problem of knowledge editing has been extended to a continual learning setting, where edits are required sequentially over time to correct a model. This leads to the sequential editing problem: hyper-network prediction quality decreases because they fail to reflect the updated model, and low-rank parameter updates interfere with one another causing catastrophic forgetting .
MELO adapts dynamic LoRA to this problem and introduces a vector database to search the selections of the blocks to be dynamically activated within the LoRA matrices for each layer. WISE adds duplicates of the MLP’s output parameters for some layers in the network, and updates them with each new edit set. A routing mechanism decides whether to use the original layer or the updated one. It further uses sharding and merging to distribute the edits into random subspaces to improve generalization and parameter utilization.

While continual learning-based knowledge editing allows models to integrate updates over time, it has fundamental limitations. Edited knowledge often lacks generalization, struggling with inferring new relationships or reasoning over multiple steps . This highlights a key challenge—knowledge editing methods can introduce updates but do not always ensure deeper understanding or adaptability.

Context Distillation. The idea behind these techniques is to transfer in-context learned information, abilities, and task-understanding by distilling them into model parameters.
proposed to use distillation when the teacher and the student are in the same model, but less in-context information is given to the student. This would enable the student to learn skills and express knowledge that would otherwise depend on including information and instances in costly and limited in-context memory. Further, proposes to exploit context distillation to inject and propagate knowledge through a model. The original model is provided with new definitions and continuations. The distillation process updates a copy of the model with only the generated continuation, conditioning the updated model to the new entities implicitly. This helps to propagate the information into the parameters (i.e., consolidating it) and thus improving inference with such entities.

## 4 Episodic Memory as a Unifying Framework

Although current work has advanced context-sensitive LLMs that are capable of handling longer sequences, it does not yet deliver efficient learning that could support long-term LLM agents. Existing methods—which extend in-context (working) memory, integrate external memory, or update parametric memory—only address subsets of episodic memory’s five essential properties, as discussed in Section 3. These approaches remain fragmented, impeding the immediate assimilation of new experiences and gradual improvement over time.

We propose that enabling episodic memory offers a unifying perspective that will combine and extend existing methods to advance the capabilities of LLM agents. By incorporating long in-context memory, external memory, and mechanisms for updating parametric memory, agents can more seamlessly adapt to new information, consolidate it, and prevent escalating costs or performance degradation during extended interactions with an environment. This view is based on Complementary Learning Systems Theory , in which episodic memory is part of a fast-learning system that stores information from individual instances. Over time, that information is consolidated into a slow-learning system that stores more stable, durable knowledge.

In Figure 1, we present a general architecture and framework that combines these elements under the overarching goal of enabling all five key features of episodic memory for LLM agents as detailed in Section 2. As a roadmap to enable episodic memory in LLM agents, we specifically call for four main research directions (encoding, retrieval, consolidation, and benchmarks), and formulate six research questions under these areas below.

### 4.1 Encoding

RQ1: *How to store information from in-context memory in a long-term external memory store?*

An external memory store is essential for retaining experience in a structured way that preserves the context of individual instances (Fig.1, arrow (b)). A straightforward approach is to store text chunks or embeddings in a non-parametric RAG-like database, potentially augmented with metadata for context . More structured representations, such as GraphRAG, could also facilitate context-sensitive retrieval. However, capacity constraints on these types of databases may make it necessary to rely on more compressed parametric representations.

RQ2: *How to segment continuous input into discrete episodes, and when to store them in an external memory?*

A major design question is *when and how to segment* a continuous stream of agent experience into episodes to be encoded into an external memory. LLMs have already been shown to be capable of segmenting text into meaningful events, in a way that is similar to humans , and recent approaches show that further bundling related segments based on model surprise can improve long-term modeling .

*Leveraging long-context advances* can further improve encoding by providing a space in which new episodes can be equipped with a rich contextualization. Large hidden states or extended attention windows help capture high-fidelity contextual information, which can then be encoded into an external memory in a compressed format for future retrieval.

### 4.2 Retrieval

RQ3: *Given an external memory, how to select relevant past episodes for retrieval and reinstatement into in-context memory for the purpose of explicit reasoning?*

To employ past experiences in current tasks, an agent must *retrieve* relevant episodes at the right time and *reintegrate* them into its in-context memory with an adequate mechanism (Fig.1, arrow (c)). Common strategies include prepending retrieved text tokens to the input sequence (as in RAG), manipulating representational states within the transformer (e.g., memory tokens ), or adapting internal representations .

RQ4: *How can retrieval mechanisms in long-context LLMs improve and accelerate the optimization of external memory retrieval and reinstatement?*

*Long-context advances* can be leveraged to inform when and what to retrieve at sequence lengths that are still feasible. Future research could explore tight integration of external memory with the model’s forward pass and adopt cross-architecture distillation to accelerate the development of external memory structures that retain many of the desirable properties of in-context memory while reducing the resource cost.

### 4.3 Consolidation

RQ5: *How to periodically consolidate external memory contents into the LLM’s base parameters without forgetting previous knowledge?*

Eventually, merging external memory contents into the model’s parameters (Fig.1, arrow (a)) promises to allow new generalized knowledge to be used without explicit retrieval. This process both prevents external memory overflow and supports continuous adaptation of the agent’s semantic and procedural backbone to the environment. Relevant techniques include context distillation, parametric knowledge editing, and localized fine-tuning methods that capture newly encountered information without catastrophic interference with other knowledge. Open questions remain about how to decide when to consolidate and how to compress many episodic instances into more abstract parametric knowledge while also retaining previous knowledge and skills.

### 4.4 Benchmarks

RQ6: *What new types of benchmarks are needed to assess episodic memory in LLM agents?*

Finally, *evaluating* episodic memory effectiveness requires new tasks and metrics. Studies should test the recall of contextualized events after long delays, assessing how well agents remember when, where, and how events occurred. An example of such a study is the testing of instance-specific temporal order memory proposed by . Beyond controlled probes, benchmarks must incorporate real-world complexities: agents should demonstrate an improving task performance that is linked to encoding, retrieval, and consolidation of past experiences over extended timescales.

## 5 Alternative Views

While we argue that an explicit episodic memory framework is necessary for effective long-term and context-sensitive behavior, there are alternative perspectives suggesting that current or emerging methods might suffice in the future without the need for the concept of episodic memory to provide guidance.

Scaling in-context memory will be sufficient. One view suggests that advances in long-context methods—such as improved transformers, state-space models, or other architectures with extended context windows—will enable practically unlimited access to past information. Proponents claim that better positional encodings, modified attention mechanisms, and other in-context memory extensions will cover most relevant applications for LLM-based agents.

Contextualized external memory will be sufficient.
A second view holds that external memory structures—such as knowledge graphs or retrieval-augmented generation (RAG) systems—could eliminate the need for an episodic memory framework. By contextualizing data chunks and storing them in structured graphs, these systems aim to incorporate past context into current tasks effectively.

“Infinite” in-context memory remains a speculative prospect. Extending limited context windows to include all information needed by an agent requires foreknowledge of the maximum timespan of relevant information. For very long timespans, this will either incur prohibitive computational costs or require compression methods that may lose key details. Only relying on external memory will still incur high storage costs, and require forgetting mechanisms. An episodic memory framework addresses these constraints by periodically consolidating information into high-capacity parametric memory (Figure 1, arrow (a)). This has the added benefit of enabling LLM agents to slowly improve over time, as they continue to learn from the past before they forget it.

## 6 Conclusion

This position paper argues that to fully realize efficient long-term LLM agents, we must endow LLM agents with episodic memory. We operationalize episodic memory—a term borrowed from cognitive science—for LLMs by highlighting five key characteristics that distinguish episodic memory from other types of memory in biological systems, and argue for why each property is also important for LLM agents. We position the call for episodic memory in LLM agents in the current literature and discuss how episodic memory can serve as a unifying goal for existing research directions. Lastly, we provide a roadmap of research questions towards implementing episodic memory in LLMs. By describing the potential of this research direction, we aim to spark a community-wide shift in how we conceive and engineer long-term memory in the move towards agentic AI—one that more deeply integrates lessons from cognitive science and brings together existing approaches in ML under a unifying goal with strong promise.

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="vector-database-vs-knowledge-graph-for-ai-agent-memory.md">
Phase: [EXPLOITATION]

## Vector database vs knowledge graph vs governed metadata graph: at a glance

| Dimension | Vector Database | Knowledge Graph |
| --- | --- | --- |
| What it is | Embedding index for semantic similarity search | Graph of typed entity relationships and traversal |
| Primary retrieval method | Approximate nearest-neighbor (ANN) on vector embeddings | Cypher/SPARQL graph traversal; multi-hop path following |
| Best for | Fuzzy recall of unstructured content; conversational grounding | Multi-hop relational reasoning; explicit ontology queries |
| Key strength | Sub-millisecond retrieval; zero cold-start; any content type | Explicit relationships; deterministic paths; temporal edges |
| Key weakness | Flat semantics; no multi-hop; no governance primitives | Cold-start cost; ontology maintenance burden |
| Hallucination risk | High: stale vectors produce fluent but incorrect answers | Lower: deterministic traversal; explicit relationships |
| Representative tools | Pinecone, Weaviate, pgvector, Qdrant, ChromaDB | Neo4j, Amazon Neptune, FalkorDB, Zep/Graphiti |

## How vector databases work for AI agent memory

Vector databases store content as high-dimensional embeddings, numerical representations of semantic meaning. When an agent needs to recall a fact, it embeds the query and runs approximate nearest-neighbor search against the index. Tools like Pinecone, Weaviate, and pgvector dominate production deployments because of their zero cold-start, sub-millisecond retrieval, and compatibility with any unstructured data type.

### How the Retrieval Mechanics Work

Content (conversations, documents, code, structured fields) is passed through an embedding model (such as `text-embedding-3-small`) to produce a high-dimensional float vector. Vectors are stored in an HNSW or IVFPQ index; both trade exact accuracy for retrieval speed.

At query time, the agent embeds the query, runs ANN search to return the K most similar vectors, then injects retrieved chunks into the LLM context window. There is no explicit entity model: “revenue” and “ARR” are similar vectors, not the same node.

### Where Vector Databases Excel

**Zero cold-start.** The system is useful the moment you embed content. No ontology engineering, no extraction pipelines, no waiting.

**Sub-millisecond retrieval at scale.** ANN is extremely fast. Pinecone, Weaviate, and Qdrant handle billions of vectors in production without meaningful latency degradation.

**Universal content type.** Text, images, audio, code, and tabular data all embed into the same vector space. A single index handles heterogeneous content.

**Low infrastructure overhead.** Managed cloud services like Pinecone and Weaviate Cloud require minimal ops work. Teams ship production-ready retrieval in days, not months.

**Conversational grounding.** Vector memory excels at episode recall: surfacing what a user asked last week, finding related conversations, grounding a response in recent interaction history.

### Where Vector Databases Fall Short

**Flat semantics.** There is no relational model. Two related concepts are similar vectors, not linked nodes. Multi-hop traversal (“what pipelines derive from this certified dataset, and who owns each one?”) is structurally impossible.

**No temporal model.** Stale and fresh vectors coexist silently. ANN has no concept of “what was true at time T.” Systems produce fluent answers on outdated data with no staleness signal.

**Invisible freshness failures.** VentureBeat (2025) documents how enterprises measure the wrong part of RAG: “freshness failures emerge when source systems change continuously while embedding pipelines update asynchronously.” The agent keeps answering, fluently and incorrectly.

**Opaque retrieval.** Similarity scores cannot explain why a fact was retrieved.

## How knowledge graphs work for AI agent memory

Knowledge graphs model the world as typed nodes and edges: entities connected by explicit, named relationships. Agents traverse these graphs using languages like Cypher (Neo4j) or SPARQL, following relationship chains that vector search cannot infer. Temporal knowledge graphs like Zep/Graphiti extend this with validity intervals on every edge, achieving 18.5% higher accuracy on temporal reasoning tasks over baseline implementations.

### How Graph Traversal Works

Entities (people, datasets, concepts, events) are modeled as nodes. Relationships between them are typed, directed edges: “governs,” “transforms,” “owns,” “derived_from.” Agents query via graph traversal using Cypher in Neo4j, SPARQL in RDF stores, or Gremlin in Amazon Neptune.

Multi-hop queries explicitly follow chains: `Customer -> Contract -> Product -> Team -> Owner`. Microsoft GraphRAG extracts a knowledge graph from a text corpus, builds a community hierarchy and summaries, and enables both local (entity-level) and global (dataset-wide) queries.

Temporal knowledge graphs go further. Zep/Graphiti’s bi-temporal model attaches validity intervals (`t_valid`, `t_invalid`) to every edge. Facts are invalidated, not deleted, giving agents full time-travel support.

### Where Knowledge Graphs Excel

**Multi-hop reasoning.** Explicitly traverses entity chains that vector similarity cannot bridge. The difference between “find similar documents” and “follow this relationship chain to the responsible owner” is architectural, not configurable.

**Typed relationships.** Edges carry semantic meaning. “Governs” is structurally different from “references” or “derives_from.” An agent traversing a knowledge graph knows the nature of each relationship it follows.

**Deterministic traversal.** Every answer traces back to specific graph nodes. This explainability matters for regulated industries and complex compliance workflows where a similarity score is not an acceptable explanation.

**Temporal graph support.** Zep/Graphiti’s bi-temporal model achieves 18.5% accuracy improvement on LongMemEval temporal reasoning tasks and 90% response latency reduction versus baseline implementations.

**GraphRAG global queries.** Knowledge graph-based retrieval strongly outperforms standard vector RAG on holistic, dataset-wide questions; standard vector RAG fails entirely on query-focused summarization.

**Measurable accuracy gains.** Knowledge graph augmentation produces 54.2% higher accuracy versus standalone LLMs (Gartner) and reduces hallucination rates by 40%+.

### Where Knowledge Graphs Fall Short

**Cold-start problem.** The graph is empty until populated. Building a knowledge graph from an enterprise data estate is labor-intensive and computationally expensive. Unlike vector databases, knowledge graphs cannot be useful immediately.

**Ontology maintenance burden.** Schema evolution as the business changes requires expert curation. Practitioners on Hacker News consistently note: “the graph is only as good as your ontology, and ontologies are expensive to build and maintain.”

**GraphRAG refresh cost.** LLM-based entity extraction incurs significant GPU costs. Refresh latency limits usefulness with dynamic content. Community variants like LazyGraphRAG and LightRAG exist specifically to reduce extraction overhead.

**Query complexity.** Cypher and SPARQL expertise is required. Most product engineering teams do not have it. This creates a practical barrier to adoption outside specialized domains.

## Hybrid approaches: GraphRAG and what the community has converged on

By early 2026, the practitioner community has largely stopped arguing vector vs. graph and converged on hybrid architectures: vectors for semantic entry-point retrieval, graphs for multi-hop relational depth. Microsoft GraphRAG and Zep’s temporal knowledge graph are the two implementations that have shaped this consensus, each solving a different half of the problem the other misses.

### The Hybrid Pattern

The standard architecture, documented across MachineLearningMastery, Vectorize, Optimum Partners, and Memgraph, follows three steps:

1. **Embed the query.** ANN search retrieves semantically relevant entry nodes from the vector index.
2. **Graph traversal.** Starting from those entry nodes, traversal follows typed relationships for relational depth.
3. **Context assembly.** Combined vector and graph context is injected into the LLM context window.

This pattern captures vector breadth and graph depth simultaneously. A comprehensive survey of 28 Graph RAG integration methods confirms that hybrid approaches consistently achieve better results for complex enterprise use cases than either architecture alone.

### Microsoft GraphRAG

GraphRAG extracts a knowledge graph from a text corpus, builds a community hierarchy, and generates community summaries at each level. It enables two query modes.

**Global Search** handles holistic, dataset-wide questions via community summaries. This is the capability where vector RAG fails entirely. “What are the main themes across this corpus?” returns nothing useful from an ANN index.

**Local Search** handles specific entity queries via graph neighborhood traversal. This is faster but produces answers bounded by what was extracted.

The benchmark evidence is strong: GraphRAG strongly outperforms standard vector RAG on global and holistic questions. The community caveat is equally consistent: high LLM extraction cost, significant GPU overhead, and slow refresh for dynamic content limit practical deployment.

### Zep and Graphiti: Temporal Knowledge Graph

Zep’s Graphiti framework implements a temporal knowledge graph with a bi-temporal model. Every edge carries validity intervals. Facts are invalidated, not deleted, enabling full time-travel queries. A three-tier hierarchy (episode subgraph, semantic entity subgraph, community subgraph) organizes information at the appropriate level of abstraction.

Zep’s benchmark reports 18.5% accuracy improvement on LongMemEval temporal reasoning tasks and 90% response latency reduction versus baseline implementations.

### Neo4j: Native Vector Index Plus Property Graph

Neo4j’s native vector index sits alongside the property graph, enabling hybrid Cypher queries that combine vector similarity with graph traversal in a single query. This is widely adopted in production and requires no separate vector infrastructure.

### Mem0 with an Optional Graph Layer

Mem0 defaults to vector retrieval, with an optional graph tier (Mem0g) for temporal reasoning use cases. Default vector mode scores on LongMemEval; graph mode reaches higher on time-sensitive questions versus OpenAI’s benchmark on the same benchmark.

## Vector database vs knowledge graph vs governed metadata graph: detailed comparison

### Detailed Head-to-Head: 10 Dimensions

| Dimension | Vector Database | Knowledge Graph |
| --- | --- | --- |
| Retrieval model | Approximate nearest-neighbor (semantic similarity) | Deterministic graph traversal (typed relationships) |
| Multi-hop reasoning | Not supported (flat embedding space) | Core capability: explicit relationship chains |
| Freshness model | Async embedding pipeline; stale vectors coexist silently | KG extraction pipeline; invalidation model (Zep) helps at conversation level |
| Cold-start cost | Zero: useful immediately after embedding | High: ontology engineering and entity extraction required |
| Coverage ceiling | Bounded by what has been embedded | Bounded by what has been extracted into the KG |
| Explainability | Similarity score only (opaque) | Explicit reasoning path (auditable) |
| Failure mode | Silent staleness: fluent answers on outdated data | Ontology drift: queries fail or mislead as schema changes |
| Query language | Natural language via vector embed and ANN | Cypher, SPARQL, Gremlin (requires expertise) |

## How to choose: routing matrix for AI agent memory

### Choose Vector Databases When

Your agent needs fast, fuzzy recall of unstructured content: documents, conversations, code. Cold-start speed matters, and you need the agent operational immediately without graph construction overhead. The use case is conversational grounding or episode recall, not complex relational reasoning.

Example agents: customer support bots, personal assistants, document Q&A, code search.

### Choose Knowledge Graphs When

Your agent needs to traverse explicit entity relationships, such as “what contracts reference this product and who owns them?” Deterministic, auditable reasoning paths are required. The domain is well-defined enough to support ontology construction and maintenance. Temporal reasoning is critical; Zep/Graphiti’s invalidation model is the strongest available for conversation-level memory with temporal precision.

Example agents: financial compliance agents, medical knowledge agents, legal document analysis.

### Choose Hybrid Approaches When

You need both broad semantic retrieval and deep relational reasoning. Your corpus is static or semi-static enough to support knowledge graph extraction without prohibitive refresh cost. The domain is document-heavy and global holistic queries matter.

Hybrid options to evaluate: Microsoft GraphRAG, Zep/Graphiti, Neo4j vector index plus property graph.

_Sources: [arXiv 2404.16130](https://arxiv.org/abs/2404.16130) \| [arXiv 2501.13956](https://arxiv.org/abs/2501
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