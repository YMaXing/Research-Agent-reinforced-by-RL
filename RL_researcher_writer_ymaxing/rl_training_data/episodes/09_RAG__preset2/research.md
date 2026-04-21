# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What are the theoretical foundations of Retrieval-Augmented Generation that make it superior to fine-tuning for addressing LLM hallucinations and static knowledge cutoffs?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://neo4j.com/blog/developer/fine-tuning-vs-rag/

Query: What are the theoretical foundations of Retrieval-Augmented Generation that make it superior to fine-tuning for addressing LLM hallucinations and static knowledge cutoffs?

Answer: Retrieval-augmented generation (RAG) addresses LLM limitations like knowledge cutoff, hallucinations, and lack of customization by using the LLM as a natural language interface to access external information, rather than relying solely on internal knowledge. Advantages over fine-tuning include: answers can cite sources for validation and updates; hallucinations are less likely since the LLM uses relevant documents instead of internal knowledge; easier to update and maintain by treating it as database maintenance rather than LLM retraining; personalized answers based on user context or permissions. Comparison: Fine-tuning adapts internal knowledge but is prone to hallucinations out-of-domain and requires retraining for updates; RAG integrates external up-to-date sources, is less prone to hallucinations (accuracy depends on retrieved data), and is more flexible for new domains by modifying retrieval data.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://www.infoworld.com/article/2335043/addressing-ai-hallucinations-with-retrieval-augmented-generation.html

Query: What are the theoretical foundations of Retrieval-Augmented Generation that make it superior to fine-tuning for addressing LLM hallucinations and static knowledge cutoffs?

Answer: Hallucinations stem from training data deficiencies. RAG improves accuracy by augmenting LLM inputs with retrieved context-specific information from proprietary or real-time data, mitigating hallucinations and providing fresh knowledge beyond static cutoffs. Unlike fine-tuning, which is often impractical, RAG is a low-cost alternative for accurate, contextual responses without retraining.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://aclanthology.org/2024.emnlp-main.15.pdf

Query: What are the theoretical foundations of Retrieval-Augmented Generation that make it superior to fine-tuning for addressing LLM hallucinations and static knowledge cutoffs?

Answer: RAG (Lewis et al., 2020) expands LLM capabilities in knowledge-intensive tasks using external knowledge sources: retrieves documents resembling the query from a knowledge base and adds them to the input for context, achievable without additional training using pre-trained embeddings (Neelakantan et al., 2022). Empirical findings: RAG consistently outperforms unsupervised fine-tuning on knowledge-intensive tasks for both existing and new knowledge; LLMs struggle to learn new facts via fine-tuning, though multiple fact variations help somewhat. Knowledge injection via post-processing is needed beyond pre-training; RAG superior for injecting external, up-to-date knowledge.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://arxiv.org/html/2312.05934v3

Query: What are the theoretical foundations of Retrieval-Augmented Generation that make it superior to fine-tuning for addressing LLM hallucinations and static knowledge cutoffs?

Answer: RAG expands LLMs’ capabilities in knowledge-intensive tasks by retrieving similar documents from an external knowledge base and adding them to the query input for context, without additional training using pre-trained embeddings. LLMs' pre-trained knowledge is limited by training data characteristics, making external injection challenging. RAG outperforms unsupervised fine-tuning on varied tasks for existing and new knowledge; fine-tuning shows limited gains, especially for new facts.

-----

</details>

<details>
<summary>How are vector embeddings generated and stored in vector databases to enable semantic similarity search as the core of the retrieval component in RAG systems?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://pub.towardsai.net/vector-databases-in-practice-building-a-realistic-hybrid-search-rag-system-with-qdrant-7b8f4a6e41e0

Query: How are vector embeddings generated and stored in vector databases to enable semantic similarity search as the core of the retrieval component in RAG systems?

Answer: In practice, a vector database is responsible for indexing, storing, and searching embeddings using nearest-neighbor algorithms, enabling fast and scalable embedding-based retrieval. This makes it a foundational component in modern RAG systems, where relevance is determined by meaning rather than lexical overlap. Vector databases are optimized for similarity search at scale. They let you ask questions like “find content most related to this input” and return fast, relevant results : especially in cases where traditional keyword-based search falls short. Vector database are retrieval system designed to store vector representations of data and efficiently rank them by semantic relevance to a query. Instead of matching documents using exact terms, it operates on embeddings and retrieves results based on similarity in a high-dimensional vector space. Indexing methods define how vectors are organized, stored, and searched efficiently. Two vector databases storing the same embeddings can perform very differently depending on the indexing strategy they use. Locality-Sensitive Hashing (LSH) groups similar vectors into the same buckets so search only looks at a small part of the space. It speeds things up by relying on probability: nearby vectors usually land together, but there’s no guarantee. Because the hash functions are fixed and don’t adapt to the data, LSH stays fast, but recall is limited.

-----

-----

Phase: [EXPLOITATION]

### Source [7]: https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/

Query: How are vector embeddings generated and stored in vector databases to enable semantic similarity search as the core of the retrieval component in RAG systems?

Answer: A vector database, as its name suggests, is a type of database designed to store, index, and efficiently search vector embeddings. These vectors are high-dimensional points that represent meaning. At its core, a vector database is designed to provide several capabilities beyond simple storage: efficient nearest-neighbor search algorithms, sophisticated indexing structures optimized for high-dimensional data. Embeddings are number arrays that capture the meaning of text, images, or audio. When text, images, audio, or other content passes through an embedding model, it is transformed into a dense vector where each dimension contributes to representing some aspect of the content’s meaning. This capability enables semantic search. The system accomplishes this by converting the query into a vector embedding using the same model that generated the product embeddings, then finding the query’s nearest neighbors in the database. Vector search typically relies on distance metrics to quantify similarity between vectors. To speed up similarity search, vector databases use algorithms such as: Indexing and Algorithms.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://qdrant.tech/articles/what-is-rag-in-ai/

Query: How are vector embeddings generated and stored in vector databases to enable semantic similarity search as the core of the retrieval component in RAG systems?

Answer: Vector databases store information as vector embeddings. This format supports efficient similarity searches to retrieve relevant data for your query. For example, Qdrant is specifically designed to perform fast, even in scenarios dealing with billions of vectors. Dense vector embeddings: This approach uses large language models like BERT to encode the query and passages into dense vector embeddings. These models are compact numerical representations that capture semantic meaning. Vector databases like Qdrant store these embeddings, allowing retrieval based on semantic similarity rather than just keywords using distance metrics like cosine similarity. This allows the retriever to match based on semantic understanding rather than just keywords. All the generated vector embeddings are stored in a knowledge base of indexed information. This supports efficient retrieval of similar pieces of information when needed. Query vectorization: Once you have vectorized your knowledge base you can do the same to the user query. When the model sees a new query, it uses the same preprocessing and embedding techniques. This ensures that the query vector is compatible with the document vectors in the index.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5

Query: How are vector embeddings generated and stored in vector databases to enable semantic similarity search as the core of the retrieval component in RAG systems?

Answer: Vector embeddings in RAG systems: A Retrieval-Augmented Generation (RAG) system is an advanced NLP architecture that enhances the capabilities of language models by combining them with retrieval-based information. Concept of Embedding Data into a Vector Database for Easy Retrieval: Before a RAG system can retrieve relevant data, the information must be structured in a way that makes it easily accessible and comparable. Data Vectorization: All the data—whether it's text, images, or any other form—needs to be transformed into vectors. This means each item in the database is converted into a high-dimensional numerical vector that represents various features of the data. Vector Database Creation and Storage: These vectors are then stored in a vector database, often using systems like FAISS (Facebook AI Similarity Search). These systems allow for efficient retrieval of vectors that are close to a given query vector in the high-dimensional space, which corresponds to retrieving data that is similar or relevant to a query.

-----

</details>

<details>
<summary>What distinguishes agentic RAG from standard linear RAG pipelines, especially when retrieval functions as a tool in a ReAct-style agent's reasoning and iteration loop?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/

Query: What distinguishes agentic RAG from standard linear RAG pipelines, especially when retrieval functions as a tool in a ReAct-style agent's reasoning and iteration loop?

Answer: Agentic RAG changes the system structure from a 'one-pass' pipeline to a control loop: retrieve, reason, decide, then retrieve again or stop. This mirrors the core pattern of 'reason and act' approaches like ReAct, where the system alternates between reasoning and action to gather new evidence. Agentic RAG retains the retriever and generator components but wraps retrieval in a loop, allowing the system to review evidence, identify gaps, and attempt retrieval again if needed. This gives the system an 'agentic' quality: it actively chooses how to gather stronger evidence until a stop condition is met. Analogy: classic RAG is like running one log query and concluding; agentic RAG is a debug loop querying, inspecting, refining, repeating until confident or hitting budget. ReAct provides a mental model with interleaved reasoning steps and actions for gathering evidence. Agents add planning (decomposition into smaller objectives, e.g., breaking down 'Why is SSO setup failing?' instead of single query) and tool use (retrieval as one of several tools). Teams are moving to agent-like loops that retry retrieval and call tools when first pass is weak.

-----

-----

Phase: [EXPLOITATION]

### Source [12]: https://www.pingcap.com/article/agentic-rag-vs-traditional-rag-key-differences-benefits/

Query: What distinguishes agentic RAG from standard linear RAG pipelines, especially when retrieval functions as a tool in a ReAct-style agent's reasoning and iteration loop?

Answer: Traditional RAG uses a static workflow with predefined queries and structured input, relying on single-step retrieval and human guidance, unable to refine without manual intervention. Agentic RAG introduces autonomous AI agents for dynamic decision-making, iterative reasoning, and real-time adaptability, adjusting prompts and strategies. Key differences: static information retrieval vs active problem-solving through dynamic retrieval; depends on human input vs minimal input with continuous re-evaluation. Agency: agents decide what to search and how to process, dynamically adjust based on goals/context. Features: autonomy (identify missing elements, seek info); dynamic retrieval (real-time data); augmented generation (integrate external info); feedback loop (refine based on feedback). Enables dynamic workflows over linear pipelines.

-----

</details>

<details>
<summary>How can query decomposition, HyDE, and advanced semantic or layout-aware chunking strategies be theoretically applied to improve retrieval accuracy in complex, real-world document corpora for RAG?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/

Query: How can query decomposition, HyDE, and advanced semantic or layout-aware chunking strategies be theoretically applied to improve retrieval accuracy in complex, real-world document corpora for RAG?

Answer: Sub-Query Decomposition breaks complex, multi-part questions into smaller, focused sub-queries, retrieves independently for each, then synthesizes the results before passing them to the LLM. This addresses complex queries that are too broad for a single retrieval pass. HyDE (Hypothetical Document Embeddings) closes the distribution gap between queries and documents where questions and answers are phrased differently, degrading embedding similarity. Process: 1. Take user’s query. 2. Generate hypothetical answer using LLM. 3. Embed the hypothetical answer. 4. Use that embedding to search vector store. 5. Retrieve real chunks closest to hypothetical answer. 6. Pass retrieved chunks + original query to LLM. Improves retrieval on knowledge-intensive tasks, especially short/vague queries vs. detailed documents. Multi-Query Retrieval generates N semantically different paraphrases, retrieves for each, deduplicates, and merges to catch missed chunks due to phrasing mismatch. Hybrid RAG addresses limitations of pure vector search by combining methods for better semantic and exact match retrieval.

-----

-----

Phase: [EXPLOITATION]

### Source [17]: https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a

Query: How can query decomposition, HyDE, and advanced semantic or layout-aware chunking strategies be theoretically applied to improve retrieval accuracy in complex, real-world document corpora for RAG?

Answer: Layout-aware chunking parses documents with structure intact, identifying titles, headers, sections, tables, lists, figures, then chunks around those boundaries. For complex documents like 10K financial filings, avoids naive fixed-token splits (e.g., 512 tokens yielding 847 chunks) by using document hierarchy. Structure matters as documents have hierarchy; context matters for tables/lists. Different documents need tailored strategies (financial reports ≠ blog posts). Semantic chunking outperforms naive approaches by preserving coherent topics, improving retrieval accuracy, though compute-intensive (embed every sentence, calculate distances, tune thresholds). Best for complex documents like academic papers, long-form articles, research reports where topic boundaries matter. Start with layout-aware for structured documents as single best improvement. At scale, page-level chunking beats complex strategies on 10K+ documents. Measure to iterate.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://cloudurable.com/blog/advanced-rag-techniques-that-will-transform-your-l/

Query: How can query decomposition, HyDE, and advanced semantic or layout-aware chunking strategies be theoretically applied to improve retrieval accuracy in complex, real-world document corpora for RAG?

Answer: Semantic Chunking optimizes text segmentation for technical documentation, research papers, legal contracts with complex topic structure. Benefits: Reduces irrelevant retrievals by 30-40% vs. fixed-size chunking; improves embedding quality by preserving conceptual integrity. Context Enriched Retrieval for narrative/educational materials where info spans sections: 25-35% improvement in context preservation. Hierarchical Indices create multi-level index (summaries for broad context, detailed chunks for precision); retrieves from summaries first, then drills down. 25-40% precision improvement for multi-faceted queries, scales for large collections. HyDE (Hypothetical Document Embedding) listed as advanced technique building on basic RAG (query embed → retrieve → LLM). Chunking strategies fundamentally impact retrieval quality.

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://docs.nvidia.com/rag/latest/query_decomposition.html

Query: How can query decomposition, HyDE, and advanced semantic or layout-aware chunking strategies be theoretically applied to improve retrieval accuracy in complex, real-world document corpora for RAG?

Answer: Query decomposition breaks down complex, multi-faceted queries into simpler, focused subqueries. Each processed independently for comprehensive context, then synthesized. Benefits: Better context coverage for multiple aspects; iterative refinement with follow-ups; multi-perspective analysis. Components: LLM-powered subquery generation, iterative processing, response synthesis. Boosts accuracy for multi-hop reasoning or context-rich queries. Valuable for multi-hop/complex queries involving multiple steps/aspects; generates intermediate answers per subquery, combines for comprehensive final answer. Disabled by default in NVIDIA RAG Blueprint; enable via values.yaml for complex queries. Not for simple factual or single-concept queries.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://neo4j.com/blog/genai/advanced-rag-techniques/

Query: How can query decomposition, HyDE, and advanced semantic or layout-aware chunking strategies be theoretically applied to improve retrieval accuracy in complex, real-world document corpora for RAG?

Answer: HyDE-style: Generate hypothetical answer from query to improve semantic alignment between query and docs, bridging phrasing gaps. Query expansion/HyDE improves recall without overfetching. Structure-aware chunking/parent-doc preserves structure. Layer after stabilizing basic retrieval: good embeddings, sensible chunking, metadata, reranking. Add hybrid search (BM25 + vectors via RRF). Introduce query understanding with expansion/HyDE. Optimize context with parent-doc logic, summarization. For basic pipeline hallucinations/misses, use hybrid retrieval, metadata filtering, reranking, structure-aware chunking/parent-doc, then summarization, query expansion/HyDE, multi-step reasoning.

-----

</details>

<details>
<summary>In what ways does RAG function as a foundational competency for AI engineers building grounded agents, particularly in complementing future memory systems and reducing hallucinations through verifiable sources?</summary>

Phase: [EXPLOITATION]

### Source [21]: https://medium.com/@fahey_james/retrieval-augmented-generation-building-grounded-ai-for-enterprise-knowledge-6bc46277fee5

Query: In what ways does RAG function as a foundational competency for AI engineers building grounded agents, particularly in complementing future memory systems and reducing hallucinations through verifiable sources?

Answer: Retrieval-Augmented Generation (RAG) builds grounded AI for enterprise knowledge by combining a retriever, ranker, and generator. The retriever fetches relevant snippets, the ranker prioritizes by relevance or quality including verified sources or up-to-date content, and the generator uses top-ranked snippets as context to produce responses. Grounding generation in external sources reduces hallucinations. RAG ensures answers are verifiable, reduces need for expensive fine-tuning, simplifies compliance by excluding sensitive info and displaying citations. It addresses insufficient context causing hallucinations via autorater and re-ranking. Future directions include combining RAG with agentic workflows where models iterate retrieval and reasoning to further reduce hallucinations and enable complex tasks. RAG supports grounded agents by injecting external context, prioritizing verifiable sources, and integrating with agentic systems for iterative retrieval.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/

Query: In what ways does RAG function as a foundational competency for AI engineers building grounded agents, particularly in complementing future memory systems and reducing hallucinations through verifiable sources?

Answer: RAG inventor discusses RAG for grounded AI and agents. Hallucinations are problematic in high-stakes scenarios, addressed by grounded models trained to hallucinate less. RAG enables agents (RAG agents) to work on user data via active retrieval: agents decide to retrieve, potentially iterate if initial retrieval errs (e.g., 'maybe I should have gone here'). This iterative retrieval-reasoning unlocks future capabilities for grounded agents, complementing memory by providing verifiable external data access.

-----

</details>

<details>
<summary>How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?</summary>

Phase: [EXPLOITATION]

### Source [27]: https://www.aimon.ai/posts/rag_and_its_different_components/

Query: How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?

Answer: The process begins with curating and indexing documents into a vector database. When a user submits a query, the system searches the vector database for relevant information. This retrieved information is then combined with the user’s query to form an enriched input, providing the necessary context for the LLM to generate a coherent and contextually informed response. Once the relevant data is retrieved, it is passed to an LLM as part of the input context. The LLM uses this retrieved context to generate outputs that are informed by relevant knowledge. Retrieval transforms the query into a vector embedding and searches the database using similarity metrics to locate matching data, which is combined with the query for enriched input to the LLM.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://toloka.ai/blog/grounding-llms-driving-ai-to-deliver-contextually-relevant-data/

Query: How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?

Answer: Grounding LLMs using Retrieval-Augmented Generation (RAG) enhances contextual understanding. The retriever scans sources to locate relevant information. When the model receives user queries, the retrieval system processes the query and searches databases or documents to find relevant information. The LLM uses this retrieved data to craft relevant responses, ensuring up-to-date and contextually accurate content informs the output. The first step is sourcing data from repositories, which the retriever uses to form the foundation for contextually accurate outputs.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://www.ibm.com/think/topics/retrieval-augmented-generation

Query: How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?

Answer: RAG adds an information retrieval component, gathering relevant information and feeding it to the generative AI model to enhance response quality. RAG systems follow a process: user submits prompt; retrieval model queries knowledge base; relevant information returned to integration layer; RAG engineers an augmented prompt to the LLM with enhanced context from retrieved data; LLM generates output. The integration layer creates a new prompt consisting of the original user query plus enhanced context from retrieval. RAG employs prompt engineering techniques to help the LLM return the best response.

-----

</details>

<details>
<summary>What are the key operations and theoretical rationale for separating RAG into offline ingestion indexing versus online query-time retrieval and generation phases?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177

Query: What are the key operations and theoretical rationale for separating RAG into offline ingestion indexing versus online query-time retrieval and generation phases?

Answer: A complete RAG pipeline consists of two main phases: Ingestion Phase (Offline): Documents → Chunking → Embedding → Index/Store in Vector Database. Retrieval Phase (Runtime): User Query → Embed Query → Similarity Search → Top-K Results → LLM Generation → Response. The RAG pipeline connects the model to the information it needs at query time. When a user asks a question, the pipeline retrieves the most relevant documents, prepares that text as context, and includes it in the prompt so the model can generate an answer grounded in retrieved material rather than training data alone. Ingestion is the process of loading documents from multiple sources and in multiple formats, transforming them into a structured form suitable for embedding and retrieval. At runtime, when a user submits a query, the retrieval phase locates the most relevant chunks to provide as context to the LLM. Query Embedding: The system encodes the user’s query with the same model used to embed documents during ingestion.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://newsletter.systemdesign.one/p/how-rag-works

Query: What are the key operations and theoretical rationale for separating RAG into offline ingestion indexing versus online query-time retrieval and generation phases?

Answer: A RAG system has two main parts: An offline ingestion pipeline that gets your data ready. An online retrieval pipeline that answers queries. Data Ingestion Pipeline (Offline Phase): First, process your knowledge base. Then, index it. Only then can your RAG system answer questions. This happens in five steps: 1. Load documents from anywhere: PDFs, databases, APIs, wikis, Slack channels, and Confluence pages. 2. Chunking: Split documents into semantically meaningful pieces. This is the single highest-leverage step to get right. 3. Embedding: Convert each chunk into a vector using an embedding model. 4. Storage: Store the vectors in a vector database optimized for similarity search. 5. Metadata tagging: Tag each chunk with source, timestamp, category, and access control information. This metadata becomes critical for filtering, attribution, and security later. What triggers the offline phase? In traditional workflows, this pipeline runs when new data is available. This can happen when documents are added or updated. It can also occur when a database changes or on a regular schedule, like nightly or weekly. Some teams trigger re-ingestion if retrieval quality drops. You’re not changing the model. You’re changing what it sees. That distinction makes RAG so powerful and so practical. The key insight for RAG is clear. System finds relevant content. It does this even if the user’s question doesn’t use the exact words from the source document. It searches by meaning, not by keywords.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://towardsdatascience.com/ragops-guide-building-and-scaling-retrieval-augmented-generation-systems-3d26b3ebd627/

Query: What are the key operations and theoretical rationale for separating RAG into offline ingestion indexing versus online query-time retrieval and generation phases?

Answer: The RAGOps stack can be visualised as layers in three categories. The critical layers enable the two core pipelines of the RAG system – the indexing pipeline and the generation pipeline. Indexing Pipeline (Offline): Step 1: Connect to previously identified external sources. Step 2: Extract documents and parse text from these documents. Step 3: Break down long pieces of text into smaller manageable pieces. Step 4: Convert these small pieces into a suitable format. Step 5: Store this information. Generation Pipeline (Online): The set of processes that is employed to search and retrieve information from the knowledge base to generate responses to user queries forms the generation pipeline. It facilitates real-time interaction with users. This can also be distilled in five steps. Step 1: User asks a question to our system. The production ecosystem for RAG and LLM applications is still evolving. Early tooling and design patterns have emerged. RAGOps (RAG Operations) refers to the operational practices, tools, and processes involved in deploying, maintaining, and optimising RAG systems in production environments. The RAGOps stack includes additional components like vector stores and embeddings models which are essential components of the indexing pipeline.

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://aws.amazon.com/what-is/retrieval-augmented-generation/

Query: What are the key operations and theoretical rationale for separating RAG into offline ingestion indexing versus online query-time retrieval and generation phases?

Answer: Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response. Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.

-----

</details>

<details>
<summary>How does hybrid retrieval theoretically combine BM25 keyword methods with dense vector search to address limitations of pure semantic retrieval in RAG?</summary>

Phase: [EXPLOITATION]

### Source [36]: https://pr-peri.github.io/blogpost/2026/03/05/blogpost-hybrid-search.html

Query: How does hybrid retrieval theoretically combine BM25 keyword methods with dense vector search to address limitations of pure semantic retrieval in RAG?

Answer: Hybrid search combines vector search with traditional keyword-based retrieval like BM25. Pure vector search relies on embedding models to convert text into high-dimensional vectors, measuring similarity using cosine similarity or dot product, but it fails on specific product codes, technical identifiers, or exact phrases because embeddings capture semantic meaning but miss exact keyword matches. BM25 is fast and precise for keywords but lacks semantic depth. By combining both methods with reciprocal rank fusion (RRF), hybrid search provides retrieval that is robust, accurate, and adaptable to diverse query types. Pure vector search struggles with exact keyword matches and rare terms, while BM25 excels at keyword matching. Hybrid search is a practical necessity for production RAG systems, offering the best of both worlds: semantic understanding from vectors and exact matches from BM25. Key takeaways include that hybrid search combines both for superior retrieval accuracy, RRF is the simplest and most effective fusion method, and it is especially valuable for diverse query types and technical domains.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid

Query: How does hybrid retrieval theoretically combine BM25 keyword methods with dense vector search to address limitations of pure semantic retrieval in RAG?

Answer: Hybrid search combines sparse (keyword-based like BM25) and dense (embedding-based vector) retrieval to address limitations of basic RAG relying on semantic search alone, which struggles with precision and efficiency on large repositories or diverse queries. Sparse retrieval (BM25) ranks documents based on keyword frequency and rarity (term frequency and inverse document frequency), effective for exact matches but fails on semantic relationships. Dense retrieval uses cosine similarity on embeddings for meaning. Implementation: 1. Keyword search with BM25. 2. Vector search. 3. Result fusion using weighted fusion H = (1−α)⋅K + α⋅V (K=keyword score, V=vector score, α=weighting parameter) or Reciprocal Rank Fusion (RRF). This leverages strengths of both: BM25 for precision on specific terms, vectors for context.

-----

-----

Phase: [EXPLOITATION]

### Source [39]: https://cubitrek.com/blog/hybrid-search-optimization-how-bm25-and-dense-vector-retrieval-work-together-for-superior-ai-search/

Query: How does hybrid retrieval theoretically combine BM25 keyword methods with dense vector search to address limitations of pure semantic retrieval in RAG?

Answer: Hybrid search combines BM25 (sparse, for exact terms) and dense vector retrieval (for meaning) to balance both dynamically, optimizing for RAG. Modern AI search must understand meaning (dense) and respect exact terms (sparse). Use BM25 for precision, vectors for meaning. Parallel retrieval: BM25 retrieves top N_s results, dense top N_d, merge with weighted formula final_score = α * dense_score + β * bm25_score. Normalize scores before combining as they are on different scales. Other modes: Sparse → Dense (BM25 filters, then dense ranks); Dense → Sparse (vectors retrieve, BM25 validates). Best for RAG pipelines. Achieves higher recall, precision, stable performance, stronger LLM grounding. For RAG, hybrid → rerank → threshold reduces hallucination.

-----

-----

Phase: [EXPLOITATION]

### Source [40]: https://community.netapp.com/t5/Tech-ONTAP-Blogs/Hybrid-RAG-in-the-Real-World-Graphs-BM25-and-the-End-of-Black-Box-Retrieval/ba-p/464834

Query: How does hybrid retrieval theoretically combine BM25 keyword methods with dense vector search to address limitations of pure semantic retrieval in RAG?

Answer: Hybrid RAG combines BM25 with vector-based retrieval. Vector search excels at subtle meaning but drifts to irrelevant passages when ambiguous. BM25 is transparent, predictable, effective for keywords, combined with vector reranking. BM25+Vector is a middle ground for explainability and grounding without full graph engineering. In hybrid pipelines, BM25 provides high-precision evidence, vectors fill semantic gaps. Research shows fusing with vectors improves faithfulness, relevance, recall over either alone.

-----

</details>

<details>
<summary>What mechanisms allow cross-encoder re-rankers to improve relevance ordering of initially retrieved passages in RAG pipelines prior to prompt augmentation?</summary>

Phase: [EXPLOITATION]

### Source [41]: https://arxiv.org/html/2407.00072v5

Query: What mechanisms allow cross-encoder re-rankers to improve relevance ordering of initially retrieved passages in RAG pipelines prior to prompt augmentation?

Answer: RAG systems have evolved through several stages. Initially, representation learning techniques such as Bi-Encoders and Maximum Inner-Product Search were employed for efficient retrieval with high semantic similarity. Later, BM25 was introduced for diversification, leading to mixed retrieval systems, but these often required segmenting text, affecting balance between local semantics and user intent. To address this, re-ranker technologies, primarily Cross-Encoders, were integrated into the RAG pipeline to enhance retrieval.

-----

-----

Phase: [EXPLOITATION]

### Source [42]: https://redis.io/blog/10-techniques-to-improve-rag-accuracy/

Query: What mechanisms allow cross-encoder re-rankers to improve relevance ordering of initially retrieved passages in RAG pipelines prior to prompt augmentation?

Answer: Re-ranking uses a second-pass model that scores query-document pairs jointly rather than independently. Cross-encoder models process query and document tokens together, allowing richer relevance assessment than bi-encoder initial retrieval. Initial retrieval optimizes for recall, but candidate ranking may be suboptimal; documents lower in initial ranking may be more relevant. Re-ranking operates on small candidate set (top 20-100), making it practical despite higher cost per document. Reports 10-40% precision improvements.

-----

-----

Phase: [EXPLOITATION]

### Source [43]: https://apxml.com/courses/optimizing-rag-for-production/chapter-2-advanced-retrieval-optimization/reranking-architectures-rag

Query: What mechanisms allow cross-encoder re-rankers to improve relevance ordering of initially retrieved passages in RAG pipelines prior to prompt augmentation?

Answer: In a two-stage pipeline, initial retriever narrows corpus to candidates; re-ranker refines for relevance before LLM. Cross-Encoders use Transformer models like BERT-base/large, fine-tuned on relevance tasks (e.g., MS MARCO). Process each query-document pair individually to produce relevance scores, then re-sort and select top for prompt. Provides maximum interaction between query and document tokens via full cross-attention, superior to bi-encoders. Balances computational cost with relevance gain; applied to top 50 candidates, select top 3-5.

-----

-----

Phase: [EXPLOITATION]

### Source [44]: https://neo4j.com/blog/genai/advanced-rag-techniques/

Query: What mechanisms allow cross-encoder re-rankers to improve relevance ordering of initially retrieved passages in RAG pipelines prior to prompt augmentation?

Answer: After first-pass retrieval, rerank with cross-encoder or rerank service so top-k to LLM is optimal. Reranking improves top-k ordering. Preceded by filtering with metadata and semantic thresholds to remove irrelevant hits, reducing prompt bloat.

-----

-----

Phase: [EXPLOITATION]

### Source [45]: https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/

Query: What mechanisms allow cross-encoder re-rankers to improve relevance ordering of initially retrieved passages in RAG pipelines prior to prompt augmentation?

Answer: In multi-stage pipeline: Stage 1 bi-encoder (independent encoding, cosine similarity, top 20). Stage 2 cross-encoder scores query-document pairs with full cross-attention (top 10). Unlike bi-encoder, cross-encoder allows deep interaction. Stage 3 optional LLM list-wise reranking sees all candidates for global ordering.

-----

</details>

<details>
<summary>How does the GraphRAG approach of building entity knowledge graphs and hierarchical community summaries enable superior handling of multi-hop relational queries over standard document retrieval?</summary>

Phase: [EXPLOITATION]

### Source [46]: https://arxiv.org/html/2601.03014v1

Query: How does the GraphRAG approach of building entity knowledge graphs and hierarchical community summaries enable superior handling of multi-hop relational queries over standard document retrieval?

Answer: GraphRAG introduces a graph-based approach that leverages LLMs to extract entities and relationships from documents, constructing a knowledge graph that captures semantic structure. Through community detection, it generates hierarchical summaries at multiple levels, enabling both local and global reasoning for complex queries. Graph-based representations encode document relations offline, reducing reliance on repeated online retrieval. It supports cross-document retrieval and question answering by organizing textual information into structured graphs, facilitating multi-hop evidence capture during retrieval. This contrasts with standard methods that rely on similarity-based connections at the chunk level, which struggle to capture fine-grained semantic and logical relationships.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://webhome.cs.uvic.ca/~thomo/papers/asonam2025-graphrag.pdf

Query: How does the GraphRAG approach of building entity knowledge graphs and hierarchical community summaries enable superior handling of multi-hop relational queries over standard document retrieval?

Answer: GraphRAG extracts entity-relation triples with an LLM, constructs a knowledge graph, applies community detection, and retrieves both local neighbors and community summaries at inference time. This extends retrieval scope and improves answer depth for multi-hop queries. It partitions the knowledge graph and uses community summaries alongside local neighbors. The design exposes the LLM to community structure among text chunks, preserving cross-chunk links vital for reasoning. At inference, it returns neighbourhood passages and community summaries. This mirrors a two-level logic for local and global search, enabling superior handling over standard retrieval by capturing relational structure without heavy reliance on explicit triples in follow-ups, though original uses entity graphs.

-----

-----

Phase: [EXPLOITATION]

### Source [49]: https://atlan.com/know/what-is-graphrag/

Query: How does the GraphRAG approach of building entity knowledge graphs and hierarchical community summaries enable superior handling of multi-hop relational queries over standard document retrieval?

Answer: GraphRAG improved comprehensiveness of answers by 50-70% over baseline RAG on complex, multi-document summarization tasks. A 2024 Stanford study confirmed graph-augmented retrieval reduced factual errors by 35-45% on multi-hop question answering benchmarks. Gains come from structure: instead of hoping the right text chunk is semantically close to the query, GraphRAG follows explicit entity-relationship paths to assemble context that an LLM can reason over. This enables superior multi-hop relational queries compared to vector-only approaches.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://arxiv.org/html/2501.00309v2

Query: How does the GraphRAG approach of building entity knowledge graphs and hierarchical community summaries enable superior handling of multi-hop relational queries over standard document retrieval?

Answer: In conventional RAG, information is stored independently as chunks, preventing capture of chunk relations and hindering multi-hop reasoning. GraphRAG stores chunks as interconnected nodes with edges denoting relations, benefiting retrieval for multi-hop tasks. It leverages graph-based techniques like graph traversal and community detection to capture relational knowledge. Unlike semantic similarity search, GraphRAG uses graph traversal (e.g., entity linking, BFS/DFS) and GNNs for retrieval, enabling following entity-relationship paths, e.g., for queries like “What drugs treat epithelioid sarcoma and affect EZH2 gene product?”, assembling relevant context via multi-hop paths over independent chunk retrieval.

-----

</details>

<details>
<summary>What theoretical principles underlie semantic similarity search in the retrieval pillar of RAG, and how do vector databases facilitate efficient lookup of relevant document chunks using embeddings?</summary>

Phase: [EXPLOITATION]

### Source [51]: https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-6-integrating-llms-external-data-rag/implementing-semantic-search-retrieval

Query: What theoretical principles underlie semantic similarity search in the retrieval pillar of RAG, and how do vector databases facilitate efficient lookup of relevant document chunks using embeddings?

Answer: Unlike keyword search, which matches exact words, semantic search finds text that is contextually and semantically similar in meaning, even if the wording is different. This is possible because our text embedding models have captured the meaning of the document chunks as vectors in a high dimensional space. Chunks with similar meanings are located closer together in this vector space. When a user submits a query (e.g., "What were the main findings of the Q3 report?"), the first step in the retrieval process is to convert this query into an embedding vector using the same text embedding model that was used to embed the document chunks. This is important; comparing vectors generated by different models is generally meaningless. We embed the user_query to get query_embedding. We call a method like similarity_search_with_score on our vector_store. We pass the query_embedding and specify k=4, meaning we want the 4 most similar document chunks. Vector store libraries might have slightly different method names (search, query, get_nearest_neighbors), but the principle is the same. The results typically include the original document chunks (or references to them) and their corresponding similarity scores. A higher score (for cosine similarity) indicates greater relevance to the query. Visualization of embeddings in 2D space. The search aims to find document points (blue) closest to the query point (red). Here, Doc 1, Doc 2, and Doc 4 would likely be retrieved if k=3. After documents are loaded, segmented into manageable chunks, converted into vector embeddings, and organized within a vector store, the subsequent task is to retrieve pertinent information in response to a user's query. This activity forms the "Retrieval" component of Retrieval Augmented Generation (RAG), and it fundamentally depends on the principle of semantic search.

-----

-----

Phase: [EXPLOITATION]

### Source [52]: https://medium.com/@robi.tomar72/how-rag-actually-works-embeddings-vector-databases-indexing-retrieval-explained-simply-3d1ca45fe1bf

Query: What theoretical principles underlie semantic similarity search in the retrieval pillar of RAG, and how do vector databases facilitate efficient lookup of relevant document chunks using embeddings?

Answer: Semantic search finds text that is contextually and semantically similar in meaning, even though wording is different. This is why embeddings are the heart of RAG. SQL and MongoDB search by exact words, substrings, filtering fields. But RAG needs semantic search. Vector DBs search by meaning, using similarity measures like cosine similarity, dot product, Euclidean distance. They store embeddings efficiently and retrieve the closest matches. Popular vector DBs: FAISS, Pinecone, Weaviate, Milvus, Qdrant. How Retrieval Works (Simple Step-by-Step): User Query → Create Embedding → Vector Search → Retrieve Top-K Chunks → Build Prompt → LLM Generates Final Answer. Example query: “Which inverter model supports 3-phase output?” Steps: Convert query to embedding, Search in vector DB, Retrieve 3–5 most relevant chunks, Pass them to the LLM with the question, LLM answers based on retrieved text. Imagine teaching a search engine to understand meaning, not just match words. RAG (Retrieval-Augmented Generation) does exactly that — it fuses smart retrieval with generative models so answers are precise and grounded. We convert documents into embeddings (compact meaning snapshots), store them in vector databases, and use indexing to fetch the most relevant pieces in milliseconds. Those retrieved snippets are then fed to an LLM that composes a fluent, evidence-based answer instead of guessing. In Short: embeddings encode meaning, vectors store it, indexes find it fast, and retrieval supplies the facts the model actually needs. Chunking = splitting documents into small meaningful pieces. Good chunk size: 200–400 tokens for most tasks. Chunk Overlap (like 30–50 tokens) ensures that information split across boundaries is still captured.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/

Query: What theoretical principles underlie semantic similarity search in the retrieval pillar of RAG, and how do vector databases facilitate efficient lookup of relevant document chunks using embeddings?

Answer: A Vector DB (Vector Database) is the core retrieval layer in a RAG (Retrieval-Augmented Generation) system. It stores document embeddings, numerical representations of text chunks, and performs semantic similarity search to find the most relevant pieces of information for a query. In Document RAG, the Vector DB enables fast and accurate retrieval of related document sections before passing them to a language model for context-aware generation. Large PDFs and long documents overwhelm vision-language models with excessive tokens and high cost. A RAG pipeline with a vector database fixes this by splitting documents into small chunks, embedding them once, and storing them with page metadata. When a user asks a question, the system searches only the most relevant parts in milliseconds. This keeps input tiny, avoids context limits, cuts inference time, and saves GPU memory. In a RAG pipeline, vector databases handle retrieval. They store document chunks as embeddings (from models like embeddingGemma). Each chunk includes metadata like page numbers or file names. When we ask a question: Popular options: sentence transformer, Qdrant. The retrieval phase has two steps: finding relevant text chunks via vector search, and then using the retrieved page metadata to extract the visual evidence. Textual Similarity Search in Vector DB and RAG: The query_with_page function performs the standard RAG retrieval using the text embedding of the user’s query against the vectors stored in Qdrant.

-----

-----

Phase: [EXPLOITATION]

### Source [54]: https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/

Query: What theoretical principles underlie semantic similarity search in the retrieval pillar of RAG, and how do vector databases facilitate efficient lookup of relevant document chunks using embeddings?

Answer: After the text is transformed into embeddings, inference becomes vector math. This is exactly what allows us to identify and retrieve relevant documents in the retrieval step of the RAG framework. Once we turn both the user’s query and the knowledge base documents into vectors using an embedding model, we can then compute how similar they are using an appropriate metric like cosine similarity, Euclidean distance (L2 distance), or dot product. Cosine similarity is a measure of how similar two vectors (embeddings) are. Given two vectors A and B, cosine similarity is calculated as follows: Simply put, cosine similarity is calculated as the cosine of the angle between two vectors, and it ranges from 1 to -1. In this script, I use LangChain’s retriever object retriever = vector_store.as_retriever(), which by default uses the similarity metric of the underlying FAISS index. FAISS provides two indices: IndexFlatL2 and IndexFlatIP. Therefore, in the initial script, chunks are retrieved using L2 distance as a metric. This script also retrieves by default the k=4 most similar chunks. In other words, what we are doing there is that we retrieve the top k most relevant to the user query chunks based on L2 distance. create vector database w FAISS vector_store = FAISS.from_documents(documents, embeddings) retriever = vector_store.as_retriever().

-----

-----

Phase: [EXPLOITATION]

### Source [55]: https://tutorialsdojo.com/aws-vector-databases-explained-semantic-search-and-rag-systems/

Query: What theoretical principles underlie semantic similarity search in the retrieval pillar of RAG, and how do vector databases facilitate efficient lookup of relevant document chunks using embeddings?

Answer: Vector search operates on an entirely different principle: it finds items whose vector representations are closest to the query vector in the embedding space, regardless of the specific words used. This capability enables semantic search. When I search for “y2k tops for women,“ a vector-powered system understands my intent and retrieves trendy tops that match the Y2K aesthetic, even if the product descriptions never use that exact phrase. The system accomplishes this by converting the query into a vector embedding using the same model that generated the product embeddings, then finding the query’s nearest neighbors in the database. Vector search typically relies on distance metrics to quantify similarity between vectors: Vector Search Common Metrics. To speed up similarity search, vector databases use algorithms such as: A vector database, as its name suggests, is a type of database designed to store, index, and efficiently search vector embeddings. These vectors are high-dimensional points that represent meaning. At its core, a vector database is designed to provide several capabilities beyond simple storage: efficient nearest-neighbor search algorithms, sophisticated indexing structures optimized for high-dimensional data, fault tolerance and durability guarantees, authentication and access control mechanisms, and query engines that support complex filtering alongside similarity search.

-----

</details>

<details>
<summary>How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?</summary>

Phase: [EXPLOITATION]

### Source [56]: https://www.topquadrant.com/resources/blog-retrieval-augmented-generation-explained/

Query: How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?

Answer: Once relevant chunks are retrieved, the system “augments” the original user query by injecting the retrieved content as context. The augmented prompt may have a template such as: QUESTION: <user query> CONTEXT: <retrieved document excerpts or summaries> INSTRUCTIONS: Using the context above, answer the question. If the context does not contain the answer, say so. Prompt engineering is essential. It ensures the model gives weight to retrieved context, handles conflicts, and respects constraints (e.g. do not hallucinate beyond context). Some systems contextualize at multiple levels or interleave retrieval and generation. At its core, RAG bridges the strengths of information retrieval with generative modeling. The retrieval component identifies candidate documents or data relevant to a user’s query; the augmentation step combines that retrieved content with the original prompt; the generation step lets the LLM produce a response informed by both the prompt and the retrieved knowledge.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://www.promptingguide.ai/research/rag

Query: How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?

Answer: Generation: The relevant documents are combined with the original prompt as additional context. The combined text and prompt are then passed to the model for response generation which is then prepared as the final output of the system to the user. Optimizing post-retrieval focuses on avoiding context window limits and dealing with noisy or potentially distracting information. A common approach to address these issues is re-ranking which could involve approaches such as relocation of relevant context to the edges of the prompt or recalculating the semantic similarity between the query and relevant text chunks. Prompt compression may also help in dealing with these issues.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What are the primary sources of noise and information loss in the standard RAG pipeline, and what theoretical approaches exist to quantify and mitigate prompt overload during the augmentation phase?</summary>

Phase: [EXPLORATION]

### Source [61]: https://www.promptingguide.ai/research/rag

Query: What are the primary sources of noise and information loss in the standard RAG pipeline, and what theoretical approaches exist to quantify and mitigate prompt overload during the augmentation phase?

Answer: Optimizing post-retrieval focuses on avoiding context window limits and dealing with noisy or potentially distracting information. A common approach to address these issues is re-ranking which could involve approaches such as relocation of relevant context to the edges of the prompt or recalculating the semantic similarity between the query and relevant text chunks. Prompt compression may also help in dealing with these issues. Evaluating a RAG framework focuses on three primary quality scores and four abilities. Quality scores include measuring context relevance (i.e., the precision and specificity of retrieved context), answer faithfulness (i.e., the faithfulness of answers to the retrieved context), and answer relevance (i.e., the relevance of answers to posed questions). In addition, there are four abilities that help measure the adaptability and efficiency of a RAG system: noise robustness, negative rejection, information integration, and counterfactual robustness.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://medium.com/@bijit211987/5-practical-challenges-of-rag-and-their-mitigation-ideas-034217d8ed96

Query: What are the primary sources of noise and information loss in the standard RAG pipeline, and what theoretical approaches exist to quantify and mitigate prompt overload during the augmentation phase?

Answer: Handling Noisy or Incomplete Knowledge Bases: Problem: In real-world scenarios, the knowledge base might be incomplete or filled with noise. This causes the retrieval component to return irrelevant or incorrect information, which undermines the generated response. Mitigation Strategy: In addition to regular updates, I recommend utilizing unsupervised anomaly detection techniques to filter out irrelevant or out-of-domain content. Tools like Anomaly Transformer can detect and remove noisy data. You can also employ knowledge graph augmentation, where a structured knowledge graph is integrated to validate and augment retrieved data. Another technique is to use document ranking algorithms that not only rely on relevance but also on trustworthiness scores based on metadata, timestamps, and domain-specific relevance metrics. Set up document deduplication pipelines to eliminate redundant information, ensuring that only the most up-to-date and relevant documents are retrieved.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://www.unite.ai/how-to-build-reliable-rag-a-deep-dive-into-7-failure-points-and-evaluation-frameworks/

Query: What are the primary sources of noise and information loss in the standard RAG pipeline, and what theoretical approaches exist to quantify and mitigate prompt overload during the augmentation phase?

Answer: According to researchers Barnett et al., Retrieval Augmented Generation (RAG) systems encounter seven specific Failure Points (FPs) throughout the pipeline. Data Integrity & Trust Failures: When missing or incorrect information is present, the system is no longer a reliable source of information. Retrieval & Efficiency Bottlenecks: The RAG pipeline can be inefficient when it misses key information in the retrieval and consolidation stages. FP7. Incomplete Answers: This is a situation where an LLM generates an output not necessarily wrong, but missing key pieces of information that were available in the context. For example, when a user asks a complex question like “What are the key points in documents A, B, and C?” , the LLM only addresses one or two of the sources.

-----

-----

Phase: [EXPLORATION]

### Source [65]: https://deconvoluteai.com/blog/rag/failure-modes

Query: What are the primary sources of noise and information loss in the standard RAG pipeline, and what theoretical approaches exist to quantify and mitigate prompt overload during the augmentation phase?

Answer: Another significant problem arises when the retrieved documents are disjoint or unrelated. In such cases, the generation component may struggle to produce a coherent response, resulting in outputs that are confusing or difficult to understand. For instance, if the system retrieves documents with conflicting information or varying contexts, the generated response might lack a logical flow. This mismatch between retrieval and generation can reduce the overall effectiveness of the RAG system. Additionally, the presence of distractors, which are completely irrelevant documents retrieved due to their semantic similarity, can cause the language model to produce false predictions. Ingestion Stage: Bias in the dataset itself can also cause significant issues. Inherent biases present in the data can skew the system's responses.

-----

</details>

<details>
<summary>How do principles from cognitive psychology on human long-term memory retrieval and contextual reconstruction inform the design of more adaptive, iterative retrieval mechanisms in agentic RAG systems?</summary>

Phase: [EXPLORATION]

### Source [66]: https://www.kore.ai/blog/what-is-agentic-rag

Query: How do principles from cognitive psychology on human long-term memory retrieval and contextual reconstruction inform the design of more adaptive, iterative retrieval mechanisms in agentic RAG systems?

Answer: In Agentic RAG, retrieval is an iterative and adaptive process guided by the agent, continuously evaluating if retrieved information meets task requirements and adjusting strategy. Core concepts include dynamic query rewriting based on partial evidence, multi-hop retrieval where one result triggers another, cross-source retrieval combining vector search, keyword search, structured data, and domain-specific repositories, and confidence scoring and filtering to remove irrelevant or low-value items. This iterative loop accumulates relevant, complete, high-precision evidence before building context. Agentic RAG introduces agentic behavior, planning, decision-making, iterative refinement, and adaptive retrieval, transforming it from static to dynamic reasoning system that decides what to retrieve, how to refine, when to re-query, and how to structure reasoning for accurate, context-aware outcomes in multi-step tasks.

-----

-----

Phase: [EXPLORATION]

### Source [67]: https://pclub.in/roadmap/2025/11/01/agentic-ai-and-rag-guide/

Query: How do principles from cognitive psychology on human long-term memory retrieval and contextual reconstruction inform the design of more adaptive, iterative retrieval mechanisms in agentic RAG systems?

Answer: Long-term memory in AI agents mirrors human cognitive psychology categories. Retrieval involves embedding the agent's query, performing similarity search in vector database to find relevant stored memories, fed back into prompt for next action. This persistent knowledge store enables retention and recall across sessions. Advanced retrieval includes re-ranking: vector search fetches candidates, re-ranker re-orders by relevance. Adaptive retrieval (Self-Corrective RAG) uses loops where system retrieves documents, LLM grades relevance, decides to proceed or retrieve more based on grade, mimicking iterative refinement.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://openreview.net/pdf/efa7518ae97c78d6fa2dcbdb06e9a6bf5e799c97.pdf

Query: How do principles from cognitive psychology on human long-term memory retrieval and contextual reconstruction inform the design of more adaptive, iterative retrieval mechanisms in agentic RAG systems?

Answer: Human memory provides conceptual scaffold for LLM-based agents' memory. Cognitive psychology distinguishes interacting systems for perceiving, maintaining, reusing information (Baddeley 2020; Tulving 1972). Memory as interacting subsystems across time scales, with short-term for temporary retention. Iterative interaction suits agents for long-horizon, dynamic problem solving, emphasizing multi-step execution and tool-augmented decision making.

-----

-----

Phase: [EXPLORATION]

### Source [69]: https://www.preprints.org/manuscript/202601.0618/v1

Query: How do principles from cognitive psychology on human long-term memory retrieval and contextual reconstruction inform the design of more adaptive, iterative retrieval mechanisms in agentic RAG systems?

Answer: Tiered memory architectures inspired by human cognition balance capacity and latency. Cognitive-inspired systems like SWIFT–SAGE dynamically adjust retrieval intensity. Streaming-update architectures maintain long-term stability without exhaustive retrieval.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory

Query: How do principles from cognitive psychology on human long-term memory retrieval and contextual reconstruction inform the design of more adaptive, iterative retrieval mechanisms in agentic RAG systems?

Answer: GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in RAG, inspired by cognitive science, uses Kalman gain rules to dynamically strengthen memory states for repeated retrieval based on query feedback, addressing static indexing issues in traditional RAG.

-----

</details>

<details>
<summary>How do hierarchical indexing and multi-scale embedding approaches theoretically improve retrieval efficiency and context preservation in RAG systems handling complex enterprise document hierarchies?</summary>

Phase: [EXPLORATION]

### Source [76]: https://www.mdpi.com/2076-3417/16/2/903

Query: How do hierarchical indexing and multi-scale embedding approaches theoretically improve retrieval efficiency and context preservation in RAG systems handling complex enterprise document hierarchies?

Answer: To overcome the limitations of flat indexing, researchers have proposed various hierarchical indexing methods. RAPTOR constructs document trees through recursive abstraction, clustering and summarizing sentences layer by layer from leaf nodes to the root. This structure improves retrieval flexibility and precision, supporting multi-level retrieval with adaptive granularity based on query complexity. While RAPTOR’s bottom-up approach may face challenges in tasks requiring complete context, its concept has inspired subsequent optimizations. Recent domain-specific applications, such as the paradigm for construction management proposed by Wu et al., further demonstrate the importance of hierarchical structures in RAG systems. This approach parses project documents into hierarchical structures. In summary, RAG indexing has evolved from flat to hierarchical and graph-based forms, increasingly emphasizing semantic association and structural preservation. While flat structures are simple, hierarchical approaches better preserve document organization, and graph structures excel at representing complex associations. However, simultaneously maintaining structural integrity and supporting efficient retrieval remains challenging. The proposed HiSem-RAG addresses this by constructing a hierarchical index that retains the original document hierarchy while facilitating precise, adaptive retrieval. Semantics-based chunking methods aim to preserve the semantic integrity of text. By identifying semantic boundaries for segmentation, they retain key information and logical structure. The Small2Big approach by Yang et al. uses sentences as basic retrieval units and supplies context sentences to the language model, improving retrieval efficiency while maintaining semantic coherence. More recently, Krassovitskiy et al. investigated the use of LLM embeddings to capture semantic coherence and topic closure. Their work demonstrates that integrating embeddings with classical clustering and graph-based methods—including a proposed magnetic clustering algorithm—significantly improves segmentation quality, providing valuable insights for optimizing RAG systems.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://arxiv.org/html/2505.06569v1

Query: How do hierarchical indexing and multi-scale embedding approaches theoretically improve retrieval efficiency and context preservation in RAG systems handling complex enterprise document hierarchies?

Answer: Hierarchical retrieval approaches offer an alternative to post-retrieval compression by capturing longer or broader contexts during the retrieval phase. These methods organize information in hierarchical structures, aiming to improve both precision and recall. Recent work, such as GraphRAG (Edge et al., 2024) and HippoRAG (Gutiérrez et al., 2024), adopts hierarchical retrieval through symbolic graphs or sentence-level indexing, which improves coverage but introduces additional overhead. In contrast, MacRAG achieves similar benefits via dense, bottom-up expansion over pre-indexed multi-scale units without symbolic structure. Another line of work bypasses chunking altogether by retrieving entire passages or documents (Qian et al., 2024). While this simplifies retrieval, it reduces granularity control. MacRAG retains a flexible structure through hierarchical slicing and adaptive composition. Given a document corpus 𝒟={d1,…,dN}, MacRAG performs offline processing to construct a hierarchy through chunking, compression, and slicing, while building a slice-level vector DB at the finest granularity to enable retrieval. Instead of using raw sentences as the base unit, we use partial summaries to reduce redundancy and enhance semantic focus, which helps improve retrieval precision and reduces noise in the multi-scale expansion.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://www.meilisearch.com/blog/rag-indexing

Query: How do hierarchical indexing and multi-scale embedding approaches theoretically improve retrieval efficiency and context preservation in RAG systems handling complex enterprise document hierarchies?

Answer: Future RAG developments are moving toward hybrid retrieval methods, graph-enhanced approaches, and RAPTOR-style hierarchical indexing. RAG indexing is the process by which a RAG system organizes and prepares data so that, when prompted by a user query, the correct information can be easily retrieved. It takes the documents, chunks them into smaller pieces, creates vector representations of the chunks, and stores them in a special index so the system can quickly find them when needed. Chunk by meaning, not by fixed length: Instead of automatically slicing text every 300 tokens, break it around natural boundaries. This includes headings, paragraphs, bullet lists, or API endpoints. It keeps context intact and reduces confusion during retrieval. Speed: Without indexing, the system would have to scan every document in its entirety whenever someone asks a question. Indexing stores precomputed embeddings, so the system can instantly search and retrieve relevant chunks without having to search from scratch. Relevance: Because chunks are embedded and tagged with metadata, the algorithm can match a user’s query to the most meaningful pieces of text. This precise retrieval enhances the relevance of answers. Accuracy: Indexing preserves context and meaning. Since the retrieval step is cleaner and more targeted, the final answer generated is better grounded in correct information.

-----

-----

Phase: [EXPLORATION]

### Source [79]: https://pixion.co/blog/rag-strategies-hierarchical-index-retrieval

Query: How do hierarchical indexing and multi-scale embedding approaches theoretically improve retrieval efficiency and context preservation in RAG systems handling complex enterprise document hierarchies?

Answer: Hierarchical index retrieval overview. The retrieval executes in steps. We start with larger document segments and work towards the smaller chunks. On each level of the hierarchy, we only work with segments that we retrieved as relevant. Each level represents an arbitrary structure of a document. However, depending on the size of chapters and sections, we might opt for a less complicated plan. We can start with documents again but then retrieve the relevant chapters. From those chapters, we would retrieve relevant chunks. This approach provides a much shorter path while capitalizing on the strengths of the hierarchical approach. In the face of growing data volumes, hierarchical index retrieval stands as a robust strategy to improve data accuracy and scalability. This strategy, which organizes data into a hierarchy and progressively narrows down to the most relevant data, is versatile and adaptable to various use cases, from structured to unstructured data. Key to implementing this strategy is the use of summaries and metadata to navigate large chunks of data, and the use of AI models for automated summarization. Progressive narrowing in hierarchical index retrieval. On each level of the hierarchy, we test our query embedding against that level's summary embedding. If it's relevant, we can continue down the hierarchy for that specific part of the document.

-----

-----

Phase: [EXPLORATION]

### Source [80]: https://arxiv.org/html/2402.01767v2

Query: How do hierarchical indexing and multi-scale embedding approaches theoretically improve retrieval efficiency and context preservation in RAG systems handling complex enterprise document hierarchies?

Answer: The retrieval challenges posed by similar documents have not been fully addressed in existing RAG-based systems. Our practical experience has highlighted a particular multi-document question-answering scenario that standard RAG models struggle with. This involves large-scale document collections with approximately similar structures and content, such as product manuals from Texas Instruments, various iPhone models, company financial reports, and medical diagnosis and treatment manuals. In RAG, documents are typically segmented into chunks and converted into embeddings for storage, which are then used for subsequent retrieval. Therefore, the performance of the embedding model significantly impacts the effectiveness of RAG. Commonly used embedding models include BGE (Xiao et al. 2023), M3E1, OpenAI’s text-ada-002, and others. LlamaIndex (Smith and Doe 2023) employs a novel indexing strategy that integrates deep learning models with traditional information retrieval systems to create a dynamic query-responsive index. This system is particularly effective in environments where the information needs are diverse, and the document collections are large and complex.

-----

</details>

<details>
<summary>How can feedback loops and self-correction mechanisms grounded in reinforcement learning theory be theoretically integrated into agentic RAG to optimize iterative retrieval decisions without external tools?</summary>

Phase: [EXPLORATION]

### Source [81]: https://apxml.com/courses/large-scale-distributed-rag/chapter-6-advanced-rag-architectures-techniques/self-correcting-improving-rag

Query: How can feedback loops and self-correction mechanisms grounded in reinforcement learning theory be theoretically integrated into agentic RAG to optimize iterative retrieval decisions without external tools?

Answer: The core principle of self-correcting and self-improving RAG systems is the establishment of feedback loops. These loops capture signals about the system's performance, either explicit feedback from users or implicit signals derived from user behavior and downstream task success, and use these signals to refine one or more components of the RAG pipeline. To enable self-correction and improvement, several components must be integrated into the RAG architecture: 1. Feedback Collection Mechanisms: These are responsible for gathering data on system performance. Explicit Feedback: Direct input from users, such as thumbs up/down ratings on responses, corrected answers, relevance scores for retrieved documents, or annotations highlighting errors or hallucinations. UI elements are typically designed for this. Implicit Feedback: Indirect signals inferred from user behavior. Examples include click-through rates on retrieved sources, time spent on a generated answer, query reformulation patterns, or successful task completion in an agentic system. System-Internal Feedback: Signals generated by the system itself, such as confidence scores from the retriever or generator, internal consistency checks, or comparisons against a ground-truth dataset if available for certain sub-tasks. Advanced RAG architectures often incorporate mechanisms for self-correction and self-improvement, enabling them to adapt, learn from interactions, and enhance their accuracy and relevance dynamically. These systems evolve into more intelligent and responsive information retrieval solutions.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://arxiv.org/pdf/2512.06060

Query: How can feedback loops and self-correction mechanisms grounded in reinforcement learning theory be theoretically integrated into agentic RAG to optimize iterative retrieval decisions without external tools?

Answer: This paper introduces Reinforcement Infused Agentic RAG (RI-RAG) framework that integrates reinforcement learning (RL) with autonomous agents for continuous improvement. It employs AI agents that learn from QE feedback, assessments, and defect discovery outcomes to automatically improve test case generation strategies. The system uses RL algorithms like Proximal Policy Optimization (PPO) and Deep Q-Networks (DQN) to optimize agent behavior based on QE-reported test effectiveness, defect detection rates, and workflow metrics. State Space: Comprises the current QE workflow context, historical feedback patterns, test generation context, knowledge base state, and team performance metrics. Action Space: Includes agent-specific generation strategies, knowledge retrieval methods, validation approaches, and workflow integration options. Reward Function: A multi-dimensional score based on QE-assessed test effectiveness, defect detection success, workflow efficiency, and compliance validation. RL-Driven Vector Database Optimization: The vector database's retrieval mechanisms are optimized via RL, dynamically tuning retrieval parameters such as similarity thresholds and embedding models based on QE feedback patterns. Feedback results in progressively improving context retrieval and relationship modeling. The multi-dimensional reward framework enables simultaneous optimization across multiple quality dimensions without manual intervention. Key insights: RL-enhanced agents demonstrate superior adaptability; dynamic knowledge base updates driven by performance feedback result in progressively improving context.

-----

-----

Phase: [EXPLORATION]

### Source [83]: https://www.digitalocean.com/community/conceptual-articles/rag-ai-agents-agentic-rag-comparative-analysis

Query: How can feedback loops and self-correction mechanisms grounded in reinforcement learning theory be theoretically integrated into agentic RAG to optimize iterative retrieval decisions without external tools?

Answer: Agentic RAG innovates by broadening retrieval augmentation to multi-step context of autonomous agents. Agent Controller and Loop Structure: In Agentic RAG systems, the agent controller manages a complex multi-step loop that integrates retrieval and generation processes. This iterative cycle enables Agentic RAG systems to engage in complex reasoning tasks, self-correct, and improve performance. Handling Ambiguity and Uncertainty: Agentic RAG systems can address challenges with strategies in a continuous feedback loop. The motivation stems from use cases requiring context-aware generation and real-time actions, where the agent must analyze information, assess importance, determine response, and execute action in a continuous feedback loop. Technical exploration emphasizes adaptive agent controllers for effective retriever modules and generator models.

-----

-----

Phase: [EXPLORATION]

### Source [84]: https://machinelearning.apple.com/research/reinforcement-learning-integrated

Query: How can feedback loops and self-correction mechanisms grounded in reinforcement learning theory be theoretically integrated into agentic RAG to optimize iterative retrieval decisions without external tools?

Answer: This paper introduces a framework that integrates reinforcement learning (RL) with autonomous agents to enable continuous improvement in automated software test cases authoring. Reinforcement Infused Agentic RAG (RI-RAG) overcomes limitations of static systems by employing AI agents that learn from QE feedback, assessments, and defect discovery outcomes to improve test case generation strategies. It combines specialized agents with a hybrid vector-graph knowledge base. Through RL algorithms, specifically Proximal Policy Optimization (PPO) and Deep Q-Networks (DQN), agents optimize behavior based on QE-reported test effectiveness, defect detection rates, and workflow metrics. As QEs execute AI-generated test cases and provide feedback, the system learns from expert guidance to improve future iterations. The framework establishes a continuous knowledge refinement loop driven by QE expertise.

-----

-----

Phase: [EXPLORATION]

### Source [85]: https://arxiv.org/html/2603.07379v1

Query: How can feedback loops and self-correction mechanisms grounded in reinforcement learning theory be theoretically integrated into agentic RAG to optimize iterative retrieval decisions without external tools?

Answer: Agentic RAG features iterative, multi-step planning loops with policy-driven reasoning and explicit tool-calling. Unlike static RAG, it has explicit deliberative phase, read/write/prune capabilities over working memory, and can discard poor retrieval and try new query. Modules include Planner (self-correction on plan failure), Controller (observation-triggered replanning), Orchestrator (cross-agent consensus voting). Standard RAG lacks native correction loops for noisy retrievals. Agentic RAG provides adaptive multi-step decisions, addressing brittleness in knowledge-intensive tasks. Table compares Active RAG and Agentic RAG: Agentic has iterative loops, explicit planning, failure handling via self-correction.

-----

</details>

<details>
<summary>What theoretical principles from uncertainty estimation and calibration can be applied to detect and mitigate hallucinations specifically during the generation phase of RAG when retrieved context is incomplete or ambiguous?</summary>

Phase: [EXPLORATION]

### Source [86]: https://arxiv.org/html/2601.09929v1

Query: What theoretical principles from uncertainty estimation and calibration can be applied to detect and mitigate hallucinations specifically during the generation phase of RAG when retrieved context is incomplete or ambiguous?

Answer: Uncertainty Estimation metrics (e.g., token-level entropy, advanced methods) are self-contained and ideal for real-time hallucination monitoring during generation. Advanced Uncertainty Estimation methods like Monte Carlo dropout, ensemble variance, and Bayesian networks provide robust uncertainty quantification without requiring ground truth, suitable for detecting hallucinations when context is incomplete or ambiguous. Confidence Calibration in Uncertainty Estimation requires labeled data for measuring deviation between predicted confidence and observed accuracy, enabling detection of low-confidence generations indicative of hallucinations. These can be applied in real-time screening during the generation phase. The table indicates Uncertainty Estimation requires no ground truth (except calibration) and is for real-time screening. In mitigation (5.2 Root Cause–Aware Mitigation), once a hallucination is confirmed via uncertainty, the framework applies confidence calibration or decoding control specifically if the detection signal suggests uncertainty, which is relevant for incomplete or ambiguous retrieved context leading to uncertain generation.

-----

-----

Phase: [EXPLORATION]

### Source [87]: https://arxiv.org/html/2507.22915v1

Query: What theoretical principles from uncertainty estimation and calibration can be applied to detect and mitigate hallucinations specifically during the generation phase of RAG when retrieved context is incomplete or ambiguous?

Answer: Calibration and uncertainty quantification help the model judge when it might be wrong during generation, mitigating hallucinations in RAG. For tasks with provided source or retrieved context, attention alignment and source attribution detect hallucinations by checking if output statements correspond to attended input or context spans; lack of correspondence signals hallucination (extrinsic), applicable when context is incomplete or ambiguous. Challenges note that if retrieval fails or context is misinterpreted, hallucinations occur in generation; RAG reduces rates by grounding but needs uncertainty methods for detection. Calibrated decoding is listed as a mitigation strategy alongside uncertainty-based detection.

-----

-----

Phase: [EXPLORATION]

### Source [88]: https://www.mdpi.com/2227-7390/13/5/856

Query: What theoretical principles from uncertainty estimation and calibration can be applied to detect and mitigate hallucinations specifically during the generation phase of RAG when retrieved context is incomplete or ambiguous?

Answer: In the generation phase of RAG, hallucinations arise from context noise, context conflict, middle curse, alignment problems, or limited model capabilities when retrieved context is incomplete or ambiguous. Analyzing root causes in generation phase provides theoretical basis for mitigation strategies. RAG mitigates hallucinations by providing richer contextual information, but generation deficiency still introduces inconsistencies with retrieved information.

-----

-----

Phase: [EXPLORATION]

### Source [89]: https://aclanthology.org/2025.findings-acl.852.pdf

Query: What theoretical principles from uncertainty estimation and calibration can be applied to detect and mitigate hallucinations specifically during the generation phase of RAG when retrieved context is incomplete or ambiguous?

Answer: Theoretical axiomatic constraints for uncertainty estimation (UE) in RAG detect hallucinations during generation when context is incomplete or ambiguous. Theorem 2 (Negatively Consistent): If response unchanged after RAG but context contradicts it, UE should increase post-RAG, signaling misalignment useful for ambiguous/incomplete context. Theorem 5 (Neutrally Consistent): If response unchanged and context unrelated, UE remains similar. Reference-free calibration coefficient α_ax = k1 · E(r1, r2) + k2 · R(c, q, r1) + k3 · R(c, q, r2) calibrates UE for RAG: U_cal = (k4 - α_ax) · U, adjusting uncertainty based on response equivalence and context relations (entailment, contradiction, independence), directly addressing shortcomings in standard UE for RAG generation with incomplete/ambiguous context.

-----

-----

Phase: [EXPLORATION]

### Source [90]: https://www.aimon.ai/posts/how-to-fix-hallucinations-in-rag-llm-apps/

Query: What theoretical principles from uncertainty estimation and calibration can be applied to detect and mitigate hallucinations specifically during the generation phase of RAG when retrieved context is incomplete or ambiguous?

Answer: In RAG generation phase, hallucinations occur if model struggles to align retrieved data with query, especially with incomplete or ambiguous queries leading to synthesis of non-present details. Retrieval limitations like tangentially related or incorrect data compromise generation.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="advanced-rag-techniques-for-high-performance-llm-application.md">
<details>
<summary>Advanced RAG Techniques for High-Performance LLM Applications</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://neo4j.com/blog/genai/advanced-rag-techniques/>

# Advanced RAG Techniques for High-Performance LLM Applications

https://dist.neo4j.com/wp-content/uploads/20240517073021/tomaz-bratanic-150x150.jpeg

https://dist.neo4j.com/wp-content/uploads/20251015110239/isobel-kruger-150x150.jpeg

[Tomaž Bratanič](https://neo4j.com/blog/contributor/tomaz-bratanic/),

[Isobel Krüger](https://neo4j.com/blog/contributor/isobel-kruger/)

October 17, 2025

17 min read

https://dist.neo4j.com/wp-content/uploads/20251015112403/advanced-rag-techniques.png

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by combining retrieval with generation to ground outputs in your own data rather than relying solely on pretraining. In practice, RAG systems retrieve relevant information from a knowledge source and integrate it into the prompt, enabling responses that are more accurate, contextual, and trustworthy.

RAG is now a widely used architecture for LLM applications, powering everything from question-answering services that leverage web search, to internal chat tools that index enterprise content, to complex QA pipelines. Its appeal is simple: by augmenting generation with retrieval, teams can deliver LLM experiences that meet today’s expectations for relevance and reliability.

But shipping a RAG system isn’t the finish line. Anyone who’s moved beyond a prototype knows the symptoms: hallucinations creep back in, long queries bog down performance, or answers miss the mark despite the right documents being retrieved. That’s where advanced RAG techniques come in. This guide walks through the strategies that help teams improve relevance, accuracy, and efficiency, so your system not only works, but works at scale.

## RAG Architecture

A typical RAG pipeline is simple to describe but also easy to underbuild for production. Understanding the RAG architecture baseline and why basic setups struggle helps you move into advanced RAG techniques with the right context.

### What the RAG Pipeline Does

A standard RAG system does four things:

1.  **Ingests content**: splits documents into chunks, adds metadata, and creates embeddings.
2.  **Indexes**: builds a store for efficient retrieval, often a vector index, sometimes with a keyword index as well.
3.  **Retrieves**: fetches top-k context for a query.
4.  **Generates**: prompts the model with the query plus the retrieved context and returns an answer.

At runtime, the system encodes the user’s query with the same model used to embed documents during ingestion, searches the index for the nearest vectors, retrieves the top-k chunks, and includes those chunks with the query in the prompt.

https://dist.neo4j.com/wp-content/uploads/20251015123017/standard-rag-system.pngThe basic RAG process

### A Typical Failure Mode

Naive pipelines often perform well in demos but break in production.

This might sound familiar: You ship a quick RAG helper for your team. It nails simple fact lookups. Then a PM asks, “Which enterprise customers renewed last quarter and also opened support tickets about SSO?” The bot replies with a partial list, misses a couple of key accounts, and adds an irrelevant customer.

Here are some common symptoms you’ll recognize:

-   Top-k returns near duplicates or shallow snippets, so the prompt lacks diversity.
-   Retrieval misses proper nouns, IDs, or acronyms (SKU-123, SSO, SOC 2) because they occur rarely.
-   Answers cite the wrong entity or mix details across similar accounts.
-   Latency climbs when you raise _k_, use longer chunks, or rerun retrieval after follow-ups.
-   Poor table and PDF splitting drops headers or footnotes that change meaning.
-   Multi-turn chats drop constraints (“only EMEA,” “last quarter”), so follow-ups forget earlier filters, leading to off-scope answers.
-   Thin retrieval sets push the model to guess and fill in unsupported details.

## Why Basic RAG Breaks (And How Advanced RAG Techniques Help)

Because RAG couples approximate retrieval with probabilistic generation and small context windows, a few recurring failure modes show up in production. These issues usually show up in logs and traces:

-   **Vector-only retrieval** is semantic and can miss exact tokens and rare strings. Without hybrid search, names and codes slip through.
-   **Chunking boundaries** cut across structure, so the model sees fragments without the right context.
-   **No reranking** means cosine similarity rewards proximity, not usefulness.
-   **Missing filters** (time, source, region) let off-scope documents into the prompt.
-   **Limited query understanding** (no expansion or decomposition) under-retrieves for multi-hop questions.
-   **Limited context window** forces you to drop good passages or rely on summaries that lose detail.
-   **No feedback loop** to detect weak context before generation, for example, a simple CRAG-style check.
-   **No graph context** to connect entities and events, so cross-document reasoning fails.
-   **Stale embeddings or indices** after data changes, which means that retrieved data reflects yesterday’s state.

An advanced RAG architecture strengthens what the model sees and how it reasons. It finds better evidence, keeps only what matters, connects it across sources, and verifies the result with citations, so answers are accurate, explainable, and repeatable at scale.

https://dist.neo4j.com/wp-content/uploads/20251015123543/naive-rag-versus-advanced-rag.pngInfographic comparing naive and advanced RAG

## Advanced RAG Advantages and Techniques to Get You There

Advanced generally means better retrieval, better context management, and better answer creation. Below, we list the main advantages of an advanced RAG architecture with go-to techniques.

### Improved Retrieval Quality and Relevance

Retrieval decides what the model even looks at. Most production RAG starts with dense retrieval (embeddings), which is strong for semantic matches but can miss rare terms, IDs, or acronyms. Advanced retrieval goes beyond this baseline with techniques that layer precision, coverage, and structure:

#### Knowledge Graph Retrieval ([opens in new tabGraphRAG](https://neo4j.com/blog/genai/what-is-graphrag/))

When your content contains rich entities and relationships (such as people, products, cases, citations), a knowledge graph lets you retrieve the _context of your data_, not just similar text. You can blend graph traversals with vector search to assemble precise, connected context for the prompt.

**Why graphs matter:** Vector/semantic search is strong for local lookups but struggles with global, cross-document questions and multi-hop relationships. Start by modeling your sources as entities and relationships, then retrieve in two ways: run local traversals to pull related entities and paths around initial hits, and use global community summaries for big-picture questions. This [opens in new tabstructured approach](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/) makes it much easier to retrieve and use specific information, expanding the types of questions you can answer with greater accuracy.

https://dist.neo4j.com/wp-content/uploads/20251016143611/graphrag-impact-diagram.jpg

#### Hybrid Retrieval (Semantic + Lexical)

Semantic retrieval encodes queries and documents into embeddings to match by meaning. Lexical retrieval (e.g., BM25 or SPLADE) matches exact terms. Semantic search excels at understanding meaning, but it can miss rare terms like IDs, codes, or proper nouns. Hybrid search covers both: pair a keyword-based retriever with dense embeddings, then combine their results using **Reciprocal Rank Fusion (RRF)** — a standard way of merging ranked lists — so the model sees passages that contain both the right meaning and the right tokens.

#### Filtering

Apply metadata rules (source, date, author, doc type) and semantic thresholds after you’ve extracted or enriched those fields from the raw docs. This removes low-quality or irrelevant hits before or alongside reranking, which reduces prompt bloat and improves grounding.

#### Reranking

After the first pass, rerank with a cross‑encoder or a rerank service so the top‑k you send to the LLM is truly the best. Reranking commonly improves top-k ordering when used after first-pass retrieval.

### Make Documents Easier to Retrieve and Use

Raw documents rarely fit cleanly into a prompt. How you split them, keep structure, add metadata, and condense context determines what gets retrieved and how useful it is in a tight token budget.

Here’s how you can keep signal, drop noise, and send the model the parts that matter:

#### Chunking

Chunk sizes and boundaries strongly influence retrieval quality. Default to fixed-size or sentence-aware splits, layer in semantic chunking when boundaries are messy, and reach for document-aware/adaptive chunkers when structure matters (table, headers, code). When you’re ready to wire it up, the [opens in new tabLangChain text-splitter docs](https://python.langchain.com/api_reference/text_splitters/) have drop-in examples.

#### Parent Retriever

Keep document structure intact by retrieving smaller “child” chunks but swapping in the “parent” block when many children from the same section appear, preserving context and reducing fragmented prompts.

#### Text Summarization / Context Distillation

Summarize the hits so more relevant info fits in the window and the model focuses on the right facts. Most stacks support this: [opens in new tabGraphRAG uses query-focused summarization](https://neo4j.com/blog/what-is-graphrag/), LangChain has a ContextualCompressionRetriever, and LlamaIndex offers tree/refine synthesizers.

#### Memory Augmentation for Conversations

For multi-turn chat, track conversation history and use retrieval-based memory so the system selectively recalls past turns instead of injecting full transcripts. Combine this with dynamic context windowing so follow-ups inherit the right context without bloating the prompt.

### Improve Query Understanding

Sometimes the way a question is written doesn’t match how your docs are written. Add a small query-understanding layer so you can rewrite or expand the question and give retrieval a better shot at finding the right passages without overfetching. Keep this step simple and inspectable.

#### Hypothetical Questions as a Retrieval Variant

Generate representative questions (or, in HyDE-style approaches, a hypothetical _answer_) from each chunk and index those. At query time, match the user question to those pre-generated items to improve semantic alignment.

#### Query Expansion

Add synonyms and related terms, or generate a few query variants, to bridge wording gaps between the question and your docs. This often boosts recall without sacrificing precision (when paired with filtering/reranking).

### Handle Complex, Multi‑Step Questions with Agentic Planning

Multi-step questions often require agentic planning. Sometimes referred to as an agent loop, this approach involves an agent breaking a problem into sub-questions, choosing the right tool for each (graph queries, hybrid retrieval, calculators), and orchestrating the loop: plan → route → act → verify → stop. This ensures coverage, provenance, and less guessing. Here’s how advanced agentic planning plays out in practice:

#### Multi-Step Reasoning or Multi-Hop QA

Some questions require stitching facts across people, events, and time. A single top-k pull often misses links. Break a complex question into smaller sub-questions and let an agent route each to the best retriever (graph/Cypher for relationships/joins; hybrid/semantic+lexical for facts and dates), then synthesize with per-claim citations. If any hop returns weak evidence, expand retrieval or ask a clarifying question before finalizing.

#### Agentic Planning Workflow

To increase the proportion of hops that have sufficient high-quality evidence that leads to a traceable source, use agentic planning to plan the steps, route each to the right tool, verify the evidence, and stop when the answer is supported; this preserves provenance and reduce hallucinations. Use the points below as a short checklist for multi-step questions:

1.  Break the question into concrete tasks (entities to find, time windows, joins/paths).
2.  Choose the best tool per task (graph/Cypher for relationships and joins; hybrid retrieval for facts/dates; calculator/code when needed).
3.  Execute the query or retrieval and collect evidence with provenance.
4.  Check coverage (does each sub-goal have strong evidence?) and conflicts (do sources disagree?). If weak, try again, broaden your approach, or switch tools.
5.  Conclude when all sub-goals are satisfied or when you hit the budget (max hops/tool calls/tokens). Provide the answer with per-claim citations or state what evidence is missing.

#### Chain-of-Thought Prompting (CoT)

Some tasks benefit when the model plans or reasons in steps instead of jumping to an answer. Use CoT as the agent’s private scratchpad to outline hops and track intermediate findings, then return a concise, source-grounded answer with citations. CoT improves multi-step inference but requires strict grounding rules (e.g., “answer only from retrieved sources; say ‘I don’t know’ if unsupported”). For higher accuracy, you can sample multiple plans/chain candidates and pick the best-supported synthesis. Use CoT for reasoning-heavy queries, not for simple lookups or latency-sensitive tasks.

### Ground Answers and Reduce Hallucinations

Even with good retrieval, models may still guess when supporting passages are thin or off‑topic. Use these fixes to keep answers tied to evidence in the data and add a simple safety check when retrieval isn’t strong enough:

#### Grounding

Instruct the model to answer only from retrieved sources. Add this to your prompt: “Answer only from the retrieved sources listed below. If the answer isn’t supported, say ‘I don’t know.’ Include source/citation IDs next to claims.”

Combine strict prompts with reference tags or citation IDs and block unsupported text. (This belongs in your prompt template and evaluation rubric.)

#### Corrective RAG (CRAG)

When strong retrieval pipelines return incomplete or irrelevant context, CRAG adds a lightweight feedback loop: before generating, the system checks whether the retrieved set is good enough. If it looks weak, the system triggers another retrieval pass or applies stricter filters and then proceeds. This self-check step helps reduce hallucinations and keeps answers tied to stronger evidence.

## How to Build an Advanced RAG Pipeline

Build an advanced RAG system by first structuring data into a knowledge graph, then layering graph-aware retrieval and an agentic plan–route–act–verify–stop loop. Choose a framework path like LangChain/LangGraph or LlamaIndex and measure impact with retrieval, answer-quality, and ops metrics.

### Structure Your Sources

Extract entities, relations, and key attributes from PDFs/web/text into a property graph (nodes, edges, properties). Keep provenance (source IDs, spans, timestamps) and optional embeddings per chunk or node so you can blend graph hops with lexical/semantic search. Define a lightweight schema early (entity/edge types, required properties). Store confidence scores on extracted fields and down-weight or ignore low-confidence metadata at query time.

### Use Agentic Planning for Complex Questions

For multi-hop/global questions, run a simple loop:

-   Plan sub-goals (which entities, which joins/paths, which time windows).
-   Route each sub-goal to the best tool: graph traversal via a graph query language (e.g., Cypher in property graphs) for relationships and joins; hybrid retrieval (lexical + semantic) for facts, names, and dates; optional calculators/code for transformations.
-   Act and verify: execute, check coverage/conflicts, use community/cluster summaries for global questions and path-bounded traversals (k-hop with type/time constraints) to keep context precise and auditable; broaden or switch tools if evidence is weak; apply termination criteria and budgets (max hops/tool calls/tokens) to prevent open-ended tool use; stop when all sub-goals are satisfied or the budget is reached.

### Evaluate Your Advanced RAG Tactics

Don’t skimp on evaluation. You can create a solid evaluation baseline by measuring:

-   **Retrieved-context relevance.** Is the context actually useful for the question?
-   **Groundedness/faithfulness.** Does the answer stick to the retrieved sources?
-   **Answer relevance.** Does it answer the user’s question?
-   **Ranking metrics for retrieval.** For example, trackMRR/Recall@k and latency for end-to-end UX.

When you introduce graphs, add simple explainers. For example, show which nodes/edges and passages supported an answer. This increases trust and makes debugging easier.

## A Practical Plan Using Advanced RAG Techniques

Practice makes perfect. Use this sequence to add improvements safely and see what actually moves the needle. Make one change, measure it, and then move to the next.

1.  **Stabilize basic retrieval:** Start with good embeddings, sensible chunking, and clean metadata. Add a reranker so the top-k results are stronger, then measure to establish a baseline.
2.  **Add hybrid search:** Combine BM25 with vectors (via Reciprocal Rank Fusion or RRF) to catch both exact tokens and semantic matches. Track precision@k, Recall@k and groundedness to see the lift.
3.  **Introduce query understanding:** Use query expansion and HyDE (hypothetical questions/documents) to bridge phrasing gaps and improve recall without overfetching.
4.  **Optimize context supply:** Use parent-doc logic and summarization/context distillation to fit more _relevant_ content into the window.
5.  **Structure your data as entities and relationships:** Extract and normalize key entities (people, orgs, products, IDs) and their relationships with provenance, then load them into a lightweight knowledge graph. Index nodes/edges alongside text so retrieval can pull paths and not just passages.
6.  **Enable agentic multi-step Q&A:** Use an agent to handle multi-hop questions: plan sub-goals, route each to the right tool, execute, verify coverage and resolve conflicts, stop within budget, and return answers with per-claim citations and auditable paths.
7.  **Harden grounding:** Lock answers to retrieved sources with strict prompts, CRAG-style retrieval checks, and citation tagging to cut hallucinations.

https://dist.neo4j.com/wp-content/uploads/20251016143758/graphrag-phases-diagram.jpg

## Start Practicing Advanced RAG

Want to move from a demo to something dependable? Kick off the process with a small baseline of test queries and a couple of metrics. Then make one change at a time and measure the impact.

-   **Pick one improvement at a time.** Start with reranking or hybrid search. Both are low-risk and high-return. Measure changes on a fixed eval set.
-   **Track your pipeline.** Log retrieved chunks, scores, graph paths, and citations for each answer.
-   **Integrate with your framework of choice.** Frameworks like LangChain, LangGraph, or LlamaIndex can help orchestrate advanced RAG pipelines, but the graph-aware pieces come from Neo4j’s ecosystem.
    -   **LangChain / LangGraph**: Use them for orchestration (e.g., routing sub-questions to the right tool, managing agents, and handling plan → route → act → verify → stop loops). Pair them with Neo4j’s GenAI ecosystem components like [opens in new tabLLM Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/) (to create knowledge graphs) and [opens in new tab Model Context Protocol](https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/) (to connect agents and LLMs to graph queries). Read this [blog post](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/) to learn how to use the [opens in new tabneo4j-advanced-rag template](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-advanced-rag) and host it using LangServe.
    -   **LlamaIndex**: Use Graph Index / Query Engine for path-bounded traversals and sub-question decomposition. Pair graph retrieval with document retrievers, apply post-processors (dedupe, compression), and rerank before generation. Parent-child retrieval or embedding hybrids are especially useful when structure or multi-hop reasoning matters.
-   **Adopt CRAG patterns.** It’s essential for high-stakes domains such as legal, compliance, or support deflection with strict SLAs.
-   **Plan for scale.** Use hybrid indices, approximate‑nearest‑neighbor vector search (ANN), and caching of common queries to cut latency without losing quality. Keep evaluations running as you optimize.

https://dist.neo4j.com/wp-content/uploads/20251015125205/implementing-advanced-rag-diagram.png

### Where to Go From Here

Advanced RAG is about steady, incremental improvements across retrieval, context management, and generation (not a single trick).

To get your RAG ship-ready, start with reranking and hybrid search, add query understanding and context distillation, and bring in multi-step reasoning with a knowledge graph. Advanced RAG patterns benefit from graph-based retrieval through improved relevance and explainability. A Neo4j knowledge graph paired with an LLM delivers:

-   **Relevancy:** Obtain more relevant answers compared to just vector searches
-   **Context:** Includes domain-specific, factual, structured knowledge on your subject
-   **Explainability:** Provide the user with more reasoning on how the results were obtained.
-   **Security:** Role-based access control (RBAC) with fine-grained privileges on labels, relationships, and properties.

## Advanced RAG: FAQs

**What are some advanced RAG techniques?**

If your basic pipeline still hallucinates or misses exact identifiers, you need techniques that get more precise results, keep structure, and keep answers grounded.

Start with hybrid retrieval (vector + keyword), metadata filtering, reranking, and structure‑aware chunking/parent‑doc. Then, layer summarization, query expansion/HyDE, multi‑step reasoning, grounding/CRAG, and retrieval‑based memory as needed.

**How do advanced RAG techniques improve accuracy in complex queries?**

Complex questions fail when retrieval lacks coverage and the model guesses. These methods raise recall and precision while keeping grounding in place. Hybrid + expansion finds the right docs, reranking and parent‑doc/summarization surface the right passages, and CRAG catches weak evidence before you answer.

**What role do knowledge graphs play in enhancing RAG systems?**

A knowledge graph unifies scattered documents, tables, and APIs into a connected picture of your data. With entities and relationships mapped out, GraphRAG retrieves along those connections, improving disambiguation, supporting multi-hop answers, and keeping sources traceable.

-   [llm](https://neo4j.com/blog/tag/llm/)
-   [rag](https://neo4j.com/blog/tag/rag/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop.md">
<details>
<summary>Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/>

# Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop

A practical guide to choosing between single-pass pipelines and adaptive retrieval loops based on your use case's complexity, cost, and reliability requirements

Mostafa Ibrahim

Mar 3, 2026

11 min read

https://towardsdatascience.com/wp-content/uploads/2026/03/classic-vs-agentic-rag-2.jpg

## Introduction: Why this comparison matters

[RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) began with a straightforward goal: ground model outputs in external evidence rather than relying solely on model weights. Most teams implemented this as a pipeline: retrieve once, then generate an answer with citations.

Over the last year, more teams have started moving from that “one-pass” pipeline towards agent-like loops that can retry retrieval and call tools when the first pass is weak. [Gartner](https://www.gartner.com/en/newsroom/press-releases/2023-11-29-gartner-says-more-than-80-percent-of-enterprises-will-have-used-generative-ai-apis-or-deployed-generative-ai-enabled-applications-by-2026) even forecasts that **33% of enterprise software applications will include agentic AI by 2028**, a sign that “agentic” patterns are becoming mainstream rather than niche.

[Agentic RAG](https://arxiv.org/abs/2301.11913) changes the system structure. Retrieval becomes a control loop: retrieve, reason, decide, then retrieve again or stop. This mirrors the core pattern of “reason and act” approaches, such as [ReAct](https://arxiv.org/abs/2210.03629), in which the system alternates between reasoning and action to gather new evidence.

However, agents do not enhance RAG without tradeoffs. Introducing loops and tool calls increases adaptability but reduces predictability. Correctness, latency, observability, and failure modes all change when debugging a process instead of a single retrieval step.

## Classic RAG: the pipeline mental model

Classic RAG is straightforward to understand because it follows a linear process. A user query is received, the system retrieves a fixed set of passages, and the model generates an answer based on that single retrieval. If issues arise, debugging usually focuses on retrieval relevance or context assembly.

At a high level, the pipeline looks like this:

1. **Query:** take the user question (and any system instructions) as input
2. **Retrieve:** fetch the top-k relevant chunks (usually via vector search, sometimes hybrid)
3. **Assemble context:** Select and arrange the best passages into a prompt context (often with reranking)
4. **Generate:** Produce an answer, ideally with citations back to the retrieved passages

https://contributor.insightmediagroup.io/wp-content/uploads/2026/02/classic-rag-pipeline.png

### What classic RAG is good at

Classic RAG is most effective when predictable cost and latency are priorities. For straightforward “doc lookup” questions such as “What does this configuration flag do?”, “Where is the API endpoint for X?”, or “What are the limits of plan Y?”, a single retrieval pass is typically sufficient. Answers are delivered quickly, and debugging is direct: if outputs are incorrect, first check retrieval relevance and chunking, then review prompt behavior.

**Example (classic RAG in practice):**

A user asks: “What does the `MAX_UPLOAD_SIZE` config flag do?”

The retriever pulls the configuration reference page where the flag is defined.

The model answers in one pass, “It sets the maximum upload size allowed per request”, and cites the exact section.

There are no loops or tool calls, so cost and latency remain stable.

### Where classic RAG hits the wall

Classic RAG is a [“one-shot” approach](https://arxiv.org/abs/2205.01068). If retrieval fails, the model lacks a built-in recovery mechanism.

That shows up in a few common ways:

- **Multi-hop questions**: the answer needs evidence spread across multiple sources
- **Underspecified queries**: the user’s wording is not the best retrieval query
- **Brittle chunking:** relevant context is split across chunks or obscured by jargon
- **Ambiguity:** the system may need to ask clarifying questions, reformulate, or explore further before providing an accurate answer.

**Why this matters:**

When classic RAG fails, it often does so quietly. The system still provides an answer, but it may be a confident synthesis based on weak evidence.

## Agentic RAG: from retrieval to a control loop

Agentic RAG retains the retriever and generator components but changes the control structure. Instead of relying on a single retrieval pass, retrieval is wrapped in a loop, allowing the system to review its evidence, identify gaps, and attempt retrieval again if needed. This loop gives the system an “agentic” quality: it not only generates answers from evidence but also actively chooses how to gather stronger evidence until a stop condition is met. A helpful analogy is incident debugging: classic RAG is like running one log query and writing the conclusion from whatever comes back, while agentic RAG is a debug loop. You query, inspect the evidence, notice what’s missing, refine the query or check a second system, and repeat until you’re confident or you hit a time/cost budget and escalate.

A minimal loop is:

1. **Retrieve:** pull candidate evidence (docs, search results, or tool outputs)
2. **Reason:** synthesize what you have and identify what’s missing or uncertain
3. **Decide:** stop and answer, refine the query, switch sources/tools, or escalate

For a research reference, ReAct provides a useful mental model: reasoning steps and actions are interleaved, enabling the system to gather more substantial evidence before finalizing an answer.

### What agents add

**Planning (decomposition)**

The agent can decompose a question into smaller evidence-based objectives.

Example: “Why is SSO setup failing for a subset of users?”

- What error codes are we seeing?
- Which IdP configuration is used
- Is this a docs question, a log question, or a configuration question

Classic RAG treats the entire question as a single query. An agent can explicitly determine what information is needed first.

**Tool use (beyond retrieval)**

In agentic RAG, retrieval is one of several available tools. The agent may also use:

- A second index
- A database query
- A search API
- A config checker
- A lightweight verifier

This is important because relevant answers often exist outside the documentation index. The loop enables the system to retrieve evidence from its actual source.

**Iterative refinement (deliberate retries)**

This represents the most significant advancement. Instead of attempting to generate a better answer from weak retrieval, the agent can deliberately requery.

[Self-RAG](https://arxiv.org/abs/2310.11511) is a good example of this research direction: it is designed to retrieve on demand the critique of retrieved passages and to generate them, rather than always using a fixed top-k retrieval step.

This is the core capability shift: the system can adapt its retrieval strategy based on information learned during execution.

https://contributor.insightmediagroup.io/wp-content/uploads/2026/02/agentic-rag-loop.png

## Tradeoffs: Benefits and Drawbacks of Loops

Agentic RAG is beneficial because [it can repair retrieval](https://arxiv.org/abs/2310.01558) rather than relying on guesses. When the initial retrieval is weak, the system can rewrite the query, switch sources, or gather additional evidence before answering. This approach is better suited for ambiguous questions, multi-hop reasoning, and situations where relevant information is dispersed.

However, introducing a loop changes production expectations. What do we mean by a **“loop”**? In this article, a loop is one complete iteration of the agent’s control cycle: Retrieve → Reason → Decide, repeated until a stop condition is met (high confidence + citations, max steps, budget cap, or escalation). That definition matters because once retrieval is iterative, cost and latency become [distributions](https://en.wikipedia.org/wiki/Fat-tailed_distribution): some runs stop quickly, while others take extra iterations, retries, or tool calls. In practice, you stop optimizing for the “typical” run and start managing **tail behavior** (p95 latency, cost spikes, and worst-case tool cascades).

Here’s a tiny example of what that Retrieve → Reason → Decide loop can look like in code:

```python
# Retrieve → Reason → Decide Loop (agentic RAG)
evidence = []
for step in range(MAX_STEPS):
    docs = retriever.search(query=build_query(user_question, evidence))
    gaps = find_gaps(user_question, docs, evidence)
    if gaps.satisfied and has_citations(docs):
        return generate_answer(user_question, docs, evidence)
    action = decide_next_action(gaps, step)
    if action.type == "refine_query":
        evidence.append(("hint", action.hint))
    elif action.type == "call_tool":
        evidence.append(("tool", tools[action.name](action.args)))
    else:
        break  # safe stop if looping isn't helping
return safe_stop_response(user_question, evidence)
```

### Where loops help

Agentic RAG is most valuable when “retrieve once → answer” isn’t enough. In practice, loops help in three typical cases:

1. The question is underspecified and needs query refinement
2. The evidence is spread across multiple documents or sources
3. The first retrieval returns partial or conflicting information, and the system needs to verify before committing

### Where loops hurt

The tradeoff is operational complexity. With loops, you introduce more moving parts (planner, retriever, optional tools, stop conditions), which increases variance and makes runs harder to reproduce. You also expand the surface area for failures: a run might look “fine” at the end, but still burn tokens through repeated retrieval, retries, or tool cascades.

This is also why [“enterprise RAG”](https://arxiv.org/abs/2404.16130) tends to get tricky in practice: security constraints, messy internal data, and integration overhead make naive retrieval brittle.

## Failure modes you’ll see early in production

Once you move from a pipeline to a control loop, a few problems show up repeatedly:

- **Retrieval thrash:** the agent keeps retrieving without improving evidence quality.
- **Tool-call cascades:** one tool call triggers another, compounding latency and cost.
- **Context bloat:** the prompt grows until quality drops or the model starts missing key details.
- **Stop-condition bugs:** the loop doesn’t stop when it should (or stops too early).
- **Confident-wrong answers:** the system converges on noisy evidence and answers with high confidence.

A key perspective is that classic RAG primarily fails due to retrieval quality or prompting. Agentic RAG can encounter these issues as well, but also introduces control-related failures, such as poor decision-making, inadequate stop rules, and uncontrolled loops. As autonomy increases, observability becomes even more critical.

## Quick comparison: Classic vs Agentic RAG

| Dimension | Classic RAG | Agentic RAG |
| --- | --- | --- |
| Cost predictability | High | Lower (depends on loop depth) |
| Latency predictability | High | Lower (p95 grows with iterations) |
| Multi-hop queries | Often weak | Stronger |
| Debugging surface | Smaller | Larger |
| Failure modes | Mostly retrieval + prompt | Adds loop control failures |

## Decision Framework: When to stay classic vs go agentic

A practical approach to choosing between classic and agentic RAG is to evaluate your use case along two axes: query complexity (the extent of multi-step reasoning or evidence gathering required) and error tolerance (the risk associated with incorrect answers for users or the business). Classic RAG is a strong default due to its predictability. Agentic RAG is preferable when tasks frequently require retries, decomposition, or cross-source verification.

### Decision matrix: complexity × error tolerance

Here, **high error tolerance** means a wrong answer is acceptable (low stakes), while **low error tolerance** means a wrong answer is costly (high stakes).

| | High error tolerance | Low error tolerance |
| --- | --- | --- |
| Low Complexity | **Classic RAG** for fast answers and predictable latency/cost. | **Classic RAG** with citations, careful retrieval, escalation |
| High Complexity | **Classic RAG + second pass on failure signals** (only loop when needed). | **Agentic RAG** with strict stop conditions, budgets, and debugging |

### Practical gating rules (what to route where)

Classic RAG is usually the better fit when the task is mostly lookup or extraction:

- FAQs and documentation Q&A
- Single-document answers (policies, specs, limits)
- Fast assist where latency predictability matters more than perfect coverage

Agentic RAG is usually worth the added complexity when the task needs multi-step evidence gathering:

- Decomposing a question into sub-questions
- Iterative retrieval (rewrite, broaden/narrow, switch sources)
- Verification and cross-checking across sources/tools
- Workflows where “try again” is required to reach a confident, cited answer.

A simple rule: **don’t pay for loops unless your task routinely fails in one pass**.

## Rollout guidance: add a second pass before going “full agent.”

You do not need to choose between a permanent pipeline and full agentic implementation. A practical compromise is to use classic RAG by default and trigger a second-pass loop only when failure signals are detected, such as missing citations, low retrieval confidence, contradictory evidence, or user follow-ups indicating the initial answer was insufficient. This approach keeps most queries efficient while providing a recovery path for more complex cases.

https://contributor.insightmediagroup.io/wp-content/uploads/2026/02/agentic-rag-decision-loop.png

### Core Takeaway

Agentic RAG is not simply an improved version of RAG; it is RAG with an added control loop. This loop can enhance correctness for complex, ambiguous, or multi-hop queries by allowing the system to refine retrieval and verify evidence before answering. The tradeoff is operational: increased complexity, higher tail latency and cost spikes, and additional failure modes to debug. Clear budgets, stop rules, and traceability are essential if you adopt this approach.

## Conclusion

If your product primarily involves document lookup, extraction, or rapid assistance, classic RAG is typically the best default. It is simpler, more cost-effective, and easier to manage. Consider agentic RAG only when there is clear evidence that single-pass retrieval fails for a significant portion of queries, or when the cost of incorrect answers justifies the additional verification and iterative evidence gathering.

A practical compromise is to begin with classic RAG and introduce a controlled second pass only when failure signals arise, such as missing citations, low retrieval confidence, contradictory evidence, or repeated user follow-ups. If second-pass usage becomes frequent, implementing an agent loop with defined budgets and stop conditions may be beneficial.

For further exploration of improved retrieval, evaluation, and tool-calling patterns, the following references are recommended.

- [Dense Passage Retrieval (DPR)](https://arxiv.org/abs/2004.04906)
- [HyDE (query expansion for better retrieval)](https://arxiv.org/abs/2212.10496)
- [BEIR benchmark (evaluate retrievers beyond one dataset)](https://arxiv.org/abs/2104.08663)
- [RAGAS (RAG evaluation framework)](https://arxiv.org/abs/2309.15217)
- [Toolformer](https://arxiv.org/abs/2302.07842)
- [FiD-style multi-document generation](https://arxiv.org/abs/2007.01282)

---

Written By

Mostafa Ibrahim

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="fine-tuning-vs-retrieval-augmented-generation-for-llms.md">
<details>
<summary>Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://neo4j.com/blog/developer/fine-tuning-vs-rag/>

# Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation

https://dist.neo4j.com/wp-content/uploads/20240517073021/tomaz-bratanic-150x150.jpeg

https://dist.neo4j.com/wp-content/uploads/20250217051229/kumar-harsh-150x150.jpeg

[Tomaž Bratanič](https://neo4j.com/blog/contributor/tomaz-bratanic/),

[Kumar Harsh](https://neo4j.com/blog/contributor/kumar-harsh/)

September 11, 2024

14 min read

https://dist.neo4j.com/wp-content/uploads/20240911090339/fine-tuning-vs-rag.png

Many organizations are considering LLMs for business use cases like answering questions as chatbots or virtual assistants or generating creative text. However, they usually run into limitations such as knowledge cutoff, hallucinations, and the lack of user customization.

Two approaches that address these challenges are **fine-tuning** and **retrieval-augmented generation**. Fine-tuning an LLM involves a supervised training phase, where question-answer pairs are provided to optimize the LLM’s performance. Conversely, in [retrieval-augmented generation](https://neo4j.com/blog/genai/what-is-retrieval-augmented-generation-rag/) (RAG), the LLM serves as a natural language interface to access external information, which means it doesn’t rely only on its internal knowledge to produce answers.

This article explores the pros and cons of using fine-tuning and RAG to curb the limitations of LLMs. We also consider the implications of each approach for organizations that already use [knowledge graphs](https://neo4j.com/books/developers-guide-how-to-build-knowledge-graph/) to organize and manage their data.

## The Limitations of LLMs

https://dist.neo4j.com/wp-content/uploads/20230608064948/1gMyohWeGauh6BZvbqsXAgw-e1726069380895.pngMidjourney’s idea of a knowledge graph chatbot.

After the launch of ChatGPT in November 2022, people began considering integrating LLMs into their applications to generate creative content and solve typical natural language processing tasks like text summarization and translation.

Using LLMs out of the box for business use cases can cause serious issues, though. Let’s explore the most critical concerns.

### Knowledge Cutoff

Knowledge cutoff refers to the fact that LLMs are unaware of any events that happened after their training. For example, if you ask ChatGPT about an event that occurred in 2024, you’ll get a response like this:

https://dist.neo4j.com/wp-content/uploads/20250219170021/image-78-1024x403.pngChatGPT’s knowledge cutoff date. Image by author.

The same problem will occur if you ask an LLM about any event not present in its training dataset. While the knowledge cutoff date is relevant for any publicly available information, the LLM doesn’t have knowledge about private or confidential information that might be available even before the knowledge cutoff date.

For example, many companies have confidential information they don’t share publicly, but they might be interested in having a custom LLM that could answer questions about that information. On the other hand, publicly available information that an LLM is aware of could already be outdated.

### Hallucinations

We cannot blindly believe everything that LLMs produce.

LLMs are trained to produce realistic-sounding output, but it might not always be accurate. Some invalid information is more challenging to spot than others. Especially for missing data, the LLMs are likely to make up an answer that sounds convincing (but is nonetheless wrong) instead of admitting that it lacks the base facts in its training.

For example, research or court citations might be easier to verify. In 2023, a lawyer got in trouble for [blindly believing the court citations ChatGPT produced](https://edition.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers/index.html). While people have become more wary since then about the information that public LLMs like ChatGPT and Gemini generate, it’s still risky.

LLMs will also consistently produce assertive yet false information about any sort of identification number, including Wikidata IDs:

https://dist.neo4j.com/wp-content/uploads/20250219170037/image-79-1024x711.pngChatGPT’s hallucinations. Image by author.

In the screenshot above, ChatGPT gave an assertive response, but it’s inaccurate. The Wikidata ID that ChatGPT gave points to a Russian singer.

### Other Problems

LLMs also have other problems:

- **Bias** – LLMs can inherit biases from their training data, leading to discriminatory or unfair outputs.
- **Prompt injection** – Malicious users can craft prompts that manipulate the LLM to generate harmful or misleading content.
- **Common sense reasoning** – LLMs often struggle with tasks requiring common-sense reasoning or an understanding of the situation’s context.
- **Explainability** – It can be difficult to understand the reasoning or sources behind an LLM’s output, which reduces trust in its outputs and complicates debugging efforts.

We won’t explore these in detail for brevity’s sake. Instead, let’s explore your first option for overcoming these challenges: supervised fine-tuning.

## Supervised Fine-Tuning of an LLM

Fine-tuning is a targeted training approach for LLMs. It refers to the supervised training phase during which you provide additional question-answer pairs to optimize an LLM’s performance. By repeatedly processing these data samples, the LLM refines its understanding and improves its ability to answer questions or generate text in that specific area.

Fine-tuning lets you use the LLM’s existing capabilities while tailoring it to address your unique needs. If you combine fine-tuning with domain-specific pre-training, you can have a [domain-specific LLM](https://arxiv.org/abs/2401.02981) to carry out specialized operations in a field such as finance, with increased accuracy.

> **Note:** Two prominent use cases for fine-tuning an LLM are updating and expanding its internal knowledge and fine-tuning a model for a specific task (like text summarization or translating natural language to database queries). You could also prepare a model for creative purposes, such as personalized artistic content generation and analysis of user preferences and behavior patterns for content filtering and recommendation. This article discusses the first use case of using fine-tuning techniques to update and expand the internal knowledge of an LLM.

### Where Does Fine-Tuning Fit In?

> Explaining in detail how LLMs are trained is beyond the scope of this blog post. If you’re curious, you can watch this [video by Andrej Karpathy](https://www.youtube.com/watch?v=bZQun8Y4L2A) to catch up on LLMs and learn about the different phases of LLM training.

The first step of creating an LLM involves pre-training a model to develop a base LLM. A base LLM is usually pre-trained using a gigantic corpus of text, frequently in the billions or even trillions of tokens. The cost of training can be upwards of hundreds of thousands or even millions of dollars — something most organizations want to avoid.

Recently, [a paper by Microsoft](https://arxiv.org/pdf/2406.02290) (published in June 2024) showed that techniques like gradient checkpointing and low-rank adaptation can reduce memory bottlenecks during the fine-tuning process. This would make fine-tuning more time- and cost-efficient, but so far, we don’t have any real-world examples that have proved cost reduction.

https://www.flaticon.com/.](https://dist.neo4j.com/wp-content/uploads/20230608064931/1LTfNOqZQB_M42KyvttjSyw.png)Supervised fine-tuning flow. Image by Tomaž Bratanič. Icons from [Flaticon](https://www.flaticon.com/).

Therefore, the most common first step is to choose a pre-trained base LLM for your use case. You need to consider several things when making this choice:

- The **number of parameters** in an LLM determines its capacity to learn and represent complex patterns in the data. Larger models require more computational power and memory for training and inference. They can also have longer training times. Fine-tuning such models can be resource-intensive, necessitating powerful hardware such as GPUs and TPUs.
- The **license** of the base LLM dictates how you can use the fine-tuned model. Some licenses may have restrictions on commercial use, distribution, or modification. Open source models offer more flexibility for fine-tuning and customization, while proprietary models might provide better performance or specific features but with more restrictive licenses. You must comply with the license terms to avoid legal issues.
- **Bias** in the base model can be amplified during fine-tuning if not properly addressed, which can lead to unfair or discriminatory behavior by the fine-tuned model. Identifying and mitigating bias needs additional data preprocessing and evaluation steps, including employing data balancing techniques, bias detection tools, and fairness-aware training algorithms. You want to choose a base LLM that has the least known bias in its initial training dataset.
- **Toxicity** refers to the fact that models can generate toxic or harmful content if they’re not properly controlled. To minimize toxicity, maintain a positive user experience, and prevent harm, you want to filter training data and implement safety layers and continuous monitoring. If possible, also choose a base LLM that has the least known toxicity and includes mechanisms to detect and mitigate toxicity during fine-tuning.

After selecting the base LLM, the next step is fine-tuning it.

### Preparing the Training Dataset

The first step of fine-tuning is to prepare the dataset you’ll use to fine-tune the base LLM.

Compared to pre-training, fine-tuning is relatively cheap in terms of computation cost due to techniques like [LoRA](https://huggingface.co/blog/lora) and [QLoRA](https://arxiv.org/abs/2305.14314). However, constructing the training dataset is more complex than the training itself and can get expensive.

Some organizations that can’t afford a dedicated team of annotators go really meta and use an LLM to construct a training dataset for fine-tuning their LLMs. For example, Stanford’s Alpaca training dataset was [created using OpenAI’s LLMs](https://crfm.stanford.edu/2023/03/13/alpaca.html). The cost of producing 52,000 training instructions was about USD $500, which is relatively cheap. The Vicuna model was fine-tuned [using the ChatGPT conversations users posted on ShareGPT](https://lmsys.org/blog/2023-03-30-vicuna/). Training this model cost even less at USD $140.

H2O also developed a project called [WizardLM](https://github.com/h2oai/h2o-wizardlm) that turns documents into question-answer pairs for fine-tuning LLMs.

However, we have yet to see any implementations around using knowledge graphs to prepare good question-answer pairs that can help fine-tune an LLM to expand its internal knowledge. This is concerning for organizations that rely on knowledge graphs to store their company-specific data. Creating a training dataset from their data store will most likely be problematic for them. A possible way to do this is the community report summarization step in the [Graph RAG proposal by Microsoft](https://arxiv.org/pdf/2404.16130), but that idea hasn’t been tested yet.

### Limitations of Fine-Tuning

A key issue with LLMs is that there are many unknowns currently. For example, can you provide two different answers to the same question, and would the LLM then somehow combine them in its internal knowledge store?

If your organization wants to use data from knowledge graphs to train an LLM, consider that some information in a knowledge graph becomes relevant only when you examine its relationships. Do you have to predefine relevant queries to consolidate these relationships into the training dataset, or is there a more generic way to do it? Or can you generate relevant pairs using the node-relationship-node patterns representing subject-predicate-object expressions?

Those concerns aside, let’s imagine you somehow managed to produce a training dataset containing question-answer pairs based on the information stored in your knowledge graph. As a result, the LLM now includes updated knowledge. Still, fine-tuning the model didn’t solve the knowledge cutoff problem; it only pushed the knowledge cutoff to a later date.

Furthermore, while fine-tuning approaches can decrease hallucinations, they can’t eliminate them. On their own, LLMs [can’t cite their sources when providing answers](https://www.reddit.com/r/ArtificialInteligence/comments/1co90z4/comment/l3ci9cd/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button). Therefore, you have no idea if the answer came from pre-training data, the fine-tuning dataset, or if the LLM made it up. If you use an LLM to create the fine-tuning dataset, a falsehood source is also always possible.

A fine-tuned model also can’t automatically provide different responses depending on who asks the questions. Likewise, there’s no concept of access restrictions, meaning that anybody interacting with the LLM has access to all its information.

### When to Use Fine-Tuning

Keeping the limitations of fine-tuning in mind, we recommend updating the internal knowledge of an LLM through fine-tuning techniques only for data that changes or updates slowly.

For example, you could use a fine-tuned model to provide information about historic tourist attractions as long as it doesn’t require any specific, time-dependent information. You would run into trouble the second you wanted to include special time-dependent (real-time) or personalized promotions in the responses.

Similarly, fine-tuned models are not ideal for analytical workflows where you might ask how many new customers the company gained over the past week.

Fine-tuning is most useful when your app requires the model to excel in highly specialized tasks or domains. By training the model on specific datasets, you can customize responses to better align with the nuances and details of the particular area of interest. This process enhances the model’s intrinsic understanding and generation capabilities, which makes it better at handling specialized queries and producing more accurate and contextually relevant outputs.

## Retrieval-Augmented Generation

The idea behind retrieval-augmented LLM applications is to avoid relying only on internal LLM knowledge to generate answers.

RAG uses LLMs to solve tasks like constructing database queries from natural language and constructing answers based on externally provided information or by using plugins or agents for retrieval. Instead of using the internal knowledge of an LLM, RAG allows you to use the LLM as a natural language interface to your company’s or private information.

### How Retrieval-Augmented Generation Works

https://www.flaticon.com/.](https://dist.neo4j.com/wp-content/uploads/20230608064925/1zydD2GKzjpEyvL-d_cP0vA.png)Retrieval-augmented generation. Image by Tomaž Bratanič. Icons from [Flaticon](https://www.flaticon.com/).

RAG uses a [smart search](https://lucidworks.com/post/what-is-smart-search/) tool to provide your LLM with an appropriately phrased question and a set of relevant documents from your data store. It then generates an answer based on information from your data source. This means you don’t rely on internal knowledge of the LLM to produce answers. Instead, the LLM is used only to extract relevant information from documents you passed in and summarize it.

The introduction of agents and tool-calling support has acted as a catalyst for the rise of RAG.

Agents act as intermediaries that connect LLMs to external knowledge sources like databases and APIs. As a result, LLMs can tap into a vast pool of real-time data, overcoming the knowledge cutoff and enabling them to access the latest information. Agents can integrate fact-checking services and verification tools into the LLM workflow, which enhances the trustworthiness of the LLM’s outputs by mitigating the risk of factual errors.

Native tool-calling functionality takes this a step further. LLMs can directly call upon external tools for specific tasks, such as complex calculations or data analysis, which allows them to handle a wider range of problems and expand their overall capabilities. For example, the [ChatGPT tools](https://openai.com/index/gpt-4o-and-more-tools-to-chatgpt-free/#:~:text=Bringing%20more%20intelligence%20and%20advanced%20tools%20for%20free) for getting web responses and uploading files for assistance in writing or analyzing can be thought of as a RAG approach to LLM applications. Because the ChatGPT interface has access to the internet, the LLM can search to access up-to-date information and use it to construct the final answer:

https://dist.neo4j.com/wp-content/uploads/20250219170151/image-80-1024x697.pngChatGPT with browsing plugin. Image by author.

In this example, ChatGPT was able to answer who won the NBA MVP in 2024. But, remember the cutoff knowledge date for ChatGPT is January 2022, so it couldn’t know who won the 2024 NBA MVP from its internal knowledge. Instead, it accessed external information from the internet with its [Browse with Bing feature](https://help.openai.com/en/articles/8077698-how-do-i-use-chatgpt-browse-with-bing-to-search-the-web), which allowed it to answer the question with up-to-date information. Such features present an integrated augmentation mechanism inside the OpenAI platform.

### Implementing Retrieval-Augmented Generation

There are multiple ways in which you can implement RAG in your systems.

[LangChain](https://python.langchain.com/v0.2/docs/introduction/), a library for developing and deploying applications using LLMs, provides tools for integrating LLMs with RAG techniques. You can use the LangChain library to [allow LLMs to access real-time information](https://towardsdatascience.com/getting-started-with-langchain-a-beginners-guide-to-building-llm-powered-applications-95fc8898732c) from various sources like Google Search, vector databases, or [knowledge graphs](https://python.langchain.com/v0.1/docs/use_cases/graph/).

For example, LangChain has added a [Cypher Search chain](https://towardsdatascience.com/langchain-has-added-cypher-search-cb9d821120d5) that converts natural language questions into a \[Cypher\]( [https://neo4j.com/docs/cypher-manual/current/introduction/](https://neo4j.com/docs/cypher-manual/current/introduction/)\] statement, uses it to retrieve information from the graph database, such as those of Neo4j, and constructs a final answer based on the information provided. With the Cypher Search chain, an LLM is not only used to construct a final answer but also to translate a natural language question into a Cypher query:

https://dist.neo4j.com/wp-content/uploads/20230608064914/1RsB4TVvro3oj7KKGpu_ohA.pngCypher Search in LangChain. Image by Tomaž Bratanič.

Another popular library for retrieval-augmented LLM workflows is [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html), formerly known as GPT Index. LlamaIndex is a comprehensive data framework that enhances the performance of LLMs by [enabling them to use private or custom data](https://medium.com/llamaindex-blog/llamaindex-on-twiml-ai-a-distilled-summary-using-llamaindex-de2a88551595).

LlamaIndex offers data connectors that facilitate ingesting various data sources and formats — including everything from APIs, PDFs, and documents to SQL or graph data — to integrate existing data into the LLM. It also provides efficient mechanisms to structure the ingested data using indexes and graphs, ensuring the data is suitably arranged for use with LLMs. Its advanced retrieval and query interface lets users input an LLM prompt and receive back a context-retrieved, knowledge-augmented output.

LlamaIndex supports creating and connecting to [property graph indexes](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/) to build a rich knowledge graph from unstructured data and then query it in flexible ways to uncover insights and relationships within your information. You can also [skip creating the knowledge graph](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/#:~:text=You%20can%20also%20skip%20creation%2C%20and%20connect%20to%20an%20existing%20knowledge%20graph) if you already have one in a graph database tool like Neo4j and use it directly in your LlamaIndex projects.

Because of [Neo4j’s native property graph model](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/#:~:text=Neo4j%20uses%20a%20property%20graph%20database%20model), knowledge graphs built on Neo4j graph databases can combine transactional data, organizational data, and vector embeddings in a single database, simplifying the overall application design. [Pairing it with LlamaIndex’s property graph index](https://neo4j.com/blog/developer/property-graph-index-llamaindex/) lets you create custom solutions to query specific types of information from within the graph.

### Advantages and Disadvantages of Retrieval-Augmented Generation

The retrieval-augmented approach has some clear advantages over fine-tuning:

- The answer can cite its sources of information, which allows you to validate the information and potentially change or update the underlying information based on requirements.
- Hallucinations are less likely to occur as the LLM no longer relies on its internal knowledge to answer the question. Instead, it uses information provided in relevant documents.
- It’s easier to change, update, and maintain the underlying information the LLM uses because you transform the problem from LLM maintenance to one involving database maintenance, querying, and context construction.
- Answers can be personalized based on the user’s context or access permission.

However, keep the limitations of RAG in mind:

- The answers are only as good as the smart search tool. Your smart search tool must be able to provide the LLM with the correctly phrased question along with enough relevant documents from your data store.
- The application needs access to your specific knowledge base, whether a database or other data stores.
- Completely disregarding the internal knowledge of the language model limits the number of questions that can be answered.
- Sometimes LLMs fail to follow instructions, so the context might be ignored, or hallucinations could still occur if no relevant answer data is found in the context.

## Contrasting Fine-Tuning and RAG for LLMs

The key differences between the two approaches are depicted in the table below:

| Comparison Point | Fine-tuning | RAG |
| --- | --- | --- |
| **Data requirements** | Large amounts of task-specific labeled data | Pre-trained LLM, separate information retrieval system, potentially some labeled data for generation |
| **Knowledge** | Adapts internal LLM knowledge for specific task | Integrates external knowledge sources, allowing access to up-to-date information |
| **Accuracy and reliability** | More accurate for tasks in its domain, prone to hallucinations for out-of-domain | Less prone to hallucinations; accuracy depends on retrieved data and LLM processing |
| **Flexibility and adaptability** | Requires retraining for different tasks/domains | Easier to adapt to new domains or update knowledge by modifying retrieval system data sources |
| **Transparency and explainability** | Difficult to explain reasoning behind answer | Allows citation of sources for better transparency |
| **Development and deployment** | Requires expertise in data preparation and fine-tuning techniques | Requires building or integrating a retrieval system alongside the LLM |

Fine-tuning is well-suited for tasks with a clear and well-defined domain and access to large amounts of labeled data, such as sentiment analysis and database query generation for a specific product. It can update the base LLM’s context with the new data and entirely remove any dependence on external data sources.

However, RAG is more accurate (see [this study](https://arxiv.org/abs/2403.01432) and [this one](https://arxiv.org/abs/2403.09727) for a more in-depth look), which means it’s better for tasks that require access to up-to-date information or integrations with existing knowledge bases such as question-answering systems and customer service chatbots.

RAG with graph databases (like [Neo4j](https://neo4j.com/)) offers several advantages. Access to a richer knowledge base with interconnected entities leads to more comprehensive answers, better adaptability to new domains and evolving knowledge, and insights into relationships and data points used by RAG to generate answers. It also offers a level of explainability that fine-tuning lacks, as well as access to the latest information, unlike fine-tuned LLMs that rely on static training data.

Fine-tuning can be used to supplement RAG, particularly when highly specialized knowledge in a well-defined domain is required. However, for most applications, RAG offers a more cost-effective and time-efficient approach. It allows you to directly use a pre-trained LLM with a knowledge store instead of preparing a training dataset and going through the supervised training phase. RAG also doesn’t require the same level of technical expertise as fine-tuning.

The reality is that most companies don’t necessarily need to create custom LLMs for a niche skill. Combining a pre-trained LLM with domain-specific data through RAG is sufficient for companies to use their own data within a powerful language model, making it an attractive option.

Many teams are working on creating ways to effectively implement RAG with graph databases. The term _GraphRAG_ is catching on, with teams from institutions like [Microsoft](https://arxiv.org/abs/2404.16130) and [Emory University, Atlanta](https://arxiv.org/pdf/2405.16506) putting forth their ideas on how to best use graphs with RAG to improve the results of RAG systems. To learn more about this combination, [Neo4j’s GraphRAG Manifesto](https://neo4j.com/blog/genai/graphrag-manifesto/) breaks it down in detail.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="hisem-rag-a-hierarchical-semantic-driven-retrieval-augmented.md">
<details>
<summary>HiSem-RAG: A Hierarchical Semantic-Driven Retrieval-Augmented Generation Method</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.mdpi.com/2076-3417/16/2/903>

Original Submission Date Received: .

Open AccessArticle

# HiSem-RAG: A Hierarchical Semantic-Driven Retrieval-Augmented Generation Method

by


Dongju Yang

https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.pngDongju Yang

[SciProfiles](https://sciprofiles.com/profile/4937532?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Dongju%20Yang) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Dongju+Yang%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Dongju+Yang)

[https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1776684316](https://orcid.org/0000-0003-3089-9611) and

Junming Wang

https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.pngJunming Wang

[SciProfiles](https://sciprofiles.com/profile/4934806?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Junming%20Wang) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Junming+Wang%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Junming%20Wang)

\* [https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1776684316](https://orcid.org/0009-0007-8303-9304)

Large-Scale Stream Data Integration and Analysis Technology Beijing Key Laboratory, School of Artificial Intelligence and Computer Science, North China University of Technology, No. 5 Jinyuanzhuang Road, Beijing 100144, China

\*

Author to whom correspondence should be addressed.

_Appl. Sci._ **2026**, _16_(2), 903; [https://doi.org/10.3390/app16020903](https://doi.com/10.3390/app16020903)

Submission received: 1 December 2025
/
Revised: 1 January 2026
/
Accepted: 2 January 2026
/
Published: 15 January 2026

(This article belongs to the Topic [Challenges and Opportunities of Integrating Service Science with Data Science and Artificial Intelligence](https://www.mdpi.com/topics/TC1EK01L61))

https://pub.mdpi-res.com/applsci/applsci-16-00903/article_deploy/html/images/applsci-16-00903-g001.png?1768553891 "                         <strong>Figure 1</strong><br/>                                                     <p>A motivating example illustrating the limitations of traditional RAG versus the proposed HiSem-RAG.</p>                                                 "https://pub.mdpi-res.com/applsci/applsci-16-00903/article_deploy/html/images/applsci-16-00903-g002.png?1768553893 "                         <strong>Figure 2</strong><br/>                                                     <p>The framework of the HiSem-RAG method.</p>                                                 "https://pub.mdpi-res.com/applsci/applsci-16-00903/article_deploy/html/images/applsci-16-00903-g003.png?1768553895 "                         <strong>Figure 3</strong><br/>                                                     <p>Experimental results on accuracy and resource consumption.</p>                                                 "

## Abstract

Traditional retrieval-augmented generation (RAG) methods struggle with hierarchical documents, often causing semantic fragmentation, structural loss, and inefficient retrieval due to fixed strategies. To address these challenges, this paper proposes HiSem-RAG, a hierarchical semantic-driven RAG method. It comprises three key modules: (1) hierarchical semantic indexing, which preserves boundaries and relationships between sections and paragraphs to reconstruct document context; (2) a bidirectional semantic enhancement mechanism that incorporates titles and summaries to facilitate two-way information flow; and (3) a distribution-aware adaptive threshold strategy that dynamically adjusts retrieval scope based on similarity distributions, balancing accuracy with computational efficiency. On the domain-specific EleQA dataset, HiSem-RAG achieves 82.00% accuracy, outperforming HyDE and RAPTOR by 5.04% and 3.98%, respectively, with reduced computational costs. On the LongQA dataset, it attains a ROUGE-L score of 0.599 and a BERT\_F1 score of 0.839. Ablation studies confirm the complementarity of these modules, particularly in long-document scenarios.

Keywords:

[hierarchical document representation](https://www.mdpi.com/search?q=hierarchical+document+representation); [semantic enhancement](https://www.mdpi.com/search?q=semantic+enhancement); [adaptive threshold retrieval](https://www.mdpi.com/search?q=adaptive+threshold+retrieval); [long-form question answering](https://www.mdpi.com/search?q=long-form+question+answering); [similarity distribution modeling](https://www.mdpi.com/search?q=similarity+distribution+modeling); [large language model](https://www.mdpi.com/search?q=large+language+model)

## 1\. Introduction

Retrieval-Augmented Generation (RAG) has emerged to address Large Language Model (LLM) limitations regarding knowledge timeliness, domain specificity, and generation stability. By combining external retrieval with generative capabilities, RAG allows models to access dynamic, domain-specific information during inference, overcoming the boundaries of closed parameter learning.

Since its proposal by Lewis et al. \[ [1](https://www.mdpi.com/2076-3417/16/2/903#B1-applsci-16-00903)\], RAG has been widely applied in question answering, summarization, and dialogue systems. Early methods, such as Dense Passage Retrieval (DPR) \[ [2](https://www.mdpi.com/2076-3417/16/2/903#B2-applsci-16-00903)\], relied on dual-encoder architectures for vector-based semantic matching. Subsequently, RAG systems evolved in two key areas: semantic indexing (advancing from fixed-length chunks to structure-aware forms) and retrieval mechanisms (expanding to hybrid \[ [3](https://www.mdpi.com/2076-3417/16/2/903#B3-applsci-16-00903)\] and adaptive approaches). For instance, Self-RAG \[ [4](https://www.mdpi.com/2076-3417/16/2/903#B4-applsci-16-00903)\] employs self-reflection to dynamically invoke external knowledge. However, reliance on external knowledge presents challenges. Mansurova et al. \[ [5](https://www.mdpi.com/2076-3417/16/2/903#B5-applsci-16-00903)\] explored LLM reliance on external vector indices (QA-RAG), highlighting persistent issues with noise robustness and external truth integration.

Despite progress, RAG faces bottlenecks when processing complex, long, or information-dense documents:

- Semantic Structure Loss: Most methods mechanically split documents into fixed-length segments, ignoring natural hierarchies like headings and sections. This disrupts semantic boundaries, resulting in fragmented retrieval and weak context, making it difficult to capture key information in long documents.

- Rigid Retrieval Quantity: Mainstream approaches typically use a fixed top-k strategy, ignoring the actual knowledge distribution. A small k risks omitting critical information, while a large k introduces noise and increases computational overhead, leading to generation interference.


To improve accuracy and efficiency, we propose HiSem-RAG, a Hierarchical Semantic-Driven Retrieval-Augmented Generation method. This approach leverages document hierarchy and semantic distribution through three designs:

- Hierarchical Semantic Indexing: Constructs multi-granularity indices based on natural document structures (sections, paragraphs), preserving original boundaries for hierarchical retrieval.

- Bidirectional Semantic Enhancement: Introduces titles and summaries to facilitate information flow across layers, strengthening semantic connections.

- Distribution-Aware Adaptive Thresholding: Dynamically sets retrieval thresholds based on similarity distributions, replacing the fixed top-k approach to balance completeness and efficiency.


Comprehensive evaluations on the EleQA and LongQA datasets demonstrate that HiSem-RAG outperforms baselines in both accuracy and resource efficiency. Ablation studies further confirm the synergistic effects of the core modules.

Further ablation studies confirm the synergistic effects among the three core modules, making HiSem-RAG particularly suitable for question-answering scenarios involving complex hierarchical structures and information-dense content.

To systematically address the challenges of structural loss and rigid retrieval strategies, this study focuses on the following three research questions (RQs):

- RQ1: How can we construct an indexing mechanism that preserves the natural hierarchical boundaries of documents to prevent context detachment and structural ambiguity?

- RQ2: How can we enable bidirectional information flow between document layers to enhance the semantic completeness of retrieved fragments?

- RQ3: How can we design a dynamic retrieval strategy that automatically adjusts the retrieval scope based on information density, balancing coverage and efficiency?


## 2\. Motivating Example and Design Rationale

To illustrate the limitations of current approaches, we present a real-world example from the LongQA dataset in [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001). The document structure (Panel A) features identical subtitles, “2. Process Standards,” under two different chapters: “Main Transformer” and “Neutral Point System.”

- Structural Ambiguity and Context Loss: Traditional RAG methods mechanically split documents into flat chunks (Panel B). This severs the connection between the subtitle and its parent chapter. Consequently, when a user asks about “Main Transformer standards,” the retriever, lacking structural awareness, is easily distracted by the similar content in the “Neutral Point” section (Chunk 7), leading to hallucinations.

- Fragmentation vs. Adaptive Retrieval: Furthermore, the correct answer spans 23 detailed items (over 3000 tokens), which are inevitably split into multiple fragments (Chunks 3–8). A rigid top-k retrieval strategy (e.g., k=3) would fetch only the initial fragments, missing the critical details in the tail.


Our Solution (HiSem-RAG): As shown in Panel C, HiSem-RAG preserves the hierarchical tree to address these issues:

- Bidirectional Enhancement: We explicitly embed the title path (Top-Down) to disambiguate the context. Simultaneously, detailed rules are compressed into a summary at the parent node (Bottom-Up Aggregation, shown as the blue “Summary” box).

- Adaptive Threshold: Instead of a fixed top-k, our distribution-aware threshold detects the semantic coherence of the parent node and automatically retrieves the entire cluster of relevant chunks (Standards 1–23) as a complete context unit (indicated by the dashed “Adaptive Scope” box).


## 3\. Related Work

### 3.1. Index Structures in RAG Systems

The index structure is a core component of RAG systems, directly determining the organization and retrieval mode of the knowledge base. With the development of RAG technology, index structures have gradually evolved from simple flat structures to more complex forms with hierarchical and semantic associations.

#### 3.1.1. Flat Indexing Methods

Early RAG systems primarily adopted flat indexing structures, representing documents as independent sets of vectors. This approach is easy to implement but struggles to capture hierarchical relationships and semantic coherence within document content. A typical example is DPR, which uses a dual-encoder to generate vector representations for queries and documents, enabling retrieval through similarity computation. Compared with traditional keyword-matching methods, DPR better captures semantic relevance but ignores the internal structure of documents.

#### 3.1.2. Hierarchical Index Structures

To overcome the limitations of flat indexing, researchers have proposed various hierarchical indexing methods. RAPTOR \[ [6](https://www.mdpi.com/2076-3417/16/2/903#B6-applsci-16-00903)\] constructs document trees through recursive abstraction, clustering and summarizing sentences layer by layer from leaf nodes to the root. This structure improves retrieval flexibility and precision, supporting multi-level retrieval with adaptive granularity based on query complexity. While RAPTOR’s bottom-up approach may face challenges in tasks requiring complete context, its concept has inspired subsequent optimizations. Recent domain-specific applications, such as the paradigm for construction management proposed by Wu et al. \[ [7](https://www.mdpi.com/2076-3417/16/2/903#B7-applsci-16-00903)\], further demonstrate the importance of hierarchical structures in RAG systems. This approach parses project documents into hierarchical structures, combining document-level features with original content to enhance granularity alignment and retrieval effectiveness. These developments have significantly influenced the hierarchical indexing approach proposed in this paper.

#### 3.1.3. Graph-Based Indexing Methods

In recent years, graph-based index structures have shown significant potential. GraphRAG \[ [8](https://www.mdpi.com/2076-3417/16/2/903#B8-applsci-16-00903)\] constructs knowledge graphs by extracting entities and relationships using large language models, addressing complex problems requiring global understanding. KA-RAG \[ [9](https://www.mdpi.com/2076-3417/16/2/903#B9-applsci-16-00903)\] integrates structured knowledge graphs with agentic workflows, employing a dual-retrieval strategy that combines symbolic graph reasoning with dense semantic retrieval to enhance interpretability and precision in educational scenarios. Several researchers \[ [10](https://www.mdpi.com/2076-3417/16/2/903#B10-applsci-16-00903), [11](https://www.mdpi.com/2076-3417/16/2/903#B11-applsci-16-00903), [12](https://www.mdpi.com/2076-3417/16/2/903#B12-applsci-16-00903)\] have extended these approaches to specialized domains, retrieving relevant triples from knowledge graphs and converting them into natural language prompts for applications ranging from general knowledge enhancement to forensic injury assessment and failure mode analysis. Additionally, Choi et al. \[ [13](https://www.mdpi.com/2076-3417/16/2/903#B13-applsci-16-00903)\] proposed integrating Knowledge Graph encoders with pre-trained models (like ALBERT) to utilize explicit external information, demonstrating that schema graph expansion effectively improves performance in commonsense question answering. Graph-based indexes naturally represent complex inter-document associations and provide structural support for advanced reasoning.

In summary, RAG indexing has evolved from flat to hierarchical and graph-based forms, increasingly emphasizing semantic association and structural preservation. While flat structures are simple, hierarchical approaches better preserve document organization, and graph structures excel at representing complex associations. However, simultaneously maintaining structural integrity and supporting efficient retrieval remains challenging. The proposed HiSem-RAG addresses this by constructing a hierarchical index that retains the original document hierarchy while facilitating precise, adaptive retrieval.

### 3.2. Optimization of Text Chunking Strategies

Text chunking is a foundational step in index construction, directly affecting the quality of the index and retrieval performance. Based on their core principles, chunking strategies can be classified as follows:

#### 3.2.1. Length-Based Chunking Methods

The most basic and widely used strategy is length-based chunking. Fixed-size chunking mechanically splits documents according to a preset number of tokens or characters. While simple to implement, this method often disrupts semantic integrity. TEJA R., through the LLAMAi framework \[ [14](https://www.mdpi.com/2076-3417/16/2/903#B14-applsci-16-00903)\], systematically studied the impact of chunk size on RAG performance, showing that an appropriate chunk size can balance efficiency and semantic completeness. As large language models’ capabilities for long-text processing have improved, research by Xu et al. \[ [15](https://www.mdpi.com/2076-3417/16/2/903#B15-applsci-16-00903)\] demonstrated that expanding the context window from 4K to 32K and combining with retrieval augmentation can significantly enhance long-text task performance.

#### 3.2.2. Semantics-Based Chunking Methods

Semantics-based chunking methods aim to preserve the semantic integrity of text. By identifying semantic boundaries for segmentation, they retain key information and logical structure. The Small2Big approach by Yang et al. \[ [16](https://www.mdpi.com/2076-3417/16/2/903#B16-applsci-16-00903)\] uses sentences as basic retrieval units and supplies context sentences to the language model, improving retrieval efficiency while maintaining semantic coherence. More recently, Krassovitskiy et al. \[ [17](https://www.mdpi.com/2076-3417/16/2/903#B17-applsci-16-00903)\] investigated the use of LLM embeddings to capture semantic coherence and topic closure. Their work demonstrates that integrating embeddings with classical clustering and graph-based methods—including a proposed magnetic clustering algorithm—significantly improves segmentation quality, providing valuable insights for optimizing RAG systems. Such methods focus on semantic cohesion within the text and are suitable for unstructured but semantically rich content.

#### 3.2.3. Structure-Aware Chunking Methods

With increasing needs for processing domain-specific documents, structure-aware chunking methods have gained attention. Meta-Chunking \[ [18](https://www.mdpi.com/2076-3417/16/2/903#B18-applsci-16-00903)\] employs dynamic chunking to balance fine and coarse granularity, using metadata to enhance contextual information within chunks. Wang et al. \[ [19](https://www.mdpi.com/2076-3417/16/2/903#B19-applsci-16-00903)\] examined the role of document structure in paragraph retrieval, showing that considering document structure helps systems understand paragraph significance within the global context. These methods fully leverage structural information—such as titles and sections—and are highly relevant to the section-title-based chunking strategy proposed in this paper. Zheng et al. \[ [20](https://www.mdpi.com/2076-3417/16/2/903#B20-applsci-16-00903)\] demonstrated how specialized text mining approaches can enhance domain-specific chunking strategies for chemistry literature. Bi et al. \[ [21](https://www.mdpi.com/2076-3417/16/2/903#B21-applsci-16-00903)\] proposed a sliding window strategy that effectively addresses limitations of traditional fixed-size context windows, dynamically adjusting window size and step length to preserve contextual information.

The evolution of text chunking strategies reflects the deepening understanding of semantics and structure in RAG systems. From initial fixed-length chunking, to semantic-aware chunking, and then to structure-aware chunking, each step addresses the limitations of the previous stage. Length-based methods are simple but cannot ensure semantic integrity; semantic chunking values content cohesion but has limited structural awareness; structure-aware chunking leverages inherent document organization but is less effective for unstructured text. Designing chunking strategies that retain the natural hierarchy of documents while maintaining paragraph-level semantic integrity is key to enhancing RAG systems’ ability to process complex documents.

### 3.3. Optimization of Retrieval Mechanisms and Strategies

Retrieval mechanisms directly determine the quality of information provided to the generation model. Retrieval optimization primarily focuses on query processing, retrieval strategies, and result optimization.

#### 3.3.1. Query Optimization and Decomposition

Query optimization studies how to improve user input to enhance retrieval quality. Various approaches have emerged to address this challenge. The HyDE method \[ [22](https://www.mdpi.com/2076-3417/16/2/903#B22-applsci-16-00903)\] generates hypothetical documents for retrieval, while query rewriting strategies like BEQUE \[ [23](https://www.mdpi.com/2076-3417/16/2/903#B23-applsci-16-00903)\] focus on enhancing sparse queries in specialized domains. Several researchers \[ [24](https://www.mdpi.com/2076-3417/16/2/903#B24-applsci-16-00903), [25](https://www.mdpi.com/2076-3417/16/2/903#B25-applsci-16-00903), [26](https://www.mdpi.com/2076-3417/16/2/903#B26-applsci-16-00903)\] have developed systems that identify user intent through specialized models and route queries to appropriate retrieval methods, significantly improving performance in contexts ranging from multi-agent QA systems to geographic question answering and military applications. For complex queries, advanced frameworks \[ [27](https://www.mdpi.com/2076-3417/16/2/903#B27-applsci-16-00903), [28](https://www.mdpi.com/2076-3417/16/2/903#B28-applsci-16-00903), [29](https://www.mdpi.com/2076-3417/16/2/903#B29-applsci-16-00903)\] employ techniques such as query decomposition, unified reading comprehension, and chain-of-thought reasoning with recursive retrieval, allowing systems to break down complex questions and retrieve information iteratively as needed.

#### 3.3.2. Hybrid Retrieval and Dynamic Strategies

Hybrid retrieval combines methods such as BM25, dense vector retrieval, and sparse encoders, leveraging their complementary strengths for both keyword matching and semantic understanding. Multiple researchers \[ [30](https://www.mdpi.com/2076-3417/16/2/903#B30-applsci-16-00903), [31](https://www.mdpi.com/2076-3417/16/2/903#B31-applsci-16-00903), [32](https://www.mdpi.com/2076-3417/16/2/903#B32-applsci-16-00903)\] have validated hybrid retrieval approaches in professional domains including power knowledge bases, industrial knowledge management, and building engineering. These systems typically combine traditional search methods with embedding processing and specialized ranking mechanisms.

Domain-specific applications have further enhanced these approaches through specialized frameworks \[ [33](https://www.mdpi.com/2076-3417/16/2/903#B33-applsci-16-00903), [34](https://www.mdpi.com/2076-3417/16/2/903#B34-applsci-16-00903)\] that incorporate dynamic fine-grained methods and query rewriting techniques. Recent advances in adaptive retrieval strategies \[ [35](https://www.mdpi.com/2076-3417/16/2/903#B35-applsci-16-00903), [36](https://www.mdpi.com/2076-3417/16/2/903#B36-applsci-16-00903), [37](https://www.mdpi.com/2076-3417/16/2/903#B37-applsci-16-00903)\] have demonstrated promising results in specialized domains ranging from multi-objective math problems to dialogue state correction and equipment maintenance, often incorporating chain-of-thought reasoning or block-based retrieval. These approaches highlight the growing importance of domain-adaptive retrieval strategies that can dynamically determine when and how to retrieve external knowledge based on content quality and user needs.

#### 3.3.3. Retrieval Result Re-Ranking

Re-ranking plays a crucial role in improving retrieval accuracy. The Re2G framework by Glass et al. \[ [38](https://www.mdpi.com/2076-3417/16/2/903#B38-applsci-16-00903)\] merges results from multiple retrieval methods and applies neural re-ranking to optimize initial retrieval results, greatly enhancing final generation quality. The RankRAG method by Yu et al. \[ [39](https://www.mdpi.com/2076-3417/16/2/903#B39-applsci-16-00903)\] uses instruction tuning to enable a single LLM to perform both context ranking and answer generation, reducing reliance on separate ranking models. Ren et al. \[ [40](https://www.mdpi.com/2076-3417/16/2/903#B40-applsci-16-00903)\] introduced an adaptive two-stage retrieval augmented fine-tuning method for interpreting research policy, combining a two-stage retrieval mechanism with adaptive hard negative sampling. Xu et al. \[ [41](https://www.mdpi.com/2076-3417/16/2/903#B41-applsci-16-00903)\] proposed a two-stage consistency learning approach for retrieval information compression in RALMs to enhance performance while maintaining semantic alignment with the teacher model’s intent. These approaches focus on improving the quality and relevance of retrieval results, providing a stronger knowledge foundation for the generation stage.

Research on optimizing retrieval mechanisms demonstrates diverse technical approaches, from query improvement, to hybrid retrieval, and result re-ranking, all contributing to advances in RAG retrieval. Query optimization enhances systems’ ability to understand user intent through rewriting and decomposition; hybrid retrieval combines the advantages of different methods to improve overall retrieval; re-ranking further refines results to enhance the quality of information provided to the generation model. However, most existing methods still use fixed retrieval quantities, lacking dynamic adjustment capabilities and struggling to adapt to varying query information needs.

In summary, existing indexing methods struggle to simultaneously preserve document hierarchical structure and paragraph-level semantic integrity. They also lack effective mechanisms to represent and utilize hierarchical semantic information. Most methods use fixed top-k retrieval strategies, which cannot dynamically adjust to query characteristics and document distribution, resulting in insufficient knowledge coverage or redundant information. The HiSem-RAG method proposed in this paper constructs a hierarchical semantic index structure to preserve the natural hierarchy and semantic integrity of documents, and introduces a distribution-aware adaptive threshold mechanism to dynamically adjust the retrieval range, balancing the breadth and precision of knowledge coverage. By organically integrating chunking strategies, index structures, and retrieval mechanisms, HiSem-RAG provides a new solution for QA tasks involving structurally complex documents.

## 4\. Method

This section provides a detailed introduction to the core components and technical details of the HiSem-RAG method. As shown in [Figure 2](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f002), the central idea of HiSem-RAG is to construct an indexing system that preserves the hierarchical structure of documents while supporting intelligent retrieval. The entire method consists of two main parts: the construction of a hierarchical semantic index structure and a distribution-aware adaptive threshold retrieval mechanism based on this structure. This design fully leverages the inherent hierarchical characteristics of documents, providing efficient and precise retrieval services while maintaining semantic integrity.

### 4.1. Hierarchical Semantic Index Structure

#### 4.1.1. Hierarchical Document Parsing

Hierarchical document parsing is the foundational step of the HiSem-RAG method. Its main goal is to preserve the natural structure of documents, converting original linear text into a tree structure with hierarchical semantic relationships. This process mainly involves three stages: hierarchical title recognition to clarify structural boundaries; tree structure construction to organize documents into multi-level node representations; recursive splitting of lengthy segments at each level to control retrieval granularity and context length. Essentially, this is a hybrid approach that combines hierarchical modeling and semantic chunking, preserving semantic integrity while providing a structured foundation suitable for long-document processing, which supports subsequent efficient retrieval and generation.

Unlike traditional fixed-length chunking, we parse the multi-level title structure of documents to transform them into tree structures with hierarchical relationships. Formally, given a document d with hierarchical structure, we parse it into a tree T={n1,n2,…,nm}, where node ni represents a semantic unit in the document, such as a section, subsection, or other title-based content fragment. This structure reflects the document’s natural hierarchy. Each node can be a content carrier or a container for other nodes, and each node ni contains the following information:

- Node identifier id: the unique identifier of the node;

- Parent node identifier parent\_id: pointer to the parent node;

- Multi-level title path Tpath: concatenated path from the root to the current node;

- Index: the sequence number after recursive splitting;

- Core knowledge points K: the knowledge points in the node content;

- Content summary S: a concise summary of the node’s content;

- Original content: the raw content of the node (empty for non-leaf nodes);

- Children: a list of IDs for all child nodes (empty for leaf nodes).


To handle potentially overlong node content, we employ a recursive character-splitting strategy, using sentence and paragraph boundaries to ensure that segmented content fits model input constraints while preserving semantic integrity as much as possible. For any node ni with content longer than the preset threshold Lmax, we recursively split the content, treat the resulting segments as child nodes, and use the index to preserve the original order, ensuring semantic coherence.

#### 4.1.2. Bidirectional Semantic Enhancement

To further improve the expressiveness of semantic units, we design a bidirectional semantic enhancement mechanism. Based on the hierarchical structure, this mechanism models information flow from both directions: top-down to provide structural context and positional awareness; bottom-up to aggregate content summaries and enhance semantic abstraction.

(1)

Semantic Block Compression and Key Knowledge Extraction

First, we use a large language model to compress and reconstruct each node’s content, extracting knowledge points K and generating summaries S:

(K,S)=LLM(P,content),

(1)

where P is the prompt, with specific designs shown in [Table 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t001) (first row). This step effectively filters redundant content, retains important information, and improves the compactness and usability of semantic representations.

(2)

Top-Down Semantic Flow

To enhance the structural positioning ability of each node, we construct a multi-level title path Tpath, which reflects the node’s context within the document and aids in structural-aware retrieval. Suppose the path from the root to the current node consists of k nodes n1,n2,…,nk, where n1 is the root and nk the current node, and title(ni) is the title of node ni. The full title path Tpath is defined as

Tpath=title(n1),ifk=1,title(n1)→title(n2)→⋯→title(nk),ifk>1,

(2)

As illustrated in the motivating example ( [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001)), this mechanism explicitly embeds the path “Main Transformer” into the semantic representation of the subsection, effectively distinguishing it from the “Neutral Point” section despite their identical subtitles.

(3)

Bottom-Up Semantic Aggregation

To strengthen higher-level nodes’ grasp of their subordinate content, we aggregate the knowledge points and summaries of all child nodes:

(Kagg,Sagg)=LLM(Pagg,{(titlei,Ki,Si)}i∈Children),

(3)

where Kagg and Sagg are the aggregated knowledge points and summary for the parent node, and Pagg is a specially designed aggregation prompt (see [Table 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t001), second row). This structure enables higher-level nodes to summarize the core semantics of subordinate nodes, while lower-level nodes contain detailed information, forming a full semantic hierarchy from abstract to concrete. Referring back to [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001), this corresponds to the blue “Summary” box, which aggregates key details from the 23 child items, enabling the parent node to act as a semantic anchor for retrieval. The specific algorithm for hierarchical semantic index construction is shown as Algorithm 1.


|     |
| --- |
| **Algorithm 1** Build Hierarchical Index |
| **Require:**<br>Document collection D, maximum chunk size Lmax<br>**Ensure:**<br>Hierarchical semantic index I<br>  1:<br>I⇐∅                           ▹ Initialize index<br>  2:<br>**for all**d∈D**do**<br>  3:<br>N⇐ ParseStructure(d)               ▹ Extract hierarchical nodes<br>  4:<br>r⇐N\[d.id\]                        ▹ Get root node<br>  5:<br>**for all**n∈N**do**<br>  6:<br>**if**\|n.content\|>Lmax**then**<br>  7:<br>C⇐ SemanticSplit(n.content,Lmax)<br>  8:<br>n.content⇐ϵ                 ▹ Clear parent content<br>  9:<br>**for all**c∈C**do**<br>10:<br>nc⇐ CreateChild(n, c)<br>11:<br>N⇐N∪{nc}<br>12:<br>**end for**<br>13:<br>**end if**<br>14:<br>**end for**<br>15:<br>BuildTitlePaths(r,N)                   ▹ Top-down enhancement<br>16:<br>GenerateSummaries(N)                 ▹ Extract knowledge points<br>17:<br>AggregateKnowledge(r,N)                ▹ Bottom-up aggregation<br>18:<br>I\[d.id\]⇐{r,N}<br>19:<br>**end for**<br>20:<br>**return**I |

### 4.2. Distribution-Aware Adaptive Threshold Retrieval

Based on the hierarchical semantic index, we design a distribution-aware adaptive threshold retrieval mechanism that fully exploits hierarchical document features for intelligent retrieval. Traditional retrieval systems usually use a fixed top-k strategy, returning a fixed number of most similar results regardless of the similarity distribution. This approach has clear limitations: when multiple semantic units are highly relevant to the query, important information might be missed; when most units have low relevance, noise may be introduced.

Our hierarchical recursive retrieval algorithm starts from the root node and explores relevant nodes level by level. For a user query q, we compute the similarity between its vector representation and the semantic-enhanced representations of nodes at the current level, i.e., using “multi-level title path + knowledge points + summary” as the similarity computation object:

sim(q,ni)=cosineEmbed(q),Embed(Tpath(ni)+Ki+Si),

(4)

where cosine is the cosine similarity function, Embed(q) is the query vector, Tpath(ni) the title path, Ki the knowledge points, and Si the summary of node ni. This gives a similarity array reflecting the query’s relevance to each semantic-enhanced node.

For these similarity distributions, we propose a distribution-aware adaptive threshold mechanism, which dynamically adjusts the threshold at each level based on statistical characteristics of the similarity distribution. Only nodes with similarity greater than or equal to the threshold are selected as candidate nodes for the next level, continuing recursively to the leaves. This directly addresses the fragmentation issue shown in [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001): instead of a fixed k=3 that would truncate the list, our adaptive threshold detects the high semantic density of the cluster and automatically expands the scope to retrieve all 23 relevant standards as a coherent unit. The threshold is computed as

θraw=β·smax−(1−γ·CV)·(smax−μ).

(5)

where

- θraw: the original dynamic threshold based on similarity distribution;

- smax: the maximum similarity at the current level;

- μ: the average similarity at the current level;

- σ: the standard deviation of similarities at the current level;

- CV=σ/μ: the coefficient of variation, measuring distribution dispersion;

- β: base retention coefficient (0.8≤β≤1), controlling the base threshold ratio;

- γ: distribution sensitivity coefficient (0.8≤γ≤1), controlling sensitivity to similarity distribution.


This mechanism sets the initial threshold based on the maximum similarity. When the similarity distribution is more dispersed (large CV), the system adopts a looser filtering criterion; when the distribution is concentrated (small CV), a stricter criterion is used. Intuitively, in a highly concentrated distribution (e.g., CV<0.1), the threshold approaches β·smax, resulting in precision-oriented filtering that retains the highly cohesive cluster; conversely, in a highly dispersed distribution (e.g., CV>0.5), the threshold drops more aggressively below smax, allowing a broader set of potentially relevant context nodes to pass through.

However, extreme cases may occur in practice, e.g., all node similarities are low, causing the raw threshold to be too low and selecting too many weakly relevant nodes, which may exceed the model’s input limit. To address this, the algorithm incorporates safety mechanisms for computing the final threshold θ:

- Minimum similarity threshold θmin to avoid selecting nodes with excessively low similarity;

- Minimum node count per level kmin to prevent over-filtering of potentially relevant nodes;

- Maximum node count per level kmax to avoid introducing too much noise;

- Overall maximum result count to control retrieval scale.


After retrieval, HiSem-RAG proceeds to the generation stage, integrating the user query and retrieval results into structured context for the large language model to generate answers. Unlike the retrieval stage, the generation stage uses “multi-level title path + index + original content” as context elements.

Through this distribution-aware recursive retrieval mechanism, the system exhibits significant intelligent adaptability: when the query is highly relevant to certain nodes, the system automatically raises the threshold to retain only highly relevant nodes; when all nodes have similarly high relevance, the system appropriately lowers the threshold to keep more potentially relevant information, dynamically balancing retrieval precision and resource consumption in different query scenarios. The specific algorithm is shown as Algorithm 2.


|     |
| --- |
| **Algorithm 2** Distribution-Aware Adaptive Threshold Retrieval |
| **Require:**<br>Query q, hierarchical index I={r,N}, parameters β, γ, θmin, kmax<br>**Ensure:**<br>Retrieved node set R<br>  1:<br>eq⇐ Embed(q)                     ▹ Query embedding<br>  2:<br>R⇐∅; V⇐∅                   ▹ Results and visited sets<br>  3:<br>SearchLevel({r}, 0)<br>  4:<br>**return**R |
| 5:<br>**function** SearchLevel(Nℓ,ℓ)<br>  6:<br>**if**ℓ>ℓmax**or**Nℓ=∅**then**<br>  7:<br>**return**<br>  8:<br>**end if**<br>  9:<br>S⇐∅                    ▹ Similarity scores at level ℓ<br>10:<br>**for all**n∈Nℓ∖V**do**<br>11:<br>sn⇐ Cosine(eq,en)<br>12:<br>S⇐S∪{(n,sn)}<br>13:<br>**end for**<br>14:<br>**if**S≠∅**then**<br>15:<br>θ⇐ AdaptiveThreshold(S,β,γ,θmin)              ▹ Equation ( [5](https://www.mdpi.com/2076-3417/16/2/903#FD5-applsci-16-00903))<br>16:<br>**for all**(n,sn)∈S**where**sn≥θ**do**<br>17:<br>V⇐V∪{n}<br>18:<br>**if** n is leaf **then**<br>19:<br>R⇐R∪{(n,sn)}<br>20:<br>**else**<br>21:<br>SearchLevel(Children(n), ℓ+1)<br>22:<br>**end if**<br>23:<br>**end for**<br>24:<br>**end if**<br>25:<br>**end function** |

By organically combining the hierarchical semantic index structure and the distribution-aware adaptive threshold retrieval mechanism, HiSem-RAG provides a complete solution for processing professional documents with complex hierarchical structures, balancing retrieval comprehensiveness and precision, and offering high-quality context to large language models.

## 5\. Experimental Setup

### 5.1. Datasets

To verify the effectiveness of the HiSem-RAG method, we evaluate various benchmarks on the public power domain expert dataset EleQA \[ [42](https://www.mdpi.com/2076-3417/16/2/903#B42-applsci-16-00903)\] and a self-constructed long-form question answering dataset (LongQA).

EleQA is a publicly available, high-quality dataset in the field of electrical engineering, covering core expert knowledge such as power system operation, equipment maintenance, and safety regulations. This dataset contains 32,610 professional specification clauses and 19,560 QA pairs, with a well-balanced distribution of question types and broad coverage. It features a high degree of professionalism and structuring, making it an important benchmark for assessing models’ capabilities in vertical domain knowledge understanding and application.

LongQA focuses on long-form document QA tasks, aiming to test RAG systems’ comprehensive ability to handle lengthy texts, multi-level structures, and complex semantic relationships. Based on preset screening criteria, we selected 27 representative long documents from technical manuals and e-books, with average length reaching 480,000 characters per document. These documents are highly hierarchical and structurally complex, covering multiple professional knowledge domains, and are well-suited for thoroughly evaluating models’ abilities in cross-paragraph reasoning and information integration.

For QA pair construction, we adopted a three-stage process: human annotation, large language model-assisted generation, and expert review. First, human annotators designed questions covering different hierarchical levels and information spans to ensure diversity. Then, large language models were used to compress document content and generate preliminary answers. Finally, annotators with domain expertise reviewed each answer, supplementing or correcting model-generated fragments to ensure accuracy and completeness.

In total, we constructed 279 high-quality QA pairs, with an average QA length of 511.23 characters. The main challenges of the LongQA dataset are large document spans, complex semantic relationships between paragraphs, requirements for multi-step reasoning, and cross-level information integration, making it suitable for research on advanced long-text processing.

These two datasets are complementary in scale, structure, knowledge domain, and evaluation focus, together forming a comprehensive experimental foundation for evaluating HiSem-RAG. [Table 2](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t002) presents their key statistics and comparison dimensions.

### 5.2. Experimental Design

Three groups of systematic experiments are designed in this study: baseline comparison, resource consumption comparison, and ablation study, to evaluate the overall performance, resource consumption, and component contributions of the HiSem-RAG method, respectively.

#### 5.2.1. Baseline Model Comparison

The baseline comparison experiment aims to comprehensively evaluate the advantages of HiSem-RAG over existing RAG methods. We select five representative RAG methods as baselines, covering both traditional retrieval models and advanced RAG techniques.

For traditional retrieval, we select BM25 and DPR as benchmarks. BM25 calculates relevance based on TF-IDF statistics without relying on neural networks; DPR uses a dual-tower neural encoder to map queries and documents into a shared vector space for similarity computation.

For advanced RAG methods, we select three state-of-the-art approaches: HyDE generates hypothetical documents as retrieval proxies using large language models to enhance query representation; Meta-Chunking adopts an adaptive chunking strategy, combining perplexity and boundary signals to optimize text segmentation; RAPTOR builds document trees via recursive abstraction for multi-level information integration and hierarchical retrieval.

All experiments use the same base model configuration: GLM-4-flash \[ [43](https://www.mdpi.com/2076-3417/16/2/903#B43-applsci-16-00903)\] as the large language model and BGE-M3 \[ [44](https://www.mdpi.com/2076-3417/16/2/903#B44-applsci-16-00903)\] as the text embedding model.

#### 5.2.2. Resource Consumption Comparison

The resource consumption comparison experiment aims to evaluate the effect of the distribution-aware adaptive threshold mechanism on retrieval efficiency and computational cost. To verify its effectiveness, we design resource consumption comparisons under different retrieval strategies and analyze the trade-off between retrieval quantity and model performance.

In the experiment, we change the fixed retrieval number (topk = 5) of DPR and HyDE to dynamic retrieval based on the adaptive threshold (range 1–7), and also replace HiSem-RAG’s adaptive threshold with fixed per-layer retrievals (topk = 2, 3). We then compare the resource consumption differences between fixed and adaptive threshold strategies.

#### 5.2.3. Ablation Study

The ablation study analyzes the independent contribution and synergy of each HiSem-RAG component, validating the rationality of the system’s design. We systematically remove or replace key modules and observe changes in system performance to evaluate their importance.

Specifically, we construct three simplified variants: (1) removing the hierarchical index module and using traditional fixed-window chunking; (2) removing the semantic enhancement module, i.e., not using title information propagation and knowledge point extraction; (3) removing the distribution-aware adaptive threshold module and using a fixed retrieval quantity strategy. By comparing the performance of these variants and the full HiSem-RAG on both datasets, we can quantitatively assess the impact of each component on different tasks and gain deeper insight into their mechanisms.

### 5.3. Evaluation Metrics

For different question types, we design differentiated evaluation metrics for comprehensive and accurate performance assessment. For single-choice, judgement, and fill-in-the-blank questions, we use Accuracy as the main metric, reflecting the model’s ability to answer questions correctly. Accuracy is defined as the ratio of correctly answered questions to the total number of questions:

Accuracy=NumberofCorrectAnswersTotalNumberofQuestions.

(6)

Evaluation standards differ by question type: single-choice and judgement questions are evaluated by strict matching, while fill-in-the-blank questions use semantic judgment, combining large language model and expert review. The prompt for fill-in-the-blank evaluation is shown in [Table 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t001) (third row).

For QA questions, we use BERTScore, ROUGE-L, and MRR@K as evaluation metrics. BERTScore \[ [45](https://www.mdpi.com/2076-3417/16/2/903#B45-applsci-16-00903)\] is a semantic similarity-based metric; it compares the generated and reference answers in semantic space, capturing semantically similar but textually different responses. It focuses on deep semantic understanding and is suitable for open-ended QA. The calculation is as follows:

BERTP=1\|BERTC\|∑xi∈BERTCmaxyj∈BERTRefsim(xi,yj),

(7)

BERTR=1\|BERTRef\|∑yj∈BERTRefmaxxi∈BERTCsim(xi,yj),

(8)

BERTF1=2×BERTP×BERTRBERTP+BERTR.

(9)

where BERTC is the set of tokens in the candidate answer, \|BERTC\| is its size, BERTRef is the set of tokens in the reference answer, \|BERTRef\| is its size, BERTP is precision, BERTR is recall, and sim(xi,yj) is the cosine similarity between candidate token xi and reference token yj.

ROUGE-L is a sequence-matching metric that computes the longest common subsequence between generated and reference texts, assessing whether the generated answer accurately covers core information and maintains reasonable word order. Compared to n-gram exact matches, ROUGE-L focuses more on structural similarity and can tolerate local word order changes. The calculation is as follows:

ROUGER=LCS(ROUGEX,ROUGEY)len(ROUGEY),

(10)

ROUGEP=LCS(ROUGEX,ROUGEY)len(ROUGEX),

(11)

ROUGEL=(1+β2)×ROUGER×ROUGEPROUGER+β2×ROUGEP.

(12)

where ROUGEX is the reference answer, ROUGEY is the generated answer, LCS is the longest common subsequence, ROUGER is recall, ROUGEP is precision, and we set the balance factor β=1 to balance precision and recall.

Mean Reciprocal Rank (MRR) is an important metric for evaluating the ranking quality of retrieval systems, focusing on the rank position of the correct answer in retrieval results. It gives higher weight to correct answers ranked higher. MRR@K only considers the top K results, and is defined as

MRR@K=1\|Q\|∑i=1\|Q\|1ranki·I(ranki≤K).

(13)

where \|Q\| is the total number of queries, ranki is the rank of the correct answer for the i-th query, and I(·) is the indicator function to include only answers ranked within K.

### 5.4. Experimental Environment and Parameter Settings

#### 5.4.1. Hardware Environment

All experiments are conducted on a server equipped with an Intel(R) Xeon(R) Platinum 8375C CPU @2.90 GHz and an NVIDIA A800 80 GB graphics processor.

#### 5.4.2. Parameter Settings

In the HiSem-RAG method, the parameters are configured based on the statistical properties of semantic similarity distributions and hardware constraints, serving as architectural constants rather than sensitive hyperparameters requiring dataset-specific tuning.

- Adaptive Threshold Coefficients (β=0.9,γ=0.8): The base retention coefficient β is set to 0.9 to ensure that only chunks with high relative similarity to the top result are retained. The distribution sensitivity coefficient γ=0.8 allows the threshold to adapt to the variance of similarity scores. These values are selected as robust statistical heuristics to capture the semantically cohesive “head” of the distribution across different contexts.

- Safety Bounds (θmin=0.3,kmax=7): The absolute minimum similarity threshold θmin is set to 0.3 to filter out clearly irrelevant noise. The maximum per-layer node count kmax is limited to 7. This upper bound is determined primarily by the context window limits of the LLM to prevent context overflow, functioning as an engineering safeguard rather than a retrieval variable.

- Global Constraints: The overall maximum number of retrieved results is set to 15, and the chunk length threshold is 1024 tokens. These settings are defined to balance information completeness with the processing capacity of the underlying model (GLM-4-flash).


## 6\. Experimental Results and Analysis

### 6.1. Main Results

#### 6.1.1. Baseline Model Comparison Analysis

The results of the baseline model comparison experiment are shown in [Table 3](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t003) and [Table 4](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t004).

The experimental results show that the HiSem-RAG method achieves superior performance across multiple evaluation dimensions. On the EleQA dataset, HiSem-RAG achieves an overall accuracy of 82.00%, outperforming other baseline methods. Analysis by question type shows that HiSem-RAG performs well in both single-choice and judgment tasks, mainly due to the synergy of its three core mechanisms: the hierarchical semantic index helps preserve the integrity of semantic boundaries between paragraphs; the bidirectional semantic enhancement transmits context information via title paths and knowledge point summaries; the adaptive threshold effectively adjusts the retrieval strategy. Notably, in fill-in-the-blank tasks, HyDE slightly outperforms HiSem-RAG and RAPTOR, possibly due to its use of hypothetical document generation as a retrieval proxy, which offers an advantage in precisely locating information fragments. This highlights the need to optimize retrieval strategies for different task types.

In the LongQA QA evaluation, HiSem-RAG not only demonstrates strong performance in generation quality metrics (with a ROUGE-L of 0.599, significantly higher than other methods) but also shows an advantage in semantic similarity (BERT\_F1 of 0.839). These results indicate that hierarchical semantic indexing and dynamic similarity thresholding are beneficial for long-document processing. When dealing with documents averaging nearly 480,000 characters, HiSem-RAG preserves document structure well and adjusts retrieval granularity according to query characteristics, alleviating the information fragmentation problem faced by traditional methods.

Analysis of retrieval ranking quality further supports these observations. For MRR@1, HiSem-RAG reaches 0.458, about 8 percentage points higher than the second-best, Meta-Chunking, indicating stronger ability to rank relevant documents at the top. The close values of HiSem-RAG’s MRR@3 and MRR@5 suggest its retrieval results are concentrated in the top three, helping reduce retrieval noise. By comparison, RAPTOR’s MRR increases more with K, indicating a more dispersed distribution of relevant results.

Through the organic combination of hierarchical semantic indexing, bidirectional semantic enhancement, and distribution-aware adaptive thresholding, HiSem-RAG flexibly adjusts retrieval strategies while maintaining overall document structure. This leads to significant advantages in most tasks, especially long-document processing, making it practically valuable for complex QA and document understanding tasks. Of course, there is still room for improvement in specific tasks such as fill-in-the-blank, pointing to directions for future research.

#### 6.1.2. Resource Consumption Analysis

To validate the effectiveness of the distribution-aware adaptive threshold mechanism, we conducted resource consumption comparison experiments. We applied adaptive thresholds to existing RAG methods and analyzed their impact on HiSem-RAG performance. Specifically, we replaced the fixed retrieval number (topk = 5) of DPR and HyDE with adaptive threshold-based dynamic retrieval (range 1–7), and also replaced HiSem-RAG’s adaptive threshold with fixed per-layer retrieval (topk = 2, 3). Experimental results are shown in [Figure 3](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f003).

The results show that the adaptive threshold mechanism effectively balances retrieval quality and resource consumption. Applying this mechanism to traditional RAG methods reduces resource consumption while maintaining nearly unchanged accuracy. For example, when DPR uses adaptive thresholds, accuracy drops by just 0.06%, but token consumption decreases by 5.46%. For HyDE, accuracy slightly increases with a 5.75% reduction in token usage. This demonstrates that adaptive thresholds can intelligently adjust retrieval quantity based on query characteristics, avoiding retrieval of excessive irrelevant content.

Analysis of different HiSem-RAG configurations further illustrates this point. With a fixed retrieval of 2 document blocks per layer, token consumption is minimized (32.1 million), but accuracy is limited (73.63%) due to insufficient retrieval. With 3 per layer, accuracy rises to 76.62% but token consumption surges to 59.2 million, indicating clear redundancy. Crucially, even with higher resource use, fixed-3 retrieval’s accuracy is still significantly lower than the adaptive threshold scheme (82.00%). This is because a fixed top-k not only introduces redundancy but also restricts the flexibility of retrieval: some layers require more blocks for key information, while others need only 1–2.

Adaptive thresholding in HiSem-RAG allows dynamic adjustment of retrieval range per layer and query, expanding it when needed (up to 7 blocks) or narrowing it when information is concentrated, thus saving about 11% computation resources while improving accuracy. This mechanism enables the model to break free from fixed window constraints and explore key regions more extensively, avoiding missing important but not absolutely top-ranked documents. These results demonstrate the limitations of fixed top-k retrieval: too small k leads to insufficient information, too large k introduces redundancy and extra computation. The adaptive threshold mechanism dynamically determines the optimal retrieval quantity, ensuring both quality and coverage while avoiding unnecessary resource waste.

### 6.2. Ablation Study

To assess the effectiveness of each HiSem-RAG component, we conducted systematic ablation experiments, removing the three core modules (hierarchical index, semantic enhancement, and adaptive threshold) in turn. Results are shown in [Table 5](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t005) and [Table 6](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t006).

The ablation results highlight the contributions of each HiSem-RAG component across different datasets. All three core modules play significant roles in both tasks, but their impact and mechanisms vary.

The hierarchical index module is foundational for both datasets. On EleQA, removing it reduces overall accuracy by 6.61%; on LongQA, ROUGE-L drops by 23.4% and MRR@1 by 27.3%. This reflects the limitations of traditional fixed-window chunking, which easily disrupts semantic integrity. Hierarchical indexing preserves natural paragraph boundaries and semantic coherence, enabling the model to better grasp document logic. This is especially important for long documents, where multi-level semantic structure is common and maintaining integrity helps the retrieval system understand organization.

The semantic enhancement module has the most pronounced impact. Its removal causes a 6.92% drop in overall EleQA accuracy, a 42.2% decrease in ROUGE-L, and a 67.9% decrease in MRR@1 on LongQA. This indicates that semantic enhancement is crucial for connecting document fragments and supplementing context: title propagation restores lost semantic links during chunking, while knowledge extraction and summarization filter out irrelevant content. Lack of semantic ties severely impacts retrieval quality, especially in long documents where fragments often need more context for accurate understanding.

The adaptive threshold module shows differentiated effects across task types. On EleQA, its effect is most marked on fill-in-the-blank questions: removing it drops accuracy from 74.13% to 62.90%. On LongQA, MRR@1 drops from 0.458 to 0.383. This validates the limitations of fixed-retrieval-number strategies, while adaptive thresholding can dynamically widen or narrow the retrieval scope within hierarchical structures according to query characteristics. This flexibility is especially important for fill-in-the-blank tasks needing precise information localization, as key information may be in non-topmost but relevant areas. For long documents, the mechanism balances retrieval breadth and depth, improving quality while reducing redundancy.

In summary, the ablation study demonstrates the complementary roles of the three core modules. The hierarchical index provides semantically complete base units, semantic enhancement supplements context and deepens understanding, and adaptive thresholding optimizes retrieval strategy to expand relevant coverage. This combination enables HiSem-RAG to adapt to various QA tasks, delivering high performance with reduced computational cost.

### 6.3. Qualitative Case Study: Retrieval Completeness Analysis

To intuitively demonstrate how HiSem-RAG improves contextual completeness compared to traditional methods, we present a detailed step-by-step analysis of a real-world query from the LongQA dataset: “What are the process standards for main transformer installation? ” (Refer to the visualized comparison in [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001)).

**Scenario Setup:** The source document contains structural ambiguity, where the subsection “2. Process Standards” recurs across \*\*multiple chapters\*\* (including Main Transformer System, Neutral Point System, etc.) with identical naming but distinct contexts. The user’s intent specifically targets the standards within the “Main Transformer” chapter.

Step 1: Baseline Retrieval (Traditional RAG) As shown in [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001) B, traditional flat retrieval relies heavily on keyword matching and fixed truncation strategies.

- False Positive: The chunk from the Neutral Point System (Chunk 7) achieves the highest similarity score (0.83) because its content heavily overlaps with the query terms, despite being semantically irrelevant to the requested equipment.

- Context Fragmentation: The subsequent relevant chunk (Chunk 4), which contains critical installation details like “relay protection,” yields a significantly lower similarity score (0.62) because it lacks direct keyword overlap with the query. Consequently, it is excluded by standard top-k or threshold filtering. Furthermore, even if Chunk 4 were retrieved, it would lack the necessary hierarchical context (i.e., belonging to “Main Transformer”), making it difficult for the LLM to interpret correctly.

- Outcome: The generated answer would likely hallucinate by mixing specifications from the wrong system or provide an incomplete response due to missing details.


Step 2: HiSem-RAG Retrieval (Ours) As shown in [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001) C, our method employs structural encoding and adaptive thresholding.

- Path-Aware Scoring: By incorporating the title path “Ch.1 > Main Transformer”, the similarity score of the correct Chunk 3 is boosted to 0.91. Conversely, the distractor (Chunk 7) is penalized due to the path mismatch (“Neutral Point” vs. “Main Transformer”), dropping its score significantly to 0.45.

- Adaptive Expansion: Based on the similarity distribution of the retrieved candidates, the system calculates a dynamic threshold θ=0.80.

- Outcome: The system successfully includes the entire cluster of relevant chunks (Chunks 3, 4–8, all scores > 0.88) while rigorously filtering out the distractor (0.45 < θ). This ensures the LLM receives the complete, non-fragmented procedure for the correct equipment.


This case study confirms that HiSem-RAG effectively utilizes structural semantics to resolve ambiguity and employs adaptive thresholds to guarantee contextual integrity, addressing the limitations observed in baselines.

## 7\. Discussion

This section interprets the results regarding our research questions, compares HiSem-RAG with related work, and discusses practical implications.

### 7.1. Answering Research Questions

Regarding RQ1 (Structure Preservation): Results confirm that preserving natural hierarchical boundaries minimizes information fragmentation. Ablation studies ( [Table 5](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t005)) show that removing the hierarchical index drops overall EleQA accuracy by 6.61%. This aligns with the “structural ambiguity” issue in [Figure 1](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f001), where traditional flat chunking fails to distinguish identical subtitles in different chapters. HiSem-RAG eliminates this ambiguity by enforcing physical document structure.

Regarding RQ2 (Semantic Enhancement): The bidirectional enhancement mechanism is critical for long-context understanding. On LongQA ( [Table 6](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-t006)), removing this module caused a 42.2% drop in ROUGE-L and a 67.9% drop in MRR@1. This answers RQ2: explicitly injecting title paths (Top-Down) and aggregating summaries (Bottom-Up) effectively bridges the semantic gap between distant layers, ensuring retrieved fragments carry full context.

Regarding RQ3 (Adaptive Retrieval): Resource consumption experiments ( [Figure 3](https://www.mdpi.com/2076-3417/16/2/903#applsci-16-00903-f003)) address RQ3, showing that dynamic retrieval outperforms fixed strategies. The distribution-aware threshold reduced token consumption by approximately 11% while maintaining high accuracy (82.00%). This confirms that the optimal retrieval scope is a dynamic variable determined by semantic density, effectively solving the “fragmentation vs. redundancy” dilemma.

### 7.2. Comparison with Related Work

Unlike DPR \[ [2](https://www.mdpi.com/2076-3417/16/2/903#B2-applsci-16-00903)\] and BM25, which treat documents as flat bags of words, HiSem-RAG explicitly encodes structural signals. This significantly reduces hallucinations caused by overlapping keywords in different sections.

Compared to RAPTOR \[ [6](https://www.mdpi.com/2076-3417/16/2/903#B6-applsci-16-00903)\], which builds hierarchy via bottom-up clustering, HiSem-RAG utilizes the explicit document structure. While RAPTOR excels with unstructured text, our method shows superior performance (4% higher accuracy on EleQA) for domain-specific documents where the table of contents provides a logical backbone. This suggests that “following the author’s logic” is often more effective and computationally cheaper than “rediscovering logic via clustering” for professional manuals.

HiSem-RAG also outperforms HyDE \[ [22](https://www.mdpi.com/2076-3417/16/2/903#B22-applsci-16-00903)\] in precise constraint checking on LongQA. HyDE relies on LLM hallucinations, which can be unstable; HiSem-RAG grounds retrieval in the actual document structure, ensuring higher faithfulness in high-stakes domains.

### 7.3. Parameter Robustness Analysis

A key motivation for adaptive thresholding is eliminating the dependency on the rigid top-k hyperparameter. Unlike top-k, our parameters (β,γ) operate on the statistical properties of similarity scores.

- Robustness of β and γ: β defines the tolerance range relative to the best match. Setting β≈0.9 ensures only chunks with similarity scores close to the top result are retained. γ adjusts this based on variance (CV). Theoretical analysis suggests that as long as β is in a high confidence range (e.g., 0.85∼0.95), the retrieved set remains stable.

- Role of kmax: kmax acts solely as an engineering upper bound to protect the LLM context window, not as a primary retrieval logic parameter.


Thus, these parameters act as architectural constants rather than sensitive hyperparameters, allowing HiSem-RAG to generalize across datasets without fine-tuning. We note that preliminary experiments across both EleQA and LongQA datasets confirmed stable performance when β and γ varied within \[0.8,1.0\]; detailed sensitivity curves are omitted for brevity, as the observed variance in accuracy was less than 1%.

### 7.4. Applicability to Unstructured Environments

While HiSem-RAG excels with structured documents, it currently relies on explicit markers (e.g., headings). In scenarios with implicit or noisy structures, performance may degrade. However, as noted in future work, this can be mitigated via an “Implicit Structure Induction” pipeline. Semantic segmentation algorithms can identify logical boundaries in unstructured text, and LLMs can generate synthetic hierarchical titles, transforming implicit semantics into the explicit structure HiSem-RAG requires.

### 7.5. Implications

Theoretical: This study shifts the RAG indexing perspective from “text-based” to “structure–semantic coupled,” highlighting document structure as a dense semantic signal essential for precision.

Practical: For industrial applications like maintenance and engineering, HiSem-RAG offers a “safe” retrieval mechanism. By retrieving complete context clusters, it minimizes the risk of missing safety-critical constraints—a common failure in fixed top-k systems. Additionally, reduced token usage lowers API costs and latency.

## 8\. Conclusions

This paper proposed HiSem-RAG, a method designed to enhance retrieval accuracy in complex, hierarchical documents. By constructing a hierarchical semantic index, employing bidirectional semantic enhancement, and introducing a distribution-aware adaptive threshold, HiSem-RAG effectively resolves issues of structural ambiguity and information fragmentation. Experimental results on EleQA and LongQA datasets demonstrate that our method outperforms state-of-the-art baselines in both accuracy and computational efficiency.

Future Work: Future research will focus on three directions: (1) Unstructured Text Adaptation: Developing implicit structure recognition algorithms to apply HiSem-RAG to texts without explicit headings (e.g., chat logs or flat reports). (2) Multimodal Integration: Extending the hierarchical index to include images and tables, which are prevalent in technical manuals. (3) Lightweight Enhancement: Investigating the use of smaller, distilled models for the semantic enhancement step to further reduce the offline indexing cost.

## Author Contributions

Conceptualization, D.Y.; methodology, D.Y. and J.W.; software, J.W.; validation, J.W.; formal analysis, J.W.; investigation, J.W.; resources, D.Y.; data curation, J.W.; writing—original draft preparation, J.W.; writing—review and editing, D.Y. and J.W.; visualization, J.W.; supervision, D.Y.; project administration, D.Y.; funding acquisition, D.Y. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by the National Natural Science Foundation of China International (Regional) Cooperation and Exchange Project, grant number 62061136006.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

The datasets and code generated and analyzed during the current study are available in the GitHub repository at [https://github.com/CharmingDaiDai/HiSem-RAG](https://github.com/CharmingDaiDai/HiSem-RAG) (accessed on 23 April 2025).

## Conflicts of Interest

The authors declare no conflicts of interest.

## References

01. Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.; Goyal, N.; Küttler, H.; Lewis, M.; Yih, W.t.; Rocktäschel, T.; et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2020; Volume 33, pp. 9459–9474. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieval-augmented+generation+for+knowledge-intensive+nlp+tasks&author=Lewis,+P.&author=Perez,+E.&author=Piktus,+A.&author=Petroni,+F.&author=Karpukhin,+V.&author=Goyal,+N.&author=K%C3%BCttler,+H.&author=Lewis,+M.&author=Yih,+W.t.&author=Rockt%C3%A4schel,+T.&author=et+al.&publication_year=2020&pages=9459%E2%80%939474)\]
02. Karpukhin, V.; Oguz, B.; Min, S.; Lewis, P.S.; Wu, L.; Edunov, S.; Chen, D.; Yih, W.-t. Dense Passage Retrieval for Open-Domain Question Answering. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), Online, 16–20 November 2020; pp. 6769–6781. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Dense+Passage+Retrieval+for+Open-Domain+Question+Answering&conference=Proceedings+of+the+2020+Conference+on+Empirical+Methods+in+Natural+Language+Processing+(EMNLP)&author=Karpukhin,+V.&author=Oguz,+B.&author=Min,+S.&author=Lewis,+P.S.&author=Wu,+L.&author=Edunov,+S.&author=Chen,+D.&author=Yih,+W.-t.&publication_year=2020&pages=6769%E2%80%936781)\]
03. Sawarkar, K.; Mangal, A.; Solanki, S.R. Blended rag: Improving rag (retriever-augmented generation) accuracy with semantic search and hybrid query-based retrievers. In Proceedings of the 2024 IEEE 7th International Conference on Multimedia Information Processing and Retrieval (MIPR), San Jose, CA, USA, 7–9 August 2024; IEEE: Piscataway, NJ, USA, 2024; pp. 155–161. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Blended+rag:+Improving+rag+(retriever-augmented+generation)+accuracy+with+semantic+search+and+hybrid+query-based+retrievers&conference=Proceedings+of+the+2024+IEEE+7th+International+Conference+on+Multimedia+Information+Processing+and+Retrieval+(MIPR)&author=Sawarkar,+K.&author=Mangal,+A.&author=Solanki,+S.R.&publication_year=2024&pages=155%E2%80%93161)\]
04. Asai, A.; Wu, Z.; Wang, Y.; Sil, A.; Hajishirzi, H. Self-rag: Learning to retrieve, generate, and critique through self-reflection. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Self-rag:+Learning+to+retrieve,+generate,+and+critique+through+self-reflection&conference=Proceedings+of+the+Twelfth+International+Conference+on+Learning+Representations&author=Asai,+A.&author=Wu,+Z.&author=Wang,+Y.&author=Sil,+A.&author=Hajishirzi,+H.&publication_year=2024)\]
05. Mansurova, A.; Mansurova, A.; Nugumanova, A. QA-RAG: Exploring LLM reliance on external knowledge. Big Data Cogn. Comput. **2024**, 8, 115\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=QA-RAG:+Exploring+LLM+reliance+on+external+knowledge&author=Mansurova,+A.&author=Mansurova,+A.&author=Nugumanova,+A.&publication_year=2024&journal=Big+Data+Cogn.+Comput.&volume=8&pages=115&doi=10.3390/bdcc8090115)\] \[ [CrossRef](https://doi.org/10.3390/bdcc8090115)\]
06. Sarthi, P.; Abdullah, S.; Tuli, A.; Khanna, S.; Goldie, A.; Manning, C.D. Raptor: Recursive abstractive processing for tree-organized retrieval. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Raptor:+Recursive+abstractive+processing+for+tree-organized+retrieval&conference=Proceedings+of+the+Twelfth+International+Conference+on+Learning+Representations&author=Sarthi,+P.&author=Abdullah,+S.&author=Tuli,+A.&author=Khanna,+S.&author=Goldie,+A.&author=Manning,+C.D.&publication_year=2024)\]
07. Wu, C.; Ding, W.; Jin, Q.; Jiang, J.; Jiang, R.; Xiao, Q.; Liao, L.; Li, X. Retrieval augmented generation-driven information retrieval and question answering in construction management. Adv. Eng. Inform. **2025**, 65, 103158\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieval+augmented+generation-driven+information+retrieval+and+question+answering+in+construction+management&author=Wu,+C.&author=Ding,+W.&author=Jin,+Q.&author=Jiang,+J.&author=Jiang,+R.&author=Xiao,+Q.&author=Liao,+L.&author=Li,+X.&publication_year=2025&journal=Adv.+Eng.+Inform.&volume=65&pages=103158&doi=10.1016/j.aei.2025.103158)\] \[ [CrossRef](https://doi.org/10.1016/j.aei.2025.103158)\]
08. Edge, D.; Trinh, H.; Cheng, N.; Bradley, J.; Chao, A.; Mody, A.; Truitt, S.; Metropolitansky, D.; Ness, R.O.; Larson, J. From local to global: A graph rag approach to query-focused summarization. arXiv **2024**, arXiv:2404.16130. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=From+local+to+global:+A+graph+rag+approach+to+query-focused+summarization&author=Edge,+D.&author=Trinh,+H.&author=Cheng,+N.&author=Bradley,+J.&author=Chao,+A.&author=Mody,+A.&author=Truitt,+S.&author=Metropolitansky,+D.&author=Ness,+R.O.&author=Larson,+J.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2404.16130)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2404.16130)\]
09. Gao, F.; Xu, S.; Hao, W.; Lu, T. KA-RAG: Integrating Knowledge Graphs and Agentic Retrieval-Augmented Generation for an Intelligent Educational Question-Answering Model. Appl. Sci. **2025**, 15, 12547\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=KA-RAG:+Integrating+Knowledge+Graphs+and+Agentic+Retrieval-Augmented+Generation+for+an+Intelligent+Educational+Question-Answering+Model&author=Gao,+F.&author=Xu,+S.&author=Hao,+W.&author=Lu,+T.&publication_year=2025&journal=Appl.+Sci.&volume=15&pages=12547&doi=10.3390/app152312547)\] \[ [CrossRef](https://doi.org/10.3390/app152312547)\]
10. Li, X.; Peng, S.; Yada, S.; Wakamiya, S.; Aramaki, E. GenKP: Generative knowledge prompts for enhancing large language models. Appl. Intell. **2025**, 55, 464\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=GenKP:+Generative+knowledge+prompts+for+enhancing+large+language+models&author=Li,+X.&author=Peng,+S.&author=Yada,+S.&author=Wakamiya,+S.&author=Aramaki,+E.&publication_year=2025&journal=Appl.+Intell.&volume=55&pages=464&doi=10.1007/s10489-025-06318-3)\] \[ [CrossRef](https://doi.org/10.1007/s10489-025-06318-3)\]
11. Zhang, F.; Luo, Y.; Gao, Z.; Han, A. Injury degree appraisal of large language model based on retrieval-augmented generation and deep learning. Int. J. Law Psychiatry **2025**, 100, 102070\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Injury+degree+appraisal+of+large+language+model+based+on+retrieval-augmented+generation+and+deep+learning&author=Zhang,+F.&author=Luo,+Y.&author=Gao,+Z.&author=Han,+A.&publication_year=2025&journal=Int.+J.+Law+Psychiatry&volume=100&pages=102070&doi=10.1016/j.ijlp.2025.102070&pmid=39970564)\] \[ [CrossRef](https://doi.org/10.1016/j.ijlp.2025.102070)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/39970564)\]
12. Bahr, L.; Wehner, C.; Wewerka, J.; Bittencourt, J.; Schmid, U.; Daub, R. Knowledge graph enhanced retrieval-augmented generation for failure mode and effects analysis. J. Ind. Inf. Integr. **2025**, 45, 100807\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Knowledge+graph+enhanced+retrieval-augmented+generation+for+failure+mode+and+effects+analysis&author=Bahr,+L.&author=Wehner,+C.&author=Wewerka,+J.&author=Bittencourt,+J.&author=Schmid,+U.&author=Daub,+R.&publication_year=2025&journal=J.+Ind.+Inf.+Integr.&volume=45&pages=100807&doi=10.1016/j.jii.2025.100807)\] \[ [CrossRef](https://doi.org/10.1016/j.jii.2025.100807)\]
13. Choi, B.; Lee, Y.; Kyung, Y.; Kim, E. ALBERT with Knowledge Graph Encoder Utilizing Semantic Similarity for Commonsense Question Answering. Intell. Autom. Soft Comput. **2023,** 36, 71–82. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=ALBERT+with+Knowledge+Graph+Encoder+Utilizing+Semantic+Similarity+for+Commonsense+Question+Answering&author=Choi,+B.&author=Lee,+Y.&author=Kyung,+Y.&author=Kim,+E.&publication_year=2023&journal=Intell.+Autom.+Soft+Comput.&volume=36&pages=71%E2%80%9382&doi=10.32604/iasc.2023.032783)\] \[ [CrossRef](https://doi.org/10.32604/iasc.2023.032783)\]
14. Theja, R. Evaluating the ideal chunk size for a rag system using llamaindex. LLAMAi \[Online\] **2023**, 30, 31\. Available online: [https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5](https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5) (accessed on 5 October 2023).
15. Xu, P.; Ping, W.; Wu, X.; McAfee, L.; Zhu, C.; Liu, Z.; Subramanian, S.; Bakhturina, E.; Shoeybi, M.; Catanzaro, B. Retrieval meets long context large language models. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieval+meets+long+context+large+language+models&conference=Proceedings+of+the+Twelfth+International+Conference+on+Learning+Representations&author=Xu,+P.&author=Ping,+W.&author=Wu,+X.&author=McAfee,+L.&author=Zhu,+C.&author=Liu,+Z.&author=Subramanian,+S.&author=Bakhturina,+E.&author=Shoeybi,+M.&author=Catanzaro,+B.&publication_year=2024)\]
16. Yang, S. Advanced Rag 01: Small-to-Big Retrieval. 2023. Available online: [https://medium.com/data-science/advanced-rag-01-small-to-big-retrieval-172181b396d4](https://medium.com/data-science/advanced-rag-01-small-to-big-retrieval-172181b396d4) (accessed on 4 November 2023).
17. Krassovitskiy, A.; Mussabayev, R.; Yakunin, K. LLM-Enhanced Semantic Text Segmentation. Appl. Sci. **2025**, 15, 10849\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=LLM-Enhanced+Semantic+Text+Segmentation&author=Krassovitskiy,+A.&author=Mussabayev,+R.&author=Yakunin,+K.&publication_year=2025&journal=Appl.+Sci.&volume=15&pages=10849&doi=10.3390/app151910849)\] \[ [CrossRef](https://doi.org/10.3390/app151910849)\]
18. Zhao, J.; Ji, Z.; Feng, Y.; Qi, P.; Niu, S.; Tang, B.; Xiong, F.; Li, Z. Meta-chunking: Learning efficient text segmentation via logical perception. arXiv **2024**, arXiv:2410.12788. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Meta-chunking:+Learning+efficient+text+segmentation+via+logical+perception&author=Zhao,+J.&author=Ji,+Z.&author=Feng,+Y.&author=Qi,+P.&author=Niu,+S.&author=Tang,+B.&author=Xiong,+F.&author=Li,+Z.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2410.12788)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2410.12788)\]
19. Wang, K.; Reimers, N.; Gurevych, I. DAPR: A benchmark on document-aware passage retrieval. arXiv **2023**, arXiv:2305.13915. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=DAPR:+A+benchmark+on+document-aware+passage+retrieval&author=Wang,+K.&author=Reimers,+N.&author=Gurevych,+I.&publication_year=2023&journal=arXiv)\]
20. Zheng, Z.; Zhang, O.; Borgs, C.; Chayes, J.T.; Yaghi, O.M. ChatGPT chemistry assistant for text mining and the prediction of MOF synthesis. J. Am. Chem. Soc. **2023**, 145, 18048–18062. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=ChatGPT+chemistry+assistant+for+text+mining+and+the+prediction+of+MOF+synthesis&author=Zheng,+Z.&author=Zhang,+O.&author=Borgs,+C.&author=Chayes,+J.T.&author=Yaghi,+O.M.&publication_year=2023&journal=J.+Am.+Chem.+Soc.&volume=145&pages=18048%E2%80%9318062&doi=10.1021/jacs.3c05819)\] \[ [CrossRef](https://doi.org/10.1021/jacs.3c05819)\]
21. Bi, F.; Zhang, Q.; Zhang, J.; Wang, Y.; Chen, Y.; Zhang, Y.; Wang, W.; Zhou, X. A Retrieval-Augmented Generation System for Large Language Models Based on Sliding Window Strategy. J. Comput. Res. Dev. **2025**, 62, 1597–1610. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Retrieval-Augmented+Generation+System+for+Large+Language+Models+Based+on+Sliding+Window+Strategy&author=Bi,+F.&author=Zhang,+Q.&author=Zhang,+J.&author=Wang,+Y.&author=Chen,+Y.&author=Zhang,+Y.&author=Wang,+W.&author=Zhou,+X.&publication_year=2025&journal=J.+Comput.+Res.+Dev.&volume=62&pages=1597%E2%80%931610)\]
22. Gao, L.; Ma, X.; Lin, J.; Callan, J. Precise zero-shot dense retrieval without relevance labels. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Toronto, ON, Canada, 9–14 July 2023; pp. 1762–1777. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Precise+zero-shot+dense+retrieval+without+relevance+labels&conference=Proceedings+of+the+61st+Annual+Meeting+of+the+Association+for+Computational+Linguistics+(Volume+1:+Long+Papers)&author=Gao,+L.&author=Ma,+X.&author=Lin,+J.&author=Callan,+J.&publication_year=2023&pages=1762%E2%80%931777)\]
23. Peng, W.; Li, G.; Jiang, Y.; Wang, Z.; Ou, D.; Zeng, X.; Xu, D.; Xu, T.; Chen, E. Large language model based long-tail query rewriting in taobao search. In Proceedings of the Companion Proceedings of the ACM Web Conference 2024, Singapore, 13–17 May 2024; pp. 20–28. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Large+language+model+based+long-tail+query+rewriting+in+taobao+search&conference=Proceedings+of+the+Companion+Proceedings+of+the+ACM+Web+Conference+2024&author=Peng,+W.&author=Li,+G.&author=Jiang,+Y.&author=Wang,+Z.&author=Ou,+D.&author=Zeng,+X.&author=Xu,+D.&author=Xu,+T.&author=Chen,+E.&publication_year=2024&pages=20%E2%80%9328)\]
24. Liu, B. Demystifying the black box: AI-enhanced logistic regression for lead scoring. Appl. Intell. **2025**, 55, 574\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Demystifying+the+black+box:+AI-enhanced+logistic+regression+for+lead+scoring&author=Liu,+B.&publication_year=2025&journal=Appl.+Intell.&volume=55&pages=574&doi=10.1007/s10489-025-06430-4)\] \[ [CrossRef](https://doi.org/10.1007/s10489-025-06430-4)\]
25. Tupayachi, J.; Li, X. Conversational Geographic Question Answering for Route Optimization: An LLM and Continuous Retrieval-Augmented Generation Approach. In Proceedings of the 17th ACM SIGSPATIAL International Workshop on Computational Transportation Science GenAI and Smart Mobility Session, Atlanta, GA, USA, 29 October–1 November 2024; pp. 56–59. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Conversational+Geographic+Question+Answering+for+Route+Optimization:+An+LLM+and+Continuous+Retrieval-Augmented+Generation+Approach&conference=Proceedings+of+the+17th+ACM+SIGSPATIAL+International+Workshop+on+Computational+Transportation+Science+GenAI+and+Smart+Mobility+Session&author=Tupayachi,+J.&author=Li,+X.&publication_year=2024&pages=56%E2%80%9359)\]
26. Zhang, Y.; Chen, M.; Tian, C.; Yi, Z.; Hu, W.; Luo, W.; Luo, Z. A Multi-Strategy Retrieval-Augmented Generation Method for Knowledge-Based Question Answering in the Military Domain. Comput. Appl. **2025**, 45, 746–754. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Multi-Strategy+Retrieval-Augmented+Generation+Method+for+Knowledge-Based+Question+Answering+in+the+Military+Domain&author=Zhang,+Y.&author=Chen,+M.&author=Tian,+C.&author=Yi,+Z.&author=Hu,+W.&author=Luo,+W.&author=Luo,+Z.&publication_year=2025&journal=Comput.+Appl.&volume=45&pages=746%E2%80%93754)\]
27. Ma, X.; Gong, Y.; He, P.; Zhao, H.; Duan, N. Query rewriting in retrieval-augmented large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, 6–10 December 2023; pp. 5303–5315. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Query+rewriting+in+retrieval-augmented+large+language+models&conference=Proceedings+of+the+2023+Conference+on+Empirical+Methods+in+Natural+Language+Processing&author=Ma,+X.&author=Gong,+Y.&author=He,+P.&author=Zhao,+H.&author=Duan,+N.&publication_year=2023&pages=5303%E2%80%935315)\]
28. Kim, G.; Kim, S.; Jeon, B.; Park, J.; Kang, J. Tree of clarifications: Answering ambiguous questions with retrieval-augmented large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, 6–10 December 2023; pp. 996–1009. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Tree+of+clarifications:+Answering+ambiguous+questions+with+retrieval-augmented+large+language+models&conference=Proceedings+of+the+2023+Conference+on+Empirical+Methods+in+Natural+Language+Processing&author=Kim,+G.&author=Kim,+S.&author=Jeon,+B.&author=Park,+J.&author=Kang,+J.&publication_year=2023&pages=996%E2%80%931009)\]
29. Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; Cao, Y. React: Synergizing reasoning and acting in language models. arXiv **2023**, arXiv:2210.03629. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=React:+Synergizing+reasoning+and+acting+in+language+models&author=Yao,+S.&author=Zhao,+J.&author=Yu,+D.&author=Du,+N.&author=Shafran,+I.&author=Narasimhan,+K.&author=Cao,+Y.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2210.03629)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2210.03629)\]
30. Zhang, J.; Wang, T.; Yao, C.; Xie, H.; Chai, L.; Liu, S.; Li, T.; Li, Z. Construction and Evaluation of an Intelligent Question Answering System for Electric Power Knowledge Base Based on Large Language Models. Comput. Sci. **2024**, 51, 286–292. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Construction+and+Evaluation+of+an+Intelligent+Question+Answering+System+for+Electric+Power+Knowledge+Base+Based+on+Large+Language+Models&author=Zhang,+J.&author=Wang,+T.&author=Yao,+C.&author=Xie,+H.&author=Chai,+L.&author=Liu,+S.&author=Li,+T.&author=Li,+Z.&publication_year=2024&journal=Comput.+Sci.&volume=51&pages=286%E2%80%93292)\]
31. Chen, L.C.; Pardeshi, M.S.; Liao, Y.X.; Pai, K.C. Application of retrieval-augmented generation for interactive industrial knowledge management via a large language model. Comput. Stand. Interfaces **2025**, 94, 103995\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Application+of+retrieval-augmented+generation+for+interactive+industrial+knowledge+management+via+a+large+language+model&author=Chen,+L.C.&author=Pardeshi,+M.S.&author=Liao,+Y.X.&author=Pai,+K.C.&publication_year=2025&journal=Comput.+Stand.+Interfaces&volume=94&pages=103995&doi=10.1016/j.csi.2025.103995)\] \[ [CrossRef](https://doi.org/10.1016/j.csi.2025.103995)\]
32. Wang, Z.; Liu, Z.; Lu, W.; Jia, L. Improving knowledge management in building engineering with hybrid retrieval-augmented generation framework. J. Build. Eng. **2025**, 103, 112189\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Improving+knowledge+management+in+building+engineering+with+hybrid+retrieval-augmented+generation+framework&author=Wang,+Z.&author=Liu,+Z.&author=Lu,+W.&author=Jia,+L.&publication_year=2025&journal=J.+Build.+Eng.&volume=103&pages=112189&doi=10.1016/j.jobe.2025.112189)\] \[ [CrossRef](https://doi.org/10.1016/j.jobe.2025.112189)\]
33. Wan, Y.; Chen, Z.; Liu, Y.; Chen, C.; Packianather, M. Empowering LLMs by hybrid retrieval-augmented generation for domain-centric Q&A in smart manufacturing. Adv. Eng. Inform. **2025**, 65, 103212\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Empowering+LLMs+by+hybrid+retrieval-augmented+generation+for+domain-centric+Q%2526A+in+smart+manufacturing&author=Wan,+Y.&author=Chen,+Z.&author=Liu,+Y.&author=Chen,+C.&author=Packianather,+M.&publication_year=2025&journal=Adv.+Eng.+Inform.&volume=65&pages=103212)\]
34. Zhang, H.; Hao, W.; Jin, D.; Cheng, K.; Zhai, Y. DF-RAG: A Retrieval-Augmented Generation Method Based on Query Rewriting and Knowledge Selection. Comput. Sci. **2025**, 52, 30–39. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=DF-RAG:+A+Retrieval-Augmented+Generation+Method+Based+on+Query+Rewriting+and+Knowledge+Selection&author=Zhang,+H.&author=Hao,+W.&author=Jin,+D.&author=Cheng,+K.&author=Zhai,+Y.&publication_year=2025&journal=Comput.+Sci.&volume=52&pages=30%E2%80%9339)\]
35. Sun, J.; Shi, W.; Shen, X.; Liu, S.; Wei, L.; Wan, Q. Multi-objective math problem generation using large language model through an adaptive multi-level retrieval augmentation framework. Inf. Fusion **2025**, 119, 103037\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Multi-objective+math+problem+generation+using+large+language+model+through+an+adaptive+multi-level+retrieval+augmentation+framework&author=Sun,+J.&author=Shi,+W.&author=Shen,+X.&author=Liu,+S.&author=Wei,+L.&author=Wan,+Q.&publication_year=2025&journal=Inf.+Fusion&volume=119&pages=103037&doi=10.1016/j.inffus.2025.103037)\] \[ [CrossRef](https://doi.org/10.1016/j.inffus.2025.103037)\]
36. Su, H.; Xie, H.; Shi, J.; Wu, D.; Jiang, L.; Huang, H.; He, Z.; Li, Y.; Fang, R.; Zhao, J.; et al. RAICL-DSC: Retrieval-Augmented In-Context Learning for Dialogue State Correction. Knowl.-Based Syst. **2025**, 317, 113423\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=RAICL-DSC:+Retrieval-Augmented+In-Context+Learning+for+Dialogue+State+Correction&author=Su,+H.&author=Xie,+H.&author=Shi,+J.&author=Wu,+D.&author=Jiang,+L.&author=Huang,+H.&author=He,+Z.&author=Li,+Y.&author=Fang,+R.&author=Zhao,+J.&author=et+al.&publication_year=2025&journal=Knowl.-Based+Syst.&volume=317&pages=113423&doi=10.1016/j.knosys.2025.113423)\] \[ [CrossRef](https://doi.org/10.1016/j.knosys.2025.113423)\]
37. He, Z.; Jiang, B.; Wang, X. Improved Retrieval Augmentation and LLM Chain-of-Thought for Maintenance Strategy Generation. Comput. Appl. Softw. **2025**, 42, 1–6+83. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Improved+Retrieval+Augmentation+and+LLM+Chain-of-Thought+for+Maintenance+Strategy+Generation&author=He,+Z.&author=Jiang,+B.&author=Wang,+X.&publication_year=2025&journal=Comput.+Appl.+Softw.&volume=42&pages=1%E2%80%936+83)\]
38. Glass, M.; Rossiello, G.; Chowdhury, M.F.M.; Naik, A.R.; Cai, P.; Gliozzo, A. Re2G: Retrieve, rerank, generate. arXiv **2022**, arXiv:2207.06300. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Re2G:+Retrieve,+rerank,+generate&author=Glass,+M.&author=Rossiello,+G.&author=Chowdhury,+M.F.M.&author=Naik,+A.R.&author=Cai,+P.&author=Gliozzo,+A.&publication_year=2022&journal=arXiv&doi=10.48550/arXiv.2207.06300)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2207.06300)\]
39. Yu, Y.; Ping, W.; Liu, Z.; Wang, B.; You, J.; Zhang, C.; Shoeybi, M.; Catanzaro, B. Rankrag: Unifying context ranking with retrieval-augmented generation in llms. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2024; Volume 37, pp. 121156–121184. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Rankrag:+Unifying+context+ranking+with+retrieval-augmented+generation+in+llms&author=Yu,+Y.&author=Ping,+W.&author=Liu,+Z.&author=Wang,+B.&author=You,+J.&author=Zhang,+C.&author=Shoeybi,+M.&author=Catanzaro,+B.&publication_year=2024&pages=121156%E2%80%93121184)\]
40. Ren, R.; Ma, J.; Zheng, Z. Large language model for interpreting research policy using adaptive two-stage retrieval augmented fine-tuning method. Expert Syst. Appl. **2025**, 278, 127330\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Large+language+model+for+interpreting+research+policy+using+adaptive+two-stage+retrieval+augmented+fine-tuning+method&author=Ren,+R.&author=Ma,+J.&author=Zheng,+Z.&publication_year=2025&journal=Expert+Syst.+Appl.&volume=278&pages=127330&doi=10.1016/j.eswa.2025.127330)\] \[ [CrossRef](https://doi.org/10.1016/j.eswa.2025.127330)\]
41. Xu, C.; Zhao, D.; Wang, B.; Xing, H. Enhancing Retrieval-Augmented LMs with a Two-Stage Consistency Learning Compressor. In Proceedings of the International Conference on Intelligent Computing, Tianjin, China, 5–8 August 2024; Springer: Singapore, 2024; pp. 511–522. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Enhancing+Retrieval-Augmented+LMs+with+a+Two-Stage+Consistency+Learning+Compressor&conference=Proceedings+of+the+International+Conference+on+Intelligent+Computing&author=Xu,+C.&author=Zhao,+D.&author=Wang,+B.&author=Xing,+H.&publication_year=2024&pages=511%E2%80%93522)\]
42. Wang, H.; Wei, J.; Jing, H.; Song, H.; Xu, B. Meta-RAG: A Metadata-Driven Retrieval-Augmented Generation Framework for the Electric Power Domain. Comput. Eng. **2024**, 1–11. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Meta-RAG:+A+Metadata-Driven+Retrieval-Augmented+Generation+Framework+for+the+Electric+Power+Domain&author=Wang,+H.&author=Wei,+J.&author=Jing,+H.&author=Song,+H.&author=Xu,+B.&publication_year=2024&journal=Comput.+Eng.&pages=1%E2%80%9311&doi=10.19678/j.issn.1000-3428.0070415)\] \[ [CrossRef](https://doi.org/10.19678/j.issn.1000-3428.0070415)\]
43. GLM, T.; Zeng, A.; Xu, B.; Wang, B.; Zhang, C.; Yin, D.; Zhang, D.; Rojas, D.; Feng, G.; Zhao, H.; et al. Chatglm: A family of large language models from glm-130b to glm-4 all tools. arXiv **2024**, arXiv:2406.12793. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Chatglm:+A+family+of+large+language+models+from+glm-130b+to+glm-4+all+tools&author=GLM,+T.&author=Zeng,+A.&author=Xu,+B.&author=Wang,+B.&author=Zhang,+C.&author=Yin,+D.&author=Zhang,+D.&author=Rojas,+D.&author=Feng,+G.&author=Zhao,+H.&author=et+al.&publication_year=2024&journal=arXiv)\]
44. Chen, J.; Xiao, S.; Liu, P.; Zhang, K.; Lian, D.; Xie, X.; Li, D. M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation. arXiv **2024**, arXiv:2402.03216. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=M3-Embedding:+Multi-Linguality,+Multi-Functionality,+Multi-Granularity+Text+Embeddings+Through+Self-Knowledge+Distillation&author=Chen,+J.&author=Xiao,+S.&author=Liu,+P.&author=Zhang,+K.&author=Lian,+D.&author=Xie,+X.&author=Li,+D.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2402.03216)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2402.03216)\]
45. Zhang, T.; Kishore, V.; Wu, F.; Weinberger, K.Q.; Artzi, Y. Bertscore: Evaluating text generation with bert. arXiv **2019**, arXiv:1904.09675. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Bertscore:+Evaluating+text+generation+with+bert&author=Zhang,+T.&author=Kishore,+V.&author=Wu,+F.&author=Weinberger,+K.Q.&author=Artzi,+Y.&publication_year=2019&journal=arXiv)\]

**Figure 1.**
A motivating example illustrating the limitations of traditional RAG versus the proposed HiSem-RAG.

**Figure 1.**
A motivating example illustrating the limitations of traditional RAG versus the proposed HiSem-RAG.

**Figure 2.**
The framework of the HiSem-RAG method.

**Figure 2.**
The framework of the HiSem-RAG method.

**Figure 3.**
Experimental results on accuracy and resource consumption.

**Figure 3.**
Experimental results on accuracy and resource consumption.

**Table 1.**
Overview of prompt design.


**Table 1.**
Overview of prompt design.

| Function | Example |
| :-- | :-- |
| Key point and summary extraction | You are a tool for extracting key points and summaries from document paragraphs. Given a text, extract its key points (a set of words separated by commas) and a summary (a paragraph describing the main content). Content: {node.page\_content} |
| Knowledge and summary aggregation | As a document analysis expert, please integrate the key points and summaries of the following subsections to generate the integrated knowledge points and summary for the current section. Current section: {node.title} Current content: {node.page\_content} Subsection key points and summaries: {child\_summaries} Please generate: 1. Core knowledge points (comma-separated keywords or phrases); 2. Summary (comprehensive summary content). Output format: Key points: \[keyword1\], \[keyword2\], … Summary: \[summary content\] |
| Fill-in-the-blank question evaluation | As an objective and fair expert evaluator, please judge whether the following fill-in-the-blank answer is correct. Question: {question\_text} Standard answer: {standard\_answer} Answer: {rag\_answer} Consider: 1. Semantic consistency; 2. Keyword matching; 3. Terminology accuracy. Only answer “correct” or “incorrect”. |

**Table 2.**
Statistics of the experimental datasets.


**Table 2.**
Statistics of the experimental datasets.

| Dataset | Documents<br>Count | QA<br>Pairs | Avg. Doc.<br>Length (Chars) | Question Type Distribution<br>& Avg. QA Length (Chars) |
| :-: | :-: | :-: | :-: | :-- |
| EleQA | 32,610 | 19,560 | 12,159.20 | Single Choice: 6150;Fill-in-the-Blank: 6590;Judgement: 6820 Avg. QA Length: 55.35 chars |
| LongQA | 27 | 279 | 478,982.93 | QA type: 279 Avg. QA Length: 511.23 chars |

**Table 3.**
Experimental results of baseline model comparison (EleQA).


**Table 3.**
Experimental results of baseline model comparison (EleQA).

| Method | Single Choice Acc. | Judgment Acc. | Fill-in-the-Blank Acc. | Overall Acc. |
| :-: | :-: | :-: | :-: | :-: |
| BM25 | 71.28% | 24.77% | 41.46% | 45.16% |
| DPR | 72.35% | 67.98% | 67.67% | 69.27% |
| HyDE | 80.19% | 75.42% | **75.48%** | 76.96% |
| Meta-Chunking | 79.01% | 73.42% | 72.62% | 74.93% |
| RAPTOR | 82.18% | 78.02% | 74.10% | 78.02% |
| HiSem-RAG | **83.12%** | **88.62%** | 74.13% | **82.00%** |

Best results highlighted in bold.

**Table 4.**
Experimental results of baseline model comparison (LongQA).


**Table 4.**
Experimental results of baseline model comparison (LongQA).

| Method | ROUGE-L | BERT\_P | BERT\_R | BERT\_F1 | MRR@1 | MRR@3 | MRR@5 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| BM25 | - | - | - | - | - | - | - |
| DPR | 0.437 | 0.805 | 0.828 | 0.815 | 0.311 | 0.412 | 0.438 |
| HyDE | 0.460 | 0.811 | 0.831 | 0.819 | 0.333 | 0.443 | 0.466 |
| Meta-Chunking | 0.508 | 0.821 | **0.843** | 0.831 | 0.379 | 0.455 | 0.469 |
| RAPTOR | 0.463 | 0.812 | 0.831 | 0.820 | 0.372 | 0.480 | 0.509 |
| HiSem-RAG | **0.599** | **0.837** | **0.843** | **0.839** | **0.458** | **0.585** | **0.587** |

Best results highlighted in bold.

**Table 5.**
Ablation study results (EleQA).


**Table 5.**
Ablation study results (EleQA).

| Method | Single Choice Acc. | Judgment Acc. | Fill-in-the-Blank Acc. | Overall Acc. |
| :-: | :-: | :-: | :-: | :-: |
| without Hierarchical Index | 78.98% | 73.69% | 73.74% | 75.39% |
| without Semantic Enhancement | 77.58% | 74.63% | 73.22% | 75.08% |
| without Adaptive Threshold | 80.32% | 86.55% | 62.90% | 76.62% |
| HiSem-RAG | 83.12% | 88.62% | 74.13% | 82.00% |

**Table 6.**
Ablation study results (LongQA).


**Table 6.**
Ablation study results (LongQA).

| Method | ROUGE-L | BERT\_P | BERT\_R | BERT\_F1 | MRR@1 | MRR@3 | MRR@5 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| without Hierarchical Index | 0.459 | 0.809 | 0.830 | 0.818 | 0.333 | 0.443 | 0.466 |
| without Semantic Enhancement | 0.346 | 0.768 | 0.775 | 0.770 | 0.147 | 0.292 | 0.334 |
| without Adaptive Threshold | 0.501 | 0.799 | 0.798 | 0.797 | 0.383 | 0.494 | 0.499 |
| HiSem-RAG | 0.599 | 0.837 | 0.843 | 0.839 | 0.458 | 0.585 | 0.587 |

|     |     |
| --- | --- |
|  | **Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. |

© 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the [Creative Commons Attribution (CC BY) license](https://creativecommons.org/licenses/by/4.0/).

## Author Contributions

Conceptualization, D.Y.; methodology, D.Y. and J.W.; software, J.W.; validation, J.W.; formal analysis, J.W.; investigation, J.W.; resources, D.Y.; data curation, J.W.; writing—original draft preparation, J.W.; writing—review and editing, D.Y. and J.W.; visualization, J.W.; supervision, D.Y.; project administration, D.Y.; funding acquisition, D.Y. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by the National Natural Science Foundation of China International (Regional) Cooperation and Exchange Project, grant number 62061136006.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

The datasets and code generated and analyzed during the current study are available in the GitHub repository at [https://github.com/CharmingDaiDai/HiSem-RAG](https://github.com/CharmingDaiDai/HiSem-RAG) (accessed on 23 April 2025).

## Conflicts of Interest

The authors declare no conflicts of interest.

## References

01. Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.; Goyal, N.; Küttler, H.; Lewis, M.; Yih, W.t.; Rocktäschel, T.; et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2020; Volume 33, pp. 9459–9474. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieval-augmented+generation+for+knowledge-intensive+nlp+tasks&author=Lewis,+P.&author=Perez,+E.&author=Piktus,+A.&author=Petroni,+F.&author=Karpukhin,+V.&author=Goyal,+N.&author=K%C3%BCttler,+H.&author=Lewis,+M.&author=Yih,+W.t.&author=Rockt%C3%A4schel,+T.&author=et+al.&publication_year=2020&pages=9459%E2%80%939474)\]
02. Karpukhin, V.; Oguz, B.; Min, S.; Lewis, P.S.; Wu, L.; Edunov, S.; Chen, D.; Yih, W.-t. Dense Passage Retrieval for Open-Domain Question Answering. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), Online, 16–20 November 2020; pp. 6769–6781. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Dense+Passage+Retrieval+for+Open-Domain+Question+Answering&conference=Proceedings+of+the+2020+Conference+on+Empirical+Methods+in+Natural+Language+Processing+(EMNLP)&author=Karpukhin,+V.&author=Oguz,+B.&author=Min,+S.&author=Lewis,+P.S.&author=Wu,+L.&author=Edunov,+S.&author=Chen,+D.&author=Yih,+W.-t.&publication_year=2020&pages=6769%E2%80%936781)\]
03. Sawarkar, K.; Mangal, A.; Solanki, S.R. Blended rag: Improving rag (retriever-augmented generation) accuracy with semantic search and hybrid query-based retrievers. In Proceedings of the 2024 IEEE 7th International Conference on Multimedia Information Processing and Retrieval (MIPR), San Jose, CA, USA, 7–9 August 2024; IEEE: Piscataway, NJ, USA, 2024; pp. 155–161. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Blended+rag:+Improving+rag+(retriever-augmented+generation)+accuracy+with+semantic+search+and+hybrid+query-based+retrievers&conference=Proceedings+of+the+2024+IEEE+7th+International+Conference+on+Multimedia+Information+Processing+and+Retrieval+(MIPR)&author=Sawarkar,+K.&author=Mangal,+A.&author=Solanki,+S.R.&publication_year=2024&pages=155%E2%80%93161)\]
04. Asai, A.; Wu, Z.; Wang, Y.; Sil, A.; Hajishirzi, H. Self-rag: Learning to retrieve, generate, and critique through self-reflection. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Self-rag:+Learning+to+retrieve,+generate,+and+critique+through+self-reflection&conference=Proceedings+of+the+Twelfth+International+Conference+on+Learning+Representations&author=Asai,+A.&author=Wu,+Z.&author=Wang,+Y.&author=Sil,+A.&author=Hajishirzi,+H.&publication_year=2024)\]
05. Mansurova, A.; Mansurova, A.; Nugumanova, A. QA-RAG: Exploring LLM reliance on external knowledge. Big Data Cogn. Comput. **2024**, 8, 115\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=QA-RAG:+Exploring+LLM+reliance+on+external+knowledge&author=Mansurova,+A.&author=Mansurova,+A.&author=Nugumanova,+A.&publication_year=2024&journal=Big+Data+Cogn.+Comput.&volume=8&pages=115&doi=10.3390/bdcc8090115)\] \[ [CrossRef](https://doi.org/10.3390/bdcc8090115)\]
06. Sarthi, P.; Abdullah, S.; Tuli, A.; Khanna, S.; Goldie, A.; Manning, C.D. Raptor: Recursive abstractive processing for tree-organized retrieval. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Raptor:+Recursive+abstractive+processing+for+tree-organized+retrieval&conference=Proceedings+of+the+Twelfth+International+Conference+on+Learning+Representations&author=Sarthi,+P.&author=Abdullah,+S.&author=Tuli,+A.&author=Khanna,+S.&author=Goldie,+A.&author=Manning,+C.D.&publication_year=2024)\]
07. Wu, C.; Ding, W.; Jin, Q.; Jiang, J.; Jiang, R.; Xiao, Q.; Liao, L.; Li, X. Retrieval augmented generation-driven information retrieval and question answering in construction management. Adv. Eng. Inform. **2025**, 65, 103158\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieval+augmented+generation-driven+information+retrieval+and+question+answering+in+construction+management&author=Wu,+C.&author=Ding,+W.&author=Jin,+Q.&author=Jiang,+J.&author=Jiang,+R.&author=Xiao,+Q.&author=Liao,+L.&author=Li,+X.&publication_year=2025&journal=Adv.+Eng.+Inform.&volume=65&pages=103158&doi=10.1016/j.aei.2025.103158)\] \[ [CrossRef](https://doi.org/10.1016/j.aei.2025.103158)\]
08. Edge, D.; Trinh, H.; Cheng, N.; Bradley, J.; Chao, A.; Mody, A.; Truitt, S.; Metropolitansky, D.; Ness, R.O.; Larson, J. From local to global: A graph rag approach to query-focused summarization. arXiv **2024**, arXiv:2404.16130. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=From+local+to+global:+A+graph+rag+approach+to+query-focused+summarization&author=Edge,+D.&author=Trinh,+H.&author=Cheng,+N.&author=Bradley,+J.&author=Chao,+A.&author=Mody,+A.&author=Truitt,+S.&author=Metropolitansky,+D.&author=Ness,+R.O.&author=Larson,+J.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2404.16130)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2404.16130)\]
09. Gao, F.; Xu, S.; Hao, W.; Lu, T. KA-RAG: Integrating Knowledge Graphs and Agentic Retrieval-Augmented Generation for an Intelligent Educational Question-Answering Model. Appl. Sci. **2025**, 15, 12547\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=KA-RAG:+Integrating+Knowledge+Graphs+and+Agentic+Retrieval-Augmented+Generation+for+an+Intelligent+Educational+Question-Answering+Model&author=Gao,+F.&author=Xu,+S.&author=Hao,+W.&author=Lu,+T.&publication_year=2025&journal=Appl.+Sci.&volume=15&pages=12547&doi=10.3390/app152312547)\] \[ [CrossRef](https://doi.org/10.3390/app152312547)\]
10. Li, X.; Peng, S.; Yada, S.; Wakamiya, S.; Aramaki, E. GenKP: Generative knowledge prompts for enhancing large language models. Appl. Intell. **2025**, 55, 464\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=GenKP:+Generative+knowledge+prompts+for+enhancing+large+language+models&author=Li,+X.&author=Peng,+S.&author=Yada,+S.&author=Wakamiya,+S.&author=Aramaki,+E.&publication_year=2025&journal=Appl.+Intell.&volume=55&pages=464&doi=10.1007/s10489-025-06318-3)\] \[ [CrossRef](https://doi.org/10.1007/s10489-025-06318-3)\]
11. Zhang, F.; Luo, Y.; Gao, Z.; Han, A. Injury degree appraisal of large language model based on retrieval-augmented generation and deep learning. Int. J. Law Psychiatry **2025**, 100, 102070\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Injury+degree+appraisal+of+large+language+model+based+on+retrieval-augmented+generation+and+deep+learning&author=Zhang,+F.&author=Luo,+Y.&author=Gao,+Z.&author=Han,+A.&publication_year=2025&journal=Int.+J.+Law+Psychiatry&volume=100&pages=102070&doi=10.1016/j.ijlp.2025.102070&pmid=39970564)\] \[ [CrossRef](https://doi.org/10.1016/j.ijlp.2025.102070)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/39970564)\]
12. Bahr, L.; Wehner, C.; Wewerka, J.; Bittencourt, J.; Schmid, U.; Daub, R. Knowledge graph enhanced retrieval-augmented generation for failure mode and effects analysis. J. Ind. Inf. Integr. **2025**, 45, 100807\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Knowledge+graph+enhanced+retrieval-augmented+generation+for+failure+mode+and+effects+analysis&author=Bahr,+L.&author=Wehner,+C.&author=Wewerka,+J.&author=Bittencourt,+J.&author=Schmid,+U.&author=Daub,+R.&publication_year=2025&journal=J.+Ind.+Inf.+Integr.&volume=45&pages=100807&doi=10.1016/j.jii.2025.100807)\] \[ [CrossRef](https://doi.org/10.1016/j.jii.2025.100807)\]
13. Choi, B.; Lee, Y.; Kyung, Y.; Kim, E. ALBERT with Knowledge Graph Encoder Utilizing Semantic Similarity for Commonsense Question Answering. Intell. Autom. Soft Comput. **2023**, 36, 71–82. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=ALBERT+with+Knowledge+Graph+Encoder+Utilizing+Semantic+Similarity+for+Commonsense+Question+Answering&author=Choi,+B.&author=Lee,+Y.&author=Kyung,+Y.&author=Kim,+E.&publication_year=2023&journal=Intell.+Autom.+Soft+Comput.&volume=36&pages=71%E2%80%9382&doi=10.32604/iasc.2023.032783)\] \[ [CrossRef](https://doi.org/10.32604/iasc.2023.032783)\]
14. Theja, R. Evaluating the ideal chunk size for a rag system using llamaindex. LLAMAi \[Online\] **2023**, 30, 31\. Available online: [https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5](https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5) (accessed on 5 October 2023).
15. Xu, P.; Ping, W.; Wu, X.; McAfee, L.; Zhu, C.; Liu, Z.; Subramanian, S.; Bakhturina, E.; Shoeybi, M.; Catanzaro, B. Retrieval meets long context large language models. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 May 2024. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieval+meets+long+context+large+language+models&conference=Proceedings+of+the+Twelfth+International+Conference+on+Learning+Representations&author=Xu,+P.&author=Ping,+W.&author=Wu,+X.&author=McAfee,+L.&author=Zhu,+C.&author=Liu,+Z.&author=Subramanian,+S.&author=Bakhturina,+E.&author=Shoeybi,+M.&author=Catanzaro,+B.&publication_year=2024)\]
16. Yang, S. Advanced Rag 01: Small-to-Big Retrieval. 2023. Available online: [https://medium.com/data-science/advanced-rag-01-small-to-big-retrieval-172181b396d4](https://medium.com/data-science/advanced-rag-01-small-to-big-retrieval-172181b396d4) (accessed on 4 November 2023).
17. Krassovitskiy, A.; Mussabayev, R.; Yakunin, K. LLM-Enhanced Semantic Text Segmentation. Appl. Sci. **2025**, 15, 10849\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=LLM-Enhanced+Semantic+Text+Segmentation&author=Krassovitskiy,+A.&author=Mussabayev,+R.&author=Yakunin,+K.&publication_year=2025&journal=Appl.+Sci.&volume=15&pages=10849&doi=10.3390/app151910849)\] \[ [CrossRef](https://doi.org/10.3390/app151910849)\]
18. Zhao, J.; Ji, Z.; Feng, Y.; Qi, P.; Niu, S.; Tang, B.; Xiong, F.; Li, Z. Meta-chunking: Learning efficient text segmentation via logical perception. arXiv **2024**, arXiv:2410.12788. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Meta-chunking:+Learning+efficient+text+segmentation+via+logical+perception&author=Zhao,+J.&author=Ji,+Z.&author=Feng,+Y.&author=Qi,+P.&author=Niu,+S.&author=Tang,+B.&author=Xiong,+F.&author=Li,+Z.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2410.12788)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2410.12788)\]
19. Wang, K.; Reimers, N.; Gurevych, I. DAPR: A benchmark on document-aware passage retrieval. arXiv **2023**, arXiv:2305.13915. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=DAPR:+A+benchmark+on+document-aware+passage+retrieval&author=Wang,+K.&author=Reimers,+N.&author=Gurevych,+I.&publication_year=2023&journal=arXiv)\]
20. Zheng, Z.; Zhang, O.; Borgs, C.; Chayes, J.T.; Yaghi, O.M. ChatGPT chemistry assistant for text mining and the prediction of MOF synthesis. J. Am. Chem. Soc. **2023**, 145, 18048–18062. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=ChatGPT+chemistry+assistant+for+text+mining+and+the+prediction+of+MOF+synthesis&author=Zheng,+Z.&author=Zhang,+O.&author=Borgs,+C.&author=Chayes,+J.T.&author=Yaghi,+O.M.&publication_year=2023&journal=J.+Am.+Chem.+Soc.&volume=145&pages=18048%E2%80%9318062&doi=10.1021/jacs.3c05819)\] \[ [CrossRef](https://doi.org/10.1021/jacs.3c05819)\]
21. Bi, F.; Zhang, Q.; Zhang, J.; Wang, Y.; Chen, Y.; Zhang, Y.; Wang, W.; Zhou, X. A Retrieval-Augmented Generation System for Large Language Models Based on Sliding Window Strategy. J. Comput. Res. Dev. **2025**, 62, 1597–1610. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Retrieval-Augmented+Generation+System+for+Large+Language+Models+Based+on+Sliding+Window+Strategy&author=Bi,+F.&author=Zhang,+Q.&author=Zhang,+J.&author=Wang,+Y.&author=Chen,+Y.&author=Zhang,+Y.&author=Wang,+W.&author=Zhou,+X.&publication_year=2025&journal=J.+Comput.+Res.+Dev.&volume=62&pages=1597%E2%80%931610)\]
22. Gao, L.; Ma, X.; Lin, J.; Callan, J. Precise zero-shot dense retrieval without relevance labels. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Toronto, ON, Canada, 9–14 July 2023; pp. 1762–1777. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Precise+zero-shot+dense+retrieval+without+relevance+labels&conference=Proceedings+of+the+61st+Annual+Meeting+of+the+Association+for+Computational+Linguistics+(Volume+1:+Long+Papers)&author=Gao,+L.&author=Ma,+X.&author=Lin,+J.&author=Callan,+J.&publication_year=2023&pages=1762%E2%80%931777)\]
23. Peng, W.; Li, G.; Jiang, Y.; Wang, Z.; Ou, D.; Zeng, X.; Xu, D.; Xu, T.; Chen, E. Large language model based long-tail query rewriting in taobao search. In Proceedings of the Companion Proceedings of the ACM Web Conference 2024, Singapore, 13–17 May 2024; pp. 20–28. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Large+language+model+based+long-tail+query+rewriting+in+taobao+search&conference=Proceedings+of+the+Companion+Proceedings+of+the+ACM+Web+Conference+2024&author=Peng,+W.&author=Li,+G.&author=Jiang,+Y.&author=Wang,+Z.&author=Ou,+D.&author=Zeng,+X.&author=Xu,+D.&author=Xu,+T.&author=Chen,+E.&publication_year=2024&pages=20%E2%80%9328)\]
24. Liu, B. Demystifying the black box: AI-enhanced logistic regression for lead scoring. Appl. Intell. **2025**, 55, 574\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Demystifying+the+black+box:+AI-enhanced+logistic+regression+for+lead+scoring&author=Liu,+B.&publication_year=2025&journal=Appl.+Intell.&volume=55&pages=574&doi=10.1007/s10489-025-06430-4)\] \[ [CrossRef](https://doi.org/10.1007/s10489-025-06430-4)\]
25. Tupayachi, J.; Li, X. Conversational Geographic Question Answering for Route Optimization: An LLM and Continuous Retrieval-Augmented Generation Approach. In Proceedings of the 17th ACM SIGSPATIAL International Workshop on Computational Transportation Science GenAI and Smart Mobility Session, Atlanta, GA, USA, 29 October–1 November 2024; pp. 56–59. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Conversational+Geographic+Question+Answering+for+Route+Optimization:+An+LLM+and+Continuous+Retrieval-Augmented+Generation+Approach&conference=Proceedings+of+the+17th+ACM+SIGSPATIAL+International+Workshop+on+Computational+Transportation+Science+GenAI+and+Smart+Mobility+Session&author=Tupayachi,+J.&author=Li,+X.&publication_year=2024&pages=56%E2%80%9359)\]
26. Zhang, Y.; Chen, M.; Tian, C.; Yi, Z.; Hu, W.; Luo, W.; Luo, Z. A Multi-Strategy Retrieval-Augmented Generation Method for Knowledge-Based Question Answering in the Military Domain. Comput. Appl. **2025**, 45, 746–754. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Multi-Strategy+Retrieval-Augmented+Generation+Method+for+Knowledge-Based+Question+Answering+in+the+Military+Domain&author=Zhang,+Y.&author=Chen,+M.&author=Tian,+C.&author=Yi,+Z.&author=Hu,+W.&author=Luo,+W.&author=Luo,+Z.&publication_year=2025&journal=Comput.+Appl.&volume=45&pages=746%E2%80%93754)\]
27. Ma, X.; Gong, Y.; He, P.; Zhao, H.; Duan, N. Query rewriting in retrieval-augmented large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, 6–10 December 2023; pp. 5303–5315. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Query+rewriting+in+retrieval-augmented+large+language+models&conference=Proceedings+of+the+2023+Conference+on+Empirical+Methods+in+Natural+Language+Processing&author=Ma,+X.&author=Gong,+Y.&author=He,+P.&author=Zhao,+H.&author=Duan,+N.&publication_year=2023&pages=5303%E2%80%935315)\]
28. Kim, G.; Kim, S.; Jeon, B.; Park, J.; Kang, J. Tree of clarifications: Answering ambiguous questions with retrieval-augmented large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, 6–10 December 2023; pp. 996–1009. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Tree+of+clarifications:+Answering+ambiguous+questions+with+retrieval-augmented+large+language+models&conference=Proceedings+of+the+2023+Conference+on+Empirical+Methods+in+Natural+Language+Processing&author=Kim,+G.&author=Kim,+S.&author=Jeon,+B.&author=Park,+J.&author=Kang,+J.&publication_year=2023&pages=996%E2%80%931009)\]
29. Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; Cao, Y. React: Synergizing reasoning and acting in language models. arXiv **2023**, arXiv:2210.03629. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=React:+Synergizing+reasoning+and+acting+in+language+models&author=Yao,+S.&author=Zhao,+J.&author=Yu,+D.&author=Du,+N.&author=Shafran,+I.&author=Narasimhan,+K.&author=Cao,+Y.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2210.03629)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2210.03629)\]
30. Zhang, J.; Wang, T.; Yao, C.; Xie, H.; Chai, L.; Liu, S.; Li, T.; Li, Z. Construction and Evaluation of an Intelligent Question Answering System for Electric Power Knowledge Base Based on Large Language Models. Comput. Sci. **2024**, 51, 286–292. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Construction+and+Evaluation+of+an+Intelligent+Question+Answering+System+for+Electric+Power+Knowledge+Base+Based+on+Large+Language+Models&author=Zhang,+J.&author=Wang,+T.&author=Yao,+C.&author=Xie,+H.&author=Chai,+L.&author=Liu,+S.&author=Li,+T.&author=Li,+Z.&publication_year=2024&journal=Comput.+Sci.&volume=51&pages=286%E2%80%93292)\]
31. Chen, L.C.; Pardeshi, M.S.; Liao, Y.X.; Pai, K.C. Application of retrieval-augmented generation for interactive industrial knowledge management via a large language model. Comput. Stand. Interfaces **2025**, 94, 103995\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Application+of+retrieval-augmented+generation+for+interactive+industrial+knowledge+management+via+a+large+language+model&author=Chen,+L.C.&author=Pardeshi,+M.S.&author=Liao,+Y.X.&author=Pai,+K.C.&publication_year=2025&journal=Comput.+Stand.+Interfaces&volume=94&pages=103995&doi=10.1016/j.csi.2025.103995)\] \[ [CrossRef](https://doi.org/10.1016/j.csi.2025.103995)\]
32. Wang, Z.; Liu, Z.; Lu, W.; Jia, L. Improving knowledge management in building engineering with hybrid retrieval-augmented generation framework. J. Build. Eng. **2025**, 103, 112189\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Improving+knowledge+management+in+building+engineering+with+hybrid+retrieval-augmented+generation+framework&author=Wang,+Z.&author=Liu,+Z.&author=Lu,+W.&author=Jia,+L.&publication_year=2025&journal=J.+Build.+Eng.&volume=103&pages=112189&doi=10.1016/j.jobe.2025.112189)\] \[ [CrossRef](https://doi.org/10.1016/j.jobe.2025.112189)\]
33. Wan, Y.; Chen, Z.; Liu, Y.; Chen, C.; Packianather, M. Empowering LLMs by hybrid retrieval-augmented generation for domain-centric Q&A in smart manufacturing. Adv. Eng. Inform. **2025**, 65, 103212\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Empowering+LLMs+by+hybrid+retrieval-augmented+generation+for+domain-centric+Q%2526A+in+smart+manufacturing&author=Wan,+Y.&author=Chen,+Z.&author=Liu,+Y.&author=Chen,+C.&author=Packianather,+M.&publication_year=2025&journal=Adv.+Eng.+Inform.&volume=65&pages=103212)\]
34. Zhang, H.; Hao, W.; Jin, D.; Cheng, K.; Zhai, Y. DF-RAG: A Retrieval-Augmented Generation Method Based on Query Rewriting and Knowledge Selection. Comput. Sci. **2025**, 52, 30–39. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=DF-RAG:+A+Retrieval-Augmented+Generation+Method+Based+on+Query+Rewriting+and+Knowledge+Selection&author=Zhang,+H.&author=Hao,+W.&author=Jin,+D.&author=Cheng,+K.&author=Zhai,+Y.&publication_year=2025&journal=Comput.+Sci.&volume=52&pages=30%E2%80%9339)\]
35. Sun, J.; Shi, W.; Shen, X.; Liu, S.; Wei, L.; Wan, Q. Multi-objective math problem generation using large language model through an adaptive multi-level retrieval augmentation framework. Inf. Fusion **2025**, 119, 103037\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Multi-objective+math+problem+generation+using+large+language+model+through+an+adaptive+multi-level+retrieval+augmentation+framework&author=Sun,+J.&author=Shi,+W.&author=Shen,+X.&author=Liu,+S.&author=Wei,+L.&author=Wan,+Q.&publication_year=2025&journal=Inf.+Fusion&volume=119&pages=103037&doi=10.1016/j.inffus.2025.103037)\] \[ [CrossRef](https://doi.org/10.1016/j.inffus.2025.103037)\]
36. Su, H.; Xie, H.; Shi, J.; Wu, D.; Jiang, L.; Huang, H.; He, Z.; Li, Y.; Fang, R.; Zhao, J.; et al. RAICL-DSC: Retrieval-Augmented In-Context Learning for Dialogue State Correction. Knowl.-Based Syst. **2025**, 317, 113423\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=RAICL-DSC:+Retrieval-Augmented+In-Context+Learning+for+Dialogue+State+Correction&author=Su,+H.&author=Xie,+H.&author=Shi,+J.&author=Wu,+D.&author=Jiang,+L.&author=Huang,+H.&author=He,+Z.&author=Li,+Y.&author=Fang,+R.&author=Zhao,+J.&author=et+al.&publication_year=2025&journal=Knowl.-Based+Syst.&volume=317&pages=113423&doi=10.1016/j.knosys.2025.113423)\] \[ [CrossRef](https://doi.org/10.1016/j.knosys.2025.113423)\]
37. He, Z.; Jiang, B.; Wang, X. Improved Retrieval Augmentation and LLM Chain-of-Thought for Maintenance Strategy Generation. Comput. Appl. Softw. **2025**, 42, 1–6+83. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Improved+Retrieval+Augmentation+and+LLM+Chain-of-Thought+for+Maintenance+Strategy+Generation&author=He,+Z.&author=Jiang,+B.&author=Wang,+X.&publication_year=2025&journal=Comput.+Appl.+Softw.&volume=42&pages=1%E2%80%936+83)\]
38. Glass, M.; Rossiello, G.; Chowdhury, M.F.M.; Naik, A.R.; Cai, P.; Gliozzo, A. Re2G: Retrieve, rerank, generate. arXiv **2022**, arXiv:2207.06300. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Re2G:+Retrieve,+rerank,+generate&author=Glass,+M.&author=Rossiello,+G.&author=Chowdhury,+M.F.M.&author=Naik,+A.R.&author=Cai,+P.&author=Gliozzo,+A.&publication_year=2022&journal=arXiv&doi=10.48550/arXiv.2207.06300)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2207.06300)\]
39. Yu, Y.; Ping, W.; Liu, Z.; Wang, B.; You, J.; Zhang, C.; Shoeybi, M.; Catanzaro, B. Rankrag: Unifying context ranking with retrieval-augmented generation in llms. In Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2024; Volume 37, pp. 121156–121184. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Rankrag:+Unifying+context+ranking+with+retrieval-augmented+generation+in+llms&author=Yu,+Y.&author=Ping,+W.&author=Liu,+Z.&author=Wang,+B.&author=You,+J.&author=Zhang,+C.&author=Shoeybi,+M.&author=Catanzaro,+B.&publication_year=2024&pages=121156%E2%80%93121184)\]
40. Ren, R.; Ma, J.; Zheng, Z. Large language model for interpreting research policy using adaptive two-stage retrieval augmented fine-tuning method. Expert Syst. Appl. **2025**, 278, 127330\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Large+language+model+for+interpreting+research+policy+using+adaptive+two-stage+retrieval+augmented+fine-tuning+method&author=Ren,+R.&author=Ma,+J.&author=Zheng,+Z.&publication_year=2025&journal=Expert+Syst.+Appl.&volume=278&pages=127330&doi=10.1016/j.eswa.2025.127330)\] \[ [CrossRef](https://doi.org/10.1016/j.eswa.2025.127330)\]
41. Xu, C.; Zhao, D.; Wang, B.; Xing, H. Enhancing Retrieval-Augmented LMs with a Two-Stage Consistency Learning Compressor. In Proceedings of the International Conference on Intelligent Computing, Tianjin, China, 5–8 August 2024; Springer: Singapore, 2024; pp. 511–522. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Enhancing+Retrieval-Augmented+LMs+with+a+Two-Stage+Consistency+Learning+Compressor&conference=Proceedings+of+the+International+Conference+on+Intelligent+Computing&author=Xu,+C.&author=Zhao,+D.&author=Wang,+B.&author=Xing,+H.&publication_year=2024&pages=511%E2%80%93522)\]
42. Wang, H.; Wei, J.; Jing, H.; Song, H.; Xu, B. Meta-RAG: A Metadata-Driven Retrieval-Augmented Generation Framework for the Electric Power Domain. Comput. Eng. **2024**, 1–11. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Meta-RAG:+A+Metadata-Driven+Retrieval-Augmented+Generation+Framework+for+the+Electric+Power+Domain&author=Wang,+H.&author=Wei,+J.&author=Jing,+H.&author=Song,+H.&author=Xu,+B.&publication_year=2024&journal=Comput.+Eng.&pages=1%E2%80%9311&doi=10.19678/j.issn.1000-3428.0070415)\] \[ [CrossRef](https://doi.org/10.19678/j.issn.1000-3428.0070415)\]
43. GLM, T.; Zeng, A.; Xu, B.; Wang, B.; Zhang, C.; Yin, D.; Zhang, D.; Rojas, D.; Feng, G.; Zhao, H.; et al. Chatglm: A family of large language models from glm-130b to glm-4 all tools. arXiv **2024**, arXiv:2406.12793. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Chatglm:+A+family+of+large+language+models+from+glm-130b+to+glm-4+all+tools&author=GLM,+T.&author=Zeng,+A.&author=Xu,+B.&author=Wang,+B.&author=Zhang,+C.&author=Yin,+D.&author=Zhang,+D.&author=Rojas,+D.&author=Feng,+G.&author=Zhao,+H.&author=et+al.&publication_year=2024&journal=arXiv)\]
44. Chen, J.; Xiao, S.; Liu, P.; Zhang, K.; Lian, D.; Xie, X.; Li, D. M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation. arXiv **2024**, arXiv:2402.03216. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=M3-Embedding:+Multi-Linguality,+Multi-Functionality,+Multi-Granularity+Text+Embeddings+Through+Self-Knowledge+Distillation&author=Chen,+J.&author=Xiao,+S.&author=Liu,+P.&author=Zhang,+K.&author=Lian,+D.&author=Xie,+X.&author=Li,+D.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2402.03216)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2402.03216)\]
45. Zhang, T.; Kishore, V.; Wu, F.; Weinberger, K.Q.; Artzi, Y. Bertscore: Evaluating text generation with bert. arXiv **2019**, arXiv:1904.09675. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Bertscore:+Evaluating+text+generation+with+bert&author=Zhang,+T.&author=Kishore,+V.&author=Wu,+F.&author=Weinberger,+K.Q.&author=Artzi,+Y.&publication_year=2019&journal=arXiv)\]

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-rag-works-by-neo-kim-and-eric-roby.md">
<details>
<summary>RAG - A Deep Dive</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://newsletter.systemdesign.one/p/how-rag-works>

# RAG - A Deep Dive

### #132: Understanding Retrieval-Augmented Generation

Every large language model ( **LLM**) you use has lied to you with confidence, fluency, and frequency…

Ask any model about something that happened last week. It doesn’t know. It can’t know. Its knowledge was frozen months ago. They might try, and if they do, they will hallucinate.

This isn’t a bug.

It’s a fundamental architectural limitation. LLMs keep knowledge in their parameters. These are billions of numerical weights learned during training. Once training ends, the knowledge is locked. The model doesn’t know what it doesn’t know, so it fills the gaps with confident fabrication. Studies show that hallucination rates can be as low as 1% for simple summarization tasks. However, they can exceed 58% for complex work.

This is exactly what Retrieval-Augmented Generation ( **RAG**) solves.

RAG doesn’t bake knowledge into the model. Instead, it pulls in relevant context when you ask a question. The model stays smart, your data stays current, and every answer is traceable back to its source.

This is the architectural pattern that makes AI actually useful.

Here’s how it works, why it works, and how to build it:

* * *

## **The Knowledge Problem**

We need to understand why LLMs struggle with real-world knowledge before we fix them. The problem has _three_ layers, and none of the obvious solutions work…

https://substackcdn.com/image/fetch/$s_!Knyq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee59d528-eb06-4bac-b934-4eabe279e7e6_1280x720.png

### **LLM knowledge is frozen at training time**

Every LLM has a cutoff date for its knowledge.

Everything the model knows was scraped, processed, and compressed into parameters during training. After that date, the model is blind. It isn’t aware of your new product launch, yesterday’s security issue, or this morning’s HR policy change.

This isn’t a minor inconvenience.

In business, accuracy is crucial. This includes areas like customer support, legal analysis, internal search, and compliance. A model that can’t access current information is a liability. It doesn’t help the business at all.

### **Context Windows Aren’t the Answer**

The brute-force approach is tempting: _dump everything into the prompt._

Context windows have increased a lot. Some models can now handle over a million tokens. But this approach has three fatal problems.

**First, it’s expensive**.

You pay for each token. Sending your entire knowledge base with every query will wipe out your budget.

**Second, there are hard limits.**

A million-token window can’t fit all of a large enterprise’s documents or its databases.

**Third, and this is the one most people miss, models get** _**worse**_ **with more context.**

Research from Stanford and UC Berkeley shows LLM performance follows a U-shaped curve. Models do best when key information is at the start or end, but accuracy drops sharply when important facts are buried in the middle. In Liu et al.’s multi-document QA experiments, accuracy for some models dropped to roughly 25% when key information was placed in the middle of a 20-document context.

It’s clear: adding more context to the prompt doesn’t guarantee the model will use it.

* * *

## **Fine-tuning isn’t the answer either**

Fine-tuning is when you take a pre-trained model and continue training it on your own specific data, so it learns new knowledge or behavior.

Fine-tuning changes the model’s weights to incorporate new knowledge. Think of it like sending someone back to school for a specialized course. In theory, this lets you teach the model about your domain.

In practice, it creates more problems than it solves…

It requires GPU compute, machine learning expertise, and carefully prepared training data. It takes days or weeks to complete. The result is a snapshot. Once your underlying data changes, your fine-tuned model becomes stale.

### **What’s Actually Needed**

The key is to provide the AI with the right information at the right time for each query. And it should be done without changing the model itself.

That’s RAG.

Now let’s investigate RAG deeper:

* * *

## **What RAG actually is**

Retrieval-Augmented Generation is an architectural pattern, not a product. The concept is straightforward, and the best analogy is an open-book exam.

https://substackcdn.com/image/fetch/$s_!WV5q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50ac6e9d-d48d-403a-aafa-40092392d779_1280x720.png

A student taking a closed-book exam relies on what they have memorized.

That’s a standard LLM. It’s smart and can reason, but it’s limited to what’s in its parameters. A student with an open-book exam has the same reasoning skills. They can check relevant pages before answering.

That’s RAG.

The formal definition comes from a 2020 paper by Patrick Lewis and his team at Facebook AI Research and University College London. RAG models combine parametric memory with a pre-trained language model and non-parametric memory. This non-parametric memory uses an external knowledge index. It’s accessed by a neural retriever.

You can still update the model’s knowledge by swapping the retrieval index. No one needs to retrain.

In practice, RAG follows a three-step loop:

1. Query comes in: a user asks a question.

2. Retrieve: System looks in an external knowledge base for the best information chunks.

3. Question and context go to the LLM. It then creates an answer based on the retrieved documents.

You’re not changing the model. You’re changing what it sees. That distinction makes RAG so powerful and so practical.

The open-book analogy makes sense at a high level. But understanding why it works so well means diving deeper into the topic…

* * *

## **How RAG Works Under the Hood**

The three-step loop sounds simple. The engineering that makes it work is where things get interesting.

A RAG system has two main parts:

- An **offline ingestion pipeline** that gets your data ready.

- An **online retrieval pipeline** that answers queries.

Let’s walk through each one…

https://substackcdn.com/image/fetch/$s_!y9LI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F821e9ca3-44bb-4aae-87c9-26d932f2f67a_1280x720.png

### **Embeddings: Core Mechanism**

Before anything else, you need to understand embeddings. This is the concept that enables semantic search.

Text embeddings turn text into dense numerical vectors. These are arrays of floating-point numbers, usually with 1,536 or 3,072 dimensions. They capture the text meaning. The magic is in what “capture meaning” means. Words and sentences with similar intent are close together in vector space. This happens even with different words.

Consider this: _“How do I reset my password?”_ and _“I can’t log into my account”_ use completely different words.

But when converted to embeddings, they produce nearly identical vectors. The distance between them is tiny because their meanings are similar. This is measured using cosine similarity, dot product, or Euclidean distance.

The key insight for RAG is clear.

System finds relevant content. It does this even if the user’s question doesn’t use the exact words from the source document. It searches by meaning, not by keywords.

### **Data Ingestion Pipeline (Offline Phase)**

First, process your knowledge base. Then, index it. Only then can your RAG system answer questions.

This happens in five steps:

**What triggers the offline phase?**

In traditional workflows, this pipeline runs when new data is available. This can happen when documents are added or updated. It can also occur when a database changes or on a regular schedule, like nightly or weekly. Some teams trigger re-ingestion if retrieval quality drops.

They also do this when a new data source connects:

1.  **Load documents from anywhere**: PDFs, databases, APIs, wikis, Slack channels, and Confluence pages. Frameworks like LangChain and LlamaIndex offer ready-made connectors for many common sources.

2.  **Chunking** **:** Split documents into semantically meaningful pieces. This is the single highest-leverage step to get right, and we will cover it in depth later.

3.  **Embedding:** Convert each chunk into a vector using an embedding model.

4.  **Storage:** Store the vectors in a vector database optimized for similarity search.

5.  **Metadata tagging:** Tag each chunk with source, timestamp, category, and access control information. This metadata becomes critical for filtering, attribution, and security later.

### **Retrieval Pipeline (Online Phase)**

When a user asks a question, the retrieval pipeline kicks in:

1.  **Query embedding**: User’s question turns into a vector. This uses the same embedding model from ingestion. This is critical: the query and the documents must live in the same vector space.

2.  **Similarity search**: The system finds the top-K similar chunks. It compares the query vector to each vector in the database.

3.  **Retrieval strategy**: This is where the real engineering decisions happen. Three primary approaches exist:

    1.  Sparse retrieval uses a statistical method that matches exact keywords. It weighs these matches using term frequency and inverse document frequency.

    2.  Dense retrieval (embeddings):Semantic search via vectors. Finds conceptually relevant content even when the wording differs.

    3.  Hybrid search (combining both): Use both sparse and dense retrieval. Then, merge the results with Reciprocal Rank Fusion (RRF). This boosts documents that rank high in both systems.
4.  **Re-ranking**: After retrieving results, a cross-encoder model rescans them. It processes the query and each document as one input. This captures fine-grained relevance that bi-encoders miss.

### **Generation Phase**

With the most relevant chunks in hand, the system assembles the final prompt:

1.  **Prompt Construction:**

    1.  **System Prompt:** Combine the system prompt (the instructions that tell the LLM how to behave, like _“You are a helpful customer support agent”_) with the user’s request.

    2.  **Retrieved Context Chunks:** Integrate the relevant pieces of text pulled from your knowledge base. For instance, if someone asks, _“What’s your refund policy?”_ You might pull two paragraphs from your company’s policy document.

    3.  **User’s Original Query:** Include the user’s actual question or task — exactly as they typed it.
2.  **LLM Call:** The model generates an answer grounded in the retrieved documents. The key facts are in the prompt. The model uses these facts to reason instead of relying on its trained memory. Think of it like giving someone an open-book exam instead of asking them to answer from memory.

3.  **Citation and Attribution:** The system shows which source documents were used and provides verifiable citations. For example, the response might say, _“Based on Section 3.2 of the Employee Handbook...”_ so the user knows exactly where the answer came from. This is one of RAG’s biggest advantages over fine-tuning: transparency.

Now that you know how RAG works mechanically, the real question is whether it’s the right tool. That depends on what you’re comparing it to…

* * *

## **Why RAG over alternatives?**

RAG isn’t the only approach to giving AI access to knowledge.

You need to know when to use it and when not to. This means comparing it to other options.

### **RAG vs. Fine-Tuning**

This is the comparison most teams face first. Here’s how they stack up:

https://substackcdn.com/image/fetch/$s_!1-2N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80bd91be-a383-4f21-a05e-1a2acadabb96_1164x814.png

The key nuance: fine-tuning and RAG are complementary, not competing.

Fine-tuning is the best option when you want to adjust the model’s behavior, style, or output format, not just its knowledge. The best production systems do two things: they fine-tune style and behavior, and then they use RAG for knowledge. You can adjust a model to produce structured JSON in a certain format.

Then, use RAG to fill it with up-to-date data.

### **RAG vs. Long Context Windows**

Context windows keep growing. Why not dump everything in the prompt?

Cost and precision. RAG retrieves only the 5-20 most relevant chunks. Long context stuffs everything in and hopes the model finds the needle. RAG is cheaper per query. It’s also more precise in what it finds. Plus, it can search millions of documents, unlike others that have a token limit.

They work well together: first, use RAG to get the right 20 chunks.

Then, use long context to process them all at once. The “lost in the middle” research shows that retrieving small, relevant chunks works better than using large context windows.

* * *

## **Traditional RAG vs. Agentic RAG**

Traditional RAG follows the straightforward three-step loop described above: retrieve, then generate. It works well for simple question-answering but has limitations. What happens when the first retrieval doesn’t return good results? Traditional RAG just pushes forward with whatever it finds.

Agentic RAG adds a reasoning layer on top.

An AI agent decides how to handle each query. It can change the search, link several retrievals, pick a knowledge base, or skip retrieval completely. Think of Traditional RAG as a student who looks up one page and writes their answer. Agentic RAG is like a student. They check several sources. They re-read sections that seem off and cross-reference information before writing.

https://substackcdn.com/image/fetch/$s_!WJ3i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb15a5d41-dd18-4a64-bd28-79621c669aec_1404x570.png

* * *

## **Multi-Step RAG Pipeline**

Production RAG systems often go beyond the simple retrieve-and-generate loop. A multi-step pipeline adds intelligence before and after retrieval:

1.  Query Intent Parsing: Before searching, the system analyzes what the user actually wants. Is it a factual question? A comparison? A request for a summary? Understanding intent helps the system choose the right retrieval strategy and knowledge base.

2.  Query Reformulation: The system may rewrite the user’s question to improve retrieval quality. For example, _“Why is my app slow?”_ might become _“application performance bottleneck causes and solutions.”_

3.  Retrieval: System searches for relevant chunks (as described above).

4.  Live Web Search: If internal documents aren’t enough, some RAG systems can do live web searches. This helps them get current information from the internet.

5.  Reranking and Filtering: Results are scored, filtered, and reranked for relevance.

6.  Generation: LLM produces an answer grounded in all the gathered context.

This multi-step approach is what separates demo-quality RAG from production-quality RAG.

* * *

## **RAG Limitations**

RAG is powerful, but it’s not a silver bullet…

Understanding its limitations helps you decide when to use it and when to look elsewhere:

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="how-to-build-reliable-rag-a-deep-dive-into-7-failure-points-.md">
<details>
<summary>How to Build Reliable RAG: A Deep Dive into 7 Failure Points and Evaluation Frameworks – Unite.AI</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.unite.ai/how-to-build-reliable-rag-a-deep-dive-into-7-failure-points-and-evaluation-frameworks/>

# How to Build Reliable RAG: A Deep Dive into 7 Failure Points and Evaluation Frameworks – Unite.AI

[Retrieval-Augmented Generation (RAG)](https://kuriko-iwai.com/research/rag-architectures-decision-path-guide#what%20is%20retrieval-augmented%20generation%20(rag)) is critical for modern AI architecture, serving as an essential framework for building context-aware agents.

But moving from a basic prototype to a production-ready system involves navigating significant hurdles in data retrieval, context consolidation, and response synthesis.

This article provides a deep dive into seven typical RAG failure points and the evaluation metrics with practical coding examples.

## The Anatomy of RAG Breakdown – 7 Failure Points (FPs)

According to researchers [Barnett et al](https://arxiv.org/html/2401.05856v1)., [Retrieval Augmented Generation (RAG) systems](https://kuriko-iwai.com/research/rag-architectures-decision-path-guide#what%20is%20retrieval-augmented%20generation%20(rag)) encounter seven specific **Failure Points (FPs)** throughout the pipeline.

The below diagram illustrates these stages:

https://cdn.hashnode.com/uploads/covers/6827f43594450a7a13bb4500/5f082b4d-295f-440e-9b21-75382da0982a.png

Figure A. Indexing and Query processes required for creating a RAG system. The indexing process is done at development time and queries at runtime. Failure points identified in this study are shown in red boxes (source)

Let us explore each FP arranged according to the pipeline sequence, following the top-left to bottom-right progression shown in **Figure A**.

### FP1. Missing Content

Missing content happens when the system is asked a question that cannot be answered because the relevant information is not present in the available vector store in the first place.

The failure occurs when an LLM provides a plausible-sounding but incorrect response instead of stating _it doesn’t know_.

### FP2. Missed the Top-Ranked Documents

This is a situation where a correct document exists in the vector store, but the retriever fails to rank it highly enough to include it in top-k documents fed to an LLM as context.

In consequence, the correct information never reaches the LLM.

### FP3. Not in Context (Consolidation Strategy Limitations)

This is a situation where a correct document exists and is retrieved from the vector store, but is excluded during the consolidation process.

This happens when too many documents are returned and the system must filter them down to fit within an LLM’s context window, token limits, or rate limits.

### FP4. Not Extracted

This is a situation where an LLM fails to identify the correct information in the context, even though the correct information was in the vector store, and successfully retrieved/consolidated.

This happens when the context is overly noisy or contains contradictory information that confuses the LLM.

### FP5. Wrong Format

This is a situation where storage, retrieval, consolidation, and LLM interpretation are successfully handled, but the LLM fails to follow specific formatting instructions provided in the prompt, such as a table, a bulleted list, or a JSON schema.

### FP6. Incorrect Specificity

An LLM’s output is technically present, but **either too general or too complex compared to the user’s needs.**

For example, an LLM generates simple answers to a user query with a complex professional goal.

### FP7. Incomplete Answers

This is a situation where an LLM generates an output not necessarily wrong, but missing key pieces of information that were available in the context.

For example, when a user asks a complex question like **_“What are the key points in documents A, B, and C?” ,_** the LLM only addresses one or two of the sources.

## How FPs Compromise RAG Pipeline Performance

Each of these FPs impact performance of RAG pipelines:

### Data Integrity & Trust Failures

When missing or incorrect information is present, the system is no longer a reliable source of information. Primary FPs include:

- **FP1 (Missing Content):** The answer is not in the doc in the first place.
- **FP4 (Not Extracted):** The LLM decides to ignore the correct answer in the doc.
- **FP7 (Incomplete):** The LLM gives half-truths, missing important pieces.

### Retrieval & Efficiency Bottlenecks

The RAG pipeline can be inefficient when it misses key information in the retrieval and consolidation stages. Primary FPs include:

- **FP2 (Missed Top Ranked):** The embedding model fails to select top-k embeddings.
- **FP3 (Consolidation Strategy):** The script to trim docs to fit the LLM limits drops the most important parts.

### User Experience & Formatting Errors

Although correct, an output with poor readability or in a wrong format can compromise user experience. Primary FPs include:

- **FP5 (Wrong Format):** The LLM fails to follow the specific output format like JSON.
- **FP6 (Incorrect Specificity)**: The LLM generates a lengthy output for a simple yes/no question, or vise versa (too brief answer to a complicated question).

## The Evaluation Stack: Frameworks to Mitigate FPs

Evaluation metrics are designed to systematically mitigate these FPs.

This section explores major evaluation metrics with practical use cases.

#### Major RAG Evaluation Metrics:

- **DeepEval**
- **RAGAS**
- **TruLens**
- **Arize Phoenix**
- **Braintrust**

### DeepEval – The Unit Test before Deployment

**DeepEval** calculates a weighted score based on the criteria.

An **LLM-as-a-judge** (e.g., GPT-4o) evaluates each criteria against an LLM’s output:

https://cdn.hashnode.com/uploads/covers/6827f43594450a7a13bb4500/6167dc69-eda4-4169-ba9f-a91c9920b4b2.png

DeepEval leverages **G-eval**, a **chain-of-thought (CoT)** framework which takes the multi-step approach to evaluate the output:

1.  **Define a criteria** to measure (e.g., “coherence,” “fluency,” or “relevance”).
2.  Generate **evaluation steps** (using an evaluator LLM).
3.  Follow the evaluation step and analyzes the input and the LLM’s output.
4.  Calculates an **expected weighted sum** of the score of each criteria.

#### Common Scenario in Practice

-   **Situation:** A technical documentation assistant (bot) for a complex software product seems to be working every time the engineer team updates the codebase.
-   **Problem:** No quantitative proof if the bot can still answer the user query (You just “think” it’s working…).
-   **Solution:** Integrate a PyTest function as CI/CD regression suite into Github Action where DeepEval runs `G-Eval` and others metrics over a test case:

-   **Expected results:** If any score of the metrics drops below the threshold (0.85), the PyTest raises `AssertionError` – immediately failing the CI build, preventing the silent regression from reaching production.

#### Pros

-   A variety of metrics (50+) including specialized bias and toxicity checks are available.
-   Seamlessly integrates with existing CI/CD pipelines.
-   No reference needed. Assess an output based solely on the prompt and provided context.

#### Cons

-   The quality of evaluation heavily depends on the judge LLM’s capabilities.
-   Computationally expensive when the judge LLM is a high-end model.

> **Developer Note – The Test Case for DeepEval**
>
> A set of `LLMTestCase` objects defines the test case that DeepEval runs.
>
> In practice, this test case should contain most important user queries and labeled outputs with the retrieved context.
>
> These can be retrieved from a JSON or CSV file.

### RAGAS – The Needle in a Haystack Optimizer

**Retrieval Augmented Generation Assessment (Ragas)** aims to evaluate RAG without human-annotated dataset by generating synthetic test sets.

Then, it computes flagship metrics:

https://cdn.hashnode.com/uploads/covers/6827f43594450a7a13bb4500/3fb44eba-a951-4afc-90fa-3802a7b91b54.png

Figure B. The RAGAS evaluation triad diagram connecting Question, Context, and Answer through Precision, Recall, Faithfulness, and Relevancy metrics (Created by Kuriko IWAI)

The flagship metrics are categorized into the three groups:

-   Retrieval pipeline (black, solid line, **Figure B**): Context precision, context recall.
-   Generation pipeline (black, dotted line, **Figure B**): Faithfulness, answer relevancy.
-   Ground truth (red box, **Figure B**): Answer semantic similarity, answer correctness.

#### Common Scenario in Practice

-   **Situation:** The RAG system for legal contracts is missing key clauses. You are unsure if the problem is in the Search (Retriever) or the Reading (Generator).
-   **Problem:** No idea on the optimal top-k (number of chunks retrieved).
-   **Solution:** Use RAGAS to create a synthetic test set with 100 pairs of questions and evidence. Then, run the RAG pipeline against the test set to calculate context recall and context precision:
-   **Expected result:** Depending on the metric results, action plan can be the following:

|     |     |     |     |
| --- | --- | --- | --- |
| **Metric** | **Score** | **Diagnostic** | **Action Plan** |
| **Context Recall** | Low | The retriever missed the correct info. | – Increase top-k.<br>– Try [hybrid search (BM25 + Vector)](https://kuriko-iwai.com/research/vector-databases-and-embedding-strategies-guide#hybrid%20embedding%20in%20action). |
| **Context Precision** | Low | Top-k chunks contain too much filter and noise – confusing the LLM. | – Decrease top-k<br>– Implement a Reranker (e.g., Cohere). |
| **Faithfulness** | Low | The generator is hallucinating despite having data. | – Adjust system prompt.<br>– Check for context window limits. |

**Table 1.** RAGAS Diagnostic Action Plan – Mapping Scores to System Adjustments.

#### Pros

-   Excellent for an early-stage project without ground-true datasets (As we saw in the code snippet, RAGAS can make a synthetic test set).

#### Cons

-   Synthetic test set might miss nuanced factual errors.
-   Requires a robust extractor model to break down answers into individual claims (I used `gpt-4o` in the example).

### TruLens – The Feedback Loop Specialist

**TruLens** focuses on the internal mechanics of the RAG process rather than just the final output by using **feedback functions.**

It also uses an LLM-based score reflecting how well the response satisfies the query’s intent, using a 4-point Likert scale (0-3), making it superior for **ranking the quality** of different search results.

#### Common Scenario in Practice

-   **Situation:** A medical advisor bot answers a user’s question correctly but adds a pro-tip that isn’t in the vetted PDF base.
-   **Problem:** The add-on pro-tip might be helpful, but not grounded.
-   **Solution:** Use TruLens to implement a groundedness feedback function with a threshold like `score > 0.8`.

-   **Expected results:** When the LLM generates a response that contains information not present in the retrieved chunks, TruLens flags the record in your dashboard.

#### Pros

-   Visualizes the reasoning chain to identify exactly where the agent went off-track.
-   Provides built-in support for grounding to catch hallucinations in real-time.

#### Cons

-   Learning curve for defining custom feedback functions.
-   The dashboard can feel heavyweight for simple scripts.

### Arize Phoenix – The Silent Failure Map

**Arize Phoenix** is an open-source observability and evaluation tool to evaluate LLM outputs, including complex RAG systems.

Built on OpenTelemetry by Arize AI, it focuses on observability by treating LLM evaluation as a subset of MLOps.

In the context of RAG evaluation, Phoenix excels at **embedding analysis**, using **Uniform Manifold Approximation and Projection (UMAP)** to reduce high-dimensional vector embeddings into 2D/3D space.

This embedding analysis mathematically reveals if the failed queries are semantically grouped together, which indicates a gap in the vector database.

#### Common Scenario in Practice

-   **Situation:** A customer support bot works great for refunds, but gives nonsensical answers to warranty claims.
-   **Problem:** Data hole in the vector database (Cannot find in logs).
-   **Solution:** Use Arize Phoenix to generate a Umap Embedding Visualization (UEV), a 3D map for the vector database – to overlay user queries on the document chunks.
-   **Expected results:** Visually see a cluster of user queries landing in the dark zone where no documents exist, telling that some documents are forgotten to upload to the vector store.

#### Pros

-   OpenTelemetry-native; integrates with existing enterprise monitoring stacks.
-   The best tool for visualizing blind spots of the vector store.

#### Cons

-   Less focused on scoring, more on observing.
-   Can be overkill for small-scale applications or single-agent tools.

### Braintrust – The Prompt Regression Safety Net

**Braintrust** is designed for high-frequency iteration cycles by using **cross-model comparison**.

Common Scenario in Practice

-   **Situation:** An engineer team upgrade prompt from “Answer the question” (Case A) to a more complex 500-word system instruction (Case B).
-   **Problem:** Improving the prompt for Case B might accidentally break Case A.
-   **Solution:** Use Braintrust to create a golden dataset with a set of N perfect examples (e.g., `N = 50`). Let Braintrust run side-by-side (SxS) comparison every time the team updates a single word in prompt:

-   **Expected result:** A difference report showing exactly which cases got better/worse for each of the golden dataset (N = 50).

#### Pros

-   Extremely fast to test before the deployment.
-   Great UI for non-technical stakeholders to review and grade the output.

#### Cons

-   Proprietary/SaaS-focused (though they have open-source components).
-   Fewer built-in deep-tech metrics compared to DeepEval or Ragas.

## Wrapping Up

When handled with proper evaluation frameworks, RAG can be a competitive tool to provide an LLM context most relevant to the user query.

### Implementation Strategy: Mapping Metrics to Failure Points

Although there’s no one-fit-all solution, **Table 2** shows which evaluation metrics to apply for each FP we covered in this article:

|     |     |     |
| --- | --- | --- |
| **Failure Point** | **Evaluation Metric Idea** | **Feature to Use** |
| **FP1: Missing Content** | **RAGAS** | Faithfulness / Answer Correctness |
| **FP2: Missed Ranking** | **TruLens** | Context Recall / Precision |
| **FP3: Consolidation** | **Arize Phoenix** | Retrieval Tracing & Latency Analysis |
| **FP4: Not Extracted** | **DeepEval** | Faithfulness / Contextual Recall |
| **FP5: Wrong Format** | **DeepEval** | G-Eval (Custom Rubric) |
| **FP6: Specificity** | **Braintrust** | Manual Grading & Side-by-Side Eval |
| **FP7: Incomplete** | **RAGAS** | Answer Relevancy |

**Table 2.** The Failure Point Mitigation Matrix – Which Tool Solves Which FP?

**DeepEval** and **RAGAS** can leverage their faithfulness metrics to measure data integrity failures ( **FP1, FP4, FP7**).

**TruLens** leverages its context precision / recall to measure the context relevance to the output – effectively assessing **FP2**.

**Arize Phoenix** provides a visual trace of the retrieval process, making it easy to see if the document retrieved was lost during the consolidation ( **FP3**).

For UX failures, **DeepEval** creates custom metrics to assess UX failures, while **Braintrust** excels at ground-truth dataset comparison.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="what-is-rag-understanding-retrieval-augmented-generation-qdr.md">
<details>
<summary>What is RAG: Understanding Retrieval-Augmented Generation</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://qdrant.tech/articles/what-is-rag-in-ai/>

# What is RAG: Understanding Retrieval-Augmented Generation

Sabrina Aquino

·

March 19, 2024

https://qdrant.tech/articles_data/what-is-rag-in-ai/preview/title.jpg

> Retrieval-augmented generation (RAG) integrates external information retrieval into the process of generating responses by Large Language Models (LLMs). It searches a database for information beyond its pre-trained knowledge base, significantly improving the accuracy and relevance of the generated responses.

Language models have exploded on the internet ever since ChatGPT came out, and rightfully so. They can write essays, code entire programs, and even make memes (though we’re still deciding on whether that’s a good thing).

But as brilliant as these chatbots become, they still have **limitations** in tasks requiring external knowledge and factual information. Yes, it can describe the honeybee’s waggle dance in excruciating detail. But they become far more valuable if they can generate insights from **any data** that we provide, rather than just their original training data. Since retraining those large language models from scratch costs millions of dollars and takes months, we need better ways to give our existing LLMs access to our custom data.

While you could be more creative with your prompts, it is only a short-term solution. LLMs can consider only a **limited** amount of text in their responses, known as a [context window](https://www.hopsworks.ai/dictionary/context-window-for-llms). Some models like GPT-3 can see up to around 12 pages of text (that’s 4,096 tokens of context). That’s not good enough for most knowledge bases.

https://qdrant.tech/articles_data/what-is-rag-in-ai/how-rag-works.jpg

The image above shows how a basic RAG system works. Before forwarding the question to the LLM, we have a layer that searches our knowledge base for the “relevant knowledge” to answer the user query. Specifically, in this case, the spending data from the last month. Our LLM can now generate a **relevant non-hallucinated** response about our budget.

As your data grows, you’ll need [efficient ways](https://qdrant.tech/rag/rag-evaluation-guide/) to identify the most relevant information for your LLM’s limited memory. This is where you’ll want a proper way to store and retrieve the specific data you’ll need for your query, without needing the LLM to remember it.

**Vector databases** store information as **vector embeddings**. This format supports efficient similarity searches to retrieve relevant data for your query. For example, Qdrant is specifically designed to perform fast, even in scenarios dealing with billions of vectors.

## RAG architecture

At its core, a RAG architecture includes the **retriever** and the **generator**. Let’s start by understanding what each of these components does.

### The Retriever

When you ask a question to the retriever, it uses **similarity search** to scan through a vast knowledge base of vector embeddings. It then pulls out the most **relevant** vectors to help answer that query. There are a few different techniques it can use to know what’s relevant:

#### How indexing works in RAG retrievers

The indexing process organizes the data into your vector database in a way that makes it easily searchable. This allows the RAG to access relevant information when responding to a query.

https://qdrant.tech/articles_data/what-is-rag-in-ai/how-indexing-works.jpg

As shown in the image above, here’s the process:

- Start with a _loader_ that gathers _documents_ containing your data. These documents could be anything from articles and books to web pages and social media posts.
- Next, a _splitter_ divides the documents into smaller chunks, typically sentences or paragraphs.
- This is because RAG models work better with smaller pieces of text. In the diagram, these are _document snippets_.
- Each text chunk is then fed into an _embedding machine_. This machine uses complex algorithms to convert the text into [vector embeddings](https://qdrant.tech/articles/what-are-embeddings/).

All the generated vector embeddings are stored in a knowledge base of indexed information. This supports efficient retrieval of similar pieces of information when needed.

#### Query vectorization

Once you have vectorized your knowledge base you can do the same to the user query. When the model sees a new query, it uses the same preprocessing and embedding techniques. This ensures that the query vector is compatible with the document vectors in the index.

https://qdrant.tech/articles_data/what-is-rag-in-ai/how-retrieval-works.jpg

#### Retrieval of relevant documents

When the system needs to find the most relevant documents or passages to answer a query, it utilizes vector similarity techniques. **Vector similarity** is a fundamental concept in machine learning and natural language processing (NLP) that quantifies the resemblance between vectors, which are mathematical representations of data points.

The system can employ different vector similarity strategies depending on the type of vectors used to represent the data:

##### Sparse vector representations

A sparse vector is characterized by a high dimensionality, with most of its elements being zero.

The classic approach is **keyword search**, which scans documents for the exact words or phrases in the query. The search creates sparse vector representations of documents by counting word occurrences and inversely weighting common words. Queries with rarer words get prioritized.

https://qdrant.tech/articles_data/what-is-rag-in-ai/sparse-vectors.jpg

[TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (Term Frequency-Inverse Document Frequency) and [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) are two classic related algorithms. They’re simple and computationally efficient. However, they can struggle with synonyms and don’t always capture semantic similarities.

#### Dense vector embeddings

This approach uses large language models like [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29) to encode the query and passages into dense vector embeddings. These models are compact numerical representations that capture semantic meaning. Vector databases like Qdrant store these embeddings, allowing retrieval based on **semantic similarity** rather than just keywords using distance metrics like cosine similarity.

This allows the retriever to match based on semantic understanding rather than just keywords. So if I ask about “compounds that cause BO,” it can retrieve relevant info about “molecules that create body odor” even if those exact words weren’t used.

#### Hybrid search

However, neither keyword search nor vector search are always perfect. Keyword search may miss relevant information expressed differently, while vector search can sometimes struggle with specificity or neglect important statistical word patterns. Hybrid methods aim to combine the strengths of different techniques.

https://qdrant.tech/articles_data/what-is-rag-in-ai/hybrid-search.jpg

Some common hybrid approaches include:

- Using keyword search to get an initial set of candidate documents. Next, the documents are re-ranked/re-scored using semantic vector representations.
- Starting with semantic vectors to find generally topically relevant documents. Next, the documents are filtered/re-ranked e based on keyword matches or other metadata.
- Considering both semantic vector closeness and statistical keyword patterns/weights in a combined scoring model.
- Having multiple stages were different techniques. One example: start with an initial keyword retrieval, followed by semantic re-ranking, then a final re-ranking using even more complex models.

When you combine the powers of different search methods in a complementary way, you can provide higher quality, more comprehensive results.

### The Generator

With the top relevant passages retrieved, it’s now the generator’s job to produce a final answer by synthesizing and expressing that information in natural language.

The LLM is typically a model like GPT, BART or T5, trained on massive datasets to understand and generate human-like text. It now takes not only the query (or question) as input but also the relevant documents or passages that the retriever identified as potentially containing the answer to generate its response.

https://qdrant.tech/articles_data/what-is-rag-in-ai/how-generation-works.png

The retriever and generator don’t operate in isolation. The image below shows how the output of the retrieval feeds the generator to produce the final generated response.

https://qdrant.tech/articles_data/what-is-rag-in-ai/rag-system.jpg

## Where is RAG being used?

Because of their more knowledgeable and contextual responses, we can find RAG models being applied in many areas today, especially those who need factual accuracy and knowledge depth.

### Real-World Applications:

**Question answering:** This is perhaps the most prominent use case for RAG models. They power advanced question-answering systems that can retrieve relevant information from large knowledge bases and then generate fluent answers.

**Language generation:** RAG enables more factual and contextualized text generation for contextualized text summarization from multiple sources

**Data-to-text generation:** By retrieving relevant structured data, RAG models can generate product/business intelligence reports from databases or describing insights from data visualizations and charts

**Multimedia understanding:** RAG isn’t limited to text - it can retrieve multimodal information like images, video, and audio to enhance understanding. Answering questions about images/videos by retrieving relevant textual context.

## Creating your first RAG chatbot with Langchain, Groq, and OpenAI

Are you ready to create your own RAG chatbot from the ground up? We have a video explaining everything from the beginning. Daniel Romero’s will guide you through:

- Setting up your chatbot
- Preprocessing and organizing data for your chatbot’s use
- Applying vector similarity search algorithms
- Enhancing the efficiency and response quality

After building your RAG chatbot, you’ll be able to [evaluate its performance](https://qdrant.tech/rag/rag-evaluation-guide/) against that of a chatbot powered solely by a Large Language Model (LLM).

Chatbot with RAG, using LangChain, OpenAI, and Groq - YouTube

Tap to unmute

[Chatbot with RAG, using LangChain, OpenAI, and Groq](https://www.youtube.com/watch?v=O60-KuZZeQA) [Qdrant Vector Search](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA)

Qdrant Vector Search11.2K subscribers

[Watch on](https://www.youtube.com/watch?v=O60-KuZZeQA)

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

_No guideline code sources found._

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>A Complete Guide to RAG</summary>

# A Complete Guide to RAG

**Source URL:** <https://towardsai.net/p/l/a-complete-guide-to-rag>

If you haven’t heard about RAG from your refrigerator yet, you surely will very soon, so popular this technique has become. Surprisingly, there is a lack of complete guides that consider all the nuances (like relevance assessment, combating hallucinations, etc.), instead of just fragmented pieces. Based on our experience, I have compiled a guide that covers this topic thoroughly.

<Base64-Image-Removed>Image by DALL-E 3

**So, why do we need RAG?**

You could use LLM models like ChatGPT to create horoscopes (which it does quite successfully), or for something more practical (like work). However, there is a problem: companies typically have a multitude of documents, rules, regulations, etc., about which ChatGPT knows nothing, of course.

**What can be done?**

There are two options: retrain the model with your data or use RAG.

Retraining is long, expensive, and most likely **will not succeed** (don’t worry, it’s not because you’re a bad parent; it’s just that few people can and know how to do it).

The second option is **Retrieval-Augmented Generation** (also known as RAG). Essentially, the idea is simple: take a good existing model (like OpenAI’s), and attach a company information search to it. The model still knows little about your company, but now it has somewhere to look. While not as effective as if it knew everything, it’s sufficient for most tasks.

Here is a basic overview of the RAG structure:

https://miro.medium.com/v2/resize:fit:700/0*4FnEj61Crx9YA-dhRAG structure, image by the author

**The Retriever** is part of the system that searches for information relevant to your query (similarly to how you would search in your own wiki, company documents, or on Google). Typically, a vector database like Qdrant, where all the company’s indexed documents are stored, is used for this purpose, but essentially anything can be used.

**The Generator** receives the data found by the Retriever and uses it (combines, condenses, and extracts only the important information) to provide an answer to the user. This part is usually done using an LLM like OpenAI. It simply takes all (or part) of the found information and asks to make sense of it and provide an answer.

Here is an example of the simplest implementation of RAG in Python and LangChain.

```
import os
import wget
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain import OpenAI
from langchain_community.document_loaders import BSHTMLLoader
from langchain.chains import RetrievalQA

#download War and Peace by Tolstoy
wget.download("http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml")

#load text from html
loader = BSHTMLLoader("text_0073.shtml", open_encoding='ISO-8859-1')
war_and_peace = loader.load()

#init Vector DB
embeddings = OpenAIEmbeddings()

doc_store = Qdrant.from_documents(
 war_and_peace,
 embeddings,
 location=":memory:",
 collection_name="docs",
)

llm = OpenAI()
# ask questions

while True:
 question = input('Your question: ')
 qa = RetrievalQA.from_chain_type(
 llm=llm,
 chain_type="stuff",
 retriever=doc_store.as_retriever(),
 return_source_documents=False,
 )

 result = qa(question)
 print(f"Answer: {result}")
```

It sounds simple, but there’s a **nuance**:

Since the knowledge isn’t hardcoded into the model, the quality of the answers depends heavily on what the Retriever finds and in what form. It’s not a trivial task, as in the typical chaos of company documents, even people usually have a hard time understanding them. Documents and knowledge are generally stored in poorly structured forms, in different places, sometimes as images, charts, handwritten notes, etc. Often, information in one place contradicts information in another, and one has to make sense of all this mess.

Part of the information simply makes no sense without context, such as abbreviations, acronyms adopted by the company, and names and surnames.

What to do?

This is where various search optimizations (aka hacks) come into play. They are applied at different stages of the search. Broadly, the search can be divided into:

- Initial processing and cleaning of the user’s question
- Data searching in repositories
- Ranking of the results obtained from the repositories
- Processing and combining results into an answer
- Evaluating the response
- Applying formatting, stylistic, and tone

Let’s take a detailed look at each stage:

Initial processing of the user’s question

You wouldn’t believe what users write as questions. You can’t count on them being reasonable — the question could be phrased as a demand, statement, complaint, threat, just a single letter, or AN ENTIRE essay the size of “War and Peace.” For example:

https://miro.medium.com/v2/resize:fit:700/0*_zzJBaDyWGgpPL0gImage by the author

What “and”?

or

https://miro.medium.com/v2/resize:fit:700/0*__thyuBVknlrDrpBOnly some enraged Medium readers with their comments might match this. Image by the author

The input needs to be processed, turning it into a query that can be used to search for information. To solve this problem, we need a translator from the user language to the human language. Who could do this? Of course, an **LLM**. Basically, it might look like this:

https://miro.medium.com/v2/resize:fit:700/0*zrXahDMAXECjFNbgGood guess 😂 Image by the author

The simplest option — ask the LLM to reformulate the user’s request. But, depending on your audience, this might not be enough!!!!!1111

Then a slightly more complex technique comes into play — **RAG Fusion**.

**RAG Fusion**

The idea is to ask the LLM to provide several versions of the user’s question, conduct a search based on them, and then combine the results, having ranked them beforehand using some clever algorithm, such as a **Cross-Encoder**. Cross Encoder works quite slowly, but it provides more relevant results, so it’s not practical to use it for information retrieval — however, for ranking a list of found results, it’s quite suitable.

**Remarks about Cross and Bi Encoders**

Vector databases use **Bi-encoder** models to compute the similarity of two concepts in vector space. These models are trained to represent data in vector form and, accordingly, during a search, the user’s query is also turned into a vector, and vectors closest to the query are returned. However, this proximity does not guarantee that it is the best answer.

https://miro.medium.com/v2/resize:fit:700/0*N_wng9uYMv5zi3ge\* BERT stands for Bidirectional Encoder Representations from Transformers, a model based on transformers that encodes text into a vector (embedding). Image by the author

**Cross-Encoder** works differently. It takes two objects (texts, images, etc.) and returns their relevance (similarity) relative to each other. Its accuracy is usually [better](https://arxiv.org/abs/1908.10084) than that of a Bi-Encoder. Typically, more results than necessary are returned from the vector database (just in case, say 30) and then they are ranked using a Cross-Encoder or similar techniques, with the top 3 being returned.

https://miro.medium.com/v2/resize:fit:700/0*h98JJPZ-YSiOWwR1Cross-Encoder, image by the author

User request preprocessing also includes its classification. For example, requests can be subdivided into questions, complaints, requests, etc. Requests can further be classified as urgent, non-urgent, spam, or fraud. They can be classified by departments (e.g., accounting, production, HR), etc. All this helps narrow down the search for information and, consequently, increases the speed and quality of the response.

For classification, an LLM model or a specially trained neural network classifier can be used again.

**Data Search in Repositories**

The so-called **retriever**(the first letter in RAG) is responsible for the search.

Usually, a vector database serves as the repository where company data from various sources (document storage, databases, wikis, CRM, etc.) are indexed. However, it’s not mandatory and anything can be used, such as Elasticsearch or even Google search.

I will not discuss non-vector base searches here, as the principle is the same everywhere.

**Digression about Vector Databases**

A vector database (or vector storage. I use these terms interchangeably, although technically they are not the same) is a type of data storage optimized for storing and processing vectors (which are essentially arrays of numbers). These vectors are used to represent complex objects, such as images, texts, or sounds, as vectors in vector spaces for machine learning and data analysis tasks. In a vector database (or, more precisely, in vector space), concepts that are semantically similar are located close to each other, regardless of their representation. For example, the words “dog” and “bulldog” will be close, whereas the words “lock” (as in a door lock) and “lock” (as in a castle) will be far apart. Therefore, vector databases are well suited for semantic data search.

Most Popular Vector Databases (as of now):

- **QDrant**— open-source database
- **Pinecone**— cloud-native (i.e., they will charge you a lot) database
- **Chroma**— another open-source database (Apache-2.0 license)
- **Weaviate**— open under BSD-3-Clause license
- **Milvus**— open under Apache-2.0 license
- **FAISS**— a separate beast, not a database but a framework from Meta

Also, some popular non-vector databases have started offering vector capabilities:

- **Pgvector** for PostgreSQL
- **Atlas** for Mongo

To improve results, several main techniques are used:

**Ensemble of retrievers and/or data sources —** a simple but effective idea, which involves asking several experts the same question and then somehow aggregating their answers (even just averaging) — the result on average turns out better. In some sense, this is analogous to “Ask the Crowd.”

As an example — the use of multiple types of retrievers from [Langchain](https://python.langchain.com/docs/modules/data_connection/retrievers/). Ensembling is particularly useful when combining sparse retrievers (like [BM25](https://python.langchain.com/docs/integrations/retrievers/bm25)) and dense retrievers (working based on embedding similarities, such as the same [vector](https://python.langchain.com/docs/modules/data_connection/retrievers/vectorstore) databases) because they complement each other well.

**Dense Retriever** — typically uses transformers, such as BERT, to encode both queries and documents into vectors in a multidimensional space. The similarity between a query and a document is measured by the proximity of their vectors in this space, often using cosine similarity to assess their closeness. This is the basis on which vector databases are built. Such a model better understands the semantic (meaningful) value of queries and documents, leading to more accurate and relevant results, especially for complex queries. Because the model operates at the level of meaning (semantics), it handles paraphrasing and semantic similarities well.

**Sparse Retriever** — uses traditional information retrieval methods, such as TF-IDF (Term Frequency) or BM25. These methods create sparse vectors, where each dimension corresponds to a specific term from a predefined dictionary. The relevance of a document to a user’s query is calculated based on the presence and frequency of the terms (or words, let’s say) of the query in the document. It is effective for keyword-based queries and when the terms of the query are expected to be directly present in the relevant documents. They don’t always work as accurately as dense retrievers, but are faster and require fewer resources for searching and training.

The [EnsembleRetriever](https://python.langchain.com/docs/modules/data_connection/retrievers/ensemble) then ranks and combines results using, for example, [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf):

_Example of an ensemble:_

```
!pip install rank_bm25
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.vectorstores import Chroma

embedding = OpenAIEmbeddings()
documents = "/all_tolstoy_novels.txt"
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

vectorstore = Chroma.from_texts(doc_list, embedding)
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# initialize the ensemble retriever
ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, vectorstore_retriever ], weights=[0.4, 0.6])
docs = ensemble_retriever.get_relevant_documents("War and Peace")
```

How to choose the right strategy from all this zoo? Experiment. Or use a framework, for example, [https://github.com/Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG).

By the way, it’s also possible to ensemble several LLMs, which also improves the result. See “ [More agents is all you need](https://arxiv.org/abs/2402.05120).”

**RELP**

This is another method for data retrieval, Retrieval Augmented Language Model based Prediction. The distinction here is in the search step — after we find information in the vector storage, including using the techniques mentioned above, we use it not to generate an answer using an LLM but to generate example answers (via [few-shot prompting](https://en.wikipedia.org/wiki/Few-shot_learning)) for the LLM. Based on these examples, the LLM effectively learns and responds based on this mini-training to the posed question. This technique is a form of dynamic learning, which is much less costly than re-training the model using standard methods.

https://miro.medium.com/v2/resize:fit:451/0*0fpWX48eZ6Lw7nJRRELP flow, image by the author

**Remarks about few-shot (learning) prompting**

There are two similar LLM prompting techniques: zero-shot and few-shot. Zero-shot is when you ask your LLM a question without providing any examples. For instance:

https://miro.medium.com/v2/resize:fit:700/0*AlG7hPApACw63e2-Image by the author

**Few-shot** is when you first give the LLM several examples on which it trains. This significantly increases the likelihood of getting a relevant answer in the relevant form. For example:

https://miro.medium.com/v2/resize:fit:700/0*hyKm2xkJEW17gXDMImage by the author

As you can see, not everything is always obvious, and examples help to understand.

**Ranking, Combining, and Evaluating the Obtained Results**

We have already partially touched on this topic as part of RAG Fusion and the ensembling of retrievers. When we extract results from a (vector) storage, before sending this data to an LLM for answer generation, we need to rank the results, and possibly discard the irrelevant ones. The order in which you present the search results to the LLM for answer formulation matters. What the LLM sees first will have a stronger influence on the final outcome (more details here).

Different approaches are used for ranking. The most common include:

1. Using a **Cross-Encoder** (described above) for re-ranking the obtained results and discarding the least relevant (for example, pulling the top 30 results from a vector database (top k), ranking them with a Cross-Encoder, and taking the first 10).

There are already ready-made solutions for these purposes, for example from [Cohere](https://cohere.com/rerankhttps:/cohere.com/rerank).

[2\. Reciprocal Rank Fusion.](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) The main idea of RRF is to give greater importance to elements occupying higher positions in each set of search results. In RRF, the score of each element is calculated based on its position in the individual search results. This is usually done using the formula 1/(k + rank), where “rank” is the position of the element in a particular set of search results, and “k” is a constant (often set around 60). This formula provides a higher score for elements with a higher rank.

Scores for each element in different sets of results are then summed to obtain a final score. Elements are sorted by these final scores to form a combined list of results.

RRF is particularly useful because it does not depend on the absolute scores assigned by individual search systems, which can vary significantly in their scale and distribution. RRF effectively combines results from different systems in a way that highlights the most consistently highly ranked elements.

3\. LLM-based ranking and evaluation: you can relax and simply ask an LLM to rank and evaluate the result 🙂. The latest versions of OpenAI handle this quite well. However, using them for this purpose is costly.

**Evaluation of search results in the Vector Store:**

Suppose you have made reranking or other changes — how do you determine whether it was beneficial? Did the relevance increase or not? And in general, how well does the system work? This is a quality metric for the information found. It is used to understand how relevant the information your system finds is and to make decisions about further refinement.

You can assess how relevant the results are to the query using the following metrics: P@K, MAP@K, NDCG@K (and similar). These usually return a number from 0 to 1, where 1 is the highest accuracy. They are similar in meaning, with differences in details:

**P@K** means precision at K, i.e., accuracy for K elements. Suppose for a query about rabbits, the system found 4 documents:

_\[“Wild Rabbits”, “Task Rabbit: modern jobs platform”, “Treatise on Carrots”, “My Bunny: Memoirs by Walter Issac”\]_

Since Walter Issac's biography or jobs platforms have nothing to do with rabbits, these positions would be rated 0, and the overall accuracy would be calculated like this:

https://miro.medium.com/v2/resize:fit:700/0*fkdMKuqKYbn5odPjImage by the author

P@K at K=4, or P@4 = 2 relevant / (2 relevant + 2 irrelevant) = ½ = 0.5.

However, this does not take into account the order. What if the returned list looks like this:

_\[“Task Rabbit: modern jobs platform”, “My Bunny: Memoirs by Walter Issac”, “Wild Rabbits”, “Treatise on Carrots”\]_

P@K is still 0.5, but as we know, the order of relevant and irrelevant results matters! (both for people and for the LLM that will use them).

Therefore, we use **AP@K** or average precision at K. The idea is simple: we need to modify the formula so that the order is taken into account and relevant results at the end of the list do not increase the overall score less than those at the beginning of the list:

https://miro.medium.com/v2/resize:fit:700/0*kQLsLwQqidjxR6sAImage by the author

Or for our example above:

AP@4 = (0 \* 0 + 0 \*½ + 1 \* ⅓ + 1 + 1 \* 2/4) .2 = (⅓ + 2/4) / 2 = 0.41

Here are a few questions that arise: how did we assess the relevance of individual elements to calculate these metrics? This is a detective question, a very good one indeed.

In the context of RAG, we often ask an LLM or another model to make an assessment. That is, we query the LLM about each element — this document we found in the vector storage — is it relevant to this query at all?

Now, the second question: is it sufficient to ask just this way? The answer is no. We need more specific questions for the LLM that ask it to assess relevance according to certain parameters. For example, for the sample above, the questions might be:

Does this document relate to the animal type “rabbit”?

Is the rabbit in this document real or metaphorical?

Etc. There can be many questions (from two to hundreds), and they depend on how you assess relevance. This needs to be aggregated, and that’s where:

MAP@K (Mean Average Precision at K) comes in — it’s the average of the sum of AP@K for all questions.

NDCG@K stands for normalized discounted cumulative gain at K, and I won’t even translate that 🙂. Look it up online yourself.

**Evaluating the results of the LLM response**

Not everyone knows this, but you can ask an LLM (including Llama and OpenAI) not just to return tokens (text) but logits. That is, you can actually ask it to return a distribution of tokens with their probabilities, and see — how confident is the model really in what it has concocted (calculating token-level uncertainty)? If the probabilities in the distribution are low (what is considered low depends on the task), then most likely, the model has started to fabricate (hallucinate) and is not at all confident in its response. This can be used to evaluate the response and to return an honest “I don’t know” to the user.

**Using formatting, style, and tone**

The easiest item 🙂. Just ask the LLM to format the answer in a certain way and use a specific tone. It’s better to give the model an example, as it then follows instructions better. For instance, you could set the tone like this:

https://miro.medium.com/v2/resize:fit:700/0*lsnHytCsXujPJZrvImage by the author

Formatting and stylistics can be programmatically set in the last step of RAG — requesting the LLM to generate the final answer, for example:

```
question = input('Your question: ')
style = 'Users have become very very impudent lately. Answer as a gangster from a ghetto'
qa = RetrievalQA.from_chain_type(
 llm=llm,
 chain_type="stuff",
 retriever=doc_store.as_retriever()
)

result = qa(style + " user question: " + question)
print(f"Answer: {result}")
```

## Fine-tuning models

Sometimes you might indeed need further training. Yes, initially I said that most likely you won’t succeed, but there are cases when it is justified. If your company uses acronyms, names/surnames, and terms that the model does not and cannot know about, RAG may perform poorly. For example, it might struggle with searching data by Russian surnames, especially their declensions. Here, a light fine-tuning of the model using [LORA](https://arxiv.org/abs/2106.09685) can help, to train the model to understand such specific cases. You can use frameworks like [https://github.com/bclavie/RAGatouille](https://github.com/bclavie/RAGatouille).

Such fine-tuning is beyond the scope of this article, but if there is interest, I will describe it separately.

**Systems based on RAG**

There are several more advanced options based on RAG. In fact, new variants are emerging almost every day, and their creators claim that they have become increasingly better…

Nevertheless, one variation stands out — [FLARE](https://arxiv.org/abs/2305.06983)(Forward Looking Active REtrieval Augmented Generation).

It’s a very interesting idea based on the principle that RAG should not be used haphazardly but only when the LLM itself wants to. If the LLM confidently answers without RAG, then please proceed. However, if it starts to doubt, that’s when more contextual data needs to be searched for. This should not be done just once but as many times as necessary. When, during the response process, the LLM feels it needs more data, it performs a RAG search.

In some ways, this is similar to how people operate. We often do not know what we do not know and realize it only during the search process itself.

I will not go into details here; that is a topic for another article.

## Summary

In this article, I’ve provided a comprehensive guide to Retrieval-Augmented Generation (RAG). Here’s a quick recap of our journey:

**Need and Advantages:** I started by discussing why RAG is needed and its benefits over retraining models with custom data.

**RAG Structure:** Then, I explained the basic structure of RAG, highlighting the roles of the Retriever and Generator components.

**Implementation:** I walked through an example implementation using Python and LangСhain.

**User Query Processing:** I delved into processing user queries, including RAG Fusion and Cross-Encoders.

**Data Search Techniques:** Next, I explored various data search techniques, such as vector databases and ensembling retrievers.

**Ranking and Evaluating:** I covered the importance of ranking, combining, and evaluating retrieved results to improve response quality.

**Advanced Methods:** Finally, I discussed optimizations and advanced methods like RELP and FLARE, as well as considerations for fine-tuning models and maintaining response formatting, style, and tone.

</details>

<details>
<summary>Your RAG Is Wrong, Here's How To Fix It</summary>

# Your RAG Is Wrong, Here's How To Fix It
**Source URL:** <https://decodingml.substack.com/p/your-rag-is-wrong-heres-how-to-fix?utm_source=publication-search>

The vanilla RAG framework doesn’t address many fundamental aspects that impact the quality of the retrieval and answer generation, such as:

- Are the retrieved documents relevant to the user’s question?
- Is the retrieved context enough to answer the user’s question?
- Is there any redundant information that only adds noise to the augmented prompt?
- Does the latency of the retrieval step match our requirements?
- What do we do if we can’t generate a valid answer using the retrieved information?

From the questions above, we can draw two conclusions.

**The first one** is that we need a robust evaluation module for our RAG system that can quantify and measure the quality of the retrieved data and generate answers relative to the user’s question.

**The second conclusion** is that we must improve our RAG framework to address the retrieval limitations directly in the algorithm. These improvements are known as advanced RAG.

This article will focus on the second conclusion, answering the question: _“How can I optimize an RAG system?”_.

[https://substackcdn.com/image/fetch/$s_!yOzH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19d2780b-7e3f-48aa-8e67-c4107ef8f0c7_792x792.png](https://substackcdn.com/image/fetch/$s_!yOzH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19d2780b-7e3f-48aa-8e67-c4107ef8f0c7_792x792.png) Figure 1: The three stages of advanced RAG

The vanilla RAG design can be **optimized** **at** **three different stages**:

1. **Pre-retrieval:** This stage focuses on structuring and preprocessing your data for data indexing and query optimizations.
2. **Retrieval:** This stage revolves around improving the embedding models and metadata filtering to improve the vector search step.
3. **Post-retrieval:** This stage mainly targets different ways to filter out noise from the retrieved documents and compress the prompt before feeding it to an LLM for answer generation.

* * *

## 1. Pre-retrieval

The pre-retrieval steps are performed in two different ways:

- **Data indexing:** It is part of the RAG ingestion pipeline. It is mainly implemented within the cleaning or chunking modules to preprocess the data for better indexing.
- **Query optimization:** The algorithm is performed directly on the user’s query before embedding it and retrieving the chunks from the vector DB.

As we index our data using embeddings that semantically represent the content of a chunked document, most of the data indexing techniques focus on better preprocessing and structuring the data to improve retrieval efficiency.

Here are a few popular methods for **optimizing data indexing**.

#### 1. Sliding window

The sliding window technique introduces overlap between text chunks, ensuring that important context near chunk boundaries is retained, which enhances retrieval accuracy.

This is particularly beneficial in domains like legal documents, scientific papers, customer support logs, and medical records, where critical information often spans multiple sections.

The embedding is computed on the chunk along with the overlapping portion. Hence, the sliding window improves the system’s ability to retrieve relevant and coherent information by maintaining context across boundaries.

#### 2. Enhancing data granularity

This involves data cleaning techniques like removing irrelevant details, verifying factual accuracy, and updating outdated information. A clean and accurate dataset allows for sharper retrieval.

#### 3. Metadata

Adding metadata tags like dates, URLs, external IDs, or chapter markers helps filter results efficiently during retrieval.

#### 4. Optimizing index structures

It is based on different data index methods, such as various chunk sizes and multi-indexing strategies.

#### 5. Small-to-big

The algorithm decouples the chunks used for retrieval and the context used in the prompt for the final answer generation.

The algorithm uses a small sequence of text to compute the embedding while preserving the sequence itself and a wider window around it in the metadata. Thus, using smaller chunks enhances the retrieval’s accuracy, while the larger context adds more contextual information to the LLM.

The intuition behind this is that if we use the whole text for computing the embedding, we might introduce too much noise, or the text could contain multiple topics, which results in a poor overall semantic representation of the embedding.

**On the** **query optimization side**, we can leverage techniques such as query routing, query rewriting, and query expansion to refine the retrieved information for the LLM further.

#### 1. Query routing

Based on the user’s input, we might have to interact with different categories of data and query each category differently.

Query rooting is used to decide what action to take based on the user’s input, similar to if/else statements. Still, the decisions are made solely using natural language instead of logical statements.

As illustrated in Figure 2, let’s assume that, based on the user’s input, to do RAG, we can retrieve additional context from a vector DB using vector search queries, a standard SQL DB by translating the user query to an SQL command, or the internet by leveraging REST API calls.

The query router can also detect whether a context is required, helping us avoid making redundant calls to external data storage. Also, a query router can pick the best prompt template for a given input.

The routing usually uses an LLM to decide what route to take or embeddings by picking the path with the most similar vectors.

To summarize, query routing is identical to an if/else statement but much more versatile as it works directly with natural language.

[https://substackcdn.com/image/fetch/$s_!SdZP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab3d3265-49a9-4bd6-a61a-7a3bf019ef25_792x792.png](https://substackcdn.com/image/fetch/$s_!SdZP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab3d3265-49a9-4bd6-a61a-7a3bf019ef25_792x792.png) Figure 2: Query routing

#### 2. Query rewriting

Sometimes, the user’s initial query might not perfectly align with how your data is structured. Query rewriting tackles this by reformulating the question to match the indexed information better.

This can involve techniques like:

- **Paraphrasing:** Rephrasing the user’s query while preserving its meaning (e.g., “What are the causes of climate change?” could be rewritten as “Factors contributing to global warming”).
- **Synonym substitution:** Replacing less common words with synonyms to broaden the search scope (e.g., “ joyful” could be rewritten as “happy”).
- **Sub-queries:** For longer queries, we can break them down into multiple shorter and more focused sub-queries. This can help the retrieval stage identify relevant documents more precisely.

#### 3. Hypothetical document embeddings (HyDE)

This technique involves having an LLM create a hypothetical response to the query. Then, both the original query and the LLM’s response are fed into the retrieval stage.

#### 4. Query expansion

This approach aims to enrich the user’s question by adding additional terms or concepts, resulting in different perspectives of the same initial question. For example, when searching for “disease,” you can leverage synonyms and related terms associated with the original query words and also include “illnesses” or “ailments.”

#### 5. Self-query

The core idea is to map unstructured queries into structured ones. An LLM identifies key entities, events, and relationships within the input text. These identities are used as filtering parameters to reduce the vector search space (e.g., identify cities within the query, for example, “Paris,” and add it to your filter to reduce your vector search space).

Both data indexing and query optimization pre-retrieval optimization techniques depend highly on your data type, structure, and source. Thus, as with any data processing pipeline, no method always works, as every use case has its own particularities and gotchas.

Optimizing your pre-retrieval RAG layer is experimental. Thus, what is essential is to try multiple methods (such as the ones enumerated in this section), reiterate, and observe what works best.

## 2. Retrieval

The retrieval step can be optimized in two fundamental ways:

- Improving the embedding models used in the RAG ingestion pipeline to encode the chunked documents and, at inference time, transform the user’s input.
- Leveraging the DB’s filter and search features. This step will be used solely at inference time when you have to retrieve the most similar chunks based on user input.

Both strategies are aligned with our ultimate goal: to enhance the vector search step by leveraging the semantic similarity between the query and the indexed data.

When improving the **embedding models**, you usually have to fine-tune the pre-trained embedding models to tailor them to specific jargon and nuances of your domain, especially for areas with evolving terminology or rare terms.

Instead of fine-tuning the embedding model, you can leverage instructor models, such as **[instructor-xl](https://huggingface.co/hkunlp/instructor-xl)**, to guide the embedding generation process with an instruction/prompt aimed at your domain. Tailoring your embedding network to your data using such a model can be a good option, as fine-tuning a model consumes more computing and human resources.

In the code snippet below, you can see an example of an Instructor model that embeds article titles about AI:

```
from InstructorEmbedding import INSTRUCTOR

model = INSTRUCTOR(“hkunlp/instructor-base”)

sentence = “RAG Fundamentals First”

instruction = “Represent the title of an article about AI:”

embeddings = model.encode([[instruction, sentence]])

print(embeddings.shape) # noqa

# Output: (1, 768)
```

On the other side of the spectrum, here is how you can **improve your retrieval** by leveraging classic filter and search DB features.

#### **Hybrid search**

This is a vector and keyword-based search blend.

Keyword-based search excels at identifying documents containing specific keywords. When your task demands pinpoint accuracy, and the retrieved information must include exact keyword matches, hybrid search shines. Vector search, while powerful, can sometimes struggle with finding exact matches, but it excels at finding more general semantic similarities.

You leverage both keyword matching and semantic similarities by combining the two methods. You have a parameter, usually called alpha, that controls the weight between the two methods. The algorithm has two independent searches, which are later normalized and unified.

#### Filtered vector search

This type of search leverages the metadata index to filter for specific keywords within the metadata. It differs from a hybrid search in that you retrieve the data once using only the vector index and perform the filtering step before or after the vector search to reduce your search space.

In practice, you usually start with filtered vector or hybrid search on the retrieval side, as they are fairly quick to implement. This approach gives you the flexibility to adjust your strategy based on performance.

If the results are unexpected, you can always fine-tune your embedding model.

## 3. Post-retrieval

The post-retrieval optimizations are solely performed on the retrieved data to ensure that the LLM’s performance is not compromised by issues such as limited context windows or noisy data.

This is because the retrieved context can sometimes be too large or contain irrelevant information, both of which can distract the LLM.

Two popular methods performed at the post-retrieval step are the following.

#### **Prompt compression**

Eliminate unnecessary details while keeping the essence of the data.

#### Re-ranking

Use a cross-encoder ML model to give a matching score between the user’s input and every retrieved chunk.

[https://substackcdn.com/image/fetch/$s_!RjK7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff797810-7274-4a51-b487-ee06e881efe6_792x792.png](https://substackcdn.com/image/fetch/$s_!RjK7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff797810-7274-4a51-b487-ee06e881efe6_792x792.png) Figure 3: Bi-encoder (the standard embedding model) versus cross-encoder

The retrieved items are sorted based on this score. Only the top N results are kept as the most relevant. As you can see in Figure 3, this works because the re-ranking model can find more complex relationships between the user input and some content than a simple similarity search.

However, we can’t apply this model at the initial retrieval step because it is costly. That is why a popular strategy is to retrieve the data using a similarity distance between the embeddings and refine the retrieved information using a re-raking model, as illustrated in Figure 4.

[https://substackcdn.com/image/fetch/$s_!2OdZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33ab6874-b3ea-4cd4-9a66-9665afe27de5_792x792.png](https://substackcdn.com/image/fetch/$s_!2OdZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33ab6874-b3ea-4cd4-9a66-9665afe27de5_792x792.png) Figure 4: The re-ranking algorithm

* * *

## Conclusion

The abovementioned techniques are far from an exhaustive list of all potential solutions. We used them as examples to get an intuition on what you can (and should) optimize at each step in your RAG workflow.

The truth is that these techniques can vary tremendously by the type of data you work with. For example, if you work with multi-modal data such as text and images, most of the techniques from earlier won’t work as they are designed for text only.

To summarize, the primary goal of these optimizations is to enhance the RAG algorithm at three key stages: pre-retrieval, retrieval, and post-retrieval.

This involves preprocessing data for improved vector indexing, adjusting user queries for more accurate searches, enhancing the embedding model, utilizing classic filtering DB operations, and removing noisy data.

By keeping these goals in mind, you can optimize your RAG workflow for data processing and retrieval.

</details>

<details>
<summary>From Local to Global: A GraphRAG Approach to Query-Focused Summarization</summary>

# From Local to Global: A GraphRAG Approach to Query-Focused Summarization

**Source URL:** <https://arxiv.org/html/2404.16130>

## Abstract

The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections.
However, RAG fails on global questions directed at an entire text corpus, such as "*What are the main themes in the dataset?*", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task.
Prior QFS methods, meanwhile, do not scale to the quantities of text indexed by typical RAG systems.
To combine the strengths of these contrasting methods, we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text.
Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities.
Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user.
For a class of global sensemaking questions over datasets in the 1 million token range, we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers.

## 1 Introduction

Retrieval augmented generation (RAG) is an established approach to using LLMs to answer queries based on data that is too large to contain in a language model’s *context window*, meaning the maximum number of *tokens* (units of text) that can be processed by the LLM at once.
In the canonical RAG setup, the system has access to a large external corpus of text records and retrieves a subset of records that are individually relevant to the query and collectively small enough to fit into the context window of the LLM. The LLM then generates a response based on both the query and the retrieved records.
This conventional approach, which we collectively call *vector RAG*, works well for queries that can be answered with information localized within a small set of records.
However, vector RAG approaches do not support sensemaking queries, meaning queries that require global understanding of the entire dataset, such as "*What are the key trends in how scientific discoveries are influenced by interdisciplinary research over the past decade?*"

Sensemaking tasks require reasoning over "*connections (which can be among people, places, and events) in order to anticipate their trajectories and act effectively*".
LLMs such as GPT, Llama, and Gemini excel at sensemaking in complex domains like scientific discovery and intelligence analysis.
Given a sensemaking query and a text with an implicit and interconnected set of concepts, an LLM can generate a summary that answers the query.
The challenge, however, arises when the volume of data requires a RAG approach, since vector RAG approaches are unable to support sensemaking over an entire corpus.

In this paper, we present GraphRAG – a graph-based RAG approach that enables sensemaking over the entirety of a large text corpus.
GraphRAG first uses an LLM to construct a knowledge graph, where nodes correspond to key entities in the corpus and edges represent relationships between those entities.
Next, it partitions the graph into a hierarchy of communities of closely related entities, before using an LLM to generate community-level summaries. These summaries are generated in a bottom-up manner following the hierarchical structure of extracted communities, with summaries at higher levels of the hierarchy recursively incorporating lower-level summaries.
Together, these community summaries provide global descriptions and insights over the corpus.
Finally, GraphRAG answers queries through map-reduce processing of community summaries; in the map step, the summaries are used to provide partial answers to the query independently and in parallel, then in the reduce step, the partial answers are combined and used to generate a final global answer.

The GraphRAG method and its ability to perform global sensemaking over an entire corpus form the main contribution of this work. To demonstrate this ability, we developed a novel application of the *LLM-as-a-judge technique* suitable for questions targeting broad issues and themes where there is no ground-truth answer.
This approach first uses one LLM to generate a diverse set of global sensemaking questions based on corpus-specific use cases, before using a second LLM to judge the answers of two different RAG systems using predefined criteria (defined in Section 3.3).
We use this approach to compare GraphRAG to vector RAG on two representative real-world text datasets.
Results show GraphRAG strongly outperforms vector RAG when using GPT-4 as the LLM.

GraphRAG is available as open-source software at [https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag).
In addition, versions of the GraphRAG approach are also available as extensions to multiple open-source libraries, including LangChain, LlamaIndex, NebulaGraph, and Neo4J.

## 2 Background

### 2.1 RAG Approaches and Systems

RAG generally refers to any system where a user query is used to retrieve relevant information from external data sources, whereupon this information is incorporated into the generation of a response to the query by an LLM (or other generative AI model, such as a multi-media model).
The query and retrieved records populate a prompt template, which is then passed to the LLM.
RAG is ideal when the total number of records in a data source is too large to include in a single prompt to the LLM, i.e. the amount of text in the data source exceeds the LLM’s context window.

In canonical RAG approaches, the retrieval process returns a set number of records that are semantically similar to the query and the generated answer uses only the information in those retrieved records.
A common approach to conventional RAG is to use text embeddings, retrieving records closest to the query in vector space where closeness corresponds to semantic similarity.
While some RAG approaches may use alternative retrieval mechanisms, we collectively refer to the family of conventional approaches as *vector RAG*.
GraphRAG contrasts with vector RAG in its ability to answer queries that require global sensemaking over the entire data corpus.

GraphRAG builds upon prior work on advanced RAG strategies.
GraphRAG leverages summaries over large sections of the data source as a form of "self-memory" (described in), which are later used to answer queries as in. These summaries are generated in parallel and iteratively aggregated into global summaries, similar to prior techniques.
In particular, GraphRAG is similar to other approaches that use hierarchical indexing to create summaries (similar to).
GraphRAG contrasts with these approaches by generating a graph index from the source data, then applying graph-based community detection to create a thematic partitioning of the data.

### 2.2 Using Knowledge Graphs with LLMs and RAG

Approaches to knowledge graph extraction from natural language text corpora include rule-matching, statistical pattern recognition, clustering, and embeddings.
GraphRAG falls into a more recent body of research that use of LLMs for knowledge graph extraction.
It also adds to a growing body of RAG approaches that use a knowledge graph as an index.
Some techniques use subgraphs, elements of the graph, or properties of the graph structure directly in the prompt or as factual grounding for generated outputs.
Other techniques use the knowledge graph to enhance retrieval, where at query time an LLM-based agent dynamically traverses a graph with nodes representing document elements (e.g., passages, tables) and edges encoding lexical and semantical similarity or structural relationships.
GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent *modularity* and the ability to partition graphs into nested modular communities of closely related nodes (e.g., Louvain; Leiden).
Specifically, GraphRAG recursively creates increasingly global summaries by using the LLM to create summaries spanning this community hierarchy.

### 2.3 Adaptive Benchmarking for RAG Evaluation

Many benchmark datasets for open-domain question answering exist, including HotPotQA, MultiHop-RAG, and MT-Bench.
However, these benchmarks are oriented towards vector RAG performance, i.e., they evaluate performance on explicit fact retrieval.
In this work, we propose an approach for generating a set of questions for evaluating global sensemaking over the entirety of the corpus.
Our approach is related to LLM methods that use a corpus to generate questions whose answers would be summaries of the corpus, such as in.
However, in order to produce a fair evaluation, our method avoids generating the questions directly from the corpus itself (as an alternative implementation, one can use a subset of the corpus held out from subsequent graph extraction and answer evaluation steps).

*Adaptive benchmarking* refers to the process of dynamically generating evaluation benchmarks tailored to specific domains or use cases.
Recent work has used LLMs for adaptive benchmarking to ensure relevance, diversity, and alignment with the target application or task.
In this work, we propose an adaptive benchmarking approach to generating global sensemaking queries for the LLM.
Our approach builds on prior work in LLM-based persona generation, where the LLM is used to generate diverse and authentic sets of personas.
Our adaptive benchmarking procedure uses persona generation to create queries that are representative of real-world RAG system usage.
Specifically, our approach uses the LLM to infer the potential users would use the RAG system and their use cases, which guide the generation of corpus-specific sensemaking queries.

### 2.4 RAG Evaluation Criteria

Our evaluation relies on the LLM to evaluate how well the RAG system answers the generated questions.
Prior work has shown LLMs to be good evaluators of natural language generation, including work where LLMs evaluations were competitive with human evaluations.
Some prior work proposes criteria for having LLMs quantify the quality of generated texts such as “fluency”
Some of these criteria are generic to vector RAG systems and not relevant to global sensemaking, such as “context relevance”, “faithfulness”, and “answer relevance” (RAGAS,).
Lacking a gold standard for evaluation, one can quantify relative performance for a given criterion by prompting the LLM to compare generations from two different competing models (*LLM-as-a-judge*,).
In this work, we design criteria for evaluating RAG-generated answers to global sensemaking questions and evaluate our results using the comparative approach.
We also validate results using statistics derived from LLM-extracted statements of verifiable facts, or “claims.”

## 3 Methods

### 3.1 GraphRAG Workflow

Figure 1 illustrates the high-level data flow of the GraphRAG approach and pipeline.
In this section, we describe the key design parameters, techniques, and implementation details for each step.

Figure: Figure 1: Graph RAG pipeline using an LLM-derived graph index of source document text. This graph index spans nodes (e.g., entities), edges (e.g., relationships), and covariates (e.g., claims) that have been detected, extracted, and summarized by LLM prompts tailored to the domain of the dataset. Community detection (e.g., Leiden,) is used to partition the graph index into groups of elements (nodes, edges, covariates) that the LLM can summarize in parallel at both indexing time and query time. The “global answer” to a given query is produced using a final round of query-focused summarization over all community summaries reporting relevance to that query.

#### 3.1.1 Source Documents $\rightarrow$ Text Chunks

To start, the documents in the corpus are split into text chunks.
The LLM extracts information from each chunk for downstream processing.
Selecting the size of the chunk is a fundamental design decision; longer text chunks require fewer LLM calls for such extraction (which reduces cost) but suffer from degraded recall of information that appears early in the chunk.
See Section A.1 for prompts and examples of the recall-precision trade-offs.

#### 3.1.2 Text Chunks $\rightarrow$ Entities & Relationships

In this step, the LLM is prompted to extract instances of important *entities* and the *relationships* between the entities from a given chunk.
Additionally, the LLM generates short descriptions for the entities and relationships. To illustrate, suppose a chunk contained the following text:

> NeoChip’s (NC) shares surged in their first week of trading on the NewTech Exchange. However, market analysts caution that the chipmaker’s public debut may not reflect trends for other technology IPOs. NeoChip, previously a private entity, was acquired by Quantum Systems in 2016. The innovative semiconductor firm specializes in low-power processors for wearables and IoT devices.

The LLM is prompted such that it extracts the following:

- The entity NeoChip, with description “NeoChip is a publicly traded company specializing in low-power processors for wearables and IoT devices.”
- The entity Quantum Systems, with description “Quantum Systems is a firm that previously owned NeoChip.”
- A relationship between NeoChip and Quantum Systems, with description “Quantum Systems owned NeoChip from 2016 until NeoChip became publicly traded.”

These prompts can be tailored to the domain of the document corpus by choosing domain appropriate few-shot exemplars for *in-context learning*.
For example, while our default prompt extracts the broad class of “named entities” like people, places, and organizations and is generally applicable, domains with specialized knowledge (e.g., science, medicine, law) will benefit from few-shot exemplars specialized to those domains.

The LLM can also be prompted to extract *claims* about detected entities.
*Claims* are important factual statements about entities, such as dates, events, and interactions with other entities.
As with entities and relationships, in-context learning exemplars can provide domain-specific guidance. Claim descriptions extracted from the example tetx chunk are as follows:

- NeoChip’s shares surged during their first week of trading on the NewTech Exchange.
- NeoChip debuted as a publicly listed company on the NewTech Exchange.
- Quantum Systems acquired NeoChip in 2016 and held ownership until NeoChip went public.

See Appendix A for prompts and details on our implementation of entity and claim extraction.

#### 3.1.3 Entities & Relationships $\rightarrow$ Knowledge Graph

The use of an LLM to extract entities, relationships, and claims is a form of abstractive summarization – these are meaningful summaries of concepts that, in the case of relationships and claims, may not be explicitly stated in the text.
The entity/relationship/claim extraction processes creates multiple instances of a single element because an element is typically detected and extracted multiple times across documents.

In the final step of the knowledge graph extraction process, these instances of entities and relationships become individual nodes and edges in the graph.
Entity descriptions are aggregated and summarized for each node and edge.
Relationships are aggregated into graph edges, where the number of duplicates for a given relationship becomes edge weights.
Claims are aggregated similarly.

In this manuscript, our analysis uses exact string matching for *entity matching* – the task of reconciling different extracted names for the same entity.
However, softer matching approaches can be used with minor adjustments to prompts or code.
Furthermore, GraphRAG is generally resilient to duplicate entities since duplicates are typically clustered together for summarization in subsequent steps.

#### 3.1.4 Knowledge Graph $\rightarrow$ Graph Communities

Given the graph index created in the previous step, a variety of community detection algorithms may be used to partition the graph into communities of strongly connected nodes (e.g., see the surveys by and).
In our pipeline, we use Leiden community detection in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned.

Each level of this hierarchy provides a community partition that covers the nodes of the graph in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization.
An illustration of such hierarchical partitioning on an example dataset can be found in Appendix B.

#### 3.1.5 Graph Communities $\rightarrow$ Community Summaries

The next step creates report-like summaries of each community in the community hierarchy, using a method designed to scale to very large datasets.
These summaries are independently useful as a way to understand the global structure and semantics of the dataset, and may themselves be used to make sense of a corpus in the absence of a specific query.
For example, a user may scan through community summaries at one level looking for general themes of interest, then read linked reports at a lower level that provide additional details for each subtopic.
Here, however, we focus on their utility as part of a graph-based index used for answering global queries.

GraphRAG generates community summaries by adding various element summaries (for nodes, edges, and related claims) to a community summary template.
Community summaries from lower-level communities are used to generate summaries for higher-level communities as follows:

- *Leaf-level communities*. The element summaries of a leaf-level community are prioritized and then iteratively added to the LLM context window until the token limit is reached.
The prioritization is as follows: for each community edge in decreasing order of combined source and target node degree (i.e., overall prominence), add descriptions of the source node, target node, the edge itself, and related claims.
- *Higher-level communities*. If all element summaries fit within the token limit of the context window, proceed as for leaf-level communities and summarize all element summaries within the community.
Otherwise, rank sub-communities in decreasing order of element summary tokens and iteratively substitute sub-community summaries (shorter) for their associated element summaries (longer) until they fit within the context window.

#### 3.1.6 Community Summaries $\rightarrow$ Community Answers $\rightarrow$ Global Answer

Given a user query, the community summaries generated in the previous step can be used to generate a final answer in a multi-stage process.
The hierarchical nature of the community structure also means that questions can be answered using the community summaries from different levels, raising the question of whether a particular level in the hierarchical community structure offers the best balance of summary detail and scope for general sensemaking questions (evaluated in section 4).

For a given community level, the global answer to any user query is generated as follows:

- *Prepare community summaries*. Community summaries are randomly shuffled and divided into chunks of pre-specified token size. This ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window.
- *Map community answers*. Intermediate answers are generated in parallel. The LLM is also asked to generate a score between 0-100 indicating how helpful the generated answer is in answering the target question. Answers with score 0 are filtered out.
- *Reduce to global answer*. Intermediate community answers are sorted in descending order of helpfulness score and iteratively added into a new context window until the token limit is reached. This final context is used to generate the global answer returned to the user.

### 3.2 Global Sensemaking Question Generation

To evaluate the effectiveness of RAG systems for global sensemaking tasks, we use an LLM to generate a set of corpus-specific questions designed to asses high-level understanding of a given corpus, without requiring retrieval of specific low-level facts.
Instead, given a high-level description of a corpus and its purposes, the LLM is prompted to generate personas of hypothetical users of the RAG system.
For each hypothetical user, the LLM is then prompted to specify tasks that this user would use the RAG system to complete.
Finally, for each combination of user and task, the LLM is prompted to generate questions that require understanding of the entire corpus. Algorithm 1 describes the approach.

**Algorithm 1: Prompting Procedure for Question Generation**

1.  Describe personas of $K$ potential users of the dataset.
2.  For each user, identify $N$ tasks relevant to the user.
3.  Specific to each user & task pair, generate $M$ high-level questions that:
    - Require understanding of the entire corpus.
    - Do not require retrieval of specific low-level facts.

For our evaluation, we set $K=M=N=5$ for a total of 125 test questions per dataset.
Table 1 shows example questions for each of the two evaluation datasets.

**Table 1: Examples of potential users, tasks, and questions generated by the LLM based on short descriptions of the target datasets. Questions target global understanding rather than specific details.**
| Dataset | Example activity framing and generation of global sensemaking questions |
|---|---|
| Podcast transcripts | *User*:<br>A tech journalist looking for insights and trends in the tech industry<br>*Task*:<br>Understanding how tech leaders view the role of policy and regulation<br>*Questions*:<br>1. Which episodes deal primarily with tech policy and government regulation?<br>2. How do guests perceive the impact of privacy laws on technology development?<br>3. Do any guests discuss the balance between innovation and ethical considerations?<br>4. What are the suggested changes to current policies mentioned by the guests?<br>5. Are collaborations between tech companies and governments discussed and how? |
| News articles | *User*:<br>Educator incorporating current affairs into curricula<br>*Task*:<br>Teaching about health and wellness<br>*Questions*:<br>1. What current topics in health can be integrated into health education curricula?<br>2. How do news articles address the concepts of preventive medicine and wellness?<br>3. Are there examples of health articles that contradict each other, and if so, why?<br>4. What insights can be gleaned about public health priorities based on news coverage?<br>5. How can educators use the dataset to highlight the importance of health literacy? |

### 3.3 Criteria for Evaluating Global Sensemaking

Given the lack of gold standard answers to our activity-based sensemaking questions, we adopt the head-to-head comparison approach using an LLM evaluator that judges relative performance according to specific criteria.
We designed three target criteria capturing qualities that are desirable for global sensemaking activities.

Appendix F shows the prompts for our head-to-head measures computed using an LLM evaluator, summarized as:

- *Comprehensiveness*. How much detail does the answer provide to cover all aspects and details of the question?
- *Diversity*. How varied and rich is the answer in providing different perspectives and insights on the question?
- *Empowerment*. How well does the answer help the reader understand and make informed judgments about the topic?

Furthermore, we use a “control criterion” called *Directness* that answers "*How specifically and clearly does the answer address the question?*".
In plain terms, directness evaluates the concision of an answer in a generic sense that applies to any generated LLM summarization.
We include it to behave as a reference against which we can judge the soundness of results for the other criteria.
Since directness is effectively in opposition to comprehensiveness and diversity, we would not expect any method to win across all four criteria.

In our evaluations, the LLM is provided with the question, the generated answers from two competing systems, and prompted to compare the two answers according to the criterion before giving a final judgment of which answer is preferred.
The LLM either indicates a winner; or, it returns a tie if they are fundamentally similar.
To account for the inherent stochasticity of LLM generation, we run each comparison with multiple replicates and average the results across replicates and questions.
An illustration of LLM assessment for answers to a sample question can be found in Appendix D.

## 4 Analysis

### 4.1 Experiment 1

#### 4.1.1 Datasets

We selected two datasets in the one million token range, each representative of corpora that users may encounter in their real-world activities:

**Podcast transcripts.** Public transcripts of *Behind the Tech with Kevin Scott*, a podcast featuring conversations between Microsoft CTO Kevin Scott and various thought leaders in science and technology.
This corpus was divided into $1669 \times 600$-token text chunks, with 100-token overlaps between chunks ($\sim$1 million tokens).

**News articles.** A benchmark dataset comprised of news articles published from September 2013 to December 2023 in a range of categories, including entertainment, business, sports, technology, health, and science.
The corpus is divided into $3197 \times 600$-token text chunks, with 100-token overlaps between chunks ($\sim$1.7 million tokens).

#### 4.1.2 Conditions

We compared six conditions including GraphRAG at four different graph community levels (C0, C1, C2, C3), a text summarization method that applies our map-reduce approach directly to source texts (TS), and a vector RAG “semantic search” approach (SS):

- **C0.** Uses root-level community summaries (fewest in number) to answer user queries.
- **C1.** Uses high-level community summaries to answer queries. These are sub-communities of C0, if present, otherwise C0 communities projected downwards.
- **C2.** Uses intermediate-level community summaries to answer queries. These are sub-communities of C1, if present, otherwise C1 communities projected downwards.
- **C3.** Uses low-level community summaries (greatest in number) to answer queries. These are sub-communities of C2, if present, otherwise C2 communities projected downwards.
- **TS.** The same method as in Section 3.1.6, except source texts (rather than community summaries) are shuffled and chunked for the map-reduce summarization stages.
- **SS.** An implementation of vector RAG in which text chunks are retrieved and added to the available context window until the specified token limit is reached.

The size of the context window and the prompts used for answer generation are the same across all six conditions (except for minor modifications to reference styles to match the types of context information used).
Conditions only differ in how the contents of the context window are created.

The graph index supporting conditions C0-C3 was created using our generic prompts for entity and relationship extraction, with entity types and few-shot examples tailored to the domain of the data.

#### 4.1.3 Configuration

We used a fixed context window size of 8k tokens for generating community summaries, community answers, and global answers (explained in Appendix C).
Graph indexing with a 600 token window (explained in Section A.2) took 281 minutes for the Podcast dataset, running on a virtual machine (16GB RAM, Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz) and using a public OpenAI endpoint for gpt-4-turbo (2M TPM, 10k RPM).

We implemented Leiden community detection using the graspologic library.
The prompts used to generate the graph index and global answers can be found in Appendix E, while the prompts used to evaluate LLM responses against our criteria can be found in Appendix F.
A full statistical analysis of the results presented in the next section can be found in Appendix G.

### 4.2 Experiment 2

To validate the comprehensiveness and diversity results from Experiment 1, we implemented claim-based measures of these qualities. We use the definition of a factual claim from, which is “a statement that explicitly presents some verifiable facts.” For example, the sentence “California and New York implemented incentives for renewable energy adoption, highlighting the broader importance of sustainability in policy decisions” contains two factual claims: (1) California implemented incentives for renewable energy adoption, and (2) New York implemented incentives for renewable energy adoption.

To extract factual claims, we used Claimify, an LLM-based method that identifies sentences in an answer containing at least one factual claim, then decomposes these sentences into simple, self-contained factual claims. We applied Claimify to the answers generated under the conditions from Experiment 1. After removing duplicate claims from each answer, we extracted 47,075 unique claims, with an average of 31 claims per answer.

We defined two metrics, with higher values indicating better performance:

1.  Comprehensiveness: Measured as the average number of claims extracted from the answers generated under each condition.
2.  Diversity: Measured by clustering the claims for each answer and calculating the average number of clusters.

For clustering, we followed the approach described by, which involved using Scikit-learn’s implementation of agglomerative clustering. Clusters were merged through “complete” linkage, meaning they were combined only if the maximum distance between their farthest points was less than or equal to a predefined distance threshold. The distance metric used was $1-\text{ROUGE-L}$. Since the distance threshold influences the number of clusters, we report results across a range of thresholds.

## 5 Results

### 5.1 Experiment 1

The indexing process resulted in a graph consisting of 8,564 nodes and 20,691 edges for the Podcast dataset, and a larger graph of 15,754 nodes and 19,520 edges for the News dataset.
Table 2 shows the number of community summaries at different levels of each graph community hierarchy.

Figure: Figure 2: Head-to-head win rate percentages of (row condition) over (column condition) across two datasets, four metrics, and 125 questions per comparison (each repeated five times and averaged). The overall winner per dataset and metric is shown in bold. Self-win rates were not computed but are shown as the expected 50% for reference. All Graph RAG conditions outperformed naïve RAG on comprehensiveness and diversity. Conditions C1-C3 also showed slight improvements in answer comprehensiveness and diversity over TS (global text summarization without a graph index).

**Table 2: Number of context units (community summaries for C0-C3 and text chunks for TS), corresponding token counts, and percentage of the maximum token count. Map-reduce summarization of source texts is the most resource-intensive approach requiring the highest number of context tokens. Root-level community summaries (C0) require dramatically fewer tokens per query (9x-43x).**
| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | C0 | C1 | C2 | C3 | TS | C0 | C1 | C2 | C3 | TS |
| **Podcast Transcripts** | **News Articles** |
| Units | 34 | 367 | 969 | 1310 | 1669 | 55 | 555 | 1797 | 2142 | 3197 |
| Tokens | 26657 | 225756 | 565720 | 746100 | 1014611 | 39770 | 352641 | 980898 | 1140266 | 1707694 |
| % Max | 2.6 | 22.2 | 55.8 | 73.5 | 100 | 2.3 | 20.7 | 57.4 | 66.8 | 100 |

**Global approaches vs. vector RAG.** As shown in Figure 2 and Table 6, global approaches significantly outperformed conventional vector RAG (SS) in both comprehensiveness and diversity criteria across datasets.
Specifically, global approaches achieved comprehensiveness win rates between 72-83% (p < .001) for Podcast transcripts and 72-80% (p < .001) for News articles, while diversity win rates ranged from 75-82% (p < .001) and 62-71% (p < .01) respectively.
Our use of directness as a validity test confirmed that vector RAG produces the most direct responses across all comparisons.

**Empowerment.** Empowerment comparisons showed mixed results for both global approaches versus vector RAG (SS) and GraphRAG approaches versus source text summarization (TS).
Using an LLM to analyze LLM reasoning for this measure indicated that the ability to provide specific examples, quotes, and citations was judged to be key to helping users reach an informed understanding.
Tuning element extraction prompts may help to retain more of these details in the GraphRAG index.

**Community summaries vs. source texts.** When comparing community summaries to source texts using GraphRAG, community summaries generally provided a small but consistent improvement in answer comprehensiveness and diversity, except for root-level summaries.
Intermediate-level summaries in the Podcast dataset and low-level community summaries in the News dataset achieved comprehensiveness win rates of 57% (p < .001) and 64% (p < .001), respectively.
Diversity win rates were 57% (p = .036) for Podcast intermediate-level summaries and 60% (p < .001) for News low-level community summaries.
Table 2 also illustrates the scalability advantages of GraphRAG compared to source text summarization: for low-level community summaries (C3), GraphRAG required 26-33% fewer context tokens, while for root-level community summaries (C0), it required over 97% fewer tokens.
For a modest drop in performance compared with other global methods, root-level GraphRAG offers a highly efficient method for the iterative question answering that characterizes sensemaking activity, while retaining advantages in comprehensiveness (72% win rate) and diversity (62% win rate) over vector RAG.

### 5.2 Experiment 2

Table 3 shows the results for the average number of extracted claims (i.e., the claim-based measure of comprehensiveness) per condition. For both the News and Podcast datasets, all global search conditions (C0-C3) and source text summarization (TS) had greater comprehensiveness than vector RAG (SS). The differences were statistically significant (p < .05) in all cases. These findings align with the LLM-based win rates from Experiment 1.

Table 4 contains the results for the average number of clusters, the claim-based measure of diversity. For the Podcast dataset, all global search conditions had significantly greater diversity than SS across all distance thresholds (p < .05), consistent with the win rates observed in Experiment 1. For the News dataset, however, only C0 significantly outperformed SS across all distance thresholds (p < .05). While C1-C3 also achieved higher average cluster counts than SS, the differences were statistically significant only at certain distance thresholds. In Experiment 1, all global search conditions significantly outperformed SS in the News dataset – not just C0. However, the differences in mean diversity scores between SS and the global search conditions were smaller for the News dataset than for the Podcast dataset, aligning directionally with the claim-based results.

For both comprehensiveness and diversity, across both datasets, there were no statistically significant differences observed among the global search conditions or between global search and TS.

Finally, for each pairwise comparison in Experiment 1, we tested whether the answer preferred by the LLM aligned with the winner based on the claim-based metrics. Since each pairwise comparison in Experiment 1 was performed five times, while the claim-based metrics provided only one outcome per comparison, we aggregated the Experiment 1 results into a single label using majority voting. For example, if C0 won over SS in three out of five judgments for comprehensiveness on a given question, C0 was labeled the winner and SS the loser. However, if C0 won twice, SS won once, and they tied twice, then there was no majority outcome, so the final label was a tie.

We found that exact ties were rare for the claim-based metrics. One possible solution is to define a tie based on a threshold (e.g., the absolute difference between the claim-based results for condition A and condition B must be less than or equal to $x$). However, we observed that the results were sensitive to the choice of threshold. As a result, we focused on cases where the aggregated LLM label was not a tie, representing 33% and 39% of pairwise comparisons for comprehensiveness and diversity, respectively. In these cases, the aggregated LLM label matched the claim-based label in 78% of pairwise comparisons for comprehensiveness and 69-70% for diversity (across all distance thresholds), indicating moderately strong alignment.

**Table 3: Average number of extracted claims, reported by condition and dataset type. Bolded values represent the highest score in each column.**
| Condition | Average Number of Claims | |
|---|---|---|
| | **News Articles** | **Podcast Transcripts** |
| C0 | **34.18** | **32.21** |
| C1 | 32.50 | 32.20 |
| C2 | 31.62 | 32.46 |
| C3 | 33.14 | 32.28 |
| TS | 32.89 | 31.39 |
| SS | 25.23 | 26.50 |

**Table 4: Average number of clusters across different distance thresholds, reported by condition and dataset type. Bolded values represent the highest score in each row.**
| Dataset | Distance Threshold | Average Number of Clusters | | | | | |
|---|---|---|---|---|---|---|---|
| | **C0** | **C1** | **C2** | **C3** | **TS** | **SS** | | |
| **News Articles** | 0.5 | **23.42** | 21.85 | 21.90 | 22.13 | 21.80 | 17.92 |
| | 0.6 | **21.65** | 20.38 | 20.30 | 20.52 | 20.13 | 16.78 | |
| | 0.7 | **20.19** | 19.06 | 19.03 | 19.13 | 18.62 | 15.80 | |
| | 0.8 | **18.86** | 17.78 | 17.82 | 17.79 | 17.30 | 14.80 | |
| **Podcast Transcripts** | 0.5 | **23.16** | 22.62 | 22.52 | 21.93 | 21.14 | 18.55 |
| | 0.6 | **21.65** | 21.33 | 21.21 | 20.62 | 19.70 | 17.39 | |
| | 0.7 | **20.41** | 20.04 | 19.79 | 19.22 | 18.08 | 16.28 | |
| | 0.8 | **19.26** | 18.77 | 18.46 | 17.89 | 16.66 | 15.07 | |

## 6 Discussion

### 6.1 Limitations of Evaluation Approach

Our evaluation to date has focused on sensemaking questions specific to two corpora each containing approximately 1 million tokens.
More work is needed to understand how performance generalizes to datasets from various domains with different use cases.
Comparison of fabrication rates, e.g., using approaches like SelfCheckGPT, would also strengthen the current analysis.

### 6.2 Future Work

The graph index, rich text annotations, and hierarchical community structure supporting the current GraphRAG approach offer many possibilities for refinement and adaptation.
This includes RAG approaches that operate in a more local manner, via embedding-based matching of user queries and graph annotations.
In particular, we see potential in hybrid RAG schemes that combine embedding-based matching with just-in-time community report generation before employing our map-reduce summarization mechanisms.
This “roll-up” approach could also be extended across multiple levels of the community hierarchy, as well as implemented as a more exploratory “drill down” mechanism that follows the information scent contained in higher-level community summaries.

*Broader impacts*. As a mechanism for question answering over large document collections, there are risks to downstream sensemaking and decision-making tasks if the generated answers do not accurately represent the source data.
System use should be accompanied by clear disclosures of AI use and the potential for errors in outputs.
Compared to vector RAG, however, GraphRAG shows promise as a way to mitigate these downstream risks for questions of a global nature, which might otherwise be answered by samples of retrieved facts falsely presented as global summaries.

## 7 Conclusion

We have presented GraphRAG, a RAG approach that combines knowledge graph generation and query-focused summarization (QFS) to support human sensemaking over entire text corpora.
Initial evaluations show substantial improvements over a vector RAG baseline for both the comprehensiveness and diversity of answers, as well as favorable comparisons to a global but graph-free approach using map-reduce source text summarization.
For situations requiring many global queries over the same dataset, summaries of root-level communities in the entity-based graph index provide a data index that is both superior to vector RAG and achieves competitive performance to other global methods at a fraction of the token cost.

## Acknowledgements

We would also like to thank the following people who contributed to the work: Alonso Guevara Fernández, Amber Hoak, Andrés Morales Esquivel, Ben Cutler, Billie Rinaldi, Chris Sanchez, Chris Trevino, Christine Caggiano, David Tittsworth, Dayenne de Souza, Douglas Orbaker, Ed Clark, Gabriel Nieves-Ponce, Gaudy Blanco Meneses, Kate Lytvynets, Katy Smith, Mónica Carvajal, Nathan Evans, Richard Ortega, Rodrigo Racanicci, Sarah Smith, and Shane Solomon.

## Appendix A Entity and Relationship Extraction Approach

The following prompts, designed for GPT-4, are used in the default GraphRAG initialization pipeline:

- [Default Graph Extraction Prompt](https://github.com/microsoft/graphrag/blob/6d21ef268377e319a165ca2250bd6841737df1ad/graphrag/prompts/index/entity_extraction.py#L6)
- [Claim Extraction Prompt](https://github.com/microsoft/graphrag/blob/6d21ef268377e319a165ca2250bd6841737df1ad/graphrag/prompts/index/claim_extraction.py#L1)

### A.1 Entity Extraction

We do this using a multipart LLM prompt that first identifies all *entities* in the text, including their name, type, and description, before identifying all *relationships* between clearly related entities, including the source and target entities and a description of their relationship. Both kinds of element instance are output in a single list of delimited tuples.

### A.2 Self-Reflection

The choice of prompt engineering techniques has a strong impact on the quality of knowledge graph extraction, and different techniques have different costs in terms of tokens consumed and generated by the model.
*Self-reflection* is a prompt engineering technique where the LLM generates an answer, and is then prompted to evaluate its output for correctness, clarity, or completeness, then finally generate an improved response based on that evaluation.
We leverage self-reflection in knowledge graph extraction, and explore ways how removing self-reflection affects performance and cost.

Using larger chunk size is less costly in terms of calls to the LLM.
However, the LLM tends to extract few entities from chunks of larger size.
For example, in a sample dataset (HotPotQA), GPT-4 extracted almost twice as many entity references when the chunk size was 600 tokens than when it was 2400.
To address this issue, we deploy a self-reflection prompt engineering approach.
After entities are extracted from a chunk, we provide the extracted entities back to the LLM, prompting it to “glean” any entities that it may have missed.
This is a multi-stage process in which we first ask the LLM to assess whether all entities were extracted, using a logit bias of 100 to force a yes/no decision.
If the LLM responds that entities were missed, then a continuation indicating that “MANY entities were missed in the last extraction” encourages the LLM to detect these missing entities.
This approach allows us to use larger chunk sizes without a drop in quality (Figure 3) or the forced introduction of noise.
We interate self-reflection steps up to a specified maximum number of times.

Figure: Figure 3: How the entity references detected in the HotPotQA dataset

## Appendix B Example Community Detection

Figure: Figure 4: Graph communities detected using the Leiden algorithm over the MultiHop-RAG dataset as indexed. Circles represent entity nodes with size proportional to their degree. Node layout was performed via OpenORD and Force Atlas 2. Node colors represent entity communities, shown at two levels of hierarchical clustering: (a) Level 0, corresponding to the hierarchical partition with maximum modularity, and (b) Level 1, which reveals internal structure within these root-level communities.
Refer to caption: Level0Multihop.jpg

## Appendix C Context Window Selection

The effect of context window size on any particular task is unclear, especially for models like gpt-4-turbo with a large context size of 128k tokens. Given the potential for information to be “lost in the middle” of longer contexts, we wanted to explore the effects of varying the context window size for our combinations of datasets, questions, and metrics. In particular, our goal was to determine the optimum context size for our baseline condition (SS) and then use this uniformly for all query-time LLM use. To that end, we tested four context window sizes: 8k, 16k, 32k and 64k. Surprisingly, the smallest context window size tested (8k) was universally better for all comparisons on comprehensiveness (average win rate of 58.1%), while performing comparably with larger context sizes on diversity (average win rate = 52.4%), and empowerment (average win rate = 51.3%). Given our preference for more comprehensive and diverse answers, we therefore used a fixed context window size of 8k tokens for the final evaluation.

## Appendix D Example Answer Comparison

**Table 5: Example question, answers, and LLM-generated assessments for the News article dataset.**
| Question | Which public figures are repeatedly mentioned across various entertainment articles? |
|---|---|
| Graph RAG | The entertainment industry is vast and diverse, encompassing film, television, music, sports, and digital media. Certain public figures stand out due to their significant contributions and influence across these sectors. The following summary highlights key individuals who are repeatedly mentioned in various entertainment articles, reflecting their impact and presence within the industry.<br>Actors and Directors […] Public Figures in Controversy […]<br>Musicians and Executives […] Athletes and Coaches […] Influencers and Entrepreneurs […]<br>The repeated mention of these figures in entertainment articles signifies their ongoing relevance and the public’s interest in their work. Their influence spans across various aspects of entertainment, from shaping cultural narratives in film and television to driving trends in music and digital media. These individuals not only contribute to their respective fields but also influence the broader cultural landscape, often becoming central figures in social discussions and public discourse. |
| Naïve RAG | Public figures who are repeatedly mentioned across various entertainment articles include Taylor Swift, Travis Kelce, Britney Spears, and Justin Timberlake. These individuals have been highlighted for various reasons, ranging from their professional achievements to their personal lives.<br>Taylor Swift […] Travis Kelce […] Britney Spears […] Justin Timberlake<br>[…]<br>These figures are frequently covered due to their high-profile status and the public’s interest in their careers and personal lives. Their activities, whether in music, sports, or personal relationships, have significant cultural and economic impacts, as evidenced by the media coverage and public reactions. |
| LLM Decision | Comprehensiveness: Winner=1 (Graph RAG). Answer 1 is better because it provides a more comprehensive and detailed list of public figures from a wider range of entertainment sectors, including film, television, music, sports, gaming, and digital media. It also includes examples of their contributions and the impact they have on their respective fields, as well as mentions of controversies and their implications. Answer 2, while detailed in its coverage of a few individuals, is limited to a smaller number of public figures and focuses primarily on their personal lives and relationships rather than a broad spectrum of their professional influence across the entertainment industry.<br>Diversity: Winner=1 (Graph RAG). Answer 1 is better because it provides a more varied and rich response by covering a wide range of public figures from different sectors of the entertainment industry, including film, television, music, sports, gaming, and digital media. It offers insights into the contributions and influence of these figures, as well as controversies and their impact on public discourse. The answer also cites specific data sources for each mentioned figure, indicating a diverse range of evidence to support the claims. In contrast, Answer 2 focuses on a smaller group of public figures, primarily from the music industry and sports, and relies heavily on a single source for data, which makes it less diverse in perspectives and insights.<br>Empowerment: Winner=1 (Graph RAG). Answer 1 is better because it provides a comprehensive and structured overview of public figures across various sectors of the entertainment industry, including film, television, music, sports, and digital media. It lists multiple individuals, providing specific examples of their contributions and the context in which they are mentioned in entertainment articles, along with references to data reports for each claim. This approach helps the reader understand the breadth of the topic and make informed judgments without being misled. In contrast, Answer 2 focuses on a smaller group of public figures and primarily discusses their personal lives and relationships, which may not provide as broad an understanding of the topic. While Answer 2 also cites sources, it does not match the depth and variety of Answer 1.<br>Directness: Winner=2 (Naïve RAG). Answer 2 is better because it directly lists specific public figures who are repeatedly mentioned across various entertainment articles, such as Taylor Swift, Travis Kelce, Britney Spears, and Justin Timberlake, and provides concise explanations for their frequent mentions. Answer 1, while comprehensive, includes a lot of detailed information about various figures in different sectors of entertainment, which, while informative, does not directly answer the question with the same level of conciseness and specificity as Answer 2. |

## Appendix E System Prompts

### E.1 Element Instance Generation

```
---Goal---
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.
---Steps---
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity’s attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_
delimiter}<entity_description>
2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_
entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_strength>)
3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.
4. When finished, output {completion_delimiter}
---Examples---
Entity_types: ORGANIZATION,PERSON
Input:
The Fed is scheduled to meet on Tuesday and Wednesday, with the central bank planning to release its latest policy decision on Wednesday at 2:00 p.m. ET, followed by a press conference where Fed Chair Jerome Powell will take questions. Investors expect the Federal Open Market Committee to hold its benchmark interest rate steady in a range of 5.25%-5.5%.
Output:
("entity"{tuple_delimiter}FED{tuple_delimiter}ORGANIZATION{tuple_delimiter}The Fed is the Federal Reserve, which is setting interest rates on Tuesday and Wednesday)
{record_delimiter}
("entity"{tuple_delimiter}JEROME POWELL{tuple_delimiter}PERSON{tuple_delimiter}Jerome Powell is the chair of the Federal Reserve)
{record_delimiter}
("entity"{tuple_delimiter}FEDERAL OPEN MARKET COMMITTEE{tuple_delimiter}ORGANIZATION{tuple_delimiter}The Federal Reserve committee makes key decisions about interest rates and the growth of the United States money supply)
{record_delimiter}
("relationship"{tuple_delimiter}JEROME POWELL{tuple_delimiter}FED{tuple_delimiter}Jerome Powell is the Chair of the Federal Reserve and will answer questions at a press conference{tuple_delimiter}9)
{completion_delimiter}
…More examples…
---Real Data---
Entity_types: {entity_types}
Input:
{input_text}
Output:
```

### E.2 Community Summary Generation

```
---Role---
You are an AI assistant that helps a human analyst to perform general information discovery. Information discovery is the process of identifying and assessing relevant information associated with certain entities (e.g., organizations and individuals) within a network.
---Goal---
Write a comprehensive report of a community, given a list of entities that belong to the community as well as their relationships and optional associated claims. The report will be used to inform decision-makers about information associated with the community and their potential impact. The content of this report includes an overview of the community’s key entities, their legal compliance, technical capabilities, reputation, and noteworthy claims.
---Report Structure---
The report should include the following sections:
- TITLE: community’s name that represents its key entities - title should be short but specific. When possible, include representative named entities in the title.
- SUMMARY: An executive summary of the community’s overall structure, how its entities are related to each other, and significant information associated with its entities.
- IMPACT SEVERITY RATING: a float score between 0-10 that represents the severity of IMPACT posed by entities within the community. IMPACT is the scored importance of a community.
- RATING EXPLANATION: Give a single sentence explanation of the IMPACT severity rating.
- DETAILED FINDINGS: A list of 5-10 key insights about the community. Each insight should have a short summary followed by multiple paragraphs of explanatory text grounded according to the grounding rules below. Be comprehensive.
Return output as a well-formed JSON-formatted string with the following format:
{{
"title": <report_title>,
"summary": <executive_summary>,
"rating": <impact_severity_rating>,
"rating_explanation": <rating_explanation>,
"findings": [
{{
"summary":<insight_1_summary>,
"explanation": <insight_1_explanation>
}},
{{
"summary":<insight_2_summary>,
"explanation": <insight_2_explanation>
}}
]
}}
---Grounding Rules---
Points supported by data should list their data references as follows:
"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."
Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.
For example:
"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Reports (1), Entities (5, 7); Relationships (23); Claims (7, 2, 34, 64, 46, +more)]."
where 1, 5, 7, 23, 2, 34, 46, and 64 represent the id (not the index) of the relevant data record.
Do not include information where the supporting evidence for it is not provided.
---Example---
Input:
Entities
id,entity,description
5,VERDANT OASIS PLAZA,Verdant Oasis Plaza is the location of the Unity March
6,HARMONY ASSEMBLY,Harmony Assembly is an organization that is holding a march at Verdant Oasis Plaza
Relationships
id,source,target,description
37,VERDANT OASIS PLAZA,UNITY MARCH,Verdant Oasis Plaza is the location of the Unity March
38,VERDANT OASIS PLAZA,HARMONY ASSEMBLY,Harmony Assembly is holding a march at Verdant Oasis Plaza
39,VERDANT OASIS PLAZA,UNITY MARCH,The Unity March is taking place at Verdant Oasis Plaza
40,VERDANT OASIS PLAZA,TRIBUNE SPOTLIGHT,Tribune Spotlight is reporting on the Unity march taking place at Verdant Oasis Plaza
41,VERDANT OASIS PLAZA,BAILEY ASADI,Bailey Asadi is speaking at Verdant Oasis Plaza about the march
43,HARMONY ASSEMBLY,UNITY MARCH,Harmony Assembly is organizing the Unity March
Output:
{{
"title": "Verdant Oasis Plaza and Unity March",
"summary": "The community revolves around the Verdant Oasis Plaza, which is the location of the Unity March. The plaza has relationships with the Harmony Assembly, Unity March, and Tribune Spotlight, all of which are associated with the march event.",
"rating": 5.0,
"rating_explanation": "The impact severity rating is moderate due to the potential for unrest or conflict during the Unity March.",
"findings": [
{{
"summary": "Verdant Oasis Plaza as the central location",
"explanation": "Verdant Oasis Plaza is the central entity in this community, serving as the location for the Unity March. This plaza is the common link between all other entities, suggesting its significance in the community. The plaza’s association with the march could potentially lead to issues such as public disorder or conflict, depending on the nature of the march and the reactions it provokes. [Data: Entities (5), Relationships (37, 38, 39, 40, 41,+more)]"
}},
{{
"summary": "Harmony Assembly’s role in the community",
"explanation": "Harmony Assembly is another key entity in this community, being the organizer of the march at Verdant Oasis Plaza. The nature of Harmony Assembly and its march could be a potential source of threat, depending on their objectives and the reactions they provoke. The relationship between Harmony Assembly and the plaza is crucial in understanding the dynamics of this community. [Data: Entities(6), Relationships (38, 43)]"
}},
{{
"summary": "Unity March as a significant event",
"explanation": "The Unity March is a significant event taking place at Verdant Oasis Plaza. This event is a key factor in the community’s dynamics and could be a potential source of threat, depending on the nature of the march and the reactions it provokes. The relationship between the march and the plaza is crucial in understanding the dynamics of this community. [Data: Relationships (39)]"
}},
{{
"summary": "Role of Tribune Spotlight",
"explanation": "Tribune Spotlight is reporting on the Unity March taking place in Verdant Oasis Plaza. This suggests that the event has attracted media attention, which could amplify its impact on the community. The role of Tribune Spotlight could be significant in shaping public perception of the event and the entities involved. [Data: Relationships (40)]"
}}
]
}}
---Real Data---
Use the following text for your answer. Do not make anything up in your answer.
Input:
{input_text}
…Report Structure and Grounding Rules Repeated…
Output:
```

### E.3 Community Answer Generation

```
---Role---
You are a helpful assistant responding to questions about a dataset by synthesizing perspectives from multiple analysts.
---Goal---
Generate a response of the target length and format that responds to the user’s question, summarize all the reports from multiple analysts who focused on different parts of the dataset, and incorporate any relevant general knowledge.
Note that the analysts’ reports provided below are ranked in the **descending order of helpfulness**.
If you don’t know the answer, just say so. Do not make anything up.
The final response should remove all irrelevant information from the analysts’ reports and merge the cleaned information into a comprehensive answer that provides explanations of all the key points and implications appropriate for the response length and format.
Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
The response shall preserve the original meaning and use of modal verbs such as "shall", "may" or "will".
The response should also preserve all the data references previously included in the analysts’ reports, but do not mention the roles of multiple analysts in the analysis process.
Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.
For example:
"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Reports (2, 7, 34, 46, 64, +more)]. He is also CEO of company X [Data: Reports (1, 3)]"
where 1, 2, 3, 7, 34, 46, and 64 represent the id (not the index) of the relevant data record.
Do not include information where the supporting evidence for it is not provided.
---Target response length and format---
{response_type}
---Analyst Reports---
{report_data}
…Goal and Target response length and format repeated…
Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
Output:
```

### E.4 Global Answer Generation

```
---Role---
You are a helpful assistant responding to questions about data in the tables provided.
---Goal---
Generate a response of the target length and format that responds to the user’s question, summarize all relevant information in the input data tables appropriate for the response length and format, and incorporate any relevant general knowledge.
If you don’t know the answer, just say so. Do not make anything up.
The response shall preserve the original meaning and use of modal verbs such as "shall", "may" or "will".
Points supported by data should list the relevant reports as references as follows:
"This is an example sentence supported by data references [Data: Reports (report ids)]"
Note: the prompts for SS (semantic search) and TS (text summarization) conditions use ”Sources” in place of ”Reports” above.
Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.
For example:
"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Reports (2, 7, 64, 46, 34, +more)]. He is also CEO of company X [Data: Reports (1, 3)]"
where 1, 2, 3, 7, 34, 46, and 64 represent the id (not the index) of the relevant data report in the provided tables.
Do not include information where the supporting evidence for it is not provided.
At the beginning of your response, generate an integer score between 0-100 that indicates how **helpful** is this response in answering the user’s question. Return the score in this format: <ANSWER_HELPFULNESS> score_value </ANSWER_HELPFULNESS>.
---Target response length and format---
{response_type}
---Data tables---
{context_data}
…Goal and Target response length and format repeated…
Output:
```

## Appendix F Evaluation Prompts

### F.1 Relative Assessment Prompt

```
---Role---
You are a helpful assistant responsible for grading two answers to a question that are provided by two different people.
---Goal---
Given a question and two answers (Answer 1 and Answer 2), assess which answer is better according to the following measure:
{criteria}
Your assessment should include two parts:
- Winner: either 1 (if Answer 1 is better) and 2 (if Answer 2 is better) or 0 if they are fundamentally similar and the differences are immaterial.
- Reasoning: a short explanation of why you chose the winner with respect to the measure described above.
Format your response as a JSON object with the following structure:
{{
"winner": <1, 2, or 0>,
"reasoning": "Answer 1 is better because <your reasoning>."
}}
---Question---
{question}
---Answer 1---
{answer1}
---Answer 2---
{answer2}
Assess which answer is better according to the following measure:
{criteria}
Output:
```

### F.2 Relative Assessment Metrics

```python
CRITERIA = {
"comprehensiveness": "How much detail does the answer provide to cover all the aspects and details of the question? A comprehensive answer should be thorough and complete, without being redundant or irrelevant. For example, if the question is ’What are the benefits and drawbacks of nuclear energy?’, a comprehensive answer would provide both the positive and negative aspects of nuclear energy, such as its efficiency, environmental impact, safety, cost, etc. A comprehensive answer should not leave out any important points or provide irrelevant information. For example, an incomplete answer would only provide the benefits of nuclear energy without describing the drawbacks, or a redundant answer would repeat the same information multiple times.",
"diversity": "How varied and rich is the answer in providing different perspectives and insights on the question? A diverse answer should be multi-faceted and multi-dimensional, offering different viewpoints and angles on the question. For example, if the question is ’What are the causes and effects of climate change?’, a diverse answer would provide different causes and effects of climate change, such as greenhouse gas emissions, deforestation, natural disasters, biodiversity loss, etc. A diverse answer should also provide different sources and evidence to support the answer. For example, a single-source answer would only cite one source or evidence, or a biased answer would only provide one perspective or opinion.",
"directness": "How specifically and clearly does the answer address the question? A direct answer should provide a clear and concise answer to the question. For example, if the question is ’What is the capital of France?’, a direct answer would be ’Paris’. A direct answer should not provide any irrelevant or unnecessary information that does not answer the question. For example, an indirect answer would be ’The capital of France is located on the river Seine’.",
"empowerment": "How well does the answer help the reader understand and make informed judgements about the topic without being misled or making fallacious assumptions. Evaluate each answer on the quality of answer as it relates to clearly explaining and providing reasoning and sources behind the claims in the answer."
}
```

## Appendix G Statistical Analysis

**Table 6: Pairwise comparisons of six conditions on four metrics across 125 questions and two datasets. For each question and metric, the winning condition received a score of 100, the losing condition received a score of 0, and in the event of a tie, each condition was scored 50. These scores were then averaged over five evaluation runs for each condition. Results of Shapiro-Wilk tests indicated that the data did not follow a normal distribution. Thus, non-parametric tests (Wilcoxon signed-rank tests) were employed to assess the performance differences between pairs of conditions, with Holm-Bonferroni correction applied to account for multiple pairwise comparisons. The corrected p-values that indicated statistically significant differences are highlighted in bold.**
| | | | **Podcast Transcripts** | | | | **News Articles** | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | **Condition 1** | **Condition 2** | **Mean 1** | **Mean 2** | **Z-value** | **p-value** | **Mean 1** | **Mean 2** | **Z-value** | **p-value** |
| **Comprehensiveness** | C0 | TS | 50.24 | 49.76 | -0.06 | 1 | 55.52 | 44.48 | -2.03 | 0.17 |
| | C1 | TS | 51.92 | 48.08 | -1.56 | 0.633 | 58.8 | 41.2 | -3.62 | **0.002** |
| | C2 | TS | 57.28 | 42.72 | -4.1 | **<0.001** | 62.08 | 37.92 | -5.07 | **<0.001** |
| | C3 | TS | 56.48 | 43.52 | -3.42 | **0.006** | 63.6 | 36.4 | -5.63 | **<0.001** |
| | C0 | SS | 71.92 | 28.08 | -6.2 | **<0.001** | 71.76 | 28.24 | -6.3 | **<0.001** |
| | C1 | SS | 75.44 | 24.56 | -7.45 | **<0.001** | 74.72 | 25.28 | -7.78 | **<0.001** |
| | C2 | SS | 77.76 | 22.24 | -8.17 | **<0.001** | 79.2 | 20.8 | -8.34 | **<0.001** |
| | C3 | SS | 78.96 | 21.04 | -8.12 | **<0.001** | 79.44 | 20.56 | -8.44 | **<0.001** |
| | TS | SS | 83.12 | 16.88 | -8.85 | **<0.001** | 79.6 | 20.4 | -8.27 | **<0.001** |
| | C0 | C1 | 53.2 | 46.8 | -1.96 | 0.389 | 51.92 | 48.08 | -0.45 | 0.777 |
| | C0 | C2 | 50.24 | 49.76 | -0.23 | 1 | 53.68 | 46.32 | -1.54 | 0.371 |
| | C1 | C2 | 51.52 | 48.48 | -1.62 | 0.633 | 57.76 | 42.24 | -4.01 | **<0.001** |
| | C0 | C3 | 49.12 | 50.88 | -0.56 | 1 | 52.16 | 47.84 | -0.86 | 0.777 |
| | C1 | C3 | 50.32 | 49.68 | -0.66 | 1 | 55.12 | 44.88 | -2.94 | **0.016** |
| | C2 | C3 | 52.24 | 47.76 | -1.97 | 0.389 | 58.64 | 41.36 | -3.68 | **0.002** |
| **Diversity** | C0 | TS | 50.24 | 49.76 | -0.11 | 1 | 46.88 | 53.12 | -1.38 | 0.676 |
| | C1 | TS | 50.48 | 49.52 | -0.12 | 1 | 54.64 | 45.36 | -1.88 | 0.298 |
| | C2 | TS | 57.12 | 42.88 | -2.84 | **0.036** | 55.76 | 44.24 | -2.16 | 0.184 |
| | C3 | TS | 54.32 | 45.68 | -2.39 | 0.1 | 60.16 | 39.84 | -4.07 | **<0.001** |
| | C0 | SS | 76.56 | 23.44 | -7.12 | **<0.001** | 62.08 | 37.92 | -3.57 | **0.003** |
| | C1 | SS | 75.44 | 24.56 | -7.33 | **<0.001** | 64.96 | 35.04 | -4.92 | **<0.001** |
| | C2 | SS | 80.56 | 19.44 | -8.21 | **<0.001** | 70.56 | 29.44 | -6.29 | **<0.001** |
| | C3 | SS | 80.8 | 19.2 | -8.3 | **<0.001** | 69.12 | 30.88 | -5.53 | **<0.001** |
| | TS | SS | 82.08 | 17.92 | -8.43 | **<0.001** | 67.2 | 32.8 | -4.85 | **<0.001** |
| | C0 | C1 | 49.76 | 50.24 | -0.13 | 1 | 39.68 | 60.32 | -3.61 | **0.003** |
| | C0 | C2 | 46.32 | 53.68 | -1.5 | 0.669 | 40.96 | 59.04 | -3.14 | **0.012** |
| | C1 | C2 | 44.08 | 55.92 | -3.27 | **0.011** | 50.24 | 49.76 | -0.22 | 1 |
| | C0 | C3 | 44 | 56 | -2.6 | 0.065 | 41.04 | 58.96 | -3.47 | **0.004** |
| | C1 | C3 | 45.44 | 54.56 | -2.98 | **0.026** | 49.52 | 50.48 | -0.01 | 1 |
| | C2 | C3 | 48.48 | 51.52 | -0.96 | 1 | 50.96 | 49.04 | -0.39 | 1 |
| **Empowerment** | C0 | TS | 40.96 | 59.04 | -4.3 | **<0.001** | 42.24 | 57.76 | -3.32 | **0.012** |
| | C1 | TS | 45.2 | 54.8 | -3.76 | **0.002** | 50 | 50 | -0.12 | 1 |
| | C2 | TS | 47.68 | 52.32 | -2.2 | 0.281 | 49.52 | 50.48 | -0.22 | 1 |
| | C3 | TS | 48.72 | 51.28 | -1.27 | 1 | 51.68 | 48.32 | -1.2 | 1 |
| | C0 | SS | 42.96 | 57.04 | -3.71 | **0.003** | 42.72 | 57.28 | -3.12 | **0.022** |
| | C1 | SS | 47.68 | 52.32 | -1.5 | 0.936 | 51.36 | 48.64 | -0.84 | 1 |
| | C2 | SS | 50.72 | 49.28 | -0.55 | 1 | 49.84 | 50.16 | -0.2 | 1 |
| | C3 | SS | 48.96 | 51.04 | -0.57 | 1 | 49.52 | 50.48 | -0.08 | 1 |
| | TS | SS | 57.52 | 42.48 | -4.1 | **<0.001** | 52.88 | 47.12 | -1.1 | 1 |
| | C0 | C1 | 48.72 | 51.28 | -1.23 | 1 | 42.4 | 57.6 | -3.9 | **0.001** |
| | C0 | C2 | 46.64 | 53.36 | -2.54 | 0.12 | 44.8 | 55.2 | -2.16 | 0.336 |
| | C1 | C2 | 49.28 | 50.72 | -1.73 | 0.682 | 52 | 48 | -1.45 | 1 |
| | C0 | C3 | 47.6 | 52.4 | -1.78 | 0.682 | 44.32 | 55.68 | -3.45 | **0.008** |
| | C1 | C3 | 50 | 50 | 0 | 1 | 51.44 | 48.56 | -1.02 | 1 |
| | C2 | C3 | 50.72 | 49.28 | -0.86 | 1 | 50.4 | 49.6 | -0.22 | 1 |
| **Directness** | C0 | TS | 44.96 | 55.04 | -4.09 | **<0.001** | 45.2 | 54.8 | -3.68 | **0.003** |
| | C1 | TS | 47.92 | 52.08 | -2.41 | 0.126 | 46.64 | 53.36 | -2.91 | **0.04** |
| | C2 | TS | 48.8 | 51.2 | -2.23 | 0.179 | 48.32 | 51.68 | -2.12 | 0.179 |
| | C3 | TS | 48.08 | 51.92 | -2.23 | 0.179 | 48.32 | 51.68 | -2.56 | 0.074 |
| | C0 | SS | 35.12 | 64.88 | -6.17 | **<0.001** | 41.44 | 58.56 | -4.82 | **<0.001** |
| | C1 | SS | 40.32 | 59.68 | -4.83 | **<0.001** | 45.2 | 54.8 | -3.19 | **0.017** |
| | C2 | SS | 40.4 | 59.6 | -4.67 | **<0.001** | 44.88 | 55.12 | -3.65 | **0.003** |
| | C3 | SS | 40.48 | 59.52 | -4.69 | **<0.001** | 45.6 | 54.4 | -2.86 | **0.043** |
| | TS | SS | 43.6 | 56.4 | -3.96 | **<0.001** | 46 | 54 | -2.68 | 0.066 |
| | C0 | C1 | 46.96 | 53.04 | -2.87 | **0.037** | 47.6 | 52.4 | -2.17 | 0.179 |
| | C0 | C2 | 48.4 | 51.6 | -2.06 | 0.197 | 48.48 | 51.52 | -1.61 | 0.321 |
| | C1 | C2 | 49.84 | 50.16 | -1 | 0.952 | 49.28 | 50.72 | -1.6 | 0.321 |
| | C0 | C3 | 48.4 | 51.6 | -1.8 | 0.29 | 47.2 | 52.8 | -2.62 | 0.071 |
| | C1 | C3 | 49.76 | 50.24 | 0 | 1 | 48.8 | 51.2 | -1.29 | 0.321 |
| | C2 | C3 | 50 | 50 | 0 | 1 | 48.8 | 51.2 | -1.84 | 0.262 |

</details>

<details>
<summary>Retrieval-Augmented Generation (RAG) Fundamentals First</summary>

# Retrieval-Augmented Generation (RAG) Fundamentals First
**Source URL:** <https://decodingml.substack.com/p/rag-fundamentals-first?utm_source=publication-search>

To build successful and complex RAG applications, you must first deeply understand the fundamentals behind them. _In this article, we will learn why we use RAG and how to design the architecture of your RAG layer._

Retrieval-augmented generation (RAG) enhances the accuracy and reliability of generative AI models with information fetched from external sources. It is a technique complementary to the internal knowledge of the LLMs. Before going into the details, let’s understand what RAG stands for:

- **Retrieval:** search for relevant data;

- **Augmented:** add the data as context to the prompt;

- **Generation:** use the augmented prompt with an LLM for generation.


Any LLM is bound to understand the data it was trained on, sometimes called parameterized knowledge. Thus, even if the LLM can perfectly answer what happened in the past, it won’t have access to the newest data or any other external sources on which it wasn’t trained.

Let’s take the most powerful model from OpenAI as an example, which in the summer of 2024 is GPT-4o. The model is trained on data up to Oct 2023. Thus, if we ask what happened during the 2020 pandemic, it can be answered perfectly due to its parametrized knowledge. However, it will not know the answer if we ask about the 2024 soccer EURO cup results due to its bounded parametrized knowledge. Another scenario is that it will start confidently hallucinating and provide a faulty answer.

RAG overcomes these two limitations of LLMs. It provides access to external or latest data and prevents hallucinations, enhancing generative AI models’ accuracy and reliability.

* * *

## **Why use RAG?**

We briefly explained the importance of using RAG in generative AI applications above. Now, we will dig deeper into the “why”. Next, we will focus on what a naïve RAG framework looks like.

For now, to get an intuition about RAG, you have to know that when using RAG, we inject the necessary information into the prompt to answer the initial user question. After, we pass the augmented prompt to the LLM for the final answer. Now the LLM will use the additional context to answer the user question.

There are two fundamental problems that RAG solves:

1\. Hallucinations

2\. Old or private information

### **Hallucinations**

If a chatbot without RAG is asked a question about something it wasn’t trained on, there are big changes that will give you a confident answer about something that isn’t true. Let’s take the 2024 soccer EURO Cup as an example. If the model is trained up to Oct 2023 and we ask something about the tournament, it will most likely come up with some random answer that is hard to differentiate from reality.

Even if the LLM doesn’t hallucinate all the time, it raises the concern of trust in its answers. Thus, we have to ask ourselves: “When can we trust the LLM’s answers?” and “How can we evaluate if the answers are correct?”

By introducing RAG, we will enforce the LLM to always answer solely based on the introduced context. The LLM will act as the reasoning engine, while the additional information added through RAG will act as the single source of truth for the generated answer.

By doing so, we can quickly evaluate if the LLM’s answer is based on the external data or not.

### **Old information**

Any LLM is trained or fine-tuned on a subset of the total world knowledge dataset. This is due to three main issues:

- **Private data:** You cannot train your model on data you don’t own or have the right to use.

- **New data**: New data is generated every second. Thus, you would have to constantly train your LLM to keep up.

- **Costs:** Training or fine-tuning an LLM is an extremely costly operation. Hence, it is not feasible to do it on an hourly or daily basis.


RAG solved these issues, as you no longer have to constantly fine-tune your LLM on new data (or even private data). Directly injecting the necessary data to respond to user questions into the prompts that are fed to the LLM is enough to generate correct and valuable answers.

## **The vanilla RAG framework**

Every RAG system is similar at its roots. We will first focus on understanding RAG in its simplest form. Later, we will gradually introduce more advanced RAG techniques to improve the system’s accuracy.

A RAG system is composed of three main modules independent of each other:

1. **Ingestion pipeline:** A batch or streaming pipeline used to populate the vector DB.

2. **Retrieval pipeline:** A module that queries the vector DB and retrieves relevant entries to the user’s input.

3. **Generation pipeline:** The layer that uses the retrieved data to augment the prompt and an LLM to generate answers.


As these three components are classes or services of their own, we will dig into each separately.

_But how are these three modules connected?_ Here is a very simplistic overview:

1. On the backend side, the ingestion pipeline runs on a schedule or constantly to populate the vector DB with external data.

2. On the client side, the user asks a question.

3. The question is passed to the retrieval module, which pre-processes the user’s input and queries the vector DB.

4. The generation pipelines use a prompt template, user input, and retrieved context to create the prompt.

5. The prompt is passed to an LLM to generate the answer.

6. The answer is shown to the user.


[https://substackcdn.com/image/fetch/$s_!nn9L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a6bf20-e217-4a8c-8df4-f00caa5c51ca_933x933.png](https://substackcdn.com/image/fetch/$s_!nn9L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a6bf20-e217-4a8c-8df4-f00caa5c51ca_933x933.png) Vanilla RAG architecture

### **Ingestion pipeline**

The RAG ingestion pipeline extracts raw documents from various data sources (e.g., data warehouse, data lake, web pages, etc.). Then, it cleans, chunks and embeds the documents. Ultimately, it loads the embedded chunks to a vector DB (or other similar vector storage).

Thus, the RAG ingestion pipeline is split again into the following:

- The **data extraction module** gathers all necessary data from various sources such as databases, APIs, or web pages. This module is highly dependent on your data. It can be as easy as querying your data warehouse or something more complex, such as crawling Wikipedia.

- A **cleaning layer** that standardizes and removes unwanted characters from the extracted data.

- The **chunking module** splits the cleaned documents into smaller ones. As we want to pass the document’s content to an embedding model, this is necessary to ensure it doesn’t exceed the model’s input maximum size. Also, chunking is required to separate specific regions that are semantically related. For example, when chunking a book chapter, the most optimal way is to group similar paragraphs into the same chunk. By doing so, at the retrieval time, you will add only the essential data to the prompt.

- The **embedding component** usesanembedding model to take the chunk’s content (text, images, audio, etc.) and project it into a dense vector packed with semantic value — more on embeddings in the Embeddings models section below.


The **loading module** takes the embedded chunks along with a metadata document. The metadata will contain essential information such as the embedded content, the URL to the source of the chunk, when the content was published on the web, etc. The embedding is used as an index to query similar chunks, while the metadata is used to access the information added to augment the prompt.

At this point, we have an RAG ingestion pipeline that takes raw documents as input, processes them, and populates a vector DB. The next step is to retrieve relevant data from the vector store correctly.

### **Retrieval pipeline**

The retrieval components take the user’s input (text, image, audio, etc.), embed it, and query the vector DB for similar vectors to the user’s input.

The primary function of the retrieval step is to project the user’s input into the same vector space as the embeddings used as an index in the vector DB. This allows us to find the top K’s most similar entries by comparing the embeddings from the vector storage with the user’s input vector. These entries then serve as content to augment the prompt that is passed to the LLM to generate the answer.

You must use a distance metric to compare two vectors, such as the Euclidean or Manhattan distance. But the most popular one is the [cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) \[1\], which is equal to 1 minus the cosine of the angle between two vectors as follows:

[https://substackcdn.com/image/fetch/$s_!LkC-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6d16dbc-de3b-4b57-9f31-07f06799ba57_397x46.jpeg](https://substackcdn.com/image/fetch/$s_!LkC-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6d16dbc-de3b-4b57-9f31-07f06799ba57_397x46.jpeg) Cosine distance formula

It ranges from -1 to 1, with a value of -1 when vectors A and B are in opposite directions, 0 if they are orthogonal and 1 if they point in the same direction.

Most of the time, the cosine distance works well in non-linear complex vector spaces. However, it is essential to notice that choosing the proper distance between two vectors depends on your data and the embedding model you use.

One critical factor to highlight is that the user’s input and embeddings must be in the same vector space. Otherwise, you cannot compute the distance between them. To do so, it is essential to pre-process the user input in the same way you processed the raw documents in the RAG ingestion pipeline. It means you must clean, chunk (if necessary), and embed the user’s input using the same functions, models, and hyperparameters. Similar to how you have to pre-process the data into features in the same way between training and inference, otherwise the inference will yield inaccurate results — a phenomenon also known as the training-serving skew.

### **Generation pipeline**

The last step of the RAG system is to take the user’s input and the retrieved data, pass them to an LLM of your choice and generate the answer.

The final prompt results from a prompt template populated with the user’s query and retrieved context. You might have a single or multiple prompt templates depending on your application. Usually, all the prompt engineering is done at the prompt template level.

Each prompt template and LLM should be tracked and versioned using MLOps best practices. Thus, you always know that a given answer was generated by a specific version of the LLM and prompt template(s).

* * *

## **Conclusion**

In this article, we have looked over the fundamentals of RAG.

First, we understood why RAG is so powerful and why many AI applications implement it, as it overcomes challenges such as hallucinations and outdated data.

Secondly, we examined the architecture of a naive RAG system, which consists of an ingestion, retrieval and generation pipeline.

</details>

<details>
<summary>What Is Retrieval-Augmented Generation, aka RAG?</summary>

# What Is Retrieval-Augmented Generation, aka RAG?

**Source URL:** <https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/>

_Editor’s note: This article, originally published on Nov. 15, 2023, has been updated._

To understand the latest advancements in [generative AI](https://www.nvidia.com/en-us/glossary/data-science/generative-ai/), imagine a courtroom.

Judges hear and decide cases based on their general understanding of the law. Sometimes a case — like a malpractice suit or a labor dispute — requires special expertise, so judges send court clerks to a law library, looking for precedents and specific cases they can cite.

Like a good judge, large language models ( [LLMs](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/)) can respond to a wide variety of human queries. But to deliver authoritative answers — grounded in specific court proceedings or similar ones  — the model needs to be provided that information.

The court clerk of AI is a process called [retrieval-augmented generation](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/), or RAG for short.

## **How It Got Named ‘RAG’**

Patrick Lewis, lead author of the [2020 paper that coined the term](https://arxiv.org/pdf/2005.11401.pdf), apologized for the unflattering acronym that now describes a growing family of methods across hundreds of papers and dozens of commercial services he believes represent the future of generative AI.

https://blogs.nvidia.com/wp-content/uploads/2023/11/Patrick-Lewis-RAG-lead-author.jpg Patrick Lewis

“We definitely would have put more thought into the name had we known our work would become so widespread,” Lewis said in an interview from Singapore, where he was sharing his ideas with a regional conference of database developers.

“We always planned to have a nicer sounding name, but when it came time to write the paper, no one had a better idea,” said Lewis, who now leads a RAG team at AI startup Cohere.

## **So, What Is Retrieval-Augmented Generation (RAG)?**

[Retrieval-augmented generation](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/) is a technique for enhancing the accuracy and reliability of generative AI models with information fetched from specific and relevant data sources.

In other words, it fills a gap in how LLMs work. Under the hood, LLMs are neural networks, typically measured by how many parameters they contain. An LLM’s parameters essentially represent the general patterns of how humans use words to form sentences.

That deep understanding, sometimes called parameterized knowledge, makes LLMs useful in responding to general prompts. However, when users need authoritative, source-grounded answers rather than broad knowledge alone, RAG can provide the necessary depth and accuracy.

## **Combining Internal, External Resources**

Lewis and colleagues developed retrieval-augmented generation to link generative AI services to external resources, especially ones rich in the latest technical details.

The paper, with coauthors from the former Facebook AI Research (now Meta AI), University College London and New York University, called RAG “a general-purpose fine-tuning recipe” because it can be used by nearly any LLM to connect with practically any external resource.

## **Building User Trust**

Retrieval-augmented generation gives models sources they can cite, like footnotes in a research paper, so users can check any claims. That builds trust.

What’s more, the technique can help models clear up ambiguity in a user query. It also reduces the possibility that a model will give a very plausible but incorrect answer, a phenomenon called hallucination.

Another great advantage of RAG is it’s relatively easy. A [blog](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/) by Lewis and three of the paper’s coauthors said developers can implement the process with as few as [five lines of code](https://huggingface.co/facebook/rag-token-nq).

That makes the method faster and less expensive than retraining a model with additional datasets. And it lets users hot-swap new sources on the fly.

## **How People Are Using RAG**

With retrieval-augmented generation, users can essentially have conversations with data repositories, opening up new kinds of experiences. This means the applications for RAG could be multiple times the number of available datasets.

For example, a generative AI model supplemented with a medical index could be a great assistant for a doctor or nurse. Financial analysts would benefit from an assistant linked to market data.

In fact, almost any business can turn its technical or policy manuals, videos or logs into resources called knowledge bases that can enhance LLMs. These sources can enable use cases such as customer or field support, employee training and developer productivity.

The broad potential is why companies including [AWS](https://aws.amazon.com/blogs/machine-learning/simplify-access-to-internal-information-using-retrieval-augmented-generation-and-langchain-agents/), [IBM](https://research.ibm.com/blog/retrieval-augmented-generation-RAG), [Glean](https://www.glean.com/resources/guides/what-is-retrieval-augmented-generation-rag), [Google](https://cloud.google.com/use-cases/retrieval-augmented-generation?hl=en), [Microsoft](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), NVIDIA, [Oracle](https://www.oracle.com/artificial-intelligence/generative-ai/retrieval-augmented-generation-rag/) and [Pinecone](https://www.pinecone.io/learn/retrieval-augmented-generation/) are adopting RAG.

## **Getting Started With Retrieval-Augmented Generation**

The [NVIDIA AI Blueprint for RAG](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline) gives developers a foundational starting point for using NVIDIA NeMo Retriever models to build scalable, customizable data extraction and retrieval pipelines that deliver high accuracy and throughput.

The blueprint can be used as is, or combined with other [NVIDIA Blueprints](https://build.nvidia.com/blueprints) for advanced use cases including [AI agents for enterprise research](https://build.nvidia.com/nvidia/aiq) and [AI assistants for customer service](https://developer.nvidia.com/blog/three-building-blocks-for-creating-ai-virtual-assistants-for-customer-service-with-an-nvidia-nim-agent-blueprint/). For example, the [AI-Q NVIDIA Blueprint](https://build.nvidia.com/nvidia/aiq) enables developers to connect AI agents to enterprise data and use reasoning and tools to distill in-depth source materials with efficiency and precision.

In addition, developers and IT teams can use an [NVIDIA Launchable](https://brev.nvidia.com/launchable/deploy?launchableID=env-2uFJF22Hp8UdIVw0jRbHHYaixXx) to experiment with deploying a RAG pipeline. A significant part of this RAG pipeline is [NVIDIA NeMo Retriever](https://www.nvidia.com/en-us/ai-data-science/products/nemo/), which provides leading, large-scale retrieval accuracy, and [NVIDIA NIM](https://www.nvidia.com/en-us/ai/) microservices for simplifying secure, high-performance AI deployment across clouds, data centers and workstations. These are offered as part of the [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/) software platform for accelerating AI development and deployment.

Getting the best performance for RAG workflows requires massive amounts of memory and compute to move and process data. The [NVIDIA GH200 Grace Hopper Superchip](https://nvidianews.nvidia.com/news/gh200-grace-hopper-superchip-with-hbm3e-memory), with its 288GB of fast HBM3e memory and 8 petaflops of compute, is ideal — it can deliver a 150x speedup over using a CPU.

Once companies get familiar with RAG, they can combine a variety of off-the-shelf or custom LLMs with internal or external knowledge bases to create a wide range of assistants that help their employees and customers.

There are several environments to get started with RAG. [LLMs are debuting on Windows PCs](https://developer.nvidia.com/blog/supercharging-llm-applications-on-windows-pcs-with-nvidia-rtx-systems/), thanks to NVIDIA software that enables all sorts of applications users can access even on their laptops.

https://blogs.nvidia.com/wp-content/uploads/2023/11/Using-RAG-on-PCs.jpg An example application for RAG on a PC.

PCs equipped with NVIDIA RTX GPUs can now run some AI models locally. By using RAG on a PC, users can link to a private knowledge source – whether that be emails, notes or articles – to improve responses. The user can then feel confident that their data source, prompts and response all remain private and secure.

[This blog](https://blogs.nvidia.com/blog/tensorrt-llm-windows-stable-diffusion-rtx/) provides an example of RAG accelerated by TensorRT-LLM for Windows to get better results fast.

## **The History of RAG**

The roots of the technique go back at least to the early 1970s. That’s when researchers in information retrieval prototyped what they called question-answering systems, apps that use natural language processing ( [NLP](https://www.nvidia.com/en-us/glossary/natural-language-processing/)) to access text, initially in narrow topics such as baseball.

The concepts behind this kind of text mining have remained fairly constant over the years. But the machine learning engines driving them have grown significantly, increasing their usefulness and popularity.

In the mid-1990s, the Ask Jeeves service, now Ask.com, popularized question answering with its mascot of a well-dressed valet. IBM’s Watson became a TV celebrity in 2011 when it handily beat two human champions on the _Jeopardy!_ game show.

https://blogs.nvidia.com/wp-content/uploads/2023/11/Ask-Jeeves-2.jpg

Today, LLMs are taking question-answering systems to a whole new level.

## **Insights From a London Lab**

The seminal 2020 paper arrived as Lewis was pursuing a doctorate in NLP at University College London and working for Meta at a new London AI lab. The team was searching for ways to pack more knowledge into an LLM’s parameters and using a benchmark it developed to measure its progress.

Building on earlier methods and inspired by [a paper](https://arxiv.org/pdf/2002.08909.pdf) from Google researchers, the group “had this compelling vision of a trained system that had a retrieval index in the middle of it, so it could learn and generate any text output you wanted,” Lewis recalled.

https://blogs.nvidia.com/wp-content/uploads/2023/11/IBM-Watson-wins-Jeopardy-YT.jpg The IBM Watson question-answering system became a celebrity when it won big on the TV game show Jeopardy!

When Lewis plugged into the work in progress a promising retrieval system from another Meta team, the first results were unexpectedly impressive.

“I showed my supervisor and he said, ‘Whoa, take the win. This sort of thing doesn’t happen very often,’ because these workflows can be hard to set up correctly the first time,” he said.

Lewis also credits major contributions from team members Ethan Perez and Douwe Kiela, then of New York University and Facebook AI Research, respectively.

When complete, the work, which ran on a cluster of NVIDIA GPUs, showed how to make generative AI models more authoritative and [trustworthy](https://blogs.nvidia.com/blog/what-is-trustworthy-ai/). It’s since been cited by hundreds of papers that amplified and extended the concepts in what continues to be an active area of research.

## **How RAG Works**

At a high level, here’s [how RAG works](https://developer.nvidia.com/topics/ai/retrieval-augmented-generation).

When users ask an LLM a question, the AI model sends the query to another model that converts it into a numeric format so machines can read it. The numeric version of the query is sometimes called an embedding or a vector.

https://blogs.nvidia.com/wp-content/uploads/2025/01/llm-rag2.3-light-r3-scaled.pngIn retrieval-augmented generation, LLMs are enhanced with embedding and reranking models, storing knowledge in a vector database for precise query retrieval.

The embedding model then compares these numeric values to vectors in a machine-readable index of an available knowledge base. When it finds a match or multiple matches, it retrieves the related data, converts it to human-readable words and passes it back to the LLM.

Finally, the LLM combines the retrieved words and its own response to the query into a final answer it presents to the user, potentially citing sources the embedding model found.

## **Keeping Sources Current**

In the background, the embedding model continuously creates and updates machine-readable indices, sometimes called vector databases, for new and updated knowledge bases as they become available.

https://blogs.nvidia.com/wp-content/uploads/2023/11/LangChain-2-LLM-with-a-retriveal-process.jpg Retrieval-augmented generation combines LLMs with embedding models and vector databases.

Many developers find LangChain, an open-source library, can be particularly useful in chaining together LLMs, embedding models and knowledge bases. NVIDIA uses LangChain in its reference architecture for retrieval-augmented generation.

The LangChain community provides its own [description of a RAG process](https://blog.langchain.dev/tutorial-chatgpt-over-your-data/).

The future of generative AI lies in [agentic AI](https://blogs.nvidia.com/blog/what-is-agentic-ai/) — where LLMs and knowledge bases are dynamically orchestrated to create autonomous assistants. These AI-driven agents can enhance decision-making, adapt to complex tasks and deliver authoritative, verifiable results for users.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="build-advanced-retrieval-augmented-generation-systems.md">
<details>
<summary>Build advanced retrieval-augmented generation systems</summary>

Phase: [EXPLOITATION]

# Build advanced retrieval-augmented generation systems

**Source URL:** <https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation>

This article explains retrieval-augmented generation (RAG) and what developers need to build a production-ready RAG solution.

To learn about two ways to build a "chat over your data" app—one of the top generative AI use cases for businesses—see [Augment LLMs with RAG or fine-tuning](https://learn.microsoft.com/en-us/azure/developer/ai/augment-llm-rag-fine-tuning).

The following diagram shows the main steps of RAG:

https://learn.microsoft.com/en-us/azure/developer/ai/media/naive-rag-inference-pipeline-highres.png

This process is called _naive RAG_. It helps you understand the basic parts and roles in a RAG-based chat system.

Real-world RAG systems need more preprocessing and post-processing to handle articles, queries, and responses. The next diagram shows a more realistic setup, called _advanced RAG_:

https://learn.microsoft.com/en-us/azure/developer/ai/media/advanced-rag-inference-pipeline-highres.png

This article gives you a simple framework to understand the main phases in a real-world RAG-based chat system:

- Ingestion phase
- Inference pipeline phase
- Evaluation phase

## Ingestion

Ingestion means saving your organization's documents so you can quickly find answers for users. The main challenge is to find and use the parts of documents that best match each question. Most systems use vector embeddings and cosine similarity search to match questions to content. You get better results when you understand the content type (like patterns and format) and organize your data well in the vector database.

When setting up ingestion, focus on these steps:

- Content preprocessing and extraction
- Chunking strategy
- Chunking organization
- Update strategy

### Content preprocessing and extraction

The first step in the ingestion phase is to preprocess and extract the content from your documents. This step is crucial because it ensures that the text is clean, structured, and ready for indexing and retrieval.

Clean and accurate content makes a RAG-based chat system work better. Start by looking at the shape and style of the documents you want to index. Do they follow a set pattern, like documentation? If not, what questions could these documents answer?

At a minimum, set up your ingestion pipeline to:

- Standardize text formats
- Handle special characters
- Remove unrelated or old content
- Track different versions of content
- Handle content with tabs, images, or tables
- Extract metadata

Some of this information, like metadata, can help during retrieval and evaluation if you keep it with the document in the vector database. You can also combine it with the text chunk to improve the chunk's vector embedding.

### Chunking strategy

As a developer, decide how to break up large documents into smaller chunks. Chunking helps send the most relevant content to the LLM so it can answer user questions better. Also, think about how you'll use the chunks after you get them. Try out common industry methods and test your chunking strategy in your organization.

When chunking, think about:

- **Chunk size optimization**: Pick the best chunk size and how to split it—by section, paragraph, or sentence.
- **Overlapping and sliding window chunks**: Decide if chunks should be separate or overlap. You can also use a sliding window approach.
- **Small2Big**: If you split by sentence, organize the content so you can find nearby sentences or the full paragraph. Giving this extra context to the LLM can help it answer better. For more, see the next section.

### Chunking organization

In a RAG system, how you organize your data in the vector database makes it easier and faster to find the right information. Here are some ways to set up your indexes and searches:

- **Hierarchical indexes**: Use layers of indexes. A top-level summary index quickly finds a small set of likely chunks. A second-level index points to the exact data. This setup speeds up searches by narrowing down the options before looking in detail.
- **Specialized indexes**: Pick indexes that fit your data. For example, use graph-based indexes if your chunks connect to each other, like in citation networks or knowledge graphs. Use relational databases if your data is in tables, and filter with SQL queries.
- **Hybrid indexes**: Combine different indexing methods. For example, use a summary index first, then a graph-based index to explore connections between chunks.

### Alignment optimization

Make retrieved chunks more relevant and accurate by matching them to the types of questions they answer. One way is to create a sample question for each chunk that shows what question it answers best. This approach helps in several ways:

- **Improved matching**: During retrieval, the system compares the user’s question to these sample questions to find the best chunk. This technique improves the relevance of the results.
- **Training data for machine learning models**: These question-chunk pairs help train the machine learning models in the RAG system. The models learn which chunks answer which types of questions.
- **Direct query handling**: If a user’s question matches a sample question, the system can quickly find and use the right chunk, speeding up the response.

Each chunk’s sample question acts as a label that guides the retrieval algorithm. The search becomes more focused and aware of context. This method works well when chunks cover many different topics or types of information.

### Update strategies

If your organization updates documents often, you need to keep your database current so the retriever can always find the latest information. The _retriever component_ is the part of the system that searches the vector database and returns results. Here are some ways to keep your vector database up to date:

- **Incremental updates**:

  - **Regular intervals**: Set updates to run on a schedule (like daily or weekly) based on how often documents change. This action keeps the database fresh.
  - **Trigger-based updates**: Set up automatic updates when someone adds or changes a document. The system reindexes only the affected parts.
- **Partial updates**:

  - **Selective reindexing**: Update only the parts of the database that changed, not the whole thing. This technique saves time and resources, especially for large datasets.
  - **Delta encoding**: Store just the changes between old and new documents, which reduces the amount of data to process.
- **Versioning**:

  - **Snapshotting**: Save versions of your document set at different times. This action lets you go back or restore earlier versions if needed.
  - **Document version control**: Use a version control system to track changes and keep a history of your documents.
- **Real-time updates**:

  - **Stream processing**: Use stream processing to update the vector database in real time as documents change.
  - **Live querying**: Use live queries to get up-to-date answers, sometimes mixing live data with cached results for speed.
- **Optimization techniques**:

  - **Batch processing**: Group changes and apply them together to save resources and reduce overhead.
  - **Hybrid approaches**: Mix different strategies:

    - Use incremental updates for small changes.
    - Use full reindexing for significant updates.
    - Track and document major changes to your data.

Pick the update strategy or mix that fits your needs. Think about:

- Document corpus size
- Update frequency
- Real-time data needs
- Available resources

Review these factors for your application. Each method has trade-offs in complexity, cost, and how quickly updates show up.

## Inference pipeline

Your articles are now chunked, vectorized, and stored in a vector database. Next, focus on getting the best answers from your system.

To get accurate and fast results, think about these key questions:

- Is the user's question clear and likely to get the right answer?
- Does the question break any company rules?
- Can you rewrite the question to help the system find better matches?
- Do the results from the database match the question?
- Should you change the results before sending them to the LLM to make sure the answer is relevant?
- Does the LLM's answer fully address the user's question?
- Does the answer follow your organization's rules?

The whole inference pipeline works in real time. There’s no single right way to set up your preprocessing and post-processing steps. You use a mix of code and LLM calls. One of the biggest trade-offs is balancing accuracy and compliance with cost and speed.

Let’s look at strategies for each stage of the inference pipeline.

### Query preprocessing steps

Query preprocessing starts right after the user sends a question:

https://learn.microsoft.com/en-us/azure/developer/ai/media/advanced-rag-query-processing-steps-highres.png

These steps help make sure the user’s question fits your system and is ready to find the best article chunks using cosine similarity or "nearest neighbor" search.

**Policy check**: Use logic to spot and remove or flag unwanted content, like personal data, bad language, or attempts to break safety rules (called "jailbreaking").

**Query rewriting**: Change the question if needed—expand acronyms, remove slang, or rephrase it to focus on bigger ideas (step-back prompting).

A special version of step-back prompting is _Hypothetical Document Embeddings (HyDE)_. HyDE has the LLM answer the question, makes an embedding from that answer, and then searches the vector database with it.

### Subqueries

Subqueries break a long or complex question into smaller, easier questions. The system answers each small question, then combines the answers.

For example, if someone asks, "Who made more important contributions to modern physics, Albert Einstein or Niels Bohr?" you can split it into:

- **Subquery 1**: "What did Albert Einstein contribute to modern physics?"
- **Subquery 2**: "What did Niels Bohr contribute to modern physics?"

The answers might include:

- For Einstein: the theory of relativity, the photoelectric effect, and _E=mc^2_.
- For Bohr: the hydrogen atom model, work on quantum mechanics, and the principle of complementarity.

You can then ask follow-up questions:

- **Subquery 3**: "How did Einstein's theories change modern physics?"
- **Subquery 4**: "How did Bohr's theories change modern physics?"

These follow-ups look at each scientist’s effect, like:

- How Einstein’s work led to new ideas in cosmology and quantum theory
- How Bohr’s work helped us understand atoms and quantum mechanics

The system combines the answers to give a full response to the original question. This method makes complex questions easier to answer by breaking them into clear, smaller parts.

### Query router

Sometimes, your content lives in several databases or search systems. In these cases, use a query router. A _query router_ picks the best database or index to answer each question.

A query router works after the user asks a question but before the system searches for answers.

Here’s how a query router works:

1. **Query analysis**: The LLM or another tool looks at the question to figure out what kind of answer is needed.
2. **Index selection**: The router picks one or more indexes that fit the question. Some indexes are better for facts, others for opinions or special topics.
3. **Query dispatch**: The router sends the question to the chosen index or indexes.
4. **Results aggregation**: The system collects and combines the answers from the indexes.
5. **Answer generation**: The system creates a clear answer using the information it found.

Use different indexes or search engines for:

- **Data type specialization**: Some indexes focus on news, others on academic papers, or on special databases like medical or legal info.
- **Query type optimization**: Some indexes are fast for simple facts (like dates), while others handle complex or expert questions.
- **Algorithmic differences**: Different search engines use different methods, like vector search, keyword search, or advanced semantic search.

For example, in a medical advice system, you might have:

- A research paper index for technical details
- A case study index for real-world examples
- A general health index for basic questions

If someone asks about the effects of a new drug, the router sends the question to the research paper index. If the question is about common symptoms, it uses the general health index for a simple answer.

### Post-retrieval processing steps

Post-retrieval processing happens after the system finds content chunks in the vector database:

https://learn.microsoft.com/en-us/azure/developer/ai/media/advanced-rag-post-retrieval-processing-steps-highres.png

Next, check if these chunks are useful for the LLM prompt before sending them to the LLM.

Keep these things in mind:

- Extra information can hide the most important details.
- Irrelevant information can make the answer worse.

Watch out for the _needle in a haystack_ problem: LLMs often pay more attention to the start and end of a prompt than the middle.

Also, remember the LLM’s maximum context window and the number of tokens needed for long prompts, especially at scale.

To handle these issues, use a post-retrieval processing pipeline with steps like:

- **Filtering results**: Only keep chunks that match the query. Ignore the rest when building the LLM prompt.
- **Re-ranking**: Put the most relevant chunks at the beginning and end of the prompt.
- **Prompt compression**: Use a small, cheap model to summarize and combine chunks into a single prompt before sending it to the LLM.

### Post-completion processing steps

Post-completion processing happens after the user’s question and all content chunks go to the LLM:

https://learn.microsoft.com/en-us/azure/developer/ai/media/advanced-rag-post-completion-processing-steps-highres.png

After the LLM gives an answer, check its accuracy. A post-completion processing pipeline can include:

- **Fact check**: Look for statements in the answer that claim to be facts, then check if they’re true. If a fact check fails, you can ask the LLM again or show an error message.
- **Policy check**: Make sure the answer doesn’t include harmful content for the user or your organization.

## Evaluation

Evaluating a system like this is more complex than running regular unit or integration tests. Think about these questions:

- Are users happy with the answers?
- Are the answers accurate?
- How do you collect user feedback?
- Are there rules about what data you can collect?
- Can you see every step the system took when answers are wrong?
- Do you keep detailed logs for root cause analysis?
- How do you update the system without making things worse?

### Capturing and acting on feedback from users

Work with your organization's privacy team to design feedback capture tools, system data, and logging for forensics and root cause analysis of a query session.

The next step is to build an _assessment pipeline_. An assessment pipeline makes it easier and faster to review feedback and find out why the AI gave certain answers. Check every response to see how the AI produced it, if the right content chunks were used, and how the documents were split up.

Also, look for extra preprocessing or post-processing steps that could improve results. This close review often finds content gaps, especially when no good documentation exists for a user's question.

You need an assessment pipeline to handle these tasks at scale. A good pipeline uses custom tools to measure answer quality. It helps you see why the AI gave a specific answer, which documents it used, and how well the inference pipeline worked.

### Golden dataset

One way to check how well a RAG chat system works is to use a golden dataset. A _golden dataset_ is a set of questions with approved answers, helpful metadata (like topic and question type), links to source documents, and different ways users might ask the same thing.

A golden dataset shows the "best case scenario." Developers use it to see how well the system works and to run tests when they add new features or updates.

### Assessing harm

Harms modeling helps you spot possible risks in a product and plan ways to reduce them.

A harms assessment tool should include these key features:

- **Stakeholder identification**: Helps you list and group everyone affected by the technology, including direct users, people affected indirectly, future generations, and even the environment.
- **Harm categories and descriptions**: Lists possible harms, like privacy loss, emotional distress, or economic harm. Guides you through examples and helps you think about both expected and unexpected problems.
- **Severity and probability assessments**: Helps you judge how serious and likely each harm is, so you can decide what to fix first. You can use data to support your choices.
- **Mitigation strategies**: Suggests ways to reduce risks, like changing the system design, add safeguards, or use other technology.
- **Feedback mechanisms**: Lets you collect feedback from stakeholders so you can keep improving the process as you learn more.
- **Documentation and reporting**: Makes it easy to create reports that show what you found and what you did to reduce risks.

These features help you find and fix risks, and they also help you build more ethical and responsible AI by thinking about all possible impacts from the start.

For more information, see these articles:

- [Foundations of assessing harm](https://learn.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/harms-modeling/)
- [Types of harm](https://learn.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/harms-modeling/type-of-harm)

### Testing and verifying the safeguards

_Red-teaming_ is key—it means to act like an attacker to find weak spots in the system. This step is especially important to stop jailbreaking. For tips on planning and managing red teaming for responsible AI, see [Planning red teaming for large language models (LLMs) and their applications](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/red-teaming?view=foundry&preserve-view=true).

Developers should test RAG system safeguards in different scenarios to make sure they work. This step makes the system stronger and also helps fine-tune responses to follow ethical standards and rules.

## Final considerations for application design

Here are some key things to remember from this article that can help you design your app:

- Generative AI unpredictability
- User prompt changes and their effect on time and cost
- Parallel LLM requests for faster performance

To build a generative AI app, check out [Get started with chat by using your own data sample for Python](https://learn.microsoft.com/en-us/azure/developer/python/get-started-app-chat-template?tabs=github-codespaces). The tutorial is also available for [.NET](https://learn.microsoft.com/en-us/dotnet/ai/get-started-app-chat-template?tabs=github-codespaces), [Java](https://learn.microsoft.com/en-us/azure/developer/java/ai/get-started-app-chat-template?tabs=github-codespaces), and [JavaScript](https://learn.microsoft.com/en-us/azure/developer/javascript/get-started-app-chat-template?tabs=github-codespaces).

**Note:** The author created this article with assistance from AI. [Learn more](https://learn.microsoft.com/principles-for-ai-generated-content)

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="introducing-contextual-retrieval.md">
<details>
<summary>Introducing Contextual Retrieval</summary>

Phase: [EXPLOITATION]

# Introducing Contextual Retrieval

**Source URL:** <https://www.anthropic.com/news/contextual-retrieval>

Published Sep 19, 2024

For an AI model to be useful in specific contexts, it often needs access to background knowledge.

For an AI model to be useful in specific contexts, it often needs access to background knowledge. For example, customer support chatbots need knowledge about the specific business they're being used for, and legal analyst bots need to know about a vast array of past cases.

Developers typically enhance an AI model's knowledge using Retrieval-Augmented Generation (RAG). RAG is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt, significantly enhancing the model's response. The problem is that traditional RAG solutions remove context when encoding information, which often results in the system failing to retrieve the relevant information from the knowledge base.

In this post, we outline a method that dramatically improves the retrieval step in RAG. The method is called “Contextual Retrieval” and uses two sub-techniques: Contextual Embeddings and Contextual BM25. This method can reduce the number of failed retrievals by 49% and, when combined with reranking, by 67%. These represent significant improvements in retrieval accuracy, which directly translates to better performance in downstream tasks.

You can easily deploy your own Contextual Retrieval solution with Claude with [our cookbook](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide).

### A note on simply using a longer prompt

Sometimes the simplest solution is the best. If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods.

A few weeks ago, we released [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) for Claude, which makes this approach significantly faster and more cost-effective. Developers can now cache frequently used prompts between API calls, reducing latency by > 2x and costs by up to 90% (you can see how it works by reading our [prompt caching cookbook](https://platform.claude.com/cookbook/misc-prompt-caching)).

However, as your knowledge base grows, you'll need a more scalable solution. That’s where Contextual Retrieval comes in.

## A primer on RAG: scaling to larger knowledge bases

For larger knowledge bases that don't fit within the context window, RAG is the typical solution. RAG works by preprocessing a knowledge base using the following steps:

1. Break down the knowledge base (the “corpus” of documents) into smaller chunks of text, usually no more than a few hundred tokens;
2. Use an embedding model to convert these chunks into vector embeddings that encode meaning;
3. Store these embeddings in a vector database that allows for searching by semantic similarity.

At runtime, when a user inputs a query to the model, the vector database is used to find the most relevant chunks based on semantic similarity to the query. Then, the most relevant chunks are added to the prompt sent to the generative model.

While embedding models excel at capturing semantic relationships, they can miss crucial exact matches. Fortunately, there’s an older technique that can assist in these situations. BM25 (Best Matching 25) is a ranking function that uses lexical matching to find precise word or phrase matches. It's particularly effective for queries that include unique identifiers or technical terms.

BM25 works by building upon the TF-IDF (Term Frequency-Inverse Document Frequency) concept. TF-IDF measures how important a word is to a document in a collection. BM25 refines this by considering document length and applying a saturation function to term frequency, which helps prevent common words from dominating the results.

Here’s how BM25 can succeed where semantic embeddings fail: Suppose a user queries "Error code TS-999" in a technical support database. An embedding model might find content about error codes in general, but could miss the exact "TS-999" match. BM25 looks for this specific text string to identify the relevant documentation.

RAG solutions can more accurately retrieve the most applicable chunks by combining the embeddings and BM25 techniques using the following steps:

1. Break down the knowledge base (the "corpus" of documents) into smaller chunks of text, usually no more than a few hundred tokens;
2. Create TF-IDF encodings and semantic embeddings for these chunks;
3. Use BM25 to find top chunks based on exact matches;
4. Use embeddings to find top chunks based on semantic similarity;
5. Combine and deduplicate results from (3) and (4) using rank fusion techniques;
6. Add the top-K chunks to the prompt to generate the response.

By leveraging both BM25 and embedding models, traditional RAG systems can provide more comprehensive and accurate results, balancing precise term matching with broader semantic understanding.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F45603646e979c62349ce27744a940abf30200d57-3840x2160.png&w=3840&q=75A Standard Retrieval-Augmented Generation (RAG) system that uses both embeddings and Best Match 25 (BM25) to retrieve information. TF-IDF (term frequency-inverse document frequency) measures word importance and forms the basis for BM25.

This approach allows you to cost-effectively scale to enormous knowledge bases, far beyond what could fit in a single prompt. But these traditional RAG systems have a significant limitation: they often destroy context.

### The context conundrum in traditional RAG

In traditional RAG, documents are typically split into smaller chunks for efficient retrieval. While this approach works well for many applications, it can lead to problems when individual chunks lack sufficient context.

For example, imagine you had a collection of financial information (say, U.S. SEC filings) embedded in your knowledge base, and you received the following question: _"What was the revenue growth for ACME Corp in Q2 2023?"_

A relevant chunk might contain the text: _"The company's revenue grew by 3% over the previous quarter."_ However, this chunk on its own doesn't specify which company it's referring to or the relevant time period, making it difficult to retrieve the right information or use the information effectively.

## Introducing Contextual Retrieval

Contextual Retrieval solves this problem by prepending chunk-specific explanatory context to each chunk before embedding (“Contextual Embeddings”) and creating the BM25 index (“Contextual BM25”).

Let’s return to our SEC filings collection example. Here's an example of how a chunk might be transformed:

```
original_chunk = "The company's revenue grew by 3% over the previous quarter."

contextualized_chunk = "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."
```

It is worth noting that other approaches to using context to improve retrieval have been proposed in the past. Other proposals include: [adding generic document summaries to chunks](https://aclanthology.org/W02-0405.pdf) (we experimented and saw very limited gains), [hypothetical document embedding](https://arxiv.org/abs/2212.10496), and [summary-based indexing](https://www.llamaindex.ai/blog/a-new-document-summary-index-for-llm-powered-qa-systems-9a32ece2f9ec) (we evaluated and saw low performance). These methods differ from what is proposed in this post.

### Implementing Contextual Retrieval

Of course, it would be far too much work to manually annotate the thousands or even millions of chunks in a knowledge base. To implement Contextual Retrieval, we turn to Claude. We’ve written a prompt that instructs the model to provide concise, chunk-specific context that explains the chunk using the context of the overall document. We used the following Claude 3 Haiku prompt to generate context for each chunk:

```
<document>
{{WHOLE_DOCUMENT}}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{{CHUNK_CONTENT}}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else.
```

The resulting contextual text, usually 50-100 tokens, is prepended to the chunk before embedding it and before creating the BM25 index.

Here’s what the preprocessing flow looks like in practice:

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2496e7c6fedd7ffaa043895c23a4089638b0c21b-3840x2160.png&w=3840&q=75_Contextual Retrieval is a preprocessing technique that improves retrieval accuracy._

If you’re interested in using Contextual Retrieval, you can get started with [our cookbook](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide).

### Using Prompt Caching to reduce the costs of Contextual Retrieval

Contextual Retrieval is uniquely possible at low cost with Claude, thanks to the special prompt caching feature we mentioned above. With prompt caching, you don’t need to pass in the reference document for every chunk. You simply load the document into the cache once and then reference the previously cached content. Assuming 800 token chunks, 8k token documents, 50 token context instructions, and 100 tokens of context per chunk, **the one-time cost to generate contextualized chunks is $1.02 per million document tokens**.

#### Methodology

We experimented across various knowledge domains (codebases, fiction, ArXiv papers, Science Papers), embedding models, retrieval strategies, and evaluation metrics. We’ve included a few examples of the questions and answers we used for each domain in [Appendix II](https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf).

The graphs below show the average performance across all knowledge domains with the top-performing embedding configuration (Gemini Text 004) and retrieving the top-20-chunks. We use 1 minus recall@20 as our evaluation metric, which measures the percentage of relevant documents that fail to be retrieved within the top 20 chunks. You can see the full results in the appendix - contextualizing improves performance in every embedding-source combination we evaluated.

#### Performance improvements

Our experiments showed that:

- **Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35%** (5.7% → 3.7%).
- **Combining Contextual Embeddings and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 49%** (5.7% → 2.9%).

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7f8d739e491fe6b3ba0e6a9c74e4083d760b88c9-3840x2160.png&w=3840&q=75_Combining Contextual Embedding and Contextual BM25 reduce the top-20-chunk retrieval failure rate by 49%._

#### Implementation considerations

When implementing Contextual Retrieval, there are a few considerations to keep in mind:

1. **Chunk boundaries:** Consider how you split your documents into chunks. The choice of chunk size, chunk boundary, and chunk overlap can affect retrieval performance1.
2. **Embedding model:** Whereas Contextual Retrieval improves performance across all embedding models we tested, some models may benefit more than others. We found [Gemini](https://ai.google.dev/gemini-api/docs/embeddings) and [Voyage](https://www.voyageai.com/) embeddings to be particularly effective.
3. **Custom contextualizer prompts:** While the generic prompt we provided works well, you may be able to achieve even better results with prompts tailored to your specific domain or use case (for example, including a glossary of key terms that might only be defined in other documents in the knowledge base).
4. **Number of chunks:** Adding more chunks into the context window increases the chances that you include the relevant information. However, more information can be distracting for models so there's a limit to this. We tried delivering 5, 10, and 20 chunks, and found using 20 to be the most performant of these options (see appendix for comparisons) but it’s worth experimenting on your use case.

**Always run evals:** Response generation may be improved by passing it the contextualized chunk and distinguishing between what is context and what is the chunk.

## Further boosting performance with Reranking

In a final step, we can combine Contextual Retrieval with another technique to give even more performance improvements. In traditional RAG, the AI system searches its knowledge base to find the potentially relevant information chunks. With large knowledge bases, this initial retrieval often returns a lot of chunks—sometimes hundreds—of varying relevance and importance.

Reranking is a commonly used filtering technique to ensure that only the most relevant chunks are passed to the model. Reranking provides better responses and reduces cost and latency because the model is processing less information. The key steps are:

1. Perform initial retrieval to get the top potentially relevant chunks (we used the top 150);
2. Pass the top-N chunks, along with the user's query, through the reranking model;
3. Using a reranking model, give each chunk a score based on its relevance and importance to the prompt, then select the top-K chunks (we used the top 20);
4. Pass the top-K chunks into the model as context to generate the final result.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8f82c6175a64442ceff4334b54fac2ab3436a1d1-3840x2160.png&w=3840&q=75_Combine Contextual Retrieva and Reranking to maximize retrieval accuracy._

### Performance improvements

There are several reranking models on the market. We ran our tests with the [Cohere reranker](https://cohere.com/rerank). Voyage [also offers a reranker](https://docs.voyageai.com/docs/reranker), though we did not have time to test it. Our experiments showed that, across various domains, adding a reranking step further optimizes retrieval.

Specifically, we found that Reranked Contextual Embedding and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 67% (5.7% → 1.9%).

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F93a70cfbb7cca35bb8d86ea0a23bdeeb699e8e58-3840x2160.png&w=3840&q=75_Reranked Contextual Embedding and Contextual BM25 reduces the top-20-chunk retrieval failure rate by 67%._

#### Cost and latency considerations

One important consideration with reranking is the impact on latency and cost, especially when reranking a large number of chunks. Because reranking adds an extra step at runtime, it inevitably adds a small amount of latency, even though the reranker scores all the chunks in parallel. There is an inherent trade-off between reranking more chunks for better performance vs. reranking fewer for lower latency and cost. We recommend experimenting with different settings on your specific use case to find the right balance.

## Conclusion

We ran a large number of tests, comparing different combinations of all the techniques described above (embedding model, use of BM25, use of contextual retrieval, use of a reranker, and total # of top-K results retrieved), all across a variety of different dataset types. Here’s a summary of what we found:

1. Embeddings+BM25 is better than embeddings on their own;
2. Voyage and Gemini have the best embeddings of the ones we tested;
3. Passing the top-20 chunks to the model is more effective than just the top-10 or top-5;
4. Adding context to chunks improves retrieval accuracy a lot;
5. Reranking is better than no reranking;
6. **All these benefits stack**: to maximize performance improvements, we can combine contextual embeddings (from Voyage or Gemini) with contextual BM25, plus a reranking step, and adding the 20 chunks to the prompt.

We encourage all developers working with knowledge bases to use [our cookbook](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide) to experiment with these approaches to unlock new levels of performance.

## Appendix I

Below is a breakdown of results across datasets, embedding providers, use of BM25 in addition to embeddings, use of contextual retrieval, and use of reranking for Retrievals @ 20.

See [Appendix II](https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf) for the breakdowns for Retrievals @ 10 and @ 5 as well as example questions and answers for each dataset.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F646a894ec4e6120cade9951a362f685cd2ec89b2-2458x2983.png&w=3840&q=75_1 minus recall @ 20 results across data sets and embedding providers._

## Acknowledgements

Research and writing by Daniel Ford. Thanks to Orowa Sikder, Gautam Mittal, and Kenneth Lien for critical feedback, Samuel Flamini for implementing the cookbooks, Lauren Polansky for project coordination and Alex Albert, Susan Payne, Stuart Ritchie, and Brad Abrams for shaping this blog post.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="rag-is-dead-long-live-agentic-retrieval.md">
<details>
<summary>RAG is dead, long live agentic retrieval</summary>

Phase: [EXPLOITATION]

# RAG is dead, long live agentic retrieval

**Source URL:** <https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval>

https://cdn.sanity.io/images/7m9jw85w/production/9fdb15bafdf8c0921f36c6cd8cdac43c8ca87e27-2232x1562.png?w=2232

RAG has come a long way since the days of naive chunk retrieval; now agentic strategies are table stakes.

Nowadays, an AI engineer has to be aware of a plethora of techniques and terminology that encompass the data-retrieval aspects of agentic systems: hybrid search, CRAG, Self-RAG, HyDE, deep research, reranking, multi-modal embeddings, and RAPTOR just to name a few.

As we’ve built the Retrieval services in LlamaParse, we’ve chosen to abstract a few of these techniques into our API, only exposing a few top-level hyper-parameters for controlling these algorithms. In this blog post, we will showcase these various techniques, explaining how and when to use them. We will build upon these techniques one by one and end with a fully agentic retrieval system that can intelligently query multiple knowledge bases at once.

## Starting with the basics

You can’t talk about RAG without talking about “naive top-k retrieval”. In this basic approach, document chunks are stored in a vector database, and query embeddings are matched with the `k` most similar chunk embeddings.

https://cdn.sanity.io/images/7m9jw85w/production/188534199027c3232c2c49248b0099295ddce603-576x1210.pngNaive top-k RAG

Here’s a basic code snippet to index a simple folder of PDFs:

```
import os
from llama_index.indices.managed.llama_cloud import LlamaParseIndex
# ^ pip install llama-index-indices-managed-llama-cloud

financial_index = LlamaParseIndex.from_documents(
    documents=[],  # leave documents empty since we will be uploading the raw files
    name="Financial Reports",
    project_name=project_name,
)

financial_reports_directory = "./data/financial_reports"
for file_name in os.listdir(financial_reports_directory):
    file_path = os.path.join(financial_reports_directory, file_name)
    # Add each file to the slides index
    financial_index.upload_file(file_path, wait_for_ingestion=False)

financial_index.wait_for_completion()
```

Once this is indexing is completed, you can start retrieving these chunks with one more line:

```
query = "Where is Microsoft headquartered?"
nodes = financial_index.as_retriever().retrieve(query)
# or, if you've set up the Settings object, generate the full response here
response = financial_index.as_query_engine().query(query)
```

Going slightly beyond this naive `chunk` retrieval mode, there are also two more modes if you want to retrieve the entire contents of relevant files:

- `files_via_metadata` \- use this mode when you want to handle queries where a specific filename or pathname is mentioned e.g. “What does the 2024\_MSFT\_10K.pdf file say about the financial outlook of MSFT?”.
- `files_via_content` \- use this mode when you want to handle queries that are asking general questions about a topic but not a particular set of files e.g. “What is the financial outlook of MSFT?”.

https://cdn.sanity.io/images/7m9jw85w/production/3e6e040367e14d6b7133820e26531396fa8c1fdd-1072x624.pngMultiple retrieval modes

While `chunk` retrieval is the default mode, you can use one of the other retrieval modes via the `retrieval_mode` kwarg:

```
files_via_metadata_nodes = financial_index.as_retriever(retrieval_mode="files_via_metadata").retrieve(query)
files_via_content_nodes = financial_index.as_retriever(retrieval_mode="files_via_content").retrieve(query)
```

## Level up: Auto Mode

Now that we have an understanding how and when to use each of our retrieval modes, you’re now equipped with the power to answer any and all of types of questions about your knowledge base!

However, many applications will not know which type of question is being asked beforehand. Most of the time, these questions are being asked by your end user. You will need a way to know which retrieval mode would be most appropriate for the given query.

Enter the 4th retrieval mode - `auto_routed` mode! As the name suggests, this mode uses a lightweight agent to determine which of the other 3 retrieval modes to use for a given query.

https://cdn.sanity.io/images/7m9jw85w/production/c2d0bd793627f4d38e93491cfe51ba0f8bad09a5-1316x1050.pngAgentically auto-routed retrieval

Using this mode is just as simple as using any of the other modes:

```
nodes = financial_index.as_retriever(retrieval_mode="auto_routed").retrieve("Where is Microsoft headquartered?")
# you can check which mode the query was routed to via the retrieval_mode metadata value
# this will print "chunks" since the input query is asking about specific information
print(nodes[0].metadata["retrieval_mode"])
```

## Expanding Beyond a single knowledge base

With the use of `auto_routed` mode, we have a lightweight agentic system that is capable of competently answering a variety of questions. However, this system is somewhat restricted in terms of its search space - it is only able to retrieve data that has been ingested in a single index.

If all of your documents are of the same format (e.g. they’re all just SEC 10K filings), it may be actually be appropriate for you to just ingest all your documents through a single index. The parsing and chunking configurations on that single index can be highly optimized to fit the formatting of this homogenous set of documents. However, your overall knowledge base will surely encompass a wide variety of file formats - SEC Filings, Meeting notes, Customer Service requests, etc. These other formats will necessitate the setup of separate indices whose parsing & chunking settings are optimized to each subset of documents.

Let’s say you have your SEC filings in the `financial_index` from the prior code snippets, and additionally have created a `slides_index` that has ingested `.ppt` PowerPoint files from a folder of slide shows.

```
import os
from llama_index.indices.managed.llama_cloud import LlamaParseIndex
# ^ pip install llama-index-indices-managed-llama-cloud

slides_index = LlamaParseIndex.from_documents(
    documents=[],  # leave documents empty since we will be uploading the raw files
    name="Slides",
    project_name=project_name,
)

# Add your slide files to the index
slides_directory = "./data/slides"
for file_name in os.listdir(slides_directory):
    file_path = os.path.join(slides_directory, file_name)
    # Add each file to the slides index
    slides_index.upload_file(file_path, wait_for_ingestion=False)
```

Your application may now have users asking questions about the SEC Filings you’ve ingested in `financial_index` & the meeting slide shows you’ve ingested in `slides_index` .

This is where our Composite Retrieval APIs shine! They provide a single Retrieval API to retrieve relevant content from many indices - not just one. The Composite Retrieval API exposes a lightweight agent layer to clients to allow them to specify a name & description for each sub-index. These parameters can help you control how the agent decides to route a question between the various indices you’ve added to your composite retriever.

```
from llama_cloud import CompositeRetrievalMode
from llama_index.indices.managed.llama_cloud import LlamaParseCompositeRetriever

composite_retriever = LlamaParseCompositeRetriever(
    name="My App Retriever",
    project_name=project_name,
    # If a Retriever named "My App Retriever" doesn't already exist, one will be created
    create_if_not_exists=True,
    # CompositeRetrievalMode.ROUTED will query route the query to a subset of indices
    mode=CompositeRetrievalMode.ROUTED,
    # return the top 5 results from all queried indices
    rerank_top_n=5,
)

# Add the above indices to the composite retriever
# Carefully craft the description as this is used internally to route a query to an attached sub-index when CompositeRetrievalMode.ROUTING is used
composite_retriever.add_index(
    slides_index,
    description="Information source for slide shows presented during team meetings",
)
composite_retriever.add_index(
    financial_index,
    description="Information source for company financial reports",
)

# Start querying across both of these indices at once
nodes = retriever.retrieve("What was the key feature of the highest revenue product in 2024 Q4?")
```

## Piecing Together a Knowledge Agent

Now that we know how to use agents for both individual and multi-index level, we can put together a single system that does agentic retrieval at every step of retrieval! Doing so will enable the use of an LLM to optimize every layer of our search path.

The system works like this:

1. At the top layer, the composite retriever uses LLM-based classification to decide which sub-index (or indices) are relevant for the given query.
2. At the sub-index level, the `auto_routed` retrieval mode determines the most appropriate retrieval method (e.g., `chunk` , `files_via_metadata` , or `files_via_content` ) for the query.

https://cdn.sanity.io/images/7m9jw85w/production/9fdb15bafdf8c0921f36c6cd8cdac43c8ca87e27-2232x1562.pngRetrieval routed agentically across multiple auto-routed indexes

Here’s the code implementation:

```
from llama_cloud import CompositeRetrievalMode
from llama_index.indices.managed.llama_cloud import LlamaParseCompositeRetriever

# Create a composite retriever
composite_retriever = LlamaParseCompositeRetriever(
    name="Knowledge Agent",
    project_name=project_name,
    create_if_not_exists=True,
    mode=CompositeRetrievalMode.ROUTED,  # Use routed mode for intelligent index selection
    rerank_top_n=5,  # Rerank and return the top 5 results
)

# Add sub-indices with detailed descriptions
composite_retriever.add_index(
    financial_index,
    description="Detailed financial reports, including SEC filings and revenue analysis",
)
composite_retriever.add_index(
    slides_index,
    description="Slide shows from team meetings, covering product updates and project insights",
)

# Query the composite retriever
query = "What does the Q4 2024 financial report say about revenue growth?"
nodes = composite_retriever.retrieve(query)

# Print the retrieval mode used for the query and the results
for node in nodes:
    print(f"Retrieved from: {node.metadata['retrieval_mode']} - {node.text}")
```

This setup ensures that retrieval decisions are intelligently routed at each layer, using LLM-based classification to handle complex queries across multiple indices and retrieval modes. The result is a fully agentic retrieval system capable of adapting dynamically to diverse user queries.

### Naive RAG is dead, agentic retrieval is the future

Agents have become an essential part of modern applications. For these agents to operate effectively and autonomously, they need precise and relevant context at their fingertips. This is why sophisticated data retrieval is crucial for any agent-based system. LlamaParse serves as the backbone for these intelligent systems, providing reliable, accurate context when and where agents need it most.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="the-rise-of-rag.md">
<details>
<summary>The Rise of RAG</summary>

Phase: [EXPLOITATION]

# The Rise of RAG

**Source URL:** <https://highlearningrate.substack.com/p/the-rise-of-rag>

### Making LLMs More Reliable Through Additional Information

Louis-François Bouchard, Francois Huppe-Marcoux, and Omar Solano

Oct 31, 2024

Good morning everyone! In this iteration, we go back to the basics and explore the popular method called retrieval augmented generation (RAG), introduced by a Meta [paper](https://arxiv.org/abs/2005.11401) in 2020. In one line: RAG answers the known limitations of LLMs, such as non-access to up-to-date information and hallucinations.

Let’s dive into what it really is (simpler than you think), how it works, and when to use it (or not)!

## Understanding RAG

RAG is conceptually simple: It improves LLM responses by adding relevant information to the context window—something the model wouldn't otherwise know. Think of it as giving the LLM access to a vast, curated library of information it can reference in real-time.

A RAG system has two parts. The first is **retrieval**, where we find the most relevant information given a context (the user prompt). The second part is **generation**, where an LLM resolves the user’s request by leveraging the retrieved information as the source. With a good enough LLM, this generation step is straightforward: you combine the retrieved information with the user prompt, and voilà—the LLM produces the response. RAG's “tricky” part is retrieving correct and useful information.

By the way, this concept of search/retrieval is nothing new. There’s been extensive research on retrieval techniques over the years, and you're probably already familiar with this idea—you’ve likely used it every time you search on Google!

A satisfactory RAG system must analyze user prompts and retrieve precisely pertinent information from external sources, such as documents, databases, or multimedia content. This retrieval challenge differentiates a bad RAG implementation from one that provides value to users.

https://substackcdn.com/image/fetch/$s_!vT0-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb26de1d-ca6f-4722-adc3-87c0b18e9c2c_2934x1524.png

## Why RAG Matters

By providing LLMs with accurate, relevant information, we improve their ability to generate helpful responses. LLMs are powerful and somewhat intelligent, but they are not accurate sources of knowledge we can blindly trust. At the beginning of the ChatGPT release, there was a [case](https://www.forbes.com/sites/mattnovak/2023/05/27/lawyer-uses-chatgpt-in-federal-court-and-it-goes-horribly-wrong/) where a lawyer cited fictive instances generated by the model in court. Now we know (hopefully) that this is bad!

The RAG approach effectively addresses the two critical limitations of traditional LLMs: knowledge cutoff dates and hallucinations. When an LLM needs to discuss recent events or specific documents, RAG ensures it's working with factual, verifiable information rather than potentially outdated or incorrect knowledge from its training data. Using RAG allows us to leverage an LLM best to manipulate and use language vs. use it to memorize facts. Moreover, RAG enables something important in professional contexts: the ability to cite sources, making responses both traceable and credible.

## Under the Hood: How RAG Works

Much of the work happens in the retrieval component of RAG. The most common approach for unstructured data like PDFs or web content is chunk-based retrieval using semantic similarity—where documents are split into smaller pieces (chunks), converted into numerical representations (embeddings), and then compared mathematically with the user's query embedding to find the most relevant pieces mathematically (semantic similarity).

This can be enhanced through various sophisticated techniques:

- Hierarchical chunking for better context preservation- creates a multi-level structure of chunks (e.g., paragraphs within sections) to maintain broader document context

- Metadata filtering for more precise results - uses document properties like date, author, or category to narrow down the search space before semantic comparison.

- Hybrid search combining traditional methods such as BM25 with semantic similarity - merges keyword-based search with semantic search to leverage the strengths of both approaches

- [Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) that considers the full query context - enhances each chunk by automatically generating and appending additional context about how the chunk fits within the broader document before creating its embedding.

- Custom-trained embedding models and rerankers - fine-tunes embedding models on domain-specific data and uses additional models to re-score initial search results for better accuracy

- [GraphRAG](https://highlearningrate.substack.com/p/should-you-be-using-graphrag) \- introduces knowledge graphs into the retrieval process. Instead of relying solely on vector similarity (comparing numbers to find the most relevant ‘similar’ matches), GraphRAG extracts entities and relationships from your data, creating a structured representation that captures semantic connections.


For structured data, RAG can leverage text-to-SQL approaches, ranging from constrained query generation to full-fledged SQL synthesis. Semantic similarity search, implemented through tools like PGVector, enables efficient retrieval from structured databases.

The effectiveness of these retrieval systems isn't left to chance. We must measure performance through metrics like recall, hit rate, and mean reciprocal rank. Read our iteration on [RAG Evaluation](https://highlearningrate.substack.com/p/rag-evaluation) to learn more about them. However, the actual test lies in user satisfaction – leading organizations increasingly track user feedback to ensure their RAG systems truly enhance the user experience.

## RAG vs. Long Context

As we addressed in a [previous iteration](https://highlearningrate.substack.com/p/the-death-of-rag), while some argue that increasing context windows (like Gemini's 1.5 Flash and Pro, 2M tokens context window) might obviate the need for RAG, the reality is more nuanced. RAG offers several advantages over simply increasing context length by retrieving specific information rather than processing vast amounts of text and enhancing efficiency and speed.

RAG shines when (1) dealing with **large datasets**, (2) where **processing time** is critical, and (3) when the application needs to be **cost-effective**. This is especially important when utilizing an LLM through an API, as sending millions of tokens for every request to provide context can be expensive. In contrast, retrieval is highly efficient and cheap, allowing you to send just the right bits of information to your LLM.

## The Future of RAG: Toward Intelligent Information Retrieval

The next frontier in RAG development lies in handling complex queries through what we might call "agentic" LLM applications. These systems can decompose complex queries into smaller components, launching multiple retrieval processes in parallel or sequence to gather comprehensive information. Ideally, automatically identifying if relevant information is missing before responding to reduce hallucinations. This approach mimics how a human researcher might break down a complex question into smaller, manageable research tasks.

Such systems represent a significant step toward more sophisticated information retrieval and synthesis, potentially revolutionizing how we interact with knowledge bases and document collections.

## Conclusion

RAG isn't just another technical innovation—it's a fundamental shift in approaching AI-powered information coupling retrieval and generation. By bridging the gap between LLMs and real-world knowledge bases, RAG is helping create more reliable, trustworthy, and useful AI systems. As we continue to push the boundaries of what's possible with LLMs, RAG will undoubtedly play a crucial role in shaping the future of AI-powered information systems.

#### Discussion about this post

CommentsRestacks

[https://substackcdn.com/image/fetch/$s_!kp97!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83e3e9a7-050c-4966-9734-06564009caf8_256x256.jpeg](https://substack.com/profile/30421304-jp?utm_source=comment)

[JP](https://substack.com/profile/30421304-jp?utm_source=substack-feed-item)

[Mar 1](https://highlearningrate.substack.com/p/the-rise-of-rag/comment/221329035 "Mar 1, 2026, 5:07 AM")

The rise might be plateauing. Anthropic recently published how they designed Claude Code's tools. They tried RAG for codebase understanding and it failed them. Retrieval was fragile, and the model understood code better when it searched for context itself using grep. As models get more capable, the need to pre-chew their context shrinks. Covered their findings here: [https://reading.sh/anthropic-revealed-how-they-build-claude-codes-brain-11e48e75fd01?sk=6662727c70ed637cd1692a81f33139e2](https://reading.sh/anthropic-revealed-how-they-build-claude-codes-brain-11e48e75fd01?sk=6662727c70ed637cd1692a81f33139e2)

Like

Reply

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="what-is-agentic-rag-1.md">
<details>
<summary>What is agentic RAG?</summary>

Phase: [EXPLOITATION]

# What is agentic RAG?

**Source URL:** <https://www.ibm.com/think/topics/agentic-rag>

- [Agentic RAG vs. traditional RAG systems](https://www.ibm.com/think/topics/agentic-rag#Agentic+RAG+vs.+traditional+RAG+systems)
- [How does agentic RAG work?](https://www.ibm.com/think/topics/agentic-rag#How+does+agentic+RAG+work%3F)
- [Agentic RAG use cases](https://www.ibm.com/think/topics/agentic-rag#Agentic+RAG+use cases)

## Authors

https://assets.ibm.com/is/image/ibm/ivan-1?wid=128

[Ivan Belcic](https://www.ibm.com/think/author/ivan-belcic)

Staff writer

https://www.ibm.com/adobe/dynamicmedia/deliver/dm-aid--6ffe6fc8-d405-4a89-ad05-780d6960d862/cole-stryker-2x.jpg?preferwebp=true&width=128

[Cole Stryker](https://www.ibm.com/think/author/cole-stryker.html)

Staff Editor, AI Models

IBM Think

Agentic RAG is the use of [AI agents](https://www.ibm.com/think/topics/ai-agents) to facilitate [retrieval augmented generation (RAG)](https://www.ibm.com/think/topics/retrieval-augmented-generation). Agentic RAG systems add AI agents to the RAG pipeline to increase adaptability and accuracy. Compared to traditional RAG systems, agentic RAG allows [large language models (LLMs)](https://www.ibm.com/think/topics/large-language-models) to conduct [information retrieval](https://www.ibm.com/think/topics/information-retrieval) from multiple sources and handle more complex [workflows](https://www.ibm.com/think/topics/workflow).

### What is RAG?

Retrieval augmented generation is an [artificial intelligence (AI)](https://www.ibm.com/think/topics/artificial-intelligence) application that connects a [generative AI](https://www.ibm.com/think/topics/generative-ai) model with an external knowledge base. The data in the knowledge base augments user queries with more context so the LLM can generate more accurate responses. RAG enables LLMs to be more accurate in domain-specific contexts without needing [fine-tuning](https://www.ibm.com/think/topics/fine-tuning).

Rather than rely solely on training data, RAG-enabled [AI models](https://www.ibm.com/think/topics/ai-model) can access current data in real time through [APIs](https://www.ibm.com/think/topics/api) and other connections to data sources. A standard RAG pipeline comprises two AI models:

- The information retrieval component, typically an [embedding](https://www.ibm.com/think/topics/embedding) model paired with a [vector database](https://www.ibm.com/think/topics/vector-database) containing the data to be retrieved.


- The [generative AI](https://www.ibm.com/think/topics/generative-ai) component, usually an LLM.


In response to [natural language](https://www.ibm.com/think/topics/natural-language-processing) user queries, the embedding model converts the query to a vector embedding, then retrieves similar data from the knowledge base. The AI system combines the retrieved data with the user query for context-aware response generation.

### What is agentic AI?

Agentic AI is a type of AI that can determine and carry out a course of action by itself. Most agents available at the time of publishing are LLMs with function-calling capabilities, meaning that they can call tools to perform tasks. In theory, AI agents are LLMs with three significant characteristics:

- They have **memory**, both short and long term, which enables them to plan and execute complex tasks. Memory also allows agents to refer to previous tasks and use that data to inform future workflows. Agentic RAG systems use semantic caching to store and refer to previous sets of queries, context and results.


- They are capable of query **routing**, step-by-step **planning** and decision-making. Agents use their memory capabilities to retain information and plot an appropriate course of action in response to complex queries and prompts.


- They can perform **tool calling** through APIs. More capable agents can choose which tools to use for the workflow they generate in response to user interactions.


Agentic workflows can consist of either one AI agent or multiagent systems that combine several agents together.

## Agentic RAG vs. traditional RAG systems

Agentic RAG brings several significant improvements over traditional RAG implementation:

- **Flexibility:** Agentic RAG applications pull data from multiple external knowledge bases and allow for external tool use. Standard RAG pipelines connect an LLM to a single external dataset. For example, many enterprise RAG systems pair a [chatbot](https://www.ibm.com/think/topics/chatbots) with a knowledge base containing proprietary organization data.

- **Adaptability:** Traditional RAG systems are reactive data retrieval tools that find relevant information in response to specific queries. There is no ability for the RAG system to adapt to changing contexts or access other data. Optimal results often require extensive [prompt engineering](https://www.ibm.com/think/topics/prompt-engineering).

Meanwhile, agentic RAG is a transition from static rule-based querying to adaptive, intelligent problem-solving. Multiagent systems encourage multiple AI models to collaborate and check each other’s work.

- **Accuracy:** Traditional RAG systems do not validate or optimize their own results. People must discern whether the system is performing at an acceptable standard. The system itself has no way of knowing whether it is finding the right data or successfully incorporating it to facilitate context-aware generation. However, AI agents can iterate on previous processes to optimize results over time.

- **Scalability:** With networks of RAG agents working together, tapping into multiple external data sources and using tool-calling and planning capabilities, agentic RAG has greater scalability. Developers can construct flexible and scalable RAG systems that can handle a wide range of user queries.

- **Multimodality:** Agentic RAG systems benefit from recent advancements in multimodal LLMs to work with a greater range of data types, such as images and audio files. Multimodal models process multiple types of [structured, semistructured and unstructured data](https://www.ibm.com/think/topics/structured-vs-unstructured-data). For example, several recent [GPT](https://www.ibm.com/think/topics/gpt) models can generate visual and audio content in addition to standard text generation.


Consider several employees working in an office. A traditional RAG system is the employee who performs well when given specific tasks and told how to accomplish them. They are reluctant to take initiative and feel uncomfortable going outside explicit instructions.

In comparison, an agentic RAG system is a proactive and creative team. They are also good at following directions but love to take initiative and solve challenges on their own. They are unafraid to come up with their own solutions to complex tasks that might stump or intimidate their coworkers.

### Is agentic RAG better than traditional RAG?

While agentic RAG optimizes results with function calling, multistep reasoning and multiagent systems, it isn’t always the better choice. More agents at work mean greater expenses, and an agentic RAG system usually require paying for more tokens. While agentic RAG can increase speed over traditional RAG, LLMs also introduce latency because it can take more time for the model to generate its outputs.

Lastly, agents are not always reliable. They might struggle and even fail to complete tasks, depending on the complexity and the agents used. Agents do not always collaborate smoothly and can compete over resources. The more agents in a system, the more complex the collaboration becomes, with a higher chance for complications. And even the most airtight RAG system cannot eliminate the potential for hallucinations entirely.

## How does agentic RAG work?

Agentic RAG works by incorporating one or more types of AI agents into RAG systems. For example, an agentic RAG system might combine multiple information retrieval agents, each specialized in a certain domain or type of data source. One agent queries external databases while another can comb through emails and web results.

[Agentic AI frameworks](https://www.ibm.com/think/insights/top-ai-agent-frameworks), such as [LangChain](https://www.ibm.com/think/topics/langchain) and [LlamaIndex](https://www.ibm.com/think/topics/llamaindex), and the orchestration framework [LangGraph](https://www.ibm.com/think/topics/langgraph) can be found on GitHub. With them, it is possible to experiment with [agentic architectures](https://www.ibm.com/think/topics/agentic-architecture) for RAG at minimal costs. If using [open source](https://www.ibm.com/think/topics/open-source) models such as [Granite](https://www.ibm.com/granite) ™ or Llama-3, RAG system designers can also mitigate the fees demanded by other providers such as OpenAI while enjoying greater [observability](https://www.ibm.com/think/topics/observability).

Agentic RAG systems can contain one or more types of AI agents, such as:

- Routing agents


- Query planning agents


- ReAct agents


- Plan-and-execute agents


### Routing agents

Routing agents determine which external knowledge sources and tools are used to address a user query. They process user prompts and identify the RAG pipeline most likely to result in optimal response generation. In a single-agent RAG system, a routing agent chooses which data source to query.

### Query planning agents

Query planning agents are the task managers of the RAG pipeline. They process complex user queries to break them down into step-by-step processes. They submit the resulting subqueries to the other agents in the RAG system, then combine the responses for a cohesive overall response. The process of using one agent to manage other AI models is a type of [AI orchestration](https://www.ibm.com/think/topics/ai-orchestration).

### ReAct agents

ReAct (reasoning and action) is an agent framework that creates [multiagent systems](https://www.ibm.com/think/topics/multiagent-system) that can create and then act on step-by-step solutions. They can also identify appropriate tools that can help. Based on the results of each step, ReAct agents can dynamically adjust subsequent stages of the generated workflow.

### Plan-and-execute agents

Plan-and-execute agent frameworks are a progression from ReAct agents. They can execute multistep workflows without calling back to the primary agent, reducing costs and increasing efficiency. And because the planning agent must reason through all the steps needed for a task, completion rates and quality tend to be higher.

## Agentic RAG use cases

While agentic RAG can suit any traditional RAG application, the greater compute demands make it more appropriate for situations that require querying multiple data sources. Agentic RAG applications include:

- **Real-time question-answering:** Enterprises can deploy RAG-powered chatbots and FAQs to provide employees and customers with current, accurate information.


- **Automated support:** Businesses wanting to streamline customer support services can use automated RAG systems to handle simpler customer inquiries. The agentic RAG system can escalate more demanding support requests to human personnel.


- **Data management:** RAG systems make it easier to find information within proprietary data stores. Employees can quickly get the data they need without having to sort through databases themselves.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="what-is-agentic-rag.md">
<details>
<summary>What is Agentic RAG</summary>

Phase: [EXPLOITATION]

# What is Agentic RAG

**Source URL:** <https://weaviate.io/blog/what-is-agentic-rag>

https://weaviate.io/assets/images/hero-d41770f860f0fa78a7230034f7d43820.png

While Retrieval-Augmented Generation (RAG), often referred to as LLM RAG, dominated 2023, [agentic workflows are driving massive progress in 2024](https://x.com/AndrewYNg/status/1770897666702233815?lang=en). The usage of AI agents opens up new possibilities for building more powerful, robust, and versatile Large Language Model(LLM)-powered applications. One possibility is enhancing LLM RAG pipelines with AI agents in agentic RAG pipelines. Agentic RAG is a way to make the RAG pipeline more reliable by adding planning, tool use, and validation loops.

This article introduces you to the concept of agentic RAG, its implementation, and its benefits and limitations.

## Fundamentals of Agentic RAG

Agentic RAG describes an AI agent-based implementation of RAG. Before we go any further, let’s quickly recap the fundamental concepts of RAG and AI agents.

### What is Retrieval-Augmented Generation (RAG)

[Retrieval-Augmented Generation (RAG)](https://weaviate.io/blog/introduction-to-rag) is a technique for building LLM-powered applications. It leverages an external knowledge source to provide the LLM with relevant context and reduce hallucinations.

Many teams also call this LLM RAG or retrieval augmented generation for LLMs, since retrieval supplies the model with external context at inference time.

A naive LLM RAG pipeline consists of a retrieval component (typically composed of an embedding model and a vector database) and a generative component (an LLM). At inference time, the user query is used to run a similarity search over the indexed documents to retrieve the most similar documents to the query and provide the LLM with additional context.

https://weaviate.io/assets/images/Vanilla_RAG-697535e2d5b9ae64ccfd6415a79965c7.png

Typical RAG applications have two considerable limitations:

1. The naive RAG pipeline only considers one external knowledge source. However, some solutions might require two external knowledge sources, and some solutions might require external tools and APIs, such as web searches.
2. They are a one-shot solution, which means that context is retrieved once. There is no reasoning or validation over the quality of the retrieved context.

### What are Agents in AI Systems

With the popularity of LLMs, new paradigms of AI agents and multi-agent systems have emerged. AI agents are LLM-based systems with a role and task that use tools and agent memory (short-term and long-term) to plan, act, and adapt. The reasoning capabilities of LLMs help the agent plan the required steps and take action to complete the task at hand.

Thus, the core components of an AI agent are:

- LLM (with a role and a task)
- Memory (short-term and long-term)
- Planning (e.g., reflection, self-critics, query routing, etc.)
- Tools (e.g., calculator, web search, etc.)

https://weaviate.io/assets/images/Components_of_an_AI_agent-2f1846374720471d6b11169203ccb865.png

One popular framework is the [ReAct framework](https://arxiv.org/abs/2210.03629). A ReAct agent can handle sequential multi-part queries while maintaining state (in memory) by combining routing, query planning, and tool use into a single entity.

> ReAct = Reason + Act (with LLMs)

The process involves the following steps:

1. Thought: Upon receiving the user query, the agent reasons about the next action to take

2. Action: the agent decides on an action and executes it (e.g., tool use)

3. Observation: the agent observes the feedback from the action

4. This process iterates until the agent completes the task and responds to the user.

https://weaviate.io/assets/images/ReAct-6d7ea59cdc1c7f882f860e7015228302.png

## What is Agentic RAG?

Agentic RAG describes an AI agent-based implementation of RAG. Specifically, it incorporates AI agents into the RAG pipeline to orchestrate its components and perform additional actions beyond simple information retrieval and generation to overcome the limitations of the non-agentic pipeline.

In other words, agentic RAG turns retrieval into an iterative process: the agent can retrieve, evaluate, re-retrieve, and validate context before generating the final answer.

This makes agentic RAG more robust than one-shot retrieval in production systems.

> Agentic RAG describes an AI agent-based implementation of RAG.

### How does Agentic RAG work?

Although agents can be incorporated in different stages of the LLM RAG pipeline, agentic RAG most commonly refers to the use of agents in the retrieval component.

Specifically, the retrieval component becomes agentic through the use of retrieval agents with access to different retriever tools, such as:

- Vector search engine (also called a query engine) that performs vector search over a vector index (like in typical RAG pipelines)
- Web search
- Calculator
- Any API to access software programmatically, such as email or chat programs
- and many more.

In many systems, retrieved results also act as a form of long-term memory, allowing agents to recall relevant information across steps.

The RAG agent can then reason and act over the following example retrieval scenarios:

1. Decide whether to retrieve information or not
2. Decide which tool to use to retrieve relevant information
3. Formulate the query itself
4. Evaluate the retrieved context and decide whether it needs to re-retrieve.

### Agentic RAG Architecture

In contrast to the sequential naive RAG architecture, the core of the agentic RAG architecture is the agent. Agentic RAG architectures can have various levels of complexity. In the simplest form, a single-agent RAG architecture is a simple router. However, you can also add multiple agents into a multi-agent RAG architecture. This section discusses the two fundamental RAG architectures.

**Single-Agent RAG (Router)**

In its simplest form, agentic RAG is a router. This means you have at least two external knowledge sources, and the agent decides which one to retrieve additional context from. However, the external knowledge sources don't have to be limited to (vector) databases. You can retrieve further information from tools as well. For example, you can conduct a web search, or you could use an API to retrieve additional information from Slack channels or your email accounts.

https://weaviate.io/assets/images/Single_Agent_RAG_System_(Router-ae2ec18616941504070d6b2a7210a358.png)

**Multi-agent RAG Systems**

As you can guess, the single-agent system also has its limitations because it's limited to only one agent with reasoning, retrieval, and answer generation in one. Therefore, it is beneficial to chain multiple agents into a multi-agent RAG application.

For example, you can have one master agent who coordinates information retrieval among multiple specialized retrieval agents. For instance, one agent could retrieve information from proprietary internal data sources. Another agent could specialize in retrieving information from your personal accounts, such as email or chat. Another agent could also specialize in retrieving public information from web searches.

https://weaviate.io/assets/images/Multi_Agent_RAG_System-73e480f62a52e172a78a0ac344dcdcb5.png

### Beyond Retrieval Agents

The above example shows the usage of different retrieval agents. However, you could also use agents for purposes other than retrieval. The possibilities of agents in the RAG system are manifold.

## Agentic RAG vs. (Vanilla) RAG

While the fundamental concept of RAG (sending a query, retrieving information, and generating a response) remains the same, **tool use generalizes it,** making it more flexible and powerful.

Think of it this way: Common (vanilla) RAG is like being at the library (before smartphones existed) to answer a specific question. Agentic RAG, on the other hand, is like having a smartphone in your hand with a web browser, a calculator, your emails, etc.

| | Vanilla LLM RAG | Agentic RAG |
| --- | --- | --- |
| Access to external tools | No | Yes |
| Query pre-processing | No | Yes |
| Multi-step retrieval | No | Yes |
| Validation of retrieved information | No | Yes |

Here, we use “RAG” and “LLM RAG” interchangeably—both refer to retrieval augmented generation for large language models.

## Implementing Agentic RAG

As outlined earlier, agents are comprised of multiple components. To build an agentic RAG pipeline, there are two options: a language model with function calling or an agent framework. Both implementations get to the same result, it will just depend on the control and flexibility you want.

### Language Models with Function Calling

Language models are the main component of agentic RAG systems. The other component is tools, which enable the language model access to external services. Language models with function calling offer a way to build an agentic system by allowing the model to interact with predefined tools. Language model providers have added this feature to their clients.

In June 2023, [OpenAI released function calling](https://platform.openai.com/docs/assistants/tools/function-calling) for `gpt-3.5-turbo` and `gpt-4`. It enabled these models to reliably connect GPT’s capabilities with external tools and APIs. Developers quickly started building applications that plugged `gpt-4` into code executors, databases, calculators, and more.

[Cohere](https://docs.cohere.com/v2/docs/tool-use) further launched their connectors API to add tools to the Command-R suite of models. Additionally, [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) and [Google](https://ai.google.dev/gemini-api/docs/function-calling) launched function calling for Claude and Gemini. By powering these models with external services, it can access and cite web resources, execute code and more.

Function calling isn’t only for proprietary models. Ollama introduced tool support for popular open-source models like `Llama3.2`, `nemotron-mini`, and [others](https://ollama.com/search?c=tools).

To build a tool, you first need to define the function. In this snippet, we’re writing a function that is using Weaviate’s [hybrid search](https://docs.weaviate.io/weaviate/search/hybrid) to retrieve objects from the database:

```python
def get_search_results(query: str) -> str:
    """Sends a query to Weaviate's Hybrid Search. Parses the response into a {k}:{v} string."""

    response = blogs.query.hybrid(query, limit=5)

    stringified_response = ""
    for idx, o in enumerate(response.objects):
        stringified_response += f"Search Result: {idx+1}:\n"
        for prop in o.properties:
            stringified_response += f"{prop}:{o.properties[prop]}"
        stringified_response += "\n"

    return stringified_response
```

We will then pass the function to the language model via a `tools_schema`. The schema is then used in the prompt to the language model:

```python
tools_schema=[{\
    'type': 'function',\
    'function': {\
        'name': 'get_search_results',\
        'description': 'Get search results for a provided query.',\
        'parameters': {\
          'type': 'object',\
          'properties': {\
            'query': {\
              'type': 'string',\
              'description': 'The search query.',\
            },\
          },\
          'required': ['query'],\
        },\
    },\
}]
```

Since you’re connecting to the language model API directly, you’ll need to write a loop that routes between the language model and tools:

```python
def ollama_generation_with_tools(user_message: str,
                                 tools_schema: List, tool_mapping: Dict,
                                 model_name: str = "llama3.1") -> str:
    messages=[{\
        "role": "user",\
        "content": user_message\
    }]
    response = ollama.chat(
        model=model_name,
        messages=messages,
        tools=tools_schema
    )
    if not response["message"].get("tool_calls"):
        return response["message"]["content"]
    else:
        for tool in response["message"]["tool_calls"]:
            function_to_call = tool_mapping[tool["function"]["name"]]
            print(f"Calling function {function_to_call}...")
            function_response = function_to_call(tool["function"]["arguments"]["query"])
            messages.append({
                "role": "tool",
                "content": function_response,
            })

    final_response = ollama.chat(model=model_name, messages=messages)
    return final_response["message"]["content"]
```

Your query will then look like this:

```python
ollama_generation_with_tools("How is HNSW different from DiskANN?",
                            tools_schema=tools_schema, tool_mapping=tool_mapping)
```

You can follow along [this recipe](https://github.com/weaviate/recipes/blob/main/integrations/llm-agent-frameworks/function-calling/ollama/ollama-weaviate-agents.ipynb) to recreate the above.

### Agent Frameworks

Agent Frameworks such as DSPy, LangChain, CrewAI, LlamaIndex, and Letta have emerged to facilitate building applications with language models. These frameworks simplify building agentic RAG systems by plugging pre-built templates together.

- DSPy supports [ReAct](https://dspy-docs.vercel.app/deep-dive/modules/react/) agents and [Avatar](https://github.com/stanfordnlp/dspy/blob/main/examples/agents/avatar_langchain_tools.ipynb) optimization. Avatar optimization describes the use of automated prompt engineering for the descriptions of each tool.
- [LangChain](https://www.langchain.com/) provides many services for working with tools. LangChain’s [LCEL](https://python.langchain.com/v0.1/docs/expression_language/) and [LangGraph](https://www.langchain.com/langgraph) frameworks further offer built-in tools.
- [LlamaIndex](https://www.llamaindex.ai/) further introduces the QueryEngineTool, a collection of templates for retrieval tools.
- [CrewAI](https://www.crewai.com/) is one of the leading frameworks for developing multi-agent systems. One of the key concepts utilized for tool use is sharing tools amongst agents.
- [Swarm](https://github.com/openai/swarm) is a framework built by OpenAI for multi-agent orchestration. Swarm similarly focuses on how tools are shared amongst agents.
- [Letta](https://docs.letta.com/introduction) interfaces reflecting and refining an internal world model as functions. This entails potentially using search results to update the agent’s memory of the chatbot user, in addition to responding to the question.

## Why are Enterprises Adopting Agentic RAG

Enterprises are moving on from vanilla RAG to building agentic RAG applications. [Replit released an agent](https://docs.replit.com/replitai/agent) that helps developers build and debug software. Additionally, [Microsoft announced copilots](https://blogs.microsoft.com/blog/2024/10/21/new-autonomous-agents-scale-your-team-like-never-before/) that work alongside users to provide suggestions in completing tasks. These are only a few examples of agents in production and the possibilities are endless.

### Benefits of Agentic RAG

The shift from vanilla RAG to agentic RAG allows these systems to produce more accurate responses, perform tasks autonomously, and better collaborate with humans.

The benefit of agentic RAG lies primarily in the improved quality of retrieved additional information. By adding agents with access to tool use, the retrieval agent can route queries to specialized knowledge sources. Furthermore, the reasoning capabilities of the agent enable a layer of validation of the retrieved context before it is used for further processing. As a result, agentic RAG pipelines can lead to more robust and accurate responses.

### Limitations of Agentic RAG

However, there are always two sides to every coin. Using an AI agent a for subtask means incorporating an LLM to do a task. This comes with the limitations of using LLMs in any application, such as added latency and unreliability. Depending on the reasoning capabilities of the LLM, an agent may fail to complete a task sufficiently (or even at all). It is important to incorporate proper failure modes to help an AI agent get unstuck when they are unable to complete a task.

## Summary

This blog discussed the concept of agentic RAG, which involves incorporating agents into the RAG pipeline. Although agents can be used for many different purposes in a RAG pipeline, agentic RAG most often involves using retrieval agents with access to tools to generalize retrieval. Agentic RAG is increasingly used to make LLM RAG pipelines more reliable by adding tool use, multi-step retrieval, and validation.

This article discussed agentic RAG architectures using single-agent and multi-agent systems and their differences from vanilla RAG pipelines.

With the rise and popularity of AI agent systems, many different frameworks are evolving for implementing agentic RAG, such as LlamaIndex, LangGraph, or CrewAI.

Finally, this article discussed the benefits and limitations of agentic RAG pipelines.

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>