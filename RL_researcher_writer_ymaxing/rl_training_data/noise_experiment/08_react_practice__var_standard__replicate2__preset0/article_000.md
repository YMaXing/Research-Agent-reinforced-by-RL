# Building a ReAct Agent From Scratch: A Step-by-Step Guide

In our last lesson, we covered the theory behind planning and reasoning frameworks like ReAct. We saw how agents could break down complex problems by interleaving `Thought`, `Action`, and `Observation`. But theory only gets you so far. To truly understand how these systems work, you have to build one. Abstract diagrams are useful, but they do not capture the engineering reality of managing state, parsing outputs, and orchestrating a control loop.

This lesson is 100% practical. We will build a minimal ReAct agent from scratch using only Python and the Gemini API. By implementing the complete `Thought` → `Action` → `Observation` cycle yourself, you will gain a concrete mental model that frameworks often hide. This hands-on experience is what separates prototyping from building production-grade AI.

We will walk through the entire process, step-by-step, following the code in the associated notebook. You will learn how to:

-   Set up a Python environment with the Gemini client.
-   Define and integrate a mock tool for the agent to use.
-   Implement the `Thought` phase to generate a plan.
-   Use function calling to select and parse actions.
-   Build a turn-based control loop to orchestrate the agent.
-   Analyze traces to verify success and graceful failure.

By the end, you will have a working ReAct agent and the confidence to debug, extend, and customize it for your own applications.

## Setup and Environment

Before we start building, let's ensure our environment is set up correctly. A clean setup ensures your code runs smoothly and the outputs match the traces we will analyze later. This lesson follows a notebook, and our first step is to configure the essentials: loading environment variables, importing packages, and initializing the Gemini client.

1.  First, we load our `GOOGLE_API_KEY` from a `.env` file. We use a simple utility function for this, which is good practice for keeping secrets out of your code.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    ```

2.  Next, we import the necessary packages. Our implementation relies on `google-genai` for the LLM, `pydantic` for creating structured data classes, and Python’s `enum` and `typing` for type safety. We also import a `pretty_print` utility to make our agent's traces easier to read.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```

3.  With our key loaded, we initialize the Gemini client. This object is our gateway to the Gemini API.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this guide, we will use `gemini-2.5-flash`, which is fast and cost-effective, making it ideal for the simple reasoning our agent requires.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model in place, we can now define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to interact with the world through tools. For this lesson, we will focus on the ReAct mechanics rather than complex API integrations. To do this, we will create a mock `search` tool. Using a mock tool simplifies the learning process by eliminating external dependencies and API keys, and it gives us predictable responses, which is perfect for testing.

Our mock tool is a simple Python function that simulates a search engine. It takes a `query` string and returns a hardcoded response if the query matches a predefined pattern. If the query is not recognized, it returns a fallback message. The function’s docstring is crucial, as it provides the description the LLM will use to understand what the tool does and how to use it.

1.  Here is the implementation of our `search` function. It handles two specific queries—the capital of France and the definition of ReAct—and has a default response for anything else.
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

2.  To make tools accessible to our agent, we use a `TOOL_REGISTRY`. This dictionary maps the tool's name (the function's name) to the function object itself. This allows our agent to plan with symbolic names like `"search"` and lets our code safely resolve and execute the corresponding Python function.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

In a production system, you could easily swap this mock function with a real one that calls an external API like Google Search or a domain-specific knowledge base. As long as the function signature (`query: str -> str`) and the purpose described in the docstring remain consistent, the agent's logic would not need to change.

Now that our agent has a tool, we need to teach it how to think about when to use it.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is where the agent analyzes the user's query and its history to decide what to do next. We will implement this by creating a prompt that asks the LLM to generate a brief, focused paragraph about its intended next action and the reasoning behind it.

To help the LLM make an informed decision, we provide it with context, including the tools available and the conversation so far. We format the tool descriptions in XML, a practice that helps the model clearly distinguish instructions from other context.

1.  First, we define a function to convert our `TOOL_REGISTRY` into a minimal XML description. It iterates through the tools, extracts their docstrings, and wraps them in `<tool>` and `<description>` tags.
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

2.  Next, we create the prompt template for the thought-generation step. It includes the XML-formatted tool descriptions and a placeholder for the conversation history.
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
    The fully formatted prompt looks like this, clearly outlining the `search` tool's capabilities:
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

3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt, calls the Gemini model, and returns the generated thought as plain text.
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

With a coherent thought generated, the agent has a plan. The next step is to translate that plan into a concrete `Action`, which could be a tool call or a final answer to the user.

## Action Phase: Function Calling and Parsing

After generating a thought, the agent must decide on a concrete action. This could be calling a tool to gather more information or, if it has enough context, providing a final answer. We will implement this "Action" phase using Gemini's native function calling capability.

A key advantage of using function calling is that we do not need to clutter our prompt with detailed tool signatures. We pass the Python tool functions directly to the Gemini API, which automatically extracts their names, docstrings (for descriptions), and parameter types. This keeps our action-selection prompt clean and focused on high-level strategy, while the API handles the technical details of tool integration.

1.  We start by defining two prompt templates. The first is for general action selection. The second, `PROMPT_TEMPLATE_ACTION_FORCED`, is a special-purpose prompt we will use to force the agent to provide a final answer, which is a crucial mechanism for preventing infinite loops.
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

2.  To handle the two possible outcomes of the action phase (a tool call or a final answer), we define two Pydantic models. These models provide a structured way to represent the agent's decision, ensuring the output is predictable and easy to parse.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  Now we implement the `generate_action` function. This is the core of the action phase. It takes the conversation history and the tool registry as input.
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
    If `force_final` is `True`, it uses the specialized prompt to request a conclusive answer. Otherwise, it passes the available tools to the `generate_content` call. We set `automatic_function_calling` to `{"disable": True}` because we want to parse the tool call ourselves and maintain full control over the execution loop. The function then inspects the response: if it contains a `function_call`, it parses the name and arguments into a `ToolCallRequest`. If not, it assumes the response is a final answer and wraps it in a `FinalAnswer` object.

With the `Thought` and `Action` phases implemented, we have all the building blocks for our agent. The next step is to orchestrate them in a control loop.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the heart of the ReAct agent, orchestrating the `Thought` → `Action` → `Observation` cycle. It manages the conversation history, calls the thought and action generation functions, executes tools, and processes their outputs (observations). To keep track of the conversation, we will use a "scratchpad," which is a list of messages representing each step of the agent's process.

1.  First, we define the data structures for our messages. `MessageRole` is an `Enum` that categorizes each message (e.g., `USER`, `THOUGHT`, `TOOL_REQUEST`). The `Message` class is a Pydantic model that holds the role and content for each entry in our scratchpad. This structured approach makes the agent's history clear and easy to trace.
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

2.  To make the agent's execution easy to follow, we create a helper function that pretty-prints each message with a color-coded header indicating its role and the current turn.
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

3.  Next, we define the `Scratchpad` class. It manages a list of `Message` objects and provides an `append` method to add new messages. When `verbose=True`, this method also calls our pretty-printer, giving us a real-time trace of the agent's activity.
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

4.  Finally, we implement the main `react_agent_loop`. This function ties everything together. It initializes the scratchpad with the user's question and then enters a loop that runs for a maximum number of turns.
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
    Inside the loop, it first generates a `Thought` and adds it to the scratchpad. Then, it generates an `Action`. If the action is a `FinalAnswer`, the loop terminates and returns the answer. If it is a `ToolCallRequest`, the loop executes the corresponding tool, captures the output as an `Observation`, and adds it to the scratchpad. If the loop reaches `max_turns`, it calls `generate_action` one last time with `force_final=True` to ensure a graceful exit.

With the control loop complete, our ReAct agent is ready to be tested.

## Tests and Traces: Success and Graceful Fallback

Now that we have built our agent, it is time to validate its behavior. We will run two tests: a straightforward factual question to check the successful execution of the full ReAct cycle, and a query our mock tool cannot answer to verify its graceful fallback and termination logic. Analyzing the traces will confirm that each component—thought, action, observation, and the control loop—works as designed.

### Successful Execution Trace

First, let's ask a question our mock tool can answer: `"What is the capital of France?"`. We will set `max_turns=2` and `verbose=True` to see the step-by-step trace.

```python
# A straightforward question requiring a search.
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The agent produces the following trace:

```text
User (Turn 1/2):
What is the capital of France?

Thought (Turn 1/2):
I need to find the capital of France. The user is asking a direct factual question, so I should use the search tool to find the answer.

Tool request (Turn 1/2):
search(query='capital of France')

Observation (Turn 1/2):
Paris is the capital of France and is known for the Eiffel Tower.

Thought (Turn 2/2):
The search tool provided the answer directly. I can now formulate the final answer based on this information.

Final answer (Turn 2/2):
Paris is the capital of France.
```

This trace confirms the ideal workflow. The agent correctly identifies the need for a search, calls the tool with the right query, processes the observation, and provides the final answer, all within the turn limit.

### Graceful Fallback Trace

Next, let's test the agent with a query our mock tool does not know: `"What is the capital of Italy?"`. This will test the agent's ability to handle tool failures and its forced termination logic.

```python
# An unknown/unsupported query for the mock tool.
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The output trace shows the agent adapting its strategy:

```text
User (Turn 1/2):
What is the capital of Italy?

Thought (Turn 1/2):
I need to find the capital of Italy. I will use the search tool to look up this information.

Tool request (Turn 1/2):
search(query='capital of Italy')

Observation (Turn 1/2):
Information about 'capital of Italy' was not found.

Thought (Turn 2/2):
The initial search for "capital of Italy" failed. I will try a broader search for just "Italy" to see if I can find the capital within a general article.

Tool request (Turn 2/2):
search(query='Italy')

Observation (Turn 2/2):
Information about 'Italy' was not found.

Final answer (Forced):
I'm sorry, but I was unable to find information about the capital of Italy using the available tools.
```

This trace demonstrates several key features. After the first search fails, the agent's next thought shows a change in strategy—it tries a broader query. When that also fails and it reaches the `max_turns` limit, the control loop correctly triggers the forced final answer path, resulting in a helpful message to the user. These tests confirm our from-scratch implementation is robust.

## Conclusion

By building a ReAct agent from the ground up, we have demystified the `Thought-Action-Observation` loop that powers modern agentic systems. We have seen how to orchestrate reasoning with Gemini, integrate external tools via function calling, manage state with a scratchpad, and ensure robust execution with a control loop. This hands-on approach provides a concrete mental model that is essential for any AI engineer looking to move beyond simple prompts and build truly interactive applications.

This minimal implementation is just the beginning. The patterns we have established—structured messages, a clear control loop, and modular tools—provide a solid foundation. In future lessons, we will build upon this by exploring more advanced topics like agent memory and Retrieval-Augmented Generation (RAG). Armed with a deep understanding of the core mechanics, you will be well-equipped to tackle those challenges and build even more sophisticated agents.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. *arXiv*. [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)
- [2] ReAct Agent - IBM. (n.d.). IBM. [https://www.ibm.com/think/topics/react-agent](https://www.ibm.com/think/topics/react-agent)
- [3] AI Agent Planning - IBM. (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-planning](https://www.ibm.com/think/topics/ai-agent-planning)
- [4] Building effective agents - Anthropic. (2024, December 19). Anthropic. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [5] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/langgraph-example](https://ai.google.dev/gemini-api/docs/langgraph-example)
- [6] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. *arXiv*. [https://arxiv.org/pdf/2504.19678](https://arxiv.org/pdf/2504.19678)
- [7] Shankar, A. (2024, June 20). Building ReAct Agents from Scratch using Gemini. *Medium*. [https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [8] AI Agent Orchestration - IBM. (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [9] Gemini Function Calling Documentation. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [10] Iusztin, P. (2025). Building Production ReAct Agents From Scratch Is Simple. *decodingai.com*. [https://www.decodingai.com/p/building-production-react-agents](https://www.decodingai.com/p/building-production-react-agents)
- [11] Pasternak, R. (2024, November 5). Building a Python React Agent Class: A Step-by-Step Guide. *Neradot*. [https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide](https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide)
- [12] Brownlee, J. (2024, July 1). Building ReAct Agents with LangGraph: A Beginner’s Guide. *Machine Learning Mastery*. [https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/](https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/)
- [13] Implementing ReAct Agentic Pattern From Scratch. (n.d.). *Daily Dose of DS*. [https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/)
- [14] Prompt design strategies. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [15] Schmid, P. (2025, March 31). ReAct agent from scratch with Gemini 2.5 and LangGraph. *philschmid.de*. [https://www.philschmid.de/langgraph-gemini-2-5-react-agent](https://www.philschmid.de/langgraph-gemini-2-5-react-agent)