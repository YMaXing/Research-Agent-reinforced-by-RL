# Lesson 6: Agent Tools & Function Calling

In our previous lessons, we built a solid foundation in AI Engineering. We explored the landscape of AI agents, distinguished between rule-based LLM workflows and autonomous agents, and mastered context engineering and structured outputs. We learned how to chain, route, and orchestrate different components to build basic workflows.

Now, we will explore one of the most critical building blocks of any AI Agent: **Tools**, also known as Function Calling. We will learn how to give our LLM the ability to take action. By implementing tool calling from scratch, you will understand how an LLM decides which tool to call, generates the correct parameters, and executes the function. This lesson will open the black box, showing you what separates a simple text generator from an agent that can interact with the external world.

## Understanding why agents need tools

LLMs have a fundamental limitation: they are powerful pattern matchers and text generators, but they cannot perform actions or interact with the external world on their own. They are trained on vast amounts of text and store their knowledge within their weights, but this knowledge is static and disconnected from real-time information or external systems. This is where tools come in.

Think of the LLM as the brain of an agent. Tools are its "hands and senses," allowing it to perceive and act in the world beyond its textual interface. They are the bridge between the LLM's internal reasoning and the external environment. With tools, an LLM transforms into an AI agent capable of executing specific instructions and interacting with the world.

This capability unlocks a wide range of applications. Modern AI agents use tools to:
- Access real-time information through APIs, such as checking today's weather or fetching the latest news [[19]](https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf).
- Interact with external databases and storage solutions, from traditional PostgreSQL databases to vector stores [[12]](https://www.ruh.ai/blogs/how-vector-databases-are-rewiring-the-tech-industry).
- Access the agent's long-term memory to recall information beyond the immediate context window [[11]](https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/).
- Execute code in sandboxed environments like Python or JavaScript for precise calculations, data manipulation, or visualizations [[18]](https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f).

## Implementing tool calls from scratch

The best way to understand how tools work is to build them from scratch. We will provide an LLM with a list of available tools and let it decide which one to use and what arguments to pass. The process involves a five-step flow between your application and the LLM.

The high-level process looks like this:
1.  **Application:** You send the LLM a prompt along with a list of available tools defined by their schemas.
2.  **LLM:** It analyzes the prompt and decides if a tool is needed. If so, it responds with a `function_call` request, specifying the tool's name and the arguments.
3.  **Application:** You parse this request and execute the corresponding function in your code.
4.  **Application:** You send the function's output back to the LLM as an observation.
5.  **LLM:** It uses the tool's output to generate a final, user-facing response or decide the next action.

This request-execute-respond cycle is the foundation of tool use in AI agents.

```mermaid
flowchart LR
  %% Main Actors
  A["Application"]
  L["LLM"]

  %% Available Tools
  subgraph Tools["Available Tools"]
    SGD["search_google_drive"]
    SDM["send_discord_message"]
    SR["summarize_report"]
  end

  %% 5-Step Request-Execute-Respond Flow
  A -- "1. Sends prompt & available tools" --> L
  L -- "2. Responds with function_call<br/>(tool, arguments)" --> A
  A -- "3. Executes requested function" --> Tools
  Tools -- "Returns function output" --> A
  A -- "4. Sends function output" --> L
  L -- "5. Generates user-facing response" --> A

  %% Visual grouping
  classDef actor stroke-width:2px
  classDef external stroke-dasharray:3,3
  class A,L actor
  class SGD,SDM,SR external
```
Image 1: Flowchart illustrating the 5-step request-execute-respond flow of calling a tool.

Let's implement a simple example where we mock searching for a document on Google Drive and sending its summary to a Discord channel.

<aside>
💡

You can find the code for this lesson in the accompanying [Jupyter Notebook](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/06_tools/notebook.ipynb) in the course's GitHub repository.

</aside>

1.  First, we set up our environment by importing the necessary libraries and initializing the Gemini client. We will use the `gemini-2.5-flash` model, which is fast and cost-effective for our examples. We also define a sample `DOCUMENT` to mock the content of a file.
    ```python
    import json
    from typing import Any
    
    from google import genai
    from google.genai import types
    from pydantic import BaseModel, Field
    
    from lessons.utils import env, pretty_print
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    
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
2.  Next, we define our mock tools as Python functions. The function signature and docstring are critical, as the LLM uses them to understand what each tool does. To keep the code simple, these functions return hardcoded data.
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
3.  For the LLM to understand and use these functions, we must provide their definitions as a schema, often described in JSON. This schema acts as a contract, telling the model the tool's name, what it does (`description`), and how to call it (`parameters`). This is an industry standard used by APIs from OpenAI, Google, and Anthropic.
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
    ```python
    send_discord_message_schema = {
        "name": "send_discord_message",
        "description": "Sends a message to a specific Discord channel.",
        "parameters": {
            "type": "object",
            "properties": {
                "channel_id": {
                    "type": "string",
                    "description": "The ID of the channel to send the message to, e.g., '#finance'.",
                },
                "message": {
                    "type": "string",
                    "description": "The content of the message to send.",
                },
            },
            "required": ["channel_id", "message"],
        },
    }
    ```
    ```python
    summarize_financial_report_schema = {
        "name": "summarize_financial_report",
        "description": "Summarizes a financial report.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text to summarize.",
                },
            },
            "required": ["text"],
        },
    }
    ```
4.  We then create a tool registry to map tool names to their corresponding functions (`handler`) and schemas (`declaration`).
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
    The `TOOLS_BY_NAME` mapping looks like this:
    ```text
    Tool name: search_google_drive
    Tool handler: <function search_google_drive at 0x104c7df80>
    ---------------------------------------------------------------------------
    Tool name: send_discord_message
    Tool handler: <function send_discord_message at 0x104c7de40>
    ---------------------------------------------------------------------------
    Tool name: summarize_financial_report
    Tool handler: <function summarize_financial_report at 0x1274f5c60>
    ---------------------------------------------------------------------------
    ```
    And here is the schema for our `search_google_drive` tool:
    ```text
    {
      "name": "search_google_drive",
      "description": "Searches for a file on Google Drive and returns its content or a summary.",
      "parameters": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "The search query to find the file, e.g., 'Q3 earnings report'."
          }
        },
        "required": [
          "query"
        ]
      }
    }
    ```
5.  Now, we create a system prompt to instruct the LLM on how to use these tools. This prompt includes guidelines on when to use tools, how to select them, and the exact format for a tool call. We embed the `TOOLS_SCHEMA` inside `<tool_definitions>` XML tags.
    ```python
    TOOL_CALLING_SYSTEM_PROMPT = """
    You are a helpful AI assistant with access to tools that enable you to take actions and retrieve information to better 
    assist users.
    
    ## Tool Usage Guidelines
    
    **When to use tools:**
    - When you need information that is not in your training data
    - When you need to perform actions in external systems and environments
    - When you need real-time, dynamic, or user-specific data
    - When computational operations are required
    
    **Tool selection:**
    - Choose the most appropriate tool based on the user's specific request
    - If multiple tools could work, select the one that most directly addresses the need
    - Consider the order of operations for multi-step tasks
    
    **Parameter requirements:**
    - Provide all required parameters with accurate values
    - Use the parameter descriptions to understand expected formats and constraints
    - Ensure data types match the tool's requirements (strings, numbers, booleans, arrays)
    
    ## Tool Call Format
    
    When you need to use a tool, output ONLY the tool call in this exact format:
    
    <tool_call>
    {{"name": "tool_name", "args": {{"param1": "value1", "param2": "value2"}}}}
    </tool_call>
    
    **Critical formatting rules:**
    - Use double quotes for all JSON strings
    - Ensure the JSON is valid and properly escaped
    - Include ALL required parameters
    - Use correct data types as specified in the tool definition
    - Do not include any additional text or explanation in the tool call
    
    ## Response Behavior
    
    - If no tools are needed, respond directly to the user with helpful information
    - If tools are needed, make the tool call first, then provide context about what you're doing
    - After receiving tool results, provide a clear, user-friendly explanation of the outcome
    - If a tool call fails, explain the issue and suggest alternatives when possible
    
    ## Available Tools
    
    <tool_definitions>
    {tools}
    </tool_definitions>
    
    Remember: Your goal is to be maximally helpful to the user. Use tools when they add value, but don't use them unnecessarily. Always prioritize accuracy and user experience.
    """
    ```
    Based on the `description` field in the tool schema, the LLM *decides* if a tool is appropriate for the user's query. This is why clear and distinct tool descriptions are critical. Vague descriptions like "Tool to search documents" can confuse the model, especially when multiple similar tools exist. Explicit descriptions like "Tool to search documents on Google Drive" versus "Tool to search files on the local disk" prevent ambiguity. This becomes essential when an agent has access to 50-100 tools. Once a tool is selected, the LLM *generates* the function name and arguments as a structured output, like JSON. This capability is enabled by instruction fine-tuning, which trains the model to interpret schemas and produce valid tool calls.

6.  Let's test it. We send a user prompt along with our system prompt to the model.
    ```python
    USER_PROMPT = """
    Can you help me find the latest quarterly report and share key insights with the team?
    """
    
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
    )
    ```
    The LLM correctly identifies the `search_google_drive` tool and generates the required arguments:
    ```text
    <tool_call>
    {"name": "search_google_drive", "args": {"query": "latest quarterly report"}}
    </tool_call>
    ```
7.  For a multi-step request, the model chains the tools sequentially.
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
    It first calls the search tool:
    ```text
    <tool_call>
    {"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}
    </tool_call>
    ```
8.  Now we need to parse the LLM's response and execute the tool. We start by extracting the JSON string from the response.
    ```python
    def extract_tool_call(response_text: str) -> str:
        """
        Extracts the tool call from the response text.
        """
        return response_text.split("<tool_call>")[1].split("</tool_call>")[0].strip()
    
    tool_call_str = extract_tool_call(response.text)
    ```
    This gives us a string: `'{"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}'`.

9.  Next, we parse this string into a Python dictionary.
    ```python
    tool_call = json.loads(tool_call_str)
    ```
    The output is a dictionary: `{'name': 'search_google_drive', 'args': {'query': 'Q3 earnings report'}}`.

10. We retrieve the actual Python function (the handler) from our `TOOLS_BY_NAME` registry.
    ```python
    tool_handler = TOOLS_BY_NAME[tool_call["name"]]
    ```
    The `tool_handler` is now a reference to our `search_google_drive` function.

11. Finally, we execute the function using the arguments generated by the LLM.
    ```python
    tool_result = tool_handler(**tool_call["args"])
    ```
    The tool returns the mocked document content:
    ```text
    {
      "files": [
        {
          "name": "Q3_Earnings_Report_2024.pdf",
          "id": "file12345",
          "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations..."
        }
      ]
    }
    ```
12. We can wrap these steps in a convenient `call_tool` function.
    ```python
    def call_tool(response_text: str, tools_by_name: dict) -> Any:
        """
        Call a tool based on the response from the LLM.
        """
    
        tool_call_str = extract_tool_call(response_text)
        tool_call = json.loads(tool_call_str)
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool = tools_by_name[tool_name]
    
        return tool(**tool_args)
    ```
    Using this function gives us the same result as before.

13. After executing the tool, we typically send the result back to the LLM to interpret it and formulate a user-facing response or decide on the next step.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=f"Interpret the tool result: {json.dumps(tool_result, indent=2)}",
    )
    ```
    The LLM provides a natural language summary:
    ```text
    The tool result provides the content of a file named `Q3_Earnings_Report_2024.pdf`.
    
    This document is a **Q3 2023 Financial Performance Analysis** and details exceptionally strong results, significantly beating market expectations.
    
    **Key highlights from the report include:**
    
    *   **Revenue Growth:** A 20% increase in revenue.
    *   **User Engagement:** 15% growth in user engagement.
    ...
    ```
This covers the basic concepts of tool calling from scratch.

## Implementing a small tool calling framework from scratch

Manually defining a JSON schema for every tool is tedious and error-prone. Modern agentic frameworks like LangGraph and protocols like MCP (Model Context Protocol) automate this by using a `@tool` decorator. This decorator inspects a function's signature and docstring to generate the schema automatically.

This approach follows the Don't Repeat Yourself (DRY) principle by creating a single source of truth for the tool's implementation and its schema. Let's build a simple framework with a `@tool` decorator to streamline our implementation.

1.  First, we define a `ToolFunction` class to wrap our decorated functions and store their schema.
    ```python
    from inspect import Parameter, signature
    from typing import Any, Callable, Dict, Optional
    
    
    class ToolFunction:
        def __init__(self, func: Callable, schema: Dict[str, Any]) -> None:
            self.func = func
            self.schema = schema
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__
    
        def __call__(self, *args: Any, **kwargs: Any) -> Any:
            return self.func(*args, **kwargs)
    ```
2.  Next, we create the `@tool` decorator. It inspects the function's signature to build the `parameters` schema, extracting parameter names and whether they are required. The function's name and docstring are used for the tool's `name` and `description`.
    ```python
    def tool(description: Optional[str] = None) -> Callable[[Callable], ToolFunction]:
        """
        A decorator that creates a tool schema from a function.
    
        Args:
            description: Optional override for the function's docstring
    
        Returns:
            A decorator function that wraps the original function and adds a schema
        """
    
        def decorator(func: Callable) -> ToolFunction:
            # Get function signature
            sig = signature(func)
    
            # Create parameters schema
            properties = {}
            required = []
    
            for param_name, param in sig.parameters.items():
                # Skip self for methods
                if param_name == "self":
                    continue
    
                param_schema = {
                    "type": "string",  # Default to string, can be enhanced with type hints
                    "description": f"The {param_name} parameter",  # Default description
                }
    
                # Add to required if parameter has no default value
                if param.default == Parameter.empty:
                    required.append(param_name)
    
                properties[param_name] = param_schema
    
            # Create the tool schema
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
3.  Now, we can redefine our tools using this decorator. The code is much cleaner as the schemas are generated automatically.
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
    ```
4.  Each decorated function is now a `ToolFunction` object. It contains the schema and a reference to the original function handler.
    The schema for `search_google_drive_example` is identical to the one we defined manually:
    ```text
    {
      "name": "search_google_drive_example",
      "description": "Search for files in Google Drive.",
      "parameters": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "The query parameter"
          }
        },
        "required": [
          "query"
        ]
      }
    }
    ```
    And we can access the underlying function via `search_google_drive_example.func`.

5.  We build our `tools_by_name` and `tools_schema` mappings as before and call the LLM.
    ```python
    tools = [
        search_google_drive_example,
        send_discord_message_example,
        summarize_financial_report_example,
    ]
    tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
    tools_schema = [tool.schema for tool in tools]
    
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
    The model's response is the same:
    ```text
    <tool_call>
    {"name": "search_google_drive_example", "args": {"query": "Q3 earnings report"}}
    </tool_call>
    ```
6.  Executing the tool call with our `call_tool` function also works just as before.
    ```python
    call_tool(response.text, tools_by_name=tools_by_name)
    ```
    It outputs: `{'files': ['Q3 earnings report']}`.

Voilà! We have created a small, reusable tool-calling framework. This implementation is conceptually similar to what frameworks like LangGraph do under the hood to simplify tool definition.

## Implementing production-level tool calls with Gemini

In production, it is best to leverage the native tool-calling features of modern LLM APIs like Gemini or OpenAI. Instead of manually engineering a system prompt, we can use the provider's configuration objects. This approach is simpler, more robust, and more efficient, as the provider optimizes the process for their specific models.

Let's refactor our example to use Gemini's native API.

1.  We define a `GenerateContentConfig` object and pass our tool schemas to it. We can also set the `mode` to `"ANY"` to force the model to call a tool instead of generating a text response.
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
2.  With this configuration, we can call the model directly with the user prompt, completely removing our lengthy `TOOL_CALLING_SYSTEM_PROMPT`.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=USER_PROMPT,
        config=config,
    )
    ```
3.  The Google `genai` Python SDK simplifies this even further by allowing us to pass Python functions directly into the configuration. The SDK automatically extracts the schema from the function's signature, type hints, and docstring, just like our custom decorator.
    ```python
    config = types.GenerateContentConfig(
        tools=[search_google_drive, send_discord_message]
    )
    ```
4.  The response object now contains a structured `function_call` attribute, which we can inspect and use directly.
    ```python
    function_call = response.candidates[0].content.parts[0].function_call
    ```
    This object has a `name` and `args` that we can use to execute the tool.
    
5.  We can simplify our `call_tool` function to work with Gemini's native `FunctionCall` object.
    ```python
    def call_tool(function_call) -> Any:
        tool_name = function_call.name
        tool_args = {key: value for key, value in function_call.args.items()}
    
        tool_handler = TOOLS_BY_NAME[tool_name]
    
        return tool_handler(**tool_args)
    
    tool_result = call_tool(function_call)
    ```
    By leveraging the native SDK, we reduced dozens of lines of code to just a few, creating a more robust and maintainable system. Other popular APIs from OpenAI and Anthropic follow a similar logic, making these concepts easily transferable.

## Using Pydantic models as tools for on-demand structured outputs

We can combine the power of tool calling with the structured data validation of Pydantic, a topic we covered in Lesson 4. A powerful pattern in agentic systems is to treat a Pydantic model as a tool. This allows an agent to perform several intermediate steps with unstructured text and then, when it's ready, call a specific "tool" to format its final answer into a reliable, structured Pydantic object.

This is useful for workflows where you need a structured output only at the end of a multi-step process, ensuring the final data is clean and validated for downstream use in your Python application.

```mermaid
flowchart LR
    A["AI Agent"]
    B["Tool Call<br/>(Unstructured Output)"]
    C["Pydantic Model Tool Call<br/>(Structured Output)<br/>(using DocumentMetadata)"]
    D["Final Structured Output"]

    A -- "initiates" --> B
    B -- "unstructured result<br/>(loop)" --> A
    A -- "decides to make<br/>structured call" --> C
    C -- "produces" --> D

    classDef tool stroke-dasharray: 5, 5
    class B,C tool
```
Image 2: A flowchart illustrating an AI agent calling multiple tools in a loop, where only the last one is a tool call for structured outputs.

Let's see how to implement this.

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
3.  We prompt the model to analyze the document and extract the metadata.
    ```python
    prompt = f"""
    Please analyze the following document and extract its metadata.
    
    Document:
    --- 
    {DOCUMENT}
    --- 
    """
    
    response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
    ```
4.  The model responds with a function call to our `extract_metadata` tool, with the arguments already structured according to our Pydantic schema.
    ```text
     Function Name:  `extract_metadata
     Function Arguments:  `{
        "growth_rate": "20%",
        "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy and market expansion. This performance provides a strong foundation for continued growth.",
        "quarter": "Q3 2023",
        "keywords": [
          "Revenue",
          "User Engagement",
          "Market Expansion",
        ],
        "tags": [
          "Financials",
          "Earnings",
          "Growth",
        ]
      }`
    ```
5.  We can then validate these arguments and parse them directly into a `DocumentMetadata` object.
    ```python
    function_call = response.candidates[0].content.parts[0].function_call
    
    try:
        document_metadata = DocumentMetadata(**function_call.args)
        print("Validation successful!")
    except Exception as e:
        print(f"Validation failed: {e}")
    ```
This pattern is frequently used in AI agents that require reliable, structured data as their final output.

## The downsides of running tools in a loop

So far, we have focused on single-turn interactions. However, real-world tasks often require multiple steps. A natural progression is to run tools in a loop, allowing an agent to chain multiple actions together. The agent can decide which tool to use at each step based on the output of the previous one. This is the final piece of the puzzle needed to build a true AI agent.

```mermaid
flowchart LR
  A["User Prompt"]
  B["LLM/Agent"]
  C["Tool Call"]
  D["Tool Result"]
  E["Final Response"]

  A -- "provides" --> B
  B -- "initiates" --> C
  C -- "returns" --> D
  D -- "informs decision" --> B
  B -- "continues loop<br/>(Tool Call)" --> C
  B -- "exits loop<br/>(Generate Response)" --> E
```
Image 3: A flowchart illustrating a tool calling loop by an LLM/Agent.

This approach offers flexibility and adaptability, enabling agents to handle complex, multi-step tasks. Let's implement a loop where an agent first finds a report on Google Drive, summarizes it, and then sends the summary to a Discord channel.

1.  We configure the model with all three of our tools: `search_google_drive`, `summarize_financial_report`, and `send_discord_message`.
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
2.  We provide a multi-step prompt and initialize a message history.
    ```python
    USER_PROMPT = """
    Please find the Q3 earnings report on Google Drive and send a summary of it to 
    the #finance channel on Discord.
    """
    
    messages = [USER_PROMPT]
    ```
3.  We run a loop that continues as long as the model requests a function call. In each iteration, we execute the tool, append the result to the message history, and send it back to the model to decide on the next step.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
        config=config,
    )
    response_message_part = response.candidates[0].content.parts[0]
    messages.append(response.candidates[0].content)
    
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
    The agent successfully executes the three tools in sequence: first searching, then summarizing, and finally sending the message.

However, this simple loop has significant limitations. It does not allow the LLM to interpret the output of each tool before deciding on the next action. The agent immediately moves to the next function call without a "thought" step to analyze what it has learned or adjust its strategy. This can lead to inefficient tool usage or getting stuck in loops.

For tasks where tools are independent, we can run them in parallel to reduce latency. For example, fetching financial news and stock prices can happen simultaneously. However, many tasks have dependencies that require a more deliberate, step-by-step approach.

These limitations motivated the development of more sophisticated agentic patterns like **ReAct** (Reasoning and Acting). ReAct explicitly interleaves reasoning steps with actions, allowing the agent to "think" about its plan and the results of its actions. We will explore this powerful pattern in detail in Lessons 7 and 8.

## Popular tools used within the industry

To ground these concepts in the real world, let's look at some popular tool categories used across the industry. These examples showcase what's possible when you connect LLMs to external systems.

### Knowledge & Memory Access
These tools allow agents to retrieve information beyond their training data. This includes querying vector databases for semantic search, document stores, or graph databases to understand relationships between entities. A powerful pattern in this category is text-to-SQL, where an agent constructs and executes SQL queries on traditional databases based on natural language prompts [[13]](https://promethium.ai/guides/text-to-sql-basics-benefits/). These tools are fundamental for memory and Retrieval-Augmented Generation (RAG), which we will cover in Lessons 9 and 10.

### Web Search & Browsing
A common use case for agents is accessing up-to-date information from the internet. This is achieved through tools that interface with search engine APIs like Google Search, Bing, or Brave [[17]](https://mantraideas.com/llm-web-search/). More advanced tools can also scrape and parse content directly from web pages, enabling agents to conduct deep research or monitor websites for changes.

### Code Execution
Code interpreter tools give agents the ability to write and execute code, typically in a sandboxed environment. A Python interpreter is invaluable for performing precise calculations, manipulating data, running statistical analyses, and creating visualizations—tasks where LLMs alone often struggle [[16]](https://arxiv.org/html/2507.08034v1). While Python is the most common, this pattern can be adapted for other languages like JavaScript.

### Other Popular Tools
The possibilities for tools are nearly endless. In enterprise settings, agents often interact with external APIs for calendars, email, and project management systems, automating routine business workflows. Productivity-focused AI applications might use tools for file system operations, like reading and writing files or listing directories, allowing them to interact directly with a user's operating system.

## Conclusion

Tool calling is a cornerstone of modern AI agents. It transforms LLMs from passive text generators into active participants that can interact with the external world. Understanding how to build, manage, and debug tools is one of the most important skills for an AI Engineer.

In this lesson, we have gone from implementing tool calling from scratch to using production-grade APIs. We have seen the power of chaining tools in a loop and also recognized its limitations. This sets the stage for our next lesson, where we will explore the theory behind more advanced agentic patterns like ReAct, which enable more sophisticated planning and reasoning.

## References

- [1]  https://www.philschmid.de/gemini-function-calling 
- [2]  https://ai.google.dev/gemini-api/docs/function-calling 
- [3]  https://glaforge.dev/posts/2023/12/22/gemini-function-calling/ 
- [4]  https://pydantic.dev/docs/ai/core-concepts/output/ 
- [5]  https://pydantic.dev/docs/ai/guides/multi-agent-applications/ 
- [6]  https://discuss.ai.google.dev/t/response-schema-from-pydantic/50028 
- [7]  https://pydantic.dev/docs/ai/tools-toolsets/tools/ 
- [8]  https://myengineeringpath.dev/genai-engineer/agentic-patterns/ 
- [9]  https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems 
- [10]  https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/ 
- [11]  https://www.ruh.ai/blogs/how-vector-databases-are-rewiring-the-tech-industry 
- [12]  https://promethium.ai/guides/text-to-sql-basics-benefits/ 
- [13]  https://www.instaclustr.com/education/vector-database/top-10-open-source-vector-databases/ 
- [14]  https://arxiv.org/html/2507.08034v1 
- [15]  https://mantraideas.com/llm-web-search/ 
- [16]  https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f 
- [17]  https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf 
- [18]  https://medium.com/@yugalnandurkar5/llm-engineering-part-i-fa48d4307d26 
- [19]  https://community.openai.com/t/prompting-best-practices-for-tool-use-function-calling/1123036 
- [20]  https://medium.com/@hariomshahu101/building-production-ready-llm-applications-bulletproof-llm-tool-calling-with-advanced-json-b95ce8889f4e 
- [21]  https://tetrate.io/learn/ai/llm-output-parsing-structured-generation 
- [22]  https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools 
- [23]  https://openai.github.io/openai-agents-python/tools/ 
- [24]  https://docs.langchain.com/oss/python/langchain/tools 
- [25]  https://reference.langchain.com/python/langchain-core/tools/convert/tool 
- [26]  https://www.anthropic.com/research/building-effective-agents 
- [27]  https://pub.towardsai.net/tool-descriptions-are-critical-making-better-llm-tools-research-capability-b315851471e7 
- [28]  https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-1-llm-agent-tooling-foundations/tool-input-output-schemas 
- [29]  https://medium.com/@abhaychougule0907/underlying-factors-behind-inconsistency-in-llm-responses-with-multi-tool-calling-628ce7b4de76 
- [30]  https://arxiv.org/html/2505.18135v2 
- [31]  https://www.decodingai.com/p/tool-calling-from-scratch-to-production 
- [32]  https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-4-interacting-with-llm-apis/overview-common-llm-apis 
- [33]  https://www.getorchestra.io/guides/llm-providers-gen-ai-platforms-compared 
- [34]  https://myengineeringpath.dev/tools/gemini-guide/ 
- [35]  https://futuresearch.ai/blog/llm-provider-quirks/