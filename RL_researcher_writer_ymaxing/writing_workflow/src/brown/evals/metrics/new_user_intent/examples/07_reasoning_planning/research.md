# Research

## Research Results

<details>
<summary>Query 1: ReAct vs Plan-and-Execute agent patterns for complex multi-step tasks</summary>

<research_source type="tavily_results" phase="exploitation" url="https://blog.langchain.com/planning-agents/">

### Source [1]: https://blog.langchain.com/planning-agents/

Planning agents are a class of AI systems that separate the planning phase from the execution phase. In contrast to the ReAct pattern, where reasoning and action are interleaved step-by-step, planning agents create a full plan consisting of a sequence of tasks, and then execute each task in order. This fundamentally changes the interaction loop: instead of deciding step by step, a single "planner" LLM call produces an ordered task list, and a separate executor processes each step. This is particularly advantageous for tasks where efficiency and predictability are priorities, as the upfront planning step reduces the number of LLM calls during execution. However, planning agents may struggle with tasks requiring extensive exploration or iterative refinement, since the plan is made before execution begins.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/">

### Source [2]: https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/

LangGraph distinguishes between several agent architectures. The ReAct architecture interleaves reasoning (Thought) and acting (Action/Observation) in a loop, deciding the next step based on the results of the previous one. This pattern enables dynamic, adaptive decision-making but can be slower and more expensive due to multiple LLM calls. The Plan-and-Execute architecture, in contrast, separates planning from execution: the planner produces a full plan upfront, and the executor handles each step. Re-planning can be triggered when conditions change or new information is discovered during execution. The key tradeoff: ReAct is better for exploratory, open-ended tasks; Plan-and-Execute is better for predictable, efficiency-focused workflows.

</research_source>

-----

<golden_source type="guideline_url" url="https://arxiv.org/pdf/2210.03629">

### Source [3]: https://arxiv.org/pdf/2210.03629

The ReAct paper introduces a framework that synergizes reasoning and acting in language models. Rather than treating reasoning (e.g., chain-of-thought) and acting (e.g., tool use) as separate capabilities, ReAct interleaves them: the model generates a reasoning trace (Thought), decides on an action (Action), observes the result (Observation), and then reasons again. This tight loop allows the model to dynamically adjust its plan based on new information, handle exceptions, and explore solutions more deeply. The paper demonstrates that ReAct outperforms both reasoning-only and acting-only approaches on tasks requiring multi-step decision-making, such as question answering over Wikipedia and web navigation. ReAct also improves interpretability, as the reasoning traces make the model's decision process transparent and debuggable.

</golden_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://dev.to/jamesli/react-vs-plan-and-execute-agents-a-comprehensive-comparison-d8d">

### Source [4]: https://dev.to/jamesli/react-vs-plan-and-execute-agents-a-comprehensive-comparison-d8d

A comprehensive comparison of ReAct and Plan-and-Execute agents. ReAct excels at tasks that require adaptability and dynamic decision-making but tends to use more tokens and make more API calls due to its iterative loop. Plan-and-Execute agents are more cost-effective for well-defined tasks because the plan is generated once and executed step-by-step, requiring fewer LLM calls. However, Plan-and-Execute may produce suboptimal results for tasks requiring significant exploration or when the task cannot be fully specified upfront. The article notes that choosing between the two depends on the task characteristics: use ReAct for uncertain, exploratory tasks; use Plan-and-Execute for predictable, efficient workflows.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://www.willowtreeapps.com/craft/building-ai-agents-with-planning-capabilities">

### Source [5]: https://www.willowtreeapps.com/craft/building-ai-agents-with-planning-capabilities

Building AI agents with planning capabilities involves structuring the agent's workflow around explicit planning steps. The article discusses how Plan-and-Execute patterns enable agents to outline a full execution plan before acting, then track progress as each step completes. The main advantages include reduced LLM calls (efficiency), clear audit trails, and predictability. Challenges include the difficulty of re-planning mid-execution when new information invalidates the original plan.

</research_source>

</details>

<details>
<summary>Query 2: Modern LLMs reasoning and tool use with interleaved thinking</summary>

<research_source type="tavily_results" phase="exploitation" url="https://platform.openai.com/docs/guides/structured-outputs">

### Source [6]: https://platform.openai.com/docs/guides/structured-outputs

OpenAI's Structured Outputs guide demonstrates how models can alternate between reasoning and tool calls by producing structured JSON actions. When a task requires multiple steps, the model generates a structured action (e.g., a function call with typed parameters), receives the tool result, then reasons about the result before deciding the next action. This interleaving of reasoning and structured action selection is the foundation of reliable agentic behavior.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking">

### Source [7]: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking

Claude's Extended Thinking feature enables the model to produce an internal reasoning trace (thinking block) before generating its visible response. This creates two distinct streams: a private "thinking" stream where the model breaks down the problem, considers alternatives, and plans its approach; and a public "answer" stream with the final response. For multi-turn conversations, thinking blocks are preserved between turns, allowing the model to build upon previous reasoning. When combined with tool use, the model can interleave thinking blocks between tool calls — reasoning about one tool's output before deciding whether to call another tool. Extended thinking improves performance on complex tasks requiring mathematical reasoning, code analysis, and multi-step problem-solving.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://docs.anthropic.com/en/docs/build-with-claude/interleaved-thinking">

### Source [8]: https://docs.anthropic.com/en/docs/build-with-claude/interleaved-thinking

Interleaved thinking extends Claude's reasoning capabilities into multi-turn, tool-use conversations. With interleaved thinking enabled, the model produces thinking blocks not just at the start of its response, but also between tool calls and their results. This means the model can: (1) receive a tool result, (2) generate a thinking block analyzing that result, (3) decide on the next action, and (4) repeat. This fine-grained reasoning loop mirrors the ReAct pattern at the model architecture level, with the key difference that the reasoning happens in a private stream, not visible to the user. For developers, this means the model's internal deliberation can be inspected for debugging but does not clutter the user-facing response.

</research_source>

</details>

<details>
<summary>Query 3: Goal decomposition and sub-task planning in AI agents</summary>

<golden_source type="guideline_url" url="https://www.ibm.com/think/topics/agentic-reasoning">

### Source [9]: https://www.ibm.com/think/topics/agentic-reasoning

Agentic reasoning is an advanced AI capability that allows machines to plan, act, evaluate, and improve in pursuit of specific goals. Unlike traditional AI systems that follow predefined rules, agentic reasoning enables adaptive decision-making processes where the AI adjusts its strategies based on outcomes. Key components include: (1) **Task decomposition** — the AI breaks a larger goal into smaller, manageable subtasks, defining clear objectives for each; (2) **Tool selection** — the system identifies which external tools or APIs to use for each subtask; (3) **Execution** — the agent carries out each subtask using the selected tools; (4) **Evaluation** — after execution, the agent reviews the results against the original goals; (5) **Self-correction** — if results fall short, the agent revises its approach and re-executes. This reasoning loop enables agents to handle ambiguous, open-ended tasks that would defeat a rigid pipeline. The ability to decompose goals into structured subtasks is fundamental to all planning-based agent architectures, whether ReAct, Plan-and-Execute, or hybrid approaches.

</golden_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://arxiv.org/html/2404.11584v1">

### Source [10]: https://arxiv.org/html/2404.11584v1

A survey on planning in LLM-based agents identifies goal decomposition as a core capability. The paper categorizes decomposition strategies: top-down (recursively splitting a high-level goal into sub-goals), bottom-up (aggregating small steps into a plan), and hybrid (combining both). Effective decomposition reduces the cognitive load on the LLM for each individual step and enables parallel execution of independent sub-tasks. The paper finds that decomposition quality is the strongest predictor of overall agent performance on complex benchmarks.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://www.amazon.science/blog/breaking-down-complex-tasks-with-llm-agents">

### Source [11]: https://www.amazon.science/blog/breaking-down-complex-tasks-with-llm-agents

Amazon Science explores how task decomposition and smaller, specialized LLMs can make AI more affordable and scalable. The approach involves a hierarchical decomposition where a "planner" agent breaks a complex goal into a sequence of subtasks, each assigned to a specialized executor. Key findings: decomposition reduces per-step error rates, enables the use of smaller models for routine subtasks while reserving larger models for planning, and improves overall system interpretability. The article also discusses failure detection during execution and dynamic re-planning when subtasks fail.

</research_source>

</details>

<details>
<summary>Query 4: Self-correction and error recovery in LLM agents</summary>

<research_source type="tavily_results" phase="exploitation" url="https://arxiv.org/abs/2310.01798">

### Source [12]: https://arxiv.org/abs/2310.01798

This paper studies self-correction in large language models — the ability of a model to refine its own output based on feedback. The paper distinguishes between intrinsic self-correction (where the model critiques and improves its own output without external feedback) and extrinsic self-correction (where external signals like tool results or human feedback guide the correction). The paper finds that intrinsic self-correction is unreliable for reasoning tasks, as models often "correct" correct answers into wrong ones. However, extrinsic self-correction — triggered by tool outputs, validation errors, or environmental feedback — is highly effective and forms the basis of the ReAct observation-driven loop.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://www.galileo.ai/blog/agentic-self-correction-for-llm-applications">

### Source [13]: https://www.galileo.ai/blog/agentic-self-correction-for-llm-applications

Agentic self-correction involves building feedback loops into AI agent workflows. After generating an initial output, the agent evaluates the result against success criteria, and if the result is unsatisfactory, the agent modifies its approach and retries. Practical self-correction strategies include: re-prompting with the error message, changing the tool or data source, simplifying the subtask, or escalating to a more capable model. The article emphasizes that self-correction is vital for production agents handling real-world, unpredictable inputs, and provides measurable improvements in task completion rates.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://arxiv.org/abs/2308.03188">

### Source [14]: https://arxiv.org/abs/2308.03188

This paper examines how to prompt LLMs for effective self-correction. The key finding is that providing structured feedback (such as specific error descriptions, failed test cases, or tool output discrepancies) dramatically improves correction quality compared to generic "try again" prompts. The paper proposes a framework where the agent: (1) generates an initial output, (2) runs a verification step (tool call, test, or schema validation), (3) if verification fails, feeds the specific error back to the model with the original output, and (4) regenerates. This loop continues until verification passes or a maximum retry count is reached.

</research_source>

</details>

<details>
<summary>Query 5: Deep research AI systems and agentic web research</summary>

<research_source type="tavily_results" phase="exploitation" url="https://glean.com/blog/deep-research-ai-agents">

### Source [15]: https://glean.com/blog/deep-research-ai-agents

Deep research AI systems represent the most complex application of planning and reasoning in LLM agents. These systems combine long-horizon task decomposition, iterative search-and-synthesis loops, and multi-source verification to produce comprehensive research reports. A deep research agent typically: (1) decomposes the research question into sub-questions, (2) searches multiple sources for each sub-question, (3) extracts and synthesizes findings, (4) identifies gaps or conflicts, (5) conducts additional targeted searches to fill gaps, and (6) generates a final structured report with citations. The system blends ReAct-style adaptive exploration with Plan-and-Execute-style upfront structuring, creating a hybrid architecture.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://serjhenrique.com/blog/deep-research-systems-explained">

### Source [16]: https://serjhenrique.com/blog/deep-research-systems-explained

Deep research systems show how reasoning and planning patterns from ReAct and Plan-and-Execute converge in production systems. The typical deep research pipeline includes: an initial plan generation step (like Plan-and-Execute), followed by iterative cycles of search, extraction, and reflection (like ReAct). When the agent encounters conflicting information across sources, it can dynamically spawn additional search queries — exhibiting the adaptive behavior characteristic of ReAct. The article argues that production-grade research agents are inherently hybrid, combining the efficiency of upfront planning with the adaptability of step-by-step reasoning.

</research_source>

</details>

<details>
<summary>Query 6: Chain-of-thought prompting history and development</summary>

<research_source type="tavily_results" phase="exploitation" url="https://arxiv.org/abs/2201.11903">

### Source [17]: https://arxiv.org/abs/2201.11903

The Chain-of-Thought (CoT) paper by Wei et al. (2022) showed that prompting LLMs to produce intermediate reasoning steps before the final answer significantly improves performance on arithmetic, commonsense, and symbolic reasoning tasks. The key insight is that by generating a reasoning trace — a series of natural-language steps leading to the answer — the model can decompose complex problems into manageable sub-steps. Scaling to larger models amplifies this effect. CoT prompting requires no model modification and works through few-shot examples that include reasoning chains.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://arxiv.org/abs/2205.11916">

### Source [18]: https://arxiv.org/abs/2205.11916

Zero-Shot Chain-of-Thought demonstrated that simply appending "Let's think step by step" to the prompt, without providing any few-shot examples, elicits reasoning traces from LLMs. This showed that chain-of-thought reasoning is an emergent capability of sufficiently large language models, not a skill that requires explicit demonstration. The paper validated CoT's generality across domains and established that prompting strategies alone can unlock sophisticated reasoning behavior.

</research_source>

</details>

<details>
<summary>Query 7: Failure modes of non-reasoning AI agents</summary>

<research_source type="tavily_results" phase="exploitation" url="https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf">

### Source [19]: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf

OpenAI's practical guide identifies key failure modes in AI agents that lack reasoning capabilities: (1) **No iteration on partial results** — the agent generates a single response without evaluating or refining it; (2) **Superficial and weak outputs** — without planning, the agent produces surface-level responses that miss nuance; (3) **No explicit breakdown of sub-goals** — the agent attempts to solve the entire problem in one pass, leading to errors on multi-step tasks; (4) **No error recovery** — when a tool call fails or returns unexpected results, the agent cannot adapt. The guide recommends building explicit reasoning and planning loops to address these failures.

</research_source>

-----

<research_source type="tavily_results" phase="exploitation" url="https://hub.athina.ai/blog/top-failure-modes-of-llm-agents-and-how-to-overcome-them/">

### Source [20]: https://hub.athina.ai/blog/top-failure-modes-of-llm-agents-and-how-to-overcome-them/

Common failure modes in LLM agents include: repeated API calls without progress (infinite loops), incorrect tool selection, hallucinated tool parameters, failure to synthesize results from multiple tools, and inability to handle ambiguous or incomplete tool responses. The article emphasizes that without explicit reasoning steps, agents are particularly prone to tool-use failures where the model generates syntactically valid but semantically incorrect tool calls.

</research_source>

</details>

<details>
<summary>Query 8: Hybrid agent architectures combining ReAct and planning patterns</summary>

<golden_source type="guideline_url" url="https://www.anthropic.com/engineering/building-effective-agents">

### Source [21]: https://www.anthropic.com/engineering/building-effective-agents

Anthropic's guide on building effective agents describes several production-ready agent patterns, from simple tool-use augmentation to fully autonomous orchestration. Key patterns include: (1) **Augmented LLM** — a base LLM enhanced with retrieval and tool use; (2) **Prompt chaining** — breaking tasks into sequential LLM calls, each processing the output of the previous; (3) **Routing** — classifying input and directing to specialized handlers; (4) **Orchestrator-workers** — a central LLM dynamically delegating subtasks to specialized worker agents; (5) **Evaluator-optimizer** — one LLM generates output, another evaluates and provides feedback. The guide emphasizes starting simple, using explicit orchestration over autonomous agents when possible, and carefully designing tool interfaces. For complex, open-ended tasks, the orchestrator-worker pattern offers the best balance of capability and reliability, with the orchestrator planning and the workers executing.

</golden_source>

-----

<golden_source type="guideline_url" url="https://www.ibm.com/think/topics/react-agent">

### Source [22]: https://www.ibm.com/think/topics/react-agent

IBM's ReAct agent explainer describes how the Reason + Act (ReAct) pattern works in practice. A ReAct agent interleaves reasoning with tool use in a tight loop: the model first generates a reasoning trace (Thought) about what to do next, then selects and executes an action (Action), receives the result (Observation), and reasons again. This loop continues until the agent has enough information to produce a final answer. Key advantages include interpretability (the reasoning trace is human-readable), grounding (actions are verified against real-world data), and adaptability (the agent can change course based on observations). Challenges include higher latency and cost due to multiple LLM calls, and the need for guardrails to prevent infinite loops.

</golden_source>

-----

<golden_source type="guideline_url" url="https://www.ibm.com/think/topics/ai-agent-orchestration">

### Source [23]: https://www.ibm.com/think/topics/ai-agent-orchestration

AI agent orchestration coordinates multiple AI agents or components to complete complex tasks. Orchestrated systems can combine planning agents, execution agents, and verification agents into multi-agent workflows. The orchestrator manages task decomposition, resource allocation, and inter-agent communication. Key benefits include scalability (distributing work across specialized agents), fault tolerance (reassigning tasks if an agent fails), and quality (enabling verification and feedback loops). IBM highlights that effective orchestration requires clear interfaces between agents, explicit state management, and robust error handling.

</golden_source>

</details>

## Sources Scraped From Research Results

<details>
<summary>IBM: Agentic Reasoning – Advanced AI Capabilities (Scraped)</summary>

<golden_source type="scraped_from_research" url="https://www.ibm.com/think/topics/agentic-reasoning">

Agentic reasoning is an advanced AI capability that allows machines to plan, act, evaluate, and improve in pursuit of specific goals. It enables AI systems to independently analyze complex problems, create strategic plans, and adapt their approach based on real-time feedback. Unlike traditional AI systems that follow predefined rules, agentic reasoning introduces a dynamic, iterative decision-making process where the AI can adjust its strategies based on outcomes.

The core loop of agentic reasoning consists of five steps:

1. **Task Decomposition** — The AI breaks a larger goal into smaller, manageable subtasks, defining clear objectives for each step.
2. **Tool Selection** — The system identifies which external tools, APIs, or data sources are most appropriate for each subtask.
3. **Execution** — The agent carries out each subtask using the selected tools and resources.
4. **Evaluation** — After execution, the agent reviews the results against the original goals and success criteria.
5. **Self-Correction** — If results fall short of expectations, the agent revises its approach, adjusts parameters, or tries alternative strategies.

This reasoning loop enables agents to handle tasks that are ambiguous, open-ended, or require real-time adaptation — scenarios that would defeat a rigid, predefined pipeline. The ability to decompose goals into structured subtasks is fundamental to all planning-based agent architectures, whether ReAct, Plan-and-Execute, or hybrid approaches.

Agentic reasoning has practical applications across industries: in business operations, it automates complex workflows that previously required human judgment; in research, it enables deep literature review and synthesis; in software development, it supports code generation, testing, and debugging cycles.

</golden_source>

</details>

<details>
<summary>Anthropic: Building Effective Agents – Extended Patterns (Scraped)</summary>

<golden_source type="scraped_from_research" url="https://www.anthropic.com/engineering/building-effective-agents">

Anthropic's guide provides detailed patterns for building agents that balance capability with reliability. The guide emphasizes a critical principle: **start with the simplest solution that works, and add complexity only when needed.** Many tasks that seem to require full agent autonomy can be solved with simpler patterns like prompt chaining or routing.

For complex research tasks, the **orchestrator-worker pattern** is recommended: a central LLM acts as the orchestrator, breaking the main task into subtasks and delegating each to specialized worker agents. The orchestrator manages the overall plan, tracks progress, and synthesizes results. Workers focus on individual subtasks (searching, extracting, summarizing) and report back to the orchestrator.

When building any agent system, the guide stresses three principles:
1. **Design clear tool interfaces** — each tool should do one thing well, with clear inputs and outputs.
2. **Provide explicit planning instructions** — tell the model to plan before acting, especially for multi-step tasks.
3. **Build in verification** — after each critical step, verify the result before proceeding.

The evaluator-optimizer pattern (one LLM generates, another evaluates) is particularly powerful for writing tasks, where iterative refinement consistently improves output quality.

</golden_source>

</details>
