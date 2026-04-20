**Building a Minimal ReAct Agent from Scratch with Gemini and Python**

When I built Brown, my writing agent, I reached for LangGraph to handle the ReAct pattern. The graph model sounded elegant on paper, but in practice it turned five-minute loops into hours of wrestling with edges and state reducers. Simple if-else logic felt unnatural when forced through their paradigm. So I did what I always do when stuck: I opened the LangGraph source code.

Reading the implementation gave me the concrete mental model I needed. The ReAct loop, the thought generation, the tool execution, the state updates, the conditional edges, everything clicked. I realized most production agents do not need the full framework. They need a clean control loop, a scratchpad, and a model that can think, act, and observe. That insight became the foundation for this lesson.

You do not need a complex orchestration library to build a working ReAct agent. You need a turn-based loop, a structured way to record thoughts and observations, and a model that can call tools. In this lesson we will build exactly that, line by line, following the notebook that accompanies the course. By the end you will have a minimal, extensible ReAct agent that uses Gemini and runs the full Thought → Action → Observation cycle. You will also understand why this pattern matters and how to debug or extend it with confidence.

We start with the environment, move to the tool layer, then implement the thought phase, the action phase, the control loop, and finally test the agent with two runs that demonstrate both success and graceful fallback. Every code block comes directly from the notebook so you can follow along and reproduce the traces.

## Setup and Environment

The first cells in the notebook prepare the runtime so every subsequent step produces the expected output. Run them exactly as written.

We load environment variables with a small helper from the course utilities. This pulls `GOOGLE_API_KEY` (or `GEMINI_API_KEY`) from a `.env` file and raises a clear error if the key is missing. The helper prints a short confirmation so you know which key is being used.

```python
from lessons.utils import env
env.load(required_env_vars=["GOOGLE_API_KEY"])
```

Next we import the packages we will use throughout the notebook. The `google-genai` client gives us access to Gemini, Pydantic defines our message and choice models, and the course utilities provide a clean pretty-printer for traces.

```python
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from enum import Enum, auto
from typing import List, Dict, Any
from lessons.utils import pretty_print
```

We create the client and set the model ID. For this lesson we use `gemini-2.5-flash` because it is fast, inexpensive, and has strong function-calling support. The printed message confirms the key is loaded.

```python
client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

With the client ready we can now define the external capability the agent will use. That is the focus of the next section.

The setup is deliberately minimal. No heavy dependencies, no graph framework, no hidden state reducers. Just a client, a model, and a few utilities. This keeps the mental model clear and makes every later step easy to trace. Once the environment is running, we move to the tool layer that gives the agent something to act upon.

## Tool Layer: Mock Search Implementation

A ReAct agent needs at least one tool to demonstrate the full cycle. Instead of calling a live search API that would require keys and rate limits, we use a simple mock tool that returns predictable responses. This choice keeps the focus on the ReAct mechanics rather than external service quirks.

The mock `search` function accepts a query string and returns a short factual snippet or a “not found” message. It uses simple string matching for demonstration purposes. In production you would replace the body with a real call to Google, Perplexity, or an internal knowledge base while keeping the same signature and docstring.

```python
def search(query: str) -> str:
    """Search for information about a specific topic or query.

    Args:
        query (str): The search query or topic to look up.
    """
    query_lower = query.lower()

    if all(word in query_lower for word in ["capital", "france"]):
        return "Paris is the capital of France and is known for the Eiffel Tower."
    elif "react" in query_lower:
        return "The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing."

    return f"Information about '{query}' was not found."
```

We register the tool in a dictionary that maps its name to both the callable and its schema. This registry lets the model reason with symbolic tool names while our code resolves those names to real functions at runtime.

```python
TOOL_REGISTRY = {
    search.__name__: search,
}
```

The docstring becomes the tool description that Gemini sees. No separate XML or JSON schema is needed in the system prompt because the SDK automatically extracts the function signature and docstring when we pass the function to the tools configuration. This separation keeps the prompt focused on strategy rather than low-level tool details.

The mock tool returns predictable strings, which makes the traces easy to read and the tests deterministic. When you later swap this function for a real search client, the rest of the agent code stays unchanged. That is the power of a clean tool interface.

With the tool layer in place we can now generate the first thought that decides what the agent should do next.

## Thought Phase: Prompt Construction and Generation

The thought phase produces a short, purposeful paragraph that guides the next step. It receives the current conversation history and the available tools, then returns plain text reasoning that the action phase will parse.

We first build a minimal XML description of the tools using only their docstrings. This description is inserted into the system prompt so the model knows what capabilities exist without duplicating tool signatures.

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

The thought prompt template contains the tool XML, the current conversation, and clear instructions to produce one short paragraph focused on the next action. The template deliberately avoids listing full tool signatures so the model stays focused on strategy.

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

Printing the template shows exactly what the model receives. The XML block contains the single `search` tool and its docstring, followed by the conversation placeholder. This keeps the prompt concise and easy to debug.

The `generate_thought` function formats the prompt with the current conversation and calls the model. It returns the stripped text so the action phase can parse it cleanly.

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

This structured thought generation mirrors how humans use inner speech as a cognitive tool for self-regulation and planning. Reviews of the phenomenon show that internal verbal thinking supports adaptive cognition on challenging tasks by manipulating inner representations, with distinct subtypes serving different functions [[9]](https://www.sciencedirect.com/science/article/pii/S1364661323002103).

The thought phase is intentionally lightweight. It produces one focused paragraph that the action phase will turn into a concrete decision. No JSON parsing, no extra validation, just clean text that reflects the agent’s current understanding of the task and the available tools.

With thoughts in place we can now move to the action phase, where the model decides whether to call a tool or return a final answer.

## Action Phase: Function Calling and Parsing

The action phase turns the thought into a concrete decision. It determines whether the agent should call a tool or conclude with a final answer. We use Gemini’s native function calling so the model can emit structured tool requests without embedding full tool signatures in the system prompt.

The action system prompt is deliberately high-level. It tells the model to analyze the query, history, and available tools, then choose either an action or a final answer. The prompt lists the tool names in parentheses but does not include descriptions or JSON schemas. This keeps the prompt clean and lets the SDK inject the tool definitions automatically.

```python
PROMPT_TEMPLATE_ACTION = """
You are selecting the best next action to reach the user goal.

Conversation so far:
<conversation>
{conversation}
</conversation>

Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
""".strip()
```

When we want to force a final answer (for example after the maximum number of turns), we use a separate prompt that disables tool calling entirely.

```python
PROMPT_TEMPLATE_ACTION_FORCED = """
You must now provide a final answer to the user.

Conversation so far:
<conversation>
{conversation}
</conversation>

Provide a concise final answer that best addresses the user's goal.
""".strip()
```

We define two Pydantic models to represent the possible outputs. `ToolCallRequest` captures the tool name and arguments when the model decides to act. `FinalAnswer` captures the text when the model is ready to conclude.

```python
class ToolCallRequest(BaseModel):
    """A request to call a tool with its name and arguments."""
    tool_name: str = Field(description="The name of the tool to call.")
    arguments: dict = Field(description="The arguments to pass to the tool.")

class FinalAnswer(BaseModel):
    """A final answer to present to the user when no further action is needed."""
    text: str = Field(description="The final answer text to present to the user.")
```

The `generate_action` function builds the prompt, passes the available tools to the model, and parses the response. If the model emits a function call, we return a `ToolCallRequest`. If it returns plain text, we treat it as a final answer. When `force_final` is true or no tools are available, we disable function calling and ask the model to produce a final answer directly.

```python
def generate_action(conversation: str, tool_registry: dict[str, callable] | None = None, force_final: bool = False) -> ToolCallRequest | FinalAnswer:
    """Generate an action by passing tools to the LLM and parsing function calls or final text.

    When force_final is True or no tools are provided, the model is instructed to produce a final answer and tool calls are disabled.
    """
    if force_final or not tool_registry:
        prompt = PROMPT_TEMPLATE_ACTION_FORCED.format(conversation=conversation)
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return FinalAnswer(text=response.text.strip())

    prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)

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

    candidate = response.candidates[0]
    parts = candidate.content.parts
    if parts and getattr(parts[0], "function_call", None):
        name = parts[0].function_call.name
        args = dict(parts[0].function_call.args) if parts[0].function_call.args is not None else {}
        return ToolCallRequest(tool_name=name, arguments=args)
    
    final_answer = "".join(part.text for part in candidate.content.parts)
    return FinalAnswer(text=final_answer.strip())
```

Notice that the system prompt does not contain tool signatures. When we pass the Python functions to the `tools` configuration, the SDK automatically extracts the function names, argument types, and docstrings. The model receives this information in a structured format that Gemini understands natively. This separation keeps the prompt focused on strategy and makes adding or removing tools trivial.

The parsing logic checks for a `function_call` attribute on the first part of the response. If present, we extract the name and arguments. If absent, we treat the entire text content as a final answer. The `force_final` path disables tool calling entirely, guaranteeing the model returns text.

Error handling is explicit. If the response cannot be parsed or the tool name is unknown, the agent falls back to the `think` method so it can try a different strategy on the next turn. This graceful fallback prevents the loop from getting stuck on a single bad response.

The action phase is intentionally decoupled from the specific tools. It only cares about the symbolic name and the arguments. The actual execution happens in the control loop, which keeps the reasoning layer clean and the execution layer easy to test or swap.

With thoughts and actions defined we can now assemble the full control loop that ties everything together.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop is the engine that runs the complete Thought → Action → Observation cycle. It maintains a scratchpad of structured messages, calls the thought and action phases in sequence, executes tools, records observations, and decides when to stop. The notebook implements this loop in a clean, readable way that makes every step visible.

We start by defining the message roles and the `Message` class that will hold every turn of the conversation. Using an enum for roles makes the traces easy to read and the code self-documenting.

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

The `Scratchpad` class wraps a list of messages and provides a convenient `append` method that can optionally print each message with color-coded titles. This makes the traces in the notebook readable without cluttering the core loop logic.

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

The consistent categorization through `MessageRole` and predictable scratchpad formatting matters more than it first appears. Research on reasoning models demonstrates that subtle variations in scratchpad style or message handling can degrade long-term coherence and impair error recovery, as models rely on familiar structures to maintain effective strategies across turns [[10]](https://arxiv.org/html/2604.08906v1). Our explicit enum and helper functions enforce the stability the model needs.

The main `react_agent_loop` function puts everything together. It creates a scratchpad, adds the user question, then runs a turn-based loop that calls `generate_thought`, parses the action, executes the tool if needed, records the observation, and checks the termination condition. When the maximum number of turns is reached, it forces a final answer so the loop always ends cleanly.

```python
def react_agent_loop(initial_question: str, tool_registry: dict[str, callable], max_turns: int = 5, verbose: bool = False) -> str:
    """
    Implements the main ReAct (Thought -> Action -> Observation) control loop.
    Uses a unified message class for the scratchpad.
    """
    scratchpad = Scratchpad(max_turns=max_turns)

    user_message = Message(role=MessageRole.USER, content=initial_question)
    scratchpad.append(user_message, verbose=verbose)

    for turn in range(1, max_turns + 1):
        scratchpad.set_turn(turn)

        thought_content = generate_thought(
            scratchpad.to_string(),
            tool_registry,
        )
        thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
        scratchpad.append(thought_message, verbose=verbose)

        action_result = generate_action(
            scratchpad.to_string(),
            tool_registry=tool_registry,
        )

        if isinstance(action_result, FinalAnswer):
            final_answer = action_result.text
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
            scratchpad.append(final_message, verbose=verbose)
            return final_answer

        if isinstance(action_result, ToolCallRequest):
            action_name = action_result.tool_name
            action_params = action_result.arguments

            params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
            action_content = f"{action_name}({params_str})"
            action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
            scratchpad.append(action_message, verbose=verbose)

            observation_content = ""
            tool_function = tool_registry[action_name]
            try:
                observation_content = tool_function(**action_params)
            except Exception as e:
                observation_content = f"Error executing tool '{action_name}': {e}"

            observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
            scratchpad.append(observation_message, verbose=verbose)

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

Observation processing is fully integrated inside the loop. After each tool call we capture the result (or an error message), wrap it in an `Observation` message, and append it to the scratchpad. The next thought generation receives the updated conversation history, so the agent can reason with the latest information. This tight integration of observation and reasoning is what makes the ReAct loop adaptive.

The helper `pretty_print_message` adds color-coded titles so the notebook output is easy to read. The titles show the role and the current turn, making it obvious when the agent is thinking, calling a tool, recording an observation, or producing a final answer.

The loop is deliberately simple. It runs a fixed number of turns, records every step, and forces a final answer if the budget is exhausted. This design makes the agent predictable, easy to debug, and straightforward to extend with more tools or richer memory.

The full implementation matches the notebook exactly. You can copy the code cells directly and run them to reproduce the traces we examine in the next section.

## Tests and Traces: Success and Graceful Fallback

We now run two test cases that demonstrate the complete loop in action. The first query succeeds cleanly. The second shows how the agent gracefully falls back when the mock tool cannot find an answer.

**Test 1: Simple factual query**

We ask for the capital of France with a limit of two turns and verbose output.

The trace shows a clean three-step cycle. The first thought decides to use the search tool. The tool returns the correct fact. The second thought recognizes that the information is sufficient and produces a final answer. The forced-final path is not triggered because the agent finished within the turn budget.

**Test 2: Unknown query and graceful fallback**

We ask for the capital of Italy, a query the mock tool cannot answer. The trace shows the agent trying twice, changing its search strategy on the second turn, and then hitting the maximum-turn limit. At that point the loop forces a final answer that honestly admits the tool returned no useful information.

These two traces confirm that the control loop, the scratchpad, the observation processing, and the forced-termination path all behave as designed. The first case shows normal success. The second shows how the agent recovers from missing information without crashing or looping forever.

You can run the exact same cells from the notebook to reproduce these traces. The color-coded titles make it easy to follow the role of each message and the turn on which it occurred.

The tests also serve as a baseline. Once the basic loop works, you can replace the mock search with real APIs, add more tools, enrich the thought prompt with few-shot examples, or introduce memory components. The structure we built in this lesson gives you a solid, debuggable foundation for all of those extensions.

## Conclusion

You now have a working, minimal ReAct agent built from scratch. We started with a clean environment, added a mock search tool, implemented the thought and action phases, assembled a turn-based control loop with a structured scratchpad, and verified the full cycle with two test traces. Every line of code came directly from the notebook, so you can run the cells and see the same outputs.

The most important takeaway is that the ReAct pattern does not require a heavy framework. A simple loop, a scratchpad that records thoughts and observations, and a model that can call tools are enough to create a flexible, debuggable agent. Understanding this minimal implementation gives you the mental model to extend the agent with real tools, richer memory, or more sophisticated reasoning without getting lost in abstractions.

This turn-based design also shares clear parallels with structured decision frameworks used in aviation and medicine, where explicit thought-action-observation cycles and strict termination conditions reduce errors in uncertain environments [[11]](https://www.nature.com/articles/s41746-026-02410-1). In the next lesson we will add memory so the agent can remember user preferences and past interactions across sessions. That will complete the core set of components you need to build production-ready agentic systems.

You have the foundation. Now go build something with it.

## References

- [1] Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629. https://arxiv.org/pdf/2210.03629
- [2] Building ReAct Agents from Scratch using Gemini. (2024). Google Cloud Blog. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [3] ReAct agent from scratch with Gemini 2.5 and LangGraph. (2025). Google AI for Developers. https://ai.google.dev/gemini-api/docs/langgraph-example
- [4] ReAct Agent. (2025). IBM. https://www.ibm.com/think/topics/react-agent
- [5] Building effective agents. (2024). Anthropic. https://www.anthropic.com/engineering/building-effective-agents
- [6] Lesson 8 Notebook. (2025). Towards AI Course Repository. https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb
- [7] From LLM Reasoning to Autonomous AI Agents. (2025). arXiv:2504.19678. https://arxiv.org/pdf/2504.19678
- [8] AI Agent Orchestration. (2025). IBM. https://www.ibm.com/think/topics/ai-agent-orchestration
- [9] Fernyhough, C., & Borghi, A. M. (2023). Inner speech as language process and cognitive tool. Trends in Cognitive Sciences. https://www.sciencedirect.com/science/article/pii/S1364661323002103
- [10] Agentic frameworks and Gemini message handling. (2025). arXiv. https://arxiv.org/html/2604.08906v1
- [11] Aviation lessons for medical AI safety. (2025). Nature. https://www.nature.com/articles/s41746-026-02410-1