# Building a ReAct Agent From Scratch

In our previous lessons, we moved from the high-level concepts of AI agents to the practical mechanics of planning and tool use. We explored the ReAct framework, a powerful paradigm that enables an LLM to reason, act, and observe, much like a human solving a problem step-by-step [[15]](https://arxiv.org/pdf/2210.03629). While theory is essential, nothing builds engineering intuition like getting your hands dirty. Abstract diagrams of agent loops can only take you so far.

This lesson is where we bridge that gap. We are leaving the theory behind to build a minimal, end-to-end ReAct agent from scratch using only Python and the Gemini API. We will implement the full Thought → Action → Observation cycle: defining a mock tool, generating thoughts, selecting actions with function calling, executing those actions, and orchestrating the entire process within a control loop.

By building this system yourself, you will gain a concrete mental model of how these agents work under the hood. This hands-on experience is what separates a prototype from a production-ready system. Once you understand the core loop, you can debug, extend, and customize agents with confidence.

```mermaid
flowchart LR
  %% Start of the ReAct Agent Design
  UQ["User Query"] --> LLM["LLM"]

  %% ReAct Cycle: Thought-Action-Observation
  LLM -- "generates thought & decides" --> A["Action"]
  A -- "executed via" --> T["Tool"]
  T -- "interacts with" --> EE["External Environment"]
  EE -- "returns" --> O["Observation"]
  O -- "informs" --> LLM

  %% Decision Point
  LLM -- "evaluates progress" --> D{"Done?"}
  D -- "Yes" --> FA["Final Answer"]
  D -- "No" --> LLM

  %% Visual Grouping
  classDef core_process stroke-width:2px
  classDef external_interface stroke-dasharray:3,3
  class LLM,A,O,D core_process
  class UQ,T,EE,FA external_interface
```
Image 1: A flowchart illustrating the core theoretical ReAct (Reasoning and Acting) agent design, showing the iterative Thought-Action-Observation cycle.

Throughout this lesson, we will follow the code from the associated Jupyter Notebook. We will cover:
- Setting up the Python environment.
- Implementing a mock tool layer.
- Constructing the thought and action phases.
- Building the main control loop.
- Testing the agent with success and failure cases.

## Setup and Environment

Before we can build our agent, we need to set up a clean and predictable environment. This ensures that our code runs smoothly and that the outputs match the expected traces, which is critical for debugging and validation. We will follow the first few cells of the notebook to get everything in place.

1.  First, we load our `GOOGLE_API_KEY` from a `.env` file. We use a custom utility for this, but you can use any method you prefer.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from `/path/to/your/.env`
    Environment variables loaded successfully.
    ```
2.  Next, we import the necessary packages. We will use `google-genai` to interact with the Gemini API, `pydantic` for data modeling, and some standard Python libraries like `enum` and `typing`.
    ```python
    import json
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```
3.  We initialize the Gemini client. If you have both `GOOGLE_API_KEY` and `GEMINI_API_KEY` set, the client will prioritize one, which is normal behavior.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
4.  Finally, we define the model ID we will use. For this lesson, `gemini-2.5-flash` is a great choice because it is fast, cost-effective, and supports the function calling features we need.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With our client initialized and model selected, we have a stable foundation. The next step is to give our agent a capability—a tool it can use to interact with the world.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to use tools to gather information or perform actions [[25]](https://www.anthropic.com/engineering/building-effective-agents). In a production system, these tools might be complex API calls to a search engine, a database, or an internal service. For this lesson, however, our goal is to understand the ReAct mechanics, not to wrestle with external APIs.

That is why we will implement a simple mock `search` tool. This approach offers several advantages for learning:
-   **Focus:** It keeps our attention on the agent's reasoning loop, not on API authentication or network requests.
-   **Simplicity:** It removes external dependencies, so you do not need extra API keys to run the code.
-   **Predictability:** It provides consistent, hardcoded responses, which makes testing and debugging the agent's behavior much easier.

1.  Our mock `search` function simulates a real search engine. It takes a string `query` and returns a string response. The docstring is crucial, as it provides the description the LLM will use to understand what the tool does and how to use it.
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
    The function checks for specific keywords in the query and returns a predefined answer. If the query does not match any of our conditions, it returns a generic "not found" message. This fallback behavior is important for testing how the agent handles situations where a tool fails to provide useful information.

2.  To manage our tools, we create a `TOOL_REGISTRY`. This dictionary maps the tool's name (as a string) to its actual Python function. This registry acts as a bridge, allowing the LLM to plan with symbolic tool names (`"search"`) while our code can safely look up and execute the corresponding function.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
In a real-world application, you could easily swap this mock `search` function with a function that calls the Google Search API or queries a private knowledge base, all without changing the agent's core logic. The key is to maintain the same function signature and ensure the docstring accurately describes its purpose.

With our tool defined, the agent now has a way to "act." The next step is to implement the "reasoning" part of the cycle: the thought phase.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is where the agent analyzes the user's query and its history to decide on the best next step. It is a moment of internal reasoning before any action is taken. To generate this thought, we need to provide the LLM with the right context, including a description of the tools it has available.

1.  We will start by creating a function that generates a minimal XML description of our tools. This function iterates through our `TOOL_REGISTRY` and uses each tool's docstring to create a `<tool>` block. XML is a great choice for this because it provides a clear, structured format that helps the LLM distinguish tool definitions from other parts of the prompt [[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies).
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
2.  Next, we define the prompt template for the thought phase. This template instructs the agent on its goal: to decide the next best step. It includes placeholders for the available tools (as an XML block) and the conversation history.
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
3.  Printing the template reveals the full context we will send to the model. It clearly outlines the available `search` tool and leaves a placeholder for the ongoing conversation.
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
4.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt with the tool descriptions, and calls the Gemini API. It returns the model's response as a clean, stripped string. This string represents the agent's "thought."
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
With a coherent thought generated, the agent now has a plan. But a plan is useless without execution. The next phase, "Action," determines whether to call a tool or conclude with a final answer.

## Action Phase: Function Calling and Parsing

After the "Thought" phase, the agent must decide what to do next. This is the "Action" phase, where it either calls a tool to gather more information or, if it has enough context, provides a final answer to the user. We will use Gemini's native function calling capabilities to handle this decision-making process.

A key design choice here is to separate the prompts for thought and action. The thought prompt includes detailed tool descriptions to help the LLM reason about *what* tools are available and *why* one might be useful. In contrast, the action prompt is more focused on the high-level decision: *should I use a tool or answer now?*

We do not need to include tool signatures in the action prompt because we pass the Python tool functions directly to the Gemini API via its `tools` configuration. The API automatically handles converting the function's signature and docstring into a format the model can understand [[27]](https://ai.google.dev/gemini-api/docs/function-calling). This separation keeps our prompts clean and makes tool management much easier.

1.  We start by defining two prompt templates for the action phase. The first is the default prompt, and the second is a specialized version used to force a final answer. We need this forced-answer prompt to ensure the agent can terminate gracefully, for example, when it reaches a turn limit.
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
2.  Next, we define two Pydantic models, `ToolCallRequest` and `FinalAnswer`, to represent the two possible outcomes of the action phase. Using Pydantic ensures our outputs are structured and validated, as we learned in Lesson 4.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
3.  Now we implement the `generate_action` function. This is the core of the action phase.
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
            config=config,
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
    This function first checks if a final answer is being forced. If so, it uses the `PROMPT_TEMPLATE_ACTION_FORCED` and returns a `FinalAnswer`. Otherwise, it uses the default prompt and configures the Gemini client with the available tools. We set `automatic_function_calling={"disable": True}` because we want to parse the response and execute the tool ourselves, giving us full control.

    The function then inspects the model's response. If it contains a `function_call` object, it extracts the tool name and arguments and returns a `ToolCallRequest`. If not, it assumes the response is a text-based final answer and returns a `FinalAnswer`. This dual-return logic is what allows the agent to decide between acting and concluding.

With the thought and action phases defined, we now have all the components needed to build the main control loop that will orchestrate the entire ReAct cycle.

## Control Loop: Messages, Scratchpad, and Orchestration

Now we arrive at the heart of our agent: the control loop. This is where we orchestrate the Thought → Action → Observation cycle, managing the flow of information and making decisions turn by turn. A key component of this loop is the "scratchpad," which serves as the agent's short-term memory, recording every step of the interaction.

To build a clean and traceable history, we first need a structured way to represent each message.

1.  We will start by defining a `MessageRole` enum and a `Message` Pydantic model. This creates a unified structure for all types of interactions: user queries, agent thoughts, tool requests, tool outputs (observations), and final answers.
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
2.  To make the agent's process easy to follow, we create a helper function to pretty-print messages in the notebook. This will give us a color-coded, readable trace of the agent's execution.
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
3.  Next, we define the `Scratchpad` class. This class manages a list of `Message` objects. Its `append` method not only stores a new message but also optionally prints it, giving us a real-time view of the agent's state. The `to_string` method serializes the entire history into a single string, which we will pass to the LLM in each turn.
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
4.  Finally, we implement the `react_agent_loop`. This function ties everything together.
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
    The loop works as follows:
    - It starts by adding the user's initial question to the scratchpad.
    - In each turn, it first calls `generate_thought` to reason about the current state.
    - Then, it calls `generate_action` to decide on the next move.
    - If the action is a `FinalAnswer`, the loop terminates and returns the answer.
    - If it is a `ToolCallRequest`, the loop looks up the tool in the `tool_registry`, executes it, and captures the output as an "Observation." This observation is added to the scratchpad, and the loop continues to the next turn.
    - If the loop reaches the `max_turns` limit, it makes one final call to `generate_action` with `force_final=True` to ensure a graceful exit.

This control loop is the engine of our agent. It systematically progresses through the ReAct cycle, building up context and moving closer to a solution with each iteration.

```mermaid
flowchart LR
    start_node["_start_"] --> llm_node["LLM Node"]

    llm_node -- "continue" --> tools_node["Tools Node"]
    llm_node -- "end" --> end_node["_end_"]

    tools_node --> llm_node
```
Image 2: A flowchart illustrating the control flow of a ReAct agent implemented using LangGraph.

## Tests and Traces: Success and Graceful Fallback

With our agent fully implemented, it is time to test it. By analyzing the execution traces, we can validate that the complete Thought-Action-Observation cycle works as designed. We will run two tests: one straightforward query to check for a successful run, and one unsupported query to verify the agent's graceful fallback behavior.

### Successful Execution Trace

First, let's ask a simple factual question that our mock `search` tool can answer: "What is the capital of France?". We will set `max_turns=2` and `verbose=True` to see the detailed trace.

1.  We call our main loop function with the question.
    ```python
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
2.  The output trace shows the agent's step-by-step process:
    -   **User (Turn 1/2):** The initial question is logged.
    -   **Thought (Turn 1/2):** The agent correctly reasons that it needs to find the capital of France and decides to use the search tool.
    -   **Tool request (Turn 1/2):** It generates a call to `search(query='capital of France')`.
    -   **Observation (Turn 1/2):** The mock tool returns the predefined answer: "Paris is the capital of France...".
    -   **Thought (Turn 2/2):** With the observation in its context, the agent recognizes it has the answer and plans to deliver it.
    -   **Final Answer (Turn 2/2):** The agent provides the correct final answer, "Paris is the capital of France."

This trace confirms that our agent can successfully follow the ReAct loop: it reasons about the query, selects and executes the correct tool, observes the result, and uses that observation to formulate a final answer, all within the specified turn limit.

### Graceful Fallback Trace

Now, let's test a query that our mock tool cannot handle: "What is the capital of Italy?". This will test the agent's ability to adapt when a tool fails and to terminate gracefully when it hits the turn limit.

1.  We run the loop with the new question.
    ```python
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
2.  The trace reveals a different path:
    -   **Thought (Turn 1/2) & Tool request (Turn 1/2):** The agent correctly identifies the need to search for "capital of Italy" and calls the search tool.
    -   **Observation (Turn 1/2):** The tool returns the fallback message: "Information about 'capital of Italy' was not found."
    -   **Thought (Turn 2/2):** Seeing the failure, the agent adapts its strategy. It decides to try a broader search for just "Italy," hoping to find the capital that way.
    -   **Tool request (Turn 2/2):** It calls `search(query='Italy')`.
    -   **Observation (Turn 2/2):** This also fails, returning "Information about 'Italy' was not found."
    -   **Final Answer (Forced):** The agent has now reached its `max_turns` limit of 2. The control loop triggers a forced final answer. The agent apologizes and states that it could not find the information.

This test demonstrates the robustness of our implementation. The agent can handle tool failures by reasoning about them and adjusting its plan. More importantly, the `max_turns` limit and the `force_final` mechanism work as an effective safety net, preventing infinite loops and ensuring the agent always provides a response, even if it is an admission of failure.

These tests confirm that our from-scratch implementation of the ReAct loop is not only functional but also resilient, providing a solid foundation for building more complex and capable agents.

## Conclusion

In this lesson, we have moved from theory to practice, building a complete, albeit minimal, ReAct agent from scratch. By implementing each component of the Thought-Action-Observation loop, we have demystified the "magic" behind agentic systems. We have seen how a structured combination of prompting, function calling, and state management allows an LLM to reason, act on its environment, and learn from the results.

This hands-on approach provides a concrete mental model that is invaluable for any AI engineer. You now have a working control loop that you can extend with more sophisticated tools, more complex reasoning patterns, and, as we will see in future lessons, a persistent memory. This foundation is not just an academic exercise; it is the core skill required to build reliable, debuggable, and production-ready AI agents.

This lesson is part of our journey through the foundations of AI agents. Having mastered the core ReAct loop, you are now prepared for the upcoming topics:
-   In Lesson 9, we will dive into **Agent Memory**, exploring how agents can retain information across sessions to provide personalized and context-aware interactions.
-   In Lesson 10, we will take a deep dive into **Retrieval-Augmented Generation (RAG)**, connecting our agents to vast external knowledge bases.

## References

- [1] ReAct: Synergizing Reasoning and Acting in Language Models. (n.d.). arXiv. https://arxiv.org/pdf/2210.03629
- [2] Prompt design strategies. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [3] Building ReAct Agents from Scratch using Gemini. (n.d.). Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] Building a Python React Agent Class: A Step-by-Step Guide. (2024, November 5). Neradot. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [5] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [6] Building ReAct Agents with LangGraph: A Beginner’s Guide. (2024, July 1). Machine Learning Mastery. https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/
- [7] Implementing ReAct Agentic Pattern From Scratch. (n.d.). Daily Dose of DS. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [8] ReAct agent with structured output. (n.d.). LangChain. https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/
- [9] Building Production ReAct Agents From Scratch Is Simple. (2025, November 18). Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [10] AI Agent Planning. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [11] Beyond the prompt: engineering the thought-action-observation loop. (n.d.). Towards AI. https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2
- [12] AI Agents IV: AI Agents through the Thought-Action-Observation (TAO) Cycle. (n.d.). Stackademic. https://blog.stackademic.com/ai-agents-iv-ai-agents-through-the-thought-action-observation-tao-cycle-3dfe2eb76629
- [13] Agent steps and structure. (n.d.). Hugging Face. https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure
- [14] DataCamp Handout. (n.d.). DataCamp. https://projector-video-pdf-converter.datacamp.com/42942/chapter2.pdf
- [15] ReAct: Synergizing Reasoning and Acting in Language Models. (n.d.). arXiv. https://arxiv.org/pdf/2210.03629
- [16] ReAct Agent. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [17] AI Agent Planning. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [18] Building effective agents. (2024, December 19). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [19] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [20] From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. (n.d.). arXiv. https://arxiv.org/pdf/2504.19678
- [21] Building ReAct Agents from Scratch using Gemini. (n.d.). Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [22] AI Agent Orchestration. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [23] Gemini Function Calling Documentation. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [24] Building Production ReAct Agents From Scratch Is Simple. (2025, November 18). Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [25] Building effective agents. (2024, December 19). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [26] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [27] Gemini Function Calling Documentation. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling