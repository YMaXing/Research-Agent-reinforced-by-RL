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

-----

Phase: [EXPLOITATION]

### Source [30]: https://galileo.ai/blog/rag-architecture

Query: How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?

Answer: RAG architecture connects LLMs to external knowledge sources at query time, retrieving relevant documents and using that context to generate grounded responses. Instead of relying on training data, it pulls from databases and sources to produce accurate, verifiable answers.

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

### Source [58]: https://medium.com/@rahulraut.techuse/introduction-to-augmenting-llms-using-retrieval-augmented-generation-rag-6530123dbb91

Query: How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?

Answer: Augments the prompt with the results of additional source knowledge. Feeds that information to the LLM. This augmentation helped the LLM in generating answers that are true to the requirements of the user, formally correct, and fact-based. After moving through the Query & Passages Stage, the ingestion process searches into the query request itself: gathering information from a pool that can include anything from databases, documents, or HTML pages to markdown files. The requirement proceeds into the Retrieve Search phase, in which relevant chunks of data are retrieved from the docs utilizing whatever advanced search techniques may apply: these could include embeddings or keyword-based models. The end aim here is to ensure only the most relevant pieces of information are retrieved for further processing.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://www.promptingguide.ai/research/rag

Query: How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?

Answer: Generation: The relevant documents are combined with the original prompt as additional context. The combined text and prompt are then passed to the model for response generation which is then prepared as the final output of the system to the user. Optimizing post-retrieval focuses on avoiding context window limits and dealing with noisy or potentially distracting information. A common approach to address these issues is re-ranking which could involve approaches such as relocation of relevant context to the edges of the prompt or recalculating the semantic similarity between the query and relevant text chunks. Prompt compression may also help in dealing with these issues.

-----

-----

Phase: [EXPLOITATION]

### Source [60]: https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c

Query: How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?

Answer: Combining Data: The chosen data segments from the database are combined with the user’s initial query, creating an expanded prompt. Generating Text: The enlarged prompt, filled with added context, is then given to the LLM, which crafts the final, context-aware response. Note that while creating the expanded prompt (with the retrieved top-k chunks) for an LLM to make an informed response generation, a strategic placement of vital information at the beginning or end of input sequences could enhance the RAG system’s effectiveness and thus make the system more performant.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What scalability and latency tradeoffs limit iterative multi-agent retrieval in production agentic RAG?</summary>

Phase: [EXPLORATION]

### Source [61]: https://arxiv.org/html/2501.09136v4

Query: What scalability and latency tradeoffs limit iterative multi-agent retrieval in production agentic RAG?

Answer: Traditional Retrieval-Augmented Generation (RAG) systems face critical challenges including scalability and latency issues. As the volume of external data sources grows, querying and ranking large datasets becomes increasingly computationally intensive. This results in significant latency, which undermines the system’s ability to provide timely responses in real-time applications. Example: In time-sensitive settings such as financial analytics or live customer support, delays caused by querying multiple databases or processing large document sets can hinder the system’s overall utility. For example, a delay in retrieving market trends during high-frequency trading could result in missed opportunities. These limitations are particularly relevant to agentic RAG, which builds on traditional RAG but introduces multi-step reasoning and iterative retrieval, exacerbating computational demands.

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://medium.com/@chinmayd49/rag-production-optimizations-and-trade-offs-a623e5834e65

Query: What scalability and latency tradeoffs limit iterative multi-agent retrieval in production agentic RAG?

Answer: In production RAG, strict latency budgets are enforced: Retrieval must be < 500–1000ms (favoring low-latency vector DBs like Redis), and Generation < 500–1000ms (using smaller, quantized LLMs and streaming). Trade-offs make slow optimizations like cross-encoder re-ranking unacceptable due to latency constraints. For secure internal use cases prioritizing accuracy over speed, larger LLMs like GPT-4 are used, accepting 5-second responses and higher costs for correctness. Production RAG requires balancing accuracy, latency, cost, and security. In low-latency chatbots, no pre- or post-retrieval steps are used to keep total time <2s, avoiding expensive processes that would increase latency.

-----

</details>

<details>
<summary>What are the primary failure modes and hallucination risks when query decomposition meets incomplete knowledge graphs in GraphRAG?</summary>

Phase: [EXPLORATION]

### Source [67]: https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/

Query: What are the primary failure modes and hallucination risks when query decomposition meets incomplete knowledge graphs in GraphRAG?

Answer: In RAG systems enhanced with knowledge graphs like GraphRAG, failure modes include the Implicit Relationship Hallucination where retrievers rely on semantic closeness, causing LLMs to hallucinate non-existent relationships if documents mention related terms without explicit links (e.g., 'Tesla,' 'Toyota,' 'Panasonic' near 'battery' leading to false partnerships). Standard RAG falters with incomplete or noisy context, forcing hallucinations or reasoning failures. Knowledge graphs address this but if incomplete, lack explicit edges means decomposed queries can't traverse missing paths, amplifying risks in multi-hop reasoning, entity ambiguity, and contradictory information. As knowledge bases grow complex with incomplete graphs, LLMs hallucinate connections or fail synthesis.

-----

-----

Phase: [EXPLORATION]

### Source [69]: https://dev.to/aws/rag-vs-graphrag-when-agents-hallucinate-answers-2mcb

Query: What are the primary failure modes and hallucination risks when query decomposition meets incomplete knowledge graphs in GraphRAG?

Answer: GraphRAG improves RAG but incomplete retrieval remains a failure mode: vector search misses scattered data, while even graph-integrated systems suffer if graphs are incomplete. Out-of-domain fabrication happens when no relevant data exists; retrieval always returns something, prompting LLM hallucinations. Research shows RAG misses info frequently, with hallucinations in fabricated statistics, precise counting, multi-hop reasoning. GraphRAG reduces but incomplete KGs lead to failures in aggregation (e.g., AVG ratings), counting amenities, multi-hop (room types/prices), as decomposed queries can't fully traverse missing graph paths.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://repositum.tuwien.at/bitstream/20.500.12708/227715/1/Dolci-2026-Towards%20LLM-KG%20Symbiosis%20for%20Reducing%20Factual%20Hallucinations-vor.pdf

Query: What are the primary failure modes and hallucination risks when query decomposition meets incomplete knowledge graphs in GraphRAG?

Answer: GraphRAG expands RAG with graph structures for higher accuracy and fewer hallucinations via KG-based retrieval. However, it adopts a closed-knowledge assumption, limited to knowledge in external sources. Real-world KGs like Wikidata or YAGO are incomplete, outdated, or insufficient, causing failure when query decomposition requires info not present, leading to hallucinations as generation can't be fully grounded.

-----

</details>

<details>
<summary>What open research directions exist for fusing agentic RAG with emerging long-context models to reduce retrieval dependency?</summary>

Phase: [EXPLORATION]

### Source [71]: https://arxiv.org/html/2501.09136v4

Query: What open research directions exist for fusing agentic RAG with emerging long-context models to reduce retrieval dependency?

Answer: The survey identifies key open research challenges related to evaluation, coordination, memory management, efficiency, and governance, outlining directions for future research. Section 12 discusses open research issues and future challenges for Agentic RAG systems. It reviews the evolution of RAG paradigms, including naïve, modular, and graph-based RAG, and their transition toward agentic systems. A principled taxonomy of Agentic RAG architectures is introduced based on agent cardinality, control structure, autonomy, and knowledge representation. The survey examines real-world applications and distills practical lessons, guiding future work on these challenges.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/

Query: What open research directions exist for fusing agentic RAG with emerging long-context models to reduce retrieval dependency?

Answer: Previous studies have mainly explored two major directions: input reduction and window extension. Input reduction reduces the length of the input context, for example by directly truncating the input, before feeding to downstream LLMs. RAG extends this direction by breaking the input into chunks and then retrieving answers to the most relevant chunks based on embedding similarity. However, because of low retrieval accuracy, LLMs could receive an incomplete context for solving the task, hurting performance. Window extension extends the context window of LLMs via fine-tuning, training the model to consume longer inputs. For example, Gemini is able to directly process 2M tokens for each input. However, when the window becomes longer even than their extended input capacities, such LLMs face limitations.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://medium.com/@infiniflowai/from-rag-to-context-a-2025-year-end-review-of-rag-03740f1a0528

Query: What open research directions exist for fusing agentic RAG with emerging long-context models to reduce retrieval dependency?

Answer: Improved long-context capabilities have not signaled RAG’s demise. Instead, they prompt deeper thinking about how the two can collaborate. For example, RAG systems can use long-context windows to hold more complete, semantically coherent retrieved chunks or to aggregate intermediate results for multi-step retrieval and reflection. This “retrieval-first, long-context containment” synergy is a key driver behind the emerging field of “Context Engineering.” It marks a shift from optimizing single “retrieval algorithms” to the systematic design of the end-to-end “retrieval-context assembly-model reasoning” pipeline. The theoretical question “Can Long Context replace RAG?” entered practical testing in 2025, with experiments in scenarios like contract reviews using long-context windows to bypass RAG retrieval issues.

-----

-----

Phase: [EXPLORATION]

### Source [74]: https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling

Query: What open research directions exist for fusing agentic RAG with emerging long-context models to reduce retrieval dependency?

Answer: Relevant papers include: Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning (Arxiv 2025). Long Context Modeling with Ranked Memory-Augmented Retrieval (Arxiv 2025). Tuning LLMs by RAG Principles: Towards LLM-native Memory (Arxiv 2025). SEAL: Scaling to Emphasize Attention for Long-Context Retrieval (Arxiv 2025). These works explore integrations like memory-augmented retrieval, KV cache compression beyond RAG, and RAG-inspired tuning for long-context handling in LLMs.

-----

</details>

<details>
<summary>How do semantic web knowledge graphs relate to GraphRAG techniques?</summary>

Phase: [EXPLORATION]

### Source [76]: https://microsoft.github.io/graphrag/

Query: How do semantic web knowledge graphs relate to GraphRAG techniques?

Answer: GraphRAG is a structured, hierarchical approach to Retrieval Augmented Generation (RAG), as opposed to naive semantic-search approaches using plain text snippets. The GraphRAG process involves extracting a knowledge graph out of raw text, building a community hierarchy, generating summaries for these communities, and then leveraging these structures when performing RAG-based tasks. GraphRAG uses knowledge graphs to provide substantial improvements in question-and-answer performance when reasoning about complex information. Retrieval-Augmented Generation (RAG) is a technique to improve LLM outputs using real-world information. This technique is an important part of most LLM-based tools and the majority of RAG approaches use vector similarity as the search technique, which we call Baseline RAG.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://www.gooddata.com/blog/from-rag-to-graphrag-knowledge-graphs-ontologies-and-smarter-ai/

Query: How do semantic web knowledge graphs relate to GraphRAG techniques?

Answer: GraphRAG is an evolution of the traditional RAG approach that explicitly incorporates a knowledge graph into the retrieval process. In GraphRAG, when a user asks a question, the system doesn’t just do a vector similarity search over text; it also queries the knowledge graph for relevant entities and relationships. GraphRAG is about integrating this graph-based knowledge into the RAG pipeline. By doing so, we aim to overcome the multi-source, ambiguity, and reasoning issues. What if, instead of giving the AI system just a pile of documents, we also gave it a knowledge graph (i.e. a network of entities and their relationships) as a scaffold for reasoning? If RAG retrieval could return not just text based on similarity search, but a set of interconnected facts, the AI system could follow those connections to produce a more insightful answer. Before we get into how GraphRAG works, though, let’s clarify what we mean by knowledge graphs and ontologies — the building blocks of this approach.

-----

-----

Phase: [EXPLORATION]

### Source [79]: https://medium.com/@zilliz_learn/graphrag-explained-enhancing-rag-with-knowledge-graphs-3312065f99e1

Query: How do semantic web knowledge graphs relate to GraphRAG techniques?

Answer: Unlike a baseline RAG that uses a vector database to retrieve semantically similar text, GraphRAG enhances RAG by incorporating knowledge graphs (KGs). Knowledge graphs are data structures that store and link related or unrelated data based on their relationships. A GraphRAG pipeline usually consists of two fundamental processes: indexing and querying. The indexing process includes four key steps. To address such challenges, Microsoft Research introduced GraphRAG, a brand-new method that augments RAG retrieval and generation with knowledge graphs. Hierarchical Clustering: GraphRAG uses the Leiden technique to perform hierarchical clustering on the initial knowledge graphs. Leiden is a community detection algorithm that can effectively discover community structures within the graph. Entities in each cluster are assigned to different communities for more in-depth analysis.

-----

-----

Phase: [EXPLORATION]

### Source [80]: https://weaviate.io/blog/graph-rag

Query: How do semantic web knowledge graphs relate to GraphRAG techniques?

Answer: GraphRAG has recently become an umbrella term referring broadly to RAG approaches where the retrieval component specifically leverages knowledge graphs. Under this umbrella, numerous methods have emerged, each differing in how they utilize graph-based retrieval to enhance LLM responses. Among these, the GraphRAG implementation from Microsoft has risen as one of the most popular and widely-adopted approaches. When a user asks a question, the system identifies key entities (people, places, concepts, etc.) that are semantically related to the query. Knowledge Graph Navigation: These identified entities act as entry points into your knowledge graph, allowing the system to: Find connected entities (relationships), Extract relevant attributes and properties, Pull in contextual information from community reports or other sources. Behind the scenes, the system then executes a Cypher query that traverses the knowledge graph, following relationships between entities and extracting contextually relevant information.

-----

</details>

<details>
<summary>What symbolic AI lessons can enhance agentic RAG reasoning loops?</summary>

Phase: [EXPLORATION]

### Source [81]: https://arxiv.org/html/2407.08516v5

Query: What symbolic AI lessons can enhance agentic RAG reasoning loops?

Answer: Current agentic reasoning approaches emulate human reasoning steps explicitly. For instance, when an agent receives a user’s request, it retrieves similar cases and enhances its actions through in-context learning, and for ambiguous requests, the agent prompts the LLM to clarify and rewrite the request in various forms. This process involves extracting vectors for each rewritten request and performing multi-vector retrieval, improving context understanding and generative performance but increasing computational load. A vector-centric perspective, utilizing encoder-decoder architectures such as GritLM that prompt generative models for instructional text encoding/vectorization, implicit neural reasoners that extend transformers with causal relation graphs for enhanced long-range reasoning. The emergent abilities of LLMs, such as contextual understanding, sequential reasoning, goal reformulation, and task decomposition, are surged by over-parameterized architectures and extensive pre-training corpora. Combining well-designed rules with the emergent abilities of LLMs enables agents to create and follow complex workflows, known as agentic workflows. By prompting large language models with instructions like “let’s think step by step”, these models analogise human’s reasoning processes and can exhibit logical and mathematical reasoning, thereby enhancing their structured reasoning skills. This agentic approach allows LLMs to not only process but also proactively generate structured, logical, and adaptive reasoning pathways, significantly improving their problem-solving. Promising directions such as neuro-vector-symbolic architectures and program-proof-of-thoughts (P2oT) prompting are on the horizon, potentially enhancing the agentic reasoning capabilities of AI further.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://builder.aws.com/content/2uYUowZxjkh80uc0s2bUji0C9FP/from-logic-to-learning-the-future-of-ai-lies-in-neuro-symbolic-agents

Query: What symbolic AI lessons can enhance agentic RAG reasoning loops?

Answer: Neuro-symbolic AI fuses these paradigms, creating systems that can both reason and learn — systems that can: Understand language using neural networks. Ground understanding in structured knowledge bases. Execute logic using explicit rules and policy frameworks. Explain decisions through symbolic traces while adapting to new inputs through learned representations. In the agentic context, this enables software agents that can: Interpret user goals flexibly (neural). Plan and make decisions deterministically (symbolic). Reflect on outcomes and evolve (neuro-symbolic feedback loops). Symbolic reasoning provides transparency, repeatability, and deterministic logic — essential for domains that require trust, compliance, and interpretability. But symbolic systems alone can be rigid, unable to adapt or generalize beyond their predefined rules. Conversely, neural models like LLMs offer fluency, adaptability, and generalization from vast amounts of unstructured data. They can infer context, handle ambiguity, and generate language with human-like flexibility. Yet they lack grounding, struggle with long-term memory, and often produce unverifiable or hallucinated output. The future of AI lies in Agentic AI systems composed of collaborative, domain-specialized agents. Each agent acts as an expert—but not in the brittle sense of legacy expert systems. Instead, they are neuro-symbolic agents: blending the reasoning of symbolic logic with the adaptive capabilities of generative models. This convergence offers a new path forward. Enterprises can build intelligent systems that reason like experts, adapt like humans, and collaborate like teams—all while staying grounded, auditable, and purpose-driven.

-----

-----

Phase: [EXPLORATION]

### Source [83]: https://www.sciencedirect.com/science/article/abs/pii/S1574013726000110

Query: What symbolic AI lessons can enhance agentic RAG reasoning loops?

Answer: Meta-cognition in neurosymbolic AI agents—the ability to monitor, evaluate, and adaptively control cognitive processes—enhances neuro-symbolic system reasoning. Despite being crucial for human-like intelligence, it remains severely underexplored, appearing in only 5% of reviewed papers, even though meta-cognitive capabilities often contribute more to performance than sophisticated integration patterns. Despite impressive capabilities, neural and symbolic approaches face fundamental limitations independently. Neural methods excel at pattern recognition and adaptation but lack interpretability, struggle with systematic reasoning, and require extensive training data. Symbolic approaches offer explicit rule-based reasoning and transparency but demonstrate brittleness in uncertain environments and limited learning capabilities. These complementary strengths suggest a natural synergy through neuro-symbolic AI. AI agents—autonomous software programs—perceive environments, reason, plan, and execute actions effectively. Recent advances (2024–2025) enable agents to coordinate in multi-agent environments, maintain long-term context through narrative memory, and employ refined chain-of-thought prompting with external tools.

-----

-----

Phase: [EXPLORATION]

### Source [85]: https://arxiv.org/html/2502.11269v1

Query: What symbolic AI lessons can enhance agentic RAG reasoning loops?

Answer: Techniques like RAG, GraphRAG, and Seq2Seq models (including LLMs, e.g., GPT) align with this method due to their reliance on neural encodings of symbolic data (e.g., text or structured information) to perform complex transformations before outputting results in symbolic form. Similarly, semantic parsing benefits from this framework by leveraging NNs to uncover latent patterns in symbolic inputs and generating interpretable symbolic conclusions. For instance, RAG-Logic proposes a dynamic example-based framework using RAG to enhance logical reasoning capabilities by integrating relevant, contextually appropriate examples. It first encodes symbolic input (e.g., logical premises) into neural representations using the RAG knowledge base search module. Neural processing occurs through the framework, resulting in symbolic outputs that improve reasoning. Generative AI is advancing at a remarkable pace, addressing increasingly complex challenges through the integration of diverse methodologies. A key development is the combination of NNs with symbolic reasoning, resulting in hybrid systems that leverage both strengths.

-----

</details>

<details>
<summary>How is RAG applied in robotics for real-time decisions?</summary>

Phase: [EXPLORATION]

### Source [86]: https://arxiv.org/html/2409.12294v1

Query: How is RAG applied in robotics for real-time decisions?

Answer: RAG systems for Robotics. Retrieval Augmented Generation (RAG) systems enhance language model predictions by retrieving relevant information from external databases [38, 39]. For example, employs RAG to collect exemplars for solving sub-tasks with web agents, while retrieves driving experiences from a database for autonomous vehicle planning. In robotics, explores retrieval for deep RL agents, but it does not use LLMs, limiting its adaptability and scalability. employs a policy retriever to extract robotic policies from a large-scale policy memory. We evaluate the performance of RAG-Modulo in AlfWorld and BabyAI [1, 15] benchmarks, depicted in Fig. 3. These benchmarks include several features representative of challenges in robot decision-making, thereby making them suitable benchmarks for evaluating RAG-Modulo. For instance, both benchmarks include a suite of sequential tasks that need to be performed by situated agents. The environments are partially observable to the agent, requiring the agent to explore, navigate and interact with objects to complete tasks described in natural language. Solving these tasks require reasoning over long-horizon in presence of a sparse reward signal, which is challenging for planning, RL and LLM-based decision-making algorithms [1, 2, 15]. To address these gaps, we propose RAG-Modulo: a framework which augments a language model with a memory that stores past interactions, retrieving relevant experience at each step of the task to guide robot decision-making.

-----

-----

Phase: [EXPLORATION]

### Source [87]: https://arxiv.org/html/2510.05547v1

Query: How is RAG applied in robotics for real-time decisions?

Answer: Retrieval-augmented generation (RAG) in NLP improves grounding by combining a language model with an external knowledge corpus. Robotics researchers have begun adapting these ideas for compliant, knowledge-grounded planning. SayComply retrieves compliance rules and manuals to constrain LLM outputs, improving task correctness and adherence to operational procedures. Similarly, behavior tree embeddings capture structured task-level knowledge to support retrieval, task comparison, and indexing, but they do not integrate real-time perception or low-level control for safety-aware execution. Other related works include structured affordance retrieval, multi-step plan synthesis with semantic grounding, and Inner Monologue-style online corrections, which improve execution reliability but Retrieval-augmented generation (RAG), originally proposed for natural language processing (NLP), enables dynamic grounding of model outputs in external, updatable knowledge sources. Recently, robotics researchers have begun exploring retrieval-based compliance frameworks. SayComply, for instance, uses retrieval to enforce adherence to operational manuals in field robotics, demonstrating improved compliance and correctness. However, such approaches often stop at high-level compliance and do not integrate low-level metric grounding, perception-driven plan validation, or safety gating for execution. In this paper, we bridge these gaps by introducing a RAG-enabled robotic manipulation pipeline–called ARRC (advanced reasoning robot control)–that unifies perception, retrieval, and safe plan execution. We deploy this system on a UFactory xArm 850 equipped with a RealSense D435 and a Dynamixel gripper, integrating retrieval of robot-centric safety heuristics and procedural templates at inference time. This design offers both adaptability and reliability, enabling the injection of new task knowledge or safety rules without retraining. Our contributions are as follows: We develop a hybrid VLA architecture integrating RAG for dynamic injection of procedural and safety knowledge.

-----

-----

Phase: [EXPLORATION]

### Source [88]: https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/

Query: How is RAG applied in robotics for real-time decisions?

Answer: Innovative solutions to take on robotics, edge, and vision AI challenges GPU-accelerated advances in AI perception, simulation, and software Bring the power of NVIDIA AI to the edge for real-time decision-making solutions Transform data into valuable insights using vision AI AI-enhanced vehicles are transforming the future of mobility For reasoning-based AV systems Explore high-fidelity sensor simulation for safe autonomous vehicle development Enables vehicles to be L4-ready Essential data center tools for safe autonomous vehicle development Develop automated driving functions and immersive in-cabin experiences State-of-the-art system for AV safety, from the cloud to the car # What Is Retrieval-Augmented Generation (RAG)? The evolution of AI chatbots to AI assistants and then AI agents marks a significant milestone for enterprises and aiding the digital workforce. These generative AI-powered software applications use RAG to query databases in real time, delivering responses that are relevant to the context of the user’s query and enriched with the most current information available, without the need for retraining the underlying LLM. This advancement profoundly impacts user engagement, particularly in industries such as customer service, education, and entertainment, where the demand for immediate, accurate, and informed responses is paramount. Industry applications that require AI-driven insights grounded in real-time, reliable data include: Transform workflows with immersive, scalable interactions in virtual environments.

-----

</details>

<details>
<summary>What multi-agent system trends complement agentic RAG designs?</summary>

Phase: [EXPLORATION]

### Source [89]: https://www.okta.com/identity-101/agentic-rag-architecture/

Query: What multi-agent system trends complement agentic RAG designs?

Answer: ## Future trends in agentic RAG

Emerging research and early production systems are exploring recursive and self-evaluating agents. These systems can assess the quality of their own outputs, identify gaps, and trigger additional retrieval or reasoning steps to fill them. As agent behavior evolves, so do its access requirements, which means lifecycle governance needs to account for drift, not just initial provisioning.

Federated multi-agent systems allow agents from different teams or organizations to collaborate through emerging interoperability protocols, extending the identity and authorization problem across organizational boundaries. How you verify an external agent's identity and limit what it can access is a question most enterprises haven't answered yet. [...] ### Multi-agent coordination

Multi-agent RAG distributes work across specialized agents coordinated via an orchestration layer. For example, the system might include a planning agent that decomposes goals, a retrieval agent, a verification agent, and an execution agent. While this example enables parallelization, it also introduces the risk of propagated errors: mistakes in intermediate outputs can cascade through subsequent agents and retrieval steps. Effective debugging requires tracing the full chain of decisions, not just identifying a single incorrect output.

-----

-----

Phase: [EXPLORATION]

### Source [90]: https://arxiv.org/html/2501.09136v4

Query: What multi-agent system trends complement agentic RAG designs?

Answer: While multi-agent collaboration offers significant potential, it is a less predictable design pattern compared to more mature workflows like Reflection and Tool Use. Nevertheless, emerging frameworks such as AutoGen, Crew AI, and LangGraph are providing new avenues for implementing effective multi-agent solutions.

Figure 10: An Overview of MultiAgent [...] Multi-agent collaboration  is a key design pattern in agentic workflows that enables task specialization and parallel processing. Agents communicate and share intermediate results, ensuring the overall workflow remains efficient and coherent. By distributing subtasks among specialized agents, this pattern improves the scalability and adaptability of complex workflows. Multi-agent systems allow developers to decompose intricate tasks into smaller, manageable subtasks assigned to different agents. This approach not only enhances task performance but also provides a robust framework for managing complex interactions. Each agent operates with its own memory and workflow, which can include the use of tools, reflection, or planning, enabling dynamic and collaborative problem-solving (see Figure [...] ### 5.2 Multi-Agent Agentic RAG Systems:

Multi-Agent RAG represents a modular and scalable evolution of single-agent architectures, designed to handle complex workflows and diverse query types by leveraging multiple specialized agents (as shown in Figure 17). Instead of relying on a single agent to manage all tasks—reasoning, retrieval, and response generation—this system distributes responsibilities across multiple agents, each optimized for a specific role or data source.

Figure 17: An Overview of Multi-Agent Agentic RAG Systems

##### Workflow

-----

-----

Phase: [EXPLORATION]

### Source [91]: https://www.ibm.com/think/topics/agentic-rag

Query: What multi-agent system trends complement agentic RAG designs?

Answer: Agentic workflows can consist of either one AI agent or multiagent systems that combine several agents together.

Multiagent systems encourage multiple AI models to collaborate and check each other’s work. [...] Agentic RAG works by incorporating one or more types of AI agents into RAG systems. For example, an agentic RAG system might combine multiple information retrieval agents, each specialized in a certain domain or type of data source. One agent queries external databases while another can comb through emails and web results.

Agentic AI frameworks, such as LangChain and LlamaIndex, and the orchestration framework LangGraph can be found on GitHub. With them, it is possible to experiment with agentic architectures for RAG at minimal costs.

-----

-----

Phase: [EXPLORATION]

### Source [93]: https://weaviate.io/blog/what-is-agentic-rag

Query: What multi-agent system trends complement agentic RAG designs?

Answer: Multi-agent RAG Systems

As you can guess, the single-agent system also has its limitations because it's limited to only one agent with reasoning, retrieval, and answer generation in one. Therefore, it is beneficial to chain multiple agents into a multi-agent RAG application.

For example, you can have one master agent who coordinates information retrieval among multiple specialized retrieval agents. For instance, one agent could retrieve information from proprietary internal data sources. Another agent could specialize in retrieving information from your personal accounts, such as email or chat. Another agent could also specialize in retrieving public information from web searches.

With the rise and popularity of AI agent systems, many different frameworks are evolving for implementing agentic RAG, such as LlamaIndex, LangGraph, or CrewAI.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="advanced-rag-retrieval-cross-encoders-reranking-towards-data.md">
<details>
<summary>Advanced RAG Retrieval: Cross-Encoders & Reranking</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/>

# Advanced RAG Retrieval: Cross-Encoders & Reranking

A deep-dive and practical guide to cross-encoders, advanced techniques, and why your retrieval pipeline deserves a second pass.

https://towardsdatascience.com/wp-content/uploads/2026/04/bi-encoder-vs-cross-encoder-scaled-1.jpg
Image generated by Author using Gemini Nano Banana

Semantic search, or embedding-based retrieval, has been a key component within many AI applications. Yet, a surprising number of applications I’ve seen still don’t do reranking, despite the relative ease of implementation.

If you’ve ever built a RAG pipeline and thought “the results are _okay_ but not _great_”, the solution isn’t always to choose a better embedding model. Instead, you should consider including a reranking step, and **cross-encoders** are probably your best bet.

**This article covers what cross-encoders are, why they’re so good at reranking, how to fine-tune them on your own data, and some ideas for pushing them even further.**

All the code is available at [https://github.com/ianhohoho/cross-encoder-and-reranking-demo](https://github.com/ianhohoho/cross-encoder-and-reranking-demo).

---

## The Retrieval Problem

Most semantic search systems use **bi-encoders**. They encode your query into a vector, encode your documents into vectors, and find the closest matches. It’s a fast operation that scales and gives you moderately decent results most of the time.

However, **encoding the query and document independently throws away the possibility of interaction signals**. And that’s because the embedding model has to compress all semantics into a single vector _before_ it ever compares anything.

Here’s a concrete example. You search “cheap hotels in Tokyo” and get back:

- “Luxury hotels in Tokyo starting at $500/night”
- “Budget hostels in Tokyo at $30/night”
- “Cheap flights to Tokyo”

Result #1 scores high because it matches “hotels” and “Tokyo.” Result #3 matches “cheap” and “Tokyo.” But result #2 — the one you actually want — might rank below both because “cheap” and “budget” aren’t that close in embedding space.

A bi-encoder can’t reason about the _relationship_ between “cheap” in your query and “$500/night” in the document. It just sees token overlap in the compressed vectors. **A cross-encoder ‘reads’ the query and document together at one go**, so it catches that $500/night contradicts “cheap” and ranks it lower. At least, that’s the layman way of explaining it.

## The Two-Stage Pattern

In the real world, we can use a combination of bi-encoders and cross-encoders to achieve the most optimal retrieval and relevance performance.

- **Stage 1**: Fast, approximate retrieval. Cast a wide net to achieve high recall with a bi-encoder or BM25. Get your top k candidates.
- **Stage 2**: Precise reranking. Run a cross-encoder over those candidates in a pair-wise manner. Get a much better ranking that directly measures relevance.

It’s actually already quite a standard pattern in production, at least for teams at the frontier:

- Cohere offers [Rerank](https://docs.cohere.com/docs/rerank) as a standalone API — designed to sit on top of any first-stage retrieval. Their `rerank-v4.0-pro` is one such [example](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-cohere-rerank-4-0-in-microsoft-foundry/4477076).
- Pinecone has built-in reranking with hosted models, describing it as [“a two-stage vector retrieval process to improve the quality of results”](https://docs.pinecone.io/guides/search/rerank-results). One of the multilingual models they offer is `bge-reranker-v2-m3` , for which the HuggingFace card can be found [here](https://huggingface.co/BAAI/bge-reranker-v2-m3).
- In fact, this practice has been around for a pretty long time already. Google announced back in 2019 that [BERT is used to re-rank search results](https://blog.google/products/search/search-language-understanding-bert/) by reading queries & snippets together to judge relevance.
- LangChain and LlamaIndex both have built-in reranking steps for RAG pipelines.

### Why Not Just Use Cross-Encoders for Everything?

Well, it’s a compute problem.

A **bi-encoder** encodes all your documents once at index time, and so the upfront complexity is O(n). At query time, you just encode the query and conduct an approximate nearest-neighbor lookup. With FAISS or any ANN index, that’s effectively O(1).

A **cross-encoder** can’t precompute anything. It needs to see the query and document _together_. So at query time, it runs a full transformer forward pass for every candidate of (query, document).

At the risk of failing my professors who used to teach about complexity, each pass costs O(L × (s\_q + s\_d)² × d), because that’s L layers, the combined sequence length squared, times the hidden dimension.

For a corpus of 1M documents, that’s 1M forward passes per query. Even with a small model like MiniLM (6 layers, 384 hidden dim), you’re looking at a silly amount of of GPU time per query so that’s obviously a non-starter.

But what if we narrowed it down to about 100+ candidates? On a single GPU, that would probably take just several hundred milliseconds.

That’s why two-stage retrieval works: retrieve cheaply and then rerank precisely.

## How Bi-Encoders and Cross-Encoders Work

### Bi-Encoder Architecture

A **bi-encoder** uses two transformer encoders, with both query and document producing a fixed-size embedding.

> Query → \[Transformer\] → query\_embedding (768-dim vector)
>
> ↓
>
> cosine similarity
>
> ↑
>
> Doc → \[Transformer\] → doc\_embedding (768-dim vector)

The similarity score is just cosine similarity between the two vectors, and it’s fast because you can precompute all document embeddings and use [approximate nearest-neighbor (ANN) search](https://www.elastic.co/blog/understanding-ann).

However, the key limitation is that the model compresses all meaning into one vector _before_ any comparison happens. Query and document tokens never interact, and so it’s akin to summarising two essays separately and then comparing between them. You lose all sorts of nuances as a result.

### Cross-Encoder Architecture

A **cross-encoder** takes a different approach. It concatenates the query and document into **one input sequence** before feeding it through a single transformer, something like that

> Input: \[CLS\] query tokens \[SEP\] document tokens \[SEP\]
>
> ↓
>
> \[Transformer — full self-attention across ALL tokens\]
>
> ↓
>
> \[CLS\] → Linear Head → sigmoid → relevance score (0 to 1)

Every token in the query can attend to every token in the document. Consequently, the output isn’t an embedding, but a directly produced relevance score between the query and documents.

### How Cross-Encoders Are Trained

Why not train a cross-encoder from scratch? Well, just like the LLMs themselves, training a transformer from scratch requires massive compute and data. BERT was trained on 3.3 billion words so… you probably don’t want to redo that.

Instead, you can use **transfer learning**. Take a pre-trained transformer that already understands language  (grammar, semantics, word relationships), and teach it one new skill, which is “given a query and document together, is this document relevant?”

The setup looks something like that:

- Start with a pre-trained transformer (BERT, RoBERTa, MiniLM).
- Add a **linear classification head** on top of the \[CLS\] token, and this maps the hidden state to a single logit.
- Apply sigmoid to get a (relevance) score between 0 and 1. Or sometimes Softmax over pairs, for example for positive vs negative examples.
- Train on `(query, document, relevance_label)` triples.

The most well-known training dataset is **MS MARCO,** which contains about 500k queries from Bing with human-annotated relevant passages.

For the loss function, you have a few options:

- **Binary cross-entropy (BCE)**: This treats the problem as classification, basically asking “is this document relevant or not?”.
- **MSE loss**: More commonly used for distillation (briefly mentioned later). Instead of hard labels, you match soft scores from a stronger teacher model.
- **Pairwise margin loss**: Given one relevant (positive) and one irrelevant (negative) document, ensure the relevant one scores higher by a margin.

The training loop is actually pretty straightforward too: sample a query, pair it with positive and negative documents, concatenate each pair as `[CLS] query [SEP] document [SEP]`, do a forward pass, compute loss, backprop, rinse and repeat.

In practice, most fine-tuning use-cases would start from an already trained cross-encoder like `cross-encoder/ms-marco-MiniLM-L-6-v2` and further fine-tune on their domain-specific data.

### Why Cross-Attention Matters: The Technical Deep Dive

We’ve kept things pretty abstract for now, so this section gets into the core of why cross-encoders are better. Let’s get into the math.

In any transformer, self-attention computes:

https://cdn-images-1.medium.com/max/1200/1*2sfXhIhULNA6MWOh6U2BLQ.png
Each token _i_ produces a query vector:

https://cdn-images-1.medium.com/max/1200/1*ExR4UqgbC-gKUatNLGQfrw.png

A key vector:

https://cdn-images-1.medium.com/max/1200/1*NujHKrejkXYEraOh8A38aA.png

and a value vector:

https://cdn-images-1.medium.com/max/1200/1*aYWQhugvg6-RRfRYWYsmWg.png

The attention score between tokens _i_ and _j_ is:

https://cdn-images-1.medium.com/max/1200/1*u5tv6saDDJs4A0IOngfxHw.png

This score determines how much token _i_ “pays attention to” token _j_.

**In a bi-encoder**, the query and document are separate sequences. The query has tokens \[q1,q2,…,qm\] and the document has \[d1,d2,…,dn\]. The attention matrix for the query is m×m and for the document, n×n.

Specifically, there are zero terms for:

https://cdn-images-1.medium.com/max/1200/1*Fw_3w5BoBgKdWyCW_X3_8Q.png

No query token ever attends to any document token. The model independently compresses each into a single vector, then compares:

https://cdn-images-1.medium.com/max/1200/1*8MUxODbE775Dl7ORu5eWoQ.png

**In a cross-encoder**, the input is one concatenated sequence \[q1,…,qm,d1,…,dn\] and The attention matrix is (m+n)×(m+n).

Now attention terms exists. In a very approximate manner, the query token for “cheap” would attend to the document token for “$500”, and the model learns through training that this combination means “not relevant.” This cross-attention happens at every layer, building increasingly abstract relationships.

**Multi-head attention** makes this even more powerful. Each attention head has its own weight matrices, so different heads learn to detect different types of relationships simultaneously:

- One head might learn **lexical matching** same or similar words
- Another might learn **semantic equivalence** — “cheap” ↔ “budget”
- Another might learn **contradiction detection** — “without sugar” vs “contains sugar”
- Another might learn **entity matching** — the same person or place referenced differently

At the end of it, the outputs of all heads are concatenated and projected:

https://cdn-images-1.medium.com/max/1200/1*eLegzX7rN9oLSToQgvUxtA.png

With multiple heads across multiple players, the model has many independent heads examining query-document interaction at every level of abstraction. Theoretically, that’s why cross-encoders are so much more expressive than bi-encoders.

But of course the tradeoff is then compute: attention costs more and nothing is precomputed.

---

## Enough theory. Let’s look at actual code.

I’ve built a companion repo with eight example .py files that progress from basic implementation to distillation pipelines and full latency-profiled ColBERT implementations.

Each one runs end-to-end and you can follow along as you read through this section.

The first is pretty straightforward:

```python
def predict_scores(self, query: str, documents: list[str]) -> list[float]:
    pairs = [(query, doc) for doc in documents]
    scores = self._model.predict(pairs)
    return [float(s) for s in scores]
```

Under the hood, all my code does is pair the query with every document and score each pair through the cross-encoder:

```python
def predict_scores(self, query: str, documents: list[str]) -> list[float]:
    pairs = [(query, doc) for doc in documents]
    scores = self._model.predict(pairs)
    return [float(s) for s in scores]
```

We begin by feeding the query “How does photosynthesis work in plants?”, along with 10 documents.

- Five are about photosynthesis
- Five are noise about stock markets, electric vehicles, and ancient Rome.

Naturally the photosynthesis documents float to the top:

```markup
--- Reranked Order (10 results) ---
  #1 (score: 8.0888) [was #0] Photosynthesis is the process by which green plants convert...
  #2 (score: 3.7970) [was #4] During photosynthesis, carbon dioxide and water are converted...
  #3 (score: 2.4054) [was #6] Chloroplasts are the organelles where photosynthesis takes...
  #4 (score: 1.8762) [was #2] Plants use chlorophyll in their leaves to absorb light...
  #5 (score: -9.7185) [was #8] The light-dependent reactions occur in the thylakoid...
  ...
  #10 (score: -11.2886) [was #7] Machine learning algorithms can process vast amounts...
```

And there’s really nothing more to it. The model concatenates the query and document as `[CLS] query [SEP] document [SEP]`, runs a forward pass, and produces a relevance score, order by descending.

### Picking the Right Model

The natural follow-up question: which cross-encoder should I use?

We benchmark four MS MARCO models on the same query — from tiny to large.

I run all four models run in parallel via `ThreadPoolExecutor`, so you get results in the time of the slowest model rather than the sum. Here’s what the output looks like:

```markup
--- Speed Comparison ---
Model                                    Time (s)   Docs/sec
---------------------------------------- --------- ----------
ms-marco-MiniLM-L-12-v2                     0.560       14.3
ms-marco-electra-base                       0.570       14.0
ms-marco-MiniLM-L6-v2                       0.811        9.9
ms-marco-TinyBERT-L-2-v2                    1.036        7.7

--- Ranking Order (by document index) ---
  ms-marco-MiniLM-L6-v2:    0 → 2 → 4 → 6 → 7 → 1 → 3 → 5
  ms-marco-TinyBERT-L-2-v2: 2 → 4 → 0 → 6 → 5 → 3 → 1 → 7
  ms-marco-MiniLM-L-12-v2:  2 → 0 → 4 → 6 → 1 → 7 → 3 → 5
  ms-marco-electra-base:    2 → 4 → 0 → 6 → 1 → 3 → 7 → 5
```

All four models agree on the top-4 documents (0, 2, 4, 6), just shuffled slightly.

- TinyBERT is the odd one out , which puts document 5 (irrelevant) in 5th place while the others push it to the bottom.

Generally speaking:

- **TinyBERT-L2-v2**: extremely fast but least accurate — use for low-latency or edge scenarios.
- **MiniLM-L6-v2**: best balance of speed and quality — use as the default for most reranking tasks.
- **MiniLM-L12-v2**: slightly more accurate but slower — use when maximizing ranking quality matters.
- **electra-base**: (older) and larger and slower with no clear advantage — generally not recommended over MiniLM.

---

### Fine-Tuning: Making the Model Understand Your Domain

Many pre-trained cross-encoders are still generalists, because they are trained on datasets like MS MARCO, which itself is a massive dataset of Bing search queries paired with web passages.

If your domain is something like legal contracts, medical records, or cybersecurity incident reports, the generalist model might not rank your content correctly. For example, it does not know that “force majeure” is a contract term, not a military phrase.

**Fine-tuning** might just do the trick.

There are two approaches depending on what kind of training data you have, and the repo includes an example of each.

**When you have soft scores**, you can use MSE loss.

- A larger teacher model scores your query-document pairs, and the student learns to reproduce those continuous scores:

```python
trainer = MSEDistillationTrainer(student_model_name=STUDENT_MODEL, config=config)
output_path = trainer.train(train_dataset)
```

**When you have binary labels**, you can use BCE loss.

- Each training pair is simply marked relevant or not relevant:

```python
finetuner = BCEFineTuner(model_name=BASE_MODEL, config=config)
output_path = finetuner.train(train_dataset)
```

Both approaches are pretty straightforward to set up. Under the hood it’s as simple as:

```python
        class BCEFineTuner:
    """Fine-tune a cross-encoder with binary cross-entropy loss.

    Suitable for binary relevance judgments (relevant/not-relevant).

    Args:
        model_name: HuggingFace model name to fine-tune.
        config: Training configuration.

    Example:
        >>> finetuner = BCEFineTuner("cross-encoder/ms-marco-MiniLM-L6-v2")
        >>> finetuner.train(train_dataset)
    """

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L6-v2",
        config: TrainingConfig | None = None,
    ) -> None:
        self._config = config or TrainingConfig()
        self._model = CrossEncoder(model_name, num_labels=1)
        self._model_name = model_name

    @property
    def model(self) -> CrossEncoder:
        """Return the model being fine-tuned."""
        return self._model

    def train(
        self,
        train_dataset: Dataset,
        eval_dataset: Dataset | None = None,
    ) -> Path:
        """Run BCE fine-tuning.

        The dataset should have columns: "sentence1", "sentence2", "label"
        where "label" is 0 or 1.

        Args:
            train_dataset: Dataset with query-document-label triples.
            eval_dataset: Optional evaluation dataset.

        Returns:
            Path to the saved model directory.
        """
        from sentence_transformers.cross_encoder.losses import BinaryCrossEntropyLoss

        loss = BinaryCrossEntropyLoss(self._model)
        args = self._config.to_training_arguments(has_eval=eval_dataset is not None)

        trainer = CrossEncoderTrainer(
            model=self._model,
            args=args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            loss=loss,
        )
        trainer.train()

        output_path = Path(self._config.output_dir) / "final_model"
        self._model.save(str(output_path))
        return output_path
```

The interesting part is the evaluation, and specifically what happens when you throw **adversarial distractors** at the model.

After training, I test on cases where each query is paired with a relevant document and a hard distractor. In my definition, a hard distractor is a document that shares keywords but is actually about something different. For this evaluation, a “pass” just means the model scored the relevant doc higher:

```python
b_scores = base_model.predict_scores(case.query, docs)
f_scores = fine_tuned.predict_scores(case.query, docs)

b_pass = b_scores[0] > b_scores[1]
f_pass = f_scores[0] > f_scores[1]
```

We split the eval into ‘SEEN’ topics (same topics as training, different examples) and ‘UNSEEN’ topics (entirely new). The ‘UNSEEN’ split is the one that matters because it proves the model learned the domain rather than memorising the training set. Just as we would for most ML evaluation workflows.

Here’s the MSE fine-tuning result:

```markup
Base Model          Fine-Tuned
  Overall accuracy:          15/20 ( 75%)       20/20 (100%)
  Seen topics:                7/10              10/10
  Unseen topics:              8/10              10/10

Fine-tuning fixed 5 case(s) the base model got wrong.
  Average confidence: 316x improvement (gap: +0.0001 -> +0.0386)
```

From the above, we see that fine-tuning fixed the 5 cases where the base model got wrong, and there was a significant improvement in average confidence. The base model’s correct answers were _barely_ correct (gap of +0.0001), but after fine-tuning, the gap widens to +0.0386. So, the model isn’t just getting the right answer more often, it’s getting it with quite a bit of conviction.

The BCE fine-tuning result on legal data (Example 4) is even clearer:

```markup
Base Model      Fine-Tuned
  Overall accuracy:           6/20 ( 30%)       19/20 ( 95%)
  Seen topics:                2/10               9/10
  Unseen topics:              4/10              10/10
```

Accuracy increasing from 30% to 95% means that the original base model was somehow worse than random on legal documents. After fine-tuning on just 72 training pairs , 12 legal topics with 6 pairs each, the model gets 19 out of 20 right. And notice that unseen topics went from 4/10 to 10/10. In a sense it learnt the domain of legal reasoning, not just the training examples.

The output in my repo marks each case where `<-- fine-tuning fixed this,`essentially where the base model failed but the fine-tuned model got it right.

Here’s one illustrative example:

```markup
[SEEN  ] What qualifies as wrongful termination?
           Relevant:   Terminating an employee in retaliation for reporting safety viola...
           Distractor: The wrongful termination of the TV series qualified it for a fan ...
           Base:  FAIL  (gap: -8.3937)   Fine-tuned:  PASS  (gap: +3.8407)
           <-- fine-tuning fixed this
```

The base model confidently chose the TV series distractor due to keyword matches. After fine-tuning, it correctly identifies the employment law document instead.

One thing I really want to call out, as I was figuring all of this out, is that **your distractors can strongly influence what your model learns.** Example 4 trains on legal data where the distractors come from related legal topics, for example, a contract dispute distractor for a tort case, a regulatory compliance distractor for a criminal law query. (No I am not a legal expert I got AI to generate these examples for me)

The challenge is that these examples share vocabulary like “plaintiff”, “jurisdiction”, “statute”. If you used cooking recipes as distractors for legal queries, the model would learn nothing because it can already tell those apart. So the hard negatives from the same domain are what force it to learn fine-grained distinctions.

In many ways, these shares similarities with how I’ve always viewed imbalanced datasets when doing supervised training. The way you select (downsample) your majority class is extremely important. Pick the observations that look really similar to the minority class, and you have yourself a dataset that will train a really powerful (precise) discriminator.

### Semantic Query Caching

In production, users ask the same question a dozen different ways. “How do I reset my password?” and “I forgot my password, how do I change it?” should ideally return same cached results rather than triggering two separate and expensive search, reranking and generation operations.

The idea is simple: use a cross-encoder fine-tuned on something like the Quora duplicate question dataset to detect semantic duplicates at query time.

```python
def find_duplicate(self, query: str) -> tuple[CacheEntry | None, float]:
    if not self._cache:
        return None, 0.0

...

cached_queries = [entry.query for entry in self._cache]
    scores = self._reranker.predict_scores(query, cached_queries)
    best_idx = max(range(len(scores)), key=lambda i: scores[i])
    best_score = scores[best_idx]
    if best_score >= self._threshold:
        return self._cache[best_idx], best_score
    return None, best_score
```

Every incoming query gets scored against everything already in the cache. If the best score exceeds a threshold, it’s a duplicate, so return the cached ranking. If not, run the full reranking pipeline and cache the new result.

To test this properly, we simulate 50 user queries across 12 topics. Each topic starts with a “seed” query that misses the cache, followed by paraphrase variants that should hit:

```markup
("How do I reset my password?", None),            # MISS - first time
("How can I reset my password?", 1),               # HIT → query #1
("How to reset my password?", 1),                  # HIT → query #1
("I forgot my password, how do I change it?", 1),  # HIT → query #1
```

The output shows the cache building up over time. Early queries are all misses, but once the cache has 12 seed queries, everything that follows is a hit:

```markup
#  Result    Time  Query                                            Matched
    1  ✗ MISS      0ms  How do I reset my password?                      -
    2  ✗ MISS   2395ms  How do I export my data from the platform?       -
    ...
    4  ✓ HIT     844ms  How can I reset my password?                     → #01 (0.99)
    ...
   25  ✓ HIT      61ms  I forgot my password, how do I change it?        → #01 (0.99)
   ...
   49  ✓ HIT      17ms  I need to reset my password, how?                → #01 (0.92)
   50  ✓ HIT      25ms  Can I add or remove people from my team?         → #12 (0.93)
```

The ground-truth labels let us compute precision and recall:

```markup
Total queries:        50
  Cache hits:           38   (expected 38)
  Cache misses:         12   (expected 12)

HIT  precision:       38 / 38  (100%)
  MISS precision:       12 / 12  (100%)
  Overall accuracy:     50 / 50  (100%)
  Without caching: 50 rankings needed.  With caching: 12 performed.  76% savings.
```

100% accuracy, and every single hit is correct, every single miss is genuinely new. As a result, we avoid 76% (38/50) of ranking operations in our test dataset.

Of course, the cache comparison itself has O(n) cost against the cache size. In a real system you’d probably want to limit the cache size or use a more efficient index. But the core idea of using a cross-encoder trained for paraphrase detection to gate expensive downstream operations is sound and production-tested.

### The Multi-Stage Funnel

Bringing it all together in production, you can build a funnel where each stage trades speed for precision, and the candidate set shrinks at every step.

For example, 50 documents → 20 (bi-encoder) → 10 (cross-encoder) → 5 (LLM)

The implementation is pretty straightforward:

```python
def run_pipeline(self, query, documents, stage1_k=20, stage2_k=10, stage3_k=5):
    s1 = self.stage1_biencoder(query, documents, top_k=stage1_k)
    s2 = self.stage2_crossencoder(query, documents, s1.doc_indices, top_k=stage2_k)
    s3 = self.stage3_llm(query, documents, s2.doc_indices, top_k=stage3_k)
    return [s1, s2, s3]
```

**Stage 1** is a bi-encoder: encode query and documents independently, rank by cosine similarity. Cheap enough for thousands of documents. Take the top 20.

**Stage 2** is the cross-encoder we’ve been discussing. Score the query-document pairs with full cross-attention. Take the top 10.

**Stage 3** is an optional step where we can utilise an LLM to do list-wise reranking. Unlike the cross-encoder which scores each pair independently, the LLM sees all 10 candidates at once in a single prompt and produces a global ordering. This is the only stage that can reason about _relative_ relevance: “Document A is better than Document B because…”

In my code, the LLM stage calls OpenRouter and uses structured output to guarantee parseable JSON back:

```python
RANKING_SCHEMA = {
    "name": "ranking_response",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "ranking": {
                "type": "array",
                "items": {"type": "integer"},
            },
        },
        "required": ["ranking"],
        "additionalProperties": False,
    },
}
```

The test corpus has 50 documents with ground-truth relevance tiers: highly relevant, partially relevant, distractors, and irrelevant.

The output shows noise getting filtered at each stage:

```markup
Stage                                          Relevant  Partial    Noise  Precision
  Bi-Encoder (all-MiniLM-L6-v2)                     10/20     7/20     3/20        85%
  Cross-Encoder (cross-encoder/ms-marco-MiniLM...)   10/10     0/10     0/10       100%
  LLM (google/gemini-2.0-flash-001)                   5/5      0/5      0/5        100%

Total pipeline time: 2243ms
```

The bi-encoder’s top-20 let through 3 noise documents and 7 partial matches. The cross-encoder eliminated all of them, 10 for 10 on relevant documents. The LLM preserved that precision while cutting to the final 5.

The timing breakdown is worth noting too: the bi-encoder took 176ms to score all 50 documents, the cross-encoder took 33ms for 20 pairs, the LLM took 2034ms for a single API call, by far the slowest stage, but it only ever sees 10 documents.

### Knowledge Distillation: Teaching the Bi-Encoder to Think Like a Cross-Encoder

The multi-stage funnel works, but the generic bi-encoder was never trained on your domain data. It retrieves based on surface-level semantic similarity, which means it might still miss relevant documents or let through irrelevant ones.

What if you could teach the bi-encoder to rank like the cross-encoder?

That’s the essence of distillation. The cross-encoder (teacher) scores your training pairs. The bi-encoder (student) learns to reproduce those scores. At inference time, you throw away the teacher and just use the fast student.

```python
distiller = CrossEncoderDistillation(
    teacher_model_name="cross-encoder/ms-marco-MiniLM-L6-v2",
    student_model_name="all-MiniLM-L6-v2",
)

output_path = distiller.train(
    training_pairs=TRAINING_PAIRS,
    epochs=4,
    batch_size=16,
)
```

The train method that I’ve implemented basically looks like this:

```python
train_dataset = Dataset.from_dict({
    "sentence1": [q for q, _, _ in training_pairs],
    "sentence2": [d for _, d, _ in training_pairs],
    "score": [s for _, _, s in training_pairs],
})

loss = losses.CosineSimilarityLoss(self._student)

args = SentenceTransformerTrainingArguments(
    output_dir=output_dir,
    num_train_epochs=epochs,
    per_device_train_batch_size=batch_size,
    learning_rate=2e-5,
    warmup_steps=0.1,
    logging_steps=5,
    logging_strategy="steps",
    save_strategy="no",
)

trainer = SentenceTransformerTrainer(
    model=self._student,
    args=args,
    train_dataset=train_dataset,
    loss=loss,
)
trainer.train()
```

To demonstrate that this actually works, we chose a deliberately difficult domain: cybersecurity. In cybersecurity, _every document shares the same vocabulary_. Attack, vulnerability, exploit, malicious, payload, compromise, breach, these words appear in documents about SQL injection, phishing, buffer overflows, and ransomware alike. A generic bi-encoder maps all of them to roughly the same region of embedding space and so it cannot tell them apart.

The AI-generated training dataset I have uses hard distractors from confusable subtopics:

- SQL injection ↔ command injection (both “injection attacks”)
- XSS ↔ CSRF (both client-side web attacks)
- phishing ↔ pretexting (both social engineering)
- buffer overflow ↔ use-after-free (both memory corruption)

After training, we run a three-way comparison on 30 test cases, 15 from attack types the model trained on, and 15 from attack types it’s never seen:

```python
t_scores = teacher.generate_teacher_scores(case.query, docs)   # cross-encoder
b_scores = teacher.generate_student_scores(case.query, docs)   # base bi-encoder
d_scores = trained.generate_student_scores(case.query, docs)   # distilled bi-encoder
```

Here’s what the output looks like for a typical case:

```markup
[SEEN  ] What is a DDoS amplification attack?
           Teacher:    rel=+5.5097  dist=-6.5875
           Base:       PASS  (rel=0.7630  dist=0.3295  gap=+0.4334)
           Distilled:  PASS  (rel=0.8640  dist=0.2481  gap=+0.6160)
```

The teacher (cross-encoder) provides the ground truth scores. Both the base and distilled bi-encoders get this one right, but look at the gap: the distilled model is 42% more confident. In a way, it pushes the relevant document further from the distractor in embedding space.

The summary of all tests tells the full story of performance:

```markup
Base Student     Distilled Student
  Overall accuracy:          29/30 ( 96.7%)       29/30 ( 96.7%)
  Seen topics:               15/15                 15/15
  Unseen topics:             14/15                 14/15
  Avg relevance gap:              +0.2679               +0.4126
```

Same accuracy, but 1.5x wider confidence margins. Both models fail on one edge case : the “memory-safe languages” query, where even the cross-encoder teacher disagreed with the expected label. But across the board, the distilled student separates relevant from irrelevant documents more decisively.

This is one of the more innovative and potentially impactful technique that I’ve been experimenting in this project: you get cross-encoder _quality_ at bi-encoder _speed_, at least for your specific domain… assuming you have enough data. So think hard about what kinds of data you would want to collect, label, and process if you think this kind of distillation would be useful to you down the road.

### ColBERT-like Late Interaction

So now we have a spectrum. On one end, bi-encoders are fast, can precompute, but there is no interaction between query and document tokens. On the other end, cross-encoders have full interaction, are more accurate, but nothing is precomputable. Is there something in between?

ColBERT( **CO** ntextualized **L** ate interaction over **BERT**) is one such middle ground. The name tells you the architecture. “Contextualised” means the token embeddings are context-dependent (unlike word2vec where “bank” always maps to the same vector, BERT’s representation of “bank” changes depending on whether it appears near “river” or “account”). “Late interaction” means query and document are encoded separately and only interact at the very end, via operationally inexpensive dot products rather than expensive transformer attention. And “BERT” is the backbone encoder.

That “late” part is the key distinction. A cross-encoder does early interaction in the sense that query and document tokens attend to each other inside the transformer. A bi-encoder does no interaction, just cosine similarity between two pooled vectors. ColBERT sits in between.

When a bi-encoder encodes a sentence, it produces one embedding per token, then **pools** them, typically by averaging into a single vector, for example:

```markup
"How do quantum computers achieve speedup?"
→ 9 token embeddings (each 384-dim)
→ mean pool
→ 1 vector (384-dim): [0.12, -0.34, 0.56, …]
```

That single vector is what gets compared via cosine similarity. It’s fast and it works, but the pooling step crushes the richness of information. The word “quantum” had its own embedding, and so did “speedup.” After mean pooling, their individual signals are averaged together with filler tokens like “do” and “how.” The resulting vector is a blurry summary of the whole sentence.

The ColBERT-like late interaction skips the pooling by keeping all 9 token embeddings:

```markup
"How do quantum computers achieve speedup?"
→
"how" → [0.05, -0.21, …] (384-dim)
"quantum" → [0.89, 0.42, …] (384-dim)
"computers" → [0.67, 0.31, …] (384-dim)
"speedup" → [0.44, 0.78, …] (384-dim)

… 9 tokens total → (9 × 384) matrix
```

Same for the documents we are comparing against. A 30-token document becomes a (30 × 384) matrix instead of a single vector.

Now you need a way to score the match between a (9 × 384) query matrix and a (30 × 384) document matrix. That’s MaxSim.

For each query token, find its best-matching document token (the one with the highest cosine similarity) and take that maximum. Then sum all the maxima across query tokens.

```python
@staticmethod
def _maxsim(q_embs, d_embs):
    sim_matrix = torch.matmul(q_embs, d_embs.T)
    max_sims = sim_matrix.max(dim=1).values
return float(max_sims.sum())
```

Let’s trace through the math. The matrix multiply \`(9 × 384) × (384 × 30)\` produces a \`9 × 30\` similarity matrix. Each cell tells you how similar one query token is to one document token. Then \`.max(dim=1)\` takes the best document match for each query token , 9 values. Then \`.sum()\` adds them up into one score.

The query token “quantum” scans all 30 document tokens and finds its best match , probably something like “qubits” with similarity ~0.85. The query token “speedup” finds something like “faster” at ~0.7. Meanwhile, filler tokens like “how” and “do” match weakly against everything (~0.1). Sum those 9 maxima and you get a score like 9.93, just as an example.

**Why does this work better than a single pooled vector?** Because the token-level matching preserves fine-grained signal. The query token “quantum” can specifically latch onto the document token “qubit” via their embedding similarity, even though they’re different words.

With mean pooling, that precise match gets averaged away into a blurry centroid where “quantum” and “how” contribute equally.

The key advantage, and the reason you’d consider ColBERT-like late interaction in production, is **pre-indexing**. Because documents are encoded independently of the query, you can encode your entire corpus offline and cache the token embeddings:

```python
def index(self, documents):
  self._doc_embeddings = []
  for doc in documents:
    emb = self._model.encode(doc, output_value="token_embeddings")
    tensor = torch.nn.functional.normalize(torch.tensor(emb), dim=-1)
    self._doc_embeddings.append(tensor)
```

At search time, you only encode the query, one forward pass, and then run dot products against the cached embeddings. The cross-encoder would need to encode all 60 (query, document) pairs from scratch.

How close does it get to cross-encoder quality? Here’s the summary from running 10 queries across a 60-document corpus spanning quantum computing, vaccines, ocean chemistry, renewable energy, ML, astrophysics, genetics, blockchain, microbiology, and geography:

```markup
Ranking agreement (ColBERT vs cross-encoder ground truth):
Avg Kendall's tau: +0.376
Avg top-3 overlap: 77%
Avg top-5 overlap: 92%

Latency breakdown:
ColBERT indexing: 358.7ms (one-time, 60 docs)
ColBERT queries: 226.4ms total (22.6ms avg per query)
Cross-encoder: 499.1ms total (49.9ms avg per query)
Query speedup: 2.2x faster
```

92% top-5 overlap, so most of the times it’s retrieving the same documents; it just occasionally shuffles the within-topic ordering. For most applications, that’s good enough, and at 2.2x faster per query.

And the real power comes when you observe what happens under load.

I collected 100 real processing time samples for each system, then simulated a single-server queue at increasing QPS levels. Requests arrive at fixed intervals, queue up if the server is busy, and we measure the total response time (queue wait + processing):

```markup
===========================================================================
LATENCY PROFILING
===========================================================================

  Raw processing time (100 samples per system):
                       p50     p95     p99    p99.9     max
    ───────────────────────────────────────────────────────
    ColBERT           20.4ms    30.8ms    54.2ms     64.3ms    64.3ms
    Cross-encoder     45.2ms    56.7ms    69.0ms     72.1ms    72.1ms

===========================================================================
QPS SIMULATION (single-server queue, 1000 requests per level)
===========================================================================

  Response time = queue wait + processing time.
  When QPS exceeds throughput, requests queue and tail latencies explode.

  QPS: 5 (ColBERT util: 10%, cross-encoder util: 23%)
                       p50     p95     p99    p99.9     max
    ───────────────────────────────────────────────────────
    ColBERT           20.4ms    30.8ms    54.2ms     64.3ms    64.3ms
    Cross-encoder     45.2ms    56.7ms    69.0ms     72.1ms    72.1ms

  QPS: 10 (ColBERT util: 20%, cross-encoder util: 45%)
                       p50     p95     p99    p99.9     max
    ───────────────────────────────────────────────────────
    ColBERT           20.4ms    30.8ms    54.2ms     64.3ms    64.3ms
    Cross-encoder     45.2ms    56.7ms    69.0ms     72.1ms    72.1ms

  QPS: 20 (ColBERT util: 41%, cross-encoder util: 90%)
                       p50     p95     p99    p99.9     max
    ───────────────────────────────────────────────────────
    ColBERT           20.4ms    34.0ms    62.9ms     64.3ms    64.3ms
    Cross-encoder     50.8ms    74.8ms    80.9ms     82.8ms    82.8ms

  QPS: 30 (ColBERT util: 61%, cross-encoder util: 136%)
                       p50     p95     p99    p99.9     max
    ───────────────────────────────────────────────────────
    ColBERT           20.7ms    49.1ms    67.3ms     79.6ms    79.6ms
    Cross-encoder   6773.0ms 12953.5ms 13408.0ms  13512.6ms 13512.6ms

  QPS: 40 (ColBERT util: 82%, cross-encoder util: 181%)
                       p50     p95     p99    p99.9     max
    ───────────────────────────────────────────────────────
    ColBERT           23.0ms    67.8ms    84.0ms     87.9ms    87.9ms
    Cross-encoder  10931.3ms 20861.8ms 21649.7ms  21837.6ms 21837.6ms
```

If you look at 30 QPS, you see that the cross-encoder’s utilization exceeds 100%, requests arrive every 33ms but each takes 45ms to process. Every request adds about 12ms of queue debt. After 500 requests, the queue has accumulated over 6 seconds of wait time. That’s your p50, so half your users are waiting nearly 7 seconds.

Meanwhile, ColBERT-like late interaction at 61% utilisation is barely sweating at 20.7ms p50, and every percentile roughly where it was at idle.

At 40 QPS, the cross-encoder’s p99.9 is over 21 seconds. ColBERT’s p50 is 23ms.

So this is something to think about as well in production, you might want to choose your reranking architecture based on your QPS budget, not just your accuracy requirements.

_A caveat:_ this is a ColBERT- _like_ implementation. It demonstrates the MaxSim mechanism using \`all-MiniLM-L6-v2\`, which is a general-purpose sentence transformer. Real ColBERT deployments use models specifically trained for token-level late interaction retrieval, like \`colbert-ir/colbertv2.0\`.

## Where Does This Leave Us?

These examples illustrate options on retrieval and reranking:

- Cross-encoder (raw): Slow, highest quality. Use for small candidate sets under 100 docs.
- Fine-tuned cross-encoder: Slow, highest quality for your domain. Use when general models perform poorly on domain content.
- Semantic caching: Instant on cache hit, same quality as underlying ranker. Use for high-traffic systems with repeated queries.
- Multi-stage funnel: Slow per query, scales to large corpora, performance near cross-encoder
- Distilled bi-encoder: Fast, near cross-encoder quality. Use as first stage of a funnel or for domain-specific retrieval.
- ColBERT-like (late interaction): Medium speed, near cross-encoder quality. Use for high-QPS services where tail latency matters.

A mature search system might combine any of them: a distilled bi-encoder for first-pass retrieval, a cross-encoder for reranking the top candidates, semantic caching to skip redundant work, and ColBERT-like interaction as a fallback when the latency budget is tight.

All the code is available at [https://github.com/ianhohoho/cross-encoder-and-reranking-demo](https://github.com/ianhohoho/cross-encoder-and-reranking-demo). In fact, every example runs end-to-end without API keys required except Example 6, which calls an LLM through OpenRouter for the list-wise reranking stage.

If you’ve made it to the end, I’d love to hear how you’re handling retrieval and reranking in production, what’s your stack look like? Are you running a multi-stage funnel, or is a single bi-encoder doing the job?

I’m always happy to hear your thoughts on the approaches I’ve laid out above, and feel free to make suggestions to my implementation as well!

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop.md">
<details>
<summary>Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/>

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/)

# Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop

A practical guide to choosing between single-pass pipelines and adaptive retrieval loops based on your use case's complexity, cost, and reliability requirements

[Mostafa Ibrahim](https://towardsdatascience.com/author/mostafaibrahim18/)

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

1.  **Query:** take the user question (and any system instructions) as input
2.  **Retrieve:** fetch the top-k relevant chunks (usually via vector search, sometimes hybrid)
3.  **Assemble context:** Select and arrange the best passages into a prompt context (often with reranking)
4.  **Generate:** Produce an answer, ideally with citations back to the retrieved passages

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

-   **Multi-hop questions**: the answer needs evidence spread across multiple sources
-   **Underspecified queries**: the user’s wording is not the best retrieval query
-   **Brittle chunking:** relevant context is split across chunks or obscured by jargon
-   **Ambiguity:** the system may need to ask clarifying questions, reformulate, or explore further before providing an accurate answer.

**Why this matters:**

When classic RAG fails, it often does so quietly. The system still provides an answer, but it may be a confident synthesis based on weak evidence.

## Agentic RAG: from retrieval to a control loop

Agentic RAG retains the retriever and generator components but changes the control structure. Instead of relying on a single retrieval pass, retrieval is wrapped in a loop, allowing the system to review its evidence, identify gaps, and attempt retrieval again if needed. This loop gives the system an “agentic” quality: it not only generates answers from evidence but also actively chooses how to gather stronger evidence until a stop condition is met. A helpful analogy is incident debugging: classic RAG is like running one log query and writing the conclusion from whatever comes back, while agentic RAG is a debug loop. You query, inspect the evidence, notice what’s missing, refine the query or check a second system, and repeat until you’re confident or you hit a time/cost budget and escalate.

A minimal loop is:

1.  **Retrieve:** pull candidate evidence (docs, search results, or tool outputs)
2.  **Reason:** synthesize what you have and identify what’s missing or uncertain
3.  **Decide:** stop and answer, refine the query, switch sources/tools, or escalate

For a research reference, ReAct provides a useful mental model: reasoning steps and actions are interleaved, enabling the system to gather more substantial evidence before finalizing an answer.

### What agents add

**Planning (decomposition)**

The agent can decompose a question into smaller evidence-based objectives.

Example: “Why is SSO setup failing for a subset of users?”

-   What error codes are we seeing?
-   Which IdP configuration is used
-   Is this a docs question, a log question, or a configuration question

Classic RAG treats the entire question as a single query. An agent can explicitly determine what information is needed first.

**Tool use (beyond retrieval)**

In agentic RAG, retrieval is one of several available tools. The agent may also use:

-   A second index
-   A database query
-   A search API
-   A config checker
-   A lightweight verifier

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

1.  The question is underspecified and needs query refinement
2.  The evidence is spread across multiple documents or sources
3.  The first retrieval returns partial or conflicting information, and the system needs to verify before committing

### Where loops hurt

The tradeoff is operational complexity. With loops, you introduce more moving parts (planner, retriever, optional tools, stop conditions), which increases variance and makes runs harder to reproduce. You also expand the surface area for failures: a run might look “fine” at the end, but still burn tokens through repeated retrieval, retries, or tool cascades.

This is also why [“enterprise RAG”](https://arxiv.org/abs/2404.16130) tends to get tricky in practice: security constraints, messy internal data, and integration overhead make naive retrieval brittle.

## Failure modes you’ll see early in production

Once you move from a pipeline to a control loop, a few problems show up repeatedly:

-   **Retrieval thrash:** the agent keeps retrieving without improving evidence quality.
-   **Tool-call cascades:** one tool call triggers another, compounding latency and cost.
-   **Context bloat:** the prompt grows until quality drops or the model starts missing key details.
-   **Stop-condition bugs:** the loop doesn’t stop when it should (or stops too early).
-   **Confident-wrong answers:** the system converges on noisy evidence and answers with high confidence.

A key perspective is that classic RAG primarily fails due to retrieval quality or prompting. Agentic RAG can encounter these issues as well, but also introduces control-related failures, such as poor decision-making, inadequate stop rules, and uncontrolled loops. As autonomy increases, observability becomes even more critical.

## Quick comparison: Classic vs Agentic RAG

| Dimension            | Classic RAG                   | Agentic RAG                           |
| :------------------- | :---------------------------- | :------------------------------------ |
| Cost predictability  | High                          | Lower (depends on loop depth)         |
| Latency predictability | High                          | Lower (p95 grows with iterations)     |
| Multi-hop queries    | Often weak                    | Stronger                              |
| Debugging surface    | Smaller                       | Larger                                |
| Failure modes        | Mostly retrieval + prompt     | Adds loop control failures            |

## Decision Framework: When to stay classic vs go agentic

A practical approach to choosing between classic and agentic RAG is to evaluate your use case along two axes: query complexity (the extent of multi-step reasoning or evidence gathering required) and error tolerance (the risk associated with incorrect answers for users or the business). Classic RAG is a strong default due to its predictability. Agentic RAG is preferable when tasks frequently require retries, decomposition, or cross-source verification.

### Decision matrix: complexity × error tolerance

Here, **high error tolerance** means a wrong answer is acceptable (low stakes), while **low error tolerance** means a wrong answer is costly (high stakes).

|                     | High error tolerance                                        | Low error tolerance                                                         |
| :------------------ | :---------------------------------------------------------- | :-------------------------------------------------------------------------- |
| Low Complexity      | **Classic RAG** for fast answers and predictable latency/cost. | **Classic RAG** with citations, careful retrieval, escalation               |
| High Complexity     | **Classic RAG + second pass on failure signals** (only loop when needed). | **Agentic RAG** with strict stop conditions, budgets, and debugging         |

### Practical gating rules (what to route where)

Classic RAG is usually the better fit when the task is mostly lookup or extraction:

-   FAQs and documentation Q&A
-   Single-document answers (policies, specs, limits)
-   Fast assist where latency predictability matters more than perfect coverage

Agentic RAG is usually worth the added complexity when the task needs multi-step evidence gathering:

-   Decomposing a question into sub-questions
-   Iterative retrieval (rewrite, broaden/narrow, switch sources)
-   Verification and cross-checking across sources/tools
-   Workflows where “try again” is required to reach a confident, cited answer.

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

-   [Dense Passage Retrieval (DPR)](https://arxiv.org/abs/2004.04906)
-   [HyDE (query expansion for better retrieval)](https://arxiv.org/abs/2212.10496)
-   [BEIR benchmark (evaluate retrievers beyond one dataset)](https://arxiv.org/abs/2104.08663)
-   [RAGAS (RAG evaluation framework)](https://arxiv.org/abs/2309.15217)
-   [Toolformer](https://arxiv.org/abs/2302.07842)
-   [FiD-style multi-document generation](https://arxiv.org/abs/2007.01282)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="converging-paradigms-the-synergy-of-symbolic-and-connectioni.md">
<details>
<summary>Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2407.08516v5>

# Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents

Haoyi Xiong, Zhiyuan Wang, Xuhong Li, Jiang Bian, Zeke Xie, Shahid Mumtaz, Anwer Al-Dulaimi, and Laura E. Barnes
H. Xiong and J. Bian are with Microsoft Corporation. Z. Wang and L. E. Barnes are with the University of Virginia. Xuhong Li is with Univiersité de technologie de Compiègne. Z. Xie is with Hong Kong University of Science and Technology (GZ). S. Mumtaz is with Nottingham Trent University, Nottingham, UK and Silesian University of Technology, Gliwice, Poland. Anwer Al-Dulaimi is with College of Technological Innovation, Zayed University, Abu Dhabi, UAE.

###### Abstract

This article explores the convergence of connectionist and symbolic artificial intelligence (AI), from historical debates to contemporary advancements. Traditionally considered distinct paradigms, connectionist AI focuses on neural networks, while symbolic AI emphasizes symbolic representation and logic. Recent advancements in large language models (LLMs), exemplified by ChatGPT and GPT-4, highlight the potential of connectionist architectures in handling human language as a form of symbols. The study argues that LLM-empowered Autonomous Agents (LAAs) embody this paradigm convergence. By utilizing LLMs for text-based knowledge modeling and representation, LAAs integrate neuro-symbolic AI principles, showcasing enhanced reasoning and decision-making capabilities. Comparing LAAs with Knowledge Graphs within the neuro-symbolic AI theme highlights the unique strengths of LAAs in mimicking human-like reasoning processes, scaling effectively with large datasets, and leveraging in-context samples without explicit re-training. The research underscores promising avenues in neuro-vector-symbolic integration, instructional encoding, and implicit reasoning, aimed at further enhancing LAA capabilities. By exploring the progression of neuro-symbolic AI and proposing future research trajectories, this work advances the understanding and development of AI technologies.

###### Index Terms:
Large Language Models (LLMs), LLM-Empowered Autonomous Agents (LAAs), Neuro-symbolic AI, Program-Proof-of-Thoughts (P2oT) prompting

## I Introduction

Artificial Intelligence (AI) has historically navigated the fascinating duality of two foundational paradigms: connectionism and symbolism. Connectionism, deeply influenced by cognitive science and computational neuroscience, delves into neural networks and machine learning algorithms that echo the deep neural architecture and functions of the human brain \[ [1](https://arxiv.org/html/2407.08516v5#bib.bib1 "")\]. Imagine a sprawling network of neurons firing in electric synchrony, mirroring how advanced AI systems identify patterns and glean insights from vast datasets. Conversely, symbolism is the epitome of conceptual and logical clarity. It anchors itself in the high-level abstractions and representations of knowledge, flourishing through rule-based systems that excel in reasoning and decision-making \[ [2](https://arxiv.org/html/2407.08516v5#bib.bib2 "")\]. Picture a grand library where every book is a rule, and every chapter a pathway to logical deduction–symbolic AI analogising the thought processes of human reasoning.

The dynamic interplay between these two paradigms has sculpted the continuous evolution of AI, like a grand philosophical debate, resulting in shifts in dominance and application across various research domains. Think of this dialectic as a dance through time—the elegant waltz of connectionism and symbolism, sometimes leading, sometimes following, yet always in a harmonious exchange that propels the boundaries of what AI can achieve. For instance, in the domain of image recognition, connectionist models driven by deep neural networks demonstrate their prowess by identifying subtle patterns in pixel data, akin to how our brains recognize faces in a crowd \[ [3](https://arxiv.org/html/2407.08516v5#bib.bib3 "")\]. Meanwhile, in expert systems used for medical diagnostics, symbolism shines by methodically applying predefined rules to diagnose diseases, mimicking the logical flow of a doctor’s thought process \[ [4](https://arxiv.org/html/2407.08516v5#bib.bib4 "")\]. This storied dance of paradigms has not just shaped, but revitalized AI, continuing to impact its trajectory as it ventures into increasingly sophisticated applications. The oscillation of dominance between these approaches resembles the ebb and flow of tides, each rise and retreat bringing new insights and innovations to the fore.

In recent years, the advancements in Large Language Models (LLMs) and foundation models have catalyzed the integration of connectionist and symbolic AI paradigms, realizing new levels of computational intelligence and versatility \[ [5](https://arxiv.org/html/2407.08516v5#bib.bib5 "")\]. These models, exemplified by systems such as OpenAI’s GPT-4, have demonstrated unprecedented capabilities in natural language understanding and generation, exhibiting robust performance across a range of complex tasks \[ [6](https://arxiv.org/html/2407.08516v5#bib.bib6 "")\]. LLMs themselves are a triumph of connectionism, empowered by vast amounts of data and sophisticated neural architectures to produce coherent and contextually relevant texts. Moreover, the emergence of LLM-empowered Autonomous Agents (LAAs) signifies a pivotal juncture in the development of AI, embodying the convergence of symbolic and connectionist AI. As shown in Figure [1](https://arxiv.org/html/2407.08516v5#S1.F1 "Figure 1 ‣ I Introduction ‣ Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents"), LAAs combine a symbolic subsystem, utilizing language-based knowledge, rules, and workflows intrinsic to symbolic AI, with the generative capabilities of LLMs \[ [7](https://arxiv.org/html/2407.08516v5#bib.bib7 "")\]. This symbolic subsystem works seamlessly with the neural subsystem and incorporates external tools for perceptions and actions \[ [8](https://arxiv.org/html/2407.08516v5#bib.bib8 "")\]. LAAs demonstrate advanced reasoning, planning, and decision-making abilities, marking a new era in AI. The dual subsystems align with dual-process theories of reasoning \[ [9](https://arxiv.org/html/2407.08516v5#bib.bib9 "")\] and Systems I and II proposed by Yoshua Bengio \[ [10](https://arxiv.org/html/2407.08516v5#bib.bib10 "")\].

https://arxiv.org/html/2407.08516v5/x1.pngFigure 1: Elements of LLM-empowered Autonomous Agents (LAAs): Large Language Models (Neural Sub-System), Agentic Workflows (Symbolic Sub-System), and External Tools

In this work, we aim at examining the historical evolution and current state of AI by exploring the enduring debate between connectionism and symbolism and their convergence in modern technologies, particularly in the theme of neuro-symbolic approaches, including Knowledge Graphs, LLMs, and LAAs. This review aims to illustrate how the integration of these paradigms has led to groundbreaking advancements, offering new perspectives on the capabilities and future directions of AI.

- •
Historical Context of Technology: This article provides an in-depth examination of the historical debate between connectionism and symbolism, contextualizing modern AI developments and highlighting the strengths of each approach. We present recent advancements in LLMs with Knowledge Graphs (KGs) \[ [11](https://arxiv.org/html/2407.08516v5#bib.bib11 "")\] as references, discussing these techniques from the perspectives of symbolic, connectionist, and neuro-symbolic AI. The article also showcases the transformative impact of these techniques on knowledge modeling, acquisition, representation, and reasoning.

- •
Convergence of Paradigms: This article highlights the convergence of symbolic and connectionist approaches in developing LAAs, emphasizing their enhanced reasoning, decision-making, and efficiency. By contrasting LAAs with Knowledge Graphs (KGs) within neuro-symbolic AI, we examine distinct patterns and functionalities. While both integrate symbolic and neural methodologies, LAAs demonstrate unique advantages over KGs: (1) analogizing human reasoning with agentic workflows and various prompting techniques \[ [12](https://arxiv.org/html/2407.08516v5#bib.bib12 ""), [13](https://arxiv.org/html/2407.08516v5#bib.bib13 "")\], (2) scaling effectively on large datasets, adapting to in-context samples, and leveraging the emergent abilities of LLMs. These strengths drive the surge of a new wave of neuro-symbolic AI \[ [14](https://arxiv.org/html/2407.08516v5#bib.bib14 "")\].

- •
Future Directions: The article highlights the trend of converging paradigms and current limitations of LAAs, pointing to two promising future directions. First is the development of _neuro-vector-symbolic architectures_, which integrate vector manipulation to enhance the reasoning capabilities of agents. Second is the approach known as _program-proof-of-thoughts (P2oT) prompting_. This involves breaking down complex reasoning processes into verifiable propositions, utilizing program proof languages (such as Dafny) for structured verification. It aims to provide rigorous reasoning by modeling propositions, integrating with theorem provers, and focusing on applications in specific domains.

These contributions are crucial as they provide a comprehensive understanding of the evolution of AI, highlight the significance of paradigm convergence, and offer insights into future research and application potentials in the rapidly evolving field of AI.

## II Preliminaries

This section begins by summarizing the historical debate between connectionist AI and symbolic AI. We then explore knowledge graphs (KGs) as an early effort to synergize these two paradigms through neuro-symbolic AI. Lastly, we examine LLMs as the latest advancements in connectionist AI.

https://arxiv.org/html/2407.08516v5/x2.pngFigure 2: Exploring the Evolution of Artificial Intelligence: A Timeline of Key Innovations and Milestones. It starts from the birth of symbolic and connectionist AI in the 1950s, through key milestones like the AI debates of the 1980s and the advancement in machine learning in the 1990s. This figure highlights significant developments such as the impact of AlexNet on image recognition, the transformation in NLP by models like BERT and GPT, and the rise of generative AI, culminating in the use of LLMs and Agents for autonomous decision-making in the 2020s.

### II-AConnectionism vs. Symbolism: a Historical Debate on AI

As shown in Figure [2](https://arxiv.org/html/2407.08516v5#S2.F2 "Figure 2 ‣ II Preliminaries ‣ Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents"), the discourse of AI has long revolved around the dichotomy between connectionism and symbolism, two paradigms integral to the field. Connectionism models cognitive processes through artificial neural networks that emulate the brain’s neuron structures, emphasizing learning through algorithms and pattern recognition. This began with Frank Rosenblatt’s Perceptron in 1958 \[ [15](https://arxiv.org/html/2407.08516v5#bib.bib15 "")\] and advanced significantly with the backpropagation algorithm developed by David Rumelhart, Geoffrey Hinton, and Ronald J. Williams in the 1980s \[ [16](https://arxiv.org/html/2407.08516v5#bib.bib16 "")\], setting the stage for modern deep learning \[ [1](https://arxiv.org/html/2407.08516v5#bib.bib1 "")\].
Conversely, symbolism focuses on high-level knowledge representations and symbolic manipulation to mimic human reasoning, gaining prominence with systems like the Logic Theorist by Allen Newell and Herbert A. Simon in 1956 \[ [17](https://arxiv.org/html/2407.08516v5#bib.bib17 "")\]17]]. Symbolic AI thrived with expert systems such as MYCIN \[ [4](https://arxiv.org/html/2407.08516v5#bib.bib4 "")\] and DENDRAL \[ [18](https://arxiv.org/html/2407.08516v5#bib.bib18 "")\] in the 1970s and 1980s, excelling in specific domains through predefined rules.

In the 1980s, as Ashok Goel noted, debates often involved criticisms that attacked caricatures of the opposing methods \[ [19](https://arxiv.org/html/2407.08516v5#bib.bib19 "")\]. Each approach has its limitations: connectionist AI is criticized for its black-box nature and lack of interpretability \[ [20](https://arxiv.org/html/2407.08516v5#bib.bib20 "")\], while symbolic AI faced challenges with the labor-intensive knowledge acquisition process \[ [21](https://arxiv.org/html/2407.08516v5#bib.bib21 "")\] and its limited adaptability \[ [22](https://arxiv.org/html/2407.08516v5#bib.bib22 "")\].
Historical debates between figures, such as Yann LeCun, Yoshua Bengio, and Gary Marcus, have underscored these limitations \[ [23](https://arxiv.org/html/2407.08516v5#bib.bib23 "")\]. However, the integration of both paradigms has led to robust hybrid models, combining neural networks’ pattern recognition with symbolic systems’ interpretability and logical reasoning \[ [24](https://arxiv.org/html/2407.08516v5#bib.bib24 "")\]. Contemporary research exemplifies this convergence, seen in neuro-symbolic AI and large-scale pre-trained models like BERT \[ [25](https://arxiv.org/html/2407.08516v5#bib.bib25 "")\], GPT \[ [5](https://arxiv.org/html/2407.08516v5#bib.bib5 "")\], and hybrid reinforcement learning models \[ [26](https://arxiv.org/html/2407.08516v5#bib.bib26 "")\], reflecting the ongoing evolution inspired by the historical debate.

### II-BKnowledge Graphs: An Early Neuro-symbolic Attempt

Knowledge graphs have a foundation rooted in the evolution of semantic web technologies and the Resource Description Framework (RDF). Proposed by the W3C in the 1990s, RDF standardized data interchange on the web using triples (subject, predicate, object) for seamless data integration and interoperability \[ [27](https://arxiv.org/html/2407.08516v5#bib.bib27 "")\]. This movement established the Semantic Web, aiming for a more intelligent and interconnected web \[ [28](https://arxiv.org/html/2407.08516v5#bib.bib28 "")\]. Early adopters used RDF to build schemas and taxonomies, forming the basics of modern knowledge graphs \[ [29](https://arxiv.org/html/2407.08516v5#bib.bib29 "")\].

As the field matured, the focus shifted towards capturing complex relationships and domain-specific knowledge. Ontologies, formal specifications of concepts and relationships, provided a framework for annotating and interlinking data, enabling semantic reasoning at a certain level \[ [30](https://arxiv.org/html/2407.08516v5#bib.bib30 "")\]. Markov-logic networks introduced probabilistic reasoning to knowledge graphs, allowing for handling uncertainty and inconsistency in data \[ [31](https://arxiv.org/html/2407.08516v5#bib.bib31 "")\]. The synergy of Ontologies and Markov-logic networks advanced the ability of symbolic AI to perform robust reasoning over large datasets \[ [32](https://arxiv.org/html/2407.08516v5#bib.bib32 "")\].

In recent years, the use of graph neural networks (GNNs) has further revolutionized the landscape of knowledge graphs. GNNs adeptly leverage the graph structure for advanced pattern recognition and complex predictions. They excel in tasks such as node classification, link prediction, and the extraction of hidden patterns from graph-structured data \[ [33](https://arxiv.org/html/2407.08516v5#bib.bib33 "")\]. This paradigm shift towards neural networks marks a convergence with modern machine learning techniques, enabling more nuanced and scalable interpretations of often massive and intricate datasets. The ability of GNNs to embed nodes and entire graphs numerically has significantly enhanced the computational handling of knowledge graphs \[ [34](https://arxiv.org/html/2407.08516v5#bib.bib34 "")\]. In conclusion, the integration of graph neural networks with rule-based reasoning has positioned knowledge graphs at the core of the neuro-symbolic AI approach \[ [11](https://arxiv.org/html/2407.08516v5#bib.bib11 "")\] prior to the surge of LLMs.

### II-CLLMs: Recent Connectionist AI Advancements

The field of connectionist AI has undergone substantial evolution, beginning with the invention of the perceptron \[ [15](https://arxiv.org/html/2407.08516v5#bib.bib15 "")\], kicking off the neural network research in the late 1950s. In the following decades, the development of Multi-Layer Perceptrons (MLPs) introduced hidden layers and non-linear activation functions, enabling the modeling of more complex functions \[ [16](https://arxiv.org/html/2407.08516v5#bib.bib16 "")\]. In the 1990s, Long Short-Term Memory (LSTM) networks were developed to address the limitations of traditional recurrent neural networks (RNNs) by introducing gating mechanisms to handle long-term dependencies in sequential data \[ [35](https://arxiv.org/html/2407.08516v5#bib.bib35 "")\]. Self-attention mechanisms and transformer architectures proposed in the late 2010s further revolutionized sequence modeling, such as texts for natural language processing, by allowing models to focus on different parts of the input sequence when generating each part of the output sequence \[ [36](https://arxiv.org/html/2407.08516v5#bib.bib36 "")\].

The development of transformer-based pre-trained language models has significantly advanced natural language processing (NLP). These architectures include encoder-only models, e.g., BERT \[ [25](https://arxiv.org/html/2407.08516v5#bib.bib25 "")\], which excel at understanding and classifying text; decoder-only models, e.g., GPT \[ [6](https://arxiv.org/html/2407.08516v5#bib.bib6 "")\], which generate coherent and contextually relevant text; and encoder-decoder models, e.g., T5 \[ [37](https://arxiv.org/html/2407.08516v5#bib.bib37 "")\], which are effective in tasks requiring both comprehension and generation. Transformer-based language models, such as OpenAI’s GPT-4 \[ [38](https://arxiv.org/html/2407.08516v5#bib.bib38 "")\], Google’s Gemini \[ [39](https://arxiv.org/html/2407.08516v5#bib.bib39 "")\] and PaLM \[ [40](https://arxiv.org/html/2407.08516v5#bib.bib40 "")\], Microsoft’s Phi-3 \[ [41](https://arxiv.org/html/2407.08516v5#bib.bib41 "")\], and Meta’s LLaMA \[ [42](https://arxiv.org/html/2407.08516v5#bib.bib42 "")\], are termed Large Language Models (LLMs). These models, illustrated in Figure [3](https://arxiv.org/html/2407.08516v5#S2.F3 "Figure 3 ‣ II-C LLMs: Recent Connectionist AI Advancements ‣ II Preliminaries ‣ Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents"), are trained on large-scale transformers comprising billions of learnable parameters to support various abilities to enable agents, including perception, reasoning, planning, and action \[ [12](https://arxiv.org/html/2407.08516v5#bib.bib12 "")\]. As the central component of an agent’s neural sub-system, the larger the model, the stronger the agent’s capability.

https://arxiv.org/html/2407.08516v5/x3.pngFigure 3: Large Language Models and Their Agentic Abilities. The X-axis shows the release dates, and the Y-axis represents the LLM Agent Benchmark Score \[ [43](https://arxiv.org/html/2407.08516v5#bib.bib43 "")\]. Bubble size indicates the number of parameters (in billions). An asterisk (\*) denotes estimated parameter counts when the official release is not available.

In general, every LLM undergos a two-stage training process: _pre-training_ and _fine-tuning_. Pre-training involves adjusting model parameters based on the statistical properties of a large text corpus, enabling an understanding of syntax, semantics, and linguistic nuances \[ [25](https://arxiv.org/html/2407.08516v5#bib.bib25 "")\]. Fine-tuning then adapts the pre-trained model to specific tasks or domains using a smaller, task-specific dataset, optimizing performance for particular applications \[ [44](https://arxiv.org/html/2407.08516v5#bib.bib44 "")\]. To ensure LLMs follow human’s instructions, align with human values and exhibit desired behaviors, instruction tuning and reinforcement learning from human feedback (RLHF) have been proposed on top of fine-tuning \[ [45](https://arxiv.org/html/2407.08516v5#bib.bib45 "")\].

As the size of LLMs increases, they exhibit a range of emerging capabilities, such as writing computer code, playing chess, diagnosing medical conditions, and translating languages. These capabilities often develop suddenly and dramatically at certain scales due to scaling laws, which describe how task performance can surge unexpectedly when a model reaches a particular threshold size \[ [46](https://arxiv.org/html/2407.08516v5#bib.bib46 "")\]. This phenomenon is particularly observable in tasks requiring multi-step reasoning, where success probabilities compound multiplicatively, leading to rapid performance jumps \[ [47](https://arxiv.org/html/2407.08516v5#bib.bib47 "")\]. However, these advancements come with _“hallucination” challenges_\[ [48](https://arxiv.org/html/2407.08516v5#bib.bib48 "")\], such as producing false or nonsensical information that appears convincing but is inaccurate or not based on reality. These issues underline the importance of continued research and engineering to harness the benefits of LLMs while mitigating their drawbacks.

## III LLM-empowered Autonomous Agents: The Convergence of Symbolism and Connectionism

This section reviews the definition of both traditional and LLM-based agents, introduces core techniques for designing and implementing LAAs, and rethinks these innovations through the lens of symbolic AI.

### III-AAutonomous Agents: Classic and LLM-empowered

An autonomous agent is an artificially intelligent entity designed to achieve specific goals independently, acquiring contextual factors to perceive the environmental state and undertaking context-relevant actions \[ [49](https://arxiv.org/html/2407.08516v5#bib.bib49 "")\]. These agents, equipped with reasoning, learning, and adaptability, thrive in dynamic and complex contexts. Unlike traditional software programs that follow predetermined rules, autonomous agents operate with self-governing attributes, allowing them to function under varying conditions \[ [50](https://arxiv.org/html/2407.08516v5#bib.bib50 "")\]. Leveraging these capabilities, they facilitate automation by performing tasks that typically require human intervention, enhancing efficiency, and reducing operational costs across fields such as robotics, communication, financial trading, and healthcare \[ [50](https://arxiv.org/html/2407.08516v5#bib.bib50 "")\]. For instance, in robotic applications, autonomous agents can navigate tasks with minimal supervision, continuously monitor their surroundings, and adapt to new situations, making them robust solutions for long-term automation \[ [51](https://arxiv.org/html/2407.08516v5#bib.bib51 ""), [52](https://arxiv.org/html/2407.08516v5#bib.bib52 "")\].

The foundational techniques of autonomous agent design originate from classic AI approaches, such as Probabilistic Graphical Models \[ [53](https://arxiv.org/html/2407.08516v5#bib.bib53 "")\], Reinforcement Learning \[ [54](https://arxiv.org/html/2407.08516v5#bib.bib54 "")\], and Multi-Agent Systems \[ [55](https://arxiv.org/html/2407.08516v5#bib.bib55 "")\], which manage uncertainty and learn optimal behaviors in dynamic environments or enable agents to interact and share information efficiently. However, the advent of LAAs marks a significant evolution beyond traditional AI for both symbolic and neural sub-systems. These agents use extensive pre-training on vast textual corpora to acquire broad knowledge, performing human reasoning tasks by generating contextually appropriate text \[ [56](https://arxiv.org/html/2407.08516v5#bib.bib56 "")\]. This capability not only simulates understanding and decision-making but also allows the generation of code and other communicative texts, enhancing their practical utility \[ [57](https://arxiv.org/html/2407.08516v5#bib.bib57 "")\]. By integrating pre-trained language models with natural language understanding, LAAs adapt flexibly to diverse scenarios, expanding AI’s potential in autonomous operations.

### III-BDesign and Implementation of LAAs

Central to the design of an agent is its neural sub-system–an LLM, which functions as the core controller or coordinator. The LLM orchestrates with the agent’s symbolic sub-system and external tools, including a planning and reasoning component for task decomposition and self-reflection, memory (both short-term and long-term), and a tool-use component that allows access to external information and functionalities.

- •
Agentic Workflow: An agentic workflow combines planning, reasoning, memory management, tool integration, and user interfaces with LLMs. Frameworks, such as LangChain \[ [58](https://arxiv.org/html/2407.08516v5#bib.bib58 "")\] and LlamaIndex \[ [59](https://arxiv.org/html/2407.08516v5#bib.bib59 "")\], help design these workflows.

- •
Planner and Reasoner: Advanced techniques such as chain-of-thought and tree-of-thought prompting \[ [60](https://arxiv.org/html/2407.08516v5#bib.bib60 "")\] break down tasks into sub-tasks, with self-reflection allowing agents to critique and refine outputs \[ [61](https://arxiv.org/html/2407.08516v5#bib.bib61 "")\].

- •
Memory Management: Incorporates short-term memory for context and long-term memory using external storage, such as vector databases, enabling efficient information retrieval and enhanced reasoning \[ [62](https://arxiv.org/html/2407.08516v5#bib.bib62 ""), [63](https://arxiv.org/html/2407.08516v5#bib.bib63 "")\].

- •
Tool-Use & Natural Language Interface (NLI) Integration: Agents can access external tools, APIs, and models, deciding when and how to utilize them based on task goals \[ [64](https://arxiv.org/html/2407.08516v5#bib.bib64 ""), [65](https://arxiv.org/html/2407.08516v5#bib.bib65 "")\]. In addition, An effective NLI interprets user requests and communicates actions \[ [66](https://arxiv.org/html/2407.08516v5#bib.bib66 "")\]. Techniques, such as ReAct and MRKL, provide structured interaction steps (thought, action, action input, observation) \[ [67](https://arxiv.org/html/2407.08516v5#bib.bib67 ""), [68](https://arxiv.org/html/2407.08516v5#bib.bib68 "")\].

By integrating these components, LAAs can tackle complex tasks. However, challenges like limited context windows, long-term planning, and reliable interfaces remain, necessitating ongoing research and development.

### III-CRethink LAAs from the Perspective of Neuro-symbolic AI

Neuro-symbolic AI combines the strengths of neural networks and symbolic reasoning, producing decision-making processes that are both explicit and interpretable. In autonomous agents enhanced by LLMs, the latest advancements in deep neural networks are harnessed, while task decomposition and planning are guided by symbolic AI principles — breaking complex tasks into discrete, logical steps that can be systematically analyzed and reasoned through \[ [69](https://arxiv.org/html/2407.08516v5#bib.bib69 "")\]. This fusion of symbolic structures and deep neural networks creates a powerful synergy, significantly boosting the capabilities of these agents.

#### Symbolic Modeling and Neural Representation

Classic symbolic AI represents knowledge using abstractions and symbols, utilizing explicit symbolic modeling such as rules and relationships to perform reasoning \[ [70](https://arxiv.org/html/2407.08516v5#bib.bib70 "")\]. This approach typically involves well-defined logic and structured knowledge bases, enabling systems to behave based on pre-defined rules. In contrast, LAAs, driven by language models, represent knowledge in a more distributed and implicit manner. Instead of relying on explicit symbols and rules, these agents leverage vast amounts of corpus and self-supervised pre-training on language models to infer patterns and relationships from raw text \[ [25](https://arxiv.org/html/2407.08516v5#bib.bib25 "")\]. The knowledge is embedded within the weights of LLMs, allowing for more flexible and context-driven reasoning. This advantage fundamentally contrasts with the rigidity of symbolic AI, providing LAAs with the ability to handle ambiguity and generate more human-like responses \[ [5](https://arxiv.org/html/2407.08516v5#bib.bib5 "")\].

#### Search-based Decision Making by Generation

Given a complex goal requiring multiple steps to achieve, existing agent technologies either harness symbolic AI to systematically explore the space of potential actions or employ reinforcement learning to optimize the trajectory of these actions, efficiently partitioning complex tasks into manageable subtasks \[ [54](https://arxiv.org/html/2407.08516v5#bib.bib54 "")\]. Within a LLM-empowered agent, the Chain-of-Thought (CoT) method guides LLMs to generate texts about intermediate reasoning steps, enhancing their cognitive task performance \[ [47](https://arxiv.org/html/2407.08516v5#bib.bib47 "")\]. By breaking tasks into logical sequences, CoT prompts encourage LLMs to structure their reasoning systematically. This method overcomes LLM limitations at the token level by enabling coherent, step-by-step elaboration of thought processes, improving problem-solving accuracy and reliability. More recently, Tree-of-Thought (ToT) prompting extends this approach by allowing LLMs to explore multiple reasoning paths simultaneously in a tree structure \[ [71](https://arxiv.org/html/2407.08516v5#bib.bib71 "")\] and the proposal of functional search over program generation, leveraging large language models (LLMs), successfully facilitates mathematical discoveries \[ [72](https://arxiv.org/html/2407.08516v5#bib.bib72 "")\]. These methods enhance LLM problem-solving abilities by promoting dynamic and reflective reasoning processes, closely mirroring symbolic reasoning techniques, on top of a neural basis.

#### Case-based Reasoning through In-context Learning

An agent must adapt to new situations, while traditional methods rely on either re-training neural networks or deducing examples of new situations into rules for better reasoning. Within a LLM-empowered agent, few-shot in-context learning (ICL) has been proposed to utilize given examples into a prompt to generate appropriate responses that solve problems without explicit re-training the LLM \[ [73](https://arxiv.org/html/2407.08516v5#bib.bib73 "")\]. This approach mimics the _case-based reasoning_, a fundamental concept in symbolic AI, by leveraging explicit knowledge and experiences to tackle new problems.
This enhances the model’s ability to generalize from specific examples, effectively creating a neuro-symbolic mapping from presented examples to desired outcomes.

#### Neuro-symbolic Integration Driven by Emergent Abilities

The emergent abilities of LLMs, such as contextual understanding, sequential reasoning, goal reformulation, and task decomposition, are surged by over-parameterized architectures and extensive pre-training corpora \[ [46](https://arxiv.org/html/2407.08516v5#bib.bib46 "")\]. Combining well-designed rules with the emergent abilities of LLMs enables agents to create and follow complex workflows, known as agentic workflows. By prompting large language models with instructions like “let’s think step by step”, these models analogise human’s reasoning processes and can exhibit logical and mathematical reasoning, thereby enhancing their structured reasoning skills \[ [12](https://arxiv.org/html/2407.08516v5#bib.bib12 ""), [13](https://arxiv.org/html/2407.08516v5#bib.bib13 "")\]. This agentic approach allows LLMs to not only process but also proactively generate structured, logical, and adaptive reasoning pathways \[ [56](https://arxiv.org/html/2407.08516v5#bib.bib56 "")\], significantly improving their problem-solving and decision-making capabilities, marking a pivotal evolution in neuro-symbolic AI technologies.

## IV Discussions and Future Directions

In this section, we discuss the LLM-empowered autonomous agent by comparing it with an alternative neuro-symbolic approach—the Knowledge Graph—and then highlight future directions for this technology.

### IV-AComparative Analysis: LAAs versus KGs

Previous sections have presented LAAs and KGs, both of which exemplify neuro-symbolic approaches to AI. We here compare these two methodologies to highlight the superior positioning of LAAs in the current wave of AI advancements.

KGs harness the power of symbolic AI, organizing domain-specific knowledge through explicit relationships and rules. This design makes them highly effective in static environments where precision, interpretability, and predefined schemas are crucial. Their logical reasoning capabilities ensure that outputs are consistent and verifiable, which is paramount for applications needing clarity and exactitude in knowledge modeling \[ [74](https://arxiv.org/html/2407.08516v5#bib.bib74 "")\]. In addition, the scalability of KGs is inherently limited by their requirements of explicit schema definitions and manual updates \[ [75](https://arxiv.org/html/2407.08516v5#bib.bib75 "")\]. As the volume of data grows, the complexity of managing and querying the graph increases significantly. The maintenance of a large-scale KG demands substantial computational resources and human expertise, affecting efficiency and agility in evolving environments.

On the other hand, LAAs are designed with a more dynamic and flexible approach. By combining the language comprehension and generation abilities of neural networks with the structured reasoning of symbolic AI, these agents are equipped to tackle a wide range of complex tasks. The implicit knowledge stored in neural networks enables context-sensitive responses and seamless adaptation to changing environments \[ [76](https://arxiv.org/html/2407.08516v5#bib.bib76 "")\]. Additionally, LLMs efficiently compress vast corpora into a learnable network, making these agents highly scalable. Once trained, the models can be fine-tuned with additional data at a fraction of the cost and effort required for updating knowledge graphs, and can even support in-context learning without fine-tuning. As a result, LLM-powered agents can handle larger datasets with ease and even process online data to respond to real-time changes effectively.

Furthermore, the advanced reasoning mechanisms employed by LAAs, such as CoT \[ [47](https://arxiv.org/html/2407.08516v5#bib.bib47 "")\] and ToT \[ [71](https://arxiv.org/html/2407.08516v5#bib.bib71 "")\], enable them to break down and solve complex problems effectively through analogising human reasoning steps \[ [12](https://arxiv.org/html/2407.08516v5#bib.bib12 "")\]. These methods mitigate the limitations of token-level constraints in LLMs, fostering a more robust and contextually aware decision-making process. As a result, LAAs are poised to drive future innovations in AI, offering more versatile and intelligent solutions than their knowledge graph counterparts.

### IV-BFuture Directions

Following prior discussions, we propose several future research directions aimed at enhancing the current landscape of LAAs.

https://arxiv.org/html/2407.08516v5/x4.pngFigure 4: An Illustrative Example of Program-Proof-of-Thoughts (P2oT) for Mathematical Proof Verification

### IV-CNeuro-vector-symbolic Integrative Intelligence

Current agentic reasoning approaches emulate human reasoning steps explicitly \[ [12](https://arxiv.org/html/2407.08516v5#bib.bib12 "")\]. For instance, when an agent receives a user’s request, it retrieves similar cases and enhances its actions through in-context learning, and for ambiguous requests, the agent prompts the LLM to clarify and rewrite the request in various forms \[ [77](https://arxiv.org/html/2407.08516v5#bib.bib77 "")\]. This process involve extracting vectors for each rewritten request and performing multi-vector retrieval, improving context understanding and generative performance but increasing computational load. A vector-centric perspective, utilizing encoder-decoder architectures such as GritLM \[ [78](https://arxiv.org/html/2407.08516v5#bib.bib78 "")\] that prompt generative models for instructional text encoding/vectorization, implicit neural reasoners that extend transformers with causal relation graphs for enhanced long-range reasoning \[ [79](https://arxiv.org/html/2407.08516v5#bib.bib79 "")\] with latent vectors and attention matrices, and vector-symbolic architectures (VSAs) \[ [80](https://arxiv.org/html/2407.08516v5#bib.bib80 "")\], could significantly address this problem. Specifically, the VSA employs high-dimensional vectors to encode and manipulate information, allowing the representation of complex structures and relationships compactly and contextually \[ [80](https://arxiv.org/html/2407.08516v5#bib.bib80 "")\]. It models the cognitive and reasoning processes as _algebraic operations_ in the vector space. Combining VSAs with LLMs could enhance cognitive capabilities, enabling precise multi-step decision-making, with applications in scientific discovery, such as solving Raven’s progressive matrices \[ [81](https://arxiv.org/html/2407.08516v5#bib.bib81 "")\], thus accelerating the convergence between connectionist and symbolic paradigms through computable vectorization.

### IV-DProgram-Proof-of-Thoughts Reasoning

We here illustrate the proposal of Program-Proof-of-Thoughts (P2oT) for agentic reasoning in a rigorous manner, building on the methodologies of CoT and ToT prompting. Specifically, P2oT decomposes complex reasoning processes into a series of propositions organized in linear or tree structures. It leverages the programming language for program proofs, such as Dafny \[ [82](https://arxiv.org/html/2407.08516v5#bib.bib82 "")\] or Lean \[ [83](https://arxiv.org/html/2407.08516v5#bib.bib83 "")\], to model and verify these propositions. Future research should focus on refining proposition modeling and verification by prompting LLMs for code generation \[ [84](https://arxiv.org/html/2407.08516v5#bib.bib84 "")\], improving integration with external theorem provers and assertion verifiers (e.g., Dafny and Lean), and scaling P2oT to handle multi-modal data for advanced reasoning. Further, automating code generation, optimizing hybrid P2oT/CoT/ToT models, incorporating self-verification and self-correction, and adopting P2oT into domain-specific applications, including logical deduction and scientific discovery can significantly advance its capabilities \[ [72](https://arxiv.org/html/2407.08516v5#bib.bib72 "")\]. Figure [4](https://arxiv.org/html/2407.08516v5#S4.F4 "Figure 4 ‣ IV-B Future Directions ‣ IV Discussions and Future Directions ‣ Converging Paradigms: The Synergy of Symbolic and Connectionist AI in LLM-Empowered Autonomous Agents") demonstrates the use of the P2oT framework to verify a basic mathematical proof that for any even integer n𝑛nitalic\_n, the sum of the first n𝑛nitalic\_n positive integers is an even number. By decomposing the problem into distinct, verifiable propositions and using Dafny for formal verification, this example highlights the structured and rigorous approach of P2oT in logical reasoning and verification.

## V Conclusions

In conclusion, the synthesis of connectionist and symbolic paradigms, particularly through the rise of LLM-empowered Autonomous Agents (LAAs), marks a pivotal evolution in the field of AI, especially the neuro-symbolic AI. This paper has highlighted the historical context and the ongoing convergence of symbolic reasoning and neural network-based methods, underscoring how LAAs leverage the text-based knowledge representation and generative capabilities of LLMs to achieve logical reasoning and decision-making. By contrasting LAAs with Knowledge Graphs (KGs), we have demonstrated the unique advantages of LAAs in mimicking human-like reasoning processes, scaling effectively with large datasets, and leveraging in-context learning without extensive re-training. Promising directions such as neuro-vector-symbolic architectures and program-proof-of-thoughts (P2oT) prompting are on the horizon, potentially enhancing the agentic reasoning capabilities of AI further. These insights not only encapsulate the transformative potential of current AI technologies but also provide a clear trajectory for future research, fostering a deeper understanding and more advanced applications of neuro-symbolic AI.

## References

- \[1\]↑
Yann LeCun, Yoshua Bengio, and Geoffrey Hinton.

Deep learning.

Nature, 521(7553):436–444, 2015.

- \[2\]↑
Allen Newell and Herbert A Simon.

Computer science as empirical inquiry: Symbols and search.

In ACM Turing award lectures, page 1975. 2007.

- \[3\]↑
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.

Imagenet classification with deep convolutional neural networks.

Advances in neural information processing systems, 25, 2012.

- \[4\]↑
Edward Shortliffe.

Computer-based medical consultations: MYCIN, volume 2.

Elsevier, 2012.

- \[5\]↑
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell,
et al.

Language models are few-shot learners.

Advances in neural information processing systems,
33:1877–1901, 2020.

- \[6\]↑
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya
Sutskever, et al.

Language models are unsupervised multitask learners.

OpenAI blog, 1(8):9, 2019.

- \[7\]↑
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric
Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg,
et al.

Sparks of artificial general intelligence: Early experiments with
gpt-4.

arXiv preprint arXiv:2303.12712, 2023.

- \[8\]↑
Haoyi Xiong, Jiang Bian, Sijia Yang, Xiaofei Zhang, Linghe Kong, and Daqing
Zhang.

Natural language based context modeling and reasoning with llms: A
tutorial.

arXiv preprint arXiv:2309.15074, 2023.

- \[9\]↑
Jonathan St BT Evans.

In two minds: dual-process accounts of reasoning.

Trends in cognitive sciences, 7(10):454–459, 2003.

- \[10\]↑
Yoshua Bengio.

Deep learning for system 2 processing.

AAAI 2020, 2020.

- \[11\]↑
Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Marttinen, and S Yu Philip.

A survey on knowledge graphs: Representation, acquisition, and
applications.

IEEE Transactions on Neural Networks and Learning Systems,
33(2):494–514, 2021.

- \[12\]↑
Taylor Webb, Keith J Holyoak, and Hongjing Lu.

Emergent analogical reasoning in large language models.

Nature Human Behaviour, 7(9):1526–1541, 2023.

- \[13\]↑
James WA Strachan, Dalila Albergo, Giulia Borghini, Oriana Pansardi, Eugenio
Scaliti, Saurabh Gupta, Krati Saxena, Alessandro Rufo, Stefano Panzeri, Guido
Manzi, et al.

Testing theory of mind in large language models and humans.

Nature Human Behaviour, pages 1–11, 2024.

- \[14\]↑
Artur d’Avila Garcez and Luis C Lamb.

Neurosymbolic ai: The 3 rd wave.

Artificial Intelligence Review, 56(11):12387–12406, 2023.

- \[15\]↑
Frank Rosenblatt.

The perceptron: a probabilistic model for information storage and
organization in the brain.

Psychological review, 65(6):386, 1958.

- \[16\]↑
David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams.

Learning representations by back-propagating errors.

Nature, 323(6088):533–536, 1986.

- \[17\]↑
Allen Newell and Herbert Simon.

The logic theory machine–a complex information processing system.

IRE Transactions on information theory, 2(3):61–79, 1956.

- \[18\]↑
Bruce G Buchanan and Edward A Feigenbaum.

Dendral and meta-dendral: Their applications dimension.

Artificial intelligence, 11(1-2):5–24, 1978.

- \[19\]↑
Ashok Kumar Goel.

Integration of case-based reasoning and model-based reasoning
for adaptive design problem-solving.

The Ohio State University, 1989.

- \[20\]↑
Zachary C Lipton.

The mythos of model interpretability: In machine learning, the
concept of interpretability is both important and slippery.

Queue, 16(3):31–57, 2018.

- \[21\]↑
Edward A Feigenbaum et al.

The art of artificial intelligence: Themes and case studies of
knowledge engineering.

1977.

- \[22\]↑
Charles Elkan and Russell Greiner.

Building large knowledge-based systems: Representation and inference
in the cyc project: Db lenat and rv guha, 1993.

- \[23\]↑
Yoshua Bengio, Yann Lecun, and Geoffrey Hinton.

Deep learning for ai.

Communications of the ACM, 64(7):58–65, 2021.

- \[24\]↑
Artur SD’Avila Garcez, Luis C Lamb, and Dov M Gabbay.

Neural-symbolic cognitive reasoning.

Springer Science & Business Media, 2008.

- \[25\]↑
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.

Bert: Pre-training of deep bidirectional transformers for language
understanding.

arXiv preprint arXiv:1810.04805, 2018.

- \[26\]↑
David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja
Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton,
et al.

Mastering the game of go without human knowledge.

Nature, 550(7676):354–359, 2017.

- \[27\]↑
World Wide Web Consortium (W3C).

Resource description framework (rdf) model and syntax specification,
1999.

Retrieved from
https://www.w3.org/TR/1999/REC-rdf-syntax-19990222/.

- \[28\]↑
Tim Berners-Lee, James Hendler, and Ora Lassila.

The semantic web: A new form of web content that is meaningful to
computers will unleash a revolution of new possibilities.

In Linking the World’s Information: Essays on Tim
Berners-Lee’s Invention of the World Wide Web, pages 91–103. 2023.

- \[29\]↑
Grigoris Antoniou and Frank Van Harmelen.

A semantic web primer.

MIT press, 2004.

- \[30\]↑
Thomas R Gruber.

A translation approach to portable ontology specifications.

Knowledge Acquisition, 5(2):199–220, 1993.

- \[31\]↑
Stanley Kok and Pedro Domingos.

Learning the structure of markov logic networks.

In Proceedings of the 22nd International Conference on Machine
Learning, pages 441–448, 2005.

- \[32\]↑
Maximilian Nickel, Kevin Murphy, Volker Tresp, and Evgeniy Gabrilovich.

A review of relational machine learning for knowledge graphs.

Proceedings of the IEEE, 104(1):11–33, 2015.

- \[33\]↑
Thomas N Kipf and Max Welling.

Semi-supervised classification with graph convolutional networks.

In International Conference on Learning Representations, 2022.

- \[34\]↑
Quan Wang, Zhendong Mao, Bin Wang, and Li Guo.

Knowledge graph embedding: A survey of approaches and applications.

IEEE Transactions on Knowledge and Data Engineering,
29(12):2724–2743, 2017.

- \[35\]↑
Sepp Hochreiter and Jürgen Schmidhuber.

Long short-term memory.

Neural computation, 9(8):1735–1780, 1997.

- \[36\]↑
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin.

Attention is all you need.

Advances in neural information processing systems, 30, 2017.

- \[37\]↑
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael
Matena, Yanqi Zhou, Wei Li, and Peter J Liu.

Exploring the limits of transfer learning with a unified text-to-text
transformer.

Journal of machine learning research, 21(140):1–67, 2020.

- \[38\]↑
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya,
Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al.

Gpt-4 technical report.

arXiv preprint arXiv:2303.08774, 2023.

- \[39\]↑
Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac,
Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al.

Gemini: a family of highly capable multimodal models.

arXiv preprint arXiv:2312.11805, 2023.

- \[40\]↑
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra,
Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian
Gehrmann, et al.

Palm: Scaling language modeling with pathways.

Journal of Machine Learning Research, 24(240):1–113, 2023.

- \[41\]↑
Marah Abdin, Sam Ade Jacobs, Ammar Ahmad Awan, Jyoti Aneja, Ahmed Awadallah,
Hany Awadalla, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Harkirat Behl,
et al.

Phi-3 technical report: A highly capable language model locally on
your phone.

arXiv preprint arXiv:2404.14219, 2024.

- \[42\]↑
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric
Hambro, Faisal Azhar, et al.

Llama: Open and efficient foundation language models.

arXiv preprint arXiv:2302.13971, 2023.

- \[43\]↑
Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu,
Hangliang Ding, Kaiwen Men, Kejuan Yang, et al.

Agentbench: Evaluating llms as agents.

arXiv preprint arXiv:2308.03688, 2023.

- \[44\]↑
Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su,
Shengding Hu, Yulin Chen, Chi-Min Chan, Weize Chen, et al.

Parameter-efficient fine-tuning of large-scale pre-trained language
models.

Nature Machine Intelligence, 5(3):220–235, 2023.

- \[45\]↑
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela
Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al.

Training language models to follow instructions with human feedback.

Advances in neural information processing systems,
35:27730–27744, 2022.

- \[46\]↑
Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo.

Are emergent abilities of large language models a mirage?

Advances in Neural Information Processing Systems, 36, 2024.

- \[47\]↑
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V
Le, Denny Zhou, et al.

Chain-of-thought prompting elicits reasoning in large language
models.

Advances in neural information processing systems,
35:24824–24837, 2022.

- \[48\]↑
Junyi Li, Xiaoxue Cheng, Wayne Xin Zhao, Jian-Yun Nie, and Ji-Rong Wen.

Halueval: A large-scale hallucination evaluation benchmark for large
language models.

In Proceedings of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 6449–6464, 2023.

- \[49\]↑
Pattie Maes.

Modeling adaptive autonomous agents.

Artificial life, 1(1\_2):135–162, 1993.

- \[50\]↑
Stefano V Albrecht and Peter Stone.

Autonomous agents modelling other agents: A comprehensive survey and
open problems.

Artificial Intelligence, 258:66–95, 2018.

- \[51\]↑
Ronald C Arkin.

Behavior-based robotics.

MIT press, 1998.

- \[52\]↑
Yara Rizk, Mariette Awad, and Edward W Tunstel.

Cooperative heterogeneous multi-robot systems: A survey.

ACM Computing Surveys (CSUR), 52(2):1–31, 2019.

- \[53\]↑
Daphne Koller and Nir Friedman.

Probabilistic graphical models: principles and techniques.

MIT press, 2009.

- \[54\]↑
Richard S Sutton and Andrew G Barto.

Reinforcement learning: An introduction.

MIT press, 2018.

- \[55\]↑
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan
Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al.

A survey on large language model based autonomous agents.

Frontiers of Computer Science, 18(6):186345, 2024.

- \[56\]↑
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming
Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al.

The rise and potential of large language model based agents: A
survey.

arXiv preprint arXiv:2309.07864, 2023.

- \[57\]↑
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu,
Beibin Li, Li Jiang, Xiaoyun Zhang, and Chi Wang.

Autogen: Enabling next-gen llm applications via multi-agent
conversation framework.

arXiv preprint arXiv:2308.08155, 2023.

- \[58\]↑
Oguzhan Topsakal and Tahir Cetin Akinci.

Creating large language model applications utilizing langchain: A
primer on developing llm apps fast.

In International Conference on Applied Engineering and Natural
Sciences, volume 1, pages 1050–1056, 2023.

- \[59\]↑
Jerry Liu.

LlamaIndex, 11 2022.

- \[60\]↑
Chan Hee Song, Jiaman Wu, Clayton Washington, Brian M Sadler, Wei-Lun Chao, and
Yu Su.

Llm-planner: Few-shot grounded planning for embodied agents with
large language models.

In Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 2998–3009, 2023.

- \[61\]↑
Bill Yuchen Lin, Yicheng Fu, Karina Yang, Faeze Brahman, Shiyu Huang, Chandra
Bhagavatula, Prithviraj Ammanabrolu, Yejin Choi, and Xiang Ren.

Swiftsage: A generative agent with fast and slow thinking for complex
interactive tasks.

Advances in Neural Information Processing Systems, 36, 2024.

- \[62\]↑
Jeff Johnson, Matthijs Douze, and Hervé Jégou.

Billion-scale similarity search with gpus.

IEEE Transactions on Big Data, 7(3):535–547, 2019.

- \[63\]↑
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang.

Retrieval augmented language model pre-training.

In International conference on machine learning, pages
3929–3938. PMLR, 2020.

- \[64\]↑
Scott Reed, Konrad Zolna, Emilio Parisotto, Sergio Gómez Colmenarejo,
Alexander Novikov, Gabriel Barth-maron, Mai Giménez, Yury Sulsky, Jackie
Kay, Jost Tobias Springenberg, et al.

A generalist agent.

Transactions on Machine Learning Research.

- \[65\]↑
Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Yueting
Zhuang.

Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging
face.

Advances in Neural Information Processing Systems, 36, 2024.

- \[66\]↑
Jianfeng Gao, Michel Galley, and Lihong Li.

Neural approaches to conversational ai.

In The 41st international ACM SIGIR conference on research &
development in information retrieval, pages 1371–1374, 2018.

- \[67\]↑
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan,
and Yuan Cao.

React: Synergizing reasoning and acting in language models.

arXiv preprint arXiv:2210.03629, 2022.

- \[68\]↑
Ehud Karpas, Omri Abend, Yonatan Belinkov, Barak Lenz, Opher Lieber, Nir
Ratner, Yoav Shoham, Hofit Bata, Yoav Levine, Kevin Leyton-Brown, et al.

Mrkl systems: A modular, neuro-symbolic architecture that combines
large language models, external knowledge sources and discrete reasoning.

arXiv preprint arXiv:2205.00445, 2022.

- \[69\]↑
Artur d’Avila Garcez, Tarek R Besold, Luc De Raedt, Peter Földiak, Pascal
Hitzler, Thomas Icard, Kai-Uwe Kühnberger, Luis C Lamb, Risto
Miikkulainen, and Daniel L Silver.

Neural-symbolic learning and reasoning: contributions and challenges.

In 2015 AAAI Spring Symposium Series, 2015.

- \[70\]↑
Ronald Brachman and Hector Levesque.

Knowledge representation and reasoning.

Morgan Kaufmann, 2004.

- \[71\]↑
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and
Karthik Narasimhan.

Tree of thoughts: Deliberate problem solving with large language
models.

Advances in Neural Information Processing Systems, 36, 2024.

- \[72\]↑
Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej
Balog, M Pawan Kumar, Emilien Dupont, Francisco JR Ruiz, Jordan S Ellenberg,
Pengming Wang, Omar Fawzi, et al.

Mathematical discoveries from program search with large language
models.

Nature, 625(7995):468–475, 2024.

- \[73\]↑
Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh
Hajishirzi, and Luke Zettlemoyer.

Rethinking the role of demonstrations: What makes in-context learning
work?

arXiv preprint arXiv:2202.12837, 2022.

- \[74\]↑
Lauren Nicole DeLong, Ramon Fernández Mir, and Jacques D Fleuriot.

Neurosymbolic ai for reasoning over knowledge graphs: A survey.

arXiv preprint arXiv:2302.07200, 2023.

- \[75\]↑
Ciyuan Peng, Feng Xia, Mehdi Naseriparsa, and Francesco Osborne.

Knowledge graphs: Opportunities and challenges.

Artificial Intelligence Review, 56(11):13071–13102, 2023.

- \[76\]↑
Sang Michael Xie, Aditi Raghunathan, Percy Liang, and Tengyu Ma.

An explanation of in-context learning as implicit bayesian inference.

arXiv preprint arXiv:2111.02080, 2021.

- \[77\]↑
Arian Askari, Roxana Petcu, Chuan Meng, Mohammad Aliannejadi, Amin Abolghasemi,
Evangelos Kanoulas, and Suzan Verberne.

Self-seeding and multi-intent self-instructing llms for generating
intent-aware information-seeking dialogs.

arXiv preprint arXiv:2402.11633, 2024.

- \[78\]↑
Niklas Muennighoff, Hongjin Su, Liang Wang, Nan Yang, Furu Wei, Tao Yu,
Amanpreet Singh, and Douwe Kiela.

Generative representational instruction tuning.

arXiv preprint arXiv:2402.09906, 2024.

- \[79\]↑
Petar Veličković and Charles Blundell.

Neural algorithmic reasoning.

Patterns, 2(7), 2021.

- \[80\]↑
Pentti Kanerva.

Hyperdimensional computing: An introduction to computing in
distributed representation with high-dimensional random vectors.

Cognitive computation, 1:139–159, 2009.

- \[81\]↑
Michael Hersche, Mustafa Zeqiri, Luca Benini, Abu Sebastian, and Abbas Rahimi.

A neuro-vector-symbolic architecture for solving raven’s
progressive matrices.

Nature Machine Intelligence, 5(4):363–375, 2023.

- \[82\]↑
K Rustan M Leino.

Dafny: An automatic program verifier for functional correctness.

In International conference on logic for programming artificial
intelligence and reasoning, pages 348–370. Springer, 2010.

- \[83\]↑
Leonardo de Moura and Sebastian Ullrich.

The lean 4 theorem prover and programming language.

In Automated Deduction–CADE 28: 28th International Conference
on Automated Deduction, Virtual Event, July 12–15, 2021, Proceedings 28,
pages 625–635. Springer, 2021.

- \[84\]↑
Eric Mugnier, Emmanuel Anaya Gonzalez, Ranjit Jhala, Nadia Polikarpova, and
Yuanyuan Zhou.

Laurel: Generating dafny assertions using large language models.

arXiv preprint arXiv:2405.16792, 2024.

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

Tomaž Bratanič,

Kumar Harsh

September 11, 2024

14 min read

https://dist.neo4j.com/wp-content/uploads/20240911090339/fine-tuning-vs-rag.png

Many organizations are considering LLMs for business use cases like answering questions as chatbots or virtual assistants or generating creative text. However, they usually run into limitations such as knowledge cutoff, hallucinations, and the lack of user customization.

Two approaches that address these challenges are **fine-tuning** and **retrieval-augmented generation**. Fine-tuning an LLM involves a supervised training phase, where question-answer pairs are provided to optimize the LLM’s performance. Conversely, in retrieval-augmented generation (RAG), the LLM serves as a natural language interface to access external information, which means it doesn’t rely only on its internal knowledge to produce answers.

This article explores the pros and cons of using fine-tuning and RAG to curb the limitations of LLMs. We also consider the implications of each approach for organizations that already use knowledge graphs to organize and manage their data.

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

### Getting Started With Neo4j & LLM

We’re offering a free GraphAcademy course on how to integrate Neo4j knowledge graph with Generative AI models using LangChain.

## The Developer’s Guide: How to Build a Knowledge Graph

This ebook gives you a step-by-step walkthrough on building your first knowledge graph.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="how-to-solve-5-common-rag-failures-with-knowledge-graphs.md">
<details>
<summary>how-to-solve-5-common-rag-failures-with-knowledge-graphs</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/>

https://cdn.hashnode.com/res/hashnode/image/upload/v1762904270014/5ebeec2b-0823-4f59-bdd7-bf37cb68a978.png

You may have built a Retrieval-Augmented Generation (RAG) pipeline to connect a vector store to a powerful LLM. And RAG pipelines are incredibly effective at grounding models in factual, up-to-date knowledge. But if you've worked with them long enough, you've likely hit a wall.

The system is great at answering "What is X?" but falls apart when you ask, "How does X relate to Y, and what happened after Z?".

The problem is that standard RAG, by its very nature, breaks context. It chops documents into isolated chunks, finds them based on semantic similarity, and hopes the LLM can piece the puzzle back together. This approach is blind to the relational context—the web of timelines, causes, and connections—that gives facts their meaning.

When queries require synthesizing information across multiple documents or complex, multi-step reasoning, standard RAG fails.

In this article, I’ll give you a practical, code-first guide to solving this problem. We'll move beyond simple vector search by implementing a robust, graph-based pattern to build more reliable, knowledge-aware systems.

## Table of Contents:

- [Prerequisites](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-prerequisites)

- [The Brittle Baseline: Our Standard RAG Setup](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-the-brittle-baseline-our-standard-rag-setup)

- [A More Robust Implementation: The KnowledgeGraph](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-a-more-robust-implementation-the-knowledgegraph)

  - [What is a Knowledge Graph?](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-what-is-a-knowledge-graph)

  - [Why is this More Effective?](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-why-is-this-more-effective)
- [5 RAG Failures and Their Graph-Based Solutions](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-5-rag-failures-and-their-graph-based-solutions)

  - [Pattern 1: The Multi-Hop Failure](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-pattern-1-the-multi-hop-failure)

  - [Pattern 2: The Causal Synthesis Failure](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-pattern-2-the-causal-synthesis-failure)

  - [Pattern 3: The Entity Ambiguity Trap](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-pattern-3-the-entity-ambiguity-trap)

  - [Pattern 4: The Contradictory Information Failure](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-pattern-4-the-contradictory-information-failure)

  - [Pattern 5: The Implicit Relationship Hallucination](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-pattern-5-the-implicit-relationship-hallucination)
- [Final Thoughts](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/#heading-final-thoughts)


### Prerequisites

This is a practical, code-first guide intended for developers and engineers who have some experience with RAG. To follow along, you should have the following:

#### Conceptual Knowledge

- A solid understanding of what Retrieval-Augmented Generation (RAG) is and its basic components (like vector stores and LLMs).

- Familiarity with basic graph concepts (nodes, edges, and relationships) is also helpful.


#### Technical Setup

- A Python environment.

- An active Google API Key to use the Gemini API.

- The Python libraries `langchain`, `langchain_google_genai`, `faiss-cpu`, and `networkx` installed.


## The Brittle Baseline: Our Standard RAG Setup

First, let's establish our baseline. This is a standard, "naïve" RAG pipeline using LangChain and the Gemini API. It ingests a list of `Document` objects, embeds them, and uses a FAISS vector store to retrieve the top-k chunks to answer a question.

This `create_rag_chain` function will serve as our point of comparison.

```python
# Install necessary libraries
# !pip install -q -U langchain langchain_google_genai faiss-cpu networkx

import os
import networkx as nx
from collections import defaultdict
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema.document import Document
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# --- Configure API Key (example) ---
# from google.colab import userdata
# GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
# os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

# --- Initialize Models ---
# Make sure your API key is set in your environment
llm = GoogleGenerativeAI(model="gemini-1.5-pro-latest")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def create_rag_chain(docs):
    """Creates a simple RAG chain using FAISS as the vector store."""

    # Create vector store from documents
    vectorstore = FAISS.from_documents(docs, embeddings)
    # K=3 means it will retrieve the top 3 most relevant chunks
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """
    Answer the following question based ONLY on the context provided.
    If the context doesn't contain the answer, say "I don't have enough information from the context."

    CONTEXT:
    {context}

    QUESTION:
    {question}
    """

    prompt = PromptTemplate.from_template(template)

    # Build the chain
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
```

## A More Robust Implementation: The KnowledgeGraph

### What is a Knowledge Graph?

At its core, a knowledge graph (KG) is a way of storing data as a network of nodes and edges.

- **Nodes** represent entities: `people`, `companies`, `concepts`, or `events`.

- **Edges** represent the explicit, labeled relationships between them: `ceo_of`, `attended`, or `partners_with`.


Instead of storing a document like "Jim Farley is the CEO of Ford," you store two nodes (`Jim Farley`, `Ford`) connected by a directed edge (`ceo_of`).

### Why is this More Effective?

This structure is more effective because it preserves and makes relationships a first-class citizen.

Standard RAG relies on "semantic similarity". It's good at finding text chunks that _sound like_ your query. But it’s "blind to the relational context" – the very thing you need for complex questions.

The graph-based approach solves this. When a query requires multi-step reasoning, you don't just search for similar text. You traverse a structured, explicit path in the graph. This allows the system to:

1. **Follow chains of logic:** It can answer multi-hop questions by finding a literal path from one node to another (for example, `F-150` → `made_by` → `Ford` → `ceo` → `Jim Farley`).

2. **Disambiguate entities:** It can use node attributes (like `type: "company"`) to distinguish between two entities with the same name.

3. **Resolve contradictions:** It can store metadata (like dates) directly _on the edge_ to programmatically determine the most current fact.


You move from "guessing from a cloud of semantically similar text" to querying a "global memory" of how facts are explicitly connected.

Here is the practical implementation of our `KnowledgeGraph`. This class uses `networkx` to store the nodes and edges we just discussed, and includes specific methods to run the structured query patterns needed to solve our RAG failures.

```python
class KnowledgeGraph:
    """
    A wrapper around networkx.DiGraph to store and query
    explicit entities and their relationships.
    """
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_data(self, nodes=None, edges=None):
        """Populates the graph with nodes and edges."""
        if nodes:
            for node, attrs in nodes:
                self.graph.add_node(node, **attrs)
        if edges:
            for u, v, attrs in edges:
                self.graph.add_edge(u, v, **attrs)

    # --- Query Patterns ---

    def query_multi_hop_path(self, source, target):
        """
        Pattern 1: Solves multi-hop queries by finding a path.
        """
        try:
            path = nx.shortest_path(self.graph, source=source, target=target)
            # Format the answer based on the discovered path
            return f"{path[-2]} attended {path[-1]}."
        except nx.NetworkXNoPath:
            return "Could not find a connection."

    def query_with_conflict_resolution(self, entity, relation, time_attr="year"):
        """
        Pattern 4: Resolves contradictions using metadata (like timestamps)
        stored on the edges.
        """
        candidates = []
        for neighbor in self.graph.neighbors(entity):
            edge_data = self.graph.get_edge_data(entity, neighbor)
            if edge_data.get("label") == relation:
                candidates.append((neighbor, edge_data.get(time_attr, 0)))

        if not candidates:
            return "No information found."

        # Sort by the time attribute, descending, and take the latest
        latest = sorted(candidates, key=lambda item: item[1], reverse=True)[0]
        return f"{latest[0]} (as of {latest[1]})"

    def query_disambiguated(self, entity_name, entity_type, attribute_key):
        """
        Pattern 3: Uses node 'type' attributes to disambiguate
        entities with the same name.
        """
        for node, attrs in self.graph.nodes(data=True):
            # Find the node that matches both name and type
            if entity_name in node and attrs.get("type") == entity_type:
                # Return the requested attribute
                year = attrs['year']
                product = attrs[attribute_key]
                return f"{node}'s first product was the {product} in {year}."
        return "Cannot disambiguate entity."

    def query_explicit_relation(self, source_node, relation_label):
        """
        Pattern 5: Finds partners based on an explicit edge label,
        preventing semantic 'bleed-over' from unrelated entities.
        """
        partners = \
            [v for u, v, data in self.graph.edges(data=True)\
            if u == source_node and data.get('label') == relation_label]

        if partners:
            return f"{source_node} partnered with {', '.join(partners)}."
        return f"No partners found for {source_node}."

# A helper function for Pattern 2 (Causal Rules)
# This logic is more rule-based but can be backed by a graph
def query_causal_chain(facts):
    """
    Pattern 2: Synthesizes a direct conclusion by following a
    chain of causal rules.
    """
    try:
        if facts["John"]["takes"] == "aspirin":
            if facts["aspirin"]["is_a"] == "blood thinner":
                if facts["blood thinner"]["risk_for"] == "surgery":
                    return "John is NOT safe due to increased bleeding risk from aspirin, a blood thinner."
    except KeyError:
        pass # Fall through to default
    return "Insufficient information to determine risk."
```

## 5 RAG Failures and Their Graph-Based Solutions

Let's run five scenarios to see how our standard RAG chain performs against our new `KnowledgeGraph`.

### Pattern 1: The Multi-Hop Failure

The multi-hop failure occurs when an answer requires connecting multiple, separate facts – a chain of reasoning that RAG often breaks.

- **Query:** "Which university did the CEO of the company that makes the F-150 attend?"

- **Problem:** A standard retriever might get chunks for `F-150 -> Ford` and `Jim Farley -> CEO`, but miss the `Jim Farley -> Georgetown` chunk. The chain is broken.


#### Why the Naïve RAG Fails

The retriever's job is to find the `top-k=3` chunks that are **semantically similar** to the entire query. When the user asks, "Which university did the CEO of the company that makes the F-150 attend?", the retriever will search our 6-document list and will likely retrieve:

1. The chunk about the **University of Michigan** (because of the words "university" and "car companies").

2. The chunk about **Jim Farley** (because of "CEO," "Ford," and "F-150 line").

3. The chunk about the **F-150 engine options** (because of "F-150").


The `top-k=3` context handed to the LLM is now full of irrelevant facts. The one chunk that contains the _actual_ answer ("...Mr Farley... from Georgetown University") is semantically too far from the main query and is **never retrieved**. The LLM fails not because it's unintelligent, but because it was never given the correct piece of the puzzle.

#### Why the GraphRAG Succeeds

The knowledge graph doesn't care about semantic similarity. It performs a deterministic traversal of explicit, verified relationships.

We ask for the _path_ from the `F-150` node to the `Georgetown University` node. The graph follows the chain we defined: `F-150` → `made_by` → `Ford Motor Company` → `ceo` → `Jim Farley` → `attended` → `Georgetown University`. It can't fail or be distracted by the "noise" documents because it's not searching – it's **navigating** a pre-built map.

```python
# --Naive RAG
docs_s1 = [\
    # --- The 3 "Answer" Chunks ---\
    Document(page_content="The Ford F-150 is a full-size pickup truck made by Ford Motor Company."),\
    Document(page_content="Jim Farley is the current CEO of Ford Motor Company."),\
    Document(page_content="Mr. Farley received his undergraduate degree from Georgetown University."),\
\
    # --- The 3 "Noise" Chunks (to distract the retriever) ---\
    Document(page_content="The University of Michigan is renowned for its automotive engineering program, which partners with many car companies."),\
    Document(page_content="The F-150 comes with several engine options, including a powerful 3.5L EcoBoost V6."),\
    Document(page_content="Mary Barra, the CEO of General Motors, is a major competitor to Ford and its F-150 line.")\
]
query_s1 = "Which university did the CEO of the company that makes the F-150 attend?"
rag_chain_s1 = create_rag_chain(docs_s1) # This uses top_k=3
print(f"Naive RAG Answer: {rag_chain_s1.invoke(query_s1)}")
#
# GraphRAG Pattern
graph_s1 = KnowledgeGraph()
edges_s1 = [\
    ("F-150", "Ford Motor Company", {"label": "made_by"}),\
    ("Ford Motor Company", "Jim Farley", {"label": "ceo"}),\
    ("Jim Farley", "Georgetown University", {"label": "attended"}),\
]
graph_s1.add_data(edges=edges_s1)
print(f"GraphRAG Answer: {graph_s1.query_multi_hop_path('F-150', 'Georgetown University')}")
```

**Output:**

```plaintext
Naive RAG Answer: I don't have enough information from the context.
GraphRAG Answer: Jim Farley attended Georgetown University.
```

### Pattern 2: The Causal Synthesis Failure

This is the failure to move from retrieval to synthesis. RAG lists facts but can't combine them to form a new conclusion.

- **Query:** "Is John safe to undergo surgery while on aspirin?"

- **Problem:** RAG will retrieve "John takes aspirin," "Aspirin is a blood thinner," and "Blood thinners increase surgery risk." But it will fail to synthesize these into a direct "No, it's not safe" answer.


#### Why the Naïve RAG Fails

The retriever searches for chunks that are semantically similar to the query: "John," "safe," "surgery," and "aspirin." In a real document base, it's highly likely to retrieve distracting, topically-related "noise" chunks.

In our example, the `top-k=3` chunks it retrieves might be:

1. "John is currently taking daily low-dose aspirin." (Relevant: "John," "aspirin")

2. "Pre-surgery safety checks are standard procedure..." (Relevant: "surgery safety")

3. "John is otherwise in good health and is cleared for the procedure..." (Relevant: "John," "safe," "procedure")


The key causal link ("Aspirin... is considered a blood thinner") is semantically less similar to the _full query_ and gets pushed out of the `top-k=3` context. The LLM is then given incomplete information. It sees "John takes aspirin" and "John is cleared," so it provides a weak, hedged answer and cannot make the correct logical leap.

#### Why the GraphRAG Succeeds

This approach doesn't use semantic search. It uses explicit logical rules (which could be backed by a causal graph). The `query_causal_chain` function is not searching for text – it's executing a pre-defined chain of logic:

1. _Fact:_ Does John take aspirin? Yes.

2. _Fact:_ Is aspirin a blood thinner? Yes.

3. _Fact:_ Is a blood thinner a risk for surgery? Yes.

4. _Conclusion:_ Therefore, John is not safe.


This deterministic, rule-based reasoning is immune to the "semantic noise" that distracts the naive RAG.

```python
# Naive RAG
docs_s2 = [\
    # --- The 3 "Answer" Chunks ---\
    Document(page_content="Aspirin reduces blood clotting and is considered a blood thinner."),\
    Document(page_content="Patients on blood thinners have increased bleeding risk during surgery."),\
    Document(page_content="John is currently taking daily low-dose aspirin."),\
\
    # --- The 3 "Noise" Chunks (to distract the retriever) ---\
    Document(page_content="John is otherwise in good health and is cleared for the procedure by his cardiologist."),\
    Document(page_content="Pre-surgery safety checks are standard procedure and usually focus on anesthesia allergies."),\
    Document(page_content="Aspirin is also commonly used to relieve minor aches and pains, but this is not why John takes it.")\
]
query_s2 = "Is John safe to undergo surgery while on aspirin?"
rag_chain_s2 = create_rag_chain (docs_s2)
print(f"Naive RAG Answer: {rag_chain_s2.invoke(query_s2)}")

# GraphRAG Pattern
facts_s2 = {
    "aspirin": {"is_a": "blood thinner"},
    "blood thinner": {"risk_for": "surgery"},
    "John": {"takes": "aspirin"},
}
print(f"GraphRAG Answer: {query_causal_chain(facts_s2)}")
```

**Output:**

```plaintext
Naive RAG Answer: Based on the context, John is currently taking daily low-dose aspirin...
GraphRAG Answer: John is NOT safe due to increased bleeding risk from aspirin, a blood thinner.
```

### Pattern 3: The Entity Ambiguity Trap

Vector search struggles with polysemy (words with multiple meanings). It relies on local semantic context, which can easily be confused.

- **Query:** "When did Apple release its first product?"

- **Problem:** The query "Apple" might retrieve documents for both Apple (company) and Apple (fruit), confusing the LLM.


#### Why the Naïve RAG Fails

The query "When did Apple release its first product?" is semantically ambiguous. The vector retriever, which looks for _semantic closeness_, will be strongly attracted to the "noise" chunks we added about the fruit.

The `top-k=3` chunks it retrieves will likely be:

1. "The 'Cosmic Crisp' is a new **apple product**... **first released**..." (Extremely high semantic similarity to "Apple releases its first product").

2. "The Granny Smith **apple**... is a popular **product**..."

3. "Many **apple** orchards **release** their new harvest..."


The _correct_ chunk ("The Apple I was introduced by Apple Inc...") is about a "company" and a specific "product" name. It might be semantically _less_ similar to the general query than the "Cosmic Crisp" chunk. The LLM is then handed a context exclusively about fruits and confidently (but incorrectly) answers about the "Cosmic Crisp" apple.

#### Why the GraphRAG Succeeds

The graph approach is immune to this ambiguity. The `query_disambiguated` function is _not_ just searching for "Apple." It is explicitly looking for a node that matches two criteria: `name='Apple'` AND `type='company'`.

This query structurally guarantees that it finds the `Apple Inc.` node and ignores the `apple (fruit)` node, regardless of semantic similarity. It then reliably retrieves the `first_product` attribute from the correct node.

```python
# Naive RAG
docs_s3 = [\
    # --- The "Answer" Chunks ---\
    Document(page_content="The Apple was introduced by Apple Inc. in 1976."),\
    Document(page_content="Apple Inc. is a technology company based in Cupertino."),\
\
    # --- "Noise" Chunks (to create ambiguity) ---\
    Document(page_content="The 'Cosmic Crisp' is a new apple product developed by Washington State University, first released to consumers in 2019."),\
    Document(page_content="Apples (the fruit) were first cultivated in Central Asia thousands of years ago."),\
    Document(page_content="The Granny Smith apple, first discovered in Australia, is a popular product for baking."),\
    Document(page_content="Many apple orchards release their new harvest in the fall.")\
]
query_s3 = "When did Apple release its first product?"
rag_chain_s3 = create_rag_chain(docs_s3)
print(f"Naive RAG Answer: {rag_chain_s3.invoke(query_s3)}")

# GraphRAG Pattern
graph_s3 = KnowledgeGraph()
nodes_s3 = [\
    ("Apple Inc.", {"type": "company", "first_product": "Apple I", "year": 1976}),\
    ("apple", {"type": "fruit", "origin": "Central Asia"}),\
]
graph_s3.add_data(nodes=nodes_s3)
print(f"GraphRAG Answer: {graph_s3.query_disambiguated('Apple', 'company', 'first_product')}")
```

**Output:**

```python
Naive RAG Answer: The 'Cosmic Crisp', a new apple product, was first released to consumers in 2019.
GraphRAG Answer: Apple Inc.'s first product was the Apple I in 1976.
```

### Pattern 4: The Contradictory Information Failure

RAG is blind to knowledge conflicts. If it retrieves two or more contradictory facts, it can't resolve them using metadata like dates or source credibility. It will hedge, merge them into a false statement, or present all of them.

- **Query:** "Who is the CEO of Twitter?"

- **Problem:** The retriever finds one chunk saying "Parag Agrawal (2022)" and another saying "Elon Musk (2023)". It may also find other related, confusing information. The LLM has no way to know which fact is the most current and authoritative.


#### Why the Naïve RAG Fails

The query "Who is the CEO of Twitter?" is semantically similar to _all_ documents containing the words "CEO" and "Twitter." In a real-world, evolving knowledge base, this is a recipe for disaster.

The `top-k=3` chunks our retriever finds will be a mess of contradictions:

1. "In 2023, Elon Musk became the CEO of Twitter." (Correct, but old)

2. "In 2022, Parag Agrawal was the CEO of Twitter." (Old)

3. "Linda Yaccarino is the current CEO of X (formerly Twitter)..." (Also correct, but a different person/role).


The LLM is handed three different, conflicting names for "CEO of Twitter" from different time periods. Because it is instructed to answer _only_ from the context and has no mechanism to identify which fact is the most recent, it cannot give a single, confident answer. It’s forced to list the conflicts it found.

#### Why the GraphRAG Succeeds

The knowledge graph is built for this. We've stored the "CEO" relationship as an **edge with metadata**, specifically a `year` attribute.

Our `query_with_conflict_resolution` function doesn't just find all CEO-related edges. It programmatically:

1. Finds all nodes connected to "Twitter" by a `ceo` label.

2. Extracts the `year` from each of those edges.

3. **Sorts the candidates by year** in descending order.

4. Returns only the top result.


This provides a deterministic, programmatic way to resolve conflicts and always provide the most current fact based on the explicit timestamps in our graph.

```python
# Naive RAG
docs_s4 = [\
    # --- The "Answer" Chunks (conflicting) ---\
    Document(page_content="In 2022, Parag Agrawal was the CEO of Twitter."),\
    Document(page_content="In 2023, Elon Musk became the CEO of Twitter."),\
\
    # --- "Noise" Chunks (to add more conflict/confusion) ---\
    Document(page_content="Linda Yaccarino is the current CEO of X (formerly Twitter), overseeing business operations."),\
    Document(page_content="Jack Dorsey, a co-founder and former CEO of Twitter, is now focused on his company Block."),\
    Document(page_content="CEOs of major tech companies, including Twitter's, have recently testified before Congress.")\
]
query_s4 = "Who is the CEO of Twitter?"
rag_chain_s4 = create_rag_chain(docs_s4)
print(f"Naive RAG Answer: {rag_chain_s4.invoke(query_s4)}")

#GraphRAG Pattern
graph_s4 = KnowledgeGraph()
edges_s4 = [\
    ("Twitter", "Parag Agrawal", {"label": "ceo", "year": 2022}),\
    ("Twitter", "Elon Musk", {"label": "ceo", "year": 2023}),\
]
graph_s4.add_data(edges=edges_s4)
print(f"GraphRAG Answer: {graph_s4.query_with_conflict_resolution('Twitter', 'ceo', 'year')}")
```

**Output:**

```python
Naive RAG Answer: According to the context, in 2022, Parag Agrawal was the CEO of Twitter. In 2023, Elon Musk became the CEO... Linda Yaccarino is the current CEO of X (formerly Twitter)...
GraphRAG Answer: Elon Musk (as of 2023)
```

### Pattern 5: The Implicit Relationship Hallucination

RAG relies on implicit semantic closeness, which can be dangerous. If "Tesla," "Toyota," and "Panasonic" all appear near the word "battery" in the vector space, the LLM might hallucinate a relationship that doesn't exist.

- **Query:** "Who did Tesla partner with on batteries?"

- **Problem:** The query is semantically "close" to any document mentioning "Tesla," "partner," and "batteries." The retriever will fetch chunks based on this closeness, even if they don't explicitly state a partnership, leading the LLM to infer one.


#### Why the Naïve RAG Fails

The vector retriever will look for chunks that "sound" like the query. In our expanded document list, it's highly likely to retrieve a confusing context for the LLM.

The `top-k=3` chunks it finds will likely be:

1. "Panasonic has a long-standing partnership to manufacture batteries..." (Relevant: "Panasonic," "partnership," "batteries")

2. "Tesla develops electric vehicles and relies on advanced battery tech..." (Relevant: "Tesla," "battery")

3. "Toyota also manufactures batteries and has discussed battery technology..." (Relevant: "Toyota," "manufactures batteries")


When the LLM receives this context, it has "Panasonic," "Tesla," and "Toyota" all in a "battery" context. The chunk for Panasonic doesn't explicitly link it to Tesla. The chunk for Toyota also mentions batteries. The LLM, forced to synthesize an answer, may _incorrectly_ infer a partnership that doesn't exist (like with Toyota) or state the facts without confirming the relationship.

#### Why the GraphRAG Succeeds

The knowledge graph isn’t vulnerable to this kind of "semantic bleed-over." It doesn’t care if nodes are "semantically near" each other.

Our `query_explicit_relation` function asks a very specific, structural question: "Start at the node **'Tesla'** and return _only_ the nodes connected to it by an edge with the _exact label_ **'partners\_with'**".

The graph then traverses its edges and finds only one: `("Tesla", "Panasonic", {"label": "partners_with"})`. It is structurally impossible for it to hallucinate a partnership with "Toyota" because no such `partners_with` edge exists for Tesla in the graph.

```python
# Naive RAG
docs_s5 = [\
    # --- The "Answer" Chunks (ambiguous) ---\
    Document(page_content="Tesla develops electric vehicles and relies on advanced battery tech."),\
    Document(page_content="Panasonic has a long-standing partnership to manufacture batteries for electric vehicles."),\
\
    # --- "Noise" Chunks (to create a false signal) ---\
    Document(page_content="Toyota also manufactures batteries and hybrid powertrains for its own vehicle lineup."),\
    Document(page_content="Tesla, Panasonic, and Toyota are all major players in the EV and battery supply chain."),\
    Document(page_content="A new partnership for solid-state batteries was announced, but it did not involve Tesla.")\
]
query_s5 = "Who did Tesla partner with on batteries?"
rag_chain_s5 = create_rag_chain(docs_s5)
print(f"Naive RAG Answer: {rag_chain_s5.invoke(query_s5)}")
#
# GraphRAG Pattern
graph_s5 = KnowledgeGraph()
edges_s5 = [\
    ("Tesla", "Panasonic", {"label": "partners_with"}),\
    ("Toyota", "Toyota", {"label": "partners_with"}),\
]
graph_s5.add_data(edges=edges_s5)
print(f"GraphRAG Answer: {graph_s5.query_explicit_relation('Tesla', 'partners_with')}")
```

**Output:**

```python
Naive RAG Answer: Based on the context, Panasonic has a partnership to manufacture batteries, and Tesla relies on advanced battery tech. Toyota also manufactures batteries.
GraphRAG Answer: Tesla partnered with Panasonic.
```

## Final Thoughts

Standard RAG is an essential tool, but its strength is **retrieval, not reasoning**. It falters when true synthesis is required.

You may find that a powerful LLM like Gemini can still correctly answer some of the simple scenarios in this article. The five patterns shown here are meant to build intuition. They demonstrate what _can_ and _does_ go wrong as your knowledge base grows larger and more complex.

The real failure of naive RAG emerges as you feed it more and more conflicting, ambiguous, or incomplete information. This "noisy" context forces the LLM to either hallucinate connections or fail to reason altogether.

By moving from a "bag of chunks" to a structured Knowledge Graph, you build a more reliable and intelligent system. You give your system a "global memory" of how facts explicitly connect, allowing it to answer complex questions by traversing a verified path rather than just guessing from a cloud of semantically similar text.

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

\useunder

\ul

SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering

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
|---|---|---|
| | G=(V,E)G=(V,E) | |

where the node set is:

| | | |
|---|---|---|
| | V=Vt∪Vc∪VsV=V\_{t}\\cup V\_{c}\\cup V\_{s} | |

Here, topic nodes VtV\_{t} represent document-level semantic summaries for cross-document bridging, core sentence nodes VcV\_{c} correspond to sentences carrying key facts and reasoning support, and supplementary sentence nodes VsV\_{s} represent subordinate sentences that elaborate on or conditionally supplement core sentences.

The edge set is formally defined as:

| | | |
|---|---|---|
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
|---|---|---|---|---|---|---|---|
| EM | F1 | EM | F1 | EM | F1 | Accuracy |
| BM25 | Retrieval Only | Passage | 3.00 | 9.20 | 15.20 | 3.40 | 9.65 | 1.40 | 4.27 | 37.20 |
| Retrieval Only | Sentence | 3.00 | 31.20 | 42.44 | 23.60 | 29.29 | 9.60 | 16.86 | 61.60 |
| RankLlama | Passage | 5.00 | 29.48 | 27.82 | 30.30 | 21.91 | 6.04 | 9.26 | 42.09 |
| SetR-CoT & IRI | Passage | 2.63 | 32.20 | 30.57 | \ul32.17 | 24.22 | 6.62 | 10.57 | 44.13 |
| KiRAG | Passage | 3.00 | 17.40 | 23.40 | 24.00 | \ul32.70 | 9.00 | 18.20 | 26.50 |
| KGP | Passage | 3.00 | \ul36.82 | \ul49.94 | 22.80 | 31.21 | 9.31 | 18.66 | \ul62.00 |
| LightRAG | Passage | 3.00 | 28.66 | 39.06 | 17.78 | 27.43 | \ul9.83 | \ul18.71 | 26.65 |
| SentGraph(Ours) | Sentence | 2.57 | 43.80 | 57.13 | 32.20 | 39.48 | 16.00 | 26.83 | 63.40 |
| BGE | Retrieval Only | Passage | 3.00 | 11.00 | 18.09 | 3.80 | 10.34 | 2.40 | 6.86 | 44.40 |
| Retrieval Only | Sentence | 3.00 | 38.60 | 50.88 | 30.80 | 40.01 | 17.00 | 28.57 | 60.20 |
| RankLlama | Passage | 5.00 | 31.88 | 32.95 | 32.24 | 25.78 | 7.61 | 11.77 | 43.51 |
| SetR-CoT & IRI | Passage | 2.91 | 36.62 | 38.11 | 35.44 | 30.35 | 10.79 | 15.43 | 47.14 |
| KiRAG | Passage | 3.00 | 18.20 | 24.50 | 26.40 | 35.00 | 6.20 | 17.00 | 22.50 |
| KGP | Passage | 3.00 | \ul44.00 | \ul58.73 | \ul36.80 | \ul48.20 | \ul21.20 | \ul34.72 | \ul63.40 |
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
|---|---|---|---|---|---|---|---|
| Retrieval | Model | RetrievalUnit | Avg\# Units | EM | F1 | EM | F1 | EM | F1 | Accuracy |
| \cellcolor[HTML]EFEFEFBase LLM: Qwen2.5-7B-Instruct |
| | RO | Passage | 3.00 | 14.20 | 19.24 | 16.00 | 18.00 | 2.20 | 4.42 | 35.20 |
| | KGP | Passage | 3.00 | \ul43.66 | \ul56.14 | \ul32.00 | \ul38.14 | \ul13.60 | \ul22.13 | \ul67.40 |
| | RO | Sentence | 3.00 | 37.60 | 49.18 | 26.80 | 32.02 | 11.60 | 19.97 | 67.00 |
| BM25 | SentGraph | Sentence | 2.89 | 48.80 | 61.98 | 44.40 | 52.53 | 25.00 | 35.09 | 68.80 |
| | RO | Passage | 3.00 | 13.60 | 18.26 | 10.00 | 10.94 | 3.20 | 4.60 | 39.40 |
| | KGP | Passage | 3.00 | \ul53.66 | \ul67.25 | \ul49.20 | \ul57.31 | \ul28.40 | \ul42.48 | \ul69.00 |
| | RO | Sentence | 3.00 | 43.80 | 56.52 | 40.80 | 49.71 | 22.40 | 34.53 | 66.00 |
| BGE | SentGraph | Sentence | 2.44 | 55.60 | 68.88 | 52.60 | 61.49 | 36.00 | 48.27 | 70.20 |
| \cellcolor[HTML]EFEFEFBase LLM: Llama-3.1-8B-Instruct |
| | RO | Passage | 3.00 | 9.20 | 15.20 | 3.40 | 9.65 | 1.40 | 4.27 | 37.20 |
| | KGP | Passage | 3.00 | \ul36.82 | \ul49.94 | 22.80 | \ul31.21 | 9.31 | \ul18.66 | \ul62.00 |
| | RO | Sentence | 3.00 | 31.20 | 42.44 | \ul23.60 | 29.29 | \ul9.60 | 16.86 | 61.60 |
| BM25 | SentGraph | Sentence | 2.57 | 43.80 | 57.13 | 32.20 | 39.48 | 16.00 | 26.83 | 63.40 |
| | RO | Passage | 3.00 | 11.00 | 18.09 | 3.80 | 10.34 | 2.40 | 6.86 | 44.40 |
| | KGP | Passage | 3.00 | \ul44.00 | \ul58.73 | \ul36.80 | \ul48.20 | \ul21.20 | \ul34.72 | \ul63.40 |
| | RO | Sentence | 3.00 | 38.60 | 50.88 | 30.80 | 40.01 | 17.00 | 28.57 | 60.20 |
| BGE | SentGraph | Sentence | 2.70 | 48.80 | 62.92 | 42.00 | 52.26 | 26.80 | 40.36 | 65.60 |
| \cellcolor[HTML]EFEFEFBase LLM: Qwen2.5-14B-Instruct |
| | RO | Passage | 3.00 | 14.00 | 18.91 | 16.20 | 18.26 | 2.20 | 2.42 | 35.60 |
| | KGP | Passage | 3.00 | \ul43.66 | \ul56.06 | \ul32.20 | \ul38.37 | 11.60 | 19.89 | 67.20 |
| | RO | Sentence | 3.00 | 37.20 | 48.94 | 27.00 | 32.08 | \ul13.20 | \ul22.10 | \ul66.80 |
| BM25 | SentGraph | Sentence | 2.89 | 49.00 | 62.36 | 43.80 | 51.84 | 24.00 | 33.93 | 69.20 |
| | RO | Passage | 3.00 | 13.60 | 18.25 | 10.00 | 10.88 | 3.00 | 4.51 | 39.20 |
| | KGP | Passage | 3.00 | \ul53.66 | \ul67.06 | \ul48.20 | \ul56.60 | \ul28.40 | \ul42.37 | \ul69.00 |
| | RO | Sentence | 3.00 | 43.00 | 56.14 | 40.80 | 49.60 | 22.60 | 34.90 | 66.20 |
| BGE | SentGraph | Sentence | 2.61 | 55.40 | 68.74 | 54.20 | 63.05 | 36.80 | 49.30 | 70.00 |
| \cellcolor[HTML]EFEFEFBase LLM: Qwen2.5-32B-Instruct |
| | RO | Passage | 3.00 | 20.80 | 27.78 | 24.00 | 26.88 | 3.40 | 7.75 | 44.80 |
| | KGP | Passage | 3.00 | \ul46.08 | \ul58.29 | \ul34.40 | \ul40.20 | \ul14.60 | \ul25.25 | 66.40 |
| | RO | Sentence | 3.00 | 40.60 | 51.70 | 31.80 | 37.22 | 12.40 | 21.27 | \ul67.20 |
| BM25 | SentGraph | Sentence | 2.54 | 51.40 | 64.03 | 45.80 | 53.69 | 25.20 | 36.78 | 72.40 |
| | RO | Passage | 3.00 | 21.00 | 28.52 | 23.40 | 26.24 | 5.00 | 9.16 | 51.20 |
| | KGP | Passage | 3.00 | \ul55.28 | \ul68.89 | \ul51.80 | \ul60.53 | \ul28.20 | \ul41.41 | 67.80 |
| | RO | Sentence | 3.00 | 43.20 | 57.01 | 45.00 | 52.76 | 25.00 | 36.89 | \ul68.80 |
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
|---|---|---|---|
| AS | AER | GPE | EM | F1 | EM | F1 | EM | F1 |
|---|---|---|---|---|---|---|---|---|
| \checkmark | \times | \times | 37.60 | 50.62 | 28.00 | 35.52 | 16.00 | 27.67 |
| \checkmark | \checkmark | \times | 44.80 | 59.37 | 37.40 | 46.96 | 25.40 | 37.57 |
| \checkmark | \checkmark | \checkmark | 48.80 | 62.92 | 42.00 | 52.26 | 26.80 | 40.36 |

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

<research_source type="scraped_from_research" phase="exploitation" file="vector-embeddings-in-rag-applications-ml-articles-weights-bi.md">
<details>
<summary>Vector Embeddings in RAG Applications</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5>

# Vector Embeddings in RAG Applications

A guide on using vector embeddings to enhance Retrieval-Augmented Generation (RAG) systems.

[Mostafa Ibrahim](https://wandb.ai/profile/mostafaibrahim17)

Created on May 17, 2024|Updated on March 1, 2025

This article explores one of the crucial factors that contributed to making [Retrieval-Augmented Generation (RAG) systems](https://wandb.ai/site/articles/what-is-retrieval-augmented-generation/): [vector embeddings](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5). These elements artechnical and transformational tools that enable RAG systems to process languages in very subtle ways, akin to some aspects of human understanding.

Vector embeddings provide a way to convert textual information into numerical data. This is instrumental, as it allows the system to quickly search and retrieve the most important information to generate responses. Such a capability is crucial in improving the accuracy and contextual relevance of an LLM output.

This article details the process of integrating vector embeddings into RAG systems and enhancing performance. We will discuss the mechanics behind this integration and its implications for AI applications.

#### What we'll cover:

[What are vector embeddings?](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#what-are-vector-embeddings?) [Text embeddings](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#text-embeddings) [Image embeddings](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#image-embeddings) [Audio embeddings](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#audio-embeddings) [How do text embedding work?](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#how-do-text-embedding-work?) [Vector embeddings in RAG systems](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#vector-embeddings-in-rag-systems) [Concept of Embedding Data into a Vector Database for Easy Retrieval](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#concept-of-embedding-data-into-a-vector-database-for-easy-retrieval) [RAG system explained in three steps](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#rag-system-explained-in-three-steps) [1) Searching for relevant data](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#1)-searching-for-relevant-data) [2) Sending relevant data to the LLM](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#2)-sending-relevant-data-to-the-llm) [3) The LLM answering using the sent data](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#3)-the-llm-answering-using-the-sent-data) [Using W&B Weave](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#using-w&b-weave-) [Practical Application: Building a RAG System for Financial Forecasting](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#practical-application:-building-a-rag-system-for-financial-forecasting) [Conclusion](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Vector-Embeddings-in-RAG-Applications--Vmlldzo3OTk1NDA5#conclusion)

## What are vector embeddings?

Vector embeddings are a powerful technique used in machine learning and artificial intelligence to transform raw data into a numerical format that models can easily process.

This transformation involves representing data as vectors in a high-dimensional space where similar items are placed closer together, enabling efficient computations and similarity comparisons. Vector embeddings come in many shapes and forms, such as.

### Text embeddings

Text embedding convert text into a set of vectors where each vector represents a word or a sentence. Techniques like [Word2Vec](https://wandb.ai/authors/embeddings/reports/Word2Vec-Teaching-Neural-Networks-to-Understand-Words--VmlldzozMzIxNjQ), [GloVe](https://wandb.ai/authors/embeddings-2/reports/An-Introduction-to-the-Global-Vectors-GloVe-Algorithm--VmlldzozNDg2NTQ), and [BERT](https://wandb.ai/mukilan/BERT_Sentiment_Analysis/reports/An-Introduction-to-BERT-And-How-To-Use-It--VmlldzoyNTIyOTA1) are commonly used for this purpose.

These models work by learning representations for words based on their contexts in large text corpora. For instance, words that appear in similar contexts, like "king" and "queen," will have close vector representations. More on this in the common section, below.

### Image embeddings

Another data type is images. Similar to text embeddings, image embedding involves converting images into a vector of numbers. Such embeddings require a different type of embedders, in this case, [Convolutional Neural Networks (CNNs)](https://wandb.ai/wandb_fc/wb-tutorials/reports/Tutorial-Convolutional-Neural-Networks--Vmlldzo0NTIwNzY5) are typically used to generate these embeddings.

An image is passed through various layers of the CNN, which extract features at different levels of abstraction. The output is a dense vector that encapsulates the visual features of the image, useful for tasks like image recognition, classification, and retrieval.

### Audio embeddings

Lastly, audio data can also be converted into vector embeddings. Techniques like Mel Frequency Cepstral Coefficients (MFCCs) or deep learning models such as WaveNet and DeepSpeech are used to extract features from raw audio.

These features are then used to create a vector that represents the audio, which can be utilized for applications like [speech recognition](https://wandb.ai/wandb_fc/wb-tutorials/reports/Tutorial-Speech-Recognition--Vmlldzo0NTM5OTEx), music analysis, and audio classification.

https://api.wandb.ai/files/mostafaibrahim17/images/projects/37042936/33f6bc3e.png

Image By Author

In this article, we will be focusing mainly of text embedding, as this is the most common embedding format and the one that works best with large language models.

## How do text embedding work?

Text embeddings represent words in a numerical format that captures semantic relationships and characteristics shared among them. Here’s how the process works, in context to the following example which includes the words "King," "Queen," "Boy," and "Girl".

When thinking about vectorization, imagine a multidimensional space where each dimension can represent a feature like age, gender, royalty, etc. In such a space:

"King" might be represented as a point at coordinates (male, high royalty).

"Queen" as (female, high royalty).

"Boy" as (male, low royalty).

"Girl" as (female, low royalty).

In the below example, we consider two features among others: gender and royalty.

https://api.wandb.ai/files/mostafaibrahim17/images/projects/37042936/72457650.png

Image By Author

Gender Feature: In the embedding space, "King" and "Boy" would be positioned closer to each other on the gender dimension, reflecting their common male attribute. Similarly, "Queen" and "Girl" would cluster together on this dimension due to their female attribute.

Royalty Feature: "King" and "Queen" would be close to each other on a royalty dimension, reflecting their high-status roles in royalty. In contrast, "Boy" and "Girl" would likely be positioned farther from "King" and "Queen" on this dimension due to their general status as non-royal.

These embeddings can then be used in various applications like:

Similarity Measurement: Calculating distances between words to find how similar they are (e.g., "King" is closer to "Queen" than "King" is to "Boy").

Analogies: Solving problems like "King is to Queen as Boy is to what?" The model would find "Girl" as the closest word vector.

Machine Translation and NLP Tasks: Using these vectors to understand text in tasks like sentiment analysis, classification, and more.

The effectiveness of embeddings in capturing such nuanced relationships makes them extremely valuable in natural language processing, allowing machines to process text in a more human-like and intuitive manner. Models like [Word2Vec](https://wandb.ai/authors/embeddings/reports/Word2Vec-Teaching-Neural-Networks-to-Understand-Words--VmlldzozMzIxNjQ), [GloVe](https://wandb.ai/authors/embeddings-2/reports/An-Introduction-to-the-Global-Vectors-GloVe-Algorithm--VmlldzozNDg2NTQ), and more recently, [BERT](https://wandb.ai/mukilan/BERT_Sentiment_Analysis/reports/An-Introduction-to-BERT-And-How-To-Use-It--VmlldzoyNTIyOTA1) and [GPT](https://wandb.ai/fully-connected/blog/gpt), use these principles to create powerful embeddings.

## Vector embeddings in RAG systems

A Retrieval-Augmented Generation (RAG) system is an advanced NLP architecture that enhances the capabilities of language models by combining them with retrieval-based information. This system significantly improves the accuracy and relevance of the responses generated by the language model, especially in complex domains where specific knowledge is required.

### Concept of Embedding Data into a Vector Database for Easy Retrieval

Before a RAG system can retrieve relevant data, the information must be structured in a way that makes it easily accessible and comparable. This involves:

Data Vectorization: All the data—whether it's text, images, or any other form—needs to be transformed into vectors. This means each item in the database is converted into a high-dimensional numerical vector that represents various features of the data.

Vector Database Creation and Storage: These vectors are then stored in a vector database, often using systems like FAISS (Facebook AI Similarity Search). These systems allow for efficient retrieval of vectors that are close to a given query vector in the high-dimensional space, which corresponds to retrieving data that is similar or relevant to a query.

## RAG system explained in three steps

https://api.wandb.ai/files/mostafaibrahim17/images/projects/37042936/62be9dcc.png

Image By Author

### 1) Searching for relevant data

Query Vectorization: When a query is received, it is first converted into a vector using the same model or method used for creating the database vectors.

Retrieval: The query vector is then used to search the vector database for similar vectors. The corresponding data for these vectors (which could be text passages, images, etc.) are deemed to be the most relevant to the query.

### 2) Sending relevant data to the LLM

Data Preparation: The retrieved data is often preprocessed or formatted in a way that can be easily used by the language model. This might involve summarizing the information or converting it into a structured format that the model can understand.

Integration: The processed, relevant data is then fed into a [large language model (LLM)](https://wandb.ai/fully-connected/blog/llm) as additional context or as part of the input. This step is crucial because it provides the LLM with specific information that directly relates to the user's query.

### 3) The LLM answering using the sent data

Response Generation: With the context provided by the retrieved data, the LLM generates a response. The model leverages both the general knowledge it has learned during pre-training and the specific information provided by the retrieved data.

Refinement and Output: The generated response is sometimes refined or adjusted to ensure coherency and relevance. The final output is then presented as the answer to the initial query.

#### Benefits of RAG Systems

The integration of retrieval systems with generative models in a RAG setup allows for responses that are not only contextually accurate but also deeply informed by specific data, making them particularly useful in specialized fields such as medical, legal, or technical domains where precise information is crucial.

This multi-step approach leverages the strengths of both retrieval systems and generative AI, bridging the gap between vast data resources and sophisticated linguistic capabilities, resulting in outputs that are both rich in content and highly relevant to the queries posed.

## Using W&B Weave

[Weave](https://wandb.ai/site/weave) is a powerful tool from Weights & Biases designed to simplify the monitoring of machine learning models during production. It provides an easy-to-use interface for tracking various metrics, visualizing data, and examining model performance in real time. By integrating Weave into our RAG system, we enhance our ability to monitor our model’s performance during production.

To use Weave, start by initializing it with weave.init('your\_project\_name'). Next, add the @weave.op() decorator to any function you wish to track. This decorator automatically logs all inputs and outputs of the function, capturing detailed information about its operation. Users can then examine this data within the Weave interface for easy inspection of function calls. We will use Weave for this project to track inputs and outputs to our model!

### Practical Application: Building a RAG System for Financial Forecasting

In the below code, we will build our own RAG system. This RAG system would include an [OpenAI](https://wandb.ai/fully-connected/blog/openai) LLM, the [Housing Datase](https://www.kaggle.com/datasets/justinas/housing-in-london) t from which we got our data, and a vector database, and FAISS which is the vector database that we used to store our vectorized data.

https://api.wandb.ai/files/mostafaibrahim17/images/projects/37042936/46fd0fba.png

#### Step 1: Installing the necessary libraries

```
!pip install langchain langchain-community tiktoken faiss-cpu transformers pandas torch openai
```

#### Step 2: Importing the necessary libraries

These libraries will include LLMChain which allows us to build our answer chain, FAISS which is where we will store our vectorized data, and OpenAIEmbeddings as the data embedder of choice.

```
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import Document
import os
import weave
```

#### Step 3: Integrating W&B Weave into our code

We will start by initializing a new Weave project.

```
weave.init('RAG_System')
```

#### Step 4: Loading and processing our dataset

Load the dataset from a local CSV file. You can always utilize any data set of choice, but make sure to properly process the dataset before usage.

```
df = pd.read_csv("/kaggle/input/housing-in-london/housing_in_london_monthly_variables.csv")
```

We will sample 10% of our dataset.

```
df = df.sample(frac=0.1, random_state=42)
```

Here we will be combining our fields into a text field for easier processing.

```
df['text'] = df.apply(lambda row: f"Date: {row['date']}, Area: {row['area']}, "
                                  f"Average Price: {row['average_price']}, "
                                  f"Code: {row['code']}, Houses Sold: {row['houses_sold']}, "
                                  f"Number of Crimes: {row['no_of_crimes']}, "
                                  f"Borough Flag: {row['borough_flag']}", axis=1)
```

Prepare the text for the knowledge base

```
texts = df['text'].tolist()
```

#### Step 5: Creating and storing our embeddings

Create embeddings for the texts.

```
embeddings = OpenAIEmbeddings(api_key=api_key)
vectors = embeddings.embed_documents(texts)
```

Create a FAISS vector store and store our embedding in it. I also added logic to cache our vector store to avoid generating new embeddings on every run:

```
# Check if the vector store already exists
vector_store_path = "faiss_index"
if os.path.exists(vector_store_path):
    # Load the existing vector store
    vector_store = FAISS.load_local(vector_store_path, embeddings, allow_dangerous_deserialization=True)
else:
    # Create and save the vector store
    vectors = embeddings.embed_documents(texts)
    vector_store = FAISS.from_texts(texts, embeddings)
    vector_store.save_local(vector_store_path)
```

#### Step 6: Retrieving our data

Define the retriever function. In this case, we will be defining our K value to 20. This will retrieve 20 data points from the vector database for each query given.

```
def retrieve(query, k=20):
    return vector_store.similarity_search(query, k=k)
```

Create a prompt template for generating responses.

```
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""Given the following data from the London housing dataset:
{context}
Please use the provided data to answer the question accurately. Calculate any necessary averages or totals directly from the data provided.
Question: {question}"""
)
```

#### Step 7: Testing and evaluating our model

Initialize the OpenAI LLM, and insert your OpenAI key below.

```
llm = OpenAI(api_key=api_key)
```

Here we will be creating an LLM chain.

```
llm_chain = LLMChain(prompt=prompt_template, llm=llm)
```

We will define a custom function to generate a response using retrieval and LLM chain. Here we leverage W&B Weave so that we can automatically log inputs and outputs to our generate\_response function, which allows us to easily monitor how are model is performing in production!

```
@weave.op()
def generate_response(question):
    # Retrieve relevant documents
    retrieved_docs = retrieve(question)
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    # Print the retrieved documents for debugging
    print(f"Retrieved documents for question '{question}':")
    for i, doc in enumerate(retrieved_docs):
        print(f"Document {i+1}:\n{doc.page_content}\n")

    # Generate response using LLM chain
    response = llm_chain.run(context=context, question=question)

    return {"response": response, "context": context}
```

Here are sample questions that we will use to test our model.

```
questions = [\
    "Using the data retrieved, what was the average price of houses in Westminster in 2019?",\
    "Using the data retrieved, how many crimes were reported in Hackney in 2018?",\
    "Using the data retrieved, what is the average price trend in London over the years?",\
]
```

Get answers to the example questions.

```
for question in questions:
    answer = generate_response(question)
    print(f"Q: {question}\nA: {answer}\n")
```

#### Weave Logging

Below are the results of our model. Since we added Weave to our generate\_response function, we automatically log our question, context, and response.

Inside Weave, you will see multiple cells for each call of the function, as shown below:

https://api.wandb.ai/files/byyoung3/images/projects/39510019/2b3a09aa.png

We can click into any of the cells, and examine more details about the inputs and outputs to the function:

https://api.wandb.ai/files/byyoung3/images/projects/39510019/052bbcbe.png

Overall, Weave is a super easy tool to use for logging data in a RAG system, as it requires simply initialization of Weave, followed by adding the @weave.op() decorator.

For instance, you may want to train new models on previous production data, or perhaps you would just like a quick and easy way to monitor how your models are performing. As seen above, the context is information retrieved by our embedding search, and the response is generated by our LLM which uses the retrieved context!

### Conclusion

By converting various forms of data into high-dimensional vectors, embeddings allow RAG systems to efficiently retrieve and utilize relevant information, significantly improving the accuracy and contextual relevance of generated responses.

In this article, we explored the mechanics of text embeddings, understanding how they capture semantic relationships and facilitate nuanced language processing. Further, we demonstrated a practical application of building a RAG system, showcasing the steps involved in integrating vector embeddings and leveraging their capabilities.

Hopefully it's clear that vector embeddings are pivotal in advancing the performance of RAG systems, bridging the gap between vast data resources and sophisticated linguistic capabilities to deliver highly informed and relevant outputs.

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