**Building a Minimal ReAct Agent from Scratch with Python and Gemini**

When I started building Brown, my writing agent, I decided to use LangGraph to implement the ReAct pattern. I embraced their graph model with nodes and edges, thinking it would make everything cleaner. What I discovered was frustrating: simple if-else logic and basic loops that should have taken five minutes became hours of work. I had to force my Python code to fit their graph paradigm, modeling everything through edges in ways that felt unnatural. It did not add real value, just complexity.

After struggling with this, I did what I always do when I am stuck: I opened the LangGraph source code and started reading. That is when everything clicked. Seeing how they actually implemented the ReAct loop, the thought generation, tool execution, state management, and control flow, gave me a concrete mental model I could not get from their documentation. Even though I was not going to use their framework in production, understanding their implementation became the foundation for building my own robust ReAct agent from scratch.

This lesson puts the theory from Lesson 7 into practice. You will build a complete, minimal ReAct agent using only Python and the Gemini API. We will follow the exact notebook structure so you can run every cell alongside the text. By the end you will have a working control loop, a clear understanding of how thoughts, actions, and observations fit together, and the confidence to extend, debug, and customize agents without relying on heavy frameworks.

## Setup and Environment

Start by creating a clean environment so every code cell runs exactly as shown in the notebook. Create a new directory for this lesson and install the required packages.

```bash
mkdir -p react-agent && cd react-agent
pip install google-genai pydantic python-dotenv
```

Next, create a `.env` file with your Gemini API key. The notebook uses a small helper to load it safely.

```python
# lessons/utils/env.py (simplified version used in the notebook)
import os
from dotenv import load_dotenv

def load(required_env_vars=None):
    load_dotenv()
    if required_env_vars:
        missing = [v for v in required_env_vars if not os.getenv(v)]
        if missing:
            raise ValueError(f"Missing environment variables: {missing}")
    print("Environment variables loaded successfully.")
```

Run the helper in the first notebook cell. You should see a confirmation that the key was loaded. The notebook then imports the Gemini client and supporting utilities.

```python
from google import genai
from lessons.utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])

client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

The client is now ready. We chose `gemini-2.5-flash` because it is fast, inexpensive, and has excellent function-calling support. All subsequent cells will reuse this client and model constant. With the environment set up, we can move to the first real component the agent will use: a tool.

## Tool Layer: Mock Search Implementation

Every ReAct agent needs external capabilities. Instead of calling real APIs that require keys and rate limits, we use a simple mock search tool. This keeps the focus on the ReAct loop itself while still giving the agent something realistic to call.

The tool is a single Python function that accepts a query string and returns a short result. For demonstration we hard-code a few responses; any unknown query returns a “not found” message. This mirrors how a real search tool would behave when it cannot locate information.

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

We store the tool in a registry so the agent can look it up by name. The registry also holds the function’s schema so Gemini knows what arguments the tool expects.

```python
TOOL_REGISTRY = {
    search.__name__: search,
}
```

This mock tool is deliberately simple. In production you would replace the body with a real call to Google, Perplexity, or an internal knowledge base. The important part is the contract: the function accepts a string and returns a string. The ReAct loop does not care whether the implementation is a mock or a live API. It only cares that it can call the tool, receive an observation, and continue reasoning.

In clinical decision support systems, the same pattern is adapted to query specialized medical knowledge bases, evidence databases, and diagnostic calculators rather than general web search. [[10]](https://medium.com/@alexglee/building-framework-for-ai-agents-in-healthcare-e6b2c0935c93)

With the tool ready, we can move to the part that decides when and why to use it.

## Thought Phase: Prompt Construction and Generation

The thought phase is where the agent reasons about the current state and decides what to do next. We give the model the conversation history, the available tools, and a clear instruction to output a short paragraph that explains its plan.

The prompt template is built dynamically. We convert the tool registry into a simple XML block so the model sees the tool name and its docstring. The conversation placeholder is filled with the current scratchpad content each turn.

```python
def build_tools_xml_description(tools: dict[str, callable]) -> str:
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

The `generate_thought` function formats the prompt with the current conversation history and calls the model. The returned text is the agent’s internal reasoning for this turn.

```python
def generate_thought(conversation: str, tool_registry: dict[str, callable]) -> str:
    tools_xml = build_tools_xml_description(tool_registry)
    prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation, tools_xml=tools_xml)

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text.strip()
```

This is the first half of the ReAct loop. The model now has a clear, tool-aware thought. The next step is to turn that thought into an actual action or a final answer.

## Action Phase: Function Calling and Parsing

The action phase uses Gemini’s native function calling to decide whether to invoke a tool or return a final answer. The prompt for this phase is deliberately minimal. It does not repeat full tool signatures; it only lists the tool names. The model already received the detailed tool schemas when we configured the client, so the prompt can focus on high-level strategy.

```python
PROMPT_TEMPLATE_ACTION = """
You are selecting the best next action to reach the user goal.

Conversation so far:
<conversation>
{conversation}
</conversation>

Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
""".strip()

PROMPT_TEMPLATE_ACTION_FORCED = """
You must now provide a final answer to the user.

Conversation so far:
<conversation>
{conversation}
</conversation>

Provide a concise final answer that best addresses the user's goal.
""".strip()
```

We define two response schemas: one for tool calls and one for final answers. The model returns structured JSON that we parse into Python objects.

```python
from pydantic import BaseModel, Field

class ToolCallRequest(BaseModel):
    tool_name: str = Field(description="The name of the tool to call.")
    arguments: dict = Field(description="The arguments to pass to the tool.")

class FinalAnswer(BaseModel):
    text: str = Field(description="The final answer text to present to the user.")
```

The `generate_action` function sends the prompt, then inspects the response. If the model produced a function call, we extract the name and arguments. If it produced plain text that matches our finish pattern, we treat it as a final answer. Any parsing error falls back to another thought.

```python
def generate_action(conversation: str, tool_registry: dict[str, callable] | None = None, force_final: bool = False) -> ToolCallRequest | FinalAnswer:
    if force_final or not tool_registry:
        prompt = PROMPT_TEMPLATE_ACTION_FORCED.format(conversation=conversation)
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
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

This design keeps the system prompt clean and lets Gemini’s built-in function-calling handle the heavy lifting of argument validation. The agent can now decide to call the search tool or conclude with a final answer.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop ties everything together. It maintains a scratchpad of messages, calls the thought generator, executes the chosen action, records the observation, and repeats until a final answer is reached or the turn budget is exhausted.

We represent every interaction as a `Message` with a clear role. This makes the history easy to read and debug.

```python
from enum import Enum
from pydantic import BaseModel, Field
from typing import List

class MessageRole(str, Enum):
    USER = "user"
    THOUGHT = "thought"
    TOOL_REQUEST = "tool request"
    OBSERVATION = "observation"
    FINAL_ANSWER = "final answer"

class Message(BaseModel):
    role: MessageRole = Field(description="The role of the message in the ReAct loop.")
    content: str = Field(description="The textual content of the message.")

    def __str__(self) -> str:
        return f"{self.role.value.capitalize()}: {self.content}"
```

The `Scratchpad` class holds the list of messages and provides a convenient way to append new ones while optionally printing them with color-coded titles.

```python
class Scratchpad:
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
                MessageRole.USER: "reset",
                MessageRole.THOUGHT: "orange",
                MessageRole.TOOL_REQUEST: "green",
                MessageRole.OBSERVATION: "yellow",
                MessageRole.FINAL_ANSWER: "cyan",
            }
            header_color = role_to_color.get(message.role, "yellow")
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

The main loop follows the notebook implementation exactly. It starts with the user question, then alternates between generating a thought, deciding on an action, executing the action (or finishing), and recording the observation. If the loop reaches the maximum number of turns, it forces a final answer so the agent never runs indefinitely.

```python
def react_agent_loop(initial_question: str, tool_registry: dict[str, callable], max_turns: int = 5, verbose: bool = False) -> str:
    scratchpad = Scratchpad(max_turns=max_turns)

    user_message = Message(role=MessageRole.USER, content=initial_question)
    scratchpad.append(user_message, verbose=verbose)

    for turn in range(1, max_turns + 1):
        scratchpad.set_turn(turn)

        thought_content = generate_thought(scratchpad.to_string(), tool_registry)
        thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
        scratchpad.append(thought_message, verbose=verbose)

        action_result = generate_action(scratchpad.to_string(), tool_registry=tool_registry)

        if isinstance(action_result, FinalAnswer):
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=action_result.text)
            scratchpad.append(final_message, verbose=verbose)
            return action_result.text

        if isinstance(action_result, ToolCallRequest):
            action_name = action_result.tool_name
            action_params = action_result.arguments

            params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
            action_content = f"{action_name}({params_str})"
            action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
            scratchpad.append(action_message, verbose=verbose)

            observation_content = ""
            tool_function = tool_registry.get(action_name)
            if tool_function:
                try:
                    observation_content = tool_function(**action_params)
                except Exception as e:
                    observation_content = f"Error executing tool '{action_name}': {e}"
            else:
                observation_content = f"Unknown tool: {action_name}. Available tools: {list(tool_registry.keys())}"

            observation_message = Message(role=MessageRole.OBSERVATION, content=str(observation_content))
            scratchpad.append(observation_message, verbose=verbose)

        if turn == max_turns:
            forced_action = generate_action(scratchpad.to_string(), force_final=True)
            final_answer = forced_action.text if isinstance(forced_action, FinalAnswer) else "Unable to produce a final answer within the allotted turns."
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
            scratchpad.append(final_message, verbose=verbose, is_forced_final_answer=True)
            return final_answer
```

The loop is deliberately simple. It uses the same thought and action functions we built earlier, records every step in the scratchpad, and stops cleanly when a final answer is produced or the turn limit is reached. This approach addresses a known limitation where ReAct agents can get stuck repeating the same ineffective thoughts or actions. The original paper recommends limiting the number of steps and falling back to a final answer to prevent infinite loops. [[11]](https://medium.com/@deejairesearcher/react-paper-explained-simply-how-language-models-can-think-and-act-f500395f88db) The `verbose=True` flag prints each step with color-coded titles so you can follow the agent’s reasoning in real time.

## Tests and Traces: Success and Graceful Fallback

With the complete loop in place, we can test two representative queries and examine the printed traces. These tests confirm that the thought generator, action parser, tool execution, observation handling, and forced-termination path all behave as expected.

**Test 1: Simple factual query**

We ask a straightforward question that the mock tool can answer directly.

```python
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The trace shows a clean two-turn flow. In the first turn the agent reasons that it should use the search tool, calls it, and receives the observation “Paris is the capital of France and is known for the Eiffel Tower.” In the second turn it recognizes that it has the answer and emits a final answer. The control loop terminates without hitting the maximum-turn boundary.

**Test 2: Unsupported query that forces fallback**

We now ask about the capital of Italy, a query our mock tool cannot satisfy. This forces the agent to try different strategies and eventually hit the turn limit.

```python
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
```

The trace shows the agent first trying a direct search for “capital of Italy,” receiving “Information about ‘capital of Italy’ was not found.” It then broadens the query to “Italy,” again receiving a not-found response. At the second turn the loop reaches its limit and the forced-final-answer path produces a polite fallback message: “I’m sorry, but I couldn’t find information about the capital of Italy.”

These two traces together verify the end-to-end behavior. The first confirms that a successful path completes quickly and cleanly. The second confirms that the agent adapts its strategy across turns, that observations are recorded correctly, and that the forced-termination path produces a graceful, user-friendly response instead of an error or infinite loop. The graceful fallback when the turn limit is reached is essential for production systems.

You now have a minimal but complete ReAct agent. The notebook cells match the code shown above, so you can run them one by one and see the same colored trace output. The mental model you built—thought, action, observation, scratchpad, and a simple turn-based loop—is the same foundation used by production agent frameworks. You can now extend the agent with real search APIs, add more tools, improve error handling, or plug it into a larger workflow.

In the next lesson we will add memory so the agent can remember user preferences and past interactions across sessions. You will see how the same control loop can be enriched with long-term episodic and semantic memory without changing the fundamental ReAct pattern. Until then, experiment with the notebook, try different queries, and observe how small changes in the thought prompt or tool descriptions affect the agent’s behavior. That hands-on familiarity is the most valuable outcome of this lesson.

## References

- [1] Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629.
- [2] Schmid, P. (2025). ReAct agent from scratch with Gemini 2.5 and LangGraph. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [3] Iusztin, P. (2025). Building Production ReAct Agents From Scratch Is Simple. Decoding AI. https://www.decodingai.com/p/building-production-react-agents
- [4] Google AI for Developers. (2025). ReAct agent from scratch with Gemini 2.5 and LangGraph. https://ai.google.dev/gemini-api/docs/langgraph-example
- [5] Neradot. (2024). Building a Python ReAct Agent Class: A Step-by-Step Guide. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [6] Brownlee, J. (2024). Building ReAct Agents with LangGraph: A Beginner’s Guide. Machine Learning Mastery. https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/
- [7] Daily Dose of DS. (2024). AI Agents Crash Course – Part 10: ReAct Framework with Implementation. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [8] Anthropic. (2024). Building effective agents. https://www.anthropic.com/engineering/building-effective-agents
- [9] IBM. (2025). ReAct Agent. https://www.ibm.com/think/topics/react-agent
- [10] Building Framework for AI Agents in Healthcare. https://medium.com/@alexglee/building-framework-for-ai-agents-in-healthcare-e6b2c0935c93
- [11] ReAct Paper Explained Simply: How Language Models Can Think and Act. https://medium.com/@deejairesearcher/react-paper-explained-simply-how-language-models-can-think-and-act-f500395f88db

(The code and notebook for this lesson are available in the course repository at `lessons/08_react_practice/notebook.ipynb`.)