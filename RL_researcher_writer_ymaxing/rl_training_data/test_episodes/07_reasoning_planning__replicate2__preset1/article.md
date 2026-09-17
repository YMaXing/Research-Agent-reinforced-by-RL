# Lesson 7: Planning and Reasoning

In our previous lessons, we've assembled the essential components for building AI systems. We learned to distinguish between structured LLM workflows and autonomous AI agents in Lesson 2, manage the flow of information with context engineering in Lesson 3, and ensure reliable data extraction with structured outputs in Lesson 4. We even gave our systems the ability to act using tools in Lesson 6. Yet, an essential piece is missing. An LLM, by itself, is a powerful text generator, but it doesn't inherently know how to plan, adapt, or reason through a complex, multi-step task.

Simply giving an agent a set of tools is like handing a person a toolbox without any instructions. They might be able to hammer a nail, but they can't build a house. To move from simple actions to complex projects, an agent needs a "brain." This is a mechanism for planning and reasoning. This lesson introduces these foundational ingredients of agentic behavior. We will explore core strategies like ReAct and Plan-and-Execute that give agents the ability to think, decompose problems, and self-correct, transforming them from simple tools into capable partners.

In this lesson, we will cover:
- Why models without explicit reasoning fail at complex tasks.
- How Chain-of-Thought prompting teaches models to "think" and its limitations.
- The foundational patterns of ReAct and Plan-and-Execute.
- How these patterns appear in real-world systems.
- The evolution of reasoning in modern models.
- Advanced capabilities enabled by planning, such as goal decomposition and self-correction.

## What a Non-Reasoning Model Does And Why It Fails on Complex Tasks

To understand the need for planning, let's consider a "Technical Research Assistant Agent." Its goal is to produce a comprehensive report on the "Latest developments in edge AI deployment." This involves finding recent papers, summarizing their findings, identifying trends, and writing a structured report.

A non-reasoning model, when given this task, treats it as a single, large text generation problem. It tries to "answer" the request in one go. It might call the right tools, perhaps searching for papers and then summarizing them, but it does so without a coherent, adaptive strategy. It follows a pre-conceived pattern without analyzing the results of its actions.

This approach quickly breaks down when faced with complexity. The agent might produce a superficial summary because it doesn't have an internal goal to cross-reference multiple sources. It won't iterate on its findings or verify conflicting information because it lacks a mechanism to analyze its own outputs. Since there is no explicit breakdown of sub-goals, it often misses critical steps. The performance of such an agent drops, often misunderstanding the task's intent or stopping too early. These models rely on pattern matching and often fail on unfamiliar tasks, lacking the ability to adapt beyond their training data [[1]](https://arxiv.org/html/2606.07462v1), [[2]](https://www.narrativa.com/ai-reasoning-vs-non-reasoning-models-key-differences-explained).

As we saw in previous lessons, LLM workflows and structured outputs provide modularity and reliability for predictable processes. Tools give our systems the ability to act. However, for complex tasks where adaptation is key—the very tasks where agents excel—this is not enough. To address this, we must first teach the model to create a reasoning trace before it provides an answer.

## Teaching Models to “Think” Chain-of-Thought and Its Limits

The first step toward more intelligent agents was teaching models to "think" before they act. This is the core idea behind Chain-of-Thought (CoT) prompting. Just as humans often talk themselves through a problem, we can instruct an LLM to write down its reasoning steps before giving the final answer [[3]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). This simple technique provides a primitive form of planning.

For our Technical Research Assistant Agent, a CoT prompt might look like this: *"Before answering, think step by step about how you will research and verify sources on edge AI deployment. Then provide the final report."*

The model would first generate a high-level plan, something like:
1.  Search for recent papers on edge AI deployment from reputable sources.
2.  Read the abstracts to identify the most relevant ones.
3.  Compare the findings and identify common trends and conflicts.
4.  Synthesize the information into a structured report.

This is a marked improvement. The model is no longer just reacting; it's formulating a strategy. However, CoT has its limits. The reasoning trace and the final answer are generated together as a single block of text, which is difficult to parse and control programmatically. More importantly, the model typically generates the plan once and then follows it. It doesn't create an iterative loop where it can act, observe the result, and then refine its plan. CoT is a heuristic that guides the LLM, but it's not a sophisticated planning algorithm that can explore alternatives or backtrack from dead ends [[4]](https://apxml.com/courses/intro-llm-agents/chapter-5-basic-agent-planning/guiding-agent-reasoning-chain-of-thought).

Furthermore, generating these extra reasoning steps is slower and uses more tokens, which increases API costs [[5]](https://mbrenndoerfer.com/writing/step-by-step-problem-solving-chain-of-thought-reasoning). The reasoning can also be verbose when a quick answer is all that's needed, and it doesn't guarantee correctness. A model can produce a detailed, logical-sounding explanation that still leads to the wrong answer [[6]](https://www.comet.com/site/blog/chain-of-thought-prompting). To gain more structure and control, we need to separate the act of planning from the act of answering.

## Separating Planning from Answering Foundations of ReAct and Plan-and-Execute

The next logical step in agent design is to create a clear separation between planning and execution. Instead of generating a single, monolithic block of text that mixes thought and action, we ask the model to perform these as two distinct steps, either interleaved or in separate phases.

This separation is the foundation for two of the most influential patterns in agent architecture: ReAct and Plan-and-Execute.

-   **ReAct (Reason + Act)** interleaves `Thought`, `Action`, and `Observation` in a tight loop. The agent thinks, acts, sees what happens, and then thinks again.
-   **Plan-and-Execute** separates the process into two distinct phases. First, the agent creates a comprehensive plan. Then, it executes that plan step-by-step.

These two patterns are foundational, but they are part of a broader family of agentic strategies. Other notable approaches include Tree-of-Thoughts, where an agent explores multiple reasoning paths in parallel, and Reflexion, where an agent critiques its own past actions to refine its strategy for future attempts [[7]](https://medium.com/@nraman.n6/architectural-taxonomy-of-modern-ai-systems-modular-vertical-agentic-and-hybrid-implementations-5f3f0f0d95b9).

This separation provides clear benefits. It gives us greater control and makes the agent's behavior more interpretable. We can inspect the plan before it's executed and analyze the reasoning behind each action. Most importantly, it enables iterative loops. An observation from the environment, such as a search result or an error message, can be fed back into the model to update its plan. This feedback loop is what allows an agent to adapt and recover from mistakes.

First, we will explore the ReAct pattern in more detail.

## ReAct in Depth Loop, Evolving Example, Pros and Cons

The ReAct pattern emerged to bridge the gap between the internal, ungrounded reasoning of Chain-of-Thought and the blind, reactive nature of action-only models. It was inspired by the synergy between reasoning and acting in human problem-solving [[8]](https://arxiv.org/pdf/2210.03629), [[9]](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models). The core idea is to create an iterative loop where the model generates a reasoning trace (`Thought`), then an `Action` to take, and finally receives an `Observation` from the environment. This observation then informs the next `Thought`, creating a dynamic feedback cycle [[10]](https://apxml.com/courses/getting-started-with-llm-toolkit/chapter-8-developing-autonomous-agents/react-pattern-for-agents).

### The ReAct Loop

At its heart, ReAct operates as a simple state machine that cycles through three phases: thinking, acting, and observing. This loop continues until the agent determines it has reached a final answer or hits a predefined limit.

```mermaid
flowchart LR
  Thought["Thought"] --> Action["Action"]
  Action --> Observation["Observation"]
  Observation --> Thought
  Thought --> FinalAnswer["Final Answer"]
```
Image 1: Flowchart illustrating the iterative ReAct loop.

### Evolving Example

Let's see how our Technical Research Assistant Agent would use the ReAct loop to complete its task.

*   **Step 1**
    *   **Thought:** I need to find recent, trustworthy sources on edge AI deployment. I should start by searching for survey papers and industry reports from the last year.
    *   **Action:** `search("latest developments in edge AI deployment 2024 site:arxiv.org OR site:acm.org")`
    *   **Observation:** A list of 10 papers is returned, including titles, authors, and abstracts.

*   **Step 2**
    *   **Thought:** The search returned several promising papers. I will select the top 3 based on their titles and abstracts, prioritizing those that mention performance metrics and real-world case studies.
    *   **Action:** `fetch_and_extract(urls=["arxiv.org/abs/2401.1234", "acm.org/doi/10.1145/12345"])`
    *   **Observation:** The full text of two papers and an abstract for the third are extracted.

*   **Step 3**
    *   **Thought:** I have the content of the papers. Now I need to summarize each one and identify key claims, particularly regarding adoption rates. I will look for conflicting information.
    *   **Action:** `summarize_and_compare(texts=[paper1_text, paper2_text])`
    *   **Observation:** "Paper A claims a 40% adoption rate in manufacturing. Paper B, a survey from a different region, reports a 25% adoption rate."

*   **Step 4**
    *   **Thought:** I have detected a conflict in the adoption rates. This is a critical point that needs to be resolved. I should search for a third-party market analysis to verify these claims.
    *   **Action:** `search("edge AI deployment adoption rate market analysis 2024")`
    *   **Observation:** A report from a major analyst firm is found, which explains the regional differences in adoption rates.

*   **Step 5**
    *   **Thought:** The market analysis report clarifies the discrepancy. I can now synthesize my findings, explain the different adoption rates, and identify trends and gaps. I have enough information to write the final report.
    *   **Action:** `finish(report_text="...")`

### Pros and Cons

This example shows the power of the ReAct loop. The agent is not just following a static plan; it is actively reasoning, gathering information, and adapting its strategy based on what it learns. The main advantages of this pattern are its high interpretability and its natural ability to handle errors and unexpected outcomes. The `Observation` step is particularly effective at reducing hallucinations, as it forces the model to ground its internal reasoning against external, factual information. This feedback loop helps constrain the model's responses to what can be verified, minimizing the generation of incorrect or unfounded information. It is particularly well-suited for exploratory tasks where the path to the solution is not clear from the start [[11]](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents), [[12]](https://arxiv.org/html/2507.22915v1).

However, this flexibility comes with major trade-offs. The most immediate is token efficiency. Because the entire history of thoughts, actions, and observations is included in the prompt for each new step, the context window grows linearly. This increases both latency and cost, and for very long tasks, it can exceed the model's context limit or run into the "lost-in-the-middle" problem where the model forgets early information. Another major challenge is error propagation. If an early action returns incorrect information, that error can cascade through all subsequent steps, as the agent tends to trust its own trajectory. The system is also constrained by action space rigidity; it can only use the tools it's been given and can't invent new ones on the fly. Finally, its performance is heavily dependent on retrieval quality. If the search tool provides noisy or misleading results, the agent's reasoning will be built on a flawed foundation [[11]](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents).

For tasks where the overall structure is more predictable, the Plan-and-Execute pattern can offer a more efficient and reliable alternative.

## Plan-and-Execute in Depth Plan, Execution, Pros and Cons

The Plan-and-Execute approach offers a more structured alternative to ReAct. Instead of interleaving thought and action at each step, this pattern separates the entire process into two distinct phases: first, the agent generates a comprehensive, high-level plan, and second, it executes that plan step-by-step. This separation allows the model to balance high-level objectives with low-level execution details. The architecture is often compared to a kitchen, where a head chef creates the high-level meal plan and line cooks execute the specific tasks [[13]](https://openreview.net/forum?id=ybA4EcMmUZ).

```mermaid
flowchart LR
  A["Planning Phase"]
  B["Execution Phase"]

  A -- "generates comprehensive plan" --> B
```
Image 2: A flowchart depicting the Plan-and-Execute approach with two distinct phases: Planning and Execution.

Let's revisit our Technical Research Assistant Agent to see how it would operate using this pattern.

### The Planning Phase

The agent is first prompted to generate a detailed, step-by-step plan to accomplish the goal. The output of this phase is not an action, but the plan itself. This planning phase is critical, but also challenging. Generating accurate plans is difficult because LLMs are not inherently trained for this specific task. To overcome this, some systems use synthetic data generation methods to fine-tune a dedicated "Planner" model. This involves taking successful action trajectories from a baseline model and using another powerful LLM to annotate them with high-level plans. These annotated trajectories then become the training data for the planner [[13]](https://openreview.net/forum?id=ybA4EcMmUZ).

*   **Planner Output:**
    1.  **Define Scope:** Identify the key areas to cover in the report: recent advancements, key technologies, adoption trends, challenges, and future outlook.
    2.  **Source Identification:** Perform targeted searches on academic databases (arXiv, Google Scholar) and industry news sites for documents published in the last 18 months.
    3.  **Source Selection:** From the search results, select the 5 most relevant and credible sources, prioritizing a mix of survey papers, case studies, and market reports.
    4.  **Information Extraction:** For each selected source, extract key findings, statistics, and conclusions related to the defined scope.
    5.  **Synthesis and Analysis:** Consolidate the extracted information, compare findings across sources, identify common trends, and note any contradictions or gaps.
    6.  **Outline Generation:** Create a structured outline for the final report based on the synthesized information.
    7.  **Report Writing:** Write the full report following the outline, ensuring all claims are supported by citations.

### The Execution Phase

Once the plan is generated, an "executor" agent (or a series of tool calls) begins to carry out each step. The executor focuses on a single task at a time, translating the high-level plan into environment-specific actions and using the plan as its guide.

1.  The executor runs `search("review paper edge AI deployment 2023-2024")`.
2.  It then runs `search("industry report edge AI market trends 2024")`.
3.  Based on the results, it selects the top 5 URLs and calls `fetch_and_extract()` for each.
4.  It passes the extracted texts to a `summarize()` tool.
5.  It synthesizes the summaries, perhaps using another LLM call with a specific prompt for this task.
6.  Finally, it generates the outline and then the full report.

Unlike ReAct, where the plan evolves with each step, the Plan-and-Execute model follows a more rigid path. Re-planning is a crucial component, but it's handled differently. Some systems trigger re-planning only when a step fails or returns an unexpected result. More dynamic implementations involve the planner updating the plan after each execution step, allowing for continuous adaptation to new information. This is especially important in dynamic environments where the state can change unexpectedly. In these cases, the agent must continuously receive feedback and adjust its plan accordingly, which might involve revising goals or changing the sequence of actions [[14]](https://openreview.net/forum?id=ybA4EcMmUZ), [[15]](https://www.anthropic.com/engineering/building-effective-agents).

### Pros and Cons

The primary advantage of this approach is its efficiency and predictability, especially for well-defined tasks. By creating a plan upfront, the agent can reduce the number of LLM calls and avoid getting sidetracked. This makes it easier to estimate the cost and time required for a task and allows for clearer ownership of stages in a development pipeline. However, this rigidity is also its main drawback. The pattern is less suited for highly exploratory problems where the path forward is unknown. If the initial plan is flawed, the agent may waste resources executing it before realizing a course correction is needed. If the environment is highly dynamic, the need for frequent re-planning can negate the initial efficiency gains, making the process nearly as iterative as ReAct but with more structural overhead [[15]](https://www.anthropic.com/engineering/building-effective-agents).

## Where This Shows Up in Practice Deep Research–Style Systems

The planning and reasoning patterns we've discussed are not just theoretical constructs; they are the engines behind powerful, real-world AI systems. A prime example is what we can call "deep research" systems, which are designed to tackle complex, long-horizon research tasks that can take a human researcher hours or even days to complete [[16]](https://www.jonkrohn.com/posts/2025/3/17/openais-deep-research-get-days-of-human-work-done-in-minutes).

These systems operationalize the iterative cycles of planning, acting, and verification at a large scale. When tasked with a complex query, a deep research agent decomposes it into a series of sub-goals. For our Technical Research Assistant Agent, this might involve dozens of micro-cycles: searching for a paper, reading its abstract, deciding if it's relevant, extracting key statistics, cross-verifying those stats with another source, and updating an internal summary or knowledge base [[17]](https://blog.promptlayer.com/how-deep-research-works).

Many of these systems are built on a ReAct-like loop, using strong system prompts and a rich set of tools to guide the agent's behavior. They often include explicit policies to enforce verification and reduce hallucinations, such as requiring multiple sources for any factual claim. Others are closer to a Plan-and-Execute model, where an initial research strategy is formulated and then executed, with periodic checkpoints to allow for re-planning if the agent hits a dead end or uncovers conflicting information [[17]](https://blog.promptlayer.com/how-deep-research-works).

The success of these systems shows that while the underlying patterns are simple, their power comes from robust implementation with well-defined tools, clear error handling, and effective state management. However, these long-horizon systems face major scalability challenges. As the agent interacts with its environment, its interaction history grows, leading to context overload that can cause it to lose track of the original goal. Furthermore, in a long chain of steps, a single local failure can cascade and derail the entire plan, a problem known as error propagation [[18]](https://www.emergentmind.com/topics/long-horizon-agent-planning). As models become more capable, some of this explicit orchestration is becoming more implicit, with models generating separate "thinking" and "answer" streams.

## Modern Reasoning Models Thinking vs Answer Streams and Interleaved Thinking

As LLMs have evolved, they have started to internalize some of the planning and reasoning structures that we previously had to engineer with explicit prompts and loops. Many modern reasoning models are now specifically trained to separate their internal thought process from their final output, a feature often described as having a private "thinking" stream and a public "answer" stream [[19]](https://www.ibm.com/think/topics/reasoning-model), [[20]](https://cameronrwolfe.substack.com/p/demystifying-reasoning-models).

### Private Thinking and Public Answers

This logical separation is fundamental. The model first generates a long chain of thought—often in a special `<think>` block—where it breaks down the problem, explores different approaches, and refines its plan. Only after this internal reasoning is complete does it generate the final, user-facing answer. This "think-first" approach allows the model to spend more computational effort on complex problems, which has been shown to yield substantial performance improvements on reasoning tasks [[19]](https://www.ibm.com/think/topics/reasoning-model), [[20]](https://cameronrwolfe.substack.com/p/demystifying-reasoning-models).

For the user, this process can be either hidden or presented as a summarized "thinking..." step, similar to what you might see in ChatGPT. This behavior is often a result of the training process, which may use reinforcement learning with specific rewards for both accuracy and correct output formatting. For example, the DeepSeek-R1 model was developed using a multi-stage process that combined supervised fine-tuning (SFT) on Chain-of-Thought data with reinforcement learning. The RL stage used rewards for accuracy, format (e.g., correctly using `<think>` tags), and consistency. In some cases, this reasoning ability can even emerge from pure reinforcement learning without any supervised fine-tuning, as researchers observed an "Aha!" moment where a model began to spontaneously generate reasoning traces [[3]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

### Interleaved Thinking

An even more advanced capability is **interleaved thinking**, which is particularly useful for agents that use tools. With interleaved thinking, the model doesn't just think once at the beginning. Instead, it can generate a `thought`, call a `tool`, receive the `result`, and then generate *another* `thought` to process that result before deciding on the next action or producing the final answer. This allows the agent to reason about the output of its actions in real-time, creating a more dynamic and responsive loop that closely mirrors the ReAct pattern, but is built into the model's behavior. This is a native feature in some modern models, where the entire assistant turn, including multiple tool calls and the reasoning in between, is treated as a single conceptual response [[21]](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking).

### Asynchronous Reasoning

Taking this a step further, some models support **asynchronous reasoning**. This training-free approach allows an LLM to think, write its public response, and process new user inputs concurrently. It works by using the geometric properties of rotary positional embeddings to manage three separate token streams (private thoughts, public response, and user input) and make the model perceive them as a single, contiguous sequence. The model can even be prompted to decide for itself when to pause writing its response to dedicate more time to thinking. This dramatically reduces the delay a user experiences, as the time to the first audible or visible token can drop from minutes to seconds [[22]](https://arxiv.org/html/2512.10931v1).

What does this mean for us as AI engineers? While these increasingly sophisticated models handle more of the reasoning process internally, it doesn't make the patterns we've discussed obsolete. We still need to provide clear instructions, well-defined tools, and robust guardrails. The separation of reasoning and answering, even when handled by the model, remains a powerful concept for debugging and maintaining control. Understanding the underlying logic of ReAct and Plan-and-Execute helps us design better prompts and interpret the behavior of even the most advanced agents. With these foundational planning and reasoning capabilities in place, agents can perform more advanced behaviors like goal decomposition and self-correction.

## Advanced Agent Capabilities Enabled by Planning Goal Decomposition and Self-Correction

Effective planning and reasoning enable agents to create and adapt their own workflows. This leads to two critical capabilities: goal decomposition and self-correction.

**Goal decomposition** is the ability to break a large task into smaller, manageable sub-goals. This concept has deep roots in classical AI planning, which used algorithms to decompose goals into executable steps. In a ReAct-style agent, this often happens implicitly within the `Thought` steps, as the agent reasons about what to do next. In Plan-and-Execute agents, it's an explicit part of the initial planning phase. Prompts can be designed to encourage more detailed decomposition, improving the agent's ability to handle complex, multi-part tasks [[23]](https://arxiv.org/html/2503.12687v1).

**Self-correction** is the agent's ability to detect when something has gone wrong and adjust its plan. This is where the feedback loop becomes critical. Returning to our example of conflicting adoption rates (40% vs. 25%), an agent capable of self-correction recognizes the contradiction. It can then insert a new "verification" sub-goal into its plan, search for an authoritative source, and use that new information to resolve the conflict before proceeding. This can be enhanced by training models with reinforcement learning on data that includes both incorrect attempts and their corrections, teaching the model to self-verify and refine its solutions [[24]](https://aclanthology.org/2025.acl-long.1104.pdf).

Even with powerful models that have built-in reasoning, explicit patterns like ReAct and Plan-and-Execute remain valuable. They provide a clear structure for debugging, ensure consistency, and give us a shared mental model of how the agent is "thinking." They are the scaffolding that allows us to build reliable and predictable systems.

These concepts are the core of agentic AI. In the next lesson, Lesson 8, we will implement the ReAct pattern from scratch. Soon after, we will explore how agents remember information with memory systems in Lesson 9, how they retrieve external knowledge in our RAG deep dive in Lesson 10, and how they handle complex data formats in Lesson 11.

## Conclusion

In this lesson, we explored the shift from simple instruction-following to dynamic planning and reasoning. We saw that without these capabilities, LLMs fail on complex tasks that require adaptation and multi-step execution. Foundational patterns like Chain-of-Thought, ReAct, and Plan-and-Execute provide the structure needed to transform LLMs from mere text generators into capable, autonomous agents.

Understanding these patterns is not just an academic exercise. They are the building blocks for creating robust, interpretable, and effective AI systems. As we move forward in this course, these concepts will be the foundation upon which we build more advanced agents with memory, knowledge, and the ability to interact with a complex, multimodal world.

## References

- [1] https://arxiv.org/html/2606.07462v1
- [2] https://www.narrativa.com/ai-reasoning-vs-non-reasoning-models-key-differences-explained
- [3] https://magazine.sebastianraschka.com/p/understanding-reasoning-llms
- [4] https://apxml.com/courses/intro-llm-agents/chapter-5-basic-agent-planning/guiding-agent-reasoning-chain-of-thought
- [5] https://mbrenndoerfer.com/writing/step-by-step-problem-solving-chain-of-thought-reasoning
- [6] https://www.comet.com/site/blog/chain-of-thought-prompting
- [7] https://medium.com/@nraman.n6/architectural-taxonomy-of-modern-ai-systems-modular-vertical-agentic-and-hybrid-implementations-5f3f0f0d95b9
- [8] https://arxiv.org/pdf/2210.03629
- [9] https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models
- [10] https://apxml.com/courses/getting-started-with-llm-toolkit/chapter-8-developing-autonomous-agents/react-pattern-for-agents
- [11] https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents
- [12] https://arxiv.org/html/2507.22915v1
- [13] https://openreview.net/forum?id=ybA4EcMmUZ
- [14] https://openreview.net/forum?id=ybA4EcMmUZ
- [15] https://www.anthropic.com/engineering/building-effective-agents
- [16] https://www.jonkrohn.com/posts/2025/3/17/openais-deep-research-get-days-of-human-work-done-in-minutes
- [17] https://blog.promptlayer.com/how-deep-research-works
- [18] https://www.emergentmind.com/topics/long-horizon-agent-planning
- [19] https://www.ibm.com/think/topics/reasoning-model
- [20] https://cameronrwolfe.substack.com/p/demystifying-reasoning-models
- [21] https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking
- [22] https://arxiv.org/html/2512.10931v1
- [23] https://arxiv.org/html/2503.12687v1
- [24] https://aclanthology.org/2025.acl-long.1104.pdf
- [25] https://www.kuppingercole.com/research/lb80993/fundamental-scaling-limitations-in-ai-reasoning-models
- [26] https://developers.openai.com/api/docs/guides/reasoning-best-practices
- [27] https://www.linkedin.com/posts/skphd_agent-laboratory-using-llm-agents-as-research-activity-7283233189651738625-q6xU
- [28] https://www.emergentmind.com/topics/chain-of-thought-and-planning-agents
- [29] https://www.ibm.com/think/topics/chain-of-thoughts
- [30] https://www.mindstudio.ai/blog/what-is-react-loop-ai-agent-reasoning
- [31] https://www.salesforce.com/agentforce/ai-agents/react-agents
- [32] https://www.ibm.com/think/topics/react-agent
- [33] https://www.ibm.com/think/topics/agentic-reasoning
- [34] https://www.ibm.com/think/topics/ai-agent-orchestration
- [35] https://arxiv.org/pdf/2504.19678
- [36] https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality
- [37] https://cdn.openai.com/deep-research-system-card.pdf
- [38] https://blogs.nvidia.com/blog/reasoning-ai-agents-decision-making/
- [39] https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- [40] https://www.ibm.com/think/topics/ai-agent-planning
- [41] https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- [42] https://arxiv.org/html/2601.10825v1
- [43] https://arxiv.org/html/2603.28376v1
- [44] https://www.ibm.com/think/topics/tree-of-thoughts