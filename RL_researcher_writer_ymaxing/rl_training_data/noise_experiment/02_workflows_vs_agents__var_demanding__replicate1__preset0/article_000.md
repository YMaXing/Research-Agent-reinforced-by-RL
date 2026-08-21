# LLM Workflows vs. AI Agents: The Critical Decision Every AI Engineer Faces

As an AI engineer preparing to build your first real AI application, after narrowing down the problem you want to solve, one key decision is how to design your AI solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach, where the LLM makes self-directed decisions along the way? This fundamental question will determine the success or failure of your project: How should you architect your AI system?

When building AI applications, engineers face this critical architectural decision early in their development process. Choosing the wrong approach can lead to an overly rigid system that breaks when users deviate from expected patterns, or an unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most. It can mean months of development time wasted rebuilding the entire architecture, frustrated users who cannot rely on the application, and executives who cannot afford to keep the system running as costs spiral out of control.

In 2024 and 2025, billion-dollar AI startups are succeeding or failing based primarily on this architectural decision. The most successful AI engineers and teams understand when to use workflows versus agents and, more importantly, how to combine both approaches effectively.

By the end of this lesson, we will provide you with a framework to confidently make this critical decision. You will understand the fundamental trade-offs between orchestrated workflows and autonomous agents, see real-world examples from leading AI companies, and learn how to design robust systems that leverage the best of both worlds.

## Understanding the Spectrum: From Workflows to Agents

To make the right architectural choice, you first need a clear understanding of what LLM workflows and AI agents are. While the terms are often used interchangeably, they represent two distinct approaches to building AI systems. Let's look at their properties and how they are used, without getting lost in technical specifics for now.

### LLM Workflows

An LLM workflow is a sequence of tasks involving LLM calls or other operations, such as reading from a database or writing to a file system. It is largely predefined and orchestrated by developer-written code. The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execution and explicit control flow. Think of it like a factory assembly line: each station performs a specific, repeatable task in a set order to produce a consistent output.![Image 1: A simple LLM workflow for document summarization and analysis in Google Workspace.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/document-summarization-workflow.png)

Image 1: A simple LLM workflow for document summarization and analysis in Google Workspace.

This structured approach is the backbone of many reliable AI applications today. In future lessons, we will explore core workflow patterns like chaining, routing, and the orchestrator-worker model in detail.

### AI Agents

In contrast, an AI agent is a system where an LLM plays a central role in dynamically planning the sequence of steps, reasoning, and actions required to achieve a goal. The steps are not defined in advance but are decided by the agent based on the task and the current state of its environment. This makes agents adaptive and capable of handling novel situations. An agent is like a skilled human expert tackling an unfamiliar problem, adapting their approach with each new piece of information.![Image 2: Core components and dynamics of a ReAct (Reason and Act) AI agent.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/react-agent-components.png)

Image 2: Core components and dynamics of a ReAct (Reason and Act) AI agent.

This autonomy is powered by core components like tools (actions), memory, and reasoning frameworks like ReAct, which we will cover in depth in upcoming lessons.

### The Role of Orchestration

Both workflows and agents require an orchestration layer, but its function is fundamentally different in each. In a workflow, the orchestrator is like a conductor following a musical score, executing a predefined plan step-by-step. In an agentic system, the orchestrator acts more like a jazz band leader, facilitating the LLM's dynamic planning and execution, allowing for improvisation and adaptation as the task unfolds. The key difference lies in who is in control: the developer's code or the LLM's reasoning.

## Choosing Your Path

We have defined LLM workflows and AI agents independently. Now, let's explore their core difference: developer-defined logic versus LLM-driven autonomy. Most real-world systems are not purely one or the other; they exist on a spectrum. The choice is about finding the right point on this gradient for your specific use case [[2]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/), [[3]](https://www.anthropic.com/engineering/building-effective-agents).![Image 3: The spectrum from structured workflows to autonomous agents, highlighting the trade-off between reliability and the agent's level of control. (Source [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)))](https://user-images.githubusercontent.com/28654329/281313759-3a31593c-2350-4824-9b2e-0672808c1f0b.png)

Image 3: The spectrum from structured workflows to autonomous agents, highlighting the trade-off between reliability and the agent's level of control. (Source [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag))

### When to Use LLM Workflows

Workflows are the default choice for tasks with a well-defined structure. If you can map out the steps required to solve a problem, a workflow is almost always the more reliable and efficient option.

Common use cases include pipelines for data extraction from sources like Slack, Zoom, or Google Drive; automated generation of reports or emails; and content repurposing, such as turning an article into social media posts. For instance, Gemini's document summarization feature in Google Workspace is a pure, multi-step workflow [[1]](https://support.google.com/docs/answer/15627020?hl=en).

**Strengths:**
Workflows are predictable and reliable. Since the execution path is fixed, debugging is straightforward. This predictability also applies to cost and latency, making them easier to manage in production. You can often use smaller, specialized models for specific sub-tasks, which reduces infrastructure overhead and operational costs.

**Weaknesses:**
The main drawback of workflows is their rigidity. They cannot handle unexpected scenarios, and adding new features can become complex as the application grows. Development time can also be longer, as each step must be manually engineered.

This predictability makes workflows the preferred choice in enterprise settings and regulated fields like finance and healthcare, where accuracy and auditability are non-negotiable. They are also ideal for building Minimum Viable Products (MVPs), where hardcoding features allows for rapid deployment.

### When to Use AI Agents

Agents are best suited for open-ended problems where the solution path is not known in advance. They excel at tasks that require dynamic problem-solving, exploration, and adaptation.

Examples include open-ended research and synthesis, such as investigating a broad topic like World War II; complex customer support that requires back-and-forth dialogue; and interactive tasks in unfamiliar environments, like booking a flight without specifying which websites to use.

**Strengths:**
The primary strength of agents is their flexibility. They can adapt to new information and handle ambiguity, allowing them to tackle complex problems that are impossible to script in advance.

**Weaknesses:**
This autonomy comes at a cost. Agents are non-deterministic, which means their performance, latency, and cost can vary with each run, making them less reliable. They often require larger, more expensive models to power their reasoning capabilities. A single agentic call can involve multiple LLM calls for planning and tool use, further increasing costs. Security is also a major concern; an agent with write permissions could potentially delete critical data or send inappropriate communications if not properly sandboxed [[18]](https://unit42.paloaltonetworks.com/agentic-ai-threats/). Finally, debugging and evaluating agents is notoriously difficult. Some developers have even joked about agents from Replit or Anthropic deleting their entire codebase, saying, "Anyway, I wanted to start a new project."

### Hybrid Approaches and the Autonomy Slider

Most production systems are not purely one or the other but are hybrids that blend both approaches. Andrej Karpathy introduced the concept of an "autonomy slider," where you, the developer, decide how much control to give the LLM versus the user [[14]](https://singjupost.com/andrej-karpathy-software-is-changing-again/).

For example, the coding assistant Cursor offers different levels of autonomy. You can use simple tab-completion (low autonomy), ask it to edit a selected block of code (medium autonomy), or give it a high-level task to execute across the entire repository (high autonomy) [[10]](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6). Similarly, Perplexity offers "Quick Search" (a simple workflow), "Research," and "Deep Research" (progressively more agentic) [[11]](https://andrewships.substack.com/p/autonomy-sliders).

The ultimate goal is to accelerate the continuous loop between AI generation and human verification. This is often achieved through a combination of well-designed architecture and a thoughtful user interface that allows for easy human oversight.![Image 4: A flowchart illustrating the continuous loop between AI generation and human verification, with the goal of speeding up the loop.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/ai-human-verification-loop.png)

Image 4: A flowchart illustrating the continuous loop between AI generation and human verification, with the goal of speeding up the loop.

## Exploring Common Patterns

To build an intuition for AI engineering, let's explore some of the most common patterns used to construct both workflows and agents. We will cover these in detail in future lessons, but for now, we will focus on the high-level concepts.

### LLM Workflow Patterns

Workflows are built by composing different patterns to automate multi-step tasks.

**Chaining and routing** are foundational patterns for automating multiple LLM calls. A chain links a sequence of LLM calls, where the output of one step becomes the input for the next. A router acts as a decision point, guiding the workflow down different paths based on the input or intermediate results. This allows you to glue together multiple LLM calls and decide between different options as the task progresses [[21]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns/).![Image 5: A flowchart illustrating the Chaining and Routing pattern for LLM workflows, showing an initial input, a routing decision, various LLM calls and sub-chains, and the final output.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/chaining-routing-pattern.png)

Image 5: A flowchart illustrating the Chaining and Routing pattern for LLM workflows, showing an initial input, a routing decision, various LLM calls and sub-chains, and the final output.

The **orchestrator-worker** pattern provides a more dynamic way to structure workflows. In this pattern, a central "orchestrator" LLM analyzes the user's intent, breaks down the task into smaller sub-tasks, and delegates them to specialized "worker" LLMs. A final "synthesizer" LLM then combines the results into a cohesive answer. This pattern makes a smooth transition between the workflow and agentic worlds by allowing the system to dynamically decide what actions to take [[25]](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/), [[26]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent).![Image 6: Flowchart illustrating the Orchestrator-Worker pattern](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/orchestrator-worker-pattern.png)

Image 6: Flowchart illustrating the Orchestrator-Worker pattern

The **evaluator-optimizer loop** is a pattern used to auto-correct and refine the output from an LLM. It works by using a second "evaluator" LLM to review the output of the first "generator" LLM. The evaluator provides feedback, often called a reflection, which is then passed back to the generator to improve its next attempt. This loop continues until the output meets a predefined quality standard, similar to how a human writer refines a document based on an editor's feedback [[30]](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html).![Image 7: A flowchart illustrating the Evaluator-Optimizer Loop pattern.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/evaluator-optimizer-loop.png)

Image 7: A flowchart illustrating the Evaluator-Optimizer Loop pattern.

### Core Components of a ReAct AI Agent

Almost all modern agents in the industry are built using the **ReAct (Reason and Act)** pattern, which has shown the most promise for building autonomous systems. The core idea is simple: the agent repeatedly cycles through a loop of reasoning about what to do next, taking an action, and observing the outcome [[5]](https://developers.google.com/gemini-code-assist/docs/gemini-cli).

This loop is powered by a few key components:
*   **Reasoning LLM**: This is the "brain" of the agent. It analyzes the task, plans the next step, and interprets the results of actions.
*   **Actions (Tools)**: These are the "hands" of the agent, allowing it to interact with the external world. Actions can be anything from searching the web to querying a database or writing to a file. We will cover tools in detail in Lesson 6.
*   **Short-Term Memory**: This is the agent's working memory, comparable to a computer's RAM. It holds the context of the current conversation, including past actions and observations.
*   **Long-Term Memory**: This provides the agent with persistent knowledge. It can include factual data about the world (semantic memory) and information about past interactions or user preferences (episodic memory). We will explore memory in Lesson 9.![Image 8: A flowchart illustrating the core components and dynamics of a ReAct (Reason and Act) AI agent.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/react-agent-dynamics.png)

Image 8: A flowchart illustrating the core components and dynamics of a ReAct (Reason and Act) AI agent.

Together, these components allow a ReAct agent to autonomously decide what action to take, interpret the output, and repeat the process until its goal is complete. We will dive much deeper into ReAct agents in Lessons 7 and 8.

## Zooming In on Our Favorite Examples

To anchor these concepts in the real world, let's analyze a few state-of-the-art systems, from a simple workflow to a complex hybrid agent. We will keep these explanations high-level, focusing on the architectural patterns rather than the technical details.

### Simple Workflow: Gemini in Google Workspace

**Problem:** When working in teams, finding the right information in a sea of documents can be a time-consuming process. Many documents are long, making it difficult to quickly determine if they contain what you are looking for. An embedded summarization tool can guide your search and save valuable time.

The document summarization feature in Google Workspace is a perfect example of a pure, simple workflow [[1]](https://support.google.com/docs/answer/15627020?hl=en). It follows a predefined chain of LLM calls to process a document without any dynamic decision-making.

The workflow looks like this:
1.  **Read Document**: The system ingests the content of the selected document.
2.  **Summarize**: An LLM call generates a concise summary of the text.
3.  **Extract Key Points**: Another LLM call identifies the most important takeaways.
4.  **Save Results**: The summary and key points are stored.
5.  **Show Results**: The generated content is displayed to the user.

This is a classic map-reduce approach, where the document is broken down, processed in stages, and the results are aggregated [[3]](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models). It is predictable, reliable, and efficient for this specific task.![Image 9: A flowchart illustrating a simple LLM workflow for document summarization and analysis in Google Workspace.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/document-summarization-workflow.png)

Image 9: A flowchart illustrating a simple LLM workflow for document summarization and analysis in Google Workspace.

### AI Agent: Gemini CLI Coding Assistant

**Problem:** Writing code is a slow and often tedious process. It involves reading dense documentation, navigating unfamiliar codebases, and learning new programming languages. A coding assistant can act as a pair programmer, dramatically speeding up development.

The open-source Gemini CLI is a great example of a single-agent system that uses the ReAct architecture to help developers with coding tasks [[43]](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43). It can write code from scratch (a practice known as "vibe coding"), assist with specific functions, generate documentation, and help you quickly get up to speed on new projects.

Based on our research, here is a high-level overview of its operational loop:
1.  **Context Gathering**: The agent starts by loading its context, which includes the directory structure of the codebase, a list of available tools, and the history of the current conversation [[40]](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/), [[44]](https://aipositive.substack.com/p/a-look-at-context-engineering-in).
2.  **LLM Reasoning**: The Gemini model analyzes the user's request and the current context to create a plan of action.
3.  **Human in the Loop**: Before executing any code, the agent presents its plan to the user for validation.
4.  **Tool Execution**: Once approved, the agent executes the selected tools. These can include file system operations (like reading code with `grep`), web searches (for documentation), and code generation or interpretation. The results of these actions are added to the conversation history.
5.  **Evaluation**: The agent dynamically evaluates the generated code, for instance by compiling or running it, to check for errors.
6.  **Loop Decision**: Finally, the agent decides if the task is complete or if it needs to repeat the cycle to refine its work.

This ReAct loop allows the Gemini CLI to function as an autonomous assistant, taking on complex coding tasks with minimal human intervention.![Image 10: A flowchart illustrating the operational loop of the Gemini CLI coding assistant, based on the ReAct pattern.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/gemini-cli-loop.png)

Image 10: A flowchart illustrating the operational loop of the Gemini CLI coding assistant, based on the ReAct pattern.

### Hybrid System: Perplexity Deep Research

**Problem:** Researching a new topic can be daunting. It is hard to know where to start, which sources to trust, and how to synthesize information from dozens of articles, papers, and videos. A research assistant that can quickly scan the internet and compile a comprehensive report is a powerful tool for learning.

Perplexity's Deep Research agent is a fascinating hybrid system that combines the structured planning of workflows with the dynamic reasoning of ReAct agents to perform expert-level autonomous research [[8]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research). Unlike the single-agent Gemini CLI, this system uses multiple specialized agents orchestrated in parallel by a workflow. It performs dozens of searches across hundreds of sources to create detailed reports in just a few minutes.

While Perplexity's exact implementation is closed-source, based on our research, here is an oversimplified look at how it might work:
1.  **Research Planning & Decomposition**: An orchestrator agent analyzes the user's research question and breaks it down into a set of targeted sub-questions. This is a classic example of the orchestrator-worker pattern.
2.  **Parallel Information Gathering**: To move faster, specialized search agents are deployed in parallel, each tackling a single sub-question. These agents use tools like web search and document retrieval to gather as much relevant information as possible. Because each agent has a narrow focus, its context is smaller, which helps the LLM stay on task.
3.  **Analysis & Synthesis**: Each agent validates its sources, scoring them for credibility and relevance. The top-ranked sources are then summarized into a report for that sub-question.
4.  **Iterative Refinement & Gap Analysis**: The orchestrator gathers the reports from all the worker agents and analyzes them to identify any knowledge gaps. If gaps are found, it generates follow-up queries and repeats the process. This loop continues until the research is complete or a maximum number of iterations is reached.
5.  **Report Generation**: Finally, the orchestrator combines the results from all the agents into a single, comprehensive report with inline citations.

This hybrid approach allows the Deep Research agent to combine structured planning with dynamic adaptation, creating a system that is both powerful and efficient.![Image 11: Flowchart illustrating Perplexity's Deep Research agent's iterative multi-step process.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/perplexity-deep-research-process.png)

Image 11: Flowchart illustrating Perplexity's Deep Research agent's iterative multi-step process.

## The Challenges of Every AI Engineer

Now that you understand the spectrum from LLM workflows to AI agents, it is important to recognize that every AI engineer—whether at a startup or a Fortune 500 company—faces these same fundamental challenges when designing a new AI application. The architectural decisions you make will determine whether your product succeeds in production or fails spectacularly [[15]](https://arxiv.org/html/2510.25423v2).

Here are some of the daily battles every AI engineer faces:
*   **Reliability Issues:** Your agent works perfectly in demos but becomes unpredictable with real users. LLM reasoning failures can compound through multi-step processes, leading to unexpected and costly outcomes [[17]](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5).
*   **Context Limits:** Systems struggle to maintain coherence across long conversations, gradually losing track of their purpose. Ensuring consistent output quality across different agent specializations presents a continuous challenge.
*   **Data Integration:** Building pipelines to pull information from Slack, web APIs, and databases is complex. You must also ensure that only high-quality data is passed to your AI system, because as the saying goes: garbage-in, garbage-out.
*   **Cost-Performance Trap:** Sophisticated agents can deliver impressive results, but they can also cost a fortune per user interaction, making them economically unfeasible for many applications.
*   **Security Concerns:** Autonomous agents with powerful write permissions could send the wrong emails, delete critical files, or expose sensitive data without robust safeguards in place [[19]](https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges).

The good news is that these challenges are solvable. In the upcoming lessons, we will systematically tackle each of these issues. We will cover patterns for building reliable products through specialized evaluation and monitoring pipelines, strategies for building hybrid systems, and ways to keep costs and latency under control.

Your path forward as an AI engineer is about mastering these realities. By the end of this course, you will have the knowledge to architect AI systems that are not only powerful but also robust, efficient, and safe. You will know when to use a workflow, when to deploy an agent, and how to build effective hybrid systems that work in the messy, unpredictable real world. In our next lesson, we will explore structured outputs, a key technique for making LLM responses reliable and machine-readable.

## References

- [1] Google. (n.d.). *Summarize a document*. Google Docs Help. [https://support.google.com/docs/answer/15627020?hl=en](https://support.google.com/docs/answer/15627020?hl=en)
- [2] Quach, H. (2025, June 27). *A Developer’s Guide to Building Scalable AI: Workflows vs Agents*. Towards Data Science. [https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)
- [3] Anthropic. (2024, December 19). *Building effective agents*. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [4] Google Cloud. (n.d.). *What is an AI agent?*. [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [5] Google for Developers. (n.d.). *Gemini CLI*. [https://developers.google.com/gemini-code-assist/docs/gemini-cli](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- [6] Iusztin, P. (2024, July 29). *Real Agents vs. Workflows: The Truth Behind AI 'Agents'* [Video]. YouTube. [https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s)
- [7] Iusztin, P. (2024, August 26). *Exploring the difference between agents and workflows*. Decoding ML. [https://decodingml.substack.com/p/llmops-for-production-agentic-rag](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
- [8] Perplexity Team. (2025, February 14). *Introducing Perplexity Deep Research*. Perplexity Blog. [https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [9] Iusztin, P. (2024, September 2). *Stop Building AI Agents: Here’s what you should build instead*. Decoding ML. [https://decodingml.substack.com/p/stop-building-ai-agents](https://decodingml.substack.com/p/stop-building-ai-agents)
- [10] Pouladian, B. (2025, June 20). *Andrej Karpathy on Software 3.0: Software in the Age of AI*. Medium. [https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6)
- [11] Ships, A. (2025, June 21). *Autonomy Sliders*. Substack. [https://andrewships.substack.com/p/autonomy-sliders](https://andrewships.substack.com/p/autonomy-sliders)
- [12] Latent Space. (2025, June 20). *S3: The Shift from Software 2.0 to 3.0*. [https://www.latent.space/p/s3](https://www.latent.space/p/s3)
- [13] Karpathy, A. (2025, June 18). *Software Is Changing (Again)* [Video]. YouTube. [https://www.youtube.com/watch?v=LCEmiRjPEtQ](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- [14] Pangambam S. (2025, June 20). *Andrej Karpathy: Software Is Changing (Again)*. The Singju Post. [https://singjupost.com/andrej-karpathy-software-is-changing-again/](https://singjupost.com/andrej-karpathy-software-is-changing-again/)
- [15] Asgari, A., Panichella, A., Derakhshanfar, P., & Olsthoorn, M. (2025). *What Challenges Do Developers Face in AI Agent Systems? An Empirical Study on Stack Overflow & GitHub Issues*. arXiv. [https://arxiv.org/html/2510.25423v2](https://arxiv.org/html/2510.25423v2)
- [16] Permiso. (n.d.). *8 Critical AI Security Challenges*. [https://permiso.io/blog/8-critical-ai-security-challenges](https://permiso.io/blog/8-critical-ai-security-challenges)
- [17] Roy, A. (2024, July 15). *Key Challenges in AI Agent Development and How to Solve Them*. Medium. [https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5)
- [18] Chen, J., & Lu, R. (2025, May 1). *AI Agents Are Here. So Are the Threats*. Unit 42. [https://unit42.paloaltonetworks.com/agentic-ai-threats/](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [19] CyberArk. (n.d.). *The Agentic AI Revolution: 5 Unexpected Security Challenges*. [https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges](https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges)
- [20] Mirascope. (n.d.). *LLM Chaining*. [https://mirascope.com/blog/llm-chaining](https://mirascope.com/blog/llm-chaining)
- [21] Andrès, D. (2024, August 28). *Issue #110 - LLM Workflow Patterns*. mlpills. [https://mlpills.substack.com/p/issue-110-llm-workflow-patterns](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [22] Orq.ai. (n.d.). *Prompt Structure & Chaining*. [https://orq.ai/blog/prompt-structure-chaining](https://orq.ai/blog/prompt-structure-chaining)
- [23] GeeksforGeeks. (n.d.). *LLM Chains*. [https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/](https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/)
- [24] Prompting Guide. (n.d.). *Prompt Chaining*. [https://www.promptingguide.ai/techniques/prompt_chaining](https://www.promptingguide.ai/techniques/prompt_chaining)
- [25] Stevens Institute of Technology. (n.d.). *Building Self-Healing AI with Orchestrator-Reflexion Patterns*. [https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/)
- [26] Andrès, D. (2024, September 4). *DIY #17 - Orchestrator-Worker LLM Agent*. mlpills. [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [27] F., S. (2025, July 1). *The orchestrator-worker pattern is a well-known design pattern...*. LinkedIn. [https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL](https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL)
- [28] Anthropic. (n.d.). *Patterns for Building with Agents: Orchestrator-Workers*. Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [29] Gurusup. (n.d.). *Agent Orchestration Patterns*. [https://gurusup.com/blog/agent-orchestration-patterns](https://gurusup.com/blog/agent-orchestration-patterns)
- [30] AWS. (n.d.). *Agentic AI Patterns: Evaluator, Reflect, and Refine Loop Patterns*. [https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html)
- [31] Roach, C. (2024, May 22). *Building Self-Correcting LLM Systems: The Evaluator-Optimizer Pattern*. DEV Community. [https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p](https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p)
- [32] Ilievski, V. (2024, July 10). *The Research on LLM Self-Correction*. Vadim's Blog. [https://vadim.blog/the-research-on-llm-self-correction](https://vadim.blog/the-research-on-llm-self-correction)
- [33] Anthropic. (n.d.). *Patterns for Building with Agents: Evaluator-Optimizer*. Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer)
- [34] G, S. (2024, July 15). *Evaluator-Optimizer LLM Workflow*. Substack. [https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow](https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow)
- [35] Laforge, G., & Spruyt, R. (2024, April 30). *Long document summarization with Workflows and Gemini models*. Google Cloud Blog. [https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models)
- [36] Google. (n.d.). *Google Workspace with Gemini*. [https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini](https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini)
- [37] Master Concept. (n.d.). *New Google Workspace Gemini Feature: Your PDFs Now Write Their Own Summaries*. [https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/](https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/)
- [38] Liu, J. (2023, October 9). *Building Production-Ready RAG Applications* [Video]. YouTube. [https://www.youtube.com/watch?v=TRjq7t2Ms5I](https://www.youtube.com/watch?v=TRjq7t2Ms5I)
- [39] Mullen, T., & Salva, R. J. (2025, June 25). *Gemini CLI: your open-source AI agent*. The Keyword. [https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [40] Veenema, W. (2025, June 26). *How Gemini CLI builds context*. [https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/)
- [41] Milvus. (n.d.). *How do I provide context files to Gemini CLI?*. [https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli](https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli)
- [42] Gemini CLI Docs. (n.d.). *GEMINI.md*. [https://geminicli.com/docs/cli/gemini-md/](https://geminicli.com/docs/cli/gemini-md/)
- [43] Google Cloud. (2025, July 1). *Gemini CLI Tutorial Series Part 9: Understanding Context, Memory, and Conversational Branching*. Medium. [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)
- [44] AI Positive. (2025, July 3). *A Look at Context Engineering in Gemini CLI*. Substack. [https://aipositive.substack.com/p/a-look-at-context-engineering-in](https://aipositive.substack.com/p/a-look-at-context-engineering-in)
- [45] Digital Applied. (n.d.). *Perplexity Agent API Platform: AI Search Developer Guide*. [https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide](https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide)
- [46] Renner, M., & Chaban, M. A. V. (2026, April 22). *1,302 real-world gen AI use cases from the world's leading organizations*. Google Cloud Blog. [https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- [47] OpenAI. (2025, July 17). *Introducing ChatGPT agent: bridging research and action*. [https://openai.com/index/introducing-chatgpt-agent/](https://openai.com/index/introducing-chatgpt-agent/)
- [48] tracer.cloud. (2025, July 25). *The third wave of data engineering...*. LinkedIn. [https://www.linkedin.com/posts/tracercloud_the-third-wave-of-data-engineering-activity-7417891798364168192-ZQJz](https://www.linkedin.com/posts/tracercloud_the-third-wave-of-data-engineering-activity-7417891798364168192-ZQJz)
- [49] Commvault. (n.d.). *Protecting AI data pipelines*. [https://www.commvault.com/use-cases/protecting-ai-data-pipelines](https://www.commvault.com/use-cases/protecting-ai-data-pipelines)
- [50] Lumenova. (n.d.). *Machine Learning Monitoring Tools for AI Reliability*. [https://www.lumenova.ai/blog/machine-learning-monitoring-tools-ai-reliability/](https://www.lumenova.ai/blog/machine-learning-monitoring-tools-ai-reliability/)
- [51] Google. (n.d.). *Gemini CLI*. GitHub. [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)# LLM Workflows vs. AI Agents: The Critical Decision Every AI Engineer Faces

As an AI engineer preparing to build your first real AI application, after narrowing down the problem you want to solve, one key decision is how to design your AI solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach, where the LLM makes self-directed decisions along the way? This fundamental question will determine the success or failure of your project: How should you architect your AI system?

When building AI applications, engineers face this critical architectural decision early in their development process. Choosing the wrong approach can lead to an overly rigid system that breaks when users deviate from expected patterns, or an unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most. It can mean months of development time wasted rebuilding the entire architecture, frustrated users who cannot rely on the application, and executives who cannot afford to keep the system running as costs spiral out of control.

In 2024 and 2025, billion-dollar AI startups are succeeding or failing based primarily on this architectural decision. The most successful AI engineers and teams understand when to use workflows versus agents and, more importantly, how to combine both approaches effectively.

By the end of this lesson, we will provide you with a framework to confidently make this critical decision. You will understand the fundamental trade-offs between orchestrated workflows and autonomous agents, see real-world examples from leading AI companies, and learn how to design robust systems that leverage the best of both worlds.

## Understanding the Spectrum: From Workflows to Agents

To make the right architectural choice, you first need a clear understanding of what LLM workflows and AI agents are. While the terms are often used interchangeably, they represent two distinct approaches to building AI systems. Let's look at their properties and how they are used, without getting lost in technical specifics for now.

### LLM Workflows

An LLM workflow is a sequence of tasks involving LLM calls or other operations, such as reading from a database or writing to a file system. It is largely predefined and orchestrated by developer-written code. The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execution and explicit control flow. Think of it like a factory assembly line: each station performs a specific, repeatable task in a set order to produce a consistent output [[2]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/), [[3]](https://www.anthropic.com/engineering/building-effective-agents).![Image 1: A simple LLM workflow for document summarization and analysis in Google Workspace.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/document-summarization-workflow.png)

Image 1: A simple LLM workflow for document summarization and analysis in Google Workspace.

This structured approach is the backbone of many reliable AI applications today. In future lessons, we will explore core workflow patterns like chaining, routing, and the orchestrator-worker model in detail.

### AI Agents

In contrast, an AI agent is a system where an LLM plays a central role in dynamically planning the sequence of steps, reasoning, and actions required to achieve a goal. The steps are not defined in advance but are decided by the agent based on the task and the current state of its environment. This makes agents adaptive and capable of handling novel situations. An agent is like a skilled human expert tackling an unfamiliar problem, adapting their approach with each new piece of information [[4]](https://cloud.google.com/discover/what-are-ai-agents).![Image 2: Core components and dynamics of a ReAct (Reason and Act) AI agent.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/react-agent-components.png)

Image 2: Core components and dynamics of a ReAct (Reason and Act) AI agent.

This autonomy is powered by core components like tools (actions), memory, and reasoning frameworks like ReAct, which we will cover in depth in upcoming lessons.

### The Role of Orchestration

Both workflows and agents require an orchestration layer, but its function is fundamentally different in each. In a workflow, the orchestrator is like a conductor following a musical score, executing a predefined plan step-by-step. In an agentic system, the orchestrator acts more like a jazz band leader, facilitating the LLM's dynamic planning and execution, allowing for improvisation and adaptation as the task unfolds. The key difference lies in who is in control: the developer's code or the LLM's reasoning.

## Choosing Your Path

We have defined LLM workflows and AI agents independently. Now, let's explore their core difference: developer-defined logic versus LLM-driven autonomy. Most real-world systems are not purely one or the other; they exist on a spectrum. The choice is about finding the right point on this gradient for your specific use case [[2]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/), [[3]](https://www.anthropic.com/engineering/building-effective-agents).![Image 3: The spectrum from structured workflows to autonomous agents, highlighting the trade-off between reliability and the agent's level of control. (Source [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag))](https://user-images.githubusercontent.com/28654329/281313759-3a31593c-2350-4824-9b2e-0672808c1f0b.png)

Image 3: The spectrum from structured workflows to autonomous agents, highlighting the trade-off between reliability and the agent's level of control. (Source [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag))

### When to Use LLM Workflows

Workflows are the default choice for tasks with a well-defined structure. If you can map out the steps required to solve a problem, a workflow is almost always the more reliable and efficient option.

Common use cases include pipelines for data extraction from sources like Slack, Zoom, or Google Drive; automated generation of reports or emails; and content repurposing, such as turning an article into social media posts. For instance, Gemini's document summarization feature in Google Workspace is a pure, multi-step workflow [[1]](https://support.google.com/docs/answer/15627020?hl=en).

**Strengths:**
Workflows are predictable and reliable. Since the execution path is fixed, debugging is straightforward. This predictability also applies to cost and latency, making them easier to manage in production. You can often use smaller, specialized models for specific sub-tasks, which reduces infrastructure overhead and operational costs.

**Weaknesses:**
The main drawback of workflows is their rigidity. They cannot handle unexpected scenarios, and adding new features can become complex as the application grows. Development time can also be longer, as each step must be manually engineered.

This predictability makes workflows the preferred choice in enterprise settings and regulated fields like finance and healthcare, where accuracy and auditability are non-negotiable. They are also ideal for building Minimum Viable Products (MVPs), where hardcoding features allows for rapid deployment.

### When to Use AI Agents

Agents are best suited for open-ended problems where the solution path is not known in advance. They excel at tasks that require dynamic problem-solving, exploration, and adaptation.

Examples include open-ended research and synthesis, such as investigating a broad topic like World War II; complex customer support that requires back-and-forth dialogue; and interactive tasks in unfamiliar environments, like booking a flight without specifying which websites to use.

**Strengths:**
The primary strength of agents is their flexibility. They can adapt to new information and handle ambiguity, allowing them to tackle complex problems that are impossible to script in advance.

**Weaknesses:**
This autonomy comes at a cost. Agents are non-deterministic, which means their performance, latency, and cost can vary with each run, making them less reliable. They often require larger, more expensive models to power their reasoning capabilities. A single agentic call can involve multiple LLM calls for planning and tool use, further increasing costs. Security is also a major concern; an agent with write permissions could potentially delete critical data or send inappropriate communications if not properly sandboxed [[18]](https://unit42.paloaltonetworks.com/agentic-ai-threats/). Finally, debugging and evaluating agents is notoriously difficult. Some developers have even joked about agents from Replit or Anthropic deleting their entire codebase, saying, "Anyway, I wanted to start a new project."

### Hybrid Approaches and the Autonomy Slider

Most production systems are not purely one or the other but are hybrids that blend both approaches. Andrej Karpathy introduced the concept of an "autonomy slider," where you, the developer, decide how much control to give the LLM versus the user [[14]](https://singjupost.com/andrej-karpathy-software-is-changing-again/).

For example, the coding assistant Cursor offers different levels of autonomy. You can use simple tab-completion (low autonomy), ask it to edit a selected block of code (medium autonomy), or give it a high-level task to execute across the entire repository (high autonomy) [[10]](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6). Similarly, Perplexity offers "Quick Search" (a simple workflow), "Research," and "Deep Research" (progressively more agentic) [[11]](https://andrewships.substack.com/p/autonomy-sliders).

The ultimate goal is to accelerate the continuous loop between AI generation and human verification. This is often achieved through a combination of well-designed architecture and a thoughtful user interface that allows for easy human oversight.![Image 4: A flowchart illustrating the continuous loop between AI generation and human verification, with the goal of speeding up the loop.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/ai-human-verification-loop.png)

Image 4: A flowchart illustrating the continuous loop between AI generation and human verification, with the goal of speeding up the loop.

## Exploring Common Patterns

To build an intuition for AI engineering, let's explore some of the most common patterns used to construct both workflows and agents. We will cover these in detail in future lessons, but for now, we will focus on the high-level concepts.

### LLM Workflow Patterns

Workflows are built by composing different patterns to automate multi-step tasks.

**Chaining and routing** are foundational patterns for automating multiple LLM calls. A chain links a sequence of LLM calls, where the output of one step becomes the input for the next. A router acts as a decision point, guiding the workflow down different paths based on the input or intermediate results. This allows you to glue together multiple LLM calls and decide between different options as the task progresses [[21]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns/).![Image 5: A flowchart illustrating the Chaining and Routing pattern for LLM workflows, showing an initial input, a routing decision, various LLM calls and sub-chains, and the final output.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/chaining-routing-pattern.png)

Image 5: A flowchart illustrating the Chaining and Routing pattern for LLM workflows, showing an initial input, a routing decision, various LLM calls and sub-chains, and the final output.

The **orchestrator-worker** pattern provides a more dynamic way to structure workflows. In this pattern, a central "orchestrator" LLM analyzes the user's intent, breaks down the task into smaller sub-tasks, and delegates them to specialized "worker" LLMs. A final "synthesizer" LLM then combines the results into a cohesive answer. This pattern makes a smooth transition between the workflow and agentic worlds by allowing the system to dynamically decide what actions to take [[25]](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/), [[26]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent).![Image 6: Flowchart illustrating the Orchestrator-Worker pattern](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/orchestrator-worker-pattern.png)

Image 6: Flowchart illustrating the Orchestrator-Worker pattern

The **evaluator-optimizer loop** is a pattern used to auto-correct and refine the output from an LLM. It works by using a second "evaluator" LLM to review the output of the first "generator" LLM. The evaluator provides feedback, often called a reflection, which is then passed back to the generator to improve its next attempt. This loop continues until the output meets a predefined quality standard, similar to how a human writer refines a document based on an editor's feedback [[30]](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html).![Image 7: A flowchart illustrating the Evaluator-Optimizer Loop pattern.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/evaluator-optimizer-loop.png)

Image 7: A flowchart illustrating the Evaluator-Optimizer Loop pattern.

### Core Components of a ReAct AI Agent

Almost all modern agents in the industry are built using the **ReAct (Reason and Act)** pattern, which has shown the most promise for building autonomous systems. The core idea is simple: the agent repeatedly cycles through a loop of reasoning about what to do next, taking an action, and observing the outcome [[5]](https://developers.google.com/gemini-code-assist/docs/gemini-cli).

This loop is powered by a few key components:
*   **Reasoning LLM**: This is the "brain" of the agent. It analyzes the task, plans the next step, and interprets the results of actions.
*   **Actions (Tools)**: These are the "hands" of the agent, allowing it to interact with the external world. Actions can be anything from searching the web to querying a database or writing to a file. We will cover tools in detail in Lesson 6.
*   **Short-Term Memory**: This is the agent's working memory, comparable to a computer's RAM. It holds the context of the current conversation, including past actions and observations.
*   **Long-Term Memory**: This provides the agent with persistent knowledge. It can include factual data about the world (semantic memory) and information about past interactions or user preferences (episodic memory). We will explore memory in Lesson 9.![Image 8: A flowchart illustrating the core components and dynamics of a ReAct (Reason and Act) AI agent.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/react-agent-dynamics.png)

Image 8: A flowchart illustrating the core components and dynamics of a ReAct (Reason and Act) AI agent.

Together, these components allow a ReAct agent to autonomously decide what action to take, interpret the output, and repeat the process until its goal is complete. We will dive much deeper into ReAct agents in Lessons 7 and 8.

## Zooming In on Our Favorite Examples

To anchor these concepts in the real world, let's analyze a few state-of-the-art systems, from a simple workflow to a complex hybrid agent. We will keep these explanations high-level, focusing on the architectural patterns rather than the technical details.

### Simple Workflow: Gemini in Google Workspace

**Problem:** When working in teams, finding the right information in a sea of documents can be a time-consuming process. Many documents are long, making it difficult to quickly determine if they contain what you are looking for. An embedded summarization tool can guide your search and save valuable time.

The document summarization feature in Google Workspace is a perfect example of a pure, simple workflow [[1]](https://support.google.com/docs/answer/15627020?hl=en). It follows a predefined chain of LLM calls to process a document without any dynamic decision-making.

The workflow looks like this:
1.  **Read Document**: The system ingests the content of the selected document.
2.  **Summarize**: An LLM call generates a concise summary of the text.
3.  **Extract Key Points**: Another LLM call identifies the most important takeaways.
4.  **Save Results**: The summary and key points are stored.
5.  **Show Results**: The generated content is displayed to the user.

This is a classic map-reduce approach, where the document is broken down, processed in stages, and the results are aggregated [[35]](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models). It is predictable, reliable, and efficient for this specific task.![Image 9: A flowchart illustrating a simple LLM workflow for document summarization and analysis in Google Workspace.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/document-summarization-workflow.png)

Image 9: A flowchart illustrating a simple LLM workflow for document summarization and analysis in Google Workspace.

### AI Agent: Gemini CLI Coding Assistant

**Problem:** Writing code is a slow and often tedious process. It involves reading dense documentation, navigating unfamiliar codebases, and learning new programming languages. A coding assistant can act as a pair programmer, dramatically speeding up development.

The open-source Gemini CLI is a great example of a single-agent system that uses the ReAct architecture to help developers with coding tasks [[43]](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43). It can write code from scratch (a practice known as "vibe coding"), assist with specific functions, generate documentation, and help you quickly get up to speed on new projects.

Based on our research, here is a high-level overview of its operational loop:
1.  **Context Gathering**: The agent starts by loading its context, which includes the directory structure of the codebase, a list of available tools, and the history of the current conversation [[40]](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/), [[44]](https://aipositive.substack.com/p/a-look-at-context-engineering-in).
2.  **LLM Reasoning**: The Gemini model analyzes the user's request and the current context to create a plan of action.
3.  **Human in the Loop**: Before executing any code, the agent presents its plan to the user for validation.
4.  **Tool Execution**: Once approved, the agent executes the selected tools. These can include file system operations (like reading code with `grep`), web searches (for documentation), and code generation or interpretation. The results of these actions are added to the conversation history.
5.  **Evaluation**: The agent dynamically evaluates the generated code, for instance by compiling or running it, to check for errors.
6.  **Loop Decision**: Finally, the agent decides if the task is complete or if it needs to repeat the cycle to refine its work.

This ReAct loop allows the Gemini CLI to function as an autonomous assistant, taking on complex coding tasks with minimal human intervention.![Image 10: A flowchart illustrating the operational loop of the Gemini CLI coding assistant, based on the ReAct pattern.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/gemini-cli-loop.png)

Image 10: A flowchart illustrating the operational loop of the Gemini CLI coding assistant, based on the ReAct pattern.

### Hybrid System: Perplexity Deep Research

**Problem:** Researching a new topic can be daunting. It is hard to know where to start, which sources to trust, and how to synthesize information from dozens of articles, papers, and videos. A research assistant that can quickly scan the internet and compile a comprehensive report is a powerful tool for learning.

Perplexity's Deep Research agent is a fascinating hybrid system that combines the structured planning of workflows with the dynamic reasoning of ReAct agents to perform expert-level autonomous research [[8]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research). Unlike the single-agent Gemini CLI, this system uses multiple specialized agents orchestrated in parallel by a workflow. It performs dozens of searches across hundreds of sources to create detailed reports in just a few minutes.

While Perplexity's exact implementation is closed-source, based on our research, here is an oversimplified look at how it might work:
1.  **Research Planning & Decomposition**: An orchestrator agent analyzes the user's research question and breaks it down into a set of targeted sub-questions. This is a classic example of the orchestrator-worker pattern.
2.  **Parallel Information Gathering**: To move faster, specialized search agents are deployed in parallel, each tackling a single sub-question. These agents use tools like web search and document retrieval to gather as much relevant information as possible. Because each agent has a narrow focus, its context is smaller, which helps the LLM stay on task.
3.  **Analysis & Synthesis**: Each agent validates its sources, scoring them for credibility and relevance. The top-ranked sources are then summarized into a report for that sub-question.
4.  **Iterative Refinement & Gap Analysis**: The orchestrator gathers the reports from all the worker agents and analyzes them to identify any knowledge gaps. If gaps are found, it generates follow-up queries and repeats the process. This loop continues until the research is complete or a maximum number of iterations is reached.
5.  **Report Generation**: Finally, the orchestrator combines the results from all the agents into a single, comprehensive report with inline citations.

This hybrid approach allows the Deep Research agent to combine structured planning with dynamic adaptation, creating a system that is both powerful and efficient.![Image 11: Flowchart illustrating Perplexity's Deep Research agent's iterative multi-step process.](https://storage.googleapis.com/articles-images/agentic-ai-engineering-course/lesson-2/perplexity-deep-research-process.png)

Image 11: Flowchart illustrating Perplexity's Deep Research agent's iterative multi-step process.

## The Challenges of Every AI Engineer

Now that you understand the spectrum from LLM workflows to AI agents, it is important to recognize that every AI engineer—whether at a startup or a Fortune 500 company—faces these same fundamental challenges when designing a new AI application. The architectural decisions you make will determine whether your product succeeds in production or fails spectacularly [[15]](https://arxiv.org/html/2510.25423v2).

Here are some of the daily battles every AI engineer faces:
*   **Reliability Issues:** Your agent works perfectly in demos but becomes unpredictable with real users. LLM reasoning failures can compound through multi-step processes, leading to unexpected and costly outcomes [[17]](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5).
*   **Context Limits:** Systems struggle to maintain coherence across long conversations, gradually losing track of their purpose. Ensuring consistent output quality across different agent specializations presents a continuous challenge.
*   **Data Integration:** Building pipelines to pull information from Slack, web APIs, and databases is complex. You must also ensure that only high-quality data is passed to your AI system, because as the saying goes: garbage-in, garbage-out.
*   **Cost-Performance Trap:** Sophisticated agents can deliver impressive results, but they can also cost a fortune per user interaction, making them economically unfeasible for many applications.
*   **Security Concerns:** Autonomous agents with powerful write permissions could send the wrong emails, delete critical files, or expose sensitive data without robust safeguards in place [[19]](https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges).

The good news is that these challenges are solvable. In the upcoming lessons, we will systematically tackle each of these issues. We will cover patterns for building reliable products through specialized evaluation and monitoring pipelines, strategies for building hybrid systems, and ways to keep costs and latency under control.

Your path forward as an AI engineer is about mastering these realities. By the end of this course, you will have the knowledge to architect AI systems that are not only powerful but also robust, efficient, and safe. You will know when to use a workflow, when to deploy an agent, and how to build effective hybrid systems that work in the messy, unpredictable real world. In our next lesson, we will explore structured outputs, a key technique for making LLM responses reliable and machine-readable.

## References

- [1] Google. (n.d.). *Summarize a document*. Google Docs Help. [https://support.google.com/docs/answer/15627020?hl=en](https://support.google.com/docs/answer/15627020?hl=en)
- [2] Quach, H. (2025, June 27). *A Developer’s Guide to Building Scalable AI: Workflows vs Agents*. Towards Data Science. [https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)
- [3] Anthropic. (2024, December 19). *Building effective agents*. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [4] Google Cloud. (n.d.). *What is an AI agent?*. [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [5] Google for Developers. (n.d.). *Gemini CLI*. [https://developers.google.com/gemini-code-assist/docs/gemini-cli](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- [6] Iusztin, P. (2024, July 29). *Real Agents vs. Workflows: The Truth Behind AI 'Agents'* [Video]. YouTube. [https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s)
- [7] Iusztin, P. (2024, August 26). *Exploring the difference between agents and workflows*. Decoding ML. [https://decodingml.substack.com/p/llmops-for-production-agentic-rag](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
- [8] Perplexity Team. (2025, February 14). *Introducing Perplexity Deep Research*. Perplexity Blog. [https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [9] Iusztin, P. (2024, September 2). *Stop Building AI Agents: Here’s what you should build instead*. Decoding ML. [https://decodingml.substack.com/p/stop-building-ai-agents](https://decodingml.substack.com/p/stop-building-ai-agents)
- [10] Pouladian, B. (2025, June 20). *Andrej Karpathy on Software 3.0: Software in the Age of AI*. Medium. [https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6)
- [11] Ships, A. (2025, June 21). *Autonomy Sliders*. Substack. [https://andrewships.substack.com/p/autonomy-sliders](https://andrewships.substack.com/p/autonomy-sliders)
- [12] Latent Space. (2025, June 20). *S3: The Shift from Software 2.0 to 3.0*. [https://www.latent.space/p/s3](https://www.latent.space/p/s3)
- [13] Karpathy, A. (2025, June 18). *Software Is Changing (Again)* [Video]. YouTube. [https://www.youtube.com/watch?v=LCEmiRjPEtQ](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- [14] Pangambam S. (2025, June 20). *Andrej Karpathy: Software Is Changing (Again)*. The Singju Post. [https://singjupost.com/andrej-karpathy-software-is-changing-again/](https://singjupost.com/andrej-karpathy-software-is-changing-again/)
- [15] Asgari, A., Panichella, A., Derakhshanfar, P., & Olsthoorn, M. (2025). *What Challenges Do Developers Face in AI Agent Systems? An Empirical Study on Stack Overflow & GitHub Issues*. arXiv. [https://arxiv.org/html/2510.25423v2](https://arxiv.org/html/2510.25423v2)
- [16] Permiso. (n.d.). *8 Critical AI Security Challenges*. [https://permiso.io/blog/8-critical-ai-security-challenges](https://permiso.io/blog/8-critical-ai-security-challenges)
- [17] Roy, A. (2024, July 15). *Key Challenges in AI Agent Development and How to Solve Them*. Medium. [https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5)
- [18] Chen, J., & Lu, R. (2025, May 1). *AI Agents Are Here. So Are the Threats*. Unit 42. [https://unit42.paloaltonetworks.com/agentic-ai-threats/](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [19] CyberArk. (n.d.). *The Agentic AI Revolution: 5 Unexpected Security Challenges*. [https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges](https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges)
- [20] Mirascope. (n.d.). *LLM Chaining*. [https://mirascope.com/blog/llm-chaining](https://mirascope.com/blog/llm-chaining)
- [21] Andrès, D. (2024, August 28). *Issue #110 - LLM Workflow Patterns*. mlpills. [https://mlpills.substack.com/p/issue-110-llm-workflow-patterns](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [22] Orq.ai. (n.d.). *Prompt Structure & Chaining*. [https://orq.ai/blog/prompt-structure-chaining](https://orq.ai/blog/prompt-structure-chaining)
- [23] GeeksforGeeks. (n.d.). *LLM Chains*. [https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/](https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/)
- [24] Prompting Guide. (n.d.). *Prompt Chaining*. [https://www.promptingguide.ai/techniques/prompt_chaining](https://www.promptingguide.ai/techniques/prompt_chaining)
- [25] Stevens Institute of Technology. (n.d.). *Building Self-Healing AI with Orchestrator-Reflexion Patterns*. [https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/)
- [26] Andrès, D. (2024, September 4). *DIY #17 - Orchestrator-Worker LLM Agent*. mlpills. [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [27] F., S. (2025, July 1). *The orchestrator-worker pattern is a well-known design pattern...*. LinkedIn. [https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL](https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL)
- [28] Anthropic. (n.d.). *Patterns for Building with Agents: Orchestrator-Workers*. Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [29] Gurusup. (n.d.). *Agent Orchestration Patterns*. [https://gurusup.com/blog/agent-orchestration-patterns](https://gurusup.com/blog/agent-orchestration-patterns)
- [30] AWS. (n.d.). *Agentic AI Patterns: Evaluator, Reflect, and Refine Loop Patterns*. [https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html)
- [31] Roach, C. (2024, May 22). *Building Self-Correcting LLM Systems: The Evaluator-Optimizer Pattern*. DEV Community. [https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p](https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p)
- [32] Ilievski, V. (2024, July 10). *The Research on LLM Self-Correction*. Vadim's Blog. [https://vadim.blog/the-research-on-llm-self-correction](https://vadim.blog/the-research-on-llm-self-correction)
- [33] Anthropic. (n.d.). *Patterns for Building with Agents: Evaluator-Optimizer*. Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer)
- [34] G, S. (2024, July 15). *Evaluator-Optimizer LLM Workflow*. Substack. [https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow](https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow)
- [35] Laforge, G., & Spruyt, R. (2024, April 30). *Long document summarization with Workflows and Gemini models*. Google Cloud Blog. [https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models)
- [36] Google. (n.d.). *Google Workspace with Gemini*. [https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini](https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini)
- [37] Master Concept. (n.d.). *New Google Workspace Gemini Feature: Your PDFs Now Write Their Own Summaries*. [https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/](https://masterconcept.ai/blog/new-google-workspace-gemini-feature-your-pdfs-now-write-their-own-summaries-and-suggest-next-steps/)
- [38] Liu, J. (2023, October 9). *Building Production-Ready RAG Applications* [Video]. YouTube. [https://www.youtube.com/watch?v=TRjq7t2Ms5I](https://www.youtube.com/watch?v=TRjq7t2Ms5I)
- [39] Mullen, T., & Salva, R. J. (2025, June 25). *Gemini CLI: your open-source AI agent*. The Keyword. [https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [40] Veenema, W. (2025, June 26). *How Gemini CLI builds context*. [https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/)
- [41] Milvus. (n.d.). *How do I provide context files to Gemini CLI?*. [https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli](https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli)
- [42] Gemini CLI Docs. (n.d.). *GEMINI.md*. [https://geminicli.com/docs/cli/gemini-md/](https://geminicli.com/docs/cli/gemini-md/)
- [43] Google Cloud. (2025, July 1). *Gemini CLI Tutorial Series Part 9: Understanding Context, Memory, and Conversational Branching*. Medium. [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)
- [44] AI Positive. (2025, July 3). *A Look at Context Engineering in Gemini CLI*. Substack. [https://aipositive.substack.com/p/a-look-at-context-engineering-in](https://aipositive.substack.com/p/a-look-at-context-engineering-in)
- [45] Digital Applied. (n.d.). *Perplexity Agent API Platform: AI Search Developer Guide*. [https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide](https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide)
- [46] Renner, M., & Chaban, M. A. V. (2026, April 22). *1,302 real-world gen AI use cases from the world's leading organizations*. Google Cloud Blog. [https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- [47] OpenAI. (2025, July 17). *Introducing ChatGPT agent: bridging research and action*. [https://openai.com/index/introducing-chatgpt-agent/](https://openai.com/index/introducing-chatgpt-agent/)
- [48] tracer.cloud. (2025, July 25). *The third wave of data engineering...*. LinkedIn. [https://www.linkedin.com/posts/tracercloud_the-third-wave-of-data-engineering-activity-7417891798364168192-ZQJz](https://www.linkedin.com/posts/tracercloud_the-third-wave-of-data-engineering-activity-7417891798364168192-ZQJz)
- [49] Commvault. (n.d.). *Protecting AI data pipelines*. [https://www.commvault.com/use-cases/protecting-ai-data-pipelines](https://www.commvault.com/use-cases/protecting-ai-data-pipelines)
- [50] Lumenova. (n.d.). *Machine Learning Monitoring Tools for AI Reliability*. [https://www.lumenova.ai/blog/machine-learning-monitoring-tools-ai-reliability/](https://www.lumenova.ai/blog/machine-learning-monitoring-tools-ai-reliability/)
- [51] Google. (n.d.). *Gemini CLI*. GitHub. [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)