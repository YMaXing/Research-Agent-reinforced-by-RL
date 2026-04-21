# Building a ReAct Agent From Scratch

In our previous lessons, we’ve covered the key concepts of AI Engineering, from context engineering and structured outputs to tools and planning. We’ve explored the theoretical foundations of the ReAct framework, which combines reasoning and acting to solve complex tasks. Now, it’s time to put that theory into practice.

This lesson is 100% hands-on. We will build a minimal ReAct agent from the ground up using only Python and the Gemini API. By implementing the full Thought → Action → Observation loop yourself, you will gain a concrete mental model of how these systems work. This practical knowledge is essential for building reliable AI systems.

We will walk through every step: defining a mock tool, generating thoughts, selecting actions with function calling, executing the tool, processing the observation, and orchestrating the entire process with a control loop. By the end, you’ll have a working agent that you can extend, debug, and customize with confidence.

Let’s get started.

## Setup and Environment

First, we need to ensure our environment is set up correctly to run the code from this lesson’s notebook. A proper setup is essential for reproducibility and ensures your outputs will match the traces we analyze later. We will configure the necessary API keys, import key packages, and initialize the Gemini client.

1.  We begin by loading our `GOOGLE_API_KEY` from the `.env` file using a utility function. This keeps our credentials secure and separate from the code. Make sure you have followed the setup instructions from the `Course Admin` lesson to create your `.env` file.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    ```

2.  Next, we import the key packages we will use throughout the lesson. We need `google-genai` to interact with the Gemini API, `pydantic` for creating structured data models, and standard Python libraries like `enum` and `typing`. We also import our custom `pretty_print` utility, which will help visualize the agent's steps in a readable format.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client, which will be our main interface for making API calls. This object handles the communication with Google's backend.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`. This model is designed for speed and cost-effectiveness, making it an excellent choice for development and for tasks that require quick responses.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model in place, our environment is ready. We can now define the external capabilities our agent will use to interact with the world.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to interact with the outside world through tools. For this lesson, we will create a simple mock search tool. This approach allows us to focus purely on the ReAct mechanics without worrying about real-world complexities like API keys, network latency, or unpredictable third-party service responses.

The philosophy behind using a mock tool here is educational. It simplifies the learning process by providing a controlled environment. You get predictable and consistent responses, which is essential for testing and understanding the agent's behavior. When you can anticipate what a tool will return, it becomes much easier to trace the agent's reasoning process and debug its logic. This hands-on implementation provides a concrete mental model for how agents chain tool uses, maintain context, and follow structured response formats for safe and interpretable interactions [[1]](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/).

1.  Our mock `search` tool is a simple Python function. It takes a `query` string and returns a predefined answer if the query matches a known topic. If the query is not recognized, it returns a fallback message. The docstring is extremely important; it serves as the primary documentation for the LLM, providing a description of what the tool does and what arguments it expects. A well-written docstring is critical for the model to select and use the tool correctly.
    ```python
    def search(query: str) -> str:
        """Search for information about a specific topic or query.

        Args:
            query (str): The search query or topic to look up.
        """
        query_lower = query.lower()

        # Predefined responses for demonstration
        if all(word in query_lower for word in ["capital", "france"]):
            return "Paris is the capital of France and is known for the Eiffel Tower."
        elif "react" in query_lower:
            return "The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing."

        # Generic response for unhandled queries
        return f"Information about '{query}' was not found."
    ```

2.  To manage our tools, we use a `TOOL_REGISTRY`. This dictionary maps the tool's name (derived from the function's name) to the actual callable function. This registry is a central part of our agent's architecture, allowing our control loop to look up and dynamically execute the correct tool based on the LLM's decision.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

In a production system, swapping this mock function with a real API call is straightforward. You could replace it with a function that queries Google Search, Wikipedia, or a private knowledge base [[2]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae). As long as the new function maintains the same signature (a query string as input and a string as output) and the docstring accurately reflects its purpose, the rest of the agent's logic remains unchanged. This modular design is a key principle for building scalable and maintainable AI systems.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is where the agent analyzes the user's query and the conversation history to reason about a plan. To guide the LLM in generating a useful thought, we need to construct a clear and informative prompt. This prompt will provide the model with all the context it needs to make a good decision.

The core idea is to dynamically build the prompt by including descriptions of the available tools. This allows the model to reason about which tool is best suited for the current subtask. We will use XML tags to structure the prompt, which helps the model distinguish between different types of information, such as instructions, tool definitions, and conversation history.

1.  First, we create a helper function, `build_tools_xml_description`, to programmatically generate an XML representation of our tools. This function iterates through the `TOOL_REGISTRY`, extracts the docstring from each tool function, and formats it into a `<tool>` block. This ensures that our prompt is always up-to-date with the available tools without manual changes.
    ```python
    def build_tools_xml_description(tools: dict[str, callable]) -> str:
        """Build a minimal XML description of tools using only their docstrings."""
        lines = []
        for tool_name, fn in tools.items():
            doc = (fn.__doc__ or "").strip()
            lines.append(f"\t<tool name=\"{tool_name}\">")
            if doc:
                lines.append(f"\t\t<description>")
                for line in doc.split("\n"):
                    lines.append(f"\t\t\t{line}")
                lines.append(f"\t\t</description>")
            lines.append("\t</tool>")
        return "\n".join(lines)
    ```

2.  Next, we define our `PROMPT_TEMPLATE_THOUGHT`. This template contains the instructions for the model, the XML block for the tools, and a placeholder for the ongoing conversation. It explicitly asks the model to state its next thought as a short paragraph focused on the intended action and the reasoning behind it.
    ```python
    tools_xml = build_tools_xml_description(TOOL_REGISTRY)

    PROMPT_TEMPLATE_THOUGHT = f"""
    You are deciding the next best step for reaching the user goal. You have some tools available to you.

    Available tools:
    <tools>
    {tools_xml}
    </tools>

    Conversation so far:
    <conversation>
    {{conversation}}
    </conversation>

    State your next thought about what to do next as one short paragraph focused on the next action you intend to take and why.
    Avoid repeating the same strategies that didn't work previously. Prefer different approaches.
    """.strip()
    ```

3.  Let's inspect the final prompt to see exactly what the model will receive.
    ```python
    print(PROMPT_TEMPLATE_THOUGHT)
    ```
    It outputs:
    ```text
    You are deciding the next best step for reaching the user goal. You have some tools available to you.

    Available tools:
    <tools>
        <tool name="search">
            <description>
                Search for information about a specific topic or query.
                
                Args:
                    query (str): The search query or topic to look up.
            </description>
        </tool>
    </tools>

    Conversation so far:
    <conversation>
    {conversation}
    </conversation>

    State your next thought about what to do next as one short paragraph focused on the next action you intend to take and why.
    Avoid repeating the same strategies that didn't work previously. Prefer different approaches.
    ```
    The output shows the clear, structured context the model sees: a set of instructions, an XML block defining the `search` tool with its description, and a placeholder for the conversation history.

4.  Finally, the `generate_thought` function ties it all together. It takes the current conversation string, builds the complete prompt using the template, calls the Gemini API, and returns the model's generated thought as a clean string.
    ```python
    def generate_thought(conversation: str, tool_registry: dict[str, callable]) -> str:
        """Generate a thought as plain text (no structured output)."""
        tools_xml = build_tools_xml_description(tool_registry)
        prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation)

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return response.text.strip()
    ```

With a coherent thought generated, the agent must now decide whether to use a tool to gather more information or to conclude with a final answer. This brings us to the "Action" phase.

## Action Phase: Function Calling and Parsing

After the "Thought" phase, the agent moves to the "Action" phase, where it makes a concrete decision: either call a tool or provide a final answer. We will use Gemini's native function calling capabilities to make this process robust and reliable. This approach is superior to manually parsing text because it leverages the model's built-in ability to generate structured JSON output for tool calls [[3]](https://ai.google.dev/gemini-api/docs/function-calling).

A key strategy here is the separation of concerns. The system prompt for the action phase focuses on high-level decision-making—choosing *whether* to act—rather than on the technical details of the tools. We do not need to include tool descriptions or signatures in the prompt itself. Instead, we pass the Python tool functions directly to the Gemini client's `tools` configuration. The client automatically handles the conversion of the function's signature and docstring into a format the model understands. This keeps our prompts clean and makes tool management much easier.

1.  We start with two prompt templates. The main one, `PROMPT_TEMPLATE_ACTION`, instructs the model to choose between a tool call and a final answer based on the conversation so far. The second, `PROMPT_TEMPLATE_ACTION_FORCED`, is a special-purpose prompt. We use it when the agent reaches its maximum turn limit to guarantee it produces a final answer instead of attempting another tool call, thus preventing infinite loops.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are selecting the best next action to reach the user goal.

    Conversation so far:
    <conversation>
    {conversation}
    </conversation>

    Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
    """.strip()

    # Dedicated prompt used when we must force a final answer
    PROMPT_TEMPLATE_ACTION_FORCED = """
    You must now provide a final answer to the user.

    Conversation so far:
    <conversation>
    {conversation}
    </conversation>

    Provide a concise final answer that best addresses the user's goal.
    """.strip()
    ```

2.  To handle the model's output in a structured way, we define two Pydantic models: `ToolCallRequest` and `FinalAnswer`. These classes act as a schema for the model's response. `ToolCallRequest` captures the details needed to execute a tool, while `FinalAnswer` holds the text of a concluding response. This ensures we can reliably parse the model's decision.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  The `generate_action` function orchestrates this phase. It takes the conversation history and the tool registry as input.
    ```python
    def generate_action(conversation: str, tool_registry: dict[str, callable] | None = None, force_final: bool = False) -> (ToolCallRequest | FinalAnswer):
        """Generate an action by passing tools to the LLM and parsing function calls or final text.

        When force_final is True or no tools are provided, the model is instructed to produce a final answer and tool calls are disabled.
        """
        # Use a dedicated prompt when forcing a final answer or no tools are provided
        if force_final or not tool_registry:
            prompt = PROMPT_TEMPLATE_ACTION_FORCED.format(conversation=conversation)
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt
            )
            return FinalAnswer(text=response.text.strip())

        # Default action prompt
        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)

        # Provide the available tools to the model; disable auto-calling so we can parse and run ourselves
        tools = list(tool_registry.values())
        config = types.GenerateContentConfig(
            tools=tools,
            automatic_function_calling={"disable": True}
        )
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=config
        )

        # Extract the function call from the response (if present)
        candidate = response.candidates[0]
        parts = candidate.content.parts
        if parts and getattr(parts[0], "function_call", None):
            name = parts[0].function_call.name
            args = dict(parts[0].function_call.args) if parts[0].function_call.args is not None else {}
            return ToolCallRequest(tool_name=name, arguments=args)
        
        # Otherwise, it's a final answer
        final_answer = "".join(part.text for part in candidate.content.parts)
        return FinalAnswer(text=final_answer.strip())
    ```
    The logic is straightforward. If `force_final` is `True`, it uses the specialized prompt to request a conclusive answer. Otherwise, it sends the main prompt along with the list of tools to the Gemini API. We set `automatic_function_calling={"disable": True}` because we want full control over parsing the tool call and executing it within our loop.

    The response parsing logic then inspects the model's output. It checks if the response contains a `function_call` object. If it does, it extracts the tool's name and arguments and returns a `ToolCallRequest` instance. If no function call is present, it assumes the response is a final answer and returns a `FinalAnswer` instance. This clear, structured decision from the LLM is now ready to be used by our control loop.

## Control Loop: Messages, Scratchpad, and Orchestration

Now we arrive at the core of our agent: the control loop. This is the engine that orchestrates the Thought → Action → Observation cycle. It manages the conversation history, calls the thought and action generation functions, executes tools, and processes the results. To manage the state of the conversation, we will use a "scratchpad," which is a list of messages that records every step of the ReAct process.

1.  We start by defining the data structures for our messages. `MessageRole` is an `Enum` that categorizes each message type (e.g., `USER`, `THOUGHT`, `OBSERVATION`). The `Message` class is a Pydantic model that holds the role and content for any message in the loop, providing a standardized format for our history.
    ```python
    class MessageRole(str, Enum):
        """Enumeration for the different roles a message can have."""
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final answer"


    class Message(BaseModel):
        """A message with a role and content, used for all message types."""
        role: MessageRole = Field(description="The role of the message in the ReAct loop.")
        content: str = Field(description="The textual content of the message.")

        def __str__(self) -> str:
            """Provides a user-friendly string representation of the message."""
            return f"{self.role.value.capitalize()}: {self.content}"
    ```

2.  To make the agent's process easy to follow, we create a helper function to print each message with a color-coded header indicating its role and the current turn. This visualization is invaluable for debugging and understanding the agent's behavior.
    ```python
    def pretty_print_message(message: Message, turn: int, max_turns: int, header_color: str = pretty_print.Color.YELLOW, is_forced_final_answer: bool = False) -> None:
        if not is_forced_final_answer:
            title = f"{message.role.value.capitalize()} (Turn {turn}/{max_turns}):"
        else:
            title = f"{message.role.value.capitalize()} (Forced):"

        pretty_print.wrapped(
            text=message.content,
            title=title,
            header_color=header_color,
        )
    ```

3.  The `Scratchpad` class manages the list of messages. Its `append` method adds a new message and, if `verbose` is enabled, prints it using our pretty-printer. The `to_string` method serializes the entire message history into a single string, which we will pass to the LLM as context for the next turn.
    ```python
    class Scratchpad:
        """Container for ReAct messages with optional pretty-print on append."""

        def __init__(self, max_turns: int) -> None:
            self.messages: List[Message] = []
            self.max_turns: int = max_turns
            self.current_turn: int = 1

        def set_turn(self, turn: int) -> None:
            self.current_turn = turn

        def append(self, message: Message, verbose: bool = False, is_forced_final_answer: bool = False) -> None:
            self.messages.append(message)
            if verbose:
                role_to_color = {
                    MessageRole.USER: pretty_print.Color.RESET,
                    MessageRole.THOUGHT: pretty_print.Color.ORANGE,
                    MessageRole.TOOL_REQUEST: pretty_print.Color.GREEN,
                    MessageRole.OBSERVATION: pretty_print.Color.YELLOW,
                    MessageRole.FINAL_ANSWER: pretty_print.Color.CYAN,
                }
                header_color = role_to_color.get(message.role, pretty_print.Color.YELLOW)
                pretty_print_message(
                    message=message,
                    turn=self.current_turn,
                    max_turns=self.max_turns,
                    header_color=header_color,
                    is_forced_final_answer=is_forced_final_answer,
                )

        def to_string(self) -> str:
            return "\n".join(str(m) for m in self.messages)
    ```

4.  Finally, we implement the `react_agent_loop` function. This is where everything comes together.
    ```python
    def react_agent_loop(initial_question: str, tool_registry: dict[str, callable], max_turns: int = 5, verbose: bool = False) -> str:
        """
        Implements the main ReAct (Thought -> Action -> Observation) control loop.
        Uses a unified message class for the scratchpad.
        """
        scratchpad = Scratchpad(max_turns=max_turns)

        # Add the user's question to the scratchpad
        user_message = Message(role=MessageRole.USER, content=initial_question)
        scratchpad.append(user_message, verbose=verbose)

        for turn in range(1, max_turns + 1):
            scratchpad.set_turn(turn)

            # Generate a thought based on the current scratchpad
            thought_content = generate_thought(
                scratchpad.to_string(),
                tool_registry,
            )
            thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
            scratchpad.append(thought_message, verbose=verbose)

            # Generate an action based on the current scratchpad
            action_result = generate_action(
                scratchpad.to_string(),
                tool_registry=tool_registry,
            )

            # If the model produced a final answer, return it
            if isinstance(action_result, FinalAnswer):
                final_answer = action_result.text
                final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                scratchpad.append(final_message, verbose=verbose)
                return final_answer

            # Otherwise, it is a tool request
            if isinstance(action_result, ToolCallRequest):
                action_name = action_result.tool_name
                action_params = action_result.arguments

                # Add the action to the scratchpad
                params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
                action_content = f"{action_name}({params_str})"
                action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
                scratchpad.append(action_message, verbose=verbose)

                # Run the action and get the observation
                observation_content = ""
                tool_function = tool_registry.get(action_name)
                if tool_function:
                    try:
                        observation_content = tool_function(**action_params)
                    except Exception as e:
                        observation_content = f"Error executing tool '{action_name}': {e}"
                else:
                    observation_content = f"Error: Unknown tool '{action_name}'. Available tools: {list(tool_registry.keys())}"


                # Add the observation to the scratchpad
                observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
                scratchpad.append(observation_message, verbose=verbose)

            # Check if the maximum number of turns has been reached. If so, force the action selector to produce a final answer
            if turn == max_turns:
                forced_action = generate_action(
                    scratchpad.to_string(),
                    force_final=True,
                )
                if isinstance(forced_action, FinalAnswer):
                    final_answer = forced_action.text
                else:
                    final_answer = "Unable to produce a final answer within the allotted turns."
                final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                scratchpad.append(final_message, verbose=verbose, is_forced_final_answer=True)
                return final_answer
    ```
    The loop starts by adding the user's question to the scratchpad. Then, for a set number of turns, it generates a thought and an action. If the action is a `FinalAnswer`, the loop terminates. If it's a `ToolCallRequest`, the loop executes the tool, captures the output as an "Observation," and adds it to the scratchpad. The observation processing is robust: it includes a `try...except` block to catch errors during tool execution and returns an informative error message. It also handles cases where the model requests an unknown tool. If the loop reaches `max_turns`, it makes a final call to `generate_action` with `force_final=True` to ensure a graceful exit.

While our scratchpad implementation is effective for simple tasks, its linear accumulation of messages presents challenges for scaling. As turns increase, the context can grow too large, leading to issues like context overload, the "lost-in-the-middle" problem where models forget details, and high token costs [[4]](https://langwatch.ai/blog/the-6-context-engineering-challenges-stopping-ai-from-scaling-in-production). These problems can degrade performance and even trigger model-specific failure modes, like infinite tool-call loops [[5]](https://discuss.ai.google.dev/t/gemini-2-5-flash-stuck-in-a-tool-call-loop-when-using-both-tools-and-structured-output/110777). Advanced memory management and context compression techniques, which we will cover in later lessons, are needed to address these scaling issues.

This control loop, illustrated in the diagram below, is the complete implementation of the ReAct pattern.

```mermaid
flowchart LR
    Start["Start: react_agent_loop"]

    subgraph "Initialization"
        InitialQuestion["initial_question"]
        AddUserMsg["Add initial_question to Scratchpad<br/>(MessageRole.USER)"]
    end

    Start --> InitialQuestion
    InitialQuestion --> AddUserMsg

    subgraph "ReAct Control Loop (Iterative Thought-Action-Observation)"
        direction TD
        MaxTurnsCheck{"turn == max_turns?"}
        ForceFinalAction["generate_action(force_final=True)"]
        AddForcedFinalAnswerMsg["Add Forced FinalAnswer to Scratchpad<br/>(MessageRole.FINAL_ANSWER)"]

        GenerateThought["generate_thought(scratchpad.to_string())"]
        AddThoughtMsg["Add thought to Scratchpad<br/>(MessageRole.THOUGHT)"]

        GenerateAction["generate_action()"]
        IsFinalAnswer{"Returns FinalAnswer?"}
        AddFinalAnswerMsg["Add FinalAnswer to Scratchpad<br/>(MessageRole.FINAL_ANSWER)"]

        AddToolRequestMsg["Add ToolCallRequest to Scratchpad<br/>(MessageRole.TOOL_REQUEST)"]
        ExecuteTool["Execute tool from TOOL_REGISTRY<br/>with action_params"]
        AddObservationMsg["Add result/error to Scratchpad<br/>(MessageRole.OBSERVATION)"]

        AddUserMsg --> MaxTurnsCheck

        MaxTurnsCheck -->|Yes| ForceFinalAction
        ForceFinalAction --> AddForcedFinalAnswerMsg

        MaxTurnsCheck -->|No| GenerateThought
        GenerateThought --> AddThoughtMsg
        AddThoughtMsg --> GenerateAction

        GenerateAction --> IsFinalAnswer
        IsFinalAnswer -->|Yes| AddFinalAnswerMsg

        IsFinalAnswer -->|No (ToolCallRequest)| AddToolRequestMsg
        AddToolRequestMsg --> ExecuteTool
        ExecuteTool --> AddObservationMsg
        AddObservationMsg --> MaxTurnsCheck
    end

    AddForcedFinalAnswerMsg --> End["End: react_agent_loop"]
    AddFinalAnswerMsg --> End

    subgraph "Scratchpad (Conversation History)"
        direction LR
        Scratchpad[(Scratchpad)]
    end

    AddUserMsg -.-> Scratchpad
    AddThoughtMsg -.-> Scratchpad
    AddToolRequestMsg -.-> Scratchpad
    AddObservationMsg -.-> Scratchpad
    AddFinalAnswerMsg -.-> Scratchpad
    AddForcedFinalAnswerMsg -.-> Scratchpad

    classDef messageRole fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    class AddUserMsg,AddThoughtMsg,AddToolRequestMsg,AddObservationMsg,AddFinalAnswerMsg,AddForcedFinalAnswerMsg messageRole
    classDef decision fill:#fff3e0,stroke:#ff9800,stroke-width:2px
    class MaxTurnsCheck,IsFinalAnswer decision
    classDef action fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    class ForceFinalAction,GenerateThought,GenerateAction,ExecuteTool action
```
Image 1: A flowchart illustrating the ReAct control loop, showing the iterative Thought-Action-Observation cycle and the role of the Scratchpad.

## Tests and Traces: Success and Graceful Fallback

With our agent fully implemented, it is time to test it. We will run two scenarios to validate its behavior: a successful query that our mock tool can handle and a query that forces the agent to handle a failure and terminate gracefully. Analyzing the traces will confirm that our ReAct loop, tool integration, and termination logic work as expected.

### Successful Execution Trace

Let's start with a straightforward factual question that our mock tool is designed to answer: "What is the capital of France?" We will set `max_turns=2` and `verbose=True` to observe the agent's step-by-step process. This trace will demonstrate the ideal path where the agent finds the information it needs on the first try.
```python
# A straightforward question requiring a search.
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
The agent produces the following trace, which we can analyze turn by turn:

*   **Turn 1:**
    1.  **User:** The loop begins with the initial question, "What is the capital of France?", which is added to the scratchpad.
    2.  **Thought:** The agent reasons that to answer the question, it needs to find the capital of France. It correctly identifies the `search` tool as the appropriate action for this factual lookup.
    3.  **Tool Request:** Based on its thought, it generates a tool call: `search(query='capital of France')`.
    4.  **Observation:** Our control loop executes the mock `search` tool. The tool finds a match and returns the predefined response: "Paris is the capital of France and is known for the Eiffel Tower." This observation is added to the scratchpad, providing the agent with the necessary information.
*   **Turn 2:**
    1.  **Thought:** In the next turn, the agent reviews the scratchpad, which now includes the successful observation. It recognizes that the answer has been found and its task is complete. Its thought is to communicate this answer to the user.
    2.  **Final Answer:** The agent generates the final answer: "Paris is the capital of France." The `generate_action` function returns a `FinalAnswer` object, which causes the loop to terminate.

This trace confirms that the agent correctly follows the ReAct cycle. It thinks, acts by calling the right tool with the correct arguments, observes the result, and then uses that observation to formulate a final answer, all within the turn limit.

### Graceful Fallback Trace

Now, let's test the agent's resilience. We will ask a question our mock tool cannot answer: "What is the capital of Italy?" This scenario is designed to test the agent's ability to handle a "not found" observation and its forced termination logic when it reaches the `max_turns` limit.
```python
# An unknown/unsupported query for the mock tool.
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
The agent's trace shows how it handles the failure and adapts its strategy:

*   **Turn 1:**
    1.  **User:** The question "What is the capital of Italy?" is added to the scratchpad.
    2.  **Thought:** The agent decides to use the `search` tool to find the answer.
    3.  **Tool Request:** It calls `search(query='capital of Italy')`.
    4.  **Observation:** The mock tool does not have a predefined response for this query and returns the fallback message: "Information about 'capital of Italy' was not found."
*   **Turn 2:**
    1.  **Thought:** The agent observes that the first attempt failed. It demonstrates adaptive reasoning by changing its strategy. It hypothesizes that a broader query might yield better results and decides to search for just "Italy," hoping to find the capital within a general article.
    2.  **Tool Request:** It calls `search(query='Italy')`.
    3.  **Observation:** This second attempt also fails, as our mock tool does not recognize "Italy" either. The observation is again a "not found" message.
*   **Forced Termination:**
    1.  The agent has now reached its `max_turns` limit of 2. The `for` loop ends.
    2.  The control loop's final logic is triggered, calling `generate_action` one last time with the `force_final=True` flag.
    3.  **Final Answer (Forced):** The model, instructed to conclude, generates a polite and honest response based on the history of failed attempts: "I'm sorry, but I couldn't find information about the capital of Italy."

This trace demonstrates the agent's graceful fallback behavior. It can adapt its strategy after a failed tool call, and when it exhausts its attempts, it terminates cleanly with a helpful message instead of getting stuck in a loop or returning a hallucinated answer. These tests validate that our from-scratch ReAct implementation is both functional and robust.

## Conclusion

By building a ReAct agent from scratch, we have demystified the engineering behind the Thought-Action-Observation loop. We have seen how to orchestrate reasoning and tool use with simple Python code, a structured scratchpad, and the power of Gemini's function calling. This hands-on approach provides a solid mental model that frameworks often abstract away.

Even if you use a library like LangGraph in production, understanding these fundamental building blocks is one of the core skills of an AI Engineer. You now have the foundation to debug, customize, and extend agentic systems with confidence.

Remember that this article is part of our AI Agents Foundations series. The simple ReAct loop you built is a foundational pattern for more advanced agentic systems. Researchers are extending this model to create agents that can reason over multimodal information like images and documents, and even to build self-reflecting agents that learn from their mistakes to improve performance [[6]](https://www.emergentmind.com/topics/react-style-agents), [[7]](https://huggingface.co/blog/Kseniase/reflection). In the next lesson, we will take the first step in that direction by diving into a critical component for building more sophisticated agents: memory. We will explore how agents can remember past interactions and leverage knowledge over time.

## References

- [1] *Implementing ReAct Agentic Pattern From Scratch*. (2024, June 10). Daily Dose of DS. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [2] Shankar, A. (2024, June 20). *Building ReAct Agents from Scratch using Gemini*. Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [3] *Function calling*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [4] Draisma, M. (2025, August 19). *The 6 context engineering challenges stopping AI from scaling in production*. LangWatch. https://langwatch.ai/blog/the-6-context-engineering-challenges-stopping-ai-from-scaling-in-production
- [5] *Gemini 2.5 Flash stuck in a tool call loop when using both tools and structured output*. (n.d.). Google for Developers Community. https://discuss.ai.google.dev/t/gemini-2-5-flash-stuck-in-a-tool-call-loop-when-using-both-tools-and-structured-output/110777
- [6] *ReAct-style Agents*. (n.d.). Emergent Mind. https://www.emergentmind.com/topics/react-style-agents
- [7] Se, K. (n.d.). *Reflection: LLM Agents that Self-Improve*. Hugging Face Blog. https://huggingface.co/blog/Kseniase/reflection
- [8] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. https://arxiv.org/pdf/2210.03629
- [9] *ReAct Agent*. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [10] Stryker, C. (n.d.). *AI agent planning*. IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [11] S., E., & Zhang, B. (2024, December 19). *Building effective agents*. Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [12] *ReAct agent from scratch with Gemini 2.5 and LangGraph*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [13] Ferrag, Tihanyi, & Debbah. (2026, March). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review (2025)*. arXiv. https://arxiv.org/pdf/2504.19678
- [14] Downie, A., & Finio, M. (n.d.). *AI Agent Orchestration*. IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [15] Iusztin, P. (2025, November 18). *Building Production ReAct Agents From Scratch Is Simple*. Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [16] Brownlee, J. (2024, July 1). *Building ReAct Agents with LangGraph: A Beginner’s Guide*. Machine Learning Mastery. https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/
- [17] Lu, Y., Liu, S., & Dong, L. (2025, October 28). *OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs*. arXiv. https://arxiv.org/html/2510.24663v1
- [18] Schmid, P. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://www.philschmid.de/langgraph-gemini-2-5-react-agent