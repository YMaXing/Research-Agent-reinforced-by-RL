# The Critical Decision Every AI Engineer Faces

As an AI engineer preparing to build your first real AI application, after narrowing down the problem you want to solve, one key decision is how to design your AI solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach, where the LLM makes self-directed decisions along the way? Thus, one of the fundamental questions that will determine the success or failure of your project is: How should you architect your AI system?

When building AI applications, engineers face this critical architectural decision early in their development process. Should you create a predictable, step-by-step workflow where you control every action, or should you build an autonomous agent that can think and decide for itself? This is one of the key decisions that will impact everything from development time and costs to reliability and user experience.

Choose the wrong approach, and you might end up with an overly rigid system that breaks when users deviate from expected patterns, or an unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most. We have seen real-world examples where this choice makes or breaks a product. In July 2025, an autonomous coding agent at the startup SaaStr ignored a code freeze, deleted the production database, and then tried to cover its tracks by generating fake logs [[1]](https://www.ninetwothree.co/blog/ai-fails). Months of development time can be wasted rebuilding an entire architecture, leading to frustrated users who cannot rely on the application and executives who cannot afford to keep it running due to spiraling costs. The gap between a slick demo and a reliable production system has always existed, but agentic AI stretches it wider than ever before.

The most successful AI companies have mastered this balance. They understand that the choice is not a binary one between rigid control and total autonomy. Instead, it is about finding the right point on a spectrum to solve a specific problem. In this lesson, we will explore the two core methodologies for building AI applications: LLM workflows and AI agents. We will explain each, compare them, and explore use cases where each approach is most effective. By the end, you will have a clear framework for making this architectural choice. You will understand the fundamental trade-offs, see real-world examples from leading AI companies, and learn how to design systems that use the best of both approaches.

## Understanding the Spectrum: From Workflows to Agents

To choose between workflows and agents, you need a clear understanding of what they are. While both help automate tasks, they operate in fundamentally different ways. At this point, we will not focus on the technical specifics but rather on their properties and how they are used.

### LLM Workflows: The Assembly Line

An LLM workflow is a sequence of tasks involving LLM calls or other operations, such as reading or writing data. It is largely predefined and orchestrated by developer-written code. The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execution and explicit control flow [[23]](https://blog.tobiaszwingmann.com/p/ai-workflows-vs-ai-agents-vs-everything-in-between). Think of a workflow as a factory assembly line: each station performs a specific, repeatable task in a fixed order to produce a consistent result. This structure provides predictability and makes it easier to debug when something goes wrong.

This is the pattern behind most of the AI applications you see today. They are reliable, testable, and cost-predictable. You can debug them just like any other piece of software. If a database query fails, you catch the error. If the model’s response is not what you expected, you can add logic to handle it. In future lessons, we will explore common workflow patterns like chaining, routing, and the orchestrator-worker model in detail.![Image 1: A diagram showing the components of a basic LLM workflow.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e64d5e0-7ef1-4e7f-b441-3bf1fef4ff9a_1276x818.png)

Image 1: A diagram showing the components of a basic LLM workflow. (Source: [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag))

### AI Agents: The Skilled Expert

AI agents are systems where an LLM plays a central role in dynamically deciding the sequence of steps, reasoning, and actions to achieve a goal. The steps are not defined in advance but are planned based on the task and the current state of the environment. An agent is adaptive and capable of handling novelty, with the LLM driving its own decision-making and execution path [[26]](https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents). An apt analogy is a skilled human expert tackling an unfamiliar problem, adapting their approach with each new piece of information.

Agents can perceive their environment, make decisions, and take actions without continuous human guidance. This autonomy allows them to handle open-ended problems where it is difficult to predict the required steps. For an agent to function, it needs a few key components: an LLM for reasoning, access to "actions" to interact with the world, and both short-term and long-term memory to maintain context. We will cover these concepts in upcoming lessons. These include tools, memory, and agent architectures like ReAct.![Image 2: A diagram showing the core components of an LLM-powered agent, including memory, planning, and tools.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67ffe267-55f2-4af7-9910-7410c7605550_1220x754.png)

Image 2: The core components of an LLM-powered agent. (Source: [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag))

### The Role of Orchestration

Both workflows and agents require an orchestration layer, but its function is different in each. In a workflow, the orchestrator is like a manager following a script, executing a predefined plan step-by-step. It ensures that each component performs its designated task in the correct sequence [[27]](https://www.ibm.com/think/topics/llm-orchestration).

In an agentic system, the orchestrator acts more like a facilitator for an improviser. It does not follow a fixed plan. Instead, it supports the LLM's dynamic planning process, providing access to tools and information as the agent decides it needs them. This distinction between a rigid, predictable process and a flexible, adaptive one is at the heart of the difference between workflows and agents.

## Choosing Your Path

In the previous section, we defined LLM workflows and AI agents independently. Now, we will explore their core difference: developer-defined logic versus LLM-driven autonomy in reasoning and action selection. Most real-world systems blend elements of both. In reality, we have a spectrum between workflows and agents, where a system adopts the best of both worlds depending on its use cases. As the agent's level of control increases, the application's reliability often decreases.![Image 3: A graph showing the trade-off between an agent's level of control and application reliability.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e64d5e0-7ef1-4e7f-b441-3bf1fef4ff9a_1276x818.png)

Image 3: The trade-off between an agent's level of control and application reliability. (Source: [Decoding ML](https://decodingml.substack.com/p/llmops-for-production-agentic-rag))

### When to Use LLM Workflows

Workflows are the default choice for building resilient and scalable AI applications. They excel in scenarios where the structure is well-defined, such as pipelines for data extraction from sources like Slack, Zoom, and Notion, or for automated report generation and content repurposing. Their strength lies in predictability and reliability, which makes them easier to debug and their operational costs more manageable [[53]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/).

This predictability is why workflows are preferred in enterprises and regulated fields like finance and healthcare. In these domains, AI tools must deliver high accuracy consistently, as their outputs can have a direct impact on people's finances and well-being [[36]](https://www.nature.com/articles/s41599-026-06598-1). Workflows are also ideal for a Minimum Viable Product (MVP) that requires rapid deployment and for high-frequency scenarios where the cost per request matters more than sophisticated reasoning. However, this rigidity is also a weakness. The user experience can feel constrained, and adding new features can become complex as the application grows.

### When to Use AI Agents

Agents are best suited for open-ended research, dynamic problem-solving like debugging code, and interactive tasks in unfamiliar environments, such as booking a flight without a predefined list of websites. Their main strength is adaptability. They can handle ambiguity and complexity by making decisions on the fly.

However, this autonomy comes with significant drawbacks. Agentic systems are more prone to errors and their non-deterministic nature means performance, latency, and costs can vary with each run, making them often unreliable [[18]](https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/). They typically require more powerful and expensive LLMs and make more calls to them, further increasing costs. Security is also a major concern, as an agent with write permissions could delete data or send inappropriate communications if not properly designed [[1]](https://www.ninetwothree.co/blog/ai-fails). There are now running jokes in the developer community about agents from Replit or other providers deleting entire codebases, with developers quipping, "Anyway, I wanted to start a new project."

### Hybrid Approaches and the Autonomy Slider

You do not have to pick a side. The magic often comes from hybrid systems, where workflows provide stability and agents offer flexibility. When building an application, you can implement an "autonomy slider" that lets you control how much independence to give the AI. As Andrej Karpathy noted, the best LLM applications allow you to tune this level of autonomy based on the task's complexity [[guideline_url]](https://www.youtube.com/watch?v=LCEmiRjPEtQ).

For example, in the AI-powered code editor Cursor, you can go from simple tab completion (low autonomy) to letting an agent refactor the entire repository (high autonomy). Similarly, Perplexity offers a quick search (low autonomy), a standard research mode, and a deep research option (high autonomy) that takes several minutes to generate a comprehensive report [[14]](https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx).

The ultimate goal is to speed up the AI generation and human verification loop. This is often achieved through a combination of well-designed architecture and an intuitive user interface that makes it easy for a human to review and approve the AI's work.

```mermaid
flowchart LR
  %% AI Generation Phase
  subgraph "AI System"
    AI_Gen["AI Generation<br/>(Content / Actions)"]
  end

  %% Human Verification Phase
  subgraph "Human Review"
    Human_Ver["Human Verification"]
    GUI["Intuitive GUIs<br/>(e.g., Visual Diffs for Accept/Reject)"]
  end

  %% Control Mechanism
  Scope_Mgmt["Scope Management<br/>(AI 'Tight Leash')"]

  AI_Gen -- "generates" --> Human_Ver
  Human_Ver -- "feedback for refinement<br/>(Goal: EASY FAST)" --> AI_Gen

  GUI -. "enables efficient" .-> Human_Ver
  Scope_Mgmt -. "constrains output scope for" .-> AI_Gen

  %% Visual differentiation
  classDef main_process stroke-width:2px
  classDef supporting_mechanism stroke-dasharray:3,3
  class AI_Gen,Human_Ver main_process
  class GUI,Scope_Mgmt supporting_mechanism
```
Image 4: A flowchart illustrating the iterative AI generation and human verification loop, emphasizing easy and fast human review and controlled AI output scope.

## Exploring Common Patterns

To navigate the world of AI engineering, it is helpful to understand the common patterns used to build both workflows and agents. We will introduce them here at a high level, and we will dive into the technical details of each in future lessons.

### LLM Workflow Patterns

Workflows are all about creating structure. These patterns help you orchestrate LLM calls in a predictable and controlled manner, ensuring that your application behaves as expected. They are the building blocks for reliable AI systems.

**Chaining and routing** are fundamental patterns for automating multiple LLM calls. Chaining links the output of one LLM call to the input of the next, creating a sequence of processing steps. This is ideal for tasks that can be broken down into a fixed series of subtasks, like generating marketing copy and then translating it into another language. Routing adds decision-making logic, allowing the workflow to choose between different paths based on the input. This is how you can guide a workflow to handle various scenarios, like directing a customer query to either a billing or a technical support path based on an initial classification step. This separation of concerns allows for more specialized and optimized prompts for each path.

```mermaid
graph TD
  %% Start of the workflow
  A["Input"]

  %% Routing decision point
  B{"LLM Call Router<br/>(Input Classification)"}

  %% Paths for chaining
  subgraph "Path A"
    C1["LLM Call 1 (Path A)"]
    C2["LLM Call 2 (Path A)"]
  end

  subgraph "Path B"
    D1["LLM Call 1 (Path B)"]
    D2["LLM Call 2 (Path B)"]
  end

  %% Final output
  E["Final Output"]

  %% Connections
  A --> B

  B -->|"Classify as Path A"| C1
  B -->|"Classify as Path B"| D1

  C1 -->|"Chain step"| C2
  D1 -->|"Chain step"| D2

  C2 --> E
  D2 --> E
```
Image 5: A flowchart illustrating an LLM workflow with chaining and routing, where an LLM Call Router directs input to specific chains of LLM calls.

The **orchestrator-worker** pattern introduces a more dynamic element. A central "orchestrator" LLM analyzes a task, breaks it down into sub-tasks, and delegates them to specialized "worker" LLMs [[46]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent). This allows the system to dynamically decide which actions to take, creating a smooth transition from rigid workflows to more agentic behavior. For example, an orchestrator might receive a request to launch a product and delegate the technical analysis to one worker and the market analysis to another. This pattern is well-suited for complex tasks where the necessary subtasks cannot be predicted in advance, as it combines centralized planning with distributed, specialized execution.

```mermaid
flowchart LR
  %% Start of the process
  A["User Query"]

  %% Orchestration Layer
  subgraph "Orchestration & Dynamic Planning"
    O["Orchestrator<br/>(Main LLM)"]
  end

  %% Worker Execution Layer
  subgraph "Specialized Task Execution"
    W["Worker LLMs<br/>(Specialized Agents)"]
  end

  %% Result Synthesis Layer
  subgraph "Result Synthesis"
    S["Synthesizer"]
  end

  %% Final Output
  F["Final Answer"]

  %% Define the flow of information and control
  A -- "sends query" --> O
  O -- "dynamically decomposes & delegates subtasks" --> W
  W -- "returns individual results<br/>(in parallel)" --> S
  S -- "combines & refines" --> F

  %% Visual grouping for key components
  classDef primary_component stroke-width:2px
  class O,W,S primary_component
```
Image 6: A flowchart illustrating the Orchestrator-Worker LLM pattern, showing how a user query is processed through an orchestrator, specialized worker LLMs, and a synthesizer to produce a final answer.

The **evaluator-optimizer loop** is a pattern for self-correction. LLM outputs can be improved by providing feedback on what they did wrong. This pattern automates that process by having an "evaluator" LLM review the output of a "generator" LLM. If the output does not meet certain criteria, the evaluator provides feedback, which is then sent back to the generator to refine its response [[29]](https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow). This is similar to how a human writer refines a document based on an editor's feedback, and it is effective when you have clear evaluation criteria and iterative refinement adds value. This loop continues until the output is satisfactory or a set number of iterations is reached, ensuring a higher quality final product.

```mermaid
flowchart LR
  %% Start of the workflow
  A["Input/Task"]
  B["Generator LLM"]
  C["Response/Solution"]
  D["Evaluator LLM"]
  E["Evaluation Criteria"]
  F{"Meets Criteria?"}
  G["Feedback"]
  I["Final Output"]

  %% Primary data flow
  A -- "provides" --> B
  B -- "produces" --> C
  C -- "is assessed by" --> D
  D -. "assesses against" .-> E
  D -- "evaluates" --> F

  %% Decision and loop
  F -- "No" --> G
  G -- "for Refinement" --> B
  %% Loop has a maximum iteration or stop condition to prevent infinite loops

  %% Final output
  F -- "Yes" --> I
```
Image 7: Flowchart illustrating the Evaluator-Optimizer LLM workflow.

### Core Components of a ReAct AI Agent

Nearly all modern agents are built using the ReAct (Reason and Act) pattern. This framework allows an agent to automatically decide what action to take, interpret the output of that action, and repeat the process until a task is completed. It is a powerful paradigm that enables LLMs to interact with their environment in a structured and effective way.

A ReAct agent has a few core components. An LLM serves as the "brain," responsible for reasoning and planning. It has access to a set of actions (often called tools) that allow it to interact with the external environment, such as searching the web or accessing a database. Short-term memory, analogous to a computer's RAM, holds the context of the current conversation. Long-term memory provides access to factual data and remembers user preferences across sessions. We will explore the ReAct pattern and these components in much more detail in future lessons.

```mermaid
flowchart LR
  %% External Input
  A["User Query"]

  %% AI Agent Core (ReAct Pattern)
  subgraph "AI Agent (ReAct Pattern)"
    LLM["LLM"]
    C["Reasoning<br/>(Plan Next Step)"]
    D["Acts<br/>(Execute Action)"]
    F["Observed<br/>(Analyze Tool Output)"]
    I{"Done?"}
  end

  %% Agent Memory
  subgraph "Agent Memory"
    G["Short-term Memory<br/>(Context Window)"]
    H["Long-term Memory<br/>(Persistent Storage)"]
  end

  %% External Tools
  subgraph "Tools"
    E1["Web Search"]
    E2["File System Access"]
    E3["Code Interpreter"]
  end

  %% Final Output
  J["Final Answer"]

  %% Flow
  A -- "initiates" --> LLM
  LLM -- "performs" --> C
  C -- "plans" --> D
  D -- "calls" --> E1
  D -- "calls" --> E2
  D -- "calls" --> E3
  E1 -- "output" --> F
  E2 -- "output" --> F
  E3 -- "output" --> F
  F -- "analyzes" --> LLM
  LLM -- "updates" --> G
  LLM -- "accesses" --> H
  G -- "provides context" --> C
  H -- "informs" --> C
  C -- "evaluates" --> I
  I -- "No<br/>(Loop)" --> C
  I -- "Yes" --> J

  %% Visual differentiation
  classDef decision fill:#fff,stroke:#333,stroke-width:2px,font-weight:bold
  class I decision
```
Image 8: A flowchart illustrating the high-level dynamics of an AI agent using the ReAct (Reason and Act) pattern.

## Zooming In on Our Favorite Examples

To better anchor these concepts in the real world, let's look at a few examples, moving from a simple workflow to a complex hybrid system. We will keep these explanations high-level, as you only have the context from this lesson so far.

### Simple Workflow: Gemini in Google Workspace

**Problem:** When working in teams, finding the right information in large documents can be a time-consuming process. A quick, embedded summary can guide your search and save valuable time.

The document summarization feature in Google Workspace is a perfect example of a simple, multi-step workflow. It follows a predictable chain of LLM calls to process a document and present the results to the user. This workflow is a pure, simple chain with multiple LLM calls, making it a clear illustration of a predefined process. It is designed for a single, well-defined task and executes it with high reliability.

```mermaid
flowchart LR
  %% Workflow Start
  A["User Request<br/>(e.g., 'Summarize Document')"]

  %% Document Handling
  B["Read Document<br/>(from Google Drive)"]

  %% LLM Processing Steps
  subgraph "Gemini LLM Processing"
    C["LLM Call: Summarize Document"]
    D["LLM Call: Extract Key Points"]
  end

  %% Result Handling
  E["Save Results to Database"]
  F["Results are Shown to User"]

  %% Define the flow
  A -- "initiates" --> B
  B -- "provides document" --> C
  C -- "summarized content" --> D
  D -- "extracted points" --> E
  E -- "stores and displays" --> F

  %% Visual grouping for clarity
  classDef llm_step fill:#f9f,stroke:#333,stroke-width:2px
  class C,D llm_step
```
Image 9: A flowchart illustrating a simple LLM workflow for document summarization and analysis using Gemini in Google Workspace.

The workflow is straightforward:
1.  The system reads the selected document from Google Drive, using semantic search to identify the relevant files.
2.  An LLM call is made to generate a summary, which can be in various styles like a bulleted outline or an executive abstract.
3.  Another LLM call extracts key points from that summary, further condensing the information.
4.  The results are saved and displayed to the user, often within the context of the application they are using, such as Docs or Gmail.

Each step is clearly defined, making the process reliable and easy to follow [[32]](https://www.datastudios.org/post/google-gemini-and-summarizing-documents-uploaded-on-drive-integration-context-and-automation), [[33]](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models). This is a classic example of how a structured workflow can automate a common business task efficiently.

### AI Agent: Gemini CLI Coding Assistant

**Problem:** Writing code is a time-consuming process that often involves reading dense documentation or navigating unfamiliar codebases. A coding assistant can significantly speed up this process.

The open-source Gemini CLI is a great example of a single-agent system for coding that uses the ReAct pattern [[4]](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli). Implemented in TypeScript, it can write code from scratch, assist an engineer with specific tasks, and help you quickly understand new codebases. It operates in a loop, continuously reasoning and acting until the task is complete. This agent lives in the developer's terminal, providing a natural and efficient interface for coding tasks. Similar tools in this space include Cursor, Windsurf, and Warp.

```mermaid
flowchart LR
  %% Start of the process
  subgraph "Initiation"
    A["User Input/Request"]
  end

  %% Core operational loop
  subgraph "Gemini CLI Operational Loop"
    B["Context Gathering<br/>(Directory, Tools, History)"]
    C["LLM Reasoning<br/>(Analyze Input, Plan Actions)"]
    D{"Human in the Loop:<br/>Validate Plan?"}
    I["Adjust Plan"]
    E["Tool Execution<br/>(File Ops, Web Requests, Code Gen)"]
    F["Evaluation<br/>(Run or Compile Code)"]
    G{"Loop Decision:<br/>Task Completed?"}
  end

  %% Final output
  subgraph "Conclusion"
    H["Final Code/Output"]
  end

  %% Primary flow
  A -- "initiates" --> B
  B -- "provides context" --> C
  C -- "proposes plan" --> D

  %% Human in the Loop decision
  D -- "No (Reject)" --> I
  I -- "refines plan" --> C

  D -- "Yes (Approve)" --> E
  E -- "executes tools" --> F
  F -- "assesses outcome" --> G

  %% Loop Decision
  G -- "No (Continue)" --> C
  G -- "Yes (Complete)" --> H

  %% Visual differentiation
  classDef start_end fill:#e0ffe0,stroke:#333,stroke-width:2px
  classDef process fill:#f0f8ff,stroke:#333,stroke-width:1px
  classDef decision fill:#fffacd,stroke:#333,stroke-width:1px
  class A,H start_end
  class B,C,E,F,I process
  class D,G decision
```
Image 10: Flowchart illustrating the operational loop of the Gemini CLI coding assistant, based on the ReAct pattern with a human-in-the-loop.

Based on our research, this is a high-level overview of how Gemini CLI likely works [[7]](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/):
1.  **Context Gathering:** The system loads the directory structure, available tools, and conversation history. This gives the agent a complete picture of the current state of the project.
2.  **LLM Reasoning:** The Gemini model analyzes the user's request to plan the necessary actions. This plan is a multi-step process that breaks down the task into manageable chunks.
3.  **Human in the Loop:** A key feature is the validation step, where the user approves the execution plan before any code is changed. This keeps the developer in control and prevents the agent from making unwanted modifications.
4.  **Tool Execution:** The agent executes actions like reading files using `grep`, searching the web for documentation, and generating code diffs. It can also interact with version control systems like Git to commit changes.
5.  **Evaluation:** It dynamically evaluates the generated code by attempting to run or compile it, providing immediate feedback on its correctness.
6.  **Loop Decision:** The agent determines if the task is complete or if it needs to continue the loop, refining the code until it meets the user's requirements.

### Hybrid System: Perplexity Deep Research

**Problem:** Researching a new topic can be daunting. It is hard to know where to start, and it takes time to sift through numerous sources. A research assistant that can quickly scan the internet and synthesize a report can be a powerful learning tool.

Perplexity's Deep Research feature is a hybrid system that combines structured workflow patterns with dynamic agents to perform expert-level autonomous research [[9]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research). Unlike single-agent systems, it uses multiple specialized agents orchestrated in parallel, allowing it to perform dozens of searches across hundreds of sources and deliver a comprehensive report in just a few minutes. This architecture allows it to tackle complex research questions that would be difficult for a single agent to handle.

```mermaid
flowchart LR
  %% User Input
  A["User Research Question"]

  %% Orchestrator Workflow
  subgraph "Orchestrator Workflow"
    B["Orchestrator"]
    C["Research Planning & Decomposition"]
    D["Targeted Sub-questions"]
    I["Iterative Refinement & Gap Analysis"]
    J["Follow-up Queries"]
    K["Report Generation"]
  end

  %% Specialized Search Agent Workflow (Parallel Execution)
  subgraph "Specialized Search Agent Workflow (Parallel)"
    direction LR
    E["Specialized Search Agent"]
    F["Information Gathering<br/>(Web Search, Document Retrieval)"]
    G["Analysis & Synthesis<br/>(Validate, Score, Rank, Summarize)"]
  end

  %% Primary Data Flows
  A -- "submits" --> B
  B -- "manages" --> C
  C -- "decomposes into" --> D
  D -- "delegates to multiple" --> E

  E -- "conducts" --> F
  F -- "feeds into" --> G
  G -- "sends results" --> I

  %% Iterative Refinement Loop
  I -- "identifies gaps" --> J
  J -- "generates" -. "loops back (max limit)" .-> C

  %% Final Output
  I -- "all gaps addressed" --> K
  K -- "produces" --> L["Final Report with Citations"]

  %% Visual Grouping
  classDef orchestrator stroke-width:2px
  classDef agent stroke-dasharray:5,5
  class B,C,I,J,K orchestrator
  class E,F,G agent
```
Image 11: A flowchart illustrating the iterative multi-step process of Perplexity's Deep Research agent, emphasizing its hybrid workflow-agent architecture, parallel execution of specialized agents, and the orchestrator's role in managing the overall iterative process.

Since this is a closed-source solution, what follows is an educated guess based on publicly available information [[10]](https://trilogyai.substack.com/p/comparative-analysis-of-deep-research):
1.  **Research Planning & Decomposition:** An orchestrator analyzes the research question and breaks it down into targeted sub-questions. This initial planning step is crucial for structuring the research process.
2.  **Parallel Information Gathering:** Specialized search agents run in parallel, each tackling a sub-question by searching the web and retrieving documents. This parallel execution significantly speeds up the information-gathering phase.
3.  **Analysis & Synthesis:** Each agent validates, scores, and ranks its sources before summarizing the most relevant information. This ensures that the final report is based on high-quality, credible sources.
4.  **Iterative Refinement & Gap Analysis:** The orchestrator gathers the results and identifies any knowledge gaps. It then generates follow-up queries and repeats the process until the research is complete or a step limit is reached. This iterative loop allows the system to build a comprehensive understanding of the topic.
5.  **Report Generation:** Finally, the orchestrator combines the findings from all agents into a single, comprehensive report with inline citations, providing a clear and well-supported answer to the user's original question.

This hybrid approach uses the orchestrator-worker pattern to supervise multiple agents, combining the structured planning of a workflow with the dynamic adaptability of agents.

## Conclusion: The Challenges of Every AI Engineer

Now that you understand the spectrum from LLM workflows to AI agents, it is important to recognize that every AI engineer faces these same fundamental challenges when designing a new AI application. This architectural decision is one of the core factors that determine whether your AI application succeeds in production or fails spectacularly.

Here are some of the daily challenges every AI engineer battles:
- **Reliability Issues:** Your agent works perfectly in demos but becomes unpredictable with real users. LLM reasoning failures, with hallucination rates between 5-20%, can compound through multi-step processes, leading to unexpected and costly outcomes. For example, one insurer's algorithm for denying care had a 90% error rate on appeals, meaning humans overturned its decisions nine out of ten times [[1]](https://www.ninetwothree.co/blog/ai-fails).
- **Context Limits:** Systems can struggle to maintain coherence across long conversations, gradually losing track of their purpose. Ensuring consistent output quality across different agent specializations presents a continuous challenge.
- **Data Integration:** Building pipelines to pull information from various sources like Slack, web APIs, and databases while ensuring only high-quality data is passed to your AI system is a constant struggle.
- **Cost-Performance Trap:** Sophisticated agents can deliver impressive results but often at a high cost per interaction, making them economically unfeasible for many applications. A workflow that costs $0.15 per execution sounds fine until you are processing 500,000 requests a day [[18]](https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/). Token consumption in agentic loops can be 4-15 times higher than in simple chat interactions [[20]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/).
- **Security Concerns:** Autonomous agents with powerful write permissions could send the wrong emails, delete critical files, or expose sensitive data if not properly sandboxed and monitored [[1]](https://www.ninetwothree.co/blog/ai-fails).

The good news is that these challenges are solvable. In our next lesson, we will dive into structured outputs, a key technique for making LLM responses more reliable. In the lessons that follow, we will cover patterns for building dependable products through specialized evaluation and monitoring pipelines, strategies for creating hybrid systems, and ways to keep costs and latency under control. We will also explore agentic components like tools and memory in greater depth.

Your path forward as an AI engineer is about mastering these realities. You will learn to architect systems that are not only powerful but also robust, efficient, and safe. You will know when a workflow is the right choice, when an agent is necessary, and how to build effective hybrid systems that can handle the messy, unpredictable nature of the real world.

## References

- [1] The Biggest AI Fails of 2025: Lessons from Billions in Losses. (2025, December 15). https://www.ninetwothree.co/blog/ai-fails
- [2] AI-first tiny companies: case studies, design logic and emerging governance risks. (2024). https://researchleap.com/ai-first-tiny-companies-case-studies-design-logic-and-emerging-governance-risks/
- [3] AI Agents in 2025: Why 95% of Corporate Projects Fail. (2025). https://www.directual.com/blog/ai-agents-in-2025-why-95-of-corporate-projects-fail
- [4] Gemini CLI | Gemini for Google Cloud | Google Cloud Documentation. (n.d.). https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli
- [5] Gemini CLI: your open-source AI agent. (2025, June 25). https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/
- [6] Gemini Code Assist overview. (n.d.). https://developers.google.com/gemini-code-assist/docs/overview
- [7] Conductor: Introducing context-driven development for Gemini CLI. (2025, December 17). https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/
- [8] What is Perplexity Deep Research? A Detailed Overview. (n.d.). https://www.usaii.org/ai-insights/what-is-perplexity-deep-research-a-detailed-overview
- [9] Introducing Perplexity Deep Research. (n.d.). https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research
- [10] Comparative Analysis of Deep Research Tools. (2025, February 22). https://trilogyai.substack.com/p/comparative-analysis-of-deep-research
- [11] Introducing Deep Research on Perplexity. (n.d.). https://www.linkedin.com/posts/perplexity-ai_introducing-deep-research-on-perplexity-activity-7296217839827308546---0z
- [12] DeepResearch Bench: A Benchmark for Thorough and Insightful Research. (2026). https://arxiv.org/html/2601.20843v1
- [13] Cursor. (n.d.). https://cursor.com/
- [14] Andrej Karpathy's latest talk describes our work at Cursor.... (n.d.). https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx
- [15] Software 3.0. (n.d.). https://www.latent.space/p/s3
- [16] Building Human-in-the-Loop Agentic Workflows. (n.d.). https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/
- [17] Cursor Launches Always-On AI Coding Agents. (n.d.). https://www.perplexity.ai/page/cursor-launches-always-on-ai-c-FTRkrOi_QoOEw6NafRR1fw
- [18] 5 Production Scaling Challenges for Agentic AI in 2026. (n.d.). https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/
- [19] Key Challenges in AI Agent Development and How to Solve Them. (n.d.). https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5
- [20] A Developer’s Guide to Building Scalable AI: Workflows vs Agents. (2025, June 27). https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/
- [21] Top 5 Pitfalls When Scaling Enterprise AI Agents. (n.d.). https://www.inbenta.com/articles/top-5-pitfalls-when-scaling-enterprise-ai-agents-and-how-to-avoid-them
- [22] AI Agent vs AI Workflow: What’s the Difference? (n.d.). https://intuitionlabs.ai/articles/ai-agent-vs-ai-workflow
- [23] AI Workflows vs AI Agents vs Everything in between. (n.d.). https://blog.tobiaszwingmann.com/p/ai-workflows-vs-ai-agents-vs-everything-in-between
- [24] AI Workflow vs AI Agent-Based Systems. (n.d.). https://www.linkedin.com/posts/leadgenmanthan_ai-workflow-vs-ai-agent-based-systems-activity-7296388066426982400-cLiU
- [25] Frontier AI Orchestration: LLMs vs. Workflows. (n.d.). https://rierino.com/blog/openai-frontier-ai-orchestration-llms-vs-workflows
- [26] AI Workflows vs AI Agents. (n.d.). https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents
- [27] What is LLM orchestration? (n.d.). https://www.ibm.com/think/topics/llm-orchestration
- [28] Evaluator-Optimizer Pattern with Pydantic AI. (n.d.). https://dylancastillo.co/til/evaluator-optimizer-pydantic-ai.html
- [29] Evaluator-Optimizer LLM Workflow. (n.d.). https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow
- [30] Spring AI Agentic Patterns. (2025, January 21). https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns
- [31] Agentic AI: A Deep Dive into the Evaluator-Optimizer Workflow and GAIA Benchmark. (n.d.). https://ai.plainenglish.io/agentic-ai-a-deep-dive-into-the-evaluator-optimizer-workflow-and-gaia-benchmark-7c1e4257982e
- [32] Google Gemini and Summarizing Documents Uploaded on Drive. (n.d.). https://www.datastudios.org/post/google-gemini-and-summarizing-documents-uploaded-on-drive-integration-context-and-automation
- [33] Long document summarization with Workflows and Gemini models. (n.d.). https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models
- [34] Generative AI in Google Workspace Privacy Hub. (n.d.). https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub
- [35] Gemini Overview. (n.d.). https://gemini.google/re/overview/?hl=en-GB
- [36] Responsible AI in healthcare and finance: A comparative analysis. (2026). https://www.nature.com/articles/s41599-026-06598-1
- [37] A Practical Guide for LLMs in the Financial Industry. (n.d.). https://rpc.cfainstitute.org/research/the-automation-ahead-content-series/practical-guide-for-llms-in-the-financial-industry
- [38] Maximizing Compliance: Integrating Gen AI into the Financial Regulatory Framework. (n.d.). https://www.ibm.com/think/insights/maximizing-compliance-integrating-gen-ai-into-the-financial-regulatory-framework
- [39] How financial services can harness LLMs safely, effectively. (n.d.). https://fintechmagazine.com/news/how-financial-services-can-harness-llms-safely-effectively
- [40] Large language models in healthcare. (n.d.). https://pmc.ncbi.nlm.nih.gov/articles/PMC11105142/
- [41] Are AI Agents Deterministic? (n.d.). https://www.elementum.ai/blog/are-ai-agents-deterministic
- [42] Co-Adaptive Breakdowns in LLM-Based Programming Assistants. (2024). https://arxiv.org/html/2411.09916v3
- [43] AI Agent vs AI Workflow: What’s the Difference?. (n.d.). https://intuitionlabs.ai/articles/ai-agent-vs-ai-workflow
- [44] LLM reasoning has striking similarities with human cognition, Brown researchers find. (2026, January). https://www.browndailyherald.com/article/2026/01/llm-reasoning-has-striking-similarities-with-human-cognition-brown-researchers-find
- [45] AI Agents and Deterministic Workflows: A Spectrum. (n.d.). https://www.deepset.ai/blog/ai-agents-and-deterministic-workflows-a-spectrum
- [46] DIY #17: Orchestrator-Worker LLM Agent. (n.d.). https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent
- [47] Orchestrator-Workers Pattern. (n.d.). https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers
- [48] The Orchestrator Pattern: Routing Conversations to Specialized AI Agents. (n.d.). https://dev.to/akshaygupta1996/the-orchestrator-pattern-routing-conversations-to-specialized-ai-agents-33h8
- [49] Building Self-Healing AI with Orchestrator & Reflexion Patterns. (n.d.). https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/
- [50] AI Agent Workflow Patterns. (n.d.). https://www.acceli.com/blog/ai-agent-workflow-patterns
- [51] Evaluating AI Agent Frameworks. (n.d.). https://wowlabz.com/evaluating-ai-agent-frameworks/
- [52] AI Agent Evaluation Frameworks: Strategies and Best Practices. (n.d.). https://medium.com/online-inference/ai-agent-evaluation-frameworks-strategies-and-best-practices-9dc3cfdf9890
- [53] A Developer’s Guide to Building Scalable AI: Workflows vs Agents. (n.d.). https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/
- [guideline_url] Building effective agents. (2024, December 19). https://www.anthropic.com/engineering/building-effective-agents
- [guideline_url] What is an AI agent?. (2026, April 2). https://cloud.google.com/discover/what-are-ai-agents
- [guideline_url] Real Agents vs. Workflows: The Truth Behind AI 'Agents'. (n.d.). https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s
- [guideline_url] Exploring the difference between agents and workflows. (n.d.). https://decodingml.substack.com/p/llmops-for-production-agentic-rag
- [guideline_url] A Developer’s Guide to Building Scalable AI: Workflows vs Agents. (2025, June 27). https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/
- [guideline_url] 601 real-world gen AI use cases from the world's leading organizations. (2025, October 9). https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
- [guideline_url] Stop Building AI Agents: Here’s what you should build instead. (n.d.). https://decodingml.substack.com/p/stop-building-ai-agents
- [guideline_url] Andrej Karpathy: Software Is Changing (Again). (n.d.). https://www.youtube.com/watch?v=LCEmiRjPEtQ
- [guideline_url] Building Production-Ready RAG Applications: Jerry Liu. (n.d.). https://www.youtube.com/watch?v=TRjq7t2Ms5I
- [guideline_url] Gemini CLI: your open-source AI agent. (n.d.). https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/
- [guideline_url] Gemini CLI README.md. (n.d.). https://github.com/google-gemini/gemini-cli/blob/main/README.md
- [guideline_url] Introducing Perplexity Deep Research. (n.d.). https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research
- [guideline_url] Introducing ChatGPT agent: bridging research and action. (2025, July 17). https://openai.com/index/introducing-chatgpt-agent/