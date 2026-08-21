# Lesson 9: Retrieval-Augmented Generation

In our previous lessons, we explored the foundational skills of AI Engineering. We covered Context Engineering, the art of managing information flow to an LLM, and saw how to implement ReAct agents that can reason and plan. Now, we will tackle one of the most critical components in building knowledgeable AI systems: Retrieval-Augmented Generation (RAG).

LLMs are trained on fixed datasets, which means their knowledge is static and they can't access information created after their training cutoff. They are essentially taking a "closed-book exam" on the world's information. When faced with questions about recent events or private company documents, they are prone to hallucination, confidently inventing plausible but incorrect answers. While fine-tuning can update a model, it is an expensive and inefficient way to teach it new facts, requiring constant retraining to keep knowledge current [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/).

RAG offers a more practical solution. Instead of relying only on its internal knowledge, we give the LLM an "open-book exam." We connect it to external, real-time knowledge sources, allowing it to retrieve relevant information on the fly. This is similar to how we as humans operate; we do not memorize everything but instead use manuals, notes, and search engines to find what we need. RAG is a core method AI Engineers use within the broader discipline of Context Engineering, which we introduced in Lesson 3, to build grounded and reliable applications.

In this lesson, we will explore the fundamentals of RAG, from its core components to the advanced and agentic patterns that power modern AI systems. We will also see how retrieval complements the agent memory systems we will discuss in Lesson 10.

## The RAG System: Core Components

To design effective RAG systems, you first need to understand their three conceptual pillars. This knowledge is a key part of the Context Engineering process we discussed in Lesson 3, as it helps you structure how information is found and presented to the LLM.

-   **Retrieval:** This is the engine responsible for finding relevant information. The process typically starts by converting both the user's query and the documents in your knowledge base into numerical representations called vector embeddings. These embeddings capture the semantic meaning of the text. They are stored in a specialized vector database that allows for efficient semantic similarity searches, finding the document chunks whose meanings are closest to the query's meaning [[8]](https://qdrant.tech/articles/what-is-rag-in-ai/), [[48]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf). This can be supplemented with traditional keyword-based search methods like BM25, which excel at finding exact matches [[36]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid).

-   **Augmentation:** Once the most relevant pieces of information are retrieved, they are assembled and injected into the prompt alongside the original user query [[27]](https://www.aimon.ai/posts/rag_and_its_different_components/), [[2]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/). This step "augments" the LLM's knowledge with external context, giving it the specific facts it needs to form a grounded response. The quality of this step relies on careful prompt construction to guide the model effectively.

-   **Generation:** In the final step, the LLM receives the augmented prompt. It then synthesizes the retrieved information to generate a coherent, context-aware answer. The goal is for the model to base its response on the provided data, reducing the risk of hallucination and allowing it to cite its sources, making the output verifiable and trustworthy [[26]](https://humanloop.com/blog/rag-architectures).

```mermaid
flowchart LR
  "User's Query" -- "sends" --> "Retriever"
  "Retriever" -- "passes info to" --> "Augmentation"
  "Augmentation" -- "feeds into" --> "Generator"
  "Generator" -- "produces" --> "Answer"
```
Image 1: A flowchart illustrating the conceptual flow of a RAG system's core components.

Understanding these three components is the first step. Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

An end-to-end RAG workflow is typically split into two distinct phases: an offline pipeline for preparing data and an online pipeline for answering user queries in real-time [[31]](https://newsletter.systemdesign.one/p/how-rag-works), [[32]](https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/).

### Phase 1: Offline Ingestion & Indexing

This phase prepares your knowledge base for efficient retrieval. It is an offline process that you run whenever your source documents are added or updated.

1.  **Load:** The pipeline begins by loading your documents from various sources using tools like Unstructured, LangChain document loaders, or LlamaIndex readers.
2.  **Split:** Large documents are broken down into smaller, semantically meaningful chunks using strategies like LangChain's `RecursiveCharacterTextSplitter` or LlamaIndex's `SemanticSplitter`. This is a critical step because if chunks are too large, they can contain irrelevant noise, and if they are too small, they can lack sufficient context.
3.  **Embed:** Each chunk of text is passed through an embedding model, such as OpenAI's `text-embedding-3-small`, Google's `text-embedding-004`, or open-source variants from Hugging Face, which converts it into a vector embedding.
4.  **Store:** The embeddings and their corresponding text chunks are loaded into a vector database or a search index. This can be a local solution like FAISS or a scalable, managed service like Milvus, Qdrant, Pinecone, or Azure AI Search [[6]](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0), [[30]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177/).

### Phase 2: Online Retrieval & Generation

This phase happens in real-time when a user interacts with your system.

1.  **Query:** The user submits a query, which can be managed using frameworks like a LangChain `Runnable` chain or a LlamaIndex `QueryEngine`.
2.  **Embed:** The user's query is converted into a vector embedding using the *same* embedding model from the ingestion phase. This ensures the query and document vectors exist in the same semantic space, making them comparable [[8]](https://qdrant.tech/articles/what-is-rag-in-ai/).
3.  **Search:** The query vector is used to perform a similarity search in the vector database, often using cosine similarity with tools like FAISS or applying advanced filters in services like Pinecone [[49]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).
4.  **Generate:** The retrieved chunks are combined with the original query into an augmented prompt. This prompt is then passed to an LLM to generate a final, grounded answer. As we saw in Lesson 4, you can use structured outputs to format the final answer predictably and include citations.

```mermaid
flowchart LR
  %% Offline Ingestion & Indexing Phase
  subgraph "Offline Ingestion & Indexing"
    doc["Documents"]
    load["Load"]
    split["Split"]
    embed_ingest["Embed<br/>(Embedding Model)"]
    store["Store<br/>(Vector Database/Search Index)"]

    doc -- "input" --> load
    load -- "process" --> split
    split -- "chunk & prepare" --> embed_ingest
    embed_ingest -- "create embeddings" --> store
  end

  %% Online Retrieval & Generation Phase
  subgraph "Online Retrieval & Generation"
    query["User Query"]
    embed_query["Embed<br/>(Embedding Model)"]
    search["Search<br/>(Vector Database/Search Index)"]
    generate["Generate<br/>(LLM, structured outputs & citations)"]

    query -- "input" --> embed_query
    embed_query -- "embed query" --> search
    search -- "retrieve context" --> generate
  end

  %% Cross-phase connections
  store -- "indexed data" --> search
  embed_ingest -. "uses same model" .-> embed_query

  %% Visual grouping
  classDef external fill:#f9f,stroke:#333,stroke-width:2px
  classDef process fill:#afa,stroke:#333,stroke-width:2px
  classDef storage fill:#ccf,stroke:#333,stroke-width:2px

  class doc,query external
  class load,split,embed_ingest,embed_query,search,generate process
  class store storage
```
Image 2: A detailed flowchart showing the end-to-end RAG workflow, split into two distinct phases: 'Offline Ingestion & Indexing' and 'Online Retrieval & Generation'.

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

Production systems require more sophisticated techniques to handle the complexities of real-world data and user queries. Here are some of the most effective methods for improving retrieval performance.

**Hybrid Search** combines dense (vector) retrieval with sparse (keyword-based) methods like BM25 [[37]](https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/). This allows the system to capture both semantic meaning and exact keyword matches, providing more comprehensive results [[36]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid), [[38]](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834).

**Re-ranking** introduces a second, more precise model (a cross-encoder) to re-evaluate the top candidates from the initial retrieval [[40]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag). For a product help query like "how to connect my account," a re-ranker would prioritize the official step-by-step setup guide over a tangentially related press release, improving the quality of the context passed to the LLM [[39]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/).

**Query Transformations** rewrite or expand the user's query. **Decomposition** breaks a complex question into smaller sub-queries [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html). **Hypothetical Document Embeddings (HyDE)** uses an LLM to generate a hypothetical answer first, then uses that answer's embedding for the search. For example, before searching, the system might draft an answer like: "Employees attending approved conferences in Europe can book economy flights..." and then search for documents that match that text [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/).

**Advanced Chunking Strategies** create more coherent chunks. For example, fixed-size chunking might split a "Reimbursements" section in half, separating the policy from the spending limits. **Semantic chunking** keeps the entire section together. Similarly, **layout-aware chunking** ensures a pricing table isn't split, keeping products and their prices connected [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a), [[18]](https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/).

**GraphRAG** builds a knowledge graph from documents, extracting entities and relationships [[42]](https://arxiv.org/html/2601.03014v1). It answers multi-hop questions by traversing this graph. For instance, to answer, "Which IT incidents were caused by weekend deploys that also touched the login service?" it can navigate connections between change records, deployment times, and incident tickets [[46]](https://arxiv.org/html/2501.00309v2), [[44]](https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf).

```mermaid
flowchart LR
  %% Input
  A["User Query"]

  %% Retrieval Processes
  subgraph Retrieval["Retrieval Processes"]
    B["BM25 Keyword Search"]
    C["Vector Search"]
  end

  %% Intermediate Results
  subgraph Results["Intermediate Results"]
    D["BM25 Results"]
    E["Vector Results"]
  end

  %% Combination and Refinement
  subgraph Refinement["Combination & Refinement"]
    F["Union"]
    G["Re-ranker"]
  end

  %% Final Output
  H["Final Context<br/>(for LLM)"]

  %% Connections
  A -- "triggers" --> B
  A -- "triggers" --> C

  B -- "produces" --> D
  C -- "produces" --> E

  D -- "feeds into" --> F
  E -- "feeds into" --> F

  F -- "unified results" --> G
  G -- "refined context" --> H

  %% Visual grouping
  classDef process stroke-width:2px
  classDef data stroke-dasharray:3,3

  class B,C,F,G process
  class D,E data
```
Image 3: A flowchart illustrating the hybrid retrieval flow, starting from a user query, through parallel BM25 and vector searches, result union, re-ranking, and finally generating the final context for an LLM.

These techniques significantly increase retrieval quality. Next, we will see how retrieval becomes one of many tools that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we learned about the ReAct framework, where an agent cycles through Thought, Action, and Observation to solve problems. **Agentic RAG** is the application of this principle, where retrieval is not a fixed step in a pipeline but a tool that a reasoning agent can choose to use.

The core distinction is the shift from a static workflow to a dynamic control loop [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

-   **Standard RAG** is a linear, pre-determined process: Retrieve → Augment → Generate. It is powerful but rigid.
-   **Agentic RAG** is adaptive and iterative. An agent decides *if*, *when*, and *how* to retrieve information, reasoning about its knowledge gaps and actively seeking context until it can form a confident answer.

This approach unlocks new capabilities. The agent can iteratively refine its query, choose which knowledge source to search (e.g., `search_tech_docs` vs. `search_emails`), and fuse information from its RAG tool with data from other tools like a web search [[12]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/), [[13]](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167).

This transforms RAG from a simple database lookup into a conversation with a knowledgeable research assistant who can navigate multiple sources and reconcile information.

```mermaid
flowchart LR
    %% Agent Main Loop
    Thought["Thought"] --> Decision{"Decision"}

    subgraph Actions["Possible Actions"]
        web_search["web_search"]
        code_interpreter["code_interpreter"]
        internal_knowledge_base["internal_knowledge_base<br/>(RAG tool)"]
    end

    Decision -->|"Choose"| web_search
    Decision -->|"Choose"| code_interpreter
    Decision -->|"Choose"| internal_knowledge_base

    web_search --> Observation["Observation"]
    code_interpreter --> Observation
    internal_knowledge_base --> Observation

    Observation --> Thought

    Decision -->|"Produce"| Final_Answer["Final Answer"]
```
Image 4: A conceptual flowchart showing an agent's main loop, demonstrating its ability to choose between various tools.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have covered the essentials of Retrieval-Augmented Generation, from its core components to advanced, agentic implementations. RAG is the industry's most widely adopted solution to the LLM's inherent knowledge limitations. By grounding models in external data, we can significantly reduce hallucinations and build user trust through verifiable, source-backed answers [[3]](https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html), [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/). Research consistently shows RAG is a more reliable and flexible choice for knowledge injection than fine-tuning [[4]](https://aclanthology.org/2024.emnlp-main.15.pdf), [[5]](https://arxiv.org/html/2312.05934v3).

The future of knowledge retrieval is agentic, where RAG is a dynamic tool within a broader reasoning process [[25]](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/), [[21]](https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5). For the modern AI Engineer, mastering RAG is a foundational competency and a key pillar of Context Engineering.

In our next lesson, we will explore Memory for Agents and see how memory systems work alongside retrieval to create agents that can learn and adapt.

## References

- [1] https://neo4j.com/blog/developer/fine-tuning-vs-rag/
- [2] https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/
- [3] https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html
- [4] https://aclanthology.org/2024.emnlp-main.15.pdf
- [5] https://arxiv.org/html/2312.05934v3
- [6] https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0
- [7] https://www.promptingguide.ai/research/rag
- [8] https://qdrant.tech/articles/what-is-rag-in-ai/
- [9] https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5
- [10] https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c
- [11] https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/
- [12] https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/
- [13] https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167
- [14] https://www.ibm.com/think/topics/retrieval-augmented-generation
- [15] https://www.ibm.com/think/topics/agentic-rag
- [16] https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/
- [17] https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a
- [18] https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/
- [19] https://docs.nvidia.com/rag/latest/query_decomposition.html
- [20] https://neo4j.com/blog/genai/advanced-rag-techniques/
- [21] https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5
- [22] https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search
- [23] https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search
- [24] https://weaviate.io/blog/what-is-agentic-rag
- [25] https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/
- [26] https://humanloop.com/blog/rag-architectures
- [27] https://www.aimon.ai/posts/rag_and_its_different_components/
- [28] https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/
- [29] https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval
- [30] https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177
- [31] https://newsletter.systemdesign.one/p/how-rag-works
- [32] https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/
- [33] https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation
- [34] https://aws.amazon.com/what-is/retrieval-augmented-generation/
- [35] https://www.anthropic.com/news/contextual-retrieval
- [36] https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid
- [37] https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/
- [38] https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834
- [39] https://redis.io/blog/10-techniques-to-improve-rag-accuracy/
- [40] https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag
- [41] https://arxiv.org/html/2407.00072v5
- [42] https://arxiv.org/html/2601.03014v1
- [43] https://arxiv.org/html/2404.16130
- [44] https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf
- [45] https://towardsai.net/p/l/a-complete-guide-to-rag
- [46] https://arxiv.org/html/2501.00309v2
- [47] https://highlearningrate.substack.com/p/the-rise-of-rag
- [48] https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf
- [49] https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/
- [50] https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/