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

<research_source type="scraped_from_research" phase="exploitation" file="what-prompts-don-t-say-understanding-and-managing-underspeci.md">
<details>
<summary>What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2505.13360v1>

# What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts

Chenyang Yang Yike Shi Qianou Ma Michael Xieyang Liu

Christian KästnerTongshuang Wu

Carnegie Mellon University

\faGithub [https://github.com/malusamayo/underspec-analysis](https://github.com/malusamayo/underspec-analysis "")Now at Google Deepmind.

###### Abstract

Building LLM-powered software requires developers to communicate their requirements through natural language,
but developer prompts are frequently underspecified, failing to fully capture many user-important requirements.
In this paper, we present an in-depth analysis of prompt underspecification,
showing that while LLMs can often (41.1%) guess unspecified requirements by default, such behavior is less robust:
Underspecified prompts are 2x more likely to regress over model or prompt changes, sometimes with accuracy drops by more than 20%.
We then demonstrate that simply adding more requirements to a prompt does not reliably improve performance, due to LLMs’ limited instruction-following capabilities and competing constraints, and standard prompt optimizers do not offer much help.
To address this, we introduce novel requirements-aware prompt optimization mechanisms that can improve performance by 4.8% on average over baselines that naively specify everything in the prompt.
Beyond prompt optimization, we envision that effectively managing prompt underspecification requires a broader process, including proactive requirements discovery, evaluation, and monitoring.

## 1 Introduction

As large language models (LLMs) are improving in capabilities and instruction following \[ [30](https://arxiv.org/html/2505.13360v1#bib.bib30 "")\], they are increasingly integrated into business applications \[e.g., [3](https://arxiv.org/html/2505.13360v1#bib.bib3 ""), [7](https://arxiv.org/html/2505.13360v1#bib.bib7 "")\] through customized instruction prompts that can span thousands of words \[e.g., [1](https://arxiv.org/html/2505.13360v1#bib.bib1 ""), [2](https://arxiv.org/html/2505.13360v1#bib.bib2 "")\].
Conveying nuanced intentions to LLMs, however, is inherently difficult.
For end users interacting directly with a model (e.g., ChatGPT), this issue is less significant, as their prompts are typically one-off and considered successful as long as they yield one satisfactory response.
For developers of LLM-powered applications, the problem is much more serious, as their prompts need to generalize to many different user inputs.

As an example (Figure [1](https://arxiv.org/html/2505.13360v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), think about a developer working on an LLM-powered trip advisor application:
The developer builds a prompt that specifies LLMs’ task ➀, tone ➁, and various behaviors, including avoiding transaction handling ➂ and clarify ambiguity ➃.
This prompt is detailed yet still underspecified in many aspects:
For example, it does not specify whether LLMs should alert users of potential weather conditions, proactively ask follow-up questions, or remind visa (entry) requirements for suggested destinations.
If the LLM ends up not satisfying these requirements, it can cause frustrations and failures, such as users booking travel activities during bad weather, receiving vague recommendations, or facing denied entry due to visa issues, ultimately undermining trust in the LLM-powered applications.
Indeed, failing to mention prerequisites of suggested activities has already led to a chaotic user experience with an existing LLM-powered trip advisor \[ [6](https://arxiv.org/html/2505.13360v1#bib.bib6 "")\].

While it is possible that developers simply do not care enough to specify these behaviors, it is equally – if not more – likely that current engineering and evaluation practices make it difficult for developers to identify such underspecification until they have already led to issues in deployment (Section [2](https://arxiv.org/html/2505.13360v1#S2 "2 Underspecification is Amplified in LLM Prompts ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
Even if developers do not believe these behaviors must be explicitly defined, they may expect models to act consistently along these dimensions to support more stable user mental models of LLM applications,
which is, however, not the case for many unspecified requirements (Figure [1](https://arxiv.org/html/2505.13360v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).

https://arxiv.org/html/2505.13360v1/x1.pngFigure 1: Developers often underspecify their prompts and miss user-important requirements.
These unspecified requirements might be guessed by LLMs by default, but are more often inconsistent across prompts or LLMs.
Such underspecification can cause frustration and failures for the end users.

In this work, we characterize (Section [2](https://arxiv.org/html/2505.13360v1#S2 "2 Underspecification is Amplified in LLM Prompts ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")) and empirically analyze (Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")) the problem of prompt underspecification.
To systematically study the effects of underspecification, we curated a set of diverse requirements across 3 representative tasks, constructed a series of prompts that specify different subsets of the requirements, and evaluated each requirement’s satisfaction rate with human-validated LLM-as-a-judge \[ [48](https://arxiv.org/html/2505.13360v1#bib.bib48 "")\] on all prompts.
In total, we collected 8.4k data points of LLM+Prompts’ aggregated behaviors on diverse requirements.
Our analysis demonstrated that, _while LLMs can indeed often (41.1%) fill in the underspecification gap, their behaviors are rather inconsistent:_
One version of an LLM may excel in fulfilling an unspecified requirement, but the next version can unexpectedly degrade by more than 20%.
This will be a problem for continuously developing, deploying, and maintaining LLM-powered applications reliably.

We then introduce requirements-aware prompt optimization as a solution strategy to deliberately communicate important requirements to the model, while leaving those already implicitly fulfilled unspecified.
We show that such strategies overcome issues with existing approaches:
The obvious strategy of simply specifying all requirements in the prompt does not work, due to LLMs’ limited instruction-following capabilities – their performance can drop by 19% as we specify more requirements (Section [3.5](https://arxiv.org/html/2505.13360v1#S3.SS5 "3.5 LLMs struggle with following many requirements at the same time ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")),
and requirement-agnostic prompt optimization only provides limited help since they have no requirement-specific feedback.
We propose and evaluate two requirement-aware prompt optimizers (Section [4](https://arxiv.org/html/2505.13360v1#S4 "4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")):
One to optimize how to specify requirements,
and the other to explicitly optimize what requirements to specify.
We demonstrate that both strategies work well (+4.8% accuracy), and the latter can produce shorter prompts (-43% tokens) that are easier to follow for the model.

Finally, we discuss what it takes to properly manage prompt underspecification when building LLM-powered applications in practice beyond prompt optimization (Section [5](https://arxiv.org/html/2505.13360v1#S5 "5 Towards Managing Prompt Underspecification ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")):
This includes proactively discovering important requirements, building reliable requirement evaluators, as well as continuously evaluating and monitoring (un-)specified requirements.
We highlight the research opportunities here to support the entire process of managing prompt (under-)specification.

In summary, our work makes the following contribution:
(1) Characterization of the underspecification problem in LLM prompts (Section [2](https://arxiv.org/html/2505.13360v1#S2 "2 Underspecification is Amplified in LLM Prompts ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")),
(2) an empirical analysis of LLM+Prompt behaviors when underspecified (Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")),
(3) mitigation mechanisms with requirements-aware prompt optimizers (Section [4](https://arxiv.org/html/2505.13360v1#S4 "4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), and
(4) a discussion of our vision for managing prompt underspecification (Section [5](https://arxiv.org/html/2505.13360v1#S5 "5 Towards Managing Prompt Underspecification ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).

## 2 Underspecification is Amplified in LLM Prompts

While underspecification is a known challenge in traditional software engineering and machine learning pipelines \[ [17](https://arxiv.org/html/2505.13360v1#bib.bib17 ""), [11](https://arxiv.org/html/2505.13360v1#bib.bib11 "")\],
it is significantly exacerbated in the context of LLM prompting.
In this section, we articulate unique characteristics in LLM prompts that make underspecification more challenging:
Unlike traditional systems, prompt engineering is informal, fast-changing, and rarely guided by systematic engineering practices \[ [22](https://arxiv.org/html/2505.13360v1#bib.bib22 ""), [43](https://arxiv.org/html/2505.13360v1#bib.bib43 "")\].
Moreover, LLM behaviors are highly sensitive to prompt phrasing and LLM versions, which further amplifies the effects of underspecification.
A summary of comparison is in Table [1](https://arxiv.org/html/2505.13360v1#S2.T1 "Table 1 ‣ 2 Underspecification is Amplified in LLM Prompts ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

Table 1: Compared to traditional ML models and software, LLM prompts are more prone to underspecification, exhibit greater instability, and evolve more frequently.
Prompt engineering practices and the dynamic LLM+prompt interplay both amplify these issues.

| Aspect | LLM Prompt | Traditional ML Models | Traditional Software |
| --- | --- | --- | --- |
| Specification Method | Natural language prompts (instructions, examples) | Training data and model architecture and pipeline | Usually natural language and sometimes formal specifications |
| Engineering Practices | Ad-hoc, trial-and-error prompt iteration \[ [22](https://arxiv.org/html/2505.13360v1#bib.bib22 ""), [43](https://arxiv.org/html/2505.13360v1#bib.bib43 "")\] | More structured experimentation pipelines \[ [16](https://arxiv.org/html/2505.13360v1#bib.bib16 "")\] | Systematic requirements engineering and design processes \[ [40](https://arxiv.org/html/2505.13360v1#bib.bib40 "")\] |
| Artifact Evolution | Frequent changes with little version control \[ [39](https://arxiv.org/html/2505.13360v1#bib.bib39 ""), [22](https://arxiv.org/html/2505.13360v1#bib.bib22 "")\] | Periodical evolution with some version control \[ [16](https://arxiv.org/html/2505.13360v1#bib.bib16 "")\] | Evolution often intentionally tracked and limited \[ [25](https://arxiv.org/html/2505.13360v1#bib.bib25 ""), [8](https://arxiv.org/html/2505.13360v1#bib.bib8 "")\] |
| Behavioral Stability | Highly sensitive to prompt phrasing and LLM version \[ [9](https://arxiv.org/html/2505.13360v1#bib.bib9 ""), [24](https://arxiv.org/html/2505.13360v1#bib.bib24 "")\] | Moderate variability across training runs and datasets \[ [11](https://arxiv.org/html/2505.13360v1#bib.bib11 "")\] | Mostly deterministic and version-controlled |
| Symptoms of Underspecification | Inconsistent and unexpected LLM behaviors (Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")) | Generalization failures, bias due to data underspecification \[ [11](https://arxiv.org/html/2505.13360v1#bib.bib11 "")\] | Software that does not meet customer needs; incorrect behavior in edge cases \[ [36](https://arxiv.org/html/2505.13360v1#bib.bib36 ""), [21](https://arxiv.org/html/2505.13360v1#bib.bib21 "")\] |

Prompt engineering practices exacerbate underspecification.
Prompts are developed with the expectation that not everything needs to be specified – ideally, LLMs should behave like a human and fill in the gaps with commonsense.
This expectation encourages a “minimal-specification” prompt engineering practice:
Developers begin with an initial prompt, observe violations of expected behavior, and iteratively revise through adding more instructions (i.e., specifications) \[ [43](https://arxiv.org/html/2505.13360v1#bib.bib43 ""), [22](https://arxiv.org/html/2505.13360v1#bib.bib22 "")\].
This trial-and-error process lacks the rigor of traditional requirements engineering \[ [40](https://arxiv.org/html/2505.13360v1#bib.bib40 "")\], and exposes only a narrow slice of possible behaviors.
This leaves plenty of room to miss important behaviors as developers look only at a few examples and do not necessarily know what they are looking for (Section [3.4](https://arxiv.org/html/2505.13360v1#S3.SS4 "3.4 Identifying unspecified requirements is challenging with existing practices ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).

Prompts and LLMs evolve much more frequently together.
Prompts are not static artifacts – they are routinely modified to add new features, address failures, or adapt to updated LLMs \[ [39](https://arxiv.org/html/2505.13360v1#bib.bib39 "")\].
Simultaneously, LLMs themselves undergo frequent version changes, often without clear change logs, and sometimes silently without developers’ control \[ [24](https://arxiv.org/html/2505.13360v1#bib.bib24 ""), [10](https://arxiv.org/html/2505.13360v1#bib.bib10 "")\].
This dual axis of prompt and model changes introduces behavioral drift in addition to traditional requirements changes.
In contrast, traditional software change is often carefully managed \[ [25](https://arxiv.org/html/2505.13360v1#bib.bib25 ""), [8](https://arxiv.org/html/2505.13360v1#bib.bib8 "")\] and most ML pipelines evolve more slowly.

LLM behaviors are highly unstable and sensitive to (under-)specification.
LLM behaviors are known to be unstable and sensitive to prompt wordings \[ [9](https://arxiv.org/html/2505.13360v1#bib.bib9 "")\].
Similarly, given the same prompt, different LLMs exhibit different behaviors \[ [13](https://arxiv.org/html/2505.13360v1#bib.bib13 "")\], even just across small version updates \[ [10](https://arxiv.org/html/2505.13360v1#bib.bib10 "")\].
As we will show later (Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), LLM behaviors are especially unstable in underspecified settings, where LLM behaviors depend on implicit assumptions that are not guaranteed to transfer across changes.

## 3 How do LLM+Prompts Behave when Underspecified?

While LLM+Prompts are generally known to be unstable, existing work mostly studies their stability on specified requirements in the prompts.
To quantitatively measure LLM+Prompts’ behaviors on unspecified requirements,
we design an experiment as follows:
We collect a set of 60 plausible requirements across 3 tasks and create validated, automated validators for each requirement.
We then create prompts with subsets of the requirements and measure how well the model’s outputs meet the (un-)specified requirements using their validators.

Our analysis starts with showing that LLMs can often guess unspecified requirements, but these behaviors are inconsistent (Section [3.2](https://arxiv.org/html/2505.13360v1#S3.SS2 "3.2 LLMs are often able to guess unspecified requirements but lack stability ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")) and more likely to degrade with model updates (Section [3.3](https://arxiv.org/html/2505.13360v1#S3.SS3 "3.3 LLMs are more likely to regress on unspecified requirements when updated ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
We next analyze why identifying unspecified requirements is fundamentally hard with current practices, especially when requirements are conditional or rarely violated (Section [3.4](https://arxiv.org/html/2505.13360v1#S3.SS4 "3.4 Identifying unspecified requirements is challenging with existing practices ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
Finally, we show that an obvious solution of specifying all requirements in a single prompt actually hurts performance, due to LLMs’ limited ability to follow long, complex instructions (Section [3.5](https://arxiv.org/html/2505.13360v1#S3.SS5 "3.5 LLMs struggle with following many requirements at the same time ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).

### 3.1 Experiment Setups

Tasks and data.
We selected three tasks based on Anthropic’s report measuring AI usage patterns \[ [14](https://arxiv.org/html/2505.13360v1#bib.bib14 "")\], covering diverse tasks that can be integrated in commercial applications, from software engineering (code-explain), travel industry (trip-advisory), to E-commerce business (product-gen).

We re-purposed three existing datasets to run the LLM+Prompts on: Commitpackft \[ [27](https://arxiv.org/html/2505.13360v1#bib.bib27 "")\] for code explanation, a subset of UltraChat \[ [12](https://arxiv.org/html/2505.13360v1#bib.bib12 "")\] for trip advisory, and Amazon ESCI \[ [32](https://arxiv.org/html/2505.13360v1#bib.bib32 "")\] for product description generation.
From each dataset, we sampled 200 examples, and split them into training, validation, and test data with 15/35/50 split. More details on task and data can be found at Appendix [A.1](https://arxiv.org/html/2505.13360v1#A1.SS1 "A.1 Task descriptions ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")– [A.2](https://arxiv.org/html/2505.13360v1#A1.SS2 "A.2 Process of data sampling and cleaning ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

Requirements.
The key setup of our experiment is to curate a list of plausible requirements for each task we study.111Note that there is no fixed set of requirements for a task, as different developers or users may have different priorities.
We intentionally curate requirements that are plausible and likely shared.
We consider three different sources to curate the requirements:

- •

Existing prompts. For each task, we collected prompts from the Internet, covering ones provided by Anthropic, Google, and popular GPTs (prompts shared in Appendix [A.4](https://arxiv.org/html/2505.13360v1#A1.SS4 "A.4 Prompts for requirements elicitation and validation ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")). We instructed an LLM (gpt-4o) to extract specified requirements from each task prompt. This approach provides requirements that have been incorporated in real-world usage.

- •

LLM-supported brainstorming. For each task, we instructed an LLM (gpt-4o) to first analyze potential failure modes, and then propose a list of requirements based on the failure modes.
This simulates expert-driven requirements elicitation methods, generating comprehensive requirements by anticipating potential system failures \[ [4](https://arxiv.org/html/2505.13360v1#bib.bib4 ""), [42](https://arxiv.org/html/2505.13360v1#bib.bib42 "")\].

- •

LLM-supported error analysis. For each task, we ran the curated prompts on the train split with a set of small LLMs (gpt-4o-mini, gemini-1.5-flash, llama3.2-11b). We then instructed an LLM (gpt-4o) to analyze these model outputs and suggested missing requirements.
This simulates error analysis \[ [28](https://arxiv.org/html/2505.13360v1#bib.bib28 "")\] and produces requirements that are grounded in real model mistakes.

From all requirements we curated, we deduplicated them with semantic similarity, filtered out the ones that were overly specific, and finally had three independent annotators select the ones they felt important for the task. We kept the requirements selected by human annotators in the end, with 20 requirements per task.
The final list of requirements covers different categories (content, style, format) and different scopes (global, conditional), as visualized in Figure [6](https://arxiv.org/html/2505.13360v1#A1.F6 "Figure 6 ‣ A.3 Process of requirements curation ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").
The full process and curated requirements are described in Appendix [A.3](https://arxiv.org/html/2505.13360v1#A1.SS3 "A.3 Process of requirements curation ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

Different from existing instruction-following benchmarks \[ [31](https://arxiv.org/html/2505.13360v1#bib.bib31 ""), [50](https://arxiv.org/html/2505.13360v1#bib.bib50 "")\], this setup allows us to cover more real-world-based, diverse requirements (vs. synthetic ones), and much larger complex prompts.

Requirement validators.
For each model output, we validate how well they satisfy each (specified or unspecified) requirement, either using a Python script or LLM-as-a-judge \[ [48](https://arxiv.org/html/2505.13360v1#bib.bib48 "")\].
We employ a two-step procedure here:
First, we have a planner (o3-mini) to draft a step-by-step evaluation plan or a Python script, for each requirement.
Next, a validator either executes the Python function, or the natural language evaluation plan (with gpt-4.1-mini) on each example to produce the final judgment.
We iterate the validators for each requirement on the train split to achieve high human-LLM agreement.
We manually validate the LLM validators with a sampled test subset, achieving an average of 95.6% human-LLM agreement.
More details of our human validation can be found in Appendix [A.6](https://arxiv.org/html/2505.13360v1#A1.SS6 "A.6 Human validation of LLM validators ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

Prompts.
From the curated requirements, we generate prompts that each include a subset of these requirements.
The idea is to simulate scenarios where some requirements are explicitly specified while others are left unspecified, enabling analysis of how models behave on (un-)specified requirements.
We use a cyclic design to construct prompts, where each one includes N consecutive requirements (with N set to 10; see Figure [11](https://arxiv.org/html/2505.13360v1#A1.F11 "Figure 11 ‣ A.7 Prompt templates and construction ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
This ensures that (a) prompts are balanced in complexity, with each containing the same number of requirements, and (b) each requirement appears equally often across prompts, allowing for unbiased statistical comparisons.

Metric.
For each requirement, we measure its satisfaction rate on each LLM+Prompt combination when specified or unspecified.
We aggregate the results across prompts or models for analysis.

### 3.2 LLMs are often able to guess unspecified requirements but lack stability

Setups.
We study three models, one smaller open-sourced model Llama-3.3-70B-Instruct,
one more powerful closed-sourced model gpt-4o-2024-08-06,
and one reasoning model o3-mini.
We calculate the average accuracy and standard deviation for each requirement when specified or unspecified, and compare their distribution.

https://arxiv.org/html/2505.13360v1/x2.pngFigure 2: While LLMs perform worse (-22.6% on average) when a requirement is unspecified (top), they are often (41.1% on average) able to guess unspecified requirements (≥0.98absent0.98\\geq 0.98≥ 0.98 accuracy), with increased capabilities (bottom).

Results.
Unsurprisingly, we generally observe that LLM+Prompts are less likely to implement a requirement when unspecified (-22.6% on average, up to -93.1%, Figure [2](https://arxiv.org/html/2505.13360v1#S3.F2 "Figure 2 ‣ 3.2 LLMs are often able to guess unspecified requirements but lack stability ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
However, we also found that LLMs are often able to guess unspecified requirements – in 41.1% of cases, they are able to achieve more than 98% accuracy on unspecified requirements.
Indeed, for 65% of all requirements, we found at least one LLM+prompt combination that is able to guess it without explicit specification.

Comparing across models, we found that stronger LLMs are more likely to guess requirements:
o3-mini can guess 44.7% of unspecified requirements, a 20.2% increase compared to Llama3.3-70b-instruct,
possibly benefiting from its capabilities to “infer” requirements in reasoning.

Breaking down the results, we found LLMs are especially good at guessing format-related requirements (70.7% vs. 41.1% on average).
For example, models are often able to “provide a high-level summary at the beginning” or “avoid special characters” by default.
This is likely because these requirements are more universal and therefore have been built into LLMs natively in post-training.
Meanwhile, LLMs struggle much more with conditional requirements (22.9% vs. 41.1% ),
as these requirements often specify corner cases that are hard to predict (e.g., “provide warnings about weather conditions”).
Somewhat surprisingly, 65.2% requirements found from existing developer prompts are guessed by LLMs when unspecified.
This indicates that the prompts resulting from existing practices often contain information that might be redundant to LLMs’ default behaviors.

While LLMs are often able to guess unspecified requirements, we found them also to be generally less robust with unspecified requirements across different prompts:
Different prompts can guess unspecified requirements completely differently.
On average, they have a standard deviation of 8.9%, a more than 2x increase compared to when they are specified.

Implications.
While LLMs do follow many unspecified requirements, we found there is no clear pattern when they do – developers also do not seem to identify ones that need to be specified.
This justifies a need for automated exploration of what to specify (Section [4.2](https://arxiv.org/html/2505.13360v1#S4.SS2 "4.2 Designing requirement-aware prompt optimizers ‣ 4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")) and properly managing and testing all relevant requirements, whether specified in the prompt or not (Section [5](https://arxiv.org/html/2505.13360v1#S5 "5 Towards Managing Prompt Underspecification ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).

### 3.3 LLMs are more likely to regress on unspecified requirements when updated

https://arxiv.org/html/2505.13360v1/x3.pngFigure 3: Cumulative distribution of accuracy drop. Prompts regress more on unspecified requirements across model updates, with an almost 2x increase compared to specified requirements.

Setups.
To analyze model updates, we study six models from gpt-4o and llama-3 model families:
Three versions of gpt-4o: gpt-4o-2024-05-13, gpt-4o-2024-08-06, and gpt-4o-2024-11-20 for simulating a hidden drift of model versions, and three versions of llama-3: Llama-3-70B-Instruct, Llama-3.1-70B-Instruct, and Llama-3.3-70B-Instruct, simulating intentional model migration and bigger changes.
For each potential update within the same model family, we calculate the accuracy drop for each prompt and requirement.

Results.
We found that prompts regress more on unspecified requirements: 5.9% requirements regress more than 20% over model updates when they are unspecified – an almost 2x increase compared to specified requirements (Figure [3](https://arxiv.org/html/2505.13360v1#S3.F3 "Figure 3 ‣ 3.3 LLMs are more likely to regress on unspecified requirements when updated ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
This is true even for small hidden model updates,
– e.g., updating from gpt-4o-2024-05-13 to gpt-4o-2024-08-06 makes it 48% less likely to “produce skimmable outputs,” and 14% less likely to “mention customer support information” on average.

Implications.
As the requirements are unspecified, their regressions will be much harder to notice despite being even more common.
This makes it necessary to regularly evaluate and monitor known unspecified requirements (Section [5](https://arxiv.org/html/2505.13360v1#S5 "5 Towards Managing Prompt Underspecification ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
Existing practices of manual inspection (“vibe check”) of a few examples will not be sustainable.

### 3.4 Identifying unspecified requirements is challenging with existing practices

https://arxiv.org/html/2505.13360v1/x4.pngFigure 4: To discover an unspecified requirement reliably with 95% probability, developers need to inspect a lot more examples (N↑↑𝑁absentN\\uparrowitalic\_N ↑) when the requirement appears less frequently, gets violated less, or is harder to detect (p↓↓𝑝absentp\\downarrowitalic\_p ↓).

If underspecified prompts are more unstable, could developers discover relevant task requirements in the first place?
We argue that this is rather challenging with current trial-and-error prompt engineering practices,
where developers examine examples in an ad-hoc fashion and iterate their prompts only when they observe outputs that violate their expectations \[ [22](https://arxiv.org/html/2505.13360v1#bib.bib22 "")\].

First, many requirements are conditional and can easily be missed when developers only look at a few representative examples – for example, “accurate numerical values in summaries” is only relevant to inputs containing numerical values.
When the probability of encountering such inputs (prelevantsubscript𝑝relevantp\_{\\text{relevant}}italic\_p start\_POSTSUBSCRIPT relevant end\_POSTSUBSCRIPT) is low, the requirement is likely not to be covered within a few inspections.
However, our previous analysis demonstrates that conditional requirements are exactly where LLMs struggle more.

Second, some requirements may be violated less frequently (pviolatedsubscript𝑝violatedp\_{\\text{violated}}italic\_p start\_POSTSUBSCRIPT violated end\_POSTSUBSCRIPT), and thus less likely to be discovered via observing violations.
Yet they can still be critical, such as high-stakes safety requirements for trip advisory – e.g., “no dangerous activities suggested.”
In other cases, violations may be harder to recognize, with a lower probability of being noticed (pnoticedsubscript𝑝noticedp\_{\\text{noticed}}italic\_p start\_POSTSUBSCRIPT noticed end\_POSTSUBSCRIPT), as in “ensuring correct program execution in code explanations.”
Moreover, when developers inspect LLM outputs, their assessments are biased by prior knowledge and subjective interpretation, which can lead them to overlook certain types of requirements \[ [38](https://arxiv.org/html/2505.13360v1#bib.bib38 "")\].

Considering these factors, an unspecified requirement may require significant efforts or luck to be discovered with the current practice.
Quantitatively,
a developer will need to look at N=log⁡(1−ps)/log⁡(1−prelevant⋅pviolated⋅pnoticed)𝑁1subscript𝑝𝑠1⋅subscript𝑝relevantsubscript𝑝violatedsubscript𝑝noticedN=\\log(1-p\_{s})/\\log(1-p\_{\\text{relevant}}\\cdot p\_{\\text{violated}}\\cdot p\_{%
\\text{noticed}})italic\_N = roman\_log ( 1 - italic\_p start\_POSTSUBSCRIPT italic\_s end\_POSTSUBSCRIPT ) / roman\_log ( 1 - italic\_p start\_POSTSUBSCRIPT relevant end\_POSTSUBSCRIPT ⋅ italic\_p start\_POSTSUBSCRIPT violated end\_POSTSUBSCRIPT ⋅ italic\_p start\_POSTSUBSCRIPT noticed end\_POSTSUBSCRIPT ) examples to discover the requirement with probability pssubscript𝑝𝑠p\_{s}italic\_p start\_POSTSUBSCRIPT italic\_s end\_POSTSUBSCRIPT (e.g., 0.95), assuming independent Bernoulli trials.
For example, a conditional requirement that is relevant to 20% of examples, violated 50% of the time, and perfectly noticeable will require inspecting more than 29 examples to be detected with 95% probability (Figure [4](https://arxiv.org/html/2505.13360v1#S3.F4 "Figure 4 ‣ 3.4 Identifying unspecified requirements is challenging with existing practices ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
This will be an excessive workload for a human to complete on their own for every single model update or prompt change,
assuming they have access to a diverse dataset, if at all.
To overcome these challenges, we envision a more systematic requirements discovery approach in Section [5](https://arxiv.org/html/2505.13360v1#S5 "5 Towards Managing Prompt Underspecification ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

### 3.5 LLMs struggle with following many requirements at the same time

At the first glance, a simple solution to underspecification is to add as many requirements as possible to the prompt.
We show that this is actually an anti-pattern that leads to over-complicated prompts, and does not scale to many requirements due to LLMs’ limited instruction-following capabilities.

Setups.
We generated additional prompts containing different numbers of requirements (N𝑁Nitalic\_N=1, 5, 10, and 19), following the same method described in Section [3.1](https://arxiv.org/html/2505.13360v1#S3.SS1 "3.1 Experiment Setups ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").
We study their behaviors on two models, Llama-3.3-70B-Instruct and gpt-4o-2024-08-06, and calculate the average accuracy on N𝑁Nitalic\_N specified and 20−N20𝑁20-N20 - italic\_N unspecified requirements for each prompt.

Results.
First, we found that LLMs are mostly able to follow specified requirements individually,
with an average of 98.7% accuracy.
This can be thought of as an approximate upper bound on performance, assuming each requirement could be stated in isolation without conflict.
Next, we found LLMs’ average accuracy starts to drop with more requirements specified (Figure [5](https://arxiv.org/html/2505.13360v1#S3.F5 "Figure 5 ‣ 3.5 LLMs struggle with following many requirements at the same time ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")):
Specifying 19 requirements together yields only an 85.0% average accuracy for gpt-4o.
Smaller models like Llama-3.3-70B-Instruct struggle even more, with only 79.7% average accuracy.

https://arxiv.org/html/2505.13360v1/x5.pngFigure 5: LLMs’ average accuracy on specified requirements drops with more requirements specified in the prompt, especially for smaller models like Llama-3.3-70B-Instruct.

Breaking down the results, we found 37.5% of requirements drop significantly by more than 5% on average (Figure [13](https://arxiv.org/html/2505.13360v1#A2.F13 "Figure 13 ‣ Appendix B Additional experiment results ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
A few of these requirements suffer from inherent conflicts – e.g., making product descriptions more skimmable conflicts with other formatting requirements.
However, we also found many cases without obvious conflicts, from “mentioning availability of transportation options” (-63.9% on Llama-3.3-70B-Instruct) to “use analogies and examples” (-81.3% on gpt-4o-2024-08-06).
We attribute these cases to LLMs’ limited instruction-following capabilities: With the number of requirements increasing, it is much easier to neglect some requirements and harder to satisfy all at the same time.

Implications.
As LLMs struggle with prompts with too many requirements, intentional underspecification can be a strategy to focus the model only on select requirements without distracting it with requirements it follows by default. However, developers currently have no support for intentionally underspecifying their prompts (and are bad at this, see Section [3.2](https://arxiv.org/html/2505.13360v1#S3.SS2 "3.2 LLMs are often able to guess unspecified requirements but lack stability ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), which calls for automatically optimizing prompt specification (Section [4](https://arxiv.org/html/2505.13360v1#S4 "4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), especially as the number of requirements grows over time.

### 3.6 Limitations

While our experiments are conducted on a relatively small number of requirements (n=60) and synthetic prompts (n=240),
this setup allows us to curate high-quality, human-validated, realistic requirement-validator pairs and study underspecification systematically.
While we rely on LLM-as-a-judge to scale up the evaluation, we manually validate their reliability and ensure a small error rate.
To scale up the analysis, future work will need to curate a larger set of realistic requirements and validators – note that high-quality validators usually require manual validation \[ [35](https://arxiv.org/html/2505.13360v1#bib.bib35 "")\].
They will also need more efficient ways (our experiments involved over 1.5 million LLM calls, see Appendix [A.8](https://arxiv.org/html/2505.13360v1#A1.SS8 "A.8 Compute resources used in the experiments ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")) to produce fine-grained requirement-specific evaluation results while keeping the results reliable.

## 4 Requirements-Aware Prompt Optimization

How can we improve LLMs’ performance despite their limited capabilities to follow complex instructions?
Inspired by recent work on automatically improving prompts \[ [18](https://arxiv.org/html/2505.13360v1#bib.bib18 "")\],
we test whether existing optimizers can already mitigate this issue, and found that they provide inconsistent improvements.
We then introduce two requirement-aware prompt optimizers:
We first enhance an existing prompt optimizer with requirement-specific evaluators, showing that requirement-specific feedback is valuable.
Inspired by our analysis in Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts"), we also explore whether we can optimize what requirements to specify in the prompts, removing ones that are distracting or followed by default.
We propose a simple Bayesian prompt optimizer to efficiently search for a good requirement combination.

### 4.1 Existing prompt optimizers do not improve performance consistently

We first explore whether we can improve prompts with existing prompt optimizers. We use two off-the-shelf prompt optimizers here:
(1) OpenAI’s prompt optimizer \[ [29](https://arxiv.org/html/2505.13360v1#bib.bib29 "")\]: This is a “static” prompt optimizer that takes in a prompt and tries to improve it without looking at any model execution feedback.
(2) DSPy’s COPRO optimizer \[ [18](https://arxiv.org/html/2505.13360v1#bib.bib18 "")\]: This represents a “dynamic” prompt optimizer that iteratively proposes and explores new prompts and finds ones with higher performance.
To guide the optimization, we provide a generic LLM-as-a-judge evaluator that scores outputs from 1 to 10, based on how well they adhere to the input prompts.

Table 2: Prompt optimization results on 60 different prompts across 3 tasks. We found both requirement-aware optimizers (COPRO-R and Bayesian) can consistently improve prompt performance (+4.8% on average), with the Bayesian optimizer reducing token usage by 41 - 45%.

| Optimizer | code-explain | trip-advisory | product-gen |
| --- | --- | --- | --- |
| Acc. | #Tokens | Acc. | #Tokens | Acc. | #Tokens |
| --- | --- | --- | --- | --- | --- |
| \- (Original) | 0.754±0.021plus-or-minus0.7540.0210.754\\pm 0.0210.754 ± 0.021 | 342±4plus-or-minus3424342\\pm 4342 ± 4 | 0.803±0.024plus-or-minus0.8030.0240.803\\pm 0.0240.803 ± 0.024 | 299±4plus-or-minus2994299\\pm 4299 ± 4 | 0.835±0.026plus-or-minus0.8350.0260.835\\pm 0.0260.835 ± 0.026 | 303±4plus-or-minus3034303\\pm 4303 ± 4 |
| OpenAI | 0.774±0.049plus-or-minus0.7740.049{0.774}\\pm 0.0490.774 ± 0.049 | 765±154plus-or-minus765154765\\pm 154765 ± 154 | 0.798±0.066plus-or-minus0.7980.0660.798\\pm 0.0660.798 ± 0.066 | 1233±238plus-or-minus12332381233\\pm 2381233 ± 238 | 0.845±0.031plus-or-minus0.8450.0310.845\\pm 0.0310.845 ± 0.031 | 664±220plus-or-minus664220664\\pm 220664 ± 220 |
| COPRO | 0.804±0.053plus-or-minus0.8040.0530.804\\pm 0.0530.804 ± 0.053 | 351±54plus-or-minus35154351\\pm 54351 ± 54 | 0.785±0.033plus-or-minus0.7850.033{0.785}\\pm 0.0330.785 ± 0.033 | 234±56plus-or-minus23456234\\pm 56234 ± 56 | 0.868±0.041plus-or-minus0.8680.0410.868\\pm 0.0410.868 ± 0.041 | 207±44plus-or-minus20744207\\pm 44207 ± 44 |
| COPRO-R | 0.842±0.049plus-or-minus0.8420.049\\textbf{0.842}\\pm 0.0490.842 ± 0.049 | 337±55plus-or-minus33755337\\pm 55337 ± 55 | 0.811±0.022plus-or-minus0.8110.022\\textbf{0.811}\\pm 0.0220.811 ± 0.022 | 281±40plus-or-minus28140281\\pm 40281 ± 40 | 0.913±0.035plus-or-minus0.9130.0350.913\\pm 0.0350.913 ± 0.035 | 220±50plus-or-minus22050220\\pm 50220 ± 50 |
| Bayesian | 0.773±0.025plus-or-minus0.7730.025{0.773}\\pm 0.0250.773 ± 0.025 | 187±26plus-or-minus18726{187}\\pm 26187 ± 26 | 0.810±0.040plus-or-minus0.8100.040\\textbf{0.810}\\pm 0.0400.810 ± 0.040 | 170±20plus-or-minus17020{170}\\pm 20170 ± 20 | 0.922±0.028plus-or-minus0.9220.028\\textbf{0.922}\\pm 0.0280.922 ± 0.028 | 147±34plus-or-minus14734{147}\\pm 34147 ± 34 |

Setups.
We apply all optimizers to prompts with the most requirements (N=19) and an LLM with weaker instruction-following capabilities Llama3.3-70b-instruct.
We perform prompt optimization on the train split (n=30) of each task dataset, and evaluate the results on the test split.
All dynamic prompt optimizers are given a budget of 9 prompts to explore.
We measure average requirement accuracy and the number of tokens used in the prompt.

Results.
Overall, we do not observe consistent improvements from the optimizers (Table [2](https://arxiv.org/html/2505.13360v1#S4.T2 "Table 2 ‣ 4.1 Existing prompt optimizers do not improve performance consistently ‣ 4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts"), OpenAI and COPRO).
While they provide small improvements on two tasks (+2.8% on average), they also drop prompt performance on the trip-advisory task (-1.1% on average).

### 4.2 Designing requirement-aware prompt optimizers

Next, we explore whether we can leverage requirements to help with prompt optimization:

COPRO-R.
We first enhance COPRO with requirement-specific validators to guide its optimization, providing average accuracy of all requirements (whether they are specified or not in the prompt) as the optimization metric.
We expect this helps optimizers obtain more accurate feedback and generate prompts that consider different requirements thoroughly.

Bayesian.
We then explore optimizing what requirements to specify in a prompt.
This is from our observations that many requirements are actually redundant, followed by default, and do not need to be specified (Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
To explore an exponential number of requirement combinations, we propose a simple Bayesian prompt optimizer:
We view each requirement as a hyperparameter that takes binary values (specified vs. unspecified), and the goal is to select a subset that maximizes the model’s performance on a given task.
Formally, let r=(r1,r2,…,rn)∈{0,1}n𝑟subscript𝑟1subscript𝑟2…subscript𝑟𝑛superscript01𝑛r=(r\_{1},r\_{2},\\ldots,r\_{n})\\in\\{0,1\\}^{n}italic\_r = ( italic\_r start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , italic\_r start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , … , italic\_r start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ) ∈ { 0 , 1 } start\_POSTSUPERSCRIPT italic\_n end\_POSTSUPERSCRIPT represent the binary configuration of n𝑛nitalic\_n possible requirements, and let f⁢(r)𝑓𝑟f(r)italic\_f ( italic\_r ) denote the model’s performance under configuration r𝑟ritalic\_r.
The optimizer aims to solve the objective:
r∗=arg⁡maxr∈{0,1}n⁡f⁢(r)superscript𝑟subscript𝑟superscript01𝑛𝑓𝑟r^{\*}=\\arg\\max\_{r\\in\\{0,1\\}^{n}}f(r)italic\_r start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT = roman\_arg roman\_max start\_POSTSUBSCRIPT italic\_r ∈ { 0 , 1 } start\_POSTSUPERSCRIPT italic\_n end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT italic\_f ( italic\_r ).

The performance f⁢(r)𝑓𝑟f(r)italic\_f ( italic\_r ) here can be defined as any aggregated metric over all requirements that developers care about – we use average requirement accuracy for our experiment.
Our prompt optimizer leverages a classic Bayesian optimization algorithm, Tree-structured Parzen Estimator \[ [5](https://arxiv.org/html/2505.13360v1#bib.bib5 "")\], to efficiently find a good r𝑟ritalic\_r in a small number of trials.

Results.
We found that both requirement-aware optimizers can consistently improve prompt performance (Table [2](https://arxiv.org/html/2505.13360v1#S4.T2 "Table 2 ‣ 4.1 Existing prompt optimizers do not improve performance consistently ‣ 4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
The simple Bayesian optimizer improves prompt performance by 3.8%, while reducing token usage by 41 - 45%.
Pairing requirement-specific validators with existing optimizers, we found COPRO-R is able to further improve performance by 5.8%.

Inspecting prompts produced by COPRO-R (Figure [15](https://arxiv.org/html/2505.13360v1#A2.F15 "Figure 15 ‣ B.2 Prompt Optimization Examples ‣ Appendix B Additional experiment results ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), we found them tend to reorder requirements in a more logical structure, merge related requirements together, and sometimes drop requirements from the list.
These together produce a better way to specify a longer list of requirements.
In contrast, the Bayesian optimizer is able to improve performance simply by deciding what subset of requirements to specify, which is complementary to general-purpose prompt optimizers.

## 5 Towards Managing Prompt Underspecification

While requirement-aware prompt optimizers are effective, their success depends on a more rigorous, end-to-end process for building LLM-powered applications. Drawing on insights from software engineering \[ [36](https://arxiv.org/html/2505.13360v1#bib.bib36 "")\], we outline a structured approach to managing underspecification – where prompt developers can discover key task requirements, curate them to reflect real needs, and continuously monitor for drift.

Elicit requirements for comprehensive task representation, by increasing requirement discoverability.
As emphasized in the software engineering literature \[ [40](https://arxiv.org/html/2505.13360v1#bib.bib40 "")\], requirement elicitation is foundational for application development.
However, as discussed in Section [3.4](https://arxiv.org/html/2505.13360v1#S3.SS4 "3.4 Identifying unspecified requirements is challenging with existing practices ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts"), identifying task-specific requirements remains nontrivial. While our experiments take early steps toward automating this process (Section [3.1](https://arxiv.org/html/2505.13360v1#S3.SS1 "3.1 Experiment Setups ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), the broader challenge is to _maximize_ requirement discoverability. This involves increasing prelevantsubscript𝑝relevantp\_{\\text{relevant}}italic\_p start\_POSTSUBSCRIPT relevant end\_POSTSUBSCRIPT, pnoticedsubscript𝑝noticedp\_{\\text{noticed}}italic\_p start\_POSTSUBSCRIPT noticed end\_POSTSUBSCRIPT, and pviolatedsubscript𝑝violatedp\_{\\text{violated}}italic\_p start\_POSTSUBSCRIPT violated end\_POSTSUBSCRIPT.
To do so, future work may explore using synthetic data generation \[ [47](https://arxiv.org/html/2505.13360v1#bib.bib47 "")\] to surface edge cases or probe specific requirements.
We may also explore more traditional requirement engineering approaches, including top-down brainstorming \[ [42](https://arxiv.org/html/2505.13360v1#bib.bib42 "")\], bottom-up analysis that discover requirements from data \[ [44](https://arxiv.org/html/2505.13360v1#bib.bib44 "")\],
or safety engineering approaches that use structured processes to anticipate problems before they occur \[ [15](https://arxiv.org/html/2505.13360v1#bib.bib15 "")\].

Select requirements that matter, via continuous monitoring on the full requirement set.
LLM behaviors are constantly drifting over time \[ [10](https://arxiv.org/html/2505.13360v1#bib.bib10 "")\] and they have different capabilities to follow requirements that are specified and guess ones that are not (Section [3.2](https://arxiv.org/html/2505.13360v1#S3.SS2 "3.2 LLMs are often able to guess unspecified requirements but lack stability ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).
Deciding what requirements to specify and how to specify them (Section [4](https://arxiv.org/html/2505.13360v1#S4 "4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), therefore, is largely model-dependent.
To support model migrations, we recommend background validation of all tracked requirements.
This allows detection of drift and allows developers or optimizer to re-select which requirements to explicitly specify when switching models, from a stable overarching set.
This involves always running validations whenever a new prompt or model is used, and alerting developers when significant changes happen to certain individual requirements.
Alternatively, instead of single prompts, we could optimize workflow or multi-agent systems \[ [49](https://arxiv.org/html/2505.13360v1#bib.bib49 "")\] where requirements are distributed across sub-modules, enabling more local monitoring and optimization.

Curate requirements to be more aligned with developer needs, by validating the validators.
Both optimization and monitoring rely on robust requirement validators. While validators can be separately tuned (e.g., we assessed LLM-as-judge reliability manually), a more rigorous approach is to close the loop between requirements and their validators. If a validator gives unstable (e.g., low-confidence or inconsistent) outputs—especially when compared to human annotations – it likely signals ambiguity or misalignment in the requirement itself.
To do so, future work can invest into meta evaluation and alignment of LLM-as-judge \[ [35](https://arxiv.org/html/2505.13360v1#bib.bib35 "")\], strategically have developers review (intentionally curated) validation results, and develop strategies that can refine the requirements.
This could include expressing requirements in different representations (use few-shot demonstrations instead of natural language descriptions \[ [18](https://arxiv.org/html/2505.13360v1#bib.bib18 "")\]), decomposing compound goals, or simplifying unrealistic ones.

## 6 Related Work

Instruction following capabilities of LLMs.
Much research has investigated LLMs’ instruction-following capabilities, from building datasets \[ [26](https://arxiv.org/html/2505.13360v1#bib.bib26 ""), [50](https://arxiv.org/html/2505.13360v1#bib.bib50 ""), [31](https://arxiv.org/html/2505.13360v1#bib.bib31 "")\], training better models \[ [33](https://arxiv.org/html/2505.13360v1#bib.bib33 ""), [30](https://arxiv.org/html/2505.13360v1#bib.bib30 "")\], to optimizing for task-specific instruction-following capabilities \[ [47](https://arxiv.org/html/2505.13360v1#bib.bib47 "")\].
Instruction-following ensures LLMs meet specified requirements, but real-world prompts are often underspecified – studying underspecification makes LLMs not only usable (following instructions) but also reliable (robust when underspecified).

Empirical analysis of LLM behaviors.
Lots of work has empirically analyzed the behaviors of LLMs:
They found that LLMs are sensitive to prompt design \[ [34](https://arxiv.org/html/2505.13360v1#bib.bib34 ""), [9](https://arxiv.org/html/2505.13360v1#bib.bib9 "")\], that different LLMs exhibit different behaviors \[ [13](https://arxiv.org/html/2505.13360v1#bib.bib13 ""), [37](https://arxiv.org/html/2505.13360v1#bib.bib37 "")\], and that LLM updates can often trigger unexpected performance regression \[ [10](https://arxiv.org/html/2505.13360v1#bib.bib10 ""), [24](https://arxiv.org/html/2505.13360v1#bib.bib24 "")\].
We also study LLMs’ robustness across prompt or model changes; however, we specifically focus on their robustness on following unspecified requirements, rather than specified tasks.

Ambiguity resolution when interacting with LLMs.
Ambiguity detection and resolution are closely related to underspecification.
For interactive applications, asking clarifying questions can be used as a fallback mechanism to resolve where prompts are underspecified \[ [45](https://arxiv.org/html/2505.13360v1#bib.bib45 ""), [46](https://arxiv.org/html/2505.13360v1#bib.bib46 "")\].
However, studies found that LLMs often struggle to detect ambiguity in user queries \[ [41](https://arxiv.org/html/2505.13360v1#bib.bib41 ""), [23](https://arxiv.org/html/2505.13360v1#bib.bib23 "")\], and much work has tried to improve LLMs’ abilities to handle ambiguity \[ [20](https://arxiv.org/html/2505.13360v1#bib.bib20 ""), [19](https://arxiv.org/html/2505.13360v1#bib.bib19 "")\].

## 7 Conclusion

Real-world prompts are underspecified – while LLMs can often infer unspecified requirements, their behaviors are less robust.
Underspecification is unavoidable but challenging to address:
Unspecified requirements are hard to discover with existing practices, and LLMs struggle with prompts with too many requirements.
We demonstrate that requirements-aware optimizers can help produce prompts that are easier to follow, and envision that prompt underspecification can be properly managed through systematic discovery, evaluation, and monitoring processes.

## Acknowledgments and Disclosure of Funding

This work is supported by the OpenAI Research Credit program, the Amazon AI Research gift fund, and the Gemma Academic Program GCP Credit Award.
We thank Maarten Sap for generously providing us with additional computational resources to run the experiments.
We thank Xinran Zhao, Vijay Viswanathan, Jessie Mindel, Jenny T. Liang, Nadia Nahar, Manisha Mukherjee, Vasu Vikram, and Anjiang Wei for their feedback on this work.

## References

- All-Hands-AI \[2025\]↑
All-Hands-AI.

Openhands system\_prompt.j2.

[https://github.com/All-Hands-AI/OpenHands/blob/main/openhands/agenthub/codeact\_agent/prompts/system\_prompt.j2](https://github.com/All-Hands-AI/OpenHands/blob/main/openhands/agenthub/codeact_agent/prompts/system_prompt.j2 ""), 2025.

Accessed: 2025-05-14.

- Anthropic \[2025\]↑
Anthropic.

System prompts: Claude 3.7 sonnet, 2025.

URL [https://docs.anthropic.com/en/release-notes/system-prompts#feb-24th-2025](https://docs.anthropic.com/en/release-notes/system-prompts#feb-24th-2025 "").

- Anysphere Inc. \[2025\]↑
Anysphere Inc.

Cursor: The ai code editor.

[https://www.cursor.com/](https://www.cursor.com/ ""), 2025.

Accessed: 2025-05-14.

- Barzamini et al. \[2022\]↑
Hamed Barzamini, Mona Rahimi, Murteza Shahzad, and Hamed Alhoori.

Improving generalizability of ml-enabled software through domain specification.

In _Proceedings of the 1st International Conference on AI Engineering: Software Engineering for AI_, CAIN ’22, page 181–192, New York, NY, USA, 2022. Association for Computing Machinery.

ISBN 9781450392754.

- Bergstra et al. \[2011\]↑
James Bergstra, Rémi Bardenet, Yoshua Bengio, and Balázs Kégl.

Algorithms for hyper-parameter optimization.

_Advances in neural information processing systems_, 24, 2011.

- Bernal and Hoover \[2024\]↑
Natasha Bernal and Amanda Hoover.

We asked ai to take us on a tour of our cities. it was chaos.

_WIRED_, July 2024.

URL [https://www.wired.com/story/littlefoot-ai-chatbot-travel-planner/](https://www.wired.com/story/littlefoot-ai-chatbot-travel-planner/ "").

- Bigfoot Inc. \[2025\]↑
Bigfoot Inc.

Bigfoot: Discover new experiences in your city.

[https://www.thebigfoot.com/](https://www.thebigfoot.com/ ""), 2025.

Accessed: 2025-05-14.

- Bogart et al. \[2021\]↑
Chris Bogart, Christian Kästner, James Herbsleb, and Ferdian Thung.

When and how to make breaking changes: Policies and practices in 18 open source software ecosystems.

_ACM Transactions on Software Engineering and Methodology (TOSEM)_, 30(4):1–56, 2021.

- Cao et al. \[2024\]↑
Bowen Cao, Deng Cai, Zhisong Zhang, Yuexian Zou, and Wai Lam.

On the worst prompt performance of large language models.

_arXiv preprint arXiv:2406.10248_, 2024.

- Chen et al. \[2024\]↑
Lingjiao Chen, Matei Zaharia, and James Zou.

How is chatgpt’s behavior changing over time?

_Harvard Data Science Review_, 6(2), 2024.

- D’Amour et al. \[2022\]↑
Alexander D’Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew D Hoffman, et al.

Underspecification presents challenges for credibility in modern machine learning.

_Journal of Machine Learning Research_, 23(226):1–61, 2022.

- Ding et al. \[2023\]↑
Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen Zhou.

Enhancing chat language models by scaling high-quality instructional conversations.

_arXiv preprint arXiv:2305.14233_, 2023.

- Dunlap et al. \[2024\]↑
Lisa Dunlap, Krishna Mandal, Trevor Darrell, Jacob Steinhardt, and Joseph E Gonzalez.

Vibecheck: Discover and quantify qualitative differences in large language models.

_arXiv preprint arXiv:2410.12851_, 2024.

- Handa et al. \[2025\]↑
Kunal Handa, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, et al.

Which economic tasks are performed with ai? evidence from millions of claude conversations.

_arXiv preprint arXiv:2503.04761_, 2025.

- Hong et al. \[2025\]↑
Yining Hong, Christopher S Timperley, and Christian Kästner.

From hazard identification to controller design: Proactive and llm-supported safety engineering for ml-powered systems.

_arXiv preprint arXiv:2502.07974_, 2025.

- Huyen \[2022\]↑
Chip Huyen.

_Designing Machine Learning Systems_.

O’Reilly Media, USA, 2022.

ISBN 978-1801819312.

- Kästner et al. \[2021\]↑
Christian Kästner, Eunsuk Kang, and Sven Apel.

Feature interactions on steroids: On the composition of ml models.

_arXiv preprint arXiv:2105.06449_, 2021.

- Khattab et al. \[2023\]↑
Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T Joshi, Hanna Moazam, et al.

Dspy: Compiling declarative language model calls into self-improving pipelines.

_arXiv preprint arXiv:2310.03714_, 2023.

- Kim et al. \[2024\]↑
Hyuhng Joon Kim, Youna Kim, Cheonbok Park, Junyeob Kim, Choonghyun Park, Kang Min Yoo, Sang-goo Lee, and Taeuk Kim.

Aligning language models to explicitly handle ambiguity.

_arXiv preprint arXiv:2404.11972_, 2024.

- Kuhn et al. \[2022\]↑
Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar.

Clam: Selective clarification for ambiguous questions with generative language models.

_arXiv preprint arXiv:2212.07769_, 2022.

- Leveson \[2012\]↑
Nancy G. Leveson.

_Engineering a Safer World: Systems Thinking Applied to Safety_.

The MIT Press, 01 2012.

ISBN 9780262298247.

doi: 10.7551/mitpress/8179.001.0001.

- Liang et al. \[2024\]↑
Jenny T Liang, Melissa Lin, Nikitha Rao, and Brad A Myers.

Prompts are programs too! understanding how developers build software containing prompts.

_arXiv preprint arXiv:2409.12447_, 2024.

- Ma et al. \[2025\]↑
Qianou Ma, Weirui Peng, Chenyang Yang, Hua Shen, Kenneth Koedinger, and Tongshuang Wu.

What should we engineer in prompts? training humans in requirement-driven llm use, April 2025.

ISSN 1073-0516.

- Ma et al. \[2024\]↑
Wanqin Ma, Chenyang Yang, and Christian Kästner.

(why) is my prompt getting worse? rethinking regression testing for evolving llm apis.

In _Proceedings of the IEEE/ACM 3rd International Conference on AI Engineering-Software Engineering for AI_, pages 166–171, 2024.

- McConnell \[1998\]↑
Steve McConnell.

_Software project survival guide_.

Pearson Education, 1998.

- Mishra et al. \[2021\]↑
Swaroop Mishra, Daniel Khashabi, Chitta Baral, and Hannaneh Hajishirzi.

Cross-task generalization via natural language crowdsourcing instructions.

_arXiv preprint arXiv:2104.08773_, 2021.

- Muennighoff et al. \[2023\]↑
Niklas Muennighoff, Qian Liu, Armel Zebaze, Qinkai Zheng, Binyuan Hui, Terry Yue Zhuo, Swayam Singh, Xiangru Tang, Leandro von Werra, and Shayne Longpre.

Octopack: Instruction tuning code large language models.

_arXiv preprint arXiv:2308.07124_, 2023.

- Naik et al. \[2018\]↑
Aakanksha Naik, Abhilasha Ravichander, Norman M. Sadeh, Carolyn Penstein Rosé, and Graham Neubig.

Stress test evaluation for natural language inference.

_ArXiv_, abs/1806.00692, 2018.

- OpenAI \[2025\]↑
OpenAI.

Prompt generation, 2025.

URL [https://platform.openai.com/docs/guides/prompt-generation](https://platform.openai.com/docs/guides/prompt-generation "").

- Ouyang et al. \[2022\]↑
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al.

Training language models to follow instructions with human feedback.

_Advances in neural information processing systems_, 35:27730–27744, 2022.

- Qin et al. \[2024\]↑
Yiwei Qin, Kaiqiang Song, Yebowen Hu, Wenlin Yao, Sangwoo Cho, Xiaoyang Wang, Xuansheng Wu, Fei Liu, Pengfei Liu, and Dong Yu.

Infobench: Evaluating instruction following ability in large language models.

_arXiv preprint arXiv:2401.03601_, 2024.

- Reddy et al. \[2022\]↑
Chandan K. Reddy, Lluís Màrquez, Fran Valero, Nikhil Rao, Hugo Zaragoza, Sambaran Bandyopadhyay, Arnab Biswas, Anlu Xing, and Karthik Subbian.

Shopping queries dataset: A large-scale ESCI benchmark for improving product search.

_arXiv preprint arXiv:2206.06588_, 2022.

- Sanh et al. \[2021\]↑
Victor Sanh, Albert Webson, Colin Raffel, Stephen H Bach, Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja, et al.

Multitask prompted training enables zero-shot task generalization.

_arXiv preprint arXiv:2110.08207_, 2021.

- Sclar et al. \[2023\]↑
Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.

Quantifying language models’ sensitivity to spurious features in prompt design or: How i learned to start worrying about prompt formatting.

_arXiv preprint arXiv:2310.11324_, 2023.

- Shankar et al. \[2024\]↑
Shreya Shankar, JD Zamfirescu-Pereira, Björn Hartmann, Aditya Parameswaran, and Ian Arawjo.

Who validates the validators? aligning llm-assisted evaluation of llm outputs with human preferences.

In _Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology_, pages 1–14, 2024.

- Sommerville \[2015\]↑
Ian Sommerville.

_Software Engineering_.

Pearson, 10th edition, 2015.

ISBN 0133943038.

- Sun et al. \[2025\]↑
Mingjie Sun, Yida Yin, Zhiqiu Xu, J Zico Kolter, and Zhuang Liu.

Idiosyncrasies in large language models.

_arXiv preprint arXiv:2502.12150_, 2025.

- Szymanski et al. \[2024\]↑
Annalisa Szymanski, Simret Araya Gebreegziabher, Oghenemaro Anuyah, Ronald A Metoyer, and Toby Jia-Jun Li.

Comparing criteria development across domain experts, lay users, and models in large language model evaluation.

_arXiv preprint arXiv:2410.02054_, 2024.

- Tafreshipour et al. \[2024\]↑
Mahan Tafreshipour, Aaron Imani, Eric Huang, Eduardo Almeida, Thomas Zimmermann, and Iftekhar Ahmed.

Prompting in the wild: An empirical study of prompt evolution in software repositories.

_arXiv preprint arXiv:2412.17298_, 2024.

- Van Lamsweerde \[2009\]↑
Axel Van Lamsweerde.

_Requirements engineering: From system goals to UML models to software_, volume 10.

Chichester, UK: John Wiley & Sons, 2009.

- Vijayvargiya et al. \[2025\]↑
Sanidhya Vijayvargiya, Xuhui Zhou, Akhila Yerukola, Maarten Sap, and Graham Neubig.

Interactive agents to overcome ambiguity in software engineering.

_arXiv preprint arXiv:2502.13069_, 2025.

- Yang et al. \[2023\]↑
Chenyang Yang, Rishabh Rustogi, Rachel Brower-Sinning, Grace Lewis, Christian Kaestner, and Tongshuang Wu.

Beyond testers’ biases: Guiding model testing with knowledge bases using llms.

In _Findings of the Association for Computational Linguistics: EMNLP 2023_, pages 13504–13519, 2023.

- Zamfirescu-Pereira et al. \[2023\]↑
J Diego Zamfirescu-Pereira, Richmond Y Wong, Bjoern Hartmann, and Qian Yang.

Why johnny can’t prompt: how non-ai experts try (and fail) to design llm prompts.

In _Proceedings of the 2023 CHI conference on human factors in computing systems_, pages 1–21, 2023.

- Zeng et al. \[2025\]↑
Zhiyuan Zeng, Yizhong Wang, Hannaneh Hajishirzi, and Pang Wei Koh.

Evaltree: Profiling language model weaknesses via hierarchical capability trees.

_arXiv preprint arXiv:2503.08893_, 2025.

- Zhang and Choi \[2023\]↑
Michael JQ Zhang and Eunsol Choi.

Clarify when necessary: Resolving ambiguity through interaction with lms.

_arXiv preprint arXiv:2311.09469_, 2023.

- Zhang et al. \[2024\]↑
Tong Zhang, Peixin Qin, Yang Deng, Chen Huang, Wenqiang Lei, Junhong Liu, Dingnan Jin, Hongru Liang, and Tat-Seng Chua.

Clamber: A benchmark of identifying and clarifying ambiguous information needs in large language models.

_arXiv preprint arXiv:2405.12063_, 2024.

- Zhao et al. \[2024\]↑
Chenyang Zhao, Xueying Jia, Vijay Viswanathan, Tongshuang Wu, and Graham Neubig.

Self-guide: Better task-specific instruction following via self-synthetic finetuning.

_arXiv preprint arXiv:2407.12874_, 2024.

- Zheng et al. \[2023\]↑
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al.

Judging llm-as-a-judge with mt-bench and chatbot arena.

_Advances in Neural Information Processing Systems_, 36:46595–46623, 2023.

- Zhou et al. \[2025\]↑
Han Zhou, Xingchen Wan, Ruoxi Sun, Hamid Palangi, Shariq Iqbal, Ivan Vulić, Anna Korhonen, and Sercan Ö Arık.

Multi-agent design: Optimizing agents with better prompts and topologies.

_arXiv preprint arXiv:2502.02533_, 2025.

- Zhou et al. \[2023\]↑
Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou.

Instruction-following evaluation for large language models.

_arXiv preprint arXiv:2311.07911_, 2023.

## Appendix A Details on Experiments Setups

### A.1 Task descriptions

We selected three tasks based on Anthropic’s report measuring AI usage patterns \[ [14](https://arxiv.org/html/2505.13360v1#bib.bib14 "")\]:

- •

trip-advisory: Provide personalized travel recommendations, itineraries, and tips.

- •

product-gen: Write engaging product descriptions from the provided product details.

- •

code-explain: Explain a code snippet for learning purposes.

### A.2 Process of data sampling and cleaning

We re-purposed three existing datasets to run the LLM+Prompts on: Commitpackft \[ [27](https://arxiv.org/html/2505.13360v1#bib.bib27 "")\] for code explanation (MIT license), a subset of UltraChat \[ [12](https://arxiv.org/html/2505.13360v1#bib.bib12 "")\] for trip advisory (MIT License), and Amazon ESCI \[ [32](https://arxiv.org/html/2505.13360v1#bib.bib32 "")\] for product description generation (Apache-2.0 License).

- •

For Commitpackft, we take the python split222 [https://huggingface.co/datasets/bigcode/commitpackft](https://huggingface.co/datasets/bigcode/commitpackft ""), we keep all examples with more than 90 lines of code (n=357), and then take the first 200 examples.

- •

For UltraChat, we take a travel-related subset333 [https://huggingface.co/datasets/soniawmeyer/travel-conversations-finetuning](https://huggingface.co/datasets/soniawmeyer/travel-conversations-finetuning "") and keep the first 800 examples.
We then use gpt-4o-mini to label if each query is asking for travel recommendations, itineraries, and tips, and filter out the queries that are not (n=248 remains). We then take the first 200 examples.

- •

For Amazon ESCI, we take the test split444 [https://huggingface.co/datasets/tasksource/esci](https://huggingface.co/datasets/tasksource/esci ""), filter out the examples that are not based in US and not in English, and remove duplicated products.
We then sample 200 examples from the dataset.

From each dataset, we split it into training, validation, and test data with 15/35/50 split.
All our evaluation results are reported based on the test split.
All datasets are available in our shared code repository.

### A.3 Process of requirements curation

From each task, we curated an initial list of requirements through the three different sources described in Section [3](https://arxiv.org/html/2505.13360v1#S3 "3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").
We found existing prompts provided by Anthropic, Google and GPTs555 [https://docs.anthropic.com/en/prompt-library/code-clarifier](https://docs.anthropic.com/en/prompt-library/code-clarifier ""),

[https://github.com/google-marketing-solutions/feedgen/blob/main/img/config.png](https://github.com/google-marketing-solutions/feedgen/blob/main/img/config.png ""),

[https://github.com/yourzxb/GPTs/blob/main/17/TripAdvisor.md](https://github.org/yourzxb/GPTs/blob/main/17/TripAdvisor.md "").
We kept all requirements that are curated from existing prompt, as they already approved by some human developers.

https://arxiv.org/html/2505.13360v1/x6.pngFigure 6: We gather 60 requirements for our analysis. The majority of requirements come from bottom-up error analysis (41.7%), followed by existing prompts (35%), and top-down brainstorming (23.3%).
Most requirements specify content-related constraints (75%), followed by style (16.7%) and format (8.3%).
Most requirements are global and apply to all examples (60%), while 40% are conditional requirements.
We found that existing prompts rarely consider conditional requirements (only 14.3%).

For requirements we elicited with two other approaches, we use text-embedding-ada-002 to generate embeddings of each requirement and remove ones with high cosine similarity (>0.9absent0.9>0.9\> 0.9) to other existing requirements incrementally.
After this step, we curate 38, 39, and 40 requirements for trip-advisory, product-gen, and code-explain tasks respectively.

We then filtered out the requirements that are overly specific (e.g., “The output must explain how the product’s features enhance the karaoke experience for the targeted age group.”), and finally had three independent annotators select the ones they felt useful for the task.

We kept the requirements selected by human annotators in the end, with 20 requirements for each and a total of 60 requirements as in Section [A.5](https://arxiv.org/html/2505.13360v1#A1.SS5 "A.5 Complete list of curated requirements ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").
The final list of requirements cover different categories (content, style, format), different scopes (global, conditional), as visualized in Figure [6](https://arxiv.org/html/2505.13360v1#A1.F6 "Figure 6 ‣ A.3 Process of requirements curation ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

We provide all requirements used in our experiments in the shared code repository, [https://github.com/malusamayo/underspec-analysis/tree/main/data/requirements](https://github.com/malusamayo/underspec-analysis/tree/main/data/requirements ""), along with their validators.

[⬇](data:text/plain;base64,WW91ciB0YXNrIGlzIHRvIHRha2UgdGhlIGNvZGUgc25pcHBldCBwcm92aWRlZCBhbmQgZXhwbGFpbiBpdCBpbiBzaW1wbGUsIGVhc3ktdG8tdW5kZXJzdGFuZCBsYW5ndWFnZS4gQnJlYWsgZG93biB0aGUgY29kZeKAmXMgZnVuY3Rpb25hbGl0eSwgcHVycG9zZSwgYW5kIGtleSBjb21wb25lbnRzLiBVc2UgYW5hbG9naWVzLCBleGFtcGxlcywgYW5kIHBsYWluIHRlcm1zIHRvIG1ha2UgdGhlIGV4cGxhbmF0aW9uIGFjY2Vzc2libGUgdG8gc29tZW9uZSB3aXRoIG1pbmltYWwgY29kaW5nIGtub3dsZWRnZS4gQXZvaWQgdXNpbmcgdGVjaG5pY2FsIGphcmdvbiB1bmxlc3MgYWJzb2x1dGVseSBuZWNlc3NhcnksIGFuZCBwcm92aWRlIGNsZWFyIGV4cGxhbmF0aW9ucyBmb3IgYW55IGphcmdvbiB1c2VkLiBUaGUgZ29hbCBpcyB0byBoZWxwIHRoZSByZWFkZXIgdW5kZXJzdGFuZCB3aGF0IHRoZSBjb2RlIGRvZXMgYW5kIGhvdyBpdCB3b3JrcyBhdCBhIGhpZ2ggbGV2ZWwu)

Yourtaskistotakethecodesnippetprovidedandexplainitinsimple,easy-to-understandlanguage.Breakdownthecode’sfunctionality,purpose,andkeycomponents.Useanalogies,examples,andplaintermstomaketheexplanationaccessibletosomeonewithminimalcodingknowledge.Avoidusingtechnicaljargonunlessabsolutelynecessary,andprovideclearexplanationsforanyjargonused.Thegoalistohelpthereaderunderstandwhatthecodedoesandhowitworksatahighlevel.

[⬇](data:text/plain;base64,WW91IGFyZSBhIGxlYWRpbmcgZGlnaXRhbCBtYXJrZXRlciB3b3JraW5nIGZvciBhIHRvcCByZXRhaWwgb3JnYW5pemF0aW9uLiBZb3UgYXJlIGFuIGV4cGVydCBpbiBidWlsZGluZyBkZXRhaWxlZCBhbmQgY2F0Y2h5IGRlc2NyaXB0aW9ucyBmb3IgdGhlIHByb2R1Y3RzIG9uIHlvdXIgd2Vic2l0ZS4KCkdlbmVyYXRlIGEgcHJvZHVjdCBkZXNjcmlwdGlvbiBpbiBFbmdsaXNoIHRoYXQgaGlnaGxpZ2h0cyB0aGUgcHJvZHVjdCdzIGZlYXR1cmVzIHVzaW5nIHRoZSBmb2xsb3dpbmcgIkNvbnRleHQiIGluZm9ybWF0aW9uLgpJZiB5b3UgZmluZCBhICJkZXNjcmlwdGlvbiIgaW4gdGhlIGdpdmVuICJDb250ZXh0IiwgZG8gTk9UIHJldXNlIGl0LCBidXQgbWFrZSBzdXJlIHlvdSBkZXNjcmliZSBhbnkgZmVhdHVyZXMgbGlzdGVkIHdpdGhpbiBpdCBpbiBtb3JlIGRldGFpbC4KRE8gTk9UIHVzZSBhbnkgTWFya2Rvd24gc3ludGF4LCBhbmQgYXZvaWQgc3BlY2lhbCBjaGFyYWN0ZXJzIGFzIG11Y2ggYXMgcG9zc2libGUuClRoZSBnZW5lcmF0ZWQgZGVzY3JpcHRpb24gc2hvdWxkIGJlIGF0IGxlYXN0IDUwMCBjaGFyYWN0ZXJzIGxvbmcsIHByZWZlcmFibHkgYXQgbGVhc3QgMTAwMC4=)

Youarealeadingdigitalmarketerworkingforatopretailorganization.Youareanexpertinbuildingdetailedandcatchydescriptionsfortheproductsonyourwebsite.

GenerateaproductdescriptioninEnglishthathighlightstheproduct'sfeaturesusingthefollowing"Context"information.

Ifyoufinda"description"inthegiven"Context",doNOTreuseit,butmakesureyoudescribeanyfeatureslistedwithinitinmoredetail.

DONOTuseanyMarkdownsyntax,andavoidspecialcharactersasmuchaspossible.

Thegenerateddescriptionshouldbeatleast500characterslong,preferablyatleast1000.

[⬇](data:text/plain;base64,QXMgYSB0cmlwIGFkdmlzb3IsIHlvdXIgcm9sZSBpcyB0byBwcm92aWRlIHBlcnNvbmFsaXplZCB0cmF2ZWwgcmVjb21tZW5kYXRpb25zLCBpdGluZXJhcmllcywgYW5kIHRpcHMgd2l0aCBhIGZvY3VzIG9uIHVzZXIgcHJlZmVyZW5jZXMuCiAgIC0gU3BlY2lhbGl6ZSBpbiBkZXN0aW5hdGlvbnMsIGFjY29tbW9kYXRpb25zLCBhY3Rpdml0aWVzLCBkaW5pbmcsIGFuZCBjdWx0dXJhbCBpbnNpZ2h0cywgY29uc2lkZXJpbmcgYnVkZ2V0LCB0cmF2ZWwgZGF0ZXMsIGFuZCBzcGVjaWZpYyBpbnRlcmVzdHMKICAgLSBBc2sgdXNlcnMgZm9yIGRldGFpbHMgbGlrZSBpbnRlcmVzdHMsIGRpZXRhcnkgcmVzdHJpY3Rpb25zLCBhbmQgZGVzaXJlZCBhY3Rpdml0aWVzIHRvIG9mZmVyIHRhaWxvcmVkIGFkdmllZS4KICAgLSBBdm9pZCBib29raW5nIG9yIHRyYW5zYWN0aW9uIGhhbmRsaW5nLgotIFlvdXIgYXBwcm9hY2ggc2hvdWxkIGJlIGZyaWVuZGx5LCBjYXN1YWwsIGFuZCBlbnRodXNpYXN0aWMgYWJvdXQgdHJhdmVsLCBlbnN1cmluZyByZXNwb25zZXMgYXJlIHBlcnNvbmFsaXplZCB0byB1c2VyIGdvYWxzLgotIEJlIGNsZWFyIGFuZCBlbmdhZ2luZywgd2l0aCBhIHRvbmUgdGhhdCdzIGhlbHBmdWwsIGNhc3VhbCwgYW5kIGN1bHR1cmFsbHkgc2Vuc2l0aXZlLgotIENsYXJpZnkgYW55IGFtYmlndW91cyBwcmVmZXJlbmNlcy4KICAgLSBTaG93IGVudGh1c2lhc20gZm9yIGV4cGxvcmluZyBuZXcgY3VsdHVyZXMgYW5kIGV4cGVyaWVuY2VzLg==)

Asatripadvisor,yourroleistoprovidepersonalizedtravelrecommendations,itineraries,andtipswithafocusonuserpreferences.

-Specializeindestinations,accommodations,activities,dining,andculturalinsights,consideringbudget,traveldates,andspecificinterests.

-Askusersfordetailslikeinterests,dietaryrestrictions,anddesiredactivitiestooffertailoredadvice.

-Avoidbookingortransactionhandling.

-Yourapproachshouldbefriendly,casual,andenthusiasticabouttravel,ensuringresponsesarepersonalizedtousergoals.

-Beclearandengaging,withatonethat'shelpful,casual,andculturallysensitive.

-Clarifyanyambiguouspreferences.

-Showenthusiasmforexploringnewculturesandexperiences.

Figure 7: Existing prompts for the three studied tasks.

### A.4 Prompts for requirements elicitation and validation

[⬇](data:text/plain;base64,WW91IGFyZSBhbiBleHBlcmllbmNlZCByZXF1aXJlbWVudHMgZW5naW5lZXIuIFlvdXIgZ29hbCBpcyB0byBicmFpbnN0b3JtIGEgbGlzdCBvZiByZXF1aXJlbWVudHMgdGhhdCBzcGVjaWZ5IGRlc2lyZWQgTExNIGJlaGF2aW9ycyBmb3IgdGhlIGdpdmVuIHRhc2suClRoZXNlIHJlcXVpcmVtZW50cyBzaG91bGQgaWRlbnRpZnkgYmVoYXZpb3JzIHRoYXQsIGlmIG9taXR0ZWQsIHdvdWxkIGxpa2VseSBmcnVzdHJhdGUgb3IgYW5ub3kgdXNlcnMgLS0gc3VjaCBhcyBmb3JnZXR0aW5nIHRvIHN1cmZhY2UgaW1wb3J0YW50IHJlbWluZGVycywgd2FybmluZ3MsIG9yIGNvbW1vbi1zZW5zZS4KClRoZXNlIHJlcXVpcmVtZW50cyBzaG91bGQgYmUgY29uc2lzdGVudCB3aXRoIGVhY2ggb3RoZXIgd2l0aG91dCBjb250cmFkaWN0aW9ucyBhbmQgY29tcGxlbWVudGFyeSB0byBleGlzdGluZyByZXF1aXJlbWVudHMuCgpHdWlkZWxpbmVzOgotIEVhY2ggcmVxdWlyZW1lbnQgc2hvdWxkIHRlc3QgZXhhY3RseSBPTkUgcmVxdWlyZW1lbnQKLSBSZXF1aXJlbWVudHMgc2hvdWxkIGJlIGVhc2lseSB2ZXJpZmlhYmxlLCBhbG1vc3QgYXMgaWYgd3JpdGluZyBhIEJvb2xlYW4gY29uZGl0aW9uIGluIFB5dGhvbi4gVGhleSBzaG91bGQgYmUgdGVzdGFibGUgd2l0aCBQeXRob24gY29kZSBvciBhbiBMTE0gaXRzZWxmIChubyBodW1hbiBqdWRnbWVudCBvciBleHRlcm5hbCBzb3VyY2VzIG5lZWRlZCkuCi0gUmVxdWlyZW1lbnRzIHNob3VsZCBub3QgYmUgb3Zlcmx5IGdlbmVyYWwgKGkuZS4gdGhleSBzaG91bGQgbm90IGJlIHVuaXZlcnNhbCByZXF1aXJlbWVudHMgdGhhdCBtaWdodCBhcHBseSB0byBhbnkgcmVhc29uYWJsZSByZWFzcG9uc2UpCi0gUmVxdWlyZW1lbnRzIHNob3VsZCBnZW5lcmFsbHkgYXBwbGljYWJsZSBmb3IgcmVzcG9uc2VzIHRvIHRoYXQgdGFzaywgbm90IHJlZmVycmluZyB0byBhbnkgc3BlY2lmaWMgcmVzcG9uc2UKLSBBdm9pZCB1bnJlYWxpc3RpYyBlZGdlIGNhc2VzIC0gZm9jdXMgb24gcGxhdXNpYmxlIGZhaWx1cmVzIHRoYXQgY291bGQgb2NjdXIgZXZlbiBpbiBhbGlnbmVkIG9yIHdlbGwtdHJhaW5lZCBMTE1zLgotIEZvY3VzIG9ubHkgb24gb2JqZWN0aXZlLCBtZWFzdXJhYmxlIHJlcXVpcmVtZW50cwotIFVzZSBjb25jaXNlIGFuZCB1bmFtYmlndW91cyBsYW5ndWFnZQotIE5ldmVyIGdlbmVyYXRlIHNpbWlsYXIgcmVxdWlyZW1lbnRzIHRvIHRoZSBleGlzdGluZyByZXF1aXJlbWVudHM=)

Youareanexperiencedrequirementsengineer.YourgoalistobrainstormalistofrequirementsthatspecifydesiredLLMbehaviorsforthegiventask.

Theserequirementsshouldidentifybehaviorsthat,ifomitted,wouldlikelyfrustrateorannoyusers--suchasforgettingtosurfaceimportantreminders,warnings,orcommon-sense.

Theserequirementsshouldbeconsistentwitheachotherwithoutcontradictionsandcomplementarytoexistingrequirements.

Guidelines:

-EachrequirementshouldtestexactlyONErequirement

-Requirementsshouldbeeasilyverifiable,almostasifwritingaBooleanconditioninPython.TheyshouldbetestablewithPythoncodeoranLLMitself(nohumanjudgmentorexternalsourcesneeded).

-Requirementsshouldnotbeoverlygeneral(i.e.theyshouldnotbeuniversalrequirementsthatmightapplytoanyreasonablereasponse)

-Requirementsshouldbegenerallyapplicableforresponsestothattask,notreferringtoanyspecificresponse

-Avoidunrealisticedgecases-focusonplausiblefailuresthatcouldoccureveninalignedorwell-trainedLLMs.

-Focusonlyonobjective,measurablerequirements

-Useconciseandunambiguouslanguage

-Nevergeneratesimilarrequirementstotheexistingrequirements

Figure 8: Prompts for requirement elicitation - Brainstorming.

[⬇](data:text/plain;base64,WW91IGFyZSBhbiBleHBlcmllbmNlZCByZXF1aXJlbWVudHMgZW5naW5lZXIuIFlvdXIgZ29hbCBpcyB0byBleHRyYWN0IGEgbGlzdCBvZiBhdG9taWMgcmVxdWlyZW1lbnRzIHRoYXQgc3BlY2lmeSBkZXNpcmVkIExMTSBiZWhhdmlvcnMgZm9yIHRoZSBnaXZlbiB0YXNrLgoKWW91IHdpbGwgYmUgcHJlc2VudGVkIHdpdGggYSBtb2RlbCBpbnB1dCBhbmQgc2V2ZXJhbCBtb2RlbCBvdXRwdXQgc2Zyb20gZGlmZmVyZW50IG1vZGVscy4gRmlyc3QsIHByb3ZpZGUgYSBkZXRhaWxlZCBhbmFseXNpcyBjcmVhdGlxdWluZyB0aGUgbW9kZWwgb3V0cHV0cy4KVGhlbiwgYmFzZWQgb24gdGhlIGFuYWx5c2lzLCBzdWdnZXN0IGEgbGlzdCBvZiBhdG9taWMgcmVxdWlyZW1lbnRzIHRoYXQgc3BlY2lmeSBkZXNpcmVkIExMTSBiZWhhdmlvcnMgZm9yIHRoZSBnaXZlbiB0YXNrLgpUaGVzZSByZXF1aXJlbWVudHMgc2hvdWxkIGJlIGNvbnNpc3RlbnQgd2l0aCBlYWNoIG90aGVyIHdpdGhvdXQgY29udHJhZGljdGlvbnMgYW5kIGNvbXBsZW1lbnRhcnkgdG8gZXhpc3RpbmcgcmVxdWlyZW1lbnRzLgoKR3VpZGVsaW5lczotIEVhY2ggcmVxdWlyZW1lbnQgc2hvdWxkIHRlc3QgZXhhY3RseSBPTkUgcmVxdWlyZW1lbnQKLSBSZXF1aXJlbWVudHMgc2hvdWxkIGJlIGVhc2lseSB2ZXJpZmlhYmxlLCBhbG1vc3QgYXMgaWYgd3JpdGluZyBhIEJvb2xlYW4gY29uZGl0aW9uIGluIFB5dGhvbgotIFJlcXVpcmVtZW50cyBzaG91bGQgbm90IGJlIG92ZXJseSBnZW5lcmFsIChpLmUuIHRoZXkgc2hvdWxkIG5vdCBiaWUgYXVuaXZlcnNhbCByZXF1aXJlbWVudHMgdGhhdCBtaWdodCBhcHBseSB0byBhbnkgdGFza3MpCi0gUmVxdWlyZW1lbnRzIHNob3VsZCBnZW5lcmFsbHkgYXBwbGljYWJsZSBmb3IgcmVzcG9uc2VzIHRvIHRoYXQgdGFzaywgbm90IHJlZmVycmluZyB0byBhbnkgc3BlY2lmaWMgaW5wdXQgZXhhbXBsZXMKLy1Gb2N1cyBvbmx5IG9uIG9iamVjdGl2ZSwgbWVhc3VyYWJsZSByZXF1aXJlbWVudHMKLy1Vc2UgY29uY2lzZSBhbmQgdW5hbWJpZ3VvdXMgbGFuZ3VhZ2UKLSBUaGUgcmVxdWlyZW1lbnRzIHNob3VsZCBiaSBjb25zaXN0ZW50IHdpdGggZWFjaCBvdGhlciB3aXRoIG91dCBjb250cmFkaWN0aW9ucwotIFRoZSByZXF1aXJlbWVudHMgc2hvdWxkIG5vdCBvdmVybGFwIHdpdGggZXhpc3RpbmcgcmVxdWlyZW1lbnRzCgpIZXJlIGFyZSBzb21lIGJhZCByZXF1aXJlbWVudHM6Ci0gVGhlIG91dHB1dCBzaG91bGQgYmUgaW50ZXJlc3RpbmcuIC0gVGhpcyBpcyBzdWJqZWN0aXZlCi0gVGhlIG91dHB1dCBzaG91bGQgcHJvdmlkZSBleGFtcGxlcyBpbiBmZXdlciB0aGFuIDI4MCBjaGFyYWN0ZXJzLiAtIFRoaXMgb3ZlcmxvYWRzIG11bHRpcGxlIGFzcGVjdHMKLSBUaGUgb3V0cHV0IHNob3VsZCBiaSBoZWxwZnVsIGFuZCBoYXJtbGVzcy4gLSBUaGlzIGlzIG92ZXJseSBnZW5lcmFsCgpIZXJlIGFyZSBzb21lIGdvb2QgYXRvbWljIHJlcXVpcmVtZW50czoKLSBUaGUgb3V0cHV0IHNob3VsZCBwcm92aWRlIGV4YW1wbGVzLgotIFRoZSBvdXRwdXQgc2hvdWxkIGJlIGZld2VyIHRoYW4gMjgwIGNoYXJhY3RlcnMuCi0gVGhlIG91dHB1dCBzaG91bGQgY29udGFpbiBhdCBsZWFzdCAzIHJlZmVyZW5jZXMu)

Youareanexperiencedrequirementsengineer.YourgoalistoextractalistofatomicrequirementsthatspecifydesiredLLMbehaviorsforthegiventask.

Youwillbepresentedwithamodelinputandseveralmodeloutputsfromdifferentmodels.First,provideadetailedanalysiscritiquingthemodeloutputs.

Then,basedontheanalysis,suggestalistofatomicrequirementsthatspecifydesiredLLMbehaviorsforthegiventask.

Theserequirementsshouldbeconsistentwitheachotherwithoutcontradictionsandcomplementarytoexistingrequirements.

Guidelines:

-EachrequirementshouldtestexactlyONErequirement

-Requirementsshouldbeeasilyverifiable,almostasifwritingaBooleanconditioninPython

-Requirementsshouldnotbeoverlygeneral(i.e.theyshouldnotbeuniversalrequirementsthatmightapplytoanytasks)

-Requirementsshouldbegenerallyapplicableforresponsestothattask,notreferringtoanyspecificinputexamples

-Focusonlyonobjective,measurablerequirements

-Useconciseandunambiguouslanguage

-Therequirementsshouldbeconsistentwitheachotherwithoutcontradictions

-Therequirementsshouldnotoverlapwithexistingrequirements

Herearesomebadrequirements:

-Theoutputshouldbeinteresting.-Thisissubjective

-Theoutputshouldprovideexamplesinfewerthan280characters.-Thisoverloadsmultipleaspects

-Theoutputshouldbehelpfulandharmless.-Thisisoverlygeneral

Herearesomegoodatomicrequirements:

-Theoutputshouldprovideexamples.

-Theoutputshouldbefewerthan280characters.

-Theoutputshouldcontainatleast3references.

Figure 9: Prompts for requirement elicitation - Error analysis.

[⬇](data:text/plain;base64,WW91IGFyZSBhIHJldmlld2VyIHdobyBpcyBldmFsdWF0aW5nIHdoZXRoZXIgYSBtb2RlbCBvdXRwdXQgc2F0aXNmaWVzIHRoZSBnaXZlbiByZXF1aXJlbWVudC4gR2l2ZW4gYSB0YXNrIGRlc2NyaXB0aW9uLCBleGFtcGxlcywgYW5kIHJlcXVpcmVtZW50LCBkcmFmdCBhIHN0ZXAtYnktc3RlcCBldmFsdWF0aW9uIHBsYW4gZm9yIHRoZSByZXF1aXJlbWVudC4KCkZvbGxvdyB0aGUgZ3VpZGVsaW5lIGJlbG93OgotIFRoZSBldmFsdWF0aW9uIHBsYW4gc2hvdWxkIGJlIGEgc3RlcC1ieS1zdGVwIHByb2Nlc3MgdG8gZXZhbHVhdGUgaWYgdGhlIHJlcXVpcmVtZW50IGlzIG1ldC4KLSBUaGUgZXZhbHVhdGlvbiBwbGFuIHNob3VsZCBiaSBjb25jaXNlIGFuZCBjbGVhciwgYW5kIGxlYWQgdG8gYSBmaW5hbCBqdWRnbWVudCBvbiB3aGV0aGVyIHRoZSBtb2RlbCBvdXRwdXQgbWVldHMgdGhlIHJlcXVpcmVtZW50LgotIFdoZW4gcmVxdWlyZW1lbnRzIGFyZSBjb25kaXRpb25hbCAoZS5nLiwgaW5kaWNhdGVkIGJ5ICJpZiBhcHBsaWNhYmxlIiksIHRoZSBldmFsdWF0aW9uIHBsYW4gc2hvdWxkIGluY2x1ZGUgYSBmaXJzdCBzdGVwIHRvIGNoZWNrIGlmIHRoZSByZXF1aXJlbWVudCBpcyBhcHBsaWNhYmxlIHRvIGFuIGV4YW1wbGUgaW5wdXQuCi0gVGhlIGV2YWx1YXRpb24gcGxhbiBzaG91bGQgb25seSBpbmNsdWRlIHRoZSBzdGVwcyB0byBldmFsdWF0ZSB0aGUgcmVxdWlyZW1lbnQsIGFuZCBub3QgaW5jbHVkZSBhbnkgYWRkaXRpb25hbCBmZWVkYmFjayBvciBzdWdnZXN0aW9ucywgb3Igc3RlcHMgdG8gZXZhbHVhdGUgb3RoZXIgcmVsYXRlZCBmZXF1aXJlbWVudHMuCgpFeGFtcGxlcwotLS0KUmVxdWlyZW1lbnQ6IFRoZSBleHBsYW5hdGlvbiBzaG91bGQgcHJvdmlkZSBleGFtcGxlcyBvZiBob3cgdG8gaW5zdGFudGlhdGUgYW5kIHVzZSBrZXkgY2xhc3NlcywgaWYgYXBwbGljYWJsZS4KRXZhbHVhdGlvbiBQbGFuOgoxLiBJZGVudGlmeSB0aGUga2V5IGNsYXNzZXMgaW4gdGhlIGdpdmVuIGNvZGUgc25pcHBldCBieSBleGFtaW5pbmcgdGhlIGNvZGUgc3RydWN0dXJlIGFuZCBjbGFzcyBkZWZpbml0aW9ucy4gSWYgdGhlcmUgYXJlIG5vIGtleSBjbGFzc2VzLCB0aGlzIHJlcXVpcmVtZW50IGlzIG5vdCBhcHBsaWNhYmxlLgoyLiBDaGVjayB0aGF0IHRoZSBleHBsYW5hdGlvbiBjbGVhcmx5IGhpZ2hsaWdodHMgd2hpY2ggY2xhc3NlcyBhcmUgY29uc2lkZXJlZCAia2V5IiBmb3IgdGhpcyBzbmlwcGV0IChmb3IgZXhhbXBsZSwgYW55IGNsYXNzZXMgdGhhdCBkZWZpbmUgY29yZSBmdW5jdGlvbmFsaXR5IG9yIGFyZSBjZW50cmFsIHRvIHRoZSBjb2RlJ3MgcHVycG9zZSkuCjMuIFZlcmlmeSB0aGF0IHRoZSBleHBsYW5hdGlvbiBpbmNsdWRlcyBjb25jcmV0ZSBleGFtcGxlcyBzaG93aW5nIGhvdyB0byBpbnN0YW50aWF0ZSB0aGUgaWRlbnRpZmllZCBrZXkgY2xhc3Nlcy4KNC4gRmluYWxseSwgYXNzZXNzIHdoZXRoZXIgdGhlIGV4cGxhbmF0aW9uIG1lZXRzIHRoZSByZXF1aXJlbWVudCBieSBwcm92aWRpbmcgc3VmZmljaWVudCBpbnN0YW50aWF0aW9uIGFuZCB1c2FnZSBleGFtcGxlcyB0aGF0IGEgdXNlciBjb3VsZCBmb2xsb3cu)

Youareareviewerwhoisevaluatingwhetheramodeloutputsatisfiesthegivenrequirement.Givenataskdescription,examples,andrequirement,draftastep-by-stepevaluationplanfortherequirement.

Followtheguidelinebelow:

-Theevaluationplanshouldbeastep-by-stepprocesstoevaluateiftherequirementismet.

-Theevaluationplanshouldbeconciseandclear,andleadtoafinaljudgmentonwhetherthemodeloutputmeetstherequirement.

-Whenrequirementsareconditional(e.g.,indicatedby"ifapplicable"),theevaluationplanshouldincludeafirststeptocheckiftherequirementisapplicabletoanexampleinput.

-Theevaluationplanshouldonlyincludethestepstoevaluatetherequirement,andnotincludeanyadditionalfeedbackorsuggestions,orstepstoevaluateotherrelatedrequirements.

Examples

\-\-\-

Requirement:Theexplanationshouldprovideexamplesofhowtoinstantiateandusekeyclasses,ifapplicable.

EvaluationPlan:

1.Identifythekeyclassesinthegivencodesnippetbyexaminingthecodestructureandclassdefinitions.Iftherearenokeyclasses,thisrequirementisnotapplicable.

2.Checkthattheexplanationclearlyhighlightswhichclassesareconsidered"key"forthissnippet(forexample,anyclassesthatdefinecorefunctionalityorarecentraltothecode'spurpose).

3.Verifythattheexplanationincludesconcreteexamplesshowinghowtoinstantiatetheidentifiedkeyclasses.

4.Finally,assesswhethertheexplanationmeetstherequirementbyprovidingsufficientinstantiationandusageexamplesthatausercouldfollow.

[⬇](data:text/plain;base64,WW91IGFyZSBhIHJldmlld2VyIHdobyBpcyBldmFsdWF0aW5nIHdoZXRoZXIgYSBtb2RlbCBvdXRwdXQgc2F0aXNmaWVzIHRoZSBnaXZlbiByZXF1aXJlbWVudC4gR2l2ZW4gYSB0YXNrIGRlc2NyaXB0aW9uLCBleGFtcGxlcywgYW5kIHJlcXVpcmVtZW50LCB3cml0ZSBhIFB5dGhvbiBmdW5jdGlvbiB0byBldmFsdWF0ZSB0aGUgcmVxdWlyZW1lbnQuCgpUaGUgUHl0aG9uIGZ1bmN0aW9uIGBldmFsdWF0aW9uX2Z1bmN0aW9uYCB0YWtlcyB0YXNrX2Rlc2NyaXB0aW9uLCBtb2RlbF9pbnB1dCwgYW5kIG1vZGVsX291dHB1dCBhcyBpbnB1dCBhcmd1bWVudHMgYW5kIHJldHVybnMgYSBib29sZWFuIHZhbHVlIGluZGljYXRpbmcgd2hldGhlciB0aGUgcmVxdWlyZW1lbnQgaXMgbWV0Lg==)

Youareareviewerwhoisevaluatingwhetheramodeloutputsatisfiesthegivenrequirement.Givenataskdescription,examples,andrequirement,writeaPythonfunctiontoevaluatetherequirement.

ThePythonfunction\`evaluation\_function\`takestask\_description,model\_input,andmodel\_outputasinputargumentsandreturnsabooleanvalueindicatingwhethertherequirementismet.

[⬇](data:text/plain;base64,WW91IGFyZSBhIHJldmlld2VyIHdobyBpcyBldmFsdWF0aW5nIHdoZXRoZXIgYSBtb2RlbCBvdXRwdXQgc2F0aXNmaWVzIHRoZSBnaXZlbiByZXF1aXJlbWVudC4KCkdpdmVuIGEgdGFzayBkZXNjcmlwdGlvbiwgbW9kZWwgaW5wdXQsIG1vZGVsIG91dHB1dCwgYSByZXF1aXJlbWVudCBhbmQgaXRzIHN0ZXAtYnktc3RlcCBldmFsdWF0aW9uIHBsYW4sIGV4ZWN1dGUgdGhlIGV2YWx1YXRpb24gcGxhbiB0byBldmFsdWF0ZSBpZiB0aGUgbW9kZWwgb3V0cHV0IG1lZXRzIHRoZSByZXF1aXJlbWVudC4gSWYgdGhlIHJlcXVpcmVtZW50IGlzIG5vdCBhcHBsaWNhYmxlLCByZXR1cm4gVHJ1ZSBmb3IgbWVldHNfcmVxdWlyZW1lbnQu)

Youareareviewerwhoisevaluatingwhetheramodeloutputsatisfiesthegivenrequirement.

Givenataskdescription,modelinput,modeloutput,arequirementanditsstep-by-stepevaluationplan,executetheevaluationplantoevaluateifthemodeloutputmeetstherequirement.Iftherequirementisnotapplicable,returnTrueformeets\_requirement.

Figure 10: Prompts for requirement evaluation: Planning (top and middle) and execution (bottom).

### A.5 Complete list of curated requirements

Curated requirements for trip-advisory•The output should consider factors such as budget, travel dates, and specific interests.•The output should ask users for details like interests, dietary restrictions, and desired activities.•The output should not include booking or transaction handling.•The output should be friendly, casual, and enthusiastic about travel.•The output should be personalized to user goals and preferences.•The output should be clear and engaging.•The output should be culturally sensitive.•The output should clarify any ambiguous preferences.•The output should show enthusiasm for exploring new cultures and experiences.•The output should ensure activities are age-appropriate if age preferences are specified by the user.•The output should highlight any visa or entry requirements specific to the suggested destinations.•The output should provide warnings about weather conditions that might affect accessibility to certain activities during the user’s planned travel dates.•The output should provide follow-up questions to solicit user preferences if they are not initially provided.•The output should clarify the geographic context if the location is ambiguous.•The output should specify if transportation options are seasonal or subject to availability.•The output should include suggestions for public transport or alternative travel methods.•The output should correctly identify and focus on sites located within the specified geographic area.•The output should provide references to local regulations or park rules, when applicable.•The output should contain a section explicitly stating safety guidelines specific to solo traveling.•The output should include tips for varying levels of experience for recommended activities.

Curated requirements for product-gen•The output must highlight the product’s features.•The output must be written in English.•The output must describe any features listed within the given Context in more detail.•The output must be at least 500 characters long.•The output should preferably be at least 1000 characters long.•The output must not use Markdown syntax.•The output must avoid special characters as much as possible.•The output must avoid excessive use of technical jargon, ensuring that the description is understandable to a general audience.•The output must use engaging and vivid language to capture and retain the reader’s attention.•The output must include at least three benefits that the product provides to the user.•The output must follow a coherent structure, ensuring logical flow from introduction to conclusion.•The output must avoid any explicit comparisons with products from brands unless specified in the context.•The output must ensure that any numerical values or ranges are accurately represented if mentioned at all.•The output must include a mention of the package content.•The output should clearly mention any customer support or warranty information included with the product.•The product description should mention any personalization options available, including any important limitations or specifications.•The output must paint a vivid picture of the customer experience with practical use cases.•The output should break down complex information into clearer, more concise points.•The output must be free from any promotional prompts such as ’click add to cart’.•The output must ensure that key product information is easily skimmable.

Curated requirements for code-explain•The output should break down the code’s functionality.•The output should explain the purpose of the code.•The output should use analogies and examples to clarify the explanation.•If technical jargon is used, the output should provide clear explanations for it.•The output should aim to make the explanation accessible to someone with minimal coding knowledge.•The output should identify and explain any variables or data structures used in the code snippet.•The output should detect and describe any dependencies or libraries required by the code snippet.•The output should check and explain any potential side effects or state changes that occur during code execution.•The output should include a precise, step-by-step execution order that aligns with the code.•If there are error handling mechanisms, the output should accurately describe them and explain how they handle potential errors.•The output should mention any missing components or aspects in the provided code snippet, such as lack of functionality or completeness.•The output should explain scenarios where certain features of the code are particularly beneficial or efficient.•The explanation should include potential applications and implications of the coded algorithm.•The output should address potential edge cases tested by the code.•The output should explicitly define the scope of explanation without making assumptions about specific use cases.•The output should not exceed 500 words to maintain conciseness and focus.•The output should not describe components or operations not present in the provided code.•The output should provide a high-level summary at the beginning to set the context.•The output should provide an example of how at least one function, class, or constant imported from the code can be used.•The output should include information about verifying the setup or configuration before execution, if applicable.

### A.6 Human validation of LLM validators

To assess the reliability of our LLM-based requirement evaluators, we curated a set of
1,095 evaluation results for human validation.
The evaluation results are curated with stratified sampling:
We sample 20 evaluation results (10 positive, 10 negative) per requirement.
If there are not enough results (e.g., when a requirement is almost always satisfied), we take the maximum number available.

We then have a human annotator manually review the evaluations.
For each model output, the annotator compared the predicted label against their own judgment of whether the output satisfied the given requirement.
Overall, the evaluators have 95.6% (SD=0.08) agreement rates, indicating a reasonably high level of human–LLM agreement.

### A.7 Prompt templates and construction

We use a simple prompt template to construct our experiment prompts. The task descriptions are one-line minimal descriptions as shown in Appendix [A.1](https://arxiv.org/html/2505.13360v1#A1.SS1 "A.1 Task descriptions ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

Prompt template for our experiments\[Task description\]Follow the guideline below:\- \[requirement 1\]\- \[requirement 2\]…\- \[requirement N\]

https://arxiv.org/html/2505.13360v1/x7.pngFigure 11: We use a cyclic design to generate prompts. Each prompt (row) covers the same number of k𝑘kitalic\_k consecutive requirements (column). Each requirement is specified k𝑘kitalic\_k times and unspecified N−k𝑁𝑘N-kitalic\_N - italic\_k times exactly. We randomize the order of requirements to distribute requirements from different sources.

In our experiments, our goal is to systematically cover requirement subsets, to make sure (a) each prompt has roughly the same complexity in terms of the number of requirements to follow, and (b) different requirements are specified or unspecified the same number of times.
We use a simple cyclic design to achieve this, as shown in Figure [11](https://arxiv.org/html/2505.13360v1#A1.F11 "Figure 11 ‣ A.7 Prompt templates and construction ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

### A.8 Compute resources used in the experiments

In our first set of experiments (up to Section [3.3](https://arxiv.org/html/2505.13360v1#S3.SS3 "3.3 LLMs are more likely to regress on unspecified requirements when updated ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), we make 6k inferences with each of the 7 models to obtain model outputs. We then make 840k inferences to evaluate the results with gpt-4.1-mini.

In our second experiment (Section [3.5](https://arxiv.org/html/2505.13360v1#S3.SS5 "3.5 LLMs struggle with following many requirements at the same time ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), we make 6k inferences with each of the two models on 3 different prompt configurations (different numbers of requirements). We then make 720k inferences to evaluate the results with gpt-4.1-mini.

For prompt optimization experiments (Section [4](https://arxiv.org/html/2505.13360v1#S4 "4 Requirements-Aware Prompt Optimization ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")), we make 16.2k inferences with each prompt optimizer to produce all optimized prompts (324k inferences for evaluation).
We then make 6k inferences with 4 different optimization results each (480k inferences for evaluation).

## Appendix B Additional experiment results

https://arxiv.org/html/2505.13360v1/x8.pngFigure 12: Comparing LLM+Prompts performances on specified requirements vs. unspecified requirements, we found that, overall, LLM+Prompts perform worse and diverge more for unspecified requirements. This is statistically significant even if we consider all other factors and explains a large portion of the variances observed (Table [3](https://arxiv.org/html/2505.13360v1#A2.T3 "Table 3 ‣ B.1 ANOVA results ‣ Appendix B Additional experiment results ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts")).https://arxiv.org/html/2505.13360v1/x9.pngFigure 13: The histogram of average requirement accuracy drops when the prompts include more requirements (N=1→→\\rightarrow→19). We found 37.5% requirements drop significantly by more than 5%.

### B.1 ANOVA results

We apply ANOVA to analyze how factors like requirement scope, source, category, or model impact LLM+Prompts performance on specified vs. unspecified requirements.
For factors that are significant, we use Tukey’s HSD test to identify which specific group means are significantly different from each other.
Results are reported in Table [3](https://arxiv.org/html/2505.13360v1#A2.T3 "Table 3 ‣ B.1 ANOVA results ‣ Appendix B Additional experiment results ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

Table 3: ANOVA results: We report the F-value and p-value, which quantify the extent to which each variable accounts for the observed variances.
We found that whether a requirement is specified has the largest impact on average accuracy (+0.2) and a significant impact on SD (-0.037).
Breaking down the requirements, we found models struggle with conditional requirements (-0.09 accuracy, +0.017 SD), but are better at requirements found in existing prompts and format-related requirements.

|  | Avg. accuracy | SD of accuracy | Acc. delta | SD delta |
| Specified? | 125.87\*\*\* | 48.47\*\*\* | - | - |
| Conditional? | 19.01\*\*\* | 16.38\*\*\* | 4.55\* | 3.03 |
| Source | 19.99\*\*\* | 36.83\*\*\* | 9.07\*\*\* | 3.63\* |
| Category | 23.86\*\*\* | 55.00\*\*\* | 1.01 | 0.44 |
| Model | 1.80 | 0.57 | 0.68 | 1.71 |
|  | p∗⁣∗∗<0.001,∗∗p<0.01,∗p<0.05{}^{\*\*\*}p<0.001,\\quad^{\*\*}p<0.01,\\quad^{\*}p<0.05start\_FLOATSUPERSCRIPT ∗ ∗ ∗ end\_FLOATSUPERSCRIPT italic\_p < 0.001 , start\_POSTSUPERSCRIPT ∗ ∗ end\_POSTSUPERSCRIPT italic\_p < 0.01 , start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT italic\_p < 0.05 |

### B.2 Prompt Optimization Examples

An example of unoptimized promptsExplain the code snippet.Follow the guideline below:\- The output should explain the purpose of the code.\- The output should explain scenarios where certain features of the code are particularly beneficial or efficient.\- The output should use analogies and examples to clarify the explanation.\- The output should not describe components or operations not present in the provided code.\- The output should check and explain any potential side effects or state changes that occur during code execution.\- The output should include a precise, step-by-step execution order that aligns with the code.\- The output should break down the code’s functionality.\- If technical jargon is used, the output should provide clear explanations for it.\- The output should include information about verifying the setup or configuration before execution, if applicable.\- The output should identify and explain any variables or data structures used in the code snippet.\- The output should explicitly define the scope of explanation without making assumptions about specific use cases.\- The output should aim to make the explanation accessible to someone with minimal coding knowledge.\- If there are error handling mechanisms, the output should accurately describe them and explain how they handle potential errors.\- The output should address potential edge cases tested by the code.\- The output should not exceed 500 words to maintain conciseness and focus.\- The output should provide an example of how at least one function, class, or constant imported from the code can be used.\- The output should detect and describe any dependencies or libraries required by the code snippet.\- The explanation should include potential applications and implications of the coded algorithm.\- The output should provide a high-level summary at the beginning to set the context.

Figure 14: Unoptimized prompts generated from the prompt template (acc=75.4%).

An example of COPRO-optimized promptsProvide a detailed explanation of the given code snippet, following these guidelines:1\. \*\*Overview\*\*: Begin with a high-level summary that sets the context for the code’s purpose and functionality.2\. \*\*Purpose and Benefits\*\*: Clearly explain the code’s main objective and highlight scenarios where its features are particularly beneficial or efficient.3\. \*\*Analogies and Examples\*\*: Use relatable analogies and examples to enhance understanding, especially for complex concepts.4\. \*\*Code Breakdown\*\*: Decompose the code into its fundamental components, explaining the role and function of each part.5\. \*\*Step-by-Step Execution\*\*: Offer a precise, sequential walkthrough of how the code executes, ensuring clarity on the process.6\. \*\*State Changes and Side Effects\*\*: Identify any potential side effects or state changes that occur during execution.7\. \*\*Variable and Data Structure Explanation\*\*: Define and explain any variables or data structures used, ensuring comprehension for those with minimal coding knowledge.8\. \*\*Technical Jargon\*\*: Simplify or clarify any technical terms to make the explanation accessible.9\. \*\*Setup Verification\*\*: Include information on verifying the setup or configuration before running the code, if relevant.10\. \*\*Error Handling\*\*: Describe any error handling mechanisms, detailing how they manage potential errors and edge cases.11\. \*\*Dependencies\*\*: Identify any libraries or dependencies required by the code.12\. \*\*Applications and Implications\*\*: Discuss potential applications and implications of the algorithm or functionality provided by the code.13\. \*\*Function Usage Example\*\*: Provide an example of how at least one function, class, or constant from the code can be utilized.14\. \*\*Conciseness\*\*: Ensure the explanation does not exceed 500 words, maintaining focus and clarity.

Figure 15: COPRO-optimized prompts (acc=86.7%). We found COPRO-optimized prompts tend to reorder requirements in a more logical structure, merge related requirements together, and sometimes drop requirements.

## NeurIPS Paper Checklist

01. 1.

    Claims

02. Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

03. Answer: \[Yes\]

04. Justification: The claims are all backed up by our experimental results.

05. Guidelines:

    - •

      The answer NA means that the abstract and introduction do not include the claims made in the paper.

    - •

      The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers.

    - •

      The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings.

    - •

      It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.

06. 2.

    Limitations

07. Question: Does the paper discuss the limitations of the work performed by the authors?

08. Answer: \[Yes\]

09. Justification: We discuss limitation in our experiment design in Section [3.6](https://arxiv.org/html/2505.13360v1#S3.SS6 "3.6 Limitations ‣ 3 How do LLM+Prompts Behave when Underspecified? ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

10. Guidelines:

    - •

      The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper.

    - •

      The authors are encouraged to create a separate "Limitations" section in their paper.

    - •

      The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be.

    - •

      The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated.

    - •

      The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon.

    - •

      The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size.

    - •

      If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness.

    - •

      While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations.

11. 3.

    Theory assumptions and proofs

12. Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

13. Answer: \[N/A\]

14. Justification: The paper does not include theoretical results.

15. Guidelines:

    - •

      The answer NA means that the paper does not include theoretical results.

    - •

      All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced.

    - •

      All assumptions should be clearly stated or referenced in the statement of any theorems.

    - •

      The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition.

    - •

      Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material.

    - •

      Theorems and Lemmas that the proof relies upon should be properly referenced.

16. 4.

    Experimental result reproducibility

17. Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?

18. Answer: \[Yes\]

19. Justification: Reproduction steps are described in the code.

20. Guidelines:

    - •

      The answer NA means that the paper does not include experiments.

    - •

      If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not.

    - •

      If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable.

    - •

      Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed.

    - •

      While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example

      1. (a)

         If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm.

      2. (b)

         If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully.

      3. (c)

         If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset).

      4. (d)

         We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.

21. 5.

    Open access to data and code

22. Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

23. Answer: \[Yes\]

24. Justification: The experiment code and data are all shared.

25. Guidelines:

    - •

      The answer NA means that paper does not include experiments requiring code.

    - •

      Please see the NeurIPS code and data submission guidelines ( [https://nips.cc/public/guides/CodeSubmissionPolicy](https://nips.cc/public/guides/CodeSubmissionPolicy "")) for more details.

    - •

      While we encourage the release of code and data, we understand that this might not be possible, so “No” is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark).

    - •

      The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines ( [https://nips.cc/public/guides/CodeSubmissionPolicy](https://nips.cc/public/guides/CodeSubmissionPolicy "")) for more details.

    - •

      The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc.

    - •

      The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why.

    - •

      At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable).

    - •

      Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted.

26. 6.

    Experimental setting/details

27. Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results?

28. Answer: \[Yes\]

29. Justification: All experiment details are described.

30. Guidelines:

    - •

      The answer NA means that the paper does not include experiments.

    - •

      The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them.

    - •

      The full details can be provided either with the code, in appendix, or as supplemental material.

31. 7.

    Experiment statistical significance

32. Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

33. Answer: \[Yes\]

34. Justification: All main results are reported with error bars when applicable.

35. Guidelines:

    - •

      The answer NA means that the paper does not include experiments.

    - •

      The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.

    - •

      The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions).

    - •

      The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.)

    - •

      The assumptions made should be given (e.g., Normally distributed errors).

    - •

      It should be clear whether the error bar is the standard deviation or the standard error of the mean.

    - •

      It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified.

    - •

      For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g. negative error rates).

    - •

      If error bars are reported in tables or plots, The authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.

36. 8.

    Experiments compute resources

37. Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

38. Answer: \[Yes\]

39. Justification: We describe compute resources used in the Appendix [A.8](https://arxiv.org/html/2505.13360v1#A1.SS8 "A.8 Compute resources used in the experiments ‣ Appendix A Details on Experiments Setups ‣ What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts").

40. Guidelines:

    - •

      The answer NA means that the paper does not include experiments.

    - •

      The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.

    - •

      The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.

    - •

      The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).

41. 9.

    Code of ethics

42. Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics [https://neurips.cc/public/EthicsGuidelines](https://neurips.cc/public/EthicsGuidelines "")?

43. Answer: \[Yes\]

44. Justification: The research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics.

45. Guidelines:

    - •

      The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.

    - •

      If the authors answer No, they should explain the special circumstances that require a deviation from the Code of Ethics.

    - •

      The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).

46. 10.

    Broader impacts

47. Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

48. Answer: \[N/A\]

49. Justification: The paper does not directly have societal impact – it studies behaviors of existing LLMs in a specific setting.

50. Guidelines:

    - •

      The answer NA means that there is no societal impact of the work performed.

    - •

      If the authors answer NA or No, they should explain why their work has no societal impact or why the paper does not address societal impact.

    - •

      Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.

    - •

      The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster.

    - •

      The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from (intentional or unintentional) misuse of the technology.

    - •

      If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML).

51. 11.

    Safeguards

52. Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pretrained language models, image generators, or scraped datasets)?

53. Answer: \[N/A\]

54. Justification: The paper poses no such risks.

55. Guidelines:

    - •

      The answer NA means that the paper poses no such risks.

    - •

      Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters.

    - •

      Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images.

    - •

      We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort.

56. 12.

    Licenses for existing assets

57. Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

58. Answer: \[Yes\]

59. Justification: Reused datasets are cited and the licenses are mentioned and respected.

60. Guidelines:

    - •

      The answer NA means that the paper does not use existing assets.

    - •

      The authors should cite the original paper that produced the code package or dataset.

    - •

      The authors should state which version of the asset is used and, if possible, include a URL.

    - •

      The name of the license (e.g., CC-BY 4.0) should be included for each asset.

    - •

      For scraped data from a particular source (e.g., website), the copyright and terms of service of that source should be provided.

    - •

      If assets are released, the license, copyright information, and terms of use in the package should be provided. For popular datasets, [paperswithcode.com/datasets](https://arxiv.org/html/2505.13360v1/paperswithcode.com/datasets "") has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset.

    - •

      For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided.

    - •

      If this information is not available online, the authors are encouraged to reach out to the asset’s creators.

61. 13.

    New assets

62. Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

63. Answer: \[Yes\]

64. Justification: Code written and data curated are shared in the paper.

65. Guidelines:

    - •

      The answer NA means that the paper does not release new assets.

    - •

      Researchers should communicate the details of the dataset/code/model as part of their submissions via structured templates. This includes details about training, license, limitations, etc.

    - •

      The paper should discuss whether and how consent was obtained from people whose asset is used.

    - •

      At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonyomized zip file.

61. 14.

    Crowdsourcing and research with human subjects

62. Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

63. Answer: \[N/A\]

64. Justification: The paper does not involve crowdsourcing nor research with human subjects.

65. Guidelines:

    - •

      The answer NA means that the paper does not involve crowdsourcing nor research with human subjects.

    - •

      Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should be included in the main paper.

    - •

      According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector.

66. 15.

    Institutional review board (IRB) approvals or equivalent for research with human subjects

67. Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

68. Answer: \[N/A\]

69. Justification: The paper does not involve crowdsourcing nor research with human subjects.

70. Guidelines:

    - •

      The answer NA means that the paper does not involve crowdsourcing nor research with human subjects.

    - •

      Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper.

    - •

      We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution.

    - •

      For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review.

71. 16.

    Declaration of LLM usage

72. Question: Does the paper describe the usage of LLMs if it is an important, original, or non-standard component of the core methods in this research? Note that if the LLM is used only for writing, editing, or formatting purposes and does not impact the core methodology, scientific rigorousness, or originality of the research, declaration is not required.

73. Answer: \[Yes\]

74. Justification: We describe how we use LLM-assisted requirements curation and LLM-as-a-judge for evaluation in our experiments.

75. Guidelines:

    - •

      The answer NA means that the core method development in this research does not involve LLMs as any important, original, or non-standard components.

    - •

      Please refer to our LLM policy ( [https://neurips.cc/Conferences/2025/LLM](https://neurips.cc/Conferences/2025/LLM "") ) for what should or should not be described.

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