# Context Engineering: 2025’s #1 Skill in AI

AI applications have evolved rapidly. In 2022, we had simple chatbots for question-answering. By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge. 2024 brought us tool-using agents that could perform actions. Now, we are building memory-enabled agents that remember past interactions and build relationships over time.

In our last lesson, we explored how to choose between AI agents and LLM workflows when designing a system. As these applications grow more complex, prompt engineering, a practice that once served us well, is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The sheer volume of information an agent might need—past conversations, user data, documents, and action descriptions—has grown exponentially. Simply stuffing all this into a prompt is not a viable strategy.

This is where context engineering comes in. It is the discipline of orchestrating this entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it. This skill is becoming a core foundation for AI engineering.

## From prompt to context engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event. This approach breaks down in stateful applications where context must be preserved and managed across multiple turns.

As a conversation or task progresses, the context grows. Without a strategy to manage this growth, the LLM’s performance degrades. This is context decay: the model gets confused by the noise of an ever-expanding history. It starts to lose track of the original instructions or key information.

Even with large context windows, a physical limit exists for what you can include. Also, on the operational side, every token adds to the cost and latency of an LLM call. Simply putting everything into the context creates a slow, expensive, and underperforming system. We will explore these concepts in more detail in upcoming lessons, including memory in Lesson 9 and RAG in Lesson 10.

On a recent project, we learned this the hard way. We were working with a model that supported a two-million-token context window, so we thought, "*What could go wrong?*" We stuffed everything in: our research, guidelines, examples, and reviews. The result was an LLM workflow that took 30 minutes to run and produced low-quality outputs.

This is where context engineering becomes essential. It shifts the focus from crafting static prompts to building dynamic systems that manage information flow. As an AI engineer, your job is to select only the most critical pieces of context for each LLM call. This makes your applications accurate, fast, and cost-effective.

## Understanding context engineering

Context engineering is about finding the best way to arrange parts of your memory into the context that's passed to the LLM to squeeze out the best results. It's a solution to an optimization problem in which you have to retrieve the right parts of both your short-term and long-term memory to solve a specific task without overwhelming the LLM [[2]](https://arxiv.org/pdf/2507.13334). This can be framed as an optimization problem: finding the ideal context C, assembled from various information components, that maximizes the model's ability to produce the correct output [[66]](https://arxiv.org/html/2507.13334v1). For example, when you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies or taste preferences. This precise selection ensures the model receives only the essential information.

Andrej Karpathy offered a great analogy for this: LLMs are like a new kind of operating system, where the model acts as the CPU and its context window functions as the RAM [[3]](https://x.com/karpathy/status/1937902205765607626). Just as an operating system manages what fits into RAM, context engineering curates what occupies the model’s working memory.

Another way to think about this is through narrative construction. Context engineering provides the necessary background for an AI agent to create a coherent interaction, much like a storyteller provides context for a character's actions [[67]](https://www.contentstack.com/blog/ai/context-engineering-in-the-ai-era).

How does context engineering relate to prompt engineering? It's simple. Prompt engineering is a subset of context engineering. You still write effective prompts, but you also design a system that feeds the right context into those prompts [[20]](https://blog.langchain.com/the-rise-of-context-engineering/). This means understanding not just *how* to phrase a task, but *what* information the model needs to perform optimally.

Table 1: A comparison of prompt engineering and context engineering.
| Dimension | Prompt Engineering | Context Engineering |
| --- | --- | --- |
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Stateless function | Stateful due to memory |
| Focus | How to phrase tasks | What information to provide |

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible. Data changes constantly, making fine-tuning a last resort. For most enterprise use cases, you get better results faster and more cheaply with context engineering. It allows for rapid iteration and adaptation to evolving data without altering the core model, a key advantage in dynamic environments. The evidence for this shift is compelling. For rapidly changing data, context engineering is far more flexible. It is also cheaper and faster; a context-engineered MVP can cost less than $1,000, while a full fine-tuning project can exceed $50,000 [[68]](https://blog.agami.ai/context-engineering-vs-fine-tuning-vs-distillation-how-to-decide/). Recent studies also show that context-based approaches can achieve better generalization and even outperform fine-tuning on complex reasoning tasks without any costly model retraining [[69]](https://venturebeat.com/ai/fine-tuning-vs-in-context-learning-new-research-guides-better-llm-customization-for-real-world-tasks), [[70]](https://www.ikangai.com/the-end-of-fine-tuning-stanfords-ace-framework-turns-context-into-intelligence/).

When you start a new AI project, your decision-making process for guiding the LLM should look like the one presented in Image 1.

```mermaid
graph TD
    A["Prompt Engineering"] --> B{"Does it solve the problem?"}
    B -->|"Yes"| C["Stop"]
    B -->|"No"| D["Context Engineering"]
    D --> E{"Does it solve the problem?"}
    E -->|"Yes"| F["Stop"]
    E -->|"No"| G["Fine-tuning"]
    G --> H{"Can you make a fine-tuning dataset?"}
    H -->|"Yes"| I["Stop"]
    H -->|"No"| J["Reframe the problem"]
```
Image 1: A flowchart illustrating the decision-making process for choosing between Prompt Engineering, Context Engineering, and Fine-tuning when building a new AI application.

For instance, if you build an agent to process internal Slack messages, you do not need to fine-tune a model on your company’s communication style. It is more effective to use a powerful reasoning model and engineer the context to retrieve specific messages and enable actions like creating tasks or drafting emails. Throughout this course, we will show you how to solve most industry problems using only context engineering.

## What makes up the context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model.

The high-level workflow, as presented in Image 2, begins when a user input triggers the system to pull relevant information from both long-term and short-term memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
flowchart LR
  %% User Interaction
  subgraph "User Interaction"
    UI["User Input"]
    A["Answer"]
  end

  %% Memory Systems
  subgraph "Memory Systems"
    LTM["Long-term Memory"]
    STWM["Short-Term Working Memory"]
  end

  %% Context Assembly & Prompting
  subgraph "Context Assembly & Prompting"
    C["Context<br/>(Re-computed per turn)"]
    PT["Prompt Template"]
    P["Prompt"]
  end

  %% LLM Execution
  subgraph "LLM Execution"
    LLMC["LLM Call"]
  end

  %% Primary Flow - Initial Turn
  UI -- "initiates" --> LTM
  LTM -- "retrieves relevant info" --> STWM
  STWM -- "assembles current state" --> C
  C -- "populates" --> PT
  PT -- "generates" --> P
  P -- "sends to" --> LLMC
  LLMC -- "produces" --> A

  %% Feedback Loop & Dynamic Context Re-computation
  A -- "stores output" --> STWM
  STWM -- "persists updates" --> LTM

  %% Emphasize re-computation for next turn
  LTM -. "informs next turn's context" .-> C
  STWM -. "contributes to next turn's context" .-> C

  %% Visual Grouping
  classDef memory_store stroke-dasharray:3,3
  class LTM,STWM memory_store
```
Image 2: A flowchart illustrating the high-level workflow of how context is assembled and used in an LLM call, highlighting the dynamic nature of context re-computation on each turn.

These components are grouped into two main categories. We will explain them intuitively for now, as we have future dedicated lessons for all of them.

### Short-Term Working Memory

Short-term working memory is the state of the agent for the current task or conversation. It is volatile and changes with each interaction, helping the agent maintain a coherent dialogue and make immediate decisions. It can include some or all of these components:

*   **User input:** The most recent query or command from the user.
*   **Message history:** The log of the current conversation, allowing the LLM to understand the flow and previous turns.
*   **Agent's internal thoughts:** The reasoning steps the agent takes to decide on its next action.
*   **Action calls and outputs:** The results from any actions the agent has performed, providing information from external systems.

### Long-Term Memory

Long-term memory is more persistent and stores information across sessions, allowing the AI system to remember things beyond a single conversation. We divide it into three types, drawing parallels from human memory [[4]](https://www.nature.com/articles/s41593-023-01496-2). An AI system can include some or all of them:

*   **Procedural memory:** This is knowledge encoded directly in the code. It includes the system prompt, which sets the agent's overall behavior. It also includes the definitions of available actions, which tell the agent what it can do, and schemas for structured outputs, which guide the format of its responses. Think of this as the agent's built-in skills.
*   **Episodic memory:** This is memory of specific past experiences, like user preferences or previous interactions. It's used to help the agent personalize its responses based on individual users. We typically store this in vector or graph databases for efficient retrieval [[5]](https://www.ibm.com/think/topics/ai-agent-memory).
*   **Semantic memory:** This is the agent’s general knowledge base. It can be internal, like company documents stored in a data lake, or external, accessed via the internet through API calls. This memory provides the factual information the agent needs to answer questions.

However, the worst memory system is one that stores everything. Effective systems are selective, using techniques like LLM-based reflection to assign an "importance score" to memories before storing them. They also require regular maintenance, such as pruning outdated facts or replacing long transcripts with summaries, to prevent historical clutter from polluting the context [[71]](https://weaviate.io/blog/context-engineering).

If this seems like a lot, bear with us. We will cover all these concepts in-depth in future lessons, including structured outputs (Lesson 4), actions (Lesson 6), memory (Lesson 9), RAG (Lesson 10), and working with multimodal data in Lesson 11.![An illustration showing how various components like user input, memory, and tools are assembled into a context for an AI agent.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39dce26a-e51e-4167-ac9e-ca28c45b53a6_1115x708.png)
Image 3: A detailed illustration of how all the context engineering components work together inside an AI agent (Source: [decodingai.com](https://www.decodingai.com/p/context-engineering-2025s-1-skill) [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill))

The key takeaway is that these components are not static. They are dynamically re-computed for every single interaction. For each conversation turn or new task, the short-term memory grows, or the long-term memory can change. Context engineering involves knowing how to select the right pieces from this vast memory pool to construct the most effective prompt for the task at hand.

## Production implementation challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These challenges all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that come up when building AI applications:

1.  **The context window challenge:** Every AI model has a limited context window, the maximum amount of information (tokens) it can process at once. Think of it like your computer's RAM. If your machine has only 32GB of RAM, that is all it can use at one time. While context windows are getting larger, they are not infinite, and treating them as such leads to other problems [[16]](https://www.comet.com/site/blog/context-window/).
2.  **Information overload:** Just because you can fit a lot of information into the context does not mean you should. Too much context reduces the performance of the LLM by confusing it. This phenomenon is often called "context rot," where model performance degrades as more tokens are added [[72]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). It stems from the transformer architecture itself; as attention is distributed across all tokens, focus becomes diluted. This creates the "lost-in-the-middle" problem, where information at the start and end of the context is recalled far better than information in the middle [[73]](https://reinteractive.com/articles/ai-real-world-use-cases/solving-ai-agent-amnesia-context-rot-and-lost-in-the-middle).
3.  **Context drift:** This occurs when conflicting versions of the truth accumulate in the memory over time. For example, the memory might contain two conflicting statements: "*My cat is white*" and "*My cat is black*." This is not Schrodinger's Cat quantum physics experiment; it is a data conflict that confuses the LLM. Without a mechanism to resolve these conflicts, such as source trust scoring or automated contradiction checks before writing to memory, the model's responses become unreliable [[7]](https://www.coforge.com/what-we-know/blog/navigating-the-shifting-sands-understanding-and-mitigating-data-drift-in-llms), [[74]](https://www.aimagicx.com/blog/ai-agent-memory-architecture-developer-guide-2026).
4.  **Tool confusion:** The final challenge is tool confusion, which arises in two main ways. First, adding too many actions to an agent can confuse the LLM about the best one for the job, a problem that often appears with over 100 actions. Second, confusion can occur when tool descriptions are poorly written or overlap. The Gorilla benchmark shows that nearly all models perform worse when given more than one tool [[7]](https://gorilla.cs.berkeley.edu/leaderboard.html). If the distinctions between actions are unclear, even a human would struggle to choose the right one.

## Key strategies for context optimization

Initially, most AI applications were chatbots over single knowledge bases. Today, modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements.

Here are four popular context engineering strategies used across the industry:

### Selecting the Right Context

Retrieving the right information from memory is a critical first step. A common mistake is to provide everything at once, assuming that models with large context windows can handle it. As we've discussed, the "lost-in-the-middle" problem often leads to poor performance, increased latency, and higher costs [[58]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2).

To solve this, consider these approaches:

*   **Use structured outputs:** Define clear schemas for what the LLM should return. This allows you to pass only the necessary, structured information to downstream steps. We will cover this in detail in Lesson 4.
*   **Use RAG:** Instead of providing entire documents, use RAG to fetch only the specific chunks of text needed to answer a user's question. This is a core topic we will explore in Lesson 10.
*   **Reduce the number of available actions:** Rather than giving an agent access to every available action, use various strategies to delegate action subsets to specialized components. For example, a typical pattern is to leverage the orchestrator-worker pattern to delegate subtasks to specialized agents. Studies show that keeping tool selections under 30 can improve tool selection accuracy threefold [[53]](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms).
*   **Rank time-sensitive data:** For time-sensitive information, rank it by date and filter out anything no longer relevant [[12]](https://www.dailydoseofds.com/llmops-crash-course-part-8/).
*   **Repeat core instructions:** For the most important instructions, repeat them at both the start and the end of the prompt. This uses the model's tendency to pay more attention to the context edges, ensuring core instructions are not lost [[57]](https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect).

Advanced retrieval systems use scoring mechanisms that weigh relevance, recency, and importance to select the most valuable information from memory [[75]](https://mem0.ai/blog/long-term-memory-ai-agents).

```mermaid
flowchart LR
  %% External Input
  subgraph "User Interaction"
    A["User Query"]
  end

  %% Context Optimization Pipeline
  subgraph "Context Optimization Pipeline"
    subgraph "Context Construction"
      B["Initial Instructions<br/>(Core Prompt)"]
      C["RAG System<br/>(Factual Retrieval)"]
      D["Temporal Relevance<br/>(Data Ranking/Filtering)"]
      E["Tool Selection<br/>(Reduced Toolset)"]
      F["Final Instructions<br/>(Core Prompt)"]
    end
    G["Optimized Context<br/>(for LLM)"]
  end

  %% Data Sources
  subgraph "Data Sources"
    H["Knowledge Base<br/>(Vector DB)"]
    I["Time-Sensitive Data<br/>(e.g., Logs, Feeds)"]
    J["Available Tools<br/>(APIs, Functions)"]
  end

  %% Core LLM Processing
  subgraph "LLM Processing"
    K["Large Language Model<br/>(LLM)"]
  end

  %% Output Handling
  subgraph "Output Handling"
    L["Structured Outputs<br/>(Parsing & Filtering)"]
    M["Downstream System<br/>(Action / Response)"]
  end

  %% Primary Data Flows
  A -- "initiates" --> B
  A -- "informs query" --> C
  A -- "informs filter" --> D

  B -- "forms part of" --> G
  F -- "reinforces" --> G

  C -- "queries" --> H
  H -- "retrieves facts" --> C
  C -- "provides facts" --> G

  D -- "processes" --> I
  I -- "provides data" --> D
  D -- "provides ranked data" --> G

  E -- "selects from" --> J
  J -- "provides tool definitions" --> E
  E -- "provides focused tools" --> G

  G -- "final prompt" --> K

  K -- "raw output" --> L
  L -- "filtered output" --> M

  %% Indirect / Supporting Relationships
  B -. "guides tool selection" .-> E
  F -. "confirms tool selection" .-> E

  %% Visual Grouping
  classDef store stroke-dasharray:3,3
  class H,I,J store
  classDef exec stroke-width:2px
  class C,D,E,K,L exec
```
Image 4: A diagram illustrating how context optimization techniques are combined in an AI system to prepare an optimized context for an LLM and process its output.

### Context Compression

As message history grows in short-term working memory, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns, as the LLM still needs to remember what happened. Instead, you need ways to compress key facts from the past.

You can do this through:

1.  **Creating summaries of past interactions:** Use an LLM to replace a long, detailed history with a concise overview [[11]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view).
2.  **Moving user preferences to long-term memory:** Transfer user preferences from working memory to long-term episodic memory. This keeps the working context clean while ensuring preferences are remembered for future sessions.
3.  **Deduplication:** Remove redundant information from the context to avoid repetition, for example by using MinHash [[8]](https://www.datacamp.com/tutorial/prompt-compression).

```mermaid
flowchart LR
  %% Input Sources
  subgraph "Input Sources"
    PI["Past Interactions"]
    STM["Short-Term Working Memory<br/>(Current Preferences)"]
  end

  %% Context Processing & Memory Management
  subgraph "Context Management"
    LLM["LLM<br/>(Summarization Engine)"]
    SC["Summarized Context"]
    DEDUP["Deduplication Module"]
    LTM["Long-Term Episodic Memory<br/>(Persistent Preferences)"]
  end

  %% Output
  subgraph "Output"
    CC["Compressed Context"]
  end

  %% Primary Data Flows
  PI -- "summarize" --> LLM
  LLM -- "outputs" --> SC
  STM -- "persists preferences" --> LTM
  SC -- "context for" --> DEDUP
  LTM -- "persistent preferences for" --> DEDUP
  DEDUP -- "generates" --> CC

  %% Visual Grouping
  classDef memory stroke-dasharray:3,3
  classDef process stroke-width:2px
  class PI,STM,SC,LTM memory
  class LLM,DEDUP process
```
Image 5: A diagram illustrating context compression strategies, including summarization, preference management, and deduplication.

### Isolating Context

Another powerful strategy is to isolate context by splitting information across multiple agents or LLM workflows. This technique is similar to tool isolation, but it's more general, referring to the whole context. The key idea is that instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context [[31]](https://www.langchain.com/blog/context-engineering-for-agents).

We often implement this using an orchestrator-worker pattern, where a central orchestrator agent breaks down a problem and assigns sub-tasks to specialized worker agents [[46]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production). Each worker operates in its own isolated context, improving focus and allowing for parallel processing. We will cover this pattern in more detail in Lesson 5. Emerging architectures like Recursive Language Models (RLMs) take this further, decomposing tasks into sub-steps that are each handled by a fresh model instance with a clean context [[76]](https://learnaitogethernewsletter.substack.com/p/lai-110-fixing-context-rot-and-rethinking).

```mermaid
flowchart LR
  %% Input
  A["Incoming Tasks"] --> B["Orchestrator"]

  %% Orchestrator processing
  B -- "breaks into subtasks" --> C["Subtasks"]

  %% Worker Agents and Context Isolation
  subgraph "Specialized Worker Agents"
    D1["Worker Agent 1"]
    D2["Worker Agent 2"]
    D3["Worker Agent 3"]

    D1 -- "maintains own" --> E1["Focused Context<br/>(Worker 1)"]
    D2 -- "maintains own" --> E2["Focused Context<br/>(Worker 2)"]
    D3 -- "maintains own" --> E3["Focused Context<br/>(Worker 3)"]
  end

  C -- "delegates to" --> D1
  C -- "delegates to" --> D2
  C -- "delegates to" --> D3

  D1 -- "produces" --> F1["Worker Result 1"]
  D2 -- "produces" --> F2["Worker Result 2"]
  D3 -- "produces" --> F3["Worker Result 3"]

  F1 --> B
  F2 --> B
  F3 --> B

  %% Final Assembly
  B -- "assembles results" --> G["Final Assembled Results"]

  %% Visual grouping
  classDef orchestrator stroke-width:2px
  classDef worker stroke-width:1.5px
  classDef context stroke-dasharray:3,3
  class B orchestrator
  class D1,D2,D3 worker
  class E1,E2,E3 context
```
Image 6: Orchestrator-Worker Pattern for Context Isolation

### Format Optimizations

Finally, the way you format the context matters. Models are sensitive to structure, and using clear delimiters can improve performance. Common strategies are to:

*   **Use XML tags:** Wrap different pieces of context in XML-like tags (e.g., `<user_query>`, `<documents>`). This helps the model distinguish between different types of information, while making it easier for the engineer to reference context elements within the system prompt [[44]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
*   **Prefer YAML over JSON:** When providing structured data as input, YAML is often more token-efficient than JSON, which helps save space in your context window.

You always have to understand what is passed to the LLM. Seeing exactly what occupies your context window at every step is key to mastering context engineering. Usually this is done by properly monitoring your traces, tracking what happens at each step, and understanding what the inputs and outputs are [[18]](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/). As this is a significant step to go from PoC to production, we will have dedicated lessons on this.

## Here is an example

Let's connect the theory and strategies discussed earlier with concrete examples. To do that, let's consider several common real-world scenarios:

*   **Healthcare:** An AI assistant accesses a patient's medical history, current symptoms, and relevant medical literature to suggest personalized diagnoses [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
*   **Financial Services:** AI systems integrate with enterprise tools like Customer Relationship Management (CRM) systems, emails, and calendars, combining real-time market data and client portfolio information to generate tailored financial advice and reports.
*   **Project Management:** AI systems access enterprise infrastructure like CRMs, Slack, and task managers to automatically understand project requirements, then add and update project tasks.
*   **Content Creator Assistant:** An AI agent uses your research, past content, and personality traits to understand what and how to create a given piece of content.
*   **Autonomous Robotics:** Edge LLMs process real-time sensor data (like radar and thermal cameras) on robots to enable navigation and task prioritization in hazardous, zero-visibility environments without relying on remote servers [[77]](https://ojs.aaai.org/index.php/AAAI-SS/article/download/35583/37738/39654).
*   **Industrial Automation:** Multi-agent systems integrated with digital twins of factory floors interpret sensory data to autonomously plan and control production lines, reacting to real-time events [[78]](https://atpinfo.de/wp-content/uploads/2025/04/xia.pdf).

Let's walk through a specific query to see context engineering in action with the healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the AI attempts to answer, a context engineering system performs several steps:

1.  It retrieves the user's patient history, known allergies, and lifestyle habits from episodic memory [[5]](https://www.ibm.com/think/topics/ai-agent-memory).
2.  It queries a medical database for non-pharmacological headache remedies from semantic memory [[4]](https://www.nature.com/articles/s41593-023-01496-2).
3.  It assembles this information, along with the user's query and conversation history, into a structured prompt.
4.  It formats this information optimally into a prompt and calls the LLM.
5.  Finally, it presents a personalized, context-aware answer to the user.

Here’s a simplified Python example showing how these components might be assembled into a complete system prompt. Notice the clear structure, ordering, and use of XML tags.

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

*   **LLM:** Gemini as a multimodal, reasoning, and cost-effective LLM API provider.
*   **Orchestration:** LangGraph for defining stateful, agentic workflows [[65]](https://www.scalablepath.com/machine-learning/langgraph).
*   **Databases:** PostgreSQL, MongoDB, Redis, Qdrant, and Neo4j. Often, it is effective to keep it simple, as you can achieve much with only PostgreSQL or MongoDB.
*   **Observability:** Opik or LangSmith for evaluation and trace monitoring.

A common pattern for implementing personalization is to maintain a structured state for each user, containing their profile and notes. At the start of a new session, relevant portions of this state are injected into the context. During the session, new insights are captured and then consolidated back into the long-term state, ensuring memory persists and evolves across interactions [[79]](https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization).

## Connecting context engineering to AI engineering

Context engineering is more of an art than a science. It is about developing the intuition to craft effective prompts, select the right information from memory, and arrange context for optimal results. This discipline helps you determine the minimal yet essential information an LLM needs to perform at its best.

It's important to understand that context engineering, or AI engineering for that matter, cannot be learned in isolation. It is a complex field that combines:

1.  **AI Engineering:** Implement practical solutions such as LLM workflows, RAG, AI Agents, and evaluation pipelines.
2.  **Software Engineering (SWE):** Build your AI product with code that is not just functional, but also scalable and maintainable, and design architectures that can grow with your product's needs [[23]](https://sombrainc.com/blog/ai-context-engineering-guide).
3.  **Data Engineering:** Design data pipelines that feed curated and validated data into the memory layer.
4.  **Operations (Ops):** Deploy agents on the proper infrastructure to ensure they are reproducible, maintainable, observable, and scalable, including automating processes with CI/CD pipelines [[21]](https://packmind.com/context-engineering-ai-coding/what-is-contextops/).

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. In the world of AI, we should all think in systems rather than isolated components, having a mindset shift from developers to architects.

In the next lesson, we will explore structured outputs. We'll see how they act as the bridge between the probabilistic world of LLMs and the deterministic code of our applications. This pattern is a recurring theme, essential for building agents that can reason, take action, and manage data reliably.

## References

- [1] [Context Engineering: 2025’s #1 Skill in AI](https://www.decodingai.com/p/context-engineering-2025s-1-skill)
- [2] [A Survey of Context Engineering for Large Language Models](https://arxiv.org/pdf/2507.13334)
- [3] [+1 for "context engineering" over "prompt engineering".](https://x.com/karpathy/status/1937902205765607626)
- [4] [From human memory to AI memory: a survey on memory mechanisms in the era of LLMs](https://www.nature.com/articles/s41593-023-01496-2)
- [5] [How AI agent memory helps them build relationships with users](https://www.ibm.com/think/topics/ai-agent-memory)
- [6] [Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/pdf/2505.00019)
- [7] [Navigating the Shifting Sands: Understanding and Mitigating Data Drift in LLMs](https://www.coforge.com/what-we-know/blog/navigating-the-shifting-sands-understanding-and-mitigating-data-drift-in-llms)
- [8] [Prompt Compression and Budget-Aware Dialogue Management with LLMs](https://www.datacamp.com/tutorial/prompt-compression)
- [9] [Dynamic Context Prioritization for Ambiguity Resolution and Personalization in Task-Oriented Dialogue Systems](https://aclanthology.org/2025.naacl-srw.42.pdf)
- [10] [Building a Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- [11] [Context Compression](https://oneuptime.com/blog/post/2026-01-30-context-compression/view)
- [12] [LLMOps Crash Course Part 8: Memory and temporal context](https://www.dailydoseofds.com/llmops-crash-course-part-8/)
- [13] [SLM-Rank: Can Small Language Models Rank Items for Semantic Search?](https://arxiv.org/html/2510.22101v1)
- [14] [Cutting Through the Noise: Smarter Context Management for LLM-Powered Agents](https://blog.jetbrains.com/research/2025/12/efficient-context-management/)
- [15] [How to implement context engineering for AI coding assistants?](https://packmind.com/context-engineering-ai-coding/how-to-implement-context-engineering/)
- [16] [Context Window: What It Is and Why It Matters for AI Agents](https://www.comet.com/site/blog/context-window/)
- [17] [Mastering Context Window Optimization for LLM Applications](https://datahub.com/blog/context-window-optimization/)
- [18] [Context Window Management Strategies for Long Context AI Agents and Chatbots](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/)
- [19] [Cutting Through the Noise: Smarter Context Management for LLM-Powered Agents](https://blog.jetbrains.com/research/2025/12/efficient-context-management/)
- [20] [The rise of "context engineering"](https://blog.langchain.com/the-rise-of-context-engineering/)
- [21] [Why AI coding assistants fail without context : an introduction to ContextOps](https://packmind.com/context-engineering-ai-coding/what-is-contextops/)
- [22] [Context Engineering for Observability: How to Deliver the Right Data to LLMs](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms)
- [23] [AI Context Engineering Guide for Businesses](https://sombrainc.com/blog/ai-context-engineering-guide)
- [24] [Context Engineering for AI: The Foundation of Reliable, High-Performing Models](https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models)
- [25] [Understanding the Evolution from Classic Chatbots to RAG Chatbots to AI-Powered Assistants](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/)
- [26] [How to Reduce LLM Hallucination: A Practical Guide](https://www.helicone.ai/blog/how-to-reduce-llm-hallucination)
- [27] [From Vibe Coding To Context Engineering: A Blueprint for Production-Grade GenAI Systems](https://www.sundeepteki.org/blog/from-vibe-coding-to-context-engineering-a-blueprint-for-production-grade-genai-systems)
- [28] [Context Engineering: The Silent Architecture Behind Every AI Agent](https://www.linkedin.com/pulse/context-engineering-silent-architecture-behind-every-ai-roychowdhury-lzcec)
- [29] [Working Memory in LLMs: From Baddeley's Model to Enterprise AI](https://atlan.com/know/working-memory-llms/)
- [30] [How Does LLM Memory Work?](https://www.datacamp.com/blog/how-does-llm-memory-work)
- [31] [Context Engineering for Agents](https://www.langchain.com/blog/context-engineering-for-agents/)
- [32] [Context Engineering vs. Prompt Engineering: Key Differences Explained](https://www.glean.com/perspectives/context-engineering-vs-prompt-engineering-key-differences-explained)
- [33] [How Does LLM Memory Work? Types, Techniques, and More](https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/)
- [34] [Why Memory Matters in LLM Agents: Short-Term vs. Long-Term Memory Architectures](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/)
- [35] [Episodic vs Persistent Memory in LLMs: A Deep Dive](https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/)
- [36] [Prompt Engineering in Healthcare](https://www.mdpi.com/2079-9292/13/15/2961)
- [37] [Multi-Agent Orchestration Patterns for Production](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)
- [38] [Multi-Agent Orchestration: A Comprehensive Guide](https://gurusup.com/blog/multi-agent-orchestration-guide)
- [39] [Multi-Agent Systems: Building with Context Engineering](https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering)
- [40] [Deterministic AI Orchestration: A Platform Architecture for Autonomous Development](https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/)
- [41] [A Framework for Building and Operating Language Agent Systems in Production](https://arxiv.org/html/2601.13671v1)
- [42] [Prompt Engineering Vs. Context Engineering: Understanding the Difference](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m)
- [43] [Prompt Engineering vs Context Engineering: What's the Difference?](https://memgraph.com/blog/prompt-engineering-vs-context-engineering)
- [44] [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [45] [What is Context Engineering? A Guide for Building Reliable AI Agents](https://www.instinctools.com/blog/context-engineering/)
- [46] [Multi-Agent Orchestration Patterns for Production](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)
- [47] [Agentic AI: Context Engineering vs. Prompt Engineering](https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/)
- [48] [Lost in the Middle: A lesson on failing AI agents backwards](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e)
- [49] [Needle-in-a-Haystack: Optimizing Retrieval and RAG over Long Context Windows](https://bigdataboutique.com/blog/needle-in-haystack-optimizing-retrieval-and-rag-over-long-context-windows-5dfb3c)
- [50] [Context Engineering in AI: A Practical Guide](https://www.codecademy.com/article/context-engineering-in-ai)
- [51] [Context Engineering in LLMs and AI Agents](https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b)
- [52] [Context Engineering Platforms Comparison 2026: LlamaIndex, LangChain, CrewAI, Atlan](https://atlan.com/know/context-engineering-platforms-comparison/)
- [53] [Context Engineering for Observability: How to Deliver the Right Data to LLMs](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms)
- [54] [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)
- [55] [Context Engineering: A Guide With Examples](https://www.datacamp.com/blog/context-engineering)
- [56] [Context Engineering - What it is, and techniques to consider](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider)
- [57] [Lost-in-the-Middle Effect](https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect)
- [58] [The "Lost in the Middle" Problem: Why LLMs Ignore the Middle of Your Context Window](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [59] [LLM Context Window Limitations: Impacts, Risks, & Fixes in 2026](https://atlan.com/know/llm-context-window-limitations/)
- [60] [Context Engineering Guide](https://nlp.elvissaravia.com/p/context-engineering-guide)
- [61] [What is Context Engineering?](https://www.pinecone.io/learn/context-engineering/)
- [62] [Own your context window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
- [63] [Context Engineering 101 cheat sheet](https://x.com/lenadroid/status/1943685060785524824)
- [64] [Context Engineering Guide 101](https://www.decodingai.com/p/context-engineering-2025s-1-skill)
- [65] [LangGraph: A New Way to Build Stateful, Multi-agent Applications](https://www.scalablepath.com/machine-learning/langgraph)
- [66] [A Survey of Context Engineering for Large Language Models](https://arxiv.org/html/2507.13334v1)
- [67] [Context Engineering in the AI Era](https://www.contentstack.com/blog/ai/context-engineering-in-the-ai-era)
- [68] [Context Engineering vs. Fine-Tuning vs. Distillation: How to Decide?](https://blog.agami.ai/context-engineering-vs-fine-tuning-vs-distillation-how-to-decide/)
- [69] [Fine-tuning vs. in-context learning: New research guides better LLM customization for real-world tasks](https://venturebeat.com/ai/fine-tuning-vs-in-context-learning-new-research-guides-better-llm-customization-for-real-world-tasks)
- [70] [The End of Fine-Tuning? Stanford's ACE Framework Turns Context Into Intelligence](https://www.ikangai.com/the-end-of-fine-tuning-stanfords-ace-framework-turns-context-into-intelligence/)
- [71] [Context Engineering](https://weaviate.io/blog/context-engineering)
- [72] [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [73] [Solving AI Agent Amnesia: Context Rot and Lost in the Middle](https://reinteractive.com/articles/ai-real-world-use-cases/solving-ai-agent-amnesia-context-rot-and-lost-in-the-middle)
- [74] [AI Agent Memory Architecture: Developer Guide 2026](https://www.aimagicx.com/blog/ai-agent-memory-architecture-developer-guide-2026)
- [75] [Long-Term Memory for AI Agents](https://mem0.ai/blog/long-term-memory-ai-agents)
- [76] [Fixing context rot and rethinking the long context LLM](https://learnaitogethernewsletter.substack.com/p/lai-110-fixing-context-rot-and-rethinking)
- [77] [Edge LLMs for Real-Time Contextual Understanding on Robotic Platforms](https://ojs.aaai.org/index.php/AAAI-SS/article/download/35583/37738/39654)
- [78] [LLM-based Multi-Agent Systems for Industrial Automation](https://atpinfo.de/wp-content/uploads/2025/04/xia.pdf)
- [79] [Context personalization](https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization)