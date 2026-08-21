# Stop Building Complex AI Prompts: Use These Workflow Patterns Instead

In our last lesson, we covered context engineering, the art of feeding the right information to an LLM. Now, we will tackle the other side of the equation: getting structured and reliable information *out* of an LLM. When we started building AI applications, we fell into a common trap. We tried to solve complex, multi-step problems with a single, massive prompt, thinking a powerful model could handle it all. The result was an unpredictable system that was difficult to debug and failed silently in production.

This experience taught us a critical lesson: monolithic prompts don’t scale. Just as in traditional software development, reliability comes from modularity. Instead of one giant, do-it-all prompt, we need to break down tasks into smaller, manageable steps. This is the core idea behind LLM workflows.

In this lesson, we will explore the fundamental patterns for building robust LLM workflows: chaining, parallelization, routing, and the orchestrator-worker pattern. We will move from theory to practice, showing you how to implement these patterns from scratch using Google's Gemini API. By the end, you will understand how to design systems that are not only powerful but also reliable, debuggable, and ready for production.

## The Challenge with Complex Single LLM Calls

A common starting point for many developers is to craft a single, comprehensive prompt that asks an LLM to perform multiple tasks at once. The intuition is that a powerful model should be ableto handle a complex set of instructions. However, this approach often leads to a host of problems in production systems.

One of the biggest issues is the difficulty in debugging. When a monolithic prompt fails, it is hard to pinpoint exactly which instruction or part of the logic caused the error. The output might be subtly wrong, or the format might be inconsistent. Without clear, intermediate steps, you are left trying to diagnose a black box. This lack of modularity also makes the system difficult to maintain. If you need to update one part of the logic, you risk breaking another, turning simple changes into a high-stakes guessing game [[36]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

Furthermore, long, complex prompts are susceptible to the "lost in the middle" problem. Research from Stanford and UC Berkeley has shown that LLMs exhibit a U-shaped performance curve when processing long contexts. They pay the most attention to information at the beginning and end of the prompt, while details in the middle are often overlooked [[2]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2). This happens due to architectural reasons like causal attention masking, where early tokens get more cumulative attention, and positional encoding decay, which weakens the signal for tokens in the middle. Simply stuffing more information into the context does not solve the problem; it just creates a larger "middle" for information to get lost in.

Finally, a single complex prompt can be less reliable and more sensitive to minor changes in the input. Studies have shown that slight variations in wording or format can lead to drastically different outputs, making the system unpredictable [[3]](https://aclanthology.org/2025.ommm-1.4.pdf). While it might seem counterintuitive, a single large prompt can also lead to higher token consumption if the model generates verbose reasoning to handle the combined complexity, compared to a series of focused, concise calls.

Let's look at a practical example. We will try to generate a Frequently Asked Questions (FAQ) page from a few documents about renewable energy, asking the model to generate questions, find answers, and cite sources all in one go.

1.  First, we set up our environment by importing the necessary packages and initializing the Gemini client. We will use the `gemini-2.5-flash` model, which is fast and cost-effective for this kind of task.
    ```python
    import asyncio
    from enum import Enum
    import random
    import time
    
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
    
    from lessons.utils import env
    from lessons.utils import pretty_print
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-2.5-flash"
    ```
    It outputs:
    ```text:
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
2.  Next, we define our source content—three mock webpages on renewable energy.
    ```python
    webpage_1 = {
        "title": "The Benefits of Solar Energy",
        "content": """
        Solar energy is a renewable powerhouse, offering numerous environmental and economic benefits.
        By converting sunlight into electricity through photovoltaic (PV) panels, it reduces reliance on fossil fuels,
        thereby cutting down greenhouse gas emissions. Homeowners who install solar panels can significantly
        lower their monthly electricity bills, and in some cases, sell excess power back to thegrid.
        While the initial installation cost can be high, government incentives and long-term savings make
        it a financially viable option for many. Solar power is also a key component in achieving energy
        independence for nations worldwide.
        """,
    }
    
    webpage_2 = {
        "title": "Understanding Wind Turbines",
        "content": """
        Wind turbines are towering structures that capture kinetic energy from the wind and convert it into
        electrical power. They are a critical part of the global shift towards sustainable energy.
        Turbines can be installed both onshore and offshore, with offshore wind farms generally producing more
        consistent power due to stronger, more reliable winds. The main challenge for wind energy is its
        intermittency—it only generates power when the wind blows. This necessitates the use of energy
        storage solutions, like large-scale batteries, to ensure a steady supply of electricity.
        """,
    }
    
    webpage_3 = {
        "title": "Energy Storage Solutions",
        "content": """
        Effective energy storage is the key to unlocking the full potential of renewable sources like solar
        and wind. Because these sources are intermittent, storing excess energy when it's plentiful and
        releasing it when it's needed is crucial for a stable power grid. The most common form of
        large-scale storage is pumped-hydro storage, but battery technologies, particularly lithium-ion,
        are rapidly becoming more affordable and widespread. These batteries can be used in homes, businesses,
        and at the utility scale to balance energy supply and demand, making our energy system more
        resilient and reliable.
        """,
    }
    
    all_sources = [webpage_1, webpage_2, webpage_3]
    
    # We'll combine the content for the LLM to process
    combined_content = "\n\n".join(
        [f"Source Title: {source['title']}\nContent: {source['content']}" for source in all_sources]
    )
    ```
3.  Here is the complex prompt that tries to do everything at once. We also define Pydantic models to ask for a structured JSON output, a concept we covered in Lesson 4.
    ```python
    # This prompt tries to do everything at once: generate questions, find answers,
    # and cite sources. This complexity can often confuse the model.
    n_questions = 10
    prompt_complex = f"""
    Based on the provided content from three webpages, generate a list of exactly {n_questions} frequently asked questions (FAQs).
    For each question, provide a concise answer derived ONLY from the text.
    After each answer, you MUST include a list of the 'Source Title's that were used to formulate that answer.
    
    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()
    
    # Pydantic classes for structured outputs
    class FAQ(BaseModel):
        """A FAQ is a question and answer pair, with a list of sources used to answer the question."""
        question: str = Field(description="The question to be answered")
        answer: str = Field(description="The answer to the question")
        sources: list[str] = Field(description="The sources used to answer the question")
    
    class FAQList(BaseModel):
        """A list of FAQs"""
        faqs: list[FAQ] = Field(description="A list of FAQs")
    
    # Generate FAQs
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
    ```text
    [
      {
        "question": "What is solar energy and how does it work?",
        "answer": "Solar energy is a renewable powerhouse that converts sunlight into electricity through photovoltaic (PV) panels.",
        "sources": [
          "The Benefits of Solar Energy"
        ]
      },
      ...
      {
        "question": "Why is energy storage crucial for renewable energy sources like solar and wind?",
        "answer": "Effective energy storage is key to unlocking the full potential of renewable sources because it allows storing excess energy when plentiful and releasing it when needed, which is crucial for a stable power grid.",
        "sources": [
          "Energy Storage Solutions",
          "Understanding Wind Turbines"
        ]
      }
    ]
    ```

While the output seems reasonable at first glance, this approach is fragile. For more complex tasks, the model might fail to follow the format, hallucinate sources, or generate answers that blend information incorrectly. For instance, the last question's answer is derived from two sources, but a single complex prompt might miss this nuance and only cite one. The more instructions we add, the higher the chance of failure.

## The Power of Modularity: Why Chain LLM Calls?

To build more reliable systems, we need to adopt a modular approach. This is where prompt chaining comes in. Prompt chaining is the practice of breaking a complex task into a sequence of smaller, simpler sub-tasks. The output of one LLM call becomes the input for the next, creating a workflow or "chain" [[41]](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a). This "divide and conquer" strategy is fundamental to building robust and maintainable AI applications.

The primary benefit of chaining is improved modularity. Each step in the chain is a self-contained component with a single responsibility. This makes the system far easier to test and debug. If a workflow fails, you can inspect the input and output of each step to isolate the exact point of failure, a process that is nearly impossible with a monolithic prompt [[46]](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns). This modularity also enhances accuracy. A simpler, more focused prompt reduces the cognitive load on the LLM, leading to more reliable and consistent outputs for each sub-task.

This flexibility is another key advantage. You can swap out, update, or optimize individual components without affecting the rest of the chain. For example, you might use a fast, cost-effective model like Gemini Flash for a simple classification step, and a more powerful model like Gemini Pro for a complex content generation step. This allows you to fine-tune the performance and cost of your workflow. Real-world case studies demonstrate this benefit; AppFolio, a property management AI company, used LangGraph (a framework for building stateful, multi-actor applications) to manage complex workflows, which allowed them to achieve an 80% performance boost in a text-to-data feature [[20]](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works).

However, prompt chaining is not without its downsides. One significant challenge is the risk of information loss between steps. As data is passed from one call to the next, critical context from early stages can be diluted or dropped entirely, a form of context decay [[22]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production). If a summary step is too aggressive, the subsequent translation step may lose important nuances. This is a form of compounding error, where a small mistake in an early step can cascade and lead to a completely wrong final output [[47]](https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge).

There is also an engineering overhead. You need to write "glue code" to manage the state and data flow between each call. This adds complexity compared to a single prompt. Finally, chaining multiple LLM calls increases both latency and cost. Each call adds to the total execution time and token count, which can be a critical factor in user-facing applications.

Despite these challenges, the control, reliability, and debuggability offered by prompt chaining make it an essential pattern for production AI systems.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's refactor our FAQ generation task into a clean, sequential workflow. Instead of one complex prompt, we will create a three-step chain:
1.  **Generate Questions**: An LLM call to create a list of questions based on the source content.
2.  **Answer Questions**: A separate LLM call to answer each question individually.
3.  **Find Sources**: A final LLM call to identify the sources used for each answer.

This modular approach allows us to control and validate each stage of the process, leading to a more reliable outcome.

Image 1: A flowchart illustrating the sequential FAQ generation pipeline.
```mermaid
flowchart LR
  %% Pipeline Stages
  A["Input Content<br/>(renewable energy webpages)"]
  B["Generate Questions"]
  C["Answer Questions"]
  D["Find Sources"]
  E["Final FAQ List"]

  %% Data Flow
  A -- "content" --> B
  B -- "list of questions" --> C
  C -- "answers, questions, original content" --> D
  D -- "processed information" --> E
```

1.  First, we create a function to generate a list of questions. The prompt is focused solely on this task, asking for a specific number of relevant questions and returning them in a structured list.
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
    
    # Test the question generation function
    questions = generate_questions(combined_content, n_questions=10)
    ```
    It outputs:
    ```text
    - What are the primary environmental and economic benefits of solar energy?
    - How do homeowners financially benefit from installing solar panels?
    - What is the main process by which wind turbines generate electricity?
    ...
    ```

2.  Next, we define a function to answer a single question. This prompt is instructed to use *only* the provided content, which helps ground the model and reduce hallucinations.
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

3.  Our third function is responsible for identifying the sources for a given question-and-answer pair. This separation ensures that citation is a deliberate verification step rather than an afterthought.
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

4.  Finally, we combine these functions into a sequential workflow. We first generate all questions, then loop through each one to generate an answer and find its sources.
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
    
    [
      {
        "question": "What are the primary financial benefits of installing solar panels for homeowners, and are there any initial costs to consider?",
        "answer": "The primary financial benefits of installing solar panels for homeowners are significantly lowered monthly electricity bills and, in some cases, the ability to sell excess power back to the grid. The initial installation cost can be high.",
        "sources": [
          "The Benefits of Solar Energy"
        ]
      },
      ...
    ]
    ```

This chained workflow took around 22 seconds to process four questions. Each step is clear, and if a source is missed or an answer is incorrect, we can easily inspect the intermediate outputs to find the problem. This level of control is essential for building production-grade applications.

## Optimizing Sequential Workflows With Parallel Processing

The sequential workflow is reliable but slow. Since the processing for each question is independent of the others, we do not need to wait for one to finish before starting the next. We can significantly speed up the process by running these tasks in parallel. This is a common optimization pattern for I/O-bound operations like making API calls to an LLM.

The trade-offs are straightforward. Sequential processing is predictable and simple to debug, but it is slow as tasks execute one by one. Parallel processing dramatically reduces the total execution time by running independent tasks concurrently. However, it introduces complexity in managing the concurrent operations and handling potential errors. For instance, if one of the parallel calls fails, you need a strategy to handle it without disrupting the others.

A critical real-world consideration when running parallel calls is API rate limiting. Services like Google Gemini or OpenAI impose limits on the number of requests you can make per minute (RPM) and tokens you can process per minute (TPM) [[7]](https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903). Aggressively parallelizing without managing these limits will result in `429` errors and failed requests [[8]](https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt). Production-grade systems must implement robust strategies like exponential backoff with jitter, which prevents multiple clients from retrying simultaneously, and retry budgets to avoid cascading failures. Advanced patterns include using circuit breakers, which temporarily halt requests to a failing service, and request queues to smooth out bursty traffic [[9]](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production).

For our example, we will use Python's `asyncio` library to run the "answer" and "find sources" steps in parallel for each question.

1.  We start by creating asynchronous versions of our `answer_question` and `find_sources` functions. These `async` functions can be run concurrently by an event loop.
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

2.  Next, we create a function `process_question_parallel` that generates an answer and finds sources for a single question.
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

3.  Finally, our parallel workflow first generates the list of questions synchronously and then uses `asyncio.gather` to execute `process_question_parallel` for all questions concurrently.
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
    
    [
      {
        "question": "What are the primary environmental and economic benefits of using solar energy?",
        "answer": "The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels.\n\nThe primary economic benefits include significantly lower monthly electricity bills, the ability to sell excess power back to the grid, long-term savings, and contributing to energy independence for nations.",
        "sources": [
          "The Benefits of Solar Energy"
        ]
      },
      ...
    ]
    ```

By running the tasks in parallel, we reduced the execution time from 22 seconds to just 9 seconds—a significant improvement. For I/O-bound tasks like LLM API calls, `asyncio` is generally faster than threading because it avoids the overhead of managing OS threads [[28]](https://testdriven.io/blog/python-concurrency-parallelism/). This pattern is highly effective for batch processing or any scenario where you have multiple independent tasks to perform.

## Introducing Dynamic Behavior: Routing and Conditional Logic

Sequential and parallel workflows are powerful, but they follow a fixed path. Real-world applications often require dynamic behavior, where the workflow adapts based on the user's input or intermediate results. This is where routing comes in. Routing uses conditional logic to direct a task down different paths, enabling you to build more intelligent and responsive systems.

The core idea is to use an LLM as a classifier or a "dispatcher" agent. This first LLM call analyzes the input and determines which specialized handler or sub-workflow is best suited to handle it. This is another application of the "divide and conquer" principle. Instead of a single, monolithic prompt that tries to handle every possible user intent, you create specialized prompts for each case (e.g., technical support, billing inquiry, general question). This keeps each prompt focused and optimized for a single responsibility, which generally leads to higher accuracy and easier maintenance [[51]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

Routing is essential for tasks where the required processing varies widely based on the input. In customer support, for example, a query about a billing error requires a completely different set of actions and information than a technical troubleshooting question. A routing workflow can identify the user's intent and trigger the appropriate path, ensuring the user gets the most relevant and efficient response. This dynamic branching is a key building block for creating more sophisticated, agent-like behaviors.

## Building a Basic Routing Workflow

Let's build a simple routing workflow for a customer service system. The goal is to classify an incoming user query into one of three intents—`Technical Support`, `Billing Inquiry`, or `General Question`—and then route it to a specialized handler that generates an appropriate first response.

This two-stage architecture—classify then handle—is a robust pattern for improving precision. The classification step creates a clear, structured taxonomy of intents, which is crucial for handling diverse user requests reliably [[11]](https://www.emergentmind.com/topics/llm-based-prompt-routing).

Image 2: A flowchart illustrating a basic routing workflow for customer service.
```mermaid
graph TD
    A["User Input"] --> B{"Intent Classification"}
    B -->|"Technical"| C["Technical Support Handler"]
    B -->|"Billing"| D["Billing Inquiry Handler"]
    B -->|"General"| E["General Question Handler"]
    C --> F["Final Response"]
    D --> F
    E --> F
```

1.  First, we define our intent classification system. We use an `Enum` and a Pydantic model to create a strict schema for our classifier. The prompt asks the LLM to categorize the user's query based on the provided list of intents.
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
    
    
    query_1 = "My internet connection is not working."
    query_2 = "I think there is a mistake on my last invoice."
    query_3 = "What are your opening hours?"
    
    intent_1 = classify_intent(query_1)
    intent_2 = classify_intent(query_2)
    intent_3 = classify_intent(query_3)
    ```
    It outputs:
    ```text
    Query: My internet connection is not working. -> Intent: IntentEnum.TECHNICAL_SUPPORT
    Query: I think there is a mistake on my last invoice. -> Intent: IntentEnum.BILLING_INQUIRY
    Query: What are your opening hours? -> Intent: IntentEnum.GENERAL_QUESTION
    ```

2.  Next, we define our specialized handlers. Each handler has a prompt tailored to its specific role. The `handle_query` function acts as our router, executing the correct prompt based on the classified intent. We also include a default route to handle any unexpected classifications gracefully.
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
    
    
    response_1 = handle_query(query_1, intent_1)
    ```
    It outputs:
    ```text
    Hello there! I'm sorry to hear you're having trouble with your internet connection. That can definitely be frustrating.
    
    To help me understand what's going on and assist you best, could you please provide a few more details?
    ...
    ```

This routing pattern allows you to build complex, multi-path workflows while keeping each individual component simple and maintainable. It is a foundational technique for creating systems that can handle a wide variety of tasks and user inputs in a structured and reliable way.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The orchestrator-worker pattern takes dynamic workflows a step further. Instead of a fixed set of branches, a central "orchestrator" LLM dynamically breaks down a complex query into a series of sub-tasks. It then delegates these sub-tasks to specialized "worker" LLMs or tools, which can run in parallel. Finally, a "synthesizer" LLM gathers the results from the workers and combines them into a single, coherent response [[16]](https://agents.kour.me/orchestrator-worker/).

This pattern is exceptionally well-suited for complex problems where the necessary steps cannot be predicted in advance [[19]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers). For example, analyzing a financial report might involve extracting key metrics, comparing them to historical data, and generating a summary—the exact sub-tasks depend on the content of the report. The key difference from simple parallelization is this flexibility; the orchestrator determines the sub-tasks at runtime based on the specific input [[53]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers).

Image 3: A flowchart depicting the orchestrator-worker pattern for dynamic task decomposition.
```mermaid
flowchart LR
  %% External interfaces
  A["User Query<br/>(complex customer request)"]

  %% Core processing agents
  B["Orchestrator"]

  %% Specialized Worker LLMs
  subgraph "Worker LLMs (parallel execution)"
    C1["Billing Worker"]
    C2["Product Return Worker"]
    C3["Order Status Worker"]
  end

  %% Core processing agents
  D["Synthesizer"]

  %% External interfaces
  E["Final Customer Response"]

  %% Primary data flows
  A -- "sends" --> B
  B -- "dynamically decomposes & delegates sub-task" --> C1
  B -- "dynamically decomposes & delegates sub-task" --> C2
  B -- "dynamically decomposes & delegates sub-task" --> C3
  C1 -- "returns individual result" --> D
  C2 -- "returns individual result" --> D
  C3 -- "returns individual result" --> D
  D -- "gathers & combines results into" --> E

  %% Visual grouping
  classDef external stroke-dasharray: 5,5
  classDef orchestrator_synth stroke-width:2px
  classDef worker_llm stroke-dasharray: 3,3

  class A,E external
  class B,D orchestrator_synth
  class C1,C2,C3 worker_llm
```

However, this pattern introduces its own challenges. The orchestrator can become a bottleneck if it is too slow. It might also fail to decompose the task completely or generate conflicting sub-tasks. The synthesizer then faces the difficult job of reconciling potentially diverse or contradictory outputs from the workers. Designing clear boundaries, consistent schemas, and robust conflict-resolution strategies for the synthesizer is crucial for success [[32]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent).

Let's implement this pattern for our customer service example, handling a complex query that involves a billing issue, a product return, and an order status request all at once.

1.  The orchestrator's job is to parse the user's query and break it down into a list of structured tasks. We define a schema for the possible tasks and prompt the LLM to generate a list of tasks that match the query.
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

2.  We then define our worker functions. Each worker is a specialist. The `handle_billing_worker` simulates opening an investigation, the `handle_return_worker` generates a return authorization, and the `handle_status_worker` fetches order details. For this example, they return mock data.
    ```python
    # Billing Worker Implementation
    class BillingTask(BaseModel): ...
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask: ...
    
    # Product Return Worker
    class ReturnTask(BaseModel): ...
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask: ...
    
    # Order Status Worker
    class StatusTask(BaseModel): ...
    def handle_status_worker(order_id: str) -> StatusTask: ...
    ```

3.  The synthesizer's role is to take the structured outputs from all the workers and compose a single, user-friendly message. It is prompted to combine the different pieces of information into a cohesive email.
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
    
    
    def synthesizer(results: list[Task]) -> str: ...
    ```

4.  Finally, we tie everything together in our main pipeline function, `process_user_query`. This function calls the orchestrator, dispatches tasks to the appropriate workers, and then uses the synthesizer to generate the final response.
    ```python
    def process_user_query(user_query):
        """Processes a query using the Orchestrator-Worker-Synthesizer pattern."""
    
        pretty_print.wrapped(
            text=user_query,
            title="User query"
        )
    
        # 1. Run orchestrator
        tasks_list = orchestrator(user_query)
        ...
    
        # 2. Run workers
        worker_results = []
        if tasks_list:
            for task in tasks_list:
                if task.query_type == QueryTypeEnum.BILLING_INQUIRY:
                    worker_results.append(handle_billing_worker(task.invoice_number, user_query))
                ...
    
        # 3. Run synthesizer
        if worker_results:
            final_user_message = synthesizer(worker_results)
            ...
    
    complex_customer_query = """
    Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.
    Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.
    Finally, can you give me an update on my order #A-12345?
    """.strip()
    
    process_user_query(complex_customer_query)
    ```
    First, the orchestrator deconstructs the query into three distinct tasks:
    ```text
    Deconstructed task 1:
    {
      "query_type": "BillingInquiry",
      "invoice_number": "INV-7890",
      ...
    }
    
    Deconstructed task 2:
    {
      "query_type": "ProductReturn",
      "product_name": "SuperWidget 5000",
      ...
    }
    
    Deconstructed task 3:
    {
      "query_type": "StatusUpdate",
      "order_id": "A-12345",
      ...
    }
    ```
    Then, each worker processes its assigned task and returns a structured result. For example, the billing worker returns:
    ```text
    Worker result 1:
    {
      "query_type": "BillingInquiry",
      "invoice_number": "INV-7890",
      "user_concern": "The invoice seems higher than expected.",
      "action_taken": "An investigation (Case ID: INV_CASE_6301) has been opened regarding your concern.",
      "resolution_eta": "2 business days"
    }
    ```
    Finally, the synthesizer combines all worker results into a single, helpful email to the customer:
    ```text
    Final synthesized response:
    Dear Customer,
    
    Thank you for reaching out to us. Here's an update on your requests:
    
    Regarding your BillingInquiry:
      - Invoice Number: INV-7890
      - Your Stated Concern: "The invoice seems higher than expected."
      - Our Action: An investigation (Case ID: INV_CASE_6301) has been opened regarding your concern.
      - Expected Resolution: We will get back to you within 2 business days.
    
    Regarding your ProductReturn:
      - Product: SuperWidget 5000
      - Reason for Return: "it's not compatible with my system"
      ...
    
    Regarding your StatusUpdate:
      - Order ID: A-12345
      - Current Status: Shipped
      ...
    
    We hope this information is helpful. Please let us know if you have any other questions.
    
    Best regards,
    Support Team
    ```

This pattern demonstrates how to build a sophisticated system that can dynamically handle complex, multi-part queries in a structured and scalable way.

## Conclusion

We have journeyed from the pitfalls of monolithic prompts to the power of modular workflows. By breaking down complex problems into smaller, manageable steps, we can build AI systems that are more reliable, debuggable, and easier to maintain. We have seen how sequential chaining provides control, parallelization offers speed, routing enables dynamic behavior, and the orchestrator-worker pattern delivers flexibility for unpredictable tasks.

These patterns are not just theoretical concepts; they are the essential building blocks for virtually any production-grade LLM application. They represent a fundamental shift from simple prompt engineering to a more systematic approach to AI engineering. As you continue your journey, you will find yourself combining these patterns to create sophisticated, multi-agent systems. In our upcoming lessons, we will build upon this foundation, exploring how to give your workflows the ability to use tools, plan their actions, and remember past interactions.

## References

- [2]  https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [3]  https://aclanthology.org/2025.ommm-1.4.pdf
- [7]  https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903
- [8]  https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt
- [9]  https://tianpan.co/blog/2026-03-11-llm-api-resilience-production
- [11]  https://www.emergentmind.com/topics/llm-based-prompt-routing
- [16]  https://agents.kour.me/orchestrator-worker/
- [19]  https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers
- [20]  https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works
- [22]  https://futureagi.substack.com/p/how-tool-chaining-fails-in-production
- [28]  https://testdriven.io/blog/python-concurrency-parallelism/
- [32]  https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent
- [36]  https://www.decodingai.com/p/stop-building-ai-agents-use-these
- [41]  https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a
- [46]  https://mlpills.substack.com/p/issue-110-llm-workflow-patterns
- [47]  https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge
- [51]  https://www.decodingai.com/p/stop-building-ai-agents-use-these
- [53]  https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers