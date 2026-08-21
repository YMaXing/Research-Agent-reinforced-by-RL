# Lesson 9: Retrieval-Augmented Generation

In our previous lessons, we built a solid foundation in AI Engineering. We explored the agent landscape, learned to distinguish between rigid workflows and autonomous agents, and mastered context engineering—the art of feeding LLMs the right information. Now, we will tackle one of the most critical techniques in an AI Engineer's toolkit: Retrieval-Augmented Generation (RAG).

LLMs are trained on a fixed dataset, which means their knowledge is static and they can become prone to hallucination. During their training, they are essentially taking a "closed-book exam" on the world's information. While we can fine-tune them, this process is often inefficient for keeping knowledge current. The ideal solution would be for models to learn continuously from experience, but we are not there yet [[36]](https://neo4j.com/blog/developer/fine-tuning-vs-rag/).

This is where RAG provides a practical and reliable solution. It allows us to give the LLM an "open-book exam" by connecting it to external, real-time knowledge sources through its context window [[1]](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/). Instead of expecting the model to memorize everything, we give it cheat sheets and manuals it can reference on the fly. This approach directly addresses fundamental LLM limitations like knowledge cut-offs and the tendency to invent facts [[57]](https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html).

As we covered in Lesson 3 on Context Engineering, curating what an LLM sees is crucial. RAG is a primary method for achieving this. It grounds the model in factual data, making its responses more accurate and trustworthy. By retrieving specific, relevant information, RAG is more efficient than simply filling a large context window with entire documents, which can be slow and costly [[23]](https://highlearningrate.substack.com/p/the-rise-of-rag).

In our next lesson, we will explore how agent memory complements RAG by providing persistent knowledge stores. For now, let's focus on the retrieval process itself. In this lesson, we will journey from the fundamentals of RAG to the advanced and agentic patterns that power modern AI systems. We will start by breaking down a RAG system into its core components, then examine the end-to-end pipeline, and finally explore the sophisticated techniques that make RAG a production-ready solution.

With the problem and motivation clear, we’ll first decompose RAG into its core components so you can see where each responsibility lives.

## The RAG System: Core Components

Understanding the components of RAG is the first step in the context engineering process of designing effective systems. At its core, a RAG system is built on three conceptual pillars that work together to answer a user's query.

Image 1: A flowchart illustrating the core components of a RAG system.

**Retrieval** is the engine that finds relevant information. When a user asks a question, the retriever searches an external knowledge base to find the most relevant data. This search is often powered by semantic similarity, which uses vector embeddings to find text chunks with similar meanings to the query [[2]](https://towardsai.net/p/l/a-complete-guide-to-rag).

Vector embeddings are numerical representations of text that capture its semantic meaning. An embedding model converts a piece of text into a high-dimensional vector, where similar concepts are located closer to each other in the vector space. These vectors are then stored in a specialized vector database, which is optimized for performing fast and efficient similarity searches [[7]](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/).

**Augmentation** is the process of preparing this retrieved information for the LLM. Once the retriever finds the most relevant document chunks, they are combined with the original user query. This creates an "augmented" prompt that provides the LLM with the necessary context to formulate an accurate answer [[56]](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/). This step is where we inject the external knowledge directly into the model's short-term attention.

**Generation** is the final step, where the LLM produces an answer. The model receives the augmented prompt—containing both the user's question and the retrieved context—and uses this information to generate a response. Because the answer is based on the provided data, it is "grounded," meaning it is less likely to be a hallucination and can often include citations back to the source documents [[3]](https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search).

These three components form a simple but powerful system for enhancing LLM capabilities. They allow the model to access information far beyond its training data, leading to more reliable and up-to-date responses.

Now that you can name each moving part, let’s see how they line up across the two phases of a real system.

## The RAG Pipeline: Ingestion and Retrieval

An end-to-end RAG workflow is composed of two distinct phases: an offline ingestion phase where knowledge is prepared, and an online retrieval phase where answers are generated in real-time [[31]](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177), [[32]](https://newsletter.systemdesign.one/p/how-rag-works).

Image 2: Flowchart of a RAG pipeline showing offline ingestion and online retrieval.

### Phase 1: Offline Ingestion & Indexing

The first phase happens offline, before any user asks a question. Its goal is to process your raw documents and index them in a way that makes them easily searchable. This pipeline is crucial because the quality of your retrieval depends heavily on how well your data is prepared [[8]](https://qdrant.tech/articles/what-is-rag-in-ai/).

The process involves several steps:
1.  **Load:** The pipeline begins by loading documents from various sources. These can be anything from PDFs and web pages to data from APIs. Tools like Unstructured, LangChain's document loaders, or LlamaIndex's readers are commonly used for this step.
2.  **Split:** Since LLMs have a limited context window, large documents are broken down into smaller, more manageable pieces called chunks. This step is critical; a good chunking strategy ensures that semantically related information stays together. Frameworks offer various splitters, such as LangChain’s `RecursiveCharacterTextSplitter` or LlamaIndex’s `SemanticSplitter`.
3.  **Embed:** Each chunk of text is then passed through an embedding model. This model converts the text into a high-dimensional vector. Popular embedding models include OpenAI's `text-embedding-3-large`, Google's `gemini-text-embedding-004`, and open-source variants from Hugging Face like BGE models.
4.  **Store:** Finally, these vector embeddings, along with the original text chunks and any associated metadata, are loaded into a vector database. This specialized database, like the local library FAISS or scalable solutions like Milvus, Qdrant, and Pinecone, is optimized for fast similarity searches [[52]](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf).

### Phase 2: Online Retrieval & Generation

This phase is triggered when a user submits a query to the system. It is the real-time part of the RAG pipeline that delivers the final answer [[33]](https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/).

Here is how it works:
1.  **Query:** The user asks a question. This query can be pre-processed to normalize it or expand it for better results, often managed by a query engine like those in LangChain or LlamaIndex.
2.  **Embed:** The user's query is converted into a vector using the *same* embedding model that was used during the ingestion phase. This ensures that the query and the document chunks are in the same vector space, making them comparable.
3.  **Search:** The system uses the query vector to search the vector database. It performs a similarity search (often using cosine similarity) to find the top-k document chunks whose embeddings are closest to the query's embedding [[54]](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/).
4.  **Generate:** The retrieved chunks are then assembled into a prompt along with the original user query and specific instructions. This augmented prompt is passed to an LLM, which generates a final answer grounded in the provided context. As we discussed in Lesson 4, using structured outputs at this stage can ensure the answer is returned in a consistent, machine-readable format with citations.

With the end-to-end path in place, the next question is quality: what are the advanced techniques to make the retrieval more accurate and useful across messy, real-world data?

## Advanced RAG Techniques

While a basic RAG pipeline is effective, its performance can degrade when dealing with complex, real-world data. To build production-grade systems, we need to move beyond naive retrieval and incorporate advanced techniques. These methods focus on improving the relevance and quality of the context provided to the LLM, which directly translates to more accurate answers [[4]](https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search).

Image 3: A flowchart illustrating the hybrid retrieval process, from user query to final context for an LLM.

### Hybrid Search

A common failure point in RAG is when the retrieval system misses relevant documents. Vector search is excellent at finding semantically similar content, but it can struggle with queries that rely on specific keywords, acronyms, or IDs. On the other hand, traditional keyword-based search, like BM25, excels at exact matches but lacks semantic understanding [[37]](https://www.chitika.com/hybrid-retrieval-rag/).

**Hybrid search** combines the strengths of both. It runs a vector search and a keyword search in parallel and then fuses the results. This is often done using an algorithm like Reciprocal Rank Fusion (RRF) [[38]](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid). This ensures that the system can capture both the meaning and the specific terms in a query. For instance, if a user asks, "My bill keeps rolling over," a keyword search would find articles with "rollover," while a semantic search might find documents about "carryover balance." Hybrid search gets you both, covering different phrasings of the same problem [[40]](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834).

### Re-ranking

The initial retrieval step is optimized for speed and recall, meaning it aims to quickly find a broad set of potentially relevant documents. However, the best document might not always be at the top of this initial list. **Re-ranking** introduces a second, more precise scoring step. After the initial retrieval, a more sophisticated model, typically a cross-encoder, re-evaluates the top candidates [[42]](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/).

Unlike bi-encoder models used for initial retrieval, which create separate embeddings for the query and documents, cross-encoders process the query and each document *together*. This allows for a deeper, more contextual assessment of relevance [[43]](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag). For example, in a product help system, a query like "how to connect my account" might initially retrieve a press release and a community forum thread. A re-ranker would likely push the step-by-step setup guide to the top of the list, ensuring the LLM receives the most useful context.

### Query Transformations

Sometimes, the user's query is not in the ideal format for retrieval. **Query transformations** rewrite or decompose the query to improve its chances of matching the right documents.

-   **Decomposition** breaks a complex, multi-part question into several simpler sub-questions [[19]](https://docs.nvidia.com/rag/latest/query_decomposition.html). For a query like, "What’s our travel policy for conferences in Europe this year?" the system might generate sub-questions: "What is the travel policy for conferences?", "What are the rules for Europe?", and "What changed this year?". It then retrieves documents for each sub-question and synthesizes the results.
-   **Hypothetical Document Embeddings (HyDE)** is another technique where the system first generates a hypothetical, ideal answer to the user's query. It then embeds this hypothetical answer and uses that embedding for the search [[16]](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/). The idea is that an answer is more likely to be semantically similar to other answers. For example, before searching, the system might draft a short answer like, "Employees attending approved conferences in Europe can book economy flights..." and then search for documents that sound like that.

### Advanced Chunking Strategies

How you split your documents can make or break your RAG system. Fixed-size chunking is simple but often cuts sentences or paragraphs in half, separating related information. For example, splitting a 20-page handbook every 500 words might cut the "Reimbursements" section in half, separating a policy from its specific cap amounts.

Advanced chunking strategies respect the document's structure:
-   **Semantic chunking** splits text based on topical changes, ensuring that each chunk is a coherent unit of meaning. This keeps the entire "Reimbursements" section together.
-   **Layout-aware chunking** is crucial for documents with complex formatting like tables or forms. Instead of splitting a pricing table by character count, this method would keep each row intact, preserving the relationship between a product, its price, and its discount.
-   **Context-enriched chunking** prepends each chunk with a summary of its parent document, providing crucial context that might be missing from the chunk itself [[6]](https://www.anthropic.com/news/contextual-retrieval).

### GraphRAG

For questions about complex relationships and interconnected data, standard document retrieval often falls short. **GraphRAG** addresses this by first constructing a knowledge graph from the source documents. In this graph, entities (like people, companies, or products) are nodes, and their relationships are edges [[46]](https://arxiv.org/html/2601.03014v1). This structured representation allows the system to answer multi-hop questions that require reasoning across different pieces of information.

For example, a retail query like, “Which shoes get the most size-related returns and were featured in last month’s ads?” requires connecting return data, reasons for returns, specific products, and the marketing calendar. Similarly, for IT operations, a question like, "Which incidents were caused by weekend deploys that also touched the login service?" requires linking change records, deploy times, affected services, and incident tickets. A knowledge graph makes these connections explicit, allowing the retrieval system to traverse the graph and assemble a precise, connected context that a standard vector search would likely miss [[5]](https://arxiv.org/html/2404.16130), [[50]](https://arxiv.org/html/2501.00309v2).

These techniques increase retrieval quality. Next, we’ll see how retrieval becomes one tool that an agent can choose to use as it reasons.

## Agentic RAG

In Lessons 7 and 8, we explored the ReAct framework, where an agent cycles through a Thought-Action-Observation loop to solve problems. **Agentic RAG** is the application of this principle, where retrieval is not a fixed step in a pipeline but a tool that a reasoning agent can choose to use, when, and how it sees fit [[11]](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/).

The core distinction is the shift from a linear workflow to an adaptive, iterative process.
-   **Standard RAG** is a rigid, one-shot pipeline: Retrieve → Augment → Generate. Every query follows this exact path.
-   **Agentic RAG** is a dynamic loop. The agent decides if it needs more information, when to retrieve it, how to reformulate its search query, and which knowledge source to consult [[12]](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/).

Image 4: A conceptual flowchart showing an agent's main iterative loop, including thought, action, tool selection, observation, and feedback.

This agentic approach unlocks several powerful capabilities. The agent can **iteratively** refine its search. If an initial retrieval yields a vague policy, the agent can reason about what is missing, narrow its query ("show me updates for EU customers in 2024"), and retrieve again. It can also **choose** which knowledge base to search, for example, deciding to query `search_incident_runbooks` instead of `search_marketing_pages` for an outage inquiry [[13]](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167).

Furthermore, an agent can **fuse** information from its RAG tool with outputs from other tools, like a web search or a code interpreter, to form a more comprehensive answer. It can even decide to **update** the RAG system's knowledge base with new information it learns. This falls under the topic of Memory for Agents, which we will cover in the next lesson.

Here is a conceptual example of an agent's thought process:
*   **Thought:** "The user is asking about the '2024 EU data retention rules.' Our internal policy documents cite 2023 regulations, which are likely outdated."
*   **Action:** `retrieve(internal_policy, query="EU data retention 2024")`
*   **Observation:** The retrieved document mentions amendments but is missing specific citations.
*   **Thought:** "I need external verification to confirm the latest changes."
*   **Action:** `web_search(query="EU data retention directive 2024 official text")`
*   **Observation:** The web search returns a link to the updated official directive.
*   **Thought:** "Now I have both the internal context and the latest external regulations. I will synthesize them, highlight the changes from 2023, and cite both sources."

This transforms the retrieval process from a simple database lookup into a conversation with a knowledgeable research assistant [[14]](https://airbyte.com/agentic-data/ai-agent-vs-rag). The agent doesn't just fetch data; it actively seeks, evaluates, and integrates it.

You now understand both a linear RAG pipeline and how an agent can control retrieval when needed. Let’s wrap up by situating RAG in the wider AI Engineering toolkit and previewing what comes next.

## Conclusion

We have explored how Retrieval-Augmented Generation is the most widely used solution to the LLM knowledge problem. While basic RAG offers a solid starting point, advanced techniques are essential for achieving production-grade quality. The future of knowledge retrieval is agentic, where an LLM can reason about its information needs and dynamically interact with knowledge sources. By grounding LLMs in verifiable data, RAG reduces hallucinations, enables customization with proprietary information, and builds user trust through source-based answers.

This makes RAG a foundational competency for any AI Engineer, and a critical component of the broader discipline of Context Engineering. It is not just a technique but a new way of thinking about how to build intelligent systems.

In our next lesson, we will dive into Memory for Agents, exploring how short-term and long-term memory systems complement the real-time retrieval capabilities of RAG. We will also cover other important topics later in this course, such as how to evaluate retrieval quality and monitor these complex systems in production to ensure they remain reliable and effective over time.

## References

- [1] [What Is Retrieval-Augmented Generation, aka RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [2] [A Complete Guide to RAG](https://towardsai.net/p/l/a-complete-guide-to-rag)
- [3] [Retrieval-Augmented Generation (RAG) Fundamentals First](https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search)
- [4] [Your RAG Is Wrong, Here's How To Fix It](https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search)
- [5] [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/html/2404.16130)
- [6] [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- [7] [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag)
- [8] [What is RAG: Understanding Retrieval-Augmented Generation](https://qdrant.tech/articles/what-is-rag-in-ai/)
- [9] [RAG is dead, long live agentic retrieval](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
- [10] [What is agentic RAG?](https://www.ibm.com/think/topics/agentic-rag)
- [11] [Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)
- [12] [Agentic RAG vs. traditional RAG: Key differences and benefits explained](https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/)
- [13] [Agentic RAG vs Traditional RAG](https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167)
- [14] [AI Agent vs. RAG: What’s the Difference?](https://airbyte.com/agentic-data/ai-agent-vs-rag)
- [15] [RAG vs Agentic AI: Which is the Right Choice for Your Enterprise?](https://domino.ai/blog/rag-vs-agentic-ai)
- [16] [RAG system in production: why it fails and how to fix it](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/)
- [17] [Build advanced retrieval-augmented generation systems](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
- [18] [Advanced RAG Techniques That Will Transform Your LLM Applications](https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/)
- [19] [Query Decomposition](https://docs.nvidia.com/rag/latest/query_decomposition.html)
- [20] [Advanced RAG Techniques for High-Performance LLM Applications](https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [21] [Retrieval-Augmented Generation: Building Grounded AI for Enterprise Knowledge](https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5)
- [22] [What is RAG?](https://www.mindstudio.ai/blog/what-is-rag/)
- [23] [The Rise of RAG](https://highlearningrate.substack.com/p/the-rise-of-rag)
- [24] [Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs](https://aclanthology.org/2024.emnlp-main.15.pdf)
- [25] [RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)
- [26] [A guide to RAG architecture types](https://humanloop.com/blog/rag-architectures)
- [27] [RAG and its Different Components](https://www.aimon.ai/posts/rag_and_its_different_components/)
- [28] [Grounding LLMs: Driving AI to Deliver Contextually Relevant Data](https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/)
- [29] [What is retrieval-augmented generation?](https://www.ibm.com/think/topics/retrieval-augmented-generation)
- [30] [What is RAG Architecture? A Guide for Machine Learning Engineers](https://galileo.ai/blog/rag-architecture)
- [31] [RAG Pipeline Deep Dive: Ingestion, Chunking, Embedding, and Vector Search](https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177)
- [32] [How RAG works](https://newsletter.systemdesign.one/p/how-rag-works)
- [33] [RAGOps Guide: Building and Scaling Retrieval-Augmented Generation Systems](https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/)
- [34] [Pistis-RAG: Enhancing Retrieval-Augmented Generation with Human Feedback](https://arxiv.org/html/2407.00072v5)
- [35] [What is Retrieval-Augmented Generation (RAG)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [36] [Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
- [37] [Hybrid Retrieval for RAG: Unlocking the Power of BM25 and FAISS](https://www.chitika.com/hybrid-retrieval-rag/)
- [38] [Optimize RAG with Hybrid Search](https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid)
- [39] [Hybrid Search Optimization: How BM25 and Dense Vector Retrieval Work Together for Superior AI Search](https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/)
- [40] [Hybrid RAG in the Real World: Graphs, BM25, and the End of Black-Box Retrieval](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834)
- [41] [Pistis-RAG: Enhancing Retrieval-Augmented Generation with Human Feedback](https://arxiv.org/html/2407.00072v5)
- [42] [10 techniques to improve RAG accuracy](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)
- [43] [Reranking Architectures in RAG](https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag)
- [44] [Advanced RAG Techniques for High-Performance LLM Applications](https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [45] [Advanced RAG: Retrieval with Cross-Encoders Re-ranking](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)
- [46] [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/html/2601.03014v1)
- [47] [Graph-Based Retrieval for RAG: Transforming Complex Queries into Contextual Insights](https://www.chitika.com/graph-based-retrieval-rag/)
- [48] [GraphRAG: A Graph-Based Approach for Improving Retrieval-Augmented Generation](https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf)
- [49] [What is GraphRAG? The Future of AI Search Explained](https://atlan.com/know/what-is-graphrag/)
- [50] [GraphRAG: A Survey of Retrieval-Augmented Generation with Knowledge Graphs](https://arxiv.org/html/2501.00309v2)
- [51] [Implementing Semantic Search for Retrieval](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval)
- [52] [How RAG Actually Works: Embeddings, Vector Databases, Indexing, Retrieval Explained Simply](https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf)
- [53] [Vector DB and RAG Pipeline for Document RAG](https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/)
- [54] [RAG Explained: Understanding Embeddings, Similarity, and Retrieval](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/)
- [55] [AWS Vector Databases Explained: Powering Semantic Search and RAG Systems](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [56] [Retrieval Augmented Generation (RAG) Explained](https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/)
- [57] [Addressing AI Hallucinations with Retrieval-Augmented Generation](https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html)
- [58] [Introduction to Augmenting LLMs using Retrieval Augmented Generation(RAG)](https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91)
- [59] [Retrieval-Augmented Generation (RAG)](https://www.promptingguide.ai/research/rag)
- [60] [Retrieval Augmented Generation (RAG): From Basics to Advanced](https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c)
- [61] [Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs](https://arxiv.org/html/2312.05934v3)
- [62] [Vector Databases in Practice: Building a Realistic Hybrid Search RAG System with Qdrant](https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0)
- [63] [AWS Vector Databases Explained: Semantic Search and RAG Systems](https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/)
- [64] [Vector Embeddings in RAG Applications](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5)
</article>