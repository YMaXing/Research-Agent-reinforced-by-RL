# Lesson 2: Workflows vs. Agents

As an AI engineer preparing to build your first real AI application, after narrowing down the problem you want to solve, one key decision is how to design your AI solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach where the LLM makes self-directed decisions? This fundamental question will determine the success or failure of your project.

Choose the wrong path, and you might build a system that is too rigid, breaking when users deviate from expected patterns. Or, you could create an unpredictable agent that works brilliantly 80% of the time but fails spectacularly when it matters most, wasting months of development time and frustrating users. In 2024 and 2025, we have seen billion-dollar AI startups succeed or fail based on this architectural decision.

This lesson provides a framework for making that choice. We will explore the trade-offs between LLM workflows and AI agents, examine real-world examples, and show you how to design systems that combine both approaches.

## Understanding the Spectrum: From Workflows to Agents

To choose between workflows and agents, it helps to think of AI autonomy not as a binary choice but as a spectrum [[1]](https://lumenalta.com/labs/from-llm-to-full-agency-understanding-the-levels-of-ai-autonomy).

### LLM Workflows

An LLM workflow is a sequence of tasks orchestrated by developer-written code. Think of it as a factory assembly line: each step is predefined, and the control flow is explicit [[2]](https://www.anthropic.com/engineering/building-effective-agents). This approach has roots in earlier rule-based AI systems, which were predictable but often struggled with nuance [[3]](https://fetch.ai/blog/evolution-ai-agents-from-rule-based-systems-to-llms-agents). Workflows use LLMs to overcome these limitations, but the developer remains in charge; the LLM acts as a component but does not decide what to do next. A workflow replaces a task a person would do [[4]](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s).

Because the paths are fixed, they are easier to debug, test, and their costs are more predictable. We will explore common workflow patterns like chaining, routing, and the orchestrator-worker model in future lessons.

```mermaid
flowchart LR
  A["User Input<br/>(Document)"]
  B["Read Document"]
  C["Summarize with LLM<br/>(Gemini in Workspace)"]
  D["Extract Key Points<br/>with LLM (Gemini)"]
  E[(Save Results<br/>to Database)]
  F["Display Summary<br/>to User"]

  A -- "provides" --> B
  B -- "parses content" --> C
  C -- "generates summary" --> D
  D -- "produces results" --> E
  E -- "persists & retrieves" --> F
```

Image 1: A flowchart illustrating a simple LLM workflow for document summarization and analysis using Gemini in Google Workspace.

### AI Agents

AI agents represent a higher level of autonomy, where the LLM dynamically directs its own processes. Instead of following a script, the agent uses its reasoning capabilities to create a plan, select actions (tools), and adapt its approach based on outcomes [[5]](https://cloud.google.com/discover/what-are-ai-agents). An agent is like a skilled expert tackling an unfamiliar problem. You can think of an agent as replacing a role a person would fill [[4]](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s).

This autonomy makes agents flexible, but it also introduces more unpredictability [[6]](https://www.zenml.io/blog/steerable-deep-research-building-production-ready-agentic-workflows-with-controlled-autonomy). The core pattern, often called ReAct, involves a continuous loop of reasoning and acting, supported by memory. We will explore tools, memory, and agent architectures in upcoming lessons.

## Choosing Your Path

The core difference between workflows and agents lies in a trade-off between control and autonomy. Workflows offer developer-defined logic, while agents provide LLM-driven autonomy. Most real-world systems exist on a spectrum between these two extremes.

Image 2: The autonomy slider, showing the trade-off between an agent's level of control and application reliability. (Source [[7]](https://decodingml.substack.com/p/stop-building-ai-agents))

**LLM workflows** are best for repeatable tasks where predictability is critical. In regulated fields like finance and healthcare, workflows are preferred because their deterministic nature ensures compliance [[8]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/). Their strengths are predictability and reliability, which makes them easier to debug and more cost-effective. Their weakness is rigidity.

**AI agents** excel at open-ended research and dynamic problem-solving. They are adaptable, but this comes at the cost of reliability. Agents can be unpredictable, harder to debug, and more expensive. It is a sobering reality that very few fully autonomous agents operate in production today; most business value still comes from more constrained, reliable systems [[1]](https://lumenalta.com/labs/from-llm-to-full-agency-understanding-the-levels-of-ai-autonomy). We have even heard stories of developers having their code accidentally deleted by an agent, joking, "Anyway, I wanted to start a new project."

Many modern AI applications feature an "autonomy slider" that lets you decide how much control to give the LLM. As Andrej Karpathy noted, tools like the Cursor code editor allow you to move from simple tab-completion to letting an agent modify your entire repository [[9]](https://singjupost.com/andrej-karpathy-software-is-changing-again/). Similarly, Perplexity offers everything from a quick search to a "deep research" mode [[10]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research).

The goal is to speed up the iterative loop between AI generation and human verification. This is often achieved through a combination of smart architecture and a well-designed user interface that makes it easy for the human to stay in the loop.

```mermaid
flowchart LR
    Start((Start)) --> AI["AI<br/>(Generation)"]

    AI -- "generates output" --> Human_Verification{"Human<br/>(Verification)"}

    Human_Verification -- "Accept Output" --> End_Loop((End Loop))
    Human_Verification -- "provides Feedback" --> AI

    %% Visual differentiation for the loop
    classDef iterative_step stroke-width:2px
    class AI,Human_Verification iterative_step
```

Image 3: A flowchart illustrating the iterative loop between AI generation and human verification.

## Exploring Common Patterns

To build effective AI systems, it helps to understand a few common architectural patterns. These patterns provide a starting point for designing both workflows and agents. We will only introduce them at a high level here, saving the detailed explanations for future lessons.

### LLM Workflow Patterns

**Chaining and routing** is the simplest pattern for automation. It involves linking multiple LLM calls in a sequence (chaining) or using an LLM to decide which path to take next (routing). This is useful for tasks that can be broken down into a series of smaller, distinct steps [[11]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns).

```mermaid
flowchart LR
  %% Workflow Start
  Input["Input"]

  %% Routing Decision
  Router{"Router LLM"}

  %% LLM Chains/Sub-workflows
  subgraph "LLM Chains"
    LLM1["LLM Call 1"]
    LLM2["LLM Call 2"]
    LLM3["LLM Call 3"]
  end

  %% Workflow End
  Output["Final Output"]

  %% Connections
  Input -- "receives query" --> Router
  Router -- "selects Chain 1" --> LLM1
  Router -- "selects Chain 2" --> LLM2
  Router -- "selects Chain 3" --> LLM3
  LLM1 -- "produces result" --> Output
  LLM2 -- "produces result" --> Output
  LLM3 -- "produces result" --> Output

  %% Visual grouping
  classDef decision stroke-dasharray:5,5
  classDef llm_process stroke-width:2px
  class Router decision
  class LLM1,LLM2,LLM3 llm_process
```

Image 4: A flowchart illustrating the "Chaining and Routing" pattern for LLM workflows.

The **Orchestrator-Worker** pattern introduces a "manager" LLM that analyzes a task, breaks it into sub-tasks, and delegates them to specialized "worker" LLMs [[12]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers). This is a step towards more dynamic behavior, bridging the gap between rigid workflows and fully autonomous agents.

```mermaid
flowchart LR
  %% Initial Task
  A["Complex Task"]

  %% Orchestrator LLM and its processes
  subgraph Orchestrator["Orchestrator"]
    OLLM["Orchestrator LLM"]
    TD["Task Decomposition"]
    RS["Result Synthesis"]
  end

  %% Worker LLMs
  subgraph Workers["Worker LLMs (Parallel Execution)"]
    W1["Worker LLM 1"]
    W2["Worker LLM 2"]
    WN["Worker LLM N"]
  end

  %% Final Output
  FA["Final Answer"]

  %% Connections
  A -- "receives" --> OLLM
  OLLM -- "performs" --> TD
  TD -- "delegates sub-tasks" --> W1
  TD -- "delegates sub-tasks" --> W2
  TD -- "delegates sub-tasks" --> WN

  W1 -- "performs Sub-task Execution<br/>returns Sub-task Results" --> OLLM
  W2 -- "performs Sub-task Execution<br/>returns Sub-task Results" --> OLLM
  WN -- "performs Sub-task Execution<br/>returns Sub-task Results" --> OLLM

  OLLM -- "initiates" --> RS
  RS -- "produces" --> FA

  %% Visual grouping
  classDef llm stroke-width:2px
  class OLLM,W1,W2,WN llm
```

Image 5: A flowchart illustrating the Orchestrator-Worker pattern with an Orchestrator LLM delegating tasks to multiple Worker LLMs and synthesizing results.

The **Evaluator-Optimizer loop** automates self-correction. One LLM generates a response, while another LLM evaluates it against a set of criteria. If the output falls short, the evaluator provides feedback (a reflection), and the generator refines its response. This loop repeats until the output is satisfactory, mimicking how a human writer revises a draft based on an editor's comments [[13]](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html).

```mermaid
flowchart LR
    GeneratorLLM["Generator LLM"] -- "produces" --> InitialOutput["Initial Output"]
    InitialOutput -- "sent to" --> EvaluatorLLM["Evaluator LLM"]
    EvaluatorLLM -- "performs" --> ReviewFeedback["Review & Feedback"]
    ReviewFeedback --> MeetsCriteria{"Meets Criteria?"}
    MeetsCriteria -- "Yes" --> FinalOutput["Final Output"]
    MeetsCriteria -- "No" --> Feedback["Feedback"]
    Feedback -- "sent back for" --> Revision["Revision"]
    Revision -- "informs" --> GeneratorLLM
```

Image 6: Flowchart illustrating the Evaluator-Optimizer Loop pattern.

### The ReAct AI Agent Pattern

The ReAct (Reason and Act) pattern is the foundation for most modern AI agents. It enables an agent to reason about a task, choose an appropriate action (tool), execute it, and then observe the outcome to inform its next step [[5]](https://cloud.google.com/discover/what-are-ai-agents). This cycle repeats until the task is complete. It relies on a few core components: an LLM for reasoning, a set of tools for taking actions, and both short-term and long-term memory. Think of short-term memory as the agent's RAM—volatile and essential for immediate tasks. As systems grow to include multiple agents, **memory engineering** becomes a critical discipline to manage shared state and ensure consistent coordination [[14]](https://www.oreilly.com/radar/why-multi-agent-systems-need-memory-engineering/).

## Zooming In on Our Favorite Examples

To make these concepts more concrete, let's look at a few examples, from a simple workflow to a complex hybrid system.

### Gemini in Google Workspace: A Simple Workflow

Finding information in long documents is time-consuming. The summarization feature in Google Workspace is a perfect example of a pure workflow [[15]](https://support.google.com/docs/answer/15627020?hl=en). It follows a predefined sequence: read the document, call an LLM to summarize it and extract key points, and display the results. The process is reliable and predictable, with no dynamic decision-making.

### Gemini CLI: A Single-Agent System

Writing code is a slow process. A coding assistant can dramatically speed this up. The open-source Gemini CLI is a great example of a single-agent system using the ReAct pattern [[16]](https://developers.google.com/gemini-code-assist/docs/gemini-cli). It follows a loop: gathering context from your codebase, reasoning to form a plan, executing tools (like file operations or web search), evaluating the result, and repeating until the task is complete. While effective, the next frontier for such agents is whole-project contextual awareness, allowing them to debug complex issues by understanding the entire dependency chain, not just isolated files [[17]](https://dev.to/alvarito1983/how-claude-code-specialized-agents-changed-my-development-workflow-in-2026-3al5).

```mermaid
flowchart LR
  %% Gemini CLI Coding Assistant Operational Loop

  subgraph "Operational Loop"
    CG["Context Gathering<br/>(Directory, Tools, History)"]
    LR["LLM Reasoning<br/>(Plan Actions)"]
    HL["Human in the Loop<br/>(Validate Plan)"]
    TE["Tool Execution<br/>(File Ops, Web, Code Gen)"]
    TO["Tool Output"]
    EV["Evaluation<br/>(Run/Compile Code)"]
    LD{"Loop Decision"}
  end

  TC["Task Complete<br/>(Output)"]

  %% Primary data flows
  CG -- "gathers context" --> LR
  LR -- "sends plan" --> HL
  HL -- "plan validated" --> TE
  TE -- "produces" --> TO
  TO -- "used for" --> EV
  EV -- "informs" --> LD

  %% Loop decision paths
  LD -- "Task Complete" --> TC
  LD -- "Repeat" --> LR

  %% Visual grouping
  classDef process stroke-width:2px
  classDef decision stroke-dasharray:3,3

  class CG,LR,HL,TE,TO,EV process
  class LD decision
```

Image 7: A flowchart illustrating the operational loop of the Gemini CLI coding assistant.

### Perplexity Deep Research: A Hybrid System

Researching a new topic is daunting. Perplexity's Deep Research feature is a powerful hybrid system that combines workflows with multiple agents to conduct expert-level research [[10]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research), [[18]](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/). It uses an orchestrator to decompose a complex query into sub-questions, which are then assigned to specialized agents. This multi-agent design avoids the "decision overload" that a single agent would face, a lesson also learned in complex robotics systems [[19]](https://www.sciencedirect.com/science/article/abs/pii/S027861252500202X). These agents gather information in parallel—a key strategy to reduce latency compared to sequential searches [[20]](https://docs.perplexity.ai/docs/agent-api/presets)—before the orchestrator synthesizes the findings, identifies gaps, and iterates until a comprehensive report is generated.

```mermaid
flowchart LR
  %% Start
  RQ["Research Question"]

  %% Orchestration and Planning
  subgraph "Orchestration & Planning"
    ORCH["Orchestrator<br/>(Research Planning & Decomposition)"]
    SQ["Sub-questions"]
  end

  %% Information Gathering
  subgraph "Information Gathering"
    PIG["Parallel Information Gathering<br/>(Specialized Search Agents)"]
    TOOLS["Tools<br/>(Web Search, Document Retrieval)"]
  end

  %% Analysis and Refinement
  subgraph "Analysis & Refinement Loop"
    AS["Analysis & Synthesis<br/>(Validate, Score, Summarize)"]
    IRA["Iterative Refinement & Gap Analysis"]
    KGR{"Knowledge Gaps Remain?"}
    GFQ["Generate Follow-up Queries"]
  end

  %% Final Output
  FRG["Final Report Generation<br/>(with Citations)"]

  %% Connections
  RQ --> ORCH
  ORCH -- "decomposes into" --> SQ
  SQ -- "processed by" --> PIG
  PIG -. "utilizes" .-> TOOLS
  PIG -- "sends results to" --> AS
  AS -- "informs" --> IRA
  IRA -- "evaluates" --> KGR
  KGR -- "Yes" --> GFQ
  GFQ -- "produces" --> SQ
  KGR -- "No" --> FRG

  %% Visual grouping
  classDef orchestrator stroke-width:2px
  class ORCH orchestrator
  classDef tool stroke-dasharray:3,3
  class TOOLS tool
```

Image 8: A flowchart illustrating Perplexity's Deep Research agent's iterative multi-step process.

## The Challenges of Every AI Engineer

Now that you understand the spectrum from workflows to agents, it is important to recognize that every AI Engineer faces these same fundamental challenges. The decision between a workflow and an agent is one of the core choices that determine whether your AI application succeeds in production.

You will battle reliability issues, where agents become unpredictable and require specialized debugging tools for multi-step tracing [[21]](https://arxiv.org/html/2510.25423v2), [[23]](https://www.braintrust.dev/articles/best-ai-agent-debugging-tools-2026). You will face context limits, data integration challenges, and cost-performance traps. Security is also a major concern, as autonomous agents with write permissions could expose sensitive data or take unintended actions [[22]](https://unit42.paloaltonetworks.com/agentic-ai-threats/). In multi-agent systems, these risks are amplified, with threats like contaminated context spreading between agents [[24]](https://www.knostic.ai/blog/multi-agent-security).

These challenges are solvable. In our next lesson, we will cover structured outputs. Later, we will explore patterns for building reliable products through evaluation and monitoring pipelines, strategies for building hybrid systems, and ways to keep costs and latency under control. Your path forward is about mastering these realities to build AI systems that are powerful, robust, and efficient.

## References

- [1] Crewe, D. (2025). _From LLM to full agency: Understanding the levels of AI autonomy_. Lumenalta. [https://lumenalta.com/labs/from-llm-to-full-agency-understanding-the-levels-of-ai-autonomy](https://lumenalta.com/labs/from-llm-to-full-agency-understanding-the-levels-of-ai-autonomy)
- [2] Anthropic. (2024). _Building effective agents_. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [3] Fetch.ai. (2024). _The Evolution of AI Agents: From Rule-Based Systems to LLMs Agents_. [https://fetch.ai/blog/evolution-ai-agents-from-rule-based-systems-to-llms-agents](https://fetch.ai/blog/evolution-ai-agents-from-rule-based-systems-to-llms-agents)
- [4] Bouchard, L. (2024). _Real Agents vs. Workflows: The Truth Behind AI 'Agents'_. [https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s)
- [5] Google. (2026). _What is an AI agent?_ [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [6] ZenML. (2024). _Steerable Deep Research: Building Production-Ready Agentic Workflows with Controlled Autonomy_. [https://www.zenml.io/blog/steerable-deep-research-building-production-ready-agentic-workflows-with-controlled-autonomy](https://www.zenml.io/blog/steerable-deep-research-building-production-ready-agentic-workflows-with-controlled-autonomy)
- [7] Iusztin, P. (2024). _Stop Building AI Agents: Here’s what you should build instead_. [https://decodingml.substack.com/p/stop-building-ai-agents](https://decodingml.substack.com/p/stop-building-ai-agents)
- [8] Quach, H. (2025). _A Developer’s Guide to Building Scalable AI: Workflows vs Agents_. Towards Data Science. [https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)
- [9] Karpathy, A. (2025). _Software Is Changing (Again)_. The Singju Post. [https://singjupost.com/andrej-karpathy-software-is-changing-again/](https://singjupost.com/andrej-karpathy-software-is-changing-again/)
- [10] Perplexity Team. (2025). _Introducing Perplexity Deep Research_. Perplexity Blog. [https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [11] ML Pills. (2024). _Issue #110 - LLM Workflow Patterns_. [https://mlpills.substack.com/p/issue-110-llm-workflow-patterns](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [12] Anthropic. (2024). _Orchestrator-Workers Workflow_. Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [13] AWS Prescriptive Guidance. (2024). _Evaluator-Reflect-Refine loop patterns_. [https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html)
- [14] O'Reilly. (2025). _Why Multi-Agent Systems Need Memory Engineering_. [https://www.oreilly.com/radar/why-multi-agent-systems-need-memory-engineering/](https://www.oreilly.com/radar/why-multi-agent-systems-need-memory-engineering/)
- [15] Google. (2024). _Get a summary of your document_. Google Docs Editors Help. [https://support.google.com/docs/answer/15627020?hl=en](https://support.google.com/docs/answer/15627020?hl=en)
- [16] Google. (2024). _Gemini CLI_. Google for Developers. [https://developers.google.com/gemini-code-assist/docs/gemini-cli](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- [17] Rodriguez, A. (2026). _How Claude Code specialized agents changed my development workflow in 2026_. DEV Community. [https://dev.to/alvarito1983/how-claude-code-specialized-agents-changed-my-development-workflow-in-2026-3al5](https://dev.to/alvarito1983/how-claude-code-specialized-agents-changed-my-development-workflow-in-2026-3al5)
- [18] van Riel, Z. (2024). _Perplexity Computer: Multi-Model Agent Orchestration for Deep Research_. [https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/)
- [19] Chen, Z., et al. (2025). _Embodied multi-agent system with vision-language model for digital twin-enabled human-robot collaborative assembly_. ScienceDirect. [https://www.sciencedirect.com/science/article/abs/pii/S027861252500202X](https://www.sciencedirect.com/science/article/abs/pii/S027861252500202X)
- [20] Perplexity. (2024). _Agent API Presets_. [https://docs.perplexity.ai/docs/agent-api/presets](https://docs.perplexity.ai/docs/agent-api/presets)
- [21] Penedo, A., et al. (2025). _AI Agent Development: An Evidence-based Technical Analysis of Challenges, Patterns, and Lessons Learned_. arXiv. [https://arxiv.org/html/2510.25423v2](https://arxiv.org/html/2510.25423v2)
- [22] Unit 42. (2025). _AI Agents Are Here. So Are the Threats._ Palo Alto Networks. [https://unit42.paloaltonetworks.com/agentic-ai-threats/](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [23] Braintrust. (2026). _The Best AI Agent Debugging Tools in 2026_. [https://www.braintrust.dev/articles/best-ai-agent-debugging-tools-2026](https://www.braintrust.dev/articles/best-ai-agent-debugging-tools-2026)
- [24] Knostic. (2025). _Securing Multi-Agent AI Systems_. [https://www.knostic.ai/blog/multi-agent-security](https://www.knostic.ai/blog/multi-agent-security)
- [25] Iusztin, P. (2024). _Exploring the difference between agents and workflows_. [https://decodingml.substack.com/p/llmops-for-production-agentic-rag](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
- [26] Al-Hasan, A., et al. (2025). _An AI-powered health care administrative workflow system_. PMC. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12360800/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360800/)

</article>