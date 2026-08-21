# Lesson 3: Context Engineering

AI applications have evolved rapidly. In 2022, we had simple chatbots for question-answering. By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge. 2024 brought us tool-using agents that could perform actions. Now, we are building memory-enabled agents that remember past interactions and build relationships over time [[26]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/).

In our last lesson, we explored how to choose between AI agents and LLM workflows when designing a system. As these applications grow more complex, prompt engineering is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The volume of information an agent might need has grown exponentially. Simply stuffing all this into a prompt is not a viable strategy. This is where context engineering comes in. It is the discipline of orchestrating this entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it [[20]](https://blog.langchain.com/the-rise-of-context-engineering/).

## From prompt to context engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event. This approach breaks down in stateful applications where context must be preserved and managed across multiple turns [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

As a conversation or task progresses, the context grows. Without a strategy to manage this growth, the LLM’s performance degrades. This is context decay: the model gets confused by the noise of an ever-expanding history and starts to lose track of key information [[3]](https://www.trychroma.com/research/context-rot).

Even with large context windows, a physical limit exists. Also, every token adds to the cost and latency of an LLM call. Simply putting everything into the context creates a slow, expensive, and underperforming system. We will explore these concepts in more detail in future lessons.

On a recent project, we learned this the hard way. We stuffed everything into the context: research, guidelines, examples, and reviews. The result? A 30-minute run time. It was unusable. This naive approach is a recipe for failure in production [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). Context engineering shifts the focus from crafting static prompts to building dynamic systems that manage information flow.

## Understanding context engineering

Context engineering is an optimization problem: finding the ideal way to assemble a context that maximizes the quality of the LLM's output for a given task [[22]](https://arxiv.org/pdf/2507.13334). To put it simply, it is about strategically filling the model’s limited context window with the right information, at the right time, and in the right format. When you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies.

Andrej Karpathy offered a great analogy: LLMs are like a new kind of operating system, where the model acts as the CPU and its context window functions as the RAM [[23]](https://x.com/karpathy/status/1937902205765607626). Just as an operating system manages what fits into RAM, context engineering curates what occupies the model’s working memory.

Prompt engineering is a subset of context engineering. You still need to write good prompts, but you also design a system that gathers the right context to feed into them [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

| Dimension | Prompt Engineering | Context Engineering |
| --- | --- | --- |
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Primarily stateless | Inherently stateful, with explicit memory management |
| Focus | How to phrase tasks | What information to provide |

Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive and inflexible. For most enterprise use cases, you get better results faster and more cheaply with context engineering [[51]](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m). When you start a new AI project, your decision-making process for guiding the LLM should look like the one in Image 1. For instance, to process internal Slack messages, you do not need to fine-tune a model. It is more effective to use context engineering to retrieve specific messages and enable actions. Throughout this course, we will show you how to solve most industry problems using only this approach.

```mermaid
graph TD
    start["Start"] --> prompt_eng["Prompt Engineering"]
    prompt_eng --> prompt_insufficient{"Prompt Engineering Insufficient?"}
    prompt_insufficient -- "No" --> end["Application Built"]
    prompt_insufficient -- "Yes" --> context_eng["Context Engineering"]
    context_eng --> context_insufficient{"Context Engineering Insufficient?"}
    context_insufficient -- "No" --> end
    context_insufficient -- "Yes" --> fine_tuning["Fine-tuning"]
    fine_tuning --> end
```
Image 1: A simplified flowchart illustrating the decision-making workflow for building AI applications.

## What makes up the context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components. The high-level workflow, as presented in Image 2, begins when user input triggers the system to pull information from memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
flowchart LR
  %% Start of the workflow
  UI["User Input"]

  %% Agent Memory components
  subgraph Memory["Agent Memory"]
    STM["Short-Term Memory"]
    LTM["Long-Term Memory"]
  end

  %% Prompt Generation components
  subgraph PromptGeneration["Prompt Generation"]
    CTX["Context"]
    PT["Prompt Template"]
    P["Prompt"]
  end

  %% LLM Interaction components
  subgraph LLMInteraction["LLM Interaction"]
    LLMC["LLM Call"]
    ANS["Answer"]
  end

  %% Primary data flows
  UI -- "provides" --> STM
  UI -- "accesses" --> LTM

  STM -- "informs" --> CTX
  LTM -- "retrieves" --> CTX

  CTX -- "fills" --> PT
  PT -- "generates" --> P

  P -- "sends" --> LLMC
  LLMC -- "produces" --> ANS

  ANS -- "stores" --> STM
  ANS -- "updates" --> LTM
  ANS -- "presents" --> UI

  %% Visual grouping
  classDef store stroke-dasharray:3,3
  classDef process stroke-width:2px

  class STM,LTM store
  class UI,CTX,PT,P,LLMC,ANS process
```
Image 2: A simplified flowchart depicting the high-level workflow of an AI application.

These components are grouped into two main categories, which we will cover in-depth in future lessons.

**Short-term working memory** is the state of the agent for the current task. It is volatile and helps the agent maintain a coherent dialogue. It includes the user input, message history, agent's internal thoughts, and outputs from any actions performed [[31]](https://www.langchain.com/blog/context-engineering-for-agents).

**Long-term memory** is more persistent and stores information across sessions. We divide it into three types, drawing parallels from human memory [[37]](https://www.datacamp.com/blog/how-does-llm-memory-work):
*   **Procedural memory:** This is knowledge encoded in the code, like the system prompt that sets the agent's behavior and the definitions of available actions.
*   **Episodic memory:** This is memory of specific past experiences, like user preferences or previous interactions, often stored in vector or graph databases for personalization.
*   **Semantic memory:** This is the agent’s general knowledge base, such as company documents or external data accessed via APIs. This is the core of RAG.

https://substackcdn.com/image/fetch/$s_!hR60!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39dce26a-e51e-4167-ac9e-ca28c45b53a6_1115x708.png
Image 3: An illustration of how context engineering components work together inside an AI agent. (Source [Decoding AI Magazine](https://www.decodingai.com/p/context-engineering-2025s-1-skill) [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill))

The key takeaway is that these components are dynamic. For each interaction, the memory can change. Context engineering involves selecting the right pieces from this memory pool to construct the most effective prompt.

## Production implementation challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These all revolve around a single question: "How can I keep my context as small as possible while providing enough information to the LLM?"

Here are four common issues that come up when building AI applications:

1.  **The context window challenge:** Every model has a limited context window, the maximum amount of information it can process at once. Think of it like your computer's RAM. While context windows are getting larger, they are not infinite, and treating them as such leads to other problems [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
2.  **Information overload:** Just because you can fit a lot of information into the context does not mean you should. Too much context confuses the model. This is the "lost-in-the-middle" problem, where models remember information best at the beginning and end of the context. Information in the middle is often overlooked, and performance can drop long before the limit is reached [[56]](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e).
3.  **Context drift:** This occurs when conflicting versions of the truth accumulate in the memory over time. For example, the memory might contain both "The user's budget is $500" and later "The user's budget is $1,000," which can confuse the agent [[6]](https://galileo.ai/blog/production-llm-monitoring-strategies).
4.  **Tool confusion:** This arises when an agent is given too many tools, especially with poorly written descriptions or overlapping functionalities. The agent gets paralyzed by choice or picks the wrong tool, leading to failed tasks [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

## Key strategies for context optimization

Modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements. Here are four popular strategies.

### Selecting the Right Context

Retrieving the right information is a critical first step. A common mistake is to provide everything at once. To solve this, use structured outputs, RAG, and reduce the number of available actions. For time-sensitive information, rank it by date. For the most important instructions, repeat them at both the start and the end of the prompt to ensure they are not lost [[57]](https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect).

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

### Context Compression

As message history grows, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns. Instead, you need to compress key facts. You can do this by creating summaries of past interactions, moving user preferences to long-term memory, or using deduplication to remove redundant information [[11]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view).

```mermaid
flowchart LR
  %% Problem
  A["Growing Message History"]

  %% Goal/Process
  B["Context Compression"]

  %% Solutions
  subgraph "Strategies"
    C["Summarization"]
    C_ex["LLM-generated summaries<br/>of older turns"]
    D["Moving Preferences to<br/>Long-Term Memory"]
    D_ex["storing key facts<br/>in vector DBs"]
    E["Deduplication"]
    E_ex["removing redundant information"]
  end

  %% Relationships
  A -- "necessitates" --> B
  B -- "applies" --> C
  B -- "applies" --> D
  B -- "applies" --> E

  C -- "e.g." --> C_ex
  D -- "e.g." --> D_ex
  E -- "e.g." --> E_ex
```
Image 5: A diagram illustrating strategies for Context Compression.

### Isolating Context

Another powerful strategy is to isolate context by splitting information across multiple agents. Instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context. We often implement this using an orchestrator-worker pattern, where a central agent breaks down a problem and assigns sub-tasks to specialized workers [[46]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production).

```mermaid
flowchart LR
  %% Input
  CT["Complex Task"]

  %% Orchestrator
  subgraph Orchestration["Orchestration Layer"]
    OA["Orchestrator Agent"]
  end

  %% Worker Agents and their contexts
  subgraph WorkerPool["Worker Agents & Contexts"]
    WA["Worker Agent"]
    OSC["Own Scoped Context"]
  end

  %% Flow
  CT -- "receives" --> OA
  OA -- "delegates subtasks" --> WA
  WA -- "operates with" --> OSC
  WA -- "returns subtask results" --> OA
  OA -- "collects & synthesizes results" --> FR["Final Result"]

  %% Visual grouping
  classDef agent stroke-width:2px
  classDef context stroke-dasharray:3,3
  class OA agent
  class WA agent
  class OSC context
```
Image 6: A simplified diagram illustrating the Orchestrator-Worker Pattern for Isolating Context.

### Format Optimization

Finally, the way you format the context matters. Models are sensitive to structure. Using clear delimiters like XML tags can improve performance. When providing structured data, YAML is often more token-efficient than JSON, which helps save space [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). Seeing exactly what occupies your context window at every step is key to mastering context engineering, which is why monitoring your application is so important.

## Here is an example

Let's connect theory with a concrete example. Consider these real-world scenarios:
*   **Healthcare:** An AI assistant accesses a patient's medical history and the latest medical literature to provide personalized diagnostic support [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
*   **Financial Services:** AI systems integrate with CRMs and real-time market data to generate tailored financial advice [[25]](https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models).
*   **Project Management:** AI systems access enterprise tools like Slack and task managers to automatically understand and update project tasks.

Let's walk through the healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the AI answers, a context engineering system gets to work:
1.  It retrieves the user's patient history and preferences from episodic memory.
2.  It queries a medical database for non-medicinal headache remedies from semantic memory.
3.  It assembles this information into a structured prompt.
4.  It calls the LLM, which generates a personalized recommendation.
5.  It logs the interaction and saves any new preferences back to memory.

Here is a simplified snippet showing how the final context sent to the LLM might be structured, using XML for clarity and YAML for data efficiency.

```xml
<system_prompt>
You are a helpful and cautious AI healthcare assistant...
</system_prompt>

<patient_history>
patient:
  name: John Doe
  age: 45
  preferences:
    medication_avoidance: true
  habits:
    stress_level: high
</patient_history>

<medical_knowledge>
articles:
  - topic: dehydration_headaches
    finding: "Dehydration is a common cause..."
  - topic: stress_relief
    finding: "Stress-relief techniques are effective..."
</medical_knowledge>

<user_query>
I have a headache. What can I do to stop it? I would prefer not to take any medicine.
</user_query>
```

To build such a system, you would use a combination of tools. An LLM like Gemini provides the reasoning. A framework like LangGraph orchestrates the workflow. Databases such as PostgreSQL or Qdrant serve as long-term memory, and observability platforms are essential for debugging [[62]](https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b).

## Connecting context engineering to AI engineering

Mastering context engineering is less about learning a specific algorithm and more about building intuition. It is the art of knowing how to structure prompts, what information to include, and how to order it for maximum impact.

This skill does not exist in a vacuum. It is a multidisciplinary practice that sits at the intersection of several key engineering fields [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill):
1.  **AI Engineering:** Understanding LLMs, RAG, and AI agents is the foundation.
2.  **Software Engineering:** You need to build scalable and maintainable systems to aggregate context.
3.  **Data Engineering:** Constructing reliable data pipelines for memory systems is critical.
4.  **Operations:** Deploying agents on the right infrastructure makes them reproducible and observable.

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. In the next lesson, we will explore structured outputs, a key technique for controlling what comes *out* of an LLM.

## References

- [1] The LangChain Team. (2025, July 2). Context Engineering. LangChain Blog. https://blog.langchain.com/context-engineering-for-agents/
- [2] LlamaIndex. (n.d.). Context Engineering - What it is, and techniques to consider. https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider
- [3] Hong, K., Troynikov, A., & Huber, J. (2025, July). Context Rot: How Increasing Input Tokens Impacts LLM Performance. Chroma. https://www.trychroma.com/research/context-rot
- [6] Bronsdon, C. (2025, July 18). Seven Strategies to Maintain LLM Reliability Across Diverse Use Cases in Production. Galileo. https://galileo.ai/blog/production-llm-monitoring-strategies
- [11] OneUptime. (2026, January 30). Context Compression: A Deep Dive into Advanced Techniques for LLM Applications. https://oneuptime.com/blog/post/2026-01-30-context-compression/view
- [20] Chase, H. (2025, June 23). The rise of "context engineering". LangChain Blog. https://blog.langchain.com/the-rise-of-context-engineering/
- [21] DataCamp. (n.d.). Context Engineering: A Guide With Examples. https://www.datacamp.com/blog/context-engineering
- [22] Mei, L., Yao, J., Ge, Y., Wang, Y., Bi, B., Cai, Y., Liu, J., Li, M., Li, Z., Zhang, D., Zhou, C., Mao, J., Xia, T., Guo, J., & Liu, S. (2025, July 17). A survey of context engineering for large language models. arXiv. https://arxiv.org/pdf/2507.13334
- [23] karpathy. (n.d.). X. https://x.com/karpathy/status/1937902205765607626
- [24] lenadroid. (n.d.). X. https://x.com/lenadroid/status/1943685060785524824
- [25] Glean. (n.d.). Context engineering AI: The foundation of reliable, high-performing models. https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models
- [26] Security Industry Association. (2024, July 16). Understanding the Evolution from Classic Chatbots to RAG Chatbots to AI-Powered Assistants. https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/
- [31] The LangChain Team. (2025, July 2). Context Engineering. LangChain Blog. https://blog.langchain.com/context-engineering-for-agents/
- [37] DataCamp. (n.d.). How Does LLM Memory Work?. https://www.datacamp.com/blog/how-does-llm-memory-work
- [41] Iusztin, P. (2025). Context Engineering: 2025’s #1 Skill in AI. Decoding AI Magazine. https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [46] Beam.ai. (n.d.). Multi-Agent Orchestration Patterns for Production. https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- [51] Panjuta, D. (2024, June). Prompt Engineering vs Context Engineering. LinkedIn. https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m
- [56] DeJohn, A. (2025, June). Lost in the Middle: A Lesson in Failing AI Agents (Backwards). LinkedIn. https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e
- [57] Promptmetheus. (n.d.). Lost-in-the-Middle Effect. https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect
- [62] Stackademic. (n.d.). Context Engineering in LLMs and AI Agents. https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b