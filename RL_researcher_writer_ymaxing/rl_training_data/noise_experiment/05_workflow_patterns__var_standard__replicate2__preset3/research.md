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

### Source [33]: https://masterofcode.com/blog/llm-orchestration

Query: What are key implementation considerations for synthesizing results from dynamically generated subtasks in an orchestrator LLM for complex customer service inquiries?

Answer: LLM orchestration frameworks manage dialogue flow, state across interactions, and provide templates for performance monitoring. LOFT framework features for customer service: Event handlers detect events in chat histories to automate inquiries and escalate complex issues; ErrorHandler manages issues by retrying/rerouting and alerting teams; Output middlewares modify LLM outputs before recording/sending for clarity and policy alignment; Sophisticated event management addresses hallucinations. Robust scalability handles increased loads; enhanced personalization via dynamic prompts. Orchestrator harmonizes LLMs, prompts, databases, agents ensuring components interact correctly. Business benefits: token economy by breaking tasks, operational reliability with observability. For complex inquiries, middleware and event handling ensure coherent synthesis and continuity.

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

### Source [37]: https://fayedigital.com/blog/ai-orchestration-platform/

Query: How do modular chaining, routing, and orchestration patterns contribute to more reliable and maintainable systems in the broader landscape of AI engineering workflows?

Answer: AI orchestration coordinates data pipelines, workflows, AI models, and agents into unified systems, producing stronger, more reliable outputs via consistent data and business context alignment, preventing unreliable results from siloed data. It reduces manual work, automates repetitive tasks, enables complex end-to-end workflows (e.g., email-to-CRM processing in 15min vs 24hrs), and supports scalable multi-agent automation. Benefits include faster execution, better governance/reduced risk with security/oversight, greater ROI by aligning with goals. Platforms manage model/agent coordination, data flows, monitoring for visibility into performance/bottlenecks. For maintainability, provides unified management, repeatable workflows, prevents tool sprawl, ensures governance across CRMs/ERPs. Essential for scaling without headcount growth, coordinating agents/systems, integrating data responsibly across org sizes.

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

### Source [43]: https://nmu.libguides.com/c.php?g=1474877&p=10982145

Query: What are proven prompt engineering techniques for decomposing complex content generation tasks like FAQ creation from renewable energy materials into focused subtasks for questions, answers, and citations?

Answer: Chain-of-Thought (CoT) prompting decomposes complex tasks into step-by-step reasoning: break into smaller prompts building on prior responses. E.g., for FAQ from materials: 1. Identify key concepts; 2. Generate questions; 3. Provide answers with reasoning; 4. Cite sources. Skeleton-of-Thought (SoT): Generate skeleton outline first (e.g., FAQ structure: questions list), then flesh out answers/citations in parallel. Tree-of-Thought explores branches for comprehensive coverage. Chain-of-Density iteratively densifies summaries with entities for concise answers. Chain-of-Verification ensures accuracy by verifying steps, ideal for cited content.

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
<summary>What information-theoretic principles explain accuracy gains from chaining specialized LLM calls versus complex single prompts?</summary>

Phase: [EXPLORATION]

### Source [62]: https://www.datacamp.com/tutorial/prompt-chaining-llm

Query: What information-theoretic principles explain accuracy gains from chaining specialized LLM calls versus complex single prompts?

Answer: The main purpose of prompt chaining is to improve the performance, reliability, and clarity of LLM applications. For complex tasks, a single prompt often doesn't provide enough depth and context for a good answer. Prompt chaining solves this by breaking the task into smaller steps, ensuring each step is handled carefully. This method improves the quality of the LLM output and makes it easier to understand how the final result was reached. When given a single prompt, LLMs might provide answers that are too broad, lack depth, or miss critical details. This limitation stems from the difficulty in capturing all necessary context and providing adequate guidance within a single prompt. Prompt chaining involves breaking down a complex task into a series of smaller, more manageable prompts. Each prompt tackles a specific part of the task, and the output from one prompt serves as the input for the next. This method allows for a more structured approach, guiding the LLM through a chain of reasoning steps that lead to a more accurate and comprehensive answer. Using a logical sequence of prompts, we can fully use LLMs to effectively solve complex problems.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://biomedeng.jmir.org/2026/1/e88053

Query: What information-theoretic principles explain accuracy gains from chaining specialized LLM calls versus complex single prompts?

Answer: This study aimed to test whether prompts based on NDM principles can improve LLM performance on a real-world, ill-defined task. The distinction between decision-making in idealized situations and in complex, ill-defined real-world settings has long been recognized in behavioral economics and psychology. Herbert Simon introduced the concept of bounded rationality to study how human decision-making takes place under limited cognitive and environmental resources rather than under the conditions of perfect knowledge and unlimited resources, the normative ideal of full rationality, which is currently assumed in many LLM benchmarks. Building on the idea of bounded rationality, the field of naturalistic decision-making (NDM) developed to study how experts make good decisions in real-world contexts. Research in NDM shows that, rather than exhaustively comparing all possible options, both experts make decisions. Although the chain-of-thought prompting strategy is inspired by human reasoning, particularly deductive decision-making, there is an ongoing debate about whether LLMs really replicate human reasoning or simply generate plausible-sounding explanations.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://www.mdpi.com/2079-9292/13/23/4712

Query: What information-theoretic principles explain accuracy gains from chaining specialized LLM calls versus complex single prompts?

Answer: Recent research has delved into the interplay between the size of Large Language Models (LLMs) and the architecture of prompts used to guide them. The consensus emerging from these studies is that, while larger models generally benefit from prompts containing a greater number of examples, enhancing their overall accuracy and reliability, this is not an absolute rule. In particular contexts, smaller, more specialized models have been shown to outperform their larger counterparts. This phenomenon is especially evident in highly specific domains where smaller LLMs, fine-tuned on domain-specific data, demonstrate superior accuracy and efficiency compared to generalized, larger models. The structure and complexity of prompts themselves play a critical role in determining LLM performance. Research has demonstrated that simple, straightforward prompt structures are often more effective for knowledge retrieval tasks compared to prompts that employ complex grammatical constructions. For instance, prompts with less syntactic complexity allow models to retrieve relevant information more consistently, minimizing the risk of misinterpretation or erroneous outputs. The chain-of-thought prompting technique encourages Large Language Models to break down complex tasks into intermediate reasoning steps, improving performance on tasks that require logical progression and detailed explanation.

-----

</details>

<details>
<summary>What context-management challenges arise in orchestrator LLMs during unpredictable dynamic task decomposition at scale?</summary>

Phase: [EXPLORATION]

### Source [66]: https://arxiv.org/html/2410.10039v1

Query: What context-management challenges arise in orchestrator LLMs during unpredictable dynamic task decomposition at scale?

Answer: One of the main challenges lies in managing the size and complexity of data over time. As the user interacts with the system, the graph database continues to grow, capturing each piece of information as nodes, with edges forming the relationships between them. Over time, this dynamic structure can become significantly large and complex, especially in cases of frequent or long-term interactions. The need to efficiently manage this expanding graph becomes crucial. As more nodes and edges are introduced, it can slow down the retrieval of relevant information, making it more difficult for the system to fetch the necessary context for a response. Additionally, the temporal nature of the graph—where each interaction is time-stamped—adds another layer of complexity, as the system must consider the time aspect when retrieving context. This methodology is designed to address several key challenges faced by traditional LLM-based systems. One of the most significant issues is context retention. By leveraging a temporal graph database, the system can track and maintain long-term context across multiple interactions. This allows it to generate responses that reflect the user’s evolving preferences, ensuring that the conversation remains coherent even over extended periods. The second challenge is efficient data retrieval. While vector databases offer a powerful mechanism for retrieving private data, they often struggle to provide contextually appropriate information. Our system overcomes this by guiding the vector database queries with the graph-based context, ensuring that the most relevant data is fetched and utilized. Limitations primarily stem from handling large-scale data in graph and vector databases, the iterative nature of the reflection phase, and inherent constraints in current LLM technologies. Data Size and Scalability issues arise in managing expanding graphs which slow retrieval and complicate context fetching in multi-LLM orchestration engines.

-----

-----

Phase: [EXPLORATION]

### Source [67]: https://www.sciencedirect.com/science/article/abs/pii/S0893608025000796

Query: What context-management challenges arise in orchestrator LLMs during unpredictable dynamic task decomposition at scale?

Answer: Despite advancements, LLM-based agents face substantial challenges in real-world tasks that demand complex planning, multi-stage reasoning, and tool utilization. For instance, in a recent agent benchmark, even GPT4 falls short with a success rate of 14%, while humans exceed 92%. Empowering agents to effectively address real-world tasks is challenging, arising from difficulties in both benchmark and methodological perspectives, such as error propagation and limited adaptability. Our multi-agent framework decomposes complex tasks into smaller, more manageable subtasks, while dynamically adjusting subsequent subtasks based on the completion status of preceding ones. For each subtask, a subtask-tailored subagent is generated using LLMs, differing from conventional approaches that rely on a single agent or a set of manually designed subagents. These subagents are equipped with an evolving and adaptable skill library, designed to meet the challenges of varied and unpredictable environments. The framework dynamically decomposes complex tasks into smaller subtasks and assigns each to a specifically generated subagent, thereby enhancing adaptability in diverse and unpredictable real-world tasks.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://arxiv.org/html/2402.10178v2

Query: What context-management challenges arise in orchestrator LLMs during unpredictable dynamic task decomposition at scale?

Answer: In our framework, complex tasks are decomposed into smaller, more manageable subtasks, addressing the challenge of excessive irrelevant contexts that may hinder LLM performance. LLM-based agents face substantial challenges in real-world tasks that demand complex planning, multi-stage reasoning, and tool utilization. For instance, in a recent agent benchmark, even GPT4 falls short with a success rate of 14%, while humans exceed 92%. Empowering agents to effectively address real-world tasks is challenging due to methodological constraints like error propagation and limited adaptability. Our multi-agent framework decomposes complex tasks into smaller subtasks, dynamically adjusting subsequent subtasks based on preceding ones. For each subtask, a subtask-tailored subagent is generated using LLMs. These subagents have an evolving skill library for varied and unpredictable environments. The framework features an advanced task decomposition strategy that dynamically adapts to evolving requirements and a flexible agent generation process for specific subtasks.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://www.amazon.science/blog/how-task-decomposition-and-smaller-llms-can-make-ai-more-affordable

Query: What context-management challenges arise in orchestrator LLMs during unpredictable dynamic task decomposition at scale?

Answer: Task decomposition typically introduces additional components like new LLMs and orchestrators, increasing system complexity and adding overhead. While smaller LLMs offer faster performance, the increased complexity can lead to higher latency. Sometimes decomposition into independent subtasks isn’t possible, requiring prompt engineering or information retrieval for coherence between subtasks. Overengineering should be avoided as it complicates workflows and risks sacrificing novelty and contextual richness that LLMs provide by capturing hidden relationships in the complete context. Task complexity as O(n): single LLM grows linearly, but parallel decomposition with k subtasks has initial O(1) decomposition plus O(n/k) per subtask, yet overall introduces trade-offs in complexity and latency for orchestrator systems.

-----

</details>

<details>
<summary>How do classification confidence thresholds influence failure modes and fallback reliability in LLM routing workflows?</summary>

Phase: [EXPLORATION]

### Source [71]: https://arxiv.org/html/2410.13284v2

Query: How do classification confidence thresholds influence failure modes and fallback reliability in LLM routing workflows?

Answer: In confidence-based routing, instances are routed to the larger LLM when the confidence score c_ℳ(x^(i), ŷ^(i)) < t for a threshold t ∈ [0,1]. Thresholds are set such that they correspond to routing approximately 0%, 5%, 10%, …, 100% of total instances. This determines which queries are handled by the smaller model and which are escalated. The paper discusses integrating confidence tokens to improve reliability and safety in real-world applications where errors are costly. It suggests future work on explicit rejection choices in Self-REF fine-tuning rather than relying solely on thresholding confidence token scores for rejection learning. Prior work uses classification models or routers for query routing to boost performance or reduce overhead, forming routing pipelines with mixture-of-experts systems.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://arxiv.org/html/2410.13284v3

Query: How do classification confidence thresholds influence failure modes and fallback reliability in LLM routing workflows?

Answer: In confidence-based routing, answers where the smaller fine-tuned LLM is uncertain (c_ℳ(x^(i), ŷ^(i)) < t) are routed to a more powerful LLM ℳ_Large. For high confidence (c_ℳ(x^(i), ŷ^(i)) ≥ t), the smaller model's answer is used. Thresholds ℳ𝒟_t = Q_p(ℂ_ℳ,𝒟) for p=0 to 20 correspond to routing 0% to 100% of instances. Uncertainty scores from LLMs may have weak correlation with prediction correctness, and consistent answers are not always the most correct, impacting routing reliability. The work focuses on downstream utility of confidence scores for routing and rejection learning beyond calibration.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://medium.com/@mr.murga/enhancing-intent-classification-and-error-handling-in-agentic-llm-applications-df2917d0a3cc

Query: How do classification confidence thresholds influence failure modes and fallback reliability in LLM routing workflows?

Answer: In hierarchical GPT classification for intent classification, a top-level GPT-based classifier processes input. If confidence is below a threshold (e.g., 0.7), it triggers fallback: asks for clarification or routes to a fallback domain. Otherwise, passes to lightweight domain-specific classifier. Errors in intent classification can cascade, so DAG structure enables dynamic routing, fallback handling, and corrections. Ingress & Classification Agent determines intent with high confidence; low confidence leads to fallback mechanisms improving error handling and reliability.

-----

</details>

<details>
<summary>What throughput cost and error-rate metrics quantify parallelization gains in real-world sequential-to-parallel FAQ pipelines?</summary>

Phase: [EXPLORATION]

### Source [76]: https://www.mdpi.com/1999-4893/18/4/182

Query: What throughput cost and error-rate metrics quantify parallelization gains in real-world sequential-to-parallel FAQ pipelines?

Answer: To quantify performance in parallel pipelines for urban water demand forecasting, the pipeline is instrumented to measure execution time of each major stage: (1) Data Preprocessing, (2) Outlier Detection, (3) Bi-LSTM Hyperparameter Optimization (HPO), (4) Bi-LSTM Imputation, (5) f-LSTM Forecasting, and (6) Random Forest Forecasting. These correspond to sequential steps, identifying parallelism benefits and bottlenecks. Overall end-to-end runtimes are computed. Throughput, measured as tasks completed per second, evaluates parallel processing capability. Outlier Detection achieves highest throughput at 40.8 tasks/second due to simple, parallelizable computations. Bi-LSTM Optimization and Imputation have lower throughputs of 1.86 and 0.078 tasks/second due to high computational demands. Throughput gains are achieved without significantly reducing task latency. Deep learning tasks maintain lower throughput due to model training/inference demands, while parallel execution accelerates overall speed with stable individual task times.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://arxiv.org/html/2504.03647v1

Query: What throughput cost and error-rate metrics quantify parallelization gains in real-world sequential-to-parallel FAQ pipelines?

Answer: Parallelization effectiveness depends on problem size, with overheads limiting small tasks and memory/cache issues large ones. Parallel patterns affect scalability, speedup, load balancing, overhead. LogP model refines parallel execution analysis with parameters: L (Latency: message communication delay), o (Overhead: processor time sending/receiving), g (Gap: minimum interval between transmissions), P (Processors). LogP accounts for real-world communication/computation costs in distributed-memory systems, addressing PRAM shortcomings like network overhead and latency.

-----

-----

Phase: [EXPLORATION]

### Source [79]: https://blog.budecosystem.com/different-parallelism-strategies-that-can-deliver-better-efficiency-for-your-genai-deployments/

Query: What throughput cost and error-rate metrics quantify parallelization gains in real-world sequential-to-parallel FAQ pipelines?

Answer: In pipeline parallelism for GenAI, Breadth-First Pipeline Parallelism optimizes scheduling, improving training throughput by up to 43% for 52B-parameter model vs. Megatron-LM, reducing time/cost with small per-GPU batches and high utilization. BPipe addresses activation memory bottleneck, cutting peak memory to 1/2-1/3 of 1F1B without throughput loss, eliminating bubble overhead. Shows 7%-55% higher throughput than 1F1B in pure pipelines, 16% gain in hybrid parallel training of language models. Enables smaller batch-per-GPU or longer sequences.

-----

-----

Phase: [EXPLORATION]

### Source [80]: https://www.starburst.io/blog/parallel-vs-sequential-processing/

Query: What throughput cost and error-rate metrics quantify parallelization gains in real-world sequential-to-parallel FAQ pipelines?

Answer: Parallel processing executes identical steps simultaneously vs. sequential one-after-another, reducing time (e.g., job in fourth time with four processors). Introduces synchronization overhead for task division/integration, but savings outweigh it. Sequential has dependencies; parallel suits many data operations.

-----

</details>

<details>
<summary>How do data pipeline patterns inform LLM chaining and routing?</summary>

Phase: [EXPLORATION]

### Source [81]: https://arxiv.org/html/2509.13487v1

Query: How do data pipeline patterns inform LLM chaining and routing?

Answer: Our approach employs task decomposition and prompt chaining techniques that break the analysis into focused sub-tasks, each designed to extract specific aspects of the pipeline architecture. The analysis begins with a plain-text description that captures objectives, processing steps, data flow patterns, configuration parameters, and external system interactions. [...] The emergence of LLMs has introduced new possibilities for code generation, with models demonstrating remarkable capabilities in generating code from natural language prompts [32, 33]. Unlike TBCG’s fixed templates, LLMs are probabilistic and context-driven, synthesizing code by learning patterns from massive code and text corpora . LLM-driven tools are increasingly applied to auto-generate pipeline code, with users prompting models for workflow descriptions and receiving complete scripts . However, generating complex, multi-component systems like data pipelines presents unique challenges including maintaining consistency across components, ensuring proper integration and data flow, and adhering to framework-specific best practices . Research indicates that LLMs, especially in direct [...] LLM-powered Generation, which employs prompt chaining with few-shot learning, guiding language models through separate phases: DAG structure generation (imports, arguments, context manager), individual operator instantiation for each workflow task, and dependency translation into platform-specific syntax. Each phase uses carefully crafted prompts with platform documentation examples for In-Context-Learning .

Both pathways incorporate comprehensive validation for syntactic correctness, extensive metadata headers for traceability (source YAML, timestamps, generation method, warnings), and preserve all parameter specifications from global pipeline settings to component-specific configurations using appropriate platform mechanisms (see F for full details on prompts and sample outputs). Data pipeline patterns inform LLM chaining by using task decomposition into sub-tasks mirroring pipeline processing steps and data flow, with prompt chaining ensuring consistency, proper integration, and data flow across components in generating pipeline code.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://meltano.com/blog/llm-apps-are-mostly-data-pipelines

Query: How do data pipeline patterns inform LLM chaining and routing?

Answer: Langchain is grouped in the Orchestration stage by a16z and is one of the main tools used by LLM app developers to do everything from extracting data from sources, to embedding documents and storing them in vector databases, to prompt chaining and storing memory for chat based apps…don’t worry if you dont understand some of these terms, I’ll explain them in the next section.

Inspired by those posts, I went on a deep dive to get a better understanding of what’s going on. I read through tons of articles, watched and listened to lots of youtube videos and podcast (on 2x speed), and built my own LLM chat app for answering questions based on the Meltano SDK docs.

In this blog post I’ll go through the following: [...] Data extraction – e.g. pull message text from the slack API
 Data cleansing – e.g. remove certain characters, extra spaces, encoding, etc.
 Data enrichment – embedding
 Data loading – write to vector databases
 Application UX i.e. prompt chaining, retrieval, inference, memory, chat UI, etc.

And those buckets look a lot like what a traditional data team has been doing for years:

 Data extraction – e.g. pull data from a variety of sources
 Data enrichment and transformation – e.g. remove duplicates, add consistent names, aggregate complex data into consumable business metrics, etc.
 Data loading – write to a data warehouse
 Data visualization and consumption – charts and dashboards that tell a story about the data [...] The first is a16z’s “Emerging Architectures for LLM Applications” article highlighting the emerging patterns for building Large Language Model (LLM) applications which highlighted the data pre-processing/embedding stage and how “this piece of the stack is relatively underdeveloped, though, and there’s an opportunity for data-replication solutions purpose-built for LLM apps”

The second was this spicey Reddit thread titled “Langchain Is Pointless“ which later hit hacker news  as well.

> “Why is this just not ETL, why do you need anything new category or product needed here? There is no new category or product needed here.” and “It is pointless – LlamaIndex and LangChain are re-inventing ETL – why use them when you have robust technology already?” Data pipeline patterns (ETL: extraction, transformation, loading) directly map to LLM app stages including prompt chaining in application UX, informing chaining as the orchestration layer akin to traditional data processing flows.

-----

-----

Phase: [EXPLORATION]

### Source [83]: https://datalearningscience.com/p/design-pattern-prompt-chaining-building

Query: How do data pipeline patterns inform LLM chaining and routing?

Answer: Variant: Extract-Format

 When to Use: When you need structured data (like JSON or CSV) from unstructured text.
 Key Tip: Always validate the fields and data types in the final output to catch errors early.

Variant: Brainstorm-Elaborate

 When to Use: Ideation, creative writing, and strategic planning.

Key Tip: Use a separate step to rank or filter the brainstormed ideas before elaborating on the best ones.

### Relevant Content

 LangChain Documentation on Chains:  (The canonical open-source implementation of this pattern).
 Foundational Concept: This pattern is a direct application of the pipeline design pattern in software engineering, adapted for LLM-based workflows.

### 📅 Next Pattern [...] # 1. Prompt Chaining - Building Step-by-Step AI Workflows

### Prompt Chaining is the Assembly Line for AI. Build complex results from simple, specialized steps.

Mario Lazo

Sep 21, 2025

### Prompt Chaining — Agentic Design Pattern Series

Prompt Chaining is a foundational pattern where you link multiple LLM calls together, using the output of one step as the input for the next, to create sophisticated, multi-step workflows.

> The Assembly Line for AI. Build complex results from simple, specialized steps. Data pipeline patterns inform LLM chaining as prompt chaining is explicitly a direct application of the pipeline design pattern in software engineering, adapted for LLM workflows, likened to an assembly line building complex results from simple steps.

-----

-----

Phase: [EXPLORATION]

### Source [84]: https://presentofcoding.substack.com/p/five-llm-tricks-for-data-pipelines

Query: How do data pipeline patterns inform LLM chaining and routing?

Answer: This structure also builds in error tolerance. If your LLM sample occasionally misses “Ruby,” you’ll probably see it in the next sample batch. You can also check completeness by comparing your found terms with your samples—and because you can model the likelihood of finding new terms by continuing to sample more, you can also quantify your sampling coverage. It’s also an example of using the LLM to label data for use with smaller models—similar to using LLMs to extract entities and use those labels to test or fine-tune your entity model, except in this case your “model” is just the presence or absence of each word.

Working with different kinds of text data pipelines makes these patterns easier to see. The more you do it, the faster you recognize when you need a new one. [...] I’m especially interested in LLM/non-LLM hybrid patterns like #3. The hybrid approach splits the work: the LLM samples your documents and extracts terms, then you use those terms with regular expressions to search your full dataset. You get the LLM’s ability to identify what’s actually in your data without manually building lists, combined with speed and transparency for the bulk processing. [...] Point made! I think I can stop writing about this pattern. So this is, instead, about a handful of other text-processing tricks I use LLMs for as part of data pipelines.

Most of these you could fold into your unstructured text pipeline; a couple work alongside tools like regular expressions or semantic clustering. They’re all variations on the same principle: if it’s a repetitive text processing task that’s easy-to-explain and doesn’t require a ton of judgement, you can write that into your data pipeline and have an LLM do it for you.

## 1. Column Discovery

The problem: Your pipeline processes data that’s fairly standardized, but column names and formats may vary between datasets. Data pipeline patterns inform LLM chaining by integrating LLMs into pipelines for tasks like sampling, extraction, and error-tolerant processing, using sequential LLM steps (chaining) within or alongside pipeline flows for text processing, entity extraction, and hybrid LLM/non-LLM approaches.

-----

-----

Phase: [EXPLORATION]

### Source [85]: https://medium.com/@shivangis2208/from-prompts-to-systems-prompt-chaining-in-agent-design-da493651214d

Query: How do data pipeline patterns inform LLM chaining and routing?

Answer: Prompts are executed in order, not independently.

   The LLM processes the first prompt and produces output
   That output is appended, summarized, or transformed
   The processed output is passed into the next prompt

This creates a pipeline flow:

> Prompt 1 → Output 1 → Prompt 2 → Output 2 → Prompt 3 → Final Result

4. Context Propagation

Each step inherits _context_ from earlier steps through the passed output.

   Earlier reasoning influences later decisions
   The model maintains consistency across the chain
   Errors or ambiguity can be caught early

This avoids overwhelming the model with all instructions at once.

5. Intermediate Validation (Optional but Recommended)

Outputs at each stage can be: [...] # From Prompts to Systems: Prompt Chaining in Agent Design | by Shivangi | Medium

Sitemap

Open in app

Sign up

Sign in

. Instead of asking an LLM to solve a problem in one large, monolithic step, this pattern promotes a divide-and-conquer strategy. The original problem is decomposed into a series of smaller, well-defined sub-tasks. Each sub-task is handled using a purpose-built prompt, and the output from one step is passed as input to the next, forming a logical chain of prompts. Data pipeline patterns inform LLM chaining through the explicit pipeline flow of sequential prompt execution (Prompt 1 → Output 1 → Prompt 2 → etc.), task decomposition into sub-tasks, context propagation for consistency, and intermediate validation, mirroring data pipeline sequencing and flow.

-----

</details>

<details>
<summary>What manufacturing assembly principles apply to LLM sequential workflows?</summary>

Phase: [EXPLORATION]

### Source [87]: https://arxiv.org/html/2410.21418v1

Query: What manufacturing assembly principles apply to LLM sequential workflows?

Answer: The integration of LLMs into smart manufacturing design addresses challenges in scalability. Traditional methods struggled with scalability, high data costs, suboptimal outcomes. LLMs deliver robust performance through generalization, handling multimodal, multitask learning. In advanced manufacturing, LLMs revolutionize design-to-manufacturing sequence, ensuring outputs are functional and manufacturable, minimizing redesigns and prototypes. This is termed GPT-CAD, applying to the design-to-manufacturing sequence in manufacturing workflows.

-----

-----

Phase: [EXPLORATION]

### Source [89]: https://www.newstreaming.com/5-strategies-for-streamlining-your-assembly-process/

Query: What manufacturing assembly principles apply to LLM sequential workflows?

Answer: Implement Lean Manufacturing Principles to eliminate waste and enhance efficiency. Techniques: 5S (Sort, Set in order, Shine, Standardize, Sustain), Kanban systems, Value Stream Mapping identify bottlenecks, reduce inventory, optimize material flow, creating agile assembly line. Invest in Automation Technologies: integrate robotics and automated systems for repetitive tasks, speeding up assembly line, improving precision and consistency. Optimize Layout and Workstation Design for assembly processes.

-----

-----

Phase: [EXPLORATION]

### Source [90]: https://leandatapoint.com/blog/manufacturing-process-flow

Query: What manufacturing assembly principles apply to LLM sequential workflows?

Answer: Flow production /Assembly line: fixed, sequential process where products move station to station with minimal interruption, ideal for high-volume standardized products, optimised using lean manufacturing to reduce waste, improve cycle time. Manufacturing process flow: structured steps in sequential order transforming raw materials to finished products, using shapes, symbols, arrows for order of operations. Assess process using SQDCP (Safety, Quality, Delivery, Cost, People) and PDCA (Plan-Do-Check-Act). Digitises production steps for SOP adherence, visibility, traceability, real-time KPI tracking.

-----

</details>

<details>
<summary>How are LLM workflow patterns adopted in creative media production?</summary>

Phase: [EXPLORATION]

### Source [92]: https://mlpills.substack.com/p/issue-110-llm-workflow-patterns

Query: How are LLM workflow patterns adopted in creative media production?

Answer: LLM workflow patterns include Prompt Chaining and Parallelisation. Prompt chaining is the most straightforward and structured workflow pattern. Each LLM call feeds into the next, forming a clear, linear sequence. Every step has a defined role: one might generate, another might critique, a third might edit or format. The system proceeds step by step until the desired outcome emerges. This approach works beautifully when tasks naturally break down into smaller, ordered subtasks. Parallelisation breaks away from linearity. Instead of executing one LLM call after another, you run many at once. Each instance might perform a different analysis, explore a different creative angle, or tackle a separate subtask. Once they finish, the system gathers the results, compares or merges them, and synthesises the final output. It’s the difference between asking a single expert for their opinion and consulting a whole panel simultaneously. This pattern excels when: A workflow is rule-driven. The developer sets the structure, and the LLM fills in the creative or analytical parts within that structure. Think of it like a well-rehearsed orchestra: every instrument knows when to play, though the LLM might improvise slightly within its solo. An agent, in contrast, decides its own moves. It can plan, choose which tools to use, and respond to feedback dynamically. Agents are more like jazz musicians—guided by skill and intuition rather than a fixed score. Most practical systems fall somewhere in between. They give the LLM some freedom to make decisions, but only inside a safe, predictable framework.

-----

-----

Phase: [EXPLORATION]

### Source [93]: https://scholarcommons.scu.edu/context/elec_senior/article/1107/viewcontent/Music_Creation_and_Recommendation_Applications_Publicaton.pdf

Query: How are LLM workflow patterns adopted in creative media production?

Answer: In LLM music creation and recommendation applications, workflows involve offline, on-device generation using LLMs for music creation. Mood Correction and Smoothing: For longer outputs, analyze emotional arc consistency across segments using a sliding-window classifier trained on valence/arousal scores. If inconsistencies are detected (e.g., a sudden switch from upbeat to dissonant), apply smoothing by transposing sections or adjusting rhythmic patterns. Export and Logging: Final outputs are stored in both MIDI and JSON formats for auditability. A metadata log includes generation settings (e.g., prompt, seed, sampling method), allowing reproducibility and comparative evaluation. Outputs can be directly used for playback in DAWs or uploaded to embedded targets such as Jetson Orin NX, where low-latency audio synthesis pipelines play the result in real time, aided by GPU-accelerated MIDI rendering engines. The system fulfills core purpose: enabling offline, on-device music generation and recommendation using a large language model (LLM). Each requirement is directly motivated by overarching goals of accessibility, low-latency performance, and creative flexibility. Execution time constrained to under 60 seconds for responsive interaction, crucial for real-time creativity.

-----

-----

Phase: [EXPLORATION]

### Source [95]: https://hdsr.mitpress.mit.edu/pub/15nqmdzl

Query: How are LLM workflow patterns adopted in creative media production?

Answer: Large Language Models (LLMs) help in design and manufacturing (CDaM) workflows across five phases. The study explores opportunities and challenges of applying LLMs in CDaM workflow. All building blocks (design, design spaces, manufacturing instructions, performance metrics) represented by compact programs. Every phase seen as translation layer between input domain-specific language (DSL) and output DSL. LLMs excel at such symbolic manipulations, addressing tasks while leveraging traditional solutions. Structured into two parts: first investigates current potential of LLMs in five phases; second presents end-to-end examples. Applies LLMs coherently across diverse tasks in design and manufacturing.

-----

</details>

<details>
<summary>What cloud-native technologies intersect with orchestrator-worker patterns?</summary>

Phase: [EXPLORATION]

### Source [96]: https://www.confluent.io/blog/event-driven-multi-agent-systems/

Query: What cloud-native technologies intersect with orchestrator-worker patterns?

Answer: Orchestrator-worker pattern

Using data streaming, you can adapt this pattern to make the agents event-driven. Data streaming technologies like Kafka offer key-based partitioning strategies, so the orchestrator can use keys to distribute command messages across partitions in a single topic. Worker agents can then act as a consumer group, pulling events from one or more assigned partitions to complete the work. Each worker agent then sends output messages into a second topic where it can be consumed by downstream systems.

The pattern now looks like this:

Event-driven orchestrator-worker pattern

While this diagram looks more complex, it dramatically simplifies the operations of the system. [...] The following explores four key patterns: orchestrator-worker, hierarchical agent, blackboard, and market-based. We show how each of these common multi-agent patterns are transformed into event-driven distributed systems, gaining the operational advantages of data streaming applications and removing the need for specialized communication paths for agent orchestration. We also describe the event-driven version of these patterns using conceptual models from Apache Kafka®. For anyone unfamiliar with Kafka, an accessible tour of its foundations can be found here.

### Orchestrator-worker pattern [...] ### Orchestrator-worker pattern

In this pattern, a central orchestrator assigns tasks to worker agents and manages their execution. This pattern, similar to the master-worker pattern in distributed computing, ensures efficient task delegation and centralized coordination while allowing workers to focus on specific, independent tasks.

Orchestrator-worker pattern

-----

-----

Phase: [EXPLORATION]

### Source [97]: https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL

Query: What cloud-native technologies intersect with orchestrator-worker patterns?

Answer: the need for custom failure handling, scaling logic, and direct worker management. Workers inherit distributed system guarantees from Kafka, reducing operational complexity while increasing reliability. This event-driven adaptation of the orchestrator-worker pattern provides a scalable, fault-tolerant foundation for real-world multi-agent systems. [...] The orchestrator-worker pattern is a well-known design pattern for structuring multi-agent systems. | Sean Falconer

[...] reassign the job. We can solve these problems by using an event-driven architecture. Instead of directly assigning tasks, the orchestrator can publish task events to Kafka, leveraging key-based partitioning for efficient workload distribution. Workers act as a consumer group, pulling events from the task queue. This shift brings several advantages: 🔗 Loose coupling – The orchestrator no longer tracks workers—it simply emits tasks as events. 📈 Automatic scaling – Kafka’s rebalance protocol redistributes work as workers are added or removed. 🔄 Resilient processing – If a worker fails, Kafka ensures that tasks can be replayed from the last committed offset, preventing data loss. By shifting coordination to the streaming layer, we eliminate the need for custom failure handling, scaling logic,

-----

-----

Phase: [EXPLORATION]

### Source [98]: https://cloudnativenow.com/features/7-cncf-tools-for-scheduling-and-orchestration/

Query: What cloud-native technologies intersect with orchestrator-worker patterns?

Answer: Kubernetes has become the near-standard container orchestration and scheduling utility, enabling engineers to better manage their distributed nodes from one control plane. Nowadays, it is the most actively maintained orchestrator, which means much of the other tooling in this area tends to integrate with Kubernetes and extend it into unique development scenarios. For example, kube-rs makes working with Kubernetes from the Rust language easier.

Techstrong Gang Youtube [...] Techstrong Gang Youtube

The Cloud Native Computing Foundation (CNCF) has been a force for new cloud-native tools in areas like streaming, observability, container runtime, CI/CD and others. Below, we’ll examine seven projects related to scheduling and orchestration that are hosted by the CNCF. Many of these open source projects are Kubernetes-aware and help deal with concerns like multi-cluster management, multi-cloud, data-intensive workloads and other specific requirements.

## 1. Kubernetes

A system for automating deployment, scaling and management of containerized applications

GitHub | Website [...] GitHub | Website

Kubernetes, often abbreviated as K8s, is the most widely used container orchestrator. Originally designed at Google, Kubernetes excels at scheduling and scaling large-scale container workloads, optimizing where they are run and handling many other application life cycle duties. As we’ve detailed before, Kubernetes is distinct from Docker although both tools are often used simultaneously. Kubernetes was open sourced in 2014 and is now a fully-graduated CNCF project.

## 2. Crossplane

A universal control plane.

GitHub | Website

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

<research_source type="scraped_from_research" phase="exploitation" file="developer-s-guide-to-multi-agent-patterns-in-adk-google-deve.md">
<details>
<summary>Developer’s guide to multi-agent patterns in ADK</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/>

# Developer’s guide to multi-agent patterns in ADK

DEC. 16, 2025

[Shubham Saboo](https://developers.googleblog.com/search/?author=Shubham+Saboo) Senior AI Product Manager

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/developer_guide_blog_Banner.original.png

The world of software development has already learned this lesson: monolithic applications don't scale. Whether you're building a massive e-commerce platform or a complex AI application, relying on a single, all-in-one entity creates bottlenecks, increases debugging costs, and limits specialized performance.

The same principle applies to an AI agent. A single agent tasked with too many responsibilities becomes a "Jack of all trades, master of none." As the complexity of instructions increases, adherence to specific rules degrades, and error rates compound, leading to more and more "hallucinations." If your agent fails, you shouldn't have to tear down the entire prompt to find the bug.

Reliability comes from decentralization and specialization. Multi-Agent Systems (MAS) allow you to build the AI equivalent of a microservices architecture. By assigning specific roles (a Parser, a Critic, a Dispatcher) to individual agents, you build systems that are inherently more modular, testable, and reliable.

In this guide we’ll be using the Google Agent Development Kit (ADK) to illustrate 8 essential design patterns, from the Sequential Pipeline to the Human-in-the-loop design pattern, providing you with the concrete patterns and pseudocode you need to build production-grade agent teams.

### **1\. Sequential Pipeline Pattern (aka the assembly line)**

Let’s start with the bread and butter of agent workflows. Think of this pattern as a classic assembly line where Agent A finishes a task and hands the baton directly to Agent B. It is linear, deterministic, and refreshingly easy to debug because you always know exactly where the data came from.

This is your go-to architecture for data processing pipelines. In the example below, we see a flow for processing raw documents: a Parser Agent turns a raw PDF into text, an Extractor Agent pulls out structured data, and a Summarizer Agent generates the final synopsis.

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/seqential_pattern.original.png

In ADK, the SequentialAgent primitive handles the orchestration for you. The secret sauce here is state management: simply use the output\_key to write to the shared session.state so the next agent in the chain knows exactly where to pick up the work.

```python

```

Python


Copied

### **2\. Coordinator/Dispatcher Pattern (aka the concierge)**

Sometimes you don't need a chain; you need a decision maker. In this pattern, a central, intelligent agent acts as a dispatcher. It analyzes the user's intent and routes the request to a specialist agent best suited for the job.

This is ideal for complex customer service bots where you might need to send a user to a "Billing" specialist for invoice issues versus a "Tech Support" specialist for troubleshooting.

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/coordinator_dispatcher_agent_pattern.original.png

This relies on LLM-driven delegation. You simply define a parent CoordinatorAgent and provide a list of specialist sub\_agents. The ADK's AutoFlow mechanism takes care of the rest, transferring execution based on the descriptions you provide for the children.

```python

```

Python


Copied

### **3\. Parallel Fan-Out/Gather Pattern (aka the octopus)**

Speed matters. If you have tasks that don't depend on each other, why run them one by one? In this pattern, multiple agents execute tasks simultaneously to reduce latency or gain diverse perspectives. Their outputs are then aggregated by a final "synthesizer" agent .

This is ideal for something like Automated Code Review. Instead of running checks sequentially, you can spawn a "Security Auditor," a "Style Enforcer," and a "Performance Analyst" to review a Pull Request simultaneously. Once they finish, a "Synthesizer" agent combines their feedback into a single, cohesive review comment.

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/parallel_fan-out.original.png

The ParallelAgent in ADK should be used to run sub-agents simultaneously. Be aware that although these agents operate in separate execution threads, they share the session state. To prevent race conditions, make sure each agent writes its data to a unique key.

```python

```

Python


Copied

### **4\. Hierarchical decomposition (aka the russian doll)**

Sometimes a task is too big for one agent context window. High-level agents can break down complex goals into sub-tasks and delegate them. Unlike the routing pattern, the parent agent might delegate just _part_ of a task and wait for the result to continue its own reasoning.

In this diagram, we see a ReportWriter that doesn't do the research itself. It delegates to a ResearchAssistant, which in turn manages WebSearch and Summarizer tools.

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/hierarchical_task_decomposition_agent.original.png

You can treat a sub-agent as a tool here. By wrapping an agent in AgentTool, the parent agent can call it explicitly, effectively treating the sub-agent's entire workflow as a single function call.

```python

```

Python


Copied

### **5\. Generator and critic (aka the editor's desk)**

Generating high-quality, reliable output often requires a second pair of eyes. In this pattern, you separate the creation of content from the validation of content. One agent acts as the Generator, producing a draft, while a second agent acts as the Critic, reviewing it against specific, hard-coded criteria or logical checks.

This architecture is distinct because of its conditional looping. If the review passes, the loop breaks, and the content is finalized. If it fails, specific feedback is routed back to the Generator to produce a compliant draft. This is incredibly useful for code generation that needs syntax checking or content creation requiring compliance review.

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/generator_critic_agent_pattern.original.png

To implement this in ADK, you separate concerns into two specific primitives: a SequentialAgent that manages the draft-and-review interaction, and a parent LoopAgent that enforces the quality gate and exit condition.

```python

```

Python


Copied

### **6\. Iterative refinement (aka the sculptor)**

Great work rarely happens in a single draft. Just like a human writer needs to revise, polish, and edit, sometimes your agents need a few attempts to get an answer exactly right. In this pattern, agents enter a cycle of generating, critiquing, and refining until the output meets a specific quality threshold.

Unlike the Generator and Critic pattern, which focuses on correctness (Pass/Fail), this pattern focuses on qualitative improvement. A Generator creates a rough draft, a Critique Agent provides optimization notes, and a Refinement Agent polishes the output based on those notes

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/iterative_refinement_agent_pattern_1.original.png

This pattern is implemented using the LoopAgent. A critical component here is the exit mechanism. While you can set a hard limit using max\_iterations, ADK also allows agents to signal early completion. An agent can trigger an exit by signaling escalate=True within its EventActions if the quality threshold is met before the maximum iterations are reached.

```python

```

Python


Copied

### **7\. Human-in-the-loop (the human safety net)**

AI Agents are powerful, but sometimes you need a human in the driver's seat for critical decision-making. In this model, agents handle the groundwork, but a human must authorize high-stakes actions - specifically those that are irreversible or carry significant consequences. This includes executing financial transactions, deploying code to production, or taking action based on sensitive data (as opposed to merely processing it), ensuring safety and accountability.

The diagram shows a Transaction Agent processing routine work. When a high-stakes check is needed, it calls an ApprovalTool Agent, which pauses execution and waits for a Human Reviewer to say "Yes" or "No."

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/human-in-the-loop_pattern.original.png

ADK allows you to implement this via custom tools. An agent can call an approval\_tool which pauses execution or triggers an external system to request human intervention.

```python

```

Python


Copied

### **8\. Composite patterns (the mix-and-match)**

Real-world enterprise applications rarely fit into a single box. You will likely combine these patterns to build production-grade applications.

For example, a robust Customer Support system might use a **Coordinator** to route requests. If the user has a technical issue, that branch might trigger a **Parallel** search of documentation and user history. The final answer might then go through a **Generator and Critic** loop to ensure tone consistency before being sent to the user.

https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/composite_agent_pattern.original.png

### **A few pro-tips before you start:**

- **State management is vital:** In ADK, session.state is your whiteboard. Use descriptive keys when using output\_key so downstream agents know exactly what they are reading.
- **Clear descriptions:** When using routing, the description field of your sub-agents is effectively your API documentation for the LLM. Be precise.
- **Start simple:** Do not build a nested loop system on day one. Start with a sequential chain, debug it, and then add complexity.

## Get Started Now

Ready to build your team of agents? Check out the [ADK Documentation](https://google.github.io/adk-docs/) to get started. We can’t wait to see what you build.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-tool-chaining-fails-in-production-llm-agents-and-how-to-.md">
<details>
<summary>How Tool Chaining Fails in Production LLM Agents and How to Fix It</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://futureagi.substack.com/p/how-tool-chaining-fails-in-production>

# How Tool Chaining Fails in Production LLM Agents and How to Fix It

### Why Multi-Tool Orchestration Breaks in Production and the Patterns That Make It Reliable

[https://substackcdn.com/image/fetch/$s_!nJhF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6b1b4fc-8c10-4429-89a7-d603d3ae0b70_2566x1642.heic](https://substackcdn.com/image/fetch/$s_!nJhF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6b1b4fc-8c10-4429-89a7-d603d3ae0b70_2566x1642.heic)

Tool chaining is the backbone of every useful agentic AI system. When an LLM agent completes a multi-step task, it calls one tool, takes the output, and feeds it into the next tool in sequence. This is multi-tool orchestration at its core. It works in demos. It consistently breaks in production.

The pattern is familiar to anyone building LLM-powered applications. Your agent chains three or four tool calls together. The first call returns slightly malformed output. The second tool accepts it but misinterprets a field. By the third call, the entire chain has gone off the rails. This is the cascading failure problem, and it remains the primary bottleneck to agent reliability in 2026. [Research from Zhu et al. (2025)](https://arxiv.org/pdf/2509.25370?) confirms that error propagation is the single biggest barrier to building dependable LLM agents.

This guide breaks down why tool chaining fails, how context preservation collapses across chained calls, what evaluation frameworks catch failures before they reach users, and practical patterns using LangGraph and LangChain.

## What Is Tool Chaining and Why It Matters for Agentic AI

Tool chaining is the sequential execution of multiple tool calls by an LLM agent, where each tool’s output becomes the input for the next tool in the sequence. An agent receives a user query, decides it needs data from an API, processes that data with a second tool, and generates a final response using the combined results.

This differs from a single tool call in important ways. A single call is straightforward: the LLM calls a function, gets a result, and responds. Chaining creates dependencies. The agent must determine the right order of operations, track intermediate state, and handle partial failures while staying focused on the original goal. In multi-agent systems, the complexity increases further because one agent might call a tool, hand the result to a second agent, which runs its own tool sequence before returning. The orchestration overhead compounds quickly, and potential failure points grow with it.

Consider a practical example. A user asks an agent to find earnings data, compare it to competitors, and generate a summary. If the first call returns revenue in the wrong currency, the comparison runs but produces misleading figures. The summary then confidently presents wrong data. No error was thrown. That is the core danger of tool chaining without validation and observability.

## The Core Challenges of Tool Chaining in Production

### Context Preservation Across Tool Calls

Context preservation is the ability to maintain relevant information as data flows from one tool call to the next. LLMs operate within a finite context window, and every tool call adds tokens to that window through function parameters, response payloads, and the agent’s reasoning about what to do next. In long chains, critical context from early steps can be pushed out of the window or diluted by intermediate results.

This problem is well documented. Research shows that LLMs lose performance on information buried in the middle of long contexts, even with large context windows. When an agent forgets a user constraint from step 1 by the time it reaches step 5, the output may be technically valid but factually wrong. The user asked for revenue in USD, but the agent lost that detail three tool calls ago.

There are practical fixes. Use structured state objects instead of raw text to pass data between tool calls, keeping the payload compact and parseable. Summarize intermediate results before passing them forward by stripping out metadata the next tool does not need. Use frameworks like LangGraph that provide explicit state management across graph nodes, keeping context durable and inspectable.

### Cascading Failures and Error Propagation

Cascading failures are the biggest production risk in tool chaining. When one tool in the chain produces an incorrect or partial result, that error flows downstream and compounds at every subsequent step. Unlike traditional software where errors throw exceptions, LLM tool chains often fail silently because the agent treats bad output as valid input and moves on.

A 2025 study published on [OpenReview](https://openreview.net/forum?id=PFR4E8583W) analyzed failed LLM agent trajectories and found that error propagation was the most common failure pattern, with memory and reflection errors being the most frequent cascade sources. Once these cascades begin, they are extremely difficult to reverse mid-chain.

In [multi-agent systems](https://arxiv.org/abs/2503.13657), cascading failures are amplified. The Gradient Institute found that transitive trust chains between agents mean a single wrong output propagates through the entire chain without verification. OWASP ASI08 specifically identifies cascading failures as a top security risk in agentic AI.

### Context Window Saturation

Every tool call consumes context window tokens. A chain of five calls can easily use 40 to 60 percent of available tokens before the agent generates its final response.

## Tool Chaining Failure Modes: A Developer Reference

Understanding common failure modes helps you build defenses early.

**Silent data corruption** occurs when a tool returns the wrong format and the agent passes it forward undetected. Add schema validation using JSON Schema or Pydantic on every tool output.

**Context loss** happens when key data from early calls gets pushed out of the context window. Use explicit state management and carry forward only essential fields.

**Cascading hallucination** is when the agent fills missing data with hallucinated values after a tool returns incomplete results. Implement strict null checks and instruct the agent to stop and report missing data.

**Tool misuse** occurs when the agent calls the wrong tool or uses incorrect parameters. Write precise tool descriptions with parameter examples and constraints.

**Timeout cascade** is triggered when one slow tool causes subsequent calls to timeout. Set per-tool timeouts and implement circuit breakers to isolate slow tools.

**Error swallowing** happens when API errors are caught but not surfaced, so the agent proceeds with empty data. Return explicit error objects and train the agent to handle error responses differently.

## Frameworks for Multi-Tool Orchestration

The right framework reduces the difficulty of building reliable tool chains. Here is how the leading options compare for production multi-tool orchestration in 2026.

**[LangGraph](https://www.langchain.com/langgraph)** is best suited for stateful, branching workflows with conditional routing. It offers graph-based state machine execution with durable checkpoints and deep tracing via LangSmith. Every node represents either a tool call or a decision point, and edges define transitions between steps. This makes it straightforward to add retry logic, fallback paths, and human-in-the-loop checkpoints. Its durable execution feature means that if a chain breaks at step 4 out of 7, it can resume from that exact point instead of restarting from scratch.

**[LangChain](https://www.langchain.com/)** remains the most popular starting point for LLM application development. Its LCEL pipe syntax makes it quick to compose linear tool chains, with tracing through LangSmith and Langfuse. For production workloads with branching logic or parallel tool calls, most teams migrate to LangGraph for additional control.

**AutoGen** is designed for multi-agent conversation collaboration using message-passing with built-in function call semantics. It offers moderate observability and needs external tooling for production traces.

**CrewAI** handles role-based multi-agent task execution with task delegation and tool assignment per role. It provides basic logging and tends toward longer deliberation before tool calls.

## Distributed Tracing and Observability for Tool Chains

You cannot fix what you cannot see. Observability is critical for tool chaining because failures are often silent. A tool chain that produces a wrong answer without throwing errors looks fine in your logs unless you have distributed tracing capturing every step.

Every tool chain should trace the following: the exact input and output of each tool call for failure replay, latency per step to catch timeout cascades, token consumption to identify context window saturation, and the agent’s reasoning between calls to surface logic errors.

Tools like LangSmith, Langfuse, and Future AGI provide native tracing for LangGraph and LangChain workflows. [Future AGI’s traceAI SDK](https://github.com/future-agi/traceAI?utm_source=toolchaining&utm_medium=Blog&utm_campaign=blog_page) integrates with OpenTelemetry and provides built-in evaluation metrics for completeness, groundedness, and function calling accuracy.

## Evaluation Frameworks for Tool Chaining

Tracing tells you what happened. Evaluation frameworks tell you whether it was correct. For tool chains, evaluation must cover tool selection accuracy, parameter correctness, chain completion rate, output faithfulness, and error recovery rate.

Running evaluations at scale requires automation. Platforms like Future AGI attach [evaluation metrics](https://app.futureagi.com/dashboard/evaluations?utm_source=toolchaining&utm_medium=Blog&utm_campaign=blog_page) directly to traces, scoring every execution and creating a continuous feedback loop.

## Building Reliable Tool Chains for Production

Based on real-world production deployments and current research, these patterns consistently improve tool chaining reliability.

**Validate at every boundary.** Add input and output validation between every tool call using Pydantic or JSON Schema. Explicit validation catches errors at the source before they propagate.

**Use plan-then-execute architecture.** Research from Scale AI shows that having the LLM formulate a structured plan first and then running it through a deterministic executor reduces tool chaining errors significantly. This separates reasoning from execution.

**Implement circuit breakers.** If a tool fails or returns unexpected results more than N times, break the circuit and return a graceful failure. This prevents one broken tool from taking down the entire workflow.

**Keep chains short.** Longer chains mean more failure opportunities and more context consumption. If your chain needs more than five or six sequential calls, restructure into sub-chains or parallel branches.

**Test with adversarial inputs.** Standard test cases will pass. Production traffic will not be standard. Test with empty responses, large payloads, unexpected types, and ambiguous queries.

**Trace everything from day one.** Instrument tool chains with distributed tracing from the first deployment. When something breaks, traces are the difference between hours of debugging and a quick fix.

## Conclusion

Tool chaining separates demo-ready agents from production-ready ones. The gap comes down to how well you handle cascading failures, preserve context across calls, and evaluate every execution against clear quality criteria. LangGraph provides the control structure, LangChain provides the integration layer, and evaluation platforms close the feedback loop.

Teams that ship reliable agentic AI treat multi-tool orchestration as a first-class engineering problem. Validate at every boundary, trace every execution, evaluate continuously, and keep chains short.

## Frequently Asked Questions

**What is tool chaining in LLM agents?**

Tool chaining is the sequential execution of multiple tool calls by an LLM agent, where each tool’s output feeds into the next step. It allows agentic AI systems to break down multi-step tasks and complete them by combining data from different sources and processing stages.

**Why do cascading failures happen in multi-tool orchestration?**

Cascading failures occur because LLM agents treat malformed tool outputs as valid inputs. The agent does not throw exceptions for bad data. Instead, it silently passes errors forward, compounding them at each subsequent step until the final output is completely wrong.

**How does context preservation affect tool chaining reliability?**

Every tool call consumes context window tokens, and critical information from early steps can get diluted or pushed out entirely. When the agent loses a user constraint or data point from earlier calls, it produces outputs that seem valid but miss key requirements.

**What evaluation frameworks help test tool chains with Future AGI?**

[Future AGI](https://docs.futureagi.com/home?utm_source=toolchaining&utm_medium=Blog&utm_campaign=blog_page) provides automated evaluation metrics that attach directly to distributed traces. These metrics measure tool selection accuracy, parameter correctness, output faithfulness, and chain completion rate, enabling continuous automated assessment of every tool chain execution at scale.

**How does LangGraph handle tool chaining differently from LangChain?**

LangGraph models tool chains as graph-based state machines with explicit nodes, edges, and conditional routing. This gives developers fine-grained control over execution flow, retry logic, and checkpoints. LangChain uses a simpler pipe-based syntax better suited for linear chains.

**What role does distributed tracing play in debugging tool chain failures?**

Distributed tracing records the inputs, outputs, latency, and token usage for every tool call in the chain. Because tool chain failures can be easy to miss, traces help developers identify the exact step where an error originates and track how it ripples through everything that follows.

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