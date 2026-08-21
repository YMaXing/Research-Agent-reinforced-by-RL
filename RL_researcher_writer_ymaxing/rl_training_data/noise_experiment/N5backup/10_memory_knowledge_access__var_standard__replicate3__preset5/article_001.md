# Lesson 9: Memory for Agents

In the previous lessons, we built a solid foundation in AI Engineering. We explored the agent landscape, learned to distinguish between rule-based LLM workflows and autonomous agents, and mastered context engineering. We even built a ReAct agent from scratch, giving our LLM the ability to reason and use tools.

Now, we will tackle one of the most important components of building intelligent systems: memory. The knowledge within LLMs is vast but frozen in time. They are fundamentally unable to learn from new interactions by updating their internal weights, a challenge known as "continual learning." To overcome this, we can feed new information into the model's context window. However, this is a limited solution due to finite context sizes and the "lost-in-the-middle" problem, where models struggle to use information buried in long prompts.

An LLM without a dedicated memory system is like an intern with amnesia. It can perform tasks based on the instructions it receives at the moment but cannot recall past conversations, learn from experience, or build a lasting understanding of a user's needs. This challenge is not new, but our approach to it has evolved. Early symbolic AI used expert systems with rigid, rule-based knowledge, which were traceable but brittle [[21]](https://builder.aws.com/content/2uYUowZxjkh80uc0s2bUji0C9FP/from-logic-to-learning-the-future-of-ai-lies-in-neuro-symbolic-agents). Modern generative AI is fluent and adaptive but often lacks factual grounding [[22]](https://djimit.nl/from-symbolic-ai-to-reasoning-llms-1950-2025/). Agentic memory systems represent a convergence, aiming to combine structured knowledge with the flexibility of neural models.

Memory tools provide an engineering workaround for the model's inability to learn, giving agents continuity, adaptability, and a semblance of memory. When building personal AI companions, many early efforts quickly hit the limits of what was possible with the context window alone. Working with 8,000 or 16,000 tokens forced us to engineer complex systems with aggressive compression and retrieval. Today, with models offering million-token context windows, the engineering trade-offs have shifted, but the core problem remains. Simply stuffing the entire history into the context is not a scalable strategy. It is slow, expensive, and introduces noise that degrades performance.

In this lesson, we will explore how to design and implement memory systems for AI agents. We will borrow concepts from biology and cognitive science to categorize different types of memory and understand their roles. You will learn the difference between a model's internal knowledge, its short-term working memory, and persistent long-term memory. We will focus on implementing three types of long-term memory—semantic (facts), episodic (experiences), and procedural (skills). By the end, you will understand the architecture, trade-offs, and practical code needed to build agents that remember.

## The Layers of Memory: Internal, Short-Term, and Long-Term

To build effective memory systems, we first need a clear mental model of how memory works. Borrowing from cognitive science helps us categorize an agent's memory into distinct layers, each serving a specific function [[1]](https://www.ibm.com/think/topics/ai-agent-memory), [[2]](https://arxiv.org/html/2309.02427). This is more than just an analogy; research is actively drawing on neuroscience, with memory architectures inspired by the human hippocampus that aim to build understanding through experience [[23]](https://medium.com/@jsmith0475/architecting-autonomy-the-neuroscience-behind-agentic-ai-systems-29aab6d5d131). These layers are not independent; they work together in a filtering hierarchy to provide the LLM with the right information at the right time [[3]](https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR).

**Internal Knowledge** is the information pre-trained into the LLM’s weights. This includes world knowledge, language patterns, and reasoning abilities. It is powerful but static and read-only. Without fine-tuning, this knowledge base does not update with new information from user interactions.

**Short-Term Memory** (or working memory) is the agent’s active context window. This is the "RAM" of the system, holding the immediate information for the current task: the user's latest query, recent conversation history, tool outputs, and intermediate reasoning steps [[4]](https://docs.letta.com/guides/agents/memory), [[5]](https://langchain-ai.github.io/langgraph/concepts/memory/). If information is not in the context window, it does not exist for the model during that specific call.

**Long-Term Memory** is an external, persistent storage system that allows an agent to retain information across sessions [[6]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems). This is where user preferences, past interactions, and learned facts are stored, giving the agent a sense of continuity.

The dynamic between these layers is a retrieval pipeline. Information from long-term memory is selectively retrieved and loaded into short-term memory to become actionable context for the LLM. This process, illustrated in Image 1, ensures the model receives relevant, personalized information without being overwhelmed by its entire history.

```mermaid
graph TD
    subgraph "Long-Term Memory (External Database)"
        A[Semantic Memory<br/>(Facts)]
        B[Episodic Memory<br/>(Experiences)]
        C[Procedural Memory<br/>(Skills)]
    end

    subgraph "Retrieval Pipeline"
        direction LR
        D{Parallel Queries}
        E[Ranking & Filtering]
        D --> E
    end

    subgraph "Short-Term Memory (Context Window)"
        F[Retrieved Context]
        G[Current Conversation]
    end

    subgraph "Agent Core"
        H((LLM))
    end

    A --> D
    B --> D
    C --> D
    E --> F
    F --> H
    G --> H
```

Image 1: The memory hierarchy, showing how information flows from long-term storage through a retrieval pipeline into the agent's short-term working memory.

This layered approach is effective because each type of memory is optimized for a different function. Internal knowledge provides general intelligence, short-term memory handles the immediate task, and long-term memory provides the personalization and continuity that the other layers lack. To better design the long-term memory, we can again borrow from cognitive science to break it down further.

## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory gives an agent persistence, allowing it to build on past interactions. To implement it effectively, we can categorize it into three types, each serving a distinct purpose in making an agent more intelligent and personalized [[7]](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents), [[2]](https://arxiv.org/html/2309.02427).

### Semantic Memory (Facts & Knowledge)

**Semantic memory** is the agent's encyclopedia, a structured repository of facts and knowledge. This information is context-independent, representing what the agent "knows" about the world, a specific domain, or a user. These "facts" can be stored as individual, independent strings like `"User is a vegetarian"`, or they can be attached to an "entity" such as a person, place, or object, for example, `{"user_profile": {"food_restrictions": "User is a vegetarian"}}`. The structure you choose is highly dependent on the agent's use case [[8]](https://langchain-ai.github.io/langgraph/concepts/memory/).

This type of memory provides the agent with a reliable source of truth. For an enterprise agent, this might involve storing internal company documents or technical manuals. For a personal assistant, semantic memory is used to build a persistent user profile. It can recall specific information like preferences (`{"music": "User likes rock music"}`), relationships (`{"dog": "User has a dog named George"}`), or constraints (`{"food_restrictions": "User is allergic to gluten"}`). This allows the agent to retrieve relevant information directly, rather than depending on a noisy and lengthy conversation history to infer these details [[9]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/). For domain-expert agents in fields like law or finance, semantic memory is the most critical type, as it allows them to integrate with RAG systems to pull in specialized knowledge [[10]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

### Episodic Memory (Experiences & History)

**Episodic memory** is the agent's personal diary, a chronological log of its past interactions and experiences. Unlike the timeless facts in semantic memory, episodic memories are about "what happened and when." Each entry is an "episode" tied to a specific point in time, preserving the context in which an event occurred [[11]](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory).

This memory type is crucial for maintaining conversational continuity and understanding the evolution of a user's state or relationship. For instance, a simple semantic memory might store two conflicting facts: `"User's brother is named Mark"` and `"User is frustrated with his brother."` An episodic memory provides deeper, time-stamped context: `"On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. I provided an empathetic response. [created_at=2025-08-25T17:20:04]"`.

This episode captures a nuanced moment that a simple fact cannot. It allows the agent to interact with more empathy in the future, perhaps by saying, "I know the topic of your brother's birthday can be sensitive..." By adding the element of time, episodic memory enables the agent to answer questions like, "What did we discuss last week?" and build a richer, more dynamic understanding of the user. This ability is also essential in robotics and autonomous systems, where an agent must recall the sequence of its past actions and their outcomes to navigate and learn in dynamic environments [[1]](https://www.ibm.com/think/topics/ai-agent-memory). For personal AI assistants focused on user personalization, episodic memory is often the most important type [[10]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

### Procedural Memory (Skills & How-To)

**Procedural memory** is the agent's muscle memory, a collection of learned skills, workflows, and "how-to" knowledge [[10]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/). It contains the playbooks for executing multi-step tasks, making the agent's behavior on common requests reliable and efficient. Rather than just storing facts, this type of memory captures how to do things better based on past experience. It can be broken down into a few levels of abstraction [[24]](https://stevekinney.com/writing/agent-memory-systems):

-   **Case-based:** At the simplest level, the agent stores raw trajectories of past tasks: "User asked X, I tried approach Y, it failed, I tried approach W, it worked." This preserves high-fidelity records but is inefficient to reuse.
-   **Strategy-based:** The agent distills insights from those raw experiences into generalizable strategies, such as, "When encountering connection timeout errors, always check the firewall settings first." This knowledge transfers across different tasks.
-   **Skill-based:** The most advanced level, where the agent compiles successful strategies into executable code or reusable tools. For example, an agent in Minecraft might learn how to mine iron, then write a `mineIron()` function that it can call directly in the future instead of reasoning from scratch [[25]](https://arxiv.org/abs/2305.16291).

This memory is often encoded directly into the agent's system prompt as a reusable tool or a defined sequence of actions. For example, an agent might have a stored procedure for a `MonthlyReportIntent`. When a user asks for a monthly update, the agent retrieves this procedure, which outlines a clear series of steps: 1) Query the sales database, 2) Summarize key findings, and 3) Ask the user for their preferred output format. By encoding successful workflows, procedural memory allows an agent to improve its efficiency over time, ensuring complex jobs are executed consistently. For workflow automation agents, this is the key memory type [[10]](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/).

While these human-inspired categories are useful, some researchers argue they may not be optimal for AI. An agent has different constraints than a human brain—such as perfect recall of stored information—and may benefit from memory structures that are learned rather than inherited from cognitive science [[24]](https://stevekinney.com/writing/agent-memory-systems). Now that we have an idea of what to save, we need to decide how to store this information.

## Storing Memories: Pros and Cons of Different Approaches

How an agent's memories are stored is a critical architectural decision that impacts performance, complexity, and scalability. While the goal is always to provide the right context at the right time, the method of storage involves trade-offs. There is no one-size-fits-all solution; the ideal approach depends entirely on your product's use case. Let's explore the pros and cons of three primary methods: storing memories as raw strings, as structured entities, and within a knowledge graph.

### Storing Memories as Raw Strings

This is the simplest method, where conversational turns or documents are stored as plain text and indexed for vector search [[12]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work).

-   **Pros:** It is simple and fast to set up, requiring minimal engineering to log text and create embeddings. This approach also preserves the full nuance of the original interaction, including emotional tone and subtle linguistic cues, as nothing is lost in translation to a structured format. Keeping raw episodic records is a good practice to avoid summarization drift, where repeated compression loses important details over time [[9]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).
-   **Cons:** Retrieval can be imprecise. Relying solely on semantic similarity often returns text that is semantically related but contextually wrong. For example, a query for "my brother's job" might retrieve all past conversations mentioning "brother" and "job" without pinpointing the current fact [[12]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). Updating information is also difficult; if a user corrects a fact ("My brother is now a doctor"), the new information simply adds to the log, creating potential contradictions. This method lacks the structure needed for reliable temporal reasoning or tracking state changes, like distinguishing between "Barry *was* the CEO" and "Claude *is* the CEO" [[13]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece).

### Storing Memories as Entities (JSON-like Structures)

In this approach, unstructured interactions are transformed into structured data, typically using an LLM, and stored in a format like JSON.

-   **Pros:** Information is organized into key-value pairs, allowing for precise, field-level filtering and retrieval. This makes it easy to pull specific facts without ambiguity. For example, by filtering for the "brother" entity, an agent can retrieve all related information, including his job and name. Updates are also straightforward; if a user's preference changes, you only need to modify the relevant field in the JSON object. This method is ideal for semantic memory, where user profiles and preferences are stored as facts [[8]](https://langchain-ai.github.io/langgraph/concepts/memory/).
-   **Cons:** This approach requires more upfront engineering to design a data schema. A predefined schema can also be rigid; if the agent encounters information that does not fit the structure, that data may be lost unless the schema is updated [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). While an LLM can dynamically alter the schema, this adds complexity and increases the risk of duplicate information. Furthermore, the extraction process strips away the rich subtext of the original conversation. The factual memory `"user_likes": ["cats"]` is far less representative than the original message, "Petting my cat is the best part of my day."

### Storing Memories in a Graph Database

This is the most advanced approach, where memories are stored as a network of nodes (entities) and edges (relationships), forming a knowledge graph.

-   **Pros:** Graphs excel at representing complex relationships explicitly. For instance, a graph can map `(User) -> [HAS_BROTHER] -> (Mark) -> [WORKS_AS] -> (Software Engineer)`, enabling sophisticated queries that trace these connections. They offer superior contextual and temporal awareness by modeling time as an explicit property of a relationship (e.g., `User -[RECOMMENDED_ON_DATE: "2025-10-25"]-> Restaurant`) [[15]](https://www.octoco.ai/blog/knowledge-graphs-as-memory). Retrieval is also transparent and auditable, as you can trace the exact path of nodes and edges that led to an answer, making it easier to debug the agent's reasoning.
-   **Cons:** This method carries the highest complexity and cost, requiring significant upfront investment in schema design, data modeling, and maintenance. Converting unstructured text into structured graph triples is a non-trivial task [[16]](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/). Complex graph traversals can also be slower than simple vector lookups. For example, benchmarks on the LOCOMO dataset show that a graph-enhanced memory system can have a p95 latency of 2.59 seconds, compared to 1.44 seconds for a vector-only approach, for a modest gain in accuracy [[26]](https://mem0.ai/blog/state-of-ai-agent-memory-2026). For many applications, this latency trade-off and the overhead of a graph database are unnecessary when a simpler approach would suffice.

Table 1: A comparison of the three primary memory storage approaches.

| Feature | Raw Strings | Entities (JSON) | Knowledge Graph |
| :--- | :--- | :--- | :--- |
| **Complexity** | Low | Medium | High |
| **Precision** | Low | High | Very High |
| **Updateability** | Low (Append-only) | High (Field-level) | High (Relationship-level) |
| **Nuance** | High | Low (Lost in extraction) | Medium (Depends on schema) |
| **Best For** | Simple logging, preserving raw interactions | Semantic memory, user profiles, facts | Complex relationships, temporal reasoning, explainability |

Beyond the initial storage architecture, a production-grade memory system must also evolve. This involves not only adding new information but also consolidating related entries, updating facts when they change, and actively forgetting outdated or irrelevant memories to maintain retrieval quality [[24]](https://stevekinney.com/writing/agent-memory-systems). The right choice of memory storage should be guided by your product's core needs. It is often best to start with the simplest architecture that delivers value and evolve it as your agent's requirements grow more complex. Now that we know what to save and how to store it, let's look at some code examples.

## Memory Implementations with Code Examples

While Retrieval-Augmented Generation (RAG) is the mechanism for retrieving information, a topic we will cover in the next lesson, the creation of high-quality memories is an equally important preceding step. To demonstrate how to implement the different memory types, we will use the `mem0` library, an open-source tool designed to give AI agents long-term memory. We will focus on the "storing memories as raw strings" approach to keep the examples simple and highlight the unique benefits of each memory category.

<aside>
💡

You can find the code for this lesson in the Lesson 9 notebook in the course's GitHub repository.

</aside>

### What is mem0?

Mem0 is an open-source memory layer that provides a scalable, production-ready solution for giving AI agents long-term memory. It automates the entire pipeline, from extracting salient information from conversations to storing, consolidating, and retrieving it when needed. It supports various backends, including vector stores and graph databases, and integrates with popular agent frameworks. On the LOCOMO benchmark, Mem0 has been shown to achieve 26% higher accuracy than OpenAI's native memory with 91% lower latency compared to full-context approaches, making it a powerful tool for building stateful agents [[27]](https://arxiv.org/html/2504.19413).

### Setup

First, we set up our environment by configuring the `mem0` library. We will use Google's Gemini for both the LLM (for fact extraction) and embeddings. For our vector store, we will use ChromaDB, which runs locally in the notebook.

1.  We define the configuration for `mem0`, specifying Gemini as the provider for our LLM and embeddings, and ChromaDB as our local vector store.

    ```python
    import os
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
    print("✅ Mem0 ready (Gemini embeddings + local Chroma).")
    ```

    It outputs:

    ```text
    ✅ Mem0 ready (Gemini embeddings + local Chroma).
    ```

2.  Next, we create a few helper functions to add and search for memories. The `mem_add_text` function saves a string to memory with a specific category tag (`semantic`, `episodic`, or `procedure`), while `mem_search` allows us to retrieve memories and optionally filter them by category.

    ```python
    from typing import Optional
    
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

Semantic memory is created through a deliberate extraction pipeline. An LLM processes unstructured text with a specific prompt designed to pull out atomic, context-independent facts. This turns messy conversational data into a queryable knowledge base [[17]](https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer). For retrieval, hybrid search is often effective, combining keyword filtering for known entities with a vector search for semantic relevance.

Example Extraction Prompt (For a general personal assistant):

```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent. While reading the messages, make sure to notice the nuance or sublte details that might be important when saving these facts.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting, he gifted me a painting a few years ago. Its really beautiful.}
```

The system would store: `Mark is the user's brother. Mark is a software engineer. Mark's real passion is painting. The user has a painting from Mark and finds it beautiful.`.

1.  We start by defining a list of facts we want to store in our semantic memory.

    ```python
    facts: list[str] = [
        "User prefers vegetarian meals.",
        "User has a dog named George.",
        "User is allergic to gluten.",
        "User's brother is named Mark and is a software engineer.",
    ]
    for f in facts:
        print(mem_add_text(f, category="semantic"))
    
    print(f"Added {len(facts)} semantic memories.")
    ```

    It outputs:

    ```text
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Saved semantic memory.
    Added 4 semantic memories.
    ```

2.  Now, we can search this memory with a natural language query. When we search for "brother job," the system retrieves the most relevant fact.

    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```

    It outputs:

    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memory functions as a chronological log of events. These memories can be created by having an LLM summarize interactions and storing them with a timestamp. This allows the agent to recall "what happened and when." Retrieval often blends temporal queries (filtering by date) with semantic search to find contextually similar past events.

Example Input: `User: "I'm feeling stressed about my project deadline on Friday.", Assistant: "I'm sorry to hear that. I'm here to help you with that."`

Memory Created (raw): `October 26th, 2025. 2:30PM EST: User: "I'm feeling stressed about my project deadline on Friday." Assistant: "I'm sorry to hear that. I'm here to help you with that."`

Memory Created (summarized): `October 26th, 2025. 2:30PM EST User: "The user is stressed about their project deadline on Friday and the assistant offers to help."`

1.  First, we define a short dialogue that we want to compress into a single "episode."

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
    ```

2.  We use an LLM to create a concise summary of this interaction. This summary becomes our episodic memory.

    ```python
    episodic_prompt = f"""Summarize the following 3–4 turns as one concise 'episode' (1–2 sentences).
    Keep salient details and tone.
    
    {dialogue}
    """
    episode_summary = client.models.generate_content(model=MODEL_ID, contents=episodic_prompt)
    episode = episode_summary.text.strip()
    print(episode)
    ```

    It outputs:

    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

3.  We add this summary to our memory, tagging it as "episodic."

    ```python
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

4.  Now, we can retrieve this episode using a semantic query. Searching for "deadline stress" brings back the summary, along with its metadata, including the creation timestamp provided by `mem0` [[18]](https://docs.mem0.ai/platform/features/timestamp). This allows the agent to answer questions like, "What did we talk about last week?"

    ```python
    print("\nSearch --> 'deadline stress'\n")
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
        print(h)
    ```

    It outputs:

    ```text
    
    Search --> 'deadline stress'
    
    
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    
    {'id': '...', 'memory': '...', 'hash': '...', 'metadata': {'turns': 4, 'summarized': True, 'category': 'episodic'}, 'score': 0.91..., 'created_at': '2025-09-12T02:30:01.358468-07:00', 'updated_at': None, 'user_id': 'lesson9_notebook_student', 'role': 'user'}
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory is created either by a developer defining a skill or by an agent learning a new workflow from a user. Retrieval is an intent-matching process where the LLM compares a user's request against the descriptions of all available procedures and triggers the best match.

Example Prompt:

```
You are an agent that can learn new skills. When a user provides a numbered list of steps to accomplish a goal, your task is to run the "learn_procedure" tool, and convert these numbered list of steps into a reusable procedure. Identify the core actions and any variable parameters (e.g., dates, locations, names).

Examples:
User Input: "I want you to book a cabin for this summer. To do that, please remember to: 1. Search for cabins on CabinRentals.com my favorite website. 2. Filter for locations in the mountains, the closer to them, the better. 3. Make sure it's available around July. 4 to 8th. 5. Send me the top 3 options."

learn_procedure(name="find_summer_cabin", steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options)
```

Memory Created: The LLM would generate a new structured procedure and save it to its tool/procedures library: `procedure_name: find_summer_cabin`, `steps=first search for cabins on CabinRentals.com, then filter for locations in the mountains, check for distance to the mountains, then check availability around what the user wants, if the user hasn't specified a date, ask the user for a date, once you have a list of options, send the top 3 options`.

1.  We define a procedure for creating a monthly report and store it as a single text block.

    ```python
    procedure_name = "monthly_report"
    steps = [
        "Query sales DB for the last 30 days.",
        "Summarize top 5 insights.",
        "Ask user whether to email or display.",
    ]
    procedure_text = f"Procedure: {procedure_name}\nSteps:\n" + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps))
    
    mem_add_text(procedure_text, category="procedure", procedure_name=procedure_name)
    
    print(f"Learned procedure: {procedure_name}")
    ```

    It outputs:

    ```text
    Learned procedure: monthly_report
    ```

2.  Later, the agent can retrieve this procedure by searching for its purpose. A query like "how to create a monthly report" will retrieve the saved steps, which can then be executed. This demonstrates how an agent can learn and trigger reusable playbooks [[19]](https://arxiv.org/html/2508.06433v4).

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

We have seen how to implement different types of memories. Now, let's discuss some additional considerations for building a production-ready memory system.

## Real-World Lessons: Challenges and Best Practices

The patterns we have discussed provide a solid toolkit for building agents with memory. However, moving from theory to a reliable production system requires navigating a series of complex trade-offs, especially as the underlying technology evolves so quickly. Here are some important lessons learned from building and scaling agent memory systems.

### Re-evaluating Compression

One of the biggest shifts in memory design has been the trade-off between compressing information and preserving its raw detail.

Just a couple of years ago, LLMs operated with small and expensive context windows of 8,000 or 16,000 tokens. This forced us to be ruthless with compression, distilling every interaction into compact summaries or facts to fit within the context limit. This process, however, is inherently lossy; summarizing an interaction retains the general idea but loses the fine details and nuance that are often critical for a personalized agent [[9]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

Today, with models offering million-token context windows at a fraction of the cost, the best practice is to lean towards less compression. The raw, unstructured conversation history is the ultimate source of truth [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). It contains the emotional subtext and relational dynamics that are often lost during extraction. While a semantic fact might state, "User has a dog named George," the raw log reveals, "User mentioned that walking their dog George is the best part of their day"—a far more valuable piece of information. Design your system to work with the most complete version of history that is economically and technically feasible.

### Designing for the Product

There is no "perfect" memory architecture. Semantic, episodic, and procedural memory are a powerful mental model, but they are a toolkit, not a mandatory blueprint. A common failure mode is over-engineering a complex, multi-part memory system for a product that does not need it [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

The product's goal should dictate the memory architecture, not the other way around.

-   For a Q&A bot over internal documents, a simple RAG pipeline is the best starting point.
-   For a long-term personal AI companion, rich episodic memories that capture the narrative of the relationship are beneficial.
-   For a task-automation agent, procedural memory is key, allowing the agent to recall and execute multi-step workflows.

### Trust, Safety, and the Human Factor

Memory exists to make the agent smarter, not to give the user a new job. A common pitfall is exposing the internal workings of the memory system, thinking it will improve transparency. In practice, it often creates significant cognitive overhead [[14]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112). Users should not be asked to "garden their agent's memories." It breaks the illusion of a capable assistant and turns the interaction into a tedious data-entry task.

Instead, memory management should be an autonomous function. The agent should learn from corrections within the natural flow of conversation, such as, "Actually, my brother's name is Mark, not Mike." The agent, not the user, is responsible for maintaining its own knowledge [[9]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

Furthermore, in any multi-user system, memory introduces critical safety and privacy requirements. One user’s memories must never be accessible to another. This requires strict tenant isolation at the storage and retrieval level. A simple metadata filter in your application code is not enough; a bug could leak sensitive data across users. This is a foundational requirement for any real-world deployment [[24]](https://stevekinney.com/writing/agent-memory-systems).

## Conclusion

Memory is a core component that transforms a simple, stateless chatbot into a truly adaptive and personalized agent. By implementing semantic, episodic, and procedural memory, we can build systems that store facts, recall past experiences, and learn new skills. We have learned that there is no one-size-fits-all solution; the right architecture depends on your product's specific needs, and the trade-offs between storage methods are constantly evolving with new technology.

The memory tools and patterns we have discussed are powerful engineering workarounds for the current limitations of LLMs, which lack true "continual learning." While these systems do not update their own weights, a well-designed memory architecture allows them to simulate learning, adapt to users, and grow more capable over time. However, many research gaps remain. The field is exploring challenges like memory staleness, where relevant information becomes outdated, and advanced architectures like multi-modal memory and policies trained with reinforcement learning to manage memory autonomously [[24]](https://stevekinney.com/writing/agent-memory-systems), [[20]](https://medium.com/data-unlocked/the-memory-problem-in-ai-agents-is-half-solved-heres-the-other-half-ebbf218ae4d5).

Now that we understand how to create and store different types of memories, the next step is to master how to retrieve them effectively. In Lesson 10, we will dive deep into Retrieval-Augmented Generation (RAG), exploring the techniques that power an agent's ability to pull the right information from its memory at the right time. We will also touch upon more advanced topics like building a research and writing agent and preparing them for production in future lessons.

## References

- [1] What is AI agent memory? (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-memory](https://www.ibm.com/think/topics/ai-agent-memory)
- [2] Wang, S. Y., et al. (2023). Cognitive Architectures for Language Agents. arXiv. [https://arxiv.org/html/2309.02427](https://arxiv.org/html/2309.02427)
- [3] Iusztin, P. (2025). Every AI agent has 4 distinct memory layers. LinkedIn. [https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR](https://www.linkedin.com/posts/pauliusztin_every-ai-agent-has-4-distinct-memory-layers-activity-7436765234800807936-QyLR)
- [4] Introduction to Stateful Agents. (n.d.). Letta Docs. [https://docs.letta.com/guides/agents/memory](https://docs.letta.com/guides/agents/memory)
- [5] Memory overview. (n.d.). LangGraph Docs. [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)
- [6] Memory in Agent Systems. (n.d.). SwirlAI Newsletter. [https://www.newsletter.swirlai.com/p/memory-in-agent-systems](https://www.newsletter.swirlai.com/p/memory-in-agent-systems)
- [7] Memory: The secret sauce of AI agents. (n.d.). Decoding ML. [https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents](https://decodingml.substack.com/p/memory-the-secret-sauce-of-ai-agents)
- [8] Long-term memory. (n.d.). LangGraph Docs. [https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory)
- [9] Lawson, N. (2026). A Practical Guide to Memory for Autonomous LLM Agents. Towards Data Science. [https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/)
- [10] Beyond Short-Term Memory: The 3 Types of Long-Term Memory AI Agents Need. (n.d.). Machine Learning Mastery. [https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/)
- [11] Agent Memory. (n.d.). MongoDB. [https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory)
- [12] How Does Memory for AI Agents Work? (2024). Decoding AI. [https://www.decodingai.com/p/how-does-memory-for-ai-agents-work](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)
- [13] Porras, D., & Barda, V. (2025). Memex 2.0: Memory The Missing Piece for Real Intelligence. [https://danielp1.substack.com/p/memex-20-memory-the-missing-piece](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece)
- [14] Whitmore, S. (2024). What is the perfect memory architecture? [Video]. YouTube. [https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112)
- [15] Lintvelt, H. (n.d.). Knowledge Graphs as Memory: Why Your AI Agent Needs to Think in Relationships. OctoCo. [https://www.octoco.ai/blog/knowledge-graphs-as-memory](https://www.octoco.ai/blog/knowledge-graphs-as-memory)
- [16] PlugMem: Transforming raw agent interactions into reusable knowledge. (2026). Microsoft Research. [https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/](https://www.microsoft.com/en-us/research/blog/from-raw-interaction-to-reusable-knowledge-rethinking-memory-for-ai-agents/)
- [17] How Mem0 works under the hood. (2024). [https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer](https://blog.lqhl.me/mem0-how-three-prompts-created-a-viral-ai-memory-layer)
- [18] Timestamp. (n.d.). Mem0 Docs. [https://docs.mem0.ai/platform/features/timestamp](https://docs.mem0.ai/platform/features/timestamp)
- [19] Procedural Memory from Experience Distillation for Sequential Task Completion. (2025). arXiv. [https://arxiv.org/html/2508.06433v4](https://arxiv.org/html/2508.06433v4)
- [20] The Memory Problem in AI Agents is Half-Solved. Here’s the Other Half. (n.d.). Medium. [https://medium.com/data-unlocked/the-memory-problem-in-ai-agents-is-half-solved-heres-the-other-half-ebbf218ae4d5](https://medium.com/data-unlocked/the-memory-problem-in-ai-agents-is-half-solved-heres-the-other-half-ebbf218ae4d5)
- [21] From logic to learning: The future of AI lies in neuro-symbolic agents. (n.d.). AWS Builder. [https://builder.aws.com/content/2uYUowZxjkh80uc0s2bUji0C9FP/from-logic-to-learning-the-future-of-ai-lies-in-neuro-symbolic-agents](https://builder.aws.com/content/2uYUowZxjkh80uc0s2bUji0C9FP/from-logic-to-learning-the-future-of-ai-lies-in-neuro-symbolic-agents)
- [22] From Symbolic AI to Reasoning LLMs (1950–2025). (n.d.). [https://djimit.nl/from-symbolic-ai-to-reasoning-llms-1950-2025/](https://djimit.nl/from-symbolic-ai-to-reasoning-llms-1950-2025/)
- [23] Smith, J. (n.d.). Architecting Autonomy: The Neuroscience Behind Agentic AI Systems. Medium. [https://medium.com/@jsmith0475/architecting-autonomy-the-neuroscience-behind-agentic-ai-systems-29aab6d5d131](https://medium.com/@jsmith0475/architecting-autonomy-the-neuroscience-behind-agentic-ai-systems-29aab6d5d131)
- [24] Kinney, S. (2026). Memory Systems for AI Agents: What the Research Says and What You Can Actually Build. [https://stevekinney.com/writing/agent-memory-systems](https://stevekinney.com/writing/agent-memory-systems)
- [25] Wang, G., et al. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv. [https://arxiv.org/abs/2305.16291](https://arxiv.org/abs/2305.16291)
- [26] State of AI Agent Memory 2026. (2026). Mem0 Blog. [https://mem0.ai/blog/state-of-ai-agent-memory-2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [27] Chhikara, P., et al. (2025). Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. arXiv. [https://arxiv.org/html/2504.19413](https://arxiv.org/html/2504.19413)