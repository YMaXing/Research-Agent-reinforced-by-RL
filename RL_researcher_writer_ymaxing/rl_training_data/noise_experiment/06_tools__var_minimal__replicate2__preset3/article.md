# Agent Tools & Function Calling: Giving Your LLM the Ability to Take Action

In previous lessons, we learned to manage the information we feed into and get out of LLMs. Now, we will explore a critical building block of any AI agent: tools. Also known as function calling, tools transform an LLM from a text generator into an agent that can act. Understanding how this works is essential for building modern AI applications.

## Understanding Why Agents Need Tools

LLMs have a fundamental limitation: they are powerful pattern matchers and text generators, but they cannot interact with the external world on their own. They need some additional engineering around them to perform actions. This limitation is addressed by tools. Think of the LLM as the brain, while tools are its "hands and senses," allowing it to perceive and act in the world beyond its training data [[1]](https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f).

Tools are the bridge between the LLM's internal reasoning and the external world. With them, an LLM becomes an AI agent that can execute specific instructions. Popular tools allow agents to access real-time information through APIs, interact with storage solutions like a PostgreSQL database or an S3 data lake, access long-term memory, execute code, and perform precise calculations beyond their training data [[2]](https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf), [[3]](https://arxiv.org/html/2507.08034v1).

## Implementing Tool Calls from Scratch

The best way to understand how tools work is to implement them from scratch. Our goal is to provide the LLM with a list of available tools and let it decide which one to use and with what arguments.

The high-level process involves five steps:
1.  **App:** Provide a list of available tools to the LLM within the system prompt.
2.  **LLM:** Respond with a `function_call` request, specifying the tool and its arguments.
3.  **App:** Execute the requested function in your code.
4.  **App:** Send the function's output back to the LLM.
5.  **LLM:** Use the output to generate a final, user-facing response.

```mermaid
flowchart LR
  %% External User
  User_Start["User"]

  %% System Components
  subgraph "Core System"
    App["App<br/>(Tool Orchestrator)"]
    LLM["LLM"]
  end

  %% Available Tools
  subgraph "Tool Implementations"
    Tool_Search["search_google_drive"]
    Tool_Discord["send_discord_message"]
    Tool_Report["summarize_financial_report"]
  end

  %% Flow Steps
  User_Start -- "Initial Request" --> App

  App -- "1. Provides tool list in system prompt" --> LLM
  LLM -- "2. Responds with function_call request<br/>(specifying tool & arguments)" --> App

  App -- "3. Executes requested function" --> Tool_Search
  App -- "3. Executes requested function" --> Tool_Discord
  App -- "3. Executes requested function" --> Tool_Report

  Tool_Search -- "Function Output" --> App
  Tool_Discord -- "Function Output" --> App
  Tool_Report -- "Function Output" --> App

  App -- "4. Sends function's output back" --> LLM
  LLM -- "5. Generates user-facing response" --> User_End["User"]

  %% Visual Grouping
  classDef main_actor stroke-width:2px
  classDef tool_impl stroke-dasharray:3,3
  class App,LLM main_actor
  class Tool_Search,Tool_Discord,Tool_Report tool_impl
```
Image 1: Flowchart illustrating the 5-step request-execute-respond flow of calling a tool.

Let's implement a simple example where we mock searching for a document on Google Drive and sending its summary to Discord. In this flow, the application layer is responsible for more than just execution; it can enforce reliability through validation, security checks, or even incorporating a human feedback step before committing to an action [[4]](https://www.zimuel.it/blog/tool_calling_AI_agents).

<aside>
💡

You can find the code for this lesson in the accompanying [GitHub repository](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/06_tools/notebook.ipynb).

</aside>

1.  We begin by setting up our environment and defining three mocked tools.
    ```python
    import json
    from typing import Any
    from google import genai
    from google.genai import types
    from pydantic import BaseModel, Field
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    client = genai.Client()
    MODEL_ID = "gemini-2.5-flash"
    
    DOCUMENT = """
    # Q3 2023 Financial Performance Analysis
    ...
    """
    
    def search_google_drive(query: str) -> dict:
        """
        Searches for a file on Google Drive and returns its content or a summary.
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
    
    def send_discord_message(channel_id: str, message: str) -> dict:
        """
        Sends a message to a specific Discord channel.
        """
        return {
            "status": "success",
            "channel": channel_id,
        }
    
    def summarize_financial_report(text: str) -> str:
        """
        Summarizes a financial report.
        """
        return "The Q3 2023 earnings report shows strong performance..."
    ```
2.  For each tool, we create a JSON schema describing its purpose and parameters. This format is an industry standard for defining tools for LLMs [[5]](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation), [[6]](https://is4.ai/blog/our-blog-1/openai-api-vs-anthropic-api-comparison-117).
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
    # Other schemas omitted for brevity
    ```
3.  We create a tool registry to map names to handlers and aggregate the schemas.
    ```python
    TOOLS = {
        "search_google_drive": {"handler": search_google_drive, "declaration": search_google_drive_schema},
        "send_discord_message": {"handler": send_discord_message, "declaration": send_discord_message_schema},
        "summarize_financial_report": {"handler": summarize_financial_report, "declaration": summarize_financial_report_schema},
    }
    TOOLS_BY_NAME = {tool_name: tool["handler"] for tool_name, tool in TOOLS.items()}
    TOOLS_SCHEMA = [tool["declaration"] for tool in TOOLS.values()]
    ```
4.  We define a system prompt that instructs the LLM on how to use the tools. Based on the `description` field, the LLM decides if a tool is appropriate. Clear and distinct tool descriptions are therefore critical, especially when an agent has access to dozens of tools [[7]](https://www.anthropic.com/research/building-effective-agents), [[8]](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools). For example, `search documents on Google Drive` is much better than a generic `search files`. The LLM is specially tuned through instruction fine-tuning to interpret these schemas and generate the correct tool calls.
    ```python
    TOOL_CALLING_SYSTEM_PROMPT = """
    You are a helpful AI assistant with access to tools...
    
    ## Available Tools
    <tool_definitions>
    {tools}
    </tool_definitions>
    ...
    """
    ```
5.  Let's test it with two different user prompts.
    ```python
    USER_PROMPT_1 = "Can you help me find the latest quarterly report and share key insights with the team?"
    messages_1 = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT_1]
    response_1 = client.models.generate_content(model=MODEL_ID, contents=messages_1)
    
    USER_PROMPT_2 = "Please find the Q3 earnings report on Google Drive and send a summary of it to the #finance channel on Discord."
    messages_2 = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT_2]
    response_2 = client.models.generate_content(model=MODEL_ID, contents=messages_2)
    ```
    The LLM correctly identifies the `search_google_drive` tool for both prompts:
    ```text
    ```tool_call
    {"name": "search_google_drive", "args": {"query": "latest quarterly report"}}
    ```
    ```
6.  We then parse the LLM's response, execute the tool, and get the result.
    ```python
    def extract_tool_call(response_text: str) -> str:
        return response_text.split("```tool_call")[1].split("```")[0].strip()
    
    def call_tool(response_text: str, tools_by_name: dict) -> Any:
        tool_call_str = extract_tool_call(response_text)
        tool_call = json.loads(tool_call_str)
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool = tools_by_name[tool_name]
        return tool(**tool_args)
    
    tool_result = call_tool(response_2.text, tools_by_name=TOOLS_BY_NAME)
    ```
7.  The final step is to send the tool's result back to the LLM, allowing it to formulate a final response or decide on the next action.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=f"Interpret the tool result: {json.dumps(tool_result, indent=2)}",
    )
    ```
    The LLM interprets the result and provides a user-friendly summary. This covers the basic concept of tool calling.

## Implementing a Tool Calling Framework from Scratch

Manually defining JSON schemas for every tool is cumbersome and violates the Don't Repeat Yourself (DRY) principle. Modern agent frameworks like LangGraph solve this with a `@tool` decorator that automatically generates a schema from a function's signature and docstring [[9]](https://openai.github.io/openai-agents-python/tools/), [[10]](https://docs.langchain.com/oss/python/langchain/tools). This approach creates a single source of truth for tool definitions and ensures compatibility with function-calling APIs [[11]](https://towardsai.net/p/machine-learning/how-tools-turn-into-agents-what-actually-happens-at-runtime).

Let's build our own simple framework to see how this works.

1.  First, we define a `ToolFunction` class to wrap our decorated functions and store their schemas. The `@tool` decorator uses Python's `inspect` module to get the function signature and docstring, which it then uses to build the schema.
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
    
    def tool(description: Optional[str] = None) -> Callable[[Callable], ToolFunction]:
        def decorator(func: Callable) -> ToolFunction:
            sig = signature(func)
            properties = {}
            required = []
            for param_name, param in sig.parameters.items():
                if param_name == "self":
                    continue
                param_schema = {"type": "string", "description": f"The {param_name} parameter"}
                if param.default == Parameter.empty:
                    required.append(param_name)
                properties[param_name] = param_schema
            schema = {
                "name": func.__name__,
                "description": description or func.__doc__ or f"Executes the {func.__name__} function.",
                "parameters": {"type": "object", "properties": properties, "required": required},
            }
            return ToolFunction(func, schema)
        return decorator
    ```
2.  Now, we can redefine our tools using the new decorator.
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
    
    tools = [search_google_drive_example, send_discord_message_example, summarize_financial_report_example]
    tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
    tools_schema = [tool.schema for tool in tools]
    ```
3.  The decorated function is now a `ToolFunction` object containing the auto-generated schema and a reference to the original handler. We can inspect it to see the generated schema.
    ```python
    print(json.dumps(search_google_drive_example.schema, indent=2))
    ```
    It outputs:
    ```json
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
4.  We can use this schema just as we did before.
    ```python
    USER_PROMPT = "Please find the Q3 earnings report on Google Drive and send a summary of it to the #finance channel on Discord."
    messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(tools_schema)), USER_PROMPT]
    response = client.models.generate_content(model=MODEL_ID, contents=messages)
    ```
    The model responds with the expected tool call, which we can execute. Voilà! We have our little tool-calling framework.

## Implementing Production-Level Tool Calls with Gemini

In production, we use native API interfaces from Gemini or OpenAI. They handle the prompt engineering, making code more robust and maintainable [[12]](https://www.decodingai.com/p/tool-calling-from-scratch-to-production).

Let's see how to use Gemini's native tool-calling capabilities.

1.  Instead of crafting a system prompt, we define a `GenerateContentConfig` object and pass our tool schemas directly to it.
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
2.  We can now call the model with just the user prompt, as the `config` object handles the tool instructions.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=USER_PROMPT,
        config=config,
    )
    ```
3.  To simplify even further, the `google-genai` SDK can automatically generate schemas from Python functions. We can pass our functions directly to the `GenerateContentConfig`, eliminating manual schema definitions entirely.
    ```python
    config = types.GenerateContentConfig(
        tools=[search_google_drive, send_discord_message]
    )
    ```
4.  We create a simplified `call_tool` function to execute the `FunctionCall` object returned by Gemini.
    ```python
    def call_tool(function_call) -> Any:
        tool_name = function_call.name
        tool_args = {key: value for key, value in function_call.args.items()}
        tool_handler = TOOLS_BY_NAME[tool_name]
        return tool_handler(**tool_args)
    
    tool_result = call_tool(response.candidates[0].content.parts[0].function_call)
    ```
By using the native SDK, we reduced dozens of lines of code to just a few. Other APIs from OpenAI and Anthropic follow a similar logic, making these concepts transferable [[13]](https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-4-interacting-with-llm-apis/overview-common-llm-apis), [[14]](https://myengineeringpath.dev/tools/gemini-guide/).

## Using Pydantic Models as Tools for On-Demand Structured Outputs

Connecting this lesson with what we learned about structured outputs in Lesson 4, we can treat a Pydantic model as a tool. This is an elegant pattern for agentic workflows where an agent performs several intermediate steps before dynamically deciding to return a final, validated answer in a structured format. This ensures the output has a predictable schema for downstream use [[15]](https://pydantic.dev/docs/ai/core-concepts/output/).

Image 2 illustrates an agent that calls multiple tools in a loop, with the final call dedicated to generating a structured output via a Pydantic model.

```mermaid
flowchart LR
    %% AI Agent Initialization
    A["AI Agent"]

    %% Iterative Tool Calling Loop
    subgraph "Iterative Tool Calls"
        direction LR
        TCI["Tool Call (Iterative)"]
        PTO["Process Tool Output"]
        MTN{"More Tools Needed?"}
    end

    %% Final Structured Output
    FSO["Structured Output Tool Call"]
    PMO["Pydantic Model Output"]
    AFR["Agent Final Response"]

    A -- "starts process" --> TCI
    TCI -- "returns raw output" --> PTO
    PTO -- "evaluates & decides" --> MTN
    MTN -- "Yes (continue)" --> TCI
    MTN -- "No (final step)" --> FSO
    FSO -- "generates structured data" --> PMO
    PMO -- "provides" --> AFR

    %% Visual Grouping
    classDef agentNode stroke-width:2px
    classDef toolCallNode stroke-dasharray:3,3
    classDef finalOutputNode stroke-width:2px,font-weight:bold

    class A agentNode
    class TCI, FSO toolCallNode
    class PMO, AFR finalOutputNode
```
Image 2: A Mermaid diagram illustrating an AI agent that calls multiple tools in a loop, with the last tool call being for structured outputs using a Pydantic model.

1.  We define a `DocumentMetadata` Pydantic model.
    ```python
    class DocumentMetadata(BaseModel):
        """A class to hold structured metadata for a document."""
        summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
        tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
        keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
        quarter: str = Field(description="The quarter of the financial year described in the document (e.g., Q3 2023).")
        growth_rate: str = Field(description="The growth rate of the company described in the document (e.g., 10%).")
    ```
2.  We create an `extraction_tool` by passing the Pydantic model's JSON schema as the function's parameters.
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
3.  After prompting the model, it returns a `function_call` with the extracted data as arguments. We then validate this data by instantiating our `DocumentMetadata` model.
    ```python
    function_call = response.candidates[0].content.parts[0].function_call
    document_metadata = DocumentMetadata(**function_call.args)
    ```

## The Downsides of Running Tools in a Loop

Until now, we have focused on single-turn tool calls. As a natural progression, we want to build more sophisticated agents that can run tools in a loop. This allows the LLM to chain multiple actions, deciding the next step based on the output of previous tools. This is the final piece needed to build a real AI agent, offering the flexibility to handle complex, multi-step tasks.

```mermaid
flowchart LR
    User["User Prompt"] --> Call["Tool Call"]
    Call --> Result["Tool Result"]
    Result -- "Repeat if needed" --> Call
```
Image 3: A Mermaid diagram illustrating a sequential tool calling loop.

Let's see how this works in code.

1.  We configure the model with all available tools and define the user's multi-step request.
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
    
    USER_PROMPT = "Please find the Q3 earnings report on Google Drive and send a summary of it to the #finance channel on Discord."
    messages = [USER_PROMPT]
    ```
2.  We implement a loop that continues as long as the model requests a function call.
    ```python
    response = client.models.generate_content(model=MODEL_ID, contents=messages, config=config)
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
        response = client.models.generate_content(model=MODEL_ID, contents=messages, config=config)
        response_message_part = response.candidates[0].content.parts[0]
        messages.append(response.candidates[0].content)
        max_iterations -= 1
    ```
The agent successfully completes the task by calling `search_google_drive`, `summarize_financial_report`, and `send_discord_message`. However, this simple sequential loop has significant drawbacks. It doesn't allow the LLM to interpret a tool's output before deciding on the next action, forcing it to act without thinking [[16]](https://myengineeringpath.dev/genai-engineer/agentic-patterns/), [[17]](https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems). This can lead to inefficient paths or getting stuck. The loop also misses a key optimization: parallelism. When tool calls are independent, they can be executed simultaneously to reduce latency [[18]](https://airbyte.com/agentic-data/parallel-tool-calls-llm). These limitations motivated the development of more advanced patterns like **ReAct** (Reasoning and Acting), which explicitly interleaves reasoning steps with tool calls. We will explore ReAct in detail in Lessons 7 and 8.

## Popular Tools Used Within the Industry

To ground this lesson in real-world applications, here are some of the most popular tool categories used by AI engineers today.

**Knowledge and Memory Access** tools query data stores like vector databases to retrieve context. This includes text-to-SQL tools that interact with classic databases, a pattern related to the memory and RAG techniques we will cover in Lessons 9 and 10 [[19]](https://promethium.ai/guides/text-to-sql-basics-benefits/).

**Web Search and Browsing** tools use search engine APIs and web scrapers to fetch online content, which is essential for research agents that need current information [[20]](https://mantraideas.com/llm-web-search/).

**Code Execution** tools, like a Python interpreter, allow agents to perform calculations, data manipulation, and analysis in a sandboxed environment [[3]](https://arxiv.org/html/2507.08034v1).

Other popular tools include integrations with **external APIs** for calendars or email and **file system operations** for productivity apps. The rise of agents is also reshaping API design to better support these interactions [[21]](https://www.gravitee.io/blog/designing-apis-for-llm-apps).

## Conclusion

Tool calling is a core concept in AI engineering that gives LLMs the ability to act. We have seen how to implement it from scratch and chain tools for multi-step tasks. These foundations lead to more advanced patterns, which we will explore in our next lesson on planning and the ReAct framework.

## References

- [1] https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f
- [2] https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf
- [3] https://arxiv.org/html/2507.08034v1
- [4] https://www.zimuel.it/blog/tool_calling_AI_agents
- [5] https://tetrate.io/learn/ai/llm-output-parsing-structured-generation
- [6] https://is4.ai/blog/our-blog-1/openai-api-vs-anthropic-api-comparison-117
- [7] https://www.anthropic.com/research/building-effective-agents
- [8] https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools
- [9] https://openai.github.io/openai-agents-python/tools/
- [10] https://docs.langchain.com/oss/python/langchain/tools
- [11] https://towardsai.net/p/machine-learning/how-tools-turn-into-agents-what-actually-happens-at-runtime
- [12] https://www.decodingai.com/p/tool-calling-from-scratch-to-production
- [13] https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-4-interacting-with-llm-apis/overview-common-llm-apis
- [14] https://myengineeringpath.dev/tools/gemini-guide/
- [15] https://pydantic.dev/docs/ai/core-concepts/output/
- [16] https://myengineeringpath.dev/genai-engineer/agentic-patterns/
- [17] https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems
- [18] https://airbyte.com/agentic-data/parallel-tool-calls-llm
- [19] https://promethium.ai/guides/text-to-sql-basics-benefits/
- [20] https://mantraideas.com/llm-web-search/
- [21] https://www.gravitee.io/blog/designing-apis-for-llm-apps
</article>