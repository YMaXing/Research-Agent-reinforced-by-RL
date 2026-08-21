# Lesson 8: Building a ReAct Agent From Scratch

In our previous lessons, we have built a solid foundation in AI Engineering. We started by exploring the agent landscape, distinguished between LLM workflows and AI agents, and delved into context engineering, structured outputs, and the core ingredients of workflows. We then gave our LLMs the ability to act through tools and function calling and unpacked the theory behind the ReAct reasoning framework.

This lesson is 100% practice. We will take everything we have learned and build a minimal ReAct agent from scratch, end-to-end, using Python and the Gemini API. This hands-on implementation will follow the code from this lesson's notebook, guiding you through the full Thought → Action → Observation cycle. You will define a mock tool, generate thoughts, select actions using function calling, execute those actions, process the observations, and orchestrate it all within a turn-based control loop.

Building the ReAct loop yourself provides a concrete mental model of how these reasoning agents actually work. By the end of this lesson, you will have a working agent that you can confidently debug, extend, and customize for your own projects.

## Setup and Environment

Before we start building, let's set up our environment. A clean and consistent setup ensures that your code runs smoothly and that the outputs match the expected traces we will be analyzing later. This section will walk you through initializing the Gemini client, importing the necessary packages, and defining our model.

1.  First, we load our `GOOGLE_API_KEY` from the `.env` file. We use a custom utility function from our course library, `lessons.utils.env.load()`, which helps keep our notebooks clean and handles environment variable loading in a standardized way.
    
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    
    It outputs:
    
    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    ```
    
2.  Next, we import the key packages for this lesson. We will be using `google-genai` to interact with the Gemini API. For data modeling, we will use `pydantic` and Python's built-in `enum` and `typing` modules. We also import `pretty_print`, another custom utility for displaying our agent's outputs in a readable format.
    
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```
    
    Using `pydantic` is a best practice for production agent development. As we covered in Lesson 4, it allows us to define strict data schemas for our inputs and outputs. This creates a formal contract with the LLM and provides runtime validation, ensuring that the data flowing through our agent is always in the expected format. `Enum` is used here to define a fixed set of roles for our messages (e.g., `USER`, `THOUGHT`), making our code more readable and preventing typos.
    
3.  We initialize the Gemini client. The client will automatically use the API key we loaded earlier.
    
    ```python
    client = genai.Client()
    ```
    
    It outputs:
    
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
    
4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is fast and cost-effective, making it ideal for development and simpler tasks.
    
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
    

With our client and model configured, we are ready to define the external capabilities our agent will use.

## Tool Layer: Mock Search Implementation

Our ReAct agent needs tools to interact with the world. As we learned in Lesson 6, tools are functions that allow the agent to perform actions beyond its internal knowledge, such as searching the web or querying a database. For this lesson, we will implement a mock search tool that serves as a simplified external knowledge source.

We use a mock tool instead of a real API for a few important reasons. First, it simplifies the learning process by allowing us to focus purely on the ReAct mechanics without worrying about external dependencies, API keys, or network issues. Second, it provides predictable, consistent responses, which is essential for testing and debugging our agent's logic.

1.  Here is the implementation of our mock `search` function from the notebook. It takes a string query and returns a predefined string response if the query matches certain keywords.
    
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
    
    Notice the docstring. As we will see in the Action phase, modern LLM APIs like Gemini automatically parse the function's docstring and signature to understand what the tool does and what arguments it expects. A clear and descriptive docstring is crucial for the model to select the right tool for the job.
    
2.  We also create a `TOOL_REGISTRY`, which is a simple Python dictionary that maps the tool's name to the actual function. This registry allows our agent to dynamically look up and execute the correct function based on the name provided by the LLM.
    
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
    

In a production system, you would replace this mock `search` function with a real one that calls an external API, like the Google Search API or a private knowledge base. This would involve handling API key authentication, managing network requests, and parsing the API's response. For example, a production-grade search tool would likely include `try-except` blocks to handle connection errors or timeouts, and it might return a structured error message to the agent if the search fails. This allows the agent to reason about the failure and potentially retry or choose a different tool [[4]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

This design also highlights a key system-level challenge: resource utilization. The agent's control loop will often interleave GPU-bound LLM calls with I/O-bound tool calls like this one. While the `search` function runs, the GPU remains idle, leading to significant underutilization. In production, this makes inter-request batching and concurrent execution essential for maintaining high throughput [[16]](https://arxiv.org/html/2506.04301v1).

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct loop is "Thought." This is where the agent analyzes the user's query and the conversation history to decide on the best next step. It formulates a plan, which might involve using a tool or answering the user directly. We will now implement the thought generation phase.

1.  First, we need a way to inform the LLM about the tools it has at its disposal. We create a helper function, `build_tools_xml_description`, that converts our `TOOL_REGISTRY` into a simple XML format.
    
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
    ```
    
    We use XML tags like `<tools>` and `<tool>` because they provide clear, structured delimiters that help the model distinguish between different parts of the prompt, a recommended practice for improving instruction following [[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies).
    
2.  Next, we define the prompt template for the thought phase. This template instructs the agent on its goal, provides the list of available tools in the XML format we just created, and includes a placeholder for the conversation history.
    
    ```python
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
    
    Let's inspect the final prompt that will be sent to the model.
    
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
    
    As you can see, the prompt clearly outlines the agent's task, lists the `search` tool with its description, and sets up a section for the ongoing conversation.
    
3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt template with the tool descriptions and conversation, and calls the Gemini API to generate the next thought. The function then returns the model's response as a clean text string.
    
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
    

With a coherent thought generated, the agent must now decide whether to call a tool or conclude with a final answer. This brings us to the "Action" phase.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent translates its thought into a concrete action. This could be calling a tool to gather more information or providing a final answer to the user. We will implement this using Gemini's native function calling capabilities, which we covered in Lesson 6.

A key design choice here is the separation of concerns. The prompt for the action phase focuses on high-level decision-making: *should I use a tool or answer now?* It does not need to include the technical details of the tools.

This is because we pass the tool definitions directly to the Gemini API through its `tools` configuration. The Gemini client automatically parses our Python `search` function, extracting its name, docstring (as the description), and parameter information from the type hints. This information is then incorporated into the model's context behind the scenes. This approach keeps our prompts clean and makes it easy to manage our tools, as we only need to update the Python function itself.

1.  First, we define two prompt templates for the action phase. The main template guides the model to choose between a tool call and a final answer. We also have a dedicated template to force a final answer, which will be useful for gracefully terminating the agent's loop.
    
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
    
2.  We define our Pydantic models for the two possible outcomes: a `ToolCallRequest` or a `FinalAnswer`. This use of structured outputs, which we discussed in Lesson 4, ensures that the model's decision is returned in a predictable and parsable format.
    
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
    
3.  Now we implement the `generate_action` function. This function is the core of the action phase.
    
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
    
    Let's break down what's happening here. The function first checks the `force_final` flag. If `True`, it uses the dedicated "forced" prompt and returns a `FinalAnswer`. This is our mechanism to ensure the agent can terminate cleanly, for example, if it reaches a maximum number of steps. This is a simple but effective strategy to prevent infinite loops, a common failure mode in production agents [[4]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).
    
    If not forcing a final answer, it formats the standard action prompt and configures the Gemini client with the available tools. We set `automatic_function_calling={"disable": True}` because we want to parse the tool call ourselves and manage the execution loop manually. The function then inspects the model's response. If it contains a `function_call` object, it parses the tool name and arguments into our `ToolCallRequest` Pydantic model. If not, it assumes the response is a text-based final answer and wraps it in our `FinalAnswer` model.
    
    In a production setting, handling tool execution failures is critical. If a tool fails (e.g., an API is down), you would typically implement retry mechanisms with exponential backoff or circuit breakers. The tool function itself should catch exceptions and return an informative error message. The agent can then observe this error message in the next turn and decide on a different course of action, such as trying a different tool or informing the user of the failure [[14]](https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/).
    

## Control Loop: Messages, Scratchpad, and Orchestration

Now we have all the pieces: a way to think, a way to act, and a tool to use. The final step is to orchestrate them in the main ReAct control loop that runs the complete Thought → Action → Observation cycle.

The core of this orchestration is the "scratchpad," which acts as the agent's short-term working memory. It's a log of everything that has happened in the current session: the user's initial query, the agent's internal thoughts, the tools it decided to call, and the observations it received from those calls. At each step, the entire scratchpad is fed back to the LLM, providing the full context it needs to decide what to do next.

1.  We start by defining the data structures for our messages and scratchpad. `MessageRole` is an `Enum` that defines the different types of messages in our loop. The `Message` class is a Pydantic model that holds the content and role for each entry in our conversation history.
    
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
    
2.  We add a helper function, `pretty_print_message`, to render each message in a readable, color-coded format. This will make it much easier to trace the agent's execution and debug its behavior.
    
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
    
3.  The `Scratchpad` class manages the list of messages. Its `append` method not only adds a new message to the history but also optionally prints it using our pretty-printing utility. This provides a real-time trace of the agent's state.
    
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
    
    While simple, this growing history has significant memory implications at scale. Each turn appends more tokens to the context, which increases the size of the Key-Value (KV) cache stored in GPU memory for each request. This makes memory optimization a critical concern for production agent systems [[16]](https://arxiv.org/html/2506.04301v1).
    
4.  Finally, we implement the `react_agent_loop` function. This is the heart of our agent. It initializes the scratchpad, then enters a loop that runs for a maximum number of turns.
    
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
    
    Inside the loop, it first calls `generate_thought` to get the agent's plan. Then, it calls `generate_action`. If the action is a `FinalAnswer`, the loop breaks and returns the answer. If it's a `ToolCallRequest`, the loop finds the corresponding function in the `tool_registry`, executes it, and captures the output as an "Observation." This observation is added to the scratchpad, and the loop continues to the next turn. If the loop reaches `max_turns`, it makes one final call to `generate_action` with `force_final=True` to ensure a graceful exit.
    
    This sequential dependency between LLM inference (thought and action) and tool execution (observation) is a fundamental performance bottleneck. The agent cannot think about the next step until the current tool call completes, limiting opportunities for parallelism within a single request. System-level optimizations like prefix caching, which reuses computations for the shared parts of the growing context, are crucial for mitigating this latency in production [[16]](https://arxiv.org/html/2506.04301v1).
    
    This entire process is illustrated in the flowchart below, which shows the iterative cycle of thought, action, and observation, the central role of the scratchpad, and the termination conditions.
    
    ```mermaid
flowchart LR
  %% Start
  UserQuery["User Query"]

  %% Memory
  subgraph Memory["Agent Memory"]
    Scratchpad["Scratchpad<br/>(Conversation History)"]
    MessageTypes["Message Types:<br/>USER, THOUGHT, TOOL_REQUEST, OBSERVATION, FINAL_ANSWER"]
  end

  %% ReAct Agent Loop
  subgraph ReActAgent["ReAct Agent Loop"]
    Thought["Thought<br/>(LLM generates thought)"]
    MaxTurnsCheck{"Max Turns Reached?"}
    IsFinalAnswer{"Is Final Answer?"}
    Action["Action<br/>(LLM selects & requests tool)"]
  end

  %% External Environment
  subgraph External["External Environment"]
    ExternalEnv["External Environment / Tool"]
  end

  %% Outputs
  FinalAnswer["Final Answer"]
  ForcedFinalAnswer["Forced Final Answer"]

  %% Primary Flow
  UserQuery -- "initiates" --> Thought
  Thought --> MaxTurnsCheck
  MaxTurnsCheck -- "No" --> IsFinalAnswer
  MaxTurnsCheck -- "Yes" --> ForcedFinalAnswer

  IsFinalAnswer -- "Yes" --> FinalAnswer
  IsFinalAnswer -- "No" --> Action
  Action -- "executes" --> ExternalEnv
  ExternalEnv -- "produces" --> Observation["Observation"]
  Observation --> Thought

  %% Scratchpad Interactions
  UserQuery -- "adds to" --> Scratchpad
  Thought -- "reads & updates" --> Scratchpad
  Action -- "adds Tool Request to" --> Scratchpad
  Observation -- "adds to" --> Scratchpad
  FinalAnswer -- "uses" --> Scratchpad
  ForcedFinalAnswer -- "uses" --> Scratchpad
```
    
    Image 1: A flowchart illustrating the complete ReAct (Reasoning and Acting) control loop, emphasizing the iterative Thought → Action → Observation cycle, the role of the Scratchpad, and forced termination via max_turns.
    

## Tests and Traces: Success and Graceful Fallback

With our complete ReAct loop implemented, the final step is to test it. By running a couple of example queries and analyzing the output traces, we can validate that each component—thought, action, observation, and loop control—is working as expected.

### Successful Factual Lookup

First, let's test the agent with a straightforward factual question that our mock `search` tool is designed to handle. We will set `max_turns=2` and `verbose=True` to see the detailed trace.

1.  We ask a question that our mock tool knows the answer to.
    
    ```python
    # A straightforward question requiring a search.
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    
    It outputs:
    
    ```text
    --------------------------------------------------------------------------------
    | User (Turn 1/2):                                                             |
    |------------------------------------------------------------------------------|
    | What is the capital of France?                                               |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Thought (Turn 1/2):                                                          |
    |------------------------------------------------------------------------------|
    | The user is asking for the capital of France. I can use the search tool to   |
    | find this information.                                                       |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Tool request (Turn 1/2):                                                     |
    |------------------------------------------------------------------------------|
    | search(query='capital of France')                                            |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Observation (Turn 1/2):                                                      |
    |------------------------------------------------------------------------------|
    | Paris is the capital of France and is known for the Eiffel Tower.            |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Thought (Turn 2/2):                                                          |
    |------------------------------------------------------------------------------|
    | The search tool provided the answer: Paris is the capital of France. I can   |
    | now provide the final answer to the user.                                    |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Final answer (Turn 2/2):                                                     |
    |------------------------------------------------------------------------------|
    | Paris is the capital of France.                                              |
    --------------------------------------------------------------------------------
    ```
    
    The trace shows the ReAct loop working perfectly. In Turn 1, the agent thinks about the query, correctly decides to use the `search` tool, and executes it. It receives the observation that "Paris is the capital of France." In Turn 2, its thought process acknowledges that it has the answer, and it proceeds to generate the `FinalAnswer`, successfully completing the task within the turn limit.
    

### Graceful Fallback on Unknown Query

Now, let's test the agent's resilience. We will ask a question that our mock tool does not have a predefined answer for. This will test the agent's ability to handle a "not found" observation and demonstrate the forced termination logic.

1.  We ask a question that will trigger the fallback response from our mock tool.
    
    ```python
    # An unsupported query for the mock tool.
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    
    It outputs:
    
    ```text
    --------------------------------------------------------------------------------
    | User (Turn 1/2):                                                             |
    |------------------------------------------------------------------------------|
    | What is the capital of Italy?                                                |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Thought (Turn 1/2):                                                          |
    |------------------------------------------------------------------------------|
    | The user is asking for the capital of Italy. I will use the search tool to   |
    | find this information.                                                       |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Tool request (Turn 1/2):                                                     |
    |------------------------------------------------------------------------------|
    | search(query='capital of Italy')                                             |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Observation (Turn 1/2):                                                      |
    |------------------------------------------------------------------------------|
    | Information about 'capital of Italy' was not found.                          |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Thought (Turn 2/2):                                                          |
    |------------------------------------------------------------------------------|
    | The initial search for "capital of Italy" failed. I will try a broader       |
    | search for just "Italy" to see if I can find any relevant information that   |
    | might lead me to the capital.                                                |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Tool request (Turn 2/2):                                                     |
    |------------------------------------------------------------------------------|
    | search(query='Italy')                                                        |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Observation (Turn 2/2):                                                      |
    |------------------------------------------------------------------------------|
    | Information about 'Italy' was not found.                                     |
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    | Final answer (Forced):                                                       |
    |------------------------------------------------------------------------------|
    | I'm sorry, but I couldn't find information about the capital of Italy.       |
    --------------------------------------------------------------------------------
    ```
    
    This trace demonstrates the agent's adaptability and our control loop's robustness. In Turn 1, the agent observes that the search failed. In its next thought (Turn 2), it adapts its strategy by trying a broader query. When that also fails, the agent reaches the `max_turns` limit. Our loop then correctly calls `generate_action` with `force_final=True`, resulting in a polite, "forced" final answer admitting it could not find the information. This confirms that our end-to-end implementation handles both success and failure gracefully.
    
    This forced termination mechanism is a simple safeguard, but tuning the `max_turns` parameter in a production environment involves a careful trade-off. A higher limit may improve accuracy on complex tasks, but research shows it often leads to diminishing returns while disproportionately increasing tail latency for difficult queries [[16]](https://arxiv.org/html/2506.04301v1). In traditional software engineering, this is analogous to unit and integration testing. A comprehensive test suite for a production agent would include many more cases: edge cases, adversarial prompts, and performance benchmarks to measure the system's heavy-tailed latency distribution and overall cost [[3]](https://arxiv.org/pdf/2504.19678).
    

These tests confirm that our from-scratch ReAct agent is fully functional. We have successfully built a system that can reason, act, observe, and adapt, providing a solid foundation for building more complex and capable agents in future lessons.

## Conclusion

In this lesson, we have moved from theory to practice, building a complete ReAct agent from the ground up. By implementing each component—the tools, the thought and action phases, and the orchestrating control loop—we have gained a practical understanding of how these agentic systems operate. We have seen how to guide an LLM's reasoning with structured prompts, how to leverage function calling for actions, and how to manage the state of a conversation using a scratchpad.

This hands-on experience is what separates production-grade AI engineering from simple prototyping. Even though frameworks can abstract away this complexity, knowing what happens under the hood is essential for debugging, optimizing, and extending your agents. The mental model you have built today will be invaluable as we move on to more advanced topics. Scaling these agentic loops to production, however, introduces serious system-level challenges in latency, resource utilization, and cost [[16]](https://arxiv.org/html/2506.04301v1). In our next lesson, we will explore how to give agents memory, allowing them to learn and build context across multiple conversations.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. https://arxiv.org/pdf/2210.03629
- [2] Google. (n.d.). *Prompt design strategies*. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [3] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review*. https://arxiv.org/pdf/2504.19678
- [4] Shankar, A. (2024). *Building ReAct Agents from Scratch using Gemini*. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [5] IBM. (n.d.). *What is a ReAct agent?* https://www.ibm.com/think/topics/react-agent
- [6] IBM. (n.d.). *What is AI agent planning?* https://www.ibm.com/think/topics/ai-agent-planning
- [7] S., E., & Zhang, B. (2024). *Building effective agents*. https://www.anthropic.com/engineering/building-effective-agents
- [8] Google. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://ai.google.dev/gemini-api/docs/langgraph-example
- [9] IBM. (n.d.). *What is AI agent orchestration?* https://www.ibm.com/think/topics/ai-agent-orchestration
- [10] Google. (n.d.). *Function calling*. https://ai.google.dev/gemini-api/docs/function-calling
- [11] Iusztin, P. (2024). *Building Production ReAct Agents From Scratch Is Simple*. https://www.decodingai.com/p/building-production-react-agents
- [12] Neradot. (2024). *Building a Python React Agent Class: A Step-by-Step Guide*. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [13] Schmid, P. (2024). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [14] Santopaolo, G. (2024). *Building ReAct Agents with Microsoft Agent Framework: From Theory to Production*. https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/
- [15] towardsai. (n.d.). *course-ai-agents/notebook.ipynb at dev · towardsai/course-ai-agents*. https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb
- [16] Kim, J., Shin, B., Chung, J., & Rhu, M. (2025). *The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective*. https://arxiv.org/html/2506.04301v1