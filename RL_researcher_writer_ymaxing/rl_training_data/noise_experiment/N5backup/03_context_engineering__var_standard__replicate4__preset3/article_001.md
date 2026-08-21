# Lesson 3: Context Engineering

## Introduction: When prompt engineering breaks

AI applications have evolved rapidly. In 2022, we had simple chatbots for question-answering [[28]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/). By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge. 2024 brought us tool-using agents that could perform actions [[29]](https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots/). Now, we are building memory-enabled agents that remember past interactions and build relationships over time [[30]](https://www.dante-ai.com/news/when-did-ai-chatbots-start).

In our last lesson, we explored how to choose between AI agents and LLM workflows when designing a system. As these applications grow more complex, prompt engineering, a practice that once served us well, is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The sheer volume of information an agent might need, such as past conversations, user data, documents, and action descriptions, has grown exponentially. Simply stuffing all this into a prompt is not a viable strategy.

The need for a more systematic approach is the foundation of context engineering. It is the discipline of orchestrating this entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it. This skill is becoming a core foundation for AI engineering, representing the shift from one-shot prompts to building dynamic, stateful systems that perform reliably in production [[7]](https://blog.langchain.com/the-rise-of-context-engineering/).

## From Prompt to Context Engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event. This approach breaks down in stateful applications where context must be preserved and managed across multiple turns.

As a conversation or task progresses, the context grows. Without a strategy to manage this growth, the LLM’s performance degrades. This is **context decay**: the model gets confused by the noise of an ever-expanding history [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). It starts to lose track of the original instructions or key information, leading to hallucinations and misguided answers [[1]](https://atlan.com/know/llm-context-window-limitations/).

Even with large context windows, a physical limit exists for what you can include. Also, on the operational side, every token adds to the cost and latency of an LLM call. This is not a linear relationship; latency often increases superlinearly as the context window expands, quickly making applications unusable [[17]](https://dev.to/gervaisamoah/latency-vs-accuracy-for-llm-apps-how-to-choose-and-how-a-memory-layer-lets-you-win-both-d6g). Simply putting everything into the context creates a slow, expensive, and underperforming system. We will explore these concepts in more detail in upcoming lessons, including memory in Lesson 9 and RAG in Lesson 10.

On a recent project, we learned this the hard way. We were working with a model that supported a two-million-token context window, so we thought, "What could go wrong?" We stuffed everything in: our research, guidelines, examples, and user history. The result was an LLM workflow that took 30 minutes to run and produced low-quality outputs. This naive approach is a recipe for failure in production [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

This is the problem context engineering solves. It addresses these limitations by treating AI applications not as a series of isolated prompts, but as systems that operate through dynamic context. As AI engineers, our job is to keep only what's essential in the context when we pass it to the LLM, making our applications accurate, fast, and cost-effective.

## Understanding Context Engineering

Context engineering is about finding the best way to arrange parts of your application's memory into the context that is passed to an LLM to get the best results [[2]](https://arxiv.org/pdf/2507.13334). It is a solution to an optimization problem where you have to retrieve the right parts of both your short-term and long-term memory to solve a specific task without overwhelming the LLM. For example, when you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies or taste preferences. This precise selection ensures the model receives only the essential information.

Andrej Karpathy offered a great analogy for this: LLMs are like a new kind of operating system, where the model acts as the CPU and its context window functions as the RAM [[56]](https://x.com/karpathy/status/1937902205765607626). Just as an operating system manages what fits into your computer’s limited RAM, context engineering curates what occupies the model’s working memory. This reframes the task from simple prompting to a core engineering discipline focused on managing a scarce resource to optimize performance [[50]](https://www.sundeepteki.org/blog/from-vibe-coding-to-context-engineering-a-blueprint-for-production-grade-genai-systems/).

How does context engineering relate to prompt engineering? It's simple. Prompt engineering is a subset of context engineering [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). You still write effective prompts, but you also design a system that feeds the right context into those prompts. This means understanding not just *how* to phrase a task, but *what* information the model needs to perform optimally. The table below highlights the key differences.

| Dimension | Prompt Engineering | Context Engineering |
| :--- | :--- | :--- |
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Stateless function | Stateful due to memory |
| Focus | How to phrase tasks | What information to provide |

Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible [[28]](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m). Data changes constantly, making fine-tuning a last resort. For most enterprise use cases, you get better results faster and more cheaply with context engineering. It allows for rapid iteration and adaptation to evolving data without altering the core model, a key advantage in dynamic environments. This approach avoids the computational resources and specialized expertise required for retraining, offering a more agile path to reliable AI applications.

When you start a new AI project, your decision-making process for guiding the LLM should look like the one presented in Image 1.

```mermaid
graph TD
    Start["Start"] --> A{"Prompt Engineering<br/>Does it solve the problem?"}
    A -- "Yes" --> End["End"]
    A -- "No" --> C{"Context Engineering<br/>Does it solve the problem?"}
    C -- "Yes" --> End
    C -- "No" --> E{"Fine-tuning<br/>Can you make a fine-tuning dataset?"}
    E -- "Yes" --> End
    E -- "No" --> G["Reframe the problem."]
    G -- End
```

Image 1: A flowchart illustrating the decision-making process for choosing a key strategy to guide an LLM.

For instance, if you build an agent to process internal Slack messages, you do not need to fine-tune a model on your company’s communication style. It is more effective to use a powerful reasoning model and engineer the context to retrieve specific messages and enable actions like creating tasks or drafting emails [[34]](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms). Throughout this course, we will show you how to solve most industry problems using only context engineering.

## What Makes Up the Context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model [[31]](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider). The high-level workflow begins when a user input triggers the system to pull relevant information from both long-term and short-term memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
graph TD
    A[User Input] --> B{Long-Term Memory};
    B --> C{Short-Term Working Memory};
    C --> D[Context Assembly];
    D --> E[Prompt Template];
    E --> F[Prompt];
    F --> G((LLM Call));
    G --> H[Answer];
    H --> C;
    subgraph Memory Update
        H --> I{Short-Term Memory};
        I --> J{Long-Term Memory};
    end
```

Image 2: The high-level workflow of how context is assembled and used in an AI system.

These components are grouped into two main categories. We will explain them intuitively for now, as we have future dedicated lessons for all of them.

**Short-term working memory** is the state of the agent for the current task or conversation. It is volatile and changes with each interaction, helping the agent maintain a coherent dialogue and make immediate decisions. It can include some or all of these components [[6]](https://blog.langchain.com/context-engineering-for-agents/):

*   **User input:** The most recent query or command from the user.
*   **Message history:** The log of the current conversation, allowing the LLM to understand the flow and previous turns.
*   **Agent's internal thoughts:** The reasoning steps the agent takes to decide on its next action.
*   **Action calls and outputs:** The results from any actions the agent has performed, providing information from external systems.

**Long-term memory** is more persistent and stores information across sessions, allowing the AI system to remember things beyond a single conversation. We divide it into three types, drawing parallels from human memory [[69]](https://www.datacamp.com/blog/how-does-llm-memory-work). An AI system can include some or all of them:

*   **Procedural memory:** This is the agent's set of built-in skills, encoded directly in the code. It includes the system prompt, which sets the agent's overall behavior. It also includes the definitions of available actions, which tell the agent what it can do, and schemas for structured outputs, which guide the format of its responses [[68]](https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/).
*   **Episodic memory:** This is memory of specific past experiences, like user preferences or previous interactions. It is used to help the agent personalize its responses based on individual users. We typically store this in vector or graph databases for efficient retrieval [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
*   **Semantic memory:** This is the agent’s general knowledge base. It can be internal, like company documents stored in a data lake, or external, accessed via the internet through API calls or web scraping. This memory provides the factual information the agent needs to answer questions [[48]](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/).

If this seems like a lot, bear with us. We will cover all these concepts in-depth in future lessons, including structured outputs in Lesson 4, actions in Lesson 6, memory in Lesson 9, RAG in Lesson 10, and working with multimodal data in Lesson 11.![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39dce26a-e51e-4167-ac9e-ca28c45b53a6_1115x708.png)

Image 3: A detailed illustration of how all the context engineering components work together inside an AI agent (Source [Decoding AI [16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill)).

The key takeaway is that these components are not static. They are dynamically re-computed for every single interaction. For each conversation turn or new task, the short-term memory grows, or the long-term memory can change. Context engineering involves knowing how to select the right pieces from this vast memory pool to construct the most effective prompt for the task at hand.

## Production Implementation Challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These challenges all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that come up when building AI applications:

1.  **The context window challenge:** Every AI model has a limited context window, the maximum amount of information (tokens) it can process at once. This is similar to your computer's RAM. The memory required for the key-value cache scales with the context length, and latency often increases superlinearly, creating a bottleneck long before the hard limit is reached [[11]](https://www.comet.com/site/blog/context-window/), [[64]](https://www.clarifai.com/blog/llm-inference-optimization/), [[65]](https://towardsai.net/p/machine-learning/the-context-window-paradox-engineering-trade-offs-in-modern-llm-architecture). For example, a 4x increase in context length can lead to a 16x increase in memory usage [[65]](https://towardsai.net/p/machine-learning/the-context-window-paradox-engineering-trade-offs-in-modern-llm-architecture).

2.  **Information overload (Context Rot):** Just because you can fit a lot of information into the context does not mean you should. This is known as the "lost-in-the-middle" problem, where LLMs recall information best at the start and end of the context. Recent research formalizes this as **context rot**: a measurable decay in output quality as input length grows, which affects even frontier models [[53]](https://www.trychroma.com/research/context-rot). This happens because models have a finite “attention budget” that is depleted with every token added to the context, forcing them to spread their focus thin [[45]](https://reinteractive.com/articles/ai-real-world-use-cases/solving-ai-agent-amnesia-context-rot-and-lost-in-the-middle), [[30]](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e), [[18]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2).

3.  **Context drift:** This occurs when conflicting versions of truth accumulate in the memory over time. For example, the memory might contain two conflicting statements: "*My cat is white*" and "*My cat is black*" [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). This is not Schrödinger's Cat quantum physics experiment; it is a data conflict that confuses the LLM. Without a mechanism to resolve these conflicts, the model's responses become unreliable as the knowledge base erodes [[10]](https://www.coforge.com/what-we-know/blog/navigating-the-shifting-sands-understanding-and-mitigating-data-drift-in-llms).

4.  **Tool confusion:** The final challenge is tool confusion, which arises in two main ways. First, adding too many tools to an agent can confuse the LLM about the best one for the job, a problem that often appears with over 100 tools. The Gorilla benchmark shows that nearly all models perform worse when given more than one tool. Second, confusion can occur when tool descriptions are poorly written or overlap. If the distinctions between actions are unclear, even a human would struggle to choose the right one [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

## Key Strategies for Context Optimization

Initially, most AI applications were chatbots over single knowledge bases. Today, modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements.

Here are four popular context engineering strategies used across the industry:

### Selecting the Right Context

Retrieving the right information from memory is a critical first step. A common mistake is to provide everything at once, assuming that models with large context windows can handle it. As we have discussed, the "lost-in-the-middle" problem often leads to poor performance, increased latency, and higher costs.

To solve this, consider these approaches:
*   **Use structured outputs:** Define clear schemas for what the LLM should return. This allows you to pass only the necessary, structured information to downstream steps. We will cover this in detail in Lesson 4.
*   **Use RAG:** Instead of providing entire documents, use RAG to fetch only the specific chunks of text needed to answer a user's question [[38]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view). This is a core topic we will explore in Lesson 10.
*   **Reduce the number of available actions:** Rather than giving an agent access to every available action, delegate action subsets to specialized components, for example, using an orchestrator-worker pattern. Limiting the selection to under 30 tools can significantly improve accuracy, but the ideal number depends on your model and tool design, so evaluation is mandatory [[39]](https://packmind.com/context-engineering-ai-coding/what-is-contextops/).
*   **Rank time-sensitive data:** For time-sensitive information, rank it by date and filter out anything no longer relevant [[12]](https://www.dailydoseofds.com/llmops-crash-course-part-8/).
*   **Repeat core instructions:** For the most important instructions, repeat them at both the start and the end of the prompt. This uses the model's tendency to pay more attention to the context edges, ensuring core instructions are not lost [[43]](https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect).
*   **Cache common queries:** Use semantic caching to store the results of frequent RAG queries. This avoids redundant retrieval and LLM calls, reducing both latency and cost for common questions [[67]](https://redis.io/blog/context-engineering-best-practices-for-an-emerging-discipline/).

```mermaid
graph TD
    subgraph "Context Selection Strategies"
        A[User Query] --> B{Context Selection Engine};

        B --> C["RAG: Retrieve Relevant Documents"];
        B --> D["Tool Selection: Filter to <30 Tools"];
        B --> E["Time Ranking: Rank by Date/Relevance"];

        C --> G[Selected Context];
        D --> G;
        E --> G;
    end

    subgraph "Context Assembly"
        G --> H[Assemble Context];
        H --> I[Add Core Instructions at Start];
        H --> J[Add Core Instructions at End];
        I --> K[Prompt Template];
        J --> K;
        K --> L[Prompt];
    end

    L --> M((LLM Call));
    M --> N[Structured Response];
    N --> O[Update Memory];
    O --> A;
```

Image 4: A workflow showing how context selection strategies can work together to optimize information retrieval and assembly.

### Context Compression

As message history grows in short-term working memory, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns, as the LLM still needs to remember what happened. Instead, you need ways to compress key facts from the past. Frameworks have demonstrated that it is possible to achieve 3–4× compression with a 20–30% reduction in end-to-end latency, while maintaining accuracy [[19]](https://www.emergentmind.com/topics/context-compression-framework).

You can do this through [[38]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view), [[12]](https://www.dailydoseofds.com/llmops-crash-course-part-8/):

1.  **Creating summaries of past interactions:** Use an LLM to replace a long, detailed history with a concise overview.
2.  **Moving user preferences to long-term memory:** Transfer user preferences from working memory to long-term episodic memory. This keeps the working context clean while ensuring preferences are remembered for future sessions.
3.  **Deduplication:** Remove redundant information from the context to avoid repetition.

```mermaid
graph TD
    subgraph "Context Compression"
        A[Long Message History] -- LLM Call --> B(Summarize);
        B --> C[Compressed History];
        A -- LLM Call --> D(Extract Preferences);
        D --> E[Long-Term Episodic Memory];
    end
```

Image 5: Compressing context by summarizing history and extracting preferences to long-term memory.

### Isolating Context

Another powerful strategy is to isolate context by splitting information across multiple agents or LLM workflows. This technique is similar to tool isolation, but it is more general, referring to the whole context. The key idea is that instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context [[54]](https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering).

We often implement this using an orchestrator-worker pattern, where a central orchestrator agent breaks down a problem and assigns sub-tasks to specialized worker agents [[3]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production). Each worker operates in its own isolated context, improving focus and allowing for parallel processing. We will cover this pattern in more detail in Lesson 5.

```mermaid
graph TD
    A[User Request] --> B(Orchestrator Agent);
    B --> C{"Worker Agent 1<br>(Context A)"};
    B --> D{"Worker Agent 2<br>(Context B)"};
    B --> E{"Worker Agent 3<br>(Context C)"};
    C --> F[Results];
    D --> F;
    E --> F;
```

Image 6: The orchestrator-worker pattern isolates context across multiple specialized agents.

### Format Optimizations

Finally, the way you format the context matters. Models are sensitive to structure, and using clear delimiters can improve performance. Common strategies are to:

*   **Use XML tags:** Wrap different pieces of context in XML-like tags (e.g., `<user_query>`, `<documents>`). This helps the model distinguish between different types of information, while making it easier for the engineer to reference context elements within the system prompt [[59]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
*   **Prefer YAML over JSON:** When providing structured data as input, YAML is often more token-efficient than JSON, which helps save space in your context window [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).

You always have to understand what is passed to the LLM. Seeing exactly what occupies your context window at every step is key to mastering context engineering. Usually this is done by properly monitoring your traces, tracking what happens at each step, and understanding what the inputs and outputs are [[21]](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/). As this is a significant step to go from PoC to production, we will have dedicated lessons on this.

## Here Is an Example

Let's connect the theory and strategies discussed earlier with concrete examples. Consider several common real-world scenarios:

*   **Healthcare:** An AI assistant accesses a patient's medical history, current symptoms, and relevant medical literature to provide personalized diagnostic support [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
*   **Financial Services:** AI systems integrate with enterprise tools like Customer Relationship Management (CRM) systems, emails, and calendars, combining real-time market data and client portfolio information to generate tailored financial advice [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
*   **Project Management:** AI systems access enterprise infrastructure like CRMs, Slack, and task managers to automatically understand project requirements, then add and update project tasks [[49]](https://sombrainc.com/blog/ai-context-engineering-guide).
*   **Content Creator Assistant:** An AI agent uses your research, past content, and personality traits to understand what and how to create a given piece of content.
*   **Enterprise Knowledge Management:** AI systems use knowledge graphs to navigate complex relationships within an organization's data. Instead of just retrieving documents, the agent can reason over structured entities like products, customers, and supply chains to answer sophisticated business questions [[35]](https://www.moodys.com/web/en/us/creditview/blog/beyond-prompts-why-enterprise-ai-demands-context-engineering.html).

Let's walk through a specific query to see context engineering in action with the healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the AI attempts to answer, a context engineering system performs several steps:

1.  It retrieves the user's patient history, known allergies, and lifestyle habits from episodic memory [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
2.  It queries a medical database for non-pharmacological headache remedies from semantic memory.
3.  It assembles the key units of information from both memory types into the final context.
4.  It formats this information into a structured prompt and calls the LLM.
5.  Finally, it presents a personalized, context-aware answer to the user.

Here is a simplified Python example showing how you might structure the context and prompt for the LLM, using XML tags to format the different context elements.

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

The key relies on the system around it that brings in the proper context to populate the system prompt [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill). To build such a system, you need a robust tech stack. Here is a potential stack we recommend and will use throughout this course:

*   **LLM:** Gemini as a multimodal, reasoning, and cost-effective LLM API provider.
*   **Orchestration:** LangGraph for defining stateful, agentic workflows [[46]](https://www.scalablepath.com/machine-learning/langgraph).
*   **Databases:** PostgreSQL, MongoDB, Redis, Qdrant, and Neo4j. Often, it is effective to keep it simple, as you can achieve much with only PostgreSQL or MongoDB.
*   **Observability:** Opik or LangSmith for evaluation and trace monitoring [[11]](https://www.comet.com/site/blog/context-window/).

## Connecting Context Engineering to AI Engineering

Context engineering is a discipline that combines intuition with systematic practice. It is about developing the skill to craft effective prompts, select the right information from memory, and arrange context for optimal results. This discipline helps you determine the minimal yet essential information an LLM needs to perform at its best. This is an evolving field with open challenges, such as the 'comprehension-generation asymmetry,' where models understand complex context better than they can generate complex outputs [[63]](https://alphaxiv.org/overview/2507.13334v2).

It's important to understand that context engineering cannot be learned in isolation. It is a complex field that combines [[16]](https://www.decodingai.com/p/context-engineering-2025s-1-skill), [[34]](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms):

1.  **AI Engineering:** Implement practical solutions such as LLM workflows, RAG, AI Agents, and evaluation pipelines.
2.  **Software Engineering (SWE):** Build your AI product with code that is not just functional, but also scalable and maintainable, and design architectures that can grow with your product's needs.
3.  **Data Engineering:** Design data pipelines that feed curated and validated data into the memory layer.
4.  **Operations (Ops):** Deploy agents on the proper infrastructure to ensure they are reproducible, maintainable, observable, and scalable, including automating processes with Continuous Integration/Continuous Deployment (CI/CD) pipelines.

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. In the world of AI, we should all think in systems rather than isolated components, having a mindset shift from developers to architects.

## Conclusion

We have seen that context engineering is a foundational discipline for building reliable and scalable AI applications. It moves beyond simple prompt design to the systematic management of an AI's entire information ecosystem. By mastering techniques for selecting, compressing, isolating, and formatting context, you can overcome the inherent limitations of LLMs and build systems that are accurate, efficient, and truly intelligent.

In the next lesson, we will explore structured outputs, a key technique for ensuring the data flowing out of your LLM is as clean and reliable as the context flowing in. Later, we will build on these concepts to cover actions, memory, and RAG in detail, giving you the complete toolkit to build intelligent, context-aware AI systems.

## References

- [1] https://atlan.com/know/llm-context-window-limitations/
- [2] https://arxiv.org/pdf/2507.13334
- [3] https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- [4] https://bigdataboutique.com/blog/needle-in-haystack-optimizing-retrieval-and-rag-over-long-context-windows-5dfb3c
- [5] https://blog.jetbrains.com/research/2025/12/efficient-context-management/
- [6] https://blog.langchain.com/context-engineering-for-agents/
- [7] https://blog.langchain.com/the-rise-of-context-engineering/
- [8] https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b
- [9] https://www.codecademy.com/article/context-engineering-in-ai
- [10] https://www.coforge.com/what-we-know/blog/navigating-the-shifting-sands-understanding-and-mitigating-data-drift-in-llms
- [11] https://www.comet.com/site/blog/context-window/
- [12] https://www.dailydoseofds.com/llmops-crash-course-part-8/
- [13] https://www.dante-ai.com/news/when-did-ai-chatbots-start
- [14] https://datahub.com/blog/context-window-optimization/
- [15] https://www.datacamp.com/blog/context-engineering
- [16] https://www.decodingai.com/p/context-engineering-2025s-1-skill
- [17] https://dev.to/gervaisamoah/latency-vs-accuracy-for-llm-apps-how-to-choose-and-how-a-memory-layer-lets-you-win-both-d6g
- [18] https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [19] https://www.emergentmind.com/topics/context-compression-framework
- [20] https://galileo.ai/blog/production-llm-monitoring-strategies
- [21] https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/
- [22] https://www.glean.com/perspectives/context-engineering-vs-prompt-engineering-key-differences-explained
- [23] https://gurusup.com/blog/multi-agent-orchestration-guide
- [24] https://www.helicone.ai/blog/how-to-reduce-llm-hallucination
- [25] https://insightfinder.com/blog/hidden-cost-llm-drift-detection/
- [26] https://www.instinctools.com/blog/context-engineering/
- [27] https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/
- [28] https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m
- [29] https://www.linkedin.com/pulse/context-engineering-silent-architecture-behind-every-ai-roychowdhury-lzcec
- [30] https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e
- [31] https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider
- [32] https://medium.com/@sahin.samia/the-common-failure-points-of-llm-rag-systems-and-how-to-overcome-them-926d9090a88f
- [33] https://memgraph.com/blog/prompt-engineering-vs-context-engineering
- [34] https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms
- [35] https://www.moodys.com/web/en/us/creditview/blog/beyond-prompts-why-enterprise-ai-demands-context-engineering.html
- [36] https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/
- [37] https://nlp.elvissaravia.com/p/context-engineering-guide
- [38] https://oneuptime.com/blog/post/2026-01-30-context-compression/view
- [39] https://packmind.com/context-engineering-ai-coding/what-is-contextops/
- [40] https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots
- [41] https://www.pinecone.io/learn/context-engineering/
- [42] https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/
- [43] https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect
- [44] https://redis.io/blog/context-window-overflow/
- [45] https://reinteractive.com/articles/ai-real-world-use-cases/solving-ai-agent-amnesia-context-rot-and-lost-in-the-middle
- [46] https://www.scalablepath.com/machine-learning/langgraph
- [47] https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/
- [48] https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/
- [49] https://sombrainc.com/blog/ai-context-engineering-guide
- [50] https://www.sundeepteki.org/blog/from-vibe-coding-to-context-engineering-a-blueprint-for-production-grade-genai-systems
- [51] https://thenewstack.io/context-rot-enterprise-ai-llms/
- [52] https://towardsdatascience.com/your-1m-context-window-llm-is-less-powerful-than-you-think/
- [53] https://www.trychroma.com/research/context-rot
- [54] https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering
- [55] https://weaviate.io/blog/context-engineering
- [56] https://x.com/karpathy/status/1937902205765607626
- [57] https://x.com/lenadroid/status/1943685060785524824
- [58] https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
- [59] https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [60] https://arxiv.org/html/2510.22101v1
- [61] https://arxiv.org/html/2601.13671v1
- [62] https://www.mdpi.com/2079-9292/13/15/2961
- [63] https://alphaxiv.org/overview/2507.13334v2
- [64] https://www.clarifai.com/blog/llm-inference-optimization/
- [65] https://towardsai.net/p/machine-learning/the-context-window-paradox-engineering-trade-offs-in-modern-llm-architecture
- [66] https://www.morphllm.com/context-rot
- [67] https://redis.io/blog/context-engineering-best-practices-for-an-emerging-discipline/
- [68] https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/
- [69] https://www.datacamp.com/blog/how-does-llm-memory-work
- [70] https://atlan.com/know/working-memory-llms/
</article>