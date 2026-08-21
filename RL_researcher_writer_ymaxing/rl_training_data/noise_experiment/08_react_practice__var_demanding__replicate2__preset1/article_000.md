# Lesson 8: Building a ReAct Agent From Scratch

In the last lesson, we covered the theory behind agentic reasoning, exploring patterns like ReAct and Plan-and-Execute. We learned how ReAct (Reasoning and Acting) enables an agent to break down complex tasks into a series of Thought → Action → Observation steps. This iterative loop allows the agent to interact with its environment, gather information, and adapt its strategy until it reaches a goal [[3]](https://arxiv.org/pdf/2210.03629), [[4]](https://www.ibm.com/think/topics/react-agent).

But theory only gets you so far. To truly understand how these systems work, you have to build one. Abstract diagrams of loops and nodes become clear once you write the code that brings them to life. This hands-on implementation provides a concrete mental model that is essential for debugging, extending, and confidently building your own agents.

This lesson is 100% practical. We will walk you through building a minimal ReAct agent from scratch, using only Python and the Gemini API. We will implement the full cycle: defining a tool, generating thoughts, selecting actions with function calling, executing the tool, processing the observation, and orchestrating it all within a control loop.

By the end, you will have a working agent and a deep, practical understanding of the mechanics that power modern reasoning systems.

## Setup and Environment

Before we start building, let's set up our Python environment. Our goal is to ensure the notebook runs seamlessly and that your outputs match the expected traces we will analyze later. This setup involves loading API keys, importing necessary packages, and initializing the Gemini client.

1.  First, we load our `GOOGLE_API_KEY` from the `.env` file using a utility function we prepared for this course.
    
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    
    It outputs:
    
    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    ```
    
2.  Next, we import the key packages for this lesson. We will use `google-genai` to interact with the Gemini API, `pydantic` and `enum` for creating structured data models, and our own `pretty_print` utility for visualizing the agent's steps.
    
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```
    
    As we covered in Lesson 4, `pydantic` is essential for creating reliable AI systems. It allows us to define clear data schemas that act as a contract between our code and the LLM's output, ensuring type safety and runtime validation. We will use `Enum` to define a fixed set of roles for our agent's internal messages, which makes the control loop more robust and readable.
    
3.  We initialize the Gemini client, which will automatically use the API key we loaded.
    
    ```python
    client = genai.Client()
    ```
    
    It outputs:
    
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
    
4.  Finally, we define the model we will use. For this exercise, we will use `gemini-2.5-flash`, a model that is both fast and cost-effective, making it ideal for the iterative development and testing we will be doing.
    
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
    

With the client and model configured, we are ready to define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

A core part of the ReAct framework is the "Act" step, where the agent interacts with external tools to gather information or perform tasks. To keep our focus on the ReAct mechanics, we will implement a simple mock search tool instead of integrating with a real API. This approach simplifies the learning process by eliminating external dependencies and providing predictable responses for testing.

Our mock `search` tool will simulate a knowledge source. It takes a string query and returns a predefined answer if the query matches a known topic. If the query is not recognized, it returns a fallback message. This design allows us to test both successful information retrieval and how the agent handles situations where a tool fails to provide an answer.

1.  The `search` function is a standard Python function with a clear signature and a docstring. As we learned in Lesson 6, the docstring is critical because modern function-calling APIs, like Gemini's, use it to understand the tool's purpose and how to use it [[1]](https://ai.google.dev/gemini-api/docs/function-calling).
    
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
    
2.  To manage our tools, we use a `TOOL_REGISTRY`, which is a simple dictionary that maps the tool's name to its function object. This registry allows our control loop to dynamically look up and execute the correct function based on the name provided by the LLM's action plan.
    
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
    

In a production system, you would replace this mock function with a real API call. For example, a production-grade search tool might use the Google Search API, which would involve managing API keys, handling network requests with libraries like `requests`, and parsing the API's JSON response [[2]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae). You would also need to implement robust error handling for things like API rate limits, network timeouts, or invalid responses. However, for our purposes, this simple mock tool is all we need to build and test our ReAct loop.

With a tool defined, the agent now needs a way to *think* about when and how to use it.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is where the agent reasons about its goal and plans its next step. To guide this process, we need to construct a prompt that provides the LLM with all the necessary context, including the available tools and the conversation history.

1.  We start by creating a helper function, `build_tools_xml_description`, that generates a minimal XML description of our tools. We use XML tags like `<tools>` and `<tool>` because they provide clear, structured delimiters that help the model distinguish between different parts of the prompt [[12]](https://ai.google.dev/gemini-api/docs/prompting-strategies). The function iterates through our `TOOL_REGISTRY` and uses each tool's docstring as its description.
    
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
    
2.  Let's inspect the full prompt template to see what the LLM will receive. It includes general instructions, the XML block describing the `search` tool, and a placeholder for the ongoing conversation.
    
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
    
3.  Finally, we create the `generate_thought` function. This function takes the current conversation history, formats the prompt template with the necessary information, and calls the Gemini model to generate the next thought. The output is a simple string representing the agent's reasoning.
    
    ```python
    def generate_thought(conversation: str, tool_registry: dict[str, callable]) -> str:
        """Generate a thought as plain text (no structured output)."""
        tools_xml = build_tools_xml_description(tool_registry)
        prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation, tools_xml=tools_xml)
    
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return response.text.strip()
    ```
    

This thought gives the agent a plan. The next step is to translate that plan into a concrete action, which could be either calling a tool or providing a final answer to the user.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent decides what to do based on its thought process. It can either call a tool to gather more information or, if it has enough context, provide a final answer. We will implement this using Gemini's native function calling capabilities, which we first introduced in Lesson 6.

A key design choice here is to separate the prompt for the action phase from the tool definitions themselves. The action prompt focuses on high-level decision-making: "Should I use a tool or answer the user?" We do not need to include tool descriptions or signatures in this prompt because we pass the Python tool functions directly to the Gemini API through its `tools` configuration. The API automatically extracts the necessary information from the function's signature and docstring, keeping our prompt clean and focused on strategic guidance [[1]](https://ai.google.dev/gemini-api/docs/function-calling).

1.  We define two prompt templates. `PROMPT_TEMPLATE_ACTION` is the default, asking the model to choose between a tool call and a final answer. `PROMPT_TEMPLATE_ACTION_FORCED` is a special-purpose prompt we will use to force the agent to conclude when it reaches its turn limit.
    
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
    
2.  To handle the model's output, we define two Pydantic models: `ToolCallRequest` and `FinalAnswer`. This ensures that the agent's decision is always returned in a predictable, structured format that we can easily parse.
    
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
    
3.  The `generate_action` function orchestrates this phase. It selects the appropriate prompt, configures the Gemini client with the available tools, and calls the model. We set `automatic_function_calling={"disable": True}` because we want to control the execution loop ourselves. This gives us the ability to inspect the tool call, log it, and manage the observation step manually.
    
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
    
    In a production environment, if a tool execution fails, you might implement more advanced error handling. For instance, you could use a retry mechanism with exponential backoff for transient network errors or a circuit breaker pattern to prevent repeated calls to a failing service. The error message returned as an observation should be clear enough for the agent to understand the failure and potentially try a different approach [[2]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

We now have separate components for the "Thought" and "Action" phases. The next step is to build a control loop that orchestrates them in the correct sequence.

## Control Loop: Messages, Scratchpad, Orchestration

Now we build the main ReAct control loop that orchestrates the Thought → Action → Observation cycle. The core of this loop is the "scratchpad," which acts as the agent's short-term memory. It logs every step of the process—user queries, internal thoughts, tool requests, and observations—as a sequence of structured messages. This history provides the full context for the agent's reasoning at each turn.

1.  We start by defining the data structures for our messages. `MessageRole` is an `Enum` that defines the possible types of messages, and `Message` is a Pydantic model that ensures every entry in our scratchpad has a consistent structure.
    
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
    
2.  To make it easy to follow the agent's execution, we create a helper function that uses our `pretty_print` utility to render each message with a color-coded header indicating its role and the current turn.
    
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
    
3.  The `Scratchpad` class manages the list of `Message` objects. Its `append` method not only adds a new message to the history but also optionally prints it to the console, giving us a real-time trace of the agent's activity.
    
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
    
4.  Finally, we implement the `react_agent_loop` function. This is the heart of our agent. It initializes the scratchpad with the user's question and then enters a loop that executes for a maximum number of turns. In each turn, it generates a thought, generates an action, and then processes the result.
    
    If the action is a `FinalAnswer`, the loop terminates. If it is a `ToolCallRequest`, the function executes the corresponding tool from our `TOOL_REGISTRY`, captures the output as an observation, and adds it to the scratchpad. If the loop reaches its `max_turns` limit, it makes one final call to `generate_action` with `force_final=True` to ensure a graceful exit.
    
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
                tool_function = tool_registry[action_name]
                try:
                    observation_content = tool_function(**action_params)
                except Exception as e:
                    observation_content = f"Error executing tool '{action_name}': {e}"
    
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
    
    While this loop provides a clear logical flow, it introduces significant performance challenges in a production environment. The sequential dependency between LLM inference and tool execution creates a fundamental bottleneck; the GPU remains idle during I/O-bound tool calls, leading to low overall utilization. A system-level analysis of AI agents found that this idle time can be substantial, making it difficult to parallelize work within a single request [[15]](https://arxiv.org/html/2506.04301v1). This iterative process also results in a heavy-tailed latency distribution, where response times can vary widely depending on the number of turns required, a stark contrast to the more predictable latency of single-pass LLM calls [[15]](https://arxiv.org/html/2506.04301v1).
    
    This control loop is visualized in the flowchart below. It shows how the user query initiates the cycle, which then iterates between Thought, Action, and Observation, constantly updating the scratchpad until a final answer is produced or the turn limit is reached.
    
    ```mermaid
    flowchart LR
      %% ReAct Control Loop
      subgraph "ReAct Agent"
        A["User Query"] --> S["Scratchpad"]
    
        subgraph "Agent Core (LLM-driven)"
          S -- "provides context" --> T["Thought<br/>(Generate thought)"]
          T --> D{"Is Final Answer?"}
          D -- "No" --> A_ACT["Action<br/>(Select & request tool)"]
        end
    
        subgraph "External Interaction"
          A_ACT --> E_TOOL["External Environment / Tool"]
          E_TOOL --> O["Observation"]
        end
    
        O -- "add to history" --> S
        S -- "update context" --> T
    
        %% Termination Paths
        D -- "Yes" --> F_ANS["Final Answer"]
        T -. "max_turns reached" .-> F_ANS
      end
    
      %% Scratchpad Details
      subgraph "Scratchpad Content"
        M["Message Objects<br/>(USER, THOUGHT, TOOL_REQUEST,<br/>OBSERVATION, FINAL_ANSWER)"]
      end
      S -. "stores" .-> M
    
      %% Visual Styling
      classDef llm_process fill:#ccf,stroke:#333,stroke-width:2px
      class T,A_ACT llm_process
      classDef memory_store fill:#f9f,stroke:#333,stroke-width:2px
      class S memory_store
      classDef external_system fill:#ffc,stroke:#333,stroke-width:2px
      class E_TOOL external_system
      classDef final_output fill:#afa,stroke:#333,stroke-width:2px
      class F_ANS final_output
      classDef message_detail fill:#eee,stroke:#999,stroke-dasharray: 5 5
      class M message_detail
    ```
    Image 1: A flowchart illustrating the ReAct (Reasoning and Acting) control loop, showing the iterative Thought, Action, and Observation cycle, the role of the Scratchpad with various Message types, and termination conditions.
    
    We now have a complete, runnable ReAct agent. Let's test it to see how it behaves in practice.

## Tests and Traces: Success and Graceful Fallback

With the full loop implemented, we can now validate our agent's behavior. We will run two tests: a straightforward factual query to check the successful execution path, and a query that our mock tool cannot answer to verify the graceful fallback and forced termination logic. Analyzing the printed traces will confirm that each component—thought generation, action selection, tool execution, and observation—is working as designed.

### Successful Execution Trace

First, let's ask a question that our mock `search` tool is designed to answer: "What is the capital of France?". We will set `max_turns=2` and `verbose=True` to see the detailed trace.

```python
# A straightforward question requiring a search.
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The agent produces the following trace:

*   **User:** The loop starts with the initial question.
*   **Thought (Turn 1/2):** The agent correctly identifies that it needs to find the capital of France and decides the `search` tool is appropriate.
*   **Tool request (Turn 1/2):** It generates a call to `search(query='capital of France')`.
*   **Observation (Turn 1/2):** The mock tool executes and returns the predefined answer: "Paris is the capital of France...".
*   **Thought (Turn 2/2):** After observing the result, the agent concludes it has enough information to answer the user's question.
*   **Final Answer (Turn 2/2):** The agent synthesizes the observation into a direct answer: "Paris is the capital of France."

This trace confirms that the agent can successfully follow the Thought → Action → Observation cycle, use a tool to retrieve information, and provide a final answer, all within the specified turn limit.

### Graceful Fallback Trace

Now, let's test the agent's resilience. We will ask a question that our mock tool does not have a predefined answer for: "What is the capital of Italy?".

```python
# An unsupported query for our mock tool.
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

This query triggers the agent's fallback behavior:

*   **Turn 1:**
    *   **Thought:** The agent decides to search for the "capital of Italy".
    *   **Tool request:** It calls `search(query='capital of Italy')`.
    *   **Observation:** The tool returns the fallback message: "Information about 'capital of Italy' was not found."
*   **Turn 2:**
    *   **Thought:** Observing the failure, the agent adapts its strategy. It reasons that a broader search for just "Italy" might yield some useful context.
    *   **Tool request:** It calls `search(query='Italy')`.
    *   **Observation:** This search also fails, returning "Information about 'Italy' was not found."
*   **Final Answer (Forced):** Since the agent has reached the `max_turns` limit of 2, the control loop forces a final answer. The agent generates a polite response, admitting it could not find the information: "I'm sorry, but I couldn't find information about the capital of Italy."

This trace demonstrates the agent's ability to handle tool failures gracefully. It adapts its strategy after an initial failure and, when it still cannot find the answer, terminates cleanly with a helpful message instead of getting stuck in a loop. This kind of robust behavior is critical for building production-ready agents. Performance testing is particularly important for agentic systems because their iterative nature can lead to unpredictable latency under load. Unlike single-turn LLM services, ReAct agents show a sharp increase in tail latency as request volume grows. For every 1 query-per-second (QPS) increase near peak throughput, the 95th percentile latency of a ReAct agent can rise by over 17 seconds, compared to less than a second for a standard chatbot service, making load testing essential for maintaining quality of service in production [[15]](https://arxiv.org/html/2506.04301v1).

## Conclusion

In this lesson, we have moved from theory to practice by building a complete ReAct agent from scratch. We implemented each component of the Thought-Action-Observation loop, from defining a simple tool to orchestrating the entire cycle with a stateful control loop. By analyzing the execution traces, we have seen firsthand how an agent reasons, acts upon its environment, and adapts based on observations.

This hands-on exercise demystifies what happens inside agentic frameworks and gives you a solid mental model for how these systems operate. This foundational understanding is invaluable. It equips you to debug unexpected behaviors, customize agent logic for specific tasks, and extend its capabilities with new tools and more sophisticated reasoning patterns.

While our agent is minimal, it serves as a robust starting point. Building on this foundation is not just about adding features, but also about addressing the significant infrastructure challenges that arise when scaling agentic systems. These systems can introduce compute, memory, and energy overheads orders of magnitude higher than conventional LLM inference, highlighting an urgent need for more efficient architectures [[15]](https://arxiv.org/html/2506.04301v1). In the upcoming lessons, we will tackle related challenges, exploring how to add persistent memory to our agents in Lesson 9 and how to connect them to vast knowledge bases using Retrieval-Augmented Generation (RAG) in Lesson 10.

## References

- [1] Function calling. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [2] Shankar, A. (2024, June 26). Building ReAct Agents from Scratch using Gemini. Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [3] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv. https://arxiv.org/pdf/2210.03629
- [4] Bergmann, D. (n.d.). What is a ReAct agent? IBM. https://www.ibm.com/think/topics/react-agent
- [5] Stryker, C. (n.d.). What is AI agent planning? IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [6] S., E., & Zhang, B. (2024, December 19). Building effective agents. Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [7] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [8] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2026, March 6). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. arXiv. https://arxiv.org/pdf/2504.19678
- [9] Downie, A., & Finio, M. (n.d.). What is AI agent orchestration? IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [10] Iusztin, P. (2024). Building Production ReAct Agents From Scratch Is Simple. Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [11] Neradot. (2024, November 5). Building a Python React Agent Class: A Step-by-Step Guide. Neradot. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [12] Prompt design strategies. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [13] Santopaolo, G. (n.d.). Building ReAct Agents with Microsoft Agent Framework: From Theory to Production. GenMind. https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/
- [14] Schmid, P. (n.d.). ReAct agent from scratch with Gemini 2.5 and LangGraph. Phil Schmid's Blog. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [15] Kim, J., Shin, B., Chung, J., & Rhu, M. (2024). The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective. arXiv. https://arxiv.org/html/2506.04301v1