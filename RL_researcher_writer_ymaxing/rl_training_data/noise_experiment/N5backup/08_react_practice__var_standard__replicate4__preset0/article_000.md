# Building a ReAct Agent From Scratch: A Step-by-Step Guide

In our previous lessons, we’ve covered the theoretical foundations of AI agents, from context engineering and structured outputs to tools and planning. We explored the ReAct framework, which enables LLMs to reason, act, and observe, solving complex problems by interacting with external environments [[1]](https://arxiv.org/pdf/2210.03629). Now, it’s time to move from theory to practice.

This lesson is 100% hands-on. We will build a minimal ReAct agent from the ground up using only Python and the Gemini API. By implementing the complete Thought → Action → Observation loop yourself, you will gain a concrete mental model of how these systems work. This hands-on experience is what separates a theoretical understanding from the practical skills needed to build, debug, and extend agents with confidence.

We will walk through the entire process, step-by-step, following the code in the associated notebook. You will learn to:
- Define a mock tool and a tool registry.
- Generate "thoughts" to guide the agent’s reasoning.
- Use function calling to select and parse actions.
- Execute tools and process their observations.
- Orchestrate the entire cycle within a turn-based control loop.

Let's get started.

## Setup and Environment

Our first step is to set up the Python environment. This ensures that the code runs smoothly and that your outputs match the traces we will analyze later. We will use the `google-genai` package to interact with the Gemini API.

1.  First, we load our `GOOGLE_API_KEY` from the environment. Our utility function checks for the key to ensure the client can be initialized.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from `...`
    Environment variables loaded successfully.
    ```

2.  Next, we import the necessary packages. We will use `google.genai` for the LLM, `pydantic` for data structures, and our own `pretty_print` utility to visualize the agent's traces.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client. The client automatically handles authentication using the API key we loaded.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model ID we will use throughout this lesson. We are using `gemini-2.5-flash`, a model that is both fast and cost-effective, making it ideal for our development and testing.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With our client and model ready, the next step is to give our agent a capability—a tool it can use to interact with an external environment.

## The Tool Layer: Mock Search Implementation

A ReAct agent’s power comes from its ability to use tools to gather information or perform actions [[2]](https://www.ibm.com/think/topics/react-agent). For this lesson, we will create a simple mock search tool. Using a mock tool instead of a real API has several advantages for learning:
- It keeps the focus on the ReAct mechanics, not on API integration details.
- It removes external dependencies, so you do not need extra API keys.
- It provides predictable, consistent responses, which is essential for debugging and understanding the agent’s behavior.

Our mock tool will simulate a search engine with a few hardcoded responses.

1.  We start by defining the `search` function. It takes a string `query` as input and includes a detailed docstring. This docstring is crucial because, as we will see in the Action Phase, Gemini’s function calling feature uses it to understand what the tool does and how to use it.
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
    The function checks for specific keywords in the query and returns a predefined answer. If the query does not match any of our conditions, it returns a "not found" message. This fallback behavior is important for testing how the agent handles failed tool calls.

2.  Next, we create a `TOOL_REGISTRY`. This dictionary maps the tool's name to its function object. The registry acts as a central place for the agent to look up and execute tools. While our agent only has one tool, a production system could have dozens. This mapping allows the model to plan with symbolic names (like `"search"`), while our code safely resolves those names to the actual Python functions.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
In a real-world application, you could easily swap this mock `search` function with a function that calls an actual external API, like Google Search or a private knowledge base. As long as the function signature (name, arguments) and the purpose described in the docstring remain consistent, the agent's logic does not need to change. This modular design is a key principle of building robust AI systems.

Now that our agent has a tool, we need to teach it how to think about when and why to use it.

## The Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is where the agent analyzes the user's query and the conversation history to decide on the best next step. It is the agent's internal monologue, where it reasons about its strategy. We generate this thought by prompting the LLM with a carefully constructed template.

1.  To let the model know which tools are available, we create an XML description from our `TOOL_REGISTRY`. The `build_tools_xml_description` function iterates through the registry and uses each tool's docstring to create a `<tool>` block. This lightweight description gives the model just enough information to reason about the tool's purpose.
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

2.  We then define our prompt template, `PROMPT_TEMPLATE_THOUGHT`. This template instructs the model to act as a decision-maker. It includes placeholders for the available tools (our XML string) and the conversation history. The final instruction asks the model to state its next thought as a short paragraph.
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
    Here is the full prompt with the tool definition injected:
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

3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt template, and calls the Gemini model. It then returns the model's raw text response, which represents the agent's "thought."
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
This thought gives the agent a clear intention. The next step is to translate that intention into a concrete "Action," which could be either a tool call or a final answer to the user.

## The Action Phase: Function Calling and Parsing

After generating a thought, the agent must decide what to do next. This is the "Action" phase. The agent can either use a tool to gather more information or, if it has enough context, provide a final answer. We use Gemini's native function calling capability to handle this decision-making process.

A key advantage of using a model's built-in function calling is that we do not need to manually include tool signatures in our prompt [[3]](https://ai.google.dev/gemini-api/docs/function-calling). When we provide Python functions in the `tools` configuration of the API call, the Gemini client automatically extracts their names, docstrings (as descriptions), and parameter type hints. This information is passed to the model in a specialized format, allowing it to reason about which tool to use without cluttering our main prompt. This separation keeps our prompts clean and focused on high-level strategy.

1.  We start by defining two prompt templates. `PROMPT_TEMPLATE_ACTION` is the default prompt, asking the model to choose between a tool call and a final answer. `PROMPT_TEMPLATE_ACTION_FORCED` is a special-purpose prompt we will use later to force the agent to conclude when it reaches its turn limit.
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

2.  We define two Pydantic models, `ToolCallRequest` and `FinalAnswer`, to represent the two possible outcomes of the action phase. This gives us a structured way to handle the model's decision.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  The `generate_action` function orchestrates this phase. Let’s break it down:
    - If `force_final` is `True` or no tools are provided, it uses the `PROMPT_TEMPLATE_ACTION_FORCED` and returns a `FinalAnswer`. This is our mechanism for gracefully ending the loop.
    - Otherwise, it uses the default `PROMPT_TEMPLATE_ACTION`. It passes the available tools from our `TOOL_REGISTRY` to the `tools` parameter of the `generate_content` call. We set `automatic_function_calling={"disable": True}` because we want to parse the model's decision ourselves, giving us full control over the execution loop.
    - It then inspects the model's response. If a `function_call` is present, it extracts the tool name and arguments and returns a `ToolCallRequest`.
    - If there is no function call, it assumes the model has provided a final answer and returns a `FinalAnswer` object containing the text.
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
With the Thought and Action phases implemented, we have all the components needed to build the main control loop that will bring our ReAct agent to life.

## The Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the engine that drives the ReAct agent, orchestrating the Thought → Action → Observation cycle. It manages the conversation history, calls the thought and action generation functions, executes tools, and processes their results.

To manage the state of the conversation, we will treat the interaction as a sequence of messages. Each message represents a step in the dialogue, whether it is from the user, an internal thought, a tool request, the tool's observation, or the final answer.

1.  We define `MessageRole` and `Message` Pydantic models to structure these interactions. Using an `Enum` for roles makes the code clean and readable.
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

2.  To make the agent's internal process easy to follow, we create a helper function to pretty-print each message. This will allow us to visualize the agent's turn-by-turn reasoning.
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

3.  The `Scratchpad` class acts as the agent's short-term memory. It holds a list of `Message` objects and includes an `append` method that both stores a new message and optionally prints it. This "scratchpad" is serialized into a string each turn and fed back into the prompts, giving the model the full context of the interaction so far.
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

4.  Now we can implement the main `react_agent_loop` function. This function ties everything together.
    - It initializes the `Scratchpad` and adds the initial user question.
    - It enters a loop that runs for a maximum of `max_turns`.
    - **Thought:** In each turn, it calls `generate_thought` with the current scratchpad content.
    - **Action:** It then calls `generate_action`. If the result is a `FinalAnswer`, the loop terminates and returns the answer.
    - **Observation:** If the result is a `ToolCallRequest`, it looks up the tool in the `TOOL_REGISTRY` and executes it. The tool's output (or an error message) becomes the observation. This observation is appended to the scratchpad, closing the loop for the current turn.
    - If the loop finishes without a `FinalAnswer`, it calls `generate_action` one last time with `force_final=True` to ensure a graceful exit.
    
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
    This loop directly implements the ReAct pattern. The agent iteratively thinks, acts, and observes, using the scratchpad to maintain context and learn from its interactions.

    ```mermaid
    flowchart LR
        _start_["_start_"] --> llm["llm"]
        llm -- "continue" --> tools["tools"]
        llm -- "end" --> _end_["_end_"]
        tools --> llm
    ```
    Image 1: A flowchart illustrating the control flow of a ReAct agent implemented using LangGraph, showing the iterative Thought-Action-Observation cycle.

## Tests and Traces: Success and Graceful Fallback

With the complete ReAct loop implemented, we can now test it. Analyzing the agent's traces is the best way to understand its behavior, debug issues, and verify that the logic works as expected. We will run two tests: one straightforward query to demonstrate a successful run, and one designed to fail to test our graceful fallback mechanism.

### Successful Execution Trace

First, let's ask a simple factual question that our mock `search` tool can answer: `"What is the capital of France?"` We will set `max_turns=2` and `verbose=True` to see the step-by-step trace.

1.  We call our main loop function with the question.
    ```python
    # A straightforward question requiring a search.
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User: What is the capital of France?

    Thought (Turn 1/2): I need to find the capital of France. The user's question is a straightforward factual query. I can use the search tool to find this information.

    Tool request (Turn 1/2): search(query='capital of France')

    Observation (Turn 1/2): Paris is the capital of France and is known for the Eiffel Tower.

    Thought (Turn 2/2): The observation from the search tool directly answers the user's question. I can now provide the final answer.

    Final answer (Turn 2/2): Paris is the capital of France.
    ```

2.  Let’s analyze this trace:
    - **Turn 1:** The agent receives the user's query. Its first **Thought** is to use the `search` tool. It generates a **Tool Request** for `search(query='capital of France')`. The tool executes and returns the **Observation**: "Paris is the capital of France...".
    - **Turn 2:** The agent sees the observation, which directly answers the question. Its next **Thought** is that it has enough information. It proceeds to the action phase, where it generates a **Final Answer**: "Paris is the capital of France." The loop then terminates successfully.
    
    This trace confirms that our agent correctly follows the Thought-Action-Observation cycle. It identifies the need for a tool, executes it, processes the result, and provides a final answer, all within the turn limit.

### Graceful Fallback Trace

Now, let's test the agent's resilience. We will ask a question that our mock tool cannot answer: `"What is the capital of Italy?"` This will trigger the tool's fallback response.

1.  We run the loop with the new question.
    ```python
    # An unknown/unsupported query for the mock tool.
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User: What is the capital of Italy?

    Thought (Turn 1/2): The user is asking for the capital of Italy. I can use the search tool to find this information.

    Tool request (Turn 1/2): search(query='capital of Italy')

    Observation (Turn 1/2): Information about 'capital of Italy' was not found.

    Thought (Turn 2/2): The previous search for "capital of Italy" failed. I should try a broader search for just "Italy" to see if I can find any relevant information that might lead me to the capital.

    Tool request (Turn 2/2): search(query='Italy')

    Observation (Turn 2/2): Information about 'Italy' was not found.

    Final answer (Forced): I am sorry, but I was unable to find the capital of Italy using the available tools.
    ```
2.  Here is the analysis:
    - **Turn 1:** The agent tries to `search` for "capital of Italy," but the tool returns the **Observation**: "Information about 'capital of Italy' was not found."
    - **Turn 2:** The agent observes the failure. Its next **Thought** shows an adaptive strategy: it decides to try a broader search for just "Italy." However, this also fails, returning another "not found" **Observation**.
    - **Forced Exit:** The agent has now reached its `max_turns` limit of 2. The control loop calls `generate_action` with `force_final=True`. This instructs the model to summarize the situation and provide a **Final Answer (Forced)**, admitting it could not find the information.

This trace demonstrates the agent's ability to handle tool failures and adapt its strategy. More importantly, it shows that our `max_turns` limit and forced-answer mechanism work as a safety net, ensuring the agent terminates gracefully instead of getting stuck in a loop of failed attempts.

## Conclusion

In this lesson, we have moved from theory to practice by building a functional ReAct agent from scratch. We implemented every component of the Thought-Action-Observation loop: defining tools, generating thoughts, selecting actions via function calling, executing tools, processing observations, and orchestrating the entire flow in a control loop. By analyzing the traces, we have seen how this simple architecture enables an agent to reason, adapt to failures, and solve problems step-by-step.

The key takeaway is that agentic systems are not magic. They are the result of careful engineering, combining LLM capabilities with structured code. Building this agent yourself provides a concrete mental model that demystifies how frameworks like LangChain or CrewAI operate under the hood. This foundational knowledge is essential for any AI engineer looking to build, customize, and debug robust agentic applications.

In our next lesson, we will build on this foundation by exploring one of the most critical components of advanced agents: memory. We will learn how agents can retain information across conversations to provide more personalized and context-aware interactions.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)
- [2] *ReAct Agent*. (n.d.). IBM. [https://www.ibm.com/think/topics/react-agent](https://www.ibm.com/think/topics/react-agent)
- [3] *Function calling*. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)