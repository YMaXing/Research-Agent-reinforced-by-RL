# Building a ReAct Agent From Scratch: A Step-by-Step Guide

In our last lesson, we covered the theory behind AI agent planning, focusing on frameworks like ReAct. Now, it’s time to get our hands dirty. This lesson is 100% practice. We are going to build a minimal ReAct agent from scratch, end-to-end, using only Python and the Gemini API.

The original ReAct paper showed that by grounding reasoning with actions—interacting with external tools—agents could overcome the hallucination and error propagation issues common in pure Chain-of-Thought models [[1]](https://arxiv.org/pdf/2210.03629). This synergy between reasoning and acting is the foundation of modern agentic AI.

When I first started building agents, I jumped straight into frameworks like LangGraph. I thought their graph-based models would make everything cleaner. Instead, I found myself fighting the framework. Simple `if-else` logic and basic loops became hours of work, forcing my code into an unnatural graph paradigm that added complexity without much value.

Frustrated, I did what I always do when I am stuck: I opened the source code. Reading LangGraph’s implementation of the ReAct loop was a lightbulb moment. It gave me a concrete mental model that the documentation never could. This pattern is not unique; it forms the basis for many emerging AI frameworks, including AutoGPT [[10]](https://www.techtarget.com/searchenterpriseai/tip/How-ReAct-agents-can-transform-the-enterprise). Even though I would not use the framework in production, understanding its internals became the foundation for building my own robust agents.

This hands-on approach is what separates production-grade AI from prototypes. By building the complete Thought → Action → Observation cycle yourself, you gain the confidence to extend, debug, and customize agents.

In this lesson, we will walk you through implementing:
*   A stable development environment.
*   A mock tool layer for predictable interactions.
*   The thought phase, where the agent plans its next move.
*   The action phase, powered by Gemini’s function calling.
*   A turn-based control loop to orchestrate the entire process.
*   Tests to validate success and graceful fallback behaviors.

Let's get started.

## Setup and Environment

Before we can build our agent, we need to set up a clean and predictable environment. This ensures your code runs smoothly and the outputs match the traces we will analyze later. This section follows the initial setup from the course notebook.

1.  First, we load our environment variables. We use a custom utility, `lessons.utils.env.load()`, to manage API keys. This modular approach keeps secrets out of our code and makes the project easier to configure.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```

2.  Next, we import the necessary libraries. We will use `google-genai` for interacting with the Gemini API, `pydantic` for data validation, and Python's `enum` and `typing` for creating structured and type-safe code. We also import a `pretty_print` utility to make our agent's traces easier to read.
    ```python
    import json
    from enum import Enum
    from typing import Callable, Union
    
    from google import genai
    from pydantic import BaseModel, Field
    
    from lessons.utils.pretty_print import pretty_print_conversation
    ```
    Using `pydantic` is a best practice for agent development. It allows us to define data schemas as Python classes, providing runtime validation that prevents malformed data from crashing our application. `Enum` helps us define a fixed set of message roles, making our agent's internal state explicit and easier to debug.

3.  We initialize the Gemini client. If you have both `GOOGLE_API_KEY` and `GEMINI_API_KEY` set, the library will default to one, and you might see a warning, which is safe to ignore.
    ```python
    client = genai.Client()
    ```

4.  Finally, we define the model we will use. For this lesson, `gemini-1.5-flash` is a great choice. It is fast, cost-effective, and powerful enough for the reasoning tasks our agent will perform.
    ```python
    MODEL_ID = "gemini-1.5-flash"
    ```

With the client and model configured, our environment is ready. The next step is to give our agent a capability—an external tool it can use to interact with the world.

## Tool Layer: Mock Search Implementation

An agent's power comes from its ability to use tools. For this lesson, we will create a mock search tool instead of calling a real API. This approach has several educational benefits: it simplifies our focus to the core ReAct mechanics, removes the need for external API keys, and provides predictable responses, which is essential for testing and debugging.

The ReAct framework was born from the insight that interleaving reasoning with tool use grounds the model in reality, overcoming the "hallucination and error propagation" common in pure reasoning systems [[1]](https://arxiv.org/pdf/2210.03629). Our mock tool simulates this grounding process.

Our mock search function will simulate a web search. It takes a query and returns a hardcoded response if the query matches a few predefined topics. If the query is unknown, it returns a "not found" message. This simulates how a real tool might behave.

1.  First, we define the mock search function. The docstring is important here; as we will see later, LLMs use the docstring to understand what a tool does and how to use it.
    ```python
    def search(query: str) -> str:
        """
        A mock search tool that returns predefined results for specific queries.
        This tool is for educational purposes to demonstrate tool integration.
        """
        print(f"Searching for: {query}")
        if "capital of france" in query.lower():
            return "Paris is the capital of France and is known for the Eiffel Tower."
        elif "python programming" in query.lower():
            return "Python is a high-level, interpreted programming language known for its simple syntax."
        else:
            return f"Information about '{query}' was not found."
    ```
    The quality of your tool definitions is as important as the quality of your prompts. Anthropic refers to this as designing the Agent-Computer Interface (ACI). A good tool definition includes clear parameter names, a descriptive docstring with examples, and well-defined boundaries to prevent confusion with other tools. For example, a file system tool that requires absolute paths instead of relative ones makes it harder for the agent to make mistakes [[11]](https://www.anthropic.com/engineering/building-effective-agents).

2.  Next, we create a `TOOL_REGISTRY` to store our tool. This registry maps the tool's name to its handler function, which allows our agent to dynamically call the correct function based on the LLM's output.
    ```python
    TOOL_REGISTRY = {
        "search": search,
    }
    ```

In a production system, you would replace this mock `search` function with a call to a real external API, like the Google Search API. This would involve handling API keys, managing network requests, and parsing the API's response format. You would also need to implement robust error handling for things like network timeouts, rate limiting, and invalid API responses. By starting with a mock tool, we can build and test the agent's reasoning loop in isolation before adding this complexity.

With a tool defined, the agent now needs a way to *think* about when and how to use it. This brings us to the first phase of the ReAct cycle: the Thought phase.

## Thought Phase: Prompt Construction and Generation

The "Thought" phase is where the agent reasons about the user's query and its history to form a plan. This process is a form of task decomposition, where the agent breaks a high-level goal into smaller, executable steps [[12]](https://www.ibm.com/think/topics/ai-agent-planning). This plan is a natural language string that outlines the next step, such as deciding to use a tool or formulate a final answer. We generate this thought by prompting an LLM with the current context.

1.  First, we need a way to describe our available tools to the LLM. We will create a helper function that generates an XML description from our `TOOL_REGISTRY`. XML tags are a common prompt engineering technique that helps the model distinguish between different parts of the prompt, improving its ability to follow instructions [[2]](https://ai.google.dev/gemini-api/docs/prompting-strategies).
    ```python
    def build_tools_xml_description(tool_registry: dict[str, Callable]) -> str:
        """
        Builds an XML string describing the available tools.
        """
        xml = "<tools>\n"
        for name, func in tool_registry.items():
            xml += f'<tool name="{name}">\n'
            xml += f"<description>{func.__doc__}</description>\n"
            xml += "</tool>\n"
        xml += "</tools>"
        return xml
    
    
    tools_xml_description = build_tools_xml_description(TOOL_REGISTRY)
    ```

2.  Next, we define the prompt template for generating a thought. This template provides the model with the available tools and the conversation history, and instructs it to think step-by-step.
    ```python
    PROMPT_TEMPLATE_THOUGHT = """
    You are an AI assistant that can use tools to answer questions.
    
    <tools>
    {tools_xml_description}
    </tools>
    
    The conversation history is provided below.
    <conversation>
    {conversation}
    </conversation>
    
    Based on the conversation, what is your next thought?
    """
    ```
    When we print this template, we can see how the tool's docstring is embedded directly into the prompt, giving the LLM the context it needs to decide when to use the `search` tool.
    ```text
    You are an AI assistant that can use tools to answer questions.
    
    <tools>
    <tool name="search">
    <description>
            A mock search tool that returns predefined results for specific queries.
            This tool is for educational purposes to demonstrate tool integration.
            </description>
    </tool>
    </tools>
    
    The conversation history is provided below.
    <conversation>
    {conversation}
    </conversation>
    
    Based on the conversation, what is your next thought?
    ```

3.  Finally, we create a function to generate the thought. This function formats the prompt with the current conversation and tool registry, sends it to the Gemini model, and returns the model's text response.
    ```python
    def generate_thought(conversation: str, tool_registry: dict[str, Callable]) -> str:
        """
        Generates a thought based on the conversation history and available tools.
        """
        tools_xml_description = build_tools_xml_description(tool_registry)
        prompt = PROMPT_TEMPLATE_THOUGHT.format(
            tools_xml_description=tools_xml_description, conversation=conversation
        )
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    ```
    When calling the model, parameters like `temperature` control the randomness of the output. While a low temperature (e.g., 0.0) is often used for deterministic tasks, Gemini's documentation warns that for complex reasoning, lowering the temperature below the default of 1.0 can sometimes cause looping or degraded performance [[13]](https://stevekinney.com/writing/prompt-engineering-frontier-llms). It's a model-specific nuance to be aware of during tuning.

A thought is just an internal plan. To make it useful, the agent must translate that plan into a concrete action, like calling a tool or providing a final answer to the user.

## Action Phase: Function Calling and Parsing

The "Action" phase determines the agent's next concrete step. Instead of parsing the thought, we will ask the LLM to decide on an action directly using Gemini’s native function calling capability. This is a more robust and reliable approach.

Early ReAct agents relied on parsing text to extract actions, which was often brittle. Modern agents use structured function calling, which is more reliable, efficient, and less prone to errors [[14]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent). However, this introduces a trade-off. For predictable tasks, a direct function call might be faster, but for complex scenarios where the path is unknown, the full ReAct loop provides superior adaptability [[15]](https://www.ibm.com/think/topics/react-agent).

The strategy is to create a high-level system prompt that guides the agent's decision-making. We do not need to include tool signatures in this prompt because Gemini handles that automatically. When we provide Python functions in the `tools` configuration, the API extracts their name, docstring (for the description), and parameter types from the function signature. This separation keeps our prompts clean and focused on strategic guidance.

1.  First, we define a prompt template for the action phase. This prompt instructs the agent to analyze the conversation and decide whether to use a tool or provide a final answer.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are an AI assistant that can use tools to answer questions.
    Analyze the conversation and determine the next action.
    If you have enough information, provide a final answer.
    Otherwise, select a tool to gather more information.
    
    <conversation>
    {conversation}
    </conversation>
    """
    ```

2.  We define constants for our actions. `ACTION_FINISH` is a special marker for when the agent decides it has the final answer.
    ```python
    ACTION_FINISH = "finish"
    
    
    class ToolCallRequest(BaseModel):
        name: str
        args: dict
    
    
    Action = Union[ToolCallRequest, str]
    ```

3.  Next, we implement the `generate_action` function. This function takes the conversation and tool registry, configures the Gemini client with the available tools, and calls the model.
    ```python
    def generate_action(conversation: str, tool_registry: dict[str, Callable]) -> Action:
        """
        Generates an action (tool call or final answer) based on the conversation.
        """
        prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)
        tools = list(tool_registry.values())
        response = client.models.generate_content(
            model=MODEL_ID, contents=prompt, tools=tools
        )
        
        # Check if the model returned a function call
        if hasattr(response.candidates[0].content.parts[0], "function_call"):
            function_call = response.candidates[0].content.parts[0].function_call
            return ToolCallRequest(
                name=function_call.name, args=dict(function_call.args)
            )
        else:
            # If no function call, it's a final answer
            return ACTION_FINISH
    ```
    The core logic here is parsing the response. If the model returns a `function_call` object, we parse it into our `ToolCallRequest` Pydantic model. If not, we interpret the response as a signal to finish the task. This dual format gives the agent a clear way to either continue its work or conclude. In a production system, you would add more robust error handling to manage malformed responses, API latency, or unexpected outputs, perhaps with retry mechanisms or a fallback to a different reasoning path. Advanced patterns even involve feeding the error back to the model, allowing it to self-correct its tool call [[16]](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling#tool-call-repair).

We now have separate functions for the "Thought" and "Action" phases. The final piece is a control loop to orchestrate them, execute tools, and manage the "Observation" phase.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop is the heart of our ReAct agent. It orchestrates the full Thought-Action-Observation cycle, manages the conversation history (our "scratchpad"), and executes tools.

We will start by defining a structured way to represent messages in our scratchpad. This makes the agent's internal state explicit and easy to track.

1.  We define `MessageRole` using an `Enum` and a `Message` Pydantic model to structure each turn of the conversation.
    ```python
    class MessageRole(Enum):
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool_request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final_answer"
    
    
    class Message(BaseModel):
        role: MessageRole
        content: str
    ```

2.  We create helper functions to format the scratchpad for both the LLM and for human-readable logging.
    ```python
    def format_scratchpad_for_llm(scratchpad: list[Message]) -> str:
        """
        Formats the scratchpad into a string for the LLM prompt.
        """
        formatted_str = ""
        for msg in scratchpad:
            formatted_str += f"<{msg.role.value}>\n{msg.content}\n</{msg.role.value}>\n"
        return formatted_str
    ```
    In a long-running agent, the scratchpad can grow to exceed the model's context window. Production systems use context compression techniques, such as summarization or selectively removing less relevant turns, to manage token usage and prevent errors [[17]](https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/).

3.  Now, we build the main `react_agent_loop`. This function orchestrates the entire ReAct cycle. It runs for a maximum number of turns, generating a thought, then an action. If the action is a tool call, it executes the tool, records the output as an observation, and adds it to the scratchpad. If the action is to finish, or if it reaches the maximum turns, it generates a final answer and terminates.
    ```python
    def react_agent_loop(
        user_query: str, tool_registry: dict[str, Callable], max_turns: int = 5, verbose: bool = False
    ) -> str:
        """
        The main ReAct agent loop.
        """
        scratchpad = [Message(role=MessageRole.USER, content=user_query)]
    
        for turn in range(max_turns):
            if verbose:
                print(f"--- Turn {turn + 1}/{max_turns} ---")
    
            # 1. Thought Phase
            conversation = format_scratchpad_for_llm(scratchpad)
            thought = generate_thought(conversation, tool_registry)
            thought_message = Message(role=MessageRole.THOUGHT, content=thought)
            scratchpad.append(thought_message)
            if verbose:
                pretty_print_conversation([thought_message])
    
            # 2. Action Phase
            conversation = format_scratchpad_for_llm(scratchpad)
            action = generate_action(conversation, tool_registry)
    
            if action == ACTION_FINISH:
                break
    
            tool_request_content = f"Tool: {action.name}, Args: {json.dumps(action.args)}"
            tool_request_message = Message(
                role=MessageRole.TOOL_REQUEST, content=tool_request_content
            )
            scratchpad.append(tool_request_message)
            if verbose:
                pretty_print_conversation([tool_request_message])
    
            # 3. Observation Phase
            if action.name in tool_registry:
                tool_func = tool_registry[action.name]
                try:
                    observation = tool_func(**action.args)
                except Exception as e:
                    observation = f"Error executing tool {action.name}: {e}"
            else:
                observation = f"Tool '{action.name}' not found. Available tools: {list(tool_registry.keys())}"
    
            observation_message = Message(
                role=MessageRole.OBSERVATION, content=str(observation)
            )
            scratchpad.append(observation_message)
            if verbose:
                pretty_print_conversation([observation_message])
    
        # Generate Final Answer
        conversation = format_scratchpad_for_llm(scratchpad)
        final_answer_prompt = f"{conversation}\nProvide a final answer to the user's query."
        final_answer = client.models.generate_content(
            model=MODEL_ID, contents=final_answer_prompt
        ).text.strip()
        final_answer_message = Message(
            role=MessageRole.FINAL_ANSWER, content=final_answer
        )
        scratchpad.append(final_answer_message)
        if verbose:
            pretty_print_conversation([final_answer_message])
    
        return final_answer
    ```
    This implementation directly mirrors the theoretical ReAct pattern. The agent loops through thinking, acting, and observing, using the scratchpad as its short-term memory. The `max_turns` parameter is not just a failsafe; it is a critical guardrail to prevent runaway loops that can occur due to high API latency or repetitive model behavior, turning a potential infinite loop into a controlled failure [[18]](https://blog.logrocket.com/5-reasons-ai-app-fails-production/).

    This control loop can be visualized as a simple state graph, similar to what frameworks like LangGraph implement under the hood [[7]](https://www.decodingai.com/p/building-production-react-agents).

    ```mermaid
flowchart LR
  _start_ --> "llm"
  "llm" -- "continue" --> "tools"
  "llm" -- "end" --> _end_
  "tools" --> "llm"
```
    Image 1: A flowchart illustrating the LangGraph implementation of the ReAct agent control loop.

    Our `react_agent_loop` function is a manual implementation of this graph. The `llm` node represents our `generate_thought` and `generate_action` calls, and the `tools` node corresponds to the observation phase where we execute the tool function. The loop continues until the agent decides to `end`.

The loop seems complete, but the real test is seeing it in action. We need to validate its behavior on both successful and unsuccessful queries to ensure it is robust.

## Tests and Traces: Success and Graceful Fallback

With our ReAct loop fully implemented, it is time to test it. Analyzing the agent's execution traces allows us to verify that each component—thought, action, observation, and termination—is working as expected. We will run two tests: a simple factual query that our mock tool can answer and a query designed to fail.

### Success Case

First, let’s ask a question our mock `search` tool is designed to handle: "What is the capital of France?". We will run the loop for a maximum of two turns.

```python
react_agent_loop(
    user_query="What is the capital of France?",
    tool_registry=TOOL_REGISTRY,
    max_turns=2,
    verbose=True,
)
```

The output trace clearly shows the ReAct cycle in action:
*   **Turn 1/2:**
    *   **Thought:** The agent correctly identifies that it needs to find the capital of France and decides the `search` tool is appropriate.
    *   **Tool Request:** It generates a call to `search(query='capital of France')`.
    *   **Observation:** The control loop executes our mock tool, which returns the predefined answer: "Paris is the capital of France and is known for the Eiffel Tower."
*   **Turn 2/2:**
    *   **Thought:** After observing the result, the agent concludes it has enough information to answer the user's query.
    *   **Final Answer:** The loop terminates because the agent signals it is finished, and it generates the final, concise answer: "Paris is the capital of France."

This trace confirms that our agent can successfully use a tool to find information and formulate an answer.

### Graceful Fallback Case

Now, let’s test a query that our mock tool cannot answer: "What is the capital of Italy?". This will test the agent's ability to handle failure and adapt its strategy.

```python
react_agent_loop(
    user_query="What is the capital of Italy?",
    tool_registry=TOOL_REGISTRY,
    max_turns=2,
    verbose=True,
)
```

The trace for this query demonstrates graceful fallback:
*   **Turn 1/2:**
    *   **Thought & Tool Request:** The agent tries to search for "capital of Italy".
    *   **Observation:** Our mock tool returns the fallback message: "Information about 'capital of Italy' was not found."
*   **Turn 2/2:**
    *   **Thought:** Observing the failure, the agent adapts its strategy. It decides to try a broader search for just "Italy", hoping to find the capital that way.
    *   **Tool Request:** It calls `search(query='Italy')`.
    *   **Observation:** This search also fails, as "Italy" is not a predefined query in our mock tool.
*   **Final Answer (Forced):** The loop reaches its `max_turns` limit. The agent is forced to conclude and generates a final answer admitting it could not find the information: "I'm sorry, but I couldn't find information about the capital of Italy."

This example highlights the agent's resilience. Even with a simple mock tool, it attempts to recover from failure by adjusting its plan. The forced termination ensures the agent does not get stuck in an infinite loop. In a production setting, you would design more comprehensive test suites to cover edge cases, adversarial prompts, and performance benchmarks, much like in traditional software engineering.

These tests confirm our from-scratch implementation of the ReAct loop is working correctly, providing a solid baseline for building more advanced agents in future lessons.

## Conclusion

By building a ReAct agent from the ground up, we have demystified the magic behind agentic frameworks. We have seen how the Thought-Action-Observation loop is not an abstract concept but a concrete software pattern implemented with prompts, function calls, and a control loop. This hands-on process provides a solid mental model for how these systems reason, plan, and execute tasks.

When building agents, we recommend focusing on three core principles: maintain simplicity in your design, prioritize transparency by making planning steps explicit, and carefully craft your agent-computer interface through thorough tool documentation and testing [[11]](https://www.anthropic.com/engineering/building-effective-agents).

Even if you ultimately use a framework like LangGraph or CrewAI in production, this fundamental understanding is invaluable. You will be better equipped to debug unexpected behavior, customize agent logic, and optimize performance because you know what is happening under the hood. For example, a ReAct agent could be used in a contact center to reason through a customer complaint, query a CRM to check purchase history, and decide whether to trigger a refund or escalate to a human [[19]](https://www.salesforce.com/agentforce/ai-agents/react-agents/).

This lesson is a stepping stone. In our upcoming lessons, we will build upon this foundation to explore more advanced topics like agent memory and Retrieval-Augmented Generation (RAG). We will also look at emerging trends, like combining ReAct with reinforcement learning to enhance adaptability, as we prepare you to build truly production-grade AI systems [[20]](https://arxiv.org/html/2404.04650v1).

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. https://arxiv.org/pdf/2210.03629
- [2] *Prompting strategies*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [3] *Building ReAct Agents from Scratch using Gemini*. (2024, July 15). Google Cloud. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] Pasternak, R. (2024, November 5). *Building a Python React Agent Class: A Step-by-Step Guide*. Neradot. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [5] *Implementing ReAct Agentic Pattern From Scratch*. (2024, June 10). Daily Dose of DS. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [6] *Function calling*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [7] Iusztin, P. (2024, November 18). *Building Production ReAct Agents From Scratch Is Simple*. Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [8] *ReAct agent from scratch with Gemini 1.5 and LangGraph*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [9] Schmid, P. (2024, March 26). *Building a ReAct Agent from scratch with Gemini 1.5 Pro and LangGraph*. Phil Schmid's Blog. https://www.philschmid.de/langgraph-gemini-1-5-react-agent
- [10] *How ReAct agents can transform the enterprise*. (n.d.). TechTarget. https://www.techtarget.com/searchenterpriseai/tip/How-ReAct-agents-can-transform-the-enterprise
- [11] *Building effective agents*. (2024, December 19). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [12] *AI Agent Planning*. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [13] Kinney, S. (n.d.). *Prompt Engineering for Frontier LLMs*. Steve Kinney. https://stevekinney.com/writing/prompt-engineering-frontier-llms
- [14] Schmid, P. (n.d.). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. Phil Schmid's Blog. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [15] *ReAct Agent*. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [16] *Tool Calling*. (n.d.). Vercel. https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling#tool-call-repair
- [17] *Optimizing Token Usage with Context Compression Techniques*. (n.d.). SitePoint. https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/
- [18] *5 reasons your AI app fails in production*. (n.d.). LogRocket Blog. https://blog.logrocket.com/5-reasons-ai-app-fails-production/
- [19] *ReAct Agents*. (n.d.). Salesforce. https://www.salesforce.com/agentforce/ai-agents/react-agents/
- [20] *Autono: A Highly Robust Autonomous Agent Framework based on ReAct*. (2024). arXiv. https://arxiv.org/html/2404.04650v1