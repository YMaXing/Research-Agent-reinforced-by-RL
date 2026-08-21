# Lesson 4: Structured Outputs

In our previous lessons, we laid the groundwork for AI Engineering. We explored the AI agent landscape, looked at the difference between rule-based LLM workflows and autonomous AI agents, and covered context engineering: the art of feeding the right information to an LLM. In this lesson, we will tackle a fundamental challenge: getting structured and reliable information *out* of an LLM.

LLMs operate in a world of unstructured data and probabilities, where we input instructions in plain English and get results as plain text. This subdomain of engineering is often called "Software 3.0". Our application, however, relies on deterministic code and predictable data structures, which is known as "Software 1.0". Structured outputs are the bridge between these two worlds, a fundamental technique for forcing LLMs to return consistent, machine-readable data. Mastering this is essential for any AI engineer building production-grade systems.

## Understanding why structured outputs are critical

Before we start coding, it is crucial to understand why structured outputs are foundational to building reliable AI applications. When an LLM returns a free-form string, you face the messy task of parsing it. This often involves fragile regular expressions or string-splitting logic that can easily break if the model changes its phrasing even slightly [[1]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk), [[2]](https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP). Structured outputs solve this by forcing the model’s response into a predictable format like JSON [[3]](https://developer.hpe.com/blog/using-structured-outputs-in-vllm). However, this control comes with a potential trade-off. Some research suggests that strictly enforcing a structured format can sometimes reduce an LLM’s reasoning performance compared to letting it generate free-form text [[15]](https://arxiv.org/abs/2408.02442v1).

This approach offers several key benefits. First, structured outputs are easy to parse, manipulate, and debug. Instead of wrestling with raw text, you work with clean Python objects, making your code more predictable. Using libraries like Pydantic adds a layer of data and type validation [[4]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs), [[5]](https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation/). If the LLM returns a string where an integer is expected, your application raises a clear validation error immediately, preventing bad data from propagating.

Structured outputs create a formal contract between the LLM and your application code, much like an OpenAPI specification defines a contract for a traditional web service [[16]](https://www.baseten.co/blog/function-calling-and-structured-output-for-llms). This makes the entire system more verifiable and auditable [[17]](https://www.leewayhertz.com/structured-outputs-in-llms), and it becomes easier to orchestrate steps in a workflow or agent [[6]](https://www.decodingai.com/p/llm-structured-outputs-the-only-way). When you know what information you have, it is much simpler to pass it to the next LLM call or a downstream system like a database or API [[7]](https://www.leewayhertz.com/structured-outputs-in-llms). For example, a popular use case is to extract entities like names, tags, and dates to build knowledge graphs for advanced RAG, a technique used in specialized domains like navigating medical regulatory knowledge [[18]](https://ebiquity.umbc.edu/get/a/publication/1476.pdf).

```mermaid
flowchart TD
    subgraph "Software 3.0"
        A[LLM]
        A --> B[Messy strings]
        A --> C[Uncontrolled outputs]
    end
    subgraph "Software 1.0"
        D[Structured Outputs <br> (JSON/Pydantic)]
        D --> E[Easy parsing]
        D --> F[Data validation]
        D --> G[Guardrails]
    end
    subgraph "Application"
        H[Downstream Processing]
    end
    B --> D
    C --> D
    D --> H
```

Image 1: A flowchart illustrating how structured outputs bridge the gap between LLMs (Software 3.0) and traditional code (Software 1.0) for downstream processing.

To understand how this works in practice, we will explore three implementations: from scratch with JSON, from scratch with Pydantic, and natively with the Gemini API.

## Implementing structured outputs from scratch using JSON

To build an intuition for what modern LLM APIs offer, we will first implement structured outputs from scratch. Our goal is to prompt a model to return a JSON object and then parse it into a Python dictionary. We will demonstrate this by extracting key details from a financial document.

<aside>
💡

You can find the code for this lesson in the accompanying notebook on our GitHub repository.

</aside>

1.  We begin by setting up our environment and initializing the Gemini client. For our examples, we will use `gemini-1.5-flash`, which is fast and cost-effective.

    ```python
    import json
    from google import genai
    from utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])

    client = genai.Client()
    MODEL_ID = "gemini-1.5-flash"
    ```

2.  Next, we define a sample document for analysis.

    ```python
    DOCUMENT = """
    # Q3 2023 Financial Performance Analysis

    The Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement,
    beating market expectations. These impressive results reflect our successful product strategy
    and strong market positioning.

    Our core business segments demonstrated remarkable resilience, with digital services leading
    the growth at 25% year-over-year. The expansion into new markets has proven particularly
    successful, contributing to 30% of the total revenue increase.

    Customer acquisition costs decreased by 10% while retention rates improved to 92%,
    marking our best performance to date. These metrics, combined with our healthy cash flow
    position, provide a strong foundation for continued growth into Q4 and beyond.
    """
    ```

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` and `<json>` to separate inputs from instructions. This is a common and effective prompt engineering technique for improving clarity [[8]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api).

    ```python
    prompt = f"""
    Analyze the following document and extract metadata from it.
    The output must be a single, valid JSON object with the following structure:
    <json>
    {{
        "summary": "A concise summary of the article.",
        "tags": ["list", "of", "relevant", "tags"],
        "keywords": ["list", "of", "key", "concepts"],
        "quarter": "Q...",
        "growth_rate": "...%",
    }}
    </json>

    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

4.  We send the prompt to the model and inspect the raw response. As expected, the model returns a JSON object, but it is often wrapped in Markdown code blocks.

    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    ```

    It outputs:

    ```text
    ```json
    {
        "summary": "The Q3 2023 financial report highlights a strong performance with a 20% increase in revenue and 15% growth in user engagement, surpassing market expectations. This success is attributed to a robust product strategy, effective market positioning, and successful expansion into new markets, leading to improved customer retention and reduced acquisition costs.",
        "tags": [
            "financials",
            "earnings report",
            "business performance",
            "revenue growth",
            "market expansion",
            "Q3 2023"
        ],
        "keywords": [
            "Q3 2023",
            "revenue",
            "user engagement",
            "market expectations",
            "product strategy",
            "market positioning",
            "digital services",
            "new markets",
            "customer acquisition costs",
            "retention rates",
            "cash flow"
        ],
        "quarter": "Q3 2023",
        "growth_rate": "20%"
    }
    ```
    ```

5.  To handle this, we create a helper function to strip the Markdown and XML tags, leaving a clean JSON string.

    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
        return json.loads(response)
    ```

6.  Finally, we parse the string into a Python dictionary, which can now be used in our application.

    ```python
    parsed_response = extract_json_from_response(response.text)
    ```

    It outputs:

    ```json
    {'summary': 'The Q3 2023 financial report highlights a strong performance with a 20% increase in revenue and 15% growth in user engagement, surpassing market expectations. This success is attributed to a robust product strategy, effective market positioning, and successful expansion into new markets, leading to improved customer retention and reduced acquisition costs.', 'tags': ['financials', 'earnings report', 'business performance', 'revenue growth', 'market expansion', 'Q3 2023'], 'keywords': ['Q3 2023', 'revenue', 'user engagement', 'market expectations', 'product strategy', 'market positioning', 'digital services', 'new markets', 'customer acquisition costs', 'retention rates', 'cash flow'], 'quarter': 'Q3 2023', 'growth_rate': '20%'}
    ```

This manual method works, but it relies on post-processing and lacks data validation. If the LLM makes a mistake, like outputting a string instead of an integer, our application will fail. Next, we will see how Pydantic provides a more robust solution.

## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. This is where Pydantic comes in. It is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[9]](https://pydantic.dev/articles/llm-intro).

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This "fail-fast" behavior is essential for building reliable systems, preventing bad data from causing hard-to-debug errors later. This is a major improvement over simple JSON parsing, as it introduces a validation layer that catches errors early.

Let's refactor our previous example to use Pydantic.

1.  We define our desired data structure as a Pydantic class, using standard Python type hints. Pydantic works with Python’s `typing` module, but since Python 3.9, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`.

    ```python
    from pydantic import BaseModel, Field

    class DocumentMetadata(BaseModel):
        """A class to hold structured metadata for a document."""
        summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
        tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
        keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
        quarter: str = Field(description="The quarter of the financial year described in the document (e.g, Q3 2023).")
        growth_rate: str = Field(description="The growth rate of the company described in the document (e.g, 10%).")
    ```

    You can also nest Pydantic models to represent more complex, hierarchical data. This helps organize your data logically and reflects real-world complexity. However, it is good practice to keep schemas from becoming overly complex, as this can confuse the LLM and lead to errors, such as malformed nested objects, type mismatches, or missing fields [[19]](https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic).

    ```python
    class Summary(BaseModel):
        text: str
        sentiment: float

    class Tag(BaseModel):
        label: str
        relevance: float

    class ComplexDocumentMetadata(BaseModel):
        summary: Summary
        tags: list[Tag]
    ```

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[10]](https://ai.google.dev/gemini-api/docs/structured-output), [[11]](https://platform.openai.com/docs/guides/structured-outputs). Internally, these APIs use a technique called constrained decoding. At each step of text generation, the model calculates probabilities (logits) for every possible next token. By applying a logit mask, the API can forbid the model from choosing tokens that would violate the schema, effectively forcing compliance [[20]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction).

    ```python
    schema = DocumentMetadata.model_json_schema()
    ```

    The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process.

    ```json
    {'description': 'A class to hold structured metadata for a document.', 'properties': {'summary': {'description': 'A concise, 1-2 sentence summary of the document.', 'title': 'Summary', 'type': 'string'}, 'tags': {'description': 'A list of 3-5 high-level tags relevant to the document.', 'items': {'type': 'string'}, 'title': 'Tags', 'type': 'array'}, 'keywords': {'description': 'A list of specific keywords or concepts mentioned.', 'items': {'type': 'string'}, 'title': 'Keywords', 'type': 'array'}, 'quarter': {'description': 'The quarter of the financial year described in the document (e.g, Q3 2023).', 'title': 'Quarter', 'type': 'string'}, 'growth_rate': {'description': 'The growth rate of the company described in the document (e.g, 10%).', 'title': 'Growth Rate', 'type': 'string'}}, 'required': ['summary', 'tags', 'keywords', 'quarter', 'growth_rate'], 'title': 'DocumentMetadata', 'type': 'object'}
    ```

3.  We update our prompt to include this JSON Schema, giving the model a more precise set of instructions.

    ```python
    prompt = f"""
    Please analyze the following document and extract metadata from it.
    The output must be a single, valid JSON object that conforms to the following JSON Schema:
    <json>
    {json.dumps(schema, indent=2)}
    </json>

    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

4.  We call the model and extract the JSON string as before.

    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    parsed_response = extract_json_from_response(response.text)
    ```

    It outputs:

    ```json
    {'summary': 'The Q3 2023 earnings report indicates strong financial performance with a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy, market expansion, and improved customer retention.', 'tags': ['Financial Performance', 'Earnings Report', 'Business Growth', 'Market Expansion', 'Customer Metrics'], 'keywords': ['Q3 2023', 'revenue increase', 'user engagement', 'digital services', 'new markets', 'customer acquisition costs', 'retention rates', 'cash flow'], 'quarter': 'Q3 2023', 'growth_rate': '20%'}
    ```

5.  Now, the biggest difference is that we can load the output dictionary into our Pydantic model and validate it.

    ```python
    try:
        document_metadata = DocumentMetadata.model_validate(parsed_response)
        print("\nValidation successful!")
    except Exception as e:
        print(f"\nValidation failed: {e}")
    ```

    It outputs:

    ```text
    Validation successful!
    ```

    The `document_metadata` object can now be safely used throughout your application. This is the main advantage: you move from unclear dictionaries to clean, predictable Python objects. If the LLM returned `tags` as a single string instead of a list of strings, Pydantic would have raised a `ValidationError`, catching the error immediately.

    A more advanced pattern is to build a retry mechanism. If Pydantic validation fails, you can automatically send a new request to the LLM, including the validation error message in the prompt. This feedback helps the model correct its mistake on the next attempt, making the extraction process more resilient [[21]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

    While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis and do not perform runtime validation [[12]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to), [[13]](https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg). If the LLM returns a string where an integer is expected, these tools will not catch the error. Pydantic’s runtime validation, type constraints, and clear schema definitions make it our favorite way for structuring and validating data in our AI apps.

## Implementing structured outputs using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually. When working with modern APIs such as Gemini and OpenAI, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective than manual prompt engineering, as the vendor will always handle the optimization on top of their models better than you can [[10]](https://ai.google.dev/gemini-api/docs/structured-output), [[14]](https://python.langchain.com/docs/how_to/structured_output/). Be aware that the first API call with a new schema may have higher latency as the service processes and caches it, but subsequent calls will be faster [[22]](https://community.openai.com/t/introducing-structured-outputs/896022).

Let’s see how to achieve the same result using the Gemini API’s native capabilities.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.

    ```python
    from google.genai import types

    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes our prompt significantly shorter and cleaner, eliminating the need to manually inject any schema.

    ```python
    prompt = f"""
    Analyze the following document and extract its metadata.

    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

3.  Now, we call the model, passing our simplified prompt and the new configuration object.

    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
    ```

4.  The Gemini client automatically parses the output for us. By accessing the `response.parsed` attribute, we receive a ready-to-use instance of our `DocumentMetadata` Pydantic model.

    ```python
    document_metadata = response.parsed
    print(f"Type of the response: `{type(document_metadata)}`")
    ```

    It outputs:

    ```text
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```

One important caveat when using Gemini's native structured output is that the API may reorder the keys in your schema alphabetically in its response. This can break logic that depends on a specific order, such as chain-of-thought reasoning where a `reasoning` field must appear before an `answer` field. If key order is important, you may need to name your fields to enforce the desired alphabetical sequence, for example, using `1_reasoning` and `2_answer` [[23]](https://dylancastillo.co/posts/gemini-structured-outputs.html).

This native approach is robust, efficient, and requires less code. It is the recommended way for modern LLM APIs.

## Conclusion: Structured Outputs Are Everywhere

Structured outputs are a fundamental pattern in AI engineering, connecting the probabilistic nature of LLMs with the deterministic world of software. Whether you are building a simple summarization workflow or a complex research agent, you will use structured outputs to ensure reliability and control.

This pattern will be a recurring theme throughout this course. In our next lesson, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between different components. Later, when we build agents that can take action (Lesson 6) or reason about the world (Lesson 7), structured outputs will be how they parse information and decide what to do next. Mastering this technique is a key step toward building powerful and predictable AI systems.

## References

- [1] Structured Output in 2026: Stop Parsing JSON with Regex and Do It Right. (n.d.). DEV Community. [https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk)
- [2] Iusztin, P. (2025, November 13). If you use regex and string splits to parse your LLM outputs, read this... LinkedIn. [https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP](https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP)
- [3] Using structured outputs in vLLM. (n.d.). HPE Developer Community. [https://developer.hpe.com/blog/using-structured-outputs-in-vllm](https://developer.hpe.com/blog/using-structured-outputs-in-vllm)
- [4] The Complete Guide to Using Pydantic for Validating LLM Outputs. (n.d.). MachineLearningMastery.com. [https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs)
- [5] How to Keep LLM Outputs Predictable Using Pydantic Validation. (n.d.). freeCodeCamp.org. [https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation](https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation)
- [6] Structured Outputs: The Silent Hero of Production AI. (n.d.). Decoding AI. [https://www.decodingai.com/p/llm-structured-outputs-the-only-way](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)
- [7] Structured Outputs in LLMs. (n.d.). LeewayHertz. [https://www.leewayhertz.com/structured-outputs-in-llms](https://www.leewayhertz.com/structured-outputs-in-llms)
- [8] Best practices for prompt engineering with the OpenAI API. (n.d.). OpenAI Help Center. [https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [9] Steering Large Language Models with Pydantic. (n.d.). Pydantic. [https://pydantic.dev/articles/llm-intro](https://pydantic.dev/articles/llm-intro)
- [10] Structured output. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)
- [11] Structured Outputs with OpenAI. (n.d.). OpenAI Platform. [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [12] Type safety in LangGraph: When to use Pydantic vs. TypedDict. (n.d.). Shazaali's Substack. [https://shazaali.substack.com/p/type-safety-in-langgraph-when-to](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to)
- [13] Dataclasses vs Pydantic vs TypedDict vs NamedTuple in Python. (n.d.). DEV Community. [https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg](https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg)
- [14] How to return structured data from a model. (n.d.). LangChain. [https://python.langchain.com/docs/how_to/structured_output/](https://python.langchain.com/docs/how_to/structured_output/)
- [15] Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models. (2024). arXiv. [https://arxiv.org/abs/2408.02442v1](https://arxiv.org/abs/2408.02442v1)
- [16] Function calling and structured output for LLMs. (n.d.). Baseten. [https://www.baseten.co/blog/function-calling-and-structured-output-for-llms](https://www.baseten.co/blog/function-calling-and-structured-output-for-llms)
- [17] Structured outputs in LLMs: Definition, techniques, applications, benefits. (n.d.). LeewayHertz. [https://www.leewayhertz.com/structured-outputs-in-llms](https://www.leewayhertz.com/structured-outputs-in-llms)
- [18] LLM-KG: A Large Language Model-based Approach for Knowledge Graph Construction and Completion. (n.d.). UMBC. [https://ebiquity.umbc.edu/get/a/publication/1476.pdf](https://ebiquity.umbc.edu/get/a/publication/1476.pdf)
- [19] From Chaos to Control: Mastering LLM Outputs with LangChain and Pydantic. (2024). Leo Con. [https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic](https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic)
- [20] Structured Decoding in vLLM: A Gentle Introduction. (n.d.). BentoML. [https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction)
- [21] The Complete Guide to Using Pydantic for Validating LLM Outputs. (2025). MachineLearningMastery.com. [https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs)
- [22] Introducing Structured Outputs. (n.d.). OpenAI Community. [https://community.openai.com/t/introducing-structured-outputs/896022](https://community.openai.com/t/introducing-structured-outputs/896022)
- [23] The good, the bad, and the ugly of Gemini’s structured outputs. (n.d.). Dylan Castillo. [https://dylancastillo.co/posts/gemini-structured-outputs.html](https://dylancastillo.co/posts/gemini-structured-outputs.html)