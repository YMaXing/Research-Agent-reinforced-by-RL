In our last lesson, we explored the theory behind LLM reasoning, focusing on frameworks like ReAct that enable agents to think, act, and observe. We saw how these patterns allow an LLM to break down complex problems and interact with external tools by grounding its reasoning in verifiable observations, which helps reduce hallucination and improves transparency [[17]](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/). But theory only takes you so far. To truly understand how these systems work, you have to build one.

This lesson is 100% hands-on. We are moving from the "what" to the "how" by implementing a minimal ReAct agent from scratch using only Python and the Gemini API. You will build the complete Thought → Action → Observation cycle: define a mock tool, generate thoughts, select actions with function calling, execute the tool, and process observations within a turn-based control loop.

This exercise provides a concrete mental model of how reasoning agents operate under the hood. By building the core mechanics yourself, you will gain the confidence to debug, customize, and extend agentic systems, a foundational skill for any AI Engineer. In this lesson, we will cover setting up the environment, defining a tool, and implementing the thought, action, and control loop phases, complete with tests to verify our agent's behavior.

## Setup and Environment

Our first step is to set up a clean Python environment to ensure the code runs smoothly and our outputs match the expected results. This project uses the `google-genai` package to interact with the Gemini API, along with Pydantic for data modeling. A proper setup is the foundation for any reproducible AI application.

1.  We start by loading our `GOOGLE_API_KEY` from an environment file. We use a simple utility function for this, which we will reuse throughout the course. This practice keeps sensitive keys out of our source code.
    
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    
    It outputs:
    
    ```text
    Trying to load environment variables from /path/to/your/project/.env
    Environment variables loaded successfully.
    ```
    
2.  Next, we import the necessary packages. This includes `google.genai` for the API client, `pydantic` for creating structured data models, and standard Python libraries like `enum` and `typing` for type hinting.
    
    ```python
    import json
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```
    
3.  We initialize the Gemini client, which will handle all our API requests. This object is our gateway to the LLM.
    
    ```python
    client = genai.Client()
    ```
    
    It outputs:
    
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```
    
4.  Finally, we define the model we will use. For this lesson, `gemini-2.5-flash` is a great choice because it is fast and cost-effective, perfect for the simple reasoning our agent will perform.
    
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
    

With the client and model configured, we can now define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

As we learned in Lesson 6, tools are functions that give an agent the ability to interact with the outside world. For this guide, we will implement a simple mock search tool instead of calling a real API. This approach has several benefits for learning: it keeps the focus on the ReAct mechanics, removes the need for external API keys, and gives us predictable responses for testing [[13]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

Our tool is a Python function named `search`. Its docstring is important because, as we will see later, the Gemini API uses it to understand what the tool does and how to call it [[9]](https://ai.google.dev/gemini-api/docs/function-calling). The function includes a few hardcoded responses for specific queries and a generic fallback for anything else. This design simulates how a real tool would return data or an error.

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

In a production system, you would replace this mock function with a real API call to a search engine or a domain-specific knowledge base [[27]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae). Because we have isolated the implementation, we can easily swap it out later without changing the agent's core logic. We also create a `TOOL_REGISTRY` to map the function's name to the callable function, which allows our control loop to execute the correct tool dynamically.

```python
TOOL_REGISTRY = {
    search.__name__: search,
}
```

Now that our agent has a tool, let's implement the first phase of the ReAct cycle: thought.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is the agent's internal monologue, where it reasons about the user's query and plans its next step [[1]](https://arxiv.org/pdf/2210.03629). We trigger this by sending a carefully constructed prompt to the LLM. This step is crucial for guiding the agent's decision-making process.

1.  First, we create a helper function to generate an XML description of the available tools. As we discussed in Lesson 3, using XML tags helps the model distinguish between different parts of the context [[15]](https://ai.google.dev/gemini-api/docs/prompting-strategies). This function takes our `TOOL_REGISTRY` and creates a simple `<tool>` block containing the function's name and docstring. This makes the tool's purpose clear to the LLM.
    
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
    
2.  We then define our main prompt template. It instructs the agent on its goal, provides the XML-formatted tool descriptions, and includes a placeholder for the conversation history. The prompt asks the model to state its next thought as a short paragraph, focusing on the next intended action and the reasoning behind it.
    
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
    
    Inspecting the full prompt reveals its structure. The `<tools>` block clearly lists the `search` tool and its description, while the `<conversation>` block will be populated with the ongoing dialogue history.
    
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
    
3.  Finally, we implement the `generate_thought` function. It takes the current conversation history, formats the prompt with the tool descriptions and history, calls the Gemini API, and returns the model's textual response. This response is the agent's "thought."
    
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
    

With a coherent thought generated, the agent must now decide whether to call a tool or conclude with a final answer.

## Action Phase: Function Calling and Parsing

The "Action" phase determines what the agent does next. Instead of manually including tool schemas in our prompt, we will leverage Gemini's native function calling capability. This is a more robust and cleaner approach, as we learned in Lesson 6. The API handles the low-level details of presenting tools to the model, allowing our prompt to focus on high-level strategy [[9]](https://ai.google.dev/gemini-api/docs/function-calling). This separation of concerns simplifies both the prompt and tool management.

1.  We define two prompt templates. The main one, `PROMPT_TEMPLATE_ACTION`, instructs the model to choose between a tool call and a final answer based on the conversation. The second, `PROMPT_TEMPLATE_ACTION_FORCED`, is a fallback used to force a conclusion, which prevents the agent from getting stuck in a loop if it cannot find an answer.
    
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
    
2.  We define two Pydantic models, `ToolCallRequest` and `FinalAnswer`, to represent the two possible outcomes of the action phase. This use of structured outputs, a concept from Lesson 4, makes the agent's decision explicit and easy to parse, creating a clear contract between the LLM and our code.
    
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```
    
3.  The `generate_action` function orchestrates this phase. It selects the appropriate prompt and calls the Gemini API. Crucially, it passes the Python tool functions directly to the `tools` parameter in the `GenerateContentConfig`. The Gemini client automatically inspects these functions, extracts their name, docstring, and parameters, and makes them available to the model. We also disable automatic execution (`"disable": True`) so our loop can handle it, giving us full control. The function then parses the response, checking if the model returned a `function_call` or plain text for a final answer.
    
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
    
    The `force_final` flag is a safety mechanism. In a ReAct loop, we need a way to terminate gracefully, for example, to avoid infinite loops or excessive costs. This flag lets us instruct the model to conclude with a final answer, ensuring a clean shutdown.

## Control Loop: Messages, Scratchpad, and Orchestration

Now we combine everything into the main ReAct control loop that orchestrates the Thought → Action → Observation cycle. This loop manages the conversation history, calls the thought and action phases, executes tools, and processes the resulting observations. This iterative process is analogous to human planning. For example, when packing for a trip, you identify what you need (thought), consult a weather forecast (action), and use that information to adjust your packing list (observation) [[3]](https://www.ibm.com/think/topics/react-agent).

Image 1: A flowchart illustrating the ReAct control loop, detailing the turn-based iteration of Thought, Action, and Observation.
```mermaid
graph TD
    A(["User Query"]) --> B["Thought<br/>(LLM Reasoning)"]
    B --> C["Action<br/>(LLM Decision)"]
    C --> D{"Is it a Tool Request?"}
    D -- "Yes" --> E["External Environment<br/>(Tool Execution)"]
    E --> F["Observation"]
    F --> B
    D -- "No" --> G(["Final Answer"])
```

1.  We start by defining data structures to manage the conversation. `MessageRole` is an `Enum` that categorizes each step (e.g., `USER`, `THOUGHT`, `TOOL_REQUEST`). The `Message` class is a Pydantic model that holds the content and role for each entry in our log. This structured approach is key to tracking the agent's state clearly.
    
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
    
2.  A `Scratchpad` class holds the list of `Message` objects. This acts as the agent's short-term memory for the current task. Its `append` method adds new messages and optionally pretty-prints them to the console, making it easy to trace the agent's execution and debug its behavior.
    
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
                # ... pretty printing logic from notebook ...
    
        def to_string(self) -> str:
            return "\n".join(str(m) for m in self.messages)
    ```
    
3.  The `react_agent_loop` function is the heart of our agent. It initializes the `Scratchpad` with the user's question and then iterates through the ReAct cycle for a maximum number of turns. In each turn, it generates a thought, then generates an action.
    
    If the action is a `FinalAnswer`, the loop terminates and returns the answer. If it is a `ToolCallRequest`, the loop finds the corresponding tool function in our `TOOL_REGISTRY` and executes it. The tool's output is captured as an "Observation" and appended to the scratchpad. The loop then continues to the next turn, where the new observation informs the next thought. If the loop reaches `max_turns`, it calls `generate_action` one last time with `force_final=True` to ensure a conclusion. This entire process, from tool execution to error handling, is managed within the loop, making the agent's reasoning transparent and resilient.
    
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
    
            # If it's a final answer, stop
            if isinstance(action_result, FinalAnswer):
                final_answer = action_result.text
                final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                scratchpad.append(final_message, verbose=verbose)
                return final_answer
    
            # If it's a tool request, execute it
            if isinstance(action_result, ToolCallRequest):
                action_name = action_result.tool_name
                action_params = action_result.arguments
    
                params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
                action_content = f"{action_name}({params_str})"
                action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
                scratchpad.append(action_message, verbose=verbose)
    
                # Run the action and get the observation
                observation_content = ""
                tool_function = tool_registry.get(action_name)
                if tool_function:
                    try:
                        observation_content = tool_function(**action_params)
                    except Exception as e:
                        observation_content = f"Error executing tool '{action_name}': {e}"
                else:
                    observation_content = f"Unknown tool '{action_name}'. Available tools: {list(tool_registry.keys())}"
    
                # Add the observation to the scratchpad
                observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
                scratchpad.append(observation_message, verbose=verbose)
    
            # Force a final answer if max turns are reached
            if turn == max_turns:
                forced_action = generate_action(scratchpad.to_string(), force_final=True)
                if isinstance(forced_action, FinalAnswer):
                    final_answer = forced_action.text
                else:
                    final_answer = "Unable to produce a final answer within the allotted turns."
                final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                scratchpad.append(final_message, verbose=verbose, is_forced_final_answer=True)
                return final_answer
    ```
    
    This loop provides a complete, albeit minimal, implementation of the ReAct pattern. It demonstrates how an agent can iteratively reason, act, and learn from observations to solve a problem. The verbose output from the scratchpad allows us to analyze how the agent reasons, how it uses tools, and how it updates its state, providing a clear window into its decision-making process. This basic implementation can be extended with more sophisticated tools, error handling, and complex reasoning patterns, which we will explore in future lessons.

## Tests and Traces: Success and Graceful Fallback

To validate our agent, we will run two tests. The first is a simple factual question to demonstrate a successful run, and the second is a query our mock tool cannot answer, demonstrating graceful fallback. By analyzing the traces, we can confirm the control loop, tool integration, and termination logic work as expected.

First, let's ask a question our mock tool can answer: `"What is the capital of France?"` We will set `max_turns=2` and `verbose=True` to see the step-by-step execution.

```python
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The trace shows the agent working perfectly. The expected output highlights the following steps:
-   **Thought (Turn 1/2):** The agent reasons that it needs to find a factual answer and should use the `search` tool.
-   **Tool request (Turn 1/2):** It correctly generates the call `search(query='capital of France')`.
-   **Observation (Turn 1/2):** It receives the mock response: "Paris is the capital of France and is known for the Eiffel Tower."
-   **Thought (Turn 2/2):** After observing the result, the agent understands that it now has the information needed to answer the user's query.
-   **Final answer (Turn 2/2):** It concludes with the correct answer: "Paris is the capital of France."

This trace confirms that the agent can correctly identify the need for a tool, execute it, process the observation, and deliver a final answer, all within the specified turn limit.

Next, we test the fallback behavior with a query our mock tool does not have a predefined response for: `"What is the capital of Italy?"`. This tests the agent's resilience to tool failures.

```python
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The trace for this query demonstrates the agent's ability to handle failure and adapt its strategy:
-   **Thought (Turn 1/2) & Tool request (Turn 1/2):** The agent first attempts to search for "capital of Italy."
-   **Observation (Turn 1/2):** The tool returns the fallback message: "Information about 'capital of Italy' was not found."
-   **Thought (Turn 2/2):** Recognizing the first attempt failed, the agent formulates a new, broader strategy. It decides to search for just "Italy" to see if it can find related information.
-   **Tool request (Turn 2/2):** It calls `search(query='Italy')`.
-   **Observation (Turn 2/2):** This also fails, returning "Information about 'Italy' was not found."
-   **Final answer (Forced):** Having reached the maximum number of turns without success, the agent is forced to conclude. It gracefully admits defeat: "I'm sorry, but I couldn't find information about the capital of Italy."

These tests confirm our end-to-end loop is working. The agent can successfully use tools when they provide useful information and can adapt its strategy and terminate cleanly when they do not.

## Conclusion

In this lesson, we built a complete, minimal ReAct agent from scratch. We implemented every part of the Thought-Action-Observation cycle, from defining a mock tool and generating thoughts to executing actions with function calling and orchestrating the flow with a control loop. This hands-on exercise demystifies what happens inside an agentic system and provides a solid foundation for building more complex agents.

Understanding these core mechanics is essential. While frameworks can accelerate development, knowing how to build the underlying components gives you the power to debug, customize, and innovate with confidence. The patterns we covered today—structured messages, a scratchpad for memory, and a turn-based control loop—are fundamental building blocks you will use repeatedly.

In our upcoming lessons, we will build on this foundation. We will explore more advanced topics like agent memory and RAG, which will allow our agents to remember information across conversations and access vast knowledge bases. This will also prepare you for more advanced orchestration patterns like multi-agent systems, self-reflection, and tree-based search that are at the frontier of AI engineering [[44]](https://arxiv.org/html/2602.10479v1).

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)
- [2] Stryker, C. (n.d.). *AI agent planning*. IBM. [https://www.ibm.com/think/topics/ai-agent-planning](https://www.ibm.com/think/topics/ai-agent-planning)
- [3] Bergmann, D. (n.d.). *ReAct Agent*. IBM. [https://www.ibm.com/think/topics/react-agent](https://www.ibm.com/think/topics/react-agent)
- [4] Anthropic. (2024). *Building effective agents*. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [5] Google. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/langgraph-example](https://ai.google.dev/gemini-api/docs/langgraph-example)
- [6] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review*. arXiv. [https://arxiv.org/pdf/2504.19678](https://arxiv.org/pdf/2504.19678)
- [7] Shankar, A. (2024). *Building ReAct Agents from Scratch using Gemini*. Medium. [https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [8] Downie, A., & Finio, M. (n.d.). *AI Agent Orchestration*. IBM. [https://www.ibm.com/think/topics/ai-agent-orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [9] Google. (n.d.). *Gemini Function Calling Documentation*. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [10] Iusztin, P. (2025). *Building Production ReAct Agents From Scratch Is Simple*. Decoding AI. [https://www.decodingai.com/p/building-production-react-agents](https://www.decodingai.com/p/building-production-react-agents)
- [11] Neradot. (2024). *Building a Python React Agent Class: A Step-by-Step Guide*. [https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide](https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide)
- [12] Lu, Y., Liu, S., & Dong, L. (2025). *OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs*. arXiv. [https://arxiv.org/html/2510.24663v1](https://arxiv.org/html/2510.24663v1)
- [13] Shankar, A. (2024). *Building ReAct Agents from Scratch using Gemini*. Medium. [https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [14] Schmid, P. (2025). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. [https://www.philschmid.de/langgraph-gemini-2-5-react-agent](https://www.philschmid.de/langgraph-gemini-2-5-react-agent)
- [15] Google. (n.d.). *Prompt design strategies*. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [16] Iusztin, P. (2025). *Building ReAct Agents From Scratch: A Simple Guide*. [https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb)
- [17] Daily Dose of DS. (2024). *AI Agents Crash Course - Part 10: ReAct Framework with Implementation*. [https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/)
- [18] Brownlee, J. (2024). *Building ReAct Agents with LangGraph: A Beginner’s Guide*. Machine Learning Mastery. [https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/](https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/)
- [19] LateNode. (2024). *LangChain ReAct Agent: Complete Implementation Guide with Working Examples (2025)*. [https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025)
- [20] GenMind. (n.d.). *Building ReAct Agents with Microsoft Agent Framework: From Theory to Production*. [https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/](https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/)
- [21] Towards AI. (n.d.). *Beyond the Prompt: Engineering the Thought-Action-Observation Loop*. [https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2](https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2)
- [22] Stackademic. (n.d.). *AI Agents IV: AI Agents through the Thought-Action-Observation (TAO) Cycle*. [https://blog.stackademic.com/ai-agents-iv-ai-agents-through-the-thought-action-observation-tao-cycle-3dfe2eb76629](https://blog.stackademic.com/ai-agents-iv-ai-agents-through-the-thought-action-observation-tao-cycle-3dfe2eb76629)
- [23] Hugging Face. (n.d.). *Agent steps and structure*. Hugging Face Agents Course. [https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure)
- [24] DataCamp. (n.d.). *Hugging Face Agents Course, Chapter 2*. [https://projector-video-pdf-converter.datacamp.com/42942/chapter2.pdf](https://projector-video-pdf-converter.datacamp.com/42942/chapter2.pdf)
- [25] Google. (n.d.). *Gemini API: Prompting Strategies*. [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [26] Google. (n.d.). *Gemini API: Thinking*. [https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking)
- [27] Shankar, A. (2024). *Building ReAct Agents from Scratch using Gemini*. Medium. [https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)
- [28] OpenAI Community. (n.d.). *Converting a ReAct prompt to use function calling*. [https://community.openai.com/t/converting-a-react-prompt-to-use-function-calling/264914](https://community.openai.com/t/converting-a-react-prompt-to-use-function-calling/264914)
- [29] OpenAI Community. (n.d.). *Using Gemini with OpenAI Agents SDK*. [https://community.openai.com/t/using-gemini-with-openai-agents-sdk/1307262](https://community.openai.com/t/using-gemini-with-openai-agents-sdk/1307262)
- [30] FreeCodeCamp. (n.d.). *Build an AI Coding Agent with Python and Gemini*. [https://www.freecodecamp.org/news/build-an-ai-coding-agent-with-python-and-gemini/](https://www.freecodecamp.org/news/build-an-ai-coding-agent-with-python-and-gemini/)
- [31] Upadhyay, A. (2025). *Building a real-time web-searching AI agent with LangChain and Google Gemini*. [https://atalupadhyay.wordpress.com/2025/11/25/building-a-real-time-web-searching-ai-agent-with-langchain-and-google-gemini/](https://atalupadhyay.wordpress.com/2025/11/25/building-a-real-time-web-searching-ai-agent-with-langchain-and-google-gemini/)
- [32] Google Developers Blog. (n.d.). *Real-world agent examples with Gemini 3*. [https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/](https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/)
- [33] IBM. (n.d.). *AI Agent Orchestration*. [https://www.ibm.com/think/topics/ai-agent-orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [34] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)
- [35] Google. (n.d.). *Prompt design strategies*. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [36] Google. (n.d.). *Gemini Function Calling Documentation*. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [37] IBM. (n.d.). *AI Agent Planning*. [https://www.ibm.com/think/topics/ai-agent-planning](https://www.ibm.com/think/topics/ai-agent-planning)
- [38] Anthropic. (2024). *Building effective agents*. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [39] Google. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/langgraph-example](https://ai.google.dev/gemini-api/docs/langgraph-example)
- [40] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review*. arXiv. [https://arxiv.org/pdf/2504.19678](https://arxiv.org/pdf/2504.19678)
- [41] IBM. (n.d.). *ReAct Agent*. [https://www.ibm.com/think/topics/react-agent](https://www.ibm.com/think/topics/react-agent)
- [42] Iusztin, P. (2025). *Building Production ReAct Agents From Scratch Is Simple*. Decoding AI. [https://www.decodingai.com/p/building-production-react-agents](https://www.decodingai.com/p/building-production-react-agents)
- [43] Daily Dose of DS. (2024). *AI Agents Crash Course - Part 10: ReAct Framework with Implementation*. [https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/)
- [44] *Agent orchestration trends*. arXiv. [https://arxiv.org/html/2602.10479v1](https://arxiv.org/html/2602.10479v1)