# Lesson 8: Building a ReAct Agent From Scratch

In our previous lessons, we explored the theoretical foundations of AI agents, from context engineering to the ReAct framework. This approach, which synergizes reasoning and acting, is more than a novel pattern. It is a direct response to a core LLM weakness—hallucination—by grounding the model in reality with external tools [[5]](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/). It also builds on foundational AI concepts, where an agent perceives its environment and acts upon it, creating a feedback loop between deliberation and action [[6]](https://www.scitepress.org/Papers/2026/144223/144223.pdf). Theory is essential, but true understanding comes from building.

This lesson is 100% practical. We will move from theory to implementation by building a minimal ReAct agent from scratch using only Python and the Gemini API. You will implement the full Thought → Action → Observation loop, define a mock tool, generate thoughts, select actions with function calling, and orchestrate the entire process.

This hands-on approach will give you a concrete mental model of how reasoning agents work. By the end, you will have a working control loop that you can debug, extend, and customize with confidence, providing a solid foundation for the more advanced topics we will cover in future lessons.

## Setup and Environment

Before we start building, let's set up our environment to ensure the code from the [course notebook](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb) runs smoothly. This initial setup involves loading our API keys, importing the necessary packages, and initializing the Gemini client.

1.  First, we load our environment variables. Our utility function handles finding the `.env` file and loading the `GOOGLE_API_KEY`.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from .../.env
    Environment variables loaded successfully.
    ```
2.  Next, we import the required packages, including `google.genai` for the Gemini API, `pydantic` for data modeling, and some utilities for printing.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```
3.  We initialize the Gemini client and define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is fast and cost-effective for our task.
    ```python
    client = genai.Client()
    MODEL_ID = "gemini-2.5-flash"
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
With our client and model ready, we can now define the external capabilities our agent will use.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to use tools to interact with the world. For this lesson, we will create a simple mock `search` tool. Using a mock tool instead of a real API call allows us to focus purely on the ReAct mechanics without worrying about external dependencies or API keys. It also gives us predictable responses, which is great for testing and debugging.

Our mock tool is a simple Python function. The docstring is important because, as we saw in Lesson 6, modern function-calling APIs use it to understand what the tool does and how to use it.

1.  We define the `search` function with a clear docstring and predefined responses for specific queries. This mimics how a real search API might behave. For any query that does not match our predefined cases, it returns a "not found" message, which lets us test the agent's fallback behavior.
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
2.  We also create a `TOOL_REGISTRY` to map the tool's name to the function itself. This allows our agent to plan with a symbolic name (`"search"`) and lets our code resolve that name to the actual Python function for execution.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
In a production system, you could easily swap this mock function with a real API call to Google Search or a domain-specific knowledge base while keeping the function signature and docstring the same. With our tool defined, let's move on to the first phase of the ReAct loop: Thought.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is the agent's internal monologue, where it reasons about the user's query and plans its next step. To guide this process, we construct a prompt that provides the LLM with all the necessary context: the available tools, the conversation history, and the user's goal.

1.  We start by creating a function to convert our tool registry into a minimal XML description. This format helps the LLM clearly distinguish the tools from other parts of the prompt. The description is generated directly from the tool's docstring.
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
    ```
2.  Next, we define our prompt template. It instructs the agent on its goal and provides placeholders for the tool descriptions and the ongoing conversation history.
    ```python
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
    When printed, this template shows the structured context the LLM will receive, including the `<tool>` block for our `search` function and the `<conversation>` placeholder.
3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt with the tool descriptions, and calls the Gemini model to generate the next thought.
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
With a coherent thought generated, the agent must now decide whether to call a tool or conclude with a final answer. This brings us to the Action phase.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent translates its thought into a concrete action. We will use Gemini's native function-calling capabilities, which we covered in Lesson 6. This approach is powerful because the model can automatically understand our tool's purpose and parameters from its Python definition, simplifying our prompt.

Instead of manually describing the tool's signature in the prompt, we pass the Python function directly to the API. The Gemini client handles the rest, allowing our prompt to focus on high-level strategic guidance.

1.  We define two prompt templates. The first is for the default action step, and the second is a specialized prompt to force a final answer when the agent reaches its turn limit.
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
2.  We define Pydantic models to represent the two possible outcomes: a `ToolCallRequest` or a `FinalAnswer`. This gives us a structured way to handle the model's decision.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
3.  The `generate_action` function orchestrates this step. It passes the available tools to the Gemini API and disables automatic execution so we can parse the response ourselves. If the model returns a `function_call`, we parse it into our `ToolCallRequest` model. Otherwise, we treat the text response as a `FinalAnswer`. The `force_final` flag allows us to instruct the model to conclude, which is useful for preventing infinite loops.
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

Now that we have the Thought and Action phases, we need to orchestrate them in a loop.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the engine of our ReAct agent. It orchestrates the Thought → Action → Observation cycle, manages the conversation history, and decides when to terminate. To build it, we first need a structured way to represent the different steps of the dialogue.

This process creates a feedback loop analogous to human problem-solving. Think about packing for a trip: you identify considerations like the weather (Thought), consult a forecast (Action), and use that information to adjust your clothing choices (Observation) before repeating the cycle [[7]](https://www.ibm.com/think/topics/react-agent).

1.  We define `MessageRole` and `Message` Pydantic models. This allows us to categorize each interaction as a user query, an internal thought, a tool request, an observation, or a final answer. This structure is key for both the agent's reasoning and our ability to debug the process.
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
2.  Next, we create a `Scratchpad` class. This class holds a list of `Message` objects and acts as the agent's short-term memory for the current task. It provides an `append` method to add new messages and a `to_string` method to serialize the entire history into a format the LLM can understand.
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
                # ... pretty printing logic ...
    
        def to_string(self) -> str:
            return "\n".join(str(m) for m in self.messages)
    ```
3.  With these structures in place, we can implement the main `react_agent_loop`. This function orchestrates the entire process. At each turn, it generates a thought, then an action. If the action is a `FinalAnswer`, the loop terminates. If it is a `ToolCallRequest`, the function executes the corresponding tool, captures the output as an "Observation," appends it to the scratchpad, and continues to the next turn. This integration of the observation is critical, as it provides the feedback the agent needs to refine its reasoning. If the loop reaches its `max_turns` limit, it calls `generate_action` one last time with `force_final=True` to ensure a graceful exit.
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
    
            # Generate a thought and an action
            thought_content = generate_thought(scratchpad.to_string(), tool_registry)
            thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
            scratchpad.append(thought_message, verbose=verbose)
    
            action_result = generate_action(scratchpad.to_string(), tool_registry=tool_registry)
    
            # Handle final answer
            if isinstance(action_result, FinalAnswer):
                final_answer = action_result.text
                final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                scratchpad.append(final_message, verbose=verbose)
                return final_answer
    
            # Handle tool request
            if isinstance(action_result, ToolCallRequest):
                # ... (add tool request to scratchpad) ...
    
                # Run the action and get the observation
                observation_content = ""
                tool_function = tool_registry.get(action_result.tool_name)
                try:
                    if tool_function:
                        observation_content = tool_function(**action_result.arguments)
                    else:
                        observation_content = f"Error: Unknown tool '{action_result.tool_name}'. Available tools: {list(tool_registry.keys())}"
                except Exception as e:
                    observation_content = f"Error executing tool '{action_result.tool_name}': {e}"
    
                # Add the observation to the scratchpad
                observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
                scratchpad.append(observation_message, verbose=verbose)
    
            # Force final answer if max turns reached
            if turn == max_turns:
                # ... (logic to generate and return a forced final answer) ...
    ```

## Tests and Traces: Success and Graceful Fallback

Now that we have built the complete ReAct loop, let's test it with two examples to validate its behavior. We will analyze the printed traces to see how the agent handles both a successful query and a case where its tool cannot find the answer.

First, we ask a simple factual question that our mock `search` tool can answer: `"What is the capital of France?"`

```python
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The trace shows a perfect two-turn execution. In the first turn, the agent thinks it should use the `search` tool, makes the tool request `search(query='capital of France')`, and receives the observation "Paris is the capital of France...". In the second turn, it recognizes it has the answer and provides the final response. This confirms that the Thought → Action → Observation cycle works as expected.

Next, let's test the graceful fallback behavior with a query our mock tool does not support: `"What is the capital of Italy?"`

```python
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

In this trace, the agent first attempts to search for "capital of Italy" but gets a "not found" observation. In its second thought, it adapts its strategy and tries a broader search for just "Italy". When that also fails, it reaches the `max_turns` limit. The control loop then correctly triggers the forced final answer path, and the agent responds that it could not find the information. This demonstrates the agent's resilience and the importance of having a termination condition to handle unsuccessful tool interactions.

These tests confirm our minimal ReAct agent is working correctly, providing a solid baseline for future extensions.

## Conclusion

In this lesson, we moved from theory to practice and built a ReAct agent from scratch. By implementing each component—the mock tool, the thought and action phases, and the control loop—we have gained a concrete mental model of how these systems operate. We have seen how an agent can reason about a task, use tools to gather information, and adapt its strategy based on observations.

This hands-on experience is foundational. While our minimal agent is a great learning tool, it’s important to remember that such systems still fall short of human expert performance on complex tasks [[8]](https://www.promptingguide.ai/techniques/react). Even so, understanding the underlying mechanics of the Thought-Action-Observation loop is a core skill for any AI engineer, even if you use frameworks like LangGraph in production. It empowers you to debug, customize, and extend agentic systems with confidence. In our next lessons, we will build on this foundation as we explore more advanced topics like agent memory and Retrieval-Augmented Generation (RAG).

## References
- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. https://arxiv.org/pdf/2210.03629
- [2] Stryker, C. (n.d.). *AI agent planning*. IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [3] S., E., & Zhang, B. (2024, December 19). *Building effective agents*. Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [4] *ReAct agent from scratch with Gemini 2.5 and LangGraph*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [5] Daily Dose of DS. (n.d.). *Implementing ReAct Agentic Pattern From Scratch*. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [6] Marques, N., & Riveiro, M. (2024). *The Rise of AI Agents*. SCITEPRESS. https://www.scitepress.org/Papers/2026/144223/144223.pdf
- [7] IBM. (n.d.). *What is a ReAct agent?*. https://www.ibm.com/think/topics/react-agent
- [8] Prompting Guide. (n.d.). *ReAct (Reason+Act) Prompting*. https://www.promptingguide.ai/techniques/react