# Lesson 6: Agent Tools & Function Calling

In our previous lessons, we built a foundation in AI Engineering. We explored the agent landscape, distinguished between LLM workflows and agents, managed context, and enforced structured outputs. Now, we will give our agents the ability to act. We will connect them to the external world using tools, transforming them from simple text generators into systems that can perform tasks.

This lesson will open the black box of tool usage. We will implement tool calling from scratch to understand how it works, then leverage the native power of the Gemini API for a production-ready approach.

## Understanding Why Agents Need Tools

LLMs have a fundamental limitation: they are pattern matchers and text generators. By themselves, they cannot interact with the external world. They are confined to the information they were trained on. This is where tools come in. Tools are the bridge between an LLM's internal reasoning and the outside world, enabling it to access real-time data and perform actions.

Think of the LLM as the brain of an agent. Tools are its hands and senses, allowing it to perceive and act in the world beyond its textual interface. With tools, an LLM evolves into an AI agent.

Popular tools that power modern AI agents allow them to:
- Access real-time information through APIs, like checking today's weather.
- Interact with external databases and storage, such as a PostgreSQL database.
- Access long-term memory to recall information beyond the context window.
- Execute code to perform precise calculations or data manipulation.

## Implementing Tool Calls From Scratch

The best way to understand how tools work is to build them from scratch. The process involves providing the LLM with a list of available functions and letting it decide which one to use and with what arguments.

At a high level, the process of calling a tool involves five steps:

1.  **You:** Provide the LLM with a list of available tools via the system prompt.
2.  **LLM:** Responds with a `function_call` request, specifying the tool and arguments.
3.  **You:** Execute the requested function in your application code.
4.  **You:** Send the function's output back to the LLM.
5.  **LLM:** Uses the tool's output to generate a final, user-facing response.

```mermaid
flowchart LR
  %% Actors
  A["App"]
  L["LLM"]
  U["User"]

  %% Process Steps
  A -- "1. Provides available tools<br/>(system prompt)" --> L
  L -- "2. Function_call request<br/>(tool & arguments)" --> A
  A -- "3. Executes requested function<br/>(e.g., search_google_drive)" --> A_exec["Function Execution"]
  A_exec -- "4. Sends function's output" --> L
  L -- "5. Generates user-facing response" --> U

  %% Highlighting the request-execute-respond flow
  %% The core cycle involves LLM making a request, App executing, and App responding to LLM.
  %% Therefore, LLM, App, and the Function Execution within App are highlighted.
  classDef request_execute_respond stroke-width:2px
  class L,A,A_exec request_execute_respond
```
Image 1: A flowchart illustrating the 5 steps of the tool calling process, highlighting the request-execute-respond flow.

Let's implement a simple example where we mock searching for a document on Google Drive and sending a summary to a Discord channel.

<aside>
💡

You can find all the code for this lesson in the accompanying [GitHub repository notebook](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/06_tools/notebook.ipynb).

</aside>

1.  First, we set up our environment by initializing the Gemini client and defining a model ID. We will use `gemini-2.5-flash`, which is fast and cost-effective. We also define a sample `DOCUMENT` to mock the content of a file.
    ```python
    import json
    from typing import Any
    
    from google import genai
    from google.genai import types
    from pydantic import BaseModel, Field
    
    from lessons.utils import pretty_print
    
    client = genai.Client()
    
    MODEL_ID = "gemini-2.5-flash"
    
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

2.  Next, we define three mock functions. The function signature and docstrings are crucial, as the LLM uses them to understand what each tool does.
    ```python
    def search_google_drive(query: str) -> dict:
        """
        Searches for a file on Google Drive and returns its content or a summary.
    
        Args:
            query (str): The search query to find the file, e.g., 'Q3 earnings report'.
    
        Returns:
            dict: A dictionary representing the search results, including file names and summaries.
        """
        return {
            "files": [
                {
                    "name": "Q3_Earnings_Report_2024.pdf",
                    "id": "file12345",
                    "content": DOCUMENT,
                }
            ]
        }
    ```
    ```python
    def send_discord_message(channel_id: str, message: str) -> dict:
        """
        Sends a message to a specific Discord channel.
    
        Args:
            channel_id (str): The ID of the channel to send the message to, e.g., '#finance'.
            message (str): The content of the message to send.
    
        Returns:
            dict: A dictionary confirming the action, e.g., {"status": "success"}.
        """
        return {
            "status": "success",
            "status_code": 200,
            "channel": channel_id,
            "message_preview": f"{message[:50]}...",
        }
    ```
    ```python
    def summarize_financial_report(text: str) -> str:
        """
        Summarizes a financial report.
    
        Args:
            text (str): The text to summarize.
    
        Returns:
            str: The summary of the text.
        """
        return "The Q3 2023 earnings report shows strong performance across all metrics with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and improved retention rates of 92%."
    ```

3.  We then define a JSON schema for each function. This schema tells the LLM what the tool does (via `description`) and how to call it (via `parameters`). This is an industry standard used by APIs from OpenAI, Google, and Anthropic [[3]](https://ai.google.dev/gemini-api/docs/function-calling), [[1]](https://platform.openai.com/docs/guides/function-calling).
    ```python
    search_google_drive_schema = {
        "name": "search_google_drive",
        "description": "Searches for a file on Google Drive and returns its content or a summary.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to find the file, e.g., 'Q3 earnings report'.",
                }
            },
            "required": ["query"],
        },
    }
    ```

4.  We aggregate our tools and their schemas into dictionaries for easy access.
    ```python
    TOOLS = {
        "search_google_drive": {
            "handler": search_google_drive,
            "declaration": search_google_drive_schema,
        },
        "send_discord_message": {
            "handler": send_discord_message,
            "declaration": send_discord_message_schema,
        },
        "summarize_financial_report": {
            "handler": summarize_financial_report,
            "declaration": summarize_financial_report_schema,
        },
    }
    TOOLS_BY_NAME = {tool_name: tool["handler"] for tool_name, tool in TOOLS.items()}
    TOOLS_SCHEMA = [tool["declaration"] for tool in TOOLS.values()]
    ```

5.  Next, we create a system prompt that instructs the LLM on how to use these tools. It includes guidelines, the expected output format, and the tool schemas.
    ```python
    TOOL_CALLING_SYSTEM_PROMPT = """
    You are a helpful AI assistant with access to tools that enable you to take actions and retrieve information to better 
    assist users.
    
    ## Tool Usage Guidelines
    ...
    
    ## Tool Call Format
    When you need to use a tool, output ONLY the tool call in this exact format:
    
    ```tool_call
    {{"name": "tool_name", "args": {{"param1": "value1", "param2": "value2"}}}}
    ```
    ...
    
    ## Available Tools
    <tool_definitions>
    {tools}
    </tool_definitions>
    
    ...
    """
    ```
    Based on the `description` in the schema, the LLM *decides* if a tool is appropriate. This is why clear and distinct descriptions are critical. For example, two tools described as `Tool used to search documents` and `Tool used to search files` would confuse the LLM. Better descriptions would be `Tool used to search documents on Google Drive` and `Tool used to search files on the local disk`. This clarity becomes essential when scaling to dozens of tools.

    Once a tool is selected, the LLM *generates* the function name and arguments as a structured JSON output. Models are specifically instruction-fine-tuned to interpret these schemas and produce the correct tool call format [[2]](https://arxiv.org/pdf/2401.17464v3).

6.  Let's send a prompt to the model.
    ```python
    USER_PROMPT = """
    Please find the Q3 earnings report on Google Drive and send a summary of it to 
    the #finance channel on Discord.
    """
    
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
    )
    ```
    The model correctly identifies the first step and returns a tool call.
    ```text
    ```tool_call
    {"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}
    ```
    ```

7.  We then parse this response, retrieve the corresponding function handler, and execute it with the arguments provided by the LLM.
    ```python
    def call_tool(response_text: str, tools_by_name: dict) -> Any:
        """
        Call a tool based on the response from the LLM.
        """
        tool_call_str = response_text.split("```tool_call")[1].split("```")[0].strip()
        tool_call = json.loads(tool_call_str)
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool = tools_by_name[tool_name]
    
        return tool(**tool_args)
    
    tool_result = call_tool(response.text, tools_by_name=TOOLS_BY_NAME)
    ```
    This returns the content of our mock document. Typically, this result is then sent back to the LLM to inform the next step or generate a final answer for the user.

## Implementing a Tool Calling Framework From Scratch

Manually defining a JSON schema for every function is tedious and violates the Don't Repeat Yourself (DRY) principle. Production frameworks like LangGraph and protocols like MCP (Model-Context-Protocol) solve this with a `@tool` decorator that automatically generates schemas from Python functions.

Let's build a simplified version of this decorator. The goal is to wrap a function and automatically extract its name, docstring, and parameters to build the schema, creating a `ToolFunction` object that holds both the schema and the callable function.

1.  We define a `ToolFunction` class to hold the function and its generated schema.
    ```python
    class ToolFunction:
        def __init__(self, func: Callable, schema: Dict[str, Any]) -> None:
            self.func = func
            self.schema = schema
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__
    
        def __call__(self, *args: Any, **kwargs: Any) -> Any:
            return self.func(*args, **kwargs)
    ```

2.  Next, we create the `@tool` decorator. It inspects the function's signature and docstring to build the JSON schema automatically.
    ```python
    from inspect import Parameter, signature
    from typing import Any, Callable, Dict, Optional
    
    def tool(description: Optional[str] = None) -> Callable[[Callable], ToolFunction]:
        """
        A decorator that creates a tool schema from a function.
        """
        def decorator(func: Callable) -> ToolFunction:
            sig = signature(func)
            properties = {}
            required = []
    
            for param_name, param in sig.parameters.items():
                if param.default == Parameter.empty:
                    required.append(param_name)
                properties[param_name] = {
                    "type": "string",
                    "description": f"The {param_name} parameter",
                }
    
            schema = {
                "name": func.__name__,
                "description": description or func.__doc__ or f"Executes the {func.__name__} function.",
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            }
            return ToolFunction(func, schema)
        return decorator
    ```

3.  Now, we can redefine our tools using the decorator, which is much cleaner.
    ```python
    @tool()
    def search_google_drive_example(query: str) -> dict:
        """Search for files in Google Drive."""
        return {"files": ["Q3 earnings report"]}
    
    @tool()
    def send_discord_message_example(channel_id: str, message: str) -> dict:
        """Send a message to a Discord channel."""
        return {"message": "Message sent successfully"}
    
    
    @tool()
    def summarize_financial_report_example(text: str) -> str:
        """Summarize the contents of a financial report."""
        return "Financial report summarized successfully"
    
    
    tools = [
        search_google_drive_example,
        send_discord_message_example,
        summarize_financial_report_example,
    ]
    tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
    tools_schema = [tool.schema for tool in tools]
    ```
    The decorated function `search_google_drive_example` is now a `ToolFunction` object. It contains the auto-generated schema and the original function handler, `search_google_drive_example.func`.

4.  When we call the LLM with the new `tools_schema`, it works just as before, but our code is now more maintainable and scalable.
    ```python
    USER_PROMPT = """
    Please find the Q3 earnings report on Google Drive and send a summary of it to 
    the #finance channel on Discord.
    """
    
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(tools_schema)), USER_PROMPT]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
    )
    ```
    It outputs:
    ```text
    ```tool_call
    {"name": "search_google_drive_example", "args": {"query": "Q3 earnings report"}}
    ```
    ```
    This small framework demonstrates the core mechanism behind modern agentic libraries.

## Implementing Production-Level Tool Calls with Gemini

While building from scratch provides great insight, production applications should leverage the native tool-calling features of APIs like Gemini. This approach is more robust, efficient, and requires less code because the provider optimizes the underlying prompts for their specific models [[3]](https://ai.google.dev/gemini-api/docs/function-calling).

Instead of crafting a complex system prompt, we can pass our tool schemas directly to Gemini's `GenerateContentConfig`.

1.  We define the configuration, passing our list of tool schemas.
    ```python
    tools = [
        types.Tool(
            function_declarations=[
                types.FunctionDeclaration(**search_google_drive_schema),
                types.FunctionDeclaration(**send_discord_message_schema),
            ]
        )
    ]
    config = types.GenerateContentConfig(
        tools=tools,
        tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
    )
    ```

2.  The `google-genai` Python SDK simplifies this even further by allowing us to pass the Python functions directly. It automatically generates the schema from the function's signature, type hints, and docstring, just like our custom decorator.
    ```python
    from google.genai import types 
    config = types.GenerateContentConfig(
        tools=[search_google_drive, send_discord_message]
    )
    ```

3.  Now, the call to the model is much cleaner. We no longer need the long system prompt.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=USER_PROMPT,
        config=config,
    )
    function_call = response.candidates[0].content.parts[0].function_call
    ```

4.  We can then create a simplified `call_tool` function to execute the call.
    ```python
    def call_tool(function_call) -> any:
        tool_name = function_call.name
        tool_args = {key: value for key, value in function_call.args.items()}
        tool_handler = TOOLS_BY_NAME[tool_name]
        return tool_handler(**tool_args)
    
    tool_result = call_tool(function_call)
    ```
    The output is the same as our manual implementation. By leveraging the native SDK, we reduced dozens of lines of code to just a few, creating a more robust and maintainable system. Other popular APIs from OpenAI and Anthropic follow a similar logic, making these concepts easily transferable [[1]](https://platform.openai.com/docs/guides/function-calling), [[4]](https://www.anthropic.com/research/building-effective-agents).

## Using Pydantic Models as Tools for On-Demand Structured Outputs

In Lesson 4, we learned how to generate structured outputs. A powerful pattern in agentic systems is to treat a Pydantic model as a tool. This allows an agent to perform several intermediate steps that may produce unstructured text, and then, when it has gathered all necessary information, call a final "tool" to format the output into a reliable, structured Pydantic object.

This combines the flexibility of multi-step reasoning with the reliability of structured data extraction.

```mermaid
flowchart LR
  %% Start of the process
  User["User Prompt"] --> "sends" Agent["AI Agent"]

  subgraph "Tool Orchestration Loop"
    Agent -- "calls" --> Tool1["Tool 1<br/>(e.g., Search Google Drive)"]
    Tool1 -- "returns" --> Result1["Tool 1 Result<br/>(unstructured)"]
    Result1 -- "feedback" --> Agent

    Agent -- "calls" --> Tool2["Tool 2<br/>(e.g., Summarize Report)"]
    Tool2 -- "returns" --> Result2["Tool 2 Result<br/>(unstructured)"]
    Result2 -- "feedback" --> Agent

    Result2 -. "intermediate tool calls" .-> Agent

    Agent -- "calls final tool" --> ToolN["Tool N<br/>(Pydantic Model for Structured Output, e.g., DocumentMetadata)"]
  end

  %% Final output generation
  ToolN -- "produces" --> Output["Structured Output<br/>(e.g., DocumentMetadata object)"]
```
Image 2: A diagram illustrating an AI agent that calls multiple tools in a loop, leading to a structured output.

Let's see how this works in code.

1.  First, we define our `DocumentMetadata` Pydantic model, just as we did in Lesson 4.
    ```python
    class DocumentMetadata(BaseModel):
        """A class to hold structured metadata for a document."""
    
        summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
        tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
        keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
        quarter: str = Field(description="The quarter of the financial year described in the document (e.g., Q3 2023).")
        growth_rate: str = Field(description="The growth rate of the company described in the document (e.g., 10%).")
    ```

2.  We then create a tool declaration where the `parameters` are derived from the Pydantic model's JSON schema.
    ```python
    extraction_tool = types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="extract_metadata",
                description="Extracts structured metadata from a financial document.",
                parameters=DocumentMetadata.model_json_schema(),
            )
        ]
    )
    config = types.GenerateContentConfig(
        tools=[extraction_tool],
        tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
    )
    ```

3.  When we prompt the model to analyze the document, it calls our `extract_metadata` tool with arguments that match the Pydantic schema.
    ```python
    prompt = f"""
    Please analyze the following document and extract its metadata.
    
    Document:
    --- 
    {DOCUMENT}
    --- 
    """
    
    response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
    function_call = response.candidates[0].content.parts[0].function_call
    ```

4.  We can then validate and instantiate the Pydantic object directly from the tool call's arguments.
    ```python
    document_metadata = DocumentMetadata(**function_call.args)
    ```
    This gives us a type-safe, validated Python object, bridging the gap between the agent's reasoning and our application's data model.

## The Downsides of Running Tools in a Loop

So far, we have focused on single-turn interactions. For an agent to handle complex tasks, it needs to chain multiple tools together, using the output of one tool to inform the input of the next. This is achieved by running tools in a loop.

```mermaid
flowchart LR
    A["User Prompt"] --> B["LLM Tool Call"]
    B --> C["App Executes Tool"]
    C --> D["Tool Result"]
    D -- "Iterate" --> B
    D -- "Loop ends" --> E["Final Response"]
```
Image 3: A flowchart illustrating a sequential tool calling loop.

Let's implement a loop where the agent first searches for the report, then summarizes it, and finally sends the summary to Discord.

1.  We set up the configuration with all three tools.
    ```python
    tools = [
        types.Tool(
            function_declarations=[
                types.FunctionDeclaration(**search_google_drive_schema),
                types.FunctionDeclaration(**send_discord_message_schema),
                types.FunctionDeclaration(**summarize_financial_report_schema),
            ]
        )
    ]
    config = types.GenerateContentConfig(
        tools=tools,
        tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
    )
    ```

2.  We initialize the conversation history and make the first call.
    ```python
    USER_PROMPT = """
    Please find the Q3 earnings report on Google Drive and send a summary of it to 
    the #finance channel on Discord.
    """
    messages = [USER_PROMPT]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
        config=config,
    )
    response_message_part = response.candidates[0].content.parts[0]
    messages.append(response.candidates[0].content)
    ```

3.  We then loop, executing tool calls and feeding the results back to the model until it stops requesting actions.
    ```python
    max_iterations = 3
    while hasattr(response_message_part, "function_call") and max_iterations > 0:
        tool_result = call_tool(response_message_part.function_call)
    
        function_response_part = types.Part.from_function_response(
            name=response_message_part.function_call.name,
            response={"result": tool_result},
        )
        messages.append(function_response_part)
    
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=messages,
            config=config,
        )
        response_message_part = response.candidates[0].content.parts[0]
        messages.append(response.candidates[0].content)
        max_iterations -= 1
    ```
    This loop works for sequential tasks. However, it has a major limitation: it assumes the agent should call a tool at each step and doesn't allow the LLM to *reason* about a tool's output before deciding on the next action. The agent immediately moves to the next function call without pausing to think.

This limitation leads to more sophisticated patterns like **ReAct** (Reasoning and Acting), which explicitly interleaves reasoning steps with tool calls. We will explore ReAct in detail in Lessons 7 and 8.

## Popular Tools Used Within the Industry

To ground this in the real world, let's look at common tool categories used in production AI systems.

1.  **Knowledge & Memory Access:** These tools connect agents to information. They can query vector databases for semantic search, document stores, or even traditional SQL databases using text-to-SQL capabilities. This is fundamental for building RAG systems, a topic we will cover in Lesson 10, and for providing agents with long-term memory, which we will discuss in Lesson 9.
2.  **Web Search & Browsing:** These tools give agents access to the live internet. They can interface with search engine APIs (like Google or Bing) or use web scraping tools to fetch and parse content from web pages. This is essential for research agents and chatbots that need up-to-date information.
3.  **Code Execution:** A Python interpreter tool allows an agent to write and execute code in a sandboxed environment. This is invaluable for performing calculations, manipulating data, or generating visualizations.
4.  **Other Popular Tools:** Agents can interact with almost any external API, enabling them to manage calendars, send emails, or operate project management software. They can also perform file system operations, like reading and writing files, which is common in productivity applications.

## Conclusion

Tool calling is the core mechanism that allows an AI agent to interact with the world. Understanding how to define, implement, and orchestrate tools is one of the most critical skills for an AI Engineer.

Now that our agent can act, it's time to teach it how to think. In our next lesson, we will explore the theory behind planning and reasoning, introducing the ReAct pattern that enables more deliberate and intelligent agent behavior.

## References

- [1] Function calling with OpenAI's API. (n.d.). OpenAI. https://platform.openai.com/docs/guides/function-calling
- [2] Gao, Y., et al. (2024). Efficient Tool Use with Chain-of-Abstraction Reasoning. arXiv. https://arxiv.org/pdf/2401.17464v3
- [3] Function calling with the Gemini API. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [4] Building effective agents. (n.d.). Anthropic. https://www.anthropic.com/research/building-effective-agents