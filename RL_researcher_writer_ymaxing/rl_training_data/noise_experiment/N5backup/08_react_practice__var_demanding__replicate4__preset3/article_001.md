# Building a ReAct Agent From Scratch

In our last lesson, we explored the theory behind agentic planning and reasoning, focusing on patterns like ReAct. We saw how agents break down problems, create plans, and use tools to find solutions. But theory can only take you so far. When I started building my first serious AI agent, I decided to use a popular framework, thinking it would make everything cleaner. What I discovered was frustrating: simple if-else logic and basic loops that should have taken five minutes became hours of work. I had to force my Python code to fit a graph paradigm that felt unnatural and added complexity without real value [[10]](https://www.decodingai.com/p/building-production-react-agents).

After struggling, I did what I always do when I am stuck: I opened the framework’s source code and started reading. That is when everything clicked. Seeing how the ReAct loop, tool execution, and state management were actually implemented gave me a concrete mental model I could not get from the documentation. This experience taught me a valuable lesson: to truly master agentic systems, you have to build one from the ground up.

This lesson is 100% practical. We will build a minimal ReAct agent from scratch, end-to-end, using only Python and the Gemini API. The ReAct pattern, short for "Reasoning and Acting," was introduced to synergize the two fundamental capabilities of LLMs. The core idea is that by interleaving generated reasoning traces (thoughts) with actions that interact with external tools, an agent can overcome the factual hallucination common in reasoning-only models [[1]](https://arxiv.org/pdf/2210.03629). The actions ground the agent in real-world information, while the thoughts allow it to create and adjust its plan dynamically.

We will implement the full Thought → Action → Observation loop. You will define a mock tool, generate thoughts, select actions with function calling, execute those actions, process the observations, and orchestrate the entire process with a turn-based control loop. By building the core logic yourself, you will gain a deep understanding of how reasoning agents operate. This foundation will give you the confidence to debug, customize, and extend agents for any application.

Let's start building.

## Setup and Environment

Before we write any agent logic, we need to set up a clean and predictable environment. This ensures our code runs smoothly and the outputs match the expected traces. We will use the code from the course's GitHub repository, so make sure you have it cloned and ready.

1.  First, we load our environment variables. We have created a small utility in `lessons.utils.env` that loads the `GOOGLE_API_KEY` from a `.env` file, which is necessary to authenticate with the Gemini API.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```

2.  Next, we import the necessary libraries. We will use `google-genai` for interacting with the Gemini API, `pydantic` for creating structured data models, and `enum` for defining message roles. Our custom `pretty_print` utility will help us visualize the agent's traces.
    ```python
    import enum
    from typing import Union, List
    
    from google import genai
    from pydantic import BaseModel, Field
    
    from lessons.utils.pretty_print import pretty_print_message
    ```
    Using `pydantic` is a best practice for agent development. As we covered in Lesson 4 on structured outputs, Pydantic models allow us to enforce a schema on the data we handle. This creates a formal contract between different parts of our system, ensuring that data is predictable and valid. For example, when our agent decides to call a tool, we can use a Pydantic model to validate that the tool's name and arguments are correctly formatted before execution. This "fail-fast" approach prevents bad data from propagating and causing hard-to-debug errors downstream.

    Similarly, `Enum` provides a robust way to define a fixed set of categories, such as the roles in our conversation history (`USER`, `THOUGHT`, etc.). Using an enum instead of raw strings prevents typos and makes the code more self-documenting. These small design choices, focused on modularity and reusability, are essential for building robust and maintainable agentic systems that can scale in complexity.

3.  We initialize the Gemini client. If you have both `GOOGLE_API_KEY` and a legacy `GEMINI_API_KEY` set, the client will default to the former and may print a warning, which is safe to ignore.
    ```python
    client = genai.Client()
    ```

4.  Finally, we define the model we will use. For this lesson, `gemini-2.5-flash` is a perfect choice. It is fast, cost-effective, and powerful enough for the reasoning tasks we will be performing.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```
With the client and model ID in place, we are ready to define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

The power of a ReAct agent comes from its ability to use tools to interact with the outside world. For this lesson, we will create a simple mock search tool instead of calling a real API. This approach has several educational benefits:

-   It keeps the focus on the ReAct mechanics, not on the complexities of API integration.
-   It removes external dependencies, so you do not need extra API keys.
-   It provides predictable responses, which is essential for testing and verifying that our agent behaves as expected.

Building effective tools requires as much care as prompt engineering. The tool's name, description, and parameter definitions form an "agent-computer interface" that the LLM must interpret correctly. As researchers at Anthropic note, a good tool definition includes clear boundaries from other tools, examples, and edge cases [[4]](https://www.anthropic.com/engineering/building-effective-agents). They found that simple changes, like modifying a tool to require absolute file paths instead of relative ones, can flawlessly fix common agent errors.

Our mock search function is designed to return predefined answers for specific queries and a fallback message for anything else.

1.  We define the `search` function. Pay close attention to its signature and docstring. The docstring is not just for human readability; modern LLMs like Gemini use it to understand what the tool does, how to use it, and what arguments it expects. This is a core concept from Lesson 6 on function calling.
    ```python
    def search(query: str) -> str:
        """
        Searches for information on a given topic and returns a summary.
    
        Args:
            query: The topic to search for.
    
        Returns:
            A summary of the search results.
        """
        print(f"Searching for: '{query}'")
    
        # Mock responses
        if query == "capital of France":
            return "Paris is the capital of France and is known for the Eiffel Tower."
        elif query == "latest AI news":
            return "Recent AI news includes advancements in large language models and their applications in various industries."
        else:
            return f"Information about '{query}' was not found."
    ```

2.  We create a `TOOL_REGISTRY` to map the tool's name to its function handler. This registry will allow our control loop to dynamically execute the correct tool based on the model's decision.
    ```python
    TOOL_REGISTRY = {
        "search": search,
    }
    ```

### From Mock to Production

In a production environment, you would replace this mock function with a real API call. The agent's core logic would remain the same; only the implementation of the `search` function would change, demonstrating the modularity of this design. For example, to integrate a real Google Search API, you would update the function to handle authentication, network requests, and error handling.

Here is how you might implement a production-grade search tool:

1.  **API Key Management:** Store your API key securely, for instance, as an environment variable, and load it into your application. Never hardcode keys in your source code.
2.  **API Call Logic:** Use a library like `requests` to make the HTTP GET request to the search API endpoint. The query from the agent would be passed as a parameter in the URL.
3.  **Error Handling:** Wrap the API call in a `try...except` block to gracefully handle potential issues like network errors (`requests.exceptions.RequestException`), timeouts, or invalid API responses (e.g., a 4xx or 5xx status code). If an error occurs, the function should return an informative message that the agent can use in its next reasoning step, such as `"Error: The search API is currently unavailable."`
4.  **Response Parsing:** The API will return a JSON object. You would parse this response to extract the relevant information, such as the top search result's snippet or a summary, and format it into a clean string for the agent to observe.
5.  **Rate Limiting:** Production APIs often have rate limits. A robust implementation might include logic to handle these limits, perhaps by adding a small delay or implementing an exponential backoff strategy for retries.

By encapsulating all this complexity within the `search` function, you preserve a clean interface for the agent. The agent only needs to know the function's name (`search`) and its input (`query`), as defined in the docstring. This separation of concerns is a key principle for building scalable and maintainable agentic systems.

With our tool defined, the agent now needs a way to "think" about when and how to use it.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct loop is "Thought." This is where the agent reasons about the user's query and the conversation history to decide on a plan. The original ReAct paper demonstrated that interleaving reasoning with actions allows the agent to induce, track, and update its plan while grounding its reasoning in externally verified information. This synergy helps overcome the factual hallucinations that can plague reasoning-only approaches like Chain-of-Thought [[1]](https://arxiv.org/pdf/2210.03629). We guide this process with a carefully constructed prompt.

This phase is critical for the agent's performance. A well-structured thought process enables the agent to break down complex problems into smaller, manageable steps. For example, if asked a multi-hop question, the agent's first thought might be to identify the initial piece of information it needs to retrieve. This step-by-step reasoning makes the agent's behavior more transparent and easier to debug.

1.  We start by creating an XML description of our available tools. Using XML tags like `<tool>` and `<name>` helps the LLM clearly distinguish the tool's structure and purpose. This is a manual context engineering technique that improves the model's ability to reason about the tools it has. It provides a structured format that the model can easily parse, reducing ambiguity compared to describing tools in plain prose.
    ```python
    def build_tools_xml_description(tool_registry: dict) -> str:
        """Builds an XML description of the available tools."""
        prompt = "<tools>\n"
        for tool_name, tool_handler in tool_registry.items():
            prompt += f"<tool name=\"{tool_name}\">\n"
            prompt += f"{tool_handler.__doc__}"
            prompt += "</tool>\n"
        prompt += "</tools>"
        return prompt
    
    
    PROMPT_TEMPLATE_THOUGHT = """
    You have access to the following tools to help you answer the user's query.
    
    {tools}
    
    Given the following conversation, what is your next thought?
    
    <conversation>
    {conversation}
    </conversation>
    
    Your thought should be a brief, high-level plan for your next step.
    """
    ```

2.  Let's inspect the full prompt template. It instructs the model on its role, provides the tool descriptions, and includes a placeholder for the ongoing conversation. This structure separates the static instructions and tool definitions from the dynamic conversation history.
    ```python
    tools_xml = build_tools_xml_description(TOOL_REGISTRY)
    print(PROMPT_TEMPLATE_THOUGHT.format(tools=tools_xml, conversation="..."))
    ```
    It outputs:
    ```text
    You have access to the following tools to help you answer the user's query.
    
    <tools>
    <tool name="search">
    
            Searches for information on a given topic and returns a summary.
        
            Args:
                query: The topic to search for.
        
            Returns:
                A summary of the search results.
            
    </tool>
    </tools>
    
    Given the following conversation, what is your next thought?
    
    <conversation>
    ...
    </conversation>
    
    Your thought should be a brief, high-level plan for your next step.
    ```
    The output shows the `<tool>` block containing the docstring from our `search` function, followed by the `<conversation>` placeholder.

3.  Next, we implement the `generate_thought` function. This function takes the current conversation history and the tool registry, formats the prompt, calls the Gemini model, and returns the generated thought as a clean string.
    ```python
    def generate_thought(conversation: str, tool_registry: dict) -> str:
        """Generates a thought based on the conversation and available tools."""
        tools_xml = build_tools_xml_description(tool_registry)
        prompt = PROMPT_TEMPLATE_THOUGHT.format(
            tools=tools_xml, conversation=conversation
        )
    
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    
        return response.text.strip()
    ```
A quick note on model parameters: while many developers default to `temperature=0` for deterministic outputs in factual tasks, this can be counterproductive with Gemini models. For complex reasoning, Gemini's documentation warns that lowering the temperature below the default of 1.0 can cause looping or degraded performance. It is safer to rely on structured outputs and evaluation to ensure reliability [[13]](https://stevekinney.com/writing/prompt-engineering-frontier-llms).

With a coherent thought generated, the agent must now translate that plan into a concrete action, which could be either calling a tool or providing a final answer to the user.

## Action Phase: Function Calling and Parsing

The "Action" phase determines the agent's next concrete step. Instead of manually prompting the model with tool details, we will leverage Gemini's native function calling capabilities. This is a more robust and scalable approach. Early ReAct agents had to parse text-based actions from the LLM's output, like `Action: [search("Olivia Wilde boyfriend")]`, which was often brittle. Modern function calling provides a structured, reliable way to connect LLMs to external tools [[14]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent).

The key advantage here is the separation of concerns. The system prompt can focus on high-level strategic guidance, while the technical details of the tools are handled automatically by the API. When we pass our Python functions to the `tools` configuration of the Gemini API, it automatically inspects their signatures and docstrings to create the necessary schema. This lets the model know what tools are available without cluttering our main prompt. This approach is more efficient for predictable tasks, whereas the full ReAct loop excels in complex, dynamic scenarios where observing the agent's step-by-step reasoning is valuable [[2]](https://www.ibm.com/think/topics/react-agent).

1.  We define a new prompt template specifically for generating actions. This prompt is much simpler because it does not need to include the tool schemas. It instructs the agent to decide between using a tool or providing a final answer based on the conversation history.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are a helpful assistant that has access to a set of tools.
    Given the following conversation, decide whether to use a tool or to provide a final answer.
    
    If the conversation has concluded, provide a final answer to the original user query.
    
    <conversation>
    {conversation}
    </conversation>
    """
    ```

2.  Next, we define constants for our actions. `ACTION_FINISH` is a special string we will use to signal that the agent has completed its task. `ToolCallRequest` is a Pydantic model to structure the tool calls generated by the model.
    ```python
    ACTION_FINISH = "finish"
    
    
    class ToolCallRequest(BaseModel):
        """A request to call a tool."""
    
        name: str = Field(description="The name of the tool to call.")
        args: dict = Field(description="The arguments to pass to the tool.")
    ```

3.  The `generate_action` function is the core of this phase. It takes the conversation history and a list of tool handlers, configures the Gemini client with the tools, and calls the model.
    ```python
    def generate_action(
        conversation: str, tool_handlers: list
    ) -> Union[ToolCallRequest, str]:
        """
        Generates an action (tool call or final answer) based on the conversation.
        """
        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)
    
        response = client.models.generate_content(
            model=MODEL_ID, contents=prompt, tools=tool_handlers
        )
    
        # Check if the model wants to call a tool
        if response.candidates[0].content.parts[0].function_call:
            function_call = response.candidates[0].content.parts[0].function_call
            tool_call_request = ToolCallRequest(
                name=function_call.name, args=dict(function_call.args)
            )
            return tool_call_request
    
        # If not, it's a final answer
        return ACTION_FINISH
    ```
    The function then parses the model's response. If the response contains a `function_call` object, it means the model wants to use a tool. We parse this into our `ToolCallRequest` Pydantic model. If there is no `function_call`, we assume the model has generated a text response, which we interpret as the signal to finish.

### Advanced Error Handling in Production

In production, tool calls can fail for many reasons: invalid arguments, network issues, or the model calling a non-existent tool. A robust agent must handle these failures gracefully. While our current implementation includes basic error handling, a production system would require more advanced strategies.

-   **Retry Mechanisms:** For transient errors like network timeouts, implementing a retry mechanism with exponential backoff is a common pattern. This involves re-attempting the tool call after a short delay, with the delay increasing after each failed attempt. This prevents the agent from giving up immediately on a recoverable error.
-   **Circuit Breakers:** For more persistent failures, such as an API being down, a circuit breaker pattern can prevent the agent from repeatedly calling a failing service. After a certain number of consecutive failures, the circuit "opens," and subsequent calls to that tool are failed immediately for a cooldown period. This saves resources and prevents the agent from getting stuck.
-   **User-Facing Error Messages:** When a tool fails permanently or after several retries, the agent should not crash. Instead, the error should be returned as an observation (e.g., `"Error: The search service is currently unavailable. Please try again later."`). The agent can then reason about this observation and either try a different tool or inform the user about the problem, providing a much better user experience.

Production-grade libraries like Vercel's AI SDK include built-in error handling for these cases, such as `NoSuchToolError` and `InvalidToolInputError`. Some even offer experimental "tool call repair," where the error is fed back to the model, giving it a chance to correct its own mistake and retry the call [[15]](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling).

Now that we have implemented the "Thought" and "Action" phases, it is time to combine them with the "Observation" phase into a complete, orchestrated control loop.

## Control Loop: Messages, Scratchpad, and Orchestration

The control loop is the heart of our ReAct agent. It orchestrates the entire Thought-Action-Observation cycle, manages the conversation history (or "scratchpad"), and ensures the agent makes progress toward a solution. This orchestration is what transforms a series of individual LLM calls into a coherent, goal-oriented process.

To manage the scratchpad effectively, we will use a structured approach with Pydantic models and enums. This is far more robust than just appending strings to a list, as it provides clarity, type safety, and makes debugging much easier. Each entry in our scratchpad will be a `Message` object with a specific `role`, allowing us to trace the agent's journey from user query to final answer.

A key challenge in production is that the scratchpad grows with every turn, increasing token costs and potentially exceeding the context window. This is a classic context engineering problem. Advanced techniques like context compression, which summarizes or filters the conversation history, are often used to manage this pressure [[16]](https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/). For our minimal agent, we will keep the full history, but it is important to be aware of this challenge for real-world applications.

1.  We start by defining `MessageRole` using an `Enum` to represent the different types of messages in our conversation: user input, the agent's internal thoughts, tool requests, observations from tool executions, and the final answer. This ensures consistency and prevents errors from simple typos in role names.
    ```python
    class MessageRole(str, enum.Enum):
        """The role of a message."""
    
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool_request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final_answer"
    ```

2.  Next, we define the `Message` Pydantic model. Each message will have a `role` and `content`. This structure allows us to keep a clean, organized log of every step the agent takes, which is invaluable for debugging and analysis.
    ```python
    class Message(BaseModel):
        """A message in the conversation."""
    
        role: MessageRole
        content: str
    ```

3.  We create a helper function to format the scratchpad (our list of `Message` objects) into a single string that can be passed to the prompt templates for the thought and action phases. We use XML tags to clearly delineate each message's role and content, making it easier for the LLM to parse the history.
    ```python
    def format_scratchpad_for_prompt(scratchpad: List[Message]) -> str:
        """Formats the scratchpad for the prompt."""
        prompt = ""
        for message in scratchpad:
            prompt += f"<{message.role}>\n{message.content}\n</{message.role}>\n"
        return prompt
    ```

4.  Now we build the main `react_agent_loop` function. This function encapsulates the entire ReAct cycle. The original ReAct paper notes that for knowledge-intensive tasks, a dense thought-action-observation loop is effective, whereas for decision-making tasks, thoughts can be more sparse, appearing only when the agent needs to update its plan [[1]](https://arxiv.org/pdf/2210.03629). Our implementation uses a dense loop for simplicity and clarity.
    ```python
    def react_agent_loop(
        initial_query: str, max_turns: int, tool_registry: dict, verbose: bool = False
    ) -> str:
        """The main ReAct agent loop."""
        scratchpad = [Message(role=MessageRole.USER, content=initial_query)]
        tool_handlers = list(tool_registry.values())
    
        for i in range(max_turns):
            turn = i + 1
            if verbose:
                print(f"--- Turn {turn}/{max_turns} ---")
    
            # 1. Thought Phase
            conversation = format_scratchpad_for_prompt(scratchpad)
            thought = generate_thought(conversation, tool_registry)
            thought_message = Message(role=MessageRole.THOUGHT, content=thought)
            scratchpad.append(thought_message)
            if verbose:
                pretty_print_message(thought_message)
    
            # 2. Action Phase
            conversation = format_scratchpad_for_prompt(scratchpad)
            action = generate_action(conversation, tool_handlers)
    
            if action == ACTION_FINISH:
                # Provide a final answer
                final_answer_thought = "The conversation has concluded. I will now provide the final answer."
                final_answer_thought_message = Message(
                    role=MessageRole.THOUGHT, content=final_answer_thought
                )
                scratchpad.append(final_answer_thought_message)
                if verbose:
                    pretty_print_message(final_answer_thought_message)
    
                conversation = format_scratchpad_for_prompt(scratchpad)
                final_answer = client.models.generate_content(
                    model=MODEL_ID, contents=conversation
                ).text.strip()
                final_answer_message = Message(
                    role=MessageRole.FINAL_ANSWER, content=final_answer
                )
                scratchpad.append(final_answer_message)
                if verbose:
                    pretty_print_message(final_answer_message)
    
                return final_answer
    
            # 3. Observation Phase
            tool_request_message = Message(
                role=MessageRole.TOOL_REQUEST,
                content=action.model_dump_json(indent=2),
            )
            scratchpad.append(tool_request_message)
            if verbose:
                pretty_print_message(tool_request_message)
    
            if action.name in tool_registry:
                tool_handler = tool_registry[action.name]
                try:
                    observation = tool_handler(**action.args)
                except Exception as e:
                    observation = f"Error executing tool {action.name}: {e}"
            else:
                observation = f"Tool '{action.name}' not found. Available tools: {list(tool_registry.keys())}"
    
            observation_message = Message(role=MessageRole.OBSERVATION, content=observation)
            scratchpad.append(observation_message)
            if verbose:
                pretty_print_message(observation_message)
    
        # Forced final answer if max_turns is reached
        final_answer_thought = "The maximum number of turns has been reached. I will now provide the final answer based on the information gathered so far."
        final_answer_thought_message = Message(
            role=MessageRole.THOUGHT, content=final_answer_thought
        )
        scratchpad.append(final_answer_thought_message)
        if verbose:
            pretty_print_message(final_answer_thought_message)
    
        conversation = format_scratchpad_for_prompt(scratchpad)
        final_answer = client.models.generate_content(
            model=MODEL_ID, contents=conversation
        ).text.strip()
        final_answer_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
        scratchpad.append(final_answer_message)
        if verbose:
            pretty_print_message(final_answer_message)
    
        return final_answer
    ```
    The loop iterates for a maximum number of turns. In each turn, it generates a thought, then an action. If the action is to finish, it generates a final answer and exits. If the action is a tool call, it executes the corresponding function from the `TOOL_REGISTRY`, captures the output as an observation, and adds it to the scratchpad. The loop includes error handling for tool execution and gracefully handles cases where an unknown tool is requested. If the loop reaches `max_turns` without a resolution, it forces a final answer based on the information gathered so far.

This control loop is a simple yet powerful implementation of the ReAct pattern. A known failure mode in production systems is that high API latency can cause agents to get stuck in infinite "thinking" loops, rapidly consuming tokens without producing an output [[17]](https://discuss.ai.google.dev/t/gemini-3-1-pro-preview-high-latency-resolution-lag-and-massive-token-consumption-24h-lockout/127008). The `max_turns` parameter in our loop acts as a simple but essential circuit breaker to prevent this runaway behavior, turning a potential infinite loop into a controlled failure [[18]](https://blog.logrocket.com/5-reasons-ai-app-fails-production/).

The flow can be visualized as a cycle where the model (LLM) generates a plan, which leads to tool execution, and the result is fed back to the model to inform the next cycle.

```mermaid
flowchart LR
  _start_ --> "llm"
  "llm" -- "continue" --> "tools"
  "llm" -- "end" --> _end_
  "tools" --> "llm"
```
Image 1: A flowchart illustrating the LangGraph implementation of the ReAct agent control loop.

This diagram shows how the `llm` node (our `generate_thought` and `generate_action` functions) decides whether to `continue` to the `tools` node (executing an action) or `end` the process. The output from the `tools` node is then fed back to the `llm` node for the next iteration.

The agent seems to work in theory. Now, let's test it with some examples and analyze the traces to see it in action.

## Tests and Traces: Success and Graceful Fallback

With our `react_agent_loop` fully implemented, it is time to validate its behavior. We will run two tests: a simple factual query that should succeed and a query that our mock tool cannot answer, which should demonstrate the agent's graceful fallback and termination logic. Analyzing the verbose traces will give us a clear view into the agent's reasoning process at each step.

1.  First, let's ask a simple factual question that our mock `search` tool can answer: "What is the capital of France?". We will set `max_turns` to 2 to give it enough room to find the answer.
    ```python
    react_agent_loop(
        initial_query="What is the capital of France?",
        max_turns=2,
        tool_registry=TOOL_REGISTRY,
        verbose=True,
    )
    ```
    It outputs the following trace:
    ```text
    --- Turn 1/2 ---
    
    [THOUGHT]
    I need to find the capital of France. I can use the search tool for this.
    
    [TOOL_REQUEST]
    {
      "name": "search",
      "args": {
        "query": "capital of France"
      }
    }
    
    Searching for: 'capital of France'
    
    [OBSERVATION]
    Paris is the capital of France and is known for the Eiffel Tower.
    
    --- Turn 2/2 ---
    
    [THOUGHT]
    I have found the answer and can now provide it to the user.
    
    [THOUGHT]
    The conversation has concluded. I will now provide the final answer.
    
    [FINAL_ANSWER]
    Paris is the capital of France.
    ```
    The trace clearly shows the ReAct cycle. In Turn 1, the agent thinks about using the search tool, generates the correct `TOOL_REQUEST`, and receives an `OBSERVATION` with the answer. In Turn 2, it recognizes it has the information, generates a final thought, and provides the `FINAL_ANSWER`. The loop correctly terminates before reaching `max_turns`.

2.  Now, let's test the fallback behavior with a query our mock tool does not support: "What is the capital of Italy?". We will again use `max_turns=2`.
    ```python
    react_agent_loop(
        initial_query="What is the capital of Italy?",
        max_turns=2,
        tool_registry=TOOL_REGISTRY,
        verbose=True,
    )
    ```
    It outputs:
    ```text
    --- Turn 1/2 ---
    
    [THOUGHT]
    I need to find the capital of Italy. I can use the search tool to find this information.
    
    [TOOL_REQUEST]
    {
      "name": "search",
      "args": {
        "query": "capital of Italy"
      }
    }
    
    Searching for: 'capital of Italy'
    
    [OBSERVATION]
    Information about 'capital of Italy' was not found.
    
    --- Turn 2/2 ---
    
    [THOUGHT]
    The first search failed. I should try a broader search for "Italy" to see if I can find any relevant information that might lead me to the capital.
    
    [TOOL_REQUEST]
    {
      "name": "search",
      "args": {
        "query": "Italy"
      }
    }
    
    Searching for: 'Italy'
    
    [OBSERVATION]
    Information about 'Italy' was not found.
    
    [THOUGHT]
    The maximum number of turns has been reached. I will now provide the final answer based on the information gathered so far.
    
    [FINAL_ANSWER]
    I'm sorry, but I couldn't find information about the capital of Italy.
    ```
    This trace demonstrates the agent's resilience. In Turn 1, the initial search fails, and the agent observes the "not found" message. In Turn 2, its thought process adapts; it decides to try a broader query. When that also fails, the agent hits the `max_turns` limit. The control loop then triggers the forced final answer logic, and the agent gracefully admits it could not find the information. This behavior is exactly what we want in a production system: predictable termination and honest responses when information is unavailable.

### Designing a Robust Test Suite

Designing comprehensive tests like these, covering both success and failure scenarios, is a critical practice borrowed from traditional software engineering. A full test suite would go further, establishing a systematic way to validate the agent's behavior under a wide range of conditions.

-   **Unit Tests for Tools:** Each tool should have its own set of unit tests to verify its functionality in isolation. For our `search` tool, we would test that it returns the correct mock response for known queries and the correct fallback message for unknown ones.
-   **Integration Tests for the Loop:** The tests we just ran are a form of integration testing, verifying that the Thought, Action, and Observation phases work together correctly. A comprehensive suite would include more complex scenarios, such as multi-hop questions that require several tool calls in sequence.
-   **Edge Case Testing:** What happens if the user provides an empty query? Or a very long, convoluted one? What if a tool returns an unexpected data format? A robust test suite should cover these edge cases to ensure the agent does not crash or behave unpredictably.
-   **Adversarial Prompts:** This involves crafting prompts designed to trick or confuse the agent. For example, a prompt might try to make the agent call a non-existent tool or perform an illogical sequence of actions. Testing against these prompts helps identify vulnerabilities in the agent's reasoning and prompting.
-   **Performance Benchmarks:** In a production setting, you would also need to measure performance. This includes tracking latency (how long does the agent take to respond?), cost (how many tokens does it consume per query?), and accuracy (how often does it provide the correct final answer?). These benchmarks are essential for optimizing the agent and ensuring it meets business requirements.

By adopting these testing methodologies, we can build confidence in our agent's reliability and systematically identify and fix potential bugs before they impact users.

## Conclusion

In this lesson, we have moved from theory to practice by building a complete ReAct agent from scratch. We implemented every component of the Thought-Action-Observation loop: we defined a tool, generated thoughts to form a plan, used function calling to select actions, executed those actions, and orchestrated the entire flow with a stateful control loop. By analyzing the execution traces, we verified that our agent can successfully solve problems and handle failures gracefully.

This hands-on experience provides a solid mental model for how agents work under the hood, demystifying the "magic" and giving you the foundational knowledge needed to build, debug, and extend more complex agentic systems. The principles we have covered—clear tool design, structured state management, and robust control loops—are the foundation of production-ready agentic systems, whether you build them from scratch or use frameworks like LangGraph or BeeAI [[19]](https://www.techtarget.com/searchenterpriseai/tip/How-ReAct-agents-can-transform-the-enterprise), [[14]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent). These agents are already being deployed for complex tasks like customer support automation, where they can query a Customer Relationship Management (CRM) system, check purchase history, and even issue refunds [[20]](https://www.salesforce.com/agentforce/ai-agents/react-agents/).

With this foundation in place, you are now ready to tackle more advanced topics. In the next lessons, we will explore how to equip agents with memory to recall past interactions (Lesson 9) and how to connect them to vast knowledge bases using Retrieval-Augmented Generation (Lesson 10).

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. *arXiv*. https://arxiv.org/pdf/2210.03629
- [2] ReAct Agent. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [3] AI Agent Planning. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [4] Building effective agents. (n.d.). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [5] ReAct agent from scratch with Gemini 2.5 and LangGraph. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [6] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. *arXiv*. https://arxiv.org/pdf/2504.19678
- [7] Building ReAct Agents from Scratch using Gemini. (n.d.). Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [8] AI Agent Orchestration. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [9] Function calling. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [10] Iusztin, P. (2025). Building Production ReAct Agents From Scratch Is Simple. *Decoding AI*. https://www.decodingai.com/p/building-production-react-agents
- [11] Pasternak, R. (2024). Building a Python React Agent Class: A Step-by-Step Guide. *Neradot*. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [12] Implementing ReAct Agentic Pattern From Scratch. (n.d.). *Daily Dose of DS*. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [13] Kinney, S. (n.d.). Prompt Engineering with Frontier LLMs. https://stevekinney.com/writing/prompt-engineering-frontier-llms
- [14] Schmid, P. (n.d.). ReAct agent from scratch with Gemini 2.5 and LangGraph. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [15] Tool Calling. (n.d.). Vercel AI SDK. https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling
- [16] Optimizing Token Usage with Context Compression Techniques. (n.d.). SitePoint. https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/
- [17] Gemini 3.1 Pro Preview - High Latency, Resolution Lag, and Massive Token Consumption / 24h Lockout. (2024). Google for Developers. https://discuss.ai.google.dev/t/gemini-3-1-pro-preview-high-latency-resolution-lag-and-massive-token-consumption-24h-lockout/127008
- [18] 5 reasons your AI app fails in production. (n.d.). LogRocket Blog. https://blog.logrocket.com/5-reasons-ai-app-fails-production/
- [19] How ReAct agents can transform the enterprise. (n.d.). TechTarget. https://www.techtarget.com/searchenterpriseai/tip/How-ReAct-agents-can-transform-the-enterprise
- [20] ReAct Agents: How AI Can Reason, Act, and Learn Like a Pro. (n.d.). Salesforce. https://www.salesforce.com/agentforce/ai-agents/react-agents/