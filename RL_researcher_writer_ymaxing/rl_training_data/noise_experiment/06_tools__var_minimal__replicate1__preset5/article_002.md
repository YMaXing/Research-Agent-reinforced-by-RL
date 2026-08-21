# Lesson 6: Agent Tools & Function Calling

In previous lessons, we learned to manage information flow *to* an LLM and get reliable data *from* it. Now, we will explore a critical building block of any AI Agent: giving it the ability to take action. This capability is the stepping stone that transforms a reactive text generator into a proactive agent that can autonomously execute complex tasks [[23]](https://fireworks.ai/blog/function-calling).

This lesson explores **Tools**, also known as **Function Calling**. This is the mechanism that transforms an LLM from a passive text generator into an active agent that can interact with the external world. We will open the black box by implementing tool calling from scratch to understand how an agent decides which action to take, generates the correct parameters, and executes it.

## Understanding Why Agents Need Tools

LLMs have a fundamental limitation: they are pattern matchers whose knowledge is frozen at the time of training. By themselves, they cannot interact with the outside world or access real-time information, which can lead to factual inaccuracies or "hallucinations" [[24]](https://www.digital-alpha.com/a-deep-dive-into-function-calling-with-llms/). They are like a brain in a jar, capable of reasoning but unable to act. This is where tools come in.

Tools are the "hands and senses" of an LLM, allowing it to perceive and act in the world beyond its training data [[1]](https://www.youtube.com/watch?v=h8gMhXYAv1k). They are the bridge between the model's internal reasoning and the external environment. With tools, an LLM becomes an AI agent that can execute instructions and interact with other systems.

Popular tools that power modern AI agents include:
*   Accessing real-time information through APIs (e.g., weather, news) [[2]](https://arxiv.org/html/2507.08034v1).
*   Interacting with external databases or data warehouses [[3]](https://promethium.ai/guides/text-to-sql-basics-benefits/).
*   Accessing the agent's long-term memory to recall information beyond its context window [[4]](https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/).
*   Executing code for precise calculations or data manipulation [[5]](https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f).

## Implementing Tool Calls from Scratch

The best way to understand how tools work is to build the mechanism from scratch. Our goal is to provide the LLM with a list of available tools and let it decide which one to use, generating the correct arguments needed to call the function. The high-level process looks like this:

1.  **Application:** You send the LLM a prompt and a list of available tool definitions.
2.  **LLM:** It responds with a `function_call` request, specifying the tool's name and arguments.
3.  **Application:** You execute the requested function in your code.
4.  **Application:** You send the function's output back to the LLM.
5.  **LLM:** It uses the tool's output to generate a final, user-facing response [[6]](https://www.philschmid.de/gemini-function-calling).

```mermaid
sequenceDiagram
    participant Application
    participant LLM
    participant Tool

    Application->>LLM: "Send Prompt & Tool Definitions"
    LLM-->>Application: "Respond with function_call(tool_name, args)"
    Application->>Tool: "Execute tool_name(args)<br/>(e.g., search_google_drive, send_discord_message, summarize_report)"
    Tool-->>Application: "Return Tool Output"
    Application->>LLM: "Send Tool Output"
    LLM-->>Application: "Generate Final User-Facing Response"
```
Image 1: A sequence diagram illustrating the 5-step request-execute-respond flow of calling a tool.

Let's implement a simple example where we mock searching for a document on Google Drive and sending its summary to a Discord channel.

<aside>
💡

You can find the code for this lesson in the accompanying [Jupyter Notebook](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/06_tools/notebook.ipynb) in the course repository.

</aside>

1.  First, we set up our environment by initializing the Gemini client. We will use `gemini-2.5-flash` for its speed and cost-effectiveness. We also define a `DOCUMENT` constant to mock the content of a file.
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

2.  Next, we define three mock functions. The function signatures and docstrings are essential, as the LLM uses them to understand what each tool does.
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

3.  For each function, we create a JSON schema. This schema tells the LLM what the tool does (via `description`) and how to call it (via `parameters`). This format is an industry standard used by major providers like OpenAI and Google [[7]](https://platform.openai.com/docs/guides/function-calling), [[8]](https://ai.google.dev/gemini-api/docs/function-calling).
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

4.  We then aggregate our tools and their schemas into registries for easy access.
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
    The `TOOLS_BY_NAME` mapping gives us a quick way to access the function handler, and `TOOLS_SCHEMA` is what we will pass to the LLM.

5.  Now, we create a system prompt that instructs the LLM on how to use these tools. It includes guidelines, the required output format, and the list of available tool schemas, often wrapped in XML tags for clarity.
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

6.  Based on the `description` field in the schema, the LLM *decides* if a tool is appropriate for the user's query. This is why clear and distinct tool descriptions are vital. This aligns with a core design principle for tools: each tool should follow the Single Responsibility Principle, handling one specific task well [[25]](https://medium.com/@zhihao.zhou.bupt/the-smart-principles-designing-interfaces-that-llms-understand-aca00630c8c9). Multi-purpose "god tools" with complex parameters tend to confuse the model, making selection harder [[26]](https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-1-llm-agent-tooling-foundations/designing-tool-interfaces). Vague descriptions like "search documents" versus explicit ones like "search documents on Google Drive" also prevent ambiguity [[9]](https://www.anthropic.com/research/building-effective-agents), [[10]](https://pub.towardsai.net/tool-descriptions-are-critical-making-better-llm-tools-research-capability-b315851471e7).

7.  These design principles become critical as you scale to dozens or even hundreds of tools per agent. As the number of available tools grows, an LLM's ability to select the correct one degrades, sometimes falling off an "accuracy cliff" once a certain threshold is passed [[27]](https://arxiv.org/html/2509.21199v3). The sheer number of choices increases the computational complexity and can strain the model's context window [[28]](https://aclanthology.org/2025.findings-acl.811.pdf). Once a tool is selected, the LLM *generates* the function name and arguments as a structured JSON output. This capability is enabled by instruction fine-tuning, where models are specifically trained to interpret schemas and produce valid tool calls [[11]](https://arxiv.org/pdf/2401.17464v3).

8.  Let's test it with two different prompts.
    ```python
    USER_PROMPT_1 = """
    Can you help me find the latest quarterly report and share key insights with the team?
    """
    
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT_1]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
    )
    ```
    It outputs:
    ```text
    <tool_call>
    {"name": "search_google_drive", "args": {"query": "latest quarterly report"}}
    </tool_call>
    ```
    ```python
    USER_PROMPT_2 = """
    Please find the Q3 earnings report on Google Drive and send a summary of it to 
    the #finance channel on Discord.
    """
    
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT_2]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
    )
    ```
    It outputs:
    ```text
    <tool_call>
    {"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}
    </tool_call>
    ```

9.  Now, let's parse the LLM's response step-by-step. First, we extract the JSON string from the XML tags.
    ```python
    def extract_tool_call(response_text: str) -> str:
        return response_text.split("<tool_call>")[1].split("</tool_call>")[0].strip()

    tool_call_str = extract_tool_call(response.text)
    ```
    It outputs:
    ```text
    '{"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}'
    ```

10. Next, we parse the string into a Python dictionary.
    ```python
    tool_call = json.loads(tool_call_str)
    ```
    It outputs:
    ```text
    {'name': 'search_google_drive', 'args': {'query': 'Q3 earnings report'}}
    ```

11. We use the tool name to retrieve the correct function handler from our registry.
    ```python
    tool_handler = TOOLS_BY_NAME[tool_call["name"]]
    ```
    It outputs:
    ```text
    <function __main__.search_google_drive(query: str) -> dict>
    ```

12. Finally, we execute the function with the arguments provided by the LLM.
    ```python
    tool_result = tool_handler(**tool_call["args"])
    ```
    It outputs:
    ```text
    {'files': [{'name': 'Q3_Earnings_Report_2024.pdf', 'id': 'file12345', 'content': '...'}]}
    ```

13. We can wrap this logic in a single helper function.
    ```python
    def call_tool(response_text: str, tools_by_name: dict) -> Any:
        tool_call_str = extract_tool_call(response_text)
        tool_call = json.loads(tool_call_str)
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool = tools_by_name[tool_name]
        return tool(**tool_args)
    ```
    The `tool_result` is then sent back to the LLM, which uses it to formulate a final response or decide on the next step. This completes the basic tool-calling loop.

## Implementing a Tool Calling Framework from Scratch

Manually defining a JSON schema for every function is tedious, error-prone, and violates the Don't Repeat Yourself (DRY) software principle [[12]](https://openai.github.io/openai-agents-python/tools/), [[13]](https://pydantic.dev/docs/ai/tools-toolsets/tools/). If the function's signature changes, you must remember to update the schema, creating a maintenance burden. Production frameworks like LangGraph solve this by using decorators to automatically generate schemas from function signatures and docstrings, keeping the function as the single source of truth [[1]](https://www.youtube.com/watch?v=h8gMhXYAv1k).

Let's build a simple `@tool` decorator to create our own mini-framework.

1.  First, we define a `ToolFunction` class. This class acts as a container, bundling the executable function (`.func`) with its machine-readable description (`.schema`). This turns a standard Python function into a self-contained, portable "tool".
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

2.  Then, we create the `@tool` decorator, which inspects a function's signature and docstring using Python's `inspect` module to build the schema automatically.
    ```python
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

3.  Now, we can decorate our functions directly.
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

4.  The decorator wraps each function in a `ToolFunction` object. We can inspect this object to see its type, the auto-generated schema, and the original function handler.
    ```python
    type(search_google_drive_example)
    ```
    It outputs:
    ```text
    __main__.ToolFunction
    ```
    ```python
    search_google_drive_example.schema
    ```
    It outputs:
    ```text
    {'name': 'search_google_drive_example', 'description': 'Search for files in Google Drive.', 'parameters': {'type': 'object', 'properties': {'query': {'type': 'string', 'description': 'The query parameter'}}, 'required': ['query']}}
    ```
    ```python
    search_google_drive_example.func
    ```
    It outputs:
    ```text
    <function __main__.search_google_drive_example(query: str) -> dict>
    ```

5.  We can now use the auto-generated schemas with our `TOOL_CALLING_SYSTEM_PROMPT` as before.
    ```python
    tools = [
        search_google_drive_example,
        send_discord_message_example,
        summarize_financial_report_example,
    ]
    tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
    tools_schema = [tool.schema for tool in tools]
    
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(tools_schema)), USER_PROMPT]
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
    )
    
    call_tool(response.text, tools_by_name=tools_by_name)
    ```
    It outputs:
    ```text
    {'files': ['Q3 earnings report']}
    ```
    This implementation is conceptually similar to what frameworks like LangChain do internally [[14]](https://docs.langchain.com/oss/python/langchain/tools).

## Implementing Production-Level Tool Calls with Gemini

While building from scratch is a good learning exercise, production systems should use the native tool-calling features of APIs like Gemini. This is more robust, as the provider optimizes the underlying prompting and logic for their specific models [[15]](https://www.newsletter.swirlai.com/p/building-ai-agents-from-scratch-part).

Let's see how to achieve the same result with Gemini's native SDK.

1.  Instead of crafting a large system prompt, we pass our tool schemas directly to a `GenerateContentConfig` object. This configuration bypasses the need for a custom system prompt because the tool definitions are passed directly in the API call. The provider then uses its own optimized, internal prompt to instruct the model.
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
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=USER_PROMPT,
        config=config,
    )
    ```

2.  The `google-genai` SDK simplifies this even further by accepting Python functions directly, automatically generating the schema from type hints and docstrings. This reduces dozens of lines of code to just a few.
    ```python
    config = types.GenerateContentConfig(
        tools=[search_google_drive, send_discord_message, summarize_financial_report]
    )
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=USER_PROMPT,
        config=config,
    )
    ```

3.  The returned `function_call` object contains the `name` of the tool to execute and its `args`.
    ```python
    function_call = response.candidates[0].content.parts[0].function_call
    ```
    It outputs:
    ```text
    FunctionCall(id=None, args={'query': 'Q3 earnings report'}, name='search_google_drive')
    ```
    ```python
    function_call.args
    ```
    It outputs:
    ```text
    {'query': 'Q3 earnings report'}
    ```

4.  We can then create a simplified `call_tool` function to execute it.
    ```python
    def call_tool(function_call) -> any:
        tool_name = function_call.name
        tool_args = {key: value for key, value in function_call.args.items()}
        tool_handler = TOOLS_BY_NAME[tool_name]
        return tool_handler(**tool_args)
    
    tool_result = call_tool(function_call)
    ```
    It outputs:
    ```text
    {'files': [{'name': 'Q3_Earnings_Report_2024.pdf', 'id': 'file12345', 'content': '...'}]}
    ```
    While object names and configuration parameters might differ slightly, the core logic of defining a schema, passing it to the model, receiving a structured call, and executing it is a consistent pattern across all major LLM providers like OpenAI and Anthropic [[16]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-4-interacting-with-llm-apis/overview-common-llm-apis), [[17]](https://myengineeringpath.dev/tools/gemini-guide/).

## Using Pydantic Models as Tools for On-Demand Structured Outputs

Connecting this lesson with what we learned about structured outputs in Lesson 4, we can treat a Pydantic model as a tool. This is a powerful pattern in agentic workflows where you perform several intermediate steps and then dynamically decide to generate a final, structured answer [[18]](https://discuss.ai.google.dev/t/response-schema-from-pydantic/50028).

This approach allows the agent to reason freely during intermediate steps and then "call" the Pydantic tool only when it's ready to produce a validated, machine-readable output for downstream systems.

```mermaid
flowchart LR
    start["Start"] --> agent["AI Agent"]
    agent -- "Initiates Task" --> loop_entry{"Loop: Evaluate & Call Tool"}

    subgraph "Tool Execution Cycle"
        loop_entry --> tool_call["Generic Tool Call"]
        tool_call -- "Tool Result" --> loop_entry
    end

    loop_entry -- "No More Tools / Final Step" --> final_tool["Structured Output Tool<br/>(Pydantic Model)"]
    final_tool -- "Structured Output" --> agent_output["Agent Final Output"]
    agent_output --> end_node["End"]
```
Image 2: A flowchart illustrating an AI agent that calls multiple tools in a loop, with the final tool call being for structured outputs using a Pydantic model.

1.  We define our `DocumentMetadata` Pydantic model and create a tool declaration from its JSON schema.
    ```python
    class DocumentMetadata(BaseModel):
        """A class to hold structured metadata for a document."""
    
        summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
        tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
        keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
        quarter: str = Field(description="The quarter of the financial year described in the document (e.g., Q3 2023).")
        growth_rate: str = Field(description="The growth rate of the company described in the document (e.g., 10%).")
    
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

2.  When we prompt the model to analyze a document, it will now generate a call to our `extract_metadata` tool.
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
    document_metadata = DocumentMetadata(**function_call.args)
    ```
    The arguments from the function call are then used to instantiate a validated `DocumentMetadata` object, bridging the gap between the LLM's output and our application's data model.

## The Downsides of Running Tools in a Loop

So far, we have focused on single tool calls. A natural progression is to run tools in a loop, allowing an agent to chain multiple actions together. At each step, the LLM can decide which tool to use based on the output of previous tools. This is the final piece we need to build a real AI agent.

```mermaid
flowchart LR
  A["User Prompt"]
  B["Tool Call"]
  C["Tool Result"]

  A -- "initiates" --> B
  B -- "returns" --> C
  C -- "triggers next" --> B
```
Image 3: A flowchart illustrating a sequential tool calling loop.

Let's implement a loop where the agent first searches for a report, then summarizes it, and finally sends the summary to Discord.

1.  We set up a loop that continues as long as the model requests a tool call.
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
    
    max_iterations = 3
    while hasattr(response_message_part, "function_call") and max_iterations > 0:
        pretty_print.function_call(response_message_part.function_call, title="Function Call")
        tool_result = call_tool(response_message_part.function_call)
        pretty_print.wrapped(tool_result, title="Tool Result", indent=2)
    
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
    This loop enables the agent to handle a multi-step task by sequentially calling `search_google_drive`, `summarize_financial_report`, and `send_discord_message`.

2.  However, this simple loop is limited. The agent acts without interpreting each tool's output, moving to the next call without pausing to think. This can lead to inefficient tool usage or getting stuck in loops [[19]](https://myengineeringpath.dev/genai-engineer/agentic-patterns/), [[20]](https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems).

3.  When tools are independent, they can be run in parallel to reduce latency. With sequential calls, total latency is the sum of all individual call times. In parallel, it's only the duration of the slowest call [[31]](https://www.codeant.ai/blogs/parallel-tool-calling). For instance, an agent could fetch financial news and stock prices simultaneously.

These limitations—especially the lack of intermediate reasoning—pushed the industry to develop more sophisticated patterns. The most foundational of these is **ReAct** (Reasoning and Acting), which we will explore in detail in Lessons 7 and 8.

## Popular Tools Used Within the Industry

To ground these concepts in the real world, here are some popular categories of tools used in production AI systems:

1.  **Knowledge & Memory Access:** These tools connect agents to external knowledge. Examples include querying vector databases for Retrieval-Augmented Generation (RAG), or using text-to-SQL to interact with traditional databases like PostgreSQL [[3]](https://promethium.ai/guides/text-to-sql-basics-benefits/), [[4]](https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/). We will cover memory and RAG in Lessons 9 and 10.
2.  **Web Search & Browsing:** These are common in research agents and chatbots. Tools can interface with search engine APIs (Google, Bing) or scrape content directly from web pages [[21]](https://mantraideas.com/llm-web-search/).
3.  **Code Execution:** A Python interpreter tool allows an agent to run code, which is invaluable for calculations and data manipulation. However, this introduces security risks, so it is essential to execute the code in a sandboxed environment to prevent malicious actions [[2]](https://arxiv.org/html/2507.08034v1).
4.  **External APIs:** Many enterprise applications use tools to interact with external services like calendars, email clients, and project management software, enabling agents to perform actions like scheduling meetings or creating tasks [[22]](https://medium.com/@yugalnandurkar5/llm-engineering-part-i-fa48d4307d26).

## Conclusion

Tool calling is a foundational skill in AI engineering, transforming LLMs into agents that can act. Mastering it is essential for building, monitoring, and debugging AI applications. In our next lesson, we will build on this foundation to explore planning and reasoning with the ReAct pattern.

## References

- [1] https://www.youtube.com/watch?v=h8gMhXYAv1k
- [2] https://arxiv.org/html/2507.08034v1
- [3] https://promethium.ai/guides/text-to-sql-basics-benefits/
- [4] https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/
- [5] https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f
- [6] https://www.philschmid.de/gemini-function-calling
- [7] https://platform.openai.com/docs/guides/function-calling
- [8] https://ai.google.dev/gemini-api/docs/function-calling
- [9] https://www.anthropic.com/research/building-effective-agents
- [10] https://pub.towardsai.net/tool-descriptions-are-critical-making-better-llm-tools-research-capability-b315851471e7
- [11] https://arxiv.org/pdf/2401.17464v3
- [12] https://openai.github.io/openai-agents-python/tools/
- [13] https://pydantic.dev/docs/ai/tools-toolsets/tools/
- [14] https://docs.langchain.com/oss/python/langchain/tools
- [15] https://www.newsletter.swirlai.com/p/building-ai-agents-from-scratch-part
- [16] https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-4-interacting-with-llm-apis/overview-common-llm-apis
- [17] https://myengineeringpath.dev/tools/gemini-guide/
- [18] https://discuss.ai.google.dev/t/response-schema-from-pydantic/50028
- [19] https://myengineeringpath.dev/genai-engineer/agentic-patterns/
- [20] https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems
- [21] https://mantraideas.com/llm-web-search/
- [22] https://medium.com/@yugalnandurkar5/llm-engineering-part-i-fa48d4307d26
- [23] https://fireworks.ai/blog/function-calling
- [24] https://www.digital-alpha.com/a-deep-dive-into-function-calling-with-llms/
- [25] https://medium.com/@zhihao.zhou.bupt/the-smart-principles-designing-interfaces-that-llms-understand-aca00630c8c9
- [26] https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-1-llm-agent-tooling-foundations/designing-tool-interfaces
- [27] https://arxiv.org/html/2509.21199v3
- [28] https://aclanthology.org/2025.findings-acl.811.pdf
- [29] https://supergok.com/open-responses-llm-interoperability/
- [30] https://arxiv.org/html/2604.09360v1
- [31] https://www.codeant.ai/blogs/parallel-tool-calling
- [32] https://garymarcus.substack.com/p/the-biggest-advance-in-ai-since-the
- [33] https://www.youtube.com/watch?v=ApoDzZP8_ck
- [34] https://pydantic.dev/docs/ai/tools-toolsets/tools/
- [35] https://medium.com/@abhaychougule0907/underlying-factors-behind-inconsistency-in-llm-responses-with-multi-tool-calling-628ce7b4de76
- [36] https://arxiv.org/html/2505.18135v2
- [37] https://www.getorchestra.io/guides/llm-providers-gen-ai-platforms-compared
- [38] https://futuresearch.ai/blog/llm-provider-quirks/
- [39] https://pydantic.dev/docs/ai/core-concepts/output/
- [40] https://pydantic.dev/docs/ai/guides/multi-agent-applications/
- [41] https://www.ruh.ai/blogs/how-vector-databases-are-rewiring-the-tech-industry
- [42] https://www.instaclustr.com/education/vector-database/top-10-open-source-vector-databases/
- [43] https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf
- [44] https://community.openai.com/t/prompting-best-practices-for-tool-use-function-calling/1123036
- [45] https://medium.com/@hariomshahu101/building-production-ready-llm-applications-bulletproof-llm-tool-calling-with-advanced-json-b95ce8889f4e
- [46] https://tetrate.io/learn/ai/llm-output-parsing-structured-generation
- [47] https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-1-llm-agent-tooling-foundations/tool-input-output-schemas
- [48] https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools
- [49] https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/
- [50] https://reference.langchain.com/python/langchain-core/tools/convert/tool
- [51] https://composio.dev/blog/how-to-build-tools-for-ai-agents-a-field-guide
- [52] https://techinfotech.tech.blog/2025/06/09/best-practices-to-build-llm-tools-in-2025/
- [53] https://glaforge.dev/posts/2023/12/22/gemini-function-calling/