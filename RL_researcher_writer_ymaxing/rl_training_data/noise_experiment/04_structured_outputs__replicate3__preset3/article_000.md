# Lesson 4: Structured Outputs

In our previous lessons, we laid the groundwork for AI Engineering. We explored the AI agent landscape, looked at the difference between rule-based LLM workflows and autonomous AI agents, and covered context engineering: the art of feeding the right information to an LLM. In this lesson, we will tackle a fundamental challenge: getting structured and reliable information *out* of an LLM.

LLMs operate in a world of unstructured data and probabilities, where we input instructions in plain English and get results as plain text. This subdomain of engineering is often called "Software 3.0". Our application, however, relies on deterministic code and predictable data structures, which is known as "Software 1.0". Structured outputs are the bridge between these two worlds, a fundamental technique for forcing LLMs to return consistent, machine-readable data. Mastering this is essential for any AI engineer building production-grade systems.

## Understanding why structured outputs are critical

Before we start coding, it is crucial to understand why structured outputs are foundational to building reliable AI applications. When an LLM returns a free-form string, you face the messy task of parsing it. This often involves fragile regular expressions or string-splitting logic. These methods easily break if the model changes its phrasing even slightly [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/), [[2]](https://arxiv.org/html/2506.21585v1). Structured outputs solve this by forcing the model’s response into a predictable format like JSON.

This approach offers several key benefits. First, structured outputs are easy to parse, manipulate, and debug. Instead of wrestling with raw text, you work with clean Python objects like dictionaries or, even better, Pydantic models. This allows you to programmatically access the data you need without guesswork, making your code cleaner and more predictable. Second, using libraries like Pydantic adds a layer of data and type validation [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). If the LLM returns a string where an integer is expected, your application raises a clear validation error immediately. This "fail-fast" behavior is essential for building reliable systems and preventing bad data from propagating.

Structured outputs create a formal contract between the LLM and your application code. This is analogous to how traditional APIs use specifications like OpenAPI, bringing a similar predictability to the nondeterministic world of LLMs [[12]](https://tianpan.co/blog/2026-04-12-llm-output-as-api-contract-versioning-structured-responses). This makes it easier to pass data to downstream systems like databases, user interfaces, or APIs [[5]](https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs), [[6]](https://humanloop.com/blog/structured-outputs). For example, a popular use case is to extract properties like names, tags, and dates to build knowledge graphs for advanced RAG. In high-stakes domains like healthcare, this is used to extract structured data from clinical notes for diagnostics or to ensure regulatory compliance [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12189880).

However, this is not without trade-offs. Some research suggests that strict schemas can sometimes degrade an LLM's reasoning performance compared to free-form text generation [[14]](https://www.llmwatch.com/p/the-downsides-of-structured-outputs). It is a factor to consider and evaluate for your specific use case.

```mermaid
flowchart LR
  %% Input
  A["LLM Output<br/>(Unstructured or Inconsistent Text)"]

  %% Transformation Layer
  subgraph "Structured Output Layer"
    B["Parsing and Validation<br/>(Pydantic Models, JSON Schema for Data & Type Quality Checks)"]
  end

  %% Structured Output
  C["Structured Data Object<br/>(e.g., Pydantic Model, JSON)"]

  %% Downstream Consumption
  D["Downstream Processing & Applications<br/>(Data Manipulation, Transformation, Filtering Redundant Context, Integration with APIs/Databases, AI Agents, LLM Workflows)"]

  %% Main Flow
  A -- "transformed by" --> B
  B -- "produces" --> C
  C -- "consumed by" --> D

  %% Highlight the "Bridge" aspect
  note right of C: "Crucial Bridge between LLM (Software 3.0) and Python (Software 1.0) worlds, establishing a clear contract for reliable data exchange."

  %% Visual grouping
  classDef input_node stroke-width:2px,stroke-dasharray: 5 5
  classDef process_node stroke-width:2px
  classDef data_object stroke-dasharray:3,3
  classDef application_node stroke-width:2px,stroke-dasharray: 1 1

  class A input_node
  class B process_node
  class C data_object
  class D application_node
```
Image 1: A flowchart illustrating the process of transforming raw Large Language Model (LLM) output into a structured format for downstream processing.

To understand how structured outputs work in practice, we will explore three ways to implement them: from scratch with JSON, from scratch with Pydantic, and natively with the Gemini API.

## Implementing structured outputs from scratch using JSON

To understand what happens behind the scenes in modern LLM APIs, we will first implement structured outputs from scratch by prompting a model to output a JSON structure.

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 4 in the course's GitHub repository.

</aside>

Our goal is to prompt the model to return a JSON object and then parse it into a Python dictionary. We will demonstrate this by extracting key details like a summary, tags, and keywords from a financial document.

1.  We begin by setting up our environment. This involves initializing the Gemini client and defining the model we will use. For our examples, we will use `gemini-3.5-flash`, which is fast and cost-effective.

    ```python
    import json
    import re
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-3.5-flash"
    ```

    <aside>
    💡

    In all our examples, we will use Google's `google-genai` Python AI SDK to access their Gemini models. To ensure everything works correctly when running the code, please follow all the steps from the course admin lesson first.

    </aside>

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

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` and `<json>` to separate the input data from the formatting instructions. This is a common and effective prompt engineering technique to improve clarity and guide the model's output [[7]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), [[8]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/).

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

5.  To parse this, we create a helper function that uses a regular expression to find and extract the JSON object from the surrounding text. This is more robust than simple string replacement [[15]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts a JSON object from a string, cleaning up markdown code blocks.
        """
        # Find the JSON block using a regular expression
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)

        # If no JSON object is found, raise an error
        raise ValueError("No JSON object found in the response.")
    ```

6.  Finally, we parse the string into a Python dictionary, which can now be used in our application.

    ```python
    parsed_response = extract_json_from_response(response.text)
    ```

    It outputs:

    ```text
    {'summary': 'The Q3 2023 financial report highlights a strong performance with a 20% increase in revenue and 15% growth in user engagement, surpassing market expectations. This success is attributed to a robust product strategy, effective market positioning, and successful expansion into new markets, leading to improved customer retention and reduced acquisition costs.', 'tags': ['financials', 'earnings report', 'business performance', 'revenue growth', 'market expansion', 'Q3 2023'], 'keywords': ['Q3 2023', 'revenue', 'user engagement', 'market expectations', 'product strategy', 'market positioning', 'digital services', 'new markets', 'customer acquisition costs', 'retention rates', 'cash flow'], 'quarter': 'Q3 2023', 'growth_rate': '20%'}
    ```

This manual method works, but it relies on post-processing and lacks data validation. If the LLM makes a mistake, our application will fail. While JSON is common, alternatives like YAML can reduce token counts by 15-56% for the same data because they eliminate punctuation like braces and commas. For cost-sensitive applications, prompting for YAML can offer significant savings [[16]](https://tashif.codes/blog/JSON-YAML-LLM). Next, we will see how Pydantic provides a much more robust solution.

## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. Pydantic is a data validation library that solves this by enforcing structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses).

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. Common failure modes include the LLM returning a string instead of a number, omitting a required field, or using an inconsistent key name; Pydantic catches all of these [[17]](https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic). This "fail-fast" behavior is essential for building reliable systems, preventing bad data from causing hard-to-debug errors later.

1.  We define our desired data structure as a Pydantic class, using standard Python type hints. This class acts as a single source of truth for your output format. Pydantic works with Python’s `typing` module, but since Python 3.9, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`.

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

    You can also nest Pydantic models to represent more complex, hierarchical data. This helps organize your data logically. However, it is good practice to keep schemas from becoming overly complex, as this can confuse the LLM and lead to errors.

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

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard term for defining the structure and constraints of your data; think of it as a formal contract between your application and the LLM. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[9]](https://ai.google.dev/gemini-api/docs/structured-output).

    ```python
    schema = DocumentMetadata.model_json_schema()
    ```

    The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process.

    It outputs:

    ```text
    {'description': 'A class to hold structured metadata for a document.', 'properties': {'summary': {'description': 'A concise, 1-2 sentence summary of the document.', 'title': 'Summary', 'type': 'string'}, 'tags': {'description': 'A list of 3-5 high-level tags relevant to the document.', 'items': {'type': 'string'}, 'title': 'Tags', 'type': 'array'}, 'keywords': {'description': 'A list of specific keywords or concepts mentioned.', 'items': {'type': 'string'}, 'title': 'Keywords', 'type': 'array'}, 'quarter': {'description': 'The quarter of the financial year described in the document (e.g, Q3 2023).', 'title': 'Quarter', 'type': 'string'}, 'growth_rate': {'description': 'The growth rate of the company described in the document (e.g, 10%).', 'title': 'Growth Rate', 'type': 'string'}}, 'required': ['summary', 'tags', 'keywords', 'quarter', 'growth_rate'], 'title': 'DocumentMetadata', 'type': 'object'}
    ```

3.  We update our prompt to include this JSON Schema, giving the model a much more precise set of instructions.

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

    ```text
    {'summary': 'The Q3 2023 earnings report indicates strong financial performance with a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy, market expansion, and improved customer retention.', 'tags': ['Financial Performance', 'Earnings Report', 'Business Growth', 'Market Expansion', 'Customer Metrics'], 'keywords': ['Q3 2023', 'revenue increase', 'user engagement', 'digital services', 'new markets', 'customer acquisition costs', 'retention rates', 'cash flow'], 'quarter': 'Q3 2023', 'growth_rate': '20%'}
    ```

5.  Now, we can easily validate the output with Pydantic.

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

    The `document_metadata` Pydantic object can now be safely used throughout your application. You move away from unclear dictionaries to clean, predictable Python objects. If the LLM returned an incorrect data type, for example, a string for the `tags` attribute instead of a list of strings, Pydantic would have raised a `ValidationError`.

While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis tools and do not perform runtime validation [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). If the LLM returns a string where an integer is expected, these tools will not catch the error. Pydantic's runtime validation, type constraints, and clear schema definitions make it a strong option for structuring and validating data in AI applications.

A powerful pattern for production systems is to not just fail on a `ValidationError`, but to use the error message as feedback for the LLM. You can implement a retry loop where, upon validation failure, you call the LLM again with a modified prompt that includes the Pydantic error, asking it to correct its mistake. For instance: `"Previous attempt failed with error: {e}. Please fix the JSON and try again."` This self-correcting loop makes the extraction process much more resilient [[15]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

## Implementing structured outputs using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct prompts and handle responses manually. When working with modern APIs like Gemini and OpenAI, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective. Under the hood, the API uses constrained decoding, applying logit biases to mask tokens that would violate the schema, which forces compliance at the token level [[18]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction). This can add minor latency on the first request with a new schema as it gets processed and cached, but subsequent calls are fast [[20]](https://community.openai.com/t/introducing-structured-outputs/896022). However, be aware that this method can sometimes underperform on complex reasoning tasks compared to prompt-based methods. The API may also reorder schema keys alphabetically, which can break logic that depends on a specific order [[19]](https://dylancastillo.co/posts/gemini-structured-outputs.html).

Let’s see how to achieve the same result using the Gemini API's native capabilities.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.

    ```python
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
    ```

    It outputs:

    ```text
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```

This native approach is robust, efficient, and requires less code. It is the recommended way to generate structured outputs, allowing you to focus on your application's logic instead of data wrangling.

## Structured Outputs Are Everywhere

We have covered the why and how of structured outputs, from manual prompting to native API integration. This technique is a fundamental pattern in AI engineering. It is the essential bridge connecting the probabilistic, free-form nature of LLMs with the deterministic, structured world of software applications. Whether you are building a simple workflow to summarize articles or a complex agent that analyzes financial data, you will use structured outputs to ensure reliability and control.

This pattern will be a recurring theme throughout this course. In our next lesson, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between different components. Later, when we build agents that can take action (Lesson 6) or reason about the world (Lesson 7), structured outputs will be how they parse information and decide what to do next. Mastering this technique is a key step toward building powerful and predictable AI systems.

## References

- [1] Ntinopoulos, V., Biefer, H. R. C., Tudorache, I., Papadopoulos, N., Odavic, D., Risteski, P., Haeussler, A., & Dzemali, O. (2024). Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation. _BMJ Health & Care Informatics_, 32(1), e101139. https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/
- [2] (n.d.). Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops. _arXiv_. https://arxiv.org/html/2506.21585v1
- [3] Speakeasy Team. (2024, August 29). Type Safety in Python: Pydantic vs. Data Classes vs. Annotations vs. TypedDicts. _Speakeasy_. https://www.speakeasy.com/blog/pydantic-vs-dataclasses
- [4] (n.d.). Validators approach in Python - Pydantic vs. Dataclasses. _Codetain_. https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/
- [5] (n.d.). Automating Knowledge Graphs with LLM Outputs. _Prompts.ai_. https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs
- [6] Kelly, C. (2024, February 13). Structured Outputs: everything you should know. _Humanloop_. https://humanloop.com/blog/structured-outputs
- [7] (n.d.). Best practices for prompt engineering with the OpenAI API. _OpenAI Help Center_. https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api
- [8] (2024, June 26). Structured data response with Amazon Bedrock: Prompt Engineering and Tool Use. _Amazon Web Services_. https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/
- [9] (n.d.). Structured output. _Google AI for Developers_. https://ai.google.dev/gemini-api/docs/structured-output
- [10] Sharma, A. (2024, October 10). When should I use function calling, structured outputs or JSON mode? _Vellum AI Blog_. https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode
- [11] (n.d.). Structured Output in vertexAI BatchPredictionJob. _Google Cloud Community_. https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640
- [12] Pan, T. (2026, April 12). LLM Output as API Contract: Versioning Structured Responses. _Tian Pan_. https://tianpan.co/blog/2026-04-12-llm-output-as-api-contract-versioning-structured-responses
- [13] (n.d.). Applications of LLMs in Generating Clinical Notes and Improving Medical Documentation. _National Center for Biotechnology Information_. https://pmc.ncbi.nlm.nih.gov/articles/PMC12189880
- [14] Biese, P. (2024, August 9). The Downsides of Structured Outputs. _LLM Watch_. https://www.llmwatch.com/p/the-downsides-of-structured-outputs
- [15] C, B. P. (2025, December 4). The Complete Guide to Using Pydantic for Validating LLM Outputs. _MachineLearningMastery.com_. https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs
- [16] Khan, T. A. (2025, October 15). YAML Over JSON in Large Language Model Applications. _Tashif.codes_. https://tashif.codes/blog/JSON-YAML-LLM
- [17] Connor, L. (2024, November 11). From Chaos to Control: Mastering LLM Outputs with LangChain and Pydantic. _Leo Connor's Blog_. https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic
- [18] (n.d.). Structured Decoding in vLLM: A Gentle Introduction. _BentoML_. https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction
- [19] Castillo, D. (n.d.). The good, the bad, and the ugly of Gemini’s structured outputs. _Dylan Castillo_. https://dylancastillo.co/posts/gemini-structured-outputs.html
- [20] (n.d.). Introducing Structured Outputs. _OpenAI Community_. https://community.openai.com/t/introducing-structured-outputs/896022