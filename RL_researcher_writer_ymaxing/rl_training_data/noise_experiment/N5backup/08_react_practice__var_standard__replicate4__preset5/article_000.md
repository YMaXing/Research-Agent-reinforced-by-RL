# Lesson 8: Build a ReAct Agent From Scratch

In our previous lesson, we explored the theory behind ReAct, a key evolutionary step that moved agentic systems from simple prompt-based interactions to structured reasoning [[1]](https://servicesground.com/blog/agentic-reasoning-patterns/). We saw how it enables an LLM to synergize reasoning and acting by following a "Thought-Action-Observation" cycle. Theory is a great start, but as engineers, our goal is to build things that work. The best way to build a deep mental model of how agents operate is to get our hands dirty and implement one from the ground up.

While frameworks like LangGraph can accelerate development, they often introduce abstractions that hide the core mechanics or add complexity to simple logic. Understanding how to build the ReAct loop from scratch is a core skill for an AI Engineer, giving you the ability to debug, customize, and build robust, production-ready systems without being overly reliant on any single framework [[2]](https://www.decodingai.com/p/building-production-react-agents).

This lesson is 100% practical. We will walk you through building a minimal, end-to-end ReAct agent using only Python and the Gemini API. You will implement the complete loop: defining a mock tool for the agent to use, generating thoughts to guide its decisions, selecting actions with function calling, executing those actions, and processing the resulting observations. By the end, you will have a working control loop that you can extend, debug, and customize with confidence.

Let's get started.

## Setup and Environment

Our first step is to set up a clean and reproducible Python environment. This ensures that the code runs smoothly and that your outputs match the traces we will analyze later in the lesson.

1.  We begin by loading our `GOOGLE_API_KEY` from a `.env` file using a small utility function we prepared for this course.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from `.../.env`
    Environment variables loaded successfully.
    ```

2.  Next, we import the key packages we will need. This includes `google.genai` for interacting with the Gemini API, `pydantic` for data validation, and some standard Python libraries like `enum` and `typing`. We also import a `pretty_print` utility to make our agent's traces easier to read.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client, which is our main interface to the API.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is both fast and cost-effective, making it ideal for our simple examples.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model in place, we can now define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

In Lesson 6, we learned how to give agents tools to interact with the outside world. Here, we will implement a simple mock `search` tool. Instead of making real API calls to Google or Wikipedia, this tool will return predefined, predictable responses.

This approach has several educational benefits. It simplifies our implementation by removing the need for external dependencies and API keys, allowing us to focus entirely on the ReAct mechanics. It also ensures our tests are deterministic, which is essential for learning and debugging. In a production setting, you could easily swap this mock function with a real API call to a search engine or a domain-specific knowledge base, preserving the same function signature and integration pattern [[3]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae), [[4]](https://atalupadhyay.wordpress.com/2025/11/25/building-a-real-time-web-searching-ai-agent-with-langchain-and-google-gemini/).

1.  Let's implement our mock `search` tool. The function takes a `query` string and returns a predefined answer if the query matches certain keywords. If no specific response is found, it returns a generic "not found" message. Notice the docstring, which clearly describes what the function does and its arguments. As we saw in Lesson 6, this documentation is what the LLM will use to understand when and how to use the tool.
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

2.  To manage our tools, we create a `TOOL_REGISTRY`. This dictionary maps the symbolic tool name to the actual Python function. This allows the agent to plan using the name "search", while our code can safely resolve that name to the `search` function for execution.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

Now that our agent has a tool, it needs a way to reason about when to use it. This brings us to the first step of the ReAct cycle: the Thought phase.

## Thought Phase: Prompt Construction and Generation

The goal of the Thought phase is to produce a short, purposeful piece of reasoning that guides the agent's next step. The agent analyzes the user's query and its conversation history to decide what to do next.

1.  We start by creating a function to build a minimal XML description of our available tools. As we discussed in Lesson 3 on Context Engineering, using XML tags helps the model distinguish between different types of information in the prompt. This function takes our `TOOL_REGISTRY` and generates an XML block containing each tool's name and its docstring.
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

2.  Next, we define the prompt template for the Thought phase. This prompt instructs the agent on its goal: to decide the next best step. It includes placeholders for the dynamically generated `<tools>` XML block and the ongoing `<conversation>` history.
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

3.  Let's inspect the full prompt to see what the model receives.
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
    As you can see, the prompt clearly lists the `search` tool and its description, providing the LLM with all the necessary context to reason about its capabilities. While this prompt is sufficient for our simple example, production-grade agents often require more sophisticated prompt engineering to improve reasoning quality. Techniques like explicitly instructing the model to "think step-by-step" or adding "guardrails" that constrain its behavior (e.g., "Reply with 'I’m not sure' if you don’t know the answer") can help minimize hallucinations and guide the agent toward more reliable thought generation [[5]](https://www.appsmith.com/blog/de-hallucinate-ai-agents).

4.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt template, calls the Gemini API, and returns the model's generated thought as a clean string.
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

With a coherent thought in hand, the agent must now decide whether to call a tool or conclude with a final answer. This is the Action phase.

## Action Phase: Function Calling and Parsing

The Action phase is where the agent commits to a specific step. It can either be a tool call or a final answer to the user. We will use Gemini's native function calling capabilities, which we covered in Lesson 6, to implement this. This is a more reliable approach than asking the model to generate JSON and parsing it manually [[6]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent).

One key difference from the Thought phase is that we do not need to manually include tool descriptions in the prompt. Instead, we pass the Python tool functions directly to the Gemini API via the `tools` parameter in the configuration. The client automatically extracts their signatures and docstrings, making them available to the model for function calling. This separation of concerns keeps our action prompt clean and focused on strategic guidance.

Image 1: A sequence diagram illustrating Gemini's function calling process.

1.  First, we define two prompt templates. `PROMPT_TEMPLATE_ACTION` is the default prompt that asks the model to choose between a tool call and a final answer. `PROMPT_TEMPLATE_ACTION_FORCED` is a special-purpose prompt we will use later to ensure the agent provides a final answer when it reaches its turn limit.
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

2.  Next, we define Pydantic models to represent the two possible outcomes of the action phase: a `ToolCallRequest` or a `FinalAnswer`. As we learned in Lesson 4 on Structured Outputs, using Pydantic models gives us robust data validation and a clear, type-safe contract for our outputs. This pattern of using a structured model for the final output is both powerful and flexible. In fact, some frameworks formalize this by treating the desired output schema as a special tool that the agent "calls" when it has gathered enough information. This approach, sometimes called a `ToolStrategy`, allows structured data to be extracted reliably from any model that supports function calling [[7]](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/).
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  Now, we implement the `generate_action` function. This function is the core of the action phase.
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
    Here is a breakdown of its logic:
    - It checks a `force_final` flag. If `True`, it uses the forced-answer prompt and returns a `FinalAnswer`. This is our mechanism for gracefully terminating the agent's loop.
    - Otherwise, it passes the list of tools from our `TOOL_REGISTRY` to the `GenerateContentConfig`. We set `automatic_function_calling={"disable": True}` because we want to parse the tool call ourselves and maintain full control over the execution loop.
    - It then inspects the model's response. If a `function_call` object is present, it extracts the tool name and arguments and returns a `ToolCallRequest`.
    - If there is no function call, it assumes the model has generated a final answer and returns a `FinalAnswer` object containing the response text.

We now have all the individual components of the ReAct cycle. The final step is to orchestrate them in a control loop.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the engine that drives the agent, orchestrating the Thought → Action → Observation cycle from end to end. It manages the conversation history, executes tools, processes observations, and decides when to terminate.

Image 2: A flowchart illustrating the ReAct control loop, emphasizing the iterative Thought-Action-Observation cycle and its termination conditions, including a conceptual Scratchpad.

### Message and Scratchpad Design

To keep track of the agent's state, we will treat the entire interaction as a sequence of messages. Each message represents a step in the dialogue, whether it is from the user, an internal thought from the agent, a tool request, or a tool's observation. Maintaining this conversation history is one of the most critical challenges in building multi-turn agents. Without a complete and accurate record of past interactions—thoughts, actions, and observations—an agent quickly loses context, leading to repetitive or irrelevant responses. The scratchpad serves as the agent's short-term memory, ensuring that its reasoning in the current turn is grounded in the full history of what has happened so far [[8]](https://codesignal.com/learn/courses/coordinating-openai-agents-workflows-in-typescript/lessons/building-multi-turn-conversations-with-openai-agents-in-typescript).

1.  We start by defining an `Enum` for the different message roles and a Pydantic `Message` model to hold the content. This structured approach makes it easy to log and review the agent's entire reasoning process.
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

2.  We also create a small helper function to pretty-print each message, which will help us visualize the agent's trace during execution.
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

3.  The `Scratchpad` class acts as our agent's short-term memory. It is a simple container for a list of `Message` objects. It provides an `append` method to both store new messages and optionally print them. At each turn, the entire scratchpad is serialized into a string and fed back into the model's context.
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

### The Orchestration Loop

With the memory structures in place, we can now implement the main control loop. The `react_agent_loop` function orchestrates the entire process.

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

Here is a turn-by-turn breakdown:

1.  **Initialization:** The loop starts by adding the user's initial question to the scratchpad.
2.  **Thought Generation:** In each turn, it calls `generate_thought`, passing the entire conversation history. The resulting thought is appended to the scratchpad.
3.  **Action Generation:** It then calls `generate_action`.
4.  **Action Handling:**
    - If the action is a `FinalAnswer`, the loop terminates, and the answer is returned.
    - If it is a `ToolCallRequest`, the loop identifies the correct tool from the `TOOL_REGISTRY` and executes it with the provided arguments. The tool's output, our observation, is captured. A `try-except` block handles potential errors during tool execution.
5.  **Observation Processing:** The observation is formatted as a message and appended to the scratchpad. This closes the loop, and the next turn begins with this new information in the context.
6.  **Termination:** If the loop reaches the `max_turns` limit, it calls `generate_action` one last time with `force_final=True`. This instructs the model to summarize its findings and provide the best possible answer with the information it has, preventing infinite loops.

This complete implementation gives us a minimal but fully functional ReAct agent. It is worth noting that while our loop executes one tool at a time, more advanced orchestrators can run multiple tool calls in parallel to reduce latency, a key optimization for production systems [[2]](https://www.decodingai.com/p/building-production-react-agents). Now, let's test it.

## Tests and Traces: Success and Graceful Fallback

To validate our agent, we will run two tests. Before we dive into the traces, it is helpful to frame our analysis. The quality of an agent can be measured with both **outcome metrics** (e.g., Was the final answer correct?) and **process metrics** (e.g., Did the agent choose the right tools? Was its reasoning path efficient?). For this lesson, we will focus on analyzing the process metrics revealed in the agent's trace to understand its behavior [[9]](https://www.braintrust.dev/articles/evaluate-agents-new-models-gemini-3). The first test is a straightforward factual question that our mock tool can answer. The second is a query that the tool cannot handle, which will test the agent's ability to adapt and terminate gracefully.

1.  Let's start with a simple question: "What is the capital of France?". We will run the agent for a maximum of two turns and set `verbose=True` to see the full trace.
    ```python
    # A straightforward question requiring a search.
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User (Turn 1/2):
    What is the capital of France?

    Thought (Turn 1/2):
    The user is asking for the capital of France. I can use the search tool to find this information.

    Tool request (Turn 1/2):
    search(query='capital of France')

    Observation (Turn 1/2):
    Paris is the capital of France and is known for the Eiffel Tower.

    Thought (Turn 2/2):
    The search tool provided the answer directly. I can now provide the final answer.

    Final answer (Turn 2/2):
    Paris is the capital of France.
    ```
    The trace shows the agent behaving exactly as expected. It correctly identifies the need for information, calls the `search` tool, processes the observation, and provides the final answer, all within the turn limit.

2.  Now, let's try a query our mock tool does not have a predefined answer for: "What is the capital of Italy?".
    ```python
    # An unsupported question to test fallback behavior.
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User (Turn 1/2):
    What is the capital of Italy?

    Thought (Turn 1/2):
    The user is asking for the capital of Italy. I will use the search tool to find this information.

    Tool request (Turn 1/2):
    search(query='capital of Italy')

    Observation (Turn 1/2):
    Information about 'capital of Italy' was not found.

    Thought (Turn 2/2):
    The previous search for "capital of Italy" failed. I will try a broader search for just "Italy" to see if I can find the capital that way.

    Tool request (Turn 2/2):
    search(query='Italy')

    Observation (Turn 2/2):
    Information about 'Italy' was not found.

    Final answer (Forced):
    I'm sorry, but I was unable to find the capital of Italy using the available tools.
    ```
    This trace demonstrates the agent's resilience. After the first tool call fails, it does not give up. Instead, its next thought reflects a new strategy: broadening the search query. When that also fails and it hits the `max_turns` limit, the forced final answer mechanism kicks in, and the agent provides a helpful, honest response acknowledging its limitations. This forced termination is a simple but crucial safeguard against common failure modes, such as getting stuck in an infinite loop by repeatedly trying the same failed action [[2]](https://www.decodingai.com/p/building-production-react-agents).

These tests confirm that our end-to-end loop is working correctly. We have built a solid foundation for more complex agents.

## Conclusion

In this lesson, we moved from theory to practice and built a complete, albeit minimal, ReAct agent from scratch. We implemented every component of the Thought-Action-Observation loop, from defining tools and generating reasoning steps to orchestrating the entire cycle in a stateful control loop. By building it ourselves, we have gained a concrete mental model of how these systems operate under the hood.

This hands-on experience is what separates production-grade AI from prototypes. The simple loop we constructed today is the foundational pattern for more advanced agentic systems seen in the real world, from financial agents that analyze live market data to sophisticated customer service bots that interact with multiple APIs [[10]](https://www.salesforce.com/ap/agentforce/ai-agents/react-agents/). In future lessons, we will build upon this foundation, exploring how to equip agents with sophisticated memory (Lesson 9), enhance their knowledge with Retrieval-Augmented Generation (Lesson 10), and enable them to process multimodal data (Lesson 11).

## References

- [1] Agentic reasoning patterns. (n.d.). https://servicesground.com/blog/agentic-reasoning-patterns/
- [2] Building Production-Ready ReAct Agents from Scratch. (n.d.). Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [3] Shankar, A. (2024, June 18). Building ReAct Agents from Scratch using Gemini. Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] Building a real-time web searching AI Agent with LangChain and Google Gemini. (2025, November 25). https://atalupadhyay.wordpress.com/2025/11/25/building-a-real-time-web-searching-ai-agent-with-langchain-and-google-gemini/
- [5] De-Hallucinate AI Agents. (n.d.). Appsmith. https://www.appsmith.com/blog/de-hallucinate-ai-agents
- [6] Schmid, P. (2025). ReAct agent from scratch with Gemini 2.5 and LangGraph. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [7] ReAct agent with structured output. (n.d.). LangChain. https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/
- [8] Building Multi-Turn Conversations with OpenAI Agents in TypeScript. (n.d.). CodeSignal. https://codesignal.com/learn/courses/coordinating-openai-agents-workflows-in-typescript/lessons/building-multi-turn-conversations-with-openai-agents-in-typescript
- [9] Evaluate agents with new models like Gemini 3. (n.d.). Braintrust. https://www.braintrust.dev/articles/evaluate-agents-new-models-gemini-3
- [10] What Are ReAct Agents? (n.d.). Salesforce. https://www.salesforce.com/ap/agentforce/ai-agents/react-agents/
- [11] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv. https://arxiv.org/pdf/2210.03629
- [12] ReAct Agent. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [13] AI Agent Planning. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [14] Roelants, P. (n.d.). Implement a simple ReAct Agent using OpenAI function calling. https://peterroelants.github.io/posts/react-openai-function-calling/
- [15] Function calling. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [16] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [17] Building a Python React Agent Class: A Step-by-Step Guide. (n.d.). https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [18] Building effective agents. (2024, December 19). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [19] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2026). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. arXiv. https://arxiv.org/pdf/2504.19678
- [20] Lu, Y., Liu, S., & Dong, L. (2025). OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs. arXiv. https://arxiv.org/html/2510.24663v1
- [21] AI Agent Orchestration. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [22] Course AI Agents Notebook for Lesson 8. (n.d.). GitHub. https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb
- [23] Building ReAct Agents with Microsoft Agent Framework: From Theory to Production. (n.d.). https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/
- [24] Implement ReAct (Agentic Pattern) from scratch. (n.d.). https://blog.dailydoseofds.com/p/implement-react-agentic-pattern-from
- [25] LangChain ReAct Agent: Complete Implementation Guide with Working Examples (2025). (n.d.). https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025
- [26] AI Agents Crash Course (Part 10 - with implementation). (n.d.). https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [27] Beyond the Prompt: Engineering the Thought-Action-Observation Loop. (n.d.). Towards AI. https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2
- [28] Building ReAct Agents with LangGraph: A Beginner’s Guide. (n.d.). Machine Learning Mastery. https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/
- [29] Prompting strategies. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [30] AI Agents (IV): AI Agents through the Thought-Action-Observation (TAO) Cycle. (n.d.). Stackademic. https://blog.stackademic.com/ai-agents-iv-ai-agents-through-the-thought-action-observation-tao-cycle-3dfe2eb76629
- [31] Agent steps and structure. (n.d.). Hugging Face. https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure
- [32] DataCamp material from Hugging Face Agents Course. (n.d.). https://projector-video-pdf-converter.datacamp.com/42942/chapter2.pdf
- [33] Real-world agent examples with Gemini 3. (n.d.). Google Developers Blog. https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/
- [34] Converting a ReAct prompt to use function calling. (n.d.). OpenAI Community Forum. https://community.openai.com/t/converting-a-react-prompt-to-use-function-calling/264914
- [35] Thinking. (n.d.). Google Cloud. https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking
- [36] Using Gemini with OpenAI Agents SDK. (n.d.). OpenAI Community Forum. https://community.openai.com/t/using-gemini-with-openai-agents-sdk/1307262
- [37] Build an AI coding agent with Python and Gemini. (n.d.). freeCodeCamp.org. https://www.freecodecamp.org/news/build-an-ai-coding-agent-with-python-and-gemini/
- [38] OrchDAG: Complex Tool Orchestration in Multi-turn Interactions with Plan DAGs. (n.d.). Amazon Science. https://www.amazon.science/publications/orchdag-complex-tool-orchestration-in-multi-turn-interactions-with-plan-dags