# The Critical Decision: LLM Workflows vs. AI Agents

As an AI engineer preparing to build your first real AI application, after narrowing down the problem you want to solve, one key decision is how to design your AI solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach, where the LLM makes self-directed decisions along the way? Thus one of the fundamental questions that will determine the success or failure of your project is: How should you architect your AI system?

When building AI applications, engineers face this critical architectural decision early in their development process. Should you create a predictable, step-by-step workflow where you control every action, or should you build an autonomous agent that can think and decide for itself? This is one of the key decisions that will impact everything from development time and costs to reliability and user experience.

Choose the wrong approach, and you might end up with an overly rigid system that breaks when users deviate from expected patterns, or an unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most. You could waste months of development time rebuilding the entire architecture, leaving you with frustrated users and executives questioning the skyrocketing costs.

This is not a theoretical problem. In 2024 and 2025, we are seeing billion-dollar AI startups succeed or fail based primarily on this architectural decision [[50]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/). The successful teams and AI engineers know when to use workflows versus agents and, more importantly, how to combine both approaches effectively.

By the end of this lesson, we will provide you with a framework to make this critical decision confidently. You will understand the fundamental trade-offs between predefined LLM workflows and dynamic AI agents, see real-world examples from leading AI companies, and learn how to design systems that leverage the best of both worlds.

## Understanding the Spectrum: From Workflows to Agents

To make the right architectural choice, you first need to understand the two core methodologies for building AI applications: LLM workflows and AI agents. For now, we will focus less on the technical specifics and more on their properties and how they are used in practice.

An LLM workflow is a sequence of tasks involving one or more LLM calls, often combined with other operations like reading from a database or writing to a file system. The key characteristic of a workflow is that it is largely predefined and orchestrated by developer-written code. The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execution and explicit control flow [[51]](https://www.anthropic.com/engineering/building-effective-agents). Think of it like a factory assembly line: each station performs a specific, repeatable task in a set order. We will explore common workflow patterns like chaining, routing, and orchestrator-worker in future lessons.

Image 1: A flowchart illustrating a simple LLM workflow for document summarization using a map/reduce approach. This diagram emphasizes the predefined and orchestrated nature of LLM workflows.

AI agents, on the other hand, are systems where an LLM plays a central role in dynamically planning the sequence of steps, reasoning, and actions to achieve a goal [[52]](https://cloud.google.com/discover/what-are-ai-agents). The steps are not defined in advance but are decided by the agent based on the task and the current state of its environment. This makes agents adaptive and capable of handling novel situations. Their behavior is driven by the LLM's autonomy in decision-making. You can think of an agent as a skilled human expert tackling an unfamiliar problem, adapting their approach with each new piece of information. In upcoming lessons, we will dive deep into the components that make this possible, such as tools, memory, and the ReAct reasoning framework.

Image 2: Architecture diagram of a simple AI agent system. (Source [Unit 42, Palo Alto Networks](https://unit42.paloaltonetworks.com/agentic-ai-threats/))

Both workflows and agents require an orchestration layer to manage their execution. However, the nature of this layer differs significantly between the two. In a workflow, the orchestrator simply executes a predefined plan, like a script. For an agent, the orchestrator's role is more dynamic; it facilitates the LLM's ongoing planning and execution, providing the environment and resources the agent needs to operate autonomously. This distinction between developer-defined logic and LLM-driven autonomy is at the heart of the architectural decision you face.

## Choosing Your Path

Now that we have defined LLM workflows and AI agents, let's explore their core differences. The fundamental trade-off is between developer-defined logic, which offers control and predictability, and LLM-driven autonomy, which provides flexibility and adaptability [[53]](https://decodingml.substack.com/p/llmops-for-production-agentic-rag).

Workflows are ideal for tasks with a well-defined structure. This includes pipelines for data extraction from sources like Slack or Google Drive, automated generation of reports and emails, and content repurposing, such as turning articles into social media posts. Their primary strength is predictability. Because the steps are fixed, you get reliable and consistent results, which makes debugging and monitoring straightforward. This is particularly important in regulated fields like finance and healthcare, where accuracy and auditability are non-negotiable. Workflows are also a great choice for MVPs, as hardcoding the logic allows for rapid deployment. However, this rigidity is also a weakness. Workflows can be brittle, unable to handle unexpected user inputs, and adding new features can become complex over time.

Agents excel where workflows fall short: in open-ended and dynamic environments. Use cases like in-depth research on a broad topic, complex code debugging, or interactive customer support benefit from an agent's ability to adapt. The main strength of agents is their flexibility. They can handle ambiguity, learn from their interactions, and devise novel solutions to problems you did not anticipate. This power comes at a cost. Agents are inherently less predictable, which makes them harder to debug and evaluate. Their reliance on powerful, and often larger, LLMs for reasoning can lead to higher latency and operational costs [[50]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/). Furthermore, giving an autonomous system the ability to perform actions, especially write operations, introduces significant security risks if not managed carefully [[18]](https://unit42.paloaltonetworks.com/agentic-ai-threats/).

This isn’t just a theoretical weakness. Recent research systematically evaluated multi-agent systems and found they consistently degrade performance on tasks requiring sequential reasoning, where each step depends on the previous one. In some cases, performance dropped by as much as 70% compared to a single-agent system. Conversely, they excelled on tasks that could be broken down into parallel, independent sub-problems, like financial analysis [[58]](https://arxiv.org/html/2512.08296v1).

In reality, most production systems are not purely one or the other. This often involves strategically partitioning workloads; for example, compute-heavy tasks like model training are best handled by a centralized workflow, while real-time operations like a customer support chatbot benefit from distributed agents that operate with lower latency [[56]](https://agenticaiguide.ai/ch_3/sec_3-2.html). They exist on a spectrum, blending elements from both approaches to create hybrid solutions. Andrej Karpathy introduced the concept of an "autonomy slider," where you, the developer, decide how much control to give the LLM versus how much to retain in your code [[14]](https://singjupost.com/andrej-karpathy-software-is-changing-again/).

A practical design principle when working with this slider is to start with a simple, controllable workflow with frequent human-in-the-loop validation. You should only increase autonomy and move toward a more agentic approach when the task's complexity truly requires it, and even then, let the user control the level of freedom given to the AI [[57]](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy).

Excellent examples of this slider in action are modern coding assistants like Cursor and research tools like Perplexity [[10]](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6). In Cursor, the autonomy ranges from simple tab-completion (low autonomy) to letting an agent refactor the entire repository (high autonomy). Similarly, Perplexity offers a "quick search" (a simple workflow), a "research" mode, and a "deep research" mode that gives the AI more freedom to explore and synthesize information [[12]](https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx).

The goal is not to eliminate human oversight but to make the collaboration between human and AI more efficient. This is often described as the generation-verification loop: the AI generates a solution, and the human verifies its correctness. The faster this loop spins, the more productive the system becomes. Well-designed architectures and intuitive user interfaces, like the diff views in Cursor, are critical for speeding up this process [[54]](https://www.youtube.com/watch?v=LCEmiRjPEtQ).

Image 3: A circular flow diagram illustrating the iterative AI Generation and Human Verification Loop.

## Exploring Common Patterns

To build effective AI systems, it helps to be familiar with the common architectural patterns that have emerged. These patterns provide blueprints for structuring both workflows and agents. While we will cover them in detail in future lessons, let's build a high-level intuition for them now.

### LLM Workflow Patterns

Workflows are all about orchestrating LLM calls and other tools in a structured way. Here are a few foundational patterns.

**Chaining and routing** are used to automate sequences of LLM calls. Chaining involves linking the output of one LLM call to the input of the next, creating a multi-step process [[20]](https://mirascope.com/blog/llm-chaining). Routing adds a decision-making layer, where an LLM or a simple rule classifies an input and directs it to the appropriate chain [[21]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns). This allows you to handle different types of queries with specialized logic.

Image 4: A flowchart illustrating the Chaining and Routing workflow pattern with dynamic decision-making and sequential LLM task execution.

The **orchestrator-worker** pattern introduces more dynamic behavior. A central "orchestrator" LLM analyzes a user's request, breaks it down into sub-tasks, and delegates them to specialized "worker" agents or workflows [[25]](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/). The orchestrator then synthesizes the results from the workers to produce a final answer. This pattern is a stepping stone toward more agentic systems, as the orchestrator dynamically decides which actions to take [[26]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent).

Image 5: A hierarchical architecture diagram illustrating the Orchestrator-Worker workflow pattern.

The **evaluator-optimizer loop** is a pattern for self-correction. One LLM, the "generator," produces an initial output. A second LLM, the "evaluator," critiques this output based on a set of criteria and provides feedback [[30]](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html). This feedback, sometimes called a reflection, is sent back to the generator, which refines its output. This loop repeats until the output meets the desired quality or a set number of iterations is reached, mimicking how a human writer might revise a draft based on an editor's comments [[33]](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer).

Image 6: A feedback loop diagram illustrating the Evaluator-Optimizer workflow pattern.

### Core Components of a ReAct AI Agent

Nearly all modern agents are built using a pattern called ReAct, which stands for Reason and Act [[52]](https://cloud.google.com/discover/what-are-ai-agents). This framework enables an agent to reason about a task, decide on an action, take that action, and then observe the outcome to inform its next step. This iterative loop of thought, action, and observation is what gives agents their autonomous problem-solving abilities. We will explore the ReAct pattern in depth in Lessons 7 and 8, but for now, let's look at its core components.

The heart of a ReAct agent is an **LLM** that serves as its reasoning engine. It decides what to do, what tools to use, and how to interpret the results. To take action in the world, the agent is given access to **tools**. Common examples include calling external APIs, performing vector searches to retrieve information, browsing the web, running code interpreters, or interacting with databases [[59]](https://weaviate.io/blog/what-are-agentic-workflows). These are functions that allow it to interact with external systems, like searching the web, querying a database, or writing to a file. We will dedicate Lesson 6 to tools.

To maintain context, agents rely on **memory**. **Short-term memory**, or working memory, holds the history of the current conversation, including the agent's thoughts and the outcomes of its actions. It functions like a computer's RAM, providing immediate context for the task at hand. **Long-term memory** stores information across sessions, such as factual knowledge from documents or user preferences. This allows the agent to learn and personalize its responses over time. We will cover memory in detail in Lesson 9.

Image 7: An architecture diagram illustrating the core components and dynamics of a ReAct (Reason and Act) AI agent.

These patterns are the building blocks of modern AI engineering. Understanding them is the first step toward designing systems that are both powerful and reliable.

## Zooming In on Our Favorite Examples

To ground these concepts in reality, let's analyze three state-of-the-art systems: a simple workflow from Google Workspace, a single-agent coding assistant from Gemini, and a complex hybrid research agent from Perplexity. These examples showcase the spectrum of architectural choices and how they are applied to solve real-world problems.

### Document Summarization by Gemini in Google Workspace

When you are working in a team, finding the right document can be a time-consuming process. Many documents are long, making it difficult to quickly determine if they contain the information you need. An embedded summarization feature can guide your search and save valuable time.

The document summarization feature in Google Workspace is a perfect example of a pure, multi-step workflow [[2]](https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/). It follows a predictable, hardcoded sequence of LLM calls to process a document and present the results to the user.

Image 8: A flowchart illustrating the Document Summarization and Analysis Workflow by Gemini in Google Workspace.

The workflow is straightforward and effective. First, the system reads the content of the document. For long documents that exceed the LLM's context window, it employs a map-reduce strategy: the document is split into smaller chunks, each chunk is summarized in parallel, and then a final summary is generated from the individual summaries [[3]](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models). After summarization, another LLM call might extract key points or action items. The results are then saved and displayed to the user. Each step is clearly defined, making the process reliable and easy to manage.

### Gemini CLI Coding Assistant

Writing code is often a slow and meticulous process. It requires reading documentation, understanding new codebases, and mastering different programming languages. A coding assistant can dramatically speed up this process.

The Gemini CLI is an open-source tool that leverages a ReAct agent architecture to create a powerful single-agent system for coding [[5]](https://developers.google.com/gemini-code-assist/docs/gemini-cli). It allows developers to write code from scratch, get assistance on existing projects, and even generate documentation, all through a conversational interface. This approach is sometimes called "vibe coding," where the developer guides the AI with natural language prompts rather than writing every line of code manually [[54]](https://www.youtube.com/watch?v=LCEmiRjPEtQ).

Image 9: A circular flow diagram illustrating the operational loop of the Gemini CLI Coding Assistant, based on the ReAct pattern.

The agent operates in a loop that follows the ReAct pattern:

1.  **Context Gathering:** The agent starts by loading its context, which includes the directory structure of the codebase, the set of available tools, and the history of the current conversation [[40]](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/).
2.  **LLM Reasoning:** The Gemini model analyzes the user's request within this context and formulates a plan, deciding which tools to use to accomplish the task.
3.  **Human in the Loop:** Before executing any actions, the agent typically presents its plan to the user for validation, ensuring the developer remains in control.
4.  **Tool Execution:** Once approved, the agent executes the selected tools. These can range from file system operations (like reading a specific function with `grep`), to web searches for documentation, to code generation and execution for dynamic validation [[55]](https://github.com/google-gemini/gemini-cli/blob/main/README.md).
5.  **Evaluation:** The agent processes the output from the tools and, if code was generated, may attempt to run or compile it to check for correctness.
6.  **Loop Decision:** Based on the results, the agent determines if the task is complete. If not, it returns to the reasoning step to plan its next action, continuing the loop until the goal is achieved.

This iterative process of reasoning, acting, and observing allows the Gemini CLI to handle complex coding tasks that would be impossible with a simple, predefined workflow.

### Perplexity Deep Research

Researching a new topic can be a daunting task. It is often unclear where to start, which sources are reliable, and how to synthesize information from dozens of articles, papers, and videos. A research assistant that can quickly scan the internet and compile a comprehensive report is an incredibly powerful tool.

Perplexity's Deep Research feature is a sophisticated hybrid system that combines ReAct reasoning with the orchestrator-worker pattern to conduct autonomous, expert-level research [[8]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research). Unlike single-agent systems, it deploys multiple specialized agents that work in parallel, performing dozens of searches across hundreds of sources to generate detailed reports in just a few minutes [[6]](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/).

This multi-agent architecture is a deliberate choice for complex, decomposable problems like research. Studies show that while single agents struggle with sequential tasks, multi-agent systems with a central orchestrator excel at problems that can be broken down into parallel sub-tasks. The orchestrator can delegate, verify, and synthesize, which contains errors and leverages the power of parallel exploration [[58]](https://arxiv.org/html/2512.08296v1).

However, simply adding more agents is not a silver bullet. Studies have shown that there are diminishing returns, with performance often plateauing after 4-8 agents. Beyond that point, the cost of coordinating the agents outweighs the benefits of adding more "brainpower," leading to wasted resources [[60]](https://arxiv.org/html/2602.03794v1).

Image 10: A hierarchical and iterative flow diagram illustrating the Perplexity Deep Research process.

While Perplexity's exact implementation is closed-source, we can infer its likely architecture based on its behavior and industry best practices. Here is a simplified version of how it might work:

1.  **Research Planning & Decomposition:** An orchestrator agent analyzes the user's research question and breaks it down into a set of targeted sub-questions. This is a classic application of the orchestrator-worker pattern, where the main agent delegates tasks to a team of specialized sub-agents.
2.  **Parallel Information Gathering:** Each sub-question is assigned to a specialized search agent. These agents run in parallel, using tools like web search and document retrieval to gather as much relevant information as possible. By isolating the context for each agent, the system ensures that the LLMs remain focused and efficient.
3.  **Analysis & Synthesis:** Each agent independently validates and ranks its sources based on credibility and relevance. It then summarizes the top-ranked sources into a concise report for its specific sub-question.
4.  **Iterative Refinement & Gap Analysis:** The orchestrator collects the reports from all the worker agents and analyzes them to identify any knowledge gaps relative to the original research request. If gaps are found, it generates follow-up queries and repeats the process, iterating until the topic is fully covered or a maximum number of steps is reached.
5.  **Report Generation:** Finally, the orchestrator synthesizes the findings from all agents into a single, comprehensive report, complete with inline citations to ensure transparency and trust.

This hybrid approach, which combines the structured control of a workflow with the dynamic reasoning of multiple agents, allows Perplexity to tackle complex research tasks with a level of depth and speed that neither a pure workflow nor a single agent could achieve alone.

## Conclusion: The Challenges of Every AI Engineer

Now that you understand the spectrum from LLM workflows to AI agents, it is important to recognize that every AI Engineer—whether at a startup or a Fortune 500 company—faces these same architectural decisions. The choice between control and autonomy is a fundamental challenge that determines whether an AI application succeeds in production or becomes another failed experiment [[50]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/).

As you begin your journey, you will encounter a recurring set of engineering challenges:

-   **Unchecked Error Amplification:** Your agent works perfectly in demos but becomes unpredictable with real users. This is often due to error amplification, where a small mistake by one component gets magnified through a multi-step process. Research has shown that independent, uncoordinated agents can amplify errors by over 17 times compared to a single system, leading to catastrophic and costly failures [[58]](https://arxiv.org/html/2512.08296v1).
-   **The Tool-Coordination Trap:** As you add more tools and complexity to your system, the overhead required to coordinate multiple agents can start to outweigh the benefits. This is especially true for tool-heavy tasks, where the computational budget gets consumed by communication instead of reasoning, leading to a drop in performance [[58]](https://arxiv.org/html/2512.08296v1).
-   **Diminishing Returns at Scale:** The assumption that "more agents are better" is a dangerous one. In reality, performance often plateaus or even declines after adding a small number of agents (typically 4-8). The coordination costs start to exceed the marginal benefit, leading to a system that is more complex, more expensive, and less effective [[60]](https://arxiv.org/html/2602.03794v1).
-   **The Cost-Observability Trap:** Sophisticated agents deliver impressive results but can burn through tokens at an alarming rate. Once you hand over control to a reasoning loop, you lose visibility into how many steps it will take or how many tools it will call. Without specialized observability tools that can track agent-specific behavior, you are one bad prompt away from a massive, unexpected bill [[50]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/).
-   **Security Concerns:** Autonomous agents with powerful write permissions could send wrong emails, delete critical files, or expose sensitive data [[16]](https://permiso.io/blog/8-critical-ai-security-challenges).

The good news is that these challenges are solvable. In upcoming lessons, we will systematically tackle each of these issues. We will cover battle-tested patterns for building reliable products through specialized evaluation and monitoring pipelines, proven strategies for managing context in hybrid systems, and practical approaches for keeping costs and latency under control. In the next lesson, we will start with a foundational technique for building any reliable AI system: structured outputs.

By the end of this course, you will have the knowledge to architect AI systems that are not only powerful but also robust, efficient, and safe. You will know when to use a workflow, when to deploy an agent, and how to build effective hybrid systems that work in the messy, unpredictable real world.

## References

- [1] How does Gemini document summarization workflow operate in Google Workspace?. (n.d.). Google Docs Editors Help. [https://support.google.com/docs/answer/15627020?hl=en](https://support.google.com/docs/answer/15627020?hl=en)
- [2] New Google Workspace Gemini Feature: Your PDFs Now Write Their Own Summaries and Suggest Next Steps. (n.d.). Master Concept. [https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/](https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/)
- [3] Long document summarization with Workflows and Gemini models. (2024, April 30). Google Cloud Blog. [https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models)
- [4] Use Gemini in the Google Workspace side panel. (n.d.). Google Workspace Learning Center. [https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini](https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini)
- [5] Gemini CLI. (n.d.). Google for Developers. [https://developers.google.com/gemini-code-assist/docs/gemini-cli](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- [6] Perplexity Computer: Multi-Model Agent Orchestration. (n.d.). Zen van Riel. [https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/)
- [7] Perplexity Computer: The Future of AI Agent Orchestration. (n.d.). Gend.co. [https://www.gend.co/blog/perplexity-computer-ai-agent-orchestration](https://www.gend.co/blog/perplexity-computer-ai-agent-orchestration)
- [8] Introducing Perplexity Deep Research. (2025, February 14). Perplexity Blog. [https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [9] Perplexity Agent API Platform: A Developer's Guide to Building with the AI Search Engine. (n.d.). DigitalApplied. [https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide](https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide)
- [10] Andrej Karpathy on Software 3.0: Software in the Age of AI. (2025, June 20). Medium. [https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6)
- [11] Autonomy Sliders. (n.d.). Andrew Ships. [https://andrewships.substack.com/p/autonomy-sliders](https://andrewships.substack.com/p/autonomy-sliders)
- [12] Andrej Karpathy's latest talk describes our collective future. (2025, June 19). LinkedIn. [https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx](https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx)
- [13] S3#15 Andrej Karpathy - Building the AI Teacher. (n.d.). Latent Space. [https://www.latent.space/p/s3](https://www.latent.space/p/s3)
- [14] Andrej Karpathy: Software Is Changing (Again). (2025, June 20). The Singju Post. [https://singjupost.com/andrej-karpathy-software-is-changing-again/](https://singjupost.com/andrej-karpathy-software-is-changing-again/)
- [15] Asgari, A., Panichella, A., Derakhshanfar, P., & Olsthoorn, M. (2025). What Challenges Do Developers Face in AI Agent Systems? An Empirical Study on Stack Overflow & GitHub Issues. arXiv. [https://arxiv.org/html/2510.25423v2](https://arxiv.org/html/2510.25423v2)
- [16] 8 Critical AI Security Challenges & How to Solve Them. (n.d.). Permiso. [https://permiso.io/blog/8-critical-ai-security-challenges](https://permiso.io/blog/8-critical-ai-security-challenges)
- [17] Key Challenges in AI Agent Development (and How to Solve Them). (2024, May 1). Medium. [https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5)
- [18] AI Agents Are Here. So Are the Threats.. (2025, May 1). Unit 42, Palo Alto Networks. [https://unit42.paloaltonetworks.com/agentic-ai-threats/](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [19] The Agentic AI Revolution: 5 Unexpected Security Challenges. (2024, May 15). CyberArk. [https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges](https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges)
- [20] LLM Chaining: A Practical Guide for Developers. (n.d.). Mirascope. [https://mirascope.com/blog/llm-chaining](https://mirascope.com/blog/llm-chaining)
- [21] Issue 110: LLM Workflow Patterns. (n.d.). ML Pills. [https://mlpills.substack.com/p/issue-110-llm-workflow-patterns](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [22] Prompt Structure and Chaining for Advanced LLM Applications. (n.d.). Orq.ai. [https://orq.ai/blog/prompt-structure-chaining](https://orq.ai/blog/prompt-structure-chaining)
- [23] LLM Chains in Artificial Intelligence. (n.d.). GeeksforGeeks. [https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/](https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/)
- [24] Prompt Chaining. (n.d.). Prompting Guide. [https://www.promptingguide.ai/techniques/prompt_chaining](https://www.promptingguide.ai/techniques/prompt_chaining)
- [25] Building a Self-Healing AI Orchestrator with Reflexion Patterns. (n.d.). Stevens Institute of Technology. [https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/)
- [26] DIY #17: Orchestrator-Worker LLM Agent. (n.d.). ML Pills. [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [27] The Orchestrator-Worker Pattern is a well known design pattern for structuring multi-agent systems. (2024, May 22). LinkedIn. [https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL](https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL)
- [28] Orchestrator-workers. (n.d.). Anthropic. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [29] Agent Orchestration Patterns. (n.d.). GurusUp. [https://gurusup.com/blog/agent-orchestration-patterns](https://gurusup.com/blog/agent-orchestration-patterns)
- [30] Evaluator (reflect and refine) loop patterns. (n.d.). AWS Prescriptive Guidance. [https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html)
- [31] Building Self-Correcting LLM Systems: The Evaluator-Optimizer Pattern. (2024, May 22). DEV Community. [https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p](https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p)
- [32] The Research on LLM Self-Correction. (n.d.). Vadim.blog. [https://vadim.blog/the-research-on-llm-self-correction](https://vadim.blog/the-research-on-llm-self-correction)
- [33] Evaluator-optimizer. (n.d.). Anthropic. [https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer)
- [34] Evaluator-Optimizer LLM Workflow. (n.d.). Seb's Notes. [https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow](https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow)
- [35] Building effective agents. (2024, December 19). Anthropic. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [36] What is an AI agent?. (2026, April 2). Google Cloud. [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [37] Real Agents vs. Workflows: The Truth Behind AI 'Agents'. (2024, May 15). YouTube. [https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s)
- [38] Exploring the difference between agents and workflows. (n.d.). Decoding ML. [https://decodingml.substack.com/p/llmops-for-production-agentic-rag](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
- [39] A Developer’s Guide to Building Scalable AI: Workflows vs Agents. (2025, June 27). Towards Data Science. [https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)
- [40] How Gemini CLI builds context. (2025). Wietse Venema. [https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/)
- [41] How Do I Provide Context Files to Gemini CLI?. (n.d.). Milvus. [https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli](https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli)
- [42] GEMINI.md. (n.d.). Gemini CLI. [https://geminicli.com/docs/cli/gemini-md/](https://geminicli.com/docs/cli/gemini-md/)
- [43] Gemini CLI Tutorial Series Part 9: Understanding Context, Memory and Conversational Branching. (2024, May 15). Medium. [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)
- [44] A Look at Context Engineering in Gemini CLI. (n.d.). AI Positive. [https://aipositive.substack.com/p/a-look-at-context-engineering-in](https://aipositive.substack.com/p/a-look-at-context-engineering-in)
- [45] The Third Wave of Data Engineering. (2025, June 17). LinkedIn. [https://www.linkedin.com/posts/tracercloud_the-third-wave-of-data-engineering-activity-7417891798364168192-ZQJz](https://www.linkedin.com/posts/tracercloud_the-third-wave-of-data-engineering-activity-7417891798364168192-ZQJz)
- [46] How AI Models and Real-Time Monitoring Improve Energy Pipeline Health. (n.d.). Sandtech. [https://www.sandtech.com/insight/ai-models-real-time-monitoring-improve-energy-pipeline-health/](https://www.sandtech.com/insight/ai-models-real-time-monitoring-improve-energy-pipeline-health/)
- [47] Protecting AI Data Pipelines. (n.d.). Commvault. [https://www.commvault.com/use-cases/protecting-ai-data-pipelines](https://www.commvault.com/use-cases/protecting-ai-data-pipelines)
- [48] Machine Learning Monitoring Tools: Your Shield for AI Reliability. (n.d.). Lumenova.ai. [https://www.lumenova.ai/blog/machine-learning-monitoring-tools-ai-reliability/](https://www.lumenova.ai/blog/machine-learning-monitoring-tools-ai-reliability/)
- [49] Top 6 Data Pipeline Monitoring Tools. (n.d.). Integrate.io. [https://www.integrate.io/blog/data-pipeline-monitoring-tools/](https://www.integrate.io/blog/data-pipeline-monitoring-tools/)
- [50] Quach, H. (2025, June 27). A Developer’s Guide to Building Scalable AI: Workflows vs Agents. Towards Data Science. [https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)
- [51] Anthropic. (2024, December 19). Building effective agents. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [52] What is an AI agent?. (2026, April 2). Google Cloud. [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [53] Iusztin, P. (n.d.). Exploring the difference between agents and workflows. Decoding ML. [https://decodingml.substack.com/p/llmops-for-production-agentic-rag](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
- [54] Karpathy, A. (2025, June 20). Andrej Karpathy: Software Is Changing (Again) [Video]. YouTube. [https://www.youtube.com/watch?v=LCEmiRjPEtQ](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- [55] google-gemini/gemini-cli. (n.d.). GitHub. [https://github.com/google-gemini/gemini-cli/blob/main/README.md](https://github.com/google-gemini/gemini-cli/blob/main/README.md)
- [56] Balancing Centralized and Decentralized AI Workloads. (n.d.). Agentic AI Guide. [https://agenticaiguide.ai/ch_3/sec_3-2.html](https://agenticaiguide.ai/ch_3/sec_3-2.html)
- [57] AI Workflows vs Agents: The Autonomy Slider. (n.d.). Decoding AI. [https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)
- [58] Kim, Y., et al. (2025). Towards a Science of Scaling Agent Systems. arXiv. [https://arxiv.org/html/2512.08296v1](https://arxiv.org/html/2512.08296v1)
- [59] What are Agentic Workflows?. (n.d.). Weaviate. [https://weaviate.io/blog/what-are-agentic-workflows](https://weaviate.io/blog/what-are-agentic-workflows)
- [60] Wang, G., et al. (2026). An Information-Theoretic Explanation for Diminishing Returns in Scaling Multi-Agent Systems. arXiv. [https://arxiv.org/html/2602.03794v1](https://arxiv.org/html/2602.03794v1)