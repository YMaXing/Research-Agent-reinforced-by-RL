# How Does Memory for AI Agents Work?

In the previous lessons, we covered the agentic landscape, context engineering, structured outputs, and the reasoning mechanisms that power AI agents like ReAct. We have the building blocks to create agents that can plan and use tools. Now, we will explore one of the most important components that transforms a simple, stateless chatbot into an adaptive and personalized system: memory.

The core problem we are solving is the limitation of LLMs: their knowledge is vast but frozen in time. They are unable to learn by updating their weights after training, a problem known as “continual learning” [[1]](https://arxiv.org/html/2510.17281v2). An LLM without memory is like an intern with amnesia. They might be brilliant, but they cannot recall previous conversations or learn from experience.

To overcome this, we use the context window as a form of “working memory.” However, keeping an entire conversation in the context window is often unrealistic. Rising costs per turn and the “lost in the middle” problem—where models struggle to use information buried in a long prompt—limit this approach [[2]](https://arxiv.org/abs/2307.03172). While context windows are increasing, relying solely on them introduces noise and overhead. Memory tools act as the solution, providing agents with continuity and the ability to “learn” without retraining.

In this article, we will explore the three fundamental layers of memory, look at the different types of long-term memory, discuss the trade-offs of various storage methods, implement them with code, and cover real-world challenges and best practices. To build agents effectively, we need a useful way to think about memory. We can borrow from biology and cognitive science to understand how memory works across different time horizons.

## The Layers of Memory: Internal, Short-Term, and Long-Term

To build effective agents, we can borrow terms from biology and cognitive science to categorize memory layers, which is useful for engineering [[3]](https://www.ibm.com/think/topics/ai-agent-memory), [[4]](https://arxiv.org/html/2309.02427).

**Internal Knowledge** is the static, pre-trained knowledge baked into the LLM’s weights. It is the best place to store general world knowledge but is frozen at the time of training.

**Short-Term Memory** is the active context window, acting as the RAM of the agentic system. It is volatile and fast, simulating “learning” during a session.

**Long-Term Memory** is the external, persistent storage (the disk) where an agent saves and retrieves information, providing personalization and context.

```mermaid
flowchart LR
  %% Memory Layers
  subgraph "AI Agent Memory System"
    IK["Internal Knowledge<br/>(Core)"]
    STM["Short-Term Memory<br/>(Context Window/Agent RAM)"]
    LTM["Long-Term Memory<br/>(External Persistent Storage/Agent Disk)"]
  end

  %% Reasoning and Output
  subgraph "Reasoning & Action"
    LLM["Large Language Model"]
    Output["Agent Output<br/>(Response/Action)"]
  end

  %% Primary Data Flows
  LTM -- "Retrieval Pipeline" --> STM
  STM -- "Curate Context" --> LLM
  LLM -- "Generate Output" --> STM
  LLM -- "Produce" --> Output

  %% Interplay and Feedback
  IK -. "Informs/Guides" .-> STM
  IK -. "Informs/Guides" .-> LLM
  STM -- "Update/Persist" --> LTM

  %% Visual Grouping
  classDef memory stroke-dasharray:3,3
  classDef process stroke-width:2px
  class IK,STM,LTM memory
  class LLM,Output process
```
Image 1: A hierarchy and flow diagram illustrating the three fundamental layers of an AI agent's memory system: Internal Knowledge, Short-Term Memory, and Long-Term Memory, showing their dynamic interplay and filtering hierarchy.

The dynamic between these layers creates the agent’s intelligence. Information from long-term memory is retrieved into short-term memory, which is then curated to create the final context for the LLM. This categorization is critical for engineering: internal knowledge handles general reasoning, short-term memory manages the immediate task, and long-term memory provides personalization.

## Long-Term Memory: Semantic, Episodic, and Procedural

Long-term memory is not a single bucket of text. It consists of three distinct types, each serving a different role in making an agent “intelligent” [[4]](https://arxiv.org/html/2309.02427), [[5]](https://www.newsletter.swirlai.com/p/memory-in-agent-systems).

### Semantic Memory (Facts & Knowledge)

Semantic memory is the agent’s encyclopedia. It stores atomic facts, like *“The user is a vegetarian,”* or structured attributes on an entity, such as `{"food_restrictions": "vegetarian"}`. For an enterprise agent, this might be internal documents. For a personal assistant, semantic memory builds a persistent user profile, recalling preferences like `{"music": "rock"}`. This allows the agent to retrieve relevant facts without searching through a noisy conversation history.

### Episodic Memory (Experiences & History)

Episodic memory is the agent’s personal diary. It records past interactions with a timestamp, capturing *“what happened and when.”* This is essential for maintaining conversational context. A semantic fact might be *“User is frustrated with his brother.”* An episodic memory would be: *“On Tuesday, the user expressed frustration that their brother, Mark, always forgets their birthday. [created_at=2025-08-25].”* This nuanced episode allows the agent to interact with more empathy in the future and answer questions like *“What happened last week?”* [[6]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

### Procedural Memory (Skills & How-To)

Procedural memory is the agent’s muscle memory of skills and learned workflows. This memory is often baked into the agent’s system prompt as reusable tools. For example, an agent might store a `MonthlyReportIntent` procedure. When a user asks for a report, the agent retrieves this procedure: 1) Query sales DB, 2) Summarize findings, 3) Email user. This makes behavior reliable and predictable, as the agent does not have to reason from scratch every time [[7]](https://arxiv.org/html/2508.06433v2).

Now that we know what to save, we must decide *how* to store it.

## Storing Memories: Pros and Cons of Different Approaches

The way an agent’s memories are stored is an architectural decision that impacts performance, complexity, and scalability. There is no one-size-fits-all solution. Let’s explore the three primary methods we experiment with as AI Engineers.

### Storing Memories as Raw Strings

This is the simplest method. Conversational turns are stored as plain text and indexed for vector search.

**Pros:** It is simple and fast to set up. It also preserves nuance, capturing emotional tone without loss in translation.

**Cons:** Retrieval is often imprecise. A query like “What is my brother’s job?” might retrieve every conversation mentioning “brother” and “job” without pinpointing the current fact [[8]](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work). Updating is difficult; a correction just adds another string to the log, creating potential contradictions.

### Storing Memories as Entities (JSON-like Structures)

Here, we use an LLM to transform messy interactions into structured memories, stored in formats like JSON.

**Pros:** It allows for precise, field-level filtering (e.g., `{"user": {"brother": {"job": "Software Engineer"}}}`). Updates are easier, as you simply overwrite the relevant field.

**Cons:** It requires upfront schema design and can be rigid [[9]](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece). The extraction process can also strip away the nuance of the original conversation. The memory `"user_likes": ["cats"]` is far less representative than, "Petting my cat is the best part of my day."

### Storing Memories in a Knowledge Graph

This is the most advanced approach. Memories are stored as a network of nodes (entities) and edges (relationships).

**Pros:** It excels at representing complex relationships (e.g., `(User) -> [HAS_BROTHER] -> (Mark)`). It offers superior contextual awareness by modeling time as a property of a relationship [[10]](https://www.octoco.ai/blog/knowledge-graphs-as-memory).

**Cons:** It has the highest complexity and cost. For simple use cases, it is often overkill [[11]](https://arxiv.org/html/2504.19413).

```mermaid
graph TD
    subgraph "Storing Memories"
        direction LR
        A[Unstructured Text: "My brother Mark is now a doctor."]

        subgraph "1. Raw Strings"
            A --> B[Vector DB<br/>'My brother Mark is now a doctor.']
        end

        subgraph "2. Entities (JSON)"
            A -- "LLM Extract" --> C[Document DB<br/>{ "brother": { "name": "Mark", "job": "doctor" } }]
        end

        subgraph "3. Knowledge Graph"
            A -- "LLM Extract" --> D[Graph DB<br/>(Mark) -[:IS_A]-> (Doctor)<br/>(User) -[:HAS_BROTHER]-> (Mark)]
        end
    end
```
Image 2: A diagram visualizing the three primary approaches to storing memories, from unstructured text to structured formats in different database types.

A key challenge across all storage methods is the "human factor" of memory updates and conflict resolution. Memory management should be an autonomous function of the agent, which learns from corrections in conversation rather than asking the user to "garden their memories" [[6]](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112).

## Memory Implementations with Code Examples

Now that we know what to save and how to store it, let's look at some code examples. We will use `mem0`, an open-source memory library, to demonstrate a simple "raw string" storage approach for each memory type. `mem0` provides a memory layer that can work with different storage backends, from simple vector stores to more complex graph databases, automating the pipeline from text input to retrievable memories.

### Setup

First, we need to set up our environment. We will use `mem0` with Google's Gemini for embeddings and a local ChromaDB vector store.

1.  We configure `mem0` to use Gemini for both the LLM and embeddings, and ChromaDB for local vector storage.

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
    ```

2.  Next, we define helper functions to add and search for memories. `mem_add_text` stores a string verbatim with a category tag, and `mem_search` is a wrapper for querying memories.

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
        """Category-aware search wrapper."""
        res = memory.search(query, user_id=MEM_USER_ID, limit=limit) or {}
    
        items = res.get("results", [])
        if category is not None:
            items = [r for r in items if (r.get("metadata") or {}).get("category") == category]
        return items
    ```

### Semantic Memory: Extracting Facts

Semantic memory is created through an extraction pipeline. An LLM is prompted to extract atomic facts from a conversation. For a personal assistant, the prompt might look like this:

```
Extract persistent facts and strong preferences as short bullet points.
- Keep each fact atomic and context-independent.
- 3–6 bullets max.

Text:
{My brother Mark is a software engineer, but his real passion is painting.}
```

This would create memories like: `Mark is the user's brother.`, `Mark is a software engineer.`, and `Mark's real passion is painting.`. Retrieval then uses hybrid search, combining keyword filters with semantic similarity to find the most relevant fact.

1.  We insert a few facts about a user into our semantic memory.

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

2.  We can now search for this specific information using a natural language query.

    ```python
    results = memory.search("brother job", user_id=MEM_USER_ID, limit=1)
    print(results["results"][0]["memory"])
    ```

    It outputs:

    ```text
    User's brother is named Mark and is a software engineer.
    ```

### Episodic Memory: The Log of Events

Episodic memories function as a chronological log. They can be created by having an LLM summarize events from a conversation, which are then stored with a timestamp. For example, given the input `User: "I'm feeling stressed about my project deadline on Friday."`, a raw memory would be the log itself, while a summarized memory might be `October 26th, 2025: User is stressed about their project deadline on Friday and the assistant offers to help.`. Retrieval combines temporal filters (e.g., "yesterday") with semantic search.

1.  We define a short dialogue and ask the LLM to summarize it into a single "episode."

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
    ```

2.  We save this summary as an episodic memory.

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

3.  We can search for this "experience" later.

    ```python
    hits = mem_search("deadline stress", limit=1, category="episodic")
    for h in hits:
        print(f"{h['memory']}\n")
    ```

    It outputs:

    ```text
    A user, stressed about a Friday project deadline because of testing and a preference for working at night, is advised to split the testing work into two manageable sessions.
    ```

### Procedural Memory: Defining and Learning Skills

Procedural memory can be developer-defined or learned from user instructions. An agent can be prompted to convert a user's step-by-step instructions into a reusable procedure. For example:

```
User Input: "To book a cabin: 1. Search CabinRentals.com. 2. Filter for mountain locations. 3. Check July availability. 4. Send me top 3 options."
```

The agent would learn a new procedure named `find_summer_cabin`. Retrieval is an intent-matching process where the LLM compares a user's request to the descriptions of all available procedures and executes the best match.

1.  We define the procedure as a text block containing steps and save it.

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

2.  We can then retrieve this procedure by searching for its intent.

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

## Real-World Lessons: Challenges and Best Practices

Moving from theory to a production-ready system requires navigating complex trade-offs that are constantly evolving. Here are some important lessons learned from building agent memory systems.

### Re-evaluating Compression

The trade-off between compressing information and preserving raw detail has shifted dramatically. Just a few years ago, models with small 8k or 16k token context windows forced us to be ruthless with compression. This process, often called **summarization drift** or **context compaction**, is inherently lossy; each compression discards details, and eventually, the agent’s memory no longer matches what happened [[13]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/), [[17]](https://dev.to/bobrenze/why-ai-agent-memory-systems-fail-in-production-and-how-i-fixed-mine-141d). Today, with million-token context windows, the best practice is to lean towards less compression. The raw conversational history is the ultimate source of truth, containing nuance that extraction often discards.

### Designing for the Product

There is no "perfect" memory architecture. The concepts of semantic, episodic, and procedural memory are a toolkit, not a mandatory blueprint. The product's goal should dictate the memory architecture. For a Q&A bot over internal documents, a simple retrieval system is a great start. For a long-term personal AI companion, rich episodic memories are valuable. For a task-automation agent, procedural memory is likely key. Start from first principles by defining the core function of your agent.

### Knowledge Integrity Failures

Beyond the human factor, several other failure modes are common. **Staleness** occurs when the agent’s memory does not reflect changes in the real world. **Self-reinforcing errors** happen when an incorrect memory is treated as ground truth, poisoning future decisions. And **contradiction handling** is often poor; if new information conflicts with old, an agent may oscillate between two beliefs instead of resolving the conflict [[13]](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/).

## Conclusion

Memory is the component that transforms a stateless chat application into a personalized agent. It is the current engineering solution to the problem of continual learning. By constantly engineering the context window, we allow agents to “learn” and adapt over time. While today's memory tools are a temporary solution for true continual learning, they are a powerful and necessary part of building effective AI systems that can be used today.

This lesson provided a conceptual overview of agent memory. In our next lesson, we will do a deep dive into Retrieval-Augmented Generation, the core mechanism for pulling information from long-term memory. We will also explore more advanced topics in the future, including multimodal data processing for images, audio, and video, as well as the Model Context Protocol (MCP) for standardized tool use. Later in the course, we will apply these concepts to build out our research and writing agents, and finally, cover how to monitor and evaluate them in production. This will give you all the tools needed to ship production-ready agents.

## References

- [1] Wang, L., Zhang, X., Su, H., & Zhu, J. (2025). A Comprehensive Survey of Continual Learning. arXiv preprint arXiv:2302.00487. [https://arxiv.org/html/2510.17281v2](https://arxiv.org/html/2510.17281v2)
- [2] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv preprint arXiv:2307.03172. [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)
- [3] What is AI agent memory?. (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-memory](https://www.ibm.com/think/topics/ai-agent-memory)
- [4] Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2023). Cognitive Architectures for Language Agents. arXiv. [https://arxiv.org/html/2309.02427](https://arxiv.org/html/2309.02427)
- [5] Griciūnas, A. (2024, October 30). Memory in Agent Systems. SwirlAI Newsletter. [https://www.newsletter.swirlai.com/p/memory-in-agent-systems](https://www.newsletter.swirlai.com/p/memory-in-agent-systems)
- [6] Whitmore, S. (2025, June 18). What is the perfect memory architecture?. YouTube. [https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112](https://www.youtube.com/watch?v=7AmhgMAJIT4&list=PLDV8PPvY5K8VlygSJcp3__mhToZMBoiwX&index=112)
- [7] Mem^p: A Framework for Procedural Memory in Agents. (n.d.). arXiv. [https://arxiv.org/html/2508.06433v2](https://arxiv.org/html/2508.06433v2)
- [8] Iusztin, P. (2025, Dec 02). How Does Memory for AI Agents Work?. Decoding AI Magazine. [https://www.decodingai.com/p/how-does-memory-for-ai-agents-work](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)
- [9] Chalef, D. (2024, June 25). Memex 2.0: Memory The Missing Piece for Real Intelligence. Substack. [https://danielp1.substack.com/p/memex-20-memory-the-missing-piece](https://danielp1.substack.com/p/memex-20-memory-the-missing-piece)
- [10] Lintvelt, H. (n.d.). Knowledge Graphs as Memory: Why Your AI Agent Needs to Think in Relationships. Octo AI. [https://www.octoco.ai/blog/knowledge-graphs-as-memory](https://www.octoco.ai/blog/knowledge-graphs-as-memory)
- [11] Chhikara, P. (2025). Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. arXiv. [https://arxiv.org/html/2504.19413](https://arxiv.org/html/2504.19413)
- [12] Kosoy, D., et al. (2026). The Foundation of Autonomous Agents. arXiv. [https://arxiv.org/html/2602.10479v1](https://arxiv.org/html/2602.10479v1)
- [13] Lawson, N. (2026, April 17). A Practical Guide to Memory for Autonomous LLM Agents. Towards Data Science. [https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/)
- [14] What is AI agent memory?. (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-memory](https://www.ibm.com/think/topics/ai-agent-memory)
- [15] Chen, S., et al. (2025). ReMe: From Blind Trial-and-error to Strategic Experience Reuse. arXiv. [https://arxiv.org/html/2512.10696](https://arxiv.org/html/2512.10696)
- [16] Pan, Z., et al. (2026). Unifying Long-term Context for Large Language Models with Graph-based Memory. arXiv. [https://arxiv.org/html/2605.02452v1](https://arxiv.org/html/2605.02452v1)
- [17] Bob R. (2026, May 22). Why AI Agent Memory Systems Fail in Production (And How I Fixed Mine). DEV Community. [https://dev.to/bobrenze/why-ai-agent-memory-systems-fail-in-production-and-how-i-fixed-mine-141d](https://dev.to/bobrenze/why-ai-agent-memory-systems-fail-in-production-and-how-i-fixed-mine-141d)
- [18] Chen, Z., et al. (2026). TeleMem: A Unified Long-Term Memory for Text-based and Multimodal Telescopic Agents. arXiv. [https://arxiv.org/html/2601.06037v1](https://arxiv.org/html/2601.06037v1)