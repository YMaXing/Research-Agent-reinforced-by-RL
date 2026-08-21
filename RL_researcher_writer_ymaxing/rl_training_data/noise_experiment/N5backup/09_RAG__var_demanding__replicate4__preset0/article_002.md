# Retrieval-Augmented Generation (RAG): Giving LLMs an Open-Book Exam

In our previous lessons, we built a solid foundation in AI Engineering. We explored the agent landscape, learned to distinguish between rigid LLM workflows and autonomous agents, and dove into context engineering. It is the art of managing the information we feed to LLMs. We have seen how to build agents that can reason and use tools to interact with their environment.

However, a core problem remains: LLMs are trained on a fixed dataset. Their knowledge is static, a snapshot of the world at a specific point in time. This makes them prone to hallucination and unable to access private or real-time information. When we ask an LLM a question, it is essentially taking a "closed-book exam" on its training data. We do not yet have techniques that allow models to continuously learn from experience after deployment.

While we can fine-tune them, this process is often inefficient. Fine-tuning is a resource-heavy and slow process. It requires large, high-quality labeled datasets, which are expensive and time-consuming to create. The training jobs themselves can take days or even weeks, and there is always the risk of "catastrophic forgetting," where the model loses previously learned information while adapting to new data [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/). Furthermore, fine-tuning only updates the model's internal knowledge up to a new point in time; it does not solve the problem of accessing real-time information.

Simply expanding the context window is not a silver bullet either. Although modern models can handle millions of tokens, this approach has its own drawbacks. Large context windows are expensive, as API costs are often tied to the number of tokens processed. They also introduce significant latency, making real-time applications sluggish. More importantly, they suffer from the "lost-in-the-middle" problem, where the model struggles to recall information buried deep within a long prompt [[2]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/). Performance can degrade long before the physical context limit is reached.

Retrieval-Augmented Generation (RAG) provides a reliable solution to this problem. It gives the LLM an "open-book exam" by connecting it to external, real-time knowledge sources [[3]](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/). Instead of forcing the model to memorize everything, we provide it with the relevant information at the moment it is needed. This approach is more like how humans work; we do not rely on memorization alone but use manuals, notes, and search engines to find the information we need.

RAG is a key method AI engineers use in the context engineering process, which we introduced in Lesson 3. It allows us to curate the context we provide to LLMs, ensuring their responses are grounded in factual, up-to-date information. In this lesson, we will explore the "what" and "how" of RAG, from its basic components to the advanced and agentic patterns that power modern AI systems. We will also see how RAG complements an agent's memory, a topic we will cover in detail in Lesson 10.

In this lesson, we will journey from the fundamentals of a basic RAG system to the advanced techniques that make it production-ready. We will explore the core components, the two-phase pipeline of ingestion and retrieval, and the sophisticated strategies that improve accuracy. Finally, we will see how RAG evolves into a powerful tool within the reasoning loop of an AI agent.

With the problem and motivation clear, we’ll first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of a RAG system is the first step in the context engineering process of designing effective AI applications. At its core, RAG can be broken down into three conceptual pillars that work together to ground an LLM's response in external data.

```mermaid
flowchart LR
  %% RAG System Core Components
  A["User Query"] --> B["Retriever"]
  B -- "retrieves relevant info" --> C["Augmentation"]
  C -- "formats augmented input" --> D["Generator (LLM)"]
  D -- "produces" --> E["Generated Answer"]
```
Image 1: A flowchart illustrating the core components and data flow of a RAG system.

### Retrieval

**Retrieval** is the engine for finding relevant information. When a user submits a query, the retriever’s job is to search an external knowledge base and pull the most relevant documents. The most common approach is semantic search, which finds text that is contextually similar in meaning, even if the wording is different [[4]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).

This is made possible by vector embeddings. These are numerical representations of text that capture its semantic meaning. During an offline process, documents are split into chunks, and each chunk is converted into a high-dimensional vector by an embedding model like BERT [[5]](https://qdrant.tech/articles/what-is-rag-in-ai/). These vectors are then stored in a specialized vector database.

Vector databases use indexing algorithms like Locality-Sensitive Hashing (LSH) or Hierarchical Navigable Small World (HNSW) to organize the vectors for fast and scalable searching [[6]](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0). At query time, the user's query is also converted into an embedding using the same model. The database then finds the chunks whose embeddings are closest to the query's embedding in the vector space, typically measured by cosine similarity [[4]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).

### Augmentation

**Augmentation** is the process of taking the retrieved information and preparing it for the LLM. Once the retriever has identified the most relevant document chunks, this information is combined with the original user query to form an enriched input, often called an augmented prompt [[7]](https://www.aimon.ai/posts/rag_and_its_different_components/). This step is a form of prompt engineering, where the retrieved context is structured in a way that guides the LLM to generate a coherent and contextually informed response [[8]](https://www.ibm.com/think/topics/retrieval-augmented-generation).

A well-constructed prompt will clearly separate the user's question from the provided context and include explicit instructions for the model. For example, a prompt template might look like this: "Using the context above, answer the question. If the context does not contain the answer, say so" [[9]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/). This ensures the model gives weight to the retrieved information and respects constraints, preventing it from falling back on its internal knowledge.

### Generation

**Generation** is the final step where the LLM produces an answer. The model receives the augmented prompt, which contains both the user’s original question and the relevant context retrieved from the external knowledge base. Using this information, the LLM synthesizes a response that is grounded in the provided data, rather than relying only on its pre-trained knowledge [[10]](https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/).

This process greatly reduces the risk of hallucinations. A notorious real-world failure occurred in 2023 when a lawyer used ChatGPT for legal research and submitted a brief citing several non-existent court cases that the model had fabricated [[1]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/). RAG mitigates this risk by forcing the model to base its answers on provided sources. This enables the generation of accurate, up-to-date, and verifiable responses that can include citations tracing back to the source documents [[11]](https://www.mindstudio.ai/blog/what-is-rag/).

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

A complete RAG pipeline is split into two distinct phases: an offline phase for preparing the data and an online phase for answering user queries in real-time. Understanding both is essential for building a production-ready system.

```mermaid
flowchart LR
  %% Phase 1: Offline Ingestion & Indexing
  subgraph "Offline Ingestion & Indexing"
    RD["Raw Documents"]
    L["Loaded<br/>(PDFs, APIs)"]
    S["Split<br/>(into chunks)"]
    E1["Embedded<br/>(Embedding Model)"]
    ST["Stored<br/>(Vector Database)"]

    RD -- "are" --> L
    L -- "then" --> S
    S -- "are" --> E1
    E1 -- "then" --> ST
  end

  %% Phase 2: Online Retrieval & Generation
  subgraph "Online Retrieval & Generation"
    UQ["User Query"]
    E2["Embedded<br/>(Embedding Model)"]
    SE["Search<br/>(Vector Database)"]
    G["Generator<br/>(LLM)"]
    GA["Grounded Answer"]

    UQ -- "is" --> E2
    E2 -- "used to" --> SE
    SE -- "retrieves chunks for" --> G
    G -- "produces" --> GA
  end

  %% Connection between phases
  ST -. "provides data for" .-> SE

  %% Visual grouping
  classDef data_store stroke-dasharray:3,3
  classDef model_op stroke-width:2px
  class ST data_store
  class E1,E2,G model_op
```
Image 2: A detailed Mermaid diagram showing the two distinct phases of a RAG pipeline: Offline Ingestion & Indexing and Online Retrieval & Generation.

### Phase 1: Offline Ingestion & Indexing

This phase happens in the background, before any user interacts with the system. Its goal is to process your knowledge base and make it searchable [[12]](https://newsletter.systemdesign.one/p/how-rag-works). This is a key step, as the quality of your indexed data directly impacts the performance of the entire RAG system.

1.  **Load:** The first step is to load raw documents from their sources. These can be PDFs, Word documents, web pages, database records, or content from APIs [[13]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177). Handling this diversity of formats is a common challenge, as each type requires different parsing logic to extract clean text while preserving structure. Libraries like `PyPDF2` for PDFs or `python-docx` for Word files can be used, but frameworks like LangChain and LlamaIndex offer unified document loaders that simplify this process by providing a consistent interface for multiple sources.

2.  **Split:** Once loaded, large documents are broken down into smaller, more manageable pieces called chunks. This is arguably the most important decision in the ingestion pipeline [[14]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a). If chunks are too large, they can contain multiple topics, leading to noisy and irrelevant retrieval. If they are too small, they may lack the necessary context to be useful. Strategies range from simple fixed-size splitting to more advanced methods like LangChain's `RecursiveCharacterTextSplitter`, which attempts to split along natural boundaries like paragraphs and sentences to maintain semantic coherence.

3.  **Embed:** Each chunk is then converted into a vector embedding using an embedding model. This numerical representation captures the semantic meaning of the text. The market offers a wide range of models, each with different performance characteristics and costs. Popular choices include OpenAI’s `text-embedding-3-large/small`, Google's `text-embedding-004`, and proprietary models from Cohere and Voyage. There are also powerful open-source models available on Hugging Face, such as the BGE and E5 series [[2]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/). The choice of model is a key decision, as it directly influences the quality of the semantic search. Considerations include the model's performance on relevant benchmarks (like MTEB), its dimensionality (which affects storage costs), and its suitability for your specific domain (e.g., legal or medical text).

4.  **Store:** Finally, the embeddings and their corresponding text chunks (along with any metadata) are loaded into a vector database. This database is optimized for efficient similarity search, allowing the system to quickly find the most relevant chunks for a given query. For small-scale projects, a local library like FAISS might suffice. For production systems, scalable databases such as Milvus, Qdrant, or Pinecone are common choices. Additionally, many traditional databases like Elasticsearch and PostgreSQL (with the `pgvector` extension) now offer k-Nearest Neighbors (k-NN) search capabilities [[15]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf).

### Phase 2: Online Retrieval & Generation

This phase is triggered in real-time when a user asks a question. It is responsible for finding the right context and generating a grounded answer. Here is a comparison of how this can be implemented using two popular frameworks: LangChain and LlamaIndex.

1.  First, let's look at a simple implementation with LangChain. It provides a high-level `RetrievalQA` chain that abstracts away many of the steps.
    ```python
    from langchain_community.vectorstores import Qdrant
    from langchain_openai import OpenAIEmbeddings, OpenAI
    from langchain.chains import RetrievalQA
    from langchain_community.document_loaders import TextLoader
    
    # 1. Load and process the document
    loader = TextLoader("document.txt")
    documents = loader.load()
    
    # 2. Create embeddings and store in a vector database (Qdrant in this case)
    embeddings = OpenAIEmbeddings()
    doc_store = Qdrant.from_documents(
        documents,
        embeddings,
        location=":memory:", # Use in-memory for simplicity
        collection_name="my_docs",
    )
    
    # 3. Set up the retrieval chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff", # "stuff" chain type combines all retrieved docs into the prompt
        retriever=doc_store.as_retriever(),
    )
    
    # 4. Ask a question
    query = "What is the main topic of the document?"
    response = qa_chain.invoke(query)
    print(response)
    ```

2.  Now, let's compare this to LlamaIndex, which is specifically designed for building RAG applications and offers more granular control.
    ```python
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
    from llama_index.embeddings.openai import OpenAIEmbedding
    from llama_index.llms.openai import OpenAI
    from llama_index.core import Settings
    
    # 1. Configure global settings for LLM and embedding models
    Settings.llm = OpenAI(model="gpt-4o")
    Settings.embed_model = OpenAIEmbedding()
    
    # 2. Load documents from a directory
    documents = SimpleDirectoryReader("./data").load_data()
    
    # 3. Create the index (handles chunking, embedding, and storing)
    index = VectorStoreIndex.from_documents(documents)
    
    # 4. Create a query engine from the index
    query_engine = index.as_query_engine()
    
    # 5. Ask a question
    query = "What is the main topic of the document?"
    response = query_engine.query(query)
    print(response)
    ```
    While both frameworks achieve the same goal, their philosophies differ. LangChain provides a flexible, chain-based abstraction that is useful for building complex workflows, whereas LlamaIndex is more RAG-centric, offering optimized components like `QueryEngine` that are tailored for retrieval and synthesis tasks. As we covered in Lesson 4, using structured outputs can further enhance this process by ensuring the answer is consistently formatted and includes citations.

With the end-to-end path in place, the next question is quality: what are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While a basic RAG pipeline is a good start, production systems require more sophisticated techniques to handle the complexities of real-world data and user queries. These advanced methods are designed to improve retrieval accuracy, manage context effectively, and ultimately produce more reliable answers.

```mermaid
flowchart LR
  %% Start of the process
  A["User Query"]

  %% Simultaneous retrieval methods
  subgraph Retrieval
    B["Dense Retrieval<br/>(Vector Search)"]
    C["Sparse Retrieval<br/>(BM25 Keyword Search)"]
  end

  %% Combining and re-ranking
  D["Reciprocal Rank Fusion (RRF)"]
  E["Re-ranker"]

  %% Final output and generation
  F["Final Top-K Chunks"]
  G["LLM"]

  %% Connections
  A -- "processed by" --> B
  A -- "processed by" --> C
  B -- "results" --> D
  C -- "results" --> D
  D -- "fused results" --> E
  E -- "re-ranked results" --> F
  F -- "for generation" --> G

  %% Visual grouping
  classDef process fill:#f9f,stroke:#333,stroke-width:2px
  class B,C,D,E,F,G process
```
Image 3: A flowchart illustrating the hybrid retrieval process from user query to LLM generation.

### Hybrid Search

Vector search is great at understanding semantic meaning, but it can sometimes miss exact keywords, product codes, or specific identifiers. Hybrid search solves this by combining dense retrieval (vector search) with sparse retrieval methods like BM25, which excel at keyword matching [[16]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid). For example, if a customer support user searches for "my bill keeps rolling over," a keyword search will find articles containing the exact term "rollover." A semantic search might also surface guides that use related phrases like "carryover balance." By running both searches in parallel and fusing the results—often using a technique called Reciprocal Rank Fusion (RRF)—the system can capture both precise and conceptually related documents, providing more comprehensive coverage [[17]](https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html).

### Re-ranking

The initial retrieval step is optimized for speed and recall, meaning it casts a wide net to find potentially relevant documents. However, not all retrieved documents are equally useful. A re-ranker is a second, more precise model that re-orders this initial set of documents to improve relevance. Typically, a cross-encoder model is used, which processes the query and each candidate document together to produce a highly accurate relevance score [[18]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag). For instance, when a user asks, "how to connect my account," a re-ranker like Cohere Rerank can push the official step-by-step setup guide to the top of the list, above a less relevant press release or a tangentially related community forum thread that also happened to match the initial query [[19]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/).

### Query Transformations

Sometimes, the user's query is not in the optimal format for retrieval. Query transformation techniques rewrite the query to improve its chances of matching the right documents.
-   **Decomposition** breaks down complex, multi-faceted questions into smaller, more focused sub-queries. For a question like, “What’s our travel policy for conferences in Europe this year?” the system might generate sub-questions such as “Where is the travel policy located?”, “What are the rules for Europe?”, and “What has changed in the policy this year?” It then retrieves documents for each sub-question and merges the results to provide a complete answer [[20]](https://docs.nvidia.com/rag/latest/query_decomposition.html).
-   **Hypothetical Document Embeddings (HyDE)** addresses the "phrasing gap" between questions and answers. Instead of embedding the user's query directly, the system first uses an LLM to generate a short, hypothetical answer. It then embeds this ideal answer and uses that embedding for the vector search [[2]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/). For a travel policy query, the system might generate a draft like, "Employees attending approved conferences in Europe can book economy flights..." and then search for documents that match this statement, leading it directly to the relevant policy pages.

### Advanced Chunking Strategies

How you chunk your documents is critical. Moving beyond simple fixed-size splitting can dramatically improve retrieval quality. NVIDIA’s 2024 benchmarks found up to a 9% recall gap between the best and worst chunking strategies [[2]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/).
-   **Semantic chunking** splits text based on topic shifts rather than arbitrary token counts. It uses embeddings to measure the semantic distance between consecutive sentences and creates a new chunk when the topic changes significantly. This ensures that each chunk contains a single, coherent idea, which is ideal for precise retrieval [[14]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a). For example, splitting a 20-page employee handbook by topic would keep the entire "Reimbursements" section intact, ensuring that rules and spending caps are not separated.
-   **Layout-aware chunking** is designed for documents with complex structures like PDFs, tables, and forms. It parses the document's visual layout to identify headers, tables, and lists, and chunks the content accordingly [[14]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a). For a pricing table, this strategy would keep each row (e.g., product, price, discount) together, preventing the system from retrieving a price without its corresponding product label.
-   **Context-enriched chunking** prepends a summary of the document's context to each chunk before embedding. This technique, also known as contextual retrieval, helps the embedding capture the chunk's place within the larger document, improving retrieval accuracy. Anthropic reported that this method can reduce retrieval failures by 49% [[2]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/).

### GraphRAG

For questions about complex relationships and interconnected entities, standard document chunks often fall short. **GraphRAG** addresses this by first extracting entities and their relationships from the source documents and constructing a knowledge graph. This structured representation allows the system to answer multi-hop questions that require reasoning across different pieces of information [[21]](https://arxiv.org/html/2601.03014v1). For example, a retail system could answer, “Which shoes get the most size-related returns and were featured in last month’s ads?” by traversing the graph from return records to sizing issues, to specific product SKUs, and finally to marketing campaign data. A 2024 Stanford study confirmed that graph-augmented retrieval reduced factual errors by 35-45% on multi-hop question answering benchmarks [[22]](https://atlan.com/know/what-is-graphrag/).

### Metadata Filtering

One of the most effective ways to improve retrieval in a production environment is to use metadata filters. By tagging each chunk with metadata—such as `source`, `department`, `country`, `policy_version`, or `effective_date`—you can dramatically narrow the search space before performing the vector search. Temporal filters are especially powerful. For a query like, “What changed between March and June 2025?”, the system can restrict its search to chunks with an `effective_date` within that range. You can even implement bitemporal logic, filtering by `effective_date` to find what was true at a certain time, while also tracking `indexed_at` to ensure data freshness [[23]](https://neo4j.com/blog/genai/advanced-rag-techniques/).

Here is a code example using LlamaIndex to create a more advanced, auto-routing retriever that can intelligently choose between different retrieval modes.
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.indices.managed.llama_cloud import LlamaParseIndex
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# This example assumes you have a LlamaParseIndex already created.
# For a new index:
# financial_index = LlamaParseIndex(name="Financial Reports", project_name="MyProject")
# financial_index.insert_documents(["path/to/doc1.pdf", "path/to/doc2.pdf"])

# For this example, we'll simulate loading an existing index.
# In a real scenario, you would load your pre-built index.
# Let's create a dummy index for demonstration purposes.
Settings.llm = OpenAI(model="gpt-4o")
Settings.embed_model = OpenAIEmbedding()
documents = SimpleDirectoryReader(input_files=["./dummy_financial_report.txt"]).load_data()
financial_index = VectorStoreIndex.from_documents(documents)


# Create a retriever with auto_routed mode
# This agentically determines whether to use chunk, files_via_metadata, or files_via_content retrieval
auto_retriever = financial_index.as_retriever(retrieval_mode="auto") # "auto" mode in newer LlamaIndex

# This query is specific and will likely be routed to vector search over chunks
nodes = auto_retriever.retrieve("What was the company's revenue in the last quarter?")
print(f"Query 1 retrieved {len(nodes)} node(s).")


# This query mentions a specific file and would be routed to a metadata-aware retriever if configured
# Note: This requires a more complex setup with metadata extraction during ingestion.
# For this simple example, it will still use vector search.
nodes_by_file = auto_retriever.retrieve("What does the dummy_financial_report.txt file say about the outlook?")
print(f"Query 2 retrieved {len(nodes_by_file)} node(s).")
```

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored how ReAct agents use a "Thought, Action, Observation" loop to reason and interact with their environment. **Agentic RAG** is the application of this principle, where retrieval is not a fixed step in a pipeline but a tool that an agent can choose to use. The agent reasons about its task, decides when it needs information, formulates a query, and observes the results, iterating until it has enough context to answer the user's question.

It is important to clarify that agents often have access to many tools, such as web search, code interpreters, and database query engines. Labeling an entire system as "agentic RAG" can be misleading; more accurately, the RAG system functions as one of the primary tools in the agent's toolkit [[24]](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167).

The core distinction between standard and agentic RAG lies in their control flow. Standard RAG is a linear, predetermined workflow: Retrieve → Augment → Generate. It is powerful but rigid [[25]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/). In contrast, agentic RAG is adaptive and iterative. The agent is in control, deciding *when* to retrieve, *how* to reformulate a query, *which* knowledge source to search, and whether to chain multiple retrieval and reasoning steps together [[26]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/). This transforms the system from a static pipeline into a dynamic control loop.

This agentic approach unlocks several advanced capabilities:
-   The agent can **iteratively** use the RAG tool. If an initial retrieval yields a vague policy document, the agent can reason about the missing information and refine its query—for example, by adding "for EU customers, 2024 updates"—and retrieve again to find more specific details.
-   It can **choose** which part of its knowledge base to search. For an inquiry about a system outage, an agent might intelligently select its `search_incident_runbooks` tool over `search_marketing_pages`.
-   It can **fuse** information from its internal RAG tool with data from other tools, like a web search. For instance, an agent could retrieve an internal company policy on data retention, then call its `web_search` tool to check for recent changes in regulatory requirements, and finally synthesize both pieces of information into a comprehensive answer.
-   It can even decide to **update** the knowledge base with new information it learns. As we will explore in Lesson 10 on agent memory, an agent might propose writing new facts to a long-term memory store, thereby improving the knowledge base for future queries.

Let's consider a conceptual "thought process" for an agent tackling a complex query:
*   **Thought:** "The user is asking about '2024 EU data retention rules.' Our internal policy documents cite a 2023 version. This information is likely outdated."
*   **Action:** `retrieve(internal_policy, query="EU data retention 2024")`
*   **Observation:** "The retrieved document mentions recent amendments but is missing specific citations for the new directive."
*   **Thought:** "I need external verification to provide a complete and accurate answer."
*   **Action:** `web_search(query="EU data retention directive 2024 official text")`
*   **Observation:** "The web search found the official directive update from the European Commission's website."
*   **Thought:** "Now I can synthesize the information from both the internal policy and the official directive, highlight the changes from the 2023 version, and cite both sources."

This shift transforms RAG from a simple database lookup into a dynamic conversation with a knowledgeable research assistant.

```mermaid
flowchart LR
  %% Main Agent Loop
  Agent["Agent"] --> Thought["Thought"]
  Thought --> Action["Action"]

  %% Tools Subgraph
  subgraph Tools["Tools"]
    WebSearch["web_search"]
    CodeInterpreter["code_interpreter"]
    InternalKB["internal_knowledge_base<br/>(RAG tool)"]
  end

  Action -- "uses" --> WebSearch
  Action -- "uses" --> CodeInterpreter
  Action -- "uses" --> InternalKB

  WebSearch --> Observation["Observation"]
  CodeInterpreter --> Observation
  InternalKB --> Observation

  Observation --> Thought: "informs new"

  %% Visual grouping
  classDef main_step stroke-width:2px
  classDef tool_node stroke-dasharray:3,3
  class Agent,Thought,Action,Observation main_step
  class WebSearch,CodeInterpreter,InternalKB tool_node
```
Image 4: A conceptual Mermaid diagram showing an agent's main loop, including thought, action, tool usage (web_search, code_interpreter, internal_knowledge_base), and observation, leading to iterative refinement.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

In this lesson, we have seen that RAG is the most widely used solution to the fundamental knowledge limitations of LLMs. It provides a practical way to ground models in external, verifiable data, moving them from "closed-book" to "open-book" reasoners. We have also learned that while basic RAG is a good starting point, production-grade applications require advanced techniques like hybrid search, re-ranking, and intelligent chunking to achieve high quality. The future of knowledge retrieval is agentic, where RAG becomes a dynamic tool in an intelligent agent's toolkit.

The core benefits of RAG are clear: it reduces hallucinations, enables customization with proprietary and real-time data, and builds user trust by providing source-backed, verifiable answers. For these reasons, mastering RAG is a foundational competency for the modern AI Engineer and a key part of the broader discipline of context engineering.

In our next lesson, we will explore memory for agents. We will see how short-term and long-term memory systems work alongside RAG's on-demand retrieval to create agents that can learn from past interactions and build a persistent understanding of their environment. RAG provides the "what" (the facts), while memory provides the "who" and "when" (the conversational and user-specific context). We will also touch upon other topics, such as retrieval quality evaluation and production monitoring, in future parts of the course to give you a complete picture of building and maintaining high-performing RAG systems.

## References

- [1] [Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [2] [RAG System in Production: Why It Fails and How to Fix It](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/)
- [3] [What Is Retrieval-Augmented Generation, aka RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [4] [Implementing Semantic Search for Retrieval](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)
- [5] [Vector databases store information as vector embeddings.](https://qdrant.tech/articles/what-is-rag-in-ai/)
- [6] [Vector Databases in Practice: Building a Realistic Hybrid-Search RAG System with Qdrant](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0)
- [7] [RAG and its different components](https://www.aimon.ai/posts/rag_and_its_different_components/)
- [8] [What is retrieval-augmented generation (RAG)?](https://www.ibm.com/think/topics/retrieval-augmented-generation)
- [9] [Retrieval-Augmented Generation, Explained](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/)
- [10] [Grounding LLMs: Driving AI to Deliver Contextually Relevant Data](https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/)
- [11] [What Is RAG?](https://www.mindstudio.ai/blog/what-is-rag/)
- [12] [How RAG works](https://newsletter.systemdesign.one/p/how-rag-works)
- [13] [RAG Pipeline Deep Dive: Ingestion, Chunking, Embedding, and Vector Search](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)
- [14] [Improve Your RAG Accuracy With A Smarter Chunking Strategy](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a)
- [15] [How RAG Actually Works: Embeddings, Vector Databases, Indexing & Retrieval Explained Simply](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf)
- [16] [Optimize RAG with Hybrid Search](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid)
- [17] [Hybrid Search Is a Must for Production RAG](https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html)
- [18] [Reranking Architectures for RAG](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag)
- [19] [10 Techniques to Improve RAG Accuracy](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)
- [20] [Query decomposition is a technique that breaks down complex, multi-faceted user queries into simpler, more focused subqueries.](https://docs.nvidia.com/rag/latest/query_decomposition.html)
- [21] [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/html/2601.03014v1)
- [22] [What Is GraphRAG? How It Works, Benefits, and More](https://atlan.com/know/what-is-graphrag/)
- [23] [Advanced RAG Techniques for High-Performance LLM Applications](https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [24] [Agentic RAG vs Traditional RAG](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167)
- [25] [Agentic RAG vs Traditional RAG: Key Differences & Benefits](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/)
- [26] [Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)