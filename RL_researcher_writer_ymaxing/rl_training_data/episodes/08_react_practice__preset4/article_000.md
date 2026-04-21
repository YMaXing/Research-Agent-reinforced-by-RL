# Build a ReAct Agent From Scratch

In the last lesson, we explored the theoretical foundations of agentic reasoning, focusing on the ReAct framework. We learned how agents can break down complex problems by interleaving thought, action, and observation. While understanding the theory is important, the real learning happens when you build it yourself. Frameworks like LangGraph, LangChain, or CrewAI are powerful, but their abstractions can sometimes hide the underlying logic that makes an agent tick, making it difficult to debug or customize your agent’s behavior [[8]](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/).

This lesson is 100% practical. We will build a minimal ReAct agent from scratch using only Python and the Gemini API. By implementing the complete Thought → Action → Observation loop, you will gain a concrete mental model of how these systems operate. This hands-on experience is what separates production-grade AI from mere prototypes. We will define a mock tool, generate thoughts, select actions with function calling, execute those actions, and orchestrate the entire process in a turn-based control loop.

By the end, you will have a working agent and the confidence to extend, debug, and customize it for your own applications.

## Setup and Environment

Our first step is to set up the Python environment to ensure everything runs smoothly. This involves loading API keys, importing the necessary libraries, and initializing the Gemini client. Our goal is to create a reproducible setup that matches the traces we will analyze later.

1.  First, we load our `GOOGLE_API_KEY` from an environment file. We use a custom utility function for this, which is a good practice for managing credentials securely.
    ```python
    from lessons.utils import env

    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from .../.env
    Environment variables loaded successfully.
    ```

2.  Next, we import the required packages. We will use `google-genai` for interacting with the Gemini API, `pydantic` for data validation, and `enum` and `typing` for creating structured and type-safe code. `pydantic` is particularly useful in AI engineering for enforcing schemas on data that might otherwise be unstructured, like LLM outputs. The `pretty_print` utility is a custom helper to make our traces more readable.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List

    from google import genai
    from google.genai import types

    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client. This object will be our main interface for making API calls.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, the latest model in the Gemini family as of this writing. It is designed for speed and efficiency, making it ideal for the rapid, iterative calls typical in agentic loops during development and experimentation.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model ready, we can now define the external capabilities our agent will use.

## Tool Layer: Mock Search Implementation

To build a ReAct agent, we need to give it tools to interact with the world. In a production system, these might be real API calls to a search engine, a database, or an internal service. For this lesson, however, we will use a mock search tool. This approach has several educational benefits.

First, it simplifies the learning process by allowing us to focus entirely on the ReAct mechanics without getting bogged down in API integrations, authentication, or managing external dependencies. Second, it provides predictable, consistent responses, which is essential for testing and ensuring our agent behaves as expected. This deterministic behavior allows us to isolate and debug the agent's reasoning logic, rather than questioning whether an external API is down or has changed. Finally, it makes this lesson self-contained and free to run.

Our mock search tool is a simple Python function that mimics a real search engine. It takes a query string and returns a predefined answer if the query matches a known pattern. If the query is unrecognized, it returns a "not found" message. This simulates how a real tool would respond to both successful and unsuccessful searches.

1.  We implement the `search` function. The docstring is important, as it provides a description that the LLM will use to understand the tool's purpose. The function's logic is straightforward: it converts the query to lowercase for case-insensitive matching and then checks for keywords. The `if all(...)` pattern is a simple way to check for multiple keywords, making the mock logic slightly more robust than a simple string equality check. The docstring is especially important, as the LLM will use its description to understand the tool's purpose and how to call it.
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

2.  We also create a `TOOL_REGISTRY`, a dictionary that maps the tool's name to its function. This allows our agent to dynamically look up and execute the correct function based on the name provided by the LLM.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

This simple setup is powerful. In a real-world application, you could easily swap this mock function with a call to the Google Search API, a query to a vector database for RAG, or an internal tool that books appointments, without changing any of the agent's core logic. The docstring and function signature provide a consistent interface—a contract—that the agent relies on. As long as the replacement tool honors this contract (same name, same parameters, similar return type), the agent can use it seamlessly. With our tool layer in place, we can now build the agent's reasoning capabilities.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct loop is "Thought." This is where the agent reasons about the user's query and the conversation history to decide on the next best action. To guide this process, we need to construct a prompt that gives the LLM all the necessary context.

Our thought-generation prompt includes three key pieces of information: the tools available to the agent, the conversation history so far, and a clear instruction to state its next thought. We will format the tool descriptions using XML tags, a common technique that helps the model clearly distinguish between different parts of the prompt [[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies).

1.  First, we create a helper function to build an XML description of our tools from the `TOOL_REGISTRY`. This function reads the docstring of each tool and formats it into a structured `<tool>` block.
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

2.  Next, we define the prompt template. It instructs the agent to analyze the situation and state its next thought as a short paragraph. Placeholders for `tools_xml` and `conversation` allow us to dynamically inject context.
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

3.  Let's print the template to see exactly what the LLM will receive. The output clearly shows the `<tool>` block containing the `search` tool's description and the `<conversation>` placeholder.
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

4.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt, calls the Gemini API, and returns the model's generated thought as a clean string.
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

It is important to note that the structure of this prompt is not arbitrary. Explicitly instructing the model to state its "thought" is a form of prompt engineering that enforces the first step of the ReAct cycle [[7]](https://www.decodingai.com/p/building-production-react-agents). By guiding the LLM to follow a specific format, we turn a passive text generator into an active problem solver that verbalizes its reasoning before acting. This explicit reasoning step is what makes the agent’s behavior transparent and easier to debug.

For more advanced implementations, insights from cognitive science can further refine this phase. Research has shown that humans often regulate their behavior more effectively using second-person self-talk ("You should...") rather than first-person ("I should..."). Applying this to the thought-generation prompt—by framing instructions as if the agent is coaching itself—could potentially improve its planning and execution on complex tasks [[9]](http://dolcoslab.beckman.illinois.edu/sites/default/files/DolcosS%26Albarracin_2014_EJSP.pdf).

With a coherent thought generated, the agent has a plan. The next step is to translate this plan into a concrete action, which could be either calling a tool or providing a final answer to the user.

## Action Phase: Function Calling and Parsing

After the "Thought" phase, the agent moves to the "Action" phase. Here, it decides whether to use a tool to gather more information or to provide a final answer if it has enough context. We will implement this using Gemini's native function calling capabilities.

A key design choice here is to separate the prompts for thought and action. The thought prompt includes detailed tool descriptions to help the LLM reason about what to do. The action prompt, however, is simpler. We do not need to manually include tool schemas in the action prompt because we pass the Python tool functions directly to the Gemini API via its `tools` configuration.

This is a powerful feature of modern LLM APIs. The API automatically inspects the function signature (`def search(query: str)`) and its docstring to create a schema that the model can understand. This keeps our prompt clean and focused on the high-level strategic decision: "should I call a tool or answer now?". This separation also allows for easier tool management. You can add or modify tools just by updating the Python functions, without having to change the action prompt.

Image 1: A sequence diagram illustrating the structured interaction of Gemini's function calling in the action phase of a ReAct agent, including the loop for using another function or providing a final answer.

1.  We define two prompt templates for the action phase. The first is the default prompt, and the second is a specialized one used to force the agent to provide a final answer, which is useful for preventing infinite loops.
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

2.  We create Pydantic models to represent the two possible outcomes of the action phase: a `ToolCallRequest` or a `FinalAnswer`. This provides a structured way to handle the model's output.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")


    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  The `generate_action` function orchestrates this phase. It selects the appropriate prompt, configures the Gemini client with the available tools, and calls the model. It then parses the response to determine if the model generated a function call or a text-based final answer.
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
    The `force_final` flag is a crucial feature for production-ready agents. It provides a mechanism to terminate the ReAct loop gracefully, for instance, when a maximum number of turns is reached. This prevents the agent from getting stuck in infinite loops or making excessive tool calls, ensuring a predictable and controlled execution.

## Control Loop: Messages, Scratchpad, Orchestration

Now we will build the main control loop that orchestrates the entire Thought → Action → Observation cycle. This loop manages the conversation history, executes actions, and processes observations, tying together the components we have built.

At the core of our loop is a `Scratchpad`, which acts as the agent's short-term memory. It stores a sequence of messages representing every step of the interaction: the user's initial query, the agent's internal thoughts, the tool calls it makes, the observations it receives, and the final answer.

1.  We start by defining the data structures for our messages. `MessageRole` is an `Enum` that categorizes each message, and the `Message` class is a Pydantic model that holds the role and content.
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
    This structured approach to messages is fundamental to the agent's performance. Proper role categorization helps the model maintain context across turns for coherent reasoning [[10]](https://www.linkedin.com/posts/akash-ghosh-7b0210302_python-ai-gemini-activity-7383075419429769216-iGgX). Research confirms that models rely on consistent scratchpad formatting to reason effectively; inconsistencies can disrupt performance and make error recovery more difficult [[11]](https://alignment.anthropic.com/2025/distill-paraphrases/).

2.  To make the agent's process easy to follow, we create a helper function to pretty-print each message. This will give us a clear, color-coded trace of the agent's execution.
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

3.  The `Scratchpad` class manages the list of messages. Its `append` method adds a new message and, if `verbose` is enabled, prints it to the console. It also tracks the current turn number to provide context in the logs.
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

4.  Finally, we implement the `react_agent_loop` function, the heart of our agent. It initializes the scratchpad and iterates through the ReAct cycle for a defined number of turns. In each turn, it generates a thought, then an action. If the action is a tool call, it executes the tool and records the observation. The loop terminates when the agent produces a final answer or reaches the maximum number of turns, forcing it to conclude.
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
    This iterative cycle is analogous to feedback loops in other engineering disciplines. It mirrors the rapid iterations of Agile software development, where quick feedback enables continuous course correction [[12]](https://revelry.co/insights/development/feedback-loops/). The structured Thought-Action-Observation sequence also parallels the checklists used in high-stakes domains like aviation, ensuring systematic error-checking at each step [[13]](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure).

Image 2: A flowchart illustrating the ReAct control loop with LangGraph implementation concepts.

## Tests and Traces: Success and Graceful Fallback

With our agent fully implemented, it is time to test it. By analyzing the execution traces, we can verify that the Thought-Action-Observation loop works as designed and that the agent can handle both successful queries and situations where it needs to fail gracefully.

### Successful Execution

Let’s start with a straightforward factual question that our mock `search` tool can answer: *"What is the capital of France?"* We will run the agent for a maximum of two turns and enable verbose logging to see each step.

1.  We call our `react_agent_loop` with the question.
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
    The search tool provided the answer directly. I can now formulate the final answer.

    Final answer (Turn 2/2):
    Paris is the capital of France.
    ```
    The trace clearly shows the ReAct cycle in action. In the first turn, the agent thinks, decides to use the `search` tool, and gets an observation. In the second turn, it recognizes that it has the answer and provides it, successfully completing the task within the turn limit.

This pattern of iterative reasoning and tool use is not just academic; it is used in high-stakes production systems. For example, financial institutions use ReAct-style agents for fraud detection, where an agent might analyze transaction data, search for related patterns, and escalate to a human if necessary. This structured, verifiable reasoning is essential for building reliable systems in critical domains [[14]](https://towardsai.net/p/machine-learning/production-ready-ai-agents-8-patterns-that-actually-work-with-real-examples-from-bank-of-america-coinbase-uipath).

### Graceful Fallback

Now, let's test a query that our mock tool cannot answer: *"What is the capital of Italy?"* This will test the agent's ability to handle tool failures and adapt its strategy.

1.  We run the loop again with the new question.
    ```python
    # A question that the mock search tool does not support, to test fallback
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
    The previous search for "capital of Italy" failed. I will try a broader search for just "Italy" to see if I can find any relevant information that might lead me to the capital.

    Tool request (Turn 2/2):
    search(query='Italy')

    Observation (Turn 2/2):
    Information about 'Italy' was not found.

    Final answer (Forced):
    I'm sorry, but I was unable to find the capital of Italy using the available tools.
    ```
    This trace demonstrates the agent's resilience. After the first search fails, the agent does not give up. In its second thought, it formulates a new, broader strategy. When that also fails and it hits the `max_turns` limit, the control loop triggers the `force_final` flag. This results in a final, honest admission that it could not find the answer. This graceful fallback is a key feature of a robust agent.

This mechanism can be seen as a basic safety feature, analogous to principles from aviation. Just as pilots maintain manual proficiency and follow checklists to prevent over-reliance on automation, the `max_turns` limit ensures the agent cannot get stuck in unproductive loops, maintaining predictable behavior. This kind of built-in guardrail is essential for designing safer, more reliable agents [[15]](https://www.nature.com/articles/s41746-026-02410-1).

These tests confirm that our end-to-end implementation is working correctly. The agent can successfully use tools to find answers and can adapt and terminate gracefully when it cannot.

## Conclusion

We have successfully built a ReAct agent from scratch, moving from individual components to a fully orchestrated control loop. By implementing the Thought-Action-Observation cycle ourselves, we have demystified what happens inside agentic frameworks. You now have a concrete mental model of how an agent reasons about a problem, selects and executes tools, and learns from observations to achieve its goals.

This foundational understanding is one of the core skills you should master as an AI Engineer. It empowers you to move beyond simply using pre-built frameworks and gives you the ability to design, debug, and extend custom agents with confidence.

Remember that this article is part of a longer series of 9 pieces on the AI Agents Foundations that will give you the tools to morph from a Python developer to an AI Engineer. In our next lessons, we will build upon this foundation, exploring more advanced topics like agent memory and Retrieval-Augmented Generation (RAG). The principles you have learned here will be essential as we construct more sophisticated and capable AI systems.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)
- [2] *Prompt design strategies*. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [3] *Function calling*. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [4] Shankar, A. (2024, June 10). *Building ReAct Agents from Scratch using Gemini*. Medium. [https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [5] Schmid, P. (2024, March 4). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. [https://www.philschmid.de/langgraph-gemini-2-5-react-agent](https://www.philschmid.de/langgraph-gemini-2-5-react-agent)
- [6] Pasternak, R. (2024, November 5). *Building a Python React Agent Class: A Step-by-Step Guide*. Neradot. [https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide](https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide)
- [7] Iusztin, P. (2025, November 18). *Building Production ReAct Agents From Scratch Is Simple*. Decoding AI. [https://www.decodingai.com/p/building-production-react-agents](https://www.decodingai.com/p/building-production-react-agents)
- [8] Daily Dose of DS. (2024, June 10). *AI Agents Crash Course - Part 10: ReAct Framework with Implementation*. [https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/)
- [9] Dolcos, S., & Albarracin, D. (2014). *The inner speech of behavioral regulation*. European Journal of Social Psychology. [http://dolcoslab.beckman.illinois.edu/sites/default/files/DolcosS%26Albarracin_2014_EJSP.pdf](http://dolcoslab.beckman.illinois.edu/sites/default/files/DolcosS%26Albarracin_2014_EJSP.pdf)
- [10] Ghosh, A. (2024). *Post on Gemini CLI agent*. LinkedIn. [https://www.linkedin.com/posts/akash-ghosh-7b0210302_python-ai-gemini-activity-7383075419429769216-iGgX](https://www.linkedin.com/posts/akash-ghosh-7b0210302_python-ai-gemini-activity-7383075419429769216-iGgX)
- [11] Pinhanez, C. et al. (2025). *Distilling Step-by-Step! Out-of-Distribution Generalization for Large Language Models using Paraphrased Self-Explanation*. Anthropic. [https://alignment.anthropic.com/2025/distill-paraphrases/](https://alignment.anthropic.com/2025/distill-paraphrases/)
- [12] *Optimizing Feedback Loops for Iterative Agile Development*. (n.d.). Revelry. [https://revelry.co/insights/development/feedback-loops/](https://revelry.co/insights/development/feedback-loops/)
- [13] *Agent steps and structure*. (n.d.). Hugging Face. [https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure)
- [14] Iusztin, P. (2024). *Production-Ready AI Agents: 8 Patterns that Actually Work*. Towards AI. [https://towardsai.net/p/machine-learning/production-ready-ai-agents-8-patterns-that-actually-work-with-real-examples-from-bank-of-america-coinbase-uipath](https://towardsai.net/p/machine-learning/production-ready-ai-agents-8-patterns-that-actually-work-with-real-examples-from-bank-of-america-coinbase-uipath)
- [15] Singh, I., et al. (2026). *From aviation safety to AI safety: learning from the past to build a safer future*. npj Digital Medicine. [https://www.nature.com/articles/s41746-026-02410-1](https://www.nature.com/articles/s41746-026-02410-1)