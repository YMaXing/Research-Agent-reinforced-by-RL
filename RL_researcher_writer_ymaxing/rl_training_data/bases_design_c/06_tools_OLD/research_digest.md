# Exploitation Digest — Tools

## 1. Source Inventory

### Golden Sources
| Source | Type | Key Contributions |
|--------|------|------------------|
| building-ai-agents-from-scratch-part-1-tool-use.md | web | Details @tool decorator for schema extraction from docstrings/type hints; Agent class with system prompt including tools list, JSON response format (requires_tools, direct_response, tool_calls); examples like convert_currency tool using exchange API; single-step planning limitations; GitHub code (tool_use.ipynb). |
| efficient-tool-use-with-chain-of-abstraction-reasoning.md | web | Chain-of-Abstraction (CoA) for multi-step tool reasoning with placeholders; fine-tuning on GSM8K/HotpotQA (LLaMa-70B, 76.6% math success); tools like SymPy, BM25 retriever; benchmarks (GSM8K: 38.29% vs. baselines +6%; HotpotQA: 28.22%); parallel inference speedup (1.47x math). |
| function-calling-with-openai-s-api.md | web | OpenAI tool calling flow (5 steps: invoke→calls→execute→outputs→response); schemas with tool_choice ("auto"/"required"), parallel_tool_calls; Pydantic/zod helpers; strict mode; tool_search (gpt-5.4+); examples get_weather, custom code_exec/math with grammars; <20 tools limit. |
| function-calling-with-the-gemini-api.md | web | Gemini function calling (OpenAPI schemas, multi-turn/parallel/compositional); GenerateContentConfig with tools=[functions]; AUTO/ANY modes; SDK auto-schema from callables; multimodal (image/pdf); examples schedule_meeting, set_light_values; best practices (temp=0, 10-20 tools); MCP integration. |
| ApoDzZP8_ck.md | youtube | Tool pattern from scratch: XML <tools>/<tool_call> in system prompt; Tool class with inspect.signature; @tool decorator; ToolAgent run loop (prompt→parse XML→validate→execute→observe); examples get_current_weather, fetch_top_hacker_news; frameworks (LangChain, LlamaIndex, CrewAI). |
| towardsai_course-ai-agents.md | code | Full notebook code for lesson: mock tools (search_google_drive, send_discord_message, summarize_financial_report) with schemas; @tool decorator/ToolFunction; TOOL_CALLING_SYSTEM_PROMPT (XML tools); call_tool/extract_tool_call; Gemini config/tools; Pydantic DocumentMetadata; sequential loop; DOCUMENT metrics (20% revenue growth etc.). |

### Exploitation Sources
| Source | Type | Key Contributions |
|--------|------|------------------|
| agentic-design-patterns-part-3-tool-use.md | web | Tool use pattern with _{tool: web-search/python-interpreter}_ syntax; heuristics for 100+ tools (RAG-like); examples web/Wiki/arXiv search, code exec (compound interest); papers (Gorilla 2023, MM-REACT, CoA 2024); more reliable than planning/multi-agent. |
| h8gMhXYAv1k.md | youtube | Traditional/embedded tool calling (client→LLM→execute→feedback); weather API example ("71° in Miami"); downsides (hallucinations); embedded libraries handle execution/retries for reliability. |
| react-vs-plan-and-execute-a-practical-comparison-of-llm-agen.md | web | ReAct (Thought-Action-Observation loop) vs. Plan-and-Execute (LangChain); tools (Search, Calculator, CSVAgent, PythonAstREPLTool); benchmarks (ReAct 85% accuracy/$0.06-0.09 vs. Plan 92%/$0.09-0.14); ReAct for simple/fast tasks. |

### Tavily Exploitation Results
- Total exploitation rounds: 12
- Total queries run: 12
- Per-query yield quality: High overall (avg. 4-5 relevant sources/query); strongest on tool limitations/parallelism (queries 5/8: 10+ sources with benchmarks like 2s latency savings for 5x500ms calls) and prompts/schemas (queries 2/9: precise JSON/OpenAPI examples); weaker on Mermaid (query 11: mostly generic diagramming, few agent-specific flows).

## 2. Per-Section Coverage Analysis

### S1 — Introduction
**Coverage: STRONG**
**What we have:** Golden code (towardsai_course-ai-agents.md) anchors prior lessons (context engineering, structured outputs, chaining/routing/parallel/orchestrator-worker from Lessons 3-5) via notebook imports/constants; golden web (building-ai-agents-from-scratch-part-1-tool-use.md) emphasizes tools transforming LLMs into agents (planning/memory/tools stack); exploitation sources (agentic-design-patterns-part-3-tool-use.md) highlight tool use as core pattern extending token limits. Tavily query 12 sources (e.g., decodingai.com) stress tool calling as foundational AI engineering skill linking to workflows/agents distinction. Gemini/OpenAI docs (function-calling-with-the-gemini-api.md, function-calling-with-openai-s-api.md) provide API evolution context without reintroducing basics.
**Remaining depth gaps:** Specific word-count alignment (135 words) with personal story of tool limitation encounter; exact transition phrasing tying past chaining/routing to tool-enabled autonomy; high-level image sourcing for tool-LLM analogy.
**Remaining breadth gaps:** Course-specific reader journey anchors (e.g., Part 1-4 progression, certification project); voice consistency examples ('we' for team, 'you' for reader).

### S2 — Understanding why agents need tools
**Coverage: STRONG**
**What we have:** Tavily query 1 yields 6 sources (e.g., machinelearningmastery.com: LLMs as pattern matchers needing tools for real-time APIs/databases/calculations; lnu.diva-portal.org: lacks current events/math/company KB; arxiv.org/2507.08034v1: RAG/code exec/APIs for stock/weather; wikipedia.org: tool syntax watching; ibm.com: real-time beyond static training). Golden youtube (ApoDzZP8_ck.md) analogies tools as external access beyond weights; golden web (function-calling-with-the-gemini-api.md) lists use cases (knowledge augment, capabilities extend, actions like scheduling). Exploitation (h8gMhXYAv1k.md) bridges LLM reasoning to world via APIs; all map to LLM-brain/tools-hands analogy, examples (weather/news/DBs/memory/code/math), and 310-word theoretical depth.
**Remaining depth gaps:** Representative image URL/explanation for high-level tool flow; explicit DRY principle tie-in for tool definitions; exact popular tools list (PostgreSQL/Snowflake/S3/memory access/precise calcs).
**Remaining breadth gaps:** 7-year-old analogies for future concepts (e.g., ReAct as "think then act"); non-English tool examples.

### S3 — Implementing tool calls from scratch
**Coverage: STRONG**
**What we have:** Golden code provides full code (imports, Gemini client/MODEL_ID/DOCUMENT, 3 mock tools/schemas, TOOLS/TOOLS_BY_NAME/TOOLS_SCHEMA, TOOL_CALLING_SYSTEM_PROMPT with XML/tools guidelines/format/behavior, extract_tool_call/call_tool, 2 USER_PROMPT examples/responses); golden youtube (ApoDzZP8_ck.md) mirrors XML parsing/execution/feedback; golden web (building-ai-agents-from-scratch-part-1-tool-use.md: Tool dataclass/JSON prompt; function-calling-with-openai-s-api.md: 5-step flow/schemas). Tavily queries 2/6/7/9/10: JSON schemas (agenta.ai: name/desc/params contract; apxml.com: OpenAI format/properties/required; mbrenndoerfer.com: ToolRegistry); fine-tuning (mbrenndoerfer.com: SFT on JSON traces); feedback (news.ycombinator.com: paste observations); prompts (dev.to/simplr_sh: role/tool instructions); registries (decodingai.com: TOOLS_BY_NAME lookup). Exploitation (agentic-design-patterns-part-3-tool-use.md) on clear descs; covers 930-word needs incl. mermaid/decision/generation/theory.
**Remaining depth gaps:** Exact mermaid diagram code for 5-step flow with 3 tools; printed TOOLS_BY_NAME/TOOLS_SCHEMA outputs; LLM response after tool feedback.
**Remaining breadth gaps:** Error handling in extract_tool_call (e.g., invalid JSON); scaling to 50-100 tools prompt.

### S4 — Implementing a tool calling framework from scratch
**Coverage: STRONG**
**What we have:** Golden code details ToolFunction class, tools registry, @tool decorator (Python decorator mechanics), redefined 3 tools_example, registry inspection (name/ToolFunction/schema/handler), tools_by_name/schema mappings; golden web (building-ai-agents-from-scratch-part-1-tool-use.md: @tool/Tool dataclass from docstrings/inspect; ApoDzZP8_ck.md: @tool auto-signature). Tavily query 3: 5 sources on decorators (langchain.com: @tool infer_schema/args_schema/parse_docstring; learn.microsoft.com: @ai_function Pydantic/approval_mode; builder.aws.com: Annotated hints → JSON; dev.to/aws: docstrings for decisions); maps to DRY/modular registry, LLM call/outputs/call_tool for 560 words.
**Remaining depth gaps:** Printed tools registry/first tool inspection outputs; exact LLM response with new schema.
**Remaining breadth gaps:** LangGraph internal similarities (beyond mention); non-Python decorator equivalents (e.g., JS).

### S5 — Implementing production-level tool calls with Gemini
**Coverage: STRONG**
**What we have:** Golden code/web (function-calling-with-the-gemini-api.md): GenerateContentConfig/tools/config (schemas/functions), skip system prompt, auto-schema from callables (search_google_drive/send_discord_message), function_call.args/handler/call_tool; golden web (function-calling-with-openai-s-api.md: analogous tool_choice/parallel). Tavily query 4/16-19: Gemini config (philschmid.de: system_instruction/tools=[pydantic]; ai.google.dev: AUTO/compositional/disable auto; composio.dev: manual loop). Covers reduction to few lines, API extrapolation (OpenAI/Anthropic), 390 words.
**Remaining depth gaps:** Printed function_call object/args outputs; manual tool_handler call output.
**Remaining breadth gaps:** Multi-tool parallel config (e.g., party setup example); strict mode equivalents.

### S6 — Using Pydantic models as tools for on-demand structured outputs
**Coverage: PARTIAL**
**What we have:** Golden code: DocumentMetadata Pydantic, extraction_tool schema from model_json_schema, config/prompt/LLM call, validation; golden web (function-calling-with-the-gemini-api.md: Pydantic direct in tools). Tavily query 4: pydantic.dev: output_type=models but no Gemini tools+structured conflict; swarms.world: tool_schema/multi-model. Mermaid need via query 11 (e.g., awesome-testing.com: flowchart TD user→LLM→tool→loop). Connects Lesson 4, agentic structured use, 315 words.
**Remaining depth gaps:** Exact mermaid for multi-tool loop ending in Pydantic; printed LLM function/args outputs; "Validation successful!" print.
**Remaining breadth gaps:** Non-Gemini Pydantic (e.g., OpenAI pydantic_function_tool); dynamic decision prompts.

### S7 — The downsides of running tools in a loop
**Coverage: STRONG**
**What we have:** Golden code: new config/USER_PROMPT/loop outputs; exploitation (react-vs-plan-and-execute-a-practical-comparison-of-llm-agen.md: ReAct loop limits); Tavily query 5/8/21-25/36-40: sequential limits (aisera.com: no reasoning pauses/planning; codeant.ai: latency for independents, 2s save 5x500ms; promptingguide.ai: infancy challenges; arxiv.org/2603.22862v2: cumulative delays/race conditions; futureagi.substack.com: cascading failures); parallel (codeant.ai: independent fetches like profile/notifications; adk.dev: ParallelAgent sub-agents; kore.ai: 15s→5s multi-DB). Mermaid query 11; ReAct tease, 520 words.
**Remaining depth gaps:** Exact mermaid loop diagram code; printed loop outputs.
**Remaining breadth gaps:** Hybrid ReAct snippets (beyond high-level).

### S8 — Going through popular tools used within the industry
**Coverage: STRONG**
**What we have:** Guideline list matched by golden web/youtube (function-calling-with-the-gemini-api.md: DB/APIs; ApoDzZP8_ck.md: HackerNews; building-ai-agents-from-scratch-part-1-tool-use.md: VectorDBs/ML APIs); exploitation (agentic-design-patterns-part-3-tool-use.md: web/scrape/Python/JS/email/calendar); Tavily query 5: knowledge (vector/DB/text-to-SQL), web (Google/Bing/Brave/scrape), code (Python sandbox/charts), other (APIs/files). Future lessons (9/10 RAG/memory), 340 words.
**Remaining depth gaps:** Grouped list expansions (e.g., graph DBs specifics); enterprise examples (Snowflake/S3).
**Remaining breadth gaps:** Multimodal tools (images/docs, Lesson 11).

### S9 - Conclusion: ...
**Coverage: STRONG**
**What we have:** Tavily query 12: tool calling core skill (decodingai.com: build/debug/monitor; sparkco.ai: evolution to reasoning/memory; composio.dev: I/O layer; galileo.ai: production evals/observability). Golden code transitions to ReAct; future lessons (7 planning/ReAct, 8 implement, 9 memory, 10 RAG), 90 words.
**Remaining depth gaps:** Exact next-lesson phrasing (Lesson 7 theory); slight Part 2/3 refs (LangGraph/MCP/evals/deploy).
**Remaining breadth gaps:** Certification project tie-in.

## 3. Overall Gap Profile
- **Gap counts:** depth_gaps=18, breadth_gaps=13
- **Weakest sections:** S6
- **Strongest sections:** S2, S3, S4, S7, S8, S9
- **Gap character:** Depth gaps cluster around code outputs/diagrams (e.g., mermaids/prints in S3/S6/S7) and prompt specifics, while breadth lacks framework alternatives/multimodal/production edges.
- **Query saturation:** Strong saturation on core mechanics (schemas/decorators/limits) via targeted 12 queries matching guideline gaps, but visualization/voice underrepresented.
- **Key insight for exploration strategy:** Prioritize 3-5 targeted Tavily rounds for Mermaid agent diagrams, code output simulations, and course-voice prompt examples to close visualization/anchoring gaps without redundant schema/tool queries.