# Lesson 9: Memory for Agents

In the last eight lessons, we have built a solid foundation in AI Engineering. We have explored the agent landscape, learned to distinguish between LLM workflows and AI agents, and mastered context engineering to manage the flow of information to a model. We have also given agents the ability to use tools and reason with frameworks like ReAct. Now, we will tackle one of the most important components for building advanced AI systems: memory.

LLMs have a fundamental limitation: their knowledge is vast but frozen in time. They are stateless and cannot update their internal weights to learn from new interactions after they have been deployed, a challenge known as "continual learning." An LLM without memory is like an intern with amnesia; it can perform a task competently in the moment but forgets everything as soon as you start a new conversation. To work around this, we can feed past information into the model's context window, which acts as a temporary working memory. However, this is not a perfect solution.

Keeping an entire conversation history in the context window is unrealistic. Context windows are finite, and even with modern models supporting millions of tokens, performance degrades as they get overloaded. The "lost-in-the-middle" problem means information buried in a long prompt is often ignored [[1]](https://openreview.net/forum?id=5sB6cSblDR). Furthermore, every token adds to the cost and latency of each turn. Standardized benchmarks quantify this trade-off: passing the full context may yield the highest accuracy, but at a p95 latency of over 17 seconds, it is unusable for real-time applications [[3]](https://mem0.ai/blog/state-of-ai-agent-memory-2026). As this technology evolves, we must constantly adapt our engineering practices. Just a few years ago, we were working with 8,000-token windows, which forced us to be aggressive with compression. Today, with one-million-token contexts, we can afford to preserve more raw detail [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

External memory systems provide a practical solution to this problem. They are the tools we have today to provide agents with continuity, adaptability, and the ability to "learn" from experience. In this lesson, we will explore how to design and implement memory. We will borrow concepts from cognitive science to categorize different types of memory, from the model's static internal knowledge to short-term working memory and persistent long-term storage. We will focus on implementing semantic, episodic, and procedural long-term memory to build agents that feel truly intelligent and personalized.

## The Layers of Memory: Internal, Short-Term, and Long-Term

To build effective memory systems, it helps to adopt terminology from biology and cognitive science. This gives us a structured way to think about how an agent stores and accesses different kinds of information across various time horizons. An agent's memory can be organized into three distinct layers, each serving a unique purpose [[4]](https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR).

**Internal Knowledge** is the static, pre-trained information baked into the LLM's weights. This is the model's vast understanding of the world, language patterns, and reasoning abilities. It is powerful but read-only; you cannot update it without fine-tuning. This is where the model stores its knowledge of entire books, ready to be accessed with an empty context window.

**Short-Term Memory**, also known as working memory, is the active context window. It is the only reality the model sees during a single call. This is where user input, retrieved facts, and conversation history live. It is volatile, fast, and, despite growing sizes, limited. This is the only layer where we can simulate "learning" over time by feeding back information from previous turns.

**Long-Term Memory** is an external, persistent storage system, like a database or file system. This is where an agent saves user preferences, past interactions, and learned facts to provide continuity across sessions.

These layers work together in a dynamic hierarchy. The agent uses a retrieval pipeline to pull relevant data from long-term memory, which populates the short-term working memory. This working state is then filtered and projected into the context window, providing the LLM with the precise information it needs to reason and respond. A useful neuroscience analogy is the process of memory consolidation in the human brain. New experiences are first captured in the hippocampus, a structure that acts as a fast, temporary storage. From there, they are gradually transferred to the neocortex for long-term storage during sleep. Similarly, an agent's recent interactions (short-term) can be processed and consolidated into its persistent, long-term memory [[5]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l).

```mermaid
flowchart LR
  %% LLM Core
  subgraph "LLM Core"
    LLM["LLM"]
    IK["Internal Knowledge<br/>(Pre-trained Weights)"]
  end

  %% Memory System
  subgraph "Memory System"
    LTM["Long-Term Memory<br/>(Persistent Storage)"]
    STM["Short-Term Memory<br/>(Working State)"]
    CW["Context Window<br/>(Filtered Projection)"]
  end

  %% Pipeline
  RP["Retrieval Pipeline"]

  %% Primary Data Flows
  LTM -- "retrieves relevant data" --> RP
  RP -- "populates" --> STM
  STM -- "filters & projects" --> CW
  CW -- "provides context" --> LLM

  %% Internal LLM relationship
  IK -- "informs reasoning" --> LLM

  %% Visual grouping
  classDef memory stroke-dasharray:3,3
  classDef process stroke-width:2px
  class LTM,STM,CW memory
  class RP,LLM process
```

Image 1: Diagram illustrating the hierarchy and flow of an AI agent's memory system.

This separation is useful because no single layer can do everything. Internal knowledge provides general intelligence, short-term memory handles the immediate task, and long-term memory provides the personalization and continuity that the other layers lack. To better understand how to design this long-term storage, we can borrow a few more concepts from cognitive science.

## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a monolith. Just like human memory, it can be broken down into different types, each storing a specific kind of information. Understanding these distinctions is key to designing an agent that can recall the right context for the right task [[6]](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents), [[7]](https://www.ibm.com/think/topics/ai-agent-memory).

### Semantic Memory (Facts & Knowledge)

**Semantic memory** is the agent's encyclopedia, a repository of factual knowledge. This is where the agent stores extracted concepts, relationships, and facts about specific domains, people, places, and things. The structure of this memory is highly dependent on the agent's use case. It could be a collection of simple, independent strings like `"The user is a vegetarian,"` or it could be a structured entity like a JSON object or even a node in a graph database.

The primary role of semantic memory is to give the agent a reliable source of truth. For an enterprise agent, this might involve storing internal company documents or a product catalog, allowing it to answer questions on proprietary topics. For a personal assistant, semantic memory is used to build a persistent profile of the user. It can store key information like preferences (`{"music": "User likes rock music"}`), relationships (`{"dog": "User has a dog named George"}`), or constraints (`{"food_restrictions": "User is allergic to gluten"}`). When the agent needs to act, it can retrieve this specific, relevant information instead of searching through a long and noisy conversation history. This curated knowledge base allows the agent to act with consistency and precision, whether it is recalling a user's favorite color or accessing technical specifications for a product [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). For example, a domain-expert agent in finance would rely heavily on semantic memory to access market data and financial models, whereas a personal assistant would prioritize episodic memory to remember user-specific details [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

### Episodic Memory (Experiences & History)

**Episodic memory** is the agent's personal diary, a chronological record of its past interactions. These are essentially facts with a timestamp attached. While semantic memory stores timeless knowledge, episodic memory is about "what happened and when" [[8]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems).

This memory type is crucial for maintaining conversational context and understanding the dynamics of a relationship over time. For instance, a simple semantic memory might store two separate facts: `"User's brother is named Mark"` and `"User is frustrated with his brother."` An episodic memory provides a much richer picture: `"On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I then provided an empathetic response. [created_at=2025-08-25T17:20:04]"`. This "episode" preserves the nuance, allowing the agent to interact with more intelligence and empathy in the future (e.g., *"As you mentioned last week, I know the topic of your brother's birthday can be sensitive..."*).

A key mechanism governing episodic memory is temporal decay, inspired by the human forgetting curve first studied by Hermann Ebbinghaus in 1885. Memories lose weight over time, so a recent event naturally outranks an older one. This doesn't mean old memories are erased; they just become less accessible, ensuring that the agent's "top-of-mind" context is populated with fresh, relevant information [[5]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l). This controlled forgetting, where relevance scores diminish unless reinforced, helps prune stale or low-value memories [[10]](https://prateekjoshi.substack.com/p/bringing-memory-to-ai-agents). The temporal element also allows the agent to answer questions like, *"What did we talk about on June 8th?"* Depending on the product, episodes can capture events from a single conversation, a full day, or an entire week. This ability to "time travel" through past interactions is what separates a simple chatbot from an assistant that understands your personal history [[5]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l).

### Procedural Memory (Skills & How-To)

**Procedural memory** is the agent's muscle memory, its collection of learned skills and workflows. It is the "how-to" knowledge that enables it to perform multi-step tasks reliably. This is a set of pre-defined playbooks for common requests [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

This memory is often encoded as a reusable tool, function, or sequence of actions, typically defined in the agent's system prompt. For example, an agent might have a procedure called `MonthlyReport`. When a user asks for a monthly update, the agent does not need to reason from scratch. It retrieves and executes the stored procedure, which defines a clear series of steps: 1) Query the sales database for the last 30 days, 2) Summarize the key findings, and 3) Ask the user if they want the report emailed or displayed. This makes the agent's behavior on common tasks fast, predictable, and reliable. By encoding successful workflows, procedural memory allows an agent to improve its efficiency over time. More advanced agents can even learn new procedures from user interactions, turning a sequence of successful steps into a new, reusable skill [[11]](https://arxiv.org/html/2508.06433v2). This is particularly important for workflow automation agents that handle repetitive processes, where procedural memory is the most critical component [[9]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

Now that we have an idea of what to save and the benefits of each memory type, how should we store this information?

## Storing Memories: Pros and Cons of Different Approaches

How an agent's memories are stored is a critical architectural decision that impacts performance, complexity, and scalability. While the goal is always to provide the right context at the right time, each storage method involves trade-offs. There is no one-size-fits-all solution; the ideal approach depends entirely on your product's use case. Let's explore the three primary methods: storing memories as raw strings, as structured entities, and within a knowledge graph [[12]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece).

**Storing memories as raw strings** is the simplest method. Conversational turns or documents are stored as plain text and indexed for vector search. The primary advantage of this approach is its simplicity and speed of implementation; it requires minimal engineering to get started. It also preserves the full nuance of an interaction, including emotional tone and subtle linguistic cues, as nothing is lost in translation to a structured format [[13]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). However, this method has significant drawbacks. Retrieval is often imprecise, as a query might return text that is semantically related but contextually wrong. For example, asking, *"What is my brother’s job?"* could retrieve every past conversation mentioning "brother" and "job" without pinpointing the correct fact [[13]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). This can be mitigated with techniques like Maximal Marginal Relevance (MMR), which diversifies results to avoid redundancy [[5]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l). Updating facts is also difficult; a correction just becomes another string in the log, creating potential contradictions. This method also struggles with temporal reasoning and state changes, as it cannot easily distinguish between "Barry *was* the CEO" and "Claude *is* the CEO" [[12]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece). As interaction logs grow, they fill with irrelevant content, making retrieval slower and less reliable [[14]](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/).

**Storing memories as entities** involves using an LLM to transform unstructured interactions into structured formats like JSON. This approach offers more precision, as information is organized into key-value pairs (`"user": {"brother": {"job": "Software Engineer"}}`), allowing for exact, field-level filtering. This makes it easy to retrieve specific facts without ambiguity and simplifies updates; if a user's preference changes, you only need to modify the relevant field. This method is ideal for semantic memory, where user profiles and preferences are stored [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). On the other hand, it requires more upfront complexity in designing a data schema. A predefined schema can be inflexible, and information that does not fit the structure may be lost. While an LLM can dynamically alter the schema, this increases the risk of saving duplicated information. Furthermore, the extraction process can strip away the rich subtext of the original conversation. The fact `"user_likes": ["cats"]` is far less descriptive than the original message, *"Petting my cat is the best part of my day"* [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

**Storing memories in a graph database** is the most advanced approach, structuring memory as a network of nodes (entities) and edges (relationships) to form a knowledge graph. The core strength of a graph is its ability to represent complex relationships explicitly, such as `(User) -> [HAS_BROTHER] -> (Mark) -> [WORKS_AS] -> (Software Engineer)`. This enables sophisticated multi-hop queries that trace these connections. Graphs also provide superior contextual and temporal awareness by modeling time as a property of a relationship (e.g., `User -[RECOMMENDED_ON_DATE: "2025-10-25"]-> Restaurant`) [[15]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). This is achieved through bi-temporal modeling, where facts are marked with both a valid time (when it happened) and a transaction time (when it was recorded), allowing outdated information to be invalidated rather than overwritten [[16]](https://arxiv.org/html/2602.05665v1). Retrieval is also transparent and auditable. However, this method has the highest complexity and cost, requiring significant investment in schema design and maintenance. Complex graph traversals can also be slower than simple vector lookups. For many simple use cases, the overhead of a graph database is not justified; it is most valuable for agents dealing with complex entity networks, like medical patient histories or enterprise account hierarchies [[3]](https://mem0.ai/blog/state-of-ai-agent-memory-2026), [[15]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).

| Storage Method | Pros | Cons |
| :--- | :--- | :--- |
| **Raw Strings** | Simple and fast to implement, preserves full conversational nuance. | Imprecise retrieval, difficult to update, lacks structure for temporal reasoning. |
| **Entities (JSON)** | Structured and precise, easy to update, ideal for factual data. | Increased upfront complexity, potential schema rigidity, loss of original nuance. |
| **Knowledge Graph** | Represents complex relationships, superior temporal awareness, auditable. | Highest complexity and cost, potentially slower queries, overkill for simple use cases. |

Table 1: A comparison of the three primary approaches to storing agent memories.

The right choice of memory storage should be guided by your product's core needs. It is often best to start with the simplest architecture that delivers value and evolve it as the demands on your agent grow more complex.

Now that we know what to save and how to store memories, let's look at some code examples using an open-source memory library.

## Memory Implementations with Code Examples

This section provides practical examples of how to implement the different memory types. While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, a topic we will cover in Lesson 10, the creation of high-quality memories is an equally important preceding step. A sophisticated memory system uses RAG-like retrieval, but it is not just a stateless lookup pipeline. It is a stateful system that changes over time based on what it learns, what is forgotten, and how it is used [[5]](https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l). To focus on the benefits of each memory category, we will use the "storing memories as raw strings" approach with the `mem0` library.

### What is mem0?

`mem0` is an open-source memory layer designed to provide AI agents with scalable long-term memory. It offers a simple API for adding, searching, and managing memories, handling tasks like data extraction, consolidation, and retrieval. It can integrate with various vector stores and LLMs, making it a flexible tool for building stateful agents [[17]](https://arxiv.org/html/2504.19413). We will use it with Google's Gemini models and a local ChromaDB vector store.

### Setup

First, we set up our environment by configuring `mem0` to use Gemini for both embeddings and LLM-based fact extraction, and ChromaDB as our local vector store. We also define two helper functions: `mem_add_text` to save a string to memory with a specific category tag, and `mem_search` to query memories.

1. We begin by defining the configuration for `mem0`, specifying Gemini as the provider for both the LLM and the embedder, and ChromaDB for the vector store.
    ```python
    import os
    from typing import Optional
    from mem0 import Memory
    
    MEM0_CONFIG = {
        "embedder": {
            "provider": "gemini",
            "config": {
                "model": "gemini-embedding-001",
                "embedding_dims": 768,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
        "vector_store": {
            "provider": "chroma",
            "config": {
                "collection_name": "lesson9_memories",
                "path": "/tmp/chroma_mem0",
            },
        },
        "llm": {
            "provider": "gemini",
            "config": {
                "model": "gemini-2.5-pro",
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
    }
    
    memory = Memory.from_config(MEM0_CONFIG)
    MEM_USER_ID = "lesson9_notebook_student"
    memory.delete_all(user_id=MEM_USER_ID)
    ```
    It outputs:
    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

2. Next, we define helper functions to simplify adding and searching for memories. `mem_add_text` stores a raw text string with a category, and `mem_search` retrieves memories based on a query, with an option to filter by category.
    ```python
    def mem_add_text(text: str, category: str = "semantic", **meta) -> str:
        """Add a single text memory. No LLM is used for extraction or summarization."""
        metadata = {"category": category}
        for k, v in meta.items():
            if isinstance(v, (str, int, float, bool)) or v is None:
                metadata[k] = v
            else:
                metadata[k] = str(v)
        memory.add(text, user_id=MEM_USER_ID, metadata=metadata, infer=False)
        return f"Saved {category} memory."
    
    
    def mem_search(query: str, limit: int = 5, category: Optional[str] = None) -> list[dict]:
        """
        Category-aware search wrapper.
        Returns the full result dicts so we can inspect metadata.
        """
        res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}
    
        items = res.get("results", [])
        if category is not None:
            items = [r for r in items if (r.get("metadata") or {}).get("category") == category]
        return items
    ```

### Semantic Memory: Extracting Facts

Semantic memory is created through an extraction pipeline. Unstructured text is passed to an LLM with a prompt designed to pull out atomic facts. For a general personal assistant, the prompt might look like this:

*Example Extraction Prompt:*
```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or subtle details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```

*Memory Created:*
The system would store these facts: `Mark is the user's brother.`, `Mark is a software engineer.`, `Mark's real passion is painting.`, `The user has a painting from Mark and finds it beautiful.`.

Retrieval uses hybrid search, combining keyword filtering with semantic search. A query like *"What's my brother's job?"* would first filter for memories containing "brother" and then perform a vector search for "job" to find the most relevant fact. Production systems often improve this with a second-pass reranker to re-score the initial candidates for relevance and metadata filtering to scope queries to specific projects or time ranges [[3]](https://mem0.ai/blog/state-of-ai-agent-memory-2026).

1. Let's add a few semantic facts to our memory store.
    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    ```
    It outputs:
    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    ```

2. Now, we can search for a specific fact using a natural language query.
    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memories function as a chronological log. They can be created by having an LLM read the conversation messages for a whole day, and then extract or summarize the insights, facts, and events that happened. These memories will have a timestamp. For example, given the input `User: "I'm stressed about my project deadline on Friday."`, a raw episodic memory would be the log itself: `October 26th, 2025. 2:30PM EST: User: "I'm feeling stressed about my project deadline on Friday."`. A summarized version might be: `October 26th, 2025. 2:30PM EST: "The user is stressed about their project deadline on Friday and the assistant offers to help."`.

Retrieval is a blend of temporal and semantic queries. A user might ask, *"What did we talk about yesterday?"* triggering a date-based filter. Or, a query like *"What was I worried about earlier?"* would trigger a semantic search for "worried" or "stressed," with results ranked by recency.

1. We simulate a short dialogue and use an LLM to create a concise summary, which we will store as an episodic memory.
    ```python
    from google import genai
    client = genai.Client()
    MODEL_ID = "gemini-2.5-pro"
    
    dialogue = [
        {"role": "user", "content": "I'm stressed about my project deadline on Friday."},
        {"role": "assistant", "content": "I’m here to help—what’s the blocker?"},
        {"role": "user", "content": "Mainly testing. I also prefer working at night."},
        {"role": "assistant", "content": "Okay, we can split testing into two sessions."},
    ]
    
    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.
    
    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    
    mem_add_text(
        episode,
        category="episodic",
        summarized=True,
        turns=4,
    )
    ```
    It outputs:
    ```text
    Saved episodic memory.
    ```

2. We can then retrieve this episode by searching for a key theme from the conversation.
    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
        print(f"Created at: {h['created_at']}")
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    
    Created at: 2025-09-12T02:30:01.358468-07:00
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory can be created in two ways: either defined by a developer as a coded tool or learned dynamically from user instructions. When a user provides explicit steps for a task, the agent can save this sequence as a new, callable procedure.

*Example Prompt:*
```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```

*Memory Created:*
The LLM would generate a new structured procedure and save it to its tool library: `procedure_name: find_summer_cabin`, `steps=[...]`.

Retrieval is an intent-matching and function-calling process. The agent compares the user's request against the descriptions of all available procedures. If a user later says, *"Let's find a summer cabin again,"* the agent will recognize the semantic similarity to the `find_summer_cabin` procedure it learned and execute it.

1. We define a multi-step procedure and save it to memory under the "procedure" category.
    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))
    
    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    ```

2. To "run" the procedure, we retrieve it by name and can then parse the steps for execution.
    ```python
    results = mem_search("how to create a monthly report", category="procedure", limit=1)
    if results:
        print(results[0]["memory"])
    ```
    It outputs:
    ```text
    Procedure: monthly_report
    Steps:
    1. Query sales DB for the last 30 days.
    2. Summarize top 5 insights.
    3. Ask user whether to email or display.
    ```
With these examples, we have seen how different types of memories can be implemented. Now, let's discuss some additional considerations when building a memory system.

## Real-World Lessons: Challenges and Best Practices

The architectural patterns we have discussed provide a useful toolkit for building agents with memory. However, moving from theory to a reliable, production-ready system requires navigating a series of complex trade-offs, especially as the underlying technology evolves so quickly. Here are some of the most important lessons learned from building and scaling agent memory systems in the real world [[2]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

One of the biggest shifts in memory design has been the re-evaluation of compression versus preserving raw detail. Just two years ago, LLMs operated with small and expensive context windows. This constraint forced us as AI Engineers to be ruthless with compression, distilling every interaction into its most compact form—summaries, facts, or entities. While necessary, this process is inherently lossy. Today, with models offering million-token context windows at a fraction of the cost, the considerations have changed. The best practice is now to lean towards less compression. The raw, unstructured conversational history is the ultimate source of truth. It contains the emotional subtext and relational dynamics that are often lost during extraction. While a fact might state, "User has a dog named George," the raw log reveals, "User mentioned that walking their dog... is the best part of their day," a far more valuable piece of information for a personalized agent. Design your system to work with the most complete version of history that is economically and technically feasible.

Another key lesson is to design for the product. There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. A common failure mode is over-engineering a complex, multi-part memory system for a product that does not need it. You should start from first principles by defining the core function of your agent. For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point. For a long-term personal AI companion, rich episodic memories are essential. For a task-automation agent, procedural memory is likely the most valuable.

Finally, the human factor and the cognitive overhead for the user should not be underestimated. Memory exists to make the agent smarter, not to give the user a new job. Many early memory implementations allowed users to view, edit, or delete stored facts. While well-intentioned, this creates significant cognitive overhead. Users should not be asked to "garden their agent's memories." This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task. Memory management should be an autonomous function. The agent should learn from corrections within the natural flow of conversation and be responsible for periodically reviewing, consolidating, and resolving conflicting information.

## Conclusion

Memory is a core component that transforms a simple, stateless chatbot into a truly adaptive and personalized agent. By enabling systems to remember past interactions, learn user preferences, and execute learned skills, memory allows us to build AI that feels more intelligent and helpful. While the techniques we have today are a practical workaround for the "continual learning" problem, they are powerful tools that allow us to create stateful experiences with the models available now. This remains an active area of research, with open problems like detecting memory staleness at scale and designing robust privacy and consent architectures [[3]](https://mem0.ai/blog/state-of-ai-agent-memory-2026).

In this lesson, we have explored the different layers of agent memory and learned how to implement semantic, episodic, and procedural long-term memory. We have also discussed the real-world challenges and best practices that come with building these systems in domains from personal assistants to robotic control systems [[7]](https://www.ibm.com/think/topics/ai-agent-memory).

The retrieval mechanisms we have touched upon are a critical part of making memory work. In our next lesson, we will dive deep into Retrieval-Augmented Generation (RAG), exploring how to build robust pipelines that can search vast knowledge bases to provide agents with the exact information they need. As we move forward in the course, we will continue to build on these concepts, learning how to monitor and evaluate our memory-enabled agents to ensure they are reliable and effective in production.

## References

- [1] Baker, G. A., Raut, A., Shaier, S., Hunter, L. E., & Von Der Wense, K. (2024, January 1). Lost in the middle, and In-Between: Enhancing language models' ability to reason over long contexts in Multi-Hop QA. *OpenReview*. https://openreview.net/forum?id=5sB6cSblDR
- [2] Whitmore, S. (2025). What is the perfect memory architecture? *YouTube*. https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112
- [3] State of AI Agent Memory 2026. (2026). *Mem0 Blog*. https://mem0.ai/blog/state-of-ai-agent-memory-2026
- [4] Iusztin, P. (2025). Every AI agent has 4 distinct memory layers. *LinkedIn*. https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR
- [5] Teaching Alfred to Remember with a Neuroscience-Inspired Memory System for AI Agents. (2026). *DEV Community*. https://dev.to/joojodontoh/teaching-alfred-to-remember-with-a-neuroscience-inspired-memory-system-for-ai-agents-2o5l
- [6] Iusztin, P. (2025). Memory: The secret sauce of AI agents. *Decoding ML*. https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents
- [7] Stryker, C. (2025). What is AI agent memory? *IBM*. https://www.ibm.com/think/topics/ai-agent-memory
- [8] Swirl AI. (2025). Memory in Agent Systems. *Swirl AI Newsletter*. https://www.newsletter.swirlai.com/p/memory-in-agent-systems
- [9] Machine Learning Mastery. (2025). The 3 Types of Long-Term Memory AI Agents Need. *Machine Learning Mastery*. https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/
- [10] Bringing memory to AI agents. (2025). *Prateek Joshi's Newsletter*. https://prateekjoshi.substack.com/p/bringing-memory-to-ai-agents
- [11] arXiv. (2025). Procedural Memory in Language Model-based Agents. *arXiv*. https://arxiv.org/html/2508.06433v2
- [12] Porras, D. & Barda, V. (2025). Memex 2.0: Memory The Missing Piece for Real Intelligence. *Substack*. https://danielp1.substack.com/p/memex-20-memory-the-missing-piece
- [13] How Does Memory for AI Agents Work? (2025). *Decoding AI*. https://www.decodingai.com/p/how-does-memory-for-ai-agents-work
- [14] From Raw Interaction to Reusable Knowledge: Rethinking Memory for AI Agents. (2025). *Microsoft Research Blog*. https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/
- [15] Lintvelt, H. (2025). Knowledge Graphs as Memory: Why Your AI Agent Needs to Think in Relationships. *OctoCo Blog*. https://www.octoco.ai/blog/knowledge-graphs-as-memory
- [16] Graphiti: A Bi-temporal Graph Model for Tracking AI Agent State. (2026). *arXiv*. https://arxiv.org/html/2602.05665v1
- [17] Mem0 Team. (2025). Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. *arXiv*. https://arxiv.org/html/2504.19413
- [18] A Practical Guide to Memory for Autonomous LLM Agents. (2026). *Towards Data Science*. https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/
- [19] 7 AI Agent Failure Modes and How To Prevent Them in Production. (2026). *Galileo*. https://galileo.ai/blog/agent-failure-modes-guide