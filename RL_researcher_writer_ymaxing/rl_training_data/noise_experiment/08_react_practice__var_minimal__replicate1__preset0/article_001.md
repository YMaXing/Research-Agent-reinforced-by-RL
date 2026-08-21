# Lesson 8: ReAct Agents From Scratch

In our previous lesson, we covered the theory behind LLM planning and reasoning, focusing on the ReAct framework. We learned how agents can break down complex problems by interleaving `Thought`, `Action`, and `Observation` steps. Abstract theory is a good start, but as engineers, we learn best by building. This lesson is 100% practical. We will build a minimal ReAct agent from scratch using only Python and the Gemini API.

We will implement the full Thought → Action → Observation loop end-to-end. This includes defining a mock tool, generating thoughts, selecting actions with function calling, executing the tool, processing observations, and orchestrating everything within a control loop. Building this simple agent gives you a concrete mental model of how these systems work. Once you understand the core mechanics, you can debug, extend, and customize agents with confidence.

Let’s get started.

## Setup and Environment

First, we need to set up our Python environment to ensure the code runs smoothly and that our outputs are reproducible. This involves loading our API keys, importing necessary libraries, and initializing the Gemini client. A consistent setup is the foundation of any reliable application, and we will follow the steps from the course notebook to get everything in place.

1.  We start by loading the necessary environment variables. Our utility function, which we have used in previous lessons, handles finding the `.env` file and loading the keys into our session.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from ...
    Environment variables loaded successfully.
    ```
2.  Next, we import the required packages. This includes `google.genai` for the Gemini API, `pydantic` for data modeling, and some utilities for pretty-printing our agent's traces to make them readable.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```
3.  We initialize the Gemini client, which is our main interface for making API requests to the model.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
4.  Finally, we define the model we will use. For this exercise, `gemini-2.5-flash` is a great choice as it is fast, cost-effective, and supports the function calling features we need.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With the client and model ready, we can now define an external tool for our agent to use.

## Tool Layer: Mock Search Implementation

Our agent needs tools to interact with the world. For this lesson, we will implement a simple mock `search` tool instead of integrating a real API. This design philosophy is intentional and offers several benefits for learning. It keeps the focus purely on the ReAct mechanics, removes the complexity of managing external dependencies and API keys, and provides predictable, deterministic responses that make it easier to test and debug our agent's logic.

Our mock tool is a simple Python function. The docstring is crucial, as modern LLM APIs use it to understand what the tool does, what its parameters are, and when to use it. This is a core concept we covered in Lesson 6 on function calling [[9]](https://ai.google.dev/gemini-api/docs/function-calling). The function simulates a search by returning predefined answers for specific queries and a fallback message for anything else.

1.  Here is the implementation of our `search` tool and the `TOOL_REGISTRY` that maps the tool's name to its function.
    ```python
    def search(query: str) -> str:
        """Search for information about a specific topic or query.

        Args:
            query (str): The search query or topic to look up.
        """
        query_lower = query.lower()

        if all(word in query_lower for word in ["capital", "france"]):
            return "Paris is the capital of France and is known for the Eiffel Tower."
        elif "react" in query_lower:
            return "The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing."

        return f"Information about '{query}' was not found."

    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
In a production system, you would replace this mock function with a real API call to a service like Google Search or a private knowledge base. However, the function signature and the way it is registered would remain the same, demonstrating the modularity of this design.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is the agent's internal monologue, where it reasons about the user's query and plans its next action [[1]](https://arxiv.org/pdf/2210.03629). We guide this process with a carefully crafted prompt template that provides the model with the necessary context to make an informed decision. This context includes the tools at its disposal and the history of the conversation so far.

1.  We create a helper function to generate an XML description of our available tools from the `TOOL_REGISTRY`. Using XML tags like `<tools>` and `<conversation>` helps the model clearly distinguish between different parts of the prompt. This description, which includes the tool's name and its docstring, will be injected into the prompt to inform the LLM about its capabilities.
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
2.  Inspecting the full prompt shows how the tool's information is embedded, giving the model a clear picture of its environment.
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
3.  The `generate_thought` function is the component that executes this phase. It takes the current conversation history, formats the prompt with the latest context, and calls the Gemini model to produce the next thought.
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
With a coherent thought generated, the agent must now decide whether to call a tool or conclude with a final answer.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent decides what to do based on its thought. We will use Gemini's native function calling capabilities to make this decision. This approach offers a significant advantage: instead of manually describing tools in the prompt, we pass the Python functions directly to the API's `tools` configuration. The Gemini client automatically extracts their signatures and docstrings, which simplifies our prompt and makes tool management cleaner and less error-prone [[9]](https://ai.google.dev/gemini-api/docs/function-calling).

This separation of concerns allows our system prompt to focus on high-level strategy—guiding the agent on *how* to think—rather than the technical details of each tool.

1.  We define two prompt templates. The first is for general use, guiding the agent to choose between a tool call and a final answer. The second is a fallback to force a final answer, which is a crucial mechanism to prevent infinite loops and ensure the agent can terminate gracefully.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are selecting the best next action to reach the user goal.

    Conversation so far:
    <conversation>
    {conversation}
    </conversation>

    Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
    """.strip()

    PROMPT_TEMPLATE_ACTION_FORCED = """
    You must now provide a final answer to the user.

    Conversation so far:
    <conversation>
    {conversation}
    </conversation>

    Provide a concise final answer that best addresses the user's goal.
    """.strip()
    ```
2.  We also define Pydantic models to represent the two possible outcomes: a `ToolCallRequest` or a `FinalAnswer`. As we discussed in Lesson 4, this brings the benefits of structured outputs, ensuring the model's response is predictable, validated, and easy to work with in our Python code.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
3.  The `generate_action` function orchestrates this phase. It sends the appropriate prompt and the list of available tools to Gemini. The model's response will either be a `function_call` object, which we parse into our `ToolCallRequest` model, or plain text, which we treat as a `FinalAnswer`. The logic handles both cases, providing a clear path for the agent's next step.
    ```python
    def generate_action(conversation: str, tool_registry: dict[str, callable] | None = None, force_final: bool = False) -> (ToolCallRequest | FinalAnswer):
        """Generate an action by passing tools to the LLM and parsing function calls or final text."""
        if force_final or not tool_registry:
            prompt = PROMPT_TEMPLATE_ACTION_FORCED.format(conversation=conversation)
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt
            )
            return FinalAnswer(text=response.text.strip())

        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)

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

        candidate = response.candidates[0]
        parts = candidate.content.parts
        if parts and getattr(parts[0], "function_call", None):
            name = parts[0].function_call.name
            args = dict(parts[0].function_call.args) if parts[0].function_call.args is not None else {}
            return ToolCallRequest(tool_name=name, arguments=args)
        
        final_answer = "".join(part.text for part in candidate.content.parts)
        return FinalAnswer(text=final_answer.strip())
    ```

## Control Loop: Messages, Scratchpad, and Orchestration

Now we build the main ReAct control loop that orchestrates the Thought → Action → Observation cycle. The conversation history, or "scratchpad," is central to this process. It allows the agent to maintain context and remember previous steps, which is essential for multi-turn reasoning [[2]](https://www.ibm.com/think/topics/react-agent). We will treat every step in the dialogue—user input, internal thoughts, tool requests, observations, and the final answer—as a structured `Message`.

1.  We start by defining the data structures to manage these messages. `MessageRole` is an `Enum` to categorize each type of interaction, and `Message` is a Pydantic model to hold the content. This structured approach is fundamental for tracking the agent's state and making the reasoning process transparent and debuggable.
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
2.  A helper function allows us to pretty-print each message with color-coding based on its role, making the agent's trace easy to follow during execution.
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
3.  The `Scratchpad` class manages the list of messages. It acts as the agent's short-term memory, providing a method to append new messages while optionally printing them for real-time monitoring.
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
4.  Finally, the `react_agent_loop` function brings everything together. It iterates through a set number of turns, defined by `max_turns`. In each turn, it generates a thought, then an action. If the action is a `ToolCallRequest`, it looks up the tool in the `TOOL_REGISTRY`, executes it, and appends the resulting observation to the scratchpad. If the tool execution fails, the error message itself becomes the observation, allowing the agent to reason about the failure. If the action is a `FinalAnswer`, the loop terminates. If the turn limit is reached, it forces a final answer to ensure a graceful exit.
    ```python
    def react_agent_loop(initial_question: str, tool_registry: dict[str, callable], max_turns: int = 5, verbose: bool = False) -> str:
        """
        Implements the main ReAct (Thought -> Action -> Observation) control loop.
        """
        scratchpad = Scratchpad(max_turns=max_turns)

        user_message = Message(role=MessageRole.USER, content=initial_question)
        scratchpad.append(user_message, verbose=verbose)

        for turn in range(1, max_turns + 1):
            scratchpad.set_turn(turn)

            thought_content = generate_thought(
                scratchpad.to_string(),
                tool_registry,
            )
            thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
            scratchpad.append(thought_message, verbose=verbose)

            action_result = generate_action(
                scratchpad.to_string(),
                tool_registry=tool_registry,
            )

            if isinstance(action_result, FinalAnswer):
                final_answer = action_result.text
                final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                scratchpad.append(final_message, verbose=verbose)
                return final_answer

            if isinstance(action_result, ToolCallRequest):
                action_name = action_result.tool_name
                action_params = action_result.arguments

                params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
                action_content = f"{action_name}({params_str})"
                action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
                scratchpad.append(action_message, verbose=verbose)

                observation_content = ""
                tool_function = tool_registry[action_name]
                try:
                    observation_content = tool_function(**action_params)
                except Exception as e:
                    observation_content = f"Error executing tool '{action_name}': {e}"

                observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
                scratchpad.append(observation_message, verbose=verbose)

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
    This loop is the engine of our ReAct agent, orchestrating the flow of reasoning, action, and learning. The diagram below illustrates this end-to-end cycle.
    
    ```mermaid
flowchart LR
  %% Start
  A["User Input"] --> B["initial_question"]
  B --> C["Add USER message to<br/>Scratchpad"]

  %% Scratchpad
  U[("Scratchpad<br/>(conversation history)")]
  C -- "stores" --> U
  ATH -- "stores" --> U
  AFA -- "stores" --> U
  ATR -- "stores" --> U
  AOB -- "stores" --> U
  GT -- "uses" --> U
  GA -- "uses" --> U

  %% Main Loop
  subgraph "ReAct Control Loop"
    D{"Loop Start"}
    C --> D

    subgraph "Thought Phase"
      GT["generate_thought"]
      PTT["PROMPT_TEMPLATE_THOUGHT"]
      T["THOUGHT"]
      ATH["Add THOUGHT to<br/>Scratchpad"]
      D --> GT
      GT -- "uses" --> PTT
      GT -- "produces" --> T
      T --> ATH
    end

    subgraph "Action Phase"
      MT{"max_turns reached?"}
      GA["generate_action"]
      PTA["PROMPT_TEMPLATE_ACTION"]
      A_OUT["Action<br/>(ToolCallRequest or FinalAnswer)"]
      IFA{"Is Action FinalAnswer?"}

      ATH --> MT
      MT -- "No" --> GA
      GA -- "uses" --> PTA
      GA -- "produces" --> A_OUT
      A_OUT --> IFA
    end

    subgraph "Tool Execution & Observation"
      ATR["Add TOOL_REQUEST to<br/>Scratchpad"]
      TE["Tool Execution<br/>(from TOOL_REGISTRY)"]
      OBS["OBSERVATION<br/>(tool's result)"]
      AOB["Add OBSERVATION to<br/>Scratchpad"]

      IFA -- "No (ToolCallRequest)" --> ATR
      ATR --> TE
      TE -- "produces" --> OBS
      OBS --> AOB
      AOB --> D
    end

    subgraph "Loop Termination"
      AFA["Add FINAL_ANSWER to<br/>Scratchpad"]
      LT["Loop Termination"]
      FA["Final Answer<br/>(return final_answer)"]

      MT -- "Yes (force_final=True)" --> AFA
      IFA -- "Yes (FinalAnswer)" --> AFA
      AFA --> LT
      LT --> FA
    end
  end

  %% Class Definitions
  classDef process stroke-width:2px
  classDef data stroke-dasharray:3,3
  classDef decision stroke-width:2px,stroke-dasharray:5,5
  classDef start_end stroke-width:3px

  class A,B,FA start_end
  class C,T,OBS,A_OUT,PTT,PTA data
  class GT,GA,TE,ATH,AFA,ATR,AOB process
  class D,MT,IFA decision
```
    Image 1: Flowchart illustrating the end-to-end ReAct control loop.

## Tests and Traces: Success and Graceful Fallback

With our agent fully implemented, it is time to test its behavior. We will use two scenarios: one where the mock tool has the answer and one where it does not. This will validate both the successful execution path and the graceful fallback mechanism, which are critical for building robust agents [[7]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

First, a simple factual question that our mock `search` tool can answer: *"What is the capital of France?"*
```python
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
The trace shows the agent working as expected. In the first turn, its `Thought` correctly identifies the need for a factual lookup. It then generates a `Tool request` for `search(query='capital of France')`. The tool returns the `Observation`: "Paris is the capital of France...". In the second turn, the agent's `Thought` process recognizes that it now has sufficient information. It then proceeds to the `Final answer`, successfully concluding the task. This confirms that the action phase correctly produces a `ToolCallRequest` and the control loop processes the observation to reach a conclusion within the turn budget.

Next, we test the fallback behavior with a query our tool cannot handle: *"What is the capital of Italy?"*
```python
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
In this trace, the agent again decides to use the search tool, but the first `Observation` is "Information about 'capital of Italy' was not found." The agent observes this failure and, in its next `Thought`, demonstrates adaptive reasoning by deciding to try a broader search for just "Italy". This also fails. Having reached its maximum of two turns, the loop triggers the forced final answer path. The agent correctly concludes, "I'm sorry, but I couldn't find information about the capital of Italy." This test validates the agent's ability to adapt its strategy based on observations and to terminate gracefully when it cannot find an answer.

## Conclusion

We have successfully built a minimal but functional ReAct agent from scratch. By implementing the Thought-Action-Observation cycle, we have gained a practical understanding of how agentic systems reason, interact with tools, and learn from their environment. This hands-on experience provides a solid foundation for building more complex and robust agents.

Even if you use a framework like LangGraph in production, knowing what happens under the hood is a core skill for any AI Engineer. This mental model is essential as you design, debug, and extend your own agentic applications. In our next lesson, we will explore how to equip agents with memory, allowing them to retain knowledge across conversations and build more sophisticated, long-term capabilities.

## References

- [1] https://arxiv.org/pdf/2210.03629
- [2] https://www.ibm.com/think/topics/react-agent
- [3] https://www.ibm.com/think/topics/ai-agent-planning
- [4] https://www.anthropic.com/engineering/building-effective-agents
- [5] https://ai.google.dev/gemini-api/docs/langgraph-example
- [6] https://arxiv.org/pdf/2504.19678
- [7] https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [8] https://www.ibm.com/think/topics/ai-agent-orchestration
- [9] https://ai.google.dev/gemini-api/docs/function-calling