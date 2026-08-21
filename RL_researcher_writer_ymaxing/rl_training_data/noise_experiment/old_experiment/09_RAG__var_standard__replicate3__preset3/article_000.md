# Lesson 9: Retrieval-Augmented Generation

In our previous lessons, we have built a solid foundation in AI Engineering. We have explored the agent landscape, distinguished between LLM workflows and autonomous agents, and, in Lesson 3, we covered context engineering—the art of managing the information an LLM sees. We have also learned how to get structured data out of models, give them tools to perform actions, and implement reasoning loops like ReAct.

A core problem we have touched on is that LLMs are trained on a fixed dataset. Their knowledge is static, making them prone to hallucination. During training, they are essentially taking a "closed-book exam" on the world's information. We do not yet have techniques that allow models to continuously learn new information after deployment in the same way humans do. While we can fine-tune them, this process is slow, expensive, and creates yet another static snapshot.

This is where Retrieval-Augmented Generation (RAG) becomes a powerful and reliable solution. Instead of trying to bake new knowledge into the model's weights, we can insert it directly into the context window at inference time. With RAG, we are giving the LLM an "open-book exam." Just as a person does not need to memorize every fact, an LLM can use external documents, manuals, or databases as a reference. This approach, a key method within the context engineering discipline we covered in Lesson 3, allows us to ground LLM responses in verifiable, up-to-date information.

This approach has rapidly evolved. The initial, straightforward method—often called "naive RAG"—has given way to more sophisticated techniques that address its limitations [[18]](https://www.arionresearch.com/blog/uuja2r7o098i1dvr8aagal2nnv3uik), [[19]](https://www.ibm.com/think/topics/rag-techniques). In this lesson, we will explore the "what" and "how" of RAG, starting with its fundamental components and moving toward the advanced and agentic patterns that power modern AI systems. We will also see how retrieval complements an agent's memory, a topic we will explore further in Lesson 10.

## The RAG System: Core Components

Understanding the core components of RAG is the first step in the context engineering process of designing an effective system. At its heart, RAG is built on three conceptual pillars: Retrieval, Augmentation, and Generation.

**Retrieval** is the engine responsible for finding relevant information. When a user submits a query, the retrieval system searches an external knowledge base to find documents or data snippets that are most likely to contain the answer. This search is often powered by semantic similarity, where the meaning of the query is matched against the meaning of the documents. This is made possible by vector embeddings—numerical representations of text—stored in a specialized vector database that allows for efficient searching.

**Augmentation** is the process of taking the retrieved information and preparing it for the LLM. The system combines the original user query with the relevant data snippets it found. This combined text, or "augmented prompt," provides the LLM with the necessary context to formulate a grounded and accurate response.

**Generation** is the final step. The augmented prompt is sent to an LLM, which uses its reasoning capabilities to synthesize an answer based on the provided context. Instead of relying on its static, internal knowledge, the model generates a response that is directly informed by the retrieved data.

Image 1: A flowchart illustrating the core components and data flow of a Retrieval Augmented Generation (RAG) system.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow is split into two distinct phases: an offline ingestion pipeline that prepares the knowledge base, and an online retrieval pipeline that answers user queries in real-time.

### Phase 1: Offline Ingestion & Indexing

This phase happens before your users ever ask a question. Its goal is to process your raw documents and index them for efficient retrieval.

- **Load:** The first step is to load your documents from their various sources. These can be PDFs, websites, databases, or APIs. Tools like LangChain's document loaders or LlamaIndex's readers can connect to almost any data source.
- **Split:** Since LLMs have limited context windows, you cannot feed them entire documents at once. The documents are broken down into smaller, semantically meaningful pieces called chunks. This can be done with simple rule-based splitters, like LangChain’s `RecursiveCharacterTextSplitter`, or more advanced semantic chunkers that avoid splitting a coherent thought in the middle.
- **Embed:** Each chunk of text is then converted into a vector embedding using an embedding model. These high-dimensional vectors capture the semantic meaning of the text. Popular models for this task include OpenAI’s `text-embedding-3` series, Google's `text-embedding-004`, and various open-source models available through Hugging Face.
- **Store:** Finally, the vector embeddings and their corresponding text chunks are loaded into a vector database. This specialized database, such as FAISS, Milvus, Qdrant, or Pinecone, is optimized for fast similarity searches, allowing the system to quickly find the most relevant chunks for a given query.

### Phase 2: Online Retrieval & Generation

This phase is triggered when a user interacts with your application.

- **Query:** The user asks a question. This query can be optionally pre-processed to normalize it or expand it for better results.
- **Embed:** The user's query is converted into a vector embedding using the exact same embedding model that was used during the ingestion phase. This is critical to ensure that the query and the documents exist in the same vector space.
- **Search:** The system uses the query vector to search the vector database. It performs a similarity search (like cosine similarity) to find the top-k document chunks whose embeddings are closest to the query's embedding.
- **Generate:** The retrieved chunks are assembled into a prompt along with the original user query and specific instructions. This augmented prompt is then passed to an LLM, which generates a final answer grounded in the provided context. To ensure reliability, we can use the structured output techniques from Lesson 4 to format the answer and include citations.

Image 2: A detailed Mermaid diagram depicting the end-to-end RAG workflow, split into two distinct phases: "Offline Ingestion & Indexing" and "Online Retrieval & Generation".

With the end-to-end path in place, the next question is quality. What are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

A basic RAG pipeline is a great start, but production systems often require more sophisticated techniques to achieve high accuracy. These advanced methods focus on improving the quality of the retrieval step, ensuring the LLM receives the most relevant and precise context possible.

### Hybrid Search

Hybrid search combines the strengths of traditional keyword-based search (like BM25) with modern vector search. While vector search is excellent at understanding semantic meaning and finding conceptually related documents, it can sometimes miss exact keyword matches for specific terms, names, or codes. BM25, on the other hand, excels at this.

For example, in a customer support scenario, a user might ask, "My bill keeps rolling over." A keyword search would find articles containing the exact term "rollover." A vector search might also surface guides about "carryover balance," capturing the user's intent even with different wording. A hybrid approach uses both, ensuring comprehensive coverage. A common technique to combine these different result sets is Reciprocal Rank Fusion (RRF). RRF elegantly merges ranked lists without needing to normalize their scores, which often operate on completely different scales. It calculates a new score based on the reciprocal of each document's rank in each list, effectively giving more weight to documents that appear high up in multiple search results [[20]](https://dev.to/lpossamai/building-hybrid-search-for-rag-combining-pgvector-and-full-text-search-with-reciprocal-rank-fusion-6nk).

Image 3: A Mermaid diagram illustrating the hybrid retrieval flow.

### Re-ranking

Re-ranking introduces a second, more precise model to refine the initial search results. The first retrieval step is optimized for speed and recall, casting a wide net to find a set of potentially relevant documents. However, the best document might not always be at the top of this initial list.

A re-ranker, often a cross-encoder model, takes the user's query and each retrieved document as a pair and calculates a more accurate relevance score. This allows it to understand the nuances of the relationship between the query and the document. For instance, if a user searches "how to connect my account," a re-ranker can push a step-by-step setup guide to the top, above a less relevant press release or a tangentially related community forum thread.

### Query Transformations

Sometimes, the user's original query is not the best one for searching your knowledge base. Query transformation techniques rewrite or decompose the query to improve retrieval accuracy.

- **Decomposition:** This method breaks down a complex, multi-part question into several simpler sub-questions. For example, the query "What’s our travel policy for conferences in Europe this year?" could be decomposed into: (1) "What is the company travel policy?", (2) "What are the rules for conferences?", (3) "Are there specific rules for Europe?", and (4) "What has changed in the policy this year?". The system retrieves documents for each sub-question and then synthesizes the answers.
- **Hypothetical Document Embeddings (HyDE):** This technique uses an LLM to generate a hypothetical, ideal answer to the user's query *before* searching. For a query about conference travel, the system might generate a short paragraph like: "Employees attending approved conferences in Europe can book economy flights and stay in hotels up to three nights, with daily meal limits." It then creates an embedding of this hypothetical answer and uses it to search for real documents that are semantically similar, which often leads to more relevant results.

### Advanced Chunking Strategies

How you split your documents into chunks has a massive impact on retrieval quality. Naive fixed-size chunking, where a document is split every N characters or tokens, is simple but often ineffective. It can cut sentences in half or separate a statement from its crucial context.

- **Semantic Chunking:** This approach splits the text based on topic shifts. It analyzes the semantic similarity between adjacent sentences and creates a new chunk when the topic changes, ensuring that each chunk is internally coherent. For example, instead of splitting a "Reimbursements" section in a handbook, it keeps the entire section together, preserving all the rules and limits.
- **Layout-Aware Chunking:** For documents with complex structures like PDFs, which contain tables, headers, and images, layout-aware chunking is essential. It parses the document's visual structure to keep related elements together. For a pricing table, this strategy ensures that each row (product, price, discount) remains intact, rather than being arbitrarily split by a character count. However, even advanced strategies can fail with noisy enterprise documents. Scanned PDFs with multi-column layouts, tables, and code blocks often break sentence-based parsers, leading to chunks that are meaningless without their original visual structure [[21]](https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/).

### GraphRAG

GraphRAG introduces knowledge graphs into the retrieval process. This technique excels at answering questions about complex relationships and interconnected entities, which are often lost in standard document chunks. It builds a graph where nodes represent entities (like people, products, or companies) and edges represent the relationships between them.

This structured representation allows the system to perform multi-hop reasoning. For example, to answer, "Which shoes get the most size-related returns and were featured in last month’s ads?", the system can traverse the graph: from return records to the reason "sizing," to the specific shoe models, and then to the marketing calendar to see which of those were advertised. This uncovers insights that would be nearly impossible to find with simple chunk-based retrieval. This approach builds on decades of research from the Semantic Web, which aimed to create structured, machine-readable knowledge [[22]](https://www.puppygraph.com/blog/knowledge-graph-vs-rag). While powerful, GraphRAG introduces significant computational complexity. Building the graph via LLM-based triple extraction is expensive, and querying large graphs can lead to a "subgraph explosion," where traversal latency exceeds production thresholds without careful pruning and optimization [[23]](https://dev.to/sreeni5018/from-rag-to-knowledge-graphs-why-the-agent-era-is-redefining-ai-architecture-3fgc).

These techniques increase retrieval quality. Next, we will see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored the ReAct framework, where an agent cycles through a loop of Thought, Action, and Observation. Agentic RAG is the practical application of this concept, where a ReAct-style agent is equipped with a retrieval tool. The agent can reason about when it has a knowledge gap and decide to call its RAG tool to find the answer.

The core distinction between standard and agentic RAG is the shift from a linear workflow to an adaptive, iterative process.

- **Standard RAG** is a pre-determined workflow: every query follows the same path of Retrieve → Augment → Generate. It is powerful but rigid.
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

RAG is not a niche skill but a foundational competency for any AI Engineer. It is a core discipline within the broader practice of context engineering. As you build more complex applications, you will find that mastering these retrieval patterns is key to creating AI that is not just intelligent, but also reliable and trustworthy.

In our next lesson, we will explore Memory for Agents, and see how short-term and long-term memory systems complement the retrieval capabilities we have discussed here. We will also cover other critical topics later in the course, such as how to build robust evaluation pipelines for retrieval quality and how to monitor these systems in production.

## References

- [1] [What Is Retrieval-Augmented Generation, aka RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [2] [A Complete Guide to RAG](https://towardsai.net/p/l/a-complete-guide-to-rag)
- [3] [Retrieval-Augmented Generation (RAG) Fundamentals First](https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search)
- [4] [Your RAG is wrong: Here's how to fix it](https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search)
- [5] [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/html/2404.16130)
- [6] [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- [7] [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag)
- [8] [RAG is dead, long live agentic retrieval](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
- [9] [What is agentic RAG?](https://www.ibm.com/think/topics/agentic-rag)
- [10] [Build advanced retrieval-augmented generation systems](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
- [11] [The Rise of RAG](https://highlearningrate.substack.com/p/the-rise-of-rag)
- [12] [Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [13] [Improve Your RAG Accuracy With A Smarter Chunking Strategy](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a)
- [14] [How RAG Works - by Neo Kim and Eric Roby](https://newsletter.systemdesign.one/p/how-rag-works)
- [15] [Advanced RAG Retrieval: Cross-Encoders & Reranking | Towards Data Science](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [16] [Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop | Towards Data Science](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [17] [SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering](https://arxiv.org/html/2601.03014v1)
- [18] [The Evolution of RAG: From Naive to Advanced Architectures](https://www.arionresearch.com/blog/uuja2r7o098i1dvr8aagal2nnv3uik)
- [19] [RAG techniques](https://www.ibm.com/think/topics/rag-techniques)
- [20] [Building Hybrid Search for RAG combining pgvector and Full-Text Search with Reciprocal Rank Fusion](https://dev.to/lpossamai/building-hybrid-search-for-rag-combining-pgvector-and-full-text-search-with-reciprocal-rank-fusion-6nk)
- [21] [Your Chunks Failed Your RAG in Production](https://towardsdatascience.com/your-chunks-failed-your-rag-in-production/)
- [22] [Knowledge Graph vs. RAG: A Deep Dive](https://www.puppygraph.com/blog/knowledge-graph-vs-rag)
- [23] [From RAG to Knowledge Graphs: Why the Agent Era is Redefining AI Architecture](https://dev.to/sreeni5018/from-rag-to-knowledge-graphs-why-the-agent-era-is-redefining-ai-architecture-3fgc)
- [24] [Beyond RAG: Why AI Agents Need Long-Term Memory, Not Retrieval](https://xtrace.ai/blog/rag-vs-long-term-memory-ai-agents)