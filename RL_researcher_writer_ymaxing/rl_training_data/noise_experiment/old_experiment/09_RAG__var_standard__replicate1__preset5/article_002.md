# Lesson 9: Retrieval-Augmented Generation (RAG)

## Introduction: Giving LLMs an Open-Book Exam

In our previous lessons, we explored the core principles of AI Engineering. We covered Context Engineering in Lesson 3, where we learned the importance of carefully curating the information we provide to an LLM. We also built a reasoning agent from scratch in Lesson 8, using the ReAct framework to give our models the ability to plan and execute actions.

A core problem remains: LLMs are trained on a fixed dataset, making their knowledge static. During training, they essentially take a "closed-book exam" on the world's information. We do not yet have efficient techniques to enable models to learn new information over time after deployment. While we can fine-tune them, this process is slow, expensive, and often struggles to teach the model new facts [[4]](https://aclanthology.org/2024.emnlp-main.15.pdf). Fine-tuning requires creating large, high-quality datasets and involves significant computational cost. Even then, it does not guarantee the model will internalize new knowledge, and the entire process must be repeated every time the information needs an update. This approach is like trying to memorize an entire library instead of just learning how to use the search index. The ultimate goal is to enable models to learn from experience over time, but we are not there yet.

This limitation leads to two major issues: knowledge cutoffs and hallucinations. A model trained up to October 2023 cannot tell you who won the 2024 NBA MVP, and if pressed, it might confidently invent an answer [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/).

Retrieval-Augmented Generation (RAG) is a reliable solution to this problem. Instead of trying to force new knowledge into the model's weights, we insert it into the context window at inference time. With RAG, we are giving the LLM an "open-book exam" by connecting it to external, real-time knowledge sources. Just as humans do not need to memorize everything, LLMs can use manuals, cheat sheets, and external documents to ground their answers in facts [[35]](https://aws.amazon.com/what-is/retrieval-augmented-generation/).

This concept of using external information is not new. It builds on decades of research in information retrieval from pre-LLM search engines. These early systems also aimed to find relevant documents in response to a query, but they relied on keyword matching and statistical methods [[81]](https://labelstud.io/blog/rag-fundamentals-challenges-and-advanced-techniques/). RAG modernizes this approach by integrating the powerful semantic understanding of LLMs, allowing for searches based on meaning rather than just keywords [[82]](https://ijcaonline.org/archives/volume187/number18/veluru-2025-ijca-925279.pdf).

RAG is a key method AI Engineers use in the process of Context Engineering. It allows us to dynamically provide the most relevant information to the LLM, ensuring that its responses are accurate, up-to-date, and trustworthy. In this lesson, we will explore the "what" and "how" of RAG, starting with its basic components and moving toward the advanced and agentic patterns that power modern AI systems. We will also contrast retrieval with agent memory, a topic we will explore further in Lesson 10, where we discuss short- and long-term memory stores that complement RAG.

With the problem and motivation clear, we will first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of RAG is the first step in the Context Engineering process of designing effective retrieval systems. At its core, RAG is built on three conceptual pillars: Retrieval, Augmentation, and Generation.

**Retrieval** is the engine for finding relevant information. Given a user's query, the retriever's job is to search an external knowledge base and pull out the most relevant pieces of data. The most common approach is semantic similarity search, which relies on vector embeddings. An embedding is a numerical representation of a piece of text that captures its meaning. To create one, text is passed through an embedding model, which transforms it into a dense vector where each dimension represents some aspect of the content’s meaning [[7]](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/). These vectors are stored in a specialized vector database, which allows for efficient searching. When a user asks a question, it is also converted into a vector, and the database finds the text chunks with the closest vectors using distance metrics like cosine similarity [[55]](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/). Another popular method is keyword-based search, using algorithms like BM25, which excels at finding exact matches for specific terms.

**Augmentation** is the process of taking the information found by the retriever and preparing it for the LLM. This involves formatting the retrieved text chunks and combining them with the original user query to create an augmented prompt [[56]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/). This new prompt provides the LLM with the necessary context to formulate an accurate and grounded response. The goal is to ensure the model gives weight to the retrieved context and respects constraints, such as not inventing information beyond what is provided [[56]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/).

**Generation** is the final step. The augmented prompt is sent to the LLM, which uses the provided context as its source of truth. The model synthesizes the information from the retrieved chunks to generate a final answer that directly addresses the user's query while being grounded in the external data [[28]](https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/). This process ensures the output is informed by relevant, up-to-date knowledge rather than relying solely on the model's pre-trained information [[30]](https://galileo.ai/blog/rag-architecture).

This approach has parallels to Case-Based Reasoning (CBR), a classic AI technique. While RAG retrieves general knowledge statements (semantic memory), CBR retrieves specific past examples or "cases" (episodic memory) to solve new problems. Both methods ground reasoning in existing data, but RAG focuses on factual knowledge while CBR leverages experiential precedents [[61]](https://ceur-ws.org/Vol-3708/paper_21.pdf).

```mermaid
flowchart LR
  %% Input
  subgraph Input
    UQ["User Query"]
  end

  %% Retrieval and Context Building
  subgraph "Retrieval & Augmentation"
    R["Retriever"]
    A["Augmentation"]
  end

  %% Generation
  subgraph Generation
    G["Generator<br/>(Large Language Model)"]
  end

  %% Output
  subgraph Output
    GA["Grounded Answer"]
  end

  %% Primary data flows
  UQ -- "submits" --> R
  R -- "retrieves info" --> A
  UQ -- "provides context" --> A
  A -- "creates prompt" --> G
  G -- "generates" --> GA
```

Image 1: A flowchart illustrating the core components and conceptual flow of a Retrieval Augmented Generation (RAG) system.

These three pillars work together to create a system that can answer questions about information it was never trained on. Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

An end-to-end RAG workflow is split into two distinct phases: an offline phase for preparing the data and an online phase for answering user queries in real-time [[32]](https://newsletter.systemdesign.one/p/how-rag-works). This separation allows the computationally intensive work of data processing to happen once, while the retrieval process remains fast and responsive for the user.

### Phase 1: Offline Ingestion & Indexing

This phase happens in the background, before any user interacts with the system. Its goal is to take a collection of raw documents and prepare them for efficient retrieval. This process involves several steps:

-   **Load:** The first step is to read documents from their various sources. These can be PDFs, websites, database records, or API responses. Tools like Unstructured, LangChain's document loaders, or LlamaIndex's readers are commonly used for this task, providing connectors to ingest data from almost anywhere [[54]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).
-   **Split:** Since documents are often too large to fit into an LLM's context window, they must be broken down into smaller, meaningful pieces, or "chunks." This is a critical step, as the quality of the chunks directly impacts retrieval accuracy. You can use simple rule-based splitters like LangChain's `RecursiveCharacterTextSplitter` or more advanced methods like LlamaIndex's `SemanticSplitter` that try to keep related ideas together [[32]](https://newsletter.systemdesign.one/p/how-rag-works).
-   **Embed:** Each chunk of text is then passed through an embedding model, which converts it into a vector embedding. This numerical representation captures the semantic meaning of the text. Popular embedding models include OpenAI's `text-embedding-3-large/small`, Google's `gemini-text-embedding-004`, Cohere's `Embed`, Voyage models, and various open-source `bge` variants from Hugging Face [[53]](https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/).
-   **Store:** Finally, the embeddings and their corresponding text chunks are loaded into a vector database. This database indexes the vectors for fast similarity search, allowing the system to quickly find the most relevant chunks for a given query. Options range from local libraries like FAISS for quick prototyping to scalable, production-grade databases like Milvus, Qdrant, Pinecone, or vector-enabled indexes in Elasticsearch, OpenSearch, and Azure AI Search [[52]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf).

### Phase 2: Online Retrieval & Generation

This phase is triggered in real-time when a user submits a query.

-   **Query & Embed:** The user's question is taken as input and converted into a vector using the same embedding model that was used during the ingestion phase. This ensures that the query and the document chunks are represented in the same vector space, making them comparable. This step can be managed within a framework like LangChain's `Runnable` chains or LlamaIndex's `QueryEngine` [[31]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177).
-   **Search:** The query vector is used to search the vector database. The database performs a similarity search (often using cosine similarity with an Approximate Nearest Neighbor algorithm for speed) to find the top-k document chunks whose embeddings are most similar to the query's embedding [[51]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).
-   **Generate:** The retrieved chunks are combined with the original user query and a set of instructions into a single prompt. This augmented prompt is then passed to an LLM, which generates a final answer grounded in the retrieved context. To ensure reliability, we often use structured outputs, a technique we covered in Lesson 4, to format the answer and include citations back to the source documents [[29]](https://www.ibm.com/think/topics/retrieval-augmented-generation).

```mermaid
flowchart LR
  %% Phase 1: Offline Ingestion & Indexing
  subgraph "Offline Ingestion & Indexing"
    RD["Raw Documents"]
    L["Load"]
    S["Split"]
    E["Embed<br/>(Embedding Model)"]
    ST[(Store<br/>(Vector Database))]
  end

  RD -- "read" --> L
  L -- "chunk" --> S
  S -- "vectorize" --> E
  E -- "index" --> ST

  %% Phase 2: Online Retrieval & Generation
  subgraph "Online Retrieval & Generation"
    UQ["User Query"]
    EQ["Embed Query<br/>(Embedding Model)"]
    SR["Search<br/>(Vector Database)"]
    G["Generate<br/>(LLM)"]
  end

  UQ -- "input" --> EQ
  EQ -- "query vectors" --> SR
  SR -- "retrieved chunks" --> G

  %% Connection between phases
  ST -. "provides indexed data" .-> SR

  %% Visual grouping
  classDef store stroke-dasharray:3,3
  classDef process stroke-width:2px

  class L,S,E,EQ,SR,G process
  class ST store
```

Image 2: A detailed flowchart depicting the two distinct phases of an end-to-end RAG pipeline: Offline Ingestion & Indexing and Online Retrieval & Generation.

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While a basic RAG pipeline works for simple lookups, production systems require more sophisticated techniques to handle the complexity of real-world data and user queries. These advanced methods significantly improve the quality and relevance of the retrieved information.

### Hybrid Search

Hybrid search combines the strengths of keyword-based search and semantic vector search. **BM25** is a popular keyword-based algorithm that ranks documents based on term frequency and inverse document frequency, making it excellent for finding exact matches of specific terms, acronyms, or IDs that vector search might miss [[38]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid). Vector search, on the other hand, excels at understanding the meaning and context behind a query, catching paraphrases and related concepts.

For example, if a customer support user asks, "my bill keeps rolling over," a keyword search will find articles containing the exact word "rollover." A semantic search might also surface guides about "carryover balances." By combining both, the system covers different wordings of the same issue. The results from both search methods are typically merged using a technique like **Reciprocal Rank Fusion (RRF)**, which combines ranked lists from different systems without needing to normalize their scores [[39]](https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/).

### Re-ranking

After an initial retrieval fetches a set of candidate documents, a re-ranker is used to improve their ordering. Re-rankers are typically cross-encoder models that evaluate the relevance of a query and a document pair together, providing a more accurate relevance score than the initial retrieval stage [[43]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag). This is different from the initial retrieval, which often uses a bi-encoder that encodes the query and document independently. A cross-encoder concatenates the query and document, allowing its attention mechanism to model the interactions between their tokens directly, which yields a much more precise relevance judgment [[62]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/).

The initial retrieval is optimized for speed and recall, bringing back a broad set of potentially relevant documents. The re-ranker, which is more computationally intensive, then focuses on precision, analyzing this smaller set to push the most relevant documents to the top. This two-stage process is necessary because running a cross-encoder on every document would be too slow. However, under high query load, even re-ranking a small set can become a bottleneck, as response times can increase dramatically when the query rate exceeds the system's throughput [[62]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/). For instance, when a user asks, "how to connect my account," a re-ranker can prioritize a step-by-step setup guide over a press release or a tangentially related community forum thread [[42]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/).

```mermaid
flowchart LR
  A["User Query"] --> B["BM25 Search"]
  A["User Query"] --> C["Vector Search"]
  B["BM25 Search"] --> D["Union"]
  C["Vector Search"] --> D["Union"]
  D["Union"] --> E["Re-ranker"]
  E["Re-ranker"] --> F["Final Context"]
```

Image 3: A flowchart illustrating the Hybrid Retrieval Flow with re-ranking.

### Query Transformations

Sometimes, the user's original query is not the best one for searching the knowledge base. Query transformation techniques rewrite or expand the query to improve retrieval results.

-   **Decomposition:** This technique breaks down a complex, multi-part question into several simpler sub-questions. The system then retrieves documents for each sub-question and merges the results. For example, the query "What’s our travel policy for conferences in Europe this year?" could be decomposed into: "What is the travel policy?", "What are the rules for conferences?", "What are the specific rules for Europe?", and "What has changed this year?" [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html). However, perfect decomposition is an open problem, as it requires handling complex logical operators and ambiguity [[63]](https://arxiv.org/html/2510.18633v1).
-   **Hypothetical Document Embeddings (HyDE):** With HyDE, the system first generates a hypothetical, ideal answer to the user's query. It then embeds this hypothetical document and uses the resulting vector to search the knowledge base. This often bridges the gap between the phrasing of the query and the language used in the documents. For a query about travel policies, the system might generate a draft answer like, "Employees can book economy flights and up to three hotel nights," and then search for documents that sound like that answer [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/). This approach has limits, as the generated answer can contain factual inaccuracies, potentially leading the retrieval astray [[64]](https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1/).

### Advanced Chunking Strategies

How documents are split into chunks has a major impact on retrieval quality. Moving beyond simple fixed-size chunks can preserve critical context.

-   **Semantic Chunking:** Instead of splitting by a fixed number of characters, semantic chunking groups related sentences together, ensuring that a complete idea or topic is contained within a single chunk. For example, when splitting a company handbook, this method would keep the entire "Reimbursements" section intact, rather than cutting it in half and separating the rules from the specific cap amounts [[18]](https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/).
-   **Layout-Aware Chunking:** For documents with complex structures like tables, forms, or financial reports, layout-aware chunking preserves the document's hierarchy. For a pricing table, this means keeping each row (product, price, discount) together, which would be lost with a naive character-based split [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a).
-   **Context-Enriched Chunking:** This approach, also known as contextual retrieval, adds a summary of the parent document's context to each chunk before embedding. This helps the retrieval system understand the chunk's relevance even if the chunk itself is ambiguous.

The optimal strategy is not universal; it depends on the document type and the kinds of questions users ask. The best approach is often a decision framework that applies different chunking rules to different documents rather than a single, one-size-fits-all method [[65]](https://www.llamaindex.ai/glossary/document-chunking-strategies).

### GraphRAG

GraphRAG introduces retrieval from knowledge graphs, which represent information as entities (nodes) and relationships (edges). This technique excels at answering questions about complex, multi-hop relationships that are often lost in standard document chunks. It is ideal for situations where understanding the connections between data points is critical [[46]](https://arxiv.org/html/2601.03014v1). For enterprise documents with deep hierarchies and cross-references, standard RAG can fail by retrieving semantically similar but outdated or irrelevant clauses. GraphRAG can traverse explicit references, respecting temporal precedence and contextual links [[66]](https://arxiv.org/html/2604.14220v1).

For example, to answer a retail query like, "Which shoes get the most size-related returns and were featured in last month’s ads?", a GraphRAG system can traverse the graph: from `returns` to `reason: sizing`, to specific `shoe SKUs`, to the `marketing calendar`. This allows it to assemble a precise context that a simple vector search would likely miss [[50]](https://arxiv.org/html/2501.00309v2). Similarly, for an IT operations query like, "Which incidents were caused by weekend deploys that also touched the login service?", the system can link `change records` to `deploy time`, to the affected `login service`, and finally to the relevant `incident tickets`, surfacing the exact write-ups needed.

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored the ReAct framework, where an agent cycles through Thought, Action, and Observation to solve problems. Agentic RAG is the application of this principle, where retrieval is not a fixed step in a pipeline but a tool that a reasoning agent can choose to use. It is important to clarify that while we often use the term "agentic RAG," this can be a narrow view. An agent typically has access to many tools, such as web search, code execution, and database queries. The retrieval mechanism is just one of these tools, so it is more accurate to think of the system as an agent equipped with a RAG tool, rather than an "agentic RAG system" [[14]](https://airbyte.com/agentic-data/ai-agent-vs-rag).

The core distinction between standard and agentic RAG is the shift from a linear workflow to an adaptive, iterative loop.

-   **Standard RAG** is a rigid, pre-determined process: every query follows the same path of Retrieve → Augment → Generate. It is powerful but inflexible. If the initial retrieval fails, the entire system fails [[12]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/).
-   **Agentic RAG** is dynamic. The agent decides *when* to retrieve, *what* to retrieve, and *whether* to retrieve again. It can reformulate queries, choose between different knowledge sources, and chain multiple retrieval and reasoning steps to arrive at a comprehensive answer [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

This agentic approach unlocks several new capabilities. The agent can iteratively use the RAG tool, refining its query based on initial findings. For example, if a first pass on a policy document is too vague, the agent can narrow its scope ("show me updates for EU customers in 2024") and retrieve again. It can also choose which knowledge base to search, such as `search_incident_runbooks` for an outage query instead of `search_marketing_pages` [[13]](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167).

Here is a conceptual example of an agent's thought process:
*   **Thought:** User asks about ‘2024 EU data retention rules’. The internal policy is from 2023 and likely outdated.
*   **Action:** `retrieve(internal_policy, query=“EU data retention 2024”)`
*   **Observation:** Mentions amendments but no citations.
*   **Thought:** Need external verification.
*   **Action:** `web_search(“EU data retention 2024 official”)`
*   **Observation:** Finds an updated directive.
*   **Thought:** Synthesize and cite both sources, highlighting changes.

This transforms RAG from a simple database lookup into a conversation with a knowledgeable research assistant.

```mermaid
flowchart LR
  %% Agent Main Loop
  subgraph "Agent Main Loop"
    A["Agent"]
    T["Thought"]
    ACT["Action"]
    O["Observation"]
  end

  %% Available Tools
  subgraph "Tools"
    WS["web_search"]
    CI["code_interpreter"]
    IKB["internal_knowledge_base<br/>(RAG retrieval tool)"]
  end

  %% Flow connections
  A -- "initiates" --> T
  T -- "decides on" --> ACT
  ACT -- "utilizes" --> WS
  ACT -- "utilizes" --> CI
  ACT -- "utilizes" --> IKB

  WS -- "produces" --> O
  CI -- "produces" --> O
  IKB -- "produces" --> O

  O -- "informs & refines" --> T
```

Image 4: A conceptual flowchart illustrating an agent's main loop in an Agentic RAG system, inspired by the ReAct framework.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

In this lesson, we have journeyed from the fundamentals of RAG to its advanced and agentic implementations. We have seen that RAG is the most widely used solution to the LLM knowledge problem, that advanced techniques are essential for production-grade quality, and that the future of knowledge retrieval is agentic. By grounding LLMs in external data, RAG reduces hallucinations, enables customization with proprietary information, and builds user trust through verifiable, source-based answers.

RAG is not a niche skill but a foundational competency for the modern AI Engineer and a core part of Context Engineering. It is the bridge that connects the vast reasoning capabilities of LLMs to the world of factual, dynamic information. As you build more complex AI systems, mastering these retrieval techniques will be essential for creating applications that are not only intelligent but also reliable and trustworthy.

In our next lesson, we will explore Memory for Agents, and see how short-term and long-term memory systems complement retrieval to create even more powerful and stateful AI applications. The field is also moving towards multimodal RAG, where systems will retrieve information not just from text but also from images, tables, and diagrams using unified multimodal embeddings, a topic we will cover in Lesson 11. We will also touch on other important topics like retrieval quality evaluation and production monitoring later in the course.

## References

- [1] [Fine-Tuning vs. Retrieval Augmented Generation for LLMs](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [4] [Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs](https://aclanthology.org/2024.emnlp-main.15.pdf)
- [7] [AWS Vector Databases Explained: Semantic Search and RAG Systems](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [11] [Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [12] [Agentic RAG vs. Traditional RAG: Key Differences & Benefits](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/)
- [13] [Agentic RAG vs Traditional RAG](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167)
- [14] [AI Agent vs RAG: What’s the Difference?](https://airbyte.com/agentic-data/ai-agent-vs-rag)
- [16] [RAG System in Production: Why It Fails and How to Fix It](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/)
- [17] [Improve your RAG accuracy with a few simple techniques](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a)
- [18] [Advanced RAG Techniques That Will Transform Your LLM Application](https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/)
- [19] [Query Decomposition](https://docs.nvidia.com/rag/latest/query_decomposition.html)
- [28] [Grounding LLMs: Driving AI to Deliver Contextually Relevant Data](https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/)
- [29] [What is retrieval-augmented generation?](https://www.ibm.com/think/topics/retrieval-augmented-generation)
- [30] [RAG Architecture: An Overview of Retrieval Augmented Generation](https://galileo.ai/blog/rag-architecture)
- [31] [RAG Pipeline Deep-Dive: Ingestion (Chunking, Embedding) and Vector Search](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)
- [32] [How RAG Works](https://newsletter.systemdesign.one/p/how-rag-works)
- [35] [What is Retrieval-Augmented Generation?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [38] [Optimize RAG with Hybrid Search](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid)
- [39] [Hybrid Search Optimization: How BM25 and Dense Vector Retrieval Work Together for Superior AI Search](https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/)
- [42] [10 Techniques to Improve RAG Accuracy](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)
- [43] [Reranking Architectures for RAG](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag)
- [46] [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/html/2601.03014v1)
- [50] [Graph-based Retrieval for Question Answering](https://arxiv.org/html/2501.00309v2)
- [51] [Implementing Semantic Search for Retrieval](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)
- [52] [How RAG Actually Works: Embeddings, Vector Databases, Indexing & Retrieval Explained Simply](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf)
- [53] [Vector DB and RAG Pipeline for Document RAG](https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/)
- [54] [RAG Explained: Understanding Embeddings, Similarity, and Retrieval](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/)
- [55] [AWS Vector Databases Explained: Semantic Search and RAG Systems](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [56] [Retrieval-Augmented Generation (RAG) Explained](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/)
- [61] [CBR-TPI: A Case-Based Reasoning Framework for Generating Explanations for Trustworthy Plan-ning](https://ceur-ws.org/Vol-3708/paper_21.pdf)
- [62] [Advanced RAG Retrieval: Cross-Encoders & Reranking](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [63] [BanditRAG: A Bandit-based Approach to Complex Question Answering with Large Language Models](https://arxiv.org/html/2510.18633v1)
- [64] [Advanced Query Transformations to Improve RAG](https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1/)
- [65] [Document Chunking Strategies](https://www.llamaindex.ai/glossary/document-chunking-strategies)
- [66] [Graph-based RAG: A Novel Approach to Mitigate Temporal Hallucinations in Large Language Models](https://arxiv.org/html/2604.14220v1)
- [67] [Agentic RAG Failure Modes: Retrieval Thrash, Tool Storms, and Context Bloat (and How to Spot Them Early)](https://towardsdatascience.com/agentic-rag-failure-modes-retrieval-thrash-tool-storms-and-context-bloat-and-how-to-spot-them-early/)
- [68] [Agentic RAG: How enterprises are surmounting the limits of traditional RAG](https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/)
- [81] [RAG Fundamentals, Challenges, and Advanced Techniques](https://labelstud.io/blog/rag-fundamentals-challenges-and-advanced-techniques/)
- [82] [Next-Generation Search Engines: A Survey of the State-of-the-Art and the Future of Information Retrieval](https://ijcaonline.org/archives/volume187/number18/veluru-2025-ijca-925279.pdf)
</article>