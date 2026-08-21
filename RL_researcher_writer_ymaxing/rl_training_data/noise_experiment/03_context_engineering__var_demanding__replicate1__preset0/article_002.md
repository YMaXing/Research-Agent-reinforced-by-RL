# Context Engineering: 2025’s #1 Skill in AI

## Introduction: When prompt engineering breaks

The story of modern AI applications is one of rapid evolution. In 2022, the world was introduced to simple chatbots, capable of answering questions in a single turn [[29]]. By 2023, these evolved into Retrieval-Augmented Generation (RAG) systems, which could connect LLMs to domain-specific knowledge, making them far more useful for specialized tasks. The year 2024 brought us tool-using agents that could perform actions and interact with external systems [[27]]. Now, in 2025, we are building memory-enabled agents that remember past interactions, learn user preferences, and build relationships over time.

In our last lesson, we explored the landscape of AI agents and LLM workflows and how to choose between them. As these applications grow more complex, prompt engineering, a practice that once served us well, is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The sheer volume of information an agent might need has grown exponentially. This includes past conversations, user data, documents, and action descriptions.

Simply stuffing all this information into a prompt is not a viable strategy. This approach leads to a new set of problems that require a more disciplined solution. Context engineering is the practice of orchestrating this entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it. This skill is becoming a core foundation for AI engineering, and in this lesson, we will explore why it is so valuable and how to apply it.

## From prompt to context engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event. This approach breaks down in stateful applications where context must be preserved and managed across multiple turns. As a conversation or task progresses, the context grows, and without a strategy to manage this growth, the LLM’s performance degrades.

This degradation happens in several ways. First, there is **context decay**, where the model gets confused by the noise of an ever-expanding history. This is often called the "lost-in-the-middle" problem, where models struggle to access information buried in the middle of long inputs. Research consistently shows that model accuracy can drop by over 30% when relevant information is not at the beginning or end of the context [[59]]. Performance can start to degrade significantly once the context exceeds 32,000 tokens, long before advertised limits are reached [[21]].

Second, there is the **context window challenge**. The context window is the model's finite working memory, and every piece of information competes for space [[31], [33]]. The self-attention mechanism in transformers also imposes a quadratic computational overhead. This means that as the context length doubles, the computation required can quadruple, making large contexts slow and expensive [[22]].

Finally, every token adds to the **cost and latency** of an LLM call. In agentic workflows, where context accumulates with each step, costs can balloon quickly [[16]]. A naive approach of "context-augmented generation," or just dumping everything in, creates a slow, expensive, and underperforming system. We will explore these concepts in more detail in upcoming lessons, including memory in Lesson 9 and RAG in Lesson 10.

On a recent project, we learned this the hard way. We were working with a model that supported a two-million-token context window, so we thought, "*What could go wrong*?" We stuffed everything in: our research, guidelines, examples, and user history. The result was an LLM workflow that took 30 minutes to run and produced low-quality outputs.

A more disciplined approach is needed. Context engineering shifts the focus from crafting static prompts to building dynamic systems that manage information flow. As an AI engineer, your job is to select only the most essential pieces of context for each LLM call. This makes your applications accurate, fast, and cost-effective.

## Understanding context engineering

Context engineering is the practice of finding the best way to arrange parts of your application's memory into the context that is passed to an LLM to achieve the best results. It is a solution to an optimization problem where you retrieve the right parts of both your short- and long-term memory to solve a specific task without overwhelming the model [[22]]. For example, when you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies or taste preferences. This precise selection ensures the model receives only the essential information.

Andrej Karpathy offered a great analogy for this: LLMs are like a new kind of operating system, where the model acts as the CPU and its context window functions as the RAM [[31], [33]]. Just as an operating system manages what fits into RAM, context engineering curates what occupies the model’s working memory. This analogy has profound implications for system design. It reframes the challenge from simply writing prompts to managing a critical system resource, forcing engineers to think about information logistics, memory hierarchies, and efficient data retrieval—much like an OS developer would [[34]]. It is important to note that the context is a *subset* of the system's total working memory; you can hold information without passing it to the LLM on every turn.

How does context engineering relate to prompt engineering? It is simple. Prompt engineering is a subset of context engineering. You still write effective prompts, but you also design a system that feeds the right context into those prompts. The scope expands from optimizing a single interaction to architecting an entire information ecosystem. While prompt engineering focuses on *how* to phrase tasks, context engineering determines *what* information to provide in the first place, a more system-level and stateful challenge.

| Dimension | Prompt Engineering | Context Engineering |
|-----------|-------------------|---------------------|
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Stateless function | Stateful due to memory |
| Focus | How to phrase tasks | What information to provide |

Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible. Data changes constantly, making fine-tuning a last resort. For most enterprise use cases, you get better results faster and more cheaply with context engineering [[52], [53]]. It allows for rapid iteration and adaptation to evolving data without altering the core model, a key advantage in dynamic environments. This approach avoids the computational resources and specialized expertise required for retraining, offering a more agile path to reliable AI applications.

When you start a new AI project, your decision-making process for guiding the LLM should look like the one presented in Image 1. This workflow provides a clear rationale: start with the simplest, cheapest method (prompting), and only escalate to more complex and costly solutions (context engineering, then fine-tuning) if the previous step fails to solve the problem. This pragmatic, iterative approach saves time and resources.

```mermaid
graph TD
    A["Prompt Engineering"] --> B{"Does it solve the problem?"}
    B -->|"Yes"| Z["End"]
    B -->|"No"| D["Context Engineering"]
    D --> E{"Does it solve the problem?"}
    E -->|"Yes"| Z
    E -->|"No"| G["Fine-tuning"]
    G --> H{"Can you make a fine-tuning dataset?"}
    H -->|"Yes"| Z
    H -->|"No"| J["Reframe the problem"]
    J --> A
```

Image 1: A flowchart illustrating the decision-making workflow for choosing a key strategy when starting a new AI project.

For instance, if you build an agent to process internal Slack messages, you do not need to fine-tune a model on your company’s communication style. It is more effective to use a powerful reasoning model and engineer the context to retrieve specific messages and enable actions like creating tasks or drafting emails. Throughout this course, we will show you how to solve most industry problems using only context engineering.

## What makes up the context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model. The high-level workflow, as presented in Image 2, begins when a user input triggers the system to pull relevant information from both long-term and short-term memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
flowchart LR
  %% User interaction
  A["User Input"]

  %% Memory components
  subgraph "Memory Management"
    B["Long-term Memory"]
    C["Short-Term Working Memory"]
  end

  %% Context and Prompt Generation
  subgraph "Context & Prompt Generation"
    D["Context"]
    E["Prompt Template"]
    F["Prompt"]
  end

  %% LLM Interaction
  subgraph "LLM Interaction"
    G["LLM Call"]
    H["Answer"]
  end

  %% Primary flow
  A -- "initiates" --> B
  B -- "retrieves relevant info" --> C
  C -- "assembles" --> D
  D -- "populates" --> E
  E -- "creates" --> F
  F -- "sends" --> G
  G -- "generates" --> H

  %% Feedback loop for memory updates
  H -- "updates" --> C
  H -- "stores new info" --> B

  %% Visual grouping
  classDef memory stroke-dasharray:3,3
  classDef process stroke-width:2px
  class B,C memory
  class D,E,F,G,H process
```

Image 2: A flowchart illustrating the high-level workflow of how context is processed in an LLM application.

These components are grouped into two main categories. We will explain them intuitively for now, as we have future dedicated lessons for all of them.

### Short-Term Working Memory

Short-term working memory is the state of the agent for the current task or conversation. It is volatile and changes with each interaction, helping the agent maintain a coherent dialogue and make immediate decisions. It includes the **user input**, which is the most recent query from the user and serves as the primary trigger for the agent's next action. It also contains the **message history**, the log of the current conversation that allows the LLM to understand previous turns and maintain conversational flow. The agent's **internal thoughts**, such as a "scratchpad" for reasoning steps, contribute to the context by making the decision-making process explicit. Finally, **tool calls and outputs**, which are the results from any actions the agent has performed, provide essential feedback from external systems, grounding the agent in reality [[36], [39]]. This working memory is the agent's immediate "consciousness."

### Long-Term Memory

Long-term memory is more persistent and stores information across sessions, allowing the AI system to remember things beyond a single conversation. We divide it into three types, drawing parallels from human memory [[22], [37]]. An AI system can include some or all of them:

**Procedural memory** is knowledge encoded directly in the code. It includes the system prompt, which sets the agent's overall behavior and rules. It also includes the definitions of available actions, which tell the agent what it can do, and schemas for structured outputs, which guide the format of its responses. This procedural memory dictates the agent's "instincts" and operational boundaries, ensuring it behaves predictably and uses its capabilities correctly [[37]].

**Episodic memory** is the memory of specific past experiences, like user preferences or previous interactions and agent actions. It is used to help the agent personalize its responses based on individual users. This type of memory allows the agent to remember things like "the user prefers concise answers" or "we discussed project X yesterday." We typically store this in vector or graph databases for efficient retrieval, enabling the agent to build a continuous relationship with the user across multiple sessions [[37], [40]].

**Semantic memory** is the agent’s factual knowledge base. It can be internal, like company documents stored in a database, or external, accessed via the internet through API calls or web scraping. This memory provides the factual information the agent needs to answer questions, such as "What were our Q3 sales figures?" This is the core of RAG, grounding the agent's responses in verifiable data rather than just its pre-trained knowledge [[37], [38]].

If this seems like a lot, bear with us. We will cover all these concepts in-depth in future lessons, including structured outputs (Lesson 4), tools (Lesson 6), memory (Lesson 9), RAG (Lesson 10), and working with multimodal data (Lesson 11).

<https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39dce26a-e51e-4167-ac9e-ca28c45b53a6_1115x708.png>
Image 3: A detailed illustration of how all the context engineering components work together inside an AI agent (Source [Decoding AI Magazine [21]](https://www.decodingai.com/p/context-engineering-2025s-1-skill))

The key takeaway is that these components are not static. They are dynamically re-computed for every single interaction. For each conversation turn or new task, the short-term memory grows, or the long-term memory can change. Context engineering involves knowing how to select the right pieces from this vast memory pool to construct the most effective prompt for the task at hand.

## Production implementation challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These challenges all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that come up when building AI applications:

1.  **The context window challenge:** Every AI model has a limited context window, which is the maximum amount of information (tokens) it can process simultaneously. For example, models like GPT-4o have a 128K token window, while Gemini 2.5 Pro offers up to 1M tokens [[59]]. However, the model's working memory is finite. The self-attention mechanism in transformers imposes a quadratic computational overhead, and the Key-Value (KV) cache, which stores intermediate computations, can become a memory bottleneck, making large contexts expensive and slow [[22], [33]].

2.  **Information overload:** Too much context reduces the performance of the LLM by confusing it. This is known as the "lost-in-the-middle" or "needle in a haystack" problem, where LLMs are known for remembering information best at the beginning and end of the context window. Empirical evidence from a 2023 Stanford study showed that accuracy drops by over 30% for information in the middle of a long context [[59]]. A 2025 study by Chroma on 18 frontier models confirmed that adding "distractors"—semantically similar but irrelevant information—amplifies this degradation, making the problem worse than just length alone [[3]].

3.  **Context drift:** This occurs when conflicting versions of the truth accumulate in the memory over time. The causes are often stale information from a knowledge base or conflicting updates from user interactions. For example, the memory might contain two conflicting statements: "*The user's budget is $500*" and later "*The user's budget is $1,000*." This is not a quantum physics experiment; it is a data conflict that confuses the LLM [[6]]. Without a mechanism to resolve or prune outdated facts, the agent's knowledge base becomes unreliable, leading to inconsistent reasoning and a gradual erosion of user trust [[7], [8]].

4.  **Tool confusion:** The final challenge is tool confusion, which arises in two main ways. First, adding too many tools to an agent can confuse the LLM about the best one for the job. The Gorilla benchmark shows that nearly all models perform worse when given more than one tool [[21]]. Second, confusion can occur when tool descriptions are poorly written or overlap. If the distinctions between actions are unclear, the model may choose the wrong tool or fail to act, leading to failed tasks. This is a common failure point in production systems where agents must navigate dozens of APIs.

## Key strategies for context optimization

Initially, most AI applications were chatbots over single knowledge bases. Today, modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements.

Here are four popular context engineering strategies used across the industry:

### Selecting the right context

Retrieving the right information from memory is an essential first step. A common mistake is to provide everything at once. To solve this, you should use RAG with reranking to fetch only the most relevant facts. The mechanics of RAG involve searching a vector database for chunks of text that are semantically similar to the user's query, which ensures the context is both concise and factually accurate. You can also use structured outputs to pass only the necessary information to downstream steps. This reduces context size and improves the reliability of processing by ensuring data conforms to a predictable schema. For time-sensitive information, you can implement temporal ranking to filter out outdated data. Algorithms for this can be as simple as sorting by date or more complex, involving decay functions that reduce the relevance of older information. Another effective technique is to reduce the number of available tools. Studies have shown that limiting the selection to under 30 tools can triple an agent's selection accuracy by reducing ambiguity [[21]]. This can be achieved through tool delegation, where a primary agent routes tasks to specialized sub-agents with smaller toolsets. Finally, for the most important instructions, repeat them at both the start and the end of the prompt. Empirical evidence shows this leverages the model's tendency to pay more attention to the context edges, ensuring core instructions are not lost [[57]].

```mermaid
flowchart LR
  %% Input
  subgraph "Input"
    UQ["User Query"]
  end

  %% Context Selection & Preparation
  subgraph "Context Selection & Preparation"
    RAG["RAG<br/>(Retrieval-Augmented Generation)"]
    RAT["Reducing the number of available tools"]
    TR["Temporal Relevance"]
    PCI["Repeat core instructions<br/>at both the start and the end"]
  end

  %% LLM Core
  subgraph "LLM Core"
    LLMC["LLM Context"]
    LLMCALL["LLM Call"]
  end

  %% Output Processing
  subgraph "Output Processing"
    SO["Structured Outputs"]
  end

  %% Primary data flows
  UQ -- "initiates" --> RAG
  UQ -- "informs" --> RAT
  UQ -- "filters by" --> TR

  RAG -- "retrieved info" --> LLMC
  RAT -- "tool selection" --> LLMC
  TR -- "time-sensitive data" --> LLMC
  PCI -- "prompt construction" --> LLMC

  LLMC -- "context for" --> LLMCALL
  LLMCALL -- "produces" --> SO

  %% Visual grouping
  classDef input_node stroke-width:2px
  classDef context_prep stroke-dasharray:3,3
  classDef llm_process stroke-width:3px
  classDef output_node stroke-width:2px,stroke-dasharray:5,5

  class UQ input_node
  class RAG,RAT,TR,PCI context_prep
  class LLMC,LLMCALL llm_process
  class SO output_node
```

Image 4: An architecture diagram illustrating context selection techniques in an LLM system.

We will cover structured outputs in Lesson 4 and RAG in Lesson 10.

### Context compression

As message history grows in short-term working memory, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns, as the LLM still needs to remember what happened. Instead, you need ways to compress key facts from the past. You can do this by **creating summaries of past interactions** using an LLM to replace a long, detailed history with a concise overview. This can involve extractive summarization (picking key sentences) or abstractive summarization (generating new, shorter text). Another method is **moving user preferences to long-term memory**, transferring them from working memory to episodic memory to keep the working context clean. This involves identifying and persisting user preferences to a database for retrieval in future sessions. Finally, **deduplication** techniques, such as semantic clustering or MinHash, can identify and remove redundant information from the context to avoid repetition [[11], [12], [14]].

```mermaid
flowchart LR
    A["Message History<br/>(Short-term Working Memory)"] -->|"processed by"| B["Deduplication"]

    B -->|"for summarization"| C["Creating summaries of past interactions<br/>(using an LLM)"]
    B -->|"for preference extraction"| D["Moving preferences about the user<br/>into Long-term Memory (Episodic Memory)"]

    C -->|"generates"| E["Compressed Context"]
    D -->|"contributes to"| E

    E -->|"used for"| F["LLM Call"]
```

Image 5: A flowchart illustrating context compression strategies for managing short-term working memory.

### Isolating Context

Another powerful strategy is to isolate context by splitting information across multiple agents or LLM workflows. This technique is similar to tool isolation but is more general, referring to the whole context. The key idea is that instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context. This approach improves scalability, maintainability, and performance by allowing each agent to specialize. We often implement this using an orchestrator-worker pattern, where a central orchestrator agent breaks down a problem and assigns sub-tasks to specialized worker agents [[46], [47]]. Each worker operates in its own isolated context, which prevents cross-domain hallucinations, reduces token consumption by 60-70%, and allows for parallel processing [[47], [48]]. We will cover this pattern in more detail in Lesson 5.

```mermaid
flowchart LR
  %% Orchestrator-Worker Pattern for Context Isolation

  subgraph Orchestrator["Orchestrator Agent"]
    OA_Receive["Receives Complex Task"]
    OA_Decompose["Decomposes Task into Subtasks"]
    OA_Delegate["Delegates Subtasks"]
    OA_Assemble["Assembles Final Result"]
  end

  subgraph Worker_Pool["Worker Agents"]
    WA_Node["Worker Agent"]
    WA_Node -- "has" --> WA_Context["Isolated Context Window"]
    WA_Node --> WA_Perform["Performs Specific Subtask"]
    WA_Perform --> WA_Return["Returns Results"]
  end

  CT["Complex Task"] --> OA_Receive
  OA_Receive --> OA_Decompose
  OA_Decompose --> OA_Delegate
  
  OA_Delegate -- "delegates to" --> WA_Node
  WA_Return -- "returns to" --> OA_Assemble
  
  OA_Assemble --> FR["Final Result"]
```

Image 6: Architecture diagram illustrating the orchestrator-worker pattern for context isolation.

### Format Optimizations

Finally, the way you format the context matters. Models are sensitive to structure, and using clear delimiters can improve performance. A common strategy is to use XML tags to wrap different pieces of context (e.g., `<user_query>`, `<documents>`) [[44]]. This helps the model distinguish between different types of information and improves reasoning reliability by making the input structure explicit. Also, when providing structured data as input, YAML is often more token-efficient than JSON. One study found it to be 66% more token-efficient, which helps save space in your context window [[21]].

You always have to understand what is passed to the LLM. Seeing exactly what occupies your context window at every step is key to mastering context engineering. This is usually done by properly monitoring your traces, tracking what happens at each step, and understanding the inputs and outputs [[16], [18]]. As this is a significant step to go from PoC to production, we will have dedicated lessons on this.

## Here is an example

Let's connect the theory and strategies discussed earlier with concrete examples. Context engineering is applied to build powerful AI systems in various domains.

*   In **healthcare**, an AI assistant can access a patient's history, current symptoms, and relevant medical literature to suggest personalized diagnoses. This involves retrieving sensitive data like patient records, allergies, and lifestyle habits from episodic memory, which requires strict privacy controls and data governance [[41]].
*   In **financial services**, an agent might integrate with a company's Customer Relationship Management (CRM) system, calendars, and financial data to make decisions based on user preferences. This requires managing context from multiple enterprise systems and adhering to strict compliance and privacy rules.
*   For **project management**, an AI system can access tools like CRMs, Slack, and task managers to automatically understand project requirements and update tasks, isolating context for each tool to avoid confusion.
*   A **content creator assistant** uses your research, past content, and personality traits to understand what and how to create a given piece of content, managing diverse sources and personal style guides.

Let's walk through a concrete example. Imagine a user asks a healthcare assistant: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the LLM even sees this query, a context engineering system gets to work:
1.  It retrieves the user's patient history, known allergies, and lifestyle habits from an episodic memory store [[41]].
2.  It queries a semantic memory of up-to-date medical literature for non-medicinal headache remedies.
3.  It assembles this information, along with the user's query and the conversation history, into a structured prompt.
4.  We send the prompt to the LLM, which generates a personalized, safe, and relevant recommendation.
5.  We log the interaction and save any new preferences back to the user's episodic memory.

Here’s a simplified Python example showing how these components might be assembled into a complete system prompt. Notice the clear structure and ordering, using XML tags to delineate different types of information.

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

A real-world failure mode for this kind of system is context rot. For example, a coding agent might be tasked with a multi-step refactoring job. In step 5, it correctly defines a function signature. However, after 20 more steps of tool calls and reasoning, the context window fills up, and the original function signature is dropped. By step 25, the agent generates new code that calls the function with the wrong arguments, causing the entire workflow to fail at compilation [[59]]. The mitigation strategy here would be context compression: summarizing the outcomes of earlier steps (like the function signature) and storing them in a more compact form in a scratchpad or episodic memory, ensuring essential details persist throughout the task.

To build such a system, you would use a combination of tools. An LLM like **Gemini** provides the reasoning engine. A framework like **LangGraph** orchestrates the workflow. Databases such as **PostgreSQL**, **Qdrant**, or **Neo4j** serve as long-term memory stores [[62]]. Specialized tools like **Mem0** can manage memory state, and observability platforms like **Opik** or **LangSmith** are essential for debugging complex interactions [[16], [64], [65]]. Often, it is effective to keep it simple, as you can achieve much with only PostgreSQL or MongoDB.

## Connecting context engineering to AI engineering

The practice of context engineering is more about building intuition than learning a specific algorithm. It is the art of knowing how to structure prompts, what information to include, and how to order it for maximum impact. This discipline helps you determine the minimal yet essential information an LLM needs to perform at its best, balancing the trade-offs between providing enough context and avoiding information overload.

This skill does not exist in a vacuum. It’s a multidisciplinary practice that sits at the intersection of several key engineering fields [[22], [23]]:

*   **AI Engineering:** This is the foundation. It involves implementing practical solutions such as LLM workflows, RAG, AI Agents, and evaluation pipelines. A key task here is to design and test different context management strategies to see how they impact model performance on specific business metrics.
*   **Software Engineering:** You need to build scalable and maintainable systems to aggregate context and wrap agents in robust APIs. This means applying principles like modularity, clear documentation, and automated testing to your AI systems, ensuring that your context-handling logic is as reliable as any other part of your application.
*   **Data Engineering:** Constructing reliable data pipelines for RAG and other memory systems is essential. This includes building Extract, Transform, Load (ETL) processes, implementing data quality checks, and establishing data governance to ensure the context fed to the LLM is accurate, fresh, and trustworthy.
*   **MLOps:** Deploying agents on the right infrastructure and automating Continuous Integration/Continuous Deployment (CI/CD) makes them reproducible, observable, and scalable. This involves monitoring for context drift, logging all interactions for debugging, and managing the lifecycle of your context-aware AI systems in production.

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. In the world of AI, we should all think in systems rather than isolated components, having a mindset shift from developers to architects.

In the next lesson, we will explore structured outputs, a key technique for selecting and formatting context. Later in the course, we will dive deeper into other concepts introduced here, such as tools, memory, and RAG, to give you a complete toolkit for building intelligent AI systems.

## References

- [1] Needle In A Haystack - Pressure Testing LLMs. (2023). https://github.com/gkamradt/LLMTest_NeedleInAHaystack
- [2] Context Window Overflow in LLMs. (n.d.). https://redis.io/blog/context-window-overflow/
- [3] Context Rot: How Increasing Input Tokens Impacts LLM Performance. (2025). https://www.trychroma.com/research/context-rot
- [4] The Common Failure Points of LLM RAG Systems and How to Overcome Them. (n.d.). https://medium.com/@sahin.samia/the-common-failure-points-of-llm-rag-systems-and-how-to-overcome-them-926d9090a88f
- [5] Your 1M+ context window LLM is less powerful than you think. (n.d.). https://towardsdatascience.com/your-1m-context-window-llm-is-less-powerful-than-you-think/
- [6] Seven Strategies to Maintain LLM Reliability Across Diverse Use Cases in Production. (2025). https://galileo.ai/blog/production-llm-monitoring-strategies
- [7] Navigating the Shifting Sands: Understanding and Mitigating Data Drift in LLMs. (n.d.). https://www.coforge.com/what-we-know/blog/navigating-the-shifting-sands-understanding-and-mitigating-data-drift-in-llms
- [8] Context Rot in Enterprise AI LLMs. (n.d.). https://thenewstack.io/context-rot-enterprise-ai-llms/
- [9] The Hidden Cost of LLM Drift Detection. (n.d.). https://insightfinder.com/blog/hidden-cost-llm-drift-detection/
- [11] How to Build Context Compression. (2026). https://oneuptime.com/blog/post/2026-01-30-context-compression/view
- [12] LLMOps Crash Course Part 8. (n.d.). https://www.dailydoseofds.com/llmops-crash-course-part-8/
- [13] Context Compression via Item Description Summarization for SLM Relevance Ranking. (2025). https://arxiv.org/html/2510.22101v1
- [14] Efficient Context Management for LLM Agents. (2025). https://blog.jetbrains.com/research/2025/12/efficient-context-management/
- [15] Context Engineering - What it is, and techniques to consider. (n.d.). https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider
- [16] Context Window: What It Is and Why It Matters for AI Agents. (2025). https://www.comet.com/site/blog/context-window/
- [17] Context Window Optimization. (n.d.). https://datahub.com/blog/context-window-optimization/
- [18] Context Window Management Strategies for Long-Context AI Agents and Chatbots. (n.d.). https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/
- [19] The rise of "context engineering". (2025). https://blog.langchain.com/the-rise-of-context-engineering/
- [20] What is Context Engineering?. (n.d.). https://www.pinecone.io/learn/context-engineering/
- [21] Context Engineering: 2025’s #1 Skill in AI. (2025). https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [22] A Survey of Context Engineering for Large Language Models. (2025). https://arxiv.org/pdf/2507.13334
- [23] Context Engineering. (n.d.). https://www.philschmid.de/context-engineering
- [24] What is ContextOps?. (n.d.). https://packmind.com/context-engineering-ai-coding/what-is-contextops/
- [25] Context Engineering for Observability. (n.d.). https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms
- [26] AI Context Engineering Guide. (n.d.). https://sombrainc.com/blog/ai-context-engineering-guide
- [27] Context Engineering: A Guide With Examples. (n.d.). https://www.datacamp.com/blog/context-engineering
- [28] Context Engineering: The Foundation of Reliable, High-Performing Models. (n.d.). https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models
- [29] Understanding the Evolution from Classic Chatbots to RAG Chatbots to AI-Powered Assistants. (2024). https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/
- [30] Evolution of AI Chatbots. (n.d.). https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots
- [31] Karpathy, A. on X. (n.d.). https://x.com/karpathy/status/1937902205765607626
- [32] Context Engineering vs. Prompt Engineering: Key Differences Explained. (n.d.). https://www.glean.com/perspectives/context-engineering-vs-prompt-engineering-key-differences-explained
- [33] Working Memory in LLMs. (n.d.). https://atlan.com/know/working-memory-llms/
- [34] From Vibe Coding to Context Engineering. (n.d.). https://www.sundeepteki.org/blog/from-vibe-coding-to-context-engineering-a-blueprint-for-production-grade-genai-systems
- [35] Context Engineering: The Silent Architecture Behind Every AI. (n.d.). https://www.linkedin.com/pulse/context-engineering-silent-architecture-behind-every-ai-roychowdhury-lzcec
- [36] Working Memory in LLMs. (n.d.). https://atlan.com/know/working-memory-llms/
- [37] How Does LLM Memory Work?. (n.d.). https://www.datacamp.com/blog/how-does-llm-memory-work
- [38] How Does LLM Memory Work?. (2026). https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/
- [39] Why Memory Matters in LLM Agents. (n.d.). https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/
- [40] Episodic vs. Persistent Memory in LLMs. (n.d.). https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/
- [41] Context Engineering: 2025’s #1 Skill in AI. (2025). https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [42] 12-Factor Agents. (n.d.). https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
- [43] Prompt Engineering in Healthcare. (2025). https://www.mdpi.com/2079-9292/13/15/2961
- [44] Effective Context Engineering for AI Agents. (n.d.). https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [45] Context Engineering Guide. (2025). https://nlp.elvissaravia.com/p/context-engineering-guide
- [46] Multi-Agent Orchestration Patterns in Production. (n.d.). https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- [47] Multi-Agent Orchestration Guide. (n.d.). https://gurusup.com/blog/multi-agent-orchestration-guide
- [48] Multi-Agent Systems: Building with Context Engineering. (n.d.). https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering
- [49] Deterministic AI Orchestration. (n.d.). https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/
- [50] Specialized Agents. (2026). https://arxiv.org/html/2601.13671v1
- [51] Prompt Engineering vs. Context Engineering. (n.d.). https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m
- [52] Prompt Engineering vs. Context Engineering. (n.d.). https://memgraph.com/blog/prompt-engineering-vs-context-engineering
- [53] Context Engineering for Observability. (n.d.). https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms
- [54] Context Engineering. (n.d.). https://www.instinctools.com/blog/context-engineering/
- [55] Agentic AI: Context Engineering vs. Prompt Engineering. (n.d.). https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/
- [56] Lost in the Middle: A Lesson in Failing AI Agents Backwards. (n.d.). https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e
- [57] Lost-in-the-Middle Effect. (n.d.). https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect
- [58] The Lost in the Middle Problem. (n.d.). https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [59] LLM Context Window Limitations. (n.d.). https://atlan.com/know/llm-context-window-limitations/
- [60] Needle in a Haystack. (n.d.). https://bigdataboutique.com/blog/needle-in-haystack-optimizing-retrieval-and-rag-over-long-context-windows-5dfb3c
- [61] Context Engineering in AI. (n.d.). https://www.codecademy.com/article/context-engineering-in-ai
- [62] Context Engineering in LLMs and AI Agents. (n.d.). https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b
- [63] Context Engineering 101 cheat sheet. (n.d.). https://x.com/lenadroid/status/1943685060785524824
- [64] Context Engineering Platforms Comparison. (n.d.). https://atlan.com/know/context-engineering-platforms-comparison/
- [65] LangGraph. (n.d.). https://www.scalablepath.com/machine-learning/langgraph