# Lesson 9: Retrieval-Augmented Generation (RAG)

In our previous lessons, we have covered the fundamentals of AI Engineering, from context engineering and structured outputs to building reasoning agents with ReAct. You have learned how to give Large Language Models (LLMs) the ability to use tools and plan actions. However, even the most sophisticated agent is limited by its internal knowledge, which is static and prone to hallucination. When training, models take a "closed-book exam" on the world's information, and we do not yet have efficient techniques to update their knowledge after deployment.

This is where Retrieval-Augmented Generation (RAG) becomes essential. RAG is a method for connecting an LLM to external, real-time knowledge sources, effectively giving it an "open-book exam." Instead of relying on memorization, the model can look up facts when it needs them, similar to how we use manuals or cheat sheets. As we discussed in Lesson 3 on Context Engineering, RAG is a core technique for curating the information an LLM sees.

This lesson will explore the "what" and "how" of RAG, starting with its basic components and moving toward the advanced and agentic patterns that power modern AI systems. While RAG is a powerful tool for information retrieval, it complements the agent memory systems we will discuss in Lesson 10, which manage conversational history and user preferences.

With the problem and motivation clear, we will first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of a RAG system is the first step in the Context Engineering process of designing effective AI applications. At its core, the RAG framework is built on three conceptual pillars that work together to ground an LLM's response in external data.

*   **Retrieval:** This is the engine responsible for finding relevant information. When a user submits a query, the retrieval system searches an external knowledge base to find the most relevant documents or data chunks. This search is often powered by vector embeddings, which are numerical representations of text that capture semantic meaning. These embeddings are stored in a vector database, allowing for efficient similarity searches [[31]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177), [[52]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf).
*   **Augmentation:** Once the retriever finds the relevant information, the augmentation step takes this data and combines it with the original user query. This process creates an "augmented prompt" that provides the LLM with the necessary context to formulate an accurate and informed response [[29]](https://www.ibm.com/think/topics/retrieval-augmented-generation), [[56]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/).
*   **Generation:** In the final step, the augmented prompt is passed to the LLM. The model then uses this enriched context to generate a final answer. Because the response is based on the provided external data, it is "grounded," which means it is less likely to be a hallucination and can often include citations to the source material [[26]](https://humanloop.com/blog/rag-architectures), [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/).

```mermaid
flowchart LR
  %% Core components of a RAG system
  User["User"]
  Query["User Query"]
  Retriever["Retriever"]
  Augmentation["Augmentation"]
  Generator["Generator (LLM)"]
  Answer["Grounded Answer"]

  %% Sequential interactions
  User -- "submits" --> Query
  Query -- "processed by" --> Retriever
  Retriever -- "retrieved information" --> Augmentation
  Augmentation -- "augmented input" --> Generator
  Generator -- "produces" --> Answer
```
Image 1: A flowchart illustrating the core components and sequential interactions of a RAG system.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow is divided into two distinct phases: an offline ingestion pipeline that prepares the knowledge base and an online retrieval pipeline that answers user queries in real-time [[32]](https://newsletter.systemdesign.one/p/how-rag-works), [[33]](https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/).

### Phase 1: Offline Ingestion & Indexing

This phase is about preparing your external data so it can be efficiently searched. It involves several steps:

*   **Load:** The process begins by loading documents from various sources, such as PDFs, websites, or APIs.
*   **Split:** Large documents are broken down into smaller, more manageable "chunks." This is a critical step because it ensures that the retrieved context is focused and relevant. Chunking can be done based on fixed sizes or, more effectively, using semantic splitters that keep related ideas together [[52]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf).
*   **Embed:** An embedding model converts each text chunk into a numerical vector. These vectors capture the semantic meaning of the text. Popular models for this task include OpenAI's `text-embedding-3` series, Google's `text-embedding-004`, and open-source alternatives from Hugging Face [[8]](https://qdrant.tech/articles/what-is-rag-in-ai/).
*   **Store:** The vector embeddings and their corresponding text chunks are stored in a vector database. This specialized database is optimized for fast similarity searches, allowing the system to quickly find the chunks that are most relevant to a user's query [[6]](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0).

### Phase 2: Online Retrieval & Generation

This phase happens in real-time when a user interacts with the system.

*   **Query:** The user submits a question.
*   **Embed:** The same embedding model used during ingestion converts the user's query into a vector. This ensures that the query and the document chunks are represented in the same vector space, making them comparable [[51]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).
*   **Search:** The system uses the query vector to search the vector database, identifying the `top-k` document chunks with the highest semantic similarity. This is typically done using a distance metric like cosine similarity [[54]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).
*   **Generate:** The retrieved chunks are combined with the original query and system instructions to form a comprehensive prompt. This prompt is then sent to the LLM, which generates a final, grounded answer. As we learned in Lesson 4, using structured outputs can help ensure the answer is well-formatted and includes citations [[59]](https://www.promptingguide.ai/research/rag).

```mermaid
flowchart LR
  %% Phase 1: Offline Ingestion & Indexing
  subgraph "Phase 1: Offline Ingestion & Indexing"
    A["Document Sources<br/>(PDFs, Websites, APIs)"]
    B["Document Loaders"]
    C["Chunkers<br/>(RecursiveCharacterTextSplitter, SemanticSplitter)"]
    D["Embedding Models<br/>(OpenAI, Google's Gemini, Cohere Embed)"]
    E["Vector Database / Search Index<br/>(FAISS, Milvus, Qdrant, Pinecone)"]
  end

  %% Phase 2: Online Retrieval & Generation
  subgraph "Phase 2: Online Retrieval & Generation"
    F["User"]
    G["Query"]
    H["Vector Similarity Search"]
    I["LLM<br/>(Generate Grounded Answer)"]
    J["Grounded Answer"]
  end

  %% Connections for Phase 1
  A -- "load" --> B
  B -- "output documents" --> C
  C -- "output chunks" --> D
  D -- "create embeddings" --> E

  %% Connections for Phase 2
  F -- "submits" --> G
  G -- "embed query" --> D
  D -- "query embedding" --> H
  E -- "search" --> H
  H -- "retrieve top-k chunks" --> I
  I -- "generate" --> J

  %% Visual grouping
  classDef storage stroke-dasharray:3,3
  classDef exec stroke-width:2px

  class E storage
  class B,C,D,H,I exec
```
Image 2: A detailed flowchart depicting the end-to-end RAG pipeline, separated into two main phases: 'Phase 1: Offline Ingestion & Indexing' and 'Phase 2: Online Retrieval & Generation'.

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While the basic RAG pipeline is powerful, its performance can be significantly improved with more advanced techniques. These methods address the limitations of simple semantic search and help deliver more accurate and relevant results in production environments.

### Hybrid Search

This technique combines traditional keyword-based search, like BM25, with modern vector search. Keyword search excels at finding exact matches for specific terms, while vector search is better at understanding semantic meaning and handling paraphrased queries. By fusing the results of both, hybrid search leverages the strengths of each approach, leading to more robust retrieval [[38]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid), [[39]](https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/). For example, a query for "my bill keeps rolling over" would be caught by keyword search for "rollover" and by vector search for "carryover balance," ensuring comprehensive coverage.

### Re-ranking

After an initial retrieval fetches candidate documents, a re-ranker refines their order. These are often cross-encoder models that process the query and each document together for a more nuanced relevance score, ensuring the best documents are prioritized for the LLM [[43]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag), [[45]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/). However, this accuracy has a latency cost; the computational overhead of cross-encoders can make them too slow for real-time applications with strict budgets [[61]](https://medium.com/@chinmayd49/rag-production-optimizations-and-trade-offs-a623e5834e65).

### Query Transformations

Instead of using the user's query as-is, we can transform it to improve retrieval accuracy. Two common techniques are:

*   **Decomposition:** A complex, multi-part query is broken down into simpler sub-questions. The system retrieves documents for each sub-question and then merges the results. For example, "What’s our travel policy for conferences in Europe this year?" could be split into separate queries about the general travel policy, conference rules, Europe-specific guidelines, and recent updates [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html).
*   **Hypothetical Document Embeddings (HyDE):** This method involves generating a hypothetical, ideal answer to the user's query first. This "hypothetical document" is then embedded and used for the similarity search. This can bridge the gap between the phrasing of a query and the language used in the source documents [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/), [[20]](https://neo4j.com/blog/genai/advanced-rag-techniques/).

### Advanced Chunking Strategies

The way documents are split into chunks has a major impact on retrieval quality. Fixed-size chunking can awkwardly cut sentences or separate related ideas. More advanced strategies include:

*   **Semantic Chunking:** Splits text based on semantic boundaries, ensuring that complete thoughts or paragraphs are kept together.
*   **Layout-Aware Chunking:** For documents like PDFs with tables or forms, this method preserves the structural layout, keeping related data like table rows intact.
*   **Context-Enriched Chunking:** This technique adds summary or metadata to each chunk, providing extra context that can improve the quality of its embedding.

### GraphRAG

For questions about complex relationships, GraphRAG is a powerful approach. Standard RAG often fails at multi-hop reasoning because it retrieves isolated text chunks [[62]](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/). GraphRAG avoids this by constructing a knowledge graph of entities (nodes) and their relationships (edges). Instead of just vector search, the system can traverse this explicit structure to answer complex queries [[63]](https://www.gooddata.com/blog/from-rag-to-graphrag-knowledge-graphs-ontologies-and-smarter-ai/). For example, it could trace connections between deployment records, incident tickets, and service logs. However, its effectiveness depends on a complete and accurate graph; missing information can still lead to failures [[64]](https://repositum.tuwien.at/bitstream/20.500.12708/227715/1/Dolci-2026-Towards%20LLM-KG%20Symbiosis%20for%20Reducing%20Factual%20Hallucinations-vor.pdf).

```mermaid
flowchart LR
  %% Start of the Hybrid Retrieval Flow
  Query["User Query"]

  subgraph Retrieval Mechanisms
    BM25["BM25 Keyword Search"]
    Vector["Vector Similarity Search"]
  end

  subgraph Result Processing
    Union["Union / Combine Results"]
    Rerank["Re-ranking<br/>(cross-encoder model)"]
  end

  subgraph Final Output
    Context["Final Context"]
    LLM["LLM for answer generation"]
  end

  %% Flow connections
  Query -- "triggers" --> BM25
  Query -- "triggers" --> Vector

  BM25 -- "retrieved docs" --> Union
  Vector -- "retrieved docs" --> Union

  Union -- "merged docs" --> Rerank
  Rerank -- "top-ranked docs" --> Context
  Context -- "provided to" --> LLM

  %% Visual grouping
  classDef input fill:#f9f,stroke:#333,stroke-width:2px
  classDef process fill:#bbf,stroke:#333,stroke-width:2px
  classDef output fill:#bfb,stroke:#333,stroke-width:2px

  class Query input
  class BM25,Vector,Union,Rerank process
  class Context,LLM output
```
Image 3: A flowchart illustrating the Hybrid Retrieval Flow, from user query to LLM answer generation.

These techniques increase retrieval quality. Next, we will see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

As we explored in Lessons 7 and 8, a ReAct-style agent operates in a loop of Thought, Action, and Observation. Agentic RAG applies this pattern by making retrieval one of the tools available to the agent. This transforms the process into a more adaptive and intelligent system.

The core distinction lies in control flow:

*   **Standard RAG:** Follows a linear, predetermined workflow: Retrieve → Augment → Generate. It is powerful but rigid [[2]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/assets/classic-rag-pipeline.png).
*   **Agentic RAG:** An adaptive, iterative process where the agent decides when and how to retrieve information. This approach is an example of neuro-symbolic AI, combining the pattern-matching strengths of neural networks with the structured reasoning of symbolic systems [[65]](https://arxiv.org/html/2407.08516v5).

This agentic approach unlocks several new capabilities. The agent can **iteratively** use its RAG tool, refining its query based on initial findings. However, these iterative loops can increase latency and computational load, posing challenges in production [[66]](https://arxiv.org/html/2501.09136v4). The agent can also **choose** which knowledge source to search (e.g., `search_incident_runbooks` vs. `search_marketing_pages`) and **fuse** information from its RAG tool with data from other tools, like a web search, to construct a comprehensive answer [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

Consider a conceptual thought process:
*   **Thought:** User asks about '2024 EU data retention rules.' Our internal policy cites 2023; it might be outdated.
*   **Action:** `retrieve(internal_policy, query="EU data retention 2024")`
*   **Observation:** Internal policy mentions amendments but lacks detail. I need external verification.
*   **Action:** `web_search(query="Official EU data retention directive 2024")`
*   **Observation:** Found new directive. I will synthesize both.

This transforms the interaction from a simple lookup into a conversation with a research assistant. To handle more complex tasks, this can be extended to multi-agent systems where responsibilities are distributed among specialized agents, such as a planning agent, a retrieval agent, and a verification agent, who collaborate to solve the problem [[67]](https://arxiv.org/html/2501.09136v4).

```mermaid
flowchart LR
  %% Agentic RAG System - Agent's Main Loop
  A["Agent"] --> T["Thought<br/>(Reasoning Step)"]

  subgraph "Agent's Main Loop"
    T --> D{"Action<br/>(Tool Selection)"}

    subgraph "Available Tools"
      WS["Web Search"]
      CI["Code Interpreter"]
      IKB["Internal Knowledge Base<br/>(RAG Tool)"]
    end

    D -- "chooses & uses" --> WS
    D -- "chooses & uses" --> CI
    D -- "chooses & uses" --> IKB

    WS --> O["Observation<br/>(Tool Results)"]
    CI --> O
    IKB --> O

    O -- "informs next" --> T
    D -- "task completed / stop condition met" --> E["End"]
  end

  %% Visual grouping for decision node
  classDef decision stroke-dasharray:3,3
  class D decision
```
Image 4: A conceptual flowchart illustrating an Agent's Main Loop in an Agentic RAG system, emphasizing iterative decision-making and tool selection.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have seen that RAG is the industry-standard solution for overcoming the knowledge limitations of LLMs. By grounding responses in external data, it reduces hallucinations, enables customization with proprietary data, and builds user trust. For the modern AI Engineer, RAG is a foundational competency within Context Engineering.

In our next lesson, we will explore Memory for Agents and how it complements retrieval. Later, we will cover the evaluation and monitoring needed for production systems. The field continues to evolve, with ongoing research into how RAG can collaborate with long-context models and the development of new paradigms like neuro-vector-symbolic architectures [[68]](https://medium.com/@infiniflowai/from-rag-to-context-a-2025-year-end-review-of-rag-03740f1a0528), [[65]](https://arxiv.org/html/2407.08516v5).

## References

- [1] Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation (https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [2] Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop (https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [3] From Local to Global: A GraphRAG Approach to Query-Focused Summarization (https://arxiv.org/html/2404.16130)
- [4] Your RAG Is Wrong, Here's How To Fix It (https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search)
- [5] A Complete Guide to RAG (https://towardsai.net/p/l/a-complete-guide-to-rag)
- [6] Vector Databases in Practice: Building a Realistic Hybrid-Search RAG System with Qdrant (https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0)
- [7] Retrieval-Augmented Generation (RAG) Fundamentals First (https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search)
- [8] What is RAG in AI? (https://qdrant.tech/articles/what-is-rag-in-ai/)
- [9] Vector Embeddings in RAG Applications (https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5)
- [10] What is Agentic RAG (https://weaviate.io/blog/what-is-agentic-rag)
- [11] Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop (https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [12] RAG is dead, long live agentic retrieval (https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
- [13] What is agentic RAG? (https://www.ibm.com/think/topics/agentic-rag)
- [14] What Is Retrieval-Augmented Generation, aka RAG? (https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [15] Build advanced retrieval-augmented generation systems (https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
- [16] RAG System in Production: Why it Fails and How to Fix it (https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/)
- [17] The Rise of RAG (https://highlearningrate.substack.com/p/the-rise-of-rag)
- [18] Addressing AI Hallucinations with Retrieval-Augmented Generation (https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html)
- [19] Query Decomposition (https://docs.nvidia.com/rag/latest/query_decomposition.html)
- [20] Advanced RAG Techniques You Should Know in 2024 (https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [21] Retrieval-Augmented Generation: Building Grounded AI for Enterprise Knowledge (https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5)
- [22] What is RAG? (Retrieval Augmented Generation) (https://www.mindstudio.ai/blog/what-is-rag)
- [23] (https://arxiv.org/html/2312.05934v3)
- [24] RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact (https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)
- [25] (https://aclanthology.org/2024.emnlp-main.15.pdf)
- [26] RAG Architectures: An Overview of Retrieval Augmented Generation Methods (https://humanloop.com/blog/rag-architectures)
- [27] RAG and Its Different Components (https://www.aimon.ai/posts/rag_and_its_different_components/)
- [28] Grounding LLMs: Driving AI to Deliver Contextually Relevant Data (https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/)
- [29] What is retrieval-augmented generation (RAG)? (https://www.ibm.com/think/topics/retrieval-augmented-generation)
- [30] RAG Architecture: A Deep Dive into Retrieval-Augmented Generation (https://galileo.ai/blog/rag-architecture)
- [31] RAG Pipeline Deep-Dive: Ingestion (Chunking, Embedding, and Vector Search) (https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)
- [32] How RAG works (https://newsletter.systemdesign.one/p/how-rag-works)
- [33] RAGOps Guide: Building and Scaling Retrieval-Augmented Generation Systems (https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/)
- [34] Introducing Contextual Retrieval (https://www.anthropic.com/news/contextual-retrieval)
- [35] What is retrieval-augmented generation? (https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [36] SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering (https://arxiv.org/html/2601.03014v1)
- [37] Advanced RAG Retrieval: Cross-Encoders & Reranking (https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [38] Optimize RAG with Hybrid Search (https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid)
- [39] Hybrid Search Optimization: How BM25 and Dense Vector Retrieval Work Together for Superior AI Search (https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/)
- [40] Hybrid RAG in the Real World: Graphs, BM25, and the End of Black Box Retrieval (https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834)
- [41] (https://arxiv.org/html/2407.00072v5)
- [42] 10 techniques to improve the accuracy of your RAG system (https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)
- [43] Reranking Architectures in RAG (https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag)
- [44] Advanced RAG Techniques You Should Know in 2024 (https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [45] Advanced RAG Retrieval: Cross-Encoders & Reranking (https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [46] SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering (https://arxiv.org/html/2601.03014v1)
- [47] (https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf)
- [48] (https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf)
- [49] What is GraphRAG and How Does it Make LLM Answers More Accurate? (https://atlan.com/know/what-is-graphrag/)
- [50] (https://arxiv.org/html/2501.00309v2)
- [51] Implementing Semantic Search for Retrieval (https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)
- [52] How RAG Actually Works: Embeddings, Vector Databases, Indexing, & Retrieval Explained Simply (https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf)
- [53] Vector DB and RAG Pipeline for Document RAG (https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/)
- [54] RAG Explained: Understanding Embeddings, Similarity and Retrieval (https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/)
- [55] AWS Vector Databases Explained: Semantic Search and RAG Systems (https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [56] Retrieval-Augmented Generation (RAG) Explained (https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/)
- [57] Introduction to Augmenting LLMs using Retrieval Augmented Generation (RAG) (https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91)
- [58] Introduction to Augmenting LLMs using Retrieval Augmented Generation (RAG) (https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91)
- [59] Retrieval-Augmented Generation (RAG) (https://www.promptingguide.ai/research/rag)
- [60] Retrieval-Augmented Generation (RAG) — From Basics to Advanced (https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c)
- [61] RAG Production Optimizations and Trade-offs (https://medium.com/@chinmayd49/rag-production-optimizations-and-trade-offs-a623e5834e65)
- [62] How to Solve 5 Common RAG Failures with Knowledge Graphs (https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/)
- [63] From RAG to GraphRAG: Knowledge Graphs, Ontologies, and Smarter AI (https://www.gooddata.com/blog/from-rag-to-graphrag-knowledge-graphs-ontologies-and-smarter-ai/)
- [64] Towards LLM-KG Symbiosis for Reducing Factual Hallucinations (https://repositum.tuwien.at/bitstream/20.500.12708/227715/1/Dolci-2026-Towards%20LLM-KG%20Symbiosis%20for%20Reducing%20Factual%20Hallucinations-vor.pdf)
- [65] Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents (https://arxiv.org/html/2407.08516v5)
- [66] Agentic RAG: A Survey of Paradigms, Platforms, and Future Directions (https://arxiv.org/html/2501.09136v4)
- [67] Agentic RAG: A Survey of Paradigms, Platforms, and Future Directions (https://arxiv.org/html/2501.09136v4)
- [68] From RAG to Context: A 2025 Year-End Review of RAG (https://medium.com/@infiniflowai/from-rag-to-context-a-2025-year-end-review-of-rag-03740f1a0528)