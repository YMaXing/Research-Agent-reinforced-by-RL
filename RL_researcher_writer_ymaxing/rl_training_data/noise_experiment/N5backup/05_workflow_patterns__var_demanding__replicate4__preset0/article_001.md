# Lesson 5: Basic AI Workflow Patterns

In the previous lessons, we’ve covered the fundamentals of AI Engineering. We explored the agent landscape, distinguished between rule-based workflows and autonomous agents, and covered context engineering. We also learned how to get reliable, structured data *out* of an LLM. Now, we will combine these ideas to build our first multi-step AI systems.

On a recent project, our first attempt at building a complex system involved a single, massive prompt. It was supposed to do everything: analyze a document, extract key points, summarize sections, and generate a report. The results were a mess. The LLM would get confused, miss steps, or ignore constraints. It was a classic case of trying to make one person do the job of an entire team. This experience taught us a critical lesson: in AI engineering, as in traditional software, modularity is key.

This lesson is about breaking down that monolithic prompt. We will explore the foundational patterns for building robust LLM workflows: chaining, parallelization, routing, and the orchestrator-worker model. You will learn why a "divide and conquer" strategy is almost always better than a single, complex LLM call. We will build a sequential pipeline for generating Frequently Asked Questions (FAQs) and a dynamic routing system for customer service, all from scratch using Google Gemini.

By the end of this lesson, you will understand how to:
- Code sequential workflows by breaking tasks into steps for better consistency.
- Implement parallel workflows to run independent tasks for higher speed.
- Build routing workflows to classify user intent and direct them to specialized handlers.
- Use the orchestrator-worker pattern to dynamically decompose complex queries.

## The Challenge with Complex Single LLM Calls

When you first start building with LLMs, it’s tempting to put all your instructions into one big prompt. The thinking is, "The model is smart, it can handle it." While this might work for simple demos, it quickly falls apart in production when faced with complex, multi-step tasks. Relying on a single, monolithic LLM call introduces several engineering challenges that make your system unreliable and hard to maintain.

First, debugging becomes a nightmare. If the final output is wrong, where did the failure occur? A single prompt is a black box, making it nearly impossible to pinpoint the source of an error. Was it a misinterpretation of one instruction out of ten? Did the model fail at an intermediate reasoning step? With a monolithic prompt, you have no visibility into the internal process, turning debugging into a frustrating guessing game. This is a significant issue in production, where traceability is essential for reliability.

Second, these systems lack modularity, which is a core principle of good software engineering. You cannot test, update, or optimize one piece of logic without rewriting the entire prompt and risking unintended side effects. This makes iterative development slow and fragile. If you want to swap out the summarization logic or improve the data extraction step, you have to re-validate the entire system from scratch. This lack of separation of concerns makes the application brittle and difficult to scale or maintain over time.

A well-documented issue with long, complex prompts is the "lost-in-the-middle" problem. Research from Stanford and UC Berkeley found that LLMs pay the most attention to information at the beginning and end of their context window, often ignoring important details buried in the middle [[2]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2). This happens due to architectural factors like causal attention masking, where early tokens get more cumulative attention, and positional encoding decay, which weakens the signal from middle tokens. Stuffing too many instructions into a single call increases the chance that the model will simply overlook a key requirement.

Finally, a single complex prompt can be inefficient and unreliable. Research has shown that as the number of requirements in a prompt increases, model accuracy drops. One study found that GPT-4o's accuracy fell from 98.7% with one requirement to 85% with 19 requirements [[5]](https://arxiv.org/html/2505.13360v1). The cognitive load on the model becomes too high, leading to inconsistent outputs, hallucinations, or a complete failure to follow instructions. A study comparing single-task and multitask prompts found that while some models can handle complexity, many perform better on focused, single-task prompts, highlighting that there is no one-size-fits-all rule [[1]](https://www.mdpi.com/2079-9292/13/23/4712).

Let's see this in practice. We will start by setting up our Gemini client and defining our model.

1.  First, we'll set up our Python environment and initialize the Gemini client. We will use `gemini-2.5-flash`, which is fast and cost-effective for these examples.

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

    It outputs:

    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

2.  Next, we will create three mock webpages about renewable energy that will serve as our source content.

    ```python
    webpage_1 = {
        "title": "The Benefits of Solar Energy",
        "content": """
        Solar energy is a renewable powerhouse, offering numerous environmental and economic benefits.
        By converting sunlight into electricity through photovoltaic (PV) panels, it reduces reliance on fossil fuels,
        thereby cutting down greenhouse gas emissions. Homeowners who install solar panels can significantly
        lower their monthly electricity bills, and in some cases, sell excess power back to the grid.
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
        releasing it when it's needed is vital for a stable power grid. The most common form of
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

3.  Now, let's create a complex prompt that asks the LLM to generate questions, find answers, and cite sources all in one go. We will use Pydantic models, which we covered in Lesson 4, to structure the output.

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

    ```json
    {
      "question": "What is solar energy and how does it work?",
      "answer": "Solar energy is a renewable powerhouse that converts sunlight into electricity through photovoltaic (PV) panels.",
      "sources": [
        "The Benefits of Solar Energy"
      ]
    }
    ...
    {
      "question": "Why is energy storage vital for renewable energy sources like solar and wind?",
      "answer": "Effective energy storage is key to unlocking the full potential of renewable sources because it allows storing excess energy when plentiful and releasing it when needed, which is vital for a stable power grid.",
      "sources": [
        "Energy Storage Solutions",
        "Understanding Wind Turbines"
      ]
    }
    ```

While this output looks acceptable, the more complex the instructions, the higher the chance of inconsistencies. For example, the model might fail to cite all relevant sources or generate a question that cannot be answered from the text. This unreliability makes it difficult to build a production-ready system. A better approach is to break the problem down into smaller, more manageable steps.

## The Power of Modularity: Why Chain LLM Calls?

Instead of a single, complex prompt, we can use prompt chaining: a sequence of simpler, focused LLM calls where the output of one step becomes the input for the next. This "divide and conquer" strategy is a cornerstone of building reliable AI workflows and mirrors how we, as humans, tackle complex problems by breaking them into smaller tasks [[18]](https://www.promptingguide.ai/techniques/prompt_chaining).

This modular approach brings several engineering benefits. First, it improves accuracy and reliability. A simpler, more targeted prompt reduces the cognitive load on the LLM, leading to more consistent and correct outputs for each sub-task. By focusing the model on one thing at a time—like generating questions first, then answering them—you reduce the chances of it getting confused or missing a step.

Second, it makes your system far easier to debug and maintain. When a failure occurs, you can isolate the exact step in the chain that caused the problem. This modularity allows you to test, version, and improve individual components without impacting the rest of the workflow. For example, AppFolio, a property management AI company, used LangGraph to manage complex workflows and achieved a significant performance boost in text-to-data functionality, from 40% to 80% accuracy, by being able to isolate and optimize specific steps [[17]](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works). Similarly, Acxiom used LangSmith to gain visibility into their multi-agent interactions, which is only practical when the system is composed of discrete, observable parts [[17]](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works).

Third, it offers greater flexibility. You can swap out components, experiment with different models for different steps, or add new logic without re-engineering the entire system. For instance, you could use a fast, cost-effective model like Gemini Flash for a simple classification task and a more powerful model like Gemini Pro for a complex generation task within the same workflow. This ability to mix and match is essential for optimizing both performance and cost in production.

However, chaining is not without its trade-offs. The most obvious is increased latency and cost, as you are making multiple API calls instead of one. Each additional call adds to the total execution time.

Another significant challenge is the risk of information loss between steps. In a long chain, important context from early steps can be diluted or pushed out of the context window by intermediate results [[19]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production). If one step in the chain produces an incorrect or partial result, that error can propagate and compound, leading to a cascading failure. To mitigate this, it is essential to use structured state objects to pass data, keep chains short (ideally under five or six calls), and validate inputs and outputs at every boundary using schemas like Pydantic [[19]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production).

Despite these challenges, the control and reliability gained from modular workflows make them a superior choice for most production use cases. Now that we understand the theory, let's refactor our FAQ generation task into a sequential workflow.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's break down our FAQ generation task into a three-step sequential pipeline:
1.  **Generate Questions**: Create a list of questions based on the source content.
2.  **Answer Questions**: For each question, generate a concise answer.
3.  **Find Sources**: For each answer, identify the source documents used.

This approach ensures each step is focused and produces a reliable, traceable output. By separating concerns, we can craft a specific prompt for each sub-task, leading to higher quality results and making the entire process easier to debug and maintain.

Image 1: The sequential FAQ generation pipeline.
```mermaid
flowchart LR
    "Input Content" --> "Generate Questions"
    "Generate Questions" --> "Answer Questions"
    "Answer Questions" --> "Find Sources"
    "Find Sources" --> "FAQ List Output"
```

1.  First, we create a function dedicated to generating questions. The prompt is simple and direct: given the content, generate a specified number of relevant questions. We use a Pydantic model, `QuestionList`, to ensure the output is a clean list of strings. This is the first link in our chain.

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
    What are the primary environmental and economic benefits of solar energy?
    How do homeowners financially benefit from installing solar panels?
    ...
    ```

2.  Next, we define a function to answer a single question. This prompt explicitly instructs the model to use *only* the provided content, which helps ground the response and reduce hallucinations. This function will be called for each question generated in the previous step.

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
        """
        answer_response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt_answer_question.format(question=question, combined_content=content),
        )
        return answer_response.text
    
    # Test the answer generation function
    test_question = questions[0]
    test_answer = answer_question(test_question, combined_content)
    ```

    For the question, "What are the primary environmental and economic benefits of solar energy?", it outputs:

    ```text
    The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels. Economically, it allows homeowners to significantly lower their monthly electricity bills and potentially sell excess power back to the grid.
    ```

3.  Finally, we create a function to identify which sources were used for a given question-answer pair. This step adds traceability to our system, making it clear where each piece of information came from. Again, we use a Pydantic model, `SourceList`, for a structured output.

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
    
    # Test the source finding function
    test_sources = find_sources(test_question, test_answer, combined_content)
    ```

    It correctly identifies the source:

    ```text
    The Benefits of Solar Energy
    ```

4.  Now, we combine these functions into a complete sequential workflow. The `sequential_workflow` function orchestrates the entire process: it calls `generate_questions` once, then iterates through each question, calling `answer_question` and `find_sources` in sequence.

    ```python
    def sequential_workflow(content, n_questions=10) -> list[FAQ]:
        """
        Execute the complete sequential workflow for FAQ generation.
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

The final result is a structured list of FAQs, each with a question, a grounded answer, and a clear list of sources. This modular pipeline is more reliable and easier to debug than our initial monolithic approach. However, processing four questions took over 20 seconds. This latency is acceptable for some applications but too slow for many real-time use cases. The sequential approach is reliable but slow. Let's see how to speed it up.

## Optimizing Sequential Workflows With Parallel Processing

While the sequential workflow improves reliability, its latency can be a bottleneck. Since the processing for each question (answering and finding sources) is independent of the others, we can run these tasks in parallel. This can dramatically reduce the total execution time, especially when dealing with a large number of items.

We will use Python's `asyncio` library to run the `answer_question` and `find_sources` calls concurrently for all questions. This is a common pattern for speeding up I/O-bound operations, such as making multiple API calls to an LLM.

1.  First, we need asynchronous versions of our `answer_question` and `find_sources` functions. The `google-genai` library provides an async client (`client.aio`) that we can use. The function signatures are almost identical, but we add the `async` keyword and use `await` for the API call.

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

2.  Next, we create a function that processes a single question by running its sub-tasks in parallel. This function, `process_question_parallel`, will be the unit of work that we distribute across our concurrent execution.

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

3.  Finally, we build the main parallel workflow. It first generates the questions synchronously (since this is a single API call) and then uses `asyncio.gather` to execute the processing for all questions concurrently. `asyncio.gather` takes a list of awaitable tasks and runs them all at the same time, waiting for all to complete before returning the results.

    ```python
    async def parallel_workflow(content: str, n_questions: int = 10) -> list[FAQ]:
        """
        Execute the complete parallel workflow for FAQ generation.
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

By running the tasks in parallel, we reduced the total processing time from 22.20 seconds to just 8.98 seconds. This is a significant improvement. For I/O-bound tasks, `asyncio` is often faster than multithreading because it avoids the overhead of managing OS threads and context switching [[22]](https://testdriven.io/blog/python-concurrency-parallelism/).

However, a critical real-world consideration is API rate limiting. Firing off many parallel requests can quickly exhaust your limits, causing your calls to fail. Users of the Gemini API, for example, have reported aggressive rate limiting that can drop requests even when using standard retry logic [[6]](https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903). Production-grade systems must implement robust strategies like exponential backoff with full jitter to avoid creating "retry storms" that amplify the load on the API [[21]](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production). Other techniques include using a retry budget to fail fast when an endpoint is degraded and implementing circuit breakers to temporarily stop sending requests to a failing service [[21]](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production).

We've improved speed, but our workflow is still static; it follows the same path every time. Let's add dynamic behavior to make our system more intelligent.

## Introducing Dynamic Behavior: Routing and Conditional Logic

So far, our workflows have been linear. But what if you need to handle different types of inputs in different ways? A customer service bot, for example, needs to distinguish between a billing question and a technical support issue. This is where routing comes in.

Routing uses conditional logic to direct a workflow down different paths based on the input or an intermediate state. It’s another application of the "divide and conquer" principle. Instead of creating one massive, complicated prompt that tries to handle every possible scenario, you create multiple smaller, specialized prompts. An initial LLM call acts as a classifier or "dispatcher," analyzing the input and deciding which specialized prompt is the right tool for the job [[16]](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/).

This approach has several advantages. It keeps your prompts focused and optimized for a single task, which generally improves accuracy. It makes the system more maintainable, as you can update the logic for one path without affecting others. It also provides a natural way to handle escalations or fallbacks; if no specific route matches, you can direct the query to a default handler or a human agent. This pattern is widely used in production. For instance, Adyen, a global fintech platform, deployed a smart ticket routing system powered by LLMs to improve accuracy and response times in their support operations [[17]](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works).

The key to a robust routing system is a clear, precise, and comprehensive taxonomy of intents. You need to define your categories carefully and provide high-quality, representative examples for each, especially for edge cases, to ensure the classification step is accurate. For complex scenarios, a two-stage architecture can improve precision, where an initial model retrieves candidate intents and a second, more powerful LLM makes the final selection. Now, let's build a simple routing system for a customer service use case.

## Building a Basic Routing Workflow

We will build a simple customer service router that classifies a user's query and directs it to one of three specialized handlers: Technical Support, Billing Inquiry, or General Question. This two-step process—classify then handle—is a common and effective pattern for building dynamic, multi-path workflows.

Image 2: The customer service intent classification routing workflow.
```mermaid
flowchart LR
  A["User Input"] --> B["Intent Classification"]

  B -->|Classified as "Technical"| C["Technical Support Handler"]
  B -->|Classified as "Billing"| D["Billing Inquiry Handler"]
  B -->|Classified as "General"| E["General Question Handler"]

  C --> F["Final Responses"]
  D --> F
  E --> F
```

1.  First, we define the possible intents using a Pydantic model and a Python `Enum`. This creates a clear schema for our classifier, ensuring the LLM's output is constrained to one of the valid categories. The prompt itself is straightforward, asking the model to classify the query based on the provided list of categories.

    ```python
    class IntentEnum(str, Enum):
        """
        Defines the allowed values for the 'intent' field.
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
    ```

2.  Next, we create the `classify_intent` function. It uses the Gemini API's structured output feature, which we covered in Lesson 4, to ensure the response conforms to our `UserIntent` schema. This is a robust way to get reliable classification results.

    ```python
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

    The classifier correctly identifies the intents:

    ```text
    Query 1: Technical Support
    Query 2: Billing Inquiry
    Query 3: General Question
    ```

3.  Now, we define our specialized handlers. Each one is a simple prompt tailored to a specific intent, giving a persona and clear instructions for the desired response. This separation of concerns is what makes the routing pattern powerful.

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

4.  Finally, we create the `handle_query` function, which acts as our router. It takes the user's query and the classified intent, and then uses a simple `if/elif/else` block to call the appropriate handler. A default or catch-all route is included to handle any unexpected classifications, ensuring the system fails gracefully.

    ```python
    def handle_query(user_query: str, intent: str) -> str:
        """Routes a query to the correct handler based on its classified intent."""
        if intent == IntentEnum.TECHNICAL_SUPPORT:
            prompt = prompt_technical_support.format(user_query=user_query)
        elif intent == IntentEnum.BILLING_INQUIRY:
            prompt = prompt_billing_inquiry.format(user_query=user_query)
        else: # Also handles GENERAL_QUESTION and any other case
            prompt = prompt_general_question.format(user_query=user_query)
        
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return response.text
    
    
    response_1 = handle_query(query_1, intent_1)
    response_2 = handle_query(query_2, intent_2)
    response_3 = handle_query(query_3, intent_3)
    ```

    For the query "My internet connection is not working," the system correctly routes it to the technical support handler, which responds:

    ```text
    Hello there! I'm sorry to hear you're having trouble with your internet connection... To help me understand what's going on... could you please provide a few more details? ... Have you already tried any troubleshooting steps yourself?
    ```

This simple routing workflow is far more robust and maintainable than a single, monolithic prompt. Routing is great for pre-defined paths, but what if the sub-tasks themselves are unpredictable and need to be determined on the fly? For that, we need a more dynamic pattern.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The orchestrator-worker pattern is a more advanced workflow where a central "orchestrator" LLM dynamically breaks down a complex task into smaller sub-tasks and delegates them to specialized "worker" LLMs or tools [[20]](https://www.anthropic.com/engineering/building-effective-agents), [[15]](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb). The orchestrator then synthesizes the results from the workers into a final, cohesive response.

This pattern is ideal for complex problems where the required steps cannot be known in advance, such as open-ended research, multi-step data analysis, or generating a complex report. Unlike simple parallelization with pre-defined tasks, the orchestrator's key strength is its flexibility; it determines the sub-tasks at runtime based on the specific input [[15]](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb). This allows the system to adapt to a wide range of unpredictable queries. For example, Athena Intelligence uses a graph-based orchestrator to manage multi-agent workflows for generating enterprise research reports, a task where the necessary data sources and analysis steps are highly variable [[17]](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works).

Image 3: The orchestrator-worker pattern, from initial query to final response, including parallel worker processing.
```mermaid
flowchart LR
  %% Initial Query
  A["Complex User Query"]

  %% Orchestration Layer
  subgraph "Orchestration"
    B["Orchestrator LLM<br/>(Analyzes & Decomposes Task)"]
  end

  %% Worker Processing Layer
  subgraph "Worker LLMs (Parallel Processing)"
    C1["Worker 1<br/>(Handles Sub-task A)"]
    C2["Worker 2<br/>(Handles Sub-task B)"]
    CN["Worker N<br/>(Handles Sub-task N)"]
  end

  %% Synthesis Layer
  subgraph "Synthesis"
    D["Synthesizer LLM<br/>(Combines Results)"]
  end

  %% Final Output
  E["Cohesive Final Response"]

  %% Flow connections
  A -- "submits" --> B
  B -- "delegates sub-task" --> C1
  B -- "delegates sub-task" --> C2
  B -- "delegates sub-task" --> CN

  C1 -- "returns result" --> D
  C2 -- "returns result" --> D
  CN -- "returns result" --> D

  D -- "produces" --> E
```

However, this pattern introduces its own challenges. The orchestrator can become a performance bottleneck if it handles too many tasks synchronously. The decomposition step might be incomplete, or workers could produce conflicting outputs that are difficult for the synthesizer to reconcile. To build a robust system, you need clear schemas for communication between the orchestrator and workers, strategies for conflict resolution, and careful prompt engineering for the synthesizer to handle diverse inputs.

Let's build an orchestrator-worker system to handle a complex customer service query that involves multiple, distinct actions.

1.  We start by defining the orchestrator. Its job is to analyze a user query and break it down into a list of structured tasks. We will use Pydantic to define the schema for these tasks, ensuring the output is predictable and machine-readable.

    ```python
    class QueryTypeEnum(str, Enum):
        """The type of query to be handled."""
        BILLING_INQUIRY = "BillingInquiry"
        PRODUCT_RETURN = "ProductReturn"
        STATUS_UPDATE = "StatusUpdate"
    
    class Task(BaseModel):
        """A task to be performed."""
        query_type: QueryTypeEnum = Field(description="The type of query to be handled.")
        invoice_number: str | None = Field(description="The invoice number...", default=None)
        product_name: str | None = Field(description="The name of the product...", default=None)
        reason_for_return: str | None = Field(description="The reason for returning...", default=None)
        order_id: str | None = Field(description="The order ID...", default=None)
    
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

2.  Next, we implement our specialized workers. Each worker is a function that handles a specific `query_type`. In a real-world application, these workers would interact with backend systems, databases, or external APIs. Here, we will simulate those actions to demonstrate the pattern.

    ```python
    # Billing Worker
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
        # ... simulates opening an investigation
        return task
    
    # Product Return Worker
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
        # ... simulates generating an RMA number
        return task
    
    # Order Status Worker
    def handle_status_worker(order_id: str) -> StatusTask:
        # ... simulates fetching order status
        return task
    ```

3.  After the workers have executed, we need a "synthesizer" to combine their structured outputs into a single, user-friendly response. The synthesizer's prompt is designed to take a list of structured results and weave them into a coherent narrative.

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
        # ... formats results into bullet points
        formatted_results = "\n\n".join(bullet_points)
        prompt = prompt_synthesizer.format(formatted_results=formatted_results)
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    ```

4.  Now, let's test the complete pipeline with a complex query that requires all three workers. The `process_user_query` function ties everything together, calling the orchestrator, dispatching tasks to the appropriate workers, and finally, using the synthesizer to generate the final response.

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
        
        # 3. Run synthesizer
        if worker_results:
            final_user_message = synthesizer(worker_results)
            # ... print final message
    
    # Test with customer query
    complex_customer_query = """
    Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.
    Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.
    Finally, can you give me an update on my order #A-12345?
    """.strip()
    
    process_user_query(complex_customer_query)
    ```

First, the orchestrator correctly decomposes the query into three distinct tasks: a billing inquiry, a product return, and a status update. Then, each worker executes its simulated action and returns a structured result. Finally, the synthesizer combines these results into a clear and helpful email to the customer.

The final synthesized response looks like this:

```text
Hi there,

I've looked into your requests and here's a summary of the actions taken:

Regarding your BillingInquiry:
  - Invoice Number: INV-7890
  - Your Stated Concern: "It seems higher than I expected."
  - Our Action: An investigation (Case ID: INV_CASE_5691) has been opened regarding your concern.
  - Expected Resolution: We will get back to you within 2 business days.

Regarding your ProductReturn:
  - Product: SuperWidget 5000
  - Reason for Return: "it's not compatible with my system"
  - Return Authorization (RMA): RMA-68407
  - Instructions: Please pack the 'SuperWidget 5000' securely...

Regarding your StatusUpdate:
  - Order ID: A-12345
  - Current Status: Shipped
  - Carrier: SuperFast Shipping
  - Tracking Number: SF252998
  - Delivery Estimate: Tomorrow

If you have any other questions, please let me know.

Best regards,
Your Support Team
```

This pattern, while more complex to implement, provides incredible flexibility and power. However, it also introduces challenges, such as the orchestrator becoming a bottleneck or workers producing conflicting outputs. We will explore advanced strategies for managing these issues in future lessons.

## Conclusion

In this lesson, we moved beyond single, monolithic prompts and explored the fundamental patterns for building modular and reliable AI workflows. We learned that breaking down complex tasks into smaller, focused steps is essential for improving accuracy, simplifying debugging, and making our systems more maintainable.

We started with sequential prompt chaining, building a three-step pipeline to generate a structured FAQ from source documents. Then, we optimized this workflow using parallel processing with `asyncio`, significantly reducing latency. We then introduced dynamic behavior with routing, creating a customer service system that intelligently directs queries to specialized handlers. Finally, we explored the orchestrator-worker pattern, a powerful approach for dynamically decomposing unpredictable tasks.

These patterns—chaining, parallelization, routing, and orchestration—are not just theoretical concepts; they are the essential building blocks you will use to construct nearly any production-grade LLM application. Mastering them is the first major step from being a prompt engineer to becoming an AI engineer. In our next lesson, we will build on this foundation and learn how to give our workflows the ability to interact with the outside world through tools and function calling.

## References

- [1] Gozzi, M., & Di Maio, F. (2024). Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts. [https://www.mdpi.com/2079-9292/13/23/4712](https://www.mdpi.com/2079-9292/13/23/4712)
- [2] Thousand Miles AI. (2023). The "Lost in the Middle" Problem — Why LLMs Ignore the Middle of Your Context Window. [https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [3] FLARE framework analyzes GPT-4 Turbo 'Inconclusive' classifications. (2025). [https://aclanthology.org/2025.ommm-1.4.pdf](https://aclanthology.org/2025.ommm-1.4.pdf)
- [4] ZeMPE benchmark evaluates 13 LLMs on multi-problem prompts. (2025). [https://aclanthology.org/2025.gem-1.14.pdf](https://aclanthology.org/2025.gem-1.14.pdf)
- [5] Underspecification analysis of prompt requirements. (2025). [https://arxiv.org/html/2505.13360v1](https://arxiv.org/html/2505.13360v1)
- [6] Google Gemini API rate limiting challenges. (2024). [https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903](https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903)
- [7] Vertex AI API 429 error handling for parallel Gemini requests. (2024). [https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt](https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt)
- [8] LLM-Based Prompt Routing patterns. (2024). [https://www.emergentmind.com/topics/llm-based-prompt-routing](https://www.emergentmind.com/topics/llm-based-prompt-routing)
- [9] Universal Model Routing for dynamic LLM pools. (2025). [https://arxiv.org/html/2502.08773v1](https://arxiv.org/html/2502.08773v1)
- [10] Multi-LLM routing strategies on AWS for generative AI. (2024). [https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)
- [11] The Orchestrator-Worker pattern for dynamic task decomposition. (2024). [https://agents.kour.me/orchestrator-worker/](https://agents.kour.me/orchestrator-worker/)
- [12] DIY Orchestrator-Worker LLM Agent. (2024). [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [13] Building a self-healing AI orchestrator with Reflexion patterns. (2024). [https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/](https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/)
- [14] Orchestrator-Workers pattern for unpredictable subtasks. (2024). [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [15] Bowne, H. (2024). Basic Multi-LLM Workflows. [https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb)
- [16] Saboo, S. (2025). Developer’s guide to multi-agent patterns in ADK. [https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [17] Strick van Linschoten, A. (2025). LLMOps in Production: 457 Case Studies of What Actually Works. [https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works)
- [18] Saravia, E. (2024). Prompt Chaining Guide. [https://www.promptingguide.ai/techniques/prompt_chaining](https://www.promptingguide.ai/techniques/prompt_chaining)
- [19] Future AGI. (2026). How Tool Chaining Fails in Production LLM Agents and How to Fix It. [https://futureagi.substack.com/p/how-tool-chaining-fails-in-production](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production)
- [20] Anthropic. (2024). Building effective agents. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [21] Pan, T. (2026). LLM API Resilience in Production: Rate Limits, Failover, and the Hidden Costs of Naive Retry Logic. [https://tianpan.co/blog/2026-03-11-llm-api-resilience-production](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production)
- [22] TestDriven.io. (2023). Parallelism, Concurrency, and asyncio in Python. [https://testdriven.io/blog/python-concurrency-parallelism/](https://testdriven.io/blog/python-concurrency-parallelism/)
- [23] Anthropic. (2024). Chain Prompts. [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts)
- [24] LangChain. (2024). LangGraph Workflows. [https://langchain-ai.github.io/langgraphjs/tutorials/workflows](https://langchain-ai.github.io/langgraphjs/tutorials/workflows)
- [25] Anthropic. (2024). Claude 4 Best Practices. [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [26] Towards AI. (2024). AI Agents Course - Lesson 5 Notebook. [https://github.com/towardsai/course-ai-agents/blob/dev/lessons/05_workflow_patterns/notebook.ipynb](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/05_workflow_patterns/notebook.ipynb)