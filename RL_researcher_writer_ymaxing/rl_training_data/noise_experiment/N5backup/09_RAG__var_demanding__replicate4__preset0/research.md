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

### Source [34]: https://apxml.com/courses/optimizing-rag-for-production/chapter-6-advanced-rag-evaluation-monitoring/rag-offline-online-evaluation

Query: What are the key operations and theoretical rationale for separating RAG into offline ingestion indexing versus online query-time retrieval and generation phases?

Answer: Offline evaluation, also known as batch evaluation, is performed on static, pre-defined datasets in an environment separate from live user traffic. It serves as a controlled laboratory for assessing your RAG system's capabilities, particularly when introducing changes to its components or architecture. The primary goals of offline evaluation are to: Assess System Changes: Quantitatively measure the impact of modifications, such as new embedding models, re-ranking algorithms, fine-tuned LLMs, or different chunking strategies, before they affect users. Regression Testing: Ensure that new updates do not degrade previously established performance levels on known benchmarks. Deep Performance Analysis: Utilize comprehensive, often computationally intensive metrics to gain detailed insights into specific aspects of the retrieval and generation pipeline. Sustaining the effectiveness of a production RAG system demands an evaluation strategy that extends past initial deployment. This involves a continuous cycle of assessment and refinement. Two primary approaches to evaluation, offline and online, form the basis of this cycle.

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

### Source [47]: https://www.chitika.com/graph-based-retrieval-rag/

Query: How does the GraphRAG approach of building entity knowledge graphs and hierarchical community summaries enable superior handling of multi-hop relational queries over standard document retrieval?

Answer: GraphRAG’s retrieval and augmentation process transforms handling of complex queries by embedding contextual reasoning into the data pipeline. Unlike traditional methods that rely on isolated document retrieval, GraphRAG dynamically integrates knowledge graphs to establish meaningful connections between disparate data points, enabling retrieval of relevant documents and the relationships that bind them. Multi-hop reasoning in GraphRAG emulates human-like decision-making by dynamically navigating interconnected data points using adaptive traversal algorithms that determine optimal hops. It employs dynamic path optimization, evaluating relevance of each node and edge during traversal, ensuring retrieval of contextual relationships. Hierarchical community clustering optimizes retrieval. This contrasts with static retrieval methods.

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

### Source [57]: https://www.linkedin.com/posts/haruiz_building-trustworthy-rag-systems-with-in-activity-7310729777227669505-nd6u

Query: How should the augmentation and prompt construction process in RAG be designed to optimally integrate retrieved chunks with user queries and instructions for grounded LLM generation, including citation requirements?

Answer: Step 3: Context Augmentation The retrieved chunks are added to the LLM prompt (as “context”), grounding it in real data. Step 4: Response Generation The LLM (e.g., Gemini, GPT, Claude) uses this augmented prompt to generate a response. This creates an AI that can reason with context, not just pattern-match text.

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

<research_source type="scraped_from_research" phase="exploitation" file="agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop.md">
<details>
<summary>Agentic RAG vs Classic RAG: From a Pipeline to a Control Loop</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/agentic-rag-vs-classic-rag-from-a-pipeline-to-a-control-loop/>

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

---

## How to Use This Article

-   **If you’re building a RAG system right now:** Skip to the section matching your document type (financial, medical, technical, etc.) and implement those strategies immediately.

-   **If you’re debugging poor RAG performance:** Start with “Why Most Chunking Strategies Are Awful” to diagnose the issue, then jump to solutions.

-   **If you’re optimizing an existing system:** Focus on “Scaling to 10K+ Documents” and the evaluation metrics section.

-   **If you’re just learning about RAG:** Read straight through. The examples will make everything clear.

---

## Table of Contents

1.  Why Most Chunking Strategies Are Awful

2.  The Three Types of Chunking Strategies

3.  Layout-Aware Chunking: The Game Changer

    -   [See interactive visualisation for this topic](https://www.miskies.app/miskie/miskie-1760769325400)
4.  Advanced Strategies That Actually Work

    -   [See interactive visualisation for this topic](https://www.miskies.app/miskie/miskie-1760769543652)
5.  Domain-Specific Playbooks

    1.  [See interactive visualisation for this topic](https://www.miskies.app/miskie/miskie-1760769820033)

        -   Financial Documents

        -   Medical Records

        -   Legal Contracts

        -   Technical Manuals
6.  Handling Tables and Images

7.  Scaling to 10K+ Documents in prod

8.  How to Actually Evaluate Your Chunking Strategy

9.  The Decision Framework

---

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

-   “Item 1: Something about compliance”

-   “Item 2: Something about auditing”

-   “Item 3: Something about reporting”

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

## The Three Types of Chunking Strategies

Not all chunking strategies are created equal. Here’s how they break down:

https://substackcdn.com/image/fetch/$s_!UDYD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b9f065e-d41f-4da7-b0bb-47015f54bdd9_1024x1024.png

### Naive Strategies (The Baseline You Should Move Past)

-   **Fixed-Size Chunking:** Split every N tokens. Fast, simple, and loses all context.

Use case: You need a quick prototype or you’re working with genuinely unstructured text (chat logs, social media feeds). That’s it.

-   **Recursive Character Chunking:** Split on `\n\n`, then `\n`, then spaces. Slightly respects structure.

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

-   Recognising that a document has headers, and those headers tell you what the following paragraphs are about.

-   Recognizing that a table is a self-contained unit.

-   Recognizing that a list is a list.

-   And so on.

## Layout-Aware Chunking

Humans don’t read documents as flat text streams. We use visual cues.

[See an interactive visualisation](https://www.miskies.app/miskie/miskie-1760769325400)

When you open a PDF, you immediately see:

-   The title (big, bold, top of page)

-   Section headers (medium, bold, with spacing)

-   Paragraphs (blocks of regular text)

-   Tables (grid structure, distinct from text)

-   Lists (bullets or numbers, indented)

-   Figures (images with captions)

You use all of this to understand the document. Why shouldn’t your RAG system?

**Layout-aware chunking means parsing documents with their structure intact.** You identify titles, headers, sections, tables, lists, and figures. Then you chunk intelligently around those boundaries.

### How It Actually Works

Let’s walk through a real example. You have a 10K financial filing.

**Traditional approach:**

1.  Split every 512 tokens

2.  Get 847 chunks

3.  Pray for good retrieval

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

-   **DeepDocDetection** (open source): Great for PDFs. Detects titles, headers, paragraphs, tables, figures. Free. Requires some setup.

-   **Amazon Textract** (AWS service): Production-ready. Handles complex layouts. Detects titles, headers, sub-headers, tables, figures, lists, footers, page numbers, key-value pairs. Costs money but works reliably.

-   **Docling** (preprocessing): Good for standardizing different document formats before chunking.

## Advanced Strategies That Actually Work

Once you’ve got layout-aware chunking down, there are three advanced techniques worth knowing.

[See an interactive visualisation](https://www.miskies.app/miskie/miskie-1760769543652)

### Hierarchical/Parent-Child Chunking

The problem: You want small chunks for precise retrieval. But you also want large chunks for context preservation.

The solution: Create both.

**How it works:**

1.  Create large “parent” chunks (1000-2000 tokens) that preserve broad context

2.  Split those into smaller “child” chunks (200-500 tokens) for precise matching

3.  Index the child chunks for retrieval

4.  Return the parent chunks to the LLM for generation

When someone asks a question, you match against the small, focused child chunks. But you give the LLM the large parent chunk with full context.

Best of both worlds.

**Real example:** Technical documentation. A section explains how to configure a database. The parent chunk is the entire “Database Configuration” section. The child chunks are individual configuration parameters.

User asks: “How do I set the connection timeout?”

You retrieve the child chunk about connection timeout (precise match). But you return the entire Database Configuration section to the LLM (full context about database settings, prerequisites, related parameters).

Result: Accurate answer with proper context.

### Agentic Chunking (When Accuracy Matters More Than Speed)

This one’s expensive. But for high-value use cases, it’s worth it.

**The concept:** Use an LLM to decide how to chunk.

1.  Convert sentences to standalone propositions (replace pronouns with actual references)

2.  Have an LLM evaluate each proposition: “Does this belong in the current chunk or should I start a new one?”

3.  Group semantically related propositions, even if they’re far apart in the document

**Example transformation:**

-   Original: “He led NASA’s Apollo 11 mission.”

-   Proposition: “Neil Armstrong led NASA’s Apollo 11 mission.”

Now that proposition makes sense on its own, without context from previous sentences.

**The results:** Reduction in incorrect assumptions. Significantly better answer completeness.

**The cost:** Multiple LLM calls per document. Slow. Expensive.

**When to use it:** Customer support knowledge bases, legal document analysis, medical literature review. Cases where getting the right answer matters more than processing speed.

### Late Chunking (For Cross-References and Pronouns)

Standard approach: chunk first, embed later.

Late chunking: embed first, chunk later.

**Why this matters:** When you embed after chunking:

-   Each chunk only has context from within itself.

-   Pronouns become ambiguous.

-   Cross-references break.

Late chunking processes the entire document through the embedding model first. Every token gets embedded with full document context, then you chunk the token embeddings.

Result: Chunks maintain semantic information from the whole document. “The system” in chunk 47 still knows which system we’re talking about from chunk 2.

**When to use it:** Technical documentation with lots of cross-references. Academic papers that reference earlier sections. Any document where pronouns and implicit references are common.

**The catch:** Requires long-context embedding models (Jina AI embeddings v3, for example) and more compute upfront.

---

## Domain-Specific Playbooks

Different document types need different approaches.

[See an interactive visualisation](https://www.miskies.app/miskie/miskie-1760769820033)

### Financial Documents

**The Challenge:**

-   Tables everywhere.

-   Numbers that need context.

-   Sections that reference each other.

**The Strategy:** Layout-aware chunking with specialised table handling.

**Step-by-step:**

1.  Use a layout parser (Textract or DeepDocDetection) to identify all structural elements

2.  Handle tables specially:

    -   Extract each table separately

    -   Convert to CSV or markdown

    -   Chunk row-by-row if the table is large

    -   Include column headers with every chunk

    -   Add the table title (usually the sentence or paragraph right before the table)
3.  Preserve section hierarchy:

    -   Income Statement is a section

    -   Revenue by Segment is a subsection

    -   Q3 Regional Breakdown is a sub-subsection

    -   Store this hierarchy in metadata
4.  Handle merged cells intelligently:

    -   Unmerge them

    -   Duplicate the original value into each cell

    -   Ensures row-by-row chunking doesn’t lose information

**What this solves:**

-   Revenue questions get answered with the right context.

-   Financial metrics come with their explanations.

-   Tables don’t float around contextless.

### Medical Documents

This is a very high stakes one.

**The Challenge:**

-   Chronological relationships matter a lot.

-   Clinical structure (SOAP notes).

-   Privacy considerations.

-   Precision when answering a question is life-or-death.

**The Strategy:** Semantic chunking for nuance, layout-aware for structure.

**Key principles:**

1.  Preserve clinical note structure:

    -   Subjective, Objective, Assessment, Plan stay together

    -   But each can be a separate chunk with metadata linking them
2.  Maintain temporal context:

    -   Medication history with dates

    -   Symptom progression over time

    -   Previous visit references
3.  Use semantic chunking for research papers:

    -   Medical literature has subtle topic shifts

    -   Semantic boundaries matter more than visual ones
4.  Handle medical terminology carefully:

    -   Keep terms with their context

    -   Don’t split disease names or drug combinations

    -   Maintain relationships between symptoms and diagnoses

**What this solves:** Treatment questions get accurate, complete information. Drug interaction warnings don’t get separated from prescriptions. Patient history maintains chronological coherence.

### Legal Contracts

**The Challenge:**

-   Clauses must stay intact.

-   Cross-references are everywhere.

-   Structure is legally significant.

**The Strategy:** Layout-aware + sliding window overlap for safety.

**Implementation:**

1.  Use layout parsing to identify clause boundaries:

    -   Numbered sections

    -   Lettered subsections

    -   Indentation levels
2.  Never split a clause:

    -   If a clause exceeds max chunk size, keep it together anyway

    -   Better one oversized chunk than broken legal language
3.  Add sliding window overlap (10-20%):

    -   Extra safety net for clauses that span boundaries

    -   Reduces risk of missing critical “except” or “provided that” language
4.  Preserve cross-references:

    -   “See Section 4.2” needs to be retrievable

    -   Store section references in metadata

    -   Enable following references programmatically

**What this solves:** Liability questions get complete clauses with exceptions. Cross-references work. Legal teams don’t yell at you.

### Technical Manuals

**The Challenge:**

-   Step-by-step procedures.

-   Diagrams with explanatory text.

-   Code examples.

-   Cross-references to other sections.

**The Strategy:** Layout-aware chunking with hierarchical metadata.

**Implementation:**

1.  Respect document hierarchy:

    -   Chapter → Section → Subsection → Procedure

    -   Store all levels in metadata

    -   Enables “give me everything about configuring X”
2.  Keep procedures together:

    -   Step 1, Step 2, Step 3 stay in one chunk

    -   Or use parent-child: each step is a child, entire procedure is parent
3.  Handle diagrams:

    -   Use vision-language models to caption images

    -   Store image description with surrounding text

    -   Keep figure references intact
4.  Preserve code blocks:

    -   Code examples stay complete

    -   Include comments and explanations

    -   Link to related configuration settings

**What this solves:** Procedural questions get complete instructions. Diagrams and explanations stay together. Code examples are usable.

---

## Handling Tables and Images (The Stuff That Breaks Everything)

Let’s talk about the elephant in the room: Most documents aren’t just text.

### The Table Problem

Tables are structured data pretending to be text. Naive chunking sees them as sentences. Disaster.

**Three approaches that work:**

**Approach 1: Table-as-Text with Structure Preservation**

-   Extract table to markdown or CSV

-   Keep column headers with every chunk

-   Add row numbers for reference

-   Include table title/caption

**Approach 2: Table-as-Data with LLM Description**

-   Extract table structure completely

-   Use an LLM to write a natural language description

-   Index both the description and the raw table

-   Return the raw table to the LLM when retrieved

**Approach 3: Dual Indexing (Recommended)**

-   Index table descriptions for retrieval

-   Store complete tables separately

-   Retrieve based on descriptions, return full tables

-   Best of both: searchable descriptions, complete data for LLM

### Merged Cells

Financial reports love merged cells. Suppose “Q1-Q3 Revenue” spans three columns. Your table chunker breaks on column boundaries. Now you have three chunks with incomplete data.

**Solution:**

1.  Detect merged cells during parsing

2.  Unmerge them

3.  Duplicate the original value into each individual cell

4.  Now row-by-row chunking works properly

### The Image Problem

Images contain information. Your text-based chunker ignores them. Bad news.

**Three strategies:**

**Strategy 1: Image Captions Only**

-   Extract image captions during parsing

-   Include captions in surrounding text chunks

-   Simplest but loses visual information

**Strategy 2: Vision-Language Model Descriptions**

-   Use GPT-4o, LLaVA, or similar to describe images

-   Store descriptions as text chunks

-   Index descriptions, link to original images

-   Retrieve description, return image to multimodal LLM

**Strategy 3: Multimodal Embeddings**

-   Use CLIP or similar for unified image-text embeddings

-   Index images and text together

-   Retrieve multimodal chunks

-   Requires multimodal LLM for generation

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

---

## Scaling to 10K+ Documents In Prod

Everything changes at scale. What works for 100 documents might not work for 10,000.

### The Page-Level Chunking Revelation

Research shows page-level chunking is surprisingly effective at scale. One page = one chunk (or a few chunks if the page is huge).

**Why this works:**

-   Pages are already meaningful units

-   Authors structure pages with coherent information

-   Reduces total chunk count dramatically

-   Simplifies metadata management

**When to use it:** Large document collections (10K+) where processing speed matters and documents are multi-page (PDFs, reports, books).

### The Metadata

At scale, metadata becomes critical. You need to filter before searching.

**Essential metadata:**

-   document\_type: “financial\_report”, “legal\_contract”, “technical\_manual”

-   date\_created: ISO format timestamp

-   section\_id: hierarchical identifier

-   parent\_chunk\_id: for hierarchical chunking

-   source\_page: page number in original document

-   confidence\_score: if using ML for structure detection

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

---

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

-   “What was Q3 revenue?”

-   “Who is the CEO?”

-   Direct fact lookups

**Medium queries** (50%):

-   “Why did revenue decline in Q3?”

-   “What are the security compliance requirements?”

-   Requires context from multiple chunks

**Hard queries** (20%):

-   “Compare Q3 performance across all product lines and explain regional variations”

-   “What are the legal implications of the liability clause exceptions?”

-   Requires synthesis across many chunks

### The A/B Test Protocol

Don’t guess. Test.

1.  Implement Strategy A (baseline: maybe fixed-size chunking)

2.  Implement Strategy B (candidate: maybe layout-aware)

3.  Run same test queries through both

4.  Compare metrics

5.  Human evaluation on disagreements

**Important:** Test on YOUR documents with YOUR queries. Benchmark results from papers don’t tell you what works for your use case.

### The Red Flags That Mean You Need Better Chunking

Watch for these in user feedback:

-   “The answer was close but missed a key detail” → Context loss at chunk boundaries

-   “The system gave me a table but I don’t know what it means” → Table without context

-   “The answer contradicted itself” → Retrieved conflicting chunks without shared context

-   “The system couldn’t find information I know is there” → Poor chunk boundaries made content unretrievable

Each of these points to a chunking problem, not a retrieval problem.

---

## The Decision Framework

Here’s how to actually decide what to implement.

### Step 1: Understand Your Documents

What are you processing?

-   Mostly text (articles, books, reports)

-   Lots of tables (financial reports, data sheets)

-   Lots of images (technical manuals, scientific papers)

-   Highly structured (legal contracts, regulatory docs)

-   Mixed content (real-world documents)

### Step 2: Understand Your Queries

What are people asking?

-   Simple fact lookup (”What is X?”)

-   Contextual questions (”Why did X happen?”)

-   Comparison questions (”How does X compare to Y?”)

-   Synthesis questions (”Explain the relationship between X, Y, and Z”)

Simple queries → simpler chunking might work

Complex queries → need sophisticated chunking

### Step 3: Understand Your Constraints

What are your limits?

**Processing time:**

-   Need it fast? → Simpler chunking (recursive, layout-aware without heavy ML)

-   Can be slow? → Sophisticated chunking (agentic, semantic with fine-tuning)

**Scale:**

-   <1000 docs? → Any strategy works

-   1K-10K docs? → Need efficient processing, batch pipelines

-   10K docs? → Page-level chunking, distributed processing, metadata filtering

**Accuracy requirements:**

-   Low stakes (internal docs)? → Start simple, iterate based on feedback

-   High stakes (legal, medical)? → Invest in sophisticated chunking upfront

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

-   Implement simplest reasonable strategy (recursive or layout-aware basic)

-   Create test set of 50 queries

-   Measure baseline performance

**Week 2: Iterate**

-   Identify top failure modes from week 1

-   Implement targeted improvements (table handling, list processing, etc.)

-   Measure improvement

**Week 3: Optimise**

-   Fine-tune chunk sizes

-   Add metadata enrichment

-   Optimise for your specific queries

**Week 4: Scale**

-   Set up batch processing if needed

-   Implement monitoring

-   Plan for continuous improvement

---

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

---

## Further Reading

**Tools mentioned:**

-   DeepDocDetection: github.com/deepdoctection/deepdoctection

-   Amazon Textract: aws.amazon.com/textract

-   Docling: Document preprocessing library

-   LlamaIndex: llamaindex.ai

-   LangChain: langchain.com

**Research papers:**

-   Search “semantic chunking RAG 2024” for latest benchmarks

-   Search “layout-aware document processing” for parsing techniques

-   Search “hierarchical retrieval RAG” for parent-child strategies

**Implementation examples:**

-   Look for “layout-aware document parsing for RAG” notebooks

-   AWS samples: amazon-archives/layout-aware-document-processing

-   Community implementations on GitHub

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="jina-scraped-1.md">
<details>
<summary>RAG System in Production: Architecture, Chunking & Evaluation Guide|47Billlion</summary>

Phase: [EXPLOITATION]

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

<research_source type="scraped_from_research" phase="exploitation" file="jina-scraped-2.md">
<details>
<summary>Advanced RAG Techniques for High-Performance LLM Applications</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://neo4j.com/blog/genai/advanced-rag-techniques/>

Title: Advanced RAG Techniques for High-Performance LLM Applications

URL Source: https://neo4j.com/blog/genai/advanced-rag-techniques/

Published Time: 2025-10-17T16:00:00+00:00

Markdown Content:
# Advanced RAG Techniques for High-Performance LLM Applications

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/blog/genai/advanced-rag-techniques/#)[Use necessary cookies only](https://neo4j.com/blog/genai/advanced-rag-techniques/#)

[Skip to content](https://neo4j.com/blog/genai/advanced-rag-techniques/#skip-to-content "Skip to content")

Complete the [opens in new tab Aura Agents Course](https://graphacademy.neo4j.com/courses/aura-agents/?category=aura) Between Apr 15 - May 15 | The First 500 Win Aura Credits

[![Image 1: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)Menu

![Image 2: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)Search Close Menu

*   [Products](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Back](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   GRAPH DATABASE
    *   [Neo4j AuraDB Fully managed graph database as a service](https://neo4j.com/product/auradb/)
    *   [Neo4j Graph Database Self managed, deploy anywhere graph database](https://neo4j.com/product/neo4j-graph-database/)
    *   GRAPH ANALYTICS
    *   [Neo4j Aura Graph Analytics Fully managed graph analytics as a service](https://neo4j.com/product/aura-graph-analytics/)
    *   [Neo4j Graph Data Science Self managed graph algorithms and ML modeling](https://neo4j.com/product/graph-data-science/)
    *   GRAPH AI
    *   [Neo4j Aura Agent Fully managed knowledge-graph-powered AI agent creation platform](https://neo4j.com/product/aura-agent/)
    *   GRAPH TOOLS
    *   [Neo4j Fleet Manager A single control plane to manage all your DB instances](https://neo4j.com/product/fleet-manager/)
    *   [Neo4j Bloom Easy graph visualization and exploration](https://neo4j.com/product/bloom/)
    *   PARTNER SOLUTIONS
    *   [Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud](https://neo4j.com/neo4j-graph-analytics-snowflake/)
    *   [Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric](https://neo4j.com/neo4j-graph-intelligence-microsoft-fabric/)

*   [Use Cases](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Back](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [AI Systems Back your LLMs with a knowledge graph for better business AI](https://neo4j.com/use-cases/ai-systems/)
    *   [Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more](https://neo4j.com/use-cases/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)

*   [Developers](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Back](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Developer Center Best practices, guides, tutorials, and downloads](https://neo4j.com/developer/)
    *   [opens in new tab GraphAcademy![Image 3](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications. Join the 100K+ Neo4j experts.](https://graphacademy.neo4j.com/)
    *   DEVELOPERS
    *   [Deployment Center Deploy Neo4j on any cloud or architecture](https://neo4j.com/deployment-center/)
    *   [Documentation![Image 4](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [Developer Blog Deep dives into more technical Neo4j topics](https://neo4j.com/blog/developer/)
    *   [opens in new tab Community A global forum for online discussion](https://community.neo4j.com/)
    *   DATA SCIENTISTS
    *   [Data Science Documentation![Image 5](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for the Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/)
    *   [Graph Data Science Home Learn what Neo4j offers for data science](https://neo4j.com/product/graph-data-science/)
    *   [Get Started With Graph Data Science Download or get started in Sandbox today](https://neo4j.com/graph-data-science-software/)
    *   [opens in new tab Data Science Community A global forum for data-driven professionals](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/)

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   [Learn](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Back](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   LEARN
    *   [Documentation![Image 6](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [GraphAcademy![Image 7](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications](https://graphacademy.neo4j.com/)
    *   [Resource Library White papers, datasheets, and more](https://neo4j.com/resources/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)
    *   CONNECT
    *   [Neo4j Events Hub![Image 8](https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg)Live and on-demand events, training, webinars, and demos](https://neo4j.com/events/)
    *   [Neo4j Blog Announcements, guides, and best practices](https://neo4j.com/blog/)
    *   [Neo4j Video Hub Covering graph databases, data science, analytics & AI](https://neo4j.com/videos/)
    *   FEATURED EVENTS
    *   [GraphSummit 2026 Graphs + AI: Transform Your Data Into Knowledge](https://neo4j.com/graphsummit/)
    *   [NODES 2026 | November 12 Virtual Conference: Engineering Better Intelligence](https://neo4j.com/nodes/)

*   [Pricing](https://neo4j.com/pricing/)
*   QUICK LINKS
*   [Partners](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Back](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Find a Partner](https://neo4j.com/partners/directory/)
    *   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
    *   [Solution Partners](https://neo4j.com/partners/solution-partners/)
    *   [OEM Partners](https://neo4j.com/partners/oem-partners/)
    *   [Technology Partners](https://neo4j.com/partners/technology-partners/)
    *   [Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

*   [Company](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [Back](https://neo4j.com/blog/genai/advanced-rag-techniques/)
    *   [About Us](https://neo4j.com/company/)
    *   [Newsroom](https://neo4j.com/newsroom/)
    *   [Awards and Honors](https://neo4j.com/awards/)
    *   [Graphs4Good](https://neo4j.com/graphs4good/)
    *   [Careers](https://neo4j.com/careers/)
    *   [Culture](https://neo4j.com/culture/)
    *   [Leadership](https://neo4j.com/leadership/)

*   [Support](https://support.neo4j.com/s/)
*   [Aura Login](https://console.neo4j.io/)

[Get Started](https://neo4j.com/product/auradb/?ref=nav-get-started-cta)[Contact Us](https://neo4j.com/contact-us/)

*   [Aura Login](https://console.neo4j.io/)
*   [Partners](https://neo4j.com/partners/)Partners: submenu

    *   [Find a Partner](https://neo4j.com/partners/directory/)
    *   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
    *   [Solution Partners](https://neo4j.com/partners/solution-partners/)
    *   [OEM Partners](https://neo4j.com/partners/oem-partners/)
    *   [Technology Partners](https://neo4j.com/partners/technology-partners/)
    *   [opens in new tab Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

*   Company Company: submenu

    *   [About Us](https://neo4j.com/company/)
    *   [Newsroom](https://neo4j.com/newsroom/)
    *   [Awards and Honors](https://neo4j.com/awards/)
    *   [Graphs4Good](https://neo4j.com/graphs4good/)
    *   [Careers](https://neo4j.com/careers/)
    *   [Culture](https://neo4j.com/culture/)
    *   [Leadership](https://neo4j.com/leadership/)

*   [Support](https://support.neo4j.com/s/)
*   Search

[![Image 9: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)

*   Products Products: submenu

GRAPH DATABASE
    *   [![Image 10: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083548/aura.svg) Neo4j AuraDB Fully managed graph database as a service](https://neo4j.com/product/auradb/)
    *   [![Image 11: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083552/Neo4j_db.svg) Neo4j Graph Database Self managed, deploy anywhere graph database](https://neo4j.com/product/neo4j-graph-database/)

GRAPH ANALYTICS
    *   [![Image 12: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083556/networkmagnifier_chart.svg) Neo4j Aura Graph Analytics Fully managed graph analytics as a service](https://neo4j.com/product/aura-graph-analytics/)
    *   [![Image 13: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083550/Graph_data_science.svg) Neo4j Graph Data Science Self managed graph algorithms and ML modeling](https://neo4j.com/product/graph-data-science/)

GRAPH AI
    *   [![Image 14: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083551/neo4j_aura_agent.svg) Neo4j Aura Agent Fully managed knowledge-graph-powered AI agent creation platform](https://neo4j.com/product/aura-agent/)

 PARTNER SOLUTIONS 

    *   [![Image 15: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083554/Neo4j_on_Fabric.svg) Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric](https://neo4j.com/neo4j-graph-intelligence-microsoft-fabric/)

    *   [![Image 16: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083555/Neo4j_on_Snowflake.svg) Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud](https://neo4j.com/neo4j-graph-analytics-snowflake/)

Graph Tools

    *   [Neo4j Fleet Manager A single control plane to manage all your DB instances](https://neo4j.com/product/fleet-manager/)
    *   [Neo4j Bloom Easy graph visualization and exploration](https://neo4j.com/product/bloom/)

*   Use Cases Use Cases: submenu

    *   [![Image 17](https://dist.neo4j.com/wp-content/uploads/20240329130329/genai.svg) AI Systems Back your LLMs with a Knowledge Graph for better business AI Learn More](https://neo4j.com/use-cases/ai-systems/)
    *   [Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more All Use Cases](https://neo4j.com/use-cases/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more All Customer Stories](https://neo4j.com/customer-stories/)

*   Developers Developers: submenu

    *   [Developer Center Best practices, guides, tutorials, and downloads Learn More](https://neo4j.com/developer/)[opens in new tab GraphAcademy Free online courses and certifications. Join the 100K+ Neo4j experts. Learn More](https://graphacademy.neo4j.com/)
    *   Developers
        *   [Deployment Center Deploy Neo4j on any cloud or architecture](https://neo4j.com/deployment-center/)
        *   [Documentation![Image 18](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
        *   [Developer Blog Deep dives into more technical Neo4j topics](https://neo4j.com/blog/developer/)
        *   [opens in new tab Community A global forum for online discussion](https://community.neo4j.com/)

DATA SCIENTISTS

    *   [Data Science Documentation![Image 19](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for the Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/)
    *   [Graph Data Science Home Learn what Neo4j offers for data science](https://neo4j.com/product/graph-data-science/)
    *   [Get Started With Graph Data Science Download or get started in Sandbox today](https://neo4j.com/graph-data-science-software/)
    *   [opens in new tab Data Science Community A global forum for data-driven professionals](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/)

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   Learn Learn: submenu

LEARN

    *   [Documentation![Image 20](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [GraphAcademy![Image 21](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications](https://graphacademy.neo4j.com/)
    *   [Resource Library White papers, datasheets, and more](https://neo4j.com/resources/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)

CONNECT

    *   [Neo4j Events Hub![Image 22](https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg)Live and on-demand events, training, webinars, and demos](https://neo4j.com/events/)
    *   [Neo4j Blog Announcements, guides, and best practices](https://neo4j.com/blog/)
    *   [Neo4j Video Hub Covering graph databases, data science, analytics & AI](https://neo4j.com/videos/)

FEATURED EVENTS

    *   [![Image 23: GraphSummit Logo](https://dist.neo4j.com/wp-content/uploads/20250306090638/graphsummit-logo.svg) Graphs + AI: Transform Your Data Into Knowledge Learn more](https://neo4j.com/graphsummit/)
    *   [opens in new tab![Image 24: Neo4j Nodes 2026](https://dist.neo4j.com/wp-content/uploads/20260416111036/nodes-2026-logo.svg) Call for Papers Virtual Conference: Engineering Better Intelligence Submit a session abstract by June 15, 2026 Submit a Talk](https://sessionize.com/nodes26/)

*   [Pricing](https://neo4j.com/pricing/)
*   [Contact Us](https://neo4j.com/contact-us/)
*   [Get Started Free](https://console.neo4j.io/)

Blog Home 

Close

*   [Blog Home](https://neo4j.com/blog/)
*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)
*   [News](https://neo4j.com/blog/news/)

*   [GenAI](https://neo4j.com/blog/genai/)

# Advanced RAG Techniques for High-Performance LLM Applications

![Image 25: Photo of Tomaž Bratanič](https://dist.neo4j.com/wp-content/uploads/20240517073021/tomaz-bratanic-150x150.jpeg)

![Image 26: Photo of Isobel Krüger](https://dist.neo4j.com/wp-content/uploads/20251015110239/isobel-kruger-150x150.jpeg)

[Tomaž Bratanič](https://neo4j.com/blog/contributor/tomaz-bratanic/),

[Isobel Krüger](https://neo4j.com/blog/contributor/isobel-kruger/)

October 17, 2025

17 min read

![Image 27: A constellation of Orion represented as a graph with nodes and relationships.](https://dist.neo4j.com/wp-content/uploads/20251015112403/advanced-rag-techniques.png)

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by combining retrieval with generation to ground outputs in your own data rather than relying solely on pretraining. In practice, RAG systems retrieve relevant information from a knowledge source and integrate it into the prompt, enabling responses that are more accurate, contextual, and trustworthy.

RAG is now a widely used architecture for LLM applications, powering everything from question-answering services that leverage web search, to internal chat tools that index enterprise content, to complex QA pipelines. Its appeal is simple: by augmenting generation with retrieval, teams can deliver LLM experiences that meet today’s expectations for relevance and reliability.

But shipping a RAG system isn’t the finish line. Anyone who’s moved beyond a prototype knows the symptoms: hallucinations creep back in, long queries bog down performance, or answers miss the mark despite the right documents being retrieved. That’s where advanced RAG techniques come in. This guide walks through the strategies that help teams improve relevance, accuracy, and efficiency, so your system not only works, but works at scale.

More in this guide:

*   [RAG Architecture](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-rag-architecture)
    

    *   [What the RAG Pipeline Does](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-what-the-rag-pipeline-does)
    *   [A Typical Failure Mode](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-a-typical-failure-mode)

*   [Why Basic RAG Breaks (And How Advanced RAG Techniques Help)](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-why-basic-rag-breaks-and-how-advanced-rag-techniques-help)
*   [Advanced RAG Advantages and Techniques to Get You There](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-advanced-rag-advantages-and-techniques-to-get-you-there)
    

    *   [Improved Retrieval Quality and Relevance](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-improved-retrieval-quality-and-relevance)
    *   [Make Documents Easier to Retrieve and Use](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-make-documents-easier-to-retrieve-and-use)
    *   [Improve Query Understanding](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-improve-query-understanding)
    *   [Handle Complex, Multi‑Step Questions with Agentic Planning](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-handle-complex-multi-step-questions-with-agentic-planning)
    *   [Ground Answers and Reduce Hallucinations](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-ground-answers-and-reduce-hallucinations)

*   [How to Build an Advanced RAG Pipeline](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-how-to-build-an-advanced-rag-pipeline)
    

    *   [Structure Your Sources](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-structure-your-sources)
    *   [Use Agentic Planning for Complex Questions](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-use-agentic-planning-for-complex-questions)
    *   [Evaluate Your Advanced RAG Tactics](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-evaluate-your-advanced-rag-tactics)

*   [A Practical Plan Using Advanced RAG Techniques](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-a-practical-plan-using-advanced-rag-techniques)
*   [Start Practicing Advanced RAG](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-start-practicing-advanced-rag)
    

    *   [Where to Go From Here](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-where-to-go-from-here)
    *   [Essential GraphRAG](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-essential-graphrag)

*   [Advanced RAG: FAQs](https://neo4j.com/blog/genai/advanced-rag-techniques/#h-advanced-rag-faqs)

## RAG Architecture

A typical RAG pipeline is simple to describe but also easy to underbuild for production. Understanding the RAG architecture baseline and why basic setups struggle helps you move into advanced RAG techniques with the right context.

### What the RAG Pipeline Does

A standard RAG system does four things:

1.   **Ingests content**: splits documents into chunks, adds metadata, and creates embeddings.
2.   **Indexes**: builds a store for efficient retrieval, often a vector index, sometimes with a keyword index as well.
3.   **Retrieves**: fetches top-k context for a query.
4.   **Generates**: prompts the model with the query plus the retrieved context and returns an answer.

At runtime, the system encodes the user’s query with the same model used to embed documents during ingestion, searches the index for the nearest vectors, retrieves the top-k chunks, and includes those chunks with the query in the prompt.

![Image 28: A diagram of the basic RAG process that starts with a question, looking up relevant documents, and then answer generation](https://dist.neo4j.com/wp-content/uploads/20251015123017/standard-rag-system.png)

The basic RAG process

### A Typical Failure Mode

Naive pipelines often perform well in demos but break in production.

This might sound familiar: You ship a quick RAG helper for your team. It nails simple fact lookups. Then a PM asks, “Which enterprise customers renewed last quarter and also opened support tickets about SSO?” The bot replies with a partial list, misses a couple of key accounts, and adds an irrelevant customer.

Here are some common symptoms you’ll recognize:

*   Top-k returns near duplicates or shallow snippets, so the prompt lacks diversity.
*   Retrieval misses proper nouns, IDs, or acronyms (SKU-123, SSO, SOC 2) because they occur rarely.
*   Answers cite the wrong entity or mix details across similar accounts.
*   Latency climbs when you raise _k_, use longer chunks, or rerun retrieval after follow-ups.
*   Poor table and PDF splitting drops headers or footnotes that change meaning.
*   Multi-turn chats drop constraints (“only EMEA,” “last quarter”), so follow-ups forget earlier filters, leading to off-scope answers.
*   Thin retrieval sets push the model to guess and fill in unsupported details.

## Why Basic RAG Breaks (And How Advanced RAG Techniques Help)

Because RAG couples approximate retrieval with probabilistic generation and small context windows, a few recurring failure modes show up in production. These issues usually show up in logs and traces:

*   **Vector-only retrieval** is semantic and can miss exact tokens and rare strings. Without hybrid search, names and codes slip through.
*   **Chunking boundaries** cut across structure, so the model sees fragments without the right context.
*   **No reranking** means cosine similarity rewards proximity, not usefulness.
*   **Missing filters** (time, source, region) let off-scope documents into the prompt.
*   **Limited query understanding** (no expansion or decomposition) under-retrieves for multi-hop questions.
*   **Limited context window** forces you to drop good passages or rely on summaries that lose detail.
*   **No feedback loop** to detect weak context before generation, for example, a simple CRAG-style check.
*   **No graph context** to connect entities and events, so cross-document reasoning fails.
*   **Stale embeddings or indices** after data changes, which means that retrieved data reflects yesterday’s state.

An advanced RAG architecture strengthens what the model sees and how it reasons. It finds better evidence, keeps only what matters, connects it across sources, and verifies the result with citations, so answers are accurate, explainable, and repeatable at scale.

![Image 29: A flow diagram showing the differences between the basic RAG and Advanced RAG processes](https://dist.neo4j.com/wp-content/uploads/20251015123543/naive-rag-versus-advanced-rag.png)

Infographic comparing naive and advanced RAG

## Advanced RAG Advantages and Techniques to Get You There

Advanced generally means better retrieval, better context management, and better answer creation. Below, we list the main advantages of an advanced RAG architecture with go-to techniques.

### Improved Retrieval Quality and Relevance

Retrieval decides what the model even looks at. Most production RAG starts with dense retrieval (embeddings), which is strong for semantic matches but can miss rare terms, IDs, or acronyms. Advanced retrieval goes beyond this baseline with techniques that layer precision, coverage, and structure:

#### Knowledge Graph Retrieval ([opens in new tab GraphRAG](https://neo4j.com/blog/genai/what-is-graphrag/))

When your content contains rich entities and relationships (such as people, products, cases, citations), a knowledge graph lets you retrieve the _context of your data_, not just similar text. You can blend graph traversals with vector search to assemble precise, connected context for the prompt.

**Why graphs matter:**Vector/semantic search is strong for local lookups but struggles with global, cross-document questions and multi-hop relationships. Start by modeling your sources as entities and relationships, then retrieve in two ways: run local traversals to pull related entities and paths around initial hits, and use global community summaries for big-picture questions. This [opens in new tab structured approach](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/) makes it much easier to retrieve and use specific information, expanding the types of questions you can answer with greater accuracy.

## The Developer’s Guide to GraphRAG

Combine a knowledge graph with RAG to build a contextual, explainable GenAI app. Get started by learning the three main patterns.

[Learn to Build](https://neo4j.com/books/the-developers-guide-to-graphrag/?utm_medium=Website&utm_source=Blog&utm_campaign=PCGenAI_CCGraphRAG&utm_content=CNAdvancedRAGTechniques)

![Image 30: A diagram illustrating the impact of GraphRAG, including rich context, accurate answers, vector and graph combination, and orchestration and flow](https://dist.neo4j.com/wp-content/uploads/20251016143611/graphrag-impact-diagram.jpg)
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

Chunk sizes and boundaries strongly influence retrieval quality. Default to fixed-size or sentence-aware splits, layer in semantic chunking when boundaries are messy, and reach for document-aware/adaptive chunkers when structure matters (table, headers, code). When you’re ready to wire it up, the [opens in new tab LangChain text-splitter docs](https://python.langchain.com/api_reference/text_splitters/) have drop-in examples.

#### Parent Retriever

Keep document structure intact by retrieving smaller “child” chunks but swapping in the “parent” block when many children from the same section appear, preserving context and reducing fragmented prompts.

#### Text Summarization / Context Distillation

Summarize the hits so more relevant info fits in the window and the model focuses on the right facts. Most stacks support this: [opens in new tab GraphRAG uses query-focused summarization](https://neo4j.com/blog/what-is-graphrag/), LangChain has a ContextualCompressionRetriever, and LlamaIndex offers tree/refine synthesizers.

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

1.   Break the question into concrete tasks (entities to find, time windows, joins/paths).
2.   Choose the best tool per task (graph/Cypher for relationships and joins; hybrid retrieval for facts/dates; calculator/code when needed).
3.   Execute the query or retrieval and collect evidence with provenance.
4.   Check coverage (does each sub-goal have strong evidence?) and conflicts (do sources disagree?). If weak, try again, broaden your approach, or switch tools.
5.   Conclude when all sub-goals are satisfied or when you hit the budget (max hops/tool calls/tokens). Provide the answer with per-claim citations or state what evidence is missing.

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

*   Plan sub-goals (which entities, which joins/paths, which time windows).
*   Route each sub-goal to the best tool: graph traversal via a graph query language (e.g., Cypher in property graphs) for relationships and joins; hybrid retrieval (lexical + semantic) for facts, names, and dates; optional calculators/code for transformations.
*   Act and verify: execute, check coverage/conflicts, use community/cluster summaries for global questions and path-bounded traversals (k-hop with type/time constraints) to keep context precise and auditable; broaden or switch tools if evidence is weak; apply termination criteria and budgets (max hops/tool calls/tokens) to prevent open-ended tool use; stop when all sub-goals are satisfied or the budget is reached.

### Evaluate Your Advanced RAG Tactics

Don’t skimp on evaluation. You can create a solid evaluation baseline by measuring:

*   **Retrieved-context relevance.**Is the context actually useful for the question?
*   **Groundedness/faithfulness.** Does the answer stick to the retrieved sources?
*   **Answer relevance.**Does it answer the user’s question?
*   **Ranking metrics for retrieval.**For example, track MRR/Recall@k and latency for end-to-end UX.

When you introduce graphs, add simple explainers. For example, show which nodes/edges and passages supported an answer. This increases trust and makes debugging easier.

## A Practical Plan Using Advanced RAG Techniques

Practice makes perfect. Use this sequence to add improvements safely and see what actually moves the needle. Make one change, measure it, and then move to the next.

1.   **Stabilize basic retrieval:**Start with good embeddings, sensible chunking, and clean metadata. Add a reranker so the top-k results are stronger, then measure to establish a baseline.
2.   **Add hybrid search:**Combine BM25 with vectors (via Reciprocal Rank Fusion or RRF) to catch both exact tokens and semantic matches. Track precision@k, Recall@k and groundedness to see the lift.
3.   **Introduce query understanding:**Use query expansion and HyDE (hypothetical questions/documents) to bridge phrasing gaps and improve recall without overfetching.
4.   **Optimize context supply:**Use parent-doc logic and summarization/context distillation to fit more _relevant_ content into the window.
5.   **Structure your data as entities and relationships:** Extract and normalize key entities (people, orgs, products, IDs) and their relationships with provenance, then load them into a lightweight knowledge graph. Index nodes/edges alongside text so retrieval can pull paths and not just passages.
6.   **Enable agentic multi-step Q&A:**Use an agent to handle multi-hop questions: plan sub-goals, route each to the right tool, execute, verify coverage and resolve conflicts, stop within budget, and return answers with per-claim citations and auditable paths.
7.   **Harden grounding:**Lock answers to retrieved sources with strict prompts, CRAG-style retrieval checks, and citation tagging to cut hallucinations.

![Image 31: A flow diagram showing the GraphRAG phases from chunking, extracting, enriching, to searching](https://dist.neo4j.com/wp-content/uploads/20251016143758/graphrag-phases-diagram.jpg)
## Start Practicing Advanced RAG

Want to move from a demo to something dependable? Kick off the process with a small baseline of test queries and a couple of metrics. Then make one change at a time and measure the impact.

*   **Pick one improvement at a time.** Start with reranking or hybrid search. Both are low-risk and high-return. Measure changes on a fixed eval set.
*   **Track your pipeline.** Log retrieved chunks, scores, graph paths, and citations for each answer.
*   **Integrate with your framework of choice.**Frameworks like LangChain, LangGraph, or LlamaIndex can help orchestrate advanced RAG pipelines, but the graph-aware pieces come from Neo4j’s ecosystem. 
    *   **LangChain / LangGraph**: Use them for orchestration (e.g., routing sub-questions to the right tool, managing agents, and handling plan → route → act → verify → stop loops). Pair them with Neo4j’s GenAI ecosystem components like [opens in new tab LLM Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/) (to create knowledge graphs) and[opens in new tab Model Context Protocol](https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/) (to connect agents and LLMs to graph queries). Read this [blog post](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/) to learn how to use the[opens in new tab neo4j-advanced-rag template](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-advanced-rag)and host it using LangServe.
    *   **LlamaIndex**: Use Graph Index / Query Engine for path-bounded traversals and sub-question decomposition. Pair graph retrieval with document retrievers, apply post-processors (dedupe, compression), and rerank before generation. Parent-child retrieval or embedding hybrids are especially useful when structure or multi-hop reasoning matters.

*   **Adopt CRAG patterns.** It’s essential for high-stakes domains such as legal, compliance, or support deflection with strict SLAs.
*   **Plan for scale.** Use hybrid indices, approximate‑nearest‑neighbor vector search (ANN), and caching of common queries to cut latency without losing quality. Keep evaluations running as you optimize.

![Image 32: A diagram showing the steps for implementing advanced RAG, including the baseline setup, improvements, framework integration, and the finished advanced RAG pipeline](https://dist.neo4j.com/wp-content/uploads/20251015125205/implementing-advanced-rag-diagram.png)
### Where to Go From Here

Advanced RAG is about steady, incremental improvements across retrieval, context management, and generation (not a single trick).

To get your RAG ship-ready, start with reranking and hybrid search, add query understanding and context distillation, and bring in multi-step reasoning with a knowledge graph. Advanced RAG patterns benefit from graph-based retrieval through improved relevance and explainability. A Neo4j knowledge graph paired with an LLM delivers:

*   **Relevancy:** Obtain more relevant answers compared to just vector searches
*   **Context:** Includes domain-specific, factual, structured knowledge on your subject
*   **Explainability:** Provide the user with more reasoning on how the results were obtained.
*   **Security:** Role-based access control (RBAC) with fine-grained privileges on labels, relationships, and properties.

Learn how to build your first GraphRAG application today with the free guide:

### Essential GraphRAG

Unlock the full potential of RAG with knowledge graphs. Get the definitive guide from Manning, free for a limited time.

[Get My Copy](https://neo4j.com/essential-graphrag/?utm_medium=Website&utm_source=Blog&utm_campaign=PCGenAI_CCGraphRAG&utm_content=CNAdvancedRAGTechniques)

[![Image 33](https://dist.neo4j.com/wp-content/uploads/20250715075432/Essential-GraphRAG.png)](https://neo4j.com/essential-graphrag/)

## Advanced RAG: FAQs

****What are some advanced RAG techniques?****
If your basic pipeline still hallucinates or misses exact identifiers, you need techniques that get more precise results, keep structure, and keep answers grounded.

Start with hybrid retrieval (vector + keyword), metadata filtering, reranking, and structure‑aware chunking/parent‑doc. Then, layer summarization, query expansion/HyDE, multi‑step reasoning, grounding/CRAG, and retrieval‑based memory as needed.

****How do advanced RAG techniques improve accuracy in complex queries?****
Complex questions fail when retrieval lacks coverage and the model guesses. These methods raise recall and precision while keeping grounding in place. Hybrid + expansion finds the right docs, reranking and parent‑doc/summarization surface the right passages, and CRAG catches weak evidence before you answer.

****What role do knowledge graphs play in enhancing RAG systems?****
A knowledge graph unifies scattered documents, tables, and APIs into a connected picture of your data. With entities and relationships mapped out, GraphRAG retrieves along those connections, improving disambiguation, supporting multi-hop answers, and keeping sources traceable.

*   [llm](https://neo4j.com/blog/tag/llm/)
*   [rag](https://neo4j.com/blog/tag/rag/)

## Share Article

*   [opens in new tab](https://www.linkedin.com/shareArticle?mini=true&url=https://neo4j.com/blog/genai/advanced-rag-techniques/)
*   [opens in new tab](https://twitter.com/intent/tweet?url=https://neo4j.com/blog/genai/advanced-rag-techniques/&text=)
*   [opens in new tab](https://www.facebook.com/sharer/sharer.php?u=https://neo4j.com/blog/genai/advanced-rag-techniques/)

[![Image 34](https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1.jpg)](https://neo4j.com/product/auradb/)

[opens in new tab![Image 35](https://dist.neo4j.com/wp-content/uploads/20250430121707/GA.jpg)](https://graphacademy.neo4j.com/)

[![Image 36](https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub.jpg)](https://neo4j.com/videos/)

## Explore

*   [Knowledge Graph](https://neo4j.com/blog/knowledge-graph/)
*   [Supply Chain & Logistics](https://neo4j.com/blog/supply-chain-and-logistics/)
*   [Fraud Detection](https://neo4j.com/blog/fraud-detection/)
*   [Graph Visualization](https://neo4j.com/blog/graph-visualization/)
*   [AuraDB](https://neo4j.com/blog/auradb/)
*   [Digital Twin](https://neo4j.com/blog/digital-twin/)

* * *

## Related Articles

![Image 37](https://dist.neo4j.com/wp-content/uploads/20260429113617/1_SIlEBcf12oJTiLl7O2mLTA-scaled.webp)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Building Stateful AI: Integrating Aura Agent Lifecycle with MCP and Persistent Memory

[16 min read](https://neo4j.com/blog/genai/building-stateful-ai-integrating-aura-agent-lifecycle-with-mcp-and-persistent-memory/)

![Image 38: GraphAcademy content is moved into Neo4j Aura, and an Aura Agent used to provide MCP server access to VS Code, Cursor, and Claude agents.](https://dist.neo4j.com/wp-content/uploads/20260423023749/architecture-1.png)

*   [Agentic AI](https://neo4j.com/blog/agentic-ai/)
*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Can I use Aura Agents to create an MCP enabled Teacher?

[8 min read](https://neo4j.com/blog/agentic-ai/can-i-use-aura-agents-to-create-an-mcp-enabled-teacher-2/)

![Image 39](https://dist.neo4j.com/wp-content/uploads/20260428043330/1l-xaXyrUxRdmeHIqDz_AFg.png)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Integrating Neo4j with Google Genkit: A Practical Guide

[21 min read](https://neo4j.com/blog/genai/integrating-neo4j-with-google-genkit-a-practical-guide/)

![Image 40](https://dist.neo4j.com/wp-content/uploads/20260428073514/1_cAfpQlomN-Qhc-_f1pCnpg-scaled.webp)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## From Identity Vacuum to Identity Driven Access Control: Securing LLM Agents in the Enterprise

[14 min read](https://neo4j.com/blog/genai/from-identity-vacuum-to-identity-driven-access-control-securing-llm-agents-in-the-enterprise/)

![Image 41](https://dist.neo4j.com/wp-content/uploads/20260424114421/1NOQlmK8z8sP1FDUEYkraQw.png)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Amnesia Is All You Need

[15 min read](https://neo4j.com/blog/developer/amnesia-is-all-you-need/)

![Image 42: Architecting Graph-Based Agentic System: When a Regulator Asks “Why Was This Loan Approved?”](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-2.jpg)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Architecting Graph-Based Agentic System: When a Regulator Asks “Why Was This Loan Approved?”

[11 min read](https://neo4j.com/blog/developer/architecting-graph-based-agentic-system-when-a-regulator-asks-why-was-this-loan-approved/)

![Image 43](https://dist.neo4j.com/wp-content/uploads/20230921083327/homepage-viz_ART-left.svg)![Image 44](https://dist.neo4j.com/wp-content/uploads/20230921083329/homepage-viz_ART-right.svg)![Image 45](https://dist.neo4j.com/wp-content/uploads/20230921082858/homepage-viz_left-side-art_375.svg)![Image 46](https://dist.neo4j.com/wp-content/uploads/20230921082910/homepage-viz_right-side-art_375.svg)

## Build Intelligent Apps Easily

Transform your data into knowledge to build smart, accurate, and adaptive applications.

[Start Building](https://neo4j.com/product/auradb/)

Products

*   [Neo4j AuraDB](https://neo4j.com/product/auradb/)
*   [Neo4j Graph Database](https://neo4j.com/product/neo4j-graph-database/)
*   [Neo4j Graph Analytics](https://neo4j.com/product/aura-graph-analytics/)
*   [Neo4j Graph Data Science](https://neo4j.com/product/graph-data-science/)
*   [Neo4j Fleet Manager](https://neo4j.com/product/fleet-manager/)
*   [Neo4j Bloom](https://neo4j.com/product/bloom/)
*   [Cypher Query Language](https://neo4j.com/product/cypher-graph-query-language/)
*   [Neo4j GraphQL](https://neo4j.com/product/graphql-library/)
*   [Pricing](https://neo4j.com/pricing/)
*   [Neo4j Community Edition](https://neo4j.com/product/community-edition/)

Use Cases

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   [Generative AI](https://neo4j.com/generativeai/)
*   [Knowledge Graphs](https://neo4j.com/use-cases/knowledge-graph/)
*   [Pattern Matching](https://neo4j.com/use-cases/pattern-matching/)
*   [Industries & Use Cases](https://neo4j.com/use-cases/)
*   [Case Studies](https://neo4j.com/customer-stories/)

Developers

*   [Developer Home](https://neo4j.com/developer/)
*   [Documentation](https://neo4j.com/docs/)
*   [Deployment Center](https://neo4j.com/deployment-center/)
*   [Developer Blog](https://neo4j.com/blog/developer/)
*   [opens in new tab Community](https://community.neo4j.com/)
*   [Virtual Events](https://neo4j.com/events/)
*   [opens in new tab GraphAcademy](https://graphacademy.neo4j.com/)
*   [Release Notes](https://neo4j.com/release-notes/)

Data Scientists

*   [Graph Data Science Home](https://neo4j.com/product/graph-data-science/)
*   [Data Science Documentation](https://neo4j.com/docs/graph-data-science/current/)
*   [Get Started with Graph Data Science](https://neo4j.com/graph-data-science-software/)
*   [opens in new tab Data Science Community](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/73)
*   [opens in new tab GraphAcademy for Data Science](https://graphacademy.neo4j.com/categories/data-scientist/)

Learn

*   [Resource Library](https://neo4j.com/resources/)
*   [Neo4j Blog](https://neo4j.com/blog/)
*   [opens in new tab GraphAcademy](https://graphacademy.neo4j.com/)
*   [Research Center](https://neo4j.com/research/)
*   [Case Studies](https://neo4j.com/customer-stories/)
*   [Neo4j Video Hub](https://neo4j.com/videos/)
*   [Neo4j Events Hub](https://neo4j.com/events/)
*   [GraphSummit](https://neo4j.com/graphsummit/)
*   [NODES](https://neo4j.com/nodes-2025/)
*   [Webinars](https://neo4j.com/webinars/)
*   [opens in new tab GraphRAG](https://graphrag.com/)

Partners

*   [Find a Partner](https://neo4j.com/partners/directory/)
*   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
*   [Solution Partners](https://neo4j.com/partners/solution-partners/)
*   [OEM Partners](https://neo4j.com/partners/oem-partners/)
*   [Technology Partners](https://neo4j.com/partners/technology-partners/)
*   [opens in new tab Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

Company

*   [About Us](https://neo4j.com/company/)
*   [Newsroom](https://neo4j.com/news/)
*   [Awards and Honors](https://neo4j.com/awards/)
*   [Graphs4Good](https://neo4j.com/graphs4good/)
*   [Careers](https://neo4j.com/careers/)
*   [Culture](https://neo4j.com/culture/)
*   [Leadership](https://neo4j.com/leadership/)
*   [opens in new tab Support](https://support.neo4j.com/s/)
*   [opens in new tab Trust Center](https://trust.neo4j.com/)

[Contact Us →](https://neo4j.com/contact-us/?ref=footer)

*   US: [1-855-636-4532](tel:1-855-636-4532)
*   Sweden: [+46 171 480 113](tel:+46 171 480 113)
*   UK: [+44 20 3868 3223](tel:+44 20 3868 3223)
*   France: [+33 (0) 1 88 46 13 20](tel:+33 (0) 1 88 46 13 20)
*   Singapore: [+65 6859 0336](tel:+65 6859 0336)
*   Australia: [+61 2 8395 2895](tel:+61 2 8395 2895)
*   India: [+91 6827 521 210](tel:+91 6827 521 210)

Social Networks

[opens in new tab](https://www.linkedin.com/company/neo4j)[opens in new tab](https://x.com/neo4j)[opens in new tab](https://youtube.com/neo4j)[opens in new tab](https://www.facebook.com/neo4j.graph.database)[opens in new tab](https://community.neo4j.com/)[opens in new tab](https://github.com/neo4j)

© 2026 Neo4j, Inc. 

[Terms](https://legal.neo4j.com/#website-terms-of-use) | [Privacy Notice](https://neo4j.com/legal-terms/privacy-notice/) | [Sitemap](https://neo4j.com/sitemap/)

[opens in new tab Anti-Corruption Policy](https://assets.neo4j.com/Neo4j_Anti-Corruption_Policy.pdf)

 ©2026 Neo4j, Inc., Neo Technology®, Neo4j®, Cypher®, Neo4j Bloom™, Neo4j Graph Data Science Library™, Neo4j® Aura™, and Neo4j® AuraDB™ are registered trademarks or a trademark of Neo4j, Inc. All other marks are owned by their respective companies. 

[![Image 47](https://dist.neo4j.com/wp-content/uploads/20210608133508/icon-tooltip-info.svg) Contact Us](https://neo4j.com/contact-us/)

[](https://neo4j.com/blog/genai/advanced-rag-techniques/)![Image 48](blob:https://neo4j.com/e3cf7807-c2bf-41de-8123-dca7cb4be3c2)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="jina-scraped-3.md">
<details>
<summary>RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/>

Title: RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact

URL Source: https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/

Published Time: 2025-03-27T00:58:44+00:00

Markdown Content:
# RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact

[Skip to content](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/#content)

[Madrona](https://www.madrona.com/)

*   [Search](https://www.madrona.com/search/)
*   [About](https://www.madrona.com/about/)
*   [Team](https://www.madrona.com/team/?show=investors)
*   [Companies](https://www.madrona.com/companies/)
    *   [All](https://www.madrona.com/companies/)
    *   [AI & Intelligent Apps](https://www.madrona.com/companies/ai-intelligent-apps/)
    *   [AI-Enabled Biotech](https://www.madrona.com/companies/ai-enabled-biotech/)
    *   [Consumer & Marketplace](https://www.madrona.com/companies/consumer-marketplace/)
    *   [Data & Infrastructure](https://www.madrona.com/companies/data-infrastructure/)
    *   [Deep Tech](https://www.madrona.com/companies/deep-tech/)
    *   [Developer Platforms & Tools](https://www.madrona.com/companies/developer-platforms-tools/)
    *   [Enterprise Apps](https://www.madrona.com/companies/enterprise-apps/)
    *   [Security](https://www.madrona.com/companies/security/)
    *   [Startup Careers](https://jobs.madrona.com/companies)

*   [Insights](https://www.madrona.com/insights/)
*   [Contact](https://www.madrona.com/contact/)
*   [Jobs](https://jobs.madrona.com/)
*   [Search](https://www.madrona.com/search/)

[All](https://www.madrona.com/insights/)

[Madrona News](https://www.madrona.com/insights/?show=madrona-news)

[Perspectives](https://www.madrona.com/insights/?show=perspectives)

[Podcasts](https://www.madrona.com/insights/?show=podcast)

 March 26, 2025 

# RAG Inventor Talks Agents, Grounded AI, and Enterprise Impact

**Listen on****[Spotify](https://open.spotify.com/episode/3MFiVzSmareh99PvFev2Ea?si=Q9dXZTPRQumqenskCG_yFw), [Apple](https://podcasts.apple.com/us/podcast/rag-inventor-talks-agents-grounded-ai-and-enterprise/id1474740843?i=1000701044681), and [Amazon](https://music.amazon.com/podcasts/00017071-4e59-4132-9d9c-4398ca4beee1/episodes/1148788d-54b1-4864-aef9-9df57c58e299/founded-funded-rag-inventor-talks-agents-grounded-ai-and-enterprise-impact) | Watch on [YouTube](https://www.youtube.com/watch?v=k-R0vY6JJU0)**

From the invention of RAG to how it evolved beyond its early use cases, and why the future lies in RAG 2.0, RAG agents, and system-level AI design, this week’s episode of Founded & Funded is a must-listen for anyone building in AI. Madrona Partner Jon Turow sits down with Douwe Kiela, the co-creator of Retrieval Augmented Generation and co-founder of Contextual AI, to unpack:

*   Why RAG was never meant to be a silver bullet — and why it still gets misunderstood
*   The false dichotomies of RAG vs. fine-tuning and long-context
*   How enterprises should evaluate and scale GenAI in production
*   What makes a problem a “RAG problem” (and what doesn’t)
*   How to build enterprise-ready AI infrastructure that actually works
*   Why hallucinations aren’t always bad (and how to evaluate them)
*   And why he believes now is the moment for RAG agents

Whether you’re a builder, an investor, or an AI practitioner, this is a conversation that will challenge how you think about the future of enterprise AI.

* * *

_This transcript was automatically generated and edited for clarity._

**Jon**: So Douwe, take us back to the beginning of RAG. What was the problem that you were trying to solve when you came up with that?

**Douwe**: The history of the RAG project, we were at Facebook AI Research, obviously, FAIR, and I had been doing a lot of work on grounding already for my PhD thesis, and grounding, at the time, really meant understanding language with respect to something else. It was like if you want to know the meaning of the word cat, like the embedding, word embedding of the word cat, this was before we had sentence embeddings, then ideally, you would also know what cats look like because then you understand the meaning of cat better. So that type of perceptual grounding was something that a lot of people were looking at at the time. Then I was talking with one of my PhD students, Ethan Perez, about, “Can we ground it in something else? Maybe we can ground in other text instead of in images.” The obvious source at the time to ground in was Wikipedia.

We would say, “This is true, sort of true,” and then you can understand language with respect to that ground truth. That was the origin of RAG. Ethan and I were looking at that, and then we found that some folks in London had been working on open-domain question answering, mostly Sebastian Riedel and Patrick Lewis, and they had amazing first models in that space and it was a very interesting problem, how can I make a generative model work on any type of data and then answer questions on top of it? We joined forces there. We happened to get very lucky at the time because the people at the Facebook AI Image Similarity Search, I think is what it stands for, basically, the first vector database, but it was just there. And so we were like — we have to take the output from the vector database, give it to a generative model. This is before we called it language models, Then the language model can generate answers grounded on the things you retrieve. And that became RAG.

We always joke with the folks who were on the original paper that we should have come up with a much better name than that, but somehow, it stuck. This was by no means the only project that was doing this, there were people at Google working on very similar things, like REALM is an amazing paper from around the same time. Why RAG, I think, stuck was because the whole field was moving towards gen AI, and the G in RAG stands for generative. We were really the first ones to show that you could make this combination of a vector database and a generative model actually work.

**Jon:**There’s an insight in here that RAG, from its very inception, was multimodal. You were starting with image grounding, and things like that, and it’s been heavily language-centric in the way people have applied it. But from that very beginning place, were you imagining that you were going to come back and apply it with images?

**Douwe:**We had some papers from around that time. There’s a paper we did with more applied folks in Facebook where we were looking at, I think it was called Extra, and it was basically RAG but then on top of images. That feels like a long time ago now, but that was always very much the idea, is you can have arbitrary data that is not captured by the parameters of the generative model, and you can do retrieval over that arbitrary data to augment the generative model so that it can do its job. It’s all about the context that you give it.

**Jon:**Well, this takes me back to another common critique of these early generative models that, for the amazing Q&A that they were capable of, the knowledge cutoff was really striking, you’ve had models in 2020 and 2021 that were not aware of COVID-19, that obviously was so important to society. Was that part of the motivation? Was that part of the solve, that you can make these things fresher?

Douwe:

Yeah, it was part of the original motivation. That is what grounding is, the vision behind the original RAG project. We did a lot of work after that on that question as well, can I have a very lightweight language model that basically has no knowledge, it’s very good at reasoning and speaking English or any language, but it knows nothing? It has to rely completely on this other model, the retriever, which does a lot of the heavy lifting to ensure that the language model has the right context, but that they really have separate responsibilities. Getting that to work turned out to be quite difficult.

Jon:

Now, we have RAG, and we still have this constellation of other techniques, we have training, and we have tuning, and we have in-context learning, and that was, I’m sure, very hard to navigate for research labs, let alone enterprises. In the conception of RAG, in the early implementations of it, what was in your head about how RAG was going to fit into that constellation? Was it meant to be standalone?

**Douwe:**It’s interesting because the concept of in-context learning didn’t really exist at the time, that really became a thing with GPT-3, and that’s an amazing paper and proof point that that actually works, and I think that unlocked a lot of possibilities. In the original RAG paper, we have a baseline, what we call the frozen baseline, where we don’t do any training and we give it as context, that’s in table six, and we showed that it doesn’t really work, or at least, that you can do a lot better if you optimize the parameters. In-context learning is great, but you can probably always beat it through machine learning if you are able to do that. If you have access to the parameters, which is, obviously, not the case with a lot of these black box frontier language models, but if you have access to the parameters and you can optimize them for the data you’re working on or the problem you’re solving, then at least, theoretically, you should always be able to do better.

I see a lot of false dichotomies around RAG. The one I often hear is it’s either RAG or fine-tuning. That’s wrong, you can fine-tune a RAG system and then it would be even better. The other dichotomy I often hear is it’s RAG or long-context. Those are the same thing, RAG is a different way to solve the problem where you have more information than you can put in the context. One solution is to try to grow the context, which doesn’t really work yet even though people like to pretend that it does, the other is to use information retrieval, which is pretty well established as a computer science research field, and leverage all of that and make sure that the language model can do its job. I think things get oversimplified where it’s like, “You should be doing all of those things. You should be doing RAG, you should have a long-context window as long as you can get, and you should fine-tune that thing.” That’s how you get the best performance.

**Jon:**What has happened since then is that, and we’ll talk about how this is all getting combined in more sophisticated ways today, but I think it’s fair to say that in the past 18, 24, 36 months, RAG has caught fire and even become misunderstood as the single silver bullet. Why do you think it’s been so seductive?

**Douwe:**It’s seductive because it’s easy. Honestly, I think long-context is even more seductive if you’re lazy, because then you don’t even have to worry about the retrieval anymore, the data, you put it all there and you pay a heavy price for having all of that data in the context. Every single time you’re answering a question about Harry Potter, you have to read the whole book in order to answer the question, which is not great. So RAG is seductive, I think, because you need to have a way to get these language models to work on top of your data. In the old paradigm of machine learning, we would probably do that in a much more sophisticated way, but because these frontier models are behind black box APIs and we have no access to what they’re actually doing, the only way to really make them do the job on your data is to use retrieval to augment them. It’s a function of what the ecosystem has looked like over the past two years since ChatGPT.

**Jon:**We’ll get to the part where we’re talking about how you need to move beyond a cool demo, but I think the power of a cool demo should not be underestimated, and RAG enables that. What are some of the aha moments that you see with enterprise executives?

**Douwe:**There are lots of aha moments, I think that’s part of the joy of my job. I think it’s where you get to show what this can do, and it’s amazing what these models can do. So basic aha moments for us, is accuracy is almost kind of table stakes at this point. It’s like, okay, you have some data, it’s like one document, you can probably answer lots of questions about that document pretty well. It becomes much harder when you have million documents or tens of millions of documents and they’re all very complicated or they have very specific things in them. We’ve worked with Qualcomm and they’re like circuit design diagrams inside those documents, it’s much harder to make sense of that type of information. The initial wow factor, at least from people using our platform, is that you can stand this up in a minute. I can build a state-of-the-art RAG agent in three clicks basically.

That time of value used to be very difficult to achieve, because you had your developers, they have to think about the optimal chunking strategy for the documents, and things that you really don’t want your developers thinking about but they had to because the technology was so immature. The next generation of these systems and platforms for building these RAG agents is going to enable developers to think much more about business value and differentiation essentially, “How can I be better than my competitors because I’ve solved this problem so much better?” Your chunking strategy should not be important for solving that problem.

**Jon:**Also, if I now connect what we were just talking about to what you said now, the seduction of long-context and RAG are that it’s straightforward and easy, and it plugs into my existing architecture. As a CTO, if I have finite resources to go implement new pieces of technology, let alone dig into concepts like chunking strategies, and how the vector similarity for non-dairy will look similar to the vector similarity for milk, things like this, is it fair to say that CTOs are wanting something coherent, that can be something that works out of the box?

**Douwe:**You would think so, and that’s probably true for CTOs, and CIOs, and CAIOs, and CDOs, and the folks who are thinking about it from that level. But then what we often find is that we talk to these people and they talk to their architects and their developers, and those developers love thinking about chunking strategies, because that’s what it means in a modern era, to be an AI engineer is to be very good at prompt engineering and evaluation and optimizing all the different parts of the RAG stack. It’s very important to have the flexibility to play with these different strategies, but you need to have very, very good defaults so that these people don’t have to do that unless they really want to squeeze the final percent, and then they can do that.

That’s what we are trying to offer, is you don’t have to worry about all this basic stuff, you should be thinking about how to really use the AI to deliver value. It’s really a journey. The maturity curve is very wide and flat. It’s like some companies are figuring it out, it’s like, “What use case should I look at?” And others have a full-blown RAG platform that they built themselves based on completely wrong assumptions for where the field is going to go, and now, they’re stuck in this paradigm, it’s all over the place, which means it’s still very early in the market.

**Jon:**Take me through some of the milestones on that maturity curve, from the cool demo all the way through to the ninja level results.

**Douwe:**The timeline is, 2023 was the year of the demo, ChatGPT had just happened, everybody was playing with it, there was a lot of experimental budget, last year has been about trying to productionize it, and you could probably get promoted if you were in a large enterprise, if you were the first one to ship genAI into production. There’s been a lot of kneecapping of those solutions happening in order to be the first one to get it into production.

**Jon:**First-pass-the-post.

**Douwe:**First-pass-the-post, but in a limited way, because it is very hard to get the real thing past the post. This year, people are really under a lot of pressure to deliver return on investment for all of those AI investments and all of the experimentation that has been happening. It turns out that getting that ROI is a very different question, that’s where you need a lot of deep expertise around the problem, but also you need to have better components that exist out there in an open source easy framework for you to cobble together a Frankenstein RAG solution, that’s great for the demo, but that doesn’t scale.

**Jon:**Our customers think about the ROI, how do they measure, perceive that?

**Douwe:**It really depends on the customer. Some are very sophisticated, trying to think through the metrics, like, “How do I measure it? How do I prioritize it?” I think a lot of consulting firms are trying to be helpful there as well, thinking through, “Okay, this use case is interesting, but it touches 10 people. They’re very highly specialized, but we have this other use case that has 10,000 people. They’re maybe slightly less specialized, but there’s much more impact there.” It’s a trade-off. I think my general stance on use case adoption is that I see a lot of people aiming too low, where it’s like, “Oh, we have AI running in production.” It’s like, “Oh, what do you have?” It’s like, “Well, we have something that can tell us who our 401(k) provider is, and how many vacation days I get.”

And that’s nice, “Is that where you get the ROI of AI from?” Obviously not, you need to move up in terms of complexity, or if you think of the org chart of the company, you want to go for this specialized roles where they have really hard problems, and if you can make them 10, 20% more effective at that problem, you can save the company tens or hundreds of millions of dollars by making those people better at their job.

**Jon:**There’s an equation you’re getting at, which is the complexity, sophistication of the work being done times the number of employees that it impacts.

**Douwe:**There’s roughly two categories for gen AI deployment, one is cost savings. So I have lots of people doing one thing, if I make all of them slightly more effective, then I can save myself a lot of money. The other is more around business transformation and generating new revenue. That second one is obviously much harder to measure, and you need to think through the metrics, like, “What am I optimizing for here?” As a result of that, I think you see a lot more production deployments in the former category where it’s about cost-saving.

**Jon:**What are some big misunderstandings that you see around what the technology is or is not capable of?

**Douwe:**I see some confusion around the gap between demo and production. A lot of people think that, “Oh, yeah, it’s great, I can easily do this myself.” Then it turns out that everything breaks down after a hundred documents, and they have a million. That is the most common one that we see. There are other misconceptions maybe around what RAG is good for and what it’s not.What is a RAG problem and what is not a RAG problem? People don’t have the same mental model that maybe AI researchers like myself have, where if I give them access to a RAG agent, often, the first question they ask is, “What’s in the data?” That is not a RAG problem, or it’s a RAG problem on the metadata, it’s not on the data in itself. A RAG question would be like, what was, I don’t know, Meta’s R&D expense in Q4 or 2024, and how did it compare to the previous year? Something like that.

It’s a specific question where you can extract the information and then reason over it and synthesize that different information. A lot of questions that people like to ask are not RAG problems. It’s like, summarize the document is another one. Summarization is not a RAG problem. Ideally, you want to put the whole document in a context and then summarize it. There are different strategies that work well for different questions, and why ChatGPT is such a great product is because they’ve abstracted away some of those decisions that go into it, but that’s still very much happening under the surface. I think people need to understand better what type of use case they have. If I’m a Qualcomm customer engineer and I need very specific answers to very specific questions, that’s very clearly a RAG problem. If I need to summarize the document, put that in context of a long-context model.

**Jon:**Now, we have Contextual, which is an amalgamation of multiple techniques, and you have what you call RAG 2.0, and you have fine-tuning, and there’s a lot of things that happen under the covers that customers ideally don’t have to worry about until they choose to do so. I expect that changes radically the conversation you have with an enterprise executive. How do you describe the kinds of problems that they should go find and apply and prioritize?

**Douwe:**We often help people with use case discovery. So, thinking through, okay, what are the RAG problems, what are maybe not RAG problems? Then for the RAG problems, how do you prioritize them? How do you define success? How do you come up with a proper test set so that you can evaluate whether it actually works? What is the process for, after that, doing what we call UAT, user acceptability testing. Putting it in front of real people, that’s really the thing that matters, right? Sometimes, we see production deployments, and they’re in production, and then I ask them, “How many people use this?” And the answer is zero. During the initial UAT, everything was great and everybody was saying, “Oh, yeah, this is so great.” Then when your boss asks you the question and your job is on the line, then you do it yourself, you don’t ask AI in that particular use case. It’s a transformation that a lot of these companies still have to go through.

**Jon:**Do the companies want support through that journey today, either direct for Contextual or from a solution partner, to get such things implemented?

**Douwe:**It’s very tempting to pretend that AI products are mature enough to be fully self-serve and standalone. It’s decent if you do that, but in order to get it to be great, you need to put in the work. We do that for our customers or we can also work through systems integrators who can do that for us.

**Jon:**I want to talk about two sides of the organization that you’ve had to build in order to bring all this for customers. One is scaling up the research and engineering function to keep pushing the envelope. There are a couple of very special things that Contextual has, something you call RAG 2.0, something you call active versus passive retrieval. Can you talk about some of those innovations that you’ve got inside Contextual and why they’re important?

**Douwe:**We really want to be a frontier company, but we don’t want to train foundation models. Obviously, that’s a very, very capital intensive business, I think language models are going to get commoditized. The really interesting problems are around how do you build systems around these models that solve the real problem? Most of the business problems that we encounter, they need to be solved by a system. Then there are a ton of super exciting research problems around how do I get that system to work well together? That’s what RAG 2.0 is in our case, how do you jointly optimize these components so that they can work well together? There’s also other things like making sure that your generations are very grounded. It’s not a general language model, it’s a language model that has been trained specifically for RAG and RAG only. It’s not doing creative writing, it can only talk about what’s in the context.

Similarly, when you build these production systems, you need to have a state-of-the-art re-ranker. Ideally, that re-ranker can also follow instructions. It’s a smarter model. There’s a lot of innovative stuff that we’re doing around building the RAG pipeline better and then how you incorporate feedback into that RAG pipeline as well. We’ve done work on KTO, and APO, and things like that, so different ways to incorporate human preferences into entire systems and not just models. That takes a very special team, which we have, I’m very proud of.

**Jon:**Can you talk about active versus passive retrieval?

**Douwe:**Passive retrieval is basically old-school RAG. It’s like I get a query, and I always retrieve, and then I take the results of that retrieval, and I give them to the language model, and it generates. That doesn’t really work. Very often, you need the language model to think, first of all, where am I going to retrieve it from and how am I going to retrieve it? Are there maybe better ways to search for the thing I’m looking for than copy and pasting the query? Modern production RAG pipelines are already way more sophisticated than having a vector database and a language model. One of the interesting things that you can do in the new paradigm of agentic things and test-time reasoning is decide for yourself if you want to retrieve something. It’s active retrieval. It’s like if you give me a query like, “Hi, how are you?” I don’t have to retrieve in order to answer that. I can just say, “I’m doing well, how can I help you?”

Then you ask me a question and now I decide that I need to go and retrieve. Maybe I make a mistake with my initial retrieval, so then I need to go and think like, “Oh, actually, maybe I should have gone here instead.” That’s active retrieval, that’s all getting unlocked now. This is what we call RAG agents, and this really is the future, I think, because gents are great, but we need a way to get them to work on your data, and that’s where RAG comes in.

**Jon:**This implies two uses of two relationships of Contextual and RAG to the agent, there is the supplying of information to the agents so that it can be performant, but if I probe into what you said, active retrieval implies a certain kind of reasoning, maybe even longer reasoning about, “Okay, what is the best source of the information that I’ve been asked to provide?”

**Douwe:**Exactly. It’s like I enjoy saying everything is Contextual. That’s very true for an enterprise. So the context that the data exists in, that really matters for the reasoning that the agent does in terms of finding the right information that all comes together in these RAG agents.

**Jon:**What is a really thorny problem that you’d like your team and the industry to try and attack in the coming years?

**Douwe:**The most interesting problems that I see everywhere in enterprises are at the intersection of structured and unstructured. We have great companies working on unstructured data, there are great companies working on structured data, but once you have the capability, which we’re starting to have now, where you can reason over both of these very different data modalities using the same model, then that unlocks so many cool use cases. That’s going to happen this year or next year, just thinking through the different data modalities and how you can reason on top of all of them with these agents.

**Jon:**Will that happen under the covers with one common piece of infrastructure or will it be a coherent single pane of glass across many different Lego bricks?

**Douwe:**I’d like to think that it would be one solution, and that is our platform, which can do all of that.

**Jon:**Let’s imagine that, but behind the covers, will you be accomplishing that with many different components each handling the structured versus unstructured?

**Douwe:**They are different components, despite what some people maybe like to pretend, I can always train up a better text-to-SQL model if I specialize it for text-to-SQL, than taking a generic off-the-shelf language model and telling it, “Generate some SQL query.” Specialization is always going to be better than generalization for specific problems, if you know what the problem is that you’re solving, the real question is much more around is it worth actually investing the money to do that? It costs money to specialize and it sometimes hampers economies of scale that you might want to have.

**Jon:**If I look at the other side of your organization that you’ve had to build, so you’ve had to build a very sophisticated research function, but Contextual is not a research lab, it’s a company, so what are the other kinds of disciplines and capabilities you’ve had to build up at Contextual that complement all the research that’s happening here?

**Douwe:**First of all, I think our researchers are really special in that we’re not focused on publishing papers or being too far out on the frontier. As a company, I don’t think you can afford that until you’re much bigger, and if you’re like Zuck and you can afford to have FAIR. The stuff I was working on at FAIR, at the time, I was doing like Wittgensteinian language games and all kinds of crazy stuff that I would never let people do here, honestly. But there’s a place for that, and that’s not a startup. The way we do research is we’re very much looking at what the customer problems are that we think we can solve better than anybody else, and then focusing, thinking from the system’s perspective about all of these problems, how can we make sure that we have the best system and then make that system jointly optimized and really specialized, or specializable, for different use cases? That’s what we can do.

That means that it’s a very fluid boundary between pure research and applied research, basically. All of our research is applied. In AI, right now, I think there’s a very fine line between product and research, where the research is basically is the product, and that’s not true for us, I think it’s true for OpenAI, Anthropic, everybody. The field is moving so quickly that you have to productize research almost immediately. As soon as it’s ready, you don’t even have time to write a paper about it anymore, you have to ship it into product very quickly because it is such a fast moving space.

**Jon:**How do you allocate your research attention? Is there some element of play, even 5%, 10%?

**Douwe:**The team would probably say not enough.

**Jon:** But not zero?

**Douwe:**As a researcher, you always want to play more but you have limited time. So yeah, it’s a trade-off, I don’t think we’re officially committing. We don’t have a 20% rule or something like Google would have, it’s more like we’re trying to solve cool problems as quickly as we can, and hopefully, have some impact on the world. Not work in isolation, but try to focus on things that matter.

**Jon:**I think I’m hearing you say that it’s zero even in an environment with finite resources and moving fast?

**Douwe:**Every environment has finite resources. It’s more like if you want to do special things, then you need to try new stuff. That’s, I think, very different for AI companies or AI native companies like us. If you compare this generation of companies with SaaS companies, there is like, okay, all the LAMP stack, everything was already there, you have to basically go and implement it. That’s not the case here, is we’re very much figuring out what we’re doing, like flying the airplane as we’re building it sort of thing, which is exciting, I think.

**Jon:**What is it like to now take this research that you’re doing and go out into the world and have that make contact with enterprises? What has that been like for you personally, and what has that been like for the company to transform from research-led to a product company?

**Douwe:**That’s my personal journey as well. I started off, I did a PhD, I was very much a pure research person and slowly transitioned to where I am now, where the key observation is that the research is the product. This is special point in time, it’s not going to always be like that. That’s been a lot of fun, honestly, I’ve been on a podcast a while back and they asked me, “What other job would you think is interesting?” And I said, “Maybe being the head of AI of JP Morgan.” And they were like, “Really?”

And I was like, “Well, I think actually, right now, at this particular point in time, that is a very interesting job.” And because you have to think about how am I going to change this giant company to use this latest piece of technology that is frankly going to change everything is going to change our entire society. For me, it gave me a lot of joy talking to people like that and thinking about what the future of the world is going to look like.

**Jon:**I think there’s going to be people problems, and organizational problems, and regulatory and domain constraints that fall outside the paper.

**Douwe:**Honestly, I would argue that those are the main problems to still overcome. I don’t care about AGI and all of those discussions, the core technology is already here for huge economic disruption. All the building blocks are here, the questions are more around how do we get lawyers to understand that? How do we get the MRM people to figure out what is an acceptable risk? One thing that we are very big on is not thinking about the accuracy, but thinking about the inaccuracy, and what do you do, if you have 98% accuracy, what do you do with the remaining 2% to make sure that you can mitigate that risk? A lot of this is happening right now. There’s a lot of change management that we’re going to need to do in these organizations. All of that is outside of the research questions where we have all the pieces to completely disrupt the global economy right now, it’s a question of executing on it, which is scary and exciting at the same time.

**Jon:**Douwe, you and I have had a conversation many times about different archetypes of founders and their capabilities. There’s one lens that stuck with me that has three click stops on it, there is a domain expert, who has expertise in revenue cycle management, but may not be that technical at all, A. B, there is somebody who is technical and able to write code but is not a PhD researcher, and Mark Zuckerberg is a really famous example of that. Then there’s the research founder, who has deep technical capabilities and advanced vision into the frontier. What do you see as the role for each of those types of founders in the next wave of companies that needs to get built?

**Douwe:**That’s a very interesting question. I would argue how many PhDs does Zuck have working for him? That’s a lot, right?

**Jon:**That’s a lot.

**Douwe:**I don’t think it matters how deep your expertise in a specific domain is, as long as you are a good leader and a good visionary, then you can recruit the PhDs to go and work for you. At the same time, obviously, it gives you an advantage if you are very deep in one field and that field happens to take off, which is what happened to me. I got very lucky, with a lot of timing there as well. Overall, one underlying question you’re asking there is around AI wrapper companies, for example. To what extent should companies go horizontal and vertical using this technology?

There’s been a lot of disdain for these wrapper companies like, “Oh, that’s a wrapper for OpenAI.” It’s like, “Well, it turns out you can make an amazing business just from that, right?” I think Cursor is like Anthropic’s biggest customer right now. It’s fine to be a wrapper company as long as you have an amazing business. People should have a lot more respect for companies building on top of fundamental new technology and discovering whole new business problems that we didn’t really knew existed, and then solving them much better than anything else.

**Jon:**Well, so I’m really thinking also about the comment you made, that we have a lot of technology that is capable of a lot of economic impact, even today, without new breakthroughs that, yes, we’ll also get. Does that change the next types of companies that should be founded in the coming year?

**Douwe:**I think so. I am also learning a lot of this myself, about how to be a good founder, basically. It’s always good to plan for what’s going to come and not for what is here right now, and that’s how you get to ride that wave in the right way. What’s going to come is that a lot of this stuff is going to become much more mature. One of the big problems we had even two years ago was that [AI infrastructure](https://www.madrona.com/ai-agent-infrastructure-three-layers-tools-data-orchestration/) was very immature. Everything would break down all the time. There were bugs into attention mechanism, implementation of frameworks we were using, really basic stuff. All of that has been solved now. With that maturity also comes the ability to scale much better, to think much, much more rigorously, I think, around cost quality trade-offs and things like that. There’s a lot of business value just right there.

**Jon:**What do new founders ask you? What kind of advice do they ask you?

**Douwe:**They ask me a lot about this wrapper company thing, and modes, and differentiation. There’s some fear that incumbents are going to eat everything, and so they obviously have amazing distribution. They’re massive opportunities for companies to be AI native and to think from day one as an AI company. If you do that right, then you have a massive opportunity to be the next Google, or Facebook, or whatever, if you play your cards right.

**Jon:**What is some advice that you’ve gotten, and I’ll ask you to break it into two, what is advice that you’ve gotten that you disagree with, and what do you think about that? And then what is advice that you’ve gotten that you take a lot from?

**Douwe:**Maybe we can start with the advice I really like, which is one observation around why Facebook is so successful, it’s like, be fluid like water. It’s like whatever the market is telling you or your users are telling you, fit into that, don’t be too rigorous in what is right and wrong, be humble and look at what the data tells you and then try to optimize for that. That is advice that when I got it, I didn’t really appreciate it fully, and I’m starting to appreciate that much more right now. Honestly, it took me too long to understand that. In terms of advice that I’ve gotten that I disagree with, it’s very easy for people to say, “You should do one thing and you should do it well.” Sure, maybe, but I’d like to be more ambitious than that. We could have been one small part of a RAG stack and we probably would’ve been the best in the world at that particular thing, but then we’re slotting into this ecosystem where we’re a small piece, and I want the whole pie ideally.

Then that’s why we’ve invested so much time in building this platform, making sure that all the individual components are state-of-the-art and that they’ve been made to work together so that you can solve this much bigger problem, but yet, that is also a lot harder to do. Not everyone would give me the advice that I should not go and solve that hard problem, but I think over time, as a company, that is where your moat comes from, doing something that everybody else thinks is kind of crazy. So that would be my advice to founders, is go and do something that everybody else thinks is crazy.

**Jon:**You’re probably going to tell me that that reflects in the team that comes to join you?

**Douwe:**Yeah, the company is the team, especially the early team. We’ve been very fortunate with the people who joined us early on, and that is what the company is. It’s the people.

**Jon:**If I piggyback a little bit and we get back into the technology for a minute, there’s a common question, maybe even misunderstanding that I hear about RAG, that, “Oh, this is the thing that’s going to solve hallucinations.” You and I have spoken about this many times, where is your head at right now on what hallucinations are, what they are not? Does RAG solve it? What’s the outlook there?

**Douwe:**I think hallucination is not a very technical term. We used to have a pretty good word for it, it was accuracy. If you were inaccurate, if you were wrong, then I guess to explain that, or to anthropomorphize it would be to say, “Oh, the model hallucinated.” I think it’s a very ill-defined term, honestly. If I would have to try to turn it into a technical definition, I would say the generation of the language model is not grounded in the context that is given, where it is told that that context is true. Basically, hallucination is about groundedness. If you have a model that adheres to its context, then it will hallucinate less. Hallucination itself is arguably a feature for a general purpose language model, it’s not a bug. If you have a creative writing department, or marketing department, creative writing thing like content generation, I think hallucination is great for that, as long as you have a way to fix it, you probably have a human somewhere double checking it and rewriting some stuff.

So hallucination itself is not even a bad thing necessarily, it is a bad thing if you have a RAG problem though and you cannot afford to make a mistake. Then that’s why we have a grounded language model that has been trained specifically not to hallucinate, or to hallucinate less. Because one other misconception that I sometimes see is that people think that these probabilistic systems can have 100% accuracy, and that is a pipe dream. It’s the same with people. If you look at a big bank, there are people in these banks and people make mistakes too.

**Jon:**SEC filings have mistakes.

**Douwe:**Exactly. The whole reason we have the SEC and that is a regulated market is so that we have mechanisms built into the market so that if a person makes a mistake, then at least we made reasonable efforts to mitigate the risk around that. It’s the same with AI deployments. That’s why I’m talking about how to mitigate the risk with inaccuracies. It’s like, we’re not going to get it to 100%, so you need to think about the 2, 3, 5, 10% depending on how hard the use cases where you might still not be perfect. How do you deal with that?

**Jon:**What are some of the things that you might’ve believed a year ago about AI adoption or AI capabilities that you think very differently about today?

**Douwe:**Many things. The main thing I thought that turned out not to be true was that I thought this would be easy.

**Jon:**What is this?

**Douwe:**Building the company and solving real problems with AI. We were very naive, especially in the beginning of the company. We were like, “Oh, yeah, we just get a research cluster. Get a bunch of GPUs in there. We train some models, it’s going to be great.” Then it turned out that getting a working GPU cluster was very hard. And then it turned out that training something on that GPU cluster in a way that actually works, where if you’re using other people’s code, then maybe that code is not that great yet. Now, you have to build your own framework for a lot of the stuff that you’re doing if you want to make sure that it’s really, really good. We had to do a lot of plumbing that we did not expect to have to do. Now, I’m very happy that we did all that work, but at the time, it was very frustrating.

**Jon:**What are we, either you and I, or we, the industry, not talking about nearly enough that we should be?

**Douwe:**Evaluation. I’ve been doing a lot of work on evaluation in my research career, things like Dynabench where it was about how do we hopefully maybe get rid of benchmarks all together and have a more dynamic way to measure model performance. Evaluation is very boring. People don’t seem to care about it. I care deeply about it, so that always surprises me. We did this amazing launch, I thought, around LMUnit, it’s natural language unit testing. You have a response from a language model, and now you want to check very specific things about that response. It’s like, did it contain this? Did it not make this mistake? Ideally, you can write unit tests as a person for what a good response looks like. You can do that with our approach. We have a model that is by far state-of-the-art at verifying that these unit tests are passing or failing.

I think this is awesome. I love talking about this, but people don’t seem to really care. It’s like, “Oh, yeah, evaluation. Yeah, we have a spreadsheet somewhere with 10 examples.” How is that possible? That’s such an important problem. When you deploy AI, you need to know if it works or not, and you need to know where it falls short, and you need to have trust in your deployment, and you need to think about the things that might go wrong, and all of that. It’s been very surprising to me just how immature a lot of companies are when it comes to evaluation, and this includes huge companies.

**Jon:**[Garry Tan](https://x.com/garrytan) posted on social media not too long ago, that evaluation is the secret weapon of the strongest AI application companies.

**Douwe:** Also, AI research companies, by the way. So OpenAI and Anthropic, part of why they’re so great is because they’re amazing at evaluation too. They know exactly what good looks like. That’s also why we are doing all of that in-house; we’re not outsourcing evaluation to somebody else. It’s like, if you are an AI company and AI is your product, then you can only assess the quality of your product through evaluation. t’s core to all of these companies.

**Jon:**Whoever is lucky enough to get that cool JP Morgan head of AI job that you would be doing in another life, is that intellectual property of JP Morgan what the evals really need to look like, or is this something that they can ultimately ask Contextual to cover for them?

**Douwe:**No. I think the tooling for evaluation, they can use us for, but the actual expertise that goes into that evaluation, the unit tests, they should write that themselves. In the limit, we talked about a company is its people, but in the limit, that might not even be true, because there might be AI mostly, and maybe only a few people. What makes a company a company is its data, and the expertise around that data and the institutional knowledge. That is what defines a company. That should be captured in how you evaluate the systems that you deploy in your company.

**Jon:**I think we can leave it there. Douwe Kiela, thank you so much. This was a lot of fun.

**Douwe:** Thank you.

### Related Insights

 March 25, 2025 

Inside Microsoft’s AI Bet: Satya Nadella on Leadership, Innovation and the Future

 March 11, 2025 |36:14 

Dropzone’s Edward Wu on Solving Security’s Biggest Bottleneck

 February 28, 2025 

by Jon Turow

The AI Agent Infrastructure Stack — Three Defining Layers: Tools, Data, and Orchestration

### Related Insights

 March 25, 2025 

Inside Microsoft’s AI Bet: Satya Nadella on Leadership, Innovation and the Future

 March 11, 2025 |36:14 

Dropzone’s Edward Wu on Solving Security’s Biggest Bottleneck

 February 28, 2025 

by Jon Turow

The AI Agent Infrastructure Stack — Three Defining Layers: Tools, Data, and Orchestration

## Sign up for our newsletter for emerging trends,

insights and new investment news.

### [Seattle](https://www.madrona.com/contact/)[Palo Alto](https://www.madrona.com/contact/)

Sign up for our newsletter

©2026 Madrona Venture Group

[Startup Careers](https://jobs.madrona.com/)

[Linkedin](http://www.linkedin.com/company/madrona-venture-group)

[YouTube](https://www.youtube.com/channel/UCkoghIUl-K-v7MrHTRT54fA)

[Podcast](https://open.spotify.com/show/2ePgKWebuH5XfcoUpSi330)

[Twitter](https://twitter.com/madronaventures)

[Instagram](https://www.instagram.com/Madronaventures/)

[Contact](https://www.madrona.com/contact/)

[LP Login](https://icx.efrontcloud.com/madrona/login.aspx)

[IA40](https://www.ia40.com/)

![Image 1: Madrona logo](https://www.madrona.com/wp-content/uploads/2022/10/Madrona_LockupV_MADGRN_RGB_1000W-300x200.png)

By using this website, you agree to our use of cookies. We use cookies to provide you with a great experience and to help our website run effectively. [Accept](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/) or view our [Privacy Policy](https://www.madrona.com/privacy-policy/)

Privacy & Cookies Policy

Close

#### Privacy Overview

This website uses cookies to improve your experience while you navigate through the website. Out of these, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the ...

[](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)

[Necessary](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)

- [x] Necessary 

Always Enabled

 Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information. 

[Non-necessary](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)

- [x] Non-necessary 

 Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website. 

[SAVE & ACCEPT](https://www.madrona.com/rag-inventor-talks-agents-grounded-ai-and-enterprise-impact/)

Sign up for our newsletter

 ✕

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="jina-scraped.md">
<details>
<summary>Fine-Tuning vs. Retrieval Augmented Generation for LLMs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://neo4j.com/blog/developer/fine-tuning-vs-rag/>

Title: Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation

URL Source: https://neo4j.com/blog/developer/fine-tuning-vs-rag/

Published Time: 2024-09-11T15:00:00+00:00

Markdown Content:
# Fine-Tuning vs. Retrieval Augmented Generation for LLMs

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/blog/developer/fine-tuning-vs-rag/#)[Use necessary cookies only](https://neo4j.com/blog/developer/fine-tuning-vs-rag/#)

[Skip to content](https://neo4j.com/blog/developer/fine-tuning-vs-rag/#skip-to-content "Skip to content")

Complete the [opens in new tab Aura Agents Course](https://graphacademy.neo4j.com/courses/aura-agents/?category=aura) Between Apr 15 - May 15 | The First 500 Win Aura Credits

[![Image 1: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)Menu

![Image 2: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)Search Close Menu

*   [Products](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Back](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   GRAPH DATABASE
    *   [Neo4j AuraDB Fully managed graph database as a service](https://neo4j.com/product/auradb/)
    *   [Neo4j Graph Database Self managed, deploy anywhere graph database](https://neo4j.com/product/neo4j-graph-database/)
    *   GRAPH ANALYTICS
    *   [Neo4j Aura Graph Analytics Fully managed graph analytics as a service](https://neo4j.com/product/aura-graph-analytics/)
    *   [Neo4j Graph Data Science Self managed graph algorithms and ML modeling](https://neo4j.com/product/graph-data-science/)
    *   GRAPH AI
    *   [Neo4j Aura Agent Fully managed knowledge-graph-powered AI agent creation platform](https://neo4j.com/product/aura-agent/)
    *   GRAPH TOOLS
    *   [Neo4j Fleet Manager A single control plane to manage all your DB instances](https://neo4j.com/product/fleet-manager/)
    *   [Neo4j Bloom Easy graph visualization and exploration](https://neo4j.com/product/bloom/)
    *   PARTNER SOLUTIONS
    *   [Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud](https://neo4j.com/neo4j-graph-analytics-snowflake/)
    *   [Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric](https://neo4j.com/neo4j-graph-intelligence-microsoft-fabric/)

*   [Use Cases](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Back](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [AI Systems Back your LLMs with a knowledge graph for better business AI](https://neo4j.com/use-cases/ai-systems/)
    *   [Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more](https://neo4j.com/use-cases/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)

*   [Developers](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Back](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Developer Center Best practices, guides, tutorials, and downloads](https://neo4j.com/developer/)
    *   [opens in new tab GraphAcademy![Image 3](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications. Join the 100K+ Neo4j experts.](https://graphacademy.neo4j.com/)
    *   DEVELOPERS
    *   [Deployment Center Deploy Neo4j on any cloud or architecture](https://neo4j.com/deployment-center/)
    *   [Documentation![Image 4](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [Developer Blog Deep dives into more technical Neo4j topics](https://neo4j.com/blog/developer/)
    *   [opens in new tab Community A global forum for online discussion](https://community.neo4j.com/)
    *   DATA SCIENTISTS
    *   [Data Science Documentation![Image 5](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for the Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/)
    *   [Graph Data Science Home Learn what Neo4j offers for data science](https://neo4j.com/product/graph-data-science/)
    *   [Get Started With Graph Data Science Download or get started in Sandbox today](https://neo4j.com/graph-data-science-software/)
    *   [opens in new tab Data Science Community A global forum for data-driven professionals](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/)

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   [Learn](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Back](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   LEARN
    *   [Documentation![Image 6](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [GraphAcademy![Image 7](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications](https://graphacademy.neo4j.com/)
    *   [Resource Library White papers, datasheets, and more](https://neo4j.com/resources/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)
    *   CONNECT
    *   [Neo4j Events Hub![Image 8](https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg)Live and on-demand events, training, webinars, and demos](https://neo4j.com/events/)
    *   [Neo4j Blog Announcements, guides, and best practices](https://neo4j.com/blog/)
    *   [Neo4j Video Hub Covering graph databases, data science, analytics & AI](https://neo4j.com/videos/)
    *   FEATURED EVENTS
    *   [GraphSummit 2026 Graphs + AI: Transform Your Data Into Knowledge](https://neo4j.com/graphsummit/)
    *   [NODES 2026 | November 12 Virtual Conference: Engineering Better Intelligence](https://neo4j.com/nodes/)

*   [Pricing](https://neo4j.com/pricing/)
*   QUICK LINKS
*   [Partners](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Back](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Find a Partner](https://neo4j.com/partners/directory/)
    *   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
    *   [Solution Partners](https://neo4j.com/partners/solution-partners/)
    *   [OEM Partners](https://neo4j.com/partners/oem-partners/)
    *   [Technology Partners](https://neo4j.com/partners/technology-partners/)
    *   [Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

*   [Company](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [Back](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
    *   [About Us](https://neo4j.com/company/)
    *   [Newsroom](https://neo4j.com/newsroom/)
    *   [Awards and Honors](https://neo4j.com/awards/)
    *   [Graphs4Good](https://neo4j.com/graphs4good/)
    *   [Careers](https://neo4j.com/careers/)
    *   [Culture](https://neo4j.com/culture/)
    *   [Leadership](https://neo4j.com/leadership/)

*   [Support](https://support.neo4j.com/s/)
*   [Aura Login](https://console.neo4j.io/)

[Get Started](https://neo4j.com/product/auradb/?ref=nav-get-started-cta)[Contact Us](https://neo4j.com/contact-us/)

*   [Aura Login](https://console.neo4j.io/)
*   [Partners](https://neo4j.com/partners/)Partners: submenu

    *   [Find a Partner](https://neo4j.com/partners/directory/)
    *   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
    *   [Solution Partners](https://neo4j.com/partners/solution-partners/)
    *   [OEM Partners](https://neo4j.com/partners/oem-partners/)
    *   [Technology Partners](https://neo4j.com/partners/technology-partners/)
    *   [opens in new tab Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

*   Company Company: submenu

    *   [About Us](https://neo4j.com/company/)
    *   [Newsroom](https://neo4j.com/newsroom/)
    *   [Awards and Honors](https://neo4j.com/awards/)
    *   [Graphs4Good](https://neo4j.com/graphs4good/)
    *   [Careers](https://neo4j.com/careers/)
    *   [Culture](https://neo4j.com/culture/)
    *   [Leadership](https://neo4j.com/leadership/)

*   [Support](https://support.neo4j.com/s/)
*   Search

[![Image 9: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)

*   Products Products: submenu

GRAPH DATABASE
    *   [![Image 10: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083548/aura.svg) Neo4j AuraDB Fully managed graph database as a service](https://neo4j.com/product/auradb/)
    *   [![Image 11: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083552/Neo4j_db.svg) Neo4j Graph Database Self managed, deploy anywhere graph database](https://neo4j.com/product/neo4j-graph-database/)

GRAPH ANALYTICS
    *   [![Image 12: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083556/networkmagnifier_chart.svg) Neo4j Aura Graph Analytics Fully managed graph analytics as a service](https://neo4j.com/product/aura-graph-analytics/)
    *   [![Image 13: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083550/Graph_data_science.svg) Neo4j Graph Data Science Self managed graph algorithms and ML modeling](https://neo4j.com/product/graph-data-science/)

GRAPH AI
    *   [![Image 14: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083551/neo4j_aura_agent.svg) Neo4j Aura Agent Fully managed knowledge-graph-powered AI agent creation platform](https://neo4j.com/product/aura-agent/)

 PARTNER SOLUTIONS 

    *   [![Image 15: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083554/Neo4j_on_Fabric.svg) Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric](https://neo4j.com/neo4j-graph-intelligence-microsoft-fabric/)

    *   [![Image 16: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083555/Neo4j_on_Snowflake.svg) Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud](https://neo4j.com/neo4j-graph-analytics-snowflake/)

Graph Tools

    *   [Neo4j Fleet Manager A single control plane to manage all your DB instances](https://neo4j.com/product/fleet-manager/)
    *   [Neo4j Bloom Easy graph visualization and exploration](https://neo4j.com/product/bloom/)

*   Use Cases Use Cases: submenu

    *   [![Image 17](https://dist.neo4j.com/wp-content/uploads/20240329130329/genai.svg) AI Systems Back your LLMs with a Knowledge Graph for better business AI Learn More](https://neo4j.com/use-cases/ai-systems/)
    *   [Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more All Use Cases](https://neo4j.com/use-cases/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more All Customer Stories](https://neo4j.com/customer-stories/)

*   Developers Developers: submenu

    *   [Developer Center Best practices, guides, tutorials, and downloads Learn More](https://neo4j.com/developer/)[opens in new tab GraphAcademy Free online courses and certifications. Join the 100K+ Neo4j experts. Learn More](https://graphacademy.neo4j.com/)
    *   Developers
        *   [Deployment Center Deploy Neo4j on any cloud or architecture](https://neo4j.com/deployment-center/)
        *   [Documentation![Image 18](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
        *   [Developer Blog Deep dives into more technical Neo4j topics](https://neo4j.com/blog/developer/)
        *   [opens in new tab Community A global forum for online discussion](https://community.neo4j.com/)

DATA SCIENTISTS

    *   [Data Science Documentation![Image 19](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for the Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/)
    *   [Graph Data Science Home Learn what Neo4j offers for data science](https://neo4j.com/product/graph-data-science/)
    *   [Get Started With Graph Data Science Download or get started in Sandbox today](https://neo4j.com/graph-data-science-software/)
    *   [opens in new tab Data Science Community A global forum for data-driven professionals](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/)

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   Learn Learn: submenu

LEARN

    *   [Documentation![Image 20](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [GraphAcademy![Image 21](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications](https://graphacademy.neo4j.com/)
    *   [Resource Library White papers, datasheets, and more](https://neo4j.com/resources/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)

CONNECT

    *   [Neo4j Events Hub![Image 22](https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg)Live and on-demand events, training, webinars, and demos](https://neo4j.com/events/)
    *   [Neo4j Blog Announcements, guides, and best practices](https://neo4j.com/blog/)
    *   [Neo4j Video Hub Covering graph databases, data science, analytics & AI](https://neo4j.com/videos/)

FEATURED EVENTS

    *   [![Image 23: GraphSummit Logo](https://dist.neo4j.com/wp-content/uploads/20250306090638/graphsummit-logo.svg) Graphs + AI: Transform Your Data Into Knowledge Learn more](https://neo4j.com/graphsummit/)
    *   [opens in new tab![Image 24: Neo4j Nodes 2026](https://dist.neo4j.com/wp-content/uploads/20260416111036/nodes-2026-logo.svg) Call for Papers Virtual Conference: Engineering Better Intelligence Submit a session abstract by June 15, 2026 Submit a Talk](https://sessionize.com/nodes26/)

*   [Pricing](https://neo4j.com/pricing/)
*   [Contact Us](https://neo4j.com/contact-us/)
*   [Get Started Free](https://console.neo4j.io/)

Blog Home 

Close

*   [Blog Home](https://neo4j.com/blog/)
*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)
*   [News](https://neo4j.com/blog/news/)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)
*   [Knowledge Graph](https://neo4j.com/blog/knowledge-graph/)

# Knowledge Graphs and LLMs: Fine-Tuning vs. Retrieval-Augmented Generation

![Image 25: Photo of Tomaž Bratanič](https://dist.neo4j.com/wp-content/uploads/20240517073021/tomaz-bratanic-150x150.jpeg)

![Image 26: Photo of Kumar Harsh](https://dist.neo4j.com/wp-content/uploads/20250217051229/kumar-harsh-150x150.jpeg)

[Tomaž Bratanič](https://neo4j.com/blog/contributor/tomaz-bratanic/),

[Kumar Harsh](https://neo4j.com/blog/contributor/kumar-harsh/)

September 11, 2024

14 min read

![Image 27](https://dist.neo4j.com/wp-content/uploads/20240911090339/fine-tuning-vs-rag.png)

Many organizations are considering LLMs for business use cases like answering questions as chatbots or virtual assistants or generating creative text. However, they usually run into limitations such as knowledge cutoff, hallucinations, and the lack of user customization.

Two approaches that address these challenges are **fine-tuning** and **retrieval-augmented generation**. Fine-tuning an LLM involves a supervised training phase, where question-answer pairs are provided to optimize the LLM’s performance. Conversely, in [retrieval-augmented generation](https://neo4j.com/blog/genai/what-is-retrieval-augmented-generation-rag/) (RAG), the LLM serves as a natural language interface to access external information, which means it doesn’t rely only on its internal knowledge to produce answers.

This article explores the pros and cons of using fine-tuning and RAG to curb the limitations of LLMs. We also consider the implications of each approach for organizations that already use [knowledge graphs](https://neo4j.com/books/developers-guide-how-to-build-knowledge-graph/) to organize and manage their data.

## The Limitations of LLMs

![Image 28: Midjourney's idea of a knowledge graph chatbot.](https://dist.neo4j.com/wp-content/uploads/20230608064948/1gMyohWeGauh6BZvbqsXAgw-e1726069380895.png)

Midjourney’s idea of a knowledge graph chatbot.

After the launch of ChatGPT in November 2022, people began considering integrating LLMs into their applications to generate creative content and solve typical natural language processing tasks like text summarization and translation.

Using LLMs out of the box for business use cases can cause serious issues, though. Let’s explore the most critical concerns.

### Knowledge Cutoff

Knowledge cutoff refers to the fact that LLMs are unaware of any events that happened after their training. For example, if you ask ChatGPT about an event that occurred in 2024, you’ll get a response like this:

![Image 29](https://dist.neo4j.com/wp-content/uploads/20250219170021/image-78-1024x403.png)

ChatGPT’s knowledge cutoff date. Image by author.

The same problem will occur if you ask an LLM about any event not present in its training dataset. While the knowledge cutoff date is relevant for any publicly available information, the LLM doesn’t have knowledge about private or confidential information that might be available even before the knowledge cutoff date.

For example, many companies have confidential information they don’t share publicly, but they might be interested in having a custom LLM that could answer questions about that information. On the other hand, publicly available information that an LLM is aware of could already be outdated.

### Hallucinations

We cannot blindly believe everything that LLMs produce.

LLMs are trained to produce realistic-sounding output, but it might not always be accurate. Some invalid information is more challenging to spot than others. Especially for missing data, the LLMs are likely to make up an answer that sounds convincing (but is nonetheless wrong) instead of admitting that it lacks the base facts in its training.

For example, research or court citations might be easier to verify. In 2023, a lawyer got in trouble for [blindly believing the court citations ChatGPT produced](https://edition.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers/index.html). While people have become more wary since then about the information that public LLMs like ChatGPT and Gemini generate, it’s still risky.

LLMs will also consistently produce assertive yet false information about any sort of identification number, including Wikidata IDs:

![Image 30](https://dist.neo4j.com/wp-content/uploads/20250219170037/image-79-1024x711.png)

ChatGPT’s hallucinations. Image by author.

In the screenshot above, ChatGPT gave an assertive response, but it’s inaccurate. The Wikidata ID that ChatGPT gave points to a Russian singer.

### Other Problems

LLMs also have other problems:

*   **Bias** – LLMs can inherit biases from their training data, leading to discriminatory or unfair outputs.
*   **Prompt injection** – Malicious users can craft prompts that manipulate the LLM to generate harmful or misleading content.
*   **Common sense reasoning** – LLMs often struggle with tasks requiring common-sense reasoning or an understanding of the situation’s context.
*   **Explainability** – It can be difficult to understand the reasoning or sources behind an LLM’s output, which reduces trust in its outputs and complicates debugging efforts.

We won’t explore these in detail for brevity’s sake. Instead, let’s explore your first option for overcoming these challenges: supervised fine-tuning.

## Supervised Fine-Tuning of an LLM

Fine-tuning is a targeted training approach for LLMs. It refers to the supervised training phase during which you provide additional question-answer pairs to optimize an LLM’s performance. By repeatedly processing these data samples, the LLM refines its understanding and improves its ability to answer questions or generate text in that specific area.

Fine-tuning lets you use the LLM’s existing capabilities while tailoring it to address your unique needs. If you combine fine-tuning with domain-specific pre-training, you can have a [domain-specific LLM](https://arxiv.org/abs/2401.02981) to carry out specialized operations in a field such as finance, with increased accuracy.

> **Note:** Two prominent use cases for fine-tuning an LLM are updating and expanding its internal knowledge and fine-tuning a model for a specific task (like text summarization or translating natural language to database queries). You could also prepare a model for creative purposes, such as personalized artistic content generation and analysis of user preferences and behavior patterns for content filtering and recommendation. This article discusses the first use case of using fine-tuning techniques to update and expand the internal knowledge of an LLM.

### Where Does Fine-Tuning Fit In?

> Explaining in detail how LLMs are trained is beyond the scope of this blog post. If you’re curious, you can watch this [video by Andrej Karpathy](https://www.youtube.com/watch?v=bZQun8Y4L2A) to catch up on LLMs and learn about the different phases of LLM training.

The first step of creating an LLM involves pre-training a model to develop a base LLM. A base LLM is usually pre-trained using a gigantic corpus of text, frequently in the billions or even trillions of tokens. The cost of training can be upwards of hundreds of thousands or even millions of dollars — something most organizations want to avoid.

Recently, [a paper by Microsoft](https://arxiv.org/pdf/2406.02290) (published in June 2024) showed that techniques like gradient checkpointing and low-rank adaptation can reduce memory bottlenecks during the fine-tuning process. This would make fine-tuning more time- and cost-efficient, but so far, we don’t have any real-world examples that have proved cost reduction.

![Image 31: Supervised fine-tuning flow. Image by Tomaž Bratanič. Icons from [Flaticon](https://www.flaticon.com/).](https://dist.neo4j.com/wp-content/uploads/20230608064931/1LTfNOqZQB_M42KyvttjSyw.png)

Supervised fine-tuning flow. Image by Tomaž Bratanič. Icons from [Flaticon](https://www.flaticon.com/).

Therefore, the most common first step is to choose a pre-trained base LLM for your use case. You need to consider several things when making this choice:

*   The **number of parameters** in an LLM determines its capacity to learn and represent complex patterns in the data. Larger models require more computational power and memory for training and inference. They can also have longer training times. Fine-tuning such models can be resource-intensive, necessitating powerful hardware such as GPUs and TPUs.
*   The **license** of the base LLM dictates how you can use the fine-tuned model. Some licenses may have restrictions on commercial use, distribution, or modification. Open source models offer more flexibility for fine-tuning and customization, while proprietary models might provide better performance or specific features but with more restrictive licenses. You must comply with the license terms to avoid legal issues.
*   **Bias** in the base model can be amplified during fine-tuning if not properly addressed, which can lead to unfair or discriminatory behavior by the fine-tuned model. Identifying and mitigating bias needs additional data preprocessing and evaluation steps, including employing data balancing techniques, bias detection tools, and fairness-aware training algorithms. You want to choose a base LLM that has the least known bias in its initial training dataset.
*   **Toxicity** refers to the fact that models can generate toxic or harmful content if they’re not properly controlled. To minimize toxicity, maintain a positive user experience, and prevent harm, you want to filter training data and implement safety layers and continuous monitoring. If possible, also choose a base LLM that has the least known toxicity and includes mechanisms to detect and mitigate toxicity during fine-tuning.

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

![Image 32: Retrieval-augmented generation. Image by Tomaž Bratanič. Icons from [Flaticon](https://www.flaticon.com/).](https://dist.neo4j.com/wp-content/uploads/20230608064925/1zydD2GKzjpEyvL-d_cP0vA.png)

Retrieval-augmented generation. Image by Tomaž Bratanič. Icons from [Flaticon](https://www.flaticon.com/).

RAG uses a [smart search](https://lucidworks.com/post/what-is-smart-search/) tool to provide your LLM with an appropriately phrased question and a set of relevant documents from your data store. It then generates an answer based on information from your data source. This means you don’t rely on internal knowledge of the LLM to produce answers. Instead, the LLM is used only to extract relevant information from documents you passed in and summarize it.

The introduction of agents and tool-calling support has acted as a catalyst for the rise of RAG.

Agents act as intermediaries that connect LLMs to external knowledge sources like databases and APIs. As a result, LLMs can tap into a vast pool of real-time data, overcoming the knowledge cutoff and enabling them to access the latest information. Agents can integrate fact-checking services and verification tools into the LLM workflow, which enhances the trustworthiness of the LLM’s outputs by mitigating the risk of factual errors.

Native tool-calling functionality takes this a step further. LLMs can directly call upon external tools for specific tasks, such as complex calculations or data analysis, which allows them to handle a wider range of problems and expand their overall capabilities. For example, the [ChatGPT tools](https://openai.com/index/gpt-4o-and-more-tools-to-chatgpt-free/#:~:text=Bringing%20more%20intelligence%20and%20advanced%20tools%20for%20free) for getting web responses and uploading files for assistance in writing or analyzing can be thought of as a RAG approach to LLM applications. Because the ChatGPT interface has access to the internet, the LLM can search to access up-to-date information and use it to construct the final answer:

![Image 33](https://dist.neo4j.com/wp-content/uploads/20250219170151/image-80-1024x697.png)

ChatGPT with browsing plugin. Image by author.

In this example, ChatGPT was able to answer who won the NBA MVP in 2024. But, remember the cutoff knowledge date for ChatGPT is January 2022, so it couldn’t know who won the 2024 NBA MVP from its internal knowledge. Instead, it accessed external information from the internet with its [Browse with Bing feature](https://help.openai.com/en/articles/8077698-how-do-i-use-chatgpt-browse-with-bing-to-search-the-web), which allowed it to answer the question with up-to-date information. Such features present an integrated augmentation mechanism inside the OpenAI platform.

### Implementing Retrieval-Augmented Generation

There are multiple ways in which you can implement RAG in your systems.

[LangChain](https://python.langchain.com/v0.2/docs/introduction/), a library for developing and deploying applications using LLMs, provides tools for integrating LLMs with RAG techniques. You can use the LangChain library to [allow LLMs to access real-time information](https://towardsdatascience.com/getting-started-with-langchain-a-beginners-guide-to-building-llm-powered-applications-95fc8898732c) from various sources like Google Search, vector databases, or [knowledge graphs](https://python.langchain.com/v0.1/docs/use_cases/graph/).

For example, LangChain has added a [Cypher Search chain](https://towardsdatascience.com/langchain-has-added-cypher-search-cb9d821120d5) that converts natural language questions into a [Cypher]([https://neo4j.com/docs/cypher-manual/current/introduction/](https://neo4j.com/docs/cypher-manual/current/introduction/)] statement, uses it to retrieve information from the graph database, such as those of Neo4j, and constructs a final answer based on the information provided. With the Cypher Search chain, an LLM is not only used to construct a final answer but also to translate a natural language question into a Cypher query:

![Image 34: Cypher search in LangChain. Image by Tomaž Bratanič.](https://dist.neo4j.com/wp-content/uploads/20230608064914/1RsB4TVvro3oj7KKGpu_ohA.png)

Cypher Search in LangChain. Image by Tomaž Bratanič.

Another popular library for retrieval-augmented LLM workflows is [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html), formerly known as GPT Index. LlamaIndex is a comprehensive data framework that enhances the performance of LLMs by [enabling them to use private or custom data](https://medium.com/llamaindex-blog/llamaindex-on-twiml-ai-a-distilled-summary-using-llamaindex-de2a88551595).

LlamaIndex offers data connectors that facilitate ingesting various data sources and formats — including everything from APIs, PDFs, and documents to SQL or graph data — to integrate existing data into the LLM. It also provides efficient mechanisms to structure the ingested data using indexes and graphs, ensuring the data is suitably arranged for use with LLMs. Its advanced retrieval and query interface lets users input an LLM prompt and receive back a context-retrieved, knowledge-augmented output.

LlamaIndex supports creating and connecting to [property graph indexes](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/) to build a rich knowledge graph from unstructured data and then query it in flexible ways to uncover insights and relationships within your information. You can also [skip creating the knowledge graph](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/#:~:text=You%20can%20also%20skip%20creation%2C%20and%20connect%20to%20an%20existing%20knowledge%20graph) if you already have one in a graph database tool like Neo4j and use it directly in your LlamaIndex projects.

Because of [Neo4j’s native property graph model](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/#:~:text=Neo4j%20uses%20a%20property%20graph%20database%20model), knowledge graphs built on Neo4j graph databases can combine transactional data, organizational data, and vector embeddings in a single database, simplifying the overall application design. [Pairing it with LlamaIndex’s property graph index](https://neo4j.com/blog/developer/property-graph-index-llamaindex/) lets you create custom solutions to query specific types of information from within the graph.

### Advantages and Disadvantages of Retrieval-Augmented Generation

The retrieval-augmented approach has some clear advantages over fine-tuning:

*   The answer can cite its sources of information, which allows you to validate the information and potentially change or update the underlying information based on requirements.
*   Hallucinations are less likely to occur as the LLM no longer relies on its internal knowledge to answer the question. Instead, it uses information provided in relevant documents.
*   It’s easier to change, update, and maintain the underlying information the LLM uses because you transform the problem from LLM maintenance to one involving database maintenance, querying, and context construction.
*   Answers can be personalized based on the user’s context or access permission.

However, keep the limitations of RAG in mind:

*   The answers are only as good as the smart search tool. Your smart search tool must be able to provide the LLM with the correctly phrased question along with enough relevant documents from your data store.
*   The application needs access to your specific knowledge base, whether a database or other data stores.
*   Completely disregarding the internal knowledge of the language model limits the number of questions that can be answered.
*   Sometimes LLMs fail to follow instructions, so the context might be ignored, or hallucinations could still occur if no relevant answer data is found in the context.

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

[Enroll Now](https://graphacademy.neo4j.com/courses/llm-fundamentals/)

## The Developer’s Guide:

How to Build a Knowledge Graph

This ebook gives you a step-by-step walkthrough on building your first knowledge graph.

[Download Now](https://neo4j.com/books/developers-guide-how-to-build-knowledge-graph/)

*   [chatbot](https://neo4j.com/blog/tag/chatbot/)
*   [ChatGPT](https://neo4j.com/blog/tag/chatgpt/)
*   [fine tuning](https://neo4j.com/blog/tag/fine-tuning/)
*   [rag](https://neo4j.com/blog/tag/rag/)

## Share Article

*   [opens in new tab](https://www.linkedin.com/shareArticle?mini=true&url=https://neo4j.com/blog/developer/fine-tuning-vs-rag/)
*   [opens in new tab](https://twitter.com/intent/tweet?url=https://neo4j.com/blog/developer/fine-tuning-vs-rag/&text=)
*   [opens in new tab](https://www.facebook.com/sharer/sharer.php?u=https://neo4j.com/blog/developer/fine-tuning-vs-rag/)

[![Image 35](https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1.jpg)](https://neo4j.com/product/auradb/)

[opens in new tab![Image 36](https://dist.neo4j.com/wp-content/uploads/20250430121707/GA.jpg)](https://graphacademy.neo4j.com/)

[![Image 37](https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub.jpg)](https://neo4j.com/videos/)

## Explore

*   [Knowledge Graph](https://neo4j.com/blog/knowledge-graph/)
*   [Supply Chain & Logistics](https://neo4j.com/blog/supply-chain-and-logistics/)
*   [Fraud Detection](https://neo4j.com/blog/fraud-detection/)
*   [Graph Visualization](https://neo4j.com/blog/graph-visualization/)
*   [AuraDB](https://neo4j.com/blog/auradb/)
*   [Digital Twin](https://neo4j.com/blog/digital-twin/)

* * *

## Related Articles

![Image 38](https://dist.neo4j.com/wp-content/uploads/20260428043318/1lEEXavEBpO6PA9kvACSlsw.png)

*   [Developer](https://neo4j.com/blog/developer/)
*   [Graph Database](https://neo4j.com/blog/graph-database/)

## Introducing Asynchronous I/O in Neo4j using io_uring

[5 min read](https://neo4j.com/blog/graph-database/introducing-asynchronous-i-o-in-neo4j-using-io_uring/)

![Image 39](https://dist.neo4j.com/wp-content/uploads/20260429114809/1_8CxvbFwxB0o_ViI1veRCMg-scaled.webp)

*   [Developer](https://neo4j.com/blog/developer/)
*   [Graph Data Science](https://neo4j.com/blog/graph-data-science/)

## SumoDB in Neo4j: Graph Analytics of Grand Sumo

[5 min read](https://neo4j.com/blog/graph-data-science/sumodb-in-neo4j-graph-analytics-of-grand-sumo/)

![Image 40](https://dist.neo4j.com/wp-content/uploads/20260429113617/1_SIlEBcf12oJTiLl7O2mLTA-scaled.webp)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Building Stateful AI: Integrating Aura Agent Lifecycle with MCP and Persistent Memory

[16 min read](https://neo4j.com/blog/genai/building-stateful-ai-integrating-aura-agent-lifecycle-with-mcp-and-persistent-memory/)

![Image 41](https://dist.neo4j.com/wp-content/uploads/20260428043331/1MeXxC_I8_cGuLBpihYbGdQ.png)

*   [Developer](https://neo4j.com/blog/developer/)
*   [Supply Chain & Logistics](https://neo4j.com/blog/supply-chain-and-logistics/)

## Precise Economic Policy in a World of Chaos

[13 min read](https://neo4j.com/blog/supply-chain-and-logistics/precise-economic-policy-in-a-world-of-chaos/)

![Image 42: GraphAcademy content is moved into Neo4j Aura, and an Aura Agent used to provide MCP server access to VS Code, Cursor, and Claude agents.](https://dist.neo4j.com/wp-content/uploads/20260423023749/architecture-1.png)

*   [Agentic AI](https://neo4j.com/blog/agentic-ai/)
*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Can I use Aura Agents to create an MCP enabled Teacher?

[8 min read](https://neo4j.com/blog/agentic-ai/can-i-use-aura-agents-to-create-an-mcp-enabled-teacher-2/)

![Image 43](https://dist.neo4j.com/wp-content/uploads/20260428043330/1l-xaXyrUxRdmeHIqDz_AFg.png)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Integrating Neo4j with Google Genkit: A Practical Guide

[21 min read](https://neo4j.com/blog/genai/integrating-neo4j-with-google-genkit-a-practical-guide/)

![Image 44](https://dist.neo4j.com/wp-content/uploads/20230921083327/homepage-viz_ART-left.svg)![Image 45](https://dist.neo4j.com/wp-content/uploads/20230921083329/homepage-viz_ART-right.svg)![Image 46](https://dist.neo4j.com/wp-content/uploads/20230921082858/homepage-viz_left-side-art_375.svg)![Image 47](https://dist.neo4j.com/wp-content/uploads/20230921082910/homepage-viz_right-side-art_375.svg)

## Build Intelligent Apps Easily

Transform your data into knowledge to build smart, accurate, and adaptive applications.

[Start Building](https://neo4j.com/product/auradb/)

Products

*   [Neo4j AuraDB](https://neo4j.com/product/auradb/)
*   [Neo4j Graph Database](https://neo4j.com/product/neo4j-graph-database/)
*   [Neo4j Graph Analytics](https://neo4j.com/product/aura-graph-analytics/)
*   [Neo4j Graph Data Science](https://neo4j.com/product/graph-data-science/)
*   [Neo4j Fleet Manager](https://neo4j.com/product/fleet-manager/)
*   [Neo4j Bloom](https://neo4j.com/product/bloom/)
*   [Cypher Query Language](https://neo4j.com/product/cypher-graph-query-language/)
*   [Neo4j GraphQL](https://neo4j.com/product/graphql-library/)
*   [Pricing](https://neo4j.com/pricing/)
*   [Neo4j Community Edition](https://neo4j.com/product/community-edition/)

Use Cases

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   [Generative AI](https://neo4j.com/generativeai/)
*   [Knowledge Graphs](https://neo4j.com/use-cases/knowledge-graph/)
*   [Pattern Matching](https://neo4j.com/use-cases/pattern-matching/)
*   [Industries & Use Cases](https://neo4j.com/use-cases/)
*   [Case Studies](https://neo4j.com/customer-stories/)

Developers

*   [Developer Home](https://neo4j.com/developer/)
*   [Documentation](https://neo4j.com/docs/)
*   [Deployment Center](https://neo4j.com/deployment-center/)
*   [Developer Blog](https://neo4j.com/blog/developer/)
*   [opens in new tab Community](https://community.neo4j.com/)
*   [Virtual Events](https://neo4j.com/events/)
*   [opens in new tab GraphAcademy](https://graphacademy.neo4j.com/)
*   [Release Notes](https://neo4j.com/release-notes/)

Data Scientists

*   [Graph Data Science Home](https://neo4j.com/product/graph-data-science/)
*   [Data Science Documentation](https://neo4j.com/docs/graph-data-science/current/)
*   [Get Started with Graph Data Science](https://neo4j.com/graph-data-science-software/)
*   [opens in new tab Data Science Community](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/73)
*   [opens in new tab GraphAcademy for Data Science](https://graphacademy.neo4j.com/categories/data-scientist/)

Learn

*   [Resource Library](https://neo4j.com/resources/)
*   [Neo4j Blog](https://neo4j.com/blog/)
*   [opens in new tab GraphAcademy](https://graphacademy.neo4j.com/)
*   [Research Center](https://neo4j.com/research/)
*   [Case Studies](https://neo4j.com/customer-stories/)
*   [Neo4j Video Hub](https://neo4j.com/videos/)
*   [Neo4j Events Hub](https://neo4j.com/events/)
*   [GraphSummit](https://neo4j.com/graphsummit/)
*   [NODES](https://neo4j.com/nodes-2025/)
*   [Webinars](https://neo4j.com/webinars/)
*   [opens in new tab GraphRAG](https://graphrag.com/)

Partners

*   [Find a Partner](https://neo4j.com/partners/directory/)
*   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
*   [Solution Partners](https://neo4j.com/partners/solution-partners/)
*   [OEM Partners](https://neo4j.com/partners/oem-partners/)
*   [Technology Partners](https://neo4j.com/partners/technology-partners/)
*   [opens in new tab Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

Company

*   [About Us](https://neo4j.com/company/)
*   [Newsroom](https://neo4j.com/news/)
*   [Awards and Honors](https://neo4j.com/awards/)
*   [Graphs4Good](https://neo4j.com/graphs4good/)
*   [Careers](https://neo4j.com/careers/)
*   [Culture](https://neo4j.com/culture/)
*   [Leadership](https://neo4j.com/leadership/)
*   [opens in new tab Support](https://support.neo4j.com/s/)
*   [opens in new tab Trust Center](https://trust.neo4j.com/)

[Contact Us →](https://neo4j.com/contact-us/?ref=footer)

*   US: [1-855-636-4532](tel:1-855-636-4532)
*   Sweden: [+46 171 480 113](tel:+46 171 480 113)
*   UK: [+44 20 3868 3223](tel:+44 20 3868 3223)
*   France: [+33 (0) 1 88 46 13 20](tel:+33 (0) 1 88 46 13 20)
*   Singapore: [+65 6859 0336](tel:+65 6859 0336)
*   Australia: [+61 2 8395 2895](tel:+61 2 8395 2895)
*   India: [+91 6827 521 210](tel:+91 6827 521 210)

Social Networks

[opens in new tab](https://www.linkedin.com/company/neo4j)[opens in new tab](https://x.com/neo4j)[opens in new tab](https://youtube.com/neo4j)[opens in new tab](https://www.facebook.com/neo4j.graph.database)[opens in new tab](https://community.neo4j.com/)[opens in new tab](https://github.com/neo4j)

© 2026 Neo4j, Inc. 

[Terms](https://legal.neo4j.com/#website-terms-of-use) | [Privacy Notice](https://neo4j.com/legal-terms/privacy-notice/) | [Sitemap](https://neo4j.com/sitemap/)

[opens in new tab Anti-Corruption Policy](https://assets.neo4j.com/Neo4j_Anti-Corruption_Policy.pdf)

 ©2026 Neo4j, Inc., Neo Technology®, Neo4j®, Cypher®, Neo4j Bloom™, Neo4j Graph Data Science Library™, Neo4j® Aura™, and Neo4j® AuraDB™ are registered trademarks or a trademark of Neo4j, Inc. All other marks are owned by their respective companies. 

[![Image 48](https://dist.neo4j.com/wp-content/uploads/20210608133508/icon-tooltip-info.svg) Contact Us](https://neo4j.com/contact-us/)

[](https://neo4j.com/blog/developer/fine-tuning-vs-rag/)![Image 49](blob:https://neo4j.com/0b6ec51c-5f48-4210-bc7d-733183fe5ea4)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vect.md">
<details>
<summary>RAG Pipeline Deep Dive: Ingestion, Chunking, Embedding, and Vector Search</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://medium.com/@derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-abd3c8bfc177>

# RAG Pipeline Deep Dive: Ingestion, Chunking, Embedding, and Vector Search

Retrieval-Augmented Generation (RAG) has become the default approach for providing context and memory to AI applications. Understanding the RAG pipeline — from document ingestion to final response generation — is essential for building high-performance AI systems. This comprehensive guide explores each stage of the RAG workflow, with special focus on Oracle Database 23ai’s native vector capabilities.

## The RAG Pipeline: An Overview

A complete RAG pipeline consists of two main phases:

**Ingestion Phase (Offline):**

Documents → Chunking → Embedding → Index/Store in Vector Database

**Retrieval Phase (Runtime):**

User Query → Embed Query → Similarity Search → Top-K Results → LLM Generation → Response

The RAG pipeline connects the model to the information it needs at query time. When a user asks a question, the pipeline retrieves the most relevant documents, prepares that text as context, and includes it in the prompt so the model can generate an answer grounded in retrieved material rather than training data alone.

## Phase 1: Document Ingestion

Ingestion is the process of loading documents from multiple sources and in multiple formats, transforming them into a structured form suitable for embedding and retrieval.

## Document Loading

Raw documents — whether PDFs, Word documents, web pages, or database records — must be transformed into manageable chunks suitable for retrieval.

**Common Sources:**

- Local files (PDF, DOCX, TXT, CSV)
- Web pages and APIs
- Databases and data warehouses
- Cloud storage (S3, GCS, Azure Blob)
- Enterprise systems (SharePoint, Confluence, Notion)

**Loading Libraries:**

- **PyPDF2**: For PDF documents
- **python-docx**: For Word documents
- **LangChain Document Loaders**: Unified interface for multiple formats
- **LlamaIndex Data Connectors**: Specialized loaders for various sources
- **Oracle OracleDocLoader**: Native loader for Oracle Database 23ai

## Text Extraction and Cleaning

A clean corpus improves both retrieval accuracy and embedding quality. Use parsing libraries to extract only the primary content from web pages or PDFs, and remove boilerplate, navigation links, and disclaimers.

**Cleaning Steps:**

1.  **Remove Noise**: Headers, footers, navigation, ads
2.  **Normalize Structure**: Convert to consistent format (JSONL, Parquet)
3.  **Preserve Metadata**: Source, timestamp, author, document type
4.  **Handle Special Characters**: Normalize encoding (UTF-8)
5.  **Maintain Logical Structure**: Keep headings, lists, tables

## Metadata Enrichment

Each chunk should carry metadata such as topic, date, and source, so that retrieval can filter and rank results more effectively.

**Important Metadata Fields:**

- **source\_id**: Unique document identifier
- **title**: Document title
- **created\_date**: Document creation timestamp
- **author**: Document creator
- **document\_type**: PDF, email, webpage
- **topic/category**: For domain filtering
- **page\_number**: For PDF sources
- **chunk\_id**: Unique identifier for the chunk

## Phase 2: Chunking — The Critical Step

Chunking is simply the act of splitting larger documents into smaller units (“chunks”). Each chunk can be individually indexed, embedded, and retrieved.

## Why Chunking Matters

The chunking process directly feeds into the embedding step, where each chunk is converted into vector representations that capture semantic meaning.

A common source of inaccurate or unstable answers lies in a structural conflict within the traditional “chunk-embed-retrieve” pipeline: using a single-granularity, fixed-size text chunk to perform two inherently conflicting tasks:

1.  **Semantic matching (recall)**: Smaller chunks (100–256 tokens) needed for precise similarity search
2.  **Context understanding (utilization)**: Larger chunks (1024+ tokens) needed for coherent LLM generation

This creates a difficult trade-off between “precise but fragmented” and “complete but vague.”

## Pre-Chunking vs Post-Chunking

Pre-chunking is the most common method. It processes documents asynchronously by breaking them into smaller pieces before embedding and storing them in the vector database. This enables fast retrieval at query time since all chunks are pre-computed.

Post-chunking takes a different approach by embedding entire documents first, then performing chunking at query time only on the documents that are actually retrieved. The chunked results can be cached, so the system becomes faster over time.

## Chunking Strategies

Fixed-Length Chunking: This is the simplest approach, segmenting text into equally sized pieces using character, token, or word counts.

**Common Chunk Sizes:**

- **300–500 tokens**: Typical chunks for most use cases, depending on the model and content type
- **100–256 tokens**: For high-precision recall in semantic search
- **1024+ tokens**: For providing complete context to LLMs

Adopt recursive/semantic chunkers with 10–20% overlap to maintain context across boundaries.

**Advanced Chunking Approaches:**

Recursive Chunking: This method is a bit smarter. It splits text hierarchically based on cues like paragraphs, line breaks, or sentences. If a section is too long, it recursively divides it further.

**Semantic Chunking**: Instead of letting token limits decide where ideas get chopped, it uses embeddings to detect where the meaning actually shifts — grouping semantically related sentences together.

**Document-Aware Chunking**: Preserves document structure (sections, paragraphs, tables) while chunking.

## Chunk Overlap

**Chunk overlap is the number of overlapping characters (or tokens) between adjacent chunks**. This ensures that context isn’t lost when information spans chunk boundaries.

**Recommended Overlap:**

- 10–20% overlap is standard practice
- For 500-token chunks, use 50–100 token overlap
- Maintains continuity without excessive redundancy

**Example:**

```
Chunk 1: [Tokens 0-500]
Chunk 2: [Tokens 450-950]  ← 50 token overlap
Chunk 3: [Tokens 900-1400] ← 50 token overlap
```

## Splitting Process

Documents are split recursively until the chunks are small enough, using text splitters that respect:

- Sentence boundaries (don’t break mid-sentence)
- Paragraph boundaries (maintain logical grouping)
- Section boundaries (preserve document structure)

**Popular Chunking Libraries:**

The LLM community often turns to two powerful open-source libraries: LangChain and LlamaIndex:

- **LangChain**: Broad framework with flexible chunking strategies
- **LlamaIndex**: Designed specifically for RAG pipelines with sophisticated NodeParsers
- **Chonkie**: Lightweight, dedicated chunking library focusing solely on text splitting

## Phase 3: Embedding and Storage

Chunking makes information retrievable; embeddings make it searchable by meaning rather than keywords.

## What Are Embeddings?

**Embeddings are numerical representations that capture semantic relationships** between text. A piece of text — whether a word, phrase, sentence, or paragraph — is converted to a vector of numbers (typically 384–1536 dimensions).

**Key Properties:**

- **Semantic similarity**: Embeddings that are numerically similar are also semantically similar
- **Dense representation**: High-dimensional vectors capture nuanced meaning
- **Model-specific**: Different embedding models produce different vector spaces

## Embedding Models

**Popular Options:**

- **OpenAI text-embedding-3-large**: 3072 dimensions, high quality
- **Cohere embed-v4.0**: 1024 dimensions, multimodal (text + images)
- **Sentence-BERT (SBERT)**: 768 dimensions, open-source
- **all-MiniLM-L6-v2**: 384 dimensions, lightweight and fast

Choose MiniLM/SBERT/Instruct/E5 for text, CLIP for images. Normalize embeddings for consistent similarity calculations.

## Embedding Generation: Outside vs Inside the Database

### Option 1: Generate Embeddings Outside Oracle Database 23ai

**Vector embeddings can be generated outside Oracle Database 23ai using third-party embedding models**, then imported into the database for storage and search.

**Workflow:**

```
from sentence_transformers import SentenceTransformer
```

```
# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')# Generate embeddings
chunks = ["First chunk text", "Second chunk text"]
embeddings = model.encode(chunks)# Store in Oracle Database 23ai
# INSERT INTO documents (text, embedding) VALUES (?, ?)
```

**Advantages:**

- Flexibility in choosing any embedding model
- Can use cloud-based embedding services
- Easy integration with existing ML pipelines

### Option 2: Generate Embeddings Inside Oracle Database 23ai

**Embeddings can also be generated inside Oracle Database 23ai by downloading pretrained embedding models, converting them to ONNX format, and importing the ONNX format models into Database 23ai**.

ONNX (Open Neural Network Exchange) is an open-source format designed to represent deep learning models. It aims to provide interoperability between different deep learning frameworks.

**Process:**

1.  **Download Pretrained Model** from Hugging Face or similar source
2.  **Convert to ONNX Format** using Oracle OML4Py utility
3.  **Import into Database 23ai** using DBMS\_VECTOR package

The command can be run to import the ONNX file into the database:

```
EXEC dbms_vector.load_onnx_model(
  'DM_DUMP',
  'all_MiniLM_L12_v2.onnx',
  'minilm_l12_v2',
  JSON('{"function": "embedding", "embeddingOutput": "embedding", "input": {"input": ["DATA"]}}')
);
```

1.  **Generate Embeddings in SQL**:

```
SELECT VECTOR_EMBEDDING(minilm_l12_v2 USING 'Your text here' AS data) AS embedding
FROM DUAL;
```

**Advantages:**

- Oracle Database implements an ONNX runtime directly within the database. This allows you to generate vector embeddings directly within Oracle Database using SQL
- Eliminates data movement between systems
- Simplified architecture and security
- Native integration with Oracle’s vector capabilities

## Phase 4: Vector Indexes for Fast Search

Once embeddings are generated and stored, **vector indexes are specialized data structures designed for similarity searches in high-dimensional vector spaces**. They help accelerate vector similarity searches by reducing the number of distance calculations needed.

## Why Vector Indexes?

Exact search to find the closest matches for a given vector are accurate but can be slow, since costly vector distance computations are needed for all vectors in a column.

Vector indexes use techniques like clustering, partitioning, and neighbor graphs to group similar vectors together, reducing the search space dramatically.

## Oracle AI Vector Search: Supported Index Types

Oracle AI Vector Search supports Hierarchical Navigable Small World (HNSW) indexes and Inverted File (IVF) indexes.

### 1. HNSW: In-Memory Neighbor Graph

**Hierarchical Navigable Small World (HNSW)** creates a navigable graph structure to locate similar vectors with exceptional speed and accuracy.

**Characteristics:**

HNSW is an In-Memory Neighbor Graph Vector Index fully built in-memory. You need to setup a new memory pool with VECTOR\_MEMORY\_SIZE in the SGA to accommodate it.

Since the HNSW index consumes a lot of memory, Oracle Database 23ai makes this index available by allocating a memory area called Vector Pool.

**Memory Calculation:**

To roughly determine the memory size needed to store an HNSW index, use the following formula: 1.3 × number of vectors × number of dimensions × size of your vector dimension type (for example, a FLOAT32 is 4 bytes).

**Creating HNSW Index:**

```
-- Configure vector pool
ALTER SYSTEM SET vector_memory_size=800M SCOPE=SPFILE;
-- Restart required
```

```
-- Create HNSW index
CREATE VECTOR INDEX documents_hnsw_idx
ON documents (embedding)
ORGANIZATION NEIGHBOR GRAPH
DISTANCE COSINE
WITH TARGET ACCURACY 95;
```

**Performance:**

HNSW enables sub-100ms retrieval at 95%+ recall — extremely fast for real-time applications.

**Limitations:**

DML operations (insert, update, delete) are not allowed after creating an HNSW index — designed for read-heavy workloads.

HNSW indexes are not available in RAC environments.

### 2. IVF: Neighbor Partition Index

**Inverted File Flat (IVF)** indexes partition data points into clusters, enabling efficient searching within relevant clusters.

**Characteristics:**

IVF Flat index is a Neighbor Partition Vector index built on disk, and its blocks are cached in the regular buffer cache.

A significant advantage of an IVF vector index is that it is not constrained by the amount of memory available in the vector pool like an HNSW vector index is.

**How IVF Works:**

It is designed to enhance search efficiency by narrowing the search area through the use of neighbor partitions or clusters. The center of each partition, or the centroid, represents the average vector for each partition. By default, the number of partitions and their corresponding centroids is set to the square root of the dataset’s size.

**Creating IVF Index:**

```
CREATE VECTOR INDEX documents_ivf_idx
ON documents (embedding)
ORGANIZATION NEIGHBOR PARTITIONS
DISTANCE COSINE
WITH TARGET ACCURACY 95;
```

**Advantages:**

- Works with massive datasets
- Supports global and local indexes on partitioned tables
- DML operations can degrade accuracy over time. Periodically rebuilding the index may be necessary
- More memory-efficient than HNSW

**Performance:**

Although an IVF index won’t be as fast as an equivalent HNSW index, it can be used for very large data sets and still provide excellent performance when compared to an exhaustive similarity search.

### 3. Hybrid Vector Indexes

Hybrid vector index combines full text and semantic search in one index, allowing users to easily index and query their documents using a combination of full text search and semantic vector search.

**Use Case:**

When you need to match both semantic meaning AND specific keywords/terms in a single query.

## GPU Acceleration

At Oracle CloudWorld 2024, Oracle demonstrated GPU-accelerated creation of vector embeddings and HNSW index creation using NVIDIA GPUs.

When a user sends a request to create an HNSW vector index to Oracle Database, the database intelligently compiles and redirects the task to a Compute Offload Server process that leverages GPUs and the CAGRA algorithm from NVIDIA cuVS library to rapidly generate a graph index.

## Phase 5: Retrieval — Finding Relevant Context

At runtime, when a user submits a query, the retrieval phase locates the most relevant chunks to provide as context to the LLM.

## Query Embedding

The system encodes the user’s query with the same model used to embed documents during ingestion.

```
-- Generate query embedding
SELECT VECTOR_EMBEDDING(minilm_l12_v2 USING 'What is RAG?' AS data) AS query_vector
FROM DUAL;
```

## Similarity Search

The query vector is compared against all document vectors in the database using a distance metric.

**Distance Metrics:**

Common options include EUCLIDEAN, L2\_SQUARED, COSINE, DOT, MANHATTAN, and HAMMING. You can specify the metric during index creation or within the search query itself.

- **Cosine Similarity**: Most common for text (measures angle between vectors)
- **Euclidean Distance**: Straight-line distance in vector space
- **Dot Product**: Efficient for normalized vectors

**Performing Similarity Search:**

```
SELECT
  text,
  VECTOR_DISTANCE(embedding, :query_vector, COSINE) AS distance
FROM documents
ORDER BY distance
FETCH APPROX FIRST 5 ROWS ONLY;
```

## Top-K Results

The system searches the index for the nearest vectors, retrieves the top-k chunks, and includes those chunks with the query in the prompt.

**Choosing K:**

- **K=3–5**: For focused, specific queries
- **K=10–20**: For broader research queries
- **K=50+**: For comprehensive document analysis

**Challenges:**

Top-k returns near duplicates or shallow snippets, so the prompt lacks diversity. Retrieval misses proper nouns, IDs, or acronyms because they occur rarely.

**Solutions:**

-   **Reranking**: Rerank with cross-encoders (Cohere ReRank, ColBERT) when precision matters
-   **Hybrid Search**: Combine BM25 (keyword) with dense vectors to boost tail recall
-   **Metadata Filtering**: Filter by date, source, document type before retrieval

## Monitoring Index Accuracy

A valuable feature is Oracle’s provision of functions to report index accuracy based on query vectors used in approximate searches. This allows you to continuously monitor and optimize the accuracy of your vector search implementation.

## Phase 6: Generation — Creating the Final Response

Once relevant chunks are retrieved, they’re combined with the user’s query and sent to an LLM for response generation.

## Prompt Assembly

Retrieved chunks are formatted into a coherent context block:

```
Context:
[Chunk 1 text]
[Chunk 2 text]
[Chunk 3 text]
```

```
Question: [User query]Answer based on the provided context:
```

## LLM Generation

The complete prompt (context + query) is sent to the LLM, which generates a response grounded in the retrieved information rather than relying solely on parametric knowledge.

**Benefits:**

- Reduces hallucinations
- Provides traceable sources
- Enables up-to-date information
- Maintains factual accuracy

## Best Practices for Production RAG Pipelines

## 1. Optimize Chunking Strategy

Align chunk size with context windows, use task-specific sentence transformers, and default to HNSW + metadata filtering for sub-100ms retrieval at 95%+ recall.

## 2. Choose Appropriate Embedding Models

- Match embedding dimensions to your dataset size
- Consider domain-specific models for specialized content
- Test multiple models and measure retrieval quality

## 3. Implement Proper Indexing

-   **Small-Medium datasets (< 1M vectors)**: HNSW for maximum speed
-   **Large datasets (1M+ vectors)**: IVF for scalability
-   **Keyword + Semantic**: Hybrid vector indexes

## 4. Monitor and Iterate

Monitor recall@k, latency, and index memory; re-embed on model upgrades.

Track metrics:

- Retrieval accuracy (precision@k, recall@k)
- Query latency (p50, p95, p99)
- Index build time
- Storage requirements

## 5. Handle Edge Cases

- Query reformulation for better retrieval
- Fallback strategies when retrieval fails
- Confidence thresholds for generated responses
- Citation and source tracking

## Advanced RAG Techniques

## 1. Self-Correction (CRAG)

When strong retrieval pipelines return incomplete or irrelevant context, CRAG adds a lightweight feedback loop: before generating, the system checks whether the retrieved set is good enough. If it looks weak, the system triggers another retrieval pass.

## 2. Agentic RAG

Agentic RAG systems plan retrieval strategies and iterate based on partial results — dynamically deciding what to retrieve next.

## 3. GraphRAG

Build an advanced RAG system by first structuring data into a knowledge graph, then layering graph-aware retrieval to capture entity relationships.

## 4. Multimodal RAG

Combining text, images, audio, and video retrieval for richer context.

A robust RAG pipeline requires careful attention to every stage:

**Ingestion**: Clean, structured data with rich metadata

**Chunking**: Balanced chunk sizes with appropriate overlap (10–20%)

**Embedding**: Semantic representations using appropriate models

**Indexing**: Fast similarity search with HNSW or IVF indexes

**Retrieval**: Accurate top-K results with metadata filtering

**Generation**: Grounded responses with proper citations

Oracle Database 23ai provides a complete, integrated platform for RAG with native vector support, ONNX model runtime, advanced indexing (HNSW, IVF, Hybrid), and SQL-native operations — eliminating the need for separate vector databases.

By mastering these components and following best practices, you can build production-grade RAG systems that deliver accurate, relevant, and trustworthy AI-powered experiences.

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