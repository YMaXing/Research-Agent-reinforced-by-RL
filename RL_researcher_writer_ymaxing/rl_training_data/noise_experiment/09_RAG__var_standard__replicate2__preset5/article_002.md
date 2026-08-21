# Retrieval Augmented Generation (RAG): Giving LLMs an Open-Book Exam

In our previous lessons, we built a foundation in AI Engineering. We explored the agent landscape, distinguished between rule-based workflows and autonomous agents, and, in Lesson 3, introduced Context Engineering—the discipline of managing the information an LLM sees. We have learned how to build agents that reason and act. Now, we will tackle one of their biggest limitations: their fixed knowledge.

I remember an early project where we built a customer support chatbot for an e-commerce client. In the demo, it worked perfectly, answering questions about products and policies. But a week after launch, we got a flood of complaints. A major product line had been updated, but the chatbot, trained on the old documentation, kept giving out outdated information. It confidently told customers about features that no longer existed and prices that were incorrect. The model was taking a "closed-book exam" on our company's knowledge, and it was failing spectacularly.

This experience highlights a fundamental problem with LLMs: their knowledge is static, frozen at the time of their training. This leads to two critical failures. First, they have a knowledge cutoff date and are unaware of any new information, like an updated product line or the winner of the 2024 NBA MVP [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/). Second, when they do not know an answer, they are prone to making things up, a phenomenon known as hallucination. An LLM might confidently invent a fake Wikidata ID or even fabricate legal case citations, creating a significant reliability crisis [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/), [[55]](https://highlearningrate.substack.com/p/the-rise-of-rag).

While we could fine-tune a model with new data, this process is slow, expensive, and often ineffective for knowledge that changes frequently. Research shows that LLMs struggle to learn new facts via fine-tuning, and it often requires exposing them to numerous variations of the same fact to see even limited gains [[4]](https://aclanthology.org/2024.emnlp-main.15.pdf). We do not yet have techniques that allow models to continuously learn from experience after deployment.

Retrieval-Augmented Generation (RAG) provides a reliable solution to this problem. It gives the LLM an "open-book exam" by connecting it to external, real-time knowledge sources. Just as humans do not need to memorize everything and can instead rely on manuals or cheat sheets, we can equip LLMs with a similar capability. RAG is a core technique in Context Engineering, allowing us to precisely curate the information an LLM uses to answer a question. By grounding the model in verifiable data, RAG makes responses more accurate, trustworthy, and up-to-date [[33]](https://aws.amazon.com/what-is/retrieval-augmented-generation/).

This lesson will guide you through the "what" and "how" of RAG, starting with its basic components and moving toward the advanced and agentic patterns used in production systems. We will also preview how retrieval complements an agent's memory, a topic we will explore fully in Lesson 10. With the problem and motivation clear, we’ll first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of RAG is the first step in the Context Engineering process of designing an effective system. At its core, RAG can be broken down into three conceptual pillars that work together to ground an LLM's response in external data.

```mermaid
flowchart LR
  UserQuery["User's Query"]
  Retriever["Retriever"]
  Augmentation["Augmentation"]
  Generator["Generator (LLM)"]

  UserQuery -- "sends" --> Retriever
  Retriever -- "retrieves context" --> Augmentation
  Augmentation -- "prepares prompt" --> Generator
  Generator -- "produces" --> Answer["Answer"]
```
Image 1: A flowchart illustrating the core components and sequential flow of a RAG system.

**Retrieval:** This is the engine responsible for finding relevant information. When a user asks a question, the retriever searches an external knowledge base to find documents or data snippets that are most likely to contain the answer. The most common approach is semantic similarity search, which relies on vector embeddings. Text is converted into numerical vectors that capture its meaning, and these vectors are stored in a specialized vector database. The user's query is also converted into a vector, and the database finds the vectors (and their corresponding text) that are closest in this high-dimensional space. This "closeness" is typically measured using distance metrics like cosine similarity, which quantifies how similar two vectors are in direction. Another popular method is keyword-based search, using algorithms like BM25, which excels at finding exact matches for specific terms [[47]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf), [[34]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid), [[49]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).

**Augmentation:** Once the retriever has found the relevant information, the augmentation step begins. This process involves taking the retrieved text chunks and integrating them into the prompt that will be sent to the LLM. The prompt is carefully constructed using a template that combines the original user query with the retrieved context. This effectively gives the model the "open-book" materials it needs to formulate an answer. Good prompt engineering is essential here to ensure the model understands that it should prioritize the provided context over its internal knowledge. For example, you can add instructions like, "Using the context above, answer the question. If the context does not contain the answer, say so." This guides the model to stick to the provided facts [[51]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/), [[27]](https://www.ibm.com/think/topics/retrieval-augmented-generation).

**Generation:** This is the final step, where the LLM receives the augmented prompt and generates a response. Instead of relying solely on its pre-trained knowledge, the model synthesizes an answer that is grounded in the retrieved data. This ensures the response is more accurate, up-to-date, and relevant to the specific context of the query. For added trust and verifiability, the generated answer can also include citations that point back to the original source documents, allowing users to validate the information themselves. This grounding mechanism is what makes RAG a powerful tool for reducing hallucinations and building trustworthy AI applications [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/), [[22]](https://www.mindstudio.ai/blog/what-is-rag/).

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow is divided into two distinct phases: an offline phase for preparing the data and an online phase for answering user queries in real-time. This separation allows for the computationally intensive work of processing and indexing documents to be done ahead of time, ensuring that the user-facing retrieval process is fast and efficient.

```mermaid
flowchart LR
  %% Shared Components
  EmbedModel["Embedding Model"]
  VectorDB["Vector Database"]
  LLM["LLM"]

  %% Offline Ingestion & Indexing Phase
  subgraph "Offline Ingestion & Indexing"
    A["Documents<br/>(Various Sources)"]
    B["Load"]
    C["Split"]
    D["Embed Chunks"]
    E["Store"]

    A -- "read" --> B
    B -- "process" --> C
    C -- "chunks" --> D
    D -- "generates embeddings" --> E
  end

  %% Connections from Offline phase to shared components
  D -- "uses" --> EmbedModel
  E -- "stores into" --> VectorDB

  %% Online Retrieval & Generation Phase
  subgraph "Online Retrieval & Generation"
    F["User Query"]
    G["Embed Query"]
    H["Search"]
    I["Generate"]
    J["Grounded Answer"]

    F -- "asks" --> G
    G -- "generates query embedding" --> H
    H -- "retrieves chunks" --> I
  end

  %% Connections from Online phase to shared components
  G -- "uses" --> EmbedModel
  H -- "queries" --> VectorDB
  I -- "builds prompt & calls" --> LLM
  LLM -- "produces" --> J
```
Image 2: A detailed flowchart illustrating the end-to-end RAG workflow, divided into Offline Ingestion & Indexing and Online Retrieval & Generation phases, highlighting shared components.

### Phase 1: Offline Ingestion & Indexing

This phase happens in the background, before any user interacts with the system. Its goal is to process your knowledge base and create an index that enables efficient retrieval. This is a critical, one-time (or periodic) process that sets the foundation for the entire RAG system [[30]](https://newsletter.systemdesign.one/p/how-rag-works).

1.  **Load:** The process begins by loading documents from various sources. These can be anything from PDFs and websites to database records and API outputs. A variety of tools, such as LangChain's document loaders or LlamaIndex's readers, can be used to handle different data formats and sources. For example, you might use a PDF loader for internal manuals and a web scraper for online articles [[31]](https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/).
2.  **Split:** Since documents are often too large to fit into an LLM's context window, they are broken down into smaller, more manageable pieces called chunks. The chunking strategy is a crucial design decision. You can use simple rule-based splitters, like LangChain's `RecursiveCharacterTextSplitter`, or more advanced semantic chunkers that analyze the text to avoid splitting in the middle of a coherent thought or idea. The goal is to create chunks that are semantically meaningful and self-contained, typically between 200-400 tokens for most tasks [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a), [[47]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf/).
3.  **Embed:** Each chunk is then passed through an embedding model, which converts the text into a high-dimensional vector. This vector is a numerical representation that captures the semantic meaning of the chunk. There is a wide range of embedding models available, from proprietary ones like OpenAI's `text-embedding-3-large/small` and Google's `gemini-text-embedding-004` to powerful open-source models like BGE variants available on Hugging Face [[46]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).
4.  **Store:** Finally, these vector embeddings and their corresponding text chunks, along with any relevant metadata (like source, date, or category), are loaded into a specialized vector database. This database is optimized for fast similarity searches, allowing the system to quickly find the most relevant chunks for a given query. Options range from local libraries like FAISS for smaller-scale applications to production-grade, scalable databases like Milvus, Qdrant, Weaviate, and Pinecone [[6]](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0).

### Phase 2: Online Retrieval & Generation

This phase is triggered in real-time when a user submits a query. It is the interactive part of the RAG system that delivers the final answer [[29]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177/).

1.  **Query & Embed:** The user's question is taken as input. This query is then converted into a vector using the *same* embedding model that was used during the ingestion phase. This is a critical step, as it ensures that the query and the document chunks are represented in the same vector space, making them directly comparable [[8]](https://qdrant.tech/articles/what-is-rag-in-ai/).
2.  **Search:** The system uses the query vector to search the vector database. It calculates the similarity (often using cosine similarity) between the query vector and all the chunk vectors in the database. The database then returns the top-k most similar chunks, which are the pieces of information most semantically related to the user's question. The value of 'k' is a configurable parameter, often set to retrieve between 3 to 5 chunks [[49]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/), [[47]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf/).
3.  **Generate:** The retrieved chunks are combined with the original user query and a set of instructions into a single, augmented prompt. This prompt is then fed to an LLM, which uses the provided context to generate a final, grounded answer. This step can also use the structured output techniques we covered in Lesson 4 to ensure the answer is in a consistent format and includes citations to the source documents.

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

A naive RAG pipeline often works well for simple lookups but can struggle with the complexities of real-world data. To build a production-grade system, we need to move beyond the basics and incorporate advanced techniques that improve retrieval performance, relevance, and context quality.

### Hybrid Search

Vector search is powerful for understanding semantic meaning, but it can sometimes miss exact keywords, acronyms, or IDs. Hybrid search solves this by combining the strengths of dense (vector) retrieval with sparse (keyword-based) retrieval, like BM25. This multi-stage approach has roots in pre-LLM search engines, which also used pipelines of sparse retrieval, dense retrieval, and re-scoring to balance speed and relevance [[35]](https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/), [[76]](https://ijcaonline.org/archives/volume187/number18/veluru-2025-ijca-925279.pdf).

For example, in a customer support scenario, a user might ask, "My bill keeps rolling over." A vector search would find documents about "carryover balances," while a keyword search would find articles that explicitly mention "rollover." By fusing the results from both using a method like Reciprocal Rank Fusion (RRF), the system can cover different phrasings of the same underlying issue, leading to more comprehensive retrieval [[34]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid).

```mermaid
flowchart LR
  %% Initial Retrieval Methods
  subgraph "Retrieval"
    A["BM25 results<br/>(Keyword Search)"]
    B["Vector results<br/>(Semantic Search)"]
  end

  %% Combination and Re-ranking
  subgraph "Processing"
    C["Union / Fusion"]
    D["Re-rank"]
  end

  %% Final Output
  subgraph "Output"
    E["Final Context<br/>for LLM"]
  end

  A -- "sparse results" --> C
  B -- "dense results" --> C
  C -- "combined results" --> D
  D -- "re-ranked context" --> E

  classDef retrieval fill:#f9f,stroke:#333,stroke-width:2px
  classDef processing fill:#ccf,stroke:#333,stroke-width:2px
  classDef output fill:#cfc,stroke:#333,stroke-width:2px

  class A,B retrieval
  class C,D processing
  class E output
```
Image 3: A flowchart illustrating the hybrid retrieval flow, showing parallel BM25 and vector results converging into a union/fusion step, followed by re-ranking to produce the final context for an LLM.

### Re-ranking

The initial retrieval step is optimized for speed and recall, meaning it might return some documents that are only loosely related to the query. A re-ranker adds a second pass to improve precision. It uses a more computationally expensive but accurate model, typically a cross-encoder, to score the relevance of each retrieved document against the query. Unlike bi-encoders, which create separate embeddings for the query and document, a cross-encoder processes them together, allowing for deeper interaction between their tokens. The documents are then re-ordered based on these scores, ensuring that the most relevant information is passed to the LLM. This two-stage pattern is necessary because a cross-encoder must run a full forward pass for every (query, document) pair, making it too slow for the initial retrieval but perfect for refining a smaller set of candidates [[38]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/), [[41]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/).

This added computation introduces a latency trade-off. Under high load, a re-ranking step can become a bottleneck, as response times grow non-linearly when query rates exceed the system's throughput [[66]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/). For instance, if a user asks, "How do I connect my account?", the initial retrieval might pull a press release, a community forum thread, and a step-by-step guide. The re-ranker would identify the guide as the most relevant and push it to the top of the list [[39]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag).

### Query Transformations

Sometimes, the user's original query is not the best one for retrieval. Query transformation techniques rewrite or decompose the query to improve its chances of matching the right documents.

-   **Decomposition:** This technique breaks down a complex, multi-part question into several simpler sub-queries. For example, the question "What’s our travel policy for conferences in Europe this year?" could be decomposed into: (1) "What is the travel policy?", (2) "What are the rules for conferences?", (3) "Are there specific rules for Europe?", and (4) "What has changed this year?". The system retrieves documents for each sub-question and then synthesizes a comprehensive answer. The optimal number of sub-queries often depends on the domain; fact-verification may only need two, while complex biomedical questions might benefit from eight or more [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html), [[74]](https://aclanthology.org/2025.findings-emnlp.1022.pdf).
-   **HyDE (Hypothetical Document Embeddings):** This approach involves using an LLM to first generate a hypothetical answer to the user's query. For instance, before searching, the system might draft a short answer like: “Employees attending approved conferences in Europe can book economy flights and up to three hotel nights with daily meal limits.” This generated answer, which is often more detailed and contains relevant keywords, is then embedded and used for the similarity search. This helps bridge the gap between a short, ambiguous query and the more descriptive content in the knowledge base. However, because the generated answer reflects relevance patterns rather than facts, it can sometimes contain inaccuracies that limit retrieval precision [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/), [[90]](https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1/).

### Advanced Chunking Strategies

How you split your documents can have a huge impact on retrieval quality. Moving beyond simple fixed-size chunks can help preserve the context and structure of your data. The optimal strategy is not universal; it should be adapted to the type of document being processed [[94]](https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/).

-   **Semantic Chunking:** Instead of splitting by a fixed number of tokens, this method splits text based on semantic boundaries, aiming to keep coherent ideas or topics within the same chunk. This prevents situations where a key piece of information is cut in half across two different chunks. For example, in a company handbook, this would ensure the entire "Reimbursements" section, including its rules and limits, stays together [[18]](https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/).
-   **Layout-Aware Chunking:** For documents with complex structures like PDFs or financial reports, this method uses the visual layout (headings, tables, lists) to guide the chunking process. For a pricing table, it would keep each row intact, ensuring that products, prices, and discounts are not separated from each other [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a).

### GraphRAG

For questions about complex relationships and interconnected data, standard document retrieval can fall short. GraphRAG addresses this by first constructing a knowledge graph from the source documents, where entities (like people, companies, or products) are nodes and their relationships are edges. This structured representation allows the system to answer multi-hop questions that require traversing these connections. This is particularly effective for deeply hierarchical documents, such as legal contracts with amendments, where vector search alone might retrieve an outdated clause, a problem sometimes called "temporal hallucination" [[42]](https://arxiv.org/html/2601.03014v1), [[59]](https://arxiv.org/html/2404.16130).

For example, to answer "Which shoes get the most size-related returns and were featured in last month’s ads?", the system can traverse the graph from "returns" to "reason: sizing," link to specific shoe SKUs, and then connect those SKUs to the "marketing calendar," pulling all the supporting documents along the way. Similarly, for an IT operations query like, “Which incidents were caused by weekend deploys that also touched the login service?”, the system can link change records to deploy times, affected services, and incident tickets to surface the relevant post-mortems. This is far more effective than trying to find a single text chunk that contains all of this information [[44]](https://atlan.com/know/what-is-graphrag/).

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we introduced the ReAct framework, where an agent cycles through Thought, Action, and Observation to solve problems. Agentic RAG is the application of this pattern to information retrieval. Instead of a rigid, linear pipeline, retrieval becomes a dynamic tool that a reasoning agent can choose to use, ignore, or re-run as needed [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

The core distinction is the shift from a predetermined workflow to an adaptive, iterative process.

-   **Standard RAG** is a one-pass system: Retrieve → Augment → Generate. It is powerful but inflexible.
-   **Agentic RAG** is a control loop. The agent decides *when* to retrieve, *what* to search for, and *whether* the results are sufficient. If the first retrieval is weak, it can reformulate the query and try again [[12]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/).

```mermaid
flowchart LR
  %% Agent Main Loop
  subgraph "Agent ReAct Loop"
    Start["Start Loop"] --> Thought["Thought<br/>(Reasoning)"]
    Thought --> Action{"Action<br/>(Tool Selection)"}

    Action --> WebSearch["web_search"]
    Action --> CodeInterpreter["code_interpreter"]
    Action --> InternalKB["internal_knowledge_base<br/>(RAG Tool)"]

    WebSearch --> Observation["Observation<br/>(Tool Result)"]
    CodeInterpreter --> Observation
    InternalKB --> Observation

    Observation --> Thought
  end

  %% Optional: End condition
  Thought -. "If task complete" .-> End["End Loop"]

  classDef loopNode stroke-width:2px
  class Start,Thought,Action,Observation loopNode
```
Image 4: A conceptual flowchart illustrating an agent's main loop, emphasizing its iterative nature and decision-making capabilities based on the ReAct pattern. The loop includes "Thought", "Action", and "Observation" steps, with dynamic tool selection within the "Action" step.

This agentic approach unlocks several advanced capabilities. The agent can iteratively refine its search, choose between different knowledge sources (e.g., deciding if a query needs semantic search or a precise SQL query), and even fuse information from its internal RAG tool with results from other tools, like a web search, to build a more complete answer. However, this iterative freedom also introduces new engineering challenges, including performance bottlenecks from increased latency and reliability risks like "retrieval thrash," where an agent gets stuck in useless retrieval loops [[80]](https://devblogs.microsoft.com/azure-sql/improve-the-r-in-rag-and-embrace-agentic-rag-in-azure-sql/), [[96]](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167/), [[86]](https://towardsdatascience.com/agentic-rag-failure-modes-retrieval-thrash-tool-storms-and-context-bloat-and-how-to-spot-them-early/), [[68]](https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/).

Consider this simplified thought process for a query about "2024 EU data retention rules":

*   **Thought:** The user is asking about the 2024 rules, but our internal policy document is from 2023. It's likely outdated.
*   **Action:** `retrieve(internal_policy, query="EU data retention 2024")`
*   **Observation:** The retrieved text mentions upcoming amendments but lacks specific details or citations.
*   **Thought:** I need to verify this with a current, external source.
*   **Action:** `web_search(query="EU data retention rules 2024 official directive")`
*   **Observation:** The web search returns an official EU directive with the updated rules.
*   **Thought:** I can now synthesize an answer using both the internal policy and the new directive, highlighting the changes from 2023.

This is the difference between a simple database lookup and a conversation with a knowledgeable research assistant. It is important to note that retrieval is just one of many tools an agent can wield. Labeling an entire system "agentic RAG" can be too narrow; more accurately, it is an agent that uses RAG [[15]](https://domino.ai/blog/rag-vs-agentic-ai).

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have seen that RAG is the most widely used solution to the LLM knowledge problem, transforming them from "closed-book" reasoners into "open-book" experts. For production-grade quality, advanced techniques like hybrid search, re-ranking, and GraphRAG are essential. The future of knowledge retrieval is agentic, where RAG is not just a pipeline but a dynamic tool wielded by an intelligent agent.

The core benefits of this approach are clear: it reduces hallucinations, enables customization with proprietary data, and builds user trust by providing verifiable, source-based answers. RAG is not a niche skill but a foundational competency for the modern AI Engineer and a critical component of Context Engineering.

In our next lesson, we will explore Memory for Agents, and see how short-term and long-term memory systems complement retrieval to create AI that learns and remembers. Looking ahead, RAG systems are also evolving to handle not just text but also images and charts through multimodal embeddings, a topic we will cover in Lesson 11. We will also touch on other critical topics, such as evaluating retrieval quality and monitoring RAG systems in production, in future parts of the course [[81]](https://superlinear.eu/insights/articles/the-future-of-multimodal-rag-systems-transforming-ai-capabilities).

## References

- [1] Fine-Tuning vs. Retrieval Augmented Generation for LLMs. (2024, September 11). Neo4j. https://neo4j.com/blog/developer/fine-tuning-vs-rag/
- [2] Retrieval-augmented generation vs. fine-tuning: Enhancing LLMs. (n.d.). Medium. https://medium.com/@tahirbalarabe2/retrieval-augmented-generation-vs-fine-tuning-enhancing-llms-697e7a0cf7e0
- [3] Addressing AI hallucinations with retrieval-augmented generation. (n.d.). InfoWorld. https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html
- [4] Ovadia, O., et al. (2024). Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs. EMNLP. https://aclanthology.org/2024.emnlp-main.15.pdf
- [5] Ovadia, O., et al. (2023). Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs. arXiv. https://arxiv.org/html/2312.05934v3
- [6] Kakde, A. (2026, January 27). Vector Databases in Practice: Building a Realistic Hybrid Search RAG System with Qdrant. Towards AI. https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0
- [7] AWS Vector Databases Explained: Semantic Search and RAG Systems. (n.d.). Tutorials Dojo. https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/
- [8] What is RAG in AI? (n.d.). Qdrant. https://qdrant.tech/articles/what-is-rag-in-ai/
- [9] Ibrahim, M. (n.d.). Vector Embeddings in RAG Applications. Weights & Biases. https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5
- [10] Ibrahim, M. (2026, March 3). Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop. Towards Data Science. https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/
- [11] Agentic RAG vs. Traditional RAG: Key Differences And Benefits. (n.d.). PingCAP. https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/
- [12] Kumar, G. R. (n.d.). Agentic RAG vs Traditional RAG. Medium. https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167
- [13] AI Agent vs RAG. (n.d.). Airbyte. https://airbyte.com/agentic-data/ai-agent-vs-rag
- [14] RAG vs. agentic AI: Key differences and when to use each. (n.d.). Domino Data Lab. https://domino.ai/blog/rag-vs-agentic-ai
- [15] RAG System in Production: Why it Fails and How to Fix It. (n.d.). 47Billion. https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/
- [16] Improve Your RAG Accuracy with a Layout-Aware Chunking Strategy. (n.d.). Sarthak AI. https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a
- [17] Advanced RAG Techniques That Will Transform Your LLM Applications. (n.d.). Cloudurable. https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/
- [18] Query Decomposition. (n.d.). NVIDIA. https://docs.nvidia.com/rag/latest/query_decomposition.html
- [19] Bratanic, T., & Kruger, I. (2025, October 17). Advanced RAG Techniques for High-Performance LLM Applications. Neo4j. https://neo4j.com/blog/genai/advanced-rag-techniques/
- [20] Fahey, J. (n.d.). Retrieval-Augmented Generation: Building Grounded AI for Enterprise Knowledge. Medium. https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5
- [21] What is RAG? (n.d.). MindStudio. https://www.mindstudio.ai/blog/what-is-rag/
- [22] RAG Inventor Talks Agents, Grounded AI and Enterprise Impact. (n.d.). Madrona. https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/
- [23] RAG Architectures. (n.d.). Humanloop. https://humanloop.com/blog/rag-architectures
- [24] RAG and its Different Components. (n.d.). Aimon.ai. https://www.aimon.ai/posts/rag_and_its_different_components/
- [25] Grounding LLMs: Driving AI to Deliver Contextually Relevant Data. (n.d.). Toloka. https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/
- [26] What is retrieval-augmented generation? (n.d.). IBM. https://www.ibm.com/think/topics/retrieval-augmented-generation
- [27] RAG Architecture. (n.d.). Galileo. https://galileo.ai/blog/rag-architecture
- [28] Giggs, D. R. (n.d.). RAG Pipeline Deep-Dive: Ingestion, Chunking, Embedding, and Vector Search. Medium. https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177/
- [29] How RAG Works. (n.d.). System Design Newsletter. https://newsletter.systemdesign.one/p/how-rag-works
- [30] RAGOps Guide: Building and Scaling Retrieval-Augmented Generation Systems. (n.d.). Towards Data Science. https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/
- [31] RAG Offline vs Online Evaluation. (n.d.). apxml. https://apxml.com/courses/optimizing-rag-for-production/chapter-6-advanced-rag-evaluation-monitoring/rag-offline-online-evaluation
- [32] What is Retrieval-Augmented Generation (RAG)? (n.d.). AWS. https://aws.amazon.com/what-is/retrieval-augmented-generation/
- [33] Optimize RAG with Hybrid Search. (n.d.). ML Pills. https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid
- [34] Hybrid Search Optimization: How BM25 and Dense Vector Retrieval Work Together for Superior AI Search. (n.d.). Cubitrek. https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/
- [35] Hybrid RAG in the Real World: Graphs, BM25, and the End of Black Box Retrieval. (n.d.). NetApp Community. https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834
- [36] Bai, Y., et al. (2024). Pistis-RAG: Enhancing Retrieval-Augmented Generation with Human Feedback. arXiv. https://arxiv.org/html/2407.00072v5
- [37] 10 Techniques to Improve RAG Accuracy. (n.d.). Redis. https://redis.io/blog/10-techniques-to-improve-rag-accuracy/
- [38] Reranking Architectures in RAG. (n.d.). apxml. https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag
- [39] Advanced RAG Retrieval: Cross-Encoders & Reranking. (n.d.). Towards Data Science. https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/
- [40] Edge, D., et al. (2024). From Local to Global: A GraphRAG Approach to Query-Focused Summarization. arXiv. https://arxiv.org/html/2601.03014v1
- [41] GraphRAG. (n.d.). University of Victoria. https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf
- [42] What Is GraphRAG? (n.d.). Atlan. https://atlan.com/know/what-is-graphrag/
- [43] GraphRAG. (n.d.). arXiv. https://arxiv.org/html/2501.00309v2
- [44] Implementing Semantic Search for Retrieval. (n.d.). apxml. https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval
- [45] Tomar, R. (n.d.). How RAG Actually Works: Embeddings, Vector Databases, Indexing & Retrieval Explained Simply. Medium. https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf
- [46] Vector DB and RAG Pipeline for Document RAG. (n.d.). Learn OpenCV. https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/
- [47] RAG Explained: Understanding Embeddings, Similarity, and Retrieval. (n.d.). Towards Data Science. https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/
- [48] AWS Vector Databases Explained: Semantic Search and RAG Systems. (n.d.). Tutorials Dojo. https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/
- [49] Retrieval-Augmented Generation Explained. (n.d.). TopQuadrant. https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/
- [50] Raut, R. (n.d.). Introduction to Augmenting LLMs using Retrieval-Augmented Generation (RAG). Medium. https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91
- [51] Retrieval-Augmented Generation (RAG). (n.d.). Prompting Guide. https://www.promptingguide.ai/research/rag
- [52] Tejpal, A. (n.d.). Retrieval Augmented Generation (RAG) — From Basics to Advanced. Medium. https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c
- [53] Bouchard, L-F., et al. (2024, October 31). The Rise of RAG. High-Performance Computing. https://highlearningrate.substack.com/p/the-rise-of-rag
- [54] Iusztin, P. (n.d.). Your RAG Is Wrong, Here's How To Fix It. Decoding ML. https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search
- [55] Iusztin, P. (n.d.). Retrieval-Augmented Generation (RAG) Fundamentals First. Decoding ML. https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search
- [56] Simon, J. (2023, November 15). What Is Retrieval-Augmented Generation, aka RAG? NVIDIA Blogs. https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/
- [57] Edge, D., et al. (2024). From Local to Global: A GraphRAG Approach to Query-Focused Summarization. arXiv. https://arxiv.org/html/2404.16130
- [58] Introducing Contextual Retrieval. (2024, September 19). Anthropic. https://www.anthropic.com/news/contextual-retrieval
- [59] What is Agentic RAG. (n.d.). Weaviate. https://weaviate.io/blog/what-is-agentic-rag
- [60] RAG is dead, long live agentic retrieval. (n.d.). LlamaIndex. https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval
- [61] What is agentic RAG? (n.d.). IBM. https://www.ibm.com/think/topics/agentic-rag
- [62] Build advanced retrieval-augmented generation systems. (n.d.). Microsoft Learn. https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation
- [63] What is GraphRAG? (n.d.). FalkorDB. https://falkordb.com/blog/what-is-graphrag/
- [64] Agentic RAG: How enterprises are surmounting the limits of traditional RAG. (n.d.). Redis. https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/
- [65] Scaling RAG: Bottlenecks & Limitations. (n.d.). apxml. https://apxml.com/courses/large-scale-distributed-rag/chapter-1-scalable-rag-architectures-foundations/scaling-rag-bottlenecks-limitations
- [66] Hofstätter, S., et al. (2022). End-to-End Training of Neural Retrievers for Open-Domain Question Answering. https://pure.uva.nl/ws/files/118144878/978_3_030_99736_6_44.pdf
- [67] Kumar, S., et al. (2025). Bandit-based Sub-query Selection for Complex Information Needs. arXiv. https://arxiv.org/html/2510.18633v1
- [68] RAG problems? Five ways to fix them. (n.d.). IBM. https://www.ibm.com/think/insights/rag-problems-five-ways-to-fix
- [69] Zheng, Y., et al. (2025). Decomposing Complex Questions for LLM-based Question Answering. EMNLP. https://aclanthology.org/2025.findings-emnlp.1022.pdf
- [70] RAG Fundamentals: Challenges and Advanced Techniques. (n.d.). Label Studio. https://labelstud.io/blog/rag-fundamentals-challenges-and-advanced-techniques/
- [71] Veluru, S., et al. (2025). A Survey on Retrieval-Augmented Generation for Large Language Models. IJCA. https://ijcaonline.org/archives/volume187/number18/veluru-2025-ijca-925279.pdf
- [72] Case-Based Reasoning with Large Language Models. (2024). CEUR-WS. https://ceur-ws.org/Vol-3708/paper_21.pdf
- [73] Das, S., et al. (2024). CBR-RAG: Case-Based Reasoning for Retrieval Augmented Generation in LLMs for Legal Question Answering. arXiv. https://arxiv.org/abs/2404.04302
- [74] Optimizing SQL Queries for your AI Agents. (n.d.). dev.to. https://dev.to/sten/optimizing-sql-queries-for-your-ai-agents-41dj
- [75] Improve the R in RAG and embrace Agentic RAG in Azure SQL. (n.d.). Microsoft Dev Blogs. https://devblogs.microsoft.com/azure-sql/improve-the-r-in-rag-and-embrace-agentic-rag-in-azure-sql/
- [76] The Future of Multimodal RAG Systems: Transforming AI Capabilities. (n.d.). Superlinear. https://superlinear.eu/insights/articles/the-future-of-multimodal-rag-systems-transforming-ai-capabilities
- [77] What is the future of embeddings in multimodal search. (n.d.). Milvus. https://milvus.io/ai-quick-reference/what-is-the-future-of-embeddings-in-multimodal-search
- [78] Multimodal RAG and agents. (n.d.). Teradata. https://www.teradata.com/insights/ai-and-machine-learning/multimodal-rag-and-agents
- [79] Best-in-Class Multimodal RAG: How the Llama 3.2 Nemo Retriever Embedding Model Boosts Pipeline Accuracy. (n.d.). NVIDIA Developer Blog. https://developer.nvidia.com/blog/best-in-class-multimodal-rag-how-the-llama-3-2-nemo-retriever-embedding-model-boosts-pipeline-accuracy/
- [80] Ten Failure Modes of RAG Nobody Talks About (and How to Detect Them Systematically). (n.d.). dev.to. https://dev.to/kuldeep_paul/ten-failure-modes-of-rag-nobody-talks-about-and-how-to-detect-them-systematically-7i4
- [81] Agentic RAG Failure Modes: Retrieval Thrash, Tool Storms, and Context Bloat (And How to Spot Them Early). (n.d.). Towards Data Science. https://towardsdatascience.com/agentic-rag-failure-modes-retrieval-thrash-tool-storms-and-context-bloat-and-how-to-spot-them-early/
- [82] What are common agentic RAG failure modes in production? (n.d.). Milvus. https://milvus.io/ai-quick-reference/what-are-common-agentic-rag-failure-modes-in-production
- [83] Why RAG has exactly 6 failure modes. (n.d.). Java Revisited. https://javarevisited.substack.com/p/why-rag-has-exactly-6-failure-modes
- [84] QB-RAG: Query-Brokered RAG for Enhanced Context Understanding. (2024). arXiv. https://arxiv.org/html/2407.18044v2
- [85] Advanced Query Transformations to Improve your RAG. (n.d.). Towards Data Science. https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1/
- [86] Improve your RAG accuracy with a Layout-Aware Chunking Strategy. (n.d.). Sarthak AI. https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a
- [87] Document Chunking Strategies. (n.d.). LlamaIndex. https://www.llamaindex.ai/glossary/document-chunking-strategies
- [88] Semantic chunking. (n.d.). Microsoft Learn. https://learn.microsoft.com/en-us/azure/search/search-how-to-semantic-chunking
- [89] Your Chunks Failed Your RAG in Production. (n.d.). Towards Data Science. https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/
- [90] Hierarchical Navigable Small World (HNSW). (n.d.). Pinecone. https://www.pinecone.io/learn/series/faiss/hnsw/
- [91] Agentic RAG vs Traditional RAG. (n.d.). Medium. https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167
- [92] Scaling RAG: Bottlenecks & Limitations. (n.d.). apxml. https://apxml.com/courses/large-scale-distributed-rag/chapter-1-scalable-rag-architectures-foundations/scaling-rag-bottlenecks-limitations
- [93] Advanced RAG Retrieval: Cross-Encoders & Reranking. (n.d.). Towards Data Science. https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/
- [94] End-to-End Training of Neural Retrievers for Open-Domain Question Answering. (n.d.). University of Amsterdam. https://pure.uva.nl/ws/files/118144878/978_3_030_99736_6_44.pdf
- [95] Kumar, S., et al. (2025). Bandit-based Sub-query Selection for Complex Information Needs. arXiv. https://arxiv.org/html/2510.18633v1
- [96] RAG problems? Five ways to fix them. (n.d.). IBM. https://www.ibm.com/think/insights/rag-problems-five-ways-to-fix
- [97] Zheng, Y., et al. (2025). Decomposing Complex Questions for LLM-based Question Answering. EMNLP. https://aclanthology.org/2025.findings-emnlp.1022.pdf
- [98] RAG Fundamentals: Challenges and Advanced Techniques. (n.d.). Label Studio. https://labelstud.io/blog/rag-fundamentals-challenges-and-advanced-techniques/
- [99] Veluru, S., et al. (2025). A Survey on Retrieval-Augmented Generation for Large Language Models. IJCA. https://ijcaonline.org/archives/volume187/number18/veluru-2025-ijca-925279.pdf
- [100] Case-Based Reasoning with Large Language Models. (2024). CEUR-WS. https://ceur-ws.org/Vol-3708/paper_21.pdf
- [101] Das, S., et al. (2024). CBR-RAG: Case-Based Reasoning for Retrieval Augmented Generation in LLMs for Legal Question Answering. arXiv. https://arxiv.org/abs/2404.04302
- [102] Optimizing SQL Queries for your AI Agents. (n.d.). dev.to. https://dev.to/sten/optimizing-sql-queries-for-your-ai-agents-41dj
- [103] Improve the R in RAG and embrace Agentic RAG in Azure SQL. (n.d.). Microsoft Dev Blogs. https://devblogs.microsoft.com/azure-sql/improve-the-r-in-rag-and-embrace-agentic-rag-in-azure-sql/
- [104] The Future of Multimodal RAG Systems: Transforming AI Capabilities. (n.d.). Superlinear. https://superlinear.eu/insights/articles/the-future-of-multimodal-rag-systems-transforming-ai-capabilities
- [105] What is the future of embeddings in multimodal search. (n.d.). Milvus. https://milvus.io/ai-quick-reference/what-is-the-future-of-embeddings-in-multimodal-search
- [106] Multimodal RAG and agents. (n.d.). Teradata. https://www.teradata.com/insights/ai-and-machine-learning/multimodal-rag-and-agents
- [107] Best-in-Class Multimodal RAG: How the Llama 3.2 Nemo Retriever Embedding Model Boosts Pipeline Accuracy. (n.d.). NVIDIA Developer Blog. https://developer.nvidia.com/blog/best-in-class-multimodal-rag-how-the-llama-3-2-nemo-retriever-embedding-model-boosts-pipeline-accuracy/
- [108] Ten Failure Modes of RAG Nobody Talks About (and How to Detect Them Systematically). (n.d.). dev.to. https://dev.to/kuldeep_paul/ten-failure-modes-of-rag-nobody-talks-about-and-how-to-detect-them-systematically-7i4
- [109] Agentic RAG Failure Modes: Retrieval Thrash, Tool Storms, and Context Bloat (And How to Spot Them Early). (n.d.). Towards Data Science. https://towardsdatascience.com/agentic-rag-failure-modes-retrieval-thrash-tool-storms-and-context-bloat-and-how-to-spot-them-early/
- [110] What are common agentic RAG failure modes in production? (n.d.). Milvus. https://milvus.io/ai-quick-reference/what-are-common-agentic-rag-failure-modes-in-production
- [111] Why RAG has exactly 6 failure modes. (n.d.). Java Revisited. https://javarevisited.substack.com/p/why-rag-has-exactly-6-failure-modes
- [112] QB-RAG: Query-Brokered RAG for Enhanced Context Understanding. (2024). arXiv. https://arxiv.org/html/2407.18044v2
- [113] Advanced Query Transformations to Improve your RAG. (n.d.). Towards Data Science. https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1/
- [114] Improve your RAG accuracy with a Layout-Aware Chunking Strategy. (n.d.). Sarthak AI. https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a
- [115] Document Chunking Strategies. (n.d.). LlamaIndex. https://www.llamaindex.ai/glossary/document-chunking-strategies
- [116] Semantic chunking. (n.d.). Microsoft Learn. https://learn.microsoft.com/en-us/azure/search/search-how-to-semantic-chunking
- [117] Your Chunks Failed Your RAG in Production. (n.d.). Towards Data Science. https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/