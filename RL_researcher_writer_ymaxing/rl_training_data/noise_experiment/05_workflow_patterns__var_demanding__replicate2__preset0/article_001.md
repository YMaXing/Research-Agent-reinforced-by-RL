# Basic Workflow Ingredients

In our previous lessons, we laid the groundwork for AI Engineering. We explored the AI agent landscape, the difference between rule-based LLM workflows and autonomous agents, and the art of context engineering. We also covered how to get reliable, structured data out of an LLM. Now, we will build on that foundation by exploring the fundamental patterns for creating multi-step LLM workflows.

Trying to solve a complex problem with a single, monolithic prompt is a common mistake. It’s like trying to build a house with one giant, multi-purpose tool. It might work for a simple shed, but for anything more complex, you need a toolbox of specialized instruments. The same principle applies to building with LLMs. A single, overloaded prompt quickly becomes brittle, expensive, and nearly impossible to debug.

This lesson will introduce you to four essential patterns that form the building blocks of almost every production-grade LLM application:
- **Prompt Chaining**: Decomposing a task into a sequence of smaller, manageable steps.
- **Parallelization**: Executing independent tasks concurrently to improve speed.
- **Routing**: Using conditional logic to direct a workflow down different paths.
- **Orchestrator-Worker**: Dynamically breaking down complex tasks and delegating them to specialized workers.

By mastering these patterns, you will learn how to move beyond simple prompts and start architecting robust, modular, and efficient AI systems.

## The Challenge with Complex Single LLM Calls

When you ask an LLM to perform multiple tasks in a single call—like generating questions, answering them, and citing sources all at once—you are creating a monolithic system. This approach often leads to inconsistent and unreliable results. The more instructions you cram into one prompt, the higher the chance the model will get confused, miss a step, or produce a low-quality output. An empirical study comparing single-task and multitask prompts found that performance is highly dependent on the model, with no universal rule favoring one approach over the other [[1]].

Several core problems emerge from this single-prompt approach. First, debugging becomes a nightmare. If the output is wrong, it is difficult to pinpoint which part of the complex instruction the model failed to follow. Was it the question generation, the answering, or the source citation? A single prompt gives you a single point of failure with no visibility into the intermediate steps.

Second, this approach lacks modularity, making the system difficult to maintain and improve. You cannot optimize one part of the task without potentially breaking another. For example, tweaking the prompt to get better answers might degrade the quality of the generated questions. This tight coupling makes iterative development slow and risky.

A third issue is sensitivity to minor changes. LLMs can be surprisingly brittle; even subtle variations in prompt formatting, such as reordering examples or changing the wording, can cause performance to fluctuate wildly. One study found that minimal prompt adjustments could lead to accuracy discrepancies as high as 76 percentage points in few-shot learning contexts [[3]]. This makes reproducibility a major challenge, as the same prompt might yield different results if the input phrasing changes slightly.

Furthermore, monolithic prompts often lead to overstuffed context windows. While modern LLMs boast large context windows, they are not infinite. Every tool call, function parameter, and response payload consumes tokens. In a long, complex prompt, you risk hitting the context limit, which can cause the model to truncate critical information from early steps [[22]].

Even if you stay within the limit, a well-documented issue with long contexts is the "lost-in-the-middle" problem. Research from Stanford and UC Berkeley has shown that LLMs pay the most attention to information at the beginning and end of their context window, often ignoring crucial details buried in the middle [[2]]. This U-shaped accuracy curve means that even if you provide all the necessary information, the model might simply overlook it if it is not positioned correctly. This bias is a structural result of how transformer architectures work, stemming from causal attention masking and positional encoding decay [[2]].

Finally, monolithic prompts can be inefficient. They often require more tokens than a series of focused prompts because you have to repeat instructions and context. This not only increases costs but also latency, as the model takes longer to process the large input.

Let's see this in action. We will use the Google Gemini API to generate a Frequently Asked Questions (FAQ) section based on content from several mock webpages about renewable energy.

1.  First, we set up our environment by initializing the Gemini client and defining our model. We will use `gemini-2.5-flash`, which is fast and cost-effective for these examples.
    ```python
    import asyncio
    from enum import Enum
    import random
    import time
    
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
    
    from lessons.utils import env, pretty_print
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-2.5-flash"
    ```
2.  Next, we define our mock data sources.
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
3.  Now, we will create a single, complex prompt that asks the model to do everything at once. We will use Pydantic to define the structured output we expect.
    ```python
    # Pydantic classes for structured outputs
    class FAQ(BaseModel):
        """A FAQ is a question and answer pair, with a list of sources used to answer the question."""
        question: str = Field(description="The question to be answered")
        answer: str = Field(description="The answer to the question")
        sources: list[str] = Field(description="The sources used to answer the question")
    
    class FAQList(BaseModel):
        """A list of FAQs"""
        faqs: list[FAQ] = Field(description="A list of FAQs")
    
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
    {
      "question": "What is solar energy and how does it work?",
      "answer": "Solar energy is a renewable powerhouse that converts sunlight into electricity through photovoltaic (PV) panels.",
      "sources": [
        "The Benefits of Solar Energy"
      ]
    }
    ...
    {
      "question": "Why is energy storage crucial for renewable energy sources like solar and wind?",
      "answer": "Effective energy storage is key to unlocking the full potential of renewable sources because it allows storing excess energy when plentiful and releasing it when needed, which is crucial for a stable power grid.",
      "sources": [
        "Energy Storage Solutions",
        "Understanding Wind Turbines"
      ]
    }
    ...
    ```
While this output looks reasonable, it often hides subtle failures. For example, an answer might be synthesized from multiple sources, but the model may only cite one. Or it might fail to generate the exact number of questions requested. These inconsistencies make the system unreliable in production.

## The Power of Modularity: Why Chain LLM Calls?

The solution to the unreliability of monolithic prompts is modularity. Prompt chaining is a fundamental workflow pattern that breaks a complex task into a sequence of smaller, simpler steps [[41]]. Each step is a focused LLM call, and the output of one step becomes the input for the next. This "divide and conquer" approach mirrors how humans solve complex problems and is a cornerstone of reliable AI engineering [[56]].

The benefits of this modular approach are significant.

**Improved Modularity and Maintainability:** Each LLM call in a chain is a self-contained component focused on a single task. This makes the system easier to test, version, and reuse. If you want to improve how answers are generated, you can modify just that step without affecting question generation or source finding [[36]].

**Enhanced Accuracy:** Simpler, targeted prompts reduce the cognitive load on the LLM. Instead of trying to juggle multiple instructions, the model can focus its full attention on one well-defined task. This almost always leads to higher-quality, more accurate outputs [[56]].

**Easier Debugging:** When a workflow fails, a chained architecture allows you to isolate the exact point of failure. You can inspect the input and output of each step to see where things went wrong. This level of observability is impossible with a single, black-box prompt. Companies like AppFolio and Acxiom use frameworks like LangGraph and observability tools like LangSmith precisely for this reason—to gain visibility into multi-step agent interactions and debug them effectively [[20]].

**Increased Flexibility and Optimization:** A modular chain gives you the flexibility to optimize each component independently. You can use different models for different steps, a powerful cost-saving strategy. For instance, you could use a fast, inexpensive model like Gemini Flash for a simple classification task and a more powerful model like Gemini Pro for complex content generation [[36]].

However, prompt chaining is not without its trade-offs. One major downside is increased latency, as each sequential call adds to the total processing time. It can also be more expensive if the combined token count of multiple calls exceeds that of a single, well-engineered prompt.

Another critical challenge is information loss, or "context decay," between steps. As information is passed from one call to the next, important details can be diluted or dropped entirely. A summary from step one might lose a nuance that was critical for step two. Mitigating this requires careful prompt design for intermediate steps and using structured state objects to pass data, ensuring that critical information is preserved throughout the chain [[22]].

Furthermore, some instructions may only make sense when processed together. Splitting them can cause the model to lose the broader context, leading to a final output that is technically correct at each step but holistically wrong. Lastly, managing the "glue code" that connects multiple prompts adds engineering overhead. While libraries like LangChain or LangGraph can help, you are still responsible for orchestrating the flow, handling state, and managing errors between calls.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's apply the prompt chaining pattern to our FAQ generation task. We will break the monolithic prompt into a three-step sequential workflow:
1.  **Generate Questions**: Create a list of questions based on the source content.
2.  **Answer Questions**: For each question, generate a concise answer.
3.  **Find Sources**: For each question-answer pair, identify the source documents used.

Image 1: A flowchart illustrating the sequential FAQ generation pipeline.

This structure provides clear, auditable steps and improves the reliability of the final output. By separating concerns, we can craft a specialized prompt for each sub-task, leading to better performance and easier debugging. This approach is common in production systems for tasks like document question-answering, where the first step extracts relevant quotes and the second step synthesizes them into an answer [[41]], [[42]].

1.  First, we define a function to generate a list of questions. This prompt is focused on a single task: creating relevant questions. We use a Pydantic model, `QuestionList`, to ensure the output is a well-formed list of strings.
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
    It outputs a list of questions:
    ```text
    What are the primary environmental and economic benefits of solar energy?
    ...
    Can excess solar power generated by homeowners be sold back to the grid?
    ```
2.  Next, a function to answer a given question. This prompt is instructed to use *only* the provided content, which helps ground the model and reduce hallucinations. Since this is a simple text generation task, we do not need a structured output here.
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
    ```
3.  Finally, a function to identify the sources for a given answer. This step adds a layer of verification, forcing the model to trace its answer back to the original documents. We again use a Pydantic model, `SourceList`, to enforce a structured output.
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
    ```
4.  Now, we combine these functions into a single sequential workflow. We will iterate through each generated question, answer it, and then find its sources. This loop represents the "chain" in prompt chaining.
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
    
    {
      "question": "What are the primary financial benefits of installing solar panels for homeowners, and are there any initial costs to consider?",
      "answer": "The primary financial benefits of installing solar panels for homeowners are significantly lowered monthly electricity bills and, in some cases, the ability to sell excess power back to the grid. The initial installation cost can be high.",
      "sources": [
        "The Benefits of Solar Energy"
      ]
    }
    ...
    ```
By breaking the task into a chain, we have created a more robust and debuggable system. Each step has a clear purpose, and the final output is built from a series of validated intermediate results. However, processing four questions took over 20 seconds. This latency might be unacceptable for many real-time applications.

## Optimizing Sequential Workflows With Parallel Processing

The sequential workflow improves reliability, but its latency can be a bottleneck. Since the tasks of answering each question and finding its sources are independent of one another, we can execute them in parallel. This can reduce the total processing time, especially when dealing with a large number of items [[45]].

We will use Python’s `asyncio` library to run our LLM calls concurrently. This is a perfect use case for `asyncio` because API calls are I/O-bound tasks; the program spends most of its time waiting for a response from the network. `asyncio` allows the program to perform other work during these waiting periods, effectively overlapping the I/O operations [[27]], [[28]].

1.  First, we need to create asynchronous versions of our `answer_question` and `find_sources` functions. The `google-genai` library provides an async client (`client.aio.models.generate_content`) for this purpose.
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
2.  Next, we create the main parallel workflow. It first generates the questions synchronously (as this is a single API call) and then creates a list of asynchronous tasks to be run concurrently using `asyncio.gather`.
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
    
    {
      "question": "What are the primary environmental and economic benefits of using solar energy?",
      "answer": "The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels.\n\nThe primary economic benefits include significantly lower monthly electricity bills, the ability to sell excess power back to the grid, long-term savings, and contributing to energy independence for nations.",
      "sources": [
        "The Benefits of Solar Energy"
      ]
    }
    ...
    ```
By running the tasks in parallel, we reduced the processing time from 22.20 seconds to just 8.98 seconds—a more than 2x speedup.

However, a word of caution: when running many parallel requests, you are likely to hit API rate limits. Production systems must implement strategies like exponential backoff with jitter to handle `429 Too Many Requests` errors gracefully. This technique involves waiting for a progressively longer, randomized amount of time before retrying a failed request, which prevents a "thundering herd" of clients from overwhelming the API simultaneously [[9]]. More advanced strategies include client-side queuing with a token bucket algorithm to smooth out bursty traffic, implementing backpressure to slow down requests when the system is overloaded, and dynamically adjusting the level of concurrency based on the API's responses. Cloud providers like Google Gemini have aggressive rate limiting, so robust error handling is not optional [[7]], [[8]].

## Introducing Dynamic Behavior: Routing and Conditional Logic

Sequential and parallel workflows are powerful, but they follow a fixed path. Many real-world applications require dynamic behavior, where the workflow adapts based on the input. This is where routing comes in. Routing uses conditional logic to direct an input to a specialized handler or sub-workflow. It is another application of the "divide and conquer" principle, ensuring that each part of your system handles only the specific tasks it was designed for [[36]].

An LLM itself can serve as the classification engine for the router. By providing the model with a set of categories and the user's input, you can prompt it to choose the most appropriate path. This is the core mechanism behind the Coordinator/Dispatcher pattern, where a "concierge" agent analyzes a user's intent and routes them to a specialist [[49]].

However, this classification step is a potential point of failure. Ambiguous user intent can lead to misclassification, sending the request down the wrong path. To build a robust router, you need to engineer the classification prompt carefully. This includes providing clear definitions for each category, using few-shot examples to demonstrate correct classification for tricky edge cases, and even including negative examples to show what *not* to do.

Using a router is preferable to creating a single, massive prompt that tries to handle every possible input type. Optimizing a prompt for one scenario (e.g., technical support) often degrades its performance on another (e.g., billing inquiries). Routing keeps prompts specialized, modular, and easier to maintain.

## Building a Basic Routing Workflow

Let's build a simple routing system for a customer service chatbot. The goal is to classify an incoming user query and route it to the appropriate specialized handler. This is a common pattern seen in production systems for customer support, where different agents handle distinct types of inquiries like billing or technical issues [[15]].

Image 2: A flowchart illustrating a basic routing workflow for customer service.

1.  First, we define the possible user intents using a Pydantic model with a Python `Enum`. This creates a clear, enforceable taxonomy for our classification step. A well-designed taxonomy is crucial for accurate routing. It should be comprehensive enough to cover all expected inputs, with clear and non-overlapping definitions for each intent. For complex systems, you might even employ a two-stage architecture, where a first-pass model retrieves a set of candidate intents, and a second, more powerful LLM makes the final selection, improving precision [[11]].
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
2.  Next, we define a specialized prompt for each intent. Each prompt is tailored to provide a helpful initial response for that specific category. This separation of concerns is key to the routing pattern's effectiveness.
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
3.  Finally, we create the `handle_query` function, which acts as our router. It takes the user's query and the classified intent, then calls the appropriate LLM with the specialized prompt. A crucial part of a production-grade router is a default or fallback route to handle cases where the intent is unclear or doesn't fit any category, preventing the system from failing silently.
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
4.  Let's test it with a few different queries.
    ```python
    query_1 = "My internet connection is not working."
    query_2 = "I think there is a mistake on my last invoice."
    
    intent_1 = classify_intent(query_1)
    intent_2 = classify_intent(query_2)
    
    response_1 = handle_query(query_1, intent_1)
    response_2 = handle_query(query_2, intent_2)
    ```
    For the technical query, it outputs:
    ```text
    Hello there! I'm sorry to hear you're having trouble with your internet connection. That can definitely be frustrating.
    
    To help me understand what's going on and assist you best, could you please provide a few more details?
    ...
    ```
    For the billing query, it outputs:
    ```text
    I'm sorry to hear you think there might be a mistake on your last invoice. I can definitely help you look into that!
    
    To access your account and investigate the charges, could you please provide your account number?
    ```
This routing workflow ensures that each query is handled by a prompt specifically designed for it, leading to more accurate and helpful responses.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The orchestrator-worker pattern takes dynamic behavior a step further. Instead of routing a task down a single, predefined path, a central "orchestrator" LLM dynamically breaks a complex query into multiple subtasks. It then delegates these subtasks to specialized "worker" LLMs, which can run in parallel. Finally, a "synthesizer" LLM gathers the results from the workers and combines them into a single, cohesive response [[17]], [[32]].

This pattern is exceptionally well-suited for complex, unpredictable tasks where the necessary steps cannot be known in advance [[16]], [[19]]. For example, analyzing a customer request might involve checking an invoice, processing a product return, and looking up an order status—all at once. The key difference from simple parallelization is this flexibility: the orchestrator determines the subtasks at runtime based on the specific input.

Image 3: A flowchart depicting the orchestrator-worker pattern for dynamic task decomposition.

While powerful, this pattern introduces its own engineering challenges. The orchestrator can become a performance bottleneck if it is too slow, and its ability to correctly and completely decompose the task is critical. An incomplete decomposition means necessary steps will be missed. To mitigate this, prompts for the orchestrator should be engineered to encourage thoroughness and perhaps even include an iterative refinement step where it reviews its own plan.

The workers must operate with clear boundaries and consistent schemas. Using structured inputs and outputs (like the Pydantic models we have been using) is essential for reliable communication between the orchestrator and workers. If workers produce conflicting or inconsistent outputs, the synthesizer may struggle to create a coherent final response. Strategies to handle this include having the synthesizer flag conflicts for human review, re-querying the conflicting workers with additional context, or even using a voting mechanism among multiple workers performing the same task. Finally, the synthesizer itself needs careful prompting to handle diverse, structured inputs and weave them into a natural, user-friendly message, gracefully managing any missing or failed worker outputs.

Let's implement this pattern to handle a multi-part customer query.

1.  First, we define the orchestrator. Its job is to analyze the user's query and break it down into a structured list of tasks using Pydantic models.
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
2.  Next, we define our worker functions. Each worker is a specialist. For this example, they simulate backend API calls (e.g., fetching an order status, creating a return authorization) and return structured data. The billing worker even uses another LLM call to extract the specific user concern about an invoice.
    ```python
    # Billing Worker
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
        # ... uses an LLM to extract the specific concern ...
        # ... simulates opening an investigation ...
        # ... returns a structured BillingTask object ...
    
    # Product Return Worker
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
        # ... simulates generating an RMA number ...
        # ... returns a structured ReturnTask object ...
    
    # Order Status Worker
    def handle_status_worker(order_id: str) -> StatusTask:
        # ... simulates fetching order status from a backend ...
        # ... returns a structured StatusTask object ...
    ```
3.  The synthesizer's role is to take the structured outputs from all workers and compose a single, user-friendly response.
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
        # ... formats the results into bullet points ...
        prompt = prompt_synthesizer.format(formatted_results=formatted_results)
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    ```
4.  Finally, we tie everything together in a main processing function.
    ```python
    def process_user_query(user_query):
        """Processes a query using the Orchestrator-Worker-Synthesizer pattern."""
        
        # 1. Run orchestrator
        tasks_list = orchestrator(user_query)
        # ...
    
        # 2. Run workers
        worker_results = []
        # ... dispatch to correct worker based on task.query_type ...
        
        # 3. Run synthesizer
        if worker_results:
            final_user_message = synthesizer(worker_results)
            # ...
    ```
5.  Let's test the full pipeline with a complex query.
    ```python
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
      "product_name": null,
      "reason_for_return": null,
      "order_id": null
    }
    
    Deconstructed task 2:
    {
      "query_type": "ProductReturn",
      "invoice_number": null,
      "product_name": "SuperWidget 5000",
      "reason_for_return": "it's not compatible with my system",
      "order_id": null
    }
    
    Deconstructed task 3:
    {
      "query_type": "StatusUpdate",
      "invoice_number": null,
      "product_name": null,
      "reason_for_return": null,
      "order_id": "A-12345"
    }
    ```
    Then, the workers execute and return their structured results. Finally, the synthesizer combines them into one email:
    ```text
    Final synthesized response:
    Dear Customer,
    
    Thank you for reaching out. Here's an update on your recent inquiries:
    
    Regarding your BillingInquiry:
      - Invoice Number: INV-7890
      - Your Stated Concern: "It seems higher than I expected."
      - Our Action: An investigation (Case ID: INV_CASE_5076) has been opened regarding your concern.
      - Expected Resolution: We will get back to you within 2 business days.
    
    Regarding your ProductReturn:
      - Product: SuperWidget 5000
      - Reason for Return: "it's not compatible with my system"
      - Return Authorization (RMA): RMA-60073
      - Instructions: Please pack the 'SuperWidget 5000' securely...
    
    Regarding your StatusUpdate:
      - Order ID: A-12345
      - Current Status: Shipped
      - Carrier: SuperFast Shipping
      - Tracking Number: SF530737
      - Delivery Estimate: Tomorrow
    
    We appreciate your patience and will follow up on the billing inquiry as soon as our investigation is complete.
    
    Best regards,
    
    The Support Team
    ```
This pattern provides a powerful way to build flexible and scalable systems that can handle a wide range of complex, multi-part tasks dynamically.

## Conclusion

In this lesson, we have moved from the limitations of single, complex prompts to the power of modular, multi-step workflows. We have explored four fundamental patterns—chaining, parallelization, routing, and orchestrator-worker—that are the essential ingredients for building reliable and scalable LLM applications. By breaking down complex tasks, you gain control, improve accuracy, and make your systems easier to debug and maintain.

These patterns are not just theoretical concepts; they are the practical building blocks used in production systems every day. They form the foundation upon which more advanced agentic behaviors are built. In our upcoming lessons, we will continue to build on this foundation. We will see how these workflows can be enhanced with tools (Lesson 6), enabling them to interact with the outside world. We will then dive into planning and reasoning (Lesson 7) and memory (Lesson 9), which are the keys to unlocking more autonomous, agent-like capabilities.

## References

- [1] [Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts](https://www.mdpi.com/2079-9292/13/23/4712)
- [2] [The "Lost in the Middle" Problem — Why LLMs Ignore the Middle of Your Context Window](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [3] [Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://aclanthology.org/2025.ommm-1.4.pdf)
- [7] [Challenges with rate limiting and handling API responses in high-volume requests](https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903)
- [8] [429 on Vertex AI API: How to send 5-20 parallel Gemini API requests without hitting rate limits](https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt)
- [9] [LLM API Resilience in Production: Rate Limits, Failover, and the Hidden Costs of Naive Retry Logic](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production)
- [11] [LLM-Based Prompt Routing](https://www.emergentmind.com/topics/llm-based-prompt-routing)
- [15] [Multi-LLM routing strategies for generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)
- [16] [Orchestrator-Worker](https://agents.kour.me/orchestrator-worker/)
- [17] [DIY #17: Orchestrator-Worker LLM Agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [19] [Cookbook: Orchestrator-Workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [20] [LLMOps in Production: 457 Case Studies of What Actually Works](https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works)
- [22] [How Tool Chaining Fails in Production LLM Agents and How to Fix It](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production)
- [27] [Python Concurrency Showdown: Asyncio vs. Threading vs. Multiprocessing—Which Should You Choose in 2025?](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a)
- [28] [parallelism-concurrency-and-asyncio-in-python-by-example](https://testdriven.io/blog/python-concurrency-parallelism/)
- [32] [DIY #17: Orchestrator-Worker LLM Agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [36] [Stop Building AI Agents. Use These 5 Workflow Patterns Instead.](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [41] [A Practical Guide to Prompt Engineering Techniques and Their Use Cases](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a)
- [42] [10 Prompt Engineering Techniques (Super Simple Explanation)](https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation)
- [45] [Orchestrating Multi-Step LLM Chains: Best Practices](https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/)
- [49] [Developer’s guide to multi-agent patterns in ADK](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [56] [Stop Building AI Agents. Use These 5 Workflow Patterns Instead.](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [Notebook code for the lesson](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/05_workflow_patterns/notebook.ipynb)
- [Prompt Chaining Guide](https://www.promptingguide.ai/techniques/prompt_chaining)
- [Building Effective Agents - Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [Claude 4 Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [LangGraph Workflows](https://langchain-ai.github.io/langgraphjs/tutorials/workflows)
- [Basic Multi-LLM Workflows](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb)
- [Chain Prompts - Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts)