# Planning and Reasoning: The Brains of an AI Agent

In our course so far, we have assembled the essential building blocks for AI engineering. We have explored the landscape of agents and workflows, learned the art of context engineering, built a foundation for reliable data with structured outputs, and given our systems the ability to act using tools. But a pile of bricks, no matter how well-made, does not make a house. You need an architect to design a blueprint and a builder to follow it.

Similarly, an agent with access to tools is just a collection of potential actions. Without a "brain" to direct those actions, it cannot tackle complex, multi-step problems. This is where planning and reasoning come in. They are the cognitive engine that transforms a simple tool-user into an autonomous agent. LLMs, by their nature, are predictors of the next word, not strategic planners. They require structure to think, plan, and adapt.

This lesson introduces the foundational patterns that give agents this structure. We will explore ReAct and Plan-and-Execute, two historically important and still highly relevant strategies for orchestrating an agent's thought process. Understanding these patterns is essential for building robust, intelligent systems that can decompose goals, correct their own mistakes, and navigate the complexities of the real world.

## What a Non-Reasoning Model Does And Why It Fails on Complex Tasks

To understand the need for planning, let's start with what happens when it is absent. We will use a recurring example throughout this lesson: a "Technical Research Assistant Agent." Its goal is to produce a comprehensive report on the "Latest developments in edge AI deployment." This involves finding recent papers, summarizing their findings, identifying trends, and writing a structured report.

A non-reasoning model, when given this task, behaves like an overeager but naive assistant. It immediately starts "answering" without first drafting a plan [[1]](https://www.narrativa.com/ai-reasoning-vs-non-reasoning-models-key-differences-explained). It treats the entire complex request as a single-shot generation task. While it might call the right tools, it does so based on pattern matching from its training data, not an adaptive strategy. If it encounters an unexpected result, like a broken link or a paywalled article, it often fails entirely because it lacks a mechanism to reconsider its approach [[2]](https://www.kuppingercole.com/research/lb80993/fundamental-scaling-limitations-in-ai-reasoning-models).

This behavior leads to several critical failures on complex tasks. The outputs are often superficial because the agent does not break the problem down into sub-goals like verifying sources or comparing conflicting claims. It performs no iteration; once a piece of text is generated, it is considered final, with no process for self-analysis or correction [[3]](https://arxiv.org/html/2606.07462v1). It might find one or two papers and summarize them, but it will likely miss the deeper requirements of identifying trends or synthesizing gaps in the research.

In our previous lessons, we built modularity with workflows and reliability with structured outputs. We enabled our systems to take action with tools. These are powerful components for predictable processes. However, for complex tasks where the path forward is uncertain and requires adaptation, they are not enough. Without explicit reasoning, the agent's performance drifts, and it cannot reliably achieve its goal. To solve this, we must first teach the model to think before it acts.

## Teaching Models to “Think” Chain-of-Thought and Its Limits

The first major step toward agentic reasoning was realizing we could prompt a model to "think" before it answers. This is the core idea behind Chain-of-Thought (CoT) prompting. Just as humans often talk themselves through a problem, we can instruct an LLM to write out its reasoning steps before providing the final response. This simple technique unlocks a basic form of planning and allows the model to iterate on its own intermediate thoughts.

Let's apply this to our research assistant agent. Instead of just asking for the report, we would modify the prompt:

"*Before answering, think step by step about how you will research and verify sources on edge AI deployment. Then provide the final report.*"

With this prompt, the model's behavior changes. It first drafts a high-level plan, something like: "First, I will search for recent papers on edge AI. Then, I will read the abstracts to identify the most relevant ones. After that, I will compare their findings to synthesize key trends. Finally, I will write the report." This reasoning trace gives the model a self-created guide to follow.

However, CoT has significant limitations that prevent it from being a complete solution for agentic planning. First, the plan and the final answer are entangled in the same text block, making the output difficult to parse and control programmatically [[7]](https://apxml.com/courses/intro-llm-agents/chapter-5-basic-agent-planning/guiding-agent-reasoning-chain-of-thought). Second, it is not a true iterative loop. The model generates the plan upfront but does not have a native mechanism to execute it step-by-step, observe the results of each action, and then adapt the plan accordingly [[7]](https://apxml.com/courses/intro-llm-agents/chapter-5-basic-agent-planning/guiding-agent-reasoning-chain-of-thought). Finally, while it improves accuracy, CoT does not guarantee correctness; a model can produce a perfectly coherent but factually wrong reasoning path [[9]](https://www.comet.com/site/blog/chain-of-thought-prompting). It is a heuristic, not a robust planning algorithm.

To gain the structure and control needed for true autonomy, we need to formally separate the process of planning from the process of acting. This separation is the foundation of the two most important patterns in agent design: ReAct and Plan-and-Execute.

## Separating Planning from Answering Foundations of ReAct and Plan-and-Execute

The key to building more powerful agents is to create a clear separation between reasoning and acting. Instead of blending thought and action into a single output, we structure the agent's process into distinct phases. This fundamental shift gives us greater control, interpretability, and the ability to build iterative loops where the agent can learn from its environment.

This separation allows us to treat reasoning traces differently from the final outputs. We can scrutinize the agent's plan, check its logic, and see how it responds to new information. This is what enables an agent to not just follow a script, but to adapt its strategy based on real-world feedback.

Two primary patterns have emerged from this idea:

*   **ReAct** is a framework that tightly interleaves reasoning and acting. The agent operates in a loop: it generates a **Thought**, takes an **Action**, and then makes an **Observation** based on the result. This cycle repeats, allowing the plan to evolve dynamically with each new piece of information.
*   **Plan-and-Execute** creates a more rigid separation. The agent first enters a dedicated **Planning** phase to generate a complete, step-by-step plan. Only then does it move to an **Execution** phase, where it carries out those steps sequentially.

These patterns are not just historical footnotes; they are foundational concepts that continue to influence the design of even the most advanced AI agents today. To see how they work, we will first take a deep dive into the ReAct framework using our research assistant example.

## ReAct in Depth Loop, Evolving Example, Pros and Cons

The ReAct framework was a breakthrough because it bridged the gap between abstract reasoning, like Chain-of-Thought, and action-oriented systems [[ReAct: Synergizing Reasoning and Acting in Language Models]](https://arxiv.org/pdf/2210.03629). It synergizes reasoning and acting by creating a continuous feedback loop. The agent thinks about what to do, acts on that thought, observes the outcome, and then uses that observation to inform its next thought. This iterative process mirrors how humans approach complex, exploratory tasks [[11]](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents).

The core of ReAct is its Thought-Action-Observation loop. Each cycle builds on the last, allowing the agent to dynamically adjust its plan based on real-time feedback from its environment, which typically consists of a set of tools.

Image 1: A flowchart illustrating the iterative ReAct loop.

Let's walk through our "Technical Research Assistant Agent" example to see how this works in practice.

*   **Thought:** "I need to find recent, trustworthy sources on edge AI deployment. I should start by searching academic databases like arXiv and industry publication sites."
*   **Action:** `search("latest developments in edge AI deployment 2024 site:arxiv.org OR site:nature.com")`
*   **Observation:** The search returns a list of five research papers and two industry reports.
*   **Thought:** "The initial search was successful. Now I need to evaluate these sources. I will select the three most cited papers and the most recent industry report to ensure relevance and credibility. I will check their publication dates and venues."
*   **Action:** `fetch_and_extract(paper_urls=['url1', 'url2', 'url3'], report_urls=['url4'])`
*   **Observation:** The tool extracts the abstracts, metadata, and key claims from the selected sources.
*   **Thought:** "I have the core information. Now I need to summarize each source and compare their claims, specifically looking for data on adoption rates. I will flag any conflicting statistics."
*   **Action:** `summarize_and_compare(extractions)`
*   **Observation:** The summary reveals a conflict: Paper A claims a 40% adoption rate in manufacturing, while Paper B reports only 25%.
*   **Thought:** "A conflict has been detected. The 15% difference in adoption rates is significant. I need a third-party source to resolve this. I will search for a market analysis report from a credible firm."
*   **Action:** `search("edge AI deployment adoption market analysis 2024")`
*   **Observation:** The search returns a report from a reputable market analysis firm that corroborates the lower 25% figure and explains the discrepancy.
*   **Thought:** "The conflict is resolved. I can now finalize the key trends and identify gaps in the research, using the market report as a tie-breaker. I am ready to structure and write the final answer."
*   **Final Answer:** The agent generates a structured report with inline citations, including a note on the resolved statistical conflict.

This example highlights the strengths of ReAct. It offers high interpretability, as we can follow the agent's reasoning at each step. It also provides a natural mechanism for error recovery; when the agent observes a conflict, it can reason about the problem and take a new action to solve it. This makes ReAct well-suited for exploratory tasks where the path to the solution is not known in advance [[Agentic Reasoning - IBM]](https://www.ibm.com/think/topics/agentic-reasoning).

However, ReAct is not without its drawbacks. The iterative nature of the loop can make it slower and more computationally expensive than other approaches. It also requires careful prompt engineering and robust guardrails to prevent it from getting stuck in repetitive loops or taking undesirable actions. For tasks where the overall structure is more predictable, the Plan-and-Execute pattern can offer a more efficient and reliable alternative.

## Plan-and-Execute in Depth Plan, Execution, Pros and Cons

While ReAct excels at exploratory tasks, many real-world problems have a more predictable structure. For these scenarios, the Plan-and-Execute pattern provides a more efficient and reliable approach. Instead of interleaving thought and action, this method separates the process into two distinct phases: first, the agent generates a comprehensive, step-by-step plan, and second, it executes that plan sequentially [[16]](https://openreview.net/forum?id=ybA4EcMmUZ).

This separation allows the agent to think holistically about the problem upfront, creating a detailed blueprint before taking any action. The execution phase then becomes a more straightforward process of carrying out predefined steps. The plan is not entirely rigid; it can be updated or refined if the agent encounters unexpected issues, but re-planning is an exception rather than the default at every step.

Image 2: A flowchart illustrating the Plan-and-Execute approach with distinct planning and execution phases, including a feedback loop for plan refinement.

Let's revisit our "Technical Research Assistant Agent" to see how it would operate using the Plan-and-Execute pattern.

**Planning Phase:**
First, the agent is prompted to create a detailed plan. The output of this phase would be a structured list of steps, similar to a project plan.

1.  **Define Scope and Success Criteria:** Clearly establish the report's objectives. The final output must be a 500-word technical report summarizing developments in edge AI, identifying at least three key trends and two research gaps, with all claims cited from sources published in the last 18 months.
2.  **Search Across Academic and Industry Sources:** Execute parallel searches on arXiv, Google Scholar, and industry news sites for keywords like "edge AI deployment," "tinyML trends," and "edge computing 2024."
3.  **Select Top N Sources:** From the search results, filter and select the top 5 academic papers and top 3 industry reports based on citation count, relevance, and publication date.
4.  **Summarize Each Source:** For each selected source, extract the abstract, key findings, and any quantitative data related to performance, adoption, or market size.
5.  **Compare Findings and Identify Trends/Gaps:** Synthesize the summaries into a single document. Cross-reference claims and data points to identify at least three consistent trends and two areas where research is lacking or findings are contradictory.
6.  **Draft Outline:** Structure the final report with an introduction, sections for each identified trend, a section on research gaps, and a conclusion.
7.  **Write the Report:** Write the full report based on the outline, ensuring every factual claim is linked to its source with an inline citation. Include a methodology note explaining the research and selection process.

**Execution Phase:**
With the plan in place, the agent begins to execute each step. It would call the necessary tools to perform searches, filter results, extract text, and so on. The agent works through the plan from step 1 to 7.

A key element of robust Plan-and-Execute systems is the use of **plan refinement triggers**. The agent does not blindly follow the plan if it hits a wall. Instead, it is designed to recognize specific failures that require it to pause execution and update the plan. Common triggers include:
*   **Missing Data:** A search returns no relevant results.
*   **Data Conflicts:** Two sources provide contradictory information (like the 40% vs. 25% adoption rates).
*   **Low-Quality Sources:** The initial sources are found to be outdated or not credible.

When a trigger is activated, the agent might re-enter the planning phase to revise the remaining steps before resuming execution.

The primary advantage of Plan-and-Execute is its structure, which improves efficiency and reliability for well-defined tasks. It is easier to estimate and bound the cost and time required, and the separation of concerns makes the system easier to debug and manage. However, its main drawback is a lack of flexibility. For highly exploratory or unpredictable problems, the initial plan may quickly become obsolete, requiring frequent and costly re-planning cycles. This rigidity can cause the agent to stick to a flawed plan, whereas a ReAct agent would have adapted more quickly.

These foundational patterns are not just academic exercises. They power real-world, large-scale systems like OpenAI's Deep Research, which operationalize iterative planning and verification to automate complex knowledge work.

## Where This Shows Up in Practice Deep Research–Style Systems

The principles of ReAct and Plan-and-Execute are the engine behind sophisticated AI systems designed for deep research. Products like OpenAI's Deep Research operationalize these planning and reasoning patterns to tackle long-horizon tasks that would take a human researcher hours or even days to complete [[30]](https://cdn.openai.com/deep-research-system-card.pdf).

These systems are designed to decompose a complex query, such as our "edge AI deployment" report, into a series of sub-goals. They then execute an iterative cycle of searching for information, reading and extracting content from various sources (including text, PDFs, and images), comparing claims, verifying facts, and progressively synthesizing the findings into a coherent, cited report [[27]](https://blog.promptlayer.com/how-deep-research-works).

To ensure reliability and reduce hallucinations, these systems are built with explicit policies and prompts that enforce verification. For example, when our research assistant agent encounters conflicting statistics on adoption rates, a deep research system is designed to recognize this conflict as a verification failure. It would then automatically initiate a new research cycle to find an authoritative source to resolve the discrepancy before including the information in its final report [[27]](https://blog.promptlayer.com/how-deep-research-works).

The architecture of these systems often blends both ReAct and Plan-and-Execute patterns. The overall process might resemble Plan-and-Execute, with an initial high-level plan to structure the research. However, each step of that plan, such as "Compare findings," might be executed as a series of smaller, ReAct-like loops where the agent iteratively searches, reads, and observes until that sub-goal is satisfied [[27]](https://blog.promptlayer.com/how-deep-research-works).

This hybrid approach demonstrates that these patterns are not mutually exclusive but are composable building blocks for creating sophisticated agents. As the underlying LLMs become more capable, some of this explicit orchestration is becoming more implicit, with models trained to generate separate "thinking" and "answer" streams natively.

## Modern Reasoning Models Thinking vs Answer Streams and Interleaved Thinking

The evolution of agentic patterns like ReAct and Plan-and-Execute has directly influenced how the next generation of LLMs are trained. Instead of relying solely on external scaffolding to separate thought from action, modern reasoning models are increasingly designed to perform this separation internally. This is achieved by training them to produce two distinct types of output: a private "thinking" stream and a public "answer" stream [[23]](https://cameronrwolfe.substack.com/p/demystifying-rethinking-models).

The thinking stream is analogous to the "Thought" step in ReAct. It contains the model's internal monologue, where it breaks down the problem, formulates a plan, and reasons through intermediate steps. This stream is not typically shown to the end-user but is crucial for the model's internal process and for developers to debug its behavior [[23]](https://cameronrwolfe.substack.com/p/demystifying-rethinking-models). The answer stream is the final, user-facing output, which is generated based on the conclusions reached in the thinking stream.

Some models adopt a "think first" approach, which mirrors the Plan-and-Execute pattern. The model generates a complete chain of thought in its private thinking stream before producing any part of the final answer [[22]](https://www.ibm.com/think/topics/reasoning-model). This ensures a full plan is in place before execution begins.

More advanced models now support **interleaved thinking**, which is a native implementation of the ReAct loop [[Interleaved Thinking for Reasoning LLMs]](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking). In this mode, the model can alternate between thinking, acting (e.g., calling a tool), and writing. For instance, after a tool call, the model can generate new private thinking tokens to process the tool's output and decide on the next step before continuing to write the final answer. This creates a much more dynamic and responsive reasoning process, allowing the model to adapt its plan based on intermediate results without needing an external loop to manage the flow [[Interleaved Thinking for Reasoning LLMs]](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking).

A recent innovation, called Asynchronous Reasoning, takes this a step further by allowing the thinking and answer streams to be generated concurrently [[21]](https://arxiv.org/html/2512.10931v1). The model can start writing its answer based on its initial thoughts while continuing to reason and refine its plan in the background. If the thinking process uncovers something that requires a change, it can pause or even correct the answer stream in real-time. This reduces latency and creates a more fluid, human-like interaction [[21]](https://arxiv.org/html/2512.10931v1).

What does this mean for you as an AI engineer? While these modern models internalize much of the planning logic, your role does not disappear. You may need to write less code to manage explicit loops, but you still need to provide high-quality prompts, well-defined tools, and robust guardrails to ensure the agent behaves reliably. The separation of reasoning and answering, whether managed externally or internally, remains a vital concept for debugging, controlling, and trusting your agent's behavior. With these powerful planning capabilities in place, agents can unlock even more advanced behaviors like goal decomposition and self-correction.

## Advanced Agent Capabilities Enabled by Planning Goal Decomposition and Self-Correction

Effective planning and reasoning are not just about following a sequence of steps; they are about creating and adapting that sequence. These capabilities unlock two of the most advanced behaviors in autonomous agents: goal decomposition and self-correction.

**Goal decomposition** is the ability to break down a large, ambiguous task into smaller, manageable sub-goals. For our research assistant agent, the initial goal—"produce a report on edge AI"—is too broad to be acted upon directly. An agent with planning capabilities can decompose this into a hierarchy of more specific goals: find sources, evaluate sources, synthesize findings, and write the report. This is often done implicitly during the "Thought" steps in a ReAct-style agent, where a well-crafted prompt can guide the model to think about the necessary sub-tasks.

**Self-correction** is the agent's ability to detect when something has gone wrong and adjust its plan accordingly. This is where the feedback loop in reasoning becomes critical. Let's return to our example of the conflicting adoption rates (40% vs. 25%). A non-reasoning agent might simply report both numbers or pick one at random. An agent capable of self-correction recognizes the contradiction as a failure state. It can then dynamically insert a new sub-goal into its plan: "verify the correct adoption rate." This might trigger a new action, like searching for a third-party market analysis to adjudicate the conflict, before it proceeds with the report [[aclanthology-org.md]](https://aclanthology.org/2025.acl-long.1104.pdf).

Even with powerful models that have built-in reasoning, understanding patterns like ReAct and Plan-and-Execute remains essential. These frameworks provide a clear mental model for how an agent should "think," which is invaluable for debugging when it behaves unexpectedly. They also give you the explicit control loops needed to enforce consistency and add guardrails.

In our next lesson, we will move from theory to practice by implementing the ReAct pattern from scratch. Soon after, we will explore the memory systems that allow agents to learn over time, the advanced retrieval techniques that power them with knowledge, and how to process multimodal data.

## Conclusion

In this lesson, we have established that planning and reasoning are the cognitive engines that elevate a simple tool-using LLM to a truly autonomous agent. We have seen that without these capabilities, models fail on complex tasks, producing superficial and unreliable results. By teaching models to think, first with Chain-of-Thought and then with more structured patterns like ReAct and Plan-and-Execute, we give them the ability to strategize, adapt, and correct their own mistakes.

We have explored the iterative loop of ReAct, ideal for exploratory tasks, and the structured approach of Plan-and-Execute, which brings efficiency to well-defined problems. We also saw how these foundational ideas have influenced the architecture of modern reasoning models, which now feature internal thinking streams and interleaved thought-action cycles. These patterns are more than just theory; they are the blueprints for building intelligent, reliable, and debuggable agents.

Now that you understand the "why" and "what" of agentic reasoning, it is time to get your hands dirty. In our next lesson, we will implement the ReAct pattern from scratch, giving you the practical skills to build an agent that can truly think for itself.

## References

- [1] [AI reasoning vs non-reasoning models: key differences explained](https://www.narrativa.com/ai-reasoning-vs-non-reasoning-models-key-differences-explained)
- [2] [Fundamental Scaling Limitations in AI Reasoning Models](https://www.kuppingercole.com/research/lb80993/fundamental-scaling-limitations-in-ai-reasoning-models)
- [3] [From LLM Reasoning to Autonomous AI Agents - arXiv](https://arxiv.org/html/2606.07462v1)
- [4] [A Practical Guide to Building Agents](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- [5] [Agent Laboratory: Using LLM Agents as Research Assistants](https://www.linkedin.com/posts/skphd_agent-laboratory-using-llm-agents-as-research-activity-7283233189651738625-q6xU)
- [6] [Chain-of-Thought and Planning Agents](https://www.emergentmind.com/topics/chain-of-thought-and-planning-agents)
- [7] [Guiding Agent Reasoning: Chain of Thought](https://apxml.com/courses/intro-llm-agents/chapter-5-basic-agent-planning/guiding-agent-reasoning-chain-of-thought)
- [8] [Step-by-step Problem Solving with Chain-of-Thought Reasoning](https://mbrenndoerfer.com/writing/step-by-step-problem-solving-chain-of-thought-reasoning)
- [9] [Chain-of-Thought Prompting: A Deep Dive](https://www.comet.com/site/blog/chain-of-thought-prompting)
- [10] [The promise and potential of chain-of-thought prompting](https://www.ibm.com/think/topics/chain-of-thoughts)
- [11] [The ReAct Pattern for LLM-Powered Agents](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents)
- [12] [The ReAct Pattern for Agents](https://apxml.com/courses/getting-started-with-llm-toolkit/chapter-8-developing-autonomous-agents/react-pattern-for-agents)
- [13] [What is the ReAct Loop in AI Agent Reasoning?](https://www.mindstudio.ai/blog/what-is-react-loop-ai-agent-reasoning)
- [14] [ReAct Agents](https://www.salesforce.com/agentforce/ai-agents/react-agents)
- [15] [ReAct Agent - IBM](https://www.ibm.com/think/topics/react-agent)
- [16] [Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks | OpenReview](https://openreview.net/forum?id=ybA4EcMmUZ)
- [17] [Asynchronous Reasoning: Training-Free Interactive Thinking LLMs](https://arxiv.org/html/2512.10931v1)
- [18] [Reasoning model - IBM](https://www.ibm.com/think/topics/reasoning-model)
- [19] [Demystifying Reasoning Models](https://cameronrwolfe.substack.com/p/demystifying-rethinking-models)
- [20] [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [21] [Asynchronous Reasoning: Training-Free Interactive Thinking LLMs](https://arxiv.org/html/2512.10931v1)
- [22] [Reasoning model - IBM](https://www.ibm.com/think/topics/reasoning-model)
- [23] [Demystifying Reasoning Models](https://cameronrwolfe.substack.com/p/demystifying-rethinking-models)
- [24] [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [25] [From LLM Reasoning to Autonomous AI Agents - arXiv](https://arxiv.org/html/2601.10825v1)
- [26] [From LLM Reasoning to Autonomous AI Agents - arXiv](https://arxiv.org/html/2603.28376v1)
- [27] [How OpenAI's Deep Research Works](https://blog.promptlayer.com/how-deep-research-works)
- [28] [OpenAI's Deep Research: Get Days of Human Work Done in Minutes](https://www.jonkrohn.com/posts/2025/3/17/openais-deep-research-get-days-of-human-work-done-in-minutes)
- [29] [Deep Research System Card](https://cdn.openai.com/deep-research-system-card.pdf)
- [30] [Deep Research System Card](https://cdn.openai.com/deep-research-system-card.pdf)
- [31] [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
- [32] [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
- [33] [Agentic Reasoning - IBM](https://www.ibm.com/think/topics/agentic-reasoning)
- [34] [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)
- [35] [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)
- [36] [Interleaved Thinking for Reasoning LLMs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking)
- [37] [Interleaved Thinking for Reasoning LLMs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking)
- [38] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)
- [39] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)
- [40] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)
- [41] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)
- [42] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)
- [43] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)
- [44] [aclanthology-org.md](https://aclanthology.org/2025.acl-long.1104.pdf)