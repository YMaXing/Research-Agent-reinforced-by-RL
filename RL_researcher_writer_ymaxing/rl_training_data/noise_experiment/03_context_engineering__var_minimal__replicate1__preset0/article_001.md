# Lesson 3: Context Engineering

## When prompt engineering breaks

AI applications have evolved rapidly. In 2022, we had simple chatbots. By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge. Now, we are building memory-enabled agents that remember past interactions and perform actions over time.

In our last lesson, we explored how to choose between AI agents and LLM workflows. As these applications grow more complex, prompt engineering, which optimizes single LLM calls, is showing its limits. The volume of information an agent might need has grown exponentially. A new discipline, context engineering, is required to orchestrate this entire information ecosystem and ensure the LLM gets exactly what it needs.

## From Prompt to Context Engineering

Prompt engineering is designed for single, stateless interactions, treating each LLM call as an isolated event. This approach breaks down in stateful applications where context must be managed across multiple turns.

As a task progresses, the context grows. Without a strategy, the LLM’s performance degrades due to context decay: the model gets confused by the noise of an ever-expanding history, leading to hallucinations and misguided answers [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). Even with large context windows, every token adds to cost and latency. On a recent project, we learned this the hard way when a workflow with a massive context took 30 minutes to run and produced low-quality outputs [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

The solution is to shift from crafting static prompts to building dynamic systems that manage information flow. As an AI engineer, your job is to select only the most critical pieces of context for each LLM call, making your applications accurate, fast, and cost-effective.

## Understanding Context Engineering

Context engineering is the practice of strategically filling the model’s limited context window with the right information, at the right time, and in the right format [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). It is an optimization problem: we retrieve the necessary parts from memory to solve a task without overwhelming the model. For example, a cooking agent needs a specific recipe and user allergies, not the entire cookbook.

Andrej Karpathy offered a great analogy for this: LLMs are like a new kind of operating system, where the model acts as the CPU and its context window functions as the RAM [[2]](https://x.com/karpathy/status/1937902205765607626). Just as an operating system manages what fits into RAM, context engineering curates what occupies the model’s working memory.

Prompt engineering is a subset of context engineering. You still write effective prompts, but you also design a system that feeds the right context into them. This means understanding not just *how* to phrase a task, but *what* information the model needs to perform optimally [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

| Dimension | Prompt Engineering | Context Engineering |
| --- | --- | --- |
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Primarily stateless | Inherently stateful, with explicit memory management |
| Focus | How to phrase tasks | What information to provide |

Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible, making it a last resort [[3]](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m). For most use cases, context engineering delivers better results faster and more cheaply. It allows for rapid iteration without altering the core model.

When you start a new AI project, your decision-making process for guiding the LLM should look like the one presented in Image 1. For instance, to process internal Slack messages, you do not need to fine-tune a model. It is more effective to use context engineering to retrieve messages and enable actions. Throughout this course, we will focus on solving problems with this approach.

```mermaid
graph TD
    A["Prompt Engineering"] --> B{"Prompt Engineering<br/>Sufficient?"}
    B -- "No" --> C["Context Engineering"]
    B -- "Yes" --> F["Application Built"]
    C --> D{"Context Engineering<br/>Sufficient?"}
    D -- "No" --> E["Fine-tuning"]
    D -- "Yes" --> F
    E --> F
```

Image 1: A simplified flowchart illustrating the decision-making workflow for building AI applications.

## What Makes Up the Context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model [[4]](https://arxiv.org/pdf/2507.13334).

The high-level workflow begins when a user input triggers the system to pull relevant information from memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats, as shown in Image 2.

```mermaid
flowchart LR
  %% Workflow Start
  UI["User Input"]

  %% Memory Components
  subgraph Memory
    STM["Short-Term Memory"]
    LTM["Long-Term Memory"]
  end

  %% Context and Prompt Generation
  subgraph "Prompt Generation"
    C["Context"]
    PT["Prompt Template"]
    P["Prompt"]
  end

  %% LLM Interaction
  subgraph "LLM Processing"
    LLMC["LLM Call"]
    A["Answer"]
  end

  %% Primary Flow
  UI -- "interacts with" --> STM
  UI -- "interacts with" --> LTM

  STM -- "provides relevant info" --> C
  LTM -- "provides relevant info" --> C

  C -- "fed into" --> PT
  PT -- "forms" --> P
  P -- "sent to" --> LLMC
  LLMC -- "generates" --> A

  %% Feedback Loop
  A -- "processed & stores" --> STM
  A -- "processed & stores" --> LTM
  A -- "leads to new" --> UI
```

Image 2: A simplified flowchart depicting the high-level workflow of an AI application.

These memory components are grouped into two main categories, which we will explain intuitively for now.

**Short-term working memory** is the agent's state for the current task. It is volatile and helps maintain a coherent dialogue. It includes user input, message history, the agent's internal thoughts, and outputs from any actions performed [[5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill), [[6]](https://www.datacamp.com/blog/context-engineering).

**Long-term memory** is persistent and stores information across sessions. We divide it into three types: **procedural memory** (the agent's built-in skills, like its system prompt), **episodic memory** (specific past experiences, like user preferences), and **semantic memory** (the agent’s general knowledge base) [[5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39dce26a-e51e-4167-ac9e-ca28c45b53a6_1115x708.png
Image 3: A detailed illustration of how all the context engineering components work together inside an AI agent. (Source [Decoding AI [5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill))

These components are dynamic and re-computed for every interaction. Context engineering involves selecting the right pieces from this memory pool to construct the most effective prompt.

## Production Implementation Challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that arise when building AI applications:

**The context window challenge** is a primary concern. Every model has a finite context window, which acts like a computer's RAM. This space is a limited and expensive resource, and the self-attention mechanism in LLMs imposes a quadratic computational overhead for every token added [[4]](https://arxiv.org/pdf/2507.13334).

This leads to **information overload**, also known as the "lost-in-the-middle" problem. Research shows that as you add more information, models lose focus on critical details, especially those in the middle of the context [[7]](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e). Performance often degrades long before the physical limit is reached.

Another issue is **context drift**, where conflicting versions of the truth accumulate over time [[8]](https://galileo.ai/blog/production-llm-monitoring-strategies). If memory contains contradictory facts, the agent can get confused, making its knowledge base unreliable.

Finally, there is **tool confusion**. This happens when an agent is given too many tools, or when tool descriptions are poorly written. Models can become paralyzed by choice or pick the wrong tool, leading to failed tasks [[1]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

## Key Strategies for Context Optimization

Modern AI solutions must manage complexity across multiple knowledge bases, tools, and conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements. Here are four popular strategies used across the industry.

**Selecting the right context** is your first line of defense against information overload. Instead of providing all available context, use techniques to filter and prioritize. Use structured outputs to define clear schemas for what the LLM should return. Use RAG to fetch specific text chunks instead of entire documents. For agents, reduce the number of available actions; studies show that limiting the selection to under 30 tools can triple selection accuracy [[9]](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider). Rank time-sensitive data by date, and repeat core instructions at both the start and end of the prompt to leverage the model's attention bias [[10]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2).

```mermaid
flowchart LR
  %% Problem
  A["Information Overload"]

  %% Strategies
  B["Structured Outputs<br/>(clear, concise data)"]
  C["RAG (Retrieval-Augmented Generation)<br/>(relevant external knowledge)"]
  D["Reducing Tool Count<br/>(prevent confusion)"]
  E["Temporal Relevance<br/>(prioritizing recent information)"]
  F["Repeating Core Instructions<br/>(for emphasis)"]

  %% Goal
  G["Optimizing Context Selection"]

  %% Connections
  A -- "addressed by" --> B
  A -- "addressed by" --> C
  A -- "addressed by" --> D
  A -- "addressed by" --> E
  A -- "addressed by" --> F

  B -- "contributes to" --> G
  C -- "contributes to" --> G
  D -- "contributes to" --> G
  E -- "contributes to" --> G
  F -- "contributes to" --> G

  %% Visual grouping
  classDef problem stroke-width:3px
  classDef strategy stroke-width:1px
  classDef goal stroke-width:3px

  class A problem
  class B,C,D,E,F strategy
  class G goal
```

Image 4: A diagram illustrating strategies for selecting the right context to combat information overload.

**Context compression** is necessary as message history grows. You cannot simply drop past turns, so you must compress key facts. This can be done by creating summaries of past interactions, moving user preferences to long-term memory, or using deduplication to remove redundant information [[11]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view).

```mermaid
flowchart LR
    %% Problem statement
    A["Growing Message History"]

    %% Overall Goal/Process
    B["Context Compression"]

    %% Strategies
    subgraph "Context Compression Strategies"
        C["Summarization"]
        D["Moving Preferences to Long-Term Memory"]
        E["Deduplication"]
    end

    %% Examples
    subgraph "Implementation Examples"
        C1["LLM-generated summaries<br/>of older turns"]
        D1["Storing key facts<br/>in vector DBs"]
        E1["Removing redundant information"]
    end

    %% Outcome
    F["Reduced Context Size"]

    A -- "necessitates" --> B
    B -- "employs" --> C
    B -- "employs" --> D
    B -- "employs" --> E

    C -- "e.g." --> C1
    D -- "e.g." --> D1
    E -- "e.g." --> E1

    C1 --> F
    D1 --> F
    E1 --> F

    %% Visual grouping (without custom styling)
    classDef problem
    classDef process
    classDef strategy
    classDef example
    classDef outcome

    class A problem
    class B process
    class C,D,E strategy
    class C1,D1,E1 example
    class F outcome
```

Image 5: A diagram illustrating strategies for context compression.

**Isolating context** involves splitting a complex problem across multiple specialized agents. Instead of one agent with a massive context window, you can have a team of agents, each with a smaller, focused one. This is often implemented using an orchestrator-worker pattern, where a central agent assigns sub-tasks to specialized workers [[12]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production).

```mermaid
flowchart LR
  %% Main Agents
  subgraph "Agent Roles"
    OA["Orchestrator Agent"]
  end

  %% Worker Agents and their context
  subgraph "Worker Agents & Context"
    WA1["Worker Agent 1"]
    OSC1["Own Scoped Context 1"]
    WA2["Worker Agent 2"]
    OSC2["Own Scoped Context 2"]
    WA3["Worker Agent 3"]
    OSC3["Own Scoped Context 3"]
  end

  %% Flow
  CT["Complex Task"] --> OA
  OA -- "delegates subtask" --> WA1
  OA -- "delegates subtask" --> WA2
  OA -- "delegates subtask" --> WA3

  WA1 -- "operates with" --> OSC1
  WA2 -- "operates with" --> OSC2
  WA3 -- "operates with" --> OSC3

  WA1 -- "sends result" --> OA
  WA2 -- "sends result" --> OA
  WA3 -- "sends result" --> OA

  OA -- "synthesizes" --> SR["Synthesized Results"]

  %% Visual grouping
  classDef agent stroke-width:2px
  classDef context stroke-dasharray:3,3
  class OA agent
  class WA1,WA2,WA3 agent
  class OSC1,OSC2,OSC3 context
```

Image 6: A diagram illustrating the Orchestrator-Worker Pattern for Isolating Context.

**Format optimization** is also important, as models are sensitive to structure. Using clear delimiters like XML tags can improve reasoning, and preferring YAML over JSON for structured data can be more token-efficient [[5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

## Here Is an Example

Let's connect the theory with a concrete example. AI systems are already being applied in various domains. In healthcare, an AI assistant can access a patient's history and medical literature to suggest diagnoses. In finance, an agent might integrate with a CRM and market data to offer personalized advice. For project management, an AI can access tools like Slack and task managers to automate updates [[5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

Let's walk through a healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the LLM even sees this query, a context engineering system gets to work:
1.  It retrieves the user's patient history, allergies, and habits from **episodic memory**.
2.  It queries a medical database for non-medicinal headache remedies from **semantic memory**.
3.  It assembles this information, along with the query and conversation history, into a structured prompt.
4.  The prompt is sent to the LLM, which generates a personalized, safe, and relevant recommendation.
5.  The interaction is logged, and new preferences are saved back to memory [[5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

Here’s a simplified example showing how these components might be assembled into a prompt, using XML tags for structure and YAML for data collections:

```
<system_prompt>
You are a helpful and cautious AI healthcare assistant. Your goal is to provide safe, non-medicinal advice. Do not provide medical diagnoses.
</system_prompt>

<patient_history>
{retrieved_patient_history_in_yaml}
</patient_history>

<medical_knowledge>
{retrieved_medical_articles_in_yaml}
</medical_knowledge>

<conversation_history>
{formatted_chat_history}
</conversation_history>

<user_query>
{user_query}
</user_query>
```

To build such a system, you would use a combination of tools. An LLM like Gemini provides the reasoning engine. A framework like LangGraph can orchestrate the workflow. Databases such as PostgreSQL, Qdrant, or Neo4j can serve as long-term memory stores. Observability platforms are essential for debugging these complex interactions.

## Connecting Context Engineering to AI Engineering

Building intuition for context engineering is about knowing how to structure prompts, what information to include, and how to order it for maximum impact.

This skill does not exist in a vacuum. It is a multidisciplinary practice that combines:
1.  **AI Engineering:** Understanding LLMs, RAG, and AI agents.
2.  **Software Engineering:** Building scalable and maintainable systems.
3.  **Data Engineering:** Constructing reliable data pipelines for memory systems.
4.  **Operations (Ops):** Deploying agents on the right infrastructure and automating CI/CD [[5]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. We believe in thinking in systems rather than isolated components, shifting our mindset from developers to architects.

In the next lesson, we will explore structured outputs.

## References

- [1] Iusztin, P. (2025, July 22). Context Engineering: 2025’s #1 Skill in AI. Decoding AI. [https://www.decodingai.com/p/context-engineering-2025s-1-skill](https://www.decodingai.com/p/context-engineering-2025s-1-skill)
- [2] Karpathy, A. (2025, July 2). +1 for "context engineering" over "prompt engineering". X. [https://x.com/karpathy/status/1937902205765607626](https://x.com/karpathy/status/1937902205765607626)
- [3] Panjuta, D. (2025, July 1). Prompt Engineering vs. Context Engineering. LinkedIn. [https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m)
- [4] Mei, L., Yao, J., Ge, Y., et al. (2025, July 17). A Survey of Context Engineering for Large Language Models. arXiv. [https://arxiv.org/pdf/2507.13334](https://arxiv.org/pdf/2507.13334)
- [5] Iusztin, P. (2025, July 22). Context Engineering: 2025’s #1 Skill in AI. Decoding AI Magazine. [https://www.decodingai.com/p/context-engineering-2025s-1-skill](https://www.decodingai.com/p/context-engineering-2025s-1-skill)
- [6] Context Engineering: A Guide With Examples. (2025). DataCamp. [https://www.datacamp.com/blog/context-engineering](https://www.datacamp.com/blog/context-engineering)
- [7] DeJohn, A. (2025, June 28). Lost in the Middle: A Lesson in Failing AI Agents (Backwards). LinkedIn. [https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e)
- [8] Bronsdon, C. (2025, July 18). Seven Strategies to Maintain LLM Reliability Across Diverse Use Cases in Production. Galileo. [https://galileo.ai/blog/production-llm-monitoring-strategies](https://galileo.ai/blog/production-llm-monitoring-strategies)
- [9] Context Engineering - What it is, and techniques to consider. (2025). LlamaIndex. [https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider)
- [10] The 'Lost in the Middle' Problem: Why LLMs ignore the middle of your context window. (2025). dev.to. [https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [11] Context Compression. (2026, January 30). OneUptime. [https://oneuptime.com/blog/post/2026-01-30-context-compression/view](https://oneuptime.com/blog/post/2026-01-30-context-compression/view)
- [12] Multi-Agent Orchestration Patterns for Production. (2025). beam.ai. [https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)