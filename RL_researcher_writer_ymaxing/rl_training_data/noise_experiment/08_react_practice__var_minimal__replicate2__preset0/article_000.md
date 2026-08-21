# Building a ReAct Agent From Scratch in Pure Python

In our previous lessons, we covered the theoretical foundations of AI agents. We explored the agent landscape, distinguished between LLM workflows and autonomous agents, learned about context engineering, structured outputs, and agent tools. In Lesson 7, we dove into the ReAct framework, understanding how agents can synergize reasoning and acting to solve complex problems.

Theory is essential, but there is no substitute for building. To truly understand how these systems work, you need to implement them yourself. Frameworks like LangGraph are powerful, but their abstractions can sometimes hide the core mechanics. By building a ReAct agent from scratch, you gain a concrete mental model that demystifies how agents think, act, and learn from their environment.

This lesson is 100% practical. We will walk you through building a minimal, end-to-end ReAct agent using only Python and the Gemini API. We will implement the full Thought → Action → Observation loop, from defining a tool to orchestrating the agent's control flow. This hands-on experience is what separates production-grade AI engineering from building prototypes.

Let's get started.

## Setup and Environment

First, we need to set up our Python environment to ensure the code runs smoothly. This involves loading our API keys, importing the necessary libraries, and initializing the Gemini client. Our goal is to create a reproducible setup that you can follow along with in the course notebook.

1.  We begin by loading our Google API key from an environment file. We use a simple utility function for this, which is a good practice for keeping secrets out of your code.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from .../.env
    Environment variables loaded successfully.
    ```
2.  Next, we import the required packages. We will use `google-genai` to interact with the Gemini API, `pydantic` for data validation, and a few standard Python libraries.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```
3.  We initialize the Gemini client, which will be our main interface for making API calls.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is a fast and cost-effective choice for tasks that do not require extensive reasoning.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model ID in place, our environment is ready. The next step is to give our agent a capability—an external tool it can use to interact with the world.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to use tools. For this lesson, we will create a simple mock search tool instead of integrating a real API. This approach has several educational benefits: it keeps the focus purely on the ReAct mechanics, removes the need for external API keys, and provides predictable, deterministic responses, which is ideal for testing and learning.

1.  Our mock `search` function is a simple Python function that returns predefined answers for specific queries. Notice the docstring, which clearly describes what the tool does and its arguments. As we will see later, this documentation is crucial because the LLM uses it to understand how and when to use the tool.
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
2.  We then create a `TOOL_REGISTRY`, a dictionary that maps the tool's name to its function. This registry allows our agent to dynamically look up and execute the correct tool based on the name provided by the LLM.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

In a production system, you would replace this mock function with a real API call to a service like Google Search or a domain-specific knowledge base. However, the interface would remain the same: a function that takes a query and returns a string. This modular design makes it easy to swap tools without changing the agent's core logic.

With a tool defined, the agent now needs a way to reason about when to use it. This brings us to the "Thought" phase of the ReAct cycle.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is where the agent formulates its internal monologue. It analyzes the user's query and its past actions to decide on the next best step. We guide this process with a carefully crafted prompt template that tells the LLM how to think.

1.  First, we create a function to generate an XML description of our available tools. We also define the prompt template, which includes placeholders for the tool descriptions and the ongoing conversation history. Using XML tags like `<tools>` and `<conversation>` helps the model clearly distinguish between different parts of the context.
    ```python
    def build_tools_xml_description(tools: dict[str, callable]) -> str:
        # ... function implementation ...

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
2.  Let's inspect the final prompt that the LLM will see. It clearly lists the `search` tool and its description, providing the necessary context for the model to reason about its capabilities.
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
3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt template, and calls the Gemini API to generate the next thought. The function simply returns the model's raw text response.
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

This thought generation gives the agent a plan. The next step is to translate that plan into a concrete action, which could be calling a tool or providing the final answer to the user.

## Action Phase: Function Calling and Parsing

In the "Action" phase, the agent commits to a specific action. We use Gemini's native function calling feature for this. Instead of manually describing tools in the prompt, we pass the Python function objects directly to the API. The model then decides whether to call one of these functions or to respond with a final answer. This separation of concerns—strategic guidance in the prompt, technical details in the tool configuration—leads to cleaner and more maintainable code.

1.  We define two prompt templates. The first is for general action selection, and the second is a specialized prompt to force a final answer, which is useful for ensuring the agent terminates gracefully.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are selecting the best next action to reach the user goal.

    Conversation so far:
    <conversation>
    {conversation}
    </conversation>

    Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
    """.strip()

    PROMPT_TEMPLATE_ACTION_FORCED = # ... similar structure
    ```
2.  We define Pydantic models to represent the two possible outcomes: a `ToolCallRequest` or a `FinalAnswer`. This provides a structured way to handle the model's output.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
3.  The `generate_action` function orchestrates this phase. It selects the appropriate prompt, configures the Gemini API with the available tools, and calls the model. Crucially, we set `automatic_function_calling={"disable": True}` so we can parse the response and execute the tool ourselves, giving us full control.
    ```python
    def generate_action(conversation: str, tool_registry: dict[str, callable] | None = None, force_final: bool = False) -> (ToolCallRequest | FinalAnswer):
        # ...
        # Use a dedicated prompt when forcing a final answer
        if force_final or not tool_registry:
            # ...
            return FinalAnswer(text=response.text.strip())

        # Default action prompt
        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)

        # Provide available tools to the model
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

        # Extract the function call from the response
        parts = response.candidates[0].content.parts
        if parts and getattr(parts[0], "function_call", None):
            name = parts[0].function_call.name
            args = dict(parts[0].function_call.args) if parts[0].function_call.args is not None else {}
            return ToolCallRequest(tool_name=name, arguments=args)
        
        # Otherwise, it's a final answer
        final_answer = "".join(part.text for part in parts)
        return FinalAnswer(text=final_answer.strip())
    ```

The `force_final` flag is an important control mechanism. In a loop, we need a way to prevent the agent from running forever. By setting a maximum number of turns, we can use this flag to instruct the model to conclude and provide the best possible answer with the information it has.

Now that we have implemented the "Thought" and "Action" phases, it is time to combine them into a coherent control loop.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the heart of the ReAct agent. It orchestrates the Thought → Action → Observation cycle, manages the conversation history, and handles tool execution. We will build this loop around a structured message system and a "scratchpad" that serves as the agent's working memory.

1.  First, we define the structure for our messages. An `Enum` called `MessageRole` categorizes each message (e.g., `USER`, `THOUGHT`, `TOOL_REQUEST`), and a `Message` Pydantic model holds the content and role. This structured approach is key to tracking the agent's state.
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
        role: MessageRole
        content: str
    ```
2.  We create a `Scratchpad` class to manage the list of messages. It provides an `append` method to add new messages and a `to_string` method to format the entire history into a single string for the LLM's context. We also include a pretty-printing utility to make the traces easier to read during debugging.
    ```python
    def pretty_print_message(message: Message, turn: int, max_turns: int, ...):
        # ... utility to print messages with colors ...

    class Scratchpad:
        """Container for ReAct messages with optional pretty-print on append."""
        def __init__(self, max_turns: int):
            self.messages: List[Message] = []
            self.max_turns = max_turns
            self.current_turn = 1
        
        def append(self, message: Message, verbose: bool = False, ...):
            # ... appends message and optionally prints it ...

        def to_string(self) -> str:
            return "\n".join(str(m) for m in self.messages)
    ```
3.  The `react_agent_loop` function brings everything together. It initializes the scratchpad with the user's question and then iterates through a fixed number of turns. In each turn, it generates a thought, selects an action, and processes the outcome.
    ```python
    def react_agent_loop(initial_question: str, tool_registry: dict[str, callable], max_turns: int = 5, verbose: bool = False) -> str:
        """
        Implements the main ReAct (Thought -> Action -> Observation) control loop.
        """
        scratchpad = Scratchpad(max_turns=max_turns)
        scratchpad.append(Message(role=MessageRole.USER, content=initial_question), verbose=verbose)

        for turn in range(1, max_turns + 1):
            scratchpad.set_turn(turn)

            # 1. Thought Phase
            thought_content = generate_thought(scratchpad.to_string(), tool_registry)
            scratchpad.append(Message(role=MessageRole.THOUGHT, content=thought_content), verbose=verbose)

            # 2. Action Phase
            action_result = generate_action(scratchpad.to_string(), tool_registry=tool_registry)

            if isinstance(action_result, FinalAnswer):
                scratchpad.append(Message(role=MessageRole.FINAL_ANSWER, content=action_result.text), verbose=verbose)
                return action_result.text

            if isinstance(action_result, ToolCallRequest):
                # ... format tool call ...
                scratchpad.append(Message(role=MessageRole.TOOL_REQUEST, content=action_content), verbose=verbose)

                # 3. Observation Phase
                try:
                    tool_function = tool_registry[action_result.tool_name]
                    observation_content = tool_function(**action_result.arguments)
                except Exception as e:
                    observation_content = f"Error executing tool '{action_result.tool_name}': {e}"
                
                scratchpad.append(Message(role=MessageRole.OBSERVATION, content=observation_content), verbose=verbose)

        # Force a final answer if max turns are reached
        forced_action = generate_action(scratchpad.to_string(), force_final=True)
        # ... handle and return forced final answer ...
    ```

The logic for integrated observation processing is a key part of this loop. When a `ToolCallRequest` is generated, the loop looks up the tool in our `TOOL_REGISTRY`, executes it, and captures the output. This output, whether successful or an error, is formatted as an `OBSERVATION` message and added to the scratchpad. This feedback mechanism is what allows the agent to learn from its actions and adjust its strategy in the next turn.

```mermaid
flowchart LR
  %% Start of the ReAct Control Loop
  A["User Query"]

  %% Core Agent Components
  subgraph "ReAct Agent Loop"
    B_scratchpad[(Scratchpad<br/>(Conversation History))]
    C_thought["Generate Thought<br/>(LLM Reasoning)"]
    D_action_select{"Action Selection<br/>(Tool Call or Final Answer)"}
    E_tool_request["Action: Tool Call<br/>(MessageRole: Tool Request)"]
    F_execute_tool["Execute Tool"]
    G_observation["Observation Processing<br/>(MessageRole: Observation)"]
    H_integrate["Integrate Observation<br/>into Scratchpad"]
    I_final_answer["Action: Final Answer<br/>(MessageRole: Final Answer)"]
    J_terminate{"Termination Check<br/>(Final Answer or Max Turns)"}
    K_max_turns["Max Turns Reached"]
  end

  %% Error Handling for Tool Execution
  subgraph "Tool Execution Error Handling"
    L_tool_fail["Tool Execution Failure"]
    M_unknown_tool["Unknown Tool Name"]
  end

  %% End of the Process
  N["End"]

  %% Primary Flow Connections
  A -- "initiates loop with" --> C_thought
  C_thought -- "uses context from" --> B_scratchpad
  B_scratchpad -- "provides history to" --> C_thought

  C_thought -- "produces" --> D_action_select

  D_action_select -- "if Tool Call" --> E_tool_request
  E_tool_request -- "triggers" --> F_execute_tool

  F_execute_tool -- "on success" --> G_observation
  F_execute_tool -- "on failure" --> L_tool_fail
  F_execute_tool -- "on unknown tool" --> M_unknown_tool

  L_tool_fail -- "generates" --> G_observation
  M_unknown_tool -- "generates" --> G_observation

  G_observation -- "results in" --> H_integrate
  H_integrate -- "updates" --> B_scratchpad

  %% Iterative Loop
  H_integrate -. "informs next iteration" .-> C_thought

  D_action_select -- "if Final Answer" --> I_final_answer
  I_final_answer -- "triggers" --> J_terminate

  J_terminate -- "if Final Answer" --> N
  J_terminate -- "if Max Turns" --> K_max_turns
  K_max_turns -- "ends process" --> N

  %% Visual Grouping
  classDef message_type
  class E_tool_request,G_observation,I_final_answer message_type

  classDef scratchpad_memory stroke-dasharray:3,3
  class B_scratchpad scratchpad_memory

  classDef decision_point
  class D_action_select,J_terminate decision_point

  classDef error_handling
  class L_tool_fail,M_unknown_tool error_handling
```
Image 1: A flowchart illustrating the ReAct control loop, showing the iterative Thought, Action, and Observation cycle, including error handling and termination conditions.

This complete loop provides a solid foundation for our agent. Now, let's test it to see how it behaves in practice.

## Tests and Traces: Success and Graceful Fallback

With the control loop in place, we can validate the agent's end-to-end behavior. We will run two tests: a straightforward factual query to verify the success path, and a query our mock tool cannot answer to test its graceful fallback mechanism.

First, let's ask a question our mock tool knows the answer to.
```python
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
The trace shows the agent working as expected. In the first turn, it thinks about the query, decides to use the `search` tool, and executes it. After observing the correct answer ("Paris is the capital of France..."), it proceeds to the second turn. In this turn, its thought process confirms it has the answer, and it generates a `FinalAnswer` action, successfully terminating the loop within the two-turn budget.

Next, we will test the fallback behavior with a query that is not in our mock tool's predefined responses.
```python
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
This trace demonstrates the agent's resilience. In the first turn, it correctly calls the `search` tool, but the observation is "Information about 'capital of Italy' was not found." The agent recognizes this failure and, in its second thought, formulates a new strategy: a broader search for just "Italy." This also fails. Having reached the `max_turns` limit, the control loop triggers the forced final answer mechanism. The agent then provides a polite and honest response, admitting it could not find the information. This confirms that our loop correctly handles tool failures and terminates gracefully.

These two tests validate that our from-scratch implementation of the ReAct loop is working correctly, providing a solid foundation for building more complex agents.

## Conclusion

In this lesson, we moved from theory to practice by building a minimal ReAct agent from scratch. We implemented the complete Thought-Action-Observation cycle in pure Python, giving us a transparent and controllable system. We defined tools, generated thoughts, selected actions using function calling, and orchestrated the entire process within a stateful control loop.

This hands-on approach provides a deep, intuitive understanding of how agentic systems operate. Even if you ultimately use a framework like LangGraph in production, knowing what happens under the hood is invaluable for debugging, customization, and building robust AI applications.

This is just the beginning. In our upcoming lessons, we will build upon this foundation. We will explore how to equip agents with long-term memory in Lesson 9, dive deep into Retrieval-Augmented Generation (RAG) in Lesson 10, and learn how to process multimodal data in Lesson 11.

## References

- [1] [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)
- [2] [ReAct Agent - IBM](https://www.ibm.com/think/topics/react-agent)
- [3] [AI Agent Planning - IBM](https://www.ibm.com/think/topics/ai-agent-planning)
- [4] [Building effective agents - Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [5] [ReAct agent from scratch with Gemini 2.5 and LangGraph](https://ai.google.dev/gemini-api/docs/langgraph-example)
- [6] [From LLM Reasoning to Autonomous AI Agents - ArXiv](https://arxiv.org/pdf/2504.19678)
- [7] [Building ReAct Agents from Scratch using Gemini - Medium](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [8] [AI Agent Orchestration - IBM](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [9] [Gemini Function Calling Documentation](https://ai.google.dev/gemini-api/docs/function-calling)