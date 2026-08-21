# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>How do internal short-term and long-term memory layers interact in agents?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR

Query: How do internal short-term and long-term memory layers interact in agents?

Answer: Every AI agent has 4 distinct memory layers: internal knowledge, context window, short-term memory, and long-term memory. These four layers form a filtering hierarchy. Long-term memory retrieves relevant data. Short-term memory accumulates working state. Context window curates only what matters. Internal knowledge applies general reasoning. For example, if a user asks about Nvidia, retrieve only Nvidia-related facts from long-term memory, not the entire database. If the conversation has run for hours, summarize older turns in short-term memory instead of passing everything verbatim into the context window. This dynamic interplay makes an agent feel coherent. Short-term memory is the working state of the entire agent system across multiple calls, including full conversation history, retrieved documents, tool outputs, structured intermediate results. For each inference step, only a subset of short-term memory is projected into the context window. Short-term memory is the reservoir; the context window is the filtered projection. Long-term memory is external, persistent storage like databases, vector stores, graph stores, file systems, storing user preferences, past interactions, learned facts, saved outputs, giving the agent continuity across sessions. Understanding these layers impacts latency, cost, reliability, and UX in production agentic systems.

-----

Phase: [EXPLOITATION]

### Source [2]: https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/

Query: How do internal short-term and long-term memory layers interact in agents?

Answer: Short-term memory ensures the agent stays informed about its current state and task, handling current conversations or tasks for coherent responses. Long-term memory stores information acquired over time for future use, guaranteeing critical facts and events are not forgotten. These two types complement each other. Long-term memory requires external storage like databases and vector databases since LLM context windows are limited. LangChain and LangGraph integrate with vector databases; CrewAI uses SQLite. Long-term memory operates through retrieval: the agent searches memory when needed and adds retrieved information back into its short-term context. Thus, long-term memory acts as a memory extension system. These memory types coexist and complement each other. For example, a coding assistant uses episodic memory from long-term to remember previous sessions, integrating with short-term for current tasks.

-----

Phase: [EXPLOITATION]

### Source [3]: https://www.moxo.com/blog/agentic-ai-memory

Query: How do internal short-term and long-term memory layers interact in agents?

Answer: Agentic systems need a two-layer memory architecture: short-term working memory and long-term persistent knowledge. Short-term memory is the working buffer holding ephemeral state for the current interaction, effective for real-time reasoning but useless after the session ends. Long-term memory is the knowledge vault with episodic memory (specific events, interactions like client accepted terms on a date) and semantic memory (generalized knowledge, facts, domain rules, client profiles). Short-term handles the current task; long-term stores what needs recall across sessions. Without both, agents fail in production with repetitive interactions and inconsistency. Moxo's architecture preserves history as artifacts linked to processes for continuity.

-----

Phase: [EXPLOITATION]

### Source [4]: https://www.dataiku.com/stories/blog/agent-memory

Query: How do internal short-term and long-term memory layers interact in agents?

Answer: Working memory is active in the current model call (context window), native to LLMs. Short-term memory spans a session or conversation via structured conversation buffer persisting across API calls, summarizing to fit limits, but evaporates post-session. Long-term memory persists across sessions: user facts, past task outcomes, accumulated knowledge, preferences. Everything beyond working memory requires external infrastructure. Short-term provides session continuity; long-term ensures persistence.

-----

Phase: [EXPLOITATION]

### Source [5]: https://towardsai.net/p/machine-learning/long-term-vs-short-term-memory-for-ai-agents-a-practical-guide-without-the-hype

Query: How do internal short-term and long-term memory layers interact in agents?

Answer: Short-term memory (STM/working memory) is ephemeral, session-scoped, in RAM, for active interaction, combining conversational state, execution state, control flow metadata, limited by context window. Long-term memory (LTM) persists across sessions/restarts via databases, vector stores, not injected every request, including chat history, events, embeddings, user preferences. Hybrid memory integrates both for long-range reasoning and experience accumulation: LTM for durability, STM for performance, tool-based retrieval for flexibility. Most issues are poor context selection, not lack of memory.

-----

</details>

<details>
<summary>What are pros and cons of raw strings for storing agent memories?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://www.decodingai.com/p/how-does-memory-for-ai-agents-work

Query: What are pros and cons of raw strings for storing agent memories?

Answer: Storing Memories as Raw Strings is the simplest method. Conversational turns or documents are stored as plain text and indexed for vector search. Pros: It is simple and fast to set up, requiring minimal engineering. It preserves nuance, capturing emotional tone and linguistic cues without loss in translation. Cons: Retrieval is often imprecise. A query like “What is my brother’s job?” might retrieve every conversation mentioning “brother” and “job” without pinpointing the current fact. Updating is difficult; if a user corrects a fact (“My brother is now a doctor”), the new string just adds to the log, creating potential contradictions. It also lacks structure, making it hard to distinguish state changes over time (e.g., “Barry was CEO” vs. “Claude is CEO”).

-----

Phase: [EXPLOITATION]

### Source [7]: https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/

Query: What are pros and cons of raw strings for storing agent memories?

Answer: Keep raw episodic records. Don’t just rely on summaries; they can drift or lose details. Raw records let you return to what actually happened and pull them in when necessary. Summarization drift occurs when you repeatedly compress history to fit it within a context window. Each compression/summarization throws away details, and eventually, you’re left with memory that doesn’t really match what happened. Attention dilution is the other failure mode in this category. Even if you can keep everything in context (as with the new 1 million-token windows), larger prompts “lose” information in the middle. While agents technically have all the memories, they can’t focus on the right parts at the right time.

-----

Phase: [EXPLOITATION]

### Source [8]: https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/

Query: What are pros and cons of raw strings for storing agent memories?

Answer: Today’s AI agents store long interaction histories but struggle to reuse them effectively. Raw memory retrieval can overwhelm agents with lengthy, low-value context. As interaction logs accumulate, they grow large, fill with irrelevant content, and become increasingly difficult to use. More memory means that agents must search through larger volumes of past interactions to find information relevant to the current task. Without structure, these records mix useful experiences with irrelevant details, making retrieval slower and less reliable. The challenge is not storing more experiences, but organizing them so that agents can quickly identify what matters in the moment.

-----

Phase: [EXPLOITATION]

### Source [9]: https://stevekinney.com/writing/agent-memory-systems

Query: What are pros and cons of raw strings for storing agent memories?

Answer: Case-based: Store raw trajectories. “User asked X, I tried approach Y, it failed with error Z, I tried approach W, it worked.” ExpeL (Zhao et al., 2024), Memento, and JARVIS-1 all take this approach. You get high fidelity—the full record of what happened—but poor generalization and expensive context consumption. Replaying a 200-step trajectory to avoid a mistake on step 47 is wasteful.

-----

</details>

<details>
<summary>How do knowledge graphs model temporal relationships in agent memory?</summary>

Phase: [EXPLOITATION]

### Source [10]: https://www.octoco.ai/blog/knowledge-graphs-as-memory

Query: How do knowledge graphs model temporal relationships in agent memory?

Answer: Knowledge graphs as agent memory store not just what the agent learns, but how different pieces of information relate to each other, and how those relationships change over time. Graphiti is Zep’s open-source framework for building temporally-aware knowledge graphs, specifically designed for agent memory, handling chat histories, structured data, and unstructured text in a unified graph. Knowledge graphs support incremental updates where new facts are added, relationships are modified, and the graph evolves without expensive recomputation, essential for agents learning from ongoing interactions. Temporal reasoning demands are essential as agents take on longer-running tasks and maintain relationships across sessions; an agent cannot manage a multi-week project if it forgets yesterday.

-----

Phase: [EXPLOITATION]

### Source [11]: https://ai.plainenglish.io/temporal-reasoning-in-ai-agent-memory-allens-interval-algebra-and-event-graphs-bd5fe9d3d1ef

Query: How do knowledge graphs model temporal relationships in agent memory?

Answer: Temporal Knowledge Graphs implement event graphs where nodes represent events with temporal attributes and edges represent Allen’s interval algebra relations or causal connections. Allen’s interval algebra provides a vocabulary for 13 possible relations between time intervals (e.g., before, during, overlaps), with a composition table enabling reasoning about indirect temporal relationships, such as if A is before B and B is during C, inferring constraints on A and C. Graph traversal algorithms enable complex temporal reasoning. Key properties include temporal consistency (e.g., transitivity: if A before B and B before C, then A before C), causal layering (encoding causation beyond temporality), abstraction hierarchies (connecting high-level to sub-events), and uncertainty handling with probabilistic elements. Constraint satisfaction networks represent temporal knowledge as constraints on event times, updating with new observations for consistency.

-----

Phase: [EXPLOITATION]

### Source [12]: https://neo4j.com/nodes-2025/agenda/building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs/

Query: How do knowledge graphs model temporal relationships in agent memory?

Answer: Temporal knowledge graphs (TKGs) integrate time as a first-class citizen, capturing not only what happened but also when and how relationships evolve over time. Unlike static knowledge graphs, TKGs provide temporal granularity, transforming static knowledge into a living, evolving memory for AI agents. They serve as dynamic memory architecture using frameworks like LangGraph and Graphiti on top of Neo4j graph databases to build evolving AI systems.

-----

Phase: [EXPLOITATION]

### Source [13]: https://medium.com/@bijit211987/agents-that-remember-temporal-knowledge-graphs-as-long-term-memory-2405377f4d51

Query: How do knowledge graphs model temporal relationships in agent memory?

Answer: Temporal Knowledge Graphs (TKGs) introduce time as a first-class citizen in knowledge graphs, enabling modeling of evolving relationships. Key features include time-stamped edges capturing when relationships started, evolved, or ended; event-driven updates for incorporating new information over time; decay and aging policies to weight old information less; and provenance tracking for knowledge acquisition details. A typical agent memory layer with TKG includes input parser converting observations to structured events, entity/relation extractor with timestamps, graph store for time-aware edges and reasoning, query layer for relevant subgraphs, memory manager for aging/pruning/deduplication/conflict resolution, and agent orchestrator combining memories. TKGs model habits/changes in behavior, decision sequences/outcomes, context-specific preferences. They support semantic memory (facts/relationships), episodic memory (event sequences), and contextual memory adapting over time.

-----

Phase: [EXPLOITATION]

### Source [14]: https://developers.openai.com/cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents

Query: How do knowledge graphs model temporal relationships in agent memory?

Answer: Temporal knowledge graphs make facts time-aware by using time-stamped triplets: [Subject] - [Predicate] - [Object] with valid_at (when true) and invalid_at (when stopped being true) timestamps, allowing queries like 'What was true at time T?' or analysis of fact/relationship shifts. A Temporal Agent pipeline ingests raw data into these triplets. The extraction prompt determines temporal nuances for statements (facts vs. predictions, static vs. dynamic), ensuring consistency in formatting for knowledge graph ingestion, enabling precise time-based querying, timeline construction, and trend analysis.

-----

</details>

<details>
<summary>What prompt extracts semantic facts for mem0 semantic memory?</summary>

Phase: [EXPLOITATION]

### Source [15]: https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer

Query: What prompt extracts semantic facts for mem0 semantic memory?

Answer: The prompt `MEMORY_DEDUCTION_PROMPT` extracts semantic facts for mem0's semantic memory. In the initial memory extraction step, Mem0 processes new data like user chat history or interactions using `MEMORY_DEDUCTION_PROMPT` to analyze input and metadata, generating a list of facts, preferences, and memories in concise bullet-point format. For example, from mentions of loving Italian food and disliking cold weather, it extracts 'Enjoys Italian cuisine' and 'Prefers warm climates'. This distills unstructured interactions into structured memory points. The full prompt is: 'Deduce the facts, preferences, and memories from the provided text.
Just return the facts, preferences, and memories in bullet points:
Natural language text: {user_input}
User/Agent details: {metadata}
Constraint for deducing facts, preferences, and memories:
- The facts, preferences, and memories should be concise and informative.
- Don\'t start by "The person likes Pizza". Instead, start with "Likes Pizza".
- Don\'t remember the user/agent details provided. Only remember the facts, preferences, and memories.
Deduced facts, preferences, and memories:' This prompt transforms raw user input into structured, concise memory points crucial for semantic memory.

-----

Phase: [EXPLOITATION]

### Source [16]: https://github.com/mem0ai/mem0/blob/main/mem0/configs/prompts.py

Query: What prompt extracts semantic facts for mem0 semantic memory?

Answer: The repository contains prompts for memory extraction in mem0. `USER_MEMORY_EXTRACTION_PROMPT` is for extracting facts, user memories, and preferences from user messages only: 'You are a Personal Information Organizer, specialized in accurately storing facts, user memories, and preferences. [...] # [IMPORTANT]: GENERATE FACTS SOLELY BASED ON THE USER\'S MESSAGES. DO NOT INCLUDE INFORMATION FROM ASSISTANT OR SYSTEM MESSAGES. [...] - Create the facts based on the user messages only. [...] - Make sure to return the response in the format mentioned in the examples. The response should be in json with a key as "facts" and corresponding value will be a list of strings. [...] You should detect the language of the user input and record the facts in the same language.' Similarly, `AGENT_MEMORY_EXTRACTION_PROMPT` extracts facts about the AI assistant from assistant messages only: 'You are an Assistant Information Organizer [...] # [IMPORTANT]: GENERATE FACTS SOLELY BASED ON THE ASSISTANT\'S MESSAGES. DO NOT INCLUDE INFORMATION FROM USER OR SYSTEM MESSAGES.' These prompts organize conversation data into distinct facts for semantic memory.

-----

Phase: [EXPLOITATION]

### Source [17]: https://docs.mem0.ai/open-source/features/custom-instructions

Query: What prompt extracts semantic facts for mem0 semantic memory?

Answer: Mem0 allows customizing fact extraction for semantic memory with `custom_fact_extraction_prompt` or `custom_instructions`. Example: 'custom_instructions = """Please only extract entities containing customer support information, order details, and user information.
Here are some few shot examples:

Input: Hi.
Output: {"facts" : []} [...]
Input: My order #12345 hasn\'t arrived yet.
Output: {"facts" : ["Order #12345 not received"]}
[...]
Return the facts and customer information in a json format as shown above."""' This tailors extraction to store only relevant details like facts in JSON format with 'facts' key. Loaded via configuration: 'from mem0 import Memory' and setting custom_instructions.

-----

Phase: [EXPLOITATION]

### Source [18]: https://www.linkedin.com/posts/mem0_how-mem0-works-under-the-hood-1-message-activity-7376713317391896576-ALQP

Query: What prompt extracts semantic facts for mem0 semantic memory?

Answer: In Mem0's pipeline, extraction step uses LLM to read current message, last m messages, and summary to extract salient memories as clean statements about facts, preferences, or events for semantic memory. No specific prompt name mentioned; process triggered by new user message, fetches context, extracts memories in parallel with asynchronous summary generation.

-----

Phase: [EXPLOITATION]

### Source [19]: https://mem0.ai/blog/long-term-memory-ai-agents

Query: What prompt extracts semantic facts for mem0 semantic memory?

Answer: Semantic memory in Mem0 stores facts, preferences, and constraints about the user across sessions, e.g., 'Budget cap $50K', 'Preferred channel: email'. Updated when contradicted. Part of long-term memory including semantic (facts), episodic, procedural. Retrieval embeds query, searches top candidates, scores by relevance × recency × type_weight (semantic: 0.6), injects top results. No specific extraction prompt named; focuses on production pipelines: extract → consolidate → store → retrieve via vectors/graphs.

-----

</details>

<details>
<summary>Why should agents autonomously manage memory without user editing?</summary>

Phase: [EXPLOITATION]

### Source [20]: https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/

Query: Why should agents autonomously manage memory without user editing?

Answer: The paper characterizes agent memory as a write-manage-read loop, not just “store and retrieve.” Write: New information enters memory (observations, results, reflections). Manage: Memory is maintained, pruned, compressed, and consolidated. Read: Relevant memory is retrieved and injected into the context. Most implementations nail “write” and “read” and completely neglect “manage.” They accumulate without curation. The result is noise, contradiction, and bloated context. Managing is the hard part, and it’s where most systems struggle or outright fail. Keep raw episodic records. Don’t just rely on summaries; they can drift or lose details. Raw records let you return to what actually happened and pull them in when necessary. Version reflective memory. To help avoid contradictions in summaries, long-term memories, and compressions, add timestamps or versions to each. This can help your agents determine what is true and what is the most accurate reflection of the system. Semantic Memory is responsible for abstracted, distilled knowledge, facts, heuristics, and learned conclusions. In OpenClaw, this is the MEMORY.md file in each agent’s workspace. It’s curated. Not everything goes in. The agent (or I, periodically) decides what’s worth preserving as a lasting truth versus what was situational. This curation step is critical; without it, semantic memory becomes a junk drawer.

-----

Phase: [EXPLOITATION]

### Source [21]: https://medium.com/@nirdiamant21/memory-optimization-strategies-in-ai-agents-1f75f8180d54

Query: Why should agents autonomously manage memory without user editing?

Answer: Long-Term Memory: This is information the agent keeps across sessions and over time. It’s often stored in external databases so the AI can look it up when needed. The bottom line: giving AI the right kind of memory makes it behave less like a forgetful goldfish and more like a thoughtful companion. But simply having memory isn’t enough; it must be used efficiently. The agent maintains a small “active” memory (like RAM) for immediate processing, while storing the bulk of its memories in external storage (like a hard drive). When it needs to recall something from long ago, it can “page in” that memory, temporarily bringing it into active context. This allows virtually unlimited conversation length while maintaining fast response times. Smart Filtering: Not all pieces of memory are equally important. AI agents can assign scores to potential memory contents to decide what to keep. If the conversation is about travel plans, the agent might score context related to “flights” and “hotels” higher than an offhand joke made earlier. Dynamic Memory Allocation: Some advanced systems adjust how they use memory based on context complexity. If the user asks a very complex question, the agent might allocate more of its context budget to pulling in relevant background info.

-----

Phase: [EXPLOITATION]

### Source [22]: https://www.dailydoseofds.com/ai-agents-crash-course-part-15-with-implementation/

Query: Why should agents autonomously manage memory without user editing?

Answer: Memory management is a crucial aspect when working with AI agents. An AI agent's ability to retain and utilize information from previous interactions is essential for generating coherent and contextually appropriate responses. Many developers assume that the ever-increasing context windows will eliminate the need for memory management. Unfortunately, this assumption breaks down the moment you move from a playground script to a production-grade system. An agent must actively manage its memory to ensure the most relevant facts are prioritized, which necessitates a system more nuanced than a simple history dump. Developers may encounter challenges maintaining consistent memory over prolonged interactions or tasks. Just as humans selectively remember important details and let trivial ones fade, AI agents need clever strategies to remember what matters and forget what doesn’t. Memory is dynamic and contextual. It consists of data that an agent stores during its operations, such as conversation history, user preferences, previous outputs, or the state of an ongoing task. If a system is running without memory, every interaction is a blank slate. It doesn’t matter if the user told the agent their name five seconds ago because it’s already forgotten.

-----

Phase: [EXPLOITATION]

### Source [23]: https://stevekinney.com/writing/agent-memory-systems

Query: Why should agents autonomously manage memory without user editing?

Answer: Agent memory stores user-specific, persistent, potentially sensitive content. In a multi-tenant system, one user’s memories must not be accessible to another. Research shows that memory modules can leak private data through indirect prompt-based attacks. If your memory retrieval path doesn’t enforce strict tenant isolation at the retrieval level—not just at the storage level—you have a data leak waiting to happen. Token-level memory is memory stored as explicit, discrete, human-readable units—text chunks, facts, user profiles, conversation logs. You write it to a database or the filesystem, you read it back, you stuff it into the prompt. Factual memory enables consistency (don’t contradict yourself across conversations), coherence (maintain topical continuity within a conversation), and adaptability (personalize behavior over time based on what you learn about the user).

-----

Phase: [EXPLOITATION]

### Source [24]: https://arxiv.org/html/2601.11653v1

Query: Why should agents autonomously manage memory without user editing?

Answer: Both paradigms treat memory as accumulated text and provide no principled write path for internal state. They do not specify what should persist, what should be revised, and what should be discarded. As horizons increase, this absence of memory governance leads to drift, loss of task invariants, and hallucinations induced by irrelevant, stale, or inconsistently recalled context. AI agents are increasingly used in long, multi-turn workflows in both research and enterprise settings. As interactions grow, agent behavior often degrades due to loss of constraint focus, error accumulation, and memory-induced drift. This problem is especially visible in real-world deployments where context evolves, distractions are introduced, and decisions must remain consistent over time.

-----

</details>

<details>
<summary>How do semantic episodic procedural memories differ in agents?</summary>

Phase: [EXPLOITATION]

### Source [25]: https://atlan.com/know/types-of-ai-agent-memory/

Query: How do semantic episodic procedural memories differ in agents?

Answer: Semantic memory stores general facts and definitions — what things are, independent of when or where they were learned. Episodic memory stores specific past events tied to time — what happened, when, in which session. Semantic memory is queried for “what does revenue mean”; episodic memory is queried for “did this agent run this revenue query before and what did it return?” Both are long-term external stores retrieved into the context window on demand. Procedural memory is per-agent rather than centrally governed, highlighting a gap in standard implementations for enterprise data agents. Each type has specific gaps at the enterprise layer: semantic memory lacks governance state, episodic memory is conversation-centric rather than data-event-centric, procedural memory is per-agent and unversioned.

-----

Phase: [EXPLOITATION]

### Source [26]: https://www.geeksforgeeks.org/artificial-intelligence/ai-agent-memory/

Query: How do semantic episodic procedural memories differ in agents?

Answer: Episodic Memory: This type remembers specific events from the past like a user’s date of birth that was used during an earlier conversation. The agent can use this memory as context in future interactions. Semantic Memory: This holds general knowledge about the world or things the AI has learned through past interactions. The agent can refer to this information to handle new problems effectively. Procedural Memory: Here the agent stores “how-to” steps or rules for making decisions. For example, it might remember the process for solving a math problem and use the same steps when tackling a similar task later.

-----

Phase: [EXPLOITATION]

### Source [27]: https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/

Query: How do semantic episodic procedural memories differ in agents?

Answer: The distinction between episodic and semantic memory matters for autonomous agents. Episodic memory tells the agent “Last Tuesday, when we tried approach X with client Y, it failed because of Z.” Semantic memory tells the agent “Approach X generally works best when conditions A and B are present.” Both are essential, but they serve different cognitive functions. For agents working in specialized domains, semantic memory often integrates with RAG systems to pull in domain-specific knowledge. Procedural memory guides execution: the agent automatically knows to start with market sizing, then move to competitive landscape analysis, followed by risk assessment, and conclude with investment recommendations. It knows how to structure sections, when to include executive summaries, and the standard format for citing sources. Without all three working together, the agent would be less capable. Episodic memory alone would make it over-personalized with no general knowledge. Semantic memory alone would make it knowledgeable but unable to learn from experience. Procedural memory alone would make it good at executing programmed tasks, but inflexible when encountering new situations. For personal AI assistants focused on user personalization, episodic memory is most important. For domain expert agents in fields like law, medicine, or finance, semantic memory matters most. For workflow automation agents that handle repetitive processes, procedural memory is key.

-----

Phase: [EXPLOITATION]

### Source [28]: https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory

Query: How do semantic episodic procedural memories differ in agents?

Answer: Long-term memory types provide the foundation for persistent learning and adaptation. Episodic Memory maintains records of specific events and interactions, similar to your autobiographical memories of particular conversations or experiences. Semantic Memory serves as the agent's organized knowledge repository about facts, concepts, and relationships - think of it as a well-structured library of world knowledge. Procedural Memory stores workflows and skills, enabling agents to execute complex multi-step processes automatically, much like how you can ride a bicycle without consciously thinking about each movement.

-----

Phase: [EXPLOITATION]

### Source [29]: https://ctoi.substack.com/p/memory-systems-in-ai-agents-episodic

Query: How do semantic episodic procedural memories differ in agents?

Answer: Episodic memory captures the "what happened when" of an agent's experience. Think of it as a detailed journal of specific interactions: user X clicked product Y at timestamp Z, resulting in outcome W. This memory type preserves the contextual richness of individual events, maintaining the temporal sequence and environmental conditions that surrounded each decision. Semantic memory supplies generalized rules. The genius emerges when these memory types work in concert. When the vehicle encounters a similar intersection, episodic memory provides specific contextual details while semantic memory supplies generalized rules. This dual-memory approach enables the agent to be both adaptive to novel situations and consistent in its fundamental behaviors.

-----

</details>

<details>
<summary>How does mem0 handle episodic memory creation with timestamps?</summary>

Phase: [EXPLOITATION]

### Source [35]: https://docs.mem0.ai/platform/features/timestamp

Query: How does mem0 handle episodic memory creation with timestamps?

Answer: Mem0 allows adding custom timestamps to memories for chronological accuracy and historical context. The documentation provides code examples for adding memories with timestamps. Import necessary modules including mem0 MemoryClient. Set MEM0_API_KEY. Create client. Compute timestamps: current_time = datetime.now(), five_days_ago = current_time - timedelta(days=5), unix_timestamp = int(five_days_ago.timestamp()). Add memory: client.add(messages=[{"role": "user", "content": "I'm travelling to SF"}], user_id="user1", timestamp=unix_timestamp). Timestamp format is Unix timestamp (seconds since epoch), e.g., january_2023_timestamp = 1672531200 for 2023-01-01 00:00:00 UTC. Use client.add(messages, user_id="user1", timestamp=january_2023_timestamp). This enables precise dating of memories during creation.

-----

Phase: [EXPLOITATION]

### Source [36]: https://atlan.com/know/episodic-memory-ai-agents/

Query: How does mem0 handle episodic memory creation with timestamps?

Answer: Mem0 stores episodic memories across user, agent, and session scopes using hybrid storage: vector databases for similarity search and graph databases (Pro tier) for relationship modeling. Retrieval works via date search and text search on the recall database. When new information contradicts existing memory, Mem0 updates rather than duplicates, using adaptive deduplication. Mem0’s graph memory stores entities as nodes and relationships as directed labeled edges, allowing fact evolution modeling for conversation-level facts. Agents pull from Recall Memory on demand; it is always out-of-context by default. Consolidation is agent-directed only.

-----

Phase: [EXPLOITATION]

### Source [37]: https://arxiv.org/html/2504.19413v1

Query: How does mem0 handle episodic memory creation with timestamps?

Answer: In Mem0, each entity node contains metadata including a creation timestamp t_v. Relationships are structured as triplets (v_s, r, v_d) with source and destination entity nodes and labeled edges. The system evaluates memory generation with timestamps, participant names, and conversation text. Prompting extracts memories with timestamps for temporal reasoning, leveraging natural language contextualization and structured graph representations. Entity nodes include entity type classification, embedding vector, and creation timestamp.

-----

</details>

<details>
<summary>How to implement procedural memory as learned agent workflows?</summary>

Phase: [EXPLOITATION]

### Source [38]: https://arxiv.org/html/2508.06433v2

Query: How to implement procedural memory as learned agent workflows?

Answer: By shifting from parallel task completion to sequential task completion, the agent can learn and distill experience from earlier tasks, thereby reducing repetitive exploration. Inspired by human procedural memory, we propose to equip the agent with a procedural memory module. This module transforms the conventional policy π(a_t|s_t) into π_{m^p}(a_t|s_t), where m^p is the agent’s learned procedural memory. Procedural memory is a type of long-term memory that involves the retention of procedures and skills, such as typing or riding a bike, which are performed automatically without conscious thought. For an agent, for a task trajectory τ and its reward r, a memory m^p is constructed by a builder B, thereby achieving the acquisition of memory, namely Mem = ∑_{t=1}^T m^p_t, where m^p_t = B(τ_t, r_t). These methods involve encoding and storing information in various formats, using retrieval mechanisms like vector embeddings and semantic search, and implementing memory updating and forgetting strategies to maintain relevance and efficiency. Despite its importance, memory in multi-turn agent interactions remains underexplored, and enabling agents to effectively learn and utilize memory across trajectories poses a significant challenge.

-----

Phase: [EXPLOITATION]

### Source [39]: https://arxiv.org/html/2508.06433v4

Query: How to implement procedural memory as learned agent workflows?

Answer: By shifting from parallel task completion to sequential task completion, the agent can learn and distill experience from earlier tasks, thereby reducing repetitive exploration. Inspired by human procedural memory, we propose to equip the agent with a procedural memory module. This module transforms the conventional policy π(a_t|s_t) into π_{m^p}(a_t|s_t), where m^p is the agent’s learned procedural memory. Procedural memory is a type of long-term memory that involves the retention of procedures and skills, such as typing or riding a bike, which are performed automatically without conscious thought. Instead of starting fresh each time, an agent should extract its experience from past successes. By turning earlier trajectories into reusable templates like patterns of reasoning, tool sequences, and recovery tactics, it can progress step by step, learning from every failure and success, until even the most convoluted missions become routine. These methods involve encoding and storing information in various formats, using retrieval mechanisms like vector embeddings and semantic search, and implementing memory updating and forgetting strategies to maintain relevance and efficiency.

-----

Phase: [EXPLOITATION]

### Source [40]: https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/

Query: How to implement procedural memory as learned agent workflows?

Answer: Procedural Memory is encoded executable skills, behavioral patterns, and learned behavior. In OpenClaw, this maps mostly to the AGENTS.md and SOUL.md files, which contain persona instructions, behavioral constraints, and escalation rules. When the agent reads these at the start of the session, it’s loading procedural memory. These should be updated based on user feedback, or even through ‘dream’ processes that analyze interactions. Treat procedural memory as code. In OpenClaw, your Agents.MD, Memory.MD, personal files, and behavioral configs are all part of your memory architecture. Review them and keep them under source control so you can examine what changes and when. This is especially important if your autonomous system can alter these based on feedback. Keep raw episodic records. Don’t just rely on summaries; they can drift or lose details. Raw records let you return to what actually happened and pull them in when necessary. Version reflective memory. To help avoid contradictions in summaries, long-term memories, and compressions, add timestamps or versions to each. This can help your agents determine what is true and what is the most accurate reflection of the system.

-----

Phase: [EXPLOITATION]

### Source [41]: https://openreview.net/forum?id=NTAhi2JEEE

Query: How to implement procedural memory as learned agent workflows?

Answer: Agent Workflow Memory (AWM) is a method for inducing commonly reused routines, i.e., workflows, and selectively providing workflows to the agent to guide subsequent generations. AWM flexibly applies to both offline and online scenarios, where agents induce workflows from training examples beforehand or from test queries on the fly. Humans can flexibly solve complex tasks by learning reusable task workflows from past experiences and using them to guide future actions. To build agents that can similarly benefit from this process, we introduce AWM that helps AI agents learn useful 'task recipes' — or workflows — from previous examples and reuse them when solving new problems.

-----

Phase: [EXPLOITATION]

### Source [42]: https://dev.to/blackgirlbytes/turning-agent-history-into-procedural-memory-37f8

Query: How to implement procedural memory as learned agent workflows?

Answer: Turning Agent History into Procedural Memory by creating procedural memory for agents as infrastructure. Procedural memory is the answer to the question, 'How do I do this kind of work well, here, in this repo, with this team?' The most popular way people are currently building reusable workflows is with Skills, so built an orchestrator skill called `Session-to-Skill`. It creates Skills for me based on repeated behavior. The Skill uses Entire to search my session metadata, checkpoints, and explanations of prior work to find the durable pattern. This data isn’t just for review, audit, or to sit quietly in the background. It’s a source of truth that can be used for building better workflows. Use agent history to recreate that ‘package up a session’ magic, but in a way that works across any agent, and works retrospectively. Daily engineering work is not net-new. You may receive a new ticket, but somebody has solved this problem before.

-----

</details>

<details>
<summary>How does agent retrieval pipeline rank parallel memory queries?</summary>

Phase: [EXPLOITATION]

### Source [43]: https://vizuara.substack.com/p/a-primer-on-re-ranking-for-retrieval

Query: How does agent retrieval pipeline rank parallel memory queries?

Answer: The source discusses ranking outputs from multiple retrievers or agents using Reciprocal Rank Fusion (RRF) in advanced RAG systems with parallel queries. The RRF formula is: RRF(d) = ∑_{i=1}^M 1/(k + rank_i(d)), where d is a candidate document, M is the number of retrievers, rank_i(d) is the rank by retriever i, and k is a constant (usually 60) to dampen high ranks. This fuses rankings from parallel retrievers/experts into a consensus ranking. It also covers agent-level reranking for outputs from independent agents (LLM + Memory + Tools). Approaches include: 1. Pointwise Scoring: s_i = f_θ(query, agent_i’s output), using LLM, cross-encoder, or scoring function for alignment, correctness, completeness. Parallelizable for self-contained outputs. 2. Pairwise Comparison: Compares agent outputs in pairs. This is conceptualized like CoLBERT at the agent level, comparing agent outputs (multi-modal or multi-step reasoning) instead of token embeddings. Reranking resolves contradictions using meta-knowledge about agent reliability, prioritizing the best agent output or combining perspectives.

-----

Phase: [EXPLOITATION]

### Source [44]: https://www.comet.com/site/blog/retrieval-augmented-generation/

Query: How does agent retrieval pipeline rank parallel memory queries?

Answer: In production RAG systems, hybrid search executes dense and sparse queries in parallel and fuses them into a single ranked list using Reciprocal Rank Fusion (RRF), the standard algorithm introduced by Cormack, Clarke, and Büttcher at SIGIR 2009. Reranking is a second-pass using cross-encoder models (e.g., BGE-Reranker) on top-N candidates (top 25-50) from initial retrieval. Cross-encoders process query and candidate chunk simultaneously for accurate relevance scores via token attention, improving accuracy for ambiguous queries despite added latency.

-----

Phase: [EXPLOITATION]

### Source [45]: https://docs.cohere.com/docs/generating-parallel-queries

Query: How does agent retrieval pipeline rank parallel memory queries?

Answer: In agentic RAG, complex queries are expanded or split into multiple optimized queries run in parallel using parallel tool calling in the Chat endpoint. For example, 'What were Apple’s and Google’s revenue in 2023?' becomes two separate queries. Over multiple data sources, queries are generated for each (e.g., developer docs and code examples) and searches performed in parallel. The agent then combines information from both sources in the response. No explicit ranking method for fusing parallel query results is detailed; focus is on query expansion and parallel execution.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What mathematical models underpin semantic memory embeddings in agents?</summary>

Phase: [EXPLORATION]

### Source [46]: https://sparkco.ai/blog/deep-dive-into-embedding-models-for-agent-memory

Query: What mathematical models underpin semantic memory embeddings in agents?

Answer: The encoder-decoder architecture serves as the backbone for embedding models in agent memory systems. The encoder, often a BERT-like model, processes the input text to generate contextual embeddings. These embeddings capture the semantic nuances of the text, making them ideal for memory storage. The decoder, typically lighter, is tasked with transforming these embeddings into output forms required by downstream tasks. Embedding models are evolving with techniques such as contextualized embeddings and transfer learning. These methods leverage pre-trained models like BERT and GPT to generate embeddings that encapsulate complex semantic meanings. A notable innovation is the use of contrastive learning to enhance embeddings by distinguishing between similar and dissimilar data points. The evolution of embedding models has been marked by significant advancements from traditional text representations to sophisticated deep learning models that power today's AI agent memory systems.

-----

Phase: [EXPLORATION]

### Source [48]: https://www.emergentmind.com/topics/semantic-embedding-methods

Query: What mathematical models underpin semantic memory embeddings in agents?

Answer: Tensor Decomposition Models: Knowledge graphs are represented as tensors with triplets (subject, relation, object) and decomposed using methods such as Canonical Polyadic (CP), Tucker, or RESCAL (Tresp et al., 2015, Tran et al., 2019). DistMult, ComplEx, and quaternion-based models extend this with more expressive multi-embedding interactions (Tran et al., 2019). Translational Models: TransE interprets relations as translations in vector space: for a valid triple (h, r, t), h + r ≈ t (Tran et al., 2019). Semilattice Embeddings: Symbolic problems are encoded as sentences in algebraic semilattice theories, producing atomized models that correspond exactly to discrete solution sets (Martin-Maroto et al., 2022). Quantum Algorithm Embeddings: Semantic embedding formalizes the algebraic manipulation of polynomial transformations in quantum circuits (QSP/QSVT), linking algorithmic operations with polynomial function space via category theory (Rossi et al., 2023). Across methods, the common design involves representing each object (e.g., word w, entity e, feature f) as a vector v_w ∈ ℝ^d (or in structured settings, as multi-embedding sets or tensors). Parameters are learned by minimizing an objective reflecting conditional likelihood (e.g., cross-entropy, log-loss), reconstruction error (e.g., squared loss for factorization), or a probabilistic negative log-likelihood for exponential family models (Rudolph et al., 2016). Semantic Space Projection (SSP): Combines symbolic structure with topic vectors derived from text, projecting embeddings onto semantic subspaces (Xiao et al., 2016).

-----

Phase: [EXPLORATION]

### Source [49]: https://www.mindstudio.ai/blog/semantic-memory-search-ai-agents-levels-tools/

Query: What mathematical models underpin semantic memory embeddings in agents?

Answer: This works through vector embeddings. Text (or other data) gets converted into a numerical representation — a list of hundreds or thousands of numbers — that captures its semantic meaning. Similar ideas end up close together in that high-dimensional space. When an agent needs to retrieve something, it embeds the query the same way and finds the nearest neighbors. Level 3 — Semantic Memory Search (Vector Retrieval): The agent converts information into vector embeddings, stores them in a vector database, and retrieves contextually relevant chunks at query time. The retrieval process works like this: This is the core of what most people mean when they talk about Retrieval-Augmented Generation (RAG). The Role of Embeddings and Chunking: Two implementation details matter enormously for semantic memory quality: how you chunk content and which embedding model you use.

-----

Phase: [EXPLORATION]

### Source [50]: https://arxiv.org/html/2602.06052v3

Query: What mathematical models underpin semantic memory embeddings in agents?

Answer: In foundation agent architectures, semantic memory functions as a stable knowledge base that supports knowing-what factual reasoning (Tulving, 1972). Its content is typically derived through the distillation and decontextualization of recurring facts accumulated in episodic memory. When an agent encounters similar knowledge patterns across multiple tasks, fragmented factual information from individual experiences is consolidated into universal concepts, entity relations, or attribute summaries via summarization mechanisms. Current techniques, such as hierarchical navigable small-world (HNSW) (Liu et al., 2025h), inverted file (IVF) (Rege et al., 2023), or product quantization (PQ) (Huang and Huang, 2024) indexing, are developed and optimized to find the most semantically similar documents or past interactions efficiently in a high-dimensional embedding space. This approximate-nearest-neighbor search retrieves a small set of context snippets, which are mapped back to their original form and fed into the agent or LLM to integrate its response with relevant, previously unseen information (Guu et al., 2020).

-----

</details>

<details>
<summary>What failure modes occur in procedural memory learning for ReAct agents?</summary>

Phase: [EXPLORATION]

### Source [51]: https://dev.to/jonathanfarrow/-how-an-agent-actually-learns-from-experience-2m28

Query: What failure modes occur in procedural memory learning for ReAct agents?

Answer: The source discusses agent memory systems, highlighting a gap in experiential memory, which is how agents improve from past actions (procedural memory). Hu et al.'s survey identifies three categories: factual memory (implemented in most systems), experiential memory (almost none implement), and working memory. Experiential memory provides leverage for agents over multiple sessions. Five failure modes emerge in agent memory systems after weeks of usage: 1. the contradiction problem (incomplete snippet, but listed first). Other problems include 'what did we know when' (reconstructing past beliefs, valid-time vs transaction-time tracking deficiencies), and 'it happened at the same time' (lack of temporal intervals and relationships, hindering pattern detection like temporal co-occurrence). These temporal and versioning issues break effective learning from experience in procedural contexts.

-----

Phase: [EXPLORATION]

### Source [52]: https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition/

Query: What failure modes occur in procedural memory learning for ReAct agents?

Answer: AI agent failure modes include context degradation, specification drift, sycophantic confirmation, tool call failures, cascading failure, and silent failure. These are structurally different from software bugs. Silent and cascading failures are most dangerous as outputs look plausible while errors propagate undetected. Failures in multi-step pipelines originate earlier; trace backward. Sycophancy requires prompt countermeasures and testing. Silent failure combines with sycophancy: LLMs produce confident text without accuracy or uncertainty signals. Fixes need external infrastructure like test sets, validation, uncertainty prompting. In multi-agent systems, cascading failures propagate. These modes disrupt learning loops in ReAct-style agents where procedural memory relies on iterative reasoning-action-observation.

-----

Phase: [EXPLORATION]

### Source [53]: https://builder.aws.com/content/3BOny05LArVv7BVN8PU3duOPM86/why-ai-agents-fail-3-failure-modes-that-cost-you-tokens-and-time

Query: What failure modes occur in procedural memory learning for ReAct agents?

Answer: Three common AI agent failure modes: 1. Context window overflow (tool returns excess data, leading to silent degradation, truncation, lost context; e.g., IBM research: 20M tokens failed vs 1,234 succeeded with pointers). 2. MCP tool timeouts (external APIs block indefinitely). 3. Reasoning loops (repeats tool calls without progress). These waste tokens and degrade quality. Fixes: Memory pointers for overflow; async patterns for timeouts; DebounceHook + clear tool states (SUCCESS/FAILED) for loops, reducing calls from 14 to 2. Hooks intercept via BeforeToolCallEvent to block duplicates. In ReAct agents, these disrupt procedural learning by breaking iterative refinement from observations.

-----

Phase: [EXPLORATION]

### Source [54]: https://www.mindstudio.ai/blog/ai-agent-failure-modes-reasoning-action-disconnect/

Query: What failure modes occur in procedural memory learning for ReAct agents?

Answer: Four failure modes where agents know the answer but err: 1. Reasoning-Action Disconnect (chain-of-thought correct, but final action contradicts; disorienting). 2. Lost in the middle (long contexts ignore middle info). 3. Distractor susceptibility (drawn to plausible incorrect details). 4. Context Contamination (correct info crowded out by irrelevant/misleading data; agent has right answer but doesn't use it). Causes: position bias, authority mimicry, high-volume distortion. In ReAct agents, reasoning-action disconnect directly breaks procedural memory learning as observations aren't translated to actions despite correct reasoning.

-----

</details>

<details>
<summary>How do latency tradeoffs scale in graph memory updates for agents?</summary>

Phase: [EXPLORATION]

### Source [56]: https://atlan.com/know/agent-memory-architectures/

Query: How do latency tradeoffs scale in graph memory updates for agents?

Answer: On the LOCOMO benchmark, graph-enhanced memory achieves 68.4% accuracy at 2.59s p95 (Mem0g variant), better relational performance than flat vector at a modest latency cost. Graph memory moved from experimental to production by early 2026; 13 agent frameworks now support graph memory integrations (Mem0 State of Memory 2026). In production in 2026, five patterns span trade-offs from 72.9% accuracy at 17.12s p95 latency to 66.9% at 1.44s. The five patterns escalate in complexity and capability from simplest (zero infrastructure, everything in the context window) to most enterprise-capable (the organization’s existing governed metadata graph as agent memory). Each pattern reflects a different primary constraint: token cost, latency, relational complexity, temporal validity, or governance. Most production systems combine two or more of these patterns.

-----

Phase: [EXPLORATION]

### Source [57]: https://www.digitalapplied.com/blog/agent-memory-architectures-vector-graph-episodic

Query: How do latency tradeoffs scale in graph memory updates for agents?

Answer: Vector memory wins on recency and similarity: Mem0 and Zep excel at surfacing recent, semantically similar facts. They struggle when the right answer depends on multi-hop relationships or precise temporal ordering. Graph memory wins on entity reasoning: Graph-RAG on Neo4j or TypeDB shines when questions hinge on who-knows-whom, cross-entity constraints, or temporal relationships a vector store cannot express. Fact lookup latency. Paging an old episode in costs a summarization round-trip. For "what's the user's email" queries, vector memory wins on latency. Memory ops cost LLM calls of their own: fact extraction, summarization, re-ranking, and triple extraction all spend tokens. Most production agents should start with vector memory, graduate to vector + short episodic as sessions get longer, and only add a graph layer when a recurring class of questions keeps failing.

-----

Phase: [EXPLORATION]

### Source [58]: https://aerospike.com/blog/langgraph-production-latency-replay-scale/

Query: How do latency tradeoffs scale in graph memory updates for agents?

Answer: Applying updates: within a superstep, intermediate updates are not visible to other actors until the next step. That structure makes race conditions less likely, and makes it practical and manageable to rerun a workflow from a previous point, because the system treats each superstep as a boundary, with a well-defined input and output. Checkpoints align with supersteps. Using a checkpointer, LangGraph can persist state at step boundaries, which allows workflows to resume from previously saved graph states. In agent systems, the part of the system that handles the actual data is involved in generating the model’s output tokens. A checkpoint write that stalls for 20 or 30 milliseconds also pushes out the next model invocation, which pushes out time to first token for the user. When hundreds or thousands of concurrent agent runs all hit superstep boundaries at roughly similar times, any storage tier that doesn’t have reliable latency will become obvious to the user.

-----

Phase: [EXPLORATION]

### Source [59]: https://www.decodingai.com/p/agentic-graphrag

Query: How do latency tradeoffs scale in graph memory updates for agents?

Answer: During retrieval, GraphRAG’s addition over RAG is this multi-hop step, after the RRF merge, which is standard for most RAG systems. Two-stage retrieval. Text and semantic search feed RRF for entry points. From there, 2-3 hop graph traversal expands the result set. There’s bottom-up, which expands entities for depth, while top-down hops across communities for a high-level overview. This translates to a trade-off between context size, latency and performance. Bottom-up vs. top-down GraphRAG. Both start at text and semantic search. Bottom-up expands entities for depth. Top-down hops across communities for a high-level overview. As the data grows, gets more complex, or we have to operate under strict cost/latency requirements, we will need more powerful solutions.

-----

Phase: [EXPLORATION]

### Source [60]: https://stevekinney.com/writing/agent-memory-systems

Query: How do latency tradeoffs scale in graph memory updates for agents?

Answer: Knowledge graph is the full-power solution: entity-relationship triples with graph traversal. Zep, Mem0g, and AriGraph all implement this. Knowledge graphs consistently win on multi-hop benchmarks. The trade-off is significant engineering commitment—building, maintaining, and querying a graph is a lot more work than maintaining a flat vector store. Planar (2D): Entries connected via explicit relationships—graphs, trees, linked notes. These structures enable multi-hop reasoning—following chains of connections to answer questions that no single entry can answer alone. The trade-off is maintenance complexity. Graphs need to be pruned, updated, and kept consistent as new information arrives. Flat (1D): A bag of entries with vector search over them. Most systems should start here.

-----

</details>

<details>
<summary>What open challenges remain in autonomous memory conflict resolution?</summary>

Phase: [EXPLORATION]

### Source [61]: https://arxiv.org/html/2603.07670v1

Query: What open challenges remain in autonomous memory conflict resolution?

Answer: Open challenges in autonomous memory conflict resolution include principled consolidation. Current systems oscillate between hoarding (store everything, drown in noise) and amnesia (compress aggressively, lose rare but vital facts). Neuroscience offers a suggestive model: during sleep, the hippocampus replays recent experiences, strengthening important traces and pruning the rest. An analogous “offline consolidation” process—scheduled during idle periods—could provide a principled balance. Open questions: how to estimate memory importance without future-sight, how to detect when consolidation is needed, and how to guarantee that safety-critical records survive the process. Open concerns remain. RL training over long horizons is expensive. Learned forgetting could delete safety-critical information. Policies trained on one task distribution may fail to transfer. And it is hard to explain why the agent chose a particular memory action—interpretability lags behind capability.

-----

Phase: [EXPLORATION]

### Source [62]: https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/

Query: What open challenges remain in autonomous memory conflict resolution?

Answer: Open challenges in autonomous memory conflict resolution include handling contradictions and knowledge-integrity failures. Contradiction handling can be incredibly frustrating. As new information is collected, if it conflicts with existing information, systems can’t always determine the actual truth. In the OpenClaw system, the agent oscillated between believing the workflow was available and believing it had failed to set up, despite verification. Design tensions involve utility vs. efficiency, with better memory meaning more tokens, latency, storage. Silent orchestration failures like paging, eviction, or archival policies doing the wrong things lead to worse responses. Knowledge-integrity failures occur. The open problems section is honest about how much is unsolved, including evaluation still primitive and governance mostly ignored in practice.

-----

Phase: [EXPLORATION]

### Source [63]: https://www.artefact.com/blog/part-2-from-memory-to-navigation-scaling-autonomous-agents-beyond-retrieval/

Query: What open challenges remain in autonomous memory conflict resolution?

Answer: Open challenges in autonomous memory conflict resolution include adversarial memory poisoning and privacy concerns. Memory that persists and evolves creates attack vectors. Adversarial inputs could poison long-term memory. Over-retention raises privacy concerns in regulated industries. OpenClaw’s 2026.2.3 release addresses some with stronger prompt injection protection, but broader safety implications of learned memory policies remain underexplored. Limitations and open questions: Training data scarcity for RL-based memory training requires environments for practice at scale, but most use synthetic tasks; transfer to enterprise workflows unproven. Reward engineering is fragile, with initial designs leading to models gaming rewards instead of solving tasks, requiring multiple iterations.

-----

Phase: [EXPLORATION]

### Source [64]: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1802727/full

Query: What open challenges remain in autonomous memory conflict resolution?

Answer: Open challenges in autonomous memory conflict resolution include secure memory management and privacy protection. Secure memory management is a major obstacle. More research is needed to design memory architectures that strike a balance between long-term utility and stringent privacy restrictions, such as contextual isolation, verifiable erasure, and selective forgetting. The lack of transparency and control over third-party services makes protecting privacy in tool-augmented reasoning challenging. Policy-aware execution layers and tool interfaces that protect privacy are still in early stages. Absence of formal privacy models for autonomous agents; current definitions from static LLM settings do not capture temporal, persistent, self-directed behavior. Open research challenge to develop agent-aware threat models and privacy metrics accounting for multi-agent coordination, tool interactions, and memory persistence.

-----

Phase: [EXPLORATION]

### Source [65]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory

Query: What open challenges remain in autonomous memory conflict resolution?

Answer: Open challenges in autonomous memory conflict resolution include conflict-driven forgetting and security threats. Conflict-Driven Forgetting: Strategically updating or discarding old memories when new evidence conflicts with them. Pre-merge validation performs logical consistency checks before writes, rejecting updates that contradict core facts to prevent hallucinations from being solidified. Temporal and permission filtering uses decay functions to filter outdated data and access control to prevent cross-user privacy leakage. Reversible periodic alignment uses dual-track storage to roll back errors and bound semantic drift. The paper analyzes security threats to autonomous LLM agents like OpenClaw across lifecycle stages: initialization, input, reasoning, decision-making, execution.

-----

</details>

<details>
<summary>How does cognitive psychology shape AI agent memory architectures?</summary>

Phase: [EXPLORATION]

### Source [66]: https://www.cognee.ai/blog/fundamentals/cognitive-architectures-for-language-agents-explained

Query: How does cognitive psychology shape AI agent memory architectures?

Answer: Cognitive psychology shapes AI agent memory architectures by inspiring a computational view of the mind that fosters collaboration between psychology, computer science, and neuroscience. The Cognitive Architectures for Language Agents (CoALA) paper echoes this by proposing that robust AI systems, like the human cognitive system, should have core components including Memory. Memory is divided into Working Memory, acting as a short-term scratchpad for immediate context such as recent chat messages or partial solutions, and Long-Term Memory, subdivided into Episodic Memory for records of past events (e.g., 'What happened the last time I tried solution X?'), Semantic Memory for factual knowledge (e.g., 'Birds can fly, except for ostriches'), and Procedural Memory for remembering how to perform tasks, embedded in the agent's code or LLM parameters. Procedures operate above storage to retrieve, manipulate, and apply information for complex actions. Cognitive architectures organize the 'mind' of AI systems for processing, storing, and retrieving information, borrowing ideas from psychology to create thinking systems.

-----

Phase: [EXPLORATION]

### Source [67]: https://mem0.ai/blog/the-modal-model-of-memory-what-ai-agents-can-learn-from-cognitive-science

Query: How does cognitive psychology shape AI agent memory architectures?

Answer: Cognitive psychology's Modal Model of Memory, developed by Atkinson and Shiffrin in 1968 and refined over decades, shapes AI agent memory architectures by providing a working theory of information management: what gets in, kept, durable, and why forgetting occurs. AI memory systems like Mem0 rediscover these principles, implementing intelligent filtering (priority scoring and contextual relevance to decide storage and surfacing, mimicking human subconscious noise filtering before conscious processing), levels-of-processing extraction, four-operation interference management, dynamic forgetting, and layered consolidation (from conversation to session to user memory). This leads to 26% higher accuracy on long-term memory benchmarks, 91% lower retrieval latency, and 90% fewer tokens vs. context-stuffing. Cognitive science predicts that memory processes outperform raw storage, influencing AI to filter before model input for compact, high-signal context.

-----

Phase: [EXPLORATION]

### Source [68]: https://www.longdom.org/open-access/memory-systems-and-artificial-intelligence-linking-human-cognition-and-machine-learning-1099549.html

Query: How does cognitive psychology shape AI agent memory architectures?

Answer: Cognitive psychology categorizes human memory into sensory memory, short-term memory, and long-term memory, each with distinct functions integral to learning, recall, and interaction. As AI evolves, it draws on these principles to enhance learning algorithms, data storage, and retrieval mechanisms, linking human cognition and machine learning by exploring parallels between human memory systems and AI.

-----

Phase: [EXPLORATION]

### Source [69]: https://genesishumanexperience.com/2025/11/03/memory-in-agentic-ai-systems-the-cognitive-architecture-behind-intelligent-collaboration/

Query: How does cognitive psychology shape AI agent memory architectures?

Answer: Cognitive psychology shapes agentic AI memory architectures through concepts like Global Workspace Theory and central executive function in the prefrontal cortex. The Orchestrator maintains Parametric Memory for foundational LLM knowledge, Working Memory for live context (ephemeral scratchpad), and Procedural Memory for rules governing subtasks, mirroring prefrontal integration of sensory, semantic, and episodic cues. Memory routing dynamically invokes types per task, as in Stanford and OpenAI research. Multi-Agent Core enables collaboration via shared memory substrate, paralleling distributed cognition and functioning like neurons in a collective brain with individual and social intelligence.

-----

Phase: [EXPLORATION]

### Source [70]: https://ccn.psych.purdue.edu/papers/cogArch_agent-springer.pdf

Query: How does cognitive psychology shape AI agent memory architectures?

Answer: Psychologically-oriented cognitive architectures, like Soar 9, increase psychological realism by subdividing long-term memory per psychology theory: Procedural Memory for associative rules, Semantic Memory for factual world knowledge (e.g., 'the earth is round'), and Episodic Memory for working memory snapshots (e.g., 'Fido the dog is now...'). These force detailed process specification for computational simulation, aiding clearer theories of cognition and general intelligence, contrasting expert systems by focusing on comprehensive human-like mechanisms rather than narrow scopes.

-----

</details>

<details>
<summary>How has AI memory evolved since early expert systems?</summary>

Phase: [EXPLORATION]

### Source [71]: https://timspark.com/blog/the-journey-of-ai-evolution/

Query: How has AI memory evolved since early expert systems?

Answer: AI memory has evolved from early expert systems, which used a fixed knowledge base of facts and rules without dynamic memory or learning, to modern Limited Memory AI systems. Expert systems from the 1980s, like MYCIN for diagnosing blood infections and DENDRAL for identifying chemical compounds, relied on a static knowledge base and an inference engine that applied rules to known facts to deduce new information. These were brittle and rule-based, with no adaptation or retention beyond the programmed rules. In contrast, today's state-of-the-art AI models, such as ChatGPT or Google Bard, employ short-term memory by remembering earlier parts of a conversation up to a limit, using recent context to predict next words coherently. Virtual assistants like Siri or Alexa maintain context for recent interactions but reset afterward. These systems learn from historical data over a short window into the past and improve over time with more data training, though they lack permanent long-term memory storage for individual conversations.

-----

Phase: [EXPLORATION]

### Source [72]: https://en.wikipedia.org/wiki/Expert_system

Query: How has AI memory evolved since early expert systems?

Answer: Early expert systems, introduced around 1965 by the Stanford Heuristic Programming Project, emulated human expert decision-making through a knowledge base of facts and if-then rules, processed by an inference engine to deduce new facts. They represented knowledge statically rather than through procedural code, with no mention of dynamic memory or learning capabilities. As they evolved, new techniques were incorporated into inference engines, but the core remained rule-based without persistent memory adaptation. These systems marked a shift from prior heuristic methods focused on computational formalisms to knowledge-driven power, as per Edward Feigenbaum. Examples include MYCIN for diagnosing infectious diseases and DENDRAL for organic molecules. They were successful in the 1970s-1980s but were later surpassed by artificial neural networks.

-----

Phase: [EXPLORATION]

### Source [73]: https://medium.com/@gilfoyle_v2/from-the-1950s-to-the-present-day-the-evolution-of-artificial-intelligence-ai-a-historical-6cda272dddd7

Query: How has AI memory evolved since early expert systems?

Answer: Expert systems, prominent from the late 1980s and early 1990s, consisted of a knowledge base with domain-specific information and an inference engine using reasoning like deduction, induction, and abduction to make decisions. They relied on structured data and rules-based logic, lacking the ability to handle unstructured data or maintain adaptive memory. This limitation spurred the 1990s development of natural language processing (NLP) and computer vision to process ambiguous, context-dependent data like text or images, marking a transition from static rule-based 'memory' (knowledge bases) to more dynamic AI approaches. Expert systems demonstrated practical AI applications but paved the way for machine learning and NLP.

-----

Phase: [EXPLORATION]

### Source [74]: https://pub.aimind.so/ai-milestone-series-episode-4-introduction-of-expert-systems-1970s-1980s-f23ae4a179eb

Query: How has AI memory evolved since early expert systems?

Answer: Expert systems emerged in the 1970s-1980s as rule-based systems using if-then-else constructs, inference engines, and domain-specific knowledge bases to simulate human expertise in narrow domains, without general or adaptive memory. Examples include DENDRAL (late 1960s-1970s), which interpreted mass spectrometry data for molecular structures, and MYCIN, a virtual doctor. These systems specialized in complex tasks but did not evolve memory capabilities; they set the stage for later AI technologies integrated into daily life, implying a shift from static knowledge representation to more advanced forms.

-----

Phase: [EXPLORATION]

### Source [75]: https://www.pigro.ai/post/hysory-of-artificial-intelligence-the-1980s

Query: How has AI memory evolved since early expert systems?

Answer: In the 1970s, first-generation expert systems used artificial intelligence methods with Boolean logic and deterministic logical reasoning for specialized domains requiring human expertise, featuring static knowledge handling without dynamic memory. By the late 1970s, second-generation expert systems evolved with the rise of minicomputers, driven by growing documentation needs for organization and consultation tools, indicating progression from rigid first-generation logic to more advanced handling of information, though still rule-based.

-----

</details>

<details>
<summary>What role does memory play in multimodal AI agents?</summary>

Phase: [EXPLORATION]

### Source [76]: https://www.ibm.com/think/topics/ai-agent-memory

Query: What role does memory play in multimodal AI agents?

Answer: AI agent memory refers to an artificial intelligence (AI) system’s ability to store and recall past experiences to improve decision-making, perception and overall performance. Unlike traditional AI models that process each task independently, AI agents with memory can retain context, recognize patterns over time and adapt based on past interactions. This capability is essential for goal-oriented AI applications, where feedback loops, knowledge bases and adaptive learning are required. Short-term memory (STM) enables an AI agent to remember recent inputs for immediate decision-making. This type of memory is useful in conversational AI, where maintaining context across multiple exchanges is required. For example, a chatbot that remembers previous messages within a session can provide coherent responses instead of treating each user input in isolation, improving user experience. For example, OpenAI’s ChatGPT retains chat history within a single session, helping to ensure smoother and more context-aware conversations. Long-term memory (LTM) allows AI agents to store and recall information across different sessions, making them more personalized and intelligent over time. Unlike short-term memory, LTM is designed for permanent storage, often implemented using databases, knowledge graphs or vector embeddings. This type of memory is crucial for AI applications that require historical knowledge, such as personalized assistants and recommendation systems. For example, an AI-powered customer support agent can remember previous interactions with a user and tailor responses accordingly, improving the overall customer experience.

-----

Phase: [EXPLORATION]

### Source [77]: https://huggingface.co/blog/Kseniase/memory

Query: What role does memory play in multimodal AI agents?

Answer: The study demonstrates that this memory-driven approach leads to emergent social behaviors, such as information diffusion, relationship formation, and coordinated activities. However, limitations remain, including potential memory retrieval failures, hallucinations, and biases inherited from the underlying language model. Ultimately, memory serves as the foundation for agent believability, enabling nuanced, dynamic interactions that go beyond single-time-point language model outputs, making generative agents capable of simulating social behavior in interactive applications. Explicit memory is what allows AI to recall facts, rules, and structured knowledge. Within this category, semantic memory is responsible for storing general truths and common knowledge. This is why an AI system can confidently state, “The Eiffel Tower is in Paris,” or “Dogs are mammals.” This type of memory provides the foundation for knowledge-based AI applications, such as search engines and chatbots. Then there’s episodic memory, which is more personal – it captures specific events and experiences, allowing an agent to remember context from past interactions. If a customer service AI recalls that a user previously requested a refund, it can tailor its responses accordingly, making interactions feel more intuitive and human-like.

-----

Phase: [EXPLORATION]

### Source [79]: https://d3.harvard.edu/smarter-memories-stronger-agents-how-selective-recall-boosts-llm-performance/

Query: What role does memory play in multimodal AI agents?

Answer: One of AI agents’ most powerful tools is memory: the ability to learn from the past, adapt to new situations, and improve over time. But as organizations and professionals increasingly deploy AI agents for complex and long-term tasks, an important question emerges: how can we ensure that these systems learn from experience without getting trapped by their past mistakes? In the new paper “How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior,” Himabindu Lakkaraju, Assistant Professor of Business Administration at Harvard Business School and PI in the Trustworthy AI Lab at the Digital Data Design (D^3) Institute at Harvard, and several co-authors delve into the critical role of memory management in LLM agents. Their paper sheds light on how strategic memory management affects agent performance.

-----

Phase: [EXPLORATION]

### Source [80]: https://arxiv.org/html/2505.16067v2

Query: What role does memory play in multimodal AI agents?

Answer: Memory is a critical component in large language model (LLM)-based agents, enabling them to store and retrieve past executions to improve task performance over time. In this paper, we conduct an empirical study on how memory management choices impact the LLM agents’ behavior, especially their long-term performance. Specifically, we focus on two fundamental memory management operations that are widely used by many agent frameworks—memory addition and deletion—to systematically study their impact on the agent behavior. Through our quantitative analysis, we find that LLM agents display an experience-following property: high similarity between a task input and the input in a retrieved memory record often results in highly similar agent outputs. To systematically analyze these phenomena, we conduct controlled experiments across four distinct agents operating on diverse tasks. Crucially, we reveal the critical yet underexplored role of trajectory evaluators in both memory addition and deletion processes, providing novel insights related to effective memory bank optimization that have been significantly overlooked in existing literature.

-----

</details>

<details>
<summary>How is agent memory applied in healthcare personalization?</summary>

Phase: [EXPLORATION]

### Source [81]: https://mem0.ai/usecase/healthcare

Query: How is agent memory applied in healthcare personalization?

Answer: Agent memory in healthcare personalizes care by remembering patient history, including conditions, allergies, medications, and preferences across sessions. It follows ongoing treatment plans, knowing what’s been recommended and what’s been done across visits and agents. For mental health, it supports better conversations by keeping track of past sessions to offer consistent, thoughtful support. It delivers personalized care at scale by adapting responses to the individual, not just the symptom. Features include adaptive conversations that shift tone and suggestions based on patient context and progression. It provides HIPAA-grade compliance with scoped, encrypted memory meeting strict healthcare standards. Memory is modular by design, turnable on per patient, session, or workflow, with real-time recall for instant access to structured context without token-heavy prompts. Problems addressed include disconnected care where patients re-explain issues, no follow-through on treatment plans making chronic care unreliable, and lost progress in therapy sessions.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="a-practical-guide-to-memory-for-autonomous-llm-agents-toward.md">
<details>
<summary>A Practical Guide to Memory for Autonomous LLM Agents</summary>

Phase: [EXPLORATION]

**Source URL:** <https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/>

# A Practical Guide to Memory for Autonomous LLM Agents

Architectures, pitfalls, and patterns that work

[Nick Lawson](https://towardsdatascience.com/author/ccrngd1/)

Apr 17, 2026

14 min read

https://towardsdatascience.com/wp-content/uploads/2026/04/Gemini_Generated_Image_stpvlkstpvlkstpv-scaled-1.jpgGemini-generated image of AI memory

I’ve been running a distributed multi-agent system both in OpenClaw and AWS AgentCore for a while now. In my OpenClaw setup alone, it has a research agent, a writing agent, a simulation engine, a heartbeat scheduler, and several more. They collaborate asynchronously, hand off context through shared files, and maintain state across sessions spanning days or weeks.

When I bring in other agentic systems like Claude Code or the agents I have deployed in AgentCore, coordination, memory, and state all become more difficult to solve for.

Eventually, I came to a realization: most of what makes these agents actually _work_ isn’t the model choice. It’s the memory architecture.

So when I came across [“Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers” (arxiv 2603.07670)](https://arxiv.org/pdf/2603.07670), I was curious whether the formal taxonomy matched what I’d built by feel and iteration. It does, pretty closely. However, it codifies a lot of what I had found on my own and helped me see that some of my current pain points aren’t unique to me and are being seen more broadly.

Let’s walk through the survey and discuss its findings as I share my experiences.

* * *

## Why Memory Matters More Than You Think

The paper leads with an empirical observation that should recalibrate your priorities if it hasn’t already:

> “The gap between ‘has memory’ and ‘does not have memory’ is often larger than the gap between different LLM backbones.”

This is a huge claim. Swapping your underlying model matters less than whether your agent can remember things. I’ve felt this intuitively, but seeing it stated this plainly in a formal survey is useful. Practitioners spend enormous energy on model selection and prompt tuning while treating memory as an afterthought. That’s backward.

The paper frames agent memory inside a Partially Observable Markov Decision Process (POMDP) structure, where memory functions as the agent’s belief state over a partially observable world. That’s a tidy formalization. In practice, it means the agent can’t see everything, so it builds and maintains an internal model of what’s true. Memory is that model. Get it wrong, and every downstream decision degrades.

* * *

## The Write-Manage-Read Loop

The paper characterizes agent memory as a **write-manage-read loop**, not just “store and retrieve.”

- **Write:** New information enters memory (observations, results, reflections)
- **Manage:** Memory is maintained, pruned, compressed, and consolidated
- **Read:** Relevant memory is retrieved and injected into the context

Most implementations I see nail “write” and “read” and completely neglect “manage.” They accumulate without curation. The result is noise, contradiction, and bloated context. Managing is the hard part, and it’s where most systems struggle or outright fail.

Before the most recent OpenClaw enhancements, I was handling this with a heuristic control policy: rules for what to store, what to summarize, when to escalate to long-term memory, and when to let things age out. It’s not elegant, but it forces me to be explicit about the management step rather than ignoring it.

In other systems I build, I often rely on mechanisms such as AgentCore Short/Long-term memory, Vector Databases, and Agent Memory systems. The file-based memory system doesn’t scale well for large, distributed systems (though for agents or chatbots, it’s not off the table).

* * *

## Four Temporal Scopes (And Where I See Them in Practice)

The paper breaks memory into four temporal scopes.

### Working Memory

This is the context window.

It’s ephemeral, high-bandwidth, and limited. Everything lives here briefly. The failure mode is attentional dilution and the “lost in the middle” effect, where relevant content gets ignored because the window is too crowded. I’ve hit this, as have most of the teams I’ve worked with.

When OpenClaw, Claude Code, or your chatbot context gets long, agent behavior degrades in ways that are hard to debug because the model technically “has” the information but isn’t using it. The most common thing I see from teams (and myself) is to create new threads for different chunks of work. You don’t keep Claude Code open all day while working on 20+ different JIRA tasks; it degrades over time and performs poorly.

### Episodic Memory

This captures concrete experiences; what happened, when, and in what sequence.

In my OpenClaw instance, this is the daily standup logs. Each agent writes a brief summary of what it did, what it found, and what it escalated. These accumulate as a searchable timeline. The practical value is enormous: agents can look back at yesterday’s work, spot patterns, and avoid repeating failures. Tools like Claude Code struggle, unless you set up instructions to force the behavior.

Production agents can leverage things like Agent Core’s short-term memory to keep these episodic memories. There are even mechanisms to understand what deserves to be persisted beyond a single interaction.

The paper validates this as a distinct and important tier.

### Semantic Memory

Is responsible for abstracted, distilled knowledge, facts, heuristics, and learned conclusions.

In my OpenClaw, this is the MEMORY.md file in each agent’s workspace. It’s curated. Not everything goes in. The agent (or I, periodically) decides what’s worth preserving as a lasting truth versus what was situational.

In Agent Core Memory, this is primarily the Long-term memory feature.

This curation step is critical; without it, semantic memory becomes a junk drawer.

### Procedural Memory

It is encoded executable skills, behavioral patterns, and learned behavior.

In OpenClaw, this maps mostly to the AGENTS.md and SOUL.md files, which contain persona instructions, behavioral constraints, and escalation rules. When the agent reads these at the start of the session, it’s loading procedural memory. These should be updated based on user feedback, or even through ‘dream’ processes that analyze interactions.

This is an area that I’ve been remiss in (as have teams that I’ve worked with). I spend time tuning a prompt, but the feedback mechanisms that drive the storage of procedural memory and the iteration on these personas often get left out.

The paper formalizes this as a distinct tier, which I found validating. These aren’t just system prompts. They’re a form of long-term learned behavior that shapes every action.

* * *

## Five Mechanism Families

Now that we have some common definitions around the types of memories, let’s dive into memory mechanisms.

### Context-Resident Compression

This covers sliding windows, rolling summaries, and hierarchical compression. These are the “stay in context” strategies. Rolling summaries are seductive because they feel clean (they’re not, I’ll get to why in a moment).

I’m sure everyone has run into Claude Code or Kiro CLI compressing a conversation when it gets too large for the context window. Oftentimes, you’re better off restarting a new thread.

### Retrieval-Augmented Stores

This is RAG applied to agent interaction history rather than static documents. The agent embeds past observations and retrieves by similarity. This is powerful for long-running agents with deep history, but retrieval quality becomes a bottleneck fast. If your embeddings don’t capture semantic intent well, you’ll miss relevant memories and surface stale ones.

You also run into issues where questions like ‘what happened last Monday’ don’t retrieve quality memories.

#### Reflective Self-Improvement

This includes systems such as [Reflexion](https://www.promptingguide.ai/techniques/reflexion) and [ExpeL](https://github.com/LeapLabTHU/ExpeL), where agents write verbal post-mortems and store conclusions for future runs. The idea is compelling; agents learn from mistakes and improve. The failure mode is severe, though (we will cover it in more detail in a minute).

I believe other ‘dream’ based reflection and systems like the [Google Memory Agent](https://towardsdatascience.com/i-replaced-vector-dbs-with-googles-memory-agent-pattern-for-my-notes-in-obsidian/) pattern belong to this class as well.

### Hierarchical Virtual Context

A [MemGPT’s](https://arxiv.org/abs/2310.08560) OS-inspired architecture ( [see GitHub repo also](https://github.com/deductive-ai/MemGPT)). A main context window is “RAM”, a recall database is the “disk”, and archival storage is “cold storage”, while the agent manages its own paging. While this category is interesting, the overhead/work of maintaining these separate tiers is burdensome and tends to fail.

The MemGPT paper and git repo are both almost 3 years old, and I have yet to see any actual use in production.

### Policy-Learned Management

This is a new frontier approach, where RL-trained operators (such as store, retrieve, update, summarize, and discard) that models learn to invoke optimally. I think there is a lot of promise here, but I haven’t seen real harnesses for builders to use or any actual production use.

* * *

## Failure Modes

We’ve covered the types of memories and the systems that make them. Next is how these can fail.

### Context-Resident Failures

**Summarization drift** occurs when you repeatedly compress history to fit it within a context window. Each compression/summarization throws away details, and eventually, you’re left with memory that doesn’t really match what happened. Again, you see this Claude Code and Kiro CLI when coding sessions cover too many features without creating new threads. One way I’ve seen teams combat this is to keep raw memories linked to the summarized/consolidated memories.

**Attention dilution** is the other failure mode in this category. Even if you can keep everything in context (as with the new 1 million-token windows), larger prompts “lose” information in the middle. While agents technically have all the memories, they can’t focus on the right parts at the right time.

### Retrieval Failures

**Semantic vs. causal mismatch** occurs when similarity searches return memories that seem related but aren’t. Embeddings are great at determining when text ‘look like’ each other, but are terrible with knowing ‘this is the cause’. In practice, I often see this when debugging through coding assistants. They see similar errors but can miss the underlying cause, which often leads to thrashing/churning, a lot of changes, but never fixes the real issue.

**Memory blindness** occurs in tiered systems when important facts never resurface. The data exists, but the agent never sees it again. This can be because a sliding window has moved on, because you only retrieve 10 memories from a data source, but what you need would have been the 11th memory.

**Silent orchestration failures** are the most dangerous in this category. Paging, eviction, or archival policies do the wrong things, but no errors are thrown (or are lost in the noise by the autonomous system or by humans running it). The only symptom will be that responses get worse, get more generic, and get less grounded. While I’ve seen this arise in several ways, the most recent for me was when OpenClaw failed to write daily memory files, so daily stand-ups/summarizations had nothing to do. I only noticed because it kept forgetting things we worked on during those days.

### Knowledge-Integrity Failures

**Staleness** is probably most common. The outside world changes, but your system memory doesn’t. Addresses, device states, user preferences, and anything that your system relies on to make decisions can drift over time. Long-lived agents will act on data from 2024 even in 2026 (who hasn’t seen an LLM insist the date is wrong, the wrong President is in office, or that the latest technology hasn’t actually hit the scene yet?).

**Self-reinforcing errors** (confirmation loops) occur when a system treats a memory as ground truth, but that memory is wrong. While you generally want systems to learn and build a new basis of truth, if a system creates a bad memory, its view of the world is affected. In my OpenClaw instance, it decided that my SmartThings integration with my Home Assistant was faulty; therefore, all information from a SmartThings device was deemed erroneous, and it ignored everything from it (in fact, there were just a few dead batteries in my system).

**Over-generalization** is a quieter version of self-reinforcement. Agents learn a lesson in a narrow context, then apply it everywhere. A workaround for a single customer or a single error is a default pattern.

### Environmental Failure

**Contradiction** handling can be incredibly frustrating. As new information is collected, if it conflicts with existing information, systems can’t always determine the actual truth. In my OpenClaw system, I asked it to create some N8N workflows. They all created correctly, but the action timed out, so it thought it failed. I verified the workflows existed, told my OpenClaw agent to remember it, and it agreed. For the next several interactions, the agent oscillated between believing the workflow was available and believing it had failed to set up.

* * *

## Design Tensions

There is going to be push-and-pull against all these for agents and memory systems.

### Utility vs. Efficiency

Better memory usually means more tokens, more latency, more storage, more systems.

### Utility vs. Adaptivity

Memory that is useful now will be stale at some point. Updating is expensive and risky.

### Adaptivity vs. Faithfulness

The more you update, revise, and compress, the more you risk distorting what actually happened.

### Faithfulness vs. Governance

Accurate memory may contain sensitive information (PHI, PII, etc) that you may be required to delete, obfuscate, or protect.

### All of the above vs. Governance

Enterprises have complex compliance requirements that can conflict with all these.

* * *

## Practical Takeaways for Builders

I’m often asked by engineering teams for the best memory system or where they should start their journey. Here’s what I say.

### Start with explicit temporal scopes

Don’t build “memory”. When you need episodic memory, build it. When your use case grows and needs semantic memory, build it. Don’t try to find one system that does it all, and don’t build every form of memory before you need it.

### Take the management step seriously

Plan how to maintain your memory. Don’t plan on accumulating indefinitely; figure out if you need compression or memory connection/dream behavior. How will you know what goes into semantic memory versus RAG memory? How do you handle updates? Without knowing these, you’ll accumulate noise, get contradictions, and your system will degrade.

### Keep raw episodic records

Don’t just rely on summaries; they can drift or lose details. Raw records let you return to what actually happened and pull them in when necessary.

### Version reflective memory

To help avoid contradictions in summaries, long-term memories, and compressions, add timestamps or versions to each. This can help your agents determine what is true and what is the most accurate reflection of the system.

### Treat procedural memory as code

In OpenClaw, your Agents.MD, Memory.MD, personal files, and behavioral configs are all part of your memory architecture. Review them and keep them under source control so you can examine what changes and when. This is especially important if your autonomous system can alter these based on feedback.

* * *

## Wrapup

The write-manage-read framing is the most useful takeaway from this paper. It’s simple, it’s complete, and it forces you to think about all three phases instead of just “store stuff, retrieve stuff.”

The taxonomy maps surprisingly well to what I built in OpenClaw through iteration and frustration. That’s either validating or humbling, depending on how you look at it (probably both.) The paper formalizes patterns that practitioners have been discovering independently, which is what a good survey should do.

The open problems section is honest about how much is unsolved. Evaluation is still primitive. Governance is mostly ignored in practice. Policy-learned management is promising but immature. There’s a lot of runway here.

Memory is where the real differentiation happens in agent systems. Not the model, not the prompts. The memory architecture. The paper gives you a vocabulary and a framework to think more clearly about it.

## About

Nicholaus Lawson is a Solution Architect with a background in software engineering and AIML. He has worked across many verticals, including Industrial Automation, Health Care, Financial Services, and Software companies, from start-ups to large enterprises.

This article and any opinions expressed by Nicholaus are his own and not a reflection of his current, past, or future employers or any of his colleagues or affiliates.

Feel free to connect with Nicholaus via LinkedIn at [https://www.linkedin.com/in/nicholaus-lawson/](https://www.linkedin.com/in/nicholaus-lawson/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="agent-memory-architectures-5-patterns-and-trade-offs.md">
<details>
<summary>Agent Memory Architectures: Patterns and Trade-offs (2026)</summary>

Phase: [EXPLORATION]

**Source URL:** <https://atlan.com/know/agent-memory-architectures/>

# Agent Memory Architectures: Patterns and Trade-offs (2026)

## Key takeaways

- Five architecture patterns escalate from in-process (zero infrastructure) to an enterprise context layer (full governance).
- Full-context in-process achieves 72.9% accuracy at 17.12s p95; flat vector drops to 66.9% at 1.44s, a 91% speed gain.
- Most enterprise deployments compose multiple patterns: working memory, external retrieval, and an enterprise context layer.
- Larger context windows don't resolve the governance problem; accuracy/latency and governance/freshness axes are independent.

## What are agent memory architectures?

> An agent memory architecture is the combination of storage substrates, retrieval mechanisms, and agent control logic that determines what an AI agent can remember, when it can access that information, and how persistent that information is across sessions. Architecture choices, not just memory type choices, determine whether an agent can answer multi-hop questions, maintain cross-session continuity, or meet enterprise governance requirements. Memory type is the content; architecture is the system that stores and retrieves it.

Five distinct [agent memory architecture](https://atlan.com/know/memory-layer-for-ai-agents/) patterns exist in production in 2026, ranging from zero-infrastructure to full enterprise governance — including Pattern 5, the enterprise context layer, which [Atlan](https://atlan.com/know/what-is-context-layer/) implements for governed organizational memory. Understanding them requires separating two concepts that practitioners often conflate: memory _types_ and memory _architectures_.

Memory types (episodic, semantic, procedural, and working) describe the _content_ being stored. [Types of AI agent memory](https://atlan.com/know/types-of-ai-agent-memory/) is a taxonomy of what. Memory architecture is the _system design_: how storage substrates, retrieval mechanisms, and agent control logic are assembled to store, access, and manage that content. The CoALA framework (Sumers et al., arXiv:2309.02427) formalizes this distinction; conflating the two is the most common source of practitioner confusion.

An architecture pattern specifies three things: (1) the storage substrate (context window, vector database, relational database, knowledge graph, or governed metadata catalog); (2) the retrieval mechanism (full-context injection, top-k semantic search, graph traversal, or function call); and (3) the agent control model (whether the agent passively receives injected context or actively manages its own memory).

Two independent axes determine which pattern fits your needs.

**Accuracy vs. latency.** Higher accuracy generally requires more context or more complex retrieval. The Mem0 LOCOMO benchmark (arXiv:2504.19413, 2026) quantifies the trade-off: full-context in-process achieves 72.9% accuracy at 17.12s p95 latency, while selective external memory drops to 66.9% accuracy but cuts latency to 1.44s, a 91% speed gain at 6-point accuracy cost, with a 90% reduction in token cost (~26,031 tokens vs. ~1,764 per conversation).

**Governance vs. freshness.** Unstructured memory (vectors, raw text) is easy to populate but impossible to govern. Governed memory (metadata catalog, knowledge graph with temporal edges) is accurate and auditable but requires upfront investment. Crucially, expanding context windows (models now support up to 2M tokens) shift the accuracy/latency trade-off but do not resolve the governance problem. The two axes are independent.

| Dimension | Data |
| --- | --- |
| Number of distinct patterns | 5 (from simplest to full enterprise) |
| Fastest pattern (latency) | Flat external vector store: 1.44s p95 (Mem0 LOCOMO benchmark, 2026) |
| Most accurate pattern (standalone) | In-process / working-only: 72.9% accuracy (LOCOMO, 2026) |
| Token cost difference | Full-context: ~26,031 tokens/conversation vs. selective: ~1,764 (90% reduction) |
| Enterprise accuracy uplift | 3x text-to-SQL improvement with live metadata vs. bare schema (Atlan/Snowflake) |
| Graph memory status | Production by early 2026; 13 frameworks now support graph memory integrations |

## The five agent memory architecture patterns

> The five patterns escalate in complexity and capability from simplest (zero infrastructure, everything in the context window) to most enterprise-capable (the organization’s existing governed metadata graph as agent memory). Each pattern reflects a different primary constraint: token cost, latency, relational complexity, temporal validity, or governance. Most production systems combine two or more of these patterns.

The five patterns escalate in complexity and capability from simplest (no infrastructure, everything in the context window) to most enterprise-capable (the organization’s existing governed metadata graph as agent memory). Most production systems combine two or more of these patterns.

### Pattern 1: In-process / working-only

The agent operates entirely within the LLM context window. All memory is the prompt: system instructions, conversation history, and any retrieved chunks loaded at inference time. Session ends, memory ends. There is no persistent external storage and no memory framework required.

**Storage substrate:** LLM context window (GPT-4o, Claude, Gemini). **Retrieval mechanism:** none; full content is injected at inference time. **Agent control model:** passive recipient.

On the Mem0 LOCOMO benchmark (arXiv:2504.19413), Pattern 1 achieves **72.9% accuracy** at **17.12s p95 latency**, consuming ~26,031 tokens per conversation. The “lost in the middle” effect (Liu et al., 2024) means LLM accuracy degrades when relevant information sits in the middle of a long context rather than at boundaries, making the raw accuracy figure optimistic for very long conversations.

**Use Pattern 1 when:** you need stateless single-turn tasks (document summarization, code generation from a complete spec), prototypes and proofs of concept, or tasks requiring strict privacy isolation between runs. See [in-context vs. external memory](https://atlan.com/know/in-context-vs-external-memory-ai-agents/) for a full comparison.

**Do not use Pattern 1 when:** cross-session continuity is required, token cost is a constraint, or context exceeds ~50% of the window limit.

| | |
| --- | --- |
| **Pros** | Zero infrastructure, zero retrieval latency overhead, maximum coherence (model sees all facts simultaneously), no retrieval misses |
| **Cons** | Linear token cost scaling, no cross-session continuity, 17.12s p95 latency, 14.7x more expensive per conversation than selective memory |

### Pattern 2: Flat external vector store

A single external vector database stores conversation history and knowledge as embeddings. At query time, the agent retrieves the top-k semantically similar chunks and injects them into the context window. All memories live in one flat namespace with no internal structure beyond similarity distance.

**Storage substrate:** Pinecone, Qdrant, Chroma, pgvector. **Retrieval mechanism:** cosine/ANN semantic similarity search. **Agent control model:** passive; retrieval happens automatically before each response.

Pattern 2 achieves **66.9% accuracy** at **1.44s p95 latency** (Mem0 LOCOMO benchmark), with a 90% token reduction vs. full-context (~1,764 tokens per conversation). The flat namespace is the key limitation: a fact from six months ago and a fact from yesterday occupy the same similarity space. Multi-hop traversal fails; vector similarity cannot answer “who owns this table, and has ownership changed since the audit?” Key tools: [Mem0, Letta, Zep and other frameworks](https://atlan.com/know/best-ai-agent-memory-frameworks-2026/) in vector-only mode.

**Use Pattern 2 when:** you need conversational agents with cross-session recall, large unstructured knowledge bases (documentation, support tickets), or user personalization.

**Do not use Pattern 2 when:** queries require relational traversal, temporal accuracy matters, or governance at the retrieval layer is required.

| | |
| --- | --- |
| **Pros** | Simple to implement, no cold-start problem, strong for fuzzy semantic search, 90% token reduction vs. Pattern 1 |
| **Cons** | Flat namespace with no temporal awareness, multi-hop queries fail, no governance or access control at retrieval layer |

### Pattern 3: Tiered memory (episodic + semantic stores)

Memory splits across multiple stores by type and access pattern, modeled on human memory and OS memory hierarchy. The canonical implementation is MemGPT/Letta (arXiv:2310.08560), which uses three tiers:

- **Core memory (hot):** always in-context, like RAM. Stores user profile, agent persona, and active task state.
- **Recall memory (warm):** searchable conversation history, like disk cache. Stores recent episodic experiences.
- **Archival memory (cold):** long-term vector store, like cold storage. Stores compressed past interactions.

The critical distinction from Pattern 2: agents actively manage their own memory through function calls. They decide what to retain, summarize, or archive; they are not passive recipients of injected context. Generative Agents (Park et al., arXiv:2304.03442) extends this with a memory stream and reflection architecture, where agents synthesize episodic experiences into general semantic knowledge over time.

The warm/cold split enables compliance archiving without polluting active retrieval, a meaningful advantage for any agent operating under retention requirements.

**Use Pattern 3 when:** you need agents requiring both immediate session coherence and long-horizon continuity, or token-constrained deployments that must prioritize what stays in-context.

**Do not use Pattern 3 when:** you need simple stateless tasks (over-engineered for single-turn use); or when memory-management overhead adds unacceptable latency.

| | |
| --- | --- |
| **Pros** | Mirrors human memory consolidation, agents actively manage retention, handles long-horizon reasoning, enables episodic-to-semantic transformation |
| **Cons** | More infrastructure than flat vector store, requires agent self-management logic, harder to debug, consolidation can lose nuance |

### Pattern 4: Knowledge graph + vector hybrid

Vector embeddings handle broad semantic entry-point retrieval; a knowledge graph handles multi-hop relational reasoning. The two systems are complementary: vectors surface what is topically relevant, the graph reveals how entities relate. This is the [vector store vs. knowledge graph](https://atlan.com/know/vector-database-vs-knowledge-graph-agent-memory/) combination that addresses queries neither system can handle alone.

Temporal knowledge graphs (Zep/Graphiti) extend Pattern 4 with time-aware edges, enabling “what was true when” queries with sub-50ms retrieval for direct lookups. Actor-aware variants tag each memory with its source agent, preventing cross-agent contamination in multi-agent systems. The result is a [context graph](https://atlan.com/know/what-is-a-context-graph/) that tracks not just what is known but when it became known and who recorded it.

On the LOCOMO benchmark, graph-enhanced memory achieves **68.4% accuracy at 2.59s p95** (Mem0g variant), better relational performance than flat vector at a modest latency cost. Graph memory moved from experimental to **production** by early 2026; 13 agent frameworks now support graph memory integrations (Mem0 State of Memory 2026). OSS Insight’s analysis of the code-review-graph project found 6.8x token reduction on code reviews using GraphRAG. The MAGMA paper (January 2026) signals the next evolution: multi-graph topologies where different relationship types occupy separate graphs.

**Use Pattern 4 when:** you have structured domains with entity relationships (financial records, legal documents, codebase dependencies); multi-hop queries; temporal validity requirements; or multi-agent actor attribution needs.

**Do not use Pattern 4 when:** the graph is cold (requires pre-population via entity extraction pipelines); or when domain schema is highly volatile (rigid schema breaks easily).

| | |
| --- | --- |
| **Pros** | Enables precise multi-hop traversal, temporal awareness prevents stale-fact failures, actor attribution prevents multi-agent poisoning, 68.4% LOCOMO accuracy |
| **Cons** | Significant implementation complexity, cold-start problem, more expensive to maintain, rigid schema can break as domain evolves |

### Pattern 5: Enterprise context layer

A governed, continuously maintained metadata graph serves as the agent’s long-term semantic and organizational memory. The key distinction: Pattern 5 does not extract definitions into a bespoke memory system. It connects agents directly to the organization’s existing governed data catalog. This is the [context layer](https://atlan.com/know/what-is-context-layer/) that chatbot-centric frameworks cannot provide.

Five components define an enterprise context layer as [agent memory architecture](https://atlan.com/know/agent-context-layer/):

1. **Semantic authority layer** — canonical metric definitions and entity resolution (resolving “customer” in Salesforce = “account” in Stripe)
2. **Active ontology** — entity relationships maintained live from source systems, not extracted snapshots
3. **Governance enforcement** — access policies enforced at inference time, not just retrieval time
4. **Provenance and lineage** — column-level transformation history making agent answers auditable
5. **Decision memory** — organizational intent captured through human corrections and active metadata, compounding over time

Unlike Patterns 1–4, which address _agent memory_ (what the agent experienced), Pattern 5 addresses _organizational memory_ (what the organization knows, governed and certified). EU AI Act requirements around data provenance extend to what AI agents remember; building memory without governance creates a compliance liability (arXiv:2603.17787).

Production deployments include Mastercard (100M+ assets), CME Group (18M assets, 1,300+ glossary terms), and Workday, where adding a semantic metadata layer produced a 3x improvement in text-to-SQL accuracy vs. bare schemas (Atlan/Snowflake joint research).

**Use Pattern 5 when:** you have multi-agent data workflows spanning multiple platforms; regulated industries requiring audit trails; or any deployment where a stale or incorrect definition triggers a compliance failure. Requires an existing governed data catalog.

**Do not use Pattern 5 when:** no governed data catalog exists; or agents operate outside structured enterprise data estates.

| | |
| --- | --- |
| **Pros** | Inherits governance by design, prevents synchronization drift, enables multi-agent consistency, makes agent responses fully auditable with lineage |
| **Cons** | Requires existing governed data catalog, high organizational complexity, not viable as greenfield build for a single agent |

## Architecture trade-off comparison

> No pattern is universally superior. The right architecture depends on whether your primary constraint is token cost, latency, accuracy, relational complexity, or governance. Five dimensions — accuracy, latency, token cost, governance, and multi-agent support — separate the patterns clearly. Most production enterprise deployments ultimately combine two or more patterns across all five dimensions.

The right architecture for your [AI memory system](https://atlan.com/know/ai-memory-system/) depends on your primary constraint: token cost, latency, accuracy, relational complexity, or governance. No pattern is universally superior, and most production enterprise deployments ultimately combine two or more. Refer to [how to choose an AI agent memory architecture](https://atlan.com/know/how-to-choose-ai-agent-memory-architecture/) for a decision guide once you understand the pattern space.

| Dimension | P1: In-Process | P2: Flat Vector | P3: Tiered | P4: Graph Hybrid | P5: Enterprise Context |
| --- | --- | --- | --- | --- | --- |
| **Accuracy** | 72.9% (LOCOMO) | 66.9% (LOCOMO) | Not separately benchmarked | 68.4% (Mem0g) | 3x SQL uplift; 20% accuracy improvement with ontology layer |
| **Latency (p95)** | 17.12s | 1.44s | Moderate (adds tier management overhead) | 2.59s | Sub-50ms for direct lookups |
| **Token cost** | Very high (~26K/conversation) | Low (~1.7K/conversation, 90% reduction) | Low-moderate (only core tier in-context) | Low-moderate | Low (targeted retrieval) |
| **Governance** | None | None (flat namespace) | Low-moderate (warm/cold split) | Moderate (temporal edges, actor tags) | High (lineage, policies, certification) |
| **Freshness** | As fresh as the prompt | As fresh as last embed | As fresh as last consolidation | Near real-time (Zep) | Live (continuous metadata sync) |
| **Multi-agent support** | Poor (no shared memory) | Moderate (shared namespace, no actor attribution) | Moderate (shared archival tier) | Good (actor-attributed edges) | Excellent (canonical shared layer) |
| **Enterprise readiness** | Low | Low | Moderate | Moderate-high | High |
| **Implementation complexity** | None | Low | Moderate | High | Very high (requires existing catalog) |

**Decision matrix:**

- **Pattern 1:** Single-turn tasks; proofs of concept; privacy-isolated runs; static small knowledge bases
- **Pattern 2:** Multi-session conversational agents; large unstructured knowledge bases; user personalization; when fuzzy search is sufficient
- **Pattern 3:** Long-horizon agents needing both session coherence and continuity; research/reasoning agents; token-constrained deployments
- **Pattern 4:** Structured domains with entity relationships; multi-hop queries; temporal validity matters; multi-agent actor attribution required
- **Pattern 5:** Multi-platform enterprise workflows; regulated industries; deployments where definition accuracy has compliance consequences; organizations with existing governed catalogs

## How architecture patterns compose

> Real production deployments do not use a single pattern in isolation. Most combine working memory (Pattern 1 elements) with external retrieval (Pattern 2 or 3) and, in enterprise settings, an enterprise context layer (Pattern 5). The patterns are layers, not alternatives — each addresses a different layer of what an agent needs to know and remember.

Real production deployments do not use a single pattern in isolation. Most combine working memory (Pattern 1 elements) with external retrieval (Pattern 2 or 3) and, in enterprise settings, an [enterprise context layer as memory foundation](https://atlan.com/know/context-layer-as-ai-memory-foundation/). The patterns are layers, not alternatives.

The most common production combination in 2026: Pattern 2 (flat vector) or Pattern 3 (tiered) as the agent’s experiential memory, plus Pattern 5 (enterprise context layer) as the organization’s semantic authority. Pattern 4 (knowledge graph) typically augments or replaces Pattern 2’s retrieval layer in structured domains, rather than replacing the full stack.

The complete layered model, from most persistent to most immediate:

1. **Working memory (Pattern 1 elements)** — what the agent is actively processing right now (context window)
2. **Episodic/experiential memory (Pattern 2 or 3)** — what this agent or user has experienced (vector store or tiered system)
3. **Semantic/relational memory (Pattern 4)** — structured entity relationships and temporal facts (knowledge graph)
4. **Organizational memory (Pattern 5)** — what the organization has formally defined, governed, and certified (enterprise context layer)

The agent draws from all four layers simultaneously, with each layer contributing a different category of knowledge. Practitioner community consensus from HN and Reddit confirms this multi-layer reality: “The four architectural camps haven’t subsumed each other” (OSS Insight 2026). The academic framing from Multi-Agent Memory from a Computer Architecture Perspective (arXiv:2603.10062) proposes a formal three-layer hierarchy and identifies cross-layer consistency as the most pressing open challenge.

Understanding this layering changes how you evaluate each pattern. Pattern 1 (in-process) is not a complete alternative to Pattern 2; it is working memory that sits on top of any external layer. Pattern 4 (knowledge graph) is not a replacement for Pattern 2; it adds relational reasoning on top of semantic retrieval. And Pattern 5 (enterprise context layer) is not an alternative to Patterns 2–4; it is the organizational foundation that makes all upper layers trustworthy. Your team should evaluate which layers you already have and which are missing, not which single pattern to adopt.

## How Atlan fits into agent memory architecture

> Atlan implements Pattern 5 — the enterprise context layer — providing the governed metadata graph that Patterns 1–4 cannot supply. Where chatbot-centric memory frameworks address what an agent experienced, Atlan addresses what the organization knows: governed metric definitions, live entity relationships, access policies, and column-level lineage. The two concerns are complementary layers, not competing products.

Atlan implements Pattern 5 — the enterprise context layer — providing the governed metadata graph that Patterns 1–4 cannot supply. Where chatbot-centric memory frameworks address what an agent experienced, Atlan addresses what the organization knows. The two concerns are complementary, not competing.

Patterns 1–4 all assume that the data feeding agent memory is unstructured and ungoverned: conversation logs, document embeddings, extracted entities. In enterprise data workflows, the memory problem is different: agents need to know what “revenue” means and whose definition governs, which table is the source of truth, and whether a metric definition changed after the last audit.

Even Pattern 4 (knowledge graph) requires an extraction pipeline: definitions must be pulled from source systems, converted into graph nodes, and kept in sync. Synchronization drift, where the extracted copy diverges from the live governed source, is the failure mode. EU AI Act requirements around data provenance extend to what AI agents remember; building memory without governance is building a compliance liability (arXiv:2603.17787).

Atlan connects agents directly to the organization’s existing governed metadata graph — no extraction pipeline, no synchronization drift. The five context layer components (semantic authority, active ontology, governance enforcement, lineage/provenance, decision memory) map directly to the requirements that Patterns 1–4 cannot address. Atlan works as a composable layer alongside existing agent memory infrastructure: your team can use Pattern 2 or 3 for experiential memory and Atlan for organizational semantic memory simultaneously.

The production evidence:

- **3x text-to-SQL accuracy improvement** when agents use a live metadata layer vs. bare schemas (Atlan/Snowflake joint research)
- **20% improvement in agent answer accuracy** with ontology layer added (Atlan internal data)
- **39% reduction in tool calls** with ontology layer (Atlan internal data)
- **37% of multi-agent failures** attributed to interagent misalignment, addressed by canonical shared context layer (Atlan research)
- **Mastercard:** 100M+ assets under governed context
- **CME Group:** 18M assets, 1,300+ glossary terms providing semantic authority to enterprise agents

## Real stories from real customers: context layer as enterprise agent memory

Workday and DigiKey represent two ends of the enterprise deployment spectrum — one building AI governance architecture from the ground up alongside Atlan, the other activating a full context operating system across the data estate.

"We're excited to build the future of AI governance with Atlan. All of the work that we did to get to a shared language at Workday can be leveraged by AI via Atlan's MCP server…as part of Atlan's AI Labs, we're co-building the semantic layer that AI needs with new constructs, like context products."

Joe DosSantos, VP of Enterprise Data & Analytics, Workday

https://website-assets.atlan.com/img/client-logos/workday-logo-1.svg

"Atlan is much more than a catalog of catalogs. It's more of a context operating system…Atlan enabled us to easily activate metadata for everything from discovery in the marketplace to AI governance to data quality to an MCP server delivering context to AI models."

Sridher Arumugham, Chief Data & Analytics Officer, DigiKey

https://website-assets.atlan.com/img/regovern-2025/digikey-logo.svg

## Five patterns, one architecture decision: what this means for your team

The five agent memory architecture patterns are not a menu; they are a progression. Most enterprise AI deployments eventually use all four layers: working memory for active processing, experiential memory for what this agent has learned, relational memory for entity traversal, and organizational memory for governed semantic authority. The question is not which pattern to choose, but which patterns your current use case requires and which gaps remain.

Context window growth changes Pattern 1’s cost curve but does not eliminate the governance problem. The accuracy/latency and governance/freshness axes are independent; solving one does not solve the other. Pattern 5 exists precisely because the enterprise memory problem is not a retrieval problem. It is a semantic authority problem: agents need to know what the organization has formally decided, not just what text is topically similar.

Teams building data agents in 2026 should audit their current stack against the five patterns and identify which layer is missing. For most enterprise deployments, the missing layer is Pattern 5 — the organizational memory that chatbot-centric frameworks were never designed to provide.

## FAQs

### 1\. What are the different types of memory in AI agents?

Two taxonomies apply: memory types and memory architectures. Memory types describe content — episodic (events), semantic (facts), procedural (rules), and working (active processing). Memory architectures describe how systems store and retrieve that content — the five patterns on this page. Types describe what; architectures describe how. The CoALA framework (Sumers et al., arXiv:2309.02427) formalizes this distinction.

### 2\. How does in-context memory differ from external memory in AI agents?

In-context memory (Pattern 1) keeps information in the LLM context window. External memory (Patterns 2-5) stores it outside the model in vector databases, knowledge graphs, or governed metadata catalogs. Mem0’s LOCOMO benchmark shows the trade-off: in-context reached 72.9% at 17.12s p95, while selective retrieval reached 66.9% at 1.44s with 90% fewer tokens.

### 3\. What is tiered memory architecture for AI agents?

Tiered memory (Pattern 3) splits memory across multiple stores by type and access frequency, modeled on OS memory hierarchy. The canonical MemGPT/Letta implementation (arXiv:2310.08560) uses three tiers: core memory (always in-context, like RAM), recall memory (searchable conversation history, like disk cache), and archival memory (long-term vector store, like cold storage). Agents actively manage their own tier assignments through explicit function calls — they decide what to retain, summarize, or archive rather than passively receiving injected context.

### 4\. When should I use a knowledge graph instead of a vector store for agent memory?

Use a knowledge graph (Pattern 4) when queries require multi-hop relational traversal, temporal validity matters (“what was true when”), or actor attribution is needed in multi-agent systems to prevent cross-agent contamination. Use a flat vector store (Pattern 2) when fuzzy semantic search is sufficient and queries are not relational. The LOCOMO benchmark shows graph-enhanced memory at 68.4% accuracy / 2.59s p95 vs. flat vector at 66.9% / 1.44s — better relational performance at a modest latency cost.

### 5\. How does MemGPT / Letta architecture manage agent memory?

MemGPT (now Letta) uses an OS-inspired model where agents issue explicit function calls to manage their own memory tiers. Core memory is a small fixed-size block always in-context. Recall memory is searchable recent conversation history. Archival memory is the long-term cold store. When core memory fills, the agent writes to archival; when it needs old information, it retrieves from recall or archival. This is Pattern 3 — tiered memory with active agent self-management rather than passive context injection.

### 6\. What is the difference between agent memory and a context layer?

Agent memory (Patterns 1-4) captures what an agent or user has experienced: conversation history, past decisions, and extracted facts. A context layer (Pattern 5) captures what the organization knows: governed metric definitions, live entity relationships, and data lineage. They are complementary layers; an enterprise context layer such as Atlan serves as canonical semantic authority.

### 7\. How do multi-agent systems share memory without conflicts?

Three approaches: (1) a shared flat vector namespace (Pattern 2), which is simple but lacks actor attribution; (2) actor-attributed knowledge graph edges (Pattern 4), which tag each memory with its source agent; and (3) a canonical shared context layer (Pattern 5), such as Atlan, which gives all agents the same governed source. Atlan research attributes 37% of multi-agent failures to interagent misalignment.

### 8\. What is the most accurate architecture for AI agent memory?

In-process / working-only (Pattern 1) achieves the highest raw recall accuracy at 72.9% on the LOCOMO benchmark, because the model sees all facts simultaneously with no retrieval misses. However, accuracy type matters: for enterprise structured queries, Pattern 5 produces a 3x improvement in text-to-SQL accuracy when agents use live metadata vs. bare schemas. The most accurate architecture depends on what type of accuracy matters — recall accuracy on conversational tasks (Pattern 1 wins) or domain accuracy on structured enterprise queries (Pattern 5 wins).

## Sources

01. [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory, arXiv](https://arxiv.org/pdf/2504.19413)
02. [State of AI Agent Memory 2026, Mem0](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
03. [CoALA: Cognitive Architectures for Language Agents, arXiv](https://arxiv.org/abs/2309.02427)
04. [MemGPT: Towards LLMs as Operating Systems, arXiv](https://arxiv.org/abs/2310.08560)
05. [Generative Agents: Interactive Simulacra of Human Behavior, arXiv](https://arxiv.org/abs/2304.03442)
06. [Governed Memory: A Production Architecture for Multi-Agent Workflows, arXiv](https://arxiv.org/html/2603.17787)
07. [Multi-Agent Memory from a Computer Architecture Perspective, arXiv](https://arxiv.org/html/2603.10062v1)
08. [The Agent Memory Race of 2026, OSS Insight](https://ossinsight.io/blog/agent-memory-race-2026)
09. [Graph-Based Memory Solutions for AI Context, Mem0](https://mem0.ai/blog/graph-memory-solutions-ai-agents)
10. [Atlan Context Layer: Enterprise AI Agent Memory, Atlan](https://atlan.com/know/atlan-context-layer-enterprise-memory/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="every-ai-agent-has-4-distinct-memory-layers-activity.md">
<details>
<summary>every-ai-agent-has-4-distinct-memory-layers-activity</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR>

Every AI agent has 4 distinct memory layers:

(Confuse them, and your system will eventually break)

𝟭/ 𝗜𝗻𝘁𝗲𝗿𝗻𝗮𝗹 𝗸𝗻𝗼𝘄𝗹𝗲𝗱𝗴𝗲

This is the pre-trained information stored inside the LLM’s weights.

World knowledge.
Language patterns.
Reasoning priors.

It’s powerful, but it’s read-only.

You cannot inject new user-specific knowledge into it during inference.

Without fine-tuning, it does not update.

This immutability is a core limitation most people forget.

𝟮/ 𝗖𝗼𝗻𝘁𝗲𝘅𝘁 𝘄𝗶𝗻𝗱𝗼𝘄

This is the only reality the model sees during a single call.

User input.
Retrieved facts.
Tool schemas.

Conversation snippets.

Internal chain-of-thought scaffolding

If it’s not in the context window, it does not exist for the model.

And if you overload it with noise, performance drops due to context rot.

Information buried in the middle of long prompts gets ignored or diluted.

𝟯/ 𝗦𝗵𝗼𝗿𝘁-𝘁𝗲𝗿𝗺 𝗺𝗲𝗺𝗼𝗿𝘆

This is the working state of the entire agent system across multiple calls.

It may include:
 
• Full conversation history
• Retrieved documents
• Tool outputs
• Structured intermediate results

But for each inference step, you only project a subset of that into the context window.

Short-term memory is the reservoir.

The context window is the filtered projection.

That projection step is where context engineering lives.

𝟰/ 𝗟𝗼𝗻𝗴-𝘁𝗲𝗿𝗺 𝗺𝗲𝗺𝗼𝗿𝘆.

This is external, persistent storage.

Think:
 
• Databases.
• Vector stores.
• Graph stores.
• File systems.

This is where you store:
 
• User preferences
• Past interactions
• Learned facts
• Saved outputs

It gives the agent continuity across sessions.

𝗧𝗵𝗲𝘀𝗲 𝗳𝗼𝘂𝗿 𝗹𝗮𝘆𝗲𝗿𝘀 𝗳𝗼𝗿𝗺 𝗮 𝗳𝗶𝗹𝘁𝗲𝗿𝗶𝗻𝗴 𝗵𝗶𝗲𝗿𝗮𝗿𝗰𝗵𝘆.

Long-term memory → retrieve relevant data
Short-term memory → accumulate working state
Context window → curate only what matters
Internal knowledge → apply general reasoning

If a user asks about Nvidia, you don’t dump your entire database into the context window.

You retrieve only Nvidia-related facts.

If the conversation has run for hours, you summarize older turns instead of passing everything verbatim.

This dynamic interplay is what makes an agent feel coherent.

If you’re building agentic systems in production, understanding these four layers directly impacts latency, cost, reliability, and UX.

We go deep into designing memory architectures, context engineering, and long-term persistence patterns inside the Agentic AI Engineering course.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="knowledge-graphs-as-memory-why-your-ai-agent-needs-to-think-.md">
<details>
<summary>Knowledge Graphs as Memory: Why Your AI Agent Needs to Think in Relationships</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.octoco.ai/blog/knowledge-graphs-as-memory>

# Knowledge Graphs as Memory: Why Your AI Agent Needs to Think in Relationships

Written by Herman Lintvelt

https://cdn.sanity.io/images/8j9syqgm/production/d5573db72281e051cbbfa5afc598f1f88200fd88-1140x645.png?w=1600

In this series on AI-era engineering practices, we’ve explored how to [specify](https://humancoder.substack.com/p/writing-user-stories-for-uncertain), [test](https://humancoder.substack.com/p/testing-the-untestable-strategies), and [continuously evaluate](https://humancoder.substack.com/p/cicdce-the-third-pillar-of-ai-development) AI systems. We’ve talked about the shift from [vibe coding to agentic engineering](https://humancoder.substack.com/p/link-to-vibe-coding-article). But there’s a foundational problem we haven’t addressed directly: memory.

AI agents are forgetful. Not occasionally, but fundamentally. They operate with volatile context windows, truncated histories, and almost no persistent understanding of the user’s evolving world. Every conversation starts from scratch. Every task lacks the context of what came before.

This isn’t a bug we can prompt our way around. It’s an architectural limitation that knowledge graphs might finally solve.

## What Does “Knowledge Graph as Memory” Actually Mean?

Let me be concrete about what we’re discussing, because “knowledge graph” gets thrown around loosely.

> [Sir Tim Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee) invented the web because he believed in the idea that knowledge is represented just as much, if not more, by the relationships between facts than the facts themselves, and he envisioned a collaborative system where it is easy to add these links, or relationships, between the various sources or nodes.

A knowledge graph represents information as a network of entities (nodes) and the relationships between them (edges). Instead of storing facts as isolated text chunks, e.g. “Alice works at Acme Pty Ltd” and “Acme Pty Ltd is in Cape Town”, a knowledge graph captures the underlying structure:

`(Alice)-[:WORKS_AT]->(Acme Pty Ltd)-[:LOCATED_IN]->(Cape Town)`

This structure enables something that vector databases fundamentally cannot: traversal. You can ask “Where does Alice work?” and get Acme Pty Ltd. You can then ask, “Where is that?” and traverse to Cape Town. The relationships are explicit, queryable, and composable.

When we talk about knowledge graphs as agent memory, we’re talking about storing not just what the agent learns, but how different pieces of information relate to each other, and how those relationships change over time.

Traditional agent architectures treat memory as a collection of text snippets retrieved by semantic similarity. You ask a question, the system finds chunks that seem relevant based on embedding similarity, and the LLM tries to synthesise them into an answer.

Knowledge graph memory inverts this. Instead of finding similar text, you traverse explicit relationships. Instead of hoping the LLM can infer connections, you store them directly.

## Why RAG Isn’t Enough

Retrieval-Augmented Generation (RAG) has been transformational. It grounds LLM responses in real data, reduces hallucinations, and enables access to information beyond the model’s training cutoff. [We’ve](https://octoco.ai/) built RAG systems, and they work.

But RAG has fundamental limitations that become painfully apparent in agentic applications:

**Single-hop retrieval.** Traditional RAG finds chunks similar to your query. It struggles when answering requires connecting dots across multiple documents or understanding how facts relate to each other. “What did Alice say about the roadmap before the product launch?” requires temporal reasoning across multiple interactions; something vector similarity alone can’t provide.

**No relationship awareness.** RAG treats knowledge as disconnected text fragments. It can’t natively understand that Alice manages Bob, Bob wrote the report, and the report affects Project X. These connections exist implicitly in documents, but the retrieval system can’t traverse them.

**Semantic similarity isn’t semantic understanding.** Finding text that’s “similar” to a query is different from understanding what the query means. RAG might retrieve text mentioning both Product A and Product B without knowing whether they’re competitors, complements, or entirely unrelated.

**Stale context.** RAG systems typically require reprocessing entire document collections when data changes. For agents that need to learn continuously from interactions, this creates an impractical maintenance burden.

The research backs this up. [GNN-RAG](https://arxiv.org/abs/2405.20139) (Mavromatis & Karypis, 2024) demonstrated that graph neural retrieval outperforms competing approaches by 8.9–15.5% on answer F1 for multi-hop and multi-entity questions across the WebQSP and CWQ benchmarks. [HopRAG](https://arxiv.org/abs/2502.12442) (Liu et al., 2025; ACL Findings) showed that graph-structured retrieval with logical traversal achieves over 36% higher answer accuracy and 21% improved retrieval F1 compared to dense vector retrievers on the MuSiQue, 2WikiMultiHopQA, and HotpotQA benchmarks. And [SG-RAG](https://www.mdpi.com/2504-4990/7/3/74) (2025) confirmed that subgraph retrieval from knowledge graphs statistically significantly outperformed traditional RAG across 1-hop, 2-hop, and 3-hop questions using both Llama-3 and GPT-4 Turbo. For complex queries requiring synthesis across multiple sources, the gap widens further.

This doesn’t mean RAG is useless; far from it. But for agents that need to reason about relationships, track temporal changes, and maintain coherent understanding across sessions, we need something more.

## The Knowledge Graph Advantage

So what do knowledge graphs actually provide that vector databases don’t?

### 1\. Multi-Hop Reasoning

Consider this query: “Which employees who worked on Project Alpha also contributed to the security audit that flagged the issues Bob mentioned in last week’s standup?”

Answering this requires traversing multiple relationships:

- Employees → worked on → Project Alpha
- Employees → contributed to → Security Audit
- Security Audit → flagged → Issues
- Bob → mentioned → Issues
- Issues → discussed in → Standup
- Standup → occurred → Last Week

A knowledge graph can traverse this path directly. RAG would need to retrieve relevant chunks for each entity and hope the LLM can piece together the connections, often unsuccessfully.

### 2\. Temporal Awareness

Facts change. Alice worked at Acme Pty Ltd. Now she works at BigTech. A naive memory system might return conflicting information. A temporally-aware knowledge graph tracks validity periods:

`(Alice)-[:WORKS_AT {valid_from: "2023-01", valid_to: "2025-06"}]->(Acme Pty Ltd)
(Alice)-[:WORKS_AT {valid_from: "2025-06"}]->(BigTech)
`

Now you can ask “Where did Alice work in 2024?” or “How has Alice’s employment changed?” and get accurate, time-aware answers. This bi-temporal model (tracking both when events occurred and when they were recorded) is essential for agents that need to understand how the world evolves.

### 3\. Explainability

When an agent makes a recommendation, you want to know why. Knowledge graphs provide explicit reasoning paths that can be audited. “I recommended this because Alice → manages → Bob, Bob → wrote → this report, and this report → relates to → your question.” The chain of reasoning is transparent, not a black-box embedding similarity score.

### 4\. Incremental Updates

Unlike RAG systems that often require reindexing entire collections, knowledge graphs can be updated incrementally. New facts are added, relationships are modified, and the graph evolves without expensive recomputation. For agents learning from ongoing interactions, this is essential.

## The Landscape: Projects and Frameworks

The tooling for knowledge graph agent memory has matured significantly. Here’s what’s worth knowing:

### Graphiti / Zep

[Graphiti](https://github.com/getzep/graphiti) is Zep’s open-source framework for building temporally-aware knowledge graphs. It’s specifically designed for agent memory, handling chat histories, structured data, and unstructured text in a unified graph.

What makes Graphiti interesting is its bi-temporal model, which tracks both when events occurred and when they were ingested. Every relationship includes validity intervals, enabling powerful historical queries. The system achieves sub-300ms retrieval latency by combining semantic embeddings, keyword search, and graph traversal, avoiding LLM calls during retrieval.

In benchmarks, Zep (powered by Graphiti) outperformed MemGPT on the Deep Memory Retrieval benchmark (94.8% vs 93.4%) while reducing response latency by 90% compared to full-context approaches.

### Mem0

[Mem0](https://github.com/mem0ai/mem0) takes a different approach: providing a memory layer that works with or without graph capabilities. The base system uses vector storage for simplicity, with an optional graph layer (Mem0ᵍ) for relationship-aware applications.

The research shows Mem0 achieves 26% higher accuracy than OpenAI’s memory system on the LOCOMO benchmark, with 91% lower latency and 90% token savings compared to full-context approaches. The graph-enhanced variant adds about 2% to accuracy while maintaining reasonable latency.

Mem0 supports Neo4j, Memgraph, and Amazon Neptune as graph backends, with straightforward integration into existing LLM workflows.

### Neo4j MCP Servers

Multiple projects now provide Model Context Protocol (MCP) servers for Neo4j integration with AI assistants:

- [mcp-neo4j-agent-memory](https://github.com/knowall-ai/mcp-neo4j-agent-memory) - Specialised for memory operations with 10 purpose-built tools
- [mcp-neo4j-memory-server](https://github.com/JovanHsu/mcp-neo4j-memory-server) - Focuses on maintaining context across conversations with semantic search

These enable AI assistants like Claude to build and query persistent knowledge graphs directly, storing facts as nodes and creating semantic relationships between them.

### Microsoft GraphRAG / LightRAG

[Microsoft’s GraphRAG](https://github.com/microsoft/graphrag) approaches the problem from a document-analysis angle: automatically extracting knowledge graphs from text corpora using LLMs, then using the graph structure to enhance retrieval.

GraphRAG excels at “global” queries that require understanding the semantic structure of an entire corpus, outperforming naive RAG by 70-80% on comprehensiveness and diversity metrics. The tradeoff is cost, as initial graph construction can be expensive.

[LightRAG](https://github.com/HKUDS/LightRAG) offers a faster, cheaper alternative with easier incremental updates. For teams wanting stepwise improvement over pure vector RAG without the full complexity, it’s worth evaluating.

## When Knowledge Graphs Make Sense (And When They Don’t)

Knowledge graphs aren’t universally superior to vector databases. The right choice depends on your use case.

**Knowledge graphs excel when:**

- Queries require multi-hop reasoning across relationships
- Temporal reasoning matters (what changed, when, how)
- Explainability and audit trails are important
- Your domain has clear entity types and relationship patterns
- Agents need to learn and adapt over long interactions

**Vector RAG is often sufficient when:**

- Queries are straightforward, factual lookups
- Relationships between data points don’t matter much
- You need fast deployment with minimal infrastructure
- Your data is highly unstructured without clear entities
- Occasional inaccuracy is acceptable

**The hybrid approach is increasingly common:** Use vector retrieval to cast a wide net for semantic relevance, then use graph structures to refine results and reason over relationships. Many production systems combine both, getting breadth from vectors and precision from graphs.

## The Challenges

Let me be honest about the difficulties. Knowledge graphs aren’t a free lunch.

**Schema design complexity.** Designing an effective graph schema requires a deep understanding of your domain. What are the entity types? What relationships matter? Get this wrong, and you’ll have a graph that doesn’t support the queries you actually need.

**Construction overhead.** Extracting entities and relationships from unstructured data is non-trivial. LLM-based extraction has improved dramatically, but it adds latency and cost to ingestion pipelines.

**Maintenance burden.** Graphs require ongoing schema governance and entity resolution. As your domain evolves, the graph needs to evolve too. This isn’t set-and-forget infrastructure.

**Query performance at scale.** Complex graph traversals can be slow on large graphs, especially with multi-hop queries. Index design and query optimisation matter.

**Learning curve.** Graph query languages like Cypher require a different way of thinking than SQL or simple API calls. Your team needs to build new skills.

These challenges are real but manageable. The question is whether your use case justifies the investment.

## My Experiment: Personal Context with Neo4j + Google ADK

I’ve been experimenting with a personal AI agent that uses Neo4j as its memory layer. The goal: create an agent that understands my personal context; not just individual data points, but the relationships between life events, health, productivity, goals, and outcomes over time.

Here’s what I learned from actually implementing this.

### The Architecture

The system uses a multi-agent architecture with [Google’s Agent Development Kit (ADK)](https://google.github.io/adk-docs/):

`Orchestrator Agent
├── User Context Agent (Neo4j MCP Tools)
└── Personal Insights Agent (Data Analysis Tools)`

The orchestrator handles conversation flow. At the start of each session, it asks the context agent to retrieve stored context. After each response, it asks the context agent to store anything worth remembering. The insights agent focuses on analysing the data—it doesn’t need to know how memory works.

Critically, the context agent uses the **official Neo4j MCP server** (`neo4j-mcp`) via MCP tools. This was simpler than I expected:

`# thrively_agent/agents/context_agent.py
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset
from mcp import StdioServerParameters

context_agent = LlmAgent(
    name="user_context_expert",
    description="Manages user context in Neo4j knowledge graph.",
    model="gemini-2.0-flash",
    instruction=context_agent_instruction,
    tools=[\
        MCPToolset(\
            connection_params=StdioConnectionParams(\
                server_params=StdioServerParameters(\
                    command="neo4j-mcp",\
                    env={\
                        "NEO4J_URI": os.environ["NEO4J_URI"],\
                        "NEO4J_USERNAME": os.environ["NEO4J_USERNAME"],\
                        "NEO4J_PASSWORD": os.environ["NEO4J_PASSWORD"],\
                    },\
                ),\
            ),\
            tool_filter=["get-schema", "read-cypher", "write-cypher"],\
        )\
    ],
)`

That’s it. The agent gets three tools: `read-cypher`, `write-cypher`, and `get-schema`. Everything else is just prompting.

### Why Life Events Need Graphs

The insight that made this click: life events don’t exist in isolation. They have causes, effects, and relationships:

- A **job change** → causes **stress** → impacts **sleep quality**
- A **pregnancy** → relates to **partner** → influences **wellness goals**
- An **injury** → prevents **running** → requires **alternative exercise**

Vector similarity search can find documents mentioning these things. But it can’t traverse the relationship: “What’s preventing me from reaching my running goal?” requires understanding that the injury → prevents → running goal path exists.

In Cypher, storing a life event with its impacts looks like:

`MATCH (u:User {user_id: $user_id})

// Create the life event
MERGE (e:LifeEvent {name: "New Job at TechCorp"})
SET e.type = "job_change",
    e.description = "Started Senior Engineer role",
    e.date = date("2026-01-15"),
    e.impact = "mixed",
    e.status = "active"

// Link to user
MERGE (u)-[:HAS_EVENT]->(e)

// Create personal insight and link
MERGE (i:PersonalInsight {category: "sleep", name: "Sleep Quality Pattern"})
SET i.observation = "Sleep quality drops during high-stress periods"
MERGE (e)-[:IMPACTS]->(i)

// Create affected goal and link
MERGE (g:Goal {name: "Morning Run Goal"})
SET g.description = "Return to 40km/week running",
    g.status = "blocked"
MERGE (e)-[:PREVENTS]->(g)
`

Now, when I ask “Why am I not sleeping well?”, the agent can traverse: User → has\_event → New Job → impacts → Sleep Quality Pattern. And when I ask “What’s blocking my running goal?”, it can find: New Job → prevents → Morning Run Goal.

### The Prompt That Makes It Work

The context agent’s instruction is deliberately open-ended. I didn’t define a rigid schema; I let the agent decide what’s worth storing:

`You are the User Context Expert.

<Context for my specific application and overarching agent goal...>

### Freedom to Create
You are NOT limited to any fixed schema. Create whatever node labels, relationship types, and properties you think best represent the user's context. Some ideas:
- LifeEvent, PersonalInsight, Preference, Goal, Achievement, Challenge, Person, Habit
- Relationships: IMPACTS, CAUSES, MOTIVATES, PREVENTS, RELATES_TO, KNOWS, etc.
- But feel free to invent new ones that better capture the meaning

### Guidelines
- Quality over quantity: only store genuinely meaningful information
- Include temporal context (dates) when mentioned or inferred
- Capture emotional context and impact when relevant
- Link related entities to each other, not just to the User node
`

This worked surprisingly well. The agent creates reasonable structures without needing exhaustive schema documentation. It invents relationship types like `WORRIED_ABOUT` or `CELEBRATES` when they fit the context better than generic `RELATES_TO`.

**The schema-less approach works.** I expected chaos. Instead, the agent creates coherent graphs. It reuses labels consistently and creates sensible relationships. There’s drift over time, but the graph remains queryable.

**Retrieval is fast.** Querying the user’s context graph takes 50-100ms. No vector embedding, no reranking, just a Cypher query that traverses relationships.

**The agent decides what’s memorable.** I don’t have explicit rules for “what to store.” The prompt says “only store genuinely meaningful information”, and the agent makes reasonable judgments. It stores life events and goals but skips routine queries about sleep scores.

**Debugging is visual.** Neo4j Browser lets me see exactly what the agent stored. When something goes wrong, I can visualise the graph and understand why.

### What I’d Do Differently

**More explicit temporal handling.** The bi-temporal model from Graphiti (tracking both event time and ingestion time) would be valuable. My current approach stores dates but doesn’t systematically track validity periods.

**Entity resolution prompts.** The agent sometimes creates duplicate nodes for the same concept (”running goal” vs “40km weekly running”). A dedicated deduplication pass would help.

**Structured extraction first.** Currently, the insights agent writes its response, then delegates to the context agent to store relevant context. A cleaner approach: extract structured entities during the conversation, then batch-write at session end.

### The Bottom Line

Neo4j + MCP gives agents relationship-aware memory with minimal infrastructure. The official `neo4j-mcp`server provides `read-cypher` and `write-cypher` tools that work directly with ADK agents. For local development, it’s a Homebrew install away (`brew install neo4j-mcp`). For production, Neo4j Aura’s free tier handles POC workloads.

## Where This Is Heading

The direction seems clear: agent memory is moving from flat document retrieval toward structured, relationship-aware knowledge representation. Not because graphs are trendy, but because agents that reason about relationships outperform those that don’t.

Several trends reinforce this:

**MCP adoption.** The Model Context Protocol is becoming a standard for connecting agents to external systems, and graph databases are a natural fit. As MCP matures, expect tighter integration between AI assistants and knowledge graphs.

**Temporal reasoning demands.** As agents take on longer-running tasks and maintain relationships across sessions, temporal awareness becomes essential. You can’t manage a multi-week project with an agent that forgets yesterday.

**Enterprise requirements.** Audit trails, explainability, and compliance all benefit from graph-based memory where reasoning chains are explicit and queryable.

**Hybrid architectures.** The “vector vs. graph” debate is resolving into “vector AND graph.” Combining semantic search with structured knowledge retrieval gives agents both breadth and precision.

The agents that remember best will be the agents that reason best. And reasoning requires structure.

## Start Here

If you’re building agents and haven’t explored graph-based memory:

1.  **Identify a use case where relationships matter.** Not every agent needs a knowledge graph. Find one where multi-hop reasoning or temporal awareness would clearly improve outcomes.
2.  **Start with a managed service.** Neo4j Aura, Amazon Neptune, or Zep Cloud let you experiment without infrastructure overhead. Build understanding before building infrastructure.
3.  **Try an MCP integration.** If you’re using Claude or another MCP-compatible assistant, one of the Neo4j MCP servers can give you graph memory capabilities in an afternoon.
4.  **Evaluate against your actual queries.** Build a small eval set of queries your agent should handle. Compare graph-based retrieval against pure vector retrieval. Let the numbers guide your decision.
5.  **Plan for iteration.** Your first schema will be wrong. Build incrementally, learn from actual usage, and refine. Graph-based memory is a capability you grow into, not a switch you flip.

The tools are ready. The research supports it. The question is whether your agents need to understand relationships, and, if they do, how much longer they can afford to forget.

**Sources and Further Reading:**

- [Graphiti (Zep) - GitHub](https://github.com/getzep/graphiti) - Open-source temporal knowledge graphs for agent memory
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv)](https://arxiv.org/abs/2501.13956) - Research paper with benchmark results
- [Mem0 - GitHub](https://github.com/mem0ai/mem0) - Universal memory layer for AI agents
- [Mem0 Research: Building Production-Ready AI Agents (arXiv)](https://arxiv.org/abs/2504.19413) - Benchmark comparisons
- [Microsoft GraphRAG - GitHub](https://github.com/microsoft/graphrag) - Graph-based RAG from Microsoft Research
- [Neo4j Agent Memory MCP Server](https://github.com/knowall-ai/mcp-neo4j-agent-memory) - MCP integration for Neo4j
- [Neo4j Blog: Graphiti Knowledge Graph Memory](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/) - Technical deep dive
- [AWS Blog: Persistent Memory with Mem0 and Neptune](https://aws.amazon.com/blogs/database/build-persistent-memory-for-agentic-ai-applications-with-mem0-open-source-amazon-elasticache-for-valkey-and-amazon-neptune-analytics/) - Enterprise deployment patterns
- [GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning (arXiv)](https://arxiv.org/abs/2405.20139) - Graph retrieval outperforms flat RAG by 8.9–15.5% on multi-hop KGQA
- [HopRAG: Multi-Hop Reasoning for Logic-Aware RAG (arXiv / ACL Findings 2025)](https://arxiv.org/abs/2502.12442) - Graph-structured traversal achieves 36%+ gains over dense retrievers
- [SG-RAG: SubGraph RAG for Multi-Hop Question Answering (MDPI)](https://www.mdpi.com/2504-4990/7/3/74) - Subgraph retrieval outperforms traditional RAG across hop counts
- [Personalised Health Knowledge Graph (PubMed)](https://pubmed.ncbi.nlm.nih.gov/34690624/) - Healthcare application of personal knowledge graphs

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="memory-systems-for-ai-agents-what-the-research-says-and-what.md">
<details>
<summary>Memory Systems for AI Agents: What the Research Says and What You Can Actually Build</summary>

Phase: [EXPLORATION]

**Source URL:** <https://stevekinney.com/writing/agent-memory-systems>

March 25, 2026

# Memory Systems for AI Agents: What the Research Says and What You Can Actually Build

The old short-term/long-term taxonomy doesn't capture what modern agent memory systems actually do. A new three-axis framework—Forms, Functions, and Dynamics—maps the design space from flat vector stores to RL-driven memory management. Here’s what the research says and what you can build today.

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

Last modified on April 9, 2026.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="plugmem-transforming-raw-agent-interactions-into-reusable-kn.md">
<details>
<summary>PlugMem: Transforming raw agent interactions into reusable knowledge - Microsoft Research</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/>

# PlugMem: Transforming raw agent interactions into reusable knowledge - Microsoft Research

https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/PlugMem-BlogHeroFeature-1400x788-1-scaled.jpg

## At a glance

- Today’s AI agents store long interaction histories but struggle to reuse them effectively.
- Raw memory retrieval can overwhelm agents with lengthy, low-value context.
- PlugMem transforms interaction history into structured, reusable knowledge.
- A single, general-purpose memory module improves performance across diverse agent benchmarks while using fewer memory tokens.

It seems counterintuitive: giving AI agents more memory can make them less effective. As interaction logs accumulate, they grow large, fill with irrelevant content, and become increasingly difficult to use.

More memory means that agents must search through larger volumes of past interactions to find information relevant to the current task. Without structure, these records mix useful experiences with irrelevant details, making retrieval slower and less reliable. The challenge is not storing more experiences, but organizing them so that agents can quickly identify what matters in the moment.

In our recent paper “ [PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents,](https://www.microsoft.com/en-us/research/publication/plugmem-a-task-agnostic-plugin-memory-module-for-llm-agents/)” we introduce a plug-and-play memory system that transforms raw agent interactions into reusable knowledge. Rather than treating memory as text to retrieve, PlugMem organizes that history into structured knowledge designed to support decisions as the agent acts.

Cognitive science offers a useful framework here. It distinguishes between remembering events, knowing facts, and knowing how to perform tasks. Past events provide context, but effective decisions rely on the facts and skills extracted from those events.

This distinction motivated a shift in how we decided to design memory for AI agents. PlugMem implements this shift by converting the agent’s interaction history, such as dialogues, documents, and web sessions, into structured, compact _knowledge units_ that can be reused across tasks.

## How PlugMem works

A key difference between PlugMem and conventional AI memory systems is what gets stored. Traditional approaches store text chunks or named entities (references to people, places, and concepts). PlugMem uses facts and reusable skills as the fundamental building blocks of memory. This design reduces redundancy, increases information density, and improves retrieval precision. It’s built around three core components:

**Structure.** Raw interactions are standardized and transformed into propositional knowledge (facts) and prescriptive knowledge (reusable skills). These knowledge units are organized into a structured memory graph, enabling knowledge to be stored in a form designed for reuse.

**Retrieval.** Rather than retrieving long passages of text, PlugMem retrieves knowledge units that are aligned with the current task. High-level concepts and inferred intents serve as routing signals, surfacing the most relevant information for the decision at hand.

**Reasoning.** Retrieved knowledge is distilled into concise, task-ready guidance before being passed to the base agent, ensuring that only decision-relevant knowledge enters the agent’s context window.

Figure 1 illustrates how these components work together.

https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Figure1-scaled.pngFigure 1. PlugMem organizes different types of agent interactions into a knowledge-centric memory graph, enabling structured retrieval and reasoning.

## One memory, any task

Most AI memory systems are built for one job. A conversational memory module is designed around dialogue. A knowledge-retrieval system is tuned to look up facts. A web agent’s memory is optimized for navigating pages. Each performs well in its target setting but rarely transfers without significant redesign.

PlugMem takes a different approach. It is a foundational memory layer that can be attached to any AI agent without needing to modify it for a specific task.

## Evaluating PlugMem

To test PlugMem, we evaluated the same memory module on three benchmarks that each make different demands on memory:

- Answering questions across long multi-turn conversations
- Finding facts that span multiple Wikipedia articles
- Making decisions while browsing the web

Across all three, PlugMem consistently outperformed both generic retrieval methods and task-specific memory designs while allowing the AI agent to use significantly less memory token budget in the process.

### Measuring memory by utility, not size

We wanted to evaluate whether the right information was reaching the agent at the right moment, without overwhelming the model’s context window, which has limited capacity. To do this, we introduced a metric that measures how much useful, decision-relevant information a memory module contributes relative to how much context it consumes.

When we plotted utility against context consumption, PlugMem consistently came out ahead: it delivered more decision-relevant information while consuming less of the AI agent’s context than other approaches, as shown in Figure 2. These results suggest that transforming experience into knowledge—rather than storing and retrieving raw logs—produces memory that is more useful and efficient.

https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/PlugMem_Fig2_AH.pngFigure 2. Across all three benchmarks, PlugMem delivered more useful memory with less of the agent’s context window.

## Why general-purpose memory can outperform task-specific designs

General-purpose memory modules can outperform systems tailored to specific tasks because the decisive factor is not specialization but whether memory can surface the right knowledge precisely when the agent needs it. Structure, retrieval, and reasoning each play a distinct role, and getting all three right matters more than optimizing for a single use case.

PlugMem is not meant to replace task-specific approaches. It provides a general memory foundation upon which task adaptations can be layered. Our experiments show that combining PlugMem with task-specific techniques yields further gains.

## Toward reusable memory for agents

As AI agents take on longer and more complex tasks, its memory needs to evolve from storing past interactions to actively supplying reusable knowledge. The goal is for agents to carry useful facts and strategies from one task to the next rather than starting from scratch each time.

PlugMem represents a step in that direction, grounding memory design in cognitive principles and treating knowledge as the primary unit of reuse. As agent capabilities expand, knowledge-centric memory may prove to be a critical building block for the next generation of intelligent agents.

Code and experimental results are publicly available on [GitHub (opens in new tab)](https://github.com/TIMAN-group/PlugMem) so that others can reproduce the results and conduct their own research.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="the-modal-model-of-memory-what-ai-agents-can-learn-from-cogn.md">
<details>
<summary>The Modal Model of Memory: What AI Agents Can Learn From Cognitive Science</summary>

Phase: [EXPLORATION]

**Source URL:** <https://mem0.ai/blog/the-modal-model-of-memory-what-ai-agents-can-learn-from-cognitive-science>

# The Modal Model of Memory: What AI Agents Can Learn From Cognitive Science

https://framerusercontent.com/images/dEubtgW9xMK2dJigMXVkC40pFWs.webp?width=2496&height=1248

In 1968, Richard Atkinson and Richard Shiffrin published a paper called "Human Memory: A Proposed System and Its Control Processes." It described memory not as a single faculty but as a set of distinct stores with different capacities, durations, and operating rules, connected by specific control processes that determined what moved between them.

Cognitive scientists spent the next five decades pressure-testing, refining, and building on that model. What came out the other side is not a textbook diagram. It is a working theory of how biological systems actually manage information at scale: what gets in, what is kept, how it becomes durable, and why forgetting is not a failure.

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

Mem0 explicitly names all five of these as core design principles: intelligent filtering, levels-of-processing-style extraction, four-operation interference management, dynamic forgetting, and layered consolidation from conversation to session to user memory. The [research paper](https://mem0.ai/research-3) demonstrates what this architecture produces: 26% higher accuracy on a standardized long-term memory benchmark, 91% lower retrieval latency, and 90% fewer tokens consumed compared to context-stuffing approaches.

The cognitive science did not predict these specific numbers. But it did predict that a system designed around the right memory processes would substantially outperform one that relied on raw storage capacity alone.

Atkinson and Shiffrin got there in 1968. The AI memory field is catching up.

_Further reading on how human memory research applies to AI:_ [_How Memory Shapes Us - A Deep Dive Into the Types of Memory_](https://mem0.ai/blog/how-memory-shapes-us-a-deep-dive-into-the-types-of-memory) _,_ [_Short-Term Memory for AI Agents_](https://mem0.ai/blog/short-term-memory-for-ai-agents) _, and_ [_Short-Term vs. Long-Term Memory in AI_](https://mem0.ai/blog/short-term-vs-long-term-memory-in-ai) _._

**External references:**

- [Atkinson & Shiffrin (1968) - Human Memory: A Proposed System and Its Control Processes](https://doi.org/10.1016/S0079-7421(08)60422-3)

- [Craik & Lockhart (1972) - Levels of Processing: A Framework for Memory Research](https://doi.org/10.1016/S0022-5371(72)80001-X)

- [Bjork & Bjork (1992) - A New Theory of Disuse and an Old Theory of Stimulus Fluctuation](https://doi.org/10.1007/978-1-4614-3050-1_1)

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