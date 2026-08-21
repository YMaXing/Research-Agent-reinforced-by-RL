# Lesson 9: Retrieval-Augmented Generation

In our course so far, we have built a solid foundation in AI Engineering. We have explored the agent landscape, distinguished between LLM workflows and AI agents, and, in Lesson 3, covered Context Engineering—the art of managing the flow of information to an LLM. We have also given agents the ability to use tools and reason with frameworks like ReAct.

Now, we will tackle one of the most fundamental problems in applied AI: an LLM’s knowledge is frozen in time. Models are trained on a fixed dataset, which means they are essentially taking a "closed-book exam" on the world's information. This static knowledge makes them prone to hallucination and unable to access private or real-time data. While fine-tuning can teach a model new information, it is slow, expensive, and quickly becomes outdated. It is not an efficient way for models to learn continuously.

The most reliable solution is Retrieval-Augmented Generation (RAG). Instead of trying to force new knowledge into the model's weights, we give it an "open-book exam." RAG connects the LLM to external, up-to-date knowledge sources at the moment of a query. This is a core technique in Context Engineering, allowing us to precisely curate the information an LLM sees.

This lesson will guide you through the what and how of RAG, from its basic components to the advanced and agentic patterns that power modern AI systems. We will also briefly touch on how retrieval complements an agent's memory, a topic we will explore fully in Lesson 10. With the problem and motivation clear, we’ll first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of RAG is the first step in designing effective systems as part of the Context Engineering process. At its core, a RAG system is built on three conceptual pillars that work together to ground an LLM's response in external data.

**Retrieval:** This is the engine responsible for finding relevant information. When a user asks a question, the retriever searches an external knowledge base to find the most relevant data. The most common approach uses semantic similarity search, which relies on vector embeddings. Documents are broken down into chunks, and each chunk is converted into a numerical vector (an embedding) that captures its meaning. These embeddings are stored in a vector database. The user's query is also converted into an embedding, and the database finds the document chunks with the closest vectors [[51]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).

**Augmentation:** This is the process of integrating the retrieved information into the prompt that will be sent to the LLM. The original user query is combined with the relevant document chunks, providing the model with the necessary context to formulate an answer [[56]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/). This step essentially engineers the final prompt that the generator will use.

**Generation:** In the final step, the LLM receives the augmented prompt—containing both the original question and the retrieved context—and generates a response. Because the answer is based on the provided data, it is grounded, accurate, and can include citations, which builds user trust [[29]](https://www.ibm.com/think/topics/retrieval-augmented-generation).

```mermaid
flowchart LR
  %% Input
  A["User's Query"]

  %% Retrieval Phase
  subgraph Retrieval["Retrieval Phase"]
    R["Retriever"]
    KB["External Knowledge Base"]
  end

  %% Augmentation Step
  AUG["Augmentation"]

  %% Generation Phase
  subgraph Generation["Generation Phase"]
    GEN["Generator<br/>(LLM)"]
  end

  %% Output
  GA["Grounded Answer"]

  %% Primary data flows
  A -- "sends query" --> R
  R -- "accesses" --> KB
  KB -- "returns relevant info" --> R
  R -- "sends retrieved info" --> AUG
  A -- "sends original query" --> AUG
  AUG -- "formats into prompt" --> GEN
  GEN -- "produces" --> GA

  %% Visual grouping
  classDef process stroke-width:2px
  classDef store stroke-dasharray:3,3

  class R,AUG,GEN process
  class KB store
```
Image 1: A flowchart illustrating the core components and data flow of a RAG system.

These three components form a simple but powerful system. Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow is typically split into two distinct phases: an offline pipeline for data preparation and an online pipeline for real-time query answering [[32]](https://newsletter.systemdesign.one/p/how-rag-works).

### Phase 1: Offline Ingestion & Indexing

This phase prepares your knowledge base for retrieval. It is an offline process that you run whenever your source data changes.

-   **Load:** The first step is to load your documents from various sources, which could be anything from PDFs and websites to APIs [[32]](https://newsletter.systemdesign.one/p/how-rag-works).
-   **Split:** Large documents are broken down into smaller, semantically meaningful chunks. This is a critical step, as you want to avoid splitting a coherent thought or piece of information across two different chunks [[32]](https://newsletter.systemdesign.one/p/how-rag-works).
-   **Embed:** An embedding model converts each text chunk into a dense numerical vector. These vectors capture the semantic meaning of the text, allowing for searches based on concepts rather than just keywords [[52]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf).
-   **Store:** The embeddings and their corresponding text chunks, along with any metadata, are loaded into a vector database. This database is optimized for fast similarity searches, enabling efficient retrieval at query time [[8]](https://qdrant.tech/articles/what-is-rag-in-ai/).

### Phase 2: Online Retrieval & Generation

This phase is triggered in real-time when a user submits a query.

-   **Query & Embed:** The user's query is received and converted into a vector using the same embedding model from the ingestion phase. This ensures the query and the documents exist in the same vector space, making them comparable [[31]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177).
-   **Search:** The system uses the query vector to search the vector database and retrieve the top-k most similar document chunks. This is typically done using a similarity metric like cosine similarity [[54]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).
-   **Generate:** Finally, a prompt is constructed containing the original query, the retrieved chunks, and instructions for the LLM. The model then generates an answer grounded in this context. To ensure reliability, you can use structured outputs, which we covered in Lesson 4, to format the response and include citations.

```mermaid
flowchart LR
  %% Phase 1: Offline Ingestion & Indexing
  subgraph "Offline Ingestion & Indexing"
    DS["Data Sources<br/>(PDFs, Websites, APIs)"]
    Load["Load<br/>(Read Documents)"]
    Split["Split<br/>(Into Chunks)"]
    Embed["Embed<br/>(Chunks to Vectors)"]
    Store["Store<br/>(Embeddings & Text)"]
  end

  %% Shared Components
  EM["Embedding Model"]
  VD["Vector Database"]

  %% Phase 2: Online Retrieval & Generation
  subgraph "Online Retrieval & Generation"
    UQ["User Query"]
    EQ["Embed Query<br/>(Query to Vector)"]
    Search["Search<br/>(Top-k Similar Chunks)"]
    GenPrompt["Generate Prompt<br/>(Chunks, Query, Instructions)"]
    LLM["LLM<br/>(Generator)"]
    GA["Grounded Answer"]
  end

  %% Phase 1 Data Flow
  DS -- "documents" --> Load
  Load -- "documents" --> Split
  Split -- "chunks" --> Embed
  Embed -- "vectors" --> Store

  %% Phase 1 to Shared Components
  EM -. "uses" .-> Embed
  Store -- "stores" --> VD

  %% Phase 2 Data Flow
  UQ -- "query" --> EQ
  EQ -- "query vector" --> Search
  Search -- "retrieved chunks" --> GenPrompt
  UQ -- "original query" --> GenPrompt
  GenPrompt -- "prompt" --> LLM
  LLM -- "generates" --> GA

  %% Shared Components to Phase 2
  EM -. "uses" .-> EQ
  VD -- "retrieves" --> Search

  %% Visual grouping
  classDef model stroke-width:2px
  classDef store stroke-dasharray:3,3
  class EM,LLM model
  class VD store
```
Image 2: A detailed flowchart depicting the end-to-end RAG workflow, divided into two main phases: "Offline Ingestion & Indexing" and "Online Retrieval & Generation".

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

A "naive" RAG pipeline often performs well in demos but can break down in production with real-world data. To build robust systems, we need to move beyond the basics and incorporate advanced techniques that improve retrieval quality and relevance.

### Hybrid Search

This technique combines keyword-based search (like BM25) with semantic vector search. Vector search is great for understanding the meaning behind a query, but it can miss exact matches for specific terms, IDs, or acronyms. Keyword search excels at this. By running both in parallel and fusing the results, you get the best of both worlds [[36]](https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html). This allows a query for "bill rollover" to match both "rollover" (keyword) and "carryover balance" (semantic) documents.

### Re-ranking

The initial retrieval step is optimized for speed and recall, meaning it casts a wide net to find potentially relevant documents. However, the initial ranking might not be perfect. Re-ranking introduces a second, more sophisticated model, often a cross-encoder, to re-order the retrieved candidates [[43]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag). This second pass uses a more powerful model to improve the ordering of initially retrieved results, pushing the most relevant documents to the top.

```mermaid
flowchart LR
    A["User Query"]

    subgraph Retrieval
        B["BM25 (Keyword) Search"]
        C["Vector (Semantic) Search"]
    end

    D["BM25 Results"]
    E["Vector Results"]

    F["Union<br/>(Reciprocal Rank Fusion)"]
    G["Re-ranking"]
    H["Final Context<br/>for LLM"]

    A -- "triggers" --> B
    A -- "triggers" --> C

    B -- "produces" --> D
    C -- "produces" --> E

    D -- "feeds into" --> F
    E -- "feeds into" --> F

    F -- "combined results" --> G
    G -- "ranked output" --> H
```
Image 3: A flowchart illustrating the hybrid retrieval flow.

### Query Transformations

Sometimes, the user's query is not optimal for retrieval. Query transformation techniques rewrite or expand the query to improve its chances of matching relevant documents.

-   **Decomposition**: Complex questions are broken down into smaller sub-queries. For "What’s our travel policy for conferences in Europe this year?", the system might generate sub-questions about the general policy, conference definitions, Europe-specific rules, and recent changes, retrieving information for each [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html). This approach is powerful, but an error in an early sub-query can propagate through the chain and degrade the final answer [[61]](https://apxml.com/courses/large-scale-distributed-rag/chapter-6-advanced-rag-architectures-techniques/multi-hop-iterative-rag-scale).
-   **HyDE (Hypothetical Document Embeddings)**: This method generates a hypothetical, ideal answer to the query, embeds that answer, and uses the resulting vector for the search. This can improve semantic matching but adds latency and risks the hypothetical answer hallucinating, which can mislead the search [[62]](https://www.linkedin.com/posts/avi-chawla_rag-vs-hyde-visually-explained-rag-is-activity-7394672682056753153-EG6q).

### Advanced Chunking Strategies

How you split your documents can significantly impact retrieval quality. Fixed-size chunking is simple but can break up coherent ideas. Advanced methods use semantic coherence or document layouts (like tables) to create chunks, often with some overlap to ensure context is not lost at the boundaries [[63]](https://docs.cohere.com/page/chunking-strategies). For example, this keeps an entire policy section on "Reimbursements" intact, rather than cutting it in half.

### GraphRAG

This technique uses a knowledge graph to represent entities and their relationships, which is often lost in standard document chunks. A common hybrid pattern uses vector search to find a relevant starting node in the graph, then traverses its connections to gather precise, multi-hop context [[64]](https://machinelearningmastery.com/vector-databases-vs-graph-rag-for-agent-memory-when-to-use-which/). GraphRAG excels at answering complex, multi-hop questions that require connecting information across different documents or data points [[46]](https://arxiv.org/html/2601.03014v1). However, building and maintaining large-scale knowledge graphs can introduce scalability bottlenecks in data ingestion and query performance [[65]](https://www.equitus.ai/post/knowledge-graph).

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we learned about ReAct agents that can reason and take action. Agentic RAG is the application of this concept, where retrieval is not just a fixed step in a pipeline but a tool that an agent can decide to use. The agent can think (Thought), choose an Action (like retrieving information), observe the results, and iterate on this process.

It is important to clarify that agents use many tools, such as web search or code execution. The retrieval component is just one of these tools. Therefore, "agentic RAG" refers to a system where an agent dynamically uses a RAG tool as part of its reasoning loop.

The core distinction between standard and agentic RAG is this:

-   **Standard RAG** is a linear, pre-determined workflow: Retrieve → Augment → Generate. It is powerful but rigid, following the same path for every query.
-   **Agentic RAG** is adaptive and iterative. An agent decides *when* to retrieve, *what* to retrieve, and *how* to use the retrieved information. It can reformulate queries, choose between different knowledge sources, or chain multiple retrieval and reasoning steps together [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

This agentic approach unlocks several capabilities. The agent can iteratively refine its search. It can also fuse information from its RAG tool with data from other tools, like a web search, to form a comprehensive answer. It can even choose which part of its knowledge base to search (e.g., `search_emails` vs. `search_tech_docs`), sometimes acting as a router to select the best data source for a given query [[68]](https://www.ibm.com/think/topics/agentic-rag). However, it also introduces new failure modes. An agent can misinterpret tool outputs or cascade reasoning errors through a multi-step workflow [[66]](https://www.okta.com/identity-101/agentic-rag-architecture/). These iterative loops are also more expensive and can get stuck without explicit stop conditions [[67]](https://www.digitalapplied.com/blog/agentic-rag-patterns-multi-step-reasoning-guide).

For example, an agent might follow this thought process:

*   **Thought:** The user is asking about "2024 EU data retention rules." Our internal policy is from 2023 and is likely outdated.
*   **Action:** `retrieve(internal_policy, query="EU data retention 2024")`
*   **Observation:** The retrieved document mentions amendments but lacks specific citations.
*   **Thought:** I need external verification.
*   **Action:** `web_search("EU data retention 2024 official directive")`
*   **Observation:** Found the updated directive.
*   **Thought:** I will synthesize information from both sources and cite the changes from 2023.

```mermaid
flowchart LR
  %% Initial Input
  UQO["User Query / Observation"]

  %% Agent Core Loop
  subgraph Agent_Core["Agent's Main Loop"]
    AGENT["Agent<br/>(LLM)"]
    THOUGHT["Thought<br/>(Reasoning Process)"]
    ACTION["Action"]
  end

  %% Tools Subgraph
  subgraph Tools_Available["Tools"]
    WS["Web Search"]
    CI["Code Interpreter"]
    IKB["Internal Knowledge Base<br/>(RAG Tool)"]
  end

  %% Observation Feedback
  OBS["Observation<br/>(Tool/Environment Results)"]

  %% Connections
  UQO -- "receives" --> AGENT
  AGENT -- "initiates" --> THOUGHT
  THOUGHT -- "decides on" --> ACTION

  ACTION -- "utilizes" --> WS
  ACTION -- "utilizes" --> CI
  ACTION -- "utilizes" --> IKB

  WS -- "produces" --> OBS
  CI -- "produces" --> OBS
  IKB -- "produces" --> OBS

  OBS -- "feeds back" --> THOUGHT

  %% Visual Grouping
  classDef core stroke-width:2px
  classDef tool stroke-dasharray: 5 5
  class AGENT,THOUGHT,ACTION core
  class WS,CI,IKB tool
```
Image 4: A conceptual flowchart illustrating an agent's main loop, showing the iterative process from user query to thought, action, tool utilization, and observation feedback.

This transforms RAG from a simple database lookup into a dynamic conversation with a research assistant. You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have seen that RAG is the most effective solution to the fundamental knowledge limitations of LLMs. It reduces hallucinations, enables customization with proprietary data, and builds user trust through verifiable, source-backed answers. For production-grade quality, advanced techniques like hybrid search and re-ranking are essential, and the future of knowledge retrieval is agentic.

RAG is not a niche skill but a foundational competency for any AI Engineer. It is a core component of Context Engineering, allowing you to build grounded, trustworthy, and knowledgeable AI systems.

In our next lesson, we will explore Memory for Agents, and see how short- and long-term memory stores complement the external knowledge provided by RAG. Later in the course, we will also cover how to build robust evaluation and monitoring pipelines to ensure your RAG systems perform reliably in production.

## References

- [1] https://neo4j.com/blog/developer/fine-tuning-vs-rag/
- [2] https://medium.com/@tahirbalarabe2/retrieval-augmented-generation-vs-fine-tuning-enhancing-llms-697e7a0cf7e0
- [3] https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html
- [4] https://aclanthology.org/2024.emnlp-main.15.pdf
- [5] https://arxiv.org/html/2312.05934v3
- [6] https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0
- [7] https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/
- [8] https://qdrant.tech/articles/what-is-rag-in-ai/
- [9] https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5
- [10] https://samirpaulb.github.io/posts/vector-databases-rag-llm/
- [11] https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/
- [12] https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/
- [13] https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167
- [14] https://airbyte.com/agentic-data/ai-agent-vs-rag
- [15] https://domino.ai/blog/rag-vs-agentic-ai
- [16] https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/
- [17] https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a
- [18] https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/
- [19] https://docs.nvidia.com/rag/latest/query_decomposition.html
- [20] https://neo4j.com/blog/genai/advanced-rag-techniques/
- [21] https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5
- [22] https://www.mindstudio.ai/blog/what-is-rag/
- [23] https://zerogravitymarketing.com/blog/the-science-behind-rag
- [24] https://www.kernshell.com/how-rag-reduces-ai-hallucinations-and-improves-accuracy/
- [25] https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/
- [26] https://humanloop.com/blog/rag-architectures
- [27] https://www.aimon.ai/posts/rag_and_its_different_components/
- [28] https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/
- [29] https://www.ibm.com/think/topics/retrieval-augmented-generation
- [30] https://galileo.ai/blog/rag-architecture
- [31] https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177
- [32] https://newsletter.systemdesign.one/p/how-rag-works
- [33] https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/
- [34] https://apxml.com/courses/optimizing-rag-for-production/chapter-6-advanced-rag-evaluation-monitoring/rag-offline-online-evaluation
- [35] https://aws.amazon.com/what-is/retrieval-augmented-generation/
- [36] https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html
- [37] https://www.chitika.com/hybrid-retrieval-rag/
- [38] https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid
- [39] https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/
- [40] https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834
- [41] https://arxiv.org/html/2407.00072v5
- [42] https://redis.io/blog/10-techniques-to-improve-rag-accuracy/
- [43] https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag
- [44] https://neo4j.com/blog/genai/advanced-rag-techniques/
- [45] https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/
- [46] https://arxiv.org/html/2601.03014v1
- [47] https://www.chitika.com/graph-based-retrieval-rag/
- [48] https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf
- [49] https://atlan.com/know/what-is-graphrag/
- [50] https://arxiv.org/html/2501.00309v2
- [51] https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval
- [52] https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf
- [53] https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/
- [54] https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/
- [55] https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/
- [56] https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/
- [57] https://www.linkedin.com/posts/haruiz_building-trustworthy-rag-systems-with-in-activity-7310729777227669505-nd6u
- [58] https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91
- [59] https://www.promptingguide.ai/research/rag
- [60] https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c
- [61] https://apxml.com/courses/large-scale-distributed-rag/chapter-6-advanced-rag-architectures-techniques/multi-hop-iterative-rag-scale
- [62] https://www.linkedin.com/posts/avi-chawla_rag-vs-hyde-visually-explained-rag-is-activity-7394672682056753153-EG6q
- [63] https://docs.cohere.com/page/chunking-strategies
- [64] https://machinelearningmastery.com/vector-databases-vs-graph-rag-for-agent-memory-when-to-use-which/
- [65] https://www.equitus.ai/post/knowledge-graph
- [66] https://www.okta.com/identity-101/agentic-rag-architecture/
- [67] https://www.digitalapplied.com/blog/agentic-rag-patterns-multi-step-reasoning-guide
- [68] https://www.ibm.com/think/topics/agentic-rag