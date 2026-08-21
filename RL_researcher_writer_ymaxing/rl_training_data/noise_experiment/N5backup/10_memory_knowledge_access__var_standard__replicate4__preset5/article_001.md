# How Memory for AI Agents Works

In the previous lessons, we built a foundation in AI Engineering. We explored the agent landscape, distinguished between LLM workflows and autonomous agents, and introduced context engineering. Now, we will focus on memory, one of the most important components of context. Memory is where an agent stores information. Context engineering is the active process of deciding what to pull from that memory, how to format it, and when to load it into the model's working attention.

The core limitation of today's LLMs is that their knowledge is vast but frozen in time. They are fundamentally unable to learn by updating their weights after deployment, a problem known as "continual learning". To overcome this, we can inject new knowledge through the context window. However, this is a limited solution due to the finite size of the context, rising costs, and the "lost-in-the-middle" problem, where models struggle to use information buried deep in a long prompt.

An LLM without memory is like an intern with amnesia. It cannot recall previous conversations or learn from experience. Memory tools are the temporary solution we have today that provides agents with continuity and adaptability, giving them the ability to "learn" over time. Many early efforts to build personal AI companions quickly hit the limits of what was possible with the context window alone, forcing engineers to build complex memory systems with heavy compression and retrieval components. Working with 8k or 16k token context windows posed a different challenge than today’s models with over one million tokens.

As context windows expand, we must constantly adapt how we engineer stateful systems. In a future with even larger context windows or true model learning, fewer compression or retrieval components will be needed, as they introduce overhead and loss of nuance.

In this lesson, we will explore how to think about memory to build effective agents. We will borrow concepts from biology and cognitive science to differentiate between the model's static internal knowledge, short-term memory (the context window), and persistent long-term memory. We will focus on three types of long-term memory: semantic (facts), episodic (experiences), and procedural (skills). We will show you how to implement them, discuss the trade-offs of different storage approaches, and share best practices learned from real-world applications.

## The Layers of Memory: Internal, Short-Term, and Long-Term

To build agents that can remember, it is useful to adopt terminology from biology and cognitive science. This gives us a clear framework for categorizing an agent's memory into three distinct layers: internal knowledge, short-term memory, and long-term memory [[1]](https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR).

**Internal Knowledge** is the static, pre-trained information baked into the LLM's weights. This is also known as parametric memory, as knowledge is encoded directly into the model's parameters. It's distinct from latent memory, which refers to the model's internal representations within a single computation, like its KV cache [[9]](https://stevekinney.com/writing/agent-memory-systems). This is where the model’s general intelligence and reasoning priors reside. It knows countless facts and concepts without needing any context. However, this knowledge is read-only and does not update from experience without fine-tuning.

**Short-Term Memory**, also known as working memory, is the active context window of the LLM. It is the agent's "RAM"—volatile, fast, but limited in size [[2]](https://towardsai.net/p/machine-learning/long-term-vs-short-term-memory-for-ai-agents-a-practical-guide-without-the-hype). This is the only reality the model sees during a single call and the only way we can simulate learning over time. If information is not in the context window, it does not exist for the model.

**Long-Term Memory** is an external, persistent storage system where an agent can save and retrieve information across sessions [[3]](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/). This is what gives an agent continuity, allowing it to build a lasting understanding of users and tasks.

These layers work together in a retrieval pipeline. When an agent needs to perform a task, it queries its long-term memory for relevant information. This retrieved data is then loaded into short-term memory, becoming part of the context window. This process can involve querying different memory types in parallel and ranking the results before presenting them to the model [[4]](https://vizuara.substack.com/p/a-primer-on-re-ranking-for-retrieval).

```mermaid
graph TD
    subgraph Long-Term Memory (Persistent)
        A[Semantic Memory<br/>(Facts)]
        B[Episodic Memory<br/>(Experiences)]
        C[Procedural Memory<br/>(Skills)]
    end

    subgraph Retrieval Pipeline
        D{Parallel Queries & Ranking}
    end

    subgraph Short-Term Memory (Volatile)
        E[Context Window]
    end

    subgraph Core
        F((LLM<br/>Internal Knowledge))
    end

    A --> D
    B --> D
    C --> D
    D --> E
    E <--> F
```
Image 1: The three layers of agent memory and their retrieval flow.

This layered approach is effective because no single layer can perform all functions. Internal knowledge provides general intelligence, short-term memory handles the immediate task, and long-term memory provides the specific context and personalization that the other layers lack. However, it is worth noting that while these human-inspired categories are a useful mental model, they may not be the optimal way to structure memory for an AI with fundamentally different constraints than a biological brain [[9]](https://stevekinney.com/writing/agent-memory-systems). To better understand how to design this persistent layer, we can again borrow from cognitive science to break down long-term memory into more specific types.

## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory can be further divided into three key types, each serving a distinct role in making an agent more capable and intelligent [[5]](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory).

### Semantic Memory (Facts & Knowledge)

Semantic memory is the agent's encyclopedia, a structured repository of facts and knowledge. This is where the agent stores extracted concepts and relationships about specific domains, people, and things [[6]](https://www.geeksforgeeks.org/artificial-intelligence/ai-agent-memory/). What you store and how you structure it depends entirely on the agent's use case. The information can be stored as simple, independent strings like "The user is a vegetarian" or attached to an entity in a more structured format like `{"food_restrictions": "User is a vegetarian"}`.

The primary role of semantic memory is to provide a reliable source of truth. For a personal assistant, it can be used to build a persistent user profile, storing preferences (`{"music": "User likes rock music"}`), relationships (`{"dog": "User has a dog named George"}`), or constraints (`{"food_restrictions": "User is allergic to gluten"}`). When the agent needs to act, it can retrieve this specific information instead of searching through a long, noisy conversation history. For an enterprise agent, semantic memory might contain internal documents or a product catalog, allowing it to answer questions on proprietary topics.

### Episodic Memory (Experiences & History)

Episodic memory is the agent's personal diary, a chronological record of its past interactions [[7]](https://atlan.com/know/types-of-ai-agent-memory/). Think of it as facts with a timestamp attached. While semantic memory stores timeless knowledge, episodic memory is about "what happened and when."

This memory type is useful for maintaining conversational context and understanding complex dynamics. A semantic memory might store two separate facts: "User's brother is named Mark" and "User is frustrated with his brother." An episodic memory captures the nuance: "On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I then provided an empathetic response. `[created_at=2025-08-25T17:20:04]`"

This "episode" provides deeper context, allowing the agent to interact with more empathy and intelligence in the future. For example, it might say, "I know the topic of your brother's birthday can be sensitive..." The time element also allows the agent to answer questions like, "What happened on June 8th?" Depending on the product, these episodes can group events over a day, a single conversation, or a week. There is no one-size-fits-all solution.

### Procedural Memory (Skills & How-To)

Procedural memory is the agent's collection of skills and learned workflows. It is the "how-to" knowledge that enables it to perform multi-step tasks, like a set of playbooks for common requests [[8]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). This type of memory can be broken down into further levels of abstraction, from raw experiences to compiled skills [[9]](https://stevekinney.com/writing/agent-memory-systems).

At its simplest, it can be **case-based**, storing raw trajectories of what worked and what did not. More effectively, it can be **strategy-based**, distilling insights from experience, such as "When encountering connection timeout errors, check the connection pool first." At the most advanced level, it becomes **skill-based**, where the agent compiles successful strategies into reusable tools or code functions that it can invoke directly in the future [[9]](https://stevekinney.com/writing/agent-memory-systems).

This memory is often encoded as a reusable tool, function, or defined sequence of actions within the agent's system prompt. For instance, an agent might have a stored procedure called `MonthlyReportIntent`. When a user asks for a monthly update, the agent retrieves this procedure, which defines a clear series of steps: 1. Query the sales database for the last 30 days, 2. Summarize the key findings, and 3. Ask the user if they want the summary emailed or displayed directly. This makes the agent's behavior on common tasks reliable and predictable. By encoding successful workflows, procedural memory allows an agent to improve its efficiency over time, ensuring complex jobs are executed consistently.

Now that we have an idea of what to save and the benefits of each memory type, how should we store this information? There are several architectural approaches, each with its own trade-offs.

## Storing Memories: Pros and Cons of Different Approaches

How an agent's memories are stored is an important architectural decision that impacts performance, complexity, and scalability. Unlike a typical Retrieval-Augmented Generation (RAG) system that reads from a static knowledge base, agent memory is write-heavy, mutable, and temporal. New memories are constantly created and updated, making the storage architecture a critical choice [[10]](https://www.digitalapplied.com/blog/agent-memory-architectures-vector-graph-episodic). While the goal is always to provide the right context at the right time, the method of storage involves trade-offs. The ideal approach depends entirely on the product's use case.

Recent benchmarks provide concrete data on these trade-offs. For instance, while using the full conversation history as context yields the highest accuracy (72.9%), it comes with a p95 latency of over 17 seconds, making it unusable for real-time applications. In contrast, selective retrieval systems with graph-enhanced memory can achieve comparable accuracy (68.4%) with over 80% lower latency and token costs [[11]](https://mem0.ai/blog/state-of-ai-agent-memory-2026). Let's explore the pros and cons of three primary methods: storing memories as raw strings, as structured entities, and within a knowledge graph.

### Storing Memories as Raw Strings

This is the simplest method, where conversational turns or documents are stored as plain text and indexed for vector search [[12]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

-   **Pros:**
    -   **Simple and fast:** This method is the easiest to set up, requiring minimal engineering to log text and create embeddings.
    -   **Preserves nuance:** By storing raw text, the full context, including emotional tone and subtle linguistic cues, is preserved. Nothing is lost in translation.
-   **Cons:**
    -   **Imprecise retrieval:** Relying on semantic similarity alone is often not enough. A query like "What is my brother’s job?" might retrieve every conversation mentioning "brother" and "job" without pinpointing the current fact [[13]](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/).
    -   **Difficulty in updating:** If a user corrects information ("My brother is now a doctor"), the new string is simply added to the log, creating potential contradictions.
    -   **Lack of structure:** This approach struggles with temporal reasoning and state changes. It cannot easily distinguish between "Barry *was* the CEO" and "Claude *is* the CEO" because the relationship is not explicitly defined.

### Storing Memories as Entities (JSON-like Structures)

In this approach, we use an LLM to transform unstructured interactions into structured memories, storing them in a format like JSON.

-   **Pros:**
    -   **Structured and precise:** Information is organized into key-value pairs (`"user": {"brother": {"job": "Software Engineer"}}`), allowing for precise, field-level filtering.
    -   **Easier to update:** If a user's preference changes, only the relevant field in the JSON object needs to be updated, ensuring the memory remains current.
    -   **Ideal for factual data:** This method is well-suited for semantic memory, where user profiles and preferences are stored as facts.
-   **Cons:**
    -   **Increased upfront complexity:** This approach requires designing a schema. Deciding what to extract and how to structure it adds an initial layer of engineering complexity.
    -   **Potential for schema rigidity:** A predefined schema can be inflexible. If the agent encounters information that does not fit, that data may be lost unless the schema is updated. Dynamically updating schemas increases the risk of saving duplicated information.
    -   **Loss of original nuance:** The extraction process strips away the rich subtext of the original conversation. The fact `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day."

### Storing Memories in a Graph Database

This is the most advanced approach, where memories are stored as a network of nodes (entities) and edges (relationships), forming a knowledge graph [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

-   **Pros:**
    -   **Represents complex relationships:** A graph's core strength is explicitly defining how information is connected. It can map `(User) -> [HAS_BROTHER] -> (Mark) -> [WORKS_AS] -> (Software Engineer)`, enabling sophisticated queries.
    -   **Superior contextual and temporal awareness:** Knowledge graphs can model context and time as explicit properties of a relationship (e.g., `User -[RECOMMENDED_ON_DATE: "2025-10-25"]-> Restaurant`), providing more accurate retrieval than vector search alone [[15]](https://neo4j.com/nodes-2025/agenda/building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs/).
    -   **Auditability and explainability:** Retrieval is transparent. You can trace the exact path of nodes and edges that led to an answer, making it easier to debug the agent's reasoning.
-   **Cons:**
    -   **Highest complexity and cost:** This method requires a significant upfront investment in schema design, data modeling, and maintenance.
    -   **Potential for slower queries:** Complex graph traversals can be slower than simple vector lookups, which might impact real-time performance if not optimized.
    -   **Overhead for simple use cases:** For many applications, the complexity of a graph database is overkill. A simpler entity-based or string-based approach may be sufficient.

| Feature | Raw Strings | Entities (JSON) | Knowledge Graph |
| :--- | :--- | :--- | :--- |
| **Complexity** | Low | Medium | High |
| **Precision** | Low | High | Very High |
| **Nuance** | High | Low | Medium |
| **Updatability** | Low | High | High |
| **Best For** | Quick prototypes, logging | Semantic memory, user profiles | Complex relationships, temporal reasoning |
| **Key Challenge** | Retrieval noise | Schema rigidity | Engineering overhead |
*Table 1: A comparison of memory storage approaches.*

The choice of memory storage should be guided by your product's core needs. It is often best to start with the simplest architecture that delivers value and evolve it as your agent's requirements grow more complex. Now that we know what to save and how to store it, let's look at some code examples.

## Memory Implementations with Code Examples

This section provides practical code examples for implementing the different memory types. While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, a topic we will cover in the next lesson, the creation of high-quality memories is an equally important preceding step. We will use the `mem0` library and a simple "raw string" storage approach to focus on the unique benefits of each memory category.

<aside>
💡

You can find the code for this lesson in the `lessons/10_memory_knowledge_access` notebook in the course's GitHub repository.

</aside>

### What is mem0?

`mem0` is an open-source library designed to provide a universal memory layer for AI agents. It automates the full pipeline from input chat text to injected memories, handling extraction, consolidation, and retrieval. It integrates with various agent frameworks and storage backends, including vector and graph databases, to provide a scalable solution for long-term memory [[16]](https://arxiv.org/html/2504.19413). We will use it to demonstrate how to implement the different memory types we have discussed.

### Setup

First, we configure `mem0` to use Google's Gemini for embeddings and LLM-based extraction, with ChromaDB as a local vector store. This setup allows us to run everything within our notebook.

1.  We begin by setting up our environment and defining the configuration for `mem0`. This includes the LLM, the embedding model, and the local vector store. We also create helper functions to simplify adding and searching for memories.

    ```python
    import os
    from typing import Optional

    from google import genai
    from mem0 import Memory
    from utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])

    client = genai.Client()
    MODEL_ID = "gemini-2.5-pro"

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
                "model": MODEL_ID,
                "api_key": os.getenv("GOOGLE_API_KEY"),
            },
        },
    }

    memory = Memory.from_config(MEM0_CONFIG)
    MEM_USER_ID = "lesson9_notebook_student"
    memory.delete_all(user_id=MEM_USER_ID)

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
        """Category-aware search wrapper."""
        res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}
        items = res.get("results", [])
        if category is not None:
            items = [r for r in items if (r.get("metadata") or {}).get("category") == category]
        return items
    ```
    It outputs:
    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

### Semantic Memory: Extracting Facts

**How it's created:** Semantic memory is created through a deliberate extraction pipeline. After an interaction, the unstructured text is passed to an LLM with a specific prompt designed to extract atomic, context-independent facts. This process transforms messy conversational threads into a queryable knowledge base [[17]](https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer).

**Prompt Used to Create:** The prompt instructs the model to act as a knowledge extractor, identifying key facts, preferences, and relationships relevant to the agent's purpose.

```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or sublte details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```

**Memory Created:** The system would store these extracted facts as individual strings.

```
Mark is the user's brother. Mark is a software engineer. Mark's real passion is painting. The user has a painting from Mark and finds it beautiful.
```

**How it's Retrieved:** Retrieval of semantic memory often benefits from hybrid search, which combines keyword search for specific entities with semantic search for contextual relevance. The system can first filter memories based on exact matches (e.g., all memories containing "brother") and then perform a vector search within that subset to find the most relevant fact for a query like "job" [[18]](https://www.comet.com/site/blog/retrieval-augmented-generation/).

1.  Let's add a few facts to our semantic memory using our helper function.

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

2.  Now, we can search for a specific fact using a natural language query.

    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```
    It outputs:
    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

**How it's Created:** Episodic memory functions as a chronological log. Events can be created by having an LLM read and summarize a series of interactions. Crucially, these memories are always stored with a timestamp, which is essential for temporal reasoning [[19]](https://docs.mem0.ai/platform/features/timestamp).

**Prompt Used to Create:** If memories are summarized, the prompt might ask the LLM to distill the key events and insights from a conversation.

```
User: "I'm feeling stressed about my project deadline on Friday.", Assistant: "I'm sorry to hear that. I'm here to help you with that."
```

**Memory Created (raw):** The simplest form is just logging the raw text with a timestamp.

```
October 26th, 2025. 2:30PM EST: User: "I'm feeling stressed about my project deadline on Friday." Assistant: "I'm sorry to hear that. I'm here to help you with that."
```

**Memory Created (summarized):** An LLM can also create a more concise summary.

```
October 26th, 2025. 2:30PM EST User: "The user is stressed about their project deadline on Friday and the assistant offers to help."
```

**How it's Retrieved:** Retrieval from episodic memory is often a blend of temporal and semantic queries. A simple retrieval might filter by a date range ("What did we talk about yesterday?"). A more robust approach uses semantic search to find contextually similar conversations and then re-ranks the results based on recency.

1.  We simulate a short dialogue and use an LLM to create a concise summary, which we will store as an "episode".

    ```python
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
    print(
        mem_add_text(
            episode,
            category="episodic",
            summarized=True,
            turns=4,
        )
    )
    ```
    It outputs:
    ```text
    Saved episodic memory.
    ```

2.  We can then retrieve this episode by searching for related concepts. The `created_at` timestamp in the metadata is key for temporal reasoning.

    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
        print(h)
    ```
    It outputs:
    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.

    {'id': '...', 'memory': 'A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.', 'hash': '...', 'metadata': {'turns': 4, 'summarized': True, 'category': 'episodic'}, 'score': 0.91..., 'created_at': '2025-09-12T02:30:01.358468-07:00', 'updated_at': None, 'user_id': 'lesson9_notebook_student', 'role': 'user'}
    ```

### Procedural Memory: Defining and Learning Skills

**How it's Created:** Procedural memory can be created in two ways: explicitly defined by a developer as a tool or function, or learned dynamically from user interactions. More advanced agents can observe a user providing steps for a task and save that sequence as a new, callable procedure [[20]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/). This allows the agent to build a library of reusable skills over time, a concept explored in methods like Agent Workflow Memory (AWM) [[21]](https://openreview.net/forum?id=NTAhi2JEEE).

**Example Prompt:** The prompt guides the agent to recognize when a user is teaching it a new skill and to structure that skill for future use.

```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```

**Memory Created:** The LLM would generate a new structured procedure and save it to its tool library.

```
procedure_name: find_summer_cabin, steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options
```

**How it's Retrieved:** Retrieval is an intent-matching and function-calling process. The agent receives the descriptions of all available procedures in its context. It then compares the user's current request against these descriptions to find the most semantically similar procedure and execute it.

1.  We define a simple procedure for creating a monthly report and store it in our procedural memory.

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
    It outputs:
    ```text
    Learned procedure: monthly_report
    ```

2.  When the user asks how to perform the task, the agent can retrieve the stored procedure and follow its steps.

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

We have seen how to implement these different memory types. Now, let's discuss some additional considerations when building a memory system.

## Real-World Lessons: Challenges and Best Practices

The architectural patterns we have discussed provide a useful toolkit, but moving from theory to a reliable production system requires navigating complex trade-offs that are constantly evolving. Here are some of the most important lessons learned from building and scaling agent memory systems.

### Re-evaluating Compression

One of the biggest changes in memory design has been the trade-off between compressing information and preserving raw detail. Just two years ago, LLMs operated with small and expensive context windows, forcing engineers to be ruthless with compression. The goal was to distill every interaction into its most compact form—summaries, facts, or entities—to fit relevant information into the context. This process, however, is inherently lossy; summarizing keeps the general idea but loses fine details. This trade-off is formalized in information theory by the concept of rate-distortion, which shows there is no single optimal compression; instead, there is a curve of possible trade-offs between the size of the memory (rate) and its fidelity (distortion) [[22]](https://2018.ccneuro.org/proceedings/1050.pdf).

Today, with models offering million-token context windows at a fraction of the cost, the considerations have shifted. The best practice now leans towards less compression. The raw, unstructured conversational history is the ultimate source of truth, containing emotional subtext and relational dynamics that are often lost during extraction. While a fact might state, "User has a dog named George," the episodic log reveals, "User mentioned that walking their dog named George is the best part of their day," a far more valuable insight for a personalized agent [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Design your system to work with the most complete version of history that is economically and technically feasible. Use summarization and fact extraction as tools for creating queryable indexes, but always treat the raw log as the ground truth.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. The most common failure mode is over-engineering a complex memory system for a product that does not need it.

Start from first principles by defining the core function of your agent. The product's goal should dictate the memory architecture.
- For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point.
- For a long-term personal AI companion, rich episodic memories that include a time element are beneficial.
- For a task-automation agent, procedural memory is likely essential for recalling and executing multi-step workflows.

### The Human Factor

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system to the user, thinking it will improve transparency. In practice, it often creates significant cognitive overhead [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

Users should not be asked to "garden their agent's memories." This breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task. Memory management should be an autonomous function of the agent [[23]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents-toward). It should learn from corrections within the natural flow of conversation, such as, "Actually, my brother's name is Mark, not Mike." Design internal processes for the agent to periodically review, consolidate, and resolve conflicting information in its memory stores. The agent, not the user, is responsible for maintaining the integrity of its own knowledge.

## Conclusion

Memory is a core component of AI agents, enabling them to become personalized assistants that "learn" over time. While the memory tools we have today are a temporary solution for the absence of true continual learning in LLMs, they are a practical and effective approach that works right now. By understanding the different layers and types of memory, you can design systems that maintain conversational continuity, access relevant knowledge, and provide more capable and reliable assistance.

However, many research problems remain. These include managing memory staleness at scale, resolving user identity across sessions, and moving beyond simply remembering what happened to learning causal beliefs from outcomes [[24]](https://www.databricks.com/blog/memory-scaling-ai-agents), [[25]](https://medium.com/data-unlocked/the-memory-problem-in-ai-agents-is-half-solved-heres-the-other-half-ebbf218ae4d5). These memory systems are also finding applications in other domains, such as robotics, where an agent must recall past actions to navigate its environment efficiently [[26]](https://www.ibm.com/think/topics/ai-agent-memory).

In this lesson, we have explored the what, why, and how of agent memory. In our next lesson, we will dive deep into Retrieval-Augmented Generation (RAG), the primary mechanism for retrieving information from these memory stores. We will also touch upon multimodal processing, monitoring, and evaluations in future lessons as we continue our journey into building production-ready AI systems.

## References

- [1] [every-ai-agent-has-4-distinct-memory-layers-activity](https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR)
- [2] [long-term-vs-short-term-memory-for-ai-agents-a-practical-guide-without-the-hype](https://towardsai.net/p/machine-learning/long-term-vs-short-term-memory-for-ai-agents-a-practical-guide-without-the-hype)
- [3] [why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/)
- [4] [a-primer-on-re-ranking-for-retrieval](https://vizuara.substack.com/p/a-primer-on-re-ranking-for-retrieval)
- [5] [agent-memory](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory)
- [6] [ai-agent-memory](https://www.geeksforgeeks.org/artificial-intelligence/ai-agent-memory/)
- [7] [types-of-ai-agent-memory](https://atlan.com/know/types-of-ai-agent-memory/)
- [8] [beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/)
- [9] [memory-systems-for-ai-agents-what-the-research-says-and-what](https://stevekinney.com/writing/agent-memory-systems)
- [10] [agent-memory-architectures-vector-graph-episodic](https://www.digitalapplied.com/blog/agent-memory-architectures-vector-graph-episodic)
- [11] [state-of-ai-agent-memory-2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [12] [how-does-memory-for-ai-agents-work](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)
- [13] [plugmem-transforming-raw-agent-interactions-into-reusable-kn](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/)
- [14] [What is the perfect memory architecture?](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112)
- [15] [building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs](https://neo4j.com/nodes-2025/agenda/building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs/)
- [16] [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/html/2504.19413)
- [17] [mem0-how-three-prompts-created-a-viral-ai-memory-layer](https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer)
- [18] [retrieval-augmented-generation](https://www.comet.com/site/blog/retrieval-augmented-generation/)
- [19] [timestamp](https://docs.mem0.ai/platform/features/timestamp)
- [20] [a-practical-guide-to-memory-for-autonomous-llm-agents](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/)
- [21] [Agent Workflow Memory (AWM)](https://openreview.net/forum?id=NTAhi2JEEE)
- [22] [Semantic compression of episodic memories](https://2018.ccneuro.org/proceedings/1050.pdf)
- [23] [a-practical-guide-to-memory-for-autonomous-llm-agents-toward](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents-toward)
- [24] [memory-scaling-ai-agents](https://www.databricks.com/blog/memory-scaling-ai-agents)
- [25] [the-memory-problem-in-ai-agents-is-half-solved-heres-the-other-half](https://medium.com/data-unlocked/the-memory-problem-in-ai-agents-is-half-solved-heres-the-other-half-ebbf218ae4d5)
- [26] [what-is-ai-agent-memory-ibm](https://www.ibm.com/think/topics/ai-agent-memory)