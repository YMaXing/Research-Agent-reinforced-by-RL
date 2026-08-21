# Retrieval-Augmented Generation: The LLM's Open-Book Exam

In our previous lessons, we have explored the foundational concepts of AI Engineering. We learned about the agent landscape, the difference between LLM workflows and AI agents, and the importance of Context Engineering. As we covered in Lesson 3, context engineering is the art and science of managing the information flow to an LLM to guide its behavior and improve its performance. Now, we will dive deep into one of the most critical techniques in an AI Engineer's toolkit: Retrieval-Augmented Generation (RAG).

LLMs are powerful, but they have a fundamental limitation: their knowledge is frozen in time. They are trained on a fixed dataset, which means they are essentially taking a "closed-book exam" on the world's information as it existed at one point. They cannot learn new information after their training is complete. While you can update a model's knowledge with fine-tuning, it is a slow, expensive, and resource-intensive process. It requires carefully curating large, high-quality datasets and running multi-day training jobs that consume significant computational resources. Furthermore, it carries the risk of "catastrophic forgetting," a phenomenon where the model loses some of its original, general-purpose capabilities while learning new, specialized information.

You might think that ever-larger context windows solve this problem, but they introduce their own challenges. First, they are finite. There will always be more information in the world than can fit into any context window. Second, cost and latency scale with the amount of information you stuff into a prompt. Processing a one-million-token context is far more expensive and slower than processing a few thousand tokens. Finally, performance often degrades as context length increases due to the "lost-in-the-middle" problem. Models have a well-documented tendency to recall information from the beginning and end of a long context far more reliably than information buried deep within the middle.

This is where RAG comes in. Instead of trying to force a model to memorize everything, we give it an "open-book exam." RAG connects the LLM to external, real-time knowledge sources, allowing it to retrieve relevant information on the fly. Just as a human expert does not need to memorize an entire library, an LLM with RAG can access cheat sheets, manuals, and documents to answer questions accurately and with up-to-date information.

This lesson will explore the "what" and "how" of RAG, from its core components to the advanced and agentic patterns that power modern AI systems. We will see how RAG is not just a technique but a foundational piece of context engineering. In our next lesson on Memory for Agents, we will discuss how short- and long-term memory stores complement the on-demand retrieval that RAG provides.

With the problem and motivation clear, we’ll first decompose RAG into its core components so you can see where each responsibility lies.

## The RAG System: Core Components

Understanding the components of a RAG system is the first step in the context engineering process of designing effective retrieval-based applications. At its core, a RAG system is built on three conceptual pillars: Retrieval, Augmentation, and Generation.

Image 1: A flowchart illustrating the core components and data flow of a Retrieval Augmented Generation (RAG) system.

**Retrieval** is the engine that finds relevant information. When a user asks a question, the retrieval system searches an external knowledge base to find documents or data snippets that are likely to contain the answer. The most common approach is semantic search, which relies on vector embeddings. Vector embeddings are numerical representations of text that capture its semantic meaning. To create them, a specialized embedding model processes a piece of text and outputs a list of numbers—a vector—that represents the text's position in a high-dimensional space. Texts with similar meanings will have vectors that are close to each other in this space. These embeddings are then stored in a vector database, which is a specialized database optimized for performing incredibly fast similarity searches across millions or even billions of vectors.

**Augmentation** is the process of taking the retrieved information and integrating it into the prompt that will be sent to the LLM. This step is crucial for providing the model with the necessary context to answer the user's query accurately. The augmented prompt is carefully constructed to include the original user query, the retrieved document chunks, and a set of instructions telling the LLM how to use the provided information. For example, the instructions might say: "Answer the user's question based only on the following context. If the answer is not in the context, say so." This creates a clear, structured input that grounds the model's generation process in factual data.

**Generation** is the final step where the LLM uses the augmented prompt to produce an answer. Because the prompt now contains relevant, factual information from the external knowledge base, the LLM can synthesize this information to generate a response that is grounded in the provided data. This significantly reduces the risk of hallucination and ensures that the answer is accurate and up-to-date. The final output is no longer just a guess based on the model's training data but an informed response backed by retrieved evidence.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow is split into two distinct phases: an offline ingestion phase, where the knowledge base is prepared, and an online retrieval phase, where user queries are answered in real-time.

Image 2: A detailed flowchart depicting the end-to-end RAG workflow, divided into two distinct phases: "Offline Ingestion & Indexing" and "Online Retrieval & Generation".

### Phase 1: Offline Ingestion & Indexing

This phase is all about preparing your data for efficient retrieval. It involves a series of steps to transform raw documents into a searchable knowledge base.

First, we **Load** the data. This involves reading documents from various sources, which can include PDFs, websites, databases, or APIs. This step comes with its own challenges, such as dealing with complex PDF layouts, extracting clean text from messy HTML, or connecting to proprietary database formats. Tools like LangChain's document loaders or LlamaIndex's readers are commonly used to handle these complexities.

Next, we **Split** the content into smaller, more manageable pieces. This process, known as chunking, is critical for retrieval quality. The goal is to create chunks that are semantically coherent and self-contained, avoiding splits in the middle of a sentence or idea. You can use rule-based splitters, like LangChain’s `RecursiveCharacterTextSplitter` which splits based on character counts, or more advanced semantic chunkers that use the model's understanding of language to find natural breakpoints in the text.

Then, we **Embed** each chunk. An embedding model, such as OpenAI's `text-embedding-3-small`, Google's `text-embedding-004`, or open-source variants like BGE models from Hugging Face, converts the text of each chunk into a vector embedding. The choice of embedding model is important, as it determines how well the semantic meaning of your documents is captured. Some models are optimized for performance, while others prioritize cost or can be run locally.

Finally, we **Store** the embeddings and their corresponding text in a vector database. This database, which could be a local, file-based solution like FAISS for quick prototyping or a managed, scalable service like Milvus, Qdrant, or Pinecone for production, indexes the vectors for fast similarity lookups. This index is what allows the system to quickly find the most relevant chunks for a given query.

### Phase 2: Online Retrieval & Generation

This phase happens in real-time when a user interacts with the system.

It begins with a user **Query**. The user asks a question, which can optionally be normalized or expanded to improve its clarity and searchability.

The system then **Embeds** the query, using the same embedding model that was used during the ingestion phase. This is critical to ensure that the query and the document chunks are in the same vector space, allowing for a meaningful comparison.

Next, the system **Searches** the vector database. It uses the query vector to find the top-k most similar document chunks based on a similarity metric like cosine similarity, which measures the angle between two vectors. This step retrieves the context that will be used to answer the user's question.

The final step is to **Generate** an answer. The system constructs a prompt that includes the original user query, the retrieved chunks, and instructions for the LLM. As we discussed in Lesson 4, using structured outputs can help ensure the answer is well-formatted and includes citations back to the source documents, which is crucial for building user trust. The LLM then synthesizes this information to produce a grounded, accurate response.

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While a basic RAG pipeline is powerful, production-grade systems often require more sophisticated techniques to handle the complexities of real-world data and user queries. These advanced methods significantly improve retrieval performance, leading to more accurate and relevant answers.

### Hybrid Search

Hybrid search combines the strengths of traditional keyword-based search (like BM25) with modern vector search. These keyword-based methods are not relics; they evolved from information retrieval systems of the 1990s that relied on algorithms like TF-IDF and BM25 [[60]](https://www.cloudthat.com/resources/blog/unveiling-the-journey-the-evolution-of-rag-systems). While vector search is great at understanding the semantic meaning of a query, it can sometimes miss exact matches for specific terms, names, or codes. BM25, on the other hand, excels at finding documents that contain the exact keywords from the query, making it a valuable tool for precision [[42]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/).

For example, in a customer support scenario, if a user asks, "my bill keeps rolling over," a keyword search will find articles containing the word "rollover." A semantic search might also surface guides about "carryover balance." By combining both, the system can cover different wordings of the same issue, improving recall and relevance [[40]](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834).

### Re-ranking

The initial retrieval step is optimized for speed and recall, meaning it quickly finds a broad set of potentially relevant documents. However, the best document might not always be at the top of the list. Re-ranking introduces a second, more sophisticated model, often a cross-encoder, to re-order this initial set of documents [[42]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/).

A cross-encoder model takes the user query and a candidate document as a pair and outputs a relevance score. This allows for a deeper interaction between the query and the document, leading to a much more accurate relevance ranking [[45]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/). For instance, when a user asks, "how to connect my account," a re-ranker can push a step-by-step setup guide to the top, above a less relevant press release or community forum thread.

Image 3: A flowchart illustrating the hybrid retrieval process in advanced RAG techniques.

### Query Transformations

Sometimes, the user's query is not in the ideal format for retrieval. Query transformation techniques modify the original query to improve its chances of matching the right documents.

-   **Decomposition:** This involves breaking down a complex, multi-part query into several simpler sub-questions [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html). For example, the question "What’s our travel policy for conferences in Europe this year?" could be decomposed into: "What is the travel policy?", "What are the rules for conferences?", and "Are there specific rules for Europe in 2024?". The system retrieves documents for each sub-question and then merges the results to form a comprehensive answer.
-   **Hypothetical Document Embeddings (HyDE):** This technique generates a hypothetical, ideal answer to the user's query before performing the search [[20]](https://neo4j.com/blog/genai/advanced-rag-techniques/). The system then embeds this hypothetical document and uses it for the similarity search. The idea is that an ideal answer is more likely to be semantically similar to the actual answer document than the original question. For a query about employee travel, the system might draft a short answer like, "Employees can book economy flights and up to three hotel nights," and then search for documents that match that statement.

### Advanced Chunking Strategies

How you split your documents into chunks has a massive impact on retrieval quality. Moving beyond simple fixed-size chunks can preserve more context and improve relevance.

-   **Semantic Chunking:** Instead of splitting by a fixed number of characters, semantic chunking splits documents along natural boundaries like paragraphs or sections. This ensures that complete ideas and their surrounding context are kept together. For example, splitting a 20-page handbook by section headings keeps the entire "Reimbursements" section intact, preventing critical information like spending caps from being separated from the main policy.
-   **Layout-Aware Chunking:** For complex documents like PDFs with tables or forms, layout-aware chunking preserves the document's structure. When processing a pricing table, this method keeps each row (product, price, discount) together, rather than slicing the page by character count and separating numbers from their labels.
-   **Context-Enriched Chunking:** This technique, also known as contextual retrieval, adds a summary or contextual information to each chunk before embedding it. For example, a chunk from a financial report might be prepended with "This chunk is from ACME Corp's Q2 2023 report" to provide necessary context that is missing from the chunk itself.

### GraphRAG

GraphRAG introduces the use of knowledge graphs for retrieval. This approach excels at answering questions about complex relationships and interconnected entities, which are often lost in standard document chunks [[46]](https://arxiv.org/html/2601.03014v1). It helps solve problems where understanding the "how" and "why" between data points is crucial.

For example, in a retail scenario, a query like "Which shoes get the most size-related returns and were featured in last month’s ads?" requires connecting multiple pieces of information. A GraphRAG system can traverse the knowledge graph from returns to their reasons (sizing), to specific products, and then to the marketing calendar, assembling a precise answer from interconnected data [[50]](https://arxiv.org/html/2501.00309v2).

### Metadata Filtering

One of the most effective techniques in production is metadata filtering. By adding metadata tags to each chunk—such as `source`, `department`, `effective_date`, or `language`—you can significantly narrow down the search space before performing the vector search.

A key implementation choice is whether to apply these filters before or after the vector search. Pre-filtering applies metadata constraints first, which is efficient for highly selective filters but can sometimes miss the best semantic matches if the filter is too restrictive. Post-filtering finds the most semantically similar vectors first and then filters them, which guarantees finding the best matches but can be inefficient if many results are discarded [[61]](https://oneuptime.com/blog/post/2026-01-30-metadata-filtering/view). Most production systems use a hybrid approach.

This technique is also essential for implementing robust security and access control. In high-stakes domains like finance, RAG systems use "identity-aware" retrieval, where metadata filters automatically enforce user permissions based on their role or department. This ensures the AI is physically unable to retrieve and surface documents a user is not authorized to see [[63]](https://www.tericsoft.com/blogs/top-10-llm-rag-architectures-for-fintech-operations). However, be aware of platform limitations. Some managed services use metadata for filtering during retrieval but do not inject those attributes into the final prompt, meaning the LLM itself is unaware of the context (e.g., the source document ID) it is reasoning over [[62]](https://repost.aws/questions/QUikNkU5ZGRTGDuf4zXkmxVg/trouble-with-aws-bedrock-metadata-filtering-for-agents-kb-retrieve-apis).

Temporal filters are particularly powerful. For a query like, "What changed between March and June 2025?", the system can restrict the search to chunks with an `effective_date` within that range. This ensures that only relevant, time-sensitive information is retrieved, preventing outdated policies or information from cluttering the results.

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored the ReAct framework, where an agent cycles through a loop of Thought, Action, and Observation. Agentic RAG is essentially a ReAct-style agent equipped with a retrieval tool. Instead of following a fixed pipeline, the agent reasons about when it has a knowledge gap and decides to call its RAG tool to find the information it needs.

It is important to clarify that agents typically have access to many tools, such as web search, code interpreters, and database query tools. Labeling an entire system "agentic RAG" can be a bit narrow, as the retrieval tool is just one of several capabilities the agent can leverage [[12]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/).

The core distinction between standard and agentic RAG lies in their control structure:

*   **Standard RAG** follows a linear, pre-determined workflow: Retrieve → Augment → Generate. It is powerful but rigid, as every query follows the same path.
*   **Agentic RAG** is adaptive and iterative. An agent decides *when* to retrieve, *how* to reformulate a query, *which* knowledge source to search, and whether it needs to chain multiple retrieval and reasoning steps to answer a complex question [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

This agentic approach unlocks several advanced capabilities. The agent can iteratively use the RAG tool, refining its query based on initial results. It can choose which part of its knowledge base to search, for example, selecting `search_incident_runbooks` over `search_marketing_pages` for an outage inquiry. It can also fuse information from its internal RAG tool with data from other tools, like a web search, to form a more comprehensive answer.

Here is a conceptual "thought process" for an agent tackling a query about outdated regulations:

**Thought:** "The user is asking about '2024 EU data retention rules.' Our internal policy documents cite the 2023 version, which is likely outdated."

**Action:** `retrieve(internal_policy, query="EU data retention 2024")`

**Observation:** "The retrieved documents mention amendments but are missing specific citations for the 2024 changes."

**Thought:** "I need external verification to confirm the latest updates."

**Action:** `web_search(query="EU data retention rules 2024 official directive")`

**Observation:** "Found the official EU directive with the 2024 updates."

**Thought:** "Now I can synthesize the information from our internal policy and the official directive, highlighting the changes from 2023 and citing both sources."

Image 4: A conceptual flowchart illustrating an agent's main loop in Agentic RAG, showing the iterative process of thought, action, tool use, and observation.

This agentic flexibility is powerful, but it comes with engineering trade-offs. The multi-step reasoning process can increase latency, and multiple calls to expensive LLMs can drive up costs. Furthermore, the increased system complexity introduces more potential points of failure. If any one of the agent's tools fails or the agent gets stuck in a reasoning loop, the entire process can break down, making reliability a significant challenge to address when moving from prototypes to production [[65]](https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/).

This represents a shift from viewing RAG as an isolated process to seeing it as a core tool in an agent's toolkit. It is the difference between a simple database lookup and a conversation with a knowledgeable research assistant who can reason, strategize, and synthesize information from multiple sources.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have journeyed from the fundamentals of RAG to the sophisticated patterns that define modern AI systems. The key takeaway is that RAG is the most effective and widely used solution to the LLM knowledge problem. While basic RAG provides a solid foundation, advanced techniques are essential for building production-grade applications that can handle the complexity of real-world data. The future of knowledge retrieval is agentic, where RAG transforms from a static pipeline into a dynamic tool that intelligent agents can use to reason and solve problems.

The core benefits of RAG are clear: it reduces hallucinations, enables customization with proprietary data, and builds user trust by providing verifiable, source-backed answers. These benefits are being realized today in high-stakes industries. For example, a regional bank implemented a RAG-based compliance assistant that reduced manual document review time by 68% and cut audit response time in half, transforming a reactive reporting process into proactive risk management [[64]](https://saison-technology-intl.com/resource/compliance-intelligence-rag-financial-services/). For the modern AI Engineer, mastering RAG is not a niche skill but a foundational competency. It is a critical component of the broader discipline of Context Engineering, allowing you to build AI systems that are not just intelligent but also grounded, reliable, and trustworthy.

In our next lesson, we will explore Memory for Agents, a topic that complements RAG. While RAG provides on-demand, just-in-time information retrieval, memory systems give agents the ability to learn and retain information across interactions. We will also touch on other important topics later in this course, such as how to evaluate retrieval quality and monitor RAG systems in production to ensure they continue to perform at a high level.

## References

- [1] https://neo4j.com/blog/developer/fine-tuning-vs-rag/
- [2] https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html
- [3] https://aclanthology.org/2024.emnlp-main.15.pdf
- [4] https://arxiv.org/html/2312.05934v3
- [5] https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0
- [6] https://qdrant.tech/articles/what-is-rag-in-ai/
- [7] https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5
- [8] https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/
- [9] https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/
- [10] https://airbyte.com/agentic-data/ai-agent-vs-rag
- [11] https://domino.ai/blog/rag-vs-agentic-ai
- [12] https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/
- [13] https://docs.nvidia.com/rag/latest/query_decomposition.html
- [14] https://neo4j.com/blog/genai/advanced-rag-techniques/
- [15] https://www.mindstudio.ai/blog/what-is-rag/
- [16] https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/
- [17] https://humanloop.com/blog/rag-architectures
- [18] https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/
- [19] https://www.ibm.com/think/topics/retrieval-augmented-generation
- [20] https://newsletter.systemdesign.one/p/how-rag-works
- [21] https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/
- [22] https://aws.amazon.com/what-is/retrieval-augmented-generation/
- [23] https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834
- [24] https://arxiv.org/html/2407.00072v5
- [25] https://redis.io/blog/10-techniques-to-improve-rag-accuracy/
- [26] https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/
- [27] https://arxiv.org/html/2601.03014v1
- [28] https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf
- [29] https://atlan.com/know/what-is-graphrag/
- [30] https://arxiv.org/html/2501.00309v2
- [31] https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/
- [32] https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/
- [33] https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/
- [34] https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/
- [35] https://www.promptingguide.ai/research/rag
- [36] https://www.cloudthat.com/resources/blog/unveiling-the-journey-the-evolution-of-rag-systems
- [37] https://oneuptime.com/blog/post/2026-01-30-metadata-filtering/view
- [38] https://repost.aws/questions/QUikNkU5ZGRTGDuf4zXkmxVg/trouble-with-aws-bedrock-metadata-filtering-for-agents-kb-retrieve-apis
- [39] https://www.tericsoft.com/blogs/top-10-llm-rag-architectures-for-fintech-operations
- [40] https://saison-technology-intl.com/resource/compliance-intelligence-rag-financial-services/
- [41] https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/