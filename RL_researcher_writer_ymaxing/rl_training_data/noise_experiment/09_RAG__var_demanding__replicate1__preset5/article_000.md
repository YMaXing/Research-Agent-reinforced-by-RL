# Lesson 9: Retrieval-Augmented Generation

In our course so far, we have explored the landscape of AI Engineering, distinguished between LLM workflows and agents, and in Lesson 3, we covered Context Engineering—the art of managing information flow to an LLM. We have also built agents that can reason and use tools. Now, we will tackle one of the most critical challenges in building knowledgeable AI systems: giving them access to information beyond their training data.

LLMs are trained on a fixed dataset, which means their knowledge is static and can become outdated. When you ask an LLM a question, it is essentially taking a "closed-book exam" on the world's information as it existed at one point in time. This leads to two major problems: knowledge cutoffs and hallucinations.

You could try to solve this by continuously fine-tuning the model with new data. However, fine-tuning is resource-heavy and slow. It requires curating large datasets and can take days to complete. It also risks "catastrophic forgetting," where the model loses previously learned information. Another approach is to stuff all the information into the LLM's context window. But even with massive context windows, this is not a scalable solution. It is expensive, slow, and suffers from the "lost in the middle" problem, where the model struggles to recall information buried in a long prompt.

This phenomenon is not just an anecdotal failure but a well-documented positional bias. Research from Stanford, UC Berkeley, and Samaya AI in their 2023 paper, "Lost in the Middle," demonstrated a distinct U-shaped performance curve. Models are most effective at using information placed at the very beginning or end of their context window, while their accuracy plummets when critical details are buried in the middle. This effect is surprisingly similar to the serial-position effect in human psychology, where we tend to remember the first (primacy) and last (recency) items in a list best [[53]](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf).

This is where Retrieval-Augmented Generation (RAG) comes in. RAG is a reliable solution that gives the LLM an "open-book exam" by connecting it to external, real-time knowledge sources. Instead of forcing the model to memorize everything, we give it the ability to look things up, just like a human using a cheat sheet or a procedures manual. RAG is a core technique within the discipline of Context Engineering we introduced in Lesson 3, focusing on curating the context fed to an LLM.

This lesson will guide you through the fundamentals of RAG, from its core components to the advanced and agentic patterns used in production systems. You will learn the "what" and "how" of building RAG pipelines that make your AI applications grounded, trustworthy, and knowledgeable. We will also briefly touch on how retrieval complements an agent's memory, a topic we will explore in-depth in Lesson 10. With the problem and motivation clear, we will first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of a RAG system is the first step in the Context Engineering process of designing effective AI applications. At a high level, RAG can be broken down into three conceptual pillars: Retrieval, Augmentation, and Generation.

Image 1: A flowchart illustrating the core components and information flow of a Retrieval Augmented Generation (RAG) system.

### Retrieval

Retrieval is the engine for finding relevant information. When a user submits a query, the retrieval system searches an external knowledge base to find documents or data snippets that are most relevant to the user's intent. The most common method for this is semantic search, which goes beyond simple keyword matching to understand the meaning behind the query.

This is made possible by vector embeddings. Vector embeddings are numerical representations of text, images, or other data, where similar concepts are located closer to each other in a high-dimensional space. During the data preparation phase, documents are split into chunks, and an embedding model converts each chunk into a vector. These vectors are then stored in a specialized database called a vector database, which is optimized for fast similarity searches [[51]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval). At query time, the user's query is also converted into a vector using the same embedding model. The system then searches the vector database to find the chunk embeddings that are "closest" to the query embedding, typically using a distance metric like cosine similarity [[54]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).

### Augmentation

Augmentation is the process of taking the retrieved information and preparing it for the LLM. Once the top-k most relevant chunks are identified, they are combined with the original user query to form an "augmented prompt."

This step is a form of prompt engineering. The goal is to structure the prompt in a way that clearly separates the user's question from the retrieved context. A common practice is to use a template that instructs the LLM to use the provided information to answer the question. For example, the prompt might look something like this: "Using the context below, answer the question. If the context does not contain the answer, say so. CONTEXT: <retrieved document excerpts> QUESTION: <user query>" [[56]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/). This ensures the model gives weight to the retrieved context and helps prevent it from relying on its internal, potentially outdated knowledge.

### Generation

Generation is the final step, where the LLM uses the augmented prompt to produce a response. The model synthesizes the information from the retrieved chunks to generate an answer that is grounded in the provided data. Because the answer is based on specific, citable sources, this process significantly reduces the risk of hallucination and increases user trust.

The generated response can also be formatted to include citations that link back to the original source documents, allowing users to verify the information for themselves. This traceability is a key advantage of RAG over other methods.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

The end-to-end RAG workflow can be divided into two distinct phases: an offline ingestion and indexing phase, where the knowledge base is prepared, and an online retrieval and generation phase, where user queries are answered in real-time.

Image 2: A detailed Mermaid diagram depicting the end-to-end RAG workflow, clearly separating the offline ingestion and indexing phase from the online retrieval and generation phase.

### Phase 1: Offline Ingestion & Indexing

This phase is all about preparing your data to be searchable. It is a multi-step process that you run before your application is live, and you repeat it whenever your knowledge base needs to be updated [[32]](https://newsletter.systemdesign.one/p/how-rag-works).

1.  **Load:** The first step is to load your documents. These can come from various sources, such as PDFs, websites, databases, or APIs. The main challenge here is handling diverse formats and extracting clean text. Tools like Unstructured, LangChain's document loaders, and LlamaIndex's readers are commonly used for this purpose.
2.  **Split:** Once the documents are loaded, they are broken down into smaller, more manageable pieces called chunks. This is a crucial step because you want each chunk to be a semantically meaningful unit of information. Simply splitting by a fixed number of characters can cut a sentence or idea in half, which hurts retrieval quality. More advanced strategies use recursive character splitting, which respects paragraph and sentence boundaries, or even semantic chunking, which splits text based on topic shifts.
3.  **Embed:** Next, each chunk is converted into a vector embedding using an embedding model. These models, such as OpenAI's `text-embedding-3-small`, Google's `text-embedding-004`, or open-source variants from Hugging Face, are trained to capture the semantic meaning of text in a dense vector. The choice of embedding model can have a significant impact on the quality of your retrieval system.
4.  **Store:** Finally, the embeddings and their corresponding text chunks are stored in a vector database. This database indexes the vectors for efficient similarity search. Popular options range from local libraries like FAISS for quick prototyping to scalable, production-ready solutions like Milvus, Qdrant, Pinecone, and vector search capabilities in traditional search engines like Elasticsearch.

### Phase 2: Online Retrieval & Generation

This phase happens in real-time, whenever a user interacts with your application.

1.  **Query:** The process starts when a user asks a question. This query can be pre-processed to normalize it or expand it with additional context, but at its core, it is the input that drives the retrieval process.
2.  **Embed:** The user's query is then converted into a vector using the exact same embedding model that was used during the ingestion phase. This is critical to ensure that the query and the document chunks are in the same vector space, allowing for a meaningful comparison.
3.  **Search:** The query vector is used to search the vector database. The database performs a similarity search (e.g., cosine similarity) to find the top-k most similar document chunks. This step leverages the power of the indexed vectors to quickly find content that is semantically related to the query, even if the exact keywords are not present.
4.  **Generate:** The retrieved chunks are then used to augment the user's query in a prompt that is sent to an LLM. As we discussed in Lesson 4, you can use structured outputs to format the final answer, ensuring it is consistent and easy to parse. A well-designed prompt will instruct the LLM to synthesize the information from the chunks and generate a grounded answer, complete with citations pointing back to the source documents.

For production systems, verifiability is non-negotiable. The format of your citations directly impacts grounding effectiveness. You must ensure the way you mark up documents in the context (e.g., `[Document 1]: ...`) matches the citation format you ask for in the output. Using structured formats like XML tags or clear delimiters helps the model distinguish document boundaries and reduces citation errors. This isn't just about formatting; it's about building a traceable chain of evidence from the generated claim back to the source text [[54]](https://mbrenndoerfer.com/writing/rag-prompt-engineering-context-citations).

With the end-to-end path in place, the next question is quality: what are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While the vanilla RAG pipeline is a good starting point, production-grade systems often require more sophisticated techniques to achieve high accuracy. These advanced methods address the limitations of simple semantic search and help the system handle complex, real-world data.

Image 3: Mermaid diagram illustrating the hybrid retrieval flow.

### Hybrid Search

Hybrid search combines the strengths of traditional keyword-based search (like BM25) with modern vector search. Keyword search excels at finding exact matches for specific terms, acronyms, or IDs, while vector search is better at understanding the semantic meaning and context of a query.

For example, in a customer support scenario, if a user searches for "Error code TS-999," a keyword search will pinpoint the exact document that mentions this code. A vector search might return general articles about error codes but miss the specific one. By combining both, you get the best of both worlds: the precision of keyword search and the contextual understanding of semantic search [[38]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid). The results from both searches are typically combined and re-ranked to produce a final, more relevant set of documents.

However, hybrid search is not a silver bullet, especially with ambiguous enterprise queries. It can fail if the user's vocabulary doesn't match the document (e.g., "annual leave" vs. "vacation policy") or when exact identifiers like product codes are missed by the semantic search component and keyword search lacks context. Without proper tuning and domain-specific optimization, hybrid systems can inherit the weaknesses of both methods [[55]](https://wearefram.com/blog/enterprise-rag/).

### Re-ranking

Re-ranking introduces a second stage to the retrieval process to improve the relevance of the retrieved documents. After an initial retrieval step fetches a larger set of candidate documents (e.g., the top 50-100), a more powerful but slower model, called a re-ranker, is used to score and re-order these candidates.

Unlike the initial retrieval, which compares the query and documents independently, re-rankers like cross-encoders process the query and each document together. This allows for a deeper, more contextual assessment of relevance [[42]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/). For a query like "how to connect my account," a re-ranker can prioritize a step-by-step guide over a press release that happens to mention similar keywords, ensuring the most useful information is at the top.

### Query Transformations

Sometimes, the user's original query is not the best one for retrieval. Query transformation techniques modify the query to improve its chances of finding the right information.

-   **Decomposition:** This technique breaks down a complex, multi-part question into several smaller, simpler sub-queries. For example, the question "What’s our travel policy for conferences in Europe this year?" could be decomposed into "What is the travel policy?", "What are the rules for conferences?", and "What are the specific rules for Europe in 2024?". The system retrieves documents for each sub-query and then synthesizes the results to form a comprehensive answer [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html).
-   **Hypothetical Document Embeddings (HyDE):** HyDE takes a creative approach by first asking an LLM to generate a hypothetical, ideal answer to the user's query. This hypothetical document is then converted into an embedding and used for the search. The idea is that this "perfect" answer is more likely to be semantically similar to the actual relevant documents than the original, often short and ambiguous, query [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/). While effective, this hypothetical step comes at a significant performance cost. Benchmarks on large-scale datasets have shown that HyDE can increase query latency by over 40%, making it a trade-off between retrieval quality for ambiguous queries and the speed required for real-time applications [[56]](https://arxiv.org/pdf/2506.21568).

### Advanced Chunking Strategies

The way you split your documents into chunks has a massive impact on retrieval quality. Moving beyond naive fixed-size chunking is one of the most effective ways to improve your RAG system.

-   **Semantic Chunking:** Instead of splitting by a fixed number of tokens, semantic chunking splits the text based on topic shifts. It uses embeddings to measure the semantic distance between sentences and creates a new chunk when the topic changes. This ensures that each chunk is a coherent, self-contained unit of information [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a).
-   **Layout-Aware Chunking:** For documents with complex structures like PDFs, financial reports, or scientific papers, layout-aware chunking is essential. This method parses the document to identify structural elements like headers, tables, lists, and figures, and then chunks the document intelligently around these boundaries. For example, it ensures that a table and its title are kept together, preventing context loss [[17]](https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a).
-   **Context-Enriched Chunking:** This technique, also known as contextual retrieval, adds a summary of the surrounding context to each chunk before embedding it. For a sentence like "The company's revenue grew by 3%," the context might add "This chunk is from an SEC filing on ACME Corp's performance in Q2 2023." This extra information makes the chunk's embedding more precise and easier to retrieve accurately.
-   **Parent Document Retrieval (Hierarchical Chunking):** This strategy directly addresses the tension between retrieval precision and generation context. It involves indexing small, precise child chunks (like a single paragraph) but linking them to their larger parent document (like a full page or section). At query time, the system fetches the specific child chunk but provides the entire parent chunk to the LLM. This gives you the best of both worlds: the targeted accuracy of small chunks for search and the complete context of a larger document for generation [[57]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/).

### GraphRAG

GraphRAG introduces a powerful new dimension to retrieval by using knowledge graphs. Instead of treating documents as isolated chunks of text, GraphRAG extracts entities and their relationships to build a structured graph of the knowledge base. This approach excels at answering multi-hop questions that require reasoning across multiple documents or data points [[46]](https://arxiv.org/html/2601.03014v1).

For example, to answer "Which shoes get the most size-related returns and were featured in last month’s ads?", a GraphRAG system can traverse the graph from "returns" to "sizing issues," connect to specific shoe models, and then link those models to the "marketing calendar," pulling together information that would be scattered and disconnected in a standard vector search. However, this power comes with computational trade-offs. Building and maintaining the graph is more complex than a simple vector index, and for large, static datasets, the pre-computation of summaries can be slow and resource-intensive [[58]](https://www.techment.com/blogs/rag-optimization-techniques-production-ai/). The real advantage emerges with dynamic data. Systems like Zep AI's Graphiti use a temporally-aware knowledge graph that can be updated incrementally in real-time, avoiding the need to recompute the entire graph when new information arrives [[59]](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/).

### Metadata Filtering

One of the most practical and powerful techniques in production is metadata filtering. When documents are chunked, you can attach metadata to each chunk, such as the source document, creation date, author, department, or policy version. During retrieval, you can use this metadata to pre-filter the search space before performing the vector search.

This is especially useful for handling temporal queries. If a user asks, "What changed between March and June 2025?", you can filter for chunks with an `effective_date` within that range. This drastically narrows down the search and improves the relevance of the results. You can even implement bitemporal logic, filtering by both the `effective_date` (when the information was valid) and the `indexed_at` date (when it was added to the system) to manage evolving and historical data accurately. For example, some advanced knowledge graphs implement this by attaching explicit validity intervals (e.g., `t_valid`, `t_invalid`) to every relationship, allowing the system to reconstruct the state of knowledge at any point in time and resolve version conflicts without discarding historical data [[59]](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/).

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored the ReAct framework, where an agent cycles through Thought, Action, and Observation to solve problems. Agentic RAG is the application of this framework to information retrieval. It transforms RAG from a rigid, linear pipeline into an adaptive, iterative process where a ReAct-style agent is equipped with a retrieval tool.

The agent's toolkit can include many tools, such as web search, code execution, or database queries. The RAG tool, which accesses your internal knowledge base, is just one of these. This framing is important—labeling an entire system "agentic RAG" can be too narrow. It is more accurate to think of it as an agent that *uses* RAG.

Image 4: A conceptual Mermaid diagram illustrating an agent's main loop, demonstrating its iterative reasoning and ability to choose between various tools.

### Standard RAG vs. Agentic RAG

The core distinction lies in the control flow.

-   **Standard RAG** is a pre-determined, linear workflow: Retrieve → Augment → Generate. Every query follows this exact path. It is powerful but inflexible. If the initial retrieval fails to find the right information, the system has no way to recover [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).
-   **Agentic RAG** is an adaptive control loop. The agent decides *when* to retrieve, *what* to search for, *which* source to use, and whether one retrieval is enough. It can reason about the information it finds and dynamically adjust its strategy [[12]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/).

### Capabilities of an Agentic Approach

This shift from a fixed pipeline to an agent-driven loop unlocks several powerful capabilities:

-   **Iterative Retrieval:** The agent can use the RAG tool multiple times, refining its query at each step. For instance, an initial query might return a vague policy document. The agent can then generate a more specific query, like "search for policy section on EU customers, 2024 updates," and retrieve again to find the precise details.
-   **Tool Selection:** An agent can choose the right tool for the job. If a query is about a recent public event, it might use a web search tool. If it is about an internal system failure, it will query the incident runbooks via its RAG tool.
-   **Information Fusion:** The agent can combine information from multiple sources. It might retrieve an internal policy using the RAG tool, then use a web search to check for recent regulatory changes, and finally synthesize both pieces of information into a comprehensive answer.
-   **Self-Correction and Reduced Hallucination:** The agent's reasoning loop is also a self-critique mechanism. After a retrieval step, the agent can evaluate the relevance of the information. If the retrieved documents are insufficient or contradictory, it can choose to rewrite its query and try again. This iterative refinement process, sometimes called a reflection pattern, allows the agent to double-check its sources and correct its course, which directly reduces the risk of generating a confident but incorrect answer [[60]](https://wandb.ai/wandb_fc/genai-research/reports/Agentic-RAG-Revolutionizing-AI-with-autonomous-retrieval--VmlldzoxNDIzMjA0MQ).
-   **Knowledge Base Updates:** An agent can even identify gaps or outdated information in the knowledge base and propose updates. This moves toward a system that not only consumes knowledge but also helps maintain it. We will explore this further in Lesson 10 when we discuss memory for agents.

Here is a conceptual thought process for an agent handling a complex query:

**Thought:** "The user is asking about '2024 EU data retention rules.' Our internal policy documents cite the 2023 version. This information is likely outdated."

**Action:** `retrieve(internal_policy, query="EU data retention 2024")`

**Observation:** "The retrieved document mentions amendments but lacks specific citations for the 2024 changes."

**Thought:** "I need to verify this externally."

**Action:** `web_search(query="official EU data retention directive 2024")`

**Observation:** "Found the official directive update on the EU's website."

**Thought:** "Now I can synthesize the internal policy with the official external update, highlight the changes from 2023, and cite both sources."

This is the difference between a simple database lookup and a conversation with a knowledgeable research assistant. The agent does not just fetch data; it reasons about it, verifies it, and synthesizes it to provide a trustworthy answer.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

In this lesson, we have journeyed from the fundamental limitations of LLMs to the sophisticated, agent-driven systems that represent the future of information retrieval. We have established that RAG is the most effective solution to the LLM knowledge problem, providing a way to ground models in factual, up-to-date, and proprietary data. For any AI Engineer, building production-grade quality requires moving beyond naive RAG and embracing advanced techniques like hybrid search, re-ranking, and GraphRAG. The future of knowledge retrieval is agentic, where RAG is not just a pipeline but a dynamic tool wielded by an intelligent agent.

The core benefits of this approach are clear: RAG reduces hallucinations, enables deep customization with private data, and builds user trust by providing verifiable, source-backed answers. These qualities are not just desirable; they are essential in high-stakes domains like healthcare and legal tech, where compliance, liability, and the cost of being wrong demand auditable, evidence-based AI systems [[61]](https://thescimus.com/blog/retrieval-augmented-generation-healthcare-guide/). It is not a niche skill but a foundational competency for the modern AI Engineer, and a critical component of the broader discipline of Context Engineering.

This lesson has set the stage for understanding how agents access external knowledge on demand. In our next lesson, we will explore a complementary concept: Memory for Agents. We will look at how short-term and long-term memory systems allow agents to retain information across interactions, learn from experience, and build a persistent understanding of their environment. While RAG provides the "open-book" for an exam, memory gives the agent the ability to remember what it has learned from previous exams. We will also touch on other important topics later in the course, such as how to build robust evaluation pipelines to measure retrieval quality and how to monitor these systems in production.

## References

- [1]  https://neo4j.com/blog/developer/fine-tuning-vs-rag/
- [2]  https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html
- [3]  https://aclanthology.org/2024.emnlp-main.15.pdf
- [4]  https://arxiv.org/html/2312.05934v3
- [5]  https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0
- [6]  https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/
- [7]  https://qdrant.tech/articles/what-is-rag-in-ai/
- [8]  https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5
- [9]  https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/
- [10]  https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/
- [11]  https://airbyte.com/agentic-data/ai-agent-vs-rag
- [12]  https://domino.ai/blog/rag-vs-agentic-ai
- [13]  https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/
- [14]  https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a
- [15]  https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/
- [16]  https://docs.nvidia.com/rag/latest/query_decomposition.html
- [17]  https://neo4j.com/blog/genai/advanced-rag-techniques/
- [18]  https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5
- [19]  https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/
- [20]  https://humanloop.com/blog/rag-architectures
- [21]  https://www.ibm.com/think/topics/retrieval-augmented-generation
- [22]  https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177
- [23]  https://newsletter.systemdesign.one/p/how-rag-works
- [24]  https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/
- [25]  https://aws.amazon.com/what-is/retrieval-augmented-generation/
- [26]  https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid
- [27]  https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/
- [28]  https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834
- [29]  https://arxiv.org/html/2407.00072v5
- [30]  https://redis.io/blog/10-techniques-to-improve-rag-accuracy/
- [31]  https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag
- [32]  https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/
- [33]  https://arxiv.org/html/2601.03014v1
- [34]  https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf
- [35]  https://atlan.com/know/what-is-graphrag/
- [36]  https://arxiv.org/html/2501.00309v2
- [37]  https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval
- [38]  https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/
- [39]  https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/
- [40]  https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/
- [41]  https://www.promptingguide.ai/research/rag
- [42]  https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/
- [43]  https://towardsai.net/p/l/a-complete-guide-to-rag
- [44]  https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search
- [45]  https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search
- [46]  https://arxiv.org/html/2404.16130
- [47]  https://www.anthropic.com/news/contextual-retrieval
- [48]  https://weaviate.io/blog/what-is-agentic-rag
- [49]  https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval
- [50]  https://www.ibm.com/think/topics/agentic-rag
- [51]  https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation
- [52]  https://highlearningrate.substack.com/p/the-rise-of-rag
- [53]  https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf
- [54]  https://mbrenndoerfer.com/writing/rag-prompt-engineering-context-citations
- [55]  https://wearefram.com/blog/enterprise-rag/
- [56]  https://arxiv.org/pdf/2506.21568
- [57]  https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/
- [58]  https://www.techment.com/blogs/rag-optimization-techniques-production-ai/
- [59]  https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/
- [60]  https://wandb.ai/wandb_fc/genai-research/reports/Agentic-RAG-Revolutionizing-AI-with-autonomous-retrieval--VmlldzoxNDIzMjA0MQ
- [61]  https://thescimus.com/blog/retrieval-augmented-generation-healthcare-guide/