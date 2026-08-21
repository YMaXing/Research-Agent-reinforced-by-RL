# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What empirical evidence and studies show how complex single-prompt LLM calls lead to higher error rates, lost-in-the-middle problems, and increased token waste compared to modular approaches?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.mdpi.com/2079-9292/13/23/4712

Query: What empirical evidence and studies show how complex single-prompt LLM calls lead to higher error rates, lost-in-the-middle problems, and increased token waste compared to modular approaches?

Answer: This empirical study compares single-task prompts (modular approach with separate prompts for sentiment analysis, NER, and JSON formatting) versus multitask prompts (complex single prompt handling all tasks) across five open-weight LLMs: Llama 3.1 8B, Qwen2 7B, Mistral 7B, Phi3 Medium, Gemma2 9B. Experiments on 1000 IMDB reviews show mixed results: single-task prompts outperform multitask in 3/5 models (e.g., Gemma2 9B: F1 NER 55.75% single vs 54.75% multi; Qwen2: BLEU 73.26% vs 56.09%; Phi3: F1 NER 22.62% vs 11.68%), but multitask excels in others (Llama 3.1: BLEU 88.94% vs 76.55%; Mistral sentiment 87.20% vs 71.80%). Statistical tests (Wilcoxon, McNemar, Friedman) confirm significant differences (p<0.05 in most cases), with no universal superiority. Multitask prompts show lower formatting errors in some models (Mistral 29‰ vs 155‰), but single-task requires more API calls (3x tokens/input). Hypothesis that simpler single-task prompts always outperform is rejected; performance depends on model architecture. Fixed-prompt architecture used for fair comparison, highlighting prompt-model interaction complexity. No direct mention of 'lost-in-the-middle' or token waste, but multitask reduces calls while risking parsing errors (e.g., JSON formatting issues requiring regex post-processing). Results challenge assumptions, advocating model-specific strategies over one-size-fits-all.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2

Query: What empirical evidence and studies show how complex single-prompt LLM calls lead to higher error rates, lost-in-the-middle problems, and increased token waste compared to modular approaches?

Answer: 2023 Stanford/UC Berkeley/Samaya AI paper 'Lost in the Middle' tested LLMs on needle-in-haystack task: relevant document position varied (beginning, middle, end) in contexts up to 32K tokens. Results: U-shaped accuracy curve—high at start/end, drops dramatically in middle (primacy/recency bias). Persists in 128K+ models (2025 MIT confirmation). Causes: causal attention masking (early tokens attended by all subsequent; middle only by later), positional encoding decay (RoPE reduces distant attention). Affects RAG, summarization, multi-doc QA, long conversations. Bigger windows worsen 'middle' problem. Mitigations: reorder docs (top at start/end), reduce docs (top 3-5), prompt compression, explicit instructions, multi-pass extraction. No direct modular comparison, but implies single long prompts waste tokens in middle (ignored), favoring modular (process chunks separately). Counterexamples: 'Bigger windows solve it' (no), 'only RAG' (no, any multi-info context). Mirrors human serial position effect.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://aclanthology.org/2025.ommm-1.4.pdf

Query: What empirical evidence and studies show how complex single-prompt LLM calls lead to higher error rates, lost-in-the-middle problems, and increased token waste compared to modular approaches?

Answer: FLARE framework analyzes GPT-4 Turbo 'Inconclusive' classifications on 900 election-misinfo texts (Van der Linden's 6 manipulation degrees). Compares ZS/FS/ICL prompting: FS causes 52.9% error rate (38x ZS's 1.4%, 9x ICL's 4.9%). 70.8% FS errors are parsing failures (E2: invalid formats like 'Classification: None'), due to examples overwhelming output without structural guidance. ZS simpler, fewer parsing issues. Semantic errors (E4-E7: misclassification, false positives) minor. Technical errors (E1-E3) dominate FS. Implies complex multi-example single prompts increase errors vs simpler/modular ZS. No lost-in-middle/token waste explicit, but parsing ties to prompt complexity.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://aclanthology.org/2025.gem-1.14.pdf

Query: What empirical evidence and studies show how complex single-prompt LLM calls lead to higher error rates, lost-in-the-middle problems, and increased token waste compared to modular approaches?

Answer: ZeMPE benchmark (53k zero-shot MPP prompts from 6 classif/12 reasoning benchmarks) evaluates 13 LLMs. BatchClf (multi-classif single prompt) accuracy 72.3% vs SingleClf 75.5% (minor drop), cost-efficient (30-82% token savings via shared instructions). But reformats (SelectOne/All: indices per class) drop sharply (BatchClf-SelectOne: -32%, large Cohen's d=1.8), even small batches (3-5). MultiReasonMS (mixed-source) worse than expected SPP average. No positional bias in BatchClf (unlike single-prompt primacy/recency), similar errors to SingleClf. FS MPP prior lit similar. Instruction-tuning enables MPP; FLAN-T5 fails. Complex single prompts handle multi-problems well short-term but fail format changes, mixed-sources—increased errors vs modular single-problem.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://arxiv.org/html/2505.13360v1

Query: What empirical evidence and studies show how complex single-prompt LLM calls lead to higher error rates, lost-in-the-middle problems, and increased token waste compared to modular approaches?

Answer: Underspecification analysis: prompts with more requirements (N=1-19) drop accuracy (gpt-4o: 98.7% N=1 to 85% N=19; Llama3.3-70B: 79.7%). 37.5% requirements drop >5% due to instruction-following limits, conflicts. Conditional/format reqs hardest. Unspec reqs guessed 41.1% but unstable (2x SD, 2x >20% regression on updates). Existing optimizers inconsistent; req-aware COPRO-R/Bayesian +4.8% acc, -43% tokens. Long complex prompts hurt vs modular spec (specify subset). Ties to token waste (long prompts inefficient), error rates (neglect reqs).

-----

</details>

<details>
<summary>How can developers implement rate limiting, backoff strategies, and error handling when running parallel LLM calls using cloud APIs like Google Gemini?</summary>

Phase: [EXPLOITATION]

### Source [7]: https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903

Query: How can developers implement rate limiting, backoff strategies, and error handling when running parallel LLM calls using cloud APIs like Google Gemini?

Answer: Users report aggressive rate limiting in Gemini API during high-volume requests, causing delayed responses and dropped requests even with exponential backoff and retries. Responses lack clear wait times before reattempting. Documentation mentions rate limits, but lacks programmatic wait time determination or production best practices. Forum seeks SDK tweaks for smoothing integration. Related threads discuss 429 errors despite retryDelay, rate limit increases, and API errors in high-volume scenarios. No specific implementation details provided; emphasizes checking Gemini API Cookbook for reference.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt

Query: How can developers implement rate limiting, backoff strategies, and error handling when running parallel LLM calls using cloud APIs like Google Gemini?

Answer: For 5-20 parallel gemini-3-pro requests on free/low-tier plans, 429 RESOURCE_EXHAUSTED errors occur beyond ~5 RPM due to per-project limits on RPM, TPM, RPD, IPM. Free-tier RPM cut 50-80% (e.g., 5 RPM for Pro models); multiple keys don't help. Exponential backoff with jitter insufficient for simultaneous bursts as requests queue and compete in same window. Sequential delays not viable for mission-critical flows needing short completion windows.

Strategies sought: batch endpoints (unclear for gemini-3-pro), multi-project fan-out (may aggregate by billing), client-side token-bucket rate limiter for staggering, Vertex AI vs AI Studio throughput benchmarks (Vertex tighter), Tier 1 RPM increases. No resolved answers; question closed.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://tianpan.co/blog/2026-03-11-llm-api-resilience-production

Query: How can developers implement rate limiting, backoff strategies, and error handling when running parallel LLM calls using cloud APIs like Google Gemini?

Answer: For parallel LLM calls, implement exponential backoff with full jitter to avoid thundering herd: sleep = random_between(0, min(cap, base * 2^attempt)); starts: 1s, 2-3s, 4-6s, cap 32-60s, max 3-5 attempts. Retry only 429 (rate limit) among 4xx, read retry-after header if present. Use retry budget: total retries ≤10% of requests, fail fast otherwise. Single retry layer (outermost). Handle dual RPM/TPM limits; TPM binds for long prompts/agents.

Circuit breakers: trip on >20% failure/60s, immediate fail during open state. Parallel hedging: simultaneous primary/secondary requests, use first response. Request queue enforces TPM/RPM. Never retry blindly to avoid storms amplifying to 3^layers calls.

-----

</details>

<details>
<summary>What are proven patterns for LLM-based intent classification to enable conditional routing in customer support workflows, including prompt design and evaluation?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://www.emergentmind.com/topics/llm-based-prompt-routing

Query: What are proven patterns for LLM-based intent classification to enable conditional routing in customer support workflows, including prompt design and evaluation?

Answer: LLM-Based Prompt Routing involves dynamic selection of LLMs, prompts, or pathways for inputs using mechanisms like semantic routers, dynamic bandits, and hybrid orchestration. Key patterns include semantic routing (embeddings and thresholding for intent mapping, decoupling free-text from orchestration), pre-generation routing (classifiers or embeddings before LLM), post-generation (cascade) routing (lightweight model first, escalate if needed), embedding/similarity-based (cosine similarity to descriptors), supervised classifiers (fine-tuned transformers for query-to-model), RL/bandits (feedback-optimized policies), and multi-objective optimization. Motivations: cost/latency efficiency, specialization, reliability. Evaluation via deferral curves (quality-cost trade-offs on benchmarks like MMLU). Architectures: semantic routers for intent, contextual bandits for real-time adaptation. Performance: up to 50x latency reduction, 60% cost savings. Prompt engineering for fairness/alignment. No specific customer support prompts, but applicable to workflows with varying intents.

-----

-----

Phase: [EXPLOITATION]

### Source [12]: https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot

Query: What are proven patterns for LLM-based intent classification to enable conditional routing in customer support workflows, including prompt design and evaluation?

Answer: For LLM intent classification in chatbots/customer support: Define intents (e.g., Order Status, Product Info, Payments, Returns, Feedback, Other fallback). Prompt design: System prompt like 'You’re a LLM that detects intent... output only the intent topic' with descriptions. Use few-shot prompts or function calling for structured output. Handler logic per intent (e.g., API calls, text responses). Evaluation: Test every path with varied queries, evaluate prompts/models at scale (e.g., 200 test cases across 4 models using Vellum). Continuous monitoring post-production. Fallback 'Other' for unclear queries. Example for e-commerce support routing to actions like API for returns or LLM for product info.

-----

-----

Phase: [EXPLOITATION]

### Source [13]: https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/

Query: What are proven patterns for LLM-based intent classification to enable conditional routing in customer support workflows, including prompt design and evaluation?

Answer: Proven LLM routing patterns: Semantic (embeddings for intent similarity, e.g., customer support vs code), Intent-Based (query complexity/domain via multi-signal: domain, complexity, format, safety), Cascading (cheap model first, escalate on quality checks), Cost-Aware (cheaper for simple queries). For customer support: route simple to Haiku, complex to Sonnet (reduced spend $42k to $18k). vLLM Semantic Router uses ModernBERT. Multi-layer: load balancing first, then intent/cost. Evaluation: cost/quality/latency metrics, A/B tests. No specific prompts, but signals like domain classification.

-----

-----

Phase: [EXPLOITATION]

### Source [14]: https://arxiv.org/html/2502.08773v1

Query: What are proven patterns for LLM-based intent classification to enable conditional routing in customer support workflows, including prompt design and evaluation?

Answer: Universal Model Routing for dynamic LLM pools: Represent LLMs via correctness vectors on validation prompts, cluster-based routing (K-means on query embeddings, per-cluster errors), learned cluster maps. Optimal rule: argmin [expected loss + λ cost]. Pre-generation (embeddings/classifiers), post-generation cascading. Evaluation: deferral curves (quality vs cost on benchmarks like MMLU). Handles unseen LLMs without retraining. Applicable to workflows by clustering intents/complexity. No customer support specifics or prompts.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/

Query: What are proven patterns for LLM-based intent classification to enable conditional routing in customer support workflows, including prompt design and evaluation?

Answer: Multi-LLM routing for customer support: Static (UI per task), Dynamic: LLM-assisted (classifier LLM routes e.g., billing/tech), Semantic (embeddings match reference prompts), Hybrid (semantic for dept, classifier for complexity/urgency). Amazon Bedrock Intelligent Prompt Routing (cost/quality optimized within families). Customer support example: semantic to dept (billing/support), then classifier for escalation. Evaluation implied via cost/latency/accuracy trade-offs. No explicit prompts.

-----

</details>

<details>
<summary>In what types of unpredictable tasks does the orchestrator-worker pattern provide advantages over both fixed chaining and static parallelization for dynamic task decomposition?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://agents.kour.me/orchestrator-worker/

Query: In what types of unpredictable tasks does the orchestrator-worker pattern provide advantages over both fixed chaining and static parallelization for dynamic task decomposition?

Answer: The Orchestrator-Worker pattern provides advantages over fixed chaining and static parallelization in unpredictable tasks requiring dynamic task decomposition. It excels in complex, multifaceted tasks where subtasks are unpredictable and cannot be predetermined, must be determined at runtime based on input. Unlike rigid, predefined workflows (fixed chaining), the orchestrator dynamically breaks down goals into subtasks at runtime, enabling adaptability to unpredictable requirements. Unlike static parallelization with predetermined tasks, it offers dynamic flexibility where the orchestrator analyzes high-level goals and decides necessary subtasks, leveraging specialization and parallelization for independent subtasks. Ideal for: complex tasks requiring diverse expertise (e.g., research, writing, coding); dynamic task requirements; long-horizon tasks; when subtasks need runtime determination. Decision guidelines: use when benefits of specialization, parallelization, and dynamic decomposition outweigh complexity—specifically for unpredictable subtasks needing diverse expertise. Avoid for fixed workflows or simple tasks. Problem it solves: complex tasks with unpredictable subtasks that rigid workflows can't handle effectively.

-----

-----

Phase: [EXPLOITATION]

### Source [17]: https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent

Query: In what types of unpredictable tasks does the orchestrator-worker pattern provide advantages over both fixed chaining and static parallelization for dynamic task decomposition?

Answer: Orchestrator-Worker provides advantages over fixed chaining and static parallelization for dynamic task decomposition in unpredictable tasks. Key difference from static parallelization: tasks are not predetermined but dynamically decided by orchestrator based on query, with potentially different inputs per worker, then synthesized. Unlike fixed chaining (sequential), it enables dynamic adaptation, adjusting plans by skipping irrelevant subtasks or adding new ones. Effective for complex queries requiring multiple expertise types with intelligent coordination rather than predetermined parallel execution. Benefits: task decomposition into manageable subtasks for specialists; dynamic adaptation unlike fixed patterns.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/

Query: In what types of unpredictable tasks does the orchestrator-worker pattern provide advantages over both fixed chaining and static parallelization for dynamic task decomposition?

Answer: Orchestrator-Workers pattern advantages over fixed chaining and static parallelization in highly complex tasks where number and nature of subtasks cannot be known in advance (unpredictable). Central orchestrator dynamically decomposes tasks into sub-tasks at runtime, delegates to workers, unlike linear chains (fixed chaining) where steps are sequential. Enables parallelization of independent tasks simultaneously, providing 5-20x speed improvements over sequential processing, unlike static parallelization.

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers

Query: In what types of unpredictable tasks does the orchestrator-worker pattern provide advantages over both fixed chaining and static parallelization for dynamic task decomposition?

Answer: Orchestrator-workers excels over fixed chaining and static parallelization in complex tasks where subtasks can't be predicted in advance, requiring dynamic determination. Unlike hardcoded parallelization with pre-defined subtasks or manual sequential prompting (fixed chaining), central LLM dynamically analyzes task and determines best subtasks at runtime based on specific input, offering flexibility and adaptability. Well-suited when subtasks aren't pre-defined but decided by orchestrator.

-----

</details>

<details>
<summary>What real-world case studies demonstrate measurable accuracy and debugging improvements when refactoring a monolithic LLM task into a sequential FAQ generation chain like questions then answers then sources?</summary>

Phase: [EXPLOITATION]

### Source [20]: https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works

Query: What real-world case studies demonstrate measurable accuracy and debugging improvements when refactoring a monolithic LLM task into a sequential FAQ generation chain like questions then answers then sources?

Answer: Clipping, an educational technology startup, developed ClippingGPT, an AI tutor that leverages a specialized knowledge base and embeddings to significantly improve LLM accuracy, achieving a 26% performance increase over GPT-4 on the Brazilian Diplomatic Career Examination by prioritizing factual recall before response generation. This demonstrates how domain-specific knowledge integration can enhance LLM accuracy for educational applications. Acxiom leveraged LLMs and LangChain to create an audience segmentation system, but faced challenges in debugging complex workflows. By implementing LangSmith for observability, they gained visibility into multi-agent interactions, optimized token usage, and scaled their hybrid model deployment effectively. AppFolio developed Realm-X Assistant, a property management AI copilot, using LangGraph for complex workflow management and LangSmith for monitoring and debugging, achieving a significant performance boost in text-to-data functionality from 40% to 80% through dynamic few-shot prompting and saving users over 10 hours per week. Athena Intelligence developed Olympus, an AI-powered platform for generating enterprise research reports, leveraging LangChain for model abstraction and tool integration, LangGraph for orchestrating complex multi-agent workflows, and LangSmith for development and production monitoring. This stack enabled them to handle complex data tasks, generate high-quality reports with accurate source citations, and achieve significant improvements in development speed and system reliability. Airtop utilized the LangChain ecosystem to develop a web automation platform, enabling AI agents to interact with websites using natural language, featuring modular architecture for easy LLM switching and LangGraph for building scalable agents with built-in validation. The platform includes an Extract API for data retrieval and an Act API for real-time interactions, with LangSmith providing debugging and testing capabilities to ensure production reliability.

-----

-----

Phase: [EXPLOITATION]

### Source [21]: https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works

Query: What real-world case studies demonstrate measurable accuracy and debugging improvements when refactoring a monolithic LLM task into a sequential FAQ generation chain like questions then answers then sources?

Answer: No direct case studies on sequential FAQ generation chains, but related improvements in accuracy and debugging: Acxiom leveraged LLMs and LangChain to create an audience segmentation system, but faced challenges in debugging complex workflows. By implementing LangSmith for observability, they gained visibility into multi-agent interactions, optimized token usage, and scaled their hybrid model deployment effectively. AppFolio developed Realm-X Assistant, a property management AI copilot, using LangGraph for complex workflow management and LangSmith for monitoring and debugging, achieving a significant performance boost in text-to-data functionality from 40% to 80% through dynamic few-shot prompting. Athena Intelligence developed Olympus, an AI-powered platform for generating enterprise research reports, leveraging LangChain for model abstraction and tool integration, LangGraph for orchestrating complex multi-agent workflows, and LangSmith for development and production monitoring. This stack enabled them to handle complex data tasks, generate high-quality reports with accurate source citations, and achieve significant improvements in development speed and system reliability. Airtop utilized the LangChain ecosystem to develop a web automation platform, enabling AI agents to interact with websites using natural language, featuring modular architecture for easy LLM switching and LangGraph for building scalable agents with built-in validation. The platform includes an Extract API for data retrieval and an Act API for real-time interactions, with LangSmith providing debugging and testing capabilities to ensure production reliability.

-----

</details>

<details>
<summary>What are practical techniques to mitigate information loss and context degradation when chaining multiple specialized LLM calls for complex tasks?</summary>

Phase: [EXPLOITATION]

### Source [22]: https://futureagi.substack.com/p/how-tool-chaining-fails-in-production

Query: What are practical techniques to mitigate information loss and context degradation when chaining multiple specialized LLM calls for complex tasks?

Answer: Research shows that LLMs lose performance on information buried in the middle of long contexts, even with large context windows. When an agent forgets a user constraint from step 1 by the time it reaches step 5, the output may be technically valid but factually wrong. The user asked for revenue in USD, but the agent lost that detail three tool calls ago.

There are practical fixes. Use structured state objects instead of raw text to pass data between tool calls, keeping the payload compact and parseable. Summarize intermediate results before passing them forward by stripping out metadata the next tool does not need. Use frameworks like LangGraph that provide explicit state management across graph nodes, keeping context durable and inspectable.

Context preservation is the ability to maintain relevant information as data flows from one tool call to the next. LLMs operate within a finite context window, and every tool call adds tokens to that window through function parameters, response payloads, and the agent’s reasoning about what to do next. In long chains, critical context from early steps can be pushed out of the window or diluted by intermediate results.

Implement circuit breakers. If a tool fails or returns unexpected results more than N times, break the circuit and return a graceful failure. This prevents one broken tool from taking down the entire workflow.

Keep chains short. Longer chains mean more failure opportunities and more context consumption. If your chain needs more than five or six sequential calls, restructure into sub-chains or parallel branches.

Test with adversarial inputs. Standard test cases will pass. Production traffic will not be standard. Test with empty responses, large payloads, unexpected types, and ambiguous queries.

Use plan-then-execute architecture. Research from Scale AI shows that having the LLM formulate a structured plan first and then running it through a deterministic executor reduces tool chaining errors significantly. This separates reasoning from execution.

Validate at every boundary. Add input and output validation between every tool call using Pydantic or JSON Schema. Explicit validation catches errors at the source before they propagate.

-----

-----

Phase: [EXPLOITATION]

### Source [23]: https://aclanthology.org/2025.acl-long.1089.pdf

Query: What are practical techniques to mitigate information loss and context degradation when chaining multiple specialized LLM calls for complex tasks?

Answer: The biggest challenge of RAG lies in how to retrieve relevant and comprehensive information. One solution is to perform multiple rounds of retrieval to gather relevant passages. The other solution seeks to remove irrelevant information from retrieved texts. Recent work pays more attention to the effective utilization of retrieved texts using techniques like gist memory, text summarization, reranking, context compression.

Sub-context integration. We remove duplicate contexts from all retrieved sentences (without using sub-questions) and use a cross-encoder to rerank the sentences for generating the final answer. This method is similar to traditional RAG, which uses only relevant text to generate the answer. It helps mitigate the impact of errors in sub-question decomposition or answers by focusing on the retrieved sentences, rather than relying solely on the sub-question answers. However, this method explicitly requires the LLM to have strong long-context processing capabilities to effectively process the merged and potentially extensive context. Compared to answering each sub-question individually, the merged context may contain more noisy information and negatively impact the final answer.

This method generates the answer to the original question by utilizing each sub-question and its answer. It relies solely on the information from the sub-questions’ answers, without external interference. Since the decomposition of sub-questions can be regarded as a reasoning process, this method enables the LLM to infer the original question’s answer. Moreover, this method ensures that the LLM processes the relevant text of only one sub-question at a time, avoiding performance degradation caused by the LLM’s weak long-context processing capabilities when processing multiple sub-questions simultaneously. Consequently, this method does not require the LLM strong long-context processing capabilities, as the final synthesis relies exclusively on the concise information from the sub-questions’ answers.

ChainRAG, a progressive retrieval framework called ChainRAG. It involves an iterative process of sentence retrieval, sub-question answering and subsequent sub-question rewriting. We first construct a sentence graph with named entity indexing from texts, which is used to facilitate entity completion in sub-question rewriting and to structure the knowledge scattered across different texts. Next, given an input question, we employ the LLM to decompose it into several sub-questions and retrieve relevant sentences for the first sub-question. Then, our iterative process operates as follows until all sub-questions are addressed. We prompt an LLM to answer the current sub-question. The answer is then used to rewrite the next sub-question by completing any missing key entities, if possible. The updated sub-question is subsequently used for retrieval. Finally, all retrieved sentences and sub-question answers are integrated to answer the original question.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://milvus.io/blog/keeping-ai-agents-grounded-context-engineering-strategies-that-prevent-context-rot-using-milvus.md

Query: What are practical techniques to mitigate information loss and context degradation when chaining multiple specialized LLM calls for complex tasks?

Answer: For complex tasks, a multi-agent architecture can be designed where a lead agent oversees the overall work, while several specialized sub-agents handle specific aspects of the task. These sub-agents dive deep into large amounts of data related to their sub-tasks but only return the concise, essential results. This approach is commonly used in scenarios like research reports or data analysis.

In practice, it’s best to start by using a single agent combined with compression to handle the task. External storage should only be introduced when there’s a need to retain memory across sessions. The multi-agent architecture should be reserved for tasks that genuinely require parallel processing of complex, specialized sub-tasks.

Retrieval is one of the most effective levers we have to combat context rot, and in practice it tends to show up in complementary patterns that address context rot from different angles.

Just-in-Time Retrieval: Reducing Unnecessary Context. One major cause of context rot is overloading the model with information it doesn’t need yet. Claude Code—Anthropic’s coding assistant—solves this issue with Just-in-Time (JIT) retrieval, a strategy where the model fetches information only when it becomes relevant.

Pre-retrieval (Vector Search): Preventing Context Drift Before It Starts. Context rot often happens because the model is handed a large pile of raw text and expected to sort out what matters. Pre-retrieval flips that: a vector database identifies the most relevant pieces before inference, ensuring only high-value context reaches the model.

Hybrid JIT and Vector Retrieval. Vector search for stable, high-confidence knowledge. Agent-driven JIT exploration for information that evolves or only becomes relevant mid-task.

When the context window approaches its limit, the model can compress earlier interactions into concise summaries. Good compression keeps Key decisions, Constraints and requirements, Outstanding issues, Relevant samples or examples. And removes Verbose tool outputs, Irrelevant logs, Redundant steps.

Structured Note-Taking: Move Stable Information Outside Context. Instead of keeping everything inside the model’s window, the system can store important facts in external memory—a separate database or a structured store that the agent can query as needed.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://www.morphllm.com/context-rot

Query: What are practical techniques to mitigate information loss and context degradation when chaining multiple specialized LLM calls for complex tasks?

Answer: Context isolation through subagent architectures. Delegate search to specialized agents with their own context windows. The coding model only sees condensed results, never the search process. Anthropic's multi-agent system improved performance by 90.2% with this approach. FlashCompact implements this with WarpGrep (search isolation), Fast Apply (compact diffs at 10,500 tok/s), and Morph Compact (verbatim cleanup at 3,300+ tok/s).

The fix for context rot isn’t making models better at long contexts. It’s keeping their context short.

Anthropic's multi-agent research system demonstrated this directly. Their architecture (an Opus 4 lead agent delegating to Sonnet 4 subagents) outperformed a single Opus 4 agent by 90.2% on research tasks. The lead agent typically spawns 3-5 subagents in parallel, each using 3+ tools simultaneously. Simple tasks use 1 agent with 3-10 tool calls. Complex research deploys 10+ subagents.

The performance gain isn’t because the subagents are smarter. It’s because the lead agent’s context stays clean. Each subagent explores, backtracks, and discards dead ends in its own context window. The lead agent never sees the 15 files that were explored and rejected. It only sees the condensed result.

Lead Agent Holds task-level context: the goal, the plan, high-level progress. Never polluted with search traces or dead-end explorations.

Search Subagent Explores in its own context window. Reads, rejects, and backtracks without polluting the parent. Returns only relevant file and line ranges.

Condensed Return Subagent returns 50-200 tokens of precise context. The lead agent never sees the 15 files that were explored and rejected.

FlashCompact: Prevention Over Compression. Most approaches to context rot are reactive: they wait for context to fill up, then compress it. FlashCompact is preventive: it stops noise from entering context in the first place.

The system has three components, each addressing a different source of context waste: WarpGrep: Search Isolation. RL-trained search subagent. 0.73 F1 in 3.8 steps. Returns only relevant code snippets, not entire files. Fast Apply: Compact Diffs. 10,500 tok/s. Generates surgical edit diffs instead of full-file rewrites. Morph Compact: Verbatim Cleanup. 3,300+ tok/s. Removes remaining noise from conversation history without summarization loss.

-----

</details>

<details>
<summary>What Python coding patterns using asyncio or threading minimize latency in parallel LLM calls for independent subtasks like answering multiple FAQ questions simultaneously?</summary>

Phase: [EXPLOITATION]

### Source [26]: https://santhalakshminarayana.github.io/blog/concurrency-patterns-python

Query: What Python coding patterns using asyncio or threading minimize latency in parallel LLM calls for independent subtasks like answering multiple FAQ questions simultaneously?

Answer: For I/O-bound tasks like network calls to LLMs, use coroutines with asyncio for concurrency. The WorkerPool pattern implements a job queue with multiple workers using asyncio.Queue and asyncio.gather(*tasks) to process n-jobs concurrently with m-workers (n >= m). Jobs are added to a Queue, workers (coroutines) continuously fetch jobs with await self.job_queue.get(), process with await self.callback(job), and mark task_done(). This achieves concurrent execution in a single thread, processing 10 jobs (1-4s each, total 21s sequential) in 8s. CustomCoroutine class runs asyncio event loops in separate threads for async callbacks. Use for independent subtasks like multiple FAQ answers to minimize latency by overlapping I/O waits without thread overhead or GIL issues. Pipeline pattern chains processing steps concurrently across workers. Avoid threads for large-scale due to memory/context switching; coroutines handle thousands efficiently.

-----

-----

Phase: [EXPLOITATION]

### Source [27]: https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a

Query: What Python coding patterns using asyncio or threading minimize latency in parallel LLM calls for independent subtasks like answering multiple FAQ questions simultaneously?

Answer: LLM calls are I/O-bound (network requests), so use asyncio with asyncio.gather() for concurrent execution: async def fetch_url(session, url): async with session.get(url) as response: return await response.text(); async def main(): async with aiohttp.ClientSession() as session: tasks = [fetch_url(session, url) for url in urls]; results = await asyncio.gather(tasks). Benchmarks: AsyncIO fetches 100 URLs in 2.3s (19.7x faster than sequential), outperforming Threading (3.1s) due to no OS thread switching overhead. Best practices: Use connection pooling (aiohttp.ClientSession), timeouts, asyncio.gather for parallel tasks, asyncio.create_task for fire-and-forget. Threading with ThreadPoolExecutor suitable alternative for blocking libs like requests, but higher overhead. Avoid multiprocessing (4.8s) due to process startup costs. Hybrid: asyncio.run_in_executor for any CPU parts. Scales to 10k+ connections with minimal memory.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://testdriven.io/blog/python-concurrency-parallelism/

Query: What Python coding patterns using asyncio or threading minimize latency in parallel LLM calls for independent subtasks like answering multiple FAQ questions simultaneously?

Answer: For I/O-bound tasks like HTTP requests (analogous to LLM API calls), asyncio.gather with async clients (httpx.AsyncClient) minimizes latency: async def main(): async with httpx.AsyncClient() as client: return await asyncio.gather(*[make_request_async(num, client) for num in range(1,101)]). Benchmark: 100 requests in 0.55s vs Threading (1.02-1.34s) vs sequential (15.7s), due to coroutines avoiding OS thread context switches; event loop optimally yields control. ThreadPoolExecutor: with ThreadPoolExecutor() as executor: futures = [executor.submit(make_request, num) for num in range(1,101)]; wait(futures) - 1.34s, limited by GIL/OS overhead. Prefer asyncio for high concurrency I/O like multiple independent FAQ/LLM calls; uses min memory, no race conditions (single-threaded). concurrent.futures abstracts switching.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://dev.to/nkpydev/concurrency-and-parallelism-in-python-threads-multiprocessing-and-async-programming-64d

Query: What Python coding patterns using asyncio or threading minimize latency in parallel LLM calls for independent subtasks like answering multiple FAQ questions simultaneously?

Answer: For I/O-bound API calls (like LLMs), use asyncio with aiohttp: async def fetch(url): async with aiohttp.ClientSession() as session: async with session.get(url) as response: return await response.text(); async def main(): tasks = [fetch(url) for url in urls]; results = await asyncio.gather(*tasks). Faster than requests for multiple calls; non-blocking. ThreadPoolExecutor for simpler concurrent I/O: with ThreadPoolExecutor(max_workers=3) as executor: executor.map(fetch_data, sites). Async handles thousands concurrently via event loops; ideal for web scraping/API calls/FAQ subtasks. Threads for I/O with blocking libs.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://blog.jetbrains.com/pycharm/2025/06/concurrency-in-async-await-and-threading/

Query: What Python coding patterns using asyncio or threading minimize latency in parallel LLM calls for independent subtasks like answering multiple FAQ questions simultaneously?

Answer: For concurrent I/O (like LLM calls), use asyncio.Queue for task distribution: workers await task_queue.get(), await task, task_done(); asyncio.gather(*workers). Example: multiple make_burger/make_fries tasks queued, 2 staff process concurrently, overlapping waits via await asyncio.sleep (simulates I/O). asyncio.to_thread(input, ...) unblocks blocking I/O. Threading equivalent uses queue_lock, pop(0) under lock to avoid races; staff threads while True: with lock check/pop/execute. Async easier (no locks/races, cooperative yielding). Both cut wait time for I/O-bound: 3 burgers sequential 15s -> concurrent 5s; limited workers 10s. Prefer async for simplicity/scalability in network subtasks.

-----

</details>

<details>
<summary>What are key implementation considerations for synthesizing results from dynamically generated subtasks in an orchestrator LLM for complex customer service inquiries?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers

Query: What are key implementation considerations for synthesizing results from dynamically generated subtasks in an orchestrator LLM for complex customer service inquiries?

Answer: The orchestrator-workers pattern features a central LLM that dynamically delegates tasks to worker LLMs and synthesizes their combined results. It operates in two phases: Analysis & Planning Phase where the orchestrator analyzes the task and generates structured subtask descriptions in XML format; Execution Phase where worker LLMs receive the original task, subtask type, description, and context to generate responses. The FlexibleOrchestrator class processes tasks by parsing orchestrator response for analysis and tasks, then runs each worker in parallel, collecting results as a list of dicts with type, description, and result. Key design decisions include using XML for structured subtask output, validating worker responses and handling empty outputs with error messages, and returning a dict with analysis and worker_results for synthesis. Limitations include cost & latency from multiple LLM calls (suggest asyncio for parallelization), potential for orchestrator to generate poor subtasks, and workers producing low-quality outputs. Enhancements: parallel execution with asyncio, quality filtering, recursive orchestration, and dynamic worker selection.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent

Query: What are key implementation considerations for synthesizing results from dynamically generated subtasks in an orchestrator LLM for complex customer service inquiries?

Answer: The Orchestrator-Worker pattern involves an Orchestrator LLM that analyzes the user’s request and creates a plan by breaking it into subtasks, Workers as specialized chains handling subtasks, and a Synthesizer LLM that takes all worker outputs and integrates them into a coherent final answer. The flow: Orchestrator creates structured JSON plan with subtasks specifying worker type and instructions; workers execute in parallel if desired; synthesizer integrates diverse outputs. Implementation uses different LLMs: capable model for orchestrator and synthesizer (temperature=0 for consistency), faster/cheaper for workers. For complex analysis like product launch, orchestrator dynamically decides subtasks for technical, market, risk workers. Key benefits: task decomposition, specialization, scalability, dynamic adaptation. The synthesizer ensures coherent final answer from diverse subtask results.

-----

-----

Phase: [EXPLOITATION]

### Source [34]: https://www.socure.com/tech-blog/build-advanced-customer-support-llm-multi-agent-workflow

Query: What are key implementation considerations for synthesizing results from dynamically generated subtasks in an orchestrator LLM for complex customer service inquiries?

Answer: In the multi-agent LLM support framework for customer support, a Supervisor Node (Intent Classifier) infers intent and selects up to three relevant specialized agents (e.g., DevHub, Troubleshooting) which execute in parallel, each generating proposed answers with RAG and tools. An Answer Evaluation node compares outputs using LLM chain based on accuracy, relevance, clarity, confidence scores, excluding empty answers, prioritizing high confidence/detailed responses, selecting the best or longest if tied. Response includes citations, confidence, latency, agent used. Human-in-loop with confidence thresholds escalates low-confidence cases. Feedback (thumbs up/down) logged for evaluation. State includes rephrased input, preferred tasks, chat history, final_answer, citations, confidence. For complex inquiries, parallel execution and LLM-based selection synthesize best subtask result into coherent response.

-----

</details>

<details>
<summary>How do modular chaining, routing, and orchestration patterns contribute to more reliable and maintainable systems in the broader landscape of AI engineering workflows?</summary>

Phase: [EXPLOITATION]

### Source [35]: https://productschool.com/blog/artificial-intelligence/ai-agent-orchestration-patterns

Query: How do modular chaining, routing, and orchestration patterns contribute to more reliable and maintainable systems in the broader landscape of AI engineering workflows?

Answer: Orchestration patterns like planner-executor loops, hierarchical task decomposition, tool-routing, guardrails/verification loops, and agent handoff protocols enhance reliability and maintainability in AI systems. Hierarchical task decomposition creates multi-level command chains where top-level manager agents delegate to subordinates, enabling parallelization, oversight at each layer for safety, and separation of concerns that makes maintenance easier for complex domains like software design or multi-step workflows. Tool-routing allows dynamic tool/model selection at runtime, improving performance by using lightweight tools for simple tasks, enhancing safety with specialized checkers, reducing costs, and offering flexibility to add new tools without reengineering, thus making systems more adaptable and maintainable. Planner-executor loops split reasoning and action, allowing scalable addition of new executors without retraining, improving throughput on complex tasks with parallel subtasks. Guardrails/verification loops ensure safety and correctness by checking outputs, catching errors early to avoid wasted work, building trust through automation. Agent handoff protocols enable modular systems where specialists focus on domains, scalable by adding new agents without reworking existing ones. Keeping architecture modular allows swapping patterns easily, starting simple and evolving, avoiding untrustworthy, undebuggable systems. Hybrid approaches combine patterns for balanced performance, safety, latency, and cost in production AI products.

-----

-----

Phase: [EXPLOITATION]

### Source [36]: https://www.decodingai.com/p/stop-building-ai-agents-use-these

Query: How do modular chaining, routing, and orchestration patterns contribute to more reliable and maintainable systems in the broader landscape of AI engineering workflows?

Answer: Modular chaining (prompt chaining) connects multiple LLM calls sequentially, breaking complex tasks into smaller, focused sub-tasks for improved reliability as simpler prompts reduce confusion and incomplete results. It enhances modularity with each call on specific tasks, accuracy from targeted prompts, easier debugging by isolating issues, and flexibility to swap/optimize components independently (e.g., cheaper models for simple steps). Orchestrator-Worker pattern dynamically decomposes tasks via central LLM orchestrator delegating to parallel workers, similar to Map-Reduce, enabling scalability and efficiency. Routing uses conditional logic/LLM classifiers to direct workflows to specialized paths based on input, keeping prompts optimized, avoiding monolithic prompts that degrade performance, with default routes for robustness. Parallelization runs independent tasks concurrently to reduce latency. Evaluator-Optimizer creates feedback loops for self-correction, improving output quality. These patterns solve 95% of production problems with controllability over agents' complexity, emphasizing workflows over agents for reliability, starting simple and escalating only if needed, making systems more maintainable and cost-effective.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems

Query: How do modular chaining, routing, and orchestration patterns contribute to more reliable and maintainable systems in the broader landscape of AI engineering workflows?

Answer: Orchestration patterns (Supervisor, Adaptive Agent Network, Custom) turn agent collections into scalable, reliable multi-agent systems by defining interactions, context sharing, collaboration for complex tasks, affecting performance, safety, cost, scalability. Supervisor pattern uses central orchestrator for decomposition, delegation, monitoring, validation in hierarchical control, ensuring transparency, quality assurance, traceability for complex workflows. Adaptive Agent Network enables decentralized collaboration with direct task transfers, optimized for low-latency, maintaining context integrity without overhead. Custom pattern offers programmatic control via SDK for compliance/integration. Choice balances control/flexibility; simplest effective pattern recommended. Enables enterprise-grade reliability, scalability matching operational needs.

-----

-----

Phase: [EXPLOITATION]

### Source [39]: https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/

Query: How do modular chaining, routing, and orchestration patterns contribute to more reliable and maintainable systems in the broader landscape of AI engineering workflows?

Answer: Orchestrator-Workers pattern scales complex tasks: central Orchestrator decomposes, delegates to parallel specialized Workers (cheap models for scoped tasks), enabling 5-20x speedups, economic optimization, efficiency over linear chains. Reflexion pattern adds self-healing via Actor-Critic loops: Actor attempts task, Evaluator checks, self-reflects on failures, retries conditioned on critique, reducing errors (e.g., VIGIL catches all failures). Finite State Machines (FSMs) enforce valid state transitions as guardrails against non-determinism, ensuring process adherence. Graph-based orchestrators like LangGraph support loops/Reflexion unlike linear chains, providing explicit state management for production reliability and maintainability in enterprise AI.

-----

</details>

<details>
<summary>What are proven prompt engineering techniques for decomposing complex content generation tasks like FAQ creation from renewable energy materials into focused subtasks for questions, answers, and citations?</summary>

Phase: [EXPLOITATION]

### Source [40]: https://www.lennysnewsletter.com/p/five-proven-prompt-engineering-techniques

Query: What are proven prompt engineering techniques for decomposing complex content generation tasks like FAQ creation from renewable energy materials into focused subtasks for questions, answers, and citations?

Answer: Proven prompt engineering techniques for decomposing complex content generation tasks include breaking tasks into subtasks via advanced tactics like Synthetic bootstrap, Few-shot learning, and Style unbundling. Synthetic bootstrap uses AI to generate multiple examples from inputs for in-context learning, useful when lacking real examples, e.g., generating user personas then using them for feedback. Few-shot learning provides examples to guide format/style. For complex tasks, split into steps rather than one prompt to correct errors. Bonus advanced tactics involve splitting tasks into multiple steps for robust outcomes, anticipating continued usefulness.

-----

-----

Phase: [EXPLOITATION]

### Source [41]: https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a

Query: What are proven prompt engineering techniques for decomposing complex content generation tasks like FAQ creation from renewable energy materials into focused subtasks for questions, answers, and citations?

Answer: Prompt Chaining decomposes complex tasks into sequential sub-goals: split into sub-tasks where each output feeds the next prompt, maintaining context. Ideal for content creation like reports or FAQs from materials—e.g., for FAQ from renewable energy materials: Prompt 1: List key topics/questions; Prompt 2: Expand each into detailed answers; Prompt 3: Add citations; Prompt 4: Format as FAQ. Benefits: reduces ambiguity, ensures coherence, allows refinement. Use cases: lengthy content generation, strategic analysis. Limitations: time-consuming, error propagation risk. Chain-of-Thought (CoT) breaks reasoning into steps for logic tasks. RAG retrieves sources for cited answers.

-----

-----

Phase: [EXPLOITATION]

### Source [42]: https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation

Query: What are proven prompt engineering techniques for decomposing complex content generation tasks like FAQ creation from renewable energy materials into focused subtasks for questions, answers, and citations?

Answer: Decomposition breaks complex tasks into smaller sub-tasks via chained prompts, output of one as input to next. Example for marketing plan (analogous to FAQ): Step 1: Identify user types; Step 2: Suggest hooks per type; Step 3: Write captions per hook/platform. For FAQ creation: Step 1: Extract key topics from materials; Step 2: Generate questions; Step 3: Draft answers; Step 4: Add citations. Iterative Prompting/Prompt Chaining uses back-and-forth for refinement. Retrieval-Augmented Generation (RAG) fetches sources for citations in knowledge-heavy tasks like renewable energy FAQs.

-----

-----

Phase: [EXPLOITATION]

### Source [44]: https://www.k2view.com/blog/prompt-engineering-techniques/

Query: What are proven prompt engineering techniques for decomposing complex content generation tasks like FAQ creation from renewable energy materials into focused subtasks for questions, answers, and citations?

Answer: Chain-of-Thought (CoT) decomposes complex tasks into sub-steps for reasoning, e.g., step-by-step for multi-part generation like FAQs: outline questions, then answers, then citations. Few-shot provides examples for subtasks. Techniques like meta prompting structure logical steps abstractly. For content from materials, combine with RAG for grounded citations. Self-consistency generates multiple paths for consistent outputs across subtasks.

-----

</details>

<details>
<summary>How does parallel execution of independent LLM subtasks impact error propagation, debugging strategies, and overall system reliability compared to purely sequential chains?</summary>

Phase: [EXPLOITATION]

### Source [45]: https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/

Query: How does parallel execution of independent LLM subtasks impact error propagation, debugging strategies, and overall system reliability compared to purely sequential chains?

Answer: Parallel execution of independent steps in multi-step LLM chains reduces latency, as in summarizing multiple documents concurrently before synthesis. For error handling and debugging, wrap each step in try-catch blocks to gracefully manage exceptions, logging errors with context like input, prompt, and step for easier debugging. Modular design promotes testing, debugging, and maintenance. Robust monitoring tracks metrics like latency, cost, and output quality; debugging uses logging of inputs/prompts/outputs, prompt introspection, A/B tests, correlation IDs to track across steps. Optimization includes parallel execution of independent steps to optimize latency. Fallback logic anticipates failures like irrelevant outputs or API errors. Robust monitoring, debugging techniques like prompt introspection, and orchestration best practices such as modular design, fallback logic, state management enhance scalability and robustness, improving reliability. Avoiding pitfalls like brittle chaining logic improves reliability. Compared to sequential, parallel execution is recommended when steps are independent to reduce latency, with error handling crucial for reliability.

-----

-----

Phase: [EXPLOITATION]

### Source [46]: https://mlpills.substack.com/p/issue-110-llm-workflow-patterns

Query: How does parallel execution of independent LLM subtasks impact error propagation, debugging strategies, and overall system reliability compared to purely sequential chains?

Answer: Parallelisation pattern runs multiple LLM calls concurrently for independent subtasks, gathering and synthesizing results afterward. Excels when tasks are independent, multiple perspectives needed, or latency matters. Trade-offs include higher cost and coordination challenges in merging results. Prompt chaining (sequential) offers predictability, straightforward debugging by identifying exact stage of issues, modular and testable, thus reliable; lacks flexibility for conditional logic. Parallelisation contrasts by breaking linearity for speed but with coordination challenges, implying potentially harder debugging due to multiple paths, though not explicitly stated as less reliable. Overall, sequential chaining is more predictable and easier to debug than parallel.

-----

-----

Phase: [EXPLOITATION]

### Source [47]: https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge

Query: How does parallel execution of independent LLM subtasks impact error propagation, debugging strategies, and overall system reliability compared to purely sequential chains?

Answer: Compounding errors in LLMs occur in sequential processing where small inaccuracies propagate and accumulate through steps, as LLMs generate token-by-token using prior outputs. In complex problems broken into steps, each with error probability, final answer error chance grows exponentially; complex problems exponentially more error-prone. Sequential nature leads to cascading errors, hindering logical reasoning like math where initial error invalidates chain. Parallel execution not directly compared, but implies reduced propagation since independent subtasks lack dependency chain, potentially mitigating compounding by avoiding sequential error buildup.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://scalingintelligence.stanford.edu/pubs/sprint.pdf

Query: How does parallel execution of independent LLM subtasks impact error propagation, debugging strategies, and overall system reliability compared to purely sequential chains?

Answer: SPRINT enables interleaved planning and parallel execution in reasoning models, dynamically identifying parallelizable subtasks. Reduces sequential tokens (up to 39% on long trajectories) vs sequential reasoning, improving efficiency while matching or exceeding accuracy (e.g., 92.5% vs 91% on MATH500). Independent executions prevent one result influencing others, potentially reducing error propagation vs sequential chains. On longer trajectories, greater parallelization opportunities. Generalizes to out-of-domain tasks with token reductions (45-65%). Baselines like Skeleton-of-Thought underperform due to assuming mutual independence without interleaved feedback. Parallel execution of independent subtasks reduces sequential tokens compared to purely sequential processing. No explicit debugging mention, but structured planning/execution aids traceability. Reliability improved via higher accuracy and efficiency.

-----

</details>

<details>
<summary>What implementation patterns enable reliable conditional branching after LLM-based intent classification in customer service systems built with the Google Gemini SDK?</summary>

Phase: [EXPLOITATION]

### Source [49]: https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/

Query: What implementation patterns enable reliable conditional branching after LLM-based intent classification in customer service systems built with the Google Gemini SDK?

Answer: The Coordinator/Dispatcher Pattern (aka the concierge) is ideal for complex customer service bots. A central, intelligent agent acts as a dispatcher that analyzes the user's intent and routes the request to a specialist agent best suited for the job, such as sending a user to a 'Billing' specialist for invoice issues versus a 'Tech Support' specialist for troubleshooting. This relies on LLM-driven delegation. Define a parent CoordinatorAgent and provide a list of specialist sub-agents. The ADK's AutoFlow mechanism handles transferring execution based on the descriptions provided for the children. Example pseudocode: billing_specialist = LlmAgent(name='BillingSpecialist', description='Handles billing inquiries and invoices.', tools=[BillingSystemDB]); tech_support = LlmAgent(name='TechSupportSpecialist', description='Troubleshoots technical issues.', tools=[DiagnosticTool]); coordinator = LlmAgent(name='CoordinatorAgent', instruction='Analyze user intent. Route billing issues to BillingSpecialist and bugs to TechSupportSpecialist.', sub_agents=[billing_specialist, tech_support]). For robust Customer Support systems, use a Coordinator to route requests; if technical issue, trigger Parallel search of documentation and user history, then Generator and Critic loop for tone consistency (composite pattern). ADK is built for Google Gemini models.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://www.linkedin.com/posts/chiragsubramanian_agentic-ai-design-patterns-my-practical-activity-7416830806939230208-nRFc

Query: What implementation patterns enable reliable conditional branching after LLM-based intent classification in customer service systems built with the Google Gemini SDK?

Answer: Orchestrator-Worker Pattern: Orchestrator handles logic and routing; Workers handle focused subtasks like classify. Supports dynamic control flow. Intent-Based Routing: Route inputs based on classification or intent. Use cases: multi-domain assistants. Router dispatches tasks based on intent or conditions. State is a typed contract between agents, tracks inputs, intermediate outputs, decisions for validation, debugging, predictable scaling. Reflection Pattern: Evaluator critiques and scores output; Router decides whether to loop or finish.

-----

-----

Phase: [EXPLOITATION]

### Source [51]: https://www.decodingai.com/p/stop-building-ai-agents-use-these

Query: What implementation patterns enable reliable conditional branching after LLM-based intent classification in customer service systems built with the Google Gemini SDK?

Answer: Routing, or conditional logic, directs workflow down different paths based on input or intermediate state. An LLM acts as a classifier to make branching decisions, keeping prompts specialized. Ideal for customer support tool routing queries to specialized handlers for technical support, billing, or general questions. Include default or catch-all route. Example: media_type = classify_media_intent(user_intent); if media_type == 'diagram': generate_diagram; etc. Orchestrator-Worker pattern: central LLM (orchestrator) dynamically breaks down task into sub-tasks, delegates to specialized workers in parallel. Implement jobs as tools; orchestrator outputs multiple tool calls. Mentions Gemini API rate limits and Python client for Google’s Generative AI Models.

-----

</details>

<details>
<summary>What prompt design principles help an orchestrator LLM effectively break down unpredictable customer service queries into distinct delegable subtasks for parallel worker execution?</summary>

Phase: [EXPLOITATION]

### Source [52]: https://mlpills.substack.com/p/issue-110-llm-workflow-patterns

Query: What prompt design principles help an orchestrator LLM effectively break down unpredictable customer service queries into distinct delegable subtasks for parallel worker execution?

Answer: The Orchestrator–Worker pattern introduces hierarchy for large or multifaceted tasks. One LLM serves as the orchestrator, dividing work into smaller subtasks and delegating them to worker models specialized in specific domains. A synthesiser then integrates the diverse outputs into a unified final result. The orchestrator analyzes a query, sends subtasks to workers like summarisation, citation checker, and stylistic editor, then integrates results. This shines when the main task decomposes into specialised components, different tools or models are needed, or combining high-level reasoning with efficient execution. It encourages modularity and scalability. The main challenge is orchestration logic—deciding what to delegate, when, and how to integrate. Parallelisation runs many LLM calls at once for independent subtasks, gathering and synthesising results. Prompt chaining forms a linear sequence where each call feeds the next for ordered subtasks.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers

Query: What prompt design principles help an orchestrator LLM effectively break down unpredictable customer service queries into distinct delegable subtasks for parallel worker execution?

Answer: The orchestrator-workers pattern has a central LLM dynamically analyze each unique task and determine the best subtasks to delegate to specialized worker LLMs at runtime, making it adaptive for unpredictable inputs unlike pre-defined parallel workflows. It operates in two phases: Analysis & Planning where the orchestrator receives task and context, analyzes valuable approaches, and generates structured subtask descriptions in XML format; Execution where each worker receives the original task, its specific instructions, and context, producing focused outputs. Key design: Use structured XML for tasks with <analysis> explaining understanding and variations, and <tasks> with <task><type> and <description></task>. Worker prompts specify style/guidelines. The orchestrator decides subtasks based on input, e.g., for product descriptions, breaking into formal, conversational types. Benefits: flexibility for complex tasks where subtasks can't be predicted; generates tailored variations. Use when multiple perspectives needed but unpredictable; not for simple tasks or strict sequences.

-----

-----

Phase: [EXPLOITATION]

### Source [54]: https://www.anthropic.com/engineering/building-effective-agents????__hstc=43401018.9b17c4d3051a2af3f924a8d9f62fbbee.1757203200284.1757203200285.1757203200286.1&__hssc=43401018.1.1757203200287&__hsfp=2825657416

Query: What prompt design principles help an orchestrator LLM effectively break down unpredictable customer service queries into distinct delegable subtasks for parallel worker execution?

Answer: In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates to worker LLMs, and synthesizes results. Use for complex tasks where subtasks can't be predicted in advance (e.g., coding where number/nature of file changes depend on task). Key difference from parallelization: flexibility—subtasks determined by orchestrator based on specific input, not pre-defined. This suits unpredictable queries as the orchestrator analyzes at runtime. Combine with other patterns like parallelization for speed or multiple perspectives. For customer support, agents handle open-ended problems with conversation and action, clear success criteria, feedback loops; orchestration adds value for tasks requiring both.

-----

-----

Phase: [EXPLOITATION]

### Source [55]: https://www.scoutos.com/blog/ai-prompt-orchestration-techniques-and-tools-you-need

Query: What prompt design principles help an orchestrator LLM effectively break down unpredictable customer service queries into distinct delegable subtasks for parallel worker execution?

Answer: AI prompt orchestration organizes requests into workflows where one response feeds the next, dividing complicated requests into focused substeps for accuracy. For customer support chatbots, orchestrate to reference knowledge base, check policy, refine clarity. Benefits: consistency, reduced errors, scalability. Strategies: Plan stages in flowchart; use chain-of-thought/multi-step techniques; add reference data/RAG; monitor/evaluate. Example workflow: Collect docs/support tickets, prompt LLM for answers, pass to summarization/rewrite, check brand/compliance, deploy. This handles unpredictable queries by structuring into substeps like data retrieval, analysis, refinement.

-----

</details>

<details>
<summary>In what ways do modular workflow patterns like chaining and routing enhance pedagogical outcomes when teaching AI engineers to build reliable LLM applications step-by-step?</summary>

Phase: [EXPLOITATION]

### Source [56]: https://www.decodingai.com/p/stop-building-ai-agents-use-these

Query: In what ways do modular workflow patterns like chaining and routing enhance pedagogical outcomes when teaching AI engineers to build reliable LLM applications step-by-step?

Answer: Modular workflow patterns like chaining and routing enhance pedagogical outcomes in teaching AI engineers to build reliable LLM applications by providing a structured, step-by-step approach that mirrors real-world production challenges. The article is part of the 'AI Agents Foundations series'—a 9-part journey from Python developer to AI Engineer, designed for busy people to build skills and mental models for shipping real AI agents in production. It teaches 'how to fish' by writing everything from scratch, jumping into building blocks. Chaining improves modularity, with each LLM call focusing on specific sub-tasks, leading to enhanced accuracy via simpler prompts, easier debugging by isolating issues to specific links, and flexibility to swap/optimize components independently (e.g., cheaper models for simple steps). Prompt chaining breaks large problems into smaller sub-tasks with clearer objectives, improving reliability. Routing enables dynamic decisions, directing workflows based on input using LLM as classifier, keeping prompts specialized and following divide-and-conquer principle. The series roadmap includes these patterns before advancing to agents, emphasizing starting with simpler, controllable patterns: 1. Prompt Chaining, 2. Parallelization, 3. Routing, etc. This progression teaches engineers to solve 95% of production problems with workflows before agents, fostering deep understanding of design without framework reliance. Examples like writing workflows (chaining media assets, article text, title, SEO) demonstrate practical, step-by-step building. The approach avoids agent complexity pitfalls, teaching modularity, control, and optimization for reliable apps.

-----

-----

Phase: [EXPLOITATION]

### Source [57]: https://mlpills.substack.com/p/issue-110-llm-workflow-patterns

Query: In what ways do modular workflow patterns like chaining and routing enhance pedagogical outcomes when teaching AI engineers to build reliable LLM applications step-by-step?

Answer: Modular workflow patterns like chaining and routing enhance pedagogical outcomes by teaching AI engineers structured, predictable approaches to LLM applications through the workflow-agent spectrum. Prompt chaining teaches linear sequences for ordered subtasks (e.g., generating article, checking consistency, polishing), providing predictability, easy debugging, modularity, and testability—ideal for step-by-step learning. It assumes known sequences, building foundational reliability. Routing (Pattern 5) teaches dynamic decisions for distinct input categories, using LLM classifiers for branching, optimizing specialized prompts over monolithic ones. The article links to prior DIY tutorials: DIY #15 Prompt Chaining with LangChain, DIY #20 Routing LLM Agent with LangChain, enabling hands-on, step-by-step implementation. Other patterns like parallelisation and orchestrator-worker reinforce modularity. Sponsored by TowardsAI's 60-hour Full Stack AI Engineering course (beginner to advanced LLM dev), which teaches building/deploying AI products with prompting, RAG, agents—directly applying these patterns in 92 lessons, code projects, Colab notebooks for certified LLM developers. This hands-on curriculum turns enthusiasts into engineers via practical workflows, enhancing step-by-step learning of reliable LLM apps.

-----

-----

Phase: [EXPLOITATION]

### Source [58]: https://datalearningscience.com/p/design-pattern-prompt-chaining-building

Query: In what ways do modular workflow patterns like chaining and routing enhance pedagogical outcomes when teaching AI engineers to build reliable LLM applications step-by-step?

Answer: Prompt chaining as a modular pattern enhances pedagogical outcomes by teaching AI engineers to build reliable LLM apps via step-by-step workflows, turning single-prompt toys into 95% reliable automations. It breaks complex tasks (e.g., research/write report) into sub-tasks (find sources, extract points, draft, format), increasing quality/reliability. Use cases like summarize-then-translate, extract-then-format teach ordered processes. Pros: simplicity, reliability via focused sub-tasks, specialization. Best practices: validate between steps (Pydantic), summarize long chains, modularize prompts—fostering testable, reusable code. Sample test plan (unit, end-to-end, robustness, performance) teaches systematic debugging/optimization. Anti-patterns (overly long chains, no validation) highlight pitfalls. Cheatsheet variants (summarize-translate, etc.) provide quick learning aids. LLM as Judge evaluates chain quality via rubrics, automating A/B testing. Part of Agentic Design Pattern Series, it builds foundational skills before advanced patterns like Routing, enabling step-by-step mastery of modular workflows for production-grade apps.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://blog.udemy.com/prompt-chaining/

Query: In what ways do modular workflow patterns like chaining and routing enhance pedagogical outcomes when teaching AI engineers to build reliable LLM applications step-by-step?

Answer: Prompt chaining enhances pedagogical outcomes for teaching AI engineers by providing structured, step-by-step workflows mirroring human problem-solving, improving reliability over stepwise prompting (per Cornell study: better accuracy, reduced issues). Udemy courses teach chaining for business use cases with GPT-5/Claude/open-source LLMs, hands-on projects (chatbots, writing assistants, code pipelines). Sequential chaining teaches control for writing/code/form-filling; branching trees (ToT) for decision flows; refinement loops for polishing; parallel for multi-tasking. Use cases: multistep content (research-outline-draft-refine), chatbots (query-classify-response), data transformation, coding (pseudocode-to-debug), teaching/training (define-examples-quiz-feedback), decision support. Design steps: define goal, break down, craft prompts, test links, chain with LangChain/CrewAI, add controls. Improves LLM handling of complex reasoning, scalable workflows for agents (PwC survey: 79% adoption, 66% productivity gains). Enables engineers to build accurate, hallucination-reduced apps step-by-step.

-----

-----

Phase: [EXPLOITATION]

### Source [60]: https://agentic-design.ai/patterns/prompt-chaining

Query: In what ways do modular workflow patterns like chaining and routing enhance pedagogical outcomes when teaching AI engineers to build reliable LLM applications step-by-step?

Answer: Prompt chaining and modular patterns like routing enhance pedagogical outcomes by teaching structured reasoning pipelines for reliable LLM apps, achieving 15.6% better accuracy than monolithic prompts (2024-2025 research). Evolves with LangChain (steps doubled to 7.7, 43% graph workflows), teaching transparency, error isolation, reduced hallucinations, modular design. Applications: content pipelines (research-draft-edit), data workflows (clean-analyze-visualize), decision systems, QA, research, code gen, educational content (curriculum-analysis-generation-assessment). Why matters: better error handling/validation/modularity for complex tasks; improves maintainability/debugging/flexibility. Implementation guide: for multi-phase tasks; best practices (interfaces, error handling, validation, logging); pitfalls (over-complexity, poor context). Part of Agentic Design Patterns catalog (includes Routing, Parallelization), providing systematic, step-by-step learning of techniques for robust AI apps.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What decision theory principles underpin effective LLM-based intent classification for routing?</summary>

Phase: [EXPLORATION]

### Source [61]: https://huggingface.co/blog/perfecXion/intentguard

Query: What decision theory principles underpin effective LLM-based intent classification for routing?

Answer: IntentGuard supports a two-stage routing architecture for organizations deploying multiple domain-specific chatbots. Stage 1: Vertical Router uses a lightweight N-way classifier to route incoming queries to the most appropriate vertical. The classification decision configures downstream LLM permissions: ALLOW grants access to tools like market data, ABSTAIN restricts to document search and asks for clarification, DENY grants no tool access. Decision parameters include tau_allow: 0.80, tau_deny: 0.90, margin_allow: 0.10, margin_deny: 0.10, indicating decision thresholds for classification outcomes. Evaluation metrics include AOC (Abstain-On-Clean): P(predicted=ABSTAIN | gold=ALLOW, category in {positive,clean}) with gate <10%, measuring unnecessary abstentions on clean queries to ensure decisiveness. Ship decision requires all gates to pass, binary outcome. These thresholds and metrics optimize safety, friction, and decisiveness in routing.

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/

Query: What decision theory principles underpin effective LLM-based intent classification for routing?

Answer: Top LLM routing techniques include confidence-based routing: route to stronger models only when cheaper model returns low-confidence responses, relying on uncertainty estimation. Rule-based routing uses heuristics like query length, technical terms, or complexity indicators. Intent-based routing analyzes query complexity, domain, structure: e.g., for 'Write a Python function to calculate Fibonacci numbers recursively', extracts signals (Domain: Programming, Complexity: Medium, Format: Code, Safety: Clear), routes to code-specialized model like GPT-4 Turbo. Other techniques: semantic routing via embeddings, cost-aware routing optimizing cost-quality tradeoff, cascading routing with progressive escalation, load balancing. Preference-based routing trains lightweight classifier on human preference data to predict better model.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://tianpan.co/blog/2026-04-16-intent-classification-agent-routers

Query: What decision theory principles underpin effective LLM-based intent classification for routing?

Answer: Intent classification for agent routers uses cascade pattern: embedding-based for speed first, fine-tuned classifier for specialization on production traffic, LLM-based as catch-all for ambiguous intents despite higher cost/latency. Fine-tuned classifiers improve on user vocabulary, domain edge cases, tool failure modes. Log classifier confidence and tool call outcomes to identify weak intents for review. At scale, predefined taxonomy via classifiers outperforms flexible LLM function calling for ambiguous/multi-step intents.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://docs.nvidia.com/aiq-blueprint/2.0.0/architecture/agents/intent-classifier.html

Query: What decision theory principles underpin effective LLM-based intent classification for routing?

Answer: NVIDIA AI-Q Blueprint's Intent Classifier combines intent (meta or research) and depth (shallow or deep for research) decisions into single LLM invocation, minimizing latency and avoiding extra round-trips. Outputs structured JSON: Intent, Meta response for meta, Depth decision. Reads/writes to ChatResearcherState for internal flow and state model.

-----

-----

Phase: [EXPLORATION]

### Source [65]: https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/

Query: What decision theory principles underpin effective LLM-based intent classification for routing?

Answer: Multi-LLM routing strategies include LLM-assisted routing: classifier LLM at entry point for fine-grained classifications across tasks, complexity, domains, comprehending patterns/context, but adds cost/latency; requires model selection, fine-tuning for balance. Semantic routing via embeddings. Hybrid: semantic for broad categorization, then LLM classifier for fine-grained. Fine-tune with proprietary data for better accuracy in specialized domains.

-----

</details>

<details>
<summary>How do operating system scheduler techniques inform dynamic task allocation in LLM orchestrator patterns?</summary>

Phase: [EXPLORATION]

### Source [66]: https://latitude.so/blog/how-task-scheduling-optimizes-llm-workflows

Query: How do operating system scheduler techniques inform dynamic task allocation in LLM orchestrator patterns?

Answer: Task scheduling acts as a 'traffic controller' for LLM workflows, determining when, where, and how computational tasks are executed across infrastructure. It handles resource allocation and orchestrates workflows to optimize resource use. Core elements include agents (LLMs), planning, memory, and tools for perception, planning, action, and reflection cycles. Learning-to-Rank-Based Scheduling uses machine learning to prioritize tasks dynamically based on resource requirements, historical performance, and system load, unlike fixed rules like FCFS or SJF. In LLM workflows, it accounts for task complexity and context: prioritizing quick tasks like text classification over lengthy summarization during peaks, and larger tasks off-peak. Challenges include LLMs' difficulties with complex planning and multi-step reasoning, resource constraints (high compute, memory limits, real-time needs), and scalability costs in production.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://labelyourdata.com/articles/llm-fine-tuning/llm-orchestration

Query: How do operating system scheduler techniques inform dynamic task allocation in LLM orchestrator patterns?

Answer: LLM orchestration includes task allocation assigning tasks to suitable models based on capabilities and balancing workloads for resource optimization. Resource allocation dynamically allocates based on task complexity: lightweight tasks like text parsing to smaller models, heavier to larger ones. Monitor usage to optimize. Frameworks enable prompt chaining and workflow orchestration (e.g., Apache Airflow, LangChain) for smooth transitions. This informs dynamic allocation patterns by emphasizing model-specific task routing and load balancing akin to scheduler priorities.

-----

-----

Phase: [EXPLORATION]

### Source [69]: https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production

Query: How do operating system scheduler techniques inform dynamic task allocation in LLM orchestrator patterns?

Answer: In multi-agent orchestration, dynamic handoff pattern has agents assess tasks and delegate to specialists based on runtime context without central coordinator. Only one agent active at a time, mirroring dynamic scheduler decisions for task handoff based on suitability.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://www.nature.com/articles/s41598-025-21709-9

Query: How do operating system scheduler techniques inform dynamic task allocation in LLM orchestrator patterns?

Answer: Decentralized adaptive task allocation for multi-agent systems simulates LLM agents (GPT-4, Claude-3.5, etc.) with dynamic success probability and latency updated from outcomes. Controllers predict execution time and waiting window to compute deadlines for task allocation in sparse graphs. Applied to multi-LLM workloads for decentralized orchestration, task routing in knowledge work like document generation.

-----

</details>

<details>
<summary>How are chaining and routing patterns applied to generative AI workflows in film post-production and game development?</summary>

Phase: [EXPLORATION]

### Source [71]: https://www.buildmvpfast.com/blog/prompt-chaining-patterns-production-ai-sequential-parallel-conditional-2026

Query: How are chaining and routing patterns applied to generative AI workflows in film post-production and game development?

Answer: Prompt Chaining Patterns for Production AI include Sequential, Parallel Fan-Out/Fan-In, and Conditional Routing workflows. Sequential chaining organizes tasks one after another, avoiding long prompts that fail often, like extracting data from a PDF, validating it, summarizing, and drafting an email. Parallel chaining runs independent tasks simultaneously to reduce latency, such as analyzing sentiment, extracting product mentions, and classifying issue types in a support ticket, with code for handling failures gracefully using asyncio.gather and filtering exceptions. Conditional routing uses a lightweight classifier prompt to route inputs to specialized prompts, avoiding giant prompts that handle every case inefficiently. This scales costs linearly but is crucial for production, deciding which specialized workflow handles the work based on input classification.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://huyenchip.com/2024/07/25/genai-platform.html

Query: How are chaining and routing patterns applied to generative AI workflows in film post-production and game development?

Answer: In building a Generative AI Platform, orchestration involves components definition and chaining (pipelining). Chaining sequences steps from user query to task completion, like function composition in pipelines. Orchestrators combine models (including for generation, routing, scoring), databases, and actions. Model routers support complex pipelines. Enhancements include guardrails, caching for latency/costs, complex logic, and actions. Observability traces queries step-by-step for monitoring and debugging. AI pipeline orchestration chains multiple models, data retrievals, and tools into end-to-end flows, applicable to complex workflows.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://www.linkedin.com/posts/aurimas-griciunas_you-must-know-these-%F0%9D%97%94%F0%9D%97%B4%F0%9D%97%B2%F0%9D%97%BB%F0%9D%98%81%F0%9D%97%B6%F0%9D%97%B0-%F0%9D%97%A6%F0%9D%98%86%F0%9D%98%80-activity-7372231823138918400-pUE3

Query: How are chaining and routing patterns applied to generative AI workflows in film post-production and game development?

Answer: Agentic System Workflow Patterns include Prompt Chaining, where each LLM call passes output to the next. Routing classifies input into paths, routing to appropriate specialized workflow, useful for complex topologies like agentic chatbots deciding between RAG or actions. Parallelization splits input into multiple queries processed in parallel, aggregating answers for speed and accuracy. Chaining combines with routing, parallelization replacing LLM nodes. These patterns simplify enterprise AI, ensuring efficiency and scalability.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="a-beginner-s-guide-to-llm-intent-classification-for-chatbots.md">
<details>
<summary>A Beginner's Guide to LLM Intent Classification for Chatbots</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot>

# A Beginner's Guide to LLM Intent Classification for Chatbots

Creating an AI chatbot involves more than just using a model API and adding context with your data.

You should also consider the various intents users might have and how to manage them.

In this blog post, we'll outline the steps to set up and evaluate intent detection in your chatbot workflow.

What Is Intent Detection?

Intent detection is a task that identifies a user's intention or desired outcome from their query. This task is essential for AI chatbots to provide accurate and relevant responses.

A very standard intent detection workflow uses a pre-trained LLM model, a prompt with instructions and context, and a handler logic for each of the intents.

Why do you need it?

Let’s look at a real example to illustrate the need for this step in a chatbot workflow.

Imagine that you’re building a customer service chatbot for an e-commerce business. Your visitors can ask the chatbot any question. Before the chatbot responds or takes any action, it needs to accurately understand the visitor's intent.

To keep this example simple, lets say that you have defined 5 intent categories: "Order Status", "Product Information", "Payments", "Returns" and "Feedback”.

For each category, there should be a distinct step where the LLM powered chatbot, figures out the user's intent. It does this by placing the user's question into the right category. After identifying the intent, the chatbot can then take the next appropriate actions for that particular category.

Having separate steps for the prompts and intent handlers is useful because each of your intents might need to do different actions. For example: “Returns” might need to be handled by an external service/API that a handler action should call, and the handler for “Product information” might just call an LLM and a context doc to answer with text response. Also, adding too many instructions in one prompt can also influence the performance.

Identifying these intents accurately allows the chatbot to respond better, call an external API or route the query to the correct personnel for further assistance.

In the next section we show you how to implement it.

How can you build intent detection for your chatbot?

To build a reliable intent detection for your chatbot you need to cover 4 critical steps:

Defining intents Setting up the intent detection prompt Setting up handler logic prompts Testing and evaluating prompts/models

We give more details on these in the following sections.

Define intents

Identify the main reasons users interact with your chatbot, like asking for help or making a purchase.

Group these reasons into categories, or 'intents', using insights from customer interactions and FAQs.

Write the intent detection prompt

After you have your intents, you should start drafting the system prompt that will be used to classify the user’s query. Make sure to give clear directions, and follow best prompt engineering practices. Here’s a simple example for the system prompt:

🤖 System Prompt: You’re a LLM that detects intent from user queries. Your task is to classify the user's intent based on their query. Below are the possible intents with brief descriptions. Use these to accurately determine the user's goal, and output only the intent topic. - Order Status: Inquiries about the current status of an order, including delivery tracking and estimated arrival times. - Product Information: Questions regarding product details, specifications, availability, or compatibility. - Payments: Queries related to making payments, payment methods, billing issues, or transaction problems. - Returns: Requests or questions about returning a product, including return policies and procedures. - Feedback: User comments, reviews, or general feedback about products, services, or experiences. - Other: Choose this if the query doesn’t fall into any of the other intents. 💬 User Query: I would like to check my last order. 🤖 Response: Order status.

- For more reliable outputs you can also consider using function calling with your models, so that you always get a structured response from the model, one that can be used to run specific functions in your code. Learn how to set it up here .

## Don’t forget to add a fallback option!

Did you notice that we added a fallback intent “Other” in the system prompt?

Adding fallback prompts is essential for handling situations where the chatbot fails to understand or correctly classify a user's intent.

Fallback prompts act as a safety net to keep users engaged, even when their query isn't a clear match. They can involve clarifying questions, rephrasing the query, or offering human assistance.

Set up handler logic

For each intent, you need to develop a response mechanism, and decide if the chatbot should perform an action like calling an API to another tool/service, or to just provide a text response.

To implement the handler logic you’ll need to build a more complex LLM chain , and use other prompts to provide text responses or to call an API to perform a specific action with external tools and services.

Test and evaluate prompts accross test cases

Testing and evaluating prompts across test cases is crucial for building reliable chatbots.

Before you push it to production, you need to be sure that your intent classifiers and handlers are working properly. You should test every intent path with various user queries and evaluate the performance of different prompt and model combinations.

For example, we recently did an experiment where we used four models and few-shot prompts to classify if a customer support ticket has been resolved or not. We had around 200 test cases, and used Vellum to evaluate our configuration at scale. Below you can see how that looked like in the product.

https://cdn.sanity.io/images/ghjnhoi4/production/43f8331e520a60c88b2b6f6dfe9e1e774991a298-1462x887.png

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="asynchronous-or-concurrency-patterns-in-python-with-asyncio-.md">
<details>
<summary>Asynchronous or Concurrency Patterns in Python with Asyncio</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://santhalakshminarayana.github.io/blog/concurrency-patterns-python>

https://santhalakshminarayana.github.io/images/concurrency-patterns-python/concurrency-patterns-python.jpg

###### Published on: **Mar 6, 2024**

# Asynchronous or Concurrency Patterns in Python with Asyncio

Most software development tasks require an asynchronous way of handling things like running background tasks, processing multiple tasks at a time, applying the same operations on huge data, distributing tasks to free workers, etc. In this blog, we will see how can we achieve some of these patterns with Python.

Before delving into the concept, the most important thing we need to understand is _concurrency vs parallelism_. Concurrency is about handling multiple tasks at a time and this handling might be in parallel or not. Whereas parallelism is about doing multiple tasks parallelly/simultaneously at a time. Parallelism can be termed as concurrency but not vice-versa.

In my earlier blog posts about [Super Fast Python: Multiprocessing](https://santhalakshminarayana.github.io/blog/super-fast-python-multi-processing), I have described how can achieve parallelism with Python.

One can ask, in parallelism, if we can do multiple things at a time, why do we need to focus on concurrency at all? The answer to this question simply depends on the program language in the discussion. Some program languages like C/C++ are built to directly use multiple cores/vCPUs of the host machine for parallelism, while other languages like Golang can still utilize multiple cores but with concurrency, not parallel. Both of these types of languages can do both concurrency and parallelism very smoothly. But we have a special child like Python, whose creators put so many restrictions (which are thoughtful at creation) to be a better resource utiliser. GIL in Python makes the Python interpreter run only one thread at a time and cannot multiplex the multiple threads to multiple cores. I have already discussed this in my previous post about [Why Python is Slow](https://santhalakshminarayana.github.io/blog/super-fast-python-why-python-slow).

To utilize multiple cores, we have to create at least one process per core. The creation and memory management of the process is time-consuming and comes with its overheads. So, a general rule of thumb is to use multi-programming for CPU-intensive tasks, and I/O bound tasks like network calls, and reading from disk are handled concurrently with threads. As we can use multi-threading in Python, creating and managing a huge number of threads is not optimal in Python or any high-level language. The solution to create and manage huge numbers of thread-like objects say in thousands or 100s of thousands, we can use Co-routines which can be termed as virtual threads or small threads whose memory footprint is very minimal compared to threads. And we can spawn thousands of these in a few microseconds.

Coroutines are part of core Python and are handled with an in-built package called [asyncio](https://docs.python.org/3/library/asyncio.html)

The goal of this article is to demonstrate some concurrency patterns rather than learning about coroutines. So, it's expected to have some basic background with _asyncio_.

In the following sections, we cover the two most used concurrency patterns:

- Background tasks with Ticker
- WorkerPool pattern
- Pipeline or Chain processing

## Ticker & Background tasks

Let's say we have a stream of data coming and stored in some data sources like Database, Redis, or in the Cloud. And we want to analyze that data periodically let's say every 1 day and send an email notification to the customers with the analyzed report. This is a basic CRON job that we execute in Linux.

If you don't know what the is ticker, it is a kind of background task where the program will be notified for every time interval that we need to do some task. Tickers are all over any periodic notification or job updates.

We will use a ticker for our coroutine to come into the foreground and call a callback that it receives with callback arguments. Let's look at the following ticker class

```python
ticker.py

1from threading import Event, Thread
2from typing import Any, Callable, Optional
3
4class Ticker(Thread):
5    def __init__(
6        self,
7        is_daemon: bool,
8        tick_period: int,
9        callback: Callable,
10        **cbkwargs: Optional[Any]
11    ):
12        Thread.__init__(self)
13        self.daemon = is_daemon
14        self.tick_period = tick_period
15        self.task_kill_event = Event()
16        self.callback = callback
17        self.cbkwargs = cbkwargs
18
19    def kill(self):
20        self.task_kill_event.set()
21
22    def run(self):
23        while True:
24            is_killed = self.task_kill_event.wait(self.tick_period)
25            if is_killed:
26                print("Exiting ticker.")
27                break
28
29            # call the callback
30            try:
31                self.callback(**self.cbkwargs)
32            except Exception as e:
33                print(f"Exception for callback: {e}")
34
```

This class inherits the _Thread_ class to implement custom thread functionality. In the constructor, we pass the _is\_daemon_ flag that makes the current thread run as a daemon or not. Usually for background tasks that do not stick to the application lifecycle, they are not meant to be daemon. And other params like _tick\_period_ which says the time interval for the ticker, _callback_ is a callback function, and _cbkwargs_ are callback key arguments to pass to this callback function. We will speak about _self.task\_kill\_event = Event()_ later.

This class has two methods _kill_ and _run_ where _run_ is an overridden _Thread_ class function.

[_threading.Event()_](https://docs.python.org/3/library/threading.html#event-objects) object is used for communication between threads. It's simply a boolean flag that one thread signals the other thread that listens to this event object states. We use an event object to signal for the background task to exit. This is what the _kill_ function is. If we call this function, it will set the event to be **True** signaling the listing thread.

The overriding _run_ method is a classic implementation of a background running thread, it will run in a loop until it receives the _is\_killed_ to be **True** which we set by calling _kill_. _self.task\_kill\_event.wait(self.tick\_period)_ is where the magic happens. Here we will wait for the specified ticker period for that event to be set. After the specified interval period, if we don't receive the event signal, the **is\_killed** will be False, and we will call the callback with the keyword arguments.

Why don't we use a simple _thread.sleep_ for sleeping in the background? Let's say, that while waiting for a ticker period, we get the event signal, then we have to right away exit the thread. For example, if the ticker period is for 10 seconds, and while in the 6th second, we get the signal, we will exit there instead of waiting for the other 4 seconds. This can't be achieved with thread sleep. This is very useful if we are running larger ticker periods let's for days or weeks.

Let's look at how we can run this ticker thread for every time inteval.

```python
ticker_example.py

1import asyncio
2from ticker import Ticker
3
4process_called = 0
5def process(task_for=""):
6    global process_called
7    process_called += 1
8    print("process called for: ", process_called, " times")
9
10async def stop_ticker(kill_func: Callable, after_time: int):
11    await asyncio.sleep(after_time)
12    kill_func()
13    # call any cleanup functions for graceful exiting
14    await asyncio.sleep(1)
15
16if __name__=="__main__":
17    cbkargs = {"task_for": "data-pre-process"}
18    ticker = Ticker(True, 3, process, **cbkargs)
19    ticker.start()
20
21    ev_loop = asyncio.get_event_loop()
22    ev_loop.run_until_complete(stop_ticker(ticker.kill, 7))
23
```

```shell
Output

1process called for:  1  times
2process called for:  2  times
3Exiting ticker.
4
```

In the above example, we have imported the _Ticker_ class and defined a function _process_ which we pass as a callback to this ticker. This function will be called for after every ticker period and this is where we do any periodic processing like sending notifications.

The line _ticker = Ticker(True, 3, process, \*\*cbkargs)_ initializes the ticker with **3** second time interval. We have defined another function _stop\_ticker_ which we will use to kill the ticker after some time. The stop ticker function will wait for some time (7 seconds here) and kill the ticker.

As we can see in the output, the ticker called the callback every 3 seconds and got stopped by the parent thread which is our main thread here through _stop\_ticker_ function.

This is a very effective way of defining a ticker in Python with a simple thread mechanism. Now we will see how we can define a worker pool for processing multiple jobs by multiple workers concurrently.

## Worker pool/Job queue pattern

We can define worker pool concurrency patterns with threads alone using multi-threading. But there are limitations with threads, like:

- Threads are synchronous, meaning when a thread is paused it blocks the execution also, leaving other threads for starvation
- we cannot create a huge number of threads due to various reasons like memory, context switching, etc.

So, we can use a coroutine to do this job because we can have an asynchronous way of doing things if have to call any API or wait to load the huge dataset, we can pause the current coroutine and let others claim the CPU. As Python is single-threaded, meaning only 1 thread can run at a time, this un-blocking way of organizing your tasks makes your Python code efficient and performant. And we can create thousands of coroutines in quick time and they occupy very little memory.

The worker pool pattern is a simple and the most widely used concurrency pattern for distributing multiple tasks or jobs (n-jobs) to multiple workers (m-workers). Usually _n >= m_. In this pattern, we have a list of jobs to be processed, and they are to be read from a static queue or a dynamic stream. And we have to distribute those jobs to idle workers who take the job and process it. Worker may or may not return the result based on the type of the Job. Idle workers are very hungry and they compete with other idle workers to take the incoming Job or un-attended Job.

https://santhalakshminarayana.github.io/images/concurrency-patterns-python/job-queue-worker-pool.jpgWorker pool with Job Queue. Each idle worker takes one job at a time and processes the Job. After the job is complete, the worker will continue to take any un-attended Job.

As in the above image, the jobs are stored in some data structure say a Job Queue, and we have a pool of workers. We usually incorporate a scheduler/distributor to assign the Jobs to idle Workers. So, at a time, if we have **m** workers, then we can process **m** Jobs concurrently. If we can access multiple cores, then these Jobs are processed parallelly like in Golang. Because Python has some overhead for forking multiple processes, we will stick to single-threaded concurrent execution of Jobs by multiple Workers. The following code implements this worker pool pattern where we have to process the n-number of Jobs.

```python
worker_pool.py

1import asyncio
2from asyncio.queues import Queue
3from threading import Thread
4from typing import Any, Callable, List
5
6
7class WorkerPool(Thread):
8    def __init__(
9        self,
10        is_daemon: bool,
11        jobs: List[Any],
12        n_workers: int,
13        callback: Callable[[List[Any]], None],
14    ):
15        Thread.__init__(self)
16        self.daemon = is_daemon
17        self.jobs = jobs
18
19        self.event_loop = asyncio.new_event_loop()
20        asyncio.set_event_loop(self.event_loop)
21
22        self.job_queue = Queue()
23        self.n_workers = n_workers
24        self.callback = callback
25
26    async def distribute(self, w_name: str):
27        while self.job_queue.qsize() > 0:
28            job = await self.job_queue.get()
29            try:
30                # call the callback with the Job details
31                await self.callback(job)
32            except Exception as e:
33                raise Exception(f"Exception for callback: {e}")
34            finally:
35                # mark the current job as done
36                # will get an exception if it's already done by the current worker or any other worker
37                try:
38                    self.job_queue.task_done()
39                except ValueError:
40                    print(f"{w_name}: Task already done.")
41                    return
42
43    async def job_wp(self):
44        # add jobs to the job-queue.
45        # this job queue can be concurrently accessed by multiple workers
46        for i in range(len(self.jobs)):
47            await self.job_queue.put(self.jobs[i])
48
49        tasks = []
50
51        # create multiple workers that take un-attended jobs from the job queue
52        # and continuously process them until all jobs are executed
53        for i in range(self.n_workers):
54            tasks.append(self.distribute(f"Worker: {i+1}"))
55
56        await asyncio.gather(*tasks)
57
57    def run(self):
58        try:
59            self.event_loop.run_until_complete(self.job_wp())
60        except Exception as e:
61            print(f"Error distributing jobs: {e}")
62        finally:
63            self.event_loop.close()
64
```

Here, we extend the _Thread_ class to execute WorkerPool in a separate thread. The constructor takes the list of job items, _n\_workers_ for how many workers to spawn, and a callback function to call with the job detail.

_WorkerPool_ class defines two methods _job\_wp_ and _distribute_. _job\_wp_ creates a JobQueue with all jobs and also creates multiple workers each with a name **Worker: i** where _i_ is ith worker. This function will wait for all workers to complete processing all Jobs.

_distribute_ function takes the unattended job and calls the callback with job details as parameters to the callback function. We can also extend this to pass arguments. After executing the job, we finally mark that job as done.

Example of processing Jobs by multiple workers:

```python
worker_pool_example.py

1from random import randint
2from time import time
3from worker_pool import WorkerPool
4
5async def process_job(job_detail: Any):
6    time_to = randint(1, 4)
7    print("Processing job:", job_detail, "will take:", time_to, "seconds")
8    await asyncio.sleep(time_to)
9    print("Completed job:", job_detail)
10
11if __name__=="__main__":
12    wp = WorkerPool(True, list(range(1, 11)), 3, process_job)
13    atime = time()
14    wp.start()
15    wp.join()
16    print("time taken:", str(int(time()-atime)) + "s")
17
```

```shell
Output

1Processing job: 1 will take: 3 seconds
2Processing job: 2 will take: 1 seconds
3Processing job: 3 will take: 1 seconds
4Completed job: 2
5Processing job: 4 will take: 4 seconds
6Completed job: 3
7Processing job: 5 will take: 4 seconds
8Completed job: 1
9Processing job: 6 will take: 3 seconds
10Completed job: 4
11Processing job: 7 will take: 1 seconds
12Completed job: 5
13Processing job: 8 will take: 1 seconds
14Completed job: 6
15Processing job: 9 will take: 2 seconds
16Completed job: 7
17Processing job: 10 will take: 1 seconds
18Completed job: 8
19Completed job: 10
20Completed job: 9
21time taken: 8s
22
```

With this asynchronous processing of Jobs, we have processed all the jobs whose collective processing time requires **21 seconds** in **8 seconds** thanks to asyncio whereas with un-optimized multi-threading, it might take the same **21 seconds** due to threads blocking nature.

## Pipeline or Chain processing

Pipeline pattern or Chain processing is a simple concurrency pattern of executing the multiple jobs consecutively where the input for the current job is the output of the previous job. For example, let's say we have to analyze incoming data about customer ratings (scale: 1-5) for our service. And we have to do the following steps:

- Analyse the feedback
- If the rating is below 3, we have to store this rating for later analyses
- Later generate the thank you message for the customer
- Finally, based on the preference notification channel (Email or SMS) we will send a thank you message.

This whole process needs a couple of logical decisions to take at each level of processing. Based on multi-logic flow, we can divide the above process into small functions and we execute each function sequentially based on where the next function call is decided based on the current input data.

https://santhalakshminarayana.github.io/images/concurrency-patterns-python/pipeline-or-chain-concurrency-processing.jpgProcessing pipeline/flow

If we have multiple customer ratings to be analyzed we can combine the **WorkerPool** pattern with this Pipeline pattern.

```python
pipeline.py

1import asyncio
2import random
3from worker_pool import WorkerPool
4
5commuincation_type = ["email", "sms"]
6
7async def process_rating(job: list):
8    rating, user, idx = job
9    print(f"1. processing rating, for item: {idx}, rating: {rating} by user: {user}")
10    # some processing
11    await asyncio.sleep(1)
12    if rating <= 2:
13        await store_for_analyses(rating, idx)
14    else:
14        await form_thankyou_message(user, idx)
15
16async def store_for_analyses(rating: int, idx: int):
17    print(f"1a. storing for analyses, for item: {idx}")
18    # store in some datastore
19    await asyncio.sleep(1)
20
21async def form_thankyou_message(user: str, idx: int):
22    print(f"2. forming thank-you message, for item: {idx}")
23    # a DB call to fetch the user details
24    await asyncio.sleep(1)
25
26    # communication medium may be {email, sms}
27    cs = random.choices(commuincation_type, weights=[0.5, 0.5], k=1)[0]
28
29    match cs:
30        case "email":
31            await send_email_message(user, idx)
32        case "sms":
33            await send_sms_message(user, idx)
34        case _:
35            return
36
37async def send_email_message(user: str, idx: int):
38    print(f"2a. sending email message, for item: {idx}, for user: {user}")
39    # sendinig might take time
40    await asyncio.sleep(1)
41
42async def send_sms_message(user: str, idx: int):
43    print(f"2b. sending sms message, for item: {idx}, for user: {user}")
44    # sendinig might take time
45    await asyncio.sleep(1)
46
47
48if __name__=="__main__":
49    # create ratings, users, and items
50    n = 10
51    ratings = random.choices([1, 2, 3, 4, 5], weights=[0.25, 0.25, 0.15, 0.15, 0.2], k=n)
52    items = list(range(1, n+1))
53    users = list(map(lambda x: f"User {x}", items))
54
55    jobs = []
56    for i in range(n):
57        jobs.append([ratings[i], users[i], items[i]])
58
59    wp = WorkerPool(True, jobs, 3, process_rating)
60    wp.start()
61    wp.join()
62
```

Here we define a list of functions that are depicted in the image above. Each function will take input from the previous function and apply its decision logic to call which function next.

In the example, we have created 10 rating items to be processed by 3 workers. The output of the processing is

```
Output

11. processing rating, for item: 1, rating: 4 by user: User 1
21. processing rating, for item: 2, rating: 3 by user: User 2
31. processing rating, for item: 3, rating: 3 by user: User 3
42. forming thank-you message, for item: 1
52. forming thank-you message, for item: 2
62. forming thank-you message, for item: 3
72b. sending sms message, for item: 1, for user: User 1
82a. sending email message, for item: 2, for user: User 2
92a. sending email message, for item: 3, for user: User 3
101. processing rating, for item: 4, rating: 2 by user: User 4
111. processing rating, for item: 5, rating: 5 by user: User 5
121. processing rating, for item: 6, rating: 4 by user: User 6
131a. storing for analyses, for item: 4
142. forming thank-you message, for item: 5
152. forming thank-you message, for item: 6
161. processing rating, for item: 7, rating: 5 by user: User 7
172a. sending email message, for item: 5, for user: User 5
182b. sending sms message, for item: 6, for user: User 6
192. forming thank-you message, for item: 7
201. processing rating, for item: 8, rating: 5 by user: User 8
211. processing rating, for item: 9, rating: 1 by user: User 9
222b. sending sms message, for item: 7, for user: User 7
232. forming thank-you message, for item: 8
241a. storing for analyses, for item: 9
251. processing rating, for item: 10, rating: 5 by user: User 10
262b. sending sms message, for item: 8, for user: User 8
272. forming thank-you message, for item: 10
282b. sending sms message, for item: 10, for user: User 10
29
```

## Custom coroutine

If you want an asynchronous function in a separate thread with the async capabilities, we can run a coroutine as follows

```python
coroutine.py

1import asyncio
2from threading import Thread
3from typing import Any, Callable, List, Optional
4
5class CustomCoroutine(Thread):
6    def __init__(
7        self,
8        is_daemon: bool,
9        callback: Callable[[List[Any]], None],
10        **cbkwargs: Optional[Any]
11    ):
12        Thread.__init__(self)
13        self.daemon = is_daemon
14        self.event_loop = asyncio.new_event_loop()
15        asyncio.set_event_loop(self.event_loop)
16        self.callback = callback
17        self.cbkwargs = cbkwargs
18
19    async def callback(self) -> None:
20        try:
21            await self.callback(**self.cbkwargs)
22        except Exception as e:
23            print(f"Error calling callback: {e}")
24
25    def run(self) -> None:
26        try:
27            self.event_loop.run_until_complete(self.callback())
28        finally:
29            self.event_loop.close()
30
```

I hope the above concurrency patterns give you some understanding of organizing your Python code for better performance and optimization. Other concurrency patterns that are worth noting are:

- **Monitor pattern**: **n** number of threads waiting on some condition to be true, if the condition is not true, those threads need to be in a sleep state and pushed to the wait queue, and they have to be notified when the condition becomes true.
- **Double Checked locking**: for creating concurrent objects. (Ex: Singleton design pattern)
- **Barrier pattern**: All concurrently executing threads must wait for others to complete and wait at a point called barrier.
- **Reactor pattern**: In an event-driven system, a service handler accepts events from multiple incoming requests and demultiplexes to respective non-blocking handlers.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="comparative-analysis-of-prompt-strategies-for-large-language.md">
<details>
<summary>Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.mdpi.com/2079-9292/13/23/4712>

All articles published by MDPI are made immediately available worldwide under an open access license. No special
permission is required to reuse all or part of the article published by MDPI, including figures and tables. For
articles published under an open access Creative Common CC BY license, any part of the article may be reused without
permission provided that the original article is clearly cited. For more information, please refer to
[https://www.mdpi.com/openaccess](https://www.mdpi.com/openaccess).

Feature papers represent the most advanced research with significant potential for high impact in the field. A Feature
Paper should be a substantial original Article that involves several techniques or approaches, provides an outlook for
future research directions and describes possible research applications.

Feature papers are submitted upon individual invitation or recommendation by the scientific editors and must receive
positive feedback from the reviewers.

Editor’s Choice articles are based on recommendations by the scientific editors of MDPI journals from around the world.
Editors select a small number of articles recently published in the journal that they believe will be particularly
interesting to readers, or important in the respective research area. The aim is to provide a snapshot of some of the
most exciting work published in the various research areas of the journal.

Original Submission Date Received: .

Open AccessArticle

# Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts

by

Manuel Gozzi

https://www.mdpi.com/profiles/3550856/thumb/Manuel_Gozzi.jpegManuel Gozzi

[SciProfiles](https://sciprofiles.com/profile/3550856?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Manuel%20Gozzi) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Manuel+Gozzi%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Manuel+Gozzi)

\*,† https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1776414554 and

Federico Di Maio

https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.pngFederico Di Maio

[SciProfiles](https://sciprofiles.com/profile/4787652?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Federico%20Di%20Maio) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Federico+Di+Maio%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Federico%20Di%20Maio)

† https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1776414554

Department of Engineering Sciences, Guglielmo Marconi University, 00193 Roma, Italy

\*

Author to whom correspondence should be addressed.

†

These authors contributed equally to this work.

_Electronics_ **2024**, _13_(23), 4712; [https://doi.org/10.3390/electronics13234712](https://www.mdpi.com/2079-9292/13/23/4712)

Submission received: 25 October 2024
/
Revised: 22 November 2024
/
Accepted: 27 November 2024
/
Published: 28 November 2024

(This article belongs to the Special Issue [Advances in Software Engineering and Programming Languages](https://www.mdpi.com/journal/electronics/special_issues/K17V2BP8P4))

## Article Menu

- [Academic Editors](https://www.mdpi.com/2079-9292/13/23/4712#academic_editors)

[https://www.mdpi.com/profiles/2677889/thumb/Hsi-Min_Chen.pngHsi-Min Chen](https://sciprofiles.com/profile/2677889?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name)

[https://www.mdpi.com/profiles/1218915/thumb/Shang-Pin_Ma.pngShang-Pin Ma](https://sciprofiles.com/profile/1218915?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name)

- [Recommended Articles](https://www.mdpi.com/2079-9292/13/23/4712#)
- [Related Info Link](https://www.mdpi.com/2079-9292/13/23/4712#related)

  - [Google Scholar](http://scholar.google.com/scholar?q=Comparative%20Analysis%20of%20Prompt%20Strategies%20for%20Large%20Language%20Models%3A%20Single-Task%20vs.%20Multitask%20Prompts)

- [More by Authors Links](https://www.mdpi.com/2079-9292/13/23/4712#authors)

  - on DOAJ

    - [Gozzi, M.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Manuel%20Gozzi%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Di Maio, F.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Federico%20Di%20Maio%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)

  - on Google Scholar

    - [Gozzi, M.](http://scholar.google.com/scholar?q=Manuel%20Gozzi)
    - [Di Maio, F.](http://scholar.google.com/scholar?q=Federico%20Di%20Maio)

  - on PubMed

    - [Gozzi, M.](http://www.pubmed.gov/?cmd=Search&term=Manuel%20Gozzi)
    - [Di Maio, F.](http://www.pubmed.gov/?cmd=Search&term=Federico%20Di%20Maio)

[Article Views](https://www.mdpi.com/2079-9292/13/23/4712#metrics)

[Citations-](https://www.mdpi.com/2079-9292/13/23/4712#metrics)

- [Table of Contents](https://www.mdpi.com/2079-9292/13/23/4712#table_of_contents)

Altmetric[_share_ Share](https://www.mdpi.com/2079-9292/13/23/4712# "Share") [_announcement_ Help](https://www.mdpi.com/2079-9292/13/23/4712# "Help")_format\_quote_ Cite [_question\_answer_ Discuss in SciProfiles](https://sciprofiles.com/discussion-groups/public/10.3390/electronics13234712?utm_source=mpdi.com&utm_medium=publication&utm_campaign=discuss_in_sciprofiles "Discuss in Sciprofiles")

## Abstract

This study investigates the effectiveness of prompt engineering strategies for Large Language Models (LLMs), comparing single-task and multitasking prompts. Specifically, we analyze whether a single prompt handling multiple tasks—such as named entity recognition (NER), sentiment analysis, and JSON output formatting—can achieve performance comparable to dedicated single-task prompts. To substantiate our findings, we employ statistical analyses, including paired Wilcoxon tests, McNemar tests, and Friedman tests, to validate claims of performance similarity or superiority. Experiments were conducted using five open-weight LLMs: LLama3.1 8B, Qwen2 7B, Mistral 7B, Phi3 Medium, and Gemma2 9B. The results indicate that there is no definitive rule favoring single-task prompts over multitask prompts; rather, their relative performance is highly contingent on the specific model’s data and architecture. This study highlights the nuanced interplay between prompt strategies and LLM characteristics, offering insights into optimizing their use for specific NLP tasks. Limitations and future directions, such as expanding task types, are also discussed.

Keywords:

[prompt engineering](https://www.mdpi.com/search?q=prompt+engineering); [artificial intelligence](https://www.mdpi.com/search?q=artificial+intelligence); [large language model](https://www.mdpi.com/search?q=large+language+model)

## 1\. Introduction

Large Language Models represent one of the most significant innovations in the field of artificial intelligence in recent years. These models are based on transformer neural architectures, characterized by self-attention mechanisms that allow for the processing of input sequences while maintaining contextual relationships between various elements. Their operation is based on a training process on enormous textual datasets, during which the model learns to predict the next token in a sequence, optimizing billions of parameters through the backpropagation process. The transformer architecture, introduced in the paper “Attention Is All You Need” \[ [1](https://www.mdpi.com/2079-9292/13/23/4712#B1-electronics-13-04712)\], distinguishes itself through its ability to process input in parallel, overcoming the limitations of traditional recurrent neural networks (RNNs). The attention mechanism allows the model to weigh differently the importance of various parts of the input, creating dynamic contextual representations. This is made possible through three main components: the query, key, and value matrices, which together allow the model to establish complex correlations between different elements of the input. Large Language Models operate through a tokenization process that converts text into numerical sequences, using vocabularies that can contain tens or hundreds of thousands of tokens. Each token is then embedded in a high-dimensional vector space, where semantic and syntactic relationships are captured through vector distances. This distributed representation allows the model to capture complex linguistic nuances and generalize to cases never seen during training. A distinctive characteristic of modern Large Language Models is their few-shot and zero-shot \[ [2](https://www.mdpi.com/2079-9292/13/23/4712#B2-electronics-13-04712)\] learning capability, meaning they can adapt to new tasks without the need for further training, simply through examples or textual instructions (prompts). This is made possible by their deep architecture and broad exposure to various contexts during training, allowing them to develop a sort of generalized language “understanding”.

Large Language Models are increasingly integrated into everyday life, making it crucial to understand and learn the correct interaction methods to effectively interface with these tools. The countless parameters that define Large Language Models are sufficient to emulate natural conversations. Mastering best practices in prompting is essential, as even minor variations in a prompt can significantly affect the outcome. In light of this, we have undertaken a research study aimed at quantifying the performance of multitask prompts in comparison to single-task prompts. Our initial hypothesis posits that single-task prompts, due to their inherently lower complexity, should yield better results than their multitask counterparts. While this assumption may seem intuitive, quantifying these differences and conducting a comparative analysis across various models is essential for understanding the performance degradation in prompting. Furthermore, despite the intuition that simpler, single-task prompts should produce better results, empirical data suggest that this is not universally true for all Large Language Models. Indeed, while certain models support our initial hypothesis, others exhibit superior performance with multitask prompts. This observation highlights the necessity for a thorough analysis to understand the underlying dynamics of each model. The differences, particularly those seen in models such as LLama 3.1 and Mistral, demonstrate that the interaction between a prompt and a model cannot be reduced to a simple general rule. This makes our study critical for optimizing the use of Large Language Models in various pipelines.

The objective of this study is to systematically and quantitatively analyze the performance differences between single-task and multitask prompts across a variety of large-scale language models. The goal is to provide empirical data that can guide developers and users in selecting the most effective prompting strategy for each model and use case. Our methodology includes defining a series of standardized tasks, which will be presented to various Large Language Models in both single-task and multitask formats. Performance will be measured using a composite metric that combines the results of three metrics applied to specific natural language processing tasks: F1 score for named entity recognition, exact match for sentiment analysis, and Bilingual Evaluation Understudy (BLEU) for review coherence. The findings from this research could have significant practical implications. Firstly, they provide data-driven guidelines to optimize interaction with Large Language Models in various application contexts. Additionally, any discrepancies observed among the models may offer valuable insights into the architectural and training differences that influence how Large Language Models respond to prompt complexity. One of the most well-known challenges of Large Language Models is the interpretability of their output. This study highlights this issue by revealing “non-standard” results when using what would be considered a standard approach.

## 2\. Related Work

Recent research has explored various prompt engineering techniques for enhancing Large Language Models’ (Large Language Models) performance in natural language processing (NLP) tasks. Studies have investigated different types of prompts, including discrete, continuous, few-shot, and zero-shot approaches \[ [3](https://www.mdpi.com/2079-9292/13/23/4712#B3-electronics-13-04712)\]. Discrete prompts are formulated using natural language, making them interpretable and easier to design, whereas continuous prompts leverage embeddings that are optimized through gradient-based methods, offering more flexibility but requiring specialized tuning techniques. Few-shot and zero-shot prompting techniques allow Large Language Models to perform tasks with minimal or no task-specific training examples, significantly reducing the need for extensive labeled data \[ [3](https://www.mdpi.com/2079-9292/13/23/4712#B3-electronics-13-04712)\]. These strategies have shown promise in various contexts, highlighting the adaptability of Large Language Models to new tasks with limited supervision.

Researchers have also developed a catalog of prompt patterns to solve common problems when interacting with Large Language Models \[ [4](https://www.mdpi.com/2079-9292/13/23/4712#B4-electronics-13-04712)\]. These patterns, which include guidelines for crafting effective prompts, address issues such as prompt ambiguity, model misinterpretations, and response consistency \[ [4](https://www.mdpi.com/2079-9292/13/23/4712#B4-electronics-13-04712)\]. They provide a taxonomy of prompt patterns that categorize different approaches based on task types, such as classification, generation, and summarization, thus offering a structured framework for prompt design that can be easily applied across different NLP tasks. The effectiveness of different prompting strategies, such as simple prefix, cloze, chain-of-thought, and anticipatory prompts, has been empirically evaluated for clinical NLP tasks \[ [5](https://www.mdpi.com/2079-9292/13/23/4712#B5-electronics-13-04712)\]. For instance, the chain-of-thought prompting technique encourages Large Language Models to break down complex tasks into intermediate reasoning steps, improving performance on tasks that require logical progression and detailed explanation. Anticipatory prompts, on the other hand, guide models to predict subsequent responses by leveraging prior knowledge of likely outcomes, enhancing the coherence and relevance of generated text, particularly in domains requiring domain-specific reasoning like clinical NLP \[ [5](https://www.mdpi.com/2079-9292/13/23/4712#B5-electronics-13-04712)\].

Additionally, novel prompting techniques like heuristic and ensemble prompting have been introduced \[ [5](https://www.mdpi.com/2079-9292/13/23/4712#B5-electronics-13-04712)\]. Heuristic prompting involves using domain-specific rules or prior knowledge to construct prompts that better align with the task at hand, while ensemble prompting combines multiple prompts to aggregate the strengths of different strategies, enhancing overall model performance and reducing variability in responses. These approaches provide robust alternatives to traditional single-prompt methods, demonstrating the potential of combining multiple prompt types for more reliable outputs. While most studies focus on single-task prompts, some research has explored multitask prompting approaches across various applications, from question–answering to commonsense reasoning \[ [6](https://www.mdpi.com/2079-9292/13/23/4712#B6-electronics-13-04712)\]. Multitask prompting aims to create a single prompt that can handle multiple related tasks, thus improving the efficiency of Large Language Models by reducing the need to design task-specific prompts. This approach has been particularly beneficial in scenarios where models must adapt quickly to a wide range of questions or tasks without retraining, underscoring the versatility of prompt engineering as a technique for broadening the applicability of Large Language Models \[ [6](https://www.mdpi.com/2079-9292/13/23/4712#B6-electronics-13-04712)\]. These advancements in prompt engineering contribute to improving Large Language Models’ performance across diverse NLP tasks without modifying core model parameters. By optimizing the way models interact with input prompts, researchers are able to enhance Large Language Models’ capabilities in handling complex, varied, and specialized tasks, driving forward the field of NLP and expanding the utility of these powerful models in real-world applications.

### The Relation Between Prompt Architecture and Large Language Model Size

Recent research has delved into the interplay between the size of Large Language Models (LLMs) and the architecture of prompts used to guide them. The consensus emerging from these studies is that, while larger models generally benefit from prompts containing a greater number of examples, enhancing their overall accuracy and reliability \[ [7](https://www.mdpi.com/2079-9292/13/23/4712#B7-electronics-13-04712)\], this is not an absolute rule. In particular contexts, smaller, more specialized models have been shown to outperform their larger counterparts. This phenomenon is especially evident in highly specific domains where smaller LLMs, fine-tuned on domain-specific data, demonstrate superior accuracy and efficiency compared to generalized, larger models \[ [8](https://www.mdpi.com/2079-9292/13/23/4712#B8-electronics-13-04712)\]. These findings underscore the importance of model specialization and the targeted use of data, suggesting that model size alone is not a definitive predictor of performance. Moreover, the structure and complexity of prompts themselves play a critical role in determining LLM performance. Research has demonstrated that simple, straightforward prompt structures are often more effective for knowledge retrieval tasks compared to prompts that employ complex grammatical constructions. For instance, Linzbach et al. \[ [9](https://www.mdpi.com/2079-9292/13/23/4712#B9-electronics-13-04712)\] found that prompts with less syntactic complexity allow models to retrieve relevant information more consistently, minimizing the risk of misinterpretation or erroneous outputs. This insight has significant implications for the design of user interactions with LLMs, suggesting that clarity and simplicity should be prioritized when crafting prompts, especially when the goal is to extract factual or technical information.

However, the sensitivity of LLMs to minor variations in prompt formatting remains a substantial challenge. Even subtle changes—such as the reordering of examples, shifts in tone, or slight alterations in wording—can have a pronounced impact on performance. In few-shot learning contexts, where LLMs are provided with only a handful of examples to guide their responses, Sclar et al. \[ [10](https://www.mdpi.com/2079-9292/13/23/4712#B10-electronics-13-04712)\] observed discrepancies in accuracy reaching as high as 76 percentage points due to minimal prompt adjustments. Notably, this sensitivity is not confined to any specific model size or level of training; it persists across a wide spectrum of LLMs, independent of the number of examples given or the extent of instruction tuning applied. These findings highlight an inherent instability in LLM responses that complicates their evaluation, making it difficult to establish reliable benchmarks. To mitigate this variability, it has been suggested that assessments of LLMs should not rely on a single-prompt format. Instead, evaluations should encompass a diverse set of prompt configurations to capture a more accurate picture of model performance. Such an approach acknowledges the influence that prompt design can exert on results and seeks to account for this factor in comparative analyses. In response to these challenges, Sclar et al. \[ [10](https://www.mdpi.com/2079-9292/13/23/4712#B10-electronics-13-04712)\] introduced the concept of “FormatSpread”, a methodology designed to systematically examine how variations in prompt format impact LLM outputs. FormatSpread aims to provide a more nuanced evaluation framework that includes an array of prompt formats, thereby enabling a more comprehensive understanding of model behavior and capabilities. The implications of these studies are far-reaching, as they call into question some common assumptions about LLM development and evaluation. The findings suggest that model size, while important, should not overshadow considerations of prompt design, specialization, and sensitivity. Furthermore, they highlight the need for a more sophisticated evaluation paradigm that acknowledges the complexities of language prompts and their effects on model performance. Researchers are increasingly advocating for evaluation protocols that reflect the diverse ways in which LLMs might be engaged in practical applications, thereby ensuring that performance metrics are both robust and representative of real-world usage scenarios.

To further build upon the discussion, our empirical study seeks to highlight the inherent complexity in determining the optimal use of single-task versus multitask prompts within a fixed-prompt architecture. Existing research often contrasts these approaches in specific contexts, suggesting that single-task prompts may offer precision and focus when handling distinct tasks, while multitask prompts provide efficiency and flexibility, especially in environments where models need to generalize across a wide array of related tasks without additional tuning. However, there is no definitive guideline to suggest that one method consistently outperforms the other across all scenarios. Our study aims to empirically demonstrate that the decision between single-task and multitask prompts cannot be universally dictated by a single criterion or strategy. In fixed-prompt architectures, the effectiveness of these approaches is highly dependent on factors such as the complexity of the tasks, the domain specificity, and the nature of the input data. We contend that instead of searching for a one-size-fits-all rule, researchers and practitioners should adopt a context-sensitive strategy, evaluating the trade-offs between precision and generalization based on the specific requirements of the task at hand. This nuanced perspective aligns with the broader trend in prompt engineering research, which emphasizes the importance of tailoring prompts to the unique characteristics of the target application, thus challenging the notion that a universal solution exists for optimizing prompt performance within Large Language Models.

## 3\. The Experiment

The objective of our experiment is to generate a JSON output for each observation in the dataset, which will be directly compared to the ground truth JSON. The dataset holds movies reviews written by users of the web. The ground truth JSON includes the sentiment label, named entities extracted from the review, and the original review text extracted from the IMDB dataset (as shown in [Listing A1](https://www.mdpi.com/2079-9292/13/23/4712#app1-electronics-13-04712)). To achieve this, we employed two distinct approaches: a single-task approach and a multitask approach, as shown in the [Figure 1](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-f001), below. These methodologies were designed to test the efficiency and accuracy of different prompt strategies for Large Language Models in handling multiple tasks simultaneously versus individually.

The two experimental workflows provide a comprehensive framework for evaluating the efficiency and precision of single-task versus multitask prompts. The outputs from both approaches were systematically compared against the ground truth JSON to determine the following key metrics: accuracy, which involves the correctness of sentiment classification and named entity recognition in both single-task and multitask scenarios; and consistency, which refers to the consistency of JSON formatting and structure across different prompt strategies.

### 3.1. The Dataset

In this study, we constructed our dataset using the IMDB review dataset available on Kaggle \[ [11](https://www.mdpi.com/2079-9292/13/23/4712#B11-electronics-13-04712)\], a well-established dataset commonly employed in sentiment analysis research. The IMDB dataset contains movie reviews, each labeled with binary sentiment values indicating whether the sentiment is positive or negative. This dataset forms the basis of our comparative analysis, which focuses on evaluating the performance of prompt strategies for Large Language Models (LLMs) in both sentiment analysis and named entity recognition (NER) tasks. Given the large size of the original IMDB dataset, we performed a random sampling to select 1000 reviews, ensuring a manageable yet representative subset for our experiments. To enrich the dataset with named entity information, we utilized the SpaCy library, a leading tool in NLP for English language tasks \[ [12](https://www.mdpi.com/2079-9292/13/23/4712#B12-electronics-13-04712)\]. We selected SpaCy’s transformer-based model, en\_core\_web\_trf, known for its ability to capture nuanced contextual information and accurately identify entities. For each review, we applied SpaCy’s NER function to extract named entities, specifically targeting categories such as persons (PER), locations (LOC), and organizations (ORG). This extraction process involved tokenizing the review text, identifying potential entities using the transformer architecture, and classifying them into relevant categories. Following NER processing, we augmented the dataset by introducing an additional column labeled “entities”. This column contains a structured list of the extracted entities for each review, organized in a dictionary format with the entity type (e.g., PER, LOC, ORG) and the corresponding text identified by the SpaCy model. This structured representation facilitates further analysis and allows us to incorporate entity information seamlessly into our experimental framework.

The final dataset is composed of three primary components: the original review text, the sentiment label provided by the IMDB dataset, and the named entities extracted through SpaCy. To better clarify the dataset structure, we show an example in the [Table 1](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t001) below. We organized this information into a JSON format, where each review is represented by three keys: “review” for the original text, “sentiment” for the sentiment label, and “entities” for the list of named entities. This JSON structure supports a comprehensive examination of LLM performance across both single-task and multitask prompts, ensuring a rigorous and systematic evaluation of the models’ accuracy and effectiveness. By leveraging the IMDB dataset’s extensive sentiment annotations and supplementing it with high-quality named entity data, we created a multifaceted testing ground to assess the efficacy of different prompting strategies for LLMs. This dual-task setup not only provides a clear benchmark for comparative performance but also highlights the practical applications of LLMs in real-world scenarios that require the integration of multiple NLP tasks.

#### Justification for IMDB Dataset Selection

Our choice to employ the IMDB dataset is grounded in its suitability for studying the capabilities of LLMs in realistic and diverse linguistic environments. The dataset is composed of user-generated movie reviews, which inherently vary in writing style, linguistic complexity, and formal accuracy. This variety introduces challenges that are essential for evaluating the robustness of LLMs, as user-generated content often includes informal expressions, grammatical errors, and unconventional syntactic structures—features that are less prevalent in professionally curated texts. The IMDB dataset’s broad adoption in the NLP research community, particularly in sentiment analysis studies, provides a well-defined benchmark for experimental comparison. Its widespread use enables us to position our findings within the context of the existing literature, facilitating a reliable assessment of the efficacy of different prompting strategies. Furthermore, the dataset’s focus on movie reviews—texts that often combine objective descriptions with subjective opinions—makes it an excellent resource for tasks requiring both sentiment analysis and NER. By selecting a dataset that closely mirrors the types of language encountered in everyday user interactions, we aim to ensure the relevance and applicability of our study. This choice allows us to evaluate the performance of LLMs in handling complex, real-world linguistic inputs, contributing to a deeper understanding of how these models manage the intricacies of unstructured and diverse language.

### 3.2. The Prompt Architecture

The experiment workflow is meant to compare the single-task prompt approach with the multitask prompt approach. We employed a fixed-prompt architecture with the aim to provide a sort of model-agnostic usage. The use of a fixed-prompt architecture in prompt engineering is driven by several factors that enhance the rigor and efficiency of comparative analysis. A fixed set of prompts allows for a fair comparison across different models, as it maintains a consistent input structure. This consistency ensures that the effects observed are due to the models’ architecture and capabilities, rather than variations in prompt formulation. In doing so, potential biases from tailored prompts for individual tasks or models are avoided, leading to a more accurate attribution of performance differences. Another advantage of the fixed-prompt approach is its ability to reduce both complexity and computational costs. By removing the need to optimize prompts for each specific task, the development and testing process becomes more straightforward. This not only saves time but also conserves computational resources, as prompt tuning is often an iterative and resource-intensive endeavor. Furthermore, a fixed-prompt strategy facilitates the assessment of a model’s generalization and robustness. Using a standardized set of prompts across tasks allows for a clear evaluation of how well a model generalizes, making comparisons between multitask and single-task approaches under uniform conditions possible. This serves as a robust test of a model’s ability to handle generic, non-optimized inputs. Scalability and ease of maintenance are also supported by this architecture. A uniform set of prompts makes system updates or modifications less complex, since changes do not require re-optimizing prompts for individual tasks. This scalability is particularly advantageous in large-scale applications, where the number of tasks may increase over time, allowing systems to expand without significant increases in maintenance overhead. The choice of a fixed-prompt architecture also enhances reproducibility, which is crucial for academic research. A consistent input context increases the likelihood that results are replicable, providing a stable baseline for evaluating the benefits of adaptive or optimized prompts. This stability allows for a quantitative assessment of prompt optimization by comparing results to a standardized reference point.

The implications of adopting a fixed-prompt architecture extend to both research and practical applications. In research, it enables more reliable benchmarking across different models, making comparisons more meaningful. Researchers can identify genuine performance differences attributable to the models themselves, rather than adjustments in prompt design, leading to a clearer understanding of the strengths and limitations of various architectures, particularly in multitask versus single-task settings. This approach also places a strong emphasis on generalization. Evaluating models under a consistent set of prompts highlights their ability to handle diverse tasks, pushing the field towards the development of architectures that perform well across a wide range of contexts without extensive adaptation. This could encourage the creation of more versatile and generalizable AI systems, as opposed to those relying on domain-specific prompt optimization. In practical applications, the fixed-prompt strategy significantly impacts scalability. In scenarios where the number of tasks or domains grows over time, using a single set of prompts allows systems to expand efficiently, making large-scale deployment more feasible and cost-effective. This is particularly valuable in commercial settings, where operational efficiency and scalability are key considerations. From a research methodology perspective, a fixed-prompt architecture establishes a solid baseline, enhancing the reproducibility of studies by providing a clear and invariant prompt set. This promotes rigorous scientific discourse, allowing new methods to be evaluated against well-defined standards. However, this approach places significant importance on the initial prompt selection. The chosen prompts must be representative and carefully designed to ensure fair assessment across a variety of tasks. If the prompts are poorly selected, they might either obscure a model’s strengths or exaggerate its weaknesses, potentially leading to misleading conclusions.

#### 3.2.1. The Single-Task Approach

In the single-task prompt approach, we decoupled the tasks of sentiment classification, named entity recognition (NER), and JSON formatting into separate, distinct operations. The goal was to isolate each task to determine how effectively Large Language Models can perform when given a dedicated prompt for each task. The process began with sentiment classification. We first used a single-task prompt to classify the binary sentiment of each review. The Large Language Models were prompted to read the review text and determine whether the sentiment was positive or negative. All 1000 elements in our dataset were processed independently, with each review being fed into the LLM, and a sentiment label (either “positive” or “negative”) was generated for each review. This operation produced an initial output consisting solely of sentiment classifications. Following sentiment classification, a separate prompt was employed to extract named entities from the reviews. The entities included people (PER), locations (LOC), and organizations (ORG). Each review was again processed individually through the Large Language Models, this time with a focus on identifying and classifying named entities. The output of this step was a collection of lists containing the extracted entities for each review. The final step involved formatting the results into a structured JSON format using the outputs from the first two tasks. The sentiment labels and named entities were combined with the original review text to create a JSON object for each review. Each JSON object included keys for “review”, “sentiment”, and “entities”, matching the structure of the ground truth JSON. This step ensured that the outputs were aligned with the expected format for comparison. A clarifying UML activity diagram of the approach is displayed below in [Figure 2](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-f002).

The used single-task prompts are shown in [Appendix Listing A3](https://www.mdpi.com/2079-9292/13/23/4712#app2-electronics-13-04712). Single-task prompts were designed to create a chain of invocations where the outputs of two calls are used as input context for the final prompt. The first two prompts performed named entity recognition (NER) and sentiment analysis classification tasks. The output of these two tasks then merged and was used as input for the third prompt, whose goal is to reorganize the obtained information, producing a comprehensive JSON output.

#### 3.2.2. The Multitask Approach

The multitask prompt approach was designed to evaluate the performance of Large Language Models when tasked with performing multiple tasks simultaneously. In this method, a single prompt was used to instruct the Large Language Models to carry out sentiment classification, named entity recognition, and JSON formatting in one unified operation. The detailed prompt is shown in [Appendix Listing A2](https://www.mdpi.com/2079-9292/13/23/4712#app2-electronics-13-04712).

In this approach, we used a unified prompting strategy where the Large Language Models were provided with a single, comprehensive prompt for each review. To better clarify the workflow, we provide an UML activity diagram shown in [Figure 3](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-f003). This prompt instructed them to analyze the sentiment, extract named entities, and format the results into a JSON object. All 1000 reviews were processed in a batch manner, with each review being fed into the LLM with a multitask prompt designed to handle all three tasks at once. The output for each review was a complete JSON object containing the sentiment classification, extracted entities, and the review text itself. By handling sentiment analysis, named entity recognition, and JSON formatting in parallel, the multitask approach leverages the Large Language Models’ ability to process complex, integrated prompts. The final output for each review was a JSON object directly generated by the LLM, structured similarly to the ground truth JSON. This direct approach allows for the assessment of the Large Language Models’ capability to multitask effectively and efficiently.

### 3.3. Execution Environment

The experiment was executed in Jupyter notebooks, which are publicly available on our GitHub repository \[ [13](https://www.mdpi.com/2079-9292/13/23/4712#B13-electronics-13-04712)\]. This decision aligns with our commitment to transparency and reproducibility, allowing other researchers to access and replicate our findings with ease. The Jupyter notebooks provide a detailed step-by-step account of the entire experimental workflow, including data preprocessing, prompt formulation, and LLM interactions. By using Jupyter notebooks, we ensure that each experiment is documented in a manner that captures the nuances of our methodology, from data ingestion to output generation. These notebooks not only contain the code used for executing each task but also include commentary and insights into the decisions made throughout the experiment. This transparency is crucial for fostering collaboration and innovation within the research community. In addition to the code, the dataset utilized in our study is also hosted on the same GitHub repository. The dataset includes the processed IMDB reviews, along with the generated JSON outputs for both single-task and multitask approaches. By providing both the data and the code, we facilitate an open-access environment where researchers can easily validate and build upon our work. Our GitHub repository serves as a comprehensive resource for those interested in exploring the intricacies of LLM prompt strategies. It invites further exploration and experimentation, offering a platform for continuous improvement and shared learning within the field of natural language processing.

#### The Temperature

In our study, we deliberately set a fixed temperature of 0.8 for all models. This decision was grounded in the need to maintain a balance between precision and creativity in the outputs. A temperature setting of 0.8 was chosen because it avoids the extremes of determinism and randomness. Lower temperatures, closer to zero, tend to produce highly deterministic responses, reducing variability and creativity, which may inhibit the model’s ability to explore diverse but relevant outputs. Conversely, higher temperatures might lead to overly creative or tangential responses, increasing the likelihood of generating irrelevant or imaginative content that could obscure the evaluation of the models’ true capabilities. By fixing the temperature at this intermediate level, our goal was to create conditions that would allow the models to demonstrate their generalization abilities more effectively. The selected temperature encourages the generation of outputs that are varied enough to showcase the models’ adaptability across tasks, yet sufficiently constrained to remain grounded in relevant contexts. This configuration emphasizes the models’ inherent capacity to manage diverse scenarios without relying on extreme prompt tuning or specialized adjustments.

The decision to keep a consistent temperature across all experiments ensures a fair and controlled environment for comparative analysis. It eliminates the variability that might arise from fluctuating temperature settings, thereby allowing us to attribute differences in performance directly to the models’ architectures and underlying mechanisms, rather than to variations in sampling strategies. This standardized approach not only enhances the reliability of our findings but also facilitates a deeper exploration of each model’s potential to generalize effectively across multiple tasks without excessive prompting or guidance. Thus, the fixed temperature of 0.8 was not merely a technical choice, but a strategic decision aimed at fostering a thorough assessment of each model’s robustness and flexibility, while maintaining a consistent baseline that allows for equitable comparisons. This enabled us to investigate how different architectures handle the inherent complexity and diversity of the prompts, offering insights into their adaptability and generalization capabilities under a balanced but challenging setting.

### 3.4. The Employed Large Language Models

In this study, we focused on evaluating the performance of five different open Large Language Models (Large Language Models) for sentiment analysis and named entity recognition tasks.

The term “open” when referring to Large Language Models, as highlighted by Liesenfeld and Dingemanse \[ [14](https://www.mdpi.com/2079-9292/13/23/4712#B14-electronics-13-04712)\], encompasses significant differences across various levels of “openness” in AI models, which can be categorized as follows:

- Open-source: The model’s source code is fully accessible and modifiable.

- Open-weights: The trained model weights are available, but possibly with licensing restrictions.

- Open-access: The model can be accessed via API, but without access to the code or weights.

- Open-science: The research methodology and results are publicly documented.

In the context of our study, the models used are primarily classified as “open-weights”, as their weights are publicly available and redistributable, though with some restrictions specified in their licenses. It is important to note that this level of openness, while significant for research reproducibility, does not necessarily equate to full freedom of use and modification, as would be found in a fully open-source project. Furthermore, as Bielefeld and Dingemanse emphasized, the simple label of “open” can obscure various degrees of restrictions and limitations, which are crucial to understand for an accurate assessment of accessibility and reproducibility in AI research.

The primary motivation behind selecting open-weight models was to enhance the reproducibility of our research. By choosing models that are accessible to the public, we ensure that other researchers can replicate our experiments, verify our findings, and build upon our work without the constraints often associated with proprietary models. While state-of-the-art Large Language Models such as OpenAI’s GPT, Anthropic’s Claude, and Google’s Gemini have demonstrated remarkable performance across a wide range of language tasks, their proprietary nature poses challenges for academic research in terms of accessibility and transparency. These models often come with usage restrictions, limited customization options, and require considerable computational resources, which can hinder reproducibility and broader scientific exploration. Therefore, to foster an open and collaborative research environment, we selected a set of high-performing open-weight models that provide a balance between accessibility and capability. The specific Large Language Models we employed in our study are as follows:

- LLama 3.1 8B (8b-instruct-q4\_0).

- Phi3 Medium (14b-medium-128k-instruct-q4\_0).

- Qwen2 7B (7b-instruct-q4\_0).

- Gemma2 9B (9b-instruct-q4\_0).

- Mistral 7B (7b-instruct-v0.3-q4\_0).

#### 3.4.1. Justification for Employed Large Language Models

The selection of these specific open-weight models was guided by several factors. Using open-weighted models, we enhanced the reproducibility of our research, enabling other researchers to replicate our experiments and validate our findings without proprietary restrictions. Open-weight models are generally more accessible, allowing a wider range of researchers and practitioners to engage with the research, regardless of their institutional or financial resources. Although not in absolute state of the art, the chosen models still offer competitive performance in sentiment analysis and named entity recognition tasks, providing meaningful insight into LLM capabilities. Open-weight models benefit from active community participation, which leads to continuous improvements and innovations. This collaborative environment fosters the development of robust models that evolve in response to community needs and feedback. The selected models have varying parameter sizes that allow for experimentation on different computational platforms, from local machines to more extensive cloud-based infrastructures, facilitating scalable research approaches. In order to determine the five candidates, we observed the “Open LLM Leaderboard 2” hosted on Huggingface that lists the open-weight LLM performances \[ [15](https://www.mdpi.com/2079-9292/13/23/4712#B15-electronics-13-04712), [16](https://www.mdpi.com/2079-9292/13/23/4712#B16-electronics-13-04712), [17](https://www.mdpi.com/2079-9292/13/23/4712#B17-electronics-13-04712), [18](https://www.mdpi.com/2079-9292/13/23/4712#B18-electronics-13-04712), [19](https://www.mdpi.com/2079-9292/13/23/4712#B19-electronics-13-04712), [20](https://www.mdpi.com/2079-9292/13/23/4712#B20-electronics-13-04712), [21](https://www.mdpi.com/2079-9292/13/23/4712#B21-electronics-13-04712), [22](https://www.mdpi.com/2079-9292/13/23/4712#B22-electronics-13-04712), [23](https://www.mdpi.com/2079-9292/13/23/4712#B23-electronics-13-04712)\]. We accessed this leaderboard in June 2024. By focusing on open-weight Large Language Models, this study not only provides valuable insights into the effectiveness of prompt strategies, but also contributes to a body of work that prioritizes transparency and accessibility in AI research. This approach aligns with the broader goals of promoting open science and collaborative innovation within the machine learning community.

In this study, the decision to utilize a smaller model, rather than opting for larger and potentially more capable alternatives, was driven by several key considerations. Firstly, smaller models offer substantial advantages in terms of resource efficiency. They require less computational power, memory, and storage, leading to reduced costs and time investment during the experimental phase. This is particularly pertinent when a high volume of experiments must be conducted or when computational resources are constrained. Additionally, the complexity of the tasks under investigation, which focused on single-classification operations, did not necessitate the deployment of the most sophisticated or extensive models. The relative simplicity of single-classification tasks can often be effectively managed by smaller models without significant losses in accuracy, thereby making their use more practical. Furthermore, the primary objective of this study was to explore the impact of different prompt strategies, specifically comparing single-task prompts with multitask prompts, rather than to assess the raw capabilities of large-scale models. Employing smaller models allowed for the isolation of prompt strategy effects, minimizing the potential influence of a model’s inherent complexity on the observed outcomes.

The study’s exclusive focus on single-classification tasks was similarly motivated by the need for a controlled and precise evaluation framework. Single-task classification offers a streamlined environment for analyzing how prompt modifications influence model performance, eliminating the complexities and additional variables that multitask scenarios would introduce. This simplicity enhances the reproducibility and comparability of results across various models and prompt strategies, allowing for clearer and more reliable insights. Moreover, single-classification tasks often serve as foundational elements within more complex natural language processing tasks. By initially concentrating on these simpler operations, the study establishes a robust baseline for understanding the dynamics of prompt strategies, which could potentially be extended to more intricate multitasking assessments in future research. In sum, the decision to employ smaller models and to focus on single-task classification facilitated a research environment in which the effects of prompt strategies could be isolated and scrutinized with greater clarity.

#### 3.4.2. The Adoption of Ollama

Ollama is an open-source framework developed to facilitate the local deployment and execution of Large Language Models (LLMs). In our experiments, Ollama played a pivotal role, serving as the platform for deploying the five chosen LLMs: LLama 3.1 7B, Phi3 Medium, Qwen2 7B, Gemma2 7B, and Mistral 7B. Its selection was driven by its user-friendly interface, ease of use, and strong alignment with our commitment to reproducibility, which is central to our research objectives. By employing Ollama, we ensured that our experimental setup remains accessible and easily replicable, fostering transparency and collaboration within the research community.

Ollama’s architecture is built upon a REST API, which simplifies model interactions through automated management processes. The framework automatically checks the local availability of requested models; if a model is not found, Ollama alerts the user and facilitates a direct download. After acquisition, the framework autonomously manages the configuration process, optimizing the model according to the available hardware. These steps encompass the extraction of model files, the fine-tuning of memory resources through quantization, and the balancing of computational loads across the RAM, CPU, and GPU. Additionally, Ollama integrates robust error management, verifying the integrity of downloaded files and recording any discrepancies to aid debugging. This architectural design ensures compatibility across major operating systems, making Ollama a versatile and accessible choice for both researchers and practitioners. In our study, this cross-platform compatibility was crucial, as it enabled a consistent and reliable setup regardless of the specific hardware used by different members of the research community.

A core feature of Ollama is its implementation of quantization, a technique that significantly reduces the numerical precision of model parameters while maintaining acceptable levels of accuracy. This reduction involves converting high-precision data types like float32 (32-bit) to more compact formats such as int8 (8-bit) or int4 (4-bit). Quantization drastically lowers memory consumption, a vital advantage for the local execution of large models. For example, a seven billion parameter model in float32 format may require up to 28 GB of RAM, whereas the int8 version requires only about 7 GB. This efficiency was particularly advantageous in our experiments, as it allowed us to run multiple high-parameter models locally without compromising performance, facilitating efficient and reproducible testing.

Ollama utilizes a standardized inference pipeline, structured into four primary phases, to optimize the execution of LLMs as shown in [Figure 4](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-f004). This structured approach was instrumental in our study, ensuring consistent and high-quality output across various models. The first phase, preprocessing, involves the preparation of input data. Text is tokenized into discrete units that the model can process, a context is constructed to guide comprehension, and memory resources are dynamically allocated. This ensures that each model receives input in a format conducive to accurate processing. In the execution phase, the framework loads the quantized model into memory and sequentially processes tokens. Effective cache management during this phase minimizes latency by reusing previously computed results, optimizing repeated tasks. The generation phase is dedicated to transforming processed tokens back into human-readable text. Advanced sampling techniques, such as beam search and nucleus sampling, are employed to enhance the quality of generated output, while incremental generation enables real-time responses. This step-by-step text generation was particularly useful in our research, as it allowed us to monitor model outputs in real time, facilitating adjustments where necessary. Finally, the postprocessing phase involves refining the generated output. Text is formatted into a coherent structure, memory resources are released, and the final output is prepared in JSON format for exposure via the API. This systematic approach, coupled with Ollama’s user-friendly interface, allowed us to maintain a reproducible and transparent workflow throughout our experiments.

Our choice of Ollama was not merely technical but also philosophical. The platform’s straightforward installation and configuration allowed us to maintain a high level of accessibility, ensuring that others can easily replicate our setup without extensive technical expertise. Its active support for a broad range of open-weight models, including those integral to our research, was another decisive factor. By enabling a seamless integration of diverse LLMs, Ollama ensured consistent execution across different experimental scenarios, contributing to the robustness of our findings. By leveraging Ollama, we adhered to our commitment to open science. The platform’s widespread usability means that any researcher interested in our work can replicate our environment and methodology with minimal effort. This accessibility not only bolsters the credibility of our results but also encourages further validation and exploration, thereby fostering a collaborative research ecosystem. Our decision to use Ollama aligns with a broader movement towards transparent and reproducible science, contributing to a culture of open inquiry and shared discovery.

### 3.5. Evaluation

In order to rigorously assess the performance of the Large Language Models (Large Language Models) employed in our study, we designed a comprehensive evaluation metric that integrates three critical components: sentiment exact match, named entity recognition (NER) performance, and review text fidelity. Our evaluation metric is designed to provide a holistic measure of how effectively the Large Language Models handle the tasks of sentiment classification, named entity extraction, and text reproduction. The evaluation metric is defined as follows:

f(x,y,z)=x+y+z3

where x is the exact match of sentiment detection, defined as follows:

x=1ifthedetectedsentimentiscorrect0otherwise

Then, y represents the F1 score of the named entity recognition (NER). True positives are entities present in both the ground truth and the output. False negatives refer to those missing from the output but included in the ground truth, while false positives are found in the output but absent from the ground truth.

This score reflects the precision and recall balance achieved by the Large Language Models in identifying and classifying named entities within the review text. The “exact match” approach has been used here. z is the BLEU (Bilingual Evaluation Understudy) score of the review, which measures how closely the generated review matches the original text. This component of the metric evaluates the LLM’s ability to reproduce the review text accurately. The function f(x,y,z) computes the arithmetic mean of x, y, and z, providing an overall performance score for each review processed by the Large Language Models. By averaging these three metrics, we achieve a balanced evaluation that considers both classification accuracy and text generation quality. The rationale behind this metric is to ensure that each aspect of the task is equally weighted, acknowledging the importance of sentiment exact match, entity recognition precision, and fidelity to the original review text. This holistic approach allows us to capture the multifaceted nature of the task, offering a robust framework for evaluating the effectiveness of different prompting strategies in Large Language Models.

The LLM’s output is postprocessed in order to extract the right JSON data. This is due to the fact that Large Language Models often respond discoursively without providing strict JSON. Two distincts regular expressions are used in this scenario. The former one, mentioned in [Appendix Listing A4](https://www.mdpi.com/2079-9292/13/23/4712#app3-electronics-13-04712) is used to remove JSON comments. Sometimes, Large Language Models follow the JSONC format for their answers instead of JSON, so we need to remove all the comments in order to parse the data correctly. Then, the second one, mentioned in [Appendix Listing A5](https://www.mdpi.com/2079-9292/13/23/4712#app3-electronics-13-04712), is a regular expression used to extract the JSON string. Ultimately, it extracts the group starting from the first left curly bracket and ending with the last right curly bracket. Moreover, Large Language Models tend to respond with a JSON that uses single apices instead of double quotes. So, in a pythonic manner, the algorithm works as shown in [Appendix Listing A6](https://www.mdpi.com/2079-9292/13/23/4712#app3-electronics-13-04712), assuming that the two regular expressions have already been applied. When the parsing fails, we attribute a score of 0% to that case.

## 4\. Results

The analysis of our experimental results provides a nuanced perspective on the efficacy of multitask versus atomic single-task prompts. Contrary to our initial hypothesis, the data reveal that the atomic single-task prompt approach does not uniformly outperform a multitask prompt across all contexts. Our study highlights significant variability in prompt effectiveness depending on the specific model used. This observation suggests that the interaction between prompt type and model architecture is complex and warrants careful consideration. Specifically, the performance of a given prompt can be highly sensitive to the underlying model’s characteristics, indicating that model-specific factors play a crucial role in determining the relative success of prompting strategies. In detail, our experiments yielded mixed outcomes. Out of the five distinct experimental setups, three demonstrated that atomic single-task prompts were more effective than their multitask counterparts. These results suggest that for certain tasks, simpler and more specialized prompts may offer advantages in terms of accuracy or efficiency. Conversely, two experiments showed that multitask prompts provided superior performance, challenging the assumption that simplicity inherently leads to better outcomes. This variability underscores the importance of tailoring the prompting approach to the specific task and model, rather than relying on a one-size-fits-all strategy.

Furthermore, the unexpected nature of our findings is worth noting. Despite the theoretical benefits of atomic single-task prompts such as the potential for improved efficiency and generalization, the empirical evidence from our study does not consistently support these advantages. We had anticipated that the low complexity associated with single-task prompts would correlate with enhanced performance. However, the results indicate that this expectation does not always hold true in practice. The complexity of single-task prompts did not translate into universally superior outcomes compared to the relatively straightforward multitask prompts. Additionally, our investigation included a range of models with varying sizes, from 2 billion to 14 billion parameters. The results from these experiments did not reveal a clear relationship between model size and prompt effectiveness. This finding suggests that the performance of prompting strategies is not solely dependent on the scale of the model but is influenced by other factors, such as task characteristics and prompt design. The [Table 2](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t002) below shows the mean scores for each model and approach, where “scores” mean the metric explained in [Section 3](https://www.mdpi.com/2079-9292/13/23/4712#sec3-electronics-13-04712).

### 4.1. Stastical Significance

In this section, we present a series of statistical tests conducted to provide additional evidence supporting our findings. First, we performed the Shapiro–Wilk test to assess whether the distributions of our data were normal. The results clearly indicate that all distributions deviate significantly from normality, as reflected by the extremely low p-values reported in [Table 3](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t003). These p-values, consistently below conventional thresholds (e.g., 0.05), strongly suggest that none of the distributions for the evaluated metrics follow a normal pattern.

Given the non-normal nature of the data, we employed the Wilcoxon signed-rank test for continuous metrics such as F1, BLEU, and the overall score. For the categorical metric, specifically the Exact-Match score for Sentiment (which can take a binary value of 0 or 1 depending on whether the output matches the ground truth), we opted for the McNemar test. The decision to use these non-parametric tests ensures that our analysis remains statistically valid despite the deviations from normality. The results are summarized in [Table 4](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t004).

Expanding upon the results, the findings provide valuable insights into how different models react to single-task versus multitask prompting strategies across a variety of evaluation metrics. Each metric presents a distinct pattern of sensitivity, indicating that the effectiveness of the prompting approaches is not uniform across tasks or models, highlighting the nuanced behavior of Large Language Models.

For the NER F1 metric, the Wilcoxon test identified significant differences in most models, suggesting that the choice between single-task and multitask prompts can substantially influence the model’s ability to recognize named entities. However, the exception of LLama 3.1 8B, with a p-value just above the conventional threshold of 0.05, indicates a borderline case where the prompting approach may have an impact, but not to a statistically significant extent. This borderline result suggests that LLama 3.1 8B might be relatively resilient to changes in prompt structure for NER tasks, or that its response to such changes lies within a range of performance variability where differences do not reach statistical significance. This observation could warrant further investigation, possibly involving larger sample sizes or additional metrics, to clarify if this lack of significance is inherent to the model or a result of sample-specific variability.

In the case of the BLEU score, which is a critical measure for assessing the quality of generated text in review scenarios, the Wilcoxon test demonstrated overwhelmingly significant results for most models, with Phi3 Medium and Qwen 2 7B exhibiting particularly strong effects. The extremely low p-values suggest that these models are highly sensitive to the structure of the prompt when tasked with generating coherent and accurate text. This sensitivity implies that for text generation tasks, selecting the appropriate prompting strategy is crucial, as it can lead to substantial differences in the quality of the generated output. The stark significance across multiple models also suggests that multitask prompting could provide a structured context that enhances generative quality, particularly for complex or multi-dimensional output like reviews.

The results for the Sentiment Score, analyzed using the McNemar test, present a more heterogeneous picture. Only Mistral 7B exhibited a strong statistically significant result, suggesting that it is particularly responsive to the choice of the prompting strategy when it comes to binary sentiment classification. In contrast, the other models showed p-values around or above the 0.05 threshold, indicating a weaker or non-significant differentiation between single-task and multitask prompts in sentiment tasks. This outcome implies that for many models, sentiment classification may be relatively stable across prompting strategies, or that the gains from multitask prompting are not as pronounced in this binary classification context. It is possible that the simplicity of binary sentiment decisions, compared to more nuanced tasks like named entity recognition or text generation, reduces the sensitivity to prompt changes, particularly in models that are already well tuned for such binary classification tasks.

Lastly, the overall Score metric, which synthesizes multiple aspects of performance, reinforces the impact of prompting strategies, as indicated by the statistically significant differences observed for the majority of models. These results suggest that across a broad spectrum of metrics, the choice of prompt affects model performance, underscoring the importance of prompt engineering in optimizing LLM outputs. However, the lack of significance for Mistral 7B, as demonstrated by a p-value of 0.60, suggests a robustness in its performance, regardless of the prompting strategy. This consistency may indicate that Mistral 7B has a more uniform handling of information across different prompts, potentially due to architectural factors or training data characteristics that enable it to maintain stable performance. It could also reflect an inherent stability in how Mistral 7B processes diverse inputs, making it less prone to fluctuations in performance based on prompt structuring.

#### Statistical Tests to Compare Large Language Models

To compare the performance of the various models across different metrics and prompting conditions, we employed the Friedman test, a non-parametric statistical test suitable for analyzing data of repeated measures. This choice was motivated by the need to assess multiple models under the same conditions while avoiding assumptions of normality, which do not hold for our data distributions. The Friedman test allowed us to determine whether there were statistically significant differences between the models’ performances in both single-task and multitask scenarios, providing a robust comparison framework that accounts for the inherent dependencies in our experimental design.

Based on the Friedman test results shown in [Table 5](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t005), it is clear that significant differences exist between the performance of the evaluated models across all metrics, under both single-task and multitask prompting conditions. Each metric consistently demonstrates p-values that are orders of magnitude below typical thresholds for statistical significance (e.g., 0.05), indicating that the models exhibit distinct behaviors depending on the prompting strategy used. This consistent pattern of significance underscores the critical role that prompt structuring plays in shaping the output quality of Large Language Models.

The F1 score for named entity recognition (NER) reveals substantial model variability, both under single-task and multitask conditions. The Friedman statistic for single-task prompting is 1030.82, with a corresponding p-value of 7.49×10−222. This already indicates a strong differentiation among the models. In the multitask setup, the statistic slightly increases to 1050.92, with an even lower p-value of 3.29×10−226, reinforcing that the multitask strategy introduces subtle, yet statistically detectable, shifts in model performance.

The BLEU score, used for evaluating the quality of text generation in review scenarios, shows a notable significance across the models. In the single-task scenario, the Friedman statistic is 1002.16, with a p-value of 1.21×10−215, suggesting strong differences in text generation abilities when the models are prompted individually. The multitask configuration amplifies this distinction dramatically, with the statistic reaching 1970.88 and a p-value effectively equal to 0, indicating extremely robust model variability under multitask prompts.

Sentiment classification, measured by the Exact-Match score, also displays clear differences, although the statistics are relatively lower compared to F1 and BLEU scores. The Friedman test for single-task conditions yields a statistic of 655.21 and a p-value of 1.73×10−140, which is still well within the range of significance. Under multitask conditions, the statistic increases to 792.74, with a corresponding p-value of 2.87×10−170, suggesting that multitask prompting potentially offers a more nuanced differentiation between the models, even in simpler binary classification tasks.

The overall Score metric, synthesizing various aspects of model performance, presents the most pronounced differences. The Friedman statistic under single-task conditions is 1310.58, with an extremely low p-value of 1.69×10−282, indicating that single-task prompts already cause marked differences in overall performance. This differentiation becomes even more pronounced in the multitask scenario, where the statistic soars to 1808.26 with a p-value of 0, highlighting a profound impact of multitask prompts on overall model effectiveness.

The statistical evidence gathered from this study confirms that different prompting strategies have a tangible impact on model behavior across various evaluation metrics. This underscores the importance of carefully selecting prompting techniques based on the desired outcome. While single-task prompts provide a baseline for evaluating individual task performance, multitask prompting introduces additional complexity that can either enhance or differentiate model outputs more significantly, depending on the metric and task at hand. Future research should explore why certain models react more sensitively to prompt changes, potentially investigating architectural factors or training data characteristics that influence prompt responsiveness. Additionally, expanding the evaluation to include more diverse tasks and model types would offer further insights into the generalizability of these findings.

### 4.2. Descriptive Statistics Related to Model Performance

#### 4.2.1. Gemma 2 9B

Gemma 2 9B outperformed all other models in this study. Although the assumption that single-task prompts yield better results compared to the dual, multitask approach still holds true, it is worth noting that the difference in performance is not particularly pronounced. Shifting the focus to individual tasks, the table below provides a detailed breakdown of the results.

The data presented in the [Table 6](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t006) highlight the comparative performance of the multitask and single-task approaches for the Gemma 2 9B model across various metrics. The single-task approach demonstrates a slight edge in certain areas, such as Exact-Match accuracy on sentiment analysis, achieving 91.50% compared to 90.00% for the multitask approach, and in the NER F1 score, with a small improvement from 54.75% to 55.75%.

However, the multitask strategy shows advantages in NER Precision, scoring 60.99% versus 59.86% for the single-task prompts, suggesting that the multitask model may be more accurate in identifying named entities, though it comes at the cost of a slightly lower NER Recall (54.11% for multitask versus 56.87% for single-task).

Additionally, the formatting error rate is similar across both approaches, with a marginal difference of 1 per thousand (9.00‰for multitask versus 8.00‰for single-task), indicating that the complexity of the prompt does not significantly impact the model’s ability to maintain proper formatting. These data suggest that while single-task prompts may offer a slight performance benefit in certain aspects, the differences are generally minor, and multitask prompting retains certain advantages, particularly in precision.

#### 4.2.2. Qwen 2 7B

For Qwen 2 7B, the assumption that single-task prompts yield better results compared to the dual, multitask approach remains valid. However, in contrast to Gemma 2, the observed pattern is more erratic, and the performance gap between the two approaches becomes more pronounced in this case, as shown in [Table 7](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t007).

[Table 7](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t007) highlights a more significant divergence between the multitask and single-task approaches for Qwen 2 7B compared to Gemma 2 9B. Single-task prompts outperform multitask prompts across most metrics, particularly in the Mean BLEU score on review tasks (73.26% vs. 56.09%), indicating a substantial advantage in generating coherent and accurate text for single-task prompts. Similarly, the Exact-Match score for sentiment analysis is higher for the single-task approach (82.70% vs. 80.80%).

However, an interesting deviation can be observed in NER Precision, where multitask prompts demonstrate better performance (32.20% vs. 27.97%), suggesting that Qwen 2 7B’s ability to precisely recognize named entities benefits from the complexity of the multitask setup. Despite this, single-task prompts yield higher NER Recall (30.79% vs. 24.32%), reflecting a trade-off between precision and recall similar to what was observed in the previous model. Additionally, the formatting error rate is notably higher for single-task prompts (88.00‰vs. 34.00‰), suggesting that while single-task prompts may improve content accuracy, they introduce a greater risk of formatting errors, a factor worth considering in practical applications.

#### 4.2.3. LLama 3.1 8B

LLama 3.1 8B is the first model to deviate from the expected pattern. In contrast to previous models, the multitask approach outperforms the single-task approach, demonstrating a clear reversal of the trends observed earlier. LLama 3.1 8B performances are described in [Table 8](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t008).

[Table 8](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t008) reveals a distinctive performance pattern for LLama 3.1 8B, where the multitask approach shows superior results compared to the single-task approach across most metrics. Notably, the Mean BLEU score on review tasks is significantly higher for multitask prompts (88.94% vs. 76.55%), indicating that LLama 3.1 8B generates more coherent and contextually accurate responses when handling multiple tasks simultaneously. Similarly, in sentiment analysis, the multitask approach outperforms the single-task approach with a higher Exact-Match score (83.70% vs. 81.00%). However, the NER metrics present a more nuanced picture. While the single-task approach achieves a slightly higher F1 score (44.10% vs. 43.00%) and NER Recall (46.01% vs. 42.05%), multitask prompts excel in NER Precision (50.25% vs. 47.98%). This suggests that LLama 3.1 8B is more precise but slightly less comprehensive in recognizing named entities when dealing with multitask prompts. Additionally, the formatting error rate is notably lower in the multitask setting (69.00‰vs. 94.00‰), indicating that multitask prompts not only yield better content accuracy but also lead to fewer formatting errors. These results underscore the model’s capacity to handle multitask scenarios effectively, challenging the conventional assumption that single-task prompting is inherently superior.

#### 4.2.4. Phi 3 Medium

Regarding Phi3 Medium 14B, based on its performances listed in [Table 9](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t009), it can be unequivocally stated that its performance was the worst among all models in the experimental set. The difference in performance between the two prompting approaches is particularly stark, with the single-task approach significantly outperforming the multitask approach.

[Table 9](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t009) illustrates that Phi3 Medium 14B exhibits the weakest overall performance across all evaluated models. The results clearly demonstrate a substantial gap between the multitask and single-task approaches, with the latter consistently outperforming the former. For instance, the Mean BLEU score on review tasks is notably higher for single-task prompts (57.63% vs. 16.98%), indicating that Phi3 Medium 14B struggles significantly with generating coherent text in multitask scenarios. Similarly, the Exact-Match score for sentiment analysis shows a slight but consistent improvement in single-task settings (50.80% vs. 48.30%).

The disparity is even more pronounced in NER tasks, where the single-task approach nearly doubles the F1 score (22.62% vs. 11.68%) and achieves higher Precision (25.45% vs. 14.49%) and Recall (23.78% vs. 11.06%). These results suggest that Phi3 Medium 14B’s ability to recognize and categorize named entities is severely hindered in multitask settings.

Moreover, both approaches exhibit high formatting error rates, with the single-task method slightly worse (307.00‰vs. 253.00‰). This suggests that, although the single-task approach improves performance in content-related tasks, both prompting methods struggle with formatting precision. These results position Phi3 Medium 14B as the least capable model in handling complex or multitask scenarios, emphasizing the limitations of this particular architecture in the context of large-scale language models.

#### 4.2.5. Mistral 7B

The following [Table 10](https://www.mdpi.com/2079-9292/13/23/4712#electronics-13-04712-t010) reflects the mixed performance of Mistral 7B across various tasks, showcasing both strengths and weaknesses depending on the task and prompting approach.

In terms of review generation, the single-task approach achieves a higher Mean BLEU score (76.41% vs. 70.84%), indicating better text generation performance for single-task prompts. However, for sentiment analysis, the multitask approach far outperforms the single-task method with a notably higher Exact-Match score (87.20% vs. 71.80%). In named entity recognition (NER), the results are more nuanced. While the single-task approach yields a slightly higher F1 score (32.56% vs. 30.60%) and Recall (33.50% vs. 28.04%), the multitask approach achieves better Precision (39.28% vs. 37.05%), highlighting a trade-off between completeness and accuracy in entity recognition. One of the most significant differences is observed in the formatting error rate, where the multitask approach significantly outperforms the single-task approach, with a much lower error rate (29.00‰vs. 155.00‰). This suggests that multitask prompts not only excel in specific tasks, such as sentiment analysis, but also lead to more reliable formatting outputs. The overall distribution of scores confirms that Mistral 7B performs better under multitask settings in certain scenarios, although single-task prompts still offer advantages in specific metrics like BLEU and NER Recall.

The experiments conducted on the five models—Gemma 2 9B, Qwen 2 7B, LLama 3.1 8B, Phi3 Medium 14B, and Mistral 7B—present a diverse and complex landscape of performance across single-task and multitask prompting approaches. While the general assumption that single-task prompts yield superior results holds true for most models, the nuances of performance reveal significant variations depending on the architecture and task type. Gemma 2 9B and Qwen 2 7B conform to expectations, with single-task prompts outperforming multitask prompts across the majority of metrics, though the difference is more pronounced in Qwen 2 7B. In contrast, LLama 3.1 8B challenges this assumption, demonstrating superior results with multitask prompts, particularly in generating coherent text and sentiment analysis, signaling that not all models adhere to a uniform performance pattern. Phi3 Medium 14B exhibited the weakest overall performance, with both single-task and multitask approaches underperforming compared to the other models, but with the single-task approach consistently outperforming the multitask one. This highlights potential limitations in the model’s architecture when handling both simple and complex tasks. Mistral 7B presents a mixed profile, with performance fluctuating between the two prompting approaches depending on the task. While single-task prompts show an advantage in text generation and NER Recall, multitask prompts excel in sentiment analysis and NER Precision, with a notably lower formatting error rate, suggesting that Mistral 7B is more versatile but less predictable. Overall, these experiments underscore the importance of selecting the appropriate prompting strategy based on the specific model and task at hand. While single-task prompts generally offer better performance, certain models like LLama 3.1 8B and Mistral 7B demonstrate the potential of multitask prompts to exceed single-task results in specific contexts. The diverse outcomes across these models suggest that optimizing prompting strategies for Large Language Models should be model-specific and task-aware, rather than guided by a one-size-fits-all approach.

## 5\. Discussion

This study provides an in-depth comparison of single-task and multitask prompting strategies for Large Language Models (LLMs) across five models: Gemma 2 9B, Qwen 2 7B, LLama 3.1 8B, Phi3 Medium 14B, and Mistral 7B. Contrary to the initial hypothesis, the results indicate that single-task prompts do not consistently outperform multitask prompts across all scenarios. The analysis revealed that, while single-task prompts often excel in structured tasks like sentiment analysis and generate higher BLEU scores for review generation, multitask prompts have their own advantages. These include higher precision in named entity recognition (NER) tasks for certain models and a reduced frequency of formatting errors, highlighting the potential of multitask prompts for integrated tasks. This variability underscores the significant impact of model architecture on the effectiveness of prompt strategies.

The findings demonstrate that prompt strategy effectiveness is model-dependent. For instance, Gemma 2 9B performed well with both prompt strategies, showing only minor differences between single-task and multitask approaches. This suggests that more capable models, like Gemma 2 9B, are relatively unaffected by prompt complexity, maintaining stable performance regardless of prompt type. However, for models like Qwen 2 7B and Phi3 Medium 14B, single-task prompts clearly outperformed multitask prompts, particularly in review generation, where BLEU scores were notably higher with single-task prompts. This suggests that models with lower capacity or different architectures might struggle with the complexity introduced by multitask prompts; on the other hand, models such as LLama 3.1 8B and Mistral 7B showed unexpected strengths with multitask prompts. LLama 3.1 8B, in particular, achieved higher BLEU scores and exhibited better sentiment classification accuracy in multitask scenarios compared to single-task ones, suggesting that its architecture might be better suited to handling integrated prompts that require simultaneous consideration of multiple tasks. This is an indication that multitask prompts might enhance contextual understanding in models designed to manage complex dependencies within the text.

Different tasks yielded varying results depending on the prompting strategy. In sentiment analysis, single-task prompts generally offered better performance across most models, leading to higher accuracy scores. This supports the notion that simpler and more focused prompts can enhance performance in tasks that require clear-cut, binary decisions. However, in NER, multitask prompts occasionally demonstrated higher precision, particularly in LLama 3.1 8B and Mistral 7B, suggesting that integrated prompts may help in extracting contextual information relevant to entity recognition. Additionally, the multitask prompt strategy resulted in a lower error rate for JSON formatting across several models, indicating that multitask prompts might provide advantages in tasks requiring consistent output structures. This insight is critical when choosing between single-task and multitask approaches, as the task requirements and desired outcomes must be carefully matched to the strengths of each prompting strategy.

The study’s findings challenge the common assumption that single-task prompts are universally superior due to their simplicity. While they frequently lead to higher precision in certain contexts, multitask prompts have demonstrated advantages in integrating multiple outputs and maintaining structural consistency. This suggests that prompt engineering must be flexible, adapting to both the task’s complexity and the specific architecture of the LLM. Moreover, the results showed no straightforward correlation between model size and prompt effectiveness. Larger models like Phi3 Medium did not always benefit from multitask prompts, while smaller ones like LLama 3.1 8B performed unexpectedly well with integrated tasks. These observations suggest that elements beyond size, such as attention mechanisms and the training dataset’s nature, significantly influence how LLMs respond to various prompt strategies.

This study’s scope is constrained by several factors. The selected models, while diverse, represent a subset of open-weight LLMs, limiting the generalizability of findings to proprietary or cutting-edge models. Additionally, the focus was on a narrow range of NLP tasks—sentiment analysis, NER, and JSON formatting—leaving room for further exploration in more diverse and challenging scenarios like machine translation or complex reasoning tasks. Future research should aim to broaden the scope by incorporating a wider variety of tasks and models, potentially examining how specific architectural elements, such as attention head count or layer depth, influence prompt performance. It would also be valuable to investigate automated prompt optimization methods, such as reinforcement learning, to dynamically adapt prompts to maximize model efficiency. Exploring domain-specific challenges, like legal or medical texts, could provide deeper insights into the applicability of single-task versus multitask strategies in specialized contexts.

From a practical standpoint, the study’s findings provide actionable guidance for developers aiming to optimize LLM interactions. The data underscore the need for a context-sensitive approach to prompt engineering, where prompt choice is not driven by simplicity alone but by a careful assessment of the task’s requirements and the model’s characteristics. Theoretically, this study challenges the dominance of single-task prompts in the field, revealing that effective prompt strategies are highly dependent on the LLM’s architecture and the nature of the task. These findings advocate for a more nuanced approach to prompt design, moving away from one-size-fits-all solutions and towards strategies tailored to the specific context.

Statistical tests corroborated the complexity of LLM responses to different prompt types. For example, non-parametric tests like the Wilcoxon signed-rank test highlighted significant differences in BLEU and NER F1 scores between single-task and multitask prompts. Such results point to deeper, architecture-specific factors influencing prompt effectiveness, suggesting that the interplay between task complexity and model design is more intricate than previously thought. To address this, future research must delve deeper into understanding how LLM architectures process prompts. Greater clarity on the internal workings of LLMs, particularly in how they handle varied prompt structures, will be crucial for developing more reliable AI systems. This is especially relevant in high-stakes domains like healthcare or finance, where transparency and consistency in AI behavior are paramount.

## 6\. Conclusions

This comparative study on the effectiveness of multitask versus single-task prompts for Large Language Models (LLMs) has produced nuanced and unexpected findings, challenging the initial assumption that single-task prompts would consistently outperform multitask ones.

Among the tested models, Gemma 2 9B exhibited the strongest overall performance, showing only a slight preference for single-task prompts. The difference between the two prompting strategies was marginal, with nearly equivalent results in sentiment exact match (91.50% for single-task vs. 90.00% for multitask) and F1 score for entity recognition (55.75% vs. 54.75%). Qwen 2 7B demonstrated a clearer advantage for single-task prompts, particularly in text generation, as evidenced by a higher BLEU score (73.26% vs. 56.09%). However, multitask prompts outperformed in NER precision (32.20% vs. 27.97%), revealing a notable trade-off between precision and recall. LLama 3.1 8B defied expectations by favoring multitask prompts, which yielded higher BLEU scores (88.94% vs. 76.55%) and better sentiment exact match (83.70% vs. 81.00%), suggesting that this model handles multitasking with greater consistency and precision in text generation and sentiment analysis. Conversely, Phi3 Medium 14B showed the weakest overall performance, with a distinct preference for single-task prompts. The disparity was particularly significant in the BLEU score (57.63% for single-task vs. 16.98% for multitask) and in the F1 score for NER (22.62% vs. 11.68%), indicating significant challenges in processing multitask scenarios. Mistral 7B displayed the most variable results. While single-task prompts yielded a better BLEU score (76.41% vs. 70.84%), multitask prompts excelled in sentiment exact match (87.20% vs. 71.80%) and resulted in a notably lower formatting error rate (29.00‰ vs. 155.00‰), indicating its capacity to handle multitasking effectively in some contexts.

These findings highlight the fact that the effectiveness of prompts varies significantly across models. In some cases, such as with LLama 3.1 8B and Mistral 7B, multitask prompts proved to be more effective, challenging the assumption that simplicity in prompting always leads to better outcomes. The analysis also revealed complex trade-offs, particularly in tasks requiring a balance between precision and recall, as observed in NER. This suggests that the choice between single-task and multitask prompts can significantly impact not only overall accuracy but also how well a model handles the nuanced aspects of performance. The practical implications of this study are substantial. It provides concrete guidance on selecting effective prompts for different LLM architectures and applications, emphasizing the need for a nuanced, model-specific approach to prompt design. Furthermore, the results underscore the importance of understanding the underlying factors that drive performance variations. Future research should focus on unpacking these mechanisms to gain a deeper understanding of how model architecture, task characteristics, and prompt complexity interact. This would lay the groundwork for optimizing prompts and refining LLM performance in real-world contexts.

## Author Contributions

Conceptualization, M.G. and F.D.M.; Methodology, M.G.; Software, M.G. and F.D.M.; Validation, M.G. and F.D.M.; Data curation, M.G. and F.D.M.; Writing–original draft, M.G. and F.D.M.; Writing–review and editing, M.G. and F.D.M.; Supervision, M.G. All authors have read and agreed to the published version of the manuscript.

## Funding

This research received no external funding.

## Data Availability Statement

The data supporting the results reported in this study are available online in a publicly accessible GitHub repository. All datasets analyzed or generated during the research can be found at the following link: [https://github.com/gozus19p/Comparative-Analysis-of-Prompt-Strategies-for-LLMs](https://github.com/gozus19p/Comparative-Analysis-of-Prompt-Strategies-for-LLMs) (accessed on 26 November 2024). We encourage further exploration and verification of our findings using these data.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Appendix A

|     |     |
| --- | --- |
| **Listing A1.** Example of a ground truth JSON data. |
| 1 | `{` |
| 2 | `  "review": "But at least this movie got what it deserved - to be sent to the` |
|  | `      ↪ Satellite of Love to be ridiculed on by Mike, Tom Servo, and~Crow T.` |
|  | `      ↪ Robot from Pearl Forrester on \"Mystery Science Theater 3000!\" \"` |
|  | `      ↪ Soultaker\" is one of those long lost, forgotten movies that are so` |
|  | `      ↪ bad you’ll be guaranteed to have nightmares or depression later on in` |
|  | `      ↪ life. Even though the movie is not that old, it’s still a very` |
|  | `      ↪ forgotten type of movie. If~it had never been for the intelligent` |
|  | `      ↪ minds at \"Mystery Science Theater 3000,\" the movie would not only` |
|  | `      ↪ seem like it was never made, but~the movie wouldn’t be very enjoyable` |
|  | `      ↪ by us moviegoers.<br /><br />In real life: this movie is really bad.` |
|  | `      ↪ In~the Satellite of Love: this movie is excellent!",` |
| 3 | `  "sentiment": "negative",` |
| 4 | `  "entities": [` |
| 5 | `    {` |
| 6 | `    "label": "PERSON",` |
| 7 | `    "value": "Mike"` |
| 8 | `    },` |
| 9 | `    {` |
| 10 | `    "label": "PERSON",` |
| 11 | `    "value": "Tom Servo"` |
| 12 | `    },` |
| 13 | `    {` |
| 14 | `    "label": "PERSON",` |
| 15 | `    "value": "Crow T. Robot"` |
| 16 | `    },` |
| 17 | `    {` |
| 18 | `    "label": "ORG",` |
| 19 | `    "value": "Pearl Forrester"` |
| 20 | `    }` |
| 21 | `  ]` |
| 22 | `}` |

## Appendix B

|     |
| --- |
| **Listing A2.** Multitask prompts. |
| `    PROMPT_TEMPLATE = """Instruction: Analyze the following review text` |
| `        ↪ and provide one distinct outputs formatted in JSON:` |
|  |
| `1.  **Sentiment Classification:** Indicate whether the sentiment of the` |
| `    ↪ review is "positive" or "negative".` |
| `2.  **Named Entity Extraction:** List all named entities present in the` |
| `    ↪ text, categorizing them by label (PERSON, ORG, LOC).` |
| `3.  **Required JSON Format:** Ensure the response is formatted in JSON` |
| `    ↪ according to the following schema:` |
|  |
| `{{` |
| `  "sentiment": "<sentiment>",` |
| `  "review": "<review>",` |
| `  "entities": [` |
| `    {{` |
| `      "label": "<label>",` |
| `      "value": "<value>"` |
| `    }}` |
| `  ]` |
| `}}` |
|  |
| `example:` |
|  |
| `"I recently visited the restaurant ’La Dolce Vita’ in Rome and was` |
| `    ↪ thrilled with the service and food. The~waiter, Marco, was` |
| `    ↪ exceptionally friendly and the truffle risotto was simply divine.` |
| `    ↪ I can’t wait to return and recommend this place to my~friends."` |
|  |
| `‘‘‘json` |
| `{{` |
| `  "sentiment": "positive",` |
| `  "review": "I recently visited the restaurant ’La Dolce Vita’ in Rome` |
| `      ↪ and was thrilled with the service and food. The~waiter, Marco,` |
| `      ↪ was exceptionally friendly and the truffle risotto was simply` |
| `      ↪ divine. I can’t wait to return and recommend this place to my` |
| `      ↪ friends.",` |
| `  "entities": [` |
| `    {{` |
| `      "label": "ORG",` |
| `      "value": "La Dolce Vita"` |
| `    }},` |
| `    {{` |
| `      "label": "LOC",` |
| `      "value": "Rome"` |
| `    }},` |
| `    {{` |
| `      "label": "PERSON",` |
| `      "value": "Marco"` |
| `    }}` |
| `  ]` |
| `}}` |
| `‘‘‘` |
|  |
| `{content}"""` |

|     |
| --- |
| **Listing A3.** Single-task prompts. |
| `    NER_PROMPT = """Analyze the following review text listing all named` |
| `        ↪ entities present in the text, categorizing them by label.` |
| `        ↪ Consider only PERSON, ORG, and~LOC categories.` |
| `Ensure the response is formatted in JSON according to the following` |
| `    ↪ schema:` |
|  |
| `[` |
| `  {{` |
| `    "label": "<label>",` |
| `    "value": "<value>"` |
| `  }}` |
| `]` |
|  |
| `Example:` |
|  |
| `"I recently visited the restaurant ’La Dolce Vita’ in Rome and was` |
| `    ↪ thrilled with the service and food. The~waiter, Marco, was` |
| `    ↪ exceptionally friendly and the truffle risotto was simply divine.` |
| `    ↪ I can’t wait to return and recommend this place to my~friends."` |
|  |
| `[` |
| `  {{` |
| `    "label": "ORG",` |
| `    "value": "La Dolce Vita"` |
| `  }},` |
| `  {{` |
| `    "label": "LOC",` |
| `    "value": "Rome"` |
| `  }},` |
| `  {{` |
| `    "label": "PERSON",` |
| `    "value": "Marco"` |
| `  }}` |
| `]` |
|  |
| `{content}"""` |
|  |
| `SENTIMENT_PROMPT = """Analyze the following review text indicating` |
| `    ↪ whether the sentiment of the review is "positive" or~"negative".` |
|  |
| `Example:` |
|  |
| `"I recently visited the restaurant ’La Dolce Vita’ in Rome and was` |
| `    ↪ thrilled with the service and food. The~waiter, Marco, was` |
| `    ↪ exceptionally friendly and the truffle risotto was simply divine.` |
| `    ↪ I can’t wait to return and recommend this place to my~friends."` |
|  |
| `"positive"` |
|  |
| `{content}"""` |
|  |
| `FORMATTING_OUTPUT = """You are given three informations: sentiment,` |
| `    ↪ review and entities. Generate a JSON representation using the` |
| `    ↪ following schema. Use just the data you receive:` |
|  |
| `{{` |
| `  "sentiment": "<sentiment>",` |
| `  "review": "<review>",` |
| `  "entities": [` |
| `    {{` |
| `      "label": "<label>",` |
| `      "value": "<value>"` |
| `    }}` |
| `  ]` |
| `}}` |
|  |
| `example:` |
|  |
| `"Sentiment: positive` |
| `Review: I recently visited the restaurant ’La Dolce Vita’ in Rome and was` |
| `    ↪ thrilled with the service and food. The~waiter, Marco, was` |
| `    ↪ exceptionally friendly and the truffle risotto was simply divine.` |
| `    ↪ I can’t wait to return and recommend this place to my friends.` |
| `Entities: [` |
| `    {{` |
| `      "label": "ORG",` |
| `      "value": "La Dolce Vita"` |
| `    }},` |
| `    {{` |
| `      "label": "LOC",` |
| `      "value": "Rome"` |
| `    }},` |
| `    {{` |
| `      "label": "PERSON",` |
| `      "value": "Marco"` |
| `    }}` |
| `  ]` |
| `}"` |
|  |
| `‘‘‘json` |
| `{{` |
| `  "sentiment": "positive",` |
| `  "review": "I recently visited the restaurant ’La Dolce Vita’ in Rome` |
| `      ↪ and was thrilled with the service and food. The~waiter, Marco,` |
| `      ↪ was exceptionally friendly and the truffle risotto was simply` |
| `      ↪ divine. I can’t wait to return and recommend this place to my` |
| `      ↪ friends.",` |
| `  "entities": [` |
| `    {{` |
| `      "label": "ORG",` |
| `      "value": "La Dolce Vita"` |
| `    }},` |
| `    {{` |
| `      "label": "LOC",` |
| `      "value": "Rome"` |
| `    }},` |
| `    {{` |
| `      "label": "PERSON",` |
| `      "value": "Marco"` |
| `    }}` |
| `  ]` |
| `}}` |
| `‘‘‘` |
|  |
|  |
| `Sentiment: {sentiment}` |
| `Review: {review}` |
| `Entities: {entities}"""` |

## Appendix C

|     |
| --- |
| **Listing A4.** Regular expression to clean JSON-like LLM output. |
| `clean_regex: str = r"(?<!\S)//.*?$"` |

|     |
| --- |
| **Listing A5.** Regular expression to extract JSON-like LLM output. |
| `extract_regex: str = r"(\{.*\})"` |

|     |
| --- |
| **Listing A6.** JSON output parsing algorithm. |
| `def parse(string: str) -> dict:` |
| `dictionary: dict = None` |
| `try:` |
| `dictionary = json.loads(string)` |
| `except Exception:` |
| `pass` |
| `try:` |
| `dictionary = eval(string)` |
| `except Exception:` |
| `pass` |
| `return dictionary` |

## References

01. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention Is All You Need. arXiv **2017**, arXiv:1706.03762. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Attention+Is+All+You+Need&author=Vaswani,+A.&author=Shazeer,+N.&author=Parmar,+N.&author=Uszkoreit,+J.&author=Jones,+L.&author=Gomez,+A.N.&author=Kaiser,+L.&author=Polosukhin,+I.&publication_year=2017&journal=arXiv&doi=10.48550/arXiv.1706.03762)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.1706.03762)\]
02. Kojima, T.; Gu, S.; Reid, M.; Matsuo, Y.; Iwasawa, Y. Large Language Models Are Zero-Shot Reasoners. 2022. Available online: [https://www.semanticscholar.org/paper/Large-Language-Models-are-Zero-Shot-Reasoners-Kojima-Gu/e7ad08848d5d7c5c47673ffe0da06af443643bda](https://www.semanticscholar.org/paper/Large-Language-Models-are-Zero-Shot-Reasoners-Kojima-Gu/e7ad08848d5d7c5c47673ffe0da06af443643bda) (accessed on 26 November 2024).
03. Li, Y. A Practical Survey on Zero-Shot Prompt Design for In-Context Learning. arXiv **2023**, arXiv:2309.13205. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Practical+Survey+on+Zero-Shot+Prompt+Design+for+In-Context+Learning&author=Li,+Y.&publication_year=2023&journal=arXiv&doi=10.26615/978-954-452-092-2_069)\] \[ [CrossRef](https://doi.org/10.26615/978-954-452-092-2_069)\]
04. White, J.; Fu, Q.; Hays, S.; Sandborn, M.; Olea, C.; Gilbert, H.; Elnashar, A.; Spencer-Smith, J.; Schmidt, D.C. A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. arXiv **2023**, arXiv:2302.11382. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Prompt+Pattern+Catalog+to+Enhance+Prompt+Engineering+with+ChatGPT&author=White,+J.&author=Fu,+Q.&author=Hays,+S.&author=Sandborn,+M.&author=Olea,+C.&author=Gilbert,+H.&author=Elnashar,+A.&author=Spencer-Smith,+J.&author=Schmidt,+D.C.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2302.11382)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2302.11382)\]
05. Sivarajkumar, S.; Kelley, M.; Samolyk-Mazzanti, A.; Visweswaran, S.; Wang, Y. An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing. arXiv **2023**, arXiv:2309.08008. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=An+Empirical+Evaluation+of+Prompting+Strategies+for+Large+Language+Models+in+Zero-Shot+Clinical+Natural+Language+Processing&author=Sivarajkumar,+S.&author=Kelley,+M.&author=Samolyk-Mazzanti,+A.&author=Visweswaran,+S.&author=Wang,+Y.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2309.08008)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2309.08008)\]
06. Sahoo, P.; Singh, A.K.; Saha, S.; Jain, V.; Mondal, S.; Chadha, A. A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications. arXiv **2024**, arXiv:2402.07927. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Systematic+Survey+of+Prompt+Engineering+in+Large+Language+Models:+Techniques+and+Applications&author=Sahoo,+P.&author=Singh,+A.K.&author=Saha,+S.&author=Jain,+V.&author=Mondal,+S.&author=Chadha,+A.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2402.07927)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2402.07927)\]
07. Joaquin, A.S.; Haroen, A. Understanding How Model Size Affects Few-shot Instruction Prompting. arXiv **2022**, arXiv:2212.01907. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Understanding+How+Model+Size+Affects+Few-shot+Instruction+Prompting&author=Joaquin,+A.S.&author=Haroen,+A.&publication_year=2022&journal=arXiv&doi=10.48550/arXiv.2212.01907)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2212.01907)\]
08. Yousri, R.; Safwat, S. How Big Can It Get? A comparative analysis of LLMs in architecture and scaling. In Proceedings of the 2023 International Conference on Computer and Applications, Cairo, Egypt, 28–30 November 2023. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=How+Big+Can+It+Get?+A+comparative+analysis+of+LLMs+in+architecture+and+scaling&conference=Proceedings+of+the+2023+International+Conference+on+Computer+and+Applications&author=Yousri,+R.&author=Safwat,+S.&publication_year=2023&doi=10.1109/ICCA59364.2023.10401818)\] \[ [CrossRef](https://doi.org/10.1109/ICCA59364.2023.10401818)\]
09. Linzbach, S.; Tressel, T.; Kallmeyer, L.; Dietze, S.; Jabeen, H. Decoding Prompt Syntax: Analysing its Impact on Knowledge Retrieval in Large Language Models. In Proceedings of the Companion Proceedings of the ACM Web Conference, Austin, TX, USA, 30 April–4 May 2023. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Decoding+Prompt+Syntax:+Analysing+its+Impact+on+Knowledge+Retrieval+in+Large+Language+Models&conference=Proceedings+of+the+Companion+Proceedings+of+the+ACM+Web+Conference&author=Linzbach,+S.&author=Tressel,+T.&author=Kallmeyer,+L.&author=Dietze,+S.&author=Jabeen,+H.&publication_year=2023&doi=10.1145/3543873.3587655)\] \[ [CrossRef](https://doi.org/10.1145/3543873.3587655)\]
10. Sclar, M.; Choi, Y.; Tsvetkov, Y.; Suhr, A. Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting. arXiv **2023**, arXiv:2310.11324. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Quantifying+Language+Models%E2%80%99+Sensitivity+to+Spurious+Features+in+Prompt+Design+or:+How+I+learned+to+start+worrying+about+prompt+formatting&author=Sclar,+M.&author=Choi,+Y.&author=Tsvetkov,+Y.&author=Suhr,+A.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2310.11324)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2310.11324)\]
11. Lakshmipathi, N. IMDB Dataset of 50K Movie Reviews. 2019. Available online: [https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) (accessed on 26 November 2024).
12. Shelar, H.; Kaur, G.; Heda, N.; Agrawal, P. Named Entity Recognition Approaches and Their Comparison for Custom NER Model. Sci. Technol. Libr. **2020**, 39, 324–337. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Named+Entity+Recognition+Approaches+and+Their+Comparison+for+Custom+NER+Model&author=Shelar,+H.&author=Kaur,+G.&author=Heda,+N.&author=Agrawal,+P.&publication_year=2020&journal=Sci.+Technol.+Libr.&volume=39&pages=324%E2%80%93337&doi=10.1080/0194262X.2020.1759479)\] \[ [CrossRef](https://doi.org/10.1080/0194262X.2020.1759479)\]
13. Gozzi, M.; Maio, F.D. Comparative Analysis of Prompt Strategies for LLMs: Single-Task vs. Multitasking Prompts. 2024. Available online: [https://github.com/gozus19p/llm-benchmark](https://github.com/gozus19p/llm-benchmark) (accessed on 26 November 2024).
14. Liesenfeld, A.; Dingemanse, M. Rethink. Open Source Gener. AI: Open Washing EU AI Act. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency, Rio de Janeiro, Brazil, 3–6 June 2024; pp. 1774–1787. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Rethink.+Open+Source+Gener.+AI:+Open+Washing+EU+AI+Act&conference=Proceedings+of+the+2024+ACM+Conference+on+Fairness,+Accountability,+and+Transparency&author=Liesenfeld,+A.&author=Dingemanse,+M.&publication_year=2024&pages=1774%E2%80%931787&doi=10.1145/3630106.3659005)\] \[ [CrossRef](https://doi.org/10.1145/3630106.3659005)\]
15. Fourrier, C.; Habib, N.; Lozovskaya, A.; Szafer, K.; Wolf, T. Open LLM Leaderboard v2. Published by Hugging Face. 2024. Available online: [https://huggingface.co/spaces/open-llm-leaderboard/open\_llm\_leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) (accessed on 15 June 2024).
16. Gao, L.; Tow, J.; Biderman, S.; Black, S.; DiPofi, A.; Foster, C.; Golding, L.; Hsu, J.; McDonell, K.; Muennighoff, N.; et al. A Framework for Few-Shot Language Model Evaluation. Zenodo, 2021, v0.0.1. Available online: [https://zenodo.org/records/14216804](https://zenodo.org/records/14216804) (accessed on 26 November 2024).
17. Zhou, J.; Lu, T.; Mishra, S.; Brahma, S.; Basu, S.; Luan, Y.; Zhou, D.; Hou, L. Instruction-Following Evaluation for Large Language Models. arXiv **2023**, arXiv:2311.07911. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Instruction-Following+Evaluation+for+Large+Language+Models&author=Zhou,+J.&author=Lu,+T.&author=Mishra,+S.&author=Brahma,+S.&author=Basu,+S.&author=Luan,+Y.&author=Zhou,+D.&author=Hou,+L.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2311.07911)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2311.07911)\]
18. Suzgun, M.; Scales, N.; Schärli, N.; Gehrmann, S.; Tay, Y.; Chung, H.W.; Chowdhery, A.; Le, Q.V.; Chi, E.H.; Zhou, D.; et al. Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them. arXiv **2022**, arXiv:2210.09261. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Challenging+BIG-Bench+Tasks+and+Whether+Chain-of-Thought+Can+Solve+Them&author=Suzgun,+M.&author=Scales,+N.&author=Sch%C3%A4rli,+N.&author=Gehrmann,+S.&author=Tay,+Y.&author=Chung,+H.W.&author=Chowdhery,+A.&author=Le,+Q.V.&author=Chi,+E.H.&author=Zhou,+D.&author=et+al.&publication_year=2022&journal=arXiv&doi=10.48550/arXiv.2210.09261)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2210.09261)\]
19. Hendrycks, D.; Burns, C.; Kadavath, S.; Arora, A.; Basart, S.; Tang, E.; Song, D.; Steinhardt, J. Measuring Mathematical Problem Solving With the MATH Dataset. arXiv **2021**, arXiv:2103.03874. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Measuring+Mathematical+Problem+Solving+With+the+MATH+Dataset&author=Hendrycks,+D.&author=Burns,+C.&author=Kadavath,+S.&author=Arora,+A.&author=Basart,+S.&author=Tang,+E.&author=Song,+D.&author=Steinhardt,+J.&publication_year=2021&journal=arXiv&doi=10.48550/arXiv.2103.03874)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2103.03874)\]
20. Rein, D.; Hou, B.L.; Stickland, A.C.; Petty, J.; Pang, R.Y.; Dirani, J.; Michael, J.; Bowman, S.R. GPQA: A Graduate-Level Google-Proof Q&A Benchmark. arXiv **2023**, arXiv:2311.12022. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=GPQA:+A+Graduate-Level+Google-Proof+Q%2526A+Benchmark&author=Rein,+D.&author=Hou,+B.L.&author=Stickland,+A.C.&author=Petty,+J.&author=Pang,+R.Y.&author=Dirani,+J.&author=Michael,+J.&author=Bowman,+S.R.&publication_year=2023&journal=arXiv&doi=10.48550/arXiv.2311.12022)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2311.12022)\]
21. Sprague, Z.; Ye, X.; Bostrom, K.; Chaudhuri, S.; Durrett, G. MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning. arXiv **2024**, arXiv:2310.16049. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=MuSR:+Testing+the+Limits+of+Chain-of-thought+with+Multistep+Soft+Reasoning&author=Sprague,+Z.&author=Ye,+X.&author=Bostrom,+K.&author=Chaudhuri,+S.&author=Durrett,+G.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2310.16049)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2310.16049)\]
22. Wang, Y.; Ma, X.; Zhang, G.; Ni, Y.; Chandra, A.; Guo, S.; Ren, W.; Arulraj, A.; He, X.; Jiang, Z.; et al. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark. arXiv **2024**, arXiv:2406.01574. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=MMLU-Pro:+A+More+Robust+and+Challenging+Multi-Task+Language+Understanding+Benchmark&author=Wang,+Y.&author=Ma,+X.&author=Zhang,+G.&author=Ni,+Y.&author=Chandra,+A.&author=Guo,+S.&author=Ren,+W.&author=Arulraj,+A.&author=He,+X.&author=Jiang,+Z.&author=et+al.&publication_year=2024&journal=arXiv&doi=10.48550/arXiv.2406.01574)\] \[ [CrossRef](https://doi.org/10.48550/arXiv.2406.01574)\]
23. Beeching, E.; Fourrier, C.; Habib, N.; Han, S.; Lambert, N.; Rajani, N.; Sanseviero, O.; Tunstall, L.; Wolf, T. Open LLM Leaderboard (2023–2024). Published by Hugging Face. 2023. Available online: [https://huggingface.co/spaces/open-llm-leaderboard-old/open\_llm\_leaderboard](https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard) (accessed on 15 June 2024).

**Figure 1.**
Flow chart that describes the experiment workflow.

**Figure 1.**
Flow chart that describes the experiment workflow.

**Figure 2.**
UML activity diagram representing the single-task prompts’ execution workflow.

**Figure 2.**
UML activity diagram representing the single-task prompts’ execution workflow.

**Figure 3.**
UML activity diagram representing the multitask prompt’s execution workflow.

**Figure 3.**
UML activity diagram representing the multitask prompt’s execution workflow.

**Figure 4.**
Flow chart that describes the Ollama inference pipeline.

**Figure 4.**
Flow chart that describes the Ollama inference pipeline.

**Table 1.**
A single row of the dataset (review text has been truncated to enhance readability).

**Table 1.**
A single row of the dataset (review text has been truncated to enhance readability).

| Review | Sentiment | Entities | Json |
| :-- | :-: | :-- | :-- |
| 1st watched 2/9/2008, 4 out of 10 (Dir-J.S. Cardone [...] ) | negative | [‘label’: ‘ORG’, ‘value’: ‘qwest‘, ‘label’: ‘ORG’, ‘value’: ‘qwest’] | {“review”: “1st watched 2/9/2008, 4 out of 10 (Dir-J.S. Cardone [...] ” , “sentiment”: “negative”, ”entities”: [{“label”: “ORG”, “value”: “qwest”}, {“label”: “ORG”, “value”: “qwest”}]} |

**Table 2.**
Performance scores of different models with single-task and multitask approaches across metrics.

**Table 2.**
Performance scores of different models with single-task and multitask approaches across metrics.

| Model | F1-Score NER | Sentiment Score | Review BLEU | Score |
| :-- | :-: | :-: | :-: | :-: |
|  | **Single** | **Multi** | **Single** | **Multi** | **Single** | **Multi** | **Single** | **Multi** |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Gemma2 9B | 55.75% | 54.74% | 91.50% | 90.00% | 96.70% | 97.49% | 81.32% | 80.74% |
| Qwen2 7B | 26.98% | 25.13% | 82.70% | 80.80% | 73.26% | 56.09% | 60.98% | 54.01% |
| LLama 3.1 8B | 44.10% | 43.00% | 81.00% | 83.70% | 76.55% | 88.94% | 67.21% | 71.88% |
| Phi3 Medium | 22.62% | 11.68% | 50.80% | 48.30% | 57.63% | 16.98% | 43.68% | 25.65% |
| Mistral 7B | 32.56% | 30.60% | 71.80% | 87.20% | 76.41% | 70.84% | 60.26% | 62.88% |

**Table 3.**
Shapiro–Wilk test p-values were measured for each model to test if the distributions are normal.

**Table 3.**
Shapiro–Wilk test p-values were measured for each model to test if the distributions are normal.

| Model | F1-Score NER | Review BLEU | Sentiment Score | Score |
| :-- | :-: | :-: | :-: | :-: |
|  | **Single** | **Multi** | **Single** | **Multi** | **Single** | **Multi** | **Single** | **Multi** |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Gemma2 9B | 5.66×10−26 | 3.85×10−26 | 5.90×10−52 | 3.87×10−53 | 1.96×10−51 | 1.08×10−50 | 1.11×10−27 | 2.63×10−27 |
| Qwen2 7B | 1.56×10−31 | 2.12×10−34 | 3.02×10−41 | 3.52×10−36 | 1.25×10−47 | 5.96×10−47 | 1.99×10−26 | 5.47×10−15 |
| LLama 3.1 8B | 4.72×10−26 | 3.91×10−26 | 3.09×10−44 | 7.98×10−49 | 5.08×10−47 | 5.29×10−48 | 3.78×10−30 | 7.45×10−32 |
| Phi3 Medium | 1.07×10−36 | 6.03×10−47 | 9.12×10−39 | 4.25×10−46 | 1.36×10−41 | 1.32×10−41 | 5.22×10−28 | 8.91×10−33 |
| Mistral 7B | 8.20×10−30 | 7.08×10−36 | 1.06×10−42 | 6.29×10−38 | 2.66×10−44 | 2.02×10−49 | 9.74×10−30 | 3.22×10−18 |

**Table 4.**
The p-values for different models using various evaluation metrics.

**Table 4.**
The p-values for different models using various evaluation metrics.

| Metric (p-Value) | Gemma 2 9B | Qwen 2 7B | LLama 3.1 8B | Phi 3 Medium | Mistral 7B |
| :-- | :-: | :-: | :-: | :-: | :-: |
| NER F1 Wilcoxon | 0.02 | 0.01 | 0.06 | 6.96×10−16 | 0.02 |
| Review BLEU Wilcoxon | 0.01 | 1.58×10−28 | 9.06×10−10 | 6.98×10−63 | 2.45×10−7 |
| Sentiment Score McNemar | 0.03 | 0.13 | 0.06 | 0.29 | 8.93×10−27 |
| Score Wilcoxon | 0.03 | 1.14×10−18 | 1.54×10−5 | 1.30×10−29 | 0.60 |

**Table 5.**
Summary of Friedman test results for different metrics and prompting conditions.

**Table 5.**
Summary of Friedman test results for different metrics and prompting conditions.

| Metric | Single-Task | Multitask |
| :-- | :-: | :-: |
| F1-Score (NER) | Statistic = 1.03×103 | Statistic = 1.05×103 |
|  | p-value = 7.49×10−222 | p-value = 3.29×10−226 |
| BLEU Score | Statistic = 1.00×103 | Statistic = 1.97×103 |
|  | p-value = 1.21×10−215 | p-value = 0.0 |
| Sentiment Score | Statistic = 6.55×102 | Statistic = 7.93×102 |
|  | p-value = 1.73×10−140 | p-value = 2.87×10−170 |
| Overall Score | Statistic = 1.31×103 | Statistic = 1.81×103 |
|  | p-value = 1.69×10−282 | p-value = 0.0 |

**Table 6.**
Specific-task performances on Gemma 2 9B.

**Table 6.**
Specific-task performances on Gemma 2 9B.

| Metric | Multitask | Single-Task |
| :-- | :-: | :-: |
| Mean BLEU on review | 97.49% | 96.70% |
| Mean Exact-Match on sentiment | 90.00% | 91.50% |
| Mean NER F1 | 54.75% | 55.75% |
| Mean NER Precision | 60.99% | 59.86% |
| Mean NER Recall | 54.11% | 56.87% |
| Formatting error rate | 9.00‰ | 8.00‰ |

**Table 7.**
Specific-task performances on Qwen 2 7B.

**Table 7.**
Specific-task performances on Qwen 2 7B.

| Metric | Multitask | Single-Task |
| :-- | :-: | :-: |
| Mean BLEU on review | 56.09% | 73.26% |
| Mean Exact-Match on sentiment | 80.80% | 82.70% |
| Mean NER F1 | 25.13% | 26.98% |
| Mean NER Precision | 32.20% | 27.97% |
| Mean NER Recall | 24.32% | 30.79% |
| Formatting error rate | 34.00‰ | 88.00‰ |

**Table 8.**
Specific-task performances on LLama 3.1 8B.

**Table 8.**
Specific-task performances on LLama 3.1 8B.

| Metric | Multitask | Single-Task |
| :-- | :-: | :-: |
| Mean BLEU on review | 88.94% | 76.55% |
| Mean Exact-Match on sentiment | 83.70% | 81.00% |
| Mean NER F1 | 43.00% | 44.10% |
| Mean NER Precision | 50.25% | 47.98% |
| Mean NER Recall | 42.05% | 46.01% |
| Formatting error rate | 69.00‰ | 94.00‰ |

**Table 9.**
Specific-task performances on Phi 3 Medium.

**Table 9.**
Specific-task performances on Phi 3 Medium.

| Metric | Multitask | Single-Task |
| :-- | :-: | :-: |
| Mean BLEU on review | 16.98% | 57.63% |
| Mean Exact-Match on sentiment | 48.30% | 50.80% |
| Mean NER F1 | 11.68% | 22.62% |
| Mean NER Precision | 14.49% | 25.45% |
| Mean NER Recall | 11.06% | 23.78% |
| Formatting error rate | 253.00‰ | 307.00‰ |

**Table 10.**
Specific-task performances on Mistral 7B.

**Table 10.**
Specific-task performances on Mistral 7B.

| Metric | Multitask | Single-Task |
| :-- | :-: | :-: |
| Mean BLEU on review | 70.84% | 76.41% |
| Mean Exact-Match on sentiment | 87.20% | 71.80% |
| Mean NER F1 | 30.60% | 32.56% |
| Mean NER Precision | 39.28% | 37.05% |
| Mean NER Recall | 28.04% | 33.50% |
| Formatting error rate | 29.00‰ | 155.00‰ |

|     |     |
| --- | --- |
|  | **Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. |

© 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ( [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="llm-api-resilience-in-production-rate-limits-failover-and-th.md">
<details>
<summary>LLM API Resilience in Production: Rate Limits, Failover, and the Hidden Costs of Naive Retry Logic</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://tianpan.co/blog/2026-03-11-llm-api-resilience-production>

# LLM API Resilience in Production: Rate Limits, Failover, and the Hidden Costs of Naive Retry Logic

In mid-2025, a team building a multi-agent financial assistant discovered their API spend had climbed from $127/week to $47,000/week. An agent loop — Agent A asked Agent B for clarification, Agent B asked Agent B back, and so on — had been running recursively for eleven days. No circuit breaker caught it. No spend alert fired in time. The retry logic dutifully kept retrying each timeout, compounding the runaway cost at every step.

This is not a story about model quality. It is a story about distributed systems engineering — specifically, about the parts of it that most LLM application developers skip because they assume the provider handles it.

They do not.

LLM API providers operate at roughly 99.0–99.5% uptime. That sounds fine until you convert it: 99% uptime means 3.5 days of downtime per year. By contrast, big-three cloud providers average 99.97% uptime — about 2.5 hours per year. That is a 6–14x difference in downtime exposure, and it is not improving quickly. API uptime across the LLM industry fell from 99.66% to 99.46% between Q1 2024 and Q1 2025 — 60% more downtime year-over-year, as demand growth outpaced infrastructure scaling.

If you are calling an LLM API from a production system and your resilience strategy is "retry on error," you have already made several expensive assumptions that will eventually be wrong.

## Why Retry Logic Is Where Good Intentions Die

The single most common resilience mistake in LLM applications is not the absence of retries — it is retries without jitter, without layering discipline, and without a budget.

When a rate limit or timeout occurs, a naively implemented retry loop fires again immediately. This hammers the same already-overloaded endpoint, exhausts the retry budget within milliseconds, and produces no recovery window. Worse, in systems with multiple service layers, the amplification compounds. Three retries at each layer of a five-service call chain produce 3^5 = 243 backend calls for each original user request. This is the canonical retry storm: the original problem was minor; the retry behavior made it fatal. About 40% of cascading failures in distributed systems trace back to retry logic.

The fix is not "remove retries." Retries are essential. The fix is three-part:

**Use full jitter, not none.** Pure exponential backoff without jitter synchronizes all clients to retry at the same moment, recreating the thundering herd on every attempt. Full jitter spreads retries: `sleep = random_between(0, min(cap, base * 2^attempt))`. Starting values that work: attempt 1 waits up to 1s, attempt 2 up to 2–3s, attempt 3 up to 4–6s, cap at 32–60s with a maximum of 3–5 attempts.

**Retry only at one layer.** If your application calls a service that calls another service, retries at every hop multiply. Pick one layer — usually the outermost application layer — and make it the only place retries happen. Internal layers should propagate failures cleanly.

**Implement a retry budget.** Set a global constraint: total retries should not exceed 10% of total requests at any given time. If your retry rate exceeds the budget, fail fast. This prevents one degraded endpoint from pulling down everything else.

One more thing: never retry 4xx errors blindly. A 400 or 403 will fail every time regardless of how many times you retry it. The only 4xx worth retrying is 429 (rate limit), and even then, read the `retry-after` header before choosing a wait duration. If the provider tells you the exact reset time, use it rather than guessing.

## TPM vs. RPM: You Are Probably Only Handling One

LLM rate limits operate on two independent axes simultaneously, and most teams only think about one of them.

**RPM (requests per minute)** limits the number of API calls. It protects infrastructure from request floods. **TPM (tokens per minute)** limits compute consumption. It protects GPU capacity from workloads with long prompts or extensive agent chains. You can stay within RPM while blowing past TPM, and vice versa. Both will produce a 429, but the underlying cause and the right response differ.

For agents and RAG pipelines, TPM is almost always the binding constraint. A pipeline that retrieves 20 documents and stuffs them into a 15,000-token prompt burns TPM at roughly 15x the rate of a short-form query, even at the same request count.

Production-grade token management requires:

- **Pre-request estimation** using a tokenizer (`tiktoken` for OpenAI, provider-specific equivalents elsewhere) to reject or queue requests before they blow the budget.
- **Always setting `max_tokens`** to cap output. Without this, a model that decides to write an unusually thorough response can silently exhaust your TPM budget on a single request.
- **Dual rate limiting at the application layer**, not just at the provider edge. Enforce both RPM and TPM limits in your own code, with a queue that smooths burst traffic using Redis or Kafka rather than shedding it.

Azure deployments add another dimension: per-instance limits and shared regional caps are independent. A deployment with five Azure instances each configured for 450K TPM on GPT-4o may still hit a region-wide limit that caps all instances combined at 300K TPM. This is not documented prominently and is typically discovered under load.

## Circuit Breakers: The Mechanism That Separates Graceful Degradation from Self-Inflicted Collapse

A circuit breaker sits between your application and the LLM provider. In normal operation (closed state), all requests pass through. When the failure rate exceeds a threshold over a rolling window — say, more than 20% of requests fail over the last 60 seconds — the circuit trips open. In the open state, requests fail immediately without touching the provider, giving the provider time to recover. After a cooldown period, the circuit enters half-open state and allows a small fraction of test traffic through to probe whether recovery has occurred.

The concrete production impact is significant. For an application making 100 requests per minute during a five-minute outage:

- **Without a circuit breaker**: 500–1,000 requests hang for 30 seconds each waiting for timeouts. Users experience degraded responses throughout the outage.
- **With a circuit breaker**: after roughly 10–15 failed requests trip the threshold, the remaining ~485 requests fail fast in under 10ms. Fallback logic engages immediately. Users see a 200ms response from the secondary provider rather than a 30-second timeout.

Mean time to detection drops from 30 minutes to 2 minutes with circuit breaker telemetry, because the circuit state is an explicit signal that something is wrong.

For LLM applications, standard HTTP circuit breaker triggers — error rate, consecutive failures, latency P95 — are necessary but not sufficient. Add:

- **Cost per request exceeding a threshold**: the $47,000/week runaway agent mentioned at the top would have been caught by a circuit breaker configured to open when cost per conversation exceeds $X.
- **Conversation turn count**: break circuits at 20+ turns in an agentic conversation. Legitimate reasoning chains rarely need more; runaway loops almost always need more.
- **Output quality score falling below threshold**: requires a lightweight LLM-as-judge running on outputs before they reach the user.

## Multi-Provider Failover Is No Longer Optional

By mid-2025, 40% of production LLM teams had multi-provider routing in place, up from 23% just ten months earlier. The main forcing function was a series of notable provider outages — including multi-hour incidents at both major foundation model providers — that left single-provider applications completely dark while multi-provider applications failed over in seconds.

The failure modes are predictable: a rate-limit storm on one provider, a 10-hour inference infrastructure outage at another, silent quality degradation that HTTP success rates cannot detect. None of these affect providers uniformly at the same time. Routing across providers converts single-provider outages into brief blips.

There are two failover architectures worth knowing:

**Sequential failover**: primary → secondary → tertiary. Simple to implement. The cost is ~1–3 seconds of additional latency per hop, which is often acceptable for non-interactive workloads.

**Parallel hedging**: fire requests to primary and secondary simultaneously; use whichever responds first; cancel the other. Eliminates the latency penalty of sequential failover but roughly doubles token cost. Reserve this for interactive use cases where first-token latency is the primary SLO.

The engineering challenges of multi-provider routing are underappreciated:

- Every provider has different error formats, rate-limit headers, and response schemas. A library like LiteLLM normalizes these, but at ~2,000 RPS LiteLLM's memory usage climbs past 8 GB. Higher-throughput environments need purpose-built gateways (Portkey, Bifrost in Go, or Bedrock for AWS-native stacks).
- Fallback models may produce structurally different outputs. Falling back from one model to another during an outage can break downstream JSON parsers if the models format responses differently.
- Cost can spike dramatically during failover. If your primary provider is the cheapest option and failover routes to a more expensive provider, a 10-hour outage during peak traffic can generate significant unexpected cost.

## Silent Degradation Is the Failure Mode You Are Not Monitoring For

In August 2025, an LLM provider published a postmortem documenting three simultaneous bugs that had been degrading response quality for weeks. None of them were hard errors. HTTP success rates looked normal throughout. The failures:

- A load balancing change caused requests to be routed to servers configured for a different context window size. At peak, 16% of requests on one model were affected.
- A TPU configuration error caused high probability weight to be assigned to rare tokens, producing responses in the wrong language intermittently.
- A compiler arithmetic mismatch caused the highest-probability token to "sometimes disappear from consideration entirely" — producing technically plausible but factually wrong outputs.

Standard uptime monitoring caught none of these. They were detected via user complaints and manual investigation.

This is the category of failure that is hardest to defend against and most consequential for applications where output correctness matters. The monitoring requirements are different from what most teams have in place:

- **Output schema validation**: if your application expects structured JSON, validate the schema on every response. Schema failures are a leading indicator of model regression.
- **LLM-as-judge on a sample**: run a small percentage of responses through a lightweight quality assessment. A drop in quality scores before a drop in HTTP success rates is a valuable early warning signal.
- **Embedding drift on outputs**: track the semantic distribution of responses over time. Sudden drift in output embeddings — even when outputs are syntactically valid — indicates something changed upstream.

None of these are expensive to implement. All of them would have caught the August 2025 bugs faster than waiting for user complaints.

## Putting It Together: A Minimum Viable Resilience Stack

The full picture: an LLM call in a production system should pass through a request queue that enforces dual TPM/RPM limits, then through a circuit breaker with error-rate and cost-threshold triggers, then to a gateway that handles exponential backoff with full jitter and can route to a secondary provider on 429s, 5xxs, or latency threshold breaches. Outputs should be schema-validated before returning to the application, with a percentage sample sent to a quality monitor.

This is not exotic infrastructure. It is the same distributed systems engineering that makes HTTP microservices reliable — applied to a new category of external dependency that happens to be slower, more expensive per call, and more likely to silently degrade than most services engineers have worked with before.

The teams that have built this are the ones whose applications kept serving users during every major provider outage in 2025 and 2026. The teams that have not built it are the ones writing incident postmortems about why their application was down for ten hours when the provider was down for ten hours.

The provider outage is not optional. The circuit breaker is.

**References:**

- [https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- [https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- [https://portkey.ai/blog/failover-routing-strategies-for-llms-in-production/](https://portkey.ai/blog/failover-routing-strategies-for-llms-in-production/)
- [https://portkey.ai/blog/rate-limiting-for-llm-applications/](https://portkey.ai/blog/rate-limiting-for-llm-applications/)
- [https://portkey.ai/blog/retries-fallbacks-and-circuit-breakers-in-llm-apps/](https://portkey.ai/blog/retries-fallbacks-and-circuit-breakers-in-llm-apps/)
- [https://www.sitepoint.com/claude-api-circuit-breaker-pattern/](https://www.sitepoint.com/claude-api-circuit-breaker-pattern/)
- [https://www.zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025](https://www.zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025)
- [https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues)
- [https://medium.com/google-cloud/building-bulletproof-llm-applications-a-guide-to-applying-sre-best-practices-1564b72fd22e](https://medium.com/google-cloud/building-bulletproof-llm-applications-a-guide-to-applying-sre-best-practices-1564b72fd22e)
- [https://learn.microsoft.com/en-us/azure/architecture/antipatterns/retry-storm/](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/retry-storm/)
- [https://cookbook.openai.com/examples/how\_to\_handle\_rate\_limits](https://cookbook.openai.com/examples/how_to_handle_rate_limits)
- [https://www.runtime.news/as-ai-adoption-surges-ai-uptime-remains-a-big-problem/](https://www.runtime.news/as-ai-adoption-surges-ai-uptime-remains-a-big-problem/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="llmops-in-production-457-case-studies-of-what-actually-works.md">
<details>
<summary>LLMOps in Production: 457 Case Studies of What Actually Works</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works>

[Blog](https://www.zenml.io/blog)/LLMOps in Production: 457 Case Studies of What Actually Works

[LLMOps](https://www.zenml.io/category/llmops)·January 20, 2025·45 minutes

# LLMOps in Production: 457 Case Studies of What Actually Works

A comprehensive overview of lessons learned from the world's largest database of LLMOps case studies (457 entries as of January 2025), examining how companies implement and deploy LLMs in production. Through nine thematic blog posts covering everything from RAG implementations to security concerns, this article synthesizes key patterns and anti-patterns in production GenAI deployments, offering practical insights for technical teams building LLM-powered applications.

![Alex Strick van Linschoten](https://assets.zenml.io/webflow/64a817a2e7e2208272d1ce30/9804d473/652948c72d87d2e2afebb29b_alex.jpg)[Alex Strick van Linschoten](https://www.zenml.io/author/alex-strick-van-linschoten)

![LLMOps in Production: 457 Case Studies of What Actually Works](https://assets.zenml.io/webflow/64a817a2e7e2208272d1ce30/742cd02e/6981d352ce4b26d085d7041b_6981d2b7cbabf896f02b0c37_Midjourney_Technical_Blueprint.avif)

Throughout 2024, we collated [a huge database of real-world LLMOps and GenAI case studies](https://www.zenml.io/llmops-database), examining how companies actually implement and deploy large language models in production. Starting with around 300 entries and growing to 457 case studies by January 2025, [this collection](https://www.zenml.io/llmops-database) represents over 600,000 words of technical implementation details, architectural decisions, and practical problem-solving approaches. To help practitioners navigate this wealth of information, we created a comprehensive series of thematic deep dives, each accompanied by an in-depth podcast episode powered by Google’s NotebookLM.

Our journey began with “ [Demystifying LLMOps](https://www.zenml.io/blog/demystifying-llmops-a-practical-database-of-real-world-generative-ai-implementations)”, providing an essential overview of our database’s methodology and structure, offering a practical starting point for those venturing into production LLM deployments. This foundation was expanded in “ [LLMOps Lessons Learned](https://www.zenml.io/blog/llmops-lessons-learned-navigating-the-wild-west-of-production-llms)”, which synthesized insights from our first 380 case studies to paint a broad picture of the current LLMOps landscape.

The technical series started with “ [Building LLM Applications That Know What They’re Talking About](https://www.zenml.io/blog/building-llm-applications-that-know-what-theyre-talking-about)”, exploring the crucial role of Retrieval-Augmented Generation (RAG) in creating knowledge-aware applications. This was followed by “ [Building Advanced Search, Retrieval, and Recommendation Systems with LLMs](https://www.zenml.io/blog/building-advanced-search-retrieval-and-recommendation-systems-with-llms)”, which explored the practical challenges and solutions in implementing embedding-based search systems.

For those interested in automation and orchestration, “ [LLM Agents in Production](https://www.zenml.io/blog/llm-agents-in-production-architectures-challenges-and-best-practices)” offered a pragmatic examination of real-world agent deployments, while “ [Prompt Engineering and Management in Production](https://www.zenml.io/blog/prompt-engineering-management-in-production-practical-lessons-from-the-llmops-database)” tackled the often-overlooked challenges of maintaining and scaling prompt infrastructure. Our “ [Evaluation Playbook](https://www.zenml.io/blog/the-evaluation-playbook-making-llms-production-ready)” provided a comprehensive look at how organizations measure and improve their LLM applications’ performance.

The series concluded with two crucial operational aspects: “ [Optimizing LLM Performance and Cost](https://www.zenml.io/blog/optimizing-llm-performance-and-cost-squeezing-every-drop-of-value)”, which examined the practical trade-offs in scaling LLM infrastructure, and “ [Production LLM Security](https://www.zenml.io/blog/production-llm-security-real-world-strategies-from-industry-leaders)”, offering essential insights into protecting LLM applications against emerging threats.

Each blog post distilled key patterns and anti-patterns from our database of case studies, providing actionable insights for practitioners at every stage of their LLMOps journey. Given the extensive scope of the database, we’ve created these high-level summaries to offer another way to explore the wealth of implementation details and lessons learned.

What follows are summaries of the summaries, which is to say high-level summaries of the key parts of each case study, from the problems that companies faced to the solutions they tried out. This is a long blog post but it’s rewarding just to scroll through and see what jumps out for you.

Going forward, we’ll continue to expand the database with new technical write-ups and panel discussions as they emerge. We’re also planning regular thematic deep-dives that explore specific aspects of AI Engineering and production GenAI deployments, helping practitioners stay current with evolving best practices and emerging patterns.

Here are the case study summaries:

- [**A bank**](https://www.zenml.io/llmops-database/challenges-in-building-enterprise-chatbots-with-llms-a-banking-case-study) \- A bank’s attempt to build a customer support chatbot using GPT-4 and RAG revealed the complexities of deploying LLMs in production, highlighting challenges in domain knowledge management, retrieval optimization, conversation flow design, and state management, with production issues including latency and regulatory compliance. The project, initially planned as a three-month proof of concept, underscores the need for robust infrastructure, comprehensive planning, and ongoing maintenance in LLMOps projects.
- [**A major gaming company**](https://www.zenml.io/llmops-database/fine-tuning-llms-for-toxic-speech-classification-in-gaming) \- A major gaming company collaborated with AWS Professional Services to build an automated toxic speech detection system by fine-tuning LLMs, starting with a small dataset and moving from a two-stage to a single-stage model, achieving 88% precision and 83% recall while reducing complexity and costs.
- [**A technology company**](https://www.zenml.io/llmops-database/scaling-and-optimizing-self-hosted-llms-for-developer-documentation) \- A technology company improved developer documentation accessibility by deploying a self-hosted LLM solution using RAG, with guard rails for content safety and topic validation. They optimized performance using vLLM for faster inference and Ray Serve for horizontal scaling, achieving significant improvements in latency and throughput while maintaining cost efficiency, and ensuring proprietary information remained secure.
- [**Aachen Uniklinik**](https://www.zenml.io/llmops-database/natural-language-interface-for-healthcare-data-analytics-using-llms) \- A UK-based NLQ company collaborated with Aachen Uniklinik to develop a natural language interface for healthcare data analytics, allowing medical professionals to query complex patient data using natural language. The system employs a hybrid architecture, combining vector databases for semantic search, a fine-tuned LLM for intent detection and query transformation, and traditional SQL for structured data access, addressing challenges like handling “dirty data” and medical terminology complexity.
- [**Accenture**](https://www.zenml.io/llmops-database/enterprise-knowledge-base-assistant-using-multi-model-genai-architecture) \- Accenture’s Knowledge Assist utilizes a multi-model GenAI architecture on AWS, combining Anthropic’s Claude-2, Amazon Titan, Pinecone, and Kendra, to provide a scalable enterprise knowledge solution, resulting in a 50% reduction in new hire training time and a 40% drop in query escalations. The system demonstrates mature LLMOps practices with real-time processing, robust monitoring, and multi-language support.
- [**Accenture**](https://www.zenml.io/llmops-database/implementing-generative-ai-in-manufacturing-a-multi-use-case-study) \- Accenture’s Industry X division implemented generative AI across manufacturing, validating nine use cases including operations twins and technical documentation automation, achieving 40-50% effort reduction in some areas. Their approach emphasized multi-agent architectures, human-in-the-loop workflows, and the use of domain-specific data for successful deployments.
- [**Accenture / Databricks**](https://www.zenml.io/llmops-database/specialized-language-models-for-contact-center-transformation) \- Accenture and Databricks partnered to deploy specialized language models (SLMs) for a client’s contact center, moving beyond basic prompt engineering by using Databricks’ MLOps platform and GPU infrastructure to create fine-tuned models that understand industry-specific context, cultural nuances, and brand styles, resulting in improved customer experience and operational efficiency. The solution includes real-time monitoring, multimodal capabilities, and advanced security, demonstrating a sophisticated approach to AI-driven customer service.
- [**Accolade**](https://www.zenml.io/llmops-database/enhancing-healthcare-service-delivery-with-rag-and-llm-powered-search) \- Accolade, a healthcare provider, addressed fragmented data by implementing a RAG system using Databricks’ DBRX model, improving information retrieval and customer service through a unified data lakehouse and real-time data ingestion, while maintaining HIPAA compliance. This setup, deployed via Databricks Model Serving, demonstrates a practical approach to LLM implementation in a regulated industry, emphasizing data governance, security, and compliance.
- [**Activeloop**](https://www.zenml.io/llmops-database/enterprise-grade-memory-agents-for-patent-processing-with-deep-lake) \- Activeloop leveraged its Deep Lake vector database to build an enterprise-grade memory agent system for patent processing, handling 600,000 new patents annually and managing 80 million total. The system uses specialized AI agents for tasks like claim search and abstract generation, reducing patent generation time and improving information retrieval accuracy by 5-10% using their Deep Memory technology.
- [**Acxiom**](https://www.zenml.io/llmops-database/llm-observability-for-enhanced-audience-segmentation-systems) \- Acxiom leveraged LLMs and LangChain to create an audience segmentation system, but faced challenges in debugging complex workflows. By implementing LangSmith for observability, they gained visibility into multi-agent interactions, optimized token usage, and scaled their hybrid model deployment effectively.
- [**Addverb**](https://www.zenml.io/llmops-database/multi-lingual-voice-control-system-for-agv-management-using-edge-llms) \- Addverb has developed a multi-lingual voice control system for managing AGV fleets, utilizing edge-deployed Llama 3 for low-latency processing and cloud-based ChatGPT for complex tasks; this allows warehouse workers to use natural language commands in 98 languages to control AGVs, improving operational efficiency and reducing reliance on specialized engineers.
- [**ADP**](https://www.zenml.io/llmops-database/building-an-enterprise-wide-generative-ai-platform-for-hr-and-payroll-services) \- ADP is developing “ADP Assist,” a generative AI platform to enhance user interaction across their HR, payroll, and workforce management tools, leveraging a “One AI” and “One Data” platform with Databricks for MLOps, vector search, and data governance. Their approach emphasizes quality assurance through robust testing and RAG implementation, while also addressing critical concerns around data security, cost optimization, and scalability for their global operations serving over 41 million workers.
- [**Adyen**](https://www.zenml.io/llmops-database/smart-ticket-routing-and-support-agent-copilot-using-llms) \- Adyen, a global fintech platform, enhanced its support operations by deploying a smart ticket routing system and a support agent copilot, both powered by LLMs and built using LangChain on Kubernetes. This resulted in improved ticket routing accuracy and faster response times through automated document retrieval and answer suggestions, while maintaining the flexibility to switch between different LLM models.
- [**Agmatix**](https://www.zenml.io/llmops-database/generative-ai-assistant-for-agricultural-field-trial-analysis) \- Agmatix developed Leafy, a generative AI assistant powered by Amazon Bedrock and the Anthropic Claude model, to streamline agricultural field trial analysis, enabling agronomists to query data using natural language and automatically generate visualizations, resulting in a 20% efficiency improvement, 25% better data integrity, and a tripling of analysis throughput. The system leverages AWS services for data pipeline management and provides a natural language interface for querying complex agricultural research data.
- [**AI Hero / Outer Bounds**](https://www.zenml.io/llmops-database/kubernetes-as-a-platform-for-llm-operations-practical-experiences-and-trade-offs) \- A panel of industry experts explored the use of Kubernetes for LLM operations, discussing its strengths in workload orchestration and vendor agnosticism, while also addressing challenges like GPU management and container size limitations. The discussion emphasized the need for tailored abstractions and optimizations when deploying LLMs on Kubernetes, covering key areas such as cost optimization and architectural patterns.
- [**Aiera**](https://www.zenml.io/llmops-database/building-and-evaluating-a-financial-earnings-call-summarization-system) \- Aiera, a financial intelligence platform, developed an automated earnings call summarization system using Anthropic’s Claude models, focusing on extracting key financial insights. Their rigorous evaluation process compared ROUGE and BERTScore metrics, revealing the trade-offs in scoring methodologies and the challenges of assessing generative AI outputs in production, ultimately selecting Claude 3.5 Sonnet as the best performer.
- [**Aimpoint Digital**](https://www.zenml.io/llmops-database/ai-agent-system-for-automated-travel-itinerary-generation) \- Aimpoint Digital built an AI agent system for automated travel itinerary generation, utilizing a multi-RAG architecture with parallel processing for places, restaurants, and events, and Databricks Vector Search for scalable data retrieval. The system employs LLM-as-judge for automated evaluation, alongside retrieval metrics and DSPy for prompt optimization, ensuring personalized itineraries are generated quickly and accurately.
- [**AirBnB**](https://www.zenml.io/llmops-database/evolving-a-conversational-ai-platform-for-production-llm-applications) \- AirBnB upgraded their conversational AI platform to a hybrid system, integrating LLMs for enhanced natural language understanding while retaining traditional workflows for sensitive operations. Their new platform features Chain of Thought reasoning, robust context management, and a comprehensive guardrails framework, demonstrating a pragmatic approach to production LLM deployment.
- [**Airbnb**](https://www.zenml.io/llmops-database/llm-integration-for-customer-support-automation-and-enhancement) \- Airbnb enhanced its customer support using LLMs for content recommendation, real-time agent assistance, and chatbot paraphrasing, moving from classification to prompt-based generation with encoder-decoder architectures. They used DeepSpeed for efficient training, implemented data cleaning pipelines, and focused on prompt engineering to improve content relevance, agent efficiency, and user engagement.
- [**Airtop**](https://www.zenml.io/llmops-database/building-and-debugging-web-automation-agents-with-langchain-ecosystem) \- Airtop utilized the LangChain ecosystem to develop a web automation platform, enabling AI agents to interact with websites using natural language, featuring modular architecture for easy LLM switching and LangGraph for building scalable agents with built-in validation. The platform includes an Extract API for data retrieval and an Act API for real-time interactions, with LangSmith providing debugging and testing capabilities to ensure production reliability.
- [**Airtrain / Healthcare company / E-commerce unicorn**](https://www.zenml.io/llmops-database/cost-reduction-through-fine-tuning-healthcare-chatbot-and-e-commerce-product-classification) \- Airtrain’s case studies demonstrate the cost-effectiveness of fine-tuning smaller LLMs for production, with a healthcare company achieving performance parity with GPT-3.5 for a patient intake chatbot by fine-tuning Mistral-7B, and an e-commerce company improving product classification accuracy from 47% to 94% while cutting costs by 94% compared to GPT-4. These examples highlight that fine-tuning can deliver significant cost savings without sacrificing performance, provided there is high-quality training data and clear evaluation metrics.
- [**Alaska Airlines**](https://www.zenml.io/llmops-database/ai-powered-natural-language-flight-search-implementation) \- Alaska Airlines utilized Google Cloud’s Gemini models to develop a natural language flight search, enabling customers to describe their travel needs conversationally, rather than using traditional search parameters. This system integrates Gemini with real-time flight data, customer profiles, and pricing systems, supporting complex queries and providing accurate, personalized recommendations, all while prioritizing factuality and user experience.
- [**Alaska Airlines / Bitra**](https://www.zenml.io/llmops-database/llm-testing-framework-using-llms-as-quality-assurance-agents) \- Alaska Airlines, in partnership with Bitra, developed QARL, a novel testing framework that uses LLMs to evaluate other LLMs in production by simulating various user interactions and evaluating responses for safety and business alignment. This approach allows for automated adversarial testing of customer-facing chatbots, identifying potential risks and unwanted behaviors before deployment.
- [**Allianz Benelux**](https://www.zenml.io/llmops-database/ai-powered-insurance-claims-chatbot-with-continuous-feedback-loop) \- Allianz Benelux implemented an AI-powered chatbot using Landbot to streamline their insurance claims process, analyzing over 92,000 unique search terms and integrating a real-time feedback loop with Slack and Trello for rapid iteration, achieving a 90% positive feedback rating across 18,000+ customer interactions. This resulted in a simplified claims process and improved operational efficiency.
- [**Allianz Direct**](https://www.zenml.io/llmops-database/rag-powered-agent-assist-tool-for-insurance-contact-centers) \- Allianz Direct utilized Databricks’ Mosaic AI to create a RAG-based agent assist tool, improving answer accuracy by 10-15% by providing agents with quick access to policy information, while also adhering to strict financial industry compliance through Unity Catalog for data governance. This allowed agents to focus on customer relationships rather than searching through documentation.
- [**Altana**](https://www.zenml.io/llmops-database/supply-chain-intelligence-platform-using-compound-ai-systems) \- Altana, a supply chain intelligence company, utilizes a “compound AI systems” approach, integrating custom deep learning models, fine-tuned LLMs, and RAG workflows, all managed through Databricks Mosaic AI. This sophisticated LLMOps infrastructure enables them to automate complex tasks like tax classification and legal write-ups, while ensuring data privacy and achieving a 20x speedup in model deployment and a 20-50% performance boost.
- [**Amazon**](https://www.zenml.io/llmops-database/scaling-rag-accuracy-from-49-to-86-in-finance-q-a-assistant) \- Amazon Finance Automation implemented a RAG-based Q&A system using Amazon Bedrock, achieving a significant accuracy increase from 49% to 86% by iteratively improving document chunking, prompt engineering, and embedding model selection, demonstrating a systematic approach to LLM optimization. This resulted in a substantial reduction in customer query response times, showcasing the practical application of LLMOps best practices in a finance setting.
- [**Amazon**](https://www.zenml.io/llmops-database/building-a-commonsense-knowledge-graph-for-e-commerce-product-recommendations) \- Amazon’s COSMO framework employs LLMs to construct a commonsense knowledge graph, enhancing product recommendations by extracting relationships from customer data, refining them with human and ML filters, and integrating the graph into recommendation models, achieving a 60% performance improvement. This demonstrates a robust LLMOps pipeline for production use.
- [**Amazon Alexa**](https://www.zenml.io/llmops-database/managing-model-updates-and-robustness-in-production-voice-assistants) \- Amazon Alexa’s NLP team focused on maintaining consistent performance during model updates and handling input variations in their production voice assistant. They used positive congruent training to preserve correct predictions from previous models and T5 models to generate synthetic data, improving the model’s robustness to slight changes in phrasing.
- [**Amazon Pharmacy**](https://www.zenml.io/llmops-database/hipaa-compliant-llm-based-chatbot-for-pharmacy-customer-service) \- Amazon Pharmacy deployed a HIPAA-compliant, LLM-powered chatbot using a Retrieval Augmented Generation (RAG) pattern with SageMaker JumpStart foundation models to provide customer service agents with quick access to accurate pharmacy information. The system incorporates a feedback loop for continuous improvement, while maintaining strict security and compliance through network isolation and role-based access control.
- [**AngelList**](https://www.zenml.io/llmops-database/llm-powered-investment-document-analysis-and-processing) \- AngelList replaced their initial AWS Comprehend-based document processing with OpenAI models, leading to the development of Relay, a system that automates the extraction of key investment data with 99% accuracy using LangChain for prompt orchestration and a multi-API approach for redundancy. This transition significantly reduced manual processing overhead and improved accuracy.
- [**Anthem Blue Cross**](https://www.zenml.io/llmops-database/building-an-on-premise-health-insurance-appeals-generation-system) \- An on-premise LLM system was built to generate health insurance appeals, using fine-tuned models trained on medical review board data and synthetic data, deployed on personal hardware with Kubernetes. The system includes GPU inference, a Django frontend, and a redundant network setup, addressing challenges like GPU optimization and hardware reliability.
- [**Anthropic**](https://www.zenml.io/llmops-database/building-a-privacy-preserving-llm-usage-analytics-system-clio) \- Anthropic developed Clio, a privacy-preserving system that uses their LLM Claude to analyze and cluster user conversations, extracting high-level insights without exposing raw data. This allows them to improve safety, understand usage patterns, and detect misuse while maintaining strong privacy through techniques like minimum cluster sizes and privacy auditing.
- [**Anthropic**](https://www.zenml.io/llmops-database/privacy-preserving-llm-usage-analysis-system-for-production-ai-safety) \- Anthropic developed Clio, an automated system powered by Claude, to analyze production usage of their Claude language models while preserving user privacy. Clio extracts metadata, performs semantic clustering, and generates cluster descriptions to identify usage patterns and potential misuse, improving safety classifiers by identifying both false positives and negatives.
- [**Anthropic / Amazon**](https://www.zenml.io/llmops-database/multilingual-document-processing-pipeline-with-human-in-the-loop-validation) \- This case study outlines a production-ready multilingual document processing pipeline that uses Anthropic’s Claude models via Amazon Bedrock, combined with human-in-the-loop validation using Amazon A2I, and a custom ReactJS UI. The system leverages a multi-stage AWS Step Functions pipeline, the Rhubarb framework for document understanding, and emphasizes structured output using JSON schemas, comprehensive state tracking with DynamoDB, and serverless architecture for scalability.
- [**Anthropic / OpenAI**](https://www.zenml.io/llmops-database/medical-transcript-summarization-using-multiple-llm-models-an-evaluation-study) \- A study evaluated Claude, GPT-4, LLaMA, and Pi 3.1 for medical transcript summarization, finding GPT-4 achieved the highest accuracy while Pi 3.1 balanced accuracy and conciseness, with results suggesting a potential to reduce care coordinator preparation time by over 50%. The research used over 5,000 medical transcripts and compared model performance using ROUGE scores and cosine similarity.
- [**Anzen**](https://www.zenml.io/llmops-database/building-robust-legal-document-processing-applications-with-llms) \- Anzen utilizes a multi-model approach, combining specialized models for document structure with LLMs for content understanding, to build a robust legal document processing system, achieving 99.9% accuracy in document classification. Their solution incorporates comprehensive monitoring, feedback, and fine-tuned classification models, demonstrating practical techniques for managing LLM hallucinations and building production-grade systems in high-stakes environments.
- [**Anzen**](https://www.zenml.io/llmops-database/using-llms-to-scale-insurance-operations-at-a-small-company) \- Anzen, a small insurance company, implemented LLMs to automate their underwriting process using BERT for document classification and AWS Textract for information extraction, achieving 95% accuracy, and also built a compliance document review system using sentence embeddings and question-answering models to provide rapid feedback on legal documents. This allowed them to compete with larger insurers by streamlining key operations.
- [**AppFolio**](https://www.zenml.io/llmops-database/building-a-property-management-ai-copilot-with-langgraph-and-langsmith) \- AppFolio developed Realm-X Assistant, a property management AI copilot, using LangGraph for complex workflow management and LangSmith for monitoring and debugging, achieving a significant performance boost in text-to-data functionality from 40% to 80% through dynamic few-shot prompting and saving users over 10 hours per week. The system incorporates robust testing, evaluation, and CI/CD pipelines, demonstrating a mature approach to LLMOps.
- [**Applaud**](https://www.zenml.io/llmops-database/lessons-from-deploying-an-hr-aware-ai-assistant-five-key-implementation-insights) \- Applaud, an HR tech company, successfully deployed an HR-focused AI assistant, addressing challenges like content management with selective integration and building a context-aware engine, while also innovating with a novel testing approach and implementing temperature controls for accuracy; the deployment emphasized integration with existing HR systems and clear communication about the AI’s capabilities, resulting in improved HR service delivery and a framework for continuous optimization.
- [**Arcade AI**](https://www.zenml.io/llmops-database/building-a-tool-calling-platform-for-llm-agents) \- Arcade AI has developed a tool calling platform to address the challenges of deploying LLM agents in production, providing a dedicated runtime for tools, separate from orchestration, and a robust authentication system with secure token management. The platform includes a Tool SDK for standardized development, an engine for serving APIs, and an actor system for scalable tool execution, along with built-in monitoring and evaluation capabilities.
- [**Ask-a-Metric**](https://www.zenml.io/llmops-database/optimizing-text-to-sql-pipeline-using-agent-experiments) \- Ask-a-Metric, a WhatsApp-based AI data analyst, refined its natural language to SQL query system by experimenting with an agent-based approach using CrewAI, ultimately implementing an optimized hybrid pipeline that achieved high accuracy with significantly reduced query response times and costs. The case study highlights the value of using agent experiments to inform the design of a production system, demonstrating how a hybrid approach can combine the benefits of different architectures.
- [**Assembled**](https://www.zenml.io/llmops-database/automating-test-generation-with-llms-at-scale) \- Assembled, a customer support solutions company, automated their test generation process using LLMs, reducing test writing time from hours to minutes and saving hundreds of engineering hours. By integrating high-quality models and structured prompts into their workflow, they achieved increased test coverage and improved code quality, while maintaining a focus on manual verification and iterative refinement.
- [**Athena Intelligence**](https://www.zenml.io/llmops-database/optimizing-research-report-generation-with-langchain-stack-and-llm-observability) \- Athena Intelligence developed Olympus, an AI-powered platform for generating enterprise research reports, leveraging LangChain for model abstraction and tool integration, LangGraph for orchestrating complex multi-agent workflows, and LangSmith for development and production monitoring. This stack enabled them to handle complex data tasks, generate high-quality reports with accurate source citations, and achieve significant improvements in development speed and system reliability.
- [**Austrian Post Group IT**](https://www.zenml.io/llmops-database/llm-based-agents-for-user-story-quality-enhancement-in-agile-development) \- Austrian Post Group IT developed an Autonomous LLM-based Agent System (ALAS) using GPT-3.5-turbo-16k and GPT-4 to enhance user story quality in agile development, employing specialized agents for Product Owner and Requirements Engineer roles. The system improved story clarity and completeness, addressing challenges like token limits through prompt optimization and manual validation, and was validated by 11 professionals across six agile teams.
- [**AWS / Metaflow**](https://www.zenml.io/llmops-database/aws-trainium-metaflow-democratizing-large-scale-ml-training-through-infrastructure-evolution) \- AWS Trainium and Metaflow are democratizing large-scale ML training by integrating purpose-built hardware with modern MLOps frameworks, enabling teams to achieve enterprise-grade infrastructure without deep distributed systems expertise. This combination results in significant cost reductions, simplified deployment, and the ability to scale from small experiments to massive distributed training with minimal code changes.
- [**AWS GenAIIC**](https://www.zenml.io/llmops-database/optimizing-rag-systems-lessons-from-production) \- AWS GenAIIC shares practical lessons from building production RAG systems, detailing their use of OpenSearch Serverless for vector search and Amazon Bedrock for custom pipelines, emphasizing retrieval optimization through hybrid search, metadata enhancement, and query rewriting, alongside chunking strategies and advanced features like custom embedding training and response quality control. The case study highlights performance optimization, scalability, and reliability mechanisms, demonstrating improved retrieval accuracy, response quality, and user trust.
- [**AWS GenAIIC**](https://www.zenml.io/llmops-database/building-production-grade-heterogeneous-rag-systems) \- AWS GenAIIC demonstrates building production RAG systems that handle heterogeneous data, using routers to direct queries, LLMs for code generation on structured data, and multimodal approaches for images; the system uses OpenSearch for vector storage and k-NN search, with modular design and robust error handling. The case study highlights practical implementations across multiple industries, focusing on managing latency, data quality, and scalability.
- [**Babbel**](https://www.zenml.io/llmops-database/building-an-ai-assisted-content-creation-platform-for-language-learning) \- Babbel leveraged Python, LangChain, and OpenAI GPT models to create an AI-assisted content creation platform, deployed on AWS, that significantly reduces the time required to produce language learning materials. The platform, featuring a Gradio-based UI, manages prompts, generates diverse content formats, and integrates human feedback loops, achieving over 85% acceptance rate from editors.
- [**Bank of America / NVIDIA / Microsoft / IBM**](https://www.zenml.io/llmops-database/blueprint-for-scalable-and-reliable-enterprise-llm-systems) \- A panel of experts from Bank of America, NVIDIA, Microsoft, and IBM discussed the implementation of LLM systems in enterprise environments, emphasizing the need for clear business metrics, robust data governance, and continuous monitoring. The discussion highlighted the differences between traditional MLOps and LLMOps, focusing on testing, evaluation, and the increasing importance of retrieval accuracy and agent-based workflows.
- [**Barclays**](https://www.zenml.io/llmops-database/mlops-evolution-and-llm-integration-at-a-major-bank) \- Barclays is adapting its MLOps infrastructure to integrate LLMs, using a hybrid approach that combines traditional ML with GenAI, emphasizing open-source tools and interoperability. Their strategy includes vector databases for RAG, new metrics for LLM monitoring, and a strong focus on regulatory compliance, all while maintaining a clear focus on business value and ROI.
- [**BenchSci**](https://www.zenml.io/llmops-database/domain-specific-llms-for-drug-discovery-biomarker-identification) \- BenchSci utilizes domain-specific LLMs and a RAG architecture, integrating their biomedical knowledge base with Google’s Med-PaLM, to accelerate drug discovery, specifically in biomarker identification, achieving a 40% increase in scientist productivity and reducing processing times from months to days. The platform emphasizes scientific accuracy through continuous validation and addresses enterprise-level security and compliance requirements.
- [**Bito**](https://www.zenml.io/llmops-database/multi-model-llm-orchestration-with-rate-limit-management) \- Bito, an AI coding assistant, built a multi-LLM orchestration system to handle API rate limits and ensure high availability, intelligently routing requests across providers like OpenAI, Anthropic, and Azure, while selecting models based on context size, cost, and performance. They also use sophisticated prompt engineering for security and accuracy, prioritizing local code processing to maintain user privacy.
- [**Block / Databricks**](https://www.zenml.io/llmops-database/building-production-grade-generative-ai-applications-with-comprehensive-llmops) \- Block (Square) deployed a comprehensive LLMOps strategy across its business units, utilizing a decoupled vector search, an AI Gateway for model management, and robust quality assurance. Built on Databricks, their architecture enabled them to scale to hundreds of production endpoints while maintaining operational control, cost-effectiveness, and security.
- [**Blueprint AI**](https://www.zenml.io/llmops-database/automated-software-development-insights-and-communication-platform) \- Blueprint AI leverages GPT-4 to create a platform that bridges communication gaps between business and technical teams by automatically analyzing data from development tools like GitHub and Jira to generate intelligent reports, track progress, and identify potential blockers, while also focusing on performance optimization through streaming responses and caching. The platform provides 24/7 monitoring and context-aware updates, aiming to keep teams informed without manual reporting overhead.
- [**BNY Mellon**](https://www.zenml.io/llmops-database/enterprise-wide-virtual-assistant-for-employee-knowledge-access) \- BNY Mellon deployed an enterprise-wide virtual assistant powered by Vertex AI, enabling 50,000 employees to access internal knowledge and policies, overcoming challenges in document processing and context-aware information delivery. The solution, which started with pilot programs, now handles diverse information requests, improving information accessibility and streamlining knowledge management practices across the organization.
- [**Bosch**](https://www.zenml.io/llmops-database/enterprise-wide-generative-ai-implementation-for-marketing-content-generation-and-translation) \- Bosch, a global enterprise, deployed “Gen Playground,” a centralized generative AI platform, to streamline marketing content creation and translation across its vast digital ecosystem, enabling 430,000+ employees to generate text and images, and perform translations, significantly reducing content creation time and costs while maintaining brand consistency. This implementation, leveraging Google Cloud services and custom models, focused on practical business use cases and user empowerment, demonstrating a pragmatic approach to enterprise AI deployment.
- [**Box / Glean / Tyace / Security AI / Citibank**](https://www.zenml.io/llmops-database/enterprise-llm-implementation-panel-lessons-from-box-glean-tyace-security-ai-and-citibank) \- A panel of leaders from Box, Glean, Tyace, Security AI, and Citibank discussed their experiences implementing LLMs in production, covering challenges like data integration, security, and cost. The discussion highlighted different use cases, including content management, enterprise search, personalized content generation, and enterprise-wide AI deployment, while emphasizing the importance of data governance and a systematic approach to scaling LLMs.
- [**BQA**](https://www.zenml.io/llmops-database/intelligent-document-processing-for-education-quality-assessment-reports) \- BQA in Bahrain implemented a production LLM system using Amazon Bedrock and other AWS services to automate the analysis of education quality assessment reports, employing a dual-model approach with Meta Llama for summarization and Amazon Titan Express for evaluation, achieving 70% accuracy in generating standards-compliant reports and reducing evidence analysis time by 30%. The system uses an event-driven architecture with SQS queues and Lambda functions for scalable document processing.
- [**Bud Financial / Scotts Miracle-Gro**](https://www.zenml.io/llmops-database/building-personalized-financial-and-gardening-experiences-with-llms) \- Bud Financial and Scotts Miracle-Gro are using Google Cloud’s AI to create personalized experiences, with Bud Financial building a conversational AI for banking using Vertex AI and GKE, and Scotts Miracle-Gro developing “MyScotty,” an AI assistant for gardening advice leveraging Vertex AI Search and multimodal inputs. Both companies prioritize rigorous testing, continuous monitoring, and seamless integration with Google Cloud services to deliver accurate and relevant responses.
- [**Build Great AI**](https://www.zenml.io/llmops-database/llm-powered-3d-model-generation-for-3d-printing) \- Build Great AI has developed a system that uses multiple LLMs, including LLaMA, GPT-4, and Claude, to generate 3D printable models from text descriptions, outputting OpenSCAD code that is converted to STL files; this approach achieves a 60x speed improvement in prototyping compared to manual CAD work, while addressing LLM spatial reasoning limitations through multiple simultaneous generations and iterative refinement.
- [**BuzzFeed**](https://www.zenml.io/llmops-database/production-ready-llm-integration-using-retrieval-augmented-generation-and-custom-react-implementation) \- BuzzFeed Tech successfully integrated LLMs into their content platform by moving from basic ChatGPT implementations to a custom retrieval-augmented generation system, addressing limitations in dataset recency and context window constraints by developing a “native ReAct” implementation and enhancing their vector search architecture with Pinecone, resulting in a more controlled, cost-efficient, and production-ready LLM system.
- [**Cambrium**](https://www.zenml.io/llmops-database/llms-and-protein-engineering-building-a-sustainable-materials-platform) \- Cambrium is using LLMs and AI to design novel proteins for sustainable materials, starting with vegan human collagen for cosmetics. They’ve developed a protein programming language and leveraged LLMs to transform protein design into a mathematical optimization problem, enabling them to efficiently search through massive protein sequence spaces.
- [**Canva**](https://www.zenml.io/llmops-database/systematic-llm-evaluation-framework-for-content-generation) \- Canva developed a systematic LLM evaluation framework for its Magic Switch feature, focusing on defining success criteria and measurable metrics before implementation. This framework uses both rule-based and LLM-based evaluators to assess content quality across dimensions like information preservation, intent alignment, and format, incorporating regression testing to ensure prompt improvements don’t degrade overall quality.
- [**Canva**](https://www.zenml.io/llmops-database/llm-feature-extraction-for-content-categorization-and-search-query-understanding) \- Canva utilized LLMs for feature extraction to categorize user search queries and group content pages semantically, replacing traditional ML classifiers. This resulted in improved accuracy, reduced development time, and lower operational costs, while also simplifying the feature extraction process for content categorization.
- [**Canva**](https://www.zenml.io/llmops-database/automating-post-incident-review-summaries-with-gpt-4) \- Canva automated their Post Incident Review (PIR) summarization process using GPT-4, extracting data from Confluence, preprocessing it, and then using a structured prompt to generate concise summaries, which are then integrated with their data warehouse and Jira, improving data consistency and reducing engineering workload. The solution proved effective, with most AI-generated summaries requiring no human modification, while maintaining high quality and consistency at a cost of $0.6 per summary.
- [**Cedars Sinai**](https://www.zenml.io/llmops-database/ai-powered-neurosurgery-from-brain-tumor-classification-to-surgical-planning) \- Cedars Sinai has implemented a range of AI-powered tools in production for neurosurgery, including a CNN-based brain tumor classification system achieving 95%+ accuracy, a graph neural network for hematoma management with 80%+ accuracy, and AI-driven surgical planning and intraoperative guidance systems, demonstrating real-time processing and integration with existing medical infrastructure. These implementations showcase the use of multiple model types and address challenges like data limitations, regulatory compliance, and clinical workflow integration.
- [**Chaos Labs**](https://www.zenml.io/llmops-database/multi-agent-system-for-prediction-market-resolution-using-langchain-and-langgraph) \- Chaos Labs’ Edge AI Oracle uses LangChain and LangGraph to create a multi-agent system for resolving prediction market queries, employing a decentralized network of AI agents powered by multiple LLMs to ensure objective and accurate resolutions. The system features a sophisticated workflow with specialized agents, providing transparent, traceable results with configurable consensus requirements.
- [**Character.ai**](https://www.zenml.io/llmops-database/scaling-a-high-traffic-llm-chat-application-to-30-000-messages-per-second) \- [Character.ai](http://character.ai/) scaled their conversational AI platform to 30,000 messages per second by building custom foundation models and implementing multi-query attention for GPU cache reduction, while also developing a sophisticated GPU caching system and a prompt management system called “prompt-poet”. This case study highlights the need for innovative solutions across the entire stack, including database optimization, and comprehensive monitoring and testing when running LLMs at scale.
- [**Checkr**](https://www.zenml.io/llmops-database/streamlining-background-check-classification-with-fine-tuned-small-language-models) \- Checkr leveraged a fine-tuned Llama-3-8b-instruct model on Predibase to classify complex background check records, achieving 90% accuracy on challenging cases, a 5x cost reduction, and a 30x speedup compared to their initial GPT-4 implementation. Their journey highlights the effectiveness of fine-tuned smaller models and the importance of monitoring, metrics, and efficient serving techniques like LoRA for production LLM deployments.
- [**Chevron Phillips Chemical**](https://www.zenml.io/llmops-database/strategic-llm-implementation-in-chemical-manufacturing-with-focus-on-documentation-and-virtual-agents) \- Chevron Phillips Chemical is strategically deploying LLMs for virtual agents and document processing, emphasizing a measured approach with a cross-functional team to address challenges like testing and bias. They are focusing on specific use cases, such as extracting data from unstructured documents and creating topic-specific virtual agents, while implementing a robust governance framework.
- [**CircleCI**](https://www.zenml.io/llmops-database/building-and-testing-production-ai-applications-at-circleci) \- CircleCI shares their experience building and deploying AI-powered features, like an error summarizer, detailing the challenges of testing LLM-based applications with non-deterministic outputs and subjective evaluations, and how they addressed these with model-graded evaluations, robust error handling, and user feedback loops. They emphasize the need for new testing strategies beyond simple string matching, while also focusing on cost optimization and scaling considerations.
- [**CircleCI**](https://www.zenml.io/llmops-database/ai-error-summarizer-implementation-a-tiger-team-approach) \- CircleCI formed a tiger team to explore AI integration, resulting in an AI error summarizer feature, using existing foundation models, LangChain, and OpenAI APIs. The team prioritized rapid prototyping and API-first integration, demonstrating that valuable AI features can be achieved through focused exploration and iterative development without the need for complex custom models.
- [**Circuitry.ai**](https://www.zenml.io/llmops-database/rag-powered-decision-intelligence-platform-for-manufacturing-knowledge-management) \- [Circuitry.ai](http://circuitry.ai/) developed a RAG-powered decision intelligence platform for manufacturers, using Delta Lake and Unity Catalog on Databricks for data management and governance, and Llama and DBRX models for response generation, achieving a 60-70% reduction in information search time. Their implementation highlights the importance of robust data management, flexible model architecture, and continuous feedback loops in enterprise LLM deployments.
- [**Cisco**](https://www.zenml.io/llmops-database/enterprise-llmops-development-operations-and-security-framework) \- Cisco developed a comprehensive LLMOps framework to manage the complexities of deploying LLMs at scale, adapting traditional DevOps practices to address the unique challenges of AI-powered applications, with a focus on continuous delivery, robust monitoring, stringent security, and specialized operational support. This framework highlights the need for enterprise-specific considerations like scalability, integration with existing systems, and governance to ensure the successful and secure implementation of LLMs.
- [**Cleric AI**](https://www.zenml.io/llmops-database/ai-sre-system-with-continuous-learning-for-production-issue-investigation) \- Cleric AI’s AI-powered SRE system automates production issue investigation by integrating with existing observability tools, using a concurrent architecture to test multiple strategies and LangSmith for monitoring. The system implements continuous learning, capturing feedback and generalizing successful patterns across deployments while maintaining strict privacy controls.
- [**Cleric Ai**](https://www.zenml.io/llmops-database/ai-powered-sre-agent-for-production-infrastructure-management) \- Cleric Ai has developed an AI-powered SRE agent that autonomously monitors infrastructure, investigates issues, and provides diagnoses using a reasoning engine, tool integrations, and memory systems, aiming to reduce engineer workload by automating investigation workflows. The system emphasizes transparent decision-making, configurable model selection, and human oversight for remediation actions.
- [**Clipping**](https://www.zenml.io/llmops-database/building-an-ai-tutor-with-enhanced-llm-accuracy-through-knowledge-base-integration) \- Clipping, an educational technology startup, developed ClippingGPT, an AI tutor that leverages a specialized knowledge base and embeddings to significantly improve LLM accuracy, achieving a 26% performance increase over GPT-4 on the Brazilian Diplomatic Career Examination by prioritizing factual recall before response generation. This demonstrates how domain-specific knowledge integration can enhance LLM accuracy for educational applications.
- [**Co-op**](https://www.zenml.io/llmops-database/rag-powered-virtual-assistant-for-retail-store-operations) \- Co-op, a major UK retailer, implemented a RAG-powered virtual assistant using the Databricks Data Intelligence Platform to improve store employee access to operational information, processing over 1,000 policy documents with vector embeddings and semantic recall, and selecting GPT-3.5 after evaluating multiple models. The system, designed to handle 50,000-60,000 weekly queries, is currently in proof-of-concept, showing improved information retrieval and reduced support center load, with plans for a phased rollout.
- [**CoActive AI**](https://www.zenml.io/llmops-database/scaling-ai-systems-for-unstructured-data-processing-logical-data-models-and-embedding-optimization) \- CoActive AI developed a system for processing unstructured data at scale, using logical data models to bridge the gap between traditional storage and AI processing needs, and optimizing embedding computations to reduce costs. Their approach includes hybrid data and AI teams, cached embeddings, and task-specific output layers to enable efficient and scalable AI operations across diverse data modalities.
- [**Codeium**](https://www.zenml.io/llmops-database/advanced-context-aware-code-generation-with-custom-infrastructure-and-parallel-llm-processing) \- Codeium developed a novel “M-query” system that uses custom infrastructure to enable parallel processing of thousands of LLM calls, allowing for independent reasoning over potential context items, moving beyond the limitations of traditional embedding-based retrieval for code generation. This approach, combined with custom model training and a focus on real-world usage metrics, allows them to handle complex contextual queries across large codebases, delivering fast and accurate code generation for their IDE plugins used by Fortune 500 companies.
- [**Codeium**](https://www.zenml.io/llmops-database/building-enterprise-ready-ai-development-infrastructure-from-day-one) \- Codeium’s development of their AI-powered IDE demonstrates the importance of early investment in robust infrastructure for enterprise-grade AI tools. By prioritizing containerization, security, and flexible deployment options from the outset, they were able to scale from individual developers to large enterprises.
- [**Cognition AI**](https://www.zenml.io/llmops-database/autonomous-software-development-agent-for-production-code-generation) \- Cognition AI’s Devin is an autonomous software engineering agent that integrates with standard development tools like GitHub, Slack, and VS Code to perform complex tasks. Devin can operate within complete development environments, manage machine states, handle pull requests, and even debug code, showcasing its capacity for parallel task processing and integration with existing workflows.
- [**Consulting Firm / Car manufacturer / International bank**](https://www.zenml.io/llmops-database/llm-production-case-studies-consulting-database-search-automotive-showroom-assistant-and-banking-development-tools) \- This case study examines several LLM implementations, including a consulting firm’s financial database search using text-to-SQL and keyword generation, an automotive showroom assistant employing multi-layer processing for non-canonical data, and a banking code copilot project emphasizing the need for clear requirements and technical expertise. The studies highlight the importance of robust testing, systematic measurement, and careful data handling, while also noting that vector databases aren’t always necessary and that engineering work can be more challenging than the LLM integration itself.
- [**Convirza**](https://www.zenml.io/llmops-database/optimizing-call-center-analytics-with-small-language-models-and-multi-adapter-serving) \- Convirza utilizes Llama 3B with LoRA adapters, deployed via Predibase, to analyze millions of call center interactions monthly, achieving sub-0.1 second inference times and a 10x cost reduction compared to OpenAI. Their multi-adapter serving architecture on single GPUs enables efficient analysis of numerous custom metrics for agent performance and caller behavior, demonstrating that smaller, well-tuned models can outperform larger ones in specific domains.
- [**Convirza / Predibase**](https://www.zenml.io/llmops-database/multi-lora-serving-for-agent-performance-analysis-at-scale) \- Convirza, an AI-powered software platform, enhanced its agent performance evaluation by switching from Longformer models to a fine-tuned Llama-3-8b model using Predibase’s multi-LoRA infrastructure, achieving a 10x cost reduction compared to OpenAI, an 8% increase in F1 scores, and an 80% increase in throughput while efficiently processing millions of customer service calls. This implementation demonstrates the effectiveness of multi-LoRA serving for high-volume, real-time analysis, maintaining sub-second inference times across 60 performance indicators.
- [**Coval**](https://www.zenml.io/llmops-database/agent-testing-and-evaluation-using-autonomous-vehicle-simulation-principles) \- Coval is revolutionizing AI agent testing by applying autonomous vehicle simulation principles, moving from manual testing to a probabilistic approach with dynamic scenarios and multi-layered testing architectures. This approach emphasizes robust error handling and reliability, using LLMs to benchmark agent performance against human capabilities, and provides tools for dynamic scenario generation and performance monitoring.
- [**Cox 2M**](https://www.zenml.io/llmops-database/integrating-gemini-for-natural-language-analytics-in-iot-fleet-management) \- Cox 2M leveraged Gemini LLMs with Thoughtspot and Google Cloud to overcome slow analytics and resource constraints, enabling non-technical users to query complex IoT and fleet management data using natural language, reducing time to insights by 88% and cutting response times from a week to under an hour. The solution also features automated insight generation, change analysis, and a feedback loop for continuous improvement, all while processing real-time IoT sensor data.
- [**Credal**](https://www.zenml.io/llmops-database/enterprise-ai-adoption-journey-from-experimentation-to-core-operations) \- This case study analyzes the journey of enterprises adopting LLMs, detailing a four-stage progression from basic experimentation to core operations integration, emphasizing the importance of a multi-LLM approach, robust security, and advanced RAG for enterprise search. It also highlights the need for careful build vs. buy decisions, platform architecture, and comprehensive monitoring and governance frameworks to address challenges like security, debugging, and performance optimization.
- [**Credal**](https://www.zenml.io/llmops-database/lessons-from-building-a-production-rag-system-data-formatting-and-prompt-engineering) \- Credal, specializing in enterprise GenAI, processed 250,000 LLM calls across 100,000 corporate documents, finding that effective production LLM systems require careful data formatting and prompt engineering, especially for complex documents with footnotes and tables, and that focusing prompts on specific, challenging aspects of tasks led to better results.
- [**Crisis Text Line / Databricks**](https://www.zenml.io/llmops-database/llm-powered-crisis-counselor-training-and-conversation-simulation) \- Crisis Text Line utilized Databricks to create a robust LLMOps platform, deploying a fine-tuned Llama 2 conversation simulator for training crisis counselors with synthetic data, and a conversation phase classifier to maintain support quality, enhancing training and supporting over 1.3 million crisis conversations. This implementation demonstrates a responsible approach to using LLMs in a sensitive healthcare context.
- [**Cursor**](https://www.zenml.io/llmops-database/building-a-next-generation-ai-enhanced-code-editor-with-real-time-inference) \- Cursor built a next-generation AI-enhanced code editor by forking VS Code and integrating advanced LLM capabilities, focusing on a responsive and predictive coding experience beyond basic autocompletion. They employ techniques like Mixture of Experts (MoE) models, speculative decoding, and sophisticated caching to handle large context windows efficiently and maintain low latency.
- [**Da.tes**](https://www.zenml.io/llmops-database/practical-implementation-of-llms-for-automated-test-case-generation) \- A software team developed a semi-automated test case generation system using GPT-3.5 Turbo and LangChain, employing structured prompts and standardized templates. The AI-generated tests, applied to the Da.tes platform, achieved a 4.31 quality score, slightly outperforming human-generated tests at 4.18, demonstrating the viability of LLMs for test automation.
- [**Dandelion Health**](https://www.zenml.io/llmops-database/healthcare-nlp-pipeline-for-hipaa-compliant-patient-data-de-identification) \- Dandelion Health implemented a HIPAA-compliant NLP pipeline for de-identifying patient data, combining John Snow Labs’ Healthcare NLP with custom pre- and post-processing within a secure AWS environment. Their system employs context-aware processing, “hiding in plain sight” techniques, and rigorous quality control to achieve high recall rates while preserving data utility for medical research.
- [**Danswer**](https://www.zenml.io/llmops-database/scaling-enterprise-rag-with-advanced-vector-search-migration) \- Danswer, an enterprise search solution, migrated to Vespa to overcome limitations in their initial vector search setup, enabling hybrid search for team-specific terminology, custom decay functions for document versioning, and multi-vector embeddings for improved context, all while maintaining performance at scale. This migration improved search accuracy and resource efficiency for their RAG-based enterprise search product, highlighting the complexities of scaling LLM applications in production.
- [**Databricks**](https://www.zenml.io/llmops-database/field-ai-assistant-for-sales-team-automation) \- Databricks built a Field AI Assistant using their Mosaic AI agent framework to streamline sales operations, integrating data from their Lakehouse, CRM, and other sources. The system, powered by Azure OpenAI’s GPT-4, provides conversational data access, automates tasks, and manages CRM updates, while emphasizing data quality, governance, and continuous monitoring.
- [**Databricks**](https://www.zenml.io/llmops-database/building-a-custom-llm-for-automated-documentation-generation) \- Databricks built a custom, fine-tuned 7B parameter LLM to generate documentation for their Unity Catalog, overcoming challenges with quality, cost, and performance experienced with SaaS LLMs. This bespoke model now powers 80% of table metadata updates, achieving better quality, 10x cost reduction, and higher throughput.
- [**Databricks / Last Mile AI / Honeycomb**](https://www.zenml.io/llmops-database/from-mvp-to-production-llm-application-evaluation-and-deployment-challenges) \- A panel of experts from Databricks, Last Mile AI, and Honeycomb, among others, discussed the complexities of deploying LLM applications to production, highlighting challenges such as unpredictable user interactions and the need for robust feedback mechanisms, while also emphasizing the importance of domain-specific evaluation and strong knowledge management. The discussion covered best practices like gradual rollouts, automated tooling, and continuous improvement strategies, drawing parallels with traditional MLOps and offering recommendations for teams to ensure successful LLM deployments.
- [**Datastax**](https://www.zenml.io/llmops-database/building-an-ai-generated-movie-quiz-game-with-rag-and-real-time-multiplayer) \- Datastax created UnReel, a real-time multiplayer movie trivia game, using Langflow for AI pipelines and RAG to generate both real and fake movie quotes, with MistralAI’s model selected after testing. The game uses Astra DB for data storage, Cloudflare Durable Objects for state management, and PartyKit for real-time multiplayer, highlighting key LLMOps lessons such as prompt engineering, batch processing, and robust state management.
- [**Dataworkz**](https://www.zenml.io/llmops-database/rag-powered-customer-service-call-center-analytics) \- Dataworkz is using a RAG-based platform to improve insurance call center efficiency by converting call recordings into searchable vectors using Amazon Transcribe, Cohere, and MongoDB Atlas Vector Search, enabling agents to quickly access relevant information. This system includes a sophisticated ETL pipeline, robust monitoring, and A/B testing capabilities, demonstrating a practical approach to implementing LLMs in production.
- [**DDI**](https://www.zenml.io/llmops-database/automating-leadership-assessment-using-genai-and-llm-operations) \- DDI, a leadership development company, automated their behavioral simulation assessments using LLMs and a robust MLOps platform built on Databricks, reducing report generation time from 48 hours to just 10 seconds. By leveraging prompt engineering techniques and fine-tuning Llama3-8b, they achieved significant improvements in both speed and accuracy of complex behavioral analysis, with a recall score of 0.98 and an F1 score of 0.86.
- [**Deepgram**](https://www.zenml.io/llmops-database/building-production-ready-conversational-ai-voice-agents-latency-voice-quality-and-integration-challenges) \- Deepgram, a leader in transcription services, details the challenges and solutions in building production-ready conversational AI voice agents, highlighting their new text-to-speech product, Aura. The case study emphasizes the need to manage latency, aiming for a 300ms benchmark, and addresses complexities in end-pointing, voice quality optimization through prosody, and natural conversation implementation using filler words and pauses.
- [**Deepgram**](https://www.zenml.io/llmops-database/domain-specific-small-language-models-for-call-center-intelligence) \- Deepgram, a Speech-to-Text company, developed domain-specific small language models for call center applications, fine-tuning a 500M parameter model on call center transcripts to achieve superior performance in tasks like conversation continuation and summarization compared to larger models, while also being more cost-effective and faster. This demonstrates the value of specialized models over general-purpose ones for practical, real-world applications.
- [**Defense Innovation Unit / Global Fishing Watch / Coast Guard / NOAA**](https://www.zenml.io/llmops-database/dark-vessel-detection-system-using-sar-imagery-and-ml) \- The Defense Innovation Unit developed a machine learning system using satellite-based SAR imagery to detect illegal fishing, deploying it across 100+ countries via the SeaVision platform, and successfully identifying “dark vessels” that do not broadcast AIS signals. This system uses a Faster R-CNN model and addresses challenges with large image sizes and edge deployment, enabling targeted enforcement in marine protected areas.
- [**Delivery Hero**](https://www.zenml.io/llmops-database/semantic-product-matching-using-retrieval-rerank-architecture) \- Delivery Hero built a production-ready product matching system using LLMs, moving from basic lexical matching to a retrieval-rerank architecture with SBERT for semantic encoding and transformer-based cross-encoders, efficiently handling large catalogs while balancing accuracy and computational cost through hard negative sampling and fine-tuning.
- [**Department of Energy / U.S. Navy**](https://www.zenml.io/llmops-database/federal-government-ai-platform-adoption-and-scalability-initiatives) \- U.S. federal agencies are deploying AI and LLMs into production, addressing challenges like budget constraints and security. The Department of Energy’s Energy GPT project uses open models in a controlled environment, while the U.S. Navy’s Project AMMO showcases MLOps success, reducing model retraining time for undersea vehicles from six months to one week.
- [**Deutsche Bank**](https://www.zenml.io/llmops-database/large-bank-llmops-implementation-lessons-from-deutsche-bank-and-others) \- Deutsche Bank and other major banks are implementing generative AI for document processing, research, and risk modeling, using a service-oriented architecture and Google Cloud’s Doc AI to handle large volumes of unstructured data, automate research, and improve risk assessments, while prioritizing regulatory compliance and responsible AI practices. They are focusing on internal efficiency gains, augmenting human capabilities, and managing risks like bias and hallucinations, with a dedicated Center of Excellence and employee upskilling programs.
- [**Digits**](https://www.zenml.io/llmops-database/production-ready-question-generation-system-using-fine-tuned-t5-models) \- Digits, a fintech company, implemented a production system using fine-tuned T5 models on Google Cloud’s Vertex AI to generate accounting-related questions for client interactions, leveraging TensorFlow Extended for a robust MLOps pipeline and addressing challenges like hallucinations and training-serving skew with a multi-layered validation system and in-house fine-tuning. This system streamlines communication, maintains professional standards, and scales using Google Cloud infrastructure.
- [**Discord**](https://www.zenml.io/llmops-database/large-scale-ai-assistant-deployment-with-safety-first-evaluation-approach) \- Discord’s deployment of Clyde AI, a chatbot reaching over 200 million users, prioritized safety and evaluation, treating evals as unit tests integrated into their development workflow. They developed PromptFu, an open-source CLI tool for simple, fast, and deterministic evaluations, and used a practical approach to maintaining a casual chat personality.
- [**Discord**](https://www.zenml.io/llmops-database/building-and-scaling-llm-applications-at-discord) \- Discord’s case study outlines their systematic approach to developing and deploying LLM-powered features, emphasizing rapid prototyping with commercial LLMs, followed by rigorous prompt engineering and AI-assisted evaluation, and scaling through hosted or self-hosted solutions. Their framework focuses on balancing rapid development with robust production deployment, while maintaining focus on user experience, safety, and cost efficiency.
- [**Discover Financial Services**](https://www.zenml.io/llmops-database/generative-ai-implementation-in-banking-customer-service-and-knowledge-management) \- Multiple major banks, including Discover Financial Services, have implemented generative AI solutions, achieving a 70% reduction in agent search time by using RAG and summarization techniques on procedure documentation, leveraging Google Cloud’s Vertex AI and Gemini models. These implementations emphasized robust data governance, security, and compliance, with human-in-the-loop validation involving technical writers and expert agents to ensure accuracy and regulatory adherence.
- [**Doctolib**](https://www.zenml.io/llmops-database/building-an-agentic-ai-system-for-healthcare-support-using-langgraph) \- Doctolib built Alfred, an agentic AI system using LangGraph, to handle customer support requests, employing multiple specialized LLM-powered agents in a directed graph architecture and integrating their existing RAG engine, with a focus on security using JWT authentication and human-in-the-loop confirmation for critical actions. The system manages approximately 17,000 messages daily, with an initial use case focused on calendar access management, demonstrating a robust approach to LLM limitations, security, and production scaling.
- [**Docugami / Reet**](https://www.zenml.io/llmops-database/production-llm-systems-document-processing-and-real-estate-agent-co-pilot-case-studies) \- Docugami built a document processing system using custom XML knowledge graphs, structural chunking, and Apache Spark, deploying models on Kubernetes with Nvidia Triton and Redis for vector storage, while Reet developed Lucy, a real estate agent co-pilot, transitioning to OpenAI function calling for better performance and focusing on robust testing and CI/CD. Both companies emphasized comprehensive testing, monitoring, and continuous improvement, highlighting the need for adaptable systems in the rapidly evolving LLMOps space, balancing automation with human oversight.
- [**Doordash**](https://www.zenml.io/llmops-database/llms-for-enhanced-search-retrieval-and-query-understanding) \- Doordash integrated LLMs into their search system, using a hybrid approach with knowledge graphs and RAG to improve understanding of complex food delivery queries, resulting in a 30% increase in popular dish carousel trigger rates and a 2% improvement in whole page relevance. This implementation demonstrates a practical approach to leveraging LLMs in production while maintaining accuracy and performance.
- [**Doordash**](https://www.zenml.io/llmops-database/scaling-llms-for-product-knowledge-and-search-in-e-commerce) \- Doordash uses LLMs to build a product knowledge graph and enhance search across their expanding e-commerce platform, employing techniques like LLM-assisted annotation, RAG for training data generation, and model optimization for production deployment. Their system also uses LLMs for multi-intent understanding in search queries, while implementing guardrails to prevent over-personalization, and includes distributed computing and low-latency pipelines.
- [**Doordash**](https://www.zenml.io/llmops-database/building-a-high-quality-rag-based-support-system-with-llm-guardrails-and-quality-monitoring) \- Doordash built a RAG-based support system for delivery contractors, emphasizing quality control with a two-tiered LLM Guardrail that reduced hallucinations by 90% and compliance issues by 99%, alongside an LLM Judge for continuous monitoring and improvement. Their system handles thousands of daily requests, using a regression prevention strategy and strategically defaulting to human agents when latency becomes an issue.
- [**DoorDash**](https://www.zenml.io/llmops-database/strategic-framework-for-generative-ai-implementation-in-food-delivery-platform) \- DoorDash is strategically implementing Generative AI across its platform, focusing on areas like customer assistance with automated cart building, interactive discovery through advanced recommendation engines, and personalized content generation, while also improving internal operations with automated SQL generation and data extraction. The framework emphasizes data privacy and security, alongside model training and continuous monitoring, aiming for enhanced customer experience and operational efficiency.
- [**DoorDash**](https://www.zenml.io/llmops-database) \- DoorDash utilizes LLMs to automate and enhance their retail catalog management by extracting product attributes from unstructured SKU data, implementing a brand extraction pipeline with a hierarchical knowledge graph, organic product labeling using a waterfall approach, and generalized attribute extraction using RAG for entity resolution, leading to improved scalability, product discovery, and personalization.
- [**DoorDash**](https://www.zenml.io/llmops-database/llm-based-dasher-support-automation-with-rag-and-quality-controls) \- DoorDash implemented an LLM-based support system for their delivery contractors, using RAG to access a knowledge base and employing a multi-layered quality control approach with an LLM Guardrail and LLM Judge. This system handles thousands of daily requests, achieving a 90% reduction in hallucinations and a 99% reduction in compliance issues.
- [**Doordash**](https://www.zenml.io/llmops-database/building-an-enterprise-llmops-stack-lessons-from-doordash) \- Doordash’s ML Platform team details their approach to building an enterprise LLMOps stack, tackling challenges like inference optimization and cost management, and implementing key components such as gateway services, RAG, and fine-tuning infrastructure. They also share insights from LinkedIn and Uber’s LLMOps strategies, focusing on modular design, automation, and robust evaluation frameworks.
- [**DoorDash**](https://www.zenml.io/llmops-database/generative-ai-contact-center-solution-with-amazon-bedrock-and-claude) \- DoorDash implemented a generative AI contact center solution using Amazon Bedrock and Anthropic’s Claude models, leveraging RAG with Knowledge Bases for accurate responses and achieving a 2.5 second response latency, resulting in a 50% reduction in development time and a significant decrease in live agent escalations. The system, integrated with Amazon Connect and Amazon Lex, handles hundreds of thousands of daily support calls, demonstrating the effectiveness of LLMs in high-volume production environments.
- [**Dropbox**](https://www.zenml.io/llmops-database/detecting-and-mitigating-prompt-injection-via-control-characters-in-chatgpt) \- Dropbox’s security team discovered a novel prompt injection technique using control characters like backspace and carriage return to bypass system instructions in OpenAI’s GPT models, effectively making them forget context and instructions. This research highlights the need for robust input sanitization and validation when deploying LLMs in production environments.
- [**Dropbox**](https://www.zenml.io/llmops-database/scaling-ai-powered-file-understanding-with-efficient-embedding-and-llm-architecture) \- Dropbox built an AI-powered file understanding system for web previews, leveraging their Riviera framework to handle 2.5 billion daily requests, enabling summarization and Q&A across various file types with significant cost and latency improvements using k-means clustering and similarity-based chunk selection.
- [**Dropbox**](https://www.zenml.io/llmops-database/building-a-silicon-brain-for-universal-enterprise-search) \- Dropbox is transforming into an AI-powered universal search and organization platform, using LLMs to enhance its Dash product with features like semantic search across enterprise content. Their approach combines open-source LLMs, custom inference stacks, and hybrid architectures to deliver AI-driven search and organization features while maintaining strict data privacy and security for over 700 million users.
- [**Dropbox / OpenAI**](https://www.zenml.io/llmops-database/llm-security-discovering-and-mitigating-repeated-token-attacks-in-production-models) \- Dropbox’s security research revealed that repeated token sequences, both single and multi-token, could bypass security guardrails in OpenAI’s GPT-3.5 and GPT-4 models, leading to model divergence and the extraction of training data; this prompted OpenAI to implement improved filtering and timeouts to mitigate these vulnerabilities.
- [**Duolingo**](https://www.zenml.io/llmops-database/github-copilot-integration-for-enhanced-developer-productivity) \- Duolingo integrated GitHub Copilot, along with Codespaces and custom API integrations, to improve developer efficiency and code consistency across their growing codebase, resulting in a 25% speed increase for developers new to a repository and a 10% increase for experienced developers. This implementation also streamlined workflows, reduced context switching, and helped maintain consistent standards across their projects.
- [**Duolingo**](https://www.zenml.io/llmops-database/ai-powered-lesson-generation-system-for-language-learning) \- Duolingo leverages a custom-trained LLM and a structured prompting system to accelerate language lesson creation, enabling rapid content generation while maintaining educational quality through human oversight. This system allows for automated parameter handling and multi-stage review pipelines, resulting in faster course development and expansion into new features.
- [**Duolingo / Brainly / SoloLearn**](https://www.zenml.io/llmops-database/llm-integration-in-edtech-lessons-from-duolingo-brainly-and-sololearn) \- Duolingo, Brainly, and SoloLearn have integrated LLMs into their platforms for language learning, homework help, and coding education, respectively, focusing on challenges like fact accuracy, cost management, and content personalization; they’ve found success using LLMs for synthesis, augmenting prompts, pre-generating content, and prioritizing teaching effectiveness. These companies emphasize the importance of controlled rollouts, quality control, and monitoring model outputs to achieve real learning outcomes.
- [**Dust.tt**](https://www.zenml.io/llmops-database/building-a-horizontal-enterprise-agent-platform-with-infrastructure-first-approach) \- [Dust.tt](http://dust.tt/) transitioned from a developer tool to a horizontal enterprise platform for AI agent deployment, achieving high daily active user rates by prioritizing a robust infrastructure with custom integrations and function calling capabilities. Their approach emphasizes real-world usage metrics and a tech stack including Next.js, Rust, and Temporal, while abstracting technical complexities to make agent creation accessible to non-technical users.
- [**DXC Technology**](https://www.zenml.io/llmops-database/llm-powered-multi-tool-architecture-for-oil-gas-data-exploration) \- DXC Technology developed an LLM-powered AI assistant for oil and gas data exploration, significantly reducing analysis time by routing queries to specialized tools optimized for different data types. Leveraging Anthropic’s Claude models on Amazon Bedrock, the solution incorporates conversational capabilities and semantic search, enabling users to efficiently analyze complex datasets and accelerate the time to first oil.
- [**Dynamo**](https://www.zenml.io/llmops-database/training-and-deploying-compliant-multilingual-foundation-models) \- Dynamo, focused on secure AI solutions, developed an 8B parameter multilingual LLM using Databricks, achieving a 20% training speed improvement and completing training in 10 days. The model includes built-in security, compliance, and multilingual support for enterprise applications like customer support and fraud detection.
- [**eBay**](https://www.zenml.io/llmops-database/multi-track-approach-to-developer-productivity-using-llms) \- eBay enhanced developer productivity using a three-pronged approach: integrating GitHub Copilot, developing a custom LLM (eBayCoder) based on Code Llama 13B, and deploying an internal knowledge base GPT using RAG, resulting in improved code acceptance, software maintenance, and access to internal documentation.
- [**eBay**](https://www.zenml.io/llmops-database/building-price-prediction-and-similar-item-search-models-for-e-commerce) \- eBay built a hybrid system using transformer models to provide sellers with price recommendations and similar item suggestions, particularly for sports trading cards. The system combines semantic similarity and direct price prediction, generating embeddings that balance price accuracy with item relevance using a multi-task learning framework and hard negative examples.
- [**Echo AI / Log10**](https://www.zenml.io/llmops-database/automated-llm-evaluation-and-quality-monitoring-in-customer-support-analytics) \- Echo AI partnered with Log10 to implement automated LLM evaluation for their customer support analytics platform, achieving a 20-point F1 score improvement by using techniques like few-shot learning and fine-tuning to ensure high accuracy and reliability across various customer use cases. This system provides real-time monitoring, human override capabilities, and detailed visibility into model performance, while also supporting multiple LLM providers and open-source models.
- [**Echo.ai / Log10**](https://www.zenml.io/llmops-database/improving-llm-accuracy-and-evaluation-in-enterprise-customer-analytics) \- [Echo.ai](http://echo.ai/), a SaaS platform for customer conversation analysis, partnered with Log10 to improve LLM accuracy and evaluation in production. By leveraging Log10’s automated feedback and tuning infrastructure, [Echo.ai](http://echo.ai/) achieved a 20-point F1 score increase and a 44% reduction in feedback prediction error, enabling successful deployment of large enterprise contracts.
- [**Edmunds**](https://www.zenml.io/llmops-database/auto-moderating-car-dealer-reviews-with-genai) \- Edmunds automated their dealer review moderation using a GenAI solution powered by GPT-4 and Databricks Model Serving, reducing processing time from 72 hours to minutes. This implementation, which included custom prompt engineering and Databricks Unity Catalog for data governance, significantly decreased moderation team size and improved decision consistency for over 300 daily reviews.
- [**Elastic**](https://www.zenml.io/llmops-database/building-production-security-features-with-langchain-and-llms) \- Elastic leveraged LangChain and LangGraph to develop three production-ready security features: Automatic Import, Attack Discovery, and Elastic AI Assistant, streamlining security operations with RAG and controllable agents for ES\|QL query generation and data integration automation. The system, which includes LangSmith for debugging and performance monitoring, is currently serving over 350 users in production.
- [**ElevenLabs**](https://www.zenml.io/llmops-database/scaling-voice-ai-with-gpu-accelerated-infrastructure) \- ElevenLabs leverages Google Kubernetes Engine (GKE) with NVIDIA GPUs, including H100s, to power its voice AI platform, achieving a 600:1 ratio of generated to real-time audio across 29 languages. They employ NVIDIA’s AI Enterprise software stack, including NeMo for model customization and NIM for inference optimization, alongside GKE Autopilot for managed deployment.
- [**Ellipsis**](https://www.zenml.io/llmops-database/building-and-operating-production-llm-agents-lessons-from-the-trenches) \- This case study explores 15 months of building and operating LLM agents in production, detailing the implementation of custom caching, CI evaluation pipelines, and observability stacks, while also addressing challenges in prompt engineering and cost optimization. The study emphasizes the need for custom solutions and manual inspection, highlighting the limitations of current tools and frameworks when building reliable LLM-based systems.
- [**Emergent Methods**](https://www.zenml.io/llmops-database/production-scale-rag-system-for-real-time-news-processing-and-analysis) \- Emergent Methods has deployed a production-scale RAG system that processes over 1 million news articles daily, utilizing a microservices architecture for real-time analysis and context engineering, combining tools like Quadrant for vector search, VLM for GPU optimization, and their own Flow.app for orchestration to ensure low latency and high availability while addressing challenges like news freshness and multilingual support.
- [**Enlightened Airlines**](https://www.zenml.io/llmops-database/real-time-data-streaming-architecture-for-ai-customer-support) \- Enlightened Airlines implemented a real-time data streaming architecture using Kafka and Flink to power their AI customer support, replacing a batch-oriented system and enabling their AI agents to access up-to-date customer information across all channels. This resulted in improved response accuracy, reduced hallucination incidents, and faster query resolution, leading to enhanced customer satisfaction and decreased operational overhead.
- [**ESGpedia**](https://www.zenml.io/llmops-database/leveraging-rag-and-llms-for-esg-data-intelligence-platform) \- ESGpedia, an ESG data platform in Asia-Pacific, consolidated 300 data pipelines into a Databricks lakehouse and implemented a custom RAG solution using Mosaic AI, achieving a 4x cost reduction in data pipeline management and enabling context-aware ESG data analysis. This allowed them to deliver granular, tailored sustainability insights to clients across the region.
- [**Faber Labs**](https://www.zenml.io/llmops-database/building-goal-oriented-retrieval-agents-for-low-latency-recommendations-at-scale) \- Faber Labs’ Gora system employs Goal-Oriented Retrieval Agents to optimize subjective relevance ranking, achieving over 200% improvements in key metrics like conversion rates and average order value, while maintaining sub-second latency using a high-performance Rust backend and real-time user feedback processing. This system demonstrates effectiveness across e-commerce and healthcare sectors, showcasing the power of unified goal optimization and privacy-preserving learning.
- [**Facebook AI Research / Unusual Ventures / Digits / Bountiful**](https://www.zenml.io/llmops-database/large-language-models-in-production-round-table-discussion-latency-cost-and-trust-considerations) \- A panel of experts from Facebook AI Research, Unusual Ventures, Digits, and Bountiful discussed the practical challenges of deploying LLMs in production, focusing on managing latency, optimizing costs, and building trust. Digits shared their experience processing 100 million daily financial transactions using LLMs, highlighting model optimization and safety measures, while the panel also explored API vs self-hosted trade-offs and strategies for mitigating hallucinations.
- [**Factory**](https://www.zenml.io/llmops-database/langsmith-integration-for-automated-feedback-and-improved-iteration-in-sdlc) \- Factory, an enterprise AI company, implemented a self-hosted LangSmith instance to improve observability and feedback within their SDLC automation platform, specifically for their Code Droid system. By integrating LangSmith with AWS CloudWatch and using its Feedback API, they achieved end-to-end LLM pipeline monitoring, automated feedback collection, and streamlined prompt optimization, resulting in a 2x improvement in iteration speed, a 20% reduction in open-to-merge time, and a 3x reduction in code churn.
- [**Factory.ai**](https://www.zenml.io/llmops-database/autonomous-software-development-using-multi-model-llm-system-with-advanced-planning-and-tool-integration) \- [Factory.ai](http://factory.ai/)’s Code Droid system uses a multi-model LLM approach, combining models from Anthropic and OpenAI, to automate software development tasks, incorporating HyperCode for codebase understanding and ByteRank for information retrieval, achieving 19.27% on SWE-bench Full and 31.67% on SWE-bench Lite while prioritizing safety and compliance.
- [**Factory.ai**](https://www.zenml.io/llmops-database/building-reliable-agentic-systems-in-production) \- [Factory.ai](http://factory.ai/) is building an AI platform for software engineering automation, focusing on reliable agentic systems. They use techniques like context propagation, consensus mechanisms, and careful tool design to address planning, decision-making, and environmental grounding challenges, emphasizing modularity and human oversight.
- [**FactSet**](https://www.zenml.io/llmops-database/building-an-enterprise-genai-platform-with-standardized-llmops-framework) \- FactSet, a financial data and analytics provider, implemented a standardized LLMOps framework using Databricks Mosaic AI and MLflow to address challenges with fragmented GenAI development, resulting in a 70% reduction in latency for code generation and a 60% reduction in end-to-end latency for text-to-formula generation, while also enabling cost-effective use of fine-tuned open-source models. This framework enabled unified governance, streamlined model development, and improved deployment capabilities, fostering a culture of collaboration and innovation.
- [**Faire**](https://www.zenml.io/llmops-database/fine-tuning-and-scaling-llms-for-search-relevance-prediction) \- Faire, a global wholesale marketplace, improved its search relevance evaluation by implementing a fine-tuned Llama model, achieving a 28% improvement in prediction accuracy compared to their previous GPT model, and scaling to 70 million predictions per day using 16 GPUs with a self-hosted solution. This transition from manual labeling to an automated LLM-based system enabled near real-time feedback on search algorithm performance and supports various applications like offline retrieval analysis and ranker optimization.
- [**Farfetch**](https://www.zenml.io/llmops-database/multimodal-search-and-conversational-ai-for-fashion-e-commerce-catalog) \- Farfetch implemented iFetch, a multimodal conversational AI system, to enhance product discovery on their fashion marketplace, using semantic search and vector databases to handle nuanced language. They extended CLIP with fashion-specific taxonomic information and relaxed contrastive loss for improved image-based search, focusing on practical improvements like handling brand-specific queries and maintaining conversational context.
- [**Farfetch**](https://www.zenml.io/llmops-database/scaling-recommender-systems-with-vector-database-infrastructure) \- Farfetch utilizes Vespa as a vector database to power a scalable recommender system, delivering personalized recommendations across multiple retailers with sub-100ms latency by employing matrix decomposition on user-product interactions and features, generating user and item embeddings. The system cleverly handles sparse data through a custom storage schema and optimized dot-product operations, along with storing the dense user embeddings matrix in a single document.
- [**FeedYou**](https://www.zenml.io/llmops-database/production-intent-recognition-system-for-enterprise-chatbots) \- FeedYou’s FeedBot Designer employs a hierarchical intent recognition system using NLP.js, with dedicated models per intent for improved performance and maintainability, achieving a 72% local intent matching rate and handling 72% of queries without human intervention by focusing on simple, well-tuned models and robust error handling. The platform prioritizes rapid model training, automated conflict detection, and real-time validation, demonstrating a practical approach to production-grade chatbot deployment.
- [**Fiddler AI**](https://www.zenml.io/llmops-database/building-a-rag-based-documentation-chatbot-lessons-from-fiddler-s-llmops-journey) \- Fiddler AI developed a documentation chatbot using GPT-3.5 and RAG, leveraging LangChain for its LLM pipeline. The project highlights practical LLMOps, addressing challenges like query processing, document chunking, and hallucination reduction through continuous monitoring, user feedback, and iterative improvements to the knowledge base.
- [**First Orion**](https://www.zenml.io/llmops-database/leveraging-amazon-q-for-integrated-cloud-operations-data-access-and-automation) \- First Orion, a telecommunications software company, implemented Amazon Q to unify access to their siloed cloud operations data, enabling engineers to use natural language queries across sources like S3, Confluence, and ServiceNow. This solution not only provides a unified access point but also automates ticket creation and management, streamlining their cloud operations workflow.
- [**FiscalNote**](https://www.zenml.io/llmops-database/streamlining-legislative-analysis-model-deployment-with-mlops) \- FiscalNote, a legal and regulatory intelligence company, streamlined their ML model deployment process by implementing Databricks’ MLflow and Model Serving, increasing deployment frequency by 3x. This new MLOps pipeline automated infrastructure management, enabled seamless model updates, and improved data asset discoverability, ultimately enhancing their ability to deliver timely legislative insights.
- [**Fuzzy Labs**](https://www.zenml.io/llmops-database/scaling-self-hosted-llms-with-gpu-optimization-and-load-testing) \- Fuzzy Labs developed a self-hosted LLM system using Mistral-7B to improve developer documentation for a tech company, employing vLLM for inference optimization and Ray Serve for horizontal scaling to achieve sub-second response times and efficient GPU usage. Through systematic load testing with Locust, they reduced response times from 11 seconds to 3 seconds, enabling the system to handle concurrent users effectively.
- [**Gantry / Structured.ie / NVIDIA**](https://www.zenml.io/llmops-database/panel-discussion-on-llm-evaluation-and-production-deployment-best-practices) \- A panel of experts from Gantry, [Structured.ie](http://structured.ie/), and NVIDIA discussed the shift in LLM deployment, highlighting the need for robust evaluation frameworks that combine automated metrics with human feedback, and emphasizing the importance of continuous monitoring and domain-specific benchmarks. They also addressed the need for better tooling and safety measures in production environments, focusing on user outcomes over model-centric metrics.
- [**Gerdau**](https://www.zenml.io/llmops-database/llm-powered-upskilling-assistant-in-steel-manufacturing) \- Gerdau, a steel manufacturer, implemented an LLM-powered upskilling assistant for employees after migrating to the Databricks Data Intelligence Platform to address data infrastructure challenges, resulting in a 40% cost reduction in data processing and the onboarding of 300 new data users. This strategic move showcases a measured approach to LLM adoption, prioritizing a robust data foundation and platform integration for future AI initiatives.
- [**GitHub**](https://www.zenml.io/llmops-database/evolution-of-llm-integration-in-github-copilot-development) \- GitHub’s development of Copilot began with experimenting with GPT-3 for code generation, evolving from a basic chatbot concept to an interactive IDE integration. Through iterative model improvements, prompt engineering, and fine-tuning, they progressed from a Python-only model to a multilingual one (Codex), implementing context-aware completions and targeted training.
- [**GitHub**](https://www.zenml.io/llmops-database/improving-contextual-understanding-in-github-copilot-through-advanced-prompt-engineering) \- GitHub Copilot, leveraging OpenAI’s Codex model, enhanced its contextual understanding through advanced prompt engineering, including a Fill-in-the-Middle (FIM) paradigm and a neighboring tabs feature, resulting in a 10% and 5% increase in completion and suggestion acceptance rates respectively, and leading to a 55% increase in coding speed for developers. These improvements, combined with sophisticated caching and retrieval systems, maintain low latency while providing more relevant code suggestions.
- [**GitHub**](https://www.zenml.io/llmops-database/enterprise-llm-application-development-github-copilot-s-journey) \- GitHub’s journey developing Copilot showcases the complexities of building and deploying an enterprise-grade LLM application, emphasizing rapid iteration, robust infrastructure, and a focus on user feedback to achieve a 55% increase in coding speed and a 74% reduction in developer frustration. Their approach involved transitioning from direct API usage to a scalable Azure infrastructure, implementing caching and quality pipelines, and prioritizing community engagement for a successful launch.
- [**GitHub**](https://www.zenml.io/llmops-database/building-production-grade-llm-applications-an-architectural-guide) \- Based on insights from GitHub’s ML experts, this case study provides a detailed architectural guide for deploying LLMs in production, covering key areas such as problem scoping, model selection, and customization, alongside essential architectural components like user input processing and enrichment pipelines. The guide also emphasizes implementation best practices for data management, security, performance optimization, and quality assurance, including vector database considerations, data filtering, caching strategies, and evaluation frameworks.
- [**GitHub**](https://www.zenml.io/llmops-database/evolving-github-copilot-through-llm-experimentation-and-user-centered-design) \- GitHub’s development of Copilot exemplifies a structured approach to integrating LLMs into developer workflows, starting with early access to GPT-4 and resulting in features like Copilot for Pull Requests, Docs, and CLI. Through iterative development and user feedback, they emphasized key principles like predictability, tolerability, steerability, and verifiability, prioritizing user experience and workflow integration over perfect accuracy.
- [**GitLab**](https://www.zenml.io/llmops-database/dogfooding-ai-features-in-gitlab-s-development-workflow) \- GitLab integrated its AI-powered GitLab Duo suite into its own development workflows, using features like AI-assisted code suggestions, merge request summarization, and documentation generation. This internal implementation led to efficiency gains, improved code quality, and streamlined incident management, while also focusing on LLMOps best practices and measuring ROI.
- [**GitLab**](https://www.zenml.io/llmops-database/llm-validation-and-testing-at-scale-gitlab-s-comprehensive-model-evaluation-framework) \- GitLab developed a Centralized Evaluation Framework (CEF) to rigorously test and validate LLMs powering their GitLab Duo AI features, using a library of thousands of prompts to evaluate model performance across numerous use cases. This framework employs a systematic approach, including establishing performance baselines, iterative development, and continuous validation using metrics like Cosine Similarity and LLM Judge, ensuring consistent quality and improvement.
- [**Gitlab**](https://www.zenml.io/llmops-database/building-production-scale-code-completion-tools-with-continuous-evaluation-and-prompt-engineering) \- Gitlab’s ModelOps team implemented a production-scale code completion tool using a combination of open-source and third-party LLMs, featuring a continuous evaluation pipeline that incorporates token-based analysis, historical code patterns, and developer feedback. Their system includes a dual-engine architecture for prompt management and a gateway, along with reinforcement learning to iteratively improve code completion accuracy and developer productivity.
- [**Glean**](https://www.zenml.io/llmops-database/building-robust-enterprise-search-with-llms-and-traditional-ir) \- Glean, an enterprise search company, employs a hybrid approach, combining traditional information retrieval with modern LLMs and embeddings, to deliver a comprehensive search solution. Their platform prioritizes rigorous ranking algorithm tuning, personalization, and cross-application integrations, rather than relying solely on AI, enabling them to serve major enterprises with features like feed recommendations and real-time updates.
- [**GoDaddy**](https://www.zenml.io/llmops-database/from-mega-prompts-to-production-lessons-learned-scaling-llms-in-enterprise-customer-support) \- GoDaddy’s Digital Care team leverages LLMs to automate customer support across messaging channels, transitioning from monolithic prompts to task-specific ones using a Controller-Delegate pattern, and implementing RAG with Sparse Priming Representations, achieving a 1% failure rate in chat completions while navigating challenges like latency and complex memory management. They emphasize the importance of structured output validation, human oversight, and model switching capabilities, while also highlighting the need for robust guardrails and testing methodologies.
- [**Golden State Warriors**](https://www.zenml.io/llmops-database/ai-powered-personalized-content-recommendations-for-sports-and-entertainment-venue) \- The Golden State Warriors utilized Vertex AI on Google Cloud to create a personalized content recommendation system, delivering tailored content across their digital platforms. This system integrates diverse data sources to provide relevant recommendations for both sports and entertainment events at the Chase Center, supporting over 18,000 seats with a lean technical team.
- [**Gong**](https://www.zenml.io/llmops-database/implementing-question-answering-over-sales-conversations-with-deal-me-at-gong) \- Gong developed “Deal Me,” an LLM-powered question-answering feature that allows users to query extensive sales interaction data, providing rapid insights. A hybrid approach was implemented to optimize costs and improve quality, routing queries to either direct LLM-based QA or pre-computed insights based on the nature of the query.
- [**Google**](https://www.zenml.io/llmops-database/source-grounded-llm-assistant-with-multi-modal-output-capabilities) \- Google’s NotebookLM uses source grounding, allowing users to upload their own documents to create a personalized AI assistant powered by Gemini 1.5 Pro, complete with a citation system, transient context windows for privacy, and safety filters; it also features a sophisticated audio overview capability that generates human-like podcast-style conversations with natural speech patterns and dual AI personas. The platform prioritizes safety and responsibility through content monitoring, clear labeling of AI-generated content, and a privacy-preserving architecture, demonstrating best practices in LLMOps.
- [**Google**](https://www.zenml.io/llmops-database/lessons-learned-from-production-ai-agent-deployments) \- Google’s Vertex AI team shares insights from deploying numerous LLM-powered agents, highlighting the need for comprehensive system design beyond just the models themselves, focusing on meta-prompting, multi-layered safety, and robust evaluation frameworks. They emphasize treating agent components as code, regular evaluation cycles, and addressing challenges like prompt injection and maintaining consistent quality.
- [**Google**](https://www.zenml.io/llmops-database/optimizing-security-incident-response-with-llms-at-google) \- Google has implemented an LLM-powered system to automate security incident response, specifically focusing on generating incident summaries and executive communications. This resulted in a 51% reduction in time spent on incident summaries and a 53% reduction in time spent on executive communications, while maintaining or improving quality compared to human-written content, all while adhering to strict data protection measures.
- [**Google / Scale Venture Partners**](https://www.zenml.io/llmops-database/framework-for-evaluating-llm-production-use-cases) \- Barak Turovsky, a veteran of Google’s AI initiatives, proposes a framework for evaluating LLM production use cases based on accuracy, fluency, and risk, recommending creative and productivity tasks for initial deployment while cautioning against high-stakes applications. The framework emphasizes data management, system architecture, and risk mitigation, advocating for a phased approach and hybrid systems that combine LLMs with traditional methods.
- [**Google Cloud / Symbol AI / Chain ML / Deloitte**](https://www.zenml.io/llmops-database/panel-discussion-scaling-generative-ai-in-enterprise---challenges-and-best-practices) \- A panel of AI leaders from Google Cloud, Symbol AI, Chain ML, and Deloitte discussed the practical challenges of scaling generative AI in the enterprise, covering model selection, infrastructure, and implementation strategies. The discussion emphasized a value-driven approach, the importance of production readiness assessments, and highlighted emerging trends like agent-based systems and domain specialization.
- [**Grab**](https://www.zenml.io/llmops-database/rag-powered-llm-system-for-automated-analytics-and-fraud-investigation) \- Grab’s Integrity Analytics team built an LLM-powered system using their internal Spellvault LLM and a custom Data-Arks middleware to automate data analysis and fraud investigations. This RAG-based solution, chosen for its cost-effectiveness and scalability, reduced report generation time by 3-4 hours per report and streamlined fraud investigations to minutes.
- [**Grab**](https://www.zenml.io/llmops-database/llm-powered-data-discovery-and-documentation-platform) \- Grab addressed data discovery issues across their extensive data infrastructure by creating HubbleIQ, an LLM-powered platform that improved search with Elasticsearch optimizations and automated documentation generation using GPT-4, increasing coverage from 20% to 90% for frequently accessed tables and reducing data discovery time. They also integrated a chatbot using Glean, resulting in a 17 percentage point increase in user satisfaction.
- [**Grab**](https://www.zenml.io/llmops-database/productionizing-llm-powered-data-governance-with-langchain-and-langsmith) \- Grab utilized LangChain and LangSmith to enhance their Metasense V2 data governance system, which employs LLMs for automated data classification and metadata generation, resulting in improved accuracy and reduced manual review. By optimizing prompts, splitting complex tasks, and implementing robust monitoring, they streamlined team collaboration and now process thousands of data entries daily, demonstrating successful LLMOps best practices in production.
- [**Grab**](https://www.zenml.io/llmops-database/enhancing-vector-similarity-search-with-llm-based-reranking) \- Grab implemented a hybrid search approach combining vector similarity search with LLM-based reranking, using FAISS and OpenAI embeddings for initial retrieval and GPT-4 for reranking, which improved performance on complex queries with constraints and negations compared to vector search alone. This two-stage process demonstrated the benefits of combining traditional and advanced techniques for enhanced search relevance.
- [**Grab**](https://www.zenml.io/llmops-database/llm-powered-data-classification-system-for-enterprise-scale-metadata-generation) \- Grab developed an LLM-powered data classification system, using GPT-3.5 via an orchestration service called Gemini, to automate metadata generation across their PetaByte-scale data infrastructure, replacing manual tagging of sensitive data. The system classifies database columns and generates metadata tags, processing over 20,000 data entities within a month of deployment, achieving 80% user satisfaction and significantly reducing manual effort in data governance.
- [**Gradient Labs**](https://www.zenml.io/llmops-database/building-production-ready-customer-support-ai-agents-challenges-and-solutions) \- Gradient Labs developed a production-ready AI customer support agent, tackling challenges beyond simple LLM prototypes by using a state machine architecture with a durable execution engine to manage complex state, race conditions, and knowledge integration. The system successfully manages hundreds of daily conversations, demonstrating the need for robust engineering practices when deploying AI agents in production.
- [**Grainger**](https://www.zenml.io/llmops-database/enterprise-scale-rag-implementation-for-e-commerce-product-discovery) \- Grainger, a major MRO distributor, implemented an enterprise-scale RAG system using Databricks to enhance product discovery across their 2.5 million item catalog, leveraging Databricks Vector Search to manage product embeddings and handle 400,000 daily updates, ensuring low-latency, real-time search and improved customer service. The system uses a flexible model-serving strategy, allowing for experimentation with different LLMs, and integrates contextual information to improve search accuracy for diverse user queries.
- [**Grammarly**](https://www.zenml.io/llmops-database/specialized-text-editing-llm-development-through-instruction-tuning) \- Grammarly’s CoEdIT showcases the effectiveness of specialized LLMs for text editing, achieving state-of-the-art results with models up to 60x smaller than GPT-3-Edit, through targeted instruction tuning on a curated dataset of non-meaning-changing edits, and offering an open-source implementation for community adoption.
- [**Grammarly**](https://www.zenml.io/llmops-database/building-a-delicate-text-detection-system-for-content-safety) \- Grammarly developed a novel system for detecting delicate text, going beyond standard toxicity detection to identify emotionally charged or potentially triggering content. They created DeTexD, a benchmark dataset and a RoBERTa-based classification model achieving a 79.3% F1 score, outperforming existing toxic text detection methods in this domain.
- [**Great Ormond Street Hospital NHS Trust**](https://www.zenml.io/llmops-database/llm-powered-information-extraction-from-pediatric-cardiac-mri-reports) \- Great Ormond Street Hospital utilized a hybrid approach, combining smaller LLMs for entity extraction with few-shot learning for tabular data, to process 15,000 unstructured pediatric cardiac MRI reports, successfully extracting patient identifiers and clinical measurements while adhering to NHS security constraints. The project demonstrated the effectiveness of prompt engineering with models like FLAN-T5 and RoBERTa, and the viability of using smaller LLMs in production healthcare settings.
- [**Greptile**](https://www.zenml.io/llmops-database/improving-ai-code-review-bot-comment-quality-through-vector-embeddings) \- Greptile improved their AI code review bot by using vector embeddings to filter out low-value comments, increasing the rate of addressed feedback from 19% to over 55% after initial attempts with prompt engineering and LLM-based severity ratings failed. This highlights the effectiveness of combining LLMs with traditional ML techniques and the importance of user feedback in production LLM systems.
- [**Guaros**](https://www.zenml.io/llmops-database/debating-the-value-and-future-of-llmops-industry-perspectives) \- A discussion between Patrick Barker, CTO of Guaros, and Farud, an ML engineer, explores the nature of LLMOps, with Patrick arguing it’s a distinct field due to unique tooling and user needs, while Farud views it as an extension of MLOps, highlighting the need for practitioners to balance traditional MLOps skills with LLM-specific knowledge. The debate covers data pipeline similarities, tool development approaches, environmental concerns, and future trends, emphasizing the importance of practical implementation over hype.
- [**Hapag-Lloyd**](https://www.zenml.io/llmops-database/streamlining-corporate-audits-with-genai-powered-document-processing) \- Hapag-Lloyd streamlined their corporate audits by implementing a GenAI solution using Databricks’ DBRX model, fine-tuned on 12T tokens of audit data. This resulted in a 66% reduction in time spent creating new findings and a 77% reduction in executive summary review time, showcasing the impact of LLMs on real-world business processes.
- [**Harvard Business School**](https://www.zenml.io/llmops-database/building-an-ai-teaching-assistant-chatltv-at-harvard-business-school) \- Harvard Business School built ChatLTV, an AI teaching assistant for their Launching Tech Ventures course, using Azure OpenAI, Pinecone, and Langchain. This RAG-based system, trained on a 15 million-word course corpus, served 250 MBA students via Slack, handling over 3000 queries and improving class preparation.
- [**Hearst / Gannett / The Globe and Mail / E24**](https://www.zenml.io/llmops-database/ai-powered-real-estate-transaction-newsworthiness-detection-system) \- A collaborative project between several news organizations developed Real Estate Alerter, an AI-powered system that uses anomaly detection and LLMs to identify newsworthy real estate transactions, incorporating a human feedback loop to improve accuracy. The system, which includes a celebrity detection feature and a Slack bot for alerts, demonstrates the practical application of GenAI in automating news discovery, while highlighting the importance of human oversight.
- [**Heidelberg University**](https://www.zenml.io/llmops-database/automating-radiology-report-generation-with-fine-tuned-llms) \- Heidelberg University’s Department of Radiology and Nuclear Medicine automated radiology report generation using Vision Transformers and a fine-tuned Llama 3 model, achieving a training loss of 0.72 and a validation loss of 1.36 while optimizing for a single GPU using techniques like 4-bit quantization and LoRA. This demonstrates the practical application of LLMs in healthcare, emphasizing efficient resource utilization and the importance of human oversight.
- [**HeyRevia**](https://www.zenml.io/llmops-database/ai-powered-call-center-agents-for-healthcare-operations) \- HeyRevia’s AI-powered call center solution leverages a multi-layered architecture with real-time audio processing, context-aware decision-making, and goal-oriented planning to handle complex healthcare tasks like insurance verification and claims processing, achieving improved efficiency and success rates while maintaining strict compliance. The system prioritizes performance with sub-500ms latency, manages multiple concurrent calls, and ensures compliance through self-hosted LLMs, SOC 2, and HIPAA adherence.
- [**Holiday Extras**](https://www.zenml.io/llmops-database/enterprise-ai-transformation-holiday-extras-chatgpt-enterprise-implementation-case-study) \- Holiday Extras, a European travel extras provider, successfully implemented ChatGPT Enterprise across their organization, achieving significant productivity gains and cultural transformation by leveraging AI for multilingual content creation, data analysis, engineering support, and customer service, resulting in 500+ hours saved weekly, $500k annual savings, and a 95% weekly adoption rate. This enterprise-wide rollout improved their NPS from 60% to 70% and fostered a more data-driven culture, empowering both technical and non-technical staff.
- [**Honeycomb**](https://www.zenml.io/llmops-database/natural-language-query-interface-with-production-llm-integration) \- Honeycomb built a natural language query interface for their observability platform using GPT-3.5, enabling users to translate natural language into structured queries with a 94% success rate. This feature significantly improved user engagement, with teams using the query assistant being 2-3x more likely to create complex queries and save them to boards.
- [**Honeycomb**](https://www.zenml.io/llmops-database/implementing-llm-observability-for-natural-language-querying-interface) \- Honeycomb, an observability company, implemented a natural language querying interface and used comprehensive observability, including distributed tracing with OpenTelemetry, to address post-launch challenges. This enabled them to monitor the entire user experience, isolate issues, and establish a continuous improvement cycle, resulting in improved product retention and conversion rates.
- [**Honeycomb**](https://www.zenml.io/llmops-database/the-hidden-complexities-of-building-production-llm-features-lessons-from-honeycomb-s-query-assistant) \- Honeycomb’s development of Query Assistant, a natural language to query interface, revealed the complexities of production LLM features, including managing large schemas, optimizing for latency, and navigating prompt engineering. Their approach focused on treating LLMs as feature engines, emphasizing non-destructive design, robust validation, and security, while also addressing legal and compliance requirements.
- [**Honeycomb**](https://www.zenml.io/llmops-database/building-and-scaling-an-llm-powered-query-assistant-in-production) \- Honeycomb built an LLM-powered Query Assistant using GPT-3.5-turbo and text embeddings to simplify querying on their observability platform, resulting in high adoption rates among enterprise and self-serve users and a significant increase in manual query retention and complex query creation. The cost-effective implementation, averaging $30/month in OpenAI costs, also demonstrated the assistant’s ability to handle unexpected inputs like DSL expressions and trace IDs, validating their “ship to learn” approach to AI integration.
- [**Hotelplan Suisse**](https://www.zenml.io/llmops-database/generative-ai-powered-knowledge-sharing-system-for-travel-expertise) \- Hotelplan Suisse collaborated with Datatonic to create a generative AI-powered knowledge-sharing system for their travel experts, integrating over 10 data sources and using semantic search to provide rapid travel recommendations, reducing response times from hours to minutes, and includes features like chat history management, automated testing, and CI/CD pipelines. The system also prioritizes safety with guardrails and extensive logging in Google Cloud.
- [**HP**](https://www.zenml.io/llmops-database/building-a-knowledge-base-chatbot-for-data-team-support-using-rag) \- HP’s data engineering team, burdened by support requests, deployed a RAG-based chatbot using Databricks Mosaic AI, which reduced operational costs by 20-30% and significantly decreased manual support requests by providing a self-service knowledge base for data models, platform features and access requests. Built in just three weeks, the system uses a vector database and web crawler to ingest internal documentation, showcasing the efficiency of LLMs for internal knowledge management.
- [**Human Loop / Find.xyz**](https://www.zenml.io/llmops-database/pitfalls-and-best-practices-for-production-llm-applications) \- Human Loop, a developer platform, shares insights from deploying LLMs in production, emphasizing objective evaluation, prompt management, and strategic optimization, including fine-tuning, while cautioning against premature optimization with complex agents. The case study of Find.xyz demonstrates the effectiveness of fine-tuning open-source models for niche applications, highlighting the need for specialized tooling and practices tailored to the unique demands of LLM applications.
- [**Humanloop / Duolingo / Gusto**](https://www.zenml.io/llmops-database/building-a-foundation-model-operations-platform) \- Humanloop has built a comprehensive LLMOps platform that provides engineers with tools for prompt engineering, version control, and evaluation, addressing the challenges of managing prompts as code. The platform also includes feedback collection and production monitoring capabilities, enabling continuous improvement of LLM performance, and is used by companies like Duolingo and Gusto to manage their LLM applications at scale.
- [**HumanLoop / Filevine / GitHub / Duolingo / Ironclad**](https://www.zenml.io/llmops-database/llmops-best-practices-and-success-patterns-across-multiple-companies) \- This study examines successful LLMOps implementations across multiple companies, emphasizing the importance of domain experts in prompt engineering and the need for robust evaluation frameworks, including iterative prototyping and user feedback integration. It highlights the necessity of tooling that enables collaboration, comprehensive logging, and debugging, showcasing examples like Ironclad’s use of Rivet to achieve a 50% contract auto-negotiation rate.
- [**HumanLoop / Jingo**](https://www.zenml.io/llmops-database/best-practices-for-llm-production-deployments-evaluation-prompt-management-and-fine-tuning) \- HumanLoop, a developer tools platform, shares best practices for deploying LLMs in production, emphasizing systematic evaluation, prompt management with versioning, and fine-tuning for performance and cost optimization; they use GitHub Copilot as a case study of successful large-scale LLM deployment.
- [**IBM**](https://www.zenml.io/llmops-database/mlops-maturity-levels-and-enterprise-implementation-challenges) \- This case study analyzes the progression of MLOps maturity in enterprises, from manual to fully automated systems, detailing the challenges faced by data scientists, ML engineers, and DevOps teams. It highlights the unique considerations for LLM deployments, including infrastructure, security, and evaluation, while providing best practices for data management, model deployment, and team collaboration.
- [**ICE / NYSE**](https://www.zenml.io/llmops-database/text-to-sql-system-with-structured-rag-and-comprehensive-evaluation) \- ICE/NYSE built a production text-to-SQL system using structured RAG on Databricks’ Mosaic AI stack, enabling business users to query data with natural language. The system features a robust evaluation framework with syntactic and execution matching, achieving 77% and 96% accuracy respectively, and incorporates a continuous improvement pipeline using feedback loops and few-shot learning.
- [**incident.io**](https://www.zenml.io/llmops-database/building-and-deploying-an-ai-powered-incident-summary-generator) \- [incident.io](http://incident.io/) implemented an AI-powered incident summary generator using OpenAI models, focusing on prompt engineering, testing, and phased rollouts. The system integrates with Slack to enrich incident data, processes updates and metadata, and generates structured summaries with a 63% direct acceptance rate and a further 26% edited before use.
- [**IncludedHealth**](https://www.zenml.io/llmops-database/building-a-comprehensive-llm-platform-for-healthcare-applications) \- IncludedHealth developed Wordsmith, a comprehensive LLM platform for healthcare applications, featuring a proxy service for multi-provider access, model serving with MLServer and HuggingFace, and robust infrastructure for training and evaluation. This platform enabled production applications like automated documentation, coverage checking, and clinical scribing, all while adhering to strict security and compliance requirements in a regulated healthcare environment.
- [**Instacart**](https://www.zenml.io/llmops-database/using-llms-to-enhance-search-discovery-and-recommendations) \- Instacart implemented LLMs to enhance search and product discovery, moving beyond exact matches by generating complementary and substitute product recommendations. They used a two-pronged approach, combining carefully crafted prompts with domain-specific knowledge, and built a sophisticated pipeline with offline generation, post-processing, and a novel “LLM as Judge” evaluation system.
- [**Instacart**](https://www.zenml.io/llmops-database/enhancing-e-commerce-search-with-llms-at-scale) \- Instacart integrated LLMs into their search architecture to improve query understanding, product attribute extraction, and complex intent handling across their grocery e-commerce platform, addressing challenges with tail queries and enabling personalized merchandising. Their implementation combines offline and online LLM processing, focusing on cost optimization and robust evaluation to enhance search relevance and enable new product discovery capabilities.
- [**Instacart**](https://www.zenml.io/llmops-database/building-and-scaling-an-enterprise-ai-assistant-with-gpt-models) \- Instacart’s Ava, an internal AI assistant built on GPT-4 and GPT-3.5, has become a key productivity tool, boasting over 50% monthly employee adoption and 900+ weekly active users, with features like a web interface, Slack integration, and a prompt exchange system, enhancing workflows across engineering and other departments.
- [**Instacart**](https://www.zenml.io/llmops-database/advanced-prompt-engineering-techniques-for-production-llm-applications) \- Instacart employs a range of advanced prompt engineering techniques, including Chain of Thought, ReAct, and novel methods like “Room for Thought” and Monte Carlo sampling, to optimize their production LLM applications such as internal tools and search features, focusing on improving output reliability and managing token usage. These techniques, primarily implemented with GPT-4, demonstrate practical strategies for enhancing LLM performance in real-world environments.
- [**InsuranceDekho**](https://www.zenml.io/llmops-database/transforming-insurance-agent-support-with-rag-powered-chat-assistant) \- InsuranceDekho implemented a RAG-based chat assistant using Amazon Bedrock and Anthropic’s Claude Haiku to streamline insurance agent support, leveraging OpenSearch for vector storage and Redis for caching, resulting in an 80% reduction in query response times. This system significantly reduced reliance on subject matter experts and improved customer service efficiency.
- [**IntellectAI**](https://www.zenml.io/llmops-database/scaling-esg-compliance-analysis-with-rag-and-vector-search) \- IntellectAI’s Purple Fabric platform uses MongoDB Atlas and Vector Search to automate ESG compliance analysis, scaling from 150 to over 8,000 companies. This RAG-based system processes 10 million documents across 30+ formats, achieving over 90% accuracy in compliance assessments, demonstrating a significant speed improvement over manual analysis.
- [**Interact.ai / Amberflow / Google / Databricks / Inflection AI**](https://www.zenml.io/llmops-database/panel-discussion-on-llmops-challenges-model-selection-ethics-and-production-deployment) \- A panel discussion featuring AI leaders explored the complexities of deploying LLMs in production, covering model selection, cost optimization, and ethical considerations. The discussion highlighted practical experiences from companies like [Interact.ai](http://interact.ai/)’s healthcare deployment, Inflection AI’s emotionally intelligent models, and insights from Google and Databricks on responsible AI deployment and tooling.
- [**Interweb Alchemy**](https://www.zenml.io/llmops-database/interactive-ai-powered-chess-tutoring-system) \- Interweb Alchemy built an interactive chess tutoring system that combines LLMs like GPT-4-mini for move generation with Stockfish for position evaluation, using chess.js for legal move validation, providing real-time feedback and analysis to enhance the learning experience. The project showcases practical LLMOps techniques such as iterative model selection, prompt engineering, and the integration of multiple AI components.
- [**Jabil**](https://www.zenml.io/llmops-database/genai-transformation-of-manufacturing-and-supply-chain-operations) \- Jabil, a global manufacturing giant, implemented Amazon Q to transform its manufacturing and supply chain operations, deploying GenAI solutions for shop floor assistance, procurement intelligence, and supply chain management, resulting in reduced downtime and improved efficiency. The company established robust governance through AI and GenAI councils, focusing on practical use cases and clear ROI.
- [**JOBifAI**](https://www.zenml.io/llmops-database/implementing-effective-safety-filters-in-a-game-based-llm-application) \- JOBifAI, a game using LLMs for interactive gameplay, struggled with inconsistent safety filter behavior, requiring a three-retry mechanism to achieve a 99% success rate, but highlighted the need for more granular error reporting and transparent safety filter implementations to improve reliability and cost-effectiveness. The case study underscores the challenges of deploying LLMs in production, particularly regarding safety filters, and calls for better error handling and cost management strategies.
- [**John Snow Labs**](https://www.zenml.io/llmops-database/enterprise-scale-healthcare-llm-system-for-unified-patient-journeys) \- John Snow Labs has developed an enterprise-scale healthcare LLM system, deployed via Kubernetes within customer infrastructure, that processes multi-modal patient data using specialized medical LLMs for information extraction and unified knowledge graphs, enabling natural language querying and outperforming general-purpose LLMs in medical tasks. The system emphasizes data privacy, explainability, and integration with existing healthcare IT infrastructure, demonstrating best practices in LLMOps for large-scale deployments.
- [**John Snow Labs**](https://www.zenml.io/llmops-database/healthcare-patient-journey-analysis-platform-with-multimodal-llms) \- John Snow Labs developed a healthcare analytics platform using specialized medical LLMs to process diverse patient data, including unstructured text and images, enabling natural language queries for patient history analysis and cohort building. Deployed within the customer’s infrastructure using Kubernetes, the system prioritizes security and scalability, and it significantly outperforms general-purpose LLMs like GPT-4 in medical tasks, while maintaining consistency and explainability.
- [**John Snow Labs**](https://www.zenml.io/llmops-database/multimodal-healthcare-data-integration-with-specialized-llms) \- John Snow Labs utilizes multiple specialized LLMs to integrate diverse healthcare data, including structured EHR data, unstructured text, and semi-structured FHIR resources, addressing the challenge of fragmented medical information by using LLMs for information extraction, semantic modeling, data deduplication, and natural language query processing, all while maintaining security, scalability, and compliance. This system improves patient data analysis, clinical decision support, and reduces manual data integration efforts.
- [**John Snow Labs**](https://www.zenml.io/llmops-database/automated-medical-literature-review-system-using-domain-specific-llms) \- John Snow Labs has developed a medical literature review system using domain-specific LLMs to automate the traditionally time-consuming process of analyzing medical research, combining proprietary LLMs with a comprehensive knowledge base to enable rapid analysis of hundreds of papers, with features like custom knowledge base integration, intelligent data extraction, and automated filtering. The system offers both SaaS and on-premise deployment options, with enterprise-grade features like security, scalability, and API integration.
- [**Johns Hopkins Applied Physics Laboratory**](https://www.zenml.io/llmops-database/medical-ai-assistant-for-battlefield-care-using-llms) \- Johns Hopkins APL is developing CPG-AI, a battlefield medical assistant that uses LLMs to guide untrained soldiers through medical procedures by translating clinical guidelines into conversational guidance. Built using APL’s RALF framework, the system demonstrates capabilities in condition inference, natural language Q&A, and step-by-step care guidance, focusing on common battlefield injuries.
- [**Kantar Worldpanel**](https://www.zenml.io/llmops-database/fine-tuning-llms-for-market-research-product-description-matching) \- Kantar Worldpanel modernized their product description matching system by using LLMs to generate training data, achieving 94% accuracy with GPT-4 and then fine-tuning smaller models for production using Databricks Mosaic AI and MLflow, automating a previously manual process. This approach allowed them to balance cost and performance while freeing up resources for more complex tasks.
- [**Kapa.ai / Docker / CircleCI / Reddit / Monday.com**](https://www.zenml.io/llmops-database/production-rag-best-practices-implementation-lessons-at-scale) \- [Kapa.ai](http://kapa.ai/)’s case study, drawing from over 100 RAG implementations at companies like Docker and Reddit, outlines best practices for production RAG systems, covering data management, refresh pipelines, and evaluation frameworks, while also addressing security and performance optimization. The study emphasizes the challenges of moving beyond proof-of-concept and provides concrete guidance for successful production deployments.
- [**Kentauros AI**](https://www.zenml.io/llmops-database/building-production-grade-ai-agents-overcoming-reasoning-and-tool-challenges) \- Kentauros AI is building production-grade AI agents, addressing challenges in reasoning, tool use, and real-world deployment through an iterative agent architecture evolution from G2 to G5, focusing on memory systems, skill management, and multiple model integration. Their approach emphasizes practical solutions, iterative testing, and resource optimization, with future directions including enhanced reinforcement learning and more sophisticated memory systems.
- [**Klarity**](https://www.zenml.io/llmops-database/document-processing-automation-with-llms-evolution-of-evaluation-strategies) \- Klarity, a document processing automation company, successfully transitioned to generative AI, processing over half a million documents for B2B SaaS customers in finance and accounting, and developed a robust evaluation framework to address the challenges of non-deterministic performance, rapid development cycles, and the limitations of standard benchmarks, using techniques like staged evaluation, customer-specific metrics, and synthetic data generation.
- [**Klarna**](https://www.zenml.io/llmops-database/ai-assistant-for-global-customer-service-automation) \- Klarna deployed an OpenAI-powered AI assistant for customer service, handling 2.3 million conversations across 23 markets and 35+ languages, reducing resolution times from 11 minutes to under 2 minutes and decreasing repeat inquiries by 25%. This system, integrated into the Klarna app, achieved customer satisfaction scores comparable to human agents and is projected to deliver a $40 million profit improvement in 2024.
- [**Komodo Health**](https://www.zenml.io/llmops-database/healthcare-data-analytics-democratization-with-mapai-and-llm-integration) \- Komodo Health’s MapAI uses multiple LLMs and a LangChain/LangGraph framework to provide an NLP interface for their MapLab platform, enabling non-technical users to perform complex healthcare data analysis, reducing weeks-long processes to instant insights. This system, built with an API-first architecture, integrates with their Healthcare Map data source and maintains HIPAA compliance, while supporting various skill levels through different interfaces.
- [**LangGraph / Waii**](https://www.zenml.io/llmops-database/building-production-grade-conversational-analytics-with-langgraph-and-waii) \- This case study showcases the creation of production-ready conversational analytics applications by combining LangGraph’s multi-agent framework with Waii’s text-to-SQL capabilities, enabling natural language querying of complex databases through sophisticated join handling and agentic workflows. The solution demonstrates how to achieve accurate and scalable interactions with intricate data structures.
- [**leboncoin**](https://www.zenml.io/llmops-database/llm-powered-search-relevance-re-ranking-system) \- leboncoin, France’s leading second-hand marketplace, implemented an LLM-powered search re-ranking system using a bi-encoder architecture with pre-computed ad embeddings to improve search relevance across their 60 million listings, achieving up to 5% improvement in click and contact rates and 10% improvement in user experience KPIs while maintaining strict latency requirements. The system leverages a distilled BERT model and a two-phase deployment strategy to handle high throughput and low latency demands.
- [**Lemonade**](https://www.zenml.io/llmops-database/troubleshooting-and-optimizing-rag-pipelines-lessons-from-production) \- Lemonade, a technology-driven insurance company, utilizes RAG pipelines for its chat-based customer interactions, addressing challenges like missing content, retrieval issues, and response generation through data cleaning, prompt engineering, and advanced retrieval strategies. Their experience highlights the importance of systematic troubleshooting, data quality, and continuous optimization for RAG pipelines in production.
- [**Lime**](https://www.zenml.io/llmops-database/ai-powered-customer-support-automation-for-global-transportation-service) \- Lime, a global micromobility company, deployed Forethought’s AI platform to automate customer support, achieving a 27% case automation rate and reducing first response times by 77% through intelligent routing and automated responses, while also processing 1.7 million tickets annually and supporting multiple languages. This implementation addressed challenges like manual ticket handling and language barriers, demonstrating significant improvements in efficiency and customer satisfaction.
- [**Lindy.ai**](https://www.zenml.io/llmops-database/evolution-from-open-ended-llm-agents-to-guided-workflows) \- [Lindy.ai](http://lindy.ai/) transitioned from an open-ended LLM agent platform to a structured, visual workflow-based system, improving reliability and usability by constraining LLM behavior through guided workflows and rails. This shift included a dedicated memory module, prompt caching, and structured output calls, demonstrating that guided workflows lead to more robust AI agents capable of handling complex automation tasks.
- [**LinkedIn**](https://www.zenml.io/llmops-database/building-a-production-text-to-sql-assistant-with-multi-agent-architecture) \- LinkedIn’s SQL Bot utilizes a multi-agent architecture built on LangChain and LangGraph to provide a text-to-SQL interface within their DARWIN data platform, addressing the complexities of enterprise data warehouses through embedding-based retrieval, LLM-based re-ranking, and self-correction agents, resulting in a 95% user satisfaction rate for query accuracy. This system demonstrates the value of a methodical approach to LLMOps, with particular attention to integration with existing enterprise systems and workflows.
- [**LinkedIn**](https://www.zenml.io/llmops-database/building-and-evolving-a-production-genai-application-stack) \- LinkedIn’s production GenAI journey involved a strategic shift from Java to Python, leveraging LangChain for building sophisticated conversational agents. This included developing a robust prompt management system, a skill-based task automation framework, and a memory system for conversational context, all while ensuring production stability and enabling both commercial and fine-tuned LLM deployments.
- [**LinkedIn**](https://www.zenml.io/llmops-database/building-a-large-scale-ai-recruiting-assistant-with-experiential-memory) \- LinkedIn’s Hiring Assistant uses LLMs to automate recruiting workflows, incorporating an experiential memory system for personalization and an agent orchestration layer for complex task management. This system handles tasks from job description creation to interview coordination, while emphasizing responsible AI practices and integrating with existing LinkedIn technologies.
- [**LinkedIn**](https://www.zenml.io/llmops-database/ai-driven-security-posture-management-platform) \- LinkedIn’s Security Posture Platform (SPP) uses an AI-driven interface, SPP AI, to manage security vulnerabilities, leveraging a security knowledge graph and LLMs for natural language queries. This system improved vulnerability response speed by 150% and increased digital infrastructure coverage by 155% through a multi-stage query processing pipeline and sophisticated context generation.
- [**LinkedIn**](https://www.zenml.io/llmops-database/building-and-scaling-a-production-generative-ai-assistant-for-professional-networking) \- LinkedIn implemented a production-grade generative AI system using a Retrieval Augmented Generation (RAG) architecture to improve job searches and content browsing, employing specialized AI agents and a custom “skills” wrapper for API integration. The team focused on overcoming challenges like LLM schema compliance, quality assurance, and optimizing for latency and resource management, using a multi-tiered evaluation framework and streaming architecture to achieve significant improvements.
- [**LinkedIn**](https://www.zenml.io/llmops-database/pragmatic-product-led-approach-to-llm-integration-and-prompt-engineering) \- LinkedIn’s Pan Cha outlines a product-led approach to LLM integration, emphasizing solving user problems over forced AI adoption, starting with simple implementations using public APIs, and iteratively improving through robust prompt engineering and evaluation frameworks. This pragmatic strategy prioritizes user trust, cost management, and clear problem definition, avoiding AI for its own sake.
- [**LinkedIn**](https://www.zenml.io/llmops-database/building-and-deploying-large-language-models-for-skills-extraction-at-scale) \- LinkedIn has implemented a multi-stage LLM-based system for extracting and mapping skills from platform content, powering their Skills Graph, using BERT models optimized with knowledge distillation for production. This system handles 200 profile edits per second with sub-100ms latency, leveraging a hybrid serving approach and Spark for offline scoring, resulting in significant improvements in job recommendations and skills matching.
- [**LinkedIn**](https://www.zenml.io/llmops-database/productionizing-generative-ai-applications-from-exploration-to-scale) \- LinkedIn implemented generative AI features across their platform, prioritizing user-centric design and systematic prompt engineering, finding that optimized prompts with GPT-3.5 Turbo could match GPT-4 performance. Their approach emphasized building trust through transparent communication and content policies, while also addressing challenges like GPU resource constraints and prompt reliability at scale.
- [**London Stock Exchange Group**](https://www.zenml.io/llmops-database/ai-powered-client-services-assistant-for-post-trade-services) \- The London Stock Exchange Group (LSEG) deployed an AI-powered client services assistant using Amazon Q Business, enhancing post-trade support with a RAG architecture that integrates internal knowledge and public data; a rigorous validation process using Claude v2 ensures response accuracy, improving customer experience and staff productivity.
- [**Malt**](https://www.zenml.io/llmops-database/building-a-scalable-retriever-ranker-architecture-malt-s-journey-with-vector-databases-and-llm-powered-freelancer-matching) \- Malt enhanced its freelancer matching system using a two-step retriever-ranker architecture powered by a vector database (Qdrant), significantly reducing response times from over 60 seconds to under 3 seconds while maintaining recommendation quality. This approach leverages custom-trained models and a robust monitoring system to achieve scalability and performance improvements.
- [**Mark43**](https://www.zenml.io/llmops-database/secure-generative-ai-integration-for-public-safety-applications) \- Mark43, a public safety technology company, integrated Amazon Q Business into their platform, providing law enforcement agencies with secure generative AI capabilities, enabling natural language queries and automated case report summaries, reducing administrative time significantly. The implementation prioritizes security, using built-in connectors and embedded web experiences to create a seamless AI assistant within existing workflows, while maintaining strict data access controls.
- [**Marsh McLennan**](https://www.zenml.io/llmops-database/enterprise-wide-llm-assistant-deployment-and-evolution-towards-fine-tuned-models) \- Marsh McLennan rolled out an enterprise-wide LLM assistant, achieving 87% adoption across 90,000 employees and processing 25 million requests annually, initially using cloud-based APIs and RAG for secure data access, then evolving to fine-tuned models for specific tasks, achieving accuracy exceeding GPT-4 with low training costs and saving over a million hours annually.
- [**Mastercard**](https://www.zenml.io/llmops-database/responsible-llm-adoption-for-fraud-detection-with-rag-architecture) \- Mastercard implemented a RAG architecture for fraud detection using LLMs, achieving a 300% improvement in some cases, while prioritizing responsible AI principles, security, and access controls. This case study highlights the complexities of enterprise-scale LLM deployment, including the need for robust data pipelines and scalable infrastructure.
- [**Mastercard**](https://www.zenml.io/llmops-database/linguistic-informed-approach-to-production-llm-systems) \- Mastercard’s data science team is using a linguistic-first approach to LLM deployment, focusing on syntax, morphology, semantics, and pragmatics to address challenges like evolving language and tokenization issues. This methodology, demonstrated with a biology question-answering system, improved accuracy from 35% to 85% using pragmatic instruction with Falcon 7B and the guidance framework, while also reducing inference time compared to vanilla ChatGPT.
- [**MediaRadar / Vivvix**](https://www.zenml.io/llmops-database/automating-video-ad-classification-with-genai) \- MediaRadar \| Vivvix, an advertising intelligence company, automated their video ad classification process using Databricks Mosaic AI and Apache Spark Structured Streaming, combining GenAI models with their existing classification systems to increase throughput from 800 to 2,000 ads per hour and reduce model experimentation time from 2 days to 4 hours. They optimized costs by choosing GPT-3.5 and improved accuracy by combining multiple classification approaches.
- [**Mendable.ai**](https://www.zenml.io/llmops-database/leveraging-langsmith-for-debugging-tools-actions-in-production-llm-applications) \- [Mendable.ai](http://mendable.ai/) utilized LangSmith to debug and optimize their production LLM-powered enterprise AI assistant, which uses tools and actions to interact with APIs and data sources, resulting in improved system performance and $1.3 million in savings for a major tech company client within five months. By implementing LangSmith, they gained visibility into agent decision-making, optimized prompts, and validated tool schemas, addressing initial challenges with observability and reliability.
- [**Mendix**](https://www.zenml.io/llmops-database/integrating-generative-ai-into-low-code-platform-development-with-amazon-bedrock) \- Mendix, a low-code platform, integrated Amazon Bedrock to provide secure and scalable access to generative AI models within their development environment, enabling features like text generation and image creation. Their implementation includes custom model training, robust security measures using AWS services, and cost-effective model selection, showcasing a mature approach to LLMOps.
- [**Mercado Libre**](https://www.zenml.io/llmops-database/enhancing-e-commerce-search-with-vector-embeddings-and-generative-ai) \- Mercado Libre, Latin America’s largest e-commerce platform, transitioned from a word-matching search system to one using vector embeddings and Google’s Vector Search, significantly improving results for complex, natural language queries which make up half of their search traffic, leading to increased conversion rates. This new system generates vector embeddings for both products and user queries, enabling a more semantic understanding of search intent.
- [**Mercado Libre**](https://www.zenml.io/llmops-database/github-copilot-deployment-at-scale-enhancing-developer-productivity) \- Mercado Libre, a leading e-commerce platform in Latin America, deployed GitHub Copilot across its 9,000+ developer team, integrating it with their existing GitHub Enterprise infrastructure, resulting in a 50% reduction in code writing time and improved developer satisfaction. The implementation also included security workflows and automated testing, demonstrating a focus on both productivity and code quality at scale.
- [**Mercado Libre**](https://www.zenml.io/llmops-database/building-a-scalable-llm-gateway-for-e-commerce-recommendations) \- Mercado Libre implemented a centralized LLM gateway, “Fury,” to manage large-scale generative AI deployments across their organization, integrating with multiple providers and offering a custom playground and SDK; a key use case is a real-time product recommendation system that leverages LLMs for personalized suggestions, supporting multiple languages and dynamic prompt versioning.
- [**Mercado Libre**](https://www.zenml.io/llmops-database/real-world-llm-implementation-rag-documentation-generation-and-natural-language-processing-at-scale) \- Mercado Libre implemented LLMs for RAG-based documentation search using Llama Index, automated documentation generation, and natural language processing for product information and booking, emphasizing data pre-processing, quality control, and iterative prompt engineering. Their experience highlighted the importance of comprehensive documentation, structured outputs, and careful model selection, showcasing practical LLMOps including function calling and continuous refinement.
- [**Mercado Libre / ATB Financial / LBLA / Collibra**](https://www.zenml.io/llmops-database/data-and-ai-governance-integration-in-enterprise-genai-adoption) \- Mercado Libre, ATB Financial, LBLA, and Collibra are implementing data and AI governance for GenAI, utilizing Google Cloud tools like Dataplex. They are exploring GenAI for automated metadata, natural language search, and lineage tracking, while addressing challenges like data quality and multi-cloud integration, emphasizing the need for strong data governance for successful AI deployment.
- [**Mercari**](https://www.zenml.io/llmops-database/building-ai-assist-llm-integration-for-e-commerce-product-listings) \- Mercari implemented an AI Assist feature using a hybrid LLM approach, leveraging GPT-4 for offline attribute extraction and GPT-3.5-turbo for real-time title suggestions, focusing on practical challenges like prompt engineering, error handling, and managing output inconsistencies in a production environment. They employed both offline and online evaluations to ensure quality and optimize for cost and performance.
- [**Mercari**](https://www.zenml.io/llmops-database/fine-tuning-and-quantizing-llms-for-dynamic-attribute-extraction) \- Mercari fine-tuned a 2B parameter LLM using QLoRA to extract dynamic attributes from user-generated listings, achieving a 95% reduction in model size and a 14x cost reduction compared to GPT-3.5-turbo, while also improving BLEU score and controlling hallucinations. The implementation included careful dataset preparation, parameter-efficient fine-tuning, and post-training quantization with llama.cpp.
- [**Meta**](https://www.zenml.io/llmops-database/scaling-ai-image-animation-system-with-optimized-latency-and-traffic-management) \- Meta’s deployment of their AI image animation feature demonstrates a comprehensive approach to scaling generative AI for billions of users, using techniques like floating-point precision reduction and temporal-attention optimization to improve model performance. The system leverages PyTorch optimizations and a sophisticated traffic management system with regional routing and load balancing to minimize latency and ensure global reliability.
- [**Meta**](https://www.zenml.io/llmops-database/scaling-llm-infrastructure-building-and-operating-24k-gpu-clusters-for-llama-training) \- Meta scaled its AI infrastructure to train LLaMA 3 by building two 24K GPU clusters, achieving 95% training efficiency through full-stack optimizations across hardware, networking, and software, while addressing challenges in hardware reliability, thermal management, and network topology. This involved a transition from smaller recommendation models to massive LLM training jobs requiring thousands of GPUs running for months.
- [**Meta**](https://www.zenml.io/llmops-database/automated-unit-test-improvement-using-llms-for-android-applications) \- Meta’s TestGen-LLM leverages large language models to automatically enhance unit test coverage for Android applications, including platforms like Instagram and Facebook. Using an Assured Offline LLM-Based Software Engineering approach, it generates additional test cases with strict quality controls, resulting in a 10% improvement in targeted classes and high acceptance from engineers.
- [**Microsoft**](https://www.zenml.io/llmops-database/building-production-grade-rag-systems-for-financial-document-analysis) \- Microsoft’s team developed a production-grade RAG system for analyzing complex financial documents, tackling challenges like metadata extraction, chart analysis, and nuanced evaluation. Their solution incorporated multi-modal models, specialized prompt engineering, and a robust evaluation framework, highlighting the complexities of building real-world RAG systems beyond basic implementations.
- [**Microsoft**](https://www.zenml.io/llmops-database/building-a-financial-data-rag-system-lessons-from-search-first-architecture) \- A financial services firm developed a RAG-based chatbot using Azure OpenAI and Azure AI Search to provide access to financial documents, overcoming initial challenges with context loss and search accuracy by implementing a “search-first” architecture that leverages GPT-4 generated summaries for improved relevance. This approach, combined with hybrid search and custom scoring, significantly improved response accuracy and reduced manual research time for financial analysts.
- [**Microsoft**](https://www.zenml.io/llmops-database/lessons-from-enterprise-llm-deployment-cross-functional-teams-experimentation-and-security) \- Microsoft engineers detail their experiences deploying LLMs for enterprise clients in Australia, emphasizing the need for cross-functional teams and robust LLMOps practices including continuous experimentation and evaluation pipelines. The case study highlights careful RAG implementation and critical security measures like guard rails to mitigate vulnerabilities such as prompt injection.
- [**Microsoft**](https://www.zenml.io/llmops-database/best-practices-for-ai-agent-development-and-deployment) \- Microsoft’s Raj Ricky outlines best practices for AI agent development, emphasizing starting with a minimal viable product and constrained environments, while avoiding premature adoption of complex frameworks. He highlights the importance of clear success criteria, human oversight during initial development, and performance optimization techniques like quantization, while balancing autonomy and control.
- [**Microsoft**](https://www.zenml.io/llmops-database/real-time-question-answering-system-with-two-stage-llm-architecture-for-sales-content-recommendations) \- Microsoft built a real-time question-answering system for their MSX Sales Copilot, enabling sellers to quickly find relevant sales content using a two-stage LLM architecture with bi-encoder retrieval and cross-encoder re-ranking, achieving few-second response times and a 3.7/5 relevancy rating from users. The system operates on document metadata due to content access limitations, and is deployed on Azure Machine Learning endpoints with weekly model refreshes.
- [**Microsoft**](https://www.zenml.io/llmops-database/llms-for-cloud-incident-management-and-root-cause-analysis) \- Microsoft Research leveraged LLMs, including GPT-3 and GPT-3.5, to automate incident management for Microsoft 365, analyzing 40,000 incidents across 1000+ services to generate root cause analysis and mitigation recommendations, with fine-tuned GPT-3.5 models achieving a 70% usefulness rating from on-call engineers in production.
- [**Microsoft / GitHub**](https://www.zenml.io/llmops-database/building-product-copilots-engineering-challenges-and-best-practices) \- A study of 26 software engineers building AI-powered product copilots highlights challenges in prompt engineering, orchestration, and testing, leading to the development of solutions like prompt linters and intent detection systems, while emphasizing safety, privacy, and cost management. The research underscores the need for more mature tooling and standardized practices to support AI-first development.
- [**Microsoft Research / Deepgram / Prem AI / ISO AI**](https://www.zenml.io/llmops-database/multi-modal-ai-agents-architectures-and-production-deployment-patterns) \- A panel of experts from Microsoft Research, Deepgram, Prem AI, and ISO AI discussed the challenges of deploying multi-modal AI agents, covering topics like latency, model architecture, and scaling. They explored how combining voice, vision, and text can improve agent performance, and how hierarchical architectures using both large and smaller specialized models can optimize for different use cases.
- [**MLflow**](https://www.zenml.io/llmops-database/mlflow-s-production-ready-agent-framework-and-llm-tracing) \- MLflow introduces a production-ready agent framework with comprehensive tracing, evaluation, and experiment tracking, addressing the challenges of deploying LLM agents. This system provides deep visibility into agent operations, detailed logging of multi-turn conversations, and evaluation tools for assessing retrieval relevance and prompt engineering effectiveness, enabling teams to efficiently monitor, debug, and optimize their LLM-powered applications.
- [**MNP**](https://www.zenml.io/llmops-database/building-a-client-focused-financial-services-platform-with-rag-and-foundation-models) \- MNP, a Canadian professional services firm, modernized its data analytics platform by implementing a lakehouse architecture on Databricks, leveraging Mixtral 8x7B with a RAG approach to deliver contextual insights to clients. This solution, deployed in under six weeks, enabled secure and efficient processing of complex data queries while maintaining data isolation through Private AI standards.
- [**MongoDB / Dataworkz**](https://www.zenml.io/llmops-database/agentic-rag-implementation-for-retail-personalization-and-customer-support) \- MongoDB and Dataworkz partnered to implement an agentic RAG solution for retail, leveraging MongoDB Atlas for vector search and Dataworkz’s RAG builder, enabling personalized customer experiences through intelligent chatbots, dynamic product recommendations, and enhanced search by integrating real-time operational data with unstructured information. The system uses an agentic approach to intelligently query multiple data sources, combining lexical and semantic search with knowledge graphs, demonstrating a significant advancement in LLMOps for complex, context-aware applications.
- [**Morgan Stanley**](https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation) \- Morgan Stanley’s wealth management division implemented a GPT-4 powered internal chatbot, enabling their financial advisors to quickly access a vast library of investment strategies, market research, and analyst insights. This system, processing hundreds of thousands of pages of PDF-based content, has over 200 daily active users, showcasing the effectiveness of LLMs for enterprise knowledge management.
- [**MosaicML**](https://www.zenml.io/llmops-database/training-and-deploying-mpt-lessons-learned-in-large-scale-llm-development) \- MosaicML developed the open-source MPT family of large language models, including 7B and 30B parameter versions, demonstrating that high-quality LLMs can be trained at significantly lower costs, with the 7B model costing under $250,000. They built a complete training platform that handles data processing, distributed training across 512+ GPUs, and model deployment at scale, while establishing key best practices around planning, experimentation, data quality, and operational excellence for production LLM development, including robust checkpointing and failure recovery.
- [**MSD**](https://www.zenml.io/llmops-database/text-to-sql-system-for-complex-healthcare-database-queries) \- MSD partnered with the AWS Generative Innovation Center to build a text-to-SQL system using Amazon Bedrock and Anthropic’s Claude 3.5 Sonnet, enabling analysts to query complex healthcare databases with natural language, using custom lookup tools and prompt engineering to handle coded columns and complex queries. This resulted in significantly reduced query times and improved data accessibility for non-technical users.
- [**MultiCare**](https://www.zenml.io/llmops-database/multicare-a-large-scale-medical-case-report-dataset-for-ai-model-training) \- The MultiCare project created a large-scale, multimodal medical case report dataset with over 75,000 articles and 135,000 images, using a sophisticated data processing pipeline with tools like BioPython, OpenCV, and spaCy to extract and structure text, images, and metadata, enabling training of language, computer vision, and multimodal AI systems. The dataset features automated extraction of demographic data, edge detection for image splitting, and contextual parsing of image captions, and is hosted on Zenodo and Hugging Face with a flexible filtering system.
- [**N8N**](https://www.zenml.io/llmops-database/building-production-ai-agents-with-vector-databases-and-automated-data-collection) \- A company developed and deployed autonomous AI agents over 18 months, focusing on lead generation and inbox management, using vector databases, automated data collection, and structured prompt engineering with n8n for custom tool integration. This resulted in a scalable multi-agent system that highlights the importance of data quality, agent architecture, and robust tool integration for complex business workflows.
- [**National Healthcare Group**](https://www.zenml.io/llmops-database/implementing-llms-for-patient-education-and-healthcare-communication) \- National Healthcare Group integrated LLMs into existing healthcare apps and messaging platforms to provide 24/7 multilingual patient education, focusing on conditions like eczema and medical test preparation. The implementation emphasizes practical integration, careful monitoring, and manual review of LLM responses to ensure accuracy and privacy.
- [**Neeva**](https://www.zenml.io/llmops-database/overcoming-llm-production-deployment-challenges) \- Neeva, a search engine company, successfully navigated the complexities of deploying LLMs in production by addressing infrastructural challenges like speed and API reliability, as well as output-related issues such as format variability and safety, emphasizing a phased approach starting with non-critical workflows and focusing on robust evaluation frameworks. Their strategy included optimizing for speed and cost, ensuring output consistency, and planning for scale, all while maintaining a user-centric approach.
- [**Neva / Intercom / Prompt Layer / OctoML**](https://www.zenml.io/llmops-database/cost-optimization-and-performance-panel-discussion-strategies-for-running-llms-in-production) \- A panel of experts from Neva, Intercom, Prompt Layer, and OctoML discussed strategies for optimizing LLM deployments in production, covering cost and performance, including transitioning from API services to in-house deployments, hardware optimization, and technical optimizations like structured printing and knowledge distillation. They also covered latency optimization through libraries and model compression, and emphasized the importance of monitoring tail latencies, costs, and quality, while balancing user experience.
- [**New Computer**](https://www.zenml.io/llmops-database/enhancing-memory-retrieval-systems-using-langsmith-testing-and-evaluation) \- New Computer utilized LangSmith to refine the memory retrieval system of their AI assistant, Dot, achieving a 50% increase in recall and a 40% improvement in precision through synthetic data testing, comparison views, and prompt optimization, which led to a successful launch and a 45% conversion rate to their paid tier.
- [**New Relic**](https://www.zenml.io/llmops-database/observability-platform-s-journey-to-production-genai-integration) \- New Relic, a major observability platform, integrated GenAI for both internal operations and customer-facing products, achieving a 15% increase in developer productivity. Their implementation features a multi-agent architecture for internal tasks, automated incident management, and a three-layer AI architecture for their product offerings, emphasizing cost management through model selection, RAG, and careful monitoring.
- [**Nextdoor**](https://www.zenml.io/llmops-database/optimizing-email-engagement-using-llms-and-rejection-sampling) \- Nextdoor implemented an LLM-based system to optimize email subject lines, using prompt engineering with the OpenAI API and a fine-tuned reward model for engagement prediction, resulting in a 1% lift in sessions and a 0.4% increase in Weekly Active Users. The system employs rejection sampling, caching, and robust monitoring to ensure cost-effective and reliable performance.
- [**NICE**](https://www.zenml.io/llmops-database/natural-language-to-sql-system-with-production-safeguards-for-contact-center-analytics) \- NICE built a production-grade natural language to SQL system for querying contact center data, achieving 86% accuracy with robust safeguards like tenant isolation, query parameter management, and result visualization. The system also includes context management for follow-up questions, query caching, and validation against business rules to ensure reliable operation.
- [**NICE Actimize**](https://www.zenml.io/llmops-database/leveraging-vector-embeddings-for-financial-fraud-detection) \- NICE Actimize, a leader in financial fraud prevention, uses vector embeddings to enhance real-time fraud detection by transforming tabular transaction data into text and then into vector embeddings using a RoBERTa variant, enabling them to identify similar fraud patterns with sub-millisecond processing times. This approach maintains the high performance required for large-scale, real-time transaction analysis while preserving semantic meaning.
- [**NICE Actimize**](https://www.zenml.io/llmops-database/generative-ai-integration-in-financial-crime-detection-platform) \- NICE Actimize integrated generative AI into their “Excite” financial crime detection platform, enabling analysts to create analytical artifacts from natural language requests. This system automates the generation of aggregations, features, and models, with built-in validation pipelines and MLOps capabilities to ensure safe and efficient deployment.
- [**No company name**](https://www.zenml.io/llmops-database/error-handling-in-llm-systems) \- This case study examines the critical need for robust error handling and response validation when deploying LLMs in production, emphasizing a multi-layered approach including input validation, response processing with retry and fallback mechanisms, and comprehensive monitoring and logging. It also covers production considerations like scalability, error recovery, security, and documentation, highlighting the importance of continuous improvement and testing to ensure system reliability and a positive user experience.
- [**No company name is explicitly mentioned in the case study.**](https://www.zenml.io/llmops-database/building-and-testing-a-production-llm-powered-quiz-application) \- A trivia quiz application was transformed from a static database to a dynamic, LLM-powered system using Google’s Vertex AI, leveraging Gemini models for quiz generation and validation, achieving a significant accuracy improvement from 70% to 91%. The team implemented robust prompt engineering, testing, and validation frameworks, showcasing the practical application of LLMs in a production environment.
- [**No company name is mentioned in this case study.**](https://www.zenml.io/llmops-database/legacy-pdf-document-processing-with-llm) \- This case study details the use of LLMs to process complex legacy PDF documents, addressing challenges like binary data, stream compression, and intricate object relationships. The solution employs LLMs for intelligent text extraction, document understanding, and semantic analysis, creating a pipeline that includes pre-processing, decoding, content analysis, and post-processing.
- [**No company name mentioned**](https://www.zenml.io/llmops-database/enterprise-challenges-and-opportunities-in-large-scale-llm-deployment) \- This case study examines the challenges of deploying LLMs at scale, contrasting traditional MLOps with the emerging LLMOps, and emphasizes the need for new approaches to data handling, evaluation, and infrastructure, while recommending leveraging existing MLOps knowledge and adapting team structures for successful implementation. It also highlights the importance of cost management, change management, and clear ROI justification for large-scale LLM deployments.
- [**North Dakota University System**](https://www.zenml.io/llmops-database/policy-search-and-response-system-using-llms-in-higher-education) \- The North Dakota University System (NDUS) deployed a “Policy Assistant” using Llama 2 on Databricks’ Data Intelligence Platform to streamline policy document search across its 11 institutions, achieving a 10-20x speedup in search operations and reducing development time from one year to six months. This system, built on Azure, processes thousands of PDFs, creates vector embeddings for efficient search, and provides natural language query capabilities with citations, all while maintaining robust governance and security.
- [**Notion**](https://www.zenml.io/llmops-database/scaling-data-infrastructure-for-ai-features-and-rag) \- Notion, grappling with massive data growth, built a scalable data lake using S3, Spark, Kafka, and Debezium CDC with Apache Hudi for efficient change data capture, reducing data ingestion times from days to minutes/hours and saving over $1 million. This infrastructure enabled the rollout of Notion AI features, including their Search and AI Embedding RAG infrastructure.
- [**NTT Data**](https://www.zenml.io/llmops-database/genai-powered-work-order-management-system-poc) \- NTT Data partnered with a large infrastructure company to implement a GenAI-powered work order management system, using a privately hosted LLM and a custom knowledge base to automate classification, urgency assessment, and special handling identification for over 500,000 annual maintenance requests, improving accuracy and consistency compared to the previous manual approach. The system also provides reasoning explanations and audit trails, while prioritizing security and data privacy.
- [**Nubank / Harvey AI / Galileo / Convirza**](https://www.zenml.io/llmops-database/production-llm-systems-at-scale---lessons-from-financial-services-legal-tech-and-ml-infrastructure) \- A panel of leaders from Nubank, Harvey AI, Galileo, and Convirza discussed their experiences deploying LLMs in production, highlighting the shift from large proprietary models to optimized, specialized ones for cost and latency, emphasizing modular architectures and robust evaluation frameworks incorporating human feedback. They also covered sophisticated model selection based on quality, latency, cost, and technical debt, alongside cost management strategies like fine-tuning and optimized inference.
- [**Numbers Station**](https://www.zenml.io/llmops-database/building-production-ready-sql-and-charting-agents-with-rag-integration) \- Numbers Station developed a production-ready self-service analytics platform using LLMs, RAG, and a unified knowledge layer to address the bottleneck of data team requests, enabling users to generate SQL queries and charts through a multi-agent architecture with a focus on accuracy, scalability, and enterprise integration. Their system demonstrated significant improvements in real-world benchmarks, reducing setup time from weeks to hours while maintaining high accuracy through contextual knowledge integration.
- [**Numbers Station**](https://www.zenml.io/llmops-database/integrating-foundation-models-into-the-modern-data-stack-challenges-and-solutions) \- Numbers Station is integrating foundation models into the modern data stack to accelerate data insights, focusing on practical applications like natural language to SQL translation, data cleaning, and data linkage. They address challenges such as model scale and performance through techniques like model distillation and hybrid approaches, while tackling prompt brittleness with prompt ensembling and decomposition.
- [**NVIDIA**](https://www.zenml.io/llmops-database/security-learnings-from-llm-production-deployments) \- NVIDIA’s product security and AI red team share their experiences securing LLM deployments, highlighting real-world challenges with RAG systems and plugin architectures. The study identifies vulnerabilities such as data poisoning in RAG, prompt injection leading to SQL injection, and remote code execution through plugins, emphasizing the need for strict access controls, input validation, sandboxing, and careful logging strategies.
- [**NVIDIA**](https://www.zenml.io/llmops-database/automated-cve-analysis-and-remediation-using-event-driven-rag-and-ai-agents) \- NVIDIA’s Agent Morpheus uses four specialized Llama3 LLMs and AI agents in an event-driven architecture to automate CVE analysis and remediation, triggered by container uploads and integrating with multiple data sources to generate remediation plans and security documentation, achieving a 9.3x speedup through parallel processing. This system, deployed using NVIDIA NIM, reduces analysis time from hours/days to seconds and includes a human-in-the-loop feedback mechanism for continuous improvement.
- [**OLX**](https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture) \- OLX developed “OLX Magic,” an AI-powered shopping assistant for their secondhand marketplace, combining traditional keyword search with LLM-driven agents to handle natural language, multi-modal (text, image, voice), and modified visual searches. The system tackles e-commerce personalization and search refinement challenges, balancing user experience with technical constraints like latency and cost.
- [**OLX**](https://www.zenml.io/llmops-database/automating-job-role-extraction-using-prosus-ai-assistant-in-production) \- OLX implemented a production system using the Prosus AI Assistant to automate job role extraction from listings, processing 2,000 daily updates with 4,000 API calls, and using LangChain for prompt engineering; initial A/B tests showed positive results, but the $15K monthly cost is driving a potential shift to self-hosted models.
- [**ONE**](https://www.zenml.io/llmops-database/from-sms-to-ai-lessons-from-5-years-of-chatbot-development-for-social-impact) \- ONE’s chatbot initiative, deployed across Facebook Messenger and WhatsApp, reached over 38,000 users in six African countries, facilitating campaign engagement and generating over 17,000 user actions using RapidPro, ActionKit CRM, and Google BigQuery; key learnings included the importance of iterative development and localized language support, while challenges included platform restrictions and varying user acquisition costs.
- [**OpenAI**](https://www.zenml.io/llmops-database/building-analytics-applications-with-llms-for-e-commerce-review-analysis) \- This case study demonstrates how LLMs can streamline e-commerce review analysis by replacing traditional machine learning workflows with a single model capable of multi-task analysis, including sentiment analysis, aspect extraction, and topic clustering, using OpenAI’s API and carefully engineered prompts. This approach enhances efficiency, reduces development time, and provides improved explainability compared to traditional black-box models.
- [**OpenAI / AWS**](https://www.zenml.io/llmops-database/deploying-llm-based-recommendation-systems-in-private-equity) \- A private equity firm successfully deployed an LLM-based recommendation system, leveraging OpenAI APIs for data cleaning and text embeddings, and AWS for deployment, focusing on practical implementation and addressing challenges in data quality and resource management. The system prioritizes relevant recommendations within the first five suggestions for a boomer-generation user base.
- [**OpenGPA / Microsoft Research**](https://www.zenml.io/llmops-database/exploring-rag-limitations-with-movie-scripts-the-copernicus-challenge) \- OpenGPA’s study reveals the limitations of standard RAG when processing context-rich documents like movie scripts, showing how basic chunking and vector search fail to capture temporal and relational context, leading to inaccurate answers; while Graph RAG offers improvements, the study emphasizes the need for advanced context management techniques and proposes a movie script benchmark for evaluating RAG systems.
- [**OpenRecovery**](https://www.zenml.io/llmops-database/multi-agent-architecture-for-addiction-recovery-support) \- OpenRecovery developed a multi-agent system using LangGraph to provide AI-powered addiction recovery support, featuring specialized agents, shared state, and dynamic context switching. Deployed via LangGraph Platform, the system integrates with mobile apps and uses LangSmith for observability and testing, while incorporating human-in-the-loop verification to ensure accuracy and empathy.
- [**Orizon**](https://www.zenml.io/llmops-database/automating-healthcare-documentation-and-rule-management-with-genai) \- Orizon, a healthcare platform, automated 63% of their medical rule documentation tasks by implementing a GenAI solution using Databricks, fine-tuning Llama2-code and DBRX models, and deploying them through Mosaic AI Model Serving, while maintaining strict security and governance. This reduced documentation time to under 5 minutes and freed up developer resources, demonstrating the potential of LLMs in regulated industries.
- [**PagerDuty**](https://www.zenml.io/llmops-database/rapid-development-and-deployment-of-enterprise-llm-features-through-centralized-llm-service-architecture) \- PagerDuty rapidly deployed multiple GenAI features, including AI-powered runbook generation and incident summarization, within two months by adopting a centralized LLM API service built on Kubernetes. This architecture enabled them to quickly iterate on new features, manage multiple LLM providers, and maintain robust security and monitoring.
- [**Paradigm**](https://www.zenml.io/llmops-database/scaling-parallel-agent-operations-with-langchain-and-langsmith-monitoring) \- Paradigm, a YC24 company, built an AI-powered spreadsheet platform using LangChain to develop specialized agents for tasks like schema generation and task planning, while leveraging LangSmith for monitoring and usage-based pricing, enabling them to manage thousands of parallel agents efficiently. This combination of tools allowed them to optimize costs and maintain high performance in their production environment.
- [**Parameta Solutions**](https://www.zenml.io/llmops-database/automated-email-triage-system-using-amazon-bedrock-flows) \- Parameta Solutions implemented an automated email triage system using Amazon Bedrock Flows, processing client requests by classifying emails, extracting entities, and generating responses, integrating with data sources like Snowflake and OpenSearch. This system reduced resolution times from weeks to days, showcasing a practical application of LLMs in a regulated financial environment.
- [**Paramount+**](https://www.zenml.io/llmops-database/video-content-summarization-and-metadata-enrichment-for-streaming-platform) \- Paramount+ partnered with Google Cloud to implement Gen AI for video summarization and metadata enrichment, processing over 50,000 videos using techniques like prompt chaining and model fine-tuning to improve content discoverability and reduce reliance on manual processes and third-party services. The system includes a three-component architecture for transcription, content generation, and personalization integration, optimizing for token limits and model selection.
- [**Parcha**](https://www.zenml.io/llmops-database/building-production-ready-ai-agents-for-enterprise-operations) \- Parcha is developing AI agents for enterprise operations and compliance, particularly in fintech, moving from LangChain to a custom framework for better control and debugging, using Claude as their primary LLM. Their approach focuses on breaking down complex workflows into smaller, manageable components with a hierarchical agent structure, emphasizing controlled execution of pre-defined procedures, achieving 90% accuracy before deployment, and providing transparency into agent decision-making.
- [**Parcha**](https://www.zenml.io/llmops-database/building-production-grade-ai-agents-with-distributed-architecture-and-error-recovery) \- Parcha built a production-grade AI agent system for compliance and operations, transitioning from a basic Langchain setup to a distributed architecture with asynchronous processing and a coordinator-worker pattern, addressing issues like context pollution and unreliable connections. Their solution incorporates robust error handling with queue-based execution, self-correction, and automated reporting, alongside a modular tool framework for easy integration and scalability.
- [**Parlance Labs / GitHub**](https://www.zenml.io/llmops-database/practical-llm-deployment-from-evaluation-to-fine-tuning) \- Parlance Labs, leveraging experience from GitHub Copilot, advocates for a practical LLM deployment approach centered on rigorous evaluation, data-centric strategies, and iterative development, including multi-level evaluation frameworks and instruction tuning. Their work, demonstrated in a real estate CRM integration, emphasizes data quality, robust evaluation systems, and human oversight, while addressing infrastructure and scalability challenges.
- [**Patronus AI**](https://www.zenml.io/llmops-database/training-and-deploying-advanced-hallucination-detection-models-for-llm-evaluation) \- Patronus AI developed Lynx, a specialized hallucination detection model, by fine-tuning Llama-3-70B-Instruct on their HaluBench dataset using Databricks’ Mosaic AI infrastructure, achieving a 1% accuracy improvement over GPT-4 in hallucination detection and open-sourcing the model and dataset. Leveraging LLM Foundry and Composer for training optimizations like FSDP and Flash Attention, they demonstrated significant gains in domain-specific areas like medical question answering.
- [**Perplexity**](https://www.zenml.io/llmops-database/building-a-production-grade-llm-orchestration-system-for-conversational-search) \- Perplexity built a production-grade conversational search engine using multiple LLMs, including GPT-4 and custom models, optimized for low latency and high-quality results. Their system combines search indices, tools, and custom embeddings to deliver personalized, accurate responses at scale, while also focusing on reliability and maintainability with a small, efficient engineering team.
- [**Perplexity**](https://www.zenml.io/llmops-database/building-a-complex-ai-answer-engine-with-multi-step-reasoning) \- Perplexity’s Pro Search is an advanced AI answer engine that tackles complex queries using multi-step reasoning, separating planning and execution phases, and integrating tools like code interpreters and Wolfram Alpha. This approach, combined with a user-friendly interface, has led to a 50% increase in query search volume.
- [**Perplexity AI**](https://www.zenml.io/llmops-database/scaling-an-ai-powered-search-and-research-assistant-from-prototype-to-production) \- Perplexity AI transitioned from internal SQL tools to a production-ready AI search and research assistant, iteratively developing from Slack and Discord bots to a web interface. They tackled challenges in search relevance, model selection, latency, and cost by implementing a hybrid approach using fine-tuned GPT models and custom LLaMA-based models, achieving superior performance metrics in citation accuracy and perceived utility compared to competitors.
- [**PeterCat.ai**](https://www.zenml.io/llmops-database/building-and-deploying-repository-specific-ai-assistants-for-github) \- [PeterCat.ai](http://petercat.ai/) developed a system that creates customized AI assistants for GitHub repositories, using LLMs and RAG to improve code review and issue management, and deploying it as a GitHub App. The system, adopted by 178 open source projects, leverages LangChain for orchestration, a vector database for knowledge storage, and AWS Lambda for asynchronous processing.
- [**Philadelphia Union**](https://www.zenml.io/llmops-database/rag-powered-chatbot-for-sports-team-roster-management) \- The Philadelphia Union utilized a RAG architecture on Databricks, incorporating Vector Search and the DBRX Instruct model, to create a chatbot that simplifies complex MLS roster rules, enabling faster decision-making and ensuring compliance. Deployed via Databricks Apps, the system showcases robust LLMOps practices, including thorough testing, monitoring, and governance.
- [**Picnic**](https://www.zenml.io/llmops-database/enhancing-e-commerce-search-with-llm-powered-semantic-retrieval) \- Picnic, a grocery delivery platform, implemented an LLM-powered search system using GPT-3.5-turbo and OpenAI’s text-embedding-3-small model to improve product discovery across multiple languages, leveraging OpenSearch for efficient retrieval and precomputed embeddings with caching to maintain low latency. This system effectively handles multilingual queries, typos, and varied user intents while maintaining the speed and reliability required for e-commerce applications.
- [**Pinterest**](https://www.zenml.io/llmops-database/safe-implementation-of-ai-assisted-development-with-github-copilot) \- Pinterest successfully rolled out GitHub Copilot for AI-assisted development, emphasizing a secure and compliant approach through a large-scale trial and cross-functional collaboration, achieving 35% adoption within six months. Their methodical implementation included robust security measures, integration with existing workflows, and a focus on developer experience, resulting in positive feedback, particularly for cross-language development.
- [**Pinterest**](https://www.zenml.io/llmops-database/text-to-sql-system-with-rag-enhanced-table-selection) \- Pinterest built a Text-to-SQL system within their Querybook tool, initially using an LLM for SQL generation and later enhancing it with RAG for table selection, improving task completion speed by 35% and first-shot acceptance rates from 20% to over 40%. The system leverages technologies like Langchain for JSON parsing, OpenSearch for vector storage, and WebSocket streaming to handle long response times, demonstrating a practical approach to deploying LLMs in a production environment.
- [**Podium**](https://www.zenml.io/llmops-database/optimizing-agent-behavior-and-support-operations-with-langsmith-testing-and-observability) \- Podium, a communication platform for small businesses, utilized LangSmith to optimize their AI Employee agent, achieving a 98.6% F1 score in response quality through comprehensive testing and dataset management, while also reducing engineering intervention by 90%. This LLMOps approach empowered their Technical Product Specialists to independently troubleshoot issues, improving overall customer satisfaction.
- [**Podzy / The Learning Agency Lab / Vanderbilt’s LEER Lab**](https://www.zenml.io/llmops-database/llm-applications-in-education-personalized-learning-and-assessment-systems) \- Educational organizations are integrating LLMs and LangChain to create enhanced learning experiences, with Podzy building a spaced repetition system with LLM-powered question generation, The Learning Agency Lab focusing on datasets and competitions for LLM educational applications, and Vanderbilt’s LEER Lab developing intelligent textbooks using LLMs for content summarization and question generation. These implementations highlight the integration of LLMs with existing educational tools while addressing challenges of accuracy, personalization, and fairness.
- [**PredictionGuard**](https://www.zenml.io/llmops-database/comprehensive-security-and-risk-management-framework-for-enterprise-llm-deployments) \- PredictionGuard’s framework provides a comprehensive approach to securing enterprise LLM deployments, addressing challenges like hallucinations with factual consistency models and RAG, supply chain risks with trusted registries, and prompt injection attacks using custom filtering. The framework also emphasizes data privacy through PII detection and confidential computing, while maintaining performance and integrating with existing enterprise systems.
- [**Prem AI**](https://www.zenml.io/llmops-database/optimizing-production-vision-pipelines-for-planet-image-generation) \- Prem AI optimized their production vision pipelines to generate millions of realistic ethereal planet images using Stable Diffusion XL, fine-tuning the model with a curated dataset and implementing a custom multi-stage upscaling pipeline. They further optimized performance through techniques like LoRA fusion, model quantization, and efficient serving with Ray Serve, resulting in consistent high-quality image generation with specific aspect ratios and controllable attributes.
- [**Principal Financial Group**](https://www.zenml.io/llmops-database/enterprise-wide-rag-implementation-with-amazon-q-business) \- Principal Financial Group implemented an enterprise-wide RAG solution using Amazon Q Business, enabling their customer service team to efficiently query over 9,000 pages of work instructions, achieving 84% accuracy in document retrieval and a 50% reduction in some workloads. The project highlights the importance of metadata quality, user training, and strong governance frameworks in successful LLM deployments.
- [**PromptOps / Insight Partners / Meta / Stripe**](https://www.zenml.io/llmops-database/panel-discussion-on-building-production-llm-applications) \- A panel of experts from PromptOps, Insight Partners, Meta, and Stripe shared practical insights on deploying LLMs in production, covering topics like managing hallucinations, prompt engineering techniques, latency optimization, and evaluation strategies, while also emphasizing cost considerations and the importance of continuous feedback loops. The discussion highlighted the need for robust infrastructure, risk management, and a pragmatic approach to model selection, including the use of open-source alternatives.
- [**Prosus**](https://www.zenml.io/llmops-database/plus-one-internal-llm-platform-for-cross-company-ai-adoption) \- Prosus developed Plus One, an internal LLM platform accessible via Slack, to democratize AI adoption across their diverse portfolio of companies. The platform supports multiple LLMs and RAG, serving thousands of users with over half a million queries spanning software development, product management, and general business tasks. Through iterative optimization, they’ve reduced hallucination rates to below 2% and implemented cost-saving measures like token economy and strategic model selection, enabling both technical and non-technical users to leverage AI effectively.
- [**Prosus / OLX**](https://www.zenml.io/llmops-database/agent-based-ai-assistants-for-enterprise-and-e-commerce-applications) \- Prosus has deployed two key AI agent applications: Toan, an enterprise assistant used by over 15,000 employees across 24 companies, and OLX Magic, an e-commerce assistant integrated into their marketplace, with Toan achieving a reduction in hallucinations from 10% to 1% and saving users an average of 48 minutes per day, while OLX Magic leverages similar agent technology to enhance product discovery through generative AI features.
- [**Q4 Inc.**](https://www.zenml.io/llmops-database/sql-generation-and-rag-for-financial-data-q-a-chatbot) \- Q4 Inc. developed a financial data Q&A chatbot for Investor Relations Officers, using Amazon Bedrock and a novel RAG approach that leverages LLMs to generate SQL queries against financial datasets, achieving high accuracy and single-digit second response times. The system uses multiple foundation models through Amazon Bedrock for different tasks (SQL generation, validation, summarization) optimized for performance and cost.
- [**Qatar Computing Research Institute**](https://www.zenml.io/llmops-database/t-rag-tree-based-rag-architecture-for-question-answering-over-organizational-documents) \- Qatar Computing Research Institute developed T-RAG, an on-premise question-answering system for confidential organizational documents, combining RAG with a fine-tuned Llama-2 7B model and a custom tree-based entity structure, achieving 73% accuracy and robust entity tracking. This approach demonstrates the benefits of combining multiple techniques for production LLM applications, while also addressing the constraints of limited resources and on-premise requirements.
- [**QualIT**](https://www.zenml.io/llmops-database/llm-enhanced-topic-modeling-system-for-qualitative-text-analysis) \- QualIT has developed an LLM-enhanced topic modeling system that combines LLMs for key phrase extraction with a two-stage hierarchical clustering approach, achieving a 70% topic coherence and 95.5% topic diversity, outperforming LDA and BERTopic benchmarks, while also implementing a robust hallucination detection framework. This system has been validated through human evaluation, demonstrating its practical utility for analyzing large volumes of text data from sources like surveys and customer feedback.
- [**QuantumBlack**](https://www.zenml.io/llmops-database/llm-applications-in-drug-discovery-and-call-center-analytics) \- QuantumBlack developed two LLM-powered systems: a molecular discovery platform using chemical language models and RAG for pharmaceutical research, and a call center analytics solution that processes audio with diarization, transcription, and LLM analysis, achieving a 60x speedup through optimizations. The call center system uses a pipeline including Whisper for transcription and a quantized Mistral 7B model for analysis.
- [**QuantumBlack**](https://www.zenml.io/llmops-database/data-engineering-challenges-and-best-practices-in-llm-production) \- QuantumBlack’s data engineers share their practical experiences implementing LLMs in production, addressing challenges around unstructured data, data quality, and privacy, while also exploring how LLMs can assist with tasks like pipeline development and synthetic data creation. They emphasize the importance of human oversight, risk mitigation, and careful evaluation when integrating LLMs into enterprise data workflows.
- [**Rakuten**](https://www.zenml.io/llmops-database/building-enterprise-scale-ai-applications-with-langchain-and-langsmith) \- Rakuten Group implemented LangChain and LangSmith to create a suite of AI applications, including AI Analyst, AI Agent, and AI Librarian, for both clients and employees; they also built an internal chatbot platform using OpenGPTs, enabling rapid development and deployment while maintaining enterprise-grade security and scalability.
- [**Ramp**](https://www.zenml.io/llmops-database/ai-powered-tour-guide-for-financial-platform-navigation) \- Ramp built an AI-powered Tour Guide agent that uses a visible cursor and step-by-step explanations to guide users through their financial platform, employing an iterative action generation system and optimized prompts. The system prioritizes human-agent collaboration, ensuring user trust through transparent actions and clear feedback, while also focusing on performance optimization and safety through guardrails and controlled interaction spaces.
- [**Rasgo**](https://www.zenml.io/llmops-database/production-lessons-from-building-and-deploying-ai-agents) \- Rasgo’s platform for AI-powered data analysis agents emphasizes database interactions and custom agent creation, highlighting the importance of a well-designed agent-computer interface and the impact of base model selection, with GPT-4 outperforming GPT-3.5 for complex tasks. Their experience underscores the necessity of robust production infrastructure, focusing on reasoning capabilities, and avoiding unnecessary abstractions for successful LLM deployment, alongside careful attention to security, error handling, and performance optimization.
- [**RealChar**](https://www.zenml.io/llmops-database/building-a-production-ready-ai-phone-call-assistant-with-multi-modal-processing) \- RealChar is developing an AI phone call assistant for customer service, utilizing a multi-modal processing system inspired by self-driving car architectures, with real-time audio processing and millisecond-level tracing. The system employs an event bus for parallel processing, fallback mechanisms for managing variable LLM response times, and a tiered model system for speed and accuracy tradeoffs, all while prioritizing reliability and real-time performance monitoring.
- [**Realtime**](https://www.zenml.io/llmops-database/automated-data-journalism-platform-using-llms-for-real-time-news-generation) \- Realtime built an automated data journalism platform using LLMs to generate news stories from real-time data, employing a multi-stage pipeline with GPT-4 Turbo and focusing on quality control, cost optimization, and transparency. The platform processes diverse data sources, constructs dynamic prompts, and implements safeguards against common LLM errors, demonstrating a practical approach to deploying LLMs in a production news environment.
- [**Reddit**](https://www.zenml.io/llmops-database) \- A network security block page, while seemingly simple, can be enhanced with LLMs for user authentication, ticket management, and security monitoring, requiring robust backend infrastructure and careful attention to data privacy and model security. Future improvements could include enhanced security features, user experience enhancements, and broader integration capabilities.
- [**Renovai**](https://www.zenml.io/llmops-database/building-production-ready-llm-agents-with-state-management-and-workflow-engineering) \- Renovai’s R&D team presented their approach to building production-ready LLM agents, detailing state management, workflow engineering, and multi-agent systems. Their work includes practical implementation patterns like Router + Code and state machines, along with advanced techniques such as multimodal agents using GPT-4V for web navigation, emphasizing the importance of robust state management and clear workflow design.
- [**Replit**](https://www.zenml.io/llmops-database/building-reliable-multi-agent-systems-for-application-development) \- Replit’s multi-agent system enhances application development by using specialized agents for workflow management, coding, and user interaction, emphasizing reliability and user engagement. They leverage advanced prompt engineering, a custom DSL for tool invocation, and robust observability via LangSmith, enabling a user-friendly experience with flexible engagement levels and a focus on real-time monitoring and trace analysis.
- [**Replit**](https://www.zenml.io/llmops-database/building-and-deploying-a-code-generation-llm-at-scale) \- Replit, a browser-based IDE platform, utilized Databricks’ Mosaic AI Training to rapidly develop and deploy a custom code completion LLM, scaling from smaller models to a multi-billion parameter model in just three weeks. This allowed them to deploy a production-ready code generation system to their 25 million users, demonstrating the feasibility of rapid LLM deployment with a small team by abstracting away infrastructure complexity.
- [**Replit**](https://www.zenml.io/llmops-database/building-and-scaling-production-code-agents-lessons-from-replit) \- Replit’s development of their AI-powered code agent involved navigating challenges such as defining diverse user needs, implementing robust failure detection using rollback tracking and sentiment analysis, and creating custom evaluation harnesses beyond generic benchmarks. The team scaled from 3 to 20 engineers, integrating traditional engineering practices with LLM-specific expertise, and deployed features like “rapid build mode” that significantly reduced application setup time.
- [**Replit**](https://www.zenml.io/llmops-database/advanced-agent-monitoring-and-debugging-with-langsmith-integration) \- Replit, a platform for over 30 million developers, integrated LangSmith to improve the observability of their complex AI agent system, Replit Agent, built on LangGraph, addressing challenges in handling large-scale trace data, enabling efficient debugging through within-trace search, and introducing thread views for monitoring human-in-the-loop interactions. This resulted in faster debugging, better system understanding, and enhanced human-AI collaboration.
- [**Replit**](https://www.zenml.io/llmops-database/optimizing-llm-server-startup-times-for-preemptable-gpu-infrastructure) \- Replit optimized their LLM infrastructure by using preemptable GPUs, achieving a 66% cost reduction by reducing server startup time from 18 minutes to under 2 minutes through container optimization, GKE image streaming, and improved model loading.
- [**Replit**](https://www.zenml.io/llmops-database/building-reliable-ai-agents-for-application-development-with-multi-agent-architecture) \- Replit developed Replit Agent, a multi-agent AI system, to streamline application development, using specialized agents for managing, editing, and verifying code. The system incorporates a custom DSL, advanced prompt engineering, and Claude 3.5 Sonnet, alongside comprehensive monitoring and version control, ensuring reliability and user control.
- [**Replit**](https://www.zenml.io/llmops-database/building-a-production-ready-multi-agent-coding-assistant) \- Replit developed a multi-agent coding assistant that allows users to create software applications without writing code, using a system of specialized agents for managing, editing, and verifying code, and leveraging GPT-3.5 Turbo for code generation. The system has seen hundreds of thousands of production runs, prioritizing user engagement and feedback, and achieving a 90% success rate in tool invocations through techniques like code-based tool calls and state replay for debugging.
- [**Replit**](https://www.zenml.io/llmops-database/building-production-ready-llms-for-automated-code-repair-a-scalable-ide-integration-case-study) \- Replit built an automated code repair system directly into their IDE, using a fine-tuned 7B parameter LLM to fix Python errors identified by LSP diagnostics, achieving performance comparable to much larger models like GPT-4 and Claude-3. The production system features low-latency inference, load balancing, and real-time code application, demonstrating successful deployment of an LLM in a demanding development environment.
- [**Resides**](https://www.zenml.io/llmops-database/panel-discussion-real-world-llm-production-use-cases) \- A panel discussion highlighted real-world LLM production use cases, including Resides achieving 95-99% question answering rates in property management by processing unstructured documents, and sales optimization with a 30% improvement through argument analysis, alongside structured output validation for executive coaching. The discussion emphasized avoiding over-engineering, focusing on quick iterations, and prioritizing user value, while also covering data management with vector databases and human-in-the-loop workflows.
- [**Revolut / Seen.it**](https://www.zenml.io/llmops-database/vector-search-and-rag-implementation-for-enhanced-user-search-experience) \- Revolut’s Sherlock fraud detection system uses vector search to identify anomalous transactions in under 50ms, achieving a 96% fraud detection rate and saving customers over $3 million annually, while [Seen.it](http://seen.it/) leverages vector embeddings for natural language video search across half a million clips, enhancing content discovery and marketing workflows. These case studies demonstrate the practical application of vector search and RAG in production, emphasizing performance optimization and user-centric design.
- [**Rexera**](https://www.zenml.io/llmops-database/evolving-quality-control-ai-agents-with-langgraph) \- Rexera, a real estate transaction company, improved its quality control by moving from single-prompt LLMs to a LangGraph-based system, achieving significant accuracy gains by implementing structured decision paths and reducing false positives from 8% to 2% and false negatives from 5% to 2%. This evolution highlights the importance of choosing the right architecture for complex LLM workflows.
- [**Roche Diagnostics / John Snow Labs**](https://www.zenml.io/llmops-database/building-healthcare-specific-llm-pipelines-for-oncology-patient-timelines) \- Roche Diagnostics, in collaboration with John Snow Labs, built a production system using healthcare-specific LLMs to extract and structure oncology patient timelines from unstructured clinical notes, leveraging a pipeline that includes OCR, NLP, and LLMs to process diverse medical documents and extract key entities. The system uses zero-shot learning with structured prompts to address challenges like data complexity and ethical considerations, demonstrating the potential of LLMs to automate data extraction and improve the accuracy of medical timeline creation.
- [**Rolls-Royce / Databricks**](https://www.zenml.io/llmops-database/optimizing-engineering-design-with-conditional-gans) \- Rolls-Royce employed conditional GANs on the Databricks platform to optimize engineering design, enabling the generation of new design concepts from simulation data, bypassing traditional modeling. This implementation, focusing on data modeling, cGAN architecture, and MLOps, resulted in faster design iterations and reduced costs while maintaining strict compliance.
- [**Rolls-Royce / Databricks**](https://www.zenml.io/llmops-database/cloud-based-generative-ai-for-preliminary-engineering-design) \- Rolls-Royce, in collaboration with Databricks and the University of Southampton, developed a cloud-based generative AI system using GANs to accelerate preliminary engineering design, encoding design parameters into images and validating them through physics-based simulations, achieving significant training time reductions and implementing robust data governance. The team also discovered that CPU training sometimes outperformed GPU training for specific validation tasks, highlighting the importance of workload-specific optimization.
- [**Runway**](https://www.zenml.io/llmops-database/multimodal-feature-stores-and-research-engineering-collaboration) \- Runway, a pioneer in generative AI for creative tools, implemented a “multimodal feature store” to manage diverse data types like video, images, and text, along with pre-computed features and embeddings, enabling efficient distributed training and improved collaboration between research and engineering teams. This system facilitates semantic queries, efficient batch access, and integrates with existing ML infrastructure, leading to faster iteration cycles for model development.
- [**Salesforce**](https://www.zenml.io/llmops-database/building-and-scaling-production-ready-ai-agents-lessons-from-agent-force) \- Salesforce’s Agent Force platform facilitates the creation and deployment of AI agents, addressing the challenges of transitioning LLMs from proof-of-concept to production by emphasizing robust testing, evaluation, and monitoring, including automated pipelines, synthetic data, and iterative testing. The case study highlights the importance of strategic fine-tuning, RAG pipeline optimization, and cost management, while also considering brand voice consistency and data privacy in enterprise environments.
- [**Salesforce**](https://www.zenml.io/llmops-database/ai-powered-slack-conversation-summarization-system) \- Salesforce AI Research developed AI Summarist, a production-grade LLM system integrated with Slack, to tackle information overload by providing on-demand and scheduled summaries of conversations, channels, and threads using state-of-the-art conversational AI, with a zero-storage architecture for privacy and features like conversation disentanglement and context-aware summarization. The system also includes user feedback loops for continuous improvement and is designed with safeguards like rate limiting and error handling.
- [**Salesforce**](https://www.zenml.io/llmops-database) \- Salesforce’s Agentforce Service Agent leverages LLMs and CRM data to create an autonomous AI agent that enhances traditional chatbot interactions by providing intelligent, context-aware responses and actions grounded in company data, with quick deployment, privacy guardrails, and seamless escalation to human agents.
- [**Salesforce**](https://www.zenml.io/llmops-database/large-scale-enterprise-copilot-deployment-lessons-from-einstein-copilot-implementation) \- Salesforce’s internal deployment of Einstein Copilot demonstrates a large-scale enterprise LLM implementation, emphasizing a phased rollout starting with standard actions before introducing custom capabilities. The deployment included a comprehensive testing framework, custom prompt templates, and specialized business-specific actions, with a focus on data privacy and continuous model evaluation.
- [**Salesforce**](https://www.zenml.io/llmops-database/enterprise-scale-llm-integration-into-crm-platform) \- Salesforce’s Einstein GPT, a generative AI system for CRM, integrates LLMs across sales, service, marketing, and development, providing features like automated email composition, content and code generation, and data analysis, all while maintaining strict data privacy and security controls. The system includes human-in-the-loop validation and per-tenant model deployment, addressing challenges in data management, integration, and production deployment to improve efficiency and response times.
- [**Sam / Div / Devin**](https://www.zenml.io/llmops-database/production-agents-routing-testing-and-browser-automation-case-studies) \- Three engineers detail their production LLM agent deployments: Sam’s personal assistant uses real-time feedback and template-based routing, Div’s Milton automates browsers with multimodal capabilities and performance optimizations, and Devin’s agent assists engineers with code understanding via background indexing and knowledge graphs. These case studies highlight practical strategies for model selection, testing, performance, and routing in production environments.
- [**Sam / Div / Devin**](https://www.zenml.io/llmops-database/production-agents-real-world-implementations-of-llm-powered-autonomous-systems) \- A panel of engineers shared their experiences deploying LLM-powered agents, detailing use cases like a personal assistant with real-time feedback, a browser automation system, and a GitHub repository assistant, emphasizing routing layers, performance optimization, and real-time feedback mechanisms, while also addressing testing challenges and production considerations. The discussion highlighted practical approaches to model selection, error handling, and monitoring, offering insights into building reliable and efficient LLM-based systems.
- [**Santalucía Seguros**](https://www.zenml.io/llmops-database/enterprise-rag-based-virtual-assistant-with-llm-evaluation-pipeline) \- Santalucía Seguros utilizes a RAG-based Virtual Assistant, integrated with Microsoft Teams, to provide insurance agents with quick access to product information. The system, built on Databricks and Azure, features an LLM-as-judge evaluation system within its CI/CD pipeline to ensure consistent quality and prevent regressions.
- [**Schneider Electric**](https://www.zenml.io/llmops-database/retrieval-augmented-llms-for-real-time-crm-account-linking) \- Schneider Electric implemented a RAG system using LangChain and the Flan-T5-XXL model on SageMaker to automate CRM account linking, integrating real-time data from Google Search and SEC filings, and improving accuracy from 55% to 71% with domain-specific prompts. This solution significantly reduced manual processing time for account teams by identifying parent-subsidiary relationships.
- [**SEGA Europe**](https://www.zenml.io/llmops-database/large-language-models-for-game-player-sentiment-analysis-and-retention) \- SEGA Europe implemented a production LLM-based sentiment analysis system on Databricks, processing over 10,000 daily user reviews to improve player retention by up to 40% in some titles. The system leverages Delta Lake, Lakehouse Federation, and Unity Catalog to unify data and provide real-time feedback loops, while also democratizing access to AI insights through natural language interfaces.
- [**Shortwave**](https://www.zenml.io/llmops-database/building-an-ai-powered-email-writing-assistant-with-personalized-style-matching) \- Shortwave’s Ghostwriter uses vector embeddings and a fine-tuned LLM to generate email drafts that match a user’s writing style, incorporating relevant information from past emails via semantic search. The system addresses challenges like style matching through fine-tuning and information accuracy by integrating with AI search and using carefully crafted training examples.
- [**Sinch**](https://www.zenml.io/llmops-database/four-critical-lessons-from-building-50-global-chatbots-a-practitioner-s-guide-to-real-world-implementation) \- Sinch’s experience building over 50 global chatbots reveals that these projects should be treated as AI initiatives, not traditional IT projects, emphasizing the need for a “99-intents” approach to handle out-of-scope queries, hierarchical intent organization, and robust error handling, aiming for 90-95% recognition rates through continuous optimization.
- [**Singapore government**](https://www.zenml.io/llmops-database/building-a-modern-search-engine-for-parliamentary-records-with-rag-capabilities) \- The Singapore government developed Pair Search, a modern search engine for Parliamentary records, using a hybrid approach combining keyword, BM25, and semantic search with e5 embeddings, followed by ColbertV2 reranking. Designed for both human users and as a RAG backend, the system has seen positive feedback from government users, with around 150 daily users and 200 daily searches, demonstrating improved search result quality and performance.
- [**Slack**](https://www.zenml.io/llmops-database/automated-evaluation-framework-for-llm-powered-features) \- Slack’s engineering team developed a multi-tiered evaluation framework for their LLM-powered features like message summarization and natural language search, using golden sets, validation sets, and A/B testing, alongside automated quality metrics to assess hallucination, accuracy and system integration, enabling rapid iteration and continuous improvement. This systematic approach ensures quality standards are maintained throughout the development lifecycle of their generative AI products.
- [**Slack**](https://www.zenml.io/llmops-database/building-a-generic-recommender-system-api-with-privacy-first-design) \- Slack developed a generic recommendation API for internal use, prioritizing privacy and ease of integration by abstracting away ML complexities. They achieved a 10% improvement over hand-tuned models by focusing on interaction patterns rather than message content, demonstrating the effectiveness of a privacy-first, vertically integrated ML team.
- [**Slack**](https://www.zenml.io/llmops-database/building-secure-and-private-enterprise-llm-infrastructure) \- Slack implemented AI features using a secure architecture that ensures customer data privacy and compliance by hosting LLMs in their VPC with AWS SageMaker, using RAG instead of fine-tuning, and maintaining strict data access controls, resulting in 90% of AI-adopting users reporting increased productivity while maintaining enterprise-grade security and compliance.
- [**Smart Business Analyst**](https://www.zenml.io/llmops-database/smart-business-analyst-automating-competitor-analysis-in-medical-device-procurement) \- A procurement team built “Smart Business Analyst,” an LLM-powered system that automates competitor analysis for medical devices, using a multi-agent architecture to extract data from diverse sources, perform precise numerical comparisons, and generate structured reports with visualizations, significantly reducing analysis time. The system incorporates real-time data updates, multilingual support, conversational memory, and source attribution, addressing the limitations of general-purpose LLMs in specialized industry contexts.
- [**Smith.ai**](https://www.zenml.io/llmops-database/integrating-live-staffed-ai-chat-with-llm-powered-customer-service) \- [Smith.ai](http://smith.ai/) enhanced their customer engagement platform by integrating LLMs into their chat system, creating a hybrid approach that combines AI automation with human oversight. This system uses a custom-tuned LLM and RAG architecture to provide context-aware responses, with seamless transitions between AI and human agents, resulting in improved customer experience and operational efficiency.
- [**Spotify**](https://www.zenml.io/llmops-database/llm-powered-personalized-music-recommendations-and-ai-dj-commentary) \- Spotify utilized Meta’s Llama models to enhance music recommendations with contextual explanations and power their AI DJ feature, achieving a 4x increase in user engagement and a 14% improvement in Spotify-specific tasks through domain adaptation, multi-task fine-tuning, and a human-in-the-loop process, scaling to millions of users using vLLM for efficient serving.
- [**Stack Overflow**](https://www.zenml.io/llmops-database/building-a-knowledge-as-a-service-platform-with-llms-and-developer-community-data) \- Stack Overflow is leveraging its massive collection of 60 million Q&A posts and 40 billion tokens of technical data to build a Knowledge as a Service platform, offering real-time API access to curated content and improving LLM accuracy by 20% through fine-tuning, while also integrating semantic search and conversational AI. This approach enables them to enhance developer workflows and maintain community engagement through strategic partnerships with major AI companies.
- [**Stackblitz / Qodo**](https://www.zenml.io/llmops-database/scaling-ai-powered-code-generation-in-browser-and-enterprise-environments) \- Stackblitz’s Bolt.new achieved rapid growth with its browser-based AI code generation, leveraging a custom WebContainer OS for efficient in-browser execution and detailed error context for the LLM, while Qodo tackles enterprise code testing and review, supporting diverse deployment options and employing specialized models and sophisticated flow engineering techniques. Both companies demonstrate different approaches to productionizing LLMs, highlighting the importance of context management, error handling, and task decomposition.
- [**Stanford**](https://www.zenml.io/llmops-database/automating-enterprise-workflows-with-foundation-models-in-healthcare) \- Stanford researchers developed aCLAr, a system leveraging multimodal foundation models to automate enterprise workflows, with a focus on healthcare. The system uses a “Demonstrate, Execute, Validate” framework, passively learning from user demonstrations, interacting with UIs visually, and incorporating self-monitoring.
- [**Stripe**](https://www.zenml.io/llmops-database/building-an-llm-powered-support-response-system) \- Stripe built an LLM-powered system to provide support agents with AI-generated response suggestions, moving from initial GPT models to a multi-stage pipeline with fine-tuned models for question validation, topic classification, and answer generation. Challenges in production highlighted the importance of UX, online monitoring, and data quality, demonstrating that a data-centric approach and iterative deployment are crucial for successful LLM implementation in complex domains.
- [**Stripe**](https://www.zenml.io/llmops-database/production-llm-implementation-for-customer-support-response-generation) \- Stripe deployed a multi-stage LLM system to improve customer support response times, using fine-tuned models for question filtering, topic classification, and response generation, and found that data quality and online monitoring were critical for success, even more so than model sophistication. They also learned that agent adoption and UX considerations are key to successful production deployments.
- [**Summer Health**](https://www.zenml.io/llmops-database/gpt-4-visit-notes-system) \- Summer Health leveraged GPT-4 to automate pediatric visit note generation, reducing note-writing time by 80% while improving clarity for parents by translating medical terminology. The system prioritizes HIPAA compliance and clinical accuracy, demonstrating the effective use of LLMs to improve both provider efficiency and patient experience in healthcare.
- [**SumUp**](https://www.zenml.io/llmops-database/llm-evaluation-framework-for-financial-crime-report-generation) \- SumUp developed an LLM-driven system to automate financial crime report generation, using a novel LLM-based evaluation framework with custom benchmarks and scoring to ensure quality. This approach outperformed traditional NLP metrics and correlated well with human assessments, while also mitigating potential biases through techniques like position swapping and few-shot prompting.
- [**Superhuman**](https://www.zenml.io/llmops-database/ai-powered-email-search-assistant-with-advanced-cognitive-architecture) \- Superhuman’s Ask AI leverages a sophisticated cognitive architecture with parallel processing to enable natural language email and calendar searches, moving beyond traditional keyword matching. This evolution from a basic RAG system to a task-specific tool integration resulted in a 14% reduction in user search time and sub-2-second response times, achieved through techniques like double-dipping prompts and advanced reranking algorithms.
- [**Swiggy**](https://www.zenml.io/llmops-database/two-stage-fine-tuning-of-language-models-for-hyperlocal-food-search-ff103) \- Swiggy, a major food delivery platform in India, improved its hyperlocal food search by implementing a two-stage fine-tuning approach for language models, using unsupervised learning on historical data followed by supervised learning with curated query-item pairs. Leveraging TSDAE and Multiple Negatives Ranking Loss, Swiggy achieved superior search relevance while maintaining a 100ms latency requirement.
- [**Swiggy**](https://www.zenml.io/llmops-database/building-a-comprehensive-llm-platform-for-food-delivery-services) \- Swiggy strategically deployed LLMs across their platform, focusing on catalog enrichment, review summarization, and restaurant partner support, building a middle layer for GenAI integration and carefully selecting models based on use case requirements, including custom models for real-time applications and RAG-based systems for vendor support. Their implementation included A/B testing and robust evaluation frameworks to mitigate issues like hallucination and latency, demonstrating a comprehensive approach to LLMOps with a focus on sustained ROI.
- [**Swiggy**](https://www.zenml.io/llmops-database/neural-search-and-conversational-ai-for-food-delivery-and-restaurant-discovery) \- Swiggy has implemented a neural search system using fine-tuned LLMs to enable conversational food and grocery discovery, handling open-ended queries across a 50 million item catalog. They’ve also developed LLM-powered chatbots for customer service, partner support, and a Dineout virtual concierge, showcasing a broad application of generative AI.
- [**The Institute for Ethical AI / Linux Foundation**](https://www.zenml.io/llmops-database/state-of-production-machine-learning-and-llmops-in-2024) \- This case study examines the current landscape of production machine learning and LLMOps, detailing the shift towards data-centric approaches and the evolution of MLOps ecosystems, while also emphasizing the importance of robust monitoring, security, and flexible development lifecycles. It further highlights the growing need for comprehensive data management, metadata tracking, and risk assessment, alongside future considerations like responsible AI and the integration of LLMs.
- [**Therapy Bot**](https://www.zenml.io/llmops-database/best-practices-for-implementing-llms-in-high-stakes-applications) \- This presentation details best practices for deploying LLMs in high-stakes environments like healthcare, emphasizing the need for robust risk assessment, human oversight, and continuous evaluation, while also providing practical solutions such as structured conversation flows, task decomposition, and prompt engineering. The discussion advocates for a balanced approach that combines LLMs with traditional methods, prioritizing safety and reliability.
- [**There is no company name mentioned in the case study.**](https://www.zenml.io/llmops-database/building-a-production-ready-business-analytics-assistant-with-chatgpt) \- A production-ready business analytics assistant was built using a multi-agent system with specialized ChatGPT agents for data engineering and data science, leveraging the ReAct framework, SQL, and Streamlit to address challenges like token limits and complex schema handling. This system demonstrates a practical approach to operationalizing LLMs for structured data analysis, emphasizing modular design and robust error handling.
- [**There is no company name mentioned in this case study.**](https://www.zenml.io/llmops-database/building-and-scaling-enterprise-llmops-platforms-from-team-topology-to-production) \- This case study details the implementation of LLMOps platforms in enterprises, applying DevOps principles to manage the complexities of AI in production. It covers platform infrastructure, team structures, and addresses challenges in testing, developer experience, and governance, emphasizing the need for robust testing, balanced automation, and comprehensive monitoring.
- [**Thomas**](https://www.zenml.io/llmops-database/enhancing-workplace-assessment-tools-with-rag-and-vector-search) \- Thomas, a workplace assessment company, modernized its legacy system by implementing a generative AI solution using Databricks, leveraging RAG and Vector Search to provide personalized insights from their extensive content database, while maintaining robust security and integrating with platforms like Microsoft Teams. This transformation enabled them to develop a new product, improve user experience, and scale their assessment processing capabilities.
- [**Thomson Reuters**](https://www.zenml.io/llmops-database/enterprise-llm-playground-development-for-internal-ai-experimentation) \- Thomson Reuters developed Open Arena, an internal LLM experimentation platform, in under six weeks using AWS serverless architecture, SageMaker, and Hugging Face containers. This platform allows non-technical users to securely test both open-source and in-house LLMs, combined with company data, using a tile-based interface with chat and document upload capabilities.
- [**Thoughtworks**](https://www.zenml.io/llmops-database/building-an-ai-co-pilot-application-patterns-and-best-practices) \- Thoughtworks built Boba, an AI co-pilot for product strategy, showcasing practical LLMOps patterns like templated prompts, structured JSON responses, and real-time streaming. The application integrates external tools, manages context with vector stores, and emphasizes user experience with feedback mechanisms, providing a detailed look at building production-ready LLM applications.
- [**Thoughtworks**](https://www.zenml.io/llmops-database/building-an-ai-co-pilot-for-product-strategy-with-llm-integration-patterns) \- Thoughtworks created Boba, an AI co-pilot for product strategy, demonstrating advanced LLM integration patterns such as templated prompts, structured JSON responses, real-time streaming, and RAG with vector stores, using OpenAI, Langchain, and Vercel AI SDK, highlighting practical implementation details for production-ready LLM applications.
- [**Thumbtack**](https://www.zenml.io/llmops-database/fine-tuned-llm-for-message-content-moderation-and-trust-safety) \- Thumbtack enhanced its message content moderation by fine-tuning an LLM, achieving a significant AUC improvement to 0.93 after initial prompt engineering attempts failed. Their production system uses a cost-effective two-tier approach, pre-filtering messages with a CNN model before routing suspicious ones to the LLM, resulting in a 3.7x precision and 1.5x recall improvement.
- [**Thumbtack**](https://www.zenml.io/llmops-database/building-and-implementing-a-company-wide-genai-strategy) \- Thumbtack implemented a company-wide GenAI strategy, focusing on enhancing their consumer product, transforming operations, and boosting employee productivity. They built new infrastructure to support both open-source and external LLMs, with a strong emphasis on PII protection and secure access, and focused on governance, security, and measurable business outcomes.
- [**Tinder**](https://www.zenml.io/llmops-database/scaling-trust-and-safety-using-llms-at-tinder) \- Tinder utilizes fine-tuned open-source LLMs with LoRA for efficient trust and safety operations, enabling them to serve multiple models on a single GPU using the Lorax framework, achieving high recall and precision in detecting various violations, including hate speech and scams. This approach demonstrates superior generalization and resilience against adversarial behavior compared to traditional ML methods, while maintaining cost-effectiveness and scalability.
- [**Titan ML / YLabs / Outer Bounds**](https://www.zenml.io/llmops-database/panel-discussion-best-practices-for-llms-in-production) \- A panel of experts from Titan ML, YLabs, and Outer Bounds discussed best practices for deploying LLMs in production, covering topics such as prototyping with API providers, system architecture, and addressing hardware constraints. The discussion emphasized the need for robust evaluation pipelines, user feedback mechanisms, and comprehensive observability to ensure performance, cost-effectiveness, and a positive user experience.
- [**TomTom**](https://www.zenml.io/llmops-database/strategic-implementation-of-generative-ai-at-scale) \- TomTom adopted a hub-and-spoke model to implement generative AI across their organization, deploying applications like a ChatGPT location plugin and an in-car AI assistant, achieving 30-60% task performance improvements with a focus on responsible AI and workforce upskilling. They also built internal tools for mapmaking and development, all while maintaining centralized oversight and quality control.
- [**Trace3**](https://www.zenml.io/llmops-database/custom-rag-implementation-for-enterprise-technology-research-and-knowledge-management) \- Trace3’s Innovation Team developed Innovation-GPT, a custom LLM-powered solution using a RAG architecture to streamline their technology research and knowledge management, automating data collection and analysis via web scraping, structured data processing, and natural language querying, while maintaining human oversight for quality control. This approach highlights the importance of balancing automation with accuracy in production LLM implementations.
- [**Tradestack**](https://www.zenml.io/llmops-database/building-a-reliable-ai-quote-generation-assistant-with-langgraph) \- Tradestack built an AI-powered WhatsApp assistant using LangGraph to automate quote generation for the trades industry, reducing quote creation time from hours to under 15 minutes. Their system leverages a multi-agent architecture, handles multimodal inputs, and uses LangSmith for rigorous testing, achieving an 85% end-to-end performance improvement and deploying to a large user base in just 6 weeks.
- [**TrainGRC**](https://www.zenml.io/llmops-database/building-a-rag-system-for-cybersecurity-research-and-reporting) \- TrainGRC implemented a RAG system for cybersecurity research, tackling fragmented knowledge and LLM censorship using Amazon Textract for OCR, custom web scraping, and optimized vector search with various embedding models, focusing on data quality, search optimization, and context chunking. The system addresses complex data processing challenges while considering long-term storage and model migration.
- [**Trigent Software**](https://www.zenml.io/llmops-database/developing-a-multilingual-ayurvedic-medical-llm-challenges-and-learnings) \- Trigent Software’s IRGPT project aimed to build a multilingual LLM for Ayurvedic medical consultations, using a fine-tuned GPT-2 model and a diverse dataset; however, challenges in data quality, translation, and cultural nuances led to a pivot towards an English-only prototype, highlighting the complexities of multilingual LLM development in specialized domains. The project underscores the importance of iterative development and high-quality data when applying LLMs to specialized fields like traditional medicine.
- [**Twelve Labs**](https://www.zenml.io/llmops-database/building-a-scalable-conversational-video-agent-with-langgraph-and-twelve-labs-apis) \- Jockey, an open-source conversational video agent, leverages LangGraph and Twelve Labs APIs to intelligently process and analyze video content, evolving from a basic LangChain implementation to a more robust LangGraph architecture. This multi-agent system, featuring a Supervisor, Planner, and specialized Workers, enables improved scalability and granular control over video workflows.
- [**Twelve Labs / Databricks**](https://www.zenml.io/llmops-database/multimodal-ai-vector-search-for-advanced-video-understanding) \- Twelve Labs partnered with Databricks Mosaic AI to create a production-grade system for advanced video understanding, using multimodal embeddings to capture visual, textual, and contextual information; this allows for nuanced search and analysis, leveraging Databricks’ Delta Lake for reliable storage and Mosaic AI for scalable vector search, with a focus on MLOps best practices.
- [**Twilio**](https://www.zenml.io/llmops-database/building-an-ai-innovation-team-and-platform-with-safeguards-at-scale) \- Twilio’s Emerging Tech and Innovation team built an AI platform to enhance customer engagement by bridging unstructured communications data with structured customer profiles, using a flexible architecture for rapid model switching. They launched “Twilio Alpha” to manage expectations around early-stage AI products, balancing rapid innovation with enterprise quality through iterative development and a cross-functional team.
- [**Twilio Segment**](https://www.zenml.io/llmops-database/llm-as-judge-framework-for-production-llm-evaluation-and-improvement) \- Twilio Segment implemented an LLM-as-Judge framework to evaluate and improve their CustomerAI feature, which uses LLMs to generate audience queries from natural language, achieving over 90% alignment with human evaluations and a 3x improvement in audience creation time. This robust framework uses a multi-agent architecture and a discrete scoring system to provide a scalable and reliable evaluation pipeline for production LLM systems.
- [**Uber**](https://www.zenml.io/llmops-database/llm-driven-developer-experience-and-code-migrations-at-scale) \- Uber’s Developer Platform team explored using LLMs for a custom IDE assistant, automated test generation (Auto Cover), and Java-to-Kotlin code migration. They found that hybrid approaches, combining deterministic steps with LLM reasoning, were more effective than pure LLM solutions, leading to significant developer productivity gains while maintaining code quality.
- [**Uber**](https://www.zenml.io/llmops-database/enterprise-scale-prompt-engineering-toolkit-with-lifecycle-management-and-production-integration) \- Uber has developed an enterprise-scale prompt engineering toolkit that manages the full lifecycle of LLM deployment, featuring centralized prompt template management, version control, and robust evaluation frameworks. The toolkit supports rapid experimentation, automated prompt generation, and includes production-grade deployment with safety features, both offline batch processing and online serving capabilities, and comprehensive monitoring of metrics.
- [**Uber**](https://www.zenml.io/llmops-database/dragoncrawl-uber-s-journey-to-ai-powered-mobile-testing-using-small-language-models) \- Uber’s DragonCrawl utilizes a small language model to automate mobile app testing, achieving 99%+ stability across 85 cities and blocking 10 high-priority bugs. This AI-powered system, built on an MPNet architecture, significantly reduced maintenance costs and demonstrated human-like problem-solving capabilities, showcasing the effectiveness of focused, small models in complex production environments.
- [**Ubisoft / AI21 Labs**](https://www.zenml.io/llmops-database/scaling-game-content-production-with-llms-and-data-augmentation) \- Ubisoft partnered with AI21 Labs to integrate LLMs into their game development pipeline, focusing on automating NPC dialogue generation and creating training data. They implemented a writer-in-the-loop system, using AI21’s models for data augmentation and leveraging a cost-effective token pricing model, which enabled them to scale content production, improve efficiency, and maintain creative control.
- [**Unify**](https://www.zenml.io/llmops-database/building-and-deploying-ai-agents-for-account-qualification) \- Unify developed an AI agent system for automating sales account qualification, using LangGraph for orchestration and LangSmith for experimentation. Through iterative development, they refined the agent architecture to improve planning, reflection, and execution, while optimizing for speed and user experience, ultimately deploying a system with real-time progress visualization and parallel tool execution.
- [**V7**](https://www.zenml.io/llmops-database/challenges-in-designing-human-in-the-loop-systems-for-llms-in-production) \- V7, a training data platform, explores the challenges of implementing human-in-the-loop LLM systems in production, noting that many implementations remain simplistic and often rely on basic feedback. They highlight the limitations of automation, the difficulties in learning from human feedback, and the gap between LLM capabilities and real-world industry requirements, emphasizing the need for careful system design and a balance between automation and human oversight.
- [**Val Town**](https://www.zenml.io/llmops-database/evolution-of-code-assistant-integration-in-a-cloud-development-platform) \- Val Town’s experience integrating LLM-powered code assistance into their cloud development platform demonstrates the iterative process of productionizing these features. Starting with basic autocomplete using ChatGPT, they progressed to more sophisticated solutions, including purpose-built models for code completion, Claude integration for improved generation, and innovative error detection systems.
- [**Vannevar Labs**](https://www.zenml.io/llmops-database/fine-tuning-mistral-7b-for-multilingual-defense-intelligence-sentiment-analysis) \- Vannevar Labs moved from using GPT-4 to a fine-tuned Mistral 7B model on Databricks Mosaic AI for defense intelligence sentiment analysis, improving accuracy to 76% and reducing latency by 75%, while also cutting costs and improving multilingual support. The entire LLMOps pipeline, including infrastructure, training, and deployment, was implemented in just two weeks, showcasing the efficiency of a custom model approach.
- [**Vendr / Extend**](https://www.zenml.io/llmops-database/scaling-document-processing-with-llms-and-human-review) \- Vendr partnered with Extend to build a production-scale document processing system using LLMs, combining OCR with LLMs for entity recognition and data extraction, and incorporating human review for quality control; the system uses document embeddings for similarity analysis, enabling efficient review processes and has successfully processed over 100,000 documents.
- [**Verizon / Anthropic / Infosys**](https://www.zenml.io/llmops-database/scaling-llm-applications-in-telecommunications-learnings-from-verizon-and-industry-partners) \- Verizon, in collaboration with Anthropic and Infosys, is deploying LLMs for content generation, software development lifecycle enhancements, and co-pilot applications, using a model-agnostic architecture and refined RAG techniques. They emphasize rigorous evaluation, aiming for 95% accuracy in production, while addressing challenges like cost, user adoption, and data management through a center of excellence and change management strategies.
- [**Vespa**](https://www.zenml.io/llmops-database/building-a-production-rag-based-slackbot-for-developer-support) \- Vespa built a production-grade Slackbot using RAG and their search infrastructure to manage a surge in support queries, incorporating semantic search, BM25, and user feedback for ranking. Deployed on GCP, the bot features user consent management, anonymization, and continuous learning to improve response quality.
- [**Vimeo**](https://www.zenml.io/llmops-database/building-an-ai-powered-help-desk-with-rag-and-model-evaluation) \- Vimeo implemented an AI-powered help desk using a RAG architecture, leveraging vector embeddings of their Zendesk content for retrieval and integrating multiple LLMs via Langchain, with a focus on model evaluation and cost optimization. The system showcases a production-ready architecture with considerations for scalability, security, and ongoing maintenance, demonstrating practical LLMOps.
- [**Vinted**](https://www.zenml.io/llmops-database/migrating-from-elasticsearch-to-vespa-for-large-scale-search-platform) \- Vinted, a major e-commerce platform, migrated its search infrastructure from Elasticsearch to Vespa, consolidating multiple clusters into a single deployment and achieving a 2.5x improvement in search latency and a 3x improvement in indexing latency, while also halving their server count. This migration, completed over a year, involved a phased approach, real-time data processing with Apache Flink, and the development of a custom Vespa Kafka connector, demonstrating significant gains in performance and operational efficiency.
- [**Vira Health**](https://www.zenml.io/llmops-database/building-and-evaluating-a-rag-based-menopause-information-chatbot) \- Vira Health built a RAG-based menopause information chatbot using GPT-4, prioritizing safety and accuracy by grounding responses in peer-reviewed medical guidelines, and rigorously evaluated it using both AI and human clinicians. The system, built with vanilla Python for control, demonstrated high faithfulness, relevance, and clinical correctness, showcasing a responsible approach to LLM deployment in healthcare.
- [**Vodafone**](https://www.zenml.io/llmops-database/network-operations-transformation-with-genai-and-aiops) \- Vodafone partnered with Google Cloud to modernize its network operations, migrating to a unified data platform managing over 2 petabytes of data and consolidating over 100 legacy systems. By integrating device-level analytics, AIOps, and GenAI for network investment planning, they’ve improved incident response, network performance monitoring, and aim to reduce OSS tools by 50%.
- [**Voiceflow**](https://www.zenml.io/llmops-database/scaling-chatbot-platform-with-hybrid-llm-and-custom-model-approach) \- Voiceflow, a platform for building chat and voice assistants, implemented a hybrid approach, integrating LLMs via the OpenAI API for generative features while retaining their custom NLU model for intent and entity detection due to its superior performance and cost-effectiveness; they also built an ML Gateway to manage connections to both LLMs and traditional models, and implemented prompt engineering and error handling to address challenges like JSON formatting.
- [**VSL Labs**](https://www.zenml.io/llmops-database/automated-sign-language-translation-using-large-language-models) \- VSL Labs has developed an automated sign language translation platform that uses generative AI to convert English text and audio into American Sign Language (ASL), addressing the challenges of accessibility for the deaf community by using a two-stage process that includes linguistic processing with in-house and GPT-4 models, and then converting this into 3D animation instructions for realistic avatar-based sign language interpretation. The API-first platform is designed for real-world applications, with a focus on quality assurance, performance, and cultural sensitivity.
- [**W&B**](https://www.zenml.io/llmops-database/evaluation-driven-refactoring-wandb) \- Weights & Biases significantly improved their LLM-powered documentation assistant, Wandbot, by adopting an evaluation-driven refactoring approach, resulting in an 84% latency reduction and a 9% increase in accuracy through systematic testing, a switch to ChromaDB, and RAG pipeline optimizations. This case study highlights the importance of continuous evaluation in LLM system development, demonstrating the benefits of modular design and efficient vector stores.
- [**Walmart**](https://www.zenml.io/llmops-database/semantic-caching-for-e-commerce-search-optimization) \- Walmart implemented a semantic caching system using vector embeddings and generative AI to improve e-commerce search, achieving a 50% cache hit rate for tail queries by understanding search intent rather than relying on exact matches, while also addressing challenges like latency and cost in a high-scale production environment. This hybrid approach combines traditional and semantic caching to deliver more relevant results and reduce zero-result searches.
- [**Walmart**](https://www.zenml.io/llmops-database/hybrid-ai-system-for-large-scale-product-categorization) \- Walmart’s Ghotok is a hybrid AI system that combines predictive and generative models to categorize 400 million SKUs, using domain-specific features and chain-of-thought prompting. The system employs a two-stage filtering process and caching to ensure millisecond-level response times, while also incorporating robust exception handling and monitoring for production stability.
- [**Wayfair**](https://www.zenml.io/llmops-database/ai-powered-co-pilot-system-for-digital-sales-agents) \- Wayfair’s Agent Co-pilot uses LLMs to provide real-time, context-aware chat suggestions to digital sales agents, incorporating product information, policies, and conversation history. This system has achieved a 10% reduction in handle time while maintaining high-quality customer interactions, demonstrating the effectiveness of LLMs in enhancing agent productivity.
- [**Weights & Biases**](https://www.zenml.io/llmops-database/building-a-voice-assistant-from-open-source-llms-a-home-project-case-study) \- A Weights & Biases founder developed a voice assistant, similar to Alexa, using open-source LLMs, demonstrating the practical steps from demo to production, including speech recognition with Whisper, local LLM deployment with llama.cpp, and iterative improvements through prompt engineering, model switching, and fine-tuning to achieve 98% accuracy. The project highlights the importance of systematic evaluation, comprehensive experiment tracking, and a balanced approach to model selection and optimization for successful LLM deployments.
- [**Weights & Biases**](https://www.zenml.io/llmops-database/building-a-voice-assistant-with-open-source-llms-from-demo-to-production) \- Weights & Biases built a production-ready, open-source voice assistant using Llama 2 and Mistral models, running on affordable hardware and incorporating Whisper for speech recognition, achieving 98% accuracy through iterative improvements like prompt engineering and fine-tuning with QLoRA. The project underscores the challenges of moving from demo to production with LLMs, highlighting the need for a robust evaluation framework and systematic experimentation.
- [**Weights & Biases**](https://www.zenml.io/llmops-database/llmops-lessons-from-w-b-s-wandbot-manual-evaluation-quality-assurance-of-production-llm-systems) \- Weights & Biases performed a manual evaluation of their production LLM-powered technical support bot, Wandbot, which uses a RAG architecture across multiple platforms, achieving a baseline accuracy of 66.67%. The study highlights the importance of systematic evaluation, clear metrics, and expert annotation in LLMOps, while also showcasing practical solutions using [Argilla.io](http://argilla.io/) for annotation management.
- [**Weights & Biases**](https://www.zenml.io/llmops-database/building-robust-llm-evaluation-frameworks-w-b-s-evaluation-driven-development-approach) \- Weights & Biases utilized an evaluation-driven methodology to refine Wandbot 1.1, creating an automated evaluation framework aligned with human annotations and leveraging GPT-4 for multi-faceted assessments, resulting in improvements to data ingestion, query enhancement, and a hybrid retrieval system. This approach led to significant performance gains, with the latest model demonstrating superior answer correctness, relevancy, and context recall.
- [**Weights & Biases**](https://www.zenml.io/llmops-database/llmops-evolution-scaling-wandbot-from-monolith-to-production-ready-microservices) \- Weights & Biases evolved their documentation chatbot, Wandbot, from a monolithic architecture to a microservices system with four core modules, enhancing scalability and maintainability. The new architecture includes features like multilingual support, model fallback, and caching, achieving a 66.67% response accuracy and 88.636% query relevancy, while also adding new platform integrations.
- [**WellSky**](https://www.zenml.io/llmops-database/responsible-ai-implementation-for-healthcare-form-automation) \- WellSky, a healthcare technology company processing over 100 million forms annually, partnered with Google Cloud to implement an AI-powered form automation solution. This initiative focused on a responsible AI framework, including mandatory evidence citation and a robust governance structure, to reduce clinician burnout and documentation errors while ensuring patient safety.
- [**Whatnot**](https://www.zenml.io/llmops-database/llm-enhanced-trust-and-safety-platform-for-e-commerce-content-moderation) \- Whatnot, a live shopping marketplace, enhanced its trust and safety operations by integrating LLMs with its existing rule-based system, achieving a 95% detection rate for scam attempts with 96% precision. This new system uses a three-phase architecture to detect scams, moderate content, and enforce platform policies by analyzing conversational context and user behavior patterns, while maintaining a human-in-the-loop approach for final decisions and incorporating multimodal processing for analyzing text in images.
- [**Whatnot**](https://www.zenml.io/llmops-database/enhancing-e-commerce-search-with-gpt-based-query-expansion) \- Whatnot implemented a GPT-based query expansion system to improve e-commerce search by addressing misspellings and abbreviations, using an offline pipeline for processing and a production cache for low-latency serving, reducing irrelevant content by over 50% for problem queries. This hybrid approach demonstrates a practical method for integrating LLMs into production search systems.
- [**Wordsmith**](https://www.zenml.io/llmops-database/langsmith-implementation-for-full-product-lifecycle-development-and-monitoring) \- Wordsmith, an AI legal assistant platform, implemented LangSmith to streamline their LLM operations across the entire product lifecycle, using features like hierarchical tracing and evaluation datasets to tackle challenges in prototyping, debugging, and evaluation. This enabled faster development cycles, efficient debugging, and data-driven experimentation while managing multiple LLM providers.
- [**Wroclaw Medical University / Institute of Mother and Child**](https://www.zenml.io/llmops-database/nlp-and-machine-learning-for-early-sepsis-detection-in-neonatal-care) \- Wroclaw Medical University, in collaboration with the Institute of Mother and Child, is developing an AI-powered system using NLP and machine learning to detect sepsis in neonatal care. The system processes real-time data, including unstructured medical records, to identify early symptoms, reducing diagnosis time from 24 hours to 2 hours, while maintaining high sensitivity and specificity.
- [**WSC Sport**](https://www.zenml.io/llmops-database/automated-sports-commentary-generation-using-llms) \- WSC Sport utilizes LLMs to automate real-time sports commentary and recaps, processing game data into coherent narratives with synthesized voiceovers, employing techniques like dynamic prompt generation and Chain-of-Thought for fact verification to reduce production time from hours to minutes, while maintaining accuracy and enabling multilingual content.
- [**WVU Medicine / John Snow Labs**](https://www.zenml.io/llmops-database/automated-hcc-code-extraction-from-clinical-notes-using-healthcare-nlp) \- WVU Medicine deployed an automated HCC code extraction system using John Snow Labs’ Healthcare NLP, processing radiology notes to identify diagnoses, convert them to CPT codes, and map them to HCC codes, achieving an 18.4% provider acceptance rate on over 27,000 codes processed. The system highlights the importance of model customization, confidence scoring, and production system integration in healthcare LLMOps.
- [**Xcel Energy**](https://www.zenml.io/llmops-database/rag-based-chatbot-for-utility-operations-and-customer-service) \- Xcel Energy deployed a RAG-based chatbot using Databricks’ Data Intelligence Platform to streamline operations like rate case reviews and legal contract analysis, reducing review times from 6 months to 2 weeks. The production-grade GenAI system leverages Vector Search, MLflow, and Foundation Model APIs, while maintaining strict security and governance for sensitive utility data.
- [**Yahoo Mail**](https://www.zenml.io/llmops-database/scaling-email-content-extraction-using-llms-in-production) \- Yahoo Mail implemented a new email content extraction system using Google Cloud’s Vertex AI and LLMs, overcoming limitations of their previous ML-based system. This resulted in improved coverage, reaching 94% for standard domains and 99% for long-tail domains, alongside a 51% increase in extraction richness and a 16% reduction in tracking API errors, while processing billions of daily messages.
- [**YouTube**](https://www.zenml.io/llmops-database/dutch-youtube-interface-localization-and-content-management) \- YouTube employs sophisticated localization and content management systems, likely using LLMs for interface translation, content moderation, and ensuring cultural relevance, with a focus on maintaining high-quality translations and optimizing user experience across diverse regions. The platform’s LLMOps implementation also addresses scalability and compliance with regional requirements.
- [**YouTube**](https://www.zenml.io/llmops-database/multilingual-content-navigation-and-localization-system) \- YouTube utilizes a sophisticated multilingual content navigation and localization system, employing LLMs for neural machine translation, content analysis, and automated quality checks, ensuring a high-quality user experience across its global audience. This system includes automated language identification, smart routing based on user preferences, and a robust content management system with version control for different language variants.
- [**zeb**](https://www.zenml.io/llmops-database/building-a-self-service-data-analytics-platform-with-generative-ai-and-rag) \- zeb developed SuperInsight, a self-service data analytics platform using generative AI and RAG, built on Databricks, that reduced manual data analyst workload by 80-90%. The system leverages DBRX models, fine-tuning, and vector search to process natural language requests, generating reports, forecasts, and ML models, demonstrating a practical application of LLMs in production.
- [**Zillow**](https://www.zenml.io/llmops-database/building-fair-housing-guardrails-for-real-estate-llms-zillow-s-multi-strategy-approach-to-preventing-discrimination) \- Zillow implemented a multi-faceted system to ensure their real estate LLMs adhere to Fair Housing regulations, combining prompt engineering, stop lists, and a BERT-based classifier to prevent discriminatory responses. This approach validates both user inputs and model outputs, using a curated dataset to achieve high recall in identifying non-compliant content.

_Check out [the full LLMOps Database](https://www.zenml.io/llmops-database) and please do let us know if you have an entry you’d like to be included!_

[LLMOps](https://www.zenml.io/tags/llmops) [llm](https://www.zenml.io/tags/llm) [llmops-database](https://www.zenml.io/tags/llmops-database) [production](https://www.zenml.io/tags/production) [genai](https://www.zenml.io/tags/genai) [agents](https://www.zenml.io/tags/agents)

[![Alex Strick van Linschoten](https://assets.zenml.io/webflow/64a817a2e7e2208272d1ce30/9804d473/652948c72d87d2e2afebb29b_alex.jpg)](https://www.zenml.io/author/alex-strick-van-linschoten)

[Alex Strick van Linschoten](https://www.zenml.io/author/alex-strick-van-linschoten)

[View all posts →](https://www.zenml.io/author/alex-strick-van-linschoten)

[← PreviousAI Engineering vs ML Engineering: Evolving Roles in the GenAI Era](https://www.zenml.io/blog/ai-engineering-vs-ml-engineering-evolving-roles-genai) [Next →Production LLM Security: Real-world Strategies from Industry Leaders 🔐](https://www.zenml.io/blog/production-llm-security-real-world-strategies-from-industry-leaders)

## Start deploying AI workflows in production today

Enterprise-grade AI platform trusted by thousands of companies in production

[Start Free Trial](https://cloud.zenml.io/signup) [Book a Demo](https://www.zenml.io/book-your-demo)

## Continue Reading

[![The Experimentation Phase Is Over: Key Findings from 1,200 Production Deployments](https://assets.zenml.io/webflow/64a817a2e7e2208272d1ce30/22d06e8a/6981d352ce4b26d085d70414_6981d2b4e0df7e2b97a5ff54_zenml-llms-short.avif)](https://www.zenml.io/blog/the-experimentation-phase-is-over-key-findings-from-1-200-production-deployments)

[LLMOps](https://www.zenml.io/category/llmops)

## [The Experimentation Phase Is Over: Key Findings from 1,200 Production Deployments](https://www.zenml.io/blog/the-experimentation-phase-is-over-key-findings-from-1-200-production-deployments)

Analysis of 1,200 production LLM deployments reveals six key patterns separating successful teams from those stuck in demo mode: context engineering over prompt engineering, infrastructure-based guardrails, rigorous evaluation practices, and the recognition that software engineering fundamentals—not frontier models—remain the primary predictor of success.

[Alex Strick van Linschoten](https://www.zenml.io/author/alex-strick-van-linschoten)

3 mins

[![LLMOps in Production: Another 419 Case Studies of What Actually Works](https://assets.zenml.io/webflow/64a817a2e7e2208272d1ce30/9ff6bf40/6981d362e92aa039b696ad11_6981d2b2349ea5b50eb500f9_variation3_1.avif)](https://www.zenml.io/blog/llmops-in-production-another-419-case-studies-of-what-actually-works)

[LLMOps](https://www.zenml.io/category/llmops)

## [LLMOps in Production: Another 419 Case Studies of What Actually Works](https://www.zenml.io/blog/llmops-in-production-another-419-case-studies-of-what-actually-works)

Explore 419 new real-world LLMOps case studies from the ZenML database, now totaling 1,182 production implementations—from multi-agent systems to RAG.

[Alex Strick van Linschoten](https://www.zenml.io/author/alex-strick-van-linschoten)

18 mins

[![The Agent Deployment Gap: Why Your LLM Loop Isn't Production-Ready (And What to Do About It)](https://assets.zenml.io/webflow/64a817a2e7e2208272d1ce30/5bf697c3/6981cf5010e873663bd75928_6981ce88bd9214d719ce5b4b_agent-deployment.avif)](https://www.zenml.io/blog/the-agent-deployment-gap-why-your-llm-loop-isnt-production-ready-and-what-to-do-about-it)

[LLMOps](https://www.zenml.io/category/llmops)

## [The Agent Deployment Gap: Why Your LLM Loop Isn't Production-Ready (And What to Do About It)](https://www.zenml.io/blog/the-agent-deployment-gap-why-your-llm-loop-isnt-production-ready-and-what-to-do-about-it)

Comprehensive analysis of why simple AI agent prototypes fail in production deployment, revealing the hidden complexities teams face when scaling from demos to enterprise-ready systems.

[Alex Strick van Linschoten](https://www.zenml.io/author/alex-strick-van-linschoten)

9 mins

We use cookies to improve your experience and analyze site traffic. See our [privacy policy](https://www.zenml.io/privacy-policy).

ManageReject allAccept all

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="pattern-orchestrator-worker-intelligence-patterns-reusable-e.md">
<details>
<summary>Pattern: Orchestrator-Worker (Coordinator)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://agents.kour.me/orchestrator-worker/>

# Pattern: Orchestrator-Worker (Coordinator)

## Motivation

A conductor coordinates an orchestra, assigning parts to different sections while maintaining the overall vision.
A project manager breaks down a complex project, delegates specialized tasks to team members, and synthesizes their contributions into a cohesive result.
The Orchestrator-Worker pattern mirrors this: a central coordinator breaks down complex goals, delegates to specialized workers, and integrates their outputs into a unified solution.

## Pattern Overview

### Problem

Complex tasks often require diverse expertise or multiple distinct capabilities that no single agent can handle effectively. When subtasks are unpredictable and dynamic rather than fixed, rigid, predefined workflows are insufficient. A single generalist agent struggles to produce high-quality outputs across multiple domains, and tasks that span many steps require maintaining high-level context while executing specific details.

### Solution

The Orchestrator-Worker pattern, also known as the "Coordinator pattern", addresses this by introducing a central orchestrator agent that dynamically breaks down complex goals into smaller subtasks, delegates them to specialized worker agents, and synthesizes the workers' outputs to produce the final result. Unlike rigid workflows, this pattern enables dynamic task decomposition where the orchestrator analyzes the high-level goal and determines necessary subtasks at runtime.

The pattern's strength lies in its ability to leverage specialization. Each worker agent can be optimized for a specific domain—research, writing, coding, analysis, or review—resulting in higher quality outputs than a single generalist agent could produce. The orchestrator acts as a strategic coordinator, managing the overall workflow, handling dependencies between subtasks, and synthesizing results into a coherent final output. This pattern is especially valuable for long-horizon tasks where the orchestrator maintains high-level context and goals while workers focus on specific execution details. The separation of concerns also enables better context management, as the orchestrator can isolate context for specific agents, preventing information overload and improving efficiency.

### Key Concepts

-   **Orchestrator (Coordinator/Lead Agent):** The central agent that receives high-level goals, decomposes them into subtasks, delegates to workers, and synthesizes results.
-   **Worker Agents:** Specialized agents that execute specific subtasks using domain expertise and specialized tools.
-   **Dynamic Task Decomposition:** The orchestrator determines subtasks at runtime based on the input, rather than using fixed workflows.
-   **Specialization:** Each worker agent focuses on a specific domain or capability, improving overall system effectiveness.
-   **Parallelization:** Independent subtasks can be executed concurrently by different workers, reducing overall latency.
-   **Hierarchical Organization:** Workers can themselves become orchestrators for sub-subtasks, creating nested multi-agent structures.
-   **Context Isolation:** The orchestrator can manage and isolate context for specific agents, improving efficiency and preventing information overload.

### How It Works: Step-by-step Explanation

1.  **Receive and Decompose:** The Orchestrator receives a high-level user request. It uses an AI model for reasoning to analyze and dynamically break the request into smaller, manageable pieces (subtasks).
2.  **Delegate:** The Orchestrator dispatches each subtask to the most appropriate specialized worker agent. The Orchestrator must provide clear, non-overlapping objectives to the subagents to avoid duplication of work or gaps in coverage.
3.  **Execute and Return:** Worker agents execute their specific task, often using specialized tools (e.g., querying a database or calling an API). They return their findings to the Orchestrator.
4.  **Synthesize:** The Orchestrator integrates the outputs from all worker agents to compile and return the final, coherent response to the user.

## When to Use This Pattern

### ✅ Use when:

-   **Complex, multifaceted tasks:** Tasks that require diverse expertise or multiple distinct capabilities that no single agent can handle effectively.
-   **Dynamic task requirements:** When subtasks cannot be predetermined and must be determined at runtime based on the input.
-   **Specialization needed:** Different aspects of the task require specialized knowledge or skills (e.g., research, writing, coding, review).
-   **Parallel processing possible:** Multiple independent sub-tasks can be executed concurrently by different agents.
-   **Long-horizon tasks:** Tasks that span many steps where maintaining high-level context is essential.
-   **Context window limitations:** Tasks where the full context exceeds a single agent's context window capacity.
-   **Resilience requirements:** When isolating failures to individual agents is important for system reliability.

### ❌ Avoid when:

-   **Simple single-agent tasks:** Tasks that can be effectively handled by a single, well-configured agent.
-   **Fixed workflows:** When tasks follow a rigid, predetermined sequence that doesn't benefit from dynamic decomposition.
-   **Tight coupling required:** Tasks where sub-tasks are so tightly coupled that coordination overhead exceeds benefits.
-   **Low-latency requirements:** When the overhead of multi-agent coordination and communication is prohibitive.
-   **Resource constraints:** When computational or cost constraints (increased model calls) make multiple agents impractical.
-   **Minimal complexity:** When the added complexity of multi-agent coordination doesn't provide sufficient benefit.

### Decision Guidelines

Use the Orchestrator-Worker pattern when the benefits of specialization, parallelization, and dynamic task decomposition outweigh the added complexity and coordination overhead.
This pattern is ideal for complex tasks where subtasks are unpredictable and require diverse expertise. Consider: task complexity (complex = orchestrator-worker), specialization needs (diverse expertise = multiple workers), and dynamic requirements (unpredictable = dynamic decomposition).
However, be aware of trade-offs: this pattern increases model calls, which raises latency, token throughput, and operational costs compared to a single-agent system.
For simple or tightly-coupled tasks, a single agent or simpler workflow may be more efficient.

## Practical Applications & Use Cases

The Orchestrator-Worker pattern is the most common pattern for complex LLM-based agentic tasks, enabling sophisticated systems that can handle multifaceted problems.

### General Use Cases

-   **Customer Service:** A coordinator agent analyzes a customer's request (e.g., order status, refund, technical support) and routes the task to the appropriate specialized agent (billing specialist, technical support agent, product information agent).
-   **Research and Report Generation:** An orchestrator breaks down research into sub-topics, delegates to specialized researcher agents who work in parallel, then a writer agent synthesizes findings into a comprehensive report.
-   **Content Creation Workflows:** A planner agent creates an outline, writer agents draft sections in parallel, and an editor agent reviews and refines the content for quality and consistency.
-   **Multi-file Software Projects:** An orchestrator analyzes requirements, identifies affected files, and delegates changes to specialized agents (frontend, backend, database, testing).

## Modern Framework Patterns

### Role-Based Specialization (ChatDev/MetaGPT Style)

Modern orchestrator-worker systems leverage role-based specialization, where each worker agent has a well-defined role with specialized prompts and Standard Operating Procedures (SOPs).
This approach, demonstrated by ChatDev and MetaGPT, enables agents to achieve expert-level performance in their domains.

**Example Role Structure (MetaGPT-style):**

-   **Architect Agent:** Analyzes requirements, designs system architecture, creates technical specifications
-   **Programmer Agent:** Implements code based on specifications, writes unit tests
-   **Reviewer Agent:** Reviews code for quality, correctness, and adherence to standards
-   **Tester Agent:** Designs and executes test cases, reports bugs

### Dynamic Agent Orchestration (AgentVerse Style)

Dynamic orchestration allows the system to adapt team composition based on task requirements. The orchestrator can spawn new specialist agents as needed and release them when tasks complete, optimizing resource usage.

Key Principles:

-   **Adaptive Team Composition:** Team structure evolves during problem-solving
-   **Agent Lifecycle Management:** Agents are created, activated, and released dynamically
-   **Emergent Behaviors:** System exhibits emergent social behaviors (leadership, cooperation) without explicit programming
-   **Resource Optimization:** System optimizes agent allocation based on current needs

### Managed Conversations (AutoGen Style)

Managed conversations enable flexible communication patterns where orchestrators coordinate structured dialogues between agents. This approach supports complex problem-solving through multi-turn agent interactions.

Key Principles:

-   **Flexible Communication Patterns:** Developers define custom orchestration patterns
-   **Structured Dialogues:** Agents engage in structured conversations with clear protocols
-   **Multi-Turn Interactions:** Complex problems solved through iterative agent dialogues
-   **Result Integration:** Orchestrator synthesizes outputs from multiple agent interactions

### Central Controller Pattern (HuggingGPT Style)

A central LLM controller orchestrates multiple specialized models or agents, planning subtasks, delegating to appropriate specialists, and integrating results. This pattern transforms LLMs into general-purpose orchestrators.

**Key Principles:**
\- **LLM-as-Manager:** Language model serves as orchestrator, planning and coordinating specialists
\- **Tool/Model Delegation:** Controller delegates to specialized models, APIs, or tools as needed
\- **Handoff Protocols:** Clear protocols ensure results pass correctly between agents
\- **Global Planning:** Controller creates global plans optimizing action sequences

## Implementation

**Prerequisites:**

```
pip install langchain langchain-openai langgraph
# or
pip install google-adk
# or
pip install crewai  # Multi-agent orchestration framework
```

Basic Example: Orchestrator-Worker Pattern

This example demonstrates a basic orchestrator-worker system where the orchestrator dynamically decomposes tasks and delegates to specialized workers:

```
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict
import json

llm = ChatOpenAI(model="gpt-4o", temperature=0)

class OrchestratorState(TypedDict):
    goal: str
    plan: str
    subtasks: List[Dict]
    worker_results: Dict[str, str]
    final_output: str

def orchestrator_decompose(state: OrchestratorState) -> OrchestratorState:
    """Orchestrator receives goal and decomposes into subtasks."""
    goal = state["goal"]

    # Use LLM to dynamically create a plan and break down into subtasks
    decomposition_prompt = f"""You are an orchestrator agent. Analyze the following goal and break it down into specific, non-overlapping subtasks.

Goal: {goal}

For each subtask, determine:
1. The subtask description
2. The type of worker needed (research, write, code, analyze, review)
3. What information is needed as input
4. What output is expected

Return a JSON list of subtasks with keys: description, worker_type, input_needed, expected_output."""

    response = llm.invoke(decomposition_prompt)
    subtasks = json.loads(response.content)

    # Save plan to state (for recitation pattern)
    plan = f"Goal: {goal}\nSubtasks: {len(subtasks)}\n" + "\n".join([f"- {t['description']}" for t in subtasks])

    return {
        **state,
        "plan": plan,
        "subtasks": subtasks,
        "worker_results": {}
    }

def research_worker(state: OrchestratorState) -> OrchestratorState:
    """Specialized research worker agent."""
    # Get current subtask
    current_subtask = state["subtasks"][0] if state["subtasks"] else None
    if not current_subtask or current_subtask["worker_type"] != "research":
        return state

    research_prompt = f"""You are a research specialist. Conduct research on the following topic:

{current_subtask['input_needed']}

Provide comprehensive findings with key points, sources, and relevant information."""

    result = llm.invoke(research_prompt)

    worker_results = state.get("worker_results", {})
    worker_results["research"] = result.content

    # Remove completed subtask
    remaining_subtasks = state["subtasks"][1:]

    return {
        **state,
        "worker_results": worker_results,
        "subtasks": remaining_subtasks
    }

def write_worker(state: OrchestratorState) -> OrchestratorState:
    """Specialized writing worker agent."""
    current_subtask = state["subtasks"][0] if state["subtasks"] else None
    if not current_subtask or current_subtask["worker_type"] != "write":
        return state

    # Get research results
    research_results = state["worker_results"].get("research", "")

    write_prompt = f"""You are a writing specialist. Based on the following research, write a comprehensive summary:

Research Findings:
{research_results}

Write a clear, well-structured summary that synthesizes the key information."""

    result = llm.invoke(write_prompt)

    worker_results = state["worker_results"]
    worker_results["write"] = result.content

    remaining_subtasks = state["subtasks"][1:]

    return {
        **state,
        "worker_results": worker_results,
        "subtasks": remaining_subtasks,
        "final_output": result.content
    }

def orchestrator_synthesize(state: OrchestratorState) -> OrchestratorState:
    """Orchestrator synthesizes all worker results into final output."""
    goal = state["goal"]
    worker_results = state["worker_results"]
    plan = state.get("plan", "")

    synthesis_prompt = f"""You are an orchestrator agent. Synthesize the following worker results into a final, coherent response to the original goal.

Original Goal: {goal}

Plan:
{plan}

Worker Results:
{json.dumps(worker_results, indent=2)}

Create a comprehensive final output that integrates all worker contributions and directly addresses the original goal."""

    result = llm.invoke(synthesis_prompt)

    return {
        **state,
        "final_output": result.content
    }

def route_to_worker(state: OrchestratorState) -> str:
    """Route to appropriate worker based on current subtask."""
    if not state["subtasks"]:
        return "synthesize"

    worker_type = state["subtasks"][0]["worker_type"]
    if worker_type == "research":
        return "research_worker"
    elif worker_type == "write":
        return "write_worker"
    else:
        return "synthesize"

# Build graph
graph = StateGraph(OrchestratorState)
graph.add_node("orchestrator", orchestrator_decompose)
graph.add_node("research_worker", research_worker)
graph.add_node("write_worker", write_worker)
graph.add_node("synthesize", orchestrator_synthesize)

graph.set_entry_point("orchestrator")
graph.add_conditional_edges("orchestrator", route_to_worker)
graph.add_edge("research_worker", "write_worker")
graph.add_conditional_edges("write_worker", route_to_worker)
graph.add_edge("synthesize", END)

# Execute
result = graph.invoke({"goal": "Create a comprehensive report on renewable energy trends"})
print(result["final_output"])
```

**Explanation:**
This example demonstrates the core orchestrator-worker pattern: the orchestrator dynamically decomposes the goal into subtasks, delegates to specialized workers (research, writing), and synthesizes the results. The orchestrator maintains the plan and coordinates the workflow, while workers focus on their specialized domains.

Advanced Example: Hierarchical Orchestrator with Context Management

This advanced example shows nested orchestrators and context management using external memory:

```
from pathlib import Path
from typing import Dict, List
import json

class HierarchicalOrchestrator:
    def __init__(self, workspace_dir: str = "./workspace"):
        self.workspace = Path(workspace_dir)
        self.workspace.mkdir(exist_ok=True)
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.plan_file = self.workspace / "orchestrator_plan.md"

    def save_plan_to_memory(self, goal: str, plan: str):
        """Save plan to external memory before spawning subagents (context management)."""
        self.plan_file.write_text(f"# Orchestrator Plan\n\nGoal: {goal}\n\n{plan}")
        return f"Plan saved to {self.plan_file}. Use read_plan() to retrieve."

    def read_plan(self) -> str:
        """Read plan from external memory (recitation pattern)."""
        if self.plan_file.exists():
            return self.plan_file.read_text()
        return "No plan found."

    def decompose_with_planning(self, goal: str) -> Dict:
        """Orchestrator creates plan and decomposes goal."""
        # Create comprehensive plan
        plan_prompt = f"""You are a lead orchestrator agent. Analyze this goal and create a strategic plan:

Goal: {goal}

Create a detailed plan that includes:
1. High-level strategy
2. Required subtasks
3. Dependencies between subtasks
4. Required worker types
5. Expected outcomes

Return as structured plan."""

        plan_response = self.llm.invoke(plan_prompt)
        plan = plan_response.content

        # Save plan to memory (context management)
        self.save_plan_to_memory(goal, plan)

        # Decompose into subtasks
        decomposition_prompt = f"""Based on this plan, break down into specific subtasks:

Plan:
{plan}

Create a list of subtasks with clear, non-overlapping objectives."""

        decomposition_response = self.llm.invoke(decomposition_prompt)

        # Parse subtasks (simplified)
        subtasks = self._parse_subtasks(decomposition_response.content)

        return {
            "goal": goal,
            "plan": plan,
            "subtasks": subtasks
        }

    def delegate_to_worker(self, subtask: Dict, context: Dict) -> str:
        """Delegate subtask to appropriate worker with isolated context."""
        worker_type = subtask.get("worker_type", "general")

        # Isolate context for this worker (only relevant information)
        worker_context = {
            "subtask": subtask,
            "relevant_info": context.get("relevant_info", ""),
            "goal": context.get("goal", "")
        }

        # Route to specialized worker
        if worker_type == "research":
            return self._research_worker(worker_context)
        elif worker_type == "write":
            return self._write_worker(worker_context)
        elif worker_type == "code":
            return self._code_worker(worker_context)
        else:
            return self._general_worker(worker_context)

    def _research_worker(self, context: Dict) -> str:
        """Specialized research worker."""
        prompt = f"""You are a research specialist. Conduct research on:

{context['subtask']['description']}

Goal context: {context['goal']}

Provide comprehensive research findings."""

        result = self.llm.invoke(prompt)
        return result.content

    def _write_worker(self, context: Dict) -> str:
        """Specialized writing worker."""
        prompt = f"""You are a writing specialist. Write:

{context['subtask']['description']}

Based on: {context.get('relevant_info', '')}

Create well-structured, clear content."""

        result = self.llm.invoke(prompt)
        return result.content

    def _code_worker(self, context: Dict) -> str:
        """Specialized coding worker."""
        prompt = f"""You are a coding specialist. Implement:

{context['subtask']['description']}

Requirements: {context.get('relevant_info', '')}

Provide complete, working code with comments."""

        result = self.llm.invoke(prompt)
        return result.content

    def _general_worker(self, context: Dict) -> str:
        """General worker for unspecified tasks."""
        prompt = f"""Execute this task:

{context['subtask']['description']}

Context: {context.get('relevant_info', '')}"""

        result = self.llm.invoke(prompt)
        return result.content

    def synthesize_results(self, goal: str, worker_results: Dict[str, str]) -> str:
        """Orchestrator synthesizes all worker results."""
        # Read plan from memory (recitation)
        plan = self.read_plan()

        synthesis_prompt = f"""You are an orchestrator agent. Synthesize worker results into a final output.

Original Goal: {goal}

Plan (from memory):
{plan}

Worker Results:
{json.dumps(worker_results, indent=2)}

Create a comprehensive final output that:
1. Directly addresses the original goal
2. Integrates all worker contributions
3. Maintains coherence and quality
4. Follows the strategic plan"""

        result = self.llm.invoke(synthesis_prompt)
        return result.content

    def _parse_subtasks(self, content: str) -> List[Dict]:
        """Parse subtasks from LLM response (simplified)."""
        # In production, use structured output or better parsing
        lines = content.split('\n')
        subtasks = []
        for line in lines:
            if line.strip() and ('-' in line or line[0].isdigit()):
                subtasks.append({
                    "description": line.strip().lstrip('- ').lstrip('0123456789. '),
                    "worker_type": "general"  # Would be determined by LLM
                })
        return subtasks[:5]  # Limit for example

# Usage
orchestrator = HierarchicalOrchestrator()

# Orchestrator decomposes goal
decomposition = orchestrator.decompose_with_planning(
    "Create a comprehensive analysis of AI agent architectures"
)

# Execute subtasks (can be parallelized)
worker_results = {}
for subtask in decomposition["subtasks"]:
    result = orchestrator.delegate_to_worker(
        subtask,
        {"goal": decomposition["goal"], "relevant_info": ""}
    )
    worker_results[subtask["description"]] = result

# Orchestrator synthesizes
final_output = orchestrator.synthesize_results(
    decomposition["goal"],
    worker_results
)
```

**Explanation:**
This advanced example demonstrates hierarchical orchestrators with context management. The orchestrator saves its plan to external memory before spawning workers (enabling better context management), delegates with isolated context for each worker, and synthesizes results. Workers can themselves become orchestrators for complex subtasks, creating nested structures.

### Framework-Specific Examples

Google ADK: Orchestrator with Sub-Agents

```
from google.adk.agents import Agent
from google.adk.runners import Runner

# Define specialized worker agents
researcher = Agent(
    name="Researcher",
    model="gemini-2.0-flash",
    instruction="You are a research specialist. Conduct thorough research on assigned topics.",
    tools=[search_tool, web_scraper_tool]
)

writer = Agent(
    name="Writer",
    model="gemini-2.0-flash",
    instruction="You are a writing specialist. Create clear, well-structured content.",
    tools=[writing_tool, formatting_tool]
)

coder = Agent(
    name="Coder",
    model="gemini-2.0-flash",
    instruction="You are a coding specialist. Write clean, functional code.",
    tools=[code_editor_tool, test_runner_tool]
)

# Create orchestrator (coordinator)
orchestrator = Agent(
    name="Orchestrator",
    model="gemini-2.0-flash",
    instruction="""You are an orchestrator agent that coordinates complex tasks.

Your responsibilities:
1. Analyze high-level goals and break them into subtasks
2. Delegate subtasks to appropriate worker agents (Researcher, Writer, Coder)
3. Provide clear, non-overlapping objectives to workers
4. Synthesize worker results into final output

Available workers:
- Researcher: For research and information gathering tasks
- Writer: For content creation and writing tasks
- Coder: For coding and software development tasks

Always maintain the high-level goal and ensure worker outputs align with it.""",
    sub_agents=[researcher, writer, coder]
)

# Runner executes orchestrator
runner = Runner(
    agent=orchestrator,
    app_name="orchestrator_app"
)

# Orchestrator dynamically decomposes and delegates
result = runner.run("Create a comprehensive guide on agentic AI patterns")
```

LangGraph: Dynamic Orchestration

```
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

class OrchestratorState(TypedDict):
    goal: str
    plan: str
    subtasks: List[Dict]
    worker_results: Dict[str, str]
    current_worker: str
    final_output: str

def orchestrator_node(state: OrchestratorState) -> OrchestratorState:
    """Orchestrator decomposes goal into subtasks."""
    goal = state["goal"]

    # Dynamic decomposition
    prompt = f"Break down this goal into subtasks: {goal}"
    response = llm.invoke(prompt)

    # Parse and create subtasks
    subtasks = parse_subtasks(response.content)

    return {
        **state,
        "plan": response.content,
        "subtasks": subtasks
    }

def worker_node(state: OrchestratorState) -> OrchestratorState:
    """Generic worker node that routes to specialized workers."""
    if not state["subtasks"]:
        return {**state, "current_worker": "done"}

    current_subtask = state["subtasks"][0]
    worker_type = current_subtask.get("type", "general")

    # Execute with specialized prompt
    prompt = create_worker_prompt(worker_type, current_subtask, state["goal"])
    result = llm.invoke(prompt)

    # Store result
    worker_results = state.get("worker_results", {})
    worker_results[current_subtask["id"]] = result.content

    # Remove completed subtask
    remaining = state["subtasks"][1:]

    return {
        **state,
        "worker_results": worker_results,
        "subtasks": remaining,
        "current_worker": worker_type
    }

def synthesize_node(state: OrchestratorState) -> OrchestratorState:
    """Orchestrator synthesizes all results."""
    prompt = f"""Synthesize these worker results for goal: {state['goal']}

Results: {json.dumps(state['worker_results'], indent=2)}"""

    result = llm.invoke(prompt)

    return {
        **state,
        "final_output": result.content
    }

def should_continue(state: OrchestratorState) -> str:
    """Determine next step."""
    if state["subtasks"]:
        return "worker"
    elif state.get("final_output"):
        return "end"
    else:
        return "synthesize"

# Build graph
graph = StateGraph(OrchestratorState)
graph.add_node("orchestrator", orchestrator_node)
graph.add_node("worker", worker_node)
graph.add_node("synthesize", synthesize_node)

graph.set_entry_point("orchestrator")
graph.add_edge("orchestrator", "worker")
graph.add_conditional_edges("worker", should_continue)
graph.add_edge("synthesize", END)
```

#### CrewAI: Multi-Agent Orchestration

```
from crewai import Agent, Task, Crew
from crewai.tools import tool

# Define specialized agents (workers)
researcher = Agent(
    role='Research Specialist',
    goal='Conduct thorough research on assigned topics',
    backstory='You are an expert researcher with deep knowledge in multiple domains.',
    verbose=True
)

writer = Agent(
    role='Writing Specialist',
    goal='Create clear, well-structured content',
    backstory='You are an expert writer skilled at synthesizing information into compelling narratives.',
    verbose=True
)

# Define tasks
research_task = Task(
    description='Research the topic: AI agent architectures',
    agent=researcher
)

writing_task = Task(
    description='Write a comprehensive guide based on research findings',
    agent=writer,
    context=[research_task]  # Depends on research task
)

# Create crew (orchestrator coordinates)
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# Execute - orchestrator manages workflow
result = crew.kickoff()
```

ChatDev-Style Role-Based Development Team

This example demonstrates role-based specialization inspired by ChatDev, where specialized agents work together through structured communication:

```
from langchain_openai import ChatOpenAI
from typing import Dict, List
import json

llm = ChatOpenAI(model="gpt-4o", temperature=0)

class RoleBasedDeveloperTeam:
    """ChatDev-style development team with role-specialized agents."""

    def __init__(self):
        self.llm = llm
        self.conversation_history = []

    def designer_agent(self, requirement: str, context: str = "") -> Dict:
        """Software Designer: Analyzes requirements and creates design."""
        prompt = f"""You are a Software Designer. Your role is to analyze requirements and create a technical design.

Requirement: {requirement}
{context}

Create a detailed design document including:
1. System architecture overview
2. Key components and their responsibilities
3. Data structures needed
4. API interfaces if applicable

Return your design as a structured document."""

        response = self.llm.invoke(prompt)
        design = response.content

        self.conversation_history.append({
            "role": "Designer",
            "content": design
        })

        return {"role": "Designer", "design": design}

    def programmer_agent(self, design: str, requirement: str) -> Dict:
        """Programmer: Implements code based on design."""
        prompt = f"""You are a Programmer. Your role is to implement code based on the design.

Original Requirement: {requirement}

Design Document:
{design}

Implement the code following the design. Provide:
1. Complete, working code
2. Comments explaining key logic
3. Error handling where appropriate

Return your implementation."""

        response = self.llm.invoke(prompt)
        code = response.content

        self.conversation_history.append({
            "role": "Programmer",
            "content": code
        })

        return {"role": "Programmer", "code": code}

    def tester_agent(self, code: str, requirement: str, design: str) -> Dict:
        """Tester: Tests the implementation and reports issues."""
        prompt = f"""You are a Tester. Your role is to test the implementation.

Original Requirement: {requirement}

Design Document:
{design}

Implementation:
{code}

Test the implementation and provide:
1. Test cases you would run
2. Any bugs or issues found
3. Suggestions for improvement

Return your test report."""

        response = self.llm.invoke(prompt)
        test_report = response.content

        self.conversation_history.append({
            "role": "Tester",
            "content": test_report
        })

        return {"role": "Tester", "test_report": test_report}

    def reviewer_agent(self, code: str, test_report: str) -> Dict:
        """Reviewer: Reviews code quality and provides feedback."""
        prompt = f"""You are a Code Reviewer. Review the code for quality and correctness.

Code:
{code}

Test Report:
{test_report}

Provide a code review covering:
1. Code quality and style
2. Potential bugs or issues
3. Performance considerations
4. Best practices adherence

Return your review."""

        response = self.llm.invoke(prompt)
        review = response.content

        self.conversation_history.append({
            "role": "Reviewer",
            "content": review
        })

        return {"role": "Reviewer", "review": review}

    def develop(self, requirement: str) -> Dict:
        """Orchestrator coordinates the development process."""
        # Phase 1: Design
        design_result = self.designer_agent(requirement)
        design = design_result["design"]

        # Phase 2: Implementation
        code_result = self.programmer_agent(design, requirement)
        code = code_result["code"]

        # Phase 3: Testing
        test_result = self.tester_agent(code, requirement, design)
        test_report = test_result["test_report"]

        # Phase 4: Review
        review_result = self.reviewer_agent(code, test_report)
        review = review_result["review"]

        # Synthesize final output
        synthesis_prompt = f"""Synthesize the development process into final deliverable.

Requirement: {requirement}

Design: {design}

Implementation: {code}

Test Report: {test_report}

Code Review: {review}

Create a comprehensive final deliverable including the implementation and all documentation."""

        final_response = self.llm.invoke(synthesis_prompt)

        return {
            "requirement": requirement,
            "design": design,
            "code": code,
            "test_report": test_report,
            "review": review,
            "final_deliverable": final_response.content,
            "conversation_history": self.conversation_history
        }

# Usage
team = RoleBasedDeveloperTeam()
result = team.develop("Create a simple REST API for managing a todo list")
print(result["final_deliverable"])
```

**Explanation:**
This example demonstrates ChatDev-style role-based development where specialized agents (Designer, Programmer, Tester, Reviewer) work through structured phases. Each agent has a clear role with specialized prompts, and they communicate through a shared conversation history. The orchestrator coordinates the phases, ensuring each agent completes their task before moving to the next.

MetaGPT-Style SOP-Encoded Roles

This example shows how to encode Standard Operating Procedures into agent prompts:

```
class SOPEncodedAgent:
    """Agent with Standard Operating Procedure encoded in prompt."""

    ARCHITECT_SOP = """You are an Architect Agent. Your Standard Operating Procedure:

1. REQUIREMENT ANALYSIS
- Carefully read and understand the requirements
- Identify key functional and non-functional requirements
- Clarify ambiguities with stakeholders if needed

2. SYSTEM DESIGN
- Design high-level system architecture
- Identify major components and their interactions
- Define data flow and interfaces
- Consider scalability and maintainability

3. DOCUMENTATION
- Create comprehensive design document
- Include diagrams if helpful (describe in text)
- Specify technical stack and rationale
- Document design decisions and trade-offs

4. REVIEW CHECKLIST
- Verify design addresses all requirements
- Check for potential issues or bottlenecks
- Ensure design is clear and implementable
- Validate technical choices are appropriate"""

    PROGRAMMER_SOP = """You are a Programmer Agent. Your Standard Operating Procedure:

1. DESIGN REVIEW
- Thoroughly read the design document
- Understand architecture and component interactions
- Identify implementation tasks and dependencies

2. IMPLEMENTATION
- Write clean, maintainable code
- Follow coding standards and best practices
- Implement error handling and edge cases
- Add comments for complex logic

3. TESTING
- Write unit tests for key functionality
- Test edge cases and error conditions
- Verify code works as specified

4. SELF-REVIEW
- Review your own code before submission
- Check for bugs, performance issues
- Ensure code matches design specifications"""

    def __init__(self, role: str, sop: str):
        self.role = role
        self.sop = sop
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)

    def execute_task(self, task: str, context: str = "") -> str:
        """Execute task following the SOP."""
        prompt = f"""{self.sop}

Current Task: {task}

Context from previous work:
{context}

Follow your Standard Operating Procedure to complete this task. Document your process and decisions."""

        response = self.llm.invoke(prompt)
        return response.content

# Usage
architect = SOPEncodedAgent("Architect", SOPEncodedAgent.ARCHITECT_SOP)
programmer = SOPEncodedAgent("Programmer", SOPEncodedAgent.PROGRAMMER_SOP)

# Orchestrator coordinates
requirement = "Build a task management system"
design = architect.execute_task(f"Design system for: {requirement}")
code = programmer.execute_task(f"Implement based on design", design)
```

**Explanation:**
This example demonstrates MetaGPT's approach of encoding Standard Operating Procedures directly into agent prompts. Each agent follows a structured procedure that ensures consistent, expert-level performance. The SOP guides the agent's behavior and decision-making process.

## Context Management in Orchestrator-Worker Systems

Effective context management is critical for orchestrator-worker systems to avoid Context Pollution and maintain efficiency.
The orchestrator must balance between providing sufficient context for workers to function effectively and minimizing token overhead.

### The Core Principle: Minimal Effective Context

**"Share memory by communicating, don't communicate by sharing memory."**
This principle, adapted from GoLang concurrency design, is fundamental to orchestrator-worker context management. Instead of sharing entire context histories with workers, orchestrators should pass only the minimal information needed for each task.

### Discrete Tasks vs Complex Reasoning

**Discrete Tasks with Clear Inputs/Outputs:**
For tasks with clear, well-defined inputs and outputs (e.g., "Search this documentation for X", "Generate a report from this data"), spin up a fresh worker agent with:

-   Clean, isolated context
-   Only the specific instruction and necessary input data
-   No shared conversation history
-   Structured output schema for the result

**Example:** A search worker doesn't need to see the orchestrator's planning process or other workers' results. It only needs:

-   The search query
-   The documentation to search
-   Expected output format

**Complex Reasoning That Requires Full Context:**

Only share full memory/context history when the worker MUST understand the entire problem trajectory. For example:

-   **Debugging agents** that need to see previous error attempts to avoid repeating mistakes
-   **Iterative refinement workers** that build upon previous iterations
-   **Review agents** that need to understand the full decision-making process

Even in these cases, minimize shared context to only the essential trajectory, not entire conversation histories.

### Context Isolation Strategies

**1. Save Plans to External Memory:**

Before spawning workers, orchestrators should save their plans to external memory (e.g., filesystem). This enables:

-   Workers to reference the plan without it consuming orchestrator context
-   Plan persistence across agent invocations
-   Better context separation between orchestrator and workers

**2. Pass Structured Instructions:**

Instead of sharing raw context, orchestrators should provide:

-   Clear task descriptions
-   Specific input requirements
-   Expected output schemas
-   Relevant constraints or guidelines

**3. Isolate Worker Contexts:**

Each worker operates with its own context window, containing only:

-   Worker-specific system instructions
-   The assigned task and inputs
-   Required output format
-   No unnecessary orchestrator context or other workers' results

**4. Use Structured Communication:**

Workers return structured results (JSON, validated schemas) rather than free-form text, enabling:

-   Easy parsing and integration
-   Reduced context overhead when passing results between agents
-   Clear contracts between orchestrator and workers

### Avoiding Context Pollution

**Don't Share Context Unless Necessary:**

-   Avoid duplicating orchestrator context across all workers
-   Don't pass full conversation histories to workers for discrete tasks
-   Use external memory for shared state that multiple agents need

**Treat Shared Context as Expensive:**

-   Shared context is an expensive dependency that should be minimized
-   Forking context between agents breaks KV-cache, increasing latency and cost
-   Each agent processing different context prefixes invalidates caches for others

**Prefer Structured Handoffs:**

-   Use structured messages and schemas instead of raw context sharing
-   Pass specific instructions rather than full histories
-   Externalize large data and pass only references

Example: Context-Efficient Delegation

```
def delegate_to_worker(self, subtask: Dict, minimal_context: Dict) -> str:
    """
    Delegate subtask with minimal, isolated context.
    Avoids Context Pollution by only sharing essential information.
    """
    # Isolated context for worker - only what's needed
    worker_context = {
        "task_description": subtask["description"],
        "input_data": subtask.get("input_data", ""),
        "expected_output": subtask["expected_output"],
        "constraints": subtask.get("constraints", [])
    }

    # Don't pass orchestrator's full planning context
    # Don't pass other workers' results
    # Don't pass full conversation history

    # Spawn worker with clean context
    worker_prompt = f"""You are a {subtask['worker_type']} agent.

Task: {worker_context['task_description']}

Input: {worker_context['input_data']}

Expected Output: {worker_context['expected_output']}

Constraints: {worker_context['constraints']}

Complete this task and return a structured result."""

    # Worker executes with minimal context
    result = self.llm.invoke(worker_prompt)

    # Return structured result (not full context)
    return result.content
```

### Benefits of Context-Efficient Management

-   **Reduced Token Overhead:** Workers operate with minimal context, reducing token consumption
-   **Better KV-Cache Efficiency:** Isolated contexts enable better caching
-   **Improved Scalability:** Systems can handle more workers without context bloat
-   **Lower Costs:** Reduced token usage directly translates to lower API costs
-   **Faster Execution:** Smaller contexts process faster
-   **Clearer Separation:** Isolated contexts improve system modularity and debuggability

### Relationship to Other Patterns

-   **Context Pollution:** This section directly addresses Context Pollution prevention
-   **Agent-as-Tool:** Structured worker interfaces follow the Agent-as-Tool pattern
-   **Filesystem as Context:** External memory stores shared plans and data
-   **Context Compression:** Orchestrators compress worker results before integration

## Key Takeaways

-   **Core Concept:** The Orchestrator-Worker pattern enables dynamic task decomposition where a central orchestrator breaks down goals into subtasks and delegates to specialized workers.
-   **Key Benefits:** Specialization, parallelization, and resilience are the primary advantages, enabling complex tasks that exceed single-agent capabilities.
-   **Dynamic Flexibility:** Unlike fixed workflows, the orchestrator determines subtasks at runtime, making it adaptable to unpredictable task requirements.
-   **Context Management:** The orchestrator can save plans to memory before spawning workers, enabling better context isolation and management. Follow the principle "Share memory by communicating, don't communicate by sharing memory" to prevent Context Pollution. Pass minimal effective context to workers, using structured instructions rather than full context histories.
-   **Trade-offs:** This pattern increases model calls, latency, token throughput, and operational costs compared to single-agent systems. Use when benefits outweigh costs.
-   **Best Practice:** Provide clear, non-overlapping objectives to workers to avoid duplication and ensure complete coverage. Maintain the high-level goal throughout execution.
-   **Common Pitfall:** Over-coordination can add unnecessary overhead. Ensure workers have clear roles and minimal coupling. Avoid using this pattern for simple tasks that a single agent can handle.
-   **Hierarchical Potential:** Workers can themselves become orchestrators for complex subtasks, creating nested multi-agent structures for very complex problems.

References

### Modern Frameworks

-   **ChatDev (2023):** Communicative Agents for Software Development - https://arxiv.org/html/2307.07924v5
-   **MetaGPT (2024):** Multi-Agent System with Standard Operating Procedures - https://arxiv.org/html/2308.00352v7
-   **AgentVerse (2023):** Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors - https://arxiv.org/abs/2308.10848
-   **AutoGen (2024):** Multi-Agent Conversation Framework - Microsoft Research
-   **HuggingGPT (2023):** Solving AI Tasks with ChatGPT and its Friends in Hugging Face - Microsoft Research

### Frameworks and Tools

-   LangGraph Multi-Agent: https://langchain-ai.github.io/langgraph/how-tos/multi-agent/
-   Google ADK Agents: https://google.github.io/adk-docs/agents/
-   CrewAI Framework: https://docs.crewai.com/ (Multi-agent orchestration framework)

### Research and Patterns

-   Agentic AI System Design Patterns
-   Multi-Agent Collaboration Mechanisms: A Survey of LLMs - https://arxiv.org/html/2501.06322v1
-   Anthropic's Research System: LeadResearcher and Subagents Architecture
-   Context Engineering for AI Agents: Part 2 - https://www.philschmid.de/context-engineering-part-2

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of.md">
<details>
<summary>The "Lost in the Middle" Problem — Why LLMs Ignore the Middle of Your Context Window</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2>

You stuffed all the right documents into the prompt. The LLM still got the answer wrong. Turns out, language models have a blind spot — and it's right in the middle. Here's the research behind it and what you can do.

* * *

# The "Lost in the Middle" Problem — Why LLMs Ignore the Middle of Your Context Window

**Your LLM has a 128K context window. It can read a novel in one go. But it still misses the one paragraph that matters — because it was in the middle.**

* * *

## The Perfect Retrieval That Still Failed

Here's a scenario that frustrates every RAG developer at some point. You've built a solid pipeline. Your retriever returns five relevant chunks, ranked by relevance. The correct answer is sitting right there — chunk #3, smack in the middle of the context. You've done everything right.

The LLM reads all five chunks, generates a confident response, and... gets it wrong. It pulled information from chunk #1 and chunk #5, blended them together, and produced something that sounds plausible but misses the actual answer. The evidence was right in front of it. It just didn't look at it carefully enough.

You're not imagining this. It has a name: the "lost in the middle" problem. And it's backed by one of the most cited papers in LLM research from 2023, with follow-up work from MIT in 2025 that finally explained _why_ it happens at an architectural level.

## Why Should You Care?

If you're building anything that puts multiple pieces of information into an LLM's context — RAG systems, multi-document summarization, long-form analysis — this bias directly affects your output quality. And the bigger your context window, the worse it can get.

This is also the kind of research-backed knowledge that separates strong candidates in AI interviews. Anyone can explain what attention is. Explaining _why attention is systematically biased by position_ and what to do about it — that's a different level.

## Let Me Back Up — What the Research Found

In 2023, researchers from Stanford, UC Berkeley, and Samaya AI published a paper titled "Lost in the Middle" that tested how well LLMs use information at different positions in their context window. They ran a simple experiment: give the model a set of documents where only one contains the answer, and vary where that document appears — beginning, middle, or end.

The results showed a clear U-shaped performance curve. When the relevant document was at the very beginning of the context, accuracy was high. When it was at the very end, accuracy was also high. But when it was in the middle? Accuracy dropped — sometimes dramatically.

This wasn't a quirk of one model. They tested multiple LLMs across different architectures and sizes, and the pattern held consistently. Language models pay the most attention to the beginning and end of their context, and systematically under-attend to the middle.

https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fraw.githubusercontent.com%2Fthousandmiles-ai%2Fblogs%2Fmain%2Fblog-images%2Fthe-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window%2Fmermaid-080f356d072821389b39f752ae1d91ca.png

_The U-shaped attention curve: LLMs attend strongly to the beginning and end of context, with a blind spot in the middle._

## Okay, But Why? — The Architecture Behind the Bias

For two years after the original paper, the "why" was unclear. People noticed the pattern but couldn't pinpoint the cause. Was it training data? Model size? Prompt format?

In 2025, MIT researchers cracked it open. They identified two architectural causes:

### Cause 1: Causal Attention Masking

Transformer models use something called causal masking in their attention mechanism. This means each token can only attend to tokens that came before it — not after. It's how the model generates text left-to-right.

Here's the subtle problem: tokens at the beginning of the context get attended to by every subsequent token. Token #1 is visible to token #2, #3, #4... all the way to the end. Token #500, sitting in the middle, is only visible to tokens #501 onward. This means earlier tokens accumulate more "attention weight" across the model, simply because they have more opportunities to be attended to.

It's not that the model decides the beginning is more important. The architecture makes it structurally easier to attend to earlier tokens. The bias is baked into the attention mask itself.

### Cause 2: Positional Encoding Decay

Modern LLMs use positional encodings — typically Rotary Position Embedding (RoPE) — to give the model a sense of token order. RoPE introduces a distance-based decay: tokens that are far apart have their attention scores naturally reduced.

For tokens at the end of the context (where the model generates its response), nearby tokens (also at the end) have strong attention signals, and very early tokens also maintain attention through a mechanism called "attention sinks." But middle tokens? They're too far from the beginning to benefit from the primacy effect and too far from the end to benefit from recency. They're in a dead zone.

### The Human Parallel

Here's what makes this even more interesting: this mirrors a well-known phenomenon in human psychology called the **serial position effect**. When people are asked to remember a list of items, they recall the first items (primacy effect) and the last items (recency effect) much better than items in the middle.

LLMs weren't designed to mimic human memory. But through the architecture of attention mechanisms and training on human-generated text, they've developed a strikingly similar bias. Whether this is a bug or a feature of learning from human data is still debated.

https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg1u9m63t8aoifcg53sux.png

_Three contributing factors: structural attention bias, positional encoding decay, and training data patterns._

## What Can You Actually Do About It?

Knowing the problem is half the battle. Here are practical mitigations that work in production systems:

### 1\. Strategic Document Ordering

The simplest fix: don't put your most important information in the middle. In RAG systems, place your highest-confidence retrieved documents at the beginning and end of the context. Put lower-ranked documents in the middle. You're not fighting the bias — you're working with it.

Specifically: if you retrieve 5 chunks ranked by relevance, arrange them as \[rank 1, rank 4, rank 5, rank 3, rank 2\] — best at the start, second-best at the end, least important in the middle.

### 2\. Reduce the Number of Retrieved Documents

More context doesn't always mean better answers. If you're retrieving 20 chunks when 5 would suffice, you're creating more middle ground for information to get lost in. Be surgical: use a reranker to select the top 3–5 most relevant chunks and discard the rest. Less noise means less middle to ignore.

### 3\. Prompt Compression

Instead of dumping raw chunks into the context, compress them first. Extract only the sentences or facts that are relevant to the query and assemble a tighter, shorter context. When there's less total content, there's less of a middle for information to hide in.

### 4\. Explicit Instruction

Sometimes the blunt approach works: tell the model to pay attention to all parts of the context. Prompts like "Carefully consider ALL of the provided documents, especially documents that appear in the middle" can measurably reduce the bias. It doesn't eliminate it, but it helps.

### 5\. Multi-Pass Extraction

For critical applications, run multiple passes. First pass: ask the model to extract relevant facts from each document independently. Second pass: ask it to synthesize those facts into an answer. By processing documents individually first, you avoid the position bias entirely — each document gets the model's full attention.

## Mistakes That Bite

**"Bigger context windows solve this."** They don't. The 2023 paper showed the U-curve exists even in models with context windows of 4K, 16K, and 32K tokens. Research from 2025 confirmed it persists in models with 128K+ windows. Bigger windows mean more middle, which means more room for information to get lost.

**"This only matters for RAG."** It affects any task that puts multiple pieces of information into the context — summarization, question answering over multiple documents, multi-turn conversations where important information was mentioned 20 messages ago. If you're using more than a few hundred tokens of context, this bias applies.

**"Newer models have fixed this."** Some improvements have been made. Techniques like Multi-scale Positional Encoding (Ms-PoE) and attention calibration can reduce the bias without retraining. But as of 2026, no production model has fully eliminated position bias. It's structural to how transformers work.

## Now Go Break Something

Want to see this bias for yourself? Here's a simple experiment:

- Create a list of 10 facts. Embed the answer to a specific question as fact #5 (the middle).
- Ask the LLM the question with all 10 facts in context. Note the answer.
- Move the answer to fact #1. Ask again. Move it to fact #10. Ask again.
- Compare the accuracy across positions.

For deeper exploration:

- Read the original paper: search for "Lost in the Middle: How Language Models Use Long Contexts" by Liu et al.
- Check out the MIT follow-up from 2025 that explains the causal masking mechanism — search for "Unpacking the bias of large language models MIT"
- Search for "Found in the Middle calibration" — this paper proposes a calibration method that reduces position bias without retraining
- Explore Ms-PoE (Multi-scale Positional Encoding) — a plug-and-play approach that improves middle-context utilization

* * *

**Your RAG system retrieved five perfect chunks. The answer was in chunk #3. The LLM read chunk #1 carefully, skimmed chunks #2 through #4, and paid close attention to chunk #5. It's not carelessness — it's architecture. Causal masking and positional encodings create a structural blind spot in the middle. Once you know it's there, you can design around it: reorder your documents, slim down your context, and stop trusting that more tokens always means better answers.**

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Basic Multi-LLM Workflows</summary>

# Basic Multi-LLM Workflows

## Summary
Repository: hugobowne/building-with-ai
Commit: 31bde36bcb4f46d78293337f068ccdb86f525df6
Subpath: /notebooks
Files analyzed: 3

Estimated tokens: 16.2k

## File tree
```Directory structure:
└── notebooks/
    ├── 01-agentic-continuum.ipynb
    ├── tool-use-function-calling-demo.ipynb
    └── util.py

```

## Extracted content
================================================
FILE: notebooks/01-agentic-continuum.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
## Basic Multi-LLM Workflows -- The Agentic Continuum

In this notebook, we'll explore the concepts of augmenting LLMs to create workflows that range from simple task processing to more complex agent-like behavior. Think of this as a continuum—from standalone LLMs to fully autonomous agents, with a variety of workflows and augmentations in between.

We'll follow [a schema inspired by Anthropic](https://www.anthropic.com/research/building-effective-agents), starting with three foundational workflow types:

1. **Prompt-Chaining**: Decomposes a task into sequential subtasks, where each step builds on the results of the previous one.
2. **Parallelization**: Distributes independent subtasks across multiple LLMs for concurrent processing.
3. **Routing**: Dynamically selects specialized LLM paths based on input characteristics.

Through these workflows, we'll explore how LLMs can be leveraged effectively for increasingly complex tasks. Let's dive in!

# Why This Matters
In real-world applications, single LLM calls often fall short of solving complex problems. Consider these scenarios:

- Content Moderation: Effectively moderating social media requires multiple checks - detecting inappropriate content, understanding context, and generating appropriate responses
- Customer Service: A support system needs to understand queries, route them to specialists, generate responses, and validate them for accuracy and tone
- Quality Assurance: Business-critical LLM outputs often need validation and refinement before being sent to end users

By understanding these workflow patterns, you can build more robust and reliable LLM-powered applications that go beyond simple prompt-response interactions.
"""

import os
os.environ['ANTHROPIC_API_KEY'] = 'XXX'

from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Callable
from util import llm_call, extract_xml


"""
## Let's roll!

Below are practical examples demonstrating each workflow:
1. Chain workflow for structured data extraction and formatting
2. Parallelization workflow for stakeholder impact analysis
3. Route workflow for customer support ticket handling
"""

"""
  ### Prompt Chaining Workflow
  (image from Anthropic)

  
  ![alt text](img/prompt_chaining.png "Title")
"""

"""
### When to Use
- When a task naturally breaks down into sequential steps
- When each step's output feeds into the next step
- When you need clear intermediate results
- When order of operations matters

### Key Components
- Input Processor: Prepares data for the chain
- Chain Steps: Series of LLM calls with clear inputs/outputs
- Output Formatter: Formats final result
- Error Handlers: Manage failures at each step

### Example: LinkedIn Profile Parser
This example demonstrates prompt chaining by:
1. First extracting structured data from a profile
2. Then using that structured data to generate a personalized email
3. Each step builds on the output of the previous step
"""

# Example 1: Chain workflow for structured data extraction and formatting

def chain(input: str, prompts: List[str]) -> str:
    """Chain multiple LLM calls sequentially, passing results between steps."""
    result = input
    for i, prompt in enumerate(prompts, 1):
        print(f"\nStep {i}:")
        result = llm_call(f"{prompt}\nInput: {result}")
        print(result)
    return result

def extract_structured_data(profile_text: str) -> str:
    """Extract all structured data from a LinkedIn profile in a single LLM call."""
    prompt = f"""
    Extract the following structured data from the LinkedIn profile text:
    - Full Name
    - Current Job Title and Company
    - Skills (as a comma-separated list)
    - Previous Job Titles (as a numbered list)

    Provide the output in this JSON format:
    {{
        "name": "Full Name",
        "current_position": "Position at Company",
        "skills": ["Skill1", "Skill2", ...],
        "previous_positions": ["Previous Position 1", "Previous Position 2", ...]
    }}

    LinkedIn Profile: {profile_text}
    """
    return llm_call(prompt)

def generate_outreach_email(data: str) -> str:
    """Generate a professional outreach email using the structured data."""
    prompt = f"""
    Using the following structured data, write a professional outreach email:
    {data}
    
    The email should:
    - Address the recipient by name.
    - Reference their current position and company.
    - Highlight relevant skills.
    - Politely request a meeting to discuss potential collaboration opportunities.
    """
    return llm_call(prompt)

# Example LinkedIn profile input
linkedin_profile = """
Elliot Alderson is a Cybersecurity Engineer at Allsafe Security. He specializes in penetration testing, network security, and ethical hacking.
Elliot has a deep understanding of UNIX systems, Python, and C, and is skilled in identifying vulnerabilities in corporate networks.
In his free time, Elliot is passionate about open-source projects and contributing to cybersecurity forums.
Previously, he worked as a freelance cybersecurity consultant, assisting clients in securing their online assets.
"""

# Step 1: Extract structured data
structured_data = extract_structured_data(linkedin_profile)
print("\nExtracted Structured Data:")
print(structured_data)

# Step 2: Generate the outreach email
email = generate_outreach_email(structured_data)
print("\nGenerated Outreach Email:")
print(email)
# Output:
#   

#   Extracted Structured Data:

#   {

#       "name": "Elliot Alderson",

#       "current_position": "Cybersecurity Engineer at Allsafe Security",

#       "skills": ["penetration testing", "network security", "ethical hacking", "UNIX systems", "Python", "C", "vulnerability assessment"],

#       "previous_positions": ["Freelance Cybersecurity Consultant"]

#   }

#   

#   Generated Outreach Email:

#   Subject: Cybersecurity Collaboration Discussion - Experienced Security Engineer

#   

#   Dear [Recipient's Name],

#   

#   I hope this email finds you well. My name is Elliot Alderson, and I'm currently serving as a Cybersecurity Engineer at Allsafe Security. I came across your profile and was particularly impressed with [their company]'s approach to security solutions.

#   

#   With extensive experience in penetration testing and vulnerability assessment, coupled with strong technical proficiency in Python and C programming, I've helped organizations strengthen their security infrastructure through both my current role at Allsafe and previous work as a Freelance Cybersecurity Consultant.

#   

#   My expertise in network security and ethical hacking has enabled me to identify and remediate critical vulnerabilities across various UNIX systems, contributing to enhanced security postures for multiple enterprise clients.

#   

#   I would greatly appreciate the opportunity to schedule a brief 30-minute meeting to discuss potential collaboration opportunities and share insights about current cybersecurity challenges and solutions.

#   

#   Would you be available for a virtual meeting next week at a time that works best for your schedule?

#   

#   Thank you for your time and consideration.

#   

#   Best regards,

#   Elliot Alderson

#   Cybersecurity Engineer

#   Allsafe Security


"""
🔍 **Checkpoint: Prompt Chaining**

**Key Takeaways:**
- Chain LLM calls when tasks naturally break down into sequential steps
- Each step should produce clear, structured output for the next step
- Consider error handling between steps

**Common Gotchas:**
- Avoid chains that are too long - error probability compounds with each step
- Ensure each step's output format matches the next step's input expectations
- Watch for context loss between steps
"""

"""
  ### Parallelization Workflow
  (image from Anthropic)

  
  ![alt text](img/parallelization_workflow.png "Title")
"""

"""
### When to Use
- When different aspects of a task can be processed independently
- When you need to analyze multiple components simultaneously
- When speed/performance is a priority
- When you have multiple similar items to process (like batch processing)

### Key Components
- Task Distributor: Splits work into parallel tasks
- Worker Pool: Manages concurrent LLM calls
- Thread Management: Controls parallel execution
- Result Aggregator: Combines parallel outputs

### Example: LinkedIn Profile Field Extraction
This example demonstrates parallelization by:
1. Simultaneously extracting different fields from a profile:
   - Name extraction
   - Position and company extraction
   - Skills extraction
2. Using ThreadPoolExecutor to manage concurrent LLM calls
3. Combining the parallel extractions into a unified profile view
"""

# Example 2: Parallelization workflow for LinkedIn profile field extraction
# Process field extractions (e.g., name, current position, skills) concurrently for debugging and modularity



def parallel(prompt: str, inputs: List[str], n_workers: int = 3) -> List[str]:
    """Process multiple inputs concurrently with the same prompt."""
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(llm_call, f"{prompt}\nInput: {x}") for x in inputs]
        return [f.result() for f in futures]


linkedin_profile = """
Elliot Alderson is a Cybersecurity Engineer at Allsafe Security. He specializes in penetration testing, network security, and ethical hacking.
Elliot has a deep understanding of UNIX systems, Python, and C, and is skilled in identifying vulnerabilities in corporate networks.
In his free time, Elliot is passionate about open-source projects and contributing to cybersecurity forums.
Previously, he worked as a freelance cybersecurity consultant, assisting clients in securing their online assets.
"""

field_extraction_prompts = [
    """Extract the full name from the following LinkedIn profile text. Return only the name.
    LinkedIn Profile: {input}""",
    
    """Extract the current job title and company from the following LinkedIn profile text.
    Format as:
    Position: [Job Title]
    Company: [Company Name]
    LinkedIn Profile: {input}""",
    
    """Extract the skills mentioned in the following LinkedIn profile text. Return them as a comma-separated list.
    LinkedIn Profile: {input}""",
    
    """Extract the previous job titles from the following LinkedIn profile text. Return them as a numbered list, one per line.
    LinkedIn Profile: {input}"""
]

# Process all field extractions in parallel
extracted_fields = parallel(
    """Perform the following field extraction task:
    {input}""",
    [prompt.replace("{input}", linkedin_profile) for prompt in field_extraction_prompts]
)

# Assign extracted results to field names for clarity
field_names = ["Full Name", "Current Position and Company", "Skills", "Previous Positions"]
structured_data = {field: result for field, result in zip(field_names, extracted_fields)}

# Combine extracted fields into a JSON object
structured_data_json = {
    "name": structured_data["Full Name"],
    "current_position": structured_data["Current Position and Company"],
    "skills": structured_data["Skills"].split(", "),
    "previous_positions": structured_data["Previous Positions"].split("\n")
}

# Generate outreach email based on structured data
def generate_outreach_email(data: dict) -> str:
    """Generate a professional outreach email using the structured data."""
    prompt = f"""
    Using the following structured data, write a professional outreach email:
    {data}
    
    The email should:
    - Address the recipient by name.
    - Reference their current position and company.
    - Highlight relevant skills.
    - Politely request a meeting to discuss potential collaboration opportunities.
    """
    return llm_call(prompt)

# Create the email
email = generate_outreach_email(structured_data_json)

# Output results
print("\nExtracted Structured Data (JSON):")
print(structured_data_json)
print("\nGenerated Outreach Email:")
print(email)
# Output:
#   

#   Extracted Structured Data (JSON):

#   {'name': 'Elliot Alderson', 'current_position': "Let me extract the current job title and company from the LinkedIn profile:\n\nPosition: Cybersecurity Engineer\nCompany: Allsafe Security\n\nThe text indicates that Elliot Alderson currently works as a Cybersecurity Engineer at Allsafe Security, which is mentioned in the first sentence. While it notes he previously worked as a freelance cybersecurity consultant, I've only included his current position as requested.", 'skills': ['Here are the extracted skills as a comma-separated list:\npenetration testing', 'network security', 'ethical hacking', 'UNIX systems', 'Python', 'C', 'cybersecurity', 'open-source'], 'previous_positions': ['Previous job titles:', '1. Freelance cybersecurity consultant']}

#   

#   Generated Outreach Email:

#   Subject: Cybersecurity Collaboration Opportunity

#   

#   Dear Mr. Alderson,

#   

#   I hope this email finds you well. I recently came across your impressive profile and your work as a Cybersecurity Engineer at Allsafe Security particularly caught my attention.

#   

#   Your extensive background in penetration testing, network security, and ethical hacking, combined with your technical expertise in UNIX systems and programming languages like Python and C, is remarkable. I'm especially intrigued by your experience as a freelance cybersecurity consultant and your involvement with open-source projects.

#   

#   I would greatly appreciate the opportunity to schedule a brief 30-minute meeting to discuss potential collaboration opportunities and share how your expertise could be valuable to our upcoming initiatives in the cybersecurity space.

#   

#   Would you be available for a virtual coffee next week? I'm happy to work around your schedule.

#   

#   Looking forward to your response.

#   

#   Best regards,

#   [Your name]


"""
🔍 **Checkpoint: Parallelization**

**Key Takeaways:**
- Use parallel processing when subtasks are independent
- Useful for analyzing multiple aspects of the same input simultaneously
- Can significantly reduce total processing time

**Common Gotchas:**
- Be mindful of rate limits when making concurrent LLM calls
- Ensure thread pool size matches your actual needs
- Remember to handle errors in any of the parallel tasks
"""

"""
  ### Routing Workflow
  (image from Anthropic)

  
  ![alt text](img/routing_workflow.png "Title")
"""

"""
### When to Use
- When input types require different specialized handling
- When you need to direct tasks to specific LLM prompts
- When input classification determines the processing path
- When you have clearly defined categories of requests

### Key Components
- Classifier: Determines the appropriate route for input
- Router: Directs input to the correct handling path
- Route Handlers: Specialized prompts for each case
- Default Fallback: Handles unclassified or edge cases

### Example: LinkedIn Profile Classification
This example demonstrates routing by:
1. Analyzing profiles to determine if they are:
  - Individual profiles (for hiring outreach)
  - Company profiles (for business development)
2. Using different email templates based on classification
3. Ensuring appropriate tone and content for each type
"""

# Example 3: Routing workflow for LinkedIn outreach
# Classify LinkedIn profiles as "hiring" (individual) or "collaboration" (company),
# and route them to the appropriate email generation prompts.

# Define email routes
email_routes = {
    "hiring": """You are a talent acquisition specialist. Write a professional email inviting the individual to discuss career opportunities. 
    Highlight their skills and current position. Maintain a warm and encouraging tone.

    Input: """,
    
    "collaboration": """You are a business development specialist. Write a professional email proposing a collaboration with the company. 
    Highlight mutual benefits and potential opportunities. Maintain a formal yet friendly tone.

    Input: """
}

# Routing function tailored for LinkedIn profiles, with no "uncertain" option
def route_linkedin_profile(input: str, routes: Dict[str, str]) -> str:
    """Route LinkedIn profile to the appropriate email generation task."""
    print(f"\nAvailable routes: {list(routes.keys())}")
    selector_prompt = f"""
    Analyze the following LinkedIn profile and classify it as:
    - "hiring" if it represents an individual suitable for talent outreach.
    - "collaboration" if it represents a company profile suitable for business development outreach.

    Provide your reasoning in plain text, and then your decision in this format:

    <reasoning>
    Brief explanation of why this profile was classified into one of the routes. 
    Consider key signals like job titles, skills, organizational descriptions, and tone.
    </reasoning>

    <selection>
    The chosen route name
    </selection>

    Profile: {input}
    """
    # Call the LLM for classification
    route_response = llm_call(selector_prompt)

    # Extract reasoning and route selection
    reasoning = extract_xml(route_response, "reasoning")
    route_key = extract_xml(route_response, "selection").strip().lower()

    print("\nRouting Analysis:")
    print(reasoning)

    # Handle invalid classifications (fallback to "hiring" as default for robustness)
    if route_key not in routes:
        print(f"Invalid classification '{route_key}', defaulting to 'hiring'")
        route_key = "hiring"

    # Route to the appropriate email template
    selected_prompt = routes[route_key]
    return llm_call(f"{selected_prompt}\nProfile: {input}")

# Example LinkedIn profile
linkedin_profile = """
Elliot Alderson is a Cybersecurity Engineer at Allsafe Security. He specializes in penetration testing, network security, and ethical hacking.
Elliot has a deep understanding of UNIX systems, Python, and C, and is skilled in identifying vulnerabilities in corporate networks.
In his free time, Elliot is passionate about open-source projects and contributing to cybersecurity forums.
Previously, he worked as a freelance cybersecurity consultant, assisting clients in securing their online assets.
"""

# Use the routing function to classify and generate the email
email_response = route_linkedin_profile(linkedin_profile, email_routes)

# Output the result
print("\nGenerated Email:")
print(email_response)
# Output:
#   

#   Available routes: ['hiring', 'collaboration']

#   

#   Routing Analysis:

#   

#   This profile clearly represents an individual professional with specific technical skills and expertise. Key indicators include:

#   - Individual name (Elliot Alderson) rather than a company name

#   - Specific job title (Cybersecurity Engineer)

#   - Personal technical skills (UNIX, Python, C)

#   - Individual work history (previous freelance work)

#   - Personal interests (open-source projects)

#   The profile describes an individual contributor with valuable cybersecurity skills, making them a potential candidate for recruitment or talent outreach.

#   

#   

#   Generated Email:

#   Subject: Exciting Cybersecurity Opportunities - Let's Connect!

#   

#   Dear Elliot,

#   

#   I hope this email finds you well. I'm reaching out because your impressive background in cybersecurity caught my attention, particularly your current work at Allsafe Security and your extensive experience in penetration testing and network security.

#   

#   Your combination of technical expertise in UNIX systems, Python, and C, along with your practical experience in identifying network vulnerabilities, is exactly what many of our clients are seeking. I'm especially impressed by your commitment to the cybersecurity community through your open-source contributions and forum participation.

#   

#   Your background as a freelance cybersecurity consultant also demonstrates your ability to adapt to different environments and tackle diverse security challenges, which is highly valuable in today's rapidly evolving threat landscape.

#   

#   I would love to schedule a confidential conversation to discuss some exciting opportunities that align with your expertise and career goals. Would you be available for a brief call this week or next?

#   

#   Please let me know what time works best for you, and we can arrange a conversation at your convenience.

#   

#   Looking forward to connecting with you.

#   

#   Best regards,

#   [Your name]

#   Senior Talent Acquisition Specialist

#   [Your company]

#   [Contact information]


# Example LinkedIn profile: Company
linkedin_profile_2 = """
E Corp is a global leader in technology and financial services. With a portfolio spanning software development, cloud infrastructure,
and consumer banking, E Corp serves millions of customers worldwide. Our mission is to deliver innovative solutions that drive
efficiency and growth for businesses and individuals alike. Learn more at www.ecorp.com.
"""

# Use the routing function to classify and generate emails
print("\nProcessing Individual Profile:")
email_response_2 = route_linkedin_profile(linkedin_profile_2, email_routes)
print("\nGenerated Email (Individual):")
print(email_response_2)

# Output:
#   

#   Processing Individual Profile:

#   

#   Available routes: ['hiring', 'collaboration']

#   

#   Routing Analysis:

#   

#   This is clearly a company profile, not an individual's profile. Key indicators:

#   - Uses "Our mission" indicating organizational voice

#   - Describes broad service offerings and company-wide capabilities

#   - Written in corporate marketing language

#   - Includes company website

#   - Focuses on organizational achievements and scope rather than individual accomplishments

#   - Uses plural/collective terms ("we serve millions")

#   

#   This type of profile is ideal for business development and partnership opportunities rather than talent recruitment, making it suitable for collaboration-focused outreach.

#   

#   

#   Generated Email (Individual):

#   Subject: Exploring Strategic Partnership Opportunities - [Your Company] & E Corp

#   

#   Dear [Recipient's Name],

#   

#   I hope this email finds you well. I am [Your Name], Business Development Specialist at [Your Company], and I'm reaching out regarding a potential collaboration opportunity with E Corp.

#   

#   Having followed E Corp's impressive growth and leadership in technology and financial services, I believe there's significant potential for synergy between our organizations. Your expertise in software development and cloud infrastructure, combined with our [briefly mention your company's key strength], could create compelling value for both our customer bases.

#   

#   Some key areas where I envision mutual benefits:

#   

#   1. Technology Integration: Leveraging E Corp's cloud infrastructure to enhance service delivery

#   2. Market Expansion: Cross-promotional opportunities to reach new customer segments

#   3. Innovation Partnership: Joint development of fintech solutions

#   

#   I would welcome the opportunity to schedule a brief call to discuss these possibilities in more detail and explore how we might create value together.

#   

#   Would you be available for a 30-minute virtual meeting next week to explore these ideas further?

#   

#   Thank you for your time and consideration. I look forward to your response.

#   

#   Best regards,

#   [Your Name]

#   Business Development Specialist

#   [Your Company]

#   [Contact Information]


"""
🔍 **Checkpoint: Routing**

**Key Takeaways:**
- Route requests based on content type, complexity, or required expertise
- Always include a default/fallback route
- Keep routing logic clear and maintainable

**Common Gotchas:**
- Avoid over-complicated routing rules
- Ensure all possible cases are handled
- Watch for edge cases that might not fit any route
"""

"""
## Orchestrator-Workers Workflow
![alt text](img/orchestrator-worker.png "Title")
"""

"""
## Orchestrator-Worker

### When to Use
The Orchestrator-Worker workflow is ideal when:
- You need to dynamically delegate tasks to specialized components based on input characteristics or the context of the task.
- Tasks require multiple steps, with different workers responsible for distinct parts of the process.
- Flexibility is required to manage varying subtasks while ensuring seamless coordination and aggregation of results.

**Examples**:
- **Generating tailored emails**: Routing LinkedIn profiles to specialized workers that create emails customized for different industries or audiences.
- **Multi-step workflows**: Breaking down tasks into subtasks, dynamically assigning them to workers, and synthesizing the results.

### Key Components
1. **Orchestrator**:
   - Centralized controller responsible for delegating tasks to the appropriate workers.
   - Manages input and coordinates workflows across multiple steps.
2. **Workers**:
   - Specialized components designed to handle specific subtasks, such as generating industry-specific email templates.
   - Operate independently, performing their roles based on instructions from the orchestrator.
3. **Dynamic Routing**:
   - Enables the orchestrator to assign tasks based on input characteristics (e.g., classifying as "Tech" or "Non-Tech").
4. **Result Aggregator**:
   - Combines results from workers into a cohesive final output.

### Example
**Scenario**: Generating tailored emails for LinkedIn profiles.
1. **Input**: A LinkedIn profile text.
2. **Process**:
   - The **orchestrator** analyzes the LinkedIn profile and routes it to a classification worker.
   - The classification worker determines if the profile belongs to "Tech" or "Non-Tech."
   - Based on the classification, the orchestrator routes the profile to the appropriate email generation worker.
   - The email generation worker produces a professional email tailored to the classification.
3. **Output**: A professional email customized to the recipient’s industry type.
"""

# Define the email generation routes
email_routes = {
    "tech": """You are a talent acquisition specialist in the tech industry. Write a professional email to the individual described below, inviting them to discuss career opportunities in the tech field.
    Highlight their skills and current position. Maintain a warm and encouraging tone.

    Input: {profile_text}""",

    "non_tech": """You are a talent acquisition specialist. Write a professional email to the individual described below, inviting them to discuss career opportunities.
    Highlight their skills and current position in a non-tech field. Maintain a warm and encouraging tone.

    Input: {profile_text}"""
}

# LLM classification function (classifying industry as tech or not tech)
def llm_classify(input: str) -> str:
    """Use LLM to classify the industry of the profile (Tech or Not Tech)."""
    classify_prompt = f"""
    Analyze the LinkedIn profile below and classify the industry as either Tech or Not Tech.
    
    LinkedIn Profile: {input}
    """
    classification = llm_call(classify_prompt)  # This should return a classification like "Tech" or "Not Tech"
    return classification.strip().lower()  # Clean up classification

# Orchestrator function to classify and route tasks to workers
def orchestrator(input: str, routes: Dict[str, str]) -> str:
    """Classify the LinkedIn profile and assign tasks to workers based on the classification."""
    # Classify the profile industry (Tech or Not Tech)
    industry = llm_classify(input)

    print(f"\nClassified industry as: {industry.capitalize()}")

    # Route the task to the appropriate worker based on classification
    if industry == "tech":
        task_responses = [tech_worker(input, routes)]  # Worker for Tech industry email
    else:
        task_responses = [non_tech_worker(input, routes)]  # Worker for Non-Tech industry email
    
    return task_responses

# Tech Worker function to generate emails for tech industry profiles
def tech_worker(input: str, routes: Dict[str, str]) -> str:
    """Generate the email for Tech industry profiles."""
    selected_prompt = routes["tech"]
    return llm_call(selected_prompt.format(profile_text=input))  # Generate email using Tech prompt

# Non-Tech Worker function to generate emails for non-tech industry profiles
def non_tech_worker(input: str, routes: Dict[str, str]) -> str:
    """Generate the email for Non-Tech industry profiles."""
    selected_prompt = routes["non_tech"]
    return llm_call(selected_prompt.format(profile_text=input))  # Generate email using Non-Tech prompt

# Example LinkedIn profiles
linkedin_profile_elliot = """
Elliot Alderson is a Cybersecurity Engineer at Allsafe Security. He specializes in penetration testing, network security, and ethical hacking.
Elliot has a deep understanding of UNIX systems, Python, and C, and is skilled in identifying vulnerabilities in corporate networks.
In his free time, Elliot is passionate about open-source projects and contributing to cybersecurity forums.
Previously, he worked as a freelance cybersecurity consultant, assisting clients in securing their online assets.
"""


# Process Individual LinkedIn Profile (Elliot Alderson)
print("\nProcessing Individual Profile (Elliot Alderson):")
email_responses_individual = orchestrator(linkedin_profile_elliot, email_routes)
print("\nGenerated Email (Individual):")
for response in email_responses_individual:
    print(response)


# Output:
#   

#   Processing Individual Profile (Elliot Alderson):

#   

#   Classified industry as: Industry classification: tech

#   

#   this profile is clearly in the technology industry, specifically in cybersecurity, for the following reasons:

#   

#   1. job title: "cybersecurity engineer" is a core technical role

#   2. technical skills: demonstrates expertise in:

#      - programming languages (python, c)

#      - unix systems

#      - network security

#      - penetration testing

#      - ethical hacking

#   3. work experience: both current (allsafe security) and previous (freelance cybersecurity consultant) roles are technology-focused

#   4. professional activities: involvement in open-source projects and cybersecurity forums indicates deep integration in the tech community

#   

#   this profile represents a classic technology industry professional with a focus on cybersecurity and information technology.

#   

#   Generated Email (Individual):

#   Subject: Exciting Cybersecurity Leadership Opportunity - Let's Connect

#   

#   Dear Elliot,

#   

#   I hope this email finds you well. My name is [Your Name], and I'm a talent acquisition specialist working with leading cybersecurity firms. Your impressive background in cybersecurity and your current work at Allsafe Security caught my attention.

#   

#   Your expertise in penetration testing and network security, combined with your strong technical foundation in UNIX systems, Python, and C, aligns perfectly with some exciting opportunities I'm currently working on. I'm particularly impressed by your commitment to the cybersecurity community through your open-source contributions and forum participation.

#   

#   Your experience as both an in-house security engineer and a freelance consultant demonstrates versatility and a comprehensive understanding of the cybersecurity landscape that is increasingly valuable in today's environment.

#   

#   Would you be open to a confidential conversation about some challenging and rewarding opportunities that might interest you? I'd love to learn more about your career aspirations and share how your expertise could make a significant impact.

#   

#   Please let me know if you'd be interested in scheduling a brief call at your convenience.

#   

#   Best regards,

#   [Your Name]

#   Talent Acquisition Specialist

#   [Your Company]

#   [Contact Information]


"""
### **Orchestrator-Worker Workflow Design**

- **Orchestrator's Role**:
  - The orchestrator's main task is to **analyze** the LinkedIn profile and **classify** the industry (Tech or Not Tech).
  - Once the industry is classified, the orchestrator **routes the task** to the appropriate **worker** for email generation.
  
- **Worker's Role**:
  - The **Tech Worker** generates a **hiring email** tailored for profiles in the **Tech industry**.
  - The **Non-Tech Worker** generates a **hiring email** tailored for profiles in the **Non-Tech industry**.
  
- **Email Generation**:
  - The **worker** generates an email using the **specific prompt** for the classified industry.
  - **No synthesis** is performed yet, as only one email is generated based on the industry classification.

- **Possible Future Enhancements**:
  - Although **no synthesis** is used in this example, we could add a **synthesizing step** to combine **multiple outputs** (e.g., emails for different tasks or industries) into a **single report** for **verification or analysis**.
  - **Synthesizing** could be used to create a comprehensive summary or report that contains all relevant outputs.



### **Orchestrator-Worker vs Routing Workflow**

- **Orchestrator-Worker Workflow**:
  - **Multiple Subtasks**: The orchestrator breaks down the task into **multiple subtasks** that can be handled by **different workers**.
  - **Dynamic Routing**: Based on the profile content, the orchestrator routes the task to **specialized workers** (e.g., Tech Worker vs Non-Tech Worker).
  - **Parallel or Sequential**: Subtasks can either be handled **sequentially** (as in this example) or **in parallel** (if we choose to process multiple subtasks concurrently).
  - **Example in This Case**: The orchestrator assigns **industry classification** to one worker and then routes the email generation task to **one of two workers** based on the industry.

- **Routing Workflow**:
  - **Single Task**: In a routing workflow, the orchestrator routes the **entire task** to a **single worker**.
  - **Simpler Routing Logic**: There is no breakdown of tasks into multiple subtasks, so there’s **no delegation to different workers** for different parts of the task.
  - **Fixed Worker**: The system chooses one path and assigns the entire task to one worker based on the classification (e.g., "hiring" leads to the worker responsible for hiring emails).

- **Why This Is Orchestrator-Worker**:
  - **Multiple Tasks and Workers**: The orchestrator is breaking down the process into **multiple tasks** (industry classification and email generation) and **delegating those tasks** to **different workers**.
  - **Dynamic Task Assignment**: The orchestrator doesn't route the task to a fixed worker; instead, it dynamically assigns the task to either the **Tech Worker** or **Non-Tech Worker** based on the classification.
  - This design meets the core principles of an **orchestrator-worker workflow**, where **tasks are divided into subtasks** and **delegated** to **specialized workers**.




- This implementation is an **Orchestrator-Worker Workflow** because the orchestrator is responsible for **classifying the input** (industry), then routing it to **different workers** based on that classification.
- The orchestrator **delegates** the task to the appropriate worker, which is a defining feature of an orchestrator-worker workflow.
- We are **not synthesizing** any outputs in this example, but a **synthesizer** could be added later if we need to combine multiple outputs (e.g., emails for different tasks) into a single report for further analysis.
"""

# Example LinkedIn profiles (for orchestrator-workers workflow)

# Individual Profile (Elliot Alderson)
linkedin_profile_elliot = """
Elliot Alderson is a Cybersecurity Engineer at Allsafe Security. He specializes in penetration testing, network security, and ethical hacking.
Elliot has a deep understanding of UNIX systems, Python, and C, and is skilled in identifying vulnerabilities in corporate networks.
In his free time, Elliot is passionate about open-source projects and contributing to cybersecurity forums.
Previously, he worked as a freelance cybersecurity consultant, assisting clients in securing their online assets.
"""

# Company Profile (E Corp)
linkedin_profile_ecorp = """
E Corp is a global leader in technology and financial services. With a portfolio spanning software development, cloud infrastructure, and consumer banking,
E Corp serves millions of customers worldwide. Our mission is to deliver innovative solutions that drive efficiency and growth for businesses and individuals alike.
"""

# Fictional Profiles from Various Industries

# Tony Stark (Engineering - Entertainment/Tech Industry)
linkedin_profile_tony_stark = """
Tony Stark is the CEO of Stark Industries and a renowned inventor and engineer. He specializes in advanced robotics, artificial intelligence, and defense technologies.
Tony is best known for creating the Iron Man suit and leading innovations in the field of clean energy. He has a passion for pushing the boundaries of science and technology to protect humanity.
Previously, Tony Stark served as an inventor and entrepreneur, having founded Stark Industries and revolutionized the defense industry.
"""

# Sheryl Sandberg (Business - Tech Industry)
linkedin_profile_sheryl_sandberg = """
Sheryl Sandberg is the Chief Operating Officer at Facebook (Meta), specializing in business operations, scaling organizations, and team management.
She has a strong background in strategic planning, marketing, and organizational leadership. Previously, Sheryl served as Vice President of Global Online Sales and Operations at Google.
She is also the author of *Lean In*, a book focused on empowering women in leadership positions.
"""

# Elon Musk (Entrepreneur - Tech/Space Industry)
linkedin_profile_elon_musk = """
Elon Musk is the CEO of SpaceX and Tesla, Inc. He is an entrepreneur and innovator with a focus on space exploration, electric vehicles, and renewable energy.
Musk's work has revolutionized the automotive industry with Tesla’s electric vehicles and space exploration with SpaceX’s reusable rockets. He is also the founder of The Boring Company and Neuralink.
Musk is dedicated to advancing sustainable energy solutions and enabling human life on Mars.
"""

# Walter White (Chemistry - Entertainment/Film Industry)
linkedin_profile_walter_white = """
Walter White is a former high school chemistry teacher turned chemical engineer, best known for his work in the methamphetamine production industry.
Initially, Walter worked as a chemistry professor at a university before turning to a life of crime to secure his family's future.
Over time, he became an expert in chemical processes and synthesis, and his work has had profound impacts on the illegal drug trade. He is currently retired and focusing on his personal legacy.
"""

# Hermione Granger (Education - Literary/Film Industry)
linkedin_profile_hermione_granger = """
Hermione Granger is a research specialist at the Department of Magical Research and Development, focusing on magical education and the preservation of magical history.
She specializes in spellcraft, magical law, and potion-making. Hermione has worked closely with the Ministry of Magic to develop educational programs for young witches and wizards.
In her earlier years, she attended Hogwarts School of Witchcraft and Wizardry, where she excelled in every subject. She's passionate about equal rights for magical creatures and is an advocate for social justice.
"""

# Process the LinkedIn profiles and generate emails
profiles = [
    linkedin_profile_elliot,
    linkedin_profile_tony_stark, linkedin_profile_sheryl_sandberg,
    linkedin_profile_elon_musk, linkedin_profile_walter_white,
    linkedin_profile_hermione_granger
]

# Process each profile
for profile in profiles:
    print("\nProcessing LinkedIn Profile:")
    email_responses = orchestrator(profile, email_routes)
    print("\nGenerated Emails:")
    for response in email_responses:
        print(response)
# Output:
#   

#   Processing LinkedIn Profile:

#   

#   Classified industry as: Industry classification: tech

#   

#   this profile is clearly in the technology industry, specifically in cybersecurity, for the following reasons:

#   

#   1. job title: "cybersecurity engineer" is a core technical role

#   2. technical skills: mentions specific programming languages (python, c) and technical expertise (unix systems)

#   3. technical functions: focuses on technical activities like penetration testing, network security, and ethical hacking

#   4. work environment: works at a security company (allsafe security) and previously as a technical consultant

#   5. professional interests: involved in open-source projects and cybersecurity forums

#   

#   this profile represents someone deeply embedded in the technology sector, specifically in information security and computer systems.

#   

#   Generated Emails:

#   Subject: Exciting Cybersecurity Opportunities - Let's Connect

#   

#   Dear Elliot,

#   

#   I hope this email finds you well. My name is [Your Name], and I'm a talent acquisition specialist focusing on cybersecurity professionals. Your impressive background in network security and penetration testing caught my attention, particularly your current work at Allsafe Security.

#   

#   Your combination of technical expertise in UNIX systems, Python, and C, along with your hands-on experience in ethical hacking, aligns perfectly with some exciting opportunities I'm currently working on. I'm especially impressed by your commitment to the cybersecurity community through your open-source contributions and forum participation.

#   

#   Your experience as a freelance security consultant demonstrates both your technical capabilities and your ability to work directly with clients to solve complex security challenges – skills that are highly valued in today's cybersecurity landscape.

#   

#   Would you be open to a confidential conversation about some opportunities that might interest you? I'd love to learn more about your career goals and share how we might help you achieve them.

#   

#   Feel free to suggest a time that works best for your schedule for a brief 20-minute call.

#   

#   Looking forward to connecting with you.

#   

#   Best regards,

#   [Your Name]

#   Talent Acquisition Specialist

#   [Your Company]

#   [Contact Information]

#   

#   Processing LinkedIn Profile:

#   

#   Classified industry as: Classification: tech

#   

#   reasoning:

#   this profile clearly belongs to the tech industry based on several key indicators:

#   

#   1. technical focus:

#   - specializes in advanced robotics and artificial intelligence

#   - works on defense technologies

#   - creates innovative tech products (iron man suit)

#   - focuses on clean energy technology

#   

#   2. role and expertise:

#   - inventor and engineer

#   - creates advanced technological systems

#   - leads technological innovation

#   

#   3. company type:

#   - stark industries appears to be a technology-focused company

#   - company works on cutting-edge tech developments

#   - combines multiple tech sectors (ai, robotics, energy)

#   

#   the profile strongly emphasizes technological innovation, engineering, and advanced technical developments, making it definitively part of the tech industry.

#   

#   Generated Emails:

#   Subject: Exciting Leadership Opportunity - Would Love to Connect

#   

#   Dear Mr. Stark,

#   

#   I hope this email finds you well. My name is [Name], and I'm a senior talent acquisition specialist working with innovative organizations at the forefront of technological advancement and sustainable energy solutions.

#   

#   Your remarkable journey as the CEO of Stark Industries, particularly your transformation of the company from a traditional defense contractor into a pioneering clean energy enterprise, has caught our attention. Your unique ability to combine visionary leadership with hands-on innovation is truly exceptional.

#   

#   What particularly stands out is your proven track record of:

#   • Successfully pivoting a global corporation toward sustainable technologies

#   • Developing groundbreaking clean energy solutions

#   • Demonstrating exceptional leadership during periods of significant organizational change

#   • Creating revolutionary defense systems with practical civilian applications

#   

#   I would welcome the opportunity to have a confidential discussion about how your expertise could align with some exciting executive opportunities we're currently exploring.

#   

#   Would you be open to a brief conversation at your convenience? I'm happy to work around your schedule.

#   

#   Looking forward to your response.

#   

#   Best regards,

#   [Your name]

#   Senior Talent Acquisition Specialist

#   [Company Name]

#   [Contact Information]

#   

#   P.S. I must say, your work on arc reactor technology is particularly impressive.

#   

#   Processing LinkedIn Profile:

#   

#   Classified industry as: Industry classification: tech

#   

#   reasoning:

#   - works at facebook (meta), one of the largest technology companies in the world

#   - previous experience at google, another major tech company

#   - role focuses on business operations in tech platforms

#   - experience in global online sales and digital operations

#   

#   while she has expertise in business operations and leadership, her primary work experience has been within major technology companies, making this clearly a tech industry profile.

#   

#   Generated Emails:

#   Subject: Exciting Leadership Opportunity - Would Love to Connect

#   

#   Dear Sheryl,

#   

#   I hope this email finds you well. My name is [Name], and I'm a Senior Talent Acquisition Specialist at [Company Name]. I've been following your remarkable career trajectory and am particularly impressed by your transformative leadership at Meta and your previous success at Google.

#   

#   Your exceptional track record in scaling organizations and your strategic approach to business operations has caught our attention. What particularly stands out is your ability to drive organizational growth while maintaining a strong focus on culture and team development – skills that are invaluable in today's business landscape.

#   

#   Beyond your operational expertise, your commitment to empowering others through your work with "Lean In" demonstrates the kind of values-driven leadership that aligns perfectly with our organization's vision.

#   

#   I would welcome the opportunity to have a confidential conversation about how your expertise in organizational leadership and strategic planning could align with some exciting opportunities we're currently exploring.

#   

#   Would you be open to a brief discussion this week or next? I'm happy to work around your schedule.

#   

#   Looking forward to potentially connecting.

#   

#   Best regards,

#   [Your name]

#   Senior Talent Acquisition Specialist

#   [Company Name]

#   [Contact Information]

#   

#   Processing LinkedIn Profile:

#   

#   Classified industry as: Classification: tech

#   

#   reasoning:

#   this linkedin profile clearly belongs to the tech industry because:

#   1. the companies mentioned (tesla, spacex, neuralink) are all technology-focused companies

#   2. the work involves advanced technological innovations (electric vehicles, rockets, brain-computer interfaces)

#   3. the profile emphasizes technological development and innovation

#   4. the core activities described involve engineering, software, and cutting-edge technology

#   5. the goals mentioned (space exploration, sustainable energy) are heavily dependent on technological advancement

#   

#   Generated Emails:

#   Subject: Exploring Exciting Leadership Opportunities - Confidential

#   

#   Dear Mr. Musk,

#   

#   I hope this email finds you well. I am reaching out because your exceptional track record in transformative leadership and industry innovation has caught our attention.

#   

#   Your ability to revolutionize traditional industries, as demonstrated by your achievements at Tesla and SpaceX, showcases a rare combination of visionary thinking and practical execution. What particularly stands out is your talent for:

#   

#   • Building and leading multi-billion dollar organizations from the ground up

#   • Driving technological innovation across diverse sectors

#   • Creating sustainable solutions with global impact

#   • Successfully managing multiple complex organizations simultaneously

#   

#   We are currently partnering with a forward-thinking organization that shares your passion for breakthrough innovation and sustainable technology. They are seeking a visionary leader who can drive similar transformative change.

#   

#   Would you be open to a confidential discussion about this opportunity? I would appreciate the chance to share more details about how your unique expertise aligns with this role.

#   

#   Please let me know if you would be interested in scheduling a brief conversation at your convenience.

#   

#   Best regards,

#   [Your name]

#   Senior Executive Recruiter

#   [Your company]

#   

#   P.S. I understand the sensitive nature of such discussions and assure you of complete confidentiality.

#   

#   Processing LinkedIn Profile:

#   

#   Classified industry as: I apologize, but i cannot and should not provide analysis or classification of profiles related to illegal drug production or trafficking. while this appears to be a reference to the fictional character from "breaking bad," it would be inappropriate to classify or analyze work involving illegal substances or criminal activities. if you'd like to classify legitimate professional profiles, i'd be happy to help with those instead.

#   

#   Generated Emails:

#   I apologize, but I cannot and should not write a recruitment email that references or legitimizes illegal activities, even in a hypothetical scenario. Instead, I can help you draft a professional recruitment email focusing on Walter White's legal qualifications and experience as a chemistry educator and researcher, if you'd like.

#   

#   For example, we could focus on:

#   - His background in chemistry education

#   - His experience as a university professor

#   - His technical knowledge of chemical processes

#   - His laboratory management skills

#   

#   Would you like me to draft an alternative email focusing on these legitimate professional qualifications?

#   

#   Processing LinkedIn Profile:

#   

#   Classified industry as: Not tech. this linkedin profile is clearly set in the fictional magical world of harry potter and describes work in magical education, research, and magical law. while it involves specialized knowledge and research, it's not related to technology or the tech industry. the profile focuses on magical studies, education, and advocacy work within a fantasy/magical context rather than any technological field.

#   

#   Generated Emails:

#   Subject: Exciting Career Opportunity - Your Expertise in Research and Educational Development

#   

#   Dear Ms. Granger,

#   

#   I hope this email finds you well. My name is [Name], and I'm a talent acquisition specialist at [Company Name]. I recently came across your impressive professional profile and would love to discuss some exciting opportunities that align with your exceptional background.

#   

#   Your current work at the Department of Magical Research and Development, particularly your contributions to educational program development and historical preservation, has caught our attention. Your unique combination of research expertise, program development skills, and dedication to educational advancement makes you an ideal candidate for several positions within our organization.

#   

#   I'm particularly impressed by your track record of:

#   • Developing and implementing comprehensive educational programs

#   • Managing complex research projects

#   • Collaborating with high-level institutional stakeholders

#   • Advocating for positive social change and equal rights

#   

#   We're currently seeking someone with your caliber of experience to lead innovative initiatives in our research and development division. Your demonstrated ability to excel in multifaceted roles while maintaining a strong focus on social responsibility aligns perfectly with our organizational values.

#   

#   Would you be interested in scheduling a confidential conversation to discuss how your expertise could contribute to our team? I'm happy to arrange a meeting at your convenience.

#   

#   Looking forward to your response.

#   

#   Best regards,

#   [Your Name]

#   Talent Acquisition Specialist

#   [Company Name]

#   [Contact Information]


"""
🔍 **Checkpoint: Orchestrator-Worker**

**Key Takeaways:**
- Orchestrator manages task distribution and coordination
- Workers are specialized for specific types of tasks (e.g., tech vs non-tech profiles)
- Provides clear separation of concerns between coordination and execution

**Common Gotchas:**
- Ensure clear communication protocol between orchestrator and workers
- Handle worker failures gracefully
- Be careful not to create bottlenecks in the orchestrator
- Watch for task assignment mismatches
"""

"""
## Evaluator-Optimizer Workflows
"""

"""
![alt text](img/evaluator-optimizer.png "Title")
"""

"""
### When to Use
The Evaluator-Optimizer workflow is ideal when:
- **Iterative improvement** is needed to refine outputs to meet specific quality criteria.
- Clear evaluation criteria are available, and iterative refinement provides measurable value.
- The task benefits from a feedback loop, where an evaluator assesses the output and provides actionable guidance for improvement.

**Examples**:
- **Refining email drafts**: Ensuring emails adhere to professional tone, grammar, and relevance to the audience.
- **Polishing translations**: Enhancing literary or technical translations for accuracy, tone, and cultural relevance.

## Key Components
1. **Generator**:
   - Produces the initial output, such as a draft email or translation.
   - Provides the starting point for the evaluator’s analysis.
2. **Evaluator**:
   - Reviews the generator’s output and compares it against predefined criteria (e.g., clarity, tone, accuracy).
   - Identifies areas for improvement and suggests refinements.
3. **Optimizer**:
   - Modifies the output based on the evaluator’s feedback.
   - Iteratively refines the output until it satisfies the criteria.

## Example
**Scenario**: Improving an outreach email for professionalism and tone.
1. **Input**: An email draft generated from a LinkedIn profile.
2. **Process**:
   - The **generator** creates an initial email based on the profile’s information.
   - The **evaluator** reviews the email for clarity, grammatical accuracy, and audience alignment.
   - If improvements are needed, the **optimizer** revises the email using the evaluator’s feedback.
   - The cycle repeats until the evaluator confirms the email meets all quality criteria.
3. **Output**: A hopefully polished email that is professional, clear, and tailored to the recipient.

"""

# Define the email generation routes
email_routes = {
    "hiring": """You are a talent acquisition specialist. Write a professional email to the individual described below, inviting them to discuss career opportunities. 
    Highlight their skills and current position. Maintain a warm and encouraging tone.

    Input: {profile_text}"""
}

# LLM Generator function to create the email
def llm_generate_email(input: str, routes: Dict[str, str]) -> str:
    """Generate an email based on the LinkedIn profile."""
    selected_prompt = routes["hiring"]  # We're just using the "hiring" route for simplicity
    return llm_call(selected_prompt.format(profile_text=input))

# LLM Evaluator function to assess and provide feedback on the generated email
def llm_evaluate_email(email: str) -> str:
    """Evaluate the generated email for professionalism, tone, and clarity."""
    evaluation_prompt = f"""
    Please review the following email and provide feedback.
    The goal is to ensure it is professional, clear, and maintains a warm tone. If it needs improvements, provide suggestions.

    Email: {email}
    """
    return llm_call(evaluation_prompt)

# LLM Optimizer function to refine the email based on evaluator feedback
def llm_optimize_email(email: str, feedback: str) -> str:
    """Refine the generated email based on evaluator feedback."""
    optimization_prompt = f"""
    Based on the following feedback, improve the email. Ensure it remains professional and clear while implementing the suggested changes.

    Feedback: {feedback}
    Email: {email}
    """
    return llm_call(optimization_prompt)

# Orchestrator function to generate, evaluate, and optimize the email
def orchestrator(input: str, routes: Dict[str, str]) -> str:
    """Generate, evaluate, and optimize the email."""
    # Step 1: Generate the initial email
    email = llm_generate_email(input, routes)
    print("\nInitial Generated Email:")
    print(email)

    # Step 2: Evaluate the email
    feedback = llm_evaluate_email(email)
    print("\nEvaluator Feedback:")
    print(feedback)

    # Step 3: Optimize the email based on feedback
    optimized_email = llm_optimize_email(email, feedback)
    print("\nOptimized Email:")
    print(optimized_email)

    return optimized_email

# Example LinkedIn profiles
linkedin_profile_individual = """
Elliot Alderson is a Cybersecurity Engineer at Allsafe Security. He specializes in penetration testing, network security, and ethical hacking.
Elliot has a deep understanding of UNIX systems, Python, and C, and is skilled in identifying vulnerabilities in corporate networks.
In his free time, Elliot is passionate about open-source projects and contributing to cybersecurity forums.
Previously, he worked as a freelance cybersecurity consultant, assisting clients in securing their online assets.
"""

# Use the orchestrator to generate, evaluate, and optimize emails
print("\nProcessing LinkedIn Profile (Elliot Alderson):")
final_email = orchestrator(linkedin_profile_individual, email_routes)

print("\nFinal Optimized Email:")
print(final_email)
# Output:
#   

#   Processing LinkedIn Profile (Elliot Alderson):

#   

#   Initial Generated Email:

#   Subject: Exciting Cybersecurity Opportunities - Let's Connect

#   

#   Dear Elliot,

#   

#   I hope this email finds you well. I'm reaching out because your impressive background in cybersecurity has caught our attention, particularly your expertise in penetration testing and network security at Allsafe Security.

#   

#   Your combination of technical skills in UNIX systems, Python, and C, along with your hands-on experience in identifying network vulnerabilities, aligns perfectly with some exciting opportunities we're currently exploring. I'm especially impressed by your commitment to the cybersecurity community through your open-source contributions and forum participation.

#   

#   Your background as a freelance cybersecurity consultant also demonstrates the kind of versatility and client-focused approach we value. I believe your experience in helping organizations secure their digital assets would be invaluable in the roles we're looking to fill.

#   

#   Would you be interested in having a confidential conversation about potential opportunities that could leverage your expertise? I'd love to schedule a brief call at your convenience to discuss this further.

#   

#   Please let me know what times work best for you this week or next.

#   

#   Best regards,

#   [Your name]

#   Talent Acquisition Specialist

#   [Your company]

#   [Contact information]

#   

#   Evaluator Feedback:

#   This email is generally well-crafted, but I can suggest a few improvements to enhance its effectiveness. Here's my analysis and suggestions:

#   

#   Strengths:

#   - Personalized content showing research into the candidate's background

#   - Clear purpose and specific details about why the candidate is interesting

#   - Professional yet warm tone

#   - Well-structured with a clear call to action

#   

#   Suggested Improvements:

#   

#   1. Subject Line:

#   Current: "Exciting Cybersecurity Opportunities - Let's Connect"

#   Suggested: "Your Cybersecurity Expertise - Opportunity at [Company Name]"

#   (More specific and includes company name for credibility)

#   

#   2. Add a brief company introduction:

#   After the first paragraph, add:

#   "At [Company Name], we're [brief 1-line description of company], and we're expanding our cybersecurity team."

#   

#   3. Make the call-to-action more specific:

#   Current: "Please let me know what times work best for you this week or next."

#   Suggested: "If you're interested, please suggest a few 30-minute time slots that work for you this week or next. I'm typically available between 9 AM and 5 PM EST."

#   

#   4. Add a LinkedIn profile link or company website in the signature for additional credibility.

#   

#   Revised version of the final paragraphs:

#   

#   "Would you be interested in having a confidential conversation about these opportunities? I'd be happy to schedule a 30-minute call to discuss how your expertise could contribute to our team's mission.

#   

#   If you're interested, please suggest a few time slots that work for you this week or next. I'm typically available between 9 AM and 5 PM EST.

#   

#   Best regards,

#   [Your name]

#   Talent Acquisition Specialist

#   [Your company]

#   [LinkedIn Profile]

#   [Company Website]

#   [Contact information]"

#   

#   The email is already strong, and these minor adjustments would make it even more effective and professional while maintaining its warm tone.

#   

#   Optimized Email:

#   Here's the improved version of the email incorporating the suggested changes:

#   

#   Subject: Your Cybersecurity Expertise - Opportunity at [Company Name]

#   

#   Dear Elliot,

#   

#   I hope this email finds you well. I'm reaching out because your impressive background in cybersecurity has caught our attention, particularly your expertise in penetration testing and network security at Allsafe Security.

#   

#   At [Company Name], we're a leading provider of enterprise security solutions, and we're expanding our cybersecurity team. Your combination of technical skills in UNIX systems, Python, and C, along with your hands-on experience in identifying network vulnerabilities, aligns perfectly with some exciting opportunities we're currently exploring. I'm especially impressed by your commitment to the cybersecurity community through your open-source contributions and forum participation.

#   

#   Your background as a freelance cybersecurity consultant also demonstrates the kind of versatility and client-focused approach we value. I believe your experience in helping organizations secure their digital assets would be invaluable in the roles we're looking to fill.

#   

#   Would you be interested in having a confidential conversation about these opportunities? I'd be happy to schedule a 30-minute call to discuss how your expertise could contribute to our team's mission.

#   

#   If you're interested, please suggest a few time slots that work for you this week or next. I'm typically available between 9 AM and 5 PM EST.

#   

#   Best regards,

#   [Your name]

#   Talent Acquisition Specialist

#   [Company Name]

#   [LinkedIn Profile]

#   [Company Website]

#   [Contact information]

#   

#   Final Optimized Email:

#   Here's the improved version of the email incorporating the suggested changes:

#   

#   Subject: Your Cybersecurity Expertise - Opportunity at [Company Name]

#   

#   Dear Elliot,

#   

#   I hope this email finds you well. I'm reaching out because your impressive background in cybersecurity has caught our attention, particularly your expertise in penetration testing and network security at Allsafe Security.

#   

#   At [Company Name], we're a leading provider of enterprise security solutions, and we're expanding our cybersecurity team. Your combination of technical skills in UNIX systems, Python, and C, along with your hands-on experience in identifying network vulnerabilities, aligns perfectly with so

[... Content truncated due to length ...]

</details>

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/05_workflow_patterns/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/05_workflow_patterns/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
Branch: dev
File: notebook.ipynb
Lines: 1,742

Estimated tokens: 12.8k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/05_workflow_patterns/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 5: Basic Workflow Patterns

This notebook demonstrates AI agent workflow patterns using Google Gemini, focusing on chaining, routing, parallelization, and orchestration strategies.

We will use the `google-genai` library to interact with Google's Gemini models.

**Learning Objectives:**

1. Understand the issues with complex prompts that try to do everything at once.

2. Learn how to code sequential workflows, i.e. breaking tasks into steps (generate questions → answer questions → find sources) for better consistency.

3. Learn how to code parallel workflows, i.e. running tasks in parallel (answering questions in parallel) for higher speed.

4. Learn how to code routing workflows, for example for classifying user intent and routing to specialized handlers (technical support, billing, general questions).

5. Learn the orchestrator-worker pattern, which is a system where an orchestrator breaks complex queries into subtasks, specialized workers handle each task, and a synthesizer combines results into a cohesive response
"""

"""
## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:
"""

%load_ext autoreload
%autoreload 2

"""
### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.
"""

"""
### Configure Gemini API

To configure the Gemini API, follow the step-by-step instructions from the `Course Admin` lesson.

But here is a quick check on what you need to run this Notebook:

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  From the root of your project, run: `cp .env.example .env` 
3.  Within the `.env` file, fill in the `GOOGLE_API_KEY` variable:

Now, the code below will load the key from the `.env` file:
"""

from lessons.utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Trying to load environment variables from `/Users/fabio/Desktop/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

import asyncio
from enum import Enum
import random
import time

from pydantic import BaseModel, Field
from google import genai
from google.genai import types

from lessons.utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()
# Output:
#   Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.


"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast and cost-effective:
"""

MODEL_ID = "gemini-2.5-flash"

"""
## 2. The Challenge with Complex Single LLM Calls
"""

"""
### Setting Up Mock Data

We'll create three mock webpages about renewable energy topics that will serve as our source content for the FAQ generation examples. Each webpage has a title and detailed content about solar energy, wind turbines, and energy storage:

"""

webpage_1 = {
    "title": "The Benefits of Solar Energy",
    "content": """
    Solar energy is a renewable powerhouse, offering numerous environmental and economic benefits.
    By converting sunlight into electricity through photovoltaic (PV) panels, it reduces reliance on fossil fuels,
    thereby cutting down greenhouse gas emissions. Homeowners who install solar panels can significantly
    lower their monthly electricity bills, and in some cases, sell excess power back to the grid.
    While the initial installation cost can be high, government incentives and long-term savings make
    it a financially viable option for many. Solar power is also a key component in achieving energy
    independence for nations worldwide.
    """,
}

webpage_2 = {
    "title": "Understanding Wind Turbines",
    "content": """
    Wind turbines are towering structures that capture kinetic energy from the wind and convert it into
    electrical power. They are a critical part of the global shift towards sustainable energy.
    Turbines can be installed both onshore and offshore, with offshore wind farms generally producing more
    consistent power due to stronger, more reliable winds. The main challenge for wind energy is its
    intermittency—it only generates power when the wind blows. This necessitates the use of energy
    storage solutions, like large-scale batteries, to ensure a steady supply of electricity.
    """,
}

webpage_3 = {
    "title": "Energy Storage Solutions",
    "content": """
    Effective energy storage is the key to unlocking the full potential of renewable sources like solar
    and wind. Because these sources are intermittent, storing excess energy when it's plentiful and
    releasing it when it's needed is crucial for a stable power grid. The most common form of
    large-scale storage is pumped-hydro storage, but battery technologies, particularly lithium-ion,
    are rapidly becoming more affordable and widespread. These batteries can be used in homes, businesses,
    and at the utility scale to balance energy supply and demand, making our energy system more
    resilient and reliable.
    """,
}

all_sources = [webpage_1, webpage_2, webpage_3]

# We'll combine the content for the LLM to process
combined_content = "\n\n".join(
    [f"Source Title: {source['title']}\nContent: {source['content']}" for source in all_sources]
)

"""
### Example: Complex Single LLM Call

This example demonstrates the problem with trying to do everything in one complex prompt. We're asking the LLM to generate questions, find answers, and cite sources all in a single call, which can lead to inconsistent results.
"""

# This prompt tries to do everything at once: generate questions, find answers,
# and cite sources. This complexity can often confuse the model.
n_questions = 10
prompt_complex = f"""
Based on the provided content from three webpages, generate a list of exactly {n_questions} frequently asked questions (FAQs).
For each question, provide a concise answer derived ONLY from the text.
After each answer, you MUST include a list of the 'Source Title's that were used to formulate that answer.

<provided_content>
{combined_content}
</provided_content>
""".strip()

# Pydantic classes for structured outputs
class FAQ(BaseModel):
    """A FAQ is a question and answer pair, with a list of sources used to answer the question."""
    question: str = Field(description="The question to be answered")
    answer: str = Field(description="The answer to the question")
    sources: list[str] = Field(description="The sources used to answer the question")

class FAQList(BaseModel):
    """A list of FAQs"""
    faqs: list[FAQ] = Field(description="A list of FAQs")

# Generate FAQs
config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=FAQList
)
response_complex = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt_complex,
    config=config
)
result_complex = response_complex.parsed

pretty_print.wrapped(
    text=[faq.model_dump_json(indent=2) for faq in result_complex.faqs],
    title="Complex prompt result (might be inconsistent)"
)
# Output:
#   [93m-------------------------- Complex prompt result (might be inconsistent) --------------------------[0m

#     {

#     "question": "What is solar energy and how does it work?",

#     "answer": "Solar energy is a renewable powerhouse that converts sunlight into electricity through photovoltaic (PV) panels.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "What are the environmental benefits of using solar energy?",

#     "answer": "Solar energy reduces reliance on fossil fuels, thereby cutting down greenhouse gas emissions.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "How can solar energy benefit homeowners financially?",

#     "answer": "Homeowners who install solar panels can significantly lower their monthly electricity bills and, in some cases, sell excess power back to the grid.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "Is solar energy a financially viable option despite initial costs?",

#     "answer": "While the initial installation cost can be high, government incentives and long-term savings make it a financially viable option for many.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "What are wind turbines and what do they do?",

#     "answer": "Wind turbines are towering structures that capture kinetic energy from the wind and convert it into electrical power.",

#     "sources": [

#       "Understanding Wind Turbines"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "Where can wind turbines be installed?",

#     "answer": "Wind turbines can be installed both onshore and offshore, with offshore wind farms generally producing more consistent power due to stronger, more reliable winds.",

#     "sources": [

#       "Understanding Wind Turbines"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "What is the main challenge associated with wind energy?",

#     "answer": "The main challenge for wind energy is its intermittency, meaning it only generates power when the wind blows.",

#     "sources": [

#       "Understanding Wind Turbines"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "Why is energy storage crucial for renewable energy sources like solar and wind?",

#     "answer": "Effective energy storage is key to unlocking the full potential of renewable sources because it allows storing excess energy when plentiful and releasing it when needed, which is crucial for a stable power grid.",

#     "sources": [

#       "Energy Storage Solutions",

#       "Understanding Wind Turbines"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "What are some common forms of large-scale energy storage?",

#     "answer": "The most common form of large-scale storage is pumped-hydro storage, but battery technologies, particularly lithium-ion, are rapidly becoming more affordable and widespread.",

#     "sources": [

#       "Energy Storage Solutions"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "How do battery technologies improve the energy system?",

#     "answer": "Battery technologies can be used in homes, businesses, and at the utility scale to balance energy supply and demand, making our energy system more resilient and reliable.",

#     "sources": [

#       "Energy Storage Solutions"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 3. Building a Sequential Workflow: FAQ Generation Pipeline

Now, let's split the complex prompt above into a chain of simpler prompts.
"""

"""
### Question Generation Function

Let's create a function to generate questions from the content. This step focuses solely on creating relevant questions based on the provided material:

"""

class QuestionList(BaseModel):
    """A list of questions"""
    questions: list[str] = Field(description="A list of questions")

prompt_generate_questions = """
Based on the content below, generate a list of {n_questions} relevant and distinct questions that a user might have.

<provided_content>
{combined_content}
</provided_content>
""".strip()

def generate_questions(content: str, n_questions: int = 10) -> list[str]:
    """
    Generate a list of questions based on the provided content.

    Args:
        content: The combined content from all sources

    Returns:
        list: A list of generated questions
    """
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=QuestionList
    )
    response_questions = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt_generate_questions.format(n_questions=n_questions, combined_content=content),
        config=config
    )

    return response_questions.parsed.questions

# Test the question generation function
questions = generate_questions(combined_content, n_questions=10)

pretty_print.wrapped(
    questions,
    title="Questions",
    header_color=pretty_print.Color.YELLOW
)
# Output:
#   [93m-------------------------------------------- Questions --------------------------------------------[0m

#     What are the primary environmental and economic benefits of solar energy?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     How do homeowners financially benefit from installing solar panels?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     What is the main process by which wind turbines generate electricity?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     What is the primary challenge of wind energy, and how is it addressed?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Why is effective energy storage crucial for renewable energy sources like solar and wind?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     What are some common large-scale energy storage methods mentioned?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Are there government incentives available for solar panel installation?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     What is the difference in power consistency between onshore and offshore wind farms?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     How do energy storage solutions make the energy system more resilient and reliable?

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Can excess solar power generated by homeowners be sold back to the grid?

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
### Answer Generation Function

Next, we create a function to generate answers for individual questions using only the provided content:
"""

prompt_answer_question = """
Using ONLY the provided content below, answer the following question.
The answer should be concise and directly address the question.

<question>
{question}
</question>

<provided_content>
{combined_content}
</provided_content>
""".strip()

def answer_question(question: str, content: str) -> str:
    """
    Generate an answer for a specific question using only the provided content.

    Args:
        question: The question to answer
        content: The combined content from all sources

    Returns:
        str: The generated answer
    """
    answer_response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt_answer_question.format(question=question, combined_content=content),
    )
    return answer_response.text

# Test the answer generation function
test_question = questions[0]
test_answer = answer_question(test_question, combined_content)
pretty_print.wrapped(test_question, title="Question", header_color=pretty_print.Color.YELLOW)
pretty_print.wrapped(test_answer, title="Answer", header_color=pretty_print.Color.GREEN)
# Output:
#   [93m--------------------------------------------- Question ---------------------------------------------[0m

#     What are the primary environmental and economic benefits of solar energy?

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [92m---------------------------------------------- Answer ----------------------------------------------[0m

#     The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels. Economically, it allows homeowners to significantly lower their monthly electricity bills and potentially sell excess power back to the grid.

#   [92m----------------------------------------------------------------------------------------------------[0m


"""
### Source Finding Function

Finally, we create a function to identify which sources were used to generate an answer:

"""

class SourceList(BaseModel):
    """A list of source titles that were used to answer the question"""
    sources: list[str] = Field(description="A list of source titles that were used to answer the question")

prompt_find_sources = """
You will be given a question and an answer that was generated from a set of documents.
Your task is to identify which of the original documents were used to create the answer.

<question>
{question}
</question>

<answer>
{answer}
</answer>

<provided_content>
{combined_content}
</provided_content>
""".strip()

def find_sources(question: str, answer: str, content: str) -> list[str]:
    """
    Identify which sources were used to generate an answer.

    Args:
        question: The original question
        answer: The generated answer
        content: The combined content from all sources

    Returns:
        list: A list of source titles that were used
    """
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=SourceList
    )
    sources_response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt_find_sources.format(question=question, answer=answer, combined_content=content),
        config=config
    )
    return sources_response.parsed.sources

# Test the source finding function
test_sources = find_sources(test_question, test_answer, combined_content)
pretty_print.wrapped(test_question, title="Question", header_color=pretty_print.Color.YELLOW)
pretty_print.wrapped(test_answer, title="Answer", header_color=pretty_print.Color.GREEN)
pretty_print.wrapped(test_sources, title="Sources", header_color=pretty_print.Color.CYAN)
# Output:
#   [93m--------------------------------------------- Question ---------------------------------------------[0m

#     What are the primary environmental and economic benefits of solar energy?

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [92m---------------------------------------------- Answer ----------------------------------------------[0m

#     The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels. Economically, it allows homeowners to significantly lower their monthly electricity bills and potentially sell excess power back to the grid.

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [96m--------------------------------------------- Sources ---------------------------------------------[0m

#     The Benefits of Solar Energy

#   [96m----------------------------------------------------------------------------------------------------[0m


"""
### Executing the Sequential Workflow

Now we combine all three functions into a sequential workflow: Generate Questions → Answer Questions → Find Sources. Each step is executed one after another for each question. Notice how much time it takes to run the full workflow.

"""

def sequential_workflow(content, n_questions=10) -> list[FAQ]:
    """
    Execute the complete sequential workflow for FAQ generation.

    Args:
        content: The combined content from all sources

    Returns:
        list: A list of FAQs with questions, answers, and sources
    """
    # Generate questions
    questions = generate_questions(content, n_questions)

    # Answer and find sources for each question sequentially
    final_faqs = []
    for question in questions:
        # Generate an answer for the current question
        answer = answer_question(question, content)

        # Identify the sources for the generated answer
        sources = find_sources(question, answer, content)

        faq = FAQ(
            question=question,
            answer=answer,
            sources=sources
        )
        final_faqs.append(faq)

    return final_faqs

# Execute the sequential workflow (measure time for comparison)
start_time = time.monotonic()
sequential_faqs = sequential_workflow(combined_content, n_questions=4)
end_time = time.monotonic()
print(f"Sequential processing completed in {end_time - start_time:.2f} seconds")

# Display the final result
pretty_print.wrapped(
    [faq.model_dump_json(indent=2) for faq in sequential_faqs],
    title="Sequential FAQ List"
)
# Output:
#   Sequential processing completed in 22.20 seconds

#   [93m--------------------------------------- Sequential FAQ List ---------------------------------------[0m

#     {

#     "question": "What are the primary financial benefits of installing solar panels for homeowners, and are there any initial costs to consider?",

#     "answer": "The primary financial benefits of installing solar panels for homeowners are significantly lowered monthly electricity bills and, in some cases, the ability to sell excess power back to the grid. The initial installation cost can be high.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "What are the main differences between onshore and offshore wind farms, and what is the biggest challenge associated with wind energy generation?",

#     "answer": "Offshore wind farms generally produce more consistent power than onshore wind farms due to stronger, more reliable winds. The biggest challenge associated with wind energy generation is its intermittency, as it only generates power when the wind blows.",

#     "sources": [

#       "Understanding Wind Turbines"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "Why is energy storage essential for renewable energy sources like solar and wind, and what are the common types of large-scale storage solutions?",

#     "answer": "Energy storage is essential for renewable sources like solar and wind because these sources are intermittent, meaning they only generate power when conditions are favorable (e.g., when the sun shines or the wind blows). Storing excess energy when it's plentiful and releasing it when needed is crucial for ensuring a stable and steady supply of electricity and unlocking their full potential for a stable power grid.\n\nCommon types of large-scale storage solutions include pumped-hydro storage and battery technologies, particularly lithium-ion.",

#     "sources": [

#       "Understanding Wind Turbines",

#       "Energy Storage Solutions"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "How do energy storage solutions address the intermittency challenges of renewable energy sources such as solar and wind?",

#     "answer": "Energy storage solutions address the intermittency challenges of renewable energy sources like solar and wind by storing excess energy when these sources are plentiful and releasing it when it's needed, thus ensuring a steady supply of electricity and balancing energy supply and demand.",

#     "sources": [

#       "Understanding Wind Turbines",

#       "Energy Storage Solutions"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 4. Optimizing Sequential Workflows With Parallel Processing

While the sequential workflow works well, we can optimize it by running some steps in parallel. We can generate the answer and find sources simultaneously for all the questions. This can significantly reduce the overall processing time.

**Important**: you may meet the rate limits of your account if you do this for a lot of questions. If you go over your rate limits, the API calls will return errors and retry after a timeout. Make sure to take this into account when building real-world products!
"""

"""
### Implementing Parallel Processing

Let's implement a parallel version of our workflow using Python's `asyncio` library.

"""

async def answer_question_async(question: str, content: str) -> str:
    """
    Async version of answer_question function.
    """
    prompt = prompt_answer_question.format(question=question, combined_content=content)
    response = await client.aio.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text

async def find_sources_async(question: str, answer: str, content: str) -> list[str]:
    """
    Async version of find_sources function.
    """
    prompt = prompt_find_sources.format(question=question, answer=answer, combined_content=content)
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=SourceList
    )
    response = await client.aio.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config
    )
    return response.parsed.sources

async def process_question_parallel(question: str, content: str) -> FAQ:
    """
    Process a single question by generating answer and finding sources in parallel.
    """
    answer = await answer_question_async(question, content)
    sources = await find_sources_async(question, answer, content)
    return FAQ(
        question=question,
        answer=answer,
        sources=sources
    )

"""
### Executing the Parallel Workflow

Now let's process all questions using parallel execution. We'll process multiple questions concurrently, which can significantly reduce the total processing time. Notice how much time it takes to run the full workflow and compare it with the execution time of the sequential workflow.

"""

async def parallel_workflow(content: str, n_questions: int = 10) -> list[FAQ]:
    """
    Execute the complete parallel workflow for FAQ generation.

    Args:
        content: The combined content from all sources

    Returns:
        list: A list of FAQs with questions, answers, and sources
    """
    # Generate questions (this step remains synchronous)
    questions = generate_questions(content, n_questions)

    # Process all questions in parallel
    tasks = [process_question_parallel(question, content) for question in questions]
    parallel_faqs = await asyncio.gather(*tasks)

    return parallel_faqs

# Execute the parallel workflow (measure time for comparison)
start_time = time.monotonic()
parallel_faqs = await parallel_workflow(combined_content, n_questions=4)
end_time = time.monotonic()
print(f"Parallel processing completed in {end_time - start_time:.2f} seconds")

# Display the final result
pretty_print.wrapped(
    text=[faq.model_dump_json(indent=2) for faq in parallel_faqs],
    title="Generated FAQ List (Parallel)"
)
# Output:
#   Parallel processing completed in 8.98 seconds

#   [93m---------------------------------- Generated FAQ List (Parallel) ----------------------------------[0m

#     {

#     "question": "What are the primary environmental and economic benefits of using solar energy?",

#     "answer": "The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels.\n\nThe primary economic benefits include significantly lower monthly electricity bills, the ability to sell excess power back to the grid, long-term savings, and contributing to energy independence for nations.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "How do wind turbines generate electricity, and what are the main challenges associated with wind power?",

#     "answer": "Wind turbines generate electricity by capturing kinetic energy from the wind and converting it into electrical power. The main challenge associated with wind power is its intermittency, as it only generates power when the wind blows.",

#     "sources": [

#       "Understanding Wind Turbines"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "Why is energy storage crucial for renewable sources like solar and wind, and what are the common large-scale storage technologies?",

#     "answer": "Energy storage is crucial for renewable sources like solar and wind because these sources are intermittent, meaning they only generate power when conditions are right (e.g., when the sun shines or the wind blows). Storing excess energy when it's plentiful and releasing it when needed ensures a steady supply of electricity and a stable power grid.\n\nThe common large-scale storage technologies mentioned are pumped-hydro storage and battery technologies, particularly lithium-ion.",

#     "sources": [

#       "Understanding Wind Turbines",

#       "Energy Storage Solutions"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "question": "How do government incentives impact the financial viability of installing solar panels, given the initial high costs?",

#     "answer": "Government incentives make installing solar panels a financially viable option, despite the initial high costs.",

#     "sources": [

#       "The Benefits of Solar Energy"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
### Sequential vs Parallel: Key Differences

The main differences between sequential and parallel approaches:

**Sequential Processing:**
- Questions are processed one at a time
- Predictable execution order
- Easier to debug and understand
- Higher total processing time

**Parallel Processing:**
- Multiple questions can be processed simultaneously
- Significant reduction in total processing time
- More complex error handling
- Better resource utilization

Both approaches produce the same results, but parallel processing can be significantly faster for larger datasets.

"""

"""
## 5. Building a Basic Routing Workflow

Routing is a method that categorizes an input and then sends it to a specific task designed to handle that type of input. This approach helps keep different functions separate and lets you create more specialized prompts. If you don't use routing, trying to optimize for one kind of input might negatively affect how well the system performs with other kinds of inputs.
"""

"""
### Intent Classification

First, we create a classification prompt and function to determine the user's intent. This will help us route the query to the appropriate handler:
"""

class IntentEnum(str, Enum):
    """
    Defines the allowed values for the 'intent' field.
    Inheriting from 'str' ensures that the values are treated as strings.
    """
    TECHNICAL_SUPPORT = "Technical Support"
    BILLING_INQUIRY = "Billing Inquiry"
    GENERAL_QUESTION = "General Question"

class UserIntent(BaseModel):
    """
    Defines the expected response schema for the intent classification.
    """
    intent: IntentEnum = Field(description="The intent of the user's query")

prompt_classification = """
Classify the user's query into one of the following categories.

<categories>
{categories}
</categories>

<user_query>
{user_query}
</user_query>
""".strip()


def classify_intent(user_query: str) -> IntentEnum:
    """Uses an LLM to classify a user query."""
    prompt = prompt_classification.format(
        user_query=user_query,
        categories=[intent.value for intent in IntentEnum]
    )
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=UserIntent
    )
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config
    )
    return response.parsed.intent


query_1 = "My internet connection is not working."
query_2 = "I think there is a mistake on my last invoice."
query_3 = "What are your opening hours?"

intent_1 = classify_intent(query_1)
intent_2 = classify_intent(query_2)
intent_3 = classify_intent(query_3)

# Print the results
queries = [query_1, query_2, query_3]
intents = [intent_1, intent_2, intent_3]
for i, (query, intent) in enumerate(zip(queries, intents), start=1):
    pretty_print.wrapped(
        text=query,
        title=f"Question {i}"
    )
    pretty_print.wrapped(
        text=intent,
        title=f"Intent {i}",
        header_color=pretty_print.Color.MAGENTA
    )
    print()
# Output:
#   [93m-------------------------------------------- Question 1 --------------------------------------------[0m

#     My internet connection is not working.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------------- Intent 1 ---------------------------------------------[0m

#     IntentEnum.TECHNICAL_SUPPORT

#   [95m----------------------------------------------------------------------------------------------------[0m

#   

#   [93m-------------------------------------------- Question 2 --------------------------------------------[0m

#     I think there is a mistake on my last invoice.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------------- Intent 2 ---------------------------------------------[0m

#     IntentEnum.BILLING_INQUIRY

#   [95m----------------------------------------------------------------------------------------------------[0m

#   

#   [93m-------------------------------------------- Question 3 --------------------------------------------[0m

#     What are your opening hours?

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------------- Intent 3 ---------------------------------------------[0m

#     IntentEnum.GENERAL_QUESTION

#   [95m----------------------------------------------------------------------------------------------------[0m

#   


"""
### Defining Specialized Handlers

Next, we create specialized prompts for each type of query and a routing function that directs queries to the appropriate handler based on the classified intent:
"""

prompt_technical_support = """
You are a helpful technical support agent.

Here's the user's query:
<user_query>
{user_query}
</user_query>

Provide a helpful first response, asking for more details like what troubleshooting steps they have already tried.
""".strip()

prompt_billing_inquiry = """
You are a helpful billing support agent.

Here's the user's query:
<user_query>
{user_query}
</user_query>

Acknowledge their concern and inform them that you will need to look up their account, asking for their account number.
""".strip()

prompt_general_question = """
You are a general assistant.

Here's the user's query:
<user_query>
{user_query}
</user_query>

Apologize that you are not sure how to help.
""".strip()


def handle_query(user_query: str, intent: str) -> str:
    """Routes a query to the correct handler based on its classified intent."""
    if intent == IntentEnum.TECHNICAL_SUPPORT:
        prompt = prompt_technical_support.format(user_query=user_query)
    elif intent == IntentEnum.BILLING_INQUIRY:
        prompt = prompt_billing_inquiry.format(user_query=user_query)
    elif intent == IntentEnum.GENERAL_QUESTION:
        prompt = prompt_general_question.format(user_query=user_query)
    else:
        prompt = prompt_general_question.format(user_query=user_query)
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text


response_1 = handle_query(query_1, intent_1)
response_2 = handle_query(query_2, intent_2)
response_3 = handle_query(query_3, intent_3)

# Print the results
queries = [query_1, query_2, query_3]
intents = [intent_1, intent_2, intent_3]
responses = [response_1, response_2, response_3]
for i, (query, intent, response) in enumerate(zip(queries, intents, responses), start=1):
    pretty_print.wrapped(
        text=query,
        title=f"Question {i}"
    )
    pretty_print.wrapped(
        text=intent,
        title=f"Intent {i}",
        header_color=pretty_print.Color.MAGENTA
    )
    pretty_print.wrapped(
        text=response,
        title=f"Response {i}",
        header_color=pretty_print.Color.GREEN
    )
    print()
# Output:
#   [93m-------------------------------------------- Question 1 --------------------------------------------[0m

#     My internet connection is not working.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------------- Intent 1 ---------------------------------------------[0m

#     IntentEnum.TECHNICAL_SUPPORT

#   [95m----------------------------------------------------------------------------------------------------[0m

#   [92m-------------------------------------------- Response 1 --------------------------------------------[0m

#     Hello there! I'm sorry to hear you're having trouble with your internet connection. That can definitely be frustrating.

#   

#   To help me understand what's going on and assist you best, could you please provide a few more details?

#   

#   1.  **What exactly are you experiencing?** For example, are you not seeing your Wi-Fi network, is your Wi-Fi connected but no websites are loading, or are there any specific error messages?

#   2.  **What device are you trying to connect with?** (e.g., a laptop, phone, desktop PC)

#   3.  **Have you already tried any troubleshooting steps yourself?** For instance, have you tried:

#       *   Restarting your computer or device?

#       *   Restarting your Wi-Fi router and modem (unplugging them for 30 seconds and plugging them back in)?

#       *   Checking if other devices can connect to the internet?

#   

#   Once I have a bit more information, I'll be happy to guide you through some potential solutions.

#   [92m----------------------------------------------------------------------------------------------------[0m

#   

#   [93m-------------------------------------------- Question 2 --------------------------------------------[0m

#     I think there is a mistake on my last invoice.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------------- Intent 2 ---------------------------------------------[0m

#     IntentEnum.BILLING_INQUIRY

#   [95m----------------------------------------------------------------------------------------------------[0m

#   [92m-------------------------------------------- Response 2 --------------------------------------------[0m

#     I'm sorry to hear you think there might be a mistake on your last invoice. I can definitely help you look into that!

#   

#   To access your account and investigate the charges, could you please provide your account number?

#   [92m----------------------------------------------------------------------------------------------------[0m

#   

#   [93m-------------------------------------------- Question 3 --------------------------------------------[0m

#     What are your opening hours?

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------------- Intent 3 ---------------------------------------------[0m

#     IntentEnum.GENERAL_QUESTION

#   [95m----------------------------------------------------------------------------------------------------[0m

#   [92m-------------------------------------------- Response 3 --------------------------------------------[0m

#     I apologize, but I'm not sure how to help with that. As an AI, I don't have a physical location or opening hours.

#   [92m----------------------------------------------------------------------------------------------------[0m

#   


"""
## 6. Orchestrator-Worker Pattern: Dynamic Task Decomposition

The orchestrator-workers workflow uses a main LLM to dynamically break down complex tasks into smaller subtasks, which are then assigned to other "worker" LLMs. The orchestrator LLM also combines the results from these workers.

This approach is ideal for complex problems where the specific steps or subtasks can't be known in advance. For instance, in a coding project, the orchestrator can decide which files need modifying and how, based on the initial request. While it might look similar to parallel processing, its key advantage is flexibility: instead of pre-defined subtasks, the orchestrator LLM determines them on the fly according to the given input.
"""

"""
### Defining the Orchestrator

The orchestrator is the central coordinator that breaks down complex user queries into structured JSON tasks. It analyzes the input and identifies what types of actions need to be taken, such as billing inquiries, product returns, or status updates:

"""

class QueryTypeEnum(str, Enum):
    """The type of query to be handled."""
    BILLING_INQUIRY = "BillingInquiry"
    PRODUCT_RETURN = "ProductReturn"
    STATUS_UPDATE = "StatusUpdate"

class Task(BaseModel):
    """A task to be performed."""
    query_type: QueryTypeEnum = Field(description="The type of query to be handled.")
    invoice_number: str | None = Field(description="The invoice number to be used for the billing inquiry.", default=None)
    product_name: str | None = Field(description="The name of the product to be returned.", default=None)
    reason_for_return: str | None = Field(description="The reason for returning the product.", default=None)
    order_id: str | None = Field(description="The order ID to be used for the status update.", default=None)

class TaskList(BaseModel):
    """A list of tasks to be performed."""
    tasks: list[Task] = Field(description="A list of tasks to be performed.")

prompt_orchestrator = f"""
You are a master orchestrator. Your job is to break down a complex user query into a list of sub-tasks.
Each sub-task must have a "query_type" and its necessary parameters.

The possible "query_type" values and their required parameters are:
1. "{QueryTypeEnum.BILLING_INQUIRY.value}": Requires "invoice_number".
2. "{QueryTypeEnum.PRODUCT_RETURN.value}": Requires "product_name" and "reason_for_return".
3. "{QueryTypeEnum.STATUS_UPDATE.value}": Requires "order_id".

Here's the user's query.

<user_query>
{{query}}
</user_query>
""".strip()


def orchestrator(query: str) -> list[Task]:
    """Breaks down a complex query into a list of tasks."""
    prompt = prompt_orchestrator.format(query=query)
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=TaskList
    )
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config
    )
    return response.parsed.tasks

"""
### Billing Worker Implementation

The billing worker specializes in handling invoice-related inquiries. It extracts the specific concern from the user's query, simulates opening an investigation, and returns structured information about the action taken:
"""

class BillingTask(BaseModel):
    """A billing inquiry task to be performed."""
    query_type: QueryTypeEnum = Field(description="The type of task to be performed.", default=QueryTypeEnum.BILLING_INQUIRY)
    invoice_number: str = Field(description="The invoice number to be used for the billing inquiry.")
    user_concern: str = Field(description="The concern or question the user has voiced about the invoice.")
    action_taken: str = Field(description="The action taken to address the user's concern.")
    resolution_eta: str = Field(description="The estimated time to resolve the concern.")

prompt_billing_worker_extractor = """
You are a specialized assistant. A user has a query regarding invoice '{invoice_number}'.
From the full user query provided below, extract the specific concern or question the user has voiced about this particular invoice.
Respond with ONLY the extracted concern/question. If no specific concern is mentioned beyond a general inquiry about the invoice, state 'General inquiry regarding the invoice'.

Here's the user's query:
<user_query>
{original_user_query}
</user_query>

Extracted concern about invoice {invoice_number}:
""".strip()


def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
    """
    Handles a billing inquiry.
    1. Uses an LLM to extract the specific concern about the invoice from the original query.
    2. Simulates opening an investigation.
    3. Returns structured data about the action taken.
    """
    extraction_prompt = prompt_billing_worker_extractor.format(
        invoice_number=invoice_number, original_user_query=original_user_query
    )
    response = client.models.generate_content(model=MODEL_ID, contents=extraction_prompt)
    extracted_concern = response.text

    # Simulate backend action: opening an investigation
    investigation_id = f"INV_CASE_{random.randint(1000, 9999)}"
    eta_days = 2

    task = BillingTask(
        invoice_number=invoice_number,
        user_concern=extracted_concern,
        action_taken=f"An investigation (Case ID: {investigation_id}) has been opened regarding your concern.",
        resolution_eta=f"{eta_days} business days",
    )

    return task

"""
### Product Return Worker

The return worker handles product return requests by generating RMA (Return Merchandise Authorization) numbers and providing detailed shipping instructions for customers:
"""

class ReturnTask(BaseModel):
    """A task to handle a product return request."""
    query_type: QueryTypeEnum = Field(description="The type of task to be performed.", default=QueryTypeEnum.PRODUCT_RETURN)
    product_name: str = Field(description="The name of the product to be returned.")
    reason_for_return: str = Field(description="The reason for returning the product.")
    rma_number: str = Field(description="The RMA number for the return.")
    shipping_instructions: str = Field(description="The shipping instructions for the return.")


def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
    """
    Handles a product return request.
    1. Simulates generating an RMA number and providing return instructions.
    2. Returns structured data.
    """
    # Simulate backend action: generating RMA and getting instructions
    rma_number = f"RMA-{random.randint(10000, 99999)}"
    shipping_instructions = (
        "Please pack the '{product_name}' securely in its original packaging if possible. "
        "Include all accessories and manuals. Write the RMA number ({rma_number}) clearly on the outside of the package. "
        "Ship to: Returns Department, 123 Automation Lane, Tech City, TC 98765."
    ).format(product_name=product_name, rma_number=rma_number)

    task = ReturnTask(
        product_name=product_name,
        reason_for_return=reason_for_return,
        rma_number=rma_number,
        shipping_instructions=shipping_instructions,
    )

    return task

"""
### Order Status Worker

The status worker retrieves and formats order status information, including shipping details, tracking numbers, and delivery estimates:
"""

class StatusTask(BaseModel):
    """A task to handle an order status update request."""
    query_type: QueryTypeEnum = Field(description="The type of task to be performed.", default=QueryTypeEnum.STATUS_UPDATE)
    order_id: str = Field(description="The order ID to be used for the status update.")
    current_status: str = Field(description="The current status of the order.")
    carrier: str = Field(description="The carrier of the order.")
    tracking_number: str = Field(description="The tracking number of the order.")
    expected_delivery: str = Field(description="The expected delivery date of the order.")

def handle_status_worker(order_id: str) -> StatusTask:
    """
    Handles an order status update request.
    1. Simulates fetching order status from a backend system.
    2. Returns structured data.
    """
    # Simulate backend action: fetching order status
    # Possible statuses and details to make it more dynamic
    possible_statuses = [
        {"status": "Processing", "carrier": "N/A", "tracking": "N/A", "delivery_estimate": "3-5 business days"},
        {
            "status": "Shipped",
            "carrier": "SuperFast Shipping",
            "tracking": f"SF{random.randint(100000, 999999)}",
            "delivery_estimate": "Tomorrow",
        },
        {
            "status": "Delivered",
            "carrier": "Local Courier",
            "tracking": f"LC{random.randint(10000, 99999)}",
            "delivery_estimate": "Delivered yesterday",
        },
        {
            "status": "Delayed",
            "carrier": "Standard Post",
            "tracking": f"SP{random.randint(10000, 99999)}",
            "delivery_estimate": "Expected in 2-3 additional days",
        },
    ]
    # For a given order_id, we could hash it to pick a status or just pick one randomly for this example
    # This ensures that for the same order_id in a single run, we'd get the same fake status if we implement a simple hash.
    # For now, let's pick randomly for demonstration.
    status_details = random.choice(possible_statuses)

    task = StatusTask(
        order_id=order_id,
        current_status=status_details["status"],
        carrier=status_details["carrier"],
        tracking_number=status_details["tracking"],
        expected_delivery=status_details["delivery_estimate"],
    )

    return task

"""
### Response Synthesizer

The synthesizer takes the structured results from all workers and combines them into a single, coherent, and customer-friendly response message:
"""

prompt_synthesizer = """
You are a master communicator. Combine several distinct pieces of information from our support team into a single, well-formatted, and friendly email to a customer.

Here are the points to include, based on the actions taken for their query:
<points>
{formatted_results}
</points>

Combine these points into one cohesive response.
Start with a friendly greeting (e.g., "Dear Customer," or "Hi there,") and end with a polite closing (e.g., "Sincerely," or "Best regards,").
Ensure the tone is helpful and professional.
""".strip()


def synthesizer(results: list[Task]) -> str:
    """Combines structured results from workers into a single user-facing message."""
    bullet_points = []
    for res in results:
        point = f"Regarding your {res.query_type}:\n"
        if res.query_type == QueryTypeEnum.BILLING_INQUIRY:
            res: BillingTask = res
            point += f"  - Invoice Number: {res.invoice_number}\n"
            point += f'  - Your Stated Concern: "{res.user_concern}"\n'
            point += f"  - Our Action: {res.action_taken}\n"
            point += f"  - Expected Resolution: We will get back to you within {res.resolution_eta}."
        elif res.query_type == QueryTypeEnum.PRODUCT_RETURN:
            res: ReturnTask = res
            point += f"  - Product: {res.product_name}\n"
            point += f'  - Reason for Return: "{res.reason_for_return}"\n'
            point += f"  - Return Authorization (RMA): {res.rma_number}\n"
            point += f"  - Instructions: {res.shipping_instructions}"
        elif res.query_type == QueryTypeEnum.STATUS_UPDATE:
            res: StatusTask = res
            point += f"  - Order ID: {res.order_id}\n"
            point += f"  - Current Status: {res.current_status}\n"
            if res.carrier != "N/A":
                point += f"  - Carrier: {res.carrier}\n"
            if res.tracking_number != "N/A":
                point += f"  - Tracking Number: {res.tracking_number}\n"
            point += f"  - Delivery Estimate: {res.expected_delivery}"
        bullet_points.append(point)

    formatted_results = "\n\n".join(bullet_points)
    prompt = prompt_synthesizer.format(formatted_results=formatted_results)
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    return response.text

"""
### Main Orchestrator-Worker Pipeline

This function coordinates the entire orchestrator-worker workflow: it runs the orchestrator to break down the query, dispatches the appropriate workers, and synthesizes the final response:
"""

def process_user_query(user_query):
    """Processes a query using the Orchestrator-Worker-Synthesizer pattern."""

    pretty_print.wrapped(
        text=user_query,
        title="User query"
    )

    # 1. Run orchestrator
    tasks_list = orchestrator(user_query)
    if not tasks_list:
        print("Orchestrator did not return any tasks. Exiting.")
        return

    for i, task in enumerate(tasks_list, start=1):
        pretty_print.wrapped(
            text=task.model_dump_json(indent=2),
            title=f"Deconstructed task {i}",
            header_color=pretty_print.Color.MAGENTA
        )

    # 2. Run workers
    worker_results = []
    if tasks_list:
        for task in tasks_list:
            if task.query_type == QueryTypeEnum.BILLING_INQUIRY:
                worker_results.append(handle_billing_worker(task.invoice_number, user_query))
            elif task.query_type == QueryTypeEnum.PRODUCT_RETURN:
                worker_results.append(handle_return_worker(task.product_name, task.reason_for_return))
            elif task.query_type == QueryTypeEnum.STATUS_UPDATE:
                worker_results.append(handle_status_worker(task.order_id))
            else:
                print(f"Warning: Unknown query_type '{task.query_type}' found in orchestrator tasks.")

        if worker_results:
            for i, res in enumerate(worker_results, start=1):
                pretty_print.wrapped(
                    text=res.model_dump_json(indent=2),
                    title=f"Worker result {i}",
                    header_color=pretty_print.Color.CYAN
                )
        else:
            print("No valid worker tasks to run.")
    else:
        print("No tasks to run for workers.")

    # 3. Run synthesizer
    if worker_results:
        final_user_message = synthesizer(worker_results)
        pretty_print.wrapped(
            text=final_user_message,
            title="Final synthesized response",
            header_color=pretty_print.Color.GREEN
        )
    else:
        print("Skipping synthesis because there were no worker results.")

"""
### Testing the Complete Workflow

Let's test our orchestrator-worker pattern with a complex customer query that involves multiple tasks: a billing inquiry, a product return, and an order status update:
"""

# Test with customer query
complex_customer_query = """
Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.
Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.
Finally, can you give me an update on my order #A-12345?
""".strip()

process_user_query(complex_customer_query)
# Output:
#   [93m-------------------------------------------- User query --------------------------------------------[0m

#     Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.

#   Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.

#   Finally, can you give me an update on my order #A-12345?

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------- Deconstructed task 1 ---------------------------------------[0m

#     {

#     "query_type": "BillingInquiry",

#     "invoice_number": "INV-7890",

#     "product_name": null,

#     "reason_for_return": null,

#     "order_id": null

#   }

#   [95m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------- Deconstructed task 2 ---------------------------------------[0m

#     {

#     "query_type": "ProductReturn",

#     "invoice_number": null,

#     "product_name": "SuperWidget 5000",

#     "reason_for_return": "not compatible with my system",

#     "order_id": null

#   }

#   [95m----------------------------------------------------------------------------------------------------[0m

#   [95m--------------------------------------- Deconstructed task 3 ---------------------------------------[0m

#     {

#     "query_type": "StatusUpdate",

#     "invoice_number": null,

#     "product_name": null,

#     "reason_for_return": null,

#     "order_id": "A-12345"

#   }

#   [95m----------------------------------------------------------------------------------------------------[0m

#   [96m----------------------------------------- Worker result 1 -----------------------------------------[0m

#     {

#     "query_type": "BillingInquiry",

#     "invoice_number": "INV-7890",

#     "user_concern": "It seems higher than I expected.",

#     "action_taken": "An investigation (Case ID: INV_CASE_1020) has been opened regarding your concern.",

#     "resolution_eta": "2 business days"

#   }

#   [96m----------------------------------------------------------------------------------------------------[0m

#   [96m----------------------------------------- Worker result 2 -----------------------------------------[0m

#     {

#     "query_type": "ProductReturn",

#     "product_name": "SuperWidget 5000",

#     "reason_for_return": "not compatible with my system",

#     "rma_number": "RMA-21819",

#     "shipping_instructions": "Please pack the 'SuperWidget 5000' securely in its original packaging if possible. Include all accessories and manuals. Write the RMA number (RMA-21819) clearly on the outside of the package. Ship to: Returns Department, 123 Automation Lane, Tech City, TC 98765."

#   }

#   [96m----------------------------------------------------------------------------------------------------[0m

#   [96m----------------------------------------- Worker result 3 -----------------------------------------[0m

#     {

#     "query_type": "StatusUpdate",

#     "order_id": "A-12345",

#     "current_status": "Processing",

#     "carrier": "N/A",

#     "tracking_number": "N/A",

#     "expected_delivery": "3-5 business days"

#   }

#   [96m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------ Final synthesized response ------------------------------------[0m

#     Hi there,

#   

#   Thank you for reaching out to us! We've received your recent inquiries and are happy to provide updates on each of them.

#   

#   Here's a summary of the actions we've taken and the information you requested:

#   

#   ---

#   

#   **Regarding Your Billing Inquiry (Invoice Number: INV-7890)**

#   We understand your concern that the amount "seems higher than expected." Please be assured that we're taking this seriously.

#   *   An investigation has been opened under **Case ID: INV_CASE_1020** to thoroughly review your invoice details.

#   *   We expect to get back to you with a resolution or a comprehensive update within **2 business days**.

#   

#   ---

#   

#   **Regarding Your Product Return (SuperWidget 5000)**

#   We've processed your return authorization for the **SuperWidget 5000** you mentioned was "not compatible with your system."

#   *   Your Return Merchandise Authorization (RMA) number is: **RMA-21819**.

#   *   To ensure a smooth return process, please follow these instructions:

#       *   Securely pack the **SuperWidget 5000** (along with all accessories and manuals), ideally in its original packaging.

#       *   Clearly write your RMA number (**RMA-21819**) on the outside of the package.

#       *   Ship the package to:

#           Returns Department

#           123 Automation Lane

#           Tech City, TC 98765

#   

#   ---

#   

#   **Regarding Your Order Status Update (Order ID: A-12345)**

#   We're happy to provide an update on your recent order.

#   *   Your order (**A-12345**) is currently **Processing**.

#   *   You can expect delivery within **3-5 business days**.

#   

#   ---

#   

#   We hope this clarifies all your current inquiries. If you have any further questions or require additional assistance, please don't hesitate to reply to this email.

#   

#   Best regards,

#   

#   The Support Team

#   [92m----------------------------------------------------------------------------------------------------[0m

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Building Effective Agents - Anthropic</summary>

# Building Effective Agents - Anthropic

**Source URL:** <https://www.anthropic.com/engineering/building-effective-agents>

Published Dec 19, 2024

We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks.

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents.

## What are agents?

"Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems.

## When (and when not) to use agents

When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

## When and how to use frameworks

There are many frameworks that make agentic systems easier to implement, including:

- The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview);
- [Strands Agents SDK by AWS](https://strandsagents.com/latest/);
- [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and
- [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our [cookbook](https://platform.claude.com/cookbook/patterns-agents-basic-workflows) for some sample implementations.

## Building blocks, workflows, and agents

In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png&w=3840&q=75The augmented LLM

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75The prompt chaining workflow

**When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Examples where prompt chaining is useful:**

- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75The routing workflow

**When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Examples where routing is useful:**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75The parallelization workflow

**When to use this workflow:** Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

**Examples where parallelization is useful:**

- **Sectioning**:
  - Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response.
  - Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model’s performance on a given prompt.
- **Voting**:
  - Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
  - Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.

### Workflow: Orchestrator-workers

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75The orchestrator-workers workflow

**When to use this workflow:** This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Example where orchestrator-workers is useful:**

- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75The evaluator-optimizer workflow

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Examples where evaluator-optimizer is useful:**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png&w=3840&q=75Autonomous agent

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Examples where agents are useful:**

The following examples are from our own implementations:

- A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
- Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png&w=3840&q=75High-level flow of a coding agent

## Combining and customizing these patterns

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent’s planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

### Acknowledgements

Written by Erik S. and Barry Zhang. This work draws upon our experiences building agents at Anthropic and the valuable insights shared by our customers, for which we're deeply grateful.

## Appendix 1: Agents in practice

Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight.

### A. Customer support

Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because:

- Support interactions naturally follow a conversation flow while requiring access to external information and actions;
- Tools can be integrated to pull customer data, order history, and knowledge base articles;
- Actions such as issuing refunds or updating tickets can be handled programmatically; and
- Success can be clearly measured through user-defined resolutions.

Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness.

### B. Coding agents

The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because:

- Code solutions are verifiable through automated tests;
- Agents can iterate on solutions using test results as feedback;
- The problem space is well-defined and structured; and
- Output quality can be measured objectively.

In our own implementation, agents can now solve real GitHub issues in the [SWE-bench Verified](https://www.anthropic.com/research/swe-bench-sonnet) benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

## Appendix 2: Prompt engineering your tools

No matter which agentic system you're building, tools will likely be an important part of your agent. [Tools](https://www.anthropic.com/news/tool-use-ga) enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a [tool use block](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block) in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

Our suggestions for deciding on tool formats are the following:

- Give the model enough tokens to "think" before it writes itself into a corner.
- Keep the format close to what the model has seen naturally occurring in text on the internet.
- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- Test how the model uses your tools: Run many example inputs in our [workbench](https://console.anthropic.com/workbench) to see what mistakes the model makes, and iterate.
- [Poka-yoke](https://en.wikipedia.org/wiki/Poka-yoke) your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for [SWE-bench](https://www.anthropic.com/research/swe-bench-sonnet), we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

</details>

<details>
<summary>Claude 4 Best Practices</summary>

# Claude 4 Best Practices

**Source URL:** <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices>

This is the single reference for prompt engineering with Claude's latest models, including Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Haiku 4.5. It covers foundational techniques, output control, tool use, thinking, and agentic systems. Jump to the section that matches your situation.

For an overview of model capabilities, see the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview). For details on what's new in Claude Opus 4.7, see [What's new in Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7). For migration guidance, see the [Migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide).

## Prompting Claude Opus 4.7

Claude Opus 4.7 is our most capable generally available model, with particular strengths in long-horizon agentic work, knowledge work, vision, and memory tasks. It performs well out of the box on existing Claude Opus 4.6 prompts. The patterns below cover the behaviors that most often require tuning.

For API parameter changes when migrating from Claude Opus 4.6 (effort levels, task budgets, thinking configuration, sampling-parameter removal, and tokenization), see the [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7).

### Response length and verbosity

Claude Opus 4.7 calibrates response length to how complex it judges the task to be, rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and much longer ones on open-ended analysis.

If your product depends on a certain style or verbosity of output, you may need to tune your prompts. As an example, to decrease verbosity, you might add:

```
Provide concise, focused responses. Skip non-essential context, and keep examples minimal.
```

If you see specific examples of kinds of verbosity (i.e. over-explaining), you can add additional instructions in your prompt to prevent them. Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do.

### Calibrating effort and thinking depth

The [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) allows you to tune Claude's intelligence vs. token spend, trading off capability for faster speed and lower costs. Start with the new `xhigh` effort level for coding and agentic use cases, and use a minimum of `high` effort for most intelligence-sensitive use cases. Experiment with other effort levels to further tune token usage and intelligence:

- **`max`:** Max effort can deliver performance gains in some use cases, but may show diminishing returns from increased token usage. This setting can also sometimes be prone to overthinking. We recommend testing max effort for intelligence-demanding tasks.
- **`xhigh` (new):** Extra high effort is the best setting for most coding and agentic use cases.
- **`high`:** This setting balances token usage and intelligence. For most intelligence-sensitive use cases, we recommend a minimum of `high` effort.
- **`medium`:** Good for cost-sensitive use cases that need to reduce token usage while trading off intelligence.
- **`low`:** Reserve for short, scoped tasks and latency-sensitive workloads that are not intelligence-sensitive.

Meaningfully changing from Claude Opus 4.6, Claude Opus 4.7 respects effort levels strictly, especially at the low end. At `low` and `medium`, the model scopes its work to what was asked rather than going above and beyond. This is good for latency and cost, but on moderately complex tasks running at `low` effort there is some risk of under-thinking.

If you observe shallow reasoning on complex problems, raise effort to `high` or `xhigh` rather than prompting around it. If you need to keep effort at `low` for latency, add targeted guidance:

```
This task involves multi-step reasoning. Think carefully through the problem before responding.
```

We expect effort to be more important for this model than for any prior Opus, and recommend experimenting with it actively when you upgrade.

The triggering behavior for adaptive thinking is steerable. If you find the model thinking more often than you'd like — which can happen with large or complex system prompts — add guidance to steer it. As always, measure the effect of any prompting changes on performance. Example:

```
Thinking adds latency and should only be used when it will meaningfully improve answer quality — typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

Conversely, if you're running hard workloads at `medium` and seeing under-thinking, the first lever is to raise effort. If you need finer control, prompt for it directly.

If you are running Claude Opus 4.7 at `max` or `xhigh` effort, set a large max output token budget so the model has room to think and act across its subagents and tool calls. We recommend starting at 64k tokens and tuning from there.

### Tool use triggering

Claude Opus 4.7 has a tendency to use tools less often than Claude Opus 4.6 and to use reasoning more. This produces better results in most cases. However, increasing the effort setting is a useful lever to increase the level of tool usage, especially in knowledge work. `high` or `xhigh` effort settings show substantially more tool usage in agentic search and coding. For scenarios where you want more tool use, you can also adjust your prompt to explicitly instruct the model about when and how to properly use its tools. For instance, if you find that the model is not using your web search tools, clearly describe why and how it should.

### User-facing progress updates

Claude Opus 4.7 provides more regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages ("After every 3 tool calls, summarize progress"), try removing it. If you find that the length or contents of Claude Opus 4.7's user-facing updates are not well-calibrated to your use case, explicitly describe what these updates should look like in the prompt and provide examples.

### More literal instruction following

Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make. The upside of this literalism is precision and less thrash, and it generally performs better for API use cases with carefully tuned prompts, structured extraction, and pipelines where you want predictable behavior. If you need Claude to apply an instruction broadly, state the scope explicitly (for example, "Apply this formatting to every section, not just the first one").

### Tone and writing style

As with any new model, prose style on long-form writing may shift. Claude Opus 4.7 is more direct and opinionated, with less validation-forward phrasing and fewer emoji than Claude Opus 4.6's warmer style. If your product relies on a specific voice, re-evaluate style prompts against the new baseline.

For instance, if your product voice is warmer or more conversational, add:

```
Use a warm, collaborative tone. Acknowledge the user's framing before answering.
```

### Controlling subagent spawning

Claude Opus 4.7 tends to spawn fewer subagents by default. However, this behavior is steerable through prompting; give Claude Opus 4.7 explicit guidance around when subagents are desirable. A toy example for a coding use case:

```
Do not spawn a subagent for work you can complete directly in a single response (e.g. refactoring a function you can already see).

Spawn multiple subagents in the same turn when fanning out across items or reading multiple files.
```

### Design and frontend defaults

Claude Opus 4.7 has stronger design instincts than Claude Opus 4.6, with a consistent default house style: warm cream/off-white backgrounds (~`#F4F1EA`), serif display type (Georgia, Fraunces, Playfair), italic word-accents, and a terracotta/amber accent. This reads well for editorial, hospitality, and portfolio briefs, but will feel off for dashboards, dev tools, fintech, healthcare, or enterprise apps — and it appears in slide decks as well as web UIs.

This default is persistent. Generic instructions ("don't use cream," "make it clean and minimal") tend to shift the model to a different fixed palette rather than producing variety. Two approaches work reliably:

**1\. Specify a concrete alternative.** The model follows explicit specs precisely:

```
Design a desktop landing page for a supplement brand called AEFRM.

The visual direction should come from a cold monochrome atmosphere using pale silver-gray tones that gradually deepen into blue-gray and near-black, similar to a misted metallic surface.

The page should feel sharp and controlled, with a strong sense of structure and restraint.

Use this tonal system across the full page instead of introducing bright accent colors.

Use the uploaded image on the hero design in black and white.

The layout should be built with clear horizontal sections and a centered max-width container. Use 4px corner radius consistently across cards, buttons, inputs, and media frames. Margins should feel generous, with enough empty space around each section so the page breathes.

Typography should use a square, angular sans-serif with wider letter spacing than usual, especially in headings and navigation, so the text feels more engineered and less compressed. Headline text can be large and uppercase, while supporting copy remains short and sparse. The sub texts should be written with Alumni Sans SC in 4-6px like tiny little texts on corners bottom centre like that.

For the structure, start with a hero section containing a strong product statement, one short supporting paragraph, and a clean product placeholder or packshot frame. Below that, add a benefit grid with three or four blocks, then a formulation or ingredients section, and finally a cta.

Buttons should be flat and precise, with subtle hover changes using transition: all 160ms ease out where brightness and border contrast shift slightly rather than using dramatic motion.

Color palette should stay within this range:
#E9ECEC, #C9D2D4, #8C9A9E, #44545B, #11171B.
```

**2\. Have the model propose options before building.** This breaks the default and gives users control. If you previously relied on `temperature` for design variety, use this approach — it produces meaningfully different directions across runs. Example prompt:

```
Before building, propose 4 distinct visual directions tailored to this brief (each as: bg hex / accent hex / typeface — one-line rationale). Ask the user to pick one, then implement only that direction.
```

Additionally, Claude Opus 4.7 requires less frontend design prompting than previous models to avoid generic patterns that users call the "AI slop" aesthetic. With earlier models, we recommended a lengthier prompt snippet in our [frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md). However, Claude Opus 4.7 generates distinctive, creative frontends with more minimal prompting guidance. This prompt snippet works well with the above prompting advice for variety:

```
<frontend_aesthetics>
NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white or dark backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. Use unique fonts, cohesive colors and themes, and animations for effects and micro-interactions.
</frontend_aesthetics>
```

### Interactive coding products

Claude Opus 4.7's token usage and behavior can differ between autonomous, asynchronous coding agents with a single user turn and interactive, synchronous coding agents with multiple user turns. Specifically, it tends to use more tokens in interactive settings, primarily because it reasons more after user turns. This can improve long-horizon coherence, instruction following, and coding capabilities in long, interactive coding sessions, but also comes with more token usage. To maximize both performance and token efficiency in coding products, we recommend using `xhigh` or `high` effort, adding autonomous features like an auto mode, and reducing the number of human interactions required from your users.

Of course, when limiting the number of required user interactions, it's important to specify the task, intent, and relevant constraints upfront in the first human turn. Providing well-specified, clear, and accurate task descriptions upfront can help maximize autonomy and intelligence while minimizing extra token usage after user turns. We find that because Claude Opus 4.7 is more autonomous than prior models, this usage pattern helps to maximize performance. In contrast, ambiguous or underspecified prompts conveyed progressively over multiple user turns tend to relatively reduce token efficiency and sometimes performance.

### Code review harnesses

Claude Opus 4.7 is meaningfully better at finding bugs than prior models, and has both higher recall and precision in our evals — 11pp better recall in one of our hardest bug-finding evals based on real Anthropic PRs. However, if your code-review harness was tuned for an earlier model, you may initially see lower recall. This is likely a harness effect, not a capability regression. When a review prompt says things like "only report high-severity issues," "be conservative," or "don't nitpick," Claude Opus 4.7 may follow that instruction more faithfully than earlier models did — it may investigate the code just as thoroughly, identify the bugs, and then not report findings it judges to be below your stated bar. This can show up as the model doing the same depth of investigation but converting fewer investigations into reported findings, especially on lower-severity bugs. Precision typically rises, but measured recall can fall even though the model's underlying bug-finding ability has improved.

Some recommended prompt language:

```
Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage - a separate verification step will do that. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them.
```

This prompt can be used without having an actual second step, but moving confidence filtering out of the finding step often helps. If your harness has a separate verification, deduplication, or ranking stage, tell the model explicitly that its job at the finding stage is coverage rather than filtering.

If you do want the model to self-filter in a single pass, be concrete about where the bar is rather than using qualitative terms like "important" — for example, "report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit nits like pure style or naming preferences."

We recommend iterating on prompts against a subset of your evals or test cases to validate recall or F1 score gains.

### Computer use

[Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) capability works across resolutions, up to a new maximum resolution of 2576px / 3.75MP. In our computer use testing, we find that sending images at 1080p provides a good balance of performance and cost.

For particularly cost-sensitive workloads, we recommend 720p or 1366×768 as lower-cost options with strong performance. We recommend that you conduct your own testing to find the ideal settings for your use case; experimenting with effort settings can also help tune the model's behavior.

## General principles

### Be clear and direct

Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want "above and beyond" behavior, explicitly request it rather than relying on the model to infer this from vague prompts.

Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. The more precisely you explain what you want, the better the result.

**Golden rule:** Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too.

- Be specific about the desired output format and constraints.
- Provide instructions as sequential steps using numbered lists or bullet points when the order or completeness of steps matters.

### Example: Creating an analytics dashboard

### Add context to improve performance

Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude better understand your goals and deliver more targeted responses.

### Example: Formatting preferences

Claude is smart enough to generalize from the explanation.

### Use examples effectively

Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) can dramatically improve accuracy and consistency.

When adding examples, make them:

- **Relevant:** Mirror your actual use case closely.
- **Diverse:** Cover edge cases and vary enough that Claude doesn't pick up unintended patterns.
- **Structured:** Wrap examples in `<example>` tags (multiple examples in `<examples>` tags) so Claude can distinguish them from instructions.

Include 3–5 examples for best results. You can also ask Claude to evaluate your examples for relevance and diversity, or to generate additional ones based on your initial set.

### Structure prompts with XML tags

XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (e.g. `<instructions>`, `<context>`, `<input>`) reduces misinterpretation.

Best practices:

- Use consistent, descriptive tag names across your prompts.
- Nest tags when content has a natural hierarchy (documents inside `<documents>`, each inside `<document index="n">`).

### Give Claude a role

Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference:

Python

```
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system="You are a helpful coding assistant specializing in Python.",
    messages=[\
        {"role": "user", "content": "How do I sort a list of dictionaries by key?"}\
    ],
)
print(message.content)
```

### Long context prompting

When working with large documents or data-rich inputs (20k+ tokens), structure your prompt carefully to get the best results:

- **Put longform data at the top**: Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples. This can significantly improve performance across all models.

Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs.

- **Structure document content and metadata with XML tags**: When using multiple documents, wrap each document in `<document>` tags with `<document_content>` and `<source>` (and other metadata) subtags for clarity.

### Example multi-document structure

- **Ground responses in quotes**: For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the noise of the rest of the document's contents.

### Example quote extraction

### Model self-knowledge

If you would like Claude to identify itself correctly in your application or use specific API strings:

Sample prompt for model identity

```
The assistant is Claude, created by Anthropic. The current model is Claude Opus 4.7.
```

For LLM-powered apps that need to specify model strings:

Sample prompt for model string

```
When an LLM is needed, please default to Claude Opus 4.7 unless the user requests otherwise. The exact model string for Claude Opus 4.7 is claude-opus-4-7.
```

## Output and formatting

### Communication style and verbosity

Claude's latest models have a more concise and natural communication style compared to previous models:

- **More direct and grounded:** Provides fact-based progress reports rather than self-celebratory updates
- **More conversational:** Slightly more fluent and colloquial, less machine-like
- **Less verbose:** May skip detailed summaries for efficiency unless prompted otherwise

This means Claude may skip verbal summaries after tool calls, jumping directly to the next action. If you prefer more visibility into its reasoning:

Sample prompt

```
After completing a task that involves tool use, provide a quick summary of the work you've done.
```

### Control the format of responses

There are a few particularly effective ways to steer output formatting:

1. **Tell Claude what to do instead of what not to do**
   - Instead of: "Do not use markdown in your response"
   - Try: "Your response should be composed of smoothly flowing prose paragraphs."
2. **Use XML format indicators**
   - Try: "Write the prose sections of your response in <smoothly\_flowing\_prose\_paragraphs> tags."
3. **Match your prompt style to the desired output**

The formatting style used in your prompt may influence Claude's response style. If you are still experiencing steerability issues with output formatting, try matching your prompt style to your desired output style as closely as possible. For example, removing markdown from your prompt can reduce the volume of markdown in the output.

4. **Use detailed prompts for specific formatting preferences**

For more control over markdown and formatting usage, provide explicit guidance:

Sample prompt to minimize markdown

````
<avoid_excessive_markdown_and_bullet_points>
When writing reports, documents, technical explanations, analyses, or any long-form content, write in clear, flowing prose using complete paragraphs and sentences. Use standard paragraph breaks for organization and reserve markdown primarily for `inline code`, code blocks (```...```), and simple headings (###, and ###). Avoid using **bold** and *italics*.

DO NOT use ordered lists (1. ...) or unordered lists (*) unless : a) you're presenting truly discrete items where a list format is the best option, or b) the user explicitly requests a list or ranking

Instead of listing items with bullets or numbers, incorporate them naturally into sentences. This guidance applies especially to technical writing. Using prose instead of excessive formatting will improve user satisfaction. NEVER output a series of overly short bullet points.

Your goal is readable, flowing text that guides the reader naturally through ideas rather than fragmenting information into isolated points.
</avoid_excessive_markdown_and_bullet_points>
````

### LaTeX output

Claude Opus 4.6 defaults to LaTeX for mathematical expressions, equations, and technical explanations. If you prefer plain text, add the following instructions to your prompt:

Sample prompt

```
Format your response in plain text only. Do not use LaTeX, MathJax, or any markup notation such as \( \), $, or \frac{}{}. Write all math expressions using standard text characters (e.g., "/" for division, "*" for multiplication, and "^" for exponents).
```

### Document creation

Claude's latest models excel at creating presentations, animations, and visual documents with impressive creative flair and strong instruction following. The models produce polished, usable output on the first try in most cases.

For best results with document creation:

Sample prompt

```
Create a professional presentation on [topic]. Include thoughtful design elements, visual hierarchy, and engaging animations where appropriate.
```

### Migrating away from prefilled responses

Starting with Claude 4.6 models and [Claude Mythos Preview](https://anthropic.com/glasswing), prefilled responses on the last assistant turn are no longer supported. On Mythos Preview, requests with prefilled assistant messages return a 400 error. Model intelligence and instruction following has advanced such that most use cases of prefill no longer require it. Existing models will continue to support prefills, and adding assistant messages elsewhere in the conversation is not affected.

Here are common prefill scenarios and how to migrate away from them:

### Controlling output formatting

### Eliminating preambles

### Avoiding bad refusals

### Continuations

### Context hydration and role consistency

## Tool use

### Tool usage

Claude's latest models are trained for precise instruction following and benefit from explicit direction to use specific tools. If you say "can you suggest some changes," Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended.

For Claude to take action, be more explicit:

### Example: Explicit instructions

To make Claude more proactive about taking action by default, you can add this to your system prompt:

Sample prompt for proactive action

```
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is unclear, infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing. Try to infer the user's intent about whether a tool call (e.g., file edit or read) is intended or not, and act accordingly.
</default_to_action>
```

On the other hand, if you want the model to be more hesitant by default, less prone to jumping straight into implementations, and only take action if requested, you can steer this behavior with a prompt like the below:

Sample prompt for conservative action

```
<do_not_act_before_instructions>
Do not jump into implementatation or changes files unless clearly instructed to make changes. When the user's intent is ambiguous, default to providing information, doing research, and providing recommendations rather than taking action. Only proceed with edits, modifications, or implementations when the user explicitly requests them.
</do_not_act_before_instructions>
```

Claude Opus 4.5 and Claude Opus 4.6 are also more responsive to the system prompt than previous models. If your prompts were designed to reduce undertriggering on tools or skills, these models may now overtrigger. The fix is to dial back any aggressive language. Where you might have said "CRITICAL: You MUST use this tool when...", you can use more normal prompting like "Use this tool when...".

### Optimize parallel tool calling

Claude's latest models excel at parallel tool execution. These models will:

- Run multiple speculative searches during research
- Read several files at once to build context faster
- Execute bash commands in parallel (which can even bottleneck system performance)

This behavior is easily steerable. While the model has a high success rate in parallel tool calling without prompting, you can boost this to ~100% or adjust the aggression level:

Sample prompt for maximum parallel efficiency

```
<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between the tool calls, make all of the independent tool calls in parallel. Prioritize calling tools simultaneously whenever the actions can be done in parallel rather than sequentially. For example, when reading 3 files, run 3 tool calls in parallel to read all 3 files into context at the same time. Maximize use of parallel tool calls where possible to increase speed and efficiency. However, if some tool calls depend on previous calls to inform dependent values like the parameters, do NOT call these tools in parallel and instead call them sequentially. Never use placeholders or guess missing parameters in tool calls.
</use_parallel_tool_calls>
```

Sample prompt to reduce parallel execution

```
Execute operations sequentially with brief pauses between each step to ensure stability.
```

## Thinking and reasoning

### Overthinking and excessive thoroughness

Claude Opus 4.6 does significantly more upfront exploration than previous models, especially at higher `effort` settings. This initial work often helps to optimize the final results, but the model may gather extensive context or pursue multiple threads of research without being prompted. If your prompts previously encouraged the model to be more thorough, you should tune that guidance for Claude Opus 4.6:

- **Replace blanket defaults with more targeted instructions.** Instead of "Default to using \[tool\]," add guidance like "Use \[tool\] when it would enhance your understanding of the problem."
- **Remove over-prompting.** Tools that undertriggered in previous models are likely to trigger appropriately now. Instructions like "If in doubt, use \[tool\]" will cause overtriggering.
- **Use effort as a fallback.** If Claude continues to be overly aggressive, use a lower setting for `effort`.

In some cases, Claude Opus 4.6 may think extensively, which can inflate thinking tokens and slow down responses. If this behavior is undesirable, you can add explicit instructions to constrain its reasoning, or you can lower the `effort` setting to reduce overall thinking and token usage.

Sample prompt

```
When you're deciding how to approach a problem, choose an approach and commit to it. Avoid revisiting decisions unless you encounter new information that directly contradicts your reasoning. If you're weighing two approaches, pick one and see it through. You can always course-correct later if the chosen approach fails.
```

If you need a hard ceiling on thinking costs, extended thinking with a `budget_tokens` cap is still functional on Opus 4.6 and Sonnet 4.6 but is deprecated. Prefer lowering the [effort](https://platform.claude.com/docs/en/build-with-claude/effort) setting or using `max_tokens` as a hard limit with [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

### Leverage thinking & interleaved thinking capabilities

Claude's latest models offer thinking capabilities that can be especially helpful for tasks involving reflection after tool use or complex multi-step reasoning. You can guide its initial or interleaved thinking for better results.

Claude Opus 4.6 and Claude Sonnet 4.6 use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`), where Claude dynamically decides when and how much to think. Claude calibrates its thinking based on two factors: the `effort` parameter and query complexity. Higher effort elicits more thinking, and more complex queries do the same. On easier queries that don't require thinking, the model responds directly. In internal evaluations, adaptive thinking reliably drives better performance than extended thinking. Consider moving to adaptive thinking to get the most intelligent responses.

Use adaptive thinking for workloads that require agentic behavior such as multi-step tool use, complex coding tasks, and long-horizon agent loops. Older models use manual thinking mode with `budget_tokens`.

You can guide Claude's thinking behavior:

Example prompt

```
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
```

The triggering behavior for adaptive thinking is promptable. If you find the model thinking more often than you'd like, which can happen with large or complex system prompts, add guidance to steer it:

Sample prompt

```
Extended thinking adds latency and should only be used when it will meaningfully improve answer quality - typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

If you are migrating from [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) with `budget_tokens`, replace your thinking configuration and move budget control to `effort`:

**Before (extended thinking, older models):**

Python

```
client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=64000,
    thinking={"type": "enabled", "budget_tokens": 32000},
    messages=[{"role": "user", "content": "..."}],
)
```

**After (adaptive thinking):**

Python

```
client.messages.create(
    model="claude-opus-4-7",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # or "max", "xhigh", "medium", "low"
    messages=[{"role": "user", "content": "..."}],
)
```

If you are not using extended thinking, no changes are required. Thinking is off by default when you omit the `thinking` parameter.

- **Prefer general instructions over prescriptive steps.** A prompt like "think thoroughly" often produces better reasoning than a hand-written step-by-step plan. Claude's reasoning frequently exceeds what a human would prescribe.
- **Multishot examples work with thinking.** Use `<thinking>` tags inside your few-shot examples to show Claude the reasoning pattern. It will generalize that style to its own extended thinking blocks.
- **Manual CoT as a fallback.** When thinking is off, you can still encourage step-by-step reasoning by asking Claude to think through the problem. Use structured tags like `<thinking>` and `<answer>` to cleanly separate reasoning from the final output.
- **Ask Claude to self-check.** Append something like "Before you finish, verify your answer against \[test criteria\]." This catches errors reliably, especially for coding and math.

When extended thinking is disabled, Claude Opus 4.5 is particularly sensitive to the word "think" and its variants. Consider using alternatives like "consider," "evaluate," or "reason through" in those cases.

For more information on thinking capabilities, see [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) and [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

## Agentic systems

### Long-horizon reasoning and state tracking

Claude's latest models excel at long-horizon reasoning tasks with exceptional state tracking capabilities. Claude maintains orientation across extended sessions by focusing on incremental progress, making steady advances on a few things at a time rather than attempting everything at once. This capability especially emerges over multiple context windows or task iterations, where Claude can work on a complex task, save the state, and continue with a fresh context window.

#### Context awareness and multi-window workflows

Claude 4.6 and Claude 4.5 models feature [context awareness](https://platform.claude.com/docs/en/build-with-claude/context-windows#context-awareness-in-claude-sonnet-4-6-sonnet-4-5-and-haiku-4-5), enabling the model to track its remaining context window (i.e. "token budget") throughout a conversation. This enables Claude to execute tasks and manage context more effectively by understanding how much space it has to work.

**Managing context limits:**

If you are using Claude in an agent harness that compacts context or allows saving context to external files (like in Claude Code), consider adding this information to your prompt so Claude can behave accordingly. Otherwise, Claude may sometimes naturally try to wrap up work as it approaches the context limit. Below is an example prompt:

Sample prompt

```
Your context window will be automatically compacted as it approaches its limit, allowing you to continue working indefinitely from where you left off. Therefore, do not stop tasks early due to token budget concerns. As you approach your token budget limit, save your current progress and state to memory before the context window refreshes. Always be as persistent and autonomous as possible and complete tasks fully, even if the end of your budget is approaching. Never artificially stop any task early regardless of the context remaining.
```

The [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) pairs naturally with context awareness for seamless context transitions.

#### Multi-context window workflows

For tasks spanning multiple context windows:

1. **Use a different prompt for the very first context window**: Use the first context window to set up a framework (write tests, create setup scripts), then use future context windows to iterate on a todo-list.

2. **Have the model write tests in a structured format**: Ask Claude to create tests before starting work and keep track of them in a structured format (e.g., `tests.json`). This leads to better long-term ability to iterate. Remind Claude of the importance of tests: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."

3. **Set up quality of life tools**: Encourage Claude to create setup scripts (e.g., `init.sh`) to gracefully start servers, run test suites, and linters. This prevents repeated work when continuing from a fresh context window.

4. **Starting fresh vs compacting**: When a context window is cleared, consider starting with a brand new context window rather than using compaction. Claude's latest models are extremely effective at discovering state from the local filesystem. In some cases, you may want to take advantage of this over compaction. Be prescriptive about how it should start:
   - "Call pwd; you can only read and write files in this directory."
   - "Review progress.txt, tests.json, and the git logs."
   - "Manually run through a fundamental integration test before moving on to implementing new features."
5. **Provide verification tools**: As the length of autonomous tasks grows, Claude needs to verify correctness without continuous human feedback. Tools like Playwright MCP server or computer use capabilities for testing UIs are helpful.

6. **Encourage complete usage of context**: Prompt Claude to efficiently complete components before moving on:

Sample prompt

```
This is a very long task, so it may be beneficial to plan out your work clearly. It's encouraged to spend your entire output context working on the task - just make sure you don't run out of context with significant uncommitted work. Continue working systematically until you have completed this task.
```

#### State management best practices

- **Use structured formats for state data**: When tracking structured information (like test results or task status), use JSON or other structured formats to help Claude understand schema requirements
- **Use unstructured text for progress notes**: Freeform progress notes work well for tracking general progress and context
- **Use git for state tracking**: Git provides a log of what's been done and checkpoints that can be restored. Claude's latest models perform especially well in using git to track state across multiple sessions.
- **Emphasize incremental progress**: Explicitly ask Claude to keep track of its progress and focus on incremental work

### Example: State tracking

### Balancing autonomy and safety

Without guidance, Claude Opus 4.6 may take actions that are difficult to reverse or affect shared systems, such as deleting files, force-pushing, or posting to external services. If you want Claude Opus 4.6 to confirm before taking potentially risky actions, add guidance to your prompt:

Sample prompt

```
Consider the reversibility and potential impact of your actions. You are encouraged to take local, reversible actions like editing files or running tests, but for actions that are hard to reverse, affect shared systems, or could be destructive, ask the user before proceeding.

Examples of actions that warrant confirmation:
- Destructive operations: deleting files or branches, dropping database tables, rm -rf
- Hard to reverse operations: git push --force, git reset --hard, amending published commits
- Operations visible to others: pushing code, commenting on PRs/issues, sending messages, modifying shared infrastructure

When encountering obstacles, do not use destructive actions as a shortcut. For example, don't bypass safety checks (e.g. --no-verify) or discard unfamiliar files that may be in-progress work.
```

### Research and information gathering

Claude's latest models demonstrate exceptional agentic search capabilities and can find and synthesize information from multiple sources effectively. For optimal research results:

1. **Provide clear success criteria**: Define what constitutes a successful answer to your research question

2. **Encourage source verification**: Ask Claude to verify information across multiple sources

3. **For complex research tasks, use a structured approach**:

Sample prompt for complex research

```
Search for this information in a structured way. As you gather data, develop several competing hypotheses. Track your confidence levels in your progress notes to improve calibration. Regularly self-critique your approach and plan. Update a hypothesis tree or research notes file to persist information and provide transparency. Break down this complex research task systematically.
```

This structured approach allows Claude to find and synthesize virtually any piece of information and iteratively critique its findings, no matter the size of the corpus.

### Subagent orchestration

Claude's latest models demonstrate significantly improved native subagent orchestration capabilities. These models can recognize when tasks would benefit from delegating work to specialized subagents and do so proactively without requiring explicit instruction.

To take advantage of this behavior:

1. **Ensure well-defined subagent tools**: Have subagent tools available and described in tool definitions
2. **Let Claude orchestrate naturally**: Claude will delegate appropriately without explicit instruction
3. **Watch for overuse**: Claude Opus 4.6 has a strong predilection for subagents and may spawn them in situations where a simpler, direct approach would suffice. For example, the model may spawn subagents for code exploration when a direct grep call is faster and sufficient.

If you're seeing excessive subagent use, add explicit guidance about when subagents are and aren't warranted:

Sample prompt for subagent usage

```
Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state. For simple tasks, sequential operations, single-file edits, or tasks where you need to maintain context across steps, work directly rather than delegating.
```

### Chain complex prompts

With adaptive thinking and subagent orchestration, Claude handles most multi-step reasoning internally. Explicit prompt chaining (breaking a task into sequential API calls) is still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure.

The most common chaining pattern is **self-correction**: generate a draft → have Claude review it against criteria → have Claude refine based on the review. Each step is a separate API call so you can log, evaluate, or branch at any point.

### Reduce file creation in agentic coding

Claude's latest models may sometimes create new files for testing and iteration purposes, particularly when working with code. This approach allows Claude to use files, especially python scripts, as a 'temporary scratchpad' before saving its final output. Using temporary files can improve outcomes particularly for agentic coding use cases.

If you'd prefer to minimize net new file creation, you can instruct Claude to clean up after itself:

Sample prompt

```
If you create any temporary new files, scripts, or helper files for iteration, clean up these files by removing them at the end of the task.
```

### Overeagerness

Claude Opus 4.5 and Claude Opus 4.6 have a tendency to overengineer by creating extra files, adding unnecessary abstractions, or building in flexibility that wasn't requested. If you're seeing this undesired behavior, add specific guidance to keep solutions minimal.

For example:

Sample prompt to minimize overengineering

```
Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused:

- Scope: Don't add features, refactor code, or make "improvements" beyond what was asked. A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability.

- Documentation: Don't add docstrings, comments, or type annotations to code you didn't change. Only add comments where the logic isn't self-evident.

- Defensive coding: Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs).

- Abstractions: Don't create helpers, utilities, or abstractions for one-time operations. Don't design for hypothetical future requirements. The right amount of complexity is the minimum needed for the current task.
```

### Avoid focusing on passing tests and hard-coding

Claude can sometimes focus too heavily on making tests pass at the expense of more general solutions, or may use workarounds like helper scripts for complex refactoring instead of using standard tools directly. To prevent this behavior and ensure robust, generalizable solutions:

Sample prompt

```
Please write a high-quality, general-purpose solution using the standard tools available. Do not create helper scripts or workarounds to accomplish the task more efficiently. Implement a solution that works correctly for all valid inputs, not just the test cases. Do not hard-code values or create solutions that only work for specific test inputs. Instead, implement the actual logic that solves the problem generally.

Focus on understanding the problem requirements and implementing the correct algorithm. Tests are there to verify correctness, not to define the solution. Provide a principled implementation that follows best practices and software design principles.

If the task is unreasonable or infeasible, or if any of the tests are incorrect, please inform me rather than working around them. The solution should be robust, maintainable, and extendable.
```

### Minimizing hallucinations in agentic coding

Claude's latest models are less prone to hallucinations and give more accurate, grounded, intelligent answers based on the code. To encourage this behavior even more and minimize hallucinations:

Sample prompt

```
<investigate_before_answering>
Never speculate about code you have not opened. If the user references a specific file, you MUST read the file before answering. Make sure to investigate and read relevant files BEFORE answering questions about the codebase. Never make any claims about code before investigating unless you are certain of the correct answer - give grounded and hallucination-free answers.
</investigate_before_answering>
```

## Capability-specific tips

### Improved vision capabilities

Claude Opus 4.5 and Claude Opus 4.6 have improved vision capabilities compared to previous Claude models. They perform better on image processing and data extraction tasks, particularly when there are multiple images present in context. These improvements carry over to computer use, where the models can more reliably interpret screenshots and UI elements. You can also use these models to analyze videos by breaking them up into frames.

One technique that has proven effective to further boost performance is to give Claude a crop tool or [skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Testing has shown consistent uplift on image evaluations when Claude is able to "zoom" in on relevant regions of an image. Anthropic has created a [cookbook for the crop tool](https://platform.claude.com/cookbook/multimodal-crop-tool).

### Frontend design

Claude Opus 4.5 and Claude Opus 4.6 excel at building complex, real-world web applications with strong frontend design. However, without guidance, models can default to generic patterns that create what users call the "AI slop" aesthetic. To create distinctive, creative frontends that surprise and delight:

For a detailed guide on improving frontend design, see the blog post on [improving frontend design through skills](https://www.claude.com/blog/improving-frontend-design-through-skills).

Here's a system prompt snippet you can use to encourage better frontend design:

Sample prompt for frontend aesthetics

```
<frontend_aesthetics>
You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight.

Focus on:
- Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box!
</frontend_aesthetics>
```

You can also refer to the [full skill definition](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md).

## Migration considerations

When migrating to Claude 4.6 models from earlier generations:

1. **Be specific about desired behavior**: Consider describing exactly what you'd like to see in the output.

2. **Frame your instructions with modifiers**: Adding modifiers that encourage Claude to increase the quality and detail of its output can help better shape Claude's performance. For example, instead of "Create an analytics dashboard", use "Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation."

3. **Request specific features explicitly**: Animations and interactive elements should be requested explicitly when desired.

4. **Update thinking configuration**: Claude 4.6 models use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`) instead of manual thinking with `budget_tokens`. Use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth.

5. **Migrate away from prefilled responses**: Prefilled responses on the last assistant turn are deprecated starting with Claude 4.6 models. See [Migrating away from prefilled responses](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#migrating-away-from-prefilled-responses) for detailed guidance on alternatives.

6. **Tune anti-laziness prompting**: If your prompts previously encouraged the model to be more thorough or use tools more aggressively, dial back that guidance. Claude 4.6 models are significantly more proactive and may overtrigger on instructions that were needed for previous models.

For detailed migration steps, see the [Migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide).

### Migrating from Claude Sonnet 4.5 to Claude Sonnet 4.6

Claude Sonnet 4.6 defaults to an effort level of `high`, in contrast to Claude Sonnet 4.5 which had no effort parameter. Consider adjusting the effort parameter as you migrate from Claude Sonnet 4.5 to Claude Sonnet 4.6. If not explicitly set, you may experience higher latency with the default effort level.

**Recommended effort settings:**

- **Medium** for most applications
- **Low** for high-volume or latency-sensitive workloads
- Set a large max output token budget (64k tokens recommended) at medium or high effort to give the model room to think and act

**When to use Opus 4.7 instead:** For the hardest, longest-horizon problems (large-scale code migrations, deep research, extended autonomous work), Opus 4.7 remains the right choice. Sonnet 4.6 is optimized for workloads where fast turnaround and cost efficiency matter most.

#### If you're not using extended thinking

If you're not using extended thinking on Claude Sonnet 4.5, you can continue without it on Claude Sonnet 4.6. You should explicitly set effort to the level appropriate for your use case. At `low` effort with thinking disabled, you can expect similar or better performance relative to Claude Sonnet 4.5 with no extended thinking.

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=8192,
    thinking={"type": "disabled"},
    output_config={"effort": "low"},
    messages=[{"role": "user", "content": "..."}],
)
```

#### If you're using extended thinking

If you're using extended thinking with `budget_tokens` on Claude Sonnet 4.5, it is still functional on Claude Sonnet 4.6 but is deprecated. Migrate to [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort).

##### Migrating to adaptive thinking

Adaptive thinking is particularly well suited to the following workload patterns:

- **Autonomous multi-step agents:** coding agents that turn requirements into working software, data analysis pipelines, and bug finding where the model runs independently across many steps. Adaptive thinking lets the model calibrate its reasoning per step, staying on path over longer trajectories. For these workloads, start at `high` effort. If latency or token usage is a concern, scale down to `medium`.
- **Computer use agents:** Claude Sonnet 4.6 achieved best-in-class accuracy on computer use evaluations using adaptive mode.
- **Bimodal workloads:** a mix of easy and hard tasks where adaptive skips thinking on simple queries and reasons deeply on complex ones.

When using adaptive thinking, evaluate `medium` and `high` effort on your tasks. The right level depends on your workload's tradeoff between quality, latency, and token usage.

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{"role": "user", "content": "..."}],
)
```

##### Keeping budget\_tokens during migration

If you need to keep `budget_tokens` temporarily while migrating, a budget around 16k tokens provides headroom for harder problems without risk of runaway token usage. This configuration is deprecated and will be removed in a future model release.

**For coding use cases** (agentic coding, tool-heavy workflows, code generation), start with `medium` effort:

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16384,
    thinking={"type": "enabled", "budget_tokens": 16384},
    output_config={"effort": "medium"},
    messages=[{"role": "user", "content": "..."}],
)
```

**For chat and non-coding use cases** (chat, content generation, search, classification), start with `low` effort:

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=8192,
    thinking={"type": "enabled", "budget_tokens": 16384},
    output_config={"effort": "low"},
    messages=[{"role": "user", "content": "..."}],
)
```

</details>

<details>
<summary>LangGraph Workflows</summary>

# LangGraph Workflows

**Source URL:** <https://langchain-ai.github.io/langgraphjs/tutorials/workflows>

LangChain is the easy way to start building completely custom agents and applications powered by LLMs.
With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and [more](https://docs.langchain.com/oss/javascript/integrations/providers/overview).
LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications.

**LangChain vs. LangGraph vs. Deep Agents**If you are looking to build an agent, we recommend you start with [Deep Agents](https://docs.langchain.com/oss/javascript/deepagents/overview) which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context.Deep Agents are implementations of LangChain [agents](https://docs.langchain.com/oss/javascript/langchain/agents). If you don’t need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain.Use [LangGraph](https://docs.langchain.com/oss/javascript/langgraph/overview), our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization.

LangChain [agents](https://docs.langchain.com/oss/javascript/langchain/agents) are built on top of LangGraph in order to provide durable execution, streaming, human-in-the-loop, persistence, and more. You do not need to know LangGraph for basic LangChain agent usage.We recommend you use LangChain if you want to quickly build agents and autonomous applications.

## Create an agent

```
// First install: npm install langchain @langchain/anthropic
import { z } from "zod";
import { createAgent, tool } from "langchain";

const getWeather = tool(
  ({ city }) => `It's always sunny in ${city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string(),
    }),
  },
);

const agent = createAgent({
  model: "anthropic:claude-sonnet-4-6",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in Tokyo?" }],
  })
);
```

See the [Installation instructions](https://docs.langchain.com/oss/javascript/langchain/install) and [Quickstart guide](https://docs.langchain.com/oss/javascript/langchain/quickstart) to get started building your own agents and applications with LangChain.

Use [LangSmith](https://docs.langchain.com/langsmith/home) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.

## Core benefits

**Standard model interface** \
\
Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in.\
\
[Learn more](https://docs.langchain.com/oss/javascript/langchain/models)

**Easy to use, highly flexible agent** \
\
LangChain’s agent abstraction is designed to be easy to get started with, letting you build a simple agent in under 10 lines of code. But it also provides enough flexibility to allow you to do all the context engineering your heart desires.\
\
[Learn more](https://docs.langchain.com/oss/javascript/langchain/agents)

[https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81\
\
**Built on top of LangGraph** \
\
LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more.\
\
[Learn more](https://docs.langchain.com/oss/javascript/langgraph/overview)

[https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc\
\
**Debug with LangSmith** \
\
Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.\
\
[Learn more](https://docs.langchain.com/langsmith/observability)

</details>

<details>
<summary>Prompt Chaining Guide</summary>

# Prompt Chaining Guide

**Source URL:** <https://www.promptingguide.ai/techniques/prompt_chaining>

## Introduction to Prompt Chaining

Prompt Chaining with GPT-4o and Flowise AI (Tutorial) - YouTube
[Prompt Chaining with GPT-4o and Flowise AI (Tutorial)](https://www.youtube.com/watch?v=CKZC5RigYEc) [Elvis Saravia](https://www.youtube.com/channel/UCyna_OxOWL7IEuOwb7WhmxQ)

Elvis Saravia24.6K subscribers

To improve the reliability and performance of LLMs, one of the important prompt engineering techniques is to break tasks into its subtasks. Once those subtasks have been identified, the LLM is prompted with a subtask and then its response is used as input to another prompt. This is what's referred to as prompt chaining, where a task is split into subtasks with the idea to create a chain of prompt operations.

Prompt chaining is useful to accomplish complex tasks which an LLM might struggle to address if prompted with a very detailed prompt. In prompt chaining, chain prompts perform transformations or additional processes on the generated responses before reaching a final desired state.

Besides achieving better performance, prompt chaining helps to boost the transparency of your LLM application, increases controllability, and reliability. This means that you can debug problems with model responses much more easily and analyze and improve performance in the different stages that need improvement.

Prompt chaining is particularly useful when building LLM-powered conversational assistants and improving the personalization and user experience of your applications.

## Use Cases for Prompt Chaining

### Prompt Chaining for Document QA

Prompt chaining can be used in different scenarios that could involve several operations or transformations. For instance, one common use case of LLMs involves answering questions about a large text document. It helps if you design two different prompts where the first prompt is responsible for extracting relevant quotes to answer a question and a second prompt takes as input the quotes and original document to answer a given question. In other words, you will be creating two different prompts to perform the task of answering a question given in a document.

The first prompt below extracts the relevant quotes from the document given the question. Note that for simplicity, we have added a placeholder for the document `{{document}}`. To test the prompt you can copy and paste an article from Wikipedia such as this page for [prompt engineering (opens in a new tab)](https://en.wikipedia.org/wiki/Prompt_engineering). Due to larger context used for this task, we are using the `gpt-4-1106-preview` model from OpenAI. You can use the prompt with other long-context LLMs like Claude.

Prompt 1:

```
You are a helpful assistant. Your task is to help answer a question given in a document. The first step is to extract quotes relevant to the question from the document, delimited by ####. Please output the list of quotes using <quotes></quotes>. Respond with "No relevant quotes found!" if no relevant quotes were found.

####
{{document}}
####
```

Here is a screenshot of the entire prompt including the question which is passed using the `user` role.

https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fprompt-chaining-1.4bdd376c.png&w=1920&q=75

Output of Prompt 1:

```
<quotes>
- Chain-of-thought (CoT) prompting[27]
- Generated knowledge prompting[37]
- Least-to-most prompting[38]
- Self-consistency decoding[39]
- Complexity-based prompting[41]
- Self-refine[42]
- Tree-of-thought prompting[43]
- Maieutic prompting[45]
- Directional-stimulus prompting[46]
- Textual inversion and embeddings[59]
- Using gradient descent to search for prompts[61][62][63][64]
- Prompt injection[65][66][67]
</quotes>
```

The quotes that were returned in the first prompt can now be used as input to the second prompt below. Note that you can clean up the quotes a bit more, i.e., remove the citations. Those citations could be removed or utilized as part of another prompt in the chain but you can ignore this for now. The second prompt then takes the relevant quotes extracted by prompt 1 and prepares a helpful response to the question given in the document and those extracted quotes. The second prompt can be the following:

Prompt 2:

```
Given a set of relevant quotes (delimited by <quotes></quotes>) extracted from a document and the original document (delimited by ####), please compose an answer to the question. Ensure that the answer is accurate, has a friendly tone, and sounds helpful.

####
{{document}}
####

<quotes>
- Chain-of-thought (CoT) prompting[27]
- Generated knowledge prompting[37]
- Least-to-most prompting[38]
- Self-consistency decoding[39]
- Complexity-based prompting[41]
- Self-refine[42]
- Tree-of-thought prompting[43]
- Maieutic prompting[45]
- Directional-stimulus prompting[46]
- Textual inversion and embeddings[59]
- Using gradient descent to search for prompts[61][62][63][64]
- Prompt injection[65][66][67]
</quotes>
```

Output of Prompt 2:

```
The prompting techniques mentioned in the document include:

1. Chain-of-thought (CoT) prompting[27]
2. Generated knowledge prompting[37]
3. Least-to-most prompting[38]
4. Self-consistency decoding[39]
5. Complexity-based prompting[41]
6. Self-refine[42]
7. Tree-of-thought prompting[43]
8. Maieutic prompting[45]
9. Directional-stimulus prompting[46]
10. Textual inversion and embeddings[59]
11. Using gradient descent to search for prompts[61][62][63][64]
12. Prompt injection[65][66][67]

Each of these techniques employs unique strategies to enhance or specify the interactions with large language models to produce the desired outcomes.
```

As you can see, simplifying and creating prompt chains is a useful prompting approach where the responses need to undergo several operations or transformations. As an exercise, feel free to design a prompt that removes the citations (e.g., \[27\]) from the response before sending this as a final response to the user of your application.

You can also find more examples of prompt chaining in this [documentation (opens in a new tab)](https://docs.anthropic.com/claude/docs/prompt-chaining) that leverages the Claude LLM. Our example is inspired and adapted from their examples.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="chain-prompts-anthropic.md">
<details>
<summary>Chain Prompts - Anthropic</summary>

Phase: [EXPLOITATION]

# Chain Prompts - Anthropic

**Source URL:** <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts>

Prompt engineering
Prompting best practices

This is the single reference for prompt engineering with Claude's latest models, including Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Haiku 4.5. It covers foundational techniques, output control, tool use, thinking, and agentic systems. Jump to the section that matches your situation.

For an overview of model capabilities, see the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview). For details on what's new in Claude Opus 4.7, see [What's new in Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7). For migration guidance, see the [Migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide).

## Prompting Claude Opus 4.7

Claude Opus 4.7 is our most capable generally available model, with particular strengths in long-horizon agentic work, knowledge work, vision, and memory tasks. It performs well out of the box on existing Claude Opus 4.6 prompts. The patterns below cover the behaviors that most often require tuning.

For API parameter changes when migrating from Claude Opus 4.6 (effort levels, task budgets, thinking configuration, sampling-parameter removal, and tokenization), see the [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7).

### Response length and verbosity

Claude Opus 4.7 calibrates response length to how complex it judges the task to be, rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and much longer ones on open-ended analysis.

If your product depends on a certain style or verbosity of output, you may need to tune your prompts. As an example, to decrease verbosity, you might add:

```
Provide concise, focused responses. Skip non-essential context, and keep examples minimal.
```

If you see specific examples of kinds of verbosity (i.e. over-explaining), you can add additional instructions in your prompt to prevent them. Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do.

### Calibrating effort and thinking depth

The [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) allows you to tune Claude's intelligence vs. token spend, trading off capability for faster speed and lower costs. Start with the new `xhigh` effort level for coding and agentic use cases, and use a minimum of `high` effort for most intelligence-sensitive use cases. Experiment with other effort levels to further tune token usage and intelligence:

- **`max`:** Max effort can deliver performance gains in some use cases, but may show diminishing returns from increased token usage. This setting can also sometimes be prone to overthinking. We recommend testing max effort for intelligence-demanding tasks.
- **`xhigh` (new):** Extra high effort is the best setting for most coding and agentic use cases.
- **`high`:** This setting balances token usage and intelligence. For most intelligence-sensitive use cases, we recommend a minimum of `high` effort.
- **`medium`:** Good for cost-sensitive use cases that need to reduce token usage while trading off intelligence.
- **`low`:** Reserve for short, scoped tasks and latency-sensitive workloads that are not intelligence-sensitive.

Meaningfully changing from Claude Opus 4.6, Claude Opus 4.7 respects effort levels strictly, especially at the low end. At `low` and `medium`, the model scopes its work to what was asked rather than going above and beyond. This is good for latency and cost, but on moderately complex tasks running at `low` effort there is some risk of under-thinking.

If you observe shallow reasoning on complex problems, raise effort to `high` or `xhigh` rather than prompting around it. If you need to keep effort at `low` for latency, add targeted guidance:

```
This task involves multi-step reasoning. Think carefully through the problem before responding.
```

We expect effort to be more important for this model than for any prior Opus, and recommend experimenting with it actively when you upgrade.

The triggering behavior for adaptive thinking is steerable. If you find the model thinking more often than you'd like — which can happen with large or complex system prompts — add guidance to steer it. As always, measure the effect of any prompting changes on performance. Example:

```
Thinking adds latency and should only be used when it will meaningfully improve answer quality — typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

Conversely, if you're running hard workloads at `medium` and seeing under-thinking, the first lever is to raise effort. If you need finer control, prompt for it directly.

If you are running Claude Opus 4.7 at `max` or `xhigh` effort, set a large max output token budget so the model has room to think and act across its subagents and tool calls. We recommend starting at 64k tokens and tuning from there.

### Tool use triggering

Claude Opus 4.7 has a tendency to use tools less often than Claude Opus 4.6 and to use reasoning more. This produces better results in most cases. However, increasing the effort setting is a useful lever to increase the level of tool usage, especially in knowledge work. `high` or `xhigh` effort settings show substantially more tool usage in agentic search and coding. For scenarios where you want more tool use, you can also adjust your prompt to explicitly instruct the model about when and how to properly use its tools. For instance, if you find that the model is not using your web search tools, clearly describe why and how it should.

### User-facing progress updates

Claude Opus 4.7 provides more regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages ("After every 3 tool calls, summarize progress"), try removing it. If you find that the length or contents of Claude Opus 4.7's user-facing updates are not well-calibrated to your use case, explicitly describe what these updates should look like in the prompt and provide examples.

### More literal instruction following

Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make. The upside of this literalism is precision and less thrash, and it generally performs better for API use cases with carefully tuned prompts, structured extraction, and pipelines where you want predictable behavior. If you need Claude to apply an instruction broadly, state the scope explicitly (for example, "Apply this formatting to every section, not just the first one").

### Tone and writing style

As with any new model, prose style on long-form writing may shift. Claude Opus 4.7 is more direct and opinionated, with less validation-forward phrasing and fewer emoji than Claude Opus 4.6's warmer style. If your product relies on a specific voice, re-evaluate style prompts against the new baseline.

For instance, if your product voice is warmer or more conversational, add:

```
Use a warm, collaborative tone. Acknowledge the user's framing before answering.
```

### Controlling subagent spawning

Claude Opus 4.7 tends to spawn fewer subagents by default. However, this behavior is steerable through prompting; give Claude Opus 4.7 explicit guidance around when subagents are desirable. A toy example for a coding use case:

```
Do not spawn a subagent for work you can complete directly in a single response (e.g. refactoring a function you can already see).

Spawn multiple subagents in the same turn when fanning out across items or reading multiple files.
```

### Design and frontend defaults

Claude Opus 4.7 has stronger design instincts than Claude Opus 4.6, with a consistent default house style: warm cream/off-white backgrounds (~`#F4F1EA`), serif display type (Georgia, Fraunces, Playfair), italic word-accents, and a terracotta/amber accent. This reads well for editorial, hospitality, and portfolio briefs, but will feel off for dashboards, dev tools, fintech, healthcare, or enterprise apps — and it appears in slide decks as well as web UIs.

This default is persistent. Generic instructions ("don't use cream," "make it clean and minimal") tend to shift the model to a different fixed palette rather than producing variety. Two approaches work reliably:

**1\. Specify a concrete alternative.** The model follows explicit specs precisely:

```
Design a desktop landing page for a supplement brand called AEFRM.

The visual direction should come from a cold monochrome atmosphere using pale silver-gray tones that gradually deepen into blue-gray and near-black, similar to a misted metallic surface.

The page should feel sharp and controlled, with a strong sense of structure and restraint.

Use this tonal system across the full page instead of introducing bright accent colors.

Use the uploaded image on the hero design in black and white.

The layout should be built with clear horizontal sections and a centered max-width container. Use 4px corner radius consistently across cards, buttons, inputs, and media frames. Margins should feel generous, with enough empty space around each section so the page breathes.

Typography should use a square, angular sans-serif with wider letter spacing than usual, especially in headings and navigation, so the text feels more engineered and less compressed. Headline text can be large and uppercase, while supporting copy remains short and sparse. The sub texts should be written with Alumni Sans SC in 4-6px like tiny little texts on corners bottom centre like that.

For the structure, start with a hero section containing a strong product statement, one short supporting paragraph, and a clean product placeholder or packshot frame. Below that, add a benefit grid with three or four blocks, then a formulation or ingredients section, and finally a cta.

Buttons should be flat and precise, with subtle hover changes using transition: all 160ms ease out where brightness and border contrast shift slightly rather than using dramatic motion.

Color palette should stay within this range:
#E9ECEC, #C9D2D4, #8C9A9E, #44545B, #11171B.
```

**2\. Have the model propose options before building.** This breaks the default and gives users control. If you previously relied on `temperature` for design variety, use this approach — it produces meaningfully different directions across runs. Example prompt:

```
Before building, propose 4 distinct visual directions tailored to this brief (each as: bg hex / accent hex / typeface — one-line rationale). Ask the user to pick one, then implement only that direction.
```

Additionally, Claude Opus 4.7 requires less frontend design prompting than previous models to avoid generic patterns that users call the "AI slop" aesthetic. With earlier models, we recommended a lengthier prompt snippet in our [frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md). However, Claude Opus 4.7 generates distinctive, creative frontends with more minimal prompting guidance. This prompt snippet works well with the above prompting advice for variety:

```
<frontend_aesthetics>
NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white or dark backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. Use unique fonts, cohesive colors and themes, and animations for effects and micro-interactions.
</frontend_aesthetics>
```

### Interactive coding products

Claude Opus 4.7's token usage and behavior can differ between autonomous, asynchronous coding agents with a single user turn and interactive, synchronous coding agents with multiple user turns. Specifically, it tends to use more tokens in interactive settings, primarily because it reasons more after user turns. This can improve long-horizon coherence, instruction following, and coding capabilities in long, interactive coding sessions, but also comes with more token usage. To maximize both performance and token efficiency in coding products, we recommend using `xhigh` or `high` effort, adding autonomous features like an auto mode, and reducing the number of human interactions required from your users.

Of course, when limiting the number of required user interactions, it's important to specify the task, intent, and relevant constraints upfront in the first human turn. Providing well-specified, clear, and accurate task descriptions upfront can help maximize autonomy and intelligence while minimizing extra token usage after user turns. We find that because Claude Opus 4.7 is more autonomous than prior models, this usage pattern helps to maximize performance. In contrast, ambiguous or underspecified prompts conveyed progressively over multiple user turns tend to relatively reduce token efficiency and sometimes performance.

### Code review harnesses

Claude Opus 4.7 is meaningfully better at finding bugs than prior models, and has both higher recall and precision in our evals — 11pp better recall in one of our hardest bug-finding evals based on real Anthropic PRs. However, if your code-review harness was tuned for an earlier model, you may initially see lower recall. This is likely a harness effect, not a capability regression. When a review prompt says things like "only report high-severity issues," "be conservative," or "don't nitpick," Claude Opus 4.7 may follow that instruction more faithfully than earlier models did — it may investigate the code just as thoroughly, identify the bugs, and then not report findings it judges to be below your stated bar. This can show up as the model doing the same depth of investigation but converting fewer investigations into reported findings, especially on lower-severity bugs. Precision typically rises, but measured recall can fall even though the model's underlying bug-finding ability has improved.

Some recommended prompt language:

```
Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage - a separate verification step will do that. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them.
```

This prompt can be used without having an actual second step, but moving confidence filtering out of the finding step often helps. If your harness has a separate verification, deduplication, or ranking stage, tell the model explicitly that its job at the finding stage is coverage rather than filtering.

If you do want the model to self-filter in a single pass, be concrete about where the bar is rather than using qualitative terms like "important" — for example, "report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit nits like pure style or naming preferences."

We recommend iterating on prompts against a subset of your evals or test cases to validate recall or F1 score gains.

### Computer use

[Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) capability works across resolutions, up to a new maximum resolution of 2576px / 3.75MP. In our computer use testing, we find that sending images at 1080p provides a good balance of performance and cost.

For particularly cost-sensitive workloads, we recommend 720p or 1366×768 as lower-cost options with strong performance. We recommend that you conduct your own testing to find the ideal settings for your use case; experimenting with effort settings can also help tune the model's behavior.

## General principles

### Be clear and direct

Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want "above and beyond" behavior, explicitly request it rather than relying on the model to infer this from vague prompts.

Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. The more precisely you explain what you want, the better the result.

**Golden rule:** Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too.

- Be specific about the desired output format and constraints.
- Provide instructions as sequential steps using numbered lists or bullet points when the order or completeness of steps matters.

### Example: Creating an analytics dashboard

### Add context to improve performance

Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude better understand your goals and deliver more targeted responses.

### Example: Formatting preferences

Claude is smart enough to generalize from the explanation.

### Use examples effectively

Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples (known as few-shot or multishot prompting) can dramatically improve accuracy and consistency.

When adding examples, make them:

- **Relevant:** Mirror your actual use case closely.
- **Diverse:** Cover edge cases and vary enough that Claude doesn't pick up unintended patterns.
- **Structured:** Wrap examples in `<example>` tags (multiple examples in `<examples>` tags) so Claude can distinguish them from instructions.

Include 3–5 examples for best results. You can also ask Claude to evaluate your examples for relevance and diversity, or to generate additional ones based on your initial set.

### Structure prompts with XML tags

XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (e.g. `<instructions>`, `<context>`, `<input>`) reduces misinterpretation.

Best practices:

- Use consistent, descriptive tag names across your prompts.
- Nest tags when content has a natural hierarchy (documents inside `<documents>`, each inside `<document index="n">`).

### Give Claude a role

Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference:

Python

```
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system="You are a helpful coding assistant specializing in Python.",
    messages=[\
        {"role": "user", "content": "How do I sort a list of dictionaries by key?"}\
    ],
)
print(message.content)
```

### Long context prompting

When working with large documents or data-rich inputs (20k+ tokens), structure your prompt carefully to get the best results:

- **Put longform data at the top**: Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples. This can significantly improve performance across all models.

Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs.

- **Structure document content and metadata with XML tags**: When using multiple documents, wrap each document in `<document>` tags with `<document_content>` and `<source>` (and other metadata) subtags for clarity.

### Example multi-document structure

- **Ground responses in quotes**: For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the noise of the rest of the document's contents.

### Example quote extraction

### Model self-knowledge

If you would like Claude to identify itself correctly in your application or use specific API strings:

Sample prompt for model identity

```
The assistant is Claude, created by Anthropic. The current model is Claude Opus 4.7.
```

For LLM-powered apps that need to specify model strings:

Sample prompt for model string

```
When an LLM is needed, please default to Claude Opus 4.7 unless the user requests otherwise. The exact model string for Claude Opus 4.7 is claude-opus-4-7.
```

## Output and formatting

### Communication style and verbosity

Claude's latest models have a more concise and natural communication style compared to previous models:

- **More direct and grounded:** Provides fact-based progress reports rather than self-celebratory updates
- **More conversational:** Slightly more fluent and colloquial, less machine-like
- **Less verbose:** May skip detailed summaries for efficiency unless prompted otherwise

This means Claude may skip verbal summaries after tool calls, jumping directly to the next action. If you prefer more visibility into its reasoning:

Sample prompt

```
After completing a task that involves tool use, provide a quick summary of the work you've done.
```

### Control the format of responses

There are a few particularly effective ways to steer output formatting:

1.  **Tell Claude what to do instead of what not to do**
    -   Instead of: "Do not use markdown in your response"
    -   Try: "Your response should be composed of smoothly flowing prose paragraphs."
2.  **Use XML format indicators**
    -   Try: "Write the prose sections of your response in <smoothly\_flowing\_prose\_paragraphs> tags."
3.  **Match your prompt style to the desired output**

The formatting style used in your prompt may influence Claude's response style. If you are still experiencing steerability issues with output formatting, try matching your prompt style to your desired output style as closely as possible. For example, removing markdown from your prompt can reduce the volume of markdown in the output.

4.  **Use detailed prompts for specific formatting preferences**

For more control over markdown and formatting usage, provide explicit guidance:

Sample prompt to minimize markdown

````
<avoid_excessive_markdown_and_bullet_points>
When writing reports, documents, technical explanations, analyses, or any long-form content, write in clear, flowing prose using complete paragraphs and sentences. Use standard paragraph breaks for organization and reserve markdown primarily for `inline code`, code blocks (```...```), and simple headings (###, and ###). Avoid using **bold** and *italics*.

DO NOT use ordered lists (1. ...) or unordered lists (*) unless : a) you're presenting truly discrete items where a list format is the best option, or b) the user explicitly requests a list or ranking

Instead of listing items with bullets or numbers, incorporate them naturally into sentences. This guidance applies especially to technical writing. Using prose instead of excessive formatting will improve user satisfaction. NEVER output a series of overly short bullet points.

Your goal is readable, flowing text that guides the reader naturally through ideas rather than fragmenting information into isolated points.
</avoid_excessive_markdown_and_bullet_points>
````

### LaTeX output

Claude Opus 4.6 defaults to LaTeX for mathematical expressions, equations, and technical explanations. If you prefer plain text, add the following instructions to your prompt:

Sample prompt

```
Format your response in plain text only. Do not use LaTeX, MathJax, or any markup notation such as \( \), $, or \frac{}{}. Write all math expressions using standard text characters (e.g., "/" for division, "*" for multiplication, and "^" for exponents).
```

### Document creation

Claude's latest models excel at creating presentations, animations, and visual documents with impressive creative flair and strong instruction following. The models produce polished, usable output on the first try in most cases.

For best results with document creation:

Sample prompt

```
Create a professional presentation on [topic]. Include thoughtful design elements, visual hierarchy, and engaging animations where appropriate.
```

### Migrating away from prefilled responses

Starting with Claude 4.6 models and [Claude Mythos Preview](https://anthropic.com/glasswing), prefilled responses on the last assistant turn are no longer supported. On Mythos Preview, requests with prefilled assistant messages return a 400 error. Model intelligence and instruction following has advanced such that most use cases of prefill no longer require it. Existing models will continue to support prefills, and adding assistant messages elsewhere in the conversation is not affected.

Here are common prefill scenarios and how to migrate away from them:

### Controlling output formatting

### Eliminating preambles

### Avoiding bad refusals

### Continuations

### Context hydration and role consistency

## Tool use

### Tool usage

Claude's latest models are trained for precise instruction following and benefit from explicit direction to use specific tools. If you say "can you suggest some changes," Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended.

For Claude to take action, be more explicit:

### Example: Explicit instructions

To make Claude more proactive about taking action by default, you can add this to your system prompt:

Sample prompt for proactive action

```
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is unclear, infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing. Try to infer the user's intent about whether a tool call (e.g., file edit or read) is intended or not, and act accordingly.
</default_to_action>
```

On the other hand, if you want the model to be more hesitant by default, less prone to jumping straight into implementations, and only take action if requested, you can steer this behavior with a prompt like the below:

Sample prompt for conservative action

```
<do_not_act_before_instructions>
Do not jump into implementatation or changes files unless clearly instructed to make changes. When the user's intent is ambiguous, default to providing information, doing research, and providing recommendations rather than taking action. Only proceed with edits, modifications, or implementations when the user explicitly requests them.
</do_not_act_before_instructions>
```

Claude Opus 4.5 and Claude Opus 4.6 are also more responsive to the system prompt than previous models. If your prompts were designed to reduce undertriggering on tools or skills, these models may now overtrigger. The fix is to dial back any aggressive language. Where you might have said "CRITICAL: You MUST use this tool when...", you can use more normal prompting like "Use this tool when...".

### Optimize parallel tool calling

Claude's latest models excel at parallel tool execution. These models will:

- Run multiple speculative searches during research
- Read several files at once to build context faster
- Execute bash commands in parallel (which can even bottleneck system performance)

This behavior is easily steerable. While the model has a high success rate in parallel tool calling without prompting, you can boost this to ~100% or adjust the aggression level:

Sample prompt for maximum parallel efficiency

```
<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between the tool calls, make all of the independent tool calls in parallel. Prioritize calling tools simultaneously whenever the actions can be done in parallel rather than sequentially. For example, when reading 3 files, run 3 tool calls in parallel to read all 3 files into context at the same time. Maximize use of parallel tool calls where possible to increase speed and efficiency. However, if some tool calls depend on previous calls to inform dependent values like the parameters, do NOT call these tools in parallel and instead call them sequentially. Never use placeholders or guess missing parameters in tool calls.
</use_parallel_tool_calls>
```

Sample prompt to reduce parallel execution

```
Execute operations sequentially with brief pauses between each step to ensure stability.
```

## Thinking and reasoning

### Overthinking and excessive thoroughness

Claude Opus 4.6 does significantly more upfront exploration than previous models, especially at higher `effort` settings. This initial work often helps to optimize the final results, but the model may gather extensive context or pursue multiple threads of research without being prompted. If your prompts previously encouraged the model to be more thorough, you should tune that guidance for Claude Opus 4.6:

-   **Replace blanket defaults with more targeted instructions.** Instead of "Default to using \[tool\]," add guidance like "Use \[tool\] when it would enhance your understanding of the problem."
-   **Remove over-prompting.** Tools that undertriggered in previous models are likely to trigger appropriately now. Instructions like "If in doubt, use \[tool\]" will cause overtriggering.
-   **Use effort as a fallback.** If Claude continues to be overly aggressive, use a lower setting for `effort`.

In some cases, Claude Opus 4.6 may think extensively, which can inflate thinking tokens and slow down responses. If this behavior is undesirable, you can add explicit instructions to constrain its reasoning, or you can lower the `effort` setting to reduce overall thinking and token usage.

Sample prompt

```
When you're deciding how to approach a problem, choose an approach and commit to it. Avoid revisiting decisions unless you encounter new information that directly contradicts your reasoning. If you're weighing two approaches, pick one and see it through. You can always course-correct later if the chosen approach fails.
```

If you need a hard ceiling on thinking costs, extended thinking with a `budget_tokens` cap is still functional on Opus 4.6 and Sonnet 4.6 but is deprecated. Prefer lowering the [effort](https://platform.claude.com/docs/en/build-with-claude/effort) setting or using `max_tokens` as a hard limit with [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

### Leverage thinking & interleaved thinking capabilities

Claude's latest models offer thinking capabilities that can be especially helpful for tasks involving reflection after tool use or complex multi-step reasoning. You can guide its initial or interleaved thinking for better results.

Claude Opus 4.6 and Claude Sonnet 4.6 use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`), where Claude dynamically decides when and how much to think. Claude calibrates its thinking based on two factors: the `effort` parameter and query complexity. Higher effort elicits more thinking, and more complex queries do the same. On easier queries that don't require thinking, the model responds directly. In internal evaluations, adaptive thinking reliably drives better performance than extended thinking. Consider moving to adaptive thinking to get the most intelligent responses.

Use adaptive thinking for workloads that require agentic behavior such as multi-step tool use, complex coding tasks, and long-horizon agent loops. Older models use manual thinking mode with `budget_tokens`.

You can guide Claude's thinking behavior:

Example prompt

```
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
```

The triggering behavior for adaptive thinking is promptable. If you find the model thinking more often than you'd like, which can happen with large or complex system prompts, add guidance to steer it:

Sample prompt

```
Extended thinking adds latency and should only be used when it will meaningfully improve answer quality - typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

If you are migrating from [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) with `budget_tokens`, replace your thinking configuration and move budget control to `effort`:

**Before (extended thinking, older models):**

Python

```
client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=64000,
    thinking={"type": "enabled", "budget_tokens": 32000},
    messages=[{"role": "user", "content": "..."}],
)
```

**After (adaptive thinking):**

Python

```
client.messages.create(
    model="claude-opus-4-7",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # or "max", "xhigh", "medium", "low"
    messages=[{"role": "user", "content": "..."}],
)
```

If you are not using extended thinking, no changes are required. Thinking is off by default when you omit the `thinking` parameter.

-   **Prefer general instructions over prescriptive steps.** A prompt like "think thoroughly" often produces better reasoning than a hand-written step-by-step plan. Claude's reasoning frequently exceeds what a human would prescribe.
-   **Multishot examples work with thinking.** Use `<thinking>` tags inside your few-shot examples to show Claude the reasoning pattern. It will generalize that style to its own extended thinking blocks.
-   **Manual CoT as a fallback.** When thinking is off, you can still encourage step-by-step reasoning by asking Claude to think through the problem. Use structured tags like `<thinking>` and `<answer>` to cleanly separate reasoning from the final output.
-   **Ask Claude to self-check.** Append something like "Before you finish, verify your answer against \[test criteria\]." This catches errors reliably, especially for coding and math.

When extended thinking is disabled, Claude Opus 4.5 is particularly sensitive to the word "think" and its variants. Consider using alternatives like "consider," "evaluate," or "reason through" in those cases.

For more information on thinking capabilities, see [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) and [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

## Agentic systems

### Long-horizon reasoning and state tracking

Claude's latest models excel at long-horizon reasoning tasks with exceptional state tracking capabilities. Claude maintains orientation across extended sessions by focusing on incremental progress, making steady advances on a few things at a time rather than attempting everything at once. This capability especially emerges over multiple context windows or task iterations, where Claude can work on a complex task, save the state, and continue with a fresh context window.

#### Context awareness and multi-window workflows

Claude 4.6 and Claude 4.5 models feature [context awareness](https://platform.claude.com/docs/en/build-with-claude/context-windows#context-awareness-in-claude-sonnet-4-6-sonnet-4-5-and-haiku-4-5), enabling the model to track its remaining context window (i.e. "token budget") throughout a conversation. This enables Claude to execute tasks and manage context more effectively by understanding how much space it has to work.

**Managing context limits:**

If you are using Claude in an agent harness that compacts context or allows saving context to external files (like in Claude Code), consider adding this information to your prompt so Claude can behave accordingly. Otherwise, Claude may sometimes naturally try to wrap up work as it approaches the context limit. Below is an example prompt:

Sample prompt

```
Your context window will be automatically compacted as it approaches its limit, allowing you to continue working indefinitely from where you left off. Therefore, do not stop tasks early due to token budget concerns. As you approach your token budget limit, save your current progress and state to memory before the context window refreshes. Always be as persistent and autonomous as possible and complete tasks fully, even if the end of your budget is approaching. Never artificially stop any task early regardless of the context remaining.
```

The [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) pairs naturally with context awareness for seamless context transitions.

#### Multi-context window workflows

For tasks spanning multiple context windows:

1.  **Use a different prompt for the very first context window**: Use the first context window to set up a framework (write tests, create setup scripts), then use future context windows to iterate on a todo-list.

2.  **Have the model write tests in a structured format**: Ask Claude to create tests before starting work and keep track of them in a structured format (e.g., `tests.json`). This leads to better long-term ability to iterate. Remind Claude of the importance of tests: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."

3.  **Set up quality of life tools**: Encourage Claude to create setup scripts (e.g., `init.sh`) to gracefully start servers, run test suites, and linters. This prevents repeated work when continuing from a fresh context window.

4.  **Starting fresh vs compacting**: When a context window is cleared, consider starting with a brand new context window rather than using compaction. Claude's latest models are extremely effective at discovering state from the local filesystem. In some cases, you may want to take advantage of this over compaction. Be prescriptive about how it should start:
    -   "Call pwd; you can only read and write files in this directory."
    -   "Review progress.txt, tests.json, and the git logs."
    -   "Manually run through a fundamental integration test before moving on to implementing new features."
5.  **Provide verification tools**: As the length of autonomous tasks grows, Claude needs to verify correctness without continuous human feedback. Tools like Playwright MCP server or computer use capabilities for testing UIs are helpful.

6.  **Encourage complete usage of context**: Prompt Claude to efficiently complete components before moving on:

Sample prompt

```
This is a very long task, so it may be beneficial to plan out your work clearly. It's encouraged to spend your entire output context working on the task - just make sure you don't run out of context with significant uncommitted work. Continue working systematically until you have completed this task.
```

#### State management best practices

-   **Use structured formats for state data**: When tracking structured information (like test results or task status), use JSON or other structured formats to help Claude understand schema requirements
-   **Use unstructured text for progress notes**: Freeform progress notes work well for tracking general progress and context
-   **Use git for state tracking**: Git provides a log of what's been done and checkpoints that can be restored. Claude's latest models perform especially well in using git to track state across multiple sessions.
-   **Emphasize incremental progress**: Explicitly ask Claude to keep track of its progress and focus on incremental work

### Example: State tracking

### Balancing autonomy and safety

Without guidance, Claude Opus 4.6 may take actions that are difficult to reverse or affect shared systems, such as deleting files, force-pushing, or posting to external services. If you want Claude Opus 4.6 to confirm before taking potentially risky actions, add guidance to your prompt:

Sample prompt

```
Consider the reversibility and potential impact of your actions. You are encouraged to take local, reversible actions like editing files or running tests, but for actions that are hard to reverse, affect shared systems, or could be destructive, ask the user before proceeding.

Examples of actions that warrant confirmation:
- Destructive operations: deleting files or branches, dropping database tables, rm -rf
- Hard to reverse operations: git push --force, git reset --hard, amending published commits
- Operations visible to others: pushing code, commenting on PRs/issues, sending messages, modifying shared infrastructure

When encountering obstacles, do not use destructive actions as a shortcut. For example, don't bypass safety checks (e.g. --no-verify) or discard unfamiliar files that may be in-progress work.
```

### Research and information gathering

Claude's latest models demonstrate exceptional agentic search capabilities and can find and synthesize information from multiple sources effectively. For optimal research results:

1.  **Provide clear success criteria**: Define what constitutes a successful answer to your research question

2.  **Encourage source verification**: Ask Claude to verify information across multiple sources

3.  **For complex research tasks, use a structured approach**:

Sample prompt for complex research

```
Search for this information in a structured way. As you gather data, develop several competing hypotheses. Track your confidence levels in your progress notes to improve calibration. Regularly self-critique your approach and plan. Update a hypothesis tree or research notes file to persist information and provide transparency. Break down this complex research task systematically.
```

This structured approach allows Claude to find and synthesize virtually any piece of information and iteratively critique its findings, no matter the size of the corpus.

### Subagent orchestration

Claude's latest models demonstrate significantly improved native subagent orchestration capabilities. These models can recognize when tasks would benefit from delegating work to specialized subagents and do so proactively without requiring explicit instruction.

To take advantage of this behavior:

1.  **Ensure well-defined subagent tools**: Have subagent tools available and described in tool definitions
2.  **Let Claude orchestrate naturally**: Claude will delegate appropriately without explicit instruction
3.  **Watch for overuse**: Claude Opus 4.6 has a strong predilection for subagents and may spawn them in situations where a simpler, direct approach would suffice. For example, the model may spawn subagents for code exploration when a direct grep call is faster and sufficient.

If you're seeing excessive subagent use, add explicit guidance about when subagents are and aren't warranted:

Sample prompt for subagent usage

```
Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state. For simple tasks, sequential operations, single-file edits, or tasks where you need to maintain context across steps, work directly rather than delegating.
```

### Chain complex prompts

With adaptive thinking and subagent orchestration, Claude handles most multi-step reasoning internally. Explicit prompt chaining (breaking a task into sequential API calls) is still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure.

The most common chaining pattern is **self-correction**: generate a draft → have Claude review it against criteria → have Claude refine based on the review. Each step is a separate API call so you can log, evaluate, or branch at any point.

### Reduce file creation in agentic coding

Claude's latest models may sometimes create new files for testing and iteration purposes, particularly when working with code. This approach allows Claude to use files, especially python scripts, as a 'temporary scratchpad' before saving its final output. Using temporary files can improve outcomes particularly for agentic coding use cases.

If you'd prefer to minimize net new file creation, you can instruct Claude to clean up after itself:

Sample prompt

```
If you create any temporary new files, scripts, or helper files for iteration, clean up these files by removing them at the end of the task.
```

### Overeagerness

Claude Opus 4.5 and Claude Opus 4.6 have a tendency to overengineer by creating extra files, adding unnecessary abstractions, or building in flexibility that wasn't requested. If you're seeing this undesired behavior, add specific guidance to keep solutions minimal.

For example:

Sample prompt to minimize overengineering

```
Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused:

- Scope: Don't add features, refactor code, or make "improvements" beyond what was asked. A bug fix doesn't need surrounding code cleaned up. A simple feature doesn't need extra configurability.

- Documentation: Don't add docstrings, comments, or type annotations to code you didn't change. Only add comments where the logic isn't self-evident.

- Defensive coding: Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs).

- Abstractions: Don't create helpers, utilities, or abstractions for one-time operations. Don't design for hypothetical future requirements. The right amount of complexity is the minimum needed for the current task.
```

### Avoid focusing on passing tests and hard-coding

Claude can sometimes focus too heavily on making tests pass at the expense of more general solutions, or may use workarounds like helper scripts for complex refactoring instead of using standard tools directly. To prevent this behavior and ensure robust, generalizable solutions:

Sample prompt

```
Please write a high-quality, general-purpose solution using the standard tools available. Do not create helper scripts or workarounds to accomplish the task more efficiently. Implement a solution that works correctly for all valid inputs, not just the test cases. Do not hard-code values or create solutions that only work for specific test inputs. Instead, implement the actual logic that solves the problem generally.

Focus on understanding the problem requirements and implementing the correct algorithm. Tests are there to verify correctness, not to define the solution. Provide a principled implementation that follows best practices and software design principles.

If the task is unreasonable or infeasible, or if any of the tests are incorrect, please inform me rather than working around them. The solution should be robust, maintainable, and extendable.
```

### Minimizing hallucinations in agentic coding

Claude's latest models are less prone to hallucinations and give more accurate, grounded, intelligent answers based on the code. To encourage this behavior even more and minimize hallucinations:

Sample prompt

```
<investigate_before_answering>
Never speculate about code you have not opened. If the user references a specific file, you MUST read the file before answering. Make sure to investigate and read relevant files BEFORE answering questions about the codebase. Never make any claims about code before investigating unless you are certain of the correct answer - give grounded and hallucination-free answers.
</investigate_before_answering>
```

## Capability-specific tips

### Improved vision capabilities

Claude Opus 4.5 and Claude Opus 4.6 have improved vision capabilities compared to previous Claude models. They perform better on image processing and data extraction tasks, particularly when there are multiple images present in context. These improvements carry over to computer use, where the models can more reliably interpret screenshots and UI elements. You can also use these models to analyze videos by breaking them up into frames.

One technique that has proven effective to further boost performance is to give Claude a crop tool or [skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Testing has shown consistent uplift on image evaluations when Claude is able to "zoom" in on relevant regions of an image. Anthropic has created a [cookbook for the crop tool](https://platform.claude.com/cookbook/multimodal-crop-tool).

### Frontend design

Claude Opus 4.5 and Claude Opus 4.6 excel at building complex, real-world web applications with strong frontend design. However, without guidance, models can default to generic patterns that create what users call the "AI slop" aesthetic. To create distinctive, creative frontends that surprise and delight:

For a detailed guide on improving frontend design, see the blog post on [improving frontend design through skills](https://www.claude.com/blog/improving-frontend-design-through-skills).

Here's a system prompt snippet you can use to encourage better frontend design:

Sample prompt for frontend aesthetics

```
<frontend_aesthetics>
You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight.

Focus on:
- Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box!
</frontend_aesthetics>
```

You can also refer to the [full skill definition](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md).

## Migration considerations

When migrating to Claude 4.6 models from earlier generations:

1.  **Be specific about desired behavior**: Consider describing exactly what you'd like to see in the output.

2.  **Frame your instructions with modifiers**: Adding modifiers that encourage Claude to increase the quality and detail of its output can help better shape Claude's performance. For example, instead of "Create an analytics dashboard", use "Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation."

3.  **Request specific features explicitly**: Animations and interactive elements should be requested explicitly when desired.

4.  **Update thinking configuration**: Claude 4.6 models use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`) instead of manual thinking with `budget_tokens`. Use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth.

5.  **Migrate away from prefilled responses**: Prefilled responses on the last assistant turn are deprecated starting with Claude 4.6 models. See [Migrating away from prefilled responses](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#migrating-away-from-prefilled-responses) for detailed guidance on alternatives.

6.  **Tune anti-laziness prompting**: If your prompts previously encouraged the model to be more thorough or use tools more aggressively, dial back that guidance. Claude 4.6 models are significantly more proactive and may overtrigger on instructions that were needed for previous models.

For detailed migration steps, see the [Migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide).

### Migrating from Claude Sonnet 4.5 to Claude Sonnet 4.6

Claude Sonnet 4.6 defaults to an effort level of `high`, in contrast to Claude Sonnet 4.5 which had no effort parameter. Consider adjusting the effort parameter as you migrate from Claude Sonnet 4.5 to Claude Sonnet 4.6. If not explicitly set, you may experience higher latency with the default effort level.

**Recommended effort settings:**

-   **Medium** for most applications
-   **Low** for high-volume or latency-sensitive workloads
-   Set a large max output token budget (64k tokens recommended) at medium or high effort to give the model room to think and act

**When to use Opus 4.7 instead:** For the hardest, longest-horizon problems (large-scale code migrations, deep research, extended autonomous work), Opus 4.7 remains the right choice. Sonnet 4.6 is optimized for workloads where fast turnaround and cost efficiency matter most.

#### If you're not using extended thinking

If you're not using extended thinking on Claude Sonnet 4.5, you can continue without it on Claude Sonnet 4.6. You should explicitly set effort to the level appropriate for your use case. At `low` effort with thinking disabled, you can expect similar or better performance relative to Claude Sonnet 4.5 with no extended thinking.

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=8192,
    thinking={"type": "disabled"},
    output_config={"effort": "low"},
    messages=[{"role": "user", "content": "..."}],
)
```

#### If you're using extended thinking

If you're using extended thinking with `budget_tokens` on Claude Sonnet 4.5, it is still functional on Claude Sonnet 4.6 but is deprecated. Migrate to [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort).

##### Migrating to adaptive thinking

Adaptive thinking is particularly well suited to the following workload patterns:

-   **Autonomous multi-step agents:** coding agents that turn requirements into working software, data analysis pipelines, and bug finding where the model runs independently across many steps. Adaptive thinking lets the model calibrate its reasoning per step, staying on path over longer trajectories. For these workloads, start at `high` effort. If latency or token usage is a concern, scale down to `medium`.
-   **Computer use agents:** Claude Sonnet 4.6 achieved best-in-class accuracy on computer use evaluations using adaptive mode.
-   **Bimodal workloads:** a mix of easy and hard tasks where adaptive skips thinking on simple queries and reasons deeply on complex ones.

When using adaptive thinking, evaluate `medium` and `high` effort on your tasks. The right level depends on your workload's tradeoff between quality, latency, and token usage.

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{"role": "user", "content": "..."}],
)
```

##### Keeping budget\_tokens during migration

If you need to keep `budget_tokens` temporarily while migrating, a budget around 16k tokens provides headroom for harder problems without risk of runaway token usage. This configuration is deprecated and will be removed in a future model release.

**For coding use cases** (agentic coding, tool-heavy workflows, code generation), start with `medium` effort:

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16384,
    thinking={"type": "enabled", "budget_tokens": 16384},
    output_config={"effort": "medium"},
    messages=[{"role": "user", "content": "..."}],
)
```

**For chat and non-coding use cases** (chat, content generation, search, classification), start with `low` effort:

Python

```
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=8192,
    thinking={"type": "enabled", "budget_tokens": 16384},
    output_config={"effort": "low"},
    messages=[{"role": "user", "content": "..."}],
)
```

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>