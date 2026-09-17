# Lesson 4: Structured Outputs

In our previous lessons, we laid the groundwork for AI Engineering. We explored the AI agent landscape, looked at the difference between rule-based LLM workflows and autonomous AI agents, and covered context engineering: the art of feeding the right information to an LLM. In this lesson, we will tackle a fundamental challenge: getting structured and reliable information *out* of an LLM.

LLMs operate in a world of unstructured data and probabilities, where we input instructions in plain English and get results as plain text. This subdomain of engineering is often called "Software 3.0". Our application, however, relies on deterministic code and predictable data structures, which is known as "Software 1.0". Structured outputs are the bridge between these two worlds, a fundamental technique for forcing LLMs to return consistent, machine-readable data. Mastering this is essential for any AI engineer building production-grade systems.

## Understanding why structured outputs are critical

Before we start coding, it is crucial to understand why structured outputs are foundational to building reliable AI applications. When an LLM returns a free-form string, you face the messy task of parsing it. This often involves fragile regular expressions or string-splitting logic that can easily break if the model changes its phrasing even slightly [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/), [[26]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). Structured outputs solve this by forcing the model’s response into a predictable format like JSON.

This approach offers several key benefits. First, structured outputs are easy to parse and manipulate. Instead of wrestling with raw text, you work with clean Python objects, making your code more predictable and easier to debug. Second, using libraries like Pydantic adds a layer of data and type validation [[6]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs). If the LLM returns a string where an integer is expected, your application raises a clear validation error immediately, preventing bad data from propagating. This "fail-fast" behavior is essential for building reliable systems.

However, this reliability can come with a trade-off. Research suggests that forcing LLMs into strict formats like JSON or XML can degrade their reasoning abilities compared to free-form text [[41]](https://arxiv.org/abs/2408.02442v1). This is a key consideration: while structured outputs give you control, they might constrain performance on complex tasks.

Structured outputs create a formal contract between the LLM and your application code, much like an OpenAPI specification defines a contract for a traditional web API [[42]](https://tianpan.co/blog/2026-04-12-llm-output-as-api-contract-versioning-structured-responses). This makes the entire system more verifiable and auditable [[43]](https://www.leewayhertz.com/structured-outputs-in-llms). This makes it easier to orchestrate steps in a workflow, passing data to the next LLM call or a downstream system like a database or API [[1]](https://www.decodingai.com/p/llm-structured-outputs-the-only-way). For example, a common use case is extracting entities like names, tags, and dates from text to build knowledge graphs for advanced RAG.

```mermaid
flowchart LR
  %% Source of unstructured data
  LLM["LLM (Software 3.0)<br/>Messy strings, Uncontrolled outputs"]

  %% The critical bridge for structured data
  SO["Structured Outputs<br/>(JSON/Pydantic)<br/>Easy parsing, Data validation, Guardrails"]

  %% Downstream environment
  subgraph PythonApplication["Python (Software 1.0) Application"]
    DP["Downstream Processing<br/>Manipulation, Transformation, Filtering"]
  end

  %% Data flow
  LLM -- "generates unpredictable text" --> SO
  SO -- "provides reliable, structured data" --> DP

  %% Visual grouping
  classDef source stroke-dasharray:3,3
  classDef process stroke-width:2px
  class LLM source
  class SO,DP process
```
Image 1: A flowchart illustrating the critical role of structured outputs in formatting LLM output for downstream processing.

To see how this works in practice, we will explore three methods for implementing structured outputs: from scratch with JSON, from scratch with Pydantic, and natively with the Gemini API.

## Implementing structured outputs from scratch using JSON

To understand what modern LLM APIs offer, we will first implement structured outputs from scratch by guiding an LLM to generate a JSON object. This hands-on approach builds intuition about the underlying mechanics.

While JSON is common, formats like YAML are often more token-efficient. JSON’s syntax (braces, quotes, commas) is verbose for tokenizers. YAML, using indentation, eliminates much of this, saving 15-50% on tokens [[44]](https://tashif.codes/blog/JSON-YAML-LLM). This can lead to significant cost savings at scale. We will start with JSON as it is universally supported and a great foundation for the core concepts.

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 4 in the course's GitHub repository.

</aside>

Our goal is to prompt a model to return a JSON object containing metadata extracted from a financial document, then parse it into a Python dictionary.

1.  First, we set up our environment by initializing the Gemini client and defining the model we will use. For this example, we will use `gemini-3.5-flash`, which is fast and cost-effective.
    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-3.5-flash"
    ```

2.  Next, we define a sample document for the LLM to analyze.
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

3.  We craft a prompt that instructs the LLM to extract metadata and format it as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` and `<json>` to separate the input data from the formatting instructions. This is an effective prompt engineering technique for improving clarity and guiding the model’s output [[7]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/).
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

4.  We send the prompt to the model and inspect the raw response.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    ```
    As expected, the model returns a JSON object, but it is often wrapped in Markdown code blocks:
    ```
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

5.  To handle this, we create a helper function to strip the Markdown tags, leaving a clean JSON string that can be safely parsed.
    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
    
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
    
        return json.loads(response)
    ```

6.  Finally, we parse the string into a Python dictionary.
    ```python
    parsed_response = extract_json_from_response(response.text)
    ```
    The `parsed_response` object can now be used in our application:
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

This manual method works, but it relies on post-processing and lacks data validation. If the LLM makes a mistake, our application will fail. Next, we will see how Pydantic provides a much more robust solution.

## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. Pydantic is a data validation library that solves this by enforcing structure and type hints at runtime [[8]](https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation). It provides a single source of truth for your data structure and can automatically generate a JSON Schema from your Python class.

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This "fail-fast" behavior is essential for building reliable systems, preventing bad data from causing hard-to-debug errors later. This is a major improvement over simple JSON parsing, as it introduces a validation layer that catches errors early.

Let's refactor our previous example to use Pydantic.

1.  We define our desired data structure as a Pydantic class, using standard Python type hints. Pydantic works with Python’s `typing` module, but since Python 3.9, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`.
    We have modified the `DocumentMetadata` model to showcase more of Pydantic’s power. We changed `growth_rate` to `growth_rate_percent` and its type to `int`, adding constraints using `Field` to ensure the value is between 0 and 1000 [[6]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs). We also added a `sentiment` field using `Literal` from Python's `typing` module, which restricts the output to one of the predefined string values [[45]](https://dev.to/klement_gunndu/stop-parsing-json-by-hand-structured-llm-outputs-with-pydantic-1pg0). This is perfect for categorical data.
    ```python
    from pydantic import BaseModel, Field
    from typing import Literal
    
    class DocumentMetadata(BaseModel):
        """A class to hold structured metadata for a document."""
    
        summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
        tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
        keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
        quarter: str = Field(description="The quarter of the financial year described in the document (e.g, Q3 2023).")
        sentiment: Literal["positive", "neutral", "negative"] = Field(description="The overall sentiment of the document.")
        growth_rate_percent: int = Field(
            description="The growth rate of the company as an integer (e.g., 20 for 20%).",
            ge=0, # greater than or equal to 0
            le=1000, # less than or equal to 1000
        )
    ```
    You can also nest Pydantic models to represent more complex, hierarchical data, but it is good practice to keep schemas as simple as possible. Complex nested structures can confuse the LLM and lead to errors [[16]](https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24).
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

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM [[1]](https://www.decodingai.com/p/llm-structured-outputs-the-only-way). This technique is similar to what APIs like Gemini and OpenAI use internally to enforce a specific output format [[9]](https://pydantic.dev/articles/llm-intro), [[22]](https://ai.google.dev/gemini-api/docs/structured-output). Internally, this is often done via constrained decoding. At each step, the model calculates probabilities (logits) for every possible next token. To enforce a schema, a logit mask is applied, setting the probability of any invalid token to zero [[46]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction). This forces the model to only generate tokens that are valid at that point in the structure, ensuring compliance.
    ```python
    schema = DocumentMetadata.model_json_schema()
    ```
    The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process:
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
      'sentiment': {'description': 'The overall sentiment of the document.',
       'enum': ['positive', 'neutral', 'negative'],
       'title': 'Sentiment',
       'type': 'string'},
      'growth_rate_percent': {'description': 'The growth rate of the company as an integer (e.g., 20 for 20%).',
       'le': 1000,
       'ge': 0,
       'title': 'Growth Rate Percent',
       'type': 'integer'}},
     'required': ['summary',
      'tags',
      'keywords',
      'quarter',
      'sentiment',
      'growth_rate_percent'],
     'title': 'DocumentMetadata',
     'type': 'object'}
    ```

3.  We update our prompt to include this JSON Schema.
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
      "sentiment": "positive",
      "growth_rate_percent": 20
    }
    ```

5.  Now, we can load the output dictionary into our Pydantic model and validate it.
    ```python
    try:
        document_metadata = DocumentMetadata.model_validate(parsed_response)
        print("\nValidation successful!")
    except Exception as e:
        print(f"\nValidation failed: {e}")
    ```
    It outputs:
    ```
    Validation successful!
    ```
    The `document_metadata` object can now be safely used throughout your application. This is the main advantage: you move from unclear dictionaries to clean, predictable Python objects.

While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis and do not perform runtime validation [[36]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to), [[37]](https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg). If the LLM returns a string where an integer is expected, these tools will not catch the error. Pydantic’s runtime validation, type constraints, and clear schema definitions make it our favorite way for structuring and validating domain data in AI apps.

## Implementing structured outputs using Gemini and Pydantic

While our manual approach with Pydantic adds validation, modern APIs like Gemini and OpenAI offer native features for structured outputs. This method is simpler, more accurate, and often more cost-effective, as the vendor handles optimizations better than manual prompting [[22]](https://ai.google.dev/gemini-api/docs/structured-output), [[31]](https://ai.google.dev/gemini-api/docs/structured-output), [[32]](https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6).

However, there are trade-offs to consider. The first API call with a new schema may have higher latency as the service processes and caches it for future use [[47]](https://community.openai.com/t/introducing-structured-outputs/896022). More importantly, some studies show that this constrained decoding can degrade performance on complex reasoning tasks [[48]](https://dylancastillo.co/posts/gemini-structured-outputs.html). Be aware that Gemini's SDK has also been observed to reorder keys in the output schema alphabetically, which can break chain-of-thought logic if your schema relies on a specific field order (e.g., `reasoning` before `answer`).

Let’s see how to achieve the same result using the Gemini API’s native capabilities.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.
    ```python
    from google.genai import types

    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes our prompt significantly shorter and cleaner, as the output format is guided directly by the config.
    ```python
    prompt = f"""
    Analyze the following document and extract its metadata.
    
    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

3.  Now, we call the model, passing our simplified prompt and the new configuration object. The API handles the rest.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
    ```

4.  The Gemini client automatically parses the output. By accessing the `response.parsed` attribute, we receive a ready-to-use instance of our `DocumentMetadata` Pydantic model.
    ```python
    document_metadata = response.parsed
    print(f"Type of the response: `{type(response.parsed)}`")
    ```
    It outputs:
    ```
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```
This native approach is robust, efficient, and requires less code. While it is the recommended way for most modern APIs, the "from scratch" method remains useful for open-source models. For those, libraries like `Instructor` or `Outlines` can provide similar schema-enforcing capabilities [[49]](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms).

## Structured Outputs Are Everywhere

We have covered the why and how of structured outputs, from manual prompting to native API integration. This technique is a fundamental pattern in AI engineering, connecting the probabilistic nature of LLMs with deterministic software. In high-stakes fields like healthcare, it is used to extract clinical data from notes or ensure regulatory compliance documents adhere to a strict format [[50]](https://ebiquity.umbc.edu/get/a/publication/1476.pdf). Whether you are building a simple summarization workflow or a complex research agent, you will use structured outputs to ensure reliability and control.

This pattern will be a recurring theme throughout this course. In our next lesson, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between different components. Later, when we build agents that can take action or reason about the world, structured outputs will be how they parse information and decide what to do next. Mastering this technique is a key step toward building powerful and predictable AI systems.

## References

- [1] Structured Outputs: The Silent Hero of Production AI. (n.d.). Decoding AI. https://www.decodingai.com/p/llm-structured-outputs-the-only-way
- [2] Ntinopoulos, V., Biefer, H. R. C., Tudorache, I., Papadopoulos, N., Odavic, D., Risteski, P., Haeussler, A., & Dzemali, O. (2024). Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation. BMJ Health & Care Informatics, 32(1), e101139. https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/
- [3] Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops. (n.d.). arXiv. https://arxiv.org/html/2506.21585v1
- [4] Speakeasy Team. (2024, August 29). Type Safety in Python: Pydantic vs. Data Classes vs. Annotations vs. TypedDicts. Speakeasy. https://www.speakeasy.com/blog/pydantic-vs-dataclasses
- [5] (n.d.). Validators approach in Python - Pydantic vs. Dataclasses. Codetain. https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/
- [6] The Complete Guide to Using Pydantic for Validating LLM Outputs. (n.d.). Machine Learning Mastery. https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs
- [7] (2024, June 26). Structured data response with Amazon Bedrock: Prompt Engineering and Tool Use. Amazon Web Services. https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/
- [8] How to Keep LLM Outputs Predictable Using Pydantic Validation. (n.d.). freeCodeCamp.org. https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation
- [9] Liu, J. (2024, January 4). Steering Large Language Models with Pydantic. Pydantic. https://pydantic.dev/articles/llm-intro
- [10] Structured Outputs with Pydantic & OpenAI Function Calling. (2024, May 16). YouTube. https://www.youtube.com/watch?v=NGEZsqEUpC0
- [11] Structured Outputs with OpenAI. (n.d.). OpenAI Platform. https://platform.openai.com/docs/guides/structured-outputs
- [12] How to return structured data from a model. (n.d.). LangChain. https://python.langchain.com/docs/how_to/structured_output/
- [13] YAML vs. JSON: Which Is More Efficient for Language Models? (2023, July 17). Better Programming. https://betterprogramming.pub/yaml-vs-json-which-is-more-efficient-for-language-models-5bc11dd0f6df
- [14] Sharma, A. (2024, October 10). When should I use function calling, structured outputs or JSON mode? Vellum AI Blog. https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode
- [15] (n.d.). Structured Output in vertexAI BatchPredictionJob. Google Cloud Community. https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640
- [16] Going Deeper with Pydantic: Nested Models and Data Structures. (n.d.). DEV Community. https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24
- [17] Issue 128: Structured LLM Outputs. (n.d.). mlpills.substack.com. https://mlpills.substack.com/p/issue-128-structured-llm-outputs
- [18] Nested Models for Complex Data Structures. (n.d.). CodeSignal. https://codesignal.com/learn/courses/working-with-data-models-in-fastapi/lessons/nested-models-for-complex-data-structures
- [19] Models. (n.d.). Pydantic. https://pydantic.dev/docs/validation/latest/concepts/models
- [20] The Complete Guide to Using Pydantic for Validating LLM Outputs. (n.d.). Machine Learning Mastery. https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs
- [21] Output. (n.d.). Pydantic. https://pydantic.dev/docs/ai/core-concepts/output
- [22] Structured output. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/structured-output
- [23] Gemini 2.0 - use a list of Pydantic objects at response schema. (n.d.). Google AI/ML Developer Community. https://discuss.ai.google.dev/t/gemini-2-0-use-a-list-of-pydantic-objects-at-response-schema/55935
- [24] Control the generated output. (n.d.). Google Cloud. https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output
- [25] Structured Output for StateGraph. (n.d.). LangChain Community. https://forum.langchain.com/t/structured-output-for-stategraph/2725
- [26] LLM structured output in 2026 - stop parsing JSON with regex and do it right. (n.d.). DEV Community. https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk
- [27] The Guide to Structured Outputs and Function Calling with LLMs. (n.g.). Agenta. https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms
- [28] Structured Outputs in LLMs: A Comprehensive Guide. (n.d.). LeewayHertz. https://www.leewayhertz.com/structured-outputs-in-llms
- [29] If you use regex and string splits to parse your LLM outputs, read this... (n.d.). LinkedIn. https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP
- [30] LLM Output Parsing and Structured Generation. (n.d.). Tetrate. https://tetrate.io/learn/ai/llm-output-parsing-structured-generation
- [31] Structured output. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/structured-output
- [32] Structured Output with Gemini Models: Begging, Borrowing, and JSON-ing. (n.d.). Medium. https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6
- [33] The Guide to Structured Outputs and Function Calling with LLMs. (n.g.). Agenta. https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms
- [34] Gemini Structured Outputs. (n.d.). dylancastillo.co. https://dylancastillo.co/posts/gemini-structured-outputs.html
- [35] Structured Output Comparison: Popular LLM Providers. (n.d.). glukhov.org. https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers
- [36] Type Safety in LangGraph: When to Use Pydantic vs TypedDict. (n.d.). shazaali.substack.com. https://shazaali.substack.com/p/type-safety-in-langgraph-when-to
- [37] Dataclasses vs Pydantic vs TypedDict vs NamedTuple in Python. (n.d.). DEV Community. https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg
- [38] TypedDict vs Pydantic. (n.d.). Packet Coders. https://www.packetcoders.io/typeddict-vs-pydantic
- [39] Pydantic vs Dataclasses: Which Excels at Python Data Validation? (n.d.). Software Logic. https://softwarelogic.co/en/blog/pydantic-vs-dataclasses-which-excels-at-python-data-validation
- [40] Pydantic vs. Data Classes vs. Annotations vs. TypedDicts. (n.d.). Speakeasy. https://www.speakeasy.com/blog/pydantic-vs-dataclasses
- [41] Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models. (2024). arXiv. https://arxiv.org/abs/2408.02442v1
- [42] Tian, P. (2026, April 12). LLM Output as API Contract: Versioning Structured Responses. Tianpan.co. https://tianpan.co/blog/2026-04-12-llm-output-as-api-contract-versioning-structured-responses
- [43] Structured outputs in LLMs: Definition, techniques, applications, benefits. (n.d.). LeewayHertz. https://www.leewayhertz.com/structured-outputs-in-llms
- [44] Khan, T. A. (2025, October 15). YAML Over JSON in Large Language Model Applications. Tashif.codes. https://tashif.codes/blog/JSON-YAML-LLM
- [45] Stop Parsing JSON By Hand: Structured LLM Outputs with Pydantic. (n.d.). DEV Community. https://dev.to/klement_gunndu/stop-parsing-json-by-hand-structured-llm-outputs-with-pydantic-1pg0
- [46] Structured Decoding in vLLM: A Gentle Introduction. (n.d.). BentoML. https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction
- [47] Introducing Structured Outputs. (2024). OpenAI Community. https://community.openai.com/t/introducing-structured-outputs/896022
- [48] Castillo, D. (n.d.). The good, the bad, and the ugly of Gemini’s structured outputs. Dylan Castillo. https://dylancastillo.co/posts/gemini-structured-outputs.html
- [49] The guide to structured outputs and function calling with LLMs. (2025, September 10). Agenta. https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms
- [50] An LLM-based Knowledge Graph approach for Automated Medical Device Regulatory Compliance. (n.d.). UMBC. https://ebiquity.umbc.edu/get/a/publication/1476.pdf