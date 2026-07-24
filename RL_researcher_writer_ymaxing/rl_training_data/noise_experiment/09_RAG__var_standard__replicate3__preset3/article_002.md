# Lesson 9: Retrieval-Augmented Generation

I remember one of my first big projects as an AI Engineer. We were building a customer support agent for a fast-growing startup. The agent was trained on all the company’s documentation and seemed brilliant in demos. But a week after launch, we got a flood of complaints. A major product feature had been updated, but the agent, with its static knowledge, kept giving customers outdated instructions. It was confidently wrong, and our users were frustrated. That experience taught me a hard lesson: an AI’s intelligence is useless if its knowledge is frozen in time.

In our previous lessons, we have built a solid foundation in AI Engineering. We have explored the agent landscape, distinguished between LLM workflows and autonomous agents, and, in Lesson 3, we covered context engineering—the art of managing the information an LLM sees. We have also learned how to get structured data out of models, give them tools to perform actions, and implement reasoning loops like ReAct.

A core problem we have touched on is that LLMs are trained on a fixed dataset. Their knowledge is static, making them prone to hallucination. During training, they are essentially taking a "closed-book exam" on the world's information. We do not yet have techniques that allow models to continuously learn new information after deployment in the same way humans do. While we can fine-tune them, this process is slow, expensive, and creates yet another static snapshot [[12]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/).

Retrieval-Augmented Generation (RAG) offers a powerful and reliable solution to this problem. Instead of trying to bake new knowledge into the model's weights, we can insert it directly into the context window at inference time. With RAG, we are giving the LLM an "open-book exam." Just as a person does not need to memorize every fact, an LLM can use external documents, manuals, or databases as a reference [[14]](https://newsletter.systemdesign.one/p/how-rag-works). This approach, a key method within the context engineering discipline we covered in Lesson 3, allows us to ground LLM responses in verifiable, up-to-date information.

This technique is not new; its roots trace back to question-answering systems from the 1970s [[1]](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/). However, its modern form was conceptualized in a 2020 paper by Meta AI researchers [[11]](https://highlearningrate.substack.com/p/the-rise-of-rag). Since then, the approach has rapidly evolved. The initial, straightforward method, often called "naive RAG," has given way to more sophisticated techniques that address its limitations [[18]](https://www.arionresearch.com/blog/uuja2r7o098i1dvr8aagal2nnv3uik), [[19]](https://www.ibm.com/think/topics/rag-techniques). In this lesson, we will explore the "what" and "how" of RAG, starting with its fundamental components and moving toward the advanced and agentic patterns that power modern AI systems. We will also see how retrieval complements an agent's memory, a topic we will explore further in Lesson 10.

With the problem and motivation clear, we will first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the core components of RAG is the first step in the context engineering process of designing an effective system. At its heart, RAG is built on three conceptual pillars: Retrieval, Augmentation, and Generation. These pillars work together to transform a user's query into a knowledgeable and grounded response, forming a robust pipeline that addresses the limitations of standalone LLMs.

**Retrieval** is the engine responsible for finding relevant information. When a user submits a query, the retrieval system searches an external knowledge base to find documents or data snippets that are most likely to contain the answer. This search is often powered by a combination of methods. The most common is semantic similarity, where the meaning of the query is matched against the meaning of the documents. This is made possible by vector embeddings—numerical representations of text that capture semantic meaning. These vectors are stored in a specialized vector database that allows for efficient searching, enabling the system to find contextually similar information even if the wording is different [[25]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).

However, semantic search alone is not always enough. It can sometimes miss specific keywords, product codes, or names. To address this, retrieval systems often incorporate traditional keyword-based search methods like BM25. This technique ranks documents based on the frequency and rarity of query terms, excelling at finding exact matches. By combining both semantic and keyword search, the retrieval pillar can cast a wider and more accurate net, ensuring that both conceptually similar and lexically identical information is found.

**Augmentation** is the process of taking the retrieved information and preparing it for the LLM. The system combines the original user query with the relevant data snippets it found. This combined text, or "augmented prompt," provides the LLM with the necessary context to formulate a grounded and accurate response. The construction of this prompt is a critical step. It often involves a template that clearly separates the user's question from the retrieved context and provides instructions on how to use that context to generate an answer. This ensures the model understands its role is to synthesize information from the provided sources, not to rely on its internal knowledge [[26]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/).

**Generation** is the final step. The augmented prompt is sent to an LLM, which uses its reasoning capabilities to synthesize an answer based on the provided context. Instead of relying on its static, internal knowledge, the model's role shifts to that of a reasoner that synthesizes information from the provided context. This directly addresses the hallucination problem by forcing the model to base its answer on the source material, which can then be cited to build user trust. The generation step turns the raw, retrieved data into a coherent, human-readable answer that directly addresses the user's query [[1]](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/).

Image 1: A flowchart illustrating the core components and data flow of a Retrieval Augmented Generation (RAG) system.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow is split into two distinct phases: an offline ingestion pipeline that prepares the knowledge base, and an online retrieval pipeline that answers user queries in real-time. This separation allows the computationally intensive work of processing documents to happen once, offline, while the user-facing retrieval process remains fast and responsive. This two-phase architecture is fundamental to building scalable and efficient RAG systems [[27]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177).

### Phase 1: Offline Ingestion & Indexing

This phase happens before your users ever ask a question. Its goal is to process your raw documents and index them for efficient retrieval. It is a multi-step process that transforms unstructured data into a searchable knowledge base, forming the foundation of your RAG system.

- **Load:** The first step is to load your documents from their various sources. These can be PDFs, websites, databases, or APIs. The research shows that modern frameworks offer connectors for a wide range of sources, including Slack channels and Confluence pages. Tools like Unstructured, LangChain document loaders, and LlamaIndex readers are commonly used to handle this data ingestion [[14]](https://newsletter.systemdesign.one/p/how-rag-works).
- **Split:** Since LLMs have limited context windows, you cannot feed them entire documents at once. The documents are broken down into smaller, semantically meaningful pieces called chunks. This can be done with simple rule-based splitters, like LangChain’s `RecursiveCharacterTextSplitter`, or more advanced semantic chunkers like LlamaIndex's `SemanticSplitter` that avoid splitting a coherent thought in the middle. Getting this step right is one of the most critical parts of building a high-quality RAG system [[14]](https://newsletter.systemdesign.one/p/how-rag-works).
- **Embed:** Each chunk of text is then converted into a vector embedding using an embedding model. These high-dimensional vectors capture the semantic meaning of the text. Popular models for this task include OpenAI’s `text-embedding-3` series, Google's `text-embedding-004`, Cohere's Embed models, Voyage, and various open-source `bge` variants available through Hugging Face.
- **Store:** Finally, the vector embeddings and their corresponding text chunks are loaded into a vector database. This specialized database is optimized for fast similarity searches. Popular choices include local libraries like FAISS for smaller projects, or scalable, production-grade databases like Milvus, Qdrant, Pinecone, and vector-enabled search indexes like Elasticsearch, OpenSearch, or Azure AI Search. During this step, it is also crucial to store metadata alongside the chunks, such as the source document, creation date, or access permissions. This metadata becomes vital for filtering results and providing citations later [[14]](https://newsletter.systemdesign.one/p/how-rag-works).

### Phase 2: Online Retrieval & Generation

This phase is triggered when a user interacts with your application. It is designed to be fast and efficient, delivering a grounded answer in seconds.

- **Query:** The user asks a question. This query can be optionally pre-processed to normalize it or expand it for better results. Frameworks like LangChain's `Runnable` chains or LlamaIndex's `QueryEngine` orchestrate this process.
- **Embed:** The user's query is converted into a vector embedding using the exact same embedding model that was used during the ingestion phase. This is critical to ensure that the query and the documents exist in the same vector space, allowing for a meaningful comparison [[25]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval).
- **Search:** The system uses the query vector to search the vector database. It performs a similarity search (like cosine similarity) to find the top-k document chunks whose embeddings are closest to the query's embedding. This can be a pure vector search or a hybrid search that also incorporates keyword matching.
- **Generate:** The retrieved chunks are assembled into a prompt along with the original user query and specific instructions. This augmented prompt is then passed to an LLM, which generates a final answer grounded in the provided context. To ensure reliability, we can use the structured output techniques from Lesson 4 to format the answer and include citations, which is a key advantage of RAG.

Image 2: A detailed Mermaid diagram depicting the end-to-end RAG workflow, split into two distinct phases: "Offline Ingestion & Indexing" and "Online Retrieval & Generation".

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

A basic RAG pipeline is a great start, but production systems often require more sophisticated techniques to achieve high accuracy. These advanced methods focus on improving the quality of the retrieval step, ensuring the LLM receives the most relevant and precise context possible. The goal is to move beyond simple semantic similarity and build a more nuanced understanding of both the query and the documents, which is essential for handling the complexity of real-world data.

### Hybrid Search

Hybrid search combines the strengths of traditional keyword-based search (like BM25) with modern vector search. While vector search is excellent at understanding semantic meaning and finding conceptually related documents, it can sometimes miss exact keyword matches for specific terms, names, or codes. BM25, on the other hand, excels at this by ranking documents based on term frequency and inverse document frequency [[28]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid).

For example, in a customer support scenario, a user might ask, "My bill keeps rolling over." A keyword search would find articles containing the exact term "rollover." A vector search might also surface guides about "carryover balance," capturing the user's intent even with different wording. A hybrid approach uses both, ensuring comprehensive coverage. A common technique to combine these different result sets is Reciprocal Rank Fusion (RRF). RRF elegantly merges ranked lists without needing to normalize their scores, which often operate on completely different scales. It calculates a new score based on the reciprocal of each document's rank in each list, effectively giving more weight to documents that appear high up in multiple search results [[20]](https://dev.to/lpossamai/building-hybrid-search-for-rag-combining-pgvector-and-full-text-search-with-reciprocal-rank-fusion-6nk).

Image 3: A Mermaid diagram illustrating the hybrid retrieval flow.

### Re-ranking

Re-ranking introduces a second, more precise model to refine the initial search results. The first retrieval step is optimized for speed and recall, casting a wide net to find a set of potentially relevant documents. This is typically done with a bi-encoder, which creates separate embeddings for the query and documents and compares them. However, the best document might not always be at the top of this initial list.

A re-ranker, often a cross-encoder model, takes the user's query and each retrieved document as a pair and calculates a more accurate relevance score. Because the cross-encoder processes the query and document tokens together, it can capture much finer-grained interactions and relevance signals [[15]](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/). For instance, if a user searches "how to connect my account," a re-ranker can push a step-by-step setup guide to the top, above a less relevant press release or a tangentially related community forum thread. Services like Cohere Rerank provide powerful, off-the-shelf models for this purpose.

### Query Transformations

Sometimes, the user's original query is not the best one for searching your knowledge base. Query transformation techniques rewrite or decompose the query to improve retrieval accuracy.

- **Decomposition:** This method breaks down a complex, multi-part question into several simpler sub-questions. For example, the query "What’s our travel policy for conferences in Europe this year?" could be decomposed into: (1) "Where is the travel policy located?", (2) "What are the rules for conferences?", (3) "Are there specific rules for Europe?", and (4) "What has changed in the policy this year?". The system retrieves documents for each sub-question and then synthesizes the answers [[29]](https://docs.nvidia.com/rag/latest/query_decomposition.html).
- **Hypothetical Document Embeddings (HyDE):** This technique uses an LLM to generate a hypothetical, ideal answer to the user's query *before* searching. For a query about conference travel, the system might generate a short paragraph like: "Employees attending approved conferences in Europe can book economy flights and stay in hotels up to three nights, with daily meal limits." It then creates an embedding of this hypothetical answer and uses it to search for real documents that are semantically similar, which often helps bridge the gap between the phrasing of a question and the phrasing of an answer [[4]](https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search).

### Advanced Chunking Strategies

How you split your documents into chunks has a massive impact on retrieval quality. Naive fixed-size chunking, where a document is split every N characters or tokens, is simple but often ineffective. It can cut sentences in half or separate a statement from its crucial context.

- **Semantic Chunking:** This approach splits the text based on topic shifts. It analyzes the semantic similarity between adjacent sentences and creates a new chunk when the topic changes, ensuring that each chunk is internally coherent. For example, instead of splitting a "Reimbursements" section in a handbook, it keeps the entire section together, preserving all the rules and limits [[13]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a).
- **Layout-Aware Chunking:** For documents with complex structures like PDFs, which contain tables, headers, and images, layout-aware chunking is essential. It parses the document's visual structure to keep related elements together. For a pricing table, this strategy ensures that each row (product, price, discount) remains intact, rather than being arbitrarily split by a character count. However, even advanced strategies can fail with noisy enterprise documents. Scanned PDFs with multi-column layouts, tables, and code blocks often break sentence-based parsers, leading to chunks that are meaningless without their original visual structure [[21]](https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/).

### GraphRAG

GraphRAG introduces knowledge graphs into the retrieval process. This technique excels at answering questions about complex relationships and interconnected entities, which are often lost in standard document chunks. It builds a graph where nodes represent entities (like people, products, or companies) and edges represent the relationships between them [[5]](https://arxiv.org/html/2404.16130).

This structured representation allows the system to perform multi-hop reasoning. For example, in a retail context, to answer, "Which shoes get the most size-related returns and were featured in last month’s ads?", the system can traverse the graph: from return records to the reason "sizing," to the specific shoe models, and then to the marketing calendar to see which of those were advertised. Similarly, in IT operations, a query like "Which incidents were caused by weekend deploys that also touched the login service?" can be answered by linking change records to deploy times, affected services, and incident tickets [[17]](https://arxiv.org/html/2601.03014v1). This uncovers insights that would be nearly impossible to find with simple chunk-based retrieval. This approach builds on decades of research from the Semantic Web, which aimed to create structured, machine-readable knowledge [[22]](https://www.puppygraph.com/blog/knowledge-graph-vs-rag). While powerful, GraphRAG introduces significant computational complexity. Building the graph via LLM-based triple extraction is expensive, and querying large graphs can lead to a "subgraph explosion," where traversal latency exceeds production thresholds without careful pruning and optimization [[23]](https://dev.to/sreeni5018/from-rag-to-knowledge-graphs-why-the-agent-era-is-redefining-ai-architecture-3fgc).

These techniques increase retrieval quality. Next, we will see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored the ReAct framework, where an agent cycles through a loop of Thought, Action, and Observation. Agentic RAG is the practical application of this concept, where a ReAct-style agent is equipped with a retrieval tool. The agent can reason about when it has a knowledge gap and decide to call its RAG tool to find the answer.

It is important to clarify that agents typically use many tools, such as web search, code execution, and database queries. Labeling an entire system "agentic RAG" can be too narrow, as the retrieval tool is just one of several capabilities the agent possesses. The real shift is that retrieval becomes a component within a broader, more intelligent system.

The core distinction between standard and agentic RAG is the shift from a linear workflow to an adaptive, iterative process.

- **Standard RAG** is a pre-determined workflow. Every query follows the same path of Retrieve → Augment → Generate. It is powerful but rigid.
- **Agentic RAG** is dynamic. The agent decides *when* to retrieve, *what* to retrieve, and whether one retrieval is enough. Retrieval is no longer a mandatory first step but a tool to be used intelligently.

This shift is critical because RAG is fundamentally a read-only system for static data, not a read-write memory system for evolving state. Using RAG as memory leads to failures like context pollution from outdated information [[24]](https://xtrace.ai/blog/rag-vs-long-term-memory-ai-agents).

This agentic approach unlocks several new capabilities. The agent can use its RAG tool **iteratively**, refining queries based on initial results. It can **choose** which knowledge source to search, like selecting `search_incident_runbooks` over `search_marketing_pages` for an outage. It can also **fuse** retrieved internal data with information from other tools, like a live web search, to form a comprehensive answer. Finally, it can decide to **update** the knowledge base, a concept tied to agent memory that we will cover in the next lesson.

Let's consider a conceptual thought process for an agent handling a complex query:

> **Thought:** The user is asking about "2024 EU data retention rules." Our internal policy document is from 2023, so it is likely outdated.
>
> **Action:** `retrieve(internal_policy, query="EU data retention 2024")`
>
> **Observation:** The retrieved document mentions amendments but is missing specific citations for the 2024 changes.
>
> **Thought:** I need external verification to provide a complete and accurate answer.
>
> **Action:** `web_search(query="EU data retention rules 2024 official directive")`
>
> **Observation:** The web search found the official directive with the latest updates.
>
> **Thought:** Now I have both the internal context and the latest external information. I can synthesize them, highlight the changes from 2023, and cite both sources.

This transforms the interaction from a simple database lookup into a conversation with a knowledgeable research assistant.

Image 4: A conceptual Mermaid diagram showing an agent's main loop, including thought, action, tool usage, observation, and final answer.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

In this lesson, we have journeyed from the fundamentals of RAG to the advanced and agentic patterns that define modern AI systems. We have seen that RAG is the most widely used solution to the LLM knowledge problem, that advanced techniques are essential for production-grade quality, and that the future of knowledge retrieval is agentic. By grounding LLMs in external, verifiable data, RAG helps reduce hallucinations, enables customization with proprietary information, and builds user trust through source-based answers.

RAG is not a niche skill but a foundational competency for any AI Engineer. It is a core discipline within the broader practice of context engineering. As you build more complex applications, you will find that mastering these retrieval patterns is key to creating AI that is not just intelligent, but also reliable and trustworthy. This is why we dedicated an entire lesson to it, and why you will see these patterns appear again and again throughout the course.

In our next lesson, we will explore Memory for Agents, and see how short-term and long-term memory systems complement the retrieval capabilities we have discussed here. We will also cover other critical topics later in the course, such as how to build robust evaluation pipelines for retrieval quality and how to monitor these systems in production.

## References

- [1] What Is Retrieval-Augmented Generation, aka RAG? (https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [2] A Complete Guide to RAG (https://towardsai.net/p/l/a-complete-guide-to-rag)
- [3] Retrieval-Augmented Generation (RAG) Fundamentals First (https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search)
- [4] Your RAG is wrong: Here's how to fix it (https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search)
- [5] From Local to Global: A GraphRAG Approach to Query-Focused Summarization (https://arxiv.org/html/2404.16130)
- [6] Introducing Contextual Retrieval (https://www.anthropic.com/news/contextual-retrieval)
- [7] What is Agentic RAG (https://weaviate.io/blog/what-is-agentic-rag)
- [8] RAG is dead, long live agentic retrieval (https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
- [9] What is agentic RAG? (https://www.ibm.com/think/topics/agentic-rag)
- [10] Build advanced retrieval-augmented generation systems (https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
- [11] The Rise of RAG (https://highlearningrate.substack.com/p/the-rise-of-rag)
- [12] Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation (https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [13] Improve Your RAG Accuracy With A Smarter Chunking Strategy (https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a)
- [14] How RAG Works (https://newsletter.systemdesign.one/p/how-rag-works)
- [15] Advanced RAG Retrieval: Cross-Encoders & Reranking (https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [16] Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop (https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [17] SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering (https://arxiv.org/html/2601.03014v1)
- [18] The Evolution of RAG: How Retrieval-Augmented Generation is Transforming Enterprise AI (https://www.arionresearch.com/blog/uuja2r7o098i1dvr8aagal2nnv3uik)
- [19] RAG techniques (https://www.ibm.com/think/topics/rag-techniques)
- [20] Building Hybrid Search for RAG: Combining pgvector and Full-Text Search with Reciprocal Rank Fusion (https://dev.to/lpossamai/building-hybrid-search-for-rag-combining-pgvector-and-full-text-search-with-reciprocal-rank-fusion-6nk)
- [21] Your Chunks Failed Your RAG in Production (https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/)
- [22] Knowledge Graph vs RAG: The Future of AI is a Hybrid (https://www.puppygraph.com/blog/knowledge-graph-vs-rag)
- [23] From RAG to Knowledge Graphs: Why the Agent Era is Redefining AI Architecture (https://dev.to/sreeni5018/from-rag-to-knowledge-graphs-why-the-agent-era-is-redefining-ai-architecture-3fgc)
- [24] Beyond RAG: Why AI Agents Need Long-Term Memory, Not Retrieval (https://xtrace.ai/blog/rag-vs-long-term-memory-ai-agents)
- [25] Implementing Semantic Search for Retrieval (https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)
- [26] Retrieval-Augmented Generation (RAG) Explained (https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/)
- [27] RAG Pipeline Deep Dive: Ingestion (Chunking, Embedding) and Vector Search (https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)
- [28] Optimize RAG with Hybrid Search (https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid)
- [29] Query Decomposition (https://docs.nvidia.com/rag/latest/query_decomposition.html)