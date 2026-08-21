In the last few lessons, we've laid the foundations of AI Engineering. We explored the agent landscape, distinguished between rule-based LLM workflows and autonomous agents, and covered context engineering and structured outputs. Now, we will build on that foundation by exploring the fundamental patterns for creating multi-step LLM workflows.

This lesson tackles a core challenge: moving beyond single, monolithic LLM calls to build robust, modular, and dynamic systems. We will explore chaining, parallelization, routing, and the orchestrator-worker pattern. By the end, you will understand how to break down complex problems into manageable steps, an essential skill for shipping reliable AI applications.

## The Challenge with Complex Single LLM Calls

When building with LLMs, it’s tempting to create a single, complex prompt that handles everything. You give the model a long list of instructions and hope for the best. While this can work for simple demos, it quickly falls apart in production.

A single, large LLM call is problematic for several reasons. First, it’s a black box. When something goes wrong, it is difficult to pinpoint the source of the error. Second, it lacks modularity, making it hard to update or improve one part of the logic without affecting everything else. Complex prompts are also more likely to suffer from the "lost-in-the-middle" problem, where models ignore instructions buried in a long context. Models tend to remember information best at the beginning and end, often overlooking what's in between. [[2]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2) This leads to higher token costs and less reliable outputs. [[1]](https://www.mdpi.com/2079-9292/13/23/4712)

Let's look at a practical example. Suppose we want to generate a Frequently Asked Questions (FAQ) page from a few documents about renewable energy.

1.  First, we set up our environment and define our model. We will use Google's Gemini API throughout this lesson.
    ```python
    from lessons.utils import env
    from google import genai

    env.load(required_env_vars=["GOOGLE_API_KEY"])

    client = genai.Client()
    MODEL_ID = "gemini-2.5-flash"
    ```

2.  We have three mock webpages on solar, wind, and energy storage. We combine their content into a single string for the LLM to process.
    ```python
    webpage_1 = {
        "title": "The Benefits of Solar Energy",
        "content": "Solar energy is a renewable powerhouse...",
    }
    # ... (webpage_2 and webpage_3 are defined similarly)

    all_sources = [webpage_1, webpage_2, webpage_3]
    combined_content = "\n\n".join(
        [f"Source Title: {source['title']}\nContent: {source['content']}" for source in all_sources]
    )
    ```

3.  Now, we create a complex prompt that asks the model to generate questions, find answers, and cite sources all in one go.
    ```python
    n_questions = 10
    prompt_complex = f"""
    Based on the provided content from three webpages, generate a list of exactly {n_questions} frequently asked questions (FAQs).
    For each question, provide a concise answer derived ONLY from the text.
    After each answer, you MUST include a list of the 'Source Title's that were used to formulate that answer.

    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()

    response_complex = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt_complex,
        # ... (config for structured output)
    )
    ```
    It outputs:
    ```json
    {
        "question": "What is solar energy and how does it work?",
        "answer": "Solar energy is a renewable powerhouse that converts sunlight into electricity through photovoltaic (PV) panels.",
        "sources": [
          "The Benefits of Solar Energy"
        ]
    }
    ```

While this output looks reasonable, a single prompt struggles as complexity grows. For instance, the model might fail to identify all relevant sources for an answer drawn from multiple documents. This is a classic failure mode. The more instructions you pack into one prompt, the higher the chance of inaccuracies.

## The Power of Modularity: Why Chain LLM Calls?

A more reliable approach is to break the task down using prompt chaining. This involves connecting multiple LLM calls sequentially, where the output of one step becomes the input for the next. [[3]](https://www.promptingguide.ai/techniques/prompt_chaining) It’s a simple "divide-and-conquer" strategy that makes complex tasks more manageable.

This modular approach offers several benefits:
-   **Improved Modularity:** Each LLM call focuses on a specific, well-defined sub-task, making the system easier to build and maintain. [[4]](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
-   **Enhanced Accuracy:** Simpler, targeted prompts generally lead to more reliable outputs.
-   **Easier Debugging:** You can isolate issues to a specific link in the chain instead of trying to debug one giant prompt.
-   **Increased Flexibility:** Individual components can be swapped or optimized independently. For example, you could use a fast, cheap model for a simple classification step and a more powerful model for content generation.

However, chaining is not a silver bullet. It introduces higher latency due to multiple sequential API calls, which can also increase costs and engineering complexity. You have to manage state and handle errors between steps, which can lead to cascading failures if not handled carefully. [[5]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production) There is also a risk of information loss, as splitting tasks can sometimes remove the context that connects them, leading to a less coherent final output.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's apply prompt chaining to our FAQ generation task. We will split it into a three-step workflow that is much more reliable and easier to debug:
1.  Generate a list of questions.
2.  For each question, generate an answer.
3.  For each question-answer pair, identify the sources.

This workflow ensures each step is focused and produces a clean output for the next stage.

Image 1: A flowchart illustrating a sequential FAQ generation pipeline.
```mermaid
flowchart LR
  "Input Content" --> "Generate Questions"
  "Generate Questions" --> "Answer Questions"
  "Answer Questions" --> "Find Sources"
```

This process begins by creating a function dedicated to generating questions. The prompt is simple: it takes the content and asks for a list of questions. This isolates the task of question generation, ensuring we have a clear set of topics to cover before diving into details.

1.  The `generate_questions` function focuses solely on creating relevant questions based on the provided material.
    ```python
    def generate_questions(content: str, n_questions: int = 10) -> list[str]:
        """
        Generate a list of questions based on the provided content.
        """
        prompt_generate_questions = f"""
        Based on the content below, generate a list of {n_questions} relevant and distinct questions that a user might have.

        <provided_content>
        {content}
        </provided_content>
        """.strip()
        # ... (API call with structured output config for QuestionList)
        return response_questions.parsed.questions
    ```

2.  Next, the `answer_question` function takes a single question and the source content, with a clear instruction to answer concisely using only the provided text. This focus on a single, targeted query improves accuracy.
    ```python
    def answer_question(question: str, content: str) -> str:
        """
        Generate an answer for a specific question using only the provided content.
        """
        prompt_answer_question = f"""
        Using ONLY the provided content below, answer the following question.
        The answer should be concise and directly address the question.

        <question>
        {question}
        </question>

        <provided_content>
        {content}
        </provided_content>
        """.strip()
        # ... (API call)
        return answer_response.text
    ```

3.  Finally, the `find_sources` function identifies which sources were used for a given answer. This step is important for traceability and grounding the model's responses in the provided text.
    ```python
    def find_sources(question: str, answer: str, content: str) -> list[str]:
        """
        Identify which sources were used to generate an answer.
        """
        prompt_find_sources = f"""
        You will be given a question and an answer that was generated from a set of documents.
        Your task is to identify which of the original documents were used to create the answer.

        <question>
        {question}
        </question>

        <answer>
        {answer}
        </answer>

        <provided_content>
        {content}
        </provided_content>
        """.strip()
        # ... (API call with structured output config for SourceList)
        return sources_response.parsed.sources
    ```

4.  We combine these functions into a `sequential_workflow` that orchestrates the entire process. It iterates through each generated question, answers it, and finds the sources, creating a pipeline that is both logical and easy to debug.
    ```python
    def sequential_workflow(content, n_questions=4) -> list:
        """
        Execute the complete sequential workflow for FAQ generation.
        """
        questions = generate_questions(content, n_questions)
        final_faqs = []
        for question in questions:
            answer = answer_question(question, content)
            sources = find_sources(question, answer, content)
            final_faqs.append({"question": question, "answer": answer, "sources": sources})
        return final_faqs

    # Execute the sequential workflow
    import time
    start_time = time.monotonic()
    sequential_faqs = sequential_workflow(combined_content)
    end_time = time.monotonic()
    ```
    It outputs:
    ```text
    Sequential processing completed in 22.20 seconds
    ```

This chained approach gives us more control and visibility at each step. While it took over 20 seconds to run, the modularity makes it more robust than the single-prompt method.

## Optimizing Sequential Workflows With Parallel Processing

The sequential workflow is reliable but slow. Since the processing for each question is independent of the others, we can run these steps in parallel to significantly reduce latency. [[6]](https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/)

We can refactor our workflow using Python's `asyncio` library to process the questions concurrently. LLM API calls are I/O-bound tasks, meaning they spend most of their time waiting for a network response rather than performing heavy computation. This makes them perfect candidates for asynchronous execution. `asyncio` uses an event loop to manage these concurrent tasks efficiently, allowing the program to work on other operations while waiting for network responses, rather than blocking execution. [[7]](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python) [[8]](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a)

1.  First, we define an asynchronous function that processes a single question by generating its answer and finding its sources. This function will be the unit of work for our parallel execution.
    ```python
    async def process_question_parallel(question: str, content: str) -> dict:
        """
        Process a single question by generating answer and finding sources in parallel.
        """
        answer = await answer_question_async(question, content) # async version of answer_question
        sources = await find_sources_async(question, answer, content) # async version of find_sources
        return {"question": question, "answer": answer, "sources": sources}
    ```

2.  Then, we create a parallel workflow that generates all questions first and then processes them concurrently using `asyncio.gather`, which runs multiple awaitable objects simultaneously.
    ```python
    async def parallel_workflow(content: str, n_questions: int = 4) -> list:
        """
        Execute the complete parallel workflow for FAQ generation.
        """
        questions = generate_questions(content, n_questions)
        tasks = [process_question_parallel(question, content) for question in questions]
        parallel_faqs = await asyncio.gather(*tasks)
        return parallel_faqs

    # Execute the parallel workflow
    start_time = time.monotonic()
    parallel_faqs = await parallel_workflow(combined_content)
    end_time = time.monotonic()
    ```
    It outputs:
    ```text
    Parallel processing completed in 8.98 seconds
    ```

By running the tasks in parallel, we cut the execution time from 22 seconds to just 9 seconds. This demonstrates the trade-off: parallel processing is faster and utilizes resources better, but it adds complexity to error handling. Furthermore, making many concurrent calls can trigger API rate limits. For example, free tiers often limit requests per minute. Running ten calls in parallel could exhaust your entire minute's quota in a single second, leading to errors that your application must handle gracefully. [[9]](https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903)

## Introducing Dynamic Behavior: Routing and Conditional Logic

So far, our workflows have been static. Every input goes through the same sequence of steps. But what if the required processing path needs to change based on the input? This is where routing comes in.

Routing uses conditional logic to direct an input down a specialized path, another application of the "divide-and-conquer" principle. [[4]](https://www.decodingai.com/p/stop-building-ai-agents-use-these) Instead of a single, monolithic prompt trying to handle every possible scenario, you create specialized prompts for different cases. An LLM itself can act as a classifier, analyzing the input and deciding which path to take. Trying to optimize a single prompt to handle both billing and technical support queries would likely degrade performance on both, as the instructions would become convoluted. This ensures each component in your system has a single, focused responsibility, which improves both performance and maintainability.

## Building a Basic Routing Workflow

A classic use case for routing is a customer service system, where different user intents trigger entirely different backend processes. Queries about billing, technical issues, and general questions all require different responses and actions. We can build a simple router that first classifies the user's intent and then directs the query to a specialized handler. This ensures that each type of query receives the most appropriate and effective response.

Image 2: A flowchart illustrating a routing workflow for customer service intent classification.
```mermaid
graph TD
    A["User Input"] --> B{"Intent Classification"}
    B -->|"Technical"| C["Technical Support"]
    B -->|"Billing"| D["Billing Inquiry"]
    B -->|"General"| E["General Question"]
    C --> F["Final Responses"]
    D --> F
    E --> F
```

1.  First, we define a function that uses the LLM to classify the user's intent. We provide a list of possible categories to guide the model, ensuring the classification is constrained to our defined intents.
    ```python
    def classify_intent(user_query: str) -> str:
        """Uses an LLM to classify a user query."""
        categories = ["Technical Support", "Billing Inquiry", "General Question"]
        prompt = f"""
        Classify the user's query into one of the following categories.

        <categories>
        {categories}
        </categories>

        <user_query>
        {user_query}
        </user_query>
        """.strip()
        # ... (API call with structured output for UserIntent)
        return response.parsed.intent
    ```

2.  Next, we define specialized prompts for each intent, each tailored to a specific type of query.
    ```python
    prompt_technical_support = "You are a helpful technical support agent..."
    prompt_billing_inquiry = "You are a helpful billing support agent..."
    prompt_general_question = "You are a general assistant..."
    ```

3.  Finally, we create a handler function that routes the query based on the classified intent. This function acts as the control flow mechanism, directing the input to the correct logic path. The `else` block serves as a crucial fallback route, ensuring the system can handle unexpected or unclassified inputs gracefully.
    ```python
    def handle_query(user_query: str, intent: str) -> str:
        """Routes a query to the correct handler based on its classified intent."""
        if intent == "Technical Support":
            prompt = prompt_technical_support.format(user_query=user_query)
        elif intent == "Billing Inquiry":
            prompt = prompt_billing_inquiry.format(user_query=user_query)
        else: # Default/fallback
            prompt = prompt_general_question.format(user_query=user_query)
        
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    ```
    For a query like "My internet connection is not working," the system first classifies the intent as "Technical Support" and then uses the specialized technical support prompt to generate a helpful first response. This keeps each part of the system simple and focused.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The patterns we've seen so far—chaining, parallelization, and routing—are powerful, but they often rely on pre-defined steps. The orchestrator-worker pattern takes this a step further by introducing a central LLM, the "orchestrator," that dynamically breaks down a complex task into subtasks and delegates them to specialized "worker" LLMs. [[10]](https://agents.kour.me/orchestrator-worker/)

This workflow is perfect for complex problems where the required steps are unpredictable. [[11]](https://www.anthropic.com/engineering/building-effective-agents) The key difference from simple parallelization is its flexibility: the orchestrator determines the subtasks at runtime based on the specific input. After the workers complete their tasks, a "synthesizer" can combine their outputs into a single, coherent response.

Image 3: A flowchart illustrating the orchestrator-worker pattern.
```mermaid
flowchart LR
  %% Initial Task Reception
  A["Complex Task"] --> B["Orchestrator"]

  %% Task Decomposition
  B -- "breaks down into" --> C["Sub-tasks"]

  %% Parallel Worker Execution
  subgraph "Worker LLMs (Specialized Workers)"
    direction LR
    C -- "delegates to" --> W1["Worker LLM 1"]
    C -- "delegates to" --> W2["Worker LLM 2"]
    C -- "delegates to" --> WN["Worker LLM N"]
  end

  %% Results Collection
  W1 -- "returns results" --> R["Results"]
  W2 -- "returns results" --> R
  WN -- "returns results" --> R

  %% Final Synthesis and Output
  R -- "synthesizes" --> B
  B -- "produces" --> F["Final Result"]
```

Let's illustrate this with a complex customer service query that requires multiple actions.

1.  A user sends a query that involves a billing question, a product return, and an order status update.
    ```python
    complex_customer_query = """
    Hi, I have a question about invoice #INV-7890. It seems higher than I expected.
    Also, I would like to return the 'SuperWidget 5000' because it's not compatible with my system.
    Finally, can you give me an update on my order #A-12345?
    """.strip()
    ```

2.  The orchestrator LLM analyzes this query and breaks it down into a structured list of tasks for the workers.
    ```python
    def orchestrator(query: str) -> list:
        """Breaks down a complex query into a list of tasks."""
        # ... (prompt instructs the LLM to identify sub-tasks and parameters)
        # ... (API call with structured output for TaskList)
        return response.parsed.tasks
    
    tasks_list = orchestrator(complex_customer_query)
    ```
    The orchestrator identifies three distinct tasks: a `BillingInquiry`, a `ProductReturn`, and a `StatusUpdate`, each with the necessary parameters extracted from the query.

3.  Each task is then dispatched to a specialized worker function (`handle_billing_worker`, `handle_return_worker`, `handle_status_worker`). These workers simulate interacting with backend systems (e.g., opening an investigation, generating an RMA number, fetching order status) and return structured results.

4.  Finally, the synthesizer LLM takes the structured outputs from all workers and composes a single, user-friendly email that addresses all parts of the original query.
    ```python
    def synthesizer(results: list) -> str:
        """Combines structured results from workers into a single user-facing message."""
        # ... (prompt combines worker results into a cohesive summary)
        # ... (API call)
        return response.text
    
    final_user_message = synthesizer(worker_results)
    ```
    The final response consolidates all actions into one clear message, demonstrating how the orchestrator-worker pattern can handle multifaceted and unpredictable requests in a structured and scalable way.

## Conclusion

In this lesson, we moved from the limitations of single, complex prompts to the power of modular LLM workflows. We've seen how to build more reliable and efficient systems by breaking down tasks using four fundamental patterns:

1.  **Prompt Chaining:** For tasks with clear, sequential steps.
2.  **Parallelization:** To speed up the processing of independent subtasks.
3.  **Routing:** To direct inputs to specialized handlers based on conditional logic.
4.  **Orchestrator-Worker:** For dynamically decomposing complex, unpredictable tasks.

These patterns are not just theoretical concepts; they are the practical building blocks for almost any production-grade AI application. They provide the control, reliability, and modularity needed to move beyond simple demos.

As you continue your journey as an AI Engineer, you will find yourself combining these patterns to create sophisticated systems. In our next lesson, we will take another big step forward by learning how to give our workflows the ability to interact with the outside world using tools and function calling.

## References

- [1] M. Gozzi and F. Di Maio, “Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts,” Electronics, vol. 13, no. 23, p. 4712, Nov. 2024. [https://www.mdpi.com/2079-9292/13/23/4712](https://www.mdpi.com/2079-9292/13/23/4712)
- [2] The "Lost in the Middle" Problem — Why LLMs Ignore the Middle of Your Context Window. (2026). dev.to. [https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [3] Prompt Chaining Guide. (2024). promptingguide.ai. [https://www.promptingguide.ai/techniques/prompt_chaining](https://www.promptingguide.ai/techniques/prompt_chaining)
- [4] Stop Building AI Agents. Use These Workflow Patterns Instead. (2024). decodingai.com. [https://www.decodingai.com/p/stop-building-ai-agents-use-these](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [5] How Tool Chaining Fails in Production LLM Agents and How to Fix It. (2026). futureagi.substack.com. [https://futureagi.substack.com/p/how-tool-chaining-fails-in-production](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production)
- [6] Orchestrating Multi-Step LLM Chains: Best Practices. (2024). deepchecks.com. [https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/](https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/)
- [7] Asynchronous or Concurrency Patterns in Python with Asyncio. (2024). santhalakshminarayana.github.io. [https://santhalakshminarayana.github.io/blog/concurrency-patterns-python](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python)
- [8] Python Concurrency Showdown: Asyncio vs. Threading vs. Multiprocessing. (2024). medium.com. [https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a)
- [9] “Challenges with rate limiting and handling API responses in high volume requests,” Google AI Community, 2024. [https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903](https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903)
- [10] Pattern: Orchestrator-Worker (Coordinator). (2024). agents.kour.me. [https://agents.kour.me/orchestrator-worker/](https://agents.kour.me/orchestrator-worker/)
- [11] Building effective agents. (2024). anthropic.com. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)