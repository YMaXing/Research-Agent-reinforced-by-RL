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

### Source [2]: https://medium.com/@tahirbalarabe2/retrieval-augmented-generation-vs-fine-tuning-enhancing-llms-697e7a0cf7e0

Query: What are the theoretical foundations of Retrieval-Augmented Generation that make it superior to fine-tuning for addressing LLM hallucinations and static knowledge cutoffs?

Answer: Fine-tuning embeds knowledge into model weights but suffers from knowledge cutoffs, requiring retraining for new data. RAG is superior for dynamic data as it retrieves external information at inference, avoiding static cutoffs. Factors favoring RAG: constantly updating external information and source transparency. Fine-tuning suits static, domain-specific knowledge but not updates.

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

### Source [13]: https://medium.com/@gaddam.rahul.kumar/agentic-rag-vs-traditional-rag-b1a156f72167

Query: What distinguishes agentic RAG from standard linear RAG pipelines, especially when retrieval functions as a tool in a ReAct-style agent's reasoning and iteration loop?

Answer: Agentic RAG makes retrieval intelligent via an agent with multiple tools (e.g., vector DB, web search, calculator, API), choosing strategies based on query. Agent uses LLM reasoning to iterate: retrieve, observe, decide if more info or different tool needed, repeat before final answer. Inspired by ReAct (Reason+Act): LLM thinks (chain-of-thought) then acts (tool call). Architecture: single-agent router in loop between query and answer, deciding tools/knowledge sources (e.g., DB A vs B, web search), reasoning which fits, retrieving/computing, feeding to final answer. Upgrades traditional RAG's static single-source retrieval with dynamic planning: agent (LLM-based) plans actions, uses tools, decides in multi-step loop, replacing simple retrieval→generation with intelligent controller determining whether/what/which tool/how to proceed based on results. Introduces adaptability and autonomy.

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

### Source [27]: https://www.aimon.ai/posts/rag_and_its_different_components/

Query: How do the augmentation and generation components in core RAG architectures transform retrieved information into contextually grounded LLM outputs?

Answer: The process begins with curating and indexing documents into a vector database. When a user submits a query, the system searches the vector database for relevant information. This retrieved information is then combined with the user’s query to form an enriched input, providing the necessary context for the LLM to generate a coherent and contextually informed response. Once the relevant data is retrieved, it is passed to an LLM as part of the input context. The LLM uses this retrieved context to generate outputs that are informed by relevant knowledge. Retrieval transforms the query into a vector embedding and searches the database using similarity metrics to locate matching data, which is combined with the query for enriched input to the LLM.

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

<research_source type="scraped_from_research" phase="exploitation" file="advanced-rag-techniques-for-high-performance-llm-application.md">
<details>
<summary>Advanced RAG Techniques for High-Performance LLM Applications</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://neo4j.com/blog/genai/advanced-rag-techniques/>

# Advanced RAG Techniques for High-Performance LLM Applications

https://dist.neo4j.com/wp-content/uploads/20240517073021/tomaz-bratanic-150x150.jpeg

https://dist.neo4j.com/wp-content/uploads/20251015110239/isobel-kruger-150x150.jpeg

Tomaž Bratanič,

Isobel Krüger

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

#### Knowledge Graph Retrieval (GraphRAG)

When your content contains rich entities and relationships (such as people, products, cases, citations), a knowledge graph lets you retrieve the _context of your data_, not just similar text. You can blend graph traversals with vector search to assemble precise, connected context for the prompt.

**Why graphs matter:** Vector/semantic search is strong for local lookups but struggles with global, cross-document questions and multi-hop relationships. Start by modeling your sources as entities and relationships, then retrieve in two ways: run local traversals to pull related entities and paths around initial hits, and use global community summaries for big-picture questions. This structured approach makes it much easier to retrieve and use specific information, expanding the types of questions you can answer with greater accuracy.

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

Chunk sizes and boundaries strongly influence retrieval quality. Default to fixed-size or sentence-aware splits, layer in semantic chunking when boundaries are messy, and reach for document-aware/adaptive chunkers when structure matters (table, headers, code). When you’re ready to wire it up, the LangChain text-splitter docs have drop-in examples.

#### Parent Retriever

Keep document structure intact by retrieving smaller “child” chunks but swapping in the “parent” block when many children from the same section appear, preserving context and reducing fragmented prompts.

#### Text Summarization / Context Distillation

Summarize the hits so more relevant info fits in the window and the model focuses on the right facts. Most stacks support this: GraphRAG uses query-focused summarization, LangChain has a ContextualCompressionRetriever, and LlamaIndex offers tree/refine synthesizers.

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

    -   **LangChain / LangGraph**: Use them for orchestration (e.g., routing sub-questions to the right tool, managing agents, and handling plan → route → act → verify → stop loops). Pair them with Neo4j’s GenAI ecosystem components like LLM Graph Builder (to create knowledge graphs) and Model Context Protocol (to connect agents and LLMs to graph queries). Read this blog post to learn how to use the neo4j-advanced-rag template and host it using LangServe.
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

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop.md">
<details>
<summary>Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/>

# Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop

A practical guide to choosing between single-pass pipelines and adaptive retrieval loops based on your use case's complexity, cost, and reliability requirements

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

| Dimension | Classic RAG | Agentic RAG |
| :-------- | :---------- | :---------- |
| Cost predictability | High | Lower (depends on loop depth) |
| Latency predictability | High | Lower (p95 grows with iterations) |
| Multi-hop queries | Often weak | Stronger |
| Debugging surface | Smaller | Larger |
| Failure modes | Mostly retrieval + prompt | Adds loop control failures |

## Decision Framework: When to stay classic vs go agentic

A practical approach to choosing between classic and agentic RAG is to evaluate your use case along two axes: query complexity (the extent of multi-step reasoning or evidence gathering required) and error tolerance (the risk associated with incorrect answers for users or the business). Classic RAG is a strong default due to its predictability. Agentic RAG is preferable when tasks frequently require retries, decomposition, or cross-source verification.

### Decision matrix: complexity × error tolerance

Here, **high error tolerance** means a wrong answer is acceptable (low stakes), while **low error tolerance** means a wrong answer is costly (high stakes).

|                   | High error tolerance                                                                         | Low error tolerance                                                                          |
| :---------------- | :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| Low Complexity    | **Classic RAG** for fast answers and predictable latency/cost.                               | **Classic RAG** with citations, careful retrieval, escalation                                |
| High Complexity   | **Classic RAG + second pass on failure signals** (only loop when needed).                    | **Agentic RAG** with strict stop conditions, budgets, and debugging                          |

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

<research_source type="scraped_from_research" phase="exploitation" file="fine-tuning-or-retrieval-comparing-knowledge-injection-in-ll.md">
<details>
<summary>Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2312.05934v3>

# Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs

Oded Ovadia
Corresponding author.Equal contribution.
{odedovadia,t-mbrief,mmishaeli,oren.elisha}@microsoft.com

Microsoft, Israel
Menachem Brief00footnotemark: 0{odedovadia,t-mbrief,mmishaeli,oren.elisha}@microsoft.com

Microsoft, Israel
Moshik Mishaeli
{odedovadia,t-mbrief,mmishaeli,oren.elisha}@microsoft.com

Microsoft, Israel
Oren Elisha
{odedovadia,t-mbrief,mmishaeli,oren.elisha}@microsoft.com

Microsoft, Israel

###### Abstract

Large language models (LLMs) encapsulate a vast amount of factual information within their pre-trained weights, as evidenced by their ability to answer diverse questions across different domains. However, this knowledge is inherently limited, relying heavily on the characteristics of the training data. Consequently, using external datasets to incorporate new information or refine the capabilities of LLMs on previously seen information poses a significant challenge. In this study, we compare two common approaches: unsupervised fine-tuning and retrieval-augmented generation (RAG). We evaluate both approaches on a variety of knowledge-intensive tasks across different topics. Our findings reveal that while unsupervised fine-tuning offers some improvement, RAG consistently outperforms it, both for existing knowledge encountered during training and entirely new knowledge. Moreover, we find that LLMs struggle to learn new factual information through unsupervised fine-tuning, and that exposing them to numerous variations of the same fact during training could alleviate this problem.

Keywords: LLMs, NLP, Fine-Tuning vs. RAG, Knowledge and Factuality.

## 1 Introduction

Large language models (LLMs) are able to capture vast amounts of factual information (Petroni et al., [2019](https://arxiv.org/html/2312.05934v3#bib.bib32 ""); Cohen et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib8 ""); Hu et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib13 "")). LLMs exhibit a remarkable level of knowledge in various domains due to their massive pre-training datasets. However, there are two significant limitations to this knowledge. First, it is static and does not update with time. Second, it is non-specific and thus may lack nuanced expertise in particular domains. While these are two different problems, they are deeply related since their solution is the same: enhancing the model’s knowledge.

Recently, the idea of adapting LLMs to particular domains and updating their knowledge has become increasingly common (Yu et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib54 "")). Various models have been suggested to improve factual knowledge and capabilities in diverse fields such as healthcare (Singhal et al., [2023a](https://arxiv.org/html/2312.05934v3#bib.bib39 ""), [b](https://arxiv.org/html/2312.05934v3#bib.bib40 ""); Wu et al., [2023a](https://arxiv.org/html/2312.05934v3#bib.bib50 "")), finance (Wu et al., [2023b](https://arxiv.org/html/2312.05934v3#bib.bib51 ""); Yang et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib53 "")), and law (Huang et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib14 ""); Nguyen, [2023](https://arxiv.org/html/2312.05934v3#bib.bib28 "")).

In this work, we focus on the evaluation of a model’s knowledge and its ability to memorize, understand, and retrieve factual data. We aim to understand the concept of knowledge injection(Wang et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib48 ""); Chen et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib4 ""); Liu et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib22 ""); Lauscher et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib20 "")). Given some knowledge base in the form of a text corpus, what is the best way to teach a pre-trained model this knowledge?

One way to add knowledge to a pre-trained model is through fine-tuning. With fine-tuning, we continue the model’s training process and adapt it using task-specific data. By exposing the model to a specific knowledge base, we expect the model weights to adapt accordingly. This process is meant to optimize the model for targeted applications, enhancing its performance and contextual relevance in specialized domains.

Another method to enhance a model’s knowledge base is through the use of in-context learning (ICL) (Chen et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib5 ""); Radford et al., [2019](https://arxiv.org/html/2312.05934v3#bib.bib33 ""); Min et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib24 ""); Lampinen et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib19 "")). The main idea behind ICL is to improve the performance of pre-trained LLMs on new tasks by modifying the input query to the model without directly changing the weights of the model. One form of ICL is retrieval augmented generation (RAG) (Lewis et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib21 ""); Neelakantan et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib27 "")). RAG uses information retrieval techniques to enable LLMs to obtain relevant information from a knowledge source and incorporate it into generated text.

This study aims to evaluate the knowledge injection capabilities of LLMs through a comparison of fine-tuning and RAG. To illustrate the rationale, let us use an analogy. Consider three college students taking a test on a specific topic. All had access to class materials but didn’t know the topic beforehand. The first student had the textbook only during the test, the second had pre-test access and studied, and the third lost access upon the test announcement. Who would probably perform better?

## 2 Background

https://arxiv.org/html/2312.05934v3/extracted/5377658/media/Wikipedia.jpgFigure 1: A visualization of the knowledge injection framework.

To assess knowledge injection, we must first understand what knowledge means for LLMs.

Knowledge and Language Models  Defining knowledge is a complex philosophical task far beyond the scope of this research. However, we can examine what factual knowledge means in the context of language models. If a model knows a fact, it can accurately and consistently answer questions about it. Furthermore, it can reliably distinguish between true and false statements related to this fact. We can then extend this definition to a whole knowledge base, not just a single fact.

Mathematically, let 𝒬={qn}n=1N𝒬superscriptsubscriptsubscript𝑞𝑛𝑛1𝑁\\mathcal{Q}=\\{q\_{n}\\}\_{n=1}^{N}caligraphic\_Q = { italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT italic\_n = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT be a set of N𝑁Nitalic\_N multiple choice factual questions, where each question has L𝐿Litalic\_L possible answers and exactly one correct answer. Let 𝒜={(an1,…,anL)}n=1N𝒜superscriptsubscriptsuperscriptsubscript𝑎𝑛1…superscriptsubscript𝑎𝑛𝐿𝑛1𝑁\\mathcal{A}=\\{(a\_{n}^{1},\\ldots,a\_{n}^{L})\\}\_{n=1}^{N}caligraphic\_A = { ( italic\_a start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT 1 end\_POSTSUPERSCRIPT , … , italic\_a start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_L end\_POSTSUPERSCRIPT ) } start\_POSTSUBSCRIPT italic\_n = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT be the corresponding set of possible answers, and 𝒞={cn}n=1N𝒞superscriptsubscriptsubscript𝑐𝑛𝑛1𝑁\\mathcal{C}=\\{c\_{n}\\}\_{n=1}^{N}caligraphic\_C = { italic\_c start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT italic\_n = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT be the correct answers.

Let ℳℳ\\mathcal{M}caligraphic\_M be a language model. We denote by ℳ⁢(qn)∈{an1,…,anL}ℳsubscript𝑞𝑛superscriptsubscript𝑎𝑛1…superscriptsubscript𝑎𝑛𝐿\\mathcal{M}(q\_{n})\\in\\{a\_{n}^{1},\\ldots,a\_{n}^{L}\\}caligraphic\_M ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) ∈ { italic\_a start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT 1 end\_POSTSUPERSCRIPT , … , italic\_a start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_L end\_POSTSUPERSCRIPT } the predicted answer of the model to the n𝑛nitalic\_n-th question.

We define the knowledge scoreℒℒ\\mathcal{L}caligraphic\_L of ℳℳ\\mathcal{M}caligraphic\_M in relation to 𝒬𝒬\\mathcal{Q}caligraphic\_Q to be the standard accuracy score:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒℳ,𝒬:=#⁢{qn\|ℳ⁢(qn)=cn}N.assignsubscriptℒℳ𝒬#conditional-setsubscript𝑞𝑛ℳsubscript𝑞𝑛subscript𝑐𝑛𝑁\\mathcal{L}\_{\\mathcal{M},\\mathcal{Q}}:=\\frac{\\#\\{q\_{n}\|\\;\\mathcal{M}(q\_{n})=c\_%<br>{n}\\}}{N}.caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT := divide start\_ARG # { italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT \| caligraphic\_M ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) = italic\_c start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT } end\_ARG start\_ARG italic\_N end\_ARG . |  | (1) |

We say that the model ℳℳ\\mathcal{M}caligraphic\_M possesses any knowledge regarding the set of questions 𝒬𝒬\\mathcal{Q}caligraphic\_Q if the following holds:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒℳ,𝒬>1L.subscriptℒℳ𝒬1𝐿\\mathcal{L}\_{\\mathcal{M},\\mathcal{Q}}>\\frac{1}{L}.caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT > divide start\_ARG 1 end\_ARG start\_ARG italic\_L end\_ARG . |  | (2) |

In simpler terms, the model can consistently give correct answers, outperforming a simple random guessing baseline. Naturally, if the knowledge score ℒℳ,𝒬subscriptℒℳ𝒬\\mathcal{L}\_{\\mathcal{M},\\mathcal{Q}}caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT is higher for one model compared to another, then we assert that the former is more knowledgeable with regards to 𝒬𝒬\\mathcal{Q}caligraphic\_Q compared to the latter.

Previously Seen Knowledge  One important distinction to make is between knowledge that the model has been exposed to before during pre-training as opposed to entirely new facts. Considering the size of modern LLM training sets, they cover a vast amount of information available through web-sourced text. As a result, even in niche domains, the goal of knowledge injection is not necessarily to teach the model entirely new facts but rather to ”refresh” its memory by inducing a bias toward a particular domain.

Knowledge and Reasoning  We emphasize that this knowledge evaluation framework for LLMs is imperfect. Importantly, it doesn’t address other quality metrics influencing a model’s response. Creating a purely knowledge-intensive dataset without involving some level of reasoning is challenging. Consequently, a model with robust reasoning abilities might excel on unfamiliar knowledge-intensive tasks by making ”educated guesses” in a multiple-choice exam. Therefore, any evaluation of knowledge in LLMs should consider this, with results seen as part of a broader range of benchmarks for reasoning (Sakaguchi et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib35 "")), reading comprehension (Dua et al., [2019](https://arxiv.org/html/2312.05934v3#bib.bib9 "")), and general language abilities (Srivastava et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib41 "")). However, this evaluation framework still strongly emphasizes factual information above all else.

Causes for Factual Errors  There are many possible reasons for the failure of models to answer factual questions accurately. In (Wang et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib47 "")), Wang et al. introduce a taxonomy of five main model-level causes:

- •

Domain knowledge deficit: A language model may lack comprehensive expertise in a specific domain to which it has not been exposed. For example, a model trained exclusively on texts written by William Shakespeare would perform poorly when asked about the works of Mark Twain.

- •

Outdated Information: LLMs invariably have a cutoff date determined by their training dataset. Consequently, any events, discoveries, or changes occurring after the last training update will not be within the model’s knowledge without access to external sources.

- •

Immemorization: Sometimes, a model is exposed to knowledge during its training process but does not retain it. This is especially true for rare facts that appear in the training dataset only scarcely (Kandpal et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib17 "")).

- •

Forgetting: Language models often undergo additional training after the pre-training phase (fine-tuning). In some cases, this might lead to a phenomenon called catastrophic forgetting(Kirkpatrick et al., [2017](https://arxiv.org/html/2312.05934v3#bib.bib18 ""); Goodfellow et al., [2013](https://arxiv.org/html/2312.05934v3#bib.bib11 ""); Chen et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib3 ""); Luo et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib23 "")), where models lose some of the knowledge they had prior to the fine-tuning process.

- •

Reasoning Failure: In certain instances, a language model might possess relevant knowledge about a fact but fail to utilize it properly. This is particularly evident in complex multi-step reasoning tasks (Tan et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib42 "")) or when posed with different questions about the same fact, resulting in disparate outcomes (Berglund et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib2 "")).


We observe that most of these issues arise during the pre-training phase, with catastrophic forgetting being the notable exception. Hence, many LLMs will suffer from factual errors of this kind regardless of any post-training process.

## 3 Injecting Knowledge to Language Models

Following the background given in [Section2](https://arxiv.org/html/2312.05934v3#S2 "2 Background ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"), it is clear that general pre-training is insufficient for many knowledge-intensive tasks. To solve this, an additional post-processing step is essential to augment the knowledge of a pre-trained model. This step is often reffered to as knowledge injection(Wang et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib48 ""); Chen et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib4 ""); Liu et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib22 ""); Lauscher et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib20 "")).

In this section, we examine two widely used frameworks for knowledge injection: fine-tuning (FT) and retrieval augmented generation (RAG). We begin by formulating the knowledge injection problem, aiming to explain both methods using consistent terminology.

### 3.1 Problem formulation

In [Equations1](https://arxiv.org/html/2312.05934v3#S2.E1 "1 ‣ 2 Background ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs") and [2](https://arxiv.org/html/2312.05934v3#S2.E2 "2 ‣ 2 Background ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"), we presented a formulation for knowledge in language models through the lens of question-answering (Q&A). We now extend this formulation to the problem of knowledge injection using the same terminology.

Given a set of factual questions, there exists some text corpus containing information that is relevant to these questions. The central assumption of knowledge injection is that given full access to this corpus, it could serve as an auxiliary knowledge base and improve the model’s performance on this set of questions.

Mathematically, let ℳℳ\\mathcal{M}caligraphic\_M be a pre-trained model, and let 𝒬𝒬\\mathcal{Q}caligraphic\_Q be a set of factual questions, as before. Now, assume we have a relevant auxiliary knowledge base ℬ𝒬subscriptℬ𝒬\\mathcal{B}\_{\\mathcal{Q}}caligraphic\_B start\_POSTSUBSCRIPT caligraphic\_Q end\_POSTSUBSCRIPT. Our objective is to discover a transformation, denoted as ℱℱ\\mathcal{F}caligraphic\_F, that, when applied, would enhance the knowledge about 𝒬𝒬\\mathcal{Q}caligraphic\_Q:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℳ′:=ℱ(ℳ,ℬ𝒬)s.t.ℒℳ′,𝒬>ℒℳ,𝒬.\\mathcal{M^{\\prime}}:=\\mathcal{F}(\\mathcal{M},\\mathcal{B}\_{\\mathcal{Q}})\\quad s%<br>.t.\\quad\\mathcal{L}\_{\\mathcal{M^{\\prime}},\\mathcal{Q}}>\\mathcal{L}\_{\\mathcal{M%<br>},\\mathcal{Q}}.caligraphic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT := caligraphic\_F ( caligraphic\_M , caligraphic\_B start\_POSTSUBSCRIPT caligraphic\_Q end\_POSTSUBSCRIPT ) italic\_s . italic\_t . caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT , caligraphic\_Q end\_POSTSUBSCRIPT > caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT . |  | (3) |

In this work, we aim to compare two choices for ℱℱ\\mathcal{F}caligraphic\_F: fine-tuning and RAG to see which option performs better in this problem.

### 3.2 Fine-Tuning

Fine-tuning is the process of adjusting a pre-trained model on a specific, often narrower, dataset or task to enhance its performance in that particular domain. Here, it is vital to distinguish between different types of fine-tuning. FT techniques are commonly classified into supervised, unsupervised, and reinforcement learning (RL) based methods. We proceed by briefly reviewing these methods and their relation to the problem of knowledge injection.

Supervised Fine-Tuning  Supervised fine-tuning (SFT) requires sets of labeled input-output pairs. One of the most common SFT methods is instruction tuning (Wang et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib49 ""); Mishra et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib25 ""); Ouyang et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib31 ""); Taori et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib43 "")), which has emerged as one of the most powerful methods to improve model performance. With instruction tuning, the input is a natural language task description, and the output is an example of the desired behavior. Many current state-of-the-art LLMs have gone through instruction tuning after their pre-training phase.

Instruction tuning has been shown to be very effective at improving the overall quality of the model, with a particular emphasis on its zero-shot and reasoning capabilities. However, despite these advantages, instruction tuning does not necessarily teach the model new knowledge (Ouyang et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib31 ""); Chung et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib7 ""); Mitra et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib26 ""); Chia et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib6 ""); Zhou et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib55 "")). As such, instruction tuning alone is not a viable solution to the knowledge injection problem.

Reinforcemnt Learning  Another form of FT relies on RL or RL-inspired optimization strategies to better align the model after its pre-training phase. A few prominent examples are reinforcement learning from human feedback (RLHF) (OpenAI, [2023](https://arxiv.org/html/2312.05934v3#bib.bib30 ""); Touvron et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib45 "")), direct preference optimization (DPO) (Rafailov et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib34 "")), and proximal policy optimization (PPO) (Schulman et al., [2017](https://arxiv.org/html/2312.05934v3#bib.bib36 ""); Tunstall et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib46 "")).

These techniques have been shown to be very useful, especially when used in conjunction with instruction tuning. However, similarly to instruction tuning, these methods focus on the overall quality of the response and its expected behavior and not necessarily on its breadth of knowledge.

Unsupervised Fine-Tuning  The final FT strategy we discuss is unsupervised, meaning there are no available labels for the model to learn from. One common unsupervised FT technique is often referred to as continual pre-training or unstructured FT.

In this method, the FT process is viewed as a direct continuation of the pre-training phase. We start with a saved checkpoint of the original LLM and train it in a causal auto-regressive manner, i.e., predicting the next token. One major difference in comparison to actual pre-training is the learning rate. Usually, one would need a much lower learning rate when continuing the pre-training of the model to avoid catastrophic forgetting (Kirkpatrick et al., [2017](https://arxiv.org/html/2312.05934v3#bib.bib18 "")).

It is well known that LLMs store vast amounts of knowledge during their pre-training phase (Zhou et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib55 "")). So, it makes sense to continue this process in order to inject knowledge into the model. Hence, we use the unsupervised FT approach throughout this work and evaluate its efficacy in enhancing the model’s capacity for learning new information.

### 3.3 Retrieval Augmented Generation

Retrieval augmented generation (RAG) (Lewis et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib21 "")) is a technique that expands LLMs’ capabilities, especially in knowledge-intensive tasks, by using external knowledge sources. While the original formulation involved additional training per task, it has since been demonstrated (Neelakantan et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib27 "")) that a pre-trained embedding model can achieve improved performance with no additional training involved.

The idea is that given an auxiliary knowledge base and an input query, we use the RAG architecture to find documents within the knowledge base that resemble the input query. These documents are then added to the input query, thus giving the model further context about the subject of the query.

In practice, implementing the suggested architecture is quite straightforward: Given an auxiliary knowledge base ℬ𝒬subscriptℬ𝒬\\mathcal{B}\_{\\mathcal{Q}}caligraphic\_B start\_POSTSUBSCRIPT caligraphic\_Q end\_POSTSUBSCRIPT and a pre-trained embedding model ℳesubscriptℳ𝑒\\mathcal{M}\_{e}caligraphic\_M start\_POSTSUBSCRIPT italic\_e end\_POSTSUBSCRIPT, we create a dense vector representation (embedding) per document b∈ℬ𝒬𝑏subscriptℬ𝒬b\\in\\mathcal{B}\_{\\mathcal{Q}}italic\_b ∈ caligraphic\_B start\_POSTSUBSCRIPT caligraphic\_Q end\_POSTSUBSCRIPT and store these in a vector store. Upon receiving a new query q𝑞qitalic\_q, we use its embedding, ℳe⁢(q)subscriptℳ𝑒𝑞\\mathcal{M}\_{e}(q)caligraphic\_M start\_POSTSUBSCRIPT italic\_e end\_POSTSUBSCRIPT ( italic\_q ), to retrieve q𝑞qitalic\_q’s top-K𝐾Kitalic\_K closest neighbors, 𝐛q={bk}1Ksubscript𝐛𝑞superscriptsubscriptsubscript𝑏𝑘1𝐾\\mathbf{b}\_{q}=\\{b\_{k}\\}\_{1}^{K}bold\_b start\_POSTSUBSCRIPT italic\_q end\_POSTSUBSCRIPT = { italic\_b start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_K end\_POSTSUPERSCRIPT, according to dot-product ranking. We then update q𝑞qitalic\_q to be q~=𝐛q∥q~𝑞conditionalsubscript𝐛𝑞𝑞\\tilde{q}=\\mathbf{b}\_{q}\\\|qover~ start\_ARG italic\_q end\_ARG = bold\_b start\_POSTSUBSCRIPT italic\_q end\_POSTSUBSCRIPT ∥ italic\_q, where ∥∥\\\|∥ denotes string concatenation. Finally, we return ℳ⁢(q~)ℳ~𝑞\\mathcal{M}(\\tilde{q})caligraphic\_M ( over~ start\_ARG italic\_q end\_ARG ) as the model’s output.

## 4 Knowledge Base Creation

Table 1: Results for the MMLU datasets described in [Section4.1](https://arxiv.org/html/2312.05934v3#S4.SS1 "4.1 Task Selection and Rationale ‣ 4 Knowledge Base Creation ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs") in terms of log-likelihood accuracy ( [Equation4](https://arxiv.org/html/2312.05934v3#S5.E4 "4 ‣ 5 Experiments and Results ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs")).

| Task | Model | Base model | Base model + RAG | Fine-tuned | Fine-tuned + RAG |
| --- | --- | --- | --- | --- | --- |
| Anatomy (0-shot) | Mistral 7B | 0.556 | 0.681 | 0.570 | 0.659 |
| Llama2 7B | 0.393 | 0.489 | 0.430 | 0.489 |
| Orca2 7B | 0.607 | 0.637 | 0.600 | 0.637 |
| Anatomy (5-shot) | Mistral 7B | 0.600 | 0.681 | 0.622 | 0.674 |
| Llama2 7B | 0.467 | 0.563 | 0.496 | 0.548 |
| Orca2 7B | 0.570 | 0.659 | 0.593 | 0.674 |
| Astronomy (0-shot) | Mistral 7B | 0.625 | 0.678 | 0.651 | 0.697 |
| Llama2 7B | 0.401 | 0.467 | 0.487 | 0.520 |
| Orca2 7B | 0.645 | 0.750 | 0.651 | 0.750 |
| Astronomy (5-shot) | Mistral 7B | 0.658 | 0.724 | 0.651 | 0.697 |
| Llama2 7B | 0.401 | 0.474 | 0.447 | 0.520 |
| Orca2 7B | 0.664 | 0.763 | 0.664 | 0.743 |
| College biology (0-shot) | Mistral 7B | 0.681 | 0.757 | 0.701 | 0.764 |
| Llama2 7B | 0.438 | 0.493 | 0.458 | 0.465 |
| Orca2 7B | 0.583 | 0.639 | 0.604 | 0.632 |
| College biology (5-shot) | Mistral 7B | 0.722 | 0.778 | 0.736 | 0.771 |
| Llama2 7B | 0.451 | 0.521 | 0.424 | 0.479 |
| Orca2 7B | 0.604 | 0.660 | 0.625 | 0.653 |
| College chemistry (0-shot) | Mistral 7B | 0.470 | 0.500 | 0.490 | 0.500 |
| Llama2 7B | 0.310 | 0.380 | 0.390 | 0.390 |
| Orca2 7B | 0.370 | 0.440 | 0.370 | 0.390 |
| College chemistry (5-shot) | Mistral 7B | 0.470 | 0.540 | 0.500 | 0.500 |
| Llama2 7B | 0.370 | 0.380 | 0.360 | 0.390 |
| Orca2 7B | 0.430 | 0.470 | 0.370 | 0.380 |
| Prehistory (0-shot) | Mistral 7B | 0.713 | 0.750 | 0.719 | 0.731 |
| Llama2 7B | 0.448 | 0.481 | 0.457 | 0.478 |
| Orca2 7B | 0.642 | 0.679 | 0.673 | 0.673 |
| Prehistory (5-shot) | Mistral 7B | 0.722 | 0.762 | 0.725 | 0.762 |
| Llama2 7B | 0.515 | 0.531 | 0.503 | 0.537 |
| Orca2 7B | 0.664 | 0.698 | 0.667 | 0.694 |

Table 2: Current events results. Models that were fine-tuned on the original dataset are labeled as FT-reg, while those trained on the dataset with multiple paraphrases are labeled as FT-par.

|  | Base model | Base model + RAG | FT-reg | FT-par | FT-reg + RAG | FT-par + RAG |
| --- | --- | --- | --- | --- | --- | --- |
| Mistral 7B | 0.481 | 0.875 | 0.504 | 0.588 | 0.810 | 0.830 |
| Llama2 7B | 0.353 | 0.585 | 0.219 | 0.392 | 0.326 | 0.520 |
| Orca2 7B | 0.456 | 0.876 | 0.511 | 0.566 | 0.820 | 0.826 |

### 4.1 Task Selection and Rationale

MMLU Benchmark  To properly evaluate the capabilities of LLMs on knowledge-intensive tasks, we selected four distinct tasks from the Massively Multilingual Language Understanding Evaluation (MMLU) benchmark (Hendrycks et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib12 "")) in the topics of anatomy, astronomy, college biology, college chemistry and prehistory. The chosen tasks were selected based on their emphasis on factual knowledge and the minimal reliance on reasoning. As a heuristic, we opted for tasks where the questions are short and involve no context. In practice we selected four STEM subjects as well as one humanities subject, to ensure the evaluation is not limited to certain fields. Note that prehistory involves questions spanning all non-modern history. This approach aims to enable us to test LLM proficiency in comprehending and manipulating information in isolation from its reasoning processes.

Current Events Task  To further isolate LLMs’ abilities to learn new knowledge, we created a task comprising multiple-choice questions about current events. This task includes multiple-choice questions about events that occurred after the cutoff of the various models’ training data. Specifically, we focused on ”current events” from the USA, in the time span of August-November 2023, that are included in the relevant Wikipedia indexes111 [https://en.wikipedia.org/wiki/Category:2023\_events\_in\_the\_United\_States\_by\_month](https://en.wikipedia.org/wiki/Category:2023_events_in_the_United_States_by_month ""). This method enables us to mostly guarantee that the models have not been exposed to these facts, thus allowing us to directly test knowledge injection capabilities.

### 4.2 Data Collection and Preprocessing

To effectively evaluate the LLMs’ performance on these knowledge-intensive tasks, a comprehensive auxiliary dataset was collected by scraping relevant articles per topic from Wikipedia. The rationale behind selecting Wikipedia as the primary source of knowledge is its broad coverage of relevant topics and its reliability as a repository of crowd-verified knowledge. All articles pertinent to the tasks were retrieved via the official Wikipedia API222 [https://www.mediawiki.org/wiki/API:Main\_page](https://www.mediawiki.org/wiki/API:Main_page "") by identifying the relevant central page per topic.

Subsequently, a rigorous cleaning process was utilized to transform the data from raw subsections to clean chunks. This step was done with the ”wikiextractor” tool (Attardi, [2015](https://arxiv.org/html/2312.05934v3#bib.bib1 "")). The division into small, clean (e.g., remove HTML, URLs, etc.) chunks was aimed at enhancing the evaluation of the LLMs’ understanding across various knowledge domains and aiding the LLMs in the fine-tuning process.

### 4.3 Current Events Task Creation

After collecting the relevant chunks from Wikipedia, we created a new multiple-choice dataset with the help of GPT-4 (OpenAI, [2023](https://arxiv.org/html/2312.05934v3#bib.bib30 "")). First, we removed any small chunks. For each remaining chunk in the corpus, GPT-4 was instructed to create four highly specific, high-quality multiple-choice questions with only one correct answer. By specific, we mean that the question can be answered without knowledge of which context the question refers to and with minimal ambiguity. Next, GPT-4 was asked to select the two most specific of the four. This was followed by a manual evaluation and verification step. In total, this resulted in 910 new questions.

### 4.4 Paraphrases Generation

After creating the dataset, we utilized GPT-4 to generate augmentations of the dataset. We instructed GPT-4 to provide paraphrased versions of the input data that fully retain the information while being reworded. Each paraphrasing iteration was done with a different seed to ensure variety.

We selected 240 chunks at random for each task and created two paraphrases per chunk. These were set aside to be used as validation sets for hyperparameter tuning. For the current events dataset, we created ten paraphrases for each chunk used in the fine-tuning process described in [Section6](https://arxiv.org/html/2312.05934v3#S6 "6 The Importance of Repetition ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs").

## 5 Experiments and Results

Experimental Framework  We used the popular LM-Evaluation-Harness (Gao et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib10 "")) repository to evaluate the performance of LLMs on the selected knowledge-intensive tasks. LM-Evaluation-Harness is a robust benchmarking tool that currently serves as the industry standard for model evaluation and is the basis of the HuggingFace leaderboard333 [https://huggingface.co/spaces/HuggingFaceH4/open\_llm\_leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard ""). Leveraging this platform ensured a standardized evaluation framework and allowed consistent comparison across models, methods, and datasets. More importantly, by using the industry standard for evaluation, we could avoid any differences stemming from prompt engineering and formatting issues and replicate the reported baseline results for each model.

Model Selection  We chose three models for inference evaluation: Llama2-7B (Touvron et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib45 "")), Mistral-7B (Jiang et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib15 "")), and Orca2-7B (Mitra et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib26 "")).
The choice of these models was meant to represent the most popular open-source base models and an instruction-tuned model across various baseline capabilities.
Additionally, we selected bge-large-en(Xiao et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib52 "")) as the embedding model for the RAG component and used FAISS (Johnson et al., [2019](https://arxiv.org/html/2312.05934v3#bib.bib16 "")) as its vector-store. This embedding model is currently the SOTA of open-source embedding models, according to the HuggingFace MTEB leaderboard444 [https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard "").

https://arxiv.org/html/2312.05934v3/extracted/5377658/media/peformance_gain.png

Figure 2: The relative accuracy gain (as explained in [Equation5](https://arxiv.org/html/2312.05934v3#S5.E5 "5 ‣ 5 Experiments and Results ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs")) for each knowledge-injection method, averaged (columnwise) across all experiments in [Table1](https://arxiv.org/html/2312.05934v3#S4.T1 "Table 1 ‣ 4 Knowledge Base Creation ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs").

Configuration Variations  Our evaluation included multiple configurations, with a grid-search over them, to allow for more comprehensive benchmarking.

Firstly, we compared the baseline and fine-tuned models and their performance with the RAG component. Secondly, we explored the optimal number of text chunks to add to the context in RAG. Specifically, different values of K∈{0,…,5}𝐾0…5K\\in\\{0,\\ldots,5\\}italic\_K ∈ { 0 , … , 5 } were employed to analyze the impact on model performance. Finally, we explored 5-shot performance vs. 0-shot.

Training Setup  We trained all of the models using the unsupervised training procedure described in [Section3.2](https://arxiv.org/html/2312.05934v3#S3.SS2 "3.2 Fine-Tuning ‣ 3 Injecting Knowledge to Language Models ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"). For each dataset, we
divided the auxiliary knowledge base into equal chunks of size 256256256256 by concatenating or splitting the original chunks based on their length. We also added two special tokens, <<<BOS>>> and <<<EOS>>>, to demarcate the original chunks’ beginnings and ends to preserve the documents’ structure.

The models were trained using learning rates between 1×10−61superscript1061\\times{10}^{-6}1 × 10 start\_POSTSUPERSCRIPT - 6 end\_POSTSUPERSCRIPT and 5×10−55superscript1055\\times{10}^{-5}5 × 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT, which were found through a hyperparameter search. All models were trained on 4 NVIDIA A-100 GPUs for a maximum of 5 epochs and a batch size of 64.

Evaluation method  All evaluations were done by appending each of the multiple-choice options to the question, followed by passing the concatenation through the model to get a log probability score per option. The highest score was interpreted as the model’s choice and used for accuracy calculation. More formally, this means that in [Equation1](https://arxiv.org/html/2312.05934v3#S2.E1 "1 ‣ 2 Background ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs") we say that ℳ⁢(qn)=cnℳsubscript𝑞𝑛subscript𝑐𝑛\\mathcal{M}(q\_{n})=c\_{n}caligraphic\_M ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) = italic\_c start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT if:

|     |     |     |     |
| --- | --- | --- | --- |
|  | cn=arg⁢maxl⁡{ℳ⁢(qn∥an1),…,ℳ⁢(qn∥anL)},subscript𝑐𝑛subscriptargmax𝑙ℳconditionalsubscript𝑞𝑛subscriptsuperscript𝑎1𝑛…ℳconditionalsubscript𝑞𝑛subscriptsuperscript𝑎𝐿𝑛c\_{n}=\\operatorname\*{arg\\,max}\_{l}\\{\\mathcal{M}(q\_{n}\\\|a^{1}\_{n}),\\ldots,%<br>\\mathcal{M}(q\_{n}\\\|a^{L}\_{n})\\},italic\_c start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT = start\_OPERATOR roman\_arg roman\_max end\_OPERATOR start\_POSTSUBSCRIPT italic\_l end\_POSTSUBSCRIPT { caligraphic\_M ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ∥ italic\_a start\_POSTSUPERSCRIPT 1 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) , … , caligraphic\_M ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ∥ italic\_a start\_POSTSUPERSCRIPT italic\_L end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) } , |  | (4) |

where ℳ⁢(qn∥anl)=log⁡Pℳ⁢(qn∥anl)ℳconditionalsubscript𝑞𝑛subscriptsuperscript𝑎𝑙𝑛subscript𝑃ℳconditionalsubscript𝑞𝑛subscriptsuperscript𝑎𝑙𝑛\\mathcal{M}(q\_{n}\\\|a^{l}\_{n})=\\log P\_{\\mathcal{M}}(q\_{n}\\\|a^{l}\_{n})caligraphic\_M ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ∥ italic\_a start\_POSTSUPERSCRIPT italic\_l end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) = roman\_log italic\_P start\_POSTSUBSCRIPT caligraphic\_M end\_POSTSUBSCRIPT ( italic\_q start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ∥ italic\_a start\_POSTSUPERSCRIPT italic\_l end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ).

MMLU Results  For each task and model, we compared four approaches: using just the base model, RAG, FT, and finally combining FT and RAG by using the fine-tuned model as the generator. Furthermore, we tested the MMLU tasks using both 0-shot and 5-shot scenarios. The full results are shown in  [Table1](https://arxiv.org/html/2312.05934v3#S4.T1 "Table 1 ‣ 4 Knowledge Base Creation ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"). An aggregation of the relative accuracy gain, i.e.,

|     |     |     |     |
| --- | --- | --- | --- |
|  | (ℒℳ′,𝒬−ℒℳ,𝒬)/ℒℳ,𝒬,subscriptℒsuperscriptℳ′𝒬subscriptℒℳ𝒬subscriptℒℳ𝒬(\\mathcal{L}\_{\\mathcal{M^{\\prime}},\\mathcal{Q}}-\\mathcal{L}\_{\\mathcal{M},%<br>\\mathcal{Q}})/{\\mathcal{L}\_{\\mathcal{M},\\mathcal{Q}}},( caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT , caligraphic\_Q end\_POSTSUBSCRIPT - caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT ) / caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT , |  | (5) |

where ℳℳ\\mathcal{M}caligraphic\_M is the base model and ℳ′superscriptℳ′\\mathcal{M^{\\prime}}caligraphic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT is the knowledge-injected model, is shown in  [Figure2](https://arxiv.org/html/2312.05934v3#S5.F2 "Figure 2 ‣ 5 Experiments and Results ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs").

In all cases, RAG performed significantly better compared to the base models. Furthermore, using RAG with the base model as the generator was consistently better than only fine-tuning. In some cases, using the fine-tuned model instead of the base model as the generator in the RAG pipeline improved results even further. However, this is not consistent and thus demonstrates the inherent instability of fine-tuning. Additionally, we found that the 5-shot approach boosts the results by a small margin in most cases, with a similar trend being observed in all of the different approaches.

Current Events Results  The evaluation on the current events task is shown in [Table2](https://arxiv.org/html/2312.05934v3#S4.T2 "Table 2 ‣ 4 Knowledge Base Creation ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"). RAG proves particularly effective due to the one-to-one correspondence between the questions and the auxiliary dataset (see [Section4.3](https://arxiv.org/html/2312.05934v3#S4.SS3 "4.3 Current Events Task Creation ‣ 4 Knowledge Base Creation ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs")). Fine-tuning is not competitive with RAG. However, fine-tuning with multiple paraphrases still provides a significant improvement over the baseline. We note that combining RAG with fine-tuning shows inferior performance compared to RAG alone.

It is worth noting that although the questions are based on information the models were not exposed to during training, the results of the base models surpass 1L=0.251𝐿0.25\\frac{1}{L}=0.25divide start\_ARG 1 end\_ARG start\_ARG italic\_L end\_ARG = 0.25. This can partially be explained by the models using reasoning and/or pre-existing knowledge when answering questions that are not independent of the past information. Some examples of this can be found in [AppendixC](https://arxiv.org/html/2312.05934v3#A3 "Appendix C Current Events Existing Knowledge Examples ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs").

Fine-Tuning vs. RAG: In the results of both the MMLU and current events tasks, a significant advantage for RAG over fine-tuning is evident. While fine-tuning improved results compared to the base model in most cases, it was not competitive with the RAG approach.

Several factors might contribute to this behavior. Firstly, RAG not only adds knowledge to a model but also incorporates context relevant to the question, a feature lacking in fine-tuning. Additionally, fine-tuning may impact other capabilities of the model due to a degree of catastrophic forgetting. Finally, it’s plausible that unsupervised fine-tuned models might benefit from further alignment through supervised or RL-based fine-tuning, as evidenced by the vastly improved performance of Orca2 over the base Llama2.

## 6 The Importance of Repetition

Unlike the other tasks, where the model has been exposed to aspects related to the topic during pretraining, current events includes new information. In this case, standard regular fine-tuning not only did not improve the performance of Llama2 but also significantly degraded it. To improve the fine-tuning results, we explored augmentation of the data using paraphrases.

https://arxiv.org/html/2312.05934v3/extracted/5377658/media/loss_curve.png

Figure 3: Training loss over time for Mistral-7B.https://arxiv.org/html/2312.05934v3/extracted/5377658/media/paraphrases_plot.pngFigure 4: Model accuracy on the current events task as a function of the number of paraphrases.

Data Augmentation Data augmentation is a well-established method for enhancing the performance of language models and has been surveyed extensively (Shorten et al., [2021](https://arxiv.org/html/2312.05934v3#bib.bib38 "")). Using generative models for augmentations has also been used successfully to improve classification models in the past (Sharma et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib37 "")).
An example of data augmentation using paraphrasing can be found in  [AppendixB](https://arxiv.org/html/2312.05934v3#A2 "Appendix B Paraphrase Examples ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs").

Monotonic Improvement This approach resulted in notable improvements in our results, showcasing a direct correlation between the number of paraphrases utilized and the models’ accuracy.
Our experimentation revealed a compelling trend, shown in [Figure4](https://arxiv.org/html/2312.05934v3#S6.F4 "Figure 4 ‣ 6 The Importance of Repetition ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"). For all models tested, the accuracy was a monotonically increasing function of the number of paraphrases used. This observation strongly suggests the positive impact of paraphrase augmentation, yielding information repetition, on the model’s ability to comprehend and generalize new knowledge from limited data.

Learning New Information In [Figure3](https://arxiv.org/html/2312.05934v3#S6.F3 "Figure 3 ‣ 6 The Importance of Repetition ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"), we can see an interesting phenomenon observed throughout our experiments. After each epoch, i.e., completing another iteration over the entire dataset, the training loss drops significantly. This is consistent with what is known about LLMs memorizing the data during training and overfitting (Tirumala et al., [2022](https://arxiv.org/html/2312.05934v3#bib.bib44 "")).

Our hypothesis is as follows:

> In order to teach pre-trained LLMs new knowledge, the knowledge must be repeated in numerous ways.
>

This is well known for LLM pre-training (Kandpal et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib17 "")), and we see in this case that this holds for fine-tuning as well. The rationale for this hypothesis is that mere memorization of sentences does not entail knowledge of their content, as was already shown in (Berglund et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib2 "")). By providing the information in numerous forms (like the data augmentation process we used), the various relationships in the data (e.g., a⟹b,b⁢／⟹cformulae-sequence𝑎𝑏𝑏𝑐a\\implies b,\\>b\\hbox to 0.0pt{$\\quad\\not$\\hss}\\implies citalic\_a ⟹ italic\_b , italic\_b ／ ⟹ italic\_c) stand a higher chance of appearing naturally. We believe this can potentially both increase ℒℳ,𝒬subscriptℒℳ𝒬\\mathcal{L}\_{\\mathcal{M},\\mathcal{Q}}caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_M , caligraphic\_Q end\_POSTSUBSCRIPT in general, as well as ameliorate Berglund et al.’s Reversal Curse. While promising, this result still warrants further research.

## 7 Conclusion and Future Work

Large language models possess vast amounts of knowledge on various topics. In this work, we tested their capability to adapt to new knowledge: both specialized and completely unseen. This is among the first studies to compare two prominent approaches in this domain, namely fine-tuning and retrieval augmented generation. While fine-tuning can be useful for many use-cases, we found that RAG is a more reliable choice for knowledge injection.

Some aspects of this work still warrant further research. For example, we focused on unsupervised training as our primary fine-tuning method, as opposed to instruction-tuning or RL-based methods. Researching combinations of various techniques, with diverse auxiliary knowledge bases, may yield improved results. This approach, combined with our hypothesis from [Section6](https://arxiv.org/html/2312.05934v3#S6 "6 The Importance of Repetition ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"), could further enhance our understanding of knowledge injection via FT.

While we believe that this work further enhances our understanding of knowledge in LLMs, there is a lot more work to be done in this field. Specifically, more research is required regarding the question of knowledge representation in LLMs, especially from a theoretical perspective.

Finally, further efforts are needed to measure knowledge in LLMs. While we employed an empirical approach as described in [Equation2](https://arxiv.org/html/2312.05934v3#S2.E2 "2 ‣ 2 Background ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"), it is important to explore other definitions and perspectives on knowledge as well, and extend upon this work.

## 8 Limitations

As in all machine learning applications, the choice of hyperparameters significantly impacts the results. We therefore strongly recommend optimizing all relevant hyperparameters for specific cases.

We have supported our claims by running the experiments on three different models. However, generalization to other LLMs should be tested thoroughly. For example, GPT-4 achieves near perfect accuracy for some MMLU tasks (Nori et al., [2023](https://arxiv.org/html/2312.05934v3#bib.bib29 "")), and thus further improvement is not applicable.

Finally, while we chose various topics for the knowledge bases, all of our sources came from Wikipedia. Other datasets may yield different results, and must be evaluated carefully.

## References

- Attardi (2015)↑
Attardi, G.

Wikiextractor.

[https://github.com/attardi/wikiextractor](https://github.com/attardi/wikiextractor ""), 2015.

- Berglund et al. (2023)↑
Berglund, L., Tong, M., Kaufmann, M., Balesni, M., Stickland, A. C., Korbak, T., and Evans, O.

The reversal curse: Llms trained on” a is b” fail to learn” b is a”.

_arXiv preprint arXiv:2309.12288_, 2023.

- Chen et al. (2020)↑
Chen, S., Hou, Y., Cui, Y., Che, W., Liu, T., and Yu, X.

Recall and learn: Fine-tuning deep pretrained language models with less forgetting.

_arXiv preprint arXiv:2004.12651_, 2020.

- Chen et al. (2022)↑
Chen, X., Zhang, N., Xie, X., Deng, S., Yao, Y., Tan, C., Huang, F., Si, L., and Chen, H.

Knowprompt: Knowledge-aware prompt-tuning with synergistic optimization for relation extraction.

In _Proceedings of the ACM Web conference 2022_, pp.  2778–2788, 2022.

- Chen et al. (2021)↑
Chen, Y., Zhong, R., Zha, S., Karypis, G., and He, H.

Meta-learning via language model in-context tuning.

_arXiv preprint arXiv:2110.07814_, 2021.

- Chia et al. (2023)↑
Chia, Y. K., Hong, P., Bing, L., and Poria, S.

Instructeval: Towards holistic evaluation of instruction-tuned large language models.

_arXiv preprint arXiv:2306.04757_, 2023.

- Chung et al. (2022)↑
Chung, H. W., Hou, L., Longpre, S., Zoph, B., Tay, Y., Fedus, W., Li, Y., Wang, X., Dehghani, M., Brahma, S., et al.

Scaling instruction-finetuned language models.

_arXiv preprint arXiv:2210.11416_, 2022.

- Cohen et al. (2023)↑
Cohen, R., Geva, M., Berant, J., and Globerson, A.

Crawling the internal knowledge-base of language models.

_arXiv preprint arXiv:2301.12810_, 2023.

- Dua et al. (2019)↑
Dua, D., Wang, Y., Dasigi, P., Stanovsky, G., Singh, S., and Gardner, M.

Drop: A reading comprehension benchmark requiring discrete reasoning over paragraphs.

_arXiv preprint arXiv:1903.00161_, 2019.

- Gao et al. (2021)↑
Gao, L., Tow, J., Biderman, S., Black, S., DiPofi, A., Foster, C., Golding, L., Hsu, J., McDonell, K., Muennighoff, N., Phang, J., Reynolds, L., Tang, E., Thite, A., Wang, B., Wang, K., and Zou, A.

A framework for few-shot language model evaluation, September 2021.

URL [https://doi.org/10.5281/zenodo.5371628](https://doi.org/10.5281/zenodo.5371628 "").

- Goodfellow et al. (2013)↑
Goodfellow, I. J., Mirza, M., Xiao, D., Courville, A., and Bengio, Y.

An empirical investigation of catastrophic forgetting in gradient-based neural networks.

_arXiv preprint arXiv:1312.6211_, 2013.

- Hendrycks et al. (2021)↑
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J.

Measuring massive multitask language understanding.

_Proceedings of the International Conference on Learning Representations (ICLR)_, 2021.

- Hu et al. (2023)↑
Hu, L., Liu, Z., Zhao, Z., Hou, L., Nie, L., and Li, J.

A survey of knowledge enhanced pre-trained language models.

_IEEE Transactions on Knowledge and Data Engineering_, 2023.

- Huang et al. (2023)↑
Huang, Q., Tao, M., An, Z., Zhang, C., Jiang, C., Chen, Z., Wu, Z., and Feng, Y.

Lawyer llama technical report.

_arXiv preprint arXiv:2305.15062_, 2023.

- Jiang et al. (2023)↑
Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., Casas, D. d. l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al.

Mistral 7b.

_arXiv preprint arXiv:2310.06825_, 2023.

- Johnson et al. (2019)↑
Johnson, J., Douze, M., and Jégou, H.

Billion-scale similarity search with GPUs.

_IEEE Transactions on Big Data_, 7(3):535–547, 2019.

- Kandpal et al. (2023)↑
Kandpal, N., Deng, H., Roberts, A., Wallace, E., and Raffel, C.

Large language models struggle to learn long-tail knowledge.

In _International Conference on Machine Learning_, pp.  15696–15707. PMLR, 2023.

- Kirkpatrick et al. (2017)↑
Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., et al.

Overcoming catastrophic forgetting in neural networks.

_Proceedings of the national academy of sciences_, 114(13):3521–3526, 2017.

- Lampinen et al. (2022)↑
Lampinen, A. K., Dasgupta, I., Chan, S. C., Matthewson, K., Tessler, M. H., Creswell, A., McClelland, J. L., Wang, J. X., and Hill, F.

Can language models learn from explanations in context?

_arXiv preprint arXiv:2204.02329_, 2022.

- Lauscher et al. (2020)↑
Lauscher, A., Majewska, O., Ribeiro, L. F., Gurevych, I., Rozanov, N., and Glavaš, G.

Common sense or world knowledge? investigating adapter-based knowledge injection into pretrained transformers.

_arXiv preprint arXiv:2005.11787_, 2020.

- Lewis et al. (2020)↑
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., et al.

Retrieval-augmented generation for knowledge-intensive nlp tasks.

_Advances in Neural Information Processing Systems_, 33:9459–9474, 2020.

- Liu et al. (2020)↑
Liu, W., Zhou, P., Zhao, Z., Wang, Z., Ju, Q., Deng, H., and Wang, P.

K-bert: Enabling language representation with knowledge graph.

In _Proceedings of the AAAI Conference on Artificial Intelligence_, volume 34, pp.  2901–2908, 2020.

- Luo et al. (2023)↑
Luo, Y., Yang, Z., Meng, F., Li, Y., Zhou, J., and Zhang, Y.

An empirical study of catastrophic forgetting in large language models during continual fine-tuning.

_arXiv preprint arXiv:2308.08747_, 2023.

- Min et al. (2021)↑
Min, S., Lewis, M., Zettlemoyer, L., and Hajishirzi, H.

Metaicl: Learning to learn in context.

_arXiv preprint arXiv:2110.15943_, 2021.

- Mishra et al. (2021)↑
Mishra, S., Khashabi, D., Baral, C., and Hajishirzi, H.

Cross-task generalization via natural language crowdsourcing instructions.

_arXiv preprint arXiv:2104.08773_, 2021.

- Mitra et al. (2023)↑
Mitra, A., Del Corro, L., Mahajan, S., Codas, A., Simoes, C., Agrawal, S., Chen, X., Razdaibiedina, A., Jones, E., Aggarwal, K., et al.

Orca 2: Teaching small language models how to reason.

_arXiv preprint arXiv:2311.11045_, 2023.

- Neelakantan et al. (2022)↑
Neelakantan, A., Xu, T., Puri, R., Radford, A., Han, J. M., Tworek, J., Yuan, Q., Tezak, N. A., Kim, J. W., Hallacy, C., Heidecke, J., Shyam, P., Power, B., Nekoul, T. E., Sastry, G., Krueger, G., Schnurr, D. P., Such, F. P., Hsu, K. S.-K., Thompson, M., Khan, T., Sherbakov, T., Jang, J., Welinder, P., and Weng, L.

Text and code embeddings by contrastive pre-training.

_ArXiv_, abs/2201.10005, 2022.

URL [https://api.semanticscholar.org/CorpusID:246275593](https://api.semanticscholar.org/CorpusID:246275593 "").

- Nguyen (2023)↑
Nguyen, H.-T.

A brief report on lawgpt 1.0: A virtual legal assistant based on gpt-3.

_arXiv preprint arXiv:2302.05729_, 2023.

- Nori et al. (2023)↑
Nori, H., King, N., McKinney, S. M., Carignan, D., and Horvitz, E.

Capabilities of gpt-4 on medical challenge problems.

_ArXiv_, abs/2303.13375, 2023.

URL [https://api.semanticscholar.org/CorpusID:257687695](https://api.semanticscholar.org/CorpusID:257687695 "").

- OpenAI (2023)↑
OpenAI.

Gpt-4 technical report.

_ArXiv_, abs/2303.08774, 2023.

URL [https://api.semanticscholar.org/CorpusID:257532815](https://api.semanticscholar.org/CorpusID:257532815 "").

- Ouyang et al. (2022)↑
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al.

Training language models to follow instructions with human feedback.

_Advances in Neural Information Processing Systems_, 35:27730–27744, 2022.

- Petroni et al. (2019)↑
Petroni, F., Rocktäschel, T., Lewis, P., Bakhtin, A., Wu, Y., Miller, A. H., and Riedel, S.

Language models as knowledge bases?

_arXiv preprint arXiv:1909.01066_, 2019.

- Radford et al. (2019)↑
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.

Language models are unsupervised multitask learners.

_OpenAI blog_, 1(8):9, 2019.

- Rafailov et al. (2023)↑
Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., and Finn, C.

Direct preference optimization: Your language model is secretly a reward model.

_arXiv preprint arXiv:2305.18290_, 2023.

- Sakaguchi et al. (2021)↑
Sakaguchi, K., Bras, R. L., Bhagavatula, C., and Choi, Y.

Winogrande: An adversarial winograd schema challenge at scale.

_Communications of the ACM_, 64(9):99–106, 2021.

- Schulman et al. (2021)↑
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O.

Proximal policy optimization algorithms.

_arXiv preprint arXiv:1707.06347_, 2017.

- Sharma et al. (2022)↑
Sharma, S., Joshi, A., Mukhija, N., Zhao, Y., Bhathena, H., Singh, P., Santhanam, S., and Biswas, P.

Systematic review of effect of data augmentation using paraphrasing on named entity recognition.

In _NeurIPS 2022 Workshop on Synthetic Data for Empowering ML Research_, 2022.

URL [https://openreview.net/forum?id=rc2h1h89aDi](https://openreview.net/forum?id=rc2h1h89aDi "").

- Shorten et al. (2021)↑
Shorten, C., Khoshgoftaar, T. M., and Furht, B.

Text data augmentation for deep learning.

_Journal of Big Data_, 8, 2021.

URL [https://api.semanticscholar.org/CorpusID:236096559](https://api.semanticscholar.org/CorpusID:236096559 "").

- Singhal et al. (2023a)↑
Singhal, K., Azizi, S., Tu, T., Mahdavi, S. S., Wei, J., Chung, H. W., Scales, N., Tanwani, A., Cole-Lewis, H., Pfohl, S., et al.

Large language models encode clinical knowledge.

_Nature_, 620(7972):172–180, 2023a.

- Singhal et al. (2023b)↑
Singhal, K., Tu, T., Gottweis, J., Sayres, R., Wulczyn, E., Hou, L., Clark, K., Pfohl, S., Cole-Lewis, H., Neal, D., et al.

Towards expert-level medical question answering with large language models.

_arXiv preprint arXiv:2305.09617_, 2023b.

- Srivastava et al. (2022)↑
Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A., Garriga-Alonso, A., et al.

Beyond the imitation game: Quantifying and extrapolating the capabilities of language models.

_arXiv preprint arXiv:2206.04615_, 2022.

- Tan et al. (2023)↑
Tan, Y., Min, D., Li, Y., Li, W., Hu, N., Chen, Y., and Qi, G.

Can chatgpt replace traditional kbqa models? an in-depth analysis of the question answering performance of the gpt llm family.

In _International Semantic Web Conference_, pp.  348–367. Springer, 2023.

- Taori et al. (2023)↑
Taori, R., Gulrajani, I., Zhang, T., Dubois, Y., Li, X., Guestrin, C., Liang, P., and Hashimoto, T. B.

Alpaca: A strong, replicable instruction-following model.

_Stanford Center for Research on Foundation Models. https://crfm. stanford. edu/2023/03/13/alpaca. html_, 3(6):7, 2023.

- Tirumala et al. (2022)↑
Tirumala, K., Markosyan, A. H., Zettlemoyer, L., and Aghajanyan, A.

Memorization without overfitting: Analyzing the training dynamics of large language models.

_ArXiv_, abs/2205.10770, 2022.

URL [https://api.semanticscholar.org/CorpusID:248986465](https://api.semanticscholar.org/CorpusID:248986465 "").

- Touvron et al. (2023)↑
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., et al.

Llama 2: Open foundation and fine-tuned chat models.

_arXiv preprint arXiv:2307.09288_, 2023.

- Tunstall et al. (2023)↑
Tunstall, L., Beeching, E., Lambert, N., Rajani, N., Rasul, K., Belkada, Y., Huang, S., von Werra, L., Fourrier, C., Habib, N., et al.

Zephyr: Direct distillation of lm alignment.

_arXiv preprint arXiv:2310.16944_, 2023.

- Wang et al. (2023)↑
Wang, C., Liu, X., Yue, Y., Tang, X., Zhang, T., Jiayang, C., Yao, Y., Gao, W., Hu, X., Qi, Z., et al.

Survey on factuality in large language models: Knowledge, retrieval and domain-specificity.

_arXiv preprint arXiv:2310.07521_, 2023.

- Wang et al. (2020)↑
Wang, R., Tang, D., Duan, N., Wei, Z., Huang, X., Cao, G., Jiang, D., Zhou, M., et al.

K-adapter: Infusing knowledge into pre-trained models with adapters.

_arXiv preprint arXiv:2002.01808_, 2020.

- Wang et al. (2022)↑
Wang, Y., Mishra, S., Alipoormolabashi, P., Kordi, Y., Mirzaei, A., Arunkumar, A., Ashok, A., Dhanasekaran, A. S., Naik, A., Stap, D., et al.

Super-naturalinstructions: Generalization via declarative instructions on 1600+ nlp tasks.

_arXiv preprint arXiv:2204.07705_, 2022.

- Wu et al. (2023a)↑
Wu, C., Zhang, X., Zhang, Y., Wang, Y., and Xie, W.

Pmc-llama: Further finetuning llama on medical papers.

_arXiv preprint arXiv:2304.14454_, 2023a.

- Wu et al. (2023b)↑
Wu, S., Irsoy, O., Lu, S., Dabravolski, V., Dredze, M., Gehrmann, S., Kambadur, P., Rosenberg, D., and Mann, G.

Bloomberggpt: A large language model for finance.

_arXiv preprint arXiv:2303.17564_, 2023b.

- Xiao et al. (2023)↑
Xiao, S., Liu, Z., Zhang, P., and Muennighoff, N.

C-pack: Packaged resources to advance general chinese embedding, 2023.

- Yang et al. (2023)↑
Yang, H., Liu, X.-Y., and Wang, C. D.

Fingpt: Open-source financial large language models.

_arXiv preprint arXiv:2306.06031_, 2023.

- Yu et al. (2022)↑
Yu, W., Zhu, C., Li, Z., Hu, Z., Wang, Q., Ji, H., and Jiang, M.

A survey of knowledge-enhanced text generation.

_ACM Computing Surveys_, 54(11s):1–38, 2022.

- Zhou et al. (2023)↑
Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X., Efrat, A., Yu, P., Yu, L., et al.

Lima: Less is more for alignment.

_arXiv preprint arXiv:2305.11206_, 2023.


## Appendix A RAG Ablation Study

As mentioned in [Section5](https://arxiv.org/html/2312.05934v3#S5 "5 Experiments and Results ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"), we compared various values of K∈{0,…,5}𝐾0…5K\\in\\{0,\\ldots,5\\}italic\_K ∈ { 0 , … , 5 }, shown in [Table3](https://arxiv.org/html/2312.05934v3#A1.T3 "Table 3 ‣ Appendix A RAG Ablation Study ‣ Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs").We were unable to find an optimal value of K𝐾Kitalic\_K per model, per 0/5050/50 / 5-shot, or per task. In fact, other than Anatomy that worked well with K=2𝐾2K=2italic\_K = 2 consistently, there seems to be no patterns that aid in predicting the performance per K𝐾Kitalic\_K, unlike the results presented in (Lewis et al., [2020](https://arxiv.org/html/2312.05934v3#bib.bib21 "")) for other setups. Moreover, the gap between the best and worst performing K𝐾Kitalic\_Ks can be large.

Unfortunately, we must conclude that this additional hyperparameter is unstable. This is a downside of using RAG in practice, and the choice of K𝐾Kitalic\_K cannot be ignored.

| Task | Model | \# Retrieved documents (k𝑘kitalic\_k) |
| --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- |
| Anatomy (0-shot) | Mistral 7B | 0.615 | 0.681 | 0.630 | 0.644 | 0.622 |
| Llama2 7B | 0.444 | 0.489 | 0.467 | 0.474 | 0.481 |
| Orca2 7B | 0.607 | 0.637 | 0.600 | 0.585 | 0.637 |
| Anatomy (5-shot) | Mistral 7B | 0.659 | 0.667 | 0.659 | 0.681 | 0.674 |
| Llama2 7B | 0.496 | 0.563 | 0.541 | 0.526 | 0.526 |
| Orca2 7B | 0.630 | 0.659 | 0.600 | 0.600 | 0.600 |
| Astronomy (0-shot) | Mistral 7B | 0.651 | 0.678 | 0.678 | 0.664 | 0.664 |
| Llama2 7B | 0.447 | 0.434 | 0.447 | 0.434 | 0.467 |
| Orca2 7B | 0.711 | 0.730 | 0.730 | 0.750 | 0.730 |
| Astronomy (5-shot) | Mistral 7B | 0.704 | 0.684 | 0.658 | 0.684 | 0.724 |
| Llama2 7B | 0.461 | 0.447 | 0.474 | 0.428 | 0.454 |
| Orca2 7B | 0.730 | 0.737 | 0.750 | 0.743 | 0.763 |
| Biology (0-shot) | Mistral 7B | 0.736 | 0.722 | 0.757 | 0.743 | 0.736 |
| Llama2 7B | 0.438 | 0.472 | 0.493 | 0.479 | 0.472 |
| Orca2 7B | 0.639 | 0.618 | 0.639 | 0.625 | 0.639 |
| Biology (5-shot) | Mistral 7B | 0.722 | 0.778 | 0.778 | 0.771 | 0.743 |
| Llama2 7B | 0.500 | 0.521 | 0.507 | 0.465 | 0.472 |
| Orca2 7B | 0.625 | 0.639 | 0.625 | 0.660 | 0.660 |
| Chemistry (0-shot) | Mistral 7B | 0.450 | 0.470 | 0.470 | 0.500 | 0.470 |
| Llama2 7B | 0.320 | 0.320 | 0.300 | 0.380 | 0.360 |
| Orca2 7B | 0.370 | 0.420 | 0.400 | 0.410 | 0.440 |
| Chemistry (5-shot) | Mistral 7B | 0.540 | 0.490 | 0.500 | 0.510 | 0.470 |
| Llama2 7B | 0.280 | 0.320 | 0.340 | 0.340 | 0.380 |
| Orca2 7B | 0.390 | 0.430 | 0.400 | 0.430 | 0.470 |
| Prehistory (0-shot) | Mistral 7B | 0.728 | 0.725 | 0.750 | 0.735 | 0.728 |
| Llama2 7B | 0.481 | 0.460 | 0.457 | 0.457 | 0.429 |
| Orca2 7B | 0.648 | 0.645 | 0.660 | 0.670 | 0.679 |
| Prehistory (5-shot) | Mistral 7B | 0.710 | 0.750 | 0.759 | 0.756 | 0.762 |
| Llama2 7B | 0.512 | 0.485 | 0.525 | 0.519 | 0.531 |
| Orca2 7B | 0.660 | 0.688 | 0.685 | 0.698 | 0.688 |

Table 3: RAG ablation study.

## Appendix B Paraphrase Examples

Below is the prompt we used to generate paraphrases with GPT-4:

> Your task is to paraphrase a text paragraph. The paragraph is given below.
>
> Make sure to keep the same meaning but change the wording. Do not change any factual information.
>
> Try to keep roughly the same length of the original text.
>
> Give NUM \_ PARAPHRASES different paraphrases for each text.
>
> These paraphrases should be as different from each other as possible.
>
> Return a JSON formatted string with one key, called ’paraphrases’, and a list of paraphrases.
>
> Input paragraph:
>

Below are some examples. First, an example taken from the following Wikipedia page: ”51st International Emmy Awards”.

> Paraphrase I
>
> The fifty-first edition of the International Emmy Awards Competition accepted submissions across all categories from December 7, 2022, until the closing date of February 16, 2023.
>
> Paraphrase II
>
> The International Emmy Awards Competition, now in its 51st year, accepted submissions across all categories starting from December 7, 2022, until the deadline on February 16, 2023.
>
> Paraphrase III
>
> The fifty-first edition of the International Emmy Awards Competition accepted submissions across all categories from December 7, 2022, until the closing date of February 16, 2023.
>

The next example was taken from the following Wikipedia page: ”2023 Indianapolis mayoral election”.

> Paraphrase I
> The mayoral election in Indianapolis took place on November 7, 2023, with preliminary elections occurring on May 2. The sitting mayor, Democrat Joe Hogsett, successfully ran for a third term. Both Hogsett and his Republican opponent, Jefferson Shreve, moved on to the main election.
>
> Paraphrase II
> On November 7, 2023, citizens of Indianapolis cast their votes to elect their Mayor, following primary elections on May 2. Joe Hogsett, the Democrat already in office, won his bid for a third term. Hogsett and the Republican candidate, Jefferson Shreve, were the two contenders in the final electoral round.
>
> Paraphrase III
>
> The mayoral election in Indianapolis took place on the 7th of November, 2023, following primary elections that occurred on the 2nd of May. Joe Hogsett, the incumbent Democrat, successfully ran for a third term. Both Hogsett and his Republican challenger, Jefferson Shreve, made it through to the final round of the election.
>

## Appendix C Current Events Existing Knowledge Examples

To give a better understanding of how a model might be able to answer questions about new information, with better than random success, we present three possible scenarios as examples. These scenarios show how models with stronger reasoning skills can infer the correct answer even for unseen information.

The first scenario involves questions about previously unseen information, where basic reasoning abilities allow a model to make an educated guess.

> Question: What was a key issue that led to the 2023 United Auto Workers strike?
>
> Answers:
>
>
> 1. 1.
>
>
>    Dissatisfaction with the quality of cafeteria food.
>
>
> 2. 2.
>
>
>    Disagreements over employee dress codes.
>
>
> 3. 3.
>
>
>    Discontent with stagnant wages and tiered employment systems.
>
>
> 4. 4.
>
>
>    Debates over the color scheme of the factories.
>
>

In this case it is easy to guess that the third option is the most likely, even without knowledge of this specific strike.

A second scenario involves questions where prior knowledge about a topic may aid a model in answering.

> Question: What environmental concern was raised by some scientists as a result of the 2023 Hawaii wildfires?
>
> Answers:
>
>
> 1. 1.
>
>
>    Rising temperatures.
>
>
> 2. 2.
>
>
>    Melting ice caps.
>
>
> 3. 3.
>
>
>    Charred soils running off into the shoreline.
>
>
> 4. 4.
>
>
>    Increased air pollution.
>
>

In this case, knowing the geography of Hawaii, as well as immediate effects of wildfires, enables a model to give the first two options a lower likelihood. This process of elimination increases the probability of choosing one of the remaining options (the third option is the correct answer).

A third scenario arises due to the automatic question generation process, some questions strongly rely on pre-existing knowledge.

> Question: What event in 2021 was compared to the September 2023 New York floods?
>
> Answers:
>
>
> 1. 1.
>
>
>    Hurricane Katrina.
>
>
> 2. 2.
>
>
>    Hurricane Ida.
>
>
> 3. 3.
>
>
>    Hurricane Sandy.
>
>
> 4. 4.
>
>
>    Hurricane Harvey.
>
>

Since only one of these events occurred in 2021 (Hurricane Ida), and all the models tested have been exposed to events from 2021 during pre-training, this question can potentially be answered without using additional current information.

Finally, to demonstrate why it is reasonable to assume that models cannot generally answer questions about new information, with better than random success, look at the following example:

> Question: How did Matthew Belk, a National Weather Service meteorologist, describe the September 2023 northeastern U.S. floods?
>
> Answers:
>
>
> 1. 1.
>
>
>    50-year event.
>
>
> 2. 2.
>
>
>    100-year event.
>
>
> 3. 3.
>
>
>    200-year event.
>
>
> 4. 4.
>
>
>    500-year event.
>
>

Even with some knowledge about floods and their statistical properties, it would be very difficult to guess that this specific meteorologist would call the flood a ‘200-year event’. This is especially true if the model was not exposed to information about the details of the flood.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-rag-works-by-neo-kim-and-eric-roby.md">
<details>
<summary>RAG - A Deep Dive</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://newsletter.systemdesign.one/p/how-rag-works>

# RAG - A Deep Dive

### #132: Understanding Retrieval-Augmented Generation

Every large language model [1](https://newsletter.systemdesign.one/p/how-rag-works#footnote-1) ( **LLM**) you use has lied to you with confidence, fluency, and frequency…

Ask any model about something that happened last week. It doesn’t know. It can’t know. Its knowledge was frozen months ago. They might try, and if they do, they will hallucinate.

This isn’t a bug.

It’s a fundamental architectural limitation. LLMs keep knowledge in their parameters [2](https://newsletter.systemdesign.one/p/how-rag-works#footnote-2). These are billions of numerical weights learned during training. Once training ends, the knowledge is locked. The model doesn’t know what it doesn’t know, so it fills the gaps with confident fabrication. Studies show that hallucination [3](https://newsletter.systemdesign.one/p/how-rag-works#footnote-3) rates can be as low as 1% for simple summarization tasks. However, they can exceed 58% for complex work.

This is exactly what Retrieval-Augmented Generation [4](https://newsletter.systemdesign.one/p/how-rag-works#footnote-4) ( **RAG**) solves.

RAG doesn’t bake knowledge into the model. Instead, it pulls in relevant context when you ask a question. The model stays smart, your data stays current, and every answer is traceable back to its source.

This is the architectural pattern that makes AI actually useful.

Here’s how it works, why it works, and how to build it:

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

Context windows [5](https://newsletter.systemdesign.one/p/how-rag-works#footnote-5) have increased a lot. Some models can now handle over a million tokens [6](https://newsletter.systemdesign.one/p/how-rag-works#footnote-6). But this approach has three fatal problems.

**First, it’s expensive**.

You pay for each token. Sending your entire knowledge base with every query will wipe out your budget.

**Second, there are hard limits.**

A million-token window can’t fit all of a large enterprise’s documents or its databases.

**Third, and this is the one most people miss, models get** _**worse**_ **with more context.**

Research from Stanford and UC Berkeley shows LLM performance follows a U-shaped curve. Models do best when key information is at the start or end, but accuracy drops sharply when important facts are buried in the middle. In Liu et al.’s multi-document QA experiments, accuracy for some models dropped to roughly 25% when key information was placed in the middle of a 20-document context.

It’s clear: adding more context to the prompt doesn’t guarantee the model will use it.

## **Fine-tuning isn’t the answer either**

Fine-tuning [7](https://newsletter.systemdesign.one/p/how-rag-works#footnote-7) is when you take a pre-trained model and continue training it on your own specific data, so it learns new knowledge or behavior.

Fine-tuning changes the model’s weights to incorporate new knowledge. Think of it like sending someone back to school for a specialized course. In theory, this lets you teach the model about your domain.

In practice, it creates more problems than it solves…

It requires GPU compute, machine learning expertise, and carefully prepared training data. It takes days or weeks to complete. The result is a snapshot. Once your underlying data changes, your fine-tuned model becomes stale.

### **What’s Actually Needed**

The key is to provide the AI with the right information at the right time for each query. And it should be done without changing the model itself.

That’s RAG.

Now let’s investigate RAG deeper:

## **What RAG actually is**

Retrieval-Augmented Generation is an architectural pattern, not a product. The concept is straightforward, and the best analogy is an open-book exam.

https://substackcdn.com/image/fetch/$s_!WV5q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50ac6e9d-d48d-403a-aafa-40092392d779_1280x720.png

A student taking a closed-book exam relies on what they have memorized.

That’s a standard LLM. It’s smart and can reason, but it’s limited to what’s in its parameters. A student with an open-book exam has the same reasoning skills. They can check relevant pages before answering.

That’s RAG.

The formal definition comes from a 2020 paper by Patrick Lewis and his team at Facebook AI Research and University College London. RAG models combine parametric memory [8](https://newsletter.systemdesign.one/p/how-rag-works#footnote-8) with a pre-trained language model and non-parametric memory [9](https://newsletter.systemdesign.one/p/how-rag-works#footnote-9). This non-parametric memory uses an external knowledge index. It’s accessed by a neural retriever [10](https://newsletter.systemdesign.one/p/how-rag-works#footnote-10).

You can still update the model’s knowledge by swapping the retrieval index. No one needs to retrain.

In practice, RAG follows a three-step loop:

1. Query comes in: a user asks a question.

2. Retrieve: System looks in an external knowledge base for the best information chunks.

3. Question and context go to the LLM. It then creates an answer based on the retrieved documents.

You’re not changing the model. You’re changing what it sees. That distinction makes RAG so powerful and so practical.

The open-book analogy makes sense at a high level. But understanding why it works so well means diving deeper into the topic…

## **How RAG Works Under the Hood**

The three-step loop sounds simple. The engineering that makes it work is where things get interesting.

A RAG system has two main parts:

- An **offline ingestion pipeline** that gets your data ready.

- An **online retrieval pipeline** that answers queries.

Let’s walk through each one…

https://substackcdn.com/image/fetch/$s_!y9LI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F821e9ca3-44bb-4aae-87c9-26d932f2f67a_1280x720.png

### **Embeddings: Core Mechanism**

Before anything else, you need to understand embeddings [11](https://newsletter.systemdesign.one/p/how-rag-works#footnote-11). This is the concept that enables semantic search [12](https://newsletter.systemdesign.one/p/how-rag-works#footnote-12).

Text embeddings turn text into dense numerical vectors [13](https://newsletter.systemdesign.one/p/how-rag-works#footnote-13). These are arrays of floating-point numbers, usually with 1,536 or 3,072 dimensions. They capture the text meaning. The magic is in what “capture meaning” means. Words and sentences with similar intent are close together in vector space. This happens even with different words.

Consider this: _“How do I reset my password?”_ and _“I can’t log into my account”_ use completely different words.

But when converted to embeddings, they produce nearly identical vectors. The distance between them is tiny because their meanings are similar. This is measured using cosine similarity [14](https://newsletter.systemdesign.one/p/how-rag-works#footnote-14), dot product, or Euclidean distance.

The key insight for RAG is clear.

System finds relevant content. It does this even if the user’s question doesn’t use the exact words from the source document. It searches by meaning, not by keywords.

### **Data Ingestion Pipeline (Offline Phase)**

First, process your knowledge base. Then, index it. Only then can your RAG system answer questions.

This happens in five steps:

**What triggers the offline phase?**

In traditional workflows, this pipeline runs when new data is available. This can happen when documents are added or updated. It can also occur when a database changes or on a regular schedule, like nightly or weekly. Some teams trigger re-ingestion if retrieval quality drops.

They also do this when a new data source connects:

1. **Load documents from anywhere**: PDFs, databases, APIs, wikis, Slack channels, and Confluence pages. Frameworks like LangChain [15](https://newsletter.systemdesign.one/p/how-rag-works#footnote-15) and LlamaIndex [16](https://newsletter.systemdesign.one/p/how-rag-works#footnote-16) offer ready-made connectors for many common sources.

2. **Chunking** [17](https://newsletter.systemdesign.one/p/how-rag-works#footnote-17) **:** Split documents into semantically meaningful pieces. This is the single highest-leverage step to get right, and we will cover it in depth later.

3. **Embedding:** Convert each chunk into a vector using an embedding model.

4. **Storage:** Store the vectors in a vector database [18](https://newsletter.systemdesign.one/p/how-rag-works#footnote-18) optimized for similarity search.

5. **Metadata tagging:** Tag each chunk with source, timestamp, category, and access control information. This metadata becomes critical for filtering, attribution, and security later.

### **Retrieval Pipeline (Online Phase)**

When a user asks a question, the retrieval pipeline kicks in:

1. **Query embedding**: User’s question turns into a vector. This uses the same embedding model from ingestion. This is critical: the query and the documents must live in the same vector space.

2. **Similarity search**: The system finds the top-K [19](https://newsletter.systemdesign.one/p/how-rag-works#footnote-19) similar chunks. It compares the query vector to each vector in the database.

3. **Retrieval strategy**: This is where the real engineering decisions happen. Three primary approaches exist:

1. Sparse retrieval [20](https://newsletter.systemdesign.one/p/how-rag-works#footnote-20) uses a statistical method that matches exact keywords. It weighs these matches using term frequency and inverse document frequency.

2. Dense retrieval (embeddings):Semantic search via vectors. Finds conceptually relevant content even when the wording differs.

3. Hybrid search (combining both): Use both sparse and dense retrieval. Then, merge the results with Reciprocal Rank Fusion [21](https://newsletter.systemdesign.one/p/how-rag-works#footnote-21) (RRF). This boosts documents that rank high in both systems.
4. **Re-ranking**: After retrieving results, a cross-encoder model rescans them. It processes the query and each document as one input. This captures fine-grained relevance that bi-encoders miss.

### **Generation Phase**

With the most relevant chunks in hand, the system assembles the final prompt:

1. **Prompt Construction:**

1. **System Prompt:** Combine the system prompt (the instructions that tell the LLM how to behave, like _“You are a helpful customer support agent”_) with the user’s request.

2. **Retrieved Context Chunks:** Integrate the relevant pieces of text pulled from your knowledge base. For instance, if someone asks, _“What’s your refund policy?”_ You might pull two paragraphs from your company’s policy document.

3. **User’s Original Query:** Include the user’s actual question or task — exactly as they typed it.
2. **LLM Call:** The model generates an answer grounded in the retrieved documents. The key facts are in the prompt. The model uses these facts to reason instead of relying on its trained memory. Think of it like giving someone an open-book exam instead of asking them to answer from memory.

3. **Citation and Attribution:** The system shows which source documents were used and provides verifiable citations. For example, the response might say, _“Based on Section 3.2 of the Employee Handbook...”_ so the user knows exactly where the answer came from. This is one of RAG’s biggest advantages over fine-tuning: transparency.

Now that you know how RAG works mechanically, the real question is whether it’s the right tool. That depends on what you’re comparing it to…

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

## **Traditional RAG vs. Agentic RAG**

Traditional RAG follows the straightforward three-step loop described above: retrieve, then generate. It works well for simple question-answering but has limitations. What happens when the first retrieval doesn’t return good results? Traditional RAG just pushes forward with whatever it finds.

Agentic RAG adds a reasoning layer on top.

An AI agent decides how to handle each query. It can change the search, link several retrievals, pick a knowledge base, or skip retrieval completely. Think of Traditional RAG as a student who looks up one page and writes their answer. Agentic RAG is like a student. They check several sources. They re-read sections that seem off and cross-reference information before writing.

https://substackcdn.com/image/fetch/$s_!WJ3i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb15a5d41-dd18-4a64-bd28-79621c669aec_1404x570.png

## **Multi-Step RAG Pipeline**

Production RAG systems often go beyond the simple retrieve-and-generate loop. A multi-step pipeline adds intelligence before and after retrieval:

1. Query Intent Parsing: Before searching, the system analyzes what the user actually wants. Is it a factual question? A comparison? A request for a summary? Understanding intent helps the system choose the right retrieval strategy and knowledge base.

2. Query Reformulation: The system may rewrite the user’s question to improve retrieval quality. For example, _“Why is my app slow?”_ might become _“application performance bottleneck causes and solutions.”_

3. Retrieval: System searches for relevant chunks (as described above).

4. Live Web Search: If internal documents aren’t enough, some RAG systems can do live web searches. This helps them get current information from the internet.

5. Reranking [22](https://newsletter.systemdesign.one/p/how-rag-works#footnote-22) and Filtering: Results are scored, filtered, and reranked for relevance.

6. Generation: LLM produces an answer grounded in all the gathered context.

This multi-step approach is what separates demo-quality RAG from production-quality RAG.

## **RAG Limitations**

RAG is powerful, but it’s not a silver bullet…

Understanding its limitations helps you decide when to use it and when to look elsewhere:

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

The full set of [RAG and GenAI resources](https://github.com/redis-developer/redis-ai-resources) in the Redis developer repository covers each technique with working code examples.

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

<research_source type="scraped_from_research" phase="exploitation" file="retrieval-augmented-generation-rag-for-llms-prompt-engineeri.md">
<details>
<summary>Retrieval Augmented Generation (RAG) for LLMs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.promptingguide.ai/research/rag>

# Retrieval Augmented Generation (RAG) for LLMs

There are many challenges when working with LLMs such as domain knowledge gaps, factuality issues, and hallucination. Retrieval Augmented Generation (RAG) provides a solution to mitigate some of these issues by augmenting LLMs with external knowledge such as databases. RAG is particularly useful in knowledge-intensive scenarios or domain-specific applications that require knowledge that's continually updating. A key advantage of RAG over other approaches is that the LLM doesn't need to be retrained for task-specific applications. RAG has been popularized recently with its application in conversational agents.

In this summary, we highlight the main findings and practical insights from the recent survey titled [Retrieval-Augmented Generation for Large Language Models: A Survey (opens in a new tab)](https://arxiv.org/abs/2312.10997) (Gao et al., 2023). In particular, we focus on the existing approaches, state-of-the-art RAG, evaluation, applications and technologies surrounding the different components that make up a RAG system (retrieval, generation, and augmentation techniques).

## Introduction to RAG

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-framework.81dc2cdc.png&w=3840&q=75

As better introduced [here (opens in a new tab)](https://www.promptingguide.ai/techniques/rag), RAG can be defined as:

> RAG takes input and retrieves a set of relevant/supporting documents given a source (e.g., Wikipedia). The documents are concatenated as context with the original input prompt and fed to the text generator which produces the final output. This makes RAG adaptive for situations where facts could evolve over time. This is very useful as LLMs's parametric knowledge is static. RAG allows language models to bypass retraining, enabling access to the latest information for generating reliable outputs via retrieval-based generation.

In short, the retrieved evidence obtained in RAG can serve as a way to enhance the accuracy, controllability, and relevancy of the LLM's response. This is why RAG can help reduce issues of hallucination or performance when addressing problems in a highly evolving environment.

While RAG has also involved the optimization of pre-training methods, current approaches have largely shifted to combining the strengths of RAG and powerful fine-tuned models like [ChatGPT (opens in a new tab)](https://www.promptingguide.ai/models/chatgpt) and [Mixtral (opens in a new tab)](https://www.promptingguide.ai/models/mixtral). The chart below shows the evolution of RAG-related research:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-evolution.929ab78b.png&w=1920&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

Below is a typical RAG application workflow:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-process.c8703891.png&w=1920&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

We can explain the different steps/components as follows:

-   **Input:** The question to which the LLM system responds is referred to as the input. If no RAG is used, the LLM is directly used to respond to the question.
-   **Indexing:** If RAG is used, then a series of related documents are indexed by chunking them first, generating embeddings of the chunks, and indexing them into a vector store. At inference, the query is also embedded in a similar way.
-   **Retrieval:** The relevant documents are obtained by comparing the query against the indexed vectors, also denoted as "Relevant Documents".
-   **Generation:** The relevant documents are combined with the original prompt as additional context. The combined text and prompt are then passed to the model for response generation which is then prepared as the final output of the system to the user.

In the example provided, using the model directly fails to respond to the question due to a lack of knowledge of current events. On the other hand, when using RAG, the system can pull the relevant information needed for the model to answer the question appropriately.

## RAG Paradigms

Over the past few years, RAG systems have evolved from Naive RAG to Advanced RAG and Modular RAG. This evolution has occurred to address certain limitations around performance, cost, and efficiency.

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-paradigms.21be1d6f.png&w=3840&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

### Naive RAG

Naive RAG follows the traditional aforementioned process of indexing, retrieval, and generation. In short, a user input is used to query relevant documents which are then combined with a prompt and passed to the model to generate a final response. Conversational history can be integrated into the prompt if the application involves multi-turn dialogue interactions.

Naive RAG has limitations such as low precision (misaligned retrieved chunks) and low recall (failure to retrieve all relevant chunks). It's also possible that the LLM is passed outdated information which is one of the main issues that a RAG system should initially aim to solve. This leads to hallucination issues and poor and inaccurate responses.

When augmentation is applied, there could also be issues with redundancy and repetition. When using multiple retrieved passages, ranking and reconciling style/tone are also key. Another challenge is ensuring that the generation task doesn't overly depend on the augmented information which can lead to the model just reiterating the retrieved content.

### Advanced RAG

Advanced RAG helps deal with issues present in Naive RAG such as improving retrieval quality that could involve optimizing the pre-retrieval, retrieval, and post-retrieval processes.

The pre-retrieval process involves optimizing data indexing which aims to enhance the quality of the data being indexed through five stages: enhancing data granularity, optimizing index structures, adding metadata, alignment optimization, and mixed retrieval.

The retrieval stage can be further improved by optimizing the embedding model itself which directly impacts the quality of the chunks that make up the context. This can be done by fine-tuning the embedding to optimize retrieval relevance or employing dynamic embeddings that better capture contextual understanding (e.g., OpenAI’s embeddings-ada-02 model).

Optimizing post-retrieval focuses on avoiding context window limits and dealing with noisy or potentially distracting information. A common approach to address these issues is re-ranking which could involve approaches such as relocation of relevant context to the edges of the prompt or recalculating the semantic similarity between the query and relevant text chunks. Prompt compression may also help in dealing with these issues.

### Modular RAG

As the name implies, Modular RAG enhances functional modules such as incorporating a search module for similarity retrieval and applying fine-tuning in the retriever. Both Naive RAG and Advanced RAG are special cases of Modular RAG and are made up of fixed modules. Extended RAG modules include search, memory, fusion, routing, predict, and task adapter which solve different problems. These modules can be rearranged to suit specific problem contexts. Therefore, Modular RAG benefits from greater diversity and flexibility in that you can add or replace modules or adjust the flow between modules based on task requirements.

Given the increased flexibility in building RAG systems, other important optimization techniques have been proposed to optimize RAG pipelines including:

-   **Hybrid Search Exploration:** This approach leverages a combination of search techniques like keyword-based search and semantic search to retrieve relevant and context-rich information; this is useful when dealing with different query types and information needs.
-   **Recursive Retrieval and Query Engine:** Involves a recursive retrieval process that might start with small semantic chunks and subsequently retrieve larger chunks that enrich the context; this is useful to balance efficiency and context-rich information.
-   **StepBack-prompt:** [A prompting technique (opens in a new tab)](https://arxiv.org/abs/2310.06117) that enables LLMs to perform abstraction that produces concepts and principles that guide reasoning; this leads to better-grounded responses when adopted to a RAG framework because the LLM moves away from specific instances and is allowed to reason more broadly if needed.
-   **Sub-Queries:** There are different query strategies such as tree queries or sequential querying of chunks that can be used for different scenarios. LlamaIndex offers a [sub question query engine (opens in a new tab)](https://docs.llamaindex.ai/en/latest/understanding/putting_it_all_together/agents.html#) that allows a query to be broken down into several questions that use different relevant data sources.
-   **Hypothetical Document Embeddings:** [HyDE (opens in a new tab)](https://arxiv.org/abs/2212.10496) generates a hypothetical answer to a query, embeds it, and uses it to retrieve documents similar to the hypothetical answer as opposed to using the query directly.

## RAG Framework

In this section, we summarize the key developments of the components of a RAG system, which include Retrieval, Generation, and Augmentation.

### Retrieval

Retrieval is the component of RAG that deals with retrieving highly relevant context from a retriever. A retriever can be enhanced in many ways, including:

**Enhancing Semantic Representations**

This process involves directly improving the semantic representations that power the retriever. Here are a few considerations:

-   **Chunking:** One important step is choosing the right chunking strategy which depends on the content you are dealing with and the application you are generating responses for. Different models also display different strengths on varying block sizes. Sentence transformers will perform better on single sentences but text-embedding-ada-002 will perform better with blocks containing 256 or 512 tokens. Other aspects to consider include the length of user questions, application, and token limits but it's common to experiment with different chunking strategies to help optimize retrieval in your RAG system.
-   **Fine-tuned Embedding Models:** Once you have determined an effective chunking strategy, it may be required to fine-tune the embedding model if you are working with a specialized domain. Otherwise, it's possible that the user queries will be completely misunderstood in your application. You can fine-tune on broad domain knowledge (i.e., domain knowledge fine-tuning) and for specific downstream tasks. [BGE-large-EN developed BAAI (opens in a new tab)](https://github.com/FlagOpen/FlagEmbedding) is a notable embedding model that can be fine-tuned to optimize retrieval relevance.

**Aligning Queries and Documents**

This process deals with aligning user's queries to those of documents in the semantic space. This may be needed when a user's query may lack semantic information or contain imprecise phrasing. Here are some approaches:

-   **Query Rewriting:** Focuses on rewriting queries using a variety of techniques such as [Query2Doc (opens in a new tab)](https://arxiv.org/abs/2303.07678), [ITER-RETGEN (opens in a new tab)](https://arxiv.org/abs/2305.15294), and HyDE.
-   **Embedding Transformation:** Optimizes the representation of query embeddings and align them to a latent space that is more closely aligned with a task.

**Aligning Retriever and LLM**

This process deals with aligning the retriever outputs with the preferences of the LLMs.

-   **Fine-tuning Retrievers:** Uses an LLM's feedback signals to refine the retrieval models. Examples include augmentation adapted retriever ( [AAR (opens in a new tab)](https://arxiv.org/abs/2305.17331)), [REPLUG (opens in a new tab)](https://arxiv.org/abs/2301.12652), and [UPRISE (opens in a new tab)](https://arxiv.org/abs/2303.08518), to name a few.
-   **Adapters:** Incorporates external adapters to help with the alignment process. Examples include [PRCA (opens in a new tab)](https://aclanthology.org/2023.emnlp-main.326/), [RECOMP (opens in a new tab)](https://arxiv.org/abs/2310.04408), and [PKG (opens in a new tab)](https://arxiv.org/abs/2305.04757).

### Generation

The generator in a RAG system is responsible for converting retrieved information into a coherent text that will form the final output of the model. This process involves diverse input data which sometimes require efforts to refine the adaptation of the language model to the input data derived from queries and documents. This can be addressed using post-retrieval process and fine-tuning:

-   **Post-retrieval with Frozen LLM:** Post-retrieval processing leaves the LLM untouched and instead focuses on enhancing the quality of retrieval results through operations like information compression and result reranking. Information compression helps with reducing noise, addressing an LLM's context length restrictions, and enhancing generation effects. Reranking aims at reordering documents to prioritize the most relevant items at the top.
-   **Fine-tuning LLM for RAG:** To improve the RAG system, the generator can be further optimized or fine-tuned to ensure that the generated text is natural and effectively leverages the retrieved documents.

### Augmentation

Augmentation involves the process of effectively integrating context from retrieved passages with the current generation task. Before discussing more on the augmentation process, augmentation stages, and augmentation data, here is a taxonomy of RAG's core components:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-taxonomy.e3b19705.png&w=3840&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

Retrieval augmentation can be applied in many different stages such as pre-training, fine-tuning, and inference.

-   **Augmentation Stages:** [RETRO (opens in a new tab)](https://arxiv.org/abs/2112.04426) is an example of a system that leverages retrieval augmentation for large-scale pre-training from scratch; it uses an additional encoder built on top of external knowledge. Fine-tuning can also be combined with RAG to help develop and improve the effectiveness of RAG systems. At the inference stage, many techniques are applied to effectively incorporate retrieved content to meet specific task demands and further refine the RAG process.

-   **Augmentation Source:** A RAG model's effectiveness is heavily impacted by the choice of augmentation data source. Data can be categorized into unstructured, structured, and LLM-generated data.

-   **Augmentation Process:** For many problems (e.g., multi-step reasoning), a single retrieval isn't enough so a few methods have been proposed:
    -   **Iterative retrieval** enables the model to perform multiple retrieval cycles to enhance the depth and relevance of information. Notable approaches that leverage this method include [RETRO (opens in a new tab)](https://arxiv.org/abs/2112.04426) and [GAR-meets-RAG (opens in a new tab)](https://arxiv.org/abs/2310.20158).
    -   **Recursive retrieval** recursively iterates on the output of one retrieval step as the input to another retrieval step; this enables delving deeper into relevant information for complex and multi-step queries (e.g., academic research and legal case analysis). Notable approaches that leverage this method include [IRCoT (opens in a new tab)](https://arxiv.org/abs/2212.10509) and [Tree of Clarifications (opens in a new tab)](https://arxiv.org/abs/2310.14696).
    -   **Adaptive retrieval** tailors the retrieval process to specific demands by determining optimal moments and content for retrieval. Notable approaches that leverage this method include [FLARE (opens in a new tab)](https://arxiv.org/abs/2305.06983) and [Self-RAG (opens in a new tab)](https://arxiv.org/abs/2310.11511).

The figure below depicts a detailed representation of RAG research with different augmentation aspects, including the augmentation stages, source, and process.

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-augmentation.0855501d.png&w=3840&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

### RAG vs. Fine-tuning

There are a lot of open discussions about the difference between RAG and fine-tuning and in which scenarios each is appropriate. Research in these two areas suggests that RAG is useful for integrating new knowledge while fine-tuning can be used to improve model performance and efficiency through improving internal knowledge, output format, and teaching complex instruction following. These approaches are not mutually exclusive and can compliment each other in an iterative process that aims to improve the use of LLMs for a complex knowledge-intensive and scalable application that requires access to quickly-evolving knowledge and customized responses that follow a certain format, tone, and style. In addition, Prompting Engineering can also help to optimize results by leveraging the inherent capabilities of the model. Below is a figure showing the different characteristics of RAG compared with other model optimization methods:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-optimization.bb88c6ae.png&w=3840&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

Here is table from the survey paper that compares the features between RAG and fine-tuned models:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-vs-finetuning.545747e9.png&w=1920&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

## RAG Evaluation

Similar to measuring the performance of LLMs on different aspects, evaluation plays a key role in understanding and optimizing the performance of RAG models across diverse application scenarios. Traditionally, RAG systems have been assessed based on the performance of the downstream tasks using task-specific metrics like F1 and EM. [RaLLe (opens in a new tab)](https://arxiv.org/abs/2308.10633v2) is a notable example of a framework used to evaluate retrieval-augmented large language models for knowledge-intensive tasks.

RAG evaluation targets are determined for both retrieval and generation where the goal is to evaluate both the quality of the context retrieved and the quality of the content generated. To evaluate retrieval quality, metrics used in other knowledge-intensive domains like recommendation systems and information retrieval are used such as NDCG and Hit Rate. To evaluate generation quality, you can evaluate different aspects like relevance and harmfulness if it's unlabeled content or accuracy for labeled content. Overall, RAG evaluation can involve either manual or automatic evaluation methods.

Evaluating a RAG framework focuses on three primary quality scores and four abilities. Quality scores include measuring context relevance (i.e., the precision and specificity of retrieved context), answer faithfulness (i.e., the faithfulness of answers to the retrieved context), and answer relevance (i.e., the relevance of answers to posed questions). In addition, there are four abilities that help measure the adaptability and efficiency of a RAG system: noise robustness, negative rejection, information integration, and counterfactual robustness. Below is a summary of metrics used for evaluating different aspects of a RAG system:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-metrics.1ddc2a61.png&w=1920&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

Several benchmarks like [RGB (opens in a new tab)](https://arxiv.org/abs/2309.01431) and [RECALL (opens in a new tab)](https://arxiv.org/abs/2311.08147) are used to evaluate RAG models. Many tools like [RAGAS (opens in a new tab)](https://arxiv.org/abs/2309.15217), [ARES (opens in a new tab)](https://arxiv.org/abs/2311.09476), and [TruLens (opens in a new tab)](https://www.trulens.org/trulens_eval/core_concepts_rag_triad/) have been developed to automate the process of evaluating RAG systems. Some of the systems rely on LLMs to determine some of the quality scores defined above.

## Challenges & Future of RAG

In this overview, we discussed several research aspects of RAG research and different approaches for enhancing retrieval, augmentation, and generation of a RAG system. Here are several challenges emphasized by [Gao et al., 2023 (opens in a new tab)](https://arxiv.org/abs/2312.10997) as we continue developing and improving RAG systems:

-   **Context length:** LLMs continue to extend context window size which presents challenges to how RAG needs to be adapted to ensure highly relevant and important context is captured.
-   **Robustness:** Dealing with counterfactual and adversarial information is important to measure and improve in RAG.
-   **Hybrid approaches:** There is an ongoing research effort to better understand how to best optimize the use of both RAG and fine-tuned models.
-   **Expanding LLM roles:** Increasing the role and capabilities of LLMs to further enhance RAG systems is of high interest.
-   **Scaling laws:** Investigation of LLM scaling laws and how they apply to RAG systems are still not properly understood.
-   **Production-ready RAG:** Production-grade RAG systems demand engineering excellence across performance, efficiency, data security, privacy, and more.
-   **Multimodal RAG:** While there have been lots of research efforts around RAG systems, they have been mostly centered around text-based tasks. There is increasing interest in extending modalities for a RAG system to support tackling problems in more domains such as image, audio and video, code, and more.
-   **Evaluation:** The interest in building complex applications with RAG requires special attention to develop nuanced metrics and assessment tools that can more reliably assess different aspects such as contextual relevance, creativity, content diversity, factuality, and more. In addition, there is also a need for better interpretability research and tools for RAG.

## RAG Tools

Some popular comprehensive tools to build RAG systems include [LangChain (opens in a new tab)](https://www.langchain.com/), [LlamaIndex (opens in a new tab)](https://www.llamaindex.ai/), and [DSPy (opens in a new tab)](https://github.com/stanfordnlp/dspy). There are also a range of specialized tools that serve different purposes such as [Flowise AI (opens in a new tab)](https://flowiseai.com/) that offers a low-code solution for building RAG applications. Other notables technologies include [HayStack (opens in a new tab)](https://haystack.deepset.ai/), [Meltano (opens in a new tab)](https://meltano.com/), [Cohere Coral (opens in a new tab)](https://cohere.com/coral), and others. Software and cloud service providers are also including RAG-centric services. For instance, Verba from Weaviate is useful for building personal assistant applications and Amazon's Kendra offers intelligent enterprise search services.

## Conclusion

In conclusion, RAG systems have evolved rapidly including the development of more advanced paradigms that enable customization and further the performance and utility of RAG across a wide range of domains. There is a huge demand for RAG applications, which has accelerated the development of methods to improve the different components of a RAG system. From hybrid methodologies to self-retrieval, these are some of the currently explored research areas of modern RAG models. There is also increasing demand for better evaluation tools and metrics. The figure below provides a recap of the RAG ecosystem, techniques to enhance RAG, challenges, and other related aspects covered in this overview:

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-ecosystem.b7b7d408.png&w=1920&q=75_[Figure Source (opens in a new tab)](https://arxiv.org/abs/2312.10997)_

## RAG Research Insights

Below is a collection of research papers highlighting key insights and the latest developments in RAG.

| **Insight** | **Reference** | **Date** |
| --- | --- | --- |
| Shows how retrieval augmentation can be used to distill language model assistants by training retrieval augmented simulators | [KAUCUS: Knowledge Augmented User Simulators for Training Language Model Assistants (opens in a new tab)](https://aclanthology.org/2024.scichat-1.5) | Mar 2024 |
| Proposes Corrective Retrieval Augmented Generation (CRAG) to improve the robustness of generation in a RAG system. The core idea is to implement a self-correct component for the retriever and improve the utilization of retrieved documents for augmenting generation. The retrieval evaluator helps to assess the overall quality of retrieved documents given a query. Using web search and optimized knowledge utilization operations can improve automatic self-correction and efficient utilization of retrieved documents. | [Corrective Retrieval Augmented Generation (opens in a new tab)](https://arxiv.org/abs/2401.15884) | Jan 2024 |
| Recursively embeds, clusters, and summarizes chunks of text, constructing a tree with differing levels of summarization from the bottom up. At inference time, the proposed RAPTOR model retrieves from the tree, integrating information across lengthy documents at different levels of abstraction. | [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval (opens in a new tab)](https://arxiv.org/abs/2401.18059) | Jan 2024 |
| A general program with multi-step interactions between LMs and retrievers to efficiently tackle multi-label classification problems. | [In-Context Learning for Extreme Multi-Label Classification (opens in a new tab)](https://arxiv.org/abs/2401.12178) | Jan 2024 |
| Extracts semantically similar prompts from high-resource languages to improve the zero-shot performance of multilingual pre-trained language models across diverse tasks. | [From Classification to Generation: Insights into Crosslingual Retrieval Augmented ICL (opens in a new tab)](https://arxiv.org/abs/2311.06595) | Nov 2023 |
| Improves the robustness of RAGs in facing noisy, irrelevant documents and in handling unknown scenarios. It generates sequential reading notes for retrieved documents, enabling a thorough evaluation of their relevance to the given question and integrating the information to prepare the final answer. | [Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models (opens in a new tab)](https://arxiv.org/abs/2311.09210) | Nov 2023 |
| Eliminates tokens that might not contribute essential information to optimize the answer generation process of a reader. Reduces run-time by up to 62.2%, with only a 2% reduction in performance. | [Optimizing Retrieval-augmented Reader Models via Token Elimination (opens in a new tab)](https://arxiv.org/abs/2310.13682) | Oct 2023 |
| Instruction-tunes a small LM verifier to verify the output and the knowledge of the knowledge-augmented LMs with a separate verifier. It helps to address scenarios where the model may fail to retrieve the knowledge relevant to the given query, or where the model may not faithfully reflect the retrieved knowledge in the generated text. | [Knowledge-Augmented Language Model Verification (opens in a new tab)](https://arxiv.org/abs/2310.12836) | Oct 2023 |
| Benchmark to analyze the performance of different LLMs in 4 fundamental abilities required for RAG, including noise robustness, negative rejection, information integration, and counterfactual robustness. | [Benchmarking Large Language Models in Retrieval-Augmented Generation (opens in a new tab)](https://arxiv.org/abs/2309.01431) | Oct 2023 |
| Introduces the Self-Reflective Retrieval-Augmented Generation (Self-RAG) framework that enhances an LM's quality and factuality through retrieval and self-reflection. It leverages an LM to adaptively retrieve passages, and generates and reflects on retrieved passages and its own generations using reflection tokens. | [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection (opens in a new tab)](https://arxiv.org/abs/2310.11511) | Oct 2023 |
| Improves zero-shot information retrieval by iteratively improving retrieval through generation-augmented retrieval (GAR) and improving rewrite through RAG. The rewrite-retrieval stages improves recall and a re-ranking stage improves precision. | [GAR-meets-RAG Paradigm for Zero-Shot Information Retrieval (opens in a new tab)](https://arxiv.org/abs/2310.20158) | Oct 2023 |
| Pretrains a 48B retrieval model using a base 43B GPT model and retrieving from 1.2 trillion tokens. The model is further instruction tuned to demonstrate significant improvement over the instruction tuned GPT on a wide range of zero-shot tasks. | [InstructRetro: Instruction Tuning post Retrieval-Augmented Pretraining (opens in a new tab)](https://arxiv.org/abs/2310.07713) | Oct 2023 |
| Retrofits an LLM with retrieval capabilities through two distinct fine-tuning steps: one updates a pre-trained LM to better use retrieved information, and the other updates the retriever to return more relevant results, as preferred by the LM. By fine-tuning over tasks that require both knowledge utilization and contextual awareness, each stage yields performance improvements. | [RA-DIT: Retrieval-Augmented Dual Instruction Tuning (opens in a new tab)](https://arxiv.org/abs/2310.01352) | Oct 2023 |
| A method to make RAGs robust to irrelevant content. It automatically generates data to fine-tune a language model to properly leverage retrieved passages, using a mix of relevant and irrelevant contexts at training time. | [Making Retrieval-Augmented Language Models Robust to Irrelevant Context (opens in a new tab)](https://arxiv.org/abs/2310.01558) | Oct 2023 |
| Finds that LLMs with 4K context window using simple retrieval-augmentation at generation achieve comparable performance to finetuned LLMs with 16K context window via positional interpolation on long context tasks. | [Retrieval meets Long Context Large Language Models (opens in a new tab)](https://arxiv.org/abs/2310.03025) | Oct 2023 |
| Compresses retrieved documents into textual summaries prior to in-context integration which reduces the computational costs and relieves the burden of LMs to identify relevant information in long retrieved documents. | [RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective Augmentation (opens in a new tab)](https://arxiv.org/abs/2310.04408) | Oct 2023 |
| An iterative retrieval-generation collaborative framework that leverages both parametric and non-parametric knowledge and helps to find the correct reasoning path through retrieval-generation interactions. Useful for tasks that require multi-step reasoning and overall improves reasoning ability of LLMs. | [Retrieval-Generation Synergy Augmented Large Language Models (opens in a new tab)](https://arxiv.org/abs/2310.05149) | Oct 2023 |
| Proposes Tree of Clarifications (ToC), a framework that recursively constructs a tree of disambiguations for ambiguous questions via few-shot prompting leveraging external knowledge. Then, it uses the tree to generate a long-form answer. | [Tree of Clarifications: Answering Ambiguous Questions with Retrieval-Augmented Large Language Models (opens in a new tab)](https://arxiv.org/abs/2310.14696) | Oct 2023 |
| An approach that lets an LLM refer to the questions it has previously encountered and adaptively call for external resources when encountering new questions. | [Self-Knowledge Guided Retrieval Augmentation for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2310.05002) | Oct 2023 |
| A suite of metrics which can be used to evaluate different dimensions (i.e., the ability of the retrieval system to identify relevant and focused context passages, the ability of the LLM to exploit such passages in a faithful way, or the quality of the generation itself) without having to rely on ground truth human annotations. | [RAGAS: Automated Evaluation of Retrieval Augmented Generation (opens in a new tab)](https://arxiv.org/abs/2309.15217) | Sep 2023 |
| Proposes a generate-then-read (GenRead) method, which first prompts a large language model to generate contextutal documents based on a given question, and then reads the generated documents to produce the final answer. | [Generate rather than Retrieve: Large Language Models are Strong Context Generators (opens in a new tab)](https://arxiv.org/abs/2209.10063) | Sep 2023 |
| Demonstrates how rankers such as DiversityRanker and LostInTheMiddleRanker can be utilized in a RAG system to select and utilize information that optimizes LLM context window utilization. | [Enhancing RAG Pipelines in Haystack: Introducing DiversityRanker and LostInTheMiddleRanker (opens in a new tab)](https://towardsdatascience.com/enhancing-rag-pipelines-in-haystack-45f14e2bc9f5) | Aug 2023 |
| Bridges LLMs with various knowledge bases (KBs), facilitating both the retrieval and storage of knowledge. The retrieval process employs program of thought prompting, which generates search language for KBs in code format with pre-defined functions for KB operations. It also offers the capability to store knowledge in a personalized KB, catering to individual user demands. | [KnowledGPT: Enhancing Large Language Models with Retrieval and Storage Access on Knowledge Bases (opens in a new tab)](https://arxiv.org/abs/2308.11761) | Aug 2023 |
| Proposes a model that combines retrieval-augmented masked language modeling and prefix language modeling. Then, it introduces Fusion-in-Context Learning to enhance few-shot performance by enabling the model to leverage more in-context examples without requiring additional training. | [RAVEN: In-Context Learning with Retrieval Augmented Encoder-Decoder Language Models (opens in a new tab)](https://arxiv.org/abs/2308.07922) | Aug 2023 |
| RaLLe is an open-source framework to develop, evaluate, and optimize RAG systems for knowledge-intensive tasks. | [RaLLe: A Framework for Developing and Evaluating Retrieval-Augmented Large Language Models (opens in a new tab)](https://arxiv.org/abs/2308.10633) | Aug 2023 |
| Finds that the performance of an LLM can degrade significantly when changing the position of relevant information, which indicates that LLMs do not robustly make use of information in long input contexts. | [Lost in the Middle: How Language Models Use Long Contexts (opens in a new tab)](https://arxiv.org/abs/2307.03172) | Jul 2023 |
| Synergizes retrieval and generation in an iterative manner. The model output is used to show what is needed to finish a task, providing informative context for retrieving more relevant knowledge which in turn helps generate a better output in the next iteration. | [Enhancing Retrieval-Augmented Large Language Models with Iterative Retrieval-Generation Synergy (opens in a new tab)](https://arxiv.org/abs/2305.15294) | May 2023 |
| Provides a generalized view of active RAG, methods that actively decide when and what to retrieve across the course of the generation. Then, proposes Forward-Looking Active REtrieval augmented generation (FLARE), a method which iteratively uses a prediction of the upcoming sentence to anticipate future content, which is then utilized as a query to retrieve relevant documents to regenerate the sentence if it contains low-confidence tokens. | [Active Retrieval Augmented Generation (opens in a new tab)](https://arxiv.org/abs/2305.06983) | May 2023 |
| Introduces a generic retrieval plug-in that utilizes a generic retriever to enhance target LMs that may be unknown in advance or are unable to be fine-tuned jointly. | [Augmentation-Adapted Retriever Improves Generalization of Language Models as Generic Plug-In (opens in a new tab)](https://arxiv.org/abs/2305.17331) | May 2023 |
| Improves dense retrieval on structured data through two pre-training strategies. First, it utilizes the natural alignment between structured and unstructured data for structure-aware pretraining. Then, it implements Masked Entity Prediction for masked entity prediction and capturing structural semantics. | [Structure-Aware Language Model Pretraining Improves Dense Retrieval on Structured Data (opens in a new tab)](https://arxiv.org/abs/2305.19912) | May 2023 |
| Dynamically incorporates grounding information from heterogeneous sources in multiple domains to enhance factual correctness of LLMs. Introduces an adaptive query generator to deal with queries tailored to different knowledge sources. The framework corrects rationales progressively to make sure that inaccuracies from preceding rationales do not propagate into the subsequent steps. | [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources (opens in a new tab)](https://arxiv.org/abs/2305.13269) | May 2023 |
| A framework to generate context-relevant and knowledge-grounded dialogues with a knowledge graph (KG). It first retrieves the relevant subgraph from the KG, and then enforces consistency across facts by perturbing their word embeddings conditioned by the retrieved subgraph. Then, it utilizes contrastive learning to ensure that the generated texts have high similarity to the retrieved subgraphs. | [Knowledge Graph-Augmented Language Models for Knowledge-Grounded Dialogue Generation (opens in a new tab)](https://arxiv.org/abs/2305.18846) | May 2023 |
| Adopts a small language model as a trainable rewriter to cater to a black-box LLM reader. The rewriter is trained using the feedback of the LLM reader by RL. Results in a new framework called Rewrite-Retrieve-Read where the focus is on optimizing queries. | [Query Rewriting for Retrieval-Augmented Large Language Models (opens in a new tab)](https://arxiv.org/abs/2305.14283) | May 2023 |
| Iteratively employs a retrieval-augmented generator to create an unbounded memory pool and uses a memory selector to choose one output as memory for the subsequent generation round. This enables a model to leverage its own output, referred to as self-memory, for improved generation. | [Lift Yourself Up: Retrieval-augmented Text Generation with Self Memory (opens in a new tab)](https://arxiv.org/abs/2305.02437) | May 2023 |
| Equips LLMs with a knowledge-guiding module to access relevant knowledge without altering its parameters. It improves performance of "black-box" LLMs on a range of domain knowledge-intensive tasks that require factual (+7.9%), tabular (+11.9%), medical (+3.0%), and multimodal (+8.1%) knowledge. | [Augmented Large Language Models with Parametric Knowledge Guiding (opens in a new tab)](https://arxiv.org/abs/2305.04757) | May 2023 |
| Equips LLMs with a general write-read memory unit, allowing them to extract, store, and recall knowledge from the text as needed for task performance. | [RET-LLM: Towards a General Read-Write Memory for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2305.14322) | May 2023 |
| Adopts a task-agnostic retriever to build a shared static index and select candidate evidence efficiently. Then, designs a prompt-guided reranker to rerank the nearest evidence according to task-specific relevance for the reader. | [Prompt-Guided Retrieval Augmentation for Non-Knowledge-Intensive Tasks (opens in a new tab)](https://arxiv.org/abs/2305.17653) | May 2023 |
| Proposes UPRISE (Universal Prompt Retrieval for Improving zero-Shot Evaluation), which tunes a lightweight and versatile retriever that automatically retrieves prompts for a given zero-shot task input. | [UPRISE: Universal Prompt Retrieval for Improving Zero-Shot Evaluation (opens in a new tab)](https://arxiv.org/abs/2303.08518) | Mar 2023 |
| An adaptive filter-then-rerank paradigm that combines the strengths of SLMs (serve as filters) and LLMs (serve as rerankers). | [Large Language Model Is Not a Good Few-shot Information Extractor, but a Good Reranker for Hard Samples! (opens in a new tab)](https://arxiv.org/abs/2303.08559) | Mar 2023 |
| Zero-shot instructs an instruction-following LLM to generate a hypothetical document that captures relevance patterns. Then, a Contriever encodes the document into an embedding vector which is used to identify a neighborhood in the corpus embedding space, where similar real documents are retrieved based on vector similarity. | [Precise Zero-Shot Dense Retrieval without Relevance Labels (opens in a new tab)](https://arxiv.org/abs/2212.10496) | Dec 2022 |
| Proposes Demonstrate-Search-Predict (DSP), a framework to compose high-level programs that bootstrap pipeline-aware demonstrations, search for relevant passages, and generate grounded predictions, systematically breaking down problems into small transformations that can be handled more reliably. | [Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP (opens in a new tab)](https://arxiv.org/abs/2212.14024) | Dec 2022 |
| An approach for multi-step QA that interleaves retrieval with steps in a CoT, guiding the retrieval with CoT and in turn using retrieved results to improve CoT. This helps to improve performance on knowledge-intensive multi-step questions. | [Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions (opens in a new tab)](https://arxiv.org/abs/2212.10509) | Dec 2022 |
| Shows that retrieval-augmentation can reduce the dependence on relevant pre-training information, which makes RAG a promising approach for capturing the long-tail. | [Large Language Models Struggle to Learn Long-Tail Knowledge (opens in a new tab)](https://arxiv.org/abs/2211.08411) | Nov 2022 |
| Recites one or several relevant passages from LLMs' own memory via sampling, and then produces the final answers. | [Recitation-Augmented Language Models (opens in a new tab)](https://arxiv.org/abs/2210.01296) | Oct 2022 |
| Leverages LLMs as a few-shot query generator, and creates task-specific retrievers based on the generated data. | [Promptagator: Few-shot Dense Retrieval From 8 Examples (opens in a new tab)](https://arxiv.org/abs/2209.11755) | Sep 2022 |
| Presents Atlas, a pre-trained retrieval augmented language model able to learn knowledge intensive tasks with very few training examples. | [Atlas: Few-shot Learning with Retrieval Augmented Language Models (opens in a new tab)](https://arxiv.org/abs/2208.03299) | Aug 2022 |
| Retrieves from the training data to achieve gains on multiple NLG and NLU tasks. | [Training Data is More Valuable than You Think: A Simple and Effective Method by Retrieving from Training Data (opens in a new tab)](https://arxiv.org/abs/2203.08773) | Mar 2022 |
| Approximates a datastore search by saving pointers between consecutive datastore entries, and clustering those entries into states. Results in a weighted finite automaton that, at inference time, helps save up to 83% of the nearest neighbor searchers over kNN-LM without hurting perplexity. | [Neuro-Symbolic Language Modeling with Automaton-augmented Retrieval (opens in a new tab)](https://arxiv.org/abs/2201.12431) | Jan 2022 |
| Improves an auto-regressive language model by conditioning on document chunks retrieved from a large corpus, based on local similarity with preceding tokens. It enhances the model by retrieving from a 2 trillion token database. | [Improving language models by retrieving from trillions of tokens (opens in a new tab)](https://arxiv.org/abs/2112.04426) | Dec 2021 |
| A novel approach to zero-shot slot filling that extends dense passage retrieval with hard negatives and robust training procedures for retrieval augmented generation models. | [Robust Retrieval Augmented Generation for Zero-shot Slot Filling (opens in a new tab)](https://arxiv.org/abs/2108.13934) | Aug 2021 |
| Introduces RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. It compares two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, and the other uses different passages per token. | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (opens in a new tab)](https://arxiv.org/abs/2005.11401) | May 2020 |
| Shows that retrieval can be implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a simple dual-encoder framework. | [Dense Passage Retrieval for Open-Domain Question Answering (opens in a new tab)](https://arxiv.org/abs/2004.04906) | Apr 2020 |

## References

-   [KAUCUS: Knowledge Augmented User Simulators for Training Language Model Assistants (opens in a new tab)](https://aclanthology.org/2024.scichat-1.5)
-   [A Survey on Hallucination in Large Language Models: Principles,Taxonomy, Challenges, and Open Questions (opens in a new tab)](https://arxiv.org/abs/2311.05232)
-   [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (opens in a new tab)](https://arxiv.org/abs/2005.11401)
-   [Retrieval-augmented multimodal language modeling (opens in a new tab)](https://arxiv.org/abs/2211.12561)
-   [In-Context Retrieval-Augmented Language Models (opens in a new tab)](https://arxiv.org/abs/2302.00083)
-   [Precise Zero-Shot Dense Retrieval without Relevance Labels (opens in a new tab)](https://arxiv.org/abs/2212.10496)
-   [Shall we pretrain autoregressive language models with retrieval? a comprehensive study. (opens in a new tab)](https://arxiv.org/pdf/2312.10997.pdf)
-   [REPLUG: Retrieval-Augmented Black-Box Language Models (opens in a new tab)](https://arxiv.org/abs/2301.12652)
-   [Query2Doc (opens in a new tab)](https://arxiv.org/abs/2303.07678)
-   [ITER-RETGEN (opens in a new tab)](https://arxiv.org/abs/2305.15294)
-   [A Survey of Techniques for Maximizing LLM Performance (opens in a new tab)](https://youtu.be/ahnGLM-RC1Y?si=z45qrLTPBfMe15LM)
-   [HyDE (opens in a new tab)](https://arxiv.org/abs/2212.10496)
-   [Advanced RAG Techniques: an Illustrated Overview (opens in a new tab)](https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6)
-   [Best Practices for LLM Evaluation of RAG Applications (opens in a new tab)](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG)
-   [Building Production-Ready RAG Applications (opens in a new tab)](https://youtu.be/TRjq7t2Ms5I?si=gywRj82NIc-wsHcF)
-   [Evaluating RAG Part I: How to Evaluate Document Retrieval (opens in a new tab)](https://www.deepset.ai/blog/rag-evaluation-retrieval)
-   [Retrieval Augmented Generation meets Reciprocal Rank Fusion and Generated Queries (opens in a new tab)](https://towardsdatascience.com/forget-rag-the-future-is-rag-fusion-1147298d8ad1)

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

This article will focus on RAG systems and architecture. If you’re interested in learning more about vector search, we recommend the following articles: [What is a Vector Database?](https://qdrant.tech/articles/what-is-a-vector-database/) and [What are Vector Embeddings?](https://qdrant.tech/articles/what-are-embeddings/).

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

If you’re interested in going deeper, refer to our article on [Sparse Vectors](https://qdrant.tech/articles/sparse-vectors/).

##### Dense vector embeddings

This approach uses large language models like [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29) to encode the query and passages into dense vector embeddings. These models are compact numerical representations that capture semantic meaning. Vector databases like Qdrant store these embeddings, allowing retrieval based on **semantic similarity** rather than just keywords using distance metrics like cosine similarity.

This allows the retriever to match based on semantic understanding rather than just keywords. So if I ask about “compounds that cause BO,” it can retrieve relevant info about “molecules that create body odor” even if those exact words weren’t used. We explain more about it in the [What are Vector Embeddings](https://qdrant.tech/articles/what-are-embeddings/) article.

#### Hybrid search

However, neither keyword search nor vector search are always perfect. Keyword search may miss relevant information expressed differently, while vector search can sometimes struggle with specificity or neglect important statistical word patterns. Hybrid methods aim to combine the strengths of different techniques.

https://qdrant.tech/articles_data/what-is-rag-in-ai/hybrid-search.jpg

Some common hybrid approaches include:

- Using keyword search to get an initial set of candidate documents. Next, the documents are re-ranked/re-scored using semantic vector representations.
- Starting with semantic vectors to find generally topically relevant documents. Next, the documents are filtered/re-ranked e based on keyword matches or other metadata.
- Considering both semantic vector closeness and statistical keyword patterns/weights in a combined scoring model.
- Having multiple stages were different techniques. One example: start with an initial keyword retrieval, followed by semantic re-ranking, then a final re-ranking using even more complex models.

When you combine the powers of different search methods in a complementary way, you can provide higher quality, more comprehensive results. Check out our article on [Hybrid Search](https://qdrant.tech/articles/hybrid-search/) if you’d like to learn more.

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

Learn more about how to properly evaluate your RAG responses: [Evaluating Retrieval Augmented Generation - a framework for assessment](https://superlinked.com/vectorhub/evaluating-retrieval-augmented-generation-a-framework-for-assessment).

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