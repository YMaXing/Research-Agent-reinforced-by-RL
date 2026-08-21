# Lesson 8: Building a ReAct Agent From Scratch

In our last lesson, we explored the theoretical foundations of AI agent planning, focusing on the ReAct pattern. We learned how agents can synergize reasoning and acting to solve complex problems. But theory only takes you so far. To truly understand how these systems work, you have to build them. This lesson is where we roll up our sleeves and do just that.

In a modern contact center, for instance, a ReAct agent can do more than answer basic questions. It can reason through a customer's complaint, query a CRM to check their purchase history, and decide whether to trigger a refund or escalate the case to a human specialist [[1]](https://www.salesforce.com/agentforce/ai-agents/react-agents/). This ability to plan and interact with external systems is what we will build from the ground up.

This is a 100% practical, step-by-step guide to building a minimal ReAct agent from scratch using only Python and the Gemini API. We will implement the full Thought → Action → Observation loop, from defining a mock tool to orchestrating a turn-based control loop.

By the end, you will have a working agent and, more importantly, a concrete mental model of how these reasoning systems operate. This hands-on experience is what separates prototyping from building production-grade AI. It gives you the confidence to debug, extend, and customize agents for any real-world task.

## Setup and Environment

Our first step is to set up a clean and reproducible Python environment. This ensures that the code from our notebook runs seamlessly and that the outputs you see match the expected traces. A well-organized environment is the foundation of any serious software project, and AI engineering is no exception.

1.  We start by loading our environment variables. We use a custom utility, `lessons.utils.env.load`, to manage API keys. This modular approach keeps sensitive information out of our code and makes it easy to switch between different environments.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```
    It outputs:
    ```text
    Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
    ```

2.  Next, we import the necessary libraries. We will use `google-genai` to interact with the Gemini API. We also import `pydantic` and `enum`, which are essential for creating structured, validated data models. `pydantic` allows us to define data schemas as Python classes, providing runtime type checking and validation. This is critical for ensuring the data flowing through our agent is predictable and reliable. `enum` helps us define a set of named constants, which we will use for message roles to make our code more readable and less error-prone. Finally, we import a custom pretty-printing utility to help us visualize the agent's internal state.
    ```python
    from enum import Enum
    from typing import Union, List, Dict, Any, TypedDict
    
    from google import genai
    from pydantic import BaseModel, Field
    
    from lessons.utils import pretty_print
    ```

3.  With our imports in place, we initialize the Gemini client.
    ```python
    client = genai.Client()
    ```

4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, a fast and cost-effective model well-suited for the simple tasks we are building.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model configured, our environment is ready. The next step is to give our agent an external capability it can use to interact with the world.

## Tool Layer: Mock Search Implementation

In Lesson 6, we learned how to give agents tools to perform actions. For this hands-on exercise, we will create a simple mock search tool. Instead of making real API calls to a search engine, this tool will return predefined, predictable responses.

This approach has several educational benefits. It allows us to focus purely on the mechanics of the ReAct loop without getting bogged down in external dependencies, API key management, or network issues. It also makes our agent's behavior deterministic, which is ideal for testing and debugging.

Our mock `search` function is designed to handle a few specific queries and provide a fallback response for anything else. The function signature includes type hints, and the docstring clearly describes what the tool does, its parameters, and what it returns. As we saw in Lesson 6, this documentation is not just for humans; LLMs use it to understand how and when to use the tool.

```python
def search(query: str) -> str:
    """
    Searches for information on a given topic and returns a concise summary.

    Args:
        query: The topic to search for.

    Returns:
        A summary of the search results or a 'not found' message.
    """
    print(f"Searching for: {query}")
    # A mock search tool that returns predefined responses for specific queries
    if query == "capital of France":
        return "Paris is the capital of France and is known for the Eiffel Tower."
    elif query == "latest AI advancements":
        return "Recent AI advancements include breakthroughs in large language models and generative AI."
    else:
        return f"Information about '{query}' was not found."
```

This concept of a well-documented tool is part of a larger principle: designing a good *agent-computer interface* (ACI). Just as human-computer interfaces require careful design, so do the interfaces we expose to agents. In one of their own agents, developers at Anthropic found that a tool requiring relative filepaths often failed, but switching to absolute filepaths made the model use it flawlessly. This highlights that tool design is as important as prompt design [[2]](https://www.anthropic.com/engineering/building-effective-agents).

In a production system, you would replace this mock function with calls to real external APIs. For example, you could use the `requests` library to query the Google Search API or a private, domain-specific knowledge base. While the implementation would change, the function signature and the ReAct loop that calls it would remain the same. This modular design is a key principle of good software engineering.

For instance, to integrate Google Search, you might use a service like Serper. Your function would handle the API call, including authentication and error handling, and then format the results into a string, preserving the same `search(query: str) -> str` signature [[3]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

With our tool defined, the agent now has a way to act. The next step is to build the reasoning component that decides when to use this tool.

## Thought Phase: Prompt Construction and Generation

The first step in the ReAct cycle is "Thought." This is where the agent analyzes the current situation and creates a plan. We implement this by prompting the LLM with the conversation history and a description of the available tools, asking it to generate a reasoning step.

1.  To give the model context about its capabilities, we format our tool descriptions using XML tags. This is a robust prompt engineering technique that helps the model clearly distinguish between different pieces of information. We create a helper function, `build_tools_xml_description`, to generate this XML block from a registry of available tools.
    ```python
    def build_tools_xml_description(tool_registry: Dict[str, Any]) -> str:
        """Builds an XML-like description of the available tools."""
        xml = "<tools>\n"
        for tool_name, tool_func in tool_registry.items():
            xml += f"<tool name=\"{tool_name}\">\n"
            xml += f"<description>{tool_func.__doc__}</description>\n"
            xml += "</tool>\n"
        xml += "</tools>"
        return xml
    
    TOOL_REGISTRY = {"search": search}
    tools_xml = build_tools_xml_description(TOOL_REGISTRY)
    ```

2.  Next, we define the prompt template for the thought-generation phase. It instructs the agent to analyze the conversation and the available tools, and then to output its reasoning inside `<thought>` tags. The `{conversation}` placeholder will be dynamically filled with the current history.
    ```python
    PROMPT_TEMPLATE_THOUGHT = """
    You are a helpful assistant. Your goal is to assist the user with their questions.
    You have access to the following tools:
    {tools_xml}
    
    The conversation so far is:
    <conversation>
    {conversation}
    </conversation>
    
    Your task is to analyze the conversation and the available tools and decide on the next step.
    Your output should be a single <thought> XML tag.
    """
    
    print(PROMPT_TEMPLATE_THOUGHT.format(tools_xml=tools_xml, conversation="..."))
    ```
    The full prompt sent to the model includes the tool description inside the `<tools>` block, making it clear what actions are available.
    ```text
    You are a helpful assistant. Your goal is to assist the user with their questions.
    You have access to the following tools:
    <tools>
    <tool name="search">
    <description>
        Searches for information on a given topic and returns a concise summary.
    
        Args:
            query: The topic to search for.
    
        Returns:
            A summary of the search results or a 'not found' message.
    </description>
    </tool>
    </tools>
    
    The conversation so far is:
    <conversation>
    ...
    </conversation>
    
    Your task is to analyze the conversation and the available tools and decide on the next step.
    Your output should be a single <thought> XML tag.
    ```

3.  Finally, we create the `generate_thought` function. It takes the current conversation and tool registry, formats the prompt, calls the Gemini API, and returns the model's textual response.
    ```python
    def generate_thought(conversation: str, tool_registry: Dict[str, Any]) -> str:
        """Generates a thought based on the conversation and available tools."""
        tools_xml = build_tools_xml_description(tool_registry)
        prompt = PROMPT_TEMPLATE_THOUGHT.format(
            tools_xml=tools_xml, conversation=conversation
        )
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    ```

This XML-based approach is one way to structure the agent's reasoning. An alternative, common in early ReAct implementations, is to prompt the model to generate a sequence of explicit `Thought:`, `Action:`, and `Observation:` text blocks. The agent's control loop would then parse this text to extract the next step. This method is more flexible but can be less reliable than structured outputs [[4]](https://www.ibm.com/think/topics/react-agent).

A thought is just a plan. It outlines what the agent intends to do, but it does not execute anything. The next step is to translate this plan into a concrete, executable action.

## Action Phase: Function Calling and Parsing

After generating a thought, the agent must decide on a concrete "Action." This could be calling a tool or, if it has enough information, providing a final answer to the user. We will implement this using Gemini's native function calling capabilities, which we covered in Lesson 6.

This approach is simpler and more robust than manually prompting the model to generate JSON for tool calls. We provide the Python function directly to the API, and Gemini handles the rest. It automatically inspects the function's signature and docstring to create a schema, which it uses to decide when and how to call the tool. This lets us keep our system prompt focused on high-level strategy rather than low-level tool implementation details [[5]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

While native function calling is robust, it represents a trade-off. For complex, unpredictable tasks, the explicit reasoning step of a full ReAct loop provides more adaptability. For simpler, more predictable tasks, a direct function call can be faster and more token-efficient [[4]](https://www.ibm.com/think/topics/react-agent).

1.  First, we define a Pydantic model for our action. This ensures the agent's decision is always returned in a structured format. The action can either be a tool call (with a name and arguments) or a final answer (a simple string). We also define a constant, `ACTION_FINISH`, to signal completion.
    ```python
    class ToolCallRequest(BaseModel):
        """A request to call a tool."""
        name: str
        args: Dict[str, Any]
    
    ACTION_FINISH = "finish"
    ```

2.  Next, we create the `generate_action` function. This is the core of our action phase. It takes the conversation history and the list of available tools and calls the Gemini model.
    ```python
    def generate_action(
        conversation: str, tool_registry: Dict[str, Any]
    ) -> Union[ToolCallRequest, str]:
        """
        Generates an action (tool call or final answer) based on the conversation.
        """
        prompt = f"""
        You are a helpful assistant. Your goal is to assist the user with their questions.
        You have access to a set of tools.
        The conversation so far is:
        <conversation>
        {conversation}
        </conversation>
        
        Based on the conversation, decide if you need to use a tool or if you can provide a final answer.
        If you need to use a tool, call the tool.
        If you have enough information, provide the final answer by calling the '{ACTION_FINISH}' tool with the answer as the 'response' argument.
        """
        
        tools = list(tool_registry.values())
        response = client.models.generate_content(
            model=MODEL_ID, contents=prompt, tools=tools
        )
        
        # ... parsing logic ...
    ```
    It is worth noting a specific behavior of Gemini models: while lowering the temperature often increases determinism, for complex reasoning tasks, setting it below the default of 1.0 can sometimes lead to degraded performance or looping. Forcing determinism is often better handled through schema constraints than temperature adjustments [[6]](https://stevekinney.com/writing/prompt-engineering-frontier-llms).

3.  Inside `generate_action`, we parse the model's response. The Gemini API returns a `function_call` object if it decides to use a tool. We check for this object in the response.
    ```python
    # Continued from generate_action
    
    try:
        function_call = response.candidates[0].content.parts[0].function_call
    
        if function_call.name == ACTION_FINISH:
            return function_call.args["response"]
    
        return ToolCallRequest(name=function_call.name, args=dict(function_call.args))
    
    except (AttributeError, IndexError):
        # If no function call is present, return the text response as the final answer.
        return response.text.strip()
    ```
    If a `function_call` exists, we check if its name is `ACTION_FINISH`. If so, we return the content of the `response` argument as the final answer. Otherwise, we construct a `ToolCallRequest` object with the tool's name and arguments. If no `function_call` is present, it means the model generated a direct text response, which we treat as the final answer.

4.  To make `ACTION_FINISH` a valid "tool" that the model can call, we define a simple Python function for it. This function takes a single `response` argument and is added to our tool registry. This clever trick allows us to use the same function-calling mechanism for both tool execution and finishing the task.
    ```python
    def finish(response: str) -> str:
        """
        Provides the final answer to the user.
        
        Args:
            response: The final answer.
        """
        return response
    
    
    TOOL_REGISTRY = {"search": search, "finish": finish}
    ```

This completes the Action phase. We can now generate a thought and translate it into a concrete, executable step. However, production systems need to be resilient. If a tool fails—due to a network error, invalid input, or an API outage—the agent should not crash. A robust implementation would include retry mechanisms with exponential backoff, circuit breakers to prevent repeated calls to a failing service, and clear, user-facing error messages that allow the agent to reason about the failure and try a different approach. A more advanced pattern involves using `strict mode` validation, where the model provider guarantees that the generated tool calls are valid against your schema [[7]](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling).

We now have the "Thought" and "Action" components. The final piece is to orchestrate them in a control loop that manages the conversation state and executes the full ReAct cycle.

## Control Loop: Messages, Scratchpad, Orchestration

With the `Thought` and `Action` phases defined, we need a control loop to orchestrate the entire process. This loop will manage the state of the conversation, execute the agent's decisions, and process the outcomes, creating the iterative Thought → Action → Observation cycle that defines a ReAct agent.

1.  First, we need a structured way to represent the conversation history, which acts as the agent's short-term memory or "scratchpad." We will use Pydantic models to define a `Message` and an `enum` for `MessageRole`. This ensures every entry in our history is strongly-typed and has a clear purpose, whether it is a user query, an agent's thought, a tool request, or an observation.
    ```python
    class MessageRole(str, Enum):
        """The role of the message sender."""
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool_request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final_answer"
    
    class Message(BaseModel):
        """A message in the conversation."""
        role: MessageRole
        content: str
    ```

2.  We also create helper functions to format the scratchpad for display and for input to the LLM. `format_scratchpad` converts our list of `Message` objects into a simple, human-readable string, using XML tags to delineate each part of the conversation.
    ```python
    def format_scratchpad(scratchpad: List[Message]) -> str:
        """Formats the scratchpad into a string for the LLM."""
        formatted_str = ""
        for msg in scratchpad:
            formatted_str += f"<{msg.role}>\n{msg.content}\n</{msg.role}>\n"
        return formatted_str
    ```
    This simple string formatting works for short conversations, but it has a scaling problem. With each turn, the scratchpad grows, and we send the entire history back to the model. This increases token consumption and costs with every step [[8]](https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/). Production systems often employ context compression techniques, such as summarizing early turns, stripping out non-essential content, or even offloading large tool outputs to a separate store and replacing them with a reference [[9]](https://www.langchain.com/blog/context-management-for-deepagents).

3.  Now, we build the main `react_agent_loop`. This function is the heart of our agent. It takes an initial user query, a tool registry, and a maximum number of turns. It initializes the scratchpad with the user's query and then enters a loop.
    ```python
    def react_agent_loop(
        user_query: str, tool_registry: Dict[str, Any], max_turns: int = 5
    ) -> List[Message]:
        """The main loop for the ReAct agent."""
        scratchpad = [Message(role=MessageRole.USER, content=user_query)]
        
        for i in range(max_turns):
            print(f"--- Turn {i+1}/{max_turns} ---")
            # ... loop logic ...
            
        return scratchpad
    ```

4.  Inside the loop, the agent performs the full ReAct cycle:
    - **Thought:** It calls `generate_thought` using the current scratchpad content. In our implementation, the agent generates a thought at every turn. However, the original ReAct paper notes that for some tasks, thoughts only need to appear sparsely when the agent needs to re-evaluate its plan. This is a design choice that trades off between explicit reasoning at every step and token efficiency [[10]](https://arxiv.org/pdf/2210.03629). The thought is added to the scratchpad.
    - **Action:** It calls `generate_action`. Based on the response, it either prepares to call a tool or identifies a final answer.
    - **Observation:** If a `ToolCallRequest` is generated, the loop looks up the tool in the `tool_registry` and executes it. The tool's output is captured as the "observation." If the tool does not exist or fails, an informative error message becomes the observation. A more advanced recovery pattern involves feeding the error message back to the model and asking it to *repair* the tool call, allowing it to self-correct invalid arguments or choose a different tool entirely [[7]](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling). The observation is then added to the scratchpad.
    The loop terminates if a final answer is produced or if it reaches the `max_turns` limit. The `max_turns` limit is a simple but critical safeguard against a common failure mode: infinite loops. High network latency or a model bug can cause an agent to get stuck, rapidly consuming its budget without making progress. Capping the number of cycles turns this runaway behavior into a controlled failure [[11]](https://blog.logrocket.com/5-reasons-ai-app-fails-production/).

    Here is the full implementation of the loop:
    ```python
    def react_agent_loop(
        user_query: str, tool_registry: Dict[str, Any], max_turns: int = 5, verbose: bool = False
    ) -> List[Message]:
        """The main loop for the ReAct agent."""
        scratchpad = [Message(role=MessageRole.USER, content=user_query)]
    
        for i in range(max_turns):
            if verbose:
                print(f"--- Turn {i+1}/{max_turns} ---")
    
            # 1. THOUGHT
            conversation = format_scratchpad(scratchpad)
            thought = generate_thought(conversation, tool_registry)
            thought_message = Message(role=MessageRole.THOUGHT, content=thought)
            scratchpad.append(thought_message)
            if verbose:
                pretty_print.message(thought_message)
    
            # 2. ACTION
            conversation = format_scratchpad(scratchpad)
            action = generate_action(conversation, tool_registry)
    
            if isinstance(action, str):
                # Final answer
                final_answer_message = Message(role=MessageRole.FINAL_ANSWER, content=action)
                scratchpad.append(final_answer_message)
                if verbose:
                    pretty_print.message(final_answer_message)
                return scratchpad
    
            tool_request_message = Message(
                role=MessageRole.TOOL_REQUEST, content=action.model_dump_json()
            )
            scratchpad.append(tool_request_message)
            if verbose:
                pretty_print.message(tool_request_message)
    
            # 3. OBSERVATION
            if action.name in tool_registry:
                tool_func = tool_registry[action.name]
                try:
                    observation = tool_func(**action.args)
                except Exception as e:
                    observation = f"Error executing tool {action.name}: {e}"
            else:
                observation = f"Unknown tool: {action.name}. Available tools: {list(tool_registry.keys())}"
    
            observation_message = Message(role=MessageRole.OBSERVATION, content=str(observation))
            scratchpad.append(observation_message)
            if verbose:
                pretty_print.message(observation_message)
    
        # Forced final answer if max_turns is reached
        final_answer_message = Message(
            role=MessageRole.FINAL_ANSWER, content="I'm sorry, but I couldn't find an answer."
        )
        scratchpad.append(final_answer_message)
        if verbose:
            pretty_print.message(final_answer_message)
    
        return scratchpad
    ```
    This control loop directly maps to the ReAct pattern. The nodes in a framework like LangGraph represent the "Reason" (`generate_thought` and `generate_action`) and "Act" (`tool_func`) phases, the state is our `scratchpad`, and the edges create the iterative loop [[12]](https://www.decodingai.com/p/building-production-react-agents).

    ```mermaid
    flowchart LR
      _start_ --> "llm"
      "llm" -- "continue" --> "tools"
      "llm" -- "end" --> _end_
      "tools" --> "llm"
    ```
    Image 1: A flowchart illustrating the LangGraph implementation of the ReAct agent control loop.

The loop appears correct, but the real test is seeing it in action. Let's run it with a few queries to validate its behavior.

## Tests and Traces: Success and Graceful Fallback

With our complete ReAct loop implemented, it is time to test it. Analyzing the execution traces will help us verify that the agent behaves as expected, both in successful scenarios and when encountering failures. This hands-on validation is essential for building confidence in the agent's reliability.

First, we will ask a simple factual question that our mock `search` tool can answer: *"What is the capital of France?"* We will limit the agent to two turns.

```python
react_agent_loop(
    user_query="What is the capital of France?",
    tool_registry=TOOL_REGISTRY,
    max_turns=2,
    verbose=True,
)
```

The trace clearly shows the ReAct cycle in action:
```text
--- Turn 1/2 ---
THOUGHT:
<thought>
The user is asking for the capital of France. I should use the search tool to find this information.
</thought>

TOOL_REQUEST:
{"name":"search","args":{"query":"capital of France"}}

Searching for: capital of France
OBSERVATION:
Paris is the capital of France and is known for the Eiffel Tower.

--- Turn 2/2 ---
THOUGHT:
<thought>
I have found the answer to the user's question. The capital of France is Paris. I should now provide the final answer.
</thought>

FINAL_ANSWER:
Paris is the capital of France.
```
In the first turn, the agent correctly reasons that it needs to use the `search` tool and forms the right query. It executes the tool and receives the observation. In the second turn, it recognizes that it has the answer and provides it, terminating the loop gracefully.

Next, let's test a scenario where the tool fails. We will ask about the capital of Italy, a query our mock tool is not programmed to handle.

```python
react_agent_loop(
    user_query="What is the capital of Italy?",
    tool_registry=TOOL_REGISTRY,
    max_turns=2,
    verbose=True,
)
```

The trace demonstrates the agent's fallback behavior:
```text
--- Turn 1/2 ---
THOUGHT:
<thought>
The user is asking for the capital of Italy. I should use the search tool to find this information.
</thought>

TOOL_REQUEST:
{"name":"search","args":{"query":"capital of Italy"}}

Searching for: capital of Italy
OBSERVATION:
Information about 'capital of Italy' was not found.

--- Turn 2/2 ---
THOUGHT:
<thought>
The search tool did not find information about the capital of Italy. I will try a broader search for "Italy" to see if I can find any relevant information.
</thought>

TOOL_REQUEST:
{"name":"search","args":{"query":"Italy"}}

Searching for: Italy
OBSERVATION:
Information about 'Italy' was not found.

FINAL_ANSWER:
I'm sorry, but I couldn't find an answer.
```
Here, the agent observes the failure from its first attempt. In the second turn, it adapts its strategy by trying a broader query. When that also fails, the loop reaches its `max_turns` limit and triggers the forced final answer, admitting it could not find the information. This demonstrates graceful failure, a critical feature of robust agents [[3]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

This reflects a fundamental trade-off identified in the original ReAct paper. While reasoning-only approaches like Chain-of-Thought are prone to factual hallucination, ReAct's reliance on external tools makes it vulnerable to "non-informative search"—if the tool returns no useful information, the agent can struggle to recover. Grounding the agent's reasoning in real tool outputs improves factuality but makes the overall process dependent on the quality of those tools and observations [[10]](https://arxiv.org/pdf/2210.03629).

While these simple tests are useful, a production-ready agent would require a much more comprehensive test suite. This would include edge cases (e.g., empty queries), adversarial prompts designed to confuse the agent, and performance benchmarks to measure latency and cost. Methodologies from traditional software engineering, such as unit tests for individual tools and integration tests for the entire loop, are essential for ensuring an agent is reliable enough for production [[3]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae).

These successful tests confirm our end-to-end implementation and provide a solid baseline. We can now extend this agent with more sophisticated tools and behaviors in our upcoming lessons.

## Conclusion

By building a ReAct agent from scratch, we have moved from abstract theory to concrete implementation. We have seen how to orchestrate the full Thought-Action-Observation loop, from constructing prompts and parsing tool calls to managing a conversational scratchpad. This hands-on process demystifies what happens inside agentic frameworks and provides a solid mental model for how these systems reason and act.

Even if you end up using a framework like LangGraph in production, the understanding you have gained by building your own solution is invaluable. You now know how to debug, customize, and extend agentic behavior at a fundamental level. As noted by engineers at Anthropic, the most successful agentic systems are often built with simple, composable patterns rather than opaque, complex frameworks [[2]](https://www.anthropic.com/engineering/building-effective-agents). This is one of the core skills that separates an AI Engineer from a prompt engineer.

This lesson provides the practical foundation we will build upon throughout the rest of the course. In our next lessons, we will explore how to equip agents with long-term memory and enhance their capabilities with advanced Retrieval-Augmented Generation (RAG) techniques. This single-agent architecture is the fundamental building block for more complex multi-agent systems, where specialized agents collaborate to solve even larger problems [[13]](https://www.ibm.com/think/topics/ai-agent-orchestration).

## References

- [1] ReAct agents. (n.d.). Salesforce. https://www.salesforce.com/agentforce/ai-agents/react-agents/
- [2] Building effective agents. (2024, December 19). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [3] Shankar, A. (2024, June 10). Building ReAct Agents from Scratch using Gemini. Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] ReAct Agent. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [5] Gemini Function Calling Documentation. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [6] Kinney, S. (n.d.). Prompt Engineering with Frontier LLMs. Steve Kinney. https://stevekinney.com/writing/prompt-engineering-frontier-llms
- [7] Tool Calling. (n.d.). AI SDK. https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling
- [8] Optimizing Token Usage with Context Compression Techniques. (n.d.). SitePoint. https://www.sitepoint.com/optimizing-token-usage-context-compression-techniques/
- [9] Context Management for DeepAgents. (n.d.). LangChain Blog. https://www.langchain.com/blog/context-management-for-deepagents
- [10] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv. https://arxiv.org/pdf/2210.03629
- [11] 5 reasons your AI app fails in production. (n.d.). LogRocket Blog. https://blog.logrocket.com/5-reasons-ai-app-fails-production/
- [12] Iusztin, P. (2025, November 18). Building Production ReAct Agents From Scratch Is Simple. Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [13] AI Agent Orchestration. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [14] How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python? (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [15] How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python? (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [16] How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python? (n.d.). Google Cloud. https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking
- [17] Schmid, P. (2024, May 22). ReAct agent from scratch with Gemini 2.5 and LangGraph. Phil Schmid's Blog. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [18] Pasternak, R. (2024, November 5). Building a Python React Agent Class: A Step-by-Step Guide. Neradot. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [19] Brownlee, J. (2024, July 1). Building ReAct Agents with LangGraph: A Beginner’s Guide. Machine Learning Mastery. https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/
- [20] Daily Dose of DS. (2024, June 10). AI Agents Crash Course - Part 10: ReAct Framework with Implementation. Daily Dose of DS. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [21] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. arXiv. https://arxiv.org/pdf/2504.19678
- [22] Implementing ReAct Agentic Pattern From Scratch. (n.d.). Daily Dose of DS. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [23] Implementing ReAct Agentic Pattern From Scratch. (n.d.). Daily Dose of DS. https://blog.dailydoseofds.com/p/implement-react-agentic-pattern-from
- [24] Beyond the Prompt: Engineering the Thought-Action-Observation Loop. (n.d.). Towards AI. https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2
- [25] Build an AI coding agent with Python and Gemini. (n.d.). freeCodeCamp.org. https://www.freecodecamp.org/news/build-an-ai-coding-agent-with-python-and-gemini/
- [26] OrchDAG: Complex Tool Orchestration in Multi-turn Interactions with Plan DAGs. (n.d.). arXiv. https://arxiv.org/html/2510.24663v1
- [27] OrchDAG: Complex Tool Orchestration in Multi-turn Interactions with Plan DAGs. (n.d.). Amazon Science. https://www.amazon.science/publications/orchdag-complex-tool-orchestration-in-multi-turn-interactions-with-plan-dags
- [28] Real-world agent examples with Gemini 3. (n.d.). Google for Developers. https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/
- [29] AI Agents IV: AI Agents Through the Thought-Action-Observation (TAO) Cycle. (n.d.). Stackademic. https://blog.stackademic.com/ai-agents-iv-ai-agents-through-the-thought-action-observation-tao-cycle-3dfe2eb76629
- [30] Agent Steps and Structure. (n.d.). Hugging Face. https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure
- [31] AI Agent Planning. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [32] AI Agent Orchestration. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration