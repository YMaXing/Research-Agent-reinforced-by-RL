# Lesson 3: Context Engineering

## Introduction: When prompt engineering breaks

AI applications have evolved rapidly. In 2022, we had simple chatbots for question-and-answering. By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge. 2024 brought us tool-using agents that could perform actions. Now, we are building memory-enabled agents that remember past interactions and build relationships over time [[1]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/).

In our last lesson, we explored how to choose between AI agents and LLM workflows when designing a system. As these applications grow more complex, prompt engineering, a practice that once served us well, is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The sheer volume of information an agent might need—past conversations, user data, documents, and action descriptions—has grown exponentially. Simply stuffing all this into a prompt is not a viable strategy [[2]](https://blog.langchain.com/context-engineering-for-agents/). The discipline of context engineering addresses this challenge. It orchestrates the entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it. This skill is becoming a core foundation for AI engineering.

## From Prompt to Context Engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event [[3]](https://sombrainc.com/blog/ai-context-engineering-guide). This approach breaks down in stateful applications where context must be preserved and managed across multiple turns.

As a conversation or task progresses, the context grows. Without a strategy to manage this growth, the LLM’s performance degrades. This is context decay: the model gets confused by the noise of an ever-expanding history and starts to lose track of the original instructions or key information [[4]](https://atlan.com/know/llm-context-window-limitations/).

Even with large context windows, a physical limit exists for what you can include. Furthermore, every token adds to the cost and latency of an LLM call [[5]](https://www.comet.com/site/blog/context-window/). The naive approach of "context-augmented generation," or just dumping everything in, is a recipe for failure in production. We will explore these concepts in more detail in upcoming lessons, including memory in Lesson 9 and RAG in Lesson 10.

On a recent project, we learned this the hard way. We were working with a model that supported a two-million-token context window, so we thought, "*What could go wrong*?" We stuffed everything in: our research, guidelines, examples, and reviews. The result was an LLM workflow that took 30 minutes to run and produced low-quality outputs.

Context engineering becomes essential to address these limitations. It shifts the focus from crafting static prompts to building dynamic systems that manage information flow. As an AI Engineer, your job is to select only the most critical pieces of context for each LLM call. This makes your applications accurate, fast, and cost-effective.

## Understanding Context Engineering

Context engineering is the discipline of finding the best way to arrange information from your application's memory into the context passed to an LLM. Formally, it is an optimization problem: finding the ideal set of functions to assemble a context that maximizes the quality of the LLM's output for a given task [[6]](https://arxiv.org/pdf/2507.13334). You retrieve the right parts from your short-term and long-term memory to solve a specific task without overwhelming the model. For example, when you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies or taste preferences. This precise selection ensures the model receives only the essential information.

Andrej Karpathy explains that LLMs are like a new kind of operating system where the model is the CPU and its context window is the RAM. Just as an operating system manages what fits into your computer’s limited RAM, context engineering manages what information occupies the model’s limited context window [[2]](https://blog.langchain.com/context-engineering-for-agents/). The model's weights are like ROM (Read-Only Memory), burned in during training, while external sources like vector stores are like disk storage—vast but passive until explicitly loaded into the context window [[7]](https://atlan.com/know/working-memory-llms/).

How does context engineering relate to prompt engineering? It's simple. Prompt engineering is a subset of context engineering. You still write effective prompts, but you also design a system that feeds the right context into those prompts [[8]](https://memgraph.com/blog/prompt-engineering-vs-context-engineering). This means understanding not just *how* to phrase a task, but *what* information the model needs to perform optimally.

| Dimension | Prompt Engineering | Context Engineering |
| --- | --- | --- |
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Stateless function | Stateful due to memory |
| Focus | How to phrase tasks | What information to provide |

Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible. Data changes constantly, making fine-tuning a last resort. For most enterprise use cases, you get better results faster and more cheaply with context engineering [[9]](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m). It allows for rapid iteration and adaptation to evolving data without altering the core model, a key advantage in dynamic environments. This approach avoids the computational resources and specialized expertise required for retraining, offering a more agile path to reliable AI applications.

When you start a new AI project, your decision-making process for guiding the LLM should look like the one presented in Image 1.

```mermaid
graph TD
    A["Prompt Engineering"] --> B{"Solves problem?"}
    B -->|"Yes"| C["Stop"]
    B -->|"No"| D["Context Engineering"]
    D --> E{"Solves problem?"}
    E -->|"Yes"| C
    E -->|"No"| F["Fine-tuning"]
    F --> G{"Fine-tuning dataset<br/>can be made?"}
    G -->|"Yes"| C
    G -->|"No"| H["Reframe the problem"]
```
Image 1: Flowchart illustrating the decision-making process for choosing an AI strategy.

For instance, if you build an agent to process internal Slack messages, you do not need to fine-tune a model on your company’s communication style. It is more effective to use a powerful reasoning model and engineer the context to retrieve specific messages and enable actions like creating tasks or drafting emails. Throughout this course, we will show you how to solve most industry problems using only context engineering.

## What Makes Up the Context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model.

The high-level workflow, as presented in Image 2, begins when a user input triggers the system to pull relevant information from both long-term and short-term memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
flowchart LR
    A["User Input"] -- "provides" --> B["Long-term Memory"]
    B -- "retrieves relevant info" --> C["Short-Term Working Memory"]
    C -- "forms" --> D["Context"]
    D -- "fills" --> E["Prompt Template"]
    E -- "generates" --> F["Prompt"]
    F -- "sends to" --> G["LLM Call"]
    G -- "produces" --> H["Answer"]

    H -- "updates" --> C
    C -- "stores" --> B

    classDef memory stroke-dasharray:3,3
    class B,C memory
```
Image 2: High-level workflow of context building and utilization in an LLM application.

These components are grouped into two main categories. We will explain them intuitively for now, as we have future dedicated lessons for all of them.

### Short-Term Working Memory

Short-term working memory is the state of the agent for the current task or conversation. It is volatile and changes with each interaction, helping the agent maintain a coherent dialogue and make immediate decisions. It can include some or all of these components [[10]](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/):

- **User input:** The most recent query or command from the user.
- **Message history:** The log of the current conversation, including the back-and-forth between the user and the agent. This allows the LLM to understand the flow and previous turns.
- **Agent's internal thoughts:** The reasoning steps the agent takes to decide on its next action, often called a scratchpad.
- **Action calls and outputs:** The results from any actions the agent has performed, providing fresh information from external systems like databases or APIs.

### Long-Term Memory

Long-term memory is more persistent and stores information across sessions, allowing the AI system to remember things beyond a single conversation. We divide it into three types, drawing parallels from human memory [[11]](https://www.datacamp.com/blog/how-does-llm-memory-work). As before, an AI system can include some or all of them:

- **Procedural memory:** This is the "how-to" knowledge encoded directly in the code. It includes the system prompt, which sets the agent's overall behavior and persona. It also includes the definitions of available actions, which tell the agent what it can do, and schemas for structured outputs, which guide the format of its responses. Think of this as the agent's built-in skills.
- **Episodic memory:** This is memory of specific past experiences, like user preferences or previous interactions. It's used to help the agent personalize its responses based on individual users. We typically store this in vector or graph databases for efficient retrieval, allowing the agent to recall facts like "the user prefers concise answers" [[12]](https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/).
- **Semantic memory:** This is the agent’s general knowledge base. It can be internal, like company documents stored in a data lake, or external, accessed via the internet through API calls or web scraping. This memory provides the factual information the agent needs to answer questions accurately [[13]](https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/).

If this seems like a lot, bear with us. We will cover all these concepts in-depth in future lessons, including structured outputs (Lesson 4), actions (Lesson 6), memory (Lesson 9), RAG (Lesson 10), and working with multimodal data in Lesson 11.![An architectural diagram of an AI agent, showing how user input flows into short-term memory, which then interacts with long-term memory (databases and MCP servers) and action tools to generate a context for a prompt.](https://i.imgur.com/Qh15c0m.jpeg)
Image 3: A detailed illustration of how all the context engineering components work together inside an AI agent. (Source [DECODING ML](https://www.decodingml.com))

The key takeaway is that these components are not static. They are dynamically re-computed for every single interaction. For each conversation turn or new task, the short-term memory grows, or the long-term memory can change. Context engineering involves knowing how to select the right pieces from this vast memory pool to construct the most effective prompt for the task at hand.

## Production Implementation Challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These challenges all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that come up when building AI applications:

**The context window challenge** is a primary concern. Every AI model has a limited context window, the maximum amount of information (tokens) it can process at once. This is similar to your computer's RAM. If your machine has only 32GB of RAM, that is all it can use at one time. While context windows are getting larger, they are not infinite, and treating them as such leads to other problems [[5]](https://www.comet.com/site/blog/context-window/).

**Information overload** is another major issue. Too much context reduces the performance of the LLM by confusing it. This is known as the "lost-in-the-middle" or "needle in the haystack" problem, where LLMs are known for remembering information best at the beginning and end of the context window. Performance can drop long before the physical context limit is reached; benchmarks show that even models with large context windows see performance degrade at 100K tokens, and multi-turn conversation accuracy can drop by nearly 40% compared to single-turn tasks [[14]](https://www.adaline.ai/blog/top-agentic-llm-models-frameworks-for-2026), [[15]](https://reinteractive.com/articles/ai-real-world-use-cases/solving-ai-agent-amnesia-context-rot-and-lost-in-the-middle). This overload can also lead to specific failure modes like *poisoning* (compounding hallucinations), *distraction* from irrelevant data, and *confusion* between multiple tasks [[16]](https://cursor.directory/plugins/context-engineering), [[17]](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e), [[18]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2).

**Context drift** occurs when conflicting views of truth accumulate over time. For example, the memory might contain two conflicting statements: "*The user's budget is $500*" and later "*The user's budget is $1,000*." This data conflict confuses the LLM. Over long interactions, this can lead to "agent drift," where an agent's behavior degrades. Studies show task success can drop by over 40% after just a few dozen interactions as the agent's reasoning becomes polluted by outdated or contradictory information [[19]](https://arxiv.org/html/2601.04170v1). Without a mechanism to resolve these conflicts, the model's responses become unreliable [[20]](https://galileo.ai/blog/production-llm-monitoring-strategies), [[21]](https://thenewstack.io/context-rot-enterprise-ai-llms/).

**Tool confusion** arises in two main ways. First, adding too many actions to an agent (often 100+) can confuse the LLM about the best one for the job. Second, confusion can occur when tool descriptions are poorly written or overlap. If the distinctions between actions are unclear, even a human would struggle to choose the right one. The Gorilla benchmark, for instance, shows that nearly all models perform worse when given more than one tool [[22]](https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots).

## Key Strategies for Context Optimization

Initially, most AI applications were chatbots over single knowledge bases. Today, modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements. A useful framework for this is the "Four-Bucket Mitigation" strategy: **write** context to external storage, **select** only relevant information, **compress** it, and **isolate** it across specialized components [[16]](https://cursor.directory/plugins/context-engineering).

Here are four popular context engineering strategies used across the industry:

### Selecting the Right Context

Retrieving the right information from memory is a critical first step. A common mistake is to provide everything at once, assuming that models with large context windows can handle it. As we've discussed, the "lost-in-the-middle" problem often leads to poor performance, increased latency, and higher costs [[4]](https://atlan.com/know/llm-context-window-limitations/).

To solve this, you can **use structured outputs** by defining clear schemas for what the LLM should return. This allows you to pass only the necessary, structured information to downstream steps, which we will cover in detail in Lesson 4. Another key strategy is to **use RAG** to fetch only the specific chunks of text needed to answer a user's question, rather than entire documents. Advanced RAG techniques further refine this by transforming the user's query for better retrieval or re-ranking the retrieved chunks for relevance [[23]](https://www.sundeepteki.org/blog/context-engineering-a-framework-for-robust-generative-ai-systems). We will explore this in Lesson 10.

It is also effective to **reduce the number of available actions**. Instead of giving an agent access to every available action, you can delegate action subsets to specialized components, such as through an orchestrator-worker pattern. Limiting the selection to under 30 tools can triple selection accuracy. For **time-sensitive information**, you should rank it by date and filter out anything no longer relevant [[24]](https://www.dailydoseofds.com/llmops-crash-course-part-8/). Finally, for the most important instructions, it is recommended to **repeat them at both the start and the end of the prompt**. This leverages the model's tendency to pay more attention to the context edges, ensuring core instructions are not lost [[25]](https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect).

```mermaid
flowchart LR
  %% Input
  UserQuery["User Query"]

  %% Memory and Retrieval
  subgraph "Memory & Retrieval"
    LTM["Long-Term Memory<br/>(Knowledge Bases, User Preferences)"]
    RAG["RAG<br/>(Retrieval Augmented Generation)"]
    TSM["Tool Selection/Management<br/>(Reducing Tools)"]
  end

  %% Context Assembly
  subgraph "Context Assembly"
    SO["Structured Outputs<br/>(Formatting)"]
    TR["Temporal Relevance<br/>(Ordering)"]
    RCI["Repeating Core Instructions<br/>(Emphasis)"]

    SO -- "formatted context" --> TR
    TR -- "ordered context" --> RCI
  end

  %% Core Model & Output
  subgraph "LLM & Output"
    LLM["LLM"]
    Answer["Answer"]
  end

  %% Primary Data Flows
  UserQuery -- "informs retrieval" --> LTM
  LTM -- "retrieved data" --> RAG

  UserQuery -- "query" --> RAG
  UserQuery -- "tool request" --> TSM

  RAG -- "augmented context" --> SO
  TSM -- "selected tools" --> SO
  UserQuery -- "direct instructions" --> SO

  RCI -- "final context" --> LLM
  LLM -- "generates" --> Answer

  %% Visual Grouping
  classDef inputOutput stroke-width:2px
  classDef memory stroke-dasharray: 5 5
  classDef process stroke-width:2px
  classDef assembly stroke-dasharray: 3 3

  class UserQuery,Answer inputOutput
  class LTM memory
  class RAG,TSM process
  class SO,TR,RCI assembly
  class LLM process
```
Image 4: System diagram illustrating context selection strategies for an LLM, including RAG, tool management, and context assembly stages.

### Context Compression

As message history grows in short-term working memory, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns, as the LLM still needs to remember what happened. Instead, you need ways to compress key facts from the past.

One approach is **creating summaries of past interactions** using an LLM to replace a long, detailed history with a concise overview [[26]](https://blog.jetbrains.com/research/2025/12/efficient-context-management/). You can also improve efficiency by **moving user preferences to long-term memory**, transferring them from the working context to a persistent episodic memory store. This keeps the working context clean while ensuring preferences are remembered for future sessions. Finally, **deduplication** helps by removing redundant information from the context to avoid repetition [[27]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view).

```mermaid
flowchart LR
    %% Initial Memory
    STM_Initial["Short-Term Working Memory<br/>(e.g., message history)"]

    %% Context Compression Processes
    subgraph "Context Compression Strategies"
        SUM_PROC["Creating Summaries of Past Interactions<br/>(using LLM)"]
        PREF_PROC["Moving User Preferences to Episodic Long-Term Memory"]
    end

    %% Outputs of Compression
    SUM_HIST["Summarized History"]
    ELTM["Episodic Long-Term Memory"]
    STM_Reduced["Short-Term Working Memory<br/>(Remaining)"]

    %% Final Context for LLM
    LLM_CONTEXT["Context<br/>for the LLM"]

    %% Primary Data Flows
    STM_Initial -- "input for summarization" --> SUM_PROC
    SUM_PROC -- "generates" --> SUM_HIST

    STM_Initial -- "extracts preferences" --> PREF_PROC
    PREF_PROC -- "stores to" --> ELTM

    %% Showing reduction of Short-Term Memory
    STM_Initial -. "processed & reduced" .-> STM_Reduced

    %% Contribution to LLM Context
    SUM_HIST -- "contributes to" --> LLM_CONTEXT
    STM_Reduced -- "contributes to" --> LLM_CONTEXT

    %% Visual Grouping
    classDef memory stroke-dasharray:3,3
    classDef process stroke-width:2px

    class STM_Initial,SUM_HIST,ELTM,STM_Reduced,LLM_CONTEXT memory
    class SUM_PROC,PREF_PROC process
```
Image 5: A flowchart illustrating context compression strategies, showing how short-term memory is processed into summarized history and reduced memory for LLM context, with user preferences moved to long-term memory.

### Isolating Context

Another powerful strategy is to isolate context by splitting information across multiple agents or LLM workflows. This technique is similar to tool isolation but it's more general, referring to the whole context. The key idea is that instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context [[28]](https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering).

We often implement this using an orchestrator-worker pattern, where a central orchestrator agent breaks down a problem and assigns sub-tasks to specialized worker agents [[29]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production). Each worker operates in its own isolated context, which prevents cross-domain hallucinations, reduces token consumption by 60-70%, and allows for parallel processing [[30]](https://gurusup.com/blog/multi-agent-orchestration-guide). We will cover this pattern in more detail in Lesson 5.

```mermaid
flowchart LR
  %% Input
  CT["Complex Task"]

  %% Orchestrator
  OA["Orchestrator Agent"]
  ST["Subtasks"]

  %% Worker Agents Subgraph
  subgraph "Worker Agents"
    WAA["Worker Agent A"]
    ICWA["Isolated Context Window<br/>(Agent A)"]
    WAB["Worker Agent B"]
    ICWB["Isolated Context Window<br/>(Agent B)"]
  end

  %% Output
  FA["Final Answer"]

  %% Primary Data Flows
  CT -- "receives" --> OA
  OA -- "decomposes into" --> ST
  ST -- "delegates to" --> WAA
  ST -- "delegates to" --> WAB

  WAA -- "returns Subtask Results" --> OA
  WAB -- "returns Subtask Results" --> OA

  OA -- "aggregates results & produces" --> FA

  %% Context Isolation (indirect relationship)
  WAA -. "operates with" .-> ICWA
  WAB -. "operates with" .-> ICWB

  %% Visual Grouping
  classDef agent stroke-width:2px
  classDef context stroke-dasharray:3,3
  class OA,WAA,WAB agent
  class ICWA,ICWB context
```
Image 6: An architecture diagram illustrating the Orchestrator-Worker pattern for context isolation.

### Format Optimization

Finally, the way you format the context matters. Models are sensitive to structure, and using clear delimiters can improve performance. A common strategy is to **use XML tags** to wrap different pieces of context (e.g., `<user_query>`, `<documents>`). This helps the model distinguish between different types of information and makes it easier to reference context elements within the system prompt [[31]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Another useful tip is to **prefer YAML over JSON** when providing structured data as input, as YAML is often more token-efficient and can help save space in your context window.

You always have to understand what is passed to the LLM. Seeing exactly what occupies your context window at every step is key to mastering context engineering. This is done by monitoring your traces, tracking what happens at each step, and understanding the inputs and outputs [[32]](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/). For RAG systems, observability tools can measure specific metrics like **Contextual Precision** and **Contextual Recall**, which helps you quantitatively assess the quality of your context [[33]](https://www.comet.com/site/blog/llm-evaluation-frameworks/). As this is a significant step to go from PoC to production, we will have dedicated lessons on this.

## Here is an Example

Let's connect the theory and strategies discussed earlier with concrete examples. Many real-world use cases require maintaining context across multiple interactions. In **healthcare**, an AI assistant can access a patient's medical history, current symptoms, and the latest medical literature to provide personalized diagnostic support [[34]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). In **financial services**, AI systems integrate with enterprise tools like Customer Relationship Management (CRM) systems, emails, and calendars to generate tailored advice. For **project management**, an AI can access tools like CRMs, Slack, and task managers to automatically understand project requirements and update tasks. Similarly, a **content creator assistant** can use your research, past content, and personality traits to create new content.

Let's walk through a specific query to see context engineering in action with the healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the AI attempts to answer, a context engineering system performs several steps. First, it retrieves the user's patient history, known allergies, and lifestyle habits from episodic memory. Next, it queries a medical database for non-pharmacological headache remedies from semantic memory. The system then assembles the key units of information from both memory types into the final context. After that, it formats this information into a structured prompt and calls the LLM. Finally, it presents a personalized, context-aware answer to the user.

Here is a simplified Python example showing how you might structure the context and prompt for the LLM, using XML tags to format the different context elements. Notice the clear structure and ordering of the prompt components [[34]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

```python
SYSTEM_PROMPT = """
You are a helpful and cautious AI healthcare assistant. Your goal is to provide safe, non-medicinal advice. Do not provide medical diagnoses.

<INSTRUCTIONS>
1. Analyze the user's query and the provided context.
2. Use the patient history to understand their health profile and preferences.
3. Use the retrieved medical knowledge to form your recommendation.
4. If you lack sufficient information, ask clarifying questions.
5. Always prioritize safety and advise consulting a doctor for serious issues.
</INSTRUCTIONS>

<PATIENT_HISTORY>
{retrieved_patient_history}
</PATIENT_HISTORY>

<MEDICAL_KNOWLEDGE>
{retrieved_medical_articles}
</MEDICAL_KNOWLEDGE>

<CONVERSATION_HISTORY>
{formatted_chat_history}
</CONVERSATION_HISTORY>

<USER_QUERY>
{user_query}
</USER_QUERY>

Based on all the information above, provide a helpful response.
"""
```

To build such a system, you need a robust tech stack. Here is a potential stack we recommend and will use throughout this course:

-   **LLM:** Gemini as a multimodal, reasoning, and cost-effective LLM API provider.
-   **Orchestration:** LangGraph for defining stateful, agentic workflows [[35]](https://www.scalablepath.com/machine-learning/langgraph).
-   **Databases:** PostgreSQL, MongoDB, Redis, Qdrant, and Neo4j. While specialized vector databases like Qdrant can offer lower tail latency, benchmarks on production-scale workloads show that general-purpose databases like PostgreSQL with extensions (e.g., pgvector) can deliver higher throughput at comparable latency, without the added operational complexity of managing a separate system [[36]](https://www.linkedin.com/posts/aman-kohli-9a9b00a7_pgvector-vs-qdrant-do-you-really-need-activity-7419746651747115008-fnT3), [[37]](https://www.tigerdata.com/blog/pgvector-vs-qdrant). Often, it is effective to keep it simple, as you can achieve much with only PostgreSQL or MongoDB.
-   **Observability:** Opik or LangSmith for evaluation and trace monitoring [[5]](https://www.comet.com/site/blog/context-window/).

## Conclusion - Wrap-up: Connecting context engineering to AI engineering

Context engineering is more of an art than a science. It is about developing the intuition to craft effective prompts, select the right information from memory, and arrange context for optimal results. This intuition is often built through iterative refinement, such as tuning context summarization prompts on complex agent traces to find the right balance between detail and brevity [[31]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). This discipline helps you determine the minimal yet essential information an LLM needs to perform at its best.

It's important to understand that context engineering, or AI engineering for that matter, cannot be learned in isolation. It parallels historical knowledge curation practices and intersects with ethical AI, as carefully managed context is key for both business intelligence and bias mitigation [[38]](https://www.ardoq.com/blog/context-engineering-ai), [[39]](https://www.nature.com/articles/s41746-025-01503-7). It is a complex field that combines several disciplines. **AI Engineering** provides the foundation by implementing practical solutions like LLM workflows, RAG, and evaluation pipelines. **Software Engineering** is needed to build scalable and maintainable systems with robust APIs and architectures [[3]](https://sombrainc.com/blog/ai-context-engineering-guide). **Data Engineering** constructs reliable data pipelines to feed curated data into the memory layer [[40]](https://www.decube.io/post/master-data-pipeline-architecture-best-practices-for-engineers). Finally, **Operations (Ops)** ensures that agents are deployed on the proper infrastructure to be reproducible, observable, and scalable, often automating processes with CI/CD pipelines in a practice now known as ContextOps [[41]](https://packmind.com/context-engineering-ai-coding/what-is-contextops/).

Our goal with this course is to teach you how to combine these skills to build production-ready AI products, shifting your mindset from a developer of isolated components to an architect of AI systems.

In the next lesson, we will explore structured outputs. We will also continue to build on the concepts introduced here, such as using actions in Lesson 6, managing memory in Lesson 9, and implementing RAG in Lesson 10.

## References

- [1] Security Industry Association. (2024, July 16). Understanding the Evolution: From Classic Chatbots to RAG Chatbots to AI-Powered Assistants. https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/
- [2] The LangChain Team. (2025, July 2). Context Engineering. https://blog.langchain.com/context-engineering-for-agents/
- [3] Sombra. (n.d.). AI Context Engineering Guide. https://sombrainc.com/blog/ai-context-engineering-guide
- [4] Atlan. (n.d.). LLM Context Window Limitations: Impacts, Risks, & Fixes in 2026. https://atlan.com/know/llm-context-window-limitations/
- [5] Comet. (2025, December 23). Context Window: What It Is and Why It Matters for AI Agents. https://www.comet.com/site/blog/context-window/
- [6] Mei, L., et al. (2025, July 17). A survey of context engineering for large language models. arXiv.org. https://arxiv.org/pdf/2507.13334
- [7] Atlan. (n.d.). Working Memory in LLMs. https://atlan.com/know/working-memory-llms/
- [8] Memgraph. (n.d.). Prompt Engineering vs. Context Engineering. https://memgraph.com/blog/prompt-engineering-vs-context-engineering
- [9] Panjuta, D. (2025). Prompt Engineering vs. Context Engineering. LinkedIn. https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m
- [10] Skymod. (n.d.). Why Memory Matters in LLM Agents: Short-Term vs. Long-Term Memory Architectures. https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/
- [11] DataCamp. (n.d.). How Does LLM Memory Work. https://www.datacamp.com/blog/how-does-llm-memory-work
- [12] Label Studio. (n.d.). Episodic vs. Persistent Memory in LLMs. https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/
- [13] Analytics Vidhya. (2026, January). How Does LLM Memory Work. https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/
- [14] Adaline.ai. (2026). Top Agentic LLM Models & Frameworks for 2026. https://www.adaline.ai/blog/top-agentic-llm-models-frameworks-for-2026
- [15] Reinteractive. (n.d.). Solving AI Agent Amnesia: Context Rot and Lost in the Middle. https://reinteractive.com/articles/ai-real-world-use-cases/solving-ai-agent-amnesia-context-rot-and-lost-in-the-middle
- [16] Cursor. (n.d.). Context Engineering. https://cursor.directory/plugins/context-engineering
- [17] DeJohn, A. (n.d.). Lost in the Middle: A Lesson in Failing AI Agents Backwards. LinkedIn. https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e
- [18] Thousand Miles AI. (n.d.). The 'Lost in the Middle' Problem: Why LLMs Ignore the Middle of Your Context Window. https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [19] Agent Drift in Continuous Deployments of Large Language Model-based Agents. (2026, January 4). arXiv.org. https://arxiv.org/html/2601.04170v1
- [20] Galileo. (n.d.). Production LLM Monitoring Strategies. https://galileo.ai/blog/production-llm-monitoring-strategies
- [21] The New Stack. (n.d.). Context Rot in Enterprise AI with LLMs. https://thenewstack.io/context-rot-enterprise-ai-llms/
- [22] PagerGPT. (n.d.). Evolution of AI Chatbots. https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots
- [23] Teki, S. (n.d.). Context Engineering: A Framework for Robust Generative AI Systems. https://www.sundeepteki.org/blog/context-engineering-a-framework-for-robust-generative-ai-systems
- [24] Daily Dose of DS. (n.d.). LLMOps Crash Course Part 8. https://www.dailydoseofds.com/llmops-crash-course-part-8/
- [25] Promptmetheus. (n.d.). Lost-in-the-Middle Effect. https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect
- [26] JetBrains Research. (2025, December). Efficient Context Management. https://blog.jetbrains.com/research/2025/12/efficient-context-management/
- [27] OneUptime. (2026, January 30). How to Build Context Compression. https://oneuptime.com/blog/post/2026-01-30-context-compression/view
- [28] Vellum.ai. (n.d.). Multi-Agent Systems: Building with Context Engineering. https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering
- [29] Beam.ai. (n.d.). Multi-Agent Orchestration Patterns in Production. https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- [30] GuruSup. (n.d.). Multi-Agent Orchestration Guide. https://gurusup.com/blog/multi-agent-orchestration-guide
- [31] Anthropic. (n.d.). Effective Context Engineering for AI Agents. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [32] Maxim.ai. (n.d.). Context Window Management Strategies for Long-Context AI Agents and Chatbots. https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/
- [33] Comet. (n.d.). LLM Evaluation Frameworks. https://www.comet.com/site/blog/llm-evaluation-frameworks/
- [34] Iusztin, P. (2025). Context Engineering: 2025’s #1 Skill in AI. Decoding AI. https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [35] Scalable Path. (n.d.). LangGraph. https://www.scalablepath.com/machine-learning/langgraph
- [36] Kohli, A. (2025). pgvector vs Qdrant. LinkedIn. https://www.linkedin.com/posts/aman-kohli-9a9b00a7_pgvector-vs-qdrant-do-you-really-need-activity-7419746651747115008-fnT3
- [37] Tiger Analytics. (n.d.). pgvector vs Qdrant. https://www.tigerdata.com/blog/pgvector-vs-qdrant
- [38] Ardoq. (n.d.). Context Engineering & AI. https://www.ardoq.com/blog/context-engineering-ai
- [39] McCradden, M. D., et al. (2025). A framework for the lifecycle of bias in healthcare artificial intelligence. npj Digital Medicine. https://www.nature.com/articles/s41746-025-01503-7
- [40] Decube. (n.d.). Master Data Pipeline Architecture: Best Practices for Engineers. https://www.decube.io/post/master-data-pipeline-architecture-best-practices-for-engineers
- [41] Packmind. (2026, April 3). Why AI coding assistants fail without context : an introduction to ContextOps. https://packmind.com/context-engineering-ai-coding/what-is-contextops/
- [42] Mezmo. (n.d.). Context Engineering for Observability: How to Deliver the Right Data to LLMs. https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms
- [43] DataCamp. (n.d.). Context Engineering: A Guide With Examples. https://www.datacamp.com/blog/context-engineering
- [44] nlp.elvissaravia.com. (n.d.). Context Engineering Guide. https://nlp.elvissaravia.com/p/context-engineering-guide
- [45] Pinecone. (n.d.). What is Context Engineering?. https://www.pinecone.io/learn/context-engineering/
- [46] karpathy, A. (n.d.). X. https://x.com/karpathy/status/1937902205765607626
- [47] lenadroid. (n.d.). X. https://x.com/lenadroid/status/1943685060785524824
- [48] Horthy, D. (n.d.). Own your context window. GitHub. https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
- [49] Chase, H. (2025, June 23). The rise of "context engineering". LangChain Blog. https://blog.langchain.com/the-rise-of-context-engineering/
- [50] Hong, K., Troynikov, A., & Huber, J. (2025, July). Context Rot: How Increasing Input Tokens Impacts LLM Performance. Chroma. https://www.trychroma.com/research/context-rot

</article>