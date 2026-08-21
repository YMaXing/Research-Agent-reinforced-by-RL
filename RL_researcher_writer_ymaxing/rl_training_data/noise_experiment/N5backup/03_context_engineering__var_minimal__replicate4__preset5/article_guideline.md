## Global Context of the Lesson

### What We Are Planning to Share

We will write a lesson on context engineering, the core foundation of AI engineering and building AI applications. We will start by explaining why prompt engineering is not enough, and then explain why it is no longer sufficient in the world of AI. Next, we will slowly introduce the idea of context engineering, starting with a general overview and how it differs from prompt engineering. Then we will present what makes up the context passed to an LLM, key challenges in production, and tools and solutions for context engineering. Ultimately, we want to connect context engineering to the broader AI engineering field. This article is a conceptual overview; surface-level treatment is expected and depth, exhaustive coverage, or production code are explicitly NOT required.

### Why We Think It's Valuable

Context engineering is the new fine-tuning. As fine-tuning is required less and less due to the fact that it is expensive, slow, and extremely inflexible in a world where data keeps changing, fine-tuning becomes the last resort when building AI applications. Thus, context engineering becomes a core skill for building successful AI agents or LLM workflows that manage the short-term memory and long-term memory of AI applications to achieve the best performance possible.

### Expected Length of the Lesson
**~1,460 words** (without the titles and references), where we assume that 200-250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

70% theory - 30% real-world examples

## Anchoring the Lesson in the Course

### Point of View
The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Lesson Scope

This is the 3rd lesson from module 1 of a broader course on AI agents and LLM workflows.

### Who Is the Intended Audience

Aspiring AI engineers who are learning about context engineering for the first time.

### Concepts Introduced in Previous Lessons

In previous lessons, we introduced the following concepts:
- What AI agents are at a high-level (NOT how they work) (Lesson 2)
- What LLM workflows are at a high-level (NOT how they work) (Lesson 2)
- How to choose between AI agents and LLM workflows when designing your AI application (Lesson 2)

As this is only the 2nd lesson of the course, we haven't introduced too many concepts. At this point, the reader only knows what an LLM is and a few high-level ideas about the LLM workflows and AI agents landscape.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:
- structured outputs (Lesson 4)
- chaining (Lesson 5)
- routing (Lesson 5)
- orchestrator-worker (Lesson 5)
- tools (Lesson 6)
- ReAct agents (Lesson 7 and 8)
- Plan-and-Execute agents (Lesson 7)
- short-term memory (Lesson 9)
- long-term memory (Lesson 9)
    - procedural long-term memory
    - semantic long-term memory
    - episodic long-term memory
- RAG (Lesson 10)
- multimodal LLMs (Lesson 11)
- evaluations
- MCP

As context engineering is the core foundation of AI engineering, we will have to introduce new terms, but we will discuss them in a highly intuitive manner, being careful not to confuse the reader with too many terms that haven't been introduced yet in the course.

### Course Instructions
When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are.

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using it, use other intuitive and grounded explanations as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer them to as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer it to as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection, only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are just allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection explicitly specify that it will be explained in more detail in future lessons.

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we solving? Why is it essential to solve it?
	- Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger picture and next steps.

## Lesson Outline

1. When prompt engineering breaks
   Must stay brief: Evolution of AI applications, context engineering definition.
2. From prompt to context engineering
   Must stay brief: Issues with prompt engineering, personal example.
3. Understanding context engineering
   Must stay brief: Definition, Karpathy quote, prompt vs. context table, context vs. fine-tuning, decision-making workflow.
4. What makes up the context
   Must stay brief: High-level workflow, short-term memory components, long-term memory components, image illustration.
5. Production implementation challenges
   Must stay brief: Context window, information overload, context drift, tool confusion.
6. Key strategies for context optimization
   Must stay brief: Selecting context (structured outputs, RAG, tools, temporal, repeat), context compression (summaries, preferences, deduplication), isolating context (orchestrator-worker), format optimization (XML, YAML).
7. Here is an example
   Must stay brief: Real-world use cases, example query walkthrough, no production code example, simplified tech stack.
8. Connecting context engineering to AI engineering
   Must stay brief: Context engineering as an art, combination of skills.

## Section 1 - Introduction: When prompt engineering breaks
(The problem.)

- Briefly introduce the evolution of AI applications (chatbots, RAG, agents, memory-enabled agents).
- Quickly reference previous lessons and transition to what this lesson covers, highlighting its importance.
- Explain that as AI applications become complex agents and LLM workflows, context engineering (orchestrating the entire ecosystem) becomes crucial, unlike prompt engineering (single LLM calls).
- Briefly mention the exponential growth of data managed by AI applications and its impact on LLM input size (context).

- **Section length:** ~100 words

## Section 2: From prompt to context engineering
(Why it's important to solve it. Current solutions and why they are not ok.)

- Briefly discuss the issues with prompt engineering: single-interaction focus, context decay, context window limitations, and costs/latency.
- Mention that these concepts will be taught in more detail in future lessons.
- Briefly provide a real-world example of prompt engineering limitations (e.g., stuffing everything into the context window leading to poor performance).
- Explain how context engineering addresses these limitations by treating AI applications as dynamic systems managing context from various sources.

- **Section length:** ~120 words

## Section 3: Understanding context engineering
(At a theoretical level, explain our solution or transformation.)

- Define context engineering as optimizing information arrangement from memory for LLM performance. Provide a simple example (e.g., cooking agent).
- Briefly introduce the analogy: `Context as the AI's "RAM"` with a quote.
- Briefly compare prompt engineering vs. context engineering, noting prompt engineering is a subset. Include the Markdown table.
- Briefly explain context engineering vs. fine-tuning, positioning fine-tuning as a last resort.
- Include a simplified Mermaid diagram of the decision-making workflow (Prompt -> Context -> Fine-tuning).
- Briefly provide a simple example (e.g., Slack messages) where context engineering suffices.
- Reiterate that the course will focus on context engineering.

- **Section length:** ~220 words (without the mermaid diagram)

## Section 4: What makes up the context
(Go deeper into the advanced theory.)

- Briefly introduce the core elements of context.
- Explain the high-level workflow: User Input -> Memory -> Context -> Prompt Template -> Prompt -> LLM Call -> Answer -> Memory -> Repeat. Include a simplified mermaid diagram.
- Explain that these concepts will be presented intuitively at a high level.
- Briefly list and describe the categories of context components:
    - Short-term working memory (user input, message history, agent's internal thoughts, action calls/outputs).
    - Long-term memory (procedural, episodic, semantic).
- Remind the reader that these concepts will be covered in depth in future lessons.
- Briefly reference an image illustrating context components (no need to include the image itself in the guideline).
- Briefly emphasize that context components are dynamic and re-computed, and context engineering involves selecting the right ones.

- **Section length:** ~220 words

## Section 5: Production implementation challenges
(Go deeper into the advanced theory)

- Transition from definition to core challenges in implementing context engineering in production.
- Frame all challenges around keeping context small yet informative.
- Briefly present four common issues:
    1.  **The context window challenge:** Limited input size for LLMs (like RAM).
    2.  **Information overload:** Too much context reduces LLM performance ("lost-in-the-middle" problem).
    3.  **Context drift:** Conflicting information over time.
    4.  **Tool confusion:** Too many tools or poorly described tools confuse the LLM.

- **Section length:** ~180 words

## Section 6: Key strategies for context optimization
(Go deeper into the advanced theory)

- Briefly state that modern AI solutions require managing complexity across multiple knowledge bases and tools.
- Briefly present four popular context engineering strategies:
    1.  **Selecting the right context:** Briefly describe the problem of information overload and solutions like structured outputs, RAG, reducing tool count, temporal relevance, and repeating core instructions. Include a simplified mermaid diagram combining these.
    2.  **Context compression:** Briefly describe the need to manage growing message history and methods like summarization, moving preferences to long-term memory, and deduplication. Include a simplified mermaid diagram.
    3.  **Isolating Context:** Briefly explain splitting information across multiple agents/workflows, referencing the orchestrator-worker pattern and including a simplified mermaid diagram.
    4.  **Format optimization for model clarity:** Briefly mention using XML tags and preferring YAML over JSON for efficiency.
- Conclude by emphasizing the importance of understanding and monitoring context.

- **Section length:** ~280 words

## Section 7: Here is an example
(An example)

- Briefly connect theory, challenges, and strategies through concrete examples.
- Briefly list a few real-world use cases (e.g., Healthcare, Financial Services, Project Managers, Content Creator Assistant).
- Briefly walk through an example query (e.g., healthcare assistant for a headache) showing the steps: retrieve history, query literature, extract info, format, call LLM, present answer.
- Provide a very short, illustrative pseudocode snippet (under 10 lines) showing how context elements might be structured in a prompt using XML/YAML, but no full production code.
- Briefly list a simplified potential tech stack (e.g., LLM, Orchestration, Databases, Observability) without going into detail about each tool.

- **Section length:** ~220 words

## Section 8 - Conclusion - Wrap-up: Connecting context engineering to AI engineering
(Connect our solution to the bigger picture and next steps)

- Briefly summarize context engineering as an art of intuition for effective prompts and optimal context arrangement.
- Briefly explain that context engineering combines:
    1.  AI Engineering
    2.  Software Engineering (SWE)
    3.  Data Engineering
    4.  Operations (Ops)
- Briefly state the course's goal: combining these skills for production-ready AI products, fostering a shift from developers to architects.
- Briefly transition to the next lesson (structured outputs) and hint at other future topics mentioned in this lesson.

- **Section length:** ~100 words

## Brevity Requirements
- Total article length must not exceed 1,500 words. This is a hard ceiling.
- Do NOT introduce external libraries, real-world case studies, named production systems, or benchmark papers that are not already established in the course. External examples are explicitly out of scope.
- No production code examples. Pseudocode or short illustrative snippets (under 10 lines) are allowed only if the original section already implied code; otherwise omit code entirely.

## Golden Sources

1. [Context Engineering](https://blog.langchain.com/context-engineering-for-agents/)
2. [Context Engineering - What it is, and techniques to consider](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider)
3. [The rise of "context engineering"](https://blog.langchain.com/the-rise-of-context-engineering/)
4. [Context Engineering: A Guide With Examples](https://www.datacamp.com/blog/context-engineering)
5. [A Survey of Context Engineering for Large Language Models](https://arxiv.org/pdf/2507.13334)

## Other Sources

1. [+1 for "context engineering" over "prompt engineering".](https://x.com/karpathy/status/1937902205765607626)
2. [Context Engineering 101 cheat sheet](https://x.com/lenadroid/status/1943685060785524824)
3. [Own your context window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
4. [Context Engineering Guide](https://nlp.elvissaravia.com/p/context-engineering-guide)
5. [What is Context Engineering?](https://www.pinecone.io/learn/context-engineering/)