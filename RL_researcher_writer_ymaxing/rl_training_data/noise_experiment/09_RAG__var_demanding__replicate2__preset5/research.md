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
<summary>What attention dilution mechanisms explain lost-in-the-middle in long RAG contexts?</summary>

Phase: [EXPLORATION]

### Source [61]: https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf

Query: What attention dilution mechanisms explain lost-in-the-middle in long RAG contexts?

Answer: Attention dilution: more tokens = harder to focus on the right span. Positional encoding limits: extrapolation beyond training length is fragile. Boundary effects: starts/ends get disproportionate attention. Cognitive analogy: primacy/recency effects in memory. The paper discusses empirical trends rather than mechanistic proofs, but these factors are consistent with prior understanding: attention budgets dilute with length, and many position encoding schemes struggle when extrapolating. Start/end tokens also benefit from structural prominence during generation.

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://diffray.ai/blog/context-dilution/

Query: What attention dilution mechanisms explain lost-in-the-middle in long RAG contexts?

Answer: Follow-up research published in ACL Findings 2024, "Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization", pinpointed the root cause: an intrinsic U-shaped attention bias where LLMs assign higher attention weights to beginning and end tokens regardless of their semantic relevance. The paper demonstrated that LLMs can attend to relevant middle content but are systematically distracted by positional bias. The seminal 2023 paper "Lost in the Middle: How Language Models Use Long Contexts" by researchers at Stanford and Meta AI established the foundational understanding of context dilution. Testing models including GPT-3.5-Turbo, Claude-1.3, and LongChat on multi-document QA tasks, the researchers discovered a striking U-shaped performance curve: LLMs perform best when relevant information appears at the beginning or end of the context, but accuracy plummets when critical details are buried in the middle.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://arxiv.org/html/2503.10720v1

Query: What attention dilution mechanisms explain lost-in-the-middle in long RAG contexts?

Answer: The long nature of RAG contexts exacerbates attention dilution (Hsieh et al., 2024; Zhu et al., 2024). When the context is excessively long, the attention scores are spread thin, causing the model to allocate less focus to any single token. This dilution of attention reduces the ability of the model to concentrate on the most relevant parts of the retrieved context.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf

Query: What attention dilution mechanisms explain lost-in-the-middle in long RAG contexts?

Answer: The U-shaped curve we observe in this work has a connection in psychology known as the serial-position effect (Ebbinghaus, 1913; Murdock Jr, 1962), that states that in free-association recall of elements from a list, humans tend to best remember the first and last elements of the list. The serial-position effect plays a role in understanding how humans develop short- and long-term memory. Observing a serial-position-like effect in language models is perhaps surprising, since the self-attention mechanisms underlying Transformer language models is technically equally capable of retrieving any token from their contexts. Both primacy and recency bias.

-----

</details>

<details>
<summary>How do bitemporal metadata schemas mitigate version conflicts in dynamic RAG knowledge bases?</summary>

Phase: [EXPLORATION]

### Source [65]: https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/

Query: How do bitemporal metadata schemas mitigate version conflicts in dynamic RAG knowledge bases?

Answer: Graphiti offers incremental, real-time updates through its temporally aware knowledge graph. This design means engineers no longer need to recompute entire graphs when data changes. Instead, Graphiti incrementally integrates updates, resolves conflicts based on temporal metadata, and maintains an accurate historical state. A key feature is Graphiti’s bi-temporal model, which tracks when an event occurred and when it was ingested. Every graph edge (or relationship) includes explicit validity intervals (t_valid, t_invalid). Graphiti uses semantic, keyword, and graph search to determine whether new knowledge conflicts with existing knowledge. When conflicts arise, Graphiti intelligently uses the temporal metadata to update or invalidate, but not discard, outdated information, preserving historical accuracy without large-scale recomputation. This temporal model enables powerful historical queries, allowing users to reconstruct states of knowledge at precise moments or analyze how data evolves over time. Graphiti helps overcome static RAG’s limitations with dynamic data. It’s a real-time, temporally-aware knowledge graph engine that incrementally processes incoming data, instantly updating entities, relationships, and communities without batch recomputation. Graphiti isn’t just another retrieval tool—it’s an ever-present source of context for agents, continuously available and updated.

-----

-----

Phase: [EXPLORATION]

### Source [67]: https://aws.amazon.com/blogs/machine-learning/dynamic-metadata-filtering-for-amazon-bedrock-knowledge-bases-with-langchain/

Query: How do bitemporal metadata schemas mitigate version conflicts in dynamic RAG knowledge bases?

Answer: Enabling dynamic filtering through Knowledge Base’s metadata filtering enhances document retrieval in RAG systems by tailoring outputs to user-specific needs, significantly improving the relevance and accuracy of LLM-generated responses. Amazon Bedrock Knowledge Bases offers a fully managed Retrieval Augmented Generation (RAG) feature that connects large language models (LLMs) to internal data sources. It’s a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://codesignal.com/learn/courses/scaling-up-rag-with-vector-databases/lessons/metadata-based-filtering-in-rag-systems

Query: How do bitemporal metadata schemas mitigate version conflicts in dynamic RAG knowledge bases?

Answer: Metadata includes any labeled information that describes your text chunks. Common examples are category, date, or title. When you have a large collection of documents, a normal text-based similarity search might return results you don't actually want. But by selectively filtering on metadata, you can drastically reduce irrelevant results and ensure only the most pertinent information is retrieved. In a large enterprise knowledge base spanning different departments (e.g., Human Resources, Technology, Finance), applying a simple metadata filter on the category field ensures that your search never strays into unrelated content. This becomes particularly useful when you have specialized queries that are domain-specific and need accurate, fast retrieval.

-----

</details>

<details>
<summary>What optimization tradeoffs arise balancing GraphRAG summarization depth against computational costs?</summary>

Phase: [EXPLORATION]

### Source [69]: https://www.lettria.com/blogpost/10-rules-for-optimizing-your-graphrag-strategies

Query: What optimization tradeoffs arise balancing GraphRAG summarization depth against computational costs?

Answer: Knowledge graphs can grow complex, but generative models often have input limitations (e.g., token limits). Balance the depth and breadth of your graph data with what the model can process effectively. Actionable Tip: Use summarization or chunking techniques to distill key information while preserving context.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://arxiv.org/html/2503.02922v1

Query: What optimization tradeoffs arise balancing GraphRAG summarization depth against computational costs?

Answer: The performance from GraphRAG on this benchmark is achieved by generating community summaries at a Leiden hierarchy level of 4 and indexing the Kevin Scott corpus at a granularity of 600 tokens. The 600-token granularity reflects how the full corpus is chunked as input into GraphRAG, influencing both the retrieval granularity and the summarization depth. This chunking strategy allows GraphRAG to capture broader thematic connections. In terms of indexing cost, both RAPTOR and TREX demonstrate savings over GraphRAG as shown in Table 1. Querying costs are also lower for RAPTOR and TREX, as indicated in Table 2, suggesting that these methods are better suited for OLTP-style benchmarks. Closer analysis reveals that some of the degradation in performance for GraphRAG in the single-document scenario is due to the hallucinations that occasionally arise.

-----

-----

Phase: [EXPLORATION]

### Source [71]: https://falkordb.com/blog/what-is-graphrag/

Query: What optimization tradeoffs arise balancing GraphRAG summarization depth against computational costs?

Answer: Successful GraphRAG implementation hinges on data quality, computational resources, expertise, and cost-benefit analysis. Vector stores can be expensive, especially for large-scale datasets. Knowledge graphs can often be far more efficient.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://gemslab.github.io/papers/liu-2018-graph-summarization.pdf

Query: What optimization tradeoffs arise balancing GraphRAG summarization depth against computational costs?

Answer: Summarization involves extracting of important or interesting information. However, the definition of “interesting” is itself subjective, usually requiring both domain knowledge and user preferences. Moreover, the cutoff between “interesting” and “uninteresting” can be difficult to determine in a principled way; usually, it is decided by considering the tradeoffs among time, space, and information preserved in the summary, as well as the complexity of mapping solutions obtained from the summary back onto the original nodes and edges. Each presented graph summarization technique uses different optimization formulations to define the interestingness of a summary.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://www.techment.com/blogs/rag-optimization-techniques-production-ai/

Query: What optimization tradeoffs arise balancing GraphRAG summarization depth against computational costs?

Answer: The challenge in production environments is balancing context richness with token limitations. Too little context results in hallucinations. Too much context increases latency and cost. Graph RAG incorporates knowledge graphs into the retrieval process. Instead of retrieving isolated documents, it retrieves connected subgraphs of knowledge. Graph-based indexing: Documents are converted into graph structures where nodes represent entities or concepts and edges represent relationships. Graph-guided retrieval: Queries retrieve relevant nodes and expand across connected relationships.

-----

</details>

<details>
<summary>How do iterative self-critique loops in agentic RAG reduce hallucination rates?</summary>

Phase: [EXPLORATION]

### Source [74]: https://www.linkedin.com/posts/stevenouri_self-rag-and-agentic-rag-still-deliver-the-activity-7356330443182411776-Pqxb

Query: How do iterative self-critique loops in agentic RAG reduce hallucination rates?

Answer: Self-RAG introduces self-awareness by grading its own outputs. If retrieved data isn’t good enough, it rewrites the query and tries again before generating a response. This iterative loop leads to sharper answers, better precision, reduces irrelevant answers, and reduces hallucinations. Agentic RAG features dynamic reasoning loops and tool orchestration that reduce hallucinations and improve complex decision-making.

-----

-----

Phase: [EXPLORATION]

### Source [75]: https://www.kore.ai/blog/what-is-agentic-rag

Query: How do iterative self-critique loops in agentic RAG reduce hallucination rates?

Answer: Agentic RAG introduces iterative refinement and adaptive retrieval. Retrieval is an iterative and adaptive process where the system evaluates if retrieved information meets requirements and adjusts strategy. This includes dynamic query rewriting, multi-hop retrieval, cross-source retrieval, confidence scoring and filtering. Iterative retrieval and validation loops reduce hallucination risk. The agent decides what to retrieve, how to refine it, when to re-query, resulting in more accurate, reliable outcomes.

-----

-----

Phase: [EXPLORATION]

### Source [76]: https://wandb.ai/wandb_fc/genai-research/reports/Agentic-RAG-Revolutionizing-AI-with-autonomous-retrieval--VmlldzoxNDIzMjA0MQ

Query: How do iterative self-critique loops in agentic RAG reduce hallucination rates?

Answer: Reflection pattern in Agentic RAG enables an agent to critique and refine its own outputs iteratively. By incorporating self-feedback, the agent identifies errors or omissions and loops back to retrieve more info or adjust response. This might involve double-checking against sources or one agent reviewing another. Iterative self-improvement leads to more accurate and well-rounded results, reducing hallucinations.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://aws.amazon.com/blogs/machine-learning/reducing-hallucinations-in-large-language-models-with-custom-intervention-using-amazon-bedrock-agents/

Query: How do iterative self-critique loops in agentic RAG reduce hallucination rates?

Answer: Agentic workflows decompose tasks into steps with iterative feedback loops and self-reflection to produce results. Combined with RAG, which reduces hallucinations, agentic workflow measures, detects, and mitigates hallucinations using custom hallucination detector with evaluation metrics. If detected, it notifies humans-in-the-loop.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://arxiv.org/html/2501.09136v2

Query: How do iterative self-critique loops in agentic RAG reduce hallucination rates?

Answer: Iterative Correction in Corrective RAG dynamically identifies and corrects irrelevant retrievals, minimizing hallucination risk by validating content. Reflection is a foundational pattern enabling agents to iteratively evaluate and refine outputs via self-feedback, identifying errors and incorporating feedback. Self-critique guides iterative reasoning. Adaptive Agentic RAG uses planning with reflection and self-critique for complex tasks.

-----

</details>

<details>
<summary>How has RAG evolved from early library information retrieval?</summary>

Phase: [EXPLORATION]

### Source [79]: https://www.linkedin.com/posts/greg-coquillo_people-think-rag-is-just-retrieve-generate-activity-7422655000109309952-TpbW

Query: How has RAG evolved from early library information retrieval?

Answer: People think RAG is just “retrieve → generate.” That version is already outdated. As models get stronger, the real bottleneck isn’t generation. It’s how, when, and why you retrieve. That’s why RAG is evolving fast. Here are 12 advanced RAG patterns that show where things are heading and what problems teams are actually solving now: 1. Mindscape-Aware RAG Builds a global view first, then retrieves with intent. Useful when long context matters more than isolated chunks. 2. Hypergraph Memory RAG Stores facts as connected graphs so multi-hop reasoning works across retrieval steps. 3. QUCO-RAG Triggers retrieval based on suspicious or rare entities, reducing confident hallucinations. 4. HiFi-RAG Uses cheap models to filter early and strong models later, cutting cost without losing quality. 5. [...] The infographic shows why “one RAG to rule them all” no longer works. This infographic does a great job showing how RAG has evolved far beyond basic retrieval. The hypergraph memory RAG flow is explained in a very intuitive way. The distinction between memory-based and graph-based RAG is very clearly presented.

-----

-----

Phase: [EXPLORATION]

### Source [80]: https://en.wikipedia.org/wiki/Retrieval-augmented_generation

Query: How has RAG evolved from early library information retrieval?

Answer: Retrieval-augmented generation (RAG) is a technique that enables large language models (LLMs) to retrieve and incorporate new information from external data sources. With RAG, LLMs first refer to a specified set of documents, then respond to user queries. These documents supplement information from the LLM's pre-existing training data. This allows LLMs to use domain-specific and/or updated information that is not available in the training data. Other retrieval techniques focus on improving accuracy by refining how documents are selected. Some retrieval methods combine sparse representations, such as SPLADE, with query expansion strategies to improve search accuracy and recall. RAG improves large language models (LLMs) by incorporating information retrieval before generating responses. Unlike LLMs that rely on static training data, RAG pulls relevant text from databases, uploaded documents, or web sources. RAG is a way of improving LLM performance, in essence by blending the LLM process with a web search or other document look-up process to help LLMs stick to the facts. This method helps reduce AI hallucinations.

-----

-----

Phase: [EXPLORATION]

### Source [81]: https://ragflow.io/blog/the-rise-and-evolution-of-rag-in-2024-a-year-in-review

Query: How has RAG evolved from early library information retrieval?

Answer: The Rise of GraphRAG. Microsoft's mid-year open-sourcing of GraphRAG was a groundbreaking event. As a library rather than an end-to-end solution, GraphRAG's rapid rise in popularity underscores its ability to tackle key issues with Retrieval-Augmented Generation (RAG), particularly the semantic gap. This issue has long been a challenge for search system developers, as queries and answers often fail to align perfectly. When search systems evolved into RAG models, this problem was amplified: while traditional search queries are defined by a few keywords, RAG queries are user questions. The shift from keywords to questions makes user intent even harder to discern, thereby exacerbating this semantic gap. GraphRAG is one design aimed at bridging this gap. Tensor-based reranking originated from early works such as ColBERT and its improved version, ColBERT v2, in 2020. However, it only gained significant attention in the industry in early 2024.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://scholarlykitchen.sspnet.org/2025/05/08/guest-post-eight-hypotheses-why-librarians-dont-like-retrieval-augmented-generation-rag/

Query: How has RAG evolved from early library information retrieval?

Answer: RAG was developed by researchers of the Facebook AI Research team and other scientists. Discovery layers were inspired by web search and first sold to us by library vendors, although the community quickly came around and developed great open-source solutions like VuFind and K10plus-Zentral. In came tools from outside library-land such as perplexity.ai, Elicit and many others that threaten to yet again make library search interfaces less relevant for our users. The answer to making search more attractive in 2025 seems to lie in combining information retrieval algorithms with a large language model (LLM) and an outside database. This approach promises fewer hallucinations than querying a non-RAG-chatbot.

-----

-----

Phase: [EXPLORATION]

### Source [83]: https://aws.amazon.com/what-is/retrieval-augmented-generation/

Query: How has RAG evolved from early library information retrieval?

Answer: Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response. Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. Without RAG, the LLM takes the user input and creates a response based on information it was trained on—or what it already knows. With RAG, an information retrieval component is introduced that utilizes the user input to first pull information from a new data source. The user query and the relevant information are both given to the LLM. The LLM uses the new knowledge and its training data to create better responses.

-----

</details>

<details>
<summary>What legal tech RAG lessons apply to medical diagnosis systems?</summary>

Phase: [EXPLORATION]

### Source [84]: https://thescimus.com/blog/retrieval-augmented-generation-healthcare-guide/

Query: What legal tech RAG lessons apply to medical diagnosis systems?

Answer: Even with technical and user adoption challenges addressed, there are still ethical and legal complexities to navigate. For starters, compliance with HIPAA is non-negotiable. Organizations must ensure that all data handling – retrieval, processing, and storage – meets federal privacy standards. This includes implementing safeguards for protected health information (PHI) and maintaining detailed audit trails for system interactions.

Liability is another pressing concern. When RAG systems provide clinical recommendations, it’s essential to define who holds responsibility. Clear protocols should outline when clinicians should rely on AI-generated insights versus their own judgment, with proper documentation of these decisions. [...] Bias in medical knowledge bases is a critical issue. Historical biases related to factors like race, gender, or socioeconomic status can inadvertently influence RAG systems. Without proper monitoring and mitigation strategies, these biases could lead to inequitable care. Organizations must actively work to detect and address such issues.

Accessibility is also a legal requirement under the Americans with Disabilities Act. RAG systems must be compatible with assistive technologies like screen readers and voice recognition software, ensuring they can be used by healthcare professionals and patients with disabilities. [...] ## Implementation Strategies and Best Practices

Developing RAG systems for healthcare requires meticulous technical planning and strict adherence to regulatory standards. The combination of complex medical data, the need for real-time precision, and the priority of patient safety calls for a well-structured approach that balances innovation with compliance.

### Technical Requirements for RAG Integration

To function effectively, RAG systems depend on a robust, HIPAA-compliant infrastructure with fast response times. At the core are secure vector databases that efficiently store and retrieve medical knowledge. These databases must use HIPAA-compliant encryption for both data at rest and in transit, while employing access controls that log every query and response.

-----

-----

Phase: [EXPLORATION]

### Source [85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12059965/

Query: What legal tech RAG lessons apply to medical diagnosis systems?

Answer: ### Ethical, legal, and regulatory considerations [...] ### Transparency and explainability

The decision-making process of LLMs, even with RAG, can lack transparency, making it difficult to understand why a particular answer was generated. In medical contexts, being able to trace the reasoning back to specific evidence is crucial for trust and accountability.8

### Integration into clinical workflows

Successfully integrating RAG models into real-world clinical practice presents operational challenges. These include ensuring the system is user-friendly, doesn't increase cognitive load for clinicians, and has appropriate safeguards against system downtime.9,10,12

-----

-----

Phase: [EXPLORATION]

### Source [86]: https://legal.thomsonreuters.com/blog/retrieval-augmented-generation-in-legal-tech/

Query: What legal tech RAG lessons apply to medical diagnosis systems?

Answer: Highlights

RAG is a method of using AI to generate text by first retrieving relevant documents and then using those documents as inputs to the AI.
It improves the accuracy and reliability of AI-generated text, especially in domains where there is a lot of specialized knowledge, such as law.

Legal research tools using RAG should be carefully evaluated to ensure that they are using high-quality data and that the models are being tested and benchmarked for accuracy [...]

-----

</details>

<details>
<summary>How might quantum computing disrupt traditional RAG architectures?</summary>

Phase: [EXPLORATION]

### Source [87]: https://www.mdpi.com/journal/ai/special_issues/0CNB0I33J8

Query: How might quantum computing disrupt traditional RAG architectures?

Answer: Quantum Computing offers transformative opportunities for enhancing RAG systems, particularly in vector search optimization for information retrieval. The computationally intensive similarity calculations critical to document retrieval represent a bottleneck for large-scale implementations. Quantum-enhanced information retrieval could potentially revolutionize the efficiency of these operations. Additionally, RAG-enhanced LLMs show significant promise for quantum code generation, making quantum programming more accessible to non-specialists by providing contextually relevant code examples and documentation. This Special Issue will supplement the existing literature by bridging these rapidly evolving fields, which have primarily been studied in isolation. While substantial research exists on LLMs, knowledge graphs, RAG, and their individual applications, their synergistic integration—especially in specialized domains like Human–Robot Interaction and Quantum Computing—remains underexplored. By fostering interdisciplinary dialogue, this Special Issue will accelerate innovation in areas where traditional approaches face limitations, placing a particular emphasis on evaluation methodologies and explainability to ensure these advanced systems are not only powerful but also trustworthy and interpretable.

-----

-----

Phase: [EXPLORATION]

### Source [89]: https://ijirp.org/index.php/files/article/view/130

Query: How might quantum computing disrupt traditional RAG architectures?

Answer: Quantum computing is the paradigm shift of information processing that can completely impact the conventional information technology infrastructure. Compared to classical computing systems that are based on binary logic and sequential computing, quantum computers use quantum bits, superposition and entanglement to compute complex computations faster than ever before. The present paper discusses the impact of the emergence of quantum computing on traditional IT architectures, software frameworks, data security mechanisms and enterprise computing strategies. The paper addresses the inefficiencies of mainstream infrastructure encountered by quantum-enabled capabilities, in particular, cryptography, large-scale optimization, simulation, and data analytics.

-----

</details>

<details>
<summary>What failure modes limit hybrid search effectiveness on ambiguous enterprise queries?</summary>

Phase: [EXPLORATION]

### Source [94]: https://wearefram.com/blog/enterprise-rag/

Query: What failure modes limit hybrid search effectiveness on ambiguous enterprise queries?

Answer: Hybrid search blends vector search and keyword search and tends to outperform pure vector search in enterprise data. However, treating the vector database as a black box leads to unstable relevance. Teams should track recall@K on eval questions, precision on top results after reranking, latency per retrieval call, and failure rate from ACL filtering. Content changes over time, vocab changes, product names change, requiring embedding drift checks and rerunning evaluation every month. Index settings matter for stable relevance; many teams overlook this. Retrieval requires tuning: increase top-K from 5 to 10 early on, add hybrid search for exact terms, add reranking to improve precision. Enterprises need hybrid search combining vector for semantic similarity and keyword for exact codes, IDs, product names, but optimization like separate indexes by domain/language, metadata filters early, deduplication is necessary to avoid issues.

-----

-----

Phase: [EXPLORATION]

### Source [95]: https://gradientflow.substack.com/p/a-pragmatic-guide-to-enterprise-search

Query: What failure modes limit hybrid search effectiveness on ambiguous enterprise queries?

Answer: Enterprise search faces inherent ambiguity due to data lacking clear ownership, governance, structure. Multiple versions of documents (drafts, outdated wiki, final PDF) create staleness and duplication, polluting knowledge base into low-signal environment where even strong retrievers like keyword-based or basic vector similarity struggle to find ground truth. Relevance is deeply contextual and ambiguous; lacks universal signals like PageRank or user behavior. Simple retrieval methods fail, returning semantically related but contextually useless results. A sales exec and software engineer get different needs from same query like 'quarterly goals'. This garbage in, garbage out limits effectiveness on ambiguous queries.

-----

-----

Phase: [EXPLORATION]

### Source [96]: https://celerdata.com/glossary/hybrid-search

Query: What failure modes limit hybrid search effectiveness on ambiguous enterprise queries?

Answer: Hybrid search limitations include increased system complexity from integrating multiple retrieval methods, requiring careful tuning of fusion strategies to balance results. May miss contextual nuances and relationships. Limited explainability of results. Challenges with dynamic or evolving data requiring frequent re-embedding. Traditional keyword search fails on synonyms, typos, user ambiguity; vector-only on recall for niche terms. Hybrid aims to balance but faces these issues, especially at scale with heterogeneous datasets and nuanced queries.

-----

-----

Phase: [EXPLORATION]

### Source [97]: https://levelup.gitconnected.com/hybrid-search-is-not-one-thing-reliable-enterprise-ai-systems-b41ba0ee9964

Query: What failure modes limit hybrid search effectiveness on ambiguous enterprise queries?

Answer: Pure vector search fails on exact matches and unique identifiers; retrieves semantically similar items but misses the exact target, like documents on other articles instead of 'Article 9'. Embeddings can't encode unseen exact strings precisely enough for reliable matching. Users seeking specific regulation names want exact text string matches, not similarity, leading to wrong retrievals and responses.

-----

-----

Phase: [EXPLORATION]

### Source [98]: https://www.elastic.co/what-is/hybrid-search

Query: What failure modes limit hybrid search effectiveness on ambiguous enterprise queries?

Answer: Lexical algorithms like BM25F excel at precision for matching terms but fail when relevant content is expressed differently (e.g., 'athletic footwear' misses 'shoes' or 'trail runner'). Semantic vector search retrieves conceptually similar documents but introduces noise if context is ambiguous. Hybrid combines them but inherits these failure modes on ambiguous queries.

-----

</details>

<details>
<summary>What latency costs does HyDE query expansion impose at billion-document scale?</summary>

Phase: [EXPLORATION]

### Source [99]: https://arxiv.org/pdf/2506.21568

Query: What latency costs does HyDE query expansion impose at billion-document scale?

Answer: Hypothetical Document Embeddings (HyDE) significantly improved semantic matching for sparse or ambiguous queries but at a substantial computational cost— introducing high latency overhead (˜43% slower on 1B, ˜60% slower on 4B). In the personal domain, HyDE exhibited a 100% hallucination rate. These results suggest HyDE is best suited for contexts where semantic depth outweighs performance constraints. Model scaling from 1B to 4B yielded modest latency improvements for the baseline and RAG pipelines (˜6–9% faster), but amplified variability in the HyDE pipeline. This indicates diminishing returns for hypothesis-driven approaches without further optimization. Key Takeaways: 1. RAG consistently accelerates response (˜17% faster at 1B; still ˜9% faster at 4B) with low variance. 2. Standard benefits moderately from scaling (˜6.5% faster at 4B). 3. HyDE introduces high latency—worsened at higher scale—making it suitable only when hypothesis-generation merits justify performance cost. Boxplots (Figure 2) confirm that both Standard and RAG reduce interquartile range upon scaling, while HyDE’s spread expands. 5.1.4 Per-Case and Cross-Scale Comparisons Plotting absolute ∆-times (4B – 1B) by case (Figure 7) reveals: • Standard saw faster responses in 7 of 12 cases (max ∆˜ –3.3 s), with slowdowns in others (max ∆˜ +0.7 s). • RAG exhibited minor fluctuations, typically within ±1 s. • HyDE had the most pronounced dynamics: several queries slowed by over 5 s (up to +10.4 s in Case 5), with relative increases as high as 96%. Relative ∆-percent plots (Figure 8) reinforce that Standard and RAG benefit modestly from scaling, while HyDE’s overhead is disproportionately amplified on complex queries.

-----

-----

Phase: [EXPLORATION]

### Source [101]: https://medium.com/@mudassar.hakim/retrieval-is-the-bottleneck-hyde-query-expansion-and-multi-query-rag-explained-for-production-c1842bed7f8a

Query: What latency costs does HyDE query expansion impose at billion-document scale?

Answer: HyDE weaknesses: High latency, High cost (multiple embeddings + searches). Use HyDE when: Queries are short or underspecified, Documents are long and structured, Precision matters more than recall, You want minimal infrastructure overhead. Use Multi-Query RAG when: You can afford higher latency and cost. Common production optimizations: Cache HyDE outputs aggressively. The article discusses HyDE in production contexts, noting high latency as a weakness, but does not provide specific numbers for billion-document scale.

-----

-----

Phase: [EXPLORATION]

### Source [102]: https://aclanthology.org/2024.findings-emnlp.103.pdf

Query: What latency costs does HyDE query expansion impose at billion-document scale?

Answer: A shared limitation across query expansion approaches, including HyDE, is the increased inference time due to the generation of extra passages with LLMs. Table 5 shows latency: BM25 -14 ms +MuGI >2500ms generation + 230 ms index search. LLM generation latency is highly related to specific models and depends on server load. With accelerating frameworks like vLLM, generation speed could be much faster. HyDE demonstrates effective performance with contriever, but performs poorly with lexical-based retrievers. Query2Doc is effective with both sparse and dense retrieval methods.

-----

-----

Phase: [EXPLORATION]

### Source [103]: https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/

Query: What latency costs does HyDE query expansion impose at billion-document scale?

Answer: The content describes HyDE process: Generate hypothetical answer using LLM, embed it, search vector store. Improves retrieval on knowledge-intensive tasks, especially short vague queries vs detailed documents. No specific latency costs or numbers mentioned for HyDE at billion-document scale.

-----

</details>

<details>
<summary>How do citation formats in structured outputs influence RAG grounding effectiveness?</summary>

Phase: [EXPLORATION]

### Source [104]: https://mbrenndoerfer.com/writing/rag-prompt-engineering-context-citations

Query: How do citation formats in structured outputs influence RAG grounding effectiveness?

Answer: A critical requirement for production RAG systems is verifiability. You need to know which retrieved passage supported which claim in the generated response. Without citations, you cannot audit the model's outputs, you cannot build trust with users, and you cannot diagnose failures. This requirement shapes not just how you instruct the model to cite, but how you format the retrieved documents in the first place. The citation format you choose in the context portion of the prompt must match the citation format you request in the output portion, and both must be simple enough that the model can reliably execute them under generation pressure. The choice of citation format also affects the readability of the output for your end users. A system that produces academic-style footnote references serves a different audience than one that produces inline links or numbered superscripts. It is worth deciding what the output should look like for users before working backward to design the prompt that produces it. The most common approach embeds citation markers directly in the context, assigning each document a short identifier: [Document 1]: The transformer architecture was introduced in 2017. [Document 2]: Attention mechanisms allow models to focus on relevant parts of the input. Structured formatting using XML or clear delimiters helps models distinguish document boundaries, metadata, and content, reducing confusion between consecutive passages. The formatting choice also encodes provenance information, such as source ID, date, and relevance score, that the model can use when reasoning about which sources to trust and how to attribute claims. Consistent formatting within a prompt, using the same structure for every document, makes the model's job easier and reduces citation errors.

-----

-----

Phase: [EXPLORATION]

### Source [105]: https://cianfrani.dev/posts/citations-in-the-key-of-rag/

Query: How do citation formats in structured outputs influence RAG grounding effectiveness?

Answer: Tools ended up being more reliable than output formats for citations. Having the model call a tool to declare citations is natural and deterministic. We can detect when it’s needed and force it rather than hoping the model follows instructions. Structured Output: Use experimental_output with GPT-4o-mini and a Zod schema to extract citations. The AI SDK has an abstraction over Open AI’s structured output feature that is very experimental. But it forces json output. It’s literally part of the API. Initial result: It worked… okay. If you show all retrieved documents as “sources,” you’re not being honest. There’s no guarantee the LLM actually used all of those retrieved documents. The user experience looks something like “I’m sorry, I can’t find any information about the return policy. Sources: Unrelated Document 1, Unrelated Document 2, Unrelated Document 3”. Instead, we need a way to identify which specific documents the LLM actually used when generating its response, not just which documents we retrieved.

-----

-----

Phase: [EXPLORATION]

### Source [106]: https://www.tensorlake.ai/blog/rag-citations

Query: How do citation formats in structured outputs influence RAG grounding effectiveness?

Answer: Beyond RAG: Citations in Structured Data Extraction. The citation techniques we've covered work perfectly for conversational RAG applications. But what if you need structured data extraction with citations? Think financial reports where you extract specific metrics, or legal documents where you pull contract terms; scenarios where you need both the extracted values and proof of where they came from. Tensorlake's Structured Extraction API solves this with a single parameter. Unlike building citation pipelines manually (which requires coordinating parsing, chunking, retrieval, and response generation), this API handles the entire citation chain in a single call, similar to how Anthropic's Claude or OpenAI's structured outputs work, but with source linking. The same citation principles apply: you get page numbers, bounding boxes, and verifiable evidence, but without building the citation infrastructure yourself. Citation-aware RAG isn't just about trust, it's about building agentic applications that can be audited, verified, and deployed in production with confidence. Precise citations, like linking claims to exact paragraphs, table cells, and figures, separate professional agentic applications from chatbot demos. Users don't just get answers; they get evidence.

-----

-----

Phase: [EXPLORATION]

### Source [107]: https://www.ai21.com/knowledge/rag-for-structured-data/

Query: How do citation formats in structured outputs influence RAG grounding effectiveness?

Answer: Retrieval-augmented generation (RAG) systems can utilize both structured and unstructured data sources to ground a large language model’s (LLM’s) outputs in enterprise context. The use of RAG enhances prompts by retrieving relevant legal documents or data, grounding LLM outputs in real evidence to deliver accurate, context-specific answers aligned with enterprise knowledge and compliance standards. By retrieving answers directly from verified enterprise systems — such as databases or knowledge graphs — RAG applied to structured data produces outputs grounded in authoritative sources. This significantly reduces hallucination, as the large language model (LLM) retrieves the actual value or policy detail from structured data rather than generating content based solely on its training data.

-----

-----

Phase: [EXPLORATION]

### Source [108]: https://medium.com/lets-code-future/how-to-make-llms-cite-their-sources-and-why-rag-isnt-enough-86a9b107feed

Query: How do citation formats in structured outputs influence RAG grounding effectiveness?

Answer: "ONLY a valid JSON array" → Forces structured output. Structured outputs (less back-and-forth, fewer retries). Our first version: “Generate a comprehensive incident report”. Result: Beautiful prose. Zero citations. Our current version: “Generate claims, then find evidence”. Result: Auditable truth. Takeaway: Don’t ask LLMs to do analysis + citation simultaneously. Do analysis first, citation second. Gemini Flash is Underrated for Structured Tasks. - If a claim has no supporting evidence, omit it. - Line numbers are 1-indexed. Output: [ { "claim": "Nil pointer panic in checkout-api", "lines": [77, 83] }, ... ] Why this works: ✅ Gemini sees the FULL log (no chunking, no context loss) ✅ Explicit task (“find evidence” not “answer question”) ✅ Structured output (JSON enforces precision) ✅ Line numbers (exact attribution, not similarity scores). Layer 4: Assembly & Citation Injection. Model: GPT-4o-mini. Task: Insert [1], [2], [3] references into the draft report.

-----

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

- [chatbot](https://neo4j.com/blog/tag/chatbot/)
- [ChatGPT](https://neo4j.com/blog/tag/chatgpt/)
- [fine tuning](https://neo4j.com/blog/tag/fine-tuning/)
- [rag](https://neo4j.com/blog/tag/rag/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="graphiti-knowledge-graph-memory-for-an-agentic-world.md">
<details>
<summary>Graphiti: Knowledge Graph Memory for an Agentic World</summary>

Phase: [EXPLORATION]

**Source URL:** <https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/>

# Graphiti: Knowledge Graph Memory for an Agentic World

https://dist.neo4j.com/wp-content/uploads/20250325060206/Daniel-Chalef-150x150.jpg

[Daniel Chalef](https://neo4j.com/blog/contributor/daniel-chalef/)

Founder and CEO, Zep AI

March 24, 2025

5 min read

https://dist.neo4j.com/wp-content/uploads/20250325055037/1wkgXwFJf8gY5GZoCT66Dmg.png

The real potential of AI goes beyond basic chatbots powered by [retrieval-augmented generation](https://neo4j.com/blog/genai/what-is-retrieval-augmented-generation-rag/) (RAG). It’s about creating autonomous agents capable of independently solving tasks — from simple interactions to complex workflows. To do this effectively, agents need more than static retrieval; they need a dynamic memory that continuously integrates user interactions, enterprise data, and external knowledge.

Current RAG approaches struggle when data is updated frequently, limiting their effectiveness for agent-based systems. To solve this, Zep AI’s Graphiti framework introduces a flexible, real-time memory layer built on temporally aware [knowledge graphs](https://neo4j.com/books/developers-guide-how-to-build-knowledge-graph/) and stored in Neo4j.

Let’s break down how Graphiti works and compare it to query-focused summarization (QFS). In particular, we’ll look at the popular Microsoft Research GraphRAG implementation of QFS.

## The Problem With Static Approaches

Microsoft’s approach to GraphRAG builds entity-centric knowledge graphs by extracting entities and relationships and grouping them into thematic clusters or “communities.” It relies on LLMs to precompute summaries of these communities. When handling queries, the Microsoft GraphRAG makes multiple LLM calls — first generating partial community-level responses, then combining them into a single comprehensive answer.

Their approach excels at providing detailed, context-rich responses from large static datasets. However, it’s less effective in scenarios where data frequently changes since updates can trigger extensive recomputation of the entire graph. Additionally, its multi-step summarization makes retrieval slow, often taking tens of seconds. This latency and lack of dynamic updates make this approach to GraphRAG unsuitable as a comprehensive and holistic memory for agentic applications.

## Graphiti With Neo4j: Real-Time Dynamic Agent Memory

Graphiti helps overcome static RAG’s limitations with dynamic data. It’s a real-time, temporally-aware knowledge graph engine that incrementally processes incoming data, instantly updating entities, relationships, and communities without batch recomputation. Graphiti isn’t just another retrieval tool — it’s an ever-present source of context for agents, continuously available and updated.

Graphiti simultaneously handles chat histories, structured JSON data, and unstructured text. All data sources can feed into a single graph, or multiple graphs can coexist within the same Graphiti setup. This gives agents a unified, evolving view of the agent’s world — something traditional RAG systems fundamentally can’t provide.

> Find Graphiti on [opens in new tabGitHub](https://github.com/getzep/graphiti).

## Why Graphiti Works Better With Dynamic Data

Graphiti’s real-time incremental architecture is built for frequent updates. It continuously ingests new data episodes (events or messages), extracting and immediately resolving entities and relationships against existing nodes.

> For an in-depth technical exploration of Graphiti and performance benchmarks, check out [opens in new tabZep: A Temporal Knowledge Graph Architecture for Agent Memory](https://zep.link/sota-paper).

A key feature is Graphiti’s bi-temporal model, which tracks when an event occurred and when it was ingested. Every graph edge (or relationship) includes explicit validity intervals (t\_valid, t\_invalid). Graphiti uses semantic, keyword, and graph search to determine whether new knowledge conflicts with existing knowledge. When conflicts arise, Graphiti intelligently uses the temporal metadata to update or invalidate, but not discard, outdated information, preserving historical accuracy without large-scale recomputation.

This temporal model enables powerful historical queries, allowing users to reconstruct states of knowledge at precise moments or analyze how data evolves over time.

https://cdn-images-1.medium.com/max/1024/0*WNycmjCXoXjuxm4U

## Fast Query Speeds: Instant Retrieval Without LLM Calls

Graphiti is built for speed. Zep’s own Graphiti implementation achieves extremely low-latency retrieval, returning results at a P95 latency of 300ms. This is enabled by a hybrid search approach that combines semantic embeddings, keyword (BM25) search, and direct graph traversal — avoiding any LLM calls during retrieval.

The use of vector and BM25 indexes offers near-constant time access to nodes and edges, regardless of graph size. This is made possible by Neo4j’s extensive support for both of these index types.

Graphiti’s query latency makes it ideal for real-time interactions, including voice applications.

## Custom Entity Types: A Simple Ontology Implementation

Graphiti automatically builds an ontology based on incoming data, taking care to de-duplicate nodes and label edge relationships consistently. Beyond automatic ontology creation, Graphiti provides an intuitive method to define custom, domain-specific entities using familiar Pydantic models.

These custom entity types allow precise context extraction, greatly improving the quality of agent interactions. Example entity types might include:

- Personalized user preferences and interests (like favorite restaurants, contacts, hobbies), along with standard attributes (name, birthdate, address)
- Procedural memory, capturing instructions for actions
- Domain-specific business objects (e.g., products, sales orders)

```
from pydantic import BaseModel, Field

class Customer(BaseModel):
    """A customer of the service"""
    name: str | None = Field(..., description="The name of the customer")
    email: str | None = Field(..., description="The email address of the customer")
    subscription_tier: str | None = Field(..., description="The customer's subscription level")
Copied
```

Graphiti automatically matches extracted entities to defined custom types. Custom entity types enhance an agent’s ability to recall knowledge accurately and improve contextual awareness, which is essential for consistent, relevant interactions.

## Key Comparison

The following table shows a breakdown of the key characteristics of Graphiti compared to QFS-based GraphRAG.

https://dist.neo4j.com/wp-content/uploads/20250417061702/graphiti-table-1024x669.webp

## Graph Memory Powering an Agentic Future

Graphiti represents a meaningful departure from traditional RAG methods, specifically because it was built from the ground up as a memory infrastructure for dynamic agentic systems. Graphiti offers incremental, real-time updates through its temporally aware knowledge graph. This design means engineers no longer need to recompute entire graphs when data changes. Instead, Graphiti incrementally integrates updates, resolves conflicts based on temporal metadata, and maintains an accurate historical state.

By removing the bottleneck of LLM-driven summarization at query time, Graphiti achieves practical latency levels that engineers require for interactive real-world applications. Its hybrid indexing system — combining semantic embeddings, keyword search, and graph traversal — allows rapid retrieval in near-constant time, independent of graph scale. With intuitive tools like custom entity types implemented through familiar structures such as Pydantic models, Graphiti addresses a significant capability gap in agent development, equipping engineers with a robust, performant, and genuinely dynamic memory layer.

> Learn more about [opens in new tabZep and Graphiti](https://www.getzep.com/?utm_campaign=neo4j-graphiti&utm_medium=blog&utm_source=neo4j).

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="improve-your-rag-accuracy-with-a-smarter-chunking-strategy.md">
<details>
<summary>Improve Your RAG Accuracy With A Smarter Chunking Strategy</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a>

# Improve Your RAG Accuracy With A Smarter Chunking Strategy

### Here's how to pick a good one based on your data + use case.

[https://substackcdn.com/image/fetch/$s_!4RCn!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34b0abb3-a350-4dc1-9c65-cf0cb61f866f_800x800.jpeg](https://substack.com/@sarthakrastogi)

[Sarthak Rastogi](https://substack.com/@sarthakrastogi)

Oct 18, 2025

#### Bad chunking is like taking a well-organised filing cabinet and dumping everything on the floor, then wondering why you can’t find anything.

😐

Everyone obsesses over which embedding model to use. Or which vector database has the lowest latency. Or prompt engineering their retrieval queries to perfection.

But **your RAG system is probably failing because of how you’re chunking your documents.** Chunking is arguably the most important decision you’ll make, and it’s the one easiest to get wrong.

I’ve seen teams spend weeks fine-tuning embedding models, only to get mediocre results because they’re using fixed-size chunking that splits sentences mid-thought. It’s like having a Ferrari with flat tires.

* * *

## How to Use This Article

- **If you’re building a RAG system right now:** Skip to the section matching your document type (financial, medical, technical, etc.) and implement those strategies immediately.

- **If you’re debugging poor RAG performance:** Start with “Why Most Chunking Strategies Are Awful” to diagnose the issue, then jump to solutions.

- **If you’re optimizing an existing system:** Focus on “Scaling to 10K+ Documents” and the evaluation metrics section.

- **If you’re just learning about RAG:** Read straight through. The examples will make everything clear.

* * *

## Table of Contents

1. Why Most Chunking Strategies Are Awful

2. The Three Types of Chunking Strategies

3. Layout-Aware Chunking: The Game Changer

   - [See interactive visualisation for this topic](https://www.miskies.app/miskie/miskie-1760769325400)
4. Advanced Strategies That Actually Work

   - [See interactive visualisation for this topic](https://www.miskies.app/miskie/miskie-1760769543652)
5. Domain-Specific Playbooks

1. [See interactive visualisation for this topic](https://www.miskies.app/miskie/miskie-1760769820033)

      - Financial Documents

      - Medical Records

      - Legal Contracts

      - Technical Manuals
6. Handling Tables and Images

7. Scaling to 10K+ Documents in prod

8. How to Actually Evaluate Your Chunking Strategy

9. The Decision Framework

* * *

## Why Most Chunking Strategies Are Awful

Let me show you what bad chunking looks like in practice.

You have a financial report. There’s a table showing quarterly revenue. Right after the table, there’s a paragraph explaining why Q3 revenue dropped 15%. Your chunking strategy splits them into separate chunks.

Someone asks: “Why did Q3 revenue decline?”

Your RAG system retrieves the table. But not the explanation. The LLM hallucinates an answer based on the numbers alone. Wrong answer. User loses trust.

This isn’t a theoretical problem. This happens **constantly** in production RAG systems.

Here’s another one: You’re chunking a legal contract with fixed 512-token windows. A clause about liability spans 650 tokens. Your chunker splits it right in the middle. The first chunk says “The company is liable for...” and the second chunk starts with “...except in cases of this and that.”

Guess which chunk gets retrieved when someone asks about liability? Yeah, the first one. Without the exception. Legal team is not happy.

Or this: You’re processing medical records with recursive character chunking. A patient’s medication list is followed by critical warnings about drug interactions. They get split. Someone queries about prescribing that medication. The warning never shows up. That’s a patient safety issue.

**The problem isn’t your embedding model. It’s that you’re feeding it garbage.**

### The Three Red Flags of Bad Chunking

**Red Flag #1: Context loss at boundaries**

You’re reading along, everything makes sense, then suddenly the chunk ends mid-sentence. The next chunk starts with “However, this approach...”

This approach? What approach?? The LLM has no idea because the previous context is gone.

**Red Flag #2: Tables without full context (or incomplete tables)**

Incomplete tables are useless. While it’s not hard to make sure that tables are treated as individual chunks (and not split up), there’s another problem.

Tables without their context are useless. You’ll see RAG systems retrieve tables that are perfectly formatted, completely accurate, and utterly meaningless because nobody knows what the table is measuring.

“Here’s a table with numbers” is not helpful. “Here’s Q3 revenue by region, showing the 15% decline mentioned in the CEO’s statement” is helpful.

**Red Flag #3: List item issues**

Similarly you’ll see chunking split a list so that only the first chunk has the list header. Now you have five chunks that say:

- “Item 1: Something about compliance”

- “Item 2: Something about auditing”

- “Item 3: Something about reporting”

Something about WHAT? Compliance with what? The header that explained this was a “Data Protection Checklist” is in a different chunk.

### Why This Happens

Suppose we start with the simplest possible approach: fixed-size chunking. Split the text every 512 tokens. Done.

It’s fast. It’s simple. It’s predictable.

It’s also terrible.

Fixed-size chunking doesn’t know what a sentence is. It doesn’t know what a paragraph is. It certainly doesn’t know what a table is. It just counts to 512 and cuts.

Then we can get slightly more sophisticated and try recursive character splitting. “I’ll split on paragraph breaks, then line breaks, then spaces!”

Better. But still not very helpful cus your document has structure that you’re completely ignoring.

**Your documents weren’t randomly generated. Someone organised them deliberately.**

There are headers that tell you what each section is about. There are tables that group related information. There are lists that enumerate steps or requirements.

All of that structure? We need to **respect** it. But fixed-size and recursive chunking throw it away.

> It’s like taking a well-organised filing cabinet and dumping everything on the floor, then wondering why you can’t find anything.

* * *

## The Three Types of Chunking Strategies

Not all chunking strategies are created equal. Here’s how they break down:

https://substackcdn.com/image/fetch/$s_!UDYD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b9f065e-d41f-4da7-b0bb-47015f54bdd9_1024x1024.png

### Naive Strategies (The Baseline You Should Move Past)

- **Fixed-Size Chunking:** Split every N tokens. Fast, simple, and loses all context.

Use case: You need a quick prototype or you’re working with genuinely unstructured text (chat logs, social media feeds). That’s it.

- **Recursive Character Chunking:** Split on `\n\n`, then `\n`, then spaces. Slightly respects structure.

Use case: Mixed document types where you need something better than fixed-size but don’t want complexity.

These are your training wheels. They’re fine for learning. Not fine for production.

### Semantic Strategies (Getting a Lilll Bit Better)

**Semantic Chunking:** Use embeddings to detect topic shifts. Split when the semantic distance between sentences >= a threshold.

This is where things get interesting. Instead of blindly counting tokens, you’re actually looking at what the text means. When the topic changes, you split.

Research shows semantic chunking significantly outperforms naive approaches. It preserves coherent topics within chunks, which means better retrieval accuracy.

The catch is that it requires running an embedding model on every sentence, calculating distances, and tuning thresholds. More compute, more complexity, but much better results.

**When to use it:** Complex documents where topic boundaries matter more than structural boundaries. Academic papers, long-form articles, research reports.

### Structure-Aware Strategies (The Good Stuff)

This is where you should be spending your time.

**The Core Insight:** Documents already have structure. Use it.

Here’s what works really well:

- Recognising that a document has headers, and those headers tell you what the following paragraphs are about.

- Recognizing that a table is a self-contained unit.

- Recognizing that a list is a list.

- And so on.

* * *

## Layout-Aware Chunking

Humans don’t read documents as flat text streams. We use visual cues.

[See an interactive visualisation](https://www.miskies.app/miskie/miskie-1760769325400)

When you open a PDF, you immediately see:

- The title (big, bold, top of page)

- Section headers (medium, bold, with spacing)

- Paragraphs (blocks of regular text)

- Tables (grid structure, distinct from text)

- Lists (bullets or numbers, indented)

- Figures (images with captions)

You use all of this to understand the document. Why shouldn’t your RAG system?

**Layout-aware chunking means parsing documents with their structure intact.** You identify titles, headers, sections, tables, lists, and figures. Then you chunk intelligently around those boundaries.

### How It Actually Works

Let’s walk through a real example. You have a 10K financial filing.

**Traditional approach:**

```
1. Split every 512 tokens

2. Get 847 chunks

3. Pray for good retrieval
```

**Layout-aware approach:**

```
1. Parse document and identify structure
   - 42 section headers detected
   - 18 tables detected
   - 127 subsections detected

2. Create hierarchical chunks
   - Each table = separate chunk (with header preserved)
   - Each subsection = separate chunk (with section header added)
   - Each list = chunked by items (with list title added)

3. Add metadata
   - section_id: “financial_statements.income_statement”
   - parent_section: “financial_statements”
   - chapter: “annual_results”
   - page_number: 47
```

Now when someone asks about Q3 revenue, you don’t just retrieve a random chunk. You retrieve the income statement section, with full context about what you’re looking at.

https://substackcdn.com/image/fetch/$s_!mOyZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8aa5c96-a618-4950-b0f0-f05e481cb2e2_1536x1024.png

### Three Principles of Layout-Aware Chunking

**Principle 1: Respect Visual Boundaries**

If there’s a section header, that’s a semantic boundary. Don’t split across it unless absolutely necessary.

If there’s a table, keep it together. Don’t split it unless it’s huge (and even then, split row-by-row, not mid-row).

If there’s a list, keep related items together. Don’t separate list items from their header.

**Principle 2: Preserve Context Through Metadata**

Every chunk should know where it came from. What section? What chapter? What page?

This lets you implement clever retrieval patterns. Retrieve a specific chunk, but show the LLM the entire section. Or retrieve based on chunk-level precision, but expand to parent-level context when needed.

**Principle 3: Handle Special Elements Specially**

Tables are structured data. Extract them separately, convert to CSV or markdown, and chunk them intelligently.

Same with lists. Same with code blocks in technical docs. Same with figures.

Don’t treat everything as a flat text stream. It’s not.

### The Tools That Make This Possible

You need a parser that understands document layout.

Three example options (lmk in a comment if you prefer another one)

- **DeepDocDetection** (open source): Great for PDFs. Detects titles, headers, paragraphs, tables, figures. Free. Requires some setup.

- **Amazon Textract** (AWS service): Production-ready. Handles complex layouts. Detects titles, headers, sub-headers, tables, figures, lists, footers, page numbers, key-value pairs. Costs money but works reliably.

- **Docling** (preprocessing): Good for standardizing different document formats before chunking.

* * *

## Advanced Strategies That Actually Work

Once you’ve got layout-aware chunking down, there are three advanced techniques worth knowing.

[See an interactive visualisation](https://www.miskies.app/miskie/miskie-1760769543652)

### Hierarchical/Parent-Child Chunking

The problem: You want small chunks for precise retrieval. But you also want large chunks for context preservation.

The solution: Create both.

**How it works:**

1. Create large “parent” chunks (1000-2000 tokens) that preserve broad context

2. Split those into smaller “child” chunks (200-500 tokens) for precise matching

3. Index the child chunks for retrieval

4. Return the parent chunks to the LLM for generation

When someone asks a question, you match against the small, focused child chunks. But you give the LLM the large parent chunk with full context.

Best of both worlds.

**Real example:** Technical documentation. A section explains how to configure a database. The parent chunk is the entire “Database Configuration” section. The child chunks are individual configuration parameters.

User asks: “How do I set the connection timeout?”

You retrieve the child chunk about connection timeout (precise match). But you return the entire Database Configuration section to the LLM (full context about database settings, prerequisites, related parameters).

Result: Accurate answer with proper context.

### Agentic Chunking (When Accuracy Matters More Than Speed)

This one’s expensive. But for high-value use cases, it’s worth it.

**The concept:** Use an LLM to decide how to chunk.

1. Convert sentences to standalone propositions (replace pronouns with actual references)

2. Have an LLM evaluate each proposition: “Does this belong in the current chunk or should I start a new one?”

3. Group semantically related propositions, even if they’re far apart in the document

**Example transformation:**

- Original: “He led NASA’s Apollo 11 mission.”

- Proposition: “Neil Armstrong led NASA’s Apollo 11 mission.”

Now that proposition makes sense on its own, without context from previous sentences.

**The results:** Reduction in incorrect assumptions. Significantly better answer completeness.

**The cost:** Multiple LLM calls per document. Slow. Expensive.

**When to use it:** Customer support knowledge bases, legal document analysis, medical literature review. Cases where getting the right answer matters more than processing speed.

### Late Chunking (For Cross-References and Pronouns)

Standard approach: chunk first, embed later.

Late chunking: embed first, chunk later.

**Why this matters:** When you embed after chunking:

- Each chunk only has context from within itself.

- Pronouns become ambiguous.

- Cross-references break.

Late chunking processes the entire document through the embedding model first. Every token gets embedded with full document context, then you chunk the token embeddings.

Result: Chunks maintain semantic information from the whole document. “The system” in chunk 47 still knows which system we’re talking about from chunk 2.

**When to use it:** Technical documentation with lots of cross-references. Academic papers that reference earlier sections. Any document where pronouns and implicit references are common.

**The catch:** Requires long-context embedding models (Jina AI embeddings v3, for example) and more compute upfront.

* * *

## Domain-Specific Playbooks

Different document types need different approaches.

[See an interactive visualisation](https://www.miskies.app/miskie/miskie-1760769820033)

### Financial Documents

**The Challenge:**

- Tables everywhere.

- Numbers that need context.

- Sections that reference each other.

**The Strategy:** Layout-aware chunking with specialised table handling.

**Step-by-step:**

1. Use a layout parser (Textract or DeepDocDetection) to identify all structural elements

2. Handle tables specially:

   - Extract each table separately

   - Convert to CSV or markdown

   - Chunk row-by-row if the table is large

   - Include column headers with every chunk

   - Add the table title (usually the sentence or paragraph right before the table)
3. Preserve section hierarchy:

   - Income Statement is a section

   - Revenue by Segment is a subsection

   - Q3 Regional Breakdown is a sub-subsection

   - Store this hierarchy in metadata
4. Handle merged cells intelligently:

   - Unmerge them

   - Duplicate the original value into each cell

   - Ensures row-by-row chunking doesn’t lose information

**What this solves:**

- Revenue questions get answered with the right context.

- Financial metrics come with their explanations.

- Tables don’t float around contextless.

### Medical Documents

This is a very high stakes one.

**The Challenge:**

- Chronological relationships matter a lot.

- Clinical structure (SOAP notes).

- Privacy considerations.

- Precision when answering a question is life-or-death.

**The Strategy:** Semantic chunking for nuance, layout-aware for structure.

**Key principles:**

1. Preserve clinical note structure:

   - Subjective, Objective, Assessment, Plan stay together

   - But each can be a separate chunk with metadata linking them
2. Maintain temporal context:

   - Medication history with dates

   - Symptom progression over time

   - Previous visit references
3. Use semantic chunking for research papers:

   - Medical literature has subtle topic shifts

   - Semantic boundaries matter more than visual ones
4. Handle medical terminology carefully:

   - Keep terms with their context

   - Don’t split disease names or drug combinations

   - Maintain relationships between symptoms and diagnoses

**What this solves:** Treatment questions get accurate, complete information. Drug interaction warnings don’t get separated from prescriptions. Patient history maintains chronological coherence.

### Legal Contracts

**The Challenge:**

- Clauses must stay intact.

- Cross-references are everywhere.

- Structure is legally significant.

**The Strategy:** Layout-aware + sliding window overlap for safety.

**Implementation:**

1. Use layout parsing to identify clause boundaries:

   - Numbered sections

   - Lettered subsections

   - Indentation levels
2. Never split a clause:

   - If a clause exceeds max chunk size, keep it together anyway

   - Better one oversized chunk than broken legal language
3. Add sliding window overlap (10-20%):

   - Extra safety net for clauses that span boundaries

   - Reduces risk of missing critical “except” or “provided that” language
4. Preserve cross-references:

   - “See Section 4.2” needs to be retrievable

   - Store section references in metadata

   - Enable following references programmatically

**What this solves:** Liability questions get complete clauses with exceptions. Cross-references work. Legal teams don’t yell at you.

### Technical Manuals

**The Challenge:**

- Step-by-step procedures.

- Diagrams with explanatory text.

- Code examples.

- Cross-references to other sections.

**The Strategy:** Layout-aware chunking with hierarchical metadata.

**Implementation:**

1. Respect document hierarchy:

   - Chapter → Section → Subsection → Procedure

   - Store all levels in metadata

   - Enables “give me everything about configuring X”
2. Keep procedures together:

   - Step 1, Step 2, Step 3 stay in one chunk

   - Or use parent-child: each step is a child, entire procedure is parent
3. Handle diagrams:

   - Use vision-language models to caption images

   - Store image description with surrounding text

   - Keep figure references intact
4. Preserve code blocks:

   - Code examples stay complete

   - Include comments and explanations

   - Link to related configuration settings

**What this solves:** Procedural questions get complete instructions. Diagrams and explanations stay together. Code examples are usable.

* * *

## Handling Tables and Images (The Stuff That Breaks Everything)

Let’s talk about the elephant in the room: Most documents aren’t just text.

### The Table Problem

Tables are structured data pretending to be text. Naive chunking sees them as sentences. Disaster.

**Three approaches that work:**

**Approach 1: Table-as-Text with Structure Preservation**

- Extract table to markdown or CSV

- Keep column headers with every chunk

- Add row numbers for reference

- Include table title/caption

**Approach 2: Table-as-Data with LLM Description**

- Extract table structure completely

- Use an LLM to write a natural language description

- Index both the description and the raw table

- Return the raw table to the LLM when retrieved

**Approach 3: Dual Indexing (Recommended)**

- Index table descriptions for retrieval

- Store complete tables separately

- Retrieve based on descriptions, return full tables

- Best of both: searchable descriptions, complete data for LLM

### Merged Cells

Financial reports love merged cells. Suppose “Q1-Q3 Revenue” spans three columns. Your table chunker breaks on column boundaries. Now you have three chunks with incomplete data.

**Solution:**

1. Detect merged cells during parsing

2. Unmerge them

3. Duplicate the original value into each individual cell

4. Now row-by-row chunking works properly

### The Image Problem

Images contain information. Your text-based chunker ignores them. Bad news.

**Three strategies:**

**Strategy 1: Image Captions Only**

- Extract image captions during parsing

- Include captions in surrounding text chunks

- Simplest but loses visual information

**Strategy 2: Vision-Language Model Descriptions**

- Use GPT-4o, LLaVA, or similar to describe images

- Store descriptions as text chunks

- Index descriptions, link to original images

- Retrieve description, return image to multimodal LLM

**Strategy 3: Multimodal Embeddings**

- Use CLIP or similar for unified image-text embeddings

- Index images and text together

- Retrieve multimodal chunks

- Requires multimodal LLM for generation

**For production:** Strategy 2. Descriptions are searchable, original images provide visual context, works with most LLMs.

### The List Problem (Seriously, This Breaks More Than You’d Think)

Lists are deceptively simple. Until you chunk them wrong.

**What breaks:**

```
List Header: “Security Compliance Requirements”
- Item 1: Encrypt data at rest
[chunk boundary]
- Item 2: Implement MFA
- Item 3: Regular security audits
```

Now items 2 and 3 are orphaned. Nobody knows these are compliance requirements.

**What works:**

```
Chunk 1:
Security Compliance Requirements
- Item 1: Encrypt data at rest

Chunk 2:
Security Compliance Requirements
- Item 2: Implement MFA

Chunk 3:
Security Compliance Requirements
- Item 3: Regular security audits
```

Each list item gets the header. Each chunk makes sense alone.

* * *

## Scaling to 10K+ Documents In Prod

Everything changes at scale. What works for 100 documents might not work for 10,000.

### The Page-Level Chunking Revelation

Research shows page-level chunking is surprisingly effective at scale. One page = one chunk (or a few chunks if the page is huge).

**Why this works:**

- Pages are already meaningful units

- Authors structure pages with coherent information

- Reduces total chunk count dramatically

- Simplifies metadata management

**When to use it:** Large document collections (10K+) where processing speed matters and documents are multi-page (PDFs, reports, books).

### The Metadata

At scale, metadata becomes critical. You need to filter before searching.

**Essential metadata:**

- document\_type: “financial\_report”, “legal\_contract”, “technical\_manual”

- date\_created: ISO format timestamp

- section\_id: hierarchical identifier

- parent\_chunk\_id: for hierarchical chunking

- source\_page: page number in original document

- confidence\_score: if using ML for structure detection

**Why this matters:** Searching 10,000 documents is slow. Searching “financial reports from Q4 2024” is fast.

Metadata lets you pre-filter to a manageable subset before doing vector similarity search.

### The Hybrid Approach That Actually Works

Different document types need different strategies. At scale, you can’t use one strategy for everything.

**Implementation:**

```
1. Classify documents by type
   - Financial: layout-aware + table processing
   - Technical: layout-aware + hierarchical
   - Legal: layout-aware + sliding window
   - Research: semantic chunking

2. Route to appropriate chunking pipeline

3. Store with consistent metadata schema

4. Search with type-aware retrieval
```

This seems complex. It is. But it’s necessary at scale.

### Chunk Size

Research consistently shows ~250 tokens (roughly 1000 characters) as a good starting point.

But—and this is important— **document structure matters more than token count.**

If your layout-aware chunker creates a 400-token chunk because that’s a complete section, that’s better than forcing it to 250 and breaking the section.

Use token limits as guidelines, not rules. Preserve semantic and structural integrity first.

* * *

## How to Actually Evaluate Your Chunking Strategy

You can’t improve what you don’t measure. Here’s how to know if your chunking works.

### The Metrics That Matter Here

**Context Relevancy:** Are retrieved chunks actually relevant to the query?

Measure: Human evaluation on sample queries. What percentage of retrieved chunks contain useful information?

Target: >80% relevancy on representative queries

**Answer Faithfulness:** Is the generated answer supported by retrieved chunks?

Measure: Check for hallucinations. Does the LLM invent facts not in the retrieved content?

Target: >90% faithfulness (anything less is dangerous)

**Answer Completeness:** Does the answer have all necessary information?

Measure: Compare against human-written answers. What’s missing?

Target: >85% completeness for critical use cases

### The Test Set You Need

Create 50-100 test queries representing real use cases:

**Easy queries** (30%):

- “What was Q3 revenue?”

- “Who is the CEO?”

- Direct fact lookups

**Medium queries** (50%):

- “Why did revenue decline in Q3?”

- “What are the security compliance requirements?”

- Requires context from multiple chunks

**Hard queries** (20%):

- “Compare Q3 performance across all product lines and explain regional variations”

- “What are the legal implications of the liability clause exceptions?”

- Requires synthesis across many chunks

### The A/B Test Protocol

Don’t guess. Test.

1. Implement Strategy A (baseline: maybe fixed-size chunking)

2. Implement Strategy B (candidate: maybe layout-aware)

3. Run same test queries through both

4. Compare metrics

5. Human evaluation on disagreements

**Important:** Test on YOUR documents with YOUR queries. Benchmark results from papers don’t tell you what works for your use case.

### The Red Flags That Mean You Need Better Chunking

Watch for these in user feedback:

- “The answer was close but missed a key detail” → Context loss at chunk boundaries

- “The system gave me a table but I don’t know what it means” → Table without context

- “The answer contradicted itself” → Retrieved conflicting chunks without shared context

- “The system couldn’t find information I know is there” → Poor chunk boundaries made content unretrievable

Each of these points to a chunking problem, not a retrieval problem.

* * *

## The Decision Framework

Here’s how to actually decide what to implement.

### Step 1: Understand Your Documents

What are you processing?

- Mostly text (articles, books, reports)

- Lots of tables (financial reports, data sheets)

- Lots of images (technical manuals, scientific papers)

- Highly structured (legal contracts, regulatory docs)

- Mixed content (real-world documents)

### Step 2: Understand Your Queries

What are people asking?

- Simple fact lookup (”What is X?”)

- Contextual questions (”Why did X happen?”)

- Comparison questions (”How does X compare to Y?”)

- Synthesis questions (”Explain the relationship between X, Y, and Z”)

Simple queries → simpler chunking might work

Complex queries → need sophisticated chunking

### Step 3: Understand Your Constraints

What are your limits?

**Processing time:**

- Need it fast? → Simpler chunking (recursive, layout-aware without heavy ML)

- Can be slow? → Sophisticated chunking (agentic, semantic with fine-tuning)

**Scale:**

- <1000 docs? → Any strategy works

- 1K-10K docs? → Need efficient processing, batch pipelines

- 10K docs? → Page-level chunking, distributed processing, metadata filtering

**Accuracy requirements:**

- Low stakes (internal docs)? → Start simple, iterate based on feedback

- High stakes (legal, medical)? → Invest in sophisticated chunking upfront

### Step 4: The Decision Tree

**For structured documents (PDFs, reports, manuals, contracts):** → **Start with layout-aware chunking**

Add hierarchical metadata if documents have clear section structure Add specialized table/list handling if those are common Add vision processing if images are critical

**For unstructured text (articles, books, chat logs):** → **Start with semantic chunking**

Add recursive boundaries if you need more consistent chunk sizes Consider sliding window if context loss is an issue

**For mission-critical applications (legal analysis, medical diagnosis):** → **Consider agentic chunking**

Only if accuracy matters more than cost/speed Test thoroughly before production

**For 10K+ documents:** → **Simplify where possible**

Page-level chunking as baseline Hybrid approach with document classification Heavy investment in metadata and filtering

### Step 5: Implementation Path

**Week 1: Baseline**

- Implement simplest reasonable strategy (recursive or layout-aware basic)

- Create test set of 50 queries

- Measure baseline performance

**Week 2: Iterate**

- Identify top failure modes from week 1

- Implement targeted improvements (table handling, list processing, etc.)

- Measure improvement

**Week 3: Optimise**

- Fine-tune chunk sizes

- Add metadata enrichment

- Optimise for your specific queries

**Week 4: Scale**

- Set up batch processing if needed

- Implement monitoring

- Plan for continuous improvement

* * *

## The Bottom Line

Most RAG systems fail because of chunking, not because of embeddings or LLMs.

**If you remember nothing else, remember this:**

1.  **Structure matters.** Documents have hierarchy. Use it.

2.  **Context matters.** Tables without explanations are useless. Lists without headers are meaningless.

3.  **Different documents need different strategies.** Financial reports aren’t blog posts.

4.  **At scale, simplicity wins.** Page-level chunking beats complex strategies on 10K+ documents.

5.  **Measure everything.** You can’t improve what you don’t measure.

Start with layout-aware chunking if you’re processing structured documents. It’s the single best improvement you can make to your RAG system.

Then iterate based on your specific failure modes. Add table handling. Add hierarchical metadata. Add specialized processing for lists.

But whatever you do, stop using fixed-size chunking in production. Your users deserve better.

* * *

## Further Reading

**Tools mentioned:**

- DeepDocDetection: github.com/deepdoctection/deepdoctection

- Amazon Textract: aws.amazon.com/textract

- Docling: Document preprocessing library

- LlamaIndex: llamaindex.ai

- LangChain: langchain.com

**Research papers:**

- Search “semantic chunking RAG 2024” for latest benchmarks

- Search “layout-aware document processing” for parsing techniques

- Search “hierarchical retrieval RAG” for parent-child strategies

**Implementation examples:**

- Look for “layout-aware document parsing for RAG” notebooks

- AWS samples: amazon-archives/layout-aware-document-processing

- Community implementations on GitHub

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="jina-scraped-1.md">
<details>
<summary>RAG System in Production: Architecture, Chunking & Evaluation Guide|47Billlion</summary>

Phase: [EXPLORATION]

**Source URL:** <https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/>

Title: RAG System in Production: Architecture, Chunking & Evaluation Guide|47Billlion

URL Source: https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/

Published Time: 2026-03-03T09:26:00+00:00

Markdown Content:
# RAG System in Production: Architecture, Chunking & Evaluation Guide|47Billlion

[Skip to content](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#main)

[47Billion](https://47billion.com/ "47Billion")

[![Image 1: Group-289916-1.png](https://47billion.com/wp-content/uploads/2025/04/Group-289916-1.png)](https://47billion.com/)

*   [Our work](https://47billion.com/our-work/)
*   [About](https://47billion.com/about/)
*   [Services](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)
    *   [AI/ML](https://47billion.com/ai-ml/)
    *   [Data Analytics](https://47billion.com/big-data-analytics/)
    *   [End-to-End Product Development](https://47billion.com/product-development/)
    *   [User Experience & Design](https://47billion.com/user-experience-design/)
    *   [US Staffing](https://47billion.com/us-staffing/)
    *   [Elevate Framework](https://47billion.com/ai-elevate/)

*   [Industries](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)
    *   [Healthcare](https://47billion.com/healthcare-industry/)
    *   [Financial Services](https://47billion.com/financial-services/)
    *   [Sustainability](https://47billion.com/esg-solutions/)
    *   [Education](https://47billion.com/education-industry/)

*   [Resources](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)
    *   [Blog](https://47billion.com/blog/)
    *   [Careers](https://47billion.com/careers/)
    *   [Press Release](https://47billion.com/press-release/)
    *   [Infographic](https://47billion.com/infographic/)
    *   [Whitepaper](https://47billion.com/white-paper/)

*   [Contact Us](https://47billion.com/contact-us/)

*   [Our work](https://47billion.com/our-work/)
*   [About](https://47billion.com/about/)
*   [Services](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)
    *   [AI/ML](https://47billion.com/ai-ml/)
    *   [Data Analytics](https://47billion.com/big-data-analytics/)
    *   [End-to-End Product Development](https://47billion.com/product-development/)
    *   [User Experience & Design](https://47billion.com/user-experience-design/)
    *   [US Staffing](https://47billion.com/us-staffing/)
    *   [Elevate Framework](https://47billion.com/ai-elevate/)

*   [Industries](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)
    *   [Healthcare](https://47billion.com/healthcare-industry/)
    *   [Financial Services](https://47billion.com/financial-services/)
    *   [Sustainability](https://47billion.com/esg-solutions/)
    *   [Education](https://47billion.com/education-industry/)

*   [Resources](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)
    *   [Blog](https://47billion.com/blog/)
    *   [Careers](https://47billion.com/careers/)
    *   [Press Release](https://47billion.com/press-release/)
    *   [Infographic](https://47billion.com/infographic/)
    *   [Whitepaper](https://47billion.com/white-paper/)

*   [Contact Us](https://47billion.com/contact-us/)

[![Image 2: Group-289916-1.png](https://47billion.com/wp-content/uploads/2025/04/Group-289916-1.png)](https://47billion.com/)

*   [Services](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Services](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)  

Menu  
    *   [AI/ML](https://47billion.com/machine-learning/)
    *   [Data Analytics](https://47billion.com/big-data-analytics/)
    *   [End-to-End Product Development](https://47billion.com/product-development/)
    *   [User Experience & Design](https://47billion.com/user-experience-design/)
    *   [US Staffing](https://47billion.com/us-staffing/)

[Elevate Framework](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Build AI that scales Our ELEVATE framework turns business problems into intelligent, well-designed systems.](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Explore the ELEVATE Framework![Image 3: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://47billion.com/ai-elevate/)

[Testimonials](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[They delivered a high-quality, user-friendly design for a competitive price.](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[View All![Image 4: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://clutch.co/profile/47billion)

![Image 5](https://47billion.com/wp-content/uploads/2025/03/elevate-ai-menu-54x300.png)

*   [Industries](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Industries](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)  

Menu  
    *   [Healthcare](https://47billion.com/healthcare-industry/)
    *   [Financial Services](https://47billion.com/financial-services/)
    *   [Sustainability](https://47billion.com/esg-solutions/)
    *   [Education](https://47billion.com/education-industry/)

[Case Studies](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Testimonials](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Sales and Marketing Analytics Platform which acts as a single source for the Client](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[View All ![Image 6: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://47billion.com/our-work/)

![Image 7](https://47billion.com/wp-content/uploads/2025/03/Group-290034-1.webp)

*   [Our Work](https://47billion.com/our-work/)
*   [Resources](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Resources](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)  

Menu  
    *   [Blog](https://47billion.com/blog/)
    *   [Careers](https://47billion.com/careers/)
    *   [Press Release](https://47billion.com/press-release/)
    *   [Infographic](https://47billion.com/infographic/)
    *   [White Paper](https://47billion.com/white-paper/)

[About 47Billion](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[We’re a team of experienced strategists, designers, and developers, working closely on all stages of your product journey – from conception to delivery.](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Know More ![Image 8: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://47billion.com/about/)

![Image 9: Group-290012-3-1](https://47billion.com/wp-content/uploads/elementor/thumbs/Group-290012-3-1-1-r9unh2p22typrekreq76qc0eixa6ekvsob4fli48uc.png)

*   [Services](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Services](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)  

Menu  
    *   [AI/ML](https://47billion.com/machine-learning/)
    *   [Data Analytics](https://47billion.com/big-data-analytics/)
    *   [End-to-End Product Development](https://47billion.com/product-development/)
    *   [User Experience & Design](https://47billion.com/user-experience-design/)
    *   [US Staffing](https://47billion.com/us-staffing/)

[Elevate Framework](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Build AI that scales Our ELEVATE framework turns business problems into intelligent, well-designed systems.](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Explore the ELEVATE Framework![Image 10: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://47billion.com/ai-elevate/)

[Testimonials](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[They delivered a high-quality, user-friendly design for a competitive price.](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[View All![Image 11: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://clutch.co/profile/47billion)

![Image 12](https://47billion.com/wp-content/uploads/2025/03/elevate-ai-menu-54x300.png)

*   [Industries](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Industries](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)  

Menu  
    *   [Healthcare](https://47billion.com/healthcare-industry/)
    *   [Financial Services](https://47billion.com/financial-services/)
    *   [Sustainability](https://47billion.com/esg-solutions/)
    *   [Education](https://47billion.com/education-industry/)

[Case Studies](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Testimonials](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Sales and Marketing Analytics Platform which acts as a single source for the Client](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[View All ![Image 13: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://47billion.com/our-work/)

![Image 14](https://47billion.com/wp-content/uploads/2025/03/Group-290034-1.webp)

*   [Our Work](https://47billion.com/our-work/)
*   [Resources](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Resources](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)  

Menu  
    *   [Blog](https://47billion.com/blog/)
    *   [Careers](https://47billion.com/careers/)
    *   [Press Release](https://47billion.com/press-release/)
    *   [Infographic](https://47billion.com/infographic/)
    *   [White Paper](https://47billion.com/white-paper/)

[About 47Billion](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[We’re a team of experienced strategists, designers, and developers, working closely on all stages of your product journey – from conception to delivery.](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/#)

[Know More ![Image 15: arrow icon](https://47billion.com/wp-content/uploads/2025/03/blue-arrow.svg)](https://47billion.com/about/)

![Image 16: Group-290012-3-1](https://47billion.com/wp-content/uploads/elementor/thumbs/Group-290012-3-1-1-r9unh2p22typrekreq76qc0eixa6ekvsob4fli48uc.png)

[Contact Us](https://47billion.com/contact-us/)

 Blog 

# RAG System in Production: Why It Fails and How to Fix It

By Kamalpreet Singh.Tech Lead,Aditya Pathak.Senior Software Engineer

By

Kamalpreet Singh. Tech Lead

Aditya Pathak. Senior Software Engineer

![Image 17](https://47billion.com/wp-content/uploads/2026/03/RAG-System-in-Production-Compress-1024x536.webp)

_From embeddings to evaluation: a practitioner’s guide to building RAG that actually works in production_

When we started building AI-powered document Q&A into our products, we made the same mistake most teams make.

We picked a vector database. We embedded our documents. We wired up GPT-4. We called it RAG.

And for a while, it looked like it was working.

Then someone asked a question that spanned three sections of a report. The answer came back confidently wrong. Not hallucinated — the information was _there_, in the document. The system just couldn’t find the right pieces and stitch them together.

That’s when we realized the problem wasn’t our LLM. It wasn’t our vector database. It was everything that happened _before_ retrieval — and everything we weren’t measuring _after_ generation.Designing this layer correctly is critical for teams building scalable, production-ready systems through structured [**enterprise AI development services**.](https://47billion.com/machine-learning/)

This is that story. And more importantly, this is what we learned.

**The Problem With “Just Add RAG”**

RAG — Retrieval-Augmented Generation — sounds straightforward: retrieve relevant documents, pass them to an LLM, get a grounded answer. No hallucinations, no stale training data.

In practice,it’s a pipeline with at least five places where things can silently break.

Here’s what a naive RAG system looks like:

User Query → Embed Query → Vector Search →Top-K Chunks → LLM → Response

Each arrow is a potential failure point. And most teams only optimize the last one — the LLM.

![Image 18](https://47billion.com/wp-content/uploads/2026/03/image.png)
**What LLMs Can and Can’t Do Alone**

Before we talk about RAG,let’s be clear about why it exists.

Large Language Models are trained on static text snapshots.They’re remarkably good at reasoning, summarizing, and generating — but they have three fundamental limitations that matter in production:

**Knowledge cutoff.**The model knows nothing about what happened after its training data were collected. For enterprise applications dealing with internal documents, policy updates, or real-time data, this is a dealbreaker.

**No private knowledge.**The model was never trained on your company’s documents, your product specs, or your customer data. You can’t fix this with fine-tuning alone — fine-tuning teaches _behavior_, not facts.

**Hallucination under uncertainty.**When an LLM doesn’t know something, it often doesn’t say “I don’t know.”It generates a plausible-sounding answer. This is fine for creative writing.It’s catastrophic for document Q&A, compliance, or medical applications.

RAG solves all three. But only if you build it correctly.

**Why RAG? The Actual Value Proposition**

The core idea: at inference time, retrieve relevant context from an external knowledge base and give it to the LLM as part of the prompt. The model then generates an answer grounded in what was retrieved — not what it vaguely remembers from training.

Without RAG: LLM answers from parametric memory → hallucination risk

With RAG: LLM answers from retrieved context →grounded, verifiable

This unlocks three things that matter for enterprise deployments:

**Updatability without retraining.**Update your knowledge base, and the system immediately knows the new information. No fine-tuning cycle, no redeployment.

**Attribution.**Every answer can be traced back to a source document. This is critical for compliance, legal, and regulated industries.

**Cost efficiency.**You don’t need the largest, most expensive model when the answer is literally in the context window. A smaller model with good retrieval outperforms a larger model with bad retrieval.

But here’s what the tutorials don’t tell you: the quality of your RAG system is almost entirely determined by what happens _before_ the LLM sees the query. Retrieval quality is the dominant variable.

**Where Naive RAG Fails**

RAG solves the LLM’s knowledge problem. But naive RAG — embed, retrieve top-K, generate — introduces its own failure modes. And these failures are silent: the system returns an answer,it just happens to be wrong.

Understanding these failure modes matters because every advanced technique covered in this guide exists to address one or more of them.

**Failure Mode****What Happens****Example**
**Vocabulary Mismatch**User phrasing doesn’t match document phrasing User asks “salary”but the document says “compensation package”
**Ambiguous Queries**Query is too vague or has multiple valid interpretations“Tell me about Python” — the snake, or the programming language?
**Lost in the Middle**LLM underweights relevant chunks positioned in the middle of a long context Correct answer is chunk 3 of 5 — the model effectively ignores it
**Irrelevant Top-K**Cosine similarity returns semantically close but contextually wrong chunks Returns results about “ML model training” when the question is about “ML model deployment”
**Chunking Artifacts**Answer split across chunk boundaries — retrieved in neither The explanation starts in chunk 7 and concludes in chunk 8
**No Answer Available**System hallucinates rather than admitting it doesn’t know Generates a confident answer from tangentially related chunks

Each section that follows — hybrid retrieval, advanced chunking,HyDE, reranking, evaluation — is a direct response to one or more rows in this table. Keep this map in mind as you read.

**Hybrid RAG: Beyond Pure Vector Search**

Most RAG tutorials show you one retrieval method: embed your query, find the nearest vectors, return the top-K results.

This is called**dense retrieval**— and it’s powerful but incomplete.

**The Problem With Pure Vector Search**

Dense retrieval is excellent at semantic similarity. Ask “what are the revenue figures for Q3?” and it finds chunks about financial performance even if they don’t contain that exact phrase.

But it fails on exact lookup. If you search for “Section 4.2.1” or “SKU-B4920” — a specific ID, a clause number, a product code — dense retrieval can miss it entirely. The embedding doesn’t capture character-level precision.

**The Problem With Pure Keyword Search**

BM25 and traditional keyword search (what Elasticsearch has used for decades) does the opposite.It’s extremely good at exact matches but fails on semantics. Search “how does the system handle payment failures?” and it might return nothing if the document says “transaction error recovery process” instead.

**Hybrid = Best of Both**

The solution is to run both in parallel and merge results. This is Hybrid RAG. In production systems, implementing hybrid retrieval effectively requires strong [**data engineering for AI systems**,](https://47billion.com/big-data-analytics/) where indexing strategy, metadata design, and search orchestration directly impact retrieval accuracy.

Query

 ├── Dense Retrieval (embedding similarity) → candidates_A

 └── Sparse Retrieval (BM25 keyword search) → candidates_B

 ↓

 Reciprocal Rank Fusion (RRF)

 ↓

 Unified Ranked Results

 ↓

 (Optional) Reranker

 ↓

 Final Top-K→ LLM

**Reciprocal Rank Fusion (RRF)**is the standard method for merging ranked lists from different retrievers.It’s simple and surprisingly effective — each result gets a score of 1/(rank + k) from each retriever, and scores are summed to produce a final ranking.

![Image 19](https://47billion.com/wp-content/uploads/2026/03/image-3.png)
**The Third Layer: Reranking**

After fusion, you still have 10-20 candidates. A**reranker**(cross-encoder) scores each retrieved chunk against the query — not just for embedding similarity, but for actual relevance.

Rerankers are slower than retrieval but more accurate. They process query+document pairs end-to-end, capturing nuance that bi-encoder embeddings miss. Models like Cohere Rerank, BGE Reranker, and Jina Reranker have become standard in production pipelines.

The flow: retrieve broadly →rerank precisely → send top 3-5 to LLM.

**Embeddings: The Layer Everyone Rushes Past**

Before you can retrieve anything, you need to represent your documents as vectors. The embedding model you choose matters more than most teams realize.

**What Embeddings Actually Are**

An embedding model converts text into a high-dimensional vector (typically 768 to 3072 dimensions). Semantically similar text produces geometrically close vectors. This is what enables semantic search.

**Choosing an Embedding Model**

Not all embedding models are created equal. Choosing the wrong one —especially for domain-specific content — can silently degrade your entire RAG system.

**Model****Dimensions****Best For**
text-embedding-3-small (OpenAI)1536 General purpose, fast
text-embedding-3-large (OpenAI)3072 Higher accuracy, more cost
BGE-M3 (BAAI)1024 Multilingual, hybrid retrieval built-in
E5-Large-v2 1024 Strong on MTEB benchmarks
Nomic Embed 768 Open source, self-hostable
Jina Embeddings v3 1024 Long documents, late chunking support

For specialized domains — legal, medical, code — domain-specific or fine-tuned embeddings consistently outperform general-purpose models.

**One Critical Thing Most Guides Skip: Embedding Dimensions Matter**

Larger embedding dimensions capture more nuance — but they’re also more expensive to store, index, and query. For most applications, text-embedding-3-small at 1536 dimensions is the right starting point. Upgrade only when benchmarks show clear improvement.

**Late Chunking: A Better Way to Embed Long Documents**

Traditional embedding: split the document into chunks, embed each chunk independently.

The problem: each chunk loses awareness of the document it came from. A chunk saying “the figure improved by 34%” has no context of what figure, in what context.

**Late Chunking**(introduced by Jina AI) inverts this: embed the _full document_ first using long-context models, then split the resulting token-level embeddings into chunks. Each chunk retains the global context of the document it belongs to.

The result: significantly better retrieval on long, structured documents where cross-section relationships matter.

**Chunking: The Most Underrated Decision in RAG**

Here’s the finding that should change how you think about RAG:

**Chunking strategy matters more than your choice of vector database.**

NVIDIA’s 2024 benchmarks across five document datasets found up to a 9% recall gap between the best and worst chunking strategies, with no other variable changed. A well-chunked corpus retrieves accurately on a basic vector DB. A poorly-chunked corpus fails even with the most sophisticated retrieval stack.

Yet most teams spend weeks evaluating vector databases and minutes thinking about chunking.

**Why Chunking Is Hard**

You’re trying to solve a fundamental tension:

*   **Chunks too large**→ embeddings average multiple topics → noisy retrieval → the system retrieves the right page but not the right answer

*   **Chunks too small**→ each chunk loses context → the answer exists but can’t be understood in isolation

The goal: chunks small enough to retrieve precisely, but complete enough to give the LLM sufficient context for generation.

![Image 20](https://47billion.com/wp-content/uploads/2026/03/image-2.png)
**Strategy 1: Fixed-Size Chunking**

The simplest approach. Split every N tokens, with some overlap to avoid context loss at boundaries.

chunk_size= 512 tokens

chunk_overlap = 50 tokens

Easy to implement. Fast. The baseline every team starts with.

The problem:it’s document-agnostic. A sentence that starts at token 500 gets split at token 512, mid-thought. The next chunk has no idea what the previous one was discussing.

**Use when:**Homogeneous, unstructured text. FAQs. Simple corpora where you need something running quickly.

**Don’t use when:**Documents have natural structure — sections, headings, slides, tables.

**Strategy 2: Recursive Character Text Splitting**

The LangChain default. Instead of splitting blindly at N tokens, it tries to split at natural boundaries — paragraphs first, then sentences, then words — only falling back to character-level splits when necessary.

In Chroma’s benchmarks,RecursiveCharacterTextSplitter at 400-512 tokens delivered**85-90% recall**without the computational overhead of semantic methods.It’s a strong default for most teams.

**Use when:**Prose-heavy documents, articles, reports, general text corpora.

**Strategy 3: Semantic Chunking**

Instead of counting tokens, semantic chunking analyzes the embedding similarity between consecutive sentences. When similarity drops significantly — meaning the topic is shifting — it creates a new chunk boundary.

The result: chunks that respect topic boundaries, not arbitrary token counts. Each chunk contains one coherent idea.

The cost: requires embedding every sentence during preprocessing, which is computationally expensive. And it introduces a threshold parameter (how much similarity drop triggers a split?)that requires tuning per document type.

Benchmarks show up to**9% improvement in recall**over fixed-size chunking for well-structured documents.

**Use when:**Academic papers, long-form reports, content where topic coherence within chunks matters.

**Strategy 4: Hierarchical Chunking**

This is the approach that changes everything for structured documents.

The idea: documents have a natural hierarchy. A research paper has sections → subsections → paragraphs. A presentation has slides → sections → bullets. A legal document has articles → clauses → provisions.

Hierarchical chunking preserves this structure explicitly:

Parent Node: Full Section (context for generation)

Child Nodes: Individual Paragraphs (precision for retrieval)

At query time:

 1. Retrieve child chunk (precise match)

 2. Return parent chunk to LLM (full context)

This is sometimes called**Parent Document Retrieval**— retrieve small,generate with large.

The result: you get the retrieval precision of small chunks and the contextual completeness of large chunks. You don’t have to choose.

**Use when:**Presentations, reports with sections, legal documents, technical documentation, anything with meaningful structure. We cover this in depth in the case study below.

**Strategy 5: Page-Level Chunking**

In NVIDIA’s 2024 benchmark, this won —**0.648 accuracy**with the lowest variance across document types.

The reason: PDFs organize information by page deliberately. Financial reports put balance sheets on one page. Research papers put figures with their captions on the same page. Splitting across page boundaries destroys these relationships.

**Use when:**PDF-heavy corpora, financial reports, regulatory filings, academic papers.

**Don’t use when:**Your PDFs are just text exports with arbitrary page breaks — the page boundary carries no semantic meaning.

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

**Use when:**High-stakes, precision-critical applications. Legal Q&A, compliance checking, medical decision support. When incorrect retrieval has real consequences.

**Chunking Strategy Selection Guide**

**Document Type****Recommended Strategy****Why**
PDFs (structured)Page-level Respects visual organization
Research papers Semantic + Hierarchical Topic coherence + section context
Presentations / Slides**Hierarchical**Structure is the meaning
Legal documents Proposition-based Precision is non-negotiable
FAQs / Chat logs Sentence-level Self-contained questions
Code documentation Recursive (language-aware)AST-aware boundaries
Mixed / Unstructured Contextual Retrieval Adds context regardless of structure

**Two More Methods Worth Knowing**

**Contextual Retrieval**(Anthropic, 2024): Before embedding, prepend a generated context summary to each chunk — e.g., “This chunk is from Section 3 of the Q3 earnings report, discussing operating margins.” This anchors the chunk in its document context without changing the chunk boundaries. Particularly effective when combined with BM25 hybrid search.

**Cluster-Based / Agentic Chunking**: Uses optimization algorithms (or LLM agents) to find chunk boundaries that maximize a “semantic reward” — coherence within chunks, dissimilarity across chunks. Computationally expensive but produces the best boundaries for complex documents.

**Retrieval Strategies: Beyond Top-K**

Once your corpus is chunked and indexed, how you actually retrieve matters.

**Naive Top-K**

Return the K most similar chunks to the query embedding. Simple. Works for simple queries.

Fails when: the question requires synthesizing information from multiple sections, or when the K most similar chunks are all slight variations of the same passage (redundant retrieval).

**MMR — Maximal Marginal Relevance**

Returns diverse results rather than the K most similar. After selecting the top result, each subsequent result is chosen to maximize relevance _and_ minimize overlap with already-selected chunks.

The result: a retrieval set that covers different aspects of the answer, not five versions of the same paragraph.

**Use when:**Summarization tasks, broad questions, anytime redundancy is a concern.

**HyDE— Hypothetical Document Embeddings**

One of the most underrated techniques in advanced RAG.

The problem:there’s often a distribution gap between queries and documents. A user asks a question. Documents contain answers. Questions and answers are phrased very differently — and this mismatch degrades embedding similarity.

HyDE closes this gap:

1. Take the user’s query

2. Generate a hypothetical answer using the LLM (no retrieval yet)

3. Embed the hypothetical answer

4. Use that embedding to search the vector store

5. Retrieve real chunks closest to the hypothetical answer

6. Pass retrieved chunks + original query to LLM for final generation

The hypothetical answer is never shown to the user.It’s just a better search vector.

*   In benchmarks,HyDE improves retrieval performance significantly on knowledge-intensive tasks, especially when queries are short and vague while documents are detailed.

![Image 21](https://47billion.com/wp-content/uploads/2026/03/image-1.png)
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

**Use when:**Questions that span multiple entities, time periods, or concepts. Comparative analysis, multi-hop reasoning, research queries.

**Step-Back Prompting**

For narrow, specific queries, retrieval often misses the broader context. Step-Back prompting first abstracts the query — “What are the principles behind X?” —retrieves on the abstracted query, then uses both abstract context and specific query for generation.

Useful when questions are highly specific but require background understanding.

**Self-RAG**

The model itself decides whether to retrieve and what to retrieve. It generates a response, evaluates whether it needs external information, retrieves if necessary, and iterates. More agentic. More expensive. Significantly better at multi-hop reasoning.

**Evaluating RAG: What Actually Matters**

Here’s where most teams are completely flying blind.

Teams deploy RAG, try a few queries manually, and call it good. They have no metrics. They don’t know if their system is getting better or worse as they iterate.Evaluation should be part of broader **[LLM infrastructure best practices](https://47billion.com/blog/from-prompt-chaos-to-production-building-enterprise-grade-llm-infrastructure/)**, not something added after deployment.

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

**Layer****Metric****What It Measures**
Retrieval Precision@K What fraction of retrieved chunks are actually relevant?
Retrieval Recall@K What fraction of relevant chunks were retrieved?
Retrieval MRR Is the first relevant chunk ranked high?
Retrieval nDCG Is the overall ranking quality good?
Generation BERTScore Semantic similarity (better than BLEU for RAG)
Generation ROUGE Token-level overlap with reference
End-to-end Faithfulness Does the answer stick to retrieved context?
End-to-end Answer Relevancy Does the answer address the question?
End-to-end Context Precision Was the retrieved context actually useful?
End-to-end Context Recall Did we retrieve all the context needed?

**RAGAS: Automated RAG Evaluation**

RAGAS (Retrieval Augmented Generation Assessment) is the standard framework for automated RAG evaluation. Its key insight: you don’t need human-annotated ground truth for every metric. LLM-as-judge can evaluate faithfulness, relevance, and context quality at scale.

from ragas import evaluate

from ragas.metrics import faithfulness,answer_relevancy, context_precision

results = evaluate(

 dataset=test_dataset,

 metrics=[faithfulness,answer_relevancy,context_precision]

)

**Faithfulness**is the most critical metric. It measures whether every claim in the generated answer is grounded in the retrieved context. A faithfulness score below 0.8 means your LLM is hallucinating — even when retrieval is working.

**Answer Relevancy**measures whether the answer addresses the actual question. A system can be perfectly faithful (sticking to retrieved context) but still irrelevant if it retrieves the wrong content.

**Context Precision**tells you if your retrieval is returning noise alongside relevant chunks. High precision means everything retrieved is useful. Low precision means your reranking needs work.

Other evaluation tools:**DeepEval**(uses G-Eval with custom rubrics),**TruLens**(focuses on the “RAG triad” of groundedness, answer relevance, context relevance),**Arize Phoenix**(production monitoring and tracing).

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

A student asks:_“What technique should I use to answer behavioral interview questions?”_

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

Query matches the child node precisely. The LLM receives the parent node as context — so it knows _why_ STAR is being discussed,_where_ in the curriculum it appears, and _what_ it applies to.

The response is specific, contextually correct, and attributable.

**The Numbers**

Across our internal benchmark on 200 student queries over 15 university presentation decks:

**Chunking Strategy****Answer Accuracy****Faithfulness****Context Precision**
Fixed-size(512 tokens)61%0.74 0.58
Semantic chunking 72%0.81 0.69
**Hierarchical (parent-child)****89%****0.91****0.84**

The hierarchical approach didn’t just improve accuracy — it specifically improved the cases that matter most: questions that require understanding _where_ a piece of information sits in the document, not just _that_ it exists.

**The Broader Principle**

Any time your document’s structure carries meaning — presentations, legal contracts with numbered clauses, technical specs with sections and subsections, financial reports with organized statements — hierarchical chunking is not optional.It’s the only approach that respects what the document is actually saying.

![Image 22](https://47billion.com/wp-content/uploads/2026/03/image-4.png)
**The Full Production RAG Stack**

Here’s what a production-grade RAG system actually looks like, integrated end-to-end:

INGESTION PIPELINE

 ──────────────────

Raw Documents → Document Parser → Structure Detection

 → Chunking Strategy (per doc type) → Embedding Model

 → Vector Store + Keyword Index

 RETRIEVAL PIPELINE

 ──────────────────

User Query → Query Analysis → [HyDE/ Multi-Query]

 → Dense Retrieval + Sparse Retrieval → RRF Fusion

 →Reranker→ Top-K Chunks

 GENERATION PIPELINE

 ──────────────────

Top-K Chunks + Query → Context Assembly → LLM

 → Response → Citation Extraction

 EVALUATION LAYER

 ────────────────

RAGAS: Faithfulness / Answer Relevancy / Context Precision

Retrieval:Precision@K/Recall@K/ MRR

Production: Latency / Throughput / Cost per Query

![Image 23](https://47billion.com/wp-content/uploads/2026/03/image-5.png)
**Common RAG Anti-Patterns (And How to Avoid Them)**

After building and debugging RAG in production, these are the mistakes we see most often:

**Skipping retrieval evaluation.**Teams measure end-to-end accuracy but never separately measure whether retrieval is working. A system can fail because of bad chunking, bad embeddings, bad retrieval, or bad generation — and without layer-specific metrics,you’re debugging blindly.

**One chunking strategy for all document types.**A single 512-token splitter applied to PDFs, slides, legal docs, and code. Each document type has different structure. The right chunking strategy depends on what the document is, not just how long it is.

**No overlap in fixed-size chunks.**Information split at the boundary of two chunks exists in neither. At minimum, 10-15% overlap prevents this. Hierarchical chunking is the proper fix.

**Embedding model mismatch.**Using a general-purpose embedding model for highly specialized content (medical, legal, technical) without checking whether a domain-specific model performs better.

**Top-K without reranking.**Embedding similarity is a proxy for relevance, not relevance itself. A reranker as the second stage significantly improves final context quality with minimal latency cost.

**Measuring faithfulness without measuring retrieval.**An LLM that faithfully echoes retrieved content still gives wrong answers if retrieval returned the wrong chunks. Faithfulness and retrieval quality are independent — you need to measure both.

**Choosing the Right Approach for Your Use Case**

**Use Case****Chunking****Retrieval****Key Metric**
Enterprise document Q&A Hierarchical Hybrid +Rerank Faithfulness
Customer support Sentence-level Dense + MMR Answer Relevancy
Legal / Compliance Proposition-based Dense + BM25 Context Precision
Research assistance Semantic HyDE+Multi-Query Recall@K
Presentation / Slide AI**Hierarchical (mandatory)**Hybrid +Rerank Answer Accuracy
Code documentation Recursive (AST-aware)Dense Exact Match

**What We’ve Learned**

RAG is not a component you add —it’s a pipeline you architect. The decisions you make at ingestion time (how you chunk, how you embed)determine the ceiling of what’s possible at retrieval and generation time.For organizations building **[enterprise-grade AI solutions](https://47billion.com/machine-learning/)**, this means treating Retrieval-Augmented Generation as a full-stack system — from ingestion and retrieval to evaluation and monitoring.

The teams that build RAG that works in production are not the ones who picked the best vector database.They’re the ones who spent time understanding their documents, matched chunking strategy to document structure, measured retrieval quality independently, and iterated based on data.

The LLM at the end of the pipeline is only as good as what you give it. Give it the right context, and it will give you the right answer.

**How 47Billion Approaches RAG Engineering**

At 47Billion,we’ve built RAG pipelines across industries — EdTech, HR Tech, enterprise knowledge management — each with different document types, different query patterns, and different accuracy requirements.

Our approach is systematic: we assess document structure before choosing chunking strategy, we instrument retrieval and generation separately, and we benchmark against domain-specific baselines before production deployment.

**Capability****What We Deliver**
RAG Architecture Design Chunking strategy, embedding selection, vector store setup
Hybrid Retrieval Implementation Dense + sparse + reranking pipeline
Evaluation Framework RAGAS integration, custom metrics, monitoring dashboards
Domain Adaptation Fine-tuned embeddings, domain-specific chunking
Production Optimization Latency tuning, cost optimization, scaling

If your RAG system isn’t performing the way you expected — or you’re building one from scratch and want to get the architecture right from the start —[let’s talk.](https://47billion.com/Contact-us/)

_© 2025 47Billion. All rights reserved._

Share this on -

[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2F47billion.com%2Fblog%2Frag-system-in-production-why-it-fails-and-how-to-fix-it%2F "Facebook")[](https://twitter.com/intent/tweet?text=RAG%20System%20in%20Production%3A%20Why%20It%20Fails%20and%20How%20to%20Fix%20It&url=https%3A%2F%2F47billion.com%2Fblog%2Frag-system-in-production-why-it-fails-and-how-to-fix-it%2F "X")[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2F47billion.com%2Fblog%2Frag-system-in-production-why-it-fails-and-how-to-fix-it%2F "Linkedin")[](https://api.whatsapp.com/send?text=RAG%20System%20in%20Production%3A%20Why%20It%20Fails%20and%20How%20to%20Fix%20It%20https%3A%2F%2F47billion.com%2Fblog%2Frag-system-in-production-why-it-fails-and-how-to-fix-it%2F "Whatsapp")[](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/ "Email")

* * *

### You might also like:

[![Image 24: What Does an AI Development Engagement Actually Cost? A Transparent Breakdown ](https://47billion.com/wp-content/uploads/2026/04/what-is-takes-being-an-AI-native-organization-1-1024x536.png) ### What Does an AI Development Engagement Actually Cost? A Transparent Breakdown ![Image 25: Arrow](https://47billion.com/wp-content/uploads/2025/03/Frame.svg)](https://47billion.com/blog/what-does-an-ai-development-engagement-actually-cost-a-transparent-breakdown/)[![Image 26: Beyond Prompt-and-Pray: Building a Production-Grade AI Question Generation Pipeline ](https://47billion.com/wp-content/uploads/2026/04/LLMs-dotn-scale-at-its-own-1024x536.png) ### Beyond Prompt-and-Pray: Building a Production-Grade AI Question Generation Pipeline ![Image 27: Arrow](https://47billion.com/wp-content/uploads/2025/03/Frame.svg)](https://47billion.com/blog/beyond-prompt-and-pray-building-a-production-grade-ai-question-generation-pipeline/)[![Image 28: How to Choose an AI Development Company? 7 Questions That Actually Matter](https://47billion.com/wp-content/uploads/2026/04/Enterprise-AI-guide-1024x536.png) ### How to Choose an AI Development Company? 7 Questions That Actually Matter ![Image 29: Arrow](https://47billion.com/wp-content/uploads/2025/03/Frame.svg)](https://47billion.com/blog/how-to-choose-an-ai-development-company-7-questions-that-actually-matter/)

![Image 30: Group 289894](https://47billion.com/wp-content/uploads/2024/04/Group-289894-1.svg)

## Building human centered AI driven solutions

## California Indore Bengaluru

## Connect With Us

## [hello@47billion.com](mailto:hello@47billion.com%C2%A0)

## SERVICES

Menu

*   [AI/ML](https://47billion.com/machine-learning/)
*   [Data Analytics](https://47billion.com/big-data-analytics/)
*   [End-to-End Product Development](https://47billion.com/product-development/)
*   [User Experience & Design](https://47billion.com/user-experience-design/)
*   [US Staffing](https://47billion.com/us-staffing/)

## INDUSTRY

Menu

*   [Healthcare](https://47billion.com/healthcare-industry/)
*   [Financial Services](https://47billion.com/financial-services/)
*   [Sustainability](https://47billion.com/esg-solutions/)
*   [Education](https://47billion.com/education-industry/)

## RESOURCES

Menu

*   [About](https://47billion.com/about/)
*   [Blog](https://47billion.com/blog/)
*   [Press Release](https://47billion.com/press-release/)
*   [Careers](https://47billion.com/careers/)
*   [Infographic](https://47billion.com/infographic/)
*   [White Paper](https://47billion.com/white-paper/)

![Image 31: Group 289894](https://47billion.com/wp-content/uploads/2024/04/Group-289894-1.svg)

## Building human centred AI driven solutions

## California Indore Bengaluru

## Connect With Us

## [hello@47billion.com](mailto:hello@47billion.com%C2%A0)

## SERVICES

Menu

*   [AI/ML](https://47billion.com/machine-learning/)
*   [Data Analytics](https://47billion.com/big-data-analytics/)
*   [End-to-End Product Development](https://47billion.com/product-development/)
*   [User Experience & Design](https://47billion.com/user-experience-design/)
*   [US Staffing](https://47billion.com/us-staffing/)

## INDUSTRY

Menu

*   [Healthcare](https://47billion.com/healthcare-industry/)
*   [Financial Services](https://47billion.com/financial-services/)
*   [Sustainability](https://47billion.com/esg-solutions/)
*   [Education](https://47billion.com/education-industry/)

## RESOURCES

Menu

*   [About](https://47billion.com/about/)
*   [Blog](https://47billion.com/blog/)
*   [Press Release](https://47billion.com/press-release/)
*   [Careers](https://47billion.com/careers/)
*   [Infographic](https://47billion.com/infographic/)
*   [White Paper](https://47billion.com/white-paper/)

## © 2026 47Billion. All Rights Reserved.

## [Privacy Policy](https://47billion.com/privacy-policy/) | [Terms & Conditions](https://47billion.com/blog/rag-system-in-production-why-it-fails-and-how-to-fix-it/terms-conditions)

[![Image 32](https://47billion.com/wp-content/uploads/2024/04/behance.svg)](https://www.behance.net/47billion)

[![Image 33: linkedin](https://47billion.com/wp-content/uploads/2024/04/linkedin.svg)](https://www.linkedin.com/company/47billion/)

[![Image 34](https://47billion.com/wp-content/uploads/2024/04/x.svg)](https://x.com/47billion)

[![Image 35](https://47billion.com/wp-content/uploads/2024/04/instagram.svg)](https://www.instagram.com/47billion/)

[![Image 36](https://47billion.com/wp-content/uploads/2024/04/facebook.svg)](https://www.facebook.com/47Billion/)

[![Image 37](https://47billion.com/wp-content/uploads/2024/04/pinterest.svg)](https://www.pinterest.com/47billion/)

[![Image 38](https://47billion.com/wp-content/uploads/2024/04/dribble.svg)](https://dribbble.com/47billion)

[![Image 39: youtube](https://47billion.com/wp-content/uploads/2024/04/youtube.svg)](https://www.youtube.com/channel/UC7l2UTez5yO-ld2BXgoOTjQ)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="jina-scraped-2.md">
<details>
<summary>Lost in the Middle: How Language Models Use Long Contexts</summary>

Phase: [EXPLORATION]

**Source URL:** <https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf>

Title: lost-in-the-middle.arxiv2023.pdf

URL Source: https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf

Published Time: Tue, 09 Dec 2025 06:16:20 GMT

Number of Pages: 18

Markdown Content:
# Lost in the Middle: How Language Models Use Long Contexts 

Nelson F. Liu 1∗ Kevin Lin 2 John Hewitt 1 Ashwin Paranjape 3

Michele Bevilacqua 3 Fabio Petroni 3 Percy Liang 11Stanford University 2University of California, Berkeley 3Samaya AI 

nfliu@cs.stanford.edu 

Abstract 

While recent language models have the abil-ity to take long contexts as input, relatively little is known about how well they use 

longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their in-put contexts: multi-document question an-swering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant informa-tion, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when rele-vant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models. 

1 Introduction 

Language models have become an important and flexible building block in a variety of user-facing language technologies, including conversational interfaces, search and summarization, and collabo-rative writing (Shuster et al., 2022; Thoppilan et al., 2022; Lee et al., 2022, inter alia ). These models perform downstream tasks primarily via prompting: all relevant task specification and data to process is formatted as a textual input context, and the model returns a generated text completion. These input contexts can contain thousands of tokens, espe-cially when language models are used to process long documents (e.g., legal or scientific documents, conversation histories, etc.) or when language mod-els are augmented with external information (e.g.,     

> *Work partially completed as an intern at Samaya AI. 1st 5th 10th 15th 20th
> Position of Document with the Answer
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-0613 (closed-book)

Figure 1: Changing the location of relevant information (in this case, the position of the passage that answers an input question) within the language model’s input con-text results in a U-shaped performance curve—models are better at using relevant information that occurs at the very beginning (primacy bias) or end of its input context (recency bias), and performance degrades significantly when models must access and use information located in the middle of its input context. 

relevant documents from a search engine, database query results, etc; Petroni et al., 2020; Ram et al., 2023; Shi et al., 2023; Mallen et al., 2023; Schick et al., 2023, inter alia ). Handling these use-cases requires language mod-els to successfully operate over long sequences. Ex-isting language models are generally implemented with Transformers (Vaswani et al., 2017), which re-quire memory and compute that increases quadrat-ically in sequence length. As a result, Trans-former language models were often trained with relatively small context windows (between 512-2048 tokens). Recent improvements in hardware (e.g., faster GPUs with more memory) and algo-rithms (Dai et al., 2019; Dao et al., 2022; Poli et al., 2023; Rubin and Berant, 2023, inter alia ) have resulted in language models with larger context windows (e.g., 4096, 32K, and even 100K tokens), but it remains unclear how these extended-context language models make use of their input contexts when performing downstream tasks. We empirically investigate this question via controlled experiments with a variety of state-of-the-art open (MPT-30B-Instruct, LongChat-13B (16K)) and closed (OpenAI’s GPT-3.5-Turbo and Anthropic’s Claude-1.3) language models in set-tings that require accessing and using information within an input context. In particular, our experi-ments make controlled changes to the input context size and the position of the relevant information within the input context and study their effects on language model performance. If language models can robustly use information within long input con-texts, then their performance should be minimally affected by the position of the relevant information in the input context. We first experiment with multi-document ques-tion answering, which requires models to reason over provided documents to find relevant informa-tion and use it to answer a given question; this task mimics the retrieval-augmented generation setup underlying many commercial generative search and question answering applications (e.g., Bing Chat). In this setting, we control (i) the input context length by changing the number of documents in the input context (akin to retrieving more or less documents in retrieval-augmented generation), and (ii) control the position of the relevant information within the input context by changing the order of the documents to place the relevant document at the beginning, middle or end of the context. We find that changing the position of relevant information in the input context can substantially affect model performance, indicating that current language models do not robustly access and use information in long input contexts. Furthermore, we observe a distinctive U-shaped performance curve (Figure 1); language model performance is highest when relevant information occurs at the very beginning (primacy bias) or end of its in-put context (recency bias), and performance sig-nificantly degrades when models must access and use information in the middle of their input con-text (§2.3). For example, when relevant infor-mation is placed in the middle of its input con-text, GPT-3.5-Turbo’s performance on the multi-document question task is lower than its perfor-mance when predicting without any documents (i.e., the closed-book setting; 56.1%). Furthermore, we find that models often have identical performance to their extended-context counterparts, indicating that extended-context models are not necessarily better at using their input context (§2.3). Given that language models struggle to retrieve and use relevant information in the multi-document question answering task, to what extent can lan-guage models even retrieve from their input con-texts? We study this question with a synthetic key-value retrieval task, which is designed to be a mini-mal testbed for the basic ability to retrieve matching tokens from the input context. In this task, models are given a collection of JSON-formatted key-value pairs and must return the value associated with a specific key. Similar to the multi-document QA task, the key-value retrieval task admits controlled changes to the input context length (adding more key-value pairs) and the position of relevant in-formation. Although some models perform the synthetic key-value retrieval task perfectly, other models struggle to simply retrieve matching tokens that occur in the middle of their input context and continue to exhibit a U-shaped performance curve. To better understand why language models strug-gle to robustly access and use information in their input contexts, we study the role of model archi-tecture (decoder-only vs. encoder-decoder), query-aware contextualization, and instruction fine-tuning (§4). We find that: • Encoder-decoder models are relatively robust to changes in the position of relevant informa-tion within their input context, but only when evaluated on sequences within its training-time sequence length. When evaluated on sequences longer than those seen during train-ing, we observe a U-shaped performance curve (§4.1). • Query-aware contextualization (placing the query before and after the documents or key-value pairs) enables near-perfect performance on the synthetic key-value task, but minimally changes trends in multi-document QA (§4.2). • Even base language models (i.e., without in-struction fine-tuning) show a U-shaped per-formance curve as we vary the position of relevant information in the input context. Our results indicate that prompting language models with longer input contexts is a trade-off— providing the language model with more informa-tion may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing ac-curacy. To better understand this trade-off in prac-tice, we perform a case study with retriever-reader models on open-domain question answering (§5). In contrast to our controlled multi-document QA task, where the context always contains exactly 

one document that answers the question, none or many of the top k documents may contain the an-swer in the open-domain QA setting. When re-trieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model perfor-mance saturates long before retriever recall satu-rates, indicating that current models fail to effec-tively use additional retrieved documents—using 50 documents instead of 20 retrieved documents only marginally improves performance ( ∼1.5% for GPT-3.5-Turbo and ∼1% for claude-1.3). Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future long-context models; to claim that a language model can robustly use information within long input con-texts, it is necessary to show that its performance is minimally affected by the position of the rele-vant information in the input context (e.g., minimal difference in best- and worst-case performance). To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data. 1

2 Multi-Document Question Answering 

Our goal is to better understand how language mod-els use their input context. To this end, we analyze model performance on multi-document question answering, which requires models to find relevant information within an input context and use it to answer the question. In particular, we make con-trolled changes to the length of the input context and the position of the relevant information and measure changes in task performance. 

2.1 Experimental Setup 

In the multi-document question answering task, the model inputs are (i) a question to answer and (ii) k

documents (e.g., passages from Wikipedia), where 

exactly one of the documents contains the answer 

> 1nelsonliu.me/papers/lost-in-the-middle

to the question and k − 1 “distractor” documents do not. This task requires the model to access the document that contains the answer within its input context and use it to answer the question. Figure 2 presents an example. We instantiate this task with data from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019), which contains historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia. In particular, we take the 2655 queries where the annotated long answer is a paragraph (as opposed to a list or a table). We use passages (chunks of at most 100 tokens) from Wikipedia as documents within our input contexts. For each of the queries, we need a document that contains the answer and k − 1 distractor documents that do not contain the answer. To obtain a document that answers the question, we use the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations. To collect k − 1 distractor documents that do not contain the answer, we use a retrieval system (Con-triever, fine-tuned on MS-MARCO; Izacard et al., 2021) to retrieve the k − 1 Wikipedia chunks that are most relevant to the query and do not contain any of the NaturalQuestions-annotated answers. 2,3 

In the input context, the distractor documents are presented in order of decreasing relevance. 4

To modulate the position of relevant information within the input context, we adjust the order of the documents to change the position of the document that contains the answer (Figure 3). To modulate the input context length in this task, we increase or decrease the number of retrieved documents that do not contain the answer (Figure 4). Following Kandpal et al. (2022) and Mallen et al. (2023), we use accuracy as our primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output.    

> 2Ambiguity in NaturalQuestions-Open means that a small number of distractor passages may contain a reasonable an-swer. We additionally run experiments on subset of unam-biguous questions, finding similar results and conclusions; see Appendix A.
> 3We also explored using random documents as distractors, see Appendix B for more details.
> 4Since there might be a prior over “search results” appear-ing in ranked order, we explored randomly ordering the k−1
> distractor documents and mentioning that the documents are randomly ordered in the task description, but found the same trends. See Appendix C for more details.

Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant). Document [1](Title: Asian Americans in science and technology) Prize in physics for discovery of the subatomic particle J/ψ. Subrahmanyan Chandrasekhar shared... 

Document [2](Title: List of Nobel laureates in Physics) The first Nobel Prize in Physics was awarded in 1901 to Wilhelm Conrad Röntgen, of Germany, who received... 

Document [3](Title: Scientist) and pursued through a unique method, was essentially in place. Ramón y Cajal won the Nobel Prize in 1906 for his remarkable... Question: who got the first nobel prize in physics Answer: 

Input Context 

Wilhelm Conrad Röntgen 

Desired Answer Figure 2: Example of the multi-document question answering task, with an input context and the desired model answer. The document containing the answer is bolded within the input context here for clarity. Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant).           

> Document [1](Title: List of Nobel laureates in Physics) ...
> Document [2](Title: Asian Americans in science and technology) ... Document [3](Title: Scientist) ... Question: who got the first nobel prize in physics Answer:
> Input Context
> Wilhelm Conrad Röntgen
> Desired Answer

Figure 3: Modulating the position of relevant informa-tion within the input context for the multi-document question answering example presented in Figure 2. Re-ordering the documents in the input context does not affect the desired output. 

Our experimental setup is similar to the needle-in-a-haystack experiments of Ivgi et al. (2023), who compare question answering performance when the relevant paragraph is placed (i) at the beginning of the input or (ii) a random position within the in-put. They find that encoder-decoder models have significantly higher performance when relevant in-formation is placed at the start of the input context. In contrast, we study finer-grained changes in the position of relevant information. 

2.2 Models 

We analyze several state-of-the-art open and closed language models. We use greedy decoding when generating outputs and leave exploration of other decoding methods to future work. We use a stan-dard set of prompts for each model (Figure 2). Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant). Document [1](Title: Asian Americans in science and technology) ...                    

> Document [2](Title: List of Nobel laureates in Physics) ...
> Document [3](Title: Scientist) ... Document [4](Title: Norwegian Americans) ... Document [5](Title: Maria Goeppert Mayer) ... Question: who got the first nobel prize in physics Answer:
> Input Context Input Context
> Wilhelm Conrad Röntgen
> Desired Answer

Figure 4: Modulating the input context length of the multi-document question answering example presented in Figure 2. Adding documents that do not contain the answer increases the length of the input context, but does not affect the desired output. 

Open models. We experiment with MPT-30B-Instruct, which has a maximum context length of 8192 tokens. The model was initially pre-trained on 1 trillion tokens using 2048-token sequences, followed by an additional sequence length adapta-tion pre-training phase on 50 billion tokens using 8192-token sequences. MPT-30B-Instruct uses AL-iBi (Press et al., 2022) to represent positional infor-mation. We also evaluate LongChat-13B (16K) (Li et al., 2023), which extends the LLaMA-13B (Tou-vron et al., 2023a) context window from 2048 to 16384 tokens by using condensed rotary positional embeddings before fine-tuning with 16384-token sequences. 

Closed models. We use the OpenAI API to ex-periment with GPT-3.5-Turbo and GPT-3.5-Turbo 1st 5th 10th                

> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 10 Total Retrieved Documents (~2K tokens)
> 1st 5th 10th 15th 20th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> 1st 5th 10th 15th 20th 25th 30th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 30 Total Retrieved Documents (~6K tokens)
> claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k

Figure 5: The effect of changing the position of relevant information (document containing the answer) on multi-document question answering performance. Lower positions are closer to the start of the input context. Performance is highest when relevant information occurs at the very start or end of the context, and rapidly degrades when models must reason over information in the middle of their input context. 

(16K). 5 GPT-3.5-Turbo has a maximum context length of 4K tokens, and GPT-3.5-Turbo (16K) is a version with an extended maximum context length of 16K tokens. We evaluate Claude-1.3 and Claude-1.3 (100K) with the Anthropic API; Claude-1.3 has a maximum context length of 8K tokens, and Claude-1.3 (100K) has an extended context length of 100K tokens. 6

2.3 Results and Discussion 

We experiment with input contexts containing 10, 20, and 30 total documents. Figure 5 presents multi-document question answering performance when varying the position of relevant information within the input context. To contextualize model perfor-mance, we also evaluate on the closed-book and oracle settings (Table 1). In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer. On the other hand, in the oracle setting, language models are given the single document that contains the answer and must use it to answer the question. 

Model performance is highest when relevant in-formation occurs at the beginning or end of its input context. As illustrated in Figure 5, chang-ing the position of relevant information in the in-put context leads to substantial decreases in model performance. In particular, we see a distinctive U-

> 5

We use the 0613 OpenAI model versions. 

> 6

We also evaluate GPT-4 (8K) on a subset of multi-document QA experiments, finding similar results and trends as other models (though GPT-4 has higher absolute perfor-mance). Evaluating GPT-4 on the full multi-document QA and key-value retrieval experiments would cost upwards of $6000. See Appendix D for GPT-4 results and discussion. Model Closed-Book Oracle LongChat-13B (16K) 35.0% 83.4% MPT-30B-Instruct 31.5% 81.9% GPT-3.5-Turbo 56.1% 88.3% GPT-3.5-Turbo (16K) 56.0% 88.6% Claude-1.3 48.3% 76.1% Claude-1.3 (100K) 48.2% 76.4% 

Table 1: Closed-book and oracle accuracy of language models on the multi-document question answering task. 

shaped performance curve—models are often much better at using relevant information that occurs at the very beginning (primacy bias) and very end of contexts (recency bias), and suffer degraded perfor-mance when forced to use information within the middle of its input context. For example, GPT-3.5-Turbo’s multi-document QA performance can drop by more than 20%—in the worst case, performance in 20- and 30-document settings is lower than per-formance without any input documents (i.e., closed-book performance; 56.1%). These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks. 

Extended-context models are not necessarily better at using input context. When the input context fits in the context window of both a model and its extended-context counterpart, we see that performance between them is nearly identical. For example, the 10- and 20-document settings both fit in the context window of GPT-3.5-Turbo and GPT-3.5-Turbo (16K), and we observe that their performance as a function of position of relative information is nearly superimposed (solid purple and dashed brown series in Figure 5). These results Extract the value corresponding to the specified key in the JSON object below. JSON data: {"2a8d601d-1d69-4e64-9f90-8ad825a74195": "bb3ba2a5-7de8-434b-a86e-a88bb9fa7289", "a54e2eed-e625-4570-9f74-3624e77d6684": "d1ff29be-4e2a-4208-a182-0cea716be3d4", "9f4a92b9-5f69-4725-ba1e-403f08dea695 ": "703a7ce5-f17f-4e6d-b895-5836ba5ec71c", "52a9c80c-da51-4fc9-bf70-4a4901bc2ac3": "b2f8ea3d-4b1b-49e0-a141-b9823991ebeb", "f4eb1c53-af0a-4dc4-a3a5-c2d50851a178": "d733b0d2-6af3-44e1-8592-e5637fdb76fb"} Key: "9f4a92b9-5f69-4725-ba1e-403f08dea695 "Corresponding value: 

> Input Context
> 703a7ce5-f17f-4e6d-b895-5836ba5ec71c
> Desired Output

Figure 6: Example of the key-value retrieval task, with an input context and the desired model output. Given a key, the goal is to return the associated value. All keys and values are 128-bit UUIDs. The relevant key-value pair for answering the query is bolded here within the input context for clarity. 

indicate that extended-context models are not nec-essarily better than their non-extended counterparts at using their input context. 

3 How Well Can Language Models Retrieve From Input Contexts? 

Given that language models struggle to retrieve and use information from the middle of their input contexts in the multi-document question answering task, to what extent can they simply retrieve from input contexts? We study this question with a syn-thetic key-value retrieval task, which is designed to provide a minimal testbed for the basic ability to retrieve matching tokens from an input context. 

3.1 Experimental Setup 

In our synthetic key-value retrieval task, the inputs are (i) a string-serialized JSON object with k key-value pairs, where each of the keys and values are unique, randomly-generated UUIDs and (ii) a key within the aforementioned JSON object. The goal is to return the value associated with the specified key. Thus, each JSON object contains one relevant key-value pair (where the value is to be returned), and k − 1 irrelevant “distractor” key-value pairs. Figure 6 provides an example input context and its corresponding desired output. We again measure accuracy by evaluating whether the correct value appears in the predicted output. Our synthetic key-value retrieval task shares sim-ilar goals with the Little Retrieval Test of Papail-iopoulos et al. (2023) and the fine-grained line re-trieval task of Li et al. (2023), but we explicitly seek to distill and simplify the task by removing as much natural language semantics as possible (using random UUIDs instead), since language features may present potential confounders. For example, Transformer language models may have varying sensitivity to different linguistic features in their input (O’Connor and Andreas, 2021). To modulate the position of relevant information within the input context, we change the position of the key to retrieve within the serialized JSON object. To modulate the input context length, we change the number of input JSON key-value pairs 

k by adding or removing random keys, changing the number of distractor key-value pairs. 

3.2 Results and Discussion 

We experiment with input contexts containing 75, 140, and 300 key-value pairs (500 examples each). We use the same set of models as the multi-document question answering experiments, see §2.2 for more details. Figure 7 presents key-value retrieval perfor-mance. Claude-1.3 and Claude-1.3 (100K) do nearly perfectly on all evaluated input context lengths, but other models struggle, especially when contexts have 140 or 300 key-value pairs— although the synthetic key-value retrieval task only requires identifying exact match within the input context, not all models achieve high performance. Similar to our multi-document QA results, GPT-3.5-Turbo, GPT-3.5-Turbo (16K), and MPT-30B-Instruct have the lowest performance when they must access key-value pairs in the middle of their input context. LongChat-13B (16K) exhibits a dif-ferent trend in the 140 key-value setting; we quali-tatively observe that when relevant information is 1st 25th 50th 75th                

> Position of Key to Retrieve
> 40
> 50
> 60
> 70
> 80
> 90
> 100
> Accuracy
> 75 Key-Value Pairs (~4K tokens)
> 1st 35th 70th 105th 140th
> Position of Key to Retrieve
> 40
> 50
> 60
> 70
> 80
> 90
> 100
> Accuracy
> 140 Key-Value Pairs (~8K tokens)
> 1st 50th 100th 150th 200th 250th 300th
> Position of Key to Retrieve
> 40
> 50
> 60
> 70
> 80
> 90
> 100
> Accuracy
> 300 Key-Value Pairs (~16K tokens)
> claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k

Figure 7: The effect of changing the input context length and the position of relevant information on key-value retrieval performance. Lower positions are closer to the start of the input context. Although some models show perfect accuracy on this synthetic task (e.g., Claude-1.3 and Claude-1.3 (100K)), we see again that performance is often highest when relevant information is occurs at the very start or end of the context, and rapidly degrades when models must retrieve from the middle of the input context. 

placed at the start of the input context, LongChat-13B (16K) tends to generate code to retrieve the key, rather than outputting the value directly. 

4 Why Are Language Models Not Robust to Changes in the Position of Relevant Information? 

Our multi-document question answering and key-value retrieval results show that language models struggle to robustly access and use information in long input contexts, since performance degrades significantly when changing the position of rele-vant information. To better understand why, we per-form some preliminary investigations into the role of model architecture (decoder-only vs. encoder-decoder), query-aware contextualization, and in-struction fine-tuning. 

4.1 Effect of Model Architecture 

The open models we evaluated are all decoder-only models—at each timestep, they may only attend to prior tokens. To better understand the poten-tial effects of model architecture on how language model use context, we compare decoder-only and encoder-decoder language models. We experiment with Flan-T5-XXL (Raffel et al., 2020; Chung et al., 2022) and Flan-UL2 (Tay et al., 2023). Flan-T5-XXL is trained with a sequences of 512 tokens (encoder and decoder). Flan-UL2 is initially trained with sequences of 512 tokens (en-coder and decoder), but is then pre-trained for an extra 100K steps with 1024 tokens (encoder and de-coder) before instruction fine-tuning on sequences with 2048 tokens in the encoder and 512 tokens in the decoder. However, since these models use relative positional embeddings, they can (in prin-ciple) extrapolate beyond these maximum context lengths; Shaham et al. (2023) find that both mod-els can perform well with sequences of up to 8K tokens. Figure 8 compares the performance of decoder-only and encoder-decoder models. When Flan-UL2 is evaluated on sequences within its 2048-token training-time context window (Figure 8; left sub-plot), its performance is relatively robust to changes in the position of relevant information within the input context (1.9% absolute difference between best- and worst-case performance). When evalu-ated on settings with sequences longer than 2048 tokens (Figure 8; center and right), Flan-UL2 per-formance begins to degrade when relevant informa-tion is placed in the middle. Flan-T5-XXL shows a similar trend, where longer input contexts result in a greater performance degradation when placing relevant information in the middle of the input con-text. We hypothesize that encoder-decoder models may make better use of their context windows be-cause their bidirectional encoder allows processing each document in the context of future documents, potentially improving relative importance estima-tion between documents. 

4.2 Effect of Query-Aware Contextualization 

Our multi-document QA and key-value retrieval experiments place the query (i.e., question to an-swer or key to retrieve) after the data to process (i.e., the documents or the key-value pairs). As a result, decoder-only models cannot attend to query tokens when contextualizing documents or key-value pairs, since the query only appears at the end 1st 5th 10th              

> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> Accuracy
> 10 Total Retrieved Documents (~2K tokens)
> 1st 5th 10th 15th 20th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> 1st 5th 10th 15th 20th 25th 30th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> Accuracy
> 30 Total Retrieved Documents (~6K tokens)
> mpt-30b-instruct longchat-13b-16k flan-t5-xxl flan-ul2

Figure 8: When encoder-decoder models (Flan-UL2 and Flan-T5-XXL) evaluated on sequences that are shorter 

than their encoder’s training-time maximum sequence length (2048 and 512 tokens, respectively), they are relatively robust to changes in the position of relevant information within their input context (left subplot). In contrast, when these models are evaluated on sequences longer than those seen during training (center and right subplots), we observe a U-shaped performance curve—performance is higher when relevant information occurs at the beginning or end of the input context, as opposed to the middle of the input context. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 50
> 60
> 70
> 80
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, query-aware contextualization)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 9: Query-aware contextualization (placing the query before and after the documents) does not sub-stantially improve robustness of language models to changing the position of relevant information in multi-document QA; performance slightly increases when relevant information occurs at the very beginning, but otherwise slightly decreases. 

of the prompt and decoder-only models can only attend to prior tokens at each timestep. In contrast, encoder-decoder models (which seem more robust to changes in the position of relevant information; §4.1) use a bidirectional encoder to contextualize input contexts—can we use this observation to im-prove decoder-only models by placing the query be-fore and after the data, enabling query-aware con-textualization of documents (or key-value pairs)? We find that query-aware contextualization dra-matically improves performance on the key-value retrieval task—all models achieve near-perfect per-formance on the 75, 140, and 300 key-value pair settings. For example, GPT-3.5-Turbo (16K) with query-aware contextualization achieves perfect per-formance when evaluated with 300 key-value pairs. In contrast, without query-aware contextualiza-tion, the worst-case performance is 45.6% (Fig-ure 7). Despite the significant impact on key-value retrieval performance, query-aware contextu-alization minimally affects performance trends in the multi-document question answering task (Fig-ure 9); it slightly improves performance when the relevant information is located at the very begin-ning of the input context, but slightly decreases performance in other settings. 

4.3 Effect of Instruction Fine-Tuning 

The models we evaluated are all instruction fine-tuned—after their initial pre-training, they undergo supervised fine-tuning on a dataset of instructions and responses. The task specification and/or in-struction is commonly placed at the beginning of the input context in supervised instruction fine-tuning data, which might lead instruction fine-tuned language models to place more weight on the start of the input context. To better understand the potential effects of instruction fine-tuning on how language models use long input contexts, we compare the multi-document question answering performance of MPT-30B-Instruct against its base model (i.e., before instruction fine-tuning) MPT-30B. We use the same experimental setup as §2. Figure 10 compares the multi-document QA performance of MPT-30B and MPT-30B-Instruct as a function of the position of the relevant in-1st 5th 10th 15th 20th  

> Position of Document with the Answer
> 44
> 46
> 48
> 50
> 52
> 54
> 56
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> mpt-30b mpt-30b-instruct Figure 10: Multi-document QA performance of MPT-30B-Instruct compared against its base model (i.e., be-fore instruction fine-tuning) MPT-30B. Both models have a U-shaped performance curve, where performance is much higher when relevant information occurs at the start or end of the input context, indicating that the instruction fine-tuning process itself is not necessarily responsible for these performance trends.

formation in the input context. Surprisingly, we see that both MPT-30B and MPT-30B-Instruct ex-hibit a U-shaped performance curve, where perfor-mance is highest when relevant information occurs at the very beginning or very end of the context. Although the absolute performance of MPT-30B-Instruct is uniformly higher than that of MPT-30B, their overall performance trends are similar. We also observe that instruction fine-tuning slightly re-duces the worst-case performance disparity from nearly 10% between the base model best- and worst-case performance to around 4%. These observations complement prior work, which found that non-instruction fine-tuned lan-guage models are biased towards recent tokens (i.e., the end of the input context; Khandelwal et al., 2018; Press et al., 2021). This recency bias has been observed in past work when evaluating mod-els on next-word prediction of contiguous text, a setting where language models minimally benefit from long-range information (Sun et al., 2021). In contrast, our results show that language models are capable of using longer-range information (i.e., the beginning of the input context) when prompted with instruction-formatted data. We hypothesize that non-instruction fine-tuned language models learn to use these long contexts from similarly-formatted data that may occur in Internet text seen during pre-training, e.g., StackOverflow questions and answers. To better understand the effect of additional fine-tuning and model scale, we also experimented with Llama-2 models of varying sizes (7B, 13B, and 70B) with and without additional supervised fine-tuning and reinforcement learning from hu-man feedback (Appendix E). We find that the U-shaped performance curve only appears in suffi-ciently large language models (with or without ad-ditional fine-tuning)—the 7B Llama-2 models are solely recency biased, while the 13B and 70B mod-els exhibit a U-shaped performance curve. In addi-tion, we see that the Llama-2 supervised fine-tuning and reinforcement learning from human feedback procedure slightly mitigates the positional bias in smaller models (13B, akin to trends shown when comparing MPT-30B and MPT-30B-Instruct), but minimally affects trends on larger models (70B). 

5 Is More Context Is Always Better? A Case Study With Open-Domain QA 

Our results indicate that prompting language mod-els with longer input contexts is a trade-off— providing the language model with more informa-tion may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. Even if a language model can take in 16K tokens, is it actually beneficial to provide 16K tokens of context? The answer to this question is ultimately downstream task-specific since it de-pends on the marginal value of the added context and the model’s ability to effectively use long input contexts, but we perform a case study with open-domain question answering on NaturalQuestions-Open to better understand this trade-off in existing language models. We use language models in a standard retriever-reader setup. A retrieval system (Contriever, fine-tuned on MS-MARCO) takes an input query from NaturalQuestions-Open and returns the k docu-ments from Wikipedia with the highest relevance score. To condition language models on these re-trieved documents, we simply include them in the prompt. We evaluate retriever recall and reader accuracy (whether any of the annotated answers appear in the predicted output) as a function of the number of retrieved documents k. We use a subset of NaturalQuestions-Open where the long answer is a paragraph (as opposed to a table or a list). Figure 11 presents retriever recall and open-5 10 20 30 40 50 

> Number of Retrieved Docs
> 50
> 60
> 70
> 80
> 90
> Metric
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k
> contriever recall

Figure 11: Retriever recall and model performance as a function of the number of retrieved documents. Model performance saturates long before retriever recall, indi-cating that the models have difficulty making use of the extra retrieved documents. 

domain QA results. We see that reader model performance saturates long before retriever per-formance saturates, indicating that readers are not effectively using the extra context. Using more than 20 retrieved documents only marginally im-proves reader performance ( ∼1.5% for GPT-3.5-Turbo and ∼1% for Claude-1.3), while significantly increasing the input context length (and thus la-tency and cost). These results, coupled with the observation that models are often better at retriev-ing and using information at the start or end of the input contexts, suggest that effective rerank-ing of retrieved documents (pushing relevant infor-mation closer to the start of the input context) or ranked list truncation (retrieving fewer documents when appropriate; Arampatzis et al., 2009) may be promising directions for improving how language-model-based readers use retrieved context. 

6 Related Work 

6.1 Long-Context Language Models 

There is much prior work in designing performant language models with cheaper scaling than Trans-formers in the context length. Many lines of work pursue Transformer variants with attention modi-fications like recurrence (Dai et al., 2019), factor-izing attention into computationally less intensive approximations (Beltagy et al., 2020; Zaheer et al., 2020), or low-rank approximations (Wang et al., 2020; Peng et al., 2021). Dao et al. (2022) in-stead provide a faster exact attention by a carefully-crafted IO-aware CUDA kernel. Separately, there are attempts to do away with attention entirely to remove quadratic sequence length complexity, of-ten through convolution and/or linear RNNs, e.g., in RWKV (Peng, 2023), S4 (Gu et al., 2022), or Hyena (Poli et al., 2023). Many prior efforts evalu-ate perplexity on a diverse web corpus as a proxy for the ability to process long contexts; this work shows that precise knowledge access on long con-texts may be an added challenge. 

6.2 How Do Language Models Use Context? 

The pioneering work of Khandelwal et al. (2018) showed that small LSTM language models make increasingly coarse use of longer-term context; Sankar et al. (2019) found similar results in di-alogue models. In a similar vein, Daniluk et al. (2017) find that attentive LSTM language mod-els tend to mainly use recent history. Petroni et al. (2020) were among the first to demonstrate the potential of combining context from an in-formation retrieval system with a pretrained lan-guage models for unsupervised question answering. O’Connor and Andreas (2021) found that many information-destroying operations had marginal ef-fects on Transformer LMs’ predictions. Krishna et al. (2022) found that long-context neural gen-eration in modestly-sized Transformer language models degenerates because models fail to prop-erly condition on long context. Finally, studying long-context models, Sun et al. (2021) found that longer contexts improves prediction of only a few tokens, an empirical finding consistent with the theory of Sharan et al. (2018), who showed that sequence distributions with bounded mutual infor-mation necessarily lead to marginal average predic-tion benefits from increasingly long context. Qin et al. (2023) analyze how efficient Transformers perform on a variety of long-context downstream NLP tasks, finding that long-context transformers are recency-biased and do not effectively use long-range context. 

6.3 The Serial-Position Effect 

The U-shaped curve we observe in this work has a connection in psychology known as the serial-position effect (Ebbinghaus, 1913; Murdock Jr, 1962), that states that in free-association recall of elements from a list, humans tend to best re-member the first and last elements of the list. The serial-position effect plays a role in understanding how humans develop short- and long-term mem-ory. Observing a serial-position-like effect in lan-guage models is perhaps surprising, since the self-attention mechanisms underlying Transformer lan-guage models is technically equally capable of re-trieving any token from their contexts. 

7 Conclusion 

We empirically study how language models use long input contexts via a series of controlled ex-periments. We show that language model perfor-mance degrades significantly when changing the position of relevant information, indicating that models struggle to robustly access and use infor-mation in long input contexts. In particular, per-formance is often lowest when models must use information in the middle of long input contexts. We conduct a preliminary investigation of the role of (i) model architecture, (ii) query-aware contextu-alization, and (iii) instruction fine-tuning to better understand how they affect how language models use context. Finally, we conclude with a practi-cal case study of open-domain question answering, finding that the performance of language model readers saturates far before retriever recall. Our results and analysis provide a better understanding of how language models use their input context and provides new evaluation protocols for future long-context models. 

Acknowledgments 

We would like to thank Luke Zettlemoyer, who served as our TACL action editor, and the the anonymous reviewers for their comments and feed-back. We also thank Claudiu Leoveanu-Condrei, Megan Leszczynski, Dmytro Okhonko, Maithra Raghu, Eric Wallace and Sang Michael Xie for feedback and discussions that helped improve this work. Further, we are grateful to Sewon Min for her help with the AmbigQA dataset. This work was supported by the Stanford Center for Research on Foundation Models (CRFM), by OpenAI via an API credits grant to the Stanford CRFM, and by Anthropic via the Claude academic access pro-gram. 

References 

Avi Arampatzis, Jaap Kamps, and Stephen Robert-son. 2009. Where to stop reading a ranked list? threshold optimization using truncated score dis-tributions. In Proc. of SIGIR .Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020. Longformer: The long-document trans-former. ArXiv:2004.05150. Hyung Won Chung, Le Hou, Shayne Longpre, Bar-ret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling instruction-finetuned language models. ArXiv:2210.11416. Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-XL: Attentive language mod-els beyond a fixed-length context. In Proc. of ACL .Michał Daniluk, Tim Rocktäschel, Johannes Welbl, and Sebastian Riedel. 2017. Frustratingly short attention spans in neural language modeling. In 

Proc. of ICLR .Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. 2022. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. ArXiv:2205.14135. Hermann Ebbinghaus. 1913. Memory: A contribu-tion to experimental psychology. H. A. Ruger & C. E. Bussenius, Trans. 

Albert Gu, Karan Goel, and Christopher Ré. 2022. Efficiently modeling long sequences with struc-tured state spaces. In Proc. of ICLR .Maor Ivgi, Uri Shaham, and Jonathan Berant. 2023. Efficient long-text understanding with short-text models. Transactions of the Association for Computational Linguistics , 11:284–299. Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. 2021. Unsupervised dense information retrieval with contrastive learning. ArXiv:2112.09118. Gautier Izacard and Edouard Grave. 2021. Lever-aging passage retrieval with generative models for open domain question answering. In Proc. of EACL .Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, and Colin Raffel. 2022. Large lan-guage models struggle to learn long-tail knowl-edge. ArXiv:2211.08411. Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. In 

Proc. of ACL .Kalpesh Krishna, Yapei Chang, John Wieting, and Mohit Iyyer. 2022. RankGen: Improving text generation with large ranking models. In Proc. of EMNLP .Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, An-drew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natural Questions: A bench-mark for question answering research. Trans-actions of the Association for Computational Linguistics , 7:452–466. Kenton Lee, Ming-Wei Chang, and Kristina Toutanova. 2019. Latent retrieval for weakly supervised open domain question answering. In 

Proc. of ACL .Mina Lee, Percy Liang, and Qian Yang. 2022. CoAuthor: Designing a human-AI collaborative writing dataset for exploring language model ca-pabilities. In Proc. of CHI .Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, , and Hao Zhang. 2023. How long can open-source LLMs truly promise on context length? Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, and Hannaneh Hajishirzi. 2023. When not to trust language models: In-vestigating effectiveness of parametric and non-parametric memories. In Proc. of ACL .Sewon Min, Julian Michael, Hannaneh Hajishirzi, and Luke Zettlemoyer. 2020. AmbigQA: An-swering ambiguous open-domain questions. In 

Proc. of EMNLP .Bennet B. Murdock Jr. 1962. The serial position effect of free recall. Journal of experimental psychology , 64(5):482. Joe O’Connor and Jacob Andreas. 2021. What con-text features can Transformer language models use? In Proc. of ACL .Dimitris Papailiopoulos, Kangwook Lee, and Jy-yong Sohn. 2023. A little retrieval test for large language models. https://github.com/ anadim/the-little-retrieval-test .Bo Peng. 2023. RWKV-LM. https://github. com/BlinkDL/RWKV-LM .Hao Peng, Nikolaos Pappas, Dani Yogatama, Roy Schwartz, Noah Smith, and Lingpeng Kong. 2021. Random feature attention. In Proc. of ICLR .Fabio Petroni, Patrick Lewis, Aleksandra Piktus, Tim Rocktäschel, Yuxiang Wu, Alexander H Miller, and Sebastian Riedel. 2020. How context affects language models’ factual predictions. In 

Proc. of AKBC .Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Ré. 2023. Hyena hierarchy: Towards larger con-volutional language models. In Proc. of ICML .Ofir Press, Noah A. Smith, and Mike Lewis. 2021. Shortformer: Better language modeling using shorter inputs. In Proc. of ACL .Ofir Press, Noah A. Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear bi-ases enables input length extrapolation. In Proc. of ICLR .Guanghui Qin, Yukun Feng, and Benjamin Van Durme. 2023. The NLP task effectiveness of long-range transformers. In Proc. of EACL .Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Ex-ploring the limits of transfer learning with a uni-fied text-to-text Transformer. Journal of Ma-chine Learning Research , 21(140):1–67. Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. 2023. In-context retrieval-augmented language models. ArXiv:2302.00083. Ohad Rubin and Jonathan Berant. 2023. Long-range language modeling with self-retrieval. ArXiv:2306.13421. Chinnadhurai Sankar, Sandeep Subramanian, Chris Pal, Sarath Chandar, and Yoshua Bengio. 2019. Do neural dialog systems use the conversation history effectively? an empirical study. In Proc. of ACL .Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettle-moyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer: Language models can teach themselves to use tools. Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Be-rant, and Omer Levy. 2023. ZeroSCROLLS: A zero-shot benchmark for long text understanding. ArXiv:2305.14196. Vatsal Sharan, Sham Kakade, Percy Liang, and Gregory Valiant. 2018. Prediction with a short memory. In Proc. of STOC .Weijia Shi, Sewon Min, Michihiro Yasunaga, Min-joon Seo, Rich James, Mike Lewis, Luke Zettle-moyer, and Wen tau Yih. 2023. REPLUG: Retrieval-augmented black-box language mod-els. ArXiv:2301.12652. Kurt Shuster, Jing Xu, Mojtaba Komeili, Da Ju, Eric Michael Smith, Stephen Roller, Megan Ung, Moya Chen, Kushal Arora, Joshua Lane, Morteza Behrooz, William Ngan, Spencer Poff, Naman Goyal, Arthur Szlam, Y-Lan Boureau, Melanie Kambadur, and Jason Weston. 2022. BlenderBot 3: a deployed conversational agent that continually learns to responsibly engage. ArXiv:2208.03188. Simeng Sun, Kalpesh Krishna, Andrew Mattarella-Micke, and Mohit Iyyer. 2021. Do long-range language models actually use long-range con-text? In Proc. of EMNLP .Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Jason Wei, Xuezhi Wang, Hyung Won Chung, Siamak Shakeri, Dara Bahri, Tal Schuster, Huaixiu Steven Zheng, Denny Zhou, Neil Houlsby, and Donald Metzler. 2023. UL2: Unifying language learning paradigms. ArXiv:2205.05131. Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, YaGuang Li, Hongrae Lee, Huaixiu Steven Zheng, Amin Ghafouri, Marcelo Menegali, Yanping Huang, Maxim Krikun, Dmitry Lepikhin, James Qin, Dehao Chen, Yuanzhong Xu, Zhifeng Chen, Adam Roberts, Maarten Bosma, Vincent Zhao, Yanqi Zhou, Chung-Ching Chang, Igor Krivokon, Will Rusch, Marc Pickett, Pranesh Srinivasan, Laichee Man, Kathleen Meier-Hellstern, Meredith Ringel Mor-ris, Tulsee Doshi, Renelito Delos Santos, Toju Duke, Johnny Soraker, Ben Zevenbergen, Vin-odkumar Prabhakaran, Mark Diaz, Ben Hutchin-son, Kristen Olson, Alejandra Molina, Erin Hoffman-John, Josh Lee, Lora Aroyo, Ravi Rajakumar, Alena Butryna, Matthew Lamm, Viktoriya Kuzmina, Joe Fenton, Aaron Cohen, Rachel Bernstein, Ray Kurzweil, Blaise Aguera-Arcas, Claire Cui, Marian Croak, Ed Chi, and Quoc Le. 2022. LaMDA: Language models for dialog applications. ArXiv:2201.08239. Hugo Touvron, Thibaut Lavril, Gautier Izac-ard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023a. LLaMA: Open and efficient foundation language models. ArXiv:2302.13971. Hugo Touvron, Louis Martin, Kevin Stone, Pe-ter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernan-des, Jeremy Fu, Wenyin Fu, Brian Fuller, Cyn-thia Gao, Vedanuj Goswami, Naman Goyal, An-thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Ko-renev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, An-gela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023b. Llama 2: Open foundation and fine-tuned chat models. ArXiv:2307.09288. Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. At-tention is all you need. In Proc. of NeurIPS .Sinong Wang, Belinda Z. Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Lin-former: Self-attention with linear complexity. ArXiv:2006.04768. Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. 2020. Big Bird: Transformers for longer sequences. In 

Proc. of NeurIPS .

A Ambiguity in Multi-Document QA Distractor Documents 

Following past work on NaturalQuestions-Open (Izacard et al., 2021; Izacard and Grave, 2021, inter alia ), we use a Wikipedia dump from late 2018 as our retrieval corpus. However, this standard Wikipedia dump has a small amount of temporal mismatch with the NaturalQuestions annotations. For example, consider the question “what nfl team does robert griffin iii play for”. The Natu-ralQuestions annotated answer is “currently a free agent”. However, the Wikipedia retrieval corpus contains the information that he plays for the “Balti-more Ravens”, since he was released from the team between the Wikipedia dump’s timestamp and the NaturalQuestions annotation process. We use the ambiguity annotations of Min et al. (2020) to create a subset unambiguous questions. Experiments on this unambiguous subset of the data show similar results and conclusions as the experiments on the full questions collection (Fig-ure 12). 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, unambiguous questions)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 12: Language model performance on a unam-biguous subset of questions. 

B Random Distractors in Multi-Document QA 

We also run multi-document question answering experiments with random Wikipedia documents as distractors, which allows us to ablate the impact of retrieved distractors (hard negatives). Note that in this setting, the the document containing the an-swer can often be identified with simple heuristics (e.g., lexical overlap with the query). Figure 13 presents the results of this experiment. Although all models have higher absolute accuracy in this setting, they surprisingly still struggle to reason over their entire input context, indicating that their performance degradation is not solely due to an inability to identify relevant documents. 

C Randomizing Distractor Order in Multi-Document QA 

Our prompt instructs the language model to use the provided search results to answer the question. There may be a prior in the pre-training or instruc-tion fine-tuning data to treat search results as sorted by decreasing relevance (i.e., the documents near the beginning of the input context are more likely to be useful than those at the end). To validate that our conclusions are not simply a byproduct of this bias, we run experiments with the modified instruction “Write a high-quality answer for the given ques-tion using only the provided search results (some of which might be irrelevant). The search results are ordered randomly.” In addition, we randomly shuffle the k − 1 distractor documents. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 65
> 70
> 75
> 80
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, random distractors)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 13: Language model performance on multi-document QA when using random distractors, rather than retrieved distractors. 

Figure 14 presents the results of this experiment. We continue to see a U-shaped performance curve, with performance degrading when language mod-els must use information in the middle of their input contexts. Comparing the results in §2.3 with those when randomizing the distractor order and mentioning such in the prompt, we see that ran-domization slightly decreases performance when the relevant information is at the very beginning of the context, and slightly increases performance when using information in the middle and end of the context. 

D GPT-4 Performance 

We evaluate GPT-4 (8K) on a subset of 500 ran-dom multi-document QA examples with 20 total documents in each input context (Figure 15). GPT-4 achieves higher absolute performance than any other language model, but still shows a U-shaped performance curve—its performance is highest when relevant information occurs at the very start or end of the context, and performance degrades when it must use information in the middle of its input context. 

E Llama-2 Performance 

We evaluate Llama-2 (Touvron et al., 2023b) on multi-document QA with 20 total documents in each input context. The Llama tokenizer pro-duces longer sequences than the tokenizers for our previously-studied models, so we discard 20 exam-1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, randomly ordered)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 14: Language model performance when random-izing the order of the distractors (rather than presenting them in order of decreasing relevance) and mentioning as such in the prompt. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 50
> 60
> 70
> 80
> 90
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, 500 question sample)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k
> gpt-4-0613

Figure 15: Although GPT-4 has higher absolute perfor-mance than other models, its performance still degrades when relevant information occurs in the middle of the input context. ples (out of 2655) that exceed Llama-2’s maximum context length of 4096 tokens. We experiment with models of varying sizes (7B, 13B, and 70B pa-rameters), with and without additional supervised fine-tuning and reinforcement learning from hu-man feedback (“ -chat-” models). The results are presented in Figure 16. Comparing Llama-2 models of varying sizes, we find that only the larger models (13B and 70B) exhibit the U-shaped performance curve (i.e., both primacy and recency bias)—the smallest Llama-2 models (7B) are solely recency-biased. Given these results, we hypothesize that prior work (e.g., Khandelwal et al., 2018; Sun et al., 2021) did not previously observe any primacy bias in language models because the models they studied were too small (less than 1B parameters). Comparing between Llama-2 models with and without additional supervised fine-tuning and re-inforcement learning from human feedback, we see that additional fine-tuning dramatically im-proves performance on the multi-document QA task. The 7B models with and without additional fine-tuning show minimal primacy bias, and are largely recency-biased. The 13B base model has a dramatic primacy and recency bias—there is a 20-point accuracy disparity between the best- and worst-case performance. Applying additional fine-tuning to the 13B seems to slightly reduce this bias (10-point worst-case degradation), but the bias remains significant. However, the 70B models with and without additional fine-tuning have largely similar trends (showing both primacy and recency bias), and additional fine-tuning minimally changes the positional bias severity. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 20
> 30
> 40
> 50
> 60
> 70
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> Llama-2-7b-chat-hf
> Llama-2-13b-chat-hf
> Llama-2-70b-chat-hf
> Llama-2-7b-hf
> Llama-2-13b-hf
> Llama-2-70b-hf

Figure 16: Multi-document QA performance (20 total documents) of Llama-2 models of varying sizes (7B, 13B, 70B parameters), with and without additional su-pervised fine-tuning and reinforcement learning from human feedback (“ -chat-” models). F Token Counts 

Table 2, Table 3, and Table 4 present the average and maximum number of tokens in each of the input contexts for all experimental settings. Note that MPT-30B and MPT-30B-Instruct use the same tokenizer, GPT-3.5-Turbo and GPT-3.5-Turbo (16K) use the same tokenizer, and Claude-1.3 and Claude-1.3 (100K) use the same tokenizer. Furthermore, the Claude-1.3 tokenizer is the same as the GPT-3.5-Turbo tokenizer, modulo some additional special tokens that do not appear in our data. As a result, the token counts for these two model families is the same in our experimental settings. Closed-Book Oracle avg ± stdev max avg ± stdev max LongChat-13B (16K) 55.6 ± 2.7 70 219.7 ± 48.5 588 MPT-30B 43.5 ± 2.2 58 187.9 ± 41.8 482 GPT-3.5-Turbo 15.3 ± 2.2 29 156.0 ± 41.8 449 Claude-1.3 15.3 ± 2.2 29 156.0 ± 41.8 449 

> Table 2: Token count statistics for each of the evaluated models on the closed-book and oracle multi-document question answering settings.

10 docs 20 docs 30 docs avg ± stdev max avg ± stdev max avg ± stdev max LongChat-13B (16K) 1749.9 ± 112.4 2511 3464.6 ± 202.3 4955 5181.9 ± 294.7 7729 MPT-30B 1499.7 ± 88.5 1907 2962.4 ± 158.4 3730 4426.9 ± 230.5 5475 GPT-3.5-Turbo 1475.6 ± 86.5 1960 2946.2 ± 155.1 3920 4419.2 ± 226.5 6101 Claude-1.3 1475.6 ± 86.5 1960 2946.2 ± 155.1 3920 4419.2 ± 226.5 6101 

> Table 3: Token count statistics for each of the evaluated models on each of the document question answering settings.

75 KV pairs 140 KV pairs 300 KV pairs avg ± stdev max avg ± stdev max avg ± stdev max LongChat-13B (16K) 5444.5 ± 19.1 5500 10072.4 ± 24.1 10139 21467.3 ± 35.9 21582 MPT-30B 4110.5 ± 23.8 4187 7600.9 ± 31.1 7687 16192.4 ± 46.6 16319 GPT-3.5-Turbo 3768.7 ± 25.6 3844 6992.8 ± 34.1 7088 14929.4 ± 50.7 15048 Claude-1.3 3768.7 ± 25.6 3844 6992.8 ± 34.1 7088 14929.4 ± 50.7 15048 

> Table 4: Token count statistics for each of the evaluated models on each of the key-value (KV) retrieval settings.

G Full Multi-Document Question Answering Results 

This section tabulates model performance when evaluated on the multi-document QA task with varying numbers of documents (Figure 5). “Index n” indicates performance when the document with the answer occurs at position n + 1 , where lower indices are closer to the start of the input context. For example, index 0 refers to performance when the document with the answer is placed at the very start of the context (i.e., first amongst all documents). 

G.1 10 Total Retrieved Documents 

Model Index 0 Index 4 Index 9 Claude-1.3 62.9% 58.3% 59.7% Claude-1.3 (100K) 63.1% 58.3% 59.7% GPT-3.5-Turbo 76.8% 61.2% 62.4% GPT-3.5-Turbo (16K) 76.9% 61.0% 62.5% MPT-30B-Instruct 60.2% 56.2% 59.7% LongChat-13B (16K) 72.1% 58.9% 58.5% 

> Table 5: Model performance when evaluated on the multi-document QA task with 10 total retrieved documents.

G.2 20 Total Retrieved Documents 

Model Index 0 Index 4 Index 9 Index 14 Index 19 Claude-1.3 59.9% 55.9% 56.8% 57.2% 60.1% Claude-1.3 (100K) 59.8% 55.9% 57.0% 57.4% 60.0% GPT-3.5-Turbo 75.8% 57.2% 53.8% 55.4% 63.2% GPT-3.5-Turbo (16K) 75.7% 57.3% 54.1% 55.4% 63.1% MPT-30B-Instruct 53.7% 51.8% 52.2% 52.7% 56.3% LongChat-13B (16K) 68.6% 57.4% 55.3% 52.5% 55.0% 

> Table 6: Model performance when evaluated on the multi-document QA task with 20 total retrieved documents.

G.3 30 Total Retrieved Documents 

Model Index 0 Index 4 Index 9 Index 14 Index 19 Index 24 Index 29 Claude-1.3 59.1% 55.1% 54.8% 55.7% 56.4% 56.2% 59.9% Claude-1.3 (100K) 59.1% 55.1% 54.9% 55.7% 56.6% 56.1% 60.0% GPT-3.5-Turbo (16K) 73.4% 55.1% 50.5% 50.9% 51.8% 54.9% 63.7% MPT-30B-Instruct 51.6% 51.3% 51.2% 49.0% 49.6% 51.3% 54.1% LongChat-13B (16K) 66.9% 54.8% 52.5% 52.9% 52.2% 51.3% 55.1%

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="jina-scraped-3.md">
<details>
<summary>Retrieval-Augmented Generation with Graphs (GraphRAG)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2501.00309v2>

# Retrieval-Augmented Generation with Graphs (GraphRAG)

## Abstract

Retrieval-augmented generation (RAG) is a powerful technique that enhances downstream task execution by retrieving additional information, such as knowledge, skills, and tools from external sources. Graphs, by their intrinsic "nodes connected by edges" nature, encode massive heterogeneous and relational information, making them a golden resource for RAG in tremendous real-world applications. As a result, we have recently witnessed increasing attention on equipping RAG with graphs, i.e., GraphRAG. However, unlike conventional RAG, where the retriever, generator, and external data sources can be uniformly designed in the neural-embedding space, the uniqueness of graph-structured data, such as diverse-formatted and domain-specific relational knowledge, poses unique and significant challenges when designing GraphRAG for different domains. Given the broad applicability, the associated design challenges, and the recent surge in GraphRAG, a systematic and up-to-date survey of its key concepts and techniques is urgently desired. Following this motivation, we present a comprehensive and up-to-date survey on GraphRAG. Our survey first proposes a holistic GraphRAG framework by defining its key components, including query processor, retriever, organizer, generator, and data source. Furthermore, recognizing that graphs in different domains exhibit distinct relational patterns and require dedicated designs, we review GraphRAG techniques uniquely tailored to each domain. Finally, we discuss research challenges and brainstorm directions to inspire cross-disciplinary opportunities. Our survey repository is publicly maintained at https://github.com/Graph-RAG/GraphRAG/.

## 1 Introduction

Retrieval-Augmented Generation (RAG), as a powerful technique to improve downstream tasks by retrieving additional information from external data sources, has been successfully applied to various real-world applications. In RAG frameworks, retrievers search for additional knowledge, skills, and tools based on user-defined queries or task instructions. The retrieved content is then refined by an organizer and seamlessly integrated with the original query or instruction, which is further fed into the generator to produce the final answer. For example, when conducting question-answering (QA) tasks, the classic "Retriever-then-Reader" frameworks retrieve external factual knowledge to improve the answer faithfulness, which significantly benefits social goodness and mitigates risks in high-stake scenarios (e.g., medical, legal, financial, and education consultation). Moreover, recent advancements in large language models (LLMs) have further underscored the power of RAG in enhancing the social responsibility of LLMs, such as mitigating hallucinations, enhancing interpretability and transparency, enabling dynamic adaptability, reducing privacy risks, ensuring reliability/robust responses, and promoting fair treatment.

Building on the unprecedented success of RAG and further considering the ubiquity of graphs in real-world applications, recent research has explored the integration of RAG with graph-structured data. Unlike textual or visual data, graph-structured data encodes heterogeneous and relational information through its intrinsic "nodes connected by edges" nature. For example, individuals connected by social relationships of social networks usually exhibit homophily behaviors, sequential decision-making steps in plans follow causal dependency, and atoms belonging to the same functional group within a molecule possess unique structural properties. Designing the RAG that utilizes relational information requires adapting its core components, such as the retriever and generator, to seamlessly integrate graph-structured data, resulting in GraphRAG. Different from RAG, which predominantly uses semantic/lexical similarity search, GraphRAG offers unique advantages in capturing relational knowledge by leveraging graph-based machine learning (e.g., Graph Neural Networks (GNNs)) and graph/network analysis techniques (e.g., Graph Traversal Search and Community Detection). For example, considering the query “What drugs are used to treat epithelioid sarcoma and also affect the EZH2 gene product?", blindly executing the existing BM25 or embedding-based search that relies solely on semantic/lexical similarity ignores relational knowledge encoded in graph structure. In contrast, some GraphRAG methods traverse the graph along the relational path “Disease (Epithelioid Sarcoma) $\rightarrow$ [indication] $\rightarrow$ Drug $\leftarrow$ [target] $\leftarrow$ Gene/Protein (EZH2 gene product)" to retrieve neighbors of Epithelioid Disease following the relation [indication], neighbors of Gene EZH2 following the relation [target], and find their intersected drug. Moreover, some domains involve entities with extremely complex geometry that require dedicated model design to characterize. For example, 3D structures in molecular graphs and hierarchical tree structures commonly found in product taxonomies (e.g., on Amazon), in document sections (e.g., when using Adobe Acrobat), and social networks (e.g., at Snap) requires carefully designed graph encoders (or, more precisely, geometric encoders) with appropriate expressiveness to capture structural nuances. Simply verbalizing node texts and feeding them into LLMs cannot express complex geometric information and becomes infeasible given the exponentially growing textual descriptions as neighborhood layers expand.

Despite the above advantages of GraphRAGs over RAGs, designing appropriate GraphRAGs faces unprecedented challenges due to the following differences in graph-structured data:

*   **Difference 1 - Unified vs. Diverse-Formatted Information**: Unlike conventional RAG, where semantic information can be uniformly represented as a 2D grid of image patches or a 1D sequence of textual corpora, graph-structured data often encompass diverse formats and are stored in heterogeneous sources. For example, document graphs embed entities as sentence chunks, knowledge graphs store graph information as triplets or paths, and molecule graphs consist of higher-order structures (e.g., cellular complexes), as shown in Figure 1. Some graph data may even be multimodal (e.g., text-attributed graphs include both structural and textual attributes, and scene graphs combine structures and vision). Consequently, this diversity necessitates different RAG designs. For retrievers, conventional RAG assumes the target information is indexed in an image or text corpus, which can be uniformly represented as vector embeddings and enable one-size-fits-all embedding-based retrieval. However, retrievers for GraphRAG must consider the concrete format and source of the desired information, making the one-size-fits-all design impractical. When dealing with knowledge graph question-answering, information of nodes, edges, or subgraphs is usually fetched by graph search before embedding matching-based retrieval. This fetching operation is usually conducted by identifying relevant nodes/edges/subgraphs via entity linking, relational matching, and graph search algorithms (e.g., Breadth-First Search, Depth-First Search, Monte Carlo Tree Search, and A* search), which is unachievable if solely through deep learning-based embedding similarity search.
    Furthermore, the design of the retriever should ensure sufficient geometric expressiveness to capture structural nuances. For instance, when retrieving APIs from a plan graph to accomplish specific goals, it is essential to equip the retriever with directional awareness. This enables the execution of APIs with resource dependencies in the correct order, preventing conflicts and avoiding invalid operations. Similarly, designing expressive retrievers capable of differentiating high-order subgraph structures, such as 6-cycle benzene vs. 4-star Methane, and 3-star T-junction vs. 4-square road, is essential in drug design for disease treatment and road construction for city planning. Beyond the retriever, the generator also requires specialized designs. When retrieved content includes complex graph structures with textual attributes, simply verbalizing the text of the subgraph and concatenating it into a prompt may obscure critical structural information. In these cases, encoding the graph with graph encoders such as GNNs before integrating it into generation can help preserve structural nuances.
*   **Difference 2 - Independent vs. Interdependent Information**: In conventional RAG, information is stored and utilized independently. For example, documents are split into chunks, such as individual sentences, paragraphs, or a fixed number of tokens, based on the document context and downstream task. Each chunk is then indexed and stored independently in a vector database. This independence prevents the retrieval from capturing chunk relations, which hinders performance on tasks requiring multi-hop reasoning and long-form planning. However, GraphRAG stores chunks as interconnected nodes with edges denoting their relations, which can benefit retrieval, organization, and generation. For retrieval, these edges could enable multi-hop traversal to capture other chunks that share a logical connection with existing retrieved chunks. Furthermore, the retrieved content can be organized not only by their semantic meaning (e.g., reranking) but also their structural relations (e.g., graph pruning). During the generation phase, squeezing interdependency (e.g., positional encoding) to the generator would encode richer structural signals into the generated content.
*   **Difference 3 - Domain Invariance vs. Domain-specific Information**: The relations in graph-structured data are domain-specific. Unlike images and texts, where different domains often share transferable semantics, such as textures and grains in images or vocabulary defined by the tokenizer in texts, graph-structured data lacks explicit transferable units. This shared basis in images and texts lays the foundation for designing encoders with geometric invariance and enables the well-known data-scaling law. However, for graph-structured data, the underlying data generation process governing the generated graphs varies significantly across different domains. This variability makes the relational information highly domain-specific, and it is nearly impossible to design a unified GraphRAG applicable to different domains. For example, when predicting the topic of an academic paper, the widely accepted homophily assumption suggests retrieving references from the paper to inform its topic prediction. However, this homophily assumption is not suitable when classifying the role of an airport in a flight network, where hubs are often sparsely distributed across a country with no direct connections. Moreover, even within the same graph from the same domain, different tasks may necessitate distinct GraphRAG designs. For example, when designing an automatic email completion system to optimize communication efficiency in a company, both content relevance and tone coherence should be considered. To ensure the content relevance of the generated emails, one might assume that close emails (i.e., emails from the same conversation thread) share similar content and thus should be retrieved for reference. However, to maintain tone coherence, emails from staff with similar roles might be retrieved, even if they do not share close social relations (e.g., between subordinates and superiors) but instead hold similar structural roles within the company (e.g., as managers of different teams).

![Figure 1: RAG works on text and images, which can be uniformly formatted as 1D sequences or 2D grids with no relational information. In contrast, GraphRAG works on graph-structured data, which encompasses diverse formats and includes domain-specific relational information.](extracted/6113564/Figure/rag-grag.png)

Despite the above differences that have driven extensive research in GraphRAG, the current research landscape in this field remains fragmented, with significant variation in concepts, techniques, and datasets across studies. Moreover, current GraphRAG research primarily focuses on knowledge and document graphs as surveyed in Figure 2, often overlooking broader applications in other domains like infrastructure graphs. This imbalance not only hampers the advancement of GraphRAG but also risks creating a "bubble effect" that restricts the scope of future exploration. To address these challenges, we present a comprehensive and up-to-date review of GraphRAG, aiming to unify the GraphRAG framework from the global perspective while also specializing its unique design for each domain from the local perspective. The key contributions of this survey are as follows:

![Figure 2: Publications of GraphRAGs in different domains based on surveyed papers](extracted/6113564/Figure/count_paper_annotated.png)

*   **A Holistic Framework of GraphRAG**: We propose a holistic framework of GraphRAG consisting of five key components: query processor, retriever, organizer, generator, and graph data source. Within each component, we review representative GraphRAG techniques.
*   **Specialization of GraphRAG in different domains**: We categorize GraphRAG designs into 10 distinct domains based on their specific applications, including knowledge graph, document graph, scientific graph, social graph, planning & reasoning graph, tabular graph, infrastructure graph, biological graph, scene graph, and random graph. For each domain, we review their unique applications and specific graph construction methods. We then summarize the distinctive designs of each component within our proposed holistic GraphRAG framework and collect rich benchmark datasets and tool resources.
*   **Challenges and Future Directions**: We highlight the challenges of current GraphRAG research and pinpoint future opportunities for further advancing GraphRAG into the new frontier.

In the following, we highlight the differences between our survey and existing surveys. Despite the urgent need for a systematic overview of GraphRAG, most existing surveys focus on general RAG within the context of i.i.d. data. Before the advent of LLMs, earlier surveys focused on textual RAGs. With the recent unprecedented success achieved by foundational models such as LLMs, various surveys have explored foundational-model-powered RAG in different modalities. group existing RAG approaches into three categories (Naive, Advanced, and Modular RAGs), summarize three core techniques (Retrieval, Generation, and Augmentation), and review evaluation metrics. In parallel, review representative RAG systems according to their corresponding application and data modality. focuses on reviewing trustworthy concerns and techniques of RAG. However, none of them have a dedicated focus on graph-structured data. To the best of our knowledge, only one very recent study has specifically surveyed RAG in the context of graph-structured data. However, this work mainly focuses on reviewing techniques introduced by graphs under the conventional RAG architecture without specializing in reviewing diverse relations and technical designs for graphs across different domains. In contrast to its holistic review philosophy, we recognize the inherent heterogeneity of graph-structured data and specialize our GraphRAG review across different domains. Specifically, we uncover the fundamental task applications (when to retrieve), graph construction methods and relational rationales (what to retrieve), and GraphRAG techniques (how to retrieve) for each domain. In this way, our survey provides a comprehensive overview of GraphRAG for information retrieval, data mining, and machine learning communities and domain-specific insights that facilitate interdisciplinary research and industrial opportunities.

Our survey is structured as follows: Section 2 introduces the holistic framework of GraphRAG and introduces representative techniques for its five key components. From Section 3 to 9, we delve into specific domains, reviewing unique task applications, summarizing existing graph construction methods that guide GraphRAG design for that domain, highlighting domain-specific techniques for each of the five components within our proposed holistic framework, and presenting existing GraphRAG resources (e.g., benchmark datasets and tools) used across different domains. Finally, we discuss research challenges and opportunities in Section 10 and conclude our survey in Section 11.

![Figure 3: A holistic framework of GraphRAG and representative techniques for its key components.](extracted/6113564/Figure/framework.png)

## 2 A Holistic Framework of GraphRAG

Based on existing literature on GraphRAG, we present a holistic framework of GraphRAG. Next, we introduce the basic problem setting and notation used throughout the whole framework.

### 2.1 Problem Setting and Notations

Following the general setting of RAG, given a graph-structured data source $G$, the user-defined query $Q$ is further sent to query processor $\boldsymbol{\Omega}^{\textbf{Processor}}$ to obtain the pre-processed query $\hat{Q}$. After that, the retriever $\boldsymbol{\Omega}^{\textbf{Retriever}}$ retrieves the content $C$ from the graph data source $G$ based on $\hat{Q}$. Next, the retrieved content $C$ is refined by the organizer $\boldsymbol{\Omega}^{\textbf{Organizer}}$ to formulate the refined content $\hat{C}$. Finally, the refined content $\hat{C}$ triggers the generator $\boldsymbol{\Omega}^{\textbf{Generator}}$ to generate the final answer $A$. The above five components are summarized as follows:

*   Query Processor $\boldsymbol{\Omega}^{\textbf{Processor}}$: Preprocessing the given query $\hat{Q}=\boldsymbol{\Omega}^{\textbf{Processor}}(Q)$.
*   Graph Data Source $G$: Information organized in graph-structured format.
*   Retriever $\boldsymbol{\Omega}^{\textbf{Retriever}}$: Retrieve the content $C=\boldsymbol{\Omega}^{\textbf{Retriever}}(\hat{Q},G)$ from $G$ based on the query $\hat{Q}$.
*   Organizer $\boldsymbol{\Omega}^{\textbf{Organizer}}$: Arrange and refine the retrieved content $\hat{C}=\boldsymbol{\Omega}^{\textbf{Organizer}}(\hat{Q},C)$.
*   Generator: Generate answers $A=\boldsymbol{\Omega}^{\textbf{Generator}}(\hat{Q},\hat{C})$ to answer query $Q$.

Unlike sequential-based textual data and grid-structured image data, graph-structured data encapsulates relational information. To effectively harness this relational information, the above five core components of GraphRAG desire dedicated designs to handle graph-structured input/output and support graph-based operations. For example, in the retriever component, conventional RAG in the Natural Language Processing (NLP) utilizes sparse/dense encoders for index search. In contrast, GraphRAG employs graph traversal methods (e.g., entity linking and BFS/DFS) and graph-based encoders (e.g., Graph Neural Networks (GNNs)) to produce embeddings for retrieval.
This motivates us to summarize key innovations and representative designs of GraphRAG for each of the above five components under the holistic GraphRAG framework in the following.

### 2.2 Task Applications and Example Query $Q$

Similar to the general RAG framework where the text-formatted query $Q$ specifies the question context or the task instruction. Query $Q$ in GraphRAG could also be in the format of text. For example, in knowledge graph-based question-answering, the query could be "What is the Capital of China?". In addition, the query could also be in other formats, such as smile strings for molecular graphs, or could even be the combination of multiple formats, such as the scene graph along with the text instruction. Table 1 summarizes the common task applications and exemplary queries used in each domain, as well as their representative references.

Table 1: Summary of Task Applications and Exemplary Queries for GraphRAG in each domain.

![Figure 4: Existing techniques of query processor $\boldsymbol{\Omega}^{\text{Processor}}$ in GraphRAG.](extracted/6113564/Figure/query_tech.png)

**Table 2: Difference of query processor $\boldsymbol{\Omega}^{\text{Processor}}$ between RAG and GraphRAG.**
| Technique | RAG | GraphRAG |
| --- | --- | --- |
| Entity Recognition | Extracting mentions in knowledge bases | Extracting mentioned nodes in graphs. |
| Relational Extraction | Extracting textual relations | Extracting graph edge relations |
| Query Structuration | Structuring text query to SQL, SPARQL | Structuring text query to GQL |
| Query Decomposition | Decomposed queries are separate | Decomposed queries are logically related |
| Query Expansion | Expansion based on semantic knowledge | Expansion based on relational knowledge |

### 2.3 Query Processor $\boldsymbol{\Omega}^{\text{Processor}}$

Unlike RAG, where both queries and data sources are purely text-formatted, data sources used in GraphRAG are graph-structured, which raises challenges in bridging text-formatted queries and graph-structured data sources. For example, the information that connects the knowledge graph and the query "Who is Justin Bieber’s brother?" is not a specific passage but instead the entity "Justin Bieber" and the relation "brother of". Many techniques are proposed to correctly extract this information from the query, including entity recognition, relational extraction, query structuration, query decomposition, and query expansion. In the following, we first review each of these five query processing techniques within the broader NLP domain, followed by a focused examination of their unique adaptations for GraphRAG.

#### 2.3.1 Name Entity Recognition

Named Entity Recognition (NER) aims to identify mentions of entities from the text that belong to predefined categories, such as persons, locations, or organizations, and it serves as a fundamental component for numerous natural language applications. NER techniques can be broadly categorized into four main approaches: (1) rule-based methods, which rely entirely on handcrafted rules and require no annotated data; (2) unsupervised learning methods, which use unsupervised algorithms without labeled training examples; (3) feature-based supervised learning methods, which depend on supervised algorithms and careful feature engineering; and (4) deep learning approaches, which automatically discover representations needed after (un)-supervised training the deep learning models. Recent LLMs fall into the category of deep learning approaches and have demonstrated unprecedented success for NER. More details about these techniques and their resources can be found in.

Specifically, in the GraphRAG context, entity recognition primarily uses deep learning techniques (e.g., EntityLinker and LLM-based extraction) to identify entities in queries grounded by nodes in the given graph data sources. This step is vital for applications such as knowledge graph-based question answering. For example, given the question, "What is the best way to guess the color of the eye of the baby?", NER extracts entities such as "baby", "eye", and "color", which correspond to nodes in the knowledge graph and are treated as the seed nodes to initialize the retrieval process thereafter. For more recent GraphRAG research, NER has evolved beyond identifying the entity names but instead their structures. For example, leverages LLMs to recognize node types in the graph, which further guides the retriever to identify nodes that match the recognized types for next-round exploration. For example, given the question "Who are the authors of ‘Language Models are Unsupervised Multi-task Learners’?" the initially recognized entity should not only be based on the semantic name "Language Models are Unsupervised Multi-task Learners" but also be based on the type of that entity, which is the paper node in this case. Accurately recognizing the names and structures of entities in GraphRAG reduces cascading errors and provides a solid foundation for subsequent retrieval and generation steps.

#### 2.3.2 Relational Extraction

Similar to NER, relational extraction (RE) is a long-standing technique in NLP to identify relations among entities and is widely applied to structured search, sentiment analysis, question answering, summarization, and knowledge graph construction. Recent advances in RE have been largely driven by deep learning techniques, and they can be summarized into three perspectives: text representation, context encoding, and triplet prediction, more details of which can be found in.

For GraphRAG, RE serves two key purposes: constructing graph-structured data sources (e.g., knowledge graphs) by extracting triplets and matching the relations mentioned in the query and the graph data source to guide the graph search. For instance, given a query like "What is the capital of China?", relational extraction identifies the relation "capital of" and searches for corresponding edges via vector similarity in the knowledge graph, which guides the neighborhood selection and graph traversal direction.

#### 2.3.3 Query Structuration

Query structuration transforms queries into formats tailored to specific data sources and tasks. It often converts natural language queries into structured formats like SQL or SPARQL to interact with relational databases. Recent advancements leverage pre-trained and fine-tuned LLMs to generate structured queries from natural language input to query databases. For graph-structured data, Graph Query Language (GQL) has emerged, such as Cypher, GraphQL, and SPARQL, which enables complex interactions with property graph databases. Additionally, introduced a technique that decomposes complex queries into multiple structured operations, including node retrieval, feature fetching, neighbor checks, and degree assessment, enhancing precision and adaptability in querying.

#### 2.3.4 Query Decomposition

Query decomposition aims to split the input query into multiple distinct subqueries, which are used to first retrieve sub-results and aggregate these sub-results together for the final results. In most existing RAG and GraphRAG, decomposed queries usually possess explicit logic connections that can handle complex tasks that require multistep reasoning and planning. For example, a query like "Please generate an image where a girl is reading a book, and her pose is the same as the boy in ‘example.jpg’ then describe the new image with your voice" involves multiple subtasks, each of which would be completed by a specific sub-query. In addition, enhance the decomposition of the query by building a question graph where each sub-query is represented as a triplet within the graph. These graph-structured sub-queries effectively guide the retriever/generator through multi-step promptings.

#### 2.3.5 Query Expansion

Query Expansion enriches a query by adding meaningful terms with similar significance, which primarily addresses three challenges: (1) user-submitted queries are ambiguous and relate to multiple topics; (2) queries may be too brief to fully capture user intent; and (3) users are often uncertain about what they are seeking. Generally, it can be categorized into manual query expansion, automatic query expansion, and interactive query expansion. More recently, LLM-based query expansion has been a prominent area due to the creativity of the generated content

Unlike existing methods that mostly focus on textual similarities and overlook relations, QE in GraphRAG augments LLM expansion with structured relations. For example expands the query by leveraging neighboring nodes of the mentioned entities in the query. Alternatively, convert the query into several sub-queries using pre-defined templates.

### 2.4 Retriever $\boldsymbol{\Omega}^{\textbf{Retriever}}$

After obtaining the processed query $\hat{Q}$, the retriever $\boldsymbol{\Omega}^{\textbf{Retriever}}$ identifies and retrieves relevant content $C$ from external graph sources $G$ to augment the downstream task execution:

$$ C=\boldsymbol{\Omega}^{\textbf{Retriever}}(\hat{Q},G) \quad (1) $$

Recently, retrievers have been increasingly integrated with LLMs to mitigate hallucination issues, address privacy concerns, and enhance explainability and dynamic adaptability. While effective, they are predominantly designed for texts and images and not readily transferable to graph-structured data for GraphRAG for two reasons. First, the input/output format of GraphRAG differs significantly from that of traditional RAG. While most retrievers in RAG use NLP tokenizers for encoders and adhere to the "Text-in, Text-out" workflow, the workflow of GraphRAG is more diverse, including "Text-in, Text-out", "Text-in, Graph-out", "Graph-in, Text-out" and "Graph-in, Graph-out" processes. Secondly, retrievers in traditional RAGs do not capture graph structure signals. Methods like BM25 and TF-IDF primarily focus on lexical signals, and deep-learning-based retrievers usually capture semantic signals, both of which overlook the graph structure signals. This motivates us to review existing GraphRAG retrievers, i.e., heuristic-based, learning-based, and domain-specific retrievers, with a particular emphasis on their unique technical design adapted to graph-structured data.

![Figure 5: Visualizing representative retrievers used in GraphRAG.](extracted/6113564/Figure/retrieve_tech.png)

**Table 3: Categorizing representative retrievers used in GraphRAG.**
| Method/Strategy | Input | Output | Description |
| --- | --- | --- | --- |
| Entity Linking | Entity Mention | Node | Match query entity and graph node |
| Relational Matching | Relation Mention | Edge | Match query relation and graph edge |
| Graph Traversal | Node/Edge | Graph | Expand seed nodes/edges into subgraphs |
| Graph Kernel | (Sub)Graph | (Sub)Graph | Match query graph and candidate graph |
| Shallow Embedding | Any | Any | Embedding similarity match query and candidate |
| Deep Embedding | Any | Any | Embedding similarity match query and candidate |
| Domain Expertise | Expertise Rule | Any | Match Domain Expertise with nodes/edges/graphs |

#### 2.4.1 Heuristic-based Retriever

Heuristic-based retrievers primarily use predefined rules, domain-specific insights, and hard-coded algorithms to extract relevant information from graph data sources. Their reliance on explicit rules often makes them more time/resource-efficient compared to deep learning models. For instance, simple graph traversal methods like BFS or DFS can be executed in linear time without needing training data. However, this same reliance on fixed heuristics also limits their adaptability to generalize to unseen scenarios. In the following, we review the heuristic-based retrievers commonly used in GraphRAG.

**Entity Linking:** In heuristic-based retrievers, entity linking involves mapping entities identified in the query to corresponding nodes in graph data sources. This mapping forms an initial bridge between the query and the graph, serving as either the retriever by itself or as a foundation for further graph traversal to broaden the scope of the retrieval. The effectiveness of this approach relies on accurate entity recognition conducted by the query processor and the quality of labeled entities on graph nodes. This technique is commonly applied in knowledge graphs, where Top-K nodes are selected as starting points based on their textual similarity to the query. The similarity metric can be computed using vector embeddings and lexical features. More recently, LLMs have been used as knowledgeable context augmenters to generate mention-centered descriptions as additional input to augment the long-tail entities where their limited training data usually cause the entity linking model to struggle to disambiguate.

**Relational Matching:**
Relational matching, similar to entity linking, is a heuristic-based retrieval approach designed to identify edges within graph data sources that align with the relations specified in a query. This method is crucial for tasks that focus on identifying relationships among entities in a graph. The matched edges guide the traversal process by indicating which edges to explore next based on the entities and relations encountered in the graph data sources. Similar to entity linking, Top-K edges are selected based on their similarity to each edge in the graph.

In addition to the efficiency and simplicity of the above two types of heuristic-based retrievers, another key advantage is their ability to overcome ambiguity. For example, although machine/deep learning-based retrievers are difficult to differentiate semantically/lexically similar entities/relations (e.g., Byte vs. Bit, and President of vs. Resident of), these heuristic methods can easily distinguish them based on pre-defined rules, even in cases where semantic/lexical differences are subtle.

**Graph Traversal:**
After performing entity linking and relational matching to identify initial nodes and relations in graph data sources, graph traversal algorithms (e.g., BFS, DFS) can expand this set to uncover additional query-relevant information. However, a core challenge for traversal-based retrieval is the risk of information overload, as the exponentially expanding neighborhood often includes substantial irrelevant content. To address this, current traversal techniques integrate adaptive retrieval and filtering processes, selectively exploring the most relevant neighboring nodes and incrementally refining the retrieved content to minimize noise. This graph traversal is mainly used in GraphRAG for knowledge and document graphs. When traversing on these two types of graphs, many methods extract all paths less than length $l$ between the nodes identified by entity linking, while others consider the $l$-hop subgraph around the initial entities. To more efficiently traverse the KG, other methods prune irrelevant paths via the use of a LLM and others use pre-defined rules or templates to traverse the graph.

**Graph Kernel:**
Compared with the above heuristic-based retrievers for retrieving nodes, edges, and their combined subgraphs, some earlier works (e.g., graph extraction and image retrieval) treat the text and image as the entire graph and use graph-level heuristics such as graph kernels to measure similarity and retrieve. Graph kernels measure pairwise similarities by calculating inner products between graphs, aligning both structural and semantic aspects of the query and the retrieved graphs. Notable examples include the random-walk kernel and the Weisfeiler Leman kernel. The random walk kernel computes similarity by performing simultaneous random walks on two graphs and counting the number of matching paths. The Weisfeiler Leman kernel iteratively applies the Weisfeiler Leman algorithm to produce color distributions of node labels at each iteration and then calculates similarity based on the inner products of these histogram vectors. For example, constructs event graphs of both documents and queries and uses a product graph kernel that counts walks between two graphs to measure the query-document similarity and rank the documents. conducts event graph matching by introducing a fast and efficient graph-matching kernel for image retrieval. Similarly, translates images into representative attribute structural graphs that capture spatial relations among regions and perform graph kernel based on random walks to derive hash codes for image retrieval.

**Domain Expertise:**
The domain-agnostic nature of traditional heuristic-based methods restricts their effectiveness in areas that require specialized expertise. For instance, in drug discovery, chemists typically design drugs by referencing existing molecules with desirable properties rather than constructing molecular structures from scratch. These molecules are selected based on domain knowledge that guides the retrieval of structures with similar characteristics. Following this intuition, many GraphRAG systems incorporate domain expertise to enhance retriever design. develop a hybrid retrieval system that integrates heuristic-based and learning-based retrieval to retrieve exemplar molecules that partially meet the target design criteria.

#### 2.4.2 Learning-based Retriever

One significant limitation of heuristic-based retrievers is their over-reliance on pre-defined rules, which limits their generalizability to data that does not strictly adhere to these rules. For example, when confronted with entities that have slight semantic or structural variations, such as "doctor" and "physician", heuristic-based retrievers like entity linking may treat them differently due to their distinct lexical representations, despite their shared underlying meaning. To overcome this limitation, learning-based retrievers have been proposed to capture deeper, more abstract, and task-relevant relations between the query and objects in data sources, which avoid relying solely on hard-coded rules. These retrievers often work by uniformly compressing information of various formats (e.g., texts and images) into embeddings based on machine learning encoders and then fetching relevant information by conducting an embedding-based similarity search. Notably, some entity linking and relational matching methods that employ machine learning encoders to generate embeddings for matching should also be considered as learning-based retrievers.

In conventional RAG, assuming the query $q$ and data sources that contain $n$ instances $S$ are embedded by corresponding encoders as $\mathbf{q}=\mathcal{F}_{q}(q)\in\mathbb{R}^{d}$ and $\mathbf{S}=\mathcal{F}_{S}(S)\in\mathbb{R}^{n\times d}$, we retrieve top-$k$ instances by similarity search according to the pre-defined similarity function $\phi$ in the embedding space.

$$ \mathcal{S}^{*}=\operatorname*{arg\,max}_{k}\phi(\mathbf{q},\mathbf{S}) \quad (2) $$

Unlike RAGs that use language and vision encoders to embed texts and images, encoders used in GraphRAG retrieval extend beyond independently and identically distributed (i.i.d.) data by embedding nodes, edges, and (sub)graphs. Depending on the input format, the encoder could be a text encoder for query, a graph-based encoder for graph structure, and an integrated text-and-graph encoder for the textual attributed graph. We specifically focus on graph-based encoders. Existing graph-based encoders can be broadly categorized into shallow embedding methods – such as Node2Vec and DeepWalk – and deep embedding methods like Graph Neural Networks (GNNs). Below, we review these two encoders and their unique roles in GraphRAG.

**Shallow Embedding Methods:**
Shallow embedding methods, like Node2Vec and Role2Vec, learn node, edge, and graph embeddings that retain the essential structural information of the original graph. Based on the type of structural information that can be extracted, these methods generally fall into two categories: proximity/role-based embeddings. Proximity-based methods, such as DeepWalk and Node2Vec, focus on preserving the proximity of connected nodes, ensuring that nodes close in the graph also remain close in the embedding space. Role-based methods, like Role2Vec and GraphWave, generate node embeddings based on their structural roles rather than their proximity relations. In general, these methods initialize each node with a latent embedding vector and conduct unsupervised training to squeeze structural signals derived from graph structure into the embedding. In GraphRAG, proximity-based shallow embeddings can effectively retrieve entities that are proximally close, while role-based embeddings can capture entities that share similar roles. For instance, proximity-based embeddings could be used to retrieve academic papers by fetching papers sharing similar research topics or retrieve reviews from products that are co-purchased with the current product. Meanwhile, role-based embeddings could support tasks like generating company emails by retrieving similar emails based on shared roles or tones.

**Deep Embedding Methods:**
Although shallow embedding methods incorporate structural signals into learned embeddings for nodes, edges, or entire graphs, they struggle to leverage semantic features—like bag-of-words representations for academic paper retrieval or atomic numbers for molecular retrieval. Additionally, these methods lack inductivity, requiring re-initialization and retraining whenever new nodes, edges, or graphs are added. This limitation significantly reduces their applicability in GraphRAG retrieval tasks as real-world knowledge evolves dynamically where new information continually replaces outdated content, such as in citation networks, social graphs, and knowledge graphs. To address these limitations, deep embedding methods have been proposed, which not only jointly fuse features and graph structures to obtain embeddings for retrieval but also inherent inductive property as the newly coming nodes/edges/graphs share common feature space with the ones during the training phase. One of the most representative and powerful approaches in this category is GNN, which combines the power of message-passing to encode structural signals and feature transformation to extract task-relevant information. Mathematically, $l^{\text{th}}$-layer graph convolution can be formulated as:

$$
\displaystyle\mathbf{x}_{i}^{l} =\gamma_{\boldsymbol{\Theta}_{\gamma}}\left(\mathbf{x}_{i}^{l-1} \oplus\sum_{j\in\mathcal{N}_{i}}\phi_{\boldsymbol{\Theta}_{\phi}}\left(\mathbf {x}_{i}^{l-1},\mathbf{x}_{j}^{l-1},\mathbf{e}_{ij}\right)\right),~{}~{}~{}~{}~ {}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}\text{Node-level} \quad (3) \\
\displaystyle\mathbf{e}_{ij}^{l} =\gamma_{\boldsymbol{\Theta}_{\gamma}}\left(\mathbf{e}_{ij}^{l-1} \oplus\sum_{e_{mn}\in\mathcal{N}_{ij}^{e}}\phi_{\boldsymbol{\Theta}_{\phi}} \left(\mathbf{e}_{ij}^{l-1},\mathbf{e}_{mn}^{l-1},\mathbf{x}_{e_{ij}\cap e_{mn }}\right)\right),~{}~{}~{}~{}\text{Edge-level} \quad (4) \\
\displaystyle\mathbf{G}^{l} =\rho_{\boldsymbol{\Theta}_{\rho_{G}}}(\{\mathbf{x}_{i}^{l}, \mathbf{e}_{ij}^{l}\mid v_{i}\in\mathcal{V}_{G},e_{ij}\in\mathcal{E}_{G}\}),~{ }~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{ }~{}~{}~{}~{}\text{Graph-level} \quad (5)
$$

In node-level graph convolution, each node $v_{i}$ adaptively aggregates the embeddings of its neighboring nodes $\mathcal{N}_{i}$, with weights based on edge features via the weighting function $\phi_{\boldsymbol{\Theta}_{\phi}}$. The aggregated neighborhood embeddings are then combined with the node’s own embedding from the previous layer $\mathbf{x}_{i}^{l-1}$, using a combination function $\gamma_{\boldsymbol{\Theta}_{\gamma}}$, as shown by Eq. (3). Optimizing loss from training downstream tasks would enable the weighting function $\phi_{\boldsymbol{\Theta}_{\phi}}$ to prioritize the most important neighbors and enable the combination function $\gamma_{\boldsymbol{\Theta}_{\gamma}}$ to balance contributions from the node’s neighborhood and its own embedding. Similarly, in edge-level graph convolution, the same aggregation principle applies, but the neighbors of an edge are edges incident to the same ending points of that edge $\mathcal{N}^{e}_{ij}$, as shown by Eq. (4). Graph-level embeddings could be obtained by further applying pooling operation $\rho_{\boldsymbol{\Theta}_{\rho}}$ over node and edge embeddings, as shown by Eq. (5). Following this GNN-based embedding paradigm, various forms of graph knowledge from diverse sources—such as nodes, edges, and (sub)graphs—can be uniformly embedded into vector representations, as shown in Figure 5(c) where we derive embeddings for nodes ($\mathbf{X}$), edges ($\mathbf{E}$), and graphs ($\mathbf{G}$).

Having obtained these node/edge/graph-level embeddings further enables us to create embeddings for different types of structures ($\mathbf{S}$) by combining these sub-structure embeddings according to specific configurations for each structure. For instance, if the retrieved subgraph is a path within a knowledge graph, we can aggregate the embeddings of the nodes and relations along that path to form a cohesive path embedding. Additionally, incorporating structural signals may be necessary, a consideration to be addressed in future work. Eventually, the resulting embeddings for different structures can be utilized either during the training phase to optimize query alignment or during the testing phase to enable similarity-based neural search. For example, GNN-RAG uses a GNN to perform retrieval, where a separate round of message passing is performed for each query. The query $\hat{Q}$ is incorporated into the message passing by, including its embedding in the message computation. A set of “candidate” nodes is chosen which have a probability of being relevant greater than some threshold. The shortest path from the query nodes to each candidate node is retrieved as context. consider the use of a conditional GNN where only the linked entities from the query are initialized to a non-zero representation. The candidate nodes are chosen in a similar manner to. A single path is then retrieved for each candidate node and is extracted by backtracking until we reach a query node. REANO encodes the query information into an edge-specific attention weight, conditional on the query. After aggregation, the top k triples most similar to the query are chosen as context.

#### 2.4.3 Advanced Retrieval Strategies

Real-world queries are often complex and encode multi-aspect intentions, possess structure patterns, and desire multi-hop reasoning that the aforementioned basic retrievers struggle to address. For example, answering "What is the name of the fight song of the university whose main campus is in Lawrence, Kansas, and whose branch campuses are in the Kansas City metropolitan area?" demands multi-hop reasoning to identify the university based on location and retrieve information about its fight song. Similarly, a query like "What are the main themes in the dataset?" requires understanding the product community structure, retrieving themes for each community, and aggregating the identified themes together to summarize the main theme. Furthermore, when asking "Who is the most impactful research scholar in deep learning?" the answer could vary depending on multiple aspects, such as the number of citations, the volume of published papers, or the number of co-authors. Accurately addressing such queries requires a deeper understanding of the underlying data distribution to discern which aspect the query prioritizes. To address these highly complex queries, advanced retrieval strategies have been proposed, and we review them as follows:

**Integrated Retrieval:** Integrated retrieval combines various types of retrievers to capture relevant information by balancing their strengths and weaknesses. Typically, integrated retrieval approaches are categorized according to which individual retrievers are used in combination, with notable examples including neural-symbolic retrieval and multimodal retrieval.

Since the knowledge stored in graph-structured data exists mostly in symbolic format, neural-symbolic retrieval is a natural choice for the integrated retrieval strategy in GraphRAG. This strategy interleaves rule-based patterns for retrieving symbolic knowledge with neural-based signals for retrieving more abstract and deep knowledge. For example, first expands the neighbors based on the knowledge of the symbolic knowledge graph and then performs path retrieval using neural matching. In contrast, first utilizes GNNs to retrieve seed entities (neural retrieval) and then extract the shortest paths from seed entities (symbolic retrieval). Similarly, fetch the k-hop neighborhood of the entities mentioned in the current question-answering pair and the session of user-generated items as the answer candidates (symbolic retrieval) and compute attention between the query and the extracted subgraph to differentiate candidate relevance (neural retrieval).

**Iterative Retrieval:** Iterative retrieval is a multistep process where consecutive retrieval operations share common dependencies such as causal, resource, and temporal dependency. These dependencies can be implicitly characterized by the retrieval order in RAG or explicitly modeled as a graph structure in GraphRAG. Consequently, iterative retrieval is primarily utilized in GraphRAG to capture these dependencies. For example, KGP alternates between generating the next piece of evidence for the question and selecting the most promising neighbor. ToG starts by identifying initial entities and then iteratively expands reasoning paths until enough information is gathered to answer the question. StructGPT pre-defines graph interfaces and prompts LLMs to iteratively invoke these interfaces until sufficient information is collected.

**Adaptive Retrieval:** While retrieved external knowledge offers benefits, it also introduces risks. If the generator already possesses sufficient internal knowledge for a task, the retrieved external information may be unnecessary or even conflicting. Specifically, when internal knowledge fully covers the necessary information, retrieval becomes redundant and may introduce contradictions. To mitigate this, knowledge checking has been proposed in RAG systems. This approach allows the system to adaptively assess when and how much external information is needed. By equipping the retriever with this adaptability, RAG can provide more intelligent, flexible, and context-aware responses, fostering better harmony between internal and external knowledge sources.

One of the adaptive retrievals in GraphRAG is designed by considering different reasoning depths for different queries, i.e., too few hops of graph traversal might overlook critical reasoning relations, while too many can introduce unnecessary noise. address this by training models to predict the required number of hops for a given query and retrieving the relevant graph content accordingly. No existing works focus on resolving knowledge conflicts in GraphRAG, and therefore, we leave this discussion to future work.

### 2.5 Organizer $\boldsymbol{\Omega}^{\textbf{Organizer}}$

After retrieving the relevant content $C$ from external graph data sources, which may be in the format of entities, relations, triplets, paths or subgraphs, the organizer $\boldsymbol{\Omega}^{\textbf{Organizer}}$ processes this content in conjunction with the processed query $\hat{Q}$. The aim is to post-process and refine the retrieved content to better adapt it for generator consumption, thereby further improving the quality of the downstream content generation. Formally, the organizer is represented as follows:

$$ \displaystyle\hat{C}=\boldsymbol{\Omega}^{\textbf{Organizer}}(\hat{Q},C) \quad (6) $$

In GraphRAG, the need for fine-grained organization and refinement of retrieved content is driven by several key reasons. Firstly, when the retrieved contents are subgraphs, their heterogeneous format of knowledge in terms of node/edge features and graph structures becomes more likely to include irrelevant and noisy information, which poses significant difficulty for LLM to digest and thus compromises the generation quality. This raises the desire for graph pruning techniques to polish the retrieved subgraph and remove task-irrelevant knowledge. Secondly, LLMs have been widely demonstrated to possess attention biases toward certain positions of relevant information within the retrieved context. Therefore, the exponentially growing neighbors as the receptive field enlarges (i.e., the number of hops increases) in the retrieved subgraphs would also exponentially increase the amount of context length in the prompt and dilute the focus of LLMs on the task-relevant knowledge. This poses a new requirement for the graph-based reranking mechanism to prioritize the most important content within the retrieved graph. Thirdly, the retrieved content might be incomplete in terms of both the semantic content and the structural content, which necessitates graph augmentation for the enhancement. Finally, the retrieved content is often a graph, which not only possesses semantic content information but also owns its unique structure. This complex structural content is not easily consumed by LLMs that are trained by next-token prediction coupled with linearized prompting, which requires structure-aware verbalization techniques to reorganize. We will formally review each of the above-motivated organizer techniques in the following sections.

#### 2.5.1 Graph Pruning

In GraphRAG, the retrieved graph can be large and potentially contain a significant amount of noisy and redundant information. For example, when graph traversal methods are applied in retrieval, the size of the retrieved subgraph exponentially increases with the number of hops. Large subgraph sizes not only increase computational costs but can also reduce generation quality due to the inclusion of noisy information. In contrast, if the number of hops is too small, the retrieved subgraph may be too small to include crucial knowledge required by tasks. To achieve a better trade-off between the size of the retrieved subgraph and the amount of its encoded task-relevant information, various graph pruning methods have been proposed to reduce the size of subgraphs by removing irrelevant nodes and edges while preserving the essential information.

*   **Semantic-based pruning**: Semantic-based pruning focuses on reducing the graph size by removing nodes and edge relations that are semantically irrelevant to the query. For example, QA-GNN prunes irrelevant nodes with low relevance scores by encoding the query context and node labels using LLMs, followed by a linear projection. GraphQA further removes clusters of nodes with the lowest relevance to the query. KnowledgeNavigator scores the relations in the retrieved graph based on the query and prunes irrelevant relations to reduce graph size. Additionally, partition the retrieved subgraph into smaller subgraphs and then ranks them with only the top-k smaller subgraphs retained for generations. G-Retriever defines a semantic score for each retrieved node and edge, then refines the graph by solving the prize-collecting Steiner tree problem to construct a more compact and relevant subgraph.
*   **Syntactic-based pruning**: Syntactic-based pruning removes irrelevant nodes from a syntactic perspective. For instance, leverages dependency analysis to generate a parsing tree of the context and then filters the retrieved nodes based on their span distance from the parsing tree.
*   **Structure-based pruning**: Structure-based pruning methods focus on pruning the retrieved graph based on its structural properties. For example, RoK filters out reasoning paths in the subgraph by calculating the average PageRank score for each path. Other works, such as and, also leverage PageRank to extract the most relevant entities.
*   **Dynamic pruning**: Unlike the aforementioned methods, which typically prune the graph once, dynamic pruning removes noisy nodes dynamically during training. For example, JointLK uses attention weights to recursively remove irrelevant nodes at each layer, keeping only a fixed ratio of nodes. Similarly, DHLK filters out nodes with attention scores below a certain threshold dynamically during the learning process.

#### 2.5.2 Reranker

The performance of LLMs can be influenced by the position of relevant information within the context, whether it appears at the beginning, middle, or end. Additionally, LLMs’ generation is impacted by the order in which in-context knowledge is provided, with later documents contributing less than earlier ones. While retrieved information is typically ordered by relevance scores during the retrieval process, these scores are often based on coarse-grained rankings across a large set of candidates. Enhancing reordering solely among the retrieved information at a fine-grained level, a process known as re-ranking, is essential to achieve optimal downstream performance. For example, rerank retrieved triples using a pre-trained cross-encoder. and employ pre-trained reranker models to rerank retrieved paths. train a GNN to rerank the retrieved passages. order the paths by the time they occurred, giving more emphasis to recent paths.

#### 2.5.3 Graph Augmentation

Graph augmentation aims to enrich the retrieved graph to either enhance the content or improve the robustness of the generator. This process can involve adding supplementary information to the retrieved graph, sourced from external data or knowledge embedded within LLMs. There are two main categories of methods:

*   **Graph Structure Augmentation**: Graph structure augmentation methods involve adding new nodes and edges to the retrieved graph. For instance, GraphQA augments the retrieved subgraph by incorporating noun phrase chunk nodes extracted from the context. Moreover, and treat the query as a node, integrating it into the retrieved graph to create direct connections between the query and relevant information. augment the graph structure based on pretrained diffusion models.
*   **Graph Feature Augmentation**: Graph feature augmentation methods focus on enriching the features of the nodes and edges in the graph. Since the original features might be lengthy or sparse, data augmenters can be employed to summarize or provide additional details for these features. For example, Once uses LLMs as Content Summarizers, User Profilers, and Personalized Content Generators in recommendation systems. Similarly, LLM-Rec and KAR apply various prompting techniques to enrich node features, making them more informative for downstream tasks.

Additionally, some graph augmentation techniques focus solely on the retrieved graph itself, such as randomly dropping nodes, edges, or features to improve model robustness. provide a systematic review of these data augmentation methods.

#### 2.5.4 Verbalizing

Verbalizing refers to converting retrieved triples, paths or graphs into natural language that can be consumed by LLMs. There are two main approaches to verbalization: linear verbalization and model-based verbalization.

Linear verbalization methods typically convert graphs into text using predefined rules. The primary techniques for linear verbalization include:

*   **Tuple-based**: These methods place the different pieces of retrieved information and order them in a tuple. For example, when performing retrieval on a KG, many methods retrieve a set of facts. A single fact is verbalized in the generation prompt as the tuple $(\text{entity } 1,\text{relation } 1,\text{entity } 2)$. For a set of facts, we first sort them in a specific order, and then verbalize them one at a time as an individual tuple. Each piece of information is typically separated by line in the prompt. Note that the same logic can be applied to paths, nodes, and so on.
*   **Template-based**: These methods verbalize paths or graphs using predefined templates to generate more natural text. For example, LLaGA proposes some templates such as Hop-Field Overview Template to convert graph into sequence. For KGs, several methods convert individual facts into natural text. For example, convert a fact (entity 1, relation, entity 2) to text using the template “The {relation} of {entity 1} is/are: {entity 2}”.

Model-based verbalization methods typically use fine-tuned models or LLMs to convert input facts into coherent and natural language. These methods generally fall into two categories:

*   **Graph-to-text verbalization**: These methods focus on converting retrieved graphs into natural language while preserving all the information. For instance, and leverage graph transformers to generate text from knowledge graph. evaluate several pretrained language models for graph-to-text generation, while, and fine-tune LLMs to transform graphs into sentences, ensuring a faithful representation of the graph content in textual form.
*   **Graph Summarization**: In contrast to Graph-to-Text Verbalization, which retains all details, Graph Summarization methods aim to generate concise summaries based on the retrieved graph and the query. EFSum proposes two approaches: one directly prompts LLMs to summarize the retrieved facts and query, while the other fine-tunes LLMs specifically for summarization tasks. CoTKR, on the other hand, alternates between two operations: Reasoning, where it decomposes the question, generates a reasoning trace, and identifies the specific knowledge needed for the current step; and Summarization, where it summarizes the relevant knowledge from the subgraph that retrieved based on the current reasoning trace.

### 2.6 Generator

The generator aims to produce the desired output for specific tasks based on the query and the retrieved information. These tasks can range from discrimination tasks (e.g., node/edge/graph classification) to generation tasks (e.g., KG-based question answering) and graph generation (e.g., molecular generation). Due to the uniqueness of different tasks, different generators are often desired. We categorize generators into three main types: Discriminative-based Generators, which leverage models like GNNs and Graph Transformers for tasks like classification; LLM-based Generators, which utilize the capabilities of LLMs to generate answers for text-based tasks; and Graph-based Generators, which generate new graphs using generative models such as diffusion models. Next, we provide a detailed illustration of these generators.

#### 2.6.1 Discrimination-based Generator

Discrimination-based generators focus on discriminative and regression tasks, which can typically be modeled as graph tasks, such as node, edge, or graph classification and regression. Models designed for graph data, such as GNNs and Graph Transformers, are widely used as discrimination-based generators. The choice of GNN depends on the graph type and task. For instance, GCN, GraphSAGE, and GAT are typically applied to homogeneous graphs, whereas models like RGCN and HAN are used for heterogeneous graphs, and HGNN and Hyper-Attention are suitable for hypergraphs. Additionally, graph transformers have gained popularity for their ability to capture global dependencies.
Additionally, different training strategies, such as (semi-)supervised learning and graph contrastive learning, are employed depending on the specific requirements of the task.

#### 2.6.2 LLM-based Generator

LLMs have demonstrated remarkable capabilities in understanding and generating natural language across a wide range of tasks. However, LLMs are inherently designed to process sequential data, while the retrieved information in GraphRAG is typically structured as graphs. Although various GraphRAG organizers, such as verbalization methods, convert retrieved graph information into text, these transformations may result in the loss of important graph structure information, which could be crucial for certain tasks. To take advantage of the ability of LLMs, many research efforts have been proposed to feed the graph information into LLMs, and we summarize them into the following categories:

*   **Verbalizing**: Verbalizing aims to convert the retrieved information in GraphRAG into sequences that can be processed by LLMs. These methods are detailed in Section 2.5.4.
*   **Embedding-fusion**: Embedding-fusion integrates graph embeddings and text embeddings within LLMs. The graph embeddings can be obtained using GNNs or Graph Transformers. To align graph embeddings with text embeddings, a domain projector is typically learned to map graph embeddings to the text embedding space. Embedding fusion can occur at different layers of LLMs. For example, feed the projected graph embeddings through the self-attention layers of LLMs, while prepend the projected graph embeddings with the text tokens. fuse the text and projected graph embeddings before the prediction layers of LLMs.
    Additionally, LLMs can either be fine-tuned along with the domain projector using methods such as LoRA, or the LLM can remain fixed, training only the graph embedding model and domain projector.
*   **Positional embedding-fusion**: Directly converting the graph into sequences by Verbalization may lose graph structure information, which can be crucial in some tasks. Positional embedding-fusion aims to add the position of nodes in the retrieved graph to the LLMs. GIMLET, as a unified graph-text model, employs a generalized position embedding to encode both graph structures and textual instructions as unified tokens. LINKGPT leverages the pairwise encoding in LPFormer to encode the pairwise information between two nodes.

#### 2.6.3 Graph-based Generator

In the scientific graph domain, GraphRAG generators often go beyond LLM-based methods due to the need for accurate structure generation. RetMol is particularly versatile because it can work with various encoder and decoder architectures, supporting multiple generative models and molecule representations. For example, generators can be transformer-based or utilize Graph VAE architectures. highlight the use of a diffusion model, specifically the 3D molecular diffusion model IRDIF. In the generation process, SE(3)-equivariance is achieved through architectures like Equivariant Graph Neural Networks (EGNNs), which ensure that the geometric properties of molecular structures remain invariant to spatial transformations such as rotation, translation, and reflection at each step. Incorporating SE(3)-equivariance into the diffusion model guarantees that the generated molecular structures maintain geometric consistency under these transformations. For KGs, multiple works use a GNN to generate the answer. The GNNs used in these works are conditional on the query, thereby making the final predictions relevant to it.

### 2.7 Graph Datasources

We have conducted a comprehensive review of the primary techniques applied in the initial four model-centric components of GraphRAG—namely, the query processor, retriever, organizer, and generator. However, even with the best configurations of these components, a GraphRAG system may still fall short of optimal performance if the underlying graph data sources, from which external knowledge is retrieved, are not meticulously curated. This also underscores the recent significant shift in AI research from a model-centric to a data-centric perspective, where enhancing data quality and relevance becomes equally, if not more, crucial for achieving superior results. Adopting this data-centric perspective, the following section provides an overview of existing GraphRAG research on constructing graph data sources from a high-level perspective, with a detailed discussion of domain-specific graph construction methods reserved for the subsequent domain-specific section.

*   **Explicit Construction**: Explicit construction refers to building graphs based on explicit and predefined relationships in the data. This method is widely adopted across various domains. For example, molecule graphs are constructed from the connections between atoms; knowledge graphs are formed based on explicit relationships between entities; citation graphs are built by linking papers through citation relationships; and recommendation graphs model interactions between users and items.
*   **Implicit Construction**: Implicit construction is used when there are no explicit relationships between nodes, but instead, implicit connections can be derived. For instance, word co-occurrence in a document can suggest shared semantic information, and feature interaction in Tabular data can indicate the correlation between features. Graphs can explicitly model these connections, which might be beneficial to the downstream tasks.

After the graph is constructed, there are also several ways to formally represent graphs.

*   **Adjacency matrix**: The adjacency matrix is one of the most popular ways to denote a graph. Specifically, the adjacency matrix $\mathbf{A}\in\mathbb{R}^{||\mathcal{V}\times|\mathcal{V}|}$ denotes the graph connections among nodes in $\mathcal{V}$, where $|\mathcal{V}|$ is the number of nodes.
*   **Edge list**: The edge list represents each edge in the graph, typically in the form of tuples or triples, such as $(i,j)$ or $(i,r,j)$, where $i$ and $j$ are nodes, and $r$ is the relation between nodes $i$ and $j$.
*   **Adjacency list**: The adjacency list is a node-centric representation where each node is associated with a list of its neighbors. It is typically represented as a dictionary $\{i:\mathcal{N}_{i}\}$, where $\mathcal{N}_{i}$ is the neighbor list of node $i$.
*   **Node Sequence**: A node sequence transforms a graph into a sequence of nodes in either an irreversible or reversible manner. Most serialization methods are irreversible and do not allow for complete recovery of the original graph structure. For example, there are also some serialization methods that are reversible which can recover the whole graph structure. For example, propose serializing graphs using Eulerian paths by first applying Eulerization to the graph. Besides, if the graph establishes a tree structure, the BFS/DFS can also serialize the graph in a reversible manner.
*   **Nature language**: With the growing popularity of LLMs for processing text-based information, various methods have been developed to describe graphs using natural language.

Note that the above-mentioned data structures can only represent basic graphs without support for complex scenarios such as multi-relational edges or edge attributes. For instance, using an adjacency matrix to represent a multi-relational attributed graph requires an expanded structure: $\mathbf{A}\in\mathbb{R}^{|\mathcal{V}|\times|\mathcal{V}|\times|\mathcal{R}|}$, where $\mathcal{R}$ denotes the set of possible relationships. Here, $\mathbf{A}_{i,j,r}$ represents the weight of the edge connecting node $i$ and node $j$ under relation $r$.

Selecting an appropriate graph representation is essential for task-specific requirements. For example, finds that the order of graph descriptions significantly impacts LLMs’ comprehension of graph structures and their performance across different tasks.

## 3 Knowledge Graph

A knowledge graph is a structured database that connects entities through well-defined relationships. It can either encompass a broad spectrum of general knowledge, such as the widely recognized Google Knowledge Graph, or delve deeply into specialized domains, like the BioASQ dataset for biomedical reasoning. The diverse information contained in a knowledge graph – represented as entities, relationships, paths, and subgraphs – serves as a valuable resource for enhancing various downstream tasks across different sectors, including question-answering, commonsense reasoning, fact-checking, recommender systems, drug discovery, healthcare, and fraud detection.

### 3.1 Application Tasks

This section reviews representative applications that GraphRAG on KGs is used for.

*   **Question-answering**: Question-answering (QA) can focus on a single domain or span across global knowledge. Typically, a query in text format is given, such as "What is the best way to predict a baby’s eye color?" or "Were there fossil fuels in the ground when humans evolved?" – the answer can be a sentence generated by a large language model (LLM), a selected text span from relevant documents, or even a specific choice in a multiple-choice QA scenario. In all these contexts, GraphRAG leverages knowledge graphs to retrieve relevant information, providing the necessary context or supporting facts to generate accurate answers.
*   **Fact-Checking**: Fact-checking is to verify the truthfulness of statements by cross-referencing them with reliable sources of information. GraphRAG enhances this task by querying a knowledge graph to retrieve relevant facts and relational structures that either support or refute the given claim. GraphRAG identifies discrepancies or confirmations within the data by mapping the statement onto the knowledge graph, providing a thorough and evidence-based validation process.
*   **Knowledge Graph Completion**: Knowledge graph completion is the task of predicting new facts to enhance the comprehensiveness of the graph and infer missing facts. GraphRAG addresses this task by retrieving structural knowledge around the triplets for inference, supplying essential structural knowledge, and enhancing the LLM inference.
*   **Cybersecurity Analysis and Defense**: Cybersecurity Analysis and Defense aims to analyze and respond to vulnerabilities, weaknesses, attack patterns, and threat tactics. With the increasing complexity and volume of cybersecurity data, GraphRAG has been proposed to provide cybersecurity analysis with more comprehensive insights into potential attack vectors and mitigation strategies.

### 3.2 Knowledge Graph Construction

We discuss how KGs are typically constructed. For each type of construction technique, we give examples of common KG databases. How a KG is constructed is important, as it can affect both its usefulness and function in different downstream tasks. We describe the main techniques below:

*   **Manual construction**: Some KGs are constructed manually via human annotation. WikiData is a KG that uses crowd-sourced efforts to gather a variety of knowledge. Each entity corresponds to a page in the Wikipedia encyclopedia. Another KG, the Unified Medical Language System (UMLS), contains biomedical facts collected from numerous sources.
*   **Rule-based construction**: Many traditional approaches use rule-based techniques for constructing the graph. This takes the form of custom parsers and manually defined rules used to extract facts from raw text. Note that these parsers can differ depending on the source of the text. Prominent examples include ConceptNet, which links different words together via assertions, and Freebase which contains a wide variety of general facts. REANO extracts the entities and relations from a set of passages using traditional entity recognition (ER) and relation extraction (RE) methods, respectively. This includes SpaCy for ER and TAGME for RE. To extract the facts that connect two entities via a relation, they use DocuNet.
*   **LLM-based construction**: Recently, work has explored how LLMs can be used to construct KGs from a set of documents. In such a way, the LLM can automatically extract the entities and relations and link those together to form facts in the given text. Of note is that no ground-truth KG exists for these methods. Rather, they simply use a KG as a way to organize and represent a set of documents. For example, CuriousLLM considers passages in the text as entities and determines whether two entities should be connected based on their encoded textual similarity. On the other hand, uses a manually-defined prompt to convert a piece of text into a KG. Graph-RAG first divides each document into chunks and then uses an LLM to detect all the entities in each chunk, including their name, type, and description. To identify the relation between any two entities, both entities and a description of their relationship are passed to an LLM. An LLM is then used again to summarize the content of each entity and relation to arrive at their final title. Lastly, AutoKG uses a combination of LLM embeddings and clustering techniques to construct a KG from a set of texts.

### 3.3 Retriever

Real-world facts in KGs can provide grounded information for generative models, enhancing the reliability of the model output. Given the structured nature of KGs, they are naturally well-suited for retrieval. The goal is for a given question or query to retrieve either relevant facts (Throughout this paper, we will refer to facts as triples or edges, interchangeably) or entities that can help answer that question. Multiple considerations need to be considered during retrieval, including the type of facts we want to retrieve, the efficiency, and the amount of facts retrieved. In general, retrieval of KGs has two stages: identifying seed entities and retrieving facts or entities. We describe both below.

**Identifying seed entities**: The first step in retrieving the relevant facts for a given query is to identify a set of “seed entities”, which we’ll refer to as $V_{\text{seed}}$. Seed entities are the initial entities that are chosen to be highly relevant to the original query. Given such, we expect that triples that contain any of these entities or are nearby in the graph should provide helpful context. Multiple techniques exist for identifying the seed entities. Some works assume that we are given a set of initial entities for each query. However, most works attempt to extract the entities from the query. One approach is through entity extraction, which uses methods specifically designed for extracting entities from a given text. Most works only extract entities from the original query. Another common approach is to extract a set of entities that are semantically similar to the original query. HyKGE first generates a hypothesis and extracts entities from the original query and the hypothesis. Similarly, in order to reduce the possibility of hallucination, uses an LLM to generate two similar questions and retrieves all entities found in the original and generated questions. In a similar vein, RoK first uses chain of thoughts reasoning to expand the original query, extracting the seed entities from the expanded query.

**Retrieval Methods**: The outcome of the previous step provides us with a set of entities that are related in some capacity to the query. These entities are then leveraged to retrieve a set of facts or entities that can aid us in answering the query. We summarize the core retrieval methods below.

*   **Traversal-based retriever**: These methods traverse the graph and extract paths to aid in answering a specific question. Given the set of seed entities, $V_{\text{seed}}$, extract all paths up to length two between the entities in $V_{\text{seed}}$, resulting in a final entity set $V$. They further augment $V$ by including all triples that connect any two entities in $V$. Given $V$, both only keep the top $k$ entities by relevance scores. This is calculated by training a separate model that takes the text embedding of the query and entity as input and outputs how relevant the entity is to the query. For, if $\lvert V\rvert>200$, they randomly sample 200 entities. use a version of beam-search to explore the KG. extract all paths of length $k\leq 2$ between seed entities. Alternatively, LARK retrieves all facts that lie on paths $\leq k$ in length starting from the seed entities. first extract the shortest paths connecting all seed entities. They further prioritize some entities over others by considering the recency, importance, and relevance to the query of their associated text. OREOLM traverse $k$ hops from the seed entities, contextualizing the importance of each relation and entity to a path via a learnable $d$-dimensional embedding and it’s LM-encoded representation. introduce a trainable retriever that traverses the graph starting from each seed entity. They also train a model to score each newly visited edge, only keeping a portion of them. KG-RAG works in a similar manner, scoring each edge by its relevance and similarity to the query via a dense retriever. They then use an LLM to decide which paths to explore in the next step.
    RoG uses instruction tuning to fine-tune an LLM to generate useful relation paths, which can be retrieved from the KG.
    KnowledgeNavigator first uses the query to predict the expected number of hops, $h_{Q}$ needed to traverse in the retrieval stage. It then traverses $h_{Q}$ hops starting from the seed entities, using an LLM to score and prune irrelevant nodes. operate in a similar manner; however, they choose which paths to traverse based solely on the relations. Furthermore, when scoring a path, all relations that lie on that path are considered when computing the score. RoK considers a different approach, using the Personalized PageRank (PPR) score to identify useful paths. They further augment these paths by including the 1-hop neighbors of the seed entities. PullNet assumes that each entity has an associated set of documents. Given a single seed entity, PullNet, traverses k hops, where in each iteration it extracts the facts for the newly observed entities. It also extracts any entities that are contained in documents associated with an entity found in the traversal. Furthermore, for each entity, only the top N facts are used, which are ranked via similarity to the query. KG-R3 uses MINERVA, a reinforcement learning approach to mining paths between entities, to retrieve a set of important paths between both entities in the fact.
    use an LLM to traverse the graph starting from the seed entities. At each iteration in the traversal, we choose the next node to visit by prompting an LLM. Specifically, given the information already collected in the traversal, the LLM is prompted to generate the remaining information needed to correctly answer the question. The neighboring node that best matches the required information is chosen as the next node to visit. They further instruction-tune the LLM.
*   **Subgraph-based retriever**: These methods extract a subgraph of size $k$ around each of the seed entities. Facts that contain one of the seed entities or are nearby, should be highly relevant to answering the question. Furthermore, they may actually contain the answer itself. Each of extract either the one or two hop subgraph around each seed entity. The final set of facts is the union of each individual subgraph. propose to first extract the subgraph containing the seed entity and potential answers using the method in. This is then partitioned into a set of smaller subgraphs. Then, they design a framework to rank the subgraphs, keeping the top $k$ subgraphs for generation. For a question-choice pair, MVP-Tuning considers the triple that contains the highest number of seed and choice entities. They further augment this by extracting the top $k$ most similar questions in the dataset using BM25, and extract the triples for each of them.
*   **Rule-based retriever**: These methods use pre-defined rules or templates to extract paths from the graph. GenTKG considers a temporal KG, where they first extract logical rules from the KG, and use the top k rules to extract paths in a given time interval for the seed entities. Both generate queries using SPARQL, which are then used to retrieve import paths. KEQING decomposes the original query into $k$ sub-queries using using an LLM fine-tuned via LoRA. For each sub-query, they find the most similar question templates, which are predefined. For each template, they further pre-define a set of logical chains, which are then used to extract matching paths for the seed entities in the sub-query from the KG.
*   **GNN-based retriever**: GNN-RAG trains a GNN for the retrieval task. A separate round of message passing is done for each query $q$, which is incorporated in the message computation along with the relation and entity representations. The GNN is then trained as in the node classification task, where the correct answer entity for $q$ has a label of 1 and 0 otherwise. During inference, the entities with probability above some threshold are treated as candidate answers, and the shortest path from the seed entity is extracted. use a conditional GNN for retrieval, where for each query, only the seed entity (they assume there is only one) is initialized to a non-zero representation based on the LLM-encoded query. They then run $L$ rounds of message passing where after each layer $l$ only the top-K new edges are kept, resulting in a set of entities $C_{q}^{l}$. This is determined by a learnable attention weight, which prunes the other edges from the graph. The final set of candidate entities is the union of candidate entities at each layer $l$, $C_{q}=\cup_{l=1}^{L}C_{q}^{l}$. It is optimized in a similar manner to. For each candidate entity, they retrieve an evidence chain by backtracking from the entity until it reaches the seed entity, choosing those edges with the highest attention weight.
    REANO initializes the entity and relation representations via the mean-pooled representations of all mentions of that entity/relation in the texts, encoded by T5. They then run a GNN, which includes an attention weight that considers the relevance of a given triple to the original question (also encoded by T5). After running the GNN, they retrieve the top K triples in the KG that are most relevant to the question, where relevance is defined via the dot product between the triple encoded by the GNN and the question.
*   **Similarity-based retriever**: STaRK considers the vector similarity of the query to each entity. Each entity embeds both the textual and relational information together. They further consider multi-vector similarity, where the entities are encoded using multiple vectors. This is done by chunking the textual and relational information of each entity, with each chunk being embedded into its own vector. Both REALM and EMERGE extract the entities most similar to the query. While REALM only retrieves the entities themselves, EMERGE further retrieves the 1-hop subgraph around each entity.
*   **Relation-based retriever**: propose a general framework for reasoning on KGs using LLMs. They first use an LLM to segment the original query into a set of $i\in I$ sub-sentences, where each sub-sentence $S_{i}$ has an associated set of entities $\mathcal{E}_{i}$. For each sub-sentence, they further use an LLM to retrieve the top-$k$ most relevant relations $\mathcal{R}_{i,k}$. Given the set of $k$ relations, for each sub-sentence, they retrieve all triples that contain a relation in $\mathcal{R}_{i,k}$ and whose entities are in $\bigcup_{i\in I}S_{i}$. GenTKGQA focuses on temporal KG QA. Like, they retrieve the top-k relations for the query. They then retrieve all facts that contain one of the top k relations and satisfy the temporal constraints.
*   **Fusion-based retriever**: These techniques consider a combination of different retrieval techniques. Mindmap considers extracting some paths $\leq k$ hops from the seed entity and the 1-hop subgraph of each seed. These two extracted components are combined into one subgraph. DALK uses a procedure similar to Mindmap, where they extract both paths and the 1-hop subgraph around each seed entity. However, they argue that this procedure often results in the retrieval of redundant or unnecessary information. To remove these facts, they use an LLM to rank the retrieved facts given both the original question and the subgraph. Only the Top-k most relevant facts are kept.
    UniOQA considers two branches for retrieving. The first is a translator, which is a fine-tuned LLM that generates the answer in a CQL format. the second is a searcher that retrieves the 1-hop subgraph around the seed entities. When determining the answer, answers from the translator are prioritized over those from the searcher. KG-Rank considers ranking all triples in the 1-hop neighborhood of the seed entities via the similarity of the relation to the query, the similarity of each triple to the encoded output of $a=\text{LLM}(q)$, and an MMR ranking that uses the similarity score. Only the top-ranked triples are kept. GrapeQA extends by further including a set of “extra nodes”, which are the common neighbors of the entities retrieved via a path-based retriever. They further introduce a clustering-based method for pruning entities that may be irrelevant to the query. SubgraphRAG considers both GNN and textual information. For the GNN, they consider initializing the node representations using a one-hot encoding to differentiate between seed entities and others. A GNN is then run for L layers, resulting in the final representation $s_{v}$ for a node $v$. To retrieve the relevant triples, they consider first concatenating the final node representations for each triple $(h,r,t)$ such that $z_{\tau}=[s_{h},s_{t}]$. The probability of choosing this triple is then given by $p(h,r,t)=\text{MLP}([z_{q},z_{h},z_{r},z_{t},z_{\tau}])$, where $z_{q}$, $z_{h}$, $z_{r}$, $z_{t}$ are the encoded textual representations of the query and the triple $(h,r,t)$, respectively. Only the top K triples are chosen.
*   **Agent-based retriever**: These techniques use LLM agents to retrieve facts from the KG. KnowledGPT defines a set of tools for searching over a KG. Given a query, they generate a piece of code to search over the KG that considers the seed entities. The code is then executed over the KG to find the correct answer. KG-Agent focuses on fine-tuning an LLM to generate the SQL code for retrieving the correct answer. Using a set of tools, they extract a set of paths that contain the seed entities. KnowAgent first identifies the relevant actions for the query via a planning module. Using these actions, they then generate a set of paths that are used for generation.
*   **Other retrievers**: KICGPT is concerned with the task of knowledge graph completion, where given a partial fact $(h,r,*)$, we want to predict the correct entity $\hat{e}$. KICGPT retrieves the entities by first scoring all possible entities using a traditional KG embedding score function. That is, for a score function $f(\cdot)$ and a partial fact $(h,r,*)$, they compute the set of scores $\{f(h,r,e)\;\forall e\in\mathcal{V}\}$. They use RotatE for the function $f(\cdot)$, a popular approach. Only the top $k$ entities by score are retrieved. To supplement their knowledge, they also retrieve all triples with (a) the same relation as the query and (b) all triples that contain the entity $h$ in the query. These are referred to as the analogous and supplement triple pools, respectively.

### 3.4 Organizer

In this subsection, we describe how the retrieved knowledge is organized for generation. More concretely, this is how the information is formatted when given to the generator. Note that not every method necessarily has an explicit organizer. We summarize the common methods below:

*   **Tuple-based organizer**: These methods consider each piece of retrieved information as an ordered triple. For example, it would include a triple in the generation prompt as “$(\text{entity } 1,\text{relation } 1,\text{entity } 2)$”. Similarly, a path of length $m$ is given by “$(\text{entity } 1,\text{relation } 1,\text{entity } 2,\text{relation } 2, \cdots,\text{entity } m)$”. The entities and relations are usually represented either as their names or IDs. Each triple or path is usually listed on a separate line. Many works append the retrieved paths to the original query as additional context. Other works that retrieve facts instead of paths operate in a similar manner, where instead they append the triples. Some methods consider only including the retrieved entities as the context. Given a set of facts, KG-R3 first lists all entities and then relations, i.e., “$(\text{entity } 1,\text{entity } 2,\cdots,\text{entity } m,\cdots,\text{relation } 1,\cdots,\text{relation } m-1)$”.
    consider a KG where each entity has an associated chunk of text. Each text chunk for an entity is considered as a different piece of information to be included in the context. Both represent each entity and relation as an embedding, which is the combination of the LLM and GNN embedding. further include the probability of each path containing the correct answer given by the GNN model. MVP-Tuning considers combining multiple facts that share the same subject and relation to remove redundant information. That is, for a subject-relation pair $(\text{subject},\text{relation})$, they denote the facts for $k$ possible objects as “$\text{subject}\>\text{relation}\>\{\text{object}\>1,\cdots,\text{object}\>k\}$”. KG-Agent stores the current KG information and the historical reasoning programs in lists.
*   **Text organizer**: verbalize the retrieved subgraph by passing each triple to the LLM and prompting it to convert it to a text representation. MindMap uses a similar procedure for subgraphs, where each is organized as a path before being passed to the LLM. Some methods use a set of pre-defined templates to verbalize the triples or paths. experiment with verbalizing either via an LLM or pre-defined question templates, finding that LLM-based verbalizing works better for ChatGPT while template-based works better for LLaMA. KICGPT uses a combination of data preprocessing and LLM prompting to convert the triples to text. StaRK uses an LLM to synthesize each entity with its relational and textual information. Note that they use some pre-defined templates that depend on the specific task. CoTKR uses an LLM to summarize and then re-write a subgraph of facts for a question through a “knowledge rewriter”. To train the rewriter, preference alignment is used, which optimizes the rewriter’s output to match our preferred output. First, $k$ representations of the retrieved subgraph are produced, with ChatGPT choosing the best and work representations as the most and least preferred solutions.
*   **Other organizer**: There are some exceptions to the previous classification. KnowledGPT represents the information in the form of a python class format. They also experiment with including additional information like the entity description and entity-aspect information.
*   **Re-Ranking**: Some methods also re-rank the information in a specific order. This is done as the order of information can have a subtle impact on LLM performance. order the text chunks of each entity based on the impact (measured by # of citations of the parent paper) and the recency. sort the triples by the relevancy score to the triple. attempt to order the paths in a logical matter, such that for a given path, the subsequent paths build upon it. re-rank the retrieved triples using a task-specific Cross-Encoder. STaRK considers re-ranking the retrieved entities using an LLM. The LLM is given the relational and textual information of each, and is asked to give it a score from 0 to 1, which is then used for re-ranking. GenTKG orders the paths by the time they occurred, further including the time with each. KICGPT ranks all entities using the score of the KG embedding score function, keeping only the top $k$ entities. KICGPT re-rank the entities using in-context learning, where they prompt the LLM with examples from the analogy and supplement pool, as prior knowledge to aid the LLM in how to re-rank the entities.

### 3.5 Generator

In this section we describe how the retrieved and organized data is used to generate a final response to the query. We categorize these generators according to the type of methods used to create these responses.

*   **LLM-based generator**: The vast majority of works use a LLM to generate the response. The input to the LLM is the original query and retrieved and organized context, formatted using a specific template. The most commonly used LLMs include ChatGPT, Gemini, Mistral, Gemma, among others. For open-source models where the weights are publicly available, fine-tuning is sometimes used to modify the weights for a specific task. This is often done through LoRA, which allows for efficient fine-tuning.
*   **GNN-based generator**: Some methods use graph neural networks (GNNs) to conduct the generation. extract both the language and GNN embeddings for each potential answer (i.e., entity) conditional on the query. The probability of a single entity being the answer is then learnt based on the fusion of the two types of embeddings.
*   **Other generators**: formulate the prediction as a masked language modeling (MLM) problem. The goal is to predict the correct value (i.e., entity) for the masked token which answers the query. To do so, they fine-tune RoBERTa language model. KG-R3 scores the potential answer entities by performing cross-attention the representations of the query and each individual entity.
    PullNet uses GraftNet to score the different entities. first selects the correct subgraph by computing the cosine similarity between the query and subgraph representations. For the subgraph with the highest similarity, it’s fed to GraftNet to select the most probable entity. REANO passes the encoded triples and their associated text passages to the T5 decoder. The task is framed as a classification problem, where the goal is to assign the highest probability to the triple with the correct answer.

### 3.6 Resources and Tools

In this section, we list common tools and KGs that are used in graph RAG systems. For each, we give a brief description and a link to the project.

#### 3.6.1 Data Resources

*   **Freebase** ([https://developers.google.com/freebase](https://developers.google.com/freebase)) is an encyclopedic KG that contains a large variety of general and basic facts.
*   **ConceptNet** ([https://conceptnet.io/](https://conceptnet.io/)) is a semantic graph, where the links in the graph are used to describe the meaning of different words or ideas.
*   **WikiData** ([https://www.wikidata.org/wiki/Wikidata:Main_Page](https://www.wikidata.org/wiki/Wikidata:Main_Page)) is a crowdsourced knowledge base that functions as a structured analog to the Wikipedia encyclopedia.

#### 3.6.2 Tools

*   **Graph RAG** ([https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)) is an official open-source implementation of the Graph RAG framework. It can further be installed via the graphrag python package.
*   **LangChain** ([https://python.langchain.com/v0.1/docs/use_cases/graph/constructing/](https://python.langchain.com/v0.1/docs/use_cases/graph/constructing/)) is an open-source framework for using LLMs with various components and applications, including RAG, where using RAG on KGs is supportive.

## 4 Document Graph

A document graph typically models the connections between different documents or various granularity of documents. It is widely observed in real-world scenarios, such as hyperlinks connecting different websites and citations linking one paper to another. Additionally, a document graph’s relationships between sentences and entities can explicitly capture semantic and syntactic contextual information. The structural information in documents can serve as a valuable resource for GraphRAG, aiding LLMs in various tasks. For example, in the retrieval process in RAG, the document containing the answer may have less apparent connections with the question, such as in multi-hop question answering. However, we can identify these relevant documents through their connections to other documents whose context is strongly aligned with the question’s context. In this section, we will systematically review the document graph.

### 4.1 Application Tasks

Document graphs are beneficial for a wide range of tasks. In this subsection, we will review the tasks where document graphs can play a significant role. Although document graphs have not yet been fully integrated with LLMs, they still offer great potential for enhancing the capabilities of LLMs in various applications.

*   **Multi-document Summarization (MDS)**: Multi-document summarization aims to condense the contents of multiple documents into a cohesive summary. Summarizing an entire corpus can involve large volumes of text, often exceeding the context window limitations of LLMs. Document graphs can help compress the corpus by extracting key components and their relationships, proving highly beneficial for MDS. These graphs also provide different levels of granularity for summarization through hierarchical clustering.
*   **Text generation**: Text generation focuses on producing coherent and meaningful text. While text-based RAG models have been widely used to generate more reliable text, document graphs can further enhance this process by retrieving similar documents using graph topology. For instance, when writing the abstract of a paper, access to its cited papers in the related work section can significantly improve writing efficiency, as these referenced papers often contain relevant knowledge and context.
*   **Document Retrieval**: Document retrieval aims to find a list of documents relevant to a given query, which is a key task in Information Retrieval (IR). The exact query terms may not always appear together in the candidate document; however, by leveraging the connections between documents, we can retrieve related documents through those documents that are strongly linked to the query. Thus, it becomes essential to consider document-level relationships in the retrieval process. Several works have leveraged document graphs with various granularities to improve document retrieval and ranking. Rather than retrieving the entire document, graphs can also be used to retrieve specific segments, such as chunks.
*   **Document Classification**: Document classification is a fundamental task in natural language processing. Traditional methods often focus on the locality of words, limiting their ability to capture long-distance and non-consecutive word interactions. Moreover, these methods typically focus on individual documents, overlooking the relationships between them, where connected documents often exhibit homophily, meaning they are more likely to share similar labels. Building a graph can help enhance document classification by leveraging both local and global relationships between words within a single document and by utilizing document-level relationships.
*   **Question Answering**: Question answering aims to provide answers to questions based on information from documents and is a fundamental task for RAG. However, documents used for question answering can be long, and traditional methods often focus on local structures within these documents, neglecting their global structure, which is crucial for long-range understanding. Additionally, some multi-hop questions require reasoning across multiple documents, necessitating the use of document-level relationships. Humans often consolidate scattered information into structured knowledge to streamline the reasoning process and make more accurate judgments, in line with cognitive load theory. Graph-based methods are well-suited for this task by constructing word-level document graphs, utilizing document-level relationships and leveraging hierarchical interactions.
*   **Relation Extraction**: Relation extraction aims to extract semantic relationships between entities in text, which often requires local, global, syntactic, and semantic dependencies, especially in the case of document-level relation extraction. Graphs have been proven to be helpful for document-level relation extraction by capturing these dependencies more effectively.
    In addition to the aforementioned tasks, graphs have also been shown to be helpful in other areas, such as fake news detection, coherence assessment, and machine translation.

### 4.2 Document Graph Construction

Different tasks may require different types of document graphs, such as document-level, sentence-level, or word-level graphs. Therefore, the method of obtaining the document graph plays a crucial role. There are primarily two approaches to constructing a document graph: explicit construction and implicit construction.

*   **Explicit Construction**. In real-world scenarios, many documents have explicit connections. Examples include web pages linked through hyperlinks, academic papers citing other works, and social media posts connected by reposts, comments, and interactions. In these cases, it is natural to connect the documents to build a document graph, as the connected documents often share semantic relationships. For instance, constructed a Wikipedia graph based on hyperlinks between Wikipedia articles. follow the same way to leverage hyperlinks to construct graphs. built a graph using an external knowledge graph (KG), where each node represents a retrieved passage mapped to entities within the KG, and two passage nodes are connected if their mapped entities are linked in the KG.
    These connections have been leveraged to pretrain large language models (LLMs), enhancing their performance across various tasks.
*   **Implicit Construction**. Despite the presence of explicit connections between documents, different components within those documents also exhibit important semantic and syntactic relationships. The structure of these components can be highly beneficial for various tasks in natural language processing. For example, semantic parsing graphs, such as Abstract Meaning Representation (AMR) graphs, can be leveraged to enhance information extraction and text summarization. Additionally, syntactic parsing trees are exploited to understand grammatical structure and resolve ambiguities.
    The implicit construction of document graphs is highly diverse, adapting to the specific requirements of different tasks. For instance, nodes in document graphs can represent various granularity, such as words, entities, sentences, text segments, paragraphs, documents, or topics. In addition, document graphs often exhibit heterogeneity, where edges connect different types of nodes. Next, we will detail the construction of different types of edges:
    *   **Word-word edge**: The word-word edges connect words with semantic or syntactic relations or dependencies. There are various methods to establish these connections, including word co-occurrence within a sliding window, dependency parsing graphs generated by NLP parsing tools, Abstract Meaning Representation and semantic graphs based on different representations. Additional techniques include coreference resolution, word embedding similarity and using large language models (LLMs) to extract relationships between words. For entities, the construction process is similar to that for words, though entity extraction methods are often required to first identify entities.
    *   **Word-Sentence edge**: Word-sentence edges connect words to sentences based primarily on the relationship of belonging. These edges are constructed by linking words to the sentences they appear in, with edge weights often measured using term frequency-inverse document frequency (TF-IDF). Besides, connects the entities with passage titles via hyperlinks with existing out-of-box entity linkers.
    *   **Sentence-Sentence edge**: Sentence-sentence edges connect sentences based on their semantic similarity or relationships. For example, these edges can be constructed through sentence interactions, similarities between TF-IDF representations, BM25, sentence embeddings, Part of speech (Pos) feature and N-Gram feature. Additionally, construct a Semantic Role Labeling (SRL) graph using AllenNLP-SRL model. This allows for connecting sentences within long documents or across different documents, which is particularly useful for LLMs with limited context length.
    *   **Sentence-document edge**: Sentence-document edges are constructed by linking sentences to the specific documents they belong to.
    *   **Document-document edge**: Document-document edges connect documents based on their similarities. These edges can be constructed when entities in one document are referenced or shared by another, through document clustering, embedding similarity, topic similarity or structural similarity.

Document graphs typically exhibit heterogeneity, consisting of multiple types of edges. In addition, several hierarchical graphs have been proposed, where different levels of abstraction are captured. The graph structure can also be dynamic or updated during the learning process. Moreover, the node in the document graph can also be the response of LLMs. For example, GoR connects the history responses of LLMs with the responding chunks of documents for long-context summarization.

### 4.3 Retriever

The retrievers for document graphs typically follow the general retriever design, as described in Section 2.4. However, there are some special retrieval methods as follows:

*   **Pre-Retrieval**: As introduced earlier, there are many scenarios where building a document graph is necessary. However, constructing a fine-grained graph for a large volume of documents can be inefficient and unnecessary. The pre-retrieval aims to first retrieve relevant documents based on the query and then construct a graph. For example, use pre-trained GloVe vectors to first extract relevant sentences and then construct a graph based on the retrieved sentences. also construct graphs based on the retrieved information.
*   **Graph similarity-based retriever**: Graph similarity aims to measure the similarity between two graphs. If both the query and the retrieval data source are graphs, calculating the graph similarity is essential to retrieve relevant information. For instance, leverages the General Maximum Common Subgraph (GMCS) method to retrieve related graphs.
*   **Iterative Retriever**: In certain tasks, such as multi-step question answering, the node containing the answer might not be directly similar to the query. Iterative retrievers address this by first retrieving nodes related to the query and then using the retrieved information to iteratively retrieve subsequent nodes. For example, utilize iterative retrieval methods for multi-step question-answering tasks, and iteratively retrieve the documents based on the existing knowledge graph. train a Recurrent Neural Network (RNN) to recurrently retrieve relevant information with the Bayesian Personalized Ranking (BRR) loss.
*   **Topology-based Retriever**: Various topological relationships in a graph can be used to measure different types of similarity. For example, proximity-based topological similarity measures the structural distance between two nodes, while role-based topological similarity assesses the similarity of the roles nodes play within the graph. These similarities can also be leveraged in the retrieval process.

### 4.4 Organizer

In this section, we describe the organizers for document graphs. GraphRAG on document graphs is still in its early stage, and many works do not incorporate explicit organizers, as shown in Section 2.5. We summarize the existing methods below:

*   **Graph Pruning**: Graph Pruning refines the retrieved subgraph to reduce irrelevant information and improve computational efficiency. For example, prune graphs based on the local clustering coefficient, while employs path-centric pruning to incorporate off-path information. dynamically drop irrelevant nodes during decoding, and prune edges based on a similarity threshold. Additionally, uses community detection algorithms to create distinct communities that are then fed into the generators.
*   **Reranking**: Reranking methods aim to reorder retrieved information to facilitate the generation. For example,, and use GNNs to rerank retrieved passages. perform listwise reranking to reorder passages expanded via the graph structure.

### 4.5 Generator

In this section, we summarize commonly used generators for document graphs. Various methods are applied within document graphs, depending on the input format. Some approaches use the entire graph as input, in which case GNNs and Graph Transformers are commonly employed. Other methods take individual sentences as input, where RNNs or (Large) Language Models are suitable. Additionally, some works leverage both graph and text as inputs, requiring integrated methods that can process multimodal data effectively. We detail each category in the following:

*   **GNN-based generator**: Numerous works model tasks as graph-related problems, leveraging GNNs as generators. Conventional GNNs, such as GCN, GraphSAGE, and GAT, are widely adopted in various studies. When graphs contain edge relations, Relational Graph Convolutional Networks (R-GCNs) are often used to capture these relationships effectively. In addition, some works incorporate graph contrastive learning techniques to enhance performance.
*   **Graph Transformer-based generator**: Graph transformers, which capture global information across the graph, are used to encode graph structures for various tasks. These models leverage the transformer’s self-attention mechanism to capture dependencies beyond local neighborhoods, making them well-suited for tasks requiring global context.
*   **RNN-based generator**: Recurrent Neural Networks (RNNs), such as LSTMs, are popular for processing sequences. Therefore, RNNs are employed when the input is in text form.
*   **LLM-based generator**: LLM-based generators typically transform the retrieved subgraph into text before using large language models (LLMs) for generation. Various models are used in this approach. For instance, BERT has been applied by to support generation tasks, while and leverage the T5 model, and use RoBERTa
*   **Integrated Generator**: Some works leverage both graph and text data simultaneously for generation, using integrated generators that combine graph models with text generation models. For example, and employ a combination of RoBERTa and GCN, while fuse GNN with T5 to harness the strengths of both graph structure and language model capabilities.

In addition to the aforementioned generators, some approaches embed graphs directly into text generation models. For example, proposes replacing traditional self-attention layers in transformers with graph-informed self-attention, enabling the model to integrate graph structure directly into the generation process.

### 4.6 Resources and Tools

The data resources for document GraphRAG can include any type of document, and thus, we do not provide a comprehensive list here. Instead, in the following, we introduce several tools specifically designed or commonly used for GraphRAG on document graphs:

*   **CoreNLP**: ([https://github.com/stanfordnlp/CoreNLP](https://github.com/stanfordnlp/CoreNLP)) The Stanford CoreNLP natural language processing toolkit offers a comprehensive set of natural language processing tools, including token and sentence boundaries, parts of speech, named entities, numeric and time values, dependency and constituency parses, coreference, sentiment, quote attributions, and relations. These tools are valuable for constructing document graphs.
*   **spaCy**: ([https://github.com/explosion/spaCy](https://github.com/explosion/spaCy)) The spaCy is an advanced natural language processing library known for its speed and neural network models, which are optimized for tasks such as tagging, parsing, named entity recognition, text classification, part-of-speech tagging, dependency parsing, sentence segmentation, lemmatization, morphological analysis, and entity linking.
*   **BLINK**: ([https://github.com/facebookresearch/BLINK](https://github.com/facebookresearch/BLINK)) BLINK is an entity linking python library that uses Wikipedia as the target knowledge base.
*   **OpenIE** ([https://github.com/dair-iitd/OpenIE-standalone](https://github.com/dair-iitd/OpenIE-standalone)): Open Information Extraction (OpenIE) is a tool for extracting structured information from text. It is valuable for generating triples from unstructured text, which can be used as nodes and edges in document graphs.
*   **CogComp NLP** ([https://github.com/CogComp/cogcomp-nlp](https://github.com/CogComp/cogcomp-nlp)): Developed by the Cognitive Computation Group, this suite includes tools for natural language processing tasks such as named entity recognition, sentiment analysis, and coreference resolution.
*   **GraphRAG** ([https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)): GraphRAG is a data pipeline and transformation suite that is designed to extract meaningful, structured data from unstructured text using the power of LLMs. The process involves extracting a knowledge graph out of raw text, building a community hierarchy, generating summaries for these communities, and then leveraging these structures when performing RAG-based tasks.
*   **LangChain** ([https://www.langchain.com/](https://www.langchain.com/)): LangChain is a framework for developing applications powered by LLMs, with use cases in document analysis and summarization, RAG, chatbots, and code analysis. Notably, LangChain supports Graph Transformers, which convert documents into graph-structured formats, making it highly suitable for processing document graphs.
*   **Neo4j** ([https://neo4j.com/](https://neo4j.com/)): Neo4j is a graph database platform offering comprehensive tools for storing, visualizing, managing, and querying graph data. It includes an LLM Graph Builder, which can extract graphs with LLMs. It also provides GraphRAG demos to demonstrate how to implement a LLMs and RAG system with Neo4j.
*   **LlamaIndex** ([https://www.llamaindex.ai/](https://www.llamaindex.ai/)): LlamaIndex is a data framework designed to support the development of applications based on LLMs. It allows developers to seamlessly integrate data sources, ranging from various file formats to applications and databases, with LLMs. LlamaIndex features an efficient data retrieval and query interface, enabling developers to input any LLM prompt and receive context-rich, knowledge-enhanced outputs. Notably, it includes a Property Graph Index that facilitates the building, modeling, storage, and querying of graphs.
*   **Haystack** ([https://haystack.deepset.ai/](https://haystack.deepset.ai/)): Haystack is an end-to-end framework for building applications powered by LLMs, Transformer models, vector search, and more. It supports a variety of use cases, including RAG, document search, question answering, and answer generation. Haystack enables the orchestration of state-of-the-art embedding models and LLMs into custom pipelines for creating comprehensive NLP applications. Additionally, it supports Neo4j as a DocumentStore, making it suitable for document graph storage and query operations.

## 5 Scientific Graph

Scientific graphs refer to graph-structured data used in domains such as drug discovery and biomedicine, both of which are common application areas for GraphRAG. Therefore, in this section, scientific graphs specifically refer to molecular graphs and medical graphs.

In recent years, significant progress has been made in the development of artificial intelligence for science. Machine learning (ML) and deep neural network technologies are increasingly driving scientific discovery from experimental data. Notably, generative models such as Large Language Models (LLMs) have achieved remarkable success in working with scientific graph data, including molecular graphs and biomedical graphs. In molecular graphs, for example, atoms serve as nodes, while chemical bonds represent edges, capturing the structure of molecules. AI technologies can handle both prediction and generation tasks on these graphs, driving advancements in fields like drug discovery.

Despite the impressive capabilities of generative models like LLMs, several challenges still hinder their applications to scientific domains. One of the most prominent challenges is the lack of domain-specific expertise. In fields like drug discovery, molecule generation is crucial, yet traditional generative models often struggle with producing incorrect or scientifically invalid structures. In medical question-answering (QA) tasks, incorrect answers, hallucinations, and limited interpretability are frequently encountered. To address these challenges, recent works have proposed leveraging external knowledge databases to enhance generation via GraphRAG. GraphRAG improves accuracy by retrieving relevant scientific graphs from extensive databases to guide the generation or answering process. This approach ensures scientific validity by incorporating known valid graph structures, leverages existing knowledge for practical applications, and accelerates the generation process by narrowing the search space.

### 5.1 Application Tasks

Scientific graphs are beneficial for a wide range of tasks. In this subsection, we will review some representative tasks where scientific graphs can play a significant role.

*   **Molecule generation**: Molecule generation refers to the process of creating or designing new molecular structures, often using generative models. It plays a crucial role in fields like drug discovery. The use of scientific graphs, especially molecular graphs, can enhance the rationality and accuracy of generated molecular structures in molecular generation. Typically, an inquiry such as a molecule is given to retrieve the most relevant molecular structures to guide molecular generation.
*   **Molecule property prediction**: Molecule property prediction refers to the use of computational methods to estimate the physical, chemical, or biological properties of molecules based on their structure.
    It has proven highly effective in accelerating the drug discovery process while significantly reducing associated costs. The use of scientific graphs, especially molecular graphs, can enhance the accuracy of prediction. To achieve this, a query molecule is provided, and similar molecules are identified as demonstrations to improve the prediction.
*   **Question answering**: Question answering (QA) in the scientific domain refers to the use of computational methods to provide accurate and context-specific answers to scientific questions. This involves retrieving or generating information from scientific literature, databases, or other resources to address complex, domain-specific queries, such as "After meals, I feel a bit of stomach reflux. What medication should I take for it?" In graghRAG, the scientific literature is usually converted into a knowledge graph to provide a basis for answering questions or to enrich the query.

### 5.2 Scientific Graph Construction

In GraphRAG, the choice and construction of data sources are crucial and typically include both public and private datasets. Public datasets are often derived from widely recognized resources, such as molecular databases like PubChem, ChEMBL, and ZINC, as well as biomedical literature and data sources like PubMed and ClinicalTrials. These datasets provide a broad foundation of information across various domains, offering reliable and authoritative references for the model.
On the other hand, private datasets contain user-specific information, such as medical records from hospitals or confidential clinical trial data. These datasets are highly confidential and unique, enabling GraphRAG models to offer personalized and proprietary knowledge support.

For chemistry, molecules can be represented in four main forms: 1D SMILES (Simplified Molecular Input Line Entry System), 2D molecular graphs, 3D molecular graphs with coordinates, and text captions describing molecular structures.
1D SMILES is a linear string generated through depth-first search (DFS) on the molecular graph, following specific rules.
2D molecular graphs represent atoms as nodes and bonds as edges, visually showing the connectivity of atoms.
3D molecular graphs incorporate spatial coordinates for each atom, reflecting the molecule’s structure in three-dimensional space, which is crucial for tasks such as molecular docking and reaction prediction.
Text captions, on the other hand, provide a natural language description of the molecular structure, which can be used in tasks that involve textual data interpreting chemical structures from text. Scientific graphs can typically be constructed as follows:

*   **Text-based construction**: Text-based graph construction is the most commonly used method, which can transform textual scientific knowledge into knowledge graphs. believe that text captions suffer from issues of information redundancy and imbalance. By constructing text as a knowledge graph, it is possible to rebalance the retrievable information and reduce redundancy.
    Building a knowledge graph typically involves two key steps:
    *   **Entity Extraction**: This step involves identifying and extracting key entities from the text, such as domain-specific terms (e.g., chemical compounds, genes).
    *   **Relationship Extraction**: After identifying the entities, the next step is to extract the relationships between these entities, determining how they are linked in the given context (e.g., "A is related to B"). This step forms the structural backbone of the knowledge graph.
*   **SMILES-based construction**:
    Many chemical databases store data in analytical descriptor formats such as SMILES. To model graphs, SMILES representations need to be transformed into graph structures.
    SMILES-based construction utilizes a library such as RDKit to read the SMILES notation, create a molecular object, and extract atomic and bonding information to construct a 2D graph. Each atom in the molecule is represented as a node, and each bond is represented as an edge between nodes. The atoms carry features such as atom type, degree, charge, and aromaticity, while the bonds can include bond type (single, double, etc.) and whether they are part of a ring.
*   **3D graph construction**:
    introduce IRDIFF, an interaction-based retrieval-augmented 3D molecular diffusion model designed for target-specific molecule generation. For pretraining, PMINet is utilized to capture interactive structural context information with binding affinity signals, leveraging the PDBbind v2016 dataset. This dataset offers 3D protein structures and a substantial set of experimentally validated protein-ligand complexes. These protein structures are primarily obtained via techniques like X-ray crystallography, nuclear magnetic resonance (NMR), or cryo-electron microscopy, containing detailed atomic coordinates, bond angles, and secondary structure information.

### 5.3 Retriever

The retriever is responsible for locating relevant information based on the input query. In GraphRAG, this information typically consists of graph-structured data. The retriever can be roughly classified as heuristic-based retriever and deep learning-based retriever.

*   **Heuristic-based retriever**: A heuristic-based retriever employs predefined rules, algorithms, and heuristics to identify and retrieve relevant knowledge from graph-structured data sources. Heuristic-based retrieval can be categorized into several types as below:
    *   **Similarity-based retriever**: retrieve exemplar molecules based on their similarity to the input molecule, using cosine similarity as the metric. MindMap encodes the entities from the query and the external knowledge graph into dense embeddings using BERT, and then retrieves the entity set with the highest similarity scores.
    *   **Matching-based retriever**: A matching-based method provides an alternative approach, enabling LLMs to generate evidence-based responses by leveraging comprehensive private data. Specifically, identify the most relevant graph through a top-down matching process. Once the relevant content is identified, the LLM generates an intermediate response with its assistance, enhancing both the transparency and interpretability of the results.
    *   **Knowledge graph-based retriever**: A knowledge graph-based method can effectively identify and retrieve the necessary information to respond to a query. use named entity recognition and relation extraction to connect user queries with relevant entities in the knowledge graph, thereby uncovering interpretable and actionable insights from existing biomedical knowledge. This approach significantly enhances the transparency and utility of predictive models. map the text chunks to the knowledge graph, then utilize graph distances to find the chunks most relevant to the user’s question. In addition, this work introduces a scoring metric that balances the data by giving each concept mapped along the shortest path an equal opportunity. This metric prioritizes text chunks based on both their recency and their impact. HyKGE first queries the LLM to generate a hypothetical output and extracts entities from both the output and the query. Then, HyKGE retrieves reasoning chains between any two anchor entities in an existing knowledge graph, such as CMeKG and CPubMed-KG, and feeds the reasoning chains along with the query into the LLM. KG-Rank identifies entities within the query and retrieves the related triples or sub-graphs from the KG to gather factual information.
    *   **Fusion-based retriever**: begins by retrieving the relevant node in the knowledge graph based on vector similarity to the query’s entity. Then, it retrieves the context triples (Subject, Predicate, Object) linked to this node within the knowledge graph.
*   **Deep Learning-based Retriever**:
    Deep learning-based retrievers can extract relevant knowledge to guide the generation process, such as the generation of molecules or proteins. Specifically, uses a pre-trained protein-molecule interaction network named PMINet to extract interactive structural context information between the target protein and ligands in the reference pool to guide the generation of target-aware ligands.
    utilize the off-the-shelf MedCPT retriever, a tool specifically tailored for retrieving documents in response to biomedical queries, capable of retrieving up to ten relevant pieces of evidence for each input. DALK filters out noise and retrieves the most relevant knowledge by utilizing the ranking capabilities of LLMs.

### 5.4 Organizer

Basically, there are two types of the organizer: embedding-based and query-based organizers according to how the retrieved knowledge is utilized.

*   **Query-based organizer**. The simplest and most direct organizer is a query-based organizer, which integrates the retrieved information with input queries to generate responses. Specifically, HyKGE enhances the reasoning process by incorporating external knowledge into the large language model. In this framework, the retrieved reasoning chains are fed into the LLM alongside the original query. This enables the model to ground its responses in structured, contextually relevant information, improving both the accuracy and depth of the generated output. prompt the LLM to answer the question by providing the retrieved entity names and their relationships in a concatenated form. This approach involves retrieving relevant entities and the relationships between them from an external knowledge source and structuring this information as a cohesive input for the LLM. DALK integrates the query and retrieves knowledge and then feeds it into LLMs for reasoning and getting the predicted answer. Similarly, KG-Rank combines the re-ranked triplets with the task prompt and inputs them into LLMs for answer generation. In contrast to the methods mentioned above, begin with context pruning. Specifically, this approach refines the retrieved context by selecting only the most semantically relevant elements needed to answer the query promptly. The input prompt is then combined with this pruning-aware information, producing an enriched prompt that is fed into the LLM for text generation. develop a data rebalancing mechanism to ensure that each entity relevant to a question has an equal opportunity of being represented while also highlighting recent significant discoveries. This rebalanced knowledge is then combined with the query prompt and provided as input to the LLM.
*   **Embeding-based organizer**. Embedding-based organizer integrates the retrieved information with input embedding to generate responses. Specifically, uses a lightweight, trainable standard cross-attention mechanism to fuse the embedding of the input molecule and the retrieved example molecules. Similarly, uses a trainable cross-attention mechanism to fuse the enhanced embeddings of the retrieved example ligands and the generated molecules.

### 5.5 Generator

The generator is a core component of the GraphRAG model and is responsible for producing the final output by integrating retrieved evidence with the input data.
Generators can be broadly classified into three categories according to the type of generated models they use: transformer-based generators, diffusion model-based generators, and large language models-based generators.

*   **Transformer-based generator**: RetMol utilizes the Megatron version of the molecule generative model Chemformer for drug discovery. Specifically, the Chemformer model is a Transformer-based model that can be efficiently applied to tasks in chemistry.
*   **Diffusion-based generator**: introduce a novel interaction-based retrieval-augmented diffusion model (IRDIFF) for structure-based drug design. Specifically, IRDIFF is able to generate molecules that bind strongly to the target pocket by utilizing protein-molecule interaction data between reference proteins and the target protein to guide the diffusion model.
*   **LLM-based generator**: Some approaches leverage large language models, such as LLaMA2, LLaMA3, GPT-4, and Gemini, etc. For instance, MedGraphRAG utilizes GraphRAG to improve the answering capabilities of models such as LLaMA2, LLaMA3, Gemini, and GPT-4 for medical question answering. MolecularGPT utilizes GraphRAG to improve GPT-3’s predictive capabilities for molecular property prediction. DALK employs GraphRAG to boost GPT-3.5-turbo’s ability to answer questions related to Alzheimer’s Disease. HyKGE utilizes GraphRAG to enhance the medical question-answering capabilities of GPT-3.5 and Baichuan13B.

### 5.6 Resources and Tools

In this section, we provide an overview of common data sources and tools utilized in graph RAG systems within the scientific domain, along with a brief description of each project.

#### 5.6.1 Data Resources

The public datasets are commonly from well-known resources, such as molecular databases:

*   **PubChem**: PubChem encompasses a wide range of chemical data, including 2D and 3D structures, chemical and physical properties, bioactivity, pharmacology, toxicology, drug targets, metabolism, safety guidelines, associated patents, and scientific literature. Most of its entries pertain to small molecules, with a primary emphasis on those containing fewer than 100 atoms and 1,000 bonds.
*   **ChEMBL**: It is an openly accessible database containing detailed information on drugs, drug-like small molecules, and their bioactivity. This curated resource stands out for its comprehensive coverage of the drug discovery process, encompassing data on more than 2.2 million compounds and over 18 million records documenting their effects on biological systems.
    ChEMBL provides insights into the interactions between small molecules and their protein targets, along with data on how these compounds influence cellular and organismal functions. It also includes information on ADMET (absorption, distribution, metabolism, excretion, and toxicity) profiles. The database stores two-dimensional structures, calculated molecular properties (such as logP, molecular weight, and Lipinski’s Rule of Five parameters), and bioactivity data like binding affinities and pharmacological effects.
*   **ZINC**: The ZINC dataset is a curated collection of commercially available chemical compounds designed specifically for virtual screening purposes. It offers over 230 million purchasable compounds in 3D formats that are ready for docking, as well as more than 750 million compounds available for analog searches. Each molecule is adjusted to biologically relevant protonation states and is annotated with properties such as molecular weight, calculated LogP, and rotatable bonds. The library includes vendor and purchasing details, making it compatible with several widely used docking software programs. Compounds are provided in multiple protonation states and tautomeric forms within certain constraints, and some formats even offer multiple conformations per molecule. The ZINC database is available for free download ([http://zinc.docking.org](http://zinc.docking.org)) in multiple common file formats, including SMILES, mol2, 3D SDF, and DOCK flexibase.

There are also biomedical data sources as below:

*   **PubMed**: PubMed is a freely accessible database that primarily houses the MEDLINE collection, containing references and abstracts in life sciences and biomedicine. Managed by the United States National Library of Medicine (NLM) within the National Institutes of Health, PubMed is part of the Entrez retrieval system. As of May 23, 2023, PubMed contains over 35 million citations and abstracts, with records dating back to 1966 and selectively to 1865, and a few even to 1809. On this date, approximately 24.6 million records include abstracts, and 26.8 million provide links to full-text articles, with around 10.9 million available freely. In the last decade (up to December 31, 2019), PubMed added nearly one million new records annually on average.
*   **ClinicalTrials**: ClinicalTrials is a global registry and database that provides information on clinical studies funded by both private and public sources. Managed by the U.S. National Library of Medicine, this resource includes a summary of each study’s protocol, and for some studies, results are available in a tabular format. Users can search studies by criteria such as study status, condition or disease, country, and other keywords. Continuously updated, the database now includes over 300,000 research studies conducted across all U.S. states and in more than 200 countries worldwide.
*   **Open-source medical KGs**: CMeKG (Clinical Medicine Knowledge Graph) ([https://cmekg.pcl.ac.cn/](https://cmekg.pcl.ac.cn/)), CPubMed-KG (Large-scale Chinese Open Medical Knowledge Graph) ([https://cpubmed.openi.org.cn/graph/wiki](https://cpubmed.openi.org.cn/graph/wiki)) and Disease-KG (Chinese disease Knowledge Graph) ([https://github.com/nuolade/disease-kb](https://github.com/nuolade/disease-kb)) are open-source medical knowledge graphs that consolidate a vast amount of medical text data, covering areas such as diseases, medications, symptoms, and diagnostic treatments. The combined knowledge graph includes 1,288,721 entities and 3,569,427 relations.

#### 5.6.2 Tools

*   **RDKit**: RDKit is open-source toolkit for cheminformatics. RDKit has several key features: it can process chemical structures by reading and writing various file formats, such as SMILES, InChI, and Mol files. It generates multiple types of molecular fingerprints, enabling chemical structure comparison and similarity searches. RDKit also provides algorithms for calculating molecular similarity and supports the representation and processing of chemical reactions, including the identification of reactants and products. Although it does not offer molecular docking capabilities on its own, RDKit can be integrated with other docking tools. Additionally, RDKit supports machine learning algorithms, allowing for pattern recognition in chemical data and the construction of predictive models.
*   **CADRO**: The Common Alzheimer’s and Related Dementias Research Ontology (CADRO) ([https://iadrp.nia.nih.gov/about/cadro](https://iadrp.nia.nih.gov/about/cadro)) is employed to extract a subset of Alzheimer’s disease (AD)-related samples from the medical QA datasets for evaluation. CADRO organizes terms into a three-tiered classification system with eight main categories and multiple subcategories focused on AD and related dementias, containing frequently used terminologies or keywords in the field. From CADRO, users obtain a list of AD-related keywords most relevant to the medical QA datasets.

## 6 Social Graph

The social graph typically consists of entities connected by their social relations and is ubiquitous across real-world applications. A primary example is social networks like Twitter and Facebook, where entities represent individuals linked by social interactions (e.g., friendships, followers/followees, likes, and mentions). These social graphs extend beyond human interactions and are not confined to living entities, such as tortoises co-using the same burrow in animal social networks, complementary products co-purchased by the same customer in E-commerce recommender systems, or even the LLM-simulated social agents. The wealth of social-relational knowledge in these social graphs is the golden resource for GraphRAG, which is reviewed in this section.

### 6.1 Application Tasks

*   **Entity Property Prediction**:
    Entity property prediction focuses on predicting properties and classifying categories for social entities in social networks, examples of which include the prediction of partnership compatibility, assessment of morality, detection of account suspensions, identification of toxic behaviors and product property prediction.
*   **Text Generation**:
    Text generation aims to produce text that aligns with social contexts and norms. Typically, the interplay between structural and textual information, such as proximity-based network homophily and role-based similarity, serves as the foundation for text generation. For instance, retrieves the texts of proximity/role-similar nodes to enhance the text generation of the target node. generate personalized recommendation explanations by retrieving customers’/products’ historical reviews. In addition, some other works also leverage semantic similarity to retrieve reference/attributes/opinions and augment the downstream review generation.
*   **Recommendation**:
    The recommendation task aims to find the most relevant items to satisfy user demands. Due to the missing and sparse customer/item interactions (e.g., cold-start issues), GraphRAG can be naturally applied to boost customer/item sparse interaction by retrieving additional meta-knowledge. Depending on the concrete recommendation scenario, GraphRAG has been used for graph-based recommendation, next-item recommendation, and conversational recommendation
*   **Question-answering**: Question-answering tasks are encountered not only in knowledge and document graph domains but also in social graphs. For example, a user might ask, "What are the best parks for family gatherings around Los Gatos?" and expect a personalized query answer. Furthermore, such questions might explicitly require graph-structured reasoning. For instance, build a semi-structured knowledge base, and some queries might ask, "Can you list the products made by Nike?" Answering this question requires not only a deep understanding of the query but also familiarity with the structural information of the data.
*   **Fake News Detection**: Detecting fake news necessitates considering both semantic content (e.g., the content of the news) and structural interactions (e.g., interactions among news). For instance, evaluates the credibility of a Reddit post based on the credibility of other Reddit posts retrieved by their common interactions with the same common commenters.

### 6.2 Social Graph Construction

The relations that GraphRAG leverages to derive additional information from social graphs can be mainly summarized into three rationales: proximity-based, role-based, and personalization-based rationale. The proximity-based rationale, rooted in the adage "birds of a feather flock together," suggests that nodes close to each other in a social network often share similar properties. For example, close friends tend to possess similar hobbies. The role-based rationale focuses on nodes with similar local subgraph structures sharing similar features or label distributions. For example, managers at the same hierarchical level within a company generally have comparable job titles and responsibilities, and hub airports exhibit similar operational characteristics and strategic importance. Lastly, the personalization-based rationale refers to individuals’ uniqueness regarding their characteristics and interactions. For example, in recommender systems, users interact with items in various ways, such as clicking, viewing, adding to a cart, purchasing, and reviewing, each interaction providing valuable knowledge that GraphRAG can leverage to personalize generated content. Based on the above three relational rationales in the social graphs, the social graph construction methods can be summarized as follows:

*   **User-User-Interaction**: This type of social graph represents user-to-user interactions commonly seen on social networks such as Twitter, Reddit, and Facebook. Examples include follower-followee relationships on Twitter, friendship relationships on Facebook, and user comments on other users’ threads on Reddit. Note that this user-user interaction naturally exists in the real world without human curation or modification compared to documents or knowledge graphs.
*   **User-Item-Interaction**: This type of social graph represents user-to-item interactions commonly found on e-commerce platforms like Amazon and eBay. These interactions, including purchasing, adding-to-the-cart, and viewing, can be modeled as a bipartite graph, where each type of interaction reflects a unique user intention.
*   **Item-Item-Interaction**: This social graph captures interactions between items, typically identified by shared interactions from the same customer or user. For example, a "co-view" interaction between two products indicates that they are viewed by the same customer, while a "view-add-to-cart" interaction indicates that one product is first viewed and the other is added to the cart next by the same customer. In e-commerce networks, these co-interactions between two items can be broadly categorized into complementary and substitute relationships.
*   **Metadata-Interaction**: Items and users often possess metadata. For example, products on platforms like Amazon may include brand, manufacturer, and color attributes. This metadata can be represented as additional node types and the corresponding edges indicating relations between products and attributes, such as ownership or association.
*   **Agent-Agent Interaction**: With the increasing intelligence of LLMs, recent literature has explored the potential of using LLM-powered agents to simulate social behaviors, such as collaboration, debate, and reflection. These agent-agent interactions could also be used for GraphRAG.

Note that among the five types of interaction mentioned above, the user-user, user-item, and metadata relations are naturally formulated without human curation. In contrast, item-item interactions are generated by manual extraction, and agent-agent interactions require simulations.

### 6.3 Retriever

The relations of the social graphs constructed according to the above methods can be leveraged in GraphRAG to enhance downstream tasks by retrieving additional information. For example, retrieving historical metadata and customer interactions can improve recommendations. Next, we review representative retrieval methods in GraphRAG for social graphs.

*   **ID-based Retriever**: Similar to entity linking, the ID-based retriever works by retrieving content specifically generated by a user/item, examples of which include retrieving historical item interactions of a specific customer, reviews posted on a specific product, and meta-data information about a specific user.
*   **Filtering-based Retriever**: Based on the ID-based retriever, the Filtering-based Retriever retrieves additional content based on collaborative filtering. For user filtering, Top K users are identified by comparing the similarity of their historical item interactions with those of the target user demanding recommendation. To enhance the context of the target user, it retrieves the most popular items from those Top K users. In contrast, for item filtering, it identifies the Top K items that are most similar to the current item by comparing their user-interaction history. Among them, the most popular ones would be fetched to augment the current item recommendation.
*   **Social Relational Retriever**: Like the ID-based Retriever, the Social Relational Retriever focuses on retrieving knowledge from entities sharing certain relations with the target entities on hand. For example, hierarchically retrieve neighboring texts several hops from the central node to augment the semantic information of the target user/item. Meanwhile, retrieve texts corresponding to nodes that share high proximity-based and role-based similarity, respectively.
*   **Integrated Neural-Symbolic Retriever**: This approach leverages both symbolic and neural retrievers to improve retrieval effectiveness. The symbolic retriever retrieves information by following explicitly defined rules, such as retrieving based on identifiers, structured relationships, or interaction patterns, ensuring that the retrieved data strictly aligns with specific criteria. Meanwhile, the neural retriever complements this by using embedding-based similarity, capturing nuanced patterns and contextual relationships that may not be directly encoded in rules. Integrating them together provides a better trade-off between rule-based precision and neural-based adaptability and generalizability. For instance, first retrieve K-hop neighboring products from the product knowledge graph (symbolic retriever) for products in the user session and further utilize neural-based adaptive filtering to aggregate items that are most relevant to the current sequence (i.e., neural retriever). Similarly, address data sparsity and heterogeneity by combining ID-based retrieval that retrieves movies based on the user ID of one party with a text-based retriever that enables movie retrieval between parties.

### 6.4 Organizer

To further enhance the retrieved content, the organizer for the social graphs employs specialized techniques beyond the typical re-ranking and filtering used in other graph domains. For social graphs, the organizer of GraphRAG often uses Keyword Extraction, Profile Summarization, and Hierarchical Graph Aggregation to curate the retrieved content:

*   **Keyword Extraction**: Keyword extraction identifies the most relevant and informative keywords from the retrieved content. These extracted keywords guide the downstream generator in prioritizing attention and reduce the risk of overwhelming LLMs with excessive context. For example, use an embedding estimator to pinpoint keywords aligned with a personalized latent query, which are then used to generate explanations.
*   **Profile Summarization**: Profile summarization creates rich and detailed user profiles that capture attributes such as age, gender, preferred and disliked genres, favorite directors, country, and language derived from users’ past interactions and item metadata. This enriched user data increases the informativeness of the retrieved content while safeguarding privacy by using rewritten profiles. Additionally, after retrieving related movies via user/item filtering, apply a three-step prompting strategy to extract features tailored to the user and select representative movies by directly instructing LLMs. These extracted features and representative movies are further used as the user profile to guide the final recommendation generation. leverage LLMs to generate more details about the entity profile based on its keywords/short phrases from external data to aid text generation.
*   **Hierarchical Graph Aggregation and Summarization**:
    When retrieving neighborhood textual information, the exponentially expanding receptive field at higher neighborhood layers often causes the aggregated content to exceed manageable limits, potentially diminishing the LLM’s effectiveness. This challenge highlights the need for hierarchical graph aggregation and summarization. The primary idea is to first summarize neighborhood information retrieved at each layer before propagating it to the next layer. This approach keeps the volume of text each node receives within consistent bounds. For instance, recursively aggregate information from neighboring nodes at higher layers and leverage LLMs to rephrase and compress the content before sharing it with relevant nodes in lower layers. Consequently, this strategy expands the receptive field while optimizing the computational budget for downstream generation tasks.

### 6.5 Generator

Once the relevant content is retrieved and organized appropriately, it is further processed by a downstream generator to produce the final content. Depending on the desired output, existing generators used for social graphs can be categorized into LLM-based text generators and Prediction-based generators. The choice between these two depends on the format of the desired output and the requirements of the social graph applications.

*   **LLM-based Text Generation**: This generator is typically used when the downstream application requires text outputs, such as item recommendations based on names, recommendation explanations, and review generation. Due to the probabilistic nature of the next token prediction, the generated text may not always precisely align with the desired output. To address this hallucination issue, the ground-truth text is often used for grounding the generated texts, such as matching generated items with the ground-truth items on the platform.
*   **Prediction-based Generation**: The generator directly predicts outputs and is primarily used for non-textual tasks, such as item recommendation and social prediction. For instance, Graph Neural Networks have become popular choices for graph-based recommendation and transformers are used for item recommendation tasks. Furthermore, in social property prediction, the generator could simply be a multilayer perception used for classification (e.g., partisanship classification) or regression (e.g., morality regression).

### 6.6 Resources and Tools

This section lists common resources and tools used for GraphRAG on social graphs. The summary and the link of are itemized as follows:

#### 6.6.1 Data Resources

*   **STARK-Amazon** ([https://stark.stanford.edu/dataset_amazon.html](https://stark.stanford.edu/dataset_amazon.html)): STARK-Amazon is a large-scale, semi-structured retrieval benchmark dataset for product search on the Amazon platform, integrating textual and relational knowledge bases. The nodes in the dataset represent products, colors, brands, and categories, while edges capture relationships like also_bought, also_viewed, has_brand, has_category, and has_color. Rich textual information, including product descriptions, customer reviews, and entity names, provides valuable context for retrieval tasks. Queries are generated by sampling relational templates and grounding them with specific entities, then leveraging LLMs to synthesize relevant textual and relational information. This process results in queries that capture customer interests, interpret specialized descriptions, and deduce relationships involving multiple entities within the query.
*   **Amazon-Review** ([https://jmcauley.ucsd.edu/data/amazon/](https://jmcauley.ucsd.edu/data/amazon/)): The Amazon-Review dataset includes reviews with ratings, text, and helpfulness votes, along with product metadata such as descriptions, categories, price, brand, and image features. Additionally, it provides link information through “also viewed” and “also bought” graphs. This dataset has two versions: the initial release logging the review data between 1996 and 2014, and a more recent version that logs ongoing data in 2014. The latest version also adds new metadata, including detailed product information, bullet points, and an ethical details table. Extensive GraphRAG work in social graphs has leveraged this dataset to build RAG frameworks for recommendation research.
*   **MovieLens** ([https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)): The MovieLens datasets describe people’s expressed preferences for movies. These preferences take the form of tuples, each resulting in a person expressing a preference (a 0-5 star rating) for a movie at a particular time. These preferences were entered through the MovieLens website — a recommender system that asks its users to give movie ratings to receive personalized movie recommendations. Side information includes movie title, year, and genre in textual format. further crawl the visual content of movie posters accessible from [https://github.com/HKUDS/LLMRec](https://github.com/HKUDS/LLMRec). Note that Movielen-100k is frequently used and provides users with demographic information such as user ID, age, gender, occupation, and zip code.
*   **Netflix** ([https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data)): This dataset was constructed to support participants in the Netflix Prize. The movie rating files contain over 100 million ratings from 480 thousand randomly chosen, anonymous Netflix customers over 17 thousand movie titles. The data were collected between October 1998 and December 2005 and reflect the distribution of all ratings received during this period. The date of each rating, the title, and the year of release for each movie ID are also provided. The multi-model side information is collected through web crawling, which is further stored [https://github.com/HKUDS/LLMRec](https://github.com/HKUDS/LLMRec).
*   **Yelp** ([https://www.yelp.com/dataset](https://www.yelp.com/dataset)): The Yelp dataset is a rich resource for academic research, particularly in fields like data science, natural language processing (NLP), and machine learning. This comprehensive dataset includes over 6.9 million reviews, 150,346 businesses, and 200,100 photos, covering 11 metropolitan areas. Researchers and students can explore real-world business and user data, with extensive details about businesses such as location, categories, attributes (like hours, parking, and ambiance), and aggregated check-ins. Reviews include full-text content, user ratings, and metadata, while user profiles offer insights into social interactions and behaviors, including friends, compliments, and review history. Additionally, the dataset contains 908,915 tips, providing quick recommendations and insights, and 1.2 million business attributes, offering granular information about service offerings.
*   **Weibo** ([https://www.aminer.cn/influencelocality](https://www.aminer.cn/influencelocality)): The Weibo dataset offers a rich snapshot of user interactions, behaviors and social connections within the Sina Weibo platform, capturing both static and dynamic facets of the social network. Starting with 100 randomly selected seed users, the dataset scales to encompass 1.7 million users and around 0.4 billion following relationships, averaging 200 followers per user. Each user is characterized by social profile details, including name, gender, verification status, and follower/followee counts. Tweet content is provided in both original Chinese and indexed formats, supporting robust research in social network analysis, content diffusion, and user interaction dynamics, making it an invaluable resource for RAG studies.
*   **Brexit** ([https://github.com/somethingx01/TopicalAttentionBrexit?tab=readme-ov-file](https://github.com/somethingx01/TopicalAttentionBrexit?tab=readme-ov-file)): This dataset includes a portion of the X (Twitter) network, specifically the remain-leave discourse before the 2016 UK Referendum on exiting the EU. It comprises a network with 7,589 users, 532,459 directed follow relationships, and 19,963 tweets, each associated with a binary stance. The dataset is preprocessed according to to assign each user a scalar value between 0 and 1, referred to as opinion, representing the average stance of the tweets retweeted by the user. The stance of each tweet is either 0 (“Remain”) or 1 (“Leave”).
*   **Diginetica** ([https://competitions.codalab.org/competitions/11161#learn_the_details-data2](https://competitions.codalab.org/competitions/11161#learn_the_details-data2)): This dataset comprises user session logs from an e-commerce search engine. The data spans six months and captures user interactions, including clicks, product views, and purchases. Each user session, defined by a one-hour inactivity period, contains anonymized user IDs, hashed queries, product descriptions, metadata (price, hashed product names, image identifiers, and product categories), and log-scaled prices.
*   **Yoochoose** ([https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015](https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015)): The Yoochoose dataset contains session data from an online European retailer. Each session records the user’s click events, with some sessions also including purchase events. Collected over several months in 2014, the data captures user interactions with the retailer’s website. The product meta-data includes categories.

#### 6.6.2 Tools

*   **X-Developer Platform** ([https://developer.x.com/en/docs/x-api/getting-started/about-x-api](https://developer.x.com/en/docs/x-api/getting-started/about-x-api)): The X Developer Platform provides powerful tools and resources for developers to integrate X’s real-time, historical, and global data into their own applications. With three main products—X API, X Ads API, and X for Websites—the platform supports a wide range of use cases, from retrieving and analyzing Tweets to managing ad campaigns and embedding X content directly into websites. The X API offers endpoints for managing conversations, exploring trends, and engaging with users, while the X Ads API enables businesses to manage ads with custom targeting and analytics. X for Websites allows seamless embedding of live content to enhance website engagement. Through comprehensive documentation, libraries, and community support, the X Developer Platform enables developers to create innovative solutions using X’s data and engagement tools.
*   **Reddit-API** ([https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki)): Reddit is a news aggregation and discussion platform where posts are organized into "subreddits," user-created boards moderated by the community. The Reddit API provides developers access to the site’s extensive collection of posts and comments. This free API has enabled the development of moderation tools, third-party applications, and training datasets for LLMs such as ChatGPT, Google, and Gemini. By using this API, we can query tremendous user interactions (i.e., comments and posts) and their corresponding textual contents (i.e., subreddit threads), which serve as golden resources for GraphRAG.
*   **Rec-Bole** ([https://recbole.io/](https://recbole.io/)): RecBole is an open-source, unified, and comprehensive library designed for developing and benchmarking recommendation algorithms. Built with Python and PyTorch, RecBole offers researchers a streamlined, efficient framework to experiment with over 100 recommendation algorithms across four main types: General, Sequential, Context-Aware, and Knowledge-Based Recommendations. The platform simplifies data handling by providing pre-processed copies of 43 benchmark datasets, making it easy for users to dive into model testing and development. The provided user-product interactions, as well as text-formatted user/product meta-data, could also be used for GraphRAG.

## 7 Planning and Reasoning Graph

A planning or reasoning graph characterizes the inherent logical flow among different entities, where entities typically represent concrete planning or reasoning substeps, and edges denote their logical relations. For the planning graph, a common example is a set of API tools used to achieve certain goals, where nodes represent actions, and edges denote their relational dependencies. For reasoning graphs, a notable example is the recent proposed chain/tree/graph of thoughts techniques where each node represents a decision-making thinking step connected by the reasoning flow. The dependency constraint and reasoning flow in the planning/reasoning graphs can be naturally represented as relational knowledge, which forms the foundation for GraphRAG in fulfilling planning/reasoning tasks. This section reviews GraphRAG for the planning and reasoning graph.

### 7.1 Application Tasks

The representative tasks conducted on planning and reasoning graphs are summarized as follows:

*   **Sequential Plan Retrieval**:
    As one of the most frequently encountered tasks, plan retrieval aims to retrieve the plan of steps or tools in the format of subgraphs to complete user queries. For example, given the user query "Please generate an image where a girl is reading a book, and her pose is the same as the boy in "example.jpg," then please describe the new image with your voice.", the retrieved final plan from the global plan graph would be "Post Detection" $\rightarrow$ "Pose-to-Image" $\rightarrow$ "Image-to-Text" $\rightarrow$ "Text-to-Speech."
*   **Naturalistic Asynchronous Planning**: In contrast to plan retrieval, which considers only dependency constraints among plans, incorporating time constraints introduces a greater challenge. Naturalistic Asynchronous Planning aims to produce a plan that meets dependency requirements and optimizes task completion efficiency, using time summation, time comparison, and constrained reasoning. For example, a user might request, "To make calzones, here are the steps and times required; please calculate the optimal plan for completion." An efficient plan would execute "roll dough," "add filling," and "fill dough" sequentially, with "preheat oven" in parallel, and then conclude with "bake."
*   **Structured Commonsense Reasoning**: Given a belief and an argument, structured common sense reasoning aims to infer the stance and generate/retrieve the corresponding commonsense explanation graph that explains the inferred stance.
*   **Defeasible Inference**: Defeasible Inference is a mode of reasoning in which, given a premise, a hypothesis may be weakened or overturned in light of new evidence. A prominent approach is to support defeasible inference through argumentation by constructing inference graphs.
*   **Tool Usage**: Instructing LLMs to use external tools for complex real-world problems has gained increasing importance. Recent research has explored advanced planning strategies to enhance LLMs’ tool-use intelligence. Notably, two approaches employ A* search and Monte Carlo Tree Search, both utilizing graph-structured reasoning to adaptively retrieve the next tool based on the LLM’s internal evaluations and environmental feedback. These methods enable dynamic tool retrieval, refining the model’s problem-solving precision and flexibility.
*   **Embodied Planning**: Embodied planning tasks in Embodied AI involve guiding agents to perform sequences of actions based on natural language instructions and visual cues in simulated or real-world environments. These tasks, such as organizing or cleaning, challenge agents due to ambiguous instructions, limited task-specific knowledge, sparse feedback, and complex, variable action spaces.

### 7.2 Reasoning and Planning Graph Construction

Most existing methods for constructing reasoning and planning graphs begin by analyzing relational dependencies and subsequently adding edges based on these hard-coded rules. Therefore, rather than limiting our focus to reviewing this only rule-based construction method, we review various dependency categories used for edge addition.

*   **Resource Dependency**: This dependency is defined as the shared resources among different actions/decisions. For example, two tools are connected if the output of one tool matches the input of the other, enabling a seamless transition from one process to another. The decision to add edges in existing graph construction methods is made by checking whether one node’s input matches another node’s output (e.g., plans, tools, or some other abstract processes).
*   **Temporal Dependency**: This relation ensures that the sequence of events follows certain orders within the planning and reasoning process. For example, connections in some collected datasets denote the successive order between two APIs for daily life.
*   **Inclusive Dependency**: The dependency described indicates that two connected nodes belong to the same category or environment. For example, cobblestones and birdhouses are both part of the category of garden decorations. Hypergraphs can effectively capture such belonging relationships where one entity belongs to multiple environments. Furthermore, these dependencies often form hierarchical structures, where "grandparent" entities encompass "parent" entities, which in turn encompass their "children." As the depth of the hierarchy increases, the space of possible dependencies grows exponentially, presenting a significant computational challenge. To address this, many previous works have proposed encoding such hierarchies in hyperbolic space. To the best of our knowledge, no prior research has explored inclusive dependencies in RAG systems.
*   **Causal Dependency**: This dependency indicates the cause-and-effect logic within the graph, where one action/decision causes the trigger of another action/decision. A long-standing example is the casual graph to encode assumptions about the data-generating process.
*   **Analogy Dependency**: This dependency underscores analogical reasoning, where relationships take the form "A is to B as C is to D." By recognizing and leveraging such dependency, humans build on existing knowledge to forge new insights across domains. A powerful historical example is the discovery of Coulomb’s Law, inspired by the analogy between gravitational forces affecting celestial bodies and electrical forces between charged particles.

While resource-dependent and causal relations involve a sequentially structured relation (former step/tool/decision leads to the later step/tool/decision), they are inherently different. For instance, if Tool A generates a report in PDF format and Tool B is designed to extract data from PDF files, Tool A and B share resource dependency because the output of Tool A (the PDF) matches the input of Tool B. However, this connection does not imply a direct cause-and-effect relationship between the two tools, i.e., using Tool A would not necessarily cause us to use Tool B.

### 7.3 Retriever

Retrievers for handling tasks on reasoning and planning graphs are often modeled as graph traversers. The query or task instruction locates the initial seeding nodes to initialize the graph traversal; then a traversal expands the graph’s scope either until a preset budget is exhausted or specific criteria are met. A core step throughout is selecting the most relevant neighbors from all potential candidates. Based on the criterion for neighborhood selection, retrievers fall into two main categories: embedding-based methods, which prioritize neighbors based on embedding similarity, and heuristic-based methods, which use local and global reward functions to determine neighbor importance.

*   **Embedding-based**: decompose the query, subsequently perform the embedding similarity match between the concatenated subquery with the current retrieved task API and each of the existing APIs, and then select the top one from the existing neighboring APIs. It explores the strategy of training and the one without training.
*   **Heuristic-based**: Compared to embedding-based methods, which rely on dedicated training data for mapping, heuristic-based methods define rules to guide the graph retriever effectively. model tool planning as a tree search algorithm, incorporating A* search to adaptively retrieve the most promising tool for subsequent use based on accumulated and anticipated costs. Both cost functions are heuristically designed, drawing on prior literature and practical insights.
*   **Thought Propagation Retrieval**: Given an input problem, thought propagation retrieval prompts LLMs to propose a set of analogous problems, and then applies established prompting techniques, like Chain-of-Thought (CoT), to derive solutions. The aggregation module subsequently consolidates solutions from these analogous problems, enhancing the problem-solving process for the original input.

### 7.4 Organizer

The current GraphRAG literature on planning and reasoning graphs generally omits organizer mechanisms, as the retrieval process alone achieves sufficient precision, eliminating the need for reranking. Unlike document or knowledge graphs, which typically apply one-shot embedding-based similarity retrieval to select the top-K relevant content, planning and reasoning graphs use a multi-round embedding similarity process integrated with reasoning steps, enhancing plan fidelity. Moreover, reward-based retrieval involves a sophisticated search that further boosts accuracy. Together, these high-quality strategies reduce the need for fine-grained reranking or filtering.

### 7.5 Generator

Most existing GraphRAG approaches for reasoning and planning tasks either output the retrieved plan directly or integrate it into the LLM for downstream solution generation. For instance, outputs the retrieved graph-structured plan as the final result, while compiles executed results from expert tools to generate the response. Similarly, after constructing a tool invocation graph, directly prompts the LLM to generate the parameters, and leverages the LLM to produce asynchronous plans based on task dependencies, time, and graph constraints. Notably, most of these works focus on fusing textual information, primarily using different graph structure formats (e.g., adjacency matrix, adjacency list, edge list, CSR) presented in textual form.

### 7.6 Resources and Tools

We summarize the useful resources and tools for GraphRAG on planning and reasoning graphs.

### 7.7 Data Resources

*   **Hugging Face** ([https://github.com/microsoft/JARVIS](https://github.com/microsoft/JARVIS)): Hugging Face offers a wide array of AI models covering multi-modality tasks in language, vision, audio, video, and more. Each task corresponds to a tool node that handles specific input and output. If tools A and B are connected, the output type of A must match the input type of B. Thus, edges in the Hugging Face plan graph represent the resource-dependent relation. firstly collects the tool repository and builds a tool graph with a collection of tools and their dependencies. Then, to generate each question, they sample a subgraph from the tool graph in the three basic formats: node, chain, and directed acyclic graph (DAG), each of which embodies a specific pattern for tool invocation. After that, the sampled subgraph is sent to LLMs to synthesize user instructions and populate the parameters for the tool subgraphs. At last, LLM-based and rule-based self-critic mechanisms are used to check and filer out the generated instruction to guarantee quality.
*   **Multimedia** ([https://github.com/microsoft/JARVIS](https://github.com/microsoft/JARVIS)): Unlike the AI-focused tools of Hugging Face, multimedia tools serve a broader range of user-centric tasks such as file downloading and video editing. The edges remain consistent with the Hugging Face domain and the tool connections denote the resource-dependent relation similar to Hugging Face. The construction of Multimedia is similar to Hugging Face.
*   **Daily Life APIs** ([https://github.com/microsoft/JARVIS](https://github.com/microsoft/JARVIS)): Daily life services, including web search and shopping, can also be viewed as tools for specific tasks. The dependencies among these APIs are primarily temporal, meaning that two daily life APIs are connected if one follows the other in sequence. The construction of Daily Life APIs is mostly similar to Hugging Face except that the edges are constructed manually because of the scarcity of publically available APIs.
*   **RestBench** ([https://restgpt.github.io/](https://restgpt.github.io/)): A dataset consisting of multiple APIs to address complex real-world user instructions in two scenarios: TMDB movie database and Spotify music player. The TMDB movie database offers RESTful APIs encompassing information about movies, TVs, actors, and images. Spotify Music Player provides API endpoints to retrieve content metadata, receive recommendations, create and manage playlists, and control playback. For RestBench, employed NLP experts to brainstorm instructions for different combinations of APIs and correspondingly annotate the gold API solution path for each instruction. Two additional experts are further employed to thoroughly verify the solvability of each instruction and the correctness of the corresponding solution path. To adapt RestBench into a graph-structured dataset, treats each API as a unique task node, modeling their relationships through two key dimensions: (1) categorical association and (2) resource dependencies. For instance, APIs offering movie-related functionalities, such as retrieving movie details or recommending films, are grouped under the ’movie’ category, while APIs focused on person-related tasks, like searching for actors, are classified under the ’person’ category. Additionally, if two APIs share a common parameter (e.g., movie-id), a link is established to represent resource dependency. To further enhance semantic distinction, GPT-4 is prompted to assign a unique name and detailed functional description to each API.
*   **AsyncHow** ([https://github.com/fangru-lin/graph-llm-asynchow-plan](https://github.com/fangru-lin/graph-llm-asynchow-plan)): A curated dataset consisting of 1.6K data points for asynchronous planning. Each data point comprises a user instruction specifying tasks with their basic execution constraints, represented by a directed acyclic graph (DAG). In these DAGs, nodes denote actions, and edges represent ordering constraints. Each edge carries a weight indicating the time required to complete the preceding action and transition to the next. Additionally, edges also signify causal links, meaning an action can only proceed if all preceding linked actions are completed. To construct this dataset, we first collected planning tasks from WikiHow. LLMs were then used for preprocessing, time annotation, and step dependency annotation. Specifically, plans containing optional steps, irrelevant tasks, or those lacking quantifiable duration were filtered out. The GPT-3.5 is used to estimate the time duration for each step, and the GPT -4 is used to annotate step dependencies using the DOT language. To generate natural language questions with execution constraints, ten trivially different but plausible templates were used to paraphrase the graph-structured dot language into human-understandable texts. The optimal time duration for a plan was calculated by determining the longest path within the DAG representation of the workflow.
*   **EXPLAGRAPHS** ([https://github.com/swarnaHub/ExplaGraphs](https://github.com/swarnaHub/ExplaGraphs)): Give the initially collected triplets consisting of belief, argument, and stance, the commonsense explanation graphs are constructed through a generic create-verify-refine iterative framework. Firstly, annotators construct a commonsense-augmented explanation graph that explicitly explains the stance. Each graph comprises 3-8 facts, each of which is a triplet with two concepts as entities connected by their relations. The graphical representation allows us to automatically perform in-browser checks for structural constraints, thereby guaranteeing the structural correctness of the graph. To further ensure the semantic correctness of the constructed graph, annotators reason through the graph to infer the stance based solely on the belief and the explanation graph. Finally, for incorrect graphs, another annotator refines them either by adding a new fact, removing an existing one, or replacing an existing fact.
*   **GSM8K** ([https://github.com/openai/grade-school-math](https://github.com/openai/grade-school-math)): The GSM8K dataset is a collection of 8.5K high-quality, linguistically diverse math word problems designed to assess multi-step reasoning for question answering. These grade school-level problems, solvable by a bright middle school student, require between 2 and 8 steps, primarily using basic arithmetic operations ($+,-,\times,\div$) without needing concepts beyond early Algebra. Solutions are presented in natural language to facilitate general applicability, offering insight into the reasoning processes of large language models. This format highlights how models handle structured, step-by-step reasoning in response to real-world math problems.
*   **PrOntoQA** ([https://github.com/asaparov/prontoqa](https://github.com/asaparov/prontoqa)): PrOntoQA is a question-answering dataset that provides examples featuring chains-of-thought to outline the reasoning needed for correct answers. The sentences are syntactically simple and well-suited for semantic parsing, making it valuable for formal analysis of predicted reasoning chains from large language models like GPT-3.

#### 7.7.1 Tools

*   **ToolBench** ([https://github.com/sambanova/toolbench](https://github.com/sambanova/toolbench)): Recent studies on software tool manipulation with LLMs primarily depend on closed model APIs (e.g., OpenAI), as there remains a significant performance gap between these proprietary models and available open-source LLMs. To investigate the underlying causes of this discrepancy and to advance the capabilities of open-source LLMs—particularly in tool manipulation—a benchmark named ToolBench has been developed. ToolBench includes a range of diverse software tools designed for real-world tasks and provides an accessible infrastructure for directly evaluating each model’s execution success rate.

## 8 Tabular Graph

Tabular data is another type of structured data that is widely used in real-world applications and is typically stored in relational databases. Tabular data may consist of a single table containing samples and their attributes, or multiple tables that share primary and foreign keys. LLMs have been explored to process and solve tasks involving tabular data, primarily by transforming the tabular data into text through serialization. However, such serialization may lead to some issues: (1) In the case of a single table, the feature columns should exhibit permutation invariance, but serializing the table data may disrupt this invariance; (2) For multiple tables, one table may be connected to another through primary/foreign keys, and leveraging these relationships is crucial for various tasks. Therefore, graph structures can be a suitable representation for tabular data. Additionally, when tables contain too many rows to fit within the context window of LLMs, graphs can facilitate efficient retrieval.

### 8.1 Application Tasks

Tables are widely used in real-world scenarios to store features and relationships between data. Understanding the structure of tabular data is crucial. As a result, there are numerous tasks that can benefit from the use of tabular graphs and below we list a few representative ones.

*   **Node-level tasks**: Node-level tasks include node classification and node regression, applied to tasks like cell type prediction, fraud detection, outlier detection, and click-through rate (CTR) prediction.
*   **Link-level tasks**: Link-level tasks involve link prediction, edge classification, and edge regression. Many tabular data tasks can be modeled as link-level tasks, such as data imputation and recommendation.
*   **Graph-level tasks**: Graph-level tasks aim to predict the properties of the entire graph, such as table type classification and table similarity prediction.
*   **Table question answering**: Table QA involves generating answers by understanding and reasoning over tabular data. This task requires comprehension of both the content and their relationships within tables, making graph structures suitable for encoding such information. For example, utilize graphs to enhance Table QA.
*   **Table retrieval**: Table retrieval focuses on retrieving semantically relevant tables based on natural language queries.

### 8.2 Tabular Graph Construction

Graphs are used in tabular data learning to model high-order feature interactions, high-order instance relationships, and relationships between instances across multiple tables. There are typically two types of nodes: instance nodes, which represent each row of a table, and feature nodes, which represent individual features. Generally, the following graphs are constructed:

*   **Instance Graph**: An instance graph connects a table’s rows (instances), modeling the relationships between instances. It is particularly useful for retrieving relevant instances within tabular data. There are mainly two approaches for constructing instance graphs:
    *   **Rule-based methods**: Instances are connected based on predefined rules. For example, heuristics derived from expert knowledge can be used to connect instances that share certain features. Expert knowledge can be leveraged for the graph construction. Another common approach is similarity-based methods, such as connecting instances through K-Nearest Neighbors (KNN) or based on similarity exceeding a threshold.
    *   **Learnable methods**: In this approach, an instance graph is typically initialized using rules or heuristics. The edge weights are then adjusted during the learning process, allowing the model to dynamically refine the graph structure over time.
*   **Feature Graph**: A feature graph connects features, with edges representing correlations between pairs of features. Typically, feature relationships are modeled in a learnable manner. Some works construct the feature graph by leveraging feature similarity, while others use heuristics based on expert knowledge to establish connections. Additionally, certain approaches link features if they belong to the same instance.
*   **Instance-Feature graphs**: The instance-feature graph is a heterogeneous graph, which connects the instance with their corresponding features.
*   **Cell Graph**: Cell graphs treat each cell in the table as a node. build a cell graph, where each cell node contains both spatial and logical locations attributes while the adjacency matrix represents the neighbor relation or the same-row and same-column relation between two cells.
*   **Tabular Hypergraph**: A hypergraph is a generalization of a graph in which an edge, known as a hyperedge, can connect multiple nodes. Since tables are often invariant to arbitrary row and column permutations, a hypergraph is a suitable structure for modeling tabular data. Specifically, model each row and column in a table as a hyperedge for pretraining purposes. Additionally, construct a hypergraph from tabular data to capture relationships between instances effectively.
    Additionally, model table as a knowledge graph, where the feature values or rows represent nodes, and the column names represent the relations. build a heterogeneous graph based on various predefined relations. construct trees for non-relational tables based on the hierarchical relations.
    Previous approaches primarily focus on constructing graphs based on a single table. However, in relational databases, there are often multiple tables. A common method is to first merge these tables into a single table, and then apply the previously mentioned methods to the merged table. However, this approach relies on manually joining the tables as part of a feature engineering step, which requires significant effort and substantial domain expertise. In the following, we will introduce cross-table graphs, which directly build a graph from multiple tables without the need for manual merging.
*   **Cross-table Graphs**: Cross-table graphs for tabular data typically connect different instances across multiple tables, where nodes usually represent rows in each table and edges are defined by primary-foreign key relationships. Additionally, propose Row2N/E: if a table has a primary key (PK), each row is treated as a node; however, if there are also two foreign key (FK) columns, each row is instead represented as an edge. These graphs model relationships across multiple tables, enabling the integration of information from different perspectives to facilitate various tasks.
    Additionally, build a hypergraph based on multiple tables, where the primary or foreign key as nodes, and the nodes within the same table as hyperedge.

### 8.3 Retriever

Modeling tabular data into graphs is still in its early stage, and most works follow popular retrieval methods, as introduced in Sections 2.4. Additionally, retrieve subgraphs based on timestamps to construct time-consistent computational graphs, while adopt a deterministic heuristic to select subgraphs.

### 8.4 Generator

Most existing methods that leverage tabular graphs still rely on GNNs or Graph Transformers as generators. Besides, fuse both GNNs and tabular based predictors, such as DeepFM, FT-Transformer, XGBoost and AutoGluon. jointly train gradient boosted decision tree (GBDT) and GNN. Recent advancements have seen the application of LLMs to tabular data tasks. This is typically achieved by converting tabular data into sequential formats suitable for LLM input, as explored by, and. However, this transformation can lead to the loss of inherent structural information present in the original tabular format. With advancements in the application of LLMs to graph data, LLMs can be further enhanced to handle various tasks more effectively with the support of tabular graphs.

### 8.5 Resources and Tools

In this section, we list some data sources and tools for GraphRAG on tabular graphs.

#### 8.5.1 Data Resources

Relational machine learning has recently gained popularity, leading to the development of several benchmarks and datasets for tabular data. For example:

*   **RelBench** (https://relbench.stanford.edu/) is a collection of realistic, large-scale, and diverse benchmark datasets for machine learning on relational databases. It includes various tasks, such as Node-level prediction tasks (e.g., multi-class classification, multi-label classification, regression), Link prediction tasks, Temporal and static prediction tasks. The benchmark features several datasets, including rel-amazon, rel-stack, rel-trial, rel-f1, rel-hm, rel-event, and rel-avito, providing a robust platform for evaluating models across multiple relational data scenarios and tasks.
*   **TabGraphs** evaluates various models — including simple baselines, tabular models, and GNNs — on graphs with tabular node features. This benchmark includes several TabGraphs datasets: tolokers-tab, questions-tab, city-reviews, browser-games, hm-categories, hm-prices, city-roads-M, city-roads-L, avazu-devices, web-fraud and web-traffic.
*   **Tabular-benchmark** (https://github.com/LeoGrin/tabular-benchmark) benchmarks 45 tabular datasets from diverse domains, comparing the performance of several tree-based and deep learning models. They evaluate tasks such as numerical classification, numerical regression, categorical classification, and categorical regression.
*   benchmark 11 tabular datasets, such as
    MSLR, Forest Cover Type, Higgs Boson, and Year Prediction.
    evaluating several tree-based models, deep learning models, and ensemble models.
*   **DBInfer Benchmark** (https://github.com/awslabs/multi-table-benchmark) is a set of benchmarks for measuring machine learning solutions over data stored as multiple tables. It includes several large-scale relational database (RDB) datasets—such as AVS, OB, DN, RR, AB, SE, MAG, and SE—with tasks like retention, CTR, purchase, CVR, churn, rating, popularity, venue prediction, citation, charge, and prepay. The benchmark provides implementations of various baselines, including popular tabular models with and without auto-feature-engineering methods, as well as Graph Neural Networks, making it a robust resource for multi-table learning evaluations.
*   **RTDL** (https://github.com/yandex-research/rtdl): RTDL (Research on Tabular Deep Learning) is a collection of papers and packages on deep learning for tabular data. It provides several popular tabular deep learning models.
*   **OpenML** (https://www.openml.org/) is an open platform for sharing datasets, algorithms, and experiments. It provides a large collection of machine learning datasets across various domains, including many tabular datasets.
*   **Kaggle** (https://www.kaggle.com/) hosts a wide array of datasets for data science competitions, making it a valuable resource for benchmarking tabular machine learning models on diverse real-world data.
*   **UC Irvine Machine Learning Repository** (https://archive.ics.uci.edu/) is a collection of databases, domain theories, and data generators that are used by the machine learning community for the empirical analysis of machine learning algorithms.
*   **HiTab** is a hierarchical table dataset for question answering and natural language generation.

#### 8.5.2 Tools

In this subsection, we list several tools that provide essential functionalities for data preparation, model training, and evaluation. These tools can be effectively leveraged for GraphRAG applications on tabular graphs.

*   **PyTorch Tabular** (https://github.com/manujosephv/pytorch_tabular): PyTorch Tabular is a powerful library built on PyTorch designed to simplify the application of deep learning techniques to tabular data. It provides several data preprocessing functions, including normalization, standardization, encoding of categorical features, and dataloader preparation. Additionally, it includes a variety of tabular machine-learning models and evaluation functions, making it a comprehensive tool for handling tabular data.
*   **DeepTables** (https://github.com/DataCanvasIO/DeepTables): DeepTables is an easy-to-use toolkit that harnesses the power of deep learning for tabular data. Built on TensorFlow, it is designed to address classification and regression tasks on tabular data. DeepTables offers a variety of tabular models and supports AutoML.
*   **PyTorch Frame** (https://github.com/pyg-team/pytorch-frame): PyTorch Frame is a deep learning extension for PyTorch, designed for heterogeneous tabular data with different column types, including numerical, categorical, time, text, and images. t provides a wide range of tabular models and supports integration with diverse model architectures, including Large Language Models.

## 9 Other Domains

While substantial GraphRAG research has been investigated in previous domains, GraphRAG remains significantly underexplored in other domains such as infrastructure, biology, and scene. Therefore, we combine them into a single comprehensive section, focusing only on key studies in these fields.

### 9.1 Infrastructure Graph

Infrastructure graphs, defined by Points of Presence (PoPs) interconnected through physical links, play a vital role in serving our daily activities across sectors such as power, water, gas, transportation, and communication. Due to the scarcity of GraphRAG research in infrastructure graphs, our review mainly focuses on graph construction methods and tasks alongside only a brief overview of recent (Graph)RAGs in this domain.

*   **Power Networks**: In power networks, nodes represent critical entities such as power plants, substations, transformers, and load points, while edges correspond to transmission and distribution lines facilitating the flow of electrical power across the network. Each node possesses features like power generation capacity, voltage level, load demand, geographical location, reliability metrics, and operational status, capturing the network’s operational and spatial aspects. Edges are characterized by features such as transmission capacity, impedance, length, voltage level, and real-time power flow, all essential for analyzing line performance and flow efficiency. This graph-based representation enables a range of essential tasks, including transformer fault diagnosis, power outage prediction, power flow approximation, and power generation optimization.
*   **Water Networks**: In water networks, nodes are junctions (pipe connections or users) and sources (reservoirs and tanks), and edges are pipes with water flow. Basic tasks include estimating node water heads and flow in all pipes given the water network layout, pipe characteristics, nodal demands, reservoir levels, and head measurements at limited locations.
*   **Gas Networks**: nodes represent connection points, gas sources, storage facilities, compressor stations and users, and edges edge respected natural gas pipelines, carrying user loads, diversion, and input.
*   **Transportation Networks**: Road networks, where intersections serve as nodes and road connections as edges, are commonly used to model spatial dependencies for traffic flow and speed forecasting. Similarly, metro and bus networks use stations as nodes with routes as edges, capturing station topology. Region-level problems involve dividing cities into regular or irregular regions, represented as graph nodes, where spatial dependencies reflect land use patterns; regular regions often use grid partitions, while irregular ones use diverse methods like road- or zip-code-based partitions. At the road level, sensor, segment, intersection, and lane graphs capture different road elements, with nodes representing sensors, segments, intersections, or lanes. For station-level networks, nodes represent various transportation hubs (subway, bus, bike, or car-sharing stations) linked by natural connections like subway or road networks, creating an interconnected spatial dependency graph.
*   **Communication Networks**: A computer network system typically comprises two interconnected graph layers: the logical and the physical. The logical layer represents the flow of data, where traffic is routed through multiple intermediate routers before reaching its destination. In this layer, nodes correspond to routers, and edges represent the logical paths that data packets traverse. Conversely, the physical topology layer refers to the underlying infrastructure, with Points of Presence (PoPs) from providers such as Comcast and Verizon serving as nodes and the physical fiber links between them forming the edges. Studies focused on the logical layer often model networks as graphs, where nodes represent devices (e.g., switches, routers) and edges denote links (e.g., fiber-optic cables) or traffic paths. This graph-based representation captures both the forwarding behavior of the network (i.e., traffic interactions) and its connectivity (i.e., topological behavior), offering valuable insights for network management. For instance, optical topology-aware traffic engineering has proven effective in mitigating issues like fiber cuts and flash crowds. For the physical layer, much previous research has focused on inferring the complete as well as aligning the physical and logical layers.

To summarize, the tasks operated on infrastructure networks could be broadly encompassed as utility prediction (e.g., flow and node performance), flow simulation and generation, vulnerability analysis, and network maintenance and operation. Managing and understanding the complex physical relationships within these graphs is essential for improving infrastructure management in key areas like service delivery, function forecasting, and network optimization. In computer networks, for instance, the state of a logical traffic routing path is directly influenced by the underlying physical fiber links. Predicting critical metrics like traffic delay and jitter depends on assessing the status of all involved fiber links, as these metrics are highly interdependent. The intricate physical connections in infrastructure graphs create valuable opportunities for employing GraphRAG techniques to enhance infrastructure management and optimization. Although no existing works have explored GraphRAG in infrastructure, few works have leveraged RAG, which we briefly review in the next.

explore the use of RAG to empower automated vehicles with the ability to anticipate pedestrian and driver behaviors, including pedestrian road-crossing actions and driver lane changes. RAG retrieves explanatory documents from the JAAD and PSI datasets to provide insights into pedestrian behavior. Additionally, build on recent advances in generative models for vision and language, proposing to harness the capabilities of LLMs within computer networking. A systematic approach has been proposed to develop a foundation model for traffic tasks, such as traffic classification and generation, treating packet hexadecimal bytes as tokens. Furthermore, the potential of generative AI in advancing telecom and networking is reviewed. Specifically, introduces an "operator’s copilot," a natural language interface that leverages LLMs for efficient data retrieval. This interface helps manage thousands of counters and metrics, minimizing the need for specialists and accelerating issue resolution through data intelligence. These pioneering works in leveraging generative AI for computer networking lay a good foundation for rebuilding (Graph)RAG for infrastructure networks.

### 9.2 Single-cell Graph

Single-cell sequencing allows for the detailed analysis of molecular traits at the level of individual cells. For example, single-cell RNA sequencing (scRNA-seq) quantifies RNA transcript levels, offering valuable information about cell identity, developmental stages, and functional characteristics.
Single-cell assay for transposase-accessible chromatin sequencing (scATAC-seq) records the number of reads per accessible chromatin region, resulting in highly dimensional data matrices containing hundreds of thousands of genomic regions.
With the explosion of the number of single-cell data, a variety of deep learning approaches have been developed in recent years to tackle single-cell analysis, especially GNN methods have been applied to various downstream tasks. In the task of cell type annotation,
sigGCN builds a gene-wise weighted adjacency matrix using data from the STRING database to establish a gene interaction network, with the node features representing corresponding gene expression levels. This graph is fed into a GCN-based autoencoder, which includes a convolutional layer and a max-pooling layer, followed by a flattened layer and a fully connected (FC) layer, to perform cell type annotation.
scDeepSort constructs a weighted bipartite graph where both cells and genes serve as nodes, with the edge weights representing the gene expression values for each cell-gene pair. Gene node features are derived through principal component analysis (PCA), while cell node features are obtained by aggregating the weighted features of the connected gene nodes.
The most common way to construct a single-cell graph is to build a KNN graph from single-cell data. To be specific, the data is first normalized to make it comparable across different cells. Next, dimensionality reduction methods, such as principal component analysis (PCA), are employed to reduce the dataset’s high dimensionality while retaining key information. In this lower-dimensional space, distances between cells are calculated, often using Euclidean distance. Each cell’s K nearest neighbors are then determined, and a graph is formed where cells are represented as nodes, and edges connect each cell to its $K$ closest neighbors.

**Multi-omics single-cell graphs**:
Multi-omics single-cell technologies integrate multiple layers of biological information—such as gene expression (RNA), chromatin accessibility (ATAC), and protein data—at the resolution of individual cells. Multiome refers to the simultaneous measurement of multiple molecular modalities, such as gene expression (RNA) and chromatin accessibility (ATAC), from the same single cell while CITE-seq (Cellular Indexing of Transcriptomes and Epitopes by Sequencing) is a multi-omics technology that allows for the simultaneous measurement of gene expression and protein surface markers at the single-cell level.
Taking multiome dataset as an example, scMoGNN builds a heterogeneous graph consisting of cell nodes, gene nodes, and peak nodes. The edge between a cell node and a gene node indicates the expression level of that gene in the cell, while the edge between a cell node and a peak node reflects the expression level of that peak in the cell. Additionally, a threshold can be applied to filter and select the connecting edges.
Additionally, pathways and gene activity can be incorporated as prior knowledge to establish connections between gene nodes, and connections between peaks and gene nodes respectively.
This graph representation captures both intra-modality (within each modality, like gene expression or chromatin accessibility) and cross-modality (between gene expression and chromatin accessibility) relationships, providing a comprehensive view of regulatory dynamics at the single-cell level

**Spatial transcriptomics single-cell graphs**:
Unlike traditional transcriptomics, spatial transcriptomics retains the precise location of spot representing a cell or small group of cells within the tissue.
Spatial transcriptomics primarily consists of three key data sources: gene expression, which captures transcript levels in specific spots; spot location, providing the spatial coordinates of each spot within the tissue; and spot images, offering visual context and morphology of the tissue at each spot.
In the task of cell type deconvolution, when building the KNN graph, GNNDeconvolver integrates both cell position information and gene expression data to compute the similarity between cells. SpaGCN additionally incorporate spot morphology to calculate similarity between spots.
Together, constructing KNN graph with such three data sources provides a richer, more holistic view of the tissue, enabling deeper insights into cellular function, interactions, and spatial organization.

### 9.3 Scene Graph

Scene graphs are a data structure designed to capture spatial and semantic relationships between objects within a scene. They are widely used in computer vision, graphics, and robotics to organize scenes, particularly when multiple objects interact, or the scene contains complex interactions. For example, SceneGraphs is a dataset for visual question answering, containing 100,000 scene graphs that describe the objects, attributes, and relationships within images. It presents tasks that test spatial reasoning and multi-step inference by asking users to answer open-ended questions based on textual descriptions derived from scene graphs.

G-Retriever processes Scene Graphs by first parsing JSON data to index objects and attributes, allowing for efficient retrieval of relevant nodes and edges based on the query. It then constructs a subgraph with the necessary scene information, filtering out unrelated details. Finally, G-Retriever uses this subgraph along with an LLM to generate answers, leveraging spatial and semantic relationships for accurate reasoning and response generation.

P-RAG engages with the environment through agents, building and updating a database of historical trajectories that guide the agent’s actions. Initially, the task’s goal instruction is provided. Before each action, the agent captures an observation image reflecting the current state, which is then converted into a scene graph format to facilitate processing by LLMs. By creating and retrieving scene graph context, P-RAG enhances the LLM’s ability to accurately interpret and navigate complex scenes, making this approach especially useful in planning embodied everyday tasks.

### 9.4 Random Graph

Random graphs are a foundational concept in network theory and are widely used for modeling and studying complex networks in fields such as computer science, physics, biology, and social sciences. They are constructed based on probabilistic rules, leading to various possible structures that reflect the diversity seen in real-world networks. These random graphs can be used to analyze the retrieval, organization, and generation processes within GraphRAG.

There are many models to generate random graphs, such as Erdős-Rényi Model (ER Model), Watts–Strogatz model, Barabási–Albert model, Random geometric graph, scale-free networks and stochastic block model. Additionally, various graph structures, such as Path Graphs, Complete Graphs, Star Graphs, and Barbell Graphs, can be generated to meet specific analytical needs.

Random graph generation models, such as Contextual stochastic block models (CSBM) has been widely leveraged in GNNs analysis. Additionally, random graphs are increasingly applied to examine the behavior of LLMs. For instance, leverage Erdős-Rényi graphs, scale-free networks, Barabási–Albert, stochastic block model, star, path and complete graph generators to test LLM performance on various graph reasoning tasks, such as edge existence, node degree, node/edge count, connected nodes and cycle check.
GraphLLM generates random graphs in various input formats to assess LLM performance on graph reasoning tasks, including substructure counting, maximum triplet sum, shortest path calculation, and bipartite graph matching. In this approach, a graph transformer encodes the graph, and the embedding-fusion method is used for generation. use star graphs to investigate limitations within the next-token prediction paradigm. Other studies, such as, and, explore the graph reasoning abilities of LLMs across various tasks.

## 10 Challenges and Future Work

After proposing the holistic framework of GraphRAG and reviewing it in each domain, we begin in this section by outlining the challenges and opportunities associated with each key component of GraphRAG, including graph construction, retriever, organizer, and generator. Then, we discuss the challenges and opportunities for GraphRAG as a holistic system with its evaluation and application.

### 10.1 Graph Construction

*   **How to construct graphs?** There are numerous ways to construct graphs, yet different tasks or domains may require different graph structures. For example, deciding on the granularity of nodes and edges, as well as which entities or relationships to extract, is critical. This process may also need to address challenges such as entity disambiguation, entity alignment, and coreference resolution. Understanding when a graph structure is necessary, whether to use single or multiple graphs and how to construct them in the most appropriate way for a specific application is essential but often complex.
*   **The format of graphs.** Graphs can be represented in various forms—are these representations equivalent, or do they offer unique advantages? Choosing the most effective representation for a given task can significantly influence performance.
*   **Multi-modal Graphs.** Despite building text-based graphs, the retrieved resources, such as images, audio, or video, can be multi-modal. Constructing a cohesive graph from multi-modal data presents a significant challenge, as it requires integrating diverse data types while preserving meaningful relationships.
*   **Dynamic graphs.** Many real-world scenarios involve dynamic data that evolve over time, which are essential for downstream tasks. Developing strategies to construct, update, and store graphs dynamically while maintaining both efficiency and effectiveness presents a further challenge worthy of exploration.

### 10.2 Retriever

*   **Differentiating Neural and Symbolic Knowledge:** Graph-structured data usually involves two distinct types of knowledge: symbolic-formatted knowledge, such as relations in knowledge graphs, and neural-formatted knowledge, such as entity names. Developing techniques to differentiate these two types of knowledge and designing corresponding retriever strategies for retrieving these two types of knowledge is worthy of further investigation.
*   **Harmonization between internal and external knowledge:** Since GraphRAG is often applied when internal knowledge alone is insufficient to address the task, assessing any overlap between internal and external knowledge using a robust calibration method is crucial. In addition, external knowledge may sometimes conflict with internal knowledge. To handle this, it is essential to design an effective knowledge validation and reconciliation mechanism, allowing selective retrieval and updating of external content as needed.
*   **Trade-off among Accuracy, Diversity, and Novelty:** Real-world user retrieval often involves complex intentions. Beyond delivering accurate content to ensure high utility—such as achieving high question-answering accuracy—there may also be a demand for diversity and novelty in the retrieved information. Balancing retrieved content’s accuracy, diversity, and novelty remains an open-ended challenge.
*   **Reasoning, planning, and thinking along the way:** A real-world retriever may need to dynamically and adaptively update its retrieve process in response to both the initial query and the content retrieved along the way. The question of how to equip the retriever with these adaptive thinking, reasoning, and planning abilities remains a big problem.

### 10.3 Organizer

*   **Balancing Completeness and Conciseness.** The retrieved graphs may be large, potentially containing significant information that is not related to the query. The Organizer should balance the need for complete information with the risk of overwhelming the model. This requires techniques for pruning irrelevant nodes and edges while retaining essential context, which is especially challenging in large or noisy graphs. Additionally, some knowledge may already be captured by LLMs, raising the question of how to identify and remove redundant information to further improve efficiency.
*   **Optimal Data Structuring:** Determining the most effective way to structure the retrieved content is a challenge. For example, deciding how to convert a structured graph into a format that the generator can leverage, how to arrange the order of retrieved content, and how to preserve the original data structure for structure-sensitive tasks are all important considerations. Different tasks may benefit from different structuring methods.
*   **Aligning Different Resources:** Retrieved content may come from various sources and in diverse formats, such as text, graphs, and images. Aligning these components effectively to help the generator poses a significant challenge, especially when integrating multiple data modalities.
*   **Data Augmentation:** Incorporating data augmentation within the Organizer involves enriching the retrieved graph content with nodes, edges, or features to improve the robustness of the model and improve downstream tasks. However, this process requires balancing real and augmented data to avoid introducing irrelevant or redundant information.

### 10.4 Generator

*   **Correct Format for Prompting.** The content retrieved after organization varies significantly in format — such as texts, triplets, or graphs — while current LLMs can only process text inputs. Exploring the most effective format for optimal LLM performance on specific tasks and designing more flexible generators that go beyond text input could be worthwhile avenues for research.
*   **Structural Encoding.** When the retrieved content is a subgraph and the downstream generator is an LLM, ensuring that the LLM can interpret the graph’s structural information is essential. Designing effective structural encodings and integrating them into token embeddings pose a key challenge. Although some previous works have incorporated various graph encodings into the text decoding process, no systematic study has yet demonstrated whether LLMs can distinguish between these encodings and accurately recognize their corresponding geometric structures.

### 10.5 GraphRAG as a System

Rather than individual components, GraphRAG is a system. Designing an efficient and cohesive GraphRAG system presents additional challenges:

*   **Integration Across Components:** Ensuring seamless interaction among the Graph Construction, Retriever, Organizer, and Generator components is essential. Each part must operate harmoniously to maintain efficiency and accuracy, which can be challenging to optimize the system globally.
*   **Scalability:** As data volumes and query demands increase, each component of the GraphRAG system, such as Graph Construction, Retriever, Organizer, and Generator, must efficiently handle larger, more complex graphs without compromising performance. For example, efficient graph storage, optimized querying (e.g., subgraph sampling and pathfinding), streamlined organization of retrieved components, and responsive generation are all essential. Additionally, training, serving, fine-tuning, and evaluating within GraphRAG demand sophisticated engineering on modern hardware and software stacks, including efficient training, data-efficient fine-tuning, communication-efficient algorithms, implementation of reinforcement learning with human feedback, GPU acceleration and other specialized hardware, model compression for deployment, and online maintenance.
*   **Trustworthiness:**
    Real-world GraphRAG systems often operate in high-stakes domains such as education, healthcare, and law, which imposes multiple desires when deploying GrapRAG systems. Therefore, deeply understanding the broader desires beyond merely optimizing utility is essential to ensure effective deployment. As motivated by trustworthy and safety research in other fields, these key goals beyond utility include reliability, robustness, fairness, and privacy. Although previous works have initiated the exploration of this multi-purpose optimization of RAG, they mostly focus on RAG without dedicated investigation of how the relational information captured by GraphRAG could cause additional trustworthy and safety concerns.
    *   **Reliability**: Reliability requires the system to deliver consistently low error rates across different scenarios. In RAGs, uncertainty quantification presents two primary challenges: Firstly, during the generation phase, uncertainty stems from the inherent probabilistic generation of LLMs. Standard techniques such as conformal prediction have been applied here with few adaptations. The general idea is to estimate the non-conformal score based on the calibration set and filter out those high-risk answers during the testing phase. Secondly, the retriever and its interaction with LLMs (e.g., treating LLMs as the reasoning agent to perform adaptive retrieval) also possess uncertainty. Unlike RAGs, retrievers and generators in GraphRAG demonstrate the multi-hop nature, which raises new requirements for multi-stage uncertainty quantification. For example, the error rate of one-step generation might accumulate after multi-step generation, and how to calibrate this accumulated error at the global level is the key challenge. The very first work proposed the learn-then-test framework to guarantee the global error rate. However, this solution may not consider the uncertainty of human-LLM interactions. Moreover, the additional learn-then-test component takes additional time and computational load for calibration. Future research aims to develop methods that can quantify and calibrate the uncertainty of (Graph)RAG as a system holistically.
    *   **Robustness**: Robustness aims the system to deliver equal-quality response under extreme scenarios such as the presence of noisy and irrelevant content. Existing research on RAGs has highlighted the significant degradation in LLMs’ performance when retrieved content includes noise or irrelevant information. Some studies address this challenge by adversarially training LLMs in noisy environments. However, there has been limited exploration of LLMs’ robustness from the structural perspective. For example, would the LLM reasoning performance change when the underlying reasoning graph gets perturbed? Addressing these issues requires a deeper focus on the interplay between structural integrity and the robustness of GraphRAG systems, paving the way for robust performance in tasks requiring complex reasoning and planning.
    *   **Safety**: Recent studies have highlighted that LLMs are susceptible to various adversarial attacks. Techniques such as prompt manipulation, hint injection, and input perturbation enable attackers to bypass safety mechanisms and exploit vulnerabilities, posing substantial social risks. RAGs that combine the power of LLMs with external databases introduce unique safety challenges. Existing works in RAGs have developed several threats (e.g., adversarial passage injection, group-query targeting, and jailbreak attacks) and defense strategies (such as isolate-then-aggregate strategy). However, all of them have overlooked the structural vulnerabilities inherent in graph-structured data. For instance, attackers can exploit the network structure of graph-based databases by leveraging principles from network science to design highly impactful attacks. Attackers can maximize their influence on the system’s behavior by strategically targeting nodes with specific structural properties, such as high degree or centrality. This highlights the need for robust defenses that account for both content-based and structural threats in RAG systems.
    *   **Privacy**: Privacy is a critical concern in RAG systems, especially when operating in domains involving sensitive or personal data, such as healthcare, education, or finance. Unlike traditional RAG systems, GraphRAG introduces additional privacy risks due to the relational nature of graphs, which may inadvertently reveal private information through connections or patterns. For instance, even if a sensitive node is protected, it may still be retrieved indirectly via its neighbors. Additionally, in graphs exhibiting homophily—where connected nodes tend to share similar attributes—sensitive information can be inferred from neighboring nodes. The use of GNNs for graph encoding further exacerbates these risks. The message-passing mechanism in GNNs propagates features across nodes and edges, potentially leading to the leakage of sensitive or confidential information during the propagation process. Addressing these challenges requires advanced privacy-preserving techniques that account for the interconnected nature of graphs, rather than treating the data as independent and identically distributed (iid). Privacy protection must be designed across the entire GraphRAG pipeline, from graph construction to generation, ensuring that sensitive information remains secure while preserving the graph’s utility for downstream tasks.
    *   **Explainability**: Explainability is essential for fostering trust in RAG systems, especially in high-stakes domains like law, healthcare, and finance. Compared to traditional RAG, GraphRAG offers enhanced explainability through the explicit relationships encoded between nodes in the graph. These explicit connections allow the system to generate clear and interpretable explanations tailored to specific tasks, making it more transparent and trustworthy for end users. For example, in the mutli-hop question answering, the GraphRAG can be leveraged to generate reasoning paths to the question. These paths provide step-by-step explanations, allowing users to understand how intermediate conclusions were derived and verify the relevance and correctness of the system’s logic. Similarly, in molecular property prediction, specific subgraphs representing functional groups or structural motifs can be utilized to explain predictions, linking molecular features to observed properties or behaviors. However, achieving such explainability requires GraphRAG to retrieve reasonable and contextually relevant subgraphs, which remains a challenge. Ensuring that explanations remain faithful to the underlying model logic while balancing comprehensiveness and simplicity will be critical challenges for future research.

### 10.6 Evaluation of GraphRAG.

Evaluating the performance of a GraphRAG system is challenging due to its complex, multi-component nature. Standard benchmarks may not fully capture the nuances of graph-based construction, retrieval, organization, and generation, so tailored benchmarks are essential to assess each component and their overall impact on the system.

*   **Component-Level Optimality:** Each component’s performance directly influences the GraphRAG system as a whole. Evaluating each component, such as Graph Construction, Retriever, Organizer, and Generator, requires specific designs suited to their unique roles. This may involve constructing different datasets and evaluation metrics that align with the intended function of each component.
*   **End-to-End Benchmarks:** To assess the system’s overall effectiveness, comprehensive end-to-end benchmarks are essential. These should evaluate the quality of generated outputs, system response time, efficiency, and resource utilization, providing a holistic view of GraphRAG’s performance in real-world applications.
*   **Task and Domain-Specific Evaluation:** Different tasks and domains may impose unique requirements on the GraphRAG system, necessitating specialized designs for each component. Methods that perform well in one domain may not generalize effectively to others, highlighting the need for diverse benchmarks. Additionally, Multi-task and multi-domain evaluations help determine the system’s adaptability and effectiveness across varied contexts.
*   **Trustworthiness benchmark.** Ensuring the trustworthiness of the GraphRAG system is critical, especially in applications where decisions rely heavily on accurate and unbiased information. A trustworthiness benchmark should evaluate aspects such as robustness against adversarial inputs, data privacy protection, and transparency in how answers are derived, ensuring that outputs are explainable and reliable.

### 10.7 New Applications

While we have introduced applications of GraphRAG in several domains and tasks, there are still many domains that can leverage GraphRAG, such as Code generation and robust cyber defense. Extending its use to other domains is promising but presents unique challenges. Determining how to adapt GraphRAG effectively for new fields requires understanding the specific requirements, data structures, and graph configurations unique to each application area. Developing tailored strategies to construct, retrieve, organize, and generate data for diverse domains is essential for maximizing GraphRAG’s adaptability and effectiveness.

## 11 Conclusion

In this survey, we first introduced the demand and rationale behind GraphRAG, highlighting its ability to enhance retrieval-augmented generation by integrating graph-structured information. We then unified the architectural designs of existing GraphRAG approaches into a holistic framework, comprising five key components: graph construction, retriever, organizer, generator, and data source. For each component, we reviewed representative techniques. Given the diversity of graph structures and their applications across different domains, we also explored GraphRAG designs tailored to specific domains. By reviewing GraphRAG applications across varied domains—from knowledge graphs and document graphs to scientific and social graphs, we illustrated how its flexibility allows it to meet unique demands and address a wide range of tasks. Finally we discuss challenges and opportunities that have the potential to push the boundaries for GraphRAG.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="jina-scraped.md">
<details>
<summary>Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop | Towards Data Science</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/>

Title: Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop

URL Source: https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/

Published Time: 2026-03-03T12:00:00+00:00

Markdown Content:
# Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop | Towards Data Science

![Image 1: Revisit consent button](https://cdn-cookieyes.com/assets/images/revisit.svg)

We value your privacy

We use cookies to enhance your browsing experience, serve personalised ads or content, and analyse our traffic. By clicking "Accept All", you consent to our use of cookies.

Customise Reject All Accept All

Customise Consent Preferences![Image 2](https://cdn-cookieyes.com/assets/images/close.svg)

We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.

The cookies that are categorised as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site. ...Show more

Necessary Always Active

Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.

*   Cookie __cf_bm 
*   Duration 1 hour 
*   Description This cookie, set by Cloudflare, is used to support Cloudflare Bot Management.  

*   Cookie AWSALBCORS 
*   Duration 7 days 
*   Description Amazon Web Services set this cookie for load balancing. 

*   Cookie _cfuvid 
*   Duration session 
*   Description Cloudflare sets this cookie to track users across sessions to optimize user experience by maintaining session consistency and providing personalized services 

*   Cookie li_gc 
*   Duration 6 months 
*   Description Linkedin set this cookie for storing visitor's consent regarding using cookies for non-essential purposes. 

*   Cookie __hssrc 
*   Duration session 
*   Description This cookie is set by Hubspot whenever it changes the session cookie. The __hssrc cookie set to 1 indicates that the user has restarted the browser, and if the cookie does not exist, it is assumed to be a new session. 

*   Cookie __hssc 
*   Duration 1 hour 
*   Description HubSpot sets this cookie to keep track of sessions and to determine if HubSpot should increment the session number and timestamps in the __hstc cookie. 

*   Cookie wpEmojiSettingsSupports 
*   Duration session 
*   Description WordPress sets this cookie when a user interacts with emojis on a WordPress site. It helps determine if the user's browser can display emojis properly. 

*   Cookie _octo 
*   Duration 1 year 
*   Description No description available. 

*   Cookie logged_in 
*   Duration 1 year 
*   Description No description available. 

*   Cookie __Secure-YEC 
*   Duration past 
*   Description YouTube sets this cookie to stores the user's video player preferences using embedded YouTube video 

*   Cookie __eoi 
*   Duration 6 months 
*   Description Description is currently not available. 

*   Cookie AWSALBTGCORS 
*   Duration 7 days 
*   Description No description available. 

*   Cookie login-status-p 
*   Duration past 
*   Description Description is currently not available. 

*   Cookie AWSALBTG 
*   Duration 7 days 
*   Description No description available. 

*   Cookie csrf_token 
*   Duration session 
*   Description No description available. 

*   Cookie token_v2 
*   Duration 1 day 
*   Description Description is currently not available. 

*   Cookie D 
*   Duration 1 year 
*   Description Description is currently not available. 

*   Cookie PHPSESSID 
*   Duration session 
*   Description This cookie is native to PHP applications. The cookie stores and identifies a user's unique session ID to manage user sessions on the website. The cookie is a session cookie and will be deleted when all the browser windows are closed. 

*   Cookie VISITOR_PRIVACY_METADATA 
*   Duration 6 months 
*   Description YouTube sets this cookie to store the user's cookie consent state for the current domain.  

*   Cookie cookietest 
*   Duration session 
*   Description The cookietest cookie is typically used to determine whether the user's browser accepts cookies, essential for website functionality and user experience. 

*   Cookie __Host-airtable-session 
*   Duration 1 year 
*   Description This cookie is used to enable us to integrate the services of Airtable. 

*   Cookie __Host-airtable-session.sig 
*   Duration 1 year 
*   Description This cookie is used to enable us to integrate the services of Airtable. 

*   Cookie m 
*   Duration 1 year 1 month 4 days 
*   Description Stripe sets this cookie for fraud prevention purposes. It identifies the device used to access the website, allowing the website to be formatted accordingly. 

*   Cookie BIGipServer* 
*   Duration session 
*   Description Marketo sets this cookie to collect information about the user's online activity and build a profile about their interests to provide advertisements relevant to the user.  

*   Cookie __cfruid 
*   Duration session 
*   Description Cloudflare sets this cookie to identify trusted web traffic. 

*   Cookie _GRECAPTCHA 
*   Duration 6 months 
*   Description Google Recaptcha service sets this cookie to identify bots to protect the website against malicious spam attacks. 

*   Cookie __Secure-YNID 
*   Duration 6 months 
*   Description Google cookie used to protect user security and prevent fraud, especially during the login process. 

*   Cookie cookieyes-consent 
*   Duration 1 year 
*   Description CookieYes sets this cookie to remember users' consent preferences so that their preferences are respected on subsequent visits to this site. It does not collect or store any personal information about the site visitors. 

Functional

- [x] 

Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.

*   Cookie BCTempID 
*   Duration 10 minutes 
*   Description No description available. 

*   Cookie BCSessionID 
*   Duration 1 year 1 month 4 days 
*   Description Blueconic sets this cookie as a unique identifier for the BlueConic profile. 

*   Cookie lidc 
*   Duration 1 day 
*   Description LinkedIn sets the lidc cookie to facilitate data center selection. 

*   Cookie brw 
*   Duration 1 year 
*   Description No description available. 

*   Cookie brwConsent 
*   Duration 5 minutes 
*   Description Description is currently not available. 

*   Cookie WMF-Uniq 
*   Duration 1 year 
*   Description Description is currently not available. 

*   Cookie loom_anon_comment 
*   Duration 1 year 
*   Description No description available. 

*   Cookie loom_referral_video 
*   Duration session 
*   Description Description is currently not available. 

*   Cookie VISITOR_INFO1_LIVE 
*   Duration 6 months 
*   Description A cookie set by YouTube to measure bandwidth that determines whether the user gets the new or old player interface. 

*   Cookie yt-remote-connected-devices 
*   Duration Never Expires 
*   Description YouTube sets this cookie to store the user's video preferences using embedded YouTube videos. 

*   Cookie ytidb::LAST_RESULT_ENTRY_KEY 
*   Duration Never Expires 
*   Description The cookie ytidb::LAST_RESULT_ENTRY_KEY is used by YouTube to store the last search result entry that was clicked by the user. This information is used to improve the user experience by providing more relevant search results in the future. 

*   Cookie yt-remote-device-id 
*   Duration Never Expires 
*   Description YouTube sets this cookie to store the user's video preferences using embedded YouTube videos. 

*   Cookie yt-remote-session-name 
*   Duration session 
*   Description The yt-remote-session-name cookie is used by YouTube to store the user's video player preferences using embedded YouTube video. 

*   Cookie yt-remote-fast-check-period 
*   Duration session 
*   Description The yt-remote-fast-check-period cookie is used by YouTube to store the user's video player preferences for embedded YouTube videos. 

*   Cookie yt-remote-session-app 
*   Duration session 
*   Description The yt-remote-session-app cookie is used by YouTube to store user preferences and information about the interface of the embedded YouTube video player. 

*   Cookie yt-remote-cast-available 
*   Duration session 
*   Description The yt-remote-cast-available cookie is used to store the user's preferences regarding whether casting is available on their YouTube video player. 

*   Cookie yt-remote-cast-installed 
*   Duration session 
*   Description The yt-remote-cast-installed cookie is used to store the user's video player preferences using embedded YouTube video. 

*   Cookie cp_session 
*   Duration 3 months 
*   Description Codepen sets this cookie for Help systems found in the website. 

*   Cookie loid 
*   Duration 1 year 1 month 4 days 
*   Description This cookie is set by the Reddit. The cookie enables the sharing of content from the website onto the social media platform. 

Analytics

- [x] 

Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.

*   Cookie __hstc 
*   Duration 6 months 
*   Description Hubspot set this main cookie for tracking visitors. It contains the domain, initial timestamp (first visit), last timestamp (last visit), current timestamp (this visit), and session number (increments for each subsequent session). 

*   Cookie hubspotutk 
*   Duration 6 months 
*   Description HubSpot sets this cookie to keep track of the visitors to the website. This cookie is passed to HubSpot on form submission and used when deduplicating contacts. 

*   Cookie _ga 
*   Duration 1 year 1 month 4 days 
*   Description Google Analytics sets this cookie to calculate visitor, session and campaign data and track site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognise unique visitors. 

*   Cookie _ga_* 
*   Duration 1 year 1 month 4 days 
*   Description Google Analytics sets this cookie to store and count page views. 

*   Cookie __Host-psifi.analyticsTrace 
*   Duration 6 hours 
*   Description Description is currently not available. 

*   Cookie __Host-psifi.analyticsTraceV2 
*   Duration 6 hours 
*   Description Description is currently not available. 

*   Cookie _gh_sess 
*   Duration session 
*   Description GitHub sets this cookie for temporary application and framework state between pages like what step the user is on in a multiple step form. 

*   Cookie YSC 
*   Duration session 
*   Description YSC cookie is set by Youtube and is used to track the views of embedded videos on Youtube pages. 

*   Cookie ajs_anonymous_id 
*   Duration 1 year 
*   Description This cookie is set by Segment to count the number of people who visit a certain site by tracking if they have visited before. 

*   Cookie vuid 
*   Duration 1 year 1 month 4 days 
*   Description Vimeo installs this cookie to collect tracking information by setting a unique ID to embed videos on the website.  

Performance

- [x] 

Performance cookies are used to understand and analyse the key performance indexes of the website which helps in delivering a better user experience for the visitors.

*   Cookie AWSALB 
*   Duration 7 days 
*   Description AWSALB is an application load balancer cookie set by Amazon Web Services to map the session to the target. 

*   Cookie acq 
*   Duration past 
*   Description Description is currently not available. 

*   Cookie acq.sig 
*   Duration past 
*   Description Description is currently not available. 

*   Cookie ptc 
*   Duration 2 years 
*   Description No description available. 

Advertisement

- [x] 

Advertisement cookies are used to provide visitors with customised advertisements based on the pages you visited previously and to analyse the effectiveness of the ad campaigns.

*   Cookie muc_ads 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to collect user behaviour and interaction data to optimize the website. 

*   Cookie guest_id_marketing 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to identify and track the website visitor. 

*   Cookie guest_id_ads 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to identify and track the website visitor. 

*   Cookie personalization_id 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to integrate and share features for social media and also store information about how the user uses the website, for tracking and targeting. 

*   Cookie guest_id 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to identify and track the website visitor. It registers if a user is signed in to the Twitter platform and collects information about ad preferences. 

*   Cookie bcookie 
*   Duration 1 year 
*   Description LinkedIn sets this cookie from LinkedIn share buttons and ad tags to recognize browser IDs. 

*   Cookie __Secure-ROLLOUT_TOKEN 
*   Duration 6 months 
*   Description YouTube sets this cookie to manage feature rollout and experimentation. It helps Google control which new features or interface changes are shown to users as part of testing and staged rollouts, ensuring consistent experience for a given user during an experiment. 

*   Cookie yt.innertube::nextId 
*   Duration Never Expires 
*   Description YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen. 

*   Cookie yt.innertube::requests 
*   Duration Never Expires 
*   Description YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen. 

*   Cookie session_tracker 
*   Duration session 
*   Description This cookie is set by the Reddit. This cookie is used to identify trusted web traffic. It also helps in adverstising on the website. 

*   Cookie edgebucket 
*   Duration session 
*   Description Reddit sets this cookie to save the information about a log-on Reddit user, for the purpose of advertisement recommendations and updating the content. 

*   Cookie did 
*   Duration 1 year 
*   Description Arbor sets this cookie to show targeted ads to site visitors.This cookie expires after 2 months or 1 year. 

Uncategorised

Other uncategorised cookies are those that are being analysed and have not been classified into a category as yet.

No cookies to display.

Reject All Save My Preferences Accept All

[Skip to content](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/#wp--skip-link--target)

[![Image 3: Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)

Publish AI, ML & data-science insights to a global community of data professionals.

[Sign in](https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/)

[Submit an Article](https://contributor.insightmediagroup.io/)

*   [Latest](https://towardsdatascience.com/latest/)
*   [Editor’s Picks](https://towardsdatascience.com/tag/editors-pick/)
*   [Deep Dives](https://towardsdatascience.com/tag/deep-dives/)
*   [Newsletter](https://towardsdatascience.com/tag/the-variable/)

* * *

*   [Write For TDS](https://towardsdatascience.com/submissions/)

[![Image 4: Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)

Toggle Mobile Navigation

*   [LinkedIn](https://www.linkedin.com/company/towards-data-science/?originalSubdomain=ca)
*   [X](https://x.com/TDataScience)

Toggle Search

Search 

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/)

# Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop

A practical guide to choosing between single-pass pipelines and adaptive retrieval loops based on your use case's complexity, cost, and reliability requirements

[Mostafa Ibrahim](https://towardsdatascience.com/author/mostafaibrahim18/)

Mar 3, 2026

 11 min read

 Share 

![Image 5](https://towardsdatascience.com/wp-content/uploads/2026/03/classic-vs-agentic-rag-2.jpg)

## Introduction: Why this comparison matters

[RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) began with a straightforward goal: ground model outputs in external evidence rather than relying solely on model weights. Most teams implemented this as a pipeline: retrieve once, then generate an answer with citations.

Over the last year, more teams have started moving from that “one-pass” pipeline towards agent-like loops that can retry retrieval and call tools when the first pass is weak. [Gartner](https://www.gartner.com/en/newsroom/press-releases/2023-11-29-gartner-says-more-than-80-percent-of-enterprises-will-have-used-generative-ai-apis-or-deployed-generative-ai-enabled-applications-by-2026) even forecasts that **33% of enterprise software applications will include agentic AI by 2028**, a sign that “agentic” patterns are becoming mainstream rather than niche.

[Agentic RAG](https://arxiv.org/abs/2301.11913) changes the system structure. Retrieval becomes a control loop: retrieve, reason, decide, then retrieve again or stop. This mirrors the core pattern of “reason and act” approaches, such as [ReAct](https://arxiv.org/abs/2210.03629), in which the system alternates between reasoning and action to gather new evidence.

However, agents do not enhance RAG without tradeoffs. Introducing loops and tool calls increases adaptability but reduces predictability. Correctness, latency, observability, and failure modes all change when debugging a process instead of a single retrieval step.

## Classic RAG: the pipeline mental model

Classic RAG is straightforward to understand because it follows a linear process. A user query is received, the system retrieves a fixed set of passages, and the model generates an answer based on that single retrieval. If issues arise, debugging usually focuses on retrieval relevance or context assembly.

At a high level, the pipeline looks like this:

1.   **Query:** take the user question (and any system instructions) as input
2.   **Retrieve:** fetch the top-k relevant chunks (usually via vector search, sometimes hybrid)
3.   **Assemble context:** Select and arrange the best passages into a prompt context (often with reranking)
4.   **Generate:** Produce an answer, ideally with citations back to the retrieved passages

![Image 6: Classic RAG pipeline: User query → Retrieve top-k → Assemble context → Generate answer with citations](https://contributor.insightmediagroup.io/wp-content/uploads/2026/02/classic-rag-pipeline.png)
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

*   **Multi-hop questions**: the answer needs evidence spread across multiple sources
*   **Underspecified queries**: the user’s wording is not the best retrieval query
*   **Brittle chunking:** relevant context is split across chunks or obscured by jargon
*   **Ambiguity:** the system may need to ask clarifying questions, reformulate, or explore further before providing an accurate answer.

**Why this matters:**

When classic RAG fails, it often does so quietly. The system still provides an answer, but it may be a confident synthesis based on weak evidence.

## Agentic RAG: from retrieval to a control loop

Agentic RAG retains the retriever and generator components but changes the control structure. Instead of relying on a single retrieval pass, retrieval is wrapped in a loop, allowing the system to review its evidence, identify gaps, and attempt retrieval again if needed. This loop gives the system an “agentic” quality: it not only generates answers from evidence but also actively chooses how to gather stronger evidence until a stop condition is met. A helpful analogy is incident debugging: classic RAG is like running one log query and writing the conclusion from whatever comes back, while agentic RAG is a debug loop. You query, inspect the evidence, notice what’s missing, refine the query or check a second system, and repeat until you’re confident or you hit a time/cost budget and escalate.

A minimal loop is:

1.   **Retrieve:** pull candidate evidence (docs, search results, or tool outputs)
2.   **Reason:** synthesize what you have and identify what’s missing or uncertain
3.   **Decide:** stop and answer, refine the query, switch sources/tools, or escalate

For a research reference, ReAct provides a useful mental model: reasoning steps and actions are interleaved, enabling the system to gather more substantial evidence before finalizing an answer.

### What agents add

**Planning (decomposition)**

The agent can decompose a question into smaller evidence-based objectives.

Example: “Why is SSO setup failing for a subset of users?”

*   What error codes are we seeing?
*   Which IdP configuration is used
*   Is this a docs question, a log question, or a configuration question

Classic RAG treats the entire question as a single query. An agent can explicitly determine what information is needed first.

**Tool use (beyond retrieval)**

In agentic RAG, retrieval is one of several available tools. The agent may also use:

*   A second index
*   A database query
*   A search API
*   A config checker
*   A lightweight verifier

This is important because relevant answers often exist outside the documentation index. The loop enables the system to retrieve evidence from its actual source.

**Iterative refinement (deliberate retries)**

This represents the most significant advancement. Instead of attempting to generate a better answer from weak retrieval, the agent can deliberately requery.

[Self-RAG](https://arxiv.org/abs/2310.11511) is a good example of this research direction: it is designed to retrieve on demand the critique of retrieved passages and to generate them, rather than always using a fixed top-k retrieval step.

This is the core capability shift: the system can adapt its retrieval strategy based on information learned during execution.

![Image 7: Agentic RAG control loop: Retrieve evidence → Reason about gaps → Decide next step → Answer with citations or call a tool](https://contributor.insightmediagroup.io/wp-content/uploads/2026/02/agentic-rag-loop.png)
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

1.   The question is underspecified and needs query refinement
2.   The evidence is spread across multiple documents or sources
3.   The first retrieval returns partial or conflicting information, and the system needs to verify before committing

### Where loops hurt

The tradeoff is operational complexity. With loops, you introduce more moving parts (planner, retriever, optional tools, stop conditions), which increases variance and makes runs harder to reproduce. You also expand the surface area for failures: a run might look “fine” at the end, but still burn tokens through repeated retrieval, retries, or tool cascades.

This is also why [“enterprise RAG”](https://arxiv.org/abs/2404.16130) tends to get tricky in practice: security constraints, messy internal data, and integration overhead make naive retrieval brittle.

## Failure modes you’ll see early in production

Once you move from a pipeline to a control loop, a few problems show up repeatedly:

*   **Retrieval thrash:** the agent keeps retrieving without improving evidence quality.
*   **Tool-call cascades:** one tool call triggers another, compounding latency and cost.
*   **Context bloat:** the prompt grows until quality drops or the model starts missing key details.
*   **Stop-condition bugs:** the loop doesn’t stop when it should (or stops too early).
*   **Confident-wrong answers:** the system converges on noisy evidence and answers with high confidence.

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

*   FAQs and documentation Q&A
*   Single-document answers (policies, specs, limits)
*   Fast assist where latency predictability matters more than perfect coverage

Agentic RAG is usually worth the added complexity when the task needs multi-step evidence gathering:

*   Decomposing a question into sub-questions
*   Iterative retrieval (rewrite, broaden/narrow, switch sources)
*   Verification and cross-checking across sources/tools
*   Workflows where “try again” is required to reach a confident, cited answer.

A simple rule: **don’t pay for loops unless your task routinely fails in one pass**.

## Rollout guidance: add a second pass before going “full agent.”

You do not need to choose between a permanent pipeline and full agentic implementation. A practical compromise is to use classic RAG by default and trigger a second-pass loop only when failure signals are detected, such as missing citations, low retrieval confidence, contradictory evidence, or user follow-ups indicating the initial answer was insufficient. This approach keeps most queries efficient while providing a recovery path for more complex cases.

![Image 8: Rollout flowchart: Run classic RAG → Failure signals? → Return answer or run second-pass loop → Stop condition met?](https://contributor.insightmediagroup.io/wp-content/uploads/2026/02/agentic-rag-decision-loop.png)
### Core Takeaway

Agentic RAG is not simply an improved version of RAG; it is RAG with an added control loop. This loop can enhance correctness for complex, ambiguous, or multi-hop queries by allowing the system to refine retrieval and verify evidence before answering. The tradeoff is operational: increased complexity, higher tail latency and cost spikes, and additional failure modes to debug. Clear budgets, stop rules, and traceability are essential if you adopt this approach.

## Conclusion

If your product primarily involves document lookup, extraction, or rapid assistance, classic RAG is typically the best default. It is simpler, more cost-effective, and easier to manage. Consider agentic RAG only when there is clear evidence that single-pass retrieval fails for a significant portion of queries, or when the cost of incorrect answers justifies the additional verification and iterative evidence gathering.

A practical compromise is to begin with classic RAG and introduce a controlled second pass only when failure signals arise, such as missing citations, low retrieval confidence, contradictory evidence, or repeated user follow-ups. If second-pass usage becomes frequent, implementing an agent loop with defined budgets and stop conditions may be beneficial.

For further exploration of improved retrieval, evaluation, and tool-calling patterns, the following references are recommended.

*   [Dense Passage Retrieval (DPR)](https://arxiv.org/abs/2004.04906)
*   [HyDE (query expansion for better retrieval)](https://arxiv.org/abs/2212.10496)
*   [BEIR benchmark (evaluate retrievers beyond one dataset)](https://arxiv.org/abs/2104.08663)
*   [RAGAS (RAG evaluation framework)](https://arxiv.org/abs/2309.15217)
*   [Toolformer](https://arxiv.org/abs/2302.07842)
*   [FiD-style multi-document generation](https://arxiv.org/abs/2007.01282)

* * *

Written By

Mostafa Ibrahim

[See all from Mostafa Ibrahim](https://towardsdatascience.com/author/mostafaibrahim18/)

[Agentic Ai](https://towardsdatascience.com/tag/agentic-ai/), [Agentic Rag](https://towardsdatascience.com/tag/agentic-rag/), [Ai Agent](https://towardsdatascience.com/tag/ai-agent/), [Deep Dives](https://towardsdatascience.com/tag/deep-dives/), [Rag](https://towardsdatascience.com/tag/rag/)

Share This Article

*   [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Ftowardsdatascience.com%2Fagentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop%2F&title=Agentic%20RAG%20vs%20Classic%20RAG%3A%20From%20a%20Pipeline%20to%20a%20Control%20Loop)
*   [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Ftowardsdatascience.com%2Fagentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop%2F&title=Agentic%20RAG%20vs%20Classic%20RAG%3A%20From%20a%20Pipeline%20to%20a%20Control%20Loop)
*   [Share on X](https://x.com/share?url=https%3A%2F%2Ftowardsdatascience.com%2Fagentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop%2F&text=Agentic%20RAG%20vs%20Classic%20RAG%3A%20From%20a%20Pipeline%20to%20a%20Control%20Loop)

Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.

[Write for TDS](https://towardsdatascience.com/questions-96667b06af5/)

## Related Articles

*   ![Image 9](https://towardsdatascience.com/wp-content/uploads/2023/06/087HNzG4rYaQmzRB3-scaled.jpg)## [If Oral and Written Communication Made Humans Develop Intelligence… What’s Up with Language Models?](https://towardsdatascience.com/if-oral-and-written-communication-made-humans-develop-intelligence-whats-up-with-language-models-b65ae22ac8e0/)

[Artificial Intelligence](https://towardsdatascience.com/category/artificial-intelligence/) Essay A discussion at the frontier between science and fiction. Human intelligence, with its extraordinary… [Luciano Abriata](https://towardsdatascience.com/author/lucianosphere/) June 30, 2023  15 min read      
*   ## [How to Build an LLM from Scratch](https://towardsdatascience.com/how-to-build-an-llm-from-scratch-8c477768f1f9/)

[Data Science](https://towardsdatascience.com/category/data-science/) Data Curation, Transformers, Training at Scale, and Model Evaluation [Shaw Talebi](https://towardsdatascience.com/author/shawhin/) September 21, 2023  20 min read      
*   ![Image 10](https://towardsdatascience.com/wp-content/uploads/2023/09/1J16KiNF4M_XxPkALZFUJHw-scaled.jpeg)## [10 Ways to Improve the Performance of Retrieval Augmented Generation Systems](https://towardsdatascience.com/10-ways-to-improve-the-performance-of-retrieval-augmented-generation-systems-5fa2cee7cd5c/)

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/) Tools to go from prototype to production [Matt Ambrogi](https://towardsdatascience.com/author/mattambrogi/) September 18, 2023  11 min read      
*   ## [All You Need to Know to Build Your First LLM App](https://towardsdatascience.com/all-you-need-to-know-to-build-your-first-llm-app-eb982c78ffac/)

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/) A step-by-step tutorial to document loaders, embeddings, vector stores and prompt templates [Dominik Polzer](https://towardsdatascience.com/author/dmnkplzr/) June 22, 2023  31 min read      
*   ## [How to Fine-Tune Llama2 for Python Coding on Consumer Hardware](https://towardsdatascience.com/how-to-fine-tune-llama2-for-python-coding-on-consumer-hardware-46942fa3cf92/)

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/) Enhancing Llama2’s proficiency in Python through supervised fine-tuning and low-rank adaptation techniques [Luís Roque](https://towardsdatascience.com/author/luisroque/) August 17, 2023  22 min read      
*   ## [Large Language Models, GPT-1 – Generative Pre-Trained Transformer](https://towardsdatascience.com/large-language-models-gpt-1-generative-pre-trained-transformer-7b895f296d3b/)

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/) Diving deeply into the working structure of the first ever version of gigantic GPT-models [Vyacheslav Efimov](https://towardsdatascience.com/author/slavahead/) January 27, 2024  11 min read      
*   ![Image 11: Image generated by DALL·E 3](https://towardsdatascience.com/wp-content/uploads/2024/03/1s6xecLnXymAByi6yyjJveg.png)## [Create an Agent with OpenAI Function Calling Capabilities](https://towardsdatascience.com/create-an-agent-with-openai-function-calling-capabilities-ad52122c3d12/)

[Large Language Models](https://towardsdatascience.com/category/artificial-intelligence/large-language-models/) OpenAI Function Calling in 2024 [Tianyi Li](https://towardsdatascience.com/author/bianbianzhu123/) March 31, 2024  18 min read      

*   [YouTube](https://www.youtube.com/c/TowardsDataScience)
*   [X](https://x.com/TDataScience)
*   [LinkedIn](https://www.linkedin.com/company/towards-data-science/?originalSubdomain=ca)
*   [Threads](https://www.threads.net/@towardsdatascience)
*   [Bluesky](https://bsky.app/profile/towardsdatascience.com)

[![Image 12: Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)

Your home for data science and Al. The world’s leading publication for data science, data analytics, data engineering, machine learning, and artificial intelligence professionals.

 © Insight Media Group, LLC 2026 

 Subscribe to Our Newsletter 

*   [Write For TDS](https://towardsdatascience.com/questions-96667b06af5/)
*   [About](https://towardsdatascience.com/about-towards-data-science-d691af11cc2f/)
*   [Advertise](https://contact.towardsdatascience.com/advertise-with-towards-data-science)
*   [Privacy Policy](https://towardsdatascience.com/privacy-policy/)
*   [Terms of Use](https://towardsdatascience.com/website-terms-of-use/)

Some areas of this page may shift around if you resize the browser window. Be sure to check heading and document order.

![Image 14](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=cd6b4b1e-5c52-4f59-b815-70191116b436&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=303aa5f6-651c-4492-8933-c086e9ae9570&pt=Agentic%20RAG%20vs%20Classic%20RAG%3A%20From%20a%20Pipeline%20to%20a%20Control%20Loop%20%7C%20Towards%20Data%20Science&tw_document_href=https%3A%2F%2Ftowardsdatascience.com%2Fagentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop%2F&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1777528448947.460678145241495324&txn_id=q494r&type=javascript&version=2.3.53)![Image 15](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=cd6b4b1e-5c52-4f59-b815-70191116b436&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=303aa5f6-651c-4492-8933-c086e9ae9570&pt=Agentic%20RAG%20vs%20Classic%20RAG%3A%20From%20a%20Pipeline%20to%20a%20Control%20Loop%20%7C%20Towards%20Data%20Science&tw_document_href=https%3A%2F%2Ftowardsdatascience.com%2Fagentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop%2F&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1777528448947.460678145241495324&txn_id=q494r&type=javascript&version=2.3.53)

#### Recommended Articles

Close

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