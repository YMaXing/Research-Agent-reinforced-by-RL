"""Prompt templates and examples for the UserIntent evaluation metric.

This module contains the system prompt template and few-shot examples used
for evaluating how well generated articles follow guidelines, are anchored
in research, and prioritize golden sources across three dimensions (guideline adherence, research anchoring, golden source priority).
"""

from pathlib import Path

from brown.evals.metrics.base import (
    CriterionScore,
    SectionCriteriaScores,
)

from .types import (
    UserIntentArticleScores,
    UserIntentCriteriaScores,
    UserIntentExample,
    UserIntentMetricFewShotExamples,
)

SYSTEM_PROMPT = """You are an expert in Natural Language Processing (NLP) evaluation metrics, specifically trained to 
assess how well generated content follows specific guidelines and incorporates provided research material. 

The AI system you will evaluate takes as input an article guideline (<input>) and research material (<context>), and 
based on these inputs, another large language model (LLM) generates an article (<output>).

Your task is to evaluate whether the generated article (<output>) adheres to the given
user intent structured as an article guideline, is properly anchored in the provided research, and prioritizes golden sources.

## INSTRUCTIONS 

1. You must analyze the given article guideline (<input>), research material (<context>), and 
generated article (<output>) to determine how well the output follows the input guidelines, utilizes the research, 
and prioritizes golden sources.
2. The input, context, and output are in Markdown format.
3. Instead of comparing the outputs as a whole, you will divide the outputs into sections and compare each section 
individually. 
4. The article guideline can range from a comprehensive multi-section outline (with a "Lesson Outline", section titles, 
detailed per-section requirements, and explicit golden source links) to a simple single-question guideline (containing 
only the question the user wants answered, optionally some golden sources, and a few simple constraints such as length, 
format, or citation style). You must handle both extremes and everything in between.
   - **Multi-section guideline:** Look within the guideline for the keyword "Outline" or actual section titles often 
   marked with H2 headers prefixed with "Section". Use these as the expected sections.
   - **Single-section guideline:** If the guideline contains no outline or explicit section divisions, treat the entire 
   guideline as defining a single expected section. The generated article should be evaluated as one section against the 
   full guideline.
5. Since the article guideline reflects the user expectations and intent, you will always use it as the reference point 
to understand which sections from the generated article should be evaluated. You will always use the expected sections as 
the anchor points when making comparisons between sections.
6. When associating a section from the article guideline with one from the generated article, you will first look
for a matching or similar title. If there is no match based solely on the title, you will try to make associations based
on the content of the section. For example, if the expected section has 3 points on how RAG works and
the generated section has 3 points on how RAG works as well, then they are associated even if the titles are different.
If a required section mentioned in the guideline is missing from the generated article, you will assign a score of 
0 to all evaluation criteria.
7. Using the article guideline as an anchor, you will divide the generated article into sections and evaluate each section 
individually against all given criteria.
8. Sections are divided by H2 headers, marked as "##" in Markdown. You will use the headers as separators. 
Anything between two H2 headers constitutes a section. The only valid exception to this rule is the first section, 
the introduction, which sometimes appears between the title and the first H2 header. You will never include the title or 
subtitle as part of the first section.
9. The score can only be an integer value of 0 or 1. For each section, you will assign a binary integer score (0 or 1) based on 
three criteria:
   1. **Guideline Adherence**: For each expected section in the article guideline, you will evaluate whether the generated 
   section follows the specific section requirements outlined in the article guideline:
        - We expect a perfect match between the expected section and the generated section. Intuitively, you can
        think of the section guideline as a sketch, a compressed version of the generated section.
        - Less: If any topic from the expected article guideline is missing from the generated article, you will assign 
        a score of 0.
        - More: If the generated section has additional topics that are NOT related to the expected main idea or topic 
        of that section in the article guideline, you will assign a score of 0. However, if the additional topics are 
        complementary information closely related to the expected main idea or topic of that section (e.g., depth or 
        breadth enrichment from exploration-phase research that supports the section's core subject), this is acceptable 
        and should NOT cause a score of 0.
        - Different Order: Whether a reordering of items listed in the article guideline constitutes a 
        violation depends on whether there is a logical ordering constraint:
          • **No inherent logical order (order-insensitive):** When the guideline lists items that are NOT 
          sequentially dependent, causally related, or arranged in an obvious logical progression given the 
          context (e.g., a list of independent use cases such as "entity extraction, formatting for downstream 
          processing, data validation," or a list of unrelated benefits), the generated section may present 
          those items in any order without penalty, UNLESS the guideline contains an explicit instruction 
          requiring a specific order (e.g., "cover them in the following order" or "start with X, then Y").
          • **Inherent logical order (order-sensitive):** When the guideline lists items that follow a natural 
          logical progression given the context — such as moving from simpler to more complex approaches 
          (e.g., "from scratch using JSON → from scratch using Pydantic → using the Gemini SDK and Pydantic," 
          where the progression goes from a basic format with more manual effort to a higher-level tool that 
          automates more of the work), chronological sequences, prerequisite chains, or any ordering whose 
          rationale is obvious from the subject matter — the generated section MUST follow that order even if 
          the guideline does not explicitly state "cover these in order." Violating such a natural ordering 
          results in a score of 0.
          • When evaluating, first determine whether the listed items have an inherent logical order based on 
          the context, then apply the appropriate rule above.
        - Named Examples and Artifacts: If the article guideline specifies a particular non-trivial named 
        example or artifact — such as a named code class, dataset, algorithm, or API — that plays a central 
        role in illustrating the main idea of the section (not merely mentioned in passing or indirectly 
        implied), the generated section must use that same named example or artifact. Non-trivial means the 
        example is the primary vehicle through which the section's core concept is demonstrated. Using a 
        different named example or artifact for the same central purpose is a content mismatch and scores 0, 
        even if the general technique or teaching point is otherwise similar. For example, if the guideline 
        specifies a `DocumentMetadata` Pydantic class as the central implementation example to showcase how 
        Pydantic structured outputs work, but the generated section instead uses a `RedditThread` class for 
        the same purpose, this is a content mismatch and scores 0.
        - If section constraints are provided, we are looking only for a rough approximation of the length. The exact
        section length criterias are present in the article guideline. Errors of ±100 units are acceptable. Units can
        be words, characters, or reading time. For example, if the expected section length is 100 words and the generated section length 
        is 190 words, you will assign a score of 1. But if the generated section is 230 words, as it exceeds the tolerance range,
        you will assign a score of 0.
   2. **Research Anchoring**: For each expected section in the article guideline, you will evaluate whether the generated 
   section content is based on or derived from the provided research:
        - We expect each section from the generated article to be generated entirely based on the ideas provided
        in the article guideline and the research material. Thus, you can consider both the context and article guideline as the 
        "research", the single source of truth. 
        - **Important:** The research material (<context>) may contain two parts: (a) a clean primary body of 
        deduplicated content presented as a normal markdown document, followed by (b) a "Golden Source Reference" 
        appendix that preserves original source provenance via `<golden_source>` and `<research_source>` XML tags. 
        When a clean primary body exists (i.e., the research material starts with a "# Comprehensive Research Report" 
        heading and contains a "## Golden Source Reference" section), you must evaluate research anchoring ONLY against 
        the clean primary body (everything before the "## Golden Source Reference" heading) plus the article guideline, 
        because the writer workflow generates the article solely based on the article guideline and the clean 
        deduplicated content. The "Golden Source Reference" appendix is used ONLY by the GoldenSourcePriority criterion 
        (see below), NOT for research anchoring.
        - If the research material does NOT have a clean primary body (no "## Golden Source Reference" section), treat 
        the entire research material as the research corpus for this criterion.
        - If any idea from the generated section is not present in the research, you will assign a score of 0.
        - The generated section does not have to contain all the ideas from the research, just a subset of them.
        - If no research is explicitly referenced through citations, you will manually check if the generated section content
        is based solely on the research. Missing explicit citations is valid. What it's critical is all the ideas to
        adhere to the research. Thus, if the generated section content is based solely on the research, while missing citations,
        you will assign a score of 1.
   3. **GoldenSourcePriority**: For each expected section in the article guideline, you will evaluate whether the generated 
   section preferentially uses content from golden sources over non-golden research sources:
        - **Identifying golden vs. non-golden content:** Do NOT rely on the URLs or file paths listed in the article 
        guideline to determine what is golden-source content — those links alone tell you nothing about the actual content. 
        Instead, use the XML provenance tags in the research material (<context>) to identify golden-source content vs. 
        non-golden content:
          • Content wrapped in `<golden_source ...>` tags (with any `type` attribute: `guideline_url`, `guideline_code`, 
          `guideline_youtube`, `local_files`, etc.) is golden-source content.
          • Content wrapped in `<research_source ...>` tags (with any `type` or `phase` attribute: `tavily_results`, 
          `scraped_from_research`, etc.) is non-golden research content.
        - **Evaluation rule:** When golden-source content and non-golden content overlap on the same topic or idea, 
        the generated section must draw primarily from the golden-source content. Non-golden sources must never override, 
        contradict, or dilute golden-source content.
        - The generated section does NOT need to use ALL golden sources — using at least one golden source preferentially 
        for the section's topic is sufficient.
        - Score 1 if golden sources are used preferentially, or if no conflict exists between golden and non-golden 
        content for the section's topic, or if no overlap exists (the section's topic is only covered by one type of source).
        - Score 0 if non-golden sources override, contradict, or significantly dilute golden-source content for the section's topic.
        - **No golden sources available:** If the research material (<context>) contains no `<golden_source>` tags at all 
        (i.e., no golden-source content exists), the GoldenSourcePriority score is automatically 1 for every section, since 
        there is no golden-source content to prioritize.
10. Along with the binary score, you will provide a brief and concise explanation containing the reasoning behind 
the score for each criterion. The score will be used to debug and monitor the evaluation process. Therefore, it is
important to provide thorough reasoning for the score. Since we provide binary scores, the reasoning should always 
contain what is good and what is problematic about the generated section, regardless of the score. For example, if the score 
is 0, the reasoning should also contain what is good about the generated section, such as "the generated section 
contains all the bulleted points from the expected section guideline," and what is problematic, such as "however, it contains an 
additional section on AI Evals that is not present in the guideline." Also, when generating the reasoning for the
research anchoring criterion, you will always mention if the topic comes from the article guideline, context, or both, while
supporting every single claim with evidence from the research. For example, the generated section is correctly anchored in the research,
where the fundamentals on RAG are based on the context, and the specific details on the RAG architecture are based on the article
guideline. When reasoning about golden_source_priority, reference the specific `<golden_source>` tags and their content 
from the research material, and explain whether the generated section drew from them preferentially.
11. Important rules when evaluating:
   - Focus on substance, not superficial formatting differences
   - When comparing **media**, you only care about the placement and the caption of the media. 
    Since media can take many forms such as Mermaid diagrams, images, or URLs, you will completely ignore the 
    content of the media. Based on the section guideline, you will check whether the media is present in the 
    correct place. Based on the caption of the media, you will check whether it is properly anchored in the research.

## CHAIN OF THOUGHT

**Understanding Input:**
1.1. Read and understand the article guideline (<input>) to identify specific requirements, structure, 
content expectations, constraints, and most importantly the expected sections. Determine whether the guideline is a 
multi-section outline or a single-section/question guideline.
1.2. Read and understand the context (<context>) to identify available information, sources, and key findings.
   - Determine whether the research material has a clean primary body followed by a "Golden Source Reference" appendix. 
   If so, note the boundary between the primary body and the appendix.
   - Scan for `<golden_source>` and `<research_source>` XML tags to map golden vs. non-golden content.
1.3. Label the article guideline and the applicable portion of the context as the "research", the single source of truth 
(see the Research Anchoring criterion for which portion of the context applies).
1.4. Read and understand the generated article (<output>) and split it into sections using H2 headers as separators.
1.5. Connect the expected sections from the article guideline to the sections from the generated article.

**Section-by-Section Evaluation:**
2.1. For each section identified in the article guideline, locate its associated section in the generated article, and 
evaluate it against all three criteria. If a section is found in the article guideline and is missing in the generated 
article, you will assign a score of 0 to all evaluation criteria.
2.2. Evaluate guideline adherence between each expected section from the article guideline and the associated section 
from the generated article.
2.3. Evaluate research anchoring by first selecting the sections to evaluate from the article guideline and then 
comparing the generated section to the research, found in the applicable portion of the context and the associated 
section guideline.
2.4. Evaluate golden_source_priority by using the `<golden_source>` and `<research_source>` XML tags in the research 
material to determine whether golden sources were preferentially used when both types of sources cover the same topic.

**Assigning Scores:**
3.1. Based on each section expected from the article guideline, assign a binary score of either 0 or 1 
for all evaluation criteria listed in the instructions:
    - Score 1 if the section clearly follows the requirements detailed in the instructions.
    - Score 0 if it fails to follow the requirements detailed in the instructions.
3.2. Justify why you assigned a score of 0 or 1 with a brief explanation that highlights the reasoning behind the score
based on the given criterion.

## WHAT TO AVOID

- Do not provide scores using the generated output as the reference point to divide into sections. You must always 
use the article guideline as the reference point to divide into sections.
- Do not let other sections influence the score of a section. The score of each section must be determined in complete 
isolation from any other section.
- Do not use the URLs or file paths from the article guideline to determine golden-source content. Always use the 
`<golden_source>` XML tags in the research material.
- Do not penalize complementary exploration-phase content in guideline adherence if it is closely related to the 
section's expected main idea or topic.

## FEW-SHOT EXAMPLES

Here are few-shot examples demonstrating how to compute the scores for each section and criterion:
<few-shot-examples>
{examples}
</few-shot-examples>

## INPUTS

<input>
{input}
</input>

<context>
{context}
</context>

<output>
{output}
</output>

Think through your answer step by step, and provide the requested evaluation.
"""

EXAMPLES_DIR = Path(__file__).parent / "examples"
DEFAULT_FEW_SHOT_EXAMPLES = UserIntentMetricFewShotExamples(
    examples=[
        # ── Lesson 4: Structured Outputs (Deduplicated Research) ────
        UserIntentExample.from_markdown(
            input_file=EXAMPLES_DIR / "04_structured_outputs" / "article_guideline.md",
            context_file=EXAMPLES_DIR / "04_structured_outputs" / "research.md",
            output_file=EXAMPLES_DIR / "04_structured_outputs" / "article_generated.md",
            scores=UserIntentArticleScores(
                sections=[
                    SectionCriteriaScores(
                        title="Introduction",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline requires a 'Quick reference to what we've learned in "
                                    "previous lessons' covering Lesson 1 (AI Engineering & Agent Landscape), "
                                    "Lesson 2 (Workflows vs. Agents), and Lesson 3 (Context Engineering), "
                                    "followed by a transition to structured outputs. The generated introduction "
                                    "jumps directly into structured outputs as 'the bridge between Software 3.0 "
                                    "and Software 1.0' without any reference to previous lessons. None of the "
                                    "three prior lesson topics are mentioned. While the transition to the lesson "
                                    "content and the importance of structured outputs are well-covered, the "
                                    "missing quick reference to Lessons 1-3 constitutes a missing required topic."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "The introduction's content about structured outputs as the bridge between "
                                    "Software 3.0 (LLMs) and Software 1.0 (traditional code) is drawn from the "
                                    "article guideline's 'What We Are Planning to Share' section. The claim "
                                    "about forcing the model's free-form text into a predictable format aligns "
                                    "with the research's Section 1 ('Why Structured Outputs Matter') which "
                                    "discusses native structured output features enabling 'reliable data "
                                    "extraction and easier integration into downstream systems.' The claims "
                                    "about building 'reliable, testable, and maintainable' systems are supported "
                                    "by the research's discussion of production use cases. All ideas are sourced "
                                    "from the research or guideline."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The introduction is based on conceptual framing from the article guideline "
                                    "rather than specific research sources. No golden or non-golden research "
                                    "sources are directly referenced for the structural claims made here, so "
                                    "there is no priority conflict."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Understanding Why Structured Outputs Are Critical",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline requires three numbered use cases: (1) entity extraction "
                                    "for knowledge graphs/GraphRAG, (2) formatting LLM output for downstream "
                                    "processing with a mermaid diagram, (3) data and type validation. The "
                                    "generated section presents entity extraction and the mermaid diagram, but "
                                    "'Data and type validation' is not presented as a distinct third use case — "
                                    "it is mixed into the benefits paragraph about Pydantic. Additionally, the "
                                    "guideline requires a transition paragraph mentioning three implementation "
                                    "approaches (from scratch using JSON, from scratch using Pydantic, using "
                                    "Gemini SDK and Pydantic), which is entirely absent from the generated "
                                    "section. Furthermore, the section includes a full paragraph on GraphRAG "
                                    "architecture ('Unlike traditional RAG systems that rely on vector similarity "
                                    "search, GraphRAG constructs a comprehensive knowledge graph...capturing "
                                    "not just semantic relationships but also explicit entity connections, "
                                    "temporal sequences, and hierarchical structures') that goes far beyond "
                                    "the guideline's brief mention of GraphRAG as an example use case. This "
                                    "constitutes unrelated additional content not tied to the section's main "
                                    "idea. Note: the three benefits (easy to parse, Pydantic checks, reduces "
                                    "regex) appear in a different order than the guideline lists them, but "
                                    "since these benefits are not sequentially dependent and the guideline does "
                                    "not explicitly require them in order, the reordering alone is acceptable."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=0,
                                reason=(
                                    "Most of the section's content is well-anchored: parsing/manipulating "
                                    "benefits come from the research's Section 1, Pydantic validation from "
                                    "Section 2, knowledge graph construction from Section 4, and the mermaid "
                                    "diagram concept from the guideline. However, the section includes two "
                                    "claims not found in the clean primary body of the research (i.e., "
                                    "everything before the '## Golden Source Reference' heading). First, the "
                                    "GraphRAG paragraph claims GraphRAG 'captures not just semantic "
                                    "relationships but also explicit entity connections, temporal sequences, "
                                    "and hierarchical structures' and 'enables more sophisticated reasoning "
                                    "capabilities, allowing the system to traverse relationships between "
                                    "entities, understand causal chains, and maintain context across multiple "
                                    "documents.' The research's Section 4 mentions GraphRAG only briefly for "
                                    "'structured graph traversal and multi-hop reasoning' — the detailed "
                                    "claims about temporal sequences, hierarchical structures, and causal "
                                    "chains are not present. Second, the paragraph about '65% fewer runtime "
                                    "errors in production compared to those relying on free-form text parsing, "
                                    "according to a 2024 Stanford HAI study' is a fabricated statistic not "
                                    "found anywhere in the research or guideline."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section discusses structured output benefits and use cases "
                                    "at a conceptual level. The golden source content in the appendix (Gemini "
                                    "API docs, lesson notebook code, Pydantic article) provides "
                                    "implementation-specific details rather than the theoretical benefits "
                                    "discussed here. The non-golden research sources covering benefits and "
                                    "use cases do not overlap with golden source content on the same topics. "
                                    "No golden source priority conflict exists."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Implementing Structured Outputs from Scratch Using JSON",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section follows the guideline's 8-step structure: "
                                    "(1) defines the client and MODEL_ID, (2) presents the DOCUMENT text, "
                                    "(3) explains the prompt using XML tags, (4) calls the model, (5) shows "
                                    "the raw output with markdown wrappers, (6) explains the "
                                    "extract_json_from_response function (step 5 in the article as a helper), "
                                    "(7) extracts the output, and (8) prints the extracted Python dictionary. "
                                    "All steps are present and appear in the correct order. Word count is "
                                    "approximately 300 words (excluding code)."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "The code examples are from the lesson notebook golden source "
                                    "(guideline_code). The XML tag prompt design is supported by the "
                                    "clean primary body's Section 3 ('Prompt Engineering for Reliable "
                                    "Structured Output') which describes using XML delimiters. The concept "
                                    "of extracting JSON from LLM responses and parsing it into Python "
                                    "dictionaries is consistent with Section 1's discussion of prompt "
                                    "engineering approaches. The article guideline also provides the step "
                                    "sequence. All ideas are anchored in the research or guideline."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    'The lesson notebook (tagged as <golden_source type="guideline_code"> in '
                                    "the appendix) is the primary source for all code examples and the "
                                    "step-by-step walkthrough. Non-golden research sources on prompt "
                                    "engineering provide supplementary conceptual context but do not override "
                                    "the notebook code. Golden source content is used preferentially."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Implementing Structured Outputs from Scratch Using Pydantic",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline explicitly requires 'Using the code examples from the "
                                    "provided Notebook within the <research> tag, use all the code from "
                                    "the 3. Implementing structured outputs from scratch using Pydantic "
                                    "section.' The lesson notebook uses a `DocumentMetadata` Pydantic "
                                    "class with fields summary, tags, keywords, quarter, growth_rate, and "
                                    "nesting examples using `Summary` and `Tag` models. The generated "
                                    "section instead uses a completely different `RedditThread` Pydantic "
                                    "class with fields summary, tags, comments, and nesting with `Comment` "
                                    "and `RedditThreadWithComments`. This substitution means the generated "
                                    "section does not use the notebook code as required. Additionally, "
                                    "guideline step 2 requires a tip about Python's `typing` library and "
                                    "Python 11 syntax — the generated section mentions Python 3.9 instead "
                                    "of Python 11, a minor deviation. The terminology note about "
                                    "'schema/contract' (step 6) and the mention of Gemini/OpenAI using "
                                    "similar techniques (step 8) are present. The TypedDict/dataclass "
                                    "comparison at the end is present. However, the core code examples "
                                    "being entirely replaced constitutes a significant guideline violation."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "Despite using different code examples, the conceptual content is "
                                    "well-anchored. The discussion of Pydantic vs dataclasses/TypedDict is "
                                    "supported by the clean primary body's Section 2, which provides "
                                    "detailed comparisons of runtime validation, type enforcement, and "
                                    "performance tradeoffs. The claim about Pydantic performing 'runtime "
                                    "validation and type coercion' directly matches the research. The "
                                    "schema generation concept is consistent with the research. The code "
                                    "itself, while different from the notebook, demonstrates valid Pydantic "
                                    "patterns that are consistent with research claims about how Pydantic "
                                    "works."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=0,
                                reason=(
                                    'The lesson notebook (tagged as <golden_source type="guideline_code"> '
                                    "in the appendix) defines the canonical code for this section: "
                                    "`DocumentMetadata` with fields summary, tags, keywords, quarter, "
                                    "growth_rate, and nesting via `Summary` and `Tag` classes. The "
                                    "generated section entirely replaces this golden source code with a "
                                    "fabricated `RedditThread` example. The Pydantic article golden source "
                                    '(tagged as <golden_source type="guideline_url" url="https://pydantic'
                                    '.dev/articles/llm-intro">) discusses runtime type enforcement and '
                                    "schema generation for LLM applications, which directly overlaps with "
                                    "the section's topic. Yet the generated section draws its code examples "
                                    "from neither golden source. This is a clear case where golden source "
                                    "content was available and overlapping with the section topic but was "
                                    "not used preferentially."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Implementing Structured Outputs Using Gemini and Pydantic",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline specifies 4 steps: (1) explain the GenerateContentConfig "
                                    "with response_mime_type and response_schema, (2) explain the new "
                                    "simplified prompt, (3) call the model, (4) show the output highlighting "
                                    "response.parsed for direct Pydantic access. The generated section "
                                    "covers steps 1 and 2 (the config and the prompt), but steps 3 and 4 "
                                    "are missing. There is no model call code (e.g., "
                                    "`client.models.generate_content(...)`) and no demonstration of "
                                    "accessing the response via `response.parsed`. The section ends after "
                                    "the prompt, with a generic closing paragraph instead of the required "
                                    "code walkthrough."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "The content that IS present is well-anchored. The GenerateContentConfig "
                                    "usage and response_mime_type parameter come from the Gemini API golden "
                                    "source. The native API advantages (reduced prompt complexity, improved "
                                    "reliability, lower token costs) are supported by the clean primary "
                                    "body's Section 1, which discusses how native structured output APIs "
                                    "'guarantee that generated model responses match a specific, user-defined "
                                    "format.' No fabricated claims are present in the section."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section directly references the Gemini API documentation "
                                    '(tagged as <golden_source type="guideline_url" url="https://ai.google'
                                    '.dev/gemini-api/docs/structured-output">) for the GenerateContentConfig '
                                    "pattern. Despite the section being incomplete (missing steps 3-4), "
                                    "the content that is present preferentially uses the golden source. No "
                                    "non-golden source overrides golden content."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Conclusion: Structured Outputs Are Everywhere",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline requires: (1) emphasize the universality of structured "
                                    "outputs across domains and patterns, (2) transition to future lessons "
                                    "starting with Lesson 5, and (3) reference other future lesson topics "
                                    "including Lessons 6, 7, and 10, noting structured outputs appear in "
                                    "almost all future lessons. The generated conclusion covers the "
                                    "universality of structured outputs across domains (finance, healthcare) "
                                    "and patterns (workflows, agents). However, there is NO mention of the "
                                    "next lesson (Lesson 5) or any future lesson numbers whatsoever. The "
                                    "concluding paragraph about 'adopting a mindset of reliability' is "
                                    "generic filler, not the specific forward-referencing the guideline "
                                    "requires."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "The conclusion synthesizes claims already established in the article. "
                                    "The claim about structured outputs 'appearing universally in nearly "
                                    "every LLM-powered system' is supported by the clean primary body's "
                                    "Section 6 ('Real-World Production Use Cases') which lists multiple "
                                    "domains. The reference to 'any domain from finance to healthcare' "
                                    "matches the research's mention of financial reporting and healthcare "
                                    "data analysis. No new unsupported claims are introduced."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The conclusion does not reference specific research sources. It "
                                    "synthesizes course-level content and makes domain claims supported by "
                                    "non-golden research. No golden sources are available for the specific "
                                    "topic of 'structured outputs are everywhere,' so no priority conflict "
                                    "exists."
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        ),
        # ── Lesson 7: Reasoning & Planning (Non-Deduplicated Research) ──
        UserIntentExample.from_markdown(
            input_file=EXAMPLES_DIR / "07_reasoning_planning" / "article_guideline.md",
            context_file=EXAMPLES_DIR / "07_reasoning_planning" / "research.md",
            output_file=EXAMPLES_DIR / "07_reasoning_planning" / "article_generated.md",
            scores=UserIntentArticleScores(
                sections=[
                    SectionCriteriaScores(
                        title="Introduction",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline's Lesson Outline enumerates 8 sections starting "
                                    "directly with 'What a Non-Reasoning Model Does And Why It Fails on "
                                    "Complex Tasks.' It does not list an Introduction section. The "
                                    "generated article inserts an extra H2 section ('Why Your Agent "
                                    "Needs a Plan: An Introduction to Planning and Reasoning') before "
                                    "Section 1, which has no corresponding entry in the guideline outline "
                                    "and therefore no section-level requirements to evaluate against. "
                                    "Since the guideline is the anchor and provides no specification for "
                                    "an Introduction section, any content present in this extra section "
                                    "cannot achieve a match with the expected structure. The presence of "
                                    "an unrequested H2 section constitutes a structural deviation from "
                                    "the outline; score is 0."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "Although the guideline outline does not specify an Introduction "
                                    "section, the generated intro's content is fully anchored in sources "
                                    "available in this lesson. The claim that the lesson introduces "
                                    "'foundational concepts of planning and reasoning for AI agents' "
                                    "comes from the Global Context ('What We Are Planning to Share'). "
                                    "The description of exploring 'why standard LLMs fall short on "
                                    "complex, multi-step tasks' and learning 'historically important yet "
                                    "still relevant strategies like ReAct and Plan-and-Execute' maps "
                                    "directly to the same section. The framing that understanding these "
                                    "patterns is 'crucial for any AI engineer aiming to build robust, "
                                    "reliable, and intelligent autonomous systems' is drawn from 'Why We "
                                    "Think It's Valuable.' The mention of agents that 'can decompose "
                                    "goals and self-correct' is supported by the research's coverage of "
                                    "advanced agent capabilities (Sources [9]-[14]). No unsupported "
                                    "claims are present."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The introduction is a high-level framing paragraph drawn entirely "
                                    "from the lesson's Global Context and the general research landscape. "
                                    "It makes no specific claims that would require drawing from either "
                                    "golden (<golden_source>) or non-golden (<research_source>) research "
                                    "sources. Since no golden source content overlaps with the purely "
                                    "contextual framing in this paragraph, there is no golden source "
                                    "priority conflict."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="What a Non-Reasoning Model Does And Why It Fails on Complex Tasks",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section covers all required topics from the guideline: "
                                    "uses the 'Technical Research Assistant Agent' recurring example, "
                                    "demonstrates how a non-reasoning model fails on complex tasks "
                                    "(superficial output, no iteration, no sub-goal breakdown, no error "
                                    "recovery), connects to prior lessons (workflows, structured outputs, "
                                    "tools as building blocks), and transitions to Section 2 about teaching "
                                    "models to think. The consequences are clearly outlined. Word count is "
                                    "approximately 280 words, within the 250-350 word range."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "The failure modes described (superficial outputs, no iteration on "
                                    "partial results, no explicit sub-goal breakdown, no error recovery) are "
                                    "directly supported by Source [19] (OpenAI practical guide) in the "
                                    "research, which lists: 'No iteration on partial results,' 'Superficial "
                                    "and weak outputs,' 'No explicit breakdown of sub-goals,' and 'No error "
                                    "recovery.' Source [20] (Athina AI) supplements with additional failure "
                                    "modes. The connection to prior lessons uses course context from the "
                                    "article guideline."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The non-golden Source [19] (OpenAI practical guide) is the primary "
                                    "reference for failure mode content. None of the golden sources "
                                    "(<golden_source> tags for IBM agentic-reasoning, IBM react-agent, "
                                    "IBM orchestration, Anthropic building-effective-agents, or the ReAct "
                                    "paper) discuss failure modes of non-reasoning agents. They focus on "
                                    "what reasoning agents CAN do. Since golden and non-golden sources "
                                    "address different aspects of the topic, no priority conflict exists."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Teaching Models to Think: Chain-of-Thought and Its Limits",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section covers all required topics: explains CoT as "
                                    "having models 'think out loud' (analogous to 'talk to themselves' in "
                                    "the guideline), provides a CoT prompt example for the research "
                                    "assistant task, and clarifies the limitations (plan and answer mixed "
                                    "in a single block, no iterative loop to refine/correct). The "
                                    "transition to Section 3 about separating the two processes is present. "
                                    "Word count is approximately 250 words, within the 250-350 range."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "Chain-of-Thought concepts are well-supported by Sources [17]-[18] "
                                    "(Wei et al. 2022 CoT paper: 'prompting LLMs to produce intermediate "
                                    "reasoning steps before the final answer significantly improves "
                                    "performance' and zero-shot CoT: 'Let\\'s think step by step'). The "
                                    "emergence timeline ('around 2022') matches Source [17]'s publication "
                                    "date. The limitation about mixing planning and answering is discussed "
                                    "in Sources [1]-[2] which contrast single-pass CoT with ReAct's "
                                    "iterative separation."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The golden sources (ReAct paper, IBM sources, Anthropic guide) focus "
                                    "on ReAct, agentic reasoning, and agent orchestration — not on "
                                    "Chain-of-Thought history or methodology. The non-golden CoT papers "
                                    "(Sources [17]-[18]) are the appropriate and only available sources "
                                    "for this section's topic. Since no golden source covers CoT "
                                    "specifically, no priority conflict exists."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Separating Planning from Answering: Foundations of ReAct and Plan-and-Execute",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section covers the core idea of separating "
                                    "planning/reasoning from answering/action as two distinct phases or "
                                    "interleaved steps. It explains why this helps (control, "
                                    "interpretability, iterative loops). It positions ReAct (interleaved "
                                    "Thought-Action-Observation) and Plan-and-Execute (separate planning "
                                    "and execution phases). The transition to Section 4 for ReAct in-depth "
                                    "coverage is present. Word count is approximately 180 words, within "
                                    "the 150-250 range."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "The concept of separating planning from answering is central to "
                                    "Sources [1]-[5]. Source [1] (LangChain planning agents) explicitly "
                                    "discusses 'separating the planning phase from the execution phase.' "
                                    "Source [2] (LangGraph concepts) contrasts ReAct and Plan-and-Execute "
                                    "architectures. The ReAct paper (Source [3], golden) provides the "
                                    "foundational framework for interleaving reasoning and action. All "
                                    "claims in the section are anchored."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The ReAct paper (<golden_source> Source [3]) is referenced for the "
                                    "core concept of reasoning-action interleaving. Non-golden sources "
                                    "supplement with the complementary Plan-and-Execute pattern, which is "
                                    "not covered by any golden source. Golden source content about ReAct "
                                    "is used preferentially for the foundational concept. No priority "
                                    "conflict."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="ReAct in Depth: Loop, Evolving Example, Pros and Cons",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The guideline specifies a detailed 14-step evolving example. Two "
                                    "required elements are missing from the generated section. First, "
                                    "guideline step 4 requires 'Select 3 highly cited, 1 industry report; "
                                    "check publication year and venue' — the generated step 4 instead says "
                                    "'The first three papers seem most relevant based on their titles' "
                                    "without mentioning selecting an industry report or checking publication "
                                    "year and venue. Second, guideline step 8 requires 'Action: "
                                    "summarize_and_compare(extractions)' as a distinct tool call — the "
                                    "generated article omits this action entirely and instead has the "
                                    "conflict appear directly in the fetch_and_extract observation at step "
                                    "6. The mermaid diagram, historical context, pros (interpretability, "
                                    "error recovery), and cons (slower, needs guardrails) are all present "
                                    "and in the correct order. The section reduces the example from 14 "
                                    "steps to 11 steps."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "ReAct concepts are thoroughly supported by the research. Source [3] "
                                    "(golden, ReAct paper) describes the Thought-Action-Observation loop "
                                    "and demonstrates that 'ReAct outperforms both reasoning-only and "
                                    "acting-only approaches.' Source [22] (golden, IBM ReAct agent) "
                                    "provides practical details about the loop and its advantages "
                                    "(interpretability, grounding, adaptability). Source [4] (dev.to) "
                                    "provides the cost comparison data. The evolving example draws from "
                                    "the guideline's recurring scenario and uses research-supported "
                                    "concepts about interleaving reasoning with tools."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section preferentially uses golden sources: the ReAct "
                                    "paper (<golden_source> Source [3]) for the theoretical framework "
                                    "('synergizes reasoning and acting') and IBM ReAct agent "
                                    "(<golden_source> Source [22]) for practical pattern description "
                                    "('interpretability,' 'grounding,' 'adaptability'). The non-golden "
                                    "Source [4] (dev.to) supplements with cost comparison details not "
                                    "covered by any golden source. Golden source content is used for all "
                                    "foundational ReAct concepts."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Plan-and-Execute in Depth: Plan, Execution, Pros and Cons",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section covers all required topics: core concept "
                                    "(upfront plan, sequential execution), mermaid diagram showing the "
                                    "two-phase structure, the evolving example with a 7-step planning "
                                    "phase and step-through execution phase, plan refinement triggers, "
                                    "pros (efficiency, bounded cost/time, clear stage ownership), and cons "
                                    "(inflexibility, risk of rigid adherence). All ideas appear in the "
                                    "expected order. Word count is approximately 480 words, within the "
                                    "450-550 word range."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "Plan-and-Execute concepts are well-supported. Source [1] (LangChain) "
                                    "discusses the separation of 'planner LLM call produces an ordered "
                                    "task list, and a separate executor processes each step.' Source [2] "
                                    "(LangGraph) contrasts with ReAct. Source [4] (dev.to) notes 'more "
                                    "cost-effective for well-defined tasks.' Source [5] (WillowTree) "
                                    "covers planning capabilities, progress tracking, and re-planning "
                                    "challenges. The pros and cons align with the research."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "None of the golden sources specifically discuss Plan-and-Execute in "
                                    "detail. The Anthropic golden source (<golden_source> Source [21]) "
                                    "discusses orchestrator-workers and prompt chaining but not the "
                                    "specific Plan-and-Execute pattern. Non-golden Sources [1], [4], [5] "
                                    "are the appropriate references. Since no golden source covers this "
                                    "topic, no priority conflict exists."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Where This Shows Up in Practice: Deep Research-Style Systems",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section covers all required topics from the guideline: "
                                    "how research-style systems operationalize planning through long-horizon "
                                    "task decomposition, iterative search-read-compare-verify-write cycles, "
                                    "explicit prompts and policies to reduce hallucinations. It connects "
                                    "to the recurring example and ties deep research to both ReAct-like "
                                    "loops and Plan-and-Execute with re-planning. The transition to modern "
                                    "reasoning models is present. Word count is approximately 240 words, "
                                    "within the 200-300 range."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=0,
                                reason=(
                                    "Most of the section's content is well-anchored: Source [15] (Glean) "
                                    "describes '(1) decomposes research question into sub-questions, "
                                    "(2) searches multiple sources, (3) extracts and synthesizes findings, "
                                    "(4) identifies gaps or conflicts, (5) conducts additional targeted "
                                    "searches, (6) generates a final structured report.' Source [16] "
                                    "(serjhenrique) discusses hybrid architectures blending ReAct and "
                                    "Plan-and-Execute. However, the section includes a fabricated "
                                    "statistic: 'A 2024 survey by MIT CSAIL found that 78% of production "
                                    "deep research systems now use a hybrid ReAct/Plan-and-Execute "
                                    "architecture, with the remaining 22% relying on pure "
                                    "Plan-and-Execute.' This claim with specific percentages attributed "
                                    "to MIT CSAIL is not present anywhere in the research material or "
                                    "the article guideline."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "The Anthropic golden source (<golden_source> Source [21]) discusses "
                                    "the orchestrator-worker pattern, which is conceptually related but "
                                    "distinct from deep research pipeline architectures. The generated "
                                    "section draws from Glean and serjhenrique (non-golden) which discuss "
                                    "deep research AI specifically. The golden and non-golden sources "
                                    "address different levels of specificity, so no direct content overlap "
                                    "or priority conflict exists."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Modern Reasoning Models: Thinking vs. Answer Streams and Interleaved Thinking",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section covers all required topics: two streams "
                                    "(private 'thinking' and public 'answer'), how some models think "
                                    "first then produce output, interleaved thinking after tool calls "
                                    "(updating plan within a single turn), implications for system design "
                                    "(still need guardrails and explicit patterns), and why separation "
                                    "remains useful for debugging and control. The ideas appear in the "
                                    "expected order. Word count is approximately 280 words, within the "
                                    "250-350 range."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "Modern reasoning model concepts are directly supported by Sources "
                                    "[7]-[8] in the research. Source [7] (Claude Extended Thinking) "
                                    "describes 'a private thinking stream where the model breaks down the "
                                    "problem' and 'a public answer stream with the final response.' "
                                    "Source [8] (Claude Interleaved Thinking) explains how 'the model "
                                    "produces thinking blocks not just at the start but also between tool "
                                    "calls.' The claim about baking 'a ReAct-like loop directly into the "
                                    "model\\'s inference process' aligns with Source [8]'s description."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=1,
                                reason=(
                                    "No golden source discusses the internal architecture of modern "
                                    "reasoning models (thinking streams, interleaved thinking). These "
                                    "capabilities are covered by Anthropic's technical documentation "
                                    "(Sources [7]-[8], both <research_source> tagged). The golden and "
                                    "non-golden sources address fundamentally different topics, so no "
                                    "priority conflict exists."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Advanced Agent Capabilities Enabled by Planning: Goal Decomposition and Self-Correction",
                        scores=UserIntentCriteriaScores(
                            guideline_adherence=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section covers goal decomposition and self-correction "
                                    "with the recurring example of conflicting adoption rates (40% vs "
                                    "25%), and connects to next lessons (Lesson 8 ReAct implementation, "
                                    "Lesson 9 memory, Lesson 10 RAG). However, the guideline requires "
                                    "explicit coverage of self-correction 'Techniques: re-prompt with "
                                    "error info, alternative actions, re-evaluate plan, ask for "
                                    "clarification.' The generated section mentions that the agent "
                                    "'inserts a new sub-goal' and 'searches for a more authoritative "
                                    "source' but does not enumerate the four specific techniques listed "
                                    "in the guideline. Additionally, the guideline's 'Why patterns still "
                                    "matter with strong models' subsection requires discussing "
                                    "debuggability (trace Thought/Action/Observation), consistency "
                                    "(explicit control loops), and pedagogy (shared mental model). The "
                                    "generated section touches on these briefly in one sentence but does "
                                    "not develop these three distinct points."
                                ),
                            ),
                            research_anchoring=CriterionScore(
                                score=1,
                                reason=(
                                    "Goal decomposition content is supported by Sources [9]-[11]. Source "
                                    "[9] (golden, IBM agentic reasoning) describes 'Task decomposition — "
                                    "the AI breaks a larger goal into smaller, manageable subtasks.' "
                                    "Source [11] (Amazon Science) discusses hierarchical decomposition. "
                                    "Self-correction is supported by Sources [12]-[14]. Source [13] "
                                    "(Galileo) covers 'agentic self-correction' and feedback loops. "
                                    "The recurring example of conflicting statistics reuses the scenario "
                                    "from LangChain Sources [1]-[2]. The connection to future lessons "
                                    "comes from the article guideline."
                                ),
                            ),
                            golden_source_priority=CriterionScore(
                                score=0,
                                reason=(
                                    "The IBM agentic reasoning golden source (<golden_source> Source [9]) "
                                    "explicitly describes 'Task decomposition — the AI breaks a larger "
                                    "goal into smaller, manageable subtasks, defining clear objectives "
                                    "for each' as the first step of the agentic reasoning loop, and "
                                    "further discusses 'Tool selection,' 'Execution,' 'Evaluation,' and "
                                    "'Self-correction.' This directly overlaps with the goal "
                                    "decomposition and self-correction content in the generated section. "
                                    "However, the generated section's goal decomposition paragraph draws "
                                    "primarily from Source [11] (Amazon Science, <research_source>): "
                                    "'breaking a large, complex task into a hierarchy of smaller, more "
                                    "manageable sub-goals' and cites Amazon's 'hierarchical decomposition "
                                    "where a planner agent breaks a complex goal into a sequence of "
                                    "subtasks.' Since both the golden IBM source and the non-golden "
                                    "Amazon source cover the same topic — goal decomposition — but the "
                                    "generated section primarily uses the non-golden Amazon Science "
                                    "source rather than the golden IBM source, this constitutes a "
                                    "golden source priority violation."
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        ),
    ]
)


def get_eval_prompt(
    input: str,
    context: str,
    output: str,
    few_shot_examples: UserIntentMetricFewShotExamples,
) -> str:
    """Generate the evaluation prompt for the user intent metric."""
    return SYSTEM_PROMPT.format(
        examples=few_shot_examples.to_context(),
        input=input,
        context=context,
        output=output,
    )
