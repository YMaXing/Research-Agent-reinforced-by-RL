# Building a ReAct Agent From Scratch: A Step-by-Step Guide

In our last lesson, we covered the theory behind ReAct, a powerful pattern for building AI agents that can reason and take action. Now, it is time to move from theory to practice. While frameworks like LangChain or CrewAI are great for getting started, they often hide the underlying logic that makes an agent work. Understanding these fundamentals is what separates building prototypes from shipping production-grade AI.

This lesson is 100% practical. We will build a minimal ReAct agent from scratch using only Python and the Gemini API. By implementing the full Thought → Action → Observation loop yourself, you will gain a concrete mental model of how these systems operate. This hands-on experience is essential for debugging, extending, and customizing agents with confidence.

We will walk through the entire process, step-by-step:
- Setting up the environment.
- Defining a mock tool for the agent to use.
- Generating thoughts to guide the agent's reasoning.
- Selecting and parsing actions with function calling.
- Building the control loop that orchestrates the agent's behavior.
- Testing the agent to see it succeed and handle failure gracefully.

## Setup and Environment

First, we need to ensure our environment is configured correctly. This setup will allow you to run the code from the lesson's notebook and get the same results.

1. We start by loading our environment variables. We use a simple helper function to load the `GOOGLE_API_KEY` from our `.env` file.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Environment variables loaded successfully.
    ```

2. Next, we import the necessary packages. We will use `google-genai` to interact with the Gemini API, `pydantic` for data modeling, and a few standard libraries for type hinting.
    ```python
    import json
    from enum import Enum
    from typing import List
    
    from google import genai
    from google.genai import types
    from pydantic import BaseModel, Field
    
    from lessons.utils import pretty_print
    ```

3. We initialize the Gemini client. This client will handle all our requests to the Gemini API.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4. Finally, we define the model we will use. For this lesson, we will use `gemini-1.5-flash`, a fast and cost-effective model perfect for our needs.
    ```python
    MODEL_ID = "gemini-1.5-flash"
    ```

With the client and model in place, we can now define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

To build a useful agent, we need to give it tools. In a production system, these tools would interact with real-world APIs, databases, or other external systems. For this lesson, however, we will use a mock search tool. This approach offers several advantages for learning:

- **It simplifies the focus:** We can concentrate on the ReAct mechanics without worrying about API keys or external dependencies.
- **It provides predictability:** The mock tool returns consistent, predefined responses, making it easier to test and debug our agent's behavior.
- **It eliminates complexity:** We avoid the need for network requests and error handling related to external services.

Our mock search tool will simulate a simple search engine. It will have a few hardcoded responses for specific queries and a fallback response for anything it does not recognize.

1. We define the `search` function. The docstring is important here; it describes what the tool does, and this information will be passed to the LLM to help it decide when to use the tool.
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

2. We create a `TOOL_REGISTRY` to map the tool's name to its function. This allows our agent to call the tool by its string name, which is how LLMs typically specify actions.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```

This simple mock tool is all we need to demonstrate the full ReAct loop. In a real-world application, you could easily swap this function with one that calls an actual API, like Google Search or a private knowledge base, without changing the agent's core logic.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct loop is "Thought." This is where the agent analyzes the user's query and its current context to decide what to do next. We will implement a function that generates this thought by prompting the LLM.

This explicit separation of concerns is a core principle for building reliable agents. By using structured formats like XML, we make it easier for the model to distinguish between its instructions, the available tools, and the ongoing conversation history [[6]](https://ai.google.dev/gemini-api/docs/prompting-strategies). This reduces ambiguity and helps prevent the model from getting confused, which in turn improves the interpretability and trustworthiness of its reasoning process [[7]](https://www.promptingguide.ai/techniques/react).

1. We start by creating a function that generates an XML description of our available tools. This structured format makes it easy for the LLM to understand what tools it can use. We will insert this XML block into our prompt.
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

2. Let's inspect the full prompt template to see what the LLM will receive.
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
    The output shows that the prompt clearly defines the agent's goal, lists the available tools with their descriptions inside an XML block, and provides a placeholder for the conversation history.

3. Now, we implement the `generate_thought` function. This function takes the current conversation history, formats the prompt with it, and calls the Gemini API to generate the agent's next thought.
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

With a coherent thought generated, the agent must now decide whether to call a tool to gather more information or conclude with a final answer. This brings us to the "Action" phase.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent decides what to do based on its thought. It can either call one of its tools or provide a final answer to the user. We will implement this using Gemini's native function calling capabilities, which we covered in Lesson 6. This approach is more robust and reliable than trying to parse actions from plain text.

The system prompt for this phase is designed to be high-level. It instructs the agent to choose an action but does not include the technical details of the tools.

```text
You are selecting the best next action to reach the user goal.

Conversation so far:
<conversation>
{conversation}
</conversation>

Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
```

Instead of putting tool schemas in the prompt, we pass the Python functions directly to the Gemini API's `tools` configuration. This reflects a fundamental principle of reliable prompt engineering: separate instructions from data [[8]](https://stevekinney.com/writing/prompt-engineering-frontier-llms). The prompt provides the high-level instruction (the goal), while the tool definitions serve as structured data for the model to use. The API automatically extracts the function name, docstring, and parameters, keeping our prompts clean and focused on strategic guidance while the API handles the technical details.

1. We start by defining two Pydantic models to represent the possible outcomes of the action phase: a `ToolCallRequest` or a `FinalAnswer`. This gives us a structured way to handle the model's decision.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

2. Next, we define the prompt templates. We have one for the standard action selection and another, `PROMPT_TEMPLATE_ACTION_FORCED`, which we will use to force the agent to provide a final answer when it reaches its turn limit.
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

3. Now, we implement the `generate_action` function. This is the core of the action phase. It sends the prompt and tool definitions to Gemini and parses the response.
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
            config=config
        )
    
        # Extract the function call from the response (if present)
        candidate = response.candidates[0]
        if hasattr(candidate.content.parts[0], "function_call"):
            function_call = candidate.content.parts[0].function_call
            name = function_call.name
            args = dict(function_call.args) if function_call.args is not None else {}
            return ToolCallRequest(tool_name=name, arguments=args)
        
        # Otherwise, it's a final answer
        final_answer = "".join(part.text for part in candidate.content.parts)
        return FinalAnswer(text=final_answer.strip())
    ```
    The `force_final` flag is a crucial feature for ensuring the agent terminates gracefully. When an agent gets stuck in a loop or exceeds a predefined number of steps, we can use this flag to instruct the model to stop calling tools and summarize its findings in a final answer.

## Control Loop: Messages, Scratchpad, and Orchestration

Now we build the main ReAct control loop that orchestrates the Thought → Action → Observation cycle. This pattern is conceptually similar to feedback control loops used in robotics and other engineering disciplines, where a system continuously senses its environment, plans a response, and acts to achieve a goal [[9]](https://www.sciencedirect.com/topics/computer-science/feedback-control-loop). Our loop will manage the conversation history, call the thought and action phases, execute tools, and process the results.

Image 1: A flowchart illustrating the core ReAct control loop.

The diagram in Image 1 shows the flow we are about to implement. The agent receives a query, enters a loop of thinking and acting, and continues until it determines it is done and can provide a final answer.

### Message Structure

To keep track of the agent's interactions, we will use a structured message system.

1. We define a `MessageRole` enum to categorize each message in the conversation. This helps us and the agent understand the context of each piece of information.
    ```python
    class MessageRole(str, Enum):
        """Enumeration for the different roles a message can have."""
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final answer"
    ```

2. We create a `Message` class using Pydantic. Each message will have a role and content. This structure is the foundation of our agent's memory, or "scratchpad."
    ```python
    class Message(BaseModel):
        """A message with a role and content, used for all message types."""
        role: MessageRole = Field(description="The role of the message in the ReAct loop.")
        content: str = Field(description="The textual content of the message.")
    
        def __str__(self) -> str:
            """Provides a user-friendly string representation of the message."""
            return f"{self.role.value.capitalize()}: {self.content}"
    ```

3. We also add a helper function to pretty-print messages, which will make it easier to trace the agent's execution.
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

### The Scratchpad

The `Scratchpad` class manages the list of messages. It appends new messages and can optionally print them verbosely for debugging. At each turn, the entire scratchpad is converted to a string and fed back to the LLM, providing the full context for its next decision.

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
While this simple scratchpad is effective for short tasks, it has a critical limitation for longer interactions: the "context avalanche." Because the entire history is sent on each turn, token consumption can grow quadratically, not linearly, becoming expensive and slow [[10]](https://www.zartis.com/ai-agent-cost-optimisation-why-token-cost-is-the-wrong-number-to-optimise/). In production, you would need more sophisticated context management, like summarizing past turns, which we will explore in future lessons on agent memory.

### The Control Loop

Finally, we implement the `react_agent_loop`. This function orchestrates the entire process.

- It starts with the user's initial question.
- In each turn, it generates a `Thought`, then an `Action`.
- If the action is a `ToolCallRequest`, it executes the tool, creates an `Observation` message with the result, and continues the loop.
- If the action is a `FinalAnswer`, the loop terminates and returns the answer.
- If the agent reaches the `max_turns` limit, it calls `generate_action` one last time with `force_final=True` to ensure a graceful exit.

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
                observation_content = f"Unknown tool '{action_name}'. Available tools: {list(tool_registry.keys())}"


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
This loop is the engine of our ReAct agent, tying together all the components we have built.

## Tests and Traces: Success and Graceful Fallback

With the complete loop implemented, it is time to test our agent. By analyzing the execution traces, we can verify that the agent behaves as expected in both successful and unsuccessful scenarios.

### Successful Execution

First, let's ask a simple factual question that our mock `search` tool can answer: "What is the capital of France?" We will set `max_turns` to 2 to see if it can solve it within the limit.

1. We define the question and run the loop.
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
    I have found the answer to the user's question. I can now provide the final answer.
    
    Final answer (Turn 2/2):
    Paris is the capital of France.
    ```

2. The trace shows the agent working perfectly:
    - **Turn 1:** It receives the user's query, thinks about how to solve it, and correctly decides to use the `search` tool. It then observes the tool's output.
    - **Turn 2:** With the information from the observation, it realizes it has the answer and generates a `FinalAnswer`.
    
    This confirms that our thought, action, and observation cycle is working correctly.

### Graceful Fallback

Now, let's test the agent's resilience. We will ask a question that our mock tool cannot answer: "What is the capital of Italy?" This will test the agent's ability to handle tool failure and the forced termination logic.

1. We run the loop with the new question.
    ```python
    question = "What is the capital of Italy?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User (Turn 1/2):
    What is the capital of Italy?
    
    Thought (Turn 1/2):
    The user is asking for the capital of Italy. I can use the search tool to find this information.
    
    Tool request (Turn 1/2):
    search(query='capital of Italy')
    
    Observation (Turn 1/2):
    Information about 'capital of Italy' was not found.
    
    Thought (Turn 2/2):
    The previous search for 'capital of Italy' failed. I will try a broader search for just 'Italy' to see if I can find the capital that way.
    
    Tool request (Turn 2/2):
    search(query='Italy')
    
    Observation (Turn 2/2):
    Information about 'Italy' was not found.
    
    Final answer (Forced):
    I'm sorry, but I couldn't find information about the capital of Italy using the available tools.
    ```
2. The trace demonstrates several important behaviors:
    - **Adaptation:** After the first search fails, the agent's thought in Turn 2 shows it adapting its strategy by trying a broader query.
    - **Tool Failure Handling:** The agent correctly processes the "not found" observation and continues its reasoning process.
    - **Forced Termination:** When it reaches the `max_turns` limit, the loop correctly triggers the `force_final=True` path, generating a polite and informative final answer that acknowledges its failure.

These tests confirm that our agent is not only capable of solving tasks but can also handle failures gracefully, a critical feature for any production system.

## Conclusion

By building a ReAct agent from scratch, we have demystified the core mechanics of the Thought-Action-Observation loop. We have seen how to structure prompts, define tools, generate thoughts, parse actions, and orchestrate the entire process within a control loop. This hands-on approach provides a solid mental model for how these systems work under the hood.

This foundational knowledge is what will allow you to build, debug, and extend more complex agents with confidence. Even if you end up using a framework in production, understanding these principles is one of the core skills you should master as an AI Engineer.

In our next lesson, we will build on this foundation by exploring how to give agents memory, allowing them to remember past interactions and learn over time.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv. https://arxiv.org/pdf/2210.03629
- [2] ReAct Agent. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [3] AI Agent Planning. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [4] Building effective agents. (2024). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [5] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [6] Prompt design strategies. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [7] ReAct. (n.d.). Prompting Guide. https://www.promptingguide.ai/techniques/react
- [8] Kinney, S. (n.d.). Prompt Engineering for Frontier LLMs. https://stevekinney.com/writing/prompt-engineering-frontier-llms
- [9] Feedback Control Loop. (n.d.). ScienceDirect. https://www.sciencedirect.com/topics/computer-science/feedback-control-loop
- [10] AI Agent Cost Optimisation: Why Token Cost Is The Wrong Number To Optimise. (n.d.). Zartis. https://www.zartis.com/ai-agent-cost-optimisation-why-token-cost-is-the-wrong-number-to-optimise/