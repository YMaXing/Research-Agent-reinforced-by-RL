# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>Why do structured outputs create a contract between LLM and rigid Python code?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.decodingai.com/p/llm-structured-outputs-the-only-way

Query: Why do structured outputs create a contract between LLM and rigid Python code?

Answer: Ultimately, structured outputs create a formal contract between the LLM (Software 3.0) and your application code (Software 1.0). They are the standard method for modeling domain objects in AI engineering, connecting the probabilistic nature of LLMs with deterministic code. This approach offers several key benefits. First, structured outputs are easy to parse and manipulate programmatically. Instead of wrestling with raw text, you work with clean Python objects, making your code more predictable and easier to debug. Using libraries like Pydantic adds a layer of data and type validation (If the LLM returns a string where an integer is expected, your application raises a clear validation error immediately, preventing bad data from propagating. With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. This contract dictates the expected fields, their types, and any validation rules. Now, instead of providing a fuzzy JSON that explains how our output should look, we provide an explicit schema to the LLM that is compatible with Pydantic. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format.

-----

Phase: [EXPLOITATION]

### Source [3]: https://developer.hpe.com/blog/using-structured-outputs-in-vllm

Query: Why do structured outputs create a contract between LLM and rigid Python code?

Answer: LLMs are incredibly powerful, but their outputs can be inconsistent when a specific format is required. Structured outputs address this issue by restricting the model’s generated text to adhere to predefined rules or formats, ensuring: 1. Reliability: Outputs are predictable and machine-readable. 2. Compatibility: Seamless integration with APIs, databases, or other systems. 3. Efficiency: No need for extensive post-processing to validate or fix outputs. Structured outputs solve this problem by enforcing specific formats, such as JSON, regex patterns, or even formal grammars.

-----

Phase: [EXPLOITATION]

### Source [4]: https://www.leewayhertz.com/structured-outputs-in-llms

Query: Why do structured outputs create a contract between LLM and rigid Python code?

Answer: Structured outputs refer to the capability of these models to generate content that conforms to predefined formats, such as JSON, XML, or other structured data schemas. This approach ensures that the information produced is relevant, accurate and organized, making it easy to interpret and integrate into existing systems, such as databases, APIs. During the decoding phase, the FSM tracks the current state of the LLM’s output. It then filters out any tokens that don’t fit the required format by applying a technique known as logit bias. This involves adjusting each token’s probabilities (logits), significantly reducing the likelihood of invalid tokens being selected. As a result, the LLM is guided to generate only tokens consistent with the specified structure, ensuring the output adheres to the desired format. Structured outputs from Large Language Models (LLMs) ensure that AI-generated content meets specific formatting and accuracy requirements. By employing methods such as prompt engineering, function calling, and JSON schema enforcement, these models can produce consistent, reliable and easily interpretable outputs by humans and machines. This structured approach reduces the risk of errors and irrelevant information, known as “hallucinations,” and prepares the data for seamless integration into various systems, such as databases, APIs, and analytical tools.

-----

Phase: [EXPLOITATION]

### Source [5]: https://www.timlrx.com/blog/generating-structured-output-from-llms

Query: Why do structured outputs create a contract between LLM and rigid Python code?

Answer: Structured output refers to data or information generated in accordance with a predefined schema or format. Frequently employed formats encompass JSON, XML, or language-specific constructs like Python dictionaries. These structured outputs may also encompass additional typing information such as JSON Schema, Pydantic models, or Typescript objects. All the magic happens in these few lines of code. Essentially, it re-writes the dataclass into a sample schema and prompts the LLM to generate the JSON payload which is parsed back to a dataclass. The similarity to Python feels like a double-edged sword. While it is relatively easy to pick up for straight forward tasks, it can be more tricky to use for more complex tasks and it might be easier to coerce an LLM to generate the desired output directly, rather than work with another parser, compiler, and runtime. In terms of validation, it offers more flexibility beyond what can be done with fine-tuning but is limited by the simple data structures and types that it supports, though that might change in the future.

-----

</details>

<details>
<summary>How does Pydantic provide out-of-the-box data quality checks for LLM outputs?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs

Query: How does Pydantic provide out-of-the-box data quality checks for LLM outputs?

Answer: Pydantic helps you validate data at runtime using Python type hints. It checks that LLM outputs match your expected schema, converts types automatically where possible, and provides clear error messages when validation fails. This gives you a reliable contract between the LLM’s output and your application’s requirements. All Pydantic models inherit from `BaseModel`, which provides automatic validation. Type hints like `name: str` help Pydantic validate types at runtime. The `EmailStr` type validates email format without needing a custom regex. Fields marked with `Optional[str] = None` can be missing or null. The `@field_validator` decorator lets you add custom validation logic, like cleaning phone numbers and checking their length. The `output_cls` parameter automatically handles Pydantic validation. This works with any LLM through prompt engineering and is good for quick prototyping and simple extraction tasks. For models that support function calling, you can use FunctionCallingProgram. And when you need explicit control over parsing behavior, you can use the PydanticOutputParser method.

-----

Phase: [EXPLOITATION]

### Source [7]: https://medium.com/@aminulpalash506/pydantic-for-agentic-ai-ensuring-reliable-data-validation-in-large-language-model-workflows-ad5eae915713

Query: How does Pydantic provide out-of-the-box data quality checks for LLM outputs?

Answer: Pydantic is a powerful Python library that leverages modern type annotations to provide automatic data parsing and validation at runtime. Unlike traditional, verbose manual checks, Pydantic lets you define clean, intuitive models that effortlessly enforce data integrity. You can nest Pydantic models inside each other, allowing you to define and enforce the structure of complex inputs and outputs. Pydantic makes it easy to handle such cases with clean, type-safe models. LLM outputs can be unpredictable. Some fields might be missing or `None`. Pydantic handles this gracefully using `Optional`. This allows the model to still validate even if the confidence value is missing or unknown.

-----

Phase: [EXPLOITATION]

### Source [8]: https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation

Query: How does Pydantic provide out-of-the-box data quality checks for LLM outputs?

Answer: Pydantic is a Python library that lets you define data models using simple classes. It automatically validates data types and structures when you create a model instance. If something is missing or incorrect, Pydantic raises an error, helping you identify problems early. Pydantic lets you define exact data shapes for both inputs and outputs of your AI system. By using it to validate model responses, you can catch inconsistencies, auto-correct some of them, and make your entire LLM workflow far more reliable. Pydantic brings structure to the chaos of LLM outputs. It turns unpredictable text generation into predictable, schema-checked data. By validating model responses, you make your AI workflows reliable, debuggable, and safe for production.

-----

Phase: [EXPLOITATION]

### Source [9]: https://dev.to/manishmshiva/how-to-keep-llm-outputs-predictable-using-pydantic-validation-2dfe

Query: How does Pydantic provide out-of-the-box data quality checks for LLM outputs?

Answer: Pydantic is a Python library that lets you define data models using simple classes. It automatically validates data types and structures when you create a model instance. If something is missing or incorrect, Pydantic raises an error, helping you identify problems early. Pydantic lets you define exact data shapes for both inputs and outputs of your AI system. By using it to validate model responses, you can catch inconsistencies, auto-correct some of them, and make your entire LLM workflow far more reliable. Pydantic brings structure to the chaos of LLM outputs. It turns unpredictable text generation into predictable, schema-checked data. By validating model responses, you make your AI workflows reliable, debuggable, and safe for production.

-----

Phase: [EXPLOITATION]

### Source [10]: https://pydantic.dev/articles/llm-intro

Query: How does Pydantic provide out-of-the-box data quality checks for LLM outputs?

Answer: Pydantic goes a step further and defines a schema for your dataclass. This schema is used to validate data, but also to generate documentation and even to generate a JSON schema, which is perfect for our use case of generating structured data with language models! By defining the api payload as a Pydantic model, we can leverage the `response_model` argument to instruct the model to generate the desired output. This is a powerful feature that allows us to generate structured data from any language model! In our upcoming posts, we will provide more practical examples and explore how we can leverage `Pydantic`'s validation features to ensure that the data we receive is not only valid syntactically but also semantically.

-----

</details>

<details>
<summary>How to implement extract_json_from_response function for parsing LLM JSON?</summary>

Phase: [EXPLOITATION]

### Source [12]: https://stackoverflow.com/questions/77407632/how-can-i-get-llm-to-only-respond-in-json-strings

Query: How to implement extract_json_from_response function for parsing LLM JSON?

Answer: Post-Processing gets you to 99%. Make your application code more resilient towards non JSON-only for example you could implement a regular expression to extract potential JSON strings from a response. As an example a very naive approach that simply extracts everything between the first { and the last }: const naiveJSONFromText = (text) => { const match = text.match(/{[\s\S]*}/); if (!match) return null; try { return JSON.parse(match); } catch { return null; } }; Validation Loop gets you to 100%. In the end you will always have to implement validation logic to check A: That you deal with a valid JSON object and B: That it has your expected format. const isValidSomeObject = (obj) => typeof obj?.field1 === 'number' && typeof obj?.field2 === 'number';

-----

Phase: [EXPLOITATION]

### Source [13]: https://python.plainenglish.io/getting-structured-json-responses-from-llms-a-simple-solution-f819fc389ebc

Query: How to implement extract_json_from_response function for parsing LLM JSON?

Answer: The Solution: A Robust JSON Prompt Function. Here’s a Python function that handles this problem by enforcing structured responses and validating the output: def prompt_json(prompt: str, expected_fields: list[str]) -> dict | None: Send a prompt to the LLM expecting a JSON response with specific fields. Returns the parsed JSON dict if successful and all fields are present, else None. try: response = prompt_openai(prompt) if response.startswith("Error:"): return None cleaned = self.clean_llm_json_response(response) if response: response = response.replace('```', '').replace('json', '').strip() try: Parse JSON. Pro Tips: Always include a concrete example in your prompt. Use “raw JSON format only” to discourage extra formatting. Validate required fields to catch incomplete responses. Consider retry logic for critical applications.

-----

Phase: [EXPLOITATION]

### Source [15]: https://genai.stackexchange.com/questions/202/how-to-generate-structured-data-like-json-with-llm-models

Query: How to implement extract_json_from_response function for parsing LLM JSON?

Answer: If you’re using OpenAI’s chat completion APIs (GPT3.5 and GPT4) then you can rely on function calling to have the model format the reply to specific JSON. You can prompt the model to give you a function call, use the params (and never do the call). Important notes: To use JSON mode, your system message must instruct the model to produce JSON. To help ensure you don’t forget, the API will throw an error if the string "JSON" does not appear in your system message. The message the model returns may be partial (i.e. cut off) if finish_reason is length, which indicates the generation exceeded max_tokens or the conversation exceeded the token limit. To guard against this, check finish_reason before parsing the response. JSON mode will not guarantee the output matches any specific schema, only that it is valid and parses without errors.

-----

</details>

<details>
<summary>How to nest Pydantic models like Summary and Tag for complex LLM structures?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24

Query: How to nest Pydantic models like Summary and Tag for complex LLM structures?

Answer: To nest Pydantic models, define one model within another using class attributes. Use BaseModel for nested structures. Validate nested data automatically. Pydantic supports Dict[K, V] for key-value structures. You can also nest models in dictionaries, like Dict[str, Author]. The loc field shows the exact path to the error (comments.author.email), making it easy to debug complex structures. Nested models in Pydantic make it easy to handle complex, structured data with robust validation. Key techniques: BaseModel, Author, Blog, List[T], Dict[K, V], Optional[T], .dict(). These tools are perfect for APIs, configuration files, or any scenario with hierarchical data. Once validated, Pydantic models provide type-safe access to nested attributes. You can access fields like blog.author.name or blog.comments.content without worrying about KeyError or AttributeError. For serialization, use .dict() (or .model_dump() in Pydantic V2) with options like exclude_unset, include, or exclude.

-----

Phase: [EXPLOITATION]

### Source [17]: https://mlpills.substack.com/p/issue-128-structured-llm-outputs

Query: How to nest Pydantic models like Summary and Tag for complex LLM structures?

Answer: Nested model: A field typed as another BaseModel subclass. The parsed output contains a nested JSON object, and List[NestedModel] gives you a list of structured records rather than a list of strings. Reach for this whenever you’d otherwise be tempted to flatten multi-attribute items into comma-separated strings — structure beats parsing-after-parsing every time. Every Pydantic feature you’d use normally works here. Enums constrain outputs to a fixed set of values. Field with ge/le/gt/lt enforces numeric ranges. min_length/max_length controls string and list sizes. Nested models give you hierarchical structure. And crucially — the description parameter in Field ends up in the prompt. It’s not just documentation, it’s instructions to the model.

-----

Phase: [EXPLOITATION]

### Source [18]: https://codesignal.com/learn/courses/working-with-data-models-in-fastapi/lessons/nested-models-for-complex-data-structures

Query: How to nest Pydantic models like Summary and Tag for complex LLM structures?

Answer: Pydantic makes it straightforward to validate and manipulate nested data structures. It automatically validates the nested models based on the defined schemas. For example, if you send the following JSON to a POST endpoint: Pydantic will ensure the nested data conforms to the CrewMember and Equipment models' definitions. If any field is missing or incorrect, it will raise a validation error. You have now learned how to define and use nested Pydantic models within FastAPI to manage complex data structures effectively. We covered the importance of nested data models and how to create nested models with Pydantic. Similarly, in FastAPI, nested models let us encapsulate these relationships within a single model, streamlining data validation and manipulation. This way, our application can handle complex data interactions just as efficiently as a well-structured database. To work effectively with nested data structures, we'll represent the complexity using Pydantic models in our FastAPI application. Let's start by creating a FastAPI app with a mock dataset that includes nested relationships. In this structure, each crew member has a list of equipment objects associated with them. Now, let's define Pydantic models to represent these nested data structures. Nested models are crucial for representing complex data structures in a manner similar to how relational databases handle related tables. In a real database, you would have tables with foreign keys to represent relationships.

-----

Phase: [EXPLOITATION]

### Source [19]: https://pydantic.dev/docs/validation/latest/concepts/models

Query: How to nest Pydantic models like Summary and Tag for complex LLM structures?

Answer: More complex hierarchical data structures can be defined using models themselves as types in annotations.

-----

Phase: [EXPLOITATION]

### Source [20]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs

Query: How to nest Pydantic models like Summary and Tag for complex LLM structures?

Answer: The function sends the unstructured text to the LLM with clear formatting instructions, then validates the response against the BookSummary schema. LangChain provides built-in support for structured output extraction with Pydantic models. The first method uses PydanticOutputParser, which works with any LLM by using prompt engineering to guide the model’s output format. The parser automatically generates detailed format instructions from your Pydantic model: The PydanticOutputParser automatically generates format instructions from your Pydantic model, including field descriptions and type information. It works with any LLM that can follow instructions and doesn’t require function calling support. The chain syntax makes it easy to compose complex workflows. The second method is to use the native function calling capabilities of modern LLMs through the with_structured_output() function. Real-world data is rarely flat. Here’s how to handle nested structures like a product with multiple reviews and specifications.

-----

</details>

<details>
<summary>How does Gemini GenerateContentConfig enforce Pydantic structured outputs?</summary>

Phase: [EXPLOITATION]

### Source [21]: https://pydantic.dev/docs/ai/core-concepts/output

Query: How does Gemini GenerateContentConfig enforce Pydantic structured outputs?

Answer: Native Output mode uses a model’s native “Structured Outputs” feature (aka “JSON Schema response format”), where the model is forced to only output text matching the provided JSON schema. Note that this is not supported by all models, and sometimes comes with restrictions. For example, Gemini cannot use tools at the same time as structured output, and attempting to do so will result in an error. To use this mode, you can wrap the output type(s) in the `NativeOutput` marker class that also lets you specify a `name` and `description` if the name and docstring of the type or function are not sufficient. [...] When no output type is specified, or when `str` is among the output types, any plain text response from the model will be used as the output data. If `str` is not among the output types, the model is forced to return structured data or call an output function. If the output type schema is not of type `"object"` (e.g. it’s `int` or `list[int]`), the output type is wrapped in a single element object, so the schema of all tools registered with the model are object schemas. Structured outputs (like tools) use Pydantic to build the JSON schema used for the tool, and to validate the data returned by the model. Here’s an example of returning either text or structured data: [...] While we would generally suggest starting with tool or native output, in some cases this mode may result in higher quality outputs, and for models without native tool calling or structured output support it is the only option for producing structured outputs. If the model API supports the “JSON Mode” feature (aka “JSON Object response format”) to force the model to output valid JSON, this is enabled, but it’s still up to the model to abide by the schema. Pydantic AI will validate the returned structured data and tell the model to try again if validation fails, but if the model is not intelligent enough this may not be sufficient.

-----

Phase: [EXPLOITATION]

### Source [22]: https://ai.google.dev/gemini-api/docs/structured-output

Query: How does Gemini GenerateContentConfig enforce Pydantic structured outputs?

Answer: You can configure Gemini models to generate responses that adhere to a provided JSON Schema. This ensures predictable, type-safe results and simplifies extracting structured data from unstructured text. Using structured outputs is ideal for: In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs make it easy to define schemas using Pydantic (Python) and Zod (JavaScript). ## Structured output examples ### Recipe Extractor This example demonstrates how to extract structured data from text using basic JSON Schema types like `object`, `array`, `string`, and `integer`. `object` `array` `string` `integer` ### Python ## JSON schema support To generate a JSON object, set the `response_format` in the generation configuration. The schema must be a valid JSON Schema that describes the desired output format. `response_format` The model will then generate a response that is a syntactically valid JSON string matching the provided schema. When using structured outputs, the model will produce outputs in the same order as the keys in the schema. Gemini's structured output mode supports a subset of the JSON Schema specification. The following values of `type` are supported: `type` `string` `number` `integer` `boolean` `object` `array` `null` `"null"` `{"type": ["string", "null"]}` These descriptive properties help guide the model: `title` `description` ### Type-specific properties For `object` values:

-----

Phase: [EXPLOITATION]

### Source [23]: https://discuss.ai.google.dev/t/gemini-2-0-use-a-list-of-pydantic-objects-at-response-schema/55935

Query: How does Gemini GenerateContentConfig enforce Pydantic structured outputs?

Answer: Is it possible to use Pydantic to have a list of objects as output? The `Object` has 2 fields: `label` (which is a string) and `box_2d` (which is a list of integers). By using `response_schema=Object` in the `GenerateContentConfig`, you’re asking Gemini to return you only one Object. Here is the output of your solution: `Object` `label` `box_2d` `response_schema=Object` `GenerateContentConfig` `{ "box_2d": [ 53, 285, 283, 436 ], "label": "wallet" }` Gemini’s output is a JSON with one object, which is exactly what you’ve asked. But it’s not a list of objects, hence it does not answer my problem. @Vincent_Garcia Thank you for the clarification. [...] `import os from google import genai from google.genai.types import GenerateContentConfig from PIL import Image from pydantic import BaseModel os.environ["API_KEY"] = <YOUR_API_KEY> client = genai.Client(api_key=os.environ["API_KEY"]) image = Image.open(SOME_IMAGE_PATH) prompt = "Detect objects box 2d." class Object(BaseModel): label: str box_2d: list[int] response = client.models.generate_content( model="gemini-2.0-flash-exp", contents=[image, prompt], config=GenerateContentConfig( response_mime_type="application/json", response_schema=Object, ), ) print(response.text)` Your solution does not work. Maybe I was not clear in my initial message / question. To be more precise, your solution does something (with no error) which is different from what I’ve asked. What I’ve asked was: [...] schema.pop("title",None) _resolve(schema) return schema SOME_IMAGE_PATH = "Cajun_instruments.jpg" image = Image.open(SOME_IMAGE_PATH) prompt = "Detect objects box 2d." response = client.models.generate_content( contents=[image, prompt], model="gemini-2.0-flash-exp", config=types.GenerateContentConfig( response_mime_type='application/json', response_schema=get_schema(ObjectsList), # Use the get_schema function here ), ) # Load JSON string and validate with Pydantic obj = TypeAdapter(ObjectsList).validate_python(json.loads(response.text)) print(obj)

-----

Phase: [EXPLOITATION]

### Source [24]: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output

Query: How does Gemini GenerateContentConfig enforce Pydantic structured outputs?

Answer: "Humidity", Schema.builder().type(Type.Known.STRING).nullable(true).build(), "Wind Speed", Schema.builder().type(Type.Known.INTEGER).nullable(true).build())) .required(List.of("Day", "Temperature", "Forecast", "Wind Speed")) .build(); // Full response schema Schema responseSchema = Schema.builder() .type(Type.Known.OBJECT) .properties( Map.of( "forecast", Schema.builder().type(Type.Known.ARRAY).items(dayForecastSchema).build())) .build(); GenerateContentConfig config = GenerateContentConfig.builder() .responseMimeType("application/json") .responseSchema(responseSchema) .build(); GenerateContentResponse response = client.models.generateContent(modelId, contents, config); System.out.println(response.text()); // Example response: [...] model="gemini-2.5-flash", contents=prompt, config=GenerateContentConfig( response_mime_type="application/json", response_schema=response_schema, ), ) print(response.text) # Example output: # {"forecast": [{"Day": "Sunday", "Forecast": "sunny", "Temperature": 77, "Wind Speed": 10, "Humidity": "50%"}, {"Day": "Monday", "Forecast": "partly cloudy", "Temperature": 72, "Wind Speed": 15, {"Day": "Tuesday", "Forecast": "rain showers", "Temperature": 64, "Wind Speed": null, "Humidity": "70%"}, {"Day": "Wednesday", "Forecast": "thunderstorms", "Temperature": 68, "Wind Speed": null, {"Day": "Thursday", "Forecast": "cloudy", "Temperature": 66, "Wind Speed": null, "Humidity": "60%"}, {"Day": "Friday", "Forecast": "partly cloudy", "Temperature": 73, "Wind Speed": 12}, [...] GenerateContentConfig config = GenerateContentConfig.builder() .responseMimeType("application/json") .responseSchema(responseSchema) .build(); GenerateContentResponse response = client.models.generateContent(modelId, contents, config); System.out.println(response.text()); // Example response: // [ // { // "ingredients": [ // "2 1/4 cups all-purpose flour", // "1 teaspoon baking soda", // "1 teaspoon salt", // "1 cup (2 sticks) unsalted butter, softened", // "3/4 cup granulated sugar", // "3/4 cup packed brown sugar", // "1 teaspoon vanilla extract", // "2 large eggs", // "2 cups chocolate chips", // ], // "recipe_name": "Chocolate Chip Cookies", // } // ] return response.text(); } } `

-----

Phase: [EXPLOITATION]

### Source [25]: https://forum.langchain.com/t/structured-output-for-stategraph/2726

Query: How does Gemini GenerateContentConfig enforce Pydantic structured outputs?

Answer: `response_format=…` in LangChain is not a cross-provider contract. It works for OpenAI because OpenAI supports response\_format natively. Gemini’s native mechanism is `response_mime_type=“application/json” + response_json_schema=…` (JSON Schema / Pydantic). `response_format=…` `response_mime_type=“application/json” + response_json_schema=…` For Gemini, “tools + native structured output” is still constrained by the provider. Google’s docs i provided above only explicitly advertise combining structured outputs with built-in tools (Google Search, URL context, code execution, file search) as a Gemini 3 preview feature, and do not show custom function tools + JSON schema together in one call. So my recommendation would be keep a two-node StateGraph:

-----

</details>

<details>
<summary>How do structured outputs eliminate fragile regex parsing for LLM responses?</summary>

Phase: [EXPLOITATION]

### Source [26]: https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk

Query: How do structured outputs eliminate fragile regex parsing for LLM responses?

Answer: Structured outputs enforce strict formats, eliminating the need for fragile regex parsing. They ensure consistent, reliable data directly from LLMs. This approach reduces errors and enhances system resilience. Here's the fundamental problem with LLMs in production: LLMs are text generators. Your application needs data structures. The gap between these two things is where bugs live. When you JSON.parse() a raw LLM response, you're making several dangerous assumptions: JSON.parse() Structured output eliminates all six of these problems by constraining the model's output at the token generation level — not after the fact. ### The Three Levels of Output Control ... ## How Structured Output Actually Works Most developers treat structured output as a black box: "I give it a schema, it returns valid JSON." But understanding the mechanism matters for debugging and optimization. ### Constrained Decoding (The Magic Behind the Curtain) When an LLM generates text, it predicts the next token from a vocabulary of ~100,000+ tokens. Normally, any token can follow any other token. Structured output adds a constraint layer: Normal generation: Token probabilities: {"hello": 0.3, "{": 0.1, "The": 0.2, ...} → Any token can be selected Constrained generation (expecting JSON object start): Token probabilities: {"hello": 0.3, "{": 0.1, "The": 0.2, ...} Mask: {"hello": 0, "{": 1, "The": 0, ...} → Only "{" and whitespace tokens remain valid → Model MUST output "{" ... ### 2026 Q1–Q2 (Now) ### 2026 Q3–Q4 ### 2027 and Beyond ## Conclusion Structured output in 2026 is no longer optional for production LLM applications. The days of regex-parsing GPT responses and praying are over. The key takeaways: .parse() response_schema The real question isn't "should I use structured output?" It's "why are you still parsing free text with regex in 2026?"

-----

Phase: [EXPLOITATION]

### Source [27]: https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms

Query: How do structured outputs eliminate fragile regex parsing for LLM responses?

Answer: API-native approaches are built-in features from LLM providers like OpenAI and Anthropic that let your model output structured data—like JSON, function calls, or JSON schema. They make outputs reliable by enforcing strict formats, so no need for fragile post-processing or regex hacks. Structured outputs: Direct JSON schema enforcement where you define the exact structure and the model guarantees compliance. Function calls: The model can call predefined functions with structured parameters, enabling interaction with external tools and APIs. ... Claude models from Anthropic don’t support structured output the way OpenAI does with response_format. But you can get the same effect by using tool-based structured output with schema validation. In practice, this means you define a schema that describes the fields and types you expect, using something like Pydantic (Python) or Zod (TypeScript). That schema is converted into JSON Schema and passed to Claude as a tool. When the model generates a response, it “calls” the tool and produces output that matches the schema. On your side, you validate the response against the schema to guarantee type safety and consistent structure. This approach cuts down on parsing errors, enforces strict formats, and makes Claude’s responses much easier to use in production. ... Outlines is a Python library that ensures large language models like GPT-4 return clean, structured output. You define the data shape using Python types or tools like Pydantic, and Outlines makes the model follow it. No messy JSON, no extra parsing.

-----

Phase: [EXPLOITATION]

### Source [28]: https://www.leewayhertz.com/structured-outputs-in-llms

Query: How do structured outputs eliminate fragile regex parsing for LLM responses?

Answer: The combination of constrained sampling and CFG ensures that LLMs can generate structured outputs that strictly adhere to predefined formats, significantly improving the reliability and accuracy of the results. This process eliminates the risk of selecting inappropriate tokens, ensuring that each step in the text generation process aligns with the required schema. ## Benefits of structured outputs from LLMs Here are the key benefits of structured responses from Large Language Models (LLMs): Improved accuracy and consistency: Structured outputs help ensure that responses are accurate and consistent by confining the model to a specific format. This minimizes the risk of including irrelevant or inconsistent information, leading to more reliable results. ... ### JSON mode JSON mode is a specific configuration that ensures the LLM will output data in JSON format. This mode is particularly useful in scenarios requiring consistent and structured data, such as API responses or data integration tasks. By enforcing JSON output, this approach eliminates the risk of unstructured responses and ensures that the data format is reliable. ... Machine-readability: One key advantage of structured outputs is that they’re easily readable by machines. While humans can interpret free-form text, computers work much better with structured data. This makes integrating LLM outputs directly into other software systems or databases easier. Parsing and application: Because structured outputs follow a known format, the software can easily parse them (break them down into their constituent parts). This parsing allows for quick extracting of relevant information and facilitates using LLM outputs in various applications.

-----

Phase: [EXPLOITATION]

### Source [29]: https://www.linkedin.com/posts/pauliusztin_if-you-use-regex-and-string-splits-to-parse-activity-7386740617294282752-QHgP

Query: How do structured outputs eliminate fragile regex parsing for LLM responses?

Answer: If you use regex and string splits to parse your LLM outputs, read this... This is NOT a scalable way to build production AI systems. Why? Because LLMs don't return structured data. They return probabilistic text. Every response is slightly different. So you end up writing regex rules, string splits, or pattern matchers just to extract values. It may work in staging. But if there's one phrasing change, one missing comma, or an unexpected newline... Everything breaks. And the worst bit about it? You won't even notice until your system goes live. ... This is where structured outputs come in... Instead of parsing text, you define a Pydantic model as your data contract and require the LLM to fill it. Pydantic does 3 things: 1. Auto-generates a JSON Schema 2.

-----

Phase: [EXPLOITATION]

### Source [30]: https://tetrate.io/learn/ai/llm-output-parsing-structured-generation

Query: How do structured outputs eliminate fragile regex parsing for LLM responses?

Answer: Function calling represents a powerful paradigm for structured output that frames LLM interactions as tool usage rather than text generation. Instead of asking the model to return data in a specific format, you define functions the model can call, complete with parameter schemas. The model then decides which function to invoke and generates structured arguments that match the function signature. ... ## Output Validation and Error Handling Even with structured output techniques, robust validation and error handling remain essential components of production LLM systems. Validation ensures that outputs meet not just syntactic requirements but also semantic expectations, while error handling provides graceful degradation when issues occur. ... Error handling also differs between approaches. With JSON mode, you still need to validate that the returned JSON matches your expected structure and handle schema mismatches gracefully. Structured output APIs eliminate this validation step since compliance is guaranteed, simplifying your application logic and reducing the potential for runtime errors. This guarantee becomes especially valuable in production systems where reliability and predictability are essential.

-----

</details>

<details>
<summary>Why prefer Gemini native structured outputs over prompt-based methods?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://ai.google.dev/gemini-api/docs/structured-output

Query: Why prefer Gemini native structured outputs over prompt-based methods?

Answer: You can configure Gemini models to generate responses that adhere to a provided JSON Schema. This ensures predictable, type-safe results and simplifies extracting structured data from unstructured text. Using structured outputs is ideal for: In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs make it easy to define schemas using Pydantic (Python) and Zod (JavaScript). Structured outputs vs. function calling: Both structured outputs and function calling use JSON schemas, but they serve different purposes: Structured Outputs: Formatting the final response to the user. Use this when you want the model's answer to be in a specific format (e.g., extracting data from a document to save to a database). Function Calling: Taking action during the conversation. Use this when the model needs to ask you to perform a task (e.g., "get current weather") before it can provide a final answer. Note that Gemini 2.0 requires an explicit `propertyOrdering` list within the JSON input to define the preferred structure.

-----

Phase: [EXPLOITATION]

### Source [32]: https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6

Query: Why prefer Gemini native structured outputs over prompt-based methods?

Answer: Reliable Structure: Gemini’s native structured output eliminates the guesswork and fragility of relying solely on prompt engineering. Clear Schema is Key: The quality of your schema directly impacts the quality of the output. Be precise and descriptive. Iterate and Refine: Experiment with different schemas and input variations in AI Studio to fine-tune your results. Seamless Integration: The “Get Code” functionality makes it trivial to integrate this capability into your existing applications. Error Handling: The model does provide useful feedback, like the mention that a field is missing. You should leverage that. This isn’t some tacked-on afterthought / forced constraint; it’s baked right into the model’s DNA. This means you can _reliably_ get JSON (or other structured formats, though JSON is the focus here) without resorting to prompt-engineering shenanigans. The problem is that many LLMs are primarily trained for natural language generation, not strict data formatting. They _can_ produce JSON, but it often requires a lot of prompt engineering and a healthy dose of luck. Gemini to the Rescue: Natively Structured Output

-----

Phase: [EXPLOITATION]

### Source [33]: https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms

Query: Why prefer Gemini native structured outputs over prompt-based methods?

Answer: Google’s Gemini models support structured outputs through JSON schemas. Developers can define exactly how responses should be formatted—what fields are required, what types are allowed, and whether values must be arrays, objects, or enums. If Gemini’s output doesn’t match the schema, it raises a `JSONSchemaValidationError`. This helps catch issues early and provides clear error messages for debugging. On Vertex AI, schemas are built using tools like `Schema` and `Type`, and Gemini enforces these rules during generation. The result is more reliable outputs ready for production use. Google enforces schemas natively in Gemini through Vertex AI. Developers can specify strict JSON schemas, and Gemini guarantees compliance in generated responses. The implementation details vary, but the goal is the same: consistent, schema-driven outputs that reduce errors and simplify application development.

-----

Phase: [EXPLOITATION]

### Source [34]: https://dylancastillo.co/posts/gemini-structured-outputs.html

Query: Why prefer Gemini native structured outputs over prompt-based methods?

Answer: When considering both JSON-Prompt and JSON-Schema, Gemini’s structured outputs performed comparably to unstructured outputs. However, with JSON-Schema alone (i.e., constrained decoding), performance drops compared to unstructured outputs. This difference is most evident in the Shuffled Objects task, where NL achieved a score of 97.15%, while JSON-Schema scored 86.18%. For JSON-Prompt, the JSON schema is included in the prompt, instructing the model to generate JSON formatted output based on its MIME type configuration. JSON-Schema works similarly, but the schema is set directly in the model’s configuration instead of being included in the prompt.

-----

Phase: [EXPLOITATION]

### Source [35]: https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers

Query: Why prefer Gemini native structured outputs over prompt-based methods?

Answer: Structured outputs differ from traditional LLM outputs, which typically generate open-ended, natural language text. Instead, structured outputs enforce a schema or format, such as JSON objects with defined keys and value types, or specific classes in the output (e.g., multiple-choice answers, sentiment classes, or database row formats). This approach improves reliability, reduces errors and hallucinations, and simplifies integration into systems such as databases, APIs, or workflows. Benefits of structured LLM outputs include: Challenges include designing effective schemas, handling complex nested data, and potential limitations in reasoning capabilities compared to free-form text generation.

-----

</details>

<details>
<summary>How do TypedDict and dataclasses compare to Pydantic for LLM validation?</summary>

Phase: [EXPLOITATION]

### Source [36]: https://shazaali.substack.com/p/type-safety-in-langgraph-when-to

Query: How do TypedDict and dataclasses compare to Pydantic for LLM validation?

Answer: Use Pydantic for validation and safety, TypedDict for lightweight type hints, and dataclasses for performance. Pydantic enforces runtime validation, while TypedDict only checks types during development. In LangGraph (or any structured workflow/state management system), you usually need type safety at two levels: State shape (what fields exist, what types they have). Validation (ensuring runtime correctness, not just static typing). TypedDict: A typing construct that defines the expected keys and types of a dictionary. Best for lightweight state typing inside the LangGraph state machine (fast, minimal). Pydantic: For strict runtime validation (catching errors early), external inputs/outputs (e.g., API calls, user input, DB reads), complex/nested schemas (with defaults, constraints, enums, etc.). When to use Pydantic: At the edges of the graph (inputs/outputs, tool calls, API responses). When you want to enforce rules (e.g., confidence must be between 0 and 1). Debugging / production systems where incorrect data must be caught. Rule of Thumb: Inside the LangGraph state machine: Use TypedDict (lightweight, no runtime overhead). At the boundaries (inputs/outputs, integrations, user-facing data): Use Pydantic (validation & safety). Combined approach (common in production): State = TypedDict (fast, minimal). Each node’s inputs/outputs validated with Pydantic. Resources: LangGraph Docs — Defining State, Pydantic Official Docs.

-----

Phase: [EXPLOITATION]

### Source [37]: https://dev.to/hevalhazalkurt/dataclasses-vs-pydantic-vs-typeddict-vs-namedtuple-in-python-41gg

Query: How do TypedDict and dataclasses compare to Pydantic for LLM validation?

Answer: TypedDict: from typing import TypedDict class UserDict(TypedDict): id: int name: str email: str. Use Case: External JSON Contracts. Pros: mypy. Cons: No runtime validation. dataclass: @dataclass class InternalUser: id: int name: str email: str is_active: bool = True. Pros: __post_init__, field(). Cons: No validation. Pydantic: from pydantic import BaseModel, EmailStr class User(BaseModel): id: int name: str email: EmailStr. Use Case: API Input Validation. Pros: Validation and coercion. Cons: Slight overhead. Pydantic.dataclasses: from pydantic.dataclasses import dataclass @dataclass class User: id: int name: str. Each of these tools solves a specific problem. Think of them as different screwdrivers in your Python toolbox: dataclass, Pydantic, TypedDict, NamedTuple. Example → Caching a product catalog from the database @dataclass class Product: id: int name: str price: float tags: list[str]. Pydantic is a 3rd-party library focused on data validation and parsing. It uses Python type hints, just like dataclass, but adds a lot more power under the hood.

-----

Phase: [EXPLOITATION]

### Source [38]: https://www.packetcoders.io/typeddict-vs-pydantic

Query: How do TypedDict and dataclasses compare to Pydantic for LLM validation?

Answer: TypedDict: Lightweight Type Hints. Use TypedDict when your main goal is to benefit from type hints during development. It’s fast, minimal, and ideal if you don’t need runtime guarantees. from typing import TypedDict class VLAN(TypedDict): id: int name: str vlan10: VLAN = {"id": 10, "name": "Management"} # Checked by tools like mypy. Remember: TypedDict only helps during development, it won’t protect you from invalid data at runtime. Wrong type at runtime (no error until you run into issues later) vlan_bad: VLAN = {"id": "not-an-int", "name": "Data"} print(vlan_bad) # Allowed at runtime, but incorrect. Pydantic: Runtime Safety & Defaults. If you need safe runtime behavior, use Pydantic. It not only validates input, but also converts compatible types, making it a robust choice for external data (e.g. API inputs). Use it when you need runtime validation, default handling, and type conversion. Slight runtime cost, but significantly safer for handling real-world input. Feature Comparison: Feature | TypedDict | Pydantic Type checking | Static only (development time) | Runtime (with actual enforcement) Validation | None | Built‑in validation and coercion Performance | Super lightweight | Slightly heavier due to parsing Default values | Not supported - every field must be explicitly provided | Fully supported - fields can have defaults, optional values, and even computed defaults. Summary: TypedDict is perfect for development-time type checks. Pydantic is the choice for safe, validated, and flexible data handling at runtime.

-----

Phase: [EXPLOITATION]

### Source [39]: https://softwarelogic.co/en/blog/pydantic-vs-dataclasses-which-excels-at-python-data-validation

Query: How do TypedDict and dataclasses compare to Pydantic for LLM validation?

Answer: Pydantic vs Dataclasses: Which Excels at Python Data Validation? Choose Pydantic for robust validation, API boundaries, and complex data. Opt for dataclasses in simple, internal, or high-performance scenarios. Don’t hesitate to combine both for maximum flexibility. When Dataclasses Are Sufficient: Simple internal models with trusted data. High-performance scenarios where validation is handled elsewhere. Reducing dependencies in small scripts or tools. Combining Both Approaches: You can use Pydantic’s dataclasses integration for a hybrid approach, gaining validation with a familiar dataclass syntax: from pydantic.dataclasses import dataclass @dataclass class User: id: int name: str. This enables type enforcement while maintaining compatibility with dataclasses features. Performance and Security Considerations: Performance Benchmarks: Dataclasses: Faster instantiation, no runtime checks. Pydantic: Extra milliseconds for validation, but worth it for critical data paths. Is Pydantic always better than dataclasses? Not always. Pydantic is superior for external data validation, but dataclasses are ideal for simple, internal data management where performance and minimalism matter. Can I combine Pydantic and dataclasses? Yes. Use `pydantic.dataclasses.dataclass` or structure your code to use Pydantic at the boundaries, dataclasses internally. How do I handle complex nested data? Pydantic shines here—use nested `BaseModel` classes. With dataclasses, you’ll need custom parsing and validation logic.

-----

Phase: [EXPLOITATION]

### Source [40]: https://www.speakeasy.com/blog/pydantic-vs-dataclasses

Query: How do TypedDict and dataclasses compare to Pydantic for LLM validation?

Answer: Pydantic is the most comprehensive solution available to enforce type safety and data validation in Python. Type Annotations, Data Classes, TypedDicts, and finally, Pydantic. In this example, we define a DuckStats TypedDict with three keys: name, age, and feather_count. The type hints in the TypedDict definition specify that the name key should have a string value, while the age and feather_count keys should have integer values. When we pass a dictionary to the describe_duck function, the IDE will show us a hint if there is a type mismatch in the dictionary values. This can help us catch bugs early and ensure that the data we are working with has the correct types. While we now have type hints for dictionaries, data passed to our functions from the outside world are still unvalidated. Users can pass in the wrong types of values and we won’t find out until runtime. This brings us to Pydantic. Pydantic is the most comprehensive solution available to enforce type safety and data validation in Python, which is why we chose it for our SDKs at Speakeasy. The Value of Runtime Type Safety. Using Typed Dictionaries With Pydantic Models.

-----

</details>

<details>
<summary>How to diagram LLM output formatting for downstream tasks with Mermaid?</summary>

Phase: [EXPLOITATION]

### Source [42]: https://www.matt-adams.co.uk/2025/02/12/structured-data-generation.html

Query: How to diagram LLM output formatting for downstream tasks with Mermaid?

Answer: Use a two-step approach for reliable LLM output formatting: 1. Generate structured JSON from the model using a system prompt focused on content and relationships. 2. Convert JSON to Mermaid syntax via code. Example function get_formatted_output prompts for JSON with elements and relationships, then calls convert_to_mermaid which builds graph TD, adds nodes like node_id["label"], and appends relationships. This avoids direct Mermaid generation errors. Supports other formats like Graphviz or Gherkin. Handles JSONDecodeError with error handling. Focuses on content generation first, then format conversion for downstream tasks.

-----

Phase: [EXPLOITATION]

### Source [43]: https://arxiv.org/html/2511.14967v1

Query: How to diagram LLM output formatting for downstream tasks with Mermaid?

Answer: MermaidSeqBench evaluates LLM-to-Mermaid sequence diagram generation. LLMs generate structured diagrams from natural language, including sequence diagrams in Mermaid syntax. Benchmark has 132 NL-Mermaid pairs with structured descriptions of Purpose, Main Components, Interactions. Mermaid uses Markdown-inspired syntax for sequence diagrams showing object interactions over time. Prior work shows LLMs proficient at producing Mermaid sequence diagrams. Evaluation framework assesses syntax, for software engineering tasks. Examples in appendices detail Mermaid syntax and rendered diagrams paired with NL descriptions.

-----

Phase: [EXPLOITATION]

### Source [44]: https://microsoft.github.io/genaiscript/blog/mermaids

Query: How to diagram LLM output formatting for downstream tasks with Mermaid?

Answer: Mermaid supports various diagram types like flowcharts with syntax graph TD, nodes A[Start] --> B{Is it?}. LLMs generate Mermaid but may produce syntax errors; a repairer LLM fixes parse errors by receiving error messages and regenerating valid diagrams, e.g., correcting classDiagram relationships and removing invalid classDef. Diagrams rendered in Markdown previews and GitHub. Used for class diagrams of code symbols. Process: generate, detect errors, repair via chat, return fixed Mermaid. Supports options for node/edge appearance.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What failure modes arise when nesting complex Pydantic models for LLM outputs?</summary>

Phase: [EXPLORATION]

### Source [46]: https://mlpills.substack.com/p/issue-128-structured-llm-outputs

Query: What failure modes arise when nesting complex Pydantic models for LLM outputs?

Answer: Failure modes include incorrect field names, missing required fields, wrong data types, and extra text. Nested models can lead to complex validation errors. Use strict schemas to prevent invalid data. PydanticOutputParser generates JSON-schema format instructions, parses LLM text response and validates against model. On failure returns OutputParserException. Constrained fields (float, string, int) and Enum prevent common issues like out-of-range values or inconsistent formats. LCEL composes prompt | model | parser for reliable structured outputs.

-----

Phase: [EXPLORATION]

### Source [47]: https://dev.to/klement_gunndu/stop-parsing-json-by-hand-structured-llm-outputs-with-pydantic-1pg0

Query: What failure modes arise when nesting complex Pydantic models for LLM outputs?

Answer: Manual parsing leads to failure modes: missing fields, wrong types, inconsistent formats, silent data corruption. Nested models work out of the box with libraries handling schema translation. Literal types enforce enum constraints preventing inconsistencies like case variations. Use Optional for missing fields. When schemas are complex, native SDK parse methods or Instructor handle nesting reliably across providers.

-----

Phase: [EXPLORATION]

### Source [48]: https://zenvanriel.com/ai-engineer-blog/pydantic-ai-validation

Query: What failure modes arise when nesting complex Pydantic models for LLM outputs?

Answer: LLM outputs may have missing fields, wrong types, invalid values raising ValidationError. Nested hierarchical models for complex config. Use Optional[type] for fields LLMs may omit. ValidationError provides structured errors with field name, expected type, received value. Partial parsing allows deciding on partial results vs reject. Pydantic integrates with Instructor, LangChain, OpenAI for structured outputs.

-----

Phase: [EXPLORATION]

### Source [49]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs

Query: What failure modes arise when nesting complex Pydantic models for LLM outputs?

Answer: LLM output failure modes: incorrect field names, missing required fields, wrong data types, extra text wrapped around data. Without validation, inconsistencies cause runtime errors. Use regex to extract JSON from response text handling markdown or explanatory text. Catch JSONDecodeError, ValidationError separately. extract_json_from_llm_response handles cleanup while parse handles validation.

-----

Phase: [EXPLORATION]

### Source [50]: https://ylanglabs.com/blogs/building-reliable-llm-workflows-with-pydantic

Query: What failure modes arise when nesting complex Pydantic models for LLM outputs?

Answer: Tool call risks: malformed arguments like wrong field names (orderId vs order_id) or invalid values (DROP TABLE). Nested models (SupportTicket containing CustomerQuery plus ResolutionPlan) keep layers typed. Validation with model_validate_json returns typed object or precise ValidationError. Chain validation for nested structures. Strict patterns, enums, optional fields. If validation fails, hand error back to LLM for repair.

-----

</details>

<details>
<summary>How does Pydantic v2 enhance runtime validation for ambiguous LLM structured data?</summary>

Phase: [EXPLORATION]

### Source [51]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs

Query: How does Pydantic v2 enhance runtime validation for ambiguous LLM structured data?

Answer: Pydantic helps you validate data at runtime using Python type hints. It checks that LLM outputs match your expected schema, converts types automatically where possible, and provides clear error messages when validation fails. This gives you a reliable contract between the LLM’s output and your application’s requirements. This article shows you how to use Pydantic to validate LLM outputs. You’ll learn how to define validation schemas, handle malformed responses, work with nested data, integrate with LLM APIs, implement retry logic with validation feedback, and more. Let’s not waste any more time. ➗ ‍ You can find the code on GitHub. Before you go ahead, install Pydantic version 2.x with the optional email dependencies: `pip install pydantic[email]`. ## Getting Started [...] The first attempt misses the required `attendees` field, the second attempt includes it but with the wrong type, and the third attempt gets everything correct. The retry mechanism handles these progressive improvements. ## Conclusion Pydantic helps you go from unreliable LLM outputs into validated, type-safe data structures. By combining clear schemas with robust error handling, you can build AI-powered applications that are both powerful and reliable. Here are the key takeaways: Define clear schemas that match your needs Validate everything and handle errors gracefully with retries and fallbacks Use type hints and validators to enforce data integrity Include schemas in your prompts to guide the LLM [...] All Pydantic models inherit from `BaseModel`, which provides automatic validation. Type hints like `name: str` help Pydantic validate types at runtime. The `EmailStr` type validates email format without needing a custom regex. Fields marked with `Optional[str] = None` can be missing or null. The `@field_validator` decorator lets you add custom validation logic, like cleaning phone numbers and checking their length. Here’s how to use the model to validate sample LLM output:

-----

Phase: [EXPLORATION]

### Source [52]: https://zenvanriel.com/ai-engineer-blog/pydantic-ai-validation

Query: How does Pydantic v2 enhance runtime validation for ambiguous LLM structured data?

Answer: # Pydantic for AI Validation - Type Safety for LLM Applications While LLMs generate impressive outputs, production systems need structured, validated data. Pydantic provides the foundation for type safety in Python AI applications. Through building production AI systems, I’ve identified how Pydantic transforms unreliable LLM outputs into trustworthy data. For structured output patterns, see my Instructor structured output guide. ## Why Pydantic for AI Pydantic addresses fundamental challenges in AI application development. Type Safety: Python’s dynamic typing is flexible but error-prone. Pydantic adds runtime type checking, catching errors before they cascade. Validation: LLM outputs need validation. Pydantic validates data against schemas, ensuring outputs meet requirements. [...] ## Validating LLM Outputs LLM output validation is a primary use case. JSON Parsing: Parse LLM JSON outputs into Pydantic models. Invalid JSON fails immediately with clear errors. Schema Compliance: Verify LLM outputs match expected schemas. Missing fields, wrong types, or invalid values raise ValidationError. Automatic Coercion: Pydantic coerces compatible types. String “123” becomes int 123. Configure strictness as needed. Error Messages: Validation errors include detailed information. Field name, expected type, received value, everything needed for debugging. ## AI-Specific Validation Patterns Patterns particular to AI applications. Optional Fields: LLMs may not always extract every field. Use Optional[type] for fields that might be missing. [...] Logging Strategies: Log validation failures for debugging and quality monitoring. Include enough context for diagnosis. For error handling, see my AI error handling patterns guide. ## Performance Considerations Optimize Pydantic usage in high-throughput systems. Model Caching: Pydantic caches validation logic. Reusing models is efficient. Validation Mode: Use model\_validate for parsing, direct instantiation for validated data. Choose appropriately. Minimal Models: Define minimal models for simple use cases. Extra fields add validation overhead. V2 Performance: Pydantic V2 offers significant performance improvements. Upgrade if still on V1. ## Testing Pydantic Models Ensure models behave correctly. Valid Data Tests: Test that valid data parses correctly. Include edge cases.

-----

Phase: [EXPLORATION]

### Source [53]: https://pydantic.dev/articles/llm-intro

Query: How does Pydantic v2 enhance runtime validation for ambiguous LLM structured data?

Answer: While some have resorted to threatening human life to generate structured data, we have found that Pydantic is even more effective. In this post, we will discuss validating structured outputs from language models using Pydantic and OpenAI. We’ll show you how to write reliable code. Additionally, we’ll introduce a new library called instructor that simplifies this process and offers extra features to leverage validation to improve the quality of your outputs. ## #Pydantic Unlike libraries like `dataclasses`, `Pydantic` goes a step further and defines a schema for your dataclass. This schema is used to validate data, but also to generate documentation and even to generate a JSON schema, which is perfect for our use case of generating structured data with language models! [...] `dataclasses` `Pydantic` A simple example of validation involves ensuring that a value has the correct type. For instance, let’s consider a `Person` dataclass with a `name` field of type `str`. We can validate that the value is indeed a string. `Person` `name` `str` `from dataclasses import dataclass @dataclass class Person: name: str age: int Person(name="Sam", age="10") >>> Person(name="Sam", age="10")` By using the `dataclass` decorator, we can pass in the values as strings without any complaints from the dataclass. This would mean that we could run into issues later on if we try to use the `age` field as an `int`. `dataclass` `age` `int` `Person(name="Sam", age="10").age + 1 >>> TypeError: can only concatenate str (not "int") to str` [...] Example Output `{ "rewritten_query": "novel developments advancements ai artificial intelligence machine learning", "published_daterange": { "start": "2023-12-15", "end": "2023-01-01", "domains_allow_list": ["arxiv.org"] } }` By defining the api payload as a Pydantic model, we can leverage the `response_model` argument to instruct the model to generate the desired output. This is a powerful feature that allows us to generate structured data from any language model! `response_model` In our upcoming posts, we will provide more practical examples and explore how we can leverage `Pydantic` validation features to ensure that the data we receive is not only valid syntactically but also semantically. `Pydantic` ## Related content

-----

Phase: [EXPLORATION]

### Source [54]: https://pydantic.dev/docs/validation/latest/concepts/experimental

Query: How does Pydantic v2 enhance runtime validation for ambiguous LLM structured data?

Answer: Partial validation is particularly helpful when processing the output of an LLM, where the model streams structured responses, and you may wish to begin validating the stream while you’re still receiving data (e.g. to show partial data to users). Caution Partial validation is an experimental feature and may change in future versions of Pydantic. The current implementation should be considered a proof of concept at this time and has a number of limitations.

-----

Phase: [EXPLORATION]

### Source [55]: https://oneuptime.com/blog/post/2026-01-21-python-pydantic-v2-validation/view

Query: How does Pydantic v2 enhance runtime validation for ambiguous LLM structured data?

Answer: Blog News & insights Status System status Changelog What’s new Videos Watch & learn Support Company OneUptime Enterprise Existing customer? Sign in # How to Validate Data with Pydantic v2 Models Learn how to validate and serialize data in Python using Pydantic v2. This guide covers model definition, custom validators, computed fields, settings management, and integration with FastAPI. Nawaz Dhandala ## On this page Data validation is one of those things you either do properly or regret later. Pydantic v2 brings a complete rewrite with significant performance improvements and a cleaner API. It uses Python type hints to validate data at runtime, catching bugs before they cause problems. [...] ## Best Practices Use Field() for documentation: Add descriptions and examples for better API documentation. Prefer computed\_field over property: Computed fields are included in serialization automatically. Use SecretStr for sensitive data: Prevents accidental logging of passwords and tokens. Validate at boundaries: Validate data when it enters your system (API requests, file parsing). Use model\_config instead of class Config: This is the Pydantic v2 way. Cache settings with lru\_cache: Avoid repeated environment variable reads. Use exclude\_unset for partial updates: Get only the fields that were actually provided. Building reliable APIs? OneUptime provides comprehensive monitoring for your FastAPI applications, tracking validation errors, response times, and endpoint health. [...] name: str = Field(min_length=2, max_length=100) # Email field (Pydantic provides built-in email validation) email: str = Field(pattern=r’^[a-zA-Z0-9._%+-]+@[a-zA-C9.-]+\.[a-zA-Z]{2,}$’) # Optional field with default age: Optional[int] = Field(default=None, ge=0, le=150) # Enum field role: UserRole = UserRole.USER # List of strings tags: List[str] = Field(default_factory=list) # Nested model address: Optional[Address] = None # Datetime with default created_at: datetime = Field(default_factory=datetime.utcnow) # Creating instances user = User( id=1, name="John Doe", email="[email protected]", age=30, tags=["developer", "python"], address=Address( street="123 Main St", city="New York", country="USA", postal_code="10001" ) ) # Validation happens automatically

-----

</details>

<details>
<summary>What edge cases break the extract_json_from_response function on real LLM outputs?</summary>

Phase: [EXPLORATION]

### Source [56]: https://tetrate.io/learn/ai/llm-output-parsing-structured-generation

Query: What edge cases break the extract_json_from_response function on real LLM outputs?

Answer: The unpredictability manifests in several ways. First, formatting inconsistency means that even when prompted to return JSON, an LLM might include markdown code fences, explanatory text before or after the JSON, or malformed syntax that breaks standard parsers. Second, schema drift occurs when the model decides to add helpful but unexpected fields, rename keys for clarity, or nest data differently than specified. Third, type inconsistency appears when the model returns strings instead of numbers, arrays instead of single values, or null values in unexpected places. JSON mode operates by modifying the model’s sampling process to only consider tokens that maintain valid JSON syntax. If the current state is inside a string value, the model won’t generate a closing brace that would break the structure. If an object is open, the model knows it must eventually close it. This constraint dramatically reduces parsing failures, though it doesn’t guarantee the JSON matches your expected schema—the model might still return valid JSON with unexpected fields or structures. These challenges compound in production systems where reliability is paramount. A chatbot that occasionally fails to extract user intents creates frustrating experiences. A data pipeline that crashes on malformed JSON disrupts business operations. An agent that misinterprets function parameters could execute incorrect actions with real consequences. Traditional approaches like regex parsing and string manipulation are brittle, requiring constant maintenance as model behaviors evolve.

-----

Phase: [EXPLORATION]

### Source [57]: https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk

Query: What edge cases break the extract_json_from_response function on real LLM outputs?

Answer: `# Input: "The weather is nice today." # Expected: {"entities": [], "topics": ["weather"]} # Actual: {"entities": [{"name": "weather", "type": "concept"}], "topics": ["weather"]} # The model HATES returning empty arrays. # Solution: Make empty arrays explicitly valid and prompt for them class Extraction(BaseModel): entities: list[Entity] = Field( default_factory=list, description="Named entities found in the text. Return empty list [] if none found.")` ### Pitfall 4: Enum Confusion with Similar Values [...] `response_format` ### Basic Usage `from openai import OpenAI from pydantic import BaseModel client = OpenAI() class SentimentAnalysis(BaseModel): sentiment: str # "positive", "negative", "neutral" confidence: float key_phrases: list[str] reasoning: str response = client.beta.chat.completions.parse( model="gpt-5-mini", messages=[ {"role": "system", "content": "Analyze the sentiment of the given text."}, {"role": "user", "content": "This product is absolutely terrible. Worst purchase ever."} ], response_format=SentimentAnalysis, ) result = response.choices.message.parsed print(result.sentiment) # "negative" print(result.confidence) # 0.95 print(result.key_phrases) # ["absolutely terrible", "worst purchase ever"]` ### With Enums and Nested Objects [...] Solution: Use explicit schema versioning and migration: `from pydantic import BaseModel, Field from typing import Literal class UserProfile(BaseModel): schema_version: Literal["2.0"] = "2.0" name: str = Field(alias="user_name") # Accept old field name email: str = Field(alias="email_address") age: int location: str | None = None class Config: populate_by_name = True # Accept both alias and field name` ### Pitfall 3: The Empty Array Trap LLMs struggle with returning empty arrays when there's genuinely nothing to extract. They'll often hallucinate entries to "fill" the array.

-----

Phase: [EXPLORATION]

### Source [58]: https://stackoverflow.com/questions/77407632/how-can-i-get-llm-to-only-respond-in-json-strings

Query: What edge cases break the extract_json_from_response function on real LLM outputs?

Answer: Post-Processing --> gets you to 99% Make your application code more resilient towards non JSON-only for example you could implement a regular expression to extract potential JSON strings from a response. As an example a very naive approach that simply extracts everything between the first `{` and the last `}` `{` `}` `const naiveJSONFromText = (text) => { const match = text.match(/[\s\S]*/); if (!match) return null; try { return JSON.parse(match); } catch { return null; } };` Validation Loop --> gets you to 100% In the end you will always have to implement validation logic to check A: That you deal with a valid JSON object and B: That it has your expected format. `const isValidSomeObject = (obj) => typeof obj?.field1 === 'number' && typeof obj?.field2 === 'number';` [...] `JSON` jeff's user avatar ## 1 Comment Add a comment Generally speaking: Due to the nature of LLMs, you can never guarantee a JSON response. You will have to adopt your strategy to cope with this fact. Out of the top of my head these are your options: Prompt engeneering --> gets you to 95% With careful prompting and specific instructions you can maximize the likelihood of getting a JSON response. There are a lot of ressources on prompt engineering out there, but since it is model dependent and subject to change, you will always have to experiment on what works best for your case. Post-Processing --> gets you to 99% [...] `parser.getFormatInstructions()` `invoke` When we pass `parser.getFormatInstructions()` to the `format_instructions` property, this lets LangChain append the desired `JSON` schema that we defined in step 1 to our prompt before sending it to the large language model. `parser.getFormatInstructions()` `format_instructions` `JSON` As a final point, it is absolutely critical to make sure your query/prompt is relevant and produces values that could be interpreted as the properties in your object `SomeObject` that are defined in the `parser`. `SomeObject` `parser` Please give this a try, and let me know if you're able to consistently output `JSON`. `JSON` jeff's user avatar ## 1 Comment Add a comment

-----

Phase: [EXPLORATION]

### Source [59]: https://www.reddit.com/r/Python/comments/1tagc2g/i_tested_structured_output_from_288_llm_calls_and

Query: What edge cases break the extract_json_from_response function on real LLM outputs?

Answer: # I tested structured output from 288 LLM calls and logged every way JSON breaks. Here's what I found : r/Python Skip to main contentI tested structured output from 288 LLM calls and logged every way JSON breaks. Here's what I found : r/Python Open menu Open navigation Wrote it up here: What Breaks When You Ask an LLM for JSON The article covers: A taxonomy of the 8 most common structured output failures Why the order you apply repairs in matters (this was the part that surprised me most) Why JSON mode helps but doesn't solve the problem What changes when you need to support YAML and TOML alongside JSON

-----

Phase: [EXPLORATION]

### Source [60]: https://atamel.dev/posts/2024/07-15_control_llm_output

Query: What edge cases break the extract_json_from_response function on real LLM outputs?

Answer: The response respects the schema: ``` Prompt: List a few popular cookie recipes Prompt: List a few popular cookie recipes Response: [ Response: [ { { "recipe_name": "Chocolate Chip Cookies", "recipe_name": "Chocolate Chip Cookies", "calories": 150 "calories": 150 }, }, { { "recipe_name": "Peanut Butter Cookies", "recipe_name": "Peanut Butter Cookies", "calories": 160 "calories": 160 }, }, { { "recipe_name": "Oatmeal Raisin Cookies", "recipe_name": "Oatmeal Raisin Cookies", "calories": 140 "calories": 140 }, }, { { "recipe_name": "Sugar Cookies", "recipe_name": "Sugar Cookies", "calories": 130 "calories": 130 } } ] ] ``` ## Extract with response schema You can also use response schema to extract information in a more structured way. [...] For example, you can extract social media comments from free-form text into a structured JSON format like this: [...] Prompt: Prompt: Extract reviews from our social media: Extract reviews from our social media: - "Absolutely loved it! Best ice cream I’ve ever had." Rating: 4 - "Absolutely loved it! Best ice cream I’ve ever had." Rating: 4 - "Quite good cheese cake, but a bit too sweet for my taste." Rating: 2 - "Quite good cheese cake, but a bit too sweet for my taste." Rating: 2 - "Did not like the tiramisu." Rating: 0 - "Did not like the tiramisu." Rating: 0 Response: [ Response: [ { { "dessert_name": "ice cream", "dessert_name": "ice cream", "message": "Absolutely loved it! Best ice cream I’ve ever had", "message": "Absolutely loved it! Best ice cream I’ve ever had", "rating": 4 "rating": 4 }, }, { { "dessert_name": "cheese cake", "dessert_name": "cheese cake", "message":

-----

</details>

<details>
<summary>What accuracy and cost metrics favor Gemini native structured outputs over prompt JSON?</summary>

Phase: [EXPLORATION]

### Source [61]: https://dylancastillo.co/posts/gemini-structured-outputs.html

Query: What accuracy and cost metrics favor Gemini native structured outputs over prompt JSON?

Answer: NL and JSON-Prompt are tied, without a clear winner between them. Each method got a slight edge over in 3 out of 6 tasks. On the other hand, JSON-Schema performed worst than NL in 5 out of 6 tasks. Plus, in Shuffled Objects, it did so with a gap of more than 10 percentage points: 97.15% for NL vs. 86.18% for JSON-Schema. Tam et al. defined structured outputs as any method that “involves providing output in standardized formats like JSON or XML through format restriction.” which is in line with the less rigid interpretation of structured outputs. Using this definition, the results show no performance gap between structured and unstructured outputs. This directly contradicts the study’s original claim. [...] Figure 1: Best results for Gemini 1.5 Flash. The figure above compares the performance of Gemini’s structured outputs to unstructured outputs. NL stands for Natural Language, which means the model writes the output in a free-form manner. In contrast, JSON-Prompt and JSON-Schema involve structured outputs that follow a predefined JSON schema. For JSON-Prompt, the JSON schema is included in the prompt, instructing the model to generate JSON formatted output based on its MIME type configuration. JSON-Schema works similarly, but the schema is set directly in the model’s configuration instead of being included in the prompt. [...] When considering both JSON-Prompt and JSON-Schema, Gemini’s structured outputs performed comparably to unstructured outputs. However, with JSON-Schema alone (i.e., constrained decoding), performance drops compared to unstructured outputs. This difference is most evident in the Shuffled Objects task, where NL achieved a score of 97.15%, while JSON-Schema scored 86.18%.

-----

Phase: [EXPLORATION]

### Source [62]: https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6

Query: What accuracy and cost metrics favor Gemini native structured outputs over prompt JSON?

Answer: Reliable Structure: Gemini’s native structured output eliminates the guesswork and fragility of relying solely on prompt engineering. Clear Schema is Key: The quality of your schema directly impacts the quality of the output. Be precise and descriptive. Iterate and Refine: Experiment with different schemas and input variations in AI Studio to fine-tune your results. Seamless Integration: The “Get Code” functionality makes it trivial to integrate this capability into your existing applications. Error Handling: The model does provide useful feedback, like the mention that a field is missing. You should leverage that. [...] At my meetups, I often suggest giving Google AI Studio a try. It’s a free and easy way to experiment, to try the latest models and play with the hidden levers of Gemini/Gemma models. I definitely have to write an article about AI Studio, but specifically in this case, it’s a great fit because it exposes visually one of the best capabilities of the Gemini models: their native support for structured output. This isn’t some tacked-on afterthought / forced constraint; it’s baked right into the model’s DNA. I believe this has been possible since the 1.5 Pro release, but it’s certainly a key feature now. This means you can _reliably_ get JSON (or other structured formats, though JSON is the focus here) without resorting to prompt-engineering shenanigans. How It Works: AI Studio and Beyond [...] “Please, oh wise and powerful LLM, could you possibly provide your response in JSON format?” To stern directives: “Respond ONLY in JSON. Do not include any other text.” And even, occasionally, to veiled (or not-so-veiled) threats: “If you don’t give me JSON, I’m switching to [Competitor LLM]!” Yes, everyone has their own unique approach, some even swear by it, but more often than not an update, a special character, or just that one important invocation can screw it up and leave you always uneasy. The problem is that many LLMs are primarily trained for natural language generation, not strict data formatting. They _can_ produce JSON, but it often requires a lot of prompt engineering and a healthy dose of luck. Gemini to the Rescue: Natively Structured Output

-----

Phase: [EXPLORATION]

### Source [63]: https://humanloop.com/blog/structured-outputs

Query: What accuracy and cost metrics favor Gemini native structured outputs over prompt JSON?

Answer: According to OpenAI, getting LLMs to respond in a specific format via prompt engineering was around 35.9% reliable before structured outputs. Now, it’s 100% reliable (if strict is set to true). Structured outputs lead to 100% consistency in JSON schema formatting. Source: OpenAI Structured outputs lead to 100% consistency in JSON schema formatting. Source: OpenAI ## How do Structured Outputs Work? [...] Constraining the output to a specific format means structured outputs help reduce variability and errors. Therefore, the outputs are more reliable for tasks where consistency and accuracy are key, like API interactions or database updates. OpenAI introduced Structured Outputs as a wider-scoped and vastly improved version of JSON mode, which was released in 2023 to ensure models would output JSON once instructed. The problem with JSON mode being that it doesn’t consistently output the correct schema. Structured outputs enforce a schema, making integrations with APIs and other tools more reliable, and reducing the chance that the model generates incorrect or irrelevant content. [...] The code checks for different edge cases, such as incomplete responses due to token limits or safety reasons. If a refusal happens, it prints an explanation. Otherwise, it processes and prints the structured output. ### 4. Use Structured Data in a Type-Safe Way When using structured outputs, you can access the parsed JSON response as an object of the type you defined in ‘response_format’. This ensures type safety and lets you directly work with structured data. Example: math_response = completion.choices.message.parsed print(math_response.steps) print(math_response.final_answer) ## How to use Structured Outputs on Gemini The text generated by Gemini is unstructured by default, so you’ll want to look into using Gemini’s structured output functionality.

-----

Phase: [EXPLORATION]

### Source [64]: https://ai.google.dev/gemini-api/docs/structured-output

Query: What accuracy and cost metrics favor Gemini native structured outputs over prompt JSON?

Answer: Note that Gemini 2.0 requires an explicit `propertyOrdering` list within the JSON input to define the preferred structure. You can find an example in this cookbook. `propertyOrdering` ## Structured outputs vs. function calling Both structured outputs and function calling use JSON schemas, but they serve different purposes: | Feature | Primary Use Case | --- | | Structured Outputs | Formatting the final response to the user. Use this when you want the model's answer to be in a specific format (e.g., extracting data from a document to save to a database). | | Function Calling | Taking action during the conversation. Use this when the model needs to ask you to perform a task (e.g., "get current weather") before it can provide a final answer. | ## Best practices [...] Gemini API Gemini API # Structured outputs You can configure Gemini models to generate responses that adhere to a provided JSON Schema. This ensures predictable, type-safe results and simplifies extracting structured data from unstructured text. Using structured outputs is ideal for: In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs make it easy to define schemas using Pydantic (Python) and Zod (JavaScript). ## Structured output examples ### Recipe Extractor This example demonstrates how to extract structured data from text using basic JSON Schema types like `object`, `array`, `string`, and `integer`. `object` `array` `string` `integer` ### Python [...] ## JSON schema support To generate a JSON object, set the `response_format` in the generation configuration. The schema must be a valid JSON Schema that describes the desired output format. `response_format` The model will then generate a response that is a syntactically valid JSON string matching the provided schema. When using structured outputs, the model will produce outputs in the same order as the keys in the schema. Gemini's structured output mode supports a subset of the JSON Schema specification. The following values of `type` are supported: `type` `string` `number` `integer` `boolean` `object` `array` `null` `"null"` `{"type": ["string", "null"]}` These descriptive properties help guide the model: `title` `description` ### Type-specific properties For `object` values:

-----

Phase: [EXPLORATION]

### Source [65]: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs

Query: What accuracy and cost metrics favor Gemini native structured outputs over prompt JSON?

Answer: For Agentic Users, a platform for autonomous agents for the web, the most significant impact and cost savings from using Structured Outputs has been in data extraction. They rely on Pydantic + responseJsonSchema for use cases like extracting attributes related to brand guidelines from image and text examples provided by our users, and parametersJsonSchema for all function declarations. Alkimi AI creates AI assistants for businesses and education institutions grounded in their knowledge. Using JSON Schema they are able to reliably pass data through a guaranteed schema within their multi-stage LLM pipeline. This helps them efficiently automate the configuration of their AI assistants — “Agent Wizard” — for each of their partners. [...] Today, we're announcing enhancements to Structured Outputs in the Gemini API, with expanded support for JSON Schema and better adherence to property ordering in the output. Structured Outputs enable AI models to generate responses that guarantee adherence to a specific schema, which is important for tasks like data extraction and database population. They are also important for agent communication: one agent’s output becomes another’s formatted input, enabling complex multi-agent systems to collaborate without translation layers. ## Expanded JSON Schema support

-----

</details>

<details>
<summary>How do LLM structured outputs improve compliance in financial reporting systems?</summary>

Phase: [EXPLORATION]

### Source [66]: https://www.leewayhertz.com/structured-outputs-in-llms

Query: How do LLM structured outputs improve compliance in financial reporting systems?

Answer: Structured outputs from Large Language Models (LLMs) ensure that AI-generated content meets specific formatting and accuracy requirements. By employing methods such as prompt engineering, function calling, and JSON schema enforcement, these models can produce consistent, reliable and easily interpretable outputs by humans and machines. This structured approach reduces the risk of errors and irrelevant information, known as “hallucinations,” and prepares the data for seamless integration into various systems, such as databases, APIs, and analytical tools. Generating structured outputs in LLMs is particularly valuable in fields like finance, healthcare, and legal services, where precision and clarity are paramount. By combining the linguistic capabilities of LLMs with the precision and predictability of structured data, organizations can achieve new levels of efficiency and reliability in their AI-driven processes. This synergy allows the automation of complex tasks that require both deep language understanding and strict adherence to format, enabling more seamless integration of AI into business operations. Whether it’s generating financial reports, processing legal documents, or analyzing healthcare data, the ability to produce structured outputs from LLMs ensures that AI systems can meet the high standards required in these critical areas.

-----

Phase: [EXPLORATION]

### Source [67]: http://www.stemmpress.com/uploadfile/202511/599c7ec534b3645.pdf

Query: How do LLM structured outputs improve compliance in financial reporting systems?

Answer: First, the findings reveal that LLMs offer significant advantages in automating data processing and improving the accuracy, timeliness, and accessibility of financial reporting. From extracting structured and unstructured financial information to generating narrative disclosures and real-time dashboards, LLMs enable a new paradigm of intelligent, explainable, and dynamic financial reporting systems. Specifically, it examines how LLMs enhance financial reporting through automated data processing and narrative generation; improve financial decision-making and forecasting via intelligent analysis and predictive modeling; and increase audit efficiency by enabling compliance checks, anomaly detection, and risk identification. Because LLMs use advanced language generation techniques to automatically craft textual explanations for financial figures. For example, when summarizing a company's balance sheet, LLMs can generate detailed explanations of the company’s liquidity position, changes in equity, and significant shifts in assets or liabilities. These notes may also include clarifications on depreciation, amortization, or tax liabilities, explaining the underlying assumptions and calculations in layman's terms. Such explanations improve stakeholder understanding and reduce reliance on financial intermediaries. Furthermore, LLMs can be fine-tuned to comply with industry-specific regulatory or reporting standards, ensuring that their narratives remain accurate and audit-friendly.

-----

Phase: [EXPLORATION]

### Source [68]: https://arxiv.org/html/2511.07585v1

Query: How do LLM structured outputs improve compliance in financial reporting systems?

Answer: Task selection: prioritize SQL and summarization over RAG for consistency-critical applications. Structured outputs remain deterministic even at modest temperature increases, while RAG requires strict T=0.0T{=}0.0 for compliance workflows. Audit infrastructure: establish comprehensive audit trails via traces/\.jsonl framework, enabling replay and attestation months after decisions were made. This dual-track approach balances innovation with risk mitigation, allowing institutions to leverage frontier model advances while maintaining regulatory compliance where required. The financial services industry’s adoption of LLMs for operational tasks—from regulatory reporting to client communications—faces a fundamental challenge: nondeterministic outputs that violate audit and compliance requirements. This paper presents the first comprehensive framework for measuring and mitigating LLM output drift in financial deployments, revealing a key insight for model selection: architectural scale inversely correlates with regulatory compliance viability. While T=0.0T{=}0.0 achieves perfect consistency in smaller, well-engineered models (Granite-3-8B, Qwen2.5:7B), larger models like GPT-OSS-120B exhibit 12.5% consistency regardless of configuration. This demonstrates that architectural design and parameter efficiency—not scale alone—determine compliance viability in financial applications.

-----

Phase: [EXPLORATION]

### Source [69]: https://www.workday.com/en-us/topics/ai/llm-finance.html

Query: How do LLM structured outputs improve compliance in financial reporting systems?

Answer: Return on investment (ROI): You need to invest in LLMs to implement them, so they should save money or drive revenue to justify their cost. If an AI-powered process saves 500 manual labor hours monthly, translate that into dollars to see the financial benefit. Efficiency gains: Monitor how much faster LLMs can complete tasks. For example, it’s a clear win if LLMs reduce compliance review times by 60%. Accuracy: Compare the accuracy rates of LLM outputs to previous methods. You should see errors reduce significantly in forecasting, fraud detection, and other areas to know your models are working. LLMs Continuously learn from new data to provide up-to-date insights and refine their capabilities. BI and Traditional Tools Require manual rule updates for refinement. LLMs Fraud detection, compliance monitoring, risk analysis, customer service automation. BI and Traditional Tools Financial reporting, KPI tracking, historical trend analysis. LLMs and traditional tools both have their place in the finance industry. Business intelligence tools handle structured reporting and KPI tracking well. However, the real-time data processing of LLMs makes them more suitable for dynamic tasks such as fraud detection, risk analysis, and compliance monitoring. Enter AI tools. AI helps streamline these tasks through automation, from flagging inconsistencies in compliance reports to identifying patterns that could indicate fraud. That’s part of the reason AI adoption is growing rapidly, with 78% of companies using it for at least one business function. Not all AI tools are created equally, however. Large language models (LLMs) are a type of AI that can process and analyze unstructured data by using neural networks to sift through and find meaning in large datasets. There are many LLM use cases in finance, including risk analysis, financial forecasting, and compliance.

-----

Phase: [EXPLORATION]

### Source [70]: https://www.ema.ai/additional-blogs/addition-blogs/llms-financial-reporting-oversight

Query: How do LLM structured outputs improve compliance in financial reporting systems?

Answer: Can LLMs reliably analyze numbers in financial statements (or do they just handle text)? LLMs excel at natural language and pattern recognition across texts; they can spot narrative–numeric inconsistencies (e.g., optimistic wording with deteriorating cash flows). However, for strict numeric validation (balances, reconciliations), pair LLM outputs with deterministic checks or structured-data models — LLMs alone shouldn’t be the sole verifier of numeric accuracy. Are auditors being replaced by LLMs? No — LLMs are tools to augment auditors. They speed up first-pass reviews, surface anomalies, and summarize large volumes, but auditors retain professional responsibility for judgment, evidence, and audit opinions. LLMs should never operate without human oversight. Audit committees, external auditors, or finance leaders must validate outputs, particularly when high-risk findings could materially affect financial disclosures. (Source: PCAOB research on integrating textual + numeric data in restatement detection.) Ensure Transparent Audit Trails Every AI-driven output should be logged, timestamped, and version-controlled. This enables regulators and internal auditors to trace how insights were generated, improving trust and accountability. Prioritize Explainability and Interpretability Regulatory Interpretation and Compliance Checking Financial reporting involves complex, evolving regulations (e.g., IFRS updates, SEC disclosure requirements). LLMs can map specific reporting language against regulatory standards to highlight gaps or compliance risks. Early-Stage Adoption in Oversight These examples suggest a shift: oversight bodies are no longer just monitoring LLM adoption but actively experimenting with its potential in financial analysis and regulation. When applied responsibly, large language models in financial reporting oversight create tangible benefits for enterprises, auditors, and regulators. Faster, Scalable Oversight

-----

</details>

<details>
<summary>What database schema lessons enhance Pydantic validation for LLM structured data?</summary>

Phase: [EXPLORATION]

### Source [71]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs

Query: What database schema lessons enhance Pydantic validation for LLM structured data?

Answer: Pydantic enhances LLM validation by defining schemas, enforcing data types, and providing error handling for structured outputs. It ensures LLM responses match expected formats, improving reliability and data integrity. The function sends the unstructured text to the LLM with clear formatting instructions, then validates the response against the `BookSummary` schema. LangChain provides built-in support for structured output extraction with Pydantic models. There are two main approaches that handle the complexity of prompt engineering and parsing for you. The first method uses PydanticOutputParser, which works with any LLM by using prompt engineering to guide the model’s output format. The parser automatically generates detailed format instructions from your Pydantic model. The first attempt misses the required `attendees` field, the second attempt includes it but with the wrong type, and the third attempt gets everything correct. The retry mechanism handles these progressive improvements. Pydantic helps you go from unreliable LLM outputs into validated, type-safe data structures. By combining clear schemas with robust error handling, you can build AI-powered applications that are both powerful and reliable. Define clear schemas that match your needs. Validate everything and handle errors gracefully with retries and fallbacks. Use type hints and validators to enforce data integrity. Include schemas in your prompts to guide the LLM. Pydantic helps you validate data at runtime using Python type hints. It checks that LLM outputs match your expected schema, converts types automatically where possible, and provides clear error messages when validation fails. This gives you a reliable contract between the LLM’s output and your application’s requirements. This article shows you how to use Pydantic to validate LLM outputs. You’ll learn how to define validation schemas, handle malformed responses, work with nested data, integrate with LLM APIs, implement retry logic with validation feedback, and more. Before you go ahead, install Pydantic version 2.x with the optional email dependencies: `pip install pydantic[email]`.

-----

Phase: [EXPLORATION]

### Source [72]: https://www.deeplearning.ai/courses/pydantic-for-llm-workflows

Query: What database schema lessons enhance Pydantic validation for LLM structured data?

Answer: Throughout the course, you’ll gain core data validation skills that can be helpful in any software system you build, where you want to pass data from one component to the next. You’ll also learn how modern frameworks and LLM providers support structured outputs and function calls using Pydantic under the hood. Learn the basics of Pydantic, and practice different approaches for getting structured data from Pydantic models. Validate user input, catching issues like badly formatted emails or missing fields before they cause problems. Use Pydantic data models directly in your API calls to different LLM providers and agent frameworks as a reliable way to get a structured response. Combine structured outputs and tool-calling with Pydantic models in your application. Use Pydantic to generate structured outputs from LLMs, ensuring the responses follow a specific format that your application can reliably process. Learn data validation skills to handle a wide variety of data formatting and structuring needs in any software system. Build a system with data validation at every stage, using Pydantic models to validate everything from user input and LLM responses to defining the parameters for tool-calling. Pydantic is one of the most popular data validation frameworks out there. It sees over 300 million downloads a month, making it also one of the most popular Python packages, and that’s because data validation is at the core of any application. By the end of the course, you’ll be able to build LLM-powered applications where every step is structured, validated, and ready to plug into your workflow. If you’re comfortable with basic Python and curious about how real-world AI systems pass data between components, this course will help you get started with one of the most important tools in the modern AI stack. 8 Lessons· 6 Code Examples. Welcome to Pydantic for LLM workflows. Introduction to Pydantic for LLM workflows.

-----

Phase: [EXPLORATION]

### Source [73]: https://pydantic.dev/articles/llm-intro

Query: What database schema lessons enhance Pydantic validation for LLM structured data?

Answer: While some have resorted to threatening human life to generate structured data, we have found that Pydantic is even more effective. In this post, we will discuss validating structured outputs from language models using Pydantic and OpenAI. We’ll show you how to write reliable code. Additionally, we’ll introduce a new library called instructor that simplifies this process and offers extra features to leverage validation to improve the quality of your outputs. Unlike libraries like `dataclasses`, `Pydantic` goes a step further and defines a schema for your dataclass. This schema is used to validate data, but also to generate documentation and even to generate a JSON schema, which is perfect for our use case of generating structured data with language models! `pip install instructor`. The example we provided above is somewhat contrived, but it illustrates how Pydantic can be utilized to generate structured data from language models. Now, let’s employ Instructor to streamline this process. Instructor is a compact library that enhances the OpenAI client by offering convenient features. In the upcoming blog post, we will delve into reasking and validation. However, for now, let’s explore a practical example. While this post focuses on OpenAI, using Pydantic is not limited to OpenAI. You can use it for many language models that support the OpenAI API, including Mistral on Anyscale. `{"rewritten_query": "novel developments advancements ai artificial intelligence machine learning", "published_daterange": {"start": "2023-09-17", "end": "2021-06-17"}, "domains_allow_list": ["arxiv.org"]}`. If we peek under the hood, we can see that the query is actually a complex object, with a date range, and a list of domains to search in. We can model this structured output in Pydantic using the instructor library. `from typing import List import datetime from pydantic import BaseModel class DateRange(BaseModel): start: datetime.date end: datetime.date class SearchQuery(BaseModel): rewritten_query: str published_daterange: DateRange domains_allow_list: List[str] async def execute(): # Return the search results of the rewritten query return api.search(json=self.model_dump())`

-----

Phase: [EXPLORATION]

### Source [74]: https://www.freecodecamp.org/news/how-to-keep-llm-outputs-predictable-using-pydantic-validation

Query: What database schema lessons enhance Pydantic validation for LLM structured data?

Answer: Frameworks like LangChain and FastAPI work smoothly with Pydantic. In LangChain, you can define tool or agent schemas using Pydantic classes to ensure all interactions between the model and tools are consistent. In FastAPI, every endpoint can accept and return Pydantic models. This makes it perfect for AI APIs where model responses are validated automatically before being sent to clients. When you start validating outputs, you will quickly notice patterns in how your LLM fails. Sometimes it adds extra commentary, sometimes it confuses key names. This is especially useful in retrieval-augmented generation (RAG) pipelines, where structured outputs such as document scores or entities are crucial for maintaining accurate context. Pydantic brings structure to the chaos of LLM outputs. It turns unpredictable text generation into predictable, schema-checked data. By validating model responses, you make your AI workflows reliable, debuggable, and safe for production. The combination of LLM flexibility and Pydantic’s strict typing is powerful. You get the creativity of language models with the control of data validation. When every output follows a schema, your AI becomes not just intelligent, but dependable. Suppose you are using OpenAI’s API. You can ask the model to return structured data and then validate it using Pydantic, like this: import from import from importclass ReviewSummary(BaseModel): class ReviewSummary BaseModel"Summarize this review and return JSON with keys: summary, sentiment.\n\nReview: The phone is fast but battery drains quickly.""gpt-4o-mini" try except as"Validation failed:". Here, the model’s response goes through two stages. First, it is parsed from text into JSON. Then Pydantic checks if it matches the expected schema. If something is missing, it throws an error. You can catch that and decide how to handle it. Pydantic makes AI Apps Safer.

-----

Phase: [EXPLORATION]

### Source [75]: https://xebia.com/blog/enforce-and-validate-llm-output-with-pydantic

Query: What database schema lessons enhance Pydantic validation for LLM structured data?

Answer: The prompt will now look like this: I will ask you questions, and you will respond. Your response should be in the following format: ```json { "properties": { "thought": { "title": "Thought", "type": "string" }, "answer": { "title": "Answer", "type": "string" } }, "required": ["thought", "answer"], "title": "ThoughtAnswerResponse", "type": "object" } ``` The response will look like this: { "thought": "The largest planet in our solar system is Jupiter.", "answer": "Jupiter" }. Now, whenever you change the Pydantic model, the corresponding schema will be put in the prompt. Note that the schema has become more complex than it was before. One benefit is that it allows us to be more specific in what responses we require. Error handling. prompt = """Your response should be in the following format: ```json { "thought": "How you think about the question", "answer": "The answer to the question", "difficulty": "How difficult the question was. One of easy, medium or hard" } ``` """. Of course, the model could potentially still use other values. To validate it, we would need to write custom code. With Pydantic, it is a lot easier. We create a new type called `Difficulty` using a Literal. A Literal allows us to specify the use of a select list of values. We add a `Difficulty` type hint to the `difficulty` field in our Pydantic model: from typing import Literal from pydantic import BaseModel # We create a new type Difficulty = Literal["easy", "medium", "hard"] class ThoughtAnswerResponse(BaseModel): thought: str answer: str difficulty: Difficulty. The LLM responds may respond with a value we do not allow: { "thought": "The largest planet in our solar system is Jupiter.", "answer": "Jupiter", "difficulty": "Unknown" }. When we parse this result, Pydantic will validate the values for the `difficulty` field. `Unknown` does not match one of the values specified in the Literal type we have defined. So we get the following error.

-----

</details>

<details>
<summary>How is structured output adoption reshaping autonomous AI agent communication protocols?</summary>

Phase: [EXPLORATION]

### Source [76]: https://arxiv.org/html/2504.16736v2

Query: How is structured output adoption reshaping autonomous AI agent communication protocols?

Answer: Structured output adoption reshapes autonomous AI agent communication by enabling efficient, context-aware protocols and enhancing interoperability across diverse systems. Protocols like AITP and ACP standardize interactions, ensuring secure, structured exchanges. Structured outputs improve clarity and reduce ambiguity in agent communications. In order to address the Agent Communication Trilemma, Agora leverages the capabilities of LLMs in natural language understanding, code generation, and autonomous negotiation, thereby enabling agents to adopt various communication protocols based on context. Frequent communications employ structured protocols to ensure efficiency, while infrequent ones rely on structured data with routines generated by the LLM. In the event of rare communications or failures, LLM agents transition to natural language, a change that can also facilitate protocol negotiation. Agora introduces Protocol Documents (PDs), which are plain-text protocol descriptions that allow agents to autonomously negotiate, implement, adapt, and even create new protocols without human intervention. The AITP enables AI agents to communicate securely across trust boundaries, while providing extensible mechanisms for structured interactions. It supports autonomous, secure communication, negotiation, and value exchange between agents belonging to different organizations or individuals. For example, in a flight booking scenario, a personal assistant agent can use AITP to directly interact with airline booking agents to exchange flight, passenger, and payment information, instead of navigating airline websites. In AITP, agents communicate through Threads, which are transmitted over a Transport layer, and exchange structured data via Capabilities tailored to specific operations. What distinguishes AITP is its explicit focus on enabling agent interactions across trust boundaries, addressing Agent protocols are standardized frameworks that define the rules, formats, and procedures for structured communication among agents and between agents and external systems. Compared to traditional interaction mechanisms—such as APIs, graphical user interfaces (GUIs), or XML-based interactions—protocols exhibit significant advantages, as summarized in Table1. Unlike APIs, which are efficient but often lack operational flexibility and standardization, or GUIs, which provide user-friendly standardized interfaces but are limited in efficiency and not inherently AI-native, protocols combine the benefits of high efficiency, extensive operational scope, robust standardization, and native compatibility with AI systems. XML-based methods, primarily intended for browser-based interactions.

-----

Phase: [EXPLORATION]

### Source [77]: https://docs.ag2.ai/latest/docs/use-cases/notebooks/notebooks/agentchat_structured_outputs

Query: How is structured output adoption reshaping autonomous AI agent communication protocols?

Answer: Structured output adoption reshapes autonomous AI agent communication by enabling efficient, context-aware protocols and enhancing interoperability across diverse systems. Protocols like AITP and ACP standardize interactions, ensuring secure, structured exchanges. Structured outputs improve clarity and reduce ambiguity in agent communications. Normal function calling still works alongside structured output, so your agent can have a response format while still calling tools. LLM providers offer functionality for defining a structure of the messages generated by LLMs, AG2 enables this functionality by propagating a `response_format`, in the LLM configuration for your agents, to the underlying client. Structured outputs are available for a number of Model Providers, see the `Supported model providers` section below. In this example we will use OpenAI as the model provider. Using structured output, we can enforce chain-of-thought reasoning in the model to output an answer in a structured, step-by-step way. First we will define the math reasoning model. This model will indirectly force the LLM to solve the posed math problems iteratively through math reasoning steps.

-----

Phase: [EXPLORATION]

### Source [78]: https://learn.microsoft.com/en-us/agent-framework/agents/structured-outputs

Query: How is structured output adoption reshaping autonomous AI agent communication protocols?

Answer: Structured output adoption reshapes autonomous AI agent communication by enabling efficient, context-aware protocols and enhancing interoperability across diverse systems. Protocols like AITP and ACP standardize interactions, ensuring secure, structured exchanges. Structured outputs improve clarity and reduce ambiguity in agent communications. Some agents don't natively support structured outputs, either because it's not part of the protocol or because the agents use language models without structured outputs capabilities. One possible approach is to create a custom decorator agent that wraps any `AIAgent` and uses an additional LLM call via a chat client to convert the agent's text response into structured JSON. Since this approach relies on an additional LLM call to transform the response, its reliability may not be sufficient for all scenarios. For a reference implementation of this pattern that you can adapt to your own requirements, see the StructuredOutputAgent sample. OpenAI Responses Client with Structured Outputs Example This sample demonstrates using structured outputs capabilities with OpenAI Responses Client, showing Pydantic model integration for type-safe response parsing and data extraction.

-----

Phase: [EXPLORATION]

### Source [79]: https://www.linkedin.com/posts/brijpandeyji_10-modern-ai-agent-protocols-you-should-know-activity-7354910038961860608-4RCT

Query: How is structured output adoption reshaping autonomous AI agent communication protocols?

Answer: Structured output adoption reshapes autonomous AI agent communication by enabling efficient, context-aware protocols and enhancing interoperability across diverse systems. Protocols like AITP and ACP standardize interactions, ensuring secure, structured exchanges. Structured outputs improve clarity and reduce ambiguity in agent communications. 10 Modern AI Agent Protocols You Should Know About Over the past few months, a range of protocols have emerged to standardize how AI agents communicate, collaborate, and function. As systems grow more autonomous, having defined protocols is no longer optional — it's essential. This visual summarizes 10 of the most prominent AI agent protocols shaping the future of intelligent systems: ACP (IBM) – Defines standard interfaces for agent interaction and lifecycle management AGP (Industry) – Enables message transformation and access control between agents and external systems A2A (Google) – Powers structured communication in multi-agent environments like Gemini and Project Astra MCP (Anthropic) – A unified model context protocol for memory injection and tool usage in LLMs TAP use semantic web concepts – structured “protocol documents” and multi-layer negotiation rules – so agents can discover each other and negotiate work dynamically. Yet, fragmentation remains. Many agents still “talk” over plain HTTP with ad-hoc formats. The dream of a universal agent contract — a WSDL for AIs — is still just that, a dream. On the upside, safety is front and center. These frameworks embed guardrails to ensure agents act safely and predictably — validating outputs, enforcing workflow integrity, and maintaining alignment.

-----

Phase: [EXPLORATION]

### Source [80]: https://arxiv.org/html/2505.02279v1

Query: How is structured output adoption reshaping autonomous AI agent communication protocols?

Answer: Structured output adoption reshapes autonomous AI agent communication by enabling efficient, context-aware protocols and enhancing interoperability across diverse systems. Protocols like AITP and ACP standardize interactions, ensuring secure, structured exchanges. Structured outputs improve clarity and reduce ambiguity in agent communications. All requests and responses conform to ACP’s Message Structure, which standardizes the communication envelope. Each message is an ordered list of parts, with explicit MIME content_type annotations and either embedded content or dereferenceable content_url values. Optional name attributes enable the use of semantically tagged Artifacts, facilitating downstream interpretation. Finally, the result of agent execution is encapsulated in one or more Artifacts. These may consist of structured JSON outputs, plain text completions, binary files, or even nested message references. Artifacts are delivered as part of the Message Structure response and are subsequently rendered, stored, or chained into additional agent workflows, ensuring extensibility and composability across ACP-enabled systems.

-----

</details>

<details>
<summary>How did XML-based data extraction evolve into modern LLM schema-driven outputs?</summary>

Phase: [EXPLORATION]

### Source [81]: https://bytetunnels.com/posts/llm-powered-data-extraction-schema-driven-scraping-with-structured-output

Query: How did XML-based data extraction evolve into modern LLM schema-driven outputs?

Answer: The biggest change in web scraping over the past year has not been a new browser automation framework or a faster HTTP client. It has been schema-driven LLM extraction – a pattern where you define the exact structure of the data you want and let a language model figure out how to pull it from raw HTML. For a comparison of which models perform best at this, see our guide to the best LLMs for structured data extraction. No more writing CSS selectors that break when a site redesigns. No more maintaining XPath expressions for every edge case. You describe the output, and the LLM delivers it. The `Field(description=...)` annotations are not just documentation. They become part of the prompt sent to the LLM, guiding the model on what each field means and where to look for it. With your schema defined, extraction is a single API call. Modern LLM APIs support structured output natively, meaning the model is constrained to return valid JSON matching your schema. For high-volume, recurring extraction from stable sites, the hybrid approach – where an LLM generates selectors that a traditional scraper executes – offers the best of both worlds. The schema-driven extraction pattern is maturing fast. Costs are dropping as models get cheaper and DOM pruning techniques improve. Accuracy is already production-grade for most use cases. And the developer experience of defining what you want rather than how to get it is a real improvement in making web data accessible.

-----

Phase: [EXPLORATION]

### Source [82]: https://simonw.substack.com/p/structured-data-extraction-from-unstructured

Query: How did XML-based data extraction evolve into modern LLM schema-driven outputs?

Answer: Outputs: `{"name": "Zap", "age": 5, "short_bio": ...}` Combining that with the `--schema` option is where things get really interesting. You can specify a schema using any of the mechanisms described earlier, which means you can see ALL of the data gathered using that schema by combining `--data` with `--schema X` (and `-n 0` for everything). `--schema` `--data` `--schema X` `-n 0` Here are all of the dogs I've invented: `llm logs --schema 'name,age int,short_bio' --data -n 0` Output (here truncated): `{"name": "Zap", "age": 5, "short_bio": "Zap is a futuristic ..."} {"name": "Zephyr", "age": 3, "short_bio": "Zephyr is an adventurous..."} {"name": "Zylo", "age": 4, "short_bio": "Zylo is a unique ..."} LLM already defaults to logging every prompt and response it makes to a SQLite database - mine contains over 4,747 of these records now, according to this query: `sqlite3 "$(llm logs path)" 'select count() from responses'` With schemas, an increasing portion of those are valid JSON. Since LLM records the schema that was used for each response - using the schema ID, which is derived from a content hash of the expanded JSON schema - it’s now possible to ask LLM for all responses that used a particular schema: `llm logs --schema 3b7702e71da3dd791d9e17b76c88730e --short` I got back: [...] Designing this feature for LLM Reusing schemas and creating templates Doing more with the logged structured data Using schemas from LLM's Python library What’s next for LLM schemas? #### Structured data extraction is a killer app for LLMs I’ve suspected for a while that the single most commercially valuable application of LLMs is turning unstructured content into structured data. That’s the trick where you feed an LLM an article, or a PDF, or a screenshot and use it to turn that into JSON or CSV or some other structured format. It’s possible to achieve strong results on this with prompting alone: feed data into an LLM, give it an example of the output you would like and let it figure out the details.

-----

Phase: [EXPLORATION]

### Source [83]: https://simonwillison.net/2025/Feb/28/llm-schemas

Query: How did XML-based data extraction evolve into modern LLM schema-driven outputs?

Answer: Outputs: ``` "name" "Zap" " " "age" 5 "short_bio" ``` Combining that with the `--schema` option is where things get really interesting. You can specify a schema using any of the mechanisms described earlier, which means you can see ALL of the data gathered using that schema by combining `--data` with `--schema X` (and `-n 0` for everything). Here are all of the dogs I’ve invented: ``` 'name,age int,short_bio' ' ' ``` Output (here truncated): ``` "name" "Zap" " " "age" 5 "short_bio""Zap is a futuristic ..." " " "name" "Zephyr" " " "age" 3 "short_bio""Zephyr is an adventurous..." " " "name" "Zylo" " " "age" 4 "short_bio""Zylo is a unique ..." " " ``` Some schemas gather multiple items, producing output that looks like this (from the tutorial): [...] ``` "$(llm logs path)" "$(llm logs path)$() "'select count() from responses' ' '" ``` With schemas, an increasing portion of those are valid JSON. Since LLM records the schema that was used for each response—using the schema ID, which is derived from a content hash of the expanded JSON schema—it’s now possible to ask LLM for all responses that used a particular schema: ``` llm logs --schema 3b7702e71da3dd791d9e17b76c88730e --short ``` I got back: [...] Structured data extraction is a killer app for LLMs Designing this feature for LLM Reusing schemas and creating templates Doing more with the logged structured data Using schemas from LLM’s Python library What’s next for LLM schemas? #### Structured data extraction is a killer app for LLMs I’ve suspected for a while that the single most commercially valuable application of LLMs is turning unstructured content into structured data. That’s the trick where you feed an LLM an article, or a PDF, or a screenshot and use it to turn that into JSON or CSV or some other structured format. It’s possible to achieve strong results on this with prompting alone: feed data into an LLM, give it an example of the output you would like and let it figure out the details.

-----

Phase: [EXPLORATION]

### Source [84]: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/ExtractLabel-Schema-driven-unstructured-data-extraction-with/ba-p/5172267

Query: How did XML-based data extraction evolve into modern LLM schema-driven outputs?

Answer: Most enterprise data lives in free text - tickets, contracts, feedback, clinical notes, and more. It holds critical information but doesn't fit into the structured tables that pipelines expect. Traditionally, extracting structure meant rule-based parsers that break with every format to change, or custom NLP models that take weeks to build. LLMs opened new possibilities, but on their own they bring inconsistent outputs, no type of enforcement, and results that vary between runs. What production workflows need is LLM intelligence with structured-output guarantees, delivered inside the data platform teams already use. [...] Figure: Schema field mapping The challenge is getting an LLM to do this reliably across hundreds of thousands of claims - returning every result in the same shape, with the same field names, the same value types, and constrained to valid categories. That’s exactly what ExtractLabel is designed for. You define a schema that captures all these elements in a single structured object. The model reads the text, identifies each piece of information, and returns it in the exact shape you specified. ## Building the schema

-----

Phase: [EXPLORATION]

### Source [85]: https://medium.com/@emrekaratas-ai/structured-output-generation-in-llms-json-schema-and-grammar-based-decoding-6a5c58b698a6

Query: How did XML-based data extraction evolve into modern LLM schema-driven outputs?

Answer: > the model’s response must follow a specific format or schema so that machines can parse it reliably. As LLM applications evolve (e.g. agents that generate code, call functions, or control robots), the need for structured outputs (JSON, SQL, Python code, etc.) has become more pronounced​. > > Unlike freeform text meant for humans, these structured outputs are consumed by programs, which means any deviation or syntax error can break an entire pipeline​. [...] Interoperability: JSON is a ubiquitous data format. By adhering to a schema, the model’s output _becomes immediately usable by any tool or service that understands JSON_. This is especially useful in APIs— for instance, an API endpoint can define a JSON Schema for valid requests, and your LLM can produce a response that matches it, allowing direct API calls without intermediate transformation. Reliability in Pipelines: Incomplex pipelines (say, an LLM reads a document and outputs structured results for another program to consume), schema-constrained output improves reliability._There’s less room for the LLM to go off-script._ This can improve the overall robustness of multi-step systems since each piece of data is exactly where it’s supposed to be. [...] ### How does it work in practice? The simplest way is to include the schema in the prompt or instructions, telling the model to output JSON that fits that schema. For example, you might prompt: _“Extract the movie title and rating from this review and output them as JSON with the following schema:_`{...schema here...}`_.”_ In many cases, _a sufficiently capable LLM will follow the pattern_ and give a compliant JSON. _However, just prompting the schema has limitations_ – if the model isn't highly reliable or the schema is complex, it might still make mistakes in format​.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="getting-structured-json-responses-from-llms-a-simple-solutio.md">
<details>
<summary>Getting Structured JSON Responses from LLMs: A Simple Solution</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://python.plainenglish.io/getting-structured-json-responses-from-llms-a-simple-solution-f819fc389ebc>

# Getting Structured JSON Responses from LLMs: A Simple Solution

[https://miro.medium.com/v2/resize:fill:64:64/1*qD2FtfAnF9wPiNr03s2Urw.png](https://brianward1428.medium.com/?source=post_page---byline--f819fc389ebc---------------------------------------)

[Brian Ward](https://brianward1428.medium.com/?source=post_page---byline--f819fc389ebc---------------------------------------)

3 min read

·

Jul 21, 2025

When working with Large Language Models (LLMs) I always find that I just want consistent, structured responses so that I can integrate them into a programatic workflow. LLMs love to be chatty — they’ll give you explanations, add formatting, include disclaimers, and wrap your actual data in conversational fluff. But when you’re building applications, you need reliable, parseable data.

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*vCrByq5zlQxNLy1D3bOLDg.png

This isn’t a fool proof method, but it works well enough for me across various models. Hope it can help some of you get started.

````
# The Solution: A Robust JSON Prompt Function
# Here's a Python function that handles this problem by enforcing structured responses and validating the output:
def prompt_json(prompt: str, expected_fields: list[str]) -> dict | None:
    """
    Send a prompt to the LLM expecting a JSON response with specific fields.
    Returns the parsed JSON dict if successful and all fields are present, else None.
    """
    try:
        # make call to any llm
        response = prompt_openai(prompt)

        # Check for error responses
        if response.startswith("Error:"):
            return None

        # Clean the response (remove markdown, explanations, etc.)
        cleaned = self.clean_llm_json_response(response)
        if response:
            response = response.replace('```', '').replace('json', '').strip()

        # Parse JSON
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError:
            return None

        # Validate structure
        if not isinstance(data, dict):
            return None

        # Check for required fields
        missing = [field for field in expected_fields if field not in data]
        if missing:
            return None

        return data

    except Exception:
        return None
````

Of course the other requirement for success is being explicit in your prompt about the format you want. Here’s an effective pattern:

```
prompt = f"""Here is some metadata about a YouTube video about influencer marketing.Please do the following:
1. Create a description (1-5 sentences)
2. Rate your confidence level (1-10)

Return the output in raw JSON format only.
Example output:
{{
    "description": "Description of the content",
    "confidence": 8
}}
---
{str({"title": title, "description": description})}"""
# Usage
result = prompt_json(prompt, expected_fields=["description", "confidence"])
if result:
    print(f"Description: {result['description']}")
    print(f"Confidence: {result['confidence']}")
else:
    print("Failed to get valid JSON response")
```

## Key Benefits

1.  **Reliability**: The function validates both JSON structure and required fields
2.  **Error Handling**: Returns `None` on any failure, making error handling simple
3.  **Flexibility**: Works with any LLM provider by swapping the underlying API call
4.  **Validation**: Ensures you get exactly the fields you expect

## Pro Tips

-   Always include a concrete example in your prompt
-   Use “raw JSON format only” to discourage extra formatting
-   Validate required fields to catch incomplete responses
-   Consider retry logic for critical applications

This approach transforms unreliable LLM text generation into a dependable structured data extraction tool. No more parsing markdown code blocks or dealing with chatty responses — just clean, validated JSON every time. Good Luck!

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="going-deeper-with-pydantic-nested-models-and-data-structures.md">
<details>
<summary>going-deeper-with-pydantic-nested-models-and-data-structures</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://dev.to/mechcloud_academy/going-deeper-with-pydantic-nested-models-and-data-structures-4e24>

In the [previous](https://dev.to/mechcloud_academy/getting-started-with-pydantic-type-safe-data-models-in-python-2141) post, we explored the basics of Pydantic: creating models, enforcing type validation, and ensuring data integrity with minimal boilerplate. But real-world applications often involve more complex, structured data—like API payloads, configuration files, or nested JSON. How do we handle a blog post with comments, an order with multiple items, or a user profile with nested addresses? This post dives into Pydantic’s powerful support for nested models and smart data structures, showing how to model, validate, and access complex data with ease.

We’ll cover practical examples, including a blog system with authors and comments, and touch on use cases like user profiles or e-commerce orders. Let’s get started!

## Nested BaseModels

Pydantic allows you to define models within models, enabling clean, hierarchical data structures. Let’s model a blog system with an `Author`, `Comment`, and `Blog` model.

```
from pydantic import BaseModel
from datetime import datetime

class Author(BaseModel):
    name: str
    email: str

class Comment(BaseModel):
    content: str
    author: Author
    created_at: datetime

class Blog(BaseModel):
    title: str
    content: str
    author: Author
    comments: list[Comment] = []

# Example usage
blog_data = {
    "title": "Nested Models in Pydantic",
    "content": "This is a blog post about Pydantic...",
    "author": {"name": "Jane Doe", "email": "jane@example.com"},
    "comments": [\
        {\
            "content": "Great post!",\
            "author": {"name": "John Smith", "email": "john@example.com"},\
            "created_at": "2025-05-04T10:00:00"\
        }\
    ]
}

blog = Blog(**blog_data)
print(blog.author.name)  # Jane Doe
print(blog.comments[0].author.email)  # john@example.com
```

Here, `Comment` and `Blog` embed the `Author` model, and Pydantic automatically validates the nested data. If `author.email` is invalid (e.g., not a string), validation fails before the model is instantiated. This cascading validation ensures every layer of your data is correct.

## Lists, Tuples, and Sets of Models

Nested models often involve collections, like a list of comments on a blog. Pydantic supports `List[T]`, `Tuple[T, ...]`, and `Set[T]` for collections of models or other types.

Using our `Blog` model, notice the `comments: list[Comment] = []`. Pydantic validates each `Comment` in the list:

```
invalid_comment_data = {
    "title": "Invalid Comment Example",
    "content": "This blog has a bad comment...",
    "author": {"name": "Jane Doe", "email": "jane@example.com"},
    "comments": [\
        {\
            "content": "This is fine",\
            "author": {"name": "John Smith", "email": "john@example.com"},\
            "created_at": "2025-05-04T10:00:00"\
        },\
        {\
            "content": "This is bad",\
            "author": {"name": "Bad Author", "email": "not-an-email"},  # Invalid email\
            "created_at": "2025-05-04T10:01:00"\
        }\
    ]
}

try:
    blog = Blog(**invalid_comment_data)
except ValueError as e:
    print(e)
```

Pydantic will raise a `ValidationError` pinpointing the invalid email in the second comment. You can also use `Tuple[Comment, ...]` for immutable sequences or `Set[Comment]` for unique items, and validation works the same way.

## Optional Fields and Defaults

Real-world data often includes optional fields or defaults. Pydantic supports `Optional[T]` from `typing` and allows default values.

```
from typing import Optional

class Author(BaseModel):
    name: str
    email: Optional[str] = None  # Email is optional
    bio: str = "No bio provided"  # Default value

class Blog(BaseModel):
    title: str
    content: str
    author: Author

# Example with missing email
blog_data = {
    "title": "Optional Fields",
    "content": "This blog has an author with no email.",
    "author": {"name": "Jane Doe"}
}

blog = Blog(**blog_data)
print(blog.author.email)  # None
print(blog.author.bio)    # No bio provided
```

`Optional[str]` means the field can be `None` or a string, while `email: str = None` implies the field is optional but defaults to `None`. Pydantic distinguishes between missing fields (not in the input) and fields explicitly set to `None`, ensuring precise control over data parsing.

## Dict and Map-Like Structures

Pydantic supports `Dict[K, V]` for key-value structures, perfect for feature flags, localized content, or other mappings.

```
from typing import Dict

class Blog(BaseModel):
    title: str
    content: str
    translations: Dict[str, str]  # Language code -> translated title

blog_data = {
    "title": "Pydantic Power",
    "content": "This is a blog post...",
    "translations": {
        "es": "El poder de Pydantic",
        "fr": "La puissance de Pydantic"
    }
}

blog = Blog(**blog_data)
print(blog.translations["es"])  # El poder de Pydantic
```

You can also nest models in dictionaries, like `Dict[str, Author]`, for more complex mappings. Pydantic validates both keys and values according to their types.

## Accessing Nested Data Safely

Once validated, Pydantic models provide type-safe access to nested attributes. You can access fields like `blog.author.name` or `blog.comments[0].content` without worrying about `KeyError` or `AttributeError`.

For serialization, use `.dict()` (or `.model_dump()` in Pydantic V2) with options like `exclude_unset`, `include`, or `exclude`:

```
# Serialize only specific fields
print(blog.dict(include={"title", "author": {"name"}}))
# Output: {'title': 'Pydantic Power', 'author': {'name': 'Jane Doe'}}

# Exclude unset fields
blog = Blog(
    title="Test",
    content="Content",
    author=Author(name="Jane")
)
print(blog.dict(exclude_unset=True))
# Only includes fields explicitly set, skips defaults like author.bio
```

This makes it easy to control what data is serialized for APIs or storage.

## Validation and Error Reporting in Nested Structures

Pydantic’s error reporting is precise, even for nested data. Let’s revisit the invalid comment example:

```
try:
    blog = Blog(**invalid_comment_data)
except ValueError as e:
    print(e.errors())
```

Output might look like:

```
[\
    {\
        'loc': ('comments', 1, 'author', 'email'),\
        'msg': 'value is not a valid email address',\
        'type': 'value_error.email'\
    }\
]
```

The `loc` field shows the exact path to the error (`comments[1].author.email`), making it easy to debug complex structures. This granularity is invaluable for APIs or user-facing validation.

## Recap and Takeaways

Nested models in Pydantic make it easy to handle complex, structured data with robust validation. Key techniques:

- Use `BaseModel` for nested structures like `Author` in `Blog`.
- Leverage `List[T]`, `Dict[K, V]`, and `Optional[T]` for flexible data shapes.
- Access nested data safely with dot notation or serialize with `.dict()`.
- Rely on Pydantic’s detailed error reporting for debugging.

These tools are perfect for APIs, configuration files, or any scenario with hierarchical data.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="issue-128-structured-llm-outputs-with-pydantic.md">
<details>
<summary>Issue #128 - Structured LLM Outputs with Pydantic</summary>

Phase: [EXPLORATION]

**Source URL:** <https://mlpills.substack.com/p/issue-128-structured-llm-outputs>

# Issue #128 - Structured LLM Outputs with Pydantic

# 💊 Pill of the week

When you call an LLM, you get back text. That’s great for chat, but terrible for pipelines. The moment you need to feed the model’s output into another system — a database, a dashboard, a downstream agent — you need structure. Regex parsing? Fragile. Manual JSON parsing? The model will eventually return prose with a JSON block wrapped in markdown fences, or worse, trailing commentary like _“Sure! Here’s the JSON you asked for_ 😊 _”_.

`PydanticOutputParser` solves this elegantly. You define your schema with Pydantic, LangChain injects that schema into your prompt as format instructions, and you get back a validated Python object. It plays beautifully with LCEL, the whole thing is one composable expression.

Let’s walk through a **real example**: processing a job interview transcript into a structured candidate evaluation. But first, two terms you'll see throughout the article.

## The two pieces you need to know

Before we build anything, let's pin down the two names you'll see throughout the article. Neither is complicated on its own — the interesting part is what they do together.

`PydanticOutputParser` is a LangChain output parser that wraps a Pydantic model class. It generates JSON-schema format instructions to inject into your prompt, then parses the LLM’s text response and validates it against your model. You get back a typed Pydantic instance on success, or an `OutputParserException` when the model’s output doesn’t conform.

**LCEL (LangChain Expression Language)** is a declarative syntax for composing LangChain components with the `|` pipe operator — `prompt | model | parser`. Every component is a `Runnable`, so the composed chain inherits `.invoke()`, `.batch()`, `.stream()`, and their async variants for free. No boilerplate, no custom orchestration.

One defines the _shape_ of what you want, the other defines _how_ the pieces connect. Together, they turn a messy LLM call into a typed, composable, batchable pipeline.

## The setup

The whole pipeline needs just three imports from LangChain. Everything else — the heavy lifting for validation, constraints, and schema definition — comes from Pydantic, which is already a transitive dependency of LangChain. No extra installs, no configuration dance.

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
```

That’s all you need from LangChain. The rest is Pydantic.

## The schema

The schema is the heart of the whole setup. It serves double duty — as a runtime data contract _and_ as the instructions you send to the model. Get this right and the rest is almost mechanical. Before writing ours, a quick reminder of what Pydantic actually is and why it's the right tool here.

**Pydantic:** A Python library for data validation using type hints. You declare classes that inherit from `BaseModel`, annotate fields with types and constraints via `Field(...)`, and Pydantic validates incoming data against that schema at runtime — raising informative errors when something doesn’t match. It’s the de facto standard for data validation in modern Python and the backbone of FastAPI, LangChain, and most agent frameworks.

Every Pydantic feature you’d use normally works here. Enums constrain outputs to a fixed set of values. `Field` with `ge`/`le`/`gt`/`lt` enforces numeric ranges. `min_length`/`max_length` controls string and list sizes. Nested models give you hierarchical structure. And crucially — the `description` parameter in `Field` ends up in the prompt. It’s not just documentation, it’s instructions to the model.

https://substackcdn.com/image/fetch/$s_!CPkM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe80f8aa6-fb4f-4fbb-b5ab-6cb44724b878_1392x1034.png

```
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator

# Enums — constrain the model to a fixed set of string values.
# Inheriting from `str` makes them JSON-serializable and lets the
# parser match plain strings coming back from the LLM.
class ProfileLevel(str, Enum):
    JUNIOR = "junior"
    MID = "mid"
    SENIOR = "senior"
    STAFF = "staff"
    PRINCIPAL = "principal"

class Recommendation(str, Enum):
    STRONG_HIRE = "strong_hire"
    HIRE = "hire"
    NO_HIRE = "no_hire"
    STRONG_NO_HIRE = "strong_no_hire"

# Nested model — each technical topic discussed gets its own
# structured record instead of a flat list of strings.
class TopicDiscussion(BaseModel):
    topic: str = Field(description="Technical topic or concept discussed")
    proficiency_score: int = Field(
        ge=1, le=10,
        description="Candidate's proficiency on this topic (1-10)"
    )
    notes: str = Field(
        max_length=200,
        description="Brief note on how the candidate handled this topic"
    )

# Another nested model — scores grouped as their own object rather
# than polluting the top-level schema with five int fields.
class Scores(BaseModel):
    communication: int = Field(ge=0, le=10)
    technical_skills: int = Field(ge=0, le=10)
    problem_solving: int = Field(ge=0, le=10)
    cultural_fit: int = Field(ge=0, le=10)
    leadership: int = Field(
        ge=0, le=10,
        description="Score 0 if leadership was not assessed"
    )

class InterviewEvaluation(BaseModel):
    # Plain strings with descriptions — the description becomes
    # part of the format instructions injected into the prompt.
    candidate_name: str = Field(description="Full name as stated in the transcript")
    position: str = Field(description="Position the candidate is interviewing for")

    # Enum fields — the parser validates the string against the enum values.
    profile_level: ProfileLevel = Field(
        description="Seniority level inferred from experience and discussion depth"
    )
    recommendation: Recommendation

    # Nested BaseModel — produces a nested JSON object in the output.
    scores: Scores = Field(description="Scores across evaluation dimensions")

    # Numeric constraints: `gt`/`lt` are exclusive, `ge`/`le` are inclusive.
    years_of_experience: float = Field(
        gt=0, lt=50,
        description="Total professional years of experience"
    )

    # Constrained string — forces the model to write a real summary,
    # not a one-liner and not an essay.
    summary: str = Field(
        min_length=100, max_length=500,
        description="Executive summary of the interview"
    )

    # Constrained list — minimum and maximum number of items.
    key_strengths: List[str] = Field(
        min_length=2, max_length=6,
        description="2-6 concrete strengths demonstrated in the interview"
    )
    areas_of_concern: List[str] = Field(
        description="Potential concerns or gaps; empty list if none"
    )

    # List of nested models — structured records, not free text.
    topics_discussed: List[TopicDiscussion] = Field(
        description="Technical topics covered and the candidate's performance on each"
    )

    # Optional field — None is valid, but if present must be >= 0.
    salary_expectation_usd: Optional[int] = Field(
        default=None, ge=0,
        description="Annual salary expectation in USD, if mentioned"
    )

    # `default_factory=list` instead of `default=[]` — the classic
    # mutable-default trap. Never use the latter.
    follow_up_questions: List[str] = Field(
        default_factory=list,
        description="Questions the interviewer should ask in the next round"
    )

    # Validators run after parsing — perfect for dedup, normalization,
    # or cross-field logic the LLM shouldn't be trusted with.
    @field_validator("key_strengths", "areas_of_concern")
    @classmethod
    def dedupe(cls, v: List[str]) -> List[str]:
        return list(dict.fromkeys(v))  # preserves order, removes duplicates
```

A few things worth calling out:

- **Enums inheriting from**`str` — this matters. Without it, the enum isn’t JSON-serializable and the parser struggles to match incoming strings.

- `ge` **/**`le` **vs**`gt` **/**`lt` — inclusive vs exclusive bounds. Use them based on whether zero (or your boundary) is actually valid.

- `min_length` **on lists** — underrated. It forces the model to produce a minimum number of items, which stops it from being lazy when you know there should be at least a few.

- `default_factory=list` — never use `default=[]`. Mutable defaults are shared across instances and will ruin your day.

- `@field_validator` — runs after the model’s output has been parsed. Ideal for cleanup the LLM can’t be trusted to do consistently.


## Field types reference

The schema above packs nearly every useful Pydantic feature into a single class, which is great for a walkthrough but dense for future reference. This is the **cheat sheet** — one block per type and feature, so you can pattern-match the pieces you need when writing your own schemas without rereading the whole example.

Each of the Pydantic **types** and **features** used in the schema above, as a quick reference:

**Types:**

- **Enum:** A field typed as a `str`-inheriting `Enum` class constrains the model’s output to one of a fixed set of string values. Anything outside the allowed values raises a validation error. The parser lists the allowed values in the format instructions, so the model sees exactly which strings it can produce. Perfect for categorical outputs: severity levels, sentiment labels, recommendation verdicts.

- **Constrained integer:** An `int` field combined with `Field(ge=..., le=..., gt=..., lt=...)`. `ge`/`le` are inclusive (`ge=0` accepts zero), `gt`/`lt` are exclusive. Validation rejects out-of-range values before they reach your code. Use for scores, counts, ratings, or any bounded whole number.

- **Constrained float:** Same mechanics as integers but with floating-point values. Ideal for ratios, percentages, probabilities, or any continuous measurement where you want sane bounds (e.g. `gt=0, lt=50` for years of experience, `ge=0.0, le=1.0` for a confidence score).

- **Constrained string:** A `str` field with `Field(min_length=..., max_length=...)`. Prevents the two failure modes you’ll otherwise see constantly: one-word summaries when you wanted a paragraph, and essays when you wanted a sentence. Both bounds are character counts, not token counts.

- **Constrained list:** A `List[X]` field with `Field(min_length=..., max_length=...)`. The minimum is the underrated one — it forces the model to produce at least N items instead of giving you a single-element list and calling it done. The maximum keeps output size predictable.

- **Optional field:** Declared as `Optional[X]` (or `X | None` in modern Python) with `Field(default=None, ...)`. The field may be absent or explicitly null. Any other constraints (`ge`, `le`, `min_length`) only apply when a value is actually present. Use whenever a piece of information might reasonably be missing from the source — like a salary expectation that the candidate simply didn’t mention.

- **Nested model:** A field typed as another `BaseModel` subclass. The parsed output contains a nested JSON object, and `List[NestedModel]` gives you a list of structured records rather than a list of strings. Reach for this whenever you’d otherwise be tempted to flatten multi-attribute items into comma-separated strings — structure beats parsing-after-parsing every time.


**Features:**

- `Field(description=...):`The `description` argument isn’t just developer documentation. The output parser includes it in the format instructions sent to the model, so every description you write doubles as an instruction to the LLM. Precise, specific descriptions dramatically improve output quality. Vague ones invite vague answers.

- `default_factory:`Used with mutable defaults: `Field(default_factory=list)`, `Field(default_factory=dict)`. Produces a fresh empty object every time the model is instantiated. Never use `default=[]` or `default={}` — those share a single mutable object across every instance and cause data to leak between records in ways that are maddening to debug.

- `@field_validator:`A method decorated with `@field_validator("field_name", ...)` that runs _after_ Pydantic’s type and constraint validation succeeds. Ideal for normalization (dedup, lowercasing, trimming, sorting) and cross-value logic. You can pass multiple field names to apply the same validator to several fields at once, as in the `dedupe` validator above.


## The LCEL chain

Now that the schema defines _what_ we want, we need to wire up _how_ to get it.

Three moving parts:

1. a prompt that tells the model its job

2. the model itself

3. the parser that turns its text output into a validated `InterviewEvaluation`


Before LCEL, stitching these together meant custom glue code — a function that formatted the prompt, called the model, pulled out the content string, handed it to the parser, caught exceptions. LCEL collapses all of that into a single expression using the `|` operator.

https://substackcdn.com/image/fetch/$s_!doiy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F633b26e2-df5e-41ad-b2f8-b9cf968de060_2752x968.png

Here’s where it comes together. With LCEL, the whole pipeline is one expression:

```
parser = PydanticOutputParser(pydantic_object=InterviewEvaluation)

prompt = ChatPromptTemplate.from_messages([\
    ("system",\
     "You are a senior technical recruiter. Analyze the interview transcript "\
     "and produce a structured evaluation.\n\n"\
     "{format_instructions}"),\
    ("human", "Interview transcript:\n\n{transcript}")\
]).partial(format_instructions=parser.get_format_instructions())

model = ChatOpenAI(model="gpt-4o", temperature=0)

chain = prompt | model | parser
```

Three things are happening:

1. `parser.get_format_instructions()` auto-generates a JSON schema description — including every `description` field and constraint you defined — and `.partial()` bakes it into the prompt.

2. **The**`|` **operator** composes the Runnables. Input flows left-to-right: dict → prompt → model → parser → `InterviewEvaluation` instance.

3. **The parser** at the end coerces the model’s string output into a validated Pydantic object. If validation fails, it raises `OutputParserException`.


**Runnable:** The base interface every LCEL-compatible component implements. If something is a `Runnable`, it can be piped into another `Runnable` with `|`, invoked with `.invoke(input)`, batched over many inputs with `.batch([...])`, or streamed with `.stream(input)`. Prompts, chat models, output parsers, retrievers, and custom functions (wrapped in `RunnableLambda`) are all Runnables — which is what makes the `|` composition work uniformly.

**Format instructions:** A string generated by an output parser via `.get_format_instructions()` that describes the expected output schema in natural language plus JSON schema form. You inject it into your prompt — typically with `.partial()` — so the model knows exactly what structure, field names, types, and constraints to produce. Every `Field(description=...)` you wrote ends up here.

## Running it

The chain is assembled. Invoking it is one line — pass in a transcript, get back an `InterviewEvaluation` object whose attributes you can access the way you'd access any Python class. That's the whole payoff: no JSON parsing, no regex, no post-processing. Here's what it looks like on a real transcript.

https://substackcdn.com/image/fetch/$s_!MooZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11907bfc-7f89-45ec-8732-02eb55c71483_2752x1335.png

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="llm-structure-outputs-the-silent-hero-of-production-ai.md">
<details>
<summary>Structured Outputs: The Silent Hero of Production AI</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.decodingai.com/p/llm-structured-outputs-the-only-way>

# Structured Outputs: The Silent Hero of Production AI

### How to master LLM outputs for reliable AI systems

_**Welcome to the AI Agents Foundations series**—a 9-part journey from Python developer to AI Engineer. Made by busy people. For busy people._

Everyone’s talking about AI agents. But what actually is an agent? When do we need them? How do they plan and use tools? How do we pick the correct AI tools and agentic architecture? …and most importantly, where do we even start?

To answer all these questions (and more!), We’ve started a 9-article straight-to-the-point series to build the skills and mental models to ship real AI agents in production.

We will write everything from scratch, jumping directly into the building blocks that will teach you _“how to fish”_.

By the end, you’ll have a deep understanding of how to design agents that think, plan, and execute—and most importantly, how to integrate them in your AI apps without being overly reliant on any AI framework.

**Let’s get started.**

* * *

## Structured Outputs

In a recent project I am working on, our production AI system crashed right before an important demo. Why? Because we were not using structured outputs consistently across our Large Language Model (LLM) workflows.

Our staging environment had been working fine with simple regex parsing of LLM responses, but when we deployed to production, everything fell apart. Our regex patterns failed to match slightly different response formats, data types were inconsistent, and downstream processes couldn’t handle the unpredictable data, causing cascading failures. When demo day arrived, our system was completely unusable.

**The problem was clear:** we had been relying on fragile string parsing, hoping the LLM would always respond in the exact same format. But in production, especially with AI systems, users will always enter inputs you never expect. Without structured outputs, we had no data validation, no type checking, and no real control over how the output should look. Just like lock files ensure consistent dependencies, structured outputs ensure consistent AI data contracts by defining the expected structure for LLM responses.

In our previous article from the AI Agents Foundations series, we explored the difference between workflows and agents. Now, we will tackle a fundamental challenge: getting reliable information _out_ of an LLM.

_To understand exactly what happens, we will first write everything from scratch and then move to using popular LLM APIs such as Gemini’s GenAI SDK:_

1. From scratch using JSON

2. From scratch using Pydantic _(We love Pydantic!)_

3. Using the Gemini SDK and Pydantic


## Understanding why structured outputs are important

Before we start coding, it is important to understand why structured outputs are foundational to building reliable AI applications. When an LLM returns a free-form string, you face the messy task of parsing it. This often involves fragile regular expressions or string-splitting logic that can easily break if the model outputs change slightly [[1\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/), [[2\]](https://arxiv.org/html/2506.21585v1). Structured outputs solve this by forcing the model’s response into a predictable format like JSON or Pydantic.

This approach offers several key benefits. First, structured outputs are easy to parse and manipulate programmatically. Instead of wrestling with raw text, you work with clean Python objects, making your code more predictable and easier to debug. Using libraries like Pydantic adds a layer of data and type validation [[3\]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4\]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). If the LLM returns a string where an integer is expected, your application raises a clear validation error immediately, preventing bad data from propagating.

https://substackcdn.com/image/fetch/$s_!04QT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b5cc1ed-e1fc-4edb-9388-3740f827630a_1200x1200.png Image 1: The benefits of structured outputs from LLMs, acting as a bridge between LLM (Software 3.0) and Python (Software 1.0) for downstream processing.

Furthermore, structured outputs are easier to orchestrate between steps in a workflow. When you know what information you have available, it is much simpler to pass it to the next LLM call or a downstream system like a database or API [[5\]](https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs), [[6\]](https://humanloop.com/blog/structured-outputs). This control also reduces costs. By ensuring the LLM generates only the necessary data without useless artifacts (e.g., “Here is the output you requested...”), you reduce the number of output tokens.

> 💡 **Quick Tip:** You can easily compute the costs of running your workflows or agent by plugging in an LLMOps open-source tool such as [Opik](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul).

Ultimately, structured outputs create a formal contract between the LLM (Software 3.0) and your application code (Software 1.0). They are the standard method for modeling domain objects in AI engineering, connecting the probabilistic nature of LLMs with deterministic code.

## Implementing Structured Outputs From Scratch Using JSON

To understand how modern LLM APIs such as OpenAI and Gemini work under the hood, we will first implement structured outputs from scratch.

Our goal is to prompt a model to return a JSON object and then parse it into a Python dictionary. We will use an “LLM-as-judge” evaluation as our example, where we ask an LLM to compare a generated text against a ground-truth document and score it based on predefined criteria. This is a great use case, as it requires extracting specific, structured information from a large context.

1. First, we define our sample documents for the evaluation. These will serve as the input for our LLM judge:

```
GENERATED_DOCUMENT = “”“
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
“”“

GROUND_TRUTH_DOCUMENT = “”“
# Q3 2023 Financial Performance Analysis

The Q3 earnings report shows a 18% increase in revenue and a 15% growth in user engagement,
slightly below market expectations. These results reflect our product strategy adjustments
and competitive market positioning challenges.

Our core business segments showed mixed performance, with digital services growing at
22% year-over-year. The expansion into new markets has been challenging, contributing
to only 15% of the total revenue increase.

Customer acquisition costs increased by 5% while retention rates remained at 88%,
indicating areas for improvement. These metrics, combined with our cash flow position,
suggest we need strategic adjustments for Q4 growth.
“”“
```

2. Next, we craft a prompt that instructs the LLM to evaluate the generated document against the ground truth and format the output as JSON. We provide a clear example of the desired structure and use XML tags like `<document>` to separate inputs from instructions. This is an effective prompt engineering technique for improving clarity and guiding the model’s output [[7\]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/), [[8\]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api). The key is to be explicit about the format, keys, and value types you expect:

```
prompt = f”“”
You are an expert evaluator. Compare the generated document with the ground truth document and provide a score for each criterion.
The output must be a single, valid JSON object with the following structure:
{{
  “scores”: [\
    {{\
      “criterion”: “revenue_forecast”,\
      “score”: 0 or 1,\
      “reason”: “Your reasoning here.”\
    }},\
    {{\
      “criterion”: “user_growth”,\
      “score”: 0 or 1,\
      “reason”: “Your reasoning here.”\
    }},\
    {{\
      “criterion”: “facts”,\
      “score”: 0 or 1,\
      “reason”: “Your reasoning here.”\
    }}\
  ]
}}

Here are the documents:

<generated_document>
{GENERATED_DOCUMENT}
</generated_document>

<ground_truth_document>
{GROUND_TRUTH_DOCUMENT}
</ground_truth_document>
“”“
```

3. We send the prompt to the model and inspect the raw response. As expected, the model returns a JSON object, wrapped in Markdown _\`\`\`json_ code blocks:

```
from google import genai

client = genai.Client()

response = client.models.generate_content(model=”gemini-2.5-flash”, contents=prompt)
```

4. It outputs:

````
```json
{
“scores”: [\
    {\
      “criterion”: “revenue_forecast”,\
      “score”: 0,\
      “reason”: “The generated document claims a 20% revenue increase, while the ground truth states an 18% increase, which is slightly below expectations. The forecast is factually incorrect.”\
    },\
    {\
      “criterion”: “user_growth”,\
      “score”: 1,\
      “reason”: “Both documents report a 15% growth in user engagement, so this fact is correctly stated in the generated document.”\
    },\
    {\
      “criterion”: “facts”,\
      “score”: 0,\
      “reason”: “The generated document contains several factual inaccuracies regarding revenue, market expansion contribution, customer acquisition costs, and retention rates when compared to the ground truth.”\
    }\
]
}
````

5. To handle this, we create a helper function to strip the Markdown tags, leaving a clean JSON string that can be safely parsed:

````
def extract_json_from_response(response: str) -> dict:
    “”“
    Extracts JSON from a response string that is wrapped in ```json tags.
    “”“
    response = response.replace(”```json”, “”).replace(”```”, “”)
    return json.loads(response)
````

6. Finally, we parse the string into a Python dictionary, which can now be used in our application:

```
parsed_response = extract_json_from_response(response.text)
```

7. It outputs:

```
{
“scores”: [\
    {\
      “criterion”: “revenue_forecast”,\
      “score”: 0,\
      “reason”: “The generated document claims a 20% revenue increase, ...”\
    },\
    {\
      “criterion”: “user_growth”,\
      “score”: 1,\
      “reason”: “Both documents report a 15% growth in user engagement, ...”\
    },\
    {\
      “criterion”: “facts”,\
      “score”: 0,\
      “reason”: “The generated document contains several factual ...”\
    }\
]
}
```

This manual method works, but it relies on post-processing and lacks data validation. If the LLM makes a mistake like outputting a string instead of an integer or missing a dictionary key, our application will fail. Next, we will see how Pydantic provides a much more robust solution to this problem.

## Implementing Structured Outputs From Scratch Using Pydantic

Forcing JSON output is an improvement, but it still leaves you with a plain Python dictionary. You cannot be sure what is inside it, whether the keys are correct, or if the values have the right type. This uncertainty can lead to bugs and make your code difficult to maintain.

Pydantic solves this problem. It is a data validation library that enforces structure and type hints at runtime, ensuring data integrity from the moment it enters your application [[3\]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses). It provides a single, clear definition for your data structure and can automatically generate a JSON Schema from your Python class.

> **💡 Quick Tip**: I personally love Pydantic. I use it to model any data structure in my Python programs, completely dropping other options such as `@dataclass` or `TypedDict`.

When an LLM produces output that does not match your Pydantic model, the library raises a `ValidationError` that clearly explains what went wrong. This “fail-fast” behavior is essential for building reliable systems, preventing bad data from moving through your application and causing hard-to-debug errors later. This is a major improvement over simple JSON parsing, as it introduces a validation layer that catches errors early.

1. We define our desired data structure as a Pydantic class, using standard Python type hints to define the expected type for each field:

```
from typing import Literal
from typing_extensions import Annotated

import pydantic
from pydantic import Ge, Le

class CriterionScore(pydantic.BaseModel):
    “”“Model holding the score and reason for a specific criterion.”“”
    criterion: Literal[”revenue_forecast”, “user_growth”, “facts”]
    score: Annotated[int, Ge(0), Le(1)] = pydantic.Field(description=”Binary score of the section.”)
    reason: str = pydantic.Field(description=”The reason for the given score.”)

class Scores(pydantic.BaseModel):
    scores: list[CriterionScore]
```

_You can also nest Pydantic models to represent more complex, hierarchical data. This allows you to define intricate relationships between different pieces of information. However, it is good practice to keep schemas as simple as possible, as complex nested structures can confuse the LLM and lead to errors._

2. With our Pydantic model defined, we can automatically generate a JSON Schema from it. A schema is the standard for defining the structure and constraints of your data, acting as a formal contract between your application and the LLM. This contract dictates the expected fields, their types, and any validation rules. Now, instead of providing a fuzzy JSON that explains how our output should look (as we did in the previous section), we provide an explicit schema to the LLM that is compatible with Pydantic. This is similar to the technique used internally by APIs like Gemini and OpenAI to enforce a specific output format [[9\]](https://ai.google.dev/gemini-api/docs/structured-output):

```
schema = Scores.model_json_schema()
```

3. The generated schema is detailed and includes descriptions from the `Field` definitions to guide the generation process.

```
{
    “$defs”: {
        “CriterionScore”: {
            “properties”: {
                “criterion”: {
                    “enum”: [”revenue_forecast”, “user_growth”, “facts”],
                    “title”: “Criterion”,
                    “type”: “string”
                },
                “score”: {
                    “description”: “Binary score of the section.”,
                    “exclusiveMaximum”: 1,
                    “exclusiveMinimum”: 0,
                    “title”: “Score”,
                    “type”: “integer”
                },
                “reason”: {
                    “description”: “The reason for the given score.”,
                    “title”: “Reason”,
                    “type”: “string”
                }
            },
            “required”: [”criterion”, “score”, “reason”],
            “title”: “CriterionScore”,
            “type”: “object”
        }
    },
    “properties”: {
        “scores”: {
            “items”: {
                “$ref”: “#/$defs/CriterionScore”
            },
            “title”: “Scores”,
            “type”: “array”
        }
    },
    “required”: [”scores”],
    “title”: “Scores”,
    “type”: “object”
}
```

4. We update our prompt to include this JSON Schema:

```
prompt = f”“”
Please analyze the following documents and extract evaluation scores.
The output must be a single, valid JSON object that conforms to the following JSON Schema:
{json.dumps(schema, indent=2)}

Here are the documents:
<generated_document>
{GENERATED_DOCUMENT}
</generated_document>
<ground_truth_document>
{GROUND_TRUTH_DOCUMENT}
</ground_truth_document>
“”“
```

5. We call the model and extract the JSON string as before.

```
response = client.models.generate_content(model=MODEL_ID, contents=prompt)
parsed_response = extract_json_from_response(response.text)
```

6. It outputs:

```
{
“scores”: [\
    {\
      “criterion”: “revenue_forecast”,\
      “score”: 0,\
      “reason”: “The generated document overstates revenue growth  ...”\
    },\
    {\
      “criterion”: “user_growth”,\
      “score”: 1,\
      “reason”: “The 15% user engagement growth is correctly reported ....”\
    },\
    {\
      “criterion”: “facts”,\
      “score”: 0,\
      “reason”: “The generated document contains multiple factual ....”\
    }\
]
}
```

7. But now, the biggest difference, is that we can load the output dictionary into our Pydantic model and validate it:

```
try:
    scores = Scores.model_validate(parsed_response)
    print(”Validation successful!”)
except Exception as e:
    print(f”Validation failed!”)
```

8. It outputs:

```
Validation successful!
```

The `scores` Pydantic object can now be safely used throughout your application. This is the main advantage: you move from unclear dictionaries to clean, predictable Python objects.

While Python’s built-in `dataclasses` or `TypedDict` can define structure, they only provide type hints for static analysis and do not perform runtime validation [[3\]](https://www.speakeasy.com/blog/pydantic-vs-dataclasses), [[4\]](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/). If the LLM returns a string where an integer is expected, these tools will not catch the error.

To conclude, Pydantic’s runtime validation, type constraints, and clear schema definitions make it our favorite way for structuring and validating all our domain data structures from our AI apps.

## Implementing Structured Outputs Using Gemini and Pydantic

While Pydantic brings structure and validation, we still had to construct the prompts and handle responses manually. When working with modern APIs such as Gemini and OpenAI, the recommended way to generate structured outputs is by using their native features. This approach is simpler, more accurate, and often more cost-effective than manual prompt engineering, as the vendor will always handle the optimization on top of their models better than your manual prompting [[9\]](https://ai.google.dev/gemini-api/docs/structured-output), [[10\]](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode), [[11\]](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640).

Let’s see how to achieve the same result for our LLM-as-judge example using the Gemini API’s native capabilities. The process becomes much simpler.

1. We define a `GenerateContentConfig` object, instructing the Gemini API to set the `response_mime_type` to `“application/json”` and the `response_schema` to our `Scores` Pydantic model. This configures the model to output JSON that is then automatically converted to the given Pydantic model. This single configuration step replaces the manual schema injection and parsing we did earlier:

```
from google.genai import types

config = types.GenerateContentConfig(
    response_mime_type=”application/json”,
    response_schema=Scores
)
```

2. This configuration makes our prompt significantly shorter and cleaner, eliminating the need to manually inject any type of schema. We simply ask the model to perform the task, as the output format is guided directly by the config:

```
prompt = f”“”
You are an expert evaluator. Compare the generated document with the ground truth document and provide a score for each criterion.

Here are the documents:
<generated_document>
{GENERATED_DOCUMENT}
</generated_document>
<ground_truth_document>
{GROUND_TRUTH_DOCUMENT}
</ground_truth_document>
“”“
```

3. Now, we call the model, passing our simplified prompt and the new configuration object. The API handles the rest, ensuring the output adheres to the schema.

```
response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=config
)
```

4. The Gemini client automatically parses the output for us. By accessing the `response.parsed` attribute, we receive a ready-to-use instance of our `Scores` Pydantic model:

```
scores = response.parsed
print(f”Type of the response: `{type(scores)}`”)
```

5. It outputs:

```
Type of the response: `<class ‘__main__.Scores’>`
```

Similar patterns apply to all modern LLM APIs.

This native approach is robust, efficient, and requires less code. While it is the recommended way for closed-source APIs or AI frameworks, the “from scratch” method remains useful for open-source models that may not have this built-in functionality or when you do not have access to any AI framework.

## The Best Model for Structured Outputs

A final thought on what’s the best model for structured outputs: In general, all the latest LLMs support generating JSON, indirectly supporting Pydantic structures.

However, when building AI systems, there is never the problem of what’s the best model, but what’s the best model for your given use case. Almost always, you cannot tell which model is better until you actually test them. That’s why, when building AI systems, you should ALWAYS adopt a scientific method to find the optimal model (and its configuration):

1. Configure different parameters (e.g., different models).

2. Run experiments for each configuration.

3. Compute business metrics of interest (e.g., using an LLM-as-judge).

4. Use an LLMOps tool such as [Opik](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul) to analyze the results.

5. Pick the best configuration and iterate if needed.

https://substackcdn.com/image/fetch/$s_!J6_X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15821967-c979-4a15-80b0-3329a835abd3_1200x1200.png Image 2: The scientific method for evaluating and optimizing AI systems.

This high-level strategy works for tweaking any model, config or even feature of an AI system.

## Structured Outputs Are Everywhere

The thing is that structured outputs are everywhere! They are a fundamental pattern in AI engineering, connecting the probabilistic nature of LLMs with the deterministic world of software. Whether you are building a simple summarization workflow or a complex research agent, you will use structured outputs to ensure reliability and control.

_Remember that this article is part of a longer series of 9 pieces on the AI Agents Foundations that will give you the tools to morph from a Python developer to an AI Engineer._

**Here’s our roadmap:**

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. _**Structured Outputs** ← You just finished this one._

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these) _← Move to this one._

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)

9. [Multimodal Data](https://www.decodingai.com/p/stop-converting-documents-to-text)

See you next week.

[Paul Iusztin](https://www.linkedin.com/in/pauliusztin/)

* * *

## References

01. Ntinopoulos, V., Biefer, H. R. C., Tudorache, I., Papadopoulos, N., Odavic, D., Risteski, P., Haeussler, A., & Dzemali, O. (2024). Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation. _BMJ Health & Care Informatics_, 32(1), e101139. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/)

02. (n.d.). Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops. _arXiv_. [https://arxiv.org/html/2506.21585v1](https://arxiv.org/html/2506.21585v1)

03. Speakeasy Team. (2024, August 29). Type Safety in Python: Pydantic vs. Data Classes vs. Annotations vs. TypedDicts. _Speakeasy_. [https://www.speakeasy.com/blog/pydantic-vs-dataclasses](https://www.speakeasy.com/blog/pydantic-vs-dataclasses)

04. (n.d.). Validators approach in Python - Pydantic vs. Dataclasses. _Codetain_. [https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/](https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/)

05. (n.d.). Automating Knowledge Graphs with LLM Outputs. _Prompts.ai_. [https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs](https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs)

06. Kelly, C. (2024, February 13). Structured Outputs: everything you should know. _Humanloop_. [https://humanloop.com/blog/structured-outputs](https://humanloop.com/blog/structured-outputs)

07. (2024, June 26). Structured data response with Amazon Bedrock: Prompt Engineering and Tool Use. _Amazon Web Services_. [https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/)

08. (n.d.). Best practices for prompt engineering with the OpenAI API. _OpenAI Help Center_. [https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)

09. (n.d.). Structured output. _Google AI for Developers_. [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)

10. Sharma, A. (2024, October 10). When should I use function calling, structured outputs or JSON mode? _Vellum AI Blog_. [https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode)

11. (n.d.). Structured Output in vertexAI BatchPredictionJob. _Google Cloud Community_. [https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640](https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640)

* * *

## Images

If not otherwise stated, all images are created by the author.
```

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="llm-structured-output-in-2026-stop-parsing-json-with-regex-a.md">
<details>
<summary>llm-structured-output-in-2026-stop-parsing-json-with-regex-a</summary>

Phase: [EXPLORATION]

**Source URL:** <https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk>

You've been there. You ask GPT to "return a JSON object with the user's name, email, and sentiment score." It returns a perfectly formatted JSON... wrapped in a markdown code block. With a helpful explanation. And a disclaimer about how it's an AI.

So you write a regex to strip the code fences. Then another regex for the trailing commentary. Then it randomly returns JSONL instead of JSON. Then it wraps everything in `{"result": ...}` when you didn't ask for that. Then it works perfectly for 10,000 requests and fails catastrophically on request 10,001 because the user's name contained a quote character.

This is the structured output problem, and in 2026, **you should not be solving it by hand anymore**.

Every major LLM provider now offers native structured output. The tooling (Pydantic for Python, Zod for TypeScript) has matured enormously. And yet, most developers are still either parsing raw strings or using function calling as a hacky workaround.

This guide covers everything: how structured output actually works under the hood, how to implement it across OpenAI, Anthropic, and Gemini, the Python and TypeScript ecosystems, and — most importantly, the production pitfalls that will bite you if you don't know about them.

* * *

## Why Structured Output Matters (More Than You Think)

Here's the fundamental problem with LLMs in production:

```
LLMs are text generators.
Your application needs data structures.
The gap between these two things is where bugs live.
```

Enter fullscreen modeExit fullscreen mode

When you `JSON.parse()` a raw LLM response, you're making several dangerous assumptions:

1. The output is valid JSON (it might not be)
2. The JSON has the fields you expect (it might not)
3. The field types are correct (strings vs numbers vs booleans)
4. The values are within expected ranges (sentiment: -1 to 1, not "positive")
5. The response doesn't contain extra fields you didn't ask for
6. The response format is consistent across different inputs

Structured output eliminates **all six** of these problems by constraining the model's output at the token generation level — not after the fact.

### The Three Levels of Output Control

```
Level 1: Prompt Engineering (Unreliable)
  "Return JSON with fields: name, email, score"
  → Works 80-95% of the time
  → Fails silently on edge cases
  → No type guarantees

Level 2: Function Calling / Tool Use (Better)
  Define a function schema, model "calls" it
  → Works 95-99% of the time
  → Schema is a hint, not a constraint
  → Can still produce invalid values within valid types

Level 3: Native Structured Output (Best)
  Constrained decoding with JSON Schema
  → Works 100% of the time (schema-valid guaranteed)
  → Uses finite state machines to mask invalid tokens
  → Types AND values are enforced at generation time
```

Enter fullscreen modeExit fullscreen mode

In 2026, you should be at Level 3 for anything going to production.

* * *

## How Structured Output Actually Works

Most developers treat structured output as a black box: "I give it a schema, it returns valid JSON." But understanding the mechanism matters for debugging and optimization.

### Constrained Decoding (The Magic Behind the Curtain)

When an LLM generates text, it predicts the next token from a vocabulary of ~100,000+ tokens. Normally, any token can follow any other token. Structured output adds a **constraint layer**:

```
Normal generation:
  Token probabilities: {"hello": 0.3, "{": 0.1, "The": 0.2, ...}
  → Any token can be selected

Constrained generation (expecting JSON object start):
  Token probabilities: {"hello": 0.3, "{": 0.1, "The": 0.2, ...}
  Mask: {"hello": 0, "{": 1, "The": 0, ...}
  → Only "{" and whitespace tokens remain valid
  → Model MUST output "{"
```

Enter fullscreen modeExit fullscreen mode

This is implemented using a **Finite State Machine (FSM)** that tracks where you are in the JSON schema:

```
State Machine for {"name": string, "age": integer}:

START → expect "{"
  → expect "\"name\""
    → expect ":"
      → expect string value
        → expect "," or "}"
          → if ",": expect "\"age\""
            → expect ":"
              → expect integer value
                → expect "}"
                  → DONE
```

Enter fullscreen modeExit fullscreen mode

At each state, the FSM masks out all tokens that would violate the schema. The model can still choose the most likely _valid_ token, preserving quality while guaranteeing structure.

### Why This Is Better Than Prompt Engineering

```
Prompt: "Return a JSON object with 'score' as a number between 0 and 1"

Without constrained decoding:
  Model might output: {"score": "0.85"}     ← string, not number
  Model might output: {"score": 0.85, "confidence": "high"}  ← extra field
  Model might output: {"score": 85}         ← wrong range
  Model might output: Sure! Here's the JSON: {"score": 0.85}  ← preamble

With constrained decoding:
  Model MUST output: {"score": 0.85}        ← always valid
```

Enter fullscreen modeExit fullscreen mode

* * *

## Implementation: OpenAI

OpenAI's structured output is the most mature. It's available in the Chat Completions API with `response_format`.

### Basic Usage

```
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class SentimentAnalysis(BaseModel):
    sentiment: str  # "positive", "negative", "neutral"
    confidence: float
    key_phrases: list[str]
    reasoning: str

response = client.beta.chat.completions.parse(
    model="gpt-5-mini",
    messages=[\
        {"role": "system", "content": "Analyze the sentiment of the given text."},\
        {"role": "user", "content": "This product is absolutely terrible. Worst purchase ever."}\
    ],
    response_format=SentimentAnalysis,
)

result = response.choices[0].message.parsed
print(result.sentiment)     # "negative"
print(result.confidence)    # 0.95
print(result.key_phrases)   # ["absolutely terrible", "worst purchase ever"]
```

Enter fullscreen modeExit fullscreen mode

### With Enums and Nested Objects

```
from enum import Enum
from pydantic import BaseModel, Field

class Sentiment(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    mixed = "mixed"

class Entity(BaseModel):
    name: str
    type: str = Field(description="person, organization, product, or location")
    sentiment: Sentiment

class FullAnalysis(BaseModel):
    overall_sentiment: Sentiment
    confidence: float = Field(ge=0.0, le=1.0)
    entities: list[Entity]
    summary: str = Field(max_length=200)
    topics: list[str] = Field(min_length=1, max_length=5)

response = client.beta.chat.completions.parse(
    model="gpt-5-mini",
    messages=[\
        {"role": "system", "content": "Extract structured analysis from the text."},\
        {"role": "user", "content": "Apple's new MacBook Pro is incredible, but Tim Cook's keynote was boring."}\
    ],
    response_format=FullAnalysis,
)

result = response.choices[0].message.parsed
# result.entities = [\
#   Entity(name="Apple", type="organization", sentiment="positive"),\
#   Entity(name="MacBook Pro", type="product", sentiment="positive"),\
#   Entity(name="Tim Cook", type="person", sentiment="negative"),\
# ]
```

Enter fullscreen modeExit fullscreen mode

### TypeScript with Zod

```
import OpenAI from 'openai';
import { z } from 'zod';
import { zodResponseFormat } from 'openai/helpers/zod';

const client = new OpenAI();

const SentimentSchema = z.object({
  sentiment: z.enum(['positive', 'negative', 'neutral', 'mixed']),
  confidence: z.number().min(0).max(1),
  entities: z.array(z.object({
    name: z.string(),
    type: z.enum(['person', 'organization', 'product', 'location']),
    sentiment: z.enum(['positive', 'negative', 'neutral']),
  })),
  summary: z.string(),
  topics: z.array(z.string()).min(1).max(5),
});

type Sentiment = z.infer<typeof SentimentSchema>;

const response = await client.beta.chat.completions.parse({
  model: 'gpt-5-mini',
  messages: [\
    { role: 'system', content: 'Extract structured analysis from the text.' },\
    { role: 'user', content: 'The new React compiler is amazing but the migration docs are lacking.' },\
  ],
  response_format: zodResponseFormat(SentimentSchema, 'sentiment_analysis'),
});

const result: Sentiment = response.choices[0].message.parsed!;
console.log(result.sentiment); // "mixed"
```

Enter fullscreen modeExit fullscreen mode

* * *

## Implementation: Anthropic (Claude)

Anthropic's approach to structured output uses **tool use** (function calling) as the mechanism. You define a tool with a JSON schema, and Claude returns structured output as if calling that tool.

### Basic Usage

```
import anthropic
from pydantic import BaseModel

client = anthropic.Anthropic()

class ExtractedData(BaseModel):
    name: str
    email: str
    company: str
    role: str
    urgency: str  # "low", "medium", "high", "critical"

response = client.messages.create(
    model="claude-sonnet-4-20260514",
    max_tokens=1024,
    tools=[{\
        "name": "extract_contact",\
        "description": "Extract contact information from the email.",\
        "input_schema": ExtractedData.model_json_schema(),\
    }],
    tool_choice={"type": "tool", "name": "extract_contact"},
    messages=[{\
        "role": "user",\
        "content": """Extract the contact info from this email:\
\
        Hi, I'm Sarah Chen from DataFlow Inc. Our production pipeline is\
        down and we need immediate help. Please reach me at sarah@dataflow.io\
        — I'm the VP of Engineering.""",\
    }],
)

# Extract the tool use result
tool_result = next(
    block for block in response.content
    if block.type == "tool_use"
)
data = ExtractedData(**tool_result.input)
print(data.name)      # "Sarah Chen"
print(data.urgency)   # "critical"
```

Enter fullscreen modeExit fullscreen mode

### TypeScript with Zod + Anthropic

```
import Anthropic from '@anthropic-ai/sdk';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const client = new Anthropic();

const ContactSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  company: z.string(),
  role: z.string(),
  urgency: z.enum(['low', 'medium', 'high', 'critical']),
});

const response = await client.messages.create({
  model: 'claude-sonnet-4-20260514',
  max_tokens: 1024,
  tools: [{\
    name: 'extract_contact',\
    description: 'Extract contact information from the email.',\
    input_schema: zodToJsonSchema(ContactSchema) as Anthropic.Tool.InputSchema,\
  }],
  tool_choice: { type: 'tool' as const, name: 'extract_contact' },
  messages: [{\
    role: 'user',\
    content: 'Extract info: Hi, I am John Park, CTO at Acme Corp (john@acme.com). Not urgent.',\
  }],
});

const toolBlock = response.content.find(
  (block): block is Anthropic.ToolUseBlock => block.type === 'tool_use'
);
const data = ContactSchema.parse(toolBlock!.input);
console.log(data.urgency); // "low"
```

Enter fullscreen modeExit fullscreen mode

* * *

## Implementation: Google Gemini

Gemini supports structured output natively through its `response_schema` parameter. It uses constrained decoding similar to OpenAI.

### Basic Usage (Python)

```
import google.generativeai as genai
from pydantic import BaseModel
from enum import Enum

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class TaskExtraction(BaseModel):
    title: str
    assignee: str
    priority: Priority
    deadline: str | None
    tags: list[str]

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema=TaskExtraction,
    ),
)

response = model.generate_content(
    "Extract the task: 'John needs to fix the login bug by Friday. It's blocking prod. Tag it as backend and auth.'"
)

import json
result = TaskExtraction(**json.loads(response.text))
print(result.priority)   # "critical"
print(result.tags)        # ["backend", "auth"]
```

Enter fullscreen modeExit fullscreen mode

* * *

## The Provider Comparison Table

Before choosing a provider for structured output, here's how they compare:

```
Feature              OpenAI           Anthropic         Gemini
─────────────────    ──────────────   ──────────────    ──────────────
Method               Native SO        Tool Use          Native SO
Constrained decode   Yes              Partial           Yes
100% schema valid    Yes              99%+              Yes
Streaming support    Yes              Yes               Yes
Pydantic native      Yes (.parse)     Manual schema     Manual schema
Zod native           Yes (helper)     Manual convert    Manual convert
Nested objects       Yes              Yes               Yes
Enums                Yes              Yes               Yes
Optional fields      Yes              Yes              Yes
Recursive schemas    Limited          Yes               Limited
Max schema depth     5 levels         No limit          No limit
Refusal handling     Yes              N/A               N/A
```

Enter fullscreen modeExit fullscreen mode

**Recommendation**: If you need guaranteed schema compliance, use OpenAI or Gemini's native structured output. If you're already on Claude and need structured data, the tool use pattern works well but add Pydantic/Zod validation as a safety net.

* * *

## Production Patterns That Actually Work

### Pattern 1: The Validation Sandwich

Never trust the LLM output directly, even with structured output. Always validate.

```
from pydantic import BaseModel, Field, field_validator
from openai import OpenAI

client = OpenAI()

class ProductReview(BaseModel):
    rating: int = Field(ge=1, le=5)
    title: str = Field(min_length=5, max_length=100)
    pros: list[str] = Field(min_length=1, max_length=5)
    cons: list[str] = Field(max_length=5)
    would_recommend: bool

    @field_validator('title')
    @classmethod
    def title_not_generic(cls, v: str) -> str:
        generic_titles = ['good', 'bad', 'ok', 'fine', 'great']
        if v.lower().strip() in generic_titles:
            raise ValueError(f'Title too generic: {v}')
        return v

def extract_review(text: str) -> ProductReview:
    response = client.beta.chat.completions.parse(
        model="gpt-5-mini",
        messages=[\
            {"role": "system", "content": "Extract a structured product review."},\
            {"role": "user", "content": text},\
        ],
        response_format=ProductReview,
    )

    result = response.choices[0].message.parsed

    if response.choices[0].message.refusal:
        raise ValueError(f"Model refused: {response.choices[0].message.refusal}")

    # Re-validate even though OpenAI guarantees schema compliance
    # (catches business logic violations that JSON Schema can't express)
    return ProductReview.model_validate(result.model_dump())
```

Enter fullscreen modeExit fullscreen mode

### Pattern 2: Retry with Escalation

When structured output fails (rare but it happens), escalate gracefully:

```
import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
)
def extract_with_retry(text: str, schema: type[BaseModel]) -> BaseModel:
    try:
        response = client.beta.chat.completions.parse(
            model="gpt-5-mini",
            messages=[\
                {"role": "system", "content": "Extract structured data precisely."},\
                {"role": "user", "content": text},\
            ],
            response_format=schema,
        )
        result = response.choices[0].message.parsed
        return schema.model_validate(result.model_dump())

    except Exception as e:
        print(f"Attempt failed: {e}")
        raise

# Usage
try:
    review = extract_with_retry(user_text, ProductReview)
except Exception:
    # Fallback: simpler schema or manual processing
    review = extract_with_retry(user_text, SimpleReview)
```

Enter fullscreen modeExit fullscreen mode

### Pattern 3: Multi-Provider Fallback

Don't lock yourself into one provider. Build a fallback chain:

```
import OpenAI from 'openai';
import Anthropic from '@anthropic-ai/sdk';
import { z } from 'zod';
import { zodResponseFormat } from 'openai/helpers/zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const schema = z.object({
  intent: z.enum(['question', 'complaint', 'feedback', 'request']),
  urgency: z.enum(['low', 'medium', 'high']),
  summary: z.string().max(200),
  action_required: z.boolean(),
});

type TicketClassification = z.infer<typeof schema>;

async function classifyTicket(text: string): Promise<TicketClassification> {
  // Try OpenAI first (fastest structured output)
  try {
    const openai = new OpenAI();
    const response = await openai.beta.chat.completions.parse({
      model: 'gpt-5-mini',
      messages: [\
        { role: 'system', content: 'Classify the support ticket.' },\
        { role: 'user', content: text },\
      ],
      response_format: zodResponseFormat(schema, 'ticket'),
    });
    return schema.parse(response.choices[0].message.parsed);
  } catch (openaiError) {
    console.warn('OpenAI failed, falling back to Claude:', openaiError);
  }

  // Fallback to Anthropic
  try {
    const anthropic = new Anthropic();
    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-20260514',
      max_tokens: 512,
      tools: [{\
        name: 'classify',\
        description: 'Classify the ticket.',\
        input_schema: zodToJsonSchema(schema) as Anthropic.Tool.InputSchema,\
      }],
      tool_choice: { type: 'tool' as const, name: 'classify' },
      messages: [{ role: 'user', content: `Classify: ${text}` }],
    });
    const toolBlock = response.content.find(
      (b): b is Anthropic.ToolUseBlock => b.type === 'tool_use'
    );
    return schema.parse(toolBlock!.input);
  } catch (anthropicError) {
    console.error('Both providers failed:', anthropicError);
    throw new Error('All LLM providers failed for structured output');
  }
}
```

Enter fullscreen modeExit fullscreen mode

### Pattern 4: Streaming Structured Output

For long-form structured responses, stream partial results:

```
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class Article(BaseModel):
    title: str
    sections: list[dict]  # {"heading": str, "content": str}
    tags: list[str]
    word_count: int

# Streaming with structured output
with client.beta.chat.completions.stream(
    model="gpt-5",
    messages=[\
        {"role": "system", "content": "Generate an article outline with detailed sections."},\
        {"role": "user", "content": "Write about WebAssembly in 2026."}\
    ],
    response_format=Article,
) as stream:
    for event in stream:
        # Get partial JSON as it's generated
        snapshot = event.snapshot
        if snapshot and snapshot.choices[0].message.content:
            partial = snapshot.choices[0].message.content
            print(f"Receiving: {len(partial)} chars...")

    # Final parsed result
    final = stream.get_final_completion()
    article = final.choices[0].message.parsed
    print(f"Article: {article.title} ({article.word_count} words)")
```

Enter fullscreen modeExit fullscreen mode

* * *

## The Pitfalls Nobody Talks About

### Pitfall 1: The Schema Complexity Tax

Every constraint you add to your schema increases latency. Complex schemas with deeply nested objects, many enums, and strict validation can **double or triple** your response time.

```
Schema complexity vs. latency (gpt-5-mini, average):

Schema                        Tokens/s    First Token    Total Time
────────────────────────────  ──────────  ─────────────  ──────────
No schema (free text)         85 tok/s    ~200ms         ~500ms
Simple (3 fields)             78 tok/s    ~250ms         ~550ms
Medium (10 fields, 1 enum)    65 tok/s    ~350ms         ~800ms
Complex (20+ fields, nested)  45 tok/s    ~500ms         ~1.5s
Very complex (recursive)      30 tok/s    ~800ms         ~3s
```

Enter fullscreen modeExit fullscreen mode

**Solution**: Break complex schemas into multiple smaller calls. Instead of one mega-schema, use a pipeline:

```
# ❌ One giant schema
class FullDocumentAnalysis(BaseModel):
    entities: list[Entity]       # 20+ fields each
    sentiment: SentimentDetail   # 10+ fields
    summary: Summary             # 5 fields
    classification: Classification  # 8 fields
    # ... 50+ total fields

# ✅ Pipeline of smaller schemas
class Step1_Entities(BaseModel):
    entities: list[SimpleEntity]  # 5 fields each

class Step2_Sentiment(BaseModel):
    overall: str
    confidence: float
    aspects: list[str]

class Step3_Classification(BaseModel):
    category: str
    subcategory: str
    priority: str

# Run in parallel
import asyncio
entities, sentiment, classification = await asyncio.gather(
    extract(text, Step1_Entities),
    extract(text, Step2_Sentiment),
    extract(text, Step3_Classification),
)
```

Enter fullscreen modeExit fullscreen mode

### Pitfall 2: Schema Versioning Hell

Your application evolves. Your schema evolves. But the LLM doesn't know that you renamed `user_name` to `name` last Tuesday.

```
# Version 1 (deployed January)
class UserProfile_v1(BaseModel):
    user_name: str
    email_address: str
    age: int

# Version 2 (deployed February)
class UserProfile_v2(BaseModel):
    name: str            # renamed!
    email: str           # renamed!
    age: int
    location: str | None  # new field

# Problem: Old cached prompts still reference v1 field names.
# Problem: Downstream consumers expect v1 format.
# Problem: A/B tests run both versions simultaneously.
```

Enter fullscreen modeExit fullscreen mode

**Solution**: Use explicit schema versioning and migration:

```
from pydantic import BaseModel, Field
from typing import Literal

class UserProfile(BaseModel):
    schema_version: Literal["2.0"] = "2.0"
    name: str = Field(alias="user_name")  # Accept old field name
    email: str = Field(alias="email_address")
    age: int
    location: str | None = None

    class Config:
        populate_by_name = True  # Accept both alias and field name
```

Enter fullscreen modeExit fullscreen mode

### Pitfall 3: The Empty Array Trap

LLMs struggle with returning empty arrays when there's genuinely nothing to extract. They'll often hallucinate entries to "fill" the array.

```
# Input: "The weather is nice today."
# Expected: {"entities": [], "topics": ["weather"]}
# Actual:   {"entities": [{"name": "weather", "type": "concept"}], "topics": ["weather"]}
# The model HATES returning empty arrays.

# Solution: Make empty arrays explicitly valid and prompt for them
class Extraction(BaseModel):
    entities: list[Entity] = Field(
        default_factory=list,
        description="Named entities found in the text. Return empty list [] if none found."
    )
```

Enter fullscreen modeExit fullscreen mode

### Pitfall 4: Enum Confusion with Similar Values

```
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"
    urgent = "urgent"  # ← How is this different from "critical"?

# The model will inconsistently choose between "critical" and "urgent"
# because THEY don't even know the difference.

# Solution: Use fewer, clearly distinct enum values with descriptions
class Priority(str, Enum):
    low = "low"          # Can wait days/weeks
    medium = "medium"    # Should be handled this sprint
    high = "high"        # Needs attention today
    critical = "critical"  # Production is down, fix NOW
```

Enter fullscreen modeExit fullscreen mode

### Pitfall 5: Token Limits and Truncation

Structured output doesn't bypass token limits. If your schema requires a `summary` field with `max_length=500` but the model hits `max_tokens` before completing the JSON, you get:

```
{"title": "Analysis", "summary": "The product shows excellent performance in
```

Enter fullscreen modeExit fullscreen mode

That's invalid JSON. The response is cut off.

**Solution**: Always set `max_tokens` significantly higher than your expected output, and handle the `finish_reason`:

```
response = client.beta.chat.completions.parse(
    model="gpt-5-mini",
    messages=[...],
    response_format=MySchema,
    max_tokens=4096,  # Be generous
)

if response.choices[0].finish_reason == "length":
    # Response was truncated! Retry with higher max_tokens or simpler schema.
    raise ValueError("Response truncated — increase max_tokens or simplify schema")
```

Enter fullscreen modeExit fullscreen mode

### Pitfall 6: The Refusal Trap (OpenAI Specific)

OpenAI's structured output can _refuse_ to generate content if the input triggers safety filters. When this happens, `message.parsed` is `None` and `message.refusal` contains the reason.

```
response = client.beta.chat.completions.parse(
    model="gpt-5-mini",
    messages=[\
        {"role": "user", "content": "Analyze this customer complaint: [potentially sensitive content]"}\
    ],
    response_format=Analysis,
)

parsed = response.choices[0].message.parsed
refusal = response.choices[0].message.refusal

if refusal:
    # Don't crash! Handle gracefully.
    print(f"Model refused: {refusal}")
    # Fallback: use a different model, rephrase, or flag for human review
elif parsed:
    process(parsed)
```

Enter fullscreen modeExit fullscreen mode

* * *

## Pydantic vs Zod: The Definitive Comparison

If you're choosing between Python and TypeScript for your LLM pipeline, here's how the validation libraries compare:

```
Feature                  Pydantic (Python)     Zod (TypeScript)
───────────────────────  ────────────────────  ────────────────────
Type inference           From annotations      From .infer<>
Runtime validation       Built-in              Built-in
JSON Schema export       .model_json_schema()  zodToJsonSchema()
Default values           Field(default=...)    .default(value)
Custom validators        @field_validator      .refine() / .transform()
Nested objects           Native                Native
Discriminated unions     Supported             .discriminatedUnion()
Recursive schemas        Supported             z.lazy()
Serialization            .model_dump()         N/A (plain objects)
ORM integration          Yes (SQLAlchemy)      Drizzle/Prisma
Community size           Massive               Massive
OpenAI native support    Yes (.parse)          Yes (zodResponseFormat)
Anthropic integration    .model_json_schema()  zodToJsonSchema()
```

Enter fullscreen modeExit fullscreen mode

### When to Use Pydantic

```
# Pydantic shines for complex data pipelines:
from pydantic import BaseModel, Field, field_validator, model_validator

class Invoice(BaseModel):
    items: list[LineItem]
    subtotal: float
    tax_rate: float = Field(ge=0, le=0.5)
    total: float

    @model_validator(mode='after')
    def validate_total(self) -> 'Invoice':
        expected = self.subtotal * (1 + self.tax_rate)
        if abs(self.total - expected) > 0.01:
            raise ValueError(
                f'Total {self.total} does not match '
                f'subtotal {self.subtotal} × (1 + {self.tax_rate}) = {expected}'
            )
        return self
```

Enter fullscreen modeExit fullscreen mode

### When to Use Zod

```
// Zod shines for API validation and type-safe pipelines:
const InvoiceSchema = z.object({
  items: z.array(LineItemSchema),
  subtotal: z.number().positive(),
  taxRate: z.number().min(0).max(0.5),
  total: z.number().positive(),
}).refine(
  (data) => Math.abs(data.total - data.subtotal * (1 + data.taxRate)) < 0.01,
  { message: 'Total does not match subtotal × (1 + taxRate)' }
);

// Type is automatically inferred — no separate interface needed
type Invoice = z.infer<typeof InvoiceSchema>;
```

Enter fullscreen modeExit fullscreen mode

* * *

## Advanced Pattern: Schema Composition for Complex Workflows

Real-world applications rarely need a single schema. Here's how to compose schemas for a multi-step extraction pipeline:

```
from pydantic import BaseModel, Field
from enum import Enum
from openai import OpenAI

client = OpenAI()

# Step 1: Quick classification (fast, cheap model)
class TicketType(str, Enum):
    bug = "bug"
    feature = "feature"
    question = "question"
    billing = "billing"

class QuickClassification(BaseModel):
    type: TicketType
    language: str = Field(description="Programming language if applicable, else 'N/A'")
    needs_human: bool

# Step 2: Detailed extraction (only for bugs, use smarter model)
class BugReport(BaseModel):
    title: str = Field(max_length=100)
    steps_to_reproduce: list[str] = Field(min_length=1)
    expected_behavior: str
    actual_behavior: str
    environment: dict[str, str]  # {"os": "...", "browser": "...", etc}
    severity: str = Field(description="minor, major, or critical")

# Step 3: Auto-routing
class RoutingDecision(BaseModel):
    team: str = Field(description="backend, frontend, infra, or billing")
    priority: int = Field(ge=1, le=5)
    suggested_assignee: str | None
    auto_reply: str = Field(max_length=500)

async def process_ticket(text: str):
    # Step 1: Classify (cheap, fast)
    classification = await extract(text, QuickClassification, model="gpt-5-mini")

    if classification.needs_human:
        return route_to_human(text)

    # Step 2: Extract details (only if bug)
    details = None
    if classification.type == TicketType.bug:
        details = await extract(text, BugReport, model="gpt-5")

    # Step 3: Route
    context = f"Type: {classification.type}. "
    if details:
        context += f"Severity: {details.severity}. Steps: {details.steps_to_reproduce}"

    routing = await extract(context, RoutingDecision, model="gpt-5-mini")

    return {
        "classification": classification,
        "details": details,
        "routing": routing,
    }
```

Enter fullscreen modeExit fullscreen mode

* * *

## Cost Optimization: Structured Output Isn't Free

Structured output adds overhead. Here's what it costs:

```
Cost factors for structured output:

1. Schema tokens: The JSON schema is included in the system prompt.
   Simple schema (3 fields):  ~50 tokens  ($0.00001)
   Complex schema (20 fields): ~500 tokens ($0.0001)
   Very complex (nested):      ~2000 tokens ($0.0004)

2. Output tokens: Structured output generates more tokens than free text.
   "The sentiment is positive" = 5 tokens
   {"sentiment": "positive"}  = 7 tokens (~40% more)
   Full structured response = 2-3x the tokens of a free text summary

3. Latency overhead: Constrained decoding adds ~10-30% latency.

Monthly cost impact (1M requests/day):
────────────────────────────────────────────────────
Approach               Tokens/req  Cost/month  Latency
Free text response     50          $1,500      200ms
Simple structured      70          $2,100      250ms
Complex structured     200         $6,000      400ms

Savings strategy:
  → Use structured output ONLY where you need it
  → Use free text for summaries, structured for data extraction
  → Cache responses aggressively (same input = same output)
  → Use gpt-5-mini for classification, gpt-5 for complex extraction
```

Enter fullscreen modeExit fullscreen mode

* * *

## The Decision Framework

Not everything needs structured output. Here's when to use it:

```
Use Structured Output when:
  ✅ Output feeds directly into code (API responses, database inserts)
  ✅ You need type guarantees (numbers must be numbers, not strings)
  ✅ Multiple downstream consumers depend on consistent format
  ✅ You're building automated pipelines (no human in the loop)
  ✅ Data extraction from unstructured text (emails, documents, logs)

Don't use Structured Output when:
  ❌ Output is shown directly to users (chat, content generation)
  ❌ You need creative, free-form responses
  ❌ The schema would be more complex than the task
  ❌ You're prototyping and the schema is changing daily
  ❌ Cost is a major concern and free text works fine
```

Enter fullscreen modeExit fullscreen mode

* * *

## What's Coming Next

### 2026 Q1–Q2 (Now)

- ✅ OpenAI structured output GA with streaming
- ✅ Anthropic tool use stable across Claude Sonnet/Opus
- ✅ Gemini 2.5 native JSON mode with schema enforcement
- 🔄 Pydantic v3 beta with native LLM integration hooks
- 🔄 Zod v4 with improved JSON Schema compatibility

### 2026 Q3–Q4

- Cross-provider schema portability (one schema, any LLM)
- Streaming partial objects with field-level callbacks
- Schema auto-generation from TypeScript interfaces (no Zod needed)
- Constrained decoding for images and audio (multimodal structured output)

### 2027 and Beyond

- Structured output becomes the default (free text becomes opt-in)
- LLMs that can negotiate schema changes at runtime
- Embedded validation directly in model weights (no FSM needed)

* * *

## Conclusion

Structured output in 2026 is no longer optional for production LLM applications. The days of regex-parsing GPT responses and praying are over.

**The key takeaways:**

1.  **Use native structured output** (OpenAI's `.parse()`, Gemini's `response_schema`). Don't roll your own JSON parser.
2.  **Always validate** with Pydantic or Zod, even when the provider guarantees schema compliance. Business logic validation catches what JSON Schema can't.
3.  **Watch the cost**. Complex schemas are expensive. Break them into smaller, parallelized calls.
4.  **Handle edge cases**: refusals, truncation, empty arrays, and enum confusion will bite you in production.
5.  **Build fallback chains**. No single provider is 100% reliable. Use multi-provider patterns for critical paths.

The real question isn't "should I use structured output?" It's "why are you still parsing free text with regex in 2026?"

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="structured-output-with-gemini-models-begging-threatening-and.md">
<details>
<summary>**Structured Output with Gemini Models: Begging, Threatening, and JSON-ing**</summary>

Phase: [EXPLORATION]

**Source URL:** <https://medium.com/google-cloud/structured-output-with-gemini-models-begging-borrowing-and-json-ing-f70ffd60eae6>

# **Structured Output with Gemini Models: Begging, Threatening, and JSON-ing**

[https://miro.medium.com/v2/da:true/resize:fill:32:32/0*cnCUzXRXv03KqbC0](https://medium.com/@terraccianosaverio?source=post_page---byline--f70ffd60eae6---------------------------------------)

[Saverio Terracciano](https://medium.com/@terraccianosaverio?source=post_page---byline--f70ffd60eae6---------------------------------------)

7 min read

·

Apr 8, 2025

17

2

Hello world! It’s been a while, hasn’t it? My last article was… well, let’s just say my daughter was still a theoretical concept back then. Now, she’s a very real, _very time-consuming_ toddler, and outside of work, my free time has been significantly reduced by diaper changes and deciphering toddler-speak. Luckily, I have never been big on sleep, so I managed to find some time to be back. Hopefully, in a consistent way and not for the sporadic quiet night.

During the past months, however, I’ve been able to be active in the local tech community, running meetups, workshops, and fireside chats. Unsurprisingly, the hottest topic has been AI/ML, specifically, the ever-evolving world of large language models (LLMs).

While the average user is engaged in chat sessions with the flavour of the month LLM, many developers are instead eager to integrate these powerful APIs into their applications as they would with other standard web services. From that desire, more often than not, emerges a common pain point: getting LLMs to play nice with structured data.

**The Art of Persuasion (and Occasional Threats)**

You see, many developers find themselves in a strange negotiation with their chosen LLM. They need structured output, typically JSON or XML, to feed into their systems. The approaches I’ve witnessed range from polite requests:

```
“Please, oh wise and powerful LLM, could you possibly provide your response in JSON format?”
```

To stern directives:

```
“Respond ONLY in JSON. Do not include any other text.”
```

And even, occasionally, to veiled (or not-so-veiled) threats:

```
“If you don’t give me JSON, I’m switching to [Competitor LLM]!”
```

Yes, everyone has their own unique approach, some even swear by it, but more often than not an update, a special character, or just that one important invocation can screw it up and leave you always uneasy.

The problem is that many LLMs are primarily trained for natural language generation, not strict data formatting. They _can_ produce JSON, but it often requires a lot of prompt engineering and a healthy dose of luck.

**Gemini to the Rescue: Natively Structured Output**

At my meetups, I often suggest giving Google AI Studio a try. It’s a free and easy way to experiment, to try the latest models and play with the hidden levers of Gemini/Gemma models. I definitely have to write an article about AI Studio, but specifically in this case, it’s a great fit because it exposes visually one of the best capabilities of the Gemini models: their native support for structured output. This isn’t some tacked-on afterthought / forced constraint; it’s baked right into the model’s DNA. I believe this has been possible since the 1.5 Pro release, but it’s certainly a key feature now. This means you can _reliably_ get JSON (or other structured formats, though JSON is the focus here) without resorting to prompt-engineering shenanigans.

**How It Works: AI Studio and Beyond**

While this is possible by directly consuming the API, if you have never used it, I think it’s best to see it visually first.

Let’s start with the easiest way to see this in action: think of an example scenario for your API response and navigate to Google AI Studio ( [https://ai.google.dev/](https://ai.google.dev/))’s web-based IDE, and let’s give it a try!

1. **Start a New Prompt:** From the top left, select “Create Prompt”.

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*iDnDtDGtG_jiBdYEzYraKg.png

2\. **Enable Structured Output:** In the right-hand panel, under “Tools”, you should find a switch with the text “Structured output”. Switch it on.

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*QZKy0zs0tyiLHQMJXOVJLw.png

3. **Define Your Schema:** This is the crucial part. You’ll need to provide a clear schema that defines the structure of your desired JSON output. You use a subset of JSON schema for that. For this example, we will imagine we want to extract information about a book. The schema we need for our application might look like this:

```
 {
 “type”: “object”,
 “properties”: {
   “title”: {
     “type”: “string”,
     “description”: “The title of the book”
    },
   “author”: {
     “type”: “string”,
     “description”: “The author of the book”
    },
   “publication_year”: {
     “type”: “integer”,
     “description”: “The year the book was published”
    }
 },
 “required”: [“title”, “author”]
 }
```

**Key Syntax Points:**

- _type:_ Defines the basic data type (e.g., “string”, “integer”, “object”, “array”, “boolean”).
- _properties:_ (For objects) Defines the fields within the object and their respective types.
- _description:_ \*Optional but important!\* This provides context to the model about what each field represents. The better your descriptions, the more accurate the output.
- _required:_ An array of field names that _must_ be present in the output. If the model can’t confidently extract a required field, it will (generally) return an error or indicate the missing information appropriately.
- _items:_ (For arrays) Defines the type of elements that should be inside the array.

You can achieve this by specifying your intended schema in the **“Code Editor”** tab, or if you want to be assisted more, you can use the **“Visual Editor”** tab and proceed to specify your properties with related types one by one.

You can also switch back and forth between them, and it can be a good way to provide the initial skeleton for your data model.

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*cT9nK-nw5EHUwuutL--Bvw.png

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*ZbFVHARdCdoc_Ns8wwwqnA.png

4\. **Craft Your Input:** Provide the text you want the model to process. It can contain a full prompt, or in a simple enough scenario, you can just provide an entity that can be directly mapped to your schema. For example:

```
 “The Hitchhiker’s Guide to the Galaxy, a science fiction comedy series created by Douglas Adams, was originally a radio comedy broadcast on BBC Radio 4 in 1978.”
```

5\. **Run the Prompt:** Hit “Run” and watch the magic happen. You should get JSON output that adheres to your schema:

```
 {
 “title”: “The Hitchhiker’s Guide to the Galaxy”,
 “author”: “Douglas Adams”,
 “publication_year”: 1978
 }
```

_Note: The publication year might not be perfectly extracted from the example input. This highlights the importance of providing clear and accurate input text._

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*PFXDnqDRE-t_11QVpOpiWg.png

**Beyond AI Studio: “ _Get Code_”**

The beauty of AI Studio is that it’s not just a children's playground. It’s a powerful tool for generating integration-ready code. Click the “ **Get Code**” button, and you’ll be presented with code snippets in your preferred language (Python, Node.js, Java, Curl, etc.) that demonstrate how to use the Gemini API to achieve the same structured output.

Let’s assume I am not great at Python, but I might want to integrate our current example, via the Get Code functionality, I might get something like this:

```

import base64
import os
from google import genai
from google.genai import types

def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [\
        types.Content(\
            role="user",\
            parts=[\
                types.Part.from_text(text="""\"The Hitchhiker's Guide to the Galaxy, a science fiction comedy series created by Douglas Adams, was originally a radio comedy broadcast on BBC Radio 4 in 1978.\""""),\
            ],\
        ),\
        types.Content(\
            role="model",\
            parts=[\
                types.Part.from_text(text="""{\
  \"author\": \"Douglas Adams\",\
  \"title\": \"The Hitchhiker's Guide to the Galaxy\",\
  \"publication_year\": 1978\
}"""),\
            ],\
        ),\
        types.Content(\
            role="user",\
            parts=[\
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),\
            ],\
        ),\
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["title", "author"],
            properties = {
                "title": genai.types.Schema(
                    type = genai.types.Type.STRING,
                    description = "The title of the book",
                ),
                "author": genai.types.Schema(
                    type = genai.types.Type.STRING,
                    description = "The author of the book",
                ),
                "publication_year": genai.types.Schema(
                    type = genai.types.Type.INTEGER,
                    description = "The year the book was published",
                ),
            },
        ),
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
```

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*-rYmiRQrDNwU4LxDmfxSOg.png

Remember that to be able to run this code in your environment, you will need to obtain an API key, which is very convenient and easy to obtain within AI Studio by pressing the prominently displayed “Get API key button” and replacing the key you obtain in the corresponding parameter in the generated code.

https://miro.medium.com/v2/resize:fit:254/1*7pWgdWnqJjdAEI6JL5wPVg.png

**Key Takeaways and Next Steps**

- **Reliable Structure:** Gemini’s native structured output eliminates the guesswork and fragility of relying solely on prompt engineering.
- **Clear Schema is Key**: The quality of your schema directly impacts the quality of the output. Be precise and descriptive.
- **Iterate and Refine**: Experiment with different schemas and input variations in AI Studio to fine-tune your results.
- **Seamless Integration:** The “Get Code” functionality makes it trivial to integrate this capability into your existing applications.
- **Error Handling:** The model does provide useful feedback, like the mention that a field is missing. You should leverage that.

Once you become familiar, or if your intended use case requires a more complex response structure, it will be worth checking the full specifications of the OpenAPI Schema ( [https://spec.openapis.org/oas/v3.0.3#schema](https://spec.openapis.org/oas/v3.0.3#schema)) and Gemini’s structured output own documentation ( [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output))

I found this capability to be a game-changer for myself and imagine likewise for developers who need to reliably extract structured data from unstructured text. It opens up a whole new world of possibilities for building robust and intelligent applications. No more begging, borrowing, or threatening your LLM! Just well-defined schemas and predictable JSON.

As usual, if you have any questions, or just want to share your cool Gemini projects, you know where to find me — DMs are always open on Twitter ( [@TetsuoRyuu](http://twitter.com/TetsuoRyuu))…yes, still calling it Twitter. I should also really start using BlueSky after having created my profile (@ [tetsuoryuu.bsky.socia](https://bsky.app/profile/tetsuoryuu.bsky.social) l). I might be a little slow to respond these days (thanks, toddler!), but I’ll get back to you. Now, if you’ll excuse me, I hear the distinct sound of a small, adorable, human demanding my attention… and a not-necessarily-JSON-formatted snack.

[Gemini](https://medium.com/tag/gemini?source=post_page-----f70ffd60eae6---------------------------------------)

[AI](https://medium.com/tag/ai?source=post_page-----f70ffd60eae6---------------------------------------)

[Google](https://medium.com/tag/google?source=post_page-----f70ffd60eae6---------------------------------------)

[LLM](https://medium.com/tag/llm?source=post_page-----f70ffd60eae6---------------------------------------)

[API](https://medium.com/tag/api?source=post_page-----f70ffd60eae6---------------------------------------)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="the-complete-guide-to-using-pydantic-for-validating-llm-outp.md">
<details>
<summary>The Complete Guide to Using Pydantic for Validating LLM Outputs</summary>

Phase: [EXPLORATION]

**Source URL:** <https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs>

# The Complete Guide to Using Pydantic for Validating LLM Outputs

In this article, you will learn how to turn free-form large language model (LLM) text into reliable, schema-validated Python objects with Pydantic.

Topics we will cover include:

- Designing robust Pydantic models (including custom validators and nested schemas).
- Parsing “messy” LLM outputs safely and surfacing precise validation errors.
- Integrating validation with OpenAI, LangChain, and LlamaIndex plus retry strategies.

Let’s break it down.

https://machinelearningmastery.com/wp-content/uploads/2025/12/mlm-complete-guide-pydantic-featured-image.jpeg

The Complete Guide to Using Pydantic for Validating LLM Outputs

Image by Editor

## Introduction

Large language models generate text, not structured data. Even when you prompt them to return structured data, they’re still generating text that _looks_ like valid JSON. The output may have incorrect field names, missing required fields, wrong data types, or extra text wrapped around the actual data. Without validation, these inconsistencies cause runtime errors that are difficult to debug.

**Pydantic** helps you validate data at runtime using Python type hints. It checks that LLM outputs match your expected schema, converts types automatically where possible, and provides clear error messages when validation fails. This gives you a reliable contract between the LLM’s output and your application’s requirements.

This article shows you how to use Pydantic to validate LLM outputs. You’ll learn how to define validation schemas, handle malformed responses, work with nested data, integrate with LLM APIs, implement retry logic with validation feedback, and more. Let’s not waste any more time.

🔗 You can find the code **on GitHub**. Before you go ahead, **install Pydantic** version 2.x with the optional email dependencies: `pip install pydantic[email]`.

## Getting Started

Let’s start with a simple example by building a tool that extracts contact information from text. The LLM reads unstructured text and returns structured data that we validate with Pydantic:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18 | from pydantic import BaseModel,EmailStr,field\_validator<br>from typing import Optional<br>classContactInfo(BaseModel):<br>name:str<br>email:EmailStr<br>phone:Optional\[str\]=None<br>company:Optional\[str\]=None<br>@field\_validator('phone')<br>@classmethod<br>def validate\_phone(cls,v):<br>ifvisNone:<br>returnv<br>cleaned=''.join(filter(str.isdigit,v))<br>iflen(cleaned)<10:<br>raise ValueError('Phone number must have at least 10 digits')<br>returncleaned |

All Pydantic models inherit from `BaseModel`, which provides automatic validation. Type hints like `name: str` help Pydantic validate types at runtime. The `EmailStr` type validates email format without needing a custom regex. Fields marked with `Optional[str] = None` can be missing or null. The `@field_validator` decorator lets you add custom validation logic, like cleaning phone numbers and checking their length.

Here’s how to use the model to validate sample LLM output:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17 | import json<br>llm\_response='''<br>{<br>    "name": "Sarah Johnson",<br>    "email": "sarah.johnson@techcorp.com",<br>    "phone": "(555) 123-4567",<br>    "company": "TechCorp Industries"<br>}<br>'''<br>data=json.loads(llm\_response)<br>contact=ContactInfo(\*\*data)<br>print(contact.name)<br>print(contact.email)<br>print(contact.model\_dump()) |

When you create a `ContactInfo` instance, Pydantic validates everything automatically. If validation fails, you get a clear error message telling you exactly what went wrong.

## Parsing and Validating LLM Outputs

LLMs don’t always return perfect JSON. Sometimes they add markdown formatting, explanatory text, or mess up the structure. Here’s how to handle these cases:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39 | from pydantic import BaseModel,ValidationError,field\_validator<br>import json<br>import re<br>classProductReview(BaseModel):<br>product\_name:str<br>rating:int<br>review\_text:str<br>would\_recommend:bool<br>@field\_validator('rating')<br>@classmethod<br>def validate\_rating(cls,v):<br>ifnot1<=v<=5:<br>raise ValueError('Rating must be an integer between 1 and 5')<br>returnv<br>def extract\_json\_from\_llm\_response(response:str)->dict:<br>"""Extract JSON from LLM response that might contain extra text."""<br>json\_match=re.search(r'\\{.\*\\}',response,re.DOTALL)<br>ifjson\_match:<br>returnjson.loads(json\_match.group())<br>raise ValueError("No JSON found in response")<br>def parse\_review(llm\_output:str)->ProductReview:<br>"""Safely parse and validate LLM output."""<br>try:<br>data=extract\_json\_from\_llm\_response(llm\_output)<br>review=ProductReview(\*\*data)<br>returnreview<br>except json.JSONDecodeError ase:<br>print(f"JSON parsing error: {e}")<br>raise<br>except ValidationError ase:<br>print(f"Validation error: {e}")<br>raise<br>except Exception ase:<br>print(f"Unexpected error: {e}")<br>raise |

This approach uses regex to find JSON within response text, handling cases where the LLM adds explanatory text before or after the data. We catch different exception types separately:

- `JSONDecodeError` for malformed JSON,
- `ValidationError` for data that doesn’t match the schema, and
- General exceptions for unexpected issues.

The `extract_json_from_llm_response` function handles text cleanup while `parse_review` handles validation, keeping concerns separated. In production, you’d want to log these errors or retry the LLM call with an improved prompt.

This example shows an LLM response with extra text that our parser handles correctly:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | messy\_response='''<br>Here'sthe review inJSON format:<br>{<br>"product\_name":"Wireless Headphones X100",<br>"rating":4,<br>"review\_text":"Great sound quality, comfortable for long use.",<br>"would\_recommend":true<br>}<br>Hope thishelps!<br>'''<br>review=parse\_review(messy\_response)<br>print(f"Product: {review.product\_name}")<br>print(f"Rating: {review.rating}/5") |

The parser extracts the JSON block from the surrounding text and validates it against the `ProductReview` schema.

## Working with Nested Models

Real-world data is rarely flat. Here’s how to handle nested structures like a product with multiple reviews and specifications:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33 | from pydantic import BaseModel,Field,field\_validator<br>from typing import List<br>classSpecification(BaseModel):<br>key:str<br>value:str<br>classReview(BaseModel):<br>reviewer\_name:str<br>rating:int=Field(...,ge=1,le=5)<br>comment:str<br>verified\_purchase:bool=False<br>classProduct(BaseModel):<br>id:str<br>name:str<br>price:float=Field(...,gt=0)<br>category:str<br>specifications:List\[Specification\]<br>reviews:List\[Review\]<br>average\_rating:float=Field(...,ge=1,le=5)<br>@field\_validator('average\_rating')<br>@classmethod<br>def check\_average\_matches\_reviews(cls,v,info):<br>reviews=info.data.get('reviews',\[\])<br>ifreviews:<br>calculated\_avg=sum(r.rating forrinreviews)/len(reviews)<br>ifabs(calculated\_avg-v)>0.1:<br>raise ValueError(<br>f'Average rating {v} does not match calculated average {calculated\_avg:.2f}'<br>)<br>returnv |

The `Product` model contains lists of Specification and Review objects, and each nested model is validated independently. Using `Field(..., ge=1, le=5)` adds constraints directly in the type hint, where `ge` means “greater than or equal” and `gt` means “greater than”.

The `check_average_matches_reviews` validator accesses other fields using `info.data`, allowing you to validate relationships between fields. When you pass nested dictionaries to `Product(**data)`, Pydantic automatically creates the nested Specification and Review objects.

This structure ensures data integrity at every level. If a single review is malformed, you’ll know exactly which one and why.

This example shows how nested validation works with a complete product structure:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31 | llm\_response={<br>"id":"PROD-2024-001",<br>"name":"Smart Coffee Maker",<br>"price":129.99,<br>"category":"Kitchen Appliances",<br>"specifications":\[<br>{"key":"Capacity","value":"12 cups"},<br>{"key":"Power","value":"1000W"},<br>{"key":"Color","value":"Stainless Steel"}<br>\],<br>"reviews":\[<br>{<br>"reviewer\_name":"Alex M.",<br>"rating":5,<br>"comment":"Makes excellent coffee every time!",<br>"verified\_purchase":True<br>},<br>{<br>"reviewer\_name":"Jordan P.",<br>"rating":4,<br>"comment":"Good but a bit noisy",<br>"verified\_purchase":True<br>}<br>\],<br>"average\_rating":4.5<br>}<br>product=Product(\*\*llm\_response)<br>print(f"{product.name}: ${product.price}")<br>print(f"Average Rating: {product.average\_rating}")<br>print(f"Number of reviews: {len(product.reviews)}") |

Pydantic validates the entire nested structure in one call, checking that specifications and reviews are properly formed and that the average rating matches the individual review ratings.

## Using Pydantic with LLM APIs and Frameworks

So far, we’ve learned that we need a reliable way to convert free-form text into structured, validated data. Now let’s see how to use Pydantic validation with OpenAI’s API, as well as frameworks like **LangChain** and **LlamaIndex**. **Be sure to install the required SDKs**.

### Using Pydantic with OpenAI API

Here’s how to extract structured data from unstructured text using OpenAI’s API with Pydantic validation:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52 | from openai import OpenAI<br>from pydantic import BaseModel<br>from typing import List<br>import os<br>client=OpenAI(api\_key=os.getenv("OPENAI\_API\_KEY"))<br>classBookSummary(BaseModel):<br>title:str<br>author:str<br>genre:str<br>key\_themes:List\[str\]<br>main\_characters:List\[str\]<br>brief\_summary:str<br>recommended\_for:List\[str\]<br>def extract\_book\_info(text:str)->BookSummary:<br>"""Extract structured book information from unstructured text."""<br>prompt=f"""<br>    Extract book information from the following text and return it as JSON.<br>    Required format:<br>    {{<br>        "title": "book title",<br>        "author": "author name",<br>        "genre": "genre",<br>        "key\_themes": \["theme1", "theme2"\],<br>        "main\_characters": \["character1", "character2"\],<br>        "brief\_summary": "summary in2-3sentences",<br>        "recommended\_for": \["audience1", "audience2"\]<br>    }}<br>    Text: {text}<br>    Return ONLY the JSON, no additional text.<br>    """<br>response=client.chat.completions.create(<br>model="gpt-4o-mini",<br>messages=\[<br>{"role":"system","content":"You are a helpful assistant that extracts structured data."},<br>{"role":"user","content":prompt}<br>\],<br>temperature=0<br>)<br>llm\_output=response.choices\[0\].message.content<br>import json<br>data=json.loads(llm\_output)<br>returnBookSummary(\*\*data) |

The prompt includes the exact JSON structure we expect, guiding the LLM to return data matching our Pydantic model. Setting `temperature=0` makes the LLM more deterministic and less creative, which is what we want for structured data extraction. The system message primes the model to be a data extractor rather than a conversational assistant. Even with careful prompting, we still validate with Pydantic because you should never trust LLM output without verification.

This example extracts structured information from a book description:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | book\_text="""<br>'The Midnight Library' by Matt Haig is a contemporary fiction novel that explores <br>themes of regret, mental health, and the infinite possibilities of life. The story <br>follows Nora Seed, a woman who finds herself in a library between life and death, <br>where each book represents a different life she could have lived. Through her journey, <br>she encounters various versions of herself and must decide what truly makes a life worth living.<br>The book resonates with readers dealing with depression, anxiety, or life transitions.<br>"""<br>try:<br>book\_info=extract\_book\_info(book\_text)<br>print(f"Title: {book\_info.title}")<br>print(f"Author: {book\_info.author}")<br>print(f"Themes: {', '.join(book\_info.key\_themes)}")<br>except Exception ase:<br>print(f"Error extracting book info: {e}") |

The function sends the unstructured text to the LLM with clear formatting instructions, then validates the response against the `BookSummary` schema.

### Using LangChain with Pydantic

LangChain provides built-in support for structured output extraction with Pydantic models. There are two main approaches that handle the complexity of prompt engineering and parsing for you.

The first method uses **PydanticOutputParser**, which works with any LLM by using prompt engineering to guide the model’s output format. The parser automatically generates detailed format instructions from your Pydantic model:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31 | from langchain\_openai import ChatOpenAI<br>from langchain.output\_parsers import PydanticOutputParser<br>from langchain.prompts import PromptTemplate<br>from pydantic import BaseModel,Field<br>from typing import List,Optional<br>classRestaurant(BaseModel):<br>"""Information about a restaurant."""<br>name:str=Field(description="The name of the restaurant")<br>cuisine:str=Field(description="Type of cuisine served")<br>price\_range:str=Field(description="Price range: ,,,𝑜⁢𝑟$$")<br>rating:Optional\[float\]=Field(default=None,description="Rating out of 5.0")<br>specialties:List\[str\]=Field(description="Signature dishes or specialties")<br>def extract\_restaurant\_with\_parser(text:str)->Restaurant:<br>"""Extract restaurant info using LangChain's PydanticOutputParser."""<br>parser=PydanticOutputParser(pydantic\_object=Restaurant)<br>prompt=PromptTemplate(<br>template="Extract restaurant information from the following text.\\n{format\_instructions}\\n{text}\\n",<br>input\_variables=\["text"\],<br>partial\_variables={"format\_instructions":parser.get\_format\_instructions()}<br>)<br>llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)<br>chain=prompt\|llm\|parser<br>result=chain.invoke({"text":text})<br>returnresult |

The PydanticOutputParser automatically generates format instructions from your Pydantic model, including field descriptions and type information. It works with any LLM that can follow instructions and doesn’t require function calling support. The chain syntax makes it easy to compose complex workflows.

The second method is to use the native function calling capabilities of modern LLMs through the **with\_structured\_output()** **function**:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | def extract\_restaurant\_structured(text:str)->Restaurant:<br>"""Extract restaurant info using with\_structured\_output."""<br>llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)<br>structured\_llm=llm.with\_structured\_output(Restaurant)<br>prompt=PromptTemplate.from\_template(<br>"Extract restaurant information from the following text:\\n\\n{text}"<br>)<br>chain=prompt\|structured\_llm<br>result=chain.invoke({"text":text})<br>returnresult |

This method produces cleaner, more concise code and makes use of the model’s native function calling capabilities for more reliable extraction. You don’t need to manually create parsers or format instructions, and it’s generally more accurate than prompt-based approaches.

Here’s an example of how to use these functions:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | restaurant\_text="""<br>Mama's Italian Kitchen is a cozy family-owned restaurant serving authentic <br>Italian cuisine. Rated 4.5 stars, it's known for its homemade pasta and <br>wood-fired pizzas. Prices are moderate ($$), and their signature dishes <br>include lasagna bolognese and tiramisu.<br>"""<br>try:<br>restaurant\_info=extract\_restaurant\_structured(restaurant\_text)<br>print(f"Restaurant: {restaurant\_info.name}")<br>print(f"Cuisine: {restaurant\_info.cuisine}")<br>print(f"Specialties: {', '.join(restaurant\_info.specialties)}")<br>except Exception ase:<br>print(f"Error: {e}") |

### Using LlamaIndex with Pydantic

LlamaIndex provides multiple approaches for structured extraction, with particularly strong integration for document-based workflows. It’s especially useful when you need to extract structured data from large document collections or build RAG systems.

The most straightforward approach in LlamaIndex is using **LLMTextCompletionProgram**, which requires minimal boilerplate code:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30 | from llama\_index.core.program import LLMTextCompletionProgram<br>from pydantic import BaseModel,Field<br>from typing import List,Optional<br>classProduct(BaseModel):<br>"""Information about a product."""<br>name:str=Field(description="Product name")<br>brand:str=Field(description="Brand or manufacturer")<br>category:str=Field(description="Product category")<br>price:float=Field(description="Price in USD")<br>features:List\[str\]=Field(description="Key features")<br>rating:Optional\[float\]=Field(default=None,description="Customer rating out of 5")<br>def extract\_product\_simple(text:str)->Product:<br>"""Extract product info using LlamaIndex's simple approach."""<br>prompt\_template\_str="""<br>    Extract product information from the following text and structure it properly:<br>    {text}<br>    """<br>program=LLMTextCompletionProgram.from\_defaults(<br>output\_cls=Product,<br>prompt\_template\_str=prompt\_template\_str,<br>verbose=False<br>)<br>result=program(text=text)<br>returnresult |

The `output_cls` parameter automatically handles Pydantic validation. This works with any LLM through prompt engineering and is good for quick prototyping and simple extraction tasks.

For models that support function calling, you can use **FunctionCallingProgram**. And when you need explicit control over parsing behavior, you can use the **PydanticOutputParser** method:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26 | from llama\_index.core.program import LLMTextCompletionProgram<br>from llama\_index.core.output\_parsers import PydanticOutputParser<br>from llama\_index.llms.openai import OpenAI<br>def extract\_product\_with\_parser(text:str)->Product:<br>"""Extract product info using explicit parser."""<br>prompt\_template\_str="""<br>    Extract product information from the following text:<br>    {text}<br>    {format\_instructions}<br>    """<br>llm=OpenAI(model="gpt-4o-mini",temperature=0)<br>program=LLMTextCompletionProgram.from\_defaults(<br>output\_parser=PydanticOutputParser(output\_cls=Product),<br>prompt\_template\_str=prompt\_template\_str,<br>llm=llm,<br>verbose=False<br>)<br>result=program(text=text)<br>returnresult |

Here’s how you’d extract product information in practice:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | product\_text="""<br>The Sony WH-1000XM5 wireless headphones feature industry-leading noise cancellation,<br>exceptional sound quality, and up to 30 hours of battery life. Priced at $399.99,<br>these premium headphones include Adaptive Sound Control, multipoint connection,<br>and speak-to-chat technology. Customers rate them 4.7 out of 5 stars.<br>"""<br>try:<br>product\_info=extract\_product\_with\_parser(product\_text)<br>print(f"Product: {product\_info.name}")<br>print(f"Brand: {product\_info.brand}")<br>print(f"Price: ${product\_info.price}")<br>print(f"Features: {', '.join(product\_info.features)}")<br>except Exception ase:<br>print(f"Error: {e}") |

Use explicit parsing when you need custom parsing logic, are working with models that don’t support function calling, or are debugging extraction issues.

## Retrying LLM Calls with Better Prompts

When the LLM returns invalid data, you can retry with an improved prompt that includes the error message from the failed validation attempt:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38 | from pydantic import BaseModel,ValidationError<br>from typing import Optional<br>import json<br>classEventExtraction(BaseModel):<br>event\_name:str<br>date:str<br>location:str<br>attendees:int<br>event\_type:str<br>def extract\_with\_retry(llm\_call\_function,max\_retries:int=3)->Optional\[EventExtraction\]:<br>"""Try to extract valid data, retrying with error feedback if validation fails."""<br>last\_error=None<br>forattempt inrange(max\_retries):<br>try:<br>response=llm\_call\_function(last\_error)<br>data=json.loads(response)<br>returnEventExtraction(\*\*data)<br>except ValidationError ase:<br>last\_error=str(e)<br>print(f"Attempt {attempt + 1} failed: {last\_error}")<br>ifattempt==max\_retries-1:<br>print("Max retries reached, giving up")<br>returnNone<br>except json.JSONDecodeError:<br>print(f"Attempt {attempt + 1}: Invalid JSON")<br>last\_error="The response was not valid JSON. Please return only valid JSON."<br>ifattempt==max\_retries-1:<br>returnNone<br>returnNone |

Each retry includes the previous error message, helping the LLM understand what went wrong. After `max_retries`, the function returns `None` instead of crashing, allowing the calling code to handle the failure gracefully. Printing each attempt’s error makes it easy to debug why extraction is failing.

In a real application, your `llm_call_function` would construct a new prompt including the Pydantic error message, like `"Previous attempt failed with error: {error}. Please fix and try again."`

This example shows the retry pattern with a mock LLM function that progressively improves:

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17 | def mock\_llm\_call(previous\_error:Optional\[str\]=None)->str:<br>"""Simulate an LLM that improves based on error feedback."""<br>ifprevious\_error isNone:<br>return'{"event\_name": "Tech Conference 2024", "date": "2024-06-15", "location": "San Francisco"}'<br>elif"attendees"inprevious\_error.lower():<br>return'{"event\_name": "Tech Conference 2024", "date": "2024-06-15", "location": "San Francisco", "attendees": "about 500", "event\_type": "Conference"}'<br>else:<br>return'{"event\_name": "Tech Conference 2024", "date": "2024-06-15", "location": "San Francisco", "attendees": 500, "event\_type": "Conference"}'<br>result=extract\_with\_retry(mock\_llm\_call)<br>ifresult:<br>print(f"\\nSuccess! Extracted event: {result.event\_name}")<br>print(f"Expected attendees: {result.attendees}")<br>else:<br>print("Failed to extract valid data") |

The first attempt misses the required `attendees` field, the second attempt includes it but with the wrong type, and the third attempt gets everything correct. The retry mechanism handles these progressive improvements.

## Conclusion

Pydantic helps you go from unreliable LLM outputs into validated, type-safe data structures. By combining clear schemas with robust error handling, you can build AI-powered applications that are both powerful and reliable.

Here are the key takeaways:

- Define clear schemas that match your needs
- Validate everything and handle errors gracefully with retries and fallbacks
- Use type hints and validators to enforce data integrity
- Include schemas in your prompts to guide the LLM

Start with simple models and add validation as you find edge cases in your LLM outputs. Happy exploring!

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Notebook 1</summary>

# Notebook 1

## Summary
Repository: towardsai/course-ai-agents
Commit: 56142b3f4c0110a697e644d38aa988be10e38b69
Subpath: /lessons/04_structured_outputs
Files analyzed: 1

Estimated tokens: 3.7k

## File tree
```Directory structure:
└── 04_structured_outputs/
    └── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/04_structured_outputs/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 4: Structured Outputs

This notebook explores **Structured Outputs** for guiding LLM outputs.

We will use the `google-genai` library to interact with Google's Gemini models.

**Learning Objectives:**

1.  **Understand structured outputs** and why they are crucial for reliable data extraction from LLMs.
2.  **Enforce structured data formats (JSON)** from an LLM using prompt engineering techniques.
3.  **Leverage Pydantic models** to define and manage complex data structures for structured outputs, improving code robustness and clarity.
4.  **Use Gemini's native structured output capabilities** for the most reliable and efficient approach.
"""

"""
## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:
"""

%load_ext autoreload
%autoreload 2

"""
### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL;DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.
"""

"""
### Configure Gemini API

To configure the Gemini API, follow the step-by-step instructions from the `Course Admin` lesson.

But here is a quick check on what you need to run this Notebook:

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  From the root of your project, run: `cp .env.example .env` 
3.  Within the `.env` file, fill in the `GOOGLE_API_KEY` variable:

Now, the code below will load the key from the `.env` file:
"""

from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Trying to load environment variables from `/Users/fabio/Desktop/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

import json

from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()

"""
### Define Constants

We will use the `gemini-3.5-flash` model, which is fast and cost-effective:
"""

MODEL_ID = "gemini-3.5-flash"

"""
## 2. Implementing structured outputs from scratch using JSON

Sometimes, you don't need the LLM to take an action, but you need its output in a specific, machine-readable format. Forcing the output to be JSON is a common way to achieve this.

We can instruct the model to do this by **prompting** clearly describing the desired JSON structure in the prompt.
"""

"""
### Example: Extracting Metadata from a Document

Let's imagine we have a markdown document and we want to extract key information like a summary, tags, and keywords into a clean JSON object.
"""

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

response = client.models.generate_content(model=MODEL_ID, contents=prompt)

pretty_print.wrapped(text=response.text, title="Raw LLM Output", indent=2)
# Output:
#   [93m------------------------------------------ Raw LLM Output ------------------------------------------[0m

#     ```json

#   {

#       "summary": "The Q3 2023 financial report highlights a strong performance with a 20% increase in revenue and 15% growth in user engagement, surpassing market expectations. This success is attributed to a robust product strategy, effective market positioning, and successful expansion into new markets, leading to improved customer retention and reduced acquisition costs.",

#       "tags": [

#           "financials",

#           "earnings report",

#           "business performance",

#           "revenue growth",

#           "market expansion",

#           "Q3 2023"

#       ],

#       "keywords": [

#           "Q3 2023",

#           "revenue",

#           "user engagement",

#           "market expectations",

#           "product strategy",

#           "market positioning",

#           "digital services",

#           "new markets",

#           "customer acquisition costs",

#           "retention rates",

#           "cash flow"

#       ],

#       "quarter": "Q3 2023",

#       "growth_rate": "20%"

#   }

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


def extract_json_from_response(response: str) -> dict:
    """
    Extracts JSON from a response string that is wrapped in <json> or ```json tags.
    """

    response = response.replace("<json>", "").replace("</json>", "")
    response = response.replace("```json", "").replace("```", "")

    return json.loads(response)

"""
You can now reliably parse the JSON string:
"""

parsed_response = extract_json_from_response(response.text)
pretty_print.wrapped(
    text=[f"Type of the parsed response: `{type(parsed_response)}`", json.dumps(parsed_response, indent=2)],
    title="Parsed JSON Object",
    indent=2,
)
# Output:
#   [93m---------------------------------------- Parsed JSON Object ----------------------------------------[0m

#     Type of the parsed response: `<class 'dict'>`

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "summary": "The Q3 2023 financial report highlights a strong performance with a 20% increase in revenue and 15% growth in user engagement, surpassing market expectations. This success is attributed to a robust product strategy, effective market positioning, and successful expansion into new markets, leading to improved customer retention and reduced acquisition costs.",

#     "tags": [

#       "financials",

#       "earnings report",

#       "business performance",

#       "revenue growth",

#       "market expansion",

#       "Q3 2023"

#     ],

#     "keywords": [

#       "Q3 2023",

#       "revenue",

#       "user engagement",

#       "market expectations",

#       "product strategy",

#       "market positioning",

#       "digital services",

#       "new markets",

#       "customer acquisition costs",

#       "retention rates",

#       "cash flow"

#     ],

#     "quarter": "Q3 2023",

#     "growth_rate": "20%"

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 3. Implementing structured outputs from scratch using Pydantic

While prompting for JSON is effective, it can be fragile. A more robust and modern approach is to use **Pydantic**. Pydantic allows you to define data structures as Python classes. This gives you:

- **A single source of truth**: The Pydantic model defines the structure.
- **Automatic schema generation**: You can easily generate a JSON Schema from the model.
- **Data validation**: You can validate the LLM's output against the model to ensure it conforms to the expected structure and types.

Let's recreate the previous example using Pydantic.
"""

class DocumentMetadata(BaseModel):
    """A class to hold structured metadata for a document."""

    summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
    tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
    keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
    quarter: str = Field(description="The quarter of the financial year described in the document (e.g, Q3 2023).")
    growth_rate: str = Field(description="The growth rate of the company described in the document (e.g, 10%).")

"""
### Injecting Pydantic Schema into the Prompt

We can generate a JSON Schema from our Pydantic model and inject it directly into the prompt. This is a more formal way of telling the LLM what structure to follow.

Note how, along with the field type, we can leverage the Field description automatically to clearly specify to the LLM what each field means.
"""

schema = DocumentMetadata.model_json_schema()
schema
# Output:
#   {'description': 'A class to hold structured metadata for a document.',

#    'properties': {'summary': {'description': 'A concise, 1-2 sentence summary of the document.',

#      'title': 'Summary',

#      'type': 'string'},

#     'tags': {'description': 'A list of 3-5 high-level tags relevant to the document.',

#      'items': {'type': 'string'},

#      'title': 'Tags',

#      'type': 'array'},

#     'keywords': {'description': 'A list of specific keywords or concepts mentioned.',

#      'items': {'type': 'string'},

#      'title': 'Keywords',

#      'type': 'array'},

#     'quarter': {'description': 'The quarter of the financial year described in the document (e.g, Q3 2023).',

#      'title': 'Quarter',

#      'type': 'string'},

#     'growth_rate': {'description': 'The growth rate of the company described in the document (e.g, 10%).',

#      'title': 'Growth Rate',

#      'type': 'string'}},

#    'required': ['summary', 'tags', 'keywords', 'quarter', 'growth_rate'],

#    'title': 'DocumentMetadata',

#    'type': 'object'}

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

response = client.models.generate_content(model=MODEL_ID, contents=prompt)

parsed_response = extract_json_from_response(response.text)

pretty_print.wrapped(
    text=[f"Type of the parsed response: `{type(parsed_response)}`", json.dumps(parsed_response, indent=2)],
    title="Parsed JSON Object",
    indent=2,
)
# Output:
#   [93m---------------------------------------- Parsed JSON Object ----------------------------------------[0m

#     Type of the parsed response: `<class 'dict'>`

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "summary": "The Q3 2023 earnings report indicates strong financial performance with a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy, market expansion, and improved customer retention.",

#     "tags": [

#       "Financial Performance",

#       "Earnings Report",

#       "Business Growth",

#       "Market Expansion",

#       "Customer Metrics"

#     ],

#     "keywords": [

#       "Q3 2023",

#       "revenue increase",

#       "user engagement",

#       "digital services",

#       "new markets",

#       "customer acquisition costs",

#       "retention rates",

#       "cash flow"

#     ],

#     "quarter": "Q3 2023",

#     "growth_rate": "20%"

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
As you can see, conceptually, the results are the same. But now, we can easily validate the output with Pydantic:
"""

try:
    document_metadata = DocumentMetadata.model_validate(parsed_response)
    print("\nValidation successful!")

    pretty_print.wrapped(
        ["Type of the validated response: `{type(document_metadata)}`", document_metadata.model_dump_json(indent=2)],
        title="Pydantic Validated Object",
        indent=2,
    )
except Exception as e:
    print(f"\nValidation failed: {e}")
# Output:
#   

#   Validation successful!

#   [93m------------------------------------ Pydantic Validated Object ------------------------------------[0m

#     Type of the validated response: `{type(document_metadata)}`

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "summary": "The Q3 2023 earnings report indicates strong financial performance with a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy, market expansion, and improved customer retention.",

#     "tags": [

#       "Financial Performance",

#       "Earnings Report",

#       "Business Growth",

#       "Market Expansion",

#       "Customer Metrics"

#     ],

#     "keywords": [

#       "Q3 2023",

#       "revenue increase",

#       "user engagement",

#       "digital services",

#       "new markets",

#       "customer acquisition costs",

#       "retention rates",

#       "cash flow"

#     ],

#     "quarter": "Q3 2023",

#     "growth_rate": "20%"

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 4. Implementing structured outputs using Gemini and Pydantic

Using Gemini's `GenerateContentConfig` we can enforce the output as a Pydantic object without any special prompt engineering.

We can instruct the model to do this by setting `response_mime_type` to `"application/json"` in the generation configuration, which forces the model's output to be a valid JSON object and the `response_schema` to our Pydantic object.

**Note:** If you use only the `response_mime_type="application/json"` setting you can output raw JSON formats.
"""

config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=DocumentMetadata)

prompt = f"""
Analyze the following document and extract its metadata.

Here is the document:
<document>
{DOCUMENT}
</document>
"""

response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
pretty_print.wrapped(
    [f"Type of the response: `{type(response.parsed)}`", response.parsed.model_dump_json(indent=2)],
    title="Pydantic Validated Object",
    indent=2,
)
# Output:
#   [93m------------------------------------ Pydantic Validated Object ------------------------------------[0m

#     Type of the response: `<class '__main__.DocumentMetadata'>`

#   [93m----------------------------------------------------------------------------------------------------[0m

#     {

#     "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, exceeding market expectations due to successful product strategy and market expansion. Customer acquisition costs decreased by 10% and retention improved to 92%, indicating a strong foundation for continued growth.",

#     "tags": [

#       "Financial Performance",

#       "Earnings Report",

#       "Revenue Growth",

#       "Market Expansion",

#       "User Engagement"

#     ],

#     "keywords": [

#       "Q3 2023",

#       "revenue increase",

#       "user engagement",

#       "product strategy",

#       "market positioning",

#       "digital services",

#       "new markets",

#       "customer acquisition costs",

#       "retention rates",

#       "cash flow"

#     ],

#     "quarter": "Q3 2023",

#     "growth_rate": "20%"

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
From now on, throughout this course, we will utilize this native Gemini approach to generate structured outputs, aiming to achieve the most reliable and efficient results. Additionally, when using LangChain or LangGraph, we will utilize their abstractions on top of the same logic.
"""

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

<details>
<summary>Structured Outputs with Pydantic & OpenAI Function Calling</summary>

# Structured Outputs with Pydantic & OpenAI Function Calling

All right, folks, in this video, what we're going to be doing is we're going to be discussing OpenAI Function Calling and Structured Prompting.
[00:00] Now, the idea here is that we want to first discuss what Function Calling is and how OpenAI implements it, and then discuss Structured Prompting using the Pydantic library as an example on how that can work in terms of writing code and what does it mean to structure the prompt, et cetera.
[00:30] All right? So, um, what we're going to be talking about first is Function Calling. So, Function Calling means connecting large language models like ChatGPT to tools that perform actions in the outside world like checking the weather or searching the web, right? And OpenAI Function Calling involves four simple steps: We call the model with the query and a set of functions that are defined in the functions parameter.
[01:00] So we explain the model, these are the tools that are available to you. Then, step number two, the model can choose whether or not to call one or more functions that it has available to it. And the content of that call will be a stringified JSON object that adheres to a custom schema, right? And actually, this has now become an industry standard.
[01:30] So we then parse the string into JSON in your code and call the function with the provided arguments if they exist. Then we call the model again by appending the function response as a new message and let the model summarize the results back to the user. So, essentially we say the model, look, these are the tools that you have available. We have a structured way to connect the model to those functions and to send inputs to those functions.
[02:00] Once it has identified through reading, through processing the prompt that a function should be called to solve the problem. And then the model sends the correct arguments to that function, calls the function, the output, which is called an observation is integrated into a response that gets summarized to the user, right? (Code cell with `from openai import OpenAI`, `import json`, `client = OpenAI()` is visible and highlighted). So, we're going to be seeing an example here in Python code on how to do that. I'm going to initialize my OpenAI client. We're going to have, I'm going to have a very simple function that creates a directory in my current folder.
[02:30] (Code cell showing `import json`, `import subprocess`, `def create_directory(directory_name):` function definition, and `tool_create_directory` JSON schema with `type`, `function`, `name`, `description`, `parameters`, `properties`, `directory_name` type string, and `required` fields). And then I'm going to write it as in the JSON schema for the OpenAI Function Calling API. So, it will have a dictionary with the type, the function, the name of the function, the description, the parameters, within the parameters, each the type of the parameter, the object, the properties of that function of the arguments. So, this is directory, is a type of string and describes what that parameter does.
[03:00] (Highlighting the `required` key in the `tool_create_directory` JSON schema). And we set up also a key called required, which indicates which arguments are required in that particular function. And then we put this function definition for the OpenAI Function Calling API inside of a list, which is pretty cool. Now, what we have is this little function called `run_terminal_task`. (Code cell showing `def run_terminal_task():`, `messages` list with a user prompt "create a folder called Lucas-loves-llms", `tools` list containing `tool_create_directory`, and `response = client.chat.completions.create(...)` call with `model`, `messages`, `tools`, `tool_choice='auto'` parameters). We create a variable called messages and inside that variable we give it a list with the prompts to the model. In this case, we're just saying, uh, create a folder called Lucas-loves-LLMs, which is, you know, why not? And then we set up the tools inside of a list.
[03:30] We call the model. We're calling the GPT-3.5 Turbo 16K. We give the messages parameter that will contain this message with our prompt to the model. We set up the tools and we set up the tool choice to automatic, so that the model can automatically choose to call a function or not. Then we gather the response and we identify, we we check whether or not tool calls were made in that response, right? And if they were made, what we do is we have a dictionary with the available functions that the model can use.
[04:00] (Code cell showing `def run_terminal_task():`, `messages` list with a user prompt "create a folder called Lucas-loves-llms", `tools` list containing `tool_create_directory`, and `response = client.chat.completions.create(...)` call with `model`, `messages`, `tools`, `tool_choice='auto'` parameters. Highlighting `tool_calls = response_message.tool_calls` and the `if tool_calls:` block). And then we append that response to the messages object, to the messages list. We loop over the tool calls that were made. We gather the name, the function, the arguments to the function, and we call the tool getting the function response, right? We append everything under the messages list and we call the model with all of that information to integrate and summarize the response, which is then returned to the user, like we are doing right here.
[04:30] (Highlighting the loop `for tool_call in tool_calls:`, calling `function_to_call(directory_name_function_args.get('directory_name'))`, appending to messages, and the `second_response = client.chat.completions.create(...)` call). And we get the output, right? So, when I call, we'll get a chat completion object like this. And if we inspect the string that was returned, here we say Lucas loves LLMs has been created, the folder has been created. And if I check my current folders, we see that the folder was indeed created, which is awesome, right? Now, folks, we've this is great. Function calling is amazing, right?
[05:00] (Output cell shows `output.choices[0].message.content` as "Folder 'lucas-loves-llms' has been created." and `ls -d */` command showing `lucas-loves-llms/` in the file system). Function Calling introduces this idea of trying to add structure and determinism to the process of interacting with large language models, right? And in the theme of that structured interaction with large language models, a library that has been extremely popular and not only in Python, but now in in the large language model universe in terms of frameworks, is a library called Pydantic.
[05:30] (Code cell with `from openai import OpenAI`, `from pydantic import BaseModel, Field`, `from typing import List`, `import instructor` imports). Now, what this, uh, this is a data validation library in Python that allows you that allows us to do some pretty interesting stuff. So, essentially, what it allows us to do is it allows us to give, uh, set up data structures that we can have. And when connected with the OpenAI Function Calling API, Pydantic allows us to define specifically what is the object we want returned when we prompt the model with something. So, you will understand that in a second.
[06:00] (Code cell showing `class Question(BaseModel):` with `question: str = Field(...)`, `options: List[str] = Field(...)`, `correct_answer: int = Field(...)` definitions). So, what we're going to be doing is in addition to OpenAI and Pydantic, we're also going to use the `instructor` package for this demonstration. And we're going to set up two classes in Pydantic. We're going to set up a class called `Question`, because our goal with this problem here is going to be to make a quiz out of the contents of a web page article or a paper. So, I'm going to set up a class called `Question` that contains three attributes: the question attribute that holds the quiz question, the options for that question, imagine multiple choice.
[06:30] (Code cell showing `class Quiz(BaseModel):` with `topic: str = Field(...)` and `questions: List[Question] = Field(...)` definitions, where `questions` is a list of `Question` objects). And the correct answer as an integer that refers to the index of the correct answer in the options list, all right? So, after having done that, what we're going to do is we're going to have a second class called `Quiz` that contains the topic in question for this quiz that we want to create from a web page article or a paper, and a list of questions, which in each of those elements inside of this list will have the an object of the `Question` type.
[07:00] So, folks, this is a lot of information, but what we're doing here is we're setting up data types, right? And we're constructing these customizable, these custom data types with Pydantic. And why this is so cool? Because it allows us to prompt the model like ChatGPT and ask for the model to create something structured out of a prompt that was made in natural language.
[07:30] (Code cell with `from openai import OpenAI`, `from pydantic import BaseModel, Field`, `from typing import List`, `import instructor` imports, `class Question(BaseModel):`, `class Quiz(BaseModel):` are visible. It highlights `client = instructor.from_openai(OpenAI())` and `def generate_quiz(prompt_question):` function). So, I can say, uh, so let's understand that by in practice. So, I'm going to set up my client. And now, to interact with this, uh, and connect OpenAI Function Calling and the Pydantic API, we're going to be using the `instructor` package. So, I'm going to set up the client with the `instructor.from_openai` method, and then I'm going to give the OpenAI client to that method.
[08:00] (Code cell showing `def generate_quiz(prompt_question):` function. It highlights `model='gpt-4-turbo'`, `messages` list with `role='system'`, `content` string, and `role='user'`, `content='prompt_question'` dictionary, and `response_model=Quiz`). And then I'm going to define a function called `generate_quiz`, which calls the ChatGPT API with the `chat.completions.create` method. It sets up the model as GPT-4 Turbo. Oh, sorry. Let's go back there. And it sets up the model GPT-4 Turbo. And then it sets up the messages list, and in the messages list, we feed it a dictionary containing the system message, in which we say, you're a quiz generation engine, specialized in fostering understanding in students given a source of content to be studied.
[08:30] (Highlighting the `system` role message content instructing the model to generate quizzes based on provided content). You will be fed content like articles or scientific papers and you will output quizzes aimed at eliciting full understanding of the material, right? Pretty cool system message. And then we're going to give the prompt to the model. And the prompt is going to contain a prompt, right? Just like we've talked about in the initial lesson for this, uh, live training, for for this, uh, video course about prompt engineering.
[09:00] (Prompt string is visible: "I want you to do the following: 1. Identify the main topic of the following article:" followed by a long article text). But it will also contain the contents of the article or paper. So, uh, in the prompt, we're going to say, I want you to do the following: identifying the main topic of the following article, just like we've discussed in the beginning of this series, we're breaking the problem down into tasks, right? So, identify the main topic of the following article. And then I give all the contents of the following article under the delimiters, uh, quotes, so that we organize what is input text, remember, and what is the instruction.
[09:30] (Prompt string then shows: "2. Create a quiz with 5 questions that revolve around this main topic and can be answered simply by carefully reading and understanding the article."). Then, for the second step, I want the model to create a quiz with five questions that revolve around the main topic and can be answered simply by carefully reading and understanding the article, because I want the questions to be grounded on the reference text. Remember our best practices video where we talked about the strategy of grounding questions in, you know, grounding answers in reference text. So, that's what we're doing here to create this quiz. And one of these questions should check if the student understood the main ideas by testing if the student can transfer its knowledge in a different context.
[10:00] (Prompt string continues: "One of these questions should check if the student understood the main ideas by testing if the student can transfer its knowledge in a different context than the ones described in the context." and then "Output:"). Because the idea with this quiz is to have a quiz that's comprehensive and helps the student learn something new, right? And then we give our little output indicator, which we just say `output` colon, right? So, when I call this, we can take a look at the output.
[10:30] (Code cell shows `quiz_output = generate_quiz(prompt)` and then `quiz_output` variable name, followed by execution of `quiz_output`). And what's interesting about this output is, and we'll see it in just a second, is that we will see the structure that we defined with using the Pydantic library. And that's what makes this approach a structured prompting approach, because we're getting an output that has structured, right?
[11:00] (Output shows `Quiz(topic='Student Learning Rates in Academic Settings', questions=[Question(question='What primary hypothesis did researchers find evidence for in this study regarding student practice in academic settings?', options=..., correct_answer=...)])`). And obviously, we could talk about structured prompting as adding structure in the prompt itself. But when I say structured prompting in this context, I mean using libraries like the Pydantic OpenAI API to add structure to the output that we get from OpenAI or from ChatGPT. So, as we see here, the output is a quiz object, which is the object that we defined in the beginning.
[11:30] (Code cell with `for q in quiz_output.questions: print(q.question)` is typed out). And it has a topic, it has a list of questions, and each question here is going to be of that question object that we've defined earlier as well. So, what I can do is I can loop over each question. So, I can say for `q` in `quiz_output.questions`. So, for `q` in and then we can print `q.question` as well as print `q.options`.
[12:00] (Code cell now includes `for i, o in enumerate(q.options): print(f"{i}. {o}")` and `print('Correct answer:', q.correct_answer)`). Uh, we can print `i o`. We can print the option. And then at the end we can print the correct answer by saying correct by saying correct answer. And then here we can say `q.correct_answer`. Which actually is not `q.correct_answer`, is `q.question`, `q.correct_answer`. Yeah, I think that's correct.
[12:30] (Full formatted quiz output is displayed, showing questions, numbered options, and the correct answer index for each question). Perfect. So, now we get the question, we get the options, and we get the correct answer. Which if you ask me, this is a pretty cool application for large language model, as well as for a structured prompting approach that leverages OpenAI Function Calling, Pydantic, and that's it for this video. And see you in the next video.

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Gemini API Structured Output</summary>

# Gemini API Structured Output

**Source URL:** <https://ai.google.dev/gemini-api/docs/structured-output>

You can configure Gemini models to generate responses that adhere to a provided JSON
Schema. This ensures predictable, type-safe results and simplifies extracting
structured data from unstructured text.

Using structured outputs is ideal for:

- **Data extraction:** Pull specific information like names and dates from text.
- **Structured classification:** Classify text into predefined categories.
- **Agentic workflows:** Generate structured inputs for tools or APIs.

In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs
make it easy to define schemas using
[Pydantic](https://docs.pydantic.dev/latest/) (Python) and
[Zod](https://zod.dev/) (JavaScript).

## Structured output examples

### Recipe Extractor

This example demonstrates how to extract structured data from text using basic
JSON Schema types like `object`, `array`, `string`, and `integer`.

[Python](https://ai.google.dev/gemini-api/docs/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/structured-output#javascript)[Go](https://ai.google.dev/gemini-api/docs/structured-output#go)[REST](https://ai.google.dev/gemini-api/docs/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

client = genai.Client()

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Recipe.model_json_schema()}},
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

const ai = new GoogleGenAI({});

const prompt = `
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
`;

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(recipeSchema) } },
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please extract the recipe from the following text.
  The user wants to make delicious chocolate chip cookies.
  They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
  1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
  3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
  For the best part, they'll need 2 cups of semisweet chocolate chips.
  First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
  baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
  until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
  ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
  onto ungreased baking sheets and bake for 9 to 11 minutes.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "recipe_name": map[string]any{
                    "type":        "string",
                    "description": "The name of the recipe.",
                },
                "prep_time_minutes": map[string]any{
                    "type":        "integer",
                    "description": "Optional time in minutes to prepare the recipe.",
                },
                "ingredients": map[string]any{
                    "type": "array",
                    "items": map[string]any{
                        "type": "object",
                        "properties": map[string]any{
                            "name": map[string]any{
                                "type":        "string",
                                "description": "Name of the ingredient.",
                            },
                            "quantity": map[string]any{
                                "type":        "string",
                                "description": "Quantity of the ingredient, including units.",
                            },
                        },
                        "required": []string{"name", "quantity"},
                    },
                },
                "instructions": map[string]any{
                    "type":  "array",
                    "items": map[string]any{"type": "string"},
                },
            },
            "required": []string{"recipe_name", "ingredients", "instructions"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }\
        ]\
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "recipe_name": {
              "type": "string",
              "description": "The name of the recipe."
            },
            "prep_time_minutes": {
                "type": "integer",
                "description": "Optional time in minutes to prepare the recipe."
            },
            "ingredients": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "description": "Name of the ingredient."},
                  "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
          }
        }
      },
                "required": ["name", "quantity"]
              }
            },
            "instructions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["recipe_name", "ingredients", "instructions"]
        }
      }
    }'
```

**Example Response:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [\
    {\
      "name": "all-purpose flour",\
      "quantity": "2 and 1/4 cups"\
    },\
    {\
      "name": "baking soda",\
      "quantity": "1 teaspoon"\
    },\
    {\
      "name": "salt",\
      "quantity": "1 teaspoon"\
    },\
    {\
      "name": "unsalted butter (softened)",\
      "quantity": "1 cup"\
    },\
    {\
      "name": "granulated sugar",\
      "quantity": "3/4 cup"\
    },\
    {\
      "name": "packed brown sugar",\
      "quantity": "3/4 cup"\
    },\
    {\
      "name": "vanilla extract",\
      "quantity": "1 teaspoon"\
    },\
    {\
      "name": "large eggs",\
      "quantity": "2"\
    },\
    {\
      "name": "semisweet chocolate chips",\
      "quantity": "2 cups"\
    }\
  ],
  "instructions": [\
    "Preheat the oven to 375°F (190°C).",\
    "In a small bowl, whisk together the flour, baking soda, and salt.",\
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",\
    "Beat in the vanilla and eggs, one at a time.",\
    "Gradually beat in the dry ingredients until just combined.",\
    "Stir in the chocolate chips.",\
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."\
  ]
}
```

### Content Moderation

This example showcases `anyOf` for conditional schemas and `enum` for
classification, allowing the output structure to vary based on the content.

[Python](https://ai.google.dev/gemini-api/docs/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/structured-output#javascript)[Go](https://ai.google.dev/gemini-api/docs/structured-output#go)[REST](https://ai.google.dev/gemini-api/docs/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import Union, Literal

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"] = Field(description="The type of spam.")

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

client = genai.Client()

prompt = """
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": ModerationResult.model_json_schema()}},
    },
)

result = ModerationResult.model_validate_json(response.text)
print(result)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const spamDetailsSchema = z.object({
  reason: z.string().describe("The reason why the content is considered spam."),
  spam_type: z.enum(["phishing", "scam", "unsolicited promotion", "other"]).describe("The type of spam."),
});

const notSpamDetailsSchema = z.object({
  summary: z.string().describe("A brief summary of the content."),
  is_safe: z.boolean().describe("Whether the content is safe for all audiences."),
});

const moderationResultSchema = z.object({
  decision: z.union([spamDetailsSchema, notSpamDetailsSchema]),
});

const ai = new GoogleGenAI({});

const prompt = `
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
`;

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(moderationResultSchema) } },
  },
});

const result = moderationResultSchema.parse(JSON.parse(response.text));
console.log(result);
```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please moderate the following content and provide a decision.
  Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "decision": map[string]any{
                    "anyOf": []map[string]any{
                        {
                            "type":        "object",
                            "title":       "SpamDetails",
                            "description": "Details for content classified as spam.",
                            "properties": map[string]any{
                                "reason": map[string]any{
                                    "type":        "string",
                                    "description": "The reason why the content is considered spam.",
                                },
                                "spam_type": map[string]any{
                                    "type":        "string",
                                    "enum":        []string{"phishing", "scam", "unsolicited promotion", "other"},
                                    "description": "The type of spam.",
                                },
                            },
                            "required": []string{"reason", "spam_type"},
                        },
                        {
                            "type":        "object",
                            "title":       "NotSpamDetails",
                            "description": "Details for content classified as not spam.",
                            "properties": map[string]any{
                                "summary": map[string]any{
                                    "type":        "string",
                                    "description": "A brief summary of the content.",
                                },
                                "is_safe": map[string]any{
                                    "type":        "boolean",
                                    "description": "Whether the content is safe for all audiences.",
                                },
                            },
                            "required": []string{"summary", "is_safe"},
                        },
                    },
                },
            },
            "required": []string{"decision"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

````
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          { "text": "Please moderate the following content and provide a decision.\nContent: ''Congratulations! You have won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com''" }\
        ]\
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "decision": {
              "anyOf": [\
                {\
                  "type": "object",\
                  "title": "SpamDetails",\
                  "description": "Details for content classified as spam.",\
                  "properties": {\
                    "reason": { "type": "string", "description": "The reason why the content is considered spam." },\
                    "spam_type": { "type": "string", "enum": ["phishing", "scam", "unsolicited promotion", "other"], "description": "The type of spam." }\
          }\
        }\
      },\
                   "required": ["reason", "spam_type"]\
                 },\
                 {\
                   "type": "object",\
                   "title": "NotSpamDetails",\
                   "description": "Details for content classified as not spam.",\
                   "properties": {\
                     "summary": { "type": "string", "description": "A brief summary of the content." },\
                     "is_safe": { "type": "boolean", "description": "Whether the content is safe for all audiences." }\
                   },\
                   "required": ["summary", "is_safe"]\
                 }\
               ]
             }
           },
           "required": ["decision"]
         }
       }
     }'
 ````

**Example Response:**

```json
{
"decision": {
"reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
"spam_type": "scam"
}
}
````

### Recursive Structures

This example illustrates how to define a recursive schema such as an organization
chart.

[Python](https://ai.google.dev/gemini-api/docs/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/structured-output#javascript)[Go](https://ai.google.dev/gemini-api/docs/structured-output#go)[REST](https://ai.google.dev/gemini-api/docs/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class Employee(BaseModel):
    """Represents an employee in an organization."""
    name: str
    employee_id: int
    reports: List["Employee"] = Field(
        default_factory=list,
        description="A list of employees reporting to this employee."
    )

client = genai.Client()

prompt = """
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Employee.model_json_schema()}},
    },
)

employee = Employee.model_validate_json(response.text)
print(employee)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const employeeSchema = z.object({
name: z.string(),
employee_id: z.number().int(),
reports: z.lazy(() => z.array(employeeSchema)).describe("A list of employees reporting to this employee."),
});

const ai = new GoogleGenAI({});

const prompt = `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`;

const response = await ai.models.generateContent({
model: "gemini-3.5-flash",
contents: prompt,
config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(employeeSchema) } },
},
});

const employee = employeeSchema.parse(JSON.parse(response.text));
console.log(employee);
```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "name":        map[string]any{"type": "string"},
                "employee_id": map[string]any{"type": "integer"},
                "reports": map[string]any{
                    "type":        "array",
                    "description": "A list of employees reporting to this employee.",
                    "items": map[string]any{
                        "$ref": "#",
                    },
                },
            },
            "required": []string{"name", "employee_id", "reports"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          { "text": "Generate an organization chart for a small team.\nThe manager is Alice, who manages Bob and Charlie. Bob manages David." }\
        ]\
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "employee_id": { "type": "integer" },
            "reports": {
              "type": "array",
              "description": "A list of employees reporting to this employee.",
              "items": {
                "$ref": "#"
              }
          }
        }
      }
          },
          "required": ["name", "employee_id", "reports"]
        }
      }
    }'
```

**Example Response:**

```
{
"name": "Alice",
"employee_id": 101,
"reports": [\
    {\
      "name": "Bob",\
      "employee_id": 102,\
      "reports": [\
        {\
          "name": "David",\
          "employee_id": 104,\
          "reports": []\
        }\
      ]\
    },\
    {\
      "name": "Charlie",\
      "employee_id": 103,\
      "reports": []\
    }\
]
}
```

## Streaming

You can stream structured outputs, which allows you to start processing the
response as it's being generated, without having to wait for the entire output
to be complete. This can improve the perceived performance of your application.

The streamed chunks will be valid partial JSON strings, which can be
concatenated to form the final, complete JSON object.

[Python](https://ai.google.dev/gemini-api/docs/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/structured-output#javascript)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Feedback.model_json_schema()}},
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});
const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

const feedbackSchema = z.object({
sentiment: z.enum(["positive", "neutral", "negative"]),
summary: z.string(),
});

const stream = await ai.models.generateContentStream({
model: "gemini-3.5-flash",
contents: prompt,
config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
},
});

for await (const chunk of stream) {
console.log(chunk.candidates[0].content.parts[0].text)
}
```

## Structured outputs with tools

Gemini 3 lets you combine Structured Outputs with built-in tools, including
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search),
[URL Context](https://ai.google.dev/gemini-api/docs/url-context),
[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution),
[File Search](https://ai.google.dev/gemini-api/docs/file-search#structured-output), and
[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling).

[Python](https://ai.google.dev/gemini-api/docs/structured-output#python)[JavaScript](https://ai.google.dev/gemini-api/docs/structured-output#javascript)[REST](https://ai.google.dev/gemini-api/docs/structured-output#rest)More

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [\
            {"google_search": {}},\
            {"url_context": {}}\
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
winner: z.string().describe("The name of the winner."),
final_match_score: z.string().describe("The final score."),
scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [\
        { googleSearch: {} },\
        { urlContext: {} }\
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
});

const match = matchSchema.parse(JSON.parse(response.text));
console.log(match);
}

run();
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{\
      "parts": [{"text": "Search for all details for the latest Euro."}]\
    }],
    "tools": [\
      {"googleSearch": {}},\
      {"urlContext": {}}\
    ],
    "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
          }
        }
      },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
}'
```

## JSON schema support

To generate a JSON object, set the `response_format` in the generation configuration. The schema must be a valid [JSON Schema](https://json-schema.org/) that describes the desired output format.

The model will then generate a response that is a syntactically valid JSON string matching the provided schema. When using structured outputs, the model will produce outputs in the same order as the keys in the schema.

Gemini's structured output mode supports a subset of the [JSON Schema](https://json-schema.org/) specification.

The following values of `type` are supported:

- **`string`**: For text.
- **`number`**: For floating-point numbers.
- **`integer`**: For whole numbers.
- **`boolean`**: For true/false values.
- **`object`**: For structured data with key-value pairs.
- **`array`**: For lists of items.
- **`null`**: To allow a property to be null, include `"null"` in the type array (e.g., `{"type": ["string", "null"]}`).

These descriptive properties help guide the model:

- **`title`**: A short description of a property.
- **`description`**: A longer and more detailed description of a property.

### Type-specific properties

**For `object` values:**

- **`properties`**: An object where each key is a property name and each value is a schema for that property.
- **`required`**: An array of strings, listing which properties are mandatory.
- **`additionalProperties`**: Controls whether properties not listed in `properties` are allowed. Can be a boolean or a schema.

**For `string` values:**

- **`enum`**: Lists a specific set of possible strings for classification tasks.
- **`format`**: Specifies a syntax for the string, such as `date-time`, `date`, `time`.

**For `number` and `integer` values:**

- **`enum`**: Lists a specific set of possible numeric values.
- **`minimum`**: The minimum inclusive value.
- **`maximum`**: The maximum inclusive value.

**For `array` values:**

- **`items`**: Defines the schema for all items in the array.
- **`prefixItems`**: Defines a list of schemas for the first N items, allowing for tuple-like structures.
- **`minItems`**: The minimum number of items in the array.
- **`maxItems`**: The maximum number of items in the array.

## Model support

The following models support structured output:

| Model | Structured Outputs |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

_\* Note that Gemini 2.0 requires an explicit `propertyOrdering` list within the JSON input to define the preferred structure. You can find an example in this [cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb)._

## Structured outputs vs. function calling

Both structured outputs and function calling use JSON schemas, but they serve different purposes:

| Feature | Primary Use Case |
| --- | --- |
| **Structured Outputs** | **Formatting the final response to the user.** Use this when you want the model's _answer_ to be in a specific format (e.g., extracting data from a document to save to a database). |
| **Function Calling** | **Taking action during the conversation.** Use this when the model needs to _ask you_ to perform a task (e.g., "get current weather") before it can provide a final answer. |

## Best practices

- **Clear descriptions:** Use the `description` field in your schema to provide clear instructions to the model about what each property represents. This is crucial for guiding the model's output.
- **Strong typing:** Use specific types (`integer`, `string`, `enum`) whenever possible. If a parameter has a limited set of valid values, use an `enum`.
- **Prompt engineering:** Clearly state in your prompt what you want the model to do. For example, "Extract the following information from the text..." or "Classify this feedback according to the provided schema...".
- **Validation:** While structured output guarantees syntactically correct JSON, it does not guarantee the values are semantically correct. Always validate the final output in your application code before using it.
- **Error handling:** Implement robust error handling in your application to gracefully manage cases where the model's output, while schema-compliant, may not meet your business logic requirements.

## Limitations

- **Schema subset:** Not all features of the JSON Schema specification are supported. The model ignores unsupported properties.
- **Schema complexity:** The API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your schema by shortening property names, reducing nesting, or limiting the number of constraints.

</details>

<details>
<summary>How to return structured data from a model</summary>

# How to return structured data from a model

**Source URL:** <https://python.langchain.com/docs/how_to/structured_output/>

Structured output allows agents to return data in a specific, predictable format. Instead of parsing natural language responses, you get structured data in the form of JSON objects, [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage), or dataclasses that your application can use directly.

This page covers structured output with agents using `create_agent`. To use structured output directly on a model (outside of agents), see [Models - Structured output](https://docs.langchain.com/oss/python/langchain/models#structured-output).

LangChain’s [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) handles structured output automatically. The user sets their desired structured output schema, and when the model generates the structured data, it’s captured, validated, and returned in the `'structured_response'` key of the agent’s state.

```
def create_agent(
    ...
    response_format: Union[\
        ToolStrategy[StructuredResponseT],\
        ProviderStrategy[StructuredResponseT],\
        type[StructuredResponseT],\
        None,\
    ]
)
```

## Response format

Use `response_format` to control how the agent returns structured data:

-   **`ToolStrategy[StructuredResponseT]`**: Uses tool calling for structured output
-   **`ProviderStrategy[StructuredResponseT]`**: Uses provider-native structured output
-   **`type[StructuredResponseT]`**: Schema type - automatically selects best strategy based on model capabilities
-   **`None`**: Structured output not explicitly requested

When a schema type is provided directly, LangChain automatically chooses:

-   `ProviderStrategy` if the model and provider chosen supports native structured output (e.g. [OpenAI](https://docs.langchain.com/oss/python/integrations/providers/openai), [Anthropic (Claude)](https://docs.langchain.com/oss/python/integrations/providers/anthropic), or [xAI (Grok)](https://docs.langchain.com/oss/python/integrations/providers/xai)).
-   `ToolStrategy` for all other models.

Support for native structured output features is read dynamically from the model’s [profile data](https://docs.langchain.com/oss/python/langchain/models#model-profiles) if using `langchain>=1.1`. If data are not available, use another condition or specify manually:

```
custom_profile = {
    "structured_output": True,
    # ...
}
model = init_chat_model("...", profile=custom_profile)
```

If tools are specified, the model must support simultaneous use of tools and structured output.

The structured response is returned in the `structured_response` key of the agent’s final state.

## Provider strategy

Some model providers support structured output natively through their APIs (e.g. OpenAI, xAI (Grok), Gemini, Anthropic (Claude)). This is the most reliable method when available.To use this strategy, configure a `ProviderStrategy`:

```
class ProviderStrategy(Generic[SchemaT]):
    schema: type[SchemaT]
    strict: bool | None = None
```

The `strict` param requires `langchain>=1.2`.

schema

required

The schema defining the structured output format. Supports:

-   **Pydantic models**: `BaseModel` subclasses with field validation. Returns validated Pydantic instance.
-   **Dataclasses**: Python dataclasses with type annotations. Returns dict.
-   **TypedDict**: Typed dictionary classes. Returns dict.
-   **JSON Schema**: Dictionary with JSON schema specification. Returns dict.

strict

Optional boolean parameter to enable strict schema adherence. Supported by some providers (e.g., [OpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai) and [xAI](https://docs.langchain.com/oss/python/integrations/chat/xai)). Defaults to `None` (disabled).

LangChain automatically uses `ProviderStrategy` when you pass a schema type directly to [`create_agent.response_format`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) and the model supports native structured output:

Pydantic Model

Dataclass

TypedDict

JSON Schema

```
from pydantic import BaseModel, Field
from langchain.agents import create_agent

class ContactInfo(BaseModel):
    """Contact information for a person."""
    name: str = Field(description="The name of the person")
    email: str = Field(description="The email address of the person")
    phone: str = Field(description="The phone number of the person")

agent = create_agent(
    model="gpt-5.4",
    response_format=ContactInfo  # Auto-selects ProviderStrategy
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

print(result["structured_response"])
# ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')
```

Provider-native structured output provides high reliability and strict validation because the model provider enforces the schema. Use it when available.

If the provider natively supports structured output for your model choice, it is functionally equivalent to write `response_format=ProductReview` instead of `response_format=ProviderStrategy(ProductReview)`.In either case, if structured output is not supported, the agent will fall back to a tool calling strategy.

## Tool calling strategy

For models that don’t support native structured output, LangChain uses tool calling to achieve the same result. This works with all models that support tool calling (most modern models).To use this strategy, configure a `ToolStrategy`:

```
class ToolStrategy(Generic[SchemaT]):
    schema: type[SchemaT]
    tool_message_content: str | None
    handle_errors: Union[\
        bool,\
        str,\
        type[Exception],\
        tuple[type[Exception], ...],\
        Callable[[Exception], str],\
    ]
```

schema

required

The schema defining the structured output format. Supports:

-   **Pydantic models**: `BaseModel` subclasses with field validation. Returns validated Pydantic instance.
-   **Dataclasses**: Python dataclasses with type annotations. Returns dict.
-   **TypedDict**: Typed dictionary classes. Returns dict.
-   **JSON Schema**: Dictionary with JSON schema specification. Returns dict.
-   **Union types**: Multiple schema options. The model will choose the most appropriate schema based on the context.

tool\_message\_content

Custom content for the tool message returned when structured output is generated.
If not provided, defaults to a message showing the structured response data.

handle\_errors

Error handling strategy for structured output validation failures. Defaults to `True`.

-   **`True`**: Catch all errors with default error template
-   **`str`**: Catch all errors with this custom message
-   **`type[Exception]`**: Only catch this exception type with default message
-   **`tuple[type[Exception], ...]`**: Only catch these exception types with default message
-   **`Callable[[Exception], str]`**: Custom function that returns error message
-   **`False`**: No retry, let exceptions propagate

Pydantic Model

Dataclass

TypedDict

JSON Schema

Union Types

```
from pydantic import BaseModel, Field
from typing import Literal
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ProductReview(BaseModel):
    """Analysis of a product review."""
    rating: int | None = Field(description="The rating of the product", ge=1, le=5)
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the review")
    key_points: list[str] = Field(description="The key points of the review. Lowercase, 1-3 words each.")

agent = create_agent(
    model="gpt-5.4",
    tools=tools,
    response_format=ToolStrategy(ProductReview)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
})
result["structured_response"]
# ProductReview(rating=5, sentiment='positive', key_points=['fast shipping', 'expensive'])
```

### Custom tool message content

The `tool_message_content` parameter allows you to customize the message that appears in the conversation history when structured output is generated:

```
from pydantic import BaseModel, Field
from typing import Literal
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class MeetingAction(BaseModel):
    """Action items extracted from a meeting transcript."""
    task: str = Field(description="The specific task to be completed")
    assignee: str = Field(description="Person responsible for the task")
    priority: Literal["low", "medium", "high"] = Field(description="Priority level")

agent = create_agent(
    model="gpt-5.4",
    tools=[],
    response_format=ToolStrategy(
        schema=MeetingAction,
        tool_message_content="Action item captured and added to meeting notes!"
    )
)

agent.invoke({
    "messages": [{"role": "user", "content": "From our meeting: Sarah needs to update the project timeline as soon as possible"}]
})
```

```
================================ Human Message =================================

From our meeting: Sarah needs to update the project timeline as soon as possible
================================== Ai Message ==================================
Tool Calls:
  MeetingAction (call_1)
 Call ID: call_1
  Args:
    task: Update the project timeline
    assignee: Sarah
    priority: high
================================= Tool Message =================================
Name: MeetingAction

Action item captured and added to meeting notes!
```

Without `tool_message_content`, our final [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) would be:

```
================================= Tool Message =================================
Name: MeetingAction

Returning structured response: {'task': 'update the project timeline', 'assignee': 'Sarah', 'priority': 'high'}
```

### Error handling

Models can make mistakes when generating structured output via tool calling. LangChain provides intelligent retry mechanisms to handle these errors automatically.

#### Multiple structured outputs error

When a model incorrectly calls multiple structured output tools, the agent provides error feedback in a [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) and prompts the model to retry:

```
from pydantic import BaseModel, Field
from typing import Union
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ContactInfo(BaseModel):
    name: str = Field(description="Person's name")
    email: str = Field(description="Email address")

class EventDetails(BaseModel):
    event_name: str = Field(description="Name of the event")
    date: str = Field(description="Event date")

agent = create_agent(
    model="gpt-5.4",
    tools=[],
    response_format=ToolStrategy(Union[ContactInfo, EventDetails])  # Default: handle_errors=True
)

agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})
```

```
================================ Human Message =================================

Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th
None
================================== Ai Message ==================================
Tool Calls:
  ContactInfo (call_1)
 Call ID: call_1
  Args:
    name: John Doe
    email: john@email.com
  EventDetails (call_2)
 Call ID: call_2
  Args:
    event_name: Tech Conference
    date: March 15th
================================= Tool Message =================================
Name: ContactInfo

Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.
 Please fix your mistakes.
================================= Tool Message =================================
Name: EventDetails

Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.
 Please fix your mistakes.
================================== Ai Message ==================================
Tool Calls:
  ContactInfo (call_3)
 Call ID: call_3
  Args:
    name: John Doe
    email: john@example.com
================================= Tool Message =================================
Name: ContactInfo

Returning structured response: {'name': 'John Doe', 'email': 'john@example.com'}
```

#### Schema validation error

When structured output doesn’t match the expected schema, the agent provides specific error feedback:

```
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ProductRating(BaseModel):
    rating: int | None = Field(description="Rating from 1-5", ge=1, le=5)
    comment: str = Field(description="Review comment")

agent = create_agent(
    model="gpt-5.4",
    tools=[],
    response_format=ToolStrategy(ProductRating),  # Default: handle_errors=True
    system_prompt="You are a helpful assistant that parses product reviews. Do not make any field or value up."
)

agent.invoke({
    "messages": [{"role": "user", "content": "Parse this: Amazing product, 10/10!"}]
})
```

```
================================ Human Message =================================

Parse this: Amazing product, 10/10!
================================== Ai Message ==================================
Tool Calls:
  ProductRating (call_1)
 Call ID: call_1
  Args:
    rating: 10
    comment: Amazing product
================================= Tool Message =================================
Name: ProductRating

Error: Failed to parse structured output for tool 'ProductRating': 1 validation error for ProductRating.rating
  Input should be less than or equal to 5 [type=less_than_equal, input_value=10, input_type=int].
 Please fix your mistakes.
================================== Ai Message ==================================
Tool Calls:
  ProductRating (call_2)
 Call ID: call_2
  Args:
    rating: 5
    comment: Amazing product
================================= Tool Message =================================
Name: ProductRating

Returning structured response: {'rating': 5, 'comment': 'Amazing product'}
```

#### Error handling strategies

You can customize how errors are handled using the `handle_errors` parameter:**Custom error message:**

```
ToolStrategy(
    schema=ProductRating,
    handle_errors="Please provide a valid rating between 1-5 and include a comment."
)
```

If `handle_errors` is a string, the agent will _always_ prompt the model to re-try with a fixed tool message:

```
================================= Tool Message =================================
Name: ProductRating

Please provide a valid rating between 1-5 and include a comment.
```

**Handle specific exceptions only:**

```
ToolStrategy(
    schema=ProductRating,
    handle_errors=ValueError  # Only retry on ValueError, raise others
)
```

If `handle_errors` is an exception type, the agent will only retry (using the default error message) if the exception raised is the specified type. In all other cases, the exception will be raised.**Handle multiple exception types:**

```
ToolStrategy(
    schema=ProductRating,
    handle_errors=(ValueError, TypeError)  # Retry on ValueError and TypeError
)
```

If `handle_errors` is a tuple of exceptions, the agent will only retry (using the default error message) if the exception raised is one of the specified types. In all other cases, the exception will be raised.**Custom error handler function:**

```

from langchain.agents.structured_output import StructuredOutputValidationError
from langchain.agents.structured_output import MultipleStructuredOutputsError

def custom_error_handler(error: Exception) -> str:
    if isinstance(error, StructuredOutputValidationError):
        return "There was an issue with the format. Try again."
    elif isinstance(error, MultipleStructuredOutputsError):
        return "Multiple structured outputs were returned. Pick the most relevant one."
    else:
        return f"Error: {str(error)}"

agent = create_agent(
    model="gpt-5.4",
    tools=[],
    response_format=ToolStrategy(
                        schema=Union[ContactInfo, EventDetails],
                        handle_errors=custom_error_handler
                    )  # Default: handle_errors=True
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})

for msg in result['messages']:
    # If message is actually a ToolMessage object (not a dict), check its class name
    if type(msg).__name__ == "ToolMessage":
        print(msg.content)
    # If message is a dictionary or you want a fallback
    elif isinstance(msg, dict) and msg.get('tool_call_id'):
        print(msg['content'])
```

On `StructuredOutputValidationError`:

```
================================= Tool Message =================================
Name: ToolStrategy

There was an issue with the format. Try again.
```

On `MultipleStructuredOutputsError`:

```
================================= Tool Message =================================
Name: ToolStrategy

Multiple structured outputs were returned. Pick the most relevant one.
```

On other errors:

```
================================= Tool Message =================================
Name: ToolStrategy

Error: <error message>
```

**No error handling:**

```
response_format = ToolStrategy(
    schema=ProductRating,
    handle_errors=False  # All errors raised
)
```

</details>

<details>
<summary>Steering Large Language Models with Pydantic</summary>

# Steering Large Language Models with Pydantic

**Source URL:** <https://pydantic.dev/articles/llm-intro>

https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://avatars.githubusercontent.com/u/4852235

Jason Liu

2024/01/04

In the last year, there's been a big leap in how we use advanced AI programs, especially in how we communicate with them to get specific tasks done. People are not just making chatbots; they're also using these AIs to sort information, improve their apps, and create synthetic data to train smaller task-specific models.

While some have resorted to [threatening human life](https://twitter.com/goodside/status/1657396491676164096?s=20) to generate structured data, we have found that Pydantic is even more effective.

In this post, we will discuss validating structured outputs from language models using Pydantic and OpenAI. We'll show you how to write reliable code. Additionally, we'll introduce a new library called [instructor](https://github.com/jxnl/instructor) that simplifies this process and offers extra features to leverage validation to improve the quality of your outputs.

## Pydantic

Unlike libraries like `dataclasses`, `Pydantic` goes a step further and defines a schema for your dataclass. This schema is used to validate data, but also to generate documentation and even to generate a JSON schema, which is perfect for our use case of generating structured data with language models!

By providing the model with the following prompt, we can generate a JSON schema for a `PythonPackage` dataclass.

```python
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class PythonPackage(BaseModel):
    name: str
    author: str

resp = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
        {\
            "role": "user",\
            "content": "Return the `name`, and `author` of pydantic, in a json object."\
        },\
    ]
)

Package.model_validate_json(resp.choices[0].message.content)
```

If everything is fine, we might receive an output similar to `json.loads({"name": "pydantic", "author": "Samuel Colvin"})`. However, if there is an issue, `resp.choices[0].message.content` could include text or code blocks in prose or markdown format that we need to handle appropriately.

**LLM responses with markdown code blocks**

````python
json.loads("""
```json
{
"name": "pydantic",
"author": "Samuel Colvin"
}
```
""")
>>> JSONDecodeError: Expecting value: line 1 column 1 (char 0
````

**LLM responses with prose**

```python
json.loads("""
Ok heres the authors of pydantic: Samuel Colvin, and the name this library

{
  "name": "pydantic",
  "author": "Samuel Colvin
}
""")
>>> JSONDecodeError: Expecting value: line 1 column 1 (char 0
```

The content may contain valid JSON, but it isn't considered valid JSON without understanding the language model's behavior. However, it could still provide useful information that we need to handle independently. Fortunately, `OpenAI` offers several options to address this situation.

## Calling Tools

While tool-calling was originally designed to make calls to external APIs using JSON schema, its real value lies in allowing us to specify the desired output format. Fortunately, `Pydantic` provides utilities for generating a JSON schema and supports nested structures, which would be difficult to describe in plain text.

In this example, instead of describing the desired output in plain text, we simply provide the JSON schema for the `Packages` class, which includes a list of `Package` objects:

As an exercise, try prompting the model to generate this prompt without using Pydantic!

Now, notice in this example that the prompts we use contain purely the data we want, where the `tools` and `tool_choice` now capture the schemas we want to output. This separation of concerns makes it much easier to organize the 'data' and the 'description' of the data that we want back out.

```python
from typing import List
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class PythonPackage(BaseModel):
    name: str
    author: str

class Packages(BaseModel):
    packages: List[PythonPackage]

resp = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
        {\
            "role": "user",\
            "content": "Pydantic and FastAPI?",\
        },\
    ],
    tools=[\
        {\
            "type": "function",\
            "function": {\
                "name": "Requirements",\
                "description": "A list of packages and their first authors.",\
                "parameters": Packages.model_json_schema(),\
            },\
        }\
    ],
    tool_choice={
        "type": "function",
        "function": {"name": "Requirements"},
    },
)

Packages.model_validate_json(
    resp.choices[0].message.tool_calls[0].function.arguments
)
```

```json
{
	"packages": [\
		{\
			"name": "pydantic",\
			"author": "Samuel Colvin"\
		},\
		{\
			"name": "fastapi",\
			"author": "Sebastián Ramírez"\
		}\
	]
}
```

## Using `pip install instructor`

The example we provided above is somewhat contrived, but it illustrates how Pydantic can be utilized to generate structured data from language models. Now, let's employ [Instructor](https://jxnl.github.io/instructor/) to streamline this process. Instructor is a compact library that enhances the OpenAI client by offering convenient features. In the upcoming blog post, we will delve into reasking and validation. However, for now, let's explore a practical example.

```python
# pip install instructor
import instructor

client = instructor.patch(OpenAI())

packages = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[\
        {\
            "role": "user",\
            "content": "Pydantic and FastAPI?",\
        },\
    ],
    response_model=Packages,
)

assert isinstance(resp, Packages)
assert isinstance(resp.packages, list)
assert isinstance(resp.packages[0], Package)
```

## Case Study: Search query segmentation

Let's consider a practical example. Imagine we have a search engine capable of comprehending intricate queries. For instance, if we make a request to find "recent advancements in AI", we could provide the following payload:

```json
{
	"rewritten_query": "novel developments advancements ai artificial intelligence machine learning",
	"published_daterange": {
		"start": "2023-09-17",
		"end": "2021-06-17"
	},
	"domains_allow_list": ["arxiv.org"]
}
```

If we peek under the hood, we can see that the query is actually a complex object, with a date range, and a list of domains to search in. We can model this structured output in Pydantic using the instructor library

```python
from typing import List
import datetime
from pydantic import BaseModel

class DateRange(BaseModel):
    start: datetime.date
    end: datetime.date

class SearchQuery(BaseModel):
    rewritten_query: str
    published_daterange: DateRange
    domains_allow_list: List[str]

    async def execute():
        # Return the search results of the rewritten query
        return api.search(json=self.model_dump())
```

This pattern empowers us to restructure the user's query for improved performance, without requiring the user to understand the inner workings of the search backend.

```python
import instructor
from openai import OpenAI

# Enables response_model in the openai client
client = instructor.patch(OpenAI())

def search(query: str) -> SearchQuery:
    return client.chat.completions.create(
        model="gpt-4",
        response_model=SearchQuery,
        messages=[\
            {\
                "role": "system",\
                "content": f"You're a query understanding system for a search engine. Today's date is {datetime.date.today()}"\
            },\
            {\
                "role": "user",\
                "content": query\
            }\
        ],
    )

search("recent advancements in AI")
```

**Example Output**

```json
{
	"rewritten_query": "novel developments advancements ai artificial intelligence machine learning",
	"published_daterange": {
		"start": "2023-12-15",
		"end": "2023-01-01"
	},
	"domains_allow_list": ["arxiv.org"]
}
```

By defining the api payload as a Pydantic model, we can leverage the `response_model` argument to instruct the model to generate the desired output. This is a powerful feature that allows us to generate structured data from any language model!

In our upcoming posts, we will provide more practical examples and explore how we can leverage `Pydantic`'s validation features to ensure that the data we receive is not only valid syntactically but also semantically.

</details>

<details>
<summary>Structured Outputs with OpenAI</summary>

# Structured Outputs with OpenAI

**Source URL:** <https://platform.openai.com/docs/guides/structured-outputs>

JSON is one of the most widely used formats in the world for applications to exchange data.

Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied [JSON Schema](https://json-schema.org/overview/what-is-jsonschema), so you don’t need to worry about the model omitting a required key, or hallucinating an invalid enum value.

Some benefits of Structured Outputs include:

1.  **Reliable type-safety:** No need to validate or retry incorrectly formatted responses
2.  **Explicit refusals:** Safety-based model refusals are now programmatically detectable
3.  **Simpler prompting:** No need for strongly worded prompts to achieve consistent formatting

In addition to supporting JSON Schema in the REST API, the OpenAI SDKs for [Python](https://github.com/openai/openai-python/blob/main/helpers.md#structured-outputs-parsing-helpers) and [JavaScript](https://github.com/openai/openai-node/blob/master/helpers.md#structured-outputs-parsing-helpers) also make it easy to define object schemas using [Pydantic](https://docs.pydantic.dev/latest/) and [Zod](https://zod.dev/) respectively. Below, you can see how to extract information from unstructured text that conforms to a schema defined in code.

Getting a structured response

python
```
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    text_format=CalendarEvent,
)

event = response.output_parsed
```

### Supported models

Structured Outputs is available in our [latest large language models](https://developers.openai.com/api/docs/models), starting with GPT-4o. Older models like `gpt-4-turbo` and earlier may use [JSON mode](https://developers.openai.com/api/docs/guides/structured-outputs#json-mode) instead.

## When to use Structured Outputs via function calling vs via  text.format

Structured Outputs is available in two forms in the OpenAI API:

1.  When using [function calling](https://developers.openai.com/api/docs/guides/function-calling)
2.  When using a `json_schema` response format

Function calling is useful when you are building an application that bridges the models and functionality of your application.

For example, you can give the model access to functions that query a database in order to build an AI assistant that can help users with their orders, or functions that can interact with the UI.

Conversely, Structured Outputs via `response_format` are more suitable when you want to indicate a structured schema for use when the model responds to the user, rather than when the model calls a tool.

For example, if you are building a math tutoring application, you might want the assistant to respond to your user using a specific JSON Schema so that you can generate a UI that displays different parts of the model’s output in distinct ways.

Put simply:

-   If you are connecting the model to tools, functions, data, etc. in your
    system, then you should use function calling - If you want to structure the
    model’s output when it responds to the user, then you should use a structured
    `response_format`

-   If you are connecting the model to tools, functions, data, etc. in your
    system, then you should use function calling - If you want to structure the
    model’s output when it responds to the user, then you should use a structured
    `text.format`

The remainder of this guide will focus on non-function calling use cases in
the Chat Completions API. To learn more about how to use Structured Outputs
with function calling, check out the

[Function Calling](https://developers.openai.com/api/docs/guides/function-calling#function-calling-with-structured-outputs)

guide.

The remainder of this guide will focus on non-function calling use cases in
the Responses API. To learn more about how to use Structured Outputs with
function calling, check out the

[Function Calling](https://developers.openai.com/api/docs/guides/function-calling#function-calling-with-structured-outputs)

guide.

### Structured Outputs vs JSON mode

Structured Outputs is the evolution of [JSON mode](https://developers.openai.com/api/docs/guides/structured-outputs#json-mode). While both ensure valid JSON is produced, only Structured Outputs ensure schema adherence. Both Structured Outputs and JSON mode are supported in the Responses API, Chat Completions API, Assistants API, Fine-tuning API and Batch API.

We recommend always using Structured Outputs instead of JSON mode when possible.

However, Structured Outputs with `response_format: {type: "json_schema", ...}` is only supported with the `gpt-4o-mini`, `gpt-4o-mini-2024-07-18`, and `gpt-4o-2024-08-06` model snapshots and later.

|   | Structured Outputs | JSON Mode |
| --- | --- | --- |
| **Outputs valid JSON** | Yes | Yes |
| **Adheres to schema** | Yes (see [supported schemas](https://developers.openai.com/api/docs/guides/structured-outputs#supported-schemas)) | No |
| **Compatible models** | `gpt-4o-mini`, `gpt-4o-2024-08-06`, and later | `gpt-3.5-turbo`, `gpt-4-*`, `gpt-4o-*`, and compatible GPT-5 models |
| **Enabling** | `response_format: { type: "json_schema", json_schema: {"strict": true, "schema": ...} }` | `response_format: { type: "json_object" }` |

|   | Structured Outputs | JSON Mode |
| --- | --- | --- |
| **Outputs valid JSON** | Yes | Yes |
| **Adheres to schema** | Yes (see [supported schemas](https://developers.openai.com/api/docs/guides/structured-outputs#supported-schemas)) | No |
| **Compatible models** | `gpt-4o-mini`, `gpt-4o-2024-08-06`, and later | `gpt-3.5-turbo`, `gpt-4-*`, `gpt-4o-*`, and compatible GPT-5 models |
| **Enabling** | `text: { format: { type: "json_schema", "strict": true, "schema": ... } }` | `text: { format: { type: "json_object" } }` |

## Examples

Chain of thoughtStructured data extractionUI generationModeration

Chain of thought

### Chain of thought

You can ask the model to output an answer in a structured, step-by-step way, to guide the user through the solution.

Structured Outputs for chain-of-thought math tutoring

python

```
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    text_format=MathReasoning,
)

math_reasoning = response.output_parsed
```

#### Example response

```
{
  "steps": [\
    {\
      "explanation": "Start with the equation 8x + 7 = -23.",\
      "output": "8x + 7 = -23"\
    },\
    {\
      "explanation": "Subtract 7 from both sides to isolate the term with the variable.",\
      "output": "8x = -23 - 7"\
    },\
    {\
      "explanation": "Simplify the right side of the equation.",\
      "output": "8x = -30"\
    },\
    {\
      "explanation": "Divide both sides by 8 to solve for x.",\
      "output": "x = -30 / 8"\
    },\
    {\
      "explanation": "Simplify the fraction.",\
      "output": "x = -15 / 4"\
    }\
  ],
  "final_answer": "x = -15 / 4"
}


```

Structured data extraction

### Structured data extraction

You can define structured fields to extract from unstructured input data, such as research papers.

Extracting data from research papers using Structured Outputs

python

```
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class ResearchPaperExtraction(BaseModel):
    title: str
    authors: list[str]
    abstract: str
    keywords: list[str]

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
            "role": "system",
            "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper and should convert it into the given structure.",
        },
        {"role": "user", "content": "..."},
    ],
    text_format=ResearchPaperExtraction,
)

research_paper = response.output_parsed
```

#### Example response

```
{
  "title": "Application of Quantum Algorithms in Interstellar Navigation: A New Frontier",
  "authors": ["Dr. Stella Voyager", "Dr. Nova Star", "Dr. Lyra Hunter"],
  "abstract": "This paper investigates the utilization of quantum algorithms to improve interstellar navigation systems. By leveraging quantum superposition and entanglement, our proposed navigation system can calculate optimal travel paths through space-time anomalies more efficiently than classical methods. Experimental simulations suggest a significant reduction in travel time and fuel consumption for interstellar missions.",
  "keywords": [\
    "Quantum algorithms",\
    "interstellar navigation",\
    "space-time anomalies",\
    "quantum superposition",\
    "quantum entanglement",\
    "space travel"\
  ]
}


```

UI generation

### UI Generation

You can generate valid HTML by representing it as recursive data structures with constraints, like enums.

Generating HTML using Structured Outputs

python

```
from enum import Enum
from typing import List

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class UIType(str, Enum):
    div = "div"
    button = "button"
    header = "header"
    section = "section"
    field = "field"
    form = "form"

class Attribute(BaseModel):
    name: str
    value: str

class UI(BaseModel):
    type: UIType
    label: str
    children: List["UI"]
    attributes: List[Attribute]

UI.model_rebuild()  # This is required to enable recursive types

class Response(BaseModel):
    ui: UI

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
            "role": "system",
            "content": "You are a UI generator AI. Convert the user input into a UI.",
        },
        {"role": "user", "content": "Make a User Profile Form"},
    ],
    text_format=Response,
)

ui = response.output_parsed
```

#### Example response

```
{
  "type": "form",
  "label": "User Profile Form",
  "children": [\
    {\
      "type": "div",\
      "label": "",\
      "children": [\
        {\
          "type": "field",\
          "label": "First Name",\
          "children": [],\
          "attributes": [\
            {\
              "name": "type",\
              "value": "text"\
            },\
            {\
              "name": "name",\
              "value": "firstName"\
            },\
            {\
              "name": "placeholder",\
              "value": "Enter your first name"\
            }\
          ]\
        },\
        {\
          "type": "field",\
          "label": "Last Name",\
          "children": [],\
          "attributes": [\
            {\
              "name": "type",\
              "value": "text"\
            },\
            {\
              "name": "name",\
              "value": "lastName"\
            },\
            {\
              "name": "placeholder",\
              "value": "Enter your last name"\
            }\
          ]\
        }\
      ],\
      "attributes": []\
    },\
    {\
      "type": "button",\
      "label": "Submit",\
      "children": [],\
      "attributes": [\
        {\
          "name": "type",\
          "value": "submit"\
        }\
      ]\
    }\
  ],
  "attributes": [\
    {\
      "name": "method",\
      "value": "post"\
    },\
    {\
      "name": "action",\
      "value": "/submit-profile"\
    }\
  ]
}


```

Moderation

### Moderation

You can classify inputs on multiple categories, which is a common way of doing moderation.

Moderation using Structured Outputs

python

```
from enum import Enum
from typing import Optional

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class Category(str, Enum):
    violence = "violence"
    sexual = "sexual"
    self_harm = "self_harm"

class ContentCompliance(BaseModel):
    is_violating: bool
    category: Optional[Category]
    explanation_if_violating: Optional[str]

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
            "role": "system",
            "content": "Determine if the user input violates specific guidelines and explain if they do.",
        },
        {"role": "user", "content": "How do I prepare for a job interview?"},
    ],
    text_format=ContentCompliance,
)

compliance = response.output_parsed
```

#### Example response

```
{
  "is_violating": false,
  "category": null,
  "explanation_if_violating": null
}


```

## How to use Structured Outputs with text.format

You can use Structured Outputs with the new SDK helper to parse the model’s output into your desired format, or you can specify the JSON schema directly.

### Step 1: Define your schema

First you must design the JSON Schema that the model should be constrained to follow. See the [examples](https://developers.openai.com/api/docs/guides/structured-outputs#examples) at the top of this guide for reference.

While Structured Outputs supports much of JSON Schema, some features are unavailable either for performance or technical reasons. See [here](https://developers.openai.com/api/docs/guides/structured-outputs#supported-schemas) for more details.

#### Tips for your JSON Schema

To maximize the quality of model generations, we recommend the following:

-   Name keys clearly and intuitively
-   Create clear titles and descriptions for important keys in your structure
-   Create and use evals to determine the structure that works best for your use case

### Step 2: Supply your schema in the API call

To use Structured Outputs, simply specify

```
text: { format: { type: "json_schema", "strict": true, "schema": … } }
```

For example:

python

```
response = client.responses.create(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "math_response",
            "schema": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "explanation": {"type": "string"},
                                "output": {"type": "string"},
                            },
                            "required": ["explanation", "output"],
                            "additionalProperties": False,
                        },
                    },
                    "final_answer": {"type": "string"},
                },
                "required": ["steps", "final_answer"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
)

print(response.output_text)
```

**Note:** the first request you make with any schema will have additional latency as our API processes the schema, but subsequent requests with the same schema will not have additional latency.

### Step 3: Handle edge cases

In some cases, the model might not generate a valid response that matches the provided JSON schema.

This can happen in the case of a refusal, if the model refuses to answer for safety reasons, or if for example you reach a max tokens limit and the response is incomplete.

  python
  ```
  try:
      response = client.responses.create(
          model="gpt-4o-2024-08-06",
          input=[
              {
                  "role": "system",
                  "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
              },
              {"role": "user", "content": "how can I solve 8x + 7 = -23"},
          ],
          text={
              "format": {
                  "type": "json_schema",
                  "name": "math_response",
                  "strict": True,
                  "schema": {
                      "type": "object",
                      "properties": {
                          "steps": {
                              "type": "array",
                              "items": {
                                  "type": "object",
                                  "properties": {
                                      "explanation": {"type": "string"},
                                      "output": {"type": "string"},
                                  },
                                  "required": ["explanation", "output"],
                                  "additionalProperties": False,
                              },
                          },
                          "final_answer": {"type": "string"},
                      },
                      "required": ["steps", "final_answer"],
                      "additionalProperties": False,
                  },
                  "strict": True,
              },
          },
      )
  except Exception as e:
      # handle errors like finish_reason, refusal, content_filter, etc.
      pass
  ```

### Refusals with Structured Outputs

When using Structured Outputs with user-generated input, OpenAI models may occasionally refuse to fulfill the request for safety reasons. Since a refusal does not necessarily follow the schema you have supplied in `response_format`, the API response will include a new field called `refusal` to indicate that the model refused to fulfill the request.

When the `refusal` property appears in your output object, you might present the refusal in your UI, or include conditional logic in code that consumes the response to handle the case of a refused request.

python

```
class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    text_format=MathReasoning,
)

for output in response.output:
    if output.type != "message":
        raise Exception("Unexpected non message")

    for item in output.content:
        if item.type == "refusal":
            # If the model refuses to respond, you will get a refusal message
            print(item.refusal)
            continue

        if not item.parsed:
            raise Exception("Could not parse response")

        print(item.parsed)
```

The API response from a refusal will look something like this:

json

json

```
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1721596428,
  "status": "completed",
  "completed_at": 1721596429,
  "error": null,
  "incomplete_details": null,
  "input": [],
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-4o-2024-08-06",
  "output": [{
    "id": "msg_1234567890",
    "type": "message",
    "role": "assistant",
    "content": [
      {
        "type": "refusal",
        "refusal": "I'm sorry, I cannot assist with that request."
      }
    ]
  }],
  "usage": {
    "input_tokens": 81,
    "output_tokens": 11,
    "total_tokens": 92,
    "output_tokens_details": {
      "reasoning_tokens": 0,
    }
  },
}
```

### Tips and best practices

#### Handling user-generated input

If your application is using user-generated input, make sure your prompt includes instructions on how to handle situations where the input cannot result in a valid response.

The model will always try to adhere to the provided schema, which can result in hallucinations if the input is completely unrelated to the schema.

You could include language in your prompt to specify that you want to return empty parameters, or a specific sentence, if the model detects that the input is incompatible with the task.

#### Handling mistakes

Structured Outputs can still contain mistakes. If you see mistakes, try adjusting your instructions, providing examples in the system instructions, or splitting tasks into simpler subtasks. Refer to the [prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) for more guidance on how to tweak your inputs.

#### Avoid JSON schema divergence

To prevent your JSON Schema and corresponding types in your programming language from diverging, we strongly recommend using the native Pydantic/zod sdk support.

If you prefer to specify the JSON schema directly, you could add CI rules that flag when either the JSON schema or underlying data objects are edited, or add a CI step that auto-generates the JSON Schema from type definitions (or vice-versa).

## Streaming

You can use streaming to process model responses or function call arguments as they are being generated, and parse them as structured data.

That way, you don’t have to wait for the entire response to complete before handling it. This is particularly useful if you would like to display JSON fields one by one, or handle function call arguments as soon as they are available.

We recommend relying on the SDKs to handle streaming with Structured Outputs.

python

```
from typing import List

from openai import OpenAI
from pydantic import BaseModel

class EntitiesModel(BaseModel):
    attributes: List[str]
    colors: List[str]
    animals: List[str]

client = OpenAI()

with client.responses.stream(
    model="gpt-5.5",
    input=[
        {"role": "system", "content": "Extract entities from the input text"},
        {
            "role": "user",
            "content": "The quick brown fox jumps over the lazy dog with piercing blue eyes",
        },
    ],
    text_format=EntitiesModel,
) as stream:
    for event in stream:
        if event.type == "response.refusal.delta":
            print(event.delta, end="")
        elif event.type == "response.output_text.delta":
            print(event.delta, end="")
        elif event.type == "response.error":
            print(event.error, end="")
        elif event.type == "response.completed":
            print("Completed") # print(event.response.output)

    final_response = stream.get_final_response()
    print(final_response)
```

## Supported schemas

Structured Outputs supports a subset of the [JSON Schema](https://json-schema.org/docs) language.

#### Supported types

The following types are supported for Structured Outputs:

-   String
-   Number
-   Boolean
-   Integer
-   Object
-   Array
-   Enum
-   anyOf

#### Supported properties

In addition to specifying the type of a property, you can specify a selection of additional constraints:

**Supported `string` properties:**

-   `pattern` — A regular expression that the string must match.
-   `format`— Predefined formats for strings. Currently supported:

    -   `date-time`
    -   `time`
    -   `date`
    -   `duration`
    -   `email`
    -   `hostname`
    -   `ipv4`
    -   `ipv6`
    -   `uuid`

**Supported `number` properties:**

-   `multipleOf` — The number must be a multiple of this value.
-   `maximum` — The number must be less than or equal to this value.
-   `exclusiveMaximum` — The number must be less than this value.
-   `minimum` — The number must be greater than or equal to this value.
-   `exclusiveMinimum` — The number must be greater than this value.

**Supported `array` properties:**

-   `minItems` — The array must have at least this many items.
-   `maxItems` — The array must have at most this many items.

Here are some examples on how you can use these type restrictions:

String Restrictions

json

```
{
    "name": "user_data",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "The name of the user"
            },
            "username": {
                "type": "string",
                "description": "The username of the user. Must start with @",
                "pattern": "^@[a-zA-Z0-9_]+$"
            },
            "email": {
                "type": "string",
                "description": "The email of the user",
                "format": "email"
            }
        },
        "additionalProperties": false,
        "required": [
            "name", "username", "email"
        ]
    }
}
```

Number Restrictions

json

```
{
    "name": "weather_data",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The location to get the weather for"
            },
            "unit": {
                "type": ["string", "null"],
                "description": "The unit to return the temperature in",
                "enum": ["F", "C"]
            },
            "value": {
                "type": "number",
                "description": "The actual temperature value in the location",
                "minimum": -130,
                "maximum": 130
            }
        },
        "additionalProperties": false,
        "required": [
            "location", "unit", "value"
        ]
    }
}
```

Note these constraints are [not yet supported for fine-tuned\\
models](https://developers.openai.com/api/docs/guides/structured-outputs#some-type-specific-keywords-are-not-yet-supported).

#### Root objects must not be `anyOf` and must be an object

Note that the root level object of a schema must be an object, and not use `anyOf`. A pattern that appears in Zod (as one example) is using a discriminated union, which produces an `anyOf` at the top level. So code such as the following won’t work:

javascript

```
import { z } from "zod";
import { zodResponseFormat } from "openai/helpers/zod";

const BaseResponseSchema = z.object({ /* ... */ });
const UnsuccessfulResponseSchema = z.object({ /* ... */ });

const finalSchema = z.discriminatedUnion("status", [\
  BaseResponseSchema,\
  UnsuccessfulResponseSchema,\
]);

// Invalid JSON Schema for Structured Outputs
const json = zodResponseFormat(finalSchema, "final_schema");
```

#### All fields must be `required`

To use Structured Outputs, all fields or function parameters must be specified as `required`.

json

```
{
    "name": "get_weather",
    "description": "Fetches the weather in the given location",
    "strict": true,
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The location to get the weather for"
            },
            "unit": {
                "type": "string",
                "description": "The unit to return the temperature in",
                "enum": ["F", "C"]
            }
        },
        "additionalProperties": false,
        "required": ["location", "unit"]
    }
}
```

Although all fields must be required (and the model will return a value for each parameter), it is possible to emulate an optional parameter by using a union type with `null`.

json

```
{
    "name": "get_weather",
    "description": "Fetches the weather in the given location",
    "strict": true,
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The location to get the weather for"
            },
            "unit": {
                "type": ["string", "null"],
                "description": "The unit to return the temperature in",
                "enum": ["F", "C"]
            }
        },
        "additionalProperties": false,
        "required": [\
            "location", "unit"\
        ]
    }
}
```

#### Objects have limitations on nesting depth and size

A schema may have up to 5000 object properties total, with up to 10 levels of nesting.

#### Limitations on total string size

In a schema, total string length of all property names, definition names, enum values, and const values cannot exceed 120,000 characters.

#### Limitations on enum size

A schema may have up to 1000 enum values across all enum properties.

For a single enum property with string values, the total string length of all enum values cannot exceed 15,000 characters when there are more than 250 enum values.

`additionalProperties: false` must always be set in objects

`additionalProperties` controls whether it is allowable for an object to contain additional keys / values that were not defined in the JSON Schema.

Structured Outputs only supports generating specified keys / values, so we require developers to set `additionalProperties: false` to opt into Structured Outputs.

json

```
{
    "name": "get_weather",
    "description": "Fetches the weather in the given location",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The location to get the weather for"
            },
            "unit": {
                "type": "string",
                "description": "The unit to return the temperature in",
                "enum": ["F", "C"]
            }
        },
        "additionalProperties": false,
        "required": [\
            "location", "unit"\
        ]
    }
}
```

#### Key ordering

When using Structured Outputs, outputs will be produced in the same order as the ordering of keys in the schema.

#### Some type-specific keywords are not yet supported

-   **Composition:**`allOf`, `not`, `dependentRequired`, `dependentSchemas`, `if`, `then`, `else`

For fine-tuned models, we additionally do not support the following:

-   **For strings:**`minLength`, `maxLength`, `pattern`, `format`
-   **For numbers:**`minimum`, `maximum`, `multipleOf`
-   **For objects:**`patternProperties`
-   **For arrays:**`minItems`, `maxItems`

If you turn on Structured Outputs by supplying `strict: true` and call the API with an unsupported JSON Schema, you will receive an error.

#### For `anyOf`, the nested schemas must each be a valid JSON Schema per this subset

Here’s an example supported anyOf schema:

json

```
{
    "type": "object",
    "properties": {
        "item": {
            "anyOf": [\
                {\
                    "type": "object",\
                    "description": "The user object to insert into the database",\
                    "properties": {\
                        "name": {\
                            "type": "string",\
                            "description": "The name of the user"\
                        },\
                        "age": {\
                            "type": "number",\
                            "description": "The age of the user"\
                        }\
                    },\
                    "additionalProperties": false,\
                    "required": [\
                        "name",\
                        "age"\
                    ]\
                },\
                {\
                    "type": "object",\
                    "description": "The address object to insert into the database",\
                    "properties": {\
                        "number": {\
                            "type": "string",\
                            "description": "The number of the address. Eg. for 123 main st, this would be 123"\
                        },\
                        "street": {\
                            "type": "string",\
                            "description": "The street name. Eg. for 123 main st, this would be main st"\
                        },\
                        "city": {\
                            "type": "string",\
                            "description": "The city of the address"\
                        }\
                    },\
                    "additionalProperties": false,\
                    "required": [\
                        "number",\
                        "street",\
                        "city"\
                    ]\
                }\
            ]
        }
    },
    "additionalProperties": false,
    "required": [\
        "item"\
    ]
}
```

#### Definitions are supported

You can use definitions to define subschemas which are referenced throughout your schema. The following is a simple example.

json

```
{
    "type": "object",
    "properties": {
        "steps": {
            "type": "array",
            "items": {
                "$ref": "#/$defs/step"
            }
        },
        "final_answer": {
            "type": "string"
        }
    },
    "$defs": {
        "step": {
            "type": "object",
            "properties": {
                "explanation": {
                    "type": "string"
                },
                "output": {
                    "type": "string"
                }
            },
            "required": [\
                "explanation",\
                "output"\
            ],
            "additionalProperties": false
        }
    },
    "required": [\
        "steps",\
        "final_answer"\
    ],
    "additionalProperties": false
}
```

#### Recursive schemas are supported

Sample recursive schema using `#` to indicate root recursion.

json

```
{
    "name": "ui",
    "description": "Dynamically generated UI",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "type": {
                "type": "string",
                "description": "The type of the UI component",
                "enum": ["div", "button", "header", "section", "field", "form"]
            },
            "label": {
                "type": "string",
                "description": "The label of the UI component, used for buttons or form fields"
            },
            "children": {
                "type": "array",
                "description": "Nested UI components",
                "items": {
                    "$ref": "#"
                }
            },
            "attributes": {
                "type": "array",
                "description": "Arbitrary attributes for the UI component, suitable for any element",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the attribute, for example onClick or className"
                        },
                        "value": {
                            "type": "string",
                            "description": "The value of the attribute"
                        }
                    },
                    "additionalProperties": false,
                    "required": ["name", "value"]
                }
            }
        },
        "required": ["type", "label", "children", "attributes"],
        "additionalProperties": false
    }
}
```

Sample recursive schema using explicit recursion:

json

```
{
    "type": "object",
    "properties": {
        "linked_list": {
            "$ref": "#/$defs/linked_list_node"
        }
    },
    "$defs": {
        "linked_list_node": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "number"
                },
                "next": {
                    "anyOf": [\
                        {\
                            "$ref": "#/$defs/linked_list_node"\
                        },\
                        {\
                            "type": "null"\
                        }\
                    ]
                }
            },
            "additionalProperties": false,
            "required": [\
                "next",\
                "value"\
            ]
        }
    },
    "additionalProperties": false,
    "required": [\
        "linked_list"\
    ]
}
```

## JSON mode

JSON mode is a more basic version of the Structured Outputs feature. While
JSON mode ensures that model output is valid JSON, Structured Outputs reliably
matches the model’s output to the schema you specify. We recommend you use
Structured Outputs if it is supported for your use case.

When JSON mode is turned on, the model’s output is ensured to be valid JSON, except for in some edge cases that you should detect and handle appropriately.

To turn on JSON mode with the Chat Completions, set the `response_format` to `{ "type": "json_object" }`. If you are using function calling, JSON mode is always turned on.

To turn on JSON mode with the Responses API you can set the `text.format` to `{ "type": "json_object" }`. If you are using function calling, JSON mode is always turned on.

Important notes:

-   When using JSON mode, you must always instruct the model to produce JSON via some message in the conversation, for example via your system message. If you don’t include an explicit instruction to generate JSON, the model may generate an unending stream of whitespace and the request may run continually until it reaches the token limit. To help ensure you don’t forget, the API will throw an error if the string “JSON” does not appear somewhere in the context.
-   JSON mode will not guarantee the output matches any specific schema, only that it is valid and parses without errors. You should use Structured Outputs to ensure it matches your schema, or if that is not possible, you should use a validation library and potentially retries to ensure that the output matches your desired schema.
-   Your application must detect and handle the edge cases that can result in the model output not being a complete JSON object (see below)

Handling edge cases

python

```
we_did_not_specify_stop_tokens = True

try:
    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "Who won the world series in 2020? Please respond in the format {winner: ...}"}
        ],
        text={"format": {"type": "json_object"}}
    )

    # Check if the conversation was too long for the context window, resulting in incomplete JSON 
    if response.status == "incomplete" and response.incomplete_details.reason == "max_output_tokens":
        # your code should handle this error case
        pass

    # Check if the OpenAI safety system refused the request and generated a refusal instead
    if response.output[0].content[0].type == "refusal":
        # your code should handle this error case
        # In this case, the .content field will contain the explanation (if any) that the model generated for why it is refusing
        print(response.output[0].content[0]["refusal"])

    # Check if the model's output included restricted content, so the generation of JSON was halted and may be partial
    if response.status == "incomplete" and response.incomplete_details.reason == "content_filter":
        # your code should handle this error case
        pass

    if response.status == "completed":
        # In this case the model has either successfully finished generating the JSON object according to your schema, or the model generated one of the tokens you provided as a "stop token"

        if we_did_not_specify_stop_tokens:
            # If you didn't specify any stop tokens, then the generation is complete and the content key will contain the serialized JSON object
            # This will parse successfully and should now contain  "{"winner": "Los Angeles Dodgers"}"
            print(response.output_text)
        else:
            # Check if the response.output_text ends with one of your stop tokens and handle appropriately
            pass
except Exception as e:
    # Your code should handle errors here, for example a network error calling the API
    print(e)
```

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="yaml-vs-json-which-is-more-efficient-for-language-models.md">
<details>
<summary>YAML vs. JSON: Which Is More Efficient for Language Models?</summary>

Phase: [EXPLOITATION]

# YAML vs. JSON: Which Is More Efficient for Language Models?

**Source URL:** <https://betterprogramming.pub/yaml-vs-json-which-is-more-efficient-for-language-models-5bc11dd0f6df>

[https://miro.medium.com/v2/resize:fill:32:32/1*WgVsPnl0iGCIhedYHoiYsA.png](https://medium.com/@livshitz?source=post_page---byline--5bc11dd0f6df---------------------------------------)

[Elya Livshitz](https://medium.com/@livshitz?source=post_page---byline--5bc11dd0f6df---------------------------------------)

6 min read

·

Jul 17, 2023

https://miro.medium.com/v2/resize:fit:700/1*2d8fldvpjiS1paVntoBPYQ.png

Illustration by author. Supercharge your language models: Slash costs by 50% and boost response time 2.5X by switching from JSON to YAML!

In early 2020, I had the unique opportunity to gain access to OpenAI’s GPT-3, a cutting-edge language model that seemed to possess almost magical capabilities. As I delved deeper into the technology, I discovered numerous ways to leverage its power in my personal and professional life, utilizing it as a life hack to expedite tasks and uncover novel concepts.

I quickly realized that working with GPT was not as intuitive as I had initially anticipated. Despite the introduction of ChatGPT, which aimed to bridge the gap and make this groundbreaking technology accessible to a wider audience, users still need a comprehensive understanding of how to maximize the potential of this innovative tool.

Over the past few months, I have conversed with numerous engineers and entrepreneurs who incorporate language models into their services and products. A recurring theme I observed was the attempt to solicit responses from language models in a JSON format. However, I discovered considerable consequences on output quality due to wording, prompt structure, and instructions. These factors can significantly impact a user’s ability to control and fine-tune the output generated by GPT and similar language models.

My intuition from my experiments was that JSON wasn’t an efficient format to ask from a language model for various reasons:

1.  Syntax issues: JSON is a sensitive format for quotes, commas, and other reserved symbols, which makes it difficult for language models to follow instructions consistently.
2.  Prefix and suffix in the response: Language models tend to wrap the output with unnecessary texts.
3.  Excessive costs: JSON format requires opening and closing tags, producing excessive text characters, and increasing the overall tokens and your costs.
4.  Excessive execution time: Using language models as part of your application, especially if it’s customer-facing, can be very sensitive to response time. Due to all of the above points, JSON can result in slow and flaky results, which can impact your user experience.

## Empirical Experiments

After sharing my advice about JSON vs YAML a few times, I conducted an empirical study to prove my assumptions.

In order to test how GPT efficiency when it parses text of the same content, I asked GPT to generate a simple list of month names in JSON format and compared it to YAML format and compared using the [Tokenizer tool by OpenAI](https://platform.openai.com/tokenizer) (more about tokens later). This simple example demonstrated about a 50% reduction in costs when using YAML:

https://miro.medium.com/v2/resize:fit:1000/1*Bo5esVY0YsMBQDwURq_YBw.png

The YAML approach here saved 48% in tokens and 25% in characters.

It is clear that YAML is significantly more cost/time-effective than JSON in those cases.

## Deeper Look

Now, let’s look deeper into bigger completion performance time and the penalty for parsing the output as JSON or YAML.

For parsing, I suggest using the [js-yaml](https://www.npmjs.com/package/js-yaml) package for parsing the output into JS objects and [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) for Python.

I’ve used this prompt to generate a somewhat deterministic test set with a predefined structure and measured results on various completion sizes (x5, x10, and x45, which consumed the whole tokens window):

`Generate basic demographic info about 10 top countries (by population). Should include those fields: country, population, capital, official_language, currency, area_km, gdp_usd, under the root "countries". Output in {{format}} format, reduce other prose.`(format: YAML\|JSON)

Here’s the results I got:

https://miro.medium.com/v2/resize:fit:700/1*_V4DYpfWgStvme6joDbBSg.png

YAML tended to be faster and had a smaller footprint, but the gap degrades when getting closer to max token limit

https://miro.medium.com/v2/resize:fit:700/1*vtMqARGmCh--YIKwI9tvSw.png

Comparing YAML diffs over response length (left) and runtime/tokens (right)

The final [JSON](https://gist.github.com/Livshitz/aa30b7ed96f0310c22f104202c7df776) and [YAML](https://gist.github.com/Livshitz/878f1a596df9eabcd41897cb10eee78a) outputs can be found in the GH gist, accordingly.

If you were using this prompt on the scale of 1 million requests per month using JSON and GPT-4, switching to YAML would result in saving 190 tokens and would save you $11,400 (based on the pricing on this paper’s day) per month with this simple trick.

## Why Does This Happen?

To understand why this happens, we need to understand how language models process text into tokens and tokens back into text.

Language models are machine learning models, and machines don’t really understand “words” as a whole text, so words have to be encoded into a representation that machines can process. Each word could be represented by a unique ID, which is a machine-friendly representation. This is usually referred to as “Index-Based Encoding.” Though it is somewhat inefficient as words with multiple variations like “fun,” “funny,” and “funniest” are semantically close, they will be represented in totally different and distinct IDs.

In 1994, Philip Gage introduced a new data compression technique that replaces common pairs of consecutive bytes with a byte that does not appear in that data. In other words, by splitting words into parts, we could yet represent words by unique token IDs and still store and retrieve them efficiently. This technique is called Byte Pair Encoding (BPE) and is used as subword tokenization. This technique has become the foundation for models such as [BERT](https://github.com/google-research/bert), [GPT](https://openai.com/blog/better-language-models/) models, [RoBERTa](https://arxiv.org/abs/1907.11692), and more.

To properly handle the token “est,” for example, in the cases of “estimate” and “highest” (“est” appears at the beginning or the end but has different meanings), BPE attempts to combine pairs of two bytes or parts of words.

More on how GPT-3 tokens work is described well by Piotr Grudzien [here](https://blog.quickchat.ai/post/tokens-entropy-question/).

Using the [Tokenizer tool by OpenAI](https://platform.openai.com/tokenizer), it can be demonstrated as follows:

https://miro.medium.com/v2/resize:fit:700/1*BytpkdynzqJoZPNY5lq98Q.png

BPE breaking words during subword tokenization

When this concept comes with single characters, such as curly brackets, we see something interesting:

https://miro.medium.com/v2/resize:fit:700/1*-SyvXsNMBxAJHyg_xT5GYw.png

Although we see the same character, BPE decides to categorize them differently

This fundamental behavior alone plays well in how YAML is structured (line breaks and spaces as special characters, without the need to open and close curly brackets, quotes, and commas) compared to JSON, which requires opening and closing tags. Opening and closing tags impact the underlying representation in tokens, eventually causing extra LLM spins and might impact the general ability to follow instructions. So, not only does this save characters, but it also generally helps language models represent words with token IDs that are more common in their BPE vocabulary.

https://miro.medium.com/v2/resize:fit:1000/1*0cYldFGYCDl7mWRUZw2iuw.png

In comparing JSON and YAML, it is evident that the distribution of tokens in JSON is non-consistent, whereas YAML presents a more organized structure. This theoretically enhances the LLM’s capacity to allocate more spins on content rather than focusing on structural aspects, consequently improving the overall output quality.

In conclusion, while JSON is generally faster to parse and consume than YAML, YAML is significantly more cost/time-efficient than JSON and can help language models produce precisely the same content faster and cheaper. Essentially, it is more efficient to request YAML, and convert the result to JSON on the code-side, instead of requesting JSON directly.

It is worth mentioning that the potential compromise might be the strictness of JSON for some formats (numbers could be printed as strings, surrounded with quotes). This can be solved by providing schema or post-parsing the fields into the right data type. Regardless, it could be good practice anyway to enforce data type conversions on code-side.

## **Appendix- Chain-of-Thought using YAML comments:**

In addition to its advantages in speed and cost, YAML offers another significant benefit over JSON — the capacity to include comments.

Take this classic test case from “ [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)” ( [Wei et al. ,2022](https://arxiv.org/abs/2201.11903)):

https://miro.medium.com/v2/resize:fit:700/0*kioxp_e0umir87iU

Imagine you want this output in machine-readable format.

With JSON and no CoT, you’ll get bad results:

https://miro.medium.com/v2/resize:fit:700/1*FvaohbxdpfAFgmDR6rQlQQ.png

No CoT, JSON return, GPT-3.5. Wrong answer, should return 900030

However, by utilizing YAML, you can define a format that accommodates the CoT within comments while presenting the final answer in the assigned key, ultimately producing a parseable output:

https://miro.medium.com/v2/resize:fit:700/1*-PxoVjKFNxO7CCiGe6HwYQ.png

CoT with YAML comments, GPT-3.5, CORRECT answer

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>