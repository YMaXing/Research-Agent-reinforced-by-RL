# Lesson 8: Building a ReAct Agent From Scratch

In our last lesson, we explored the theory behind agentic planning and reasoning, focusing on frameworks like ReAct. We learned how agents can break down complex problems by interleaving thought, action, and observation. But theory only takes you so far. The real understanding comes from building. Many AI frameworks abstract away the core mechanics, making it difficult to grasp what is happening under the hood. This can be frustrating when things go wrong and you need to debug a system you did not build.

This lesson is 100% practical. We will build a minimal ReAct agent from scratch using only Python and the Gemini API, following the code from our course notebook. By implementing the full Thought → Action → Observation cycle yourself, you will gain a concrete mental model of how these systems work. This hands-on experience is what gives you the confidence to build, debug, and extend agents for production.

We will walk through the entire process, step-by-step:
- Setting up the Python environment and Gemini client.
- Defining a mock tool to give our agent a capability.
- Implementing the "Thought" phase to generate a plan.
- Building the "Action" phase using function calling.
- Orchestrating everything with a turn-based control loop.
- Testing our agent to see it succeed and handle failure gracefully.

## Setup and Environment

Before we start building, let's ensure our environment is set up correctly. A clean setup ensures that the code runs smoothly and the outputs match what we expect, making it easier to follow along and debug. This section mirrors the initial cells of the lesson's notebook.

1.  First, we load our `GOOGLE_API_KEY` from the `.env` file. Our utility function handles this, making sure the key is available as an environment variable for the Gemini client.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Trying to load environment variables from `/.../.env`
    Environment variables loaded successfully.
    ```

2.  Next, we import the necessary packages. We will use `google-genai` for interacting with the Gemini API, `pydantic` for data modeling, and some standard Python libraries like `enum` and `typing`. Our custom `pretty_print` utility will help visualize the agent's traces.
    ```python
    from enum import Enum
    from pydantic import BaseModel, Field
    from typing import List
    
    from google import genai
    from google.genai import types
    
    from lessons.utils import pretty_print
    ```

3.  With the API key loaded, we can initialize the Gemini client.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is fast and cost-effective, making it ideal for the simple reasoning tasks in our agent.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With our client and model ready, we can now define an external tool for our agent to use.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to interact with the world through tools. For this lesson, we will create a simple mock `search` tool instead of integrating with a real API like Google Search. This approach has several educational benefits. It keeps our focus on the ReAct mechanics, removes the need for external API keys, and gives us predictable responses, which is perfect for testing and learning.

In a production system, you could easily swap this mock function with a real API call to Google Search or a domain-specific knowledge base, as long as you preserve the same function signature and update the docstring.

1.  Let's implement our mock `search` tool. The function takes a string `query` as input and returns a string as output. The docstring is important, as it describes the tool's purpose, which the LLM will use to decide when to call it.
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
    Our mock tool has predefined answers for queries about the capital of France and the ReAct framework. For any other query, it returns a "not found" message. This controlled behavior will allow us to test both success and fallback scenarios later.

2.  We also create a `TOOL_REGISTRY`, which is a dictionary that maps the tool's name to its function. This allows our agent to plan using symbolic tool names (like `"search"`) while our code can safely look up and execute the corresponding Python function.
    ```python
    TOOL_REGISTRY = {
        search.__name__: search,
    }
    ```
With a tool in place, the agent now needs a way to "think" about when and how to use it. This brings us to the first step of the ReAct cycle: the Thought phase.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is where the agent reasons about the user's goal and plans its next step. This is not just an internal state; it is an explicit piece of text generated by the LLM that we can inspect. To guide this process, we will construct a prompt template that tells the model how to think.

1.  First, we need a way to describe our available tools to the LLM. We will create a helper function that converts our `TOOL_REGISTRY` into a simple XML format. This function reads the docstring from each tool and wraps it in `<tool>` and `<description>` tags. Using XML is a common technique that helps the model clearly distinguish instructions from other context [[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies).
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

2.  Let's inspect the final prompt template. It instructs the model on its role, shows the available tools in the XML format we just created, and provides a placeholder for the conversation history.
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

3.  Now, we implement the `generate_thought` function. This function takes the current `conversation` history, inserts it into our prompt template, calls the Gemini model, and returns the generated thought as plain text.
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
A thought is a plan. To execute that plan, the agent must move to the "Action" phase, where it decides whether to call a tool or conclude with a final answer.

## Action Phase: Function Calling and Parsing

The "Action" phase translates the agent's thought into a concrete action. This could be a call to an external tool or a final answer to the user. We will use Gemini's native function calling feature to handle this, as it is more reliable than asking the model to generate a JSON string and parsing it manually.

The prompt for this phase is focused on high-level decision-making. We do not need to include tool descriptions in the prompt text itself. Instead, we pass the Python tool functions directly to the Gemini API via its configuration. The API automatically parses the function signatures and docstrings, making them available to the model. This keeps our prompt clean and separates the strategic guidance from the technical tool specifications [[31]](https://ai.google.dev/gemini-api/docs/function-calling).

1.  We define two prompt templates. The first is for a standard action step, and the second is a special prompt to force a final answer. We will use this second prompt to ensure our agent can terminate gracefully if it reaches an iteration limit.
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

2.  We define two Pydantic models to represent the possible outcomes of the action phase: a `ToolCallRequest` or a `FinalAnswer`. This structured approach makes the output predictable and easy to work with.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool with its name and arguments."""
        tool_name: str = Field(description="The name of the tool to call.")
        arguments: dict = Field(description="The arguments to pass to the tool.")
    
    
    class FinalAnswer(BaseModel):
        """A final answer to present to the user when no further action is needed."""
        text: str = Field(description="The final answer text to present to the user.")
    ```

3.  Now we implement the `generate_action` function. This is the core of the action phase.
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
    If `force_final` is true, it uses the dedicated prompt and returns a `FinalAnswer`. Otherwise, it passes the available tools to the `generate_content` call. We set `automatic_function_calling={"disable": True}` because we want to parse the model's response and execute the tool ourselves, giving us full control. The function then checks the response: if it contains a `function_call`, it extracts the name and arguments and returns a `ToolCallRequest`. If not, it assumes the model has provided a final answer and returns a `FinalAnswer`.

Image 1: A flowchart illustrating the structured interaction between an application, the Gemini model, and external functions during the function calling process.
```mermaid
flowchart LR
  subgraph "Application"
    A_init["Initiates Process"]
    A_exec["Executes Function"]
    A_send_res["Sends Result to Model"]
    A_final_res["Receives Final Response"]
  end

  subgraph "Gemini Model"
    G_decide{"Decides: Call Function<br/>or Respond Directly?"}
    G_gen_res["Generates Final Response"]
  end

  subgraph "External Functions"
    EF_code["Function Code<br/>(Executed by App)"]
  end

  %% Initial setup
  A_init -- "1. Defines function declarations" --> G_decide
  A_init -- "2. Sends user prompt<br/>& declarations" --> G_decide

  %% Function Calling Loop
  G_decide -- "3a. Suggests function call<br/>(JSON: name, args, ID)" --> A_exec
  A_exec -- "4. Executes function code" --> EF_code
  EF_code -- "5. Returns result" --> A_send_res
  A_send_res -- "6. Sends result<br/>(with ID)" --> G_decide

  %% Direct Response Path
  G_decide -- "3b. Responds directly<br/>(no function call)" --> G_gen_res

  %% Final Response
  G_gen_res -- "7. Delivers final response" --> A_final_res
```
We now have the "Thought" and "Action" components. The final piece is the control loop that orchestrates them in the full ReAct cycle.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the engine of our ReAct agent. It orchestrates the Thought → Action → Observation cycle, manages the conversation history, executes tools, and processes their outputs. We will build this loop by treating the entire interaction as a sequence of structured messages stored in a "scratchpad."

1.  First, we define the structure of our messages. A `MessageRole` enum categorizes each part of the interaction (e.g., `USER`, `THOUGHT`, `TOOL_REQUEST`). The `Message` Pydantic model holds the content and role for each step. This structured approach is key to tracking the agent's state clearly.
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

2.  We will use a helper function to pretty-print each message. This will make the agent's traces easy to read and debug by color-coding messages based on their role.
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

3.  The `Scratchpad` class will manage our list of `Message` objects. It provides an `append` method to add new messages and optionally print them. Its `to_string` method serializes the entire history into a single string, which we will feed back to the LLM in each turn.
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

4.  Finally, we implement the `react_agent_loop` function. This is where everything comes together.
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
    The loop starts with the user's question. In each turn, it generates a thought, then an action. If the action is a `FinalAnswer`, the loop terminates. If it is a `ToolCallRequest`, the loop looks up the tool in the `tool_registry`, executes it, and appends the result as an `OBSERVATION` message to the scratchpad. This observation becomes part of the context for the next turn. If the loop reaches `max_turns`, it calls `generate_action` one last time with `force_final=True` to ensure a clean exit.

Image 2: A flowchart comparing the theoretical ReAct agent design with its LangGraph implementation, highlighting the Thought-Action-Observation loop.
```mermaid
flowchart LR
  %% Theoretical ReAct Agent Design
  subgraph "Theoretical ReAct Agent Design"
    Query_T["Query"]
    LLM_Thought_T["LLM<br/>(Thought)"]
    Thought_Interpret_T["Thought<br/>(Interpret Context)"]
    Done_Decision_T{"Done?"}
    LLM_Action_T["LLM<br/>(Action)"]
    Action_Tool_T["Action<br/>(Through Tool)"]
    External_Env_T["External Environment"]
    Observation_Output_T["Observation<br/>(As Tool Output)"]
    Final_Answer_T["Final Answer"]

    Query_T --> LLM_Thought_T
    LLM_Thought_T --> Thought_Interpret_T
    Thought_Interpret_T --> Done_Decision_T
    Done_Decision_T -- "No" --> LLM_Action_T
    LLM_Action_T --> Action_Tool_T
    Action_Tool_T --> External_Env_T
    External_Env_T --> Observation_Output_T
    Observation_Output_T -- "feeds back" --> LLM_Thought_T
    Done_Decision_T -- "Yes" --> Final_Answer_T
  end

  %% LangGraph's ReAct Agent Implementation
  subgraph "LangGraph's ReAct Agent Implementation"
    Start_LG["_start_"]
    Query_LG["Query"]
    Model_LG["Model<br/>(LLM)"]
    Thought_LG["Thought"]
    Action_LG["Action"]
    Tools_LG["Tools"]
    Tool_Output_LG["Tool Output"]
    Final_Answer_LG["Final Answer"]
    End_LG["_end_"]

    Start_LG --> Query_LG
    Query_LG --> Model_LG
    Model_LG -- "generates" --> Thought_LG
    Model_LG -- "decides" --> Action_LG
    Action_LG --> Tools_LG
    Tools_LG --> Tool_Output_LG
    Tool_Output_LG -- "feeds back" --> Model_LG
    Model_LG -- "Retry" --> Model_LG
    Model_LG -- "produces" --> Final_Answer_LG
    Final_Answer_LG --> End_LG
  end

  %% Visual grouping for decision nodes and start/end nodes
  classDef decision fill:#fff,stroke:#333,stroke-width:2px,font-weight:bold
  class Done_Decision_T decision
  classDef start_end fill:#eee,stroke:#333,stroke-width:2px,font-weight:bold
  class Start_LG,End_LG start_end
```
With the complete loop implemented, let's test it to see how it performs on both successful and failed queries.

## Tests and Traces: Success and Graceful Fallback

Now it is time to validate our agent. We will run two tests: one with a question our mock tool can answer, and one with a question it cannot. By analyzing the traces, we can verify that the full ReAct cycle works as designed, including tool execution, observation handling, and forced termination.

### Success Case

First, let's ask a simple factual question that our `search` tool is designed to answer. We will set `verbose=True` to see the full trace.

1.  We run the loop with the question "What is the capital of France?" and a limit of two turns.
    ```python
    question = "What is the capital of France?"
    final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
    ```
    It outputs:
    ```text
    User (Turn 1/2):
    What is the capital of France?
    
    Thought (Turn 1/2):
    I need to find the capital of France. I can use the search tool for this.
    
    Tool request (Turn 1/2):
    search(query='capital of France')
    
    Observation (Turn 1/2):
    Paris is the capital of France and is known for the Eiffel Tower.
    
    Thought (Turn 2/2):
    I have found the answer. The capital of France is Paris. I will now provide the final answer.
    
    Final answer (Turn 2/2):
    Paris is the capital of France.
    ```
    The trace shows the perfect ReAct cycle. The agent correctly identifies the need for a search, calls the tool, processes the observation, and concludes with the final answer, all within the turn limit.

### Graceful Fallback Case

Next, let's test the agent's ability to handle a query that our mock tool does not have a predefined answer for. This will test its fallback behavior and the forced termination logic.

1.  We ask, "What is the capital of Italy?" and keep the same two-turn limit.
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
    The initial search for "capital of Italy" failed. I will try a broader search for just "Italy" to see if I can find the capital that way.
    
    Tool request (Turn 2/2):
    search(query='Italy')
    
    Observation (Turn 2/2):
    Information about 'Italy' was not found.
    
    Final answer (Forced):
    I'm sorry, but I couldn't find information about the capital of Italy using the available tools.
    ```
    This trace demonstrates the agent's resilience. After the first search fails, it observes the "not found" message and adapts its strategy in the second turn by trying a broader query. When that also fails, it hits the `max_turns` limit. The control loop then correctly triggers the forced final answer, and the agent provides a helpful response admitting it could not find the information.

These tests confirm that our from-scratch ReAct implementation is working correctly, providing a solid foundation for building more advanced agents.

## Conclusion

We have successfully built a minimal, yet fully functional, ReAct agent from scratch. By implementing each component—the tools, the thought and action phases, and the orchestrating control loop—we have demystified what happens inside agentic frameworks. This hands-on process provides a concrete mental model that is essential for any AI engineer. You now understand how an agent reasons about a task, decides to use a tool, processes the outcome, and iterates until it reaches a conclusion.

This foundation is the key to building more complex and robust AI systems. In our upcoming lessons, we will build on this model. We will explore how to add persistent memory so agents can learn from past interactions in Lesson 9, and we will dive deep into Retrieval-Augmented Generation (RAG) to connect them to vast knowledge bases in Lesson 10. The principles you learned here will apply directly to those more advanced topics.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. https://arxiv.org/pdf/2210.03629
- [2] *Prompt design strategies*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [3] *Gemini Function Calling Documentation*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling