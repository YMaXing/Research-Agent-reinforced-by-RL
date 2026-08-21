# Building a ReAct Agent From Scratch in Pure Python

In our journey from Python developer to AI Engineer, we have covered the foundational concepts of AI systems. We have explored the landscape of agents and workflows, learned the art of context engineering, and mastered how to get reliable, structured data out of LLMs. We also looked at the core patterns for building workflows and the mechanics of tool calling and planning.

Now, it is time to put it all together. This lesson is 100% practical. We will build a minimal ReAct agent from scratch, end-to-end, using only Python and the Gemini API. You will implement the full Thought → Action → Observation loop, giving you a concrete mental model of how these reasoning systems truly work.

When I started building my own AI agents, I initially turned to frameworks like LangGraph. I thought their graph-based model would make my logic cleaner. Instead, I found myself fighting the framework. Simple if-else statements and loops became hours of work as I tried to force my code into a paradigm that felt unnatural and added more complexity than value.

Frustrated, I did what I always do when I am stuck: I opened the source code. Reading LangGraph’s implementation of the ReAct loop was the "aha" moment. Seeing how they handled thought generation, tool execution, and state management gave me the mental model I couldn't get from the documentation. This hands-on understanding is what separates prototypes from production-ready systems. Even if you don't use this exact implementation in production, building it yourself provides the confidence to debug, extend, and customize any agent you encounter.

In this lesson, we will walk through the core components of a ReAct agent, step by step, following the code in our accompanying notebook. We will cover:

-   Setting up the environment and Gemini client.
-   Defining a mock tool and a tool registry.
-   Implementing the thought and action generation phases.
-   Building the main control loop to orchestrate the agent.
-   Testing our agent to see it succeed and handle failures gracefully.

## Setup and Environment

Our first step is to set up the Python environment. This ensures that your code runs smoothly and that the outputs match the traces we will analyze later. This lesson is based on a notebook, and we will follow its structure closely.

1.  We start by loading our environment variables. We use a simple utility function to load the `GOOGLE_API_KEY` from a `.env` file at the root of our project.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from `.../.env`
    Environment variables loaded successfully.
    ```
2.  Next, we import the necessary packages. We will use `google-genai` for interacting with the Gemini API, `pydantic` for data modeling, and a few standard libraries for type hinting.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```
3.  We initialize the Gemini client, which will handle our API requests.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is fast, cost-effective, and perfectly suited for our needs.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model ID in place, our environment is ready. Now, we can define the external capabilities our agent will use.

## Tool Layer: Mock Search Implementation

A ReAct agent’s power comes from its ability to interact with the outside world through tools. For this lesson, we will create a simple mock search tool. This approach allows us to focus purely on the ReAct mechanics without getting bogged down in external dependencies or API key management. A mock tool also gives us predictable responses, which is ideal for learning and testing.

Our mock tool is a Python function named `search`. It takes a string `query` as input and returns a string as output.

1.  The docstring is particularly important. It is not just for human developers; it serves as the primary documentation for the LLM. The model will read this docstring to understand what the tool does and how to use it. Clear, descriptive docstrings are essential for reliable tool selection.
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
    Inside the function, we have hardcoded responses for a few specific queries. For any other query, it returns a "not found" message. This fallback behavior is crucial for testing how the agent handles situations where a tool fails to provide the needed information.

2.  To manage our tools, we create a `TOOL_REGISTRY`. This dictionary maps the tool's name (as a string) to its callable function. This registry allows our control loop to dynamically look up and execute the correct tool based on the name provided by the LLM.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

In a production system, you would replace this mock `search` function with a real one that calls an external API like Google Search or a domain-specific knowledge base. The beauty of this design is that the agent's core logic remains unchanged. As long as the new function has the same name and a clear docstring, you can swap it in seamlessly.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is where the agent reasons about the user's query and the conversation history to decide on a plan. This separation of reasoning from acting is a core principle of the ReAct framework, improving reliability and interpretability by allowing the model to form a coherent plan before committing to a tool or a final answer [[11]](https://www.promptingguide.ai/techniques/react). We guide this process with a carefully crafted prompt.

1.  To ensure the LLM knows which tools are available, we create a helper function that generates a minimal XML description of our tools from the `TOOL_REGISTRY`. This function iterates through the tools, extracts their docstrings, and formats them into an XML block. Using XML tags like `<tool>` and `<description>` helps the model clearly distinguish the tool's name from its purpose [[8]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), [[9]](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/). This practice is also recommended in Gemini's official documentation, as using clear delimiters helps the model distinguish between instructions, context, and data [[12]](https://ai.google.dev/gemini-api/docs/prompting-strategies).
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

2.  Next, we define the prompt template for the thought generation phase. It instructs the agent to analyze the situation, consider the available tools, and state its next thought as a short paragraph. The `{conversation}` placeholder will be filled with the history of interactions.
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
    Let's inspect the final prompt to see how it looks with the tool definitions injected.
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

3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt, calls the Gemini model, and returns the generated thought as a clean text string.
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

This function produces a natural language reasoning step, like "I need to find the capital of France, so I should use the search tool." This thought provides the rationale for the next phase: Action.

## Action Phase: Function Calling and Parsing

After the agent generates a thought, it needs to decide on a concrete action. This could be calling a tool or, if it has enough information, providing a final answer to the user. We will use Gemini's native function calling capabilities to handle this decision-making process.

A key advantage of using a modern API like Gemini is that we do not need to include detailed tool schemas in our system prompt. Instead, we can pass the Python tool functions directly to the API configuration. The client automatically parses the function signatures and docstrings to create the necessary schema for the model [[10]](https://ai.google.dev/gemini-api/docs/function-calling). This keeps our prompts clean and focused on strategic guidance, while the API handles the technical details of tool integration.

1.  We start by defining the prompts for the action phase. We have two templates: one for the standard action-selection step and another to be used when we need to force the agent to provide a final answer, for example, when it reaches a maximum number of iterations.
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

2.  To handle the model's output, we define two Pydantic models: `ToolCallRequest` and `FinalAnswer`. These classes ensure that the data we parse from the model's response is structured and validated.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  Now, we implement the `generate_action` function. This is the core of the action phase.
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
        )
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=config,
        )
    
        # Extract the function call from the response (if present)
        candidate = response.candidates[0]
        if hasattr(candidate.content.parts[0], "function_call"):
            fc = candidate.content.parts[0].function_call
            name = fc.name
            args = dict(fc.args) if fc.args is not None else {}
            return ToolCallRequest(tool_name=name, arguments=args)
        
        # Otherwise, it's a final answer
        final_answer = "".join(part.text for part in candidate.content.parts)
        return FinalAnswer(text=final_answer.strip())
    ```
    This function first checks if a final answer should be forced. If so, it uses the `PROMPT_TEMPLATE_ACTION_FORCED` and returns a `FinalAnswer`. Otherwise, it sends the standard action prompt along with the list of available tools to the Gemini API. It then parses the response. If the model returns a `function_call` object, we extract the tool name and arguments and return a `ToolCallRequest`. If not, we assume the response is a text-based final answer and return a `FinalAnswer`.

This separation of thought and action, combined with native function calling, creates a robust and maintainable agent architecture.

## Control Loop: Messages, Scratchpad, Orchestration

With the thought and action phases defined, we can now build the control loop that orchestrates the entire ReAct cycle. This loop manages the conversation history, calls the thought and action generation functions, executes tools, and processes observations.

1.  To keep track of the conversation, we define a structured message system. The `MessageRole` enum categorizes each part of the interaction (e.g., `USER`, `THOUGHT`, `TOOL_REQUEST`). The `Message` Pydantic model holds the content and role for each message.
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

2.  We also create a `pretty_print_message` utility to display messages in a color-coded, readable format. This will make it easy to trace the agent's execution.
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

3.  The `Scratchpad` class acts as the agent's short-term memory. It holds a list of `Message` objects and provides methods to append new messages and convert the entire history to a string for the LLM's context.
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
    While this simple scratchpad is effective for short tasks, it has a critical limitation in long-running agents: context avalanche. With each turn, the full history is re-sent to the model, causing token consumption to grow quadratically, not linearly [[13]](https://www.zartis.com/ai-agent-cost-optimisation-why-token-cost-is-the-wrong-number-to-optimise/). In production, you would need more advanced strategies, like summarizing older turns, to manage this.

4.  This iterative cycle of sensing (observation), planning (thought), and acting (action) is not unique to AI agents. It mirrors the feedback control loops used in robotics and other self-adaptive systems, often described by models like MAPE (Monitor-Analyze-Plan-Execute) [[14]](https://www.sciencedirect.com/topics/computer-science/feedback-control-loop). This gives us a robust engineering pattern to follow as we implement the `react_agent_loop`, the heart of our agent. This function initializes the scratchpad with the user's question and then iterates through the Thought → Action → Observation cycle for a maximum number of turns.
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
                if action_name in tool_registry:
                    tool_function = tool_registry[action_name]
                    try:
                        observation_content = tool_function(**action_params)
                    except Exception as e:
                        observation_content = f"Error executing tool '{action_name}': {e}"
                else:
                    observation_content = f"Error: Tool '{action_name}' not found. Available tools: {list(tool_registry.keys())}"
    
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
    Inside the loop, it first generates a thought, then an action. If the action is a `FinalAnswer`, the loop terminates. If it's a `ToolCallRequest`, the function looks up the tool in the `TOOL_REGISTRY`, executes it, and appends the result as an `OBSERVATION` to the scratchpad. The loop continues until a final answer is reached or `max_turns` is exceeded, at which point it forces a concluding answer.

Image 1 visualizes this entire control flow, showing how messages are passed through the `Scratchpad` and how the loop orchestrates the Thought, Action, and Observation phases until a final answer is produced.

```mermaid
flowchart LR
  %% Start of the ReAct Control Loop
  subgraph "ReAct Control Loop"
    UI["User Input"]
    SP["Scratchpad<br/>(USER, THOUGHT, TOOL_REQUEST, OBSERVATION, FINAL_ANSWER)"]
    TG["Thought Generation<br/>(LLM Reasoning)<br/>`generate_thought()`"]
    MTR{"Maximum Turns Reached?"}
    AG["Action Generation<br/>(LLM Decision-making)<br/>`generate_action()`"]
    TE["Tool Execution"]
    OBS["Observation"]
    FA["Final Answer"]
  end

  TR["TOOL_REGISTRY"]

  %% Primary Flow
  UI -- "initial prompt" --> SP
  SP -- "context for reasoning" --> TG
  TG -- "updates with thought" --> SP

  %% Loop and Termination Logic
  SP -- "context for decision" --> MTR
  MTR -- "No" --> AG
  MTR -- "Yes (force termination)" --> FA

  AG -- "Tool Request" --> TE
  TE -- "uses" --> TR
  TE -- "produces" --> OBS
  OBS -- "adds to context" --> SP

  AG -- "Final Answer" --> FA

  %% Visual Grouping
  classDef llm_process fill:#e0f2f7,stroke:#0288d1,stroke-width:2px
  classDef memory fill:#fffde7,stroke:#fbc02d,stroke-width:2px
  classDef external fill:#fce4ec,stroke:#d81b60,stroke-width:2px
  classDef termination fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px

  class TG,AG llm_process
  class SP memory
  class TR external
  class FA termination
```
Image 1: A flowchart illustrating the ReAct control loop with iterative Thought, Action, and Observation cycles, including termination conditions and the role of the Scratchpad and TOOL_REGISTRY.

## Tests and Traces: Success and Graceful Fallback

Now that we have built the complete ReAct agent, it is time to test it. We will run two scenarios: one where the mock tool has the answer and one where it does not. Analyzing the output traces will validate that our loop, tool integration, and termination logic work as designed.

### Successful Run

First, let's ask a question that our mock `search` tool is programmed to answer: "What is the capital of France?" We will set `max_turns` to 2 and enable `verbose` to see the full trace.

1.  Here is the code to run the agent.
    ```python
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    The agent executes and prints a detailed trace of its process.

2.  **Turn 1:**
    -   **Thought:** The agent correctly identifies that it needs to find a factual answer and decides to use the `search` tool.
    -   **Tool Request:** It generates a call: `search(query='capital of France')`.
    -   **Observation:** The tool executes and returns the predefined answer: "Paris is the capital of France and is known for the Eiffel Tower."

3.  **Turn 2:**
    -   **Thought:** The agent observes the successful search result, recognizes it has the necessary information, and decides to formulate the final answer.
    -   **Final Answer:** It concludes with the correct answer: "Paris is the capital of France."

The full trace confirms that the agent successfully follows the Thought-Action-Observation cycle, uses the tool correctly, and terminates within the turn limit once it finds the answer.

### Graceful Fallback

Next, let's test a query our mock tool cannot answer: "What is the capital of Italy?" This will test the agent's ability to handle tool failures and its forced termination logic.

1.  We run the agent with the new question.
    ```python
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```

2.  **Turn 1:**
    -   **Thought:** The agent again decides to use the `search` tool.
    -   **Tool Request:** It calls `search(query='capital of Italy')`.
    -   **Observation:** The tool returns the fallback message: "Information about 'capital of Italy' was not found."

3.  **Turn 2:**
    -   **Thought:** Observing the failure, the agent adapts its strategy. It decides to broaden the search to just "Italy," hoping to find relevant information it can parse.
    -   **Tool Request:** It calls `search(query='Italy')`.
    -   **Observation:** This search also fails, returning "Information about 'Italy' was not found."

4.  **Forced Termination:**
    -   Having reached the `max_turns` limit of 2, the control loop triggers the forced final answer mechanism.
    -   **Final Answer (Forced):** The agent generates a polite and honest response: "I'm sorry, but I couldn't find information about the capital of Italy."

This trace demonstrates the agent's resilience. It does not crash on tool failure but instead tries a different approach. When it exhausts its attempts, the control loop ensures it terminates gracefully with a helpful message.

These tests confirm our from-scratch implementation of the ReAct loop is working correctly. We now have a solid foundation for building more complex and capable agents.

## Conclusion

By building a ReAct agent from the ground up, we have demystified the magic behind agentic frameworks. We have seen how a simple loop, combined with structured prompts and native function calling, can orchestrate a powerful Thought-Action-Observation cycle. This hands-on process provides a concrete mental model that is far more valuable than just using a high-level library. You now understand the core mechanics of how an agent reasons, acts on the world, and learns from feedback.

This foundation is critical. The principles of managing an agent's state and context will remain relevant even as the underlying technology evolves. For example, the advent of models with million-token context windows may reduce the need for complex summarization techniques, but it also introduces new challenges, as the model can "drown" in excessive information if the context is not managed carefully [[15]](https://www.linkedin.com/posts/andreashorn1_%F0%9D%97%A5%F0%9D%97%B2%F0%9D%97%B0%F0%9D%98%82%F0%9D%97%BF%F0%9D%98%80%F0%9D%97%B6%F0%9D%98%83%F0%9D%97%B2-%F0%9D%97%9F%F0%9D%97%AE%F0%9D%97%BB%F0%9D%97%B4%F0%9D%98%82%F0%9D%97%AE%F0%9D%97%B4%F0%9D%97%B2-%F0%9D%97%A0%F0%9D%97%BC%F0%9D%97%B1%F0%9D%97%B2%F0%9D%97%B9%F0%9D%98%80-activity-7427962498198290433-M4wm). Even if you use a framework like LangGraph in production for its convenience and features like parallel execution and monitoring, you now have the knowledge to look under the hood, debug effectively, and customize its behavior. You are no longer just a user of a black box; you are an AI Engineer who understands the principles.

This lesson concludes our exploration of the core building blocks of agents. In our upcoming lessons, we will build on this foundation to explore more advanced topics. In Lesson 9, we will dive into Agent Memory, exploring how agents can remember information across conversations. Following that, in Lesson 10, we will do a deep dive into Retrieval-Augmented Generation (RAG) to see how agents can leverage vast external knowledge bases.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)
- [2] *ReAct Agent*. (n.d.). IBM. [https://www.ibm.com/think/topics/react-agent](https://www.ibm.com/think/topics/react-agent)
- [3] *AI Agent Planning*. (n.d.). IBM. [https://www.ibm.com/think/topics/ai-agent-planning](https://www.ibm.com/think/topics/ai-agent-planning)
- [4] *Building effective agents*. (2024, December 19). Anthropic. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [5] *ReAct agent from scratch with Gemini 2.5 and LangGraph*. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/langgraph-example](https://ai.google.dev/gemini-api/docs/langgraph-example)
- [6] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2026, March 6). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review*. arXiv. [https://arxiv.org/pdf/2504.19678](https://arxiv.org/pdf/2504.19678)
- [7] Shankar, A. (2024, June 18). *Building ReAct Agents from Scratch using Gemini*. Medium. [https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [8] *Best practices for prompt engineering with the OpenAI API*. (n.d.). OpenAI Help Center. [https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [9] *Structured data response with Amazon Bedrock: Prompt Engineering and Tool Use*. (2025, June 26). Amazon Web Services. [https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/](https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/)
- [10] *Function calling*. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [11] *ReAct (Reasoning and Acting) Prompting*. (n.d.). Prompting Guide. [https://www.promptingguide.ai/techniques/react](https://www.promptingguide.ai/techniques/react)
- [12] *Prompt design strategies*. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [13] *AI Agent Cost Optimisation: Why Token Cost is the Wrong Number to Optimise*. (n.d.). Zartis. [https://www.zartis.com/ai-agent-cost-optimisation-why-token-cost-is-the-wrong-number-to-optimise/](https://www.zartis.com/ai-agent-cost-optimisation-why-token-cost-is-the-wrong-number-to-optimise/)
- [14] *Feedback Control Loop*. (n.d.). ScienceDirect. [https://www.sciencedirect.com/topics/computer-science/feedback-control-loop](https://www.sciencedirect.com/topics/computer-science/feedback-control-loop)
- [15] Horn, A. (n.d.). *LinkedIn Post on Relational Language Models*. LinkedIn. [https://www.linkedin.com/posts/andreashorn1_%F0%9D%97%A5%F0%9D%97%B2%F0%9D%97%B0%F0%9D%98%82%F0%9D%97%BF%F0%9D%98%80%F0%9D%97%B6%F0%9D%98%83%F0%9D%97%B2-%F0%9D%97%9F%F0%9D%97%AE%F0%9D%97%BB%F0%9D%97%B4%F0%9D%98%82%F0%9D%97%AE%F0%9D%97%B4%F0%9D%97%B2-%F0%9D%97%A0%F0%9D%97%BC%F0%9D%97%B1%F0%9D%97%B2%F0%9D%97%B9%F0%9D%98%80-activity-7427962498198290433-M4wm](https://www.linkedin.com/posts/andreashorn1_%F0%9D%97%A5%F0%9D%97%B2%F0%9D%97%B0%F0%9D%98%82%F0%9D%97%BF%F0%9D%98%80%F0%9D%97%B6%F0%9D%98%83%F0%9D%97%B2-%F0%9D%97%9F%F0%9D%97%AE%F0%9D%97%BB%F0%9D%97%B4%F0%9D%98%82%F0%9D%97%AE%F0%9D%97%B4%F0%9D%97%B2-%F0%9D%97%A0%F0%9D%97%BC%F0%9D%97%B1%F0%9D%97%B2%F0%9D%97%B9%F0%9D%98%80-activity-7427962498198290433-M4wm)