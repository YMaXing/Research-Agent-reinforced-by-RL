## Global Context of the Lesson

### What We Are Planning to Share

This lesson provides concise knowledge about the Retrieval Augmented Generation (RAG) method. This method consists of retrieving important/relevant information from external sources based on a user's query and adding it into the context window of the LLM.

RAG is one of the key methods we use for context engineering (taught in Lesson 03 of the course). We will explore how RAG is getting integrated into "agentic" pipelines, transforming agents from relying on static knowledge to reasoning over dynamic, external data sources. A key focus is distinguishing standard RAG from agentic RAG (i.e., a ReAct-style agent equipped with a retrieval tool). The lesson will cover practical architectures, and strategies.

### Why We Think It's Valuable

RAG is one of the core technologies (and part of the context engineering work done by AI Engineers) for building AI agents that are grounded, trustworthy, and knowledgeable. It directly addresses LLM limitations like knowledge cut-offs and hallucinations. For an AI Engineer, mastering RAG is not optional—it's a fundamental skill for creating agents that can leverage proprietary data, access real-time information, and provide accurate, source-backed answers. This lesson provides practical and conceptual knowledge needed to understand RAG-powered systems.

### Expected Length of the Lesson
**3,200 words** (without the titles and references), where we assume that 200-250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

100% theory - 0% real-world examples

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons.

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- Use the points of view described below.
- To not reintroduce concepts already taught in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is Lesson 9 (from part 1) of the course on AI Agents.

The article H1 title must follow the format `# Lesson 9: <Your Creative Subtitle Here>`.

### Point of View
The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

Aspiring AI engineers who are learning about RAG for the first time.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

Part 1:
- Lesson 1 - AI Engineering & Agent Landscape: Role, stack, and why agents matter now
- Lesson 2 - Workflows vs. Agents: Predefined logic vs. LLM-driven autonomy
- Lesson 3 - Context Engineering: Managing information flow to LLMs
- Lesson 4 - Structured Outputs: Reliable data extraction from LLM responses
- Lesson 5 - Basic Workflow Ingredients: Chaining, parallelization, routing, orchestrator-worker
- Lesson 6 - Agent Tools & Function Calling: Giving your LLM the ability to take action
- Lesson 7 - LLM Planning & Reasoning (ReAct and Plan-and-Executre)
- Lesson 8 - Implementing ReAct: Building a reasoning agent from scratch

As this is only the 9th lesson of the course, we have introduced some of the core concepts. At this point, the reader knows what an LLM is, ideas about LLM workflows, AI agents landscape, structured outputs, tools for agents, and ReAct agents.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:

Part 1:
- Lesson 10 (next) - Memory for Agents: Short-term vs. long-term memory (procedural, episodic, semantic)
- Lesson 11 - Multimodal Processing: Documents, images, and complex data

Part 2:

- MCP
- Developing the research agent and the writing agent

Part 3:

- Making the research and writing agents ready for production
- Monitoring
- Evaluations

If you must mention these, keep it high-level and note we will cover them in their respective lessons.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in their educational journey is critical for this piece. You have to use only previously introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using them, use intuitive analogies or explanations that are more general and easier to understand, as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer to them as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer to it as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are only allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection, explicitly specify in what lesson it will be explained in more detail, leveraging the particulars from the subsection. If not explicitly specified in the subsection, simply state that we will cover it in future lessons without providing a concrete lesson number. 

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we learning to solve? Why is it essential to solve it?
    - Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger field of AI Engineering. Add course next steps.

## Lesson Outline

1. Introduction: Giving LLMs an Open-Book Exam
2. The RAG System: Core Components
3. The RAG Pipeline: Ingestion and Retrieval
4. Advanced RAG Techniques
5. Agentic RAG
6. Conclusion

## Section 1 - Introduction: Giving LLMs an Open-Book Exam

- Begin with a short personal story from our early experiments with LLMs: we asked a model about recent events or proprietary company data only to receive confident but completely fabricated answers, highlighting the frustration of knowledge cut-offs and hallucinations.
- Tie this directly to context engineering from Lesson 3: the core challenge is ensuring the right information reaches the LLM at the right time rather than hoping the model has memorized it.
- Introduce the "open-book exam" analogy in depth: contrast a closed-book exam (parametric knowledge only, prone to forgetting or fabricating details) with an open-book exam (LLM can reference external materials), explaining why the latter produces more trustworthy outputs.
- Explain the fundamental limitations this addresses: static training data becomes outdated the moment it is cut off; parametric memory cannot be updated without expensive retraining; hallucinations occur when the model fills knowledge gaps with plausible but incorrect tokens.
- Address the 'lost in the middle' problem: even with a large context window, attention degrades for content buried deep in long inputs — naive context stuffing is unreliable; RAG solves this by retrieving only the most relevant chunks and injecting a focused, manageable amount of context.
- Position RAG as a foundational context engineering technique that dynamically augments the context window with relevant external data, turning agents from brittle systems into grounded reasoners.
- Establish the memory framing: RAG is the tool agents use to access external knowledge on demand; briefly note that in Lesson 10 we will contrast RAG-based retrieval with short- and long-term memory stores (which often use the same vector databases under the hood) — RAG is one essential building block of a complete agent memory architecture.
- Clarify that this lesson is 100% theoretical: we will dissect architectures, pipelines, failure modes, and progression from naive RAG to agentic variants without any implementation code or specific project deployments.
- Highlight why this matters for you as an aspiring AI engineer: RAG is no longer optional when building production agents that must remain accurate, up-to-date, and auditable.
- Use a simple diagram (describe in text for the writer to render) showing an LLM alone versus an LLM with a retrieval interface feeding external knowledge.
- Transition to Section 2: Now that we understand the problem RAG solves, we can break down the core components that make the system work.

-  **Section length:** 565 words

## Section 2 - The RAG System: Core Components

- Define RAG formally as a hybrid system that combines parametric knowledge (inside the LLM) with non-parametric knowledge (external data sources) through a retrieve-then-generate pattern.
- Break down the three canonical components with precise theoretical roles:
    - Retrieval: The mechanism that identifies and fetches the most relevant information given a query, typically using similarity in embedding space.
    - Augmentation: The process of intelligently inserting retrieved information into the prompt template so the LLM can condition its generation on it.
    - Generation: The LLM call itself, now producing responses grounded in the supplied external context.
- Discuss the embedding model as the translator between human language and vector space: explain how it creates dense numerical representations that capture semantic similarity rather than lexical overlap.
- Detail the vector database (or vector store) as the indexed memory layer that enables fast approximate nearest-neighbor search at scale; contrast this with traditional keyword search to show why vector similarity is superior for semantic tasks.
- Provide a Mermaid diagram scoped to inference time only: user query → Retrieval → Augmentation (retrieved passages injected into prompt) → Generation (LLM response). Keep the diagram focused on these three runtime components; ingestion and indexing steps are NOT part of this diagram (they belong in Section 3).
- Connect back to context engineering: RAG is the practical implementation of deciding "what information to provide" from long-term semantic memory.
- Discuss success metrics theoretically: relevance (measured by recall/precision of retrieved chunks), faithfulness (how closely the generated answer sticks to retrieved content), and answer quality (coherence and usefulness).
- Highlight that each component introduces its own trade-offs (embedding quality vs speed, chunk size vs context limits) which advanced techniques later attempt to optimize.
- Transition to Section 3: With the components defined, we can now examine the end-to-end pipeline that turns raw data into retrievable knowledge and queries into grounded answers.

-  **Section length:** 465 words

## Section 3 - The RAG Pipeline: Ingestion and Retrieval

- Separate the pipeline into two distinct phases—ingestion (offline, one-time or periodic) and retrieval/generation (online, per query)—and explain why this separation enables scalability.
- Dive deeply into the ingestion phase with step-by-step theoretical breakdown:
    - Data loading from heterogeneous sources (documents, databases, web content).
    - Chunking strategies: fixed-size, semantic, recursive, hierarchical; discuss pros and cons of each for information preservation.
    - Embedding generation: how each chunk is transformed into a high-dimensional vector; mention the importance of domain-specific embedding models versus general ones.
    - Indexing: building efficient data structures (inverted files, HNSW graphs) inside the vector store for sub-linear search.
- Cover the retrieval phase in matching detail:
    - Query transformation: embedding the user's question into the same vector space.
    - Similarity computation: cosine similarity, dot product, or maximum inner product search; explain why these metrics align with semantic closeness.
    - Top-k selection and the importance of choosing the right k value (too small loses information, too large causes information overload).
    - Optional reranking stage: using a more expensive cross-encoder to reorder initial results for higher precision.
- Illustrate the full pipeline with a detailed Mermaid flowchart (writer to create) that shows parallel paths for ingestion and query-time retrieval.
- Discuss theoretical failure modes already visible at this stage: poor chunk boundaries that split key concepts, embedding misalignment between query and document distributions, and the "lost in the middle" problem when too many chunks are stuffed into context.
- Explain how the retrieved context is formatted (e.g., as numbered passages or XML-tagged segments) to help the LLM distinguish source material from instructions.
- Emphasize that this pipeline is the minimal viable implementation of RAG; most production systems require the advanced techniques covered next.
- Transition to Section 4: The basic pipeline works for simple cases but quickly reveals limitations; we now explore sophisticated enhancements that address these weaknesses.

-  **Section length:** 625 words

## Section 4 - Advanced RAG Techniques

- Frame advanced RAG as a collection of optimizations applied at pre-retrieval, retrieval, and post-retrieval stages to improve relevance, reduce noise, and better utilize the context window.
- Pre-retrieval techniques:
    - Query decomposition: break a complex multi-faceted question into 3–4 targeted sub-questions, retrieve separately for each, then merge results — dramatically improves recall on questions that span multiple document sections. Walk through a concrete step-by-step example (e.g., a travel policy question decomposed into sub-questions about approved destinations, spending limits, and approval processes).
    - Metadata filtering: using structured attributes (date, source type, entity category) to constrain the vector search space before similarity scoring; this eliminates irrelevant document pools entirely before retrieval runs.
    - Hypothetical Document Embeddings (HyDE): generating a short hypothetical ideal-answer first, then using its embedding as the retrieval query — bridges the gap between question-style and answer-style embeddings.
- Retrieval enhancements:
    - Hybrid search: combining vector similarity with traditional BM25 keyword matching to capture both semantic and exact-term needs.
    - Multi-vector and late-interaction models: moving beyond single-vector-per-document representations.
    - Contextual retrieval (detail the technique from Anthropic's approach): enriching each chunk with surrounding context or query-aware summaries before embedding to reduce ambiguity.
- **Advanced Chunking Strategies:** Explain that ingestion quality directly determines retrieval quality; cover methods beyond fixed-size splitting:
    - Semantic chunking: splitting at natural sentence/paragraph boundaries that preserve meaning rather than at arbitrary character counts.
    - Layout-aware chunking: for structured documents (PDFs, tables, forms), respecting document structure so related rows, captions, and values stay together (e.g., a pricing table where fixed-size chunks would separate product names from their prices).
    - Context-enriched chunking: prepending a brief contextual summary to each chunk before embedding so the vector captures the chunk's role within the broader document.
- Post-retrieval optimizations:
    - Reranking with cross-encoders or LLM-based judges to reorder results by relevance to the specific query.
    - Context compression and summarization: condensing retrieved passages so more unique information fits inside the context window.
    - Result fusion from multiple indexes or embedding models.
- Dedicate substantial depth to GraphRAG (drawing from the arxiv paper "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"): explain how it builds knowledge graphs from documents, performs community detection, and generates summaries at multiple levels of granularity to handle global queries better than naive vector RAG.
- Present a comparison table (to be rendered in Markdown) contrasting naive RAG vs advanced RAG across dimensions: recall, precision, latency, token efficiency, and suitability for complex queries.
- Discuss failure modes addressed by these techniques: "Your RAG is wrong" scenarios such as lost context, irrelevant results dominating, and inability to synthesize across disparate sources; show how each advanced method mitigates specific failure modes.
- Include a conceptual diagram illustrating the advanced RAG pyramid with naive RAG at the base and increasingly sophisticated layers (query transformation, hybrid retrieval, graph methods, compression) stacked on top.
- Explain the theoretical trade-off curve: each improvement typically increases complexity, latency, or cost; the AI engineer must select the right level of sophistication for the use case.
- Transition to Section 5: These advanced techniques still assume a single retrieval step before generation; we now examine how turning retrieval into an agent tool creates an even more powerful paradigm.

-  **Section length:** 910 words

## Section 5 - Agentic RAG

- Define agentic RAG as the integration of retrieval capabilities into a reasoning agent (building directly on the ReAct pattern from Lesson 7 and Lesson 8) so the agent can decide when, what, and how often to retrieve rather than following a fixed single-retrieval pipeline.
- Contrast standard RAG (one-shot retrieval then generation) with agentic RAG (multi-step reasoning where retrieval is one available action among others): the agent can critique its own retrieved context, generate follow-up queries, combine information across multiple retrieval calls, or even decide retrieval is unnecessary.
- Detail the theoretical architecture: a ReAct-style loop where the agent has a "retrieve" tool that accepts natural language queries and returns ranked passages; the agent's scratchpad maintains retrieved context across turns.
- Explain the advantages for complex tasks: handling multi-hop questions, adapting retrieval strategy based on intermediate findings, incorporating verification steps, and dynamically balancing exploration versus exploitation of external knowledge.
- Discuss routing and orchestration aspects (referencing Lesson 5 concepts at a high level): an orchestrator can direct simpler queries to standard RAG while routing ambiguous or multi-faceted ones to the agentic variant.
- Cover key theoretical considerations: prompt design for the agent so it knows when to call the retrieval tool, managing context accumulation across multiple retrievals without exceeding limits, and implementing stopping conditions.
- Provide a Mermaid sequence diagram (to be rendered) showing the agent deciding to retrieve, receiving results, reasoning, retrieving again with a refined query, then generating a final grounded answer.
- Highlight how agentic RAG transforms the retrieval system from a static pipeline into a dynamic reasoning partner, directly supporting the shift toward more autonomous agents.
- Note that while powerful, agentic RAG increases latency and token usage, requiring careful evaluation (to be covered in future lessons).
- No transition line needed as this is the penultimate section.

-  **Section length:** 395 words

## Section 6 - Conclusion ...

- Summarize the theoretical journey: from the open-book exam metaphor, through core components and the basic pipeline, to advanced optimizations and finally the agentic integration that makes retrieval a first-class reasoning action.
- Reiterate that RAG is a cornerstone of context engineering, directly addressing the limitations of parametric knowledge and enabling agents that remain grounded in external, updatable data.
- Connect to the broader AI engineering field: RAG represents the fusion of information retrieval, embedding mathematics, prompt design, and agent orchestration; mastering its theory prepares you to make informed architectural choices.
- Anchor in the educational journey: this lesson builds on your understanding of context engineering (Lesson 3), tools (Lesson 6), and ReAct (Lessons 7-8); it sets the stage for Lesson 10 where we will explore memory for agents in more depth, including how semantic memory often leverages the same vector stores used in RAG.
- End with a forward-looking statement: as you continue through the course, you will see how these concepts combine into complete agent systems that are both intelligent and trustworthy.
- Provide a final conceptual diagram summarizing the RAG spectrum from naive to advanced to agentic.

-  **Section length:** 210 words

## Golden Sources

1. [What Is Retrieval-Augmented Generation, aka RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
2. [A Complete Guide to RAG](https://towardsai.net/p/l/a-complete-guide-to-rag)
3. [Retrieval-Augmented Generation (RAG) Fundamentals First](https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search)
4. [Your RAG is wrong: Here's how to fix it](https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search)
5. [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/html/2404.16130)

## Other Sources

1. [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
2. [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag)
3. [RAG is dead, long live agentic retrieval](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
4. [What is agentic RAG?](https://www.ibm.com/think/topics/agentic-rag)
5. [Build advanced retrieval-augmented generation systems](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
6. [The Rise of RAG](https://highlearningrate.substack.com/p/the-rise-of-rag)