In our previous lessons, we laid the groundwork for AI Engineering. We explored the AI agent landscape, looked at the difference between rule-based LLM workflows and autonomous AI agents, and covered context engineering: the art of feeding the right information to an LLM. In this lesson, we will tackle a fundamental challenge: getting structured and reliable information *out* of an LLM.

LLMs operate in a world of unstructured data and probabilities, where we input instructions in plain English and get results as plain text. This subdomain of engineering is often called "Software 3.0". Our application, however, relies on deterministic code and predictable data structures, which is known as "Software 1.0". Structured outputs are the bridge between these two worlds, a fundamental technique for forcing LLMs to return consistent, machine-readable data. Mastering this is essential for any AI engineer building production-grade systems.

## Understanding why structured outputs are critical

Before we start coding, it is important to understand why structured outputs are foundational to building reliable AI applications. When an LLM returns a free-form string, you face the messy task of parsing it. This often involves fragile regular expressions or string-splitting logic. These methods easily break if the model changes its phrasing even slightly [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/), [[2]](https://arxiv.org/html/2506.21585v1). Structured outputs solve this by forcing the model’s response into a predictable format like JSON.

This approach offers several key benefits. First, structured outputs are easy to parse, manipulate, and debug. Instead of wrestling with raw text, you work with clean Python objects like dictionaries or, even better, Pydantic models. This allows you to programmatically access the data you need without guesswork.

Second, using libraries like Pydantic adds a layer of data and type validation [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). If the LLM returns a string where an integer is expected, your application will not crash silently down the line. Instead, it will raise a clear validation error immediately. This "fail-fast" behavior is essential for building reliable systems.

Structured outputs create a formal contract between the LLM and your application code. The analogy to traditional API contracts, like OpenAPI, is strong. Just as an API contract guarantees a response shape, a structured output schema prevents the LLM's variability from breaking downstream systems [[12]](https://tianpan.co/blog/2026-04-12-llm-output-as-api-contract-versioning-structured-responses). This pattern is used everywhere to pass the right information to the next LLM step or to downstream systems like databases or APIs. For example, a popular use case is to extract entities like names and dates to build knowledge graphs, which are used in advanced systems that can reason over your private data [[5]](https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs), [[6]](https://humanloop.com/blog/structured-outputs).

```mermaid
flowchart LR
  %% Input Stage
  LLM_Output["LLM Output<br/>(Messy, Unpredictable Text)"]

  %% Pydantic Validation Layer
  subgraph "Pydantic Validation Layer"
    JSON_Extract["JSON Extraction"]
    Schema_Validate["Schema Validation"]
    Custom_Validate["Custom Validators"]

    JSON_Extract -- "extracted JSON" --> Schema_Validate
    Schema_Validate -- "validated data" --> Custom_Validate
  end

  %% Output Stage
  Structured_Data["Reliable Structured Data<br/>(Quality, Type-Safe)"]

  %% Downstream Usage
  App_Integration["Application Integration"]
  Downstream_Process["Downstream Processing"]

  %% Primary Data Flows
  LLM_Output -- "unstructured input" --> JSON_Extract
  Custom_Validate -- "structured output" --> Structured_Data

  Structured_Data -- "feeds into" --> App_Integration
  Structured_Data -- "enables" --> Downstream_Process

  %% Emphasize the bridge aspect
  %% Reliable Structured Data acts as a bridge between LLM (Software 3.0) and Python (Software 1.0) worlds,
  %% ensuring data quality, type safety, and ease of manipulation for subsequent tasks.

  %% Visual grouping (without custom colors)
  classDef input_node stroke-width:2px
  classDef process_node stroke-dasharray:3,3
  classDef output_node stroke-width:2px
  classDef usage_node stroke-dasharray:5,5

  class LLM_Output input_node
  class JSON_Extract,Schema_Validate,Custom_Validate process_node
  class Structured_Data output_node
  class App_Integration,Downstream_Process usage_node
```
Image 1: A flowchart illustrating the process of transforming unstructured LLM output into reliable, structured data using Pydantic for downstream processing and application integration.

However, this reliability can come with a trade-off. Some research suggests that strict format constraints may slightly reduce an LLM’s reasoning performance compared to free-form generation, a factor to consider in complex tasks [[13]](https://www.llmwatch.com/p/the-downsides-of-structured-outputs). To understand how structured outputs work in practice, we will explore three ways to implement them: from scratch with JSON, from scratch with Pydantic, and natively with the Gemini API.

## Implementing structured outputs from scratch using JSON

To understand what happens behind the scenes, we will first implement structured outputs from scratch by prompting the model to output JSON structures. This hands-on approach reveals the underlying mechanics and highlights the challenges that more advanced libraries and APIs are designed to solve.

<aside>
💡

You can find the code for this lesson in the notebook of Lesson 4, in the GitHub repository of the course.

</aside>

1.  We begin by setting up our environment. This involves initializing the Gemini client and defining the model we will use. For our examples, we will use `gemini-3.5-flash`, which is fast and cost-effective.
    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-3.5-flash"
    ```

2.  Next, we define a sample financial document for analysis.
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

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` and `<json>` to separate the input data from the formatting instructions. This is a common and effective prompt engineering technique that improves clarity and guides the model's output [[7]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), [[8]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/).
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

5.  To parse the generated output, we create a simple helper function to strip the Markdown and XML tags, leaving us with a clean JSON string. This step is necessary because LLMs are text generators, and they often include conversational text or formatting like Markdown around the data you requested [[14]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk).
    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts a JSON string from a response that might be wrapped in ```json markdown blocks or <json> XML tags.
        """
    
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
    
        return json.loads(response)
    ```

6.  Finally, we parse the string into a Python dictionary.
    ```python
    parsed_response = extract_json_from_response(response.text)
    ```
    It outputs:
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
This "from scratch" method demonstrates the core concept but also reveals its limitations. Relying on string manipulation and hoping for perfect JSON is not a scalable strategy for production AI systems. LLMs are probabilistic, and their text output can vary in subtle ways. A single missing comma, an unexpected newline, or a slight change in phrasing can cause your parsing logic to break [[15]](https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP).

This manual method is fragile; it relies on post-processing and lacks data validation. The LLM can make mistakes. For example, it might output a string instead of an integer, miss a key, or add an extra comma. In these cases, the `json.loads()` call will fail, or worse, your application will receive malformed data without realizing it. Next, we will see how Pydantic provides a much more robust solution to this problem.

## Implementing structured outputs from scratch using Pydantic

While forcing JSON output is an improvement, it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, if the keys are correct, or if the values have the right type. Pydantic is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses). When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. Common failure modes include type mismatches, missing required fields, or malformed nested objects. Pydantic catches all of these, preventing corrupted data from propagating through your system [[16]](https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic).

Let's refactor our previous example to use Pydantic.

1.  We define our desired data structure as a Pydantic class. This class acts as a single source of truth for your output format. Pydantic works with Python’s `typing` module, but since Python 3.9, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`.
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
    You can also nest Pydantic models to represent more complex, hierarchical data. This allows you to define intricate relationships between different pieces of information. However, it is a good practice to keep schemas from becoming overly complex, as it can confuse the LLM and lead to errors [[17]](https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24).
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

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard term for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. We provide this schema to the LLM to guide its output. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[9]](https://ai.google.dev/gemini-api/docs/structured-output).
    ```python
    schema = DocumentMetadata.model_json_schema()
    ```
    The generated schema looks like this. Notice how the `description` from the `Field` definition is present to guide the generation process.
    ```json
    {'description': 'A class to hold structured metadata for a document.',
     'properties': {'summary': {'description': 'A concise, 1-2 sentence summary of the document.',
       'title': 'Summary',
       'type': 'string'},
      'tags': {'description': 'A list of 3-5 high-level tags relevant to the document.',
       'items': {'type': 'string'},
       'title': 'Tags',
       'type': 'array'},
      'keywords': {'description': 'A list of specific keywords or concepts mentioned.',
       'items': {'type': 'string'},
       'title': 'Keywords',
       'type': 'array'},
      'quarter': {'description': 'The quarter of the financial year described in the document (e.g, Q3 2023).',
       'title': 'Quarter',
       'type': 'string'},
      'growth_rate': {'description': 'The growth rate of the company described in the document (e.g, 10%).',
       'title': 'Growth Rate',
       'type': 'string'}},
     'required': ['summary', 'tags', 'keywords', 'quarter', 'growth_rate'],
     'title': 'DocumentMetadata',
     'type': 'object'}
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

4.  Now we call the model and extract the JSON string, as in the previous example.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    
    parsed_response = extract_json_from_response(response.text)
    ```
    It outputs:
    ```json
    {
      "summary": "The Q3 2023 earnings report indicates strong financial performance with a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy, market expansion, and improved customer retention.",
      "tags": [
        "Financial Performance",
        "Earnings Report",
        "Business Growth",
        "Market Expansion",
        "Customer Metrics"
      ],
      "keywords": [
        "Q3 2023",
        "revenue increase",
        "user engagement",
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

5.  Finally, we validate and parse it directly into our `DocumentMetadata` object.
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
    The `document_metadata` Pydantic object can now be safely used throughout your application. This is the main advantage: you move away from unclear dictionaries to clean, predictable Python objects. If the LLM returned an incorrect type or missed a field, Pydantic would have raised a `ValidationError`. For production systems, you can build on this by creating a retry loop. If a `ValidationError` occurs, you can automatically send another request to the LLM, including the specific error message in the new prompt. This feedback helps the model correct its mistake on the next attempt. For example, a prompt could be augmented with: `"Previous attempt failed with error: {e}. Please fix the format and try again."` This self-correcting pattern makes your application more resilient to occasional LLM errors [[18]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

The core idea is to use Pydantic objects directly in your downstream components. This eliminates obscure Python dictionaries where you do not know what is inside, forcing you to pollute your code with `if-else` statements to check for missing keys or incorrect types. With Pydantic, the data contract is enforced at the entry point, leading to cleaner and more maintainable code.

Python’s built-in `dataclasses` or `TypedDict` can define structure, but they only provide type hints for static analysis tools [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). They do not perform runtime validation. This means if the LLM returns a string where an integer is expected, or if a required field is missing, a `dataclass` or `TypedDict` will not catch this error immediately. A type mismatch will go unnoticed until it causes an error during execution, potentially leading to difficult-to-debug issues later. While `TypedDict` can be faster for simple cases without validation, Pydantic's overhead is minimal for the robust data integrity it provides [[19]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to), [[20]](https://www.packetcoders.io/typeddict-vs-pydantic).

## Implementing structured outputs using Gemini and Pydantic

When working with modern APIs like Gemini and OpenAI, the recommended way to generate structured outputs is by leveraging their native features. This approach is simpler, more accurate, and often more cost-effective than manual prompt engineering, as the vendor handles the optimization [[9]](https://ai.google.dev/gemini-api/docs/structured-output), [[10]](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode), [[11]](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640). This increased accuracy comes from a technique called constrained decoding. The API uses the provided schema to apply logit biases during token generation, permitting only tokens that conform to the required format and preventing syntax errors [[21]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction).

Let’s see how to achieve the same result using the Gemini API's native capabilities.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.
    ```python
    from google.genai import types
    
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes our prompt significantly shorter and cleaner, eliminating the need to manually inject schemas.
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
    print(f"Type of the response: `{type(response.parsed)}`")
    ```
    It outputs:
    ```text
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```
This native approach is robust, efficient, and requires less code. However, it has trade-offs. The first API call with a new schema may have higher latency as the service caches it [[22]](https://community.openai.com/t/introducing-structured-outputs/896022). Also, be aware that some benchmarks show heavily constrained decoding can be sensitive to implementation details like the ordering of keys in the schema [[23]](https://dylancastillo.co/posts/gemini-structured-outputs.html).

## Structured Outputs Are Everywhere

We have covered the why and how of structured outputs, from manual prompting to native API integration. This technique is a fundamental pattern in AI engineering, connecting the probabilistic nature of LLMs with the deterministic world of software. Whether you are building a simple summarization workflow or a complex research agent, you will use structured outputs to ensure reliability and control. This pattern is used everywhere, from extracting clinical notes in medicine to ensuring regulatory compliance [[24]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12189880), [[25]](https://ebiquity.umbc.edu/get/a/publication/1476.pdf).

This pattern will be a recurring theme throughout this course. In our next lesson, Lesson 5, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between components. Later, when we build agents that can take action in Lesson 6, structured outputs will be how they parse information and decide what to do next. Mastering this technique is a key step toward building powerful and predictable AI systems.

## References

- [1] https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/
- [2] https://arxiv.org/html/2506.21585v1
- [3] https://www.speakeasy.com/blog/pydantic-vs-dataclasses
- [4] https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/
- [5] https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs
- [6] https://humanloop.com/blog/structured-outputs
- [7] https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api
- [8] https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/
- [9] https://ai.google.dev/gemini-api/docs/structured-output
- [10] https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode
- [11] https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640
- [12] https://tianpan.co/blog/2026-04-12-llm-output-as-api-contract-versioning-structured-responses
- [13] https://www.llmwatch.com/p/the-downsides-of-structured-outputs
- [14] https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk
- [15] https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP
- [16] https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic
- [17] https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24
- [18] https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs
- [19] https://shazaali.substack.com/p/type-safety-in-langgraph-when-to
- [20] https://www.packetcoders.io/typeddict-vs-pydantic
- [21] https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction
- [22] https://community.openai.com/t/introducing-structured-outputs/896022
- [23] https://dylancastillo.co/posts/gemini-structured-outputs.html
- [24] https://pmc.ncbi.nlm.nih.gov/articles/PMC12189880
- [25] https://ebiquity.umbc.edu/get/a/publication/1476.pdf