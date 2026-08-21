# Stop Writing Complex Prompts: A Guide to AI Workflow Patterns

In our previous lessons, we built a foundation in AI Engineering. We explored the agent landscape, distinguished between rule-based workflows and autonomous agents, and covered context engineering. Now, we will tackle a fundamental challenge: getting structured, reliable information *out* of an LLM and building robust systems on top.

When you start building AI applications, the first instinct is often to write a single, complex prompt that does everything. We've been there. We once built a system with a massive prompt that was supposed to generate questions, find answers, and cite sources all in one go. It seemed to work in demos, but in production, it was a different story. The outputs were inconsistent, debugging was a nightmare, and every small change felt like performing open-heart surgery on a monolithic beast.

This is a common pitfall. A single, all-in-one prompt creates a "Jack of all trades, master of none" agent that struggles with reliability. This lesson will show you a better way. We will break down complex tasks into manageable, modular workflows using patterns like chaining, parallelization, routing, and orchestration. You will learn to build systems that are not just more reliable and easier to debug but also faster and more flexible.

In this lesson, we will cover:
- The problems with complex, single LLM calls.
- Why modularity through prompt chaining is a more robust approach.
- How to build a sequential FAQ generation pipeline.
- How to speed up workflows with parallel processing.
- How to introduce dynamic logic with routing.
- How to use the orchestrator-worker pattern for dynamic task decomposition.

## The Challenge with Complex Single LLM Calls

Relying on a single, large prompt for a multi-step task is a recipe for unreliability. While it might seem efficient to ask an LLM to do everything at once, this approach introduces several engineering challenges that make production systems brittle.

First, a monolithic prompt makes it difficult to pinpoint errors. If the final output is wrong, was it because the model misunderstood the first instruction, failed on the third, or misinterpreted the source material? Without clear intermediate steps, debugging becomes a guessing game. Second, this approach lacks modularity. You cannot update or optimize one part of the task without rewriting the entire prompt, which risks breaking other parts.

Furthermore, long and complex prompts are more susceptible to the "lost-in-the-middle" problem, where the model pays less attention to information buried in the middle of a large context [[2]]. This can lead to the model ignoring critical instructions or source data. Finally, trying to cram too many instructions into a single call often leads to higher token consumption and less reliable outputs as the model struggles to follow every constraint perfectly [[5]].

Let's see this in practice. We will build an FAQ generator from a few mock webpages on renewable energy.

1.  First, we set up our environment by initializing the Gemini client. We will use `gemini-1.5-flash`, which is fast and cost-effective for these examples.
    ```python
    from lessons.utils import env
    import google.generai as genai
    from google.genai import types
    from pydantic import BaseModel, Field
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-1.5-flash"
    ```

2.  Next, we define our mock source content.
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
    
    combined_content = "\n\n".join(
        [f"Source Title: {source['title']}\nContent: {source['content']}" for source in all_sources]
    )
    ```

3.  Now, we write a single, complex prompt that asks the model to generate questions, find answers, and cite sources all at once. We use Pydantic models for structured output, a concept we covered in Lesson 4.
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
    ```

While this output looks acceptable, the approach is fragile. As instructions become more complex, a single prompt is more likely to fail. For instance, the model might correctly answer a question using information from two sources but only cite one. This kind of subtle error is common with monolithic prompts and hard to fix without making the prompt even more convoluted. A better approach is to break the problem down.

## The Power of Modularity: Why Chain LLM Calls?

Instead of a single, complex prompt, we can use prompt chaining. This technique breaks a large task into a sequence of smaller, more focused sub-tasks. The output of one LLM call becomes the input for the next, creating a workflow or "chain" [[41], [42]]. This is a divide-and-conquer strategy that brings the principles of modular software design to AI engineering.

This modular approach offers several advantages for building reliable systems [[36], [56], [58]]. First, it improves accuracy. Simpler, targeted prompts are less confusing for the LLM, leading to more consistent and correct outputs for each sub-task. Second, it makes debugging far easier. If a workflow fails, you can inspect the output of each step to pinpoint exactly where the error occurred. Third, it increases flexibility. You can swap, update, or optimize individual components of the chain without affecting the others. For example, you could use a fast, cheap model for a simple classification step and a more powerful model for a complex generation step.

However, prompt chaining is not without its trade-offs. It can increase latency and cost because it requires multiple LLM calls instead of one. There is also a risk of information loss or error propagation; a mistake in an early step can cascade through the rest of the chain [[22], [41], [47]]. For example, if a summarization step loses a key detail, a subsequent translation step will not be able to recover it. Despite these challenges, for most complex tasks, the gains in reliability and maintainability far outweigh the downsides.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's refactor our FAQ generation task into a three-step sequential workflow:
1.  **Generate Questions:** The first LLM call will read the source content and generate a list of relevant questions.
2.  **Answer Questions:** For each question, a second LLM call will generate a concise answer based on the content.
3.  **Find Sources:** For each question-and-answer pair, a third LLM call will identify the source titles used.

Image 1: A sequential workflow for FAQ generation.

1.  First, we create a function dedicated to generating questions. This prompt has a single, clear responsibility.
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
    
    questions = generate_questions(combined_content, n_questions=10)
    ```
    It outputs:
    ```text
    ['What are the primary environmental and economic benefits of solar energy?', 'How do homeowners financially benefit from installing solar panels?', 'What is the main process by which wind turbines generate electricity?', 'What is the primary challenge of wind energy, and how is it addressed?', 'Why is effective energy storage crucial for renewable energy sources like solar and wind?', 'What are some common large-scale energy storage methods mentioned?', 'Are there government incentives available for solar panel installation?', 'What is the difference in power consistency between onshore and offshore wind farms?', 'How do energy storage solutions make the energy system more resilient and reliable?', 'Can excess solar power generated by homeowners be sold back to the grid?']
    ```

2.  Next, we define a function to answer a single question. This function takes a question and the source content as input.
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
    
    test_question = questions[0]
    test_answer = answer_question(test_question, combined_content)
    ```
    It outputs:
    ```text
    The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels. Economically, it allows homeowners to significantly lower their monthly electricity bills and potentially sell excess power back to the grid.
    ```

3.  Finally, we create a function to find the sources for a given answer. This step enhances traceability and helps ensure the answers are grounded in the provided content.
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
    
    test_sources = find_sources(test_question, test_answer, combined_content)
    ```
    It outputs:
    ```text
    ['The Benefits of Solar Energy']
    ```

4.  Now, we combine these functions into a complete sequential workflow. We will loop through each generated question, answer it, and find its sources one by one.
    ```python
    import time
    
    def sequential_workflow(content, n_questions=10) -> list[FAQ]:
        """
        Execute the complete sequential workflow for FAQ generation.
        """
        questions = generate_questions(content, n_questions)
    
        final_faqs = []
        for question in questions:
            answer = answer_question(question, content)
            sources = find_sources(question, answer, content)
    
            faq = FAQ(
                question=question,
                answer=answer,
                sources=sources
            )
            final_faqs.append(faq)
    
        return final_faqs
    
    start_time = time.monotonic()
    sequential_faqs = sequential_workflow(combined_content, n_questions=4)
    end_time = time.monotonic()
    print(f"Sequential processing completed in {end_time - start_time:.2f} seconds")
    ```
    It outputs:
    ```text
    Sequential processing completed in 13.91 seconds
    ```
    Here is one of the final FAQ objects:
    ```json
    {
      "question": "What are the main differences between onshore and offshore wind farms, and what is the biggest challenge associated with wind energy generation?",
      "answer": "Offshore wind farms generally produce more consistent power than onshore wind farms due to stronger, more reliable winds. The biggest challenge associated with wind energy generation is its intermittency, as it only generates power when the wind blows.",
      "sources": [
        "Understanding Wind Turbines"
      ]
    }
    ```

This modular approach is more robust and easier to debug than the single-prompt version. However, processing each question sequentially took nearly 14 seconds. We can do better.

## Optimizing Sequential Workflows With Parallel Processing

Many steps in a workflow are independent. In our FAQ example, answering each question does not depend on the answer to any other question. This means we can run these independent tasks in parallel to significantly reduce latency.

We will refactor our workflow to use Python’s `asyncio` library for concurrent execution. Instead of processing questions one by one, we will fire off the "answer" and "find sources" calls for all questions at the same time.

1.  First, we need asynchronous versions of our `answer_question` and `find_sources` functions. The `google-genai` library provides an `aio` (asynchronous I/O) client for this purpose.
    ```python
    import asyncio
    
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

2.  Next, we create a function that processes a single question by running its two sub-tasks concurrently.
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

3.  Finally, we assemble the full parallel workflow. The `generate_questions` step remains sequential, but we then use `asyncio.gather` to execute `process_question_parallel` for all questions concurrently.
    ```python
    async def parallel_workflow(content: str, n_questions: int = 10) -> list[FAQ]:
        """
        Execute the complete parallel workflow for FAQ generation.
        """
        questions = generate_questions(content, n_questions)
    
        tasks = [process_question_parallel(question, content) for question in questions]
        parallel_faqs = await asyncio.gather(*tasks)
    
        return parallel_faqs
    
    start_time = time.monotonic()
    parallel_faqs = await parallel_workflow(combined_content, n_questions=4)
    end_time = time.monotonic()
    print(f"Parallel processing completed in {end_time - start_time:.2f} seconds")
    ```
    It outputs:
    ```text
    Parallel processing completed in 5.37 seconds
    ```

By running the independent tasks in parallel, we reduced the execution time from 13.91 seconds to just 5.37 seconds—a significant improvement.

Here is a quick comparison:

| Approach | Pros | Cons |
| --- | --- | --- |
| **Sequential** | Predictable, easier to debug. | Higher total processing time. |
| **Parallel** | Much faster, better resource use. | More complex error handling, risk of hitting rate limits. |

⚠️ A quick note on rate limits: when making many parallel API calls, you can easily exceed the limits imposed by your LLM provider (e.g., requests per minute). Production systems need robust error handling, such as exponential backoff with jitter, to manage these limits gracefully [[9]].

## Introducing Dynamic Behavior: Routing and Conditional Logic

So far, our workflows have been fixed. A sequential chain always executes the same steps, and a parallel workflow runs the same tasks concurrently. But what if your application needs to handle different types of input in different ways? This is where routing comes in.

Routing introduces conditional logic to your workflow. Instead of a single, linear path, you can create branches that direct the flow based on the input or an intermediate state. This allows you to use specialized prompts and tools for specific scenarios, following the same "divide-and-conquer" principle. A common pattern is to use an initial LLM call as a classifier to decide which branch to take.

For example, a customer support system could classify an incoming query as "Technical Support," "Billing Inquiry," or "General Question" and route it to a specialized handler for each case. This is far more effective than trying to create a single, monolithic prompt that can handle every possible type of customer query.

## Building a Basic Routing Workflow

Let's build a simple routing system for a customer service bot. The workflow will first classify the user's intent and then pass the query to a specialized handler.

Image 2: A routing workflow for customer service intent classification.

1.  First, we define the possible intents and use an LLM to classify the user's query. We use an `Enum` and Pydantic models to ensure the classification is one of our expected values.
    ```python
    from enum import Enum
    
    class IntentEnum(str, Enum):
        """Defines the allowed values for the 'intent' field."""
        TECHNICAL_SUPPORT = "Technical Support"
        BILLING_INQUIRY = "Billing Inquiry"
        GENERAL_QUESTION = "General Question"
    
    class UserIntent(BaseModel):
        """Defines the expected response schema for the intent classification."""
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
    intent_1 = classify_intent(query_1)
    ```
    It outputs:
    ```text
    IntentEnum.TECHNICAL_SUPPORT
    ```

2.  Next, we define specialized prompts for each intent. Each prompt is tailored to handle a specific type of query.
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

3.  Finally, we create a `handle_query` function that acts as our router. It takes the user's query and the classified intent, then calls the appropriate handler.
    ```python
    def handle_query(user_query: str, intent: str) -> str:
        """Routes a query to the correct handler based on its classified intent."""
        if intent == IntentEnum.TECHNICAL_SUPPORT:
            prompt = prompt_technical_support.format(user_query=user_query)
        elif intent == IntentEnum.BILLING_INQUIRY:
            prompt = prompt_billing_inquiry.format(user_query=user_query)
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
    Hello! I'm sorry to hear you're having trouble with your internet connection. To help me troubleshoot, could you please tell me a bit more about the issue? For example, have you already tried restarting your router or modem?
    ```
This routing pattern allows us to build a more sophisticated and reliable system by directing tasks to specialized components, keeping each part of our application simple and focused.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The patterns we have seen so far—chaining, parallelization, and routing—are powerful, but they rely on pre-defined workflows. What if you have a complex task where the necessary sub-tasks cannot be known in advance? This requires a more dynamic approach.

The orchestrator-worker pattern uses a central LLM, the "orchestrator," to analyze a complex query and dynamically break it down into smaller sub-tasks. It then delegates these sub-tasks to specialized "worker" components, which can be other LLM calls or external tools. Once the workers complete their tasks, a final "synthesizer" step combines their outputs into a single, coherent response [[16], [17], [32], [53]].

The key advantage here is flexibility. Unlike a fixed parallel workflow, the orchestrator determines the sub-tasks at runtime based on the specific input. This is ideal for handling unpredictable, multi-part user queries, such as a customer request that involves a billing question, a product return, and an order status update all at once.

Let's implement this pattern for our customer support example.

Image 3: A flowchart illustrating the orchestrator-worker pattern, showing query decomposition, parallel worker execution, and final synthesis.

1.  First, we define the orchestrator. Its job is to parse a complex user query and break it down into a list of structured tasks. We will use Pydantic models to define the task schema.
    ```python
    class QueryTypeEnum(str, Enum):
        BILLING_INQUIRY = "BillingInquiry"
        PRODUCT_RETURN = "ProductReturn"
        STATUS_UPDATE = "StatusUpdate"
    
    class Task(BaseModel):
        query_type: QueryTypeEnum
        invoice_number: str | None = None
        product_name: str | None = None
        reason_for_return: str | None = None
        order_id: str | None = None
    
    class TaskList(BaseModel):
        tasks: list[Task]
    
    prompt_orchestrator = f"""
    You are a master orchestrator. Your job is to break down a complex user query into a list of sub-tasks.
    Each sub-task must have a "query_type" and its necessary parameters.
    
    The possible "query_type" values and their required parameters are:
    1. "{QueryTypeEnum.BILLING_INQUIRY.value}": Requires "invoice_number".
    2. "{QueryTypeEnum.PRODUCT_RETURN.value}": Requires "product_name" and "reason_for_return".
    3. "{QueryTypeEnum.STATUS_UPDATE.value}": Requires "order_id".
    
    Here's the user's query:
    <user_query>
    {{query}}
    </user_query>
    """.strip()
    
    def orchestrator(query: str) -> list[Task]:
        """Breaks down a complex query into a list of tasks."""
        # ... implementation using Gemini client ...
    ```

2.  Next, we define our specialized workers. Each worker is a function that handles one type of task (billing, returns, or status updates). In a real application, these workers might call external APIs or databases. Here, we will simulate that behavior.
    ```python
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
        # ... implementation using LLM to extract concern and simulate investigation ...
    
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
        # ... implementation to simulate RMA generation ...
    
    def handle_status_worker(order_id: str) -> StatusTask:
        # ... implementation to simulate fetching order status ...
    ```

3.  After the workers run, we need a synthesizer to combine their structured outputs into a single, human-readable response.
    ```python
    prompt_synthesizer = """
    You are a master communicator. Combine several distinct pieces of information from our support team into a single, well-formatted, and friendly email to a customer.
    
    Here are the points to include, based on the actions taken for their query:
    <points>
    {formatted_results}
    </points>
    
    Combine these points into one cohesive response.
    """.strip()
    
    def synthesizer(results: list) -> str:
        # ... implementation to format worker results and call LLM ...
    ```

4.  Finally, we tie everything together in a main processing function. This function calls the orchestrator, dispatches tasks to the appropriate workers (which could run in parallel), and then passes the results to the synthesizer.
    ```python
    def process_user_query(user_query):
        """Processes a query using the Orchestrator-Worker-Synthesizer pattern."""
        # 1. Run orchestrator
        tasks_list = orchestrator(user_query)
    
        # 2. Run workers
        worker_results = []
        for task in tasks_list:
            if task.query_type == QueryTypeEnum.BILLING_INQUIRY:
                worker_results.append(handle_billing_worker(task.invoice_number, user_query))
            # ... handle other task types
    
        # 3. Run synthesizer
        final_user_message = synthesizer(worker_results)
        print(final_user_message)
    ```

5.  Let's test it with a complex query.
    ```python
    complex_customer_query = """
    Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.
    Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.
    Finally, can you give me an update on my order #A-12345?
    """.strip()
    
    process_user_query(complex_customer_query)
    ```
    First, the orchestrator deconstructs the query into three distinct tasks:
    ```json
    [
      {
        "query_type": "BillingInquiry",
        "invoice_number": "INV-7890",
        "product_name": null,
        "reason_for_return": null,
        "order_id": null
      },
      {
        "query_type": "ProductReturn",
        "invoice_number": null,
        "product_name": "SuperWidget 5000",
        "reason_for_return": "not compatible with my system",
        "order_id": null
      },
      {
        "query_type": "StatusUpdate",
        "invoice_number": null,
        "product_name": null,
        "reason_for_return": null,
        "order_id": "A-12345"
      }
    ]
    ```
    Then, the workers process these tasks, and the synthesizer generates the final, consolidated response:
    ```text
    Hi there,
    
    Thank you for reaching out to us. Here's a summary of the actions we've taken regarding your query:
    
    Regarding your BillingInquiry:
      - Invoice Number: INV-7890
      - Your Stated Concern: "The invoice seems higher than I expected."
      - Our Action: An investigation (Case ID: INV_CASE_8338) has been opened regarding your concern.
      - Expected Resolution: We will get back to you within 2 business days.
    
    Regarding your ProductReturn:
      - Product: SuperWidget 5000
      - Reason for Return: "it's not compatible with my system"
      - Return Authorization (RMA): RMA-89196
      - Instructions: Please pack the 'SuperWidget 5000' securely in its original packaging if possible. Include all accessories and manuals. Write the RMA number (RMA-89196) clearly on the outside of the package. Ship to: Returns Department, 123 Automation Lane, Tech City, TC 98765.
    
    Regarding your StatusUpdate:
      - Order ID: A-12345
      - Current Status: Delivered
      - Carrier: Local Courier
      - Tracking Number: LC61298
      - Delivery Estimate: Delivered yesterday
    
    We hope this information is helpful. Please let us know if you have any other questions.
    
    Best regards,
    The Support Team
    ```
The orchestrator-worker pattern provides a scalable and flexible architecture for building sophisticated AI systems that can handle complex, unpredictable tasks by breaking them down into manageable, specialized components.

## Conclusion

We have journeyed from the pitfalls of single, complex prompts to the power of modular AI workflows. You have learned that breaking down tasks into smaller, focused steps is key to building reliable and maintainable systems. We started with simple prompt chaining, then accelerated our workflow with parallelization. We introduced dynamic behavior with routing and, finally, tackled unpredictable tasks with the orchestrator-worker pattern.

These patterns are not just theoretical concepts; they are the fundamental building blocks you will use to construct nearly any LLM-powered application. As we have seen, these workflow-based approaches can solve a vast majority of production problems more reliably and controllably than a single, monolithic agent [[36]]. In the upcoming lessons, we will build upon this foundation, exploring how to give these workflows the ability to use tools, reason about their actions, and manage memory. Mastering these patterns is your first major step from being a prompt engineer to becoming a true AI engineer.

## References

- [2] N. F. Liu, K. Lin, J. Hewitt, A. Cheung, A. Garg, A. R. Singh, & P. Liang. (2023). Lost in the Middle: How Language Models Use Long Contexts. *arXiv*. [https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2)
- [5] C. Yang, Y. Shi, Q. Ma, M. X. Liu, C. Kästner, & T. Wu. (2025). What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts. *arXiv*. [https://arxiv.org/html/2505.13360v1](https://arxiv.org/html/2505.13360v1)
- [9] LLM API Resilience in Production. (2026). *Tian Pan*. [https://tianpan.co/blog/2026-03-11-llm-api-resilience-production](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production)
- [12] How to build intent detection for your chatbot. (n.d.). *Vellum*. [https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot](https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot)
- [16] Orchestrator-Worker. (n.d.). *Agents.kour.me*. [https://agents.kour.me/orchestrator-worker/](https://agents.kour.me/orchestrator-worker/)
- [17] DIY #17: Orchestrator-Worker LLM Agent. (2024). *ML Pills*. [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [22] How Tool Chaining Fails in Production LLM Agents and How to Fix It. (2026). *FutureAGI*. [https://futureagi.substack.com/p/how-tool-chaining-fails-in-production](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production)
- [26] Concurrency Patterns in Python. (n.d.). *Santhalakshminarayana*. [https://santhalakshminarayana.github.io/blog/concurrency-patterns-python](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python)
- [27] Python Concurrency Showdown: Asyncio vs. Threading vs. Multiprocessing. (2024). *Medium*. [https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a)
- [32] DIY #17: Orchestrator-Worker LLM Agent. (2024). *ML Pills*. [https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent)
- [36] Stop Building AI Agents. Use These Workflow Patterns Instead. (2024). *Decoding AI*. [https://www.decodingai.com/p/stop-building-ai-agents-use-these](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [41] A Practical Guide to Prompt Engineering Techniques and Their Use Cases. (2024). *Medium*. [https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a)
- [42] 10 Prompt Engineering Techniques (Super Simple Explanation). (2024). *Scrum.org*. [https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation](https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation)
- [45] Orchestrating Multi-Step LLM Chains: Best Practices. (n.d.). *Deepchecks*. [https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/](https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/)
- [46] Issue 110: LLM Workflow Patterns. (2024). *ML Pills*. [https://mlpills.substack.com/p/issue-110-llm-workflow-patterns](https://mlpills.substack.com/p/issue-110-llm-workflow-patterns)
- [47] The Compounding Error Effect in Large Language Models: A Growing Challenge. (n.d.). *Wand.ai*. [https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge](https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge)
- [49] Developer’s guide to multi-agent patterns in ADK. (2025). *Google for Developers*. [https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [53] Orchestrator-Workers Workflow. (n.d.). *Anthropic*. [https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers)
- [56] Stop Building AI Agents. Use These Workflow Patterns Instead. (2024). *Decoding AI*. [https://www.decodingai.com/p/stop-building-ai-agents-use-these](https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [58] Design Pattern: Prompt Chaining - Building reliable LLM applications. (2024). *Data Learning Science*. [https://datalearningscience.com/p/design-pattern-prompt-chaining-building](https://datalearningscience.com/p/design-pattern-prompt-chaining-building)