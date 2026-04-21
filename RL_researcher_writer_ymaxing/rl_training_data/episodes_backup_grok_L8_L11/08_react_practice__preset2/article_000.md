# Build a ReAct Agent From Scratch with Python and Gemini

In the last lesson, we covered the theory behind agentic planning and reasoning, focusing on the ReAct (Reason and Act) framework. We learned how agents break down complex problems by interleaving thoughts, actions, and observations. But theory only gets you so far. To truly understand how these systems work, you have to build one.

This lesson is 100% practical. We are going to implement a minimal ReAct agent from scratch using only Python and the Gemini API. We will walk through every step of the process, mirroring the code in the accompanying notebook. You will learn how to define a mock tool, generate thoughts, select actions with function calling, execute those actions, process the resulting observations, and orchestrate the entire cycle in a control loop.

Hands-on implementation provides a concrete mental model that demystifies how reasoning agents operate. By the end of this lesson, you will have a working ReAct agent that you can confidently debug, extend, and customize for your own projects.

## Setup and Environment

Before we start building, we need to set up our Python environment to ensure the code runs smoothly and the outputs match what we expect. This lesson is designed to follow a notebook, so our first step is to get the essentials in place.

1.  First, we load our `GOOGLE_API_KEY` from a `.env` file. We use a small utility function from our course repository to handle this.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from `/path/to/your/project/.env`
    Environment variables loaded successfully.
    ```
2.  Next, we import the necessary packages. We will use `google-genai` to interact with the Gemini API, `pydantic` for data modeling, and a few standard libraries for typing and enums.
    ```python
    import json
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```
3.  With our API key loaded, we can initialize the Gemini client.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
4.  Finally, we define the model we will use. Gemini offers several models, but for this lesson, we will use `gemini-2.5-flash`. It is a fast and cost-effective model, perfect for the simple reasoning and function-calling tasks we will be performing.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With the client and model ID configured, our environment is ready. Now, we can start building the first component of our agent: the tool it will use to interact with its environment.

## Tool Layer: Mock Search Implementation

As we learned in Lesson 6, tools are what give an agent the ability to take action. They are functions that allow the agent to interact with external systems, whether it is searching the web, querying a database, or calling an API. For this lesson, we will create a simple mock search tool to keep our focus on the ReAct mechanics.

Using a mock tool has several educational benefits. It simplifies the learning process by removing the need for real API keys and external dependencies. It also provides predictable, consistent responses, which is essential for testing and understanding the agent's behavior. In a production system, you could easily swap this mock function with a real API call to Google Search, Wikipedia, or any other domain-specific knowledge base without changing the agent's core logic.

1.  Let's implement our mock `search` tool. It is a simple Python function that takes a `query` string and returns a predefined response based on the query's content. The function's docstring is important, as it provides the description the LLM will use to understand what the tool does.
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
    This function simulates a search engine. If the query is about the capital of France or the ReAct framework, it returns a hardcoded, factual answer. For any other query, it returns a "not found" message. This fallback behavior is useful for testing how the agent handles failed actions.

2.  Next, we create a `TOOL_REGISTRY`. This dictionary maps the symbolic name of our tool (the function's name) to the actual Python function. This registry allows our code to safely execute the tool that the LLM selects by name.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
This simple tool layer is all our agent needs to perform its "Action" step. With the tool defined, we can now move on to the "Reason" part of the cycle: the thought phase.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is where the agent reasons about the user's query and decides what to do next. As we learned in Lesson 7, this step involves generating a natural language rationale that guides the subsequent action. We will implement this by constructing a prompt that gives the LLM the necessary context and instructions to produce a useful thought.

1.  Our prompt needs to inform the model about the tools it has available. We will create a helper function that generates a minimal XML description of our tools using their docstrings. This makes our prompt template dynamic and easy to maintain.
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
2.  Let's inspect the complete prompt template. It includes a section for available tools, a placeholder for the conversation history, and a clear instruction for the model to generate its next thought.
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
    The use of XML tags like `<tools>` and `<conversation>` is a deliberate design choice. It follows a recommended practice for prompting Gemini, which involves using clear delimiters to separate different parts of the prompt, helping the model distinguish between instructions, context, and tasks. [[1]](https://ai.google.dev/gemini-api/docs/prompting-strategies)
3.  With the prompt template defined, we create a function to generate a thought. This function takes the current conversation history, formats the prompt, and calls the Gemini API. The model's response is a plain-text paragraph representing its reasoning.
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
This function completes the "Thought" phase. The agent now has a coherent plan for its next step. A key to ensuring these thoughts remain productive is to stick with the default model temperature. For Gemini models, lowering the temperature below the default 1.0 can sometimes lead to repetitive, unhelpful reasoning loops, a common failure mode in agentic systems. [[1]](https://ai.google.dev/gemini-api/docs/prompting-strategies) The next logical phase is to translate that thought into a concrete action, which could be either calling a tool or providing a final answer to the user.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent commits to a specific course of action based on its preceding thought. This can either be a call to one of its available tools or, if it has enough information, a final answer to the user. We will use Gemini's native function calling capabilities to implement this, as it provides a more robust and reliable way to structure actions than manual text parsing.

The system prompt for the action phase focuses on high-level decision-making. We instruct the model to choose between calling a tool or providing a final answer. We also provide a separate, more direct prompt to use when we need to force a final answer, which is a useful mechanism for preventing infinite loops.

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

This direct and uncluttered approach aligns with best practices for instruction-following models. By placing the core task—choosing a tool or a final answer—at the forefront and keeping the language precise, we guide the model more effectively than with overly verbose or persuasive language. [[1]](https://ai.google.dev/gemini-api/docs/prompting-strategies)

Notice that we do not need to include tool descriptions or signatures in this prompt. When we pass the Python tool functions to the Gemini API's `tools` configuration, it automatically extracts their docstrings and parameter information. This separation of concerns keeps our prompts clean and focused on strategic guidance, while the API handles the technical details of tool integration.

1.  To handle the model's output, we define two Pydantic models: `ToolCallRequest` for when a tool is chosen, and `FinalAnswer` for when the agent is ready to conclude. These models provide the structured outputs we discussed in Lesson 4.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
2.  Now, we implement the `generate_action` function. This function is the core of the action phase.
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
    This function first checks if a final answer must be forced. If so, it uses the simpler `PROMPT_TEMPLATE_ACTION_FORCED` and returns a `FinalAnswer`. Otherwise, it sends the main action prompt along with the list of available tools to the Gemini API. We disable automatic function calling because we want to parse the model's decision and execute the tool ourselves in our control loop. The function then inspects the response: if it contains a `function_call`, it extracts the details and returns a `ToolCallRequest`; otherwise, it assumes the response is a final answer.

This robust action generation logic gives us a clear signal about the agent's intent. The final step is to orchestrate these thought and action phases within a control loop.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the engine that drives the ReAct agent, orchestrating the Thought → Action → Observation cycle. It manages the conversation history, executes actions, processes observations, and decides when to terminate. To build this, we will first define a structured way to handle messages and then implement the main loop.

1.  We start by defining the data structures for our messages. An `Enum` called `MessageRole` categorizes each message, and a Pydantic `Message` model holds the content and role. This structured approach makes it easy to track the agent's state and debug the conversation flow.
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
    This explicit categorization is critical for reliability. In agentic systems, errors in managing conversation history, such as assigning an incorrect role, can cause the agent to lose context and break its reasoning cycle. This class of error, sometimes called a "Message Fault," is why a structured scratchpad is essential. [[2]](https://arxiv.org/html/2604.08906v1)
2.  We also add a helper function to pretty-print messages, which will make our agent's traces much more readable.
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
3.  Next, we create a `Scratchpad` class. This class acts as the agent's short-term working memory. It holds a list of `Message` objects and provides a method to append new messages, with an option to print them verbosely. The `to_string` method serializes the entire history into a single string, which we will feed back into the model's context in each turn.
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
4.  Finally, we implement the `react_agent_loop` function. This is the heart of our agent.
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
    The loop begins by adding the user's question to the scratchpad. Then, for a maximum number of turns, it generates a thought and an action. If the action is a `FinalAnswer`, the loop terminates. If it is a `ToolCallRequest`, the loop executes the corresponding tool, captures the output as an "Observation," and appends it to the scratchpad. This observation becomes part of the context for the next turn. If the loop reaches its maximum number of turns, it calls `generate_action` one last time with `force_final=True` to ensure a clean exit.

This complete loop now orchestrates the entire ReAct cycle. All that is left is to test it and see our agent in action.

## Tests and Traces: Success and Graceful Fallback

With our ReAct loop fully implemented, it is time to validate its behavior. We will run two test cases: one where the agent should succeed easily and another designed to test its ability to handle failure and recover gracefully. Analyzing the output traces will give us a clear picture of how the agent thinks, acts, and observes.

1.  First, let's ask a straightforward factual question that our mock `search` tool can answer: `"What is the capital of France?"`. We will run the loop for a maximum of two turns and set `verbose=True` to see the full trace.
    ```python
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User (Turn 1/2):
    What is the capital of France?

    Thought (Turn 1/2):
    I need to find the capital of France. The user's question is a straightforward factual query. I can use the search tool to find this information.

    Tool request (Turn 1/2):
    search(query='capital of France')

    Observation (Turn 1/2):
    Paris is the capital of France and is known for the Eiffel Tower.

    Thought (Turn 2/2):
    I have found the answer to the user's question. The search tool returned that Paris is the capital of France. I can now provide the final answer.

    Final answer (Turn 2/2):
    Paris is the capital of France.
    ```
    The trace clearly shows the ReAct cycle. The agent correctly identifies the need for a search, calls the tool with the right query, processes the observation, and then concludes with the final answer, all within the two-turn limit.

2.  Now, let's test a query that our mock tool cannot handle: `"What is the capital of Italy?"`. This will test the agent's fallback behavior and the forced termination at `max_turns`.
    ```python
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User (Turn 1/2):
    What is the capital of Italy?

    Thought (Turn 1/2):
    I need to find the capital of Italy. I can use the search tool to find this information.

    Tool request (Turn 1/2):
    search(query='capital of Italy')

    Observation (Turn 1/2):
    Information about 'capital of Italy' was not found.

    Thought (Turn 2/2):
    The previous search for "capital of Italy" failed. I will try a broader search for just "Italy" to see if I can find any relevant information that might lead me to the capital.

    Tool request (Turn 2/2):
    search(query='Italy')

    Observation (Turn 2/2):
    Information about 'Italy' was not found.

    Final answer (Forced):
    I am sorry, but I was unable to find the capital of Italy using the available tools.
    ```
    This trace demonstrates the agent's resilience. After the first tool call fails, its next thought is to try a different strategy—a broader search. When that also fails and it hits the `max_turns` limit, the control loop correctly triggers the forced final answer, providing a polite and honest response.

These tests confirm that our from-scratch implementation of the ReAct loop works as expected. It can successfully solve tasks when its tools are effective and can fail gracefully and transparently when they are not.

## Conclusion

By building a ReAct agent from scratch, we have demystified the core mechanics of how these systems reason and act. We have seen how a simple loop of Thought, Action, and Observation, orchestrated with structured messages and a scratchpad for memory, can create an agent capable of tackling problems. This hands-on exercise provides a concrete mental model that frameworks often abstract away.

The principles you have implemented are foundational. In production, this simple loop can be extended into more robust patterns like orchestrator-worker systems, where a central agent delegates tasks to many specialized agents. [[3]](https://www.decodingai.com/p/stop-building-ai-agents-use-these) Furthermore, the core ReAct cycle is not limited to software; it is being adapted for embodied agents, allowing robots to use physical tools and navigate the real world by grounding their reasoning in sensor feedback. [[4]](https://cameronrwolfe.substack.com/p/ai-agents)

This foundational understanding is critical for any AI engineer. Even if you use a framework like LangGraph in production, knowing what happens under the hood allows you to debug more effectively, customize behavior with confidence, and make better architectural decisions.

In our next lesson, we will build on this foundation by exploring agent memory. We will dive into the different types of memory—procedural, episodic, and semantic—and see how they enable agents to learn from past interactions and build a more persistent understanding of their world.

## References

- [1] Prompt design strategies (https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [2] Smol Puddle: A Study of Bug Fixes in the Wild for an Agentic Framework (https://arxiv.org/html/2604.08906v1)
- [3] Stop Building AI Agents. Use These 5 Patterns Instead. (https://www.decodingai.com/p/stop-building-ai-agents-use-these)
- [4] AI Agents (Part I) (https://cameronrwolfe.substack.com/p/ai-agents)