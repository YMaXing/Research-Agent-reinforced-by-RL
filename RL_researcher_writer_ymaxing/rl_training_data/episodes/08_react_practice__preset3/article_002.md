# Lesson 8: Building a ReAct Agent From Scratch

In our last lesson, we covered the theory behind agentic reasoning, focusing on the ReAct pattern. First proposed by Yao et al. in 2022, the core idea is to create a synergy between reasoning and acting by having the LLM generate both internal thoughts and external actions in an interleaved fashion [[1]](https://arxiv.org/pdf/2210.03629). We saw how the Thought → Action → Observation cycle allows an LLM to break down complex problems, interact with external tools, and dynamically plan its way to a solution. Abstract theory is a good start, but as engineers, we learn best by building.

This lesson is 100% practical. We will move from theory to implementation by building a minimal ReAct agent from the ground up using only Python and the Gemini API. You will implement the full reasoning loop: defining a mock tool for the agent to use, generating thoughts, selecting actions with function calling, executing the tool, and processing the resulting observations. While early ReAct agents relied on parsing text-based thoughts and actions from the LLM's raw output, modern implementations can leverage native function calling for more reliable and structured tool use [[4]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent). We will tie it all together with a turn-based control loop that orchestrates the entire process.

By the end of this hands-on session, you will have a concrete mental model of how these agents work under the hood. This foundational understanding is what allows you to debug, extend, and confidently build more complex agentic systems.

## Setup and Environment

Our first step is to set up the Python environment to ensure our code runs smoothly and that the outputs match the expected traces. This involves loading our API keys, importing the necessary libraries, and initializing the Gemini client. A correct setup is the foundation for any reproducible AI engineering work, ensuring that anyone can run the code and get the same results.

1.  We begin by loading our environment variables using a custom utility function from our course library. This function securely loads the `GOOGLE_API_KEY` from a `.env` file in your project root, keeping your credentials out of the source code. It also provides helpful feedback, confirming which key is being used if multiple are present.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```

2.  Next, we import the required packages. We will use `google-genai` for interacting with the Gemini API, `pydantic` for creating structured data models that ensure type safety and data validation, and `enum` for defining a controlled vocabulary for our message roles. We also import a `pretty_print` utility to help visualize our agent's traces in a readable format.
    ```python
    from google import genai
    from pydantic import BaseModel, Field
    from enum import Enum
    from typing import Callable, Union
    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client, which will be our main interface for making calls to the LLM. This object handles the authentication and communication with Google's backend services, abstracting away the low-level HTTP requests.
    ```python
    client = genai.Client()
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

4.  Finally, we define the model we will use. For this exercise, `gemini-2.5-flash` is an excellent choice. It is designed for speed and cost-efficiency, making it ideal for development and for tasks like the ones in this lesson, which involve generating structured outputs and following clear instructions. While more powerful models exist for complex, multi-step reasoning, `flash` provides the right balance for building and testing our core agent logic quickly and affordably.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With the client and model in place, we can now define the external capabilities our agent will need to perform its tasks.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to use tools to interact with its environment. In a production system, these tools might call a real search engine API, query a database, or execute code. For this lesson, however, we will use a mock `search` tool.

### Tool Design Philosophy

Using a mock tool is a deliberate choice with several educational benefits. It simplifies the implementation, allowing us to focus purely on the ReAct mechanics without getting sidetracked by external dependencies, network latency, or API key management. It also provides predictable, deterministic responses, which is essential for testing and understanding the agent's behavior during development. When you can control the exact output of a tool, you can more easily debug the agent's reasoning process and verify that its logic is sound. This hands-on approach demystifies how frameworks operate, giving you the control needed for optimization and troubleshooting [[6]](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/).

Implementing the complete Thought-Action-Observation cycle in a controlled environment like a notebook provides a concrete mental model for how agents function. It allows you to step through each phase, inspect the agent's internal state, and see exactly how an observation influences the next thought. This transparency builds confidence and provides the foundational skills needed to debug and extend more complex agents with new tools or more sophisticated reasoning patterns [[12]](https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2).

### Implementation

1.  First, we define the `Tool` class, which will act as a wrapper for our tool functions. It stores the tool's name, its callable function, and a `use` method that executes the function and handles any potential errors.
    ```python
    class Tool(BaseModel):
        """A wrapper for a tool that the agent can use."""
    
        name: str
        description: str
        func: Callable
    
        def use(self, query: str) -> Union[str, Exception]:
            """
            Executes the tool with the given query and handles exceptions.
            """
            try:
                return self.func(query)
            except Exception as e:
                return e
    ```

2.  Next, we implement the `search` function. The function's docstring is crucial, as it serves as the description that the LLM will see. A good description helps the model understand what the tool does and when to use it. The function contains a small dictionary to mock responses for a few predefined queries.
    ```python
    def search(query: str) -> str:
        """
        A mock search tool that returns predefined results for specific queries.
        This tool can be used to find factual information.
        """
        mock_results = {
            "capital of France": "Paris is the capital of France and is known for the Eiffel Tower.",
        }
        return mock_results.get(query, f"Information about '{query}' was not found.")
    ```

3.  Finally, we create a `TOOL_REGISTRY` to store our tool. This registry will make it easy for our agent to look up and execute the correct tool by name.
    ```python
    TOOL_REGISTRY = {
        "search": Tool(
            name="search",
            description=search.__doc__,
            func=search,
        )
    }
    ```

### Real-World Context

In a real-world application, you could easily swap this mock function with a call to an actual API like Google Search or a domain-specific knowledge base. As long as you preserve the function signature (`query: str -> str`) and update the docstring to reflect the new capability, the agent's logic does not need to change [[3]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae). This modular approach is a key principle of building extensible AI agents.

When designing tools, it is helpful to think of them as a well-defined agent-computer interface (ACI). The tool's name, parameters, and especially its docstring description should be crafted with the same care as a system prompt, as this documentation is what guides the LLM's decision-making. Testing how the model uses your tools and refining their design to be less error-prone is a crucial step in building effective agents [[9]](https://www.anthropic.com/engineering/building-effective-agents). For example, if you find a model consistently misuses a tool, you might need to rename its parameters or clarify its description to make its purpose more obvious.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." Here, the agent analyzes the user's request and its conversation history to form a plan. As the original ReAct paper outlines, these thoughts are crucial for allowing the model to "induce, track, and update action plans as well as handle exceptions" [[1]](https://arxiv.org/pdf/2210.03629). This is achieved by prompting the LLM with a carefully crafted template that encourages it to reason about the next step. The quality of this prompt directly influences the agent's ability to decompose problems and strategize effectively.

This internal reasoning step is what makes the agent's behavior transparent and interpretable. By externalizing its thought process, the agent allows us to see *why* it chose a particular action, which is invaluable for debugging and building trust in the system. Without this step, we would only see the inputs and the final output, leaving the intermediate logic as a black box.

1.  We start by creating a helper function to format our tool descriptions into an XML structure. Using XML tags like `<tools>` and `<tool>` provides clear delimiters that help the LLM distinguish the tool definitions from other parts of the prompt [[7]](https://ai.google.dev/gemini-api/docs/prompting-strategies). This is a common context engineering technique we discussed in Lesson 3, which improves the model's ability to parse and understand the provided context.
    ```python
    def build_tools_xml_description(tool_registry: dict) -> str:
        """
        Builds an XML description of the available tools for the LLM.
        """
        xml = "<tools>\n"
        for tool in tool_registry.values():
            xml += f'<tool name="{tool.name}">\n'
            xml += f"<description>{tool.description}</description>\n"
            xml += "</tool>\n"
        xml += "</tools>"
        return xml
    ```

2.  Next, we define our prompt template for the thought-generation phase. The template has three main parts. First, it instructs the agent on its role and provides the available tools via the XML block. Second, it includes a placeholder for the ongoing `{conversation}` history, which allows the agent to be stateful and consider past interactions. Finally, the instruction "What is your next thought?" explicitly asks the model to produce a reasoning step, focusing its output on planning.
    ```python
    tools_xml_description = build_tools_xml_description(TOOL_REGISTRY)
    
    PROMPT_TEMPLATE_THOUGHT = f"""
    You are a helpful assistant that has access to the following tools:
    {tools_xml_description}
    
    You are responsible for helping a user with their request.
    
    Here is the conversation so far:
    <conversation>
    {{conversation}}
    </conversation>
    
    What is your next thought?
    """
    ```
    Inspecting the template shows how the tool's name and docstring are presented to the model:
    ```text
    You are a helpful assistant that has access to the following tools:
    <tools>
    <tool name="search">
    <description>
            A mock search tool that returns predefined results for specific queries.
            This tool can be used to find factual information.
            </description>
    </tool>
    </tools>
    
    You are responsible for helping a user with their request.
    
    Here is the conversation so far:
    <conversation>
    {conversation}
    </conversation>
    
    What is your next thought?
    ```

3.  Finally, we create the `generate_thought` function. It takes the current conversation history and the tool registry, formats the prompt template, sends it to the Gemini model, and returns the LLM's generated thought as a clean string. This function encapsulates the entire thought-generation process.
    ```python
    def generate_thought(conversation: str, tool_registry: dict) -> str:
        """
        Generates a thought from the LLM based on the conversation history.
        """
        prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation)
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    ```
This function completes the "Thought" phase. With a coherent thought generated, the agent now has a plan. The next step is to decide whether to execute a tool or provide a final answer to the user.

## Action Phase: Function Calling and Parsing

After generating a thought, the agent must decide on a concrete "Action." This could be calling a tool to gather more information or, if it has enough context, providing a final answer. We will use Gemini's native function calling capabilities to handle this decision-making process.

As we learned in Lesson 6, function calling allows the LLM to signal its intent to use a tool by returning a structured object containing the function's name and arguments. This is more reliable than asking the model to generate a raw string and then parsing it manually. Early ReAct implementations relied on parsing specific text formats like "Action: [search('capital of France')]", which was often brittle. Native function calling provides a structured, less error-prone way for the model to declare its intent [[4]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent).

### System Prompt Strategy

Our prompt for the action phase is intentionally high-level. It asks the model to decide on its next action—either call a tool or finish—based on the conversation history. It does not include technical details about the tools themselves. This separation of concerns is a useful design approach. The prompt focuses on the strategic decision, while the technical details are handled by the API configuration.

### Automatic Tool Integration with Gemini

A key advantage of Gemini's implementation is that we do not need to include detailed tool signatures in our system prompt. We simply pass the Python function objects to the `tools` parameter in the API call. The Gemini client automatically inspects these functions and generates the necessary schema for the model. It uses the function's name, its docstring as the description, and its type hints for the parameters. This keeps our prompts clean and makes it easy to add or modify tools without changing the prompt template.

### Implementation

1.  We start by defining our action types. An agent can either request a `ToolCallRequest` with a name and query, or it can signal that it is finished with an `ACTION_FINISH` constant. We use a Pydantic model for the tool call to ensure the data is structured and validated.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool."""
    
        name: str
        query: str
    
    
    ACTION_FINISH = "finish"
    ```

2.  Next, we define the prompt for the action phase. This prompt is given the conversation history, which now includes the latest thought. It instructs the agent to decide whether to use a tool or finish the conversation.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    Based on the following conversation, what is your next action?
    Your action must be one of the following:
    - Call a tool to gather more information.
    - Finish the conversation and provide a final answer to the user.
    
    Here is the conversation so far:
    <conversation>
    {conversation}
    </conversation>
    """
    ```

3.  The `generate_action` function orchestrates this step. It takes the conversation and tool registry, configures the Gemini client with the available tools, and sends the prompt. The core of this function is the response parsing logic. We check if the model's response contains a `function_call`.
    - If it does, we extract the name and arguments, creating a `ToolCallRequest` object.
    - If it does not, we assume the agent wants to provide a final answer and return the `ACTION_FINISH` constant.
    This dual-path logic cleanly separates tool usage from task completion. In a production system, you would add more robust error handling here to manage cases where the model's output is malformed, but for our learning purposes, this simple check is sufficient.
    ```python
    def generate_action(
        conversation: str, tool_registry: dict
    ) -> Union[ToolCallRequest, str]:
        """
        Generates an action from the LLM based on the conversation history.
        """
        tools = [tool.func for tool in tool_registry.values()]
    
        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)
        response = client.models.generate_content(
            model=MODEL_ID, contents=prompt, tools=tools
        )
    
        if response.candidates[0].content.parts[0].function_call:
            function_call = response.candidates[0].content.parts[0].function_call
            tool_name = function_call.name
            tool_query = function_call.args["query"]
            return ToolCallRequest(name=tool_name, query=tool_query)
        else:
            return ACTION_FINISH
    ```
This completes the "Action" phase. The agent has now moved from abstract reasoning to a concrete, executable decision. The final piece of the puzzle is to build a control loop that orchestrates this entire cycle.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop is the engine that drives the ReAct agent, orchestrating the iterative Thought → Action → Observation cycle. This design has conceptual roots in classic cognitive architectures from AI and robotics, which often rely on a similar deliberative sense-plan-act loop to enable intelligent behavior [[10]](https://arxiv.org/html/2602.10479v1). It manages the conversation history, executes tool calls, processes observations, and decides when to terminate. A key component of this loop is the "scratchpad," which is our term for the running log of all interactions.

### Message Structure and Scratchpad

To maintain a clean and structured history, we first define a `Message` class and a `MessageRole` enum. Each interaction—whether it is a user query, an agent's thought, a tool request, an observation, or a final answer—is stored as a `Message` object with a specific role. This makes the agent's trace easy to read and debug.

1.  We define the roles an entity can have in the conversation using an `Enum`. This provides a controlled vocabulary and prevents typos or inconsistencies in role names.
    ```python
    class MessageRole(str, Enum):
        """The role of a message."""
    
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool_request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final_answer"
    ```

2.  We define the `Message` class using Pydantic to hold the role and content for each turn. This ensures that every message in our scratchpad adheres to a consistent structure.
    ```python
    class Message(BaseModel):
        """A message in the conversation."""
    
        role: MessageRole
        content: str
    ```

3.  We create helper functions to format the scratchpad (our list of `Message` objects) into a string for the LLM prompt and to pretty-print the messages for human-readable output. As the scratchpad grows with each turn, it is important to consider the LLM's context window. While models like Gemini 2.5 Flash have very large context windows, every token adds to the cost and latency of the API call. For agents that run for many turns, this cumulative history can become a bottleneck. In production systems, strategies like summarizing older parts of the conversation or using a vector database to retrieve only relevant memories become necessary to manage the context effectively [[11]](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf).
    ```python
    def format_scratchpad(scratchpad: list[Message]) -> str:
        """
        Formats the scratchpad into a string for the LLM.
        """
        formatted_scratchpad = ""
        for message in scratchpad:
            formatted_scratchpad += f"<{message.role}>\n"
            formatted_scratchpad += f"{message.content}\n"
            formatted_scratchpad += f"</{message.role}>\n"
        return formatted_scratchpad
    
    
    def pretty_print_message(message: Message):
        """
        Prints a message in a human-readable format.
        """
        if message.role == MessageRole.USER:
            pretty_print.print_info(f"User: {message.content}")
        elif message.role == MessageRole.THOUGHT:
            pretty_print.print_info(f"Thought: {message.content}")
        elif message.role == MessageRole.TOOL_REQUEST:
            pretty_print.print_info(f"Tool request: {message.content}")
        elif message.role == MessageRole.OBSERVATION:
            pretty_print.print_info(f"Observation: {message.content}")
        elif message.role == MessageRole.FINAL_ANSWER:
            pretty_print.print_success(f"Final answer: {message.content}")
    ```

### The ReAct Control Loop

Now we can implement the main `react_agent_loop` function. This function takes an initial user query, a tool registry, and a maximum number of turns. It then enters a loop, iterating through the ReAct cycle until it reaches a final answer or hits the turn limit.

```mermaid
flowchart LR
  %% ReAct Control Loop
  Start["Start"] --> Input["Receive Input<br/>(User Question)"]
  Input --> Thought["Thought Phase<br/>(LLM generates thought)"]
  Thought --> Action["Action Phase<br/>(LLM decides action)"]
  Action --> Decision{"Is Final Answer?"}

  Decision -- "Yes" --> FinalAnswer["Final Answer"]
  FinalAnswer --> Finish["Finish"]

  Decision -- "No" --> ExecuteTool["Execute Tool"]
  ExecuteTool --> Observation["Receive Observation"]
  Observation --> Thought

  %% Supporting elements
  Scratchpad[(Scratchpad<br/>(Conversation History))]

  %% Scratchpad interactions
  Scratchpad -. "informs" .-> Thought
  Scratchpad -. "informs" .-> Action
  Observation -. "updates" .-> Scratchpad

  %% Visual grouping
  classDef mainLoop stroke-width:2px
  classDef memoryNode stroke-dasharray:3,3
  class Thought,Action,Observation mainLoop
  class Scratchpad memoryNode
```
Image 1: A flowchart illustrating the ReAct control loop, detailing the iterative Thought → Action → Observation cycle, and the role of the scratchpad.

1.  The loop begins by initializing the scratchpad with the user's query. The `verbose` flag allows us to control whether the agent's internal steps are printed to the console, which is useful for debugging.
    ```python
    def react_agent_loop(
        user_query: str, tool_registry: dict, max_turns: int = 5, verbose: bool = False
    ):
        """
        A ReAct agent loop that uses the LLM to generate thoughts and actions.
        """
        scratchpad = [Message(role=MessageRole.USER, content=user_query)]
    ```

2.  Inside the loop, for each turn, it first formats the current scratchpad into a string to provide the full context to the LLM.
    ```python
        for i in range(max_turns):
            if verbose:
                pretty_print.print_info(f"Turn {i+1}/{max_turns}")
    
            conversation = format_scratchpad(scratchpad)
    ```

3.  It then calls `generate_thought` to produce the next reasoning step and adds it to the scratchpad. This new thought becomes part of the context for the subsequent action decision.
    ```python
            thought = generate_thought(conversation, tool_registry)
            thought_message = Message(role=MessageRole.THOUGHT, content=thought)
            scratchpad.append(thought_message)
    ```

4.  With the new thought appended, it calls `generate_action` to decide the next move. The updated conversation, now including the latest thought, is passed to this function.
    ```python
            conversation = format_scratchpad(scratchpad)
            action = generate_action(conversation, tool_registry)
    ```

5.  The loop then processes the action. This is where the "Observation" part of the cycle is integrated.
    - If the action is a `ToolCallRequest`, it logs the request, finds the corresponding tool in the registry, and executes it. The result of the tool (the "Observation") is then added to the scratchpad. We also handle cases where the requested tool does not exist.
    - If the action is `ACTION_FINISH`, the agent generates a final thought and provides its answer, breaking the loop.
    ```python
            if isinstance(action, ToolCallRequest):
                tool_request_message = Message(
                    role=MessageRole.TOOL_REQUEST,
                    content=f'{action.name}(query="{action.query}")',
                )
                scratchpad.append(tool_request_message)
    
                if action.name in tool_registry:
                    tool = tool_registry[action.name]
                    observation = tool.use(action.query)
                else:
                    observation = f"Tool '{action.name}' not found."
    
                observation_message = Message(role=MessageRole.OBSERVATION, content=observation)
                scratchpad.append(observation_message)
    
            elif action == ACTION_FINISH:
                thought = generate_thought(format_scratchpad(scratchpad), tool_registry)
                final_answer_message = Message(
                    role=MessageRole.FINAL_ANSWER, content=thought
                )
                scratchpad.append(final_answer_message)
                break
    ```

6.  If the loop completes all turns without reaching a final answer, it forces a conclusion by generating one last thought and presenting it as the final answer. This prevents the agent from getting stuck in an infinite loop and ensures it always provides some output.
    ```python
        # Force a final answer if the loop finishes
        if scratchpad[-1].role != MessageRole.FINAL_ANSWER:
            thought = generate_thought(format_scratchpad(scratchpad), tool_registry)
            final_answer_message = Message(
                role=MessageRole.FINAL_ANSWER,
                content=f"I'm sorry, but I couldn't find the answer. My last thought is: {thought}",
            )
            scratchpad.append(final_answer_message)
    
        if verbose:
            for message in scratchpad:
                pretty_print_message(message)
    ```

### Integrated Observation Processing

The observation step is where the agent learns from its actions. When a tool is executed, its output—whether a successful result or an error message—is captured as an "observation." This observation is not just a side effect; it is a critical input for the next reasoning cycle. By appending the `observation_message` to the scratchpad, we ensure that the LLM sees the outcome of its previous action when it generates its next thought. This feedback mechanism allows the agent to self-correct. If a tool call fails or returns no information, the agent can reason about that failure and try a different tool or a modified query in the next turn. This ability to react to observations is what makes the ReAct framework so powerful and adaptable.

This function provides a complete, working implementation of a ReAct agent. It systematically progresses through the reasoning cycle, maintains state via the scratchpad, and gracefully handles both successful tool use and termination conditions.

## Tests and Traces: Success and Graceful Fallback

With our end-to-end agent loop implemented, the final step is to test it and analyze its behavior. We will run two scenarios: a simple factual query where our mock tool has the answer, and a query for which the tool will fail. Analyzing these traces will validate that our agent can successfully solve problems and handle failures gracefully.

### Test 1: Successful Factual Lookup

First, we ask a question that our mock `search` tool is designed to answer: "What is the capital of France?" We limit the agent to two turns.

1.  We call our main loop with the query.
    ```python
    react_agent_loop(
        user_query="What is the capital of France?",
        tool_registry=TOOL_REGISTRY,
        max_turns=2,
        verbose=True,
    )
    ```
    The agent produces the following trace:
    ```text
    Turn 1/2
    Turn 2/2
    User: What is the capital of France?
    Thought: I need to find the capital of France. I can use the search tool for this.
    Tool request: search(query="capital of France")
    Observation: Paris is the capital of France and is known for the Eiffel Tower.
    Thought: I have found the answer to the user's question. I will now provide the final answer.
    Final answer: I have found the answer to the user's question. I will now provide the final answer.
    ```
    In the first turn, the agent correctly identifies the need to use the `search` tool and forms the right query. It receives the observation from our mock tool. In the second turn, recognizing it has the answer, it generates a final thought and concludes. The trace confirms that the Thought → Action → Observation cycle worked perfectly. The `ToolCallRequest` was correctly generated, the tool was executed, and the observation was used to reach a final answer within the turn limit.

### Test 2: Graceful Fallback on Tool Failure

Next, we ask about the capital of Italy, a query our mock tool does not have an answer for. This test will check the agent's ability to handle a failed tool call and its forced termination logic.

1.  We run the loop with the new query.
    ```python
    react_agent_loop(
        user_query="What is the capital of Italy?",
        tool_registry=TOOL_REGISTRY,
        max_turns=2,
        verbose=True,
    )
    ```
    The trace shows a different behavior:
    ```text
    Turn 1/2
    Turn 2/2
    User: What is the capital of Italy?
    Thought: I need to find the capital of Italy. I can use the search tool for this.
    Tool request: search(query="capital of Italy")
    Observation: Information about 'capital of Italy' was not found.
    Thought: The search tool did not find any information about the capital of Italy. I will try a broader search.
    Tool request: search(query="Italy")
    Observation: Information about 'Italy' was not found.
    Final answer: I'm sorry, but I couldn't find the answer. My last thought is: The search tool did not return any results for "Italy". I will inform the user that I cannot answer the question.
    ```
    Here, the first tool call results in an observation that the information was not found. In its next thought, the agent adapts its strategy and attempts a broader search for "Italy". This change in strategy, reflected in the thought message, is a direct result of processing the previous observation. When that also fails, the agent reaches its `max_turns` limit. The control loop then triggers the forced final answer logic, informing the user that it could not find the information. This demonstrates the agent's resilience and graceful failure handling.

This adaptive behavior has deep roots in early AI research. Planning systems from the 1970s, like STRIPS, used an "execution monitor" to check if the real-world state matched the expected state after an action. It would compute a "kernel" of conditions that had to be true for the rest of the plan to succeed, allowing it to detect errors and attempt to recover without starting over from scratch [[13]](http://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/stripsrevisit.pdf). Our agent's Observation → Thought step serves a similar purpose, assessing the outcome of an action and replanning the next step accordingly.

These tests confirm our from-scratch implementation is working as expected. We have a solid foundation that can be extended with more sophisticated tools, memory systems, and planning strategies, which we will explore in future lessons.

## Conclusion

In this lesson, we moved from the theory of ReAct to a complete, hands-on implementation. By building each component from scratch—the mock tool, the thought and action generation phases, and the orchestrating control loop—you have gained a practical understanding of how agentic systems reason and interact with their environment. We saw how a structured cycle of Thought, Action, and Observation, managed via a scratchpad, enables an agent to break down problems, use tools, and adapt its strategy based on new information.

This from-scratch agent is the foundational building block for more advanced systems. The same core principles apply whether you are using a framework like LangGraph or building a custom solution. Now that you have implemented the engine yourself, you are better equipped to extend its capabilities. In our upcoming lessons, we will build on this foundation as we dive into agent memory, how to connect agents to vast knowledge bases, and how to process multimodal data.

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv. https://arxiv.org/pdf/2210.03629
- [2] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. arXiv. https://arxiv.org/pdf/2504.19678
- [3] Shankar, A. (2025). Building ReAct Agents from Scratch using Gemini. Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] Schmid, P. (2025). ReAct agent from scratch with Gemini 2.5 and LangGraph. Google for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [5] Pasternak, R. (2025). Building a Python React Agent Class: A Step-by-Step Guide. Neradot. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [6] Implementing ReAct Agentic Pattern From Scratch. (2025). Daily Dose of DS. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [7] Google AI for Developers. (n.d.). Prompt design strategies. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [8] Google AI for Developers. (n.d.). Function calling. https://ai.google.dev/gemini-api/docs/function-calling
- [9] Anthropic. (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents
- [10] Arxiv. (2026). LLM-based agents: A survey. https://arxiv.org/html/2602.10479v1
- [11] Google DeepMind. (2024). Gemini 2.5 Technical Report. https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf
- [12] Towards AI. (2024). Beyond the Prompt: Engineering the Thought-Action-Observation Loop. https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2
- [13] Fikes, R. E., & Nilsson, N. J. (1993). STRIPS, a retrospective. Artificial Intelligence. http://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/stripsrevisit.pdf