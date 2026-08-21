# The Critical Decision Every AI Engineer Faces: LLM Workflows vs. AI Agents

As an AI engineer preparing to build your first real AI application, after narrowing down the problem you want to solve, one key decision is how to design your AI solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach, where the LLM makes self-directed decisions along the way? This fundamental question will determine the success or failure of your project: How should you architect your AI system?

When building AI applications, you face this critical architectural decision early in your development process. Should you create a predictable workflow where you control every action, or should you build an autonomous agent that can think and decide for itself? This choice will impact everything from development time and costs to reliability and user experience.

Choose the wrong approach, and you might end up with an overly rigid system that breaks when users deviate from expected patterns or when you try to add new features. You could also build an unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most. This can lead to months of wasted development time, frustrated users who cannot rely on the application, and executives who cannot afford to keep the system running as costs skyrocket.

In 2024 and 2025, billion-dollar AI startups are succeeding or failing based on this architectural decision. The most successful teams and AI engineers know when to use workflows versus agents and, more importantly, how to combine both approaches effectively.

By the end of this lesson, you will have a framework to confidently make this critical decision. You will understand the fundamental trade-offs, see real-world examples from leading AI companies, and learn how to design systems that leverage the best of both worlds.

## Understanding the Spectrum: From Workflows to Agents

Before we can choose between workflows and agents, you need a clear understanding of what they are. At this point, we will not focus on the technical specifics but rather on their properties and how they are used.

An LLM workflow is a sequence of tasks involving LLM calls or other operations, such as reading or writing data. It is largely predefined and orchestrated by developer-written code. The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execution and explicit control flow. Think of a workflow as a factory assembly line, where each station performs a specific, repeatable task in a set order. In future lessons, we will explore common workflow patterns like chaining, routing, and orchestrator-worker designs.
Image 1: A simple LLM workflow, where an input is processed by a series of LLM calls to produce an output.

AI agents, on the other hand, are systems where an LLM plays a central role in dynamically deciding the sequence of steps, reasoning, and actions to achieve a goal [[1]](https://cloud.google.com/discover/what-are-ai-agents). The steps are not defined in advance but are planned based on the task and the current state of the environment. This makes them adaptive and capable of handling novelty. An agent is like a skilled human expert tackling an unfamiliar problem, adapting their approach with each new piece of information. To do this, agents use actions, memory, and reasoning patterns like ReAct, which we will cover in future lessons.
Image 2: An AI agent consists of memory, planning, and tools, with the agent at the center coordinating these components. (Source [Decoding ML](https://d/p/llmops-for-production-agentic-rag))

Both workflows and agents require an orchestration layer, but its nature differs. In workflows, the orchestrator executes a defined plan. In agents, it facilitates the LLM's dynamic planning and execution. This distinction between developer-defined logic and LLM-driven autonomy is the core of the architectural choice you will face.

## Choosing Your Path

In the previous section, we defined LLM workflows and AI agents independently. Now, we want to explore their core differences: developer-defined logic versus LLM-driven autonomy in reasoning and action selection.
Image 3: A diagram showing the spectrum from a structured Workflow to an autonomous Agent, highlighting the trade-off between application reliability and the agent's level of control. (Source [Decoding ML](https://decodingml.substack.com/p/stop-building-ai-agents))

### When to Use LLM Workflows

Workflows are best for tasks with a well-defined structure. This includes pipelines for data extraction from sources like Slack or Google Drive, automated report or email generation, and content repurposing. Their strength lies in predictability and reliability, which makes them easier to debug and test. Operationally, you can often use smaller, specialized models for each sub-task, leading to lower and more predictable costs and latency [[2]](https://www.anthropic.com/engineering/building-effective-agents). However, building them can require more development time upfront, and the user experience can feel rigid if it cannot handle unexpected scenarios.

Because of their reliability, workflows are preferred in enterprises and regulated fields like finance and healthcare. In these domains, a system must produce the correct, auditable output every time, as errors can have a direct impact on people's money and lives. Workflows are also ideal for building Minimum Viable Products (MVPs) that require rapid deployment, as well as for high-frequency scenarios where the cost per request matters more than sophisticated reasoning.

### When to Use AI Agents

Agents are better suited for open-ended or dynamic tasks. This includes complex customer support, open-ended research and synthesis, or interactive problem-solving like debugging code. Their primary strength is their adaptability and flexibility to handle ambiguity.

However, this autonomy comes with significant weaknesses. Agents are more prone to errors and non-deterministic behavior, making performance, latency, and costs vary with each run. They often require larger, more expensive models to generalize effectively. Security is also a major concern, as an agent with write permissions could delete data or send inappropriate emails. Finally, agents are notoriously difficult to debug and evaluate [[3]](https://arxiv.org/html/2510.25423v2). There are already stories of developers having their code deleted by an agent, joking that they "wanted to start a new project anyway."

### Hybrid Approaches and the Autonomy Slider

Most real-world systems are not purely one or the other; they blend elements of both. In reality, there is a spectrum between rigid workflows and fully autonomous agents, and the best systems often find a balance.

Andrej Karpathy introduced the concept of an "autonomy slider," where you decide how much control to give the LLM versus the user [[4]](https://singjupost.com/andrej-karpathy-software-is-changing-again/). Coding assistants like Cursor exemplify this. A user can choose tab-completion (low autonomy), editing a selected block of code (medium autonomy), or letting the agent modify the entire repository (high autonomy). Similarly, Perplexity offers a quick search (workflow-like), a more involved research mode, or a "deep research" (agentic) option [[4]](https://singjupost.com/andrej-karpathy-software-is-changing-again/). The user tunes the level of autonomy based on the complexity of the task.

The ultimate goal is to speed up the loop between AI generation and human verification. This is achieved not just through a well-designed architecture but also through a thoughtful user interface that makes it easy for humans to guide and correct the AI, as seen in products like Cursor [[4]](https://singjupost.com/andrej-karpathy-software-is-changing-again/).

```mermaid
flowchart LR
  %% Human Interaction
  subgraph "Human"
    H_init["Human<br/>(Initiates Task)"]
    H_ver["Human<br/>(Verification)"]
  end

  %% AI Process
  subgraph "AI Process"
    AI_gen["AI Generation"]
  end

  %% Flow
  H_init -- "Initiates" --> AI_gen
  AI_gen -- "Generates Output" --> H_ver
  H_ver -- "Feedback<br/>(Refinement)" --> AI_gen
  H_ver -- "Accepts" --> Final_out["Final Output"]
```
Image 4: A circular flow diagram illustrating the iterative process of AI generation and human verification.

## Exploring Common Patterns

To navigate the world of AI Engineering, it helps to understand the common patterns used to build both workflows and agents. We will introduce them here at a high level to build intuition; future lessons will dive into the technical details of each.

### LLM Workflow Patterns

Workflows are constructed from several foundational patterns that allow for structured, multi-step processing.

**Chaining and routing** is the simplest pattern, used to automate multiple LLM calls together [[5]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns). It helps glue different steps and allows the system to decide between different paths based on the input or intermediate outputs.

```mermaid
flowchart LR
  A["Input"] --> B{"LLM Call Router"}
  B -->|"Condition 1"| C["LLM Call 1"]
  B -->|"Condition 2"| D["LLM Call 2"]
  B -->|"Condition 3"| E["LLM Call 3"]
  C --> F["Final Output"]
  D --> F
  E --> F
```
Image 5: A flowchart illustrating the "Chaining and Routing" pattern for LLM workflows.

The **orchestrator-worker** pattern introduces a level of dynamic planning [[6]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns). A central orchestrator LLM analyzes the user's intent, breaks the task into sub-tasks, and delegates them to specialized worker models. The orchestrator then synthesizes the results into a final answer. This pattern makes a smooth transition from rigid workflows to more adaptive, agentic behavior.

```mermaid
flowchart LR
  %% Start of the process
  Input["Input"]

  %% Orchestration layer
  subgraph Orchestration["Orchestration Layer"]
    Orchestrator["Orchestrator<br/>(Central LLM)"]
  end

  %% Worker layer
  subgraph Workers["Worker LLMs (Parallel Execution)"]
    Worker1["Worker 1"]
    Worker2["Worker 2"]
    Worker3["Worker 3"]
  end

  %% Synthesis layer
  subgraph Synthesis["Synthesis Layer"]
    Synthesizer["Synthesizer"]
  end

  %% Final output
  Output["Final Output"]

  %% Data flow
  Input -- "feeds" --> Orchestrator
  Orchestrator -- "delegates subtask" --> Worker1
  Orchestrator -- "delegates subtask" --> Worker2
  Orchestrator -- "delegates subtask" --> Worker3

  Worker1 -- "sends result" --> Synthesizer
  Worker2 -- "sends result" --> Synthesizer
  Worker3 -- "sends result" --> Synthesizer

  Synthesizer -- "produces" --> Output

  %% Visual grouping for LLMs
  classDef llm stroke-width:2px
  class Orchestrator,Worker1,Worker2,Worker3 llm
```
Image 6: A flowchart illustrating the Orchestrator-Worker pattern with a central LLM orchestrating parallel worker LLMs and a synthesizer combining results.

An **evaluator-optimizer loop** is used to auto-correct and refine the output from an LLM [[7]](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer). In this pattern, one LLM generates a response, and another "evaluator" LLM reviews it against specific criteria. The evaluator provides feedback, which is then passed back to the generator to improve its next attempt. This cycle repeats until the output meets the desired quality, mimicking how a human writer refines a document based on an editor's feedback.

```mermaid
flowchart LR
  %% LLM components
  A["Generator LLM"]
  C["Evaluator LLM"]

  %% Data and results
  B["Output"]
  D["Feedback"]
  E["Final Result"]

  %% Primary flow
  A -- "produces" --> B
  B -- "assesses against criteria" --> C
  C -- "provides" --> D
  D -- "refines" --> A

  %% Exit condition
  B -- "meets success criteria" --> E

  %% Visual grouping
  classDef exec stroke-width:2px
  classDef artifact stroke-dasharray:3,3
  class A,C exec
  class B,D,E artifact
```
Image 7: A circular flow diagram illustrating the "Evaluator-Optimizer" loop.

### Core Components of a ReAct AI Agent

The ReAct (Reason and Act) framework is the dominant pattern for building modern AI agents [[8]](https://cloud.google.com/discover/what-are-ai-agents). It enables an agent to automatically decide what action to take, interpret the output of that action, and repeat the process until a task is completed.

A ReAct agent consists of several core components:
*   An **LLM** to reason, plan actions, and interpret outputs.
*   A set of **tools** (or actions) that allow the agent to interact with its external environment. We will cover tools in detail in Lesson 6.
*   **Short-term memory** to keep track of the current conversation and actions, much like RAM in a computer.
*   **Long-term memory** to access factual knowledge (from the internet or private databases) and remember user preferences across sessions. We will explore memory in Lesson 9.

This iterative loop of reasoning, acting, and observing is what gives ReAct agents their power and flexibility. We will dive deep into this pattern in Lessons 7 and 8.

```mermaid
flowchart LR
  %% ReAct Agent Components
  subgraph "ReAct Agent"
    Agent["Agent<br/>(LLM)"]
    Reasoning["Reasoning Process"]
    Memory["Memory<br/>(Short-term & Long-term)"]
  end

  %% External Interaction
  subgraph "External Interaction"
    Tools["Tools"]
    Environment["External Environment"]
    ToolOutput["Tool Output"]
  end

  %% Primary Data Flows
  Agent -- "initiates" --> Reasoning
  Reasoning -- "decides & selects" --> Tools
  Tools -- "interacts with" --> Environment
  Environment -- "generates" --> ToolOutput
  ToolOutput -- "observes" --> Agent

  %% Iterative Loop & Learning
  Agent -- "updates" --> Memory
  Memory -- "informs next cycle" --> Reasoning

  %% Task Completion
  Agent -- "task completed" --> FinalAnswer["Final Answer"]

  %% Visual Grouping
  classDef coreProcess stroke-width:2px
  classDef dataStore stroke-dasharray:3,3
  class Agent,Reasoning,Tools,Environment,ToolOutput coreProcess
  class Memory dataStore
```
Image 8: A flowchart illustrating the high-level dynamics of a ReAct (Reason and Act) AI agent.

## Zooming In on Our Favorite Examples

To better anchor these concepts in the real world, let's look at a few examples, from a simple workflow to a more advanced hybrid system. We will keep these explanations high-level and intuitive.

### Document Summarization in Google Workspace: A Simple Workflow

A common problem in team environments is finding the right information within large documents. A quick, embedded summary can save significant time and guide search strategies. The document summarization feature in Google Workspace is a perfect example of a pure, multi-step workflow [[9]](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models).

This system likely operates as a simple chain of LLM calls:
1.  **Read Document:** The system ingests the text from the document.
2.  **Summarize:** An LLM call generates a concise summary.
3.  **Extract Key Points:** Another LLM call identifies the main takeaways.
4.  **Save and Display:** The results are stored and shown to the user.

Each step is predictable and follows a predefined path, making it a classic example of a reliable, structured workflow.

```mermaid
flowchart LR
    A["Read Document"] -- "processes" --> B["Summarize (LLM Call)"]
    B -- "generates summary" --> C["Extract Key Points (LLM Call)"]
    C -- "identifies key points" --> D["Save Results to Database"]
    D -- "stores & displays" --> E["Show Results to User"]
```
Image 9: A sequential flowchart illustrating a simple LLM workflow for document summarization and analysis using Gemini in Google Workspace.

### Gemini CLI: An Agentic Coding Assistant

Writing code is a time-consuming process that often involves reading dense documentation or navigating unfamiliar codebases. A coding assistant can dramatically speed this up. The Gemini CLI, an open-source tool from Google, is a great example of a single-agent system that uses the ReAct pattern to assist with coding [[10]](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/).

Here is how Gemini CLI likely works:
1.  **Context Gathering:** The agent starts by loading the directory structure, available tools (actions), and conversation history into its working memory [[11]](https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/).
2.  **LLM Reasoning:** The Gemini model analyzes your request and the current context to create a plan of action.
3.  **Human in the Loop:** Before executing, it often validates the plan with you.
4.  **Tool Execution:** The agent executes the selected tools, which could include reading files, searching documentation online, or generating code diffs. The results are added back to its memory.
5.  **Evaluation:** It dynamically evaluates the generated code, for instance, by running or compiling it.
6.  **Loop Decision:** The agent determines if the task is complete or if it needs to repeat the cycle by planning and executing more actions.

This iterative loop of reasoning and acting allows the Gemini CLI to handle complex coding tasks that a simple workflow could not.

```mermaid
flowchart TD
  %% Start of the operational loop
  Start["Start"] --> CG["Context Gathering<br/>(Loading directory structure, tools, conversation history)"]

  %% Main operational loop
  CG --> LLMR["LLM Reasoning<br/>(Gemini analyzes user input and plans actions)"]
  LLMR --> HITL["Human in the Loop<br/>(Validation of planned actions)"]
  HITL --> TE["Tool Execution<br/>(File operations, web requests, code generation)"]
  TE --> E["Evaluation<br/>(Running or compiling code)"]
  E --> LD{"Loop Decision"}

  %% Loop decision and termination
  LD -- "Repeat for refinement" --> LLMR
  LD -- "Task Complete" --> End["End"]

  %% Visual grouping
  classDef decisionNode stroke-width:2px,stroke-dasharray: 5 5
  class LD decisionNode
```
Image 10: A circular flow diagram illustrating the operational loop of the Gemini CLI coding assistant, which implements the ReAct pattern.

### Perplexity Deep Research: A Hybrid System

Researching a new topic can be daunting. You often do not know where to start, and sifting through countless sources is time-consuming. Perplexity's Deep Research feature is a powerful research assistant that acts as a hybrid system, combining structured workflows with dynamic, multi-agent reasoning to produce expert-level reports [[12]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research).

While Perplexity's exact architecture is closed-source, we can infer how it might work based on its behavior and industry best practices. It likely uses an orchestrator-worker pattern to manage multiple specialized agents in parallel [[13]](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/).

Here is an oversimplified view of the process:
1.  **Research Planning & Decomposition:** An orchestrator agent analyzes your research question and breaks it down into several targeted sub-questions.
2.  **Parallel Information Gathering:** Specialized research agents are deployed in parallel, each tackling one sub-question. They use tools like web search and document retrieval to gather information. This isolation keeps each agent focused and its context window clean.
3.  **Analysis & Synthesis:** Each agent validates its sources for credibility and relevance, ranks them, and summarizes the top findings.
4.  **Iterative Refinement:** The orchestrator collects the results and identifies any knowledge gaps. If needed, it generates follow-up queries and repeats the process until the research is comprehensive or a step limit is reached.
5.  **Report Generation:** Finally, the orchestrator synthesizes all the information into a single, cohesive report with inline citations.

This hybrid approach combines the structured planning of a workflow with the adaptive reasoning of multiple agents, allowing it to tackle complex research tasks that are beyond the scope of a single agent or a rigid workflow.

```mermaid
graph TD
    A[User Query] --> B(Orchestrator: Decompose & Plan);
    B --> C{Parallel Agents};
    subgraph Parallel Agents
        C1[Agent 1: Research Sub-Question 1];
        C2[Agent 2: Research Sub-Question 2];
        C3[Agent 3: Research Sub-Question 3];
    end
    C1 --> D(Synthesize & Analyze);
    C2 --> D;
    C3 --> D;
    D --> E{Orchestrator: Identify Gaps};
    E -- "Gaps Found" --> B;
    E -- "No Gaps" --> F(Final Report Generation);
    F --> G[Comprehensive Report];
```
Image 11: An iterative, multi-step process for a hybrid research agent like Perplexity's Deep Research.

## The Challenges of Every AI Engineer

Now that you understand the spectrum from LLM workflows to AI agents, it is important to recognize that every AI engineer—whether at a startup or a Fortune 500 company—faces these same fundamental challenges when designing a new AI application. This choice is one of the core decisions that determine whether your application succeeds in production or fails spectacularly.

As you build, you will constantly battle a reliability crisis. Here are some of the daily challenges every AI engineer faces:
*   **Reliability Issues:** Your agent works perfectly in demos but becomes unpredictable with real users. LLM reasoning failures can compound through multi-step processes, leading to unexpected and costly outcomes [[14]](https://arxiv.org/html/2510.25423v2).
*   **Context Limits:** Systems struggle to maintain coherence across long conversations, gradually losing track of their purpose. Ensuring consistent output quality across different agent specializations presents a continuous challenge.
*   **Data Integration:** You will need to build pipelines to pull information from Slack, web APIs, SQL databases, and data lakes, all while ensuring only high-quality data is passed to your AI system, following the "garbage-in, garbage-out" principle.
*   **Cost-Performance Trap:** Sophisticated agents can deliver impressive results but may cost a fortune per user interaction, making them economically unfeasible for many applications.
*   **Security Concerns:** Autonomous agents with powerful write permissions could send the wrong emails, delete critical files, or expose sensitive data if not properly sandboxed and monitored [[15]](https://permiso.io/blog/8-critical-ai-security-challenges).

These challenges are solvable. In the upcoming lessons, we will systematically tackle each of these issues. You will learn battle-tested patterns for building reliable products through specialized evaluation and monitoring pipelines, proven strategies for managing context, and practical approaches for building hybrid systems that keep costs and latency under control.

Your path forward as an AI engineer is about mastering these realities. By the end of this course, you will have the knowledge to architect AI systems that are not only powerful but also robust, efficient, and safe. You will know when to use a workflow, when to deploy an agent, and how to build effective hybrid systems that work in the messy, unpredictable real world. In our next lesson, we will explore structured outputs, a key technique for making LLM interactions more reliable.

## References

- [1] https://cloud.google.com/discover/what-are-ai-agents
- [2] https://www.anthropic.com/engineering/building-effective-agents
- [3] https://arxiv.org/html/2510.25423v2
- [4] https://singjupost.com/andrej-karpathy-software-is-changing-again/
- [5] https://mlpills.substack.com/p/issue-110-llm-workflow-patterns
- [6] https://mlpills.substack.com/p/issue-110-llm-workflow-patterns
- [7] https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer
- [8] https://cloud.google.com/discover/what-are-ai-agents
- [9] https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models
- [10] https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/
- [11] https://wietsevenema.eu/blog/2025/how-gemini-cli-builds-context/
- [12] https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research
- [13] https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/
- [14] https://arxiv.org/html/2510.25423v2
- [15] https://permiso.io/blog/8-critical-ai-security-challenges
- [16] https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s
- [17] https://d/p/llmops-for-production-agentic-rag
- [18] https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/
- [19] https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
- [20] https://decodingml.substack.com/p/stop-building-ai-agents
- [21] https://www.youtube.com/watch?v=LCEmiRjPEtQ
- [22] https://www.youtube.com/watch?v=TRjq7t2Ms5I
- [23] https://github.com/google-gemini/gemini-cli/blob/main/README.md
- [24] https://openai.com/index/introducing-chatgpt-agent/