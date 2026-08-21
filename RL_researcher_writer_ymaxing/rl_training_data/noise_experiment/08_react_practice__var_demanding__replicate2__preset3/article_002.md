# Building a ReAct Agent From Scratch: A Step-by-Step Guide

In our last lesson, we covered the theory behind AI agent planning, focusing on frameworks like ReAct. Now, it’s time to get our hands dirty. This lesson is 100% practice. We are going to build a minimal ReAct agent from scratch, end-to-end, using only Python and the Gemini API.

The original ReAct paper showed that by grounding reasoning with actions, agents could overcome the hallucination and error propagation issues common in pure Chain-of-Thought models. Interacting with external tools provides this grounding.[[1]](https://arxiv.org/pdf/2210.03629) This synergy between reasoning and acting is the foundation of modern agentic AI.

When we first started building agents, we jumped straight into frameworks like LangGraph. We thought their graph-based models would make everything cleaner. Instead, we found ourselves fighting the framework. Simple `if-else` logic and basic loops became hours of work, forcing our code into an unnatural graph paradigm that added complexity without much value.

Frustrated, we did what we always do when we are stuck: we opened the source code. Reading LangGraph’s implementation of the ReAct loop was a lightbulb moment. It gave us a concrete mental model that the documentation never could. This pattern is not unique; it forms the basis for many emerging AI frameworks, including AutoGPT.[[10]](https://www.techtarget.com/searchenterpriseai/tip/How-ReAct-agents-can-transform-the-enterprise) Even though we would not use the framework in production, understanding its internals became the foundation for building our own robust agents.

By building the complete Thought → Action → Observation cycle yourself, you gain the confidence to extend, debug, and customize agents.

In this lesson, we will walk you through implementing:
*   A stable development environment.
*   A mock tool layer for predictable interactions.
*   The thought phase, where the agent plans its next move.
*   The action phase, powered by Gemini’s function calling.
*   A turn-based control loop to orchestrate the entire process.
*   Tests to validate success and graceful fallback behaviors.

Let's get started.

## Setup and Environment

Before we can build our agent, we need to set up a clean and predictable environment. This ensures your code runs smoothly and the outputs match the traces we will analyze later. This section follows the initial setup from the course notebook.

1.  First, we load our environment variables. We use a custom utility, `lessons.utils.env.load()`, to manage API keys. This modular approach keeps secrets out of our code and makes the project easier to configure. The design rationale behind such utilities is to promote reusability and maintain a clean separation of concerns, a core principle in any production-grade software project. A well-organized environment setup is the first step toward building reproducible and maintainable AI systems, saving you from debugging headaches down the line.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```

2.  Next, we import the necessary libraries. We will use `google-genai` for interacting with the Gemini API, `pydantic` for data validation, and Python's `enum` and `typing` for creating structured and type-safe code. We also import a `pretty_print` utility to make our agent's traces easier to read.
    ```python
    import json
    from enum import Enum
    from typing import Callable, Union
    
    from google import genai
    from pydantic import BaseModel, Field
    
    from lessons.utils.pretty_print import pretty_print_conversation
    ```
    Using `pydantic` is a best practice for agent development. It allows us to define data schemas as Python classes, providing runtime validation that prevents malformed data from crashing our application. For example, if an LLM returns a string where an integer is expected, Pydantic raises a `ValidationError`, allowing for immediate and clear error handling. This is far more robust than using standard Python dictionaries, which offer no such guarantees. This "fail-fast" behavior is essential for building reliable systems.

    Similarly, `Enum` is invaluable for defining a fixed set of states or roles, such as the different types of messages in our agent's scratchpad (`USER`, `THOUGHT`, `OBSERVATION`). This makes the agent's internal state explicit and easier to debug, preventing errors from typos and ensuring that message roles are always one of the expected values. These small but powerful constructs bring engineering discipline to the probabilistic world of LLMs.

3.  We initialize the Gemini client. If you have both `GOOGLE_API_KEY` and `GEMINI_API_KEY` set, the library will default to one, and you might see a warning, which is safe to ignore.
    ```python
    client = genai.Client()
    ```

4.  Finally, we define the model we will use. For this lesson, `gemini-2.5-flash` is a great choice. It is fast, cost-effective, and powerful enough for the reasoning tasks our agent will perform.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model configured, our environment is ready. The next step is to give our agent a capability—an external tool it can use to interact with the world.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to use tools. For this lesson, we will create a mock search tool instead of calling a real API. This approach has several educational benefits: it simplifies our focus to the core ReAct mechanics, removes the need for external API keys, and provides predictable responses, which is essential for testing and debugging.

The ReAct framework was born from the insight that interleaving reasoning with tool use grounds the model in reality, overcoming the "hallucination and error propagation" common in pure reasoning systems.[[1]](https://arxiv.org/pdf/2210.03629) Our mock tool simulates this grounding process.

Our mock search function will simulate a web search. It takes a query and returns a hardcoded response if the query matches a few predefined topics. If the query is unknown, it returns a "not found" message. This simulates how a real tool might behave.

1.  First, we define the mock search function. The docstring is important here; as we will see later, LLMs use the docstring to understand what a tool does and how to use it.
    ```python
    def search(query: str) -> str:
        """
        A mock search tool that returns predefined results for specific queries.
        This tool is for educational purposes to demonstrate tool integration.
        """
        print(f"Searching for: {query}")
        if "capital of france" in query.lower():
            return "Paris is the capital of France and is known for the Eiffel Tower."
        elif "python programming" in query.lower():
            return "Python is a high-level, interpreted programming language known for its simple syntax."
        else:
            return f"Information about '{query}' was not found."
    ```
    The quality of your tool definitions is as important as the quality of your prompts. Anthropic refers to this as designing the Agent-Computer Interface (ACI). A good tool definition includes clear parameter names, a descriptive docstring with examples, and well-defined boundaries to prevent confusion with other tools. For example, a file system tool that requires absolute paths instead of relative ones makes it harder for the agent to make mistakes.[[11]](https://www.anthropic.com/engineering/building-effective-agents)

2.  Next, we create a `TOOL_REGISTRY` to store our tool. This registry maps the tool's name to its handler function, which allows our agent to dynamically call the correct function based on the LLM's output.
    ```python
    TOOL_REGISTRY = {
        "search": search,
    }
    ```

In a production system, you would replace this mock `search` function with a call to a real external API, like the Google Search API. This involves several considerations. First, you would need to manage API keys securely, typically using environment variables or a secrets management service. Second, you must handle network requests, which can fail or time out. A robust implementation would include retry logic, possibly with exponential backoff, to handle transient network issues. Third, you need to parse the API's response format and handle potential errors, such as a 429 (Too Many Requests) status code, which indicates you have hit a rate limit.

For example, a production-ready search tool might look like this:
```python
import requests
import os
import time

def google_search(query: str, retries: int = 3, delay: int = 2) -> str:
    """
    Performs a Google search using the SERP API and returns the top results.
    Handles network errors with exponential backoff.
    """
    api_key = os.getenv("SERP_API_KEY")
    if not api_key:
        return "Error: SERP_API_KEY not found in environment variables."

    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": api_key}

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            # Raise an HTTPError for bad responses (4xx or 5xx)
            response.raise_for_status()
            data = response.json()
            
            if "organic_results" in data and data["organic_results"]:
                # Extract and format snippets from the top 3 results
                snippets = [
                    f"Title: {res.get('title', 'N/A')}\nSnippet: {res.get('snippet', 'N/A')}"
                    for res in data["organic_results"][:3]
                ]
                return "\n---\n".join(snippets)
            elif "answer_box" in data:
                return data["answer_box"].get("snippet") or data["answer_box"].get("answer", "No direct answer found.")
            else:
                return "No organic results found for the query."
                
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                # Exponential backoff: wait longer after each failed attempt
                time.sleep(delay * (2 ** attempt))
                print(f"Request failed. Retrying in {delay * (2 ** attempt)} seconds...")
                continue
            else:
                # Return a detailed error message after the final retry
                return f"Error performing search after {retries} attempts: {e}"
```
This example demonstrates a more resilient approach suitable for production. It includes clear error messages, handles missing API keys, retries on failure with increasing delays, and parses a more complex JSON response. For learning the ReAct loop, however, our simple mock tool is sufficient and keeps the focus on the agent's logic.

With a tool defined, the agent now needs a way to *think* about when and how to use it. This brings us to the first phase of the ReAct cycle: the Thought phase.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is where the agent reasons about the user's query and its history to form a plan. This process is a form of task decomposition, where the agent breaks a high-level goal into smaller, executable steps.[[12]](https://www.ibm.com/think/topics/ai-agent-planning) This plan is a natural language string that outlines the next step, such as deciding to use a tool or formulate a final answer. We generate this thought by prompting an LLM with the current context.

This explicit reasoning step is a hallmark of the ReAct pattern. It makes the agent's decision-making process transparent and interpretable. By externalizing its thought process, the agent can track its progress, handle exceptions, and update its plan based on new information. This contrasts with simpler models that might jump directly to an action, which can be less robust for complex, multi-step tasks. The thought provides a "scratchpad" for the model to structure its reasoning before committing to an action.

This approach is more than just a debugging aid; it fundamentally improves the agent's performance. The reasoning traces help the model induce, track, and update action plans, and even handle exceptions, while the actions allow it to gather new information from external sources.[[1]](https://arxiv.org/pdf/2210.03629)

1.  First, we need a way to describe our available tools to the LLM. We will create a helper function that generates an XML description from our `TOOL_REGISTRY`. XML tags are a common prompt engineering technique that helps the model distinguish between different parts of the prompt, improving its ability to follow instructions.[[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies) This structured format makes it clear to the model what its capabilities are.
    ```python
    def build_tools_xml_description(tool_registry: dict[str, Callable]) -> str:
        """
        Builds an XML string describing the available tools.
        """
        xml = "<tools>\n"
        for name, func in tool_registry.items():
            xml += f'<tool name="{name}">\n'
            xml += f"<description>{func.__doc__}</description>\n"
            xml += "</tool>\n"
        xml += "</tools>"
        return xml
    
    
    tools_xml_description = build_tools_xml_description(TOOL_REGISTRY)
    ```

2.  Next, we define the prompt template for generating a thought. This template provides the model with the available tools and the conversation history, and instructs it to think step-by-step. The structure of this prompt is critical. It sets the context, defines the agent's capabilities through the tool descriptions, and constrains the task by asking for a single, focused thought.
    ```python
    PROMPT_TEMPLATE_THOUGHT = """
    You are an AI assistant that can use tools to answer questions.
    
    <tools>
    {tools_xml_description}
    </tools>
    
    The conversation history is provided below.
    <conversation>
    {conversation}
    </conversation>
    
    Based on the conversation, what is your next thought?
    """
    ```
    When we print this template, we can see how the tool's docstring is embedded directly into the prompt, giving the LLM the context it needs to decide when to use the `search` tool.
    ```text
    You are an AI assistant that can use tools to answer questions.
    
    <tools>
    <tool name="search">
    <description>
            A mock search tool that returns predefined results for specific queries.
            This tool is for educational purposes to demonstrate tool integration.
            </description>
    </tool>
    </tools>
    
    The conversation history is provided below.
    <conversation>
    {conversation}
    </conversation>
    
    Based on the conversation, what is your next thought?
    ```

3.  Finally, we create a function to generate the thought. This function formats the prompt with the current conversation and tool registry, sends it to the Gemini model, and returns the model's text response.
    ```python
    def generate_thought(conversation: str, tool_registry: dict[str, Callable]) -> str:
        """
        Generates a thought based on the conversation history and available tools.
        """
        tools_xml_description = build_tools_xml_description(tool_registry)
        prompt = PROMPT_TEMPLATE_THOUGHT.format(
            tools_xml_description=tools_xml_description, conversation=conversation
        )
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    ```
    When calling the model, parameters like `temperature` control the randomness of the output. While a low temperature (e.g., 0.0) is often used for deterministic tasks, Gemini's documentation warns that for complex reasoning, lowering the temperature below the default of 1.0 can sometimes cause looping or degraded performance.[[13]](https://stevekinney.com/writing/prompt-engineering-frontier-llms) It's a model-specific nuance to be aware of during tuning.

A thought is just an internal plan. To make it useful, the agent must translate that plan into a concrete action, like calling a tool or providing a final answer to the user.

## Action Phase: Function Calling and Parsing

The "Action" phase determines the agent's next concrete step. Instead of parsing the thought, we will ask the LLM to decide on an action directly using Gemini’s native function calling capability. This is a more robust and reliable approach.

Early ReAct agents relied on parsing text to extract actions, which was often brittle. Modern agents use structured function calling, which is more reliable, efficient, and less prone to errors.[[14]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent) However, this introduces a trade-off. For predictable tasks, a direct function call might be faster, but for complex scenarios where the path is unknown, the full ReAct loop provides superior adaptability.[[15]](https://www.ibm.com/think/topics/react-agent)

The strategy is to create a high-level system prompt that guides the agent's decision-making. We do not need to include tool signatures in this prompt because Gemini handles that automatically. When we provide Python functions in the `tools` configuration, the API extracts their name, docstring (for the description), and parameter types from the function signature.[[6]](https://ai.google.dev/gemini-api/docs/function-calling) This separation keeps our prompts clean and focused on strategic guidance.

1.  First, we define a prompt template for the action phase. This prompt instructs the agent to analyze the conversation and decide whether to use a tool or provide a final answer. It is intentionally high-level, trusting the model's function-calling abilities to handle the specifics.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are an AI assistant that can use tools to answer questions.
    Analyze the conversation and determine the next action.
    If you have enough information, provide a final answer.
    Otherwise, select a tool to gather more information.
    
    <conversation>
    {conversation}
    </conversation>
    """

2.  We define constants for our actions. `ACTION_FINISH` is a special marker for when the agent decides it has the final answer. We also define a Pydantic model, `ToolCallRequest`, to structure the data for a tool call. This ensures that any tool call generated by the LLM is validated against a known schema.
    ```python
    ACTION_FINISH = "finish"
    
    
    class ToolCallRequest(BaseModel):
        name: str
        args: dict
    
    
    Action = Union[ToolCallRequest, str]
    ```

3.  Next, we implement the `generate_action` function. This function takes the conversation and tool registry, configures the Gemini client with the available tools, and calls the model.
    ```python
    def generate_action(conversation: str, tool_registry: dict[str, Callable]) -> Action:
        """
        Generates an action (tool call or final answer) based on the conversation.
        """
        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)
        tools = list(tool_registry.values())
        response = client.models.generate_content(
            model=MODEL_ID, contents=prompt, tools=tools
        )
        
        # Check if the model returned a function call
        if hasattr(response.candidates[0].content.parts[0], "function_call"):
            function_call = response.candidates[0].content.parts[0].function_call
            return ToolCallRequest(
                name=function_call.name, args=dict(function_call.args)
            )
        else:
            # If no function call, it's a final answer
            return ACTION_FINISH
    ```
    The core logic here is parsing the response. If the model returns a `function_call` object, we parse it into our `ToolCallRequest` Pydantic model. If not, we interpret the response as a signal to finish the task. This dual format gives the agent a clear way to either continue its work or conclude.

    In a production system, error handling is critical. What if the tool fails, the API times out, or the LLM returns a malformed response? A simple `try-except` block is a start, but more advanced patterns provide greater resilience. For instance, a **retry mechanism** with exponential backoff can handle transient network failures. A **circuit breaker** pattern can prevent an agent from repeatedly calling a failing service, temporarily disabling the tool and allowing the system to recover.

    Furthermore, some frameworks allow for **tool call repair**. If a tool call fails due to invalid arguments, the error can be fed back to the LLM in the next turn. The model can then analyze the error message and attempt to correct its previous tool call, enabling a form of self-healing.[[16]](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling#tool-call-repair) This makes the agent more robust to its own mistakes. For example, if a tool call fails due to a `NoSuchToolError`, an `onError` function could inform the model that the tool is unknown, allowing it to try a different one.
    ```python
    # Pseudocode for advanced error handling
    try:
        # Generate action
        action = generate_action(...)
    except (NoSuchToolError, InvalidToolInputError) as e:
        # Feed the error back to the model for self-correction
        error_observation = f"Error: {e}. Please try a different tool or correct your input."
        # Add error_observation to scratchpad and re-run the thought phase
        ...
    ```

We now have separate functions for the "Thought" and "Action" phases. The final piece is a control loop to orchestrate them, execute tools, and manage the "Observation" phase.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop is the heart of our ReAct agent. It orchestrates the full Thought-Action-Observation cycle, manages the conversation history (our "scratchpad"), and executes tools. This loop is what makes the agent dynamic, allowing it to iterate and adapt its strategy based on new information.

We will start by defining a structured way to represent messages in our scratchpad. This makes the agent's internal state explicit and easy to track, which is essential for both debugging and for providing clear context to the LLM in subsequent turns.

1.  We define `MessageRole` using an `Enum` and a `Message` Pydantic model to structure each turn of the conversation. This ensures every piece of information in our scratchpad has a clear role, whether it is a user query, an internal thought, a tool call, or an observation. This structured approach is fundamental to building reliable agents, as it imposes a predictable format on the otherwise unstructured flow of conversation.
    ```python
    class MessageRole(Enum):
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool_request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final_answer"
    
    
    class Message(BaseModel):
        role: MessageRole
        content: str
    ```

2.  We create helper functions to format the scratchpad for both the LLM and for human-readable logging. The `format_scratchpad_for_llm` function converts our list of `Message` objects into a single string with XML tags, which is the format our thought and action prompts expect. This serialization step is where the agent's memory is prepared for the LLM, and its format can significantly impact performance.
    ```python
    def format_scratchpad_for_llm(scratchpad: list[Message]) -> str:
        """
        Formats the scratchpad into a string for the LLM prompt.
        """
        formatted_str = ""
        for msg in scratchpad:
            formatted_str += f"<{msg.role.value}>\n{msg.content}\n</{msg.role.value}>\n"
        return formatted_str
    ```
    In a long-running agent, the scratchpad can grow to exceed the model's context window. Production systems use context compression techniques, such as summarization or selectively removing less relevant turns, to manage token usage and prevent errors.[[17]](https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/) Our simple list-based scratchpad is a good starting point, but for more complex applications, you would need a more sophisticated memory management strategy, a topic we will cover in a future lesson. Without a proper control loop that integrates observations, multi-turn scenarios often fail due to lost context or an inability to handle dependencies between turns.[[21]](https://arxiv.org/html/2410.24663v1)

3.  Now, we build the main `react_agent_loop`. This function orchestrates the entire ReAct cycle. It runs for a maximum number of turns, generating a thought, then an action. If the action is a tool call, it executes the tool, records the output as an observation, and adds it to the scratchpad. If the action is to finish, or if it reaches the maximum turns, it generates a final answer and terminates.
    ```python
    def react_agent_loop(
        user_query: str, tool_registry: dict[str, Callable], max_turns: int = 5, verbose: bool = False
    ) -> str:
        """
        The main ReAct agent loop.
        """
        scratchpad = [Message(role=MessageRole.USER, content=user_query)]
    
        for turn in range(max_turns):
            if verbose:
                print(f"--- Turn {turn + 1}/{max_turns} ---")
    
            # 1. Thought Phase
            conversation = format_scratchpad_for_llm(scratchpad)
            thought = generate_thought(conversation, tool_registry)
            thought_message = Message(role=MessageRole.THOUGHT, content=thought)
            scratchpad.append(thought_message)
            if verbose:
                pretty_print_conversation([thought_message])
    
            # 2. Action Phase
            conversation = format_scratchpad_for_llm(scratchpad)
            action = generate_action(conversation, tool_registry)
    
            if action == ACTION_FINISH:
                break
    
            tool_request_content = f"Tool: {action.name}, Args: {json.dumps(action.args)}"
            tool_request_message = Message(
                role=MessageRole.TOOL_REQUEST, content=tool_request_content
            )
            scratchpad.append(tool_request_message)
            if verbose:
                pretty_print_conversation([tool_request_message])
    
            # 3. Observation Phase
            if action.name in tool_registry:
                tool_func = tool_registry[action.name]
                try:
                    observation = tool_func(**action.args)
                except Exception as e:
                    observation = f"Error executing tool {action.name}: {e}"
            else:
                observation = f"Tool '{action.name}' not found. Available tools: {list(tool_registry.keys())}"
    
            observation_message = Message(
                role=MessageRole.OBSERVATION, content=str(observation)
            )
            scratchpad.append(observation_message)
            if verbose:
                pretty_print_conversation([observation_message])
    
        # Generate Final Answer
        conversation = format_scratchpad_for_llm(scratchpad)
        final_answer_prompt = f"{conversation}\nProvide a final answer to the user's query."
        final_answer = client.models.generate_content(
            model=MODEL_ID, contents=final_answer_prompt
        ).text.strip()
        final_answer_message = Message(
            role=MessageRole.FINAL_ANSWER, content=final_answer
        )
        scratchpad.append(final_answer_message)
        if verbose:
            pretty_print_conversation([final_answer_message])
    
        return final_answer
    ```
    This implementation directly mirrors the theoretical ReAct pattern. The agent loops through thinking, acting, and observing, using the scratchpad as its short-term memory. The "Observation" phase is critical; it closes the feedback loop by providing the results of an action back to the agent's reasoning process.[[1]](https://arxiv.org/pdf/2210.03629) This allows the agent to learn from its interactions and adjust its plan. The `max_turns` parameter is not just a failsafe; it is a critical guardrail to prevent runaway loops that can occur due to high API latency or repetitive model behavior, turning a potential infinite loop into a controlled failure.[[18]](https://blog.logrocket.com/5-reasons-ai-app-fails-production/)

    This control loop can be visualized as a simple state graph, similar to what frameworks like LangGraph implement under the hood.[[7]](https://www.decodingai.com/p/building-production-react-agents)

    ```mermaid
flowchart LR
  _start_ --> "llm"
  "llm" -- "continue" --> "tools"
  "llm" -- "end" --> _end_
  "tools" --> "llm"
```
    Image 1: A flowchart illustrating the LangGraph implementation of the ReAct agent control loop.

    Our `react_agent_loop` function is a manual implementation of this graph. The `llm` node represents our `generate_thought` and `generate_action` calls, and the `tools` node corresponds to the observation phase where we execute the tool function. The loop continues until the agent decides to `end`. This graph-based mental model is powerful because it allows you to visualize the agent's control flow and identify potential points of failure or optimization.

The loop seems complete, but the real test is seeing it in action. We need to validate its behavior on both successful and unsuccessful queries to ensure it is robust.

## Tests and Traces: Success and Graceful Fallback

With our ReAct loop fully implemented, it is time to test it. Analyzing the agent's execution traces allows us to verify that each component—thought, action, observation, and termination—is working as expected. We will run two tests: a simple factual query that our mock tool can answer and a query designed to fail.

### Success Case

First, let’s ask a question our mock `search` tool is designed to handle: "What is the capital of France?". We will run the loop for a maximum of two turns.

```python
react_agent_loop(
    user_query="What is the capital of France?",
    tool_registry=TOOL_REGISTRY,
    max_turns=2,
    verbose=True,
)
```

The output trace clearly shows the ReAct cycle in action:
*   **Turn 1/2:**
    *   **Thought:** The agent correctly identifies that it needs to find the capital of France and decides the `search` tool is appropriate. This step shows the agent's ability to decompose the user's query into a concrete plan. The thought is: `I need to find the capital of France. I can use the search tool for this.`
    *   **Tool Request:** It generates a call to `search(query='capital of France')`. This confirms our action generation and parsing logic is working.
    *   **Observation:** The control loop executes our mock tool, which returns the predefined answer: "Paris is the capital of France and is known for the Eiffel Tower." This closes the first loop, providing the agent with new information.
*   **Turn 2/2:**
    *   **Thought:** After observing the result, the agent concludes it has enough information to answer the user's query. It recognizes that the observation directly answers the question. The thought generated is: `The search result provides the answer. I can now formulate the final response.`
    *   **Final Answer:** The loop terminates because the agent signals it is finished, and it generates the final, concise answer: "Paris is the capital of France."

This trace confirms that our agent can successfully use a tool to find information and formulate an answer. The explicit thoughts provide a clear window into its reasoning process, making it easy to debug and trust.

### Graceful Fallback Case

Now, let’s test a query that our mock tool cannot answer: "What is the capital of Italy?". This will test the agent's ability to handle failure and adapt its strategy.

```python
react_agent_loop(
    user_query="What is the capital of Italy?",
    tool_registry=TOOL_REGISTRY,
    max_turns=2,
    verbose=True,
)
```

The trace for this query demonstrates graceful fallback:
*   **Turn 1/2:**
    *   **Thought & Tool Request:** The agent tries to search for "capital of Italy", following the same logic as the successful case. Its thought is: `I need to find the capital of Italy. I will use the search tool.`
    *   **Observation:** Our mock tool returns the fallback message: "Information about 'capital of Italy' was not found." This simulates a failed tool execution.
*   **Turn 2/2:**
    *   **Thought:** Observing the failure, the agent adapts its strategy. It decides to try a broader search for just "Italy", hoping to find the capital that way. This demonstrates a simple but important form of error recovery. The thought is: `The previous search failed. I will try a broader query to see if I can find any information about Italy that might mention its capital.`
    *   **Tool Request:** It calls `search(query='Italy')`.
    *   **Observation:** This search also fails, as "Italy" is not a predefined query in our mock tool.
*   **Final Answer (Forced):** The loop reaches its `max_turns` limit. The agent is forced to conclude and generates a final answer admitting it could not find the information: "I'm sorry, but I couldn't find information about the capital of Italy."

This example highlights the agent's resilience. Even with a simple mock tool, it attempts to recover from failure by adjusting its plan. The forced termination ensures the agent does not get stuck in an infinite loop.

In a production setting, testing goes far beyond these simple cases. You would design a comprehensive test suite, much like in traditional software engineering. This would include **unit tests** for each tool to ensure they handle various inputs and edge cases correctly. **Integration tests** would validate the ReAct loop itself, using mock tools to simulate different scenarios like tool failures, long-running tasks, or unexpected outputs. Finally, **end-to-end tests** would run the agent against real APIs in a sandboxed environment to verify its behavior in a live setting.

You would also create a "golden dataset" of queries with expected outcomes to benchmark performance and detect regressions over time. Testing for **adversarial prompts**—queries designed to confuse the agent or exploit vulnerabilities—is also essential for building a robust and secure system.[[17]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)

These tests confirm our from-scratch implementation of the ReAct loop is working correctly, providing a solid baseline for building more advanced agents in future lessons.

## Conclusion

By building a ReAct agent from the ground up, we have demystified the magic behind agentic frameworks. We have seen how the Thought-Action-Observation loop is not an abstract concept but a concrete software pattern implemented with prompts, function calls, and a control loop. This hands-on process provides a solid mental model for how these systems reason, plan, and execute tasks.

When building agents, we recommend focusing on three core principles: maintain simplicity in your design, prioritize transparency by making planning steps explicit, and carefully craft your agent-computer interface through thorough tool documentation and testing.[[11]](https://www.anthropic.com/engineering/building-effective-agents)

Even if you ultimately use a framework like LangGraph or CrewAI in production, this fundamental understanding is very useful. You will be better equipped to debug unexpected behavior, customize agent logic, and optimize performance because you know what is happening under the hood. For example, a ReAct agent could be used in a contact center to reason through a customer complaint, query a CRM to check purchase history, and decide whether to trigger a refund or escalate to a human.[[19]](https://www.salesforce.com/agentforce/ai-agents/react-agents/)

This lesson is a stepping stone. In our upcoming lessons, we will build upon this foundation to explore more advanced topics like agent memory and Retrieval-Augmented Generation (RAG). We will also look at emerging trends, like combining ReAct with reinforcement learning to enhance adaptability, as we prepare you to build truly production-grade AI systems.[[20]](https://arxiv.org/html/2404.04650v1)

## References

- [1] https://arxiv.org/pdf/2210.03629
- [2] https://ai.google.dev/gemini-api/docs/prompting-strategies
- [3] https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [5] https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [6] https://ai.google.dev/gemini-api/docs/function-calling
- [7] https://www.decodingai.com/p/building-production-react-agents
- [8] https://ai.google.dev/gemini-api/docs/langgraph-example
- [9] https://www.philschmid.de/langgraph-gemini-1-5-react-agent
- [10] https://www.techtarget.com/searchenterpriseai/tip/How-ReAct-agents-can-transform-the-enterprise
- [11] https://www.anthropic.com/engineering/building-effective-agents
- [12] https://www.ibm.com/think/topics/ai-agent-planning
- [13] https://stevekinney.com/writing/prompt-engineering-frontier-llms
- [14] https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [15] https://www.ibm.com/think/topics/react-agent
- [16] https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling#tool-call-repair
- [17] https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/
- [18] https://blog.logrocket.com/5-reasons-ai-app-fails-production/
- [19] https://www.salesforce.com/agentforce/ai-agents/react-agents/
- [20] https://arxiv.org/html/2404.04650v1
- [21] https://arxiv.org/html/2410.24663v1