In our previous lessons, we covered the agent landscape, the difference between workflows and agents, context engineering, and structured outputs. These are the foundational skills you need as an AI Engineer. Now, we will build on that foundation by exploring the basic patterns for constructing LLM workflows: chaining, parallelization, routing, and the orchestrator-worker pattern.

Mastering these patterns is the first step toward building sophisticated and reliable LLM applications. They provide modularity, improve accuracy, and allow for more controlled processing. These techniques are the building blocks for both the deterministic workflows and the more complex agentic systems we will build later in this course.

## The Challenge with Complex Single LLM Calls

A common mistake when starting with LLMs is to cram too many instructions into a single, complex prompt. The thinking is that a powerful model should be able to handle it all at once. While this might work for simple demos, it quickly breaks down in production.

Trying to make a single LLM call handle a multi-step task leads to several problems. Research shows that as the number of requirements in a prompt increases, model accuracy drops significantly [[3]](https://arxiv.org/html/2505.13360v1). This is partly due to prompt sensitivity, where even minor changes in wording or the order of examples can cause wildly different outputs, making the system unpredictable [[2]](https://www.mdpi.com/2079-9292/13/23/4712). Furthermore, long contexts create their own issues. Models often suffer from the "lost in the middle" problem, where they pay more attention to information at the beginning and end of the prompt, effectively ignoring crucial details buried in the middle. This U-shaped performance curve is not a quirk; it is a result of the model's architecture. Two main factors are at play: causal attention masking, which gives early tokens more cumulative attention, and positional encoding decay, which weakens the signal for tokens far from the start or end [[1]](https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2). Finally, a single complex call makes debugging a nightmare. If the output is wrong, it is nearly impossible to pinpoint which part of the instruction the model failed to follow.

Let's look at a practical example. We will start with our usual setup.

1.  First, we configure the Gemini API client and define the model we will use. We will use `gemini-2.5-flash`, which is fast and cost-effective.
    ```python
    from lessons.utils import env
    import asyncio
    from enum import Enum
    import random
    import time
    
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    MODEL_ID = "gemini-2.5-flash"
    ```
2.  Next, we will use three mock webpages about renewable energy as our source content.
    ```python
    webpage_1 = {
        "title": "The Benefits of Solar Energy",
        "content": "...",
    }
    
    webpage_2 = {
        "title": "Understanding Wind Turbines",
        "content": "...",
    }
    
    webpage_3 = {
        "title": "Energy Storage Solutions",
        "content": "...",
    }
    
    all_sources = [webpage_1, webpage_2, webpage_3]
    
    combined_content = "\n\n".join(
        [f"Source Title: {source['title']}\nContent: {source['content']}" for source in all_sources]
    )
    ```
3.  Now, we will try to generate a list of Frequently Asked Questions (FAQs), provide answers, and cite sources, all in a single, complex prompt.
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
    
    class FAQ(BaseModel):
        """A FAQ is a question and answer pair, with a list of sources used to answer the question."""
        question: str = Field(description="The question to be answered")
        answer: str = Field(description="The answer to the question")
        sources: list[str] = Field(description="The sources used to answer the question")
    
    class FAQList(BaseModel):
        """A list of FAQs"""
        faqs: list[FAQ] = Field(description="A list of FAQs")
    
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
    ```
While the output might look acceptable, this approach is brittle. The more complex the instructions, the higher the chance of inaccuracies. For example, the model might fail to cite all relevant sources or hallucinate an answer.

## The Power of Modularity: Why Chain LLM Calls?

A more robust solution is to break the complex task into smaller, manageable subtasks. This is the core idea behind prompt chaining: connecting multiple LLM calls sequentially, where the output of one step becomes the input for the next [[4]](https://www.decodingai.com/p/stop-building-ai-agents-use-these), [[5]](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a). It is a simple "divide-and-conquer" strategy, often compared to a manufacturing assembly line where each station performs one specialized task [[6]](https://datalearningscience.com/p/design-pattern-prompt-chaining-building).

This modular approach offers several benefits. The core insight is that it is often cheaper and more effective to have several specialized, smaller models work on subtasks than to rely on one giant model for everything [[7]](https://www.together.ai/blog/plan-divide-conquer). Each LLM call focuses on a specific, well-defined task, which generally leads to higher accuracy. It becomes much easier to debug because you can isolate issues to a specific step in the chain. This also gives you flexibility; you can swap, update, or optimize individual components independently [[4]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

However, chaining is not without downsides. It increases latency because you are making multiple sequential API calls. It can also be more expensive, as the total number of tokens processed across several simple prompts may be higher than in a single complex one [[2]](https://www.mdpi.com/2079-9292/13/23/4712). There is also the risk of context degradation, where critical information or nuance is lost as data is passed from one step to the next [[8]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production). We will explore techniques to manage these trade-offs throughout the course.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's refactor our FAQ generation example into a three-step sequential workflow. This approach gives us more control and produces more consistent results by breaking down the problem into logical, isolated steps. Instead of asking the model to do everything at once, we guide it through a process that mirrors how a human would tackle the task: first understand the topics, then formulate questions, and finally, answer them with proper citations [[5]](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a).

This modularity is key to building reliable systems. Each function in our chain has a single responsibility, making it easier to test, debug, and refine. If the generated questions are poor, we know to adjust the `generate_questions` prompt without touching the answering logic. If the answers are inaccurate, we can focus on the `answer_question` step. This traceability is lost in a single, monolithic prompt, where the entire process is a black box. By decomposing the task, we also create opportunities for optimization. For instance, we could use a smaller, faster model for the relatively simple task of generating questions, and a more powerful model for the nuanced work of answering them and finding sources. This separation of concerns allows for targeted improvements and cost management that are impossible with a single-call approach. This workflow provides clear intermediate results at each stage, which is crucial for validation and ensuring the final output is both accurate and well-grounded.

```mermaid
flowchart LR
    A["Input Content"] --> B["Generate Questions"]
    B --> C["Answer Questions"]
    C --> D["Find Sources"]
```
Image 1: A flowchart illustrating the sequential FAQ generation pipeline.

1.  First, we create a function that focuses only on generating a list of questions from the provided content. This isolates the task of identifying key topics and turning them into relevant questions.
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
        # ... function implementation
        return response_questions.parsed.questions
    ```
2.  Next, a function to answer a single question, using the same content as a knowledge source. This step is focused purely on information retrieval and synthesis.
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
        # ... function implementation
        return answer_response.text
    ```
3.  Finally, a function to identify which sources were used to generate a given answer. This adds a layer of verification and grounding to our workflow.
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
        # ... function implementation
        return sources_response.parsed.sources
    ```
4.  We combine these functions into a sequential workflow. By executing these steps in order, we build a more robust and predictable pipeline. The structured output from each step ensures that the next step receives exactly the input it expects, reducing the chance of errors.
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
            answer = answer_question(question, content)
            sources = find_sources(question, answer, content)
            faq = FAQ(question=question, answer=answer, sources=sources)
            final_faqs.append(faq)
    
        return final_faqs
    
    start_time = time.monotonic()
    sequential_faqs = sequential_workflow(combined_content, n_questions=4)
    end_time = time.monotonic()
    print(f"Sequential processing completed in {end_time - start_time:.2f} seconds")
    ```
    It outputs:
    ```text
    Sequential processing completed in 22.20 seconds
    ```

This chained approach took about 22 seconds. While it is more reliable, the latency is noticeable. This brings us to our next pattern.

## Optimizing Sequential Workflows With Parallel Processing

For subtasks that are independent of each other, we can run them in parallel to significantly reduce the total processing time [[9]](https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/). The intuition is simple, like cooking a large meal: instead of preparing each dish one after another, you work on the chicken, potatoes, and salad at the same time so everything is ready faster [[10]](https://mlpills.substack.com/p/diy-17-parallelisation-with-langchain). In our FAQ example, once we have the list of questions, answering each one and finding its sources are independent operations that can be processed concurrently.

This pattern is particularly effective for I/O-bound operations, such as making API calls to an LLM, where the program spends most of its time waiting for a response from a network. By executing these calls concurrently, we can overlap the waiting times, leading to a substantial decrease in overall latency. We can implement this using Python's `asyncio` library, which is designed for exactly this kind of asynchronous programming [[11]](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python), [[12]](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a).

1.  We will create asynchronous versions of our `answer_question` and `find_sources` functions. Then, we will create a function to process a single question by running these two steps concurrently.
    ```python
    async def answer_question_async(question: str, content: str) -> str:
        # ... async implementation
    
    async def find_sources_async(question: str, answer: str, content: str) -> list[str]:
        # ... async implementation
    
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
2.  Now, we can build our parallel workflow.
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
    
    start_time = time.monotonic()
    parallel_faqs = await parallel_workflow(combined_content, n_questions=4)
    end_time = time.monotonic()
    print(f"Parallel processing completed in {end_time - start_time:.2f} seconds")
    ```
    It outputs:
    ```text
    Parallel processing completed in 8.98 seconds
    ```
By running the tasks in parallel, we reduced the processing time from 22 seconds to just 9 seconds. While parallelization offers a significant speedup, it introduces concurrency challenges like race conditions or timeouts [[4]](https://www.decodingai.com/p/stop-building-ai-agents-use-these). You also have to be mindful of API rate limits. Making too many concurrent requests can lead to errors [[13]](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production). In production systems, you would need to implement strategies like exponential backoff or use a request queue to manage the load. The trade-off is clear: parallel processing offers a significant reduction in processing time at the cost of more complex error handling and resource management, while sequential processing is slower but easier to debug and more predictable.

## Introducing Dynamic Behavior: Routing and Conditional Logic

So far, our workflows have been linear. But real-world applications often require dynamic behavior. Routing, or conditional logic, allows a workflow to branch based on the input or an intermediate state [[4]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

This is another application of the "divide-and-conquer" principle. Instead of creating a single, monolithic prompt, we can use an LLM as a classifier to direct the input to a specialized handler. A common pattern is "cascading routing," where a request is first sent to a cheaper model and only escalated to a more powerful one if the initial response is insufficient [[14]](https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/). For reliability, it is also wise to implement fallback logic, so if one handler fails, the request can be rerouted [[15]](https://blog.logrocket.com/llm-routing-right-model-for-requests/).

## Building a Basic Routing Workflow

Let's build a simple routing system for a customer service chatbot. This is a classic use case where understanding the user's intent is the first step to providing a useful response. Different user queries require different expertise; a billing question might need access to a payment API, while a technical issue requires diagnostic tools. Routing allows us to direct each query to a specialized handler equipped with the right context and capabilities [[16]](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/).

The system will first classify the user's query into predefined categories—such as Technical Support, Billing Inquiry, or General Question—and then route it to a specialized prompt. This ensures the user receives a relevant response, rather than a generic one. For robustness, it is also a best practice to include a fallback or "Other" route to handle queries that do not fit neatly into any category, preventing the user from hitting a dead end [[17]](https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot).

```mermaid
graph TD
    A["User Input"] --> B{"Intent Classification"}
    B -->|"Technical"| C["Technical Support Handler"]
    B -->|"Billing"| D["Billing Inquiry Handler"]
    B -->|"General"| E["General Question Handler"]
    C --> F["Final Responses"]
    D --> F
    E --> F
```
Image 2: A flowchart illustrating a customer service routing workflow.

1.  First, we define the possible intents and create a function to classify a user's query. This step acts as the decision point in our workflow.
    ```python
    class IntentEnum(str, Enum):
        TECHNICAL_SUPPORT = "Technical Support"
        BILLING_INQUIRY = "Billing Inquiry"
        GENERAL_QUESTION = "General Question"
    
    class UserIntent(BaseModel):
        intent: IntentEnum
    
    def classify_intent(user_query: str) -> IntentEnum:
        """Uses an LLM to classify a user query."""
        # ... function implementation
        return response.parsed.intent
    ```
2.  Next, we define specialized prompts for each intent and a `handle_query` function that acts as our router, directing the query to the correct handler.
    ```python
    prompt_technical_support = "..."
    prompt_billing_inquiry = "..."
    prompt_general_question = "..."
    
    def handle_query(user_query: str, intent: str) -> str:
        """Routes a query to the correct handler based on its classified intent."""
        if intent == IntentEnum.TECHNICAL_SUPPORT:
            prompt = prompt_technical_support.format(user_query=user_query)
        elif intent == IntentEnum.BILLING_INQUIRY:
            prompt = prompt_billing_inquiry.format(user_query=user_query)
        else:
            prompt = prompt_general_question.format(user_query=user_query)
        
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    ```
3.  Now we can test the complete routing workflow.
    ```python
    query = "My internet connection is not working."
    intent = classify_intent(query)
    response = handle_query(query, intent)
    ```
    The query is correctly classified as `TECHNICAL_SUPPORT`, and the system provides a helpful, specialized response asking for more details. This modular approach is far more robust and maintainable than a single prompt trying to handle all possible customer issues.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

The orchestrator-worker pattern takes dynamic behavior a step further. It is one of the most widely deployed patterns in production AI systems [[19]](https://gurusup.com/blog/agent-orchestration-patterns). A central "orchestrator" LLM dynamically breaks down a complex task into subtasks, delegates them to specialized "worker" LLMs, and synthesizes their results [[16]](https://agents.kour.me/orchestrator-worker/), [[17]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent). This pattern is analogous to the master-worker model in distributed computing, providing a scalable way to manage complex operations [[18]](https://www.confluent.io/blog/event-driven-multi-agent-systems/).

This approach is perfect for complex problems where the required steps cannot be predicted in advance. The key difference from simple parallelization is its flexibility; the orchestrator determines the subtasks at runtime based on the specific input [[20]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers). For example, a coding agent might analyze a bug report and decide which files need to be read, modified, and tested, all on the fly. However, this coordination adds latency and complexity, so the pattern should be avoided in time-critical applications or when tasks cannot be decomposed without significant information loss [[21]](https://zencoder.ai/blog/multi-agent-orchestration-patterns).

```mermaid
flowchart LR
  %% Start of the process
  A["User Query"]

  %% Orchestrator component
  B["Orchestrator"]

  %% Sub-tasks generation
  C["Sub-tasks"]

  %% Worker LLMs for execution
  D["Worker LLMs"]

  %% Final output
  E["Synthesized Results"]

  %% Flow of the Orchestrator-Worker pattern
  A -- "initiates" --> B
  B -- "dynamically breaks down into" --> C
  C -- "delegates to" --> D
  D -- "return results" --> B
  B -- "processes and produces" --> E
```
Image 3: A flowchart illustrating the Orchestrator-Worker pattern, showing the flow from a user query to synthesized results via an orchestrator and worker LLMs.

Let's implement a simple customer service system using this pattern.

1.  First, the orchestrator analyzes a complex user query and breaks it down into a list of structured tasks.
    ```python
    def orchestrator(query: str) -> list[Task]:
        """Breaks down a complex query into a list of tasks."""
        # ... function implementation
        return response.parsed.tasks
    ```
2.  We then have specialized worker functions for each task type (`BillingInquiry`, `ProductReturn`, `StatusUpdate`), which simulate interacting with backend systems.
    ```python
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
        # ... function implementation
    
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
        # ... function implementation
    
    def handle_status_worker(order_id: str) -> StatusTask:
        # ... function implementation
    ```
3.  A synthesizer LLM takes the structured outputs from the workers and composes a single, user-friendly response.
    ```python
    def synthesizer(results: list[Task]) -> str:
        """Combines structured results from workers into a single user-facing message."""
        # ... function implementation
        return response.text
    ```
4.  Finally, we tie everything together in a main processing pipeline.
    ```python
    def process_user_query(user_query):
        # 1. Run orchestrator to get tasks
        tasks_list = orchestrator(user_query)
    
        # 2. Run workers based on tasks
        worker_results = []
        for task in tasks_list:
            if task.query_type == QueryTypeEnum.BILLING_INQUIRY:
                worker_results.append(handle_billing_worker(task.invoice_number, user_query))
            # ... other workers
    
        # 3. Run synthesizer
        final_user_message = synthesizer(worker_results)
        print(final_user_message)
    
    complex_customer_query = """
    Hi, I'm writing to you because I have a question about invoice #INV-7890. It seems higher than I expected.
    Also, I would like to return the 'SuperWidget 5000' I bought because it's not compatible with my system.
    Finally, can you give me an update on my order #A-12345?
    """
    
    process_user_query(complex_customer_query)
    ```
    The orchestrator correctly deconstructs the query into three distinct tasks. Each task is handled by its specialized worker, and the synthesizer combines the results into a single, comprehensive email to the customer. This pattern provides a flexible and scalable way to handle unpredictable, multi-part user requests.

## Conclusion

In this lesson, we explored the fundamental workflow patterns that form the backbone of reliable LLM applications. We saw why breaking down complex problems into smaller, modular steps is superior to relying on a single, monolithic prompt. We implemented sequential chaining, optimized it with parallel processing, and added dynamic behavior with routing. Finally, we introduced the orchestrator-worker pattern for handling unpredictable, multi-step tasks.

These patterns—chaining, parallelization, routing, and orchestration—are not just theoretical concepts. They are the practical tools you will use every day as an AI Engineer to build systems that are more accurate, debuggable, and maintainable. In our next lesson, we will give our workflows the ability to interact with the outside world by introducing tools and function calling.

## References
- [1] https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [2] https://www.mdpi.com/2079-9292/13/23/4712
- [3] https://arxiv.org/html/2505.13360v1
- [4] https://www.decodingai.com/p/stop-building-ai-agents-use-these
- [5] https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a
- [6] https://datalearningscience.com/p/design-pattern-prompt-chaining-building
- [7] https://www.together.ai/blog/plan-divide-conquer
- [8] https://futureagi.substack.com/p/how-tool-chaining-fails-in-production
- [9] https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/
- [10] https://mlpills.substack.com/p/diy-17-parallelisation-with-langchain
- [11] https://santhalakshminarayana.github.io/blog/concurrency-patterns-python
- [12] https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a
- [13] https://tianpan.co/blog/2026-03-11-llm-api-resilience-production
- [14] https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/
- [15] https://blog.logrocket.com/llm-routing-right-model-for-requests/
- [16] https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- [17] https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot
- [18] https://agents.kour.me/orchestrator-worker/
- [19] https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent
- [20] https://www.confluent.io/blog/event-driven-multi-agent-systems/
- [21] https://gurusup.com/blog/agent-orchestration-patterns
- [22] https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers
- [23] https://zencoder.ai/blog/multi-agent-orchestration-patterns