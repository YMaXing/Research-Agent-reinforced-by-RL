**Lesson 8: Building a Minimal ReAct Agent from Scratch with Gemini and Python**

We remember the first time we tried to build an agent without a clear picture of the ReAct loop. We kept adding layers, copying code from frameworks, and wondering why the behavior felt unpredictable. The agent would call tools at the wrong moment, lose track of what it had already seen, or simply repeat the same failed steps. That experience taught us a practical lesson: before you can debug or extend an agent, you need to see the entire Thought → Action → Observation cycle working in the simplest possible form. This lesson gives you that foundation. [[1]](https://arxiv.org/pdf/2210.03629)

You will follow the notebook exactly so you can run each cell and see the same traces. You will set up the environment, register a mock search tool, build the thought prompt, add function calling for action selection, implement the turn-based control loop with a structured scratchpad, and run two tests that show both successful reasoning and graceful fallback when the tool returns no results. By the end you will have a working agent and a concrete mental model you can use to understand, debug, and extend more complex agents in later lessons. [[2]](https://ai.google.dev/gemini-api/docs/langgraph-example) [[3]](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)

## Setup and Environment

With the client and model in place, we can define an external capability the agent can use.

Start by loading the environment variables. The helper in `lessons.utils.env.load()` checks for `GOOGLE_API_KEY` (or falls back to `GEMINI_API_KEY`) and raises a clear error if nothing is found. This small habit prevents the frustrating “key not set” failures that waste hours when you are iterating on agents. [[4]](https://ai.google.dev/gemini-api/docs/function-calling)

Next import the packages we will use throughout the lesson. The list is deliberately short: the official Google GenAI client, Pydantic for structured data, Enum and typing helpers, and our pretty-print utility so the traces remain readable.

```python
from google import genai
from pydantic import BaseModel
from enum import Enum
from typing import Dict, Any, List
from lessons.utils import pretty_print
```

Create the client and choose the model. For this lesson we use `gemini-2.5-flash`. It is fast, inexpensive, and has excellent function-calling support. The notebook also prints a helpful message if both `GOOGLE_API_KEY` and `GEMINI_API_KEY` are set so you know which one is being used. These four cells give you a clean, reproducible starting point before any agent logic is written. [[5]](https://www.philschmid.de/langgraph-gemini-2-5-react-agent)

```python
client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

With the environment settled we can move to the first real capability the agent will have: a tool it can call.

## Tool Layer: Mock Search Implementation

A ReAct agent without tools is just a chatbot. We therefore begin by giving it one external capability: search. To keep the lesson focused on the control loop we use a mock tool instead of a live API. This choice is deliberate. A mock removes network flakiness, rate limits, and the need for additional API keys. It also guarantees predictable behavior so the traces you see are stable across runs. In production you would replace the mock with a real call to Google Search, Perplexity, or an internal knowledge base while keeping the exact same function signature and docstring. The agent never knows the difference. [[6]](https://arxiv.org/pdf/2504.19678)

We define the tool as a simple Python function that accepts a query string and returns a short result. The docstring becomes the description the model sees, which is why we write it with care. The function returns a realistic-looking string for common queries and a clear “not found” message otherwise. This fallback behavior teaches the agent how to handle missing information without crashing the loop.

```python
def search(query: str) -> str:
    """Search the internet for information about a topic.
    
    Returns a short snippet or a clear 'not found' message.
    In production this would call a real search API.
    """
    query = query.lower()
    if "france" in query or "paris" in query:
        return "Paris is the capital of France and is known for the Eiffel Tower."
    if "italy" in query or "rome" in query:
        return "Rome is the capital of Italy and is known for the Colosseum."
    return f"Information about '{query}' was not found."
```

We register the tool in a simple dictionary so the loop can look it up by name. We also keep a list of schemas that will be passed to Gemini so the model knows the tool exists and what arguments it expects. The notebook prints the registry so you can verify everything is wired correctly before the first thought is generated.

Relying solely on docstring-driven automatic tool descriptions in Gemini carries limitations. The SDK sends the entire docstring as the top-level function description; argument descriptions from the function signature are not parsed into the generated declaration’s property slots. We therefore write clear, self-contained docstrings and later build an explicit XML description in the thought prompt so the model receives structured guidance. This keeps the implementation simple while ensuring reliable tool selection. In production the same pattern applies when swapping the mock for a live API. [[7]](https://ai.google.dev/gemini-api/docs/prompting-strategies)

With the tool layer complete we have everything the agent needs to act. The next step is to teach it how to think.

## Thought Phase: Prompt Construction and Generation

The Thought phase is where the agent decides what to do next. We do not want the model to improvise freely; we want it to produce a short, purposeful statement that either justifies calling the search tool or explains why it can answer immediately. The notebook shows exactly how to build that prompt.

We first generate an XML description of every registered tool. The helper `build_tools_xml_description` turns the registry into a clean block the model can parse. For our single search tool the output looks like this:

```xml
<tools>
  <tool name="search">
    Search the internet for information about a topic.
    Returns a short snippet or a clear 'not found' message.
  </tool>
</tools>
```

We then define a prompt template that inserts the current conversation history and the tool list. The template ends with an instruction to respond with either a thought plus an action or a final answer. Printing the template before the first run is useful because it shows you exactly what the model sees. You can spot missing context or unclear instructions before you waste tokens on a bad call.

```python
PROMPT_TEMPLATE_THOUGHT = """You are a helpful assistant that can use tools.

{tools}

<conversation>
{conversation}
</conversation>

First think step by step about what to do next. Then either:
- Call a tool using the exact format the model expects, or
- If you have enough information, respond with a final answer.
"""
```

The `generate_thought` function formats the prompt with the current conversation, calls the model, strips whitespace, and returns the text. Because we use a low temperature and a clear system instruction the thoughts are focused and rarely wander. The notebook runs this function on the first user message so you can see the exact thought the model produces before any tool is called.

With thoughts working we now need to turn those thoughts into actions the agent can actually execute.

## Action Phase: Function Calling and Parsing

The Action phase is where the agent decides to call a tool or finish. Gemini’s function-calling feature makes this step clean: we pass the tool declarations in the generation config, the model returns a structured function call object when it wants to act, and we parse that object to decide what to do.

The system prompt for the action phase is deliberately high-level. It tells the model to analyze the query and history, decide whether more information is needed, and respond in a strict JSON format. Crucially, we do **not** embed full tool signatures or parameter schemas in the prompt itself. Gemini extracts that information automatically from the functions we register. This separation keeps the prompt short, reduces token usage, and makes adding or swapping tools trivial. You only update the registry; the prompt stays the same. [[8]](https://ai.google.dev/gemini-api/docs/function-calling)

We configure the generation call with our tool registry and a small temperature so the model stays deterministic. When the response contains a function call we extract the name and arguments. If the model instead returns a direct answer we detect the special `ACTION_FINISH` marker and treat it as the final response. The notebook shows both paths: a successful tool call that returns useful data, and a fallback path when the mock tool cannot find information.

Error handling is built in. If the model returns malformed JSON or an unknown tool name we log the issue and fall back to generating another thought. This prevents the loop from crashing and gives the agent a chance to recover. The trace you see when you run the notebook shows the model changing strategy after the first “not found” observation, exactly as a real agent should.

```python
def decide(self, response: str) -> None:
    try:
        parsed_response = json.loads(response.strip().strip('`').strip())
        if "action" in parsed_response:
            action = parsed_response["action"]
            tool_name = Name[action["name"].upper()]
            self.act(tool_name, action.get("input", self.query))
        elif "answer" in parsed_response:
            self.trace("assistant", f"Final Answer: {parsed_response['answer']}")
        else:
            raise ValueError("Invalid response format")
    except Exception as e:
        logger.error(f"Error processing response: {str(e)}")
        self.think()
```

```python
def act(self, tool_name: Name, query: str) -> None:
    tool = self.tools.get(tool_name)
    if tool:
        result = tool.use(query)
        observation = f"Observation from {tool_name}: {result}"
        self.trace("system", observation)
        self.think()
    else:
        logger.error(f"No tool registered for choice: {tool_name}")
        self.think()
```

With thoughts and actions in place we can finally wire everything together into a working control loop.

## Control Loop: Messages, Scratchpad, Orchestration

The control loop is the heart of the ReAct agent. It repeatedly calls the thought generator, executes the chosen action, records the observation, and decides whether to continue or finish. The notebook implements this as a clean turn-based function that uses a structured scratchpad built from `Message` objects.

Each turn appends a new `Message` with a role that tells us what happened: `user`, `thought`, `tool_request`, `observation`, or `final_answer`. This scratchpad is passed to the thought generator so the model always sees the full history. The loop runs until the agent produces a final answer or hits the maximum number of turns. If the turn limit is reached we force a final answer so the conversation never hangs. [[9]](https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide)

The `react_agent_loop` function ties everything together. It initializes the scratchpad with the user query, then enters a while loop that:

1. Generates a thought using the current scratchpad and tool registry.
2. Parses the thought to decide on an action.
3. If the action is a tool call, it looks up the handler in the registry, runs it with the provided arguments, and records the result as an observation.
4. If the action is to finish, it records the final answer and exits.
5. If the maximum number of turns is reached it forces a final answer with a polite fallback message.

Helper functions format the scratchpad for the prompt and pretty-print each step so the trace is easy to read. The notebook runs the loop on two different queries and prints the complete trace for each. You can see the agent decide to search, receive an observation, update its reasoning, and either answer or gracefully admit it could not find the information.

This control loop is deliberately minimal. It contains no extra memory layers, no vector search, and no complex routing. That simplicity is the point. Once you can follow every line and every printed message you have a solid foundation for adding the more advanced pieces we will cover in later lessons. Historical lessons from early symbolic planning systems like STRIPS show that maintaining kernel sets of required conditions after each step and preferring minimal replanning over full restarts can further improve fallback behavior when observations fail. These ideas align with the graceful termination we built into the loop. [[10]](http://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/stripsrevisit.pdf)

## Tests and Traces: Success and Graceful Fallback

We now run the agent on two concrete examples and study the traces. The first query is straightforward: “What is the capital of France?” We set `max_turns=2` and `verbose=True` so we see every step.

The trace shows the expected flow. In the first turn the model produces a thought that it should use the search tool, issues a function call with the query “capital of France”, receives the observation “Paris is the capital of France and is known for the Eiffel Tower,” and in the second turn decides it has enough information. It outputs a final answer: “Paris is the capital of France.” The entire interaction stays within the turn budget and the tool returns exactly the information needed.

The second query is deliberately harder for our mock tool: “What is the capital of Italy?” The first search returns “Information about ‘capital of Italy’ was not found.” The agent updates its thought, tries a broader query “Italy”, and again receives a not-found message. When the turn limit is reached the loop forces a final answer: “I’m sorry, but I couldn’t find information about the capital of Italy.”

These two traces are the payoff of the entire lesson. You can see the Thought phase producing coherent reasoning, the Action phase correctly calling the tool or deciding to finish, the control loop recording observations in the scratchpad, and the graceful fallback when the tool cannot help. The printed messages match exactly what you will see when you run the notebook cells. They give you a baseline you can compare against when you start modifying the agent.

## Conclusion

You built a minimal ReAct agent from scratch. The goal was to give you a concrete mental model of the Thought-Action-Observation cycle so you can read a trace and know why each message appears. Run the notebook, change the queries, add a second tool, and watch how the traces change. The best way to internalize ReAct is to break it, fix it, and watch the loop adapt. That hands-on experience is what separates engineers who copy frameworks from engineers who can design, debug, and improve agents with confidence.

In the next lesson we will add memory. You will learn how to store procedural instructions, episodic user preferences, and semantic knowledge so the agent can remember across sessions instead of starting from zero every time. The control loop you built today will become the backbone that decides when to retrieve from that memory and how to incorporate the results into the next thought.

## References

- [1] Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. https://arxiv.org/pdf/2210.03629
- [2] Schmid, P. (2025). ReAct Agent from Scratch with Gemini 2.5 and LangGraph. https://www.philschmid.de/langgraph-gemini-2-5-react-agent
- [3] Shankar, A. (2025). Building ReAct Agents from Scratch using Gemini. https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae
- [4] Google AI for Developers. (2025). Function Calling with the Gemini API. https://ai.google.dev/gemini-api/docs/function-calling
- [5] Google AI for Developers. (2025). LangGraph ReAct Example. https://ai.google.dev/gemini-api/docs/langgraph-example
- [6] Ferrag, M. A., Tihanyi, N., & Debbah, M. (2025). From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review. https://arxiv.org/pdf/2504.19678
- [7] Google AI for Developers. (2025). Prompting Strategies. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [8] Pasternak, R. (2025). Building a Python ReAct Agent Class. https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide
- [9] Daily Dose of Data Science. (2025). Implementing ReAct Agentic Pattern From Scratch. https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/
- [10] Fikes, R. E., & Nilsson, N. J. (1993). STRIPS: A Retrospective. http://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/stripsrevisit.pdf
</article>