# Lesson 4: Structured Outputs

In our previous lessons, we laid the groundwork for AI Engineering. We explored the AI agent landscape, looked at the difference between rule-based LLM workflows and autonomous AI agents, and covered context engineering: the art of feeding the right information to an LLM. In this lesson, we will tackle a fundamental challenge: getting structured and reliable information *out* of an LLM.

LLMs operate in a world of unstructured data and probabilities, where we input instructions in plain English and get results as plain text. This subdomain of engineering is often called "Software 3.0". Our application, however, relies on deterministic code and predictable data structures, which is known as "Software 1.0". Structured outputs are the bridge between these two worlds, a fundamental technique for forcing LLMs to return consistent, machine-readable data. Mastering this is essential for any AI engineer building production-grade systems.

## Understanding why structured outputs are critical

Before we start coding, it is important to understand why structured outputs are foundational to building reliable AI applications. When an LLM returns a free-form string, you face the messy task of parsing it. This often involves fragile regular expressions or string-splitting logic—a modern parallel to the brittle CSS selectors of traditional web scraping—that can easily break if the model changes its phrasing even slightly [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/), [[2]](https://arxiv.org/html/2506.21585v1), [[12]](https://bytetunnels.com/posts/llm-powered-data-extraction-schema-driven-scraping-with-structured-output). Structured outputs solve this by forcing the model’s response into a predictable format like JSON, often via constrained decoding, a process that guides the model at the token level to ensure its output is always syntactically correct [[13]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). The reliability gain is substantial; OpenAI reported accuracy jumping from around 36% with prompt engineering to 100% with native support [[14]](https://humanloop.com/blog/structured-outputs).

This approach offers several key benefits. First, structured outputs are easy to parse and manipulate. Instead of wrestling with raw text, you work with clean Python objects, making your code more predictable and easier to debug. Using libraries like Pydantic adds a layer of data and type validation [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). If the LLM returns a string where an integer is expected, your application raises a clear validation error immediately, preventing bad data from propagating.

Structured outputs create a formal contract between the LLM and your application code. This makes it easier to pass data between steps in a workflow or to downstream systems like a database or API [[5]](https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs), [[6]](https://humanloop.com/blog/structured-outputs). For example, you can extract entities like names and dates to build knowledge graphs for advanced RAG. This precision is especially important in regulated fields like finance, healthcare, and legal services, where consistency and auditability are non-negotiable [[15]](https://www.leewayhertz.com/structured-outputs-in-llms).

```mermaid
flowchart LR
    subgraph "Software 3.0"
        A(("LLMs"))
    end
    
    subgraph "Software 1.0"
        B(("Code"))
    end
    
    A -->|"Unstructured Output"| B
    B -->|"Structured Input"| A
```

Image 1: The goal of structured outputs is to fill in the gap between Software 3.0 (LLM workflows & AI Agents) and Software 1.0 (Traditional Applications).

To understand how structured outputs work in practice, we will explore three ways to implement them: from scratch with JSON, from scratch with Pydantic, and natively with the Gemini API.

## Implementing structured outputs from scratch using JSON

To understand how modern LLM APIs work under the hood, we will first implement structured outputs from scratch. This often feels like a negotiation with the model, where we find ourselves politely asking, or even demanding, that it return data in the correct format [[16]](https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6). Our goal is to prompt a model to return a JSON object and then parse it into a Python dictionary. We will use a simple example of extracting metadata from a financial document.

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 4, in the GitHub repository of the course.

</aside>

1.  First, we set up our environment by initializing the Gemini client and defining the model we will use, `gemini-3.5-flash`, which is fast and cost-effective.

    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-3.5-flash"
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

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` and `<json>` to separate inputs from instructions. This is an effective prompt engineering technique for improving clarity and guiding the model’s output [[7]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), [[8]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/).

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

4.  We send the prompt to the model and inspect the raw response. As expected, the model returns a JSON object, often wrapped in Markdown code blocks.

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

6.  Finally, we parse the string into a Python dictionary, which can now be used in our application.

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

This manual method works, but it is brittle. It relies on post-processing and lacks data validation. The model can still suffer from schema drift (adding or renaming keys) or type inconsistency (returning a string for a number) [[17]](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation). If the LLM makes a mistake, our application will fail, potentially with a `JSONDecodeError` for malformed syntax or, more subtly, with bad data that passes the parser but violates our expectations [[18]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs). Next, we will see how Pydantic provides a much more robust solution.

## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. This uncertainty can lead to bugs and make your code difficult to maintain.

Pydantic solves this problem. It is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses). Pydantic also performs automatic type coercion where possible; for instance, it can convert a string like "123" into an integer 123, which is helpful when dealing with LLM outputs that might confuse types [[19]](https://zenvanriel.com/ai-engineer-blog/pydantic-ai-validation). It provides a single, clear definition for your data structure and can automatically generate a JSON Schema from your Python class. When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This “fail-fast” behavior is essential for building reliable systems, preventing bad data from moving through your application and causing hard-to-debug errors later.

1.  We define our desired data structure as a Pydantic class, using standard Python type hints to define the expected type for each field. Pydantic works with Python’s `typing` module, but since Python 3.9, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`.

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

    You can also nest Pydantic models to represent more complex, hierarchical data. However, it is good practice to keep schemas as simple as possible, as complex nested structures can confuse the LLM, lead to errors, and increase latency—a phenomenon sometimes called the "schema complexity tax" [[13]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). Here is an example:

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

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[9]](https://ai.google.dev/gemini-api/docs/structured-output).

    ```python
    schema = DocumentMetadata.model_json_schema()
    ```

    The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process.

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
        "growth_rate": "20%"
      }
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

This approach is powerful, but be aware of common pitfalls. LLMs sometimes struggle to return empty lists, often hallucinating data to avoid it; explicitly instructing the model in the field description to return an empty list if no data is found can help mitigate this "empty array trap" [[13]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). Also, be mindful that structured output does not bypass token limits. If the model's output is truncated, it will result in invalid JSON [[13]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk).

The `document_metadata` Pydantic object can now be safely used throughout your application. This is the main advantage: you move from unclear dictionaries to clean, predictable Python objects. While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis and do not perform runtime validation [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). For example, a dataclass would accept a string for an integer field at runtime, leading to errors later [[20]](https://pydantic.dev/articles/llm-intro). Pydantic’s runtime validation, type constraints, and clear schema definitions make it our favorite way for structuring and validating domain data structures from our AI apps.

## Implementing structured outputs using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually. When working with modern APIs such as Gemini and OpenAI, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective than manual prompt engineering, as the vendor will always handle the optimization on top of their models better than your manual prompting [[9]](https://ai.google.dev/gemini-api/docs/structured-output), [[10]](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode), [[11]](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640). Companies like Alkimi AI use this to automate the configuration of AI assistants, and it has led to significant cost savings in data extraction for platforms like Agentic Users [[21]](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs). However, it is not a silver bullet; some research suggests that for certain tasks, constrained decoding can underperform carefully prompted natural language outputs, so testing is key [[22]](https://dylancastillo.co/posts/gemini-structured-outputs.html).

Let’s see how to achieve the same result using the Gemini API’s native capabilities. The process becomes much simpler.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.

    ```python
    from google.genai import types
    
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes our prompt significantly shorter and cleaner, eliminating the need to manually inject any type of schema. We simply ask the model to perform the task, as the output format is guided directly by the config.

    ```python
    prompt = f"""
    Analyze the following document and extract its metadata.
    
    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

3.  Now, we call the model, passing our simplified prompt and the new configuration object. The API handles the rest, ensuring the output adheres to the schema.

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

This native approach is robust, efficient, and requires less code. While it is the recommended way for closed-source APIs or AI frameworks, the “from scratch” method remains useful for open-source models that may not have this built-in functionality.

## Structured Outputs Are Everywhere

Structured outputs are a fundamental pattern in AI engineering, connecting the probabilistic nature of LLMs with the deterministic world of software. Whether you are building a simple summarization workflow or a complex research agent, you will use structured outputs to ensure reliability and control.

This pattern will be a recurring theme throughout this course. In our next lesson, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between different components. Later, when we build agents that can take action or reason about the world, structured outputs will be how they parse information and decide what to do next. This is distinct from, but related to, function calling, which we will cover in Lesson 6 [[9]](https://ai.google.dev/gemini-api/docs/structured-output). This pattern is so fundamental that it is becoming the basis for standardized agent communication protocols, enabling different AI systems to interact reliably [[23]](https://arxiv.org/html/2504.16736v2). Mastering this technique is a key step toward building powerful and predictable AI systems.

## References

- [1] Ntinopoulos, V., Biefer, H. R. C., Tudorache, I., Papadopoulos, N., Odavic, D., Risteski, P., Haeussler, A., & Dzemali, O. (2024). Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation. *BMJ Health & Care Informatics*, 32(1), e101139. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/)
- [2] (n.d.). Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops. *arXiv*. [https://arxiv.org/html/2506.21585v1](https://arxiv.org/html/2506.21585v1)
- [3] Speakeasy Team. (2024, August 29). Type Safety in Python: Pydantic vs. Data Classes vs. Annotations vs. TypedDicts. *Speakeasy*. [https://www.speakeasy.com/blog/pydantic-vs-dataclasses](https://www.speakeasy.com/blog/pydantic-vs-dataclasses)
- [4] (n.d.). Validators approach in Python - Pydantic vs. Dataclasses. *Codetain*. [https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/)
- [5] (n.d.). Automating Knowledge Graphs with LLM Outputs. *Prompts.ai*. [https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs](https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs)
- [6] Kelly, C. (2024, February 13). Structured Outputs: everything you should know. *Humanloop*. [https://humanloop.com/blog/structured-outputs](https://humanloop.com/blog/structured-outputs)
- [7] (n.d.). Best practices for prompt engineering with the OpenAI API. *OpenAI Help Center*. [https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [8] (2024, June 26). Structured data response with Amazon Bedrock: Prompt Engineering and Tool Use. *Amazon Web Services*. [https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/)
- [9] (n.d.). Structured output. *Google AI for Developers*. [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)
- [10] Sharma, A. (2024, October 10). When should I use function calling, structured outputs or JSON mode? *Vellum AI Blog*. [https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode)
- [11] (n.d.). Structured Output in vertexAI BatchPredictionJob. *Google Cloud Community*. [https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640)
- [12] (n.d.). Schema-Driven LLM Data Extraction. *Byte Tunnels*. [https://bytetunnels.com/posts/llm-powered-data-extraction-schema-driven-scraping-with-structured-output](https://bytetunnels.com/posts/llm-powered-data-extraction-schema-driven-scraping-with-structured-output)
- [13] Gunn, D. K. (2026, May 14). LLM Structured Output in 2026: Stop parsing JSON with regex and do it right. *DEV Community*. [https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk)
- [14] Kelly, C. (2024, February 13). Structured Outputs: everything you should know. *Humanloop*. [https://humanloop.com/blog/structured-outputs](https://humanloop.com/blog/structured-outputs)
- [15] (n.d.). Structured Outputs in LLMs: How to Get Reliable, Consistent and Formatted Outputs. *LeewayHertz*. [https://www.leewayhertz.com/structured-outputs-in-llms](https://www.leewayhertz.com/structured-outputs-in-llms)
- [16] Terracciano, S. (2025, April 8). Structured Output with Gemini Models: Begging, Threatening, and JSON-ing. *Medium*. [https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6](https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6)
- [17] (n.d.). LLM Output Parsing: Why Structured Generation is a Game-Changer. *Tetrate*. [https://tetrate.io/learn/ai/llm-output-parsing-structured-generation/](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation/)
- [18] Brown, J. (2025, December 2). The Complete Guide to Using Pydantic for Validating LLM Outputs. *MachineLearningMastery.com*. [https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs/](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs/)
- [19] van Riel, Z. (n.d.). Pydantic for AI Validation - Type Safety for LLM Applications. *Zen van Riel*. [https://zenvanriel.com/ai-engineer-blog/pydantic-ai-validation](https://zenvanriel.com/ai-engineer-blog/pydantic-ai-validation)
- [20] Liu, J. (n.d.). Steering Large Language Models with Pydantic. *Pydantic*. [https://pydantic.dev/articles/llm-intro](https://pydantic.dev/articles/llm-intro)
- [21] (n.d.). Expanded JSON Schema support in the Gemini API. *Google*. [https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs/](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs/)
- [22] Castillo, D. (n.d.). Gemini’s Structured Outputs Don’t Improve Performance. *Dylan Castillo*. [https://dylancastillo.co/posts/gemini-structured-outputs.html](https://dylancastillo.co/posts/gemini-structured-outputs.html)
- [23] (n.d.). Agora: A Multi-Protocol Communication Framework for LLM Agents. *arXiv*. [https://arxiv.org/html/2504.16736v2](https://arxiv.org/html/2504.16736v2)