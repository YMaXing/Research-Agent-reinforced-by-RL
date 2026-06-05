"""
Corrections for preset4: 08_react_practice__var_minimal__preset4
Applies all confirmed errors and borderline resolutions.
"""
import json

BASE = (
    "/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing"
    "/rl_training_data/episodes/08_react_practice__var_minimal__preset4"
)

# ─────────────────────────────────────────────────────────────────────────────
# 1. scores.json
# ─────────────────────────────────────────────────────────────────────────────
with open(f"{BASE}/scores.json", "r", encoding="utf-8") as f:
    scores = json.load(f)

# FollowsGT: now 11 sections (added pre-H2 intro)
# core: 7/11  flow: 4/11  struct: 3/11 (Setup corrected to 1)
# depth: 0   breadth: 1/11 (Control Loop only)  pres: 9/11
scores["ground_truth_core_content"]       = round(7 / 11, 6)   # 0.636364
scores["ground_truth_flow"]               = round(4 / 11, 6)   # 0.363636
scores["ground_truth_structure"]          = round(3 / 11, 6)   # 0.272727
scores["ground_truth_depth_enhancement"]  = 0.0
scores["ground_truth_breadth_enhancement"] = round(1 / 11, 6)  # 0.090909
scores["ground_truth_core_preservation"]  = round(9 / 11, 6)   # 0.818182

# UserIntent: now 8 sections (intro + 6 guideline + Conclusion)
# guideline_adherence: 5/8  (intro=1, Setup=1, Tool=1, Thought=0, Action=0, Loop=0, Tests=1, Conc=1)
# research_anchoring:  6/8  (intro=1, Setup=1, Tool=1, Thought=1, Action=0, Loop=0, Tests=1, Conc=1)
# golden_source_priority: 6/8  (intro=1, Setup=1, Tool=1, Thought=1, Action=0, Loop=0, Tests=1, Conc=1)
scores["user_intent_guideline_adherence"]   = round(5 / 8, 6)  # 0.625
scores["user_intent_research_anchoring"]    = round(6 / 8, 6)  # 0.75
scores["user_intent_golden_source_priority"] = round(6 / 8, 6) # 0.75

with open(f"{BASE}/scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, indent=2)
print("✓ scores.json updated")

# ─────────────────────────────────────────────────────────────────────────────
# 2. reasoning.json
# ─────────────────────────────────────────────────────────────────────────────
with open(f"{BASE}/reasoning.json", "r", encoding="utf-8") as f:
    r = json.load(f)

# ── Intro entries to prepend to each FollowsGT metric ──────────────────────

INTRO_CORE = (
    "Introduction:\n"
    "**1:** Both sections introduce the goal of building a minimal ReAct agent from scratch. "
    "The generated section expands on this with additional motivational context (hallucination "
    "risks in pure reasoning, framework complexity trade-offs), but all core ideas from the "
    "expected introduction are present.\n\n"
)

INTRO_FLOW = (
    "Introduction:\n"
    "**0:** The generated section omits the 'Note' callout box present in the expected "
    "introduction, which provides a link to the lesson's GitHub repository. The callout is a "
    "media element whose placement is required; its absence is a flow failure.\n\n"
)

INTRO_STRUCT = (
    "Introduction:\n"
    "**0:** The generated section is missing the 'Note' callout box layout element present in "
    "the expected introduction. The extra prose paragraphs in the generated introduction "
    "(motivational context about hallucination and framework complexity) are accepted supporting "
    "narrative additions and do not constitute a structure failure.\n\n"
)

INTRO_DEPTH = (
    "Introduction:\n"
    "**0:** No depth additions present. The motivational context about hallucination in pure "
    "reasoning describes the core problem that ReAct solves and is part of the basic topic "
    "introduction; it does not constitute a deeper technical exploration or theoretical "
    "foundation beyond the expected section.\n\n"
)

INTRO_BREADTH = (
    "Introduction:\n"
    "**0:** The mention of hallucination risks in pure reasoning (citing the ReAct paper [[1]]) "
    "does not pass the source attribution gate. The ReAct paper is a golden source, not an "
    "exploration source; the specific facts must trace to an exploration-phase source to qualify. "
    "No listed exploration source was found that covers this content. Score is 0 even though the "
    "content could otherwise qualify as adjacent motivational context.\n\n"
)

INTRO_PRES = (
    "Introduction:\n"
    "**1:** The motivational additions (hallucination context, framework complexity trade-offs) "
    "enrich the introduction without diluting the core message of building a ReAct agent from "
    "scratch. The ground truth core remains fully intact.\n\n"
)

r["ground_truth_core_content"]      = INTRO_CORE   + r["ground_truth_core_content"]
r["ground_truth_flow"]              = INTRO_FLOW   + r["ground_truth_flow"]
r["ground_truth_structure"]         = INTRO_STRUCT + r["ground_truth_structure"]
r["ground_truth_depth_enhancement"] = INTRO_DEPTH  + r["ground_truth_depth_enhancement"]
r["ground_truth_breadth_enhancement"] = INTRO_BREADTH + r["ground_truth_breadth_enhancement"]
r["ground_truth_core_preservation"] = INTRO_PRES   + r["ground_truth_core_preservation"]

# ── Fix: ground_truth_flow — Control Loop reason (wrong "omits the diagrams") ─

OLD_CL_FLOW = (
    "The Control Loop: Messages, Scratchpad, Orchestration:\n"
    "**0:** The generated section's flow is different. It introduces the message structure, "
    "then the main loop function, and integrates the observation logic within the loop "
    "description. The expected output has a more structured flow: it introduces the loop "
    "concept with a diagram, explains the scratchpad with an image from the ReAct paper, "
    "defines the message structure, defines a `Scratchpad` class, and then builds the main "
    "loop function piece by piece. The generated version is less structured and omits the diagrams."
)

NEW_CL_FLOW = (
    "The Control Loop: Messages, Scratchpad, Orchestration:\n"
    "**0:** The generated section includes a Mermaid diagram as an accepted substitute for "
    "the first GT static image (the 'Main ReAct Loop' flowchart). However, the flow of ideas "
    "differs significantly: the expected section opens with the flowchart, then introduces the "
    "scratchpad concept via the ReAct paper trace image and its narrative, then defines the "
    "message structure, then the `Scratchpad` class, and finally builds the loop function piece "
    "by piece. The generated section instead opens with a motivational paragraph, then defines "
    "message structure under an H3 header, then loop architecture under a second H3 header, "
    "integrating observation logic within the loop description. The second GT image (the "
    "huyenchip.com paper trace) and its accompanying narrative paragraph are absent. "
    "The overall sequence of ideas deviates from the expected flow."
)

assert OLD_CL_FLOW in r["ground_truth_flow"], "Control Loop flow text not found — check exact string"
r["ground_truth_flow"] = r["ground_truth_flow"].replace(OLD_CL_FLOW, NEW_CL_FLOW)

# ── Fix: ground_truth_structure — Setup (0 → 1, wrong callout reason) ────────

OLD_SETUP_STRUCT = (
    'Setup and Environment:\n'
    '**0:** The generated section omits the initial code block for loading environment '
    'variables and has a different order for the remaining code blocks. Additionally, the '
    'expected output includes a "Note" callout box, which is a distinct layout element '
    'missing from the generated section.'
)

NEW_SETUP_STRUCT = (
    "Setup and Environment:\n"
    "**1:** The generated section adds a short introductory paragraph ('Before we start "
    "building...') before the first code block. This is an accepted supporting narrative "
    "addition and does not constitute a structure failure. The two code blocks (imports and "
    "client/MODEL_ID initialization) are present in the same relative order as the expected "
    "output. No H3 headers or callout layout elements are expected in this section."
)

assert OLD_SETUP_STRUCT in r["ground_truth_structure"], "Setup struct text not found — check exact string"
r["ground_truth_structure"] = r["ground_truth_structure"].replace(OLD_SETUP_STRUCT, NEW_SETUP_STRUCT)

# ── Fix: ground_truth_structure — Control Loop reason (diagrams → H3 subsections) ──

OLD_CL_STRUCT = (
    'The Control Loop: Messages, Scratchpad, Orchestration:\n'
    '**0:** The generated section is missing the two diagrams present in the expected output '
    '("Main ReAct Loop" and the example from the ReAct paper). It also uses a simple list for '
    'the scratchpad instead of the dedicated `Scratchpad` class defined in the expected output, '
    'which is a structural difference in the code.'
)

NEW_CL_STRUCT = (
    "The Control Loop: Messages, Scratchpad, Orchestration:\n"
    "**0:** The generated section introduces three H3 subsections ('Message Structure "
    "Foundation', 'Control Loop Architecture', 'Integrated Observation Processing') that are "
    "entirely absent from the expected output, which presents the control loop as continuous "
    "prose with no H3 headers. This H3-level structure mismatch is the primary failure. The "
    "Mermaid diagram in the generated section is an accepted media substitute and is not a "
    "structural failure; missing media elements in the generated section are also not a "
    "structural failure per the structure criterion."
)

assert OLD_CL_STRUCT in r["ground_truth_structure"], "Control Loop struct text not found — check exact string"
r["ground_truth_structure"] = r["ground_truth_structure"].replace(OLD_CL_STRUCT, NEW_CL_STRUCT)

# ── UserIntent: add intro entry ───────────────────────────────────────────────

INTRO_GA = (
    "Introduction:\n"
    "**1:** The generated introduction is a complementary addition that sets context for the "
    "lesson. It is not penalized for its presence, as the content is closely aligned with the "
    "guideline's stated goals ('Why We Think It's Valuable' and 'What We Are Planning to "
    "Share'). The introduction motivates the lesson effectively and introduces no off-topic "
    "material. No word count target applies to this section.\n\n"
)

INTRO_RA = (
    "Introduction:\n"
    "**1:** The content is well-anchored. The motivation for building from scratch traces to "
    "the article guideline directly. The hallucination claim cites the ReAct paper "
    "([[1]](https://arxiv.org/pdf/2210.03629)), which is present in the research material as "
    "a golden source.\n\n"
)

INTRO_GSP = (
    "Introduction:\n"
    "**1:** The introduction draws its core framing from the article guideline and cites the "
    "ReAct paper ([[1]](https://arxiv.org/pdf/2210.03629)), a golden source. No non-golden "
    "sources are used preferentially, and no priority conflict exists.\n\n"
)

r["user_intent_guideline_adherence"]    = INTRO_GA  + r["user_intent_guideline_adherence"]
r["user_intent_research_anchoring"]     = INTRO_RA  + r["user_intent_research_anchoring"]
r["user_intent_golden_source_priority"] = INTRO_GSP + r["user_intent_golden_source_priority"]

# ── Fix: user_intent_guideline_adherence — Thought Phase (1 → 0) ─────────────

OLD_THOUGHT_GA = (
    "Thought Phase: Prompt construction and generation:\n"
    "**1:** The generated section follows the guideline's requirements. It explains the prompt "
    "construction, including the use of XML for tool descriptions, and the implementation of "
    "the `generate_thought` function. It correctly follows the step-by-step flow from the "
    "notebook's code cells [8], [9], and [10]. The prose word count is approximately 215 "
    "words, which is within the tolerance of the 200-word target. The transition to the "
    "action phase is also present."
)

NEW_THOUGHT_GA = (
    "Thought Phase: Prompt construction and generation:\n"
    "**0:** The generated section omits a required step from the guideline. Code cell [9] "
    "specifies printing `PROMPT_TEMPLATE_THOUGHT` to inspect the formatted output and "
    "explaining it ('XML block with one `<tool name=\"search\">` containing the docstring, "
    "plus the `<conversation>` placeholder'). The generated article includes the template "
    "definition and the `generate_thought` function but skips the print-and-inspect step "
    "entirely. The remaining steps (build_tools_xml_description, PROMPT_TEMPLATE_THOUGHT "
    "definition, generate_thought function) are correctly covered, and the prose word count "
    "(~199 words) is within the target range of 200 \u00b1 25 words [175, 225]."
)

assert OLD_THOUGHT_GA in r["user_intent_guideline_adherence"], "Thought Phase GA text not found"
r["user_intent_guideline_adherence"] = r["user_intent_guideline_adherence"].replace(
    OLD_THOUGHT_GA, NEW_THOUGHT_GA
)

# ── Fix: user_intent_golden_source_priority — Action Phase (1 → 0) ───────────

OLD_ACTION_GSP = (
    "Action Phase: Function calling and parsing:\n"
    "**1:** The generated section's implementation details, including the use of "
    "`FunctionDeclaration.from_callable` and the parsing logic for the model's response, "
    "are based on the lesson notebook, which is the primary golden source. The explanation "
    "of how Gemini's function calling works is also consistent with the golden source Gemini "
    "documentation. Non-golden sources offer alternative implementations but do not override "
    "the notebook's approach."
)

NEW_ACTION_GSP = (
    "Action Phase: Function calling and parsing:\n"
    "**0:** The generated section does not prioritize the golden source. The golden source "
    "lesson notebook specifies `PROMPT_TEMPLATE_ACTION`, `PROMPT_TEMPLATE_ACTION_FORCED`, "
    "`ToolCallRequest`, and `FinalAnswer` Pydantic models with a `force_final` flag in "
    "`generate_action`. The generated section instead uses `types.FunctionDeclaration"
    ".from_callable` with a single `Action` model, a pattern that matches the Gemini "
    "Function Calling Documentation \u2014 an explicitly non-golden 'Other Source' in the "
    "guideline. This constitutes a case where a non-golden source's implementation pattern "
    "overrides the golden source notebook's specified approach."
)

assert OLD_ACTION_GSP in r["user_intent_golden_source_priority"], "Action Phase GSP text not found"
r["user_intent_golden_source_priority"] = r["user_intent_golden_source_priority"].replace(
    OLD_ACTION_GSP, NEW_ACTION_GSP
)

# ── Append Conclusion entries to each UserIntent metric ───────────────────────

CONC_GA = (
    "\n\nConclusion:\n"
    "**1:** The generated conclusion is a complementary addition that summarizes the lesson "
    "and previews future topics (memory, RAG). It is not penalized for its presence, as it "
    "wraps up the lesson's main takeaways in a way consistent with the guideline's 'Concepts "
    "That Will Be Introduced in Future Lessons' section. The content is cohesive and on-topic."
)

CONC_RA = (
    "\n\nConclusion:\n"
    "**1:** The content is well-anchored. The summary of the ReAct iterative loop traces to "
    "the golden source notebook. The forward-looking statements about memory and RAG trace "
    "directly to the 'Concepts That Will Be Introduced in Future Lessons' section of the "
    "guideline. The ReAct paper citation ([[1]]) supports the trade-off claim."
)

CONC_GSP = (
    "\n\nConclusion:\n"
    "**1:** The conclusion's key claims are supported by the ReAct paper (golden source "
    "[[1]]). The forward reference to future lessons is from the guideline itself. No "
    "non-golden sources are used preferentially, and no priority conflict exists."
)

r["user_intent_guideline_adherence"]    = r["user_intent_guideline_adherence"].rstrip("\n")    + CONC_GA  + "\n\n"
r["user_intent_research_anchoring"]     = r["user_intent_research_anchoring"].rstrip("\n")     + CONC_RA  + "\n\n"
r["user_intent_golden_source_priority"] = r["user_intent_golden_source_priority"].rstrip("\n") + CONC_GSP + "\n\n"

# ─────────────────────────────────────────────────────────────────────────────
# 3. Write reasoning.json
# ─────────────────────────────────────────────────────────────────────────────
with open(f"{BASE}/reasoning.json", "w", encoding="utf-8") as f:
    json.dump(r, f, indent=2, ensure_ascii=False)
print("✓ reasoning.json updated")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Quick sanity checks
# ─────────────────────────────────────────────────────────────────────────────
with open(f"{BASE}/scores.json", "r", encoding="utf-8") as f:
    s = json.load(f)
print("\nFinal scores.json:")
for k, v in s.items():
    print(f"  {k}: {v}")

with open(f"{BASE}/reasoning.json", "r", encoding="utf-8") as f:
    rr = json.load(f)
print("\nReasoning section counts (should all start with 'Introduction'):")
for k, v in rr.items():
    starts_with_intro = v.startswith("Introduction:")
    section_count = v.count(":\n**")
    print(f"  {k}: starts_with_intro={starts_with_intro}, section_count={section_count}")
