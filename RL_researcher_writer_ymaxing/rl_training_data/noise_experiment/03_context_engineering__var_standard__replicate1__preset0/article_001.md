# Context Engineering

## When prompt engineering breaks

AI applications have evolved rapidly. In 2022, we had simple chatbots for question-and-answer interfaces [[25]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/). By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge [[25]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/). 2024 brought us tool-using agents that could perform actions, moving from simply responding to actively accomplishing tasks [[26]](https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots). Now, we are building memory-enabled agents that remember past interactions and build relationships over time, with multiple agents collaborating to solve complex problems [[28]](https://www.linkedin.com/posts/ai-apps-central_most-people-put-all-ai-systems-in-the-same-activity-7438555783077793792-UEUm).

In our last lesson, we explored how to choose between AI agents and LLM workflows when designing a system. As these applications grow more complex, prompt engineering, a practice that once served us well, is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The sheer volume of information an agent might need—past conversations, user data, documents, and action descriptions—has grown exponentially. Simply stuffing all this into a prompt is not a viable strategy. Context engineering is the discipline of orchestrating this entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it. This skill is becoming a core foundation for AI engineering.

## From prompt to context engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event. This approach breaks down in stateful applications where context must be preserved and managed across multiple turns.

As a conversation or task progresses, the context grows. Without a strategy to manage this growth, the LLM’s performance degrades. This is context decay: the model gets confused by the noise of an ever-expanding history. It starts to lose track of the original instructions or key information [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

Even with large context windows, a physical limit exists for what you can include. Also, on the operational side, every token adds to the cost and latency of an LLM call. Simply putting everything into the context creates a slow, expensive, and underperforming system. We will explore these concepts in more detail in upcoming lessons, including memory in Lesson 9 and RAG in Lesson 10.

On a recent project, we learned this the hard way. We were working with a model that supported a million-token context window, so we thought, "*What could go wrong*?" We stuffed everything in: our research, guidelines, examples, and user history. The result was an LLM workflow that took 30 minutes to run and produced low-quality outputs [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

To solve these problems, we use context engineering. It shifts the focus from crafting static prompts to building dynamic systems that manage information flow. As an AI engineer, your job is to select only the most critical pieces of context for each LLM call. This makes your applications accurate, fast, and cost-effective [[19]](https://blog.langchain.com/the-rise-of-context-engineering/).

## Understanding context engineering

Context engineering is about finding the best way to arrange parts of your application's memory into the context that's passed to an LLM to get the best results. It is a solution to an optimization problem where you retrieve the right parts from your short-term and long-term memory to solve a specific task without overwhelming the model [[2]](https://arxiv.org/pdf/2507.13334). For example, when you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies or taste preferences. This precise selection ensures the model receives only the essential information.

Andrej Karpathy explains that LLMs are like a new kind of operating system where the model is the CPU and its context window is the RAM [[3]](https://x.com/karpathy/status/1937902205765607626), [[29]](https://www.langchain.com/blog/context-engineering-for-agents). Just as an operating system manages what fits into your computer’s limited RAM, context engineering manages what information occupies the model’s limited context window. This analogy extends further: external sources like vector stores or documents are like disk storage—vast and passive, requiring an explicit loading process to influence the CPU's reasoning [[31]](https://atlan.com/know/working-memory-llms/).

How does context engineering relate to prompt engineering? It's simple. Prompt engineering is a subset of context engineering. You still write effective prompts, but you also design a system that feeds the right context into those prompts. This means understanding not just *how* to phrase a task, but *what* information the model needs to perform optimally [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

| Dimension | Prompt Engineering | Context Engineering |
|-----------|-------------------|---------------------|
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Stateless function | Stateful due to memory |
| Focus | How to phrase tasks | What information to provide |
Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible. Data changes constantly, making fine-tuning a last resort. For most enterprise use cases, you get better results faster and more cheaply with context engineering [[45]](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m). It allows for rapid iteration and adaptation to evolving data without altering the core model, a key advantage in dynamic environments. This approach avoids the computational resources and specialized expertise required for retraining, offering a more agile path to reliable AI applications.

When you start a new AI project, your decision-making process for guiding the LLM should look like this:

```mermaid
graph TD
    A["Prompt Engineering"]
    B{"Prompt Engineering<br/>solves problem?"}
    C["Context Engineering"]
    D{"Context Engineering<br/>solves problem?"}
    E["Fine-tuning"]
    F{"Can fine-tuning dataset<br/>be made?"}
    G["Reframe the problem"]
    H["End"]

    A --> B
    B -- "Yes" --> H
    B -- "No" --> C
    C --> D
    D -- "Yes" --> H
    D -- "No" --> E
    E --> F
    F -- "Yes" --> H
    F -- "No" --> G
    G --> H
```
Image 1: A flowchart illustrating the decision-making process for choosing between Prompt Engineering, Context Engineering, and Fine-tuning.

For instance, if you build an agent to process internal Slack messages, you do not need to fine-tune a model on your company’s communication style. It is more effective to use a powerful reasoning model and engineer the context to retrieve specific messages and enable actions like creating tasks or drafting emails. Throughout this course, we will show you how to solve most industry problems using only context engineering.

## What makes up the context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model.

The high-level workflow begins when a user input triggers the system to pull relevant information from both long-term and short-term memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
flowchart LR
  %% Input and Memory
  subgraph "Input & Memory"
    UI["User Input"]
    LTM["Long-term Memory<br/>(procedural, episodic, semantic)"]
    STM["Short-Term Working Memory<br/>(user input, message history, agent's internal thoughts, tool calls and outputs)"]
  end

  %% Context Assembly
  subgraph "Context Assembly"
    C["Context"]
    PT["Prompt Template"]
    P["Prompt"]
  end

  %% LLM Execution
  subgraph "LLM Execution"
    LLMC["LLM Call"]
    A["Answer"]
  end

  %% Primary Data Flow
  UI -- "provides" --> C
  LTM -- "contributes to" --> C
  STM -- "contributes to" --> C

  C -- "assembled into" --> PT
  PT -- "generates" --> P
  P -- "sent to" --> LLMC
  LLMC -- "produces" --> A

  %% Feedback Loop
  A -- "updates" --> STM
  A -- "updates" --> LTM

  STM -. "feeds into next cycle" .-> C
  LTM -. "feeds into next cycle" .-> C

  %% Visual Grouping
  classDef memory stroke-dasharray:3,3
  classDef process stroke-width:2px
  class LTM,STM memory
  class C,PT,P,LLMC,A process
```
Image 2: A flowchart illustrating the high-level workflow of how context is assembled and used in an LLM call.

These components are grouped into two main categories. We will explain them intuitively for now, as we have future dedicated lessons for all of them.

### Short-Term Working Memory

Short-term working memory is the state of the agent for the current task or conversation. It is volatile and changes with each interaction, helping the agent maintain a coherent dialogue and make immediate decisions. It can include some or all of these components [[36]](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/):

-   **User input:** The most recent query or command from the user.
-   **Message history:** The log of the current conversation, allowing the LLM to understand the flow and previous turns.
-   **Agent's internal thoughts:** The reasoning steps the agent takes to decide on its next action.
-   **Action calls and outputs:** The results from any actions the agent has performed, providing information from external systems.

### Long-Term Memory

Long-term memory is more persistent and stores information across sessions, allowing the AI system to remember things beyond a single conversation. We divide it into three types, drawing parallels from human memory [[34]](https://www.datacamp.com/blog/how-does-llm-memory-work). An AI system can include some or all of them:

-   **Procedural memory:** This is knowledge encoded directly in the code. It includes the system prompt, which sets the agent's overall behavior. It also includes the definitions of available actions, which tell the agent what it can do, and schemas for structured outputs, which guide the format of its responses. Procedural memory represents the agent's built-in skills [[35]](https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/).
-   **Episodic memory:** This is memory of specific past experiences, like user preferences or previous interactions. It's used to help the agent personalize its responses based on individual users. We typically store this in vector or graph databases for efficient retrieval [[37]](https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/).
-   **Semantic memory:** This is the agent’s general knowledge base. It can be internal, like company documents stored in a data lake, or external, accessed via the internet through API calls or web scraping. This memory provides the factual information the agent needs to answer questions [[33]](https://atlan.com/know/working-memory-llms/).

If this seems like a lot, bear with us. We will cover all these concepts in-depth in future lessons, including structured outputs (Lesson 4), actions (Lesson 6), memory (Lesson 9), RAG (Lesson 10), and working with multimodal data (Lesson 11).
Image 3: A detailed illustration of how all the context engineering components work together inside an AI agent (Source: [DECODING ML](https://www.decodingai.com/))

The key takeaway is that these components are not static. They are dynamically re-computed for every single interaction. For each conversation turn or new task, the short-term memory grows, or the long-term memory can change. Context engineering involves knowing how to select the right pieces from this vast memory pool to construct the most effective prompt for the task at hand.

## Production Implementation Challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These challenges all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that come up when building AI applications:

1.  **The context window challenge:** Every AI model has a limited context window, the maximum amount of information (tokens) it can process at once. The context window is the model's working memory, similar to a computer's RAM. If your machine has only 32GB of RAM, that is all it can use at one time. While context windows are getting larger, they are not infinite, and treating them as such leads to other problems [[14]](https://www.comet.com/site/blog/context-window/).
2.  **Information overload:** Just because you can fit a lot of information into the context does not mean you should. Too much context reduces the performance of the LLM by confusing it. This is known as the *"lost-in-the-middle"* or *"needle in the haystack"* problem, where LLMs are known for remembering information best at the beginning and end of the context window. Information in the middle is often overlooked, and performance can drop long before the physical context limit is reached [[49]](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e), [[51]](https://atlan.com/know/llm-context-window-limitations/).
3.  **Context drift:** This occurs when conflicting views of truth accumulate in the memory over time. For example, the memory might contain two conflicting statements: "*My cat is white*" and "*My cat is black*." This is not Schrodinger's Cat quantum physics experiment; it is a data conflict that confuses the LLM. Without a mechanism to resolve these conflicts, the model's responses become unreliable [[6]](https://galileo.ai/blog/production-llm-monitoring-strategies), [[8]](https://thenewstack.io/context-rot-enterprise-ai-llms/).
4.  **Tool confusion:** The final challenge is tool confusion, which arises in two main ways. First, adding too many actions to an agent can confuse the LLM about the best one for the job. The Gorilla benchmark shows nearly all models perform worse when given more than one tool [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). Second, confusion can occur when tool descriptions are poorly written or overlap. If the distinctions between actions are unclear, even a human would struggle to choose the right one.

## Key Strategies for Context Optimization

Initially, most AI applications were chatbots over single knowledge bases. Today, modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements.

Here are four popular context engineering strategies used across the industry:

### Selecting the Right Context

Retrieving the right information from memory is a critical first step. A common mistake is to provide everything at once, assuming that models with large context windows can handle it. As we've discussed, the "lost-in-the-middle" problem often leads to poor performance, increased latency, and higher costs.

To solve this, consider these approaches:

-   **Use structured outputs:** Define clear schemas for what the LLM should return. This allows you to pass only the necessary, structured information to downstream steps. We will cover this in detail in Lesson 4.
-   **Use RAG:** Instead of providing entire documents, use RAG to fetch only the specific chunks of text needed to answer a user's question. This is a core topic we will explore in Lesson 10.
-   **Reduce the number of available actions:** Rather than giving an agent access to every available action, use various strategies to delegate action subsets to specialized components. For example, a typical pattern is to use the orchestrator-worker pattern to delegate subtasks to specialized agents. Studies have shown that applying RAG to tool descriptions can triple the agent's selection accuracy [[20]](https://www.datacamp.com/blog/context-engineering).
-   **Rank time-sensitive data:** For time-sensitive information, rank it by date and filter out anything no longer relevant [[11]](https://www.dailydoseofds.com/llmops-crash-course-part-8/).
-   **Repeat core instructions:** For the most important instructions, repeat them at both the start and the end of the prompt. This uses the model's tendency to pay more attention to the context edges, ensuring core instructions are not lost.

```mermaid
flowchart LR
  %% Core System Components
  A["User Query"]
  B["LLM"]
  C["Final Output"]

  %% Context Optimization Techniques
  D["RAG<br/>(Factual Info Retrieval)"]
  E["Temporal Relevance<br/>(Data Filtering & Ranking)"]
  F["Reduced Tools<br/>(LLM Action Scope)"]
  G["Repeating Instructions<br/>(Prompt Reinforcement)"]
  H["Structured Outputs<br/>(Output Parsing & Filtering)"]

  %% Intermediate Context
  I["Optimized Context"]
  J["Raw LLM Output"]

  %% Flow
  A -- "initiates" --> D
  A -- "informs" --> E

  D -- "provides" --> I
  E -- "refines" --> I

  G -- "embeds in" --> I

  I -- "feeds into" --> B
  B -- "generates" --> J
  J -- "processes via" --> H
  H -- "produces" --> C

  %% Indirect relationships
  F -- "configures" --> B
  B -. "guided by" .-> F

  %% Visual grouping
  classDef technique fill:#e0f2f7,stroke:#00bcd4,stroke-width:2px
  classDef core fill:#fff9c4,stroke:#ffeb3b,stroke-width:2px
  class D,E,F,G,H technique
  class A,B,C,I,J core
```
Image 4: A diagram illustrating how various context optimization techniques work together to create an optimized context for an LLM.

### Context Compression

As message history grows in short-term working memory, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns, as the LLM still needs to remember what happened. Instead, you need ways to compress key facts from the past.

You can do this through:

1.  **Creating summaries of past interactions:** Use an LLM to replace a long, detailed history with a concise overview [[13]](https://blog.jetbrains.com/research/2025/12/efficient-context-management/).
2.  **Moving user preferences to long-term memory:** Transfer user preferences from working memory to long-term episodic memory. This keeps the working context clean while ensuring preferences are remembered for future sessions.
3.  **Deduplication:** Remove redundant information from the context to avoid repetition using techniques like MinHash [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill) or semantic clustering [[10]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view).

```mermaid
flowchart LR
  A["Message History Grows"]
  A -- "necessitates" --> B["Context Compression"]

  subgraph "Context Compression Strategies"
    C["Creating Summaries of Past Interactions<br/>using an LLM"]
    D["Moving Preferences about the User<br/>from Working Memory<br/>into Episodic Memory (Long-Term Memory)"]
    E["Deduplication to avoid repetition"]
  end

  B -- "employs" --> C
  B -- "employs" --> D
  B -- "employs" --> E

  subgraph "Goals"
    F["Shrink Short-Term Memory"]
    G["Keep Context Window in Check"]
  end

  C -- "achieves" --> F
  D -- "achieves" --> F
  E -- "achieves" --> F

  C -- "achieves" --> G
  D -- "achieves" --> G
  E -- "achieves" --> G
```
Image 5: A flowchart illustrating context compression strategies for managing message history in short-term working memory.

### Isolating Context

Another powerful strategy is to isolate context by splitting information across multiple agents or LLM workflows. This technique is similar to tool isolation but is more general, referring to the whole context. The key idea is that instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context [[42]](https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering).

We often implement this using an orchestrator-worker pattern, where a central orchestrator agent breaks down a problem and assigns sub-tasks to specialized worker agents. Each worker operates in its own isolated context, improving focus and allowing for parallel processing. We will cover this pattern in more detail in Lesson 5 [[40]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production).

```mermaid
flowchart LR
  %% Central Orchestrator
  subgraph "Orchestration Layer"
    Orchestrator["Orchestrator"]
  end

  %% Worker Agents with Isolated Contexts
  subgraph "Worker Agents"
    subgraph "Worker Agent 1"
      Worker1["Worker Agent 1"]
      Context1["Own Focused Context Window"]
    end
    subgraph "Worker Agent 2"
      Worker2["Worker Agent 2"]
      Context2["Own Focused Context Window"]
    end
  end

  %% Flow of tasks and results
  Orchestrator -- "Distributes Task" --> Worker1
  Orchestrator -- "Distributes Task" --> Worker2

  Worker1 -- "Operates within" --> Context1
  Worker2 -- "Operates within" --> Context2

  Worker1 -- "Sends Result" --> Orchestrator
  Worker2 -- "Sends Result" --> Orchestrator
```
Image 6: Architecture diagram showing the orchestrator-worker pattern for context isolation.

### Format Optimizations

Finally, the way you format the context matters. Models are sensitive to structure, and using clear delimiters can improve performance. Common strategies are to:

-   **Use XML tags:** Wrap different pieces of context in XML-like tags (e.g., `<user_query>`, `<documents>`). This helps the model distinguish between different types of information, while making it easier for the engineer to reference context elements within the system prompt [[39]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
-   **Prefer YAML over JSON:** When providing structured data as input, YAML is often more token-efficient than JSON, which helps save space in your context window [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

To conclude, you always have to understand what is passed to the LLM. Seeing exactly what occupies your context window at every step is key to mastering context engineering. Usually, this is done by properly monitoring your traces, tracking what happens at each step, and understanding what the inputs and outputs are. As this is a significant step to go from PoC to production, we will have dedicated lessons on this [[17]](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/).

## Here is an Example

Let's connect the theory and strategies discussed earlier with concrete examples. Consider several common real-world scenarios:

-   **Healthcare:** An AI assistant accesses a patient's medical history, current symptoms, and the latest medical literature to provide personalized diagnostic support [[38]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
-   **Financial Services:** AI systems integrate with enterprise tools like Customer Relationship Management (CRM) systems, emails, and calendars, combining real-time market data and client portfolio information to generate tailored financial advice and reports.
-   **Project Management:** AI systems access enterprise infrastructure like CRMs, Slack, and task managers to automatically understand project requirements, then add and update project tasks.
-   **Content Creator Assistant:** An AI agent uses your research, past content, and personality traits to understand what and how to create a given piece of content.

Let's walk through a specific query to see context engineering in action with the healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the AI attempts to answer, a context engineering system performs several steps:

1.  It retrieves the user's patient history, known allergies, and lifestyle habits from episodic memory. This step is crucial for personalization and safety [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
2.  It queries a medical database for non-pharmacological headache remedies from semantic memory. This ensures the advice is grounded in up-to-date, reliable information.
3.  It uses various tools to assemble the key units of information from both memory types into the final context. This assembly process is where much of the "engineering" happens, filtering and prioritizing what the model sees.
4.  It formats this information into a structured prompt and calls the LLM. The structure helps the model differentiate between patient data, medical facts, and the user's direct query.
5.  Finally, it presents a personalized, context-aware answer to the user, and may log the interaction to refine future responses.

Here is a simplified Python example showing how you might structure the context and prompt for the LLM, using XML tags to format the different context elements. Notice the clear structure and ordering [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

```
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
-   **Orchestration:** LangGraph for defining stateful, agentic workflows. Its graph-based structure is ideal for managing the complex, cyclical flow of context in agentic systems [[56]](https://www.scalablepath.com/machine-learning/langgraph).
-   **Databases:** PostgreSQL, MongoDB, Redis, Qdrant, and Neo4j. Often, it is effective to keep it simple, as you can achieve much with only PostgreSQL or MongoDB.
-   **Observability:** Opik or LangSmith for evaluation and trace monitoring. These tools are essential for debugging context-related issues by providing visibility into what information is in the context window at each step [[55]](https://atlan.com/know/context-engineering-platforms-comparison/).

## Connecting Context Engineering to AI Engineering

Context engineering is more of an art than a science. It is about developing the intuition to craft effective prompts, select the right information from memory, and arrange context for optimal results. This discipline helps you determine the minimal yet essential information an LLM needs to perform at its best.

It's important to understand that context engineering, or AI engineering for that matter, cannot be learned in isolation. It is a complex field that combines:

1.  **AI Engineering:** Implement practical solutions such as LLM workflows, RAG, AI Agents, and evaluation pipelines.
2.  **Software Engineering (SWE):** Build your AI product with code that is not just functional, but also scalable and maintainable. This involves designing architectures that can grow with your product's needs, such as creating robust APIs to wrap agents [[22]](https://sombrainc.com/blog/ai-context-engineering-guide).
3.  **Data Engineering:** Design reliable data pipelines that feed curated and validated data into the memory layer. This ensures the information your agent uses is accurate and up-to-date [[21]](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms).
4.  **Operations (Ops):** Deploy agents on the proper infrastructure to ensure they are reproducible, maintainable, observable, and scalable. This includes automating processes with Continuous Integration/Continuous Deployment (CI/CD) pipelines to make systems reproducible and observable [[4]](https://packmind.com/context-engineering-ai-coding/what-is-contextops/).

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. In the world of AI, we should all think in systems rather than isolated components, having a mindset shift from developers to architects.

In the next lesson, we will explore structured outputs. We will also revisit memory, RAG, and tools in more detail in future lessons.

## References

- [1] https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [2] https://arxiv.org/pdf/2507.13334
- [3] https://x.com/karpathy/status/1937902205765607626
- [4] https://packmind.com/context-engineering-ai-coding/what-is-contextops/
- [5] https://www.ibm.com/think/topics/ai-agent-memory
- [6] https://galileo.ai/blog/production-llm-monitoring-strategies
- [7] https://arxiv.org/pdf/2505.00019
- [8] https://thenewstack.io/context-rot-enterprise-ai-llms/
- [9] https://aclanthology.org/2025.naacl-srw.42.pdf
- [10] https://oneuptime.com/blog/post/2026-01-30-context-compression/view
- [11] https://www.dailydoseofds.com/llmops-crash-course-part-8/
- [12] https://arxiv.org/html/2510.22101v1
- [13] https://blog.jetbrains.com/research/2025/12/efficient-context-management/
- [14] https://www.comet.com/site/blog/context-window/
- [15] https://datahub.com/blog/context-window-optimization/
- [16] https://www.linkedin.com/posts/aditya-santhanam_your-llm-hits-the-token-limit-conversation-activity-7425863566190260224-Pz6v
- [17] https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/
- [18] https://www.nature.com/articles/s41593-023-01496-2
- [19] https://blog.langchain.com/the-rise-of-context-engineering/
- [20] https://www.datacamp.com/blog/context-engineering
- [21] https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms
- [22] https://sombrainc.com/blog/ai-context-engineering-guide
- [23] https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models
- [24] https://www.datacamp.com/tutorial/prompt-compression
- [25] https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/
- [26] https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots
- [27] https://www.dante-ai.com/news/when-did-ai-chatbots-start
- [28] https://www.linkedin.com/posts/ai-apps-central_most-people-put-all-ai-systems-in-the-same-activity-7438555783077793792-UEUm
- [29] https://www.langchain.com/blog/context-engineering-for-agents
- [30] https://www.glean.com/perspectives/context-engineering-vs-prompt-engineering-key-differences-explained
- [31] https://atlan.com/know/working-memory-llms/
- [32] https://www.sundeepteki.org/blog/from-vibe-coding-to-context-engineering-a-blueprint-for-production-grade-genai-systems
- [33] https://www.linkedin.com/pulse/context-engineering-silent-architecture-behind-every-ai-roychowdhury-lzcec
- [34] https://www.datacamp.com/blog/how-does-llm-memory-work
- [35] https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/
- [36] https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/
- [37] https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/
- [38] https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [39] https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [40] https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- [41] https://gurusup.com/blog/multi-agent-orchestration-guide
- [42] https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering
- [43] https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/
- [44] https://arxiv.org/html/2601.13671v1
- [45] https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m
- [46] https://memgraph.com/blog/prompt-engineering-vs-context-engineering
- [47] https://www.instinctools.com/blog/context-engineering/
- [48] https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/
- [49] https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e
- [50] https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [51] https://atlan.com/know/llm-context-window-limitations/
- [52] https://bigdataboutique.com/blog/needle-in-haystack-optimizing-retrieval-and-rag-over-long-context-windows-5dfb3c
- [53] https://www.codecademy.com/article/context-engineering-in-ai
- [54] https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b
- [55] https://atlan.com/know/context-engineering-platforms-comparison/
- [56] https://www.scalablepath.com/machine-learning/langgraph
- [57] https://www.mdpi.com/2079-9292/13/15/2961