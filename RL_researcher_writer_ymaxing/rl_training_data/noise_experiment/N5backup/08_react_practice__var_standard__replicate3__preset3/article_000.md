# Lesson 8: Building a ReAct Agent From Scratch

In our previous lessons, we have covered the theoretical foundations of AI engineering. We have explored the landscape of AI agents, distinguished between rule-based workflows and autonomous agents, and learned the art of context engineering. We have also covered how to get structured data from LLMs, how to give them tools through function calling, and the theory behind reasoning patterns like ReAct.

This lesson is 100% practice. We will take everything we have learned and build a minimal ReAct agent from the ground up, using only Python and the Gemini API. By implementing the full Thought → Action → Observation loop yourself, you will gain a concrete mental model of how these reasoning agents work. This architecture creates a synergy between reasoning and acting: reasoning traces help the model track and update its plan, while actions allow it to interface with external sources to gather new information [[1]](https://arxiv.org/pdf/2210.03629). This hands-on experience is what gives you the confidence to extend, debug, and customize agents for production.

We will walk through the implementation step-by-step, mirroring the code in the associated notebook. You will learn how to:
- Set up the environment and select the right model.
- Define a mock tool to simulate external interactions.
- Generate thoughts to guide the agent’s reasoning.
- Select and parse actions using function calling.
- Orchestrate the full cycle in a turn-based control loop.
- Test the agent and analyze its success and failure traces.

## Setup and Environment

Our first step is to set up a clean Python environment to ensure the code runs smoothly and the outputs match our expected traces. This involves loading our API keys, importing the necessary libraries, and initializing the Gemini client.

1.  We start by loading our environment variables. The `lessons.utils.env.load()` helper function ensures our `GOOGLE_API_KEY` is available for the Gemini client.
    ```python
    from lessons.utils import env
    
    env.load(required_env_vars=["GOOGLE_API_KEY"])
    ```

2.  Next, we import the required libraries. We will use `google-genai` for interacting with the Gemini API, `pydantic` for data validation, and some standard typing modules.
    ```python
    import json
    from enum import Enum
    from typing import Union
    
    from google import genai
    from pydantic import BaseModel, Field
    
    from lessons.utils import pretty_print
    ```

3.  We initialize the Gemini client. This object is our main interface for making API calls.
    ```python
    client = genai.Client()
    ```

4.  Finally, we define the model we will use. For this lesson, we will use `gemini-2.5-flash`, which is a fast and cost-effective choice for tasks that do not require intensive, multi-step reasoning.
    ```python
    MODEL_ID = "gemini-2.5-flash"
    ```

With the client and model in place, we can now define an external capability for our agent to use.

## Tool Layer: Mock Search Implementation

To build a ReAct agent, we need to give it tools to interact with an external environment. For this lesson, we will create a simple mock search tool instead of calling a real API like Google Search. This approach offers several advantages for learning.

First, it simplifies our focus. We can concentrate on the mechanics of the ReAct loop—thought, action, and observation—without worrying about external dependencies, network latency, or managing API keys. Second, a mock tool provides predictable, consistent responses. This is essential for testing and debugging, as it allows us to verify that our agent behaves as expected in specific scenarios.

Our mock `search` function will simulate a web search. It takes a query and returns a hardcoded string if the query matches a few predefined topics. If the query is not recognized, it returns a "not found" message, simulating a failed search. This fallback behavior is important for testing our agent's ability to handle tool failures gracefully.

1.  We define the `search` function with a clear signature and a docstring. As we learned in Lesson 6, the docstring is critical because modern function-calling APIs use it as the description for the tool, helping the LLM understand what the tool does and when to use it.
    ```python
    def search(query: str) -> str:
        """
        A mock search tool that returns predefined results for specific queries.
    
        Args:
            query: The search query.
    
        Returns:
            A string with the search result or a 'not found' message.
        """
        if "eiffel tower" in query.lower():
            return "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France."
        if "capital of france" in query.lower():
            return "Paris is the capital of France and is known for the Eiffel Tower."
        return f"Information about '{query}' was not found."
    ```

2.  To make our tools manageable, we create a `TOOL_REGISTRY`. This dictionary maps the tool's name to its handler function. This registry allows our agent to look up and execute the correct function based on the name provided by the LLM.
    ```python
    TOOL_REGISTRY = {
        "search": search,
    }
    ```

In a production system, you could easily replace this mock function with a real API call to Google Search, Wikipedia, or any domain-specific knowledge base, as long as you preserve the function signature. This modular design is a key principle of building extensible AI agents.

It is good practice to invest the same effort in designing your tool definitions as you would in a human-computer interface (HCI). Think of it as creating a good "agent-computer interface" (ACI). Your tool's name, description, and parameters should be as clear as possible to the LLM. For example, the Anthropic team found that their coding agent made fewer mistakes when a file-editing tool was changed to require absolute filepaths instead of relative ones, making the agent's behavior more reliable [[4]](https://www.anthropic.com/engineering/building-effective-agents).

## Thought Phase: Prompt Construction and Generation

The first phase of the ReAct cycle is "Thought." This is where the agent interprets the user's query and its context, then formulates a plan. This step is a form of AI agent planning, where the model breaks down a high-level goal into smaller, more manageable sub-goals—a process called task decomposition [[10]](https://www.ibm.com/think/topics/ai-agent-planning). To guide this process, we will construct a prompt that instructs the LLM to think step-by-step and decide on its next action.

We will use a prompt template that includes the available tools and the conversation history. The tools are formatted using XML tags, a technique we covered in Lesson 3. This helps the LLM clearly distinguish the tool descriptions from other parts of the prompt.

1.  We start by defining a helper function to format our tool registry into an XML string. Each tool is wrapped in `<tool>` tags, with its name and description (from the docstring) included.
    ```python
    def build_tools_xml_description(tool_registry: dict) -> str:
        """Builds an XML string describing the available tools."""
        xml = "<tools>\n"
        for tool_name, tool_handler in tool_registry.items():
            xml += f'<tool name="{tool_name}">\n'
            xml += f"<description>{tool_handler.__doc__}</description>\n"
            xml += "</tool>\n"
        xml += "</tools>"
        return xml
    ```

2.  Next, we define the prompt template for the thought-generation step. It includes placeholders for the tool descriptions and the ongoing conversation. The instructions guide the model to analyze the context and produce a `thought` explaining its reasoning.
    ```python
    tools_xml = build_tools_xml_description(TOOL_REGISTRY)
    
    PROMPT_TEMPLATE_THOUGHT = f"""
    You are an AI assistant that answers questions by thinking step-by-step and using the available tools.
    
    {tools_xml}
    
    The conversation so far is:
    <conversation>
    {{conversation}}
    </conversation>
    
    Your task is to analyze the conversation and determine the next step.
    If you can answer the question directly, provide the final answer.
    If you need more information, think about which tool to use.
    
    Your output must be a single thought, wrapped in <thought> tags.
    For example:
    <thought>I need to search for the capital of France to answer the user's question.</thought>
    """
    ```
    The resulting prompt template looks like this:
    ```text
    You are an AI assistant that answers questions by thinking step-by-step and using the available tools.
    
    <tools>
    <tool name="search">
    <description>
            A mock search tool that returns predefined results for specific queries.
    
            Args:
                query: The search query.
    
            Returns:
                A string with the search result or a 'not found' message.
            
    </description>
    </tool>
    </tools>
    
    The conversation so far is:
    <conversation>
    {conversation}
    </conversation>
    
    Your task is to analyze the conversation and determine the next step.
    If you can answer the question directly, provide the final answer.
    If you need more information, think about which tool to use.
    
    Your output must be a single thought, wrapped in <thought> tags.
    For example:
    <thought>I need to search for the capital of France to answer the user's question.</thought>
    ```

3.  Finally, we create a function to generate the thought. It formats the prompt with the current conversation history and calls the Gemini API.
    ```python
    def generate_thought(conversation: str, tool_registry: dict) -> str:
        """Generates a thought based on the conversation and available tools."""
        prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation)
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    ```

This function produces a short, purposeful thought that guides the agent's next step. With a coherent thought generated, the agent must now decide whether to call a tool or conclude with a final answer.

## Action Phase: Function Calling and Parsing

The "Action" phase is where the agent decides what to do based on its thought. It can either execute a tool to gather more information or provide a final answer if it has enough context. We will use Gemini's native function calling capabilities to handle this.

As we discussed in Lesson 6, instead of manually crafting prompts with tool signatures, we can pass the function definitions directly to the model's configuration. Gemini automatically extracts the function name, docstring (for the description), and parameter information from the Python function signature. This keeps our system prompt clean and focused on high-level strategy, while the API handles the technical details of tool integration.

This structured approach is a major improvement over first-generation ReAct agents. Early implementations relied on the LLM generating text like `Action: [search("Olivia Wilde boyfriend")]`, which then had to be parsed from the raw output. This method was often brittle and prone to errors. Modern agents that use native function calling are more reliable and efficient [[11]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent).

Our prompt will instruct the agent to decide between using a tool or finishing the task. The model's response will either be a structured `function_call` object or a plain text response indicating the final answer.

1.  First, we define a Pydantic model for our tool calls. This ensures the output is structured and easy to parse.
    ```python
    class ToolCallRequest(BaseModel):
        """A Pydantic model for a tool call request."""
        name: str
        args: dict
    ```

2.  Next, we define constants for our action types. This makes the code more readable and less prone to typos.
    ```python
    ACTION_FINISH = "finish"
    ```

3.  The system prompt for the action phase is focused on decision-making. It tells the agent to use the provided thought and conversation history to choose its next action.
    ```python
    PROMPT_TEMPLATE_ACTION = """
    You are an AI assistant that answers questions by thinking step-by-step and using the available tools.
    Your task is to take the user's query, the conversation history, and your thought, and decide on the next action.
    
    You have two choices:
    1. Use a tool to get more information.
    2. Provide the final answer with the 'finish' action if you have enough information.
    
    The conversation so far is:
    <conversation>
    {conversation}
    </conversation>
    
    Your thought is:
    <thought>
    {thought}
    </thought>
    """
    ```

4.  The `generate_action` function orchestrates this phase. It configures the Gemini client with the available tools from our `TOOL_REGISTRY` and sends the prompt.
    ```python
    def generate_action(
        thought: str, conversation: str, tool_registry: dict
    ) -> Union[ToolCallRequest, str]:
        """Generates an action based on the thought and conversation."""
        prompt = PROMPT_TEMPLATE_ACTION.format(
            conversation=conversation, thought=thought
        )
        tools = list(tool_registry.values())
    
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=genai.types.GenerateContentConfig(tools=tools),
        )
        
        # Check if the model returned a function call
        if hasattr(response.candidates[0].content.parts[0], "function_call"):
            function_call = response.candidates[0].content.parts[0].function_call
            return ToolCallRequest(name=function_call.name, args=dict(function_call.args))
        
        # Otherwise, assume it's a final answer
        return ACTION_FINISH
    ```
    The function then parses the response. If the model returns a `function_call` object, we parse it into our `ToolCallRequest` Pydantic model. If it returns a text response, we assume the agent has decided to finish. This dual-return logic is the core of the action phase.

With the ability to generate thoughts and decide on actions, we now have all the pieces needed to build the main control loop.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop is the engine of our ReAct agent. It orchestrates the entire Thought-Action-Observation cycle, managing the conversation history, executing tools, and processing observations. This loop is what makes the agent autonomous, allowing it to iterate through reasoning steps until it reaches a conclusion.

Image 1: A flowchart illustrating the Theoretical ReAct Agent Design, showing the iterative Thought-Action-Observation loop.

```mermaid
flowchart LR
    A["User Query"] --> B["LLM"]
    B -- "generates" --> C["Thought<br/>(interpreting context)"]
    C --> D{"Done?"}
    D -- "No" --> E["Action<br/>(through a tool)"]
    E -- "interacts with" --> F["External Environment"]
    F -- "produces" --> G["Observation<br/>(tool output)"]
    G -- "feeds back" --> B
    D -- "Yes" --> H["Final Answer"]
```

At its core, this cycle mirrors a classic feedback control loop, a fundamental concept in control theory and engineering. The agent takes an action (the input), sees the result (the observation), compares this new state to its goal, and then generates a new thought to adjust its next action, continuously working to minimize the "error" between its current state and the desired outcome [[12]](https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/11%3A_Control_Architectures/11.01%3A_Feedback_control-_What_is_it_When_useful_When_not_Common_usage.).

To manage the state of the conversation, we will use a "scratchpad," which is simply a list of messages that logs every step of the agent's process. This approach is inspired by the way humans use an "inner monologue" to reason through problems step-by-step [[2]](https://www.ibm.com/think/topics/react-agent). We will define a structured `Message` class to ensure this history is clean and easy to parse.

1.  First, we define an `Enum` for the different roles a message can have and a Pydantic `BaseModel` for the `Message` structure itself. This keeps our scratchpad organized.
    ```python
    class MessageRole(Enum):
        """Enum for the different roles in a conversation."""
        USER = "user"
        THOUGHT = "thought"
        TOOL_REQUEST = "tool_request"
        OBSERVATION = "observation"
        FINAL_ANSWER = "final_answer"
    
    class Message(BaseModel):
        """A Pydantic model for a message in the scratchpad."""
        role: MessageRole
        content: str
    ```

2.  We create a helper function to format the scratchpad (our list of `Message` objects) into a single string that can be passed to the LLM.
    ```python
    def format_scratchpad(scratchpad: list[Message]) -> str:
        """Formats the scratchpad into a string for the LLM."""
        formatted_string = ""
        for msg in scratchpad:
            formatted_string += f"<{msg.role.value}>\n{msg.content}\n</{msg.role.value}>\n"
        return formatted_string
    ```

3.  The core of our agent is the `react_agent_loop` function. It initializes the scratchpad with the user's query and then enters a loop that runs for a maximum number of turns.
    ```python
    def react_agent_loop(
        query: str, tool_registry: dict, max_turns: int = 5, verbose: bool = False
    ):
        """The main control loop for the ReAct agent."""
        scratchpad = [Message(role=MessageRole.USER, content=query)]
    
        for i in range(max_turns):
            turn = i + 1
            if verbose:
                print(f"--- Turn {turn}/{max_turns} ---")
    
            # 1. THOUGHT
            conversation = format_scratchpad(scratchpad)
            thought = generate_thought(conversation, tool_registry)
            scratchpad.append(Message(role=MessageRole.THOUGHT, content=thought))
            if verbose:
                pretty_print.message(scratchpad[-1])
    
            # 2. ACTION
            action = generate_action(thought, conversation, tool_registry)
    
            if isinstance(action, ToolCallRequest):
                scratchpad.append(
                    Message(
                        role=MessageRole.TOOL_REQUEST,
                        content=json.dumps(
                            {"name": action.name, "args": action.args}, indent=2
                        ),
                    )
                )
                if verbose:
                    pretty_print.message(scratchpad[-1])
    
                # 3. OBSERVATION
                tool_handler = tool_registry.get(action.name)
                if tool_handler:
                    try:
                        observation = tool_handler(**action.args)
                    except Exception as e:
                        observation = f"Error executing tool {action.name}: {e}"
                else:
                    observation = f"Tool '{action.name}' not found. Available tools: {list(tool_registry.keys())}"
    
                scratchpad.append(Message(role=MessageRole.OBSERVATION, content=observation))
                if verbose:
                    pretty_print.message(scratchpad[-1])
    
            elif action == ACTION_FINISH:
                final_answer = thought # The last thought is the final answer
                scratchpad.append(
                    Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
                )
                if verbose:
                    pretty_print.message(scratchpad[-1])
                return
    
        # If the loop finishes without a final answer, force one
        final_answer = f"I'm sorry, but I couldn't find an answer after {max_turns} turns."
        scratchpad.append(Message(role=MessageRole.FINAL_ANSWER, content=final_answer))
        if verbose:
            pretty_print.message(scratchpad[-1])
    ```
    Inside the loop, the agent performs the three ReAct phases:
    - **Thought:** It calls `generate_thought` to reason about the next step and appends the thought to the scratchpad.
    - **Action:** It calls `generate_action`. If a tool is requested, it records the request and moves to the observation phase. If the action is to `finish`, it uses the last thought as the final answer and terminates the loop.
    - **Observation:** It executes the requested tool using the `TOOL_REGISTRY`. It handles potential errors, such as a missing tool or an exception during execution. The result (or error message) is added to the scratchpad as an observation.

    If the loop completes without reaching a `finish` action, it generates a default message indicating it could not find an answer within the turn limit. This prevents the agent from running indefinitely. Deciding when and how to end the loop is a key design consideration for any ReAct agent, helping to manage costs, limit latency, and avoid getting stuck in repetitive cycles [[2]](https://www.ibm.com/think/topics/react-agent).

With this control loop, we have a fully functional Re-Act agent. Let's test it to see how it performs on different queries.

## Tests and Traces: Success and Graceful Fallback

Now that we have built the complete ReAct loop, it is time to validate its behavior. We will run two tests: a simple factual query where the mock tool has the answer, and a query where the tool will fail. Analyzing the traces will show us if the agent can successfully use its tool and how it handles failures.

Our first test is a straightforward question: "What is the capital of France?" We expect the agent to use the `search` tool, find the answer in the mock response, and provide it.

1.  We call our `react_agent_loop` with the query and set `verbose=True` to see the full trace.
    ```python
    react_agent_loop(
        query="What is the capital of France?",
        tool_registry=TOOL_REGISTRY,
        max_turns=2,
        verbose=True,
    )
    ```
    The trace shows the agent working as expected:
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
    
    [OBSERVATION]
    Paris is the capital of France and is known for the Eiffel Tower.
    
    --- Turn 2/2 ---
    [THOUGHT]
    I have found the answer. The capital of France is Paris.
    
    [FINAL_ANSWER]
    I have found the answer. The capital of France is Paris.
    ```
    - In **Turn 1**, the agent correctly identifies the need to search and forms a `ToolCallRequest` for `search(query='capital of France')`. The observation confirms that our mock tool returned the correct information.
    - In **Turn 2**, the agent observes that it has the answer and generates a final thought, which becomes the final answer. The loop terminates successfully.

Our second test uses a query our mock tool does not recognize: "What is the capital of Italy?" This will test the agent's ability to handle a "not found" observation and adapt its strategy.

1.  We run the loop again with the new query.
    ```python
    react_agent_loop(
        query="What is the capital of Italy?",
        tool_registry=TOOL_REGISTRY,
        max_turns=2,
        verbose=True,
    )
    ```
    The trace demonstrates the agent's fallback behavior:
    ```text
    --- Turn 1/2 ---
    [THOUGHT]
    I need to find the capital of Italy. I will use the search tool to find this information.
    
    [TOOL_REQUEST]
    {
      "name": "search",
      "args": {
        "query": "capital of Italy"
      }
    }
    
    [OBSERVATION]
    Information about 'capital of Italy' was not found.
    
    --- Turn 2/2 ---
    [THOUGHT]
    The first search failed. I will try a broader search for 'Italy' to see if I can find any relevant information that might lead to the capital.
    
    [TOOL_REQUEST]
    {
      "name": "search",
      "args": {
        "query": "Italy"
      }
    }
    
    [OBSERVATION]
    Information about 'Italy' was not found.
    
    [FINAL_ANSWER]
    I'm sorry, but I couldn't find an answer after 2 turns.
    ```
    - In **Turn 1**, the agent tries to search for "capital of Italy," but the observation shows the information was not found.
    - In **Turn 2**, the agent adapts its strategy. Its thought reflects a new plan: to try a broader search for "Italy." This also fails.
    - Because the loop reaches its `max_turns` limit of 2, the forced final answer is triggered, and the agent admits it could not find the information.

This failure mode is characteristic of the trade-offs in the ReAct architecture. The original paper noted that while reasoning-only approaches like Chain-of-Thought often fail due to factual hallucination, ReAct agents are more grounded but can be derailed by non-informative search results from their tools, which is exactly what happened here [[1]](https://arxiv.org/pdf/2210.03629).

These tests confirm that our from-scratch implementation of the ReAct loop is working correctly. The agent can successfully use tools to find answers and demonstrates basic reasoning to adapt its strategy when a tool fails. This provides a solid foundation for building more complex agents with richer tools and behaviors.

## Conclusion

In this lesson, we have moved from theory to practice by building a complete ReAct agent from scratch. By implementing each component—the tool layer, the thought and action phases, and the orchestrating control loop—you have gained a concrete mental model of how autonomous agents reason and interact with their environment. We have seen how a simple, turn-based loop, powered by a well-structured scratchpad, can create a powerful problem-solving engine.

The ReAct framework offers several key benefits, including versatility in tool use, adaptability to new challenges, and improved explainability due to its step-by-step reasoning trace. Most importantly, by grounding its reasoning in observations from external tools, it significantly reduces the risk of factual hallucination, making agents more accurate and trustworthy [[2]](https://www.ibm.com/think/topics/react-agent).

This hands-on approach is what separates production-grade AI engineering from building simple prototypes. Even if you end up using a framework like LangGraph in production, understanding the underlying mechanics allows you to debug, customize, and extend your agents with confidence [[5]](https://ai.google.dev/gemini-api/docs/langgraph-example). The principles of state management, tool execution, and iterative reasoning are foundational skills you will use to build any advanced AI system. As you move toward production, you will need to manage the trade-offs between reasoning depth, token usage, and latency to control costs and ensure a good user experience [[13]](https://blog.promptlayer.com/benchmarking-gemini-3-1-pro-latency-cost-and-reasoning-trade-offs/).

The simple loop we built is just the beginning. You can extend it with more advanced patterns, such as an "evaluator-optimizer" loop where one agent generates a solution and another critiques it iteratively [[4]](https://www.anthropic.com/engineering/building-effective-agents). These capabilities are powering a new generation of agents that can tackle complex, multi-step tasks in fields like customer support and automated scientific discovery [[14]](https://kempnerinstitute.harvard.edu/research/deeper-learning/from-models-to-scientists-building-ai-agents-for-scientific-discovery/).

## References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv. https://arxiv.org/pdf/2210.03629
- [2] *ReAct Agent*. (n.d.). IBM. https://www.ibm.com/think/topics/react-agent
- [3] *AI Agent Planning*. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [4] *Building effective agents*. (n.d.). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [5] *ReAct agent from scratch with Gemini 2.5 and LangGraph*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [6] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2026). *From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review*. arXiv. https://arxiv.org/pdf/2504.19678
- [7] Shankar, A. (2024, June 20). *Building ReAct Agents from Scratch using Gemini*. Medium. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [8] *AI Agent Orchestration*. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [9] *Function calling*. (n.d.). Google AI for Developers. https://ai.google.dev/gemini-api/docs/function-calling
- [10] *AI Agent Planning*. (n.d.). IBM. https://www.ibm.com/think/topics/ai-agent-planning
- [11] Schmid, P. (2025, March 31). *ReAct agent from scratch with Gemini 2.5 and LangGraph*. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [12] *Feedback control- What is it? When useful? When not? Common usage*. (n.d.). Engineering LibreTexts. https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/11%3A_Control_Architectures/11.01%3A_Feedback_control-_What_is_it_When_useful_When_not_Common_usage.
- [13] *Benchmarking Gemini 3.1 Pro: Latency, Cost, and Reasoning Trade-offs*. (n.d.). PromptLayer. https://blog.promptlayer.com/benchmarking-gemini-3-1-pro-latency-cost-and-reasoning-trade-offs/
- [14] *From Models to Scientists: Building AI Agents for Scientific Discovery*. (n.d.). Kempner Institute Harvard University. https://kempnerinstitute.harvard.edu/research/deeper-learning/from-models-to-scientists-building-ai-agents-for-scientific-discovery/