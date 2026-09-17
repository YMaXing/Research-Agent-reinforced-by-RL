# Near-tie review: 10_memory_knowledge_access__var_standard  (light vs standard, margin=+0.0193)

## Reviewer conclusion (2026-08-27): KEEP `light`, no override

**No corrections needed** — all scores and reasonings confirmed accurate.

**Quantitative basis:** per-dimension tallies (n=21/arm, 7 sections) show a
mixed picture: `standard` has a slight edge on `cc` (0.762 vs 0.714) and `be`
(0.286 vs 0.238), while `light`'s `de` advantage (0.524 vs 0.429) is the
deciding factor, with `fl`, `cp`, and `ga` tied. Section-level, `light` loses
ground on S6 (Real-World Lessons, weight 0.187, −0.0304, the single largest
swing in the article) and S5 (Memory Implementations, −0.0200), but wins
decisively on S3 (Long-Term Memory, +0.0350) and S4 (Storing Memories,
+0.0479, the largest positive swing), which together outweigh the S5/S6 losses.
Per-draw R_w margins (light−standard): [+0.041, −0.031, +0.048], mean +0.019,
sd 0.044 — two of three draws favor `light`. Moderated significance p≈0.283,
still ambiguous.

**Decision:** no manual override needed — `light` is already mean-R_w's own
winner. `needs_review=True` is left as-is (it reflects an objective statistical
fact about the margin, not review status); this note is the durable record that
the article has been human-reviewed and the pick confirmed.

---

## All sections (light vs standard), most-against-light first
| section | weight | contribution | running total |
|---|---:|---:|---:|
| section-6-real-world-lessons-challenges-and-best-p | 0.187 | -0.0304 | -0.0304 |
| section-5-memory-implementations-with-code-example | 0.187 | -0.0200 | -0.0504 |
| section-1-introduction-why-agents-need-a-memory-in | 0.150 | -0.0135 | -0.0640 |
| section-2-the-layers-of-memory-internal-short-term | 0.103 | +0.0002 | -0.0638 |
| section-7-conclusion | 0.075 | +0.0002 | -0.0635 |
| section-3-long-term-memory-semantic-episodic-and-p | 0.150 | +0.0350 | -0.0285 |
| section-4-storing-memories-pros-and-cons-of-differ | 0.150 | +0.0479 | +0.0193 |

(stored article margin = +0.0193 -- should match the running total's final row to ~4 decimals)

## Section: S6::section-6-real-world-lessons-challenges-and-best-practices  (weight=0.187, contribution=-0.0304 AGAINST light)
Stored section rewards: light=0.2908  standard=0.5119  (explore: light=0.0875  standard=0.3350)

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset1`

**Article text:**
```
## Real-World Lessons: Challenges and Best Practices

Moving from theory to a reliable production system requires navigating a series of complex trade-offs that are constantly evolving with the underlying technology. Here are some important lessons learned from building and scaling agent memory systems.

### Re-evaluating Compression

One of the biggest shifts in memory design has been the trade-off between compressing information and preserving its raw detail.

Just two years ago, with small and expensive context windows, AI engineers were forced to be ruthless with compression. This process is inherently lossy, leading to **summarization drift**: with each cycle, the memory distorts further from the original event [[8]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/). Today, with models offering million-token context windows at a fraction of the cost, the considerations have changed. The best practice is now to lean towards less compression. The raw, unstructured conversational history is the ultimate source of truth, containing emotional subtext and relational dynamics often lost during extraction [[3]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Design your system to work with the most complete version of history that is economically and technically feasible. Use summarization as a tool for creating queryable indexes, but always treat the raw log as the ground truth.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. A common failure mode is over-engineering a complex system for a product that does not need it.

Start from first principles by defining the core function of your agent. The product's goal should dictate the memory architecture. For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point. For a long-term personal AI companion, rich episodic memories are more valuable. For a task-automation agent, procedural memories are likely key.

### The Human Factor and Autonomous Management

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the memory's inner workings. While intended to improve transparency, this often creates significant cognitive overhead.

Users should not be asked to "garden their agent's memories" [[3]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task. Memory management should be autonomous. The agent must learn from corrections in natural conversation (e.g., “Actually, my brother’s name is Mark, not Mike”). This autonomy, however, introduces risks like **self-reinforcing errors**, where an agent treats a faulty memory as ground truth, corrupting its worldview over time [[8]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

A robust system must also handle **contradictions**. When new information conflicts with existing memory, the agent needs a strategy to resolve it. This can involve temporal versioning (preferring the newest information), source attribution (trusting user input over its own inferences), or flagging conflicts for review [[20]](https://arxiv.org/html/2603.07670v1). A more advanced concept, inspired by neuroscience, is **memory reconsolidation**. This theory suggests that when a memory is retrieved, it becomes temporarily malleable, allowing it to be updated with new information before being stored again. This provides a mechanism for memories to adapt and remain relevant over time, rather than being static records [[21]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605913/). Finally, one of the most dangerous failure modes is **silent orchestration failures**, where memory management policies for paging, eviction, or archival do the wrong thing without throwing errors. The only symptom is that responses get worse over time, making these failures difficult to debug [[22]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).
```
**Grader reasoning:**
- `cc`: Real-World Challenges:
**1:** The expected section covers two core topics: Re-evaluating Compression and Designing for the Product. Both are fully present in the generated section. The generated section additionally includes a third topic, 'The Human Factor and Autonomous Management' — this is an extra topic beyond the GT, not a missing one. Since both GT core topics are fully covered, the core content score is 1.
_(matched by ordinal position -- title text didn't match)_
- `fl`: Real-World Challenges:
**1:** The expected section covers two topics (Re-evaluating Compression and Designing for the Product), and both are present in the generated section in the same logical order. The generated section additionally includes a third topic ('The Human Factor and Autonomous Management') appended after the GT's two topics. The GT's Real-World section contains no media elements to misplace. Extra content appended after the GT's topics does not disrupt the narrative logic of the shared topics.
_(matched by ordinal position -- title text didn't match)_
- `de`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=4; quality=strong,strong,strong,strong] Four distinct depth additions qualify: (1) self-reinforcing errors (agent treats faulty memory as ground truth and corrupts its worldview), (2) silent orchestration failures (paging/eviction/archival policies do the wrong thing with no visible errors; only symptom is gradual degradation), (3) explicit strategies for handling contradictions (temporal versioning preferring newest, source attribution trusting user input over agent inference, periodic consolidation), and (4) memory reconsolidation theory, which supplies theoretical foundations and an alternative implementation perspective for autonomous memory updating and contradiction handling (retrieval makes memory temporarily malleable, allowing update before re-storage). All four trace to exploration-phase Sources [46], [48], and [51]. Instances qualify.
- `be`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=1; quality=strong] One breadth addition qualifies: memory reconsolidation theory from neuroscience (when a memory is retrieved it becomes temporarily malleable, allowing it to be updated with new information before being stored again). This provides a mechanism for memories to adapt and remain relevant. This is a clear cross-domain analogy/lesson from another field (neuroscience). It also independently qualifies as depth (theoretical foundations + alternative implementation perspective for autonomous contradiction handling), but is counted here under breadth per the independent criteria. Traces directly to exploration-phase Source [51] (PMC reconsolidation paper) and is discussed in context of Sources [46]/[48]. Instance qualifies.
- `cp`: Real-World Challenges:
**1:** The depth and breadth additions are well-integrated and support the core narrative. The ground truth's focus on re-evaluating compression and designing for the product remains the dominant theme, with the new concepts of specific failure modes and memory reconsolidation serving as enriching, not diluting, details.
_(matched by ordinal position -- title text didn't match)_
- `ga`: Real-World Lessons: Challenges and Best Practices:
**1:** The generated section correctly covers the three main topics required by the guideline: Re-evaluating compression (Old Challenge vs. New Reality), Designing for the Product (no perfect architecture, start from first principles), and The Human Factor (avoiding user cognitive overhead). The content within each subsection accurately reflects the detailed points specified in the guideline. The word count is approximately 500 words, which meets the target. All requirements are met.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset1`

**Article text:**
```
## Real-World Lessons: Challenges and Best Practices

Moving from theory to a reliable production system requires navigating complex trade-offs. Here are some important lessons learned from building and scaling agent memory systems.

### Re-evaluating Compression

One of the biggest shifts in memory design has been the trade-off between compressing information and preserving its raw detail. Just a few years ago, LLMs operated with small and expensive context windows. This constraint forced us, as AI Engineers, to be ruthless with compression. We had to distill every interaction into its most compact form, such as summaries or facts, to fit relevant information into the context window. While necessary, this process is inherently lossy. By summarizing, you keep the general idea but lose the fine details and nuance, which might be important for a personalized agent.

Today, with models offering million-token context windows at a fraction of the cost, the considerations have changed. The best practice is now to lean towards less compression. The raw, unstructured conversational history is the ultimate source of truth. It contains the emotional subtext, subtle hesitations, and relational dynamics that are often dismissed during extraction. While a fact might state, "User has a dog named George," the episodic log reveals, "User mentioned that walking their dog named George is the best part of their day," a far more valuable piece of information for a personalized agent [[6]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). Design your system to work with the most complete version of history that is economically and technically feasible. Use summarization and fact extraction as tools for creating queryable indexes, but always treat the raw log as the ground truth.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. The most common failure mode is over-engineering a complex, multi-part memory system for a product that doesn't need it. It can be tempting to build a system that handles all these memory types from day one. However, this often leads to unnecessary complexity, higher maintenance costs, and slower performance.

The product's goal should dictate the memory architecture, not the other way around [[6]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point. For a long-term personal AI companion, rich episodic memories are beneficial, as the agent's value comes from its ability to remember the narrative of your relationship. For a task-automation agent, procedural memory is likely useful, allowing the agent to recall and execute multi-step workflows.

### The Human Factor

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system to the user, thinking it will improve transparency. In practice, it often creates significant cognitive overhead. Users should not be asked to "garden their agent's memories." This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task. A user's mental model is that they are talking to a single entity; they do not want to switch to being a database administrator.

Memory management should be an autonomous function of the agent. It should learn from corrections within the natural flow of conversation (e.g., "Actually, my brother's name is Mark, not Mike"). The agent, not the user, is responsible for maintaining the integrity of its own knowledge through internal processes for reviewing, consolidating, and resolving conflicting information [[6]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).
```
**Grader reasoning:**
- `cc`: Real-World Lessons: Challenges and Best Practices:
**1:** Both sections cover the compression-versus-raw-detail trade-off and the over-engineering/product-first design point with matching use-case examples. The generated section additionally covers a 'Human Factor' sub-topic with no counterpart in the expected section — a pure addition that does not cause any expected idea to be missing.
- `fl`: Real-World Lessons: Challenges and Best Practices:
**1:** The compression and product-design sub-topics appear in the same order as the expected section, with the added Human Factor sub-topic appended after both.
- `de`: Real-World Lessons: Challenges and Best Practices:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources do exist for this episode, so this is a content-based 0 (nothing to trace), not the code-level hard zero that applies when no exploration sources exist at all.
- `be`: Real-World Lessons: Challenges and Best Practices:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources do exist for this episode, so this is a content-based 0 (nothing to trace), not the code-level hard zero that applies when no exploration sources exist at all.
- `cp`: Real-World Lessons: Challenges and Best Practices:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default, since there are no qualifying additions to evaluate for dilution of the ground truth core.
- `ga`: Real-World Lessons: Challenges and Best Practices:
**0:** At 568 prose-only words against a 500-word target (tolerance ceiling ~550 words), this section runs over by about 18 words past the tolerance boundary — past the trivial-margin grace (roughly 12.5 words on a 50-word band) but only barely, and flagged as a borderline call alongside the Introduction and Layers-of-Memory length calls above. Content otherwise covers all three guideline points in the guideline's own order.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset1`

**Article text:**
```
## Real-World Lessons: Challenges and Best Practices

Moving from theory to a reliable production system requires navigating a series of complex trade-offs. Here are some of the most important lessons learned from building and scaling agent memory systems.

### Re-evaluating Compression

The trade-off between compressing information and preserving its raw detail has shifted dramatically. Just two years ago, small and expensive context windows (8k or 16k tokens) forced us to be ruthless with compression. We had to distill every interaction into its most compact form—summaries, facts, or entities. This process is inherently lossy, sacrificing fine details for brevity. This has also led to strategies for active forgetting. In robotics, agents use frequency- and similarity-based mechanisms to automatically discard redundant data, reducing memory size without significant performance loss [[16]](https://h2t.iar.kit.edu/pdf/Plewnia2025.pdf).

Today, with models offering million-token context windows at a fraction of the cost, the best practice is to lean towards less compression [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). The raw, unstructured conversational history is the ultimate source of truth. It contains the emotional subtext and relational dynamics that are often lost during extraction. While a fact might state, "User has a dog named George," the episodic log reveals, "User mentioned that walking their dog...is the best part of their day," a far more valuable piece of information for a personalized agent. Design your system to work with the most complete version of history that is economically and technically feasible.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful toolkit, not a mandatory blueprint. The most common failure mode is over-engineering a complex memory system for a product that does not need it [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Start from first principles by defining the core function of your agent. The product's goal should dictate the memory architecture. For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point. For a long-term personal AI companion, rich episodic memories are essential. For a task-automation agent, procedural memory is likely the most useful.

### The Human Factor

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system, thinking it improves transparency. In practice, it often creates significant cognitive overhead.

Users should not be asked to "garden their agent's memories." This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). Memory management should be an autonomous function. The agent should learn from corrections within the natural flow of conversation (e.g., "Actually, my brother's name is Mark, not Mike"). The agent, not the user, is responsible for maintaining the integrity of its own knowledge. This includes resolving contradictions. When new information conflicts with existing memories, the system needs a strategy, such as temporal versioning (preferring the newest data) or source attribution (trusting user input over agent inference), to maintain a coherent state [[17]](https://arxiv.org/html/2603.07670v1).
```
**Grader reasoning:**
- `cc`: Real-World Lessons: Challenges and Best Practices:
**1:** Both sections cover the compression-versus-raw-detail trade-off and the over-engineering/product-first design point with matching use-case examples, plus a 'Human Factor' addition with no counterpart in the expected section. Two further additions (a robotics forgetting-mechanism example under Compression, and a temporal-versioning/source-attribution point under Human Factor, both verified below as genuine depth/breadth) enrich rather than displace the expected content.
- `fl`: Real-World Lessons: Challenges and Best Practices:
**1:** The compression and product-design sub-topics appear in the same order as the expected section.
- `de`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=1; quality=strong] 'The system needs a strategy, such as temporal versioning (preferring the newest data) or source attribution (trusting user input over agent inference)' traces directly to the exploration-phase arxiv source on memory systems for language agents ('temporal versioning (prefer newest record), source attribution (user > agent inference)'). A specific, named technique for the section's own conflict-resolution topic — strong.
- `be`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=1; quality=strong] 'In robotics, agents use frequency- and similarity-based mechanisms to automatically discard redundant data, reducing memory size without significant performance loss' traces directly to the exploration-phase ARMAR-6 robotics paper on episodic-memory forgetting. A practical application in an adjacent domain (robotics) with a specific named mechanism — strong.
- `cp`: Real-World Lessons: Challenges and Best Practices:
**1:** Both depth_enhancement and breadth_enhancement are 1 here, so this is evaluated rather than defaulted: the robotics example and the temporal-versioning point are each one sentence within their respective subsections, and the three expected lessons remain the section's clear focus. No dilution.
- `ga`: Real-World Lessons: Challenges and Best Practices:
**1:** Within the 500-word target (480 words, prose-only). Covers all three guideline points in the guideline's own order. The robotics and temporal-versioning additions are closely related to the compression and human-factor topics they sit under, so they read as complementary enrichment rather than unrelated topics under the guideline's 'more' rule.

### Arm: standard (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset3`

**Article text:**
```
## Real-World Lessons: Challenges and Best Practices

The architectural patterns we have discussed provide a useful toolkit, but moving from theory to a reliable, production-ready system requires navigating complex trade-offs. The underlying technology is improving so fast that best practices are constantly evolving.

Here are some of the most important lessons learned from building and scaling agent memory systems.

**Re-evaluating compression** is one of the biggest changes. Just a couple of years ago, LLMs operated with small and expensive context windows, forcing us to be ruthless with compression. We distilled every interaction into its most compact form—summaries, facts, or entities. This process is inherently lossy, a failure mode known as "summarization drift," where repeated compression erodes details until the memory no longer reflects what happened [[4]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/). Today, benchmarks show that while a full-context approach is most accurate, it is unusable in production due to high latency (17s at p95) and token costs. Selective memory systems trade a small amount of accuracy (around 6 percentage points) for a 91% reduction in latency and 90% fewer tokens, making them a practical necessity [[19]](https://mem0.ai/blog/state-of-ai-agent-memory-2026).

**Designing for the product** is another key lesson. There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. A common failure mode is over-engineering a complex system for a product that does not need it. The product's goal should dictate the memory architecture, not the other way around. For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point. For a long-term personal AI companion, rich episodic memories are more valuable. For a task-automation agent, procedural memory is likely key [[8]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

**The human factor** is often overlooked. Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system to the user, thinking it will improve transparency. In practice, it often creates significant cognitive overhead. Users should not be asked to "garden their agent's memories" [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task. Memory management should be an autonomous function of the agent, learning from corrections within the natural flow of conversation. Advanced systems even perform autonomous memory consolidation, using idle time to review, merge, and clean up memories without user intervention [[20]](https://www.indium.tech/blog/7-state-persistence-strategies-ai-agents-2026/).

**Preventing memory staleness** is a critical, unsolved challenge. As a memory store grows, information can become outdated. A user preference from two years ago may no longer apply, but if it is highly relevant, it will continue to be retrieved, leading the agent to be confidently wrong. This is a distinct problem from normal decay; it is about detecting when high-relevance facts become invalid, which remains an open research problem [[19]](https://mem0.ai/blog/state-of-ai-agent-memory-2026). Other dangerous failure modes include **memory corruption**, where poisoned or incorrect data enters the memory and persists across sessions, and **hallucination cascades**, where a fabricated fact is used to inform subsequent decisions, creating a chain reaction of errors [[21]](https://galileo.ai/blog/agent-failure-modes-guide).
```
**Grader reasoning:**
- `cc`: Real-World Challenges:
**1:** The generated section covers the same core topics as the expected output, discussing the re-evaluation of compression due to larger context windows and the importance of designing the memory architecture based on product needs. However, it adds two additional topics not present in the expected section: "The human factor" and "Preventing memory staleness".
_(matched by ordinal position -- title text didn't match)_
- `fl`: Real-World Challenges:
**1:** Both sections discuss the challenges of building memory systems. The generated section follows a similar flow but adds two extra points at the end. These additions are complementary and do not disrupt the overall narrative.
_(matched by ordinal position -- title text didn't match)_
- `de`: Real-World Challenges:
**1:** [instances=4; quality=strong,strong,strong,strong] A depth addition is present: the generated section discusses several critical implementation challenges and failure modes not mentioned in the expected output, including "memory staleness" (high-relevance facts becoming outdated but still retrieved), "memory corruption," "hallucination cascades," and autonomous memory consolidation during idle time. These qualify as 'limitations, criticisms, or failure modes of the core topic' and 'implementation challenges'. Traces to exploration-phase sources https://galileo.ai/blog/agent-failure-modes-guide, https://mem0.ai/blog/state-of-ai-agent-memory-2026, and https://www.indium.tech/blog/7-state-persistence-strategies-ai-agents-2026/ in research.md. Instances qualify.
_(matched by ordinal position -- title text didn't match)_
- `be`: Real-World Challenges:
**0:** [instances=0] No breadth additions present. The section focuses on best practices and challenges directly related to agent memory without qualifying cross-domain expansions traceable to exploration-phase sources.
_(matched by ordinal position -- title text didn't match)_
- `cp`: Real-World Challenges:
**1:** The depth additions ("memory staleness," "memory corruption," "hallucination cascades," and autonomous consolidation) are all directly relevant implementation challenges. They are well-integrated and serve to deepen the section's core topic, which is about real-world challenges. The ground truth core is preserved and enhanced.
_(matched by ordinal position -- title text didn't match)_
- `ga`: Real-World Lessons: Challenges and Best Practices:
**1:** The generated section successfully covers all the required topics. It discusses the three main points: 1. Re-evaluating compression, contrasting the old challenge of small context windows with the new reality of larger ones. 2. Designing for the product, emphasizing that the memory architecture should be dictated by the product's core function with examples for a Q&A bot, a personal companion, and a task-automation agent. 3. The Human Factor, explaining the cognitive overhead for users and arguing that memory management should be autonomous. The prose-only word count is approximately 520 words, which is within the 500-word target.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset3`

**Article text:**
```
## Real-World Lessons: Challenges and Best Practices

The architectural patterns we have discussed provide a useful toolkit, but moving from theory to a reliable, production-ready system requires navigating complex trade-offs. Here are some of the most important lessons learned from building and scaling agent memory systems in the real world.

### Re-evaluating compression

One of the biggest shifts in memory design has been the trade-off between compressing information and preserving its raw detail. Just two years ago, with small and expensive context windows, the primary goal was to distill every interaction into its most compact form. This process, however, causes **summarization drift**: with each compression, details are lost, and the memory can diverge from what actually happened [[52]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

Today, with million-token context windows, the best practice is to lean towards less compression. While full context provides the highest theoretical accuracy, benchmarks show it comes at a cost that is unusable in production: a p95 latency over 17 seconds and 14 times the token cost of selective memory systems [[51]](https://mem0.ai/blog/state-of-ai-agent-memory-2026). The raw, unstructured conversational history is the ultimate source of truth. It contains the emotional subtext and relational dynamics that are often lost during extraction. A fact might state, "User has a dog named George," but the episodic log reveals, "User mentioned that walking their dog... is the best part of their day," a far more valuable piece of information. Design your system to work with the most complete version of history that is feasible. Use summarization and fact extraction to create queryable indexes, but always treat the raw log as the ground truth.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. A common failure mode is over-engineering a complex, multi-part memory system for a product that does not need it [[9]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Start from first principles by defining the core function of your agent. The product's goal should dictate the memory architecture. For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point. For a long-term personal AI companion, rich episodic memories are beneficial, as the agent's value comes from its ability to remember the narrative of your relationship. For a task-automation agent, procedural memory is key, allowing it to recall and execute multi-step workflows reliably.

### Autonomous Memory Management

A key practice is autonomous consolidation. A background process can run during idle time to review, extract, and merge learnings from recent conversations. This "sleep-cycle" refinement improves performance and memory organization [[56]](https://www.indium.tech/blog/7-state-persistence-strategies-ai-agents-2026/).

### The Human Factor: The additional user cognitive overhead

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system to the user, thinking it will improve transparency. In practice, this often creates a large amount of cognitive overhead [[9]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Users should not be asked to "garden their agent's memories." This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task. Memory management should be an autonomous function of the agent. It should learn from corrections within the natural flow of conversation (e.g., "Actually, my brother's name is Mark, not Mike"). The agent, not the user, is responsible for periodically reviewing, consolidating, and resolving conflicting information in its memory stores. The agent should also be designed to handle contradictions and avoid **self-reinforcing errors**, where a single incorrect memory is treated as ground truth and corrupts future reasoning [[52]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).
```
**Grader reasoning:**
- `cc`: Real-World Lessons: Challenges and Best Practices:
**1:** Both sections cover the compression-versus-raw-detail trade-off and the over-engineering/product-first design point with matching use-case examples. The generated section adds a full extra 'Autonomous Memory Management' subsection and a 'Human Factor' subsection, neither present in the expected section — both are additions and do not cause any expected idea to be missing.
- `fl`: Real-World Lessons: Challenges and Best Practices:
**1:** The compression and product-design sub-topics appear in the same order as the expected section; the two added subsections are appended after rather than interspersed between them.
- `de`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=4; quality=strong,strong,strong,strong] (1) 'Summarization drift' traces to the exploration-phase Practical Guide's Failure Modes section. (2) The LOCOMO 'p95 latency over 17 seconds and 14 times the token cost' figures trace to the exploration-phase 'State of AI Agent Memory 2026' source (a separate instance from the Introduction's use of the same source, since each section's enhancement is evaluated independently). (3) The 'sleep-cycle' autonomous-consolidation practice traces to the exploration-phase indium.tech source's 'Sleep-Time Asynchronous Memory Refinement' strategy, matching almost sentence-for-sentence. (4) 'Self-reinforcing errors' traces to the exploration-phase Practical Guide's Failure Modes section ('self-reinforcing errors... a system treats a memory as ground truth'). All four are named, specific mechanisms with real explanation or quantified data — strong.
- `be`: Real-World Lessons: Challenges and Best Practices:
**0:** [instances=0] All four qualifying additions in this section deepen understanding of the core topic's own challenges rather than connecting outward to an adjacent field.
- `cp`: Real-World Lessons: Challenges and Best Practices:
**1:** depth_enhancement=1 for this section (four instances), so this is evaluated rather than defaulted: the four additions are distributed across four different subsections (one each, mostly), each a sentence or two; the three-lessons-plus-human-factor content remains the section's clear focus. No dilution.
- `ga`: Real-World Lessons: Challenges and Best Practices:
**0:** At 580 prose-only words against a 500-word target (tolerance ceiling ~550 words), this section runs over by about 30 words past the tolerance boundary, driven largely by the two added subsections and the four depth additions. This drives the score to 0; content is otherwise guideline-aligned and the additions are closely related to the topics they sit under.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset3`

**Article text:**
```
## Real-World Lessons: Challenges and Best Practices

The architectural patterns we have discussed provide a useful toolkit, but moving from theory to a reliable, production-ready system requires navigating complex trade-offs that are constantly evolving. Here are some important lessons learned from building and scaling agent memory systems.

### Re-evaluating Compression

One of the biggest shifts in memory design has been the trade-off between compressing information and preserving its raw detail.

Just a couple of years ago, LLMs operated with small and expensive context windows. This forced us to be ruthless with compression, distilling every interaction into its most compact form. While necessary, this process is inherently lossy, leading to "summarization drift" where repeated compression gradually distorts the original meaning [[5]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/). You keep the general idea but lose the fine details and nuance [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Today, with models offering million-token context windows at a fraction of the cost, the considerations have changed. The best practice now leans toward less compression. The raw history is the ultimate source of truth, containing emotional subtext lost during extraction.

Your retrieval pipeline may need to do less *retrieving* and more intelligent *filtering* of a larger, in-context history.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. A common failure mode is over-engineering a complex, multi-part memory system for a product that does not need it. The product's goal should dictate the memory architecture, not the other way around [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

For a Q&A bot over internal documents, a simple RAG pipeline is often the best starting point. For a long-term personal companion, rich episodic memories are beneficial. For a task-automation agent, procedural memory is likely key. Start from first principles by defining the core function of your agent.

### The Human Factor

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system to the user. While well-intentioned, asking users to "garden their agent's memories" by manually editing or deleting facts creates significant cognitive overhead and breaks the illusion of a capable assistant [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Memory management should be an autonomous function. The agent should learn from corrections within the natural flow of conversation (e.g., "Actually, my brother's name is Mark, not Mike"). The agent, not the user, is responsible for maintaining its own knowledge.

This can be implemented via a background "consolidation pipeline" or "dreaming" process that periodically reviews, merges, and prunes memories, inspired by how the human brain solidifies knowledge during sleep [[12]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l). This also helps prevent "memory corruption," where a single poisoned entry can silently corrupt future decisions [[16]](https://galileo.ai/blog/agent-failure-modes-guide).
```
**Grader reasoning:**
- `cc`: Real-World Lessons: Challenges and Best Practices:
**1:** Both sections cover the compression-versus-raw-detail trade-off and the over-engineering/product-first design point with matching use-case examples. The three additions verified below (summarization drift, the sleep-inspired consolidation pipeline, and memory corruption) enrich rather than displace the expected content.
- `fl`: Real-World Lessons: Challenges and Best Practices:
**1:** The compression and product-design sub-topics appear in the same order as the expected section.
- `de`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=3; quality=strong,strong,strong] (1) 'Summarization drift' traces to the exploration-phase Practical Guide's Failure Modes section. (2) The background 'consolidation pipeline' or 'dreaming' process that periodically reviews, merges, and prunes memories is a specific implementation pattern traced to the exploration-phase Teaching Alfred source's DreamPromotion mechanism (also credited as breadth below, since the same instance qualifies for both). (3) 'Memory corruption', where a single poisoned entry silently corrupts future decisions, traces directly to the exploration-phase Galileo failure-modes article, which names memory corruption as one of seven agent failure patterns. All three are named, specific mechanisms — strong.
- `be`: Real-World Lessons: Challenges and Best Practices:
**1:** [instances=1; quality=strong] The same consolidation-pipeline/'dreaming' addition is explicitly framed as 'inspired by how the human brain solidifies knowledge during sleep', qualifying independently as a cross-domain (neuroscience) analogy per the instruction that one instance can satisfy both depth and breadth. Strong given the specific named mechanism and explanation.
- `cp`: Real-World Lessons: Challenges and Best Practices:
**1:** Both depth_enhancement and breadth_enhancement are 1 here, so this is evaluated rather than defaulted: the three additions are distributed one per subsection, each a sentence or two; the three expected lessons remain the section's clear focus. No dilution.
- `ga`: Real-World Lessons: Challenges and Best Practices:
**1:** At 444 prose-only words against a 500-word target (tolerance floor ~450 words), this section is 6 words under the floor — within the trivial-margin grace used elsewhere in this set (roughly 12.5 words on a 50-word band), so scored as passing. Content covers all three guideline points in the guideline's own order, with the three additions closely related to the topics they sit under.

## Section: S5::section-5-memory-implementations-with-code-examples  (weight=0.187, contribution=-0.0200 AGAINST light)
Stored section rewards: light=0.1700  standard=0.2978  (explore: light=0.0000  standard=0.0875)

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset1`

**Article text:**
```
## Memory Implementations with Code Examples

This section provides code examples for implementing different memory types using the `mem0` library. While RAG is the mechanism for retrieving information, a topic we will cover in the next lesson, creating high-quality memories is an equally important preceding step. We will use a simple "raw strings" storage approach to focus on the creation and benefits of each memory category.

### What is mem0?

`mem0` is an open-source memory layer for AI agents that simplifies the process of adding long-term memory. It handles the extraction, storage, and retrieval of information, allowing developers to make their agents stateful with just a few lines of code. It supports various backends, including vector stores and graph databases, and can be configured to use different LLMs and embedding models. Its architecture is designed to dynamically extract, consolidate, and retrieve salient information from conversations [[19]](https://arxiv.org/html/2504.19413).

### Setup

Before diving into specific memory types, we need to set up our environment. This involves configuring `mem0` to use Gemini for both the LLM and embeddings, and ChromaDB as a local vector store. We also define a few helper functions to simplify adding and searching for memories.

1.  First, we configure `mem0` to use Gemini for embeddings and the LLM, with ChromaDB as the local vector store.
    ```python
    import os
    from mem0 import Memory
    
    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
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
                "model": "gemini-2.5-pro",
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
    }
    
    memory = Memory.from_config(MEM0_CONFIG)
    MEM_USER_ID = "lesson9_notebook_student"
    memory.delete_all(user_id=MEM_USER_ID)
    ```
    It outputs:
    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

2.  Next, we define helper functions to add text to memory and search for it. `mem_add_text` stores text verbatim, while `mem_search` is a wrapper that allows optional filtering by category.
    ```python
    from typing import Optional

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
    ```

### Semantic Memory: Extracting Facts

Semantic memory is created through an extraction pipeline. An LLM processes conversation text with a prompt designed to pull out atomic facts, which are then stored. For example, a prompt might instruct the model to identify persistent facts and strong preferences from a user's message.

A typical extraction prompt might be:
```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent.
- Note subtle details that might be important.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting. He gifted me a painting a few years ago. It's really beautiful.}
```
The system would store facts like: `Mark is the user's brother.`, `Mark is a software engineer.`, `Mark's real passion is painting.`, and `The user has a beautiful painting from Mark.`

Retrieval often uses hybrid search, which we will cover in the next lesson. It combines keyword filtering (e.g., finding all memories containing "brother") with semantic search (e.g., matching the query "job" to the stored fact "is a software engineer").

Let's see this in code.

1.  We insert a few facts as individual strings, tagging them with the "semantic" category.
    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    ```
    It outputs:
    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    ```

2.  We can now search for a specific fact using a natural language query.
    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memory functions as a chronological log. Memories can be raw conversation turns or summaries created by an LLM, but they always include a timestamp. For instance, an input like `User: "I'm feeling stressed about my project deadline on Friday."` could be stored raw with its timestamp or summarized as `User is stressed about a Friday deadline.`

Retrieval is a blend of temporal and semantic queries. A user might ask, "What did we talk about yesterday?" (a temporal query), or "What was I worried about earlier?" (a semantic query, likely ranked by recency).

Here is how we can implement this.

1.  We define a short dialogue and use the Gemini client to summarize it into a single, concise "episode."
    ```python
    from google import genai
    client = genai.Client()
    MODEL_ID = "gemini-2.5-pro"

    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]
    
    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.
    
    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    ```

2.  We save this summary as an episodic memory, including metadata about the original interaction.
    ```python
    print(
        mem_add_text(
            episode,
            category="episodic",
            summarized=True,
            turns=4,
        )
    )
    ```
    It outputs:
    ```text
    Saved episodic memory.
    ```

3.  Later, we can retrieve this episode using a semantic search.
    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory is unique because it can be created in two ways: developer-defined or user-taught.

**Developer-Defined** skills are explicitly coded tools or functions, like a `book_flight()` procedure. This is the most common approach. Let's implement a simple developer-defined procedure.

1.  We define a multi-step procedure as a text block and save it to memory with the "procedure" category.
    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))
    
    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    ```
    It outputs:
    ```text
    Saved procedure memory.
    ```

2.  We can then retrieve this procedure by searching for its purpose.
    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```
    It outputs:
    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```

**User-Taught** skills allow advanced agents to learn new procedures dynamically. When a user provides explicit steps, the agent can save this sequence as a new, callable procedure. For example, a prompt could instruct the agent to use a `learn_procedure` tool when it sees a numbered list of steps.

An example prompt for this might be:
```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```
The agent would then generate and save a new structured procedure to its library. Retrieval for both types is an intent-matching process where the LLM compares the user's request against all available procedures and executes the best match.

We have seen how to implement different types of memories. Now, let's talk about some additional considerations when building a memory system.
```
**Grader reasoning:**
- `cc`: Memory Implementations With Code Examples:
**1:** Both sections provide code examples for semantic, episodic, and procedural memory using the `mem0` library. The procedural memory sub-section in the generated article explicitly covers both the Developer-Defined and User-Taught approaches, including the required `find_summer_cabin` example prompt demonstrating how an agent learns a new skill dynamically. The embedding model name difference (`gemini-embedding-001` vs `text-embedding-004`) is a configuration parameter, not a substantive idea difference — CoreContent is strictly about ideas, not implementation parameters.
- `fl`: Memory Implementations With Code Examples:
**0:** Both sections follow a similar flow: setup, semantic memory example, episodic memory example, and procedural memory example. The user-taught procedural memory content is present in the generated section. However, the expected section places a 💡 Tip callout (containing a Colab notebook link) before the setup code block — a media element that is absent from the generated section. A missing media element at a position where the expected section places one constitutes a flow failure.
- `de`: Memory Implementations With Code Examples:
**0:** [instances=0] No depth additions present. The extra H3 header “### What is mem0?” (describing dynamic extraction, consolidation, and retrieval architecture) was reviewed but disqualified because its content cannot be traced to any exploration-phase source for this episode. It also does not intensify the core topic of providing code examples for creating the three memory types.
- `be`: Memory Implementations With Code Examples:
**0:** [instances=0] No breadth additions present. The section is a practical code walkthrough and does not expand into adjacent concepts or historical context traceable to exploration-phase sources.
- `cp`: Memory Implementations With Code Examples:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default.
- `ga`: Memory implementations with code examples:
**1:** The generated section meets all content requirements from the guideline. It covers 'What is mem0?' as an introductory subsection and implements all three memory types (Semantic, Episodic, Procedural) with code examples. Procedural memory includes both the Developer-Defined and User-Taught approaches, with the required `find_summer_cabin` example prompt demonstrating how an agent learns a new procedure. The guideline does not require exact 0-3 subsection numbering or the Colab notebook link as mandatory content elements — the substance of all required content is present. All requirements are met.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset1`

**Article text:**
```
## Memory Implementations with Code Examples

This section details how to implement the different memory types. While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, creating high-quality memories is an equally important preceding step. We will cover RAG in the next lesson. To focus on the benefits of each memory category, we will use the "raw strings" storage approach.

### What is mem0?

We will use `mem0`, an open-source memory library, to demonstrate these concepts. It provides a simple API for adding and searching memories, handling the underlying storage and retrieval logic. It automates the pipeline from raw text to indexed memories, using an LLM for extraction and consolidation, and supports various storage backends like vector databases and knowledge graphs [[11]](https://arxiv.org/html/2504.19413).

### Setup

1.  First, we configure `mem0` with our Gemini model, embeddings, and a local ChromaDB vector store.
    ```python
    import os
    import re
    from typing import Optional

    from google import genai
    from mem0 import Memory
    from utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])

    client = genai.Client()
    MODEL_ID = "gemini-2.5-pro"

    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
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
    ```
    It outputs:
    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

2.  Next, we define helper functions to add and search for memories, tagging them with a category.
    ```python
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
    ```

### Semantic Memory: Extracting Facts

**How it's created:** Semantic memory is created through a deliberate extraction pipeline. An LLM processes unstructured text with a specific prompt designed to extract factual data, turning messy conversation threads into a queryable knowledge base. For example, a prompt might instruct the model to identify persistent facts and strong preferences, keeping each fact atomic and context-independent [[13]](https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer).

Example Extraction Prompt (For a general personal assistant):
```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or sublte details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```
Memory Created: The system would store: `Mark is the user's brother. Mark is a software engineer. Mark's real passion is painting. The user has a painting from Mark and finds it beautiful.`.

**How it's retrieved:** Retrieval often uses hybrid search, which combines keyword filtering and semantic relevance. The system first narrows the search based on exact matches for known entities (e.g., "brother") and then performs a vector search within that set to find the most contextually relevant fact (e.g., "job" is similar to "software engineer").

1.  We insert a few example facts as atomic strings.
    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    ```
    It outputs:
    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    ```

2.  We can now search for a specific fact using a natural language query.
    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

**How it's created:** Episodic memory functions as a chronological log. An LLM can read conversation messages over a period and summarize the key events, which are then stored with a timestamp. This can be a raw log of the conversation or a summarized version.

Example Input: `User: "I'm feeling stressed about my project deadline on Friday.", Assistant: "I'm sorry to hear that. I'm here to help you with that."`
Memory Created (raw): `October 26th, 2025. 2:30PM EST: User: "I'm feeling stressed about my project deadline on Friday." Assistant: "I'm sorry to hear that. I'm here to help you with that."`
Memory Created (summarized): `October 26th, 2025. 2:30PM EST User: "The user is stressed about their project deadline on Friday and the assistant offers to help."`

**How it's retrieved:** Retrieval is a blend of temporal and semantic queries. A simple retrieval might filter by a date range ("What did we talk about yesterday?"). A more robust approach uses semantic search to find contextually similar conversations and then re-ranks the results by recency.

1.  We define a short dialogue and ask the LLM to summarize it into a concise "episode."
    ```python
    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]

    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.

    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    ```

2.  We save this summary as an episodic memory with additional metadata.
    ```python
    print(
        mem_add_text(
            episode,
            category="episodic",
            summarized=True,
            turns=4,
        )
    )
    ```
    It outputs:
    ```text
    Saved episodic memory.
    ```

3.  Later, we can search for this "experience" using a semantic query.
    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

### Procedural Memory: Defining and Learning Skills

**How it's created:** Procedural memory can be created in two ways. A developer can explicitly code a tool or function, or a more advanced agent can learn a new procedure from a user's instructions. When a user provides a numbered list of steps, the agent can convert this into a reusable procedure.

Example Prompt:
```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```
Memory Created: The LLM would generate a new structured procedure and save it to its tool/procedures library: `procedure_name: find_summer_cabin`, `steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options`.

**How it's retrieved:** Retrieval is an intent-matching and function-calling process. The agent's LLM receives the descriptions of all available procedures in its context. It then compares the user's request against these descriptions to find the best semantic match and execute the corresponding function.

1.  We define a procedure as a text block containing a name and a series of steps.
    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))

    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    ```

2.  The agent can then retrieve this procedure by searching for a related intent.
    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```
    It outputs:
    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```

Now that we have seen how to implement these memory types, let's discuss some additional considerations for building a production-ready memory system.
```
**Grader reasoning:**
- `cc`: Memory Implementations with Code Examples:
**1:** Both sections walk through mem0 setup, then Semantic, Episodic, and Procedural memory with matching code, outputs, and explanatory prose. The generated section's 'What is mem0?' subsection matches the article guideline's own outline and is an addition, not an omission.
- `fl`: Memory Implementations with Code Examples:
**1:** The mem0 introduction, setup, and three memory-type walkthroughs appear in the same order with the same code-then-output-then-explanation pattern throughout.
- `de`: Memory Implementations with Code Examples:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources do exist for this episode, so this is a content-based 0 (nothing to trace), not the code-level hard zero that applies when no exploration sources exist at all.
- `be`: Memory Implementations with Code Examples:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources do exist for this episode, so this is a content-based 0 (nothing to trace), not the code-level hard zero that applies when no exploration sources exist at all.
- `cp`: Memory Implementations with Code Examples:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default, since there are no qualifying additions to evaluate for dilution of the ground truth core.
- `ga`: Memory Implementations with Code Examples:
**0:** At 784 prose-only words against a 500-word target (tolerance ceiling ~550 words), this section is substantially over length, which alone drives this score to 0. Content otherwise matches the guideline's outline point for point, and the code is verified faithful to the notebook, including the 'gemini-2.5-pro' MODEL_ID and 'lesson9_memories' collection name.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset1`

**Article text:**
```
## Memory Implementations with Code Examples

This section provides code examples for implementing the different memory types using the `mem0` library. While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, a topic we will cover in the next lesson, the creation of high-quality memories is an equally important preceding step. To focus on the benefits of each memory category, we will use the simple "storing memories as raw strings" approach.

### What is mem0?

`mem0` is an open-source memory layer for AI agents that automates the pipeline from input text to injected memories [[15]](https://arxiv.org/html/2504.19413). It can extract facts, consolidate information, and store it for later retrieval. It supports various backends, including vector and graph databases, making it a flexible tool for experimenting with different memory architectures. We will use it to demonstrate how to create and retrieve semantic, episodic, and procedural memories.

### Setup

First, we set up our environment by installing the necessary packages and configuring the Gemini client and `mem0`. We will use Gemini for both the LLM and embeddings, with ChromaDB as a local vector store.

1.  We define our configuration for `mem0`, specifying Gemini as the provider for both the LLM and embeddings, and ChromaDB as our local vector store.

    ```python
    import os
    from mem0 import Memory
    
    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
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
    ```

2.  Next, we create a few helper functions to add and search for memories. `mem_add_text` saves a string with a category tag, and `mem_search` wraps the search functionality to allow filtering by category.

    ```python
    from typing import Optional

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
    ```

### Semantic Memory: Extracting Facts

Semantic memory is created through an extraction pipeline. An LLM analyzes unstructured text and extracts factual data, turning messy conversation threads into a queryable knowledge base. The prompt for this task typically instructs the model to identify persistent facts, user preferences, and key attributes.

For example, a prompt might be:
```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or subtle details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```
The system would then store facts like: `Mark is the user's brother`, `Mark is a software engineer`, and `Mark's real passion is painting`. Retrieval often uses a hybrid search, which combines keyword search with semantic relevance. First, the system filters the memory store for exact matches of known entities (e.g., all memories containing "brother"). Then, a vector search is performed on this subset to find the most contextually relevant fact, matching "job" with "software engineer."

1.  We add several facts to our semantic memory.

    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    ```
    It outputs:
    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    ```

2.  Now, we can search for a specific fact using a natural language query.

    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memory functions as a chronological log. Memories can be created by having an LLM summarize a conversation or by simply logging the raw text with a timestamp. If we want to create a summary, the prompt might instruct the model to distill a short exchange into a concise "episode."

For example, given the input `User: "I'm feeling stressed about my project deadline on Friday."`, a raw episodic memory would be `October 26th, 2025, 2:30PM EST: User: "I'm feeling stressed about my project deadline on Friday."`. A summarized version might be `October 26th, 2025, 2:30PM EST: The user is stressed about their project deadline and the assistant offers to help.` Retrieval combines temporal filtering (e.g., "yesterday") with semantic search to find contextually similar past events, often re-ranking results by recency.

1.  We define a short dialogue and use the LLM to create a concise summary.

    ```python
    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]
    
    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.
    
    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    ```

2.  We save this summary as an episodic memory with additional metadata.

    ```python
    print(
        mem_add_text(
            episode,
            category="episodic",
            summarized=True,
            turns=4,
        )
    )
    ```
    It outputs:
    ```text
    Saved episodic memory.
    ```

3.  Later, we can retrieve this "experience" using a semantic query.

    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory can be created by a developer who explicitly codes a tool or function, or it can be learned dynamically from user interactions. For example, an agent can be prompted to convert a user's step-by-step instructions into a reusable procedure. Retrieval is an intent-matching process where the LLM compares a user's request against the descriptions of all available procedures and executes the best match.

1.  We define a simple procedure as a text block containing a name and a list of steps.

    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))
    
    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    ```

2.  When the user expresses an intent that matches this procedure, the agent can retrieve and "run" it.

    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```
    It outputs:
    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```

Now that we have seen how to implement these memory types, let's discuss some additional considerations for building a production-ready memory system.
```
**Grader reasoning:**
- `cc`: Memory Implementations with Code Examples:
**0:** Both sections walk through mem0 setup, then Semantic, Episodic, and Procedural memory with matching explanatory prose. However, the generated section's Setup code block never defines `MODEL_ID` or `client`, both of which are referenced later (`model=MODEL_ID`, `client.models.generate_content`) in the Episodic Memory code — the actual notebook defines both during Setup (`client = genai.Client()`, `MODEL_ID = "gemini-2.5-pro"`), so this is code that would raise a NameError as written, not just an incomplete-but-functional excerpt. A working setup is a core expected element of this section, so this is scored as a content gap rather than a purely stylistic difference.
- `fl`: Memory Implementations with Code Examples:
**1:** The mem0 introduction, setup, and three memory-type walkthroughs appear in the same order with the same code-then-output-then-explanation pattern; the missing lines are an omission within the code itself, not a reordering of the section's steps.
- `de`: Memory Implementations with Code Examples:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist for this episode, so this is a content-based 0 (nothing to trace), not the code-level hard zero that applies when no exploration sources exist at all.
- `be`: Memory Implementations with Code Examples:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist for this episode, so this is a content-based 0 (nothing to trace), not the code-level hard zero that applies when no exploration sources exist at all.
- `cp`: Memory Implementations with Code Examples:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default.
- `ga`: Memory Implementations with Code Examples:
**0:** At 695 prose-only words against a 500-word target (tolerance ceiling ~550 words), this section is over length, which alone drives this score to 0. Independently, the Setup code omits the `MODEL_ID` and `client` definitions that the actual notebook includes and that later code in this same section depends on — a fidelity gap against 'use the code from the provided notebook' beyond just the length issue.

### Arm: standard (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset3`

**Article text:**
```
## Memory Implementations with Code Examples

This section provides practical examples of how to implement different memory types. It is important to distinguish between a stateless retrieval pattern like RAG and a stateful memory system. RAG is a lookup pipeline; it retrieves information from a static knowledge base to ground a response. Memory, by contrast, is a dynamic system that changes over time based on interactions, creating a persistent, evolving model of the user and the conversation [[16]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l). We will cover RAG in Lesson 10. Here, we focus on creating stateful memory with `mem0`, an open-source library for this purpose.

`mem0` is a universal memory layer for AI agents that simplifies the process of adding long-term memory to applications. It handles the extraction, storage, and retrieval of information, allowing developers to make their agents stateful with just a few lines of code. It supports various backends, including vector stores and graph databases, and provides a flexible API for managing different types of memory [[17]](https://arxiv.org/html/2504.19413v1).

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 9 in the course's GitHub repository.

</aside>

### Setup

`mem0` provides a memory layer that can work with various backends. For our examples, we will configure it to use Google's Gemini for both the LLM and embeddings, with ChromaDB as a local vector store that runs directly in our notebook [[17]](https://arxiv.org/html/2504.19413v1).

1.  First, we configure `mem0` to use our Gemini client for fact extraction, the Gemini embedding model, and a local ChromaDB instance for storage.

    ```python
    import os
    from mem0 import Memory
    
    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
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
                "model": "gemini-2.5-pro",
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
    }
    
    memory = Memory.from_config(MEM0_CONFIG)
    MEM_USER_ID = "lesson9_notebook_student"
    memory.delete_all(user_id=MEM_USER_ID)
    print("✅ Mem0 ready (Gemini embeddings + local Chroma).")
    ```

    It outputs:

    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

2.  Next, we define a few helper functions to add and search for memories. `mem_add_text` stores a string with a category tag, and `mem_search` wraps the search functionality to allow filtering by that category.

    ```python
    from typing import Optional
    
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
    ```

### Semantic Memory: Extracting Facts

Semantic memory is created through a deliberate extraction pipeline. Unstructured text is passed to an LLM with a prompt designed to pull out atomic facts. For a personal assistant, a prompt might look like this:

```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent.
- Notice subtle details that might be important.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting. He gifted me a painting a few years ago. It's really beautiful.}
```

The system would then store facts like: `Mark is the user's brother.`, `Mark is a software engineer.`, `Mark's real passion is painting.`, and `The user has a beautiful painting from Mark.`

1.  Let's add a few semantic facts to our memory.

    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    
    print(f"Added {len(facts)} semantic memories.")
    ```

    It outputs:

    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Added 4 semantic memories.
    ```

2.  Now, we can retrieve a specific fact using a natural language query. Retrieval often uses hybrid search, combining keyword filtering with semantic search. For a query like "brother job," the system would first filter for memories containing "brother" and then perform a vector search to find the most contextually relevant fact.

    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```

    It outputs:

    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memories function as a chronological log. They can be created by having an LLM summarize a conversation or simply by logging the raw text with a timestamp.

1.  We will simulate a short dialogue and use an LLM to create a concise summary.

    ```python
    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]
    
    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.
    
    {dialogue}
    """
    episode_summary = client.models.generate_content(model="gemini-2.5-pro", contents=episodic_prompt)
    episode = episode_summary.text.strip()
    print(episode)
    ```

    It outputs:

    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

2.  We add this summary to our episodic memory, along with some metadata.

    ```python
    print(
        mem_add_text(
            episode,
            category="episodic",
            summarized=True,
            turns=4,
        )
    )
    ```

    It outputs:

    ```text
    Saved episodic memory.
    ```

3.  Retrieval from episodic memory blends temporal and semantic queries. A user could ask "What did we talk about yesterday?" to filter by date. Or, as we do here, they can search semantically for a past event. `mem0` automatically adds a `created_at` timestamp, which is useful for temporal filtering [[18]](https://docs.mem0.ai/platform/features/timestamp).

    ```python
    print("\nSearch --> 'deadline stress'\n")
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
        print(f"Created at: {h['created_at']}")
    ```

    It outputs:

    ```text
    
    Search --> 'deadline stress'
    
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    
    Created at: 2025-09-12T02:30:01.358468-07:00
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory can be created by a developer who explicitly codes a tool or function. More advanced agents can also learn new procedures from user instructions. A prompt to enable this might look like:

```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```

1.  Let's teach our agent a procedure for creating a monthly report by saving the steps as a single text block.

    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))
    
    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    
    print(f"Learned procedure: {procedure_name}")
    ```

    It outputs:

    ```text
    Learned procedure: monthly_report
    ```

2.  Retrieval is an intent-matching process. The agent compares the user's request against the descriptions of all available procedures. If there is a semantic match, it executes the corresponding steps.

    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```

    It outputs:

    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```

We have seen how to implement the different memory types. Now, let's discuss some of the real-world challenges you will face when building a memory system.
```
**Grader reasoning:**
- `cc`: Memory Implementations With Code Examples:
**1:** Both sections provide identical substantive content: the mem0 configuration structure, helper functions (`mem_add_text`, `mem_search`), semantic extraction pipeline and stored facts, episodic summarisation via `episodic_prompt`, and procedural memory with the `find_summer_cabin` and `monthly_report` examples. The different Gemini model names ("gemini-2.5-pro"/"gemini-embedding-001" vs. "gemini-2.5-flash"/"text-embedding-004") are configuration parameters, not substantive ideas; per the CoreContent criterion, model names and configuration details are excluded from evaluation.
- `fl`: Memory Implementations With Code Examples:
**0:** Both sections follow the same logical flow: introducing the distinction between RAG and stateful memory, setting up the `mem0` library, and then providing implementation examples for each of the three memory types in the same order. The generated section omits the introductory paragraph from the expected output that distinguishes between the helper functions and their use as tools in an agentic application.
- `de`: Memory Implementations With Code Examples:
**0:** [instances=0] No depth additions present. The section provides code examples and explanations that are parallel to the expected output, without adding deeper technical nuances or discussing implementation challenges beyond what is covered in the ground truth.
- `be`: Memory Implementations With Code Examples:
**0:** [instances=0] No breadth additions present. The section is a practical implementation guide and does not expand into adjacent topics.
- `cp`: Memory Implementations With Code Examples:
**1:** Both depth_enhancement and breadth_enhancement scored 0, meaning no qualifying additions were identified. CorePreservation scores 1 by default.
- `ga`: Memory implementations with code examples:
**1:** The generated section covers all required guideline components: (1) mem0 introduction ("mem0 is a universal memory layer for AI agents…"), (2) Semantic Memory — extraction pipeline, extraction prompt template, stored facts description ("The system would then store facts like…"), and hybrid search retrieval, (3) Episodic Memory — `episodic_prompt` summarisation prompt with example input, memory output, and retrieval, (4) Procedural Memory — `learn_procedure` example prompt with the `find_summer_cabin` example, code to store the procedure, and intent-matching retrieval. The guideline's sub-section labels are a sketch; all required content is present in the generated section. The prose-only word count is approximately 510 words, which is within the 500-word target.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset3`

**Article text:**
```
## Memory implementations with code examples

This section provides a practical look at how to implement the different types of long-term memory. While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, the creation of high-quality memories is an equally important, preceding step. In production systems, retrieval is rarely a single vector search. A common pattern is to first fetch a larger set of candidate memories and then use a more sophisticated, and often more expensive, reranking model to re-order the candidates for final selection. This second pass improves the precision of what goes into the context window [[51]](https://mem0.ai/blog/state-of-ai-agent-memory-2026). This two-stage process computationally mirrors the cognitive science concept of pattern separation, where the brain distinguishes between similar experiences to avoid blurring them together. The reranker's job is to ensure the final context is not just relevant, but also diverse [[53]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l). We will cover RAG in detail in our next lesson. Here, we will focus on the memory creation process for each memory type, using the simple "storing memories as raw strings" approach to highlight the unique benefits of each category.

To do this, we will use `mem0`, an open-source library designed to add long-term memory to AI agents [[4]](https://arxiv.org/html/2504.19413). It provides a simple interface for storing, searching, and managing different types of memories.

### Setup

First, let's set up our environment. We will configure `mem0` to use Gemini for both embeddings and the underlying LLM for fact extraction, with ChromaDB as a local vector store. This allows us to run everything in our notebook.

1.  We start by loading our environment variables and importing the necessary packages.
    ```python
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    import os
    import re
    from typing import Optional
    
    from google import genai
    from mem0 import Memory
    ```
    It outputs:
    ```text
    Environment variables loaded from /Users/fabio/Desktop/course-ai-agents/.env
    Environment variables loaded successfully.
    ```

2.  Next, we initialize the Gemini client and define our model ID.
    ```python
    client = genai.Client()
    MODEL_ID = "gemini-2.5-pro"
    ```

3.  We then configure `mem0` with our Gemini models and a local ChromaDB instance for storage.
    ```python
    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
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
    ```
    It outputs:
    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

4.  Finally, we create a few helper functions to simplify adding and searching for memories. `mem_add_text` will store raw text with a category tag, and `mem_search` will allow us to search and filter by that category.
    ```python
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
        Returns a list of results.
        """
        res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}
    
        items = res.get("results", [])
        if category is not None:
            items = [r for r in items if (r.get("metadata") or {}).get("category") == category]
        return items
    ```

### Semantic Memory: Extracting Facts

**How it's created:** While semantic memory is often created through a deliberate extraction pipeline where an LLM processes unstructured text, for our example, we will take a simpler approach. We will directly add pre-defined, atomic facts as raw strings. This aligns with our goal of demonstrating the core mechanics of storing and retrieving different memory types without adding the complexity of an extraction layer. The `infer=False` parameter in our `mem_add_text` function ensures that `mem0` does not trigger its own LLM-based fact extraction, giving us direct control.

**Prompt Used to Create:** In a more advanced implementation, you would use a prompt to guide the LLM's extraction process. For a personal assistant, such a prompt might look like this:
```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or subtle details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```

**Memory Created:** From the prompt above, the system would ideally store individual facts like: `Mark is the user's brother.`, `Mark is a software engineer.`, `Mark's real passion is painting.`, and `The user has a beautiful painting from Mark.`.

**How it's Retrieved:** Retrieval of semantic memory often uses hybrid search. The system first filters the memory store based on keyword matches for known entities (e.g., "brother"). Then, within that filtered set, a vector search is performed to find the most contextually relevant fact (e.g., the one most similar to "job").

Let's implement this by adding a few facts to our semantic memory.

1.  We define a list of facts and use our helper function to add them to `mem0` with the category "semantic".
    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    
    print(f"Added {len(facts)} semantic memories.")
    ```
    It outputs:
    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Added 4 semantic memories.
    ```

2.  Now, we can search for a specific fact. When we query for "brother job", the system retrieves the most relevant fact.
    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

**How it's Created:** Episodic memory functions as a chronological log of events. Memories can be created by having an LLM read a conversation and summarize the key insights, or by simply logging the raw text of the interaction with a timestamp.

**Prompt Used to Create:** If summarizing, the prompt might be: "You are a personal coding tutor. Extract events, likes, dislikes, or any other insights from the conversation that will help you better teach the user." For raw storage, no extraction prompt is needed.

**Memory Created (raw):** `October 26th, 2025. 2:30PM EST: User: "I'm feeling stressed about my project deadline on Friday." Assistant: "I'm sorry to hear that. I'm here to help you with that."`

**Memory Created (summarized):** `October 26th, 2025. 2:30PM EST: The user is stressed about their project deadline on Friday and the assistant offers to help.`

**How it's Retrieved:** Retrieval from episodic memory is often a blend of temporal and semantic queries. A user might ask, "What did we talk about yesterday?" (a temporal query). A more robust approach uses semantic search to find contextually similar conversations and then re-ranks the results by recency.

Let's create a summarized episodic memory.

1.  We start with a short dialogue and use an LLM to create a concise summary.
    ```python
    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]
    
    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.
    
    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    print(episode)
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

2.  We add this summary to our memory with the category "episodic".
    ```python
    print(
        mem_add_text(
            episode,
            category="episodic",
            summarized=True,
            turns=4,
        )
    )
    ```
    It outputs:
    ```text
    Saved episodic memory.
    ```

3.  When we search for "deadline stress", the system retrieves our summarized episode, complete with its creation timestamp.
    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
        print(h)
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    
    {'id': '93ebb9eb-65b0-4975-9c0d-105497b43e5c', 'memory': 'A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.', 'hash': '44f0bcd0965a1fb557c1d3b5a9f8ae6c', 'metadata': {'turns': 4, 'summarized': True, 'category': 'episodic'}, 'score': 0.9109697937965393, 'created_at': '2025-09-12T02:30:01.358468-07:00', 'updated_at': None, 'user_id': 'lesson9_notebook_student', 'role': 'user'}
    ```

### Procedural Memory: Defining and Learning Skills

**How it's Created:** Procedural memory can be created in two ways: either defined by a developer as a tool or function (e.g., `book_flight()`), or learned dynamically from user interactions. More advanced agents can save a sequence of steps provided by a user as a new, callable procedure.

**Example Prompt:**
```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```

**Memory Created:** The LLM would generate a new structured procedure and save it to its tool/procedures library: `procedure_name: find_summer_cabin`, `steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options`.

**How it's Retrieved:** Retrieval is an intent-matching and function-calling process. The agent is given access to its entire library of procedures—both built-in and user-taught. The LLM receives the descriptions of all available tools in its context and compares the user's current request against them. If the user later says, "Let's find a summer cabin again," the agent will recognize the semantic similarity to its newly learned `find_summer_cabin` procedure and execute it.

Let's teach our agent a simple procedure.

1.  We define the steps for a "monthly_report" procedure and store it as a single text block.
    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))
    
    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    
    print(f"Learned procedure: {procedure_name}")
    ```
    It outputs:
    ```text
    Learned procedure: monthly_report
    ```

2.  When we search for "how to create a monthly report", the system retrieves our newly learned procedure.
    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```
    It outputs:
    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```

We have now seen how to implement the three main types of long-term memory. While these examples are simple, they illustrate the core mechanics of memory creation and retrieval. Now, let's discuss some of the real-world challenges and best practices for building memory systems.
```
**Grader reasoning:**
- `cc`: Memory implementations with code examples:
**1:** Both sections walk through mem0 setup, then Semantic, Episodic, and Procedural memory with matching code, outputs, and prose. Code fidelity checked out fully this time, including `client` and `MODEL_ID` both being properly defined during Setup (unlike a preset-1 article where these were referenced but never defined). The retrieval-reranking and pattern-separation additions (verified below) enrich rather than displace the expected content.
- `fl`: Memory implementations with code examples:
**1:** The mem0 introduction, setup, and three memory-type walkthroughs appear in the same order with the same code-then-output-then-explanation pattern.
- `de`: Memory implementations with code examples:
**1:** [instances=1; quality=strong] 'A common pattern is to first fetch a larger set of candidate memories and then use a more sophisticated... reranking model to re-order the candidates for final selection' traces to the exploration-phase 'State of AI Agent Memory 2026' source's discussion of production retrieval pipelines. A specific implementation pattern beyond a passing mention — strong.
- `be`: Memory implementations with code examples:
**1:** [instances=1; quality=strong] 'This two-stage process computationally mirrors the cognitive science concept of pattern separation, where the brain distinguishes between similar experiences to avoid blurring them together' traces directly to the exploration-phase 'Teaching Alfred' source's dentate-gyrus/pattern-separation section, including the same 're-ranking for diversity' computational analogy (MMR). Strong: named cross-domain mechanism, distinct from the hippocampus/neocortex instance credited to the Layers-of-Memory section.
- `cp`: Memory implementations with code examples:
**1:** Both depth_enhancement and breadth_enhancement are 1 here, so this is evaluated rather than defaulted: the reranking/pattern-separation aside is a single paragraph before the mem0 walkthrough begins; the full setup, code, and three memory-type implementations remain completely intact and are clearly the section's dominant content. No dilution, though this is the longest section in the article (1,135 words) and worth being aware of for that reason even though the specific additions here are not what's driving the length.
- `ga`: Memory implementations with code examples:
**0:** At 1,135 prose-only words against a 500-word target (tolerance ceiling ~550 words), this section is dramatically over length — more than double the target, the largest overage of any section graded in this set — which alone drives this score to 0.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset3`

**Article text:**
```
## Memory Implementations with Code Examples

Now that we know what to save and how to store memories, let's look at some code examples. While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, a topic we will cover in the next lesson, the creation of high-quality memories is an equally important preceding step. We will use the open-source `mem0` library to demonstrate how to implement each memory type, focusing on the simple "raw strings" storage approach to highlight the benefits of each category [[9]](https://arxiv.org/html/2504.19413).

### What is mem0?

`mem0` is a memory layer for AI agents that handles the extraction, storage, and retrieval of information. It can be configured with different LLMs, embedding models, and vector stores, providing a flexible foundation for building stateful agents.

### Setup

First, we will set up our environment. This involves configuring `mem0` to use Google's Gemini models for both fact extraction and embeddings, and ChromaDB as a local vector store. We also define a few helper functions to simplify adding and searching for memories.

1.  We start by configuring `mem0`. We will use the `gemini-2.5-pro` model for LLM operations and `gemini-embedding-001` for creating embeddings. The vector store will be a local ChromaDB instance.
    ```python
    import os
    from typing import Optional
    from mem0 import Memory

    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
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
                "model": "gemini-2.5-pro",
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
    }

    memory = Memory.from_config(MEM0_CONFIG)
    MEM_USER_ID = "lesson9_notebook_student"
    memory.delete_all(user_id=MEM_USER_ID)
    print("✅ Mem0 ready (Gemini embeddings + local Chroma).")
    ```
    It outputs:
    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

2.  Next, we define two helper functions. `mem_add_text` saves a string to memory with a specified category, and `mem_search` retrieves memories, with an option to filter by category.
    ```python
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
        """Category-aware search wrapper."""
        res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}
        items = res.get("results", [])
        if category is not None:
            items = [r for r in items if (r.get("metadata") or {}).get("category") == category]
        return items
    ```

### Semantic Memory: Extracting Facts

Semantic memory is created through a deliberate extraction pipeline. An LLM analyzes unstructured text and extracts discrete facts, turning messy conversations into a queryable knowledge base. The extraction prompt is key; for a personal assistant, it might focus on persistent facts and strong preferences [[14]](https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer). For example, a prompt could be:

```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or subtle details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```

The system would then store facts like: `Mark is the user's brother. Mark is a software engineer. Mark's real passion is painting. The user has a painting from Mark and finds it beautiful.`.

Retrieval of semantic memory is where hybrid search is useful. This combines keyword search for exact matches with semantic search for contextual relevance. First, the system filters the memory store for known entities or tags (e.g., all memories containing "brother"). Then, within that filtered set, a vector search finds the most contextually relevant fact. The query "job" will have high semantic similarity to the stored memory "is a software engineer," ensuring a relevant answer.

1.  Let's add a few facts to our semantic memory. These are short, atomic pieces of information about the user.
    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        mem_add_text(f, category="semantic")

    print(f"Added {len(facts)} semantic memories.")
    ```
    It outputs:
    ```text
    Added 4 semantic memories.
    ```

2.  Now, we can search for a specific fact using a natural language query.
    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memories function as a chronological log. They can be created by having an LLM read conversation messages for a period, like a day, and then summarize the key events. These memories will have a timestamp and can be stored raw or summarized. For a coding tutor, the prompt might be: *"You are a personal coding tutor... extract events, likes, dislikes, or any other insights from the conversation text that will serve to better teach the user."*

Retrieval from episodic memory is often a blend of temporal and semantic queries. A simple retrieval might filter by a date range ("What did we talk about yesterday?"). A more robust approach uses semantic search to find contextually similar conversations and then re-ranks the results by recency. For example, if a user asks, "What was that thing I was worried about earlier?" the system would search for past messages with a "worried" or "stressed" sentiment and prioritize the most recent ones.

1.  We will simulate a short dialogue and use an LLM to create a concise summary, which we will store as an "episode".
    ```python
    from google import genai
    client = genai.Client()
    MODEL_ID = "gemini-2.5-pro"

    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]

    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.

    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    print(episode)
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

2.  We add this summary to our episodic memory, including metadata about the interaction.
    ```python
    mem_add_text(
        episode,
        category="episodic",
        summarized=True,
        turns=4,
    )
    ```

3.  Here, we will search for the episode using a semantic query. The `created_at` timestamp provided by `mem0` allows for temporal filtering.
    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    if hits:
        print(f"{hits[0]['memory']}\n")
        print(f"Created at: {hits[0]['created_at']}")
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.

    Created at: 2025-09-12T02:30:01.358468-07:00
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory can be either developer-defined or learned from user interactions. An agent can learn new procedures dynamically by converting user-provided steps into a reusable tool. For example, a prompt could instruct the agent: *"When a user provides a numbered list of steps... convert these into a reusable procedure."*

```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```

The LLM would generate a new structured procedure and save it to its tool library. Retrieval is an intent-matching and function-calling process. The agent receives descriptions of all available procedures in its context and compares the user's request against them to find the best match.

1.  Here, we will demonstrate how to define a procedure and store it for later retrieval. We define a multi-step procedure for creating a monthly report and store it as a single text block.
    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))

    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    print(f"Learned procedure: {procedure_name}")
    ```
    It outputs:
    ```text
    Learned procedure: monthly_report
    ```

2.  The agent can then retrieve this procedure by matching the user's intent to the procedure's description.
    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```
    It outputs:
    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```

These examples show how different types of memories are created and retrieved. While we used a simple string-based storage method, these principles apply across more complex architectures.
```
**Grader reasoning:**
- `cc`: Memory Implementations with Code Examples:
**1:** Both sections walk through mem0 setup, then Semantic, Episodic, and Procedural memory with matching code, outputs, and prose. The Setup code omits `client`/`MODEL_ID`/the `genai` import, but both are properly defined (import included) at the top of the Episodic Memory code block, before their first use there — a reordering of where initialization happens, not a functional break, consistent with how a similar reordering was treated for a preset-0 article.
- `fl`: Memory Implementations with Code Examples:
**1:** The mem0 introduction, setup, and three memory-type walkthroughs appear in the same order with the same code-then-output-then-explanation pattern.
- `de`: Memory Implementations with Code Examples:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist extensively for this episode, so this is a content-based 0, not the code-level hard zero.
- `be`: Memory Implementations with Code Examples:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist extensively for this episode, so this is a content-based 0, not the code-level hard zero.
- `cp`: Memory Implementations with Code Examples:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default.
- `ga`: Memory Implementations with Code Examples:
**0:** At 831 prose-only words against a 500-word target (tolerance ceiling ~550 words), this section is substantially over length, which alone drives this score to 0.

## Section: S4::section-4-storing-memories-pros-and-cons-of-different-approaches  (weight=0.150, contribution=+0.0479 FOR light)
Stored section rewards: light=0.4283  standard=0.0961  (explore: light=0.3250  standard=0.0525)

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset1`

**Article text:**
```
## Storing Memories: Pros and Cons of Different Approaches

The way an agent’s memories are stored is an architectural decision that impacts performance, complexity, and scalability. There is no one-size-fits-all solution; the ideal approach depends entirely on the product's use case. Let’s explore the pros and cons of the three primary methods we experiment with as AI Engineers: storing memories as raw strings, as structured entities, and within a knowledge graph [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work), [[15]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece).

### Storing Memories as Raw Strings

This is the simplest method. Conversational turns or documents are stored as plain text and indexed for vector search.

**Pros:** It is simple and fast to set up, requiring minimal engineering. It preserves nuance, capturing emotional tone and linguistic cues without loss in translation. Keeping raw episodic records is crucial because summaries can drift or lose important details over time. This drift occurs from repeatedly compressing history to fit a context window, with each compression discarding details until the memory no longer matches what happened [[8]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

**Cons:** Retrieval is often imprecise. A query like “What is my brother’s job?” might retrieve every conversation mentioning “brother” and “job” without pinpointing the current fact [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). As interaction logs grow, they fill with irrelevant content, making retrieval slower and less reliable [[16]](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/). Updating is difficult; if a user corrects a fact (“My brother is now a doctor”), the new string just adds to the log, creating potential contradictions. It also lacks structure, making it hard to distinguish state changes over time (e.g., “Barry _was_ CEO” vs. “Claude _is_ CEO”). Even with large context windows, this approach suffers from attention dilution, where the model "loses" information in the middle of a long prompt [[8]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

### Storing Memories as Entities (JSON-like Structures)

Here, we use an LLM to transform messy interactions into structured memories, stored in formats like JSON within document databases or SQL databases.

**Pros:** It allows for precise, field-level filtering (e.g., `“user”: {”brother”: {”job”: “Software Engineer”}}`). The agent can retrieve specific facts without ambiguity. Updates are easier, as you simply overwrite the relevant field. This is ideal for semantic memory like user profiles or preferences.

**Cons:** It requires upfront schema design complexity. It can also be rigid; if the agent encounters information that does not fit the schema, that data might be lost unless the schema is updated [[15]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece). While an LLM could dynamically alter the schema, this introduces its own risks. The agent might create duplicate entities or inconsistent relationships, increasing the complexity of memory management and the potential for saving contradictory information. Furthermore, the extraction process can strip away the rich subtext of the original conversation. The factual memory `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day."

### Storing Memories in a Knowledge Graph

This is the most advanced approach. Memories are stored as a network of nodes (entities) and edges (relationships) using databases such as Neo4j.

**Pros:** It excels at representing complex relationships (e.g., `(User) -> [HAS_BROTHER] -> (Mark)`). This structure enables multi-hop reasoning that vector search cannot handle alone, allowing an agent to answer questions that require connecting multiple pieces of information [[17]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). It offers superior contextual and temporal awareness by modeling time as a property of a relationship (e.g., `[RECOMMENDED_ON_DATE]`). This is critical for tasks requiring an understanding of how facts evolve over time [[18]](https://neo4j.com/nodes-2025/agenda/building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs/). Retrieval is also auditable; you can trace the path of reasoning, which builds trust.

**Cons:** It has the highest complexity and cost. Converting unstructured text into graph triples is difficult and adds latency to ingestion pipelines. Graph traversals can be slower than vector lookups, potentially impacting real-time performance. For simple use cases, the complexity of implementing and maintaining a graph database is often overkill [[19]](https://arxiv.org/html/2504.19413).

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Raw Strings** | Simple to set up, preserves full nuance and emotional tone. | Imprecise retrieval, difficult to update, lacks structure for temporal reasoning. |
| **Entities (JSON)** | Precise, field-level filtering, easy to update, ideal for factual data. | Requires upfront schema design, can be rigid, loses original conversational nuance. |
| **Knowledge Graph** | Excellent for complex relationships, superior temporal awareness, auditable and explainable. | Highest complexity and cost, potentially slower queries, overkill for simple use cases. |
Table 1: A comparison of the three primary approaches for storing agent memories.

The choice should be guided by your product’s core needs. Start simple and evolve as complexity grows. Now that we know what to save and how to store memories, let's look at some code examples.
```
**Grader reasoning:**
- `cc`: Storing Memories: Pros and Cons of Different Approaches:
**0:** Both sections discuss the same three approaches for storing memories: as raw strings, as structured entities (JSON), and in a knowledge graph. They cover similar pros and cons for each method. The expected output's discussion of an LLM-supervised layer for memory operations is a key idea that is absent from the generated section.
- `fl`: Storing Memories: Pros and Cons of Different Approaches:
**1:** Both sections follow the same logical flow, introducing the topic and then discussing each storage approach in the order of raw strings, entities, and knowledge graphs, followed by a summary table. The transitions are logical and the progression of ideas is identical.
- `de`: Storing Memories: Pros and Cons of Different Approaches:
**1:** [instances=1; quality=strong] One depth addition qualifies in the Raw Strings “Cons” sub-section: “attention dilution” (the model loses information in the middle of even very large context windows). Note: attention dilution and lost-in-the-middle are treated as a single combined instance per instructions. This qualifies as a limitation/failure mode of the raw-strings storage approach. Traces to exploration-phase Source [46]. Instance qualifies.
- `be`: Storing Memories: Pros and Cons of Different Approaches:
**0:** [instances=0] No breadth additions present. The section focuses on the technical trade-offs of memory storage without expanding into adjacent concepts or historical context.
- `cp`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The depth addition (attention dilution failure mode) is well-integrated as an additional con within the Raw Strings sub-section. It reinforces the GT's message about retrieval limitations without displacing the GT's core comparison of the three storage approaches.
- `ga`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The generated section correctly follows the guideline's structure. It explores the pros and cons of the three primary storage methods: raw strings, entities (JSON), and knowledge graphs. It includes a table that serves the function of the requested Mermaid diagram by visualizing the three approaches. The content for each method's pros and cons directly reflects the points listed in the guideline. The transition to the next section is present. The word count is approximately 450 words, slightly over the 400-word target but within the acceptable +/-10% tolerance.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset1`

**Article text:**
```
## Storing Memories: Pros and Cons of Different Approaches

The way an agent’s memories are stored is an architectural decision that impacts performance, complexity, and scalability. There is no one-size-fits-all solution. Let’s explore the three primary methods we experiment with as AI Engineers.

### Storing Memories as Raw Strings

This is the simplest method. Conversational turns or documents are stored as plain text and indexed for vector search. This method's main advantage is its simplicity. It is fast to set up, requiring minimal engineering, and it preserves the full nuance of the original text without any loss in translation [[8]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

However, it has significant drawbacks. Retrieval is often imprecise. A query like “What is my brother’s job?” might retrieve every conversation mentioning “brother” and “job” without pinpointing the current fact. Updating is difficult; if a user corrects a fact (“My brother is now a doctor”), the new string just adds to the log, creating potential contradictions. It also lacks structure, making it hard to distinguish state changes over time (e.g., “Barry _was_ CEO” vs. “Claude _is_ CEO”) [[8]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

### Storing Memories as Entities (JSON-like Structures)

Here, we use an LLM to transform messy interactions into structured memories, stored in formats like JSON within document or SQL databases. A key benefit is that it allows for precise, field-level filtering (e.g., `“user”: {”brother”: {”job”: “Software Engineer”}}`). The agent can retrieve specific facts without ambiguity. Updates are also easier, as you simply overwrite the relevant field. This is ideal for semantic memory like user profiles or preferences [[8]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

The downsides include upfront schema design complexity. It can also be rigid; if the agent encounters information that does not fit the schema, that data might be lost unless the schema is updated [[9]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece). The extraction process can also strip away the rich subtext of the original conversation. The factual memory `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day."

### Storing Memories in a Knowledge Graph

This is the most advanced approach. Memories are stored as a network of nodes (entities) and edges (relationships) using databases such as Neo4j. It excels at representing complex relationships (e.g., `(User) -> [HAS_BROTHER] -> (Mark)`). It offers superior contextual and temporal awareness by modeling time as a property of a relationship (e.g., `[RECOMMENDED_ON_DATE]`). Retrieval is also auditable, as you can trace the path of reasoning, which builds trust [[8]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work), [[10]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).

This approach brings the highest complexity and cost. Converting unstructured text into graph triples is difficult. Graph traversals can be slower than vector lookups, potentially impacting real-time performance. For simple use cases, it is often overkill [[8]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work), [[11]](https://arxiv.org/html/2504.19413).

The challenge of updating memories, especially when new information contradicts old facts, is a significant engineering hurdle. Neuroscience offers a powerful analogy in **memory reconsolidation**. This theory suggests that when an existing memory is recalled, it becomes temporarily unstable and can be modified before being stored again. This allows new information to be incorporated, strengthening or altering the original memory. Applying this concept to AI agents could lead to more adaptive systems that don't just add new facts but intelligently update their existing knowledge based on new experiences [[12]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605913/).

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Raw Strings** | Simple setup, preserves nuance. | Imprecise retrieval, hard to update, lacks structure. |
| **Entities (JSON)** | Precise filtering, easy updates, good for facts. | Schema complexity, can be rigid, loses nuance. |
| **Knowledge Graph** | Models complex relationships, temporal awareness, auditable. | High complexity and cost, potentially slower queries, overkill for simple cases. |

Table 1: A comparison of the three primary approaches for storing agent memories.

The choice should be guided by your product’s needs. Start simple and evolve as complexity grows. Now that we know what to save and how to store it, let's look at some code examples.
```
**Grader reasoning:**
- `cc`: Storing Memories: Pros and Cons of Different Approaches:
**0:** Both sections cover the same three storage approaches with matching pros/cons and the same comparison table. As flagged for the earlier preset-0 articles, the expected section's opening point about recurring memory conflicts being resolved via LLM-proposed ADD/UPDATE/DELETE/NONE operations plus guardrails is absent as a general, cross-cutting framing — kept as a violation under the same reasoning as before (a mechanism with no other representation in the section, not a redundant illustration of an idea covered elsewhere). This is the same open question flagged previously and not yet resolved either way.
- `fl`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The three approaches and the table appear in the same relative order as the expected section. The generated section inserts a memory-reconsolidation aside between the knowledge-graph discussion and the table; it reads as a coherent cross-cutting aside about the updating problem raised earlier in the section rather than a disruptive break, so this does not create a bridgeless gap.
- `de`: Storing Memories: Pros and Cons of Different Approaches:
**1:** [instances=1; quality=strong] The memory-reconsolidation paragraph offers a theoretical lens for the section's own update/contradiction-handling problem (already raised as a con of raw strings earlier in the section): existing memories become temporarily unstable when recalled and can be modified before being re-stored, allowing intelligent updates rather than just appending contradictory facts. This traces to the exploration-phase PMC neuroscience source on memory reconsolidation ('existing memories to be reactivated, destabilized, and modified or strengthened during a reconsolidation window'). A named theoretical mechanism directly relevant to a challenge the section itself raises — strong.
- `be`: Storing Memories: Pros and Cons of Different Approaches:
**1:** [instances=1; quality=strong] The same reconsolidation paragraph is also a cross-domain analogy from neuroscience applied to AI agent memory updating, qualifying independently as breadth per the instruction that a single addition may satisfy both criteria simultaneously. Strong given the named theory and detailed mechanism explanation, not a passing mention.
- `cp`: Storing Memories: Pros and Cons of Different Approaches:
**1:** Both depth_enhancement and breadth_enhancement are 1 for this section (the reconsolidation paragraph), so this is evaluated rather than defaulted: the paragraph is a single ~75-word aside within a roughly 550-word section covering three storage methods and a comparison table; the three methods and table remain the section's clearly dominant content. No dilution.
- `ga`: Storing Memories: Pros and Cons of Different Approaches:
**0:** At 552 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0. As with core_content, the missing ADD/UPDATE/DELETE/NONE framing is the same open question flagged previously and not re-litigated here since length already determines the score.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset1`

**Article text:**
```
## Storing Memories: Pros and Cons of Different Approaches

The way an agent’s memories are stored is an architectural decision that impacts performance, complexity, and scalability. There is no one-size-fits-all solution. Let’s explore the three primary methods we experiment with as AI Engineers [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

### Storing Memories as Raw Strings

This is the simplest method. Conversational turns or documents are stored as plain text and indexed for vector search.

**Pros:** It is simple and fast to set up, requiring minimal engineering. It preserves nuance, capturing emotional tone and linguistic cues without loss in translation.

**Cons:** Retrieval is often imprecise. A query like “What is my brother’s job?” might retrieve every conversation mentioning “brother” and “job” without pinpointing the current fact [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). This approach also suffers from **summarization drift**, where repeated compression of history to fit a context window causes details to be lost over time. Even with large context windows, **attention dilution** can occur, where the model ignores information buried in the middle of a long prompt [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/). Updating is difficult; if a user corrects a fact (“My brother is now a doctor”), the new string just adds to the log, creating potential contradictions. This challenge mirrors findings in neuroscience, where memories must become temporarily unstable or "labile" to be updated—a process known as reconsolidation. Without a structured way to reactivate and modify specific memories, the agent’s knowledge base can become a collection of conflicting statements [[12]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605913/). It also lacks structure, making it hard to distinguish state changes over time (e.g., “Barry _was_ CEO” vs. “Claude _is_ CEO”) [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

### Storing Memories as Entities (JSON-like Structures)

Here, we use an LLM to transform messy interactions into structured memories, stored in formats like JSON within document or SQL databases.

**Pros:** It allows for precise, field-level filtering (e.g., `“user”: {”brother”: {”job”: “Software Engineer”}}`). The agent can retrieve specific facts without ambiguity. Updates are easier; you simply overwrite the relevant field. This is ideal for semantic memory like user profiles or preferences.

**Cons:** It requires upfront schema design complexity. It can also be rigid. If the agent encounters information that does not fit the schema, that data might be lost unless the schema is updated [[13]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece). Allowing an LLM to dynamically add new entities or fields can increase flexibility, but it also introduces risks. The schema can become inconsistent, making updates more complex and increasing the chance of saving duplicated or conflicting information. Furthermore, the extraction process can strip away the rich subtext of the original conversation. The factual memory `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day."

### Storing Memories in a Knowledge Graph

This is the most advanced approach. Memories are stored as a network of nodes (entities) and edges (relationships) using graph databases.

**Pros:** It excels at representing complex relationships (e.g., `(User) -> [HAS_BROTHER] -> (Mark)`). This structure enables multi-hop reasoning, allowing the agent to answer questions that require connecting multiple pieces of information. It offers superior contextual and temporal awareness by modeling time as a property of a relationship (e.g., `[RECOMMENDED_ON_DATE]`) [[14]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). Retrieval is also auditable. You can trace the path of reasoning, which builds trust.

**Cons:** It has the highest complexity and cost. Converting unstructured text into graph triples is difficult. Graph traversals can be slower than vector lookups, potentially impacting real-time performance. For simple use cases, it is often overkill [[15]](https://arxiv.org/html/2504.19413).

Beyond these storage formats, more advanced architectural patterns are emerging. **Reflective self-improvement** allows an agent to analyze its own interactions, write post-mortems on its failures, and store those conclusions to improve future performance. Another approach is **hierarchical virtual context**, where memory is tiered like a computer’s OS—with RAM for active context, a disk for recent recall, and cold storage for archives—and the agent learns to manage its own paging between them [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Raw Strings** | Simple setup, preserves nuance. | Imprecise retrieval, hard to update, lacks structure, prone to drift. |
| **Entities (JSON)** | Precise filtering, easy updates, good for facts. | Schema design complexity, can be rigid, loses nuance. |
| **Knowledge Graph** | Models complex relationships, time-aware, auditable. | High complexity and cost, potentially slower queries. |
Table 1: A comparison of the three primary approaches for storing agent memories.

<aside>
💡 The choice should be guided by your product’s needs. Start simple and evolve as complexity grows.
</aside>

Now that we know what to save and how to store it, let's look at some code examples.
```
**Grader reasoning:**
- `cc`: Storing Memories: Pros and Cons of Different Approaches:
**0:** Both sections cover the same three storage approaches with matching pros/cons and the same comparison table. As flagged for the earlier articles, the expected section's opening point about resolving memory conflicts via LLM-proposed ADD/UPDATE/DELETE/NONE operations plus guardrails is absent as a general framing device — kept as a violation under the same still-unresolved reasoning as before.
- `fl`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The three approaches and the table appear in the same relative order. The Raw-Strings cons paragraph interleaves several exploration-sourced additions (summarization drift, attention dilution, memory reconsolidation) with the expected section's own three cons (imprecise retrieval, difficulty updating, lack of temporal structure); stepping over the additions, the three original cons still appear in the expected relative order, so this does not break flow. A further paragraph on reflective self-improvement and hierarchical virtual context is appended after the three methods and before the table, which is a dense addition but does not reorder or omit any expected idea.
- `de`: Storing Memories: Pros and Cons of Different Approaches:
**1:** [instances=5; quality=strong,strong,strong,strong,strong] Five distinct additions, all traced to the exploration-phase Practical Guide: (1) 'summarization drift' (Failure Modes: 'each compression throws away details... memory that doesn't really match what happened'); (2) 'attention dilution' (Failure Modes, same named mechanism as the Introduction's instance, a separate addition here in a different section); (3) memory reconsolidation (also breadth, see below); (4) 'reflective self-improvement' (Five Mechanism Families: 'agents write verbal post-mortems and store conclusions', naming Reflexion/ExpeL); (5) 'hierarchical virtual context' (Five Mechanism Families: MemGPT's RAM/disk/cold-storage OS-paging analogy). All five are named, specific mechanisms with real explanation rather than passing mentions — strong. Flagged as unusually dense: five qualifying depth instances in one section is more than any other section graded so far.
- `be`: Storing Memories: Pros and Cons of Different Approaches:
**1:** [instances=1; quality=strong] The memory-reconsolidation paragraph is also a cross-domain analogy from neuroscience, qualifying independently as breadth per the same reasoning established for the earlier preset-1 article. Strong given the named theory and detailed mechanism. (Hierarchical virtual context, while OS-inspired, is treated as depth-only here — an alternative implementation perspective on the core topic rather than a genuine import from an unrelated field the way neuroscience is; flagged as a judgment call, since a case could be made either way.)
- `cp`: Storing Memories: Pros and Cons of Different Approaches:
**1:** Both depth_enhancement and breadth_enhancement are 1 here, and with five depth instances this is the densest section graded so far, so this deserves real scrutiny rather than a quick default: the three storage methods, their full pros/cons, and the comparison table are all still completely intact and take up the clear majority of the section; the additions are woven in as extra failure modes and a closing 'beyond these formats' aside rather than replacing any original content. Scored 1, but flagged given the density — this is closer to the point where dilution would become a real question than any other section in this set.
- `ga`: Storing Memories: Pros and Cons of Different Approaches:
**0:** At 663 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length — the most over-length section in this article, consistent with how much enhancement content is packed into it — which alone drives this score to 0.

### Arm: standard (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset3`

**Article text:**
```
## Storing Memories: Pros and Cons of Different Approaches

How an agent's memories are stored is a critical architectural decision that directly impacts its performance, complexity, and scalability. While the goal is always to provide the right context at the right time, the method of storage involves significant trade-offs. There is no one-size-fits-all solution; the ideal approach depends entirely on your product's use case [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). Let's explore three primary methods: storing memories as raw strings, as structured entities, and within a knowledge graph.

### Storing Memories as Raw Strings

The simplest method is to store conversational turns or documents as plain text and index them for vector search [[14]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). The primary advantage of this approach is its simplicity and speed of setup. It requires minimal engineering overhead, as it mainly involves logging text and creating embeddings. This method also preserves the full nuance of the original interaction, including emotional tone and subtle linguistic cues, ensuring nothing is lost in translation.

However, this approach has significant drawbacks. Retrieval can be imprecise, as semantic similarity alone is often not enough. A query might return text that is semantically related but contextually wrong. For example, asking, "What is my brother's job?" could retrieve every past conversation mentioning "brother" and "job" without pinpointing the correct fact [[14]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). Updating information is also difficult; a correction from a user simply adds another string to the log, creating potential contradictions. This lack of structure makes it hard to handle temporal reasoning or state changes, as it cannot easily distinguish between "Barry *was* the CEO" and "Claude *is* the CEO" [[14]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). Furthermore, this method is prone to issues like summarization drift, where repeated compression loses details, and attention dilution, where models ignore information buried in long contexts [[4]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

### Storing Memories as Entities (JSON-like Structures)

A more structured approach involves using an LLM to transform unstructured interactions into structured memories, often stored in a format like JSON. This method organizes information into key-value pairs, which allows for precise, field-level filtering and makes it easy to retrieve specific facts without ambiguity. If a user's preference changes, only the relevant field in the JSON object needs to be updated, ensuring the memory remains current. This makes it well-suited for semantic memory, where user profiles and preferences are stored.

The main disadvantage is the increased upfront complexity. This approach requires designing a schema or data model, which adds an initial layer of engineering effort. A predefined schema can also be rigid; if the agent encounters information that does not fit the existing structure, that data may be lost [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). While an LLM can dynamically add new fields, this can complicate memory updates and increase the risk of saving duplicate information. Additionally, the extraction process can strip away the rich subtext of the original conversation; the factual memory `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day."

### Storing Memories in a Graph Database

The most advanced approach is to store memories as a network of nodes (entities) and edges (relationships), forming a knowledge graph [[15]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). The core strength of a graph is its ability to explicitly define how different pieces of information are connected, enabling sophisticated queries that trace these connections. For instance, it can map `(User) -> [HAS_BROTHER] -> (Mark) -> [WORKS_AS] -> (Software Engineer)`. Knowledge graphs also provide superior contextual and temporal awareness by modeling time as an explicit property of a relationship, offering more accurate retrieval than vector search alone. Furthermore, retrieval is transparent and auditable, as you can trace the exact path that led to an answer.

However, this method comes with the highest complexity and cost. It requires a significant upfront investment in schema design, data modeling, and ongoing maintenance. The process of converting unstructured interactions into structured graph triples is a complex task. While powerful, graph traversals for complex queries can be slower than a simple vector lookup, which might impact real-time performance if not carefully optimized. For many applications, the complexity of implementing and maintaining a graph database is overkill, and a simpler approach may be sufficient.

| Approach | Pros | Cons |
| --- | --- | --- |
| **Raw Strings** | Simple to set up, preserves full nuance. | Imprecise retrieval, hard to update, lacks structure, prone to drift. |
| **Entities (JSON)** | Precise retrieval, easy to update, good for facts. | Schema design needed, can be rigid, loses nuance. |
| **Knowledge Graph** | Models complex relationships, superior temporal awareness, auditable. | High complexity and cost, potentially slower queries, overkill for simple use cases. |

Table 1: A comparison of three primary approaches to storing agent memories.

The choice of memory storage should be guided by your product's core needs. A good practice is to start with the simplest architecture that delivers value and evolve it as your agent's requirements grow more complex.

Now that we know what to save and how to store it, let's look at some code examples using available memory tools.
```
**Grader reasoning:**
- `cc`: Storing Memories: Pros and Cons of Different Approaches:
**0:** The GT section opens with a substantive 2-paragraph block on the LLM-supervised ADD/UPDATE/DELETE/NONE memory-operation mechanism — a core engineering pattern for managing real-world memory updates and conflict resolution. The generated section omits this concept entirely, covering only the three storage methods without the introductory framing. Since this block constitutes a key topic/key point of the GT section, its complete absence is a CoreContent failure.
- `fl`: Storing Memories: Pros and Cons of Different Approaches:
**1:** Both sections follow the same logical flow for the three storage methods that are present (raw strings → entities → knowledge graph → table). The omission of the LLM-supervised ADD/UPDATE/DELETE introductory block is already scored under CoreContent and does not create a narrative discontinuity among the ideas that remain; the relative order of the shared content is preserved.
- `de`: Storing Memories: Pros and Cons of Different Approaches:
**1:** [instances=1; quality=strong] A depth addition is present: the generated section discusses specific failure modes for the raw string approach, such as "summarization drift" and "attention dilution," providing more technical detail on the limitations. Note: these are treated as one combined instance. This qualifies as 'limitations, criticisms, or failure modes of the core topic'. Traces to exploration-phase source https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/ in research.md. Instance qualifies.
- `be`: Storing Memories: Pros and Cons of Different Approaches:
**0:** [instances=0] No breadth additions present. The section focuses on the core topic of memory storage methods.
- `cp`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The depth addition about specific failure modes like "summarization drift" and "attention dilution" directly supports the core argument about the cons of the raw string approach. It enriches the ground truth's narrative without shifting its focus.
- `ga`: Storing Memories: Pros and Cons of Different Approaches:
**0:** The generated section fails to meet a key requirement. The guideline explicitly asks for a Mermaid diagram to visualize the three storage approaches. This diagram is completely missing from the generated output. While the section does cover the pros and cons of the three storage methods (raw strings, entities/JSON, and knowledge graphs) and includes the concluding tip, the absence of the mandatory diagram constitutes a significant violation of the guideline. The prose-only word count is approximately 450 words, which is within the 400-word target.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset3`

**Article text:**
```
## Storing Memories: Pros and Cons of Different Approaches

How an agent's memories are stored is an important architectural decision that directly impacts its performance, complexity, and scalability. While the goal is always to provide the right context at the right time, the method of storage involves trade-offs. There is no one-size-fits-all solution; the ideal approach depends entirely on the product's use case. Let's explore the pros and cons of three primary methods: storing memories as raw strings, as structured entities, and within a knowledge graph.

### Storing Memories as Raw Strings

This is the simplest method, where conversational turns or documents are stored as plain text and typically indexed for vector search [[6]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

-   **Pros:** This method is the easiest to set up, requiring minimal engineering overhead to get started. By storing the raw text, the full context, including emotional tone and subtle linguistic cues, is preserved. Nothing is lost in translation to a structured format, allowing you to return to the original record of what happened [[7]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/755491854613).
-   **Cons:** Retrieval can be imprecise. Relying solely on semantic similarity is often not enough. A query like "What is my brother's job?" might retrieve every past conversation where "brother" and "job" were mentioned, without pinpointing the single correct fact [[6]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). As interaction logs grow, they fill with irrelevant content, making retrieval slower and less reliable [[8]](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/). Updating memory is also difficult. If a user corrects information ("My brother is no longer a lawyer, he's a doctor now"), the new information is just another string in a growing log, creating potential contradictions. This approach also struggles with temporal reasoning and state changes, as it cannot easily distinguish between "Barry *was* the CEO" and "Claude *is* the CEO" because the relationship is not explicitly defined [[6]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

### Storing Memories as Entities (JSON-like Structures)

In this approach, we use an LLM to transform unstructured, messy interactions into structured memories, storing them in a format like JSON [[9]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

-   **Pros:** Information is organized into key-value pairs (`"user": {"brother": {"job": "Software Engineer"}}`), which allows for precise, field-level filtering. This structure makes it easy to retrieve specific facts without ambiguity and to update information when it changes. This method is perfectly suited for semantic memory, where user profiles and preferences are stored.
-   **Cons:** This approach requires designing a schema, which adds an initial layer of engineering complexity. A predefined schema can also be inflexible; if the agent encounters information that does not fit the existing structure, that data may be lost. While an LLM can dynamically add new entities or fields, this increases the complexity of updating memories and the risk of saving duplicate information. The extraction process also strips away the rich subtext of the original conversation. The factual memory `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day" [[9]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). Furthermore, exposing these structured memories to users can create cognitive overhead, as they may feel pressured to "garden" their own data, which detracts from a seamless user experience [[9]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

### Storing Memories in a Graph Database

This is the most advanced approach, where memories are stored as a network of nodes (entities) and edges (relationships), forming a knowledge graph [[10]](https://www.octoco.ai/blog/knowledge-graphs-as-memory), [[18]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece).

-   **Pros:** A graph's core strength is representing complex relationships explicitly, such as `(User) -> [HAS_BROTHER] -> (Mark) -> [WORKS_AS] -> (Software Engineer)`. This enables sophisticated, multi-hop queries that trace these connections. Knowledge graphs can model context and time as explicit properties of a relationship (e.g., `User -[RECOMMENDED_ON_DATE: "2025-10-25"]-> Restaurant`), providing more accurate and grounded retrieval than vector search alone. This temporal awareness allows the graph to evolve without expensive re-computation [[10]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). Retrieval is also transparent and auditable, as you can trace the exact path that led to an answer, making it easier to debug the agent's reasoning [[10]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).
-   **Cons:** This method requires a higher upfront investment in schema design, data modeling, and ongoing maintenance. The process of converting unstructured interactions into structured graph triples is more complex than just storing strings. Complex graph traversals can also be slower than a simple vector lookup, which might impact real-time performance if not carefully optimized. For many applications, the complexity of implementing and maintaining a graph database is overkill [[10]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Raw Strings** | Simple and fast to set up; preserves full conversational nuance. | Imprecise retrieval; difficult to update; lacks structure for temporal reasoning. |
| **Entities (JSON)** | Structured and precise; easy to update; ideal for factual data. | Higher upfront complexity; potential for schema rigidity; loss of original nuance. |
| **Knowledge Graph** | Represents complex relationships; superior temporal awareness; auditable and explainable. | Highest complexity and cost; potentially slower queries; overkill for simple use cases. |
Table 1: A comparison of three primary approaches for storing agent memories.

The choice of memory storage should be guided by your product's core needs. It is often best to start with the simplest architecture that delivers value and evolve it as the demands on your agent grow more complex. Now that we know what to save and how to store it, let's look at some code examples using an open-source memory tool.
```
**Grader reasoning:**
- `cc`: Storing Memories: Pros and Cons of Different Approaches:
**0:** Both sections cover the same three storage approaches with matching pros/cons and the same comparison table. As flagged for the earlier articles in this set, the expected section's opening point about resolving memory conflicts via LLM-proposed ADD/UPDATE/DELETE/NONE operations plus guardrails is absent — kept as a violation under the same still-unresolved reasoning as before.
- `fl`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The three approaches and the table appear in the same relative order as the expected section.
- `de`: Storing Memories: Pros and Cons of Different Approaches:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist for this episode (extensively, for this article), so this is a content-based 0, not the code-level hard zero.
- `be`: Storing Memories: Pros and Cons of Different Approaches:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist for this episode (extensively, for this article), so this is a content-based 0, not the code-level hard zero.
- `cp`: Storing Memories: Pros and Cons of Different Approaches:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default.
- `ga`: Storing Memories: Pros and Cons of Different Approaches:
**0:** At 756 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset3`

**Article text:**
```
## Storing Memories: Pros and Cons of Different Approaches

How an agent's memories are stored is an important architectural decision that directly impacts its performance, complexity, and scalability. While the goal is always to provide the right context at the right time, the method of storage involves trade-offs. There is no one-size-fits-all solution; the ideal approach depends entirely on the product's use case. Let's explore the pros and cons of the three primary methods: storing memories as raw strings, as structured entities, and within a knowledge graph.

### Storing Memories as Raw Strings

This is the simplest method, where conversational turns or documents are stored as plain text and indexed for vector search [[3]](https://stevekinney.com/writing/agent-memory-systems), [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

**Pros:** This approach is **simple and fast to set up**, requiring minimal engineering overhead. It also **preserves nuance** by storing the raw text, ensuring that emotional tone and subtle linguistic cues are not lost in translation to a structured format [[5]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

**Cons:** Retrieval can be **imprecise**. A query might retrieve text that is semantically related but contextually wrong. For example, asking "What is my brother’s job?" could retrieve every past conversation mentioning "brother" and "job" without pinpointing the correct fact [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). It is also **difficult to update**; a correction just adds another string to the log, creating potential contradictions. Finally, the **lack of structure** makes it hard to handle temporal reasoning or state changes, like distinguishing between "Barry *was* the CEO" and "Claude *is* the CEO" [[3]](https://stevekinney.com/writing/agent-memory-systems), [[4]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

### Storing Memories as Entities (JSON)

In this approach, we move from unstructured interactions to structured memories, often using an LLM to perform the extraction and storing them in a format like JSON.

This method offers several advantages. First, information is **structured and precise**, organized into key-value pairs (e.g., `"user": {"brother": {"job": "Software Engineer"}}`) that allow for exact filtering. By filtering for "brother," the agent can retrieve everything related to him. Second, memories are **easier to update**; if a user's preference changes, only the relevant field needs to be modified. This makes the approach **ideal for factual data**, especially for semantic memory where user profiles and preferences are stored.

However, this approach has its downsides. It introduces **increased upfront complexity** due to the need for schema design. A predefined schema can also be **inflexible**; if the agent encounters information that does not fit the structure, that data may be lost. While an LLM can dynamically alter the schema, this increases the risk of saving duplicate information. Finally, the extraction process can lead to a **loss of original nuance**, as the rich subtext of the conversation is stripped away.

### Storing Memories in a Knowledge Graph

This is the most advanced approach, where memories are stored as a network of nodes (entities) and edges (relationships).

Its core strength is the ability to **represent complex relationships** explicitly, such as `(User) -> [HAS_BROTHER] -> (Mark) -> [WORKS_AS] -> (Software Engineer)`. This structure enables sophisticated queries that trace these connections [[6]](https://www.octoco.ai/blog/knowledge-graphs-as-memory), [[7]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece).

Knowledge graphs also provide **superior temporal awareness**. They can model time as an explicit property of a relationship (e.g., `User -[RECOMMENDED_ON_DATE: "2025-10-25"]-> Restaurant`), enabling more accurate retrieval than vector search alone [[8]](https://neo4j.com/nodes-2025/agenda/building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs/), [[6]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). They can also resolve conflicts by using timestamps to invalidate outdated facts rather than overwriting them, preserving a faithful history of state changes [[13]](https://developers.openai.com/cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents). Finally, this approach offers **auditability and explainability**, as you can trace the exact path of nodes and edges that led to an answer, making it easier to debug the agent's reasoning [[6]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).

The main drawbacks are the **highest complexity and cost**, requiring significant investment in schema design and maintenance. **Queries can be slower** than simple vector lookups, and the overall **overhead may be excessive for simple use cases** [[6]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Raw Strings** | Simple setup, preserves nuance | Imprecise retrieval, hard to update, lacks structure |
| **Entities (JSON)** | Structured, precise, easy to update | Upfront complexity, schema rigidity, loss of nuance |
| **Knowledge Graph** | Represents complex relationships, temporal awareness, explainable | Highest complexity, slower queries, overkill for simple cases |

Table 1: A comparison of memory storage approaches.

The choice of memory storage should be guided by your product's core needs. It is often best to start with the simplest architecture that delivers value and evolve it as your agent's requirements grow more complex.
```
**Grader reasoning:**
- `cc`: Storing Memories: Pros and Cons of Different Approaches:
**0:** Both sections cover the same three storage approaches with matching pros/cons and the same comparison table. As flagged for the earlier articles, the ADD/UPDATE/DELETE/NONE-plus-guardrails framing is absent — kept as a violation under the same still-unresolved reasoning as before.
- `fl`: Storing Memories: Pros and Cons of Different Approaches:
**1:** The three approaches and the table appear in the same relative order as the expected section.
- `de`: Storing Memories: Pros and Cons of Different Approaches:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist extensively for this episode, so this is a content-based 0, not the code-level hard zero.
- `be`: Storing Memories: Pros and Cons of Different Approaches:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist extensively for this episode, so this is a content-based 0, not the code-level hard zero.
- `cp`: Storing Memories: Pros and Cons of Different Approaches:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default.
- `ga`: Storing Memories: Pros and Cons of Different Approaches:
**0:** At 641 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0.

## Section: S3::section-3-long-term-memory-semantic-episodic-and-procedural  (weight=0.150, contribution=+0.0350 FOR light)
Stored section rewards: light=0.5208  standard=0.2769  (explore: light=0.2175  standard=0.0000)

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset1`

**Article text:**
```
## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a single bucket of text. It consists of three distinct types, each serving a different role in making an agent “intelligent” [[9]](https://arxiv.org/html/2309.02427), [[10]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems).

### Semantic Memory (Facts & Knowledge)

**Semantic memory** is the agent’s encyclopedia. It stores individual pieces of knowledge or “facts.” These can be independent strings, such as _“The user is a vegetarian,”_ or structured attributes attached to an entity, like `{"food_restrictions": "vegetarian"}`. This is where the agent stores concepts and relationships regarding specific domains, people, or places. The structure of this memory is highly dependent on the agent's use case. It could be a simple collection of text or a complex graph database.

The primary role of semantic memory is to provide a reliable source of truth. For an enterprise agent, this might involve storing internal company documents, technical manuals, or an entire product catalog, allowing it to answer questions on proprietary topics. For a personal assistant, semantic memory builds a persistent user profile. It recalls specific preferences like `{"music": "User likes rock music"}` or constraints like `{"dog": "User has a dog named George"}`. This allows the agent to retrieve relevant facts without searching through a noisy conversation history. For domain-expert agents in fields like law or medicine, semantic memory is the most critical component, providing a deep, structured knowledge base for reliable reasoning. In these specialized domains, semantic memory often integrates with RAG systems to pull in knowledge that was not part of the base model's training, allowing the agent to maintain deep expertise [[11]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

### Episodic Memory (Experiences & History)

**Episodic memory** is the agent’s personal diary. It records past interactions, but unlike timeless facts, these memories have a timestamp. It captures _“what happened and when.”_ Think of it as a detailed journal of specific interactions: user X did action Y at timestamp Z, resulting in outcome W. This preserves the rich context of individual events, maintaining the temporal sequence and environmental conditions that surrounded each decision [[12]](https://ctoi.substack.com/p/memory-systems-in-ai-agents-episodic).

This memory type is essential for maintaining conversational context and understanding relationship dynamics. A semantic fact might be _“User is frustrated with his brother.”_ An episodic memory would be: _“On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I provided an empathetic response. [created_at=2025-08-25].”_

This “episode” provides nuanced context. If the topic comes up again, the agent can say, “I know the topic of your brother’s birthday can be sensitive,” rather than just stating a fact. It also allows the agent to answer questions like _“What happened last week?”_ [[3]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). Depending on the use case, episodic memories can group important events that happened during a whole day, a single conversation, or over a week. For personal AI assistants focused on user personalization, episodic memory is paramount, as it allows the agent to provide increasingly tailored experiences based on past interactions. It enables a form of case-based reasoning, where the agent consults past "case studies" from its memory to make more refined decisions over time [[11]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

### Procedural Memory (Skills & How-To)

**Procedural memory** is the agent’s muscle memory. It consists of skills, learned workflows, and “how-to” knowledge. It dictates the agent’s ability to perform multi-step tasks. This is the memory of how to perform a common task without actively thinking about it, like riding a bike or tying your shoes [[13]](https://www.geeksforgeeks.org/artificial-intelligence/ai-agent-memory/).

This memory is often baked into the agent’s system prompt as reusable tools or defined sequences. For example, an agent might store a `MonthlyReportIntent` procedure. When a user asks for a report, the agent retrieves this procedure: 1) Query sales DB, 2) Summarize findings, 3) Email user. This makes behavior reliable and predictable. It encodes successful workflows so the agent does not have to reason from scratch every time [[14]](https://arxiv.org/html/2508.06433v2). For workflow automation agents that handle repetitive processes, procedural memory is the key to executing tasks efficiently and at scale. It reduces repetitive deliberation, allowing the agent's reasoning to focus on novel situations rather than re-solving common problems [[11]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

Now that we have an idea of what to save and the benefits of specific types of memories, how should they be stored? There are three main approaches we can experiment with.
```
**Grader reasoning:**
- `cc`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections define and explain the same three types of long-term memory: Semantic, Episodic, and Procedural. They provide similar examples and discuss the primary role of each memory type in agent design.
- `fl`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections follow the same logical progression, introducing the three types of memory and then detailing each one in the order of Semantic, Episodic, and Procedural. The transitions between the subsections are smooth.
- `de`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No depth additions present. The domain-specific elaborations (law/medicine examples for semantic memory, “case-based reasoning” phrasing for episodic memory, workflow automation emphasis for procedural memory, and RAG integration mentions) were carefully reviewed but disqualified. They cannot be traced to any exploration-phase sources in research.md for this episode and remain within the ground-truth core topic of defining the three memory types and explaining their primary roles.
- `be`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No breadth additions present. The section stays focused on the three types of long-term memory without expanding into adjacent fields or historical context traceable to exploration-phase sources.
- `cp`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default.
- `ga`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** The generated section correctly breaks down the three types of long-term memory as required. For Semantic Memory, it explains what it is and how it's used, providing examples. For Episodic Memory, it defines it as a "personal diary" with timestamps and explains its use with an example. For Procedural Memory, it defines it as "muscle memory" and explains its use. The content for each memory type aligns perfectly with the detailed descriptions in the guideline. The transition to the next section is also included. The word count is approximately 400 words, meeting the guideline's target.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset1`

**Article text:**
```
## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a single bucket of text. It consists of three distinct types, each serving a different role in making an agent “intelligent” [[4]](https://arxiv.org/html/2309.02427), [[5]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems).

### Semantic Memory (Facts & Knowledge)

Semantic memory is the agent’s encyclopedia. It stores individual pieces of knowledge or “facts.” These can be independent strings, such as _“The user is a vegetarian,”_ or structured attributes attached to an entity, like `{"food_restrictions": "vegetarian"}`. This is where the agent stores concepts and relationships regarding specific domains, people, or places. The structure you choose depends heavily on the agent's use case; it could be a simple collection of text or a complex graph database. We will explore the pros and cons of these approaches later.

The primary role of semantic memory is to provide a reliable source of truth. For an enterprise agent, this might involve storing internal company documents or technical manuals, allowing it to answer questions on proprietary topics. For a personal assistant, semantic memory builds a persistent user profile. It recalls specific preferences like `{"music": "User likes rock music"}` or constraints like `{"dog": "User has a dog named George"}`. This allows the agent to retrieve relevant facts without searching through a noisy conversation history. In practice, this can be implemented as a curated file, such as a `MEMORY.md` in an agent's workspace, where the agent or a developer periodically decides which facts are worth preserving as lasting truths [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

### Episodic Memory (Experiences & History)

Episodic memory is the agent’s personal diary. It records past interactions, but unlike timeless facts, these memories have a timestamp. It captures _“what happened and when.”_ This memory type is essential for maintaining conversational context and understanding relationship dynamics [[6]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

A semantic fact might be _“User is frustrated with his brother.”_ An episodic memory would be: _“On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I provided an empathetic response. [created_at=2025-08-25].”_ This “episode” provides nuanced context. If the topic comes up again, the agent can say, “I know the topic of your brother’s birthday can be sensitive,” rather than just stating a fact. It also allows the agent to answer questions like _“What happened last week?”_ Depending on the use case, these memories can group events over a day, a week, or a single conversation. A practical implementation could be daily logs where each agent summarizes its activities, findings, and escalations. This creates a searchable timeline that allows agents to review past work, identify patterns, and avoid repeating failures [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

### Procedural Memory (Skills & How-To)

Procedural memory is the agent’s muscle memory. It consists of skills, learned workflows, and “how-to” knowledge. It dictates the agent’s ability to perform multi-step tasks.

This memory is often baked into the agent’s system prompt as reusable tools or defined sequences. For example, an agent might store a `MonthlyReportIntent` procedure. When a user asks for a report, the agent retrieves this procedure: 1) Query sales DB, 2) Summarize findings, 3) Email user. This makes behavior reliable and predictable. It encodes successful workflows so the agent does not have to reason from scratch every time [[7]](https://arxiv.org/html/2508.06433v2). This can be managed through configuration files that define an agent's persona, behavioral constraints, and escalation rules. These files act as a form of long-term learned behavior that shapes every action, and they should be updated based on feedback to allow the agent to improve over time [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

Now that we have an idea of what to save and the benefits of specific types of memories, we must decide how to store it.
```
**Grader reasoning:**
- `cc`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections cover Semantic, Episodic, and Procedural memory with matching definitions and the same illustrative examples (vegetarian/dog-named-George/brother-Mark facts; the Tuesday birthday-episode; the MonthlyReportIntent-style procedure). The generated section adds a concrete implementation pattern under each subheading (a MEMORY.md-style curated file, daily searchable logs, and persona/escalation configuration files) — verified below as genuine depth additions — without omitting any expected idea.
- `fl`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** The three memory types appear in the identical order with matching internal progression; the three added implementation-pattern sentences sit at the end of their respective subsections as trailing elaborations, not disrupting the sequence or transitions of the expected examples.
- `de`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** [instances=3; quality=strong,strong,strong] Three distinct implementation-pattern additions, one under each subheading: (1) Semantic — a curated MEMORY.md-style file where facts are periodically decided as 'lasting truths'; (2) Episodic — daily searchable logs that let agents 'review past work, identify patterns, and avoid repeating failures'; (3) Procedural — persona/behavioral-constraint/escalation-rule configuration files framed as 'long-term learned behavior' updated via feedback. All three trace directly to the exploration-phase 'Practical Guide' source's 'Four Temporal Scopes' section, which describes the MEMORY.md file, the daily standup logs with the identical 'spot patterns, avoid repeating failures' phrasing, and the AGENTS.md/SOUL.md persona-and-escalation files updated via feedback — each a named, concrete pattern rather than a passing mention, so all three are strong.
- `be`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] All three additions deepen understanding of how each long-term memory type is implemented in practice; none connects outward to an adjacent field, so none qualifies as breadth for this section.
- `cp`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** depth_enhancement=1 for this section (three implementation-pattern additions), so this is evaluated rather than defaulted: each addition is a single trailing sentence within its own subsection, proportionate relative to the subsection's core definition and example, which remain dominant. No dilution.
- `ga`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** At 588 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0. Content otherwise matches the guideline's three memory types and examples closely, plus the three added implementation patterns.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset1`

**Article text:**
```
## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a single bucket of text. It consists of three distinct types, each serving a different role in making an agent “intelligent” [[1]](https://arxiv.org/html/2309.02427), [[8]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems).

### Semantic Memory (Facts & Knowledge)

Semantic memory is the agent’s encyclopedia [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). It stores individual pieces of knowledge or “facts.” These can be independent strings, such as _“The user is a vegetarian,”_ or structured attributes attached to an entity, like `{"food_restrictions": "vegetarian"}`. This is where the agent stores concepts and relationships regarding specific domains, people, or places. The primary role of semantic memory is to provide a reliable source of truth. For an enterprise agent, this might involve storing internal company documents, technical manuals, or an entire product catalog, allowing it to answer questions on proprietary topics. For a personal assistant, semantic memory builds a persistent user profile. It recalls specific preferences like `{"music": "User likes rock music"}` or constraints like `{"dog": "User has a dog named George"}`. This allows the agent to retrieve relevant facts without searching through a noisy conversation history.

The distinction between memory types is important for choosing the right architecture. For domain expert agents in fields like law or finance, semantic memory is the most critical component, often integrated with RAG systems to pull in specialized knowledge. However, this memory requires careful curation. Without it, semantic memory can become a "junk drawer" of outdated or irrelevant information, degrading the agent's performance [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

### Episodic Memory (Experiences & History)

Episodic memory is the agent’s personal diary. It records past interactions, but unlike timeless facts, these memories have a timestamp. It captures _“what happened and when.”_ [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/) This memory type is essential for maintaining conversational context and understanding relationship dynamics. A semantic fact might be _“User is frustrated with his brother.”_ An episodic memory would be: _“On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I provided an empathetic response. [created_at=2025-08-25].”_ [[10]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112)

This “episode” provides nuanced context. If the topic comes up again, the agent can say, “I know the topic of your brother’s birthday can be sensitive,” rather than just stating a fact. It also allows the agent to answer questions like _“What happened last week?”_ This enables a form of case-based reasoning, where an agent learns from its own history. For example, an AI financial advisor with episodic memory can recall that a previous stock recommendation underperformed, and use that experience to inform future advice. For personal AI assistants, episodic memory is often the most important type, as it drives personalization [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). Depending on the use case, these memories can group important events that happened over a day, a single conversation, or a week. There is no one-size-fits-all solution; the product dictates the required time scale.

### Procedural Memory (Skills & How-To)

Procedural memory is the agent’s muscle memory. It consists of skills, learned workflows, and “how-to” knowledge. It dictates the agent’s ability to perform multi-step tasks [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). This memory is often baked into the agent’s system prompt as reusable tools or defined sequences. For example, an agent might store a `MonthlyReportIntent` procedure. When a user asks for a report, the agent retrieves this procedure: 1) Query sales DB, 2) Summarize findings, 3) Email user. This makes behavior reliable and predictable. It encodes successful workflows so the agent doesn’t have to reason from scratch every time [[11]](https://arxiv.org/html/2508.06433v2).

This type of memory is key for workflow automation agents. It reduces repetitive deliberation, allowing the agent's reasoning to focus on novel situations. For complex tasks, procedural memory enables smooth orchestration. An agent booking travel doesn't just know facts about airlines (semantic) or remember past trips (episodic); it knows *how* to execute the multi-step process of searching, comparing, and booking [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). This memory can be treated as code, versioned, and updated based on user feedback or automated analysis of interactions [[3]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

Now that we know what to save, we must decide _how_ to store it.
```
**Grader reasoning:**
- `cc`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections cover Semantic, Episodic, and Procedural memory with matching definitions and the same illustrative examples. The generated section adds a 'junk drawer' curation-failure analogy under Semantic Memory and a 'treat procedural memory as code, keep it under source control' point under Procedural Memory (both verified below as genuine depth additions), plus a domain-expert/law-and-finance elaboration and a case-based-reasoning/financial-advisor example that are present in research.md's exploitation-phase content but do not trace to any exploration source (so they don't count as enhancement, though they don't omit anything either). No expected idea is missing.
- `fl`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** The three memory types appear in the identical order with matching internal progression; the added sentences sit at the end of their respective subsections as trailing elaborations.
- `de`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** [instances=2; quality=strong,strong] (1) The 'junk drawer' analogy for uncurated semantic memory traces directly to the exploration-phase Practical Guide's Semantic Memory subsection ('without it, semantic memory becomes a junk drawer'). (2) 'This memory can be treated as code, versioned...' traces to the same source's 'Practical Takeaways' section ('Treat procedural memory as code... keep them under source control') and its Procedural Memory subsection (updates driven by user feedback). Both are named, specific practices rather than passing mentions — strong. (The domain-expert/law-and-finance point and the case-based-reasoning/financial-advisor example are present only in exploitation-phase content, per core_content, so neither counts here.)
- `be`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] Both qualifying additions deepen understanding of how each memory type is implemented in practice; neither connects outward to an adjacent field.
- `cp`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** depth_enhancement=1 for this section, so this is evaluated rather than defaulted: both additions are single trailing sentences within their own subsections, proportionate relative to the core definitions and examples, which remain dominant. No dilution.
- `ga`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** At 645 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0. Content otherwise matches the guideline's three memory types and examples closely.

### Arm: standard (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/episodes/10_memory_knowledge_access__var_standard__preset3`

**Article text:**
```
## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a single, monolithic block of data. Just as in human cognition, we can divide it into different types based on what is stored and how it is used [[5]](https://arxiv.org/html/2309.02427), [[6]](https://www.ibm.com/think/topics/ai-agent-memory). Understanding these distinctions is key to designing a memory architecture that fits your product's needs.

### Semantic Memory (Facts & Knowledge)

**Semantic memory** is the agent's encyclopedia, a repository of factual information. These facts can be stored as simple, independent strings like "The user is a vegetarian" or as structured data attached to an "entity" like a person, place, or object (e.g., `{"user": {"food_restrictions": "allergic to gluten"}}`) [[7]](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents). The structure and content of this memory are highly dependent on the agent's purpose. For example, a personal AI assistant focused on user personalization will prioritize episodic memory, while a domain expert agent in finance will rely more heavily on semantic memory [[8]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

The primary role of semantic memory is to provide a reliable source of truth. For an enterprise agent, this might involve storing internal company documents or a product catalog, allowing it to answer questions on proprietary topics. For a personal assistant, semantic memory is used to build a persistent user profile. It can store preferences ("User likes rock music"), relationships ("User has a dog named George"), or constraints ("User's budget is $500") [[9]](https://mem0.ai/blog/long-term-memory-ai-agents). By retrieving these facts, the agent can offer personalized responses instead of relying on a noisy and lengthy conversation history. This curation step is critical; without it, semantic memory becomes a junk drawer of unsorted information [[4]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

### Episodic Memory (Experiences & History)

**Episodic memory** is the agent's personal diary, a chronological record of its past interactions [[7]](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents). Think of these as facts with a timestamp attached. Unlike the timeless knowledge in semantic memory, episodic memories are about "what happened and when." They capture the specific events, actions, and outcomes of an agent's experiences, preserving the temporal sequence and context of each interaction [[10]](https://ctoi.substack.com/p/memory-systems-in-ai-agents-episodic).

This memory type is essential for maintaining conversational context and understanding complex dynamics over time. For example, a semantic memory might store "User's brother is named Mark" and "User is frustrated with his brother." An episodic memory captures a richer story: *"On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I provided an empathetic response. [created_at=2025-08-25T17:20:04]"*.

This episode provides nuanced context, allowing the agent to interact with more intelligence in the future (e.g., "I know the topic of your brother's birthday can be sensitive..."). The time element also enables temporal queries like "What did we talk about last week?" Depending on the use case, these memories can group events from a single conversation, a full day, or even a week. There is no one-size-fits-all solution; the right time scale depends on the product. For agents that need to learn from experience, episodic memory is indispensable [[8]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

### Procedural Memory (Skills & How-To)

**Procedural memory** is the agent's collection of skills and learned workflows—its "muscle memory" [[6]](https://www.ibm.com/think/topics/ai-agent-memory). It stores the "how-to" knowledge that enables it to perform multi-step tasks reliably and automatically. This is the memory of processes, routines, and executable skills that the agent can apply without conscious reasoning for each step [[11]](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory).

This memory is often encoded as a reusable tool, function, or a defined sequence of actions, sometimes as part of the system prompt [[12]](https://arxiv.org/html/2508.06433v2). For instance, an agent might have a stored procedure for generating a monthly report. When a user requests an update, the agent does not need to reason from scratch. Instead, it retrieves the `monthly_report` procedure, which outlines a clear series of steps: 1. Query the sales database for the last 30 days, 2. Summarize the top five insights, and 3. Ask the user for their preferred output format [[13]](https://www.geeksforgeeks.org/artificial-intelligence/ai-agent-memory/).

This makes the agent's behavior on common tasks highly predictable and efficient. By encoding successful workflows, procedural memory allows an agent to improve its task completion over time, reducing errors and ensuring complex jobs are executed consistently. For workflow automation agents that handle repetitive processes, procedural memory is the most critical component [[8]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

Now that we have a clear idea of what to save and the benefits of each memory type, a new question arises: how should we store this information?
```
**Grader reasoning:**
- `cc`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections break down long-term memory into the same three categories (Semantic, Episodic, Procedural) and describe their functions and use cases in a similar manner.
- `fl`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections follow the same logical progression, discussing Semantic, then Episodic, then Procedural memory in that order. The transitions between the subsections are smooth in both.
- `de`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No depth additions present. The generated section provides similar examples and explanations as the expected output without adding deeper technical nuances, limitations, or case studies traceable to exploration-phase sources.
- `be`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No breadth additions present. The section stays within the core topic of memory types.
- `cp`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both depth_enhancement and breadth_enhancement scored 0, meaning no qualifying additions were identified. CorePreservation scores 1 by default.
- `ga`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** The generated section successfully covers all the required points for the three types of long-term memory. For Semantic Memory, it defines it as the agent's "encyclopedia" and explains its use for storing facts and building user profiles. For Episodic Memory, it defines it as the agent's "personal diary" with timestamps and explains its use for maintaining conversational context with a clear example. For Procedural Memory, it defines it as the agent's "muscle memory" and explains its use for reliable task execution with an example. The transition to the next section is also present. The prose-only word count is approximately 420 words, which is within the 400-word target.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate1__preset3`

**Article text:**
```
## Long-Term Memory: Semantic, Episodic, and Procedural

Just as human long-term memory is not a single entity, an agent's long-term memory can be broken down into different types. This categorization helps us design systems that store and retrieve different kinds of information in the most effective way [[12]](https://langchain-ai.github.io/langgraph/concepts/memory/), [[16]](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents), [[17]](https://arxiv.org/html/2309.02427). Let's explore the three key types: semantic, episodic, and procedural memory.

### Semantic Memory (Facts & Knowledge)

**What it is:** Semantic memory is the agent's encyclopedia, a repository of factual knowledge. This is where the agent stores extracted concepts, relationships, and facts about specific domains, people, places, and things. The structure of this memory is highly dependent on the agent's use case. "Facts" can be individual, independent strings like "The user is a vegetarian," or they can be attached to an "entity," which can be a person, place, or object, in a more structured format like `{"food_restrictions": "User is a vegetarian"}`.

**How it's used:** The primary role of semantic memory is to provide the agent with a reliable source of truth. For an enterprise agent, this might involve storing internal company documents, technical manuals, or an entire product catalog, allowing it to answer questions on proprietary topics. For personal assistants, semantic memory is used to build a persistent profile of each user. It can recall specific, important information like preferences (`{"music": "User likes rock music"}`), relationships (`{"dog": "User has a dog named George"}`), or hard constraints (`{"food_restrictions": "User is allergic to gluten"}`). This allows the agent to retrieve relevant and important information directly, rather than depending on a noisy and very long conversation history.

### Episodic Memory (Experiences & History)

**What it is:** Episodic memory is the agent's personal diary, a record of its past interactions with the user and the context in which they occurred. Think of these memories as facts with a timestamp attached, adding an important element of time. Unlike the timeless facts in semantic memory, episodic memories are about "what happened and when." Depending on the use case, these memories can group important events that happened over a whole day, a single conversation, or a week. There is no one-size-fits-all solution; a different time scale might be needed for different products.

**How it's used:** This memory type is useful for maintaining conversational context and understanding complex dynamics, like a relationship. For instance, a simple system of facts might extract "User's brother is named Mark" and "User is frustrated with his brother" and save them to semantic memory. A system that captures the element of time might save: "On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I then provided an empathetic response. [created_at=2025-08-25T17:20:04.648191-07:00]". This "episode" provides a deeper, more nuanced context, allowing the agent to interact with more empathy and intelligence in the future (e.g., "As you expressed last week, I know the topic of your brother's birthday can be sensitive..."). With the time element, the agent can now also answer questions such as "What happened on June 8th?".

### Procedural Memory (Skills & How-To)

**What it is:** Procedural memory is the agent's collection of skills and learned workflows. It is the "how-to" knowledge that dictates its ability to perform multi-step tasks. This is the agent's muscle memory, a set of pre-defined playbooks for common requests.

**How it's used:** This memory is often encoded directly into the agent's system prompt as a "reusable tool," function, or defined sequence of actions. For example, an agent might have a stored procedure called `MonthlyReportIntent`. When a user asks for a monthly update, the agent does not need to reason from scratch about how to create a report. Instead, by retrieving from its procedural memory, the procedure can be used, defining a clear series of steps: 1) Query the sales database for the last 30 days, 2) Summarize the key findings, and 3) Ask the user if they want the summary emailed or displayed directly. This makes the agent's behavior on common tasks highly reliable, fast, and predictable. By encoding successful (and even unsuccessful) workflows, procedural memory allows an agent to improve its task completion efficiency over time, reducing errors and ensuring that complex jobs are executed consistently every time.

Now that we have an idea of what to save and the benefits of each memory type, how should we store this information? The storage architecture we choose has a significant impact on our agent's performance.
```
**Grader reasoning:**
- `cc`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections cover Semantic, Episodic, and Procedural memory with matching definitions and the same illustrative examples. No expected idea is missing, and no additions are present in this particular section.
- `fl`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** The three memory types appear in the identical order with matching internal progression.
- `de`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist for this episode (extensively, for this article), so this is a content-based 0, not the code-level hard zero.
- `be`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist for this episode (extensively, for this article), so this is a content-based 0, not the code-level hard zero.
- `cp`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default.
- `ga`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** At 721 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0. Content otherwise matches the guideline's three memory types and examples closely.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/10_memory_knowledge_access__var_standard__replicate2__preset3`

**Article text:**
```
## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a monolith. Just as our own minds organize information differently, an agent's long-term memory can be broken down into specialized components. Borrowing again from cognitive science, we can categorize it into three key types: semantic, episodic, and procedural [[1]](https://arxiv.org/html/2309.02427).

### Semantic Memory (Facts & Knowledge)

**Semantic memory** is the agent's encyclopedia. It is a repository of individual pieces of knowledge. These "facts" can be independent strings like "The user is a vegetarian," or they can be attached to an "entity" like a person, place, or object. This is where the agent stores extracted concepts and relationships about specific domains. What you decide to store and how you structure it depends heavily on the agent's use case. It could even be structured as a graph database.

The primary role of semantic memory is to provide the agent with a reliable source of truth. For an enterprise agent, this might involve storing internal company documents, technical manuals, or an entire product catalog, allowing it to answer questions on proprietary topics. For a personal assistant, semantic memory is used to build a persistent profile of each user. It can recall specific information like preferences (`{"music": "User likes rock music"}`), relationships (`{"dog": "User has a dog named George"}`), or hard constraints (`{"food_restrictions": "User is allergic to gluten"}`). This capability allows the agent to retrieve relevant and important information directly, rather than depending on a noisy and very long conversation history.

### Episodic Memory (Experiences & History)

**Episodic memory** is the agent's personal diary, a record of its past interactions with the user. It is a log of specific events with a timestamp attached, adding the element of time. Unlike the timeless facts in semantic memory, episodic memories are about "what happened and when."

This memory type is useful for maintaining conversational context and understanding complex dynamics. For instance, a simple system of facts might extract "User's brother is named Mark" and "User is frustrated with his brother" and save them to semantic memory. A system that captures the element of time might save an episode: `"On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I then provided an empathetic response. [created_at=2025-08-25T17:20:04.648191-07:00]"`.

This episode provides a deeper, more nuanced context, allowing the agent to interact with more empathy and intelligence in the future if the topic of the brother comes up again (e.g., "As you expressed last week, I know the topic of your brother's birthday can be sensitive..."). With the time element, the agent can also answer questions such as "What happened on June 8th?" Depending on the use case, these episodic memories can group important events that happened during a whole day, a single conversation, or over the span of a week. There is no one-size-fits-all solution; different products require different time scales.

### Procedural Memory (Skills & How-To)

**Procedural memory** is the agent's collection of skills and learned workflows. It is the "how-to" knowledge that dictates its ability to perform multi-step tasks, acting as the agent's muscle memory or a set of pre-defined playbooks for common requests [[2]](https://langchain-ai.github.io/langgraph/concepts/memory/).

This memory is often baked directly into the agent's system prompt as a "reusable tool," function, or defined sequence of actions. For example, an agent might have a stored procedure called `MonthlyReportIntent`. When a user asks for a monthly update, the agent does not need to reason from scratch about how to create a report. Instead, by retrieving from its procedural memory, the procedure can be used, defining a clear series of steps: 1) Query the sales database for the last 30 days, 2) Summarize the key findings, and 3) Ask the user if they want the summary emailed or displayed directly. This makes the agent's behavior on common tasks highly reliable, fast, and predictable. By encoding successful (and even unsuccessful) workflows, procedural memory allows an agent to improve its task completion efficiency over time, reducing errors and ensuring that complex jobs are executed consistently every time.

Now that we have an idea of what to save and the benefits of specific types of memories, how should they be stored?
```
**Grader reasoning:**
- `cc`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both sections cover Semantic, Episodic, and Procedural memory with matching definitions and the same illustrative examples. No expected idea is missing, and no additions are present in this particular section.
- `fl`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** The three memory types appear in the identical order with matching internal progression.
- `de`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist extensively for this episode, so this is a content-based 0, not the code-level hard zero.
- `be`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** [instances=0] No depth/breadth additions are present in this section. Exploration-phase sources exist extensively for this episode, so this is a content-based 0, not the code-level hard zero.
- `cp`: Long-Term Memory: Semantic, Episodic, and Procedural:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section, so the mandatory default rule applies: core_preservation is 1 by default.
- `ga`: Long-Term Memory: Semantic, Episodic, and Procedural:
**0:** At 682 prose-only words against a 400-word target (tolerance ceiling ~440 words), this section is substantially over length, which alone drives this score to 0.
