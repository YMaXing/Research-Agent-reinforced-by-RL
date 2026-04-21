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

-----

Phase: [EXPLOITATION]

### Source [14]: https://airbyte.com/agentic-data/ai-agent-vs-rag

Query: What distinguishes agentic RAG from standard linear RAG pipelines, especially when retrieval functions as a tool in a ReAct-style agent's reasoning and iteration loop?

Answer: In agentic RAG, agents orchestrate retrieval within reasoning loop rather than fixed pipeline. Traditional RAG retrieves once before generation; agentic embeds retrieval in loop with multiple passes, refining queries on intermediate results, evaluating sufficiency, requesting more, routing to sources, validating across sources. Handles complex tasks vs traditional's single-step efficiency for factual queries. Agent decides steps (agentic); predefined workflow is RAG. Progress to agentic RAG when gaps appear for better accuracy despite latency. Agents enable multi-step orchestration.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://domino.ai/blog/rag-vs-agentic-ai

Query: What distinguishes agentic RAG from standard linear RAG pipelines, especially when retrieval functions as a tool in a ReAct-style agent's reasoning and iteration loop?

Answer: RAG assumes fixed retrieval step in pipeline to improve informational answers; agentic systems treat retrieval as conditional capability invoked as needed. Agent may not know initial info needs, retrieves, acts, observes, decides if context irrelevant/incomplete, evolving situation. Agents decide what questions worth answering, breaking RAG's scope limitation (assumes informational problem). Not just better prompts or autonomous workflows; fundamentally different model. Research shows complex tasks need iterative determination of info needs vs fixed retrieval phase.

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

### Source [22]: https://www.mindstudio.ai/blog/what-is-rag/

Query: In what ways does RAG function as a foundational competency for AI engineers building grounded agents, particularly in complementing future memory systems and reducing hallucinations through verifiable sources?

Answer: RAG (Retrieval-Augmented Generation) is essential for AI agents, reducing hallucinations by 70-90% by grounding responses in retrieved documents from external knowledge bases like vector databases. Instead of guessing, agents cite specific verifiable sources. RAG enables dynamic knowledge access to live data sources without retraining, addressing limitations of standard LLMs such as outdated info, lack of domain expertise, and hallucinations. For AI agents, RAG provides domain expertise from proprietary data, current information like policy changes, and grounds responses in verifiable external sources. The process involves retrieval of relevant info, augmentation of query with context, and generation by LLM. Multimodal RAG extends this to visual content. RAG complements future memory systems by enabling real-time access to updatable knowledge bases.

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

### Source [26]: https://humanloop.com/blog/rag-architectures

Query: How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?

Answer: Retrieval Augmented Generation (RAG) is a technique in large language models (LLMs) that enhances text generation by incorporating real-time data retrieval. Unlike traditional models that rely solely on their pre-trained knowledge, RAG allows models to search external databases or documents during the generation process, resulting in more accurate and up-to-date responses. By blending retrieval and generation, RAG architecture addresses key limitations such as hallucinations and improves fact-based, contextually relevant outputs. In RAG, the model operates in two stages.

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

### Source [37]: https://www.chitika.com/hybrid-retrieval-rag/

Query: How does hybrid retrieval theoretically combine BM25 keyword methods with dense vector search to address limitations of pure semantic retrieval in RAG?

Answer: Hybrid retrieval combines BM25 (keyword-based) and FAISS (dense vector search) to enhance RAG performance. Keyword-based search like BM25 is precise but lacks semantic understanding, while dense vector search like FAISS captures meaning but often returns irrelevant results. Neither alone suffices for RAG. One approach is BM25 first retrieves a subset of documents, then FAISS refines it by dense vector similarity on the smaller set, enhancing accuracy and reducing overhead. Hybrid search combines keyword (BM25, SPLADE) and semantic (embedding) methods, generally more effective than either alone. The process flows from query and documents to vector and sparse n-grams indexes, top k results via reciprocal rank fusion, then to LLM. This synergy transforms retrieval into a context-aware tool, as in pharmaceutical research where BM25 identifies specific drug names and FAISS discerns nuanced connections like molecular pathways.

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
<summary>What are the main scalability challenges and indexing trade-offs when implementing hierarchical community detection and summarization in GraphRAG for very large document corpora?</summary>

Phase: [EXPLORATION]

### Source [61]: https://www.articsledge.com/post/graphrag-retrieval-augmented-generation

Query: What are the main scalability challenges and indexing trade-offs when implementing hierarchical community detection and summarization in GraphRAG for very large document corpora?

Answer: Scalability challenges in GraphRAG for very large corpora include high computational costs for community detection, which becomes expensive as graphs grow to billions of nodes and edges. Memory overhead doubles for disambiguation context, and traversal slows without an optimized graph database. Upfront indexing cost is a major issue: building a knowledge graph for 1M tokens costs $20-50 in API fees and several hours of compute, scaling to hundreds of dollars for large corpora. Indexing trade-offs involve high upfront costs ($20-500 for typical corpora vs. $2-5 for vector RAG), but lower ongoing costs, especially with LazyGraphRAG reducing costs to 0.1% of original while maintaining quality through lazy indexing, incremental indexing, smaller models like GPT-4o-mini, or self-hosting LLMs. Community detection uses the Leiden algorithm in the core pipeline: extract entities/relationships, build graph, detect communities, generate summaries. Mitigations for scalability include LazyGraphRAG for minimal overhead, similar to vector storage.

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://ojs.aaai.org/index.php/AAAI/article/view/38619/42581

Query: What are the main scalability challenges and indexing trade-offs when implementing hierarchical community detection and summarization in GraphRAG for very large document corpora?

Answer: GraphRAG's scalability challenges stem from low community quality using Leiden algorithm, which relies solely on graph structure ignoring node/edge semantics, leading to communities with different themes and poor summary quality. High generation cost: analyzing all communities with LLMs is time- and token-consuming; e.g., 2,984 communities in Multihop-RAG dataset for 100 questions costs ~$650 and 106 million tokens, impractical overhead. Limited compatibility as Global/Local Search retrieves at one granularity, inadequate for abstract/specific questions. These limit applicability to large corpora.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://ai.plainenglish.io/from-graphrag-to-hierarchical-rag-making-global-sensemaking-practical-2193ea5da342

Query: What are the main scalability challenges and indexing trade-offs when implementing hierarchical community detection and summarization in GraphRAG for very large document corpora?

Answer: Challenges with early GraphRAG at scale include expensive community traversal for global questions, increasing latency and token cost. Static and costly updates: significant data changes require re-running community detection and re-summarization. Weak alignment between local and global context, with summaries generated separately not explaining entity contributions clearly. Implicit reasoning hides paths in LLM, reducing interpretability. These arise from knowledge graphs and communities addressing chunk-based RAG's global understanding limits but introducing new scalability issues for large corpora.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://arxiv.org/html/2502.09891v3

Query: What are the main scalability challenges and indexing trade-offs when implementing hierarchical community detection and summarization in GraphRAG for very large document corpora?

Answer: GraphRAG limitations for large corpora: L1. Low community quality from Leiden algorithm using only graph structure, ignoring semantics, resulting in mixed-theme communities and poor summaries. L2. Limited compatibility: Global/Local Search at single granularity, inadequate for abstract/specific questions. L3. High generation cost: LLM analysis of all communities is time/token-intensive; e.g., 2,984 communities in Multihop-RAG for 100 questions ~$650 and 106M tokens. ArchRAG contrasts with token cost O(D(1 + (1-a^L)/(1-a))) for KG construction O(D) and summaries, L=O(log n) but typically <=5 due to clustering constraints.

-----

-----

Phase: [EXPLORATION]

### Source [65]: https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00046-GraphRAG.pdf

Query: What are the main scalability challenges and indexing trade-offs when implementing hierarchical community detection and summarization in GraphRAG for very large document corpora?

Answer: Scalability for very large datasets in hierarchical community detection and summarization: method designed to scale, creating summaries of Leiden hierarchy communities independently useful for global structure understanding. Trade-offs of graph index: high compute investment upfront, depending on budget, lifetime queries per dataset, value from summaries/other graph RAG. GraphRAG best for head-to-head but graph-free competitive; decision factors include expected queries. Challenge for query-focused summarization over entire corpus exceeding LLM windows, with info loss in long contexts; naive RAG inadequate, needs pre-indexing for global summarization.

-----

</details>

<details>
<summary>How do uncertainty estimation techniques and confidence scoring mechanisms in the generation phase of RAG pipelines theoretically detect and mitigate residual hallucinations even after applying hybrid retrieval, reranking, and query transformations?</summary>

Phase: [EXPLORATION]

### Source [67]: https://mbrenndoerfer.com/writing/hallucination-mitigation

Query: How do uncertainty estimation techniques and confidence scoring mechanisms in the generation phase of RAG pipelines theoretically detect and mitigate residual hallucinations even after applying hybrid retrieval, reranking, and query transformations?

Answer: In the full mitigation pipeline for RAG, after retrieval (which reduces parametric memory errors), the generation phase employs self-consistency and uncertainty estimation to detect and mitigate residual hallucinations. Multiple responses (N samples) are generated conditioned on retrieved documents. Self-consistency decoding computes a consistency_score across responses to identify unstable outputs. Uncertainty is estimated via log probability standard deviation (lp_std) from generation log_probs. Confidence scoring combines these: high confidence if consistency_score >= threshold (e.g., 0.6) and lp_std <= uncertainty_threshold (e.g., 0.1), leading to 'answer'; medium for hedging; low triggers 'abstain'. This theoretically flags low-confidence or inconsistent generations as potential hallucinations even post-retrieval enhancements like hybrid methods, reranking, or query transformations, adding layers of protection by deciding to answer, hedge, or abstain.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://arxiv.org/html/2512.09148v1

Query: How do uncertainty estimation techniques and confidence scoring mechanisms in the generation phase of RAG pipelines theoretically detect and mitigate residual hallucinations even after applying hybrid retrieval, reranking, and query transformations?

Answer: Model-internal confidence metrics in the generation phase detect hallucinations in RAG by exploiting the LLM’s internal uncertainty signals, even after retrieval grounding. Techniques include perplexity (exponential of cross-entropy loss for sequence-level likelihood), token confidence (average prediction probabilities across generated tokens), and maximum token probability (highest confidence prediction in the response). These score low-confidence outputs indicative of hallucinations. Hallucinations persist in RAG when models over-rely on parametric memory in FFNs despite external context from attention heads. Semantic entropy measures model uncertainty and representation. Theoretically, these mechanisms flag residual hallucinations post-retrieval (hybrid, reranking, query transformations) by quantifying generation uncertainty, enabling mitigation like abstaining or review of low-scoring responses.

-----

-----

Phase: [EXPLORATION]

### Source [69]: https://aws.amazon.com/blogs/machine-learning/detect-hallucinations-for-rag-based-systems/

Query: How do uncertainty estimation techniques and confidence scoring mechanisms in the generation phase of RAG pipelines theoretically detect and mitigate residual hallucinations even after applying hybrid retrieval, reranking, and query transformations?

Answer: In RAG-based systems, hallucination detection in generation uses confidence scoring: a secondary model scores response sentences (0-1 float, 0=grounded in context, 1=not based on context) to quantify hallucination risk. This leverages available retrieved context post-hybrid retrieval, reranking, and query transformations. Low scores indicate direct context basing (no hallucination); high scores flag fabrications. Uncertainty in scoring (mid-range floats) reflects ambiguity. Theoretically, this mitigates residual hallucinations by identifying ungrounded generations, enabling actions like correction or abstention. Pros/cons consider accuracy, precision, recall, cost; foundational for reliable RAG by detecting where generation deviates from context despite prior retrieval enhancements.

-----

</details>

<details>
<summary>What theoretical principles and empirical decision criteria guide an agent's choice of retrieval iteration count, query reformulation, and termination conditions within agentic RAG's ReAct-style reasoning loop?</summary>

Phase: [EXPLORATION]

### Source [71]: https://www.kore.ai/blog/what-is-agentic-rag

Query: What theoretical principles and empirical decision criteria guide an agent's choice of retrieval iteration count, query reformulation, and termination conditions within agentic RAG's ReAct-style reasoning loop?

Answer: In Agentic RAG, retrieval is an iterative and adaptive process guided by the agent. The system continuously evaluates whether retrieved information meets the task requirements and adjusts its retrieval strategy accordingly. Core retrieval concepts include dynamic query rewriting based on partial evidence, multi-hop retrieval where one retrieved result triggers another, cross-source retrieval combining vector search, keyword search, structured data, and domain-specific repositories, and confidence scoring and filtering to remove irrelevant or low-value items. This iterative retrieval loop ensures accumulation of the most relevant, complete, and high-precision evidence before building context. Agentic RAG introduces agentic behavior, planning, decision-making, iterative refinement, and adaptive retrieval, elevating it to a dynamic reasoning system. The agent actively decides what to retrieve, how to refine it, when to re-query, and how to structure its reasoning path, resulting in more accurate, context-aware outcomes especially for multi-step reasoning.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://www.digitalapplied.com/blog/agentic-rag-patterns-multi-step-reasoning-guide

Query: What theoretical principles and empirical decision criteria guide an agent's choice of retrieval iteration count, query reformulation, and termination conditions within agentic RAG's ReAct-style reasoning loop?

Answer: In Agentic RAG, retrieval becomes a tool the agent calls when more context is needed. The agent evaluates retrieved information to decide next moves: re-retrieve with a refined query, decompose into sub-queries, triangulate across corpora, or commit to an answer. The loop runs until the model signals confidence or a stop condition fires. Key patterns include iterative retrieval, query decomposition, hypothesis-driven retrieval, cross-corpus triangulation, and evidence-weighted synthesis. Successful implementation involves setting iteration budgets tight to bound cost, per-iteration observability, aggressive prompt caching, hybrid routing, and explicit stop conditions. The best stop conditions are cooperative, showing the remaining budget to the model so it can scope work and commit to a partial answer before exhaustion. Most systems route to classic RAG first, escalating to agentic RAG when needed, using a decision matrix for routing logic.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://arxiv.org/html/2603.07379v1

Query: What theoretical principles and empirical decision criteria guide an agent's choice of retrieval iteration count, query reformulation, and termination conditions within agentic RAG's ReAct-style reasoning loop?

Answer: Agentic RAG is formulated as a POMDP where state s_t includes user query, intermediate reasoning traces, retrieved documents, and memory. Actions a_t include issuing retrieval queries or tools. The policy π_θ selects actions based on context. ReAct-style interleaves reasoning with actions (tool invocations), producing observations that update reasoning, running in a loop until a stop condition. Agentic properties map to POMDP components: iterative control via stochastic policy for loop governance; dynamic retrieval as query generation action; termination via finite horizon T_max to prevent infinite execution and constrain loop depth. Chain-of-Thought prompting elicits reasoning traces acting as query-construction substrate. Distinguishes Active RAG vs Agentic RAG.

-----

-----

Phase: [EXPLORATION]

### Source [74]: https://www.ibm.com/think/topics/react-agent

Query: What theoretical principles and empirical decision criteria guide an agent's choice of retrieval iteration count, query reformulation, and termination conditions within agentic RAG's ReAct-style reasoning loop?

Answer: In a ReAct agent, the loop of thought, action, observation repeats. After each action and observation, the agent decides whether to repeat or end the loop. Termination considerations include establishing a maximum number of loop iterations to limit latency, costs, token usage, and avoid endless loops. Alternatively, end when a specific condition is met, such as identifying a potential final answer exceeding a confidence threshold.

-----

-----

Phase: [EXPLORATION]

### Source [75]: https://medium.com/@romanbessouat/agentic-rag-how-ai-agents-improve-retrieval-and-accuracy-ce8e8842ca77

Query: What theoretical principles and empirical decision criteria guide an agent's choice of retrieval iteration count, query reformulation, and termination conditions within agentic RAG's ReAct-style reasoning loop?

Answer: Agentic RAG involves iteratively refining the query if initial retrieval lacks information, reranking or discarding chunks, invoking tools in multiple steps, and maintaining chain-of-thought reasoning on whether more retrieval is needed. The multi-step execution loop is: Thought (internal reasoning), Action (tool invocation), Observation (tool result), Refine/Next Thought, until ready for final answer. Benefits include dynamic retrieval for refining/expanding queries if insufficient, improved accuracy via multiple steps reducing hallucination, for complex queries where single pass fails.

-----

</details>

<details>
<summary>How have foundational principles from traditional library and information science, such as cataloging and metadata management, influenced the development of advanced indexing and chunking strategies in modern RAG systems?</summary>

Phase: [EXPLORATION]

### Source [76]: https://howaibuildthis.substack.com/p/rag-in-action-beyond-basics-to-advanced

Query: How have foundational principles from traditional library and information science, such as cataloging and metadata management, influenced the development of advanced indexing and chunking strategies in modern RAG systems?

Answer: The provided content discusses advanced data processing for better data retrieval in RAG systems, focusing on chunking strategies. Chunking is described as breaking up text into manageable, clear, and significant chunks to allow RAG systems to find relevant context more quickly and accurately. It mentions the evolution of document processing strategies from simple document chunks to techniques like hierarchies, sentence windows, and auto-merge. The post emphasizes preparing documents for indexing and notes that different document types, such as table-based PDFs in financial and insurance papers, require more sophisticated data processing and chunking strategies compared to text-based documents. However, it does not explicitly reference foundational principles from traditional library and information science, cataloging, or metadata management influencing these strategies.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://labelstud.io/blog/rag-fundamentals-challenges-and-advanced-techniques/

Query: How have foundational principles from traditional library and information science, such as cataloging and metadata management, influenced the development of advanced indexing and chunking strategies in modern RAG systems?

Answer: The content highlights that traditional knowledge bases used keywords and statistics for querying documents, suitable for search engines but less ideal for specific LLM questions requiring precise context from document chunks. It stresses data quality's importance in RAG performance, addressing issues like bad chunking strategies through preprocessing such as better text segmentation and noise reduction. For complex documents with structured elements like tables and diagrams, structured metadata and layout-aware processing techniques are recommended to preserve original context and format, ensuring retrieved information remains meaningful. This implies an influence from metadata management principles to enhance chunking and retrieval in RAG systems, akin to traditional information organization.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://hal.science/hal-05063024/file/RetrievalAugmentedGeneration-ITAL.pdf

Query: How have foundational principles from traditional library and information science, such as cataloging and metadata management, influenced the development of advanced indexing and chunking strategies in modern RAG systems?

Answer: Academic libraries host structured data like metadata and catalogs alongside unstructured content. RAG systems rely on semantic indexing for precision, processing resources through embedding models like Sentence-BERT to create vectors capturing semantic relationships. Metadata such as subject headings, keywords, and abstracts provides structure for organizing resources. RAG accesses both metadata and full content, enabling effective processing of structured and unstructured data. This leverages metadata in a manner directly drawing from traditional library cataloging principles to enhance indexing and retrieval accuracy in RAG, going beyond keyword matching to semantic relevance. Comparisons show RAG improves on traditional library search by using natural language queries, semantic accuracy, and synthesized summaries.

-----

-----

Phase: [EXPLORATION]

### Source [79]: https://arxiv.org/abs/2504.19754

Query: How have foundational principles from traditional library and information science, such as cataloging and metadata management, influenced the development of advanced indexing and chunking strategies in modern RAG systems?

Answer: The abstract discusses challenges in RAG where traditional fixed-size chunking fragments context, leading to incomplete retrieval. It introduces advanced techniques like late chunking and contextual retrieval to preserve global context within LLM input limits. No explicit mention of influences from traditional library and information science, cataloging, or metadata management on these strategies.

-----

-----

Phase: [EXPLORATION]

### Source [80]: https://www.linkedin.com/posts/piyush-ranjan-9297a632_rag-chunking-design-patterns-a-practical-activity-7375007110058647552-ndRg

Query: How have foundational principles from traditional library and information science, such as cataloging and metadata management, influenced the development of advanced indexing and chunking strategies in modern RAG systems?

Answer: The post outlines 11 RAG chunking strategies impacting retrieval quality: Fixed-Length, Sentence-Based, Overlap, Semantic-Based (ML-powered), Metadata-Enhanced Chunking, Modality-Aware, Summary-Attached, Adaptive (Hybrid), LLM-Suggested, Paragraph-Based, and Hierarchical Chunking. Metadata-Enhanced Chunking is specifically listed, suggesting use of metadata to improve chunking, which echoes traditional metadata management principles for better organization and retrieval. It mentions structured outputs from tools like Docling aiding chunkers and vectorizers for precise grounding.

-----

</details>

<details>
<summary>What lessons from recommendation systems and collaborative filtering in e-commerce can be applied to improve query routing and personalization in agentic RAG architectures?</summary>

Phase: [EXPLORATION]

### Source [81]: https://arxiv.org/pdf/2506.21931

Query: What lessons from recommendation systems and collaborative filtering in e-commerce can be applied to improve query routing and personalization in agentic RAG architectures?

Answer: Adapting Retrieval-Augmented Generation (RAG) systems to recommendation scenarios enhances the accuracy and personalization of suggestions. RAG can augment traditional recommendation algorithms with real-time, diverse information retrieval, going beyond static databases of user preferences and item characteristics. It dynamically fetches additional relevant data such as recent trends, user reviews, expert opinions, or real-time market data. RAG helps explain recommendations by retrieving and presenting supporting information, enhancing user trust and engagement. The adaptive nature of RAG enables recommendation systems to handle long-tail items or new users more effectively by drawing upon a broader knowledge base, addressing cold start problems in collaborative filtering. Current limitations of RAG in recommendation contexts include reliance on simplistic retrieval mechanisms like cosine similarity-based retrieval and embedding matching, which fall short in capturing nuanced preferences and contexts. More sophisticated approaches to information retrieval and matching are needed for the complexity of user preferences and multifaceted items.

-----

</details>

<details>
<summary>How are RAG approaches being adapted in the biotechnology and pharmaceutical industries for literature mining and hypothesis generation, particularly when dealing with multimodal scientific data?</summary>

Phase: [EXPLORATION]

### Source [86]: https://www.mindwalkai.com/blog/how-retrieval-augmented-generation-can-transform-drug-discovery

Query: How are RAG approaches being adapted in the biotechnology and pharmaceutical industries for literature mining and hypothesis generation, particularly when dealing with multimodal scientific data?

Answer: In the context of drug discovery, RAG can be applied to a range of tasks, from literature reviews to biomolecule design. Currently, generative models have demonstrated potential for de novo molecular design but are still hampered by their inability to integrate multimodal information or provide interpretability. The RAG framework can facilitate the retrieval of multimodal Information, from a range of sources, such as chemical databases, biological data, clinical trials, images, etc., that can significantly augment generative molecular design. Retrieval augmented generation is a natural language processing (NLP) approach that combines elements of both information retrieval and text generation models to enhance the performance of knowledge-intensive tasks. The retrieval component aggregates information relevant to specific queries from a predefined set of documents or knowledge sources which then serves as the context for the generation model. Once the information has been retrieved, it is combined with the input context to create an integrated context containing both the original query and the relevant retrieved information. The same expanded retrieval + augmented generation template applies to a whole range of applications in drug discovery like, for example, compound design (retrieve compounds/ properties and generate improvements/ new properties), drug-target interaction prediction (retrieve known drug-target interactions and generate potential interactions between new compounds and specific targets. adverse effects prediction (retrieve known adverse and generate modifications to eliminate effects). etc.

-----

-----

Phase: [EXPLORATION]

### Source [87]: https://intuitionlabs.ai/articles/rag-drug-discovery-eln-lims

Query: How are RAG approaches being adapted in the biotechnology and pharmaceutical industries for literature mining and hypothesis generation, particularly when dealing with multimodal scientific data?

Answer: MindWalk AI’s approach embodies this. They report that their RAG-driven LLM interface naturally “grounds” the model’s outputs in life-sciences specific information. Similarly, Mindwalk’s blog posits that RAG enables LLMs to access the “most current and reliable information from domain-specific, high-quality sources”, which is exactly what integrating journal literature and ELN/LIMS yields. Practical RAG deployment in pharma labs involves numerous considerations. In an unpublished internal evaluation, a biotech firm compared two groups of researchers given identical research questions: one used traditional search (ELN/LIMS search interfaces + literature), the other used a RAG-powered AI assistant. The RAG group achieved correct answers ~30–40% faster and with fewer search iterations. The assistant also helped junior scientists perform like senior experts in synthesizing information. Use Case: Literature & Knowledge Mining. Another scenario is querying across internal and external documents. For instance, a project leader might query: “What drug targets related to gene Z appear in our past publications or patents?” RAG can scour not only company patent archives and internal publications, but also public databases and PubMed. Notably, suggests that once integrated, an ELN provides ability to drill down to hard data such as biological assay measurements. RAG operationalizes this by automating the “drill down”: the data is pulled from the knowledge base on command.

-----

-----

Phase: [EXPLORATION]

### Source [88]: https://arxiv.org/html/2412.16701v2

Query: How are RAG approaches being adapted in the biotechnology and pharmaceutical industries for literature mining and hypothesis generation, particularly when dealing with multimodal scientific data?

Answer: In this research, we describe a novel Multimodal Retrieval Augmented Generation (RAG) application, AlzheimerRAG that integrates textual and visual modalities to improve contextual understanding and information synthesis from the biomedical literature. Our primary research objective in implementing multimodal RAG is to enhance context-aware retrieval capabilities by integrating heterogeneous data types, including textual data, images, and clinical trial information from PubMed articles. Existing methods typically focus on textual or visual data separately, leaving a gap for integrated multimodal solutions. The work by laid the groundwork for RAG models by demonstrating how retrieval can enhance the generation capabilities of language models, particularly in. The application of AI in Alzheimer’s research has been underscored by studies, which leverage multimodal inputs to improve early diagnosis and patient stratification. Other research, such as, has focused on using AI to manage Alzheimer’s symptoms, demonstrating that AI-driven solutions can provide valuable insights and recommendations for patient care. The BioBERT model represents a significant advancement in biomedical text mining, emphasizing the utility of transformer models fine-tuned for biomedical applications. This model has been foundational in developing various biomedical applications, including those focused on Alzheimer’s disease, where precision in information retrieval is critical. RAG methodologies have gained traction in biomedical research for efficiently synthesizing. The AlzheimerRAG application represents a significant advancement in biomedical research, particularly in understanding and managing Alzheimer’s disease. By integrating multimodal data—including textual information from PubMed articles, imaging studies, and clinical trial scenarios — this innovative Retrieval-Augmented Generation (RAG) tool provides a comprehensive platform for analyzing complex biomedical data. The use of cross-modal attention fusion enhances the alignment and processing of diverse data types, leading to improved accuracy in generating insights relevant to diagnosis, treatment planning, and understanding the pathophysiology of Alzheimer’s disease. The experimental results indicate that AlzheimerRAG outperforms existing methodologies in terms of accuracy and robustness.

-----

-----

Phase: [EXPLORATION]

### Source [89]: https://www.bprescient.com/case-study/llms-for-target-discovery/

Query: How are RAG approaches being adapted in the biotechnology and pharmaceutical industries for literature mining and hypothesis generation, particularly when dealing with multimodal scientific data?

Answer: Client success story. LLM’s for Target Discovery. Business Value Delivered: Better Drug Targets Identified Faster. Summary: Enabling Faster Target Identification Through Customized AI Tools. A mid-size biotechnology company wanted to identify novel drug targets using proprietary molecular data and publicly available literature, but data volumes were large and the data was in many disparate files and databases. bPrescient used large language model (LLM) technology augmented with retrieval-augmented generation (RAG) techniques to build a web application that allowed the client’s scientists to research and identify targets more quickly. Challenge: Large and Disparate Data To Mine For Targets.

-----

-----

Phase: [EXPLORATION]

### Source [90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12917324/

Query: How are RAG approaches being adapted in the biotechnology and pharmaceutical industries for literature mining and hypothesis generation, particularly when dealing with multimodal scientific data?

Answer: Retrieval‐augmented generation (RAG) is a complementary approach to LLM that allows precise control over the data domain across which training and generation occur. The provenance of RAG outputs can be readily traced to the corresponding source documents, and their findings can be further manipulated. RAGs can harness data from specialized user‐provided information sources, e.g., regulatory documents, and can be used to guide LLM. These features enhance capabilities, data security, and user trust. RAG‐integrated methods have the potential to be engineered to address task‐specific needs and knowledge‐intensive problems in clinical pharmacology and pharmacometrics research. Lu et al. review the potential applications of LLM in drug discovery, preclinical research, and literature review automation, with several case studies including LLM‐based tools for biomedical queries, regulatory intelligence, and medical writing. LLMs are also being used in AI‐augmented workflows for quantitative systems pharmacology modeling to improve knowledge integration and enhance reproducibility in rare diseases such as Gaucher's disease. LLMs are also being studied for pharmacovigilance to predict drug‐adverse event associations through text mining of discharge summaries, in the context of pharmacoepidemiological study design. While we evaluated RAGs in the context of regulatory documents and clinical trial protocol tasks, the approach might also be useful for other drug development applications. For example, it could be used in trial design to compare clinical endpoints, inclusion/exclusion criteria, dosing regimens, and outcomes with other drugs for the same indication, or in the same therapeutic class. In the preclinical stages, RAGs could be used to summarize the bioinformatics of drug targets, their signaling pathways, disease implications, and possible off‐target interactions. Our approach may also enable sponsors to check documents for compliance within the context of AI‐enabled drug evaluation processes at the FDA, which now include the recently launched ELSA, a secure LLM‐based tool for scientific.

-----

</details>

<details>
<summary>In what ways is the rise of decentralized AI and blockchain-based knowledge sharing transforming the security and provenance aspects of enterprise RAG deployments?</summary>

Phase: [EXPLORATION]

### Source [91]: https://medium.com/@sachinkumarbit/rag-security-essentials-protecting-enterprise-knowledge-from-ai-powered-attacks-1e7b8c878c4e

Query: In what ways is the rise of decentralized AI and blockchain-based knowledge sharing transforming the security and provenance aspects of enterprise RAG deployments?

Answer: The enterprise AI landscape has undergone a fundamental transformation with Retrieval-Augmented Generation (RAG) systems that combine large language models with real-time access to enterprise knowledge bases. These systems democratize access to institutional knowledge but create new security considerations due to dynamic connections between user queries and enterprise data, requiring adapted access control and validation unlike traditional applications.

-----

-----

Phase: [EXPLORATION]

### Source [92]: https://medium.com/fluree/how-decentralized-graphrag-improves-genai-accuracy-0cb3fd861712

Query: In what ways is the rise of decentralized AI and blockchain-based knowledge sharing transforming the security and provenance aspects of enterprise RAG deployments?

Answer: Decentralized Knowledge Graphs solve privacy and safety barriers in RAG-GenAI with a data-centric security approach, embedding policies at the data layer for dynamic enforcement of governance, regulation, copyright, and privacy on real-time data. Fluree uses cryptography for tamper-proof audit trails, enabling traceability to data origins, history review, and improved explainability. This allows secure, real-time access to enterprise knowledge across sources for RAG, reducing hallucinations with trusted, authoritative data while managing granular security built-in.

-----

-----

Phase: [EXPLORATION]

### Source [93]: https://par.nsf.gov/biblio/10578004-rag-privacy-preserving-framework-decentralized-rag-using-blockchain

Query: In what ways is the rise of decentralized AI and blockchain-based knowledge sharing transforming the security and provenance aspects of enterprise RAG deployments?

Answer: D-RAG is a privacy-preserving framework for decentralized RAG using blockchain. RAG enhances LLMs by retrieving relevant information from large knowledge bases without retraining. It employs Fully Homomorphic Encryption (FHE) for privacy during query processing (encrypted query embedding for k-means similarity ranking) and Private Information Retrieval (PIR) to privately retrieve top-ranked documents and embeddings. RAGtime-PIANO provides a lightweight, fully secure RAG protocol ensuring complete security in decentralized processing.

-----

-----

Phase: [EXPLORATION]

### Source [94]: https://review.stanfordblockchain.xyz/p/56-sahara-ai-the-decentralized-blockchain

Query: In what ways is the rise of decentralized AI and blockchain-based knowledge sharing transforming the security and provenance aspects of enterprise RAG deployments?

Answer: Sahara AI's decentralized blockchain platform manages sovereignty and provenance of AI assets. The Execution Layer logs all activities (model access, data usage, computation) on the Sahara Blockchain via SAPs and SBPs. It interacts with the Data Layer using vault abstractions and protocols for secure data access in training and RAG, ensuring privacy, security, and integrity through integrated mechanisms.

-----

-----

Phase: [EXPLORATION]

### Source [95]: https://flur.ee/fluree-blog/how-decentralized-graphrag-improves-genai-accuracy/

Query: In what ways is the rise of decentralized AI and blockchain-based knowledge sharing transforming the security and provenance aspects of enterprise RAG deployments?

Answer: Decentralized Knowledge Graphs (DKGs) are networks of independently managed graphs connected at query time based on rights and permissions, enabling secure, real-time access to broad enterprise knowledge for RAG. Fluree automates data silo conversion to semantic knowledge graphs with embedded security policies protecting against unwanted exposure, and adds digital cryptography at the data tier for verifying data authenticity. This supports accurate GenAI by grounding in trusted sources, outperforming traditional systems in reducing hallucinations with ontological context and provenance.

-----

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

Over the last year, more teams have started moving from that “one-pass” pipeline towards agent-like loops that can retry retrieval and call tools when the first pass is weak. [Gartner](https://www.gartner.com/en/newsroom/press-reports/2023-11-29-gartner-says-more-than-80-percent-of-enterprises-will-have-used-generative-ai-apis-or-deployed-generative-ai-enabled-applications-by-2026) even forecasts that **33% of enterprise software applications will include agentic AI by 2028**, a sign that “agentic” patterns are becoming mainstream rather than niche.

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

|  | High error tolerance | Low error tolerance |
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

<research_source type="scraped_from_research" phase="exploitation" file="improving-rag-accuracy-10-techniques-that-actually-work.md">
<details>
<summary>10 techniques to improve RAG accuracy</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://redis.io/blog/10-techniques-to-improve-rag-accuracy/>

# 10 techniques to improve RAG accuracy

February 25, 202614 minute read

[Manvinder Singh](https://redis.io/blog/author/manvindersingh/)

https://cdn.sanity.io/images/sy1jschh/production/38c9d03ecf54e2c6ceb4a870f40a9eab1661c9ef-406x406.jpg?w=828&q=80&fit=clip&auto=format

Manvinder Singh

### Key takeaways

- Retrieval augmented generation (RAG) improves AI accuracy by grounding LLM outputs in verified, domain-specific context rather than relying on static training data alone.
- Start simple: baseline a naive RAG pipeline, then measure and iterate with clear metrics.
- Strengthen retrieval: use hybrid search to bridge keyword and vector gaps, tune HNSW indices, and optimize chunking.
- Specialize models: fine-tune [vector embeddings](https://redis.io/glossary/vector-embeddings/) for domain language and LLMs for tone, format, or compliance.
- Stabilize answers: apply semantic [caching](https://redis.io/solutions/caching/) for FAQs and manage long-term memory for multi-turn interactions.
- Improve fidelity: use query transforms to clarify vague inputs, add an LLM as judge to evaluate faithfulness, and re-rank noisy results.

## **How RAG improves the accuracy of AI responses**

You've probably seen this before: your LLM confidently answers a question about your company's refund policy—except the policy changed six months ago, and the model has no idea. LLMs have a hard knowledge cutoff. Their parametric knowledge is frozen the moment training ends, and they don't know what they don't know. Modern LLMs extend beyond this through tool use, web browsing, and retrieval systems, but those are external additions, not inherent model capabilities. Without them, even a capable model will struggle with recent or domain-specific information.

[Retrieval augmented generation (RAG)](https://redis.io/glossary/retrieval-augmented-generation/) is the most widely adopted approach to closing that gap. It searches a knowledge base for relevant documents before generating a response, grounding outputs in your actual data instead of relying on the model's training alone.

But basic RAG only gets you so far. Poor chunking, weak retrieval, and untuned models all chip away at accuracy in ways that aren't immediately obvious. The fix is systematic optimization: baseline a naive pipeline, define quantitative metrics using frameworks like [Retrieval Augmented Generation Assessment (RAGAS)](https://redis.io/blog/get-better-rag-responses-with-ragas/), and iterate by fixing one weak link at a time.

This guide covers the 10 [RAG accuracy](https://redis.io/docs/latest/develop/get-started/rag/) techniques that consistently deliver the largest gains, along with when and why to apply each one.

## **1\. Hybrid search**

The most common RAG accuracy problem is retrieval failure: the right document exists in your corpus, but the system doesn't surface it. Semantic vector search captures conceptual similarity well, but it can miss documents where exact terminology matters, like part numbers, regulatory codes, proper nouns, and domain-specific jargon. Pure keyword matching has the opposite problem, missing conceptually related content that uses different vocabulary than the query.

Hybrid search runs both approaches in parallel and fuses the results. Combining BM25 keyword matching with vector similarity means your system captures both exact-match precision and semantic recall simultaneously. For mixed or structured corpora like legal documents, technical manuals, and medical records, this is often the single biggest accuracy lever available.

Redis Query Engine supports hybrid queries natively through the FT.HYBRID command introduced in [Redis 8.4](https://redis.io/blog/revamping-context-oriented-retrieval-with-hybrid-search-in-redis-84/), combining BM25 and vector similarity from a single query interface without external post-processing. Score fusion happens inside the query engine using Reciprocal Rank Fusion (RRF) or linear combination methods, preserving consistent normalization across both retrieval signals. Research on hybrid RAG systems, including [Blended RAG and HyPA-RAG](https://redis.io/blog/revamping-context-oriented-retrieval-with-hybrid-search-in-redis-84/), found that combining keyword and vector searches improved retrieval recall by 3 to 3.5 times and raised end-to-end answer accuracy by 11 to 15 percent on complex reasoning tasks. To get started, see the [hybrid search tutorial](https://github.com/redis-developer/redis-ai-resources/blob/main/python-recipes/vector-search/02_hybrid_search.ipynb).

## **2\. Tuning HNSW indices for retrieval precision**

Vector search accuracy depends on more than just the embedding model. Hierarchical Navigable Small World (HNSW) indices organize vectors into a multi-layered graph for fast approximate nearest-neighbor search, but the default parameters aren't optimized for every workload.

Three parameters govern the accuracy-performance tradeoff:

- **M (maximum connections per node).** Higher M creates denser graphs with more connections, improving recall and retrieval consistency, especially when your corpus contains similar but subtly distinct entries like FAQ variants or near-duplicate documents.
- **EF\_CONSTRUCTION (search depth during index building).** Controls how thoroughly the algorithm explores the graph while inserting new vectors. Higher values produce a better-connected graph at the cost of longer index build times.
- **EF\_RUNTIME (search depth during queries).** Controls how many candidate neighbors the algorithm examines per query. Higher values improve recall at the cost of slightly higher latency.

Redis' [published benchmarks](https://redis.io/blog/benchmarking-results-for-vector-databases/) suggest you may have headroom to raise EF\_RUNTIME values, and therefore improve recall, without violating latency SLAs, depending on your workload and K. In a billion-scale benchmark, Redis reported 90% precision at 200ms median latency when retrieving the top 100 nearest neighbors under 50 concurrent queries. That performance budget may let you trade a fraction of raw speed for denser graphs that deliver higher retrieval precision in production. More on [HNSW algorithms](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/).

## **3\. Chunking & parsing optimization**

How you split documents before indexing them determines what context your LLM actually receives. Fixed-length chunking, splitting at uniform token counts regardless of content structure, is the default for most pipelines, but it has a predictable failure mode: it breaks coherent ideas across chunk boundaries, separating information that should appear together and leaving the model to work with fragments.

Better chunking strategies respect semantic boundaries. Splitting at paragraph breaks, section headers, or points of topical discontinuity (identified through embedding similarity between consecutive sentences) keeps related information together. Each retrieved chunk should represent a complete thought rather than half of one. Moving from fixed-length to adaptive chunking can meaningfully improve both retrieval precision and recall because the model receives more coherent context and makes better use of it.

Redis integrates cleanly with chunking-aware frameworks like LangChain and LlamaIndex, making it straightforward to iterate across chunking strategies without rebuilding your pipeline. See the [LangChain RAG notebook](https://github.com/redis-developer/redis-ai-resources/blob/main/python-recipes/RAG/02_langchain.ipynb) for a practical starting point.

## **4\. Fine-tuning embeddings for domain-specific accuracy**

Generic embedding models trained on broad internet-scale text learn general semantic relationships. In specialized domains, those relationships don't always hold. A generic model might score "cardiac arrhythmia" and "irregular heartbeat" as moderately similar when a cardiologist would treat them as equivalent, or fail to distinguish between legal concepts that differ only in subtle doctrinal detail.

Fine-tuning [vector embeddings](https://redis.io/glossary/vector-embeddings/) on domain-specific labeled pairs, using contrastive learning or MultipleNegativesRankingLoss, teaches the model the semantic relationships that matter in your corpus. Even with modest training data, fine-tuned compact models often outperform much larger generic models on domain-specific retrieval tasks, which also reduces inference overhead.

Redis supports storing and querying multiple embedding models in parallel, so you can run a fine-tuned domain model alongside your existing generic model for A/B testing without rebuilding your index from scratch. More details in our blog on [fine-tuning embeddings for RAG](https://redis.io/blog/get-better-rag-by-fine-tuning-embedding-models/).

## **5\. Fine-tuning the LLM**

Retrieval quality determines what information reaches the model, but the model's own weights determine what it does with that information. If your RAG system consistently gets retrieval right but fumbles the response (wrong tone, inconsistent citation format, safety disclaimers that don't match your compliance requirements), the problem is in generation, not retrieval.

LLM fine-tuning addresses this by training the model on examples that demonstrate exactly the behavior you need: how to cite sources, what format responses should follow, how to handle edge cases, and what language to use for your domain. Parameter-efficient techniques like Low-Rank Adaptation (LoRA) make this practical without retraining billion-parameter models from scratch. You adapt the model's behavior without destroying its broader knowledge. This is especially valuable in high-stakes domains like healthcare or finance, where response format and compliance language need to be consistent across every interaction, not just statistically likely.

## **6\. Semantic caching for consistency & cost**

Semantic caching improves RAG accuracy in an often-overlooked way: by making responses consistent. When two users ask semantically identical questions ("How do I reset my password?" and "I forgot my login credentials"), a system that regenerates responses independently introduces variability. Cached responses are consistent—semantically similar queries that hit the same cache entry get the same answer, which matters when accuracy depends on consistency.

[Redis LangCache (preview)](https://redis.io/langcache/) implements semantic caching by converting queries to [vector embeddings](https://redis.io/glossary/vector-embeddings/) and comparing them against previously cached query embeddings using a similarity threshold. When a new query is semantically close enough to a cached one, the system returns the cached response rather than invoking the LLM again. This is particularly valuable for stable knowledge bases (FAQs, product docs, internal policy queries) where high-confidence answers exist and should be served reliably. In conversational workloads with optimized configurations, Redis LangCache has achieved up to 73% cost reduction, and cached responses return in milliseconds rather than seconds. See the [Redis LangCache docs](https://redis.io/docs/latest/develop/ai/langcache/) for setup and API details.

## **7\. Long-term memory management for multi-turn accuracy**

Single-turn RAG is straightforward: retrieve relevant documents, augment the prompt, generate a response. Multi-turn interactions are harder. Without explicit memory management, each query starts from scratch. The model loses context from prior exchanges, can't build on established preferences, and forces users to re-establish context they've already provided.

Long-term memory solves this by storing interaction history as vector embeddings and retrieving semantically relevant past exchanges as context for new queries. Rather than concatenating an ever-growing conversation transcript (which bloats context windows and triggers the "lost-in-the-middle" accuracy problem), semantic memory retrieval surfaces only the prior exchanges relevant to the current question. This keeps context windows lean and focused, which generally improves model reasoning quality. The [langgraph-checkpoint-redis](https://github.com/redis-developer/langgraph-redis) package provides both thread-level session persistence through RedisSaver and cross-thread long-term memory through RedisStore with vector search. More in our blog on [building agent memory with Redis and LangGraph](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/).

## **8\. Query transforms to improve retrieval coverage**

Retrieval quality depends on how well the query matches the document corpus, and users rarely phrase questions the way technical documents are written. A user asking "What's broken with my internet?" won't naturally match troubleshooting docs written in terms of "network connectivity diagnostics" or "ISP service verification." The semantic distance between user intent and document language degrades retrieval before generation even starts.

Query transformation techniques close this gap. Hypothetical Document Embeddings (HyDE) generates a synthetic answer to the user's query, then uses that synthetic document as the retrieval query instead of the original question. Because the hypothetical answer is written in the language of answers, not questions, it tends to match actual documents more closely. Multi-query generation creates several reformulations of the original query in parallel, then retrieves using all variants to maximize recall. Both techniques add inference overhead, so they're best applied adaptively: trigger query transformation when initial retrieval returns weak results, skip it when standard retrieval is already surfacing strong candidates.

## **9\. LLM as judge for faithfulness evaluation**

Measuring RAG accuracy requires evaluating two things independently: whether retrieval surfaced the right documents, and whether generation stayed faithful to those documents. Human evaluation is the gold standard but doesn't scale. Automated metrics like BLEU or ROUGE measure surface-level similarity, not faithfulness. LLM-as-judge fills the gap by using a capable model to score responses against defined criteria at scale.

A faithfulness judge evaluates whether the generated response is grounded in the retrieved context or invents unsupported details. A relevance judge assesses whether the response actually addresses the user's question. A context precision judge evaluates whether the retrieved documents appear in the right rank order. GPT-4 evaluators [match human annotator agreement levels](https://arxiv.org/abs/2306.05685)—over 80% on pairwise comparisons—though agreement can drop in specialized domains like medicine or law. Frameworks like [RAGAS](https://redis.io/blog/get-better-rag-responses-with-ragas/) operationalize this approach and integrate directly with Redis-backed pipelines.

## **10\. Re-ranking for precision refinement**

Initial vector or hybrid retrieval is optimized for recall: getting potentially relevant documents into the candidate set. But the ranking of those candidates often leaves something to be desired. Documents ranked 8th or 9th in initial retrieval may be more relevant than those ranked 2nd or 3rd, and LLMs tend to pay more attention to context that appears early in their input.

Re-ranking addresses this with a second-pass model that scores query-document pairs jointly rather than independently. Cross-encoder models process query and document tokens together, allowing for richer relevance assessment than the bi-encoder approach used during initial retrieval. The computational cost is higher per document, but because re-ranking operates on a small candidate set (typically top 20 to 100 from initial retrieval) rather than the full corpus, it's practical in production. Mature implementations report 10 to 40 percent precision improvements depending on baseline quality and domain complexity. See our blog on [fine-tuning rerankers for better retrieval](https://redis.io/blog/improving-information-retrieval-with-fine-tuned-rerankers).

| Technique | Description | Best use cases |
| --- | --- | --- |
| 1\. Hybrid search | Combines keyword matching (BM25) with semantic vector search | • Legal/technical documents • Domain-specific jargon • Mixed structured/unstructured data |
| 2\. Tuning HNSW indices | Optimizes vector index by creating denser search graphs via M and efConstruction parameters | • Near-duplicate documents • FAQ variants • Similar product specs |
| 3\. Chunking & parsing | Optimizes document splitting by sentence, paragraph, or semantic sections | • Complex document structures • Medical records • Policy manuals |
| 4\. Fine-tune embeddings | Customizes embedding models for specialized domains using contrastive learning | • Law, finance, pharma • Domain-specific terminology • Nuanced language |
| 5\. Fine-tune LLM | Adapts the language model for specific response formats and tones | • Healthcare/finance compliance • Specific citation formats • Regulatory constraints |
| 6\. Semantic caching | Pre-loads high-confidence answers using vector similarity matching | • FAQs • Product documentation • Stable knowledge bases |
| 7\. Long-term memory | Persists user interactions and context across sessions | • Multi-turn dialogues • Coaching apps • Support agents |
| 8\. Query transforms | Enriches vague queries using techniques like HyDE | • Ambiguous queries • Terse inputs • Open-domain systems |
| 9\. LLM as judge | Uses LLM to evaluate response faithfulness against retrieved context | • High-stakes apps • Legal/healthcare • Enterprise search |
| 10\. Re-ranking | Reorders retrieval results using ML models or secondary LLM pass | • Noisy corpora • Multiple retrieval sources • Low initial precision |

## **The path to more accurate RAG**

These 10 techniques are a proven toolkit for improving RAG accuracy, but the order matters. Start with retrieval fundamentals (hybrid search, chunking, HNSW tuning) before moving to model customization (embedding fine-tuning, LLM fine-tuning). Accuracy measurement through LLM-as-judge should run throughout, not just at the end. Advanced patterns like [agentic RAG orchestration](https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/), metadata conditioning, and prompt tuning build on top of a solid foundation, not a substitute for one.

Redis provides the unified real-time infrastructure to run this entire stack: vector search and hybrid retrieval through Redis Query Engine, semantic caching through [Redis LangCache](https://redis.io/langcache/) (preview), [agent memory](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/) through Redis' native data structures and [vector indexing](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/), and integrations with 30+ AI frameworks including LangChain, LangGraph, and LlamaIndex. You don't need a separate vector database, a separate cache, and a separate session store. Redis delivers sub-millisecond access for caching and session operations, and low-latency vector retrieval at scale, simplifying the pipeline and reducing the operational surface area you're debugging when accuracy degrades.

The full set of [RAG and GenAI resources](https://github.com/redis-developer/redis-ai-resources) in the Redis developer repository covers each technique with working code examples. [Try Redis free](https://redis.io/try-free/) to see how the platform performs against your workload, or [talk to our team](https://redis.io/meeting/) about building production-grade RAG pipelines that actually stay accurate at scale.

## **Frequently asked questions about RAG**

### **What is the recommended order for implementing RAG optimization techniques to get the biggest accuracy improvements first?**

Start by establishing baseline metrics using frameworks like RAGAS, then prioritize retrieval quality first: hybrid search, chunking optimization, and HNSW tuning. Even the best LLM cannot compensate for missing or irrelevant source documents. Once retrieval is reliable, move to model specialization like fine-tuning embeddings and adapting the LLM for domain-specific needs.

Run LLM-as-judge evaluation continuously throughout to catch regressions early. Layer on advanced techniques like query transformation, re-ranking, semantic caching, and long-term memory only after foundational elements are stable, as these amplify existing quality rather than compensating for structural weaknesses.

### **How does hybrid search combining BM25 and vector similarity compare to using either approach alone in terms of retrieval recall and answer accuracy?**

BM25 excels at exact terminology and rare tokens but fails on synonyms, while vector search captures semantic meaning but struggles with homonyms and precision-critical terms. Hybrid search fuses both via methods like Reciprocal Rank Fusion. [Microsoft's Azure AI Search benchmarks](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/azure-ai-search-outperforming-vector-search-with-hybrid-retrieval-and-reranking/3929167) found that hybrid retrieval improved NDCG scores by roughly 10-20% over single-mode approaches across customer and academic datasets, with further gains when combined with semantic reranking. Exact improvements vary by dataset and configuration.

This dual-mode approach is especially valuable in enterprise settings where documents mix structured metadata needing exact matching with unstructured content needing semantic understanding, letting systems handle diverse query types without requiring users to reformulate their questions.

### **How should I approach tuning HNSW index parameters (M, EF\_CONSTRUCTION, EF\_RUNTIME) for my RAG pipeline?**

The three parameters control different tradeoffs. EF\_RUNTIME is the easiest to adjust since it affects query-time recall without requiring reindexing; raise it incrementally until you hit your latency ceiling. M affects graph connectivity and memory consumption; higher values improve recall but increase storage requirements. EF\_CONSTRUCTION mainly affects index build quality and time.

The right values depend on your corpus size, query patterns, and latency requirements. Start with your vector database's recommended defaults, then tune incrementally while measuring retrieval recall at your target K values against your actual corpus and query distribution rather than synthetic benchmarks.

### **How do query transformation techniques like HyDE and multi-query generation work, and when should they be triggered versus skipped to avoid unnecessary inference overhead?**

HyDE prompts an LLM to generate a hypothetical answer matching your corpus style, then searches using that synthetic document's embedding instead of the raw query, effectively comparing document-to-document rather than question-to-document. Multi-query generation creates parallel reformulations of the original question and merges retrieval results across all variants to maximize coverage. Both require additional LLM inference calls before retrieval begins.

Use adaptive triggering: skip transformation when initial retrieval returns high-confidence results, and apply it only when results are weak or below a confidence cutoff. Simple factual lookups rarely need transformation, while ambiguous or exploratory queries benefit most. Apply selectively to balance accuracy against latency costs.

### **How can I measure RAG pipeline accuracy using the LLM-as-judge approach, and what faithfulness score thresholds indicate production readiness?**

Construct evaluation prompts that score responses on faithfulness, relevance, and context precision using structured JSON output with numeric scores and reasoning chains. Target faithfulness above 0.85 on a normalized scale for general use, though regulated domains like finance and healthcare may require 0.90+, while customer support may tolerate 0.80 with human escalation.

Validate your judge against human annotations for the first 200–500 responses, use temperature zero for consistency, and monitor score distributions over time, not just averages. Be aware that LLM judges can exhibit systematic biases such as preferring longer responses and showing positional bias, so calibration against human-verified datasets is essential. Sample 5–10 percent of production traffic through the judge pipeline daily to catch silent accuracy degradation from corpus changes and usage drift.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="rag-system-in-production-architecture-chunking-evaluation-gu.md">
<details>
<summary>RAG System in Production: Why It Fails and How to Fix It</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/>

# RAG System in Production: Why It Fails and How to Fix It

ByKamalpreet Singh.Tech Lead,Aditya Pathak.Senior Software Engineer

https://47billion.com/wp-content/uploads/2026/03/RAG-System-in-Production-Compress-1024x536.webp

_From embeddings to evaluation: a practitioner’s guide to building RAG that actually works in production_

When we started building AI-powered document Q&A into our products, we made the same mistake most teams make.

We picked a vector database. We embedded our documents. We wired up GPT-4. We called it RAG.

And for a while, it looked like it was working.

Then someone asked a question that spanned three sections of a report. The answer came back confidently wrong. Not hallucinated — the information was _there_, in the document. The system just couldn’t find the right pieces and stitch them together.

That’s when we realized the problem wasn’t our LLM. It wasn’t our vector database. It was everything that happened _before_ retrieval — and everything we weren’t measuring _after_ generation. Designing this layer correctly is critical for teams building scalable, production-ready systems through structured [**enterprise AI development services**](https://47billion.com/machine-learning/).

This is that story. And more importantly, this is what we learned.

**The Problem With “Just Add RAG”**

RAG — Retrieval-Augmented Generation — sounds straightforward: retrieve relevant documents, pass them to an LLM, get a grounded answer. No hallucinations, no stale training data.

In practice, it’s a pipeline with at least five places where things can silently break.

Here’s what a naive RAG system looks like:

User Query → Embed Query → Vector Search → Top-K Chunks → LLM → Response

Each arrow is a potential failure point. And most teams only optimize the last one — the LLM.

https://47billion.com/wp-content/uploads/2026/03/image.png

**What LLMs Can and Can’t Do Alone**

Before we talk about RAG, let’s be clear about why it exists.

Large Language Models are trained on static text snapshots. They’re remarkably good at reasoning, summarizing, and generating — but they have three fundamental limitations that matter in production:

**Knowledge cutoff.** The model knows nothing about what happened after its training data were collected. For enterprise applications dealing with internal documents, policy updates, or real-time data, this is a dealbreaker.

**No private knowledge.** The model was never trained on your company’s documents, your product specs, or your customer data. You can’t fix this with fine-tuning alone — fine-tuning teaches _behavior_, not facts.

**Hallucination under uncertainty.** When an LLM doesn’t know something, it often doesn’t say “I don’t know.” It generates a plausible-sounding answer. This is fine for creative writing. It’s catastrophic for document Q&A, compliance, or medical applications.

RAG solves all three. But only if you build it correctly.

**Why RAG? The Actual Value Proposition**

The core idea: at inference time, retrieve relevant context from an external knowledge base and give it to the LLM as part of the prompt. The model then generates an answer grounded in what was retrieved — not what it vaguely remembers from training.

Without RAG: LLM answers from parametric memory → hallucination risk

With RAG: LLM answers from retrieved context → grounded, verifiable

This unlocks three things that matter for enterprise deployments:

**Updatability without retraining.** Update your knowledge base, and the system immediately knows the new information. No fine-tuning cycle, no redeployment.

**Attribution.** Every answer can be traced back to a source document. This is critical for compliance, legal, and regulated industries.

**Cost efficiency.** You don’t need the largest, most expensive model when the answer is literally in the context window. A smaller model with good retrieval outperforms a larger model with bad retrieval.

But here’s what the tutorials don’t tell you: the quality of your RAG system is almost entirely determined by what happens _before_ the LLM sees the query. Retrieval quality is the dominant variable.

**Where Naive RAG Fails**

RAG solves the LLM’s knowledge problem. But naive RAG — embed, retrieve top-K, generate — introduces its own failure modes. And these failures are silent: the system returns an answer, it just happens to be wrong.

Understanding these failure modes matters because every advanced technique covered in this guide exists to address one or more of them.

| **Failure Mode** | **What Happens** | **Example** |
| --- | --- | --- |
| **Vocabulary Mismatch** | User phrasing doesn’t match document phrasing | User asks “salary” but the document says “compensation package” |
| **Ambiguous Queries** | Query is too vague or has multiple valid interpretations | “Tell me about Python” — the snake, or the programming language? |
| **Lost in the Middle** | LLM underweights relevant chunks positioned in the middle of a long context | Correct answer is chunk 3 of 5 — the model effectively ignores it |
| **Irrelevant Top-K** | Cosine similarity returns semantically close but contextually wrong chunks | Returns results about “ML model training” when the question is about “ML model deployment” |
| **Chunking Artifacts** | Answer split across chunk boundaries — retrieved in neither | The explanation starts in chunk 7 and concludes in chunk 8 |
| **No Answer Available** | System hallucinates rather than admitting it doesn’t know | Generates a confident answer from tangentially related chunks |

Each section that follows — hybrid retrieval, advanced chunking, HyDE, reranking, evaluation — is a direct response to one or more rows in this table. Keep this map in mind as you read.

**Hybrid RAG: Beyond Pure Vector Search**

Most RAG tutorials show you one retrieval method: embed your query, find the nearest vectors, return the top-K results.

This is called **dense retrieval** — and it’s powerful but incomplete.

**The Problem With Pure Vector Search**

Dense retrieval is excellent at semantic similarity. Ask “what are the revenue figures for Q3?” and it finds chunks about financial performance even if they don’t contain that exact phrase.

But it fails on exact lookup. If you search for “Section 4.2.1” or “SKU-B4920” — a specific ID, a clause number, a product code — dense retrieval can miss it entirely. The embedding doesn’t capture character-level precision.

**The Problem With Pure Keyword Search**

BM25 and traditional keyword search (what Elasticsearch has used for decades) does the opposite. It’s extremely good at exact matches but fails on semantics. Search “how does the system handle payment failures?” and it might return nothing if the document says “transaction error recovery process” instead.

**Hybrid = Best of Both**

The solution is to run both in parallel and merge results. This is Hybrid RAG. In production systems, implementing hybrid retrieval effectively requires strong [**data engineering for AI systems**](https://47billion.com/big-data-analytics/), where indexing strategy, metadata design, and search orchestration directly impact retrieval accuracy.

Query

├── Dense Retrieval (embedding similarity) → candidates\_A

└── Sparse Retrieval (BM25 keyword search) → candidates\_B

            ↓

     Reciprocal Rank Fusion (RRF)

            ↓

     Unified Ranked Results

            ↓

     (Optional) Reranker

            ↓

     Final Top-K → LLM

**Reciprocal Rank Fusion (RRF)** is the standard method for merging ranked lists from different retrievers. It’s simple and surprisingly effective — each result gets a score of 1/(rank + k) from each retriever, and scores are summed to produce a final ranking.

https://47billion.com/wp-content/uploads/2026/03/image-3.png

**The Third Layer: Reranking**

After fusion, you still have 10-20 candidates. A **reranker** (cross-encoder) scores each retrieved chunk against the query — not just for embedding similarity, but for actual relevance.

Rerankers are slower than retrieval but more accurate. They process query+document pairs end-to-end, capturing nuance that bi-encoder embeddings miss. Models like Cohere Rerank, BGE Reranker, and Jina Reranker have become standard in production pipelines.

The flow: retrieve broadly → rerank precisely → send top 3-5 to LLM.

**Embeddings: The Layer Everyone Rushes Past**

Before you can retrieve anything, you need to represent your documents as vectors. The embedding model you choose matters more than most teams realize.

**What Embeddings Actually Are**

An embedding model converts text into a high-dimensional vector (typically 768 to 3072 dimensions). Semantically similar text produces geometrically close vectors. This is what enables semantic search.

**Choosing an Embedding Model**

Not all embedding models are created equal. Choosing the wrong one — especially for domain-specific content — can silently degrade your entire RAG system.

| **Model** | **Dimensions** | **Best For** |
| --- | --- | --- |
| text-embedding-3-small (OpenAI) | 1536 | General purpose, fast |
| text-embedding-3-large (OpenAI) | 3072 | Higher accuracy, more cost |
| BGE-M3 (BAAI) | 1024 | Multilingual, hybrid retrieval built-in |
| E5-Large-v2 | 1024 | Strong on MTEB benchmarks |
| Nomic Embed | 768 | Open source, self-hostable |
| Jina Embeddings v3 | 1024 | Long documents, late chunking support |

For specialized domains — legal, medical, code — domain-specific or fine-tuned embeddings consistently outperform general-purpose models.

**One Critical Thing Most Guides Skip: Embedding Dimensions Matter**

Larger embedding dimensions capture more nuance — but they’re also more expensive to store, index, and query. For most applications, text-embedding-3-small at 1536 dimensions is the right starting point. Upgrade only when benchmarks show clear improvement.

**Late Chunking: A Better Way to Embed Long Documents**

Traditional embedding: split the document into chunks, embed each chunk independently.

The problem: each chunk loses awareness of the document it came from. A chunk saying “the figure improved by 34%” has no context of what figure, in what context.

**Late Chunking** (introduced by Jina AI) inverts this: embed the _full document_ first using long-context models, then split the resulting token-level embeddings into chunks. Each chunk retains the global context of the document it belongs to.

The result: significantly better retrieval on long, structured documents where cross-section relationships matter.

**Chunking: The Most Underrated Decision in RAG**

Here’s the finding that should change how you think about RAG:

**Chunking strategy matters more than your choice of vector database.**

NVIDIA’s 2024 benchmarks across five document datasets found up to a 9% recall gap between the best and worst chunking strategies, with no other variable changed. A well-chunked corpus retrieves accurately on a basic vector DB. A poorly-chunked corpus fails even with the most sophisticated retrieval stack.

Yet most teams spend weeks evaluating vector databases and minutes thinking about chunking.

**Why Chunking Is Hard**

You’re trying to solve a fundamental tension:

- **Chunks too large** → embeddings average multiple topics → noisy retrieval → the system retrieves the right page but not the right answer

- **Chunks too small** → each chunk loses context → the answer exists but can’t be understood in isolation

The goal: chunks small enough to retrieve precisely, but complete enough to give the LLM sufficient context for generation.

https://47billion.com/wp-content/uploads/2026/03/image-2.png

**Strategy 1: Fixed-Size Chunking**

The simplest approach. Split every N tokens, with some overlap to avoid context loss at boundaries.

chunk\_size = 512 tokens

chunk\_overlap = 50 tokens

Easy to implement. Fast. The baseline every team starts with.

The problem: it’s document-agnostic. A sentence that starts at token 500 gets split at token 512, mid-thought. The next chunk has no idea what the previous one was discussing.

**Use when:** Homogeneous, unstructured text. FAQs. Simple corpora where you need something running quickly.

**Don’t use when:** Documents have natural structure — sections, headings, slides, tables.

**Strategy 2: Recursive Character Text Splitting**

The LangChain default. Instead of splitting blindly at N tokens, it tries to split at natural boundaries — paragraphs first, then sentences, then words — only falling back to character-level splits when necessary.

In Chroma’s benchmarks, RecursiveCharacterTextSplitter at 400-512 tokens delivered **85-90% recall** without the computational overhead of semantic methods. It’s a strong default for most teams.

**Use when:** Prose-heavy documents, articles, reports, general text corpora.

**Strategy 3: Semantic Chunking**

Instead of counting tokens, semantic chunking analyzes the embedding similarity between consecutive sentences. When similarity drops significantly — meaning the topic is shifting — it creates a new chunk boundary.

The result: chunks that respect topic boundaries, not arbitrary token counts. Each chunk contains one coherent idea.

The cost: requires embedding every sentence during preprocessing, which is computationally expensive. And it introduces a threshold parameter (how much similarity drop triggers a split?) that requires tuning per document type.

Benchmarks show up to **9% improvement in recall** over fixed-size chunking for well-structured documents.

**Use when:** Academic papers, long-form reports, content where topic coherence within chunks matters.

**Strategy 4: Hierarchical Chunking**

This is the approach that changes everything for structured documents.

The idea: documents have a natural hierarchy. A research paper has sections → subsections → paragraphs. A presentation has slides → sections → bullets. A legal document has articles → clauses → provisions.

Hierarchical chunking preserves this structure explicitly:

Parent Node: Full Section (context for generation)

Child Nodes: Individual Paragraphs (precision for retrieval)

At query time:

1. Retrieve child chunk (precise match)

2. Return parent chunk to LLM (full context)

This is sometimes called **Parent Document Retrieval** — retrieve small, generate with large.

The result: you get the retrieval precision of small chunks and the contextual completeness of large chunks. You don’t have to choose.

**Use when:** Presentations, reports with sections, legal documents, technical documentation, anything with meaningful structure. We cover this in depth in the case study below.

**Strategy 5: Page-Level Chunking**

In NVIDIA’s 2024 benchmark, this won — **0.648 accuracy** with the lowest variance across document types.

The reason: PDFs organize information by page deliberately. Financial reports put balance sheets on one page. Research papers put figures with their captions on the same page. Splitting across page boundaries destroys these relationships.

**Use when:** PDF-heavy corpora, financial reports, regulatory filings, academic papers.

**Don’t use when:** Your PDFs are just text exports with arbitrary page breaks — the page boundary carries no semantic meaning.

**Strategy 6: Proposition-Based Chunking**

Instead of splitting on structure or semantics, an LLM extracts atomic factual claims — “propositions” — from each passage. Each proposition becomes a chunk.

Original: “Revenue grew 34% YoY, driven primarily by enterprise subscriptions

           and geographic expansion into Southeast Asia.”

Propositions:

→ “Revenue grew 34% year-over-year.”

→ “Revenue growth was driven by enterprise subscriptions.”

→ “Revenue growth was driven by geographic expansion into Southeast Asia.”

The result: extremely high retrieval precision. Each chunk is a single, self-contained fact — no noise, no mixed topics.

The cost: expensive. Requires LLM calls during preprocessing. Not practical for large corpora at scale without careful budgeting.

**Use when:** High-stakes, precision-critical applications. Legal Q&A, compliance checking, medical decision support. When incorrect retrieval has real consequences.

**Chunking Strategy Selection Guide**

| **Document Type** | **Recommended Strategy** | **Why** |
| --- | --- | --- |
| PDFs (structured) | Page-level | Respects visual organization |
| Research papers | Semantic + Hierarchical | Topic coherence + section context |
| Presentations / Slides | **Hierarchical** | Structure is the meaning |
| Legal documents | Proposition-based | Precision is non-negotiable |
| FAQs / Chat logs | Sentence-level | Self-contained questions |
| Code documentation | Recursive (language-aware) | AST-aware boundaries |
| Mixed / Unstructured | Contextual Retrieval | Adds context regardless of structure |

**Two More Methods Worth Knowing**

**Contextual Retrieval** (Anthropic, 2024): Before embedding, prepend a generated context summary to each chunk — e.g., “This chunk is from Section 3 of the Q3 earnings report, discussing operating margins.” This anchors the chunk in its document context without changing the chunk boundaries. Particularly effective when combined with BM25 hybrid search.

**Cluster-Based / Agentic Chunking**: Uses optimization algorithms (or LLM agents) to find chunk boundaries that maximize a “semantic reward” — coherence within chunks, dissimilarity across chunks. Computationally expensive but produces the best boundaries for complex documents.

**Retrieval Strategies: Beyond Top-K**

Once your corpus is chunked and indexed, how you actually retrieve matters.

**Naive Top-K**

Return the K most similar chunks to the query embedding. Simple. Works for simple queries.

Fails when: the question requires synthesizing information from multiple sections, or when the K most similar chunks are all slight variations of the same passage (redundant retrieval).

**MMR — Maximal Marginal Relevance**

Returns diverse results rather than the K most similar. After selecting the top result, each subsequent result is chosen to maximize relevance _and_ minimize overlap with already-selected chunks.

The result: a retrieval set that covers different aspects of the answer, not five versions of the same paragraph.

**Use when:** Summarization tasks, broad questions, anytime redundancy is a concern.

**HyDE — Hypothetical Document Embeddings**

One of the most underrated techniques in advanced RAG.

The problem: there’s often a distribution gap between queries and documents. A user asks a question. Documents contain answers. Questions and answers are phrased very differently — and this mismatch degrades embedding similarity.

HyDE closes this gap:

1. Take the user’s query

2. Generate a hypothetical answer using the LLM (no retrieval yet)

3. Embed the hypothetical answer

4. Use that embedding to search the vector store

5. Retrieve real chunks closest to the hypothetical answer

6. Pass retrieved chunks + original query to LLM for final generation

The hypothetical answer is never shown to the user. It’s just a better search vector.

- In benchmarks, HyDE improves retrieval performance significantly on knowledge-intensive tasks, especially when queries are short and vague while documents are detailed.

https://47billion.com/wp-content/uploads/2026/03/image-1.png

**Multi-Query Retrieval**

Generate N semantically different paraphrases of the user’s query, retrieve chunks for each, deduplicate, and merge. Catches chunks that would be missed if the user’s specific phrasing didn’t match the document’s phrasing.

**Sub-Query Decomposition**

Complex, multi-part questions are often too broad for a single retrieval pass. Sub-Query Decomposition breaks the original query into smaller, focused sub-queries, retrieves independently for each, then synthesizes the results before passing them to the LLM.

Original: “Compare the machine learning approaches used by Google and Meta

           for content recommendation”

Sub-queries:

→ “Google machine learning content recommendation system”

→ “Meta machine learning recommendation approach”

→ “Comparison of recommendation systems in big tech”

Each sub-query targets a specific slice of the answer. The retrieved chunks are merged and deduplicated, giving the LLM complete, structured context to reason across — rather than forcing it to infer comparisons from a single ambiguous retrieval.

**Use when:** Questions that span multiple entities, time periods, or concepts. Comparative analysis, multi-hop reasoning, research queries.

**Step-Back Prompting**

For narrow, specific queries, retrieval often misses the broader context. Step-Back prompting first abstracts the query — “What are the principles behind X?” — retrieves on the abstracted query, then uses both abstract context and specific query for generation.

Useful when questions are highly specific but require background understanding.

**Self-RAG**

The model itself decides whether to retrieve and what to retrieve. It generates a response, evaluates whether it needs external information, retrieves if necessary, and iterates. More agentic. More expensive. Significantly better at multi-hop reasoning.

**Evaluating RAG: What Actually Matters**

Here’s where most teams are completely flying blind.

Teams deploy RAG, try a few queries manually, and call it good. They have no metrics. They don’t know if their system is getting better or worse as they iterate. Evaluation should be part of broader [**LLM infrastructure best practices**](https://47billion.com/blog/from-prompt-chaos-to-production-building-enterprise-grade-llm-infrastructure/), not something added after deployment.

**Why BLEU and ROUGE Are Not Enough**

BLEU and ROUGE measure n-gram overlap between a generated answer and a reference answer. They were designed for machine translation and summarization — where the output should look like the reference.

RAG has different requirements. A correct answer that uses different phrasing from the reference will score poorly on BLEU. An answer that sounds similar but uses wrong facts from the document will score well.

You need metrics that evaluate _factual grounding_, not _surface similarity_.

**The Three Evaluation Layers**

Layer 1: Retrieval Quality

→ Is the right information being found?

Layer 2: Generation Quality

→ Is the LLM using what was retrieved correctly?

Layer 3: End-to-End Quality

→ Does the final answer actually answer the question?

| **Layer** | **Metric** | **What It Measures** |
| --- | --- | --- |
| Retrieval | Precision@K | What fraction of retrieved chunks are actually relevant? |
| Retrieval | Recall@K | What fraction of relevant chunks were retrieved? |
| Retrieval | MRR | Is the first relevant chunk ranked high? |
| Retrieval | nDCG | Is the overall ranking quality good? |
| Generation | BERTScore | Semantic similarity (better than BLEU for RAG) |
| Generation | ROUGE | Token-level overlap with reference |
| End-to-end | Faithfulness | Does the answer stick to retrieved context? |
| End-to-end | Answer Relevancy | Does the answer address the question? |
| End-to-end | Context Precision | Was the retrieved context actually useful? |
| End-to-end | Context Recall | Did we retrieve all the context needed? |

**RAGAS: Automated RAG Evaluation**

RAGAS (Retrieval Augmented Generation Assessment) is the standard framework for automated RAG evaluation. Its key insight: you don’t need human-annotated ground truth for every metric. LLM-as-judge can evaluate faithfulness, relevance, and context quality at scale.

from ragas import evaluate

from ragas.metrics import faithfulness, answer\_relevancy, context\_precision

results = evaluate(

    dataset=test\_dataset,

    metrics=\[faithfulness, answer\_relevancy, context\_precision\]

)

**Faithfulness** is the most critical metric. It measures whether every claim in the generated answer is grounded in the retrieved context. A faithfulness score below 0.8 means your LLM is hallucinating — even when retrieval is working.

**Answer Relevancy** measures whether the answer addresses the actual question. A system can be perfectly faithful (sticking to retrieved context) but still irrelevant if it retrieves the wrong content.

**Context Precision** tells you if your retrieval is returning noise alongside relevant chunks. High precision means everything retrieved is useful. Low precision means your reranking needs work.

Other evaluation tools: **DeepEval** (uses G-Eval with custom rubrics), **TruLens** (focuses on the “RAG triad” of groundedness, answer relevance, context relevance), **Arize Phoenix** (production monitoring and tracing).

**Case Study: Why Hierarchical Chunking Is Essential for Presentation-Based AI**

This isn’t theoretical. This is a problem we hit building AI-powered Q&A over university presentation content.

**The Setup**

Universities share large volumes of structured content with students — course presentations, placement preparation decks, syllabus documents. These presentations have a clear hierarchy:

Presentation

└── Section: “Placement Preparation”

        └── Slide: “Interview Skills”

              └── Bullet: “Maintain eye contact with the interviewer”

              └── Bullet: “Structure answers using STAR method”

              └── Sub-bullet: “Situation → Task → Action → Result”

A student asks: _“What technique should I use to answer behavioral interview questions?”_

The correct answer is the STAR method. It lives in a sub-bullet on slide 7 of a 45-slide presentation.

**What Naive Chunking Does**

With 512-token fixed-size chunking, the processor doesn’t know about slides, sections, or bullets. It splits the text mechanically.

The sub-bullet “Situation → Task → Action → Result” might end up in a chunk that looks like:

…communication skills important for success in technical roles.

Situation → Task → Action → Result. Practice with common behavioral

questions before your interview. Research the company thoroughly…

When retrieved, this chunk gets passed to the LLM. The LLM sees fragments from three different bullet points. It generates an answer that’s vague, inconsistent, or misattributed. The STAR method might be mentioned, but without the context that it’s specifically for behavioral questions and interview preparation.

**What Hierarchical Chunking Does**

With hierarchical indexing, the structure is preserved:

Parent Node (stored, not retrieved):

“Section: Placement Preparation → Slide: Interview Skills — This slide

covers structured communication techniques for interview success,

including the STAR method for behavioral questions.”

Child Node (indexed for retrieval):

“Use the STAR method to answer behavioral interview questions:

Situation → Task → Action → Result.”

Query matches the child node precisely. The LLM receives the parent node as context — so it knows _why_ STAR is being discussed, _where_ in the curriculum it appears, and _what_ it applies to.

The response is specific, contextually correct, and attributable.

**The Numbers**

Across our internal benchmark on 200 student queries over 15 university presentation decks:

| **Chunking Strategy** | **Answer Accuracy** | **Faithfulness** | **Context Precision** |
| --- | --- | --- | --- |
| Fixed-size (512 tokens) | 61% | 0.74 | 0.58 |
| Semantic chunking | 72% | 0.81 | 0.69 |
| **Hierarchical (parent-child)** | **89%** | **0.91** | **0.84** |

The hierarchical approach didn’t just improve accuracy — it specifically improved the cases that matter most: questions that require understanding _where_ a piece of information sits in the document, not just _that_ it exists.

**The Broader Principle**

Any time your document’s structure carries meaning — presentations, legal contracts with numbered clauses, technical specs with sections and subsections, financial reports with organized statements — hierarchical chunking is not optional. It’s the only approach that respects what the document is actually saying.

https://47billion.com/wp-content/uploads/2026/03/image-4.png

**The Full Production RAG Stack**

Here’s what a production-grade RAG system actually looks like, integrated end-to-end:

                       INGESTION PIPELINE

                        ──────────────────

Raw Documents → Document Parser → Structure Detection

    → Chunking Strategy (per doc type) → Embedding Model

    → Vector Store + Keyword Index

                        RETRIEVAL PIPELINE

                        ──────────────────

User Query → Query Analysis → \[HyDE / Multi-Query\]

    → Dense Retrieval + Sparse Retrieval → RRF Fusion

    → Reranker → Top-K Chunks

                        GENERATION PIPELINE

                        ──────────────────

Top-K Chunks + Query → Context Assembly → LLM

    → Response → Citation Extraction

                        EVALUATION LAYER

                        ────────────────

RAGAS: Faithfulness / Answer Relevancy / Context Precision

Retrieval: Precision@K / Recall@K / MRR

Production: Latency / Throughput / Cost per Query

https://47billion.com/wp-content/uploads/2026/03/image-5.png

**Common RAG Anti-Patterns (And How to Avoid Them)**

After building and debugging RAG in production, these are the mistakes we see most often:

**Skipping retrieval evaluation.** Teams measure end-to-end accuracy but never separately measure whether retrieval is working. A system can fail because of bad chunking, bad embeddings, bad retrieval, or bad generation — and without layer-specific metrics, you’re debugging blindly.

**One chunking strategy for all document types.** A single 512-token splitter applied to PDFs, slides, legal docs, and code. Each document type has different structure. The right chunking strategy depends on what the document is, not just how long it is.

**No overlap in fixed-size chunks.** Information split at the boundary of two chunks exists in neither. At minimum, 10-15% overlap prevents this. Hierarchical chunking is the proper fix.

**Embedding model mismatch.** Using a general-purpose embedding model for highly specialized content (medical, legal, technical) without checking whether a domain-specific model performs better.

**Top-K without reranking.** Embedding similarity is a proxy for relevance, not relevance itself. A reranker as the second stage significantly improves final context quality with minimal latency cost.

**Measuring faithfulness without measuring retrieval.** An LLM that faithfully echoes retrieved content still gives wrong answers if retrieval returned the wrong chunks. Faithfulness and retrieval quality are independent — you need to measure both.

**Choosing the Right Approach for Your Use Case**

| **Use Case** | **Chunking** | **Retrieval** | **Key Metric** |
| --- | --- | --- | --- |
| Enterprise document Q&A | Hierarchical | Hybrid + Rerank | Faithfulness |
| Customer support | Sentence-level | Dense + MMR | Answer Relevancy |
| Legal / Compliance | Proposition-based | Dense + BM25 | Context Precision |
| Research assistance | Semantic | HyDE + Multi-Query | Recall@K |
| Presentation / Slide AI | **Hierarchical (mandatory)** | Hybrid + Rerank | Answer Accuracy |
| Code documentation | Recursive (AST-aware) | Dense | Exact Match |

**What We’ve Learned**

RAG is not a component you add — it’s a pipeline you architect. The decisions you make at ingestion time (how you chunk, how you embed) determine the ceiling of what’s possible at retrieval and generation time. For organizations building [**enterprise-grade AI solutions**](https://47billion.com/machine-learning/), this means treating Retrieval-Augmented Generation as a full-stack system — from ingestion and retrieval to evaluation and monitoring.

The teams that build RAG that works in production are not the ones who picked the best vector database. They’re the ones who spent time understanding their documents, matched chunking strategy to document structure, measured retrieval quality independently, and iterated based on data.

The LLM at the end of the pipeline is only as good as what you give it. Give it the right context, and it will give you the right answer.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="sentgraph-hierarchical-sentence-graph-for-multi-hop-retrieva.md">
<details>
<summary>SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2601.03014v1>

# SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering

Junli Liang1,
Pengfei Zhou1,
Wangqiu Zhou2,
Wenjie Qing1,

Qi Zhao1,
Ziwen Wang1,
Qi Song1,
Xiangyang Li1,

1University of Science and Technology of China,
2Hefei University of Technology

{jlliang,pengfeizhou,qingwenjie,wangziwen}@mail.ustc.edu.cn;

rafazwq@hfut.edu.cn; zq2020email@163.com;{qisong09,xiangyangli}@ustc.edu.cnCorresponding authors

###### Abstract

Traditional Retrieval-Augmented Generation (RAG) effectively supports single-hop question answering with large language models but faces significant limitations in multi-hop question answering tasks, which require combining evidence from multiple documents.
Existing chunk-based retrieval often provides irrelevant and logically incoherent context, leading to incomplete evidence chains and incorrect reasoning during answer generation.
To address these challenges, we propose SentGraph, a sentence-level graph-based RAG framework that explicitly models fine-grained logical relationships between sentences for multi-hop question answering.
Specifically, we construct a hierarchical sentence graph offline by first adapting Rhetorical Structure Theory to distinguish nucleus and satellite sentences, and then organizing them into topic-level subgraphs with cross-document entity bridges.
During online retrieval, SentGraph performs graph-guided evidence selection and path expansion to retrieve fine-grained sentence-level evidence.
Extensive experiments on four multi-hop question answering benchmarks demonstrate the effectiveness of SentGraph, validating the importance of explicitly modeling sentence-level logical dependencies for multi-hop reasoning.

Junli Liang1,
Pengfei Zhou1,
Wangqiu Zhou2,
Wenjie Qing1,Qi Zhao1,
Ziwen Wang1,
Qi Song1††thanks: Corresponding authors,
Xiangyang Li1,1University of Science and Technology of China,
2Hefei University of Technology{jlliang,pengfeizhou,qingwenjie,wangziwen}@mail.ustc.edu.cn;rafazwq@hfut.edu.cn; zq2020email@163.com;{qisong09,xiangyangli}@ustc.edu.cn

## 1 Introduction

Large Language Models (LLMs) have demonstrated strong capabilities in semantic understanding and text generation, showing broad potential in document reading comprehension tasks (application1; llms\_development; application2).
However, LLMs remain constrained by their internal knowledge boundaries and are prone to hallucination (Hallucination2; Hallucination1), particularly in scenarios requiring strict factual accuracy.

To address these issues, Retrieval-Augmented Generation (RAG) incorporates external knowledge to support LLM generation (rag0; rag1).
Traditional RAG methods typically adopt a “chunk-index-retrieval” paradigm, retrieving fixed-length text chunks based on semantic similarity (rag00; rag2).
While effective for single-hop question answering (QA), such methods struggle with multi-hop question answering, which requires aggregating evidence across multiple documents, often failing to capture complete evidence chains and leading to incorrect or incomplete answers (HotpotQA; 2wiki; rag\_single).

https://arxiv.org/html/2601.03014v1/x1.pngFigure 1: Comparison of the traditional chunk-level and our adopted sentence-level graph construction methods.

To effectively tackle multi-hop question answering tasks, researchers have explored several solutions.
Post-retrieval optimization methods aim to refine the retrieval results to improve their quality (refiner; RECOMP). However, this approach heavily depends on the accuracy of the initial retrieval and often ignores the relationships between evidence across different documents, making it difficult to recover missing key evidence (Shifting). To address the limited recall of single-step retrieval, iterative retrieval methods have been proposed to gradually construct an evidence chain through multiple rounds of retrieval (ircot; RAPTOR). While iterative retrieval can expand the coverage of retrieved evidence, the repeated process introduces significant computational overhead and latency (KiRAG), limiting its applicability in real-time scenarios.

In recent years, some prominent approaches have begun to explicitly model cross-document relationships by constructing graph-based knowledge structures offline, thereby reducing online inference latency (KGP; graphRAG; lightrag). By organizing textual information into structured graphs, these methods facilitate multi-hop evidence capture during retrieval. Nevertheless, as shown in Figure [1](https://arxiv.org/html/2601.03014v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering")(a), existing graph-based methods often rely on similarity-based connections at the chunk level, making it difficult to capture fine-grained semantic and logical relationships between core sentences. Moreover, during online retrieval, the returned chunks frequently contain many sentences irrelevant to the query. Such redundant information not only consumes context space but also interferes with the reasoning process of LLMs, increasing the risk of hallucination (irrelevant2). Furthermore, weakly relevant yet crucial evidence sentences may be overlooked because they are not directly similar to the query, which can ultimately lead to incorrect answers.

Inspired by these prior efforts and to overcome their shortcomings, our basic idea is to propose a sentence graph-based retrieval-enhanced generation method. Specifically, we attempt to reduce the retrieval granularity from chunks to individual sentences and to explicitly model the semantic and logical relationships between sentences using a graph structure. However, constructing sentence-level graphs faces three technical challenges:
_(1) Context loss_: Sentences containing anaphoric expressions such as pronouns and deictic terms lose their specific referents when isolated from chunk context, which can lead to ambiguity in understanding what entities or concepts they refer to. _(2) Relationship modeling complexity_: Different from chunk-level connections that can rely on surface-level similarity, sentence-level relationships are far more diverse and complex, encompassing various logical types such as causality, condition, and contrast. This diversity poses challenges in both determining which relationship types to represent and accurately identifying them between sentences. _(3) High computational overhead_: The number of sentences in documents is significantly larger than the number of text chunks, making global sentence graph construction computationally expensive and potentially impractical for large-scale applications.

To overcome these challenges, we propose an offline hierarchical sentence graph construction framework, as shown in Figure [1](https://arxiv.org/html/2601.03014v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering")(b).
To address context loss and relationship modeling complexity, we employ a refined set of logical relationships based on Rhetorical Structure Theory (RST) (rst).
Specifically, we adapt RST by consolidating frequently occurring relations and removing rare ones, resulting in a practical relationship taxonomy that naturally distinguishes between nucleus sentences and satellite sentences.
To tackle high computational overhead, we design a three-layer graph structure with topic, core sentence, and supplementary sentence layers.
Instead of building a dense global sentence graph, we first construct topic-level subgraphs within individual documents, then establish cross-document connections through entity-concept bridges at the topic layer.
In the online retrieval stage, we introduce a sentence graph-based retrieval-enhanced generation strategy that enables fine-grained evidence selection, thereby reducing irrelevant context and token consumption during LLM generation.

We summarize our contributions as follows:

- •

We are the first to apply Rhetorical Structure Theory to sentence-level graph construction for retrieval-augmented generation, providing a principled approach to model fine-grained logical relationships between sentences.

- •

We propose an offline hierarchical sentence graph construction method with dual logical relationship modeling, along with an online sentence-level retrieval strategy that leverages the graph structure to retrieve key evidence sentences with their logical context for multi-hop question answering tasks.

- •

Extensive experiments on multi-hop question answering benchmarks demonstrate the superior performance of our approach and validate the effectiveness of our framework.

## 2 Related Work

### 2.1 Retrieval-Augmented Generation

Retrieval-Augmented Generation has shown strong performance in question answering tasks (rag0; rag00).
However, although standard RAG models perform well on single-hop questions, they face clear challenges on multi-hop QA tasks (HotpotQA).

To improve retrieval quality, several extensions have been proposed.
Refiner (refiner) extracts query-relevant content and reorganizes it in a structured form, which helps LLMs better align with the original context.
(Shifting) shifts retrieval from ranking individual passages to optimizing the overall quality of a passage set.
However, the performance of these methods still depends heavily on the quality of the initial retrieval results.

To overcome the limited coverage of single-round retrieval,
(ircot) alternates between chain-of-thought reasoning and knowledge retrieval.
The reasoning process guides retrieval, while retrieved evidence is used to refine reasoning.
This design targets knowledge-intensive multi-hop question answering.
KiRAG (KiRAG) further introduces iterative retrieval based on knowledge triples.
It explicitly integrates reasoning into the retrieval process to adapt to changing information needs.
While these approaches improve evidence coverage, multi-round retrieval introduces unavoidable computational overhead.

### 2.2 Graph-Based RAG Methods

Graph-based representations offer a promising alternative.
They encode document relations offline, reducing the reliance on repeated online retrieval.
KGP (KGP) constructs a knowledge graph over multiple documents and designs an LLM-based graph traversal agent.
This agent supports cross-document retrieval and question answering.
GraphRAG (graphRAG) introduces a graph-based approach that leverages LLMs to extract entities and relationships from documents, constructing a knowledge graph that captures semantic structure. Through community detection, it generates hierarchical summaries at multiple levels, enabling both local and global reasoning for complex queries.
LightRAG (lightrag) proposes a graph-enhanced retrieval framework. Instead of relying on community detection and hierarchical summarization, it adopts a dual-level retrieval strategy that enables both low-level and high-level knowledge discovery.

However, most existing graph-based methods operate at the chunk level.
They treat multi-sentence text chunks as graph nodes, which limits their ability to capture fine-grained semantic relations.
In addition, retrieved chunks often contain irrelevant sentences, introducing noise and increasing the risk of missing weakly related but critical evidence due to coarse chunk-level similarity.

## 3 The Proposed SentGraph Method

https://arxiv.org/html/2601.03014v1/x2.pngFigure 2: An overview of the SentGraph framework. The offline stage constructs a hierarchical sentence logic graph, and the online stage performs graph-based retrieval and answer generation for multi-hop question answering.

SentGraph is a sentence-level logic graph construction and retrieval-augmented generation framework for multi-hop question answering.
It departs from the traditional chunk-based retrieval and modeling paradigm by explicitly capturing sentence-level logical dependencies within and across documents. This design enables finer-grained knowledge organization and reasoning path modeling.
As shown in Figure [2](https://arxiv.org/html/2601.03014v1#S3.F2 "Figure 2 ‣ 3 The Proposed SentGraph Method ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering"), the framework consists of two stages: offline sentence logic graph construction and online graph-based retrieval and answer generation. In the offline stage, we construct a hierarchical sentence logic graph by modeling sentence-level logical structures. In the online stage, we perform evidence retrieval and answer generation based on the graph, thereby improving LLMs’ effectiveness for cross-document reasoning on complex questions.

### 3.1 Offline Stage: Hierarchical Sentence Logic Graph Construction

Given a document collection, denoted as D={d1,d2,…,dn}D=\\{d\_{1},d\_{2},\\dots,d\_{n}\\}, we first decompose each document into sentence-level semantic units. Compared to traditional chunk-level modeling, sentence-level units provide finer-grained evidence granularity, but also introduce several challenges, including context loss, complex relation modeling, and high computational overhead when directly constructing a global sentence graph. To address these challenges, we propose a hierarchical graph construction method based on refined Rhetorical Structure Theory (RST). This method alleviates context loss and relation complexity through RST-based logical relation modeling, while reducing computational overhead through hierarchical architecture design.

Considering that RST defines many relation types, some of which have limited discriminative power for reasoning and QA, we simplify the relation set from the perspective of reasoning function and evidence organization, retaining only relation types that substantially impact cross-document reasoning. Specifically, based on the functional roles of sentences in discourse, we define two categories of relations: _Nucleus-Nucleus (N-N) relations_ model logical connections between sentences of equal importance that jointly convey core document semantics, including conjunction, contrast, disjunction, multinuclear restatement, and sequence relations, whereas _Nucleus-Satellite (N-S) relations_ model asymmetric dependencies between core sentences and their supporting sentences, including cause, result, opposition, elaboration, circumstance, evaluation, and solutionhood relations.

Based on the above relation modeling, we design a three-layer graph structure that balances expressive power and computational complexity through hierarchical organization, avoiding the computational overhead of directly constructing a global sentence graph. The graph is formally defined as:

| | | |
| --- | --- | --- |
| | G=(V,E)G=(V,E) | |

where the node set is:

| | | |
| --- | --- | --- |
| | V=Vt∪Vc∪VsV=V\_{t}\\cup V\_{c}\\cup V\_{s} | |

Here, topic nodes VtV\_{t} represent document-level semantic summaries for cross-document bridging, core sentence nodes VcV\_{c} correspond to sentences carrying key facts and reasoning support, and supplementary sentence nodes VsV\_{s} represent subordinate sentences that elaborate on or conditionally supplement core sentences.

The edge set is formally defined as:

| | | |
| --- | --- | --- |
| | E=Et​t∪Et​c∪Ec​c∪Ec​sE=E\_{tt}\\cup E\_{tc}\\cup E\_{cc}\\cup E\_{cs} | |

Here, inter-topic bridging edges Et​tE\_{tt} establish cross-document semantic connections, topic-to-core edges Et​cE\_{tc} associate topics with their subordinate core sentences, core-to-core edges Ec​cE\_{cc} represent N-N relations such as parallel, contrast, and sequence, and core-to-supplementary edges Ec​sE\_{cs} represent N-S dependencies such as cause, background, and evaluation.

The construction process consists of two steps: intra-document logic modeling and cross-document semantic bridging.

In the intra-document logic modeling stage, we first employ LLMs guided by refined RST to identify core sentences carrying main facts and determine N-N logical relations between them. We then cluster non-core sentences and assign them to corresponding core sentences based on semantic similarity and contextual distance, before using LLMs to establish N-S subordinate relations. This process captures the hierarchical logical structure within each document. Detailed prompt templates are provided in Appendix [A.1](https://arxiv.org/html/2601.03014v1#A1.SS1 "A.1 Prompt for N-N Relations Recognition ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering") and Appendix [A.2](https://arxiv.org/html/2601.03014v1#A1.SS2 "A.2 Prompt for N-S Relations Recognition ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

In the cross-document semantic bridging stage, we leverage the background knowledge of LLMs to identify commonsense relations between topic entities across different documents, and establish inter-topic bridging edges Et​tE\_{tt} between topic nodes. This enables the reasoning process to integrate key evidence across documents and form cross-document reasoning chains. The detailed prompt template is provided in Appendix [A.3](https://arxiv.org/html/2601.03014v1#A1.SS3 "A.3 Prompt for Cross-document Semantic Bridging ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

### 3.2 Online Stage: Graph-Based Retrieval and Answer Generation

Given a user query, the online process consists of three modules: anchor selection and refinement, adaptive path expansion, and answer generation.

Anchor selection and refinement.
We adopt a coarse-to-fine two-stage strategy. First, a retriever computes similarity scores between the query and all graph nodes, and the Top-KK highest-scoring nodes are selected as candidate anchors. These candidates are then refined by the LLM, which filters out loosely related nodes and evaluates whether the remaining anchors contain sufficient evidence. If the evidence is sufficient, the process proceeds directly to answer generation. Otherwise, the process triggers path expansion to retrieve additional evidence. The detailed prompt template used for anchor refinement is provided in Appendix [A.4](https://arxiv.org/html/2601.03014v1#A1.SS4 "A.4 Prompt for Anchor Refinement ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

Adaptive path expansion.
We explore reasoning paths starting from each anchor using a breadth-first strategy. For each anchor, we maintain a path queue and expand paths along graph edges by selecting neighboring nodes based on similarity. Newly selected nodes are appended to the current path until a predefined maximum path length or expansion limit is reached.

Answer generation.
We extract all sentence nodes from the retained paths to form the final evidence set. Then, we provide this evidence along with the query to the LLM, instructing it to generate a final answer based on the given context. The LLM performs multi-hop reasoning over the evidence and generates the final answer.

## 4 Experiment

### 4.1 Experiment Setting

Datasets.
We evaluate our approach on four complex multi-hop question answering datasets.
HotpotQA HotpotQA contains 113k question-answer pairs that require cross-document reasoning and provide sentence-level supporting facts.
2WikiMultiHopQA (2Wiki) 2wiki is a multi-hop question answering dataset constructed from Wikipedia, requiring reasoning across multiple documents.
MuSiQue MuSiQue contains approximately 25k questions and enforces multi-step reasoning with 2–4 hops to avoid shortcut solutions.
MultiHopRAG(MultiHop) multihop is a benchmark designed for RAG systems and includes 2,556 questions whose answers must be synthesized from 2–4 news articles.

Source Models.
We evaluate our method using two retrieval models and multiple LLMs.
For retrieval, we use BM25 bm25, a traditional unsupervised method, and bge-large-en-v1.5(BGE) bge, a supervised dense retriever.
For generation, we use Llama-3.1-8B-Instruct llama3.1 as the primary LLM.
To evaluate generalization across model scales, we additionally test Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, and Qwen2.5-32B-Instruct qwen2; qwen2.5.

| Retrieval | Model | RetrievalUnits | Avg\# Units | HotpotQA | 2Wiki | MuSiQue | MultiHop |
| EM | F1 | EM | F1 | EM | F1 | Accuracy |
| BM25 | Retrieval Only | Passage | 3.00 | 9.20 | 15.20 | 3.40 | 9.65 | 1.40 | 4.27 | 37.20 |
| Retrieval Only | Sentence | 3.00 | 31.20 | 42.44 | 23.60 | 29.29 | 9.60 | 16.86 | 61.60 |
| RankLlama | Passage | 5.00 | 29.48 | 27.82 | 30.30 | 21.91 | 6.04 | 9.26 | 42.09 |
| SetR-CoT & IRI | Passage | 2.63 | 32.20 | 30.57 | \\ul32.17 | 24.22 | 6.62 | 10.57 | 44.13 |
| KiRAG | Passage | 3.00 | 17.40 | 23.40 | 24.00 | \\ul32.70 | 9.00 | 18.20 | 26.50 |
| KGP | Passage | 3.00 | \\ul36.82 | \\ul49.94 | 22.80 | 31.21 | 9.31 | 18.66 | \\ul62.00 |
| LightRAG | Passage | 3.00 | 28.66 | 39.06 | 17.78 | 27.43 | \\ul9.83 | \\ul18.71 | 26.65 |
| SentGraph(Ours) | Sentence | 2.57 | 43.80 | 57.13 | 32.20 | 39.48 | 16.00 | 26.83 | 63.40 |
| BGE | Retrieval Only | Passage | 3.00 | 11.00 | 18.09 | 3.80 | 10.34 | 2.40 | 6.86 | 44.40 |
| Retrieval Only | Sentence | 3.00 | 38.60 | 50.88 | 30.80 | 40.01 | 17.00 | 28.57 | 60.20 |
| RankLlama | Passage | 5.00 | 31.88 | 32.95 | 32.24 | 25.78 | 7.61 | 11.77 | 43.51 |
| SetR-CoT & IRI | Passage | 2.91 | 36.62 | 38.11 | 35.44 | 30.35 | 10.79 | 15.43 | 47.14 |
| KiRAG | Passage | 3.00 | 18.20 | 24.50 | 26.40 | 35.00 | 6.20 | 17.00 | 22.50 |
| KGP | Passage | 3.00 | \\ul44.00 | \\ul58.73 | \\ul36.80 | \\ul48.20 | \\ul21.20 | \\ul34.72 | \\ul63.40 |
| LightRAG | Passage | 3.00 | 27.17 | 37.75 | 17.40 | 26.99 | 8.60 | 17.71 | 20.44 |
| SentGraph(Ours) | Sentence | 2.70 | 48.80 | 62.92 | 42.00 | 52.26 | 26.80 | 40.36 | 65.60 |

Table 1: Performance (%) comparison on four multi-hop question answering datasets (passage-level as chunk-level instantiation). Bold and underlined indicate the best and second best performance, respectively.

Baselines.
(1) Retrieval Only(RO) serves as a basic baseline and follows the standard in-context RAG paradigm ragcontext.
We evaluate both passage-level and sentence-level retrieval units, where the sentence-level baseline uses simple document sentence splitting.
(2) RankLlamaRankLlama and SetR-CoT & IRIShifting are post-retrieval optimization methods.
(3) KiRAGKiRAG represents iterative retrieval strategies.
(4) LightRAGlightrag and KGPKGP are graph-enhanced RAG methods that incorporate explicit graph structures for multi-hop QA.

For fair comparison, we restrict all baseline methods to a single retrieval step, focusing the comparison on retrieval granularity and structural modeling.
Additionally, in terms of retrieval granularity, all baseline methods follow prior work and operate on passage-level retrieval units, unless otherwise specified.
In our experimental setting, passage-level retrieval constitutes a concrete instantiation of chunk-level retrieval.
In contrast, our method operates on sentence-level retrieval units.

Metrics.
Following common practice in prior RAG evaluations, we uniformly sample 500 questions from each dataset for all methods and use the same evaluation subsets to ensure fair comparison.
We use Exact Match(EM %) and F1 score( %) as the primary evaluation metrics.
For the MultiHopRAG dataset, we report Accuracy, following its previous evaluation protocol.
All experiments are conducted on a Linux server equipped with four NVIDIA A800 80GB GPUs, dual Intel Xeon CPUs (2.9 GHz), and 512 GB of memory.
All models are evaluated with deterministic decoding, with the temperature set to 0.

### 4.2 Main Results

We compare SentGraph with baselines on four multi-hop question answering datasets under both sparse (BM25) and dense (BGE) retrieval settings in Table [1](https://arxiv.org/html/2601.03014v1#S4.T1 "Table 1 ‣ 4.1 Experiment Setting ‣ 4 Experiment ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering"). SentGraph consistently achieves the best performance across all datasets and retrieval settings. It is important to note that SentGraph operates on sentence-level retrieval units while most baselines use passage-level units, demonstrating that fine-grained evidence modeling with structured logical dependencies is more effective than coarse-grained retrieval for multi-hop QA. Next, we summarize key observations as follows:

Fine-grained retrieval is necessary but insufficient. Sentence-level retrieval significantly outperforms passage-level retrieval in the retrieval-only setting. For instance, under BM25, sentence-level units achieve 31.20 EM on HotpotQA compared to only 9.20 EM for passage-level units, confirming the importance of fine-grained retrieval for multi-hop reasoning. However, sentence-level retrieval alone still substantially underperforms SentGraph, with gaps of 12.6 EM points on HotpotQA and 10.2 points on 2Wiki under BM25. This indicates that modeling logical dependencies between sentences is critical beyond granularity alone.

| | | | | HotpotQA | 2Wiki | MuSiQue | MultiHop |
| Retrieval | Model | RetrievalUnit | Avg\# Units | EM | F1 | EM | F1 | EM | F1 | Accuracy |
| \\cellcolor\[HTML\]EFEFEFBase LLM: Qwen2.5-7B-Instruct |
| | RO | Passage | 3.00 | 14.20 | 19.24 | 16.00 | 18.00 | 2.20 | 4.42 | 35.20 |
| | KGP | Passage | 3.00 | \\ul43.66 | \\ul56.14 | \\ul32.00 | \\ul38.14 | \\ul13.60 | \\ul22.13 | \\ul67.40 |
| | RO | Sentence | 3.00 | 37.60 | 49.18 | 26.80 | 32.02 | 11.60 | 19.97 | 67.00 |
| BM25 | SentGraph | Sentence | 2.89 | 48.80 | 61.98 | 44.40 | 52.53 | 25.00 | 35.09 | 68.80 |
| | RO | Passage | 3.00 | 13.60 | 18.26 | 10.00 | 10.94 | 3.20 | 4.60 | 39.40 |
| | KGP | Passage | 3.00 | \\ul53.66 | \\ul67.25 | \\ul49.20 | \\ul57.31 | \\ul28.40 | \\ul42.48 | \\ul69.00 |
| | RO | Sentence | 3.00 | 43.80 | 56.52 | 40.80 | 49.71 | 22.40 | 34.53 | 66.00 |
| BGE | SentGraph | Sentence | 2.44 | 55.60 | 68.88 | 52.60 | 61.49 | 36.00 | 48.27 | 70.20 |
| \\cellcolor\[HTML\]EFEFEFBase LLM: Llama-3.1-8B-Instruct |
| | RO | Passage | 3.00 | 9.20 | 15.20 | 3.40 | 9.65 | 1.40 | 4.27 | 37.20 |
| | KGP | Passage | 3.00 | \\ul36.82 | \\ul49.94 | 22.80 | \\ul31.21 | 9.31 | \\ul18.66 | \\ul62.00 |
| | RO | Sentence | 3.00 | 31.20 | 42.44 | \\ul23.60 | 29.29 | \\ul9.60 | 16.86 | 61.60 |
| BM25 | SentGraph | Sentence | 2.57 | 43.80 | 57.13 | 32.20 | 39.48 | 16.00 | 26.83 | 63.40 |
| | RO | Passage | 3.00 | 11.00 | 18.09 | 3.80 | 10.34 | 2.40 | 6.86 | 44.40 |
| | KGP | Passage | 3.00 | \\ul44.00 | \\ul58.73 | \\ul36.80 | \\ul48.20 | \\ul21.20 | \\ul34.72 | \\ul63.40 |
| | RO | Sentence | 3.00 | 38.60 | 50.88 | 30.80 | 40.01 | 17.00 | 28.57 | 60.20 |
| BGE | SentGraph | Sentence | 2.70 | 48.80 | 62.92 | 42.00 | 52.26 | 26.80 | 40.36 | 65.60 |
| \\cellcolor\[HTML\]EFEFEFBase LLM: Qwen2.5-14B-Instruct |
| | RO | Passage | 3.00 | 14.00 | 18.91 | 16.20 | 18.26 | 2.20 | 2.42 | 35.60 |
| | KGP | Passage | 3.00 | \\ul43.66 | \\ul56.06 | \\ul32.20 | \\ul38.37 | 11.60 | 19.89 | 67.20 |
| | RO | Sentence | 3.00 | 37.20 | 48.94 | 27.00 | 32.08 | \\ul13.20 | \\ul22.10 | \\ul66.80 |
| BM25 | SentGraph | Sentence | 2.89 | 49.00 | 62.36 | 43.80 | 51.84 | 24.00 | 33.93 | 69.20 |
| | RO | Passage | 3.00 | 13.60 | 18.25 | 10.00 | 10.88 | 3.00 | 4.51 | 39.20 |
| | KGP | Passage | 3.00 | \\ul53.66 | \\ul67.06 | \\ul48.20 | \\ul56.60 | \\ul28.40 | \\ul42.37 | \\ul69.00 |
| | RO | Sentence | 3.00 | 43.00 | 56.14 | 40.80 | 49.60 | 22.60 | 34.90 | 66.20 |
| BGE | SentGraph | Sentence | 2.61 | 55.40 | 68.74 | 54.20 | 63.05 | 36.80 | 49.30 | 70.00 |
| \\cellcolor\[HTML\]EFEFEFBase LLM: Qwen2.5-32B-Instruct |
| | RO | Passage | 3.00 | 20.80 | 27.78 | 24.00 | 26.88 | 3.40 | 7.75 | 44.80 |
| | KGP | Passage | 3.00 | \\ul46.08 | \\ul58.29 | \\ul34.40 | \\ul40.20 | \\ul14.60 | \\ul25.25 | 66.40 |
| | RO | Sentence | 3.00 | 40.60 | 51.70 | 31.80 | 37.22 | 12.40 | 21.27 | \\ul67.20 |
| BM25 | SentGraph | Sentence | 2.54 | 51.40 | 64.03 | 45.80 | 53.69 | 25.20 | 36.78 | 72.40 |
| | RO | Passage | 3.00 | 21.00 | 28.52 | 23.40 | 26.24 | 5.00 | 9.16 | 51.20 |
| | KGP | Passage | 3.00 | \\ul55.28 | \\ul68.89 | \\ul51.80 | \\ul60.53 | \\ul28.20 | \\ul41.41 | 67.80 |
| | RO | Sentence | 3.00 | 43.20 | 57.01 | 45.00 | 52.76 | 25.00 | 36.89 | \\ul68.80 |
| BGE | SentGraph | Sentence | 2.62 | 57.60 | 70.64 | 55.40 | 64.73 | 38.80 | 52.01 | 73.00 |

Table 2: Performance (%) comparison across four multi-hop question answering datasets at different LLM scales (passage-level as chunk-level instantiation). “RO” denotes retrieval-only. Bold and underlined values indicate the best and second-best results, respectively.

Post-retrieval and iterative methods show limited gains. RankLlama and SetR-CoT & IRI improve over retrieval-only baselines through result refinement, but their effectiveness remains constrained by initial retrieval quality. KiRAG attempts to discover missing evidence through iterative retrieval, but achieves limited improvements when the number of iterations is restricted, obtaining only 17.40 and 18.20 EM on HotpotQA under BM25 and BGE respectively.

Graph-enhanced methods benefit from structure but lack fine-grained modeling. LightRAG and KGP outperform retrieval-only baselines by introducing explicit structural connections. Among all baselines, KGP achieves the strongest performance, reaching 44.00 EM on HotpotQA and 36.80 EM on 2WikiMultiHopQA under BGE retrieval. However, these methods typically construct graphs at the passage level, which limits their ability to capture fine-grained logical relations between sentences.
In contrast, SentGraph models sentence-level logical dependencies and achieves superior performance. Under BGE setting, SentGraph outperforms KGP by 4.8 EM points on HotpotQA, 5.2 points on 2WikiMultiHopQA, and 5.6 points on MuSiQue. This demonstrates that SentGraph’s gains arise from fine-grained evidence selection and structured reasoning paths rather than increased context length.

### 4.3 Results across Different Base LLMs

Table [2](https://arxiv.org/html/2601.03014v1#S4.T2 "Table 2 ‣ 4.2 Main Results ‣ 4 Experiment ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering") presents the performance of SentGraph across multiple base LLMs with different model sizes, ranging from 7B to 32B parameters. We evaluate methods under two key dimensions: retrieval granularity (passage-level vs. sentence-level) and structural modeling (retrieval-only vs. graph-based). SentGraph consistently outperforms all baselines across different model scales, demonstrating the necessity of modeling logical dependencies at the sentence level for multi-hop QA.

Specifically, across all LLMs, sentence-level retrieval-only consistently outperforms passage-level retrieval-only by substantial margins. For example, with Qwen2.5-32B under BGE retrieval, sentence-level retrieval achieves 43.20 EM on HotpotQA and 45.00 EM on 2WikiMultiHopQA, compared to only 21.00 and 23.40 EM for passage-level retrieval.
This once again confirms that fine-grained evidence units are critical for capturing precise multi-hop reasoning paths. Moreover, we observe that more powerful LLMs generally improve the performance of all methods. However, the improvement achieved by retrieval-only is limited. This further indicates that granularity alone is insufficient and that proper evidence organization remains crucial even with more capable LLMs.

The graph-based method KGP improves over passage-level retrieval-only across all LLM scales. With Qwen2.5-32B under BGE retrieval, KGP reaches 55.28 EM on HotpotQA and 51.80 EM on 2WikiMultiHopQA, representing gains of 34.28 and 28.40 EM points over passage-level retrieval-only. This confirms the benefit of explicit structural modeling for multi-hop reasoning. However, coarse-grained passage units inherently mix relevant and irrelevant sentences, limiting the effectiveness of graph-based reasoning. In contrast, SentGraph constructs a hierarchical sentence-level graph that explicitly models logical dependencies between sentences, enabling fine-grained evidence selection and structured reasoning paths. With the same LLM, SentGraph achieves 57.60 EM on HotpotQA, 55.40 EM on 2WikiMultiHopQA, and 38.80 EM on MuSiQue, outperforming sentence-level retrieval-only by 14.4, 10.4, and 13.8 EM points, and surpassing KGP by 2.32, 3.6, and 10.6 EM points respectively.
Notably, these improvements remain consistent across different LLM scales, demonstrating robust and scalable gains.

| Components | HotpotQA | 2Wiki | MuSiQue |
| --- | --- | --- | --- |
| AS | AER | GPE | EM | F1 | EM | F1 | EM | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✓\\checkmark | ×\\times | ×\\times | 37.60 | 50.62 | 28.00 | 35.52 | 16.00 | 27.67 |
| ✓\\checkmark | ✓\\checkmark | ×\\times | 44.80 | 59.37 | 37.40 | 46.96 | 25.40 | 37.57 |
| ✓\\checkmark | ✓\\checkmark | ✓\\checkmark | 48.80 | 62.92 | 42.00 | 52.26 | 26.80 | 40.36 |

Table 3: Ablation study on core components.

### 4.4 Ablation Study

Table [3](https://arxiv.org/html/2601.03014v1#S4.T3 "Table 3 ‣ 4.3 Results across Different Base LLMs ‣ 4 Experiment ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering") reports the ablation results of SentGraph by progressively enabling its core components.
AS denotes anchor selection, AER denotes adaptive evidence refinement, and GPE denotes guided path expansion.
AS alone provides baseline performance by identifying locally relevant sentences, but remains insufficient for complex multi-hop reasoning.
Introducing AER leads to substantial improvements, with EM gains of 7.2 points on HotpotQA, 9.4 points on 2WikiMultiHopQA, and 9.4 points on MuSiQue, highlighting the importance of filtering irrelevant anchors and assessing evidence sufficiency. Further adding GPE yields additional gains of 4.0, 4.6, and 1.4 EM points, respectively.
These results demonstrate that SentGraph benefits from the complementary roles of its components, where anchor selection provides initial candidates, evidence refinement filters noise and assesses sufficiency, and path expansion broadens evidence coverage to support multi-hop reasoning.

Figure [3](https://arxiv.org/html/2601.03014v1#S4.F3 "Figure 3 ‣ 4.4 Ablation Study ‣ 4 Experiment ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering") presents the impact of the number of anchors on SentGraph performance. As the number of anchors increases from 5 to 25, performance consistently improves, with gains of 6.2 EM points on HotpotQA, 8.8 points on 2WikiMultiHopQA, and 8.4 points on MuSiQue. Beyond 20 anchors, the performance improvement becomes smaller.
This indicates that an adequate pool of candidate anchors is crucial for capturing diverse reasoning paths in multi-hop questions, but excessively large anchor sets yield diminishing returns.

HotpotQA2WikiMultiHopQAMuSiQue

5510101515202025253030151520202525303035354040454550505555Anchor NumberEM (%)
(a) EM scores across different anchor numbers.

5510101515202025253030303035354040454550505555606065657070Anchor NumberF1 (%)
(b) F1 scores across different anchor numbers.

Figure 3: Performance across multi-hop question answering datasets with varying anchor numbers.

### 4.5 Performance and Efficiency Analysis

Figure [4](https://arxiv.org/html/2601.03014v1#S4.F4 "Figure 4 ‣ 4.5 Performance and Efficiency Analysis ‣ 4 Experiment ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering") compares the token usage of SentGraph and KGP. SentGraph achieves consistent reductions in both input and output token consumption while maintaining superior performance.
For input tokens, SentGraph reduces context length by 29.99% on HotpotQA, 45.26% on 2WikiMultiHopQA, and 30.38% on MuSiQue compared to KGP.
These reductions stem from sentence-level retrieval granularity, which enables more fine-grained evidence selection and helps reduce irrelevant context that is often included in passage-level retrieval.
Output token savings are even more pronounced, with reductions of 69.00% on HotpotQA, 18.56% on 2WikiMultiHopQA, and 9.22% on MuSiQue. This indicates that cleaner input evidence leads to more concise and focused generation.
Combined with the performance improvements shown in Table [1](https://arxiv.org/html/2601.03014v1#S4.T1 "Table 1 ‣ 4.1 Experiment Setting ‣ 4 Experiment ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering"), these results demonstrate that SentGraph achieves better accuracy with lower computational cost.

KGPSentGraph

HotpotQA2WikiMuSiQue0100100200200300300400400Input Tokens
(a) Average input token usage per query.

HotpotQA2WikiMuSiQue0101020203030Output Tokens
(b) Average output token usage per query.

Figure 4: Efficiency analysis on average token usage per query across multi-hop question answering datasets.

## 5 Conclusion

We propose SentGraph, a sentence-level graph-based RAG framework for multi-hop QA that constructs hierarchical sentence graphs with explicit logical dependencies by adapting RST. SentGraph further employs a graph-guided retrieval strategy to enable fine-grained evidence selection at the sentence level. Extensive experiments show that SentGraph achieves consistent performance improvements with lower token consumption, highlighting the importance of fine-grained logical dependency modeling for effective multi-hop QA.

## Limitations

Despite its effectiveness, SentGraph has several limitations.
First, the construction of the hierarchical sentence graph relies on LLMs to identify N-N and N-S relations, as well as cross-document semantic bridges.
While LLMs provide strong generalization capabilities, their predictions may introduce noise, which could affect the quality of the constructed graph.
We also observe that the quality of relation annotation is sensitive to the capacity of the underlying LLMs, with larger models tending to produce more reliable structures.
However, we do not explicitly quantify the impact of annotation errors on downstream reasoning performance.
Future work could investigate more robust graph construction strategies or human-in-the-loop validation mechanisms.

Second, our adaptation of Rhetorical Structure Theory focuses on a refined set of relation types tailored specifically to multi-hop question answering.
While effective for this task, it may not fully capture all discourse phenomena, and its applicability to other downstream tasks remains to be explored.

Finally, SentGraph emphasizes online inference efficiency by shifting most computation to an offline stage.
However, the offline graph construction process introduces additional computational costs, especially when applied to large-scale corpora.
Future work could explore more efficient or incremental graph construction strategies.

## Ethics Statement

This work focuses on improving multi-hop retrieval and reasoning through structured sentence-level representations. The proposed method is evaluated on publicly available benchmark datasets and does not involve the collection or use of personal, sensitive, or proprietary data. SentGraph does not train or modify LLMs. It operates as a retrieval framework that provides structured context to existing LLMs for answer generation. Like other RAG frameworks, ethical considerations depend on downstream application contexts and require appropriate safeguards during deployment.

## Appendix A Prompt

### A.1 Prompt for N-N Relations Recognition

In the intra-document logic modeling stage, we first identify core sentences and their N–N (Nucleus–Nucleus) logical relations. To accomplish this, we design a prompt that instructs the LLM to recognize five types of N–N relations between sentences. The detailed prompt template is shown in Figure [5](https://arxiv.org/html/2601.03014v1#A1.F5 "Figure 5 ‣ A.1 Prompt for N-N Relations Recognition ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

https://arxiv.org/html/2601.03014v1/x3.pngFigure 5: Prompt Template for N-N Relations Recognition.

### A.2 Prompt for N-S Relations Recognition

After identifying core sentences, we cluster non-core sentences and establish N-S (Nucleus-Satellite) relations between them. We design a prompt that instructs the LLM to recognize seven types of N-S relations. The detailed prompt template is shown in Figure [6](https://arxiv.org/html/2601.03014v1#A1.F6 "Figure 6 ‣ A.2 Prompt for N-S Relations Recognition ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

https://arxiv.org/html/2601.03014v1/x4.pngFigure 6: Prompt Template for N-S Relations Recognition.

### A.3 Prompt for Cross-document Semantic Bridging

To connect information across different documents, we identify semantic relations between topic entities. We design a prompt that instructs the LLM to extract entity relationships based on its background knowledge. The detailed prompt template is shown in Figure [7](https://arxiv.org/html/2601.03014v1#A1.F7 "Figure 7 ‣ A.3 Prompt for Cross-document Semantic Bridging ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

https://arxiv.org/html/2601.03014v1/x5.pngFigure 7: Prompt Template for Cross-document Semantic Bridging.

### A.4 Prompt for Anchor Refinement

In the online reasoning stage, we refine the initially retrieved anchor nodes. We design a prompt that instructs the LLM to evaluate which evidence paths are most relevant for answering the given query. The detailed prompt template is shown in Figure [8](https://arxiv.org/html/2601.03014v1#A1.F8 "Figure 8 ‣ A.4 Prompt for Anchor Refinement ‣ Appendix A Prompt ‣ SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering").

https://arxiv.org/html/2601.03014v1/x6.pngFigure 8: Prompt Template for Anchor Refinement.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="sok-agentic-retrieval-augmented-generation-rag-taxonomy-arch.md">
<details>
<summary>SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2603.07379v1>

Title:

Content selection saved. Describe the issue below:

Description:

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.07379v1 \[cs.AI\] 07 Mar 2026

# SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions

Saroj Mishra1,
Suman Niroula2,
Umesh Yadav3,
Dilip Thakur4,
Srijan Gyawali5, and
Shiva Gaire5

###### Abstract

Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies. Despite rapid industrial adoption, current research lacks a systematic understanding of Agentic RAG as a sequential decision-making system, leading to highly fragmented architectures, inconsistent evaluation methodologies, and unresolved reliability risks. This Systematization of Knowledge (SoK) paper provides the first unified framework for understanding these autonomous systems. We formalize agentic retrieval-generation loops as finite-horizon partially observable Markov decision processes, explicitly modeling their control policies and state transitions. Building upon this formalization, we develop a comprehensive taxonomy and modular architectural decomposition that categorizes systems by their planning mechanisms, retrieval orchestration, memory paradigms, and tool-invocation behaviors. We further analyze the critical limitations of traditional static evaluation practices and identify severe systemic risks inherent to autonomous loops, including compounding hallucination propagation, memory poisoning, retrieval misalignment, and cascading tool-execution vulnerabilities. Finally, we outline key doctoral-scale research directions spanning stable adaptive retrieval, cost-aware orchestration, formal trajectory evaluation, and oversight mechanisms, providing a definitive roadmap for building reliable, controllable, and scalable agentic retrieval systems.

## I Introduction

Retrieval-Augmented Generation (RAG) fundamentally couples a parametric generator with a non-parametric corpus to condition outputs on retrieved evidence \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks")\]. However, the standard formulation relies on a static control flow: a retriever fetches a fixed set of passages, and the generator synthesizes an answer without adaptive multi-step decisions \[ [44](https://arxiv.org/html/2603.07379v1#bib.bib2 "Dense passage retrieval for open-domain question answering")\]. This deterministic pipeline exhibits severe brittleness in knowledge-intensive and multi-hop tasks \[ [106](https://arxiv.org/html/2603.07379v1#bib.bib30 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")\]. Because retrieval occurs blindly before reasoning begins, static systems suffer from context overloading \[ [55](https://arxiv.org/html/2603.07379v1#bib.bib4 "Lost in the middle: how language models use long contexts")\], lack native correction loops for noisy retrievals \[ [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\], and indiscriminately retrieve regardless of input necessity, which can actively diminish response quality \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\].

To mitigate these limitations, early heuristic approaches introduced active and iterative retrieval paradigms \[ [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\]. Frameworks like unified active-retrieval (UAR) treat the retrieval trigger as a dynamic decision \[ [13](https://arxiv.org/html/2603.07379v1#bib.bib12 "Unified active retrieval for retrieval augmented generation")\], while generation-in-the-loop architectures interleave intermediate reasoning to refine subsequent queries \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\]. Concurrently, the emergence of tool-augmented large language models (LLMs) established the foundation for fully autonomous control \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools"), [43](https://arxiv.org/html/2603.07379v1#bib.bib7 "MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning")\]. Models such as ReAct (Reasoning and Acting) demonstrated that LLMs can act as reasoning agents emitting interleaved thoughts and actions \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\]. Furthermore, paradigms incorporating episodic memory \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\], tree-based exploration \[ [8](https://arxiv.org/html/2603.07379v1#bib.bib23 "Attributed question answering: evaluation and modeling for attributed large language models")\], and interactive search \[ [69](https://arxiv.org/html/2603.07379v1#bib.bib8 "WebGPT: browser-assisted question-answering with human feedback")\] proved that agents can optimize trajectories based on environmental observations.

As illustrated in Figure [1](https://arxiv.org/html/2603.07379v1#S1.F1 "Figure 1 ‣ I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), the convergence of dynamic retrieval policies with autonomous planning loops has crystallized into a new paradigm: Agentic RAG\[ [87](https://arxiv.org/html/2603.07379v1#bib.bib34 "Agentic retrieval-augmented generation: a survey on agentic rag")\]. In this architecture, retrieval is no longer a preprocessing step, but an explicitly managed tool within a multi-step, policy-driven reasoning trajectory \[ [22](https://arxiv.org/html/2603.07379v1#bib.bib24 "Is agentic rag worth it? an experimental comparison of rag approaches")\]. The LLM orchestrates the entire process, deciding which actions to perform, whether to iterate, and how to adaptively search at multiple granularities \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\]. This requires a fundamental shift from fixed retrieve-then-read workflows to modular, pattern-based control strategies \[ [91](https://arxiv.org/html/2603.07379v1#bib.bib33 "Workflow patterns: on the expressive power of petri-net-based workflow languages")\].

![Refer to caption](https://arxiv.org/html/2603.07379v1/diagrams/Introduction.png)Figure 1: High-level progression from single-pass retrieval-augmented generation to iterative retrieval and Agentic RAG. This demonstrates the architectural shift from static, one-shot context utilization to explicit multi-step control over retrieval, reasoning, and termination, conceptually anchoring the systematization presented in this paper.

This paper positions itself as a Systematization of Knowledge (SoK). Currently, the rapid proliferation of Agentic RAG systems has led to severe field fragmentation, a lack of a unified taxonomy, and an absence of standardized evaluation frameworks. To address these systemic gaps, the main contributions of this work are summarized as follows:

- •


We provide a formal conceptualization of agentic retrieval-augmented generation by framing it as a sequential decision-making process that integrates reasoning, retrieval, memory, and tool interaction.

- •


We introduce a multi-dimensional taxonomy that organizes the design space of agentic RAG systems across planning strategies, retrieval orchestration, memory paradigms, and tool coordination mechanisms.

- •


We decompose agentic RAG architectures into core modular components and reusable design patterns, offering a systematic blueprint for building and analyzing such systems.

- •


We examine emerging evaluation challenges and propose a layered perspective that moves beyond static answer metrics toward trajectory-level assessment of reasoning and retrieval behavior.

- •


We identify key reliability risks, deployment challenges, and open research directions that will shape the future development of agentic RAG systems.


This section established the motivation for formalizing Agentic RAG as a distinct paradigm beyond static retrieval-augmented generation. We clarified the conceptual gap between traditional RAG pipelines and autonomous, multi-step reasoning architectures that dynamically plan, retrieve, and adapt. By framing the need for structured taxonomy, evaluation reform, and formal modeling, we positioned Agentic RAG as a systems problem rather than a prompt engineering extension. The next section grounds this discussion in the foundational evolution of large language models and retrieval systems, setting the theoretical and historical context necessary for formal definition.

## II Background and Foundations

This section establishes the conceptual building blocks that underpin Agentic RAG systems. It reviews large language models, classic retrieval-augmented generation, tool-augmented paradigms, planning, and memory architectures. The goal is to provide evidence-driven grounding for the formalization, taxonomy, and architectural discussions that follow.

### II-ALarge Language Models

Modern large language models (LLMs) rely on the Transformer architecture to learn contextual representations from massive corpora \[ [92](https://arxiv.org/html/2603.07379v1#bib.bib64 "Attention is all you need"), [42](https://arxiv.org/html/2603.07379v1#bib.bib65 "Scaling laws for neural language models")\]. While highly capable text generators, their ability to perform autonomous reasoning stems primarily from in-context learning: the capacity to adapt to novel tasks via prompt conditioning without parameter updates \[ [9](https://arxiv.org/html/2603.07379v1#bib.bib66 "Language models are few-shot learners")\]. Techniques like chain-of-thought prompting extend this by eliciting intermediate reasoning steps, allowing models to decompose problems and follow multi-step procedures \[ [97](https://arxiv.org/html/2603.07379v1#bib.bib67 "Chain-of-thought prompting elicits reasoning in large language models")\]. These zero-shot planning capabilities serve as the foundational engine for agentic control.

However, LLMs exhibit fundamental limitations that necessitate external augmentation. Their parametric knowledge is frozen at training time \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks")\], making them prone to hallucinating facts for novel or niche queries \[ [37](https://arxiv.org/html/2603.07379v1#bib.bib68 "A survey on hallucination in large language models: principles, taxonomy, challenges, and open questions")\]. Furthermore, simply expanding the context window to inject more information is insufficient; models frequently ignore relevant data placed in the middle of long inputs, a vulnerability known as the “lost in the middle” effect \[ [55](https://arxiv.org/html/2603.07379v1#bib.bib4 "Lost in the middle: how language models use long contexts")\]. Overcoming these constraints requires active tool invocation and dynamic retrieval rather than passive text generation.

### II-BRetrieval-Augmented Generation

To address the knowledge deficit of frozen LLMs, Retrieval-Augmented Generation (RAG) couples a parametric generator with a non-parametric retrieval index \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks")\]. Classic RAG utilizes dense retrieval models (e.g., DPR) to map queries and documents into a shared embedding space, fetching the top-kk most relevant passages for the generator to condition upon \[ [44](https://arxiv.org/html/2603.07379v1#bib.bib2 "Dense passage retrieval for open-domain question answering")\]. Extensions like Fusion-in-Decoder (FiD) allow models to fuse evidence from multiple retrieved documents efficiently while maintaining tractable compute \[ [40](https://arxiv.org/html/2603.07379v1#bib.bib3 "Leveraging passage retrieval with generative models for open domain question answering")\].

Despite these advances, standard RAG architectures rely on a strictly static control flow: retrieve once, then generate. This deterministic pipeline is fundamentally brittle. Retrieval quality depends entirely on the initial, often underspecified user query, with no mechanism to refine the search based on intermediate generation states \[ [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\]. Because the retrieved context is fixed upfront, the system cannot autonomously self-correct if the initial evidence is noisy or incomplete \[ [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\]. These structural rigidities directly motivate the shift toward iterative, policy-driven retrieval frameworks.

### II-CTool-Augmented and Agentic LLMs

A parallel research trajectory reframed LLMs from static text generators to interactive agents capable of taking actions in external environments. ReAct (Reasoning and Acting) introduced a prompting paradigm that interleaves explicit reasoning traces with actions (e.g., search queries, API calls), enabling the model to gather information iteratively and adjust its trajectory based on observations \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\]. Toolformer addressed a complementary challenge: teaching models to autonomously decide which tools to invoke, when to invoke them, and how to incorporate results \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\]. MRKL Systems proposed a modular neuro-symbolic architecture in which an LLM serves as a router that delegates to specialized external modules, emphasizing extensibility beyond pure parametric capabilities \[ [43](https://arxiv.org/html/2603.07379v1#bib.bib7 "MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning")\].

The concept of agentic LLMs further crystallized through work on self-improvement and reflective control. Reflexion introduced verbal reinforcement learning, where an agent stores textual reflections on its past failures in an episodic memory buffer and uses them to improve subsequent attempts \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\]. A comprehensive survey by Wang et al. formalized the LLM-based autonomous agent as a system comprising profiling, memory, planning, and action modules \[ [94](https://arxiv.org/html/2603.07379v1#bib.bib69 "A survey on large language model based autonomous agents")\]. These developments established the agent design patterns—planning, tool use, and reflection—that Agentic RAG systems embed directly into the retrieval pipeline.

### II-DMulti-Hop Reasoning and Planning

Many knowledge-intensive tasks require reasoning across multiple pieces of evidence that cannot be retrieved in a single step. HotpotQA formalized this requirement by introducing a multi-hop question answering benchmark where systems must reason over multiple supporting documents to derive an answer \[ [106](https://arxiv.org/html/2603.07379v1#bib.bib30 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")\]. Standard retrieval approaches struggle with such tasks because the information needed for later reasoning steps depends on intermediate deductions, creating a dependency that single-pass retrieval cannot resolve \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\].

Query decomposition addresses this challenge by breaking a complex query into simpler sub-questions. Least-to-most prompting solves decomposed problems sequentially \[ [116](https://arxiv.org/html/2603.07379v1#bib.bib16 "Least-to-most prompting enables complex reasoning in large language models")\], while Plan-and-Solve prompting generates an explicit upfront plan before execution \[ [95](https://arxiv.org/html/2603.07379v1#bib.bib17 "Plan-and-solve prompting: improving zero-shot chain-of-thought reasoning by large language models")\]. Self-Ask extends this paradigm by teaching models to generate explicit follow-up questions and route them to a search engine \[ [78](https://arxiv.org/html/2603.07379v1#bib.bib15 "Measuring and narrowing the compositionality gap in language models")\].

Interleaved retrieval-reasoning approaches take this further by tightly coupling retrieval with ongoing chain-of-thought generation. IRCoT interleaves reasoning steps with retrieval calls, using the evolving trace to guide what to retrieve next \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\]. Tree-of-Thoughts generalizes this toward explicit tree-structured exploration with search and self-evaluation \[ [107](https://arxiv.org/html/2603.07379v1#bib.bib71 "Tree of thoughts: deliberate problem solving with large language models")\]. These methods establish the reasoning foundations upon which agentic retrieval systems build their planning mechanisms.

### II-EMemory-Augmented Systems

Effective multi-step reasoning requires maintaining and updating state across interactions. Short-term memory in agentic systems typically corresponds to the evolving context window: the accumulation of observations, actions, and intermediate outputs. However, as contexts grow long, models exhibit degraded utilization of information, motivating strategies for dynamic context pruning and selective attention \[ [55](https://arxiv.org/html/2603.07379v1#bib.bib4 "Lost in the middle: how language models use long contexts")\].

Long-term memory systems enable agents to retain and recall information across tasks or sessions. Retrieval-based memory stores past experiences as embeddings in a vector store and retrieves relevant entries at inference time, functioning analogously to RAG but over the agent’s own history \[ [75](https://arxiv.org/html/2603.07379v1#bib.bib70 "Generative agents: interactive simulacra of human behavior")\]. Episodic memory captures structured records of past interaction trajectories, including actions taken and outcomes achieved \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\].

Recent work proposes unified architectures that dynamically manage both short-term working memory and long-term persistent storage, allowing agents to selectively consolidate, retrieve, and forget information based on task demands \[ [110](https://arxiv.org/html/2603.07379v1#bib.bib47 "Agentic memory: learning unified long-term and short-term memory management for large language model agents")\]. These persistent memory mechanisms act as a necessary prerequisite for the state-tracking capabilities that distinguish Agentic RAG from static pipelines.

The progression from static generation to retrieval-augmented systems reveals the architectural primitives that make autonomous reasoning possible. However, the literature lacks a precise formal boundary distinguishing iterative retrieval from true agentic behavior. The following section formalizes Agentic RAG using necessary and sufficient conditions and frames it within a sequential decision-making model to resolve this ambiguity.

## III From Static RAG to Agentic RAG

The transition from static Retrieval-Augmented Generation (RAG) to agentic RAG represents a fundamental paradigm shift in how large language models (LLMs) interact with external knowledge. While traditional RAG operates strictly as a linear pipeline—fetching documents based on an initial query and passing them to a generator—it lacks the capacity for autonomous correction, multi-step reasoning, and dynamic context formulation. This section traces the evolutionary path from static pipelines to planning-driven retrieval systems. We formally define Agentic RAG, explicitly mathematically map its state transition and control policies, and demarcate the boundary between single-pass active retrieval and true agentic workflows.

### III-ALimitations of Standard RAG Pipelines

Standard RAG architectures \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks")\] decouple knowledge retrieval from text generation through a deterministic, sequential mechanism. Given a user query qq and a knowledge corpus 𝒞\\mathcal{C}, a retriever fetches a top-kk set of documents DD, and the generator produces an output yy conditioned on qq and DD. This static, one-shot retrieval paradigm suffers from three critical systemic limitations:

First, it is highly susceptible to retrieval irrelevance and context overloading. If the initial embedding maps the query to suboptimal documents, the generator is forced to condition its output on irrelevant noise. As demonstrated by Liu et al. \[ [54](https://arxiv.org/html/2603.07379v1#bib.bib53 "Lost in the middle: how language models use long contexts")\], LLMs suffer from a “lost in the middle” phenomenon, where the inclusion of excessive, low-signal retrieved context degrades reasoning quality.

Second, static pipelines possess no adaptive reasoning or correction loops. If a complex query requires synthesizing information across disparate documents that do not share semantic similarity in the vector space, a single-pass retriever will fail to fetch the requisite connective context \[ [89](https://arxiv.org/html/2603.07379v1#bib.bib54 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions"), [45](https://arxiv.org/html/2603.07379v1#bib.bib59 "Baleen: robust multi-hop reasoning at scale via condensed retrieval")\].

Third, this architecture is prone to error propagation. Because the retrieval phase is strictly isolated from the generation phase, the LLM cannot pause generation to request missing information, resulting in hallucinations when the retrieved context is insufficient \[ [84](https://arxiv.org/html/2603.07379v1#bib.bib55 "Trusting your evidence: hallucinate less with context-aware decoding")\].

### III-BNeed for Iterative Retrieval

To address the brittleness of one-shot retrieval, the field moved toward iterative retrieval mechanisms. Complex user intents, particularly in domains requiring multi-hop reasoning (e.g., answering compositional questions over datasets like HotpotQA \[ [106](https://arxiv.org/html/2603.07379v1#bib.bib30 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")\] or MuSiQue \[ [47](https://arxiv.org/html/2603.07379v1#bib.bib57 "MuSiQue: multihop questions via single-hop question generation")\]), rarely map to a single contiguous text chunk.

Iterative retrieval allows the system to execute sequential queries against the database, where subsequent queries are conditioned on the information retrieved in prior steps \[ [27](https://arxiv.org/html/2603.07379v1#bib.bib56 "Enabling large language models to generate text with citations")\]. This necessity arises from the problem of query reformulation. A user’s initial prompt is often underspecified. Iterative systems employ the LLM to rewrite or expand the query based on partial information, progressively building a high-fidelity context window. However, early iterative retrieval models relied on heuristic triggers (e.g., retrieving every nn tokens) rather than semantic understanding of when external knowledge was actually required.

### III-CEmergence of Planning-Driven Retrieval

The limitations of heuristic-based iterative retrieval precipitated the integration of planning modules, leading to planning-driven retrieval. Inspired by the ReAct (Reasoning and Acting) framework \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\], architectures began coupling the retriever with an LLM planner.

Concurrently, paradigms like Toolformer \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\] established that LLMs could be trained to autonomously invoke external APIs. Models like WebGPT \[ [69](https://arxiv.org/html/2603.07379v1#bib.bib8 "WebGPT: browser-assisted question-answering with human feedback")\] demonstrated that LLMs could navigate text interfaces and execute search queries to gather evidence before formulating an answer. The emergence of open-source autonomous agent frameworks (e.g., AutoGPT \[ [80](https://arxiv.org/html/2603.07379v1#bib.bib58 "Auto-GPT: an autonomous GPT-4 experiment")\]) further normalized the concept of granting LLMs continuous execution privileges.

In this evolved paradigm, the LLM does not merely consume retrieved text; it actively decides when to invoke the retriever as an external tool, what specific query to pass to it, and how to evaluate the returned context against the overarching goal. This orchestration of retrieval through autonomous planning loops serves as the foundational architecture for Agentic RAG. The conceptual progression from deterministic, single-pass pipelines to this policy-driven framework is illustrated in Figure [2](https://arxiv.org/html/2603.07379v1#S3.F2 "Figure 2 ‣ III-C Emergence of Planning-Driven Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

![Refer to caption](https://arxiv.org/html/2603.07379v1/figures/rag_evolution.png)Figure 2: The architectural evolution from static one-shot RAG pipelines to the Agentic RAG POMDP formulation. The Agentic framework replaces linear generation with a cyclic control policy (πθ\\pi\_{\\theta}) managing a persistent memory state (ℳt\\mathcal{M}\_{t}).

### III-DFormal Definition of Agentic RAG

Agentic RAG is not defined by the presence of a retriever, but by the presence of an autonomous control policy that governs retrieval and reasoning over a discrete action space.

#### III-D1 System-Level Formalization

We model Agentic RAG as a finite-horizon Partially Observable Markov Decision Process (POMDP), where the external knowledge corpus 𝒞\\mathcal{C} constitutes a latent, partially observable information source. We formally define the system as the tuple:

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒮A​R​A​G=⟨𝒮e​n​v,𝒜,Ω,𝒪,πθ,ℳ,𝒯⟩\\mathcal{S}\_{ARAG}=\\langle\\mathcal{S}\_{env},\\mathcal{A},\\Omega,\\mathcal{O},\\pi\_{\\theta},\\mathcal{M},\\mathcal{T}\\rangle |  | (1) |

where:

- •


𝒮e​n​v\\mathcal{S}\_{env} is the latent true state of the required knowledge residing in 𝒞\\mathcal{C}.

- •


𝒜\\mathcal{A} is the discrete action space consisting of retrieval, reasoning, tool use, and termination: 𝒜=𝒜r​e​t∪𝒜r​e​a​s​o​n∪𝒜t​o​o​l∪{S​T​O​P}\\mathcal{A}=\\mathcal{A}\_{ret}\\cup\\mathcal{A}\_{reason}\\cup\\mathcal{A}\_{tool}\\cup\\{STOP\\}.

- •


Ω\\Omega is the observation space (e.g., text chunks returned by a retriever or outputs from a tool).

- •


𝒪​(ot\|st,at)\\mathcal{O}(o\_{t}\|s\_{t},a\_{t}) is the observation function that returns an observation ot∈Ωo\_{t}\\in\\Omega conditioned on the hidden state st∈𝒮e​n​vs\_{t}\\in\\mathcal{S}\_{env} and the action ata\_{t} taken.

- •


πθ​(at\|ℳt)\\pi\_{\\theta}(a\_{t}\|\\mathcal{M}\_{t}) is a stochastic control policy parameterized by the LLM (implemented via prompting or fine-tuning), conditioned on the observable history.

- •


ℳt\\mathcal{M}\_{t} is the dynamic working memory (or observable history hth\_{t}) at step tt. The working memory ℳt\\mathcal{M}\_{t} serves as a tractable approximation of the belief state btb\_{t}.

- •


𝒯​(st+1\|st,at)\\mathcal{T}(s\_{t+1}\|s\_{t},a\_{t}) is the latent state transition function.


In this formulation, the state sts\_{t} represents the evolving task context, including the user query, intermediate reasoning traces, retrieved documents, and relevant memory elements accumulated during interaction. The action ata\_{t} corresponds to decisions such as issuing a retrieval query, invoking an external tool, updating memory, or generating response tokens. The policy πθ​(at\|ℳt)\\pi\_{\\theta}(a\_{t}\|\\mathcal{M}\_{t}) defines the agent’s strategy for selecting actions conditioned on the current context. The environment captures external knowledge sources, retrieval systems, and tool interfaces with which the agent interacts during task execution.

At any discrete time step t∈\[0,Tm​a​x\]t\\in\[0,T\_{max}\] (where Tm​a​xT\_{max} is the finite horizon limit), the system maintains a memory state ℳt\\mathcal{M}\_{t} seeded with the initial user query qq. The stochastic policy πθ\\pi\_{\\theta} samples the next action at∼πθ(⋅\|ℳt)a\_{t}\\sim\\pi\_{\\theta}(\\cdot\|\\mathcal{M}\_{t}).

If the policy selects a retrieval action at=Retrieve​(qt′)a\_{t}=\\text{Retrieve}(q^{\\prime}\_{t}), the observation function queries the latent corpus and deterministically updates the memory with the observation oto\_{t} such that ℳt+1=ℳt∪𝒪​(ot\|st,at)\\mathcal{M}\_{t+1}=\\mathcal{M}\_{t}\\cup\\mathcal{O}(o\_{t}\|s\_{t},a\_{t}). If the policy dictates a reasoning step at=Reason​(ct)a\_{t}=\\text{Reason}(c\_{t}), the intermediate conclusion ctc\_{t} is appended as ℳt+1=ℳt∪{ct}\\mathcal{M}\_{t+1}=\\mathcal{M}\_{t}\\cup\\{c\_{t}\\}. The process iterates strictly within the finite horizon Tm​a​xT\_{max} until πθ\\pi\_{\\theta} outputs the S​T​O​PSTOP action, triggering the final generation y=G​(ℳT)y=G(\\mathcal{M}\_{T}).

In practice, maintaining an exact Bayesian belief state over the environment is infeasible for large-scale language agents. Instead, most implementations approximate the belief state through structured memory representations ℳt\\mathcal{M}\_{t}. These representations may include intermediate reasoning traces, retrieved document sets, tool outputs, and summarized contextual knowledge accumulated across reasoning steps. Belief updates therefore correspond to memory update operations such as selective retrieval augmentation, summarization, pruning of redundant information, or learned memory controllers that retain high-utility signals while discarding low-relevance context. Such approximations enable tractable reasoning while preserving relevant task information across multi-step interactions.

#### III-D2 Necessary Properties

Based on the POMDP formalization above, an Agentic RAG system must exhibit the following intrinsic properties. A direct mapping between these operational requirements and their corresponding formal POMDP components is summarized in Table [I](https://arxiv.org/html/2603.07379v1#S3.T1 "TABLE I ‣ III-D2 Necessary Properties ‣ III-D Formal Definition of Agentic RAG ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

1. 1.


Iterative Control: The system must possess a feedback loop governed by a stochastic policy πθ\\pi\_{\\theta}, allowing for multiple transitions before final generation.

2. 2.


Dynamic Retrieval: Retrieval queries qt′q^{\\prime}\_{t} must be conditionally generated at runtime based on the evolving memory state ℳt\\mathcal{M}\_{t}.

3. 3.


Tool-Mediated Interaction: The retriever must be modeled as an explicit function call within the action space 𝒜\\mathcal{A}, subject to validation via the observation function.

4. 4.


State Persistence: The system must maintain an episodic working memory ℳt\\mathcal{M}\_{t} that persists across the control loop to approximate the fully observable state.


While these four properties are analytically necessary to classify a system as Agentic RAG, they are not sufficient to guarantee stability or safety. An architecture may possess the correct POMDP loops but still fail due to an unaligned policy or corrupted memory—a limitation that necessitates the rigorous evaluation and safety frameworks discussed in subsequent sections. Ultimately, Agentic RAG constitutes a partially observable sequential decision process under adaptive retrieval policies.

TABLE I: Mapping Agentic System Properties to POMDP Formalization

| Agentic Property | POMDP Component | Operational Interpretation |
| --- | --- | --- |
| Iterative Control | Stochastic Policy πθ\\pi\_{\\theta} | Non-deterministic action selection governing the loop |
| Dynamic Retrieval | Action Space 𝒜\\mathcal{A} | Query generation treated as a discrete runtime action |
| Tool Mediation | Observation Model 𝒪\\mathcal{O} | External API interaction returning state context |
| State Persistence | Belief State bt≈ℳtb\_{t}\\approx\\mathcal{M}\_{t} | Memory acts as a tractable approximation of hidden state |
| Termination | Finite Horizon Tm​a​xT\_{max} | Constrained loop depth to prevent infinite execution |

#### III-D3 Distinguishing Active RAG vs Agentic RAG

A common source of ambiguity in the literature is the conflation of “Active RAG” (e.g., FLARE \[ [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\]) and Agentic RAG. Active RAG dynamically decides when to retrieve during the token generation process, often using probability confidence thresholds to trigger a database lookup. However, Active RAG is fundamentally a single-pass generative process that uses retrieval to fill localized knowledge gaps.

In contrast, Agentic RAG separates planning from generation. It is policy-driven, executes multi-step tool use, and can perform operations that do not directly result in output tokens (e.g., self-correction, discarding retrieved context, or switching tools). A summary of these architectural distinctions is provided in Table [II](https://arxiv.org/html/2603.07379v1#S3.T2 "TABLE II ‣ III-D3 Distinguishing Active RAG vs Agentic RAG ‣ III-D Formal Definition of Agentic RAG ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

TABLE II: Architectural Distinctions Between Active RAG and Agentic RAG

| Feature | Active RAG | Agentic RAG |
| --- | --- | --- |
| Trigger Mechanism | Log-probability thresholds or token heuristics | Policy-driven reasoning and explicit tool-calling |
| Control Flow | Single-pass, forward-generating | Iterative, multi-step planning loops |
| Planning Explicitness | Implicit during generation | Explicit deliberative phase |
| Context Management | Append-only (accumulates fetched text) | Read/Write/Prune capabilities over working memory |
| Failure Handling | Cannot self-correct prior token generation | Can discard poor retrieval and explicitly try new query |

### III-EProblem Formulation of Agentic RAG Systems

Given the POMDP representation, the engineering of an Agentic RAG system can be formulated as a constrained sequential decision-making problem. The objective is to optimize the stochastic policy πθ\\pi\_{\\theta} to maximize the fidelity of the final output yy relative to an ideal response y∗y^{\*}, while strictly minimizing the computational overhead of the iterative loop.

We define an objective function over a trajectory τ=(ℳ0,a0,o1,ℳ1,…,ℳT)\\tau=(\\mathcal{M}\_{0},a\_{0},o\_{1},\\mathcal{M}\_{1},\\dots,\\mathcal{M}\_{T}) generated by policy πθ\\pi\_{\\theta}. Let Rt​a​s​k​(y,y∗)R\_{task}(y,y^{\*}) be the terminal reward function measuring response quality. Let C​(at)C(a\_{t}) represent the step-wise cost function, which models latency, token consumption, and API limits. The problem formulation of an Agentic RAG system is:

|     |     |     |     |
| --- | --- | --- | --- |
|  | maxπθ⁡𝔼τ∼πθ​\[Rt​a​s​k​(y,y∗)−λ​∑t=0T−1C​(at)\]\\max\_{\\pi\_{\\theta}}\\mathbb{E}\_{\\tau\\sim\\pi\_{\\theta}}\\left\[R\_{task}(y,y^{\*})-\\lambda\\sum\_{t=0}^{T-1}C(a\_{t})\\right\] |  | (2) |

where λ\\lambda is a regularization parameter controlling the trade-off between reasoning depth and operational efficiency.

This section established the theoretical backbone of Agentic RAG by formalizing its state transitions and defining the necessary properties of iterative control, dynamic retrieval, and memory persistence. We demonstrated that moving beyond static and active RAG pipelines fundamentally transforms the architecture into a budget-constrained sequential decision-making problem. Having clarified this structural foundation, Section [IV](https://arxiv.org/html/2603.07379v1#S4 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") systematizes the field by classifying existing Agentic RAG frameworks across these operational dimensions.

## IV Taxonomy of Agentic RAG Systems

Retrieval-Augmented Generation (RAG) couples a _Retriever_ with a _Generator_—typically a large language model (LLM)—to ground model outputs in external evidence rather than relying solely on parametric knowledge \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks"), [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey"), [21](https://arxiv.org/html/2603.07379v1#bib.bib89 "A survey on RAG meeting LLMs: towards retrieval-augmented large language models")\]. _Agentic RAG_ extends this paradigm by introducing an explicit _Planner_ that governs _Tool Invocation_ (including retrieval) under a _Control Policy_, thereby enabling _Iterative Retrieval_, _Dynamic Context Construction_, and _Multi-step Reasoning_ beyond a single retrieve-then-generate pass \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models"), [71](https://arxiv.org/html/2603.07379v1#bib.bib109 "Function calling — openai api documentation"), [5](https://arxiv.org/html/2603.07379v1#bib.bib110 "Tool use with claude: overview (claude api docs)"), [30](https://arxiv.org/html/2603.07379v1#bib.bib112 "Agent development kit (adk) documentation")\].

This section provides an _attribute-based taxonomy_: we classify Agentic RAG systems by orthogonal axes that describe what kind of system they are, not how to implement them. Section [V](https://arxiv.org/html/2603.07379v1#S5 "V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") instantiates these classes into concrete architectures, while Section [VI](https://arxiv.org/html/2603.07379v1#S6 "VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") abstracts recurring solutions as design patterns.

To provide a rigorous classification of the Agentic RAG landscape, we propose a taxonomy organized across four dimensions: Planning, Memory, Tool Orchestration, and Retrieval Strategy. As illustrated in Figure [3](https://arxiv.org/html/2603.07379v1#S4.F3 "Figure 3 ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), these dimensions are designed to be Mutually Exclusive and Collectively Exhaustive (MECE) regarding the system’s operational control flow. A system may implement varying degrees of complexity within each dimension, but every Agentic RAG architecture must inherently make a design choice across these four axes. Table [III](https://arxiv.org/html/2603.07379v1#S4.T3 "TABLE III ‣ IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") synthesizes this classification, mapping common archetypes to their core taxonomic attributes.

![Refer to caption](https://arxiv.org/html/2603.07379v1/figures/section4_taxonomy.png)Figure 3: Taxonomy of Agentic RAG systems across architecture, retrieval strategy, reasoning paradigm, and memory/context management. This structural mapping demonstrates how orthogonal control-flow decisions combine to form distinct, reproducible agentic archetypes.

### IV-AArchitectural Taxonomy

Architectural taxonomy in Agentic RAG classifies systems by _agent topology_—i.e., how many distinct decision-making entities exist, where the Planner function is located, and whether roles such as retrieval and generation are centrally controlled or distributed. This axis is intentionally orthogonal to retrieval strategy: a single-agent system may still perform iterative retrieval, and a multi-agent system may still perform one-shot retrieval if its control policy is static \[ [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey"), [21](https://arxiv.org/html/2603.07379v1#bib.bib89 "A survey on RAG meeting LLMs: towards retrieval-augmented large language models")\]. Modern SDKs and frameworks expose topology and tool loops explicitly \[ [72](https://arxiv.org/html/2603.07379v1#bib.bib108 "Agents sdk — openai api documentation"), [49](https://arxiv.org/html/2603.07379v1#bib.bib102 "LangChain agents documentation")\], enabling the same application class to be realized under different topologies \[ [5](https://arxiv.org/html/2603.07379v1#bib.bib110 "Tool use with claude: overview (claude api docs)"), [30](https://arxiv.org/html/2603.07379v1#bib.bib112 "Agent development kit (adk) documentation"), [56](https://arxiv.org/html/2603.07379v1#bib.bib105 "LlamaIndex agents documentation")\].

#### IV-A1 Single-Agent RAG

Single-Agent RAG denotes systems where one agent jointly performs planning and generation, invoking retrieval and other tools under a single control policy. Classical RAG formulations already combine a retriever and generator, but they need not be agentic if retrieval is purely pre-specified; the agentic variant emerges when the planner role adapts actions \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks"), [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey"), [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\]. Single-agent loops are directly supported in major frameworks \[ [72](https://arxiv.org/html/2603.07379v1#bib.bib108 "Agents sdk — openai api documentation"), [49](https://arxiv.org/html/2603.07379v1#bib.bib102 "LangChain agents documentation"), [56](https://arxiv.org/html/2603.07379v1#bib.bib105 "LlamaIndex agents documentation")\], while other orchestrators provide lightweight agent abstractions suitable for retrieval-centric tool use \[ [38](https://arxiv.org/html/2603.07379v1#bib.bib106 "Smolagents documentation"), [39](https://arxiv.org/html/2603.07379v1#bib.bib107 "Smolagents (github repository)")\].

#### IV-A2 Planner–Executor Architectures

Planner–Executor architectures separate the Planner (which decomposes goals, selects tool invocation, and sets retrieval objectives) from an Executor (which carries out retrieval and returns observations). The defining criterion is explicit role separation and an inter-role interface that mediates decision and action \[ [83](https://arxiv.org/html/2603.07379v1#bib.bib91 "HuggingGPT: solving AI tasks with chatgpt and its friends in hugging face"), [43](https://arxiv.org/html/2603.07379v1#bib.bib7 "MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning"), [20](https://arxiv.org/html/2603.07379v1#bib.bib92 "Improving planning of agents for long-horizon tasks")\]. HuggingGPT adopts a controller/executor framing where an LLM orchestrates specialized models, while tool-use documentation highlights that tool calling is a multi-step interaction boundary requiring delegation and handoffs \[ [71](https://arxiv.org/html/2603.07379v1#bib.bib109 "Function calling — openai api documentation"), [5](https://arxiv.org/html/2603.07379v1#bib.bib110 "Tool use with claude: overview (claude api docs)")\].

#### IV-A3 Multi-Agent RAG Systems

Multi-Agent RAG Systems distribute planning, retrieval, and generation across multiple agents that interact to complete a query. The defining property is distributed decision-making with interaction among agents \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation"), [30](https://arxiv.org/html/2603.07379v1#bib.bib112 "Agent development kit (adk) documentation"), [48](https://arxiv.org/html/2603.07379v1#bib.bib103 "LangGraph (github repository)"), [17](https://arxiv.org/html/2603.07379v1#bib.bib101 "CrewAI: multi-agent framework (github repository)")\]. AutoGen formalizes multi-agent conversation with tool-using agents \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation"), [63](https://arxiv.org/html/2603.07379v1#bib.bib100 "AutoGen documentation: multi-agent conversation framework")\], whereas frameworks like LangGraph provide an orchestration substrate for graph-structured agentic workloads \[ [48](https://arxiv.org/html/2603.07379v1#bib.bib103 "LangGraph (github repository)"), [50](https://arxiv.org/html/2603.07379v1#bib.bib104 "LangGraph: agent orchestration framework (product page)")\].

### IV-BRetrieval Strategy Taxonomy

Retrieval strategy taxonomy captures when and how the Retriever is invoked across a trajectory, and how retrieved evidence is incorporated into dynamic context construction. Agentic systems increasingly treat retrieval as a repeated, state-dependent action rather than an upfront preprocessing step \[ [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation"), [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey"), [21](https://arxiv.org/html/2603.07379v1#bib.bib89 "A survey on RAG meeting LLMs: towards retrieval-augmented large language models")\].

#### IV-B1 One-Shot Retrieval

One-Shot Retrieval refers to a single retrieval action conditioned on the user query followed by generation conditioned on a fixed retrieved context, matching baseline RAG \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks"), [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey")\]. Within Agentic RAG, this remains a class where no state-dependent retrieval actions occur after initiation, regardless of whether a Planner exists \[ [72](https://arxiv.org/html/2603.07379v1#bib.bib108 "Agents sdk — openai api documentation"), [49](https://arxiv.org/html/2603.07379v1#bib.bib102 "LangChain agents documentation")\].

#### IV-B2 Iterative Retrieval

Iterative Retrieval performs multiple retrieval actions during a single query resolution, where later retrievals depend on intermediate state. IRCoT interleaves retrieval with Chain-of-Thought steps \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\]. Iter-RetGen repeats retrieval and generation with intermediate generations informing retrieval \[ [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\]. This class increases the degrees of freedom of the control policy and tightly couples retrieval with token economics \[ [71](https://arxiv.org/html/2603.07379v1#bib.bib109 "Function calling — openai api documentation")\].

#### IV-B3 Self-Refining Retrieval

Self-Refining Retrieval couples retrieval with critique, revision, or self-evaluation such that queries and evidence are refined to increase faithfulness \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection"), [25](https://arxiv.org/html/2603.07379v1#bib.bib90 "RARR: researching and revising what language models say, using language models")\]. Self-RAG learns to retrieve on-demand and critique both retrieved passages and generations \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\]. Such systems often employ hybrid or learned control policies to drive active knowledge assimilation from retrieved evidence \[ [103](https://arxiv.org/html/2603.07379v1#bib.bib99 "ActiveRAG: autonomously knowledge assimilation and accommodation through retrieval-augmented agents"), [111](https://arxiv.org/html/2603.07379v1#bib.bib98 "Agentic memory: learning unified long-term and short-term memory management for large language model agents")\].

### IV-CReasoning Taxonomy

Reasoning taxonomy classifies the form of multi-step reasoning used to decide tool invocation and transform evidence into grounded outputs. We adopt four classes: Chain-of-Thought, ReAct-style interleaving, reflection-based reasoning, and tree-based exploration \[ [97](https://arxiv.org/html/2603.07379v1#bib.bib67 "Chain-of-thought prompting elicits reasoning in large language models"), [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models"), [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning"), [107](https://arxiv.org/html/2603.07379v1#bib.bib71 "Tree of thoughts: deliberate problem solving with large language models")\].

#### IV-C1 Chain-of-Thought & ReAct-Style

Chain-of-Thought (CoT) prompting elicits a sequential reasoning trace of intermediate steps \[ [97](https://arxiv.org/html/2603.07379v1#bib.bib67 "Chain-of-thought prompting elicits reasoning in large language models")\], frequently acting as a query-construction substrate in IRCoT and planning decompositions \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions"), [95](https://arxiv.org/html/2603.07379v1#bib.bib17 "Plan-and-solve prompting: improving zero-shot chain-of-thought reasoning by large language models")\]. ReAct extends this by interleaving reasoning steps with actions (tool invocations), producing observations that update subsequent reasoning \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\]. Many agent frameworks describe agents as running tools in a loop until a stop condition, corresponding closely to the ReAct taxonomy class \[ [49](https://arxiv.org/html/2603.07379v1#bib.bib102 "LangChain agents documentation"), [72](https://arxiv.org/html/2603.07379v1#bib.bib108 "Agents sdk — openai api documentation")\].

#### IV-C2 Reflection & Tree-Based Exploration

Reflection-based reasoning introduces explicit self-evaluation steps that critique intermediate reasoning, retrieved evidence, or generated assertions. Reflexion stores this feedback in an episodic memory buffer to improve later behavior \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\], while RARR retrieves evidence specifically to attribute and revise generated text \[ [25](https://arxiv.org/html/2603.07379v1#bib.bib90 "RARR: researching and revising what language models say, using language models")\]. Conversely, Tree-based exploration treats reasoning as a search over multiple candidate branches. Tree-of-Thoughts realizes this by proposing, evaluating, and expanding thoughts with backtracking \[ [107](https://arxiv.org/html/2603.07379v1#bib.bib71 "Tree of thoughts: deliberate problem solving with large language models")\], supporting evidence gathering for competing hypotheses.

### IV-DMemory and Context Paradigms

Agentic RAG must manage memory that persists across episodes and the active context given to the Generator at each step. Long-context models do not remove the need for structured context selection, as performance often degrades depending on the position of relevant information within long inputs \[ [55](https://arxiv.org/html/2603.07379v1#bib.bib4 "Lost in the middle: how language models use long contexts")\]. Consequently, Dynamic Context Pruning has emerged to remove or compress retrieved content before generation. Methods like FILCO \[ [96](https://arxiv.org/html/2603.07379v1#bib.bib94 "Learning to filter context for retrieval-augmented generation")\] and Provence \[ [14](https://arxiv.org/html/2603.07379v1#bib.bib95 "Provence: efficient and robust context pruning for retrieval-augmented generation")\] learn to filter retrieved contexts, reducing overhead and mitigating irrelevant evidence—a capability that becomes increasingly critical under iterative and multi-agent settings \[ [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\].

Beyond active context window management, architectures require Episodic Memory to store temporally bounded trajectories of agent behavior and feedback. For instance, Reflexion stores reflective feedback in an episodic buffer \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\], while Generative Agents utilize a memory stream to support iterative planning \[ [76](https://arxiv.org/html/2603.07379v1#bib.bib93 "Generative agents: interactive simulacra of human behavior")\]. This episodic logging acts as a localized attention mechanism, preserving reasoning fidelity while managing API costs across distinct task steps.

To maintain coherence across multiple independent sessions, systems also deploy Persistent Long-Horizon Memory. This paradigm retains information across sessions by persisting latent states into vector databases. Frameworks like MemoryBank \[ [115](https://arxiv.org/html/2603.07379v1#bib.bib96 "Enhancing large language models with long-term memory")\] and MemGPT \[ [74](https://arxiv.org/html/2603.07379v1#bib.bib97 "MemGPT: towards llms as operating systems")\] explicitly target storing, recalling, and updating long-term interaction memories. These systems define memory-refresh strategies—dictating how memory is updated, consolidated, or decayed over time—shifting the architecture from a stateless functional call to a stateful, continuous entity \[ [111](https://arxiv.org/html/2603.07379v1#bib.bib98 "Agentic memory: learning unified long-term and short-term memory management for large language model agents"), [72](https://arxiv.org/html/2603.07379v1#bib.bib108 "Agents sdk — openai api documentation")\].

### IV-ECross-Dimensional Trade-Off Analysis

Taxonomy dimensions interact in practice; choices along one dimension induce constraints along others. These trade-offs are surfaced in both academic work on iterative retrieval and industrial documentation on tool calling and orchestration \[ [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation"), [71](https://arxiv.org/html/2603.07379v1#bib.bib109 "Function calling — openai api documentation"), [4](https://arxiv.org/html/2603.07379v1#bib.bib111 "Introducing advanced tool use on the claude developer platform"), [30](https://arxiv.org/html/2603.07379v1#bib.bib112 "Agent development kit (adk) documentation")\].

#### IV-E1 Retrieval Depth vs Cost

Deeper retrieval (iterative/self-refining) improves coverage for multi-hop and long-form tasks \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions"), [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy"), [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\] but increases cost via more tool calls, longer contexts, and extra generations. Pruning methods partially decouple depth from cost but risk removing necessary evidence \[ [96](https://arxiv.org/html/2603.07379v1#bib.bib94 "Learning to filter context for retrieval-augmented generation"), [14](https://arxiv.org/html/2603.07379v1#bib.bib95 "Provence: efficient and robust context pruning for retrieval-augmented generation")\].

#### IV-E2 Planning Complexity vs Latency

Planner–executor separation, explicit planning, and tree-based exploration reduce error propagation but impose latency due to extra planning and coordination \[ [20](https://arxiv.org/html/2603.07379v1#bib.bib92 "Improving planning of agents for long-horizon tasks"), [107](https://arxiv.org/html/2603.07379v1#bib.bib71 "Tree of thoughts: deliberate problem solving with large language models")\]. Tool calling is inherently multi-step and can stack latency when sequential \[ [71](https://arxiv.org/html/2603.07379v1#bib.bib109 "Function calling — openai api documentation")\]. Parallel or reduced round-trip tool use is highlighted as a mitigation in industrial guidance \[ [4](https://arxiv.org/html/2603.07379v1#bib.bib111 "Introducing advanced tool use on the claude developer platform")\].

#### IV-E3 Cost, Latency, and Token Economics

Agentic RAG introduces token amplification: intermediate reasoning, tool queries, and critique steps expand generated tokens and multiply model invocations \[ [71](https://arxiv.org/html/2603.07379v1#bib.bib109 "Function calling — openai api documentation"), [49](https://arxiv.org/html/2603.07379v1#bib.bib102 "LangChain agents documentation")\]. Iterative retrieval paradigms often scale cost directly with the number of steps \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions"), [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\]. Learned tool-use decisions motivate budget-aware orchestration as a core control-policy property \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools"), [111](https://arxiv.org/html/2603.07379v1#bib.bib98 "Agentic memory: learning unified long-term and short-term memory management for large language model agents")\].

TABLE III: Consolidated taxonomy mapping archetypes to their core Agentic RAG attributes.

| Archetype | Topology | Retrieval | Reasoning | Memory/Context | Policy | Representative anchors |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline grounded generation | Single-agent | One-shot | Minimal / linear | Minimal; optional filtering | Heuristic | RAG \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks")\]; surveys \[ [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey"), [21](https://arxiv.org/html/2603.07379v1#bib.bib89 "A survey on RAG meeting LLMs: towards retrieval-augmented large language models")\] |
| Iterative evidence accumulation | Single-agent | Iterative | CoT / ReAct | Dynamic context construction | Heuristic/Hybrid | IRCoT \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\]; Iter-RetGen \[ [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\]; LangChain agents \[ [49](https://arxiv.org/html/2603.07379v1#bib.bib102 "LangChain agents documentation")\] |
| Reflective refinement | Single-agent | Self-refining | Reflection-based | Episodic critique; pruning | Hybrid/Learned | Self-RAG \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\]; RARR \[ [25](https://arxiv.org/html/2603.07379v1#bib.bib90 "RARR: researching and revising what language models say, using language models")\]; Reflexion \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\] |
| Role-separated orchestration | Planner–Executor | Iterative/self-refining | Planning + execution | Executor logging; pruning | Hybrid | HuggingGPT \[ [83](https://arxiv.org/html/2603.07379v1#bib.bib91 "HuggingGPT: solving AI tasks with chatgpt and its friends in hugging face")\]; MRKL \[ [43](https://arxiv.org/html/2603.07379v1#bib.bib7 "MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning")\]; OpenAI Agents \[ [72](https://arxiv.org/html/2603.07379v1#bib.bib108 "Agents sdk — openai api documentation")\] |
| Distributed knowledge work | Multi-agent | Iterative/mixed | ReAct/reflective | Agent-local episodic; aggregation | Hybrid | AutoGen \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation"), [63](https://arxiv.org/html/2603.07379v1#bib.bib100 "AutoGen documentation: multi-agent conversation framework")\]; CrewAI \[ [17](https://arxiv.org/html/2603.07379v1#bib.bib101 "CrewAI: multi-agent framework (github repository)")\]; LangGraph \[ [48](https://arxiv.org/html/2603.07379v1#bib.bib103 "LangGraph (github repository)")\]; ADK \[ [30](https://arxiv.org/html/2603.07379v1#bib.bib112 "Agent development kit (adk) documentation")\] |
| Memory-centric long-horizon | Any | Mixed | Reflection common | Persistent+episodic; refresh | Hybrid/Learned | MemoryBank \[ [115](https://arxiv.org/html/2603.07379v1#bib.bib96 "Enhancing large language models with long-term memory")\]; MemGPT \[ [74](https://arxiv.org/html/2603.07379v1#bib.bib97 "MemGPT: towards llms as operating systems")\]; AgeMem \[ [111](https://arxiv.org/html/2603.07379v1#bib.bib98 "Agentic memory: learning unified long-term and short-term memory management for large language model agents")\] |

TABLE IV: Mapping Representative Agentic RAG Systems to the Proposed Taxonomy Dimensions

| System | Planning Topology | Retrieval Strategy | Memory Model | Tool Coordination |
| --- | --- | --- | --- | --- |
| ReAct | Linear reasoning loop | Iterative retrieval | Short-term scratchpad | Search tools |
| A-RAG | Hierarchical planning | Progressive retrieval | Hybrid memory | Multi-stage retrieval tools |
| Search-R2 | Actor–refiner architecture | Search-integrated reasoning | Episodic memory | Retrieval and repair tools |
| LangGraph workflows | Graph-based control flow | Tool-triggered retrieval | Persistent state | Structured tool orchestration |
| AutoGen agents | Multi-agent coordination | Tool-driven retrieval | Shared memory | Multi-agent tool usage |

Table [IV](https://arxiv.org/html/2603.07379v1#S4.T4 "TABLE IV ‣ IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") illustrates how representative agentic RAG systems can be categorized using the proposed taxonomy dimensions. This mapping demonstrates that the taxonomy captures diverse architectures spanning different planning strategies, retrieval mechanisms, memory paradigms, and tool coordination patterns.

This taxonomy categorizes Agentic RAG systems along structural and operational attributes, separating topology, memory strategies, and retrieval dynamics from implementation details. By organizing systems through architectural properties rather than surface tools, we establish a stable comparative framework. Having defined these structural categories, the next section decomposes the internal architectural modules that operationalize these attributes in practice.

## V Core Architectural Components

Building upon the taxonomy established in the preceding classification frameworks, it becomes necessary to transition from a theoretical categorization of Agentic Retrieval-Augmented Generation (Agentic RAG) systems toward a concrete systems-engineering perspective. Standard RAG architectures often rely on rigid, linear pipelines—typically defined by a monolithic sequence of query rewriting, document selection, and answer generation \[ [87](https://arxiv.org/html/2603.07379v1#bib.bib34 "Agentic retrieval-augmented generation: a survey on agentic rag")\]. While these static joint optimization models maximize system performance for single-turn queries, their rigid topology restricts the agent to a uniform workflow, rendering them incapable of decomposing complex, multi-hop queries that demand variable reasoning paths \[ [87](https://arxiv.org/html/2603.07379v1#bib.bib34 "Agentic retrieval-augmented generation: a survey on agentic rag")\]. In contrast, Agentic RAG demands a decoupled yet highly orchestrated modular architecture capable of dynamic state management, iterative reasoning, and verifiable execution \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\].

To realize theoretical autonomy, an Agentic RAG system must be structured as a network of interdependent but specialized modules \[ [70](https://arxiv.org/html/2603.07379v1#bib.bib38 "MA-rag: multi-agent retrieval-augmented generation via collaborative chain-of-thought reasoning")\]. A critical systems boundary must be maintained between three core roles: the planner breaks a complex query into a sub-task graph; the controller (Reasoning Engine) executes the immediate next step based on the local state; and the orchestrator manages the routing of inputs and outputs across distinct, specialized agents. This formal division of labor ensures that cognitive reasoning is explicitly separated from tool execution \[ [70](https://arxiv.org/html/2603.07379v1#bib.bib38 "MA-rag: multi-agent retrieval-augmented generation via collaborative chain-of-thought reasoning")\]. As illustrated in Figure [4](https://arxiv.org/html/2603.07379v1#S5.F4 "Figure 4 ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), the modular interaction between these components enforces a closed feedback loop before any output is finalized. The specific inputs, outputs, and control signals governing these modules are synthesized in Table [V](https://arxiv.org/html/2603.07379v1#S5.T5 "TABLE V ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

![Refer to caption](https://arxiv.org/html/2603.07379v1/diagrams/System_Architecture_Overview.png)Figure 4: Core architectural components and control-flow relationships within a generalized Agentic RAG system. This demonstrates how the Reasoning Engine coordinates bidirectionally with Memory Systems and delegates execution to the Tool Orchestration Layer to maintain verifiable state control.TABLE V: Architectural Decomposition of Agentic RAG Modules

| Module | Inputs | Outputs | Control Signals | Feedback Loops |
| --- | --- | --- | --- | --- |
| Planner | User Query, Global State | Sub-task Graph | Depth limits, Max steps | Self-correction on plan failure |
| Controller | Sub-task, Local Memory | Action / Tool Call | Confidence thresholds | Observation-triggered replanning |
| Orchestrator | Multi-Agent Outputs | Final Synthesis | Agent-routing logic | Cross-agent consensus voting |

### V-APlanner Module

The Planner Module serves as the strategic orchestrator of the architecture \[ [12](https://arxiv.org/html/2603.07379v1#bib.bib39 "JADE: bridging the strategic-operational gap in dynamic agentic rag")\]. Unlike traditional pipelines where retrieval is triggered by a single user query, the Planner is responsible for dynamically parsing high-dimensional intents, decomposing them into tractable sub-tasks, and formulating an iterative execution strategy \[ [70](https://arxiv.org/html/2603.07379v1#bib.bib38 "MA-rag: multi-agent retrieval-augmented generation via collaborative chain-of-thought reasoning")\]. This module addresses the critical limitation of static RAG, which frequently fails when confronted with vague prompts or tasks requiring cross-domain synthesis \[ [87](https://arxiv.org/html/2603.07379v1#bib.bib34 "Agentic retrieval-augmented generation: a survey on agentic rag")\]. By establishing a structured collaboration topology, the Planner determines agent role assignments and constructs a flexible plan that adapts to environmental uncertainties \[ [12](https://arxiv.org/html/2603.07379v1#bib.bib39 "JADE: bridging the strategic-operational gap in dynamic agentic rag")\].

At a formal systemic level, task decomposition involves mapping a high-level query into a sequence of interdependent sub-queries under a defined control policy. The Planner evaluates the evolving system state to determine the optimal next action, invoking specialized sub-agents to generate detailed subqueries based on the step goal and prior outputs \[ [70](https://arxiv.org/html/2603.07379v1#bib.bib38 "MA-rag: multi-agent retrieval-augmented generation via collaborative chain-of-thought reasoning")\]. This dynamic invocation prevents the execution of rigid pipelines, allowing the system to average variable steps per question depending on the complexity of the query.

Historically, planner architectures suffered from a strategic-operational mismatch \[ [12](https://arxiv.org/html/2603.07379v1#bib.bib39 "JADE: bridging the strategic-operational gap in dynamic agentic rag")\]. In dynamic decoupled paradigms, the planner generates sophisticated plans that frozen, black-box execution tools are ill-equipped to fulfill, leading to execution failures. To resolve this, advanced architectures employ frameworks such as Joint Agentic Dynamic Execution (JADE), which unifies strategic planning and operational execution into a single learnable policy \[ [12](https://arxiv.org/html/2603.07379v1#bib.bib39 "JADE: bridging the strategic-operational gap in dynamic agentic rag")\]. This co-adaptation allows the planner to learn the precise capability boundaries of downstream executors, transitioning the module from a static prompt generator to an outcome-driven orchestrator.

### V-BRetrieval Engine

In an Agentic RAG architecture, the Retrieval Engine ceases to operate as a passive document filter; instead, it functions as an active logic co-processor \[ [1](https://arxiv.org/html/2603.07379v1#bib.bib44 "Capturing p: on the expressive power and efficient evaluation of boolean retrieval")\]. Standard embedding-based retrievers map queries into a latent vector space. However, fixed-dimensional embeddings are mathematically incapable of representing the full expressive spectrum of complex Boolean logic due to the linear separability limit \[ [1](https://arxiv.org/html/2603.07379v1#bib.bib44 "Capturing p: on the expressive power and efficient evaluation of boolean retrieval")\]. To circumvent this bottleneck, the agentic Retrieval Engine integrates diverse indexing structures—including dense vector search, sparse keyword matching, structured SQL databases, and formal knowledge graphs—orchestrated through programmable interfaces \[ [102](https://arxiv.org/html/2603.07379v1#bib.bib36 "KA-rag: integrating knowledge graphs and agentic retrieval-augmented generation for an intelligent educational question-answering model")\].

A defining implementation of this paradigm exposes hierarchical retrieval interfaces directly to the reasoning model \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\]. Rather than concatenating a massive context window that degrades model attention, architectures equip the agent with granular tools: broad lexical matching, dense conceptual retrieval, and the targeted extraction of specific document segments \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\]. This progressive information disclosure grants the agent autonomy to adjust its strategy dynamically. Empirical evaluations demonstrate that this interface design allows the agent to retrieve significantly fewer tokens than traditional static methods while achieving superior accuracy \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\].

Furthermore, to balance precision and latency, production-grade engines employ multiphase ranking architectures. Running deep machine learning ranking models across an entire candidate set introduces unacceptable latency stacking \[ [85](https://arxiv.org/html/2603.07379v1#bib.bib37 "Learning latency-aware orchestration for parallel multi-agent systems")\]. Staged ranking eliminates this trade-off by applying lightweight filters first, reserving heavier models strictly for top results \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\]. Empirical evaluations further demonstrate that coupling optimized semantic chunking with these two-stage cross-encoder re-ranking pipelines significantly improves retrieval faithfulness and mitigates hallucination risks in high-stakes environments \[ [60](https://arxiv.org/html/2603.07379v1#bib.bib121 "Chunking, retrieval, and re-ranking: an empirical evaluation of rag architectures for policy document question answering")\]. Industrial implementations also incorporate provenance-aware data fetching, executing dynamic queries against telemetry logs to ensure that retrieval is grounded in verifiable systemic evidence rather than hallucinated artifacts \[ [68](https://arxiv.org/html/2603.07379v1#bib.bib43 "LLM-driven provenance forensics for threat investigation and detection")\].

### V-CReasoning Engine (The Controller)

The Reasoning Engine operates as the controller of the Agentic RAG system, responsible for interpreting retrieved contexts, updating the internal consensus state, and managing the step-by-step resolution of the generated plan. While the Planner dictates the overarching strategy, the Reasoning Engine controls the microscopic flow of state updates, determining how individual tool outputs are synthesized into actionable intelligence. This module navigates dynamic environments, handles tool invocation errors, and dynamically allocates deliberation time based on task complexity.

A primary architectural requirement is the establishment of a robust interface between the language model’s cognitive space and the operational environment. In traditional workflows, models interact with verbose human-computer interfaces, which quickly overload the context window during long multi-turn dialogues, leading to attention degradation \[ [105](https://arxiv.org/html/2603.07379v1#bib.bib40 "SWE-agent: agent-computer interfaces enable automated software engineering")\]. Modern architectures solve this by formalizing the Agent-Computer Interface (ACI). An effective ACI enforces structured interaction patterns based on simple atomic commands, informative state observation, and efficient error recovery mechanisms \[ [105](https://arxiv.org/html/2603.07379v1#bib.bib40 "SWE-agent: agent-computer interfaces enable automated software engineering")\]. Instead of returning massive error traces, the ACI provides concise, syntax-checked feedback, preventing the agent from becoming trapped in infinite loops.

By operating through an ACI, the Reasoning Engine maintains strict execution control. It updates the system’s working state by applying iterative edits, executing sandboxed code, and navigating repositories without losing context. Artifacts generated by these actions constitute a consensus memory. The Reasoning Engine constantly reads and modifies this structured task state, ensuring that distributed agents maintain a cohesive understanding of the problem space across protracted execution sessions.

### V-DMemory Systems

Traditional RAG implementations treat context dynamically but transiently; the system reconstructs its worldview from scratch with every independent query. This assumption that memory is merely static storage leaves the agent without continuity of identity or historical awareness \[ [57](https://arxiv.org/html/2603.07379v1#bib.bib45 "Continuum memory architectures for long-horizon llm agents")\]. Agentic RAG redesigns this by separating memory into distinct subsystems: short-term working state, long-term persistent storage, and episodic memory \[ [57](https://arxiv.org/html/2603.07379v1#bib.bib45 "Continuum memory architectures for long-horizon llm agents")\]. Short-term memory acts as the immediate scratchpad, maintaining the evolving system state and conversational history. To prevent context exhaustion, this layer employs dynamic context pruning algorithms and strict state-checkpointing.

The most critical advancement is the formalization of Episodic Memory within Continuum Memory Architectures (CMA). CMA treats memory as a continuously evolving subsystem where memories persist, decay, and alter through retrieval-induced interference \[ [57](https://arxiv.org/html/2603.07379v1#bib.bib45 "Continuum memory architectures for long-horizon llm agents")\]. Episodic memory captures discrete trajectories of past problem-solving behaviors, allowing the agent to reflect on past experiences to inform future planning.

Advanced implementations grant the memory system intrinsic agency. Self-evolving memory systems allow artifacts to actively generate contextual descriptions and evolve their relational graphs as new experiences emerge \[ [2](https://arxiv.org/html/2603.07379v1#bib.bib46 "Agentic memory systems")\]. Furthermore, frameworks integrate memory management directly into the agent’s action space. Unlike systems relying on external heuristics, these utilize reinforcement learning to autonomously dictate when a memory should be accessed, retained, or forgotten, optimizing the cognitive load of the Reasoning Engine dynamically \[ [110](https://arxiv.org/html/2603.07379v1#bib.bib47 "Agentic memory: learning unified long-term and short-term memory management for large language model agents")\].

### V-ETool Orchestration Layer

The Tool Orchestration Layer acts as the middleware connecting the cognitive layers to external computational environments, APIs, and subsidiary sub-agents. It abstracts the complexities of API payload formatting, resource management, and execution limits, allowing the Reasoning Engine to interact with the environment through standardized interfaces. This layer is critical for transforming a theoretical reasoning path into actionable execution.

In sophisticated multi-agent ecosystems, tool orchestration is handled via specialized architectural primitives that enforce rigid hierarchy and state isolation. Hierarchical delegation allows a primary LLM agent to wrap a highly specialized secondary agent and invoke it as a functional tool. This facilitates the Coordinator/Dispatcher pattern, where a central agent manages requests and relinquishes control to specialists based on intent classification.

To manage execution flow without introducing unnecessary inference overhead, the orchestration layer employs deterministic routing components that control sub-agent execution structurally rather than cognitively. Sequential routers enforce strict pipeline execution, passing shared context between agents to ensure predictable data flow. Parallel routers manage concurrent fan-out operations—essential for reducing latency during independent multi-source data retrieval—before gathering results into a shared session state. Loop routers orchestrate iterative refinement, executing Generator-Critic patterns until a specific termination condition is met to prevent infinite recursion.

### V-FVerification and Self-Correction Modules

Agentic systems are inherently susceptible to cascading reasoning failures. In a multi-step workflow, a minor hallucination or incorrect tool invocation early in the execution graph can propagate, leading to systemic failure. Therefore, robust Verification and Self-Correction Modules must be integrated directly into the iterative loop to provide runtime supervision, reflection, and rigorous output validation.

These modules function by establishing a closed-loop Perception-Planning-Action-Reflection (PPAR) cycle. As illustrated in Figure [5](https://arxiv.org/html/2603.07379v1#S5.F5 "Figure 5 ‣ V-F Verification and Self-Correction Modules ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), when the Reasoning Engine proposes a solution, it is first evaluated by a separate verification agent or internal critic. Domain-specific standalone agents illustrate that systems cannot rely solely on simple LLM self-reflection, as models suffer from evaluation blind spots \[ [36](https://arxiv.org/html/2603.07379v1#bib.bib49 "Towards llm-powered verilog rtl assistant: self-verification and self-correction")\]. Instead, self-verification relies on empirical testing, such as iterative simulation against ground-truth constraints \[ [36](https://arxiv.org/html/2603.07379v1#bib.bib49 "Towards llm-powered verilog rtl assistant: self-verification and self-correction")\].

If the verification module detects a factual inconsistency or syntax error, it generates structured feedback detailing the failure state. The Reasoning Engine incorporates this feedback to iteratively adjust the query formulation or switch retrieval strategies until the output passes all validation constraints. In scenarios where self-correction fails to converge, the Verification module triggers an escalation path through Human-in-the-Loop (HITL) intervention. Operating through policy engines, the module intercepts tool calls that violate guardrails, pausing execution for human approval.

![Refer to caption](https://arxiv.org/html/2603.07379v1/diagrams/PPAR_Verification_Loop_with_HITL.png)Figure 5: The closed-loop Perception-Planning-Action-Reflection (PPAR) cycle with Human-in-the-Loop (HITL) escalation. This demonstrates the structural necessity of verification loops: outputs failing constraint checks are returned as structured feedback, and unresolvable loops are escalated to prevent autonomous hallucination.

This architectural decomposition isolates the core modules—planner, retriever, memory controller, and execution interface—that enable iterative reasoning and adaptive retrieval. By abstracting these components from specific implementations, we provide a systems-level blueprint for agentic orchestration. The subsequent section builds upon this modular foundation to identify recurring design patterns that emerge across implementations.

## VI Design Patterns in Agentic RAG

Building on the architectural module decomposition established in Section [V](https://arxiv.org/html/2603.07379v1#S5 "V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), this section abstracts away from specific implementations to identify reusable control-flow strategies. These design patterns specify how planning, retrieval, generation, verification, and memory updates are sequenced and iterated under a control policy \[ [91](https://arxiv.org/html/2603.07379v1#bib.bib33 "Workflow patterns: on the expressive power of petri-net-based workflow languages")\]. As illustrated in Figure [6](https://arxiv.org/html/2603.07379v1#S6.F6 "Figure 6 ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), these patterns operate as engineering-level motifs that can be combined and composed to dictate the operational tempo of the agent \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\].

![Refer to caption](https://arxiv.org/html/2603.07379v1/diagrams/Section-6-top-to-bottom.png)Figure 6: Control-flow map demonstrating how Agentic RAG systems compose design patterns through explicit decisions over task decomposition, retrieval timing, iterative refinement, and orchestration. This structural mapping highlights the transition from linear pipelines to cyclic loops.

### VI-APlan-Then-Retrieve Pattern

This pattern explicitly separates task decomposition from execution. The agent first produces a high-level plan or sub-question list, then performs retrieval conditioned on each step before composing a final answer \[ [95](https://arxiv.org/html/2603.07379v1#bib.bib17 "Plan-and-solve prompting: improving zero-shot chain-of-thought reasoning by large language models"), [78](https://arxiv.org/html/2603.07379v1#bib.bib15 "Measuring and narrowing the compositionality gap in language models")\].

- •


Control Flow: (i) Plan/decompose →\\rightarrow (ii) retrieve evidence per subtask →\\rightarrow (iii) generate intermediate notes →\\rightarrow (iv) synthesize final answer \[ [64](https://arxiv.org/html/2603.07379v1#bib.bib29 "Multi-hop reading comprehension through question decomposition and rescoring")\].

- •


Strengths: Makes information needs explicit and significantly improves compositional generalization in multi-step tasks \[ [116](https://arxiv.org/html/2603.07379v1#bib.bib16 "Least-to-most prompting enables complex reasoning in large language models")\].

- •


Limitations: Decomposition quality is critical; if the initial plan is flawed or ambiguous, the entire subsequent retrieval trajectory fails \[ [64](https://arxiv.org/html/2603.07379v1#bib.bib29 "Multi-hop reading comprehension through question decomposition and rescoring")\].

- •


Typical Use Cases: Multi-hop QA where evidence requirements can be enumerated in advance (e.g., HotpotQA) \[ [106](https://arxiv.org/html/2603.07379v1#bib.bib30 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")\].

- •


Failure Modes: Hallucinating an unsolvable sub-question or failing to dynamically adjust the plan when newly retrieved evidence contradicts the initial premise.

- •


Cost/Latency Implications: High upfront token cost for planning, but retrievals can often be parallelized to optimize wall-clock latency.


### VI-BRetrieve-Reflect-Refine Pattern

The agent alternates retrieval and generation with explicit reflection steps to decide if retrieved evidence is sufficient, and refines subsequent actions (e.g., query rewriting, retrieval gating) accordingly \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\]. Recent work such as A-RAG \[ [19](https://arxiv.org/html/2603.07379v1#bib.bib35 "A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces")\] introduces hierarchical retrieval interfaces that allow agents to progressively refine context acquisition through staged document exploration, improving token efficiency and retrieval relevance.

- •


Control Flow: (i) Retrieve →\\rightarrow (ii) draft partial answer →\\rightarrow (iii) reflect on document utility →\\rightarrow (iv) refine query →\\rightarrow repeat until stop \[ [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\].

- •


Strengths: Improves factuality and citation accuracy by establishing a “retrieval-on-demand” critique signal rather than blindly passing context \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\].

- •


Limitations: Relies heavily on the LLM’s inherent self-critique capabilities, which can suffer from evaluation blind spots or over-confidence.

- •


Typical Use Cases: Long-form attributed generation and open-domain QA where initial retrieval is typically imperfect \[ [58](https://arxiv.org/html/2603.07379v1#bib.bib31 "Query rewriting for retrieval-augmented large language models")\].

- •


Failure Modes: Infinite loops where the agent repeatedly refines a query but retrieves the same unhelpful documents.

- •


Cost/Latency Implications: Introduces sequential iterations that compound latency and increase compute overhead, motivating budget-aware gating mechanisms \[ [13](https://arxiv.org/html/2603.07379v1#bib.bib12 "Unified active retrieval for retrieval augmented generation"), [41](https://arxiv.org/html/2603.07379v1#bib.bib11 "Active retrieval augmented generation")\].


### VI-CDecomposition-Based Retrieval Pattern

Rather than producing a full plan upfront, the agent decomposes the query implicitly through stepwise reasoning, triggering retrieval mid-trajectory based on evolving hypotheses \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions"), [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\]. Emerging approaches such as DLLM-Searcher \[ [112](https://arxiv.org/html/2603.07379v1#bib.bib115 "DLLM-searcher: diffusion large language models for search and reasoning")\] explore diffusion-based language models to parallelize reasoning trajectories, reducing latency while maintaining diverse search exploration.

- •


Control Flow: (i) Generate reasoning step →\\rightarrow (ii) formulate retrieval action →\\rightarrow (iii) incorporate observation →\\rightarrow repeat \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\].

- •


Strengths: Highly adaptable; allows the system to discover the next information need based on partial inference, mimicking human investigative behavior \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\].

- •


Limitations: The repeated interleaving of reasoning and tool calls creates highly redundant prompt prefixes \[ [101](https://arxiv.org/html/2603.07379v1#bib.bib18 "ReWOO: decoupling reasoning from observations for efficient augmented language models")\].

- •


Typical Use Cases: Complex investigative tasks where subsequent logical steps are entirely dependent on the specific facts uncovered in the previous step \[ [106](https://arxiv.org/html/2603.07379v1#bib.bib30 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")\].

- •


Failure Modes: Reasoning drift, where the agent forgets the original objective after a long sequence of intermediate observations.

- •


Cost/Latency Implications: Extremely expensive computationally due to repeated prompt accumulation and sequential bottlenecking \[ [101](https://arxiv.org/html/2603.07379v1#bib.bib18 "ReWOO: decoupling reasoning from observations for efficient augmented language models")\].


### VI-DTool-Augmented Retrieval Loop Pattern

Retrieval is treated as just one tool among many (e.g., calculators, code execution, SQL). The agent dynamically chooses among these heterogeneous tools in an iterative loop to update its state \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\].

- •


Control Flow: (i) Decide next tool →\\rightarrow (ii) execute tool →\\rightarrow (iii) process observation →\\rightarrow (iv) update state →\\rightarrow repeat \[ [69](https://arxiv.org/html/2603.07379v1#bib.bib8 "WebGPT: browser-assisted question-answering with human feedback")\].

- •


Strengths: Enables massive zero-shot generalization across domains requiring distinct modalities (math, search, code) while preserving core modeling ability \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools"), [31](https://arxiv.org/html/2603.07379v1#bib.bib19 "CRITIC: large language models can self-correct with tool-interactive critiquing")\].

- •


Limitations: Tool routing reliability becomes a first-class failure point; agents frequently struggle with strict syntax formatting for complex APIs \[ [43](https://arxiv.org/html/2603.07379v1#bib.bib7 "MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning")\].

- •


Typical Use Cases: Broad knowledge-intensive tasks requiring non-textual computation or interaction with structured databases \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\].

- •


Failure Modes: Tool hallucination (inventing non-existent APIs) or failure to recover gracefully when an API returns an unexpected error code \[ [101](https://arxiv.org/html/2603.07379v1#bib.bib18 "ReWOO: decoupling reasoning from observations for efficient augmented language models")\].

- •


Cost/Latency Implications: Variable cost depending heavily on the latency of the external APIs invoked.


### VI-EMulti-Agent Collaboration Pattern

Multiple LLM-driven agents coordinate through structured interaction protocols (e.g., debate, role specialization) to divide labor across retrieval, reasoning, and verification \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation"), [52](https://arxiv.org/html/2603.07379v1#bib.bib26 "CAMEL: communicative agents for ”mind” exploration of large language model society")\].

- •


Control Flow: (i) Assign roles →\\rightarrow (ii) iterative message passing →\\rightarrow (iii) integrate artifacts into final synthesis \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation")\].

- •


Strengths: Specialization reduces cognitive load per agent and enables peer-review mechanisms (e.g., communicative dehallucination) \[ [79](https://arxiv.org/html/2603.07379v1#bib.bib28 "ChatDev: communicative agents for software development"), [35](https://arxiv.org/html/2603.07379v1#bib.bib27 "MetaGPT: meta programming for a multi-agent collaborative framework")\].

- •


Limitations: High risk of coordination overhead, infinite debates, or consensus forming around an incorrect premise (groupthink).

- •


Typical Use Cases: Long-horizon workflows like software engineering or exhaustive legal research where task decomposition by distinct roles is natural \[ [79](https://arxiv.org/html/2603.07379v1#bib.bib28 "ChatDev: communicative agents for software development")\].

- •


Failure Modes: Cascading hallucinations if the verifying agent is too permissive of the retrieving agent’s claims \[ [35](https://arxiv.org/html/2603.07379v1#bib.bib27 "MetaGPT: meta programming for a multi-agent collaborative framework")\].

- •


Cost/Latency Implications: Highest token amplification profile; cross-agent communication aggressively consumes token budgets.


### VI-FRetrieval-Grounded Self-Verification Pattern

The agent treats verification as a dedicated, first-class execution stage, retrieving evidence specifically to validate, refute, and attribute claims made in a draft response \[ [18](https://arxiv.org/html/2603.07379v1#bib.bib20 "Chain-of-verification reduces hallucination in large language models"), [31](https://arxiv.org/html/2603.07379v1#bib.bib19 "CRITIC: large language models can self-correct with tool-interactive critiquing")\]. Systems such as Search-R2 \[ [53](https://arxiv.org/html/2603.07379v1#bib.bib114 "Search-r2: search-augmented reasoning and refinement for large language models")\] propose actor–refiner architectures that iteratively repair reasoning trajectories through retrieval-augmented refinement, illustrating how verification modules can be integrated directly into agentic search policies.

- •


Control Flow: (i) Draft answer →\\rightarrow (ii) extract checkable claims →\\rightarrow (iii) retrieve evidence per claim →\\rightarrow (iv) revise and attach citations \[ [18](https://arxiv.org/html/2603.07379v1#bib.bib20 "Chain-of-verification reduces hallucination in large language models")\].

- •


Strengths: Directly reduces hallucination and provides highly auditable, attributable outputs supported by verified quotes \[ [62](https://arxiv.org/html/2603.07379v1#bib.bib21 "Teaching language models to support answers with verified quotes")\].

- •


Limitations: Verification quality is ultimately bounded by the retriever’s recall; it cannot correct a claim if the grounding truth is missing from the corpus \[ [8](https://arxiv.org/html/2603.07379v1#bib.bib23 "Attributed question answering: evaluation and modeling for attributed large language models")\].

- •


Typical Use Cases: Medical, legal, and compliance domains requiring strict auditability and traceable evidence \[ [26](https://arxiv.org/html/2603.07379v1#bib.bib22 "Enabling large language models to generate text with citations")\].

- •


Failure Modes: The agent forcibly misaligns generated claims with irrelevant evidence to satisfy a formatting requirement (false attribution).

- •


Cost/Latency Implications: Effectively doubles the generation latency, as the system must complete an initial draft before the verification phase even begins.


### VI-GHuman-As-A-Tool (HITL) Pattern

This pattern models human oversight as a callable API within the action space. When epistemic uncertainty exceeds a defined threshold, the policy pauses execution to request disambiguation or supervision \[ [69](https://arxiv.org/html/2603.07379v1#bib.bib8 "WebGPT: browser-assisted question-answering with human feedback"), [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation")\].

- •


Control Flow: (i) Execute loop →\\rightarrow (ii) detect ambiguity/risk threshold →\\rightarrow (iii) pause for human input →\\rightarrow (iv) resume execution with human observation \[ [86](https://arxiv.org/html/2603.07379v1#bib.bib9 "Reflexion: language agents with verbal reinforcement learning")\].

- •


Strengths: Guarantees safety in high-stakes environments and strictly enforces evidence discipline via human feedback \[ [69](https://arxiv.org/html/2603.07379v1#bib.bib8 "WebGPT: browser-assisted question-answering with human feedback")\].

- •


Limitations: Fundamentally breaks continuous system autonomy and creates operational bottlenecks.

- •


Typical Use Cases: High-stakes financial, medical, or administrative tasks where automated retrieval is inadequate and strict compliance oversight is mandatory.

- •


Failure Modes: Human fatigue leading to rubber-stamping, or poorly calibrated uncertainty thresholds causing excessive system interruptions.

- •


Cost/Latency Implications: Negligible API cost, but introduces extreme wall-clock latency that halts the automated execution loop entirely \[ [13](https://arxiv.org/html/2603.07379v1#bib.bib12 "Unified active retrieval for retrieval augmented generation")\].


As synthesized in Table [VI](https://arxiv.org/html/2603.07379v1#S6.T6 "TABLE VI ‣ VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), these patterns are not mutually exclusive. Robust systems frequently combine them, overlaying Human-in-the-Loop escalation rules on top of Multi-Agent Collaboration loops to balance autonomy with oversight.

TABLE VI: Comparison of Core Agentic RAG Design Patterns

| Design Pattern | Core Control Question | Termination Condition | Tradeoffs (Cost / Latency / Risk) | Representative Anchors |
| --- | --- | --- | --- | --- |
| Plan-then-retrieve | “What subtasks must be answered before synthesis?” | All planned sub-questions answered | High upfront planning cost; risk of brittle initial plans | Self-Ask \[ [78](https://arxiv.org/html/2603.07379v1#bib.bib15 "Measuring and narrowing the compositionality gap in language models")\], Plan-and-Solve \[ [95](https://arxiv.org/html/2603.07379v1#bib.bib17 "Plan-and-solve prompting: improving zero-shot chain-of-thought reasoning by large language models")\] |
| Retrieve-reflect-refine | “Is retrieval needed? Are these passages relevant?” | Reflection indicates sufficiency or budget exhausted | High latency due to sequential query iterations | Self-RAG \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\], Iter-RetGen \[ [82](https://arxiv.org/html/2603.07379v1#bib.bib13 "Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy")\] |
| Decomp-based retrieval | “Given the current reasoning state, what is missing?” | Answer reached with adequate evidence | Extreme token accumulation; reasoning drift risk | IRCoT \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\], ReAct \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\] |
| Tool-augmented loops | “Which heterogeneous tool to call now?” | Tool results stabilize answer or verifier halts | Variable latency; high risk of tool-syntax failure | Toolformer \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\], CRITIC \[ [31](https://arxiv.org/html/2603.07379v1#bib.bib19 "CRITIC: large language models can self-correct with tool-interactive critiquing")\] |
| Multi-agent collaboration | “Which agent role should handle this task?” | Cross-agent consensus reached | Massive token amplification; coordination overhead | AutoGen \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation")\], MetaGPT \[ [35](https://arxiv.org/html/2603.07379v1#bib.bib27 "MetaGPT: meta programming for a multi-agent collaborative framework")\] |
| Self-verification | “Which claims require checking against the corpus?” | Verification passes or abstention is triggered | Doubles baseline latency; bounded by retriever recall | CoVe \[ [18](https://arxiv.org/html/2603.07379v1#bib.bib20 "Chain-of-verification reduces hallucination in large language models")\], GopherCite \[ [62](https://arxiv.org/html/2603.07379v1#bib.bib21 "Teaching language models to support answers with verified quotes")\] |
| Human-as-a-tool | “Is human input required for disambiguation?” | Human resolves uncertainty and resumes loop | Extreme wall-clock latency; guarantees safety | WebGPT \[ [69](https://arxiv.org/html/2603.07379v1#bib.bib8 "WebGPT: browser-assisted question-answering with human feedback")\], AutoGen \[ [99](https://arxiv.org/html/2603.07379v1#bib.bib25 "AutoGen: enabling next-gen llm applications via multi-agent conversation")\] |

The design patterns identified here reflect recurring control-flow strategies that govern how agentic systems plan, retrieve, and adapt. These patterns highlight trade-offs between autonomy, stability, and computational overhead. However, architectural sophistication alone does not guarantee reliability. The next section examines how such systems should be evaluated beyond static accuracy metrics.

## VII Evaluation and Benchmarking

Despite the growing deployment of agentic RAG systems, current evaluation methodologies largely remain inherited from traditional retrieval or language generation tasks. These approaches primarily focus on final answer quality and fail to capture the multi-step reasoning, tool interaction, and decision dependencies that characterize agentic systems. As a result, commonly used benchmarks may obscure critical failure modes and provide incomplete signals about system reliability. This section therefore examines the limitations of existing evaluation practices and outlines a structured framework for assessing agentic RAG behavior.

Standard generation metrics were originally designed for static, single-turn text generation tasks and fail to capture the interactive and iterative behavior of agentic systems \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey"), [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents")\]. While traditional metrics evaluate the ”engine” (the LLM’s terminal text output), agentic evaluation must assess the ”car” (the entire system’s behavior across planning, tool use, and environment interaction) \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\].

Traditional metrics like BLEU or ROUGE focus on lexical overlap rather than semantic truth or reasoning trajectories. Consequently, they are incapable of distinguishing between a correct final answer reached through flawed logic and one reached through valid planning \[ [61](https://arxiv.org/html/2603.07379v1#bib.bib80 "A review of faithfulness metrics for hallucination assessment in large language models"), [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models"), [117](https://arxiv.org/html/2603.07379v1#bib.bib82 "RAGEval: scenario specific RAG evaluation dataset generation framework")\]. To highlight these inadequacies, Table [VII](https://arxiv.org/html/2603.07379v1#S7.T7 "TABLE VII ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") synthesizes a Metric Failure Analysis, demonstrating exactly how and why static metrics break down when applied to autonomous multi-step architectures.

TABLE VII: Metric Failure Analysis: Why Standard Evaluation Fails for Agentic RAG

| Metric | Failure Dimension | Why It Fails Agentic Systems | Agentic Failure Case |
| --- | --- | --- | --- |
| BLEU / ROUGE | Lexical Rigidity | Primarily measures surface-level lexical overlap; ignores semantic consistency and factual keypoints \[ [61](https://arxiv.org/html/2603.07379v1#bib.bib80 "A review of faithfulness metrics for hallucination assessment in large language models")\]. | An agent correctly diagnoses a condition but uses synonyms not in the reference text, receiving a failing score despite factual accuracy \[ [100](https://arxiv.org/html/2603.07379v1#bib.bib83 "Benchmarking retrieval-augmented generation for medicine")\]. |
| Exact Match (EM) | Binary Inflexibility | Offers no flexibility for valid aliases or the superfluous reasoning detail often generated by agents \[ [61](https://arxiv.org/html/2603.07379v1#bib.bib80 "A review of faithfulness metrics for hallucination assessment in large language models")\]. | An agent outputs the correct entity but is failed because it included a valid reasoning trace before the target word \[ [61](https://arxiv.org/html/2603.07379v1#bib.bib80 "A review of faithfulness metrics for hallucination assessment in large language models")\]. |
| Final-Answer Accuracy | Trajectory Blindness | Provides a ”black box” view; cannot determine if the agent correctly reasoned or merely guessed \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. | A math agent reaches the correct final digit through mutually canceling calculation errors, hiding a fundamental planning breakdown \[ [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents")\]. |
| Success Rate (SR) | Credit Assignment | Non-diagnostic; identifies that a failure occurred but fails to pinpoint the bottleneck (retrieval vs. tool call) \[ [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents")\]. | An agent correctly writes code but fails execution due to a syntax timeout; SR marks it 0, obscuring the successful reasoning \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. |
| Pass@k | Reliability Blindness | Focuses on best-case capability rather than the consistency required for enterprise deployment \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\]. | An agent succeeds once in ten attempts; while technically ”capable,” it is dangerously unreliable for production tasks \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\]. |

To quantify the efficiency and correctness of these intermediate steps, agentic evaluation relies on specific trajectory-level metrics:

Progress Rate (PR).
Progress Rate measures the fraction of reasoning steps that meaningfully advance task completion:

|     |     |     |
| --- | --- | --- |
|  | P​R=Number of successful reasoning stepsTotal reasoning stepsPR=\\frac{\\text{Number of successful reasoning steps}}{\\text{Total reasoning steps}} |  |

Effective Information Rate (EIR).
Effective Information Rate measures the efficiency of retrieved information used during reasoning:

|     |     |     |
| --- | --- | --- |
|  | E​I​R=Useful retrieved tokensTotal retrieved tokensEIR=\\frac{\\text{Useful retrieved tokens}}{\\text{Total retrieved tokens}} |  |

Higher EIR indicates that the retrieval subsystem provides more relevant information relative to the overall retrieval volume.

### VII-AEvaluation Dimensions for Agentic RAG

To move beyond the limitations of static metrics, evaluation must be decomposed into specific behavioral dimensions that capture the lifecycle of an agentic decision \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\].

- •


Faithfulness: The degree to which a generated response remains strictly aligned with the retrieved context, even when that context contradicts the model’s pre-trained priors \[ [61](https://arxiv.org/html/2603.07379v1#bib.bib80 "A review of faithfulness metrics for hallucination assessment in large language models")\]. Evaluation utilizes frameworks like TRACe (Adherence) and Natural Language Inference (NLI) to detect hallucinations across noisy or counterfactual contexts \[ [23](https://arxiv.org/html/2603.07379v1#bib.bib85 "RAGBench: explainable benchmark for retrieval-augmented generation systems"), [65](https://arxiv.org/html/2603.07379v1#bib.bib84 "FaithEval: can your language model stay faithful to context, even if “the moon is made of marshmallows”")\].

- •


Iterative Reasoning Quality: Evaluates the ”thinking” process connecting retrieval to action \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. Methods like Reasoning Via Planning (RAP) audit the logical steps, while metrics like Progress Rate measure how effectively an agent advances toward a goal across multiple turns, emphasizing intra-test-time self-correction \[ [16](https://arxiv.org/html/2603.07379v1#bib.bib87 "GAMEBENCH: evaluating strategic reasoning abilities of LLM agents"), [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\].

- •


Retrieval Efficiency: Measures autonomous decision-making regarding when, what, and how to retrieve \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. Core metrics include Context Relevance (fraction of useful documents) and Effective Information Rate (EIR), which specifically penalize the system for context overloading and the ”lost-in-the-middle” effect \[ [23](https://arxiv.org/html/2603.07379v1#bib.bib85 "RAGBench: explainable benchmark for retrieval-augmented generation systems"), [117](https://arxiv.org/html/2603.07379v1#bib.bib82 "RAGEval: scenario specific RAG evaluation dataset generation framework")\].

- •


Tool Reliability: Assesses if an agent can correctly reason about when a tool is needed, select the right one, and provide correct parameters \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\]. Advanced evaluation bypasses static syntax checks in favor of execution-based assessment, where tool calls are run in sandboxes to verify outcomes \[ [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents")\].

- •


Robustness: Evaluates worst-case stability. This includes Noise Robustness (extracting answers from distracting context), Negative Rejection (declining to answer when context is absent), and Adaptive Resilience (recovering when environmental structures change mid-task) \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey"), [10](https://arxiv.org/html/2603.07379v1#bib.bib86 "Benchmarking large language models in retrieval-augmented generation")\].


### VII-BFrom Static Benchmarks to Evaluation Frameworks

Existing benchmarks for RAG focus heavily on static, one-shot evaluation \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. To prevent the mere listing of leaderboards, Table [VIII](https://arxiv.org/html/2603.07379v1#S7.T8 "TABLE VIII ‣ VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") converts the current fragmented benchmarking landscape into a synthesis of target capabilities and their remaining agentic limitations. While frameworks like RGB \[ [10](https://arxiv.org/html/2603.07379v1#bib.bib86 "Benchmarking large language models in retrieval-augmented generation")\], RAGBench \[ [23](https://arxiv.org/html/2603.07379v1#bib.bib85 "RAGBench: explainable benchmark for retrieval-augmented generation systems")\], and RAGEval \[ [117](https://arxiv.org/html/2603.07379v1#bib.bib82 "RAGEval: scenario specific RAG evaluation dataset generation framework")\] provide excellent component-level stress tests for noise and faithfulness, they fundamentally lack the capacity to assess long-horizon trajectory evaluation and dynamic tool invocation \[ [100](https://arxiv.org/html/2603.07379v1#bib.bib83 "Benchmarking retrieval-augmented generation for medicine"), [65](https://arxiv.org/html/2603.07379v1#bib.bib84 "FaithEval: can your language model stay faithful to context, even if “the moon is made of marshmallows”")\].

Recent frameworks such as DRACO \[ [11](https://arxiv.org/html/2603.07379v1#bib.bib116 "DRACO: diagnostic reasoning for comprehensive agent evaluation")\] and CL-Bench \[ [93](https://arxiv.org/html/2603.07379v1#bib.bib117 "CL-bench: a contamination-aware context learning benchmark for rag")\] advocate rubric-based multi-criteria evaluation and contamination-aware context learning benchmarks, aligning with trajectory-level and faithfulness-oriented evaluation goals.

TABLE VIII: Synthesis of Current RAG Evaluation Frameworks and Agentic Limitations

| Evaluation Framework | Targeted Capability | Limitation for Agentic RAG |
| --- | --- | --- |
| RGB & FaithEval\[ [10](https://arxiv.org/html/2603.07379v1#bib.bib86 "Benchmarking large language models in retrieval-augmented generation"), [65](https://arxiv.org/html/2603.07379v1#bib.bib84 "FaithEval: can your language model stay faithful to context, even if “the moon is made of marshmallows”")\] | Noise robustness, negative rejection, and counterfactual adherence. | Assumes a single forward-pass; cannot evaluate dynamic query reformulation. |
| RAGBench (TRACe)\[ [23](https://arxiv.org/html/2603.07379v1#bib.bib85 "RAGBench: explainable benchmark for retrieval-augmented generation systems")\] | uTilization, Relevance, Adherence, and Completeness across industries. | Static dataset; fails to capture multi-step tool use or environment interaction. |
| RAGEval & CRAG\[ [117](https://arxiv.org/html/2603.07379v1#bib.bib82 "RAGEval: scenario specific RAG evaluation dataset generation framework")\] | Keypoint-based factual accuracy and multi-hop reasoning coverage. | Evaluates final output via mock APIs but lacks metrics for reasoning efficiency or cost. |

### VII-CToward a Structured Agentic Evaluation Pipeline

Because Agentic RAG systems exhibit iterative reasoning, tool interaction, and memory usage, evaluation must operate at multiple scopes of measurement \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\]. As illustrated in Figure [7](https://arxiv.org/html/2603.07379v1#S7.F7 "Figure 7 ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), we abstract these into a structured three-layer evaluation pipeline that moves from atomic actions to holistic system utility.

![Refer to caption](https://arxiv.org/html/2603.07379v1/figures/eval_pipeline.png)Figure 7: The Agentic RAG Evaluation Pipeline. This framework demonstrates the necessary structural shift from terminal output scoring to multi-layered assessment, capturing component-level tool accuracy, trajectory-level reasoning coherence, and system-level outcome fidelity.

#### VII-C1 Layer 1: Component-Level Assessment

Isolates individual primitives to assess localized correctness before considering their interaction over time \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. This includes evaluating the Planner (task decomposition), the Retriever (recall precision), and the Tool Executor (invocation accuracy and parameter F1 scores) \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\]. It captures localized failure modes without conflating them with downstream reasoning errors.

#### VII-C2 Layer 2: Trajectory-Level Coherence

Examines how atomic actions compose into coherent reasoning sequences across interaction steps \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. This layer tracks logical progression, adaptation to intermediate API responses, and memory consistency \[ [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents")\]. Metrics include Progress Rate and step-success ratios, capturing failure modes that static metrics overlook, such as compounding errors and infinite execution loops \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\].

#### VII-C3 Layer 3: System-Level Outcome

Treats the agentic pipeline holistically, focusing on deployment-relevant properties \[ [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. At this scope, evaluation abstracts away internal structure to assess final task completion, cross-agent coordination effectiveness, and output faithfulness \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey"), [65](https://arxiv.org/html/2603.07379v1#bib.bib84 "FaithEval: can your language model stay faithful to context, even if “the moon is made of marshmallows”")\]. Crucially, this layer must also incorporate Cost and Latency Awareness, measuring token amplification and Time-To-First-Token (TTFT) to ensure the system is economically viable for real-world deployment \[ [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents")\].

### VII-DSystemic Evaluation Gaps

Despite the layered framework proposed above, significant systemic gaps remain in the current literature. First, the reliance on LLM-as-a-judge methodologies creates a reproducibility crisis. While automated judges correlate with humans, they are highly sensitive to prompt sequencing and exhibit ”sycophantic” biases toward their own generated output patterns, making stable baseline comparisons difficult as frontier models evolve \[ [61](https://arxiv.org/html/2603.07379v1#bib.bib80 "A review of faithfulness metrics for hallucination assessment in large language models"), [117](https://arxiv.org/html/2603.07379v1#bib.bib82 "RAGEval: scenario specific RAG evaluation dataset generation framework")\].

Second, the field lacks standardized mechanisms for credit assignment. Current evaluations treat agents as black boxes, providing a single score that fails to pinpoint whether a failure occurred during planning, retrieval, or final synthesis \[ [109](https://arxiv.org/html/2603.07379v1#bib.bib79 "Survey on evaluation of LLM-based agents"), [98](https://arxiv.org/html/2603.07379v1#bib.bib81 "Agentic reasoning for large language models")\]. Finally, methods for evaluating an agent’s ability to maintain persistent state and episodic memory across long-horizon conversations (e.g., hundreds of turns) remain highly underdeveloped, leaving critical deployment realities untested \[ [67](https://arxiv.org/html/2603.07379v1#bib.bib78 "Evaluation and benchmarking of LLM agents: a survey")\].

Traditional static metrics such as BLEU and ROUGE fail to capture multi-step reasoning consistency, adaptive retrieval quality, and tool invocation correctness. Agentic RAG requires evaluation at the trajectory and policy levels rather than isolated output comparison. With this evaluation foundation established, the following section examines how these systems are instantiated within industrial frameworks and real-world deployments.

## VIII Industry Frameworks and Real-World Systems

The transition of Agentic RAG from academic prototype to production exposes how theoretical architectures are operationalized in practice. By embedding autonomy, iterative retrieval, and verifiable execution into enterprise workflows, industrial systems attempt to overcome the accuracy limitations of static generative models. This section evaluates the deployment of Agentic RAG across specialized domains, analyzes the orchestration frameworks that abstract these architectures, and details the systemic constraints of production deployment.

### VIII-ADomain-Specific Implementations

In enterprise environments, proprietary data is heavily fragmented across secure document stores and specialized databases. Static RAG pipelines struggle with these domain-specific ontologies and access controls. Agentic architectures address this by utilizing multi-hop planning to fuse cross-document information. For example, systems like TURA (Tool-Augmented Unified Retrieval Agent) implement Directed Acyclic Graph (DAG) based planning to handle transactional financial data \[ [113](https://arxiv.org/html/2603.07379v1#bib.bib42 "TURA: tool-augmented unified retrieval agent for ai search")\]. By modeling sub-tasks and data dependencies as a DAG, TURA orchestrates reasoning chains across both static documents and dynamic APIs, enforcing strict access governance during execution \[ [113](https://arxiv.org/html/2603.07379v1#bib.bib42 "TURA: tool-augmented unified retrieval agent for ai search")\]. Furthermore, because retrieving and embedding sensitive enterprise records directly into the generation context introduces severe information leakage vulnerabilities, deploying these systems safely increasingly requires differentially private in-context learning frameworks \[ [7](https://arxiv.org/html/2603.07379v1#bib.bib122 "Privacy preserving in-context-learning framework for large language models")\]. To further enforce strict access governance, future enterprise agents could integrate visual authentication models such as deep learning-based masked facial recognition \[ [66](https://arxiv.org/html/2603.07379v1#bib.bib118 "A face recognition method using deep learning to identify mask and unmask objects")\] as a prerequisite tool call before accessing sensitive records.

Scientific research requires a different architectural emphasis: rigorous attribution and verifiable citation traces. Systems like PaperQA2 mitigate hallucination by treating the literature corpus as an interactive environment \[ [88](https://arxiv.org/html/2603.07379v1#bib.bib41 "Language agents achieve superhuman synthesis of scientific knowledge")\]. Rather than executing a single vector search, the agent uses a multi-phase loop: it generates targeted search queries, retrieves candidate chunks, and applies LLM-based Contextual Summarization to score evidence before generation \[ [88](https://arxiv.org/html/2603.07379v1#bib.bib41 "Language agents achieve superhuman synthesis of scientific knowledge")\]. The agent employs citation traversal tools to verify the provenance of its claims, demonstrating how hierarchical retrieval interfaces isolate and evaluate evidence systematically.

Software engineering represents a highly complex embodied environment where agents must autonomously explore repositories, run diagnostic tests, and parse compilation logs \[ [105](https://arxiv.org/html/2603.07379v1#bib.bib40 "SWE-agent: agent-computer interfaces enable automated software engineering")\]. The SWE-agent framework operationalizes this by providing an Agent-Computer Interface (ACI) to isolate and execute codebase operations safely \[ [105](https://arxiv.org/html/2603.07379v1#bib.bib40 "SWE-agent: agent-computer interfaces enable automated software engineering")\]. Instead of attempting full-file overwrites—which exhaust context windows—the agent uses targeted diff patching and dynamic exploration \[ [105](https://arxiv.org/html/2603.07379v1#bib.bib40 "SWE-agent: agent-computer interfaces enable automated software engineering")\]. This couples dynamic code retrieval with iterative execution feedback, allowing the agent to organically debug and self-improve through grounded environmental interactions.

### VIII-BIndustrial Orchestration Frameworks

The transition from bespoke academic prototypes to scalable enterprise applications is facilitated by orchestration frameworks. These platforms abstract memory management, tool integration, and control loops, providing the routing primitives necessary to engineer complex agentic topologies \[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\].

Rather than hardcoding API payloads, developers utilize these frameworks to define architectural boundaries. For instance, LangGraph abstracts stateful, cyclic orchestration by modeling agent interactions as a directed graph, providing fine-grained control over state persistence and reflection loops \[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\]. Conversely, frameworks like Google’s Agent Development Kit (ADK) provide hierarchical routing primitives \[ [29](https://arxiv.org/html/2603.07379v1#bib.bib48 "Agent development kit (adk)")\]. ADK orchestrates non-deterministic LLM agents using deterministic structural routers, leveraging the Model Context Protocol (MCP) to standardize external tool interfaces and ensure environment-agnostic deployment \[ [29](https://arxiv.org/html/2603.07379v1#bib.bib48 "Agent development kit (adk)")\]. However, while MCP solves critical interoperability challenges by decoupling context from execution, securing these interfaces against adversarial tool poisoning and prompt injection remains a profound systemic challenge \[ [24](https://arxiv.org/html/2603.07379v1#bib.bib119 "Systematization of knowledge: security and safety in the model context protocol ecosystem")\].

Other frameworks optimize for distinct control-flow paradigms. AutoGen implements an asynchronous, event-driven chat interface for conversational multi-agent coordination \[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\]. CrewAI implements process-driven sequential routing, optimizing for defined hand-offs and role-based division of labor \[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\]. LlamaIndex, originally a static ingestion pipeline, now provides abstract query pipelines and index-centric memory routing \[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\]. Table [IX](https://arxiv.org/html/2603.07379v1#S8.T9 "TABLE IX ‣ VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") synthesizes how these industrial frameworks operationalize the core architectural modules (Planner, Controller, Memory, Orchestrator) defined in Section [V](https://arxiv.org/html/2603.07379v1#S5 "V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

TABLE IX: Mapping Industrial Frameworks to Agentic RAG Architectural Modules

| Framework | Orchestrator Model | Planner / Control Flow | Memory Routing | Tool Abstraction |
| --- | --- | --- | --- | --- |
| LangGraph\[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\] | Cyclic Directed Graphs | State-machine nodes | Persistent checkpointing | Wrapped Python functions |
| Google ADK\[ [29](https://arxiv.org/html/2603.07379v1#bib.bib48 "Agent development kit (adk)")\] | Hierarchical Composition | Deterministic routing loops | Shared contextual state | Model Context Protocol |
| CrewAI\[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\] | Role-based Sequential | Process-driven delegation | Structured persona memory | Assigned capability arrays |
| AutoGen\[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\] | Asynchronous Chat | Event-driven conversation | Message history logs | Executable code blocks |
| LlamaIndex\[ [3](https://arxiv.org/html/2603.07379v1#bib.bib52 "From prompt–response to goal-directed systems: the evolution of agentic ai software architecture")\] | Query Pipelines | Data-driven routing | Index-centric retrieval | LlamaPack interfaces |

### VIII-CDeployment Implications and the Research Gap

Deploying these frameworks exposes operational bottlenecks rarely encountered in isolated academic benchmarks. The most critical constraint is latency stacking \[ [85](https://arxiv.org/html/2603.07379v1#bib.bib37 "Learning latency-aware orchestration for parallel multi-agent systems")\]. In static RAG, latency is bounded by a single retrieval and generation step. In Agentic RAG, every reasoning loop, tool invocation, and reflection step compounds the total response time \[ [85](https://arxiv.org/html/2603.07379v1#bib.bib37 "Learning latency-aware orchestration for parallel multi-agent systems")\]. To mitigate this, systems construct layer-wise execution topology graphs, enabling the parallel execution of independent agent sub-tasks and concurrent security scanning \[ [85](https://arxiv.org/html/2603.07379v1#bib.bib37 "Learning latency-aware orchestration for parallel multi-agent systems")\].

Additionally, agents operating in non-deterministic loops can easily become trapped in infinite execution cycles if confronted with ambiguous API feedback. Without strict orchestration limits on recursion depth, autonomous agents rapidly exhaust API budgets \[ [113](https://arxiv.org/html/2603.07379v1#bib.bib42 "TURA: tool-augmented unified retrieval agent for ai search")\]. Consequently, production systems mandate rigorous observability layers to monitor token economics and execution trajectories in real-time.

This highlights a structural divergence between academic research and industrial deployment. Academic prototypes frequently rely on monolithic LLMs executing unconstrained tool usage to maximize benchmark scores. Conversely, industry prioritizes determinism, utilizing constrained Agent-Computer Interfaces and lightweight, distilled routing models to achieve fidelity at a fraction of the computational cost \[ [113](https://arxiv.org/html/2603.07379v1#bib.bib42 "TURA: tool-augmented unified retrieval agent for ai search")\]. Bridging this gap requires standardizing evaluation pipelines to measure computational efficiency and procedural control alongside final output accuracy.

Practical deployments of agentic RAG systems must also account for operational constraints such as latency limits, token budgets, and memory footprint restrictions. Industrial applications often impose limits on reasoning trajectory length and retrieval expansion to control inference cost and response time. These constraints motivate adaptive policies such as budget-aware retrieval triggers, early termination criteria, and hierarchical retrieval pipelines that minimize redundant context expansion. Designing agent policies that balance reasoning depth with computational efficiency remains a critical challenge for real-world agentic systems.

Industrial frameworks operationalize agentic abstractions through modular orchestration layers and tool routing mechanisms. While these systems demonstrate practical feasibility, they often prioritize flexibility over formal guarantees. The next section examines the systemic risks and safety challenges that arise from such autonomy.

## IX Failure Modes, Safety, and Reliability Challenges

While the preceding sections characterized the architectures and design patterns of Agentic RAG, this section addresses their systemic vulnerabilities. The shift from static retrieve-then-generate pipelines to multi-step, tool-integrated workflows introduces novel attack surfaces. Because agentic systems operate iteratively, localized errors compound in ways that are qualitatively different from traditional RAG failures. As synthesized in Table [X](https://arxiv.org/html/2603.07379v1#S9.T10 "TABLE X ‣ IX-F Systemic Risk Amplification in Iterative Agents ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), this section provides a structured analysis of these failure categories, organized by their position in the agentic pipeline.

### IX-ARetrieval Drift and Query Misalignment

In static RAG, retrieval quality is determined entirely by the initial query. In Agentic RAG, the agent reformulates queries across iterations, introducing the possibility of semantic drift: a gradual divergence between the evolving query and the user’s original information need \[ [90](https://arxiv.org/html/2603.07379v1#bib.bib14 "Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions")\]. Query-rewriting approaches acknowledge this problem directly, noting that original queries frequently misalign with what the retriever can effectively resolve \[ [58](https://arxiv.org/html/2603.07379v1#bib.bib31 "Query rewriting for retrieval-augmented large language models")\].

In multi-agent architectures, retrieval drift is compounded by delegation. When a planner agent decomposes a task and delegates sub-queries to retriever agents, the planner’s interpretation of sub-task requirements may diverge from what the retriever can meaningfully resolve \[ [12](https://arxiv.org/html/2603.07379v1#bib.bib39 "JADE: bridging the strategic-operational gap in dynamic agentic rag")\]. Without explicit convergence criteria or retrieval-quality feedback loops, iterative query reformulation can wander indefinitely, consuming token budgets without approaching a satisfactory answer.

### IX-BHallucination Despite Retrieval

RAG was initially motivated as a mechanism to reduce hallucination by grounding generation in retrieved evidence \[ [51](https://arxiv.org/html/2603.07379v1#bib.bib1 "Retrieval-augmented generation for knowledge-intensive NLP tasks")\]. However, empirical studies demonstrate that retrieval does not eliminate this risk; retrieval-augmented legal research tools exhibited hallucination rates up to 33%, contradicting vendor claims \[ [59](https://arxiv.org/html/2603.07379v1#bib.bib72 "Hallucination-free? assessing the reliability of leading AI legal research tools")\]. This occurs when retrieved passages are topically relevant but factually insufficient, when multiple documents contain conflicting information \[ [28](https://arxiv.org/html/2603.07379v1#bib.bib88 "Retrieval-augmented generation for large language models: a survey")\], or when the model succumbs to the lost-in-the-middle effect \[ [55](https://arxiv.org/html/2603.07379v1#bib.bib4 "Lost in the middle: how language models use long contexts")\].

In agentic settings, the hallucination risk is amplified by iteration. An intermediate generation containing a hallucinated claim may be used as context for subsequent retrieval or reasoning steps, causing the error to propagate and reinforce across iterations. While mechanisms like self-reflection attempt to address this by enabling the model to critique its own retrieved passages, the approach relies on the model’s own judgments, which are fundamentally fallible \[ [6](https://arxiv.org/html/2603.07379v1#bib.bib10 "Self-rag: learning to retrieve, generate, and critique through self-reflection")\].

### IX-CTool Misuse and Cascading Errors

Agentic RAG systems extend LLMs beyond text generation to tool invocation, including database queries, API calls, and code execution. Each tool call introduces a potential failure point: the model may select an inappropriate tool, formulate a malformed query, or encounter API timeouts \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\]. ReWOO explicitly evaluates robustness under tool-failure scenarios, noting the severe brittleness of repeated thought-action-observation loops \[ [101](https://arxiv.org/html/2603.07379v1#bib.bib18 "ReWOO: decoupling reasoning from observations for efficient augmented language models")\].

In multi-step workflows, tool failures cascade. A failed API call produces an error message that the agent may misinterpret as valid output and incorporate into subsequent reasoning \[ [35](https://arxiv.org/html/2603.07379v1#bib.bib27 "MetaGPT: meta programming for a multi-agent collaborative framework")\]. While systems implement critique loops where outputs are evaluated and revised based on feedback \[ [31](https://arxiv.org/html/2603.07379v1#bib.bib19 "CRITIC: large language models can self-correct with tool-interactive critiquing")\], the absence of robust fallback mechanisms at each tool invocation point represents a significant structural reliability gap. Furthermore, as agentic workflows increasingly incorporate multimodal tools, they inherently inherit the vulnerabilities of those underlying modules, such as the susceptibility of visual classifiers to stealthy adversarial perturbations and malicious payload injections \[ [104](https://arxiv.org/html/2603.07379v1#bib.bib120 "Exploring secure machine learning through payload injection and fgsm attacks on resnet-50")\].

### IX-DPrompt Injection in Iterative Retrieval

Agentic RAG systems that retrieve from open or semi-curated corpora are highly vulnerable to indirect prompt injection: adversarial content embedded in retrieved documents that manipulates the agent’s behavior. Unlike static RAG, where the attack surface is limited to a single retrieval pass, agentic systems face a compounded risk because each iterative retrieval step offers a new opportunity to encounter injected content \[ [33](https://arxiv.org/html/2603.07379v1#bib.bib73 "Not what you’ve signed up for: compromising real-world LLM-integrated applications with indirect prompt injection")\].

Injecting as few as five carefully crafted malicious documents into a corpus can cause RAG systems to generate attacker-specified answers with a 90% success rate \[ [118](https://arxiv.org/html/2603.07379v1#bib.bib74 "PoisonedRAG: knowledge corruption attacks to retrieval-augmented generation of large language models")\]. In agentic settings, the consequences extend beyond generation errors: injected instructions can alter the agent’s planning, cause it to invoke unintended tools, or exfiltrate information through subsequent actions \[ [77](https://arxiv.org/html/2603.07379v1#bib.bib75 "Securing AI agents against prompt injection attacks")\]. The OWASP Top 10 for LLM Applications identifies this as a leading vulnerability, noting that models struggle to distinguish between trusted instructions and adversarial content in retrieved contexts \[ [73](https://arxiv.org/html/2603.07379v1#bib.bib76 "LLM01:2025 prompt injection")\].

### IX-EMemory Poisoning

Systems that maintain persistent memory across sessions introduce an additional attack vector. If an adversary can influence the content stored in an agent’s long-term memory, all subsequent interactions conditioned on that memory are compromised. This attack survives session terminations, logouts, and device changes when memories are stored server-side \[ [15](https://arxiv.org/html/2603.07379v1#bib.bib77 "Here comes the AI worm: unleashing zero-click worms that target GenAI-powered applications")\].

In Agentic RAG architectures with episodic memory modules, memory poisoning alters the agent’s future retrieval strategies, planning heuristics, and tool-use preferences. Unlike corpus poisoning, which affects a shared knowledge base, memory poisoning targets the agent’s personalized state, making detection exceptionally difficult because the corrupted information is specific to individual user sessions \[ [110](https://arxiv.org/html/2603.07379v1#bib.bib47 "Agentic memory: learning unified long-term and short-term memory management for large language model agents")\].

### IX-FSystemic Risk Amplification in Iterative Agents

The failure modes described above interact and compound in iterative agentic workflows, creating systemic risks that exceed the sum of individual failure categories. Three amplification mechanisms govern this degradation:

- •


Cascading Failure Amplification: A single error at an early step (e.g., a hallucinated intermediate answer or failed tool call) propagates through subsequent iterations. Because agentic systems condition actions on the accumulated history, errors are integrated into the evolving system state rather than isolated.

- •


Compounded Hallucination Loops: When an intermediate hallucination is used as context for a subsequent query, the retriever may return passages that spuriously corroborate the hallucination, creating a self-reinforcing cycle that artificially increases the model’s confidence in incorrect information.

- •


Feedback Reinforcement Instability: In systems with reflection modules, the critique mechanism may be biased by the same errors it is meant to detect. If the reflection module operates under the same parametric biases as the generator, it may approve flawed outputs, leading to divergent behavior rather than convergence.


TABLE X: Structured Failure-Mode Categorization for Agentic RAG Systems

| Failure Mode | Pipeline Stage | Root Cause | Agentic Amplification Factor | Severity / Impact |
| --- | --- | --- | --- | --- |
| Retrieval Drift | Iterative Retrieval | Semantic divergence in query reformulation | Compounds across iterations without convergence guarantees | Moderate (Degrades accuracy, increases cost) |
| Hallucination | Generation | Context insufficiency or positional bias | Hallucinated outputs become retrieval context in next iteration | High (Corrupts downstream logic and planning) |
| Tool Misuse | Tool Orchestration | Malformed queries, API failures | Errors propagate through dependent downstream tool calls | High (Causes systemic execution crashes) |
| Prompt Injection | Retrieval Context | Adversarial content in retrieved documents | Each retrieval iteration exposes new injection surface | Critical (Enables unauthorized data exfiltration) |
| Memory Poisoning | Memory Systems | Adversarial manipulation of persistent state | Corrupted memory affects all future sessions and decisions | Critical (Persistent, cross-session compromise) |
| Feedback Instability | Reflection | Reflection module shares generator biases | Self-critique may approve errors or reject correct outputs | Moderate (Prevents loop convergence) |

The autonomy introduced by agentic retrieval loops amplifies traditional LLM risks while introducing new systemic vulnerabilities such as cascading hallucinations, retrieval poisoning, and tool misuse. These risks emerge from feedback-driven decision processes rather than isolated generation errors. Addressing these structural vulnerabilities requires research beyond patch-based mitigation, motivating the grand challenges discussed in the next section.

## X Open Research Challenges and Future Directions

The transition from static Retrieval-Augmented Generation (RAG) to agentic architectures expands the operational capabilities of retrieval-based systems, but it introduces structural complexities that current ad-hoc implementations cannot sustainably manage. As the field matures, research must pivot from empirical prototyping to developing theoretically grounded, scalable, and verifiable systems \[ [108](https://arxiv.org/html/2603.07379v1#bib.bib5 "ReAct: synergizing reasoning and acting in language models")\]. Currently, the development of Agentic RAG remains theoretically under-specified; disparate frameworks rely on customized heuristics for tool orchestration and memory management, a fragmentation that severely impedes reproducibility \[ [94](https://arxiv.org/html/2603.07379v1#bib.bib69 "A survey on large language model based autonomous agents")\]. Furthermore, there is a distinct absence of theoretical frameworks that mathematically bound the behavior of autonomous retrieval loops, leaving the field reliant on empirical prompt engineering rather than formal guarantees \[ [81](https://arxiv.org/html/2603.07379v1#bib.bib6 "Toolformer: language models can teach themselves to use tools")\].

To address these systemic bottlenecks, we formalize five grand research directions structured as doctoral-scale problems. These problems are not mutually exclusive and necessitate interdisciplinary approaches. As mapped in Figure [8](https://arxiv.org/html/2603.07379v1#S10.F8 "Figure 8 ‣ X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"), resolving these grand challenges requires integrating methodologies across multiple foundational system dimensions spanning short, medium, and long-term horizons. A consolidated overview of these five problems—detailing their primary risks, theoretical gaps, and core evaluation metrics—is provided in Table [XI](https://arxiv.org/html/2603.07379v1#S10.T11 "TABLE XI ‣ X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

![Refer to caption](https://arxiv.org/html/2603.07379v1/figures/research_landscape.png)Figure 8: The interdisciplinary mapping of the proposed doctoral-scale grand problems across foundational system dimensions and research time horizons. Addressing these challenges requires systemic integration rather than isolated optimization.TABLE XI: Summary of Grand Research Problems and Interdisciplinary Roadmap for Agentic RAG

| Grand Problem | Primary Risk | Theoretical Gap | Core Evaluation Metric | Interdisciplinary Domain |
| --- | --- | --- | --- | --- |
| 10.1 Stable Retrieval | Semantic drift and reasoning collapse | Lack of formal convergence proofs for context loops | State-transition convergence bounds | Control Theory, RL |
| 10.2 Reasoning Evaluation | Undetected logical failures | Absence of intermediate trajectory verification | Trajectory inter-rater reliability | Formal Verification |
| 10.3 Memory Security | Persistent episodic poisoning | No robust state modeling against latent triggers | Provable state recovery rate | Systems Security |
| 10.4 Cost Orchestration | Token explosion and latency stacking | No budget-aware multi-agent routing optimization | Pareto efficiency (Compute vs. Accuracy) | Operations Research |
| 10.5 Trust Calibration | Overconfidence in corrupted context | Lack of dynamic uncertainty bounds during retrieval | Expected Calibration Error (ECE) | HCI, Statistics |

### X-AStable Adaptive Retrieval Under Planning Loops

- •


Problem Statement: How can iterative retrieval processes be stabilized under dynamic planning decisions without causing retrieval drift or infinite execution loops?

- •


Why It Matters: Unstable retrieval leads to cascading reasoning failures in multi-step tasks. If an autonomous agent fetches a misaligned document in step one, the error compounds, derailing the cognitive trajectory. The field currently lacks empirical standardization for halting iterative retrievals securely.

- •


Current Limitations: Systems rely on arbitrary heuristic query reformulation (e.g., rigid max\_steps parameters) and lack formal stability guarantees or mathematical convergence proofs for the retrieval loop.

- •


Evaluation Criteria: Maximum task horizon length before reasoning collapse; state-transition convergence bounds; semantic drift penalty scores; and marginal utility of successive retrieval steps.

- •


Methodological Approaches: Control-theoretic modeling of the context window; reinforcement learning with strict stability constraints; retrieval confidence calibration utilizing Bayesian uncertainty estimation.


### X-BFormal Evaluation of Agentic Reasoning Quality

- •


Problem Statement: How can we construct a scalable, automated evaluation framework that assesses the semantic validity, efficiency, and safety of an agent’s multi-step reasoning trajectory rather than just its terminal output?

- •


Why It Matters: Without rigorous trajectory evaluation, developers cannot verify whether a correct terminal answer was achieved through sound logic or stochastic luck, making it impossible to guarantee safety in high-stakes domains \[ [114](https://arxiv.org/html/2603.07379v1#bib.bib62 "Judging LLM-as-a-judge with MT-Bench and chatbot arena")\]. This vulnerability is particularly evident in clinical applications, where recent empirical evaluations demonstrate that while advanced reasoning models achieve high overall diagnostic accuracy, they still exhibit severe performance gaps across specific disease categories, necessitating strict trajectory verification \[ [34](https://arxiv.org/html/2603.07379v1#bib.bib123 "LLMs in disease diagnosis: a comparative study of deepseek-r1 and o3 mini across chronic health conditions")\].

- •


Current Limitations: Existing metrics heavily favor static generation evaluation. Attempts at automated trajectory scoring lack standardized rubrics for intermediate step verification and suffer from evaluator-generator coupling bias.

- •


Evaluation Criteria: Trajectory inter-rater reliability (Cohen’s κ\\kappa) between automated judges and experts; false positive rates for intermediate tool invocations; and quantifiable correlation coefficients between reasoning path efficiency and output quality.

- •


Methodological Approaches: Development of deterministic verification state machines; automated generation of counterfactual retrieval datasets to test agent resilience; multi-dimensional reward modeling focusing on logical coherence.


### X-CMemory Robustness and Poisoning Resistance

- •


Problem Statement: How can Agentic RAG systems with persistent read/write memory be secured against adversarial data injection that corrupts the control policy over time?

- •


Why It Matters: While Section [IX](https://arxiv.org/html/2603.07379v1#S9 "IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") diagnoses the systemic vulnerabilities of persistent memory, the theoretical gap lies in developing architectural immunity. The field requires formal guarantees to ensure an autonomous policy remains uncorrupted after ingesting adversarial context into episodic memory \[ [32](https://arxiv.org/html/2603.07379v1#bib.bib63 "More than you’ve asked for: a comprehensive analysis of novel prompt injection threats to application-integrated large language models")\].

- •


Current Limitations: Existing defenses rely on superficial input sanitization or static guardrails, which fail entirely when malicious triggers are mapped to unique, stealthy regions in the vector embedding space.

- •


Evaluation Criteria: Provable state recovery rates post-injection; cross-session leakage containment bounds; and the Attack Success Rate (ASR) of latent triggers evaluated strictly under formal verification constraints.

- •


Methodological Approaches: Implementation of cryptographic memory provenance tracking; anomaly detection in latent vector spaces to isolate optimized backdoor triggers; memory compartmentalization architectures with strict privilege separation.


### X-DCost-Aware Autonomous Orchestration

- •


Problem Statement: How can Agentic RAG orchestrators dynamically balance the trade-off between the depth of autonomous reasoning and the financial and computational cost of execution?

- •


Why It Matters: Multi-agent collaboration introduces severe token amplification. This problem explicitly targets economic optimality under budget constraints. Without formal cost-aware routing, deploying Agentic RAG at enterprise scale remains computationally unsustainable \[ [46](https://arxiv.org/html/2603.07379v1#bib.bib60 "DSPy: compiling declarative language model calls into state-of-the-art pipelines")\].

- •


Current Limitations: Orchestration frameworks treat queries with uniform resource allocation or rely on static, manually configured routing rules that fail to adapt to query complexity.

- •


Evaluation Criteria: Pareto efficiency optimization (Compute cost vs. Response fidelity); algorithmic routing complexity bounds; and Time-to-First-Token (TTFT) variance under simulated multi-agent load.

- •


Methodological Approaches: Integration of Operations Research (OR) with multi-dimensional reward functions prioritizing budget; predictive complexity modeling to dynamically assign token budgets per query; early-exit classification algorithms for the planning module.


### X-ETrust Calibration and Oversight Mechanisms

- •


Problem Statement: How can Agentic RAG systems internally quantify their epistemic uncertainty during external tool use and autonomously determine when to escalate decisions to human supervisors?

- •


Why It Matters: In mission-critical environments, autonomous agents must not execute high-risk tool calls when retrieval results are ambiguous. Overconfidence in corrupted retrieved context leads to non-compliant outputs and operational failures.

- •


Current Limitations: LLMs exhibit poor inherent uncertainty calibration. Existing Human-in-the-Loop implementations are rigid, requiring validation at predefined programmatic bottlenecks rather than intelligently triggering based on internal state ambiguity.

- •


Evaluation Criteria: Expected Calibration Error (ECE) for tool-use confidence; human-escalation precision and recall; and zero-shot detection rates for conflicting retrieved contexts.

- •


Methodological Approaches: Conformal prediction techniques applied to generative trajectories; entropy-based uncertainty estimation across retrieved document clusters; dynamic human-machine trust negotiation protocols based on game theory.


The grand challenges identified here highlight the systemic research bottlenecks preventing the deployment of truly autonomous, reliable Agentic RAG. Addressing these gaps requires an interdisciplinary convergence of control theory, formal verification, and systems engineering. By solving these doctoral-scale problems, the field can transition Agentic RAG from the empirically driven heuristics of today into the rigorously bounded, partially observable sequential decision processes formalized in Section [III](https://arxiv.org/html/2603.07379v1#S3 "III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"). Having charted this theoretical roadmap, Section [XI](https://arxiv.org/html/2603.07379v1#S11 "XI Conclusion ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions") synthesizes the core structural takeaways of this Systematization of Knowledge.

## XI Conclusion

This Systematization of Knowledge unified the emerging landscape of Agentic Retrieval-Augmented Generation through formal definitions, structural taxonomy, architectural decomposition, evaluation reform, and systemic risk analysis. By mapping the transition from static, single-pass retrieval pipelines to dynamic, policy-driven reasoning loops, this paper provided a comprehensive foundation for understanding how large language models autonomously orchestrate external tools, manage persistent memory, and adapt to environmental feedback.

By distinguishing agentic behavior from iterative retrieval and grounding it within a sequential decision-making framework, we clarified conceptual boundaries that are often conflated in current literature. Our analysis demonstrated that true autonomy requires explicit modular separation between strategic planning, active retrieval, and robust state management. Furthermore, we established that evaluating these architectures necessitates a paradigm shift from static terminal metrics to multi-dimensional trajectory assessments capable of auditing intermediate logic and tool-use correctness.

As agentic systems continue to evolve, rigorous formalization, evaluation standardization, and safety guarantees will determine whether these architectures mature into reliable reasoning systems or remain experimental extensions of retrieval pipelines. Resolving the doctoral-scale challenges identified in this roadmap—ranging from stable retrieval convergence to memory poisoning resistance—requires interdisciplinary collaboration across control theory, cybersecurity, and operations research.

A central insight emerging from this systematization is that agentic RAG systems should be viewed not merely as extensions of retrieval pipelines, but as sequential decision-making systems in which language models coordinate reasoning, retrieval, and tool interaction across multiple steps. Recognizing this shift is essential for designing robust architectures, developing meaningful evaluation methodologies, and understanding the broader reliability implications of deploying such systems in real-world environments. Ultimately, transitioning from empirical heuristics to theoretically bounded frameworks is the prerequisite for deploying trustworthy autonomous knowledge systems in high-stakes environments.

## References

- \[1\]A. Aavani (2026)Capturing p: on the expressive power and efficient evaluation of boolean retrieval.
arXiv preprint arXiv:2601.18747.
Cited by: [§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p1.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[2\]Agentic Memory Authors (2025)Agentic memory systems.
arXiv preprint arXiv:2502.12110.
Cited by: [§V-D](https://arxiv.org/html/2603.07379v1#S5.SS4.p3.1 "V-D Memory Systems ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[3\]M. Alenezi (2026)From prompt–response to goal-directed systems: the evolution of agentic ai software architecture.
arXiv preprint arXiv:2602.10479.
Cited by: [§VIII-B](https://arxiv.org/html/2603.07379v1#S8.SS2.p1.1 "VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VIII-B](https://arxiv.org/html/2603.07379v1#S8.SS2.p2.1 "VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VIII-B](https://arxiv.org/html/2603.07379v1#S8.SS2.p3.1 "VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE IX](https://arxiv.org/html/2603.07379v1#S8.T9.1.2.1.1.1.1 "In VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE IX](https://arxiv.org/html/2603.07379v1#S8.T9.1.4.3.1.1.1 "In VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE IX](https://arxiv.org/html/2603.07379v1#S8.T9.1.5.4.1.1.1 "In VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE IX](https://arxiv.org/html/2603.07379v1#S8.T9.1.6.5.1.1.1 "In VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[4\]Anthropic (2025)Introducing advanced tool use on the claude developer platform.
Note: Accessed 2026-02-24External Links: [Link](https://www.anthropic.com/engineering/advanced-tool-use "")Cited by: [§IV-E2](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS2.p1.1 "IV-E2 Planning Complexity vs Latency ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E](https://arxiv.org/html/2603.07379v1#S4.SS5.p1.1 "IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[5\]Anthropic (2026)Tool use with claude: overview (claude api docs).
Note: Accessed 2026-02-24External Links: [Link](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview "")Cited by: [§IV-A2](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS2.p1.1 "IV-A2 Planner–Executor Architectures ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[6\]A. Asai et al. (2024)Self-rag: learning to retrieve, generate, and critique through self-reflection.
In International Conference on Learning Representations (ICLR),
External Links: 2310.11511,
[Link](https://arxiv.org/abs/2310.11511 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p1.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B3](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS3.p1.1 "IV-B3 Self-Refining Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.4.3.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[2nd item](https://arxiv.org/html/2603.07379v1#S6.I2.i2.p1.1 "In VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-B](https://arxiv.org/html/2603.07379v1#S6.SS2.p1.1 "VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.3.2.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-B](https://arxiv.org/html/2603.07379v1#S9.SS2.p2.1 "IX-B Hallucination Despite Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[7\]B. Bhusal, M. Acharya, R. Kaur, C. Samplawski, A. Roy, A. D. Cobb, R. Chadha, and S. Jha (2025)Privacy preserving in-context-learning framework for large language models.
arXiv preprint arXiv:2509.13625.
External Links: [Link](https://arxiv.org/abs/2509.13625 "")Cited by: [§VIII-A](https://arxiv.org/html/2603.07379v1#S8.SS1.p1.1 "VIII-A Domain-Specific Implementations ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[8\]B. Bohnet, V. Q. Tran, P. Verga, R. Aharoni, D. Andor, L. Baldini Soares, M. Ciaramita, J. Eisenstein, K. Ganchev, J. Herzig, K. Hui, T. Kwiatkowski, J. Ma, J. Ni, L. Sestorain Saralegui, T. Schuster, W. W. Cohen, M. Collins, D. Das, D. Metzler, S. Petrov, and K. Webster (2022)Attributed question answering: evaluation and modeling for attributed large language models.
arXiv preprint arXiv:2212.08037.
External Links: [Link](https://arxiv.org/abs/2212.08037 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[3rd item](https://arxiv.org/html/2603.07379v1#S6.I6.i3.p1.1 "In VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[9\]T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. (2020)Language models are few-shot learners.
In Advances in Neural Information Processing Systems (NeurIPS),
Vol. 33.
External Links: [Link](https://arxiv.org/abs/2005.14165 "")Cited by: [§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p1.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[10\]J. Chen, H. Lin, X. Han, and L. Sun (2023)Benchmarking large language models in retrieval-augmented generation.
External Links: 2309.01431,
[Link](https://arxiv.org/abs/2309.01431 "")Cited by: [5th item](https://arxiv.org/html/2603.07379v1#S7.I1.i5.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p1.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VIII](https://arxiv.org/html/2603.07379v1#S7.T8.1.2.1.1.1.1 "In VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[11\]Y. Chen et al. (2024)DRACO: diagnostic reasoning for comprehensive agent evaluation.
arXiv preprint arXiv:2403.XXXXX.
External Links: [Link](https://arxiv.org/abs/2403.XXXXX "")Cited by: [§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p2.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[12\]Y. Chen, E. Zhang, T. Hu, S. Wang, Z. Yang, M. Zhong, and J. Mao (2026)JADE: bridging the strategic-operational gap in dynamic agentic rag.
arXiv preprint arXiv:2601.21916.
Cited by: [§V-A](https://arxiv.org/html/2603.07379v1#S5.SS1.p1.1 "V-A Planner Module ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-A](https://arxiv.org/html/2603.07379v1#S5.SS1.p3.1 "V-A Planner Module ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-A](https://arxiv.org/html/2603.07379v1#S9.SS1.p2.1 "IX-A Retrieval Drift and Query Misalignment ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[13\]Q. Cheng, X. Li, S. Li, Q. Zhu, Z. Yin, Y. Shao, L. Li, T. Sun, H. Yan, and X. Qiu (2024)Unified active retrieval for retrieval augmented generation.
In Findings of the Association for Computational Linguistics: EMNLP 2024,
External Links: [Link](https://aclanthology.org/2024.findings-emnlp.999/ ""),
[Document](https://dx.doi.org/10.18653/v1/2024.findings-emnlp.999 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[6th item](https://arxiv.org/html/2603.07379v1#S6.I2.i6.p1.1 "In VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[6th item](https://arxiv.org/html/2603.07379v1#S6.I7.i6.p1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[14\]N. Chirkova, T. Formal, V. Nikoulina, and S. Clinchant (2025)Provence: efficient and robust context pruning for retrieval-augmented generation.
External Links: 2501.16214,
[Link](https://arxiv.org/abs/2501.16214 "")Cited by: [§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p1.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E1](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS1.p1.1 "IV-E1 Retrieval Depth vs Cost ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[15\]S. Cohen, R. Bitton, and B. Nassi (2024)Here comes the AI worm: unleashing zero-click worms that target GenAI-powered applications.
arXiv preprint arXiv:2403.02817.
External Links: [Link](https://arxiv.org/abs/2403.02817 "")Cited by: [§IX-E](https://arxiv.org/html/2603.07379v1#S9.SS5.p1.1 "IX-E Memory Poisoning ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[16\]A. Costarelli, M. Allen, R. Hauksson, G. Sodunke, S. Hariharan, C. Cheng, W. Li, and A. Yadav (2024)GAMEBENCH: evaluating strategic reasoning abilities of LLM agents.
Note: arXivExternal Links: [Link](https://arxiv.org/html/2406.06613v1#S1 "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S7.I1.i2.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[17\]crewAIInc (2026)CrewAI: multi-agent framework (github repository).
Note: Accessed 2026-02-24External Links: [Link](https://github.com/crewAIInc/crewAI "")Cited by: [§IV-A3](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS3.p1.1 "IV-A3 Multi-Agent RAG Systems ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.6.5.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[18\]S. Dhuliawala et al. (2023)Chain-of-verification reduces hallucination in large language models.
arXiv preprint arXiv:2309.11495.
External Links: [Link](https://arxiv.org/abs/2309.11495 "")Cited by: [1st item](https://arxiv.org/html/2603.07379v1#S6.I6.i1.p1.3 "In VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-F](https://arxiv.org/html/2603.07379v1#S6.SS6.p1.1 "VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.7.6.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[19\]M. Du, B. Xu, C. Zhu, S. Wang, P. Wang, X. Wang, and Z. Mao (2026)A-rag: scaling agentic retrieval-augmented generation via hierarchical retrieval interfaces.
arXiv preprint arXiv:2602.03442.
Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p3.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p2.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p3.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V](https://arxiv.org/html/2603.07379v1#S5.p1.1 "V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-B](https://arxiv.org/html/2603.07379v1#S6.SS2.p1.1 "VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[20\]L. E. Erdogan et al. (2025)Improving planning of agents for long-horizon tasks.
External Links: 2503.09572,
[Link](https://arxiv.org/abs/2503.09572 "")Cited by: [§IV-A2](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS2.p1.1 "IV-A2 Planner–Executor Architectures ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E2](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS2.p1.1 "IV-E2 Planning Complexity vs Latency ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[21\]W. Fan, Y. Ding, L. Ning, S. Wang, H. Li, D. Yin, T. Chua, and Q. Li (2024)A survey on RAG meeting LLMs: towards retrieval-augmented large language models.
External Links: 2405.06211,
[Link](https://arxiv.org/abs/2405.06211 "")Cited by: [§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B](https://arxiv.org/html/2603.07379v1#S4.SS2.p1.1 "IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.2.1.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[22\]P. Ferrazzi, M. Cvjeticanin, A. Piraccini, and D. Giannuzzi (2026)Is agentic rag worth it? an experimental comparison of rag approaches.
arXiv preprint arXiv:2601.07711.
External Links: [Link](https://arxiv.org/abs/2601.07711 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p3.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[23\]R. Friel, M. Belyi, and A. Sanyal (2025)RAGBench: explainable benchmark for retrieval-augmented generation systems.
External Links: 2407.11005,
[Link](https://arxiv.org/abs/2407.11005 "")Cited by: [1st item](https://arxiv.org/html/2603.07379v1#S7.I1.i1.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[3rd item](https://arxiv.org/html/2603.07379v1#S7.I1.i3.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p1.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VIII](https://arxiv.org/html/2603.07379v1#S7.T8.1.3.2.1.1.1 "In VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[24\]S. Gaire, S. Gyawali, S. Mishra, S. Niroula, D. Thakur, and U. Yadav (2025)Systematization of knowledge: security and safety in the model context protocol ecosystem.
arXiv preprint arXiv:2512.08290.
External Links: [Link](https://arxiv.org/abs/2512.08290 "")Cited by: [§VIII-B](https://arxiv.org/html/2603.07379v1#S8.SS2.p2.1 "VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[25\]L. Gao, Z. Dai, P. Pasupat, A. Chen, A. T. Chaganty, Y. Fan, V. Zhao, N. Lao, H. Lee, D. Juan, and K. Guu (2023)RARR: researching and revising what language models say, using language models.
In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
Toronto, Canada,  pp. 16477–16508.
External Links: [Document](https://dx.doi.org/10.18653/v1/2023.acl-long.910 ""),
[Link](https://aclanthology.org/2023.acl-long.910/ "")Cited by: [§IV-B3](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS3.p1.1 "IV-B3 Self-Refining Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C2](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS2.p1.1 "IV-C2 Reflection & Tree-Based Exploration ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.4.3.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[26\]T. Gao et al. (2023)Enabling large language models to generate text with citations.
arXiv preprint arXiv:2305.14627.
External Links: [Link](https://arxiv.org/abs/2305.14627 "")Cited by: [4th item](https://arxiv.org/html/2603.07379v1#S6.I6.i4.p1.1 "In VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[27\]T. Gao, H. Yen, J. Yu, and D. Chen (2023)Enabling large language models to generate text with citations.
In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
pp. 6465–6488.
Cited by: [§III-B](https://arxiv.org/html/2603.07379v1#S3.SS2.p2.1 "III-B Need for Iterative Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[28\]Y. Gao, Y. Xiong, X. Gao, K. Jia, J. Pan, Y. Bi, Y. Dai, J. Sun, M. Wang, and H. Wang (2023)Retrieval-augmented generation for large language models: a survey.
External Links: 2312.10997,
[Link](https://arxiv.org/abs/2312.10997 "")Cited by: [§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B1](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS1.p1.1 "IV-B1 One-Shot Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B](https://arxiv.org/html/2603.07379v1#S4.SS2.p1.1 "IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.2.1.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-B](https://arxiv.org/html/2603.07379v1#S9.SS2.p1.1 "IX-B Hallucination Despite Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[29\]Google Developer Documentation (2025)Agent development kit (adk).
Note: Google Open SourceCited by: [§VIII-B](https://arxiv.org/html/2603.07379v1#S8.SS2.p2.1 "VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE IX](https://arxiv.org/html/2603.07379v1#S8.T9.1.3.2.1.1.1 "In VIII-B Industrial Orchestration Frameworks ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[30\]Google (2026)Agent development kit (adk) documentation.
Note: Accessed 2026-02-24External Links: [Link](https://google.github.io/adk-docs/ "")Cited by: [§IV-A3](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS3.p1.1 "IV-A3 Multi-Agent RAG Systems ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E](https://arxiv.org/html/2603.07379v1#S4.SS5.p1.1 "IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.6.5.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[31\]Z. Gou et al. (2023)CRITIC: large language models can self-correct with tool-interactive critiquing.
arXiv preprint arXiv:2305.11738.
External Links: [Link](https://arxiv.org/abs/2305.11738 "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S6.I4.i2.p1.1 "In VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-F](https://arxiv.org/html/2603.07379v1#S6.SS6.p1.1 "VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.5.4.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-C](https://arxiv.org/html/2603.07379v1#S9.SS3.p2.1 "IX-C Tool Misuse and Cascading Errors ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[32\]K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz (2023)More than you’ve asked for: a comprehensive analysis of novel prompt injection threats to application-integrated large language models.
In Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security,
Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S10.I3.i2.p1.1 "In X-C Memory Robustness and Poisoning Resistance ‣ X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[33\]K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz (2023)Not what you’ve signed up for: compromising real-world LLM-integrated applications with indirect prompt injection.
arXiv preprint arXiv:2302.12173.
External Links: [Link](https://arxiv.org/abs/2302.12173 "")Cited by: [§IX-D](https://arxiv.org/html/2603.07379v1#S9.SS4.p1.1 "IX-D Prompt Injection in Iterative Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[34\]G. K. Gupta, P. Pande, N. Acharya, A. K. Singh, and S. Niroula (2025)LLMs in disease diagnosis: a comparative study of deepseek-r1 and o3 mini across chronic health conditions.
arXiv preprint arXiv:2503.10486.
External Links: [Link](https://arxiv.org/abs/2503.10486 "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S10.I2.i2.p1.1 "In X-B Formal Evaluation of Agentic Reasoning Quality ‣ X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[35\]S. Hong et al. (2024)MetaGPT: meta programming for a multi-agent collaborative framework.
In International Conference on Learning Representations (ICLR),
External Links: [Link](https://openreview.net/forum "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S6.I5.i2.p1.1 "In VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[5th item](https://arxiv.org/html/2603.07379v1#S6.I5.i5.p1.1 "In VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.6.5.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-C](https://arxiv.org/html/2603.07379v1#S9.SS3.p2.1 "IX-C Tool Misuse and Cascading Errors ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[36\]H. Huang, Z. Lin, Z. Wang, X. Chen, K. Ding, and J. Zhao (2024)Towards llm-powered verilog rtl assistant: self-verification and self-correction.
arXiv preprint arXiv:2406.00115.
Cited by: [§V-F](https://arxiv.org/html/2603.07379v1#S5.SS6.p2.1 "V-F Verification and Self-Correction Modules ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[37\]L. Huang, W. Yu, W. Ma, W. Zhong, Z. Feng, H. Wang, Q. Chen, W. Peng, X. Feng, B. Qin, and T. Liu (2023)A survey on hallucination in large language models: principles, taxonomy, challenges, and open questions.
arXiv preprint arXiv:2311.05232.
External Links: [Link](https://arxiv.org/abs/2311.05232 "")Cited by: [§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p2.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[38\]Hugging Face (2026)Smolagents documentation.
Note: Accessed 2026-02-24External Links: [Link](https://huggingface.co/docs/smolagents/en/index "")Cited by: [§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[39\]Hugging-Face (2026)Smolagents (github repository).
Note: Accessed 2026-02-24External Links: [Link](https://github.com/huggingface/smolagents "")Cited by: [§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[40\]G. Izacard and E. Grave (2021)Leveraging passage retrieval with generative models for open domain question answering.
In Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume (EACL),
External Links: [Link](https://aclanthology.org/2021.eacl-main.74/ ""),
[Document](https://dx.doi.org/10.18653/v1/2021.eacl-main.74 "")Cited by: [§II-B](https://arxiv.org/html/2603.07379v1#S2.SS2.p1.1 "II-B Retrieval-Augmented Generation ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[41\]Z. Jiang, F. F. Xu, L. Gao, Z. Sun, Q. Liu, J. Dwivedi-Yu, Y. Yang, J. Callan, and G. Neubig (2023)Active retrieval augmented generation.
arXiv preprint arXiv:2305.06983.
External Links: [Link](https://arxiv.org/abs/2305.06983 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-B](https://arxiv.org/html/2603.07379v1#S2.SS2.p2.1 "II-B Retrieval-Augmented Generation ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§III-D3](https://arxiv.org/html/2603.07379v1#S3.SS4.SSS3.p1.1 "III-D3 Distinguishing Active RAG vs Agentic RAG ‣ III-D Formal Definition of Agentic RAG ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B](https://arxiv.org/html/2603.07379v1#S4.SS2.p1.1 "IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p1.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E1](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS1.p1.1 "IV-E1 Retrieval Depth vs Cost ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E](https://arxiv.org/html/2603.07379v1#S4.SS5.p1.1 "IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[6th item](https://arxiv.org/html/2603.07379v1#S6.I2.i6.p1.1 "In VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[42\]J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei (2020)Scaling laws for neural language models.
arXiv preprint arXiv:2001.08361.
External Links: [Link](https://arxiv.org/abs/2001.08361 "")Cited by: [§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p1.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[43\]E. Karpas, A. Singer, J. Ainslie, E. Omer, A. Petrović, et al. (2022)MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning.
arXiv preprint arXiv:2205.00445.
External Links: [Link](https://arxiv.org/abs/2205.00445 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-C](https://arxiv.org/html/2603.07379v1#S2.SS3.p1.1 "II-C Tool-Augmented and Agentic LLMs ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A2](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS2.p1.1 "IV-A2 Planner–Executor Architectures ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.5.4.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[3rd item](https://arxiv.org/html/2603.07379v1#S6.I4.i3.p1.1 "In VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[44\]V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W. Yih (2020)Dense passage retrieval for open-domain question answering.
In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP),
External Links: [Link](https://aclanthology.org/2020.emnlp-main.550/ ""),
[Document](https://dx.doi.org/10.18653/v1/2020.emnlp-main.550 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p1.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-B](https://arxiv.org/html/2603.07379v1#S2.SS2.p1.1 "II-B Retrieval-Augmented Generation ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[45\]O. Khattab, C. Potts, and M. Zaharia (2021)Baleen: robust multi-hop reasoning at scale via condensed retrieval.
In Advances in Neural Information Processing Systems,
Vol. 34,  pp. 27670–27682.
Cited by: [§III-A](https://arxiv.org/html/2603.07379v1#S3.SS1.p3.1 "III-A Limitations of Standard RAG Pipelines ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[46\]O. Khattab, A. Singhvi, P. Maheshwari, Z. Zhang, K. Santhanam, S. Vardhamanan, S. Haq, A. Sharma, T. T. Joshi, H. Moazam, H. Miller, M. Zaharia, and C. Potts (2024)DSPy: compiling declarative language model calls into state-of-the-art pipelines.
In International Conference on Learning Representations (ICLR),
Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S10.I4.i2.p1.1 "In X-D Cost-Aware Autonomous Orchestration ‣ X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[47\]T. Khot, H. Trivedi, M. Finlayson, Y. Fu, K. Richardson, P. Clark, and A. Sabharwal (2021)MuSiQue: multihop questions via single-hop question generation.
Transactions of the Association for Computational Linguistics9,  pp. 537–554.
Cited by: [§III-B](https://arxiv.org/html/2603.07379v1#S3.SS2.p1.1 "III-B Need for Iterative Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[48\]LangChain-AI (2026)LangGraph (github repository).
Note: Accessed 2026-02-24External Links: [Link](https://github.com/langchain-ai/langgraph "")Cited by: [§IV-A3](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS3.p1.1 "IV-A3 Multi-Agent RAG Systems ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.6.5.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[49\]LangChain (2026)LangChain agents documentation.
Note: Accessed 2026-02-24External Links: [Link](https://docs.langchain.com/oss/python/langchain/agents "")Cited by: [§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B1](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS1.p1.1 "IV-B1 One-Shot Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C1](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS1.p1.1 "IV-C1 Chain-of-Thought & ReAct-Style ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E3](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS3.p1.1 "IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.3.2.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[50\]LangChain (2026)LangGraph: agent orchestration framework (product page).
Note: Accessed 2026-02-24External Links: [Link](https://www.langchain.com/langgraph "")Cited by: [§IV-A3](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS3.p1.1 "IV-A3 Multi-Agent RAG Systems ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[51\]P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, and D. Kiela (2020)Retrieval-augmented generation for knowledge-intensive NLP tasks.
In Advances in Neural Information Processing Systems (NeurIPS),
External Links: 2005.11401,
[Link](https://arxiv.org/abs/2005.11401 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p1.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p2.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-B](https://arxiv.org/html/2603.07379v1#S2.SS2.p1.1 "II-B Retrieval-Augmented Generation ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§III-A](https://arxiv.org/html/2603.07379v1#S3.SS1.p1.7 "III-A Limitations of Standard RAG Pipelines ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B1](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS1.p1.1 "IV-B1 One-Shot Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.2.1.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-B](https://arxiv.org/html/2603.07379v1#S9.SS2.p1.1 "IX-B Hallucination Despite Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[52\]G. Li et al. (2023)CAMEL: communicative agents for ”mind” exploration of large language model society.
arXiv preprint arXiv:2303.17760.
External Links: [Link](https://arxiv.org/abs/2303.17760 "")Cited by: [§VI-E](https://arxiv.org/html/2603.07379v1#S6.SS5.p1.1 "VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[53\]M. Li et al. (2024)Search-r2: search-augmented reasoning and refinement for large language models.
arXiv preprint arXiv:2405.XXXXX.
External Links: [Link](https://arxiv.org/abs/2405.XXXXX "")Cited by: [§VI-F](https://arxiv.org/html/2603.07379v1#S6.SS6.p1.1 "VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[54\]N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni, and P. Liang (2024)Lost in the middle: how language models use long contexts.
Transactions of the Association for Computational Linguistics12,  pp. 157–173.
Cited by: [§III-A](https://arxiv.org/html/2603.07379v1#S3.SS1.p2.1 "III-A Limitations of Standard RAG Pipelines ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[55\]N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni, and P. Liang (2024)Lost in the middle: how language models use long contexts.
Transactions of the Association for Computational Linguistics12,  pp. 157–173.
External Links: [Link](https://aclanthology.org/2024.tacl-1.9/ ""),
[Document](https://dx.doi.org/10.1162/tacl%5Fa%5F00638 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p1.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p2.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-E](https://arxiv.org/html/2603.07379v1#S2.SS5.p1.1 "II-E Memory-Augmented Systems ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p1.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-B](https://arxiv.org/html/2603.07379v1#S9.SS2.p1.1 "IX-B Hallucination Despite Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[56\]LlamaIndex (2026)LlamaIndex agents documentation.
Note: Accessed 2026-02-24External Links: [Link](https://developers.llamaindex.ai/python/framework/use_cases/agents/ "")Cited by: [§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[57\]J. Logan (2026)Continuum memory architectures for long-horizon llm agents.
arXiv preprint arXiv:2601.09913.
Cited by: [§V-D](https://arxiv.org/html/2603.07379v1#S5.SS4.p1.1 "V-D Memory Systems ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-D](https://arxiv.org/html/2603.07379v1#S5.SS4.p2.1 "V-D Memory Systems ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[58\]X. Ma, Y. Gong, P. He, H. Zhao, and N. Duan (2023)Query rewriting for retrieval-augmented large language models.
arXiv preprint arXiv:2305.14283.
External Links: [Link](https://arxiv.org/abs/2305.14283 "")Cited by: [4th item](https://arxiv.org/html/2603.07379v1#S6.I2.i4.p1.1 "In VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-A](https://arxiv.org/html/2603.07379v1#S9.SS1.p1.1 "IX-A Retrieval Drift and Query Misalignment ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[59\]V. Magesh, F. Surani, M. Dahl, M. Suzgun, C. D. Manning, and D. E. Ho (2025)Hallucination-free? assessing the reliability of leading AI legal research tools.
Journal of Empirical Legal Studies.
External Links: [Link](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf "")Cited by: [§IX-B](https://arxiv.org/html/2603.07379v1#S9.SS2.p1.1 "IX-B Hallucination Despite Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[60\]A. Maharjan and U. Yadav (2026)Chunking, retrieval, and re-ranking: an empirical evaluation of rag architectures for policy document question answering.
arXiv preprint arXiv:2601.15457.
External Links: [Link](https://arxiv.org/abs/2601.15457 "")Cited by: [§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p3.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[61\]B. Malin, T. Kalganova, and N. Boulgouris (2025)A review of faithfulness metrics for hallucination assessment in large language models.
External Links: 2501.00269,
[Link](https://arxiv.org/abs/2501.00269 "")Cited by: [1st item](https://arxiv.org/html/2603.07379v1#S7.I1.i1.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-D](https://arxiv.org/html/2603.07379v1#S7.SS4.p1.1 "VII-D Systemic Evaluation Gaps ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.2.1.3.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.3.2.3.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.3.2.4.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII](https://arxiv.org/html/2603.07379v1#S7.p3.1 "VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[62\]J. Menick et al. (2022)Teaching language models to support answers with verified quotes.
arXiv preprint arXiv:2203.11147.
External Links: [Link](https://arxiv.org/abs/2203.11147 "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S6.I6.i2.p1.1 "In VI-F Retrieval-Grounded Self-Verification Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.7.6.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[63\]Microsoft (2026)AutoGen documentation: multi-agent conversation framework.
Note: Accessed 2026-02-24External Links: [Link](https://microsoft.github.io/autogen/0.2/docs/Use-Cases/agent_chat/ "")Cited by: [§IV-A3](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS3.p1.1 "IV-A3 Multi-Agent RAG Systems ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.6.5.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[64\]S. Min, V. Zhong, L. Zettlemoyer, and H. Hajishirzi (2019)Multi-hop reading comprehension through question decomposition and rescoring.
In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL),
External Links: [Link](https://aclanthology.org/P19-1613/ ""),
[Document](https://dx.doi.org/10.18653/v1/P19-1613 "")Cited by: [1st item](https://arxiv.org/html/2603.07379v1#S6.I1.i1.p1.3 "In VI-A Plan-Then-Retrieve Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[3rd item](https://arxiv.org/html/2603.07379v1#S6.I1.i3.p1.1 "In VI-A Plan-Then-Retrieve Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[65\]Y. Ming, S. Purushwalkam, S. Pandit, Z. Ke, X.-P. Nguyen, C. Xiong, and S. Joty (2024)FaithEval: can your language model stay faithful to context, even if “the moon is made of marshmallows”.
External Links: 2410.03727,
[Link](https://arxiv.org/abs/2410.03727 "")Cited by: [1st item](https://arxiv.org/html/2603.07379v1#S7.I1.i1.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p1.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C3](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS3.p1.1 "VII-C3 Layer 3: System-Level Outcome ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VIII](https://arxiv.org/html/2603.07379v1#S7.T8.1.2.1.1.1.1 "In VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[66\]S. Mishra and H. Reza (2022)A face recognition method using deep learning to identify mask and unmask objects.
In 2022 IEEE World AI IoT Congress (AIIoT),
pp. 091–099.
External Links: [Document](https://dx.doi.org/10.1109/AIIoT54504.2022.9817324 "")Cited by: [§VIII-A](https://arxiv.org/html/2603.07379v1#S8.SS1.p1.1 "VIII-A Domain-Specific Implementations ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[67\]M. Mohammadi, Y. Li, J. Lo, and W. Yip (2025)Evaluation and benchmarking of LLM agents: a survey.
External Links: 2507.21504,
[Link](https://arxiv.org/abs/2507.21504 "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S7.I1.i2.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[4th item](https://arxiv.org/html/2603.07379v1#S7.I1.i4.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[5th item](https://arxiv.org/html/2603.07379v1#S7.I1.i5.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C1](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS1.p1.1 "VII-C1 Layer 1: Component-Level Assessment ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C2](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS2.p1.1 "VII-C2 Layer 2: Trajectory-Level Coherence ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C3](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS3.p1.1 "VII-C3 Layer 3: System-Level Outcome ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C](https://arxiv.org/html/2603.07379v1#S7.SS3.p1.1 "VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-D](https://arxiv.org/html/2603.07379v1#S7.SS4.p2.1 "VII-D Systemic Evaluation Gaps ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.6.5.3.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.6.5.4.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII](https://arxiv.org/html/2603.07379v1#S7.p2.1 "VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[68\]K. Mukherjee et al. (2025)LLM-driven provenance forensics for threat investigation and detection.
arXiv preprint arXiv:2508.21323.
Cited by: [§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p3.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[69\]R. Nakano, J. Hilton, S. Balaji, J. Wu, P. Abbeel, et al. (2021)WebGPT: browser-assisted question-answering with human feedback.
arXiv preprint arXiv:2112.09332.
External Links: [Link](https://arxiv.org/abs/2112.09332 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§III-C](https://arxiv.org/html/2603.07379v1#S3.SS3.p2.1 "III-C Emergence of Planning-Driven Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[1st item](https://arxiv.org/html/2603.07379v1#S6.I4.i1.p1.4 "In VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[2nd item](https://arxiv.org/html/2603.07379v1#S6.I7.i2.p1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-G](https://arxiv.org/html/2603.07379v1#S6.SS7.p1.1 "VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.8.7.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[70\]T. Nguyen, P. Chin, and Y.-W. Tai (2025)MA-rag: multi-agent retrieval-augmented generation via collaborative chain-of-thought reasoning.
arXiv preprint arXiv:2505.20096.
Cited by: [§V-A](https://arxiv.org/html/2603.07379v1#S5.SS1.p1.1 "V-A Planner Module ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-A](https://arxiv.org/html/2603.07379v1#S5.SS1.p2.1 "V-A Planner Module ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V](https://arxiv.org/html/2603.07379v1#S5.p2.1 "V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[71\]OpenAI (2025)Function calling — openai api documentation.
Note: Accessed 2026-02-24External Links: [Link](https://developers.openai.com/api/docs/guides/function-calling/ "")Cited by: [§IV-A2](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS2.p1.1 "IV-A2 Planner–Executor Architectures ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B2](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS2.p1.1 "IV-B2 Iterative Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E2](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS2.p1.1 "IV-E2 Planning Complexity vs Latency ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E3](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS3.p1.1 "IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E](https://arxiv.org/html/2603.07379v1#S4.SS5.p1.1 "IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[72\]OpenAI (2026)Agents sdk — openai api documentation.
Note: Accessed 2026-02-24External Links: [Link](https://developers.openai.com/api/docs/guides/agents-sdk/ "")Cited by: [§IV-A1](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS1.p1.1 "IV-A1 Single-Agent RAG ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-A](https://arxiv.org/html/2603.07379v1#S4.SS1.p1.1 "IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B1](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS1.p1.1 "IV-B1 One-Shot Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C1](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS1.p1.1 "IV-C1 Chain-of-Thought & ReAct-Style ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p3.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.5.4.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[73\]OWASP Foundation (2025)LLM01:2025 prompt injection.
Note: OWASP Top 10 for Large Language Model ApplicationsExternal Links: [Link](https://genai.owasp.org/llmrisk/llm01-prompt-injection/ "")Cited by: [§IX-D](https://arxiv.org/html/2603.07379v1#S9.SS4.p2.1 "IX-D Prompt Injection in Iterative Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[74\]C. Packer, S. Wooders, K. Lin, V. Fang, S. G. Patil, I. Stoica, and J. E. Gonzalez (2024)MemGPT: towards llms as operating systems.
External Links: 2310.08560,
[Link](https://arxiv.org/abs/2310.08560 "")Cited by: [§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p3.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.7.6.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[75\]J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein (2023)Generative agents: interactive simulacra of human behavior.
In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST),
External Links: [Link](https://arxiv.org/abs/2304.03442 ""),
[Document](https://dx.doi.org/10.1145/3586183.3606763 "")Cited by: [§II-E](https://arxiv.org/html/2603.07379v1#S2.SS5.p2.1 "II-E Memory-Augmented Systems ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[76\]J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein (2023)Generative agents: interactive simulacra of human behavior.
External Links: 2304.03442,
[Link](https://arxiv.org/abs/2304.03442 "")Cited by: [§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p2.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[77\]D. Pasquini et al. (2024)Securing AI agents against prompt injection attacks.
arXiv preprint arXiv:2511.15759.
External Links: [Link](https://arxiv.org/abs/2511.15759 "")Cited by: [§IX-D](https://arxiv.org/html/2603.07379v1#S9.SS4.p2.1 "IX-D Prompt Injection in Iterative Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[78\]O. Press et al. (2022)Measuring and narrowing the compositionality gap in language models.
arXiv preprint arXiv:2210.03350.
External Links: [Link](https://arxiv.org/abs/2210.03350 "")Cited by: [§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p2.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-A](https://arxiv.org/html/2603.07379v1#S6.SS1.p1.1 "VI-A Plan-Then-Retrieve Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.2.1.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[79\]C. Qian et al. (2024)ChatDev: communicative agents for software development.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL), Long Papers,
External Links: [Link](https://aclanthology.org/2024.acl-long.810/ "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S6.I5.i2.p1.1 "In VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[4th item](https://arxiv.org/html/2603.07379v1#S6.I5.i4.p1.1 "In VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[80\]T. Richards (2023)Auto-GPT: an autonomous GPT-4 experiment.
GitHub.
Note: [https://github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT "")Cited by: [§III-C](https://arxiv.org/html/2603.07379v1#S3.SS3.p2.1 "III-C Emergence of Planning-Driven Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[81\]T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, L. Zettlemoyer, N. Cancedda, and T. Scialom (2023)Toolformer: language models can teach themselves to use tools.
arXiv preprint arXiv:2302.04761.
External Links: [Link](https://arxiv.org/abs/2302.04761 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§X](https://arxiv.org/html/2603.07379v1#S10.p1.1 "X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-C](https://arxiv.org/html/2603.07379v1#S2.SS3.p1.1 "II-C Tool-Augmented and Agentic LLMs ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§III-C](https://arxiv.org/html/2603.07379v1#S3.SS3.p2.1 "III-C Emergence of Planning-Driven Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E3](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS3.p1.1 "IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[2nd item](https://arxiv.org/html/2603.07379v1#S6.I4.i2.p1.1 "In VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[4th item](https://arxiv.org/html/2603.07379v1#S6.I4.i4.p1.1 "In VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-D](https://arxiv.org/html/2603.07379v1#S6.SS4.p1.1 "VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.5.4.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-C](https://arxiv.org/html/2603.07379v1#S9.SS3.p1.1 "IX-C Tool Misuse and Cascading Errors ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[82\]Z. Shao, Y. Gong, Y. Shen, M. Huang, N. Duan, and W. Chen (2023)Enhancing retrieval-augmented large language models with iterative retrieval-generation synergy.
In Findings of the Association for Computational Linguistics: EMNLP 2023,
External Links: [Link](https://aclanthology.org/2023.findings-emnlp.620/ ""),
[Document](https://dx.doi.org/10.18653/v1/2023.findings-emnlp.620 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p1.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-B](https://arxiv.org/html/2603.07379v1#S2.SS2.p2.1 "II-B Retrieval-Augmented Generation ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B2](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS2.p1.1 "IV-B2 Iterative Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E1](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS1.p1.1 "IV-E1 Retrieval Depth vs Cost ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E3](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS3.p1.1 "IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.3.2.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[1st item](https://arxiv.org/html/2603.07379v1#S6.I2.i1.p1.4 "In VI-B Retrieve-Reflect-Refine Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.3.2.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[83\]Y. Shen et al. (2023)HuggingGPT: solving AI tasks with chatgpt and its friends in hugging face.
External Links: 2303.17580,
[Link](https://arxiv.org/abs/2303.17580 "")Cited by: [§IV-A2](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS2.p1.1 "IV-A2 Planner–Executor Architectures ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.5.4.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[84\]W. Shi, M. Xia, A. R. Fabbri, L. Zettlemoyer, and R. Das (2024)Trusting your evidence: hallucinate less with context-aware decoding.
In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics,
pp. 1234–1249.
Cited by: [§III-A](https://arxiv.org/html/2603.07379v1#S3.SS1.p4.1 "III-A Limitations of Standard RAG Pipelines ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[85\]X. Shi, M. Zheng, and Q. Lou (2026)Learning latency-aware orchestration for parallel multi-agent systems.
arXiv preprint arXiv:2601.10560.
Cited by: [§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p3.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VIII-C](https://arxiv.org/html/2603.07379v1#S8.SS3.p1.1 "VIII-C Deployment Implications and the Research Gap ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[86\]N. Shinn, B. Labash, A. Gopinath, K. Narasimhan, and S. Yao (2023)Reflexion: language agents with verbal reinforcement learning.
arXiv preprint arXiv:2303.11366.
External Links: [Link](https://arxiv.org/abs/2303.11366 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-C](https://arxiv.org/html/2603.07379v1#S2.SS3.p2.1 "II-C Tool-Augmented and Agentic LLMs ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-E](https://arxiv.org/html/2603.07379v1#S2.SS5.p2.1 "II-E Memory-Augmented Systems ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C2](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS2.p1.1 "IV-C2 Reflection & Tree-Based Exploration ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C](https://arxiv.org/html/2603.07379v1#S4.SS3.p1.1 "IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p2.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.4.3.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[1st item](https://arxiv.org/html/2603.07379v1#S6.I7.i1.p1.3 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[87\]A. Singh, A. Ehtesham, S. Kumar, and T. T. Khoei (2025)Agentic retrieval-augmented generation: a survey on agentic rag.
arXiv preprint arXiv:2501.09136.
Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p3.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-A](https://arxiv.org/html/2603.07379v1#S5.SS1.p1.1 "V-A Planner Module ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V](https://arxiv.org/html/2603.07379v1#S5.p1.1 "V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[88\]M. D. Skarlinski, S. Cox, J. M. Laurent, J. D. Braza, M. M. Hinks, M. J. Hammerling, M. Ponnapati, S. G. Rodriques, and A. D. White (2024)Language agents achieve superhuman synthesis of scientific knowledge.
arXiv preprint arXiv:2409.13740.
Cited by: [§VIII-A](https://arxiv.org/html/2603.07379v1#S8.SS1.p2.1 "VIII-A Domain-Specific Implementations ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[89\]H. Trivedi, N. Balasubramanian, T. Khot, and A. Sabharwal (2023)Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions.
In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 10014–10037.
Cited by: [§III-A](https://arxiv.org/html/2603.07379v1#S3.SS1.p3.1 "III-A Limitations of Standard RAG Pipelines ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[90\]H. Trivedi, N. Balasubramanian, T. Khot, and A. Sabharwal (2023)Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions.
In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), Long Papers,
External Links: [Link](https://aclanthology.org/2023.acl-long.557/ "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p1.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p3.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-B2](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS2.p1.1 "IV-B2 Iterative Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C1](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS1.p1.1 "IV-C1 Chain-of-Thought & ReAct-Style ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E1](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS1.p1.1 "IV-E1 Retrieval Depth vs Cost ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E3](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS3.p1.1 "IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.3.2.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[1st item](https://arxiv.org/html/2603.07379v1#S6.I3.i1.p1.3 "In VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-C](https://arxiv.org/html/2603.07379v1#S6.SS3.p1.1 "VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.4.3.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-A](https://arxiv.org/html/2603.07379v1#S9.SS1.p1.1 "IX-A Retrieval Drift and Query Misalignment ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[91\]W. M. P. van der Aalst, A. H. M. ter Hofstede, et al. (2002)Workflow patterns: on the expressive power of petri-net-based workflow languages.
In Proceedings of the Fourth Workshop on the Practical Use of Coloured Petri Nets and CPN Tools (CPN 2002),
External Links: [Link](https://research.tue.nl/en/publications/workflow-patterns-on-the-expressive-power-of-petri-net-based-work/ "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p3.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI](https://arxiv.org/html/2603.07379v1#S6.p1.1 "VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[92\]A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017)Attention is all you need.
In Advances in Neural Information Processing Systems (NeurIPS),
Vol. 30.
External Links: [Link](https://arxiv.org/abs/1706.03762 "")Cited by: [§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p1.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[93\]H. Wang et al. (2024)CL-bench: a contamination-aware context learning benchmark for rag.
arXiv preprint arXiv:2406.XXXXX.
External Links: [Link](https://arxiv.org/abs/2406.XXXXX "")Cited by: [§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p2.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[94\]L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, W. X. Zhao, Z. Wei, and J. Wen (2024)A survey on large language model based autonomous agents.
Frontiers of Computer Science18 (6),  pp. 186345.
External Links: [Link](https://arxiv.org/abs/2308.11432 "")Cited by: [§X](https://arxiv.org/html/2603.07379v1#S10.p1.1 "X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-C](https://arxiv.org/html/2603.07379v1#S2.SS3.p2.1 "II-C Tool-Augmented and Agentic LLMs ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[95\]L. Wang et al. (2023)Plan-and-solve prompting: improving zero-shot chain-of-thought reasoning by large language models.
In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), Long Papers,
External Links: [Link](https://aclanthology.org/2023.acl-long.147/ "")Cited by: [§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p2.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C1](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS1.p1.1 "IV-C1 Chain-of-Thought & ReAct-Style ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-A](https://arxiv.org/html/2603.07379v1#S6.SS1.p1.1 "VI-A Plan-Then-Retrieve Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.2.1.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[96\]Z. Wang, J. Araki, Z. Jiang, M. R. Parvez, and G. Neubig (2023)Learning to filter context for retrieval-augmented generation.
External Links: 2311.08377,
[Link](https://arxiv.org/abs/2311.08377 "")Cited by: [§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p1.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E1](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS1.p1.1 "IV-E1 Retrieval Depth vs Cost ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[97\]J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou (2022)Chain-of-thought prompting elicits reasoning in large language models.
In Advances in Neural Information Processing Systems (NeurIPS),
Vol. 35.
External Links: [Link](https://arxiv.org/abs/2201.11903 "")Cited by: [§II-A](https://arxiv.org/html/2603.07379v1#S2.SS1.p1.1 "II-A Large Language Models ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C1](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS1.p1.1 "IV-C1 Chain-of-Thought & ReAct-Style ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C](https://arxiv.org/html/2603.07379v1#S4.SS3.p1.1 "IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[98\]T. Wei, T.-W. Li, Z. Liu, X. Ning, Z. Yang, J. Zou, Z. Zeng, R. Qiu, X. Lin, D. Fu, Z. Li, M. Ai, D. Zhou, W. Bao, Y. Li, G. Li, C. Qian, Y. Wang, X. Tang, and Y. Xiao (2026)Agentic reasoning for large language models.
External Links: 2601.12538,
[Link](https://arxiv.org/abs/2601.12538 "")Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S7.I1.i2.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[3rd item](https://arxiv.org/html/2603.07379v1#S7.I1.i3.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-A](https://arxiv.org/html/2603.07379v1#S7.SS1.p1.1 "VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p1.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C1](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS1.p1.1 "VII-C1 Layer 1: Component-Level Assessment ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C2](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS2.p1.1 "VII-C2 Layer 2: Trajectory-Level Coherence ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C3](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS3.p1.1 "VII-C3 Layer 3: System-Level Outcome ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-D](https://arxiv.org/html/2603.07379v1#S7.SS4.p2.1 "VII-D Systemic Evaluation Gaps ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.4.3.3.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.5.4.4.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII](https://arxiv.org/html/2603.07379v1#S7.p3.1 "VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[99\]Q. Wu et al. (2023)AutoGen: enabling next-gen llm applications via multi-agent conversation.
arXiv preprint arXiv:2308.08155.
External Links: [Link](https://arxiv.org/abs/2308.08155 "")Cited by: [§IV-A3](https://arxiv.org/html/2603.07379v1#S4.SS1.SSS3.p1.1 "IV-A3 Multi-Agent RAG Systems ‣ IV-A Architectural Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.6.5.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[1st item](https://arxiv.org/html/2603.07379v1#S6.I5.i1.p1.2 "In VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-E](https://arxiv.org/html/2603.07379v1#S6.SS5.p1.1 "VI-E Multi-Agent Collaboration Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-G](https://arxiv.org/html/2603.07379v1#S6.SS7.p1.1 "VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.6.5.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.8.7.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[100\]G. Xiong, Q. Jin, Z. Lu, and A. Zhang (2024)Benchmarking retrieval-augmented generation for medicine.
In Association for Computational Linguistics,
Bangkok, Thailand.
Cited by: [§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p1.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.2.1.4.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[101\]B. Xu, Z. Peng, B. Lei, S. Mukherjee, Y. Liu, and D. Xu (2023)ReWOO: decoupling reasoning from observations for efficient augmented language models.
arXiv preprint arXiv:2305.18323.
External Links: [Link](https://arxiv.org/abs/2305.18323 "")Cited by: [3rd item](https://arxiv.org/html/2603.07379v1#S6.I3.i3.p1.1 "In VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[6th item](https://arxiv.org/html/2603.07379v1#S6.I3.i6.p1.1 "In VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[5th item](https://arxiv.org/html/2603.07379v1#S6.I4.i5.p1.1 "In VI-D Tool-Augmented Retrieval Loop Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-C](https://arxiv.org/html/2603.07379v1#S9.SS3.p1.1 "IX-C Tool Misuse and Cascading Errors ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[102\]S. Xu, W. Hao, and T. Lu (2025)KA-rag: integrating knowledge graphs and agentic retrieval-augmented generation for an intelligent educational question-answering model.
Applied Sciences15 (12547).
Cited by: [§V-B](https://arxiv.org/html/2603.07379v1#S5.SS2.p1.1 "V-B Retrieval Engine ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[103\]Z. Xu, Z. Liu, Y. Yan, S. Wang, S. Yu, Z. Zeng, C. Xiao, Z. Liu, G. Yu, and C. Xiong (2024)ActiveRAG: autonomously knowledge assimilation and accommodation through retrieval-augmented agents.
External Links: 2402.13547,
[Link](https://arxiv.org/abs/2402.13547 "")Cited by: [§IV-B3](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS3.p1.1 "IV-B3 Self-Refining Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[104\]U. Yadav, S. Niroula, G. K. Gupta, and B. Yadav (2025)Exploring secure machine learning through payload injection and fgsm attacks on resnet-50.
In 2025 IEEE Silicon Valley Cybersecurity Conference (SVCC),
External Links: [Document](https://dx.doi.org/10.1109/SVCC.2025.11133652 "")Cited by: [§IX-C](https://arxiv.org/html/2603.07379v1#S9.SS3.p2.1 "IX-C Tool Misuse and Cascading Errors ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[105\]J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. R. Narasimhan, and O. Press (2024)SWE-agent: agent-computer interfaces enable automated software engineering.
In Advances in Neural Information Processing Systems,
Vol. 37.
Cited by: [§V-C](https://arxiv.org/html/2603.07379v1#S5.SS3.p2.1 "V-C Reasoning Engine (The Controller) ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VIII-A](https://arxiv.org/html/2603.07379v1#S8.SS1.p3.1 "VIII-A Domain-Specific Implementations ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[106\]Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. W. Cohen, R. Salakhutdinov, and C. D. Manning (2018)HotpotQA: a dataset for diverse, explainable multi-hop question answering.
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP),
External Links: [Link](https://aclanthology.org/D18-1259/ "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p1.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p1.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§III-B](https://arxiv.org/html/2603.07379v1#S3.SS2.p1.1 "III-B Need for Iterative Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[4th item](https://arxiv.org/html/2603.07379v1#S6.I1.i4.p1.1 "In VI-A Plan-Then-Retrieve Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[4th item](https://arxiv.org/html/2603.07379v1#S6.I3.i4.p1.1 "In VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[107\]S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, and K. Narasimhan (2024)Tree of thoughts: deliberate problem solving with large language models.
In Advances in Neural Information Processing Systems (NeurIPS),
Vol. 36.
External Links: [Link](https://arxiv.org/abs/2305.10601 "")Cited by: [§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p3.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C2](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS2.p1.1 "IV-C2 Reflection & Tree-Based Exploration ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C](https://arxiv.org/html/2603.07379v1#S4.SS3.p1.1 "IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E2](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS2.p1.1 "IV-E2 Planning Complexity vs Latency ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[108\]S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2023)ReAct: synergizing reasoning and acting in language models.
In International Conference on Learning Representations (ICLR),
External Links: 2210.03629,
[Link](https://arxiv.org/abs/2210.03629 "")Cited by: [§I](https://arxiv.org/html/2603.07379v1#S1.p2.1 "I Introduction ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§X](https://arxiv.org/html/2603.07379v1#S10.p1.1 "X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§II-C](https://arxiv.org/html/2603.07379v1#S2.SS3.p1.1 "II-C Tool-Augmented and Agentic LLMs ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§III-C](https://arxiv.org/html/2603.07379v1#S3.SS3.p1.1 "III-C Emergence of Planning-Driven Retrieval ‣ III From Static RAG to Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C1](https://arxiv.org/html/2603.07379v1#S4.SS3.SSS1.p1.1 "IV-C1 Chain-of-Thought & ReAct-Style ‣ IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-C](https://arxiv.org/html/2603.07379v1#S4.SS3.p1.1 "IV-C Reasoning Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV](https://arxiv.org/html/2603.07379v1#S4.p1.1 "IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[2nd item](https://arxiv.org/html/2603.07379v1#S6.I3.i2.p1.1 "In VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI-C](https://arxiv.org/html/2603.07379v1#S6.SS3.p1.1 "VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VI](https://arxiv.org/html/2603.07379v1#S6.T6.1.4.3.5.1.1 "In VI-G Human-As-A-Tool (HITL) Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VI](https://arxiv.org/html/2603.07379v1#S6.p1.1 "VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[109\]A. Yehudai, L. Eden, A. Li, G. Uziel, Y. Zhao, R. Bar-Haim, A. Cohan, and M. Shmueli-Scheuer (2025)Survey on evaluation of LLM-based agents.
External Links: 2503.16416,
[Link](https://arxiv.org/abs/2503.16416 "")Cited by: [4th item](https://arxiv.org/html/2603.07379v1#S7.I1.i4.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C2](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS2.p1.1 "VII-C2 Layer 2: Trajectory-Level Coherence ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-C3](https://arxiv.org/html/2603.07379v1#S7.SS3.SSS3.p1.1 "VII-C3 Layer 3: System-Level Outcome ‣ VII-C Toward a Structured Agentic Evaluation Pipeline ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-D](https://arxiv.org/html/2603.07379v1#S7.SS4.p2.1 "VII-D Systemic Evaluation Gaps ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.4.3.4.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VII](https://arxiv.org/html/2603.07379v1#S7.T7.1.5.4.3.1.1 "In VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII](https://arxiv.org/html/2603.07379v1#S7.p2.1 "VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[110\]Y. Yu, L. Yao, Y. Xie, Q. Tan, J. Feng, Y. Li, and L. Wu (2026)Agentic memory: learning unified long-term and short-term memory management for large language model agents.
arXiv preprint arXiv:2601.01885.
Cited by: [§II-E](https://arxiv.org/html/2603.07379v1#S2.SS5.p3.1 "II-E Memory-Augmented Systems ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§V-D](https://arxiv.org/html/2603.07379v1#S5.SS4.p3.1 "V-D Memory Systems ‣ V Core Architectural Components ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IX-E](https://arxiv.org/html/2603.07379v1#S9.SS5.p2.1 "IX-E Memory Poisoning ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[111\]Y. Yu, L. Yao, Y. Xie, Q. Tan, J. Feng, Y. Li, and L. Wu (2026)Agentic memory: learning unified long-term and short-term memory management for large language model agents.
External Links: 2601.01885,
[Link](https://arxiv.org/abs/2601.01885 "")Cited by: [§IV-B3](https://arxiv.org/html/2603.07379v1#S4.SS2.SSS3.p1.1 "IV-B3 Self-Refining Retrieval ‣ IV-B Retrieval Strategy Taxonomy ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p3.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§IV-E3](https://arxiv.org/html/2603.07379v1#S4.SS5.SSS3.p1.1 "IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.7.6.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[112\]W. Zhang et al. (2024)DLLM-searcher: diffusion large language models for search and reasoning.
arXiv preprint arXiv:2404.XXXXX.
External Links: [Link](https://arxiv.org/abs/2404.XXXXX "")Cited by: [§VI-C](https://arxiv.org/html/2603.07379v1#S6.SS3.p1.1 "VI-C Decomposition-Based Retrieval Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[113\]Z. Zhao, Y. Dong, A. Liu, L. Zheng, D. Yin, et al. (2025)TURA: tool-augmented unified retrieval agent for ai search.
arXiv preprint arXiv:2508.04604.
Cited by: [§VIII-A](https://arxiv.org/html/2603.07379v1#S8.SS1.p1.1 "VIII-A Domain-Specific Implementations ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VIII-C](https://arxiv.org/html/2603.07379v1#S8.SS3.p2.1 "VIII-C Deployment Implications and the Research Gap ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VIII-C](https://arxiv.org/html/2603.07379v1#S8.SS3.p3.1 "VIII-C Deployment Implications and the Research Gap ‣ VIII Industry Frameworks and Real-World Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[114\]L. Zheng, W. Chiang, Y. Sheng, S. Hao, Z. Wu, S. Ba, E. Zhuang, Y. Lin, Z. Li, D. Weng, X. Xing, J. E. Gonzalez, I. Stoica, and E. P. Xing (2023)Judging LLM-as-a-judge with MT-Bench and chatbot arena.
In Advances in Neural Information Processing Systems,
Vol. 36.
Cited by: [2nd item](https://arxiv.org/html/2603.07379v1#S10.I2.i2.p1.1 "In X-B Formal Evaluation of Agentic Reasoning Quality ‣ X Open Research Challenges and Future Directions ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[115\]W. Zhong, L. Guo, et al. (2023)Enhancing large language models with long-term memory.
External Links: 2305.10250,
[Link](https://arxiv.org/abs/2305.10250 "")Cited by: [§IV-D](https://arxiv.org/html/2603.07379v1#S4.SS4.p3.1 "IV-D Memory and Context Paradigms ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE III](https://arxiv.org/html/2603.07379v1#S4.T3.1.7.6.7.1.1 "In IV-E3 Cost, Latency, and Token Economics ‣ IV-E Cross-Dimensional Trade-Off Analysis ‣ IV Taxonomy of Agentic RAG Systems ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[116\]D. Zhou et al. (2022)Least-to-most prompting enables complex reasoning in large language models.
arXiv preprint arXiv:2205.10625.
External Links: [Link](https://arxiv.org/abs/2205.10625 "")Cited by: [§II-D](https://arxiv.org/html/2603.07379v1#S2.SS4.p2.1 "II-D Multi-Hop Reasoning and Planning ‣ II Background and Foundations ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[2nd item](https://arxiv.org/html/2603.07379v1#S6.I1.i2.p1.1 "In VI-A Plan-Then-Retrieve Pattern ‣ VI Design Patterns in Agentic RAG ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[117\]K. Zhu, Y. Luo, D. Xu, Y. Yan, Z. Liu, S. Yu, R. Wang, Y. Li, N. Zhang, X. Han, Z. Liu, and M. Sun (2025)RAGEval: scenario specific RAG evaluation dataset generation framework.
In Association for Computational Linguistics,
Vienna, Austria.
Cited by: [3rd item](https://arxiv.org/html/2603.07379v1#S7.I1.i3.p1.1 "In VII-A Evaluation Dimensions for Agentic RAG ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-B](https://arxiv.org/html/2603.07379v1#S7.SS2.p1.1 "VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII-D](https://arxiv.org/html/2603.07379v1#S7.SS4.p1.1 "VII-D Systemic Evaluation Gaps ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[TABLE VIII](https://arxiv.org/html/2603.07379v1#S7.T8.1.4.3.1.1.1 "In VII-B From Static Benchmarks to Evaluation Frameworks ‣ VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"),
[§VII](https://arxiv.org/html/2603.07379v1#S7.p3.1 "VII Evaluation and Benchmarking ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").

- \[118\]W. Zou, R. Geng, B. Wang, and J. Jia (2025)PoisonedRAG: knowledge corruption attacks to retrieval-augmented generation of large language models.
In USENIX Security Symposium,
External Links: [Link](https://arxiv.org/abs/2402.07867 "")Cited by: [§IX-D](https://arxiv.org/html/2603.07379v1#S9.SS4.p2.1 "IX-D Prompt Injection in Iterative Retrieval ‣ IX Failure Modes, Safety, and Reliability Challenges ‣ SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions").


BETA

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

##### Dense vector embeddings

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

## What’s next?

Have a RAG project you want to bring to life? Join our [Discord community](https://discord.gg/qdrant) where we’re always sharing tips and answering questions on vector search and retrieval.

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