# Workflows vs. Agents: The Critical Decision Every AI Engineer Faces

As an AI engineer preparing to build your first real AI application, one of the first key decisions you will make is how to design your solution. Should it follow a predictable, step-by-step workflow, or does it demand a more autonomous approach, where the LLM makes self-directed decisions? This fundamental question will determine the success or failure of your project and will impact development time, costs, reliability, and user experience.

Choose the wrong approach, and you might end up with an overly rigid system that breaks when users deviate from expected patterns. Or, you could build an unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most. Months of development time can be wasted rebuilding the entire architecture, leading to frustrated users and executives who cannot afford to keep the system running.

In 2024 and 2025, we have seen billion-dollar AI startups succeed or fail based on this architectural decision. The most successful AI engineers and teams know when to use workflows versus agents and, more importantly, how to combine both approaches effectively.

This lesson will provide you with a framework to make this critical decision with confidence. We will explore the fundamental trade-offs between LLM workflows and AI agents, examine real-world examples from leading AI companies, and show you how to design robust systems that leverage the best of both worlds. By the end, you will be equipped to choose the right path for your AI applications.

## Understanding the Spectrum: From Workflows to Agents

Before choosing between workflows and agents, it helps to see them not as a binary choice but as levels on a spectrum of autonomy [[45]](https://lumenalta.com/labs/from-llm-to-full-agency-understanding-the-levels-of-ai-autonomy). We are not focused on the technical specifics yet, but on their core properties.

An **LLM workflow** is a sequence of tasks involving LLM calls or other operations, orchestrated by developer-written code. The steps are defined in advance, creating predictable, rule-based paths. This approach evolved from historical rule-based systems, which were effective for clear-cut instructions but struggled with ambiguity and scale [[46]](https://fetch.ai/blog/evolution-ai-agents-from-rule-based-systems-to-llms-agents). Think of a modern workflow as a factory assembly line, where each station performs a specific task [[2]](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s), [[21]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns). In future lessons, we will explore patterns like chaining and routing.

**AI agents** represent a higher level of autonomy. Here, an LLM dynamically decides the sequence of steps, reasoning, and actions to achieve a goal. The path is not predefined but is planned based on the task and environment. This gives agents flexibility to handle ambiguity and complexity, much like a skilled expert tackling an unfamiliar problem [[17]](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5). We will cover agent-specific concepts like tools, memory, and the ReAct architecture later.

Both require an orchestration layer. In workflows, this layer executes a defined plan. In agents, it facilitates the LLM's dynamic planning and execution.

## Choosing Your Path

In the previous section, we defined LLM workflows and AI agents independently. Now, we will explore their core difference: developer-defined logic versus LLM-driven autonomy.

Most real-world systems exist on a spectrum between rigid workflows and autonomous agents. When building, you have an "autonomy slider" to decide how much control the LLM has [[14]](https://singjupost.com/andrej-karpathy-software-is-changing-again/). For example, Cursor's coding assistance ranges from simple completion to rewriting a repository. Perplexity offers everything from a quick search to a deep research function that takes minutes to generate a report [[12]](https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx).

The ultimate goal is to speed up the loop between AI generation and human verification. This is often achieved through a well-designed architecture and a user-friendly interface that makes it easy for humans to review and guide the AI's work.

```mermaid
flowchart LR
    A["Start"] --> B["AI System"]
    B -- "performs" --> C["Generation"]
    C -- "produces" --> D["AI Output"]
    D -- "sent to" --> E["Human"]
    E -- "evaluates" --> F{"Verification Result?"}
    F -- "Accept Output" --> G["End Loop"]
    F -- "Provide Feedback" --> H["Feedback"]
    H -- "informs refinement" --> B
```

Image 1: A flowchart illustrating the iterative loop between AI generation and human verification.

You should use an **LLM workflow** for well-defined tasks like data extraction or report generation. Workflows offer predictability, reliability, and easier debugging, with more predictable costs and latency. This makes them ideal for regulated fields like finance and healthcare, where AI-powered administrative systems already help coordinate patient care [[47]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360800/). Their main weakness is rigidity. You should use an **AI agent** for open-ended tasks like research or code debugging. Agents adapt to new situations but are less reliable, harder to debug, and pose security risks.

The choice also impacts how you measure success. For a workflow generating a financial report, you might use reference-free metrics that assess the correctness of financial takeaways and reasoning [[48]](https://arxiv.org/html/2504.14233v1). For an agent, you would focus on metrics like action completion, tool selection quality, and reasoning coherence [[49]](https://galileo.ai/blog/accuracy-metrics-ai-evaluation).

## Exploring Common Patterns

To build your intuition, let's look at the most common patterns for constructing both workflows and agents. We will cover these in detail in future lessons, but for now, the goal is to understand the high-level concepts.

For LLM workflows, we often use patterns like:
*   **Chaining and routing**, which automates sequences of LLM calls and directs the flow based on specific conditions. This is a foundational step in building more complex automations [[21]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns).

```mermaid
flowchart LR
  %% Workflow Start
  A["Input"] --> B{"Router LLM"}

  %% Routing Decision
  B -->|"Route to Chain 1"| C["LLM Call 1"]
  B -->|"Route to Chain 2"| D["LLM Call 2"]
  B -->|"Route to Chain 3"| E["LLM Call 3"]

  %% Chains/Sub-workflows converge
  C --> F["Final Output"]
  D --> F
  E --> F
```

Image 2: A flowchart illustrating the "Chaining and Routing" pattern for LLM workflows.

*   The **orchestrator-worker** pattern involves a central orchestrator that understands user intent, dynamically plans sub-tasks, and delegates them to specialized workers. This creates a smooth transition from rigid workflows to more dynamic, agent-like behavior [[25]](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/).

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

Image 3: A flowchart illustrating the Orchestrator-Worker pattern with an Orchestrator LLM delegating tasks to multiple Worker LLMs and synthesizing results.

*   The **evaluator-optimizer loop** is used to auto-correct LLM outputs. One LLM generates a response, while another acts as a reviewer, providing feedback to help the first LLM refine its answer. This is similar to how a human writer improves a document based on an editor's comments [[30]](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html).

```mermaid
flowchart LR
  %% LLM Agents
  G["Generator LLM"]
  E["Evaluator LLM"]

  %% Outputs
  IO["Initial Output"]
  F["Feedback"]
  FO["Final Output"]

  %% Evaluation Process
  RF["Review & Feedback"]
  MC{"Meets Criteria?"}

  %% Flow
  G -- "produces" --> IO
  IO -- "sent to" --> E
  E -- "performs" --> RF
  RF -- "leads to" --> MC
  MC -- "Yes" --> FO
  MC -- "No" --> F
  F -- "for Revision" --> G

  %% Visual grouping
  classDef llm stroke-width:2px
  classDef output stroke-dasharray:3,3
  class G,E llm
  class IO,F,FO output
```

Image 4: A flowchart illustrating the Evaluator-Optimizer Loop pattern.

The core of nearly all modern agents is the **ReAct (Reason and Act)** pattern. This architecture allows an agent to decide what action to take, interpret the output of that action, and repeat the cycle until its task is complete. A ReAct agent typically consists of an LLM for reasoning, tools for taking actions, and both short-term (working) and long-term (knowledge) memory [[5]](https://developers.google.com/gemini-code-assist/docs/gemini-cli). As systems evolve from stateless tools to persistent collaborators, memory architecture is becoming a core concern, with advanced designs that allow memory to evolve and form interconnected knowledge networks [[50]](https://arxiv.org/html/2601.09913v1). We will explore this pattern in detail in future lessons.

```mermaid
flowchart LR
  %% Agent Memory
  subgraph "Agent Memory"
    STM["Short-term Memory<br/>(Working Context)"]
    LTM["Long-term Memory<br/>(Knowledge Base)"]
  end

  %% Core Agent
  LLM["LLM<br/>(Reasoning & Planning)"]

  %% External Interaction
  TOOLS["Tools<br/>(Actions)"]

  %% Flow
  STM -- "provides context" --> LLM
  LTM -- "provides knowledge" --> LLM

  LLM -- "1. Reasons & Selects Tool" --> TOOLS
  TOOLS -- "2. Executes Action & Returns Output" --> LLM
  LLM -- "3. Observes Output & Updates Memory" --> STM
  LLM -- "3. Observes Output & Updates Memory" --> LTM

  %% Cycle Repetition
  STM -- "4. Context for Next Cycle" --> LLM
  LTM -- "4. Knowledge for Next Cycle" --> LLM

  %% Visual Grouping
  classDef memory stroke-dasharray:3,3
  classDef core_agent stroke-width:2px
  classDef external_action stroke-width:2px
  class STM,LTM memory
  class LLM core_agent
  class TOOLS external_action
```

Image 5: Flowchart illustrating the ReAct pattern in an AI agent, showing the cyclical interaction between the LLM, tools, and memory components.

## Zooming In on Our Favorite Examples

To make these concepts more concrete, let's analyze a few real-world examples, from a simple workflow to a more advanced hybrid system.

### Document Summarization in Google Workspace

A common problem in team environments is finding the right information quickly within large documents. An embedded summarization feature can save time and guide search strategies. This is a perfect use case for a simple, multi-step LLM workflow [[3]](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models), [[1]](https://support.google.com/docs/answer/15627020?hl=en).

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

Image 6: A flowchart illustrating a simple LLM workflow for document summarization and analysis using Gemini in Google Workspace.

This is a pure workflow. A chain of LLM calls reads a document, summarizes it, extracts key points, and displays the result. Each step is predefined, making the process reliable and easy to follow.

### Gemini CLI Coding Assistant

Writing code can be a slow process, involving reading documentation and understanding new codebases. An AI coding assistant can significantly speed this up. The open-source Gemini CLI is a single-agent system that uses a ReAct-like architecture to help developers write, debug, and understand code [[5]](https://developers.google.com/gemini-code-assist/docs/gemini-cli). It can write code from scratch, assist with specific functions, generate documentation, and more.

The operational loop looks like this:
1.  **Context Gathering**: The agent loads the codebase, tools, and history.
2.  **Reasoning**: The LLM plans the required actions.
3.  **Validation**: The user approves the plan.
4.  **Execution**: The agent uses its tools (e.g., file access, code generation).
5.  **Evaluation**: The agent runs or compiles the code to check it.
6.  **Loop**: The agent decides if the task is done or if it needs to repeat the cycle.

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

### Perplexity's Deep Research

Researching a new topic can be daunting. Perplexity's Deep Research feature is a hybrid system that combines ReAct reasoning with workflow patterns to conduct expert-level autonomous research [[8]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research). It uses multiple specialized agents, orchestrated in parallel, to perform dozens of searches across hundreds of sources, delivering a comprehensive report in minutes [[6]](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/). This multi-agent approach mirrors coordination strategies seen in robotics, where complex tasks are broken down for multiple specialized robots to solve in parallel [[51]](https://openaccess.thecvf.com/content/CVPR2025W/MEIS/papers/Chen_Multi-Agent_Systems_for_Robotic_Autonomy_with_LLMs_CVPRW_2025_paper.pdf).

A simplified view of its process:
1.  **Planning**: An orchestrator agent decomposes the research question into sub-questions.
2.  **Parallel Gathering**: To reduce latency, specialized search agents execute simple, single-entity search queries in parallel rather than running one complex query sequentially [[52]](https://docs.perplexity.ai/docs/agent-api/presets).
3.  **Synthesis**: Each agent validates and summarizes its sources.
4.  **Refinement**: The orchestrator identifies knowledge gaps and generates follow-up queries, repeating the process.
5.  **Report Generation**: The orchestrator combines all results into a final, cited report.

This hybrid system uses the orchestrator-worker pattern to supervise multiple agents, combining the structure of a workflow with the flexibility of agents.

```mermaid
flowchart LR
  %% Initial Research Phase
  RQ["Research Question"] --> ORCH["Orchestrator<br/>(Research Planning & Decomposition)"]
  ORCH -- "decomposes into" --> SUBQ["Sub-questions"]

  %% Iterative Research Process
  subgraph "Iterative Research Process"
    direction LR
    SUBQ --> PIG["Parallel Information Gathering<br/>(Specialized Search Agents)"]
    PIG -- "sends results to" --> ANASYN["Analysis & Synthesis<br/>(Validate, Score, Summarize)"]
    ANASYN -- "provides insights to" --> IRA["Iterative Refinement & Gap Analysis"]
    IRA --> GAPS{"Knowledge Gaps Remain?"}
    GAPS -- "Yes" --> GFQ["Generate Follow-up Queries"]
    GFQ -- "feeds into" --> PIG
  end

  %% Tool Interaction
  PIG -- "uses" --> TOOLS["Tools<br/>(Web Search, Document Retrieval)"]
  TOOLS -. "returns data" .-> PIG

  %% Final Output
  GAPS -- "No" --> FRG["Final Report Generation<br/>(with Citations)"]

  %% Visual grouping
  classDef decision fill:#fff,stroke:#333,stroke-width:2px
  class GAPS decision
```

Image 8: A flowchart illustrating Perplexity's Deep Research agent's iterative multi-step process.

## The Challenges of Every AI Engineer

Now that you understand the spectrum from LLM workflows to AI agents, it is important to recognize that every AI engineer faces these same fundamental challenges. The architectural decisions you make will determine whether your AI application succeeds in production or fails spectacularly.

Every AI engineer battles daily challenges like reliability issues, where an agent that works in a demo becomes unpredictable with real users. Systems struggle with context limits, losing coherence over long conversations, and integrating data from multiple sources is a constant struggle. Furthermore, there is the cost-performance trap, where sophisticated agents deliver impressive results but at an economically unfeasible price [[15]](https://arxiv.org/html/2510.25423v2). Finally, autonomous agents pose significant security risks. In multi-agent systems, vulnerabilities like "capability bleed"—where one agent gains unintended access to another's tools—or the rapid spread of contaminated data can compromise the entire system [[53]](https://www.knostic.ai/blog/multi-agent-security).

The good news is that these challenges are solvable. In upcoming lessons, we will cover patterns for building reliable AI products, including structured outputs, memory management, and robust evaluation pipelines. We will explore strategies for creating hybrid systems and keeping costs and latency under control.

By the end of this course, you will have the knowledge to architect AI systems that are not only powerful but also robust, efficient, and safe. You will know when to use a workflow, when to deploy an agent, and how to build effective hybrid systems that work in the real world.

## References

- [1] [How does Gemini document summarization workflow operate in Google Workspace?](https://support.google.com/docs/answer/15627020?hl=en)
- [2] [Real Agents vs. Workflows: The Truth Behind AI 'Agents'](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s)
- [3] [Long document summarization with Workflows and Gemini models](https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models)
- [4] [How does Gemini document summarization workflow operate in Google Workspace?](https://knowledge.workspace.google.com/admin/gemini/google-workspace-with-gemini)
- [5] [What ReAct pattern does Gemini CLI coding assistant implement?](https://developers.google.com/gemini-code-assist/docs/gemini-cli)
- [6] [How does Perplexity Deep Research hybrid agent orchestrate parallel research?](https://zenvanriel.com/ai-engineer-blog/perplexity-computer-multi-model-agent-orchestration/)
- [7] [How does Perplexity Deep Research hybrid agent orchestrate parallel research?](https://www.gend.co/blog/perplexity-computer-ai-agent-orchestration)
- [8] [Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [9] [How does Perplexity Deep Research hybrid agent orchestrate parallel research?](https://www.digitalapplied.com/blog/perplexity-agent-api-platform-ai-search-developer-guide)
- [10] [What autonomy slider examples use Cursor and Perplexity in Karpathy talk?](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6)
- [11] [What autonomy slider examples use Cursor and Perplexity in Karpathy talk?](https://andrewships.substack.com/p/autonomy-sliders)
- [12] [What autonomy slider examples use Cursor and Perplexity in Karpathy talk?](https://www.linkedin.com/posts/markbarbir_andrej-karpathys-latest-talk-describes-our-activity-7343449417426837505-oTFx)
- [13] [What autonomy slider examples use Cursor and Perplexity in Karpathy talk?](https://www.latent.space/p/s3)
- [14] [Andrej Karpathy: Software Is Changing (Again)](https://singjupost.com/andrej-karpathy-software-is-changing-again/)
- [15] [What reliability context and security challenges face AI engineers building agents?](https://arxiv.org/html/2510.25423v2)
- [16] [What reliability context and security challenges face AI engineers building agents?](https://permiso.io/blog/8-critical-ai-security-challenges)
- [17] [What reliability context and security challenges face AI engineers building agents?](https://medium.com/@ananya_95177/key-challenges-in-ai-agent-development-and-how-to-solve-them-460fceb0a6d5)
- [18] [AI Agents Are Here. So Are the Threats.](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [19] [What reliability context and security challenges face AI engineers building agents?](https://www.cyberark.com/resources/blog/the-agentic-ai-revolution-5-unexpected-security-challenges)
- [20] [How does chaining and routing work in LLM workflows?](https://mirascope.com/blog/llm-chaining)
- [21] [How does chaining and routing work in LLM workflows?](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [22] [How does chaining and routing work in LLM workflows?](https://orq.ai/blog/prompt-structure-chaining)
- [23] [How does chaining and routing work in LLM workflows?](https://www.geeksforgeeks.org/artificial-intelligence/llm-chains/)
- [24] [How does chaining and routing work in LLM workflows?](https://www.promptingguide.ai/techniques/prompt_chaining)
- [25] [What is orchestrator-worker pattern for LLM to agent transition?](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/)
- [26] [What is orchestrator-worker pattern for LLM to agent transition?](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [27] [What is orchestrator-worker pattern for LLM to agent transition?](https://www.linkedin.com/posts/seanf_the-orchestrator-worker-pattern-is-a-well-known-activity-7294775230353313792-_zFL)
- [28] [Orchestrator-Workers Workflow](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [29] [What is orchestrator-worker pattern for LLM to agent transition?](https://gurusup.com/blog/agent-orchestration-patterns)
- [30] [How does evaluator-optimizer loop auto-correct LLMs with reflection?](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html)
- [31] [How does evaluator-optimizer loop auto-correct LLMs with reflection?](https://dev.to/clayroach/building-self-correcting-llm-systems-the-evaluator-optimizer-pattern-169p)
- [32] [How does evaluator-optimizer loop auto-correct LLMs with reflection?](https://vadim.blog/the-research-on-llm-self-correction)
- [33] [How does evaluator-optimizer loop auto-correct LLMs with reflection?](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer)
- [34] [How does evaluator-optimizer loop auto-correct LLMs with reflection?](https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow)
- [35] [A Developer’s Guide to Building Scalable AI: Workflows vs Agents](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)
- [36] [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [37] [Exploring the difference between agents and workflows](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
- [38] [What is an AI agent?](https://cloud.google.com/discover/what-are-ai-agents)
- [39] [601 real-world gen AI use cases from the world's leading organizations](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- [40] [Stop Building AI Agents: Here’s what you should build instead](https://decodingml.substack.com/p/stop-building-ai-agents)
- [41] [Building Production-Ready RAG Applications: Jerry Liu](https://www.youtube.com/watch?v=TRjq7t2Ms5I)
- [42] [Gemini CLI: your open-source AI agent](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [43] [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/README.md)
- [44] [Introducing ChatGPT agent: bridging research and action](https://openai.com/index/introducing-chatgpt-agent/)
- [45] [From LLM to full agency: Understanding the levels of AI autonomy](https://lumenalta.com/labs/from-llm-to-full-agency-understanding-the-levels-of-ai-autonomy)
- [46] [The Evolution of AI Agents: From Rule-Based Systems to LLMs Agents](https://fetch.ai/blog/evolution-ai-agents-from-rule-based-systems-to-llms-agents)
- [47] [AI-Powered Health Care Administrative Workflow Systems](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360800/)
- [48] [Making LLaMA SEE and HEAR: A Comprehensive Study of Modality Adapters in Large Vision-Language Models](https://arxiv.org/html/2504.14233v1)
- [49] [A Guide to Accuracy Metrics in AI Evaluation](https://galileo.ai/blog/accuracy-metrics-ai-evaluation)
- [50] [Memory as a System: A Survey of Computational Memory in AI](https://arxiv.org/html/2601.09913v1)
- [51] [Multi-Agent Systems for Robotic Autonomy with LLMs](https://openaccess.thecvf.com/content/CVPR2025W/MEIS/papers/Chen_Multi-Agent_Systems_for_Robotic_Autonomy_with_LLMs_CVPRW_2025_paper.pdf)
- [52] [Agent API Presets](https://docs.perplexity.ai/docs/agent-api/presets)
- [53] [How to Secure Multi-Agent AI Systems](https://www.knostic.ai/blog/multi-agent-security)