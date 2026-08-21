# Stop Building Monolithic LLM Calls. Use These 4 Workflow Patterns Instead.

In our last few lessons, we have laid the foundation for AI Engineering. We explored the agent landscape, distinguished between rule-based workflows and autonomous agents, and covered context engineering. Now, we will tackle a fundamental challenge: building reliable, multi-step applications by moving beyond single, monolithic LLM calls.

Many engineers starting with LLMs fall into the trap of writing a single, massive prompt that tries to do everything at once. We have been there. On an early project, we tried to build a system that would take a long technical document, generate a summary, extract key entities, create a list of FAQs, and format everything into a single JSON object—all in one go. The result was a mess of inconsistent outputs, high latency, and a debugging nightmare.

This is a common failure mode. While it’s tempting to throw a complex task at a powerful model and hope for the best, this approach is brittle and doesn’t scale. Production-grade AI requires a more structured, modular approach.

This lesson will show you how to build robust LLM applications using four foundational workflow patterns. We will cover how to chain multiple LLM calls, run them in parallel, route them with conditional logic, and orchestrate them with a central controller. These patterns are the building blocks for 95% of the production systems we see today, providing the control and reliability that single prompts lack.

We will explore:
- The challenges of complex, single LLM calls.
- The power of modularity and prompt chaining.
- How to build a sequential FAQ generation pipeline.
- How to optimize it with parallel processing.
- How to add dynamic behavior with routing.
- How to use the orchestrator-worker pattern for dynamic tasks.

## The Challenge with Complex Single LLM Calls

A single, complex prompt that asks an LLM to perform multiple distinct operations is often a recipe for unreliability. This approach, while simple to prototype, introduces several problems that make it unsuitable for production environments.

First, debugging becomes incredibly difficult. When a monolithic prompt fails, it is hard to pinpoint which instruction or part of the logic caused the error. You are left guessing whether the model misunderstood the formatting requirements, failed to extract an entity correctly, or generated a poor summary. Research on GPT-4 has shown that few-shot prompts with multiple examples can have error rates as high as 52.9%, with over 70% of those errors being simple parsing failures due to the model getting overwhelmed by the prompt's complexity [[1]](https://aclanthology.org/2025.ommm-1.4.pdf). This lack of visibility makes iterative improvement slow and frustrating.

Second, this design lacks modularity. If you want to improve one part of the task—say, enhance the summary generation—you have to modify the entire prompt. This risks unintentionally breaking other parts of thelogic. A modular system, by contrast, allows you to update or swap out individual components without affecting the rest of the workflow. This principle is a cornerstone of good software engineering, and it applies just as much to AI systems [[10]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

Furthermore, long and complex prompts are more susceptible to the "lost in the middle" problem. LLMs pay the most attention to the beginning and end of their context window, and information buried in the middle is often overlooked. This happens due to architectural factors like causal attention masking, where early tokens get more cumulative attention, and positional encoding decay, which weakens the signal for tokens in the middle. When you cram too many instructions and too much context into a single call, you increase the chance that the model will ignore important details. Studies have shown this U-shaped performance curve persists even in models with very large context windows [[2]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2).

Finally, monolithic prompts can be inefficient. They often require more tokens to describe the entire complex task, and you might be forced to use a powerful, expensive model for every part of the task, even when simpler, cheaper models would suffice for some sub-steps. Studies on multi-problem prompts have shown that while they can offer token savings of 30-82%, they often fail when the output format changes or when tasks are mixed, leading to increased error rates compared to modular, single-problem prompts [[11]](https://aclanthology.org/2025.gem-1.14.pdf).

To see this in practice, let's start with our setup.

1.  We will use the `google-genai` library to interact with Google's Gemini models. We will use `gemini-2.5-flash`, which is fast and cost-effective for the tasks in this lesson. Remember to set up your `GOOGLE_API_KEY` in your environment.

    ```python
    import asyncio
    from enum import Enum
    import random
    import time
    
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
    
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    MODEL_ID = "gemini-2.5-flash"
    ```

2.  Next, we will use mock content from three webpages about renewable energy as our source material.

    ```python
    webpage_1 = {
        "title": "The Benefits of Solar Energy",
        "content": "Solar energy is a renewable powerhouse, offering numerous environmental and economic benefits...",
    }
    
    webpage_2 = {
        "title": "Understanding Wind Turbines",
        "content": "Wind turbines are towering structures that capture kinetic energy from the wind and convert it into electrical power...",
    }
    
    webpage_3 = {
        "title": "Energy Storage Solutions",
        "content": "Effective energy storage is the key to unlocking the full potential of renewable sources like solar and wind...",
    }
    
    all_sources = [webpage_1, webpage_2, webpage_3]
    
    combined_content = "\n\n".join(
        [f"Source Title: {source['title']}\nContent: {source['content']}" for source in all_sources]
    )
    ```

3.  Now, let's create a complex prompt that asks the LLM to generate questions, find answers, and cite sources all in one call. We will use Pydantic for structured output, a concept we covered in Lesson 4.

    ```python
    class FAQ(BaseModel):
        """A FAQ is a question and answer pair, with a list of sources used to answer the question."""
        question: str = Field(description="The question to be answered")
        answer: str = Field(description="The answer to the question")
        sources: list[str] = Field(description="The sources used to answer the question")
    
    class FAQList(BaseModel):
        """A list of FAQs"""
        faqs: list[FAQ] = Field(description="A list of FAQs")
    
    n_questions = 10
    prompt_complex = f"""
    Based on the provided content from three webpages, generate a list of exactly {n_questions} frequently asked questions (FAQs).
    For each question, provide a concise answer derived ONLY from the text.
    After each answer, you MUST include a list of the 'Source Title's that were used to formulate that answer.
    
    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()
    
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=FAQList
    )
    response_complex = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt_complex,
        config=config
    )
    result_complex = response_complex.parsed
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
    {
      "question": "What are the environmental benefits of using solar energy?",
      "answer": "Solar energy reduces reliance on fossil fuels, thereby cutting down greenhouse gas emissions.",
      "sources": [
        "The Benefits of Solar Energy"
      ]
    }
    ...
    ```

While this output might look acceptable at first glance, this approach is fragile. The more instructions we add, the higher the chance of inconsistent formatting or factual inaccuracies. For example, the model might fail to cite a source correctly or hallucinate an answer not present in the text. This unreliability makes it a poor choice for production systems.

## The Power of Modularity: Why Chain LLM Calls?

The solution to the unreliability of monolithic prompts is modularity. Instead of asking one LLM call to do everything, we break the task into a series of smaller, more focused steps. This is the core idea behind **prompt chaining**: connecting multiple LLM calls sequentially, where the output of one step becomes the input for the next. It’s a simple "divide and conquer" strategy that brings traditional software engineering principles into the world of AI [[12]](https://www.decodingai.com/p/stop-building-ai-agents-use-these), [[13]](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a).

This approach offers several key benefits. First, it improves **modularity**. Each LLM call in the chain is responsible for a single, well-defined sub-task. This separation of concerns makes the system easier to understand, maintain, and update. You can work on the "question generation" prompt without worrying about breaking the "answer generation" logic. This is the same principle behind writing small, single-purpose functions in software engineering; it reduces cognitive load and makes the system more robust.

Second, it enhances **accuracy**. Simpler, more targeted prompts are less confusing for the LLM, which generally leads to more reliable and higher-quality outputs. Research and empirical evidence show that breaking down complex tasks into smaller steps consistently improves performance. Instead of juggling multiple instructions, the model can focus its full attention on one thing at a time [[12]](https://www.decodingai.com/p/stop-building-ai-agents-use-these), [[14]](https://blog.udemy.com/prompt-chaining/).

Third, it makes **debugging** much easier. If the final output is incorrect, you can inspect the output of each intermediate step to pinpoint exactly where things went wrong. This traceability is essential for identifying and fixing issues in a production environment. Finally, chaining offers greater **flexibility and optimization**. You can swap individual components of the chain, or even use different models for different steps. For instance, you could use a fast, cheap model for a simple classification task and a more powerful, expensive model for a complex content generation step. This allows you to balance cost, latency, and quality effectively [[12]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

However, prompt chaining is not without its trade-offs. One downside is increased latency, as you have to wait for multiple sequential API calls to complete. It can also increase costs due to the higher number of calls and total tokens used. Another risk is that some instructions may lose their meaning when split. A set of instructions might be semantically coherent only when presented together, and breaking them apart can lead to misinterpretation by the LLM at each step. Furthermore, as information is passed from one step to the next, important details can be lost or diluted, especially in long chains. This is a form of **context degradation**. We will explore techniques to mitigate this, such as using structured state objects, in future lessons on agent memory [[7]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production).

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's apply the principle of prompt chaining to our FAQ generation task. We will break the monolithic prompt into a three-step sequential workflow:
1.  **Generate Questions**: Create a list of questions based on the source content.
2.  **Answer Questions**: For each question, generate a concise answer.
3.  **Find Sources**: For each question-answer pair, identify the source documents.

Image 1: A flowchart illustrating the sequential FAQ generation pipeline.
```mermaid
flowchart LR
  "Input Content" --> "Generate Questions"
  "Generate Questions" --> "Answer Questions"
  "Answer Questions" --> "Find Sources"
```

This modular approach allows us to create specialized prompts for each sub-task, leading to more reliable and traceable results. Each function in our pipeline will have a single responsibility, making the entire system easier to manage and debug. This pattern is widely used in production for tasks like content creation, where a document might be outlined, drafted, and then formatted in separate steps [[13]](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a), [[15]](https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation). Real-world case studies from companies like AppFolio and Athena Intelligence show that using graph-based orchestration frameworks like LangGraph, which formalize these chains, leads to significant performance boosts and easier debugging in complex workflows [[16]](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works).

1.  First, we create a function dedicated solely to generating a list of questions. The prompt is simple and focused, asking only for questions and returning them in a structured list using the `QuestionList` Pydantic model. This ensures the output is clean and ready for the next step. By isolating this task, we can fine-tune the question generation process—for example, by adjusting the number of questions or specifying a particular style—without affecting the downstream answering and sourcing logic. This modularity is a key advantage of the chaining pattern.

    ```python
    class QuestionList(BaseModel):
        """A list of questions"""
        questions: list[str] = Field(description="A list of questions")
    
    prompt_generate_questions = """
    Based on the content below, generate a list of {n_questions} relevant and distinct questions that a user might have.
    
    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()
    
    def generate_questions(content: str, n_questions: int = 10) -> list[str]:
        """
        Generate a list of questions based on the provided content.
    
        Args:
            content: The combined content from all sources
    
        Returns:
            list: A list of generated questions
        """
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=QuestionList
        )
        response_questions = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt_generate_questions.format(n_questions=n_questions, combined_content=content),
            config=config
        )
    
        return response_questions.parsed.questions
    ```

2.  Next, we define a function to answer a given question. The prompt for this step is important: it explicitly instructs the model to use *only* the provided content. This technique, known as grounding, is vital for reducing hallucinations and ensuring the answers are factually based on the source material. By separating this step, we can apply different strategies to the answering process, such as asking for a concise answer or a detailed explanation, depending on the application's needs. This level of control is difficult to achieve in a single, monolithic prompt.

    ```python
    prompt_answer_question = """
    Using ONLY the provided content below, answer the following question.
    The answer should be concise and directly address the question.
    
    <question>
    {question}
    </question>
    
    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()
    
    def answer_question(question: str, content: str) -> str:
        """
        Generate an answer for a specific question using only the provided content.
    
        Args:
            question: The question to answer
            content: The combined content from all sources
    
        Returns:
            str: The generated answer
        """
        answer_response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt_answer_question.format(question=question, combined_content=content),
        )
        return answer_response.text
    ```

3.  Finally, we create a function to identify the sources for a given answer. This step adds a layer of verifiability and trust to our system. By asking the model to trace its answer back to the original documents, we can build applications that provide citations, allowing users to verify the information for themselves. Isolating this as the final step ensures that the model is focused on a pure reasoning task: connecting the generated answer to the source text without the cognitive load of also generating the answer itself.

    ```python
    class SourceList(BaseModel):
        """A list of source titles that were used to answer the question"""
        sources: list[str] = Field(description="A list of source titles that were used to answer the question")
    
    prompt_find_sources = """
    You will be given a question and an answer that was generated from a set of documents.
    Your task is to identify which of the original documents were used to create the answer.
    
    <question>
    {question}
    </question>
    
    <answer>
    {answer}
    </answer>
    
    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()
    
    def find_sources(question: str, answer: str, content: str) -> list[str]:
        """
        Identify which sources were used to generate an answer.
    
        Args:
            question: The original question
            answer: The generated answer
            content: The combined content from all sources
    
        Returns:
            list: A list of source titles that were used
        """
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=SourceList
        )
        sources_response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt_find_sources.format(question=question, answer=answer, combined_content=content),
            config=config
        )
        return sources_response.parsed.sources
    ```

4.  Now, we combine these functions into a single `sequential_workflow`. This function orchestrates the entire process: it first calls `generate_questions` to get the list of questions. Then, it iterates through each question, calling `answer_question` and `find_sources` in sequence. The results are collected into a list of `FAQ` objects. This orchestration logic is simple but effective, ensuring that each step is executed in the correct order and that the data flows correctly through the pipeline.

    ```python
    def sequential_workflow(content, n_questions=10) -> list[FAQ]:
        """
        Execute the complete sequential workflow for FAQ generation.
    
        Args:
            content: The combined content from all sources
    
        Returns:
            list: A list of FAQs with questions, answers, and sources
        """
        # Generate questions
        questions = generate_questions(content, n_questions)
    
        # Answer and find sources for each question sequentially
        final_faqs = []
        for question in questions:
            # Generate an answer for the current question
            answer = answer_question(question, content)
    
            # Identify the sources for the generated answer
            sources = find_sources(question, answer, content)
    
            faq = FAQ(
                question=question,
                answer=answer,
                sources=sources
            )
            final_faqs.append(faq)
    
        return final_faqs
    
    # Execute the sequential workflow (measure time for comparison)
    start_time = time.monotonic()
    sequential_faqs = sequential_workflow(combined_content, n_questions=4)
    end_time = time.monotonic()
    print(f"Sequential processing completed in {end_time - start_time:.2f} seconds")
    ```

    It outputs:

    ```text
    Sequential processing completed in 22.20 seconds
    ```

    The final `sequential_faqs` list contains well-structured `FAQ` objects, each with a question, a grounded answer, and a list of sources. By breaking the task down, we have created a more robust, debuggable, and maintainable system. However, processing each question one after the other is slow. This latency is a significant drawback for user-facing applications where real-time responses are expected.

## Optimizing Sequential Workflows With Parallel Processing

The sequential workflow improves reliability, but it is not efficient. Since answering each question is an independent task, we do not need to wait for one to finish before starting the next. This is a perfect opportunity for parallelization. LLM API calls are I/O-bound tasks; the program spends most of its time waiting for a response from the network. This makes them ideal candidates for asynchronous programming, which allows the program to work on other tasks while waiting for I/O operations to complete [[8]](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python), [[9]](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a).

By running these independent sub-tasks concurrently, we can greatly reduce the total processing time. We will use Python’s `asyncio` library to make asynchronous API calls to the Gemini model, allowing us to process multiple questions in parallel. Benchmarks show that for I/O-bound tasks like API calls, `asyncio` can be over 19 times faster than sequential execution and also outperforms traditional threading due to lower overhead [[9]](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a).

A word of caution: when making many parallel calls, you can easily hit API rate limits, especially with free-tier accounts. Production systems need robust error handling with strategies like exponential backoff and jitter to manage these limits gracefully. Exponential backoff involves increasing the wait time between retries after each failure, while jitter adds a small, random amount of time to each backoff to prevent a "thundering herd" of clients retrying at the exact same moment. For even greater resilience, you can implement a retry budget to limit the total number of retries or a circuit breaker pattern, which stops sending requests to a failing service for a period of time to allow it to recover. We will keep our example small to avoid this issue [[3]](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production).

1.  First, we need asynchronous versions of our `answer_question` and `find_sources` functions. The `google-genai` library provides an `aio` (asynchronous I/O) client for this purpose. The `async def` syntax defines a coroutine, a special function that can be paused and resumed. The `await` keyword pauses the function's execution until the awaited task (in this case, the API call) is complete, allowing the event loop to run other tasks in the meantime.

    ```python
    async def answer_question_async(question: str, content: str) -> str:
        """
        Async version of answer_question function.
        """
        prompt = prompt_answer_question.format(question=question, combined_content=content)
        response = await client.aio.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return response.text
    
    async def find_sources_async(question: str, answer: str, content: str) -> list[str]:
        """
        Async version of find_sources function.
        """
        prompt = prompt_find_sources.format(question=question, answer=answer, combined_content=content)
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=SourceList
        )
        response = await client.aio.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=config
        )
        return response.parsed.sources
    ```

2.  Next, we create a function that processes a single question by generating its answer and finding its sources. Although the steps for a single question are sequential (`find_sources` depends on `answer`), we define this as an `async` function so it can be run in parallel with the processing of other questions. This function encapsulates the logic for one unit of work in our parallel pipeline.

    ```python
    async def process_question_parallel(question: str, content: str) -> FAQ:
        """
        Process a single question by generating answer and finding sources in parallel.
        """
        answer = await answer_question_async(question, content)
        sources = await find_sources_async(question, answer, content)
        return FAQ(
            question=question,
            answer=answer,
            sources=sources
        )
    ```

3.  Finally, we define our parallel workflow. It first generates the questions synchronously, as before. Then, it creates a list of tasks, where each task is a call to `process_question_parallel`. The `asyncio.gather(*tasks)` function is the key here; it runs all the tasks in the list concurrently and waits for all of them to complete before returning the results. This is far more efficient than a sequential loop because the I/O wait times for the different API calls overlap.

    ```python
    async def parallel_workflow(content: str, n_questions: int = 10) -> list[FAQ]:
        """
        Execute the complete parallel workflow for FAQ generation.
    
        Args:
            content: The combined content from all sources
    
        Returns:
            list: A list of FAQs with questions, answers, and sources
        """
        # Generate questions (this step remains synchronous)
        questions = generate_questions(content, n_questions)
    
        # Process all questions in parallel
        tasks = [process_question_parallel(question, content) for question in questions]
        parallel_faqs = await asyncio.gather(*tasks)
    
        return parallel_faqs
    
    # Execute the parallel workflow (measure time for comparison)
    start_time = time.monotonic()
    parallel_faqs = await parallel_workflow(combined_content, n_questions=4)
    end_time = time.monotonic()
    print(f"Parallel processing completed in {end_time - start_time:.2f} seconds")
    ```

    It outputs:

    ```text
    Parallel processing completed in 8.98 seconds
    ```

By running the tasks in parallel, we reduced the execution time from 22.20 seconds to just 8.98 seconds. This represents a 2.5x speedup. For a larger number of questions, the improvement would be even more dramatic. This demonstrates the trade-off: parallel processing is faster and utilizes resources better, but it adds complexity to error handling and requires careful management of API rate limits. Sequential processing is slower but more predictable and easier to debug. In parallel execution, since subtasks are independent, it can also help mitigate the compounding error effect seen in long sequential chains, where a small error in an early step invalidates all subsequent results [[17]](https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge).

## Introducing Dynamic Behavior: Routing and Conditional Logic

So far, our workflows have been static. The FAQ generation pipeline follows a fixed, linear path. But what if our application needs to handle different types of inputs in different ways? Trying to optimize a single prompt to handle multiple distinct cases is inefficient and often leads to degraded performance. This is where routing comes in.

Routing introduces conditional logic into our workflows, allowing us to dynamically select a processing path based on the input. It is another application of the "divide and conquer" principle. Instead of one monolithic prompt, we create specialized prompts for each case and use a classifier to direct the input to the appropriate one [[12]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

While using an LLM as the classifier is a common approach, routing can be implemented using several techniques. These include rule-based routing using heuristics like query length, semantic routing via vector embeddings, or even cost-aware routing that sends a query to a more powerful model only when a cheaper one returns a low-confidence score [[18]](https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/). For specialized domains, fine-tuning a smaller classifier model on proprietary data can also improve accuracy [[19]](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/).

An LLM call itself can serve as this classifier. We can prompt a model to analyze an input and categorize it, and then use that classification in our application code to trigger the correct downstream logic. This creates a branching workflow, where different inputs are handled by specialized experts. For example, a customer support system might route a query about a billing issue to a billing-specialized prompt, while a technical problem goes to a technical support prompt. This ensures each query gets the most relevant and accurate response.

In production, this often evolves into a cascade pattern: a fast, cheap method like semantic search handles the initial broad categorization, followed by a fine-tuned classifier for more specific cases, with a powerful LLM as a final backstop for the most ambiguous inputs. This tiered approach balances cost, latency, and accuracy. For high-stakes decisions, you can implement more advanced logic based on decision theory, using confidence thresholds to decide whether to allow an action, abstain and ask for clarification, or deny the request outright [[20]](https://huggingface.co/blog/perfecXion/intentguard), [[21]](https://tianpan.co/blog/2026-04-16-intent-classification-agent-routers).

## Building a Basic Routing Workflow

Let's build a simple routing workflow for a customer service system. The goal is to classify an incoming user query into one of three intents—`Technical Support`, `Billing Inquiry`, or `General Question`—and then route it to a specialized handler.

Image 2: A flowchart illustrating a routing workflow for customer service intent classification.
```mermaid
graph TD
    A["User Input"] --> B["Intent Classification"]
    B -->|"Technical Support Intent"| C["Technical Support"]
    B -->|"Billing Inquiry Intent"| D["Billing Inquiry"]
    B -->|"General Question Intent"| E["General Question"]
    C --> F["Final Responses"]
    D --> F
    E --> F
```

This pattern keeps our prompts focused and maintainable. Each handler can be optimized for its specific task without interfering with the others. This modularity is key to building scalable and reliable systems. This approach is common in production; for example, Google's ADK framework uses a "Coordinator/Dispatcher" pattern where a central agent analyzes user intent and routes the request to a specialist sub-agent, like a 'Billing' or 'Tech Support' specialist [[22]](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/).

1.  First, we define our intents using a Python `Enum` and create a Pydantic model, `UserIntent`, to enforce the structure of the classifier's output. This creates a clear contract for what we expect from the LLM. The classification prompt is straightforward: it asks the model to categorize the user query based on the provided list of categories. This step is the core of our routing logic, turning an unstructured user query into a structured, actionable intent.

    ```python
    class IntentEnum(str, Enum):
        """
        Defines the allowed values for the 'intent' field.
        Inheriting from 'str' ensures that the values are treated as strings.
        """
        TECHNICAL_SUPPORT = "Technical Support"
        BILLING_INQUIRY = "Billing Inquiry"
        GENERAL_QUESTION = "General Question"
    
    class UserIntent(BaseModel):
        """
        Defines the expected response schema for the intent classification.
        """
        intent: IntentEnum = Field(description="The intent of the user's query")
    
    prompt_classification = """
    Classify the user's query into one of the following categories.
    
    <categories>
    {categories}
    </categories>
    
    <user_query>
    {user_query}
    </user_query>
    """.strip()
    
    
    def classify_intent(user_query: str) -> IntentEnum:
        """Uses an LLM to classify a user query."""
        prompt = prompt_classification.format(
            user_query=user_query,
            categories=[intent.value for intent in IntentEnum]
        )
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=UserIntent
        )
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=config
        )
        return response.parsed.intent
    ```

2.  Next, we define specialized prompts for each intent. The `prompt_technical_support` is designed to gather more information for troubleshooting. The `prompt_billing_inquiry` is tailored to acknowledge the concern and request an account number. The `prompt_general_question` serves as a fallback. Each prompt gives the LLM a clear role and objective, ensuring that the response is appropriate for the classified intent. This specialization is what makes the routing pattern so effective.

    ```python
    prompt_technical_support = """
    You are a helpful technical support agent.
    
    Here's the user's query:
    <user_query>
    {user_query}
    </user_query>
    
    Provide a helpful first response, asking for more details like what troubleshooting steps they have already tried.
    """.strip()
    
    prompt_billing_inquiry = """
    You are a helpful billing support agent.
    
    Here's the user's query:
    <user_query>
    {user_query}
    </user_query>
    
    Acknowledge their concern and inform them that you will need to look up their account, asking for their account number.
    """.strip()
    
    prompt_general_question = """
    You are a general assistant.
    
    Here's the user's query:
    <user_query>
    {user_query}
    </user_query>
    
    Apologize that you are not sure how to help.
    """.strip()
    ```

3.  Finally, we create a `handle_query` function that acts as our router. It takes the user query and the classified intent, and then uses simple `if/elif/else` logic to select the appropriate prompt and call the LLM. This function is the bridge between the classification step and the specialized handlers. Including a default or catch-all route is an important practice for robustness, ensuring the system can gracefully handle unexpected or unclassifiable inputs [[12]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

    ```python
    def handle_query(user_query: str, intent: str) -> str:
        """Routes a query to the correct handler based on its classified intent."""
        if intent == IntentEnum.TECHNICAL_SUPPORT:
            prompt = prompt_technical_support.format(user_query=user_query)
        elif intent == IntentEnum.BILLING_INQUIRY:
            prompt = prompt_billing_inquiry.format(user_query=user_query)
        elif intent == IntentEnum.GENERAL_QUESTION:
            prompt = prompt_general_question.format(user_query=user_query)
        else:
            prompt = prompt_general_question.format(user_query=user_query)
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return response.text
    ```

4.  Let's test it with a few different queries. For a query like "My internet connection is not working," the system correctly identifies the intent as `Technical Support` and generates a helpful response asking for more details. For "I think there is a mistake on my last invoice," it identifies `Billing Inquiry` and responds by asking for an account number. This simple routing workflow demonstrates how to build more intelligent and specialized AI systems.

    To optimize this further, you could even combine multiple classification decisions into a single LLM call. For instance, you could ask the model to determine both the *intent* (e.g., technical) and the *depth* (e.g., simple vs. complex) in one structured output, minimizing API latency [[23]](https://docs.nvidia.com/aiq-blueprint/2.0.0/architecture/agents/intent-classifier.html).

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The final pattern we will explore is the orchestrator-worker pattern. This is a more advanced workflow where a central "orchestrator" LLM dynamically breaks down a complex task into smaller sub-tasks and delegates them to specialized "worker" LLMs or functions. After the workers complete their tasks, often in parallel, the orchestrator synthesizes their results into a cohesive final output [[4]](https://agents.kour.me/orchestrator-worker/), [[12]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

Image 3: A flowchart illustrating the orchestrator-worker pattern, showing dynamic task decomposition, delegation to specialized worker LLMs, and result synthesis.
```mermaid
flowchart LR
  %% User initiates query
  User["User"] --> Query["Complex User Query"]

  %% Orchestrator processes query and breaks down tasks
  Query --> Orchestrator["Orchestrator"]
  Orchestrator -- "receives" --> Breakdown["Dynamically Breaks Down Task<br/>into Subtasks"]

  %% Delegation to specialized Worker LLMs
  subgraph WorkerLLMs["Worker LLMs"]
    Billing["Billing Inquiry"]
    Product["Product Return"]
    Status["Status Update"]
  end

  Breakdown -- "delegates subtask" --> Billing
  Breakdown -- "delegates subtask" --> Product
  Breakdown -- "delegates subtask" --> Status

  %% Worker LLMs execute and return results
  Billing -- "execute & return results" --> Orchestrator
  Product -- "execute & return results" --> Orchestrator
  Status -- "execute & return results" --> Orchestrator

  %% Orchestrator synthesizes and responds
  Orchestrator -- "synthesizes results" --> Synthesize["Synthesizes Results into<br/>Cohesive Response"]
  Synthesize --> User["User"]
```

This pattern is powerful for complex problems where the necessary steps cannot be predicted in advance. The key difference from simple parallelization is its flexibility: the orchestrator determines the sub-tasks at runtime based on the specific input [[6]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers). The orchestrator is analogous to a project manager who assesses a request, breaks it down into assignments, gives them to the right team members, and then assembles their work into a final deliverable.

This process is similar to how an operating system's task scheduler manages computational resources. The orchestrator acts as a "traffic controller," deciding which tasks to run, when, and where, potentially prioritizing them based on complexity or system load [[24]](https://latitude.so/blog/how-task-scheduling-optimizes-llm-workflows). While this pattern uses a centralized coordinator, other approaches exist, such as decentralized patterns where agents dynamically allocate tasks among themselves without a central orchestrator, using predictions about execution time and success probability [[25]](https://www.nature.com/articles/s41598-025-21709-9), [[26]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production).

Let's build a customer support system using this pattern. A user might have a single query that involves multiple issues, like a billing question, a product return, and an order status request.

1.  First, we define the orchestrator. Its job is to analyze the user's query and break it down into a structured list of tasks, each with a specific type and the necessary parameters. The prompt clearly defines the available `query_type` values and their required parameters, guiding the LLM to produce a valid `TaskList`. Using structured output like XML or JSON for the subtask descriptions is a key design principle, as it ensures the workers receive clear, unambiguous instructions [[27]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns), [[28]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers).

    ```python
    class QueryTypeEnum(str, Enum):
        """The type of query to be handled."""
        BILLING_INQUIRY = "BillingInquiry"
        PRODUCT_RETURN = "ProductReturn"
        STATUS_UPDATE = "StatusUpdate"
    
    class Task(BaseModel):
        """A task to be performed."""
        query_type: QueryTypeEnum = Field(description="The type of query to be handled.")
        invoice_number: str | None = Field(description="The invoice number to be used for the billing inquiry.", default=None)
        product_name: str | None = Field(description="The name of the product to be returned.", default=None)
        reason_for_return: str | None = Field(description="The reason for returning the product.", default=None)
        order_id: str | None = Field(description="The order ID to be used for the status update.", default=None)
    
    class TaskList(BaseModel):
        """A list of tasks to be performed."""
        tasks: list[Task] = Field(description="A list of tasks to be performed.")
    
    prompt_orchestrator = f"""
    You are a master orchestrator. Your job is to break down a complex user query into a list of sub-tasks.
    Each sub-task must have a "query_type" and its necessary parameters.
    
    The possible "query_type" values and their required parameters are:
    1. "{QueryTypeEnum.BILLING_INQUIRY.value}": Requires "invoice_number".
    2. "{QueryTypeEnum.PRODUCT_RETURN.value}": Requires "product_name" and "reason_for_return".
    3. "{QueryTypeEnum.STATUS_UPDATE.value}": Requires "order_id".
    
    Here's the user's query.
    
    <user_query>
    {{query}}
    </user_query>
    """.strip()
    
    
    def orchestrator(query: str) -> list[Task]:
        """Breaks down a complex query into a list of tasks."""
        prompt = prompt_orchestrator.format(query=query)
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=TaskList
        )
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=config
        )
        return response.parsed.tasks
    ```

2.  Next, we define our specialized workers. In a real application, these would interact with backend systems, databases, or external APIs. For this example, we will simulate their behavior. We will have a `handle_billing_worker`, a `handle_return_worker`, and a `handle_status_worker`. Each takes specific inputs and returns a structured output. This specialization can also extend to the models themselves; for instance, a simple data-lookup task might be delegated to a small, fast model, while a complex analysis task goes to a more powerful one to optimize cost and performance [[29]](https://labelyourdata.com/articles/llm-fine-tuning/llm-orchestration).

    ```python
    class BillingTask(BaseModel):
        """A billing inquiry task to be performed."""
        query_type: QueryTypeEnum = Field(description="The type of task to be performed.", default=QueryTypeEnum.BILLING_INQUIRY)
        invoice_number: str = Field(description="The invoice number to be used for the billing inquiry.")
        user_concern: str = Field(description="The concern or question the user has voiced about the invoice.")
        action_taken: str = Field(description="The action taken to address the user's concern.")
        resolution_eta: str = Field(description="The estimated time to resolve the concern.")
    
    prompt_billing_worker_extractor = """
    You are a specialized assistant. A user has a query regarding invoice '{invoice_number}'.
    From the full user query provided below, extract the specific concern or question the user has voiced about this particular invoice.
    Respond with ONLY the extracted concern/question. If no specific concern is mentioned beyond a general inquiry about the invoice, state 'General inquiry regarding the invoice'.
    
    Here's the user's query:
    <user_query>
    {original_user_query}
    </user_query>
    
    Extracted concern about invoice {invoice_number}:
    """.strip()
    
    
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
        """
        Handles a billing inquiry.
        1. Uses an LLM to extract the specific concern about the invoice from the original query.
        2. Simulates opening an investigation.
        3. Returns structured data about the action taken.
        """
        extraction_prompt = prompt_billing_worker_extractor.format(
            invoice_number=invoice_number, original_user_query=original_user_query
        )
        response = client.models.generate_content(model=MODEL_ID, contents=extraction_prompt)
        extracted_concern = response.text
    
        # Simulate backend action: opening an investigation
        investigation_id = f"INV_CASE_{random.randint(1000, 9999)}"
        eta_days = 2
    
        task = BillingTask(
            invoice_number=invoice_number,
            user_concern=extracted_concern,
            action_taken=f"An investigation (Case ID: {investigation_id}) has been opened regarding your concern.",
            resolution_eta=f"{eta_days} business days",
        )
    
        return task
    
    class ReturnTask(BaseModel):
        """A task to handle a product return request."""
        query_type: QueryTypeEnum = Field(description="The type of task to be performed.", default=QueryTypeEnum.PRODUCT_RETURN)
        product_name: str = Field(description="The name of the product to be returned.")
        reason_for_return: str = Field(description="The reason for returning the product.")
        rma_number: str = Field(description="The RMA number for the return.")
        shipping_instructions: str = Field(description="The shipping instructions for the return.")
    
    
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
        """
        Handles a product return request.
        1. Simulates generating an RMA number and providing return instructions.
        2. Returns structured data.
        """
        # Simulate backend action: generating RMA and getting instructions
        rma_number = f"RMA-{random.randint(10000, 99999)}"
        shipping_instructions = (
            "Please pack the '{product_name}' securely in its original packaging if possible. "
            "Include all accessories and manuals. Write the RMA number ({rma_number}) clearly on the outside of the package. "
            "Ship to: Returns Department, 123 Automation Lane, Tech City, TC 98765."
        ).format(product_name=product_name, rma_number=rma_number)
    
        task = ReturnTask(
            product_name=product_name,
            reason_for_return=reason_for_return,
            rma_number=rma_number,
            shipping_instructions=shipping_instructions,
        )
    
        return task
    
    class StatusTask(BaseModel):
        """A task to handle an order status update request."""
        query_type: QueryTypeEnum = Field(description="The type of task to be performed.", default=QueryTypeEnum.STATUS_UPDATE)
        order_id: str = Field(description="The order ID to be used for the status update.")
        current_status: str = Field(description="The current status of the order.")
        carrier: str = Field(description="The carrier of the order.")
        tracking_number: str = Field(description="The tracking number of the order.")
        expected_delivery: str = Field(description="The expected delivery date of the order.")
    
    def handle_status_worker(order_id: str) -> StatusTask:
        """
        Handles an order status update request.
        1. Simulates fetching order status from a backend system.
        2. Returns structured data.
        """
        # Simulate backend action: fetching order status
        possible_statuses = [
            {"status": "Processing", "carrier": "N/A", "tracking": "N/A", "delivery_estimate": "3-5 business days"},
            {
                "status": "Shipped",
                "carrier": "SuperFast Shipping",
                "tracking": f"SF{random.randint(100000, 999999)}",
                "delivery_estimate": "Tomorrow",
            },
            {
                "status": "Delivered",
                "carrier": "Local Courier",
                "tracking": f"LC{random.randint(10000, 99999)}",
                "delivery_estimate": "Delivered yesterday",
            },
            {
                "status": "Delayed",
                "carrier": "Standard Post",
                "tracking": f"SP{random.randint(10000, 99999)}",
                "delivery_estimate": "Expected in 2-3 additional days",
            },
        ]
        status_details = random.choice(possible_statuses)
    
        task = StatusTask(
            order_id=order_id,
            current_status=status_details["status"],
            carrier=status_details["carrier"],
            tracking_number=status_details["tracking"],
            expected_delivery=status_details["delivery_estimate"],
        )
    
        return task
    ```

3.  After the workers have done their jobs, we need a synthesizer. This component takes the structured results from all workers and uses an LLM to craft a single, coherent, and user-friendly response. The prompt instructs the model to combine the distinct points into one cohesive message, ensuring a professional and helpful tone. The synthesis step is what brings the parallel work back together into a valuable final product for the user [[30]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent).

    ```python
    prompt_synthesizer = """
    You are a master communicator. Combine several distinct pieces of information from our support team into a single, well-formatted, and friendly email to a customer.
    
    Here are the points to include, based on the actions taken for their query:
    <points>
    {formatted_results}
    </points>
    
    Combine these points into one cohesive response.
    Start with a friendly greeting (e.g., "Dear Customer," or "Hi there,") and end with a polite closing (e.g., "Sincerely," or "Best regards,").
    Ensure the tone is helpful and professional.
    """.strip()
    
    
    def synthesizer(results: list[Task]) -> str:
        """Combines structured results from workers into a single user-facing message."""
        bullet_points = []
        for res in results:
            point = f"Regarding your {res.query_type}:\n"
            if res.query_type == QueryTypeEnum.BILLING_INQUIRY:
                res: BillingTask = res
                point += f"  - Invoice Number: {res.invoice_number}\n"
                point += f'  - Your Stated Concern: "{res.user_concern}"\n'
                point += f"  - Our Action: {res.action_taken}\n"
                point += f"  - Expected Resolution: We will get back to you within {res.resolution_eta}."
            elif res.query_type == QueryTypeEnum.PRODUCT_RETURN:
                res: ReturnTask = res
                point += f"  - Product: {res.product_name}\n"
                point += f'  - Reason for Return: "{res.reason_for_return}"\n'
                point += f"  - Return Authorization (RMA): {res.rma_number}\n"
                point += f"  - Instructions: {res.shipping_instructions}"
            elif res.query_type == QueryTypeEnum.STATUS_UPDATE:
                res: StatusTask = res
                point += f"  - Order ID: {res.order_id}\n"
                point += f"  - Current Status: {res.current_status}\n"
                if res.carrier != "N/A":
                    point += f"  - Carrier: {res.carrier}\n"
                if res.tracking_number != "N/A":
                    point += f"  - Tracking Number: {res.tracking_number}\n"
                point += f"  - Delivery Estimate: {res.expected_delivery}"
            bullet_points.append(point)
    
        formatted_results = "\n\n".join(bullet_points)
        prompt = prompt_synthesizer.format(formatted_results=formatted_results)
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    ```

4.  Finally, we tie everything together in a main pipeline function. This `process_user_query` function orchestrates the entire workflow: it calls the orchestrator to break down the query, dispatches the appropriate workers based on the task type, collects their results, and passes them to the synthesizer to generate the final response.

    ```python
    def process_user_query(user_query):
        """Processes a query using the Orchestrator-Worker-Synthesizer pattern."""
    
        # 1. Run orchestrator
        tasks_list = orchestrator(user_query)
        
        # 2. Run workers
        worker_results = []
        if tasks_list:
            for task in tasks_list:
                if task.query_type == QueryTypeEnum.BILLING_INQUIRY:
                    worker_results.append(handle_billing_worker(task.invoice_number, user_query))
                elif task.query_type == QueryTypeEnum.PRODUCT_RETURN:
                    worker_results.append(handle_return_worker(task.product_name, task.reason_for_return))
                elif task.query_type == QueryTypeEnum.STATUS_UPDATE:
                    worker_results.append(handle_status_worker(task.order_id))
                else:
                    print(f"Warning: Unknown query_type '{task.query_type}' found in orchestrator tasks.")
    
        # 3. Run synthesizer
        if worker_results:
            final_user_message = synthesizer(worker_results)
    ```

5.  Let's test it with a complex query that triggers all three workers.

    ```python
    complex_customer_query = """
    Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.
    Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.
    Finally, can you give me an update on my order #A-12345?
    """.strip()
    
    process_user_query(complex_customer_query)
    ```

The orchestrator correctly identifies the three distinct tasks and extracts the necessary parameters. The workers then process these tasks, and the synthesizer combines their outputs into a single, helpful email to the customer. This pattern allows us to build sophisticated systems that can handle complex, multi-part queries dynamically and reliably.

## Conclusion

In this lesson, we have moved beyond simple, monolithic prompts and explored four foundational patterns for building robust LLM workflows. We have seen how breaking down complex tasks into smaller, manageable steps is key to creating reliable and maintainable AI applications.

We started with **prompt chaining**, a sequential pattern that improves modularity and makes debugging easier. We then optimized this with **parallelization**, greatly reducing latency for independent tasks. We introduced dynamic behavior with **routing**, using an LLM as a classifier to direct inputs to specialized handlers. Finally, we explored the **orchestrator-worker** pattern, a flexible approach for dynamically decomposing and delegating complex tasks.

These four patterns—chaining, parallelization, routing, and orchestration—are not just theoretical concepts; they are the bread and butter of production AI engineering. They are the core components of any modern Generative AI platform, which combines models, databases, and actions into reliable pipelines. They provide the control, reliability, and scalability needed to move from simple prototypes to powerful applications. As you continue your journey as an AI Engineer, you will find yourself using and combining these patterns to solve a wide range of problems [[31]](https://huyenchip.com/2024/07/25/genai-platform.html).

In our next lesson, we will take another step up the agentic continuum. We will learn how to give our workflows the ability to interact with the outside world by teaching them how to use tools through function calling.

## References

- [1] Gozzi, M., & Di Maio, F. (2024). Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts. Electronics, 13(23), 4712. [https://www.mdpi.com/2079-9292/13/23/4712](https://www.mdpi.com/2079-9292/13/23/4712)
- [2] The "Lost in the Middle" Problem — Why LLMs Ignore the Middle of Your Context Window. (2026). dev.to. [https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [3] Tian, P. (2026). LLM API Resilience in Production. [https://tianpan.co/blog/2026-03-11-llm-api-resilience-production](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production)
- [4] Kour, G. (n.d.). Pattern: Orchestrator-Worker (Coordinator). [https://agents.kour.me/orchestrator-worker/](https://agents.kour.me/orchestrator-worker/)
- [5] FLARE framework analyzes GPT-4 Turbo. (2025). [https://aclanthology.org/2025.ommm-1.4.pdf](https://aclanthology.org/2025.ommm-1.4.pdf)
- [6] Orchestrator-Workers Pattern. (n.d.). Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [7] How Tool Chaining Fails in Production. (n.d.). futureagi.substack.com. [https://futureagi.substack.com/p/how-tool-chaining-fails-in-production](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production)
- [8] Santhala, K. (2024). Concurrency Patterns in Python with Asyncio. [https://santhalakshminarayana.github.io/blog/concurrency-patterns-python](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python)
- [9] Python Concurrency Showdown. (n.d.). Medium. [https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a)
- [10] Underspecification analysis. (2025). [https://arxiv.org/html/2505.13360v1](https://arxiv.org/html/2505.13360v1)
- [11] ZeMPE benchmark. (2025). [https://aclanthology.org/2025.gem-1.14.pdf](https://aclanthology.org/2025.gem-1.14.pdf)
- [12] Iusztin, P. (n.d.). Stop Building AI Agents. Use These Workflow Patterns Instead. Decoding AI. [https://www.decodingai.com/p/stop-building-ai-agents-use-these](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [13] Lalli, F. (n.d.). A Practical Guide to Prompt Engineering Techniques. Medium. [https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a)
- [14] Prompt Chaining. (n.d.). Udemy. [https://blog.udemy.com/prompt-chaining/](https://blog.udemy.com/prompt-chaining/)
- [15] 10 Prompt Engineering Techniques. (n.d.). Scrum.org. [https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation](https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation)
- [16] LLMOps in Production: 457 Case Studies. (2025). ZenML. [https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works)
- [17] Compounding Error Effect in LLMs. (n.d.). wand.ai. [https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge](https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge)
- [18] Top 5 LLM Routing Techniques. (n.d.). getmaxim.ai. [https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/](https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/)
- [19] Multi-LLM routing strategies on AWS. (n.d.). AWS. [https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)
- [20] IntentGuard: Two-stage routing architecture. (n.d.). Hugging Face. [https://huggingface.co/blog/perfecXion/intentguard](https://huggingface.co/blog/perfecXion/intentguard)
- [21] Tian, P. (2026). Intent Classification for Agent Routers. [https://tianpan.co/blog/2026-04-16-intent-classification-agent-routers](https://tianpan.co/blog/2026-04-16-intent-classification-agent-routers)
- [22] Multi-agent patterns in ADK. (n.d.). Google Developers Blog. [https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [23] NVIDIA AI-Q Blueprint: Intent Classifier. (n.d.). NVIDIA Docs. [https://docs.nvidia.com/aiq-blueprint/2.0.0/architecture/agents/intent-classifier.html](https://docs.nvidia.com/aiq-blueprint/2.0.0/architecture/agents/intent-classifier.html)
- [24] How Task Scheduling Optimizes LLM Workflows. (n.d.). Latitude. [https://latitude.so/blog/how-task-scheduling-optimizes-llm-workflows](https://latitude.so/blog/how-task-scheduling-optimizes-llm-workflows)
- [25] Decentralized adaptive task allocation for multi-agent systems. (2025). Nature. [https://www.nature.com/articles/s41598-025-21709-9](https://www.nature.com/articles/s41598-025-21709-9)
- [26] Multi-Agent Orchestration Patterns for Production. (n.d.). Beam.ai. [https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)
- [27] Issue 110: LLM Workflow Patterns. (n.d.). mlpills.substack.com. [https://mlpills.substack.com/p/issue-110-llm-workflow-patterns](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [28] Orchestrator-Workers Pattern. (n.d.). Claude Cookbook. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [29] LLM Orchestration Explained. (n.d.). Label Your Data. [https://labelyourdata.com/articles/llm-fine-tuning/llm-orchestration](https://labelyourdata.com/articles/llm-fine-tuning/llm-orchestration)
- [30] DIY #17: Orchestrator-Worker LLM Agent. (n.d.). mlpills.substack.com. [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [31] Huyen, C. (2024). Building a Generative AI Platform. [https://huyenchip.com/2024/07/25/genai-platform.html](https://huyenchip.com/2024/07/25/genai-platform.html)