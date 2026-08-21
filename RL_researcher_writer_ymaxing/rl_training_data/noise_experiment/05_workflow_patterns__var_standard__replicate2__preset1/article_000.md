# Lesson 5: Basic Workflow Ingredients

In the last lesson, we covered structured outputs, the essential technique for getting reliable, machine-readable data out of an LLM. We now have a solid foundation for both providing context *to* a model and getting predictable results *from* it. With these building blocks, we can move from single LLM calls to building multi-step, production-grade systems.

This lesson is about the fundamental patterns for composing those calls: chaining, parallelization, routing, and orchestration. These are the core ingredients of almost every complex LLM application you will encounter. Mastering them is the first major step toward building sophisticated and reliable AI. We will show you how to break down complex problems into manageable pieces, a skill that separates prototypes from products.

We will cover the following:
- The problems with complex, single-prompt LLM calls.
- How to build sequential workflows by chaining LLM calls.
- How to speed up workflows with parallel processing.
- How to implement dynamic logic using routing.
- How to use the orchestrator-worker pattern for complex, unpredictable tasks.

## The Challenge with Complex Single LLM Calls

When you first start building with LLMs, the temptation is to write a single, massive prompt that does everything at once. It feels efficient. You have a complex task—like generating a FAQ from a set of documents—so you write a detailed set of instructions asking the model to generate questions, find the answers, and cite the sources, all in one go.

This approach often works for a demo, but it quickly falls apart in production. Relying on a single, complex LLM call introduces several problems.

First, it creates a black box that is difficult to debug. When the output is wrong, it is hard to pinpoint which part of the instruction the model failed to follow. Was the question bad? Was the answer incorrect? Or did it just fail to find the right source? Without intermediate steps, you are left guessing.

Second, this monolithic approach lacks modularity. If you want to improve just one part of the process, like the question generation, you have to rewrite and re-test the entire prompt, which can be slow and unpredictable.

Third, long and complex prompts are more susceptible to performance degradation. As we discussed in Lesson 3 on Context Engineering, models can suffer from the "lost-in-the-middle" problem, where they pay less attention to information buried in a long context [[2]]. A single prompt trying to do too much can easily become a "long context" and lead to unreliable outputs.

Let’s look at a practical example. We will start with our setup, which involves importing the necessary libraries, creating the Gemini client, and defining our model.

1.  First, we set up our environment and initialize the Gemini client. We will use `gemini-2.5-flash` for these examples, as it is fast and cost-effective.
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
2.  Next, we define our source content: three mock web pages about renewable energy. We will combine their content to serve as the knowledge base for our FAQ generation task.
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
3.  Now, we create a single, complex prompt that asks the LLM to do everything at once. We also define Pydantic models to get a structured JSON output, a technique we covered in Lesson 4.
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
      "question": "Why is energy storage crucial for renewable energy sources like solar and wind?",
      "answer": "Effective energy storage is key to unlocking the full potential of renewable sources because it allows storing excess energy when plentiful and releasing it when needed, which is crucial for a stable power grid.",
      "sources": [
        "Energy Storage Solutions",
        "Understanding Wind Turbines"
      ]
    }
    ```
While the output seems reasonable, this approach is brittle. The more complex the instructions, the higher the chance of failure. For example, the model might occasionally miss a source or generate a question that is not directly answerable from the text. This is a classic "divide and conquer" problem, which leads us to our first workflow pattern: prompt chaining.

## The Power of Modularity: Why Chain LLM Calls?

Instead of relying on a single prompt, we can break down the task into a series of smaller, more focused steps. This is called **prompt chaining**: a workflow where multiple LLM calls are connected sequentially, with the output of one step feeding into the next [[41]](https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a). This modular approach is a more reliable and manageable way to build complex systems [[36]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

The benefits of this divide-and-conquer strategy are significant.

First, it improves **modularity**. Each LLM call is responsible for a single, well-defined sub-task. This separation of concerns makes the system easier to understand, maintain, and update. You can work on one component without affecting the others.

Second, it enhances **accuracy**. Simpler, more targeted prompts reduce the cognitive load on the LLM, leading to more reliable and higher-quality outputs for each step. This increased reliability at the component level translates to a more robust system overall.

Third, it makes **debugging** much easier. If something goes wrong, you can inspect the inputs and outputs of each step to isolate the point of failure. This transparency is essential for building production-grade applications.

Finally, chaining offers greater **flexibility**. You can swap out individual components, experiment with different models for different steps, or insert programmatic logic between calls. For instance, you could use a cheaper, faster model for a simple classification task and a more powerful, expensive model for a complex generation task within the same workflow.

However, chaining is not without its trade-offs. It can increase latency, as you have to wait for multiple LLM calls to complete sequentially. It can also be more expensive due to the increased number of API calls and total tokens used. Another risk is context degradation, where important information from early steps gets lost or diluted in later stages of the chain [[22]](https://futureagi.substack.com/p/how-tool-chaining-fails-in-production). In production GenAI platforms, these trade-offs are often managed with techniques like caching intermediate results to reduce both latency and cost [[61]](https://huyenchip.com/2024/07/25/genai-platform.html). Despite these downsides, the gains in reliability and maintainability often make prompt chaining the superior choice for complex tasks.

## Building a Sequential Workflow: FAQ Generation Pipeline

Let's refactor our FAQ generation example into a three-step sequential workflow:
1.  **Generate Questions**: Create a list of questions based on the source content.
2.  **Answer Questions**: For each question, generate a concise answer.
3.  **Find Sources**: For each question-answer pair, identify the original source documents.

This modular structure allows us to focus on one task at a time, leading to more consistent and traceable results.

```mermaid
flowchart LR
  A["Input Content"] --> B["Generate Questions"]
  B --> C["Answer Questions"]
  C --> D["Find Sources"]
```
Image 1: A flowchart illustrating the sequential FAQ generation pipeline.

### ### Generate Questions

First, we create a function that focuses solely on generating a list of relevant questions from the provided content.

1.  We start by defining a Pydantic model to structure the list of questions we expect from the LLM.
    ```python
    class QuestionList(BaseModel):
        """A list of questions"""
        questions: list[str] = Field(description="A list of questions")
    ```
2.  Next, we create a targeted prompt for question generation.
    ```python
    prompt_generate_questions = """
    Based on the content below, generate a list of {n_questions} relevant and distinct questions that a user might have.
    
    <provided_content>
    {combined_content}
    </provided_content>
    """.strip()
    ```
3.  Finally, we wrap this logic in a function.
    ```python
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
    A test run gives us a clean list of questions:
    ```text
    - What are the primary environmental and economic benefits of solar energy?
    - How do homeowners financially benefit from installing solar panels?
    - What is the main process by which wind turbines generate electricity?
    ...
    ```

### ### Answer Questions

With a list of questions, our next step is to generate an answer for each one. This function takes a single question and the source content, and returns a concise answer.

1.  The prompt for this step is straightforward. It instructs the model to answer a specific question using only the provided context.
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
    ```
2.  The corresponding function makes a simple LLM call.
    ```python
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
    For the question `"What are the primary environmental and economic benefits of solar energy?"`, it produces a focused answer:
    ```text
    The primary environmental benefit of solar energy is cutting down greenhouse gas emissions by reducing reliance on fossil fuels. Economically, it allows homeowners to significantly lower their monthly electricity bills and potentially sell excess power back to the grid.
    ```

### ### Find Sources

The final step is to identify which of the original documents were used to create the answer. This is crucial for traceability and allows users to verify the information.

1.  We define another Pydantic model for the expected output.
    ```python
    class SourceList(BaseModel):
        """A list of source titles that were used to answer the question"""
        sources: list[str] = Field(description="A list of source titles that were used to answer the question")
    ```
2.  The prompt asks the model to act as a fact-checker, comparing the question and answer against the source content.
    ```python
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
    ```
3.  The function for this step returns a list of source titles.
    ```python
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
    For our example question and answer, it correctly identifies the source:
    ```text
    ['The Benefits of Solar Energy']
    ```

### ### Executing the Workflow

Now, we combine these functions into a complete sequential workflow. The code iterates through each generated question, calls the `answer_question` function, and then the `find_sources` function.

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
The final result is a well-structured list of FAQs, where each entry is generated and verified through a clear, multi-step process. While this approach is reliable, processing each question one by one took over 20 seconds. This latency might be acceptable for some applications, but for others, we need a faster solution.

## Optimizing Sequential Workflows With Parallel Processing

The sequential workflow is robust, but its latency grows linearly with the number of questions. Since the processing for each question (answering and finding sources) is independent of the others, we can run these tasks in parallel to significantly reduce the total execution time.

We can use Python’s `asyncio` library to perform these network-bound LLM calls concurrently. Instead of waiting for each question to be fully processed before starting the next, we can initiate the calls for all questions at once and wait for them all to complete.

### ### Implementing Parallel Processing

First, we need asynchronous versions of our `answer_question` and `find_sources` functions. The `google-genai` library provides an `aio` (asynchronous I/O) client for this purpose.

1.  We define `async` versions of our core functions. The logic is the same, but we use `await` to make the API calls non-blocking [[26]](https://santhalakshminarayana.github.io/blog/concurrency-patterns-python).
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
2.  Next, we create a function to process a single question in parallel. It generates the answer and finds the sources asynchronously.
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

### ### Executing the Parallel Workflow

With these async functions, we can now build our parallel workflow. The `generate_questions` step remains synchronous, as we need the questions before we can process them. However, we then use `asyncio.gather` to run `process_question_parallel` for all questions concurrently [[27]](https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a).

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
By running the tasks in parallel, we reduced the total processing time from 22.20 seconds to just 8.98 seconds—a significant improvement.

This comparison highlights the trade-offs. Sequential processing is simpler and more predictable, making it easier to debug. Parallel processing is much faster but introduces complexity in error handling and resource management. For applications where latency is critical, parallelization is a powerful optimization technique.

One important caveat: when making many concurrent API calls, you are more likely to hit rate limits [[9]](https://tianpan.co/blog/2026-03-11-llm-api-resilience-production). Production systems need robust error handling, such as exponential backoff with jitter, to manage these limits gracefully [[8]](https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt). This also includes handling individual task failures within a parallel batch so that one failed call does not bring down the entire workflow [[62]](https://www.buildmvpfast.com/blog/prompt-chaining-patterns-production-ai-sequential-parallel-conditional-2026).

## Introducing Dynamic Behavior: Routing and Conditional Logic

So far, our workflows have been deterministic: every input goes through the same sequence of steps. But what if we need to handle different types of inputs differently? This is where **routing** comes in.

Routing introduces conditional logic into our workflows. Instead of a fixed path, we can create branches that direct the input to specialized handlers based on its characteristics. This is another application of the "divide and conquer" principle. By routing different types of requests to different, specialized prompts, we avoid creating a single, monolithic prompt that has to handle every possible case. This keeps our prompts focused and optimized for a single responsibility, which generally improves performance and reliability [[36]](https://www.decodingai.com/p/stop-building-ai-agents-use-these).

While simple intent classification is a common starting point, routing can be more sophisticated. Strategies can include routing based on a model's confidence score, query complexity, or even cost considerations, directing requests to more powerful models only when necessary [[63]](https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/). In production, a common architecture is the "cascade pattern," which uses a sequence of routers—starting with a fast, cheap method like semantic search and escalating to a more powerful LLM-based classifier only for ambiguous cases [[64]](https://tianpan.co/blog/2026-04-16-intent-classification-agent-routers).

The router itself, often an LLM call, can be optimized by fine-tuning it on domain-specific data to improve its accuracy on specialized queries [[65]](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/). This allows us to build dynamic systems that can adapt their behavior based on the user's intent. For example, a customer support system could classify an incoming query as a "billing issue," "technical problem," or "general question," and then route it to a specialized agent trained to handle that specific type of inquiry [[12]](https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot).

## Building a Basic Routing Workflow

Let's build a simple routing workflow for a customer service system. The goal is to classify a user's query and then route it to the appropriate specialized handler.

```mermaid
graph TD
    A["User Input"] --> B["Intent Classification"]
    B -->|"Technical Intent"| C["Technical Support Handler"]
    B -->|"Billing Intent"| D["Billing Inquiry Handler"]
    B -->|"General Intent"| E["General Question Handler"]
    C --> F["Final Responses"]
    D --> F
    E --> F
```
Image 2: A flowchart illustrating a routing workflow for customer service queries.

### ### Intent Classification

First, we need a classifier. We will use an LLM to determine the user's intent from their query.

1.  We define the possible intents using a Python `Enum` and a Pydantic model for the structured output.
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
    ```
2.  The classification prompt asks the model to categorize the user's query into one of our predefined intents.
    ```python
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
3.  The `classify_intent` function takes a user query and returns the classified intent.
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
    ```
    Testing with a few sample queries shows the classifier works as expected:
    - `"My internet connection is not working."` → `TECHNICAL_SUPPORT`
    - `"I think there is a mistake on my last invoice."` → `BILLING_INQUIRY`
    - `"What are your opening hours?"` → `GENERAL_QUESTION`

This simple classification works well, but a production system might need more nuance. For instance, instead of forcing a choice, you could use confidence thresholds to implement a three-stage logic: `ALLOW` the request if confidence is high, `ABSTAIN` and ask for clarification if confidence is medium, or `DENY` if the query is out-of-scope [[66]](https://huggingface.co/blog/perfecXion/intentguard). This prevents the system from confidently misrouting ambiguous queries. This single-call approach for classification is common in production systems, as it minimizes round-trip latency compared to more complex, multi-step classification schemes [[67]](https://docs.nvidia.com/aiq-blueprint/2.0.0/architecture/agents/intent-classifier.html).

### ### Defining Specialized Handlers

Now that we can classify the intent, we need to create specialized prompts for each case. We will have one handler for technical support, one for billing, and a general fallback.

1.  We define three distinct prompts, each tailored to a specific intent.
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
2.  The `handle_query` function acts as our router. It takes the user query and the classified intent, selects the appropriate prompt, and calls the LLM.
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
    Running our sample queries through the full workflow demonstrates the dynamic behavior. Each query is routed to its specialized handler, resulting in a context-appropriate response. This pattern is fundamental for building adaptable and intelligent AI systems.

## Orchestrator-Worker Pattern: Dynamic Task Decomposition

Chaining, parallelization, and routing are powerful, but they rely on predefined paths. What happens when a task is so complex that you cannot predict the necessary subtasks in advance? This is where the **orchestrator-worker** pattern comes in.

In this workflow, a central "orchestrator" LLM analyzes a complex user request and dynamically breaks it down into smaller, executable subtasks. These subtasks are then delegated to specialized "worker" components, which can be other LLM calls or external tools. Once the workers complete their tasks, the orchestrator synthesizes their results into a final, coherent response [[32]](https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent).

A key aspect of this pattern is not just decomposing the task, but also allocating the subtasks intelligently. The workers do not have to be identical. An orchestrator can assign simpler subtasks, like data extraction, to smaller, faster models, while routing more complex reasoning tasks to more powerful models, optimizing for both cost and performance [[68]](https://labelyourdata.com/articles/llm-fine-tuning/llm-orchestration).

You can think of the orchestrator as being analogous to a sophisticated operating system scheduler. Instead of just processing tasks in a fixed order, it can dynamically prioritize them based on factors like complexity, resource requirements, or system load, ensuring that the entire workflow is executed efficiently [[69]](https://latitude.so/blog/how-task-scheduling-optimizes-llm-workflows).

The key advantage of this pattern is its flexibility. Unlike simple parallelization where subtasks are fixed, the orchestrator determines the plan at runtime based on the specific input [[19]](https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers). This makes it ideal for handling unpredictable, multifaceted queries that require diverse expertise, such as a customer support request that involves a billing issue, a product return, and an order status update all at once [[16]](https://agents.kour.me/orchestrator-worker/).

```mermaid
flowchart LR
  %% User Input
  A["Complex User Query"]

  %% Orchestrator LLM
  B["Orchestrator LLM"]

  %% Sub-tasks and Worker LLMs
  subgraph TaskDecompositionAndExecution["Dynamic Decomposition & Parallel Execution"]
    C["Sub-tasks"]
    subgraph Workers["Worker LLMs (Parallel)"]
      D1["Worker LLM 1<br/>(Specialized)"]
      D2["Worker LLM 2<br/>(Specialized)"]
      D3["Worker LLM N<br/>(Specialized)"]
    end
  end

  %% Synthesis and Final Response
  E["Synthesis of Results"]
  F["Final Coherent Response"]

  %% Flow
  A -- "receives" --> B
  B -- "dynamically breaks down into" --> C
  C -- "delegates to" --> D1
  C -- "delegates to" --> D2
  C -- "delegates to" --> D3

  D1 -- "returns result" --> B
  D2 -- "returns result" --> B
  D3 -- "returns result" --> B

  B -- "collects results for" --> E
  E -- "generates" --> F

  %% Visual differentiation
  classDef llm stroke-width:2px
  class B,D1,D2,D3 llm
```
Image 3: A flowchart illustrating the orchestrator-worker pattern with dynamic decomposition and parallel execution.

While our example uses a centralized orchestrator, it is worth noting that other architectures exist. One alternative is a decentralized "dynamic handoff" pattern, where agents themselves assess a task and decide whether to handle it or pass it to a more suitable specialist, without a single coordinator directing the flow [[70]](https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production).

Let's build a system to handle our complex customer query.

### ### The Orchestrator

The orchestrator’s job is to analyze the user's query and decompose it into a structured list of tasks for the workers.

1.  We define Pydantic models for the tasks. This ensures the orchestrator's output is structured and machine-readable.
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
    ```
2.  The orchestrator prompt instructs the LLM to break down the query into sub-tasks, identifying the `query_type` and extracting the necessary parameters for each.
    ```python
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

### ### The Workers

We need three specialized workers: one for billing, one for returns, and one for order status. In a real system, these workers would interact with external APIs or databases. For this example, we will simulate their behavior.

1.  **Billing Worker:** This worker handles invoice inquiries. It uses an LLM to extract the specific user concern and then simulates opening an investigation, returning a structured result.
    ```python
    def handle_billing_worker(invoice_number: str, original_user_query: str) -> BillingTask:
        """
        Handles a billing inquiry.
        1. Uses an LLM to extract the specific concern about the invoice from the original query.
        2. Simulates opening an investigation.
        3. Returns structured data about the action taken.
        """
        # ... (LLM call to extract concern)
        # ... (Simulate backend action)
        return BillingTask(...)
    ```
2.  **Product Return Worker:** This worker processes return requests, generating a simulated RMA number and shipping instructions.
    ```python
    def handle_return_worker(product_name: str, reason_for_return: str) -> ReturnTask:
        """
        Handles a product return request.
        1. Simulates generating an RMA number and providing return instructions.
        2. Returns structured data.
        """
        # ... (Simulate backend action)
        return ReturnTask(...)
    ```
3.  **Order Status Worker:** This worker fetches the status for a given order ID, simulating a lookup in a backend system.
    ```python
    def handle_status_worker(order_id: str) -> StatusTask:
        """
        Handles an order status update request.
        1. Simulates fetching order status from a backend system.
        2. Returns structured data.
        """
        # ... (Simulate backend action)
        return StatusTask(...)
    ```

### ### The Synthesizer

After the workers have completed their tasks, the synthesizer's job is to combine their structured outputs into a single, user-friendly response.

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
    # ... (Formats worker results into bullet points)
    prompt = prompt_synthesizer.format(formatted_results=formatted_results)
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    return response.text
```

### ### The Full Pipeline

Finally, we create a main function that orchestrates the entire process: it calls the orchestrator, dispatches tasks to the appropriate workers, and uses the synthesizer to craft the final response.

When we run a complex query through this system, the orchestrator first breaks it down into three distinct tasks. Then, the corresponding workers execute in parallel, and their results are collected. Finally, the synthesizer combines the structured outputs into a single, helpful email to the customer. This pattern allows us to handle complex, unpredictable requests in a modular, scalable, and reliable way.

## Conclusion

In this lesson, we have moved beyond single LLM calls and explored the fundamental patterns for building multi-step AI workflows. We have seen how breaking down complex tasks into smaller, more manageable pieces is a core principle of AI engineering.

We started with **prompt chaining**, a sequential pattern that improves reliability and debuggability by dedicating each LLM call to a specific sub-task. We then optimized this with **parallelization**, significantly reducing latency by running independent tasks concurrently. We introduced dynamic behavior with **routing**, using an LLM to classify user intent and direct the workflow down specialized paths. Finally, we explored the **orchestrator-worker** pattern, a flexible approach where a central orchestrator dynamically decomposes complex problems and delegates subtasks to specialized workers.

These patterns—chaining, parallelization, routing, and orchestration—are not just theoretical concepts; they are the practical building blocks you will use to construct robust, production-ready AI applications. They provide the control, modularity, and scalability needed to move from simple prototypes to sophisticated systems.

In our next lesson, we will give our workflows the ability to interact with the outside world. We will dive into agent tools and function calling, learning how to empower LLMs to take action, query databases, and call external APIs.

## References

- [1] Comparative Analysis of Prompt Strategies for Large Language Models: Single-Task vs. Multitask Prompts. (2024). MDPI. https://www.mdpi.com/2079-9292/13/23/4712
- [2] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv. https://dev.to/thousand_miles_ai/the-lost-in-the-middle-problem-why-llms-ignore-the-middle-of-your-context-window-3al2
- [3] Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023). Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting. arXiv. https://aclanthology.org/2025.ommm-1.4.pdf
- [4] Zhong, W., Cui, C., Zha, Z., Chen, J., & Li, Y. (2024). ZeMPE: A Zero-Shot Multiple-Problem Evaluation of Large Language Models. arXiv. https://aclanthology.org/2025.gem-1.14.pdf
- [5] Chen, L., Chen, Y., Chen, J., & Wang, W. Y. (2025). When Large Language Models Follow Rules with Conflicting Human Interests. arXiv. https://arxiv.org/html/2505.13360v1
- [7] Challenges with rate limiting and handling API responses in high volume requests. (2024). Google for Developers. https://discuss.ai.google.dev/t/challenges-with-rate-limiting-and-handling-api-responses-in-high-volume-requests/61903
- [8] 429 on Vertex AI API - how to send 5-20 parallel gemini-api requests without hitting rate limit? (2024). Stack Overflow. https://stackoverflow.com/questions/79924021/429-on-vertex-ai-api-how-to-send-5-20-parallel-gemini-api-requests-without-hitt
- [9] Pan, T. (2026). LLM API Resilience in Production: Rate Limits, Failover, and the Hidden Costs of Naive Retry Logic. https://tianpan.co/blog/2026-03-11-llm-api-resilience-production
- [11] LLM-Based Prompt Routing. (2024). Emergent Mind. https://www.emergentmind.com/topics/llm-based-prompt-routing
- [12] A Beginner's Guide to LLM Intent Classification for Chatbots. (2024). Vellum AI. https://www.vellum.ai/blog/how-to-build-intent-detection-for-your-chatbot
- [13] Top 5 LLM Routing Techniques. (2024). Maxim.ai. https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/
- [14] Bajaj, A., Chen, Z., & Chen, W. (2025). Universal Model Routing with Mixture of Experts. arXiv. https://arxiv.org/html/2502.08773v1
- [15] Multi-LLM routing strategies for generative AI applications on AWS. (2024). AWS Machine Learning Blog. https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- [16] Pattern: Orchestrator-Worker (Coordinator). (2024). Kour.me. https://agents.kour.me/orchestrator-worker/
- [17] DIY #17 Orchestrator-Worker LLM Agent. (2024). ML Pills. https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent
- [18] Building a Self-Healing AI Orchestrator with Reflexion Patterns. (2024). Stevens Institute of Technology. https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/
- [19] Orchestrator-Workers. (2024). Claude Cookbook. https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers
- [20] LLMOps in Production: 457 Case Studies of What Actually Works. (2025). ZenML. https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works
- [21] LLMOps in Production: 287 More Case Studies of What Actually Works. (2024). ZenML. https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works
- [22] How Tool Chaining Fails in Production. (2024). FutureAGI. https://futureagi.substack.com/p/how-tool-chaining-fails-in-production
- [23] ChainRAG: A Progressive Retrieval Framework for Large Language Models. (2025). ACL Anthology. https://aclanthology.org/2025.acl-long.1089.pdf
- [24] Keeping AI Agents Grounded: Context Engineering Strategies that Prevent Context Rot Using Milvus. (2024). Milvus.io. https://milvus.io/blog/keeping-ai-agents-grounded-context-engineering-strategies-that-prevent-context-rot-using-milvus.md
- [25] Context Rot. (2024). Morph. https://www.morphllm.com/context-rot
- [26] Asynchronous or Concurrency Patterns in Python with Asyncio. (2024). Santhana Narayana. https://santhalakshminarayana.github.io/blog/concurrency-patterns-python
- [27] Python Concurrency Showdown: Asyncio vs. Threading vs. Multiprocessing. (2024). Medium. https://medium.com/@sizanmahmud08/python-concurrency-showdown-asyncio-vs-threading-vs-multiprocessing-which-should-you-choose-in-31205161899a
- [28] Concurrency and Parallelism in Python. (2024). TestDriven.io. https://testdriven.io/blog/python-concurrency-parallelism/
- [29] Concurrency and Parallelism in Python: Threads, Multiprocessing, and Async Programming. (2024). Dev.to. https://dev.to/nkpydev/concurrency-and-parallelism-in-python-threads-multiprocessing-and-async-programming-64d
- [30] Concurrency in async/await and threading. (2025). JetBrains. https://blog.jetbrains.com/pycharm/2025/06/concurrency-in-async-await-and-threading/
- [31] Orchestrator-Workers. (2024). Claude Cookbook. https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers
- [32] DIY #17 Orchestrator-Worker LLM Agent. (2024). ML Pills. https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent
- [34] Build Advanced Customer Support LLM with Multi-Agent Workflow. (2024). Socure. https://www.socure.com/tech-blog/build-advanced-customer-support-llm-multi-agent-workflow
- [35] AI Agent Orchestration Patterns. (2024). Product School. https://productschool.com/blog/artificial-intelligence/ai-agent-orchestration-patterns
- [36] Stop Building AI Agents. Use These 5 LLM Workflows Instead. (2024). Decoding AI. https://www.decodingai.com/p/stop-building-ai-agents-use-these
- [38] Choosing the Right Orchestration Pattern for Multi-Agent Systems. (2024). Kore.ai. https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems
- [39] Building a Self-Healing AI Orchestrator with Reflexion Patterns. (2024). Stevens Institute of Technology. https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/
- [40] Five Proven Prompt Engineering Techniques. (2024). Lenny's Newsletter. https://www.lennysnewsletter.com/p/five-proven-prompt-engineering-techniques
- [41] A Practical Guide to Prompt Engineering Techniques and Their Use Cases. (2024). Medium. https://medium.com/@fabiolalli/a-practical-guide-to-prompt-engineering-techniques-and-their-use-cases-5f8574e2cd9a
- [42] 10 Prompt Engineering Techniques for Super Simple Explanation. (2024). Scrum.org. https://www.scrum.org/resources/blog/10-prompt-engineering-techniques-super-simple-explanation
- [44] Prompt Engineering Techniques. (2024). K2View. https://www.k2view.com/blog/prompt-engineering-techniques/
- [45] Orchestrating Multi-Step LLM Chains: Best Practices. (2024). Deepchecks. https://deepchecks.com/orchestrating-multi-step-llm-chains-best-practices/
- [46] LLM Workflow Patterns. (2024). ML Pills. https://mlpills.substack.com/p/issue-110-llm-workflow-patterns
- [47] Compounding Error Effect in Large Language Models: A Growing Challenge. (2024). W&B. https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge
- [48] SPRINT: Structured Planning and Parallel Execution in Reasoning Models. (2024). Stanford University. https://scalingintelligence.stanford.edu/pubs/sprint.pdf
- [49] A Developer's Guide to Multi-Agent Patterns in ADK. (2024). Google for Developers Blog. https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/
- [50] Agentic AI Design Patterns. (2024). LinkedIn. https://www.linkedin.com/posts/chiragsubramanian_agentic-ai-design-patterns-my-practical-activity-7416830806939230208-nRFc
- [51] Stop Building AI Agents. Use These 5 LLM Workflows Instead. (2024). Decoding AI. https://www.decodingai.com/p/stop-building-ai-agents-use-these
- [52] LLM Workflow Patterns. (2024). ML Pills. https://mlpills.substack.com/p/issue-110-llm-workflow-patterns
- [53] Orchestrator-Workers. (2024). Claude Cookbook. https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers
- [54] Building Effective Agents. (2024). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [55] AI Prompt Orchestration Techniques and Tools You Need. (2024). Scoutos. https://www.scoutos.com/blog/ai-prompt-orchestration-techniques-and-tools-you-need
- [56] Stop Building AI Agents. Use These 5 LLM Workflows Instead. (2024). Decoding AI. https://www.decodingai.com/p/stop-building-ai-agents-use-these
- [57] LLM Workflow Patterns. (2024). ML Pills. https://mlpills.substack.com/p/issue-110-llm-workflow-patterns
- [58] Design Pattern: Prompt Chaining - Building Reliable LLM Workflows. (2024). Data Learning Science. https://datalearningscience.com/p/design-pattern-prompt-chaining-building
- [59] Prompt Chaining. (2024). Udemy. https://blog.udemy.com/prompt-chaining/
- [60] Prompt Chaining. (2024). Agentic Design. https://agentic-design.ai/patterns/prompt-chaining
- [61] Building a Generative AI Platform. (2024). Huyen Chip. https://huyenchip.com/2024/07/25/genai-platform.html
- [62] Prompt Chaining Patterns for Production AI. (2026). Build MVP Fast. https://www.buildmvpfast.com/blog/prompt-chaining-patterns-production-ai-sequential-parallel-conditional-2026
- [63] Top 5 LLM Routing Techniques. (2024). Maxim.ai. https://www.getmaxim.ai/articles/top-5-llm-routing-techniques/
- [64] Intent Classification for Agent Routers. (2026). Tian Pan. https://tianpan.co/blog/2026-04-16-intent-classification-agent-routers
- [65] Multi-LLM routing strategies for generative AI applications on AWS. (2024). AWS Machine Learning Blog. https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- [66] IntentGuard: A Guardrail for Out-of-Distribution Intents. (2024). Hugging Face. https://huggingface.co/blog/perfecXion/intentguard
- [67] Intent Classifier Agent. (2024). NVIDIA AI-Q Blueprint. https://docs.nvidia.com/aiq-blueprint/2.0.0/architecture/agents/intent-classifier.html
- [68] LLM Orchestration. (2024). Label Your Data. https://labelyourdata.com/articles/llm-fine-tuning/llm-orchestration
- [69] How Task Scheduling Optimizes LLM Workflows. (2024). Latitude. https://latitude.so/blog/how-task-scheduling-optimizes-llm-workflows
- [70] Multi-Agent Orchestration Patterns for Production. (2024). Beam.ai. https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production