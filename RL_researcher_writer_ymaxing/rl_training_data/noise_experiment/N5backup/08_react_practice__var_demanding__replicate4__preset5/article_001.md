# Lesson 8: Building a ReAct Agent From Scratch

In our previous lessons, we covered the theoretical foundations of AI agents, exploring planning, reasoning, and how to equip LLMs with tools. We learned about the ReAct framework, which enables an agent to reason about a problem, take actions in an environment, and process observations to inform its next step. Theory is essential, but to truly master a concept, you have to build it yourself.

This lesson is all about practice. We are moving from theory to implementation by building a minimal ReAct agent from the ground up using only Python and the Gemini API. We will implement the full Thought → Action → Observation loop, piece by piece. This hands-on approach shows what happens inside agentic frameworks. By understanding the core mechanics, you can build, debug, and customize agents with confidence, freeing you from the limitations of any single library.

We will walk through the entire process, following the code from the lesson's notebook. By the end, you will have a working agent and a concrete mental model of how these systems operate.

**What's ahead:**

1.  Setup and Environment
2.  Tool Layer: Mock Search Implementation
3.  Thought Phase: Prompt Construction and Generation
4.  Action Phase: Function Calling and Parsing
5.  Control Loop: Messages, Scratchpad, and Orchestration
6.  Tests and Traces: Success and Graceful Fallback

Let's get started.

## Setup and Environment

Before we write any agent logic, we need to set up a clean and reproducible Python environment. This ensures our code runs as expected and that our outputs match the traces we will analyze later. This initial setup is a critical step in any software project, and AI engineering is no exception. It lays the foundation for a maintainable and scalable application.

1.  First, we load our `GOOGLE_API_KEY` from the `.env` file using a custom utility. The `lessons.utils.env.load` function is a simple helper that encapsulates the logic for finding and loading environment variables. This is a good software engineering practice as it promotes modularity. By abstracting this logic into a utility, we can reuse it across different lessons and projects without duplicating code. It also keeps our main notebook clean and focused on the agent's logic, separating configuration from implementation.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    ```

2.  Next, we import the key packages for our agent. We will use `google-genai` to interact with the Gemini API. For structuring our data, we use `pydantic`, `enum`, and `typing`. Pydantic is particularly important for production-grade agents. It allows us to define a strict data schema, creating a formal contract between the LLM's output and our application code. This provides runtime data validation, which is essential for reliability. While any runtime validation adds overhead, Pydantic's performance, particularly since version 2 which is partially written in Rust, is exceptional. For agentic workloads, the validation latency is negligible compared to the latency of the LLM call itself, making it a production-safe choice for ensuring data integrity without sacrificing speed [[21]](https://medium.com/@mohitcharan04/comprehensive-comparison-of-ai-agent-frameworks-bec7d25df8a6). The `Enum` class is used to define a fixed set of roles for our messages (e.g., `USER`, `THOUGHT`). This makes the agent's internal state machine more explicit and readable, preventing bugs that could arise from using plain strings. Finally, `pretty_print` is another custom utility designed for reusability, helping us visualize the agent's execution trace in a clear, color-coded format.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client, which will be our interface to the language model.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this lesson, `gemini-2.5-flash` is a great choice because it is fast and cost-effective, perfect for the iterative development and testing we will be doing.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model ID in place, we are ready to define the external capabilities our agent can use.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to interact with the world through tools. For this lesson, we will implement a mock search tool to serve as our agent's external knowledge source. We use a mock tool instead of a real API for a few important reasons: it simplifies our focus to the ReAct mechanics, removes external dependencies, and provides predictable responses, which is ideal for testing and learning [[12]](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/).

1.  Our mock `search` function is a simple Python function that takes a string query and returns a string response. Its docstring is critical, as it provides the description the LLM will use to understand what the tool does and when to use it.
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
    The function includes hardcoded responses for specific queries and a generic "not found" message as a fallback. This fallback behavior is crucial for teaching the agent how to handle situations where a tool fails to provide useful information.

2.  To make the tool available to our agent, we create a `TOOL_REGISTRY`. This dictionary maps the tool's name (which the LLM will generate) to the actual Python function. This simple mapping is a common and effective pattern for managing tools in agentic systems.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

In a production system, you would replace this mock function with calls to real external APIs. The strategy is to encapsulate the API logic within a Python function that preserves the same signature (`query: str -> str`) and docstring. For example, to integrate a real Google Search, you could use a library that wraps the SERP API [[13]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

A production implementation would look something like this:
```python
from some_search_library import GoogleSearchAPI

def google_search(query: str) -> str:
    """Searches the web using Google Search. Useful for getting up-to-date news and factual information."""
    try:
        # API key would be loaded from environment variables
        search_api = GoogleSearchAPI(api_key=os.getenv("GOOGLE_API_KEY"))
        results = search_api.search(query)
        # Format results into a string for the agent
        return format_search_results(results)
    except Exception as e:
        # Return an informative error message to the agent
        return f"Error during Google Search: {str(e)}"
```
This approach has several production considerations. API key management is critical; keys should be stored securely as environment variables, never hardcoded. You must also handle potential network errors and API rate limits. A common strategy is to implement a retry mechanism with exponential backoff, which waits progressively longer between retries to avoid overwhelming the API. Finally, the function should gracefully handle failures by catching exceptions and returning an informative error string. This allows the agent to observe the failure and reason about its next step, such as trying a different tool or rephrasing the query [[15]](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025). Because the agent's core logic interacts with the tool through a consistent interface (name, signature, and docstring), you can swap the mock implementation with a production-ready one without changing the agent itself [[27]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is the agent's internal monologue. It is where the LLM analyzes the current situation—the user's query and the conversation history—and plans its next move. A clear, well-structured thought is the foundation for effective action. This step directly corresponds to the "Reasoning" part of the ReAct framework, where the agent formulates a strategy before acting [[1]](https://arxiv.org/pdf/2210.03629).

1.  To help the model reason effectively, we provide it with a description of the available tools. We create a helper function, `build_tools_xml_description`, to generate an XML representation of our tools from their docstrings. Using XML tags like `<tool>` and `<description>` provides clear, structured delimiters that help the model distinguish between different parts of the prompt [[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies). This technique is a form of context engineering, where we structure the input to guide the model's attention and improve its parsing accuracy. The prompt template itself is designed to be a zero-shot instruction, meaning it tells the model how to behave without providing explicit examples of a full conversation. It sets the agent's persona ("You are deciding the next best step..."), provides the necessary context (tools and conversation history), and constrains the output format ("State your next thought... as one short paragraph").
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

2.  Let's inspect the full prompt template. It clearly instructs the model on its role, shows it the available tools, and provides a placeholder for the conversation history. This gives the agent all the context it needs to generate a relevant thought.
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

3.  The `generate_thought` function ties everything together. It takes the current conversation history, formats the prompt template with the tool descriptions, calls the Gemini model, and returns the generated thought as a clean string. This function is the engine of the "Reason" step in our loop. Its output is not shown to the user but is instead added to the agent's internal scratchpad, providing the rationale for the subsequent "Action" phase. This explicit reasoning step is what makes the agent's behavior interpretable and easier to debug [[4]](https://www.ibm.com/think/topics/react-agent).
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

With a coherent thought generated, the agent has a plan. The next step is to translate that plan into a concrete action, which could be calling a tool or providing the final answer to the user.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent commits to a course of action. Based on its thought and the conversation history, it must decide whether to use a tool to gather more information or to conclude with a final answer. Modern LLM APIs like Gemini offer a powerful feature called "function calling" that makes this process robust and reliable [[20]](https://ai.google.dev/gemini-api/docs/function-calling). Instead of asking the model to generate text that we have to parse, we can ask it to generate a structured request to call a specific function.

1.  First, we define two prompt templates for the action phase. `PROMPT_TEMPLATE_ACTION` is the default, asking the model to choose between a tool call and a final answer. `PROMPT_TEMPLATE_ACTION_FORCED` is a special-purpose prompt we will use to ensure the agent provides a conclusion, which is a crucial mechanism for preventing infinite loops. This separation of concerns in prompting allows us to guide the model more precisely depending on the state of the control loop.
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

2.  To handle the model's output, we define two Pydantic models: `ToolCallRequest` and `FinalAnswer`. These models create a strict schema for the action, ensuring the output is always predictable and easy to parse.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
    This strict schema is a key element of production-grade agents. The performance overhead of Pydantic validation is minimal compared to network and model latency, making it a worthwhile trade-off for the reliability it provides [[21]](https://medium.com/@mohitcharan04/comprehensive-comparison-of-ai-agent-frameworks-bec7d25df8a6).

3.  The `generate_action` function orchestrates this phase. It selects the appropriate prompt and, most importantly, passes the Python tool functions directly to the `generate_content` call via the `tools` parameter. The Gemini client automatically converts these functions and their docstrings into a schema the model can understand. This is a powerful feature that separates the strategic guidance in our prompt from the technical details of the tools. We also set `automatic_function_calling={"disable": True}` because we want to maintain full control over the execution loop. This allows us to inspect the model's intended action, log it, and then execute it ourselves, which is essential for debugging and building robust systems.
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
    The function then parses the response. If the model generated a `function_call`, we package it into our `ToolCallRequest` model. Otherwise, we treat the text response as a `FinalAnswer`. This robust parsing logic, combined with native function calling, creates a reliable action phase.

    In a production setting, this is where a significant amount of engineering effort is focused. Tool calls can fail in many ways: APIs time out, return partial data, or exhaust rate limits [[22]](https://dev.to/wassimchegham/why-your-ai-agent-demo-falls-apart-in-production-1320). Even the model's use of tools can be unreliable. For instance, some developers have reported that Gemini models can occasionally hallucinate tool outputs or ignore valid data returned by a tool, a failure mode that converts the developer into a "babysitter" for the agent [[23]](https://adam.holter.com/gemini-tool-calling-problems-why-it-feels-nervous-in-agents/).

    To mitigate this, you would implement patterns like exponential backoff for retries. However, a global retry counter can be drained by a single misbehaving tool or by the LLM hallucinating a non-existent tool name repeatedly, causing the entire agent to fail [[24]](https://towardsdatascience.com/your-react-agent-is-wasting-90-of-its-retries-heres-how-to-stop-it/). A more robust solution is the circuit breaker pattern. Like an electrical breaker, it "trips" after a certain number of failures, preventing further calls to an unhealthy service and allowing it time to recover [[25]](https://www.statsig.com/perspectives/building-fault-tolerant-systems-with-circuit-breakers). In AI agents, this concept can be taken further by using Representation Engineering to build circuit breakers inside the model itself. This technique identifies the internal activation patterns that precede a harmful action (like a malicious tool call) and reroutes them, stopping the unsafe behavior before it is even generated [[26]](https://neuraltrust.ai/blog/circuit-breakers). For example, if the agent intends to call a function like `send_disinformation_email`, the circuit breaker would detect the harmful intent from the model's internal state and block the action before it is executed.

## ReAct Control Loop: Messages, Scratchpad, and Orchestration

Now we arrive at the core of our agent: the control loop. This is the orchestrator that brings together the Thought, Action, and Observation phases, managing the flow of information and driving the agent toward its goal. We will build this loop around a structured messaging system and a "scratchpad" that serves as the agent's working memory. This orchestration is what turns a series of disconnected LLM calls into a coherent, goal-directed process.

Image 1: A flowchart illustrating the ReAct (Reasoning and Acting) control loop.

1.  First, we define the structure for all interactions within the agent. The `MessageRole` enum categorizes each message, and the `Message` Pydantic model provides a unified format for content. This structured approach is fundamental to building a transparent and debuggable agent. By defining explicit roles like `THOUGHT` and `TOOL_REQUEST`, we can easily trace the agent's internal state and decision-making process at each step of the loop.
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

2.  To make tracing the agent's execution easier, we create a helper function to pretty-print each message. Visualizing the sequence of thoughts, actions, and observations is essential for debugging and understanding how the agent arrives at its conclusions. This function uses role-based coloring to make the trace more readable.
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

3.  The `Scratchpad` class acts as the agent's short-term memory for a given task. It wraps a list of `Message` objects and provides a simple interface to append new messages and serialize the entire history into a string for the LLM's context. This history is the "Observation" that the agent uses in the next "Reasoning" step.
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
    While simple, this accumulating approach has a critical performance implication: the context sent to the LLM grows linearly with each turn. A benchmark showed that for a 10-turn ReAct loop, an accumulating scratchpad processed ~60% more tokens than an ephemeral approach that only keeps the last scratchpad state. In long-running tasks, this not only increases cost and latency but can lead to context window overflow [[27]](https://azguards.com/ai-engineering/the-memory-leak-in-the-loop-optimizing-custom-state-reducers-in-langgraph/). For production systems, you would implement more sophisticated state management, a topic we will explore later.

4.  Finally, we implement the `react_agent_loop`. This function orchestrates the entire process. It iterates through a set number of turns, generating a thought, then an action. If the action is a `FinalAnswer`, the loop terminates. If it is a `ToolCallRequest`, the loop executes the tool, captures the output as an `Observation`, appends it to the scratchpad, and continues to the next turn. The tool execution block is wrapped in a `try...except` to handle any errors that might occur, ensuring the agent doesn't crash. If the agent reaches its maximum turn limit, it makes one final call to `generate_action` with `force_final=True` to ensure a graceful exit. This `max_turns` limit is a critical safety rail. Without it, agents can get stuck in "reasoning loops," where they repeatedly call the same tool with the same arguments without making progress, wasting tokens and time. The forced exit ensures the agent terminates predictably, even when it fails to solve the problem [[28]](https://builder.aws.com/content/3BOny05LArVv7BVN8PU3duOPM86/why-ai-agents-fail-3-failure-modes-that-cost-you-tokens-and-time).
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
    This loop is the engine of our ReAct agent. It demonstrates how a simple, turn-based process with structured state management can produce complex, goal-oriented behavior.

## Tests and Traces: Success and Graceful Fallback

With our agent fully assembled, it is time to test it and analyze its behavior. By observing the execution traces, we can validate that each component—thought generation, action selection, tool execution, and the control loop—is working as intended.

### Success Case: Factual Question

Let's start with a straightforward factual question that our mock tool is designed to answer. We will set `max_turns=2` and `verbose=True` to see the step-by-step execution.
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
I need to find the capital of France. I can use the search tool to find this information.

Tool request (Turn 1/2):
search(query='capital of France')

Observation (Turn 1/2):
Paris is the capital of France and is known for the Eiffel Tower.

Thought (Turn 2/2):
I have found the answer. The capital of France is Paris.

Final answer (Turn 2/2):
The capital of France is Paris.
```
This trace perfectly demonstrates the ideal ReAct flow. In the first turn, the agent thinks about its goal, requests the `search` tool, and receives a successful observation. In the second turn, it recognizes that it has the answer and generates the final response, terminating the loop correctly.

### Fallback Case: Unsupported Question

Now, let's test the agent's resilience. We will ask a question that our mock tool does not have a predefined answer for. This will test the agent's ability to handle tool "failures" and the forced termination logic.
```python
# A question where the search tool will not find a direct answer, testing fallback.
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```
The trace shows a more complex reasoning process:
```text
User (Turn 1/2):
What is the capital of Italy?

Thought (Turn 1/2):
I need to find the capital of Italy. I will use the search tool for this.

Tool request (Turn 1/2):
search(query='capital of Italy')

Observation (Turn 1/2):
Information about 'capital of Italy' was not found.

Thought (Turn 2/2):
The previous search for "capital of Italy" failed. I should try a broader search for just "Italy" and see if I can find the capital from that information.

Tool request (Turn 2/2):
search(query='Italy')

Observation (Turn 2/2):
Information about 'Italy' was not found.

Final answer (Forced):
I am unable to find the capital of Italy using the available tools.
```
This trace highlights the agent's graceful fallback behavior. After the first tool call fails, its next thought is to try a different strategy—a broader query. This demonstrates adaptive reasoning. When that also fails and it reaches the `max_turns` limit, the control loop correctly triggers the forced final answer, and the agent admits it cannot fulfill the request. This is much better than hallucinating an incorrect answer.

In a production environment, testing moves beyond simple success and fallback cases. It becomes a systematic effort to discover and mitigate failure modes. This involves creating a comprehensive test suite with edge cases and performance benchmarks, similar to traditional software engineering. For agents, this also requires adversarial testing, where the goal is to actively mislead the agent.

A key threat model is *Adversarial Environmental Injection*, where tool outputs are deliberately poisoned. The Potemkin evaluation framework, for example, formalizes two types of such attacks. "Breadth attacks" poison the content of search results to make the agent adopt false beliefs. "Depth attacks" poison the structure of information, creating fake navigational paths that trap the agent in infinite loops, causing it to waste its entire turn budget [[29]](https://arxiv.org/html/2604.18874v1). Research shows that robustness to these two attack types are independent capabilities; an agent that resists content poisoning may still fall into navigational traps. Building robust agents means testing for both epistemic (belief) and navigational (planning) resilience. This rigorous validation is what separates a prototype from a production-ready system.

## Conclusion

We have successfully built a complete ReAct agent from scratch. By implementing each component of the Thought-Action-Observation cycle, we have gained a deep, practical understanding of how these systems work under the hood. This hands-on experience provides a concrete mental model that is essential for any AI engineer. It gives you the confidence to not only use existing agentic frameworks but also to extend, debug, and even build your own custom solutions when the need arises.

The agent we built is minimal, but it is a solid foundation. This from-scratch understanding is critical, even when using production frameworks like LangGraph, which formalize the agent loop as a more controllable and observable stateful graph [[30]](https://www.abstractalgorithms.dev/langgraph-react-agent-pattern). The core principles remain the same and can be adapted to other domains like robotics by simply swapping out the tools [[31]](https://ai.plainenglish.io/agents-react-vs-coact-d44ada0dd103). Now that you have a working control loop, you can enhance it with more sophisticated capabilities. In our upcoming lessons, we will explore how to add persistent memory to our agent, allowing it to learn from past interactions (Lesson 9), and how to connect it to vast knowledge bases using Retrieval-Augmented Generation (RAG) (Lesson 10).

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. https://arxiv.org/pdf/2210.03629
- [2] Google. (n.d.). *Prompting strategies*. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [3] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review*. https://arxiv.org/pdf/2504.19678
- [4] IBM. (n.d.). *What is a ReAct agent?* https://www.ibm.com/think/topics/react-agent
- [5] IBM. (n.d.). *What is AI agent planning?* https://www.ibm.com/think/topics/ai-agent-planning
- [6] Anthropic. (2024). *Building effective agents*. https://www.anthropic.com/engineering/building-effective-agents
- [7] Google. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://ai.google.dev/gemini-api/docs/langgraph-example
- [8] Daily Dose of DS. (2024). *AI Agents Crash Course - Part 10: ReAct Framework with Implementation*. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [9] Brownlee, J. (2024). *Building ReAct Agents with LangGraph: A Beginner’s Guide*. https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/
- [10] Iusztin, P. (2024). *Building Production ReAct Agents From Scratch Is Simple*. https://www.decodingai.com/p/building-production-react-agents
- [11] Schmid, P. (2025). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [12] Neradot. (2024). *Building a Python ReAct Agent Class: A Step-by-Step Guide*. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [13] Shankar, A. (2024). *Building ReAct Agents from Scratch using Gemini*. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [14] Roelants, P. (2023). *ReAct with OpenAI Function calling*. https://peterroelants.github.io/posts/react-openai-function-calling/
- [15] LateNode. (2024). *LangChain ReAct Agent: Complete Implementation Guide with Working Examples (2025)*. https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025
- [16] GenMind. (n.d.). *Building ReAct Agents with Microsoft Agent Framework: From Theory to Production*. https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/
- [17] Shankar, A. (2024). *Building ReAct Agents from Scratch using Gemini*. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [18] Schmid, P. (2025). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [19] Google. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://ai.google.dev/gemini-api/docs/langgraph-example
- [20] Google. (n.d.). *Function calling*. https://ai.google.dev/gemini-api/docs/function-calling
- [21] Charan, M. (2024). *Comprehensive Comparison of AI Agent Frameworks*. https://medium.com/@mohitcharan04/comprehensive-comparison-of-ai-agent-frameworks-bec7d25df8a6
- [22] Chegham, W. (n.d.). *Why your AI Agent Demo falls apart in Production*. https://dev.to/wassimchegham/why-your-ai-agent-demo-falls-apart-in-production-1320
- [23] Holter, A. (n.d.). *Gemini Tool Calling Problems: Why It Feels Nervous in Agents*. https://adam.holter.com/gemini-tool-calling-problems-why-it-feels-nervous-in-agents/
- [24] Towards Data Science. (n.d.). *Your ReAct Agent Is Wasting 90% of Its Retries. Here’s How to Stop It*. https://towardsdatascience.com/your-react-agent-is-wasting-90-of-its-retries-heres-how-to-stop-it/
- [25] Statsig. (n.d.). *Building Fault-Tolerant Systems with Circuit Breakers*. https://www.statsig.com/perspectives/building-fault-tolerant-systems-with-circuit-breakers
- [26] NeuralTrust. (2026). *Using Circuit Breakers to Secure the Next Generation of AI Agents*. https://neuraltrust.ai/blog/circuit-breakers
- [27] Azguards. (n.d.). *The Memory Leak in the Loop: Optimizing Custom State Reducers in LangGraph*. https://azguards.com/ai-engineering/the-memory-leak-in-the-loop-optimizing-custom-state-reducers-in-langgraph/
- [28] AWS. (n.d.). *Why AI Agents Fail: 3 Failure Modes That Cost You Tokens and Time*. https://builder.aws.com/content/3BOny05LArVv7BVN8PU3duOPM86/why-ai-agents-fail-3-failure-modes-that-cost-you-tokens-and-time
- [29] Zhan, Z., Zhou, H., Li, Z., Jing, P., Li, K., & Haddadi, H. (2026). *How Adversarial Environments Mislead Agentic AI*. https://arxiv.org/html/2604.18874v1
- [30] Abstract. (n.d.). *The LangGraph ReAct Agent Pattern*. https://www.abstractalgorithms.dev/langgraph-react-agent-pattern
- [31] AI In Plain English. (n.d.). *Agents: ReAct vs CoAct*. https://ai.plainenglish.io/agents-react-vs-coact-d44ada0dd103