# Retrieval-Augmented Generation (RAG)

In our previous lessons, we built a solid foundation in AI engineering. We explored the agent landscape, distinguished between rule-based workflows and autonomous agents, and in Lesson 3, we introduced Context Engineering. We have also covered how to give agents tools and make them reason with the ReAct framework. Now, we will dive into a key technique in an AI Engineer's toolkit.

I remember an early project where we built a chatbot to help our team navigate internal documentation. During a live demo, someone asked about a new policy launched the previous week. The chatbot, with great confidence, gave a completely wrong answer based on the old, outdated policy. Its knowledge was frozen in time, and in that moment, our promising demo failed. This is a common story. The core problem with LLMs is that they are trained on a fixed dataset. They are essentially taking a "closed-book exam" on the world's information.

This static knowledge leads to outdated answers and a tendency to "hallucinate." This means they confidently invent facts when they do not know the answer. While fine-tuning can update a model, it is slow, expensive, and quickly becomes stale. Retrieval-Augmented Generation (RAG) offers a practical and reliable solution. Instead of relying on memorized facts, we give the LLM an "open-book exam." RAG connects the model to external, up-to-date knowledge sources at the moment it needs to answer a question. This is a core method within the Context Engineering discipline we covered in Lesson 3, ensuring we provide the LLM with the most relevant and accurate context.

This lesson will walk you through the fundamentals of RAG, from its core components and pipeline architecture to the advanced and agentic patterns that power modern AI systems. We will also briefly touch on how RAG complements an agent's memory, a topic we will explore fully in Lesson 10. With the problem and motivation clear, we’ll first decompose RAG into its core components.

## The RAG System: Core Components

To design effective RAG systems, you first need to understand their three conceptual pillars. This is the first step in the Context Engineering process, as it helps you map out where each responsibility lives within your application.

**Retrieval:** This is the engine that finds relevant information. When a user asks a question, the retriever searches an external knowledge base to find the most relevant documents or data chunks. This search often relies on vector embeddings, which are numerical representations of text that capture semantic meaning. These embeddings are stored in a vector database, a specialized system designed for efficient similarity searches. This allows the system to find information that is conceptually similar to the user's query, not just matching keywords.

**Augmentation:** Once the retriever finds the relevant information, the augmentation step takes this retrieved context and combines it with the original user query. This process creates an "augmented prompt." This new prompt provides the LLM with both the question and the necessary background information to answer it accurately. The way this context is structured and presented to the model is a key part of prompt engineering within the RAG framework.

**Generation:** In the final step, the augmented prompt is sent to the LLM. The model then uses its reasoning capabilities to synthesize an answer based *only* on the information provided in the context. This ensures the generated response is grounded in the retrieved data, making it more reliable and factually accurate. A well-designed system will also enable the model to cite its sources, allowing users to verify the information. [[22]](https://www.mindstudio.ai/blog/what-is-rag/)[[51]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)

```mermaid
flowchart LR
  %% Start of the RAG system flow
  UserQuery["User Query"]

  subgraph RAGSystem["Retrieval Augmented Generation System"]
    Retriever["Retriever"]
    Augmentation["Augmentation"]
    Generator["Generator"]
  end

  LLMOutput["LLM Output"]

  %% Data flow connections
  UserQuery -- "submits" --> Retriever
  Retriever -- "retrieves context" --> Augmentation
  Augmentation -- "prepares prompt" --> Generator
  Generator -- "generates response" --> LLMOutput

  %% Visual grouping
  classDef boundary stroke-dasharray:5,5
  classDef core stroke-width:2px
  class UserQuery,LLMOutput boundary
  class Retriever,Augmentation,Generator core
```
Image 1: A flowchart illustrating the conceptual flow of a Retrieval Augmented Generation (RAG) system.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

A production-ready RAG system operates in two distinct phases: an offline phase for preparing data and an online phase for answering queries in real-time. Understanding this separation is key to building a scalable and maintainable system.

### Phase 1: Offline Ingestion & Indexing

This phase is all about preparing your knowledge base so that it can be efficiently searched. It happens before your users ever ask a question and typically runs as a batch process. The goal is to transform raw documents into a structured format that the retrieval system can understand and query quickly. [[32]](https://newsletter.systemdesign.one/p/how-rag-works)

### Load

The first step is to load your documents from their various sources. These could be PDFs, web pages, or data from APIs. Tools like Unstructured, LangChain's document loaders, or LlamaIndex's readers are commonly used for this task.

### Split

Large documents are broken down into smaller, semantically meaningful chunks. This is an important step because you want to avoid splitting a coherent idea across two different chunks. You can use rule-based splitters, like LangChain’s `RecursiveCharacterTextSplitter`, or more advanced semantic chunkers like LlamaIndex's `SemanticSplitter`.

### Embed

Each chunk is converted into a vector embedding using a specialized model. Popular choices include models from OpenAI like text-embedding-3-large/small, Google's gemini-text-embedding-004, Cohere Embed, Voyage, or open-source alternatives like BGE variants. These models transform text into numerical representations that capture its meaning. [[9]](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5)

### Store

The embeddings and their corresponding text chunks are loaded into a vector database. This database is optimized for fast similarity searches, allowing the system to quickly find the most relevant chunks for a given query. Examples include local libraries like FAISS or managed services like Milvus, Qdrant, Pinecone, Elasticsearch/OpenSearch (with kNN), and Azure AI Search. [[6]](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0)

### Phase 2: Online Retrieval & Generation

This phase happens in real-time when a user interacts with your application. It is designed to be fast and responsive, delivering accurate answers with low latency. [[31]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)

### Embed Query

The user’s question is converted into a vector embedding using the *same* model from the ingestion phase. This is essential because it ensures the query and the documents exist in the same vector space, making comparison possible.

### Search

The system uses the query vector to search the vector database, retrieving the top-k most similar document chunks. This is typically done using a similarity metric like cosine similarity, which measures the angle between two vectors to determine how close they are in meaning.

### Generate

The retrieved chunks are combined with the original query and instructions into a final prompt. This augmented prompt is then passed to an LLM, which generates an answer grounded in the provided context. As we learned in Lesson 4, using structured outputs here can help format the final answer and include citations.

```mermaid
flowchart LR
  %% Offline Ingestion & Indexing Phase
  subgraph "Offline Ingestion & Indexing"
    A["Documents<br/>(Various Sources)"]
    B["Load<br/>(e.g., Unstructured, LangChain loaders)"]
    C["Split<br/>(e.g., RecursiveCharacterTextSplitter, SemanticSplitter)"]
    D["Embed<br/>(e.g., OpenAI, Google Gemini, Cohere)"]
    E[(Store<br/>(Vector DB: FAISS, Milvus, Qdrant, Pinecone, Elasticsearch/OpenSearch))]
  end

  %% Online Retrieval & Generation Phase
  subgraph "Online Retrieval & Generation"
    F["User Query"]
    G["Embed<br/>(Same embedding model as ingestion)"]
    H["Search<br/>(Vector DB for top-k similar chunks)"]
    I["Generate<br/>(Prompt with query & chunks, LLM call, Structured outputs)"]
    J["Answer"]
  end

  %% Primary Data Flows - Ingestion
  A -- "input" --> B
  B -- "parses" --> C
  C -- "chunks" --> D
  D -- "creates embeddings" --> E

  %% Primary Data Flows - Retrieval & Generation
  F -- "submits" --> G
  G -- "embeds query" --> H
  H -- "retrieves" --> I
  I -- "generates" --> J

  %% Connection between phases
  E -- "indexed data" -.-> H

  %% Visual grouping
  classDef db_store stroke-dasharray:3,3
  class E db_store
```
Image 2: A detailed flowchart depicting the end-to-end RAG workflow, divided into two distinct phases: "Offline Ingestion & Indexing" and "Online Retrieval & Generation".

With the end-to-end path in place, the next question is quality. What advanced techniques can make retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While a basic RAG pipeline is a good start, production systems need more advanced techniques to improve retrieval quality for complex, real-world data.

### Hybrid Search

This technique combines the strengths of two different search methods: keyword-based search (like BM25) and semantic vector search. Keyword search is excellent for finding exact matches, such as product codes or specific names, while vector search is better at understanding the meaning and intent behind a query. By fusing the results of both, hybrid search ensures better coverage and precision. [[36]](https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html)

```mermaid
flowchart LR
  %% Initial Retrieval Paths
  BM25["BM25 Keyword Search Results"]
  Vector["Vector Search Results"]

  %% Combination
  Union["Union"]

  %% Processing
  ReRank["Re-rank"]

  %% Final Output
  FinalContext["Final Context for LLM"]

  %% Connections
  BM25 -- "results" --> Union
  Vector -- "results" --> Union
  Union -- "combined results" --> ReRank
  ReRank -- "re-ranked context" --> FinalContext
```
Image 3: A flowchart illustrating the hybrid retrieval flow.

### Re-ranking

Initial retrieval is optimized for speed and recall, meaning it casts a wide net to find potentially relevant documents. However, the best document might not be at the top of the initial list. Re-ranking introduces a second, more precise model to re-order this initial set of results. Cross-encoder models are often used for this, as they evaluate the relevance of a query and a document pair together, providing a more accurate score than the initial similarity search. [[42]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)

### Query Transformations

Sometimes, the user's query is not in the best format for retrieval. Query transformation techniques rewrite or expand the query to improve its chances of matching the right documents.
-   **Decomposition:** A complex question is broken down into smaller sub-questions. For example, "What’s our travel policy for conferences in Europe this year?" can be split into questions about the general policy, conference rules, Europe-specific rules, and recent changes. The system retrieves answers for each and then synthesizes a complete response. The risk is error propagation, where a mistake in an early sub-question compromises the final result. [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html)[[63]](https://apxml.com/courses/large-scale-distributed-rag/chapter-6-advanced-rag-architectures-techniques/multi-hop-iterative-rag-scale)
-   **Hypothetical Document Embeddings (HyDE):** This method generates a hypothetical, ideal answer to the user's query first. It then searches for documents that are similar to this generated answer. This often bridges the gap between the language of questions and the language of answers, but the extra LLM call adds latency and cost. [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/)[[61]](https://arxiv.org/pdf/2506.21568)[[62]](https://www.linkedin.com/posts/avi-chawla_rag-vs-hyde-visually-explained-rag-is-activity-7394672682056753153-EG6q)

### Advanced Chunking Strategies

How you split your documents has a major impact on retrieval quality. Fixed-size chunking can awkwardly cut sentences or ideas in half. For instance, splitting a handbook every 500 words might cut the "Reimbursements" section in half, separating a policy from its spending caps. Advanced strategies respect the document's structure. Semantic chunking splits text based on topical shifts, ensuring that the entire "Reimbursements" section stays together. [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a)[[64]](https://docs.cohere.com/page/chunking-strategies)[[65]](https://oneuptime.com/blog/post/2026-01-30-rag-overlap-strategies/view)

### GraphRAG

For questions about complex relationships, standard document retrieval can fall short. GraphRAG builds a knowledge graph from your data, connecting entities and their relationships. This allows the system to answer multi-hop questions that require traversing these connections, like “Which shoes get the most size-related returns and were featured in last month’s ads?” or “Which IT incidents were caused by weekend deploys that also touched the login service?” However, building and querying large knowledge graphs at scale introduces cost and performance challenges. [[46]](https://arxiv.org/html/2601.03014v1)[[66]](https://www.equitus.ai/post/knowledge-graph)

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one of several tools that an agent can choose to use as it reasons.

## Agentic RAG

So far, we have treated RAG as a linear pipeline. This is effective, but it is also rigid. What happens if the first retrieval pass fails? A standard RAG system has no way to recover. This is where agentic RAG comes in, transforming retrieval from a fixed process into an adaptive, iterative loop. As we saw in Lessons 7 and 8, Agentic RAG is essentially a ReAct-style agent with a retrieval tool. It reasons (Thought), acts (Action), and uses the results (Observation) to decide its next step.

The key distinction is the shift from a fixed workflow to an adaptive, decision-making process. The agent decides when, what, and how to retrieve information. Retrieval is just one of many tools an agent might have, like web search or code execution. But this autonomy adds risks. Agents can loop, misinterpret tool outputs, or have reasoning errors cascade. These cycles are also more expensive, requiring strict stop conditions to control costs. [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)[[67]](https://www.okta.com/identity-101/agentic-rag-architecture/)[[68]](https://arxiv.org/html/2603.07379v1)[[69]](https://www.digitalapplied.com/blog/agentic-rag-patterns-multi-step-reasoning-guide)[[70]](https://www.vellum.ai/blog/agentic-rag)

An agentic approach unlocks several capabilities:
-   **Iterative Retrieval:** If the initial search results are insufficient, the agent can refine its query and try again.
-   **Tool Selection:** The agent can choose the most appropriate knowledge source to search, such as querying incident runbooks instead of marketing pages for an IT outage.
-   **Information Fusion:** The agent can combine information from its RAG tool with outputs from other tools, like a live web search, to construct a more comprehensive answer.
-   **Knowledge Base Updates:** An agent can even decide to update the knowledge base with new information it learns. We will explore this concept of memory in more detail in the next lesson.

Here is a conceptual example of an agent's thought process:

**Thought:** The user is asking about '2024 EU data retention rules'. Our internal policy document cites 2023 regulations, which are likely outdated. I need to verify this externally.
**Action:** `retrieve(internal_policy, query="EU data retention 2024")`
**Observation:** The internal document mentions amendments but is missing specific citations for 2024.
**Thought:** I need external verification to get the current rules.
**Action:** `web_search(query="EU data retention rules 2024 official directive")`
**Observation:** The search returns a new directive update from an official source.
**Thought:** I have both the internal context and the latest external rules. I will synthesize them, highlight the changes from 2023, and cite both sources.

This turns a simple lookup into a dynamic research process, orchestrated by the agent.

```mermaid
flowchart LR
  %% Agent's Main Loop in Agentic RAG
  subgraph "Agentic RAG Main Loop"
    A["Agent (LLM)"]
    T["Thought"]
    ACT["Action"]
    OBS["Observation"]

    subgraph "Tool Use"
      WS["web_search"]
      CI["code_interpreter"]
      IKB["internal_knowledge_base (RAG tool)"]
    end

    A -- "initiates" --> T
    T -- "decides on" --> ACT
    ACT -- "selects & uses" --> WS
    ACT -- "selects & uses" --> CI
    ACT -- "selects & uses" --> IKB

    WS -- "produces" --> OBS
    CI -- "produces" --> OBS
    IKB -- "produces" --> OBS

    OBS -- "informs next" --> A
  end

  %% Visual grouping
  classDef agent stroke-width:2px
  classDef tool stroke-dasharray:3,3
  class A agent
  class WS,CI,IKB tool
```
Image 4: A conceptual flowchart illustrating an agent's main loop in Agentic RAG.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have seen that Retrieval-Augmented Generation is the most widely adopted solution to the LLM's inherent knowledge limitations. By connecting models to external data, RAG reduces hallucinations, enables customization with proprietary information, and builds user trust through verifiable, source-backed answers. For the modern AI Engineer, mastering RAG is not just a useful skill but a foundational competency and a key part of the broader discipline of Context Engineering.

The journey from a simple, naive pipeline to a sophisticated, agentic system shows the evolution of the field. Advanced techniques are crucial for production-grade quality, and the future of knowledge retrieval is increasingly agentic, where retrieval is one of many tools an intelligent system can use to reason and act.

In our next lesson, we will explore Memory for Agents, and see how short- and long-term memory stores complement the retrieval mechanisms we have discussed here. Later in the course, we will also cover how to build robust evaluation and monitoring systems to ensure your RAG pipelines are performing as expected in production.

## References

- [1] Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation (https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [2] Retrieval-Augmented Generation vs. Fine-Tuning: Enhancing LLMs (https://medium.com/@tahirbalarabe2/retrieval-augmented-generation-vs-fine-tuning-enhancing-llms-697e7a0cf7e0)
- [3] Addressing AI hallucinations with retrieval-augmented generation (https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html)
- [4] A Study on the Effectiveness of Retrieval-Augmented Generation for Knowledge-Intensive Tasks (https://aclanthology.org/2024.emnlp-main.15.pdf)
- [5] Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs (https://arxiv.org/html/2312.05934v3)
- [6] Vector Databases in Practice: Building a Realistic Hybrid-Search RAG System with Qdrant (https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0)
- [7] AWS Vector Databases Explained: Semantic Search and RAG Systems (https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [8] What is RAG in AI? (https://qdrant.tech/articles/what-is-rag-in-ai/)
- [9] Vector Embeddings in RAG Applications (https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5)
- [10] Vector Databases, RAG, and LLMs (https://samirpaulb.github.io/posts/vector-databases-rag-llm/)
- [11] Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop (https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [12] Agentic RAG vs. Traditional RAG: Key Differences & Benefits (https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/)
- [13] Agentic RAG vs Traditional RAG (https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167)
- [14] AI Agent vs RAG: What’s the Difference? (https://airbyte.com/agentic-data/ai-agent-vs-rag)
- [15] RAG vs. Agentic AI: What’s the Difference? (https://domino.ai/blog/rag-vs-agentic-ai)
- [16] Why Your RAG System Fails in Production and How to Fix It (https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/)
- [17] Improve your RAG accuracy with a simple trick (https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a)
- [18] Advanced RAG Techniques That Will Transform Your LLM Application (https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/)
- [19] Query Decomposition (https://docs.nvidia.com/rag/latest/query_decomposition.html)
- [20] Advanced RAG Techniques for High-Performance LLM Applications (https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [21] Retrieval-Augmented Generation: Building Grounded AI for Enterprise Knowledge (https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5)
- [22] What is RAG? (Retrieval-Augmented Generation) (https://www.mindstudio.ai/blog/what-is-rag/)
- [23] The Science Behind RAG: How It Reduces AI Hallucinations (https://zerogravitymarketing.com/blog/the-science-behind-rag)
- [24] How RAG Reduces AI Hallucinations and Improves Accuracy (https://www.kernshell.com/how-rag-reduces-ai-hallucinations-and-improves-accuracy/)
- [25] RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact (https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)
- [26] RAG Architectures: An Overview of 5 Common Approaches (https://humanloop.com/blog/rag-architectures)
- [27] RAG and its Different Components (https://www.aimon.ai/posts/rag_and_its_different_components/)
- [28] Grounding LLMs: Driving AI to Deliver Contextually Relevant Data (https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/)
- [29] What is retrieval-augmented generation? (https://www.ibm.com/think/topics/retrieval-augmented-generation)
- [30] RAG Architecture: A Deep Dive into Retrieval-Augmented Generation (https://galileo.ai/blog/rag-architecture)
- [31] RAG Pipeline Deep Dive: Ingestion, Chunking, Embedding, and Vector Search (https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)
- [32] RAG - A Deep Dive (https://newsletter.systemdesign.one/p/how-rag-works)
- [33] RAGOps Guide: Building and Scaling Retrieval-Augmented Generation Systems (https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/)
- [34] RAG Offline vs. Online Evaluation (https://apxml.com/courses/optimizing-rag-for-production/chapter-6-advanced-rag-evaluation-monitoring/rag-offline-online-evaluation)
- [35] What is Retrieval-Augmented Generation (RAG)? (https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [36] Hybrid Search is a Practical Necessity for Production RAG (https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html)
- [37] Hybrid Retrieval for RAG: Combining BM25 and FAISS (https://www.chitika.com/hybrid-retrieval-rag/)
- [38] Optimize RAG with Hybrid Search (https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid)
- [39] Hybrid Search Optimization: How BM25 and Dense Vector Retrieval Work Together for Superior AI Search (https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/)
- [40] Hybrid RAG in the Real World: Graphs, BM25, and the End of Black Box Retrieval (https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834)
- [41] A Survey on Retrieval-Augmented Generation for Large Language Models (https://arxiv.org/html/2407.00072v5)
- [42] 10 techniques to improve RAG accuracy (https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)
- [43] Reranking Architectures for RAG (https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag)
- [44] Advanced RAG Techniques for High-Performance LLM Applications (https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [45] Advanced RAG: Retrieval with Cross-Encoders Re-ranking (https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [46] From Local to Global: A GraphRAG Approach to Query-Focused Summarization (https://arxiv.org/html/2601.03014v1)
- [47] Graph-Based Retrieval for RAG: A Deep Dive (https://www.chitika.com/graph-based-retrieval-rag/)
- [48] From Local to Global: A GraphRAG Approach to Query-Focused Summarization (https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf)
- [49] What is GraphRAG? The Next Evolution of RAG (https://atlan.com/know/what-is-graphrag/)
- [50] Graph-based Retrieval for In-Context Learning (https://arxiv.org/html/2501.00309v2)
- [51] Implementing Semantic Search for Retrieval (https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)
- [52] How RAG Actually Works: Embeddings, Vector Databases, Indexing & Retrieval Explained Simply (https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf)
- [53] Vector DB and RAG Pipeline for Document RAG (https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/)
- [54] RAG Explained: Understanding Embeddings, Similarity, and Retrieval (https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/)
- [55] AWS Vector Databases Explained: Semantic Search and RAG Systems (https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [56] Retrieval-Augmented Generation (RAG) Explained (https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/)
- [57] Building Trustworthy RAG Systems (https://www.linkedin.com/posts/haruiz_building-trustworthy-rag-systems-with-in-activity-7310729777227669505-nd6u)
- [58] Introduction to Augmenting LLMs using Retrieval Augmented Generation (RAG) (https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91)
- [59] Retrieval-Augmented Generation (RAG) (https://www.promptingguide.ai/research/rag)
- [60] Retrieval-Augmented Generation (RAG): From Basics to Advanced (https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c)
- [61] HyDE-based RAG for Personal Knowledge Assistants (https://arxiv.org/pdf/2506.21568)
- [62] RAG vs HyDE Visually Explained (https://www.linkedin.com/posts/avi-chawla_rag-vs-hyde-visually-explained-rag-is-activity-7394672682056753153-EG6q)
- [63] Multi-Hop & Iterative RAG at Scale (https://apxml.com/courses/large-scale-distributed-rag/chapter-6-advanced-rag-architectures-techniques/multi-hop-iterative-rag-scale)
- [64] Chunking Strategies (https://docs.cohere.com/page/chunking-strategies)
- [65] RAG Overlap Strategies (https://oneuptime.com/blog/post/2026-01-30-rag-overlap-strategies/view)
- [66] Knowledge Graph (https://www.equitus.ai/post/knowledge-graph)
- [67] Agentic RAG Architecture (https://www.okta.com/identity-101/agentic-rag-architecture/)
- [68] A Survey on Large Language Model-based Autonomous Agents (https://arxiv.org/html/2603.07379v1)
- [69] Agentic RAG Patterns: A Multi-Step Reasoning Guide (https://www.digitalapplied.com/blog/agentic-rag-patterns-multi-step-reasoning-guide)
- [70] Agentic RAG (https://www.vellum.ai/blog/agentic-rag)
- [71] What Is Retrieval-Augmented Generation, aka RAG? (https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [72] A Complete Guide to RAG (https://towardsai.net/p/l/a-complete-guide-to-rag)
- [73] Retrieval-Augmented Generation (RAG) Fundamentals First (https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search)
- [74] Your RAG is wrong: Here's how to fix it (https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search)
- [75] From Local to Global: A GraphRAG Approach to Query-Focused Summarization (https://arxiv.org/html/2404.16130)
- [76] Introducing Contextual Retrieval (https://www.anthropic.com/news/contextual-retrieval)
- [77] What is Agentic RAG (https://weaviate.io/blog/what-is-agentic-rag)
- [78] RAG is dead, long live agentic retrieval (https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
- [79] What is agentic RAG? (https://www.ibm.com/think/topics/agentic-rag)
- [80] Build advanced retrieval-augmented generation systems (https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
- [81] The Rise of RAG (https://highlearningrate.substack.com/p/the-rise-of-rag)