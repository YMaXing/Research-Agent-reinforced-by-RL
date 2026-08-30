# Near-tie review: 04_structured_outputs  (deep vs standard, margin=+0.0000)


## Reviewer conclusion (2026-08-26): KEEP `deep`, no override

**Quantitative basis** (see "All sections" table below): the two highest-weighted
contrarian sections (3, 6) pull against `deep` by a combined −0.0359, but three
other sections (1, 4, 5) pull for `deep` by +0.0373, netting an almost-exact tie
(+0.0000). Sections 3 and 6 were reviewed and confirmed accurately and
consistently graded across all 3 draws — `deep` genuinely contains fewer
depth/breadth enhancement instances than `standard` there, so their negative
contribution is a real content property, not a grading artifact.

**Qualitative basis (new):** sections 4 ("Implementing structured outputs from
scratch using JSON" — Pydantic-based structured parsing) and 5 ("Implementing
structured outputs using Gemini's native structured output support") are the
article's most practically important content — the actual production-relevant
techniques a reader would use — more so than their word-count weight (0.400 +
0.133 = 0.533 combined) alone conveys. These are also exactly the two sections
where `deep` wins over `standard`. This reinforces `deep` as the right pick
independent of the statistical margin being razor-thin.

**Decision:** no manual override needed — `deep` already is mean-R_w's own
winner. `needs_review=True` is left as-is in `article_oracle.json` (it reflects
an objective, reproducible statistical fact about the margin, not review
status); this note is the durable record that the article has been
human-reviewed and the pick confirmed.

---


## All sections (deep vs standard), most-against-deep first
| section | weight | contribution | running total |
|---|---:|---:|---:|
| section-3-implementing-structured-outputs-from-scr | 0.200 | -0.0274 | -0.0274 |
| section-6-conclusion-structured-outputs-are-everyw | 0.067 | -0.0085 | -0.0359 |
| section-2-understanding-why-structured-outputs-are | 0.133 | -0.0014 | -0.0373 |
| lesson-code | 0.000 | +0.0000 | -0.0373 |
| section-1-introduction | 0.067 | +0.0040 | -0.0333 |
| section-4-implementing-structured-outputs-from-scr | 0.400 | +0.0163 | -0.0169 |
| section-5-implementing-structured-outputs-using-ge | 0.133 | +0.0170 | +0.0000 |

(stored article margin = +0.0000 -- should match the running total's final row to ~4 decimals)

## Section: S3::section-3-implementing-structured-outputs-from-scratch-using-json  (weight=0.200, contribution=-0.0274 AGAINST deep)
Stored section rewards: deep=0.3324  standard=0.5056  (explore: deep=0.0350  standard=0.1620)

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset3`

**Article text:**
```
## Implementing structured outputs from scratch using JSON

To understand what happens behind the scenes in modern LLM APIs, you will first implement structured outputs from scratch by prompting a model to return a JSON object. You will then parse it into a Python dictionary. This hands-on approach builds a strong intuition for the challenges involved and highlights why more robust methods are necessary for production systems. Our example will involve extracting key details like a summary and tags from a financial document.

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 4, located in the course's GitHub repository.

</aside>

1.  First, you set up your environment by initializing the Gemini client and defining which model to use. We will use `gemini-1.5-flash`, which is fast and cost-effective for our examples.
    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-1.5-flash"
    ```
    <aside>
    💡
    
    In all our examples, we will use Google's official `google-genai` Python AI SDK to access their Gemini models. For more information, you can consult their [getting started guides](https://ai.google.dev/gemini-api/docs) or [SDK docs](https://googleapis.github.io/python-genai/index.html). Please ensure you have completed the setup steps from the course admin lesson before running the code.
    
    </aside>

2.  Next, you define a sample document for analysis. This represents a typical piece of unstructured text that an AI system might encounter in a business context, such as an internal report or a news article.
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

3.  You then craft a prompt that instructs the LLM to extract metadata and format it as JSON. The prompt explicitly defines the desired structure with an example, which is a key technique in prompt engineering. We also use XML tags like `<document>` and `<json>` to create clear boundaries for the model, which helps it distinguish between instructions, input data, and the desired output format. This separation is critical for improving the reliability of the model's response [[6]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), [[7]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/).
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

4.  Next, you send the prompt to the model.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    ```

5.  The raw output is a string that often includes Markdown formatting, a common artifact since many models are trained on internet data where code is presented this way.
    It outputs:
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

6.  Because LLMs return probabilistic text, not guaranteed data structures, you need to clean the output before parsing. This helper function strips the Markdown and XML tags, leaving a clean JSON string. While this function handles common cases, it is a simple and brittle solution; a slight change in the LLM's output format, like adding an introductory sentence, could break it [[13]](https://python.plainenglish.io/getting-structured-json-responses-from-llms-a-simple-solution-f819fc389ebc).
    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
    
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
    
        return json.loads(response)
    ```

7.  You then use this function to parse the string into a Python dictionary.
    ```python
    parsed_response = extract_json_from_response(response.text)
    ```

8.  The resulting dictionary can now be used in your application. This is a standard Python object, which is useful but lacks the safety and clarity of typed data structures.
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

This manual method works for simple cases, but it relies on post-processing and lacks data validation. If the LLM makes a mistake, like outputting a string instead of an integer or missing a key, your application will fail at runtime. This is not a scalable way to build production AI systems [[14]](https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP). Next, you will see how Pydantic provides a much more robust solution to this problem.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Both sections walk through the same underlying content using the same artifacts: the DOCUMENT text, the prompt structure with XML tags, the extract_json_from_response function, and the parsed Python dictionary output. The generated section uses 8 numbered steps and adds explanatory commentary about WHY LLMs produce Markdown, the brittleness of the helper function, and the non-scalability of the approach. All core content is present.
- `fl`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Neither section contains images or diagrams. Both use an aside callout box followed by numbered steps with code blocks. The generated section has a second aside box within step 1 for SDK documentation, but this does not affect media placement. Flow matches.
- `de`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] Three candidate depth additions were examined and all fail the source-attribution gate. (1) The claim that Markdown code blocks are 'a common artifact since many models are trained on internet data' has no supporting exploration-phase source. (2) The characterization of the helper function as 'a simple and brittle solution' traces to python.plainenglish.io, which is an exploitation-phase source. (3) The statement 'This is not a scalable way to build production AI systems' traces to the LinkedIn/pauliusztin source, also exploitation-phase. No instance can be traced to an exploration-phase source.
- `be`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] No breadth additions. All examined candidates were either untraceable or pure depth within the implementation domain.
- `cp`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The depth additions are integrated within individual step descriptions without shortening any core notebook content. The aside box in step 1 is additive. All eight conceptual points are present and complete. Core preserved.
- `ga`: Implementing structured outputs from scratch using JSON:
**1:** All eight guideline-specified concepts are present: (1) client and MODEL_ID setup, (2) the DOCUMENT text, (3) prompt with XML tags explained, (4) model call, (5) raw output shown, (6) extract_json_from_response function explained, (7) extraction call, (8) final parsed output shown. Both aside callout boxes are present. The added Markdown-artifact explanation, brittleness note, and 'not scalable' transition are acceptable exploration-phase complementary content. Prose-only word count is approximately 491 words, within the 405–495 tolerance band (target 450 ± 45).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset3`

**Article text:**
```
## Implementing structured outputs from scratch using JSON

To build an intuition for what modern LLM APIs offer, we will first implement structured outputs from scratch. Our goal is to prompt a model to return a JSON object and then parse it into a Python dictionary. This hands-on approach reveals the underlying mechanics and challenges that more advanced libraries and APIs abstract away. We will demonstrate this by extracting key details from a financial document.

Because LLMs are probabilistic text generators, they do not "understand" JSON syntax in the way a compiler does. They are simply predicting the next most likely token. This means that even with clear instructions, they can make small mistakes like adding an extra comma, forgetting a quote, or wrapping the JSON in explanatory text. These minor deviations will break standard JSON parsers, making this "from scratch" method inherently fragile. The helper functions we will write are necessary but brittle workarounds for this unpredictability, highlighting why this approach is not recommended for production systems where reliability is paramount.

<aside>
💡

You can find the code for this lesson in the accompanying notebook on our GitHub repository.

</aside>

1.  We begin by setting up our environment and initializing the Gemini client. For our examples, we will use `gemini-1.5-flash`. This model is part of Google's Gemini family and is optimized for speed and cost-efficiency, making it a good choice for tasks like data extraction where rapid responses are valuable.

    ```python
    import json
    from google import genai
    from utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])

    client = genai.Client()
    MODEL_ID = "gemini-1.5-flash"
    ```

2.  Next, we define a sample document for analysis. This text will serve as the unstructured input that we want to convert into a structured format.

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

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` and `<json>` to separate inputs from instructions. This technique helps the model distinguish between the content it needs to analyze and the formatting rules it must follow, which is a common and effective prompt engineering practice [[8]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api).

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

4.  We send the prompt to the model. The model processes the text and generates a response that attempts to follow our JSON formatting instructions.

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

5.  LLMs often wrap JSON in Markdown code blocks (```json ... ```) because they are trained on vast amounts of text from the internet, including documentation where code is presented this way. To handle this, we create a helper function to strip these tags, leaving a clean JSON string.

    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
        return json.loads(response)
    ```

6.  Finally, we parse the string into a Python dictionary. This dictionary can now be used programmatically in our application, allowing us to access specific fields like `summary` or `tags`.

    ```python
    parsed_response = extract_json_from_response(response.text)
    ```

    It outputs:

    ```json
    {'summary': 'The Q3 2023 financial report highlights a strong performance with a 20% increase in revenue and 15% growth in user engagement, surpassing market expectations. This success is attributed to a robust product strategy, effective market positioning, and successful expansion into new markets, leading to improved customer retention and reduced acquisition costs.', 'tags': ['financials', 'earnings report', 'business performance', 'revenue growth', 'market expansion', 'Q3 2023'], 'keywords': ['Q3 2023', 'revenue', 'user engagement', 'market expectations', 'product strategy', 'market positioning', 'digital services', 'new markets', 'customer acquisition costs', 'retention rates', 'cash flow'], 'quarter': 'Q3 2023', 'growth_rate': '20%'}
    ```

This manual method works, but it relies on post-processing and lacks data validation. If the LLM makes a mistake, like outputting a string instead of an integer, our application will fail. Next, we will see how Pydantic provides a much more robust solution.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Every step from the expected section is present with matching substance: client/MODEL_ID setup, the sample financial DOCUMENT, the XML-tagged prompt, calling the model and inspecting the raw response, the extract_json_from_response helper, and parsing into a final dictionary. The expected section's second aside is absent, but per the standing note on untraceable GT-only content, this has no basis in the guideline or research.md and is not held against the section.
- `fl`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The generated section follows the same progression, and the closing transition into Pydantic is present and equivalent. The missing second aside is not counted per the untraceable-content standing note.
- `de`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] No depth additions traceable to an exploration-phase source were identified in this section specifically (the opening elaboration on why LLMs mis-format JSON is plausible but generic, without a specific verifiable source match).
- `be`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] No breadth additions identified in this section.
- `cp`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so core_preservation scores 1 by default.
- `ga`: Implementing structured outputs from scratch using JSON:
**1:** All eight guideline steps are present in order. Prose-only word count is 477 words against a 450-word target (+/-45 tolerance, range 405-495), within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset3`

**Article text:**
```
## Implementing structured outputs from scratch using JSON

To understand what modern LLM APIs offer, we will first implement structured outputs from scratch by guiding an LLM to generate a JSON object. This hands-on approach builds intuition about the underlying mechanics.

While JSON is common, formats like YAML are often more token-efficient. JSON’s syntax (braces, quotes, commas) is verbose for tokenizers. YAML, using indentation, eliminates much of this, saving 15-50% on tokens [[8]](https://tashif.codes/blog/JSON-YAML-LLM). This can lead to significant cost savings at scale. We will start with JSON as it is universally supported and a great foundation for the core concepts.

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 4 in the course's GitHub repository.

</aside>

Our goal is to prompt the model to return a JSON object containing metadata extracted from a financial document, then parse it into a Python dictionary.

1.  First, we set up our environment by initializing the Gemini client from the `google-genai` package and defining the model we will use. The `google-genai` library provides a straightforward interface to Google's AI models. For this example, we will use `gemini-3.5-flash`, a model optimized for speed and cost-effectiveness, making it ideal for tasks like simple data extraction where rapid responses are valued over deep, complex reasoning.
    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-3.5-flash"
    ```

2.  Next, we define a sample document for the LLM to analyze. This financial performance analysis is a good example because it contains a mix of qualitative statements and specific quantitative data (percentages, quarters), which is a common scenario for structured data extraction.
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

3.  We craft a prompt that instructs the LLM to extract metadata and format it as JSON. We use XML tags like `<document>` and `<json>` to create clear boundaries that the model can easily distinguish, reducing ambiguity between instructions and raw data [[9]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/). Providing a concrete example of the JSON structure also acts as a one-shot example, guiding the model to replicate the format precisely. This explicit instruction is crucial because, without it, the model might generate a natural language summary or a differently structured JSON.
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

4.  We send the prompt to the model using the `generate_content` method and inspect the raw response. This method sends the prompt to the specified model and returns a response object containing the generated text.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    ```
    It outputs:
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

5.  To handle this, we create a helper function to strip the Markdown tags and XML wrappers. This function uses simple string replacement to clean the output, leaving a pure JSON string that can be safely parsed. While simple, this approach is fragile. If the model's output format changes—for instance, by adding a preamble like "Here is the JSON you requested:"—our string replacement logic will fail. This highlights the need for more robust parsing and validation.
    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
    
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
    
        return json.loads(response)
    ```

6.  Finally, we parse the string into a Python dictionary. This `parsed_response` object can now be used in our application, allowing us to access data programmatically, for example, `parsed_response['summary']`. While a dictionary is a flexible data structure, it offers no guarantees about its contents. A missing key or an incorrect data type will only be discovered at runtime, potentially causing unexpected errors.
    ```python
    parsed_response = extract_json_from_response(response.text)
    ```
    The `parsed_response` object now holds the structured data:
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

This manual method works, but it relies on post-processing and lacks data validation. The `extract_json_from_response` function is fragile; if the LLM changes its output format even slightly, our string replacement logic will fail. Furthermore, if the model makes a mistake inside the JSON, such as outputting a string instead of an integer, our application will not catch the error until it causes a problem downstream. Next, we will see how Pydantic provides a much more robust solution.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Every step from the expected section is present with matching substance: client/MODEL_ID setup, the sample financial DOCUMENT, the XML-tagged prompt, calling the model and inspecting the raw response, the extract_json_from_response helper, and parsing into a final dictionary. The second aside is absent, but per the standing note on untraceable GT-only content, this is not held against the section.
- `fl`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The generated section follows the same progression, and the closing transition into Pydantic is present and equivalent. The added YAML-efficiency digression at the section's opening does not disrupt the walkthrough that follows. The missing second aside is not counted per the untraceable-content standing note.
- `de`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] No depth additions identified in this section specifically; the qualifying addition here (YAML token efficiency) connects outward to an adjacent format/technology rather than deepening the JSON-from-scratch topic itself, so it is credited under breadth instead.
- `be`: Implementing Structured Outputs From Scratch Using JSON:
**1:** [instances=1; quality=strong] The claim that YAML 'saving 15-50% on tokens' compared to JSON matches an exploration-tagged source almost exactly ('YAML often reduces token usage by 15-56% compared to JSON'), verified directly. This is a 'cross-domain... enabling technology that intersects with the core topic' -- comparing to an adjacent serialization format -- and is classified strong given the specific, quantified figure that closely matches the source.
- `cp`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The qualifying breadth addition is a short opening digression before the walkthrough begins; the section's core JSON-from-scratch content remains the clearly dominant focus.
- `ga`: Implementing structured outputs from scratch using JSON:
**0:** All eight guideline steps are present and the YAML digression is closely related, not off-topic. However, prose-only word count is approximately 592 words against a 450-word target (+/-45 tolerance, range 405-495) -- 97 words over the upper bound, well beyond the tolerance band (about double the band's own width past the boundary), a clear and decisive overage.

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset2`

**Article text:**
```
## Implementing structured outputs from scratch using JSON

To understand what happens behind the scenes in modern LLM APIs, we will first implement structured outputs from scratch by prompting the model to output JSON. Our goal is to extract key details from a financial document. This hands-on approach helps build an intuition for the challenges that more advanced tools are designed to solve.

This method relies entirely on prompt engineering and manual parsing. While it offers maximum control, it is also the most fragile. The LLM is not programmatically constrained and can deviate from the requested format. You are responsible for anticipating and handling these inconsistencies in your application code. This process highlights why native structured output features, which we will cover later, are so valuable for production systems.

<aside>
💡

You can find the code for this lesson in the notebook of Lesson 4, in the GitHub repository of the course.

</aside>

1.  First, we define our Gemini client and the model ID. We will use `gemini-1.5-flash`, which is fast and cost-effective.
    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-1.5-flash"
    ```

2.  Next, we define the sample document for analysis.
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

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. This prompt uses several key techniques. We explicitly state that the output must be a single, valid JSON object. We provide a clear example of the desired structure, including keys and example value types. Finally, we use XML tags like `<document>` and `<json>` to separate the input data from the formatting instructions. This helps the model distinguish between content and commands, improving the reliability of the output [[4]](https://www.leewayhertz.com/structured-outputs-in-llms).
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

4.  We send the prompt to the model.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    ```

5.  The model returns a text response. A common failure mode is that LLMs often wrap the JSON in Markdown code blocks or add conversational text like "Sure, here is the JSON you requested:" [[43]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk).
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

6.  To handle this, we create a helper function to strip these extra characters, leaving a clean JSON string. This post-processing step is a necessary defense against the unpredictable nature of raw LLM text generation. It makes the output programmatically parsable, but it's a reactive measure, not a preventative one.
    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
    
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
    
        return json.loads(response)
    ```

7.  We can now reliably parse the JSON string into a Python dictionary.
    ```python
    parsed_response = extract_json_from_response(response.text)
    ```

8.  The final `parsed_response` is a dictionary that can be used in our application.
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

This manual method works, but it relies on post-processing and lacks robust data validation. If the LLM returns a malformed string, the `json.loads` call will raise a `JSONDecodeError` [[41]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs). Even if the JSON is syntactically valid, there are no guarantees about its contents. Next, we will see how Pydantic provides a much more robust solution.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Both sections walk through the same underlying content: the DOCUMENT text, the prompt structure with XML tags, the extract_json_from_response function, and the parsed Python dictionary output. The generated section uses 8 numbered steps (vs GT's 6), adds failure mode commentary, and a more explicit transition. All core content is present.
- `fl`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Neither section contains images or diagrams. Both use an aside callout followed by numbered steps with code blocks. Flow matches.
- `de`: Implementing Structured Outputs From Scratch Using JSON:
**1:** [instances=2; quality=standard,standard] Two depth additions remain after dropping the untraceable 'reactive measure, not preventative' characterization. (1) Explicit naming of the Markdown-wrapping / conversational-text failure mode ('Sure, here is the JSON you requested') — traces to exploration material (dev.to-related). (2) Explicit JSONDecodeError as a failure mode of json.loads — traces to machinelearningmastery exploration material. Both qualify as technical failure modes of the from-scratch JSON approach.
- `be`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] No breadth additions. All remaining additions are depth content within the same implementation domain.
- `cp`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The depth additions (failure mode in step 5, 'reactive measure' commentary in step 6, JSONDecodeError in the transition) enrich individual steps without shortening or replacing any core notebook content. All 8 conceptual points remain complete. Core preserved.
- `ga`: Implementing structured outputs from scratch using JSON:
**1:** All eight guideline-specified concepts are present: (1) client and MODEL_ID setup, (2) the DOCUMENT text, (3) prompt with XML tags explained, (4) model call, (5) raw output shown, (6) extract_json_from_response function explained, (7) extraction call, (8) final parsed output shown. The aside callout is present. The added failure mode commentary and JSONDecodeError transition note are acceptable as complementary exploration-phase content closely related to the section's core subject. Prose-only word count is approximately 421 words, within the 405–495 tolerance band (target 450 ± 45).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset2`

**Article text:**
```
## Implementing structured outputs from scratch using JSON

To understand what happens behind the scenes in modern LLM APIs, we will first implement structured outputs from scratch. Our goal is to prompt the model to return a JSON object and then parse it into a Python dictionary. We will demonstrate this by extracting key details from a financial document.

<aside>
💡

You can find the code of this lesson in the notebook of Lesson 4, in the GitHub repository of the course.

</aside>

### Setting Up the Environment

1.  We begin by setting up our environment. This involves initializing the Gemini client from the `google-genai` package and defining the model we will use. For this example, we will use `gemini-3.5-flash`, which is fast and cost-effective for tasks like simple data extraction.

    ```python
    import json
    
    from google import genai
    from utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
    client = genai.Client()
    
    MODEL_ID = "gemini-3.5-flash"
    ```

### Defining the Input Document

2.  Next, we define a sample document for analysis. This financial performance analysis is a good example because it contains specific, extractable pieces of information like percentages, quarters, and key business metrics that we want to capture in a structured format.

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

### Crafting the Prompt

3.  Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. We use two key prompt engineering techniques here. First, we provide a clear example of the desired JSON structure, including keys and example value types. This gives the model a concrete template to follow. Second, we use XML tags like `<document>` and `<json>` to clearly separate the input data from the formatting instructions. This helps the model distinguish between content and commands, improving the reliability of the output [[2]](https://www.decodingai.com/p/llm-structured-outputs-the-only-way).

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

### Calling the Model

4.  We send the prompt to the model using the `generate_content` method. The model processes the document and the instructions, generating a text response that should conform to our requested JSON format.

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

### Parsing the Response

5.  LLMs often wrap their JSON output in Markdown code blocks (e.g., ` ```json ... ``` `) or other conversational text. To handle this, we create a helper function to strip these extra characters, ensuring we are left with a clean JSON string that can be safely parsed. This post-processing step is a common necessity when not using native structured output features.

    ```python
    def extract_json_from_response(response: str) -> dict:
        """
        Extracts JSON from a response string that is wrapped in <json> or ```json tags.
        """
    
        response = response.replace("<json>", "").replace("</json>", "")
        response = response.replace("```json", "").replace("```", "")
    
        return json.loads(response)
    ```

### Using the Parsed Data

6.  Finally, we use our helper function to parse the string into a Python dictionary. This structured data can now be easily accessed and used in the rest of our application, for example, to populate a database or display on a dashboard.

    ```python
    parsed_response = extract_json_from_response(response.text)
    ```

    It outputs a dictionary that can be used programmatically:

    ```text
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
    ...
    }
    ```

This manual method works, but it is fragile. Beyond simple formatting errors, it is vulnerable to schema drift, where the model adds unexpected fields, or type inconsistency, where it returns a string instead of a number [[7]](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation). If the LLM makes a mistake, our application will fail. Next, we will see how Pydantic provides a more robust solution.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Every step from the expected section is present with matching substance: client/MODEL_ID setup, the sample financial DOCUMENT, the XML-tagged prompt, calling the model and inspecting the raw response, the extract_json_from_response helper, and parsing into a final dictionary. The expected section's second aside (google-genai SDK usage note) is absent, but per the standing note on untraceable GT-only content, this has no basis in the guideline or research.md and is not held against the section.
- `fl`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The generated section follows the same progression, and the closing transition into Pydantic is present and expanded (schema drift, type inconsistency) without disrupting the bridge to the next section. The missing second aside is not counted per the untraceable-content standing note (see core_content).
- `de`: Implementing Structured Outputs From Scratch Using JSON:
**1:** [instances=1; quality=strong] The closing paragraph's claim that the manual method 'is vulnerable to schema drift, where the model adds unexpected fields, or type inconsistency, where it returns a string instead of a number' matches an exploration-tagged source nearly verbatim ('schema drift occurs when the model decides to add helpful but unexpected fields... type inconsistency appears when the model returns strings instead of numbers'). This is 'limitations, criticisms, or failure modes of the core topic' and is classified strong: it names two specific, distinct failure modes rather than a generic caution.
- `be`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] The qualifying depth instance above stays within the core topic (this section's own JSON-parsing reliability) rather than connecting outward to an adjacent field.
- `cp`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The qualifying depth addition is a short closing note; the section's core JSON-from-scratch walkthrough remains the clearly dominant focus.
- `ga`: Implementing structured outputs from scratch using JSON:
**1:** All eight guideline steps are present in order, and the added schema-drift/type-inconsistency discussion is closely related to the section's own topic. Prose-only word count is 475 words against a 450-word target (+/-45 tolerance, range 405-495), within range. The H3 sub-headers introduced in this section are a formatting choice the guideline does not itself prescribe or forbid at this level of detail, so they are not treated as a guideline_adherence issue here (structure/formatting concerns are captured under the FollowsGT structure dimension instead).

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset2`

**Article text:**
```
## Implementing structured outputs from scratch using JSON

To understand how modern LLM APIs work under the hood, we will first implement structured outputs from scratch. This often feels like a negotiation with the model, where we find ourselves politely asking, or even demanding, that it return data in the correct format. Our goal is to prompt a model to return a JSON object and then parse it into a Python dictionary. We will use a simple example of extracting metadata from a financial document [[10]](https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6).

<aside>
💡

You can find the code for this lesson in the notebook for Lesson 4, in the GitHub repository of the course.

</aside>

### Setting Up the Environment

First, we set up our environment. We initialize the Gemini client from the `google-genai` Python package and define the model we will use. For this example, we will use `gemini-3.5-flash`, which is a fast and cost-effective choice for tasks like simple data extraction.

```python
import json

from google import genai
from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])

client = genai.Client()

MODEL_ID = "gemini-3.5-flash"
```

### Defining the Document

Next, we define a sample document for analysis. This financial report contains the kind of semi-structured text that is a perfect candidate for metadata extraction.

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

### Crafting the Prompt

Now, we craft a prompt that instructs the LLM to extract metadata and format it as JSON. The prompt explicitly defines the desired JSON structure, including keys and example value types. We also wrap the input document and the JSON example in XML tags like `<document>` and `<json>`. This technique helps the model clearly distinguish between instructions, examples, and the content to be processed, which improves the reliability of the output [[11]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), [[12]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/).

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

### Calling the Model

We send the prompt to the model using the `generate_content` method. The model processes the input and returns a response object. The actual text generated by the LLM is contained in the `text` attribute of this object.

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

### Parsing the Response

The raw output is a string that includes Markdown formatting (` ```json` and ````). To parse this, we create a helper function that uses simple string replacement to remove these artifacts, as well as the XML tags we used in the prompt, leaving a clean JSON string.

```python
def extract_json_from_response(response: str) -> dict:
    """
    Extracts JSON from a response string that is wrapped in <json> or ```json tags.
    """

    response = response.replace("<json>", "").replace("</json>", "")
    response = response.replace("```json", "").replace("```", "")

    return json.loads(response)
```

Finally, we call our helper function to parse the cleaned string into a standard Python dictionary. This dictionary can now be used by other parts of our application, for example, to populate a database or display information in a user interface.

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

This manual method works, but it is brittle. It relies on post-processing and lacks data validation. The model can still suffer from schema drift (adding or renaming keys) or type inconsistency (returning a string for a number). If the LLM makes a mistake, our application will fail, potentially with a `JSONDecodeError` for malformed syntax or, more subtly, with bad data that passes the parser but violates our expectations. Next, we will see how Pydantic provides a much more robust solution [[13]](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation), [[14]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using JSON:
**1:** Every step from the expected section is present with matching substance: client/MODEL_ID setup, the sample financial DOCUMENT, the XML-tagged prompt, calling the model and inspecting the raw response, the extract_json_from_response helper, and parsing into a final dictionary. The second aside is absent, but per the standing note on untraceable GT-only content, this is not held against the section.
- `fl`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The generated section follows the same progression, and the closing transition into Pydantic is present and expanded (schema drift, type inconsistency) without disrupting the bridge. The missing second aside is not counted per the untraceable-content standing note.
- `de`: Implementing Structured Outputs From Scratch Using JSON:
**1:** [instances=1; quality=strong] The closing claim that the manual method 'can still suffer from schema drift (adding or renaming keys) or type inconsistency (returning a string for a number)' matches an exploration-tagged source nearly verbatim, the same finding independently confirmed on a different article using this same research.md. Classified strong: it names two specific, distinct failure modes.
- `be`: Implementing Structured Outputs From Scratch Using JSON:
**0:** [instances=0] The qualifying depth instance stays within the core topic (this section's own JSON-parsing reliability) rather than connecting outward to an adjacent field.
- `cp`: Implementing Structured Outputs From Scratch Using JSON:
**1:** The qualifying depth addition is a short closing note; the section's core JSON-from-scratch walkthrough remains the clearly dominant focus.
- `ga`: Implementing structured outputs from scratch using JSON:
**1:** All eight guideline steps are present, organized under H3 sub-headers (a formatting choice captured under the FollowsGT structure dimension, not treated as a guideline_adherence issue since the guideline does not prescribe header structure at this level of detail). Prose-only word count is 472 words against a 450-word target (+/-45 tolerance, range 405-495), within range.

## Section: S6::section-6-conclusion-structured-outputs-are-everywhere  (weight=0.067, contribution=-0.0085 AGAINST deep)
Stored section rewards: deep=0.3998  standard=0.4661  (explore: deep=0.0691  standard=0.1225)

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset3`

**Article text:**
```
## Conclusion: Structured Outputs Are Everywhere

Structured outputs are everywhere. They are a fundamental pattern in AI engineering, connecting the probabilistic nature of LLMs with the deterministic world of software. Whether you are building a simple summarization workflow or a complex research agent, you will use structured outputs to ensure reliability and control. By making model outputs predictable and verifiable, this pattern is a key enabler for building auditable and trustworthy AI systems, which is essential for production-grade applications [[23]](https://www.leewayhertz.com/structured-outputs-in-llms).

This pattern will be a recurring theme throughout this course. In our next lesson, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between different components. Later, when we build agents that can take action (Lesson 6) or reason about the world (Lesson 7), structured outputs will be how they parse information and decide what to do next. Mastering this technique is a key step toward building powerful and predictable AI systems.
```
**Grader reasoning:**
- `cc`: Structured Outputs Are Everywhere:
**1:** Both sections make the same core closing arguments: fundamental pattern, bridge metaphor, recurring theme throughout course, next lesson (basic LLM workflow ingredients), Lesson 6 and 7 references, mastering key step. The generated section adds 'auditable and trustworthy AI systems' as an additional application dimension. Core content fully present.
- `fl`: Structured Outputs Are Everywhere:
**1:** Neither section contains visual elements. Both are prose-only conclusions. Flow matches.
- `de`: Structured Outputs Are Everywhere:
**1:** [instances=1; quality=standard] A depth addition is present: 'By making model outputs predictable and verifiable, this pattern is a key enabler for building auditable and trustworthy AI systems.' This adds a new application dimension (auditability / trustworthiness) beyond the GT framing. It traces to the leewayhertz.com exploration-phase source.
- `be`: Structured Outputs Are Everywhere:
**0:** [instances=0] No breadth additions. The auditable/trustworthy framing is a depth addition about a production attribute of the same core technique.
- `cp`: Structured Outputs Are Everywhere:
**1:** The auditable/trustworthy AI addition is a brief phrase within an existing sentence structure. The GT core elements are fully intact. Core preserved.
- `ga`: Conclusion: Structured Outputs Are Everywhere:
**1:** All guideline requirements are satisfied. The universality of structured outputs is emphasized, the next lesson is referenced ('In our next lesson, we will explore the basic ingredients of LLM workflows'), and Lesson 6 and Lesson 7 are explicitly cited. The 'auditable and trustworthy AI' addition is acceptable complementary content. Prose-only word count is approximately 153 words, within the 125–175 tolerance band (target 150 ± 25).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset3`

**Article text:**
```
## Conclusion: Structured Outputs Are Everywhere

We have covered the why and how of structured outputs, from manual prompting to native API integration. This technique is a fundamental pattern in AI engineering. It is the essential bridge between the free-form nature of LLMs and the structured world of software applications. Whether you are building a simple workflow to summarize articles or a complex agent that analyzes financial data, you will use structured outputs. This ensures reliability and control.

This pattern will be a recurring theme throughout this course. In our next lesson, we will explore the basic ingredients of LLM workflows, where we will see how structured data flows between different components. Later, when we build agents that can take action (Lesson 6) or reason about the world (Lesson 7), structured outputs will be how they parse information and decide what to do next. They are also essential for managing an agent's memory (Lesson 9) by structuring past experiences and for processing retrieved documents in RAG systems (Lesson 10). Mastering this technique is a key step toward building powerful and predictable AI systems.
```
**Grader reasoning:**
- `cc`: Structured Outputs Are Everywhere:
**1:** The first paragraph matches the expected section closely, including the same illustrative examples (summarization workflow; agent analyzing financial data). The second paragraph covers the same core ideas and adds four explicit lesson-number references (6, 7, 9, 10), all of which are drawn from the guideline's own future-lessons list.
- `fl`: Structured Outputs Are Everywhere:
**1:** Both paragraphs appear in the same order with the same internal progression, and neither section has media elements to place.
- `de`: Structured Outputs Are Everywhere:
**0:** [instances=0] No depth additions present; the four lesson-number references are guideline-authorized content additions, not enhancement-shaped technical or theoretical content.
- `be`: Structured Outputs Are Everywhere:
**0:** [instances=0] No breadth additions present in this section.
- `cp`: Structured Outputs Are Everywhere:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so core_preservation scores 1 by default.
- `ga`: Conclusion: Structured Outputs Are Everywhere:
**1:** Universality is covered with the same examples as the guideline's underlying framing. The next lesson's content is described accurately (though without a literal '(Lesson 5)' label, the same minor and now-familiar gap seen on every article). Four future lessons are explicitly named with lesson numbers (6, 7, 9, 10), all drawn from the guideline's own future-lessons list -- thorough compliance with the 'slight references' requirement. Prose-only word count is 177 words against a 150-word target (+/-25 tolerance, range 125-175) -- 2 words over the upper bound, a negligible near-boundary miss treated as noise.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset3`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Structured Outputs Are Everywhere:
**1:** The first paragraph covers the same core ideas as the expected section (fundamental pattern, bridge framing, illustrative examples), adding a well-grounded healthcare/regulatory example. The second paragraph matches the expected section's structure and content; unlike several other articles, this one does not add explicit lesson numbers for the 'take action or reason about the world' reference, matching the expected section's own level of specificity rather than exceeding it.
- `fl`: Structured Outputs Are Everywhere:
**1:** Both paragraphs appear in the same order with the same internal progression, and the added healthcare example does not disrupt the established order.
- `de`: Structured Outputs Are Everywhere:
**0:** [instances=0] No depth additions present; the healthcare/regulatory addition (discussed under breadth_enhancement) connects outward to another industry/domain rather than deepening the core topic itself.
- `be`: Structured Outputs Are Everywhere:
**1:** [instances=1; quality=strong] The claim that structured outputs are used 'in high-stakes fields like healthcare... to extract clinical data from notes or ensure regulatory compliance documents adhere to a strict format' matches the same exploration-tagged medical-device-regulatory-compliance paper independently confirmed on a different article using this same research.md. Classified strong given the specific, detailed source material. This is a practical application of the core topic in another industry/domain, thematically on-topic and well-grounded, so per the standing ruling on adjacent-concept forward references, it is not treated as a guideline_adherence problem either (see UserIntent scores).
- `cp`: Structured Outputs Are Everywhere:
**1:** The qualifying breadth addition is a single sentence; the section's core message about the ubiquity of structured outputs remains fully intact and dominant.
- `ga`: Conclusion: Structured Outputs Are Everywhere:
**1:** Universality is covered. The healthcare/regulatory-compliance addition is well-grounded and thematically on-topic; per the standing ruling that forward-references in this section are not limited to the guideline's explicitly named future-lesson list, this is not treated as a violation. The next lesson's content is described accurately (without a literal '(Lesson 5)' label, the familiar minor gap), and unlike several other articles this one does not add explicit Lesson 6/7 numbers for the later agent reference -- matching the expected article's own level of specificity rather than falling short of a guideline requirement, since the guideline does not mandate exhaustive lesson-numbering. Prose-only word count is 159 words against a 150-word target (+/-25 tolerance, range 125-175), within range.

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Structured Outputs Are Everywhere:
**1:** Both sections make the same core closing arguments: fundamental pattern, bridge metaphor, universality, transition to next lesson (LLM workflows), reference to agents taking action (Lesson 6). The generated section adds a function calling distinction and a multi-agent systems reference as depth additions. Core content fully present.
- `fl`: Structured Outputs Are Everywhere:
**1:** Neither section contains visual elements. Both are prose-only conclusions. Flow matches.
- `de`: Structured Outputs Are Everywhere:
**1:** [instances=1; quality=strong] One depth addition remains: the statement that structured outputs are the foundation for multi-agent systems, enabling them to communicate reliably through standardized protocols. This traces directly to the arxiv Agora paper (https://arxiv.org/html/2504.16736v2), which is under phase="exploration". (The function-calling vs structured-outputs distinction is primarily supported by the Gemini golden-source documentation and is not required once the Agora instance is present.)
- `be`: Structured Outputs Are Everywhere:
**0:** [instances=0] No breadth additions. The multi-agent systems reference remains within the AI engineering / agent-communication domain and qualifies as depth rather than cross-domain breadth.
- `cp`: Structured Outputs Are Everywhere:
**1:** The function calling distinction and multi-agent systems sentence are brief additions at the end of the second paragraph. The core GT elements (fundamental pattern, bridge metaphor, next lesson reference, Lesson 6 mention, mastering key step) are all present. Core preserved.
- `ga`: Conclusion: Structured Outputs Are Everywhere:
**1:** All guideline requirements are satisfied. The universality of structured outputs is emphasized ('This pattern is a recurring theme'), Lesson 5 is referenced as the next lesson ('In our next lesson, we will explore LLM workflows'), and Lesson 6 is referenced for agents that can take action. The function calling distinction (from Lesson 6 content) and multi-agent systems reference are acceptable as complementary additions. Prose-only word count is approximately 166 words, within the 125–175 tolerance band (target 150 ± 25).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Structured Outputs Are Everywhere:
**1:** The first paragraph covers the same ideas as the expected section, substituting the illustrative examples (summarization workflow, research agent) for the expected section's pairing -- a swap within an illustrative list, not a missing substantive idea. The second paragraph covers the same core ideas (recurring theme, next-lesson preview, later agents parsing information) and adds an explicit Lesson 6 reference plus a new closing point about multi-agent communication protocols.
- `fl`: Structured Outputs Are Everywhere:
**1:** Both paragraphs appear in the same order with the same internal progression; the new multi-agent-protocols sentence is appended at the end without disrupting the established order or the closing sentence's role.
- `de`: Structured Outputs Are Everywhere:
**0:** [instances=0] No depth additions present. The multi-agent-protocols addition (discussed under breadth_enhancement) connects outward to an adjacent research area rather than deepening the core topic itself.
- `be`: Structured Outputs Are Everywhere:
**1:** [instances=1; quality=strong] The closing claim that 'multi-agent systems... use structured data to allow agents to collaborate reliably' matches an exploration-tagged arXiv source on agent communication protocols (Agora, AITP) in detail. This is a genuine 'enabling technology that intersects with the core topic' in an adjacent research area, and is classified strong given the specific, detailed source material it draws on, even though the article's own sentence is a single compressed clause.
- `cp`: Structured Outputs Are Everywhere:
**1:** The qualifying breadth addition is a single sentence appended near the end of the section; the section's core message about the ubiquity of structured outputs remains fully intact and dominant.
- `ga`: Conclusion: Structured Outputs Are Everywhere:
**1:** Universality is covered, the next lesson's content is described accurately (though without a literal '(Lesson 5)' label, a minor and now-familiar gap), and Lesson 6 is explicitly named. Prose-only word count is 166 words against a 150-word target (+/-25 tolerance, range 125-175), within range. The closing sentence about multi-agent communication protocols (Agora, AITP) is well-grounded in research.md (see research_anchoring) and thematically on-topic (structured data enabling agent collaboration); forward-references in this section are not limited to only the guideline's explicitly named future-lesson list, so this is not treated as a violation.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Structured Outputs Are Everywhere:
**1:** The generated section drops the expected section's opening recap sentence ('We have covered the why and how of structured outputs, from manual prompting to native API integration') and its 'essential bridge' framing language, going straight to the fundamental-pattern statement instead; the overall message (bridges probabilistic LLMs and deterministic software, ensures reliability/control) is still conveyed, so this reads as a compressed restatement rather than a missing idea, but it is a more noticeable omission than the usual illustrative-example swaps seen on other articles. The second paragraph covers the same core ideas and adds a Lesson 6 reference plus a well-grounded multi-agent-protocols closing point (see breadth_enhancement).
- `fl`: Structured Outputs Are Everywhere:
**1:** Both paragraphs appear in the same order with the same internal progression; the new multi-agent-protocols sentence is appended at the end without disrupting the established order.
- `de`: Structured Outputs Are Everywhere:
**0:** [instances=0] No depth additions present; the multi-agent-protocols addition (discussed under breadth_enhancement) connects outward to an adjacent research area rather than deepening the core topic itself.
- `be`: Structured Outputs Are Everywhere:
**1:** [instances=1; quality=strong] The closing claim that structured outputs are 'becoming the basis for standardized agent communication protocols, enabling different AI systems to interact reliably' matches the same exploration-tagged arXiv source on agent communication protocols (Agora, AITP) found on a different article using this same research.md. Classified strong given the specific, detailed source material. Per the standing ruling on this exact topic, this is not penalized for guideline_adherence either (see UserIntent scores).
- `cp`: Structured Outputs Are Everywhere:
**1:** The qualifying breadth addition is a single sentence; the section's core message about the ubiquity of structured outputs remains fully intact and dominant.
- `ga`: Conclusion: Structured Outputs Are Everywhere:
**1:** Universality is covered (the dropped recap sentence discussed under core_content is not itself a guideline-mandated element -- the guideline asks for the universality emphasis and forward-references, not a specific 'here is what we covered' framing sentence). The next lesson's content is described accurately (without a literal '(Lesson 5)' label, the familiar minor gap). Lesson 6 is explicitly named. The multi-agent-protocols closing point is well-grounded and, per the standing ruling on this exact topic, is not treated as out-of-scope. Prose-only word count is 161 words against a 150-word target (+/-25 tolerance, range 125-175), within range.

## Section: S5::section-5-implementing-structured-outputs-using-gemini-and-pydantic  (weight=0.133, contribution=+0.0170 FOR deep)
Stored section rewards: deep=0.5685  standard=0.4506  (explore: deep=0.3045  standard=0.1736)

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset3`

**Article text:**
```
## Implementing structured outputs using Gemini and Pydantic

So far, you have constructed prompts manually. However, modern APIs like Gemini and OpenAI offer native features for structured outputs. This approach is simpler, more accurate, and more cost-effective, as vendors optimize these features for their own models [[8]](https://ai.google.dev/gemini-api/docs/structured-output), [[9]](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode), [[10]](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640).

Using native support is more accurate because it relies on constrained decoding directly within the model's generation process, rather than just prompt-based guidance. It is often cheaper because the vendor can optimize token usage for their specific features. The process also becomes much simpler, as it reduces the amount of code needed for prompt engineering and manual parsing. This pattern is not unique to Gemini; other providers like OpenAI and Anthropic offer similar functionalities, making it an industry standard for reliable structured data extraction [[21]](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms).

Let’s see how to achieve the same result for our example using the Gemini API's native capabilities.

1.  You define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.
    ```python
    from google.genai import types
    
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes your prompt significantly shorter and cleaner, eliminating the need to manually inject any type of schema. You simply ask the model to perform the task, as the output format is guided directly by the config.
    ```python
    prompt = f"""
    Analyze the following document and extract its metadata.
    
    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

3.  Now, you call the model, passing your simplified prompt and the new configuration object. The API handles the rest, ensuring the output adheres to the schema.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
    ```

4.  The Gemini client automatically parses the output for you. By accessing the `response.parsed` attribute, you receive a ready-to-use instance of our `DocumentMetadata` Pydantic model.
    ```python
    document_metadata = response.parsed
    print(f"Type of the response: `{type(document_metadata)}`")
    ```
    It outputs:
    ```
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```
This native approach is robust and efficient. However, be aware of provider-specific behaviors. For example, some benchmarks suggest Gemini's constrained decoding is less performant on certain reasoning tasks, and its API may reorder schema keys alphabetically, which can break logic that depends on field order [[22]](https://dylancastillo.co/posts/gemini-structured-outputs.html). While it is the recommended way for closed-source APIs, the “from scratch” method remains useful for open-source models that may not have this built-in functionality.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** Both sections present the same four-step pattern: GenerateContentConfig, simplified prompt, model call, response.parsed. The generated section adds depth about constrained decoding superiority, cross-provider ubiquity, and Gemini-specific benchmarks. All four required core steps are present.
- `fl`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** Both sections use numbered steps with code blocks. Flow matches.
- `de`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** [instances=3; quality=strong,standard,strong] Three depth additions. (1) Native support is more accurate because it relies on constrained decoding inside the generation process rather than prompt guidance. (2) Cross-provider industry-standard note (OpenAI, Anthropic, etc.) — traces to agenta.ai exploration material. (3) Provider-specific caveats: Gemini constrained decoding can be less performant on certain reasoning tasks, and the API may reorder schema keys alphabetically (traces to dylancastillo.co exploration source).
- `be`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] No breadth additions. Cross-provider notes and Gemini-specific benchmarks remain inside the AI-engineering domain.
- `cp`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The four required GT steps are present and complete. The depth additions are placed before (intro) and after (closing) the core steps without shortening them. Core preserved.
- `ga`: Implementing structured outputs using Gemini and Pydantic:
**0:** The guideline specifies a section length of 300 words, with an acceptable range of 270–330 (tolerance ±30). The generated section has approximately 339 prose words, exceeding the target by 39 words — more than the tolerance. The excess is driven primarily by the additional introductory paragraph on constrained decoding, cost optimization, and cross-provider ubiquity (~75 words) and the closing trade-offs paragraph including the alphabetical key reordering issue (~70 words), both from exploration-phase research. All four required guideline steps are present and correct, but the word count failure requires a score of 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset3`

**Article text:**
```
## Implementing structured outputs using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually. When working with modern APIs such as Gemini and OpenAI, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective than manual prompt engineering, as the vendor will always handle the optimization on top of their models better than you can. Be aware that the first API call with a new schema may have higher latency as the service processes and caches it, but subsequent calls will be faster [[10]](https://ai.google.dev/gemini-api/docs/structured-output), [[14]](https://python.langchain.com/docs/how_to/structured_output/), [[22]](https://community.openai.com/t/introducing-structured-outputs/896022).

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
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** All four expected steps are present with matching substance: the GenerateContentConfig object, the shortened prompt, the model call, and response.parsed producing a ready DocumentMetadata instance. The closing paragraph covers the same 'recommended, but from-scratch remains an option' idea, reworded.
- `fl`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The section opens with the transition relocated from the end of the expected Pydantic section, reading naturally here. The four steps follow the same order as the expected section, and the added latency/key-ordering caveats are appended after the walkthrough without disrupting it.
- `de`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** [instances=2; quality=strong,standard] Two distinct qualifying instances trace to this episode's exploration-phase sources. (1) The key-reordering caveat -- Gemini alphabetizes schema keys, which can break order-dependent logic like chain-of-thought fields, with a naming workaround -- matches an exploration-tagged source ('the order of the keys in the schema gets sorted alphabetically... I resorted to a quick workaround: I named the keys...') in close detail, down to the reasoning/answer-field example. Classified strong: specific, verified, and actionable. (2) The latency/caching note ('the first API call with a new schema may have higher latency... subsequent calls will be faster') matches an exploration-tagged source on schema-complexity latency and caching closely; standard, a brief single-sentence treatment.
- `be`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] Both qualifying depth instances are technical implementation details of the core topic (Gemini's own native structured-output behavior) rather than connections to an adjacent field.
- `cp`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The two qualifying additions are appended after the four-step walkthrough and together form a meaningful but not overwhelming portion of the section; the core Gemini/Pydantic walkthrough remains the clearly dominant focus.
- `ga`: Implementing structured outputs using Gemini and Pydantic:
**1:** All four guideline steps are present and correctly explained. The latency/caching and key-reordering caveats are both closely related, well-grounded additions rather than off-topic content. Prose-only word count is 309 words against a 300-word target (+/-30 tolerance, range 270-330), within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset3`

**Article text:**
```
## Implementing structured outputs using Gemini and Pydantic

While our manual approach with Pydantic adds validation, modern APIs like Gemini and OpenAI offer native features for structured outputs. This method is simpler, more accurate, and often more cost-effective, as the vendor handles optimizations better than manual prompting [[14]](https://ai.google.dev/gemini-api/docs/structured-output), [[21]](https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6). By offloading the schema enforcement to the API, you reduce the complexity of your own code and benefit from the provider's highly optimized implementation of constrained decoding.

However, there are trade-offs to consider. The first API call with a new schema may have higher latency as the service processes and caches it for future use [[22]](https://community.openai.com/t/introducing-structured-outputs/896022). More importantly, some studies show that this constrained decoding can degrade performance on complex reasoning tasks [[23]](https://dylancastillo.co/posts/gemini-structured-outputs.html). Be aware that Gemini's SDK has also been observed to reorder keys in the output schema alphabetically, which can break chain-of-thought logic if your schema relies on a specific field order (e.g., `reasoning` before `answer`). Despite these considerations, for most data extraction and formatting tasks, the native approach is superior.

Let’s see how to achieve the same result using the Gemini API’s native capabilities.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This single configuration step replaces the manual schema injection and parsing we did earlier. The SDK uses this configuration to tell the Gemini model to generate a JSON object that conforms to the schema derived from the `DocumentMetadata` class.
    ```python
    from google.genai import types
    
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes our prompt significantly shorter and cleaner, as the output format is guided directly by the config. We no longer need to include a lengthy JSON schema or examples in the prompt itself. We can simply focus on the core task we want the model to perform.
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

4.  The Gemini client automatically parses the output. By accessing the `response.parsed` attribute, we receive a ready-to-use instance of our `DocumentMetadata` Pydantic model. This eliminates the need for custom parsing functions or manual validation steps, streamlining the entire process.
    ```python
    document_metadata = response.parsed
    print(f"Type of the response: `{type(response.parsed)}`")
    ```
    It outputs:
    ```
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```
This native approach is robust, efficient, and requires less code. While it is the recommended way for most modern APIs, the "from scratch" method remains useful for open-source models. For those, libraries like `Instructor` or `Outlines` can provide similar schema-enforcing capabilities [[24]](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms).
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** All four expected steps are present with matching substance: the GenerateContentConfig object, the shortened prompt, the model call, and response.parsed producing a ready DocumentMetadata instance. The closing paragraph covers the same 'recommended, but from-scratch remains useful' idea, extended with an Instructor/Outlines mention for open-source models.
- `fl`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The section opens with the transition relocated from the end of the expected Pydantic section, reading naturally here. The added trade-offs paragraph (latency, reasoning-performance, key-reordering) is placed before the four-step walkthrough and does not disrupt its internal order.
- `de`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** [instances=3; quality=strong,strong,standard] Three distinct qualifying instances trace to this episode's exploration-phase sources, each verified directly. (1) The claim that 'constrained decoding can degrade performance on complex reasoning tasks' specifically for Gemini matches an exploration-tagged source that discusses both the underlying reasoning-performance paper and Gemini-specific testing; strong. (2) The key-reordering caveat (Gemini alphabetizes schema keys, breaking chain-of-thought field order) matches the same exploration-tagged source's detailed, verified account of this exact issue; strong. (3) The latency/caching note ('the first API call with a new schema may have higher latency... cached for future use') matches an exploration-tagged source on schema-caching behavior; standard, a brief treatment. Note: a fourth candidate -- the Instructor/Outlines libraries mention for open-source models -- was checked directly and does not qualify, since that specific claim traces to an exploitation-tagged instance of the cited source, not its exploration-tagged instance.
- `be`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] All three qualifying depth instances are technical limitations of this section's own core topic (Gemini's native structured-output behavior) rather than connections to an adjacent field.
- `cp`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The three qualifying additions form one consolidated trade-offs paragraph (roughly a fifth of the section), placed before the four-step walkthrough; the walkthrough itself remains fully present and is still the section's clear focus, though this is the highest proportion of enhancement content relative to section length seen so far -- worth keeping an eye on rather than a clear violation.
- `ga`: Implementing structured outputs using Gemini and Pydantic:
**0:** All four guideline steps are present and correctly explained, enriched with three well-grounded caveats. However, prose-only word count is approximately 401 words against a 300-word target (+/-30 tolerance, range 270-330) -- 71 words over the upper bound, well beyond the tolerance band, a clear and decisive overage despite the strong content quality.

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset2`

**Article text:**
```
## Implementing structured outputs using Gemini and Pydantic

So far, we have implemented structured outputs from scratch. When working with modern APIs such as Gemini and OpenAI, the recommended way is to use their native features. This approach is more reliable because it uses constrained decoding, where the API programmatically forces the model to generate only tokens that conform to your JSON schema, guaranteeing a syntactically valid output [[43]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). This can improve reliability from around 36% with prompting to nearly 100% [[44]](https://humanloop.com/blog/structured-outputs).

Using the native API is also simpler, as it eliminates the need for complex prompt engineering and manual parsing logic. Furthermore, it is often more cost-effective. By removing the lengthy JSON schema from the prompt, you reduce the number of input tokens sent with each request, which can lead to significant savings at scale.

Let’s see how to achieve the same result using the Gemini API’s native capabilities. The process becomes much simpler.

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This single configuration step replaces the manual schema injection and parsing we did earlier.
    ```python
    from google.genai import types
    
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

2.  This configuration makes our prompt significantly shorter and cleaner, eliminating the need to manually inject any schema. We simply ask the model to perform the task, as the output format is guided directly by the config.
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
    print(f"Type of the response: `{type(response.parsed)}`")
    ```
    It outputs:
    ```text
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```
    And here is the final object:
    ```json
    {
      "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, exceeding market expectations due to successful product strategy and market expansion. Customer acquisition costs decreased by 10% and retention improved to 92%, indicating a strong foundation for continued growth.",
      "tags": [
        "Financial Performance",
        "Earnings Report",
        "Revenue Growth",
        "Market Expansion",
        "User Engagement"
      ],
      "keywords": [
        "Q3 2023",
        "revenue increase",
        "user engagement",
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

While robust, this approach has trade-offs. Complex schemas can increase latency due to the "schema complexity tax," and in some niche cases, may even slightly reduce semantic accuracy compared to a well-crafted prompt [[43]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk), [[45]](https://dylancastillo.co/posts/gemini-structured-outputs.html). Additionally, structured output does not bypass token limits. If your schema requires a long response but the model hits its `max_tokens` limit, you will receive a truncated, invalid JSON object. Always set `max_tokens` generously and check the `finish_reason` to handle potential truncation [[43]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). Despite these considerations, for most production systems, the reliability of native APIs makes them the recommended choice.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** Both sections present the same four-step pattern: GenerateContentConfig, simplified prompt, model call, response.parsed. The generated section adds depth content about constrained decoding with a reliability metric, cost reduction explanation, and a trade-offs closing paragraph. All four required core steps are present.
- `fl`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** Neither section contains images or diagrams. Both use numbered steps with code blocks. Flow matches.
- `de`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** [instances=4; quality=strong,strong,standard,standard] Four depth additions remain after dropping the untraceable concrete '36% → nearly 100%' reliability metric. (1) Constrained decoding mechanism (API programmatically forces only schema-conforming tokens) — present in multiple exploration sources. (2) Schema complexity tax / latency increase with complex schemas (explicitly named 'Pitfall 1: The Schema Complexity Tax' in exploration material). (3) Token-limit truncation risk and the need to check finish_reason — present in exploration material. (4) Cost reduction from removing the lengthy JSON schema from the prompt (supported by exploration discussion of prompt vs. native config). The dropped 36% metric had no textual support in research.md.
- `be`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] No breadth additions. Constrained decoding, schema complexity tax, truncation handling, and cost reduction are all technical depth about the same native API approach.
- `cp`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The four required GT steps are present and complete. The depth additions (constrained decoding intro, cost reduction, trade-offs closing paragraph) are placed before and after the core steps without shortening them. Core preserved.
- `ga`: Implementing structured outputs using Gemini and Pydantic:
**0:** The guideline specifies a section length of 300 words (prose only, excluding code), with an acceptable range of 270–330 words (tolerance ±30). The generated section has approximately 368 prose words, exceeding the target by 68 words — more than double the tolerance. The excess is driven primarily by (1) the introductory constrained decoding / reliability metric paragraph (~60 words), (2) the cost reduction sentence and context (~40 words), and (3) the closing trade-offs paragraph (~90 words), all from exploration-phase research. All four required guideline steps are present and correct, but the word count failure alone requires a score of 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset2`

**Article text:**
```
## Implementing structured outputs using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually. When working with modern APIs like Gemini, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective, with some providers claiming a jump in reliability from ~36% to nearly 100% compared to prompt engineering alone [[9]](https://ai.google.dev/gemini-api/docs/structured-output), [[11]](https://humanloop.com/blog/structured-outputs).

Let’s see how to achieve the same result using the Gemini API’s native capabilities.

### Configuring the Gemini API

1.  We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This single configuration step replaces the manual schema injection and parsing we did earlier. The SDK uses this configuration to internally construct the appropriate prompt and ensures the model's output is constrained to the provided schema. This not only simplifies the code but also leverages the provider's internal optimizations for structured data generation, which are typically more efficient than manual prompting.

    ```python
    from google.genai import types
    
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
    ```

### Simplifying the Prompt

2.  This configuration makes our prompt significantly shorter and cleaner. We simply ask the model to perform the task, as the output format is guided directly by the config. This separation of concerns—content in the prompt, format in the configuration—makes the code more maintainable and easier to read.

    ```python
    prompt = f"""
    Analyze the following document and extract its metadata.
    
    Here is the document:
    <document>
    {DOCUMENT}
    </document>
    """
    ```

### Calling the Model

3.  Now, we call the model, passing our simplified prompt and the new configuration object. The API handles the rest, ensuring the output adheres to the schema.

    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
    ```

### Accessing the Parsed Output

4.  The Gemini client automatically parses the output for us. By accessing the `response.parsed` attribute, we receive a ready-to-use instance of our `DocumentMetadata` Pydantic model. This eliminates the need for custom parsing functions or manual validation steps, streamlining the entire process. This pattern of using a dedicated configuration for structured output is becoming a standard across modern LLM providers, including OpenAI.

    ```python
    document_metadata = response.parsed
    print(f"Type of the response: `{type(response.parsed)}`")
    ```

    It outputs:

    ```text
    Type of the response: `<class '__main__.DocumentMetadata'>`
    ```

This native approach is robust, efficient, and requires less code. While it is the recommended way for most modern LLM APIs, the “from scratch” method remains useful for open-source models that may not have this built-in functionality.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** All four expected steps are present with matching substance: the GenerateContentConfig object, the shortened prompt, the model call, and response.parsed producing a ready DocumentMetadata instance. The closing paragraph covers the same 'recommended approach, but from-scratch remains useful' idea as the expected section, reworded rather than verbatim.
- `fl`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The section opens with the transition relocated from the end of the expected Pydantic section, which reads naturally here. The four steps follow the same order as the expected section, and the closing sentence plays the same wrap-up role as the expected section's.
- `de`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** [instances=1; quality=strong] The claim that 'some providers claim a jump in reliability from ~36% to nearly 100% compared to prompt engineering alone' matches an exploration-tagged source precisely ('was around 35.9% reliable before structured outputs. Now, it's 100% reliable') -- verified against the source directly rather than assumed from the citation, and the article's 'nearly 100%' is if anything slightly more conservative than the source's flat 100%. This is a 'real-world case study or concrete metric about the core topic's performance' and is classified strong given the specific, verified quantified figures.
- `be`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] The qualifying depth instance above is a performance metric about the core topic itself (native structured output reliability) rather than a connection to an adjacent field.
- `cp`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The qualifying depth addition is a single clause within the section's introductory paragraph; the section's core Gemini/Pydantic walkthrough remains the clearly dominant focus.
- `ga`: Implementing structured outputs using Gemini and Pydantic:
**0:** All four guideline steps are present and correctly explained, including a verified, accurately-represented reliability statistic. The issue is length: prose-only word count is approximately 359 words against a 300-word target (+/-30 tolerance, range 270-330) -- 29 words over the upper bound, a real overage rather than a near-boundary case. As with the Pydantic section, every required element is present and correct; the section is simply over-elaborated relative to the guideline's stated length.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset2`

**Article text:**
```
## Implementing structured outputs using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually. When working with modern APIs such as Gemini and OpenAI, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective than manual prompt engineering, as the vendor will always handle the optimization on top of their models better than your manual prompting [[16]](https://ai.google.dev/gemini-api/docs/structured-output), [[18]](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode), [[19]](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640).

Let’s see how to achieve the same result using the Gemini API's native capabilities. The process becomes much simpler.

### Configuring the Model for Pydantic Output

We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `"application/json"` and the `response_schema` to our `DocumentMetadata` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model.

```python
from google.genai import types

config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)
```

### Simplifying the Prompt

This configuration makes our prompt significantly shorter and cleaner, eliminating the need to manually inject any type of schema. We simply ask the model to perform the task, as the output format is guided directly by the config.

```python
prompt = f"""
Analyze the following document and extract its metadata.

Here is the document:
<document>
{DOCUMENT}
</document>
"""
```

### Calling the Model and Parsing the Response

Now, we call the model, passing our simplified prompt and the new configuration object. The API handles the rest, ensuring the output adheres to the schema.

```python
response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
```

The Gemini client automatically parses the output for us. By accessing the `response.parsed` attribute, we receive a ready-to-use instance of our `DocumentMetadata` Pydantic model.

```python
document_metadata = response.parsed
print(f"Type of the response: `{type(document_metadata)}`")
```

It outputs:

```text
Type of the response: `<class '__main__.DocumentMetadata'>`
```

This native approach is robust, efficient, and requires less code. While it is the recommended way for closed-source APIs or AI frameworks, the “from scratch” method remains useful for open-source models that may not have this built-in functionality.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** All four expected steps are present with matching substance: the GenerateContentConfig object, the shortened prompt, the model call, and response.parsed producing a ready DocumentMetadata instance. The closing paragraph covers the same 'recommended, but from-scratch remains useful' idea, reworded.
- `fl`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** The section opens with the transition relocated from the end of the expected Pydantic section, reading naturally here. The four steps follow the same order as the expected section.
- `de`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] No depth additions traceable to an exploration-phase source were identified specifically in this section on this article (the notable verified additions -- the reliability statistic, the web-scraping analogy, the schema-complexity tax -- all landed in earlier sections this time).
- `be`: Implementing Structured Outputs Using Gemini and Pydantic:
**0:** [instances=0] No breadth additions identified in this section.
- `cp`: Implementing Structured Outputs Using Gemini and Pydantic:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so core_preservation scores 1 by default.
- `ga`: Implementing structured outputs using Gemini and Pydantic:
**1:** All four guideline steps are present and correctly explained. Prose-only word count is 281 words against a 300-word target (+/-30 tolerance, range 270-330), within range.

## Section: S4::section-4-implementing-structured-outputs-from-scratch-using-pydantic  (weight=0.400, contribution=+0.0163 FOR deep)
Stored section rewards: deep=0.4641  standard=0.3866  (explore: deep=0.3334  standard=0.2764)

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset3`

**Article text:**
```
## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. This uncertainty can lead to bugs and make your code difficult to maintain. Pydantic solves this problem by enforcing structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses).

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This "fail-fast" behavior is essential for building reliable systems, preventing bad data from moving through your application and causing hard-to-debug errors later. This is a major improvement over simple JSON parsing, as it introduces a validation layer that catches errors early.

1.  You define your desired data structure as a Pydantic class, using standard Python type hints for each field. Pydantic works with Python’s `typing` module, but in newer Python versions, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over `from typing import List` and `tags: List[str]`. The `Field` function allows you to add descriptions, which are not just for documentation; they are included in the generated schema to give the LLM more context about what each field represents.
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

2.  You can also nest Pydantic models to represent more complex, hierarchical data. This allows you to define intricate relationships between different pieces of information. For example, when analyzing customer reviews, you might want a summary with a sentiment score and a list of tagged topics with relevance scores. However, it is good practice to keep schemas as simple as possible, as complex nested structures can confuse the LLM, lead to errors, and potentially increase latency on the first API call as the schema is processed and cached by the provider [[15]](https://community.openai.com/t/introducing-structured-outputs/896022).
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

3.  With our Pydantic model defined, you can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. This contract dictates the expected fields, their types, and any validation rules. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[8]](https://ai.google.dev/gemini-api/docs/structured-output). This enforcement is not magic. Under the hood, modern APIs use techniques like constrained decoding. At each step of text generation, the model calculates probabilities (logits) for every possible next token. A grammar-based guide, often implemented as a finite-state machine, then applies a bias to these logits, effectively forbidding any token that would violate the schema's rules [[16]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction).
    ```python
    schema = DocumentMetadata.model_json_schema()
    ```

4.  The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process. Pydantic automatically translates Python types (`str`, `list[str]`) into their JSON Schema equivalents (`string`, `array` of `string`).
    It outputs:
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

5.  You update your prompt to include this JSON Schema, giving the model a much more precise set of instructions.
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

6.  You call the model and extract the JSON string as before.
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

7.  The biggest difference is that you can now load the output dictionary into your Pydantic model and validate it.
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
    The `document_metadata` Pydantic object can now be safely used throughout your application. This is the main advantage: you move from unclear dictionaries to clean, predictable Python objects. If the LLM had returned `tags` as a simple string instead of a list, Pydantic would have caught it and the output would have been `Validation failed!`. A common production pattern is to catch the `ValidationError`, feed the error message back to the LLM, and retry. This self-correction loop, where the model learns from its mistakes, significantly improves the reliability of data extraction pipelines [[17]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

### Pydantic vs. Dataclasses and TypedDict

Python’s built-in `dataclasses` or `TypedDict` can define structure, but they only provide type hints for static analysis tools like `mypy` [[3]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). They do not perform runtime validation. This means if the LLM returns a string where an integer is expected, or if a required field is missing, a `dataclass` or `TypedDict` will not catch this error immediately. The error will only surface later during execution, making it harder to debug [[18]](https://www.packetcoders.io/typeddict-vs-pydantic).

-   **TypedDict**: Best for lightweight type hints inside a system where you trust the data sources and want to avoid runtime overhead. It helps during development with static analysis but offers no protection at runtime [[19]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to).
-   **Dataclasses**: Ideal for simple, internal data containers where performance is a priority and validation is handled elsewhere. They are faster to instantiate because they skip runtime checks [[20]](https://softwarelogic.co/en/blog/pydantic-vs-dataclasses-which-excels-at-python-data-validation).
-   **Pydantic**: The best choice for handling external, untrusted data, such as LLM outputs or API inputs. Its runtime validation, type coercion, and clear error messages provide the data integrity needed for production systems.

Overall, Pydantic’s runtime validation, type constraints, and clear schema definitions make it a strong option for structuring and validating data in LLM workflows and AI agent systems. Its features are well-suited for building reliable, production-ready applications.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** Both sections cover the same core ideas: plain dictionaries are insufficient, Pydantic's ValidationError / fail-fast behavior, the DocumentMetadata class, nested Summary/Tag models, schema generation, schema/contract terminology, Gemini/OpenAI similar technique, schema-injected prompt, model call, Pydantic validation with successful output, the validation failure concept (present in prose at step 7), and the TypedDict/dataclasses comparison. The generated section adds depth content (constrained decoding/FSM mechanism, self-correction retry) and restructures the TypedDict comparison as bullets under an H3. All core ideas from the GT are present.
- `fl`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** Neither section contains images or diagrams. Both use prose paragraphs followed by numbered steps. Flow matches.
- `de`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** [instances=4; quality=strong,strong,standard,standard] Four depth additions, all traceable to exploration sources. (1) Field descriptions are not just documentation; they are included in the generated schema to give the LLM more context (mechanism explanation). (2) Complex nested schemas can increase latency on the first API call as the schema is processed and cached (traces to community.openai.com exploration material). (3) Full constrained-decoding / finite-state-machine / logit-bias explanation of how modern APIs enforce schemas under the hood (traces to bentoml.com exploration source). (4) Self-correction retry pattern that catches ValidationError, feeds the error back to the LLM, and retries (traces to machinelearningmastery.com exploration source).
- `be`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** [instances=0] No breadth additions. Constrained decoding, latency, and the self-correction loop are technical depth within the LLM/Pydantic domain.
- `cp`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The depth additions (Field descriptions rationale, latency note, constrained decoding/FSM, self-correction retry) enrich individual steps without shortening or replacing GT core content. The DocumentMetadata class, nested models, schema generation, validation, and TypedDict comparison are all present. Core preserved.
- `ga`: Implementing structured outputs from scratch using Pydantic:
**1:** All 14 guideline-specified conceptual points are present and in the correct order: DocumentMetadata class, Python typing note (in step 1 prose), nesting with Summary and Tag (step 2), schema generation (step 3), schema/contract terminology (step 3), Gemini/OpenAI reference (step 3), prompt (step 5), model call (step 6), validated output (step 7), validation failure concept in prose (step 7), TypedDict/dataclasses comparison, and the final Pydantic-vs-dicts note. Depth additions (constrained decoding/FSM, latency note, self-correction retry) are acceptable exploration-phase content closely related to the section's subject. Prose-only word count is approximately 816 words, within the 810–990 tolerance band (target 900 ± 90).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset3`

**Article text:**
```
## Implementing structured outputs from scratch using Pydantic

Pydantic solves the problem of data integrity by enforcing structure and type hints at runtime. It provides a single, clear source of truth for your data structure and can automatically generate a JSON Schema from your Python class [[9]](https://pydantic.dev/articles/llm-intro).

When an LLM produces output that does not match the structure and types defined in your Pydantic model, the library raises a `ValidationError`. This error isn't generic; it clearly explains what went wrong—for example, `field 'growth_rate' expected a string but received an integer`. This "fail-fast" behavior is essential for building reliable systems, preventing bad data from moving through your application and causing hard-to-debug errors later.

This is a major improvement over simple JSON parsing, as it introduces a validation layer that catches errors early. Let's refactor our previous example to use Pydantic.

1.  We define our desired data structure as a Pydantic class. This class acts as a single source of truth for your output format. We use standard Python type hints to define the expected type for each field. Pydantic works with Python’s `typing` module, but starting with Python 11, you can use built-in types like `list` directly.

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

    You can also nest Pydantic models to represent more complex, hierarchical data. This helps organize your data logically and reflects real-world complexity. However, it is good practice to keep schemas from becoming overly complex, as this can confuse the LLM and lead to errors, such as malformed nested objects, type mismatches, or missing fields.

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

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. The standard term for defining the structure and constraints of your data is a `schema` or a `contract`. Think of it as a formal agreement between your application and the LLM. This contract precisely dictates the expected fields, their types, and any validation rules. We provide this generated schema to the LLM to guide its output, giving the model a clear blueprint for its response. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[10]](https://ai.google.dev/gemini-api/docs/structured-output), [[11]](https://platform.openai.com/docs/guides/structured-outputs).

    Internally, these APIs use a technique called constrained decoding. At each step of text generation, the model calculates probabilities (logits) for every possible next token. By applying a logit mask, the API can forbid the model from choosing tokens that would violate the schema, effectively forcing compliance.

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

    A more advanced pattern is to build a retry mechanism. If Pydantic validation fails, you can automatically send a new request to the LLM, including the validation error message in the prompt. This feedback helps the model correct its mistake on the next attempt, making the extraction process more resilient [[19]](https://www.leocon.dev/blog/2024/11/from-chaos-to-control-mastering-llm-outputs-with-langchain-and-pydantic), [[20]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction), [[21]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

    While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis tools. They do not perform runtime validation. This means if the LLM returns a string where an integer is expected, or if a required field is missing, a `dataclass` or `TypedDict` will not catch this error immediately. The invalid data will propagate through your system until it causes an error during execution, potentially leading to difficult-to-debug issues later. Pydantic's runtime validation makes it a more robust choice for handling data from unpredictable sources like LLMs [[12]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to), [[13]](https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg).

    Pydantic’s runtime validation, type constraints, and clear schema definitions make it a strong option for structuring and validating data in LLM workflows and AI agent systems. Its features are well-suited for building reliable, production-ready applications.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The generated section uses the same `DocumentMetadata` class (identical fields) as the central named example -- no substitution. Nesting, schema generation, the schema-injected prompt, the model call, and validation via model_validate are all present with matching substance. As on all three prior articles, the expected section's worked type-mismatch failure example is replaced by a prose description of the same idea rather than a worked demonstration -- the same recurring borderline question applies here too.
- `fl`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** Internal progression matches. However, the expected section's closing transition ('Let's see how we can configure modern LLM APIs like Gemini...') is absent from the end of this section -- it has been relocated to the opening of the generated Gemini section instead, the fourth article in a row with this exact relocation pattern. Scored against where it is expected, its absence here is a Flow failure.
- `de`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** [instances=2; quality=strong,standard] Two distinct qualifying instances trace to this episode's exploration-phase sources. (1) The constrained-decoding/logit-mask explanation ('the model calculates probabilities (logits) for every possible next token... a logit mask [forbids]...tokens that would violate the schema') is not explicitly cited by number, but its content matches exploration-phase sources describing logit masking and constrained decoding almost exactly -- traceable through content match rather than an inline citation marker, which the source-attribution gate permits. Classified strong: a detailed, accurate mechanism explanation, not a passing mention. (2) The production retry pattern (capturing a ValidationError and feeding it back to the LLM) matches exploration-tagged sources on LLM output error-recovery; standard, brief treatment consistent with the same pattern seen on two prior articles.
- `be`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** [instances=0] Both qualifying depth instances stay within the core topic (schema-enforcement mechanics and Pydantic's own error-recovery patterns) rather than connecting outward to an adjacent field.
- `cp`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The constrained-decoding paragraph and the retry-pattern note are each a few sentences within a much longer walkthrough; the section's core DocumentMetadata walkthrough and TypedDict/dataclass comparison remain fully present and clearly dominant.
- `ga`: Implementing structured outputs from scratch using Pydantic:
**0:** Content coverage is thorough -- the `DocumentMetadata` class matches the golden notebook exactly, and nesting, schema generation/injection, the terminology note, the constrained-decoding explanation, validation, and the TypedDict/dataclass comparison are all present, several enriched with well-grounded technical depth. However, prose-only word count is approximately 696 words against a 900-word target (+/-90 tolerance, range 810-990) -- about 114 words below the lower bound, a real and non-trivial shortfall (the fourth article in a row where this section runs short, though less severe than the first two).

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset3`

**Article text:**
```
## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. Pydantic is a data validation library that solves this by enforcing structure and type hints at runtime, ensuring data integrity from the moment data enters your application [[10]](https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation). It provides a single source of truth for your data structure and can automatically generate a JSON Schema from your Python class.

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This immediate feedback mechanism is crucial for constructing robust applications, preventing bad data from moving through your application and causing hard-to-debug errors later. This is a major improvement over simple JSON parsing, as it introduces a validation layer that catches errors early.

Let's refactor our previous example to use Pydantic.

1.  We define our desired data structure as a Pydantic class. Pydantic works with Python’s `typing` module, but starting with Python 11, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`. We have modified the `DocumentMetadata` model to showcase more of Pydantic’s power. We changed `growth_rate` to `growth_rate_percent` and its type to `int`, adding constraints using `Field` to ensure the value is between 0 and 1000 [[3]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs). We also added a `sentiment` field using `Literal` from Python's `typing` module, which restricts the output to one of the predefined string values [[11]](https://dev.to/klement_gunndu/stop-parsing-json-by-hand-structured-llm-outputs-with-pydantic-1pg0). These declarative validation rules are a key advantage of Pydantic, as they allow you to define complex constraints directly within your data model, making your code cleaner and more maintainable.
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
    You can also nest Pydantic models to represent more complex, hierarchical data [[12]](https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24). This allows you to define intricate relationships between different pieces of information. However, it is good practice to keep schemas as simple as possible, as complex nested structures can confuse the LLM and lead to errors. Here is how you could define a more complex structure:
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
    When this `ComplexDocumentMetadata` model is converted to a JSON Schema, Pydantic automatically handles the nested structure by creating definitions for `Summary` and `Tag` and referencing them using `$ref`. This creates a clean, modular schema that is easy for both humans and machines to understand. This capability is essential for modeling real-world data, which is often hierarchical.

2.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM [[7]](https://www.decodingai.com/p/llm-structured-outputs-the-only-way). This technique is similar to what APIs like Gemini and OpenAI use internally to enforce a specific output format [[13]](https://pydantic.dev/articles/llm-intro), [[14]](https://ai.google.dev/gemini-api/docs/structured-output). Internally, this is often done via constrained decoding. At each step, the model calculates probabilities (logits) for every possible next token. To enforce a schema, a logit mask is applied, setting the probability of any invalid token to zero [[15]](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction). This forces the model to only generate tokens that are valid at that point in the structure, ensuring compliance.
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

3.  We update our prompt to include this JSON Schema. This gives the model a much more precise set of instructions than our previous plain-text example, reducing the chance of misinterpretation.
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

4.  We call the model and extract the JSON string as before. The process remains the same, but the quality and consistency of the output are expected to be higher due to the more explicit instructions.
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
        "Revenue Growth",
        "Market Expansion"
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

5.  Now, we can load the output dictionary into our Pydantic model and validate it. The `model_validate` method is the core of Pydantic's power. It takes the raw dictionary, checks it against the schema, performs type coercion where possible (e.g., converting a string "20" to an integer 20), and raises a `ValidationError` if anything is amiss.
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
    The `document_metadata` object can now be safely used throughout your application. The core idea is to use these predictable Pydantic objects in downstream components, not obscure Python dictionaries. With dictionaries, you constantly have to write defensive code, checking for missing keys or incorrect types, which pollutes your logic with `if-else` statements and `try-except` blocks. Pydantic objects eliminate this, providing clean, type-safe attribute access and better IDE support like autocompletion.

### Pydantic vs. TypedDict and Dataclasses

While Pydantic is a powerful tool, it is worth knowing about other options in Python for defining data structures. Python’s built-in `dataclasses` and `TypedDict` also help define structure, but they serve different purposes [[16]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to), [[17]](https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg).

**TypedDict** is a feature from the `typing` module that provides static type checking for dictionary keys and values. It is lightweight and fast because it does not perform any validation at runtime. This makes it suitable for internal type hints where you trust the data source, but it offers no protection against invalid data from an external source like an LLM [[18]](https://www.packetcoders.io/typeddict-vs-pydantic). If the LLM returns a dictionary with a missing key or a wrong type, `TypedDict` will not raise an error at runtime; the problem will only surface later when your code tries to access the incorrect data.

**Dataclasses** are a convenient way to create classes for storing data. They automatically generate methods like `__init__` and `__repr__`, reducing boilerplate code. However, like `TypedDict`, they do not perform runtime validation by default. If an LLM returns a string where an integer is expected, a dataclass will not catch the error upon instantiation [[19]](https://softwarelogic.co/en/blog/pydantic-vs-dataclasses-which-excels-at-python-data-validation). The type mismatch will go unnoticed until it causes an error during execution, potentially leading to difficult-to-debug issues later.

Pydantic, on the other hand, is built specifically for runtime data validation and parsing. While this adds a small performance overhead compared to dataclasses, the safety it provides is invaluable when dealing with unpredictable LLM outputs [[20]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses). For this reason, Pydantic has become the standard for modeling data in AI applications. Its ability to catch errors at the boundary—where data enters your system—makes it an indispensable tool for building robust and reliable AI workflows.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The generated section uses the same `DocumentMetadata` class name and purpose as the central example, but modifies two of its five fields: `growth_rate` (str) becomes `growth_rate_percent` (int, with Field ge=0/le=1000 constraints), and a new `sentiment: Literal[...]` field is added. This is explicitly flagged in the article's own text as a deliberate enhancement ('We have modified the DocumentMetadata model to showcase more of Pydantic's power'), not an accidental substitution, and the nesting example (Summary/Tag/ComplexDocumentMetadata) is left unchanged and matches the expected section exactly. This is a genuinely novel situation relative to every prior article -- not a wholesale substitution to a differently-named class (which would be a clear-cut content mismatch), but a partial, well-integrated modification of the same named artifact. Scored 1 since the class identity, purpose, and majority of structure are preserved and the core teaching point is intact (if anything, extended), but flagging this explicitly as worth a ruling given it is a new pattern that could recur.
- `fl`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** Internal progression matches. However, the expected section's closing transition is absent from the end of this section -- it has been relocated to the opening of the generated Gemini section instead, consistent with the systematic relocation pattern observed on nearly every article graded for this lesson. Scored against where it is expected, its absence here is a Flow failure.
- `de`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** [instances=3; quality=strong,strong,strong] Three distinct qualifying instances trace to this episode's exploration-phase sources, each verified against actual source content. (1) The `growth_rate_percent` Field(ge=0, le=1000) numeric-constraint addition matches exploration-tagged content on Pydantic constrained-integer patterns ('Field(ge=..., le=...)... Validation rejects out-of-range values') closely. (2) The `sentiment: Literal[...]` addition matches an exploration-tagged source's dedicated 'Pattern 2: Use Literal for Constrained Choices' section almost exactly, down to the enum-constraint mechanism explanation. (3) The logit-mask/constrained-decoding explanation ('a logit mask is applied, setting the probability of any invalid token to zero') matches an exploration-tagged source on grammar-constrained decoding via logit masks precisely. All three are classified strong: specific, verified, technical mechanism explanations rather than generic mentions.
- `be`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** [instances=0] All three qualifying depth instances stay within the core topic (Pydantic schema modeling and decoding mechanics) rather than connecting outward to an adjacent field.
- `cp`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The three qualifying additions total perhaps 12-15% of this section's substantial word count; the core DocumentMetadata walkthrough (modified but intact) and the TypedDict/dataclass comparison remain clearly dominant and are not crowded out.
- `ga`: Implementing structured outputs from scratch using Pydantic:
**0:** Word count here is not the issue -- approximately 1028 words against a 900-word target (+/-90 tolerance, range 810-990) is only about 21% of the tolerance band's width past the boundary, treated as a trivial near-boundary miss. The substantive concern is different and new: the guideline explicitly instructs to 'use all the code from the notebook' for this section, but this article modifies the notebook's `DocumentMetadata` class (renaming/retyping `growth_rate`, adding a `sentiment` field) rather than reproducing it as given, even though the modification is well-motivated and clearly flagged. Whether a deliberate, well-integrated enhancement to the notebook's own central class should count as 'using all the code from the notebook' is a genuinely new judgment call -- flagging explicitly rather than resolving it silently, since this pattern has not come up on any prior article and could recur.

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/04_structured_outputs__preset2`

**Article text:**
```
## Implementing structured outputs from scratch using Pydantic

While forcing JSON output is an improvement, it still leaves you with a plain Python dictionary. You cannot be sure what is inside that dictionary, if the keys are correct, or if the values have the right type. This uncertainty can lead to bugs and make your code difficult to maintain. This is where Pydantic helps. Pydantic is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment data enters your application [[6]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

When an LLM produces output that does not match the structure and types defined in your Pydantic model, the library raises a `ValidationError`. This error clearly explains what went wrong, allowing you to quickly identify and fix issues. This "fail-fast" behavior is essential for building reliable systems, preventing bad data from moving through your application and causing hard-to-debug errors later.

Let's refactor our previous example to use Pydantic.

1.  We define our desired data structure as a Pydantic class. This class provides a single, clear definition for your output format. We use standard Python type hints to define the expected type for each field. The `description` parameter in `Field` is not just for documentation; it’s a direct instruction to the LLM. Underlying extraction mechanisms inject these descriptions into the prompt, so a clear and specific description improves the quality of the generated output [[42]](https://mlpills.substack.com/p/issue-128-structured-llm-outputs).
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

2.  Pydantic works with Python’s `typing` module, but starting with Python 11, you can use built-in types like `list` directly. For example, `tags: list[str]` is now preferred over importing `List` from `typing`.

3.  You can also nest Pydantic models to represent more complex, hierarchical data, such as a `DocumentMetadata` model containing `Summary` and `Tag` objects. This allows you to define intricate relationships between different pieces of information. However, it is good practice to keep schemas as simple as possible, as complex nested structures can confuse the LLM [[17]](https://mlpills.substack.com/p/issue-128-structured-llm-outputs). Pydantic also allows for custom validation logic using the `@field_validator` decorator. This is useful for checks that go beyond simple type and range constraints, such as ensuring a field's value conforms to a specific business rule [[41]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).
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
    A common pitfall to be aware of is the "Empty Array Trap." LLMs often struggle with returning empty lists when no relevant data is found, sometimes hallucinating entries to avoid an empty array. To mitigate this, you can explicitly guide the model by setting a default and providing a clear description in the `Field` definition, like `tags: list[str] = Field(default_factory=list, description="A list of tags. Return an empty list [] if no tags are found.")` [[43]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk).

### Injecting Pydantic Schema into the Prompt

1.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM [[1]](https://www.decodingai.com/p/llm-structured-outputs-the-only-way).
    ```python
    schema = DocumentMetadata.model_json_schema()
    ```

2.  The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[22]](https://ai.google.dev/gemini-api/docs/structured-output).
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

5.  The output is a JSON object conforming to the schema.
    ```json
    {
        "summary": "The Q3 2023 earnings report indicates strong financial performance with a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy, market expansion, and improved customer retention.",
        "tags": [
            "Financial Performance",
            "Earnings Report",
            "Business Growth",
            "Revenue Growth",
            "Market Expansion"
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

6.  Now, the key difference is that we can validate the output with Pydantic.
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

7.  The `document_metadata` object is a Pydantic model instance that can be safely used throughout your application, with full type-hinting and attribute access. This is the main advantage: you move from unclear dictionaries to clean, predictable Python objects. For example, if the LLM returned a simple string for the `tags` attribute instead of a list, Pydantic would raise a `ValidationError`, preventing the invalid data from proceeding.
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

Python’s built-in `dataclasses` or `TypedDict` can define structure, but they only provide type hints for static analysis tools [[36]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to), [[38]](https://www.packetcoders.io/typeddict-vs-pydantic). They do not perform runtime validation. This means if the LLM returns a string where an integer is expected, or if a required field is missing, a `dataclass` or `TypedDict` will not catch this error immediately. A type mismatch will go unnoticed until it causes an error during execution, potentially leading to difficult-to-debug issues later. While `TypedDict` can be faster for simple cases without validation, Pydantic's overhead is minimal for the robust data integrity it provides.

Overall, Pydantic’s runtime validation, type constraints, and clear schema definitions make it a strong option for structuring and validating data in LLM workflows and AI agent systems. Its features are well-suited for building reliable, production-ready applications.

While Pydantic brings structure and validation to LLM outputs, in this example, we still had to construct prompts and handle responses manually. Let’s see how we can configure modern LLM APIs like Gemini to natively output Pydantic structured outputs.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** Both sections cover the same core ideas: plain dictionaries are insufficient, Pydantic's ValidationError / fail-fast behavior, the DocumentMetadata class with the same fields, nested Summary/Tag models, schema generation, the schema/contract terminology, the schema-injected prompt, model call, Pydantic validation with successful output, and the TypedDict/dataclasses comparison. The generated section adds depth material (Field description as LLM instruction, custom validators, Empty Array Trap) and introduces an H3 sub-header, but all core ideas from the GT are present. The validation failure concept is conveyed in prose in step 7 even without a separate explicit failure demo code block.
- `fl`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** Neither section contains images or diagrams. Both have prose paragraphs followed by numbered steps with code blocks. Flow matches. (The H3 sub-header is a structural issue addressed in the structure criterion, not a media placement issue.)
- `de`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** [instances=3; quality=strong,strong,strong] Three depth additions, all cleanly traceable to exploration sources. (1) The description parameter in Field is not just documentation; it is a direct instruction injected into the prompt (traces to bytetunnels.com and mlpills.substack.com exploration sources). (2) Custom validation via the @field_validator decorator for business-rule checks beyond simple type/range constraints (traces to machinelearningmastery exploration source). (3) The 'Empty Array Trap' (LLMs struggle with returning empty lists and may hallucinate entries) together with the concrete mitigation of default_factory=list + clear Field description (explicitly named as 'Pitfall 3: The Empty Array Trap' in exploration material).
- `be`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** [instances=0] No breadth additions. Field-description injection, custom validators, and the Empty Array Trap are technical depth within the Pydantic/LLM validation domain.
- `cp`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The depth additions (Field description as LLM instruction in step 1, custom validators in step 3, Empty Array Trap paragraph) are insertions that supplement rather than replace core content. The DocumentMetadata class, nested models, schema generation, validation, TypedDict comparison, and final Pydantic-vs-dicts note are all present. Core preserved.
- `ga`: Implementing structured outputs from scratch using Pydantic:
**0:** The guideline specifies a section length of 900 words (prose only, excluding code). The generated section has approximately 782 prose words, which falls 28 words below the 810-word lower bound of the acceptable range (target 900 ± 90). All 14 guideline-specified conceptual points are present and in the correct order (DocumentMetadata class, Python 11 typing note, nesting with Summary and Tag, schema injection subsection, schema/contract terminology, Gemini/OpenAI reference, prompt, model call, validation with successful output, validation failure concept in prose, TypedDict/dataclasses comparison, and the final Pydantic-vs-dicts note), and the depth additions (Field descriptions as LLM instructions, custom validators, Empty Array Trap) are well-integrated. However, the prose depth remains slightly insufficient, falling just outside the lower bound of the acceptable word count range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate1__preset2`

**Article text:**
```
## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. Pydantic solves this problem. It is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[4]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to).

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. For example, if the model returns a string instead of an integer or misses a required field, Pydantic will catch the error immediately. This "fail-fast" behavior is essential for building reliable systems.

Let's refactor our previous example to use Pydantic.

### Defining the Pydantic Model

1.  We define our desired data structure as a Pydantic class, which acts as a single source of truth for the output format. It works with Python’s standard `typing` library to define the expected type for each attribute. Since Python 3.9, you can use built-in types like `list` directly, so `tags: list[str]` is now preferred over importing `List` from `typing`.

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

    It is important to note that the `description` parameter in `Field` is not just for documentation; it is injected into the prompt to guide the model, making specific descriptions a key part of the prompt engineering process [[8]](https://mlpills.substack.com/p/issue-128-structured-llm-outputs).

### Nesting Pydantic Models

2.  You can also nest Pydantic models to represent more complex, hierarchical data. This allows you to define intricate relationships between different pieces of information. However, every constraint you add increases latency, and complex schemas can sometimes confuse the LLM [[3]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). It is good practice to start simple and add complexity only when necessary.

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

    Even with a well-defined schema, LLMs can exhibit subtle failure modes. A common issue is the “empty array trap,” where models may hallucinate an entry rather than return a truly empty list if no relevant information is found in the text. Explicitly instructing the model in the prompt to return an empty list `[]` if no items are found can help mitigate this [[3]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk).

### Generating the JSON Schema

3.  With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard term for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. We provide this schema to the LLM to guide its output. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[9]](https://ai.google.dev/gemini-api/docs/structured-output).

    ```python
    schema = DocumentMetadata.model_json_schema()
    ```

    The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process.

    ```text
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

### Updating the Prompt

4.  We update our prompt to include this JSON Schema, giving the model a much more precise set of instructions.

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

### Calling the Model and Parsing

5.  We call the model and extract the JSON string as before.

    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    
    parsed_response = extract_json_from_response(response.text)
    ```

    It outputs:

    ```text
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

### Validating the Output

6.  Now, the biggest difference is that we can load the output dictionary into our Pydantic model and validate it.

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

    The `document_metadata` Pydantic object can now be safely used throughout your application. This is the main advantage: you move from obscure dictionaries to clean, predictable Python objects. You no longer need to pollute your code with checks for missing keys or incorrect types. For example, if the `tags` attribute were a simple string instead of a list, Pydantic would raise a `ValidationError`, immediately flagging the issue.

For production systems, you can build even more resilience by implementing a retry mechanism. If Pydantic validation fails, the `ValidationError` can be captured, and its message can be fed back to the LLM in a subsequent call. This allows the model to self-correct based on the specific error, progressively improving its output until it conforms to the schema [[10]](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs).

### Pydantic vs. Other Options

While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis and do not perform runtime validation [[4]](https://shazaali.substack.com/p/type-safety-in-langgraph-when-to). If the LLM returns a string where an integer is expected, these tools will not catch the error. Pydantic's runtime validation, type constraints, and clear schema definitions make it our favorite way for structuring and validating domain data structures in our AI apps.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The generated section uses the same `DocumentMetadata` class (identical fields) as the central named example -- no substitution. Nesting, schema generation, the schema-injected prompt, the model call, and validation via model_validate are all present with matching substance. As on both prior articles, the expected section's worked type-mismatch failure example (actual code plus a 'Validation failed!' output) is replaced by a prose description of the same idea rather than a worked demonstration -- the same recurring borderline question about whether this counts as a missing substantive idea applies here too.
- `fl`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** Internal progression matches. However, the expected section's closing transition ('Let's see how we can configure modern LLM APIs like Gemini...') is absent from the end of this section -- it has been relocated to the opening of the generated Gemini section instead ('While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually...'). This is now the third article in a row with this exact relocation pattern, suggesting it may be a systematic pipeline characteristic rather than an isolated choice. Scored against where it is expected, its absence here is a Flow failure.
- `de`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** [instances=4; quality=strong,standard,standard,standard] Four distinct qualifying instances trace to this episode's exploration-phase sources. (1) The 'empty array trap' -- models hallucinating an entry instead of returning an empty list -- matches an exploration-tagged source's dedicated 'Pitfall 3: The Empty Array Trap' section closely; strong, since it names a specific failure pattern with a specific mitigation. (2) The latency/complexity caution ('every constraint you add increases latency, and complex schemas can sometimes confuse the LLM') matches an exploration-tagged source's latency-vs-schema-complexity discussion; standard, since the article's own treatment is brief and does not carry over the source's own quantification. (3) The field-description-injection note (Field descriptions are 'injected into the prompt to guide the model') matches an exploration-tagged mlpills source; standard. (4) The production retry pattern (capturing a ValidationError and feeding it back to the LLM to self-correct) matches an exploration-tagged Pydantic-validation guide's retry-with-error-feedback content; standard, brief single-sentence treatment.
- `be`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** [instances=0] All four qualifying depth instances above stay within the core topic (Pydantic/schema mechanics and their own failure modes) rather than connecting outward to adjacent fields or industries.
- `cp`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** Even with four qualifying depth additions, each is brief (a sentence or two), and the section's core walkthrough -- class definition, nesting, schema, prompt, validation, and the TypedDict/dataclass comparison -- remains fully present and clearly dominant; the additions read as supporting asides rather than a competing narrative.
- `ga`: Implementing structured outputs from scratch using Pydantic:
**0:** Content coverage is strong -- the `DocumentMetadata` class matches the golden notebook exactly, and nesting, schema generation/injection, the terminology note, the Gemini/OpenAI parallel, validation, and the TypedDict/dataclass comparison are all present, several enriched with well-grounded technical detail (the empty-array trap, latency tradeoffs, the retry pattern). However, prose-only word count is approximately 716 words against a 900-word target (+/-90 tolerance, range 810-990) -- about 94 words below the lower bound, roughly 10% short of the boundary itself, which is a real, non-trivial shortfall (this is the third article in a row where this specific section runs short, though the smallest gap of the three).

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/04_structured_outputs__replicate2__preset2`

**Article text:**
```
## Implementing structured outputs from scratch using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. This uncertainty can lead to bugs and make your code difficult to maintain.

Pydantic solves this problem. It is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment it enters your application. Pydantic also performs automatic type coercion where possible; for instance, it can convert a string like "123" into an integer 123, which is helpful when dealing with LLM outputs that might confuse types. It provides a single, clear definition for your data structure and can automatically generate a JSON Schema from your Python class. A schema is a formal contract between your application and the LLM. This contract dictates the expected fields, their types, and any validation rules. When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This “fail-fast” behavior is essential for building reliable systems, preventing bad data from moving through your application and causing hard-to-debug errors later [[6]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[15]](https://zenvanriel.com/ai-engineer-blog/pydantic-ai-validation).

### Defining the Pydantic Model

We define our desired data structure as a Pydantic class, using standard Python type hints to define the expected type for each field. Pydantic works with Python’s `typing` module, but starting with Python 3.9, you can use built-in types like `list` directly. For example, `tags: list[str]` can be used instead of importing `List` from `typing` and writing `tags: List[str]`.

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

You can also nest Pydantic models to represent more complex, hierarchical data. However, it is good practice to keep schemas as simple as possible, as complex nested structures can confuse the LLM, lead to errors, and increase latency. This is sometimes called the "schema complexity tax" [[4]](https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk). Here is an example:

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

### Injecting the Schema into the Prompt

With our Pydantic model defined, we can automatically generate a JSON Schema from it. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[16]](https://ai.google.dev/gemini-api/docs/structured-output).

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

We update our prompt to include this JSON Schema.

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

### Validating the Output

We call the model and extract the JSON string as before.

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

But now, the biggest difference, is that we can load the output dictionary into our Pydantic model and validate it.

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

### The Power of Runtime Validation

The real strength of Pydantic is its ability to catch errors at runtime. Suppose the LLM returned the `tags` field as a single comma-separated string instead of a list:

```python
# Malformed response from an LLM
bad_response = {
    "summary": "...",
    "tags": "Financial Performance, Earnings Report, Business Growth", # Incorrect type
    "keywords": ["..."],
    "quarter": "Q3 2023",
    "growth_rate": "20%"
}

try:
    DocumentMetadata.model_validate(bad_response)
except Exception as e:
    print(f"Validation failed!\n{e}")
```

Pydantic would immediately raise a `ValidationError`, telling you exactly what went wrong:

```text
Validation failed!
1 validation error for DocumentMetadata
tags
  Input should be a valid list [type=list_type, input_value='Financial Performance, Ea...', input_type=str]
```

This immediate and precise feedback is invaluable for debugging. The `document_metadata` Pydantic object can now be safely used throughout your application, with full type-hinting and attribute access. This is the main advantage: you move from unclear dictionaries, where you constantly check for missing keys or incorrect types, to clean, predictable Python objects. Accessing `dict['key']` is risky and can raise a `KeyError`, whereas `pydantic_object.key` is type-safe and benefits from editor autocompletion.

Python’s built-in `dataclasses` or `TypedDict` can define structure, but they only provide type hints for static analysis tools. They do not perform runtime validation. This means if the LLM returns a string where an integer is expected, or if a required field is missing, a `dataclass` or `TypedDict` will not catch this error immediately. A type mismatch will go unnoticed until it causes an error during execution, potentially leading to difficult-to-debug issues later. While `TypedDict` can be faster for simple cases without validation, Pydantic's overhead is minimal for the robust data integrity it provides [[6]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[7]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/), [[16]](https://ai.google.dev/gemini-api/docs/structured-output), [[17]](https://pydantic.dev/articles/llm-intro).

Overall, Pydantic’s runtime validation, type constraints, and clear schema definitions make it a strong option for structuring and validating data in LLM workflows and AI agent systems. Its features are well-suited for building reliable, production-ready applications.
```
**Grader reasoning:**
- `cc`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The generated section uses the same `DocumentMetadata` class (identical fields) as the central named example -- no substitution. Nesting, schema generation, the schema-injected prompt, the model call, and validation via model_validate are all present with matching substance. Notably, this version fully resolves the recurring borderline question from every prior article: it includes an actual worked type-mismatch failure example (a `bad_response` dict with `tags` as a string, raising a real `ValidationError` with the precise Pydantic error message shown), which is a more complete demonstration than even the expected section's own version. No content gap here.
- `fl`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** Internal progression matches. However, the expected section's closing transition is absent from the end of this section -- it has been relocated to the opening of the generated Gemini section instead, confirming again the systematic relocation pattern observed on nearly every article graded for this lesson so far. Scored against where it is expected, its absence here is a Flow failure.
- `de`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** [instances=1; quality=standard] The nesting caution -- 'complex nested structures can confuse the LLM, lead to errors, and increase latency,' dubbed the schema complexity tax -- matches an exploration-tagged source on schema-complexity latency tradeoffs, verified directly. Standard: a catchy framing but a brief single-clause treatment without the source's own quantification.
- `be`: Implementing Structured Outputs From Scratch Using Pydantic:
**0:** [instances=0] The qualifying depth instance stays within the core topic (Pydantic schema complexity) rather than connecting outward to an adjacent field.
- `cp`: Implementing Structured Outputs From Scratch Using Pydantic:
**1:** The qualifying addition is a brief clause; the section's core walkthrough -- now including a full worked failure-case demonstration -- remains fully present and clearly dominant.
- `ga`: Implementing structured outputs from scratch using Pydantic:
**0:** Content coverage is excellent -- the `DocumentMetadata` class matches the golden notebook exactly, and nesting, schema generation/injection, the terminology note, validation, and the TypedDict/dataclass comparison are all present, plus a full worked failure-case demonstration that goes beyond even the ground-truth article's own treatment. However, prose-only word count is approximately 676 words against a 900-word target (+/-90 tolerance, range 810-990) -- about 134 words below the lower bound, roughly 74% of the tolerance band's width past the boundary, a clear and decisive shortfall despite the strong content.
