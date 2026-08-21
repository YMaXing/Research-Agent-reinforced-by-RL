# Context Engineering: 2025’s #1 Skill in AI

AI applications have evolved rapidly. In 2022, we had simple chatbots for question-answering [[26]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/). By 2023, Retrieval-Augmented Generation (RAG) systems connected LLMs to domain-specific knowledge [[26]](https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/). 2024 brought us tool-using agents that could perform actions [[27]](https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots). Now, we are building memory-enabled agents that remember past interactions and build relationships over time.

In our last lesson, we explored how to choose between AI agents and LLM workflows when designing a system. As these applications grow more complex, prompt engineering, a practice that once served us well, is showing its limits. It optimizes single LLM calls but fails when managing systems with memory, actions, and long interaction histories. The sheer volume of information an agent might need—past conversations, user data, documents, and action descriptions—has grown exponentially. Simply stuffing all this into a prompt is not a viable strategy.

This is where context engineering comes in. It is the discipline of orchestrating this entire information ecosystem to ensure the LLM gets exactly what it needs, when it needs it. This skill is becoming a core foundation for AI engineering.

## From prompt to context engineering

Prompt engineering, while effective for simple tasks, is designed for single, stateless interactions. It treats each call to an LLM as a new, isolated event. This approach breaks down in stateful applications where context must be preserved and managed across multiple turns.

As a conversation or task progresses, the context grows. Without a strategy to manage this growth, the LLM’s performance degrades. This is context decay: the model gets confused by the noise of an ever-expanding history. It starts to lose track of the original instructions or key information. A recent study found that model correctness can start dropping significantly once the context exceeds 32,000 tokens, long before advertised limits are reached.

Even with large context windows, there's a physical limit to what you can include. On the operational side, every token adds to the cost and latency of an LLM call. Simply putting everything into the context creates a slow, expensive, and underperforming system. We will explore these concepts in more detail in upcoming lessons, including memory in Lesson 9 and RAG in Lesson 10.

On a recent project, we learned this the hard way. We were working with a model that supported a one-million-token context window, so we thought, "*What could go wrong?*" We stuffed everything in: our research, guidelines, examples, and user history. The result was an LLM workflow that took 30 minutes to run and produced low-quality outputs.

This is where context engineering becomes essential. It shifts the focus from crafting static prompts to building dynamic systems that manage information flow. As an AI engineer, your job is to select only the most critical pieces of context for each LLM call. This makes your applications accurate, fast, and cost-effective.

## Understanding context engineering

Context engineering is about finding the best way to arrange parts of your memory into the context that's passed to an LLM to squeeze out the best results. It's a solution to an optimization problem where you retrieve the right parts of both your short-term and long-term memory to solve a specific task without overwhelming the LLM [[22]](https://arxiv.org/pdf/2507.13334). For example, when you ask a cooking agent for a recipe, you do not give it the entire cookbook. Instead, you retrieve the specific recipe, along with personal context like allergies or taste preferences. This precise selection ensures the model receives only the essential information.

Andrej Karpathy offered a great analogy for this: LLMs are like a new kind of operating system, where the model acts as the CPU and its context window functions as the RAM [[31]](https://www.langchain.com/blog/context-engineering-for-agents), [[1]](https://x.com/karpathy/status/1937902205765607626). Just as an operating system manages what fits into RAM, context engineering curates what occupies the model’s working memory. It is important to note that the context is a subset of the system's total working memory; you can hold information without passing it to the LLM on every turn.

Context engineering is not replacing prompt engineering. Instead, prompt engineering is a subset of context engineering [[20]](https://blog.langchain.com/the-rise-of-context-engineering/). You still work with prompts, so learning how to write them effectively is still a critical skill. But on top of that, it's important to know how to incorporate the right context into the prompt without compromising the LLM's performance.

| Dimension | Prompt Engineering | Context Engineering |
| --- | --- | --- |
| Scope | Single interaction optimization | Entire information ecosystem |
| State Management | Stateless function | Stateful due to memory |
| Focus | How to phrase tasks | What information to provide |

Table 1: A comparison of prompt engineering and context engineering.

Context engineering is the new fine-tuning. While fine-tuning has its place, it is expensive, time-consuming, and inflexible. For most enterprise use cases, you get better results faster and more cheaply with context engineering [[53]](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms). It allows for rapid iteration and adaptation to evolving data without altering the core model. Fine-tuning should always be the last resort if nothing else works [[51]](https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m).

When you start a new AI project, your decision-making process for guiding the LLM should look like this:

```mermaid
graph TD
    PE["Prompt Engineering"] --> D1{"Does it solve the problem?"}
    D1 -- "Yes" --> S1["Stop"]
    D1 -- "No" --> CE["Context Engineering"]
    CE --> D2{"Does it solve the problem?"}
    D2 -- "Yes" --> S2["Stop"]
    D2 -- "No" --> FT["Fine-tuning"]
    FT --> D3{"Can you make a fine-tuning dataset?"}
    D3 -- "Yes" --> S3["Stop"]
    D3 -- "No" --> RP["Reframe the problem."]
```
Image 1: A flowchart illustrating the decision-making workflow for choosing a key strategy when starting a new AI project.

Suppose you build an agent to process internal Slack messages. You do not need to fine-tune a model on your company’s communication style. It is more effective to use a powerful reasoning model and engineer the context to retrieve specific messages and enable actions like creating tasks or drafting emails. Throughout this course, we will show you how to solve most industry problems using only context engineering.

## What makes up the context

To master context engineering, you first need to understand what "context" actually is. It is everything the LLM sees in a single turn, dynamically assembled from various memory components before being passed to the model [[19]](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider).

The high-level workflow begins when a user input triggers the system to pull relevant information from both long-term and short-term memory. This information is assembled into the final context, inserted into a prompt template, and sent to the LLM. The LLM’s answer then updates the memory, and the cycle repeats.

```mermaid
flowchart LR
  %% User interaction
  User_Input["User Input"]

  %% Memory components
  subgraph Memory["Memory Management"]
    LTM["Long-term Memory"]
    STM["Short-Term Working Memory"]
  end

  %% Context assembly
  subgraph Context_Assembly["Context Assembly"]
    Context["Context"]
    Prompt_Template["Prompt Template"]
    Prompt["Prompt"]
  end

  %% LLM Interaction
  subgraph LLM_Interaction["LLM Interaction"]
    LLM_Call["LLM Call"]
    Answer["Answer"]
  end

  %% Flow
  User_Input -- "initiates query" --> LTM
  LTM -- "retrieves relevant info" --> STM
  STM -- "assembles current context" --> Context
  Context -- "fills" --> Prompt_Template
  Prompt_Template -- "generates" --> Prompt
  Prompt -- "sends to" --> LLM_Call
  LLM_Call -- "produces" --> Answer

  %% Memory updates and loop back
  Answer -- "updates" --> STM
  Answer -- "persists" --> LTM

  STM -- "ready for next cycle" --> Repeat["Repeat"]
  LTM -- "informs next cycle" --> Repeat
  Repeat -- "new interaction" --> User_Input

  %% Visual differentiation
  classDef memory_store stroke-dasharray:3,3
  classDef process_step stroke-width:2px
  class LTM,STM memory_store
  class User_Input,Context,Prompt_Template,Prompt,LLM_Call,Answer,Repeat process_step
```
Image 2: A flowchart illustrating the high-level workflow of how context is built and used in an LLM application, including memory updates and a loop for subsequent interactions.

These components are grouped into two main categories. We will explain them intuitively for now, as we have future dedicated lessons for all of them.

### Short-Term Working Memory

Short-term working memory is the state of the agent for the current task or conversation. It is volatile and changes with each interaction, helping the agent maintain a coherent dialogue and make immediate decisions. It can include some or all of these components [[36]](https://atlan.com/know/working-memory-llms/):

-   **User input:** The most recent query or command from the user.
-   **Message history:** The log of the current conversation, allowing the LLM to understand the flow and previous turns.
-   **Agent's internal thoughts:** The reasoning steps the agent takes to decide on its next action.
-   **Action calls and outputs:** The results from any actions the agent has performed, providing information from external systems.

### Long-Term Memory

Long-term memory is more persistent and stores information across sessions, allowing the AI system to remember things beyond a single conversation. We divide it into three types, drawing parallels from human memory [[37]](https://www.datacamp.com/blog/how-does-llm-memory-work). An AI system can include some or all of them:

-   **Procedural memory:** This is knowledge encoded directly in the code. It includes the system prompt, which sets the agent's overall behavior. It also includes the definitions of available actions, which tell the agent what it can do, and schemas for structured outputs, which guide the format of its responses. Think of this as the agent's built-in skills [[39]](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/).
-   **Episodic memory:** This is memory of specific past experiences, like user preferences or previous interactions. It's used to help the agent personalize its responses based on individual users. We typically store this in vector or graph databases for efficient retrieval.
-   **Semantic memory:** This is the agent’s general knowledge base. It can be internal, like company documents stored in a data lake, or external, accessed via the internet through API calls or web scraping. This memory provides the factual information the agent needs to answer questions.

If this seems like a lot, bear with us. We will cover all these concepts in-depth in future lessons, including structured outputs (Lesson 4), actions (Lesson 6), memory (Lesson 9), RAG (Lesson 10), and working with multimodal data (Lesson 11).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39dce26a-e51e-4167-ac9e-ca28c45b53a6_1115x708.png 
Image 3: What makes up the context. (Source [Decoding AI Magazine](https://www.decodingai.com/p/context-engineering-2025s-1-skill))

The key takeaway is that these components are not static. They are dynamically re-computed for every single interaction. For each conversation turn or new task, the short-term memory grows, or the long-term memory can change. Context engineering involves knowing how to select the right pieces from this vast memory pool to construct the most effective prompt for the task at hand.

## Production implementation challenges

Now that we understand what makes up the context, let's look at the core challenges of implementing it in production. These challenges all revolve around a single question: *"How can I keep my context as small as possible while providing enough information to the LLM?"*

Here are four common issues that come up when building AI applications:

1.  **The context window challenge:** Every AI model has a limited context window, the maximum amount of information (tokens) it can process at once. Think of it like your computer's RAM. If your machine has only 32GB of RAM, that is all it can use at one time [[16]](https://www.comet.com/site/blog/context-window/). While context windows are getting larger, they are not infinite, and treating them as such leads to other problems. Enterprise queries can consume 50,000 to 100,000 tokens before the model even starts reasoning [[59]](https://atlan.com/know/llm-context-window-limitations/).
2.  **Information overload:** Just because you can fit a lot of information into the context does not mean you should. Too much context reduces the performance of the LLM by confusing it. This is known as the "lost-in-the-middle" or "needle in the haystack" problem, where LLMs are known for remembering information best at the beginning and end of the context window [[56]](https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e). Information in the middle is often overlooked, and performance can drop long before the physical context limit is reached. Research shows accuracy can drop by over 30% for information in the middle of the context [[59]](https://atlan.com/know/llm-context-window-limitations/).
3.  **Context drift:** This occurs when conflicting versions of the truth accumulate in the memory over time [[6]](https://galileo.ai/blog/production-llm-monitoring-strategies). For example, the memory might contain two conflicting statements: "*My cat is white*" and "*My cat is black*." This is not Schrodinger's Cat quantum physics experiment; it is a data conflict that confuses the LLM. Without a mechanism to resolve these conflicts, the model's responses become unreliable [[8]](https://thenewstack.io/context-rot-enterprise-ai-llms/).
4.  **Tool confusion:** The final challenge is tool confusion, which arises in two main ways. First, adding too many actions to an agent can confuse the LLM about the best one for the job, a problem that often appears with over 100 actions. Second, confusion can occur when tool descriptions are poorly written or overlap. If the distinctions between actions are unclear, even a human would struggle to choose the right one. The Gorilla benchmark shows that nearly all models perform worse when given more than one tool.

## Key strategies for context optimization

Initially, most AI applications were chatbots over single knowledge bases. Today, modern AI solutions must manage multiple knowledge bases, tools, and complex conversational histories. Context engineering is about managing this complexity while meeting performance, latency, and cost requirements.

Here are four popular context engineering strategies used across the industry:

### Selecting the right context

Retrieving the right information from memory is a critical first step. A common mistake is to provide everything at once, assuming that models with large context windows can handle it. As we've discussed, the "lost-in-the-middle" problem often leads to poor performance, increased latency, and higher costs. To solve this, consider these approaches:

-   **Use structured outputs:** Define clear schemas for what the LLM should return. This allows you to pass only the necessary, structured information to downstream steps. We will cover this in detail in Lesson 4.
-   **Use RAG:** Instead of providing entire documents, use RAG to fetch only the specific chunks of text needed to answer a user's question. This is a core topic we will explore in Lesson 10.
-   **Reduce the number of available tools:** Rather than giving an agent access to every available action, use various strategies to delegate action subsets to specialized components. Studies show that limiting the selection to under 30 tools can triple the agent's selection accuracy [[21]](https://www.datacamp.com/blog/context-engineering). Still, the ideal number of tools an agent can use can be highly dependent on what tools you provide, what LLM you use, and how well the actions are defined.
-   **Rank time-sensitive data:** For time-sensitive information, rank it by date and filter out anything no longer relevant.
-   **Repeat core instructions:** For the most important instructions, repeat them at both the start and the end of the prompt. This uses the model's tendency to pay more attention to the context edges, ensuring core instructions are not lost [[57]](https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect).

```mermaid
flowchart LR
  %% System Entry
  Input["User Query / Initial Context"]

  %% Context Optimization Layer
  subgraph "Context Optimization Layer"
    RAG["Retrieval Augmented Generation<br/>(RAG)"]
    TR["Temporal Relevance<br/>(Context Filtering)"]
    RT["Reducing Tools<br/>(Tool Selection)"]
    SO["Structured Outputs<br/>(Context Formatting)"]
    RCI["Repeating Core Instructions<br/>(Instruction Reinforcement)"]
  end

  %% LLM Processing & Output
  LLM["Large Language Model"]
  Output["AI System Response / Action"]

  %% Primary Flow
  Input -- "initial context" --> RAG
  RAG -- "retrieved data" --> TR
  Input -- "current context" --> TR
  TR -- "time-optimized context" --> RT
  Input -- "available tools" --> RT
  RT -- "context + selected tools" --> SO
  SO -- "structured input" --> RCI
  RCI -- "final LLM context" --> LLM
  LLM -- "generates" --> Output

  %% Indirect / Supporting Relationships
  Input -. "guides RAG query" .-> RAG
  Input -. "informs temporal window" .-> TR
  Input -. "influences tool relevance" .-> RT
```
Image 4: A flowchart illustrating how various context selection techniques are combined and orchestrated within an AI system for context optimization.

### Context compression

As message history grows in short-term working memory, you must manage past interactions to keep your context window in check. You cannot simply drop past conversation turns, as the LLM still needs to remember what happened. Instead, you need ways to compress key facts from the past. You can do this through:

-   **Creating summaries of past interactions:** Use an LLM to replace a long, detailed history with a concise overview [[12]](https://www.dailydoseofds.com/llmops-crash-course-part-8/).
-   **Moving user preferences to long-term memory:** Transfer user preferences from working memory to long-term episodic memory. This keeps the working context clean while ensuring preferences are remembered for future sessions.
-   **Deduplication:** Remove redundant information from the context to avoid repetition, using techniques like MinHash or semantic clustering [[11]](https://oneuptime.com/blog/post/2026-01-30-context-compression/view).

```mermaid
flowchart LR
  %% Input Sources
  subgraph "Input Sources"
    PI["Past Interactions"]
    UPWM["User Preferences<br/>(Working Memory)"]
  end

  %% Compression Strategies
  subgraph "Compression Strategies"
    SUM["Summarization Process"]
    PE["Preference Extraction<br/>& Storage"]
    DEDUP["Deduplication Techniques"]
  end

  %% Memory Management
  subgraph "Memory Management"
    ELTM["Episodic Long-Term Memory"]
    STM["Short-Term Memory<br/>(Context Window)"]
  end

  %% LLM Interaction
  subgraph "LLM Interaction"
    LLMC["LLM Call"]
  end

  %% Primary data flows
  PI -- "generates summary" --> SUM
  UPWM -- "extracts & moves" --> PE
  PE -- "stores" --> ELTM
  ELTM -- "retrieves relevant" --> STM
  SUM -- "adds summarized context to" --> STM
  STM -- "undergoes" --> DEDUP
  DEDUP -- "provides compressed context for" --> LLMC

  %% Visual grouping
  classDef source stroke-dasharray:5,5
  classDef process stroke-width:2px
  classDef memory stroke-dasharray:3,3
  classDef output stroke-width:3px

  class PI,UPWM source
  class SUM,PE,DEDUP process
  class ELTM,STM memory
  class LLMC output
```
Image 5: A flowchart illustrating context compression strategies for LLMs.

### Isolating context

Another powerful strategy is to isolate context by splitting information across multiple agents or LLM workflows. This technique is similar to tool isolation, but it's more general, referring to the whole context. The key idea is that instead of one agent with a massive, cluttered context window, you can have a team of agents, each with a smaller, focused context [[48]](https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering). We often implement this using an orchestrator-worker pattern, where a central orchestrator agent breaks down a problem and assigns sub-tasks to specialized worker agents [[46]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production). Each worker operates in its own isolated context, improving focus and allowing for parallel processing. We will cover this pattern in more detail in Lesson 5.

```mermaid
flowchart LR
  %% Orchestrator
  subgraph "Orchestrator"
    O["Orchestrator Agent<br/>(Complex Problem Splitter)"]
  end

  %% Worker Agents and their contexts
  subgraph "Specialized Worker Agents"
    W1["Worker Agent 1<br/>(Subtask A)"]
    C1["Focused Context Window<br/>(Worker 1)"]
    W2["Worker Agent 2<br/>(Subtask B)"]
    C2["Focused Context Window<br/>(Worker 2)"]
    W3["Worker Agent 3<br/>(Subtask C)"]
    C3["Focused Context Window<br/>(Worker 3)"]
  end

  %% Primary flows
  O -- "delegates subtask A" --> W1
  O -- "delegates subtask B" --> W2
  O -- "delegates subtask C" --> W3

  W1 -- "uses focused context" --> C1
  W2 -- "uses focused context" --> C2
  W3 -- "uses focused context" --> C3

  W1 -- "returns result A" --> O
  W2 -- "returns result B" --> O
  W3 -- "returns result C" --> O

  %% Visual grouping
  classDef orchestrator stroke-width:2px
  classDef worker stroke-width:1.5px
  classDef context stroke-dasharray:3,3

  class O orchestrator
  class W1,W2,W3 worker
  class C1,C2,C3 context
```
Image 6: A flowchart illustrating the orchestrator-worker pattern for context isolation, showing a central orchestrator delegating subtasks to specialized worker agents, each with its own focused context window.

### Format optimization

Finally, the way you format the context matters. Models are sensitive to structure, and using clear delimiters can improve performance. Common strategies are to use XML tags to wrap different pieces of context (e.g., `<user_query>`, `<documents>`) [[44]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). This helps the model distinguish between different types of information. Also, when providing structured data as input, YAML is often more token-efficient than JSON, which helps save space in your context window.

You always have to understand what is passed to the LLM. Seeing exactly what occupies your context window at every step is key to mastering context engineering. Usually this is done by properly monitoring your traces with observability platforms, tracking what happens at each step, and understanding the inputs and outputs [[18]](https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots). As this is a significant step to go from PoC to production, we will have dedicated lessons on this.

## Here is an example

Let's connect the theory and strategies discussed earlier with concrete examples. Consider several common real-world scenarios:

-   **Healthcare:** An AI assistant accesses a patient's medical history, current symptoms, and the latest medical literature to provide personalized diagnostic support [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
-   **Financial Services:** An AI system integrates with enterprise tools like Customer Relationship Management (CRM) systems and calendars, combining real-time market data and client portfolio information to generate tailored financial advice [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill).
-   **Project Management:** An AI system accesses enterprise infrastructure like CRMs, Slack, and task managers to automatically understand project requirements, then adds and updates project tasks.
-   **Content Creator Assistant:** An AI agent uses your research, past content, and personality traits to understand what and how to create a given piece of content.

Let's walk through a specific query to see context engineering in action with the healthcare assistant scenario. A user asks: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`

Before the AI attempts to answer, a context engineering system performs several steps [[41]](https://www.decodingai.com/p/context-engineering-2025s-1-skill):

1.  It retrieves the user's patient history, known allergies, and lifestyle habits from episodic memory.
2.  It queries a medical database for non-pharmacological headache remedies from semantic memory.
3.  It assembles this information, along with the user's query and conversation history, into a structured prompt.
4.  We send the prompt to the LLM, which generates a personalized, safe, and relevant recommendation.
5.  We log the interaction and save any new preferences back to the user's episodic memory.

Here’s a simplified Python example showing how these components might be assembled into a complete system prompt. Notice the clear structure and ordering using XML tags.

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

Still, the key relies on the system around it that brings in the proper context to populate the system prompt.

To build such a system, you would use a combination of tools. An LLM like **Gemini** provides the reasoning engine. A framework like **LangGraph** orchestrates the workflow [[65]](https://www.scalablepath.com/machine-learning/langgraph). Databases such as **PostgreSQL**, **Qdrant**, or **Neo4j** serve as long-term memory stores [[62]](https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b). Specialized tools like **Mem0** can manage memory state, and observability platforms like **Opik** or **LangSmith** are essential for debugging complex interactions [[64]](https://atlan.com/know/context-engineering-platforms-comparison/). For simpler applications, you can achieve significant results with only PostgreSQL or MongoDB.

## Connecting context engineering to AI engineering

Mastering context engineering is less about learning a specific algorithm and more about building intuition. It’s the art of knowing how to structure prompts, what information to include, and how to order it for maximum impact.

This skill doesn't exist in a vacuum. It’s a multidisciplinary practice that sits at the intersection of several key engineering fields [[23]](https://sombrainc.com/blog/ai-context-engineering-guide):

-   **AI Engineering:** Understanding LLMs, RAG, and AI agents is the foundation.
-   **Software Engineering:** You need to build scalable and maintainable systems to aggregate context and wrap agents in robust APIs [[22]](https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms).
-   **Data Engineering:** Constructing reliable data pipelines for RAG and other memory systems is critical [[25]](https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models).
-   **Operations (Ops):** Deploying agents on the right infrastructure and automating Continuous Integration/Continuous Deployment (CI/CD) makes them reproducible, observable, and scalable [[21]](https://packmind.com/context-engineering-ai-coding/what-is-contextops/).

Our goal with this course is to teach you how to combine these skills to build production-ready AI products. In the world of AI, we should all think in systems rather than isolated components, having a mindset shift from developers to architects.

In the next lesson, we will explore structured outputs, a key technique for selecting and formatting context. We will also continue to build on these ideas in later lessons covering actions, memory, and RAG.

## References

- [1]  https://x.com/karpathy/status/1937902205765607626 
- [2]  https://x.com/lenadroid/status/1943685060785524824 
- [3]  https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md 
- [4]  https://nlp.elvissaravia.com/p/context-engineering-guide 
- [5]  https://www.pinecone.io/learn/context-engineering/ 
- [6]  https://galileo.ai/blog/production-llm-monitoring-strategies 
- [7]  https://www.coforge.com/what-we-know/blog/navigating-the-shifting-sands-understanding-and-mitigating-data-drift-in-llms 
- [8]  https://thenewstack.io/context-rot-enterprise-ai-llms/ 
- [9]  https://insightfinder.com/blog/hidden-cost-llm-drift-detection/ 
- [10]  https://www.trychroma.com/research/context-rot 
- [11]  https://oneuptime.com/blog/post/2026-01-30-context-compression/view 
- [12]  https://www.dailydoseofds.com/llmops-crash-course-part-8/ 
- [13]  https://arxiv.org/html/2510.22101v1 
- [14]  https://blog.jetbrains.com/research/2025/12/efficient-context-management/ 
- [15]  https://www.decodingai.com/p/context-engineering-2025s-1-skill 
- [16]  https://www.comet.com/site/blog/context-window/ 
- [17]  https://datahub.com/blog/context-window-optimization/ 
- [18]  https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/ 
- [19]  https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider 
- [20]  https://blog.langchain.com/the-rise-of-context-engineering/ 
- [21]  https://www.datacamp.com/blog/context-engineering 
- [22]  https://arxiv.org/pdf/2507.13334 
- [23]  https://sombrainc.com/blog/ai-context-engineering-guide 
- [24]  https://packmind.com/context-engineering-ai-coding/what-is-contextops/ 
- [25]  https://www.glean.com/blog/context-engineering-ai-the-foundation-of-reliable-high-performing-models 
- [26]  https://www.securityindustry.org/2024/07/16/understanding-the-evolution-from-classic-chatbots-to-rag-chatbots-to-ai-powered-assistants/ 
- [27]  https://pagergpt.ai/ai-chatbot/evolution-of-ai-chatbots 
- [28]  https://www.dante-ai.com/news/when-did-ai-chatbots-start 
- [29]  https://www.linkedin.com/pulse/context-engineering-silent-architecture-behind-every-ai-roychowdhury-lzcec 
- [30]  https://www.sundeepteki.org/blog/from-vibe-coding-to-context-engineering-a-blueprint-for-production-grade-genai-systems 
- [31]  https://www.langchain.com/blog/context-engineering-for-agents 
- [32]  https://www.glean.com/perspectives/context-engineering-vs-prompt-engineering-key-differences-explained 
- [33]  https://atlan.com/know/working-memory-llms/ 
- [34]  https://arxiv.org/abs/2505.06120 
- [35]  https://arxiv.org/pdf/2505.00019 
- [36]  https://atlan.com/know/working-memory-llms/ 
- [37]  https://www.datacamp.com/blog/how-does-llm-memory-work 
- [38]  https://www.analyticsvidhya.com/blog/2026/01/how-does-llm-memory-work/ 
- [39]  https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/ 
- [40]  https://labelstud.io/learningcenter/episodic-vs-persistent-memory-in-llms/ 
- [41]  https://www.decodingai.com/p/context-engineering-2025s-1-skill 
- [42]  https://www.mdpi.com/2079-9292/13/15/2961 
- [43]  https://www.nature.com/articles/s41593-023-01496-2 
- [44]  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents 
- [45]  https://www.ibm.com/think/topics/ai-agent-memory 
- [46]  https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production 
- [47]  https://gurusup.com/blog/multi-agent-orchestration-guide 
- [48]  https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering 
- [49]  https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/ 
- [50]  https://arxiv.org/html/2601.13671v1 
- [51]  https://www.linkedin.com/posts/denis-panjuta_prompt-engineering-vs-context-engineering-activity-7363945251180322816-1q_m 
- [52]  https://memgraph.com/blog/prompt-engineering-vs-context-engineering 
- [53]  https://www.mezmo.com/learn-observability/context-engineering-for-observability-how-to-deliver-the-right-data-to-llms 
- [54]  https://www.instinctools.com/blog/context-engineering/ 
- [55]  https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/ 
- [56]  https://www.linkedin.com/pulse/lost-middle-lesson-failing-ai-agents-backwards-anthony-dejohn-01k2e 
- [57]  https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect 
- [58]  https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2 
- [59]  https://atlan.com/know/llm-context-window-limitations/ 
- [60]  https://bigdataboutique.com/blog/needle-in-haystack-optimizing-retrieval-and-rag-over-long-context-windows-5dfb3c 
- [61]  https://www.codecademy.com/article/context-engineering-in-ai 
- [62]  https://blog.stackademic.com/context-engineering-in-llms-and-ai-agents-eb861f0d3e9b 
- [63]  https://www.datacamp.com/tutorial/prompt-compression 
- [64]  https://atlan.com/know/context-engineering-platforms-comparison/ 
- [65]  https://www.scalablepath.com/machine-learning/langgraph 
- [66]  https://aclanthology.org/2025.naacl-srw.42.pdf 
- [67]  https://gorilla.cs.berkeley.edu/leaderboard.html 
- [68]  https://arxiv.org/abs/2505.03275 
- [69]  https://www.databricks.com/blog/long-context-rag-performance-llms 
- [70]  https://towardsdatascience.com/your-1m-context-window-llm-is-less-powerful-than-you-think/ 
- [71]  https://redis.io/blog/context-window-overflow/ 
- [72]  https://medium.com/@sahin.samia/the-common-failure-points-of-llm-rag-systems-and-how-to-overcome-them-926d9090a88f 
- [73]  https://www.unite.ai/why-large-language-models-forget-the-middle-uncovering-ais-hidden-blind-spot/