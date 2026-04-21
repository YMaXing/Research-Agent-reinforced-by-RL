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

-----

Phase: [EXPLOITATION]

### Source [10]: https://samirpaulb.github.io/posts/vector-databases-rag-llm/

Query: How are vector embeddings generated and stored in vector databases to enable semantic similarity search as the core of the retrieval component in RAG systems?

Answer: A vector database is a specialized database designed to store and query high-dimensional vector embeddings efficiently. Unlike traditional databases that excel at exact matches, vector databases excel at similarity searches. Embeddings transform text into searchable vectors capturing semantic meaning. Vector databases enable fast similarity search at scale (HNSW is the standard). RAG Architecture Overview - Flow: User query → Embedding model → Vector database → Retrieved documents → LLM → Answer. RAG Pipeline Steps: 1. User Query → User asks a question 2. Query Embedding → Convert query to vector 3. Vector Search → Find similar documents 4. Context Retrieval → Fetch document content.

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
<summary>What theoretical analyses explain the "lost in the middle" phenomenon in long-context RAG prompting, and which context reordering or compression techniques have shown to improve generation quality?</summary>

Phase: [EXPLORATION]

### Source [61]: https://arxiv.org/html/2410.05983v1

Query: What theoretical analyses explain the "lost in the middle" phenomenon in long-context RAG prompting, and which context reordering or compression techniques have shown to improve generation quality?

Answer: The 'lost-in-the-middle' phenomenon in long-context RAG is attributed to the interplay of two factors that become increasingly significant with larger retrieval sets: (1) the amplified 'lost-in-the-middle' phenomenon, where LLMs prioritize information at the beginning and end of the input sequence, and (2) the increased prevalence of hard negatives, which can hinder accurate answer generation. As highlighted by Liu et al. (2024), LLMs exhibit a tendency to prioritize information presented at the beginning and end of an input sequence, while paying less attention to the middle. Retrieval reordering mitigates these issues by strategically placing passages, leveraging the inherent 'lost-in-the-middle' phenomenon to mitigate the negative effects of hard negatives. The strategy involves reordering the retrieved passages based on their relevance scores calculated by the retriever. Given a query q and a set of retrieved passages d1, d2, …, dk with decreasing relevance scores, the standard input sequence is [I, d1, d2, …, dk−1, dk, q], but reordering places the most relevant passages at the beginning and end.

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf

Query: What theoretical analyses explain the "lost in the middle" phenomenon in long-context RAG prompting, and which context reordering or compression techniques have shown to improve generation quality?

Answer: The 'lost in the middle' phenomenon is observed where performance is highest when the answer is at the very beginning or very end of the context, and it drops when the answer sits in the middle. This is due to attention dilution: more tokens make it harder to focus on the right span, leading to a U-shaped performance curve. For RAG pipelines, practical implications include re-ranking so the best evidence is first (or last), trimming irrelevant text, avoiding unnecessary length, preferring chunking/sliding windows or hierarchical aggregation. If controlling the prompt, bias it so key evidence is early (or echoed late), pre-summarize, highlight, or quote the most relevant spans, keep contexts lean. For documents not controlled, use retrieval + re-ranking to bring the best passages forward. Consider hierarchical or multi-step reading rather than a single monolithic prompt. Longer windows alone do not solve the problem; models lose focus, suffer from attention dilution, and forget critical information.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://machinelearningmastery.com/5-techniques-for-efficient-long-context-rag/

Query: What theoretical analyses explain the "lost in the middle" phenomenon in long-context RAG prompting, and which context reordering or compression techniques have shown to improve generation quality?

Answer: The 'Lost in the Middle' problem, identified in a 2023 study by Stanford and UC Berkeley, reveals a critical limitation in LLM attention mechanisms. When presented with long context, model performance peaks when relevant information appears at the beginning or end; information buried in the middle is significantly more likely to be ignored or misinterpreted. Technique 1: Implementing a Reranking Architecture to Fight 'Lost in the Middle'. Reranking brings the most relevant chunks to the front (or end) of the context window, countering the attention bias. This involves a two-stage retrieval: initial embedding search followed by a cross-encoder reranker (e.g., using models like MS-MARCO or domain-specific fine-tunes).

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://arxiv.org/html/2409.13385v1

Query: What theoretical analyses explain the "lost in the middle" phenomenon in long-context RAG prompting, and which context reordering or compression techniques have shown to improve generation quality?

Answer: Liu et al. (2024) identified the 'lost in the middle' issue where language models struggle with information in long contexts. Modeling long-range dependencies is a hurdle for Transformer-based LMs due to self-attention. Efforts to handle long contexts include Context Distillation, Prompting, Efficient Attention Operations, Extrapolation and Interpolation, and Context Window Extension. A novel approach, 'context compression', proposed by Ge et al. (2023), recognizes that an LLM can represent the same information in varying lengths. They introduce the In-context Autoencoder (ICAE), which compresses lengthy contexts into a fixed number of memory buffers using a learnable encoder and a fixed decoder.

-----

-----

Phase: [EXPLORATION]

### Source [65]: https://openreview.net/pdf/6c92fb0f99f1065fec1f61cbe6a4e9263a28501b.pdf

Query: What theoretical analyses explain the "lost in the middle" phenomenon in long-context RAG prompting, and which context reordering or compression techniques have shown to improve generation quality?

Answer: Liu et al. (2024a) first identified the 'lost-in-the-middle' problem, where LLMs struggle to capture information in the middle of long contexts. The Compress method introduces a preprocessing stage using LLMLingua model (Jiang et al., 2023) to achieve 50% text compression by discarding non-essential content while retaining key information via semantic-aware compression, easing the LLM’s contextual processing burden. RAL-WRITER alleviates the 'lost-in-the-middle' issue, showing reduced decline in accuracy for questions related to the middle position compared to baselines like AgentWrite, Compress, and single-model invocation.

-----

</details>

<details>
<summary>How do uncertainty quantification methods from probabilistic machine learning apply to calibrating confidence scores in RAG outputs to better identify and handle residual hallucination risks?</summary>

Phase: [EXPLORATION]

### Source [66]: https://www.nature.com/articles/s41598-024-65954-w

Query: How do uncertainty quantification methods from probabilistic machine learning apply to calibrating confidence scores in RAG outputs to better identify and handle residual hallucination risks?

Answer: Uncertainty quantification in probabilistic machine learning uses conformal prediction to calibrate confidence scores. Nonconformity scores are computed for calibration, then used to determine a probability threshold for a user-defined confidence level (1-alpha) via finite-sample correction: qLevel = ceil((1 + nCal)(1 - α)) / nCal, where qLevel is the adjusted quantile, α is the error tolerance, and nCal is calibration set size. During inference, classes with nonconformity scores >= threshold are included in prediction sets, ensuring only high-confidence predictions are output. Data is split into 80% calibration and 20% test sets. Calibrated conformal classifiers produce prediction sets including the true class with high probability (e.g., empirical marginal coverage 0.89 at 0.9 confidence). Probability thresholds are computed for confidence levels 0.7 to 0.95. This calibration aligns predicted confidence with actual coverage, applicable to identifying low-confidence RAG outputs as potential hallucinations for handling risks.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://www.ibm.com/think/topics/uncertainty-quantification

Query: How do uncertainty quantification methods from probabilistic machine learning apply to calibrating confidence scores in RAG outputs to better identify and handle residual hallucination risks?

Answer: Uncertainty quantification (UQ) treats model outputs as random variables with probability distributions; wider distributions indicate higher uncertainty. UQ calibrates models so predicted confidence p matches correctness rate p (e.g., p-confident predictions are correct p% of time). Calibration metrics group probabilities across datasets; proper scoring rules evaluate deviation from true distributions for probabilistic models. Use multiple metrics as they capture different uncertainty aspects. Calibrated confidence scores in RAG enable identifying low-confidence outputs as hallucination risks, allowing abstention or hedging to handle residual risks reliably.

-----

-----

Phase: [EXPLORATION]

### Source [69]: https://aws.amazon.com/blogs/machine-learning/detect-hallucinations-for-rag-based-systems/

Query: How do uncertainty quantification methods from probabilistic machine learning apply to calibrating confidence scores in RAG outputs to better identify and handle residual hallucination risks?

Answer: Hallucination detection in RAG uses stochastic sampling: generate N answers from LLM, compute BERT scores (cosine similarity of embeddings) between original sentences and samples. High consistency (high BERT scores) indicates factual content; low consistency signals hallucinations. Parse outputs for sentence-level 0-1 scores, tune domain-specific thresholds independently from Q&A LLM. Classify as hallucination or fact based on threshold. Store query, context, answer for evaluation. This uncertainty measure via generation variability calibrates confidence, identifying inconsistent (low-score) RAG outputs as hallucination risks for handling.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://purl.stanford.edu/sm978sh0523

Query: How do uncertainty quantification methods from probabilistic machine learning apply to calibrating confidence scores in RAG outputs to better identify and handle residual hallucination risks?

Answer: Reliable uncertainty quantification requires calibration where predicted probabilities align with empirical frequencies (e.g., 90% CI includes outcome 90% time). Interventions improve calibration across model lifecycle: training objectives, post-processing to correct miscalibration, online adaptive techniques with vanishing regret vs. expert predictors. This enables trustworthy uncertainty estimates for high-stakes settings, applicable to RAG by calibrating confidence scores to identify low-confidence outputs as residual hallucination risks, allowing safe handling like abstention.

-----

</details>

<details>
<summary>How have core RAG retrieval and augmentation principles been adapted and applied within enterprise knowledge management systems in regulated industries such as finance and healthcare?</summary>

Phase: [EXPLORATION]

### Source [71]: https://www.kore.ai/blog/what-is-rag-retrieval-augmented-generation

Query: How have core RAG retrieval and augmentation principles been adapted and applied within enterprise knowledge management systems in regulated industries such as finance and healthcare?

Answer: Enterprise RAG is designed to retrieve and generate knowledge securely, transparently, and in alignment with organizational policies, becoming a trusted intelligence system for sensitive and regulated functions in highly regulated industries such as finance, banking, insurance, healthcare, and law. Example: A financial analyst asks, 'What regulatory risks should I flag for our European investment portfolio?' Enterprise RAG retrieves sensitive data from internal systems, applies compliance filters, synthesizes insights, and provides a citation-backed answer while logging the process for audit. RAG reduces hallucinations by tying outputs to retrieved knowledge, crucial for high-stakes industries like healthcare and finance where it is a prerequisite for safe deployment. In healthcare, RAG retrieves latest clinical trial results, emerging therapies, and updated protocols for queries like 'new cancer treatments,' synthesizing into precise summaries for evidence-based decisions. In finance, for 'Q1 financial outlook,' it retrieves current economic data, analyst insights, and real-time market trends, generating concise answers with risks, opportunities, and actionable insights.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://www.mdpi.com/2076-3417/16/1/368

Query: How have core RAG retrieval and augmentation principles been adapted and applied within enterprise knowledge management systems in regulated industries such as finance and healthcare?

Answer: Organizations in finance and healthcare must organize, retrieve, and integrate knowledge to comply with regulations using RAG for knowledge management (KM) and document automation, as traditional systems struggle with evolving data. On-premises deployments ensure data sovereignty and regulatory compliance in these sectors. Enterprise RAG architecture uses a retriever to identify relevant document chunks from corporate corpus via dense vector similarity or sparse keyword matching, fed into LLM for grounded generation. Enterprise implementations employ hybrid indexing strategies combining dense embeddings with symbolic Knowledge Graphs (KGs) for high precision and auditability required in regulated industries.

-----

</details>

<details>
<summary>What foundational ideas from 1980s-1990s case-based reasoning and information retrieval theory have been scaled and rediscovered in contemporary LLM-powered RAG architectures?</summary>

Phase: [EXPLORATION]

### Source [76]: https://arxiv.org/abs/2404.04302

Query: What foundational ideas from 1980s-1990s case-based reasoning and information retrieval theory have been scaled and rediscovered in contemporary LLM-powered RAG architectures?

Answer: The paper introduces CBR-RAG: Case-Based Reasoning for Retrieval Augmented Generation in LLMs for Legal Question Answering. It directly connects 1980s-1990s case-based reasoning (CBR) to modern RAG architectures. CBR, a foundational AI paradigm from the 1980s-1990s, involves retrieving similar past cases (experiences) from a case base, adapting them to the current problem, and storing new solutions. This retrieve-adapt-generate cycle is rediscovered and scaled in RAG, where LLMs retrieve relevant documents or cases from a knowledge base, augment the prompt, and generate answers. In legal QA, CBR-RAG enhances RAG by using CBR principles: case retrieval based on similarity to the query, selection of most relevant cases, adaptation via LLM reasoning, and evaluation. This scales classic CBR (e.g., from ICCBR conferences) to handle large-scale legal corpora with vector embeddings and LLMs, improving factual accuracy and reducing hallucinations compared to standard RAG.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://arxiv.org/html/2502.14822v3

Query: What foundational ideas from 1980s-1990s case-based reasoning and information retrieval theory have been scaled and rediscovered in contemporary LLM-powered RAG architectures?

Answer: The survey traces IR evolution from 1980s-1990s term-based retrieval models like BM25 to neural architectures integrated in modern RAG. Foundational IR ideas—probabilistic ranking (e.g., BM25 from Okapi/Atire systems in 1990s), term frequency-inverse document frequency (TF-IDF from 1970s-1980s), and vector space models (Salton 1975, scaled in 1980s)—are scaled in LLM-powered RAG via dense retrieval (e.g., DPR, ColBERT) using transformers for semantic embeddings. Learning-to-Rank (LTR) from 2000s builds on 1990s supervised ranking, combining BM25 signals with learned functions; this is rediscovered in RAG's hybrid retrieval (sparse + dense) and reranking stages. RAG architectures process raw inputs, extract features with Transformer backbones (BERT/DPR), and estimate relevance, transforming heuristic IR scoring into end-to-end neural systems. Challenges include scaling to multimodal data, mirroring 1990s IR expansions.

-----

-----

Phase: [EXPLORATION]

### Source [79]: https://aclanthology.org/2026.eacl-long.350.pdf

Query: What foundational ideas from 1980s-1990s case-based reasoning and information retrieval theory have been scaled and rediscovered in contemporary LLM-powered RAG architectures?

Answer: Mentions retrieval-augmented-generation (RAG) enhancements via metacognition and Theory of Mind (ToM), drawing from 1970s-1990s cognitive psych (Flavell 1979). RAG (Asai et al. 2024; Zhou et al. 2024) scales 1980s-1990s introspective reasoning for hallucination mitigation, akin to case-based reflection. Links to Kahneman's 2011 System 1/2 (roots in 1980s dual-process theories), operationalized in RAG via chain-of-thought, tree-of-thoughts for retrieval coherence. Perception, attention, memory support RAG retrieval, rediscovering 1990s cognitive architectures in LLM prompting for multi-hop QA and tool use.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="aclanthology-org.md">
<details>
<summary>aclanthology-org</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://aclanthology.org/2024.emnlp-main.15.pdf>

The provided markdown content appears to be a full research paper, including its abstract, main sections, figures, tables, and a comprehensive bibliography/appendix. It does not contain any web-page boilerplate such as site headers, footers, navigation menus, cookie banners, advertisements, sidebars, subscription prompts, self-promotion blocks, social-media share buttons, or "related articles" sections in the typical sense of a blog post.

According to the critical rules:
- Keep ALL substantive article content.
- Do NOT filter or remove sections based on topic relevance.
- Do NOT summarize, condense, paraphrase, or rewrite. Return it verbatim.
- When in doubt, **keep** the content.

Therefore, the entire content is considered substantive and will be returned verbatim.

```markdown
Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs

Oded Ovadia\*, Meni Brief\*, Moshik Mishaeli, and Oren Elisha
Microsoft, Israel

Abstract

Large language models (LLMs) encapsulate a vast amount of factual information within their pre-trained weights, as evidenced by their ability to answer diverse questions across different domains. However, this knowledge is inherently limited, relying heavily on the characteristics of the training data. Consequently, using external datasets to incorporate new information or refine the capabilities of LLMs on previously seen information poses a significant challenge. In this study, we compare two common approaches: unsupervised fine-tuning and retrieval-augmented generation (RAG). We evaluate both approaches on a variety of knowledge-intensive tasks across different topics. Our findings reveal that while unsupervised fine-tuning offers some improvement, RAG consistently outperforms it, both for existing knowledge encountered during training and entirely new knowledge. Moreover, we find that LLMs struggle to learn new factual information through unsupervised fine-tuning and that exposing them to numerous variations of the same fact during training could alleviate this problem.

1 Introduction

Large language models (LLMs) are able to capture vast amounts of factual information (Petroni et al., 2019; Cohen et al., 2023; Hu et al., 2023). LLMs exhibit a remarkable level of knowledge in various domains due to their massive pre-training datasets. However, there are two significant limitations to this knowledge. First, it is static and does not update with time. Second, it is non-specific and thus may lack nuanced expertise in particular domains. While these are two different problems, they are deeply related since their solution is the same: enhancing the model’s knowledge.

Recently, the idea of adapting LLMs to particular domains and updating their knowledge has become increasingly common (Yu et al., 2022). Various models have been suggested to improve factual knowledge and capabilities in diverse fields such as healthcare (Singhal et al., 2023a,b; Wu et al., 2023a), finance (Wu et al., 2023b; Yang et al., 2023), and law (Huang et al., 2023; Nguyen, 2023).

In this work, we focus on the evaluation of a model’s knowledge and its ability to memorize, understand, and retrieve factual data. We aim to understand the concept of knowledge injection (Wang et al., 2020; Chen et al., 2022; Liu et al., 2020; Lauscher et al., 2020). Given some knowledge base in the form of a text corpus, what is the best way to teach a pre-trained model this knowledge?

One way to add knowledge to a pre-trained model is through fine-tuning. With fine-tuning, we continue the model’s training process and adapt it using task-specific data. By exposing the model to a specific knowledge base, we expect the model weights to adapt accordingly. This process is meant to optimize the model for targeted applications, enhancing its performance and contextual relevance in specialized domains.

Another method to enhance a model’s knowledge base is through the use of in-context learning (ICL) (Chen et al., 2021; Radford et al., 2019; Min et al., 2021; Lampinen et al., 2022). The main idea behind ICL is to improve the performance of pre-trained LLMs on new tasks by modifying the input query to the model without directly changing the weights of the model. One form of ICL is retrieval augmented generation (RAG) (Lewis et al., 2020; Neelakantam et al., 2022). RAG uses information retrieval techniques to enable LLMs to obtain relevant information from a knowledge source and incorporate it into generated text.

This study aims to evaluate the knowledge injection capabilities of LLMs through a comparison of fine-tuning and RAG. To illustrate the rationale, let us use an analogy. Consider three college students taking a test on a specific topic. All had access to class materials but didn’t know the topic before-hand. The first student had the textbook only during the test, the second had pre-test access and studied, and the third lost access upon the test announcement. Who would probably perform better?

2 Background

To assess knowledge injection, we must first understand what knowledge means for LLMs.

Knowledge and Language Models Defining knowledge is a complex philosophical task far beyond the scope of this research. However, we can examine what factual knowledge means in the context of language models. If a model knows a fact, it can accurately and consistently answer questions about it. Furthermore, it can reliably distinguish between true and false statements related to this fact. We can then extend this definition to a whole knowledge base, not just a single fact.

Mathematically, let $Q = {q\_{i,j}} _{i,j=1}^{N}$ be a set of $N$ multiple choice factual questions, where each question has $L$ possible answers and exactly one correct answer. Let $A = {a_{i\_1}, \\dots, a\_{i\_n}} _{i=1}^N$ be the corresponding set of possible answers, and $C = {c_{n}}\_{n=1}^N$ be the correct answers.

Let $\\mathcal{M}$ be a language model. We denote by $\\mathcal{M}(q\_{i\_j}) \\in {a\_{i\_1}, \\dots, a\_{i\_n}}\_{i=1}^N$ the predicted answer of the model to the $n$-th question. We define the knowledge score $\\mathcal{L}$ of $\\mathcal{M}$ in relation to $\\mathcal{Q}$ to be the standard accuracy score:

$$\\mathcal{L} _{\\mathcal{M}, Q} := \\frac{#{q_{i\_j}} \\mathcal{M}(q\_{i\_j}) = c\_{n}}{L}.$$

(1)

We say that the model $\\mathcal{M}$ possesses any knowledge regarding the set of questions $\\mathcal{Q}$ if the following holds:

$$\\mathcal{L}\_{\\mathcal{M}, Q} > \\frac{1}{L}.$$

(2)

In simpler terms, the model can consistently give correct answers, outperforming a simple random guessing baseline. Naturally, if the knowledge score $\\mathcal{L}\_{\\mathcal{M}, Q}$ is higher for one model compared to another, then we assert that the former is more knowledgeable with regards to $\\mathcal{Q}$ compared to the latter.

Previously Seen Knowledge One important distinction to make is between knowledge that the model has been exposed to before during pretraining as opposed to entirely new facts. Considering the size of modern LLM training sets, they cover a vast amount of information available through web-sourced text. As a result, even in niche domains, the goal of knowledge injection is not necessarily to teach the model entirely new facts but rather to "refresh" its memory by inducing a bias toward a particular domain.

Knowledge and Reasoning We emphasize that this knowledge evaluation framework for LLMs is imperfect. Importantly, it doesn’t address other quality metrics influencing a model’s response. Creating a purely knowledge-intensive dataset without involving some level of reasoning is challenging. Consequently, a model with robust reasoning abilities might excel on unfamiliar knowledge-intensive tasks by making “educated guesses” in a multiple-choice exam. Therefore, any evaluation of knowledge in LLMs should consider this, with results seen as part of a broader range of benchmarks for reasoning (Sakaguchi et al., 2021), reading comprehension (Dua et al., 2019), and general language abilities (Srivastava et al., 2022). However, this evaluation framework still strongly emphasizes factual information above all else.

Causes for Factual Errors There are many possible reasons for the failure of models to answer factual questions accurately. In (Wang et al., 2023), Wang et al. introduce a taxonomy of five main model-level causes:

• Domain knowledge deficit: A language model may lack comprehensive expertise in a specific domain to which it has not been exposed. For example, a model trained exclusively on texts written by William Shakespeare would perform poorly when asked about the works of Mark Twain.

• Outdated Information: LLMs invariably have a cutoff date determined by their training dataset. Consequently, any events, discoveries, or changes occurring after the last training update will not be within the model's knowledge without access to external sources.

• Immemorization: Sometimes, a model is exposed to knowledge during its training process but does not retain it. This is especially true for rare facts that appear in the training dataset only scarcely (Kandal et al., 2023).

• Forgetting: Language models often undergo additional training after the pre-training phase (fine-tuning). In some cases, this might lead to a phenomenon called catastrophic forgetting

* * *

Figure 1: A visualization of the knowledge injection framework.

(Kirkpatrick et al., 2017; Goodfellow et al., 2013; Chen et al., 2020; Luo et al., 2023), where models lose some of the knowledge they had prior to the fine-tuning process.

• Reasoning Failure: In certain instances, a language model might possess relevant knowledge about a fact but fail to utilize it properly. This is particularly evident in complex multi-step reasoning tasks (Tan et al., 2023) or when posed with different questions about the same fact, resulting in disparate outcomes (Berghund et al., 2023).

We observe that most of these issues arise during the pre-training phase, with catastrophic forgetting being the notable exception. Hence, many LLMs will suffer from factual errors of this kind regardless of any post-training process.

3 Injecting Knowledge to Language Models

Following the background given in Section 2, it is clear that general pre-training is insufficient for many knowledge-intensive tasks. To solve this, an additional post-processing step is essential to augment the knowledge of a pre-trained model. This step is often referred to as knowledge injection (Wang et al., 2020; Chen et al., 2022; Liu et al., 2020; Lauscher et al., 2020).

In this section, we examine two widely used frameworks for knowledge injection: fine-tuning

(FT) and retrieval augmented generation (RAG). We begin by formulating the knowledge injection problem, aiming to explain both methods using consistent terminology.

3.1 Problem formulation

In Equations (1) and (2), we presented a formulation for knowledge in language models through the lens of question-answering (Q&A). We now extend this formulation to the problem of knowledge injection using the same terminology.

Given a set of factual questions, there exists some text corpus containing information that is relevant to these questions. The central assumption of knowledge injection is that given full access to this corpus, it could serve as an auxiliary knowledge base and improve the model's performance on this set of questions.

Mathematically, let $M$ be a pre-trained model, and let $Q$ be a set of factual questions, as before. Now, assume we have a relevant auxiliary knowledge base $B\_Q$. Our objective is to discover a transformation, denoted as $F$, that, when applied, would enhance the knowledge about $Q$:

$$M' := F(M, B\_Q) \\quad s.t. \\quad L\_{M', Q} > L\_{M, Q}. \\tag{3}$$

In this work, we aim to compare two choices for $F$: fine-tuning and RAG to see which option performs better in this problem.

* * *

3.2 Fine-Tuning

Fine-tuning is the process of adjusting a pre-trained model on a specific, often narrower, dataset or task to enhance its performance in that particular domain. Here, it is vital to distinguish between different types of fine-tuning. FT techniques are commonly classified into supervised, unsupervised, and reinforcement learning (RL) based methods. We proceed by briefly reviewing these methods and their relation to the problem of knowledge injection.

Supervised Fine-Tuning Supervised fine-tuning (SFT) requires sets of labeled input-output pairs. One of the most common SFT methods is instruction tuning (Wang et al., 2022; Mishra et al., 2021; Ouyang et al., 2022; Taori et al., 2023), which has emerged as one of the most powerful methods to improve model performance. With instruction tuning, the input is a natural language task description, and the output is an example of the desired behavior. Many current state-of-the-art LLMs have gone through instruction tuning after their pre-training phase.

Instruction tuning has been shown to be very effective at improving the overall quality of the model, with a particular emphasis on its zero-shot and reasoning capabilities. However, despite these advantages, instruction tuning does not necessarily teach the model new knowledge (Ouyang et al., 2022; Cheng et al., 2022; Mitra et al., 2023; Chia et al., 2023; Zhou et al., 2023). As such, instruction tuning alone is not a viable solution to the knowledge injection problem.

Reinforcement Learning Another form of FT relus on RL or RL-inspired optimization strategies to better align the model after its pre-training task. A few prominent examples are reinforcement learning from human feedback (LRHF) (OpenAI, 2023; Touvron et al., 2023), direct preference optimization (DPO) (Rafailov et al., 2023), and proximal policy optimization (PPO) (Schulman et al., 2017; Tunstall et al., 2023).

These techniques have been shown to be very useful, especially when used in conjunction with instruction tuning. However, similarly to instruction tuning, these methods focus on the overall quality of the response and its expected behavior and not necessarily on its breadth of knowledge.

Unsupervised Fine-Tuning The final FT strategy we discuss is unsupervised, meaning there are no available labels for the model to learn from.

One common unsupervised FT technique is often referred to as continual pre-training or unstructured FT.

In this method, the FT process is viewed as a direct continuation of the pre-training phase. We start with a saved checkpoint of the original LLM and train it in a causal auto-regressive manner, i.e., predicting the actual pre-training is the learning rate. Usually, one would need a much lower learning rate when continuing the pre-training of the model to avoid catastrophic forgetting (Kirkpatrick et al., 2017).

It is well known that LLMs store vast amounts of knowledge during their pre-training phase (Zhou et al., 2023). So, it makes sense to continue this process in order to inject knowledge into the model. Hence, we use the unsupervised FT approach throughout this work and evaluate its efficacy in enhancing the model's capacity for learning new information.

3.3 Retrieval Augmented Generation

Retrieval augmented generation (RAG) (Lewis et al., 2020) is a technique that expands LLMs' capabilities, especially in knowledge-intensive tasks, by using external knowledge sources. While the original formulation involved additional training per task, it has since been demonstrated (Neelakantan et al., 2022) that a pre-trained embedding model can achieve improved performance with no additional training involved.

The idea is that given an auxiliary knowledge base and an input query, we use the RAG architecture to find documents within the knowledge base that resemble the input query. These documents are then added to the input query, thus giving the model further context about the subject of the query.

In practice, implementing the suggested architecture is quite straightforward: Given an auxiliary knowledge base $B\_Q$ and a pre-trained embedding model $M\_e$, we create a dense vector representation (embedding) per document $b \\in B\_Q$ and store these in a vector store. Upon receiving a new query $q$, we use its embedding, $M\_e(q)$, to retrieve $q$'s top-$K$ closest neighbors, $b\_q = {b\_k}^k$, according to dot-product ranking. We then update $q$ to be $\\bar{q} = b\_\\parallel q$, where $\\parallel$ denotes string concatenation. Finally, we return $\\mathcal{M}(\\bar{q})$ as the model's output.

* * *

* * *

isolation from its reasoning processes.

Current Events Task To further isolate LLMs' abilities to learn new knowledge, we created a task comprising multiple-choice questions about current events. This task includes multiple-choice questions about events that occurred after the cutoff of the various models' training data. Specifically, we focused on "current events" from the USA, in the time span of August-November 2023, that are included in the relevant Wikipedia indexes¹. This method enables us to mostly guarantee that the models have not been exposed to these facts, thus allowing us to directly test knowledge injection capabilities.

4.2 Data Collection and Preprocessing

To effectively evaluate the LLMs' performance on these knowledge-intensive tasks, a comprehensive auxiliary dataset was collected by scraping relevant articles per topic from Wikipedia. The rationale behind selecting Wikipedia as the primary source of knowledge is its broad coverage of relevant topics and its reliability as a repository of crowd-verified knowledge. All articles pertinent to the tasks were retrieved via the official Wikipedia API² by identifying the relevant central page per topic.

Subsequently, a rigorous cleaning process was utilized to transform the data from raw subsections to clean chunks. This step was done with the "wikitextractor" tool (Attardi, 2015). The division into small, clean (e.g., remove HTML, URLs, etc.) chunks was aimed at enhancing the evaluation of the LLMs' understanding across various knowledge domains and aiding the LLMs in the fine-tuning process.

4.3 Current Events Task Creation

After collecting the relevant chunks from Wikipedia, we created a new multiple-choice dataset with the help of GPT-4 (OpenAI, 2023). First, we removed any small chunks. For each remaining chunk in the corpus, GPT-4 was instructed to create four highly specific, high-quality multiple-choice questions with only one correct answer. By specific, we mean that the question can be answered without knowledge of which context the question refers to and with minimal ambiguity. Next, GPT-4 was asked to select the two most specific of the four. This was followed

[https://en.wikipedia.org/wiki/Category:2023\_events\_in\_the\_United](https://en.wikipedia.org/wiki/Category:2023_events_in_the_United) States\_by\_month [https://www.mediawiki.org/wikiAPI/Main\_page](https://www.mediawiki.org/wikiAPI/Main_page) by a manual evaluation and verification step. In total, this resulted in 910 new questions.

4.4 Paraphrases Generation

After creating the dataset, we utilized GPT-4 to generate augmentations of the dataset. We instructed GPT-4 to provide paraphrased versions of the input data that fully retain the information while being reworded. Each paraphrasing iteration was done with a different seed to ensure variety.

We selected 240 chunks at random for each task and created two paraphrases per chunk. These were set aside to be used as validation sets for hyperparameter tuning. For the current events dataset, we created ten paraphrases for each chunk used in the fine-tuning process described in Section 6.

5 Experiments and Results

Experimental Framework We used the popular LM-Evaluation-Harness (Gao et al., 2021) repository to evaluate the performance of LLMs on the selected knowledge-intensive tasks. LM-Evaluation-Harness is a robust benchmarking tool that currently serves as the industry standard for model evaluation and is the basis of the HuggingFace leaderboard³. Leveraging this platform ensured a standardized evaluation framework and allowed consistent comparison across models, methods, and datasets. More importantly, by using the industry standard for evaluation, we could avoid any differences stemming from prompt engineering and formatting issues and replicate the reported baseline results for each model.

Model Selection We chose three models for inference evaluation: Llama2-TB (Tournø et al., 2023), Mistral-TB (Jiang et al., 2023), and Orca2-TB (Mitra et al., 2023). The choice of these models was meant to represent the most popular open-source base models and an instruction-tuned model across various baseline capabilities. Additionally, we selected hge-large-en (Xiao et al., 2023) as the embedding model for the RAG component and used FAISS (Johnson et al., 2019) as its vector-store. This embedding model is currently the SOTA of open-source embedding models, according to the HuggingFace MTEB leaderboard⁴.

Configuration Variations Our evaluation included multiple configurations, with a grid-search

[https://huggingface.co/spaces/HuggingFaceH4/open\_lm\_leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_lm_leaderboard) [https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard) over them, to allow for more comprehensive benchmarking.

Firstly, we compared the baseline and fine-tuned models and their performance with the RAG component. Secondly, we explored the optimal number of text chunks to add to the context in RAG. Specifically, different values of $K \\in {0, \\dots, 5}$ were employed to analyze the impact on model performance. Finally, we explored 5-shot performance vs. 0-shot.

**Training Setup** We trained all of the models using the unsupervised training procedure described in Section 3.2. For each dataset, we divided the auxiliary knowledge base into equal chunks of size 250 by concatenating or splitting the original chunks based on their length. We also added two special tokens, $$ and $$, to demarcate the original chunks' beginnings and ends to preserve the documents' structure.

The models were trained using learning rates between $1 \\times 10^{-6}$ and $5 \\times 10^{-5}$, which were found through a hyperparameter search. All models were trained on 4 NVIDIA A-100 GPUs for a maximum of 5 epochs and a batch size of 64.

**Evaluation method** All evaluations were done by appending each of the multiple-choice options to the question, followed by passing the concatenation through the model to get a log probability score per option. The highest score was interpreted as the model's choice and used for accuracy calculation. More formally, this means that in Equation (1) we say that $\\mathcal{M}(q\_n) = c\_n$ if:

$$c\_n = \\arg \\max\_{l} \\left{\\mathcal{M}(q\_n\|a\_n^l), \\dots, \\mathcal{M}(q\_n\|a\_n^L)\\right},$$

where $\\mathcal{M}(q\_n\|a\_n^l) = \\log P\_{\\mathcal{M}}(q\_n\|a\_n^l)$.

**MMLU Results** For each task and model, we compared four approaches: using just the base model, RAG, FT, and finally combining FT and RAG by using the fine-tuned model as the generator. Furthermore, we tested the MMLU tasks using both 0-shot and 5-shot scenarios. The full results are shown in Table 1. An aggregation of the relative accuracy gain, i.e.,

$$(\\mathcal{L} _{\\mathcal{M}'Q} - \\mathcal{L}_{\\mathcal{M},Q}) / \\mathcal{L}\_{\\mathcal{M},Q}$$

where $\\mathcal{M}$ is the base model and $\\mathcal{M}'$ is the knowledge-injected model, is shown in Figure 2.

In all cases, RAG performed significantly better compared to the base models. Furthermore, using RAG with the base model as the generator was consistently better than only fine-tuning. In some cases, using the fine-tuned model instead of the base model as the generator in the RAG pipeline improved results even further. However, this is not consistent and thus demonstrates the inherent instability of fine-tuning. Additionally, we found that the 5-shot approach boosts the results by a small margin in most cases, with a similar trend being observed in all of the different approaches.

**Current Events Results** The evaluation on the current events task is shown in Table 2. RAG proves particularly effective due to the one-to-one correspondence between the questions and the auxiliary dataset (see Section 4.3). Fine-tuning is not competitive with RAG. However, fine-tuning with multiple paraphrases still provides a significant improvement over the baseline. We note that combining RAG with fine-tuning shows inferior performance compared to RAG alone.

It is worth noting that although the questions are based on information the models were not exposed to during training, the results of the base models surpass $\\frac{1}{4} = 0.25$. This can partially be explained by the models using reasoning and/or pre-existing knowledge when answering questions that are not independent of the past information. Some examples of this can be found in Appendix D.

**Fine-Tuning vs. RAG:** In the results of both the MMLU and current events tasks, a significant advantage for RAG over fine-tuning is evident. While fine-tuning improved results compared to the base model in most cases, it was not competitive with the RAG approach.

Several factors might contribute to this behavior. Firstly, RAG not only adds knowledge to a model but also incorporates context relevant to the question, a feature lacking in fine-tuning. Additionally, fine-tuning may impact other capabilities of the model due to a degree of catastrophic forgetting. Finally, it’s plausible that unsupervised fine-tuned models might benefit from further alignment through supervised or RL-based fine-tuning, as evidenced by the vastly improved performance of Orca2 over the base Llama2.

6 The Importance of Repetition

Unlike the other tasks, where the model has been exposed to aspects related to the topic during pre-training, current events includes new information. In this case, standard regular fine-tuning not only did not improve the performance of Llama2 but also significantly degraded it. To improve the fine-tuning results, we explored augmentation of the data using paraphrases.

Data Augmentation Data augmentation is a well-established method for enhancing the performance of language models and has been surveyed extensively (Shorten et al., 2021). Using generative models for augmentations has also been used successfully to improve classification models in the past (Sharma et al., 2022). An example of data augmentation using paraphrasing can be found in Appendix C.

Monotonic Improvement This approach resulted in notable improvements in our results, showcasing a direct correlation between the number of paraphrases utilized and the model’s accuracy. Our experimentation revealed a compelling trend. For all models tested, the accuracy was a monotonically increasing function of the number of paraphrases used (visualized in Appendix A, Figure 4). This observation strongly suggests the positive impact of paraphrase augmentation, yielding information repetition, on the model’s ability to comprehend and generalize new knowledge from limited data.

Learning New Information In Appendix A, Figure 3, we can see an interesting phenomenon observed throughout our experiments. After each epoch, i.e., completing another iteration over the entire dataset, the training loss drops significantly. This is consistent with knowles about LLMs memorizing the data during training and overfitting (Tirumala et al., 2022).

Our hypothesis is as follows:

In order to teach pre-trained LLMs new knowledge, the knowledge must be repeated in numerous ways.

This is well known for LLM pre-training (Kandal pal et al., 2023), and we see in this case that this holds for fine-tuning as well. The rationale for this hypothesis is that mere memorization of sentences does not entail knowledge of their content, as was already shown in (Berglund et al., 2023). By providing the information in numerous forms (like the data augmentation process we used), the various relationships in the data (e.g., a ⇒ b, b ⇒ c) stand a higher chance of appearing naturally. We believe this can potentially both increase $ \\mathcal{L}\_{\\mathcal{M},\\mathcal{Q}} $ in general, as well as ameliorate Berglund et al.’s Reversal Curse. While promising, this result still warrants further research.

7 Conclusion and Future Work

Large language models possess vast amounts of knowledge on various topics. In this work, we tested their capability to adapt to new knowledge; both specialized and completely unseen. This is among the first studies to compare two prominent approaches in this domain, namely fine-tuning and retrieval augmented generation. While fine-tuning can be useful for many use-cases, we found that RAG is a more reliable choice for knowledge injection.

Some aspects of this work still warrant further research. For example, we focused on unsupervised training as our primary fine-tuning method, as opposed to instruction-tuning or RL-based methods. Researching combinations of various techniques, with diverse auxiliary knowledge bases, may yield improved results. This approach, combined with our hypothesis from Section 6, could further enhance our understanding of knowledge injection via FT.

While we believe that this work further enhances our understanding of knowledge in LLMs, there is a lot more work to be done in this field. Specifically, more research is required regarding the question of knowledge representation in LLMs, especially from a theoretical perspective.

Finally, further efforts are needed to measure knowledge in LLMs. While we employed an empirical approach as described in Equation (2), it is important to explore other definitions and perspectives on knowledge as well, and extend upon this work.

8 Limitations

As in all machine learning applications, the choice of hyperparameters significantly impacts the results. We therefore strongly recommend optimiz-

* * *

* * *

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kruitcher, Mike Lewis, Wen-tau Yih, Tim Rocktaschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. _Advances in Neural Information Processing Systems_, 33:9459-9474.

Weijie Liu, Peng Zhou, Zhehao Zhuang, Wenzu Yih, Tim Rocktaschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. _Advances in Neural Information Processing Systems_, 33:9459-9474.

Yun Luo, Zhien Yang, Fandong Meng, Yafu Li, Jie Zhou, and Yue Yue. 2023. An empirical study of catastrophic forgetting in large language models during continual fine-tuning. _arxiv preprint arXiv:2308.08747_.

Sewon Min, Mike Lewis, Luke Zettlemoyer, and Hannah Hajishirzi. 2021. Metacit: Learning to learn in context. _arxiv preprint arXii:2110.15943_.

Swaroop Mishra, Daniel Khasabi, Chitta Baral, and Hannah Hajishirzi. 2021. Cross-task generalization via natural language crowdsourcing instructions. _arxiv preprint arXiv:2104.08773_.

Indramid Mitra, Luciano Del Corro, Shweti Mahajan, Andres Codas, Clarisse Simos, Sahaj Agrawal, Xuxi Chen, Anastasia Razadibadee, Erick Jones, Kri Agrawal, Orca 2. Teaching small language models how to reason. _arxiv preprint arXiii:1110.145_.

Arvind Neelakantan, Tao Xu, Raul Peri, Alec Radford, Jesse Akiyu, Tian Tweok, Quing Wuhan, Nikolas A, Tezek, Jong Wook Kim, Chris Hallay, Johanes Heideck, Pranav Shym, Boris Power, Tyna Eloundou Nekoul, Girish Sastry, Gretchen Krueger, David P. Schnur, Felipe Petroski Such, Kenny Sai-Kiu Hsu, Madeleine Thompson, Tabarak Khan, Toki Sherbekov, Joane Wang, Peter Welter, and Lilian Weing. 2022. Text and code embeddings by contrastive pre-training. _Arxiv_, abs/2201.10005.

Ha-Thanh Nguyen. 2023. A brief report on lawgpt 1.0: A virtual legal assistant based on gpt-3. _arxiv preprint arXiv:2302.05729_.

Harsha Nori, Nicholas King, Scott Mayer McKinney, Dean Carignan, and Eric Horwitz. 2023. Capabilities of gpt-4 on medical challenge problems. _Arxiv_, abs/2303.1375.

OpenAI. 2023. Gpt-4 technical report. _Arxiv_, abs/2303.08774.

Long Ouyang, Jeffrey Wu, Xu Xiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agawal, Katarin Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback. _Advances in Neural Information Processing Systems_, 35:27730-27744.

Fabio Petroni, Tim Rocktaschel, Patrick Lewis, Anton Bakkinh, Yuxiang Wu, Alexander H Miller, and Sebastian Riedel. 2019. Language models as knowledge bases? _arxiv preprint arXiv:1909.01066_.

Alce Reaford, Jeffrey Wiu, Reunion Diel, David Lauan, Dario Amodel, Ilya Sauskwer, et al. 2019. Language models are unsupervised multitask learners. _OpenAI blog_, 18:9).

Rafael Rafikov, Archi Sharma, Eric Mitchell, Stefano Ernson, Christopher D Manning, and Chelsea Finn. 2023. Direct preference optimization. Your language model is secretly a reward model. _arxiv preprint arXiv:2305.18290_.

Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. 2021. Winninggrade. An adversarial winograd schema challenge at scale. _Communications of the ACM, 64(9)_-99-106.

John Schalmman, Filip Wolski, Prafulla Dhiariwal, Alce Reaford, and Oleg Kinow. 2017. Proximal policy optimization analysis. _arxiv preprint arXiv:1707.06347_.

Saket Sharma, Aviral Joshi, Namrata Mukhija, Yiyun Zhao, Hanor Bhathena, Praeke Singh, Sashank Santhanam, and Pritan Bhyang. 2022. Systematic review of data augmentation using paraphrasing on named entity recognition. In _NerlPS 2022 Workshop on Synthetic Data for Empowering ML Research_.

Connor Shorten, Taigi M. Khosghoftaar, and Borko Furht. 2021. Text data augmentation for deep learning. _Journal of Big Data_, 8.

Karan Singenh, Sheshofez Aziri, Tuo T苏, Sara Mahdavi, Jaswei Wuj, Hong Wong, Nathan Scales, Ajay Tanwani, Heather Cole-Lew, Stephen Pfohl, et al. 2023a. Large language models encode clinical knowledge. _Nature_, 620(7972):172-180.

Karan Singeh, Tauo Tujur J Gotwei, Rory Sayres, Ellery Wulczyn, Le Hou, Kevin Clark, Stephen Pfohl, Heather Cole-Lew, Darlene Neal, et al. 2023b. Towards expert-level medical question answering with large language models. _arxiv preprint arXiv:2305.09617_.

Aurohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Sheeb, Abubaker Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta, Adria Garriga-Alonse, et al. 2022. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. _arxiv preprint arXiv:2206.04915_.

Yiming Tan, Dehai Min, Yu Li, Wenbo Li, Nan Hu, Yongrui Chen, and Gulin Qi. 2023. Can chatgpt replace traditional kqna models' an in-depth analysis of the question answering performance of the gmt lim family. In _International Semantic Web Conference_, pages 348-367. Springer.

* * *

Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guesrin, Percy Liang, and Tatsunori B Hashimoto. 2023. Alpaca: A strong, replicable instruction-following model. Stanford Center for Research on Foundation Models. [https://lcfrm.stanford.edu/2023/01/13/paca.html](https://lcfrm.stanford.edu/2023/01/13/paca.html), 3(6)7.

Kushal Triumala, Aram H. Markosyan, Luke Zettle-moyer, and Armen Aghajyanan. 2022. Memorization without overfitting: Analyzing the training dynamics of large language models. arXiv preprint arXiv:2307.09288.

Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Ajad Almahari, Yasmine Babaei, Nikolay Bashykov, Soumya Bara, Prajwal Bhargava, Shiruti Bhassele, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288.

Lewis Tunstall, Edward Beeching, Nathan Lambert, Nazneen Rajani, Kashif Rasul, Younes Beltka, Shengyi Huang, Leandro von Werra, Clémentine Fourrier, Nathan Habib, et al. 2023. Zephyr: Direct distillation of Im alignment. arXiv preprint arXiv:2310.16944.

Cunxiang Wang, Xiaoze Liu, Yuanhao Yue, Xiangru Tang, Tianhang Zhang, Cheng Jiayang, Yunzhi Yao, Wenyang Gao, Xuming Hu, Zhen Qi, et al. 2023. Survey on factuality in large language models: Knowledge retrieval and domain-specificity. arXiv preprint arXiv:2310.107521.

Ruize Wang, Dayu Tan, Nan Duan, Zhonggyu Wei, Xuuning Huang, Guihong Cao, Daxin Jiang, Ming Zhou, et al. 2020. K-adapter: Infusing knowledge into pre-trained models with adapters. arXiv preprint arXiv:2002.01808.

Yizhong Wang, Swaroop Mishra, Pegah Alipoor-molabashi, Yeginch Kordi, Amireza Mirzeai, Anjana Arunkumar, Arjun Ashok, Arut Selvan Dhanasekaran, Atharva Naik, David Stap, et al. 2022. Super-natural instructions: Generalization via declarative instructions on 1600+ nlp tasks. arXiv preprint arXiv:2204.07075.

Chaoyi Wu, Xiaoman Zhang, Ya Zhang, Yanfeng Wang, and Weidi Xie. 2023a. Pmc-llama: Further fine-tuning lama on medical papers. arXiv preprint arXiv:2304.14454.

Shijie Wu, Ozan Irsoy, Steven Lu, Vadium Dabravolski, Mark Dolgar, Sebastian Gehn, Prabhanjan Kambadur, David Reinklage and Cideon Mann. 2023b. Bloomberggt: A large language model for finance. arXiv preprint arXiv:2303.17564.

Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas Muenighoff. 2023. C-pack: Packaged resources to advance general Chinese embedding. Preprint, arXiv:2309.07597.

Hongyang Yang, Xiao-Yang Liu, and Christina Dan Wang. 2023. Finget: Open-source financial large language models. arXiv preprint arXiv:2306.06031.

Wenhao Yu, Chengquang Zhu, Zaitang Li, Zhiting Hu, Qingyun Wang, Heng Ji, and Meng Jiang. 2022. A survey of knowledge-enhanced text generation. ACM Computing Surveys, 54(11)s)-1-38.

Chunting Zhou, Pengfei Lin, Pusin Xu, Srini Iyer, Jiao Sun, Yining Mao, Xueze Ma, Avia Erfut, Ping Yu, Lili Yu, et al. 2023. Limar: Less is more for alignment. arXiv preprint arXiv:2305.11206.

A The Importance of Repetition Figures

Figure 3: Training loss over time for Mistral-7B.

Effect of Paraphrases on Accuracy

Figure 4: Model accuracy on the current events task as a function of the number of paraphrases.

B RAG Ablation Study

As mentioned in Section 5, we compared various values of $K \\in {0, \\dots, 5}$, shown in Table 3. We were unable to find an optimal value of $K$ per model, per 0/5-shot, or per task. In fact, other than Anatomy that worked well with $K = 2$ consistently, there seems to be no patterns that aid in predicting the performance per $K$, unlike the results presented in (Lewis et al., 2020) for other setups. Moreover, the gap between the best and worst performing $K$s can be large.

* * *

Unfortunately, we must conclude that this additional hyperparameter is unstable. This is a downside of using RAG in practice, and the choice of K cannot be ignored.

C Paraphrase Examples

Below is the prompt we used to generate paraphrases with GPT-4:

Your task is to paraphrase a text paragraph. The paragraph is given below.

Make sure to keep the same meaning but change the wording. Do not change any factual information.

Try to keep roughly the same length of the original text.

Give NUM \_ PARAPHRASES different paraphrases for each text.

These paraphrases should be as different from each other as possible.

Return a JSON formatted string with one key, called 'paraphrases', and a list of paraphrases.

Input paragraph:

Below are some examples. First, an example taken from the following Wikipedia page: "51st International Emmy Awards".

Paraphrase I

The fifty-first edition of the International Emmy Awards Competition accepted submissions across all categories from December 7, 2022, until the closing date of February 16, 2023.

Paraphrase II

The International Emmy Awards Competition, now in its 51st year, accepted submissions across all categories starting from December 7, 2022, until the deadline on February 16, 2023.

Paraphrase III

The fifty-first edition of the International Emmy Awards Competition accepted submissions across all categories from December 7, 2022, until the closing date of February 16, 2023.

The next example was taken from the following Wikipedia page: "2023 Indianapolis mayoral election".

Paraphrase I The mayoral election in Indianapolis took place on November 7, 2023, with preliminary elections occurring on May 2. The sitting mayor, Democrat Joe Hogsett, successfully ran for a third term. Both Hogsett and his Republican opponent, Jefferson Shreve, moved on to the main election.

Paraphrase II On November 7, 2023, citizens of Indianapolis cast their votes to elect their Mayor, following primary elections on May 2. Joe Hogsett, the Democrat already in office, won his bid for a third term. Hogsett and the Republican candidate, Jefferson Shreve, were the two contenders in the final electoral round.

Paraphrase III The mayoral election in Indianapolis took place on the 7th of November, 2023, following primary elections that occurred on the 2nd of May. Joe Hogsett, the incumbent Democrat, successfully ran for a third term. Both Hogsett and his Republican challenger, Jefferson Shreve, made it through to the final round of the election.

D Current Events Existing Knowledge Examples

To give a better understanding of how a model might be able to answer questions about new information, with better than random success, we present three possible scenarios as examples. These scenarios show how models with stronger reasoning skills can infer the correct answer even for unseen information.

The first scenario involves questions about previously unseen information, where basic reasoning abilities allow a model to make an educated guess.

Question: What was a key issue that led to the 2023 United Auto Workers strike?

Answers:

* * *

Task Model # Retrieved documents (k)
1 2 3 4 5

Anatomy (0-shot) Mistral 7B 0.615 **0.681** 0.630 0.644 0.622
Llama2 7B 0.444 **0.489** 0.467 0.474 0.481
Orca2 7B 0.607 **0.637** 0.600 0.585 **0.637**

Anatomy (5-shot) Mistral 7B 0.659 0.667 0.659 **0.681** 0.674
Llama2 7B 0.496 **0.563** 0.541 0.526 0.526
Orca2 7B 0.630 **0.659** 0.600 0.600 0.600

Astronomy (0-shot) Mistral 7B 0.651 **0.678** **0.678** 0.664 0.664
Llama2 7B 0.447 0.434 0.447 0.434 **0.467**
Orca2 7B 0.711 0.730 0.730 **0.750** 0.730

Astronomy (5-shot) Mistral 7B 0.704 0.684 0.658 0.684 **0.724**
Llama2 7B 0.461 0.447 **0.474** 0.428 0.454
Orca2 7B 0.730 0.737 0.750 0.743 **0.763**

Biology (0-shot) Mistral 7B 0.736 0.722 **0.757** 0.743 0.736
Llama2 7B 0.438 0.472 **0.493** 0.479 0.472
Orca2 7B **0.639** 0.618 **0.639** 0.625 **0.639**

Biology (5-shot) Mistral 7B 0.722 **0.778** **0.778** 0.771 0.743
Llama2 7B 0.500 **0.521** 0.507 0.465 0.472
Orca2 7B 0.625 0.639 0.625 **0.660** **0.660**

Chemistry (0-shot) Mistral 7B 0.450 0.470 0.470 **0.500** 0.470
Llama2 7B 0.320 0.320 0.300 **0.380** 0.360
Orca2 7B 0.370 0.420 0.400 0.410 **0.440**

Chemistry (5-shot) Mistral 7B 0.540 0.490 0.500 0.510 0.470
Llama2 7B 0.280 0.320 0.340 0.340 **0.380**
Orca2 7B 0.390 0.430 0.400 0.430 **0.470**

Prehistory (0-shot) Mistral 7B 0.728 0.725 **0.750** 0.735 0.728
Llama2 7B **0.481** 0.460 0.457 0.457 0.429
Orca2 7B 0.648 0.645 0.660 0.670 **0.679**

Prehistory (5-shot) Mistral 7B 0.710 0.750 0.759 0.756 **0.762**
Llama2 7B 0.512 0.485 0.525 0.519 **0.531**
Orca2 7B 0.660 0.688 0.685 **0.698** 0.688

In this case it is easy to guess that the third option is the most likely, even without knowledge of this specific strike.

A second scenario involves questions where prior knowledge about a topic may aid a model in answering.

Question: What environmental concern was raised by some scientists as a result of the 2023 Hawaii wildfires?

* * *

Even with some knowledge about floods and Answers: their statistical properties, it would be very difficult to guess that this specific meteorologist would call

1.Rising temperatures.
the flood a ‘200-year event’. This is especially true

2.Melting ice caps.
if the model was not exposed to information about Charred soils running off into the 3. the details of the flood. shoreline.

4.Increased air pollution.
In this case, knowing the geography of Hawaii, as well as immediate effects of wildfires, enables a model to give the first two options a lower likelihood. This process of elimination increases the probability of choosing one of the remaining options (the third option is the correct answer).

A third scenario arises due to the automatic question generation process, some questions strongly rely on pre-existing knowledge.

What event in 2021 was Question: compared to the September 2023 New York floods?

Answers:

1.Hurricane Katrina.
2.Hurricane Ida.
3.Hurricane Sandy.
4.Hurricane Harvey.
Since only one of these events occurred in 2021 (Hurricane Ida), and all the models tested have been exposed to events from 2021 during pre- training, this question can potentially be answered without using additional current information.

Finally, to demonstrate why it is reasonable to assume that models cannot generally answer questions about new information, with better than random success, look at the following example:

How did Matthew Belk, a Question: National Weather Service meteorologist, describe the September 2023 northeast- ern U.S. floods?

Answers:

1.50-year event.
2.100-year event.
3.200-year event.
4.500-year event.
```

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="advanced-rag-retrieval-cross-encoders-reranking-towards-data.md">
<details>
<summary>Advanced RAG Retrieval: Cross-Encoders & Reranking</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/>

# Advanced RAG Retrieval: Cross-Encoders & Reranking

A deep-dive and practical guide to cross-encoders, advanced techniques, and why your retrieval pipeline deserves a second pass.

[Ian Ho](https://towardsdatascience.com/author/ianhojy/)

Apr 11, 2026

28 min read

https://towardsdatascience.com/wp-content/uploads/2026/04/bi-encoder-vs-cross-encoder-scaled-1.jpg
Image generated by Author using Gemini Nano Banana

Semantic search, or embedding-based retrieval, has been a key component within many AI applications. Yet, a surprising number of applications I’ve seen still don’t do reranking, despite the relative ease of implementation.

If you’ve ever built a RAG pipeline and thought “the results are _okay_ but not _great_”, the solution isn’t always to choose a better embedding model. Instead, you should consider including a reranking step, and **cross-encoders** are probably your best bet.

**This article covers what cross-encoders are, why they’re so good at reranking, how to fine-tune them on your own data, and some ideas for pushing them even further.**

All the code is available at [https://github.com/ianhohoho/cross-encoder-and-reranking-demo](https://github.com/ianhohoho/cross-encoder-and-reranking-demo).

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
- Pinecone has built-in reranking with hosted models, describing it as [“a two-stage vector retrieval process to improve the quality of results”](https://docs.pinecone.io/guides/search/rerank-results). One of the multilingual models they offer is `bge-reranker-v2-m3` , for which the HuggingFace card can be found [here](https://huggingface.co/BAAI/bge-reranker-v2-m3).
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

### How Cross-Encoders Are Trained

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

### Why Cross-Attention Matters: The Technical Deep Dive

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

Now attention terms​​ exists. In a very approximate manner, the query token for “cheap” would attend to the document token for “$500”, and the model learns through training that this combination means “not relevant.” This cross-attention happens at every layer, building increasingly abstract relationships.

**Multi-head attention** makes this even more powerful. Each attention head has its own weight matrices​, so different heads learn to detect different types of relationships simultaneously:

- One head might learn **lexical matching** same or similar words
- Another might learn **semantic equivalence** — “cheap” ↔ “budget”
- Another might learn **contradiction detection** — “without sugar” vs “contains sugar”
- Another might learn **entity matching** — the same person or place referenced differently

At the end of it, the outputs of all heads are concatenated and projected:

https://cdn-images-1.medium.com/max/1200/1*eLegzX7rN9oLSToQgvUxtA.png

With multiple heads across multiple players, the model has many independent heads examining query-document interaction at every level of abstraction. Theoretically, that’s why cross-encoders are so much more expressive than bi-encoders.

But of course the tradeoff is then compute: attention costs more and nothing is precomputed.

## Enough theory. Let’s look at actual code.

I’ve built a companion repo with eight example .py files that progress from basic implementation to distillation pipelines and full latency-profiled ColBERT implementations.

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

### Picking the Right Model

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

- TinyBERT is the odd one out , which puts document 5 (irrelevant) in 5th place while the others push it to the bottom.

Generally speaking:

- **TinyBERT-L2-v2**: extremely fast but least accurate — use for low-latency or edge scenarios.
- **MiniLM-L6-v2**: best balance of speed and quality — use as the default for most reranking tasks.
- **MiniLM-L12-v2**: slightly more accurate but slower — use when maximizing ranking quality matters.
- **electra-base**: (older) and larger and slower with no clear advantage — generally not recommended over MiniLM.

### Fine-Tuning: Making the Model Understand Your Domain

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

Accuracy increasing from 30% to 95% means that the original base model was somehow worse than random on legal documents. After fine-tuning on just 72 training pairs , 12 legal topics with 6 pairs each, the model gets 19 out of 20 right. And notice that unseen topics went from 4/10 to 10/10. In a sense it learnt the domain of legal reasoning, not just the training examples.

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

### Semantic Query Caching

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

Let’s trace through the math. The matrix multiply \`(9 × 384) × (384 × 30)\` produces a \`9 × 30\` similarity matrix. Each cell tells you how similar one query token is to one document token. Then \`.max(dim=1)\` takes the best document match for each query token , 9 values. Then \`.sum()\` adds them up into one score.

The query token “quantum” scans all 30 document tokens and finds its best match , probably something like “qubits” with similarity ~0.85. The query token “speedup” finds something like “faster” at ~0.7. Meanwhile, filler tokens like “how” and “do” match weakly against everything (~0.1). Sum those 9 maxima and you get a score like 9.93, just as an example.

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

## Where Does This Leave Us?

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

Written By

Ian Ho

[See all from Ian Ho](https://towardsdatascience.com/author/ianhojy/)

[Deep Dives](https://towardsdatascience.com/tag/deep-dives/), [Llm](https://towardsdatascience.com/tag/llm/), [Machine Learning](https://towardsdatascience.com/tag/machine-learning/), [Rag](https://towardsdatascience.com/tag/rag/), [reranking](https://towardsdatascience.com/tag/reranking/)

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

#### Knowledge Graph Retrieval ( [opens in new tabGraphRAG](https://neo4j.com/blog/genai/what-is-graphrag/))

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

- [llm](https://neo4j.com/blog/tag/llm/)
- [rag](https://neo4j.com/blog/tag/rag/)

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

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="cbr-rag-case-based-reasoning-for-retrieval-augmented-generat.md">
<details>
<summary>CBR-RAG: Case-Based Reasoning for Retrieval Augmented Generation in LLMs for Legal Question Answering † † thanks: This research is funded by SFC International Science Partnerships Fund.</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/abs/2404.04302>

# CBR-RAG: Case-Based Reasoning for Retrieval Augmented Generation in LLMs for Legal Question Answering † † thanks: This research is funded by SFC International Science Partnerships Fund.

## Abstract

Retrieval-Augmented Generation (RAG) enhances Large Language Model (LLM) output by providing prior knowledge as context to input. This is beneficial for knowledge-intensive and expert reliant tasks, including legal question-answering, which require evidence to validate generated text outputs. We highlight that Case-Based Reasoning (CBR) presents key opportunities to structure retrieval as part of the RAG process in an LLM. We introduce CBR-RAG, where CBR cycle’s initial retrieval stage, its indexing vocabulary, and similarity knowledge containers are used to enhance LLM queries with contextually relevant cases. This integration augments the original LLM query, providing a richer prompt. We present an evaluation of CBR-RAG, and examine different representations (i.e., general and domain-specific embeddings) and methods of comparison (i.e., inter, intra and hybrid similarity) on the task of legal question-answering. Our results indicate that the context provided by CBR’s case reuse enforces similarity between relevant components of the questions and the evidence base leading to significant improvements in the quality of generated answers.

## 1 Introduction

Retrieval-Augmented Generation (RAG) enhances the performance of large language models (LLMs) on knowledge-intensive NLP tasks by combining the strengths of pre-trained parametric (language models with learned parameters) and non-parametric (external knowledge resources e.g., Wikipedia) memories. This hybrid approach not only sets new benchmarks in open-domain question answering by generating more accurate, specific, and factually correct responses but also addresses critical challenges in the field such as the difficulty in updating stored knowledge and providing provenance for generated outputs. For example, in the context of legal question-answering, RAG-based systems can retrieve publicly available legislation documents from open knowledge bases to provide context for user queries. However, such a system would require output that could be validated, and moderation of content generated by LLMs has been highlighted as a critical concern.

Case-Based Reasoning (CBR) presents an excellent opportunity here, as previous solutions form the basis of a knowledge-base which can be evidenced in best practice or regulations. CBR can enhance the retrieval process in RAG models by organising the non-parametric memory in a way that cases (knowledge entries or past experiences) are more effectively matched to queries. Previous work on ensemble CBR-neural systems has also highlighted the benefits of CBR integration, demonstrating improvements in factual correctness over purely neural methods. Accordingly, in this work we present three contributions.

*   Firstly, we formalise the role of the CBR methodology to form context for RAG systems.
*   Secondly, we provide an empirical comparison of different retrieval methods for RAG, examining different representations (i.e., general and domain-specific embeddings) and methods of comparison (i.e., inter, intra and hybrid similarity).
*   Finally, we present these contributions in the context of the legal domain, and provide results for a generative legal question-answering (QA) application (Reproducible code is available: [https://github.com/rgu-iit-bt/cbr-for-legal-rag](https://github.com/rgu-iit-bt/cbr-for-legal-rag)). Our results highlight the opportunities of CBR-RAG systems for knowledge-reliant generative tasks.

This paper is structured as follows. In Section 2 we describe influential work targeting the legal domain from CBR and LLM literature. In Section 3, we formalise CBR-RAG and its application to legal QA, while in Section 4 we detail the different methods for creating and comparing embeddings to perform case retrieval. In Section 5 we describe the different encoders used to create embeddings. Finally, in Section 6 we discuss the methodology and results of our evaluation, followed by conclusions in Section 7.

## 2 Related Work

CBR boasts a long-standing history in the legal domain, with initial efforts concentrating on extracting features to index law cases effectively. These features, referred to as ‘factors’, are pivotal in systems like HYPO, which employ fact-oriented representations applied to trade secret law and extended to legal tutoring with the CATO system. More generally with Textual CBR, a key focus has been on extracting features for case comparison, using methods that range from decision trees, as exemplified by the SMILE system in creating indexing vocabularies for legal case retrieval, to association rules for case representation. Much of this has now been advanced by the adoption of neural transformations of input text through transformer-style embeddings with LLMs.

The application of LLMs presents an interesting approach in addressing challenges within the legal domain. LLMs use language understanding capabilities to interact with users, enabling extraction of key elements from legal documents, and present information in an understandable manner to enhance decision-making processes. For this reason, GPT-based and BERT-based transformer models are popular for LegalAI. However their black-box nature and tendency to hallucinate and lack of factual faithfulness present significant challenges for deployment. Retrieval-Augmented Generation (RAG) systems address this by presenting the LLM with factual data to generate responses, employing a variety of sophisticated fact identifying mechanisms. However currently such retrieval methods in RAG do not make use of CBR’s potential for varying matching strategies across different segments of the content being matched. Here we are reminded of research in CBR involving the integration with IR systems, specifically where CBR has been effectively used to retrieve ‘most on-point’ cases to guide the search and browse of vast IR collections. Our work draws inspiration from these integrative approaches, applying the principles of CBR to improve contextual understanding within LLMs.

LLMs are typically pre-trained on general text and subsequently fine-tuned on legal texts to learn domain-specific representations. Obtaining sufficiently large data sets for LLM training poses a significant challenge. For example, pre-trained LLMs may be fine-tuned using the LEDGAR dataset for legal text classification downstream tasks or on extensive corpora like the Harvard Law case corpus ([https://case.law/](https://case.law/)) using masked-language modelling or next-sentence prediction techniques. Thereafter tested on other legal downstream tasks, such as those found in the CaseHOLD dataset, which include tasks related to Overruling, Terms of Service, and CaseHOLD itself. We observe that there remains a notable scarcity of LLMs specifically applied to legal question answering tasks. This is likely because existing legal QA datasets are mostly small, manually curated datasets (for example, the rule-qa task in the LegalBench collection is formed from 50 question-answer pairs). However the recent release of the Open Australian Legal Question-Answering (ALQA) dataset ([https://huggingface.co/datasets/umarbutler/open-australian-legal-qa](https://huggingface.co/datasets/umarbutler/open-australian-legal-qa)), comprising over 2,100 question-answer-snippet triplets (synthesised by GPT-4 from the Open Australian Legal Corpus), presents an opportunity for LLMs to expand to legal QA.

## 3 CBR-RAG: Using CBR to form context for LLMs

In CBR-RAG, we integrate the initial retrieve-only stage of the CBR cycle with its indexing vocabulary and similarity knowledge containers to enable the retrieval of cases that serve as context for querying an LLM. Consequently, the original LLM query is augmented with content retrieved via CBR, creating a contextually enriched prompt for the LLM.

Figure 1 illustrates a high-level architecture of a generative model for Question-Answering systems, highlighting the integration of CBR within it. Here we denote the generative LLM model as, $G$, and the prompt, $P$, used to generate the response as a tuple, $p=(\mathcal{Q},\mathcal{C})$, where $\mathcal{Q}$ is the question reflecting the user’s query, and, $\mathcal{C}$, is the context text with relevant details to guide the response generation. The response generated by the model for the query, $\mathcal{Q}$, is denoted as the answer, $A$.

![Figure 1: CBR-RAG](extracted/5517515/images/CBR-RAG.jpg)

### 3.1 Casebase

We used the Australian Open Legal QA (ALQA) dataset to create the casebase. The dataset is formed of 2,124 LLM-generated question-answer pairs from the Australian Open Legal Corpus dataset. Each QA pair is corroborated by a supporting textual snippet from a legal document within the corpus for factual validation. An example case about the ‘interpretation of reasonable grounds in searches without a warrant’ appears in Table 1. Here the support text provides the context in which the question should be answered. The bold text further highlights examples of named entities that might usefully be captured separately for case comparison purposes.

**Table 1: Examples Legal Q&A case**

| Component | Description |
| --- | --- |
| Case Name | Smith v The State of New South Wales (2015) |
| Question | How did the case of Smith v The State of New South Wales (2015) clarify the interpretation of ‘reasonable grounds’ for conducting a search without a warrant? |
| Support | In [Case Name: Smith v The State of NSW (2015)], the plaintiff [Action: was searched without a warrant] [Location: near a known drug trafficking area] based on the plaintiff’s nervous demeanor and presence in the area, but [Outcome: no drugs were found]. The legality of the search was contested, focusing on [Legal Concept: whether ‘reasonable grounds’ existed]. |
| Answer | The case ruled ‘reasonable grounds’ require clear, specific facts of criminal activity, not just location or behavior. |

![Figure 2: Ten most frequent legal acts in the casebase are listed on the left, and the legal act frequency distribution appears on the right.](extracted/5517515/images/case_act_frequency_distribution.png)

Figure 2 provides a frequency distributions of the legal acts identified in the casebase with the most frequently referenced legal acts in the dataset listed in the table (extracted using the prompt in Table 3). The most frequently mentioned act is the ‘Federal Court Rules’ out of 785 unique legal acts. Within the dataset, 1,183 (57%) cases were found to have no reference to legal acts, while only 44 acts appeared in more than 1 case. Accordingly, relying solely on legal acts for indexing would not be suitable for this casebase. Instead, it presents an ideal opportunity for experimentation with neural embeddings. These embeddings form the indexing vocabulary, with weighted similarity contributing to the similarity knowledge.

## 4 Representation and Similarity

We formalise our retrieval and representation methods. Let’s denote the casebase as a collection of cases $C=\{c_{1},c_{2},\ldots,c_{n}\}$ containing question and answer legal cases. Each case $c$, in the context of RAG is formalised as a tuple,

$$c=\;<Q,S,E,A>$$

where $Q$ represents a question, $A$ represents the answer, $S$ represents the support for a given answer from an evidence base, and $E$ represents a set of entities extracted from $S$. This case representation underpins RAG in its use of $S$. Typical CBR for question answering would be composed mainly of problem-solution components (i.e., question and answer respectively together with any lessons learnt), structuring cases as problem-solution-support enhances answer generation for the LLM by providing factually accurate context. Furthermore, while only the most relevant component of a document is extracted as the support text, the link to the full document is available in the original ALQA corpus.

### 4.1 Representation

Initially, in textual form, each part is represented by neural embeddings. For diverse retrieval scenarios, we use a dual embedding form for $Q$ to enable matching it with not only other questions but where necessary matching it to the supporting text or the entities as follows:

*   Intra Embeddings, $f(\cdot)$, optimised for attribute matching. These embeddings facilitate attribute-to-attribute comparisons where local similarities can be computed between the same types of attributes (e.g., questions with questions).
*   Inter Embeddings, $g(\cdot)$, designed for information retrieval (IR) scenarios. These embeddings allow for matching that is not restricted to like attributes, enabling inter-attribute similarity assessment. This approach is particularly useful in situations where a question may be relevant for comparison to the support text or the entities.

A representation using intra-embedding is useful for tasks like semantic textual similarity that focus on finding sentences with closely related meanings, even if phrased differently. For example, a sentence like ‘The judge dismissed the case due to lack of evidence.’ would find a semantically similar counterpart in ‘The court threw out the lawsuit because there was insufficient proof’. Conversely, an inter-embedding representation is suited for tasks aimed at searching for documents relevant to a query. For example, a legal query on ‘copyright infringement in digital media’ may yield cases with outcomes such as rulings on unauthorised content distribution or streaming without permission. These highlight the distinction between representations needed for ascertaining semantic similarity with intra-embeddings ($f(\cdot)$), and finding relevant content with inter-embeddings ($g(\cdot)$).

The dual-embedding case representation, accommodating both forms of retrieval tasks, is given by:

$$c=\;<f(Q),g(Q),g(S),g(E),A>$$

Similarly, the prompt can be expressed using the inter embedding as follows (Note: In our notation, we employ a calligraphic font for the prompt components ($f(\mathcal{Q}),g(\mathcal{Q}),\mathcal{C}$) to distinguish them from those of cases. Despite this stylistic difference, it is important to understand that both prompts and cases utilise similar embedding representations.):

$$p=\;<f(\mathcal{Q}),g(\mathcal{Q}),\mathcal{C}>$$

### 4.2 Case Retrieval

We use case retrieval to augment the context part of a prompt, $p$, given its query, $\mathcal{Q}$. Accordingly, there are three comparison strategies for case retrieval: intra-, inter-, and hybrid-embedding based retrieval.

Intra-embedding retrieval involves matching on the basis of embeddings obtained from function $f(\cdot)$. Here $f(\mathcal{Q})$ which represents the embeddings from the prompt’s query is matched to query parts of the cases in the casebase. The best matching case identified from intra-embedding retrieval is defined by:

$$\beta_{k}=\underset{c_{i}\in C,\,k}{\text{top-k}}\,\text{Sim}(f(\mathcal{Q}),f (Q_{i})) \tag{1}$$

Here, top-k refers to the selection of indices corresponding to the $k$ highest-scoring cases as determined by the similarity measure. $\beta$ represents the indices of these retrieved cases, while $\text{Sim}$ is a similarity metric (e.g., cosine similarity) that measures the similarity between the intra-embedding of the prompt’s question and the intra-embeddings of the question parts of each case in the casebase.

Inter-embedding retrieval uses $g(\mathcal{Q})$ from the prompt to search the casebase, focusing on identifying relevant cases akin to an information retrieval style search, where attribute-to-attribute matching is not strictly followed. The best matching case is identified as follows:

$$\beta_{k}=\underset{c_{i}\in C,\,k}{\text{top-k}}\,\;\text{Sim}(g(\mathcal{Q}) ,g(X_{i})) \tag{2}$$

where $X_{i}$ can be either $S_{i}$ (the Snippet part) or $E_{i}$ (the Entity part) of the case.

Hybrid embedding retrieval is an alternative matching that involves a combination of both intra and inter-embeddings of the prompt’s $\mathcal{Q}$ representations being used to match cases in a hybrid weighted retrieval approach:

$$\begin{split}\beta_{k}=\underset{c_{i}\in C,\,k}{\text{top-k}}\,(&w_{1}\cdot \text{Sim}(f(\mathcal{Q}),f(Q_{i}))+w_{2}\cdot\text{Sim}(g(\mathcal{Q}),g(S_{i }))+\\ &w_{3}\cdot\text{Sim}(g(\mathcal{Q}),g(E_{i})))\end{split} \tag{3}$$

This approach utilises both representation forms of the prompt’s query $f(\mathcal{Q})$ and $g(\mathcal{Q})$ for retrieval. Given the top $k$ cases $\{c_{\beta_{j}}\}_{j=1}^{k}$, we can extract the context for the prompt based on the retrieval option $\rho$ as follows:

$$\displaystyle\text{Context,}\;\mathcal{C}(\rho)= \displaystyle\{S_{\beta_{j}}\}_{j=1}^{k} \text{ if } \rho=1 \text{ , “support-text-only”} \tag{4a}$$
$$\displaystyle\text{Context,}\;\mathcal{C}(\rho)= \displaystyle\{Q_{\beta_{j}},S_{\beta_{j}},E_{\beta_{j}},A_{\beta_{j}}\}_{j=1} ^{k} \text{ if } \rho=2 \text{ , “full-case”} \tag{4b}$$

## 5 Embedding models

In this work, we explore embeddings generated by BERT, AnglEBERT, and LegalBERT; the latter being pre-trained on diverse English legal documents, with the rest all being general-purpose embeddings. We next provide an overview of these models, as illustrated in Figure 3, and discuss how they can be used to generate the $f$ and $g$ forms of representations.

![Figure 3: Architecture and training process for BERT and AnglEBERT. Note that LegalBERT has the same architecture as BERT, but is pre-trained on legal text.](x1.png)

### 5.1 BERT

The Bidirectional Encoder Representations from Transformers (BERT) model is a language model for learning generalisable text embeddings. The model is formed of an encoder block (taken from the transformer architecture in), followed by a fully-connected layer. The bidirectional nature of BERT is derived from its pre-training technique, which conditions on both the left and right contexts of input sentences simultaneously. The model uses a self-supervised learning strategy that combines masked-language modeling (MLM) with next sentence prediction (NSP) to acquire contextually rich word embeddings. During training, a pair of sentences is fed into the model, and a random subset of words is replaced with the `[MASK]` token, establishing a sequence-to-point task. The objective here is to predict the masked words by using the context provided by both previous and subsequent words. Furthermore, a `[CLS]` token is inserted at the beginning of the input sequence to accumulate contextual information from the entire sequence, facilitating tasks like sentence relationship classification. Pre-training with both MLM and NSP, can be seen as typical text prediction and is controlled by the standard cross-entropy objective function. BERT is pre-trained on a combination of large general purpose text datasets totalling 3.3B words and has demonstrated strong performance across many domains.

### 5.2 LegalBERT Trained on General Legal Data

Domain-specific knowledge is known to be beneficial for legal tasks. For example, the word ‘case’ may refer to a variety of containers (brief case, suit case, display case, etc), but also a court case. While semantic relations with the latter are likely to be impactful for legal question answering, the greater frequency of the former in general corpora will result in embeddings more weighted towards that context. The LegalBERT family of models enhance the BERT model by further pre-training on an additional 12 GB of diverse English legal documents from a mix of UK, EU, and US legislation and case law. The goal is to embed domain knowledge into produced embeddings by learning from a relevant document set.

### 5.3 BERT with AnglE Embeddings

The AnglE embeddings adopts a contrastive learning strategy (similar to Siamese networks) to learn embeddings through matching both positive and negative text pairs, where a positive pair is considered to be similar (above some threshold usually). The process begins with BERT embeddings, input to AnglE for optimisation. Its novelty stems from one of the three loss functions, that are designed to overcome the vanishing gradient issue encountered in cosine similarity-based comparisons, particularly at the extremes of similarity (or dissimilarity). This is achieved by comparing embeddings based on angle and magnitude within complex spaces, effectively bypassing cosine similarity’s saturation problem. Once trained the AnglE embedding model can be used to generate text embeddings using a final pooling layer.

One of the difficulties when using AnglEBERT for a specific domain is that one must generate a supervised training set (unlike with BERT which can be trained in an unsupervised manner using the MLM and NSP self-supervision methods). This is because the AnglE method adopts a contrastive learning strategy, where the supervised dataset must include paired instances for training. This can be prohibitive in contexts where domain expertise is required for labelling.

### 5.4 Dual-embedding Case Representation with AnglE

For the purposes of this work, we leverage dual-embeddings introduced in. In terms of the inter-embedding retrieval, a specific embedding prompt cue $Cue(\mathcal{Q})$ is used to contextualise the relevance of the query embeddings towards matching with attributes other than that of questions, as follows:

$$Cue(Q)=\text{“Represent this sentence for searching relevant passages: ”}\{Q\}$$

The idea here is that the cue is used to influence the embedding generation towards inter-retrieval oriented embeddings as follows:

$$g(Cue(\mathcal{Q}))$$

For intra-embedding retrieval the prompt text is empty, i.e., input the text without specifying an additional prompt cue. This means the embedding function $f$ processes the query $\mathcal{Q}$ directly, as $f(\mathcal{Q})$. Table 2 provides an example of question and support text version that are used as input to each of BERT, AnglEBERT and LegalBERT with relevant prompts to enable the generation of the alternative embeddings that we intend using during case matching with CBR.

**Table 2: Comparison of an example question with and without the `Cue` text (in blue) to create inter and intra embeddings.**

| Embedding | Question |
| --- | --- |
| intra | $f$(“What were the court’s findings regarding the financial liabilities of Allco Finance Group Ltd to Blairgowrie Trading Ltd?”) |
| inter | $g$(“Represent this sentence for searching relevant passages:” + “What were the court’s findings regarding the financial liabilities of Allco Finance Group Ltd to Blairgowrie Trading Ltd?” ) |

## 6 Evaluation

The aim of our evaluation is two-fold: 1) to understand the impact of inter and intra embeddings on weighted retrieval, and 2) to understand the generative quality of RAG systems when coupled with a case-based retrieval-only system. To analyse weighted retrieval we compared several representation combinations of embedding models and similarity weights as follows:

*   compare three alternative forms of text embeddings using the encoders presented in Section 5 - BERT, LegalBERT and AnglEBERT;
*   compare four alternative weighting schemes to assess utility of question, support, and entity components within case representations. These include:
    *   Question only, represented by the weights [1,0,0] (see Equation 1),
    *   Support only, with weights [0,1,0],
    *   Entities only, using weights [0,0,1] (see Equation 2),
    *   A hybrid approach, combining these components with weights [0.25, 0.40, 0.35] (refer to Equation 3).

Accordingly BERT[0,1,0] would denote using a Support only version of retrieval with the BERT embedding; and using the same naming convention, AnglEBERT[0.25,0.4,0.35] indicates a hybrid dual embedding method where AnglEBERT embeddings are used with the specified weights for case retrieval. Our baseline comparator is an LLM with no case retrieval i.e. No-RAG.

We selected Mistral for answer generation at test time, due to its open-source availability, allowing us to use a model distinct from OpenAI’s GPT-4, which was employed for formulating the Q&A casebase. This approach effectively simulates consulting an alternative expert in place of a human specialist.

### 6.1 Legal QA Dataset Analysis

The ALQA dataset, introduced in Section 3 is a synthetic Q&A dataset generated from real legal documents in the Australian Open Legal Corpus. Here sentences extracted from documents, each coupled with a prompt, are used to generate corresponding questions and answers from OpenAI’s GPT-4 model. We performed a multi-stage analysis to ensure that this dataset was appropriate for our retrieval and follow-on answer generation tasks.

![Figure 4: Cosine similarity distribution for intra- and inter-embeddings.](extracted/5517515/images/legal_sim_dist.png)

Dataset Validation involved a randomly sampled manual analysis of the questions and answers performed by the research team to ensure the dataset contained no LLM-based anomalies (i.e., hallucination, factually incorrect statements, etc). We then converted the question text into intra- and inter-embeddings using BERT, LegalBERT and AnglEBERT and examined the similarity distribution by calculating the cosine similarity between each instance and its nearest neighbour (shown in Figure 4). We observe that the similarity distributions are mostly Gaussian, with the most frequent values between 0.7 and 0.8 cosine similarity for both embedding types produced by BERT and AnglEBERT. Embeddings learned by LegalBERT seem to be more densely clustered, as indicated by the higher similarity. This could suggest a reduced ability to discriminate based on similarity compared to BERT and AnglEBERT. We believe the results of this analysis were very promising, as they suggest the embeddings avoid the traditional issues associated with feature engineering approaches (such as sparse similarity distributions).

Case-Base consisted of the ALQA dataset where each case consists of the full Q&A content as discussed in Section 3.1. While originally containing 2,124 question-support-answer triplets, 40 were removed due to offensive content, and therefore our case-base contains 2,084 cases. The case representation was also expanded to include entities to form the complete tuple as discussed in Section 4.

**Table 3: Prompts used in this research.**

| Scenarios & Generator | Prompt |
| --- | --- |
| Extract legal acts to pair cases for test set creation. Gpt-3.5-turbo-0125 | Extract the legal act(s) in this text. Print ‘None’ if nothing is found. { TEXT } |
| Extract entities for case representation. Gpt-3.5-turbo-0125 | Extract named entities and unique identifiers as a single text (separated with white-space) line from this ” + TEXT. Print ‘’ if nothing is found. { TEXT } |
| Generate Qs from text pairs for test set creation. Mistral-7B | Produce a question and answer where the answer requires detailed access to both Text 1 and Text 2. Don’t refer texts in the question or answer. { Text1: TEXT1 — Text2: TEXT } |
| Generate answers from snippets for retrieval analysis. Mistral-7B | Answer QUESTION by using the following contexts: { TEXT1 — TEXT2 } |
| Generating answers from cases for retrieval analysis. Mistral-7B | Answer QUESTION as a simple string (with no structure) by using the following question, citation, and answer tuples as context: { Question: Q1, Citation: C1, Answer: A1 — Question: Q2, Citation: C2, Answer: A2 } |

Test Set Creation focused on creating a discrete test set of questions that reference applicable knowledge in the case-base, without directly mapping to a single case in the case-base. To guide the generation of unique questions for test purposes, we first analysed the case-base in terms of unique legal acts mentioned in all cases. We then selected case pairs based on the common acts and, using Mistral-7B generated 35 new question-answer pairs, each answerable using the combined information from both cases in a pair, as detailed in the prompt presented in Table 3. The rationale is that by pairing cases with common legal acts, we can encourage Mistral to create novel test Q&A pairs. These pairs are unique in that they necessitate synthesising information from both cases in the pair to form a coherent question and corresponding answer, ensuring that the resulting pairs differ from the questions and answers of the individual cases in the case-base, thereby creating a set of new test cases that are reasonably disjoint. All outputs were manually reviewed to ensure they were suitable test cases (Test dataset available at [open-australian-legal-qa-test](https://huggingface.co/datasets/Ramitha/open-australian-legal-qa-test)). After pruning cases that lacked suitable answers or contained answers merely linked to the case pair by conjunctions, we were left with a total of 32 cases.

### 6.2 Retrieval Analysis

We first evaluated the quality of case retrieval, by exploiting the fact that each of our 32 test cases had originated from a pair of parent cases. Accordingly, for each test case, we treated the pair of parent cases from the training set as relevant, and all other cases as irrelevant (allowing calculation of ranked precision and recall). We then performed a similarity-based retrieval using the k-Nearest Neighbors algorithm, exploring a range of $k$ values consisting of prime numbers between 1 and 37. We calculated results using F1-score for retrieval@k and visualised using a heat-map (see Figure 5). Here the best performing algorithm was Hybrid AnglEBERT with [0.25, 0.40, 0.35] weights and $k=3$. Accordingly, $k$ was selected as 3 to be used in the subsequent generative experiments with $k=1$ as a comparative baseline.

![Figure 5: F1 score for Retrieval@k](extracted/5517515/images/f_score_heatmap_per_k.png)

### 6.3 Generation Results

We evaluated the quality of generated output using six algorithms run with $k=1$ and $k=3$, along with the baseline for No-RAG. The results are presented in Table 4.

**Table 4: Cosine scores for hybrid algorithms**

| | | No Context | Support | Full Case |
| --- | --- | --- | --- | --- |
| $k=0$ | No-RAG | 0.8967 | | |
| $k=1$ | Hybrid BERT | - | 0.8986 | 0.9068 |
| | Hybrid LegalBERT | - | 0.9020 | 0.9043 |
| | Hybrid AnglEBERT | - | 0.9121 | 0.9074 |
| $k=3$ | Hybrid BERT | | 0.9007 | 0.8998 |
| | Hybrid LegalBERT | - | 0.9034 | 0.9045 |
| | Hybrid AnglEBERT | - | 0.9092 | *0.9141 |

Next, we evaluated the quality of generated output. Six algorithms were run with $k=1$ and $k=3$, along with the baseline for No-RAG.

The Mistral-7B-open model was utilised as the LLM to generate the answers given a question from a test case with the RAG context (formed using the CBR-RAG retrieval approaches). The generated content was then converted to an embedding using Mistral for cosine-based comparison with the expected answer from the test case (i.e., reference text) for comparison, with the expectation that higher the similarity the better the CBR-RAG setup.

Relatively high cosine scores were observed with the No-RAG baseline due to the generator having parametric memory in most of the legal questions asked by default. The best semantic similarity was noted with the Hybrid AnglEBERT variant when 3 nearest neighbours were fed into the generator in the form of full cases forming context for RAG. It provided answers on average with 1.94% increase in performance. All hybrid variants performed better than the No-RAG baseline. We also observed that including the full case in the prompt provided better results compared to including only the Support text in most hybrid algorithms. Overall, Hybrid AnglEBERT outperforms the BERT and LegalBERT variants with higher semantic similarity observed when $k=3$.

We performed a series of ANOVA tests to evaluate whether results were significant. Following this we carried out paired tests between the best-performing methods from each of the BERT and LegalBERT groups (in bold), as well as the baseline No-RAG. Here we found that hybrid AnglEBERT k=3, significantly outperforms (asterisk) both ’No-RAG’ and hybrid LegalBERT k=3, at the 95% confidence level, as shown by a one-tailed T-test. Against hybrid BERT k=1, AnglEBERT k=3 shows significant improvement at the 90% confidence level.

## 7 Conclusions

In this paper we have presented CBR-RAG, improving LLM output by augmenting input with supporting information from a case-base of previous examples. We have performed an empirical evaluation of different retrieval methods with knowledge representation and comparison using BERT, LegalBERT, and AnglEBERT embeddings. Responses generated by CBR-RAG outperforms those of baseline models in similarity to ground truth. Our findings confirm that using a case-retrieval approach in RAG systems lead to clear performance benefits, but selecting an appropriate embedding for case representation is key. A qualitative analysis with a domain expert would be an ideal next step to validate these results. The fact that AnglEBERT had the best performance suggests that its contrastive approach to optimising for embeddings (based on similarity comparisons) remains more important than the standard self-supervised masked training strategies used by LegalBERT, even if trained on general legal data. We note that none of the embedding methods, including LegalBERT (trained on broader legal collections), were fine-tuned to the ALQA-specific legal corpus. We are keen to explore the impact of fine-tuning using contrastive self-supervision methods and determine the necessary data supervision burdens for this process, which could pose disadvantages in certain domains.

In future work, we aim to explore further opportunities within representation and specifically alternative methods for text embeddings. Moreover, given the hybrid embeddings’ success, which combines multiple representations for fine-grained similarity comparison, we are keen to expand CBR-RAG with more retrieval capabilities. Finally, we found that combining multiple neighbours while maintaining a coherent prompt is challenging, so we plan to explore case aggregation strategies in the future.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="improve-your-rag-accuracy-with-a-smarter-chunking-strategy.md">
<details>
<summary>Improve Your RAG Accuracy With A Smarter Chunking Strategy</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://sarthakai.substack.com/p/improve-your-rag-accuracy-with-a>

# Improve Your RAG Accuracy With A Smarter Chunking Strategy

### Here's how to pick a good one based on your data + use case.

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

https://substackcdn.com/image/fetch/$s_!UDYD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b9f065e-d41f-4da7-b0bb-47015f54bdd9_1024x1024.png

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

https://substackcdn.com/image/fetch/$s_!mOyZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8aa5c96-a618-4950-b0f0-f05e481cb2e2_1536x1024.png

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

1. **Structure matters.** Documents have hierarchy. Use it.

2. **Context matters.** Tables without explanations are useless. Lists without headers are meaningless.

3. **Different documents need different strategies.** Financial reports aren’t blog posts.

4. **At scale, simplicity wins.** Page-level chunking beats complex strategies on 10K+ documents.

5. **Measure everything.** You can’t improve what you don’t measure.

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

* * *

_Have questions about chunking strategies for your specific use case? I’m always experimenting with new approaches and would love to hear what’s working (or not working) for you._

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="issue-76-optimize-rag-with-hybrid-search.md">
<details>
<summary>Issue #76 - Optimize RAG with Hybrid search</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://mlpills.substack.com/p/issue-76-optimize-rag-with-hybrid>

# Issue #76 - Optimize RAG with Hybrid search

# 💊 Pill of the week

Retrieval-Augmented Generation (RAG) is reshaping traditional search and AI-driven information retrieval systems by **combining the power of retrieval and generation models**. However, RAG systems often face challenges when scaling to large data repositories or handling diverse queries. A basic RAG system, which **typically relies on semantic search** alone, can struggle with both precision and efficiency. This article explores the use of **hybrid search—combining sparse (keyword-based) and dense (vector-based) retrieval**—to address these limitations, diving into the technical intricacies, practical implementation, and potential challenges.

This article is the first in a two-part series on optimizing RAG. Next week, we'll delve into another critical optimization technique: reranking. Stay tuned for the follow-up article, "Enhancing RAG with Reranking," which will focus on refining retrieval results to ensure the most relevant documents are prioritized for response generation.

## Understanding RAG

RAG operates in two main stages:

1. **Retrieval**: The system retrieves relevant documents or passages from an external knowledge base based on an input query.

2. **Generation**: These retrieved documents are used as context to generate a response.


The standard RAG system **typically uses a dense retriever**—often based on a bi-encoder architecture that learns to embed queries and documents into the same vector space—and a sequence-to-sequence generator (such as a transformer). While the dense retriever excels at capturing semantic meaning, it can **struggle with precise term matching**, making it less reliable in situations where exact phrases, rare words, or domain-specific terminology are essential.

This limitation makes hybrid search a natural solution for improving RAG’s retrieval accuracy and efficiency.

## Challenges in RAG Optimization

1. **Quality of Retrieved Documents**: Irrelevant documents degrade the performance of the generator, leading to unhelpful or incorrect responses.

2. **Relevance Ranking**: The ordering of retrieved documents matters. If the most relevant documents are not prioritized, the generator’s output will be suboptimal.

3. **Scalability**: With growing data, balancing retrieval speed with result quality becomes a critical issue.

4. **Domain Specificity**: RAG systems often require domain-specific fine-tuning to handle specialized queries effectively. Dense retrieval alone may not suffice in these cases, making hybrid search a valuable alternative.


## Hybrid Search

Hybrid search combines **two key retrieval methods: sparse (keyword-based) and dense (embedding-based) retrieval**. Each has its strengths and weaknesses, and hybrid search leverages the best of both worlds.

https://substackcdn.com/image/fetch/$s_!vOTo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66287a2e-84b0-4d0f-b2a2-91c9f5a46d59_810x939.png

### Sparse Retrieval (Keyword Search)

Sparse retrieval, commonly implemented through algorithms like BM25, **ranks documents based on keyword frequency and rarity**. BM25 works well for exact **keyword matching**, making it effective in retrieving documents with specific terms. However, it fails to capture the deeper semantic relationships between words, so it may miss documents that are contextually relevant but do not contain the exact query terms.

BM25 ranks documents based on:

- **Term Frequency**: The more a query term appears in a document, the more relevant it is considered.

- **Inverse Document Frequency**: The fewer documents contain a query term, the more weight it carries.


This method shines in cases where the query includes rare terms, specific phrases, or domain-specific keywords but may struggle to retrieve documents that convey the same meaning with different words.

### Dense Retrieval (Vector Search)

Dense retrieval involves **embedding both the query and documents into vectors in a high-dimensional space, with the goal of capturing their underlying semantics**. Common methods like cosine similarity measure how close the query and document vectors are, indicating their relevance. Dense retrieval excels in finding semantically related content even when exact word matches are not present.

However, dense retrieval can fall short in cases where specific terms, rare words, or names are critical. Since embeddings prioritize semantic closeness, they may rank documents higher that are contextually similar but miss exact term matches.

### Advantages of Hybrid Search

Hybrid search combines the strengths of sparse and dense retrieval methods:

1. **Improved Accuracy**: Combining keyword precision from sparse retrieval with the semantic understanding of dense retrieval results in more relevant document retrieval.

2. **Contextual and Specific Matching**: Hybrid systems handle both semantic similarity and exact term matching, improving performance on queries that require specific term recognition, such as abbreviations or technical jargon.

3. **Flexibility**: The combination enables the system to perform well across a broader range of query types, from specific fact-based queries to more open-ended or context-based ones.


### Limitations of Hybrid Search

While hybrid search offers notable advantages, it comes with some challenges:

1. **Increased Latency**: Running both sparse and dense retrieval in parallel may lead to slower response times.

2. **Computational Expense**: Hybrid models are more computationally demanding, as they require the maintenance and execution of both sparse and dense indexes.

3. **Implementation Complexity**: Merging results from different retrieval methods can be non-trivial, requiring custom fusion techniques or weighted scoring mechanisms.


## Implementation of Hybrid Search

Implementing hybrid search involves the following steps:

1. **Keyword Search**: Use sparse retrieval methods like BM25 to score documents based on term frequency and inverse document frequency.

2. **Vector Search**: Perform dense retrieval using techniques such as cosine similarity on vector embeddings of the documents and query.

3. **Result Fusion**: Combine results from both retrieval methods using techniques such as weighted fusion:


> H = (1−α)⋅K + α⋅V


where:


   - H is the hybrid score,

   - K is the keyword search score,

   - V is the vector search score,

   - α is a weighting parameter that balances the contribution of sparse and dense retrieval.


Alternative fusion techniques, like Reciprocal Rank Fusion (RRF), can also be used to combine results.

## Performance Considerations

### Accuracy

By leveraging both sparse and dense retrieval, hybrid systems can capture both exact matches and semantically related content, significantly improving the overall accuracy of RAG systems.

### Efficiency

Careful optimization, such as caching frequently accessed vectors or documents, can mitigate the increased latency from running dual search algorithms. Fine-tuning the weight parameter α\\alphaα also helps maintain a balance between precision and recall.

### Scalability

Hybrid retrieval methods scale better than dense-only systems, especially in large datasets. The computational burden of dense vector search can be reduced by using sparse retrieval as a first-pass filter.

### Memory Usage

Hybrid systems may require more memory due to the need to maintain both inverted indexes for sparse retrieval and vector indexes for dense retrieval.

## Conclusion

Hybrid search offers a powerful solution for optimizing RAG systems by blending the exactness of sparse retrieval with the semantic richness of dense retrieval. The ability to match both keywords and concepts improves retrieval accuracy and ensures that relevant documents are prioritized, even in large or domain-specific datasets. While hybrid search comes with additional computational and implementation complexities, its benefits in terms of accuracy and flexibility often outweigh the costs.

In our next article, we'll explore how reranking can further enhance the relevance of retrieved documents by intelligently reordering results from hybrid search. Look out for "Enhancing RAG with Reranking" next week!

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